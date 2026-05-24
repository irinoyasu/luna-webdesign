# Writing Text & Slide Phase Reference

## Purpose

This phase involves creating the business plan narrative pitch and transforming it into a highly visual, persuasive Google Slides presentation. 

1. **Narrative Pitch:** Create a compelling, investor-focused pitch document that addresses market needs, reinforces contrarian insights, and demonstrates credibility.
2. **Visual Presentation:** Transform the written narrative into a 10-minute presentation perfectly adapted for speaking and visual scanning by investors.

> **📖 Required reading:** Before starting this phase, load and review [persuasive-writing-guide.md](../assets/persuasive-writing-guide.md) for detailed persuasive writing patterns, frameworks, and techniques.

## Inputs

**Process Dependencies:**
- **Phase 1-16 (Mandatory):** This phase is the ultimate synthesis. All preceding research, strategy, operations, team, and financial phases must be finalized.
- **Phase 13: Financials (Mandatory):** Key charts and ROI metrics for the financial slides.
- **Phase 15: Execution Planning (Mandatory):** Roadmaps and milestones for the execution slides, anchored in the release timing of product.

**You MUST synthesize information from ALL previously completed phases before drafting.** 
This phase is the culmination of the entire business planning pipeline. Your inputs include:
1. **Phase 1-16 Deliverables:** Comprehensive data from all prior research and strategy phases:
   - **Phase 1: Research** (`research/`)
   - **Phase 2: Problem & Opportunity Definition** (`problem/`)
   - **Phase 3: Solution** (`solution/`)
   - **Phase 4: Technology** (`technology/`)
   - **Phase 5: Business Model** (`business-model/`)
   - **Phase 6: Traction & Progress** (`traction-progress/`)
   - **Phase 7: Market** (`market/`)
   - **Phase 8: Competition** (`competition/`)
   - **Phase 9: Go-To-Market (GTM)** (`go-to-market/`)
   - **Phase 10: Operations** (`operations/`)
   - **Phase 11: Team** (`team/`)
   - **Phase 12: Purpose** (`purpose/`)
   - **Phase 13: Financials** (`financials/`)
   - **Phase 14: Insight** (`insight/`)
   - **Phase 15: Execution Planning** (`execution/`)
   - **Phase 16: Ask** (`ask/`)
2. **Existing Drafts:** Incorporate any files in `{output_folder}/businessplan-writing/writing-slide/` to ensure continuity.

## Sub-Task Index

| # | Sub-Task | Output File(s) | Description |
|---|---|---|---|
| 1 | Generate Narrative Outline | `writing-slide/pitch-outline.md` | A clear, logical structural outline of the 10-minute pitch divided by 18 specific sections. |
| 2 | Write Complete Pitch Text | `writing-slide/10min-text.md` | ONE structured text document containing the pitch narrative formatted for the required 10-minute duration based on the outline. |
| 3 | Draft 10-Minute Google Slides Data | `writing-slide/10min-slideData.json` | 10-minute presentation data JSON file based on the pitch text. |
| 4 | Generate Google Apps Script for Slides | `writing-slide/10min-gas_presentation.js` | Merged Google Apps Script for creating the presentation. |

**CRITICAL: You must produce all files above to complete this phase. NO SKIP.**

---

### 1. Generate Narrative Outline Instructions

**Dependencies:**
- **Phases 1-16 (Mandatory):** This phase is the ultimate synthesis. Every section in the outline must be directly mapped to the outputs of the preceding 16 phases.

**Goal:** Before writing full sentences, organize the content into a clear, logical structural outline. This ensures that the narrative flow is optimized and all critical data points from Phases 1-16 are accounted for.

### Required Outline Sections (STRICT RULE)
The outline MUST be saved as `writing-slide/pitch-outline.md` and contain these 18 sections in this EXACT order. For each section, list the **Key Data Points** and **Primary Message** derived from the previous phases.

1. **Video Link Slide:** Instructions for video placeholder.
2. **Title Slide:** Name, tagline, and high-level mission.
3. **Team:** Key founders, relevant experience, and "Why You" proof points.
4. **Problem:** Status Quo vs. Opportunity Cost (with quantitative metrics).
5. **Solution:** Core Feature and Value Prop (with quantitative metrics).
6. **Technology:** Underlying Magic and Strategic Value.
7. **Business Model:** Revenue streams and unit economics summary.
8. **Traction & Progress:** Key achievements and historical growth metrics.
9. **Market:** TAM/SAM/SOM and specific market catalysts.
10. **Competition:** Moat definition and competitive matrix positioning.
11. **Go-to-Market:** Acquisition strategy and CAC vs. LTV targets.
12. **Why Now:** Market/Technology catalysts making this the optimal moment.
13. **Execution Plan:** 12-24 month roadmap and immediate milestones based on the release timing of product.
14. **Purpose:** Mission/Vision and long-term societal/economic impact.
15. **Insight:** The contrarian truth or unique discovery driving the business.
16. **Financials:** 10-year P&L highlights and ROI expectations.
17. **The Ask / Next Steps:** Fundraising terms, use of proceeds, and closing timeline.
18. **Final Contact Slide:** Founder contact info and final call to action.

---

## 2. Write Complete Pitch Text Instructions

**Dependencies:**
- **Sub-task 17-1 (Outline):** Use the narrative outline as the structural frame for the complete pitch text.
- **Phase 12: Purpose:** Use the mission and vision for the emotional "hook" and conclusion.
- **Phase 14: Insight:** Use the contrarian truth as the intellectual core of the pitch.

### Narrative & Style Rules
- **Customer-First Language:** Use "you/your" at least 3× more than "we/our". Speak directly to their specific workflows and "walls."
- **BLUF (Bottom Line Up Front):** Lead every section with the most important conclusion (Assertion → Evidence → Benefit).
- **Proof Triangle:** Every major claim needs a Feature, Proof, and Benefit.
- **Ghost Competitor Technique:** Address competitor weaknesses indirectly without naming them.
- **Conciseness:** Short sentences (≤25 words), active voice, concrete nouns over abstract, numbers over adjectives.
- **Jargon-Free Language (STRICT RULE):** The text MUST be extremely easy to understand. Actively avoid jargon, complex technical language, internal project codes, and confusing acronyms (e.g., do not use contrived terms like "MIIP" or "Mobility Infotainment Infrastructure Platform" without clear, immediate, and simple explanations). Explain complex concepts in plain, descriptive language that an intelligent layperson or general investor can immediately grasp.
- **Conversational Spoken Tone (STRICT RULE):** Since this is a script for a presentation, use natural spoken language. Do NOT use noun-ending phrases (体言止め) like "〜のご提案". Instead, explicitly write out polite, fluent spoken sentences (e.g., "〜のご提案について、お話しさせていただきます。" or "〜についてご説明します。"). Furthermore, actively avoid unnatural "translated phrasing" such as "この" + adjective (e.g., avoid "この素晴らしい仕組み", "この強力なツール"). Use natural Japanese phrasing like "本提案の仕組み" or "本ツール" instead. Additionally, avoid exaggerated, emotional, or overly dramatic adjectives (e.g., avoid "驚異的な", "素晴らしい", "劇的に", "非常にスピーディーで明確な"). Keep the tone professional, objective, and natural for a Japanese B2B business pitch.
- **Emphasizing Key Words:** You MUST use markdown (e.g., **bold**) to emphasize key words. Do NOT use the `[[]]` syntax used for slides.

### 10-Minute speaking Instructions
You are required to draft the **10-minute verbal presentation text**.
- **Output File:** `writing-slide/10min-text.md`
- **Target Length Constraint (STRICT RULE):** You MUST write to these character targets: **1,200–1,300 words (English) / 3,000–3,500 characters (Japanese)**. This is calculated at about 130 words per minute for English, and 300-350 characters per minute for Japanese, making it a true 10-minute pitch. **CRITICAL:** Do NOT repeat paragraphs redundantly to artificially meet the character count. Ensure even distribution of speaking content across all sections.

---

## 3. Draft 10-Minute Google Slides Data Instructions

**Dependencies:**
- **Sub-task 17-2 (Pitch Text):** Transform the 10-minute verbal script into speaker notes and visual bullet points.
- **Phase 13: Financials:** Identify key charts and financial highlights for the slides.
- **Phase 15: Execution Planning:** Use the visual roadmap for the execution slides.

To draft the 10-Minute Google Slides (`writing-slide/10min-slideData.json`), you must rigidly adhere to these universal rules for the presentation structure.

### 1. File & Schema Constraints
- **Map to `slideData` Schema:** Strictly follow the detailed instructions in the reference `gem.prompt.md` to map the proposal to the exact JSON schema required.
- **Speaker Notes Total Volume Constraint (STRICT RULE):** You must strictly control the total sum of all `notes` texts across all slides to precisely match the target length of **3,000 – 3,500 characters** (JP) / 1,200 – 1,300 words (EN). Count only characters inside the `"notes"` fields (ignore spaces/JSON syntax). **CRITICAL:** Do NOT artificially bloat or repeat text on the last slide to meet this requirement. The notes must represent a natural, evenly distributed speech flow across all slides.
- **Jargon-Free Language (STRICT RULE):** Both the slide text and the speaker `notes` MUST avoid jargon, unnecessary or contrived acronyms (e.g., avoid confusing abbreviations like "MIIP"), and dense technical vocabulary. The final presentation and Google Slides MUST be extremely easy to understand for general investors. Express complex thoughts in simple, everyday language that any layperson can comprehend.
- **Conversational Spoken Tone (STRICT RULE):** All speaker `notes` MUST be written in natural spoken language that the speaker will actually say. Do NOT use noun-ending phrases (体言止め) like "〜のご提案". Instead, explicitly write out polite, fluent spoken sentences (e.g., "〜のご提案について、お話しさせていただきます。" or "〜についてご説明します。"). Furthermore, actively avoid unnatural "translated phrasing" such as "この" + adjective (e.g., avoid "この素晴らしい仕組み", "この強力なツール"). Use natural Japanese phrasing like "本提案の仕組み" or "本ツール" instead. Additionally, avoid exaggerated, emotional, or overly dramatic adjectives (e.g., avoid "驚異的な", "素晴らしい", "劇的に", "非常にスピーディーで明確な"). Keep the tone professional, objective, and natural for a Japanese B2B business pitch. Additionally, because the notes are read by Google Text To Speech, you must account for mispronunciations: never write "数倍" (which is read incorrectly), always explicitly write "すう倍" in the notes.
- **Emphasizing Key Words:** You MUST use `[[]]` (double square brackets) to emphasize key words in the slide text (e.g., `[[日米]]で[[粉体一筋]]27年`). The Google Apps Script uses this syntax to emphasize the words in blue color. You MUST NOT use markdown for emphasis in slides.

### 2. Required Slide Format (STRICT RULE)
The slides must be generated in this EXACT sequence and format:

1. **Video Link Slide:** The very first slide must ALWAYS be a title slide pointing to a video link:
   ```json
   {
      "type": "title",
      "title": "説明動画をクリック",
      "hyperlinkText": "[URL of tinyurl]",
      "date": " ",
      "notes": "説明動画へのリンクをクリックして下さい。"
   }
   ```

2. **Title Slide:** Include one slide for the presentation title.
   **CRITICAL INSTRUCTION:** Think about the title of the proposal and the notes of the proposal based on the output of `writing-slide/10min-text.md`.
   ```json
   {
      "type": "title",
      "title": "[[Title of the proposal]]",
      "date": " ",
      "notes": "[Title]について、お話しさせていただきます。"
   }
   ```

3. **Required Sequence Continues:** Follow the sequence below, mapping content from the 10-Minute Pitch Text:
   - **Team**
   - **Problem:** Type `headerCards`, Status Quo & Opportunity Cost.
   - **Solution:** Type `headerCards`, Core Feature & Value Prop.
   - **Technology:** Type `headerCards`, Underlying Magic & Strategic Value.
   - **Business Model**
   - **Traction & Progress**
   - **Market**
   - **Competition:** Matrix/Axis comparison.
   - **Go-to-Market:** CAC vs LTV.
   - **Why Now**
   - **Execution Plan**
   - **Purpose**
   - **Insight**
   - **Financials**
   - **The Ask / Next Steps**

4. **Final Contact Slide:** Include the final slide for contact information.
   ```json
   {
      "type": "bulletCards",
      "title": "連絡先",
      "subhead": " ",
      "items": [
            {
               "title": "○○株式会社 代表取締役 △△ △△",
               "desc": "[[[EMAIL_ADDRESS]]]\n+ 81 - 90 - 1234 - 5678(Japan)\n+ 1 - 123 - 456 - 7890(US)"
            }
      ],
      "notes": "お時間をいただき、ありがとうございました。\n連絡先は、○○までよろしくお願いします。"
   }
   ```

---

## 4. Generate Google Apps Script for Slides Instructions (THE "TOTAL FILE" RULE)

1. **Automated Generation:** Use the Python script `scripts/merge_gas_presentation.py`.
2. Run:
   ```bash
   python /Users/yasutakairino/businessplan/.agent/skills/proposal-writing/scripts/merge_gas_presentation.py \
     --proposal-dir [PATH_TO_PROPOSAL_DIR] \
     --sample-path /Users/yasutakairino/businessplan/.agent/skills/businessplan-writing/assets/gas_presentation_sample.js
   ```

## Phase Validation Checklist

- [ ] Narrative Outline generated in the `writing-slide/` folder.
- [ ] Outline contains ALL 18 required sections in the correct order.
- [ ] The 10-minute pitch script is generated in the `writing-slide/` folder.
- [ ] Pitch script adheres to length constraints (3,000-3,500 JP chars / 1,200-1,300 EN words).
- [ ] **Universal Rules passed:** No raw English jargon headers, clear conversational explanations used.
- [ ] Google Slides `slideData` generated AND merged into the full boilerplate.
- [ ] **Speaker notes character count explicitly verified** to fall within the calibrated range.
- [ ] **Content strict mapping:** Both text and slides contain ALL critical sections in the required order.
- [ ] Phase deliverables stored in `writing-slide/` folder.
