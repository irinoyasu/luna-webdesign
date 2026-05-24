# Phase 3: Google Slides Generation (Strict Protocol) Reference

## Purpose

This phase transforms the Q&A pairs into a professional-grade Google Slides presentation. We use a "Pixel Perfect" high-fidelity design template (9,700+ lines) and a Python merge script to automate the process, ensuring consistency across 160+ slides with advanced styling.

## Inputs

**You MUST synthesize information from ALL previously completed Q&A phases.**
1. **Q&A Pairs:** Generated in Phase 2 (`answer/answers-[persona].md`).
2. **Judging Criteria:** Defined in `reference/question-phase.md`.
3. **Professional Template (CRITICAL):** `.agent/skills/q-and-a/assets/q-and-a-gas-template.js` (Must be the 9,700+ line version).
4. **Merge Script:** `.agent/skills/q-and-a/scripts/merge_gas_presentation.py`.

## Sub-Task Index

| # | Sub-Task | Output File(s) | Description |
|---|---|---|---|
| 1 | Generate Outline | `slide/outline.md` | Logical structural outline of the Q&A session. |
| 2 | Write Complete Pitch Text | `slide/text.md` | Structured narrative script for speaker notes. |
| 3 | Draft Google Slides Data | `slide/writing-slide/10min-slideData.json` | JSON data array mapped to the required schema. |
| 4 | Generate GAS Presentation | `slide/q-and-a-gas_presentation.js` | The executable Google Apps Script (Merged with Pro Template). |

**CRITICAL: You must produce all files above. NO SKIP. The final script MUST follow the professional template format exactly.**

---

## Detailed Sub-Task Instructions

### 1. Generate Outline
- Categorize the 82 Q&A pairs into logical sections (e.g., Vision, Problem, Traction).
- Use section headers to group personas (Sam Altman, Seed VC, Series B, MIT).

### 2. Write Complete Pitch Text (`slide/text.md`)
- **Conversational Spoken Tone (STRICT):** Use professional Japanese (丁寧語/ですます調).
- **Dialogue Format:**
  - `(Q1: Criteria Name)`
  - `Persona Name：Question text...`
  - `(A1: Criteria Name)`
  - `創業者：Answer text...`
- **Emphasis:** Use `**keyword**` for emphasis. Do NOT use `[[ ]]` in this file.

### 3. Draft Google Slides Data (`slide/writing-slide/10min-slideData.json`)
- **JSON Structure:** Flat array of objects (`type`, `title`, `text`, `author`, `notes`).
- **Intro Slides:** Add a `content` type slide at the beginning of each persona's round.
- **Criteria Titles (CRITICAL):** The `title` field MUST use the **Criteria Title** from the judging criteria.
  - Format: `Q1: [[Criteria Title]]` and `A1: [[Criteria Title]]`.
- **Emphasis:**
  - `text` and `title`: Use `[[強調語]]` for blue emphasis.
  - `notes`: **PLAIN TEXT ONLY**. No markdown symbols.
- **Sequence:** Video Link -> Title -> Persona Intro -> Q1 -> A1 -> ... -> Closing.

### 4. Generate GAS Presentation Script (`slide/q-and-a-gas_presentation.js`)
- **MERGE PROCESS (CRITICAL):** Use the provided Python script to inject your JSON data into the **9,700+ line professional template**. Simplified scripts (under 3,000 lines) are strictly forbidden as they lack the "Pixel Perfect" styling engine.
  
  **Run Command:**
  ```bash
  python3 .agent/skills/q-and-a/scripts/merge_gas_presentation.py \
    --proposal-dir [PATH_TO_Q_AND_A_DIR]/slide \
    --sample-path .agent/skills/q-and-a/assets/q-and-a-gas-template.js
  ```
- **FINAL STEP:** Move the generated script to the root of the `slide` directory and verify it has the correct volume:
  ```bash
  mv [PATH_TO_Q_AND_A_DIR]/slide/writing-slide/10min-gas_presentation.js [PATH_TO_Q_AND_A_DIR]/slide/q-and-a-gas_presentation.js
  ```

---

## Validation Checklist
- [x] 82 Questions and 82 Answers (164 Q&A slides + titles/intros).
- [x] Titles follow the `Q1: [[Criteria]]` format using exact judging criteria names.
- [x] `notes` field is plain text (no `**` or `[[ ]]`).
- [x] Blue emphasis `[[ ]]` is used correctly in the `text` field.
- [x] Final script is generated via `merge_gas_presentation.py` and uses the 9,700+ line template.
- [x] Final file `slide/q-and-a-gas_presentation.js` is over 10,000 lines total.
