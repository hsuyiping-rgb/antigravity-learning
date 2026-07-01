---
name: lesson-plan-generator
description: Use this skill when the user wants to generate, edit, or format a lesson plan (教案) for high school or middle school classes.
---

# 教案生成與優化技能 (Lesson Plan Generation Skill)

當使用者請求產生或設計一份教學教案時，請遵循本 Skill 規定的格式與步驟進行設計。

## 教案標準格式

所有產出的教案均必須包含以下幾個核心區塊，並使用 Markdown 格式呈現：

1.  **基本資訊**：
    *   課程名稱 (Course Title)
    *   適合年級 (Target Grade)
    *   預估時間 (Duration)
2.  **教學目標 (Learning Objectives)**：
    *   條列出 2-3 項學生在課程結束後能夠掌握的核心概念或技能。
3.  **教學準備 (Preparation)**：
    *   教師與學生需要提前準備的軟硬體工具（例如：電腦、Python 環境、Antigravity 平台等）。
4.  **教學流程 (Lesson Flow)**：
    *   **導入 (Hook, 10%)**：引發動機的核心提問或日常場景。
    *   **概念講授 (Instruction, 30%)**：核心觀念的解說。
    *   **動手實作 (Hands-on Practice, 40%)**：學生自己動手或與 Agent 協同操作的步驟。
    *   **總結與反思 (Wrap-up, 20%)**：複習與課後討論問題。
5.  **學習評量 (Assessment)**：
    *   提供一個簡單的隨堂檢測題目或實作檢核表。

## 執行規範

*   **人機協作重點**：在「動手實作」環節，必須特別設計一個引導學生如何與 AI Agent 協同除錯（Debug）或進行專案評估的步驟。
*   **字數限制**：教案說明字數應介於 800 至 1200 字之間，保持結構清晰、步驟明確。
