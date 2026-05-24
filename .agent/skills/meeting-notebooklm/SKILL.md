---
name: meeting-notebooklm
description: Automates meeting intelligence by fetching videos from Google Drive, splitting them for compatibility, and using NotebookLM (via notebooklm-py) to generate meeting minutes, explainer videos, and AI podcasts.
---

# Meeting NotebookLM Skill

This skill automates the process of transforming meeting recordings into actionable intelligence using NotebookLM.

## Workflow Overview

1.  **Fetch**: Retrieve video from Google Drive.
2.  **Split**: Ensure video parts are under 200MB (NotebookLM limit) using `scripts/split_video.py`.
3.  **Process**: Upload chunks, **wait for processing**, and then generate artifacts.
4.  **Generate**: Produce meeting minutes (Markdown), Explainer Video (MP4), AI Podcast (M4A), and **Polished Transcription (Markdown)**.

## Prerequisites & Setup

This skill uses `notebooklm-py` and `moviepy`.

### 1. Environment Setup
The skill environment is managed at:
- **Venv**: `/Users/yasutakairino/meeting/notebooklm-py-venv`
- **Source**: `/Users/yasutakairino/meeting/notebooklm-py-src`

Ensure you use the full path to the venv python:
```bash
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm [command]
```

### 2. Authentication
Check status before starting:
```bash
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm list
```
If "Not logged in", run:
```bash
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm login
```

## Core Commands

### Step 1: Split Video (if > 200MB)
```bash
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python scripts/split_video.py [input_path] [output_dir] --size 190
```

### Step 2: Create Notebook & Set Context
```bash
# Create notebook and capture the ID
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm create "Meeting: [Title] [Date]"

# Use the ID to set context
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm use [notebook_id]
```

### Step 3: Add Sources & Wait for Processing
**CRITICAL**: Sources must be "ready" before generating artifacts.
```bash
# Add each video chunk
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm source add [chunk_path] --type file

# Wait for each source (use prefix or full ID)
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm source wait [source_id]
```

### Step 4: Generate & Download Artifacts

#### A. Meeting Minutes (Report)
```bash
# Generate - include context about date/time/participants if known
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm generate report "Create detailed meeting minutes. Include the meeting date, time, and participants (guess from the source filename or discussion). Cover key decisions, action items, and a summary of the discussion." --format briefing-doc --wait

# Download as Markdown (.md)
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm download report meeting_minutes.md
```

#### B. Polished Transcription (Clean-up)
Use this task to convert a raw transcription (which may include filler words like "あー", "えー", "そうですね") into a professional final draft.
```bash
# Generate Polished Transcription
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm generate report "Create a verbatim transcription of the meeting. CRITICAL: Remove all filler words and verbal tics such as 'あー', 'えー', 'えーと', 'そうですね', and 'あのー' to produce a clean, professional final draft. Keep the speaker names and the content accurate but polished." --format briefing-doc --wait

# Download as Markdown (.md)
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm download report transcription_polished.md
```

#### C. Explainer Video
```bash
# Generate (Video takes 10-20 minutes)
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm generate video "Create a professional explainer video summarizing the meeting highlights." --style classic

# Wait explicitly with high timeout if the initial command times out
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm artifact wait [artifact_id] --timeout 1200

# Download as MP4
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm download video explainer_video.mp4
```

#### D. AI Podcast (Audio Overview)
```bash
# Generate
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm generate audio "Create a deep-dive podcast discussion about the meeting topics." --format deep-dive

# Wait explicitly
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm artifact wait [artifact_id] --timeout 1200

# Download as M4A (Required extension for NotebookLM audio)
/Users/yasutakairino/meeting/notebooklm-py-venv/bin/python -m notebooklm download audio meeting_podcast.m4a
```

## Best Practices

- **Timeout Management**: Large artifacts (Video/Audio) often exceed default tool timeouts (5 mins). Use `artifact list` to check status and `artifact wait --timeout 1200` to monitor long-running tasks.
- **File Extensions**: 
    - Reports: `.md`
    - Video: `.mp4`
    - Audio: `.m4a` (Using `.wav` will result in a silent file or errors).
- **Notebook Context**: Always verify `notebooklm status` before adding sources if multiple notebooks exist.

## Error Handling

- **Silent Audio**: If a downloaded audio file has no sound, ensure it was downloaded with the `.m4a` extension.
- **Failed Generation**: If an artifact status is "failed", delete it (`artifact delete [id] -y`) and try again after checking source status.
- **Unknown Type Warning**: Ignore `UnknownTypeWarning` for source types; it doesn't affect generation.
