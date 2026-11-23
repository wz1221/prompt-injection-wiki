import sys, json, asyncio
from playwright.async_api import async_playwright
SRC=sys.argv[1]; OUT=sys.argv[2]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1360,'height':840})
        errs=[]
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        pg.on('pageerror',lambda e: errs.append(str(e)))
        reqs=[]
        pg.on('request',lambda r: reqs.append(r.url) if not r.url.startswith('file:') and not r.url.startswith('data:') else None)
        await pg.goto('file://'+SRC); await pg.wait_for_timeout(500)
        N=await pg.evaluate("document.querySelectorAll('.slide').length")
        res={'N':N,'overflow':[],'src_trunc':[]}
        for i in range(N):
            if i>0:
                await pg.keyboard.press('ArrowRight')
            await pg.wait_for_timeout(1300)
            info=await pg.evaluate("""()=>{
              const s=document.querySelector('.slide.active'); const sr=s.getBoundingClientRect();
              const sc=parseFloat(getComputedStyle(document.getElementById('deck')).transform.split('(')[1])||1;
              const bad=[];
              s.querySelectorAll('*').forEach(el=>{
                if(el.closest('.more')||el.classList.contains('more')) return;
                if(el.closest('svg')&&el.tagName.toLowerCase()!=='svg') return;
                if(el.classList.contains('deco')||el.classList.contains('partno')) return;
                const r=el.getBoundingClientRect(); if(r.width===0||r.height===0) return;
                const limitB = el.classList.contains('src')||el.classList.contains('pgno') ? sr.bottom : sr.bottom-46*sc;
                if(r.bottom>limitB+1||r.right>sr.right+1||r.left<sr.left-1) bad.push((el.className||el.tagName)+' b:'+Math.round((r.bottom-sr.bottom)/sc)+' r:'+Math.round((r.right-sr.right)/sc));
                if(el.scrollWidth>el.clientWidth+2 && getComputedStyle(el).overflow!=='visible' && !el.classList.contains('src')) bad.push('scrollX:'+(el.className||el.tagName));
              });
              const src=s.querySelector('.src'); const tr = src && src.scrollWidth>src.clientWidth+1;
              return {title:s.dataset.title,counter:document.getElementById('counter').textContent,bad:bad.slice(0,6),srcTrunc:tr};
            }""")
            if info['bad']: res['overflow'].append({'i':i+1,**info})
            if info['srcTrunc']: res['src_trunc'].append(i+1)
            await pg.screenshot(path=f'{OUT}/s{i+1:02d}.png')
            # open more panel if any
            has=await pg.evaluate("!!document.querySelector('.slide.active .more-btn')")
            if has:
                await pg.click('.slide.active .more-btn'); await pg.wait_for_timeout(450)
                await pg.screenshot(path=f'{OUT}/s{i+1:02d}_more.png')
                await pg.click('.slide.active .more .x'); await pg.wait_for_timeout(350)
        # nav tests
        t={}
        t['end_counter']=await pg.evaluate("document.getElementById('counter').textContent")
        t['next_disabled_at_end']=await pg.evaluate("document.getElementById('btn-next').disabled")
        await pg.keyboard.press('Home'); await pg.wait_for_timeout(300)
        t['home']=await pg.evaluate("document.getElementById('counter').textContent")
        await pg.click('#btn-next'); await pg.wait_for_timeout(300)
        t['btn_next']=await pg.evaluate("document.getElementById('counter').textContent")
        await pg.click('#btn-prev'); await pg.wait_for_timeout(300)
        t['btn_prev']=await pg.evaluate("document.getElementById('counter').textContent")
        await pg.click('#btn-toc'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=f'{OUT}/toc.png')
        await pg.click('#toc a:nth-of-type(20)'); await pg.wait_for_timeout(400)
        t['toc_jump']=await pg.evaluate("document.getElementById('counter').textContent+' '+document.querySelector('.slide.active').dataset.title")
        t['toc_closed']=await pg.evaluate("!document.getElementById('toc').classList.contains('open')")
        # quiz test slide 12
        await pg.goto('file://'+SRC+'#12'); await pg.reload(); await pg.wait_for_timeout(1200)
        qs=pg.locator('.slide.active .quiz-q')
        await qs.nth(0).locator('.opt[data-v="a"]').click(); await pg.wait_for_timeout(200)
        await qs.nth(1).locator('.opt[data-v="a"]').click(); await pg.wait_for_timeout(400)
        t['quiz_fb']=await pg.evaluate("[...document.querySelectorAll('.slide.active .fb')].map(f=>f.textContent)")
        t['quiz_classes']=await pg.evaluate("[...document.querySelectorAll('.slide.active .opt')].map(o=>o.className)")
        await pg.screenshot(path=f'{OUT}/quiz12.png')
        t['hash_load']=await pg.evaluate("document.getElementById('counter').textContent")
        # small viewport
        await pg.set_viewport_size({'width':900,'height':600}); await pg.wait_for_timeout(400)
        await pg.screenshot(path=f'{OUT}/small_viewport.png')
        res['nav']=t; res['console_errors']=errs; res['external_requests']=reqs
        print(json.dumps(res,ensure_ascii=False,indent=1))
        await b.close()
asyncio.run(main())
