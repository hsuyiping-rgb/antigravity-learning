# -*- coding: utf-8 -*-
"""
AI Agent 實戰示範：智慧影片剪輯與字幕自動生成

本腳本展示了 AI Agent（如 Antigravity）如何透過程式碼自動化完成以下流程：
1. 提取影片音訊並使用語音轉文字（STT）模型生成 .srt 字幕檔。
2. 語意解析字幕，自動尋找關鍵詞所在的時間段。
3. 使用 moviepy / ffmpeg 剪輯出精華影片。
"""

import os
import sys

def check_dependencies():
    """檢測執行所需的套件是否安裝"""
    try:
        import moviepy
        print("[資訊] 偵測到 moviepy 已安裝。")
    except ImportError:
        print("[警告] 未偵測到 moviepy，請執行: pip install moviepy")
        print("[說明] Agent 在實戰中會自動替您安裝此套件。")

def transcribe_video_mock(video_path):
    """
    模擬語音轉文字 (Speech-to-Text) 生成字幕的過程。
    實務上，Agent 會寫程式呼叫 OpenAI Whisper API、Gemini API 或本地 Whisper 模型。
    """
    print(f"\n[步驟 1] 正在提取影片 {video_path} 的音訊並送至語音辨識模型...")
    print("[資訊] 語音辨識中... 成功辨識出語音並產生時間軸。")
    
    # 模擬產生的 SRT 字幕內容
    srt_content = """1
00:00:01,000 --> 00:00:05,000
各位老師好，今天我們要來學習什麼是 AI Agent（智能代理）。

2
00:00:06,000 --> 00:00:10,000
AI Agent 與傳統的 Chatbot 不同，它具有主動規劃與執行任務的能力。

3
00:00:11,000 --> 00:00:16,000
例如，它可以自動幫我們剪接這段教學影片，並產生精準的字幕。
"""
    srt_path = video_path.replace(".mp4", ".srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content.strip())
    print(f"[成功] 已自動產生字幕檔：{srt_path}")
    return srt_path

def search_highlights(srt_path, keyword):
    """
    模擬 Agent 閱讀字幕並篩選關鍵片段的時間軸。
    """
    print(f"\n[步驟 2] Agent 正在分析字幕，搜尋關鍵字：'{keyword}'...")
    
    # 簡單的搜尋邏輯
    highlights = []
    with open(srt_path, "r", encoding="utf-8") as f:
        content = f.read()
        blocks = content.split("\n\n")
        for block in blocks:
            lines = block.split("\n")
            if len(lines) >= 3:
                times = lines[1]
                text = " ".join(lines[2:])
                if keyword in text:
                    start_time, end_time = times.split(" --> ")
                    highlights.append((start_time, end_time, text))
                    print(f"  -> 找到匹配段落 [{start_time} - {end_time}]: {text}")
    return highlights

def clip_video_mock(video_path, start_time, end_time, output_path):
    """
    模擬使用 ffmpeg/moviepy 剪輯影片的過程。
    """
    print(f"\n[步驟 3] Agent 正在執行剪輯命令，將 {video_path} 的 [{start_time} 至 {end_time}] 剪出...")
    
    # 在真實執行中，Agent 會生成類似下面的指令並執行：
    # ffmpeg_cmd = f"ffmpeg -i {video_path} -ss {start_time} -to {end_time} -c copy {output_path}"
    
    print(f"[指令模擬] ffmpeg -i {video_path} -ss {start_time} -to {end_time} -c copy {output_path}")
    print(f"[成功] 精華影片剪輯完成，輸出至：{output_path}")

def main():
    print("=== AI Agent 影片剪輯與字幕生成 Demo (模擬流程) ===")
    check_dependencies()
    
    # 設定虛擬檔案路徑
    dummy_video = "classroom_lecture.mp4"
    
    # 創建虛擬影片檔以便演示（若不存在）
    if not os.path.exists(dummy_video):
        with open(dummy_video, "w") as f:
            f.write("dummy video data")
            
    # 1. 產生字幕
    srt_file = transcribe_video_mock(dummy_video)
    
    # 2. 搜尋關鍵字 "Agent"
    highlights = search_highlights(srt_file, "Agent")
    
    # 3. 剪接影片
    if highlights:
        # 剪輯第一個匹配的段落
        start, end, text = highlights[0]
        output_clip = "agent_definition_highlight.mp4"
        clip_video_mock(dummy_video, start, end, output_clip)
    else:
        print("[警告] 字幕中未找到關鍵字。")
        
    # 清理虛擬測試檔案
    try:
        os.remove(dummy_video)
        os.remove(srt_file)
        print("\n[清理] 已清除模擬測試檔案。")
    except Exception:
        pass

if __name__ == "__main__":
    main()
