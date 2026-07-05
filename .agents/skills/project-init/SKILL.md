---
name: project-init
description: 說「初始化專案」時自動建立新專案與關聯服務。
---

# 專案初始化流程

當使用者說「初始化專案」時，請執行以下步驟：

1. **建立基本專案檔案**：
   - 在根目錄建立 `ANTIGRAVITY.md` 專案駕駛艙。
   - 建立 `.gitignore`（自動排除 `.venv/`、`node_modules/`、`.env`、`output.pptx` 臨時檔等）。
   - 建立 `README.md` 專案基本說明。
2. **初始化 Git 與 GitHub**：
   - 執行 `git init`，加入所有檔案並完成 initial commit。
   - 使用 `gh repo create` 自動在 GitHub 上建立對應的遠端儲存庫並推上去。
3. **建立 Obsidian 專案目錄**：
   - 在 `G:\我的雲端硬碟\secondbrain\` 底下建立對應新專案名稱的筆記工作區資料夾。
