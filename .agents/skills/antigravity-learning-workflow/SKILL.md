---
name: antigravity-learning-workflow
description: >-
  A project-specific workflow skill for setting up the Antigravity teacher assistant, generating PPTX and HTML slides with auto-fit titles and dynamic body font sizes, and conducting SLC classroom video analysis.
---

# Antigravity Learning Workflow

## Overview
This skill provides the standard operating procedure (SOP) for utilizing the Antigravity Teacher AI Agent to generate, modify, and optimize educational slides, synchronize external NotebookLM knowledge bases, and perform School as Learning Community (SLC) lesson studies.

## Quick Start
To trigger this workflow, tell the agent:
"請按照 Antigravity Learning Workflow 引導我完成簡報優化與觀課分析。"

## Workflow

### 1. Environment Setup & Lazy Pack Installation
- Download the Antigravity Lazy Pack from: https://github.com/mathruffian-dot/antigravity-lazy-pack/tree/main
- Install by providing `09-AntiGravity專屬懶人包.md` to the agent and commanding: "安裝這個懶人包".
- Configure global and project settings in `.agents` and check model, permissions, and directory access.

### 2. Dual-Brain Sync (NotebookLM)
- Place NotebookLM export notes into the workspace.
- Install the `notebooklm-sync` skill under `.agents/skills/`.
- Ask the agent to read notes and generate interactive quiz pages (`quiz.html`) to verify student understanding.

### 3. Lesson Study & Video Analysis (SLC)
- Install the `classroom-video-analyzer` skill and the `SLC-skill` from: https://github.com/hsuyiping-rgb/SLC-skill
- Feed classroom video recordings or transcripts to the agent.
- Ask the agent to perform SLC analysis: "進行學共觀課分析".
- Verify that student listening and collaborative learning patterns are mapped, and the report `slc_report.docx` is generated.

### 4. Slide Generation & Layout Optimization (Marp & PPTX)
- Write the Marp outline (`slides.md`).
- Run the native PowerPoint compiler script `demos/generate_native_pptx.py` to compile `slides/output_v2.pptx`.
- Recompile slides to a responsive HTML file (`slides_v2.html`) using Marp CLI.
- Ensure all text-align is left, and raw asterisks (`*`) are removed from all slide text.
- Apply dynamic font sizing:
  - Slide titles: Pt(24) to Pt(34) depending on title length to keep titles strictly on a single line.
  - Slide body bullets: Pt(20) to Pt(24) depending on slide content volume to prevent text overflow.

## Common Mistakes
- **PowerPoint File Locking**: Running the compiler while `output_v2.pptx` is open in PowerPoint will fail. Close PowerPoint first, or check the fallback file `output_v2_new.pptx`.
- **Literal Asterisks in PPTX**: Ensure all single asterisks or Markdown bold/italic markers are parsed and removed before rendering.
- **Marp HTML Path Errors**: Keep the HTML slides file (`slides_v2.html`) in the root folder so that relative paths to `slides/images/...` resolve correctly.
