---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #090e17
color: #e2e8f0
style: |
  section {
    font-family: 'Outfit', 'Inter', 'PingFang TC', 'Microsoft JhengHei', sans-serif;
    padding: 60px;
    background: linear-gradient(135deg, #090e17 0%, #131b2e 100%);
  }
  h1 {
    color: #00f2fe;
    border-bottom: 4px solid #4facfe;
    padding-bottom: 12px;
    font-size: 40px;
    margin-top: 0;
  }
  h2 {
    color: #4facfe;
    font-size: 28px;
    border: none;
    margin-top: 10px;
  }
  strong {
    color: #ff5e62;
    font-weight: bold;
  }
  li {
    margin-bottom: 10px;
    line-height: 1.5;
    font-size: 28px;
    color: #cbd5e1;
  }
  code {
    background-color: rgba(255, 255, 255, 0.08);
    color: #00f2fe;
    padding: 3px 8px;
    border-radius: 5px;
    font-family: 'Fira Code', 'Cascadia Code', Consolas, monospace;
    font-size: 85%;
  }
  blockquote {
    border-left: 6px solid #00f2fe;
    background: rgba(255, 255, 255, 0.05);
    padding: 12px 20px;
    margin: 15px 0;
    border-radius: 0 10px 10px 0;
    font-style: normal;
    color: #94a3b8;
    font-size: 28px;
  }
  section.lead {
    background: linear-gradient(135deg, #05080c 0%, #0c1220 100%);
    color: #ffffff;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section.lead h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 48px;
    text-shadow: 0 4px 12px rgba(0, 242, 254, 0.4);
  }
  section.lead h2 {
    color: #00f2fe;
    font-size: 24px;
    text-shadow: 0 2px 4px rgba(0, 242, 254, 0.2);
  }
  footer {
    font-size: 13px;
    color: #4a5568;
  }
---

# 從「被動聊天」到「主動做事」
## 教師的 AI Agent (虛擬助教) 實戰啟蒙

主講人：[您的名字]  
時間：2026  

![bg right:45%](slides/images/slide_1.png)

---

# 傳統 AI 聊天 vs. AI Agent 助教

* **傳統 AI (Chat)**
  - 像**「點唱機」**：問一句答一句，手動做所有事。
  - 沒有記憶，無法幫您操作電腦或使用工具。
* **AI Agent (虛擬助教)**
  - 像**「實習生」**：給它一個「目標」，它會自己想辦法完成。
  - 能讀寫檔案、寫簡單的程式、上網找資料，還會自我除錯。
  - 運作流程：**查資料 $\rightarrow$ 提計畫 $\rightarrow$ 動手做 $\rightarrow$ 檢查結果**。

![bg right:40%](slides/images/slide_3.png)

---

# 虛擬助教的準備：快速上手

* **快速建置環境**
  - 使用 `uv` 工具，一鍵建立一個乾淨、不干擾系統的 Python 虛擬工作間。
* **指定專屬工作資料夾 (Workspace)**
  - 告訴助教：「你只能在這個資料夾內活動與修改檔案」。
  - 確保助教執行指令與檔案讀寫時的安全，防止動到電腦的其他重要檔案。

![bg right:40%](slides/images/slide_5.png)

---

# 虛擬助教的準備：設定與權限簿

* **全域設定 (Global)**
  - 路徑：`C:\Users\vm\.gemini\config`
  - 存放助教通用的密鑰、您的登入帳號與預設 AI 模型。
* **專案設定 (Project)**
  - 路徑：專案資料夾下的 `.agents`
  - 存放該專案專屬的工作規則，告訴助教什麼能做、什麼不能做。

![bg right:40%](slides/images/slide_5.png)

---

# 虛擬助教的準備：簡單兩步驟

* **第一步：安裝軟體與套件**
  - 安裝好編輯器（如 `VS Code`）與 `Antigravity` 套件，這是老師與助教溝通的橋樑。
* **第二步：建立工作目錄**
  - 建立一個全新的專案資料夾。
  - 設定好版本控制與虛擬環境，讓助教隨時可以開工。

![bg right:40%](slides/images/slide_5.png)

---

# 設定面板：定義助教的工作守則

* `General (一般)`：設定助教要用的命令視窗與工作資料夾路徑。
* `Account (帳戶)`：登入您的 Google 帳戶，讓助教獲得 AI 的超能力。
* `Permissions (權限控制)`：**最安全！** 設定助教做事前（如改檔案、跑指令）是否要先敲門請老師點擊同意。
* `Appearance (外觀)`：調整畫面顏色深淺與字型大小，讓老師眼睛不吃力。
* `Models (模型)`：挑選適合的 AI 模型作為助教的智囊團。
* `Customizations (客製化)`：匯入特別的「技能卡」或特定的規則。
* `Browser (瀏覽器)`：設定助教上網查詢資料時使用的設定。
* `App (應用程式)`：管理系統暫存檔與助教的工作紀錄日記。

![bg right:40%](slides/images/slide_6.png)

---

# 脈絡工具：給助教的「參考資料與任務指令」

* `Media (上傳參考資料)`：可以直接把簡報 PDF、課堂照片、影片拉給助教，多模態 AI 能直接看懂排版或 UI 設計。
* `@ 標記提及 (Mentions)`：精準交代資料。標記 `@ 某個檔案` 就像是「直接把考卷遞給助教看」，或指名特定的專業子助教。
* `Actions (快捷動作)`：輸入斜線指令（如 `/goal` 直接交代大目標，`/schedule` 交代定時自動工作）。
* `Browser (網頁瀏覽)`：讓助教開啟瀏覽器上網，抓取最新的時事或學術資料來設計教材。

![bg right:40%](slides/images/slide_7.png)

---

# 什麼是 Skill？助教的「SOP 教戰手冊」

* **Skill (技能) 的結構**
  - 它是一份寫好的標準作業程序檔案（如 `SKILL.md`），搭配輔助程式。
* **觸發機制**
  - 當老師提出需求（如「我想設計教案」）時，助教若發現手冊有寫，就會自動套用 SOP。
* **教學應用**
  - 老師可自訂 `lesson-plan-generator` 或期末考審題手冊，確保助教產出的講義與題目都符合學校的格式標準。

![bg right:40%](slides/images/slide_8.png)

---

# 實戰任務一：課堂影片自動剪接與字幕對齊

> **老師痛點**：下課後要把 2 小時的課堂影片剪出重點，還要手動聽寫、對齊字幕，非常耗時。

* **虛擬助教的自動化三步驟**：
  1. **聽寫字幕**：助教聽取影片聲音，自動生成對齊時間軸的 `.srt` 字幕檔。
  2. **尋找精華**：助教自動讀取字幕內容，找出包含關鍵教學重點的時間區段。
  3. **自動剪輯**：助教自動寫出剪接指令，剪出重點影片片段並把字幕對齊壓好。

![bg right:40%](slides/images/slide_9.png)

---

# 實戰任務二：講義大綱一鍵生成精美投影片

> **老師痛點**：每次備課都要花大量時間調整簡報字型、對齊排版，無法專注在內容設計上。

* **虛擬助教的解法**：
  * **寫程式生簡報**：助教自動寫出 Python 程式，直接產出一份可供老師自由修改的 `.pptx` 簡報檔。
  * **文字大綱秒變投影片**：助教撰寫符合 `Marp` 格式的大綱，一鍵轉換成簡報網頁或 PDF。
  * **AI 自動畫插圖**：助教自動生成適合簡報內容的教學配圖，不用再到處找無版權圖片。

![bg right:40%](slides/images/slide_10.png)

---

# 實戰任務三：隨堂測驗網頁一鍵放上雲端

> **老師痛點**：寫好一個互動測驗網頁後，不知道要怎麼放上網路給學生連線使用。

* **虛擬助教的解法**：
  - **自動雲端存檔**：助教自動幫您把專案做好 Git 控制，一鍵推上雲端代管平台。
  - **一鍵完成網站發布**：助教自動跑好 Firebase 部署流程，在幾秒鐘內把網頁推上雲端網站。
* **教學應用**：做好的測驗網頁隨即擁有網址，上課時投在螢幕上，學生拿手機掃 QR Code 就能立即連線進行隨堂小測驗！

![bg right:40%](slides/images/slide_11.png)

---

# NotebookLM 與 Antigravity：協同雙腦工作流

* **NotebookLM (大腦 — 負責讀書思考)**
  - 適合：讀入講義、課綱、PDF 檔案。
  - 功能：做摘要、整理學習指引、回答老師提問、生成對答語音。
* **Antigravity (雙手 — 負責動手建造)**
  - 適合：將軍師思考好的架構與大綱，化為實際行動。
  - 功能：啟動 `Planning Mode` (寫企劃書)，自動寫出程式碼、生成簡報、發布網頁。

> **一句話總結**：NotebookLM 幫您「讀書動腦」，Antigravity 幫您「動手完成」。

![bg right:40%](slides/images/slide_12.png)

---

# NotebookLM 串接實務：Markdown 同步法

* **將兩大 AI 串聯的實務步驟**
  - **第一步：複製貼上**：把 NotebookLM 整理好的重點內容，貼到工作區的 `notebooklm_sync/notebook_content.md` 檔案中。
  - **第二步：助教偵測**：助教發現檔案內容有更新，自動讀取內容。
  - **第三步：解析與生成**：助教自動執行解析程式，一鍵產生一個精美且可互動的隨堂測驗網頁 `quiz.html`。

![bg right:40%](slides/images/slide_13.png)

---

# AI 時代的啟示：教學典範的轉移

* **核心能力的轉變**：
  - 學生不一定要死記所有的程式碼語法，而是學習「如何定義目標」、「如何審查助教提的計畫企劃書」，以及「如何使用工具解決問題」。
* **教師角色的轉變**：
  - 教師從單純的「板書抄寫與語法教學者」，升級為「引導者與決策者」。
  - 老師審查學生提出的 `implementation_plan.md`，引導學生思考與修正。

![bg right:40%](slides/images/slide_14.png)

---

# Q & A

感謝各位老師的參與！
讓我們一起用「虛擬助教」開啟更輕鬆、更有趣的教學新旅程。

![bg right:45%](slides/images/slide_15.png)
