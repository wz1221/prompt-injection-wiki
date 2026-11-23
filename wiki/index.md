# Prompt Injection 與 LLM Agent 安全 — Wiki 首頁

> 給一般大眾的入門知識庫，不需要 AI 或資安背景。
> 最後更新：2026-11-23｜來源：9 份（2022–2026）｜所有重要論述皆標示來源 `[S編號, 章節]`

## 這個 Wiki 在講什麼？

AI 助理越來越能幹，可以幫你讀信、上網、整理文件，甚至自己動手做事。但它有一個根本弱點：**分不清「該聽的指令」和「只是要處理的資料」**。有心人只要把指令藏在 AI 會讀到的地方，就可能讓 AI 做出你沒要求的事，這就是**提示注入（Prompt Injection）**。

這個 Wiki 用白話說明它是什麼、為什麼會發生、會造成什麼影響、現在怎麼防，以及為什麼還防不完全。

## 建議閱讀順序

| 順序 | 頁面 | 你會知道什麼 |
|---|---|---|
| 1 | [基本概念](concepts.md) | LLM、Prompt 是什麼？Prompt Injection 為什麼會發生？和越獄有什麼關係？ |
| 2 | [攻擊類型](attack-types.md) | 直接注入 vs 間接注入；指令會藏在哪裡；攻擊想達成什麼 |
| 3 | [Agent 與外部資料風險](agent-security.md) | 網頁、郵件、文件、RAG、工具的風險；致命三要素 |
| 4 | [案例](real-world-cases.md) | 研究示範、產品因應、真實事件 EchoLeak |
| 5 | [防禦與限制](defenses.md) | 怎麼防？為什麼防不完全？一般人可以注意什麼？ |
| 6 | [綜合分析](synthesis.md) | 9 份來源的共同發現、差異與處理方式 |

## 工具頁

- 📖 [術語表](glossary.md)：遇到看不懂的詞先查這裡（約 45 個術語）
- 📝 [建置紀錄](log.md)：這套 Wiki 怎麼一步步建起來的，包括錯誤與修正

## 知識地圖

```
                 ┌──────────────┐
                 │  基本概念     │ 為什麼會發生？
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │  攻擊類型     │ 直接 / 間接
                 └──────┬───────┘
                        ↓
        ┌───────────────┴───────────────┐
        ↓                               ↓
 ┌──────────────┐               ┌──────────────┐
 │ Agent 風險    │ ←── 印證 ───→ │   案例        │
 └──────┬───────┘               └──────┬───────┘
        └───────────────┬───────────────┘
                        ↓
                 ┌──────────────┐
                 │ 防禦與限制    │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │  綜合分析     │ 共同發現與差異
                 └──────────────┘
         （所有頁面的術語 → 術語表）
```

## 最重要的三個結論

1. **根本原因**：AI 分不清指令和資料。[S1, 描述][S2, §1–2][S3, §1] → [基本概念](concepts.md)
2. **目前無法完全防禦**：7 份來源直接指出，另 2 份間接支持（含 1 份真實案例）。（綜合 S1–S9）→ [綜合分析](synthesis.md)
3. **防禦思維的轉變**：從「讓 AI 不被騙」轉向「就算被騙也做不了太大的壞事」。[S1, 防禦][S9, Lockdown] → [防禦與限制](defenses.md)

## 資料來源

| 編號 | 來源 | 作者／機構 | 年份 | 類型 | 可信度 | 網址 |
|---|---|---|---|---|---|---|
| S1 | LLM01:2026 Prompt Injection | OWASP GenAI Security Project | 2026 | 資安組織 | 🟢 | https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ |
| S2 | Not What You've Signed Up For | Greshake, Abdelnabi 等 | 2023 | 論文 | 🟢 | https://arxiv.org/abs/2302.12173 |
| S3 | Ignore Previous Prompt | Perez, Ribeiro | 2022 | 論文 | 🟡 | https://arxiv.org/abs/2211.09527 |
| S4 | NIST AI 100-2e2025 Adversarial Machine Learning | Vassilev 等（NIST） | 2025 | 政府機構 | 🟢 | https://csrc.nist.gov/pubs/ai/100/2/e2025/final |
| S5 | AgentDojo | Debenedetti 等 | 2024 | 論文 | 🟢 | https://arxiv.org/abs/2406.13352 |
| S6 | Mitigating the risk of prompt injections in browser use | Anthropic | 2025 | AI 公司 | 🟡 | https://www.anthropic.com/research/prompt-injection-defenses |
| S7 | EchoLeak（CVE-2025-32711）案例 | Reddy, Gujral；Microsoft／NVD | 2025 | 實際案例 | 🟢／🟡 | https://arxiv.org/abs/2509.10540 |
| S8 | The Attacker Moves Second | Nasr, Carlini 等 | 2025 | 論文 | 🟢 | https://arxiv.org/abs/2510.09023 |
| S9 | Lockdown Mode and Elevated Risk labels | OpenAI | 2026 | AI 公司 | 🟡 | https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/ |

- 可信度：🟢 高（經審查論文、官方文件）／🟡 中（預印本、工作坊論文、AI 公司自家文件）／🟠 需注意（單一來源）
- 歷史版本：S1-2025（OWASP LLM01:2025）
- 每份來源的完整筆記：`raw/source-01.md` … `raw/source-09.md`

## 引用格式說明

- `[S2, §3.1]`：來源 S2 的第 3.1 節
- `（綜合 S1、S3）`：根據多份來源整理出的推論，不是單一來源直接寫的
- `（通識）`：一般常識性說明，不含研究數據或結論
- `> ⚠️ 來源差異`：不同來源說法不一致的地方，以及本 Wiki 的處理方式
