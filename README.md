# Antigravity 學習專案 (Antigravity Learning Project)

本專案旨在為教師提供關於 AI Agent（特別是 Antigravity）與教學自動化的學習資源、簡報檔大綱與實作 Demo 腳本。

## 專案資料夾結構

*   `slides.md`：本課程的簡報大綱（符合 **Marp** 簡報工具格式，可直接轉為 PDF/PPT/HTML）。
*   `demos/`：專案實務自動化 Demo 示範腳本。
    *   `video_clipper.py`：展示 Agent 如何呼叫轉錄（Whisper/Gemini）與剪輯工具（FFmpeg）來剪輯影片與生成字幕。
    *   `ppt_generator.py`：展示 Agent 如何透過 Python 程式碼自動生成投影片。
*   `skills/`：自訂 Agent Skill 的示範目錄。
    *   `demo-skill/SKILL.md`：自訂 Skill 的架構範例。

## 快速開始

1.  **安裝簡報檢視工具 (Marp)**：
    *   您可以在 VS Code 中安裝 **Marp for VS Code** 擴充功能，即可即時預覽與匯出 `slides.md`。
2.  **執行 Demo 腳本**：
    *   請先確保已安裝 Python 環境與相依套件：
        ```bash
        pip install moviepy python-pptx
        ```
    *   進入 `demos/` 資料夾並參考腳本註解進行測試。
3.  **了解 Skill 運作方式**：
    *   閱讀 `skills/demo-skill/SKILL.md`，了解如何透過 YAML Frontmatter 讓 Antigravity 自動識別並套用特定的教學步驟。
