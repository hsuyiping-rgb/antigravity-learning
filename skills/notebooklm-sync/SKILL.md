---
name: notebooklm-integrator
description: Use this skill when the user wants to sync, import, or process content exported from Google NotebookLM (such as raw notes, study guides, FAQs, or notebook URLs).
---

# NotebookLM 整合與自動化處理技能

本 Skill 專門用於處理從 Google NotebookLM 匯出的結構化教學內容，並將其自動轉換為本專案的教學資源（如投影片、隨堂測驗或程式範例）。

## 工作流規範

由於 Google NotebookLM 目前沒有公開 API 且需要 Google 帳號授權，我們透過「檔案同步法」來實現無縫串接：

1.  **使用者操作**：
    *   在 NotebookLM 中整理好內容（如筆記、Study Guide）。
    *   將內容複製並貼到本工作區的 `notebooklm_sync/notebook_content.md` 檔案中。
2.  **Agent 自動化處理**：
    *   當偵測到該檔案更新時，本 Skill 會引導 Agent 執行 `demos/notebook_processor.py` 腳本。
    *   腳本會自動解析該檔案，並更新 `slides.md` 投影片或在 `demos/quiz/` 中生成測驗網頁。

## 處理指令集

當使用者說「**同步 NotebookLM 內容**」或「**更新筆記**」時，請執行以下步驟：

1.  讀取 `notebooklm_sync/notebook_content.md` 的內容。
2.  呼叫 `demos/notebook_processor.py` 進行解析。
3.  根據解析出來的結構：
    *   若包含「投影片大綱」，則自動修改 `slides.md`。
    *   若包含「測驗題」，則自動在 `demos/` 下建立或更新 `quiz.html`。
    *   若包含「概念定義」，則自動生成對應的程式碼範例。
