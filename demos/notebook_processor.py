# -*- coding: utf-8 -*-
"""
AI Agent 實戰示範：NotebookLM 內容自動處理器

本腳本模擬 Agent 如何處理從 NotebookLM 複製過來的 Markdown 資料：
1. 讀取 notebooklm_sync/notebook_content.md
2. 解析裡面的「問答」與「概念」
3. 自動生成一個互動式的隨堂測驗網頁 (quiz.html)
"""

import os
import re

def initialize_sync_dir():
    """初始化同步資料夾與範本檔案"""
    sync_dir = "notebooklm_sync"
    content_file = os.path.join(sync_dir, "notebook_content.md")
    
    if not os.path.exists(sync_dir):
        os.makedirs(sync_dir)
        print(f"[資訊] 已建立同步資料夾：{sync_dir}")
        
    if not os.path.exists(content_file):
        # 建立一個模擬的 NotebookLM 導出內容
        template_content = """# NotebookLM 導出內容範本

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
"""
        with open(content_file, "w", encoding="utf-8") as f:
            f.write(template_content.strip())
        print(f"[資訊] 已建立範本資料夾與檔案：{content_file}")
        print("[說明] 您可以把您的 NotebookLM 內容複製貼上到此檔案中。")
    
    return content_file

def parse_notebook_content(file_path):
    """解析 Markdown 檔案中的問答題"""
    print(f"\n[步驟 1] 正在讀取並解析：{file_path} ...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        
    # 用正則表達式尋找問答題
    # 格式匹配: Q1: ... A) ... B) ... 答案: X
    questions = []
    
    # 簡單的正則匹配段落
    q_blocks = re.findall(r"(Q\d+:.*?)(?=Q\d+:|$)", text, re.DOTALL)
    
    for block in q_blocks:
        lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
        if len(lines) >= 3:
            q_text = lines[0]
            options = []
            ans = ""
            for line in lines[1:]:
                if line.startswith("答案:"):
                    ans = line.replace("答案:", "").strip()
                elif any(line.startswith(prefix) for prefix in ["A)", "B)", "C)", "D)"]):
                    options.append(line)
            if q_text and options and ans:
                questions.append({
                    "question": q_text,
                    "options": options,
                    "answer": ans
                })
                print(f"  -> 解析成功：{q_text[:20]}... 答案：{ans}")
                
    return questions

def generate_interactive_quiz_html(questions, output_path="demos/quiz.html"):
    """根據解析出的題目生成精美的互動測驗 HTML 網頁"""
    print(f"\n[步驟 2] 正在根據解析結果生成互動測驗網頁：{output_path} ...")
    
    # 確保 demos 目錄存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 建構題目 JS 陣列
    questions_js = []
    for q in questions:
        opts_str = ", ".join([f'"{opt}"' for opt in q["options"]])
        questions_js.append(f"""
        {{
            question: "{q['question']}",
            options: [{opts_str}],
            answer: "{q['answer']}"
        }}""")
    questions_js_str = ",\n".join(questions_js)

    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NotebookLM 隨堂小測驗</title>
    <style>
        body {{
            font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif;
            background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%);
            color: #fff;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            padding: 20px;
        }}
        .quiz-container {{
            background: rgba(255, 255, 255, 0.95);
            color: #333;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
            transition: all 0.3s ease;
        }}
        h1 {{
            color: #0b3c5d;
            text-align: center;
            margin-top: 0;
            font-size: 24px;
            border-bottom: 2px solid #328cc1;
            padding-bottom: 10px;
        }}
        .question {{
            font-size: 18px;
            font-weight: bold;
            margin: 20px 0 15px 0;
            color: #0b3c5d;
        }}
        .option-btn {{
            display: block;
            width: 100%;
            padding: 12px 15px;
            margin: 8px 0;
            background: #f0f4f8;
            border: 2px solid #d0e0f0;
            border-radius: 8px;
            text-align: left;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .option-btn:hover {{
            background: #e1effa;
            border-color: #328cc1;
        }}
        .option-btn.correct {{
            background: #d4edda;
            border-color: #28a745;
            color: #155724;
            font-weight: bold;
        }}
        .option-btn.wrong {{
            background: #f8d7da;
            border-color: #dc3545;
            color: #721c24;
        }}
        .result {{
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
            color: #0b3c5d;
        }}
        .progress {{
            font-size: 14px;
            color: #666;
            text-align: right;
        }}
        .restart-btn {{
            display: block;
            width: 100%;
            padding: 12px;
            background: #0b3c5d;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 20px;
            text-align: center;
        }}
        .restart-btn:hover {{
            background: #328cc1;
        }}
    </style>
</head>
<body>

<div class="quiz-container" id="quiz-box">
    <h1>📝 NotebookLM 隨堂小測驗</h1>
    <div class="progress" id="progress-text">載入中...</div>
    <div class="question" id="question-text">題目載入中...</div>
    <div id="options-box"></div>
    <div class="result" id="result-text"></div>
</div>

<script>
    const questions = [
{questions_js_str}
    ];

    let currentIndex = 0;
    let score = 0;

    const progressEl = document.getElementById("progress-text");
    const questionEl = document.getElementById("question-text");
    const optionsEl = document.getElementById("options-box");
    const resultEl = document.getElementById("result-text");

    function loadQuestion() {{
        if (questions.length === 0) {{
            questionEl.innerText = "目前沒有解析出任何測驗題目。";
            progressEl.innerText = "";
            return;
        }}
        
        resultEl.innerText = "";
        const currentQ = questions[currentIndex];
        progressEl.innerText = `第 ${{currentIndex + 1}} 題 / 共 ${{questions.length}} 題`;
        questionEl.innerText = currentQ.question;
        optionsEl.innerHTML = "";

        currentQ.options.forEach(opt => {{
            const btn = document.createElement("button");
            btn.className = "option-btn";
            btn.innerText = opt;
            btn.onclick = () => checkAnswer(btn, opt, currentQ.answer);
            optionsEl.appendChild(btn);
        }});
    }}

    function checkAnswer(selectedBtn, selectedText, correctAnswer) {{
        // 取得選擇的代號 (A, B, C, D)
        const selectedCode = selectedText.charAt(0);
        const buttons = optionsEl.getElementsByTagName("button");
        
        // 停用所有按鈕防止重複點擊
        for (let btn of buttons) {{
            btn.disabled = true;
            const btnCode = btn.innerText.charAt(0);
            if (btnCode === correctAnswer) {{
                btn.classList.add("correct");
            }}
        }}

        if (selectedCode === correctAnswer) {{
            score++;
            resultEl.innerHTML = "🎉 回答正確！";
            resultEl.style.color = "#28a745";
        }} else {{
            selectedBtn.classList.add("wrong");
            resultEl.innerHTML = `❌ 回答錯誤，正確答案是: ${{correctAnswer}}`;
            resultEl.style.color = "#dc3545";
        }}

        setTimeout(() => {{
            currentIndex++;
            if (currentIndex < questions.length) {{
                loadQuestion();
            }} else {{
                showFinalResults();
            }}
        }}, 2000);
    }}

    function showFinalResults() {{
        progressEl.innerText = "測驗完成";
        questionEl.innerText = "您的最終得分：";
        optionsEl.innerHTML = `
            <div style="font-size: 32px; font-weight: bold; text-align: center; color: #0b3c5d; margin: 20px 0;">
                ${{score}} / ${{questions.length}}
            </div>
            <button class="restart-btn" onclick="restartQuiz()">重新測驗</button>
        `;
        resultEl.innerText = "";
    }}

    function restartQuiz() {{
        currentIndex = 0;
        score = 0;
        loadQuestion();
    }}

    // 初始化載入
    loadQuestion();
</script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[成功] 互動測驗網頁已生成！請開啟檔案檢視：{output_path}")

def main():
    print("=== NotebookLM 內容同步解析引擎 ===")
    content_file = initialize_sync_dir()
    questions = parse_notebook_content(content_file)
    if questions:
        generate_interactive_quiz_html(questions)
    else:
        print("[資訊] 尚未在 Markdown 檔案中偵測到符合格式的問答題。")

if __name__ == "__main__":
    main()
