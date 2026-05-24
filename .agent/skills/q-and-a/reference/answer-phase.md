# Phase 2: Answer Generation (Business Plan Synthesis) Reference

## Purpose

Synthesizing professional, evidence-backed answers for each generated question based on the existing business plan deliverables (Phases 1-16). This phase ensures that the business plan and the Q&A responses are logically consistent and data-driven.

## Inputs

**You MUST synthesize information from ALL previously completed business plan phases before drafting.**
Your inputs include:
1. **Questions:** Generated in Phase 1 (`question/questions-[persona].md`).
2. **Business Plan Deliverables:** Analysis of all directories and files in `businessplan-writing/` folder.

## Outputs
Answer for each question.

## Sub-Task Index

| # | Sub-Task | Output File(s) | Description |
|---|---|---|---|
| 1 | Synthesize Answers (Sam Altman) | `answer/answers-altman.md` | Evidence-backed answers for Sam Altman's 23 questions. |
| 2 | Synthesize Answers (Seed Stage VC) | `answer/answers-seed-vc.md` | Evidence-backed answers for Seed Stage VC's 13 questions. |
| 3 | Synthesize Answers (Series B Stage VC) | `answer/answers-series-b-vc.md` | Evidence-backed answers for Series B Stage VC's 30 questions. |
| 4 | Synthesize Answers (MIT Business Plan Contest) | `answer/answers-mit.md` | Evidence-backed answers for MIT Business Plan Contest's 16 questions. |

## Detailed Sub-Task Instructions

### General Principles for All Personas
- **One Answer per Question**: You MUST generate a professional, evidence-backed answer for every question generated in Phase 1.
- **Evidence-Backed Logic**: Every claim must be supported by data from the `businessplan-writing/` folder.
- **Tone & Style**: Use natural, professional spoken Japanese (丁寧語/ですます調). Avoid noun-ending phrases (体言止め).
- **Markdown Formatting**: Use **bold** for emphasis. Do NOT use `[[ ]]`.
- **Citations**: Explicitly cite the source file (e.g., `market-size.md`) for every data point.

### 1. Synthesize Answers (Sam Altman)
- **Input**: `question/questions-altman.md` (23 questions).
- **Focus**: Synthesize answers that demonstrate moonshot potential, contrarian truths, and extreme founder resourcefulness.
- **Output**: Save results to `answer/answers-altman.md`.

### 2. Synthesize Answers (Seed Stage VC)
- **Input**: `question/questions-seed-vc.md` (13 questions).
- **Focus**: Provide realistic, operational answers regarding early-stage survival, MVP traction, and immediate GTM strategies.
- **Output**: Save results to `answer/answers-seed-vc.md`.

### 3. Synthesize Answers (Series B Stage VC)
- **Input**: `question/questions-series-b-vc.md` (30 questions).
- **Focus**: Focus on unit economics at scale, predictable growth engines, organizational structure, and international expansion.
- **Output**: Save results to `answer/answers-series-b-vc.md`.

### 4. Synthesize Answers (MIT Business Plan Contest)
- **Input**: `question/questions-mit.md` (16 questions).
- **Focus**: Ensure logical consistency, academic realism, and a balanced view of team quality and market leadership.
- **Output**: Save results to `answer/answers-mit.md`.

## Answer Strategy & Style Rules

### Evidence-Backed Logic
- **Direct Search:** Search the specific folders in the business plan for supporting data.
- **Quantitative Metrics:** Use real numbers from the business plan to support claims.
- **Source Citations:** Cite the specific business plan phase or data file used.

### Professional Presentation
- **Direct Response:** Address the core of the question immediately (Assertion → Evidence → Benefit).
- **Tone:** Professional, objective, and natural for a Japanese business pitch.
- **Tone Rules:** Use natural professional spoken Japanese. Avoid noun-ending phrases (体言止め).
- **Data Integrity**: Every answer must cite a source from the 16 phases of the business plan.
- **Emphasizing Key Words:** Use markdown (e.g., **bold**) to emphasize key words. Do NOT use the `[[]]` syntax used for slides.

## Phase Validation Checklist

- [ ] Every question from Phase 1 has a corresponding answer in the respective persona file.
- [ ] Answers are logically consistent with the current business plan.
- [ ] Quantitative data and proof points are correctly cited from the business plan.
- [ ] Output saved to the correct `answer/answers-[persona].md` file.
