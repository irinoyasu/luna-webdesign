# Writing Text Phase Reference

## Purpose

The purpose of this phase is to create a proposal in narrative. Transform your strategy, solution design, and pricing into a compelling, customer-focused proposal document. Every section must address customer needs, reinforce win themes, and demonstrate credibility.

**Key principle:** The proposal is written for the *reader*, not the writer. Busy decision-makers will scan, not study. Lead with conclusions, use visual hierarchy, and make every paragraph earn its place.

> **📖 Required reading:** Before starting this phase, load and review [persuasive-writing-guide.md](../assets/persuasive-writing-guide.md) for detailed persuasive writing patterns, frameworks, and techniques that apply to every sub-task in this phase.

## Inputs

**You MUST synthesize information from ALL files created in ALL previous phases before writing.** 
The proposal text is the culmination of the entire skill pipeline. Your inputs include, but are not limited to:
- **Phase 1-2:** Research & Problem/Opportunity Definition (customer logic, specific pain points)
- **Phase 3-4:** Strategy & Solution Design (win themes, competitive positioning, tracing matrix)
- **Phase 5-6:** Costing & Pricing and ROI Calculation (pricing models, NPV, IRR, narrative financial impacts)
- **Phase 7:** Execution Planning (implementation timelines, resource mapping, risk mitigation)

## Task

| # | Task | Output File(s) | Description |
|---|---|---|---|
| 1 | Write Complete Proposals | `writing-text/10min-text.md` | ONE structured proposal document containing the pitch narrative formatted for the required 10-minute duration. |

**CRITICAL: You must produce the 1 file above to complete this phase. NO SKIP.** If the user asks for "a proposal," they expect the full deliverable.

---

## Narrative & Style Rules
- **Customer-First Language:** Use "you/your" at least 3× more than "we/our". Speak directly to their specific workflows and "walls."
- **BLUF (Bottom Line Up Front):** Lead every section with the most important conclusion (Assertion → Evidence → Benefit).
- **Proof Triangle:** Every major claim needs a Feature, Proof, and Benefit.
- **Ghost Competitor Technique:** Address competitor weaknesses indirectly without naming them.
- **Conciseness:** Short sentences (≤25 words), active voice, concrete nouns over abstract, numbers over adjectives.
- **Conversational Spoken Tone (STRICT RULE):** Since this is a script for a presentation, use natural spoken language. Do NOT use noun-ending phrases (体言止め) like "〜のご提案". Instead, explicitly write out polite, spoken sentences (e.g., "〜のご提案について、お話しさせていただきます。"). Furthermore, actively avoid unnatural "translated phrasing" such as "この" + adjective (e.g., avoid "この素晴らしい仕組み", "この強力なツール"). Use natural Japanese phrasing like "本提案の仕組み" or "本ツール" instead. Additionally, avoid exaggerated, emotional, or overly dramatic adjectives (e.g., avoid "驚異的な", "素晴らしい", "劇的に", "非常にスピーディーで明確な"). Keep the tone professional, objective, and natural for a Japanese B2B business pitch.
- **Emphasizing Key Words:** You MUST use markdown (e.g., **bold**) to emphasize key words. Do NOT use the `[[]]` syntax used for slides.

---

## 10-Minute Proposal Instructions

You are required to draft the **10-minute verbal presentation text**.
- **Output File:** `writing-text/10min-text.md`
- **Target Length Constraint (STRICT RULE):** You MUST write to these character targets: **1,200–1,300 words (English) / 3,000–3,500 characters (Japanese)**. This is calculated at about 130 words per minute for English, and 300-350 characters per minute for Japanese, making it a true 10-minute pitch. **CRITICAL:** Do NOT repeat paragraphs redundantly to artificially meet the character count. Ensure even distribution of speaking content across all sections.

### Structure & Content Requirements (STRICT RULE)
The 10-minute text proposal MUST PERFECTLY mirror the following structure and content flow. Omissions or reordering are prohibited. Use this EXACT order:

1. **Video Link Section:** Must start with a section indicating a video link (e.g., "説明動画をクリック" and "説明動画へのリンクをクリックして下さい。").
2. **Title Section:** Include a section for the presentation title immediately after the video link.
3. **Self-Introduction & Company Introduction:** Give a brief personal and company introduction.
4. **Effort Summary ("本提案のために実施した作業"):** Immediately following the introduction, you MUST list the exact evaluation steps used to create the proposal in this format:
   `この提案を作成するために、調査、課題の定義、解決策の定義、実施計画、コスト見積り、投資対効果の計算の順に作業を行いました。`
5. **Problem/Solution Pairs:** 
    - **All Pairs Required:** You must include *ALL* pairs mapped from `solution-design.md`.
    - **Consecutive Pairing:** Structure the narrative flow so that EVERY problem is immediately followed by its corresponding solution. You are prohibited from grouping all problems into one section and all solutions into another. Present them as sequential "pairs".
    - **ONE PROBLEM = ONE PAIR (STRICT SPLIT RULE):** Each pair must represent exactly ONE atomic problem and ONE atomic solution. You MUST NOT put different problems into one section. For example, "用語の違いによる検索機会の損失" and "3Dデータ提供の不足" are two entirely different problems. They MUST be separated into two distinct problem sections. Similarly, you MUST NOT put two different solutions in one section. For example, "実機常設展示" and "診断ツール" are two different solutions. They MUST be separated into two distinct solution sections. Likewise, "30-second AI avatar videos" and "2-minute loop technical explanation videos" are TWO different solutions to TWO different problems and MUST be split. Do not combine multiple different issues or solutions into a single section/paragraph.
    - **Clear Explanation in Native Language:** Titles and subheads MUST be translated and expanded into simple, straightforward, jargon-free explanations requiring no prior knowledge. You MUST NOT use raw English labels, jargon, or acronyms directly if they are not instantly understandable. 
    - **Problem Content:** For every problem, you MUST explicitly define **"現状"** and **"機会損失"**. Under **"現状"**, you MUST weave in the empathetic narrative:
      - **Persona:** Describe the specific user ("I am...").
      - **Outcome:** Describe what they are trying to achieve ("Trying to...").
      - **Barriers & Emotional Impact:** Describe the struggle and frustration ("But...", "which makes me feel...").
      - **Root Cause:** Address why it's happening ("Because...").
      - The "機会損失" (Opportunity Cost) MUST include both a quantitative metric and a qualitative narrative.
    - **Solution Content:** For every solution, you MUST explicitly define **"特徴"** and **"利点"**. The "利点" (Benefits) MUST include both a quantitative metric and a qualitative narrative.
    - **Depth:** Expand deeply on the nuances, mechanics, and financial impacts of every single solution in the narrative.
    - **Example for a problem section:**
      ```markdown
      ## 課題1：海外での声掛けに対する心理的障壁
      **現状:**
      私は**展示会の現場担当者**ですが、ネイティブではない英語で来場者に話しかけることに強い**不安**を感じています。本当は来場者の足を止め、自社の技術を**熱心に伝えたい**のですが、いざとなると言葉が詰まり、見送ってしまうことが多々あります。これは、単なる語学力の不足ではなく、**「失敗してはいけない」という強いプレッシャー**が原因であり、そのたびに**「チャンスを逃した」という無力感**に苛まれます。
      
      **機会損失:**
      日本の展示会なら1日に**300人**ほどに声掛けできますが、海外の展示会だと心理的障壁により**50人**程度にとどまってしまうこともあります。これにより、見込み顧客獲得数が**80%以上毀損**しています。
      ```
    - **Example for a solution section:**
      ```markdown
      ## 解決策1：話しかけ用のAI動画を作成
      **特徴:**
      **30秒**の動画でアピールします。**iPad**に表示させます。声もマネる**AIクローン**を作成することもできます。
      
      **利点:**
      ネイティブスピーカーでなくても**誰でも簡単**に、画面を見せるだけで済みます。これにより、ブースへの来訪者数が**数倍**になります。
      ```

6. **Video Demo Section:** Only if a image file that fits the solution exists in input directory,insert a demo section immediately after the each solution section.
    - **Example for a demo section:**
      ```markdown
      ## [[Product name]]
      Image of the product
      
      **50** years in **Japan**
      Hi, give me just 30 seconds. We are a [[Product name]] manufacturer. We have a history of 50 years in Japan. 
      ```

7. **Investment Breakdown:** Include exactly one dedicated section for the Investment. Never combine this directly with the ROI section.

8. **Return On Investment (ROI):** Include the exact numerical metrics and narrative explanation based on, but not limited to Phase 6 (`roi/financial-impact.md`).Ensure you include the following metrics:
  - Required Funding
  - Break-even point
  - Payback Period
  - Multiple on Invested Capital (MOIC)
  - Net Present Value (NPV)
  - Internal Rate of Return (IRR)

9. **Next Steps:** Include exactly one dedicated section for the Next Steps based on Phase 7 (`execution-plan/implementation-plan.md`).

10. **Contact Information:** The final section must provide the contact information:
  Example:
   - ○○株式会社 代表取締役 ○○ ○○
   - [EMAIL_ADDRESS]
   - +81-90-1234-5678(Japan)

---

## RFP Response Guidelines (If Applicable)

If an RFP is provided, follow the customer's prescribed structure above all else. Mirror their section numbering and headings.
- Include a compliance matrix (requirement → response → page reference).
- Embed the proof triangle (feature → proof → benefit) directly under their requirements.
- Ensure every graphic MUST have an action caption (e.g., "Figure 3: Our phased approach delivers market presence 12 months faster", not just "Figure 3: Project Timeline").

---

## Phase Validation Checklist

- [ ] The 10-minute pitch duration is generated in the `writing-text/` folder.
- [ ] **Universal Rules passed:** No raw English jargon headers (Clear Explanations used), "本提案のために実施した作業" (Effort Summary) is strictly present, and Investment/ROI are separated.
- [ ] **Length Rules passed:** The pitch version aligns with the specific word/character counts documented in the sections above.
- [ ] **10-Min strict mapping:** The 10-minute pitch contains ALL problem-solution pairs exactly derived from `solution-design.md`. None are missing.
