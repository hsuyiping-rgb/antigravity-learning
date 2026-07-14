# NotebookLM 導出內容範本

## 筆記主題：AI Agent 的基礎與應用

### 核心定義
*   **AI Agent (智能代理)**：一種能夠自主規劃、使用工具、並執行複雜任務的 AI 系統。
*   **Planning Mode (規劃模式)**：Agent 在執行任務前，先撰寫計畫並尋求人類審查的工作流程。

### 隨堂測驗題目
Q1: 傳統 AI (如普通對答) 與 AI Agent 的最大差異是什麼？
A) AI Agent 只能聊天
B) AI Agent 具備規劃與呼叫工具自主執行的能力
C) 傳統 AI 不需要網路
D) 兩者完全沒有差異
答案: B

Q2: 在 Antigravity 中，哪一個模式需要人類審查計畫後才能執行程式？
A) 快速模式 (Fast Mode)
B) 規劃模式 (Planning Mode)
C) 程式碼模式 (Code Mode)
D) 靜音模式 (Silent Mode)
答案: B

---

# 📓 AntiGravity Learning：三師爸的 AntiGravity AI Agent 實戰系列筆記

本筆記彙整了 YouTube 頻道「三師爸 Sense Bar」所製作的 **AntiGravity 基本功** 教學影片系列（EP01 - EP08）。此系列影片專門探討如何利用 Google 的 AI Agent 技術（AntiGravity）來協助教師進行備課、行政自動化與教學應用程式開發。

---

## 🎥 影片清單與內容摘要

### 1. **EP01：Google AntiGravity 2.0 實測評價**
*   **主題**：初探 Google 最新推出的 AI Agent 開發代理工具。
*   **內容要點**：
    *   評測其作為 AI 助教的自主執行能力，並與 Claude Code、Codex 等主流工具進行橫向對比。
    *   特別解析其核心的 **Implementation Plan (實作計畫)** 機制，讓使用者在執行代碼前可以編輯與修改計畫，極大提升了 AI 代理任務的準確性。
*   **影片連結**：[前往觀看 EP01](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP01)

### 2. **EP02：備課救星！極速處理教學檔案**
*   **主題**：運用 AI Agent 快速自動化處理教學與行政檔案。
*   **內容要點**：
    *   示範如何讓助教自動下載網路上的考古題 PDF。
    *   使用 OCR 工具自動識別考卷圖形、擷取文字，並一鍵重整為標準格式的 Word 考卷。
    *   與本機的 Obsidian 知識庫進行連動與資料索引。
*   **影片連結**：[前往觀看 EP02](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP02)

### 3. **EP03：最強備課懶人包！寫 GAS 不用再複製貼上**
*   **主題**：串接大腦 (NotebookLM) 與雙手 (AI Agent) 實現自動化部署。
*   **內容要點**：
    *   整合 NotebookLM 作為學習大腦，提供完整的參考資料與脈絡。
    *   將 GitHub、Firebase 與 Netlify 等雲端發布平台納入助教的工具箱。
    *   實作一鍵自動化撰寫與部署 GAS (Google Apps Script) 代碼，解決傳統手動複製貼上程式碼的痛點。
*   **影片連結**：[前往觀看 EP03](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP03)

### 4. **EP04：一鍵將 Gems 全面升級成 Skill 的終極指南**
*   **主題**：將簡易的 Google Gems 升級為擁有程式碼運行能力的 Agent Skill。
*   **內容要點**：
    *   介紹如何將原本只能進行對話的 Gems（提示詞指令），封裝並部署成擁有實際工具調用與 CLI 執行權限的 SOP 技能（Skill）。
    *   提供 Skill 安裝與升級的懶人包大放送。
*   **影片連結**：[前往觀看 EP04](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP04)

### 5. **EP05：教學應用程式的 5 個階段**
*   **主題**：教師如何從零開始引導 AI 開發出實用的互動式教學網頁。
*   **內容要點**：
    *   解析教學 App 開發的五個成長階段（從靜態 HTML 網頁、動態 JS 交互，到串接資料庫與語音合成的 AI 語音助教）。
    *   引導教師建立 Firebase 與 Google Sheets 的資料庫思維，實現學生成績與課堂互動的自動化記錄。
*   **影片連結**：[前往觀看 EP05](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP05)

### 6. **EP06：全面代理你的 Google Classroom**
*   **主題**：行政與班級管理自動化實戰。
*   **內容要點**：
    *   授權 AI 代理人全面接管 Google Classroom。
    *   自動執行批次派發作業、自動收集學生回傳的檔案，並根據預設的標準答案或規準完成初步批改。
*   **影片連結**：[前往觀看 EP06](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP06)

### 7. **EP07：一句話生成 Padlet 課程牆**
*   **主題**：課堂互動看板的 AI Agent 自動化管理。
*   **內容要點**：
    *   實作透過簡單一句指令，讓助教在 Padlet 平台上自動建立分區課程牆。
    *   自動化執行貼文生成、投票統計以及呼叫生圖工具生成課程看板背景插圖。
*   **影片連結**：[前往觀看 EP07](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP07)

### 8. **EP08：Agent 代理免費複製你的聲音**
*   **主題**：AI 語音克隆（Voice Cloning）技術的教學應用。
*   **內容要點**：
    *   教學如何僅用一行指令，讓 AI 代理在本地端免費複製老師自己的聲音，並將其轉化為自然流暢的語音講稿。
    *   擺脫昂貴的商業 AI 語音訂閱服務，快速為投影片或教學影片壓製語音旁白。
*   **影片連結**：[前往觀看 EP08](https://www.youtube.com/@sensebar) (請至頻道搜尋 EP08)

---

## 💡 老師的核心收穫

1.  **大腦與雙手協同 (NotebookLM + AntiGravity)**：
    *   利用 NotebookLM 來儲存教材、閱讀文獻並做邏輯思考，再利用 AntiGravity (AI Agent) 寫程式、建網頁並部署上線，大幅降低教師的技術門檻。
2.  **行政減負與代理思維**：
    *   將例行性、重複性高的行政工作（如 Classroom 派課、Padlet 收發、考卷打字、語音錄製）交給 AI 代理自動處理，讓教師能專注於課堂互動與學生學習輔導。
3.  **無縫部署流程**：
    *   透過 lazy-pack (懶人包) 與一鍵配置，老師可以快速在本地建立起結合 GitHub 與 Firebase 的雲端發布環境，一秒完成隨堂小測驗網頁的發布。
