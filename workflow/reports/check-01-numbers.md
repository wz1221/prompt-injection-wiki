# 檢查報告 01：數字與官方頁面核對

- **檢查日期**：2026-11-23
- **檢查對象**：raw/ 來源筆記與 wiki/ 頁面中的所有研究數據，以及先前無法開啟的官方頁面
- **對應檢查項目**：AGENTS.md §10.1 第 3 項（引用與來源一致；數據類全數核對）
- **時機**：原定第八階段，使用者於 2026-11-23 選擇**提前到製作簡報前**執行，避免錯誤數字被放上投影片
- **方法**：用 Claude Desktop 內建瀏覽器開啟原文（ar5iv／arXiv HTML、Anthropic 官網、NVD、doi.org），以 JavaScript 在頁面全文中搜尋關鍵數字，擷取前後文直接比對。**不再依賴工具摘要。**

## 結果

| # | 來源 | 檢查項目 | 筆記原寫法 | 原文實際內容 | 結果 |
|---|---|---|---|---|---|
| 1 | S3 | 目標劫持／提示洩漏成功率 | 58.6%／23.6% | 58.6 % ± 1.6／23.6 % ± 2.7 | ✅ 通過 |
| 2 | S3 | 模型比較（Table B10） | davinci-002 最高 | ada 13.8、babbage 29.5、curie 23.8、davinci-001 30.5、davinci-002 58.6 | ✅ 通過 |
| 3 | S3 | 反向縮放 | 作者稱之為反向縮放 | 「suggesting the presence of the inverse scaling phenomenon」 | ✅ 通過 |
| 4 | S3 | 疑似引文「virtually impossible」 | 不確定是否逐字 | 原文確有此句 | ✅ 通過（可作為短引用） |
| 5 | S3 | 停止序列、使用者輸入後接文字 | 降低但無法消除 | 60.0→47.5；63.1→51.8 | ✅ 通過 |
| 6 | S3 | 越有害越難 | 越有害成功率越低 | 58.6／49.3／無害 70.0 | ✅ 通過；「與對齊訓練有關」推測未核對 → 不引用 |
| 7 | S5 | <66%、<25%、8% | （先前已核對） | 原文相符 | ✅ 通過 |
| 8 | S5 | 偵測器誤判 | 誤判太多、降低有用性 | 「too many false positives…significantly degrades utility」 | ✅ 通過 |
| 9 | S5 | 工具過濾 7.5%、17% | 7.5%；約 17% | 7.5%；17% of our test cases | ✅ 通過 |
| 10 | S5 | 重複提示不太可能擋住適應性攻擊 | 同 | 「unlikely to withstand adaptive attacks」 | ✅ 通過 |
| 11 | S5 | 反向縮放、GPT-4o 47.69% | 同 | 「more capable models tend to be easier to attack, a form of inverse scaling law」；47.69 | ✅ 通過 |
| 12 | S5 | 受攻擊時有用性下降 10%–25% | 同 | 原文相符 | ✅ 通過 |
| 13 | S5 | 措辭影響 | 攻擊措辭影響成功率 | 第一次搜尋關鍵字找不到 → 第二次以「phrasing」搜到：「variations in prompt injection phrasing can have a large impact」 | ✅ 通過（第二次） |
| 14 | S5 | 某些旅遊任務 0%、猜錯名字減弱攻擊 | 同 | 本次未搜尋到 | ❌ 未核對 → 筆記標「不引用」 |
| 15 | S6 | 圖表數字、100 次嘗試、樣本數 | 13.8／10.7／2.0…1.4% | 原文完全相符 | ✅ 通過 |
| 16 | S6 | 「1%」與「1.4%」 | 頁面內不一致 | 內文寫「A 1% attack success rate」，圖表為 1.4% | ✅ 確認為原文差異；Wiki 用 1.4% |
| 17 | S8 | 多數 >90%、原宣稱接近零 | 同 | 原文相符 | ✅ 通過 |
| 18 | S8 | 聚光燈法／Sandwiching 1% → >95% | 同 | 「as low as 1 %…above 95 % for both defenses」 | ✅ 通過 |
| 19 | S8 | PIGuard 71%、其他偵測器 >90% | 同 | 原文相符 | ✅ 通過 |
| 20 | S8 | 人類紅隊所有情境成功 | 同 | 「human red-teaming succeeds on all of the scenarios while the static attack succeeds on none」 | ✅ 通過 |
| 21 | S8 | 500 人、2 萬美元、40 關 | 同 | 原文相符 | ✅ 通過 |
| 22 | S8 | MetaSecAlign 從宣稱 2% 升到 96% | 同 | 表格中有 96%，但找不到「宣稱 2%」 | ❌ 未核對 → **Wiki 不引用** |
| 23 | S8 | 「通過測試≠證明有效」 | 「通過測試只能證明沒找到破解方法」 | 「empirical evaluations cannot prove that a defense is robust; all it can do is fail to prove that the defense is broken」 | ⚠️ 意思相符但措辭不精確 → **已修正** Wiki 寫法 |
| 24 | S7 | NVD 官方頁面 | CVSS 9.3（嚴重） | **Microsoft 評 9.3（Critical）；NVD 評 7.5（High）**；CWE-74 | ❌ **發現錯誤** → 已修正 |
| 25 | S2 | ACM DOI | 尚未直接開啟 | doi.org 導向 ACM DL 本論文頁 | ✅ 通過 |

## 發現的問題與修正

| 問題 | 嚴重度 | 修正方式 | 修正後結果 |
|---|---|---|---|
| **CVSS 只寫 9.3，未區分評分者**（#24） | 中：與官方資料不一致 | source-07、real-world-cases、glossary 改為兩個分數並列；synthesis 新增「⚠️ 差異 4」 | ✅ 已修正並重新檢查：wiki 中所有「9.3」皆標明為 Microsoft 評分 |
| MetaSecAlign「宣稱 2%」無法核對（#22） | 低：Wiki 原本就未使用 | source-08 標記不引用 | ✅ |
| S5 兩項細節無法核對（#14） | 低：Wiki 未使用 | source-05 標記不引用 | ✅ |
| S8 教訓的措辭不精確（#23） | 低 | defenses.md 改為貼近原文的說法 | ✅ |
| 第一次搜尋漏掉 S5 措辭原句（#13） | 方法問題 | 換關鍵字再搜一次 | ✅ 找到 |

## 修正後重新檢查

- 全專案 `【待逐字核對】` 標記：raw／wiki 中 **0 個**（log.md 的歷史紀錄除外）
- wiki/ 內部連結（含新增的 synthesis 錨點）以程式重新檢查：結果見 log
- 「9.3」出現處：3 處，皆標明為 Microsoft 評分並附 NVD 7.5

## 是否通過

**通過**（第 3 項：數據類引用全數核對）。所有 Wiki 使用的數字都已在原文找到；無法核對的 3 項說法皆未在 Wiki 中使用並已標記。

## 反思素材

1. **工具摘要不等於原文**：第四階段用網頁讀取工具取得的是「小模型的摘要」，數字大致正確，但有 1 項無法在原文找到（#22），1 項措辭被改寫（#23）。
2. **二手報導會簡化資訊**：多家媒體都寫「CVSS 9.3」，但官方頁面其實有兩個分數。
3. **「交叉確認」不夠**：當初用 4 個以上二手來源交叉確認 9.3，但它們很可能都引用同一個來源（Microsoft），所以數量多不等於獨立。
4. **提前檢查值得**：如果照原計畫在簡報完成後才檢查，錯誤的 CVSS 分數很可能已經上了投影片。
