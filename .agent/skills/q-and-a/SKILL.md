---
name: q-and-a
description: >
  Create a comprehensive Q&A session for a business plan based on four key personas:
  Sam Altman, Seed VC (Incubate Fund), Series B VC, and MIT Business Plan Contest. This skill generates
  challenging questions, synthesizes answers from existing business plan data,
  and produces a visual slide deck using the 'quote' slide type. Use this skill
  when the user wants to prepare for an investor meeting, stress-test their
  startup idea, or generate a pitch rehearsal deck.
---

# Q&A Strategy Skill

This skill automates the creation of a high-impact Q&A session by simulating different investor and founder perspectives. It follows a structured 3-phase workflow to ensure persona persistence, evidence-backed synthesis, and professional presentation output ready for Google Slides automation.

## Workflow Overview

The Q&A process follows these **3 phases in strict sequential order**:

1. **Question Generation (Persona Persistence)** — Generate questions by deep-diving into the business plan through the eyes of four distinct investor personas.
2. **Answer Generation (Business Plan Synthesis)** — Generate answers based on the questions generated in phase 1 and evidence-backed answers that bridge strategy with data.
3. **Google Slides Generation (Strict Protocol)** — Convert the Q&A pairs into a presentation deck using the `slideData` schema.

## How to Use This Skill

### Step 1: Set Up Project Directory

Initialize the Q&A output folder within the main business plan directory:

```
{output_folder}/q-and-a/
├── question/           # Phase 1: Generated questions
├── answer/             # Phase 2: Q&A pairs
├── slide/               # Phase 3: Presentation data
└── progress-tracker.md  # Mandatory tracking
```

## Execution Principles (STRICT REQUIREMENT)

- **FULL CONTENT GENERATION:** You MUST generate the complete content for every persona and every Q&A pair.
- **NO PLACEHOLDERS:** Phrases like "(以下、...を展開)", "(Rest of questions...)", or "..." are strictly forbidden. Every single question (82 total) and every single answer (82 total) MUST be written out in full in the `slide/text.md` file and other deliverables.
- **Conversational Tone:** All Japanese output MUST use professional, natural spoken language (丁寧語/ですます調). Noun-ending phrases (体言止め) are forbidden.

For each phase:
1. **Load Phase Reference**: Read the corresponding file in `reference/`.
2. **Execute Sub-tasks**: Follow the instructions for each step.
3. **Draft & Save**: research → draft → produce deliverable → validate.
4. **Iterative Batching**: Generate questions for each persona (Altman, Seed, Series B, MIT) as separate sub-tasks.
5. **Update Tracker**: Move to the next sub-task only after checking off the previous one.

## Phase Reference Files

| Phase | Reference Document |
|---|---|
| 1. Question Generation | [reference/question-phase.md](reference/question-phase.md) |
| 2. Answer Generation | [reference/answer-phase.md](reference/answer-phase.md) |
| 3. Google Slides Generation | [reference/slide-phase.md](reference/slide-phase.md) |
