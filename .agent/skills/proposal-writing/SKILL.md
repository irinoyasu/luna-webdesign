---
name: proposal-writing
description: >
  Comprehensive proposal writing following an 11-phase methodology inspired by
  Shipley/APMP best practices and modern B2B sales proposal research.
  Phases run in strict order: Research → Problem & Opportunity Definition → Strategy → Solution Design → Costing & Pricing → ROI Calculation → Execution Planning → Writing → Presentation Generation → Review → Delivery.
  Use when the user asks to "write a proposal", "create a proposal", "respond to an RFP",
  "bid on a contract", "prepare a tender", "draft a proposal response",
  "write a sales proposal", "create a business proposal", "write a project proposal",
  or mentions proposal phases such as capture planning, opportunity qualification,
  RFP analysis, win themes, value proposition, solution storyboard, 
  technical volume, pricing strategy, compliance matrix, color team reviews
  (pink team, red team, gold team), or pitch preparation.
  Supports RFP responses, unsolicited sales proposals, and internal proposals.
  Supports bilingual (JP/EN) output with quantitative metrics and source citations.
---

# Proposal Writing Skill

Create winning, customer-focused proposals through a structured 11-phase methodology grounded in Shipley/APMP best practices and modern B2B sales research. Each phase builds on outputs from previous phases to produce a cohesive, compliant, and persuasive proposal — and then converts it into a concrete day-by-day execution plan.

## Core Philosophy

### Customer is the Hero
The customer is the main character of the proposal story. You are their trusted guide — the one who understands their challenges and shows them a clear path to success. Write about *their* world, not yours.

### Define the Problem First (The "55 Minutes" Rule)
*“If I had an hour to solve a problem I would spend 55 minutes thinking about the problem and 5 minutes thinking about the solution.”*
A perfect solution to the wrong problem will fail. Separate the *problem* (e.g., "Wait times are 20 mins") from the *missing solution* (e.g., "We need a chatbot").
1. **Look Inward:** Audit your own biases (confirmation, internal, survivorship) and solution-first thinking before framing.
2. **Apply Empathy:** Use the narrative framework — **I am** [Persona], **Trying to** [Outcome], **But** [Barrier], **Because** [Root Cause], **Which makes me feel** [Emotion].
3. **Look Outward:** Research who else has the problem, who has been left out, and who benefits from the status quo.
Always dig for the root cause using the "5 Whys" and quantify the impact before designing a solution.

### Atomic Problems & Solutions (The "One Per File/Section/Slide" Rule)
Never combine multiple distinct problems or multiple distinct solutions into a single section, paragraph, or slide. Every distinct problem (e.g., "SEO visibility is poor" vs. "Lack of 3D models") MUST be completely separated into its own standalone, atomic Problem/Solution pair. Similarly, different solutions (e.g., "Permanent physical exhibition" vs. "Diagnostic tool") MUST NOT be combined. Grouping disparate problems or solutions together dilutes the message and causes structural errors later in the pipeline.

### Evidence Over Assertion
Every claim needs proof. Use the **Proof Triangle** for every major point:
- **Feature** — What it is (capability, approach, tool)
- **Proof** — That it works (case study, metric, certification, testimonial)
- **Benefit** — Why the customer cares (outcome in their terms)

### BLUF (Bottom Line Up Front)
Lead every section with the most important conclusion, then support with evidence. Evaluators may only read the first paragraph of each section.

### Simple, Clear Language (No Jargon)
Always follow the style and tone guidelines in `assets/persuasive-writing-guide.md`. The explanation must be simple, straightforward, and easily understandable by someone with *no background* in your field. Do not use confusing jargon, buzzwords, or insider terms (e.g., instead of confusing phrases like "Compliance Hub," use concrete, self-explanatory phrases). Ensure a professional, objective B2B tone. Actively avoid exaggerated, emotional, or overly dramatic adjectives (e.g., "驚異的な", "素晴らしい", "劇的に", "非常にスピーディーで明確な"). Use natural phrasing instead.

---

## Workflow Overview

The proposal follows these **11 phases in strict sequential order**:

1. **Research** — Research the customer, qualify the opportunity, and deep-search both your competitive landscape and the customer's market dynamics (their customers & competitors) via active web research
2. **Problem & Opportunity Definition** — Execute three steps: **1) Look Inward** (audit proposer biases/assumptions), **2) Look Outward & Reframe** (define problems through an empathetic "Persona/Outcome/Barrier/Root Cause/Emotion" narrative and "How Might We" statements), and **3) Define Opportunities** (map As-Is to To-Be, including solution-led innovations). Conduct **Persona Analysis**, **Customer Journey Mapping**, and **Jobs To Be Done (JTBD)** analysis for both the direct customer and their end-users.
3. **Strategy** — Develop win themes, define differentiators, craft audience-specific value propositions
4. **Solution Design** — Design the proposed solution architecture including detailed features, benefits, implementers, deliverables, timeline, and team
5. **Costing & Pricing** — Estimate delivery costs (bottom-up), build pricing strategy, **model Revenue KPIs** (sales funnel stages — Awareness → Interest → Consideration → Purchase — with conversion rates at each stage, Customer Lifetime Value / LTV, Customer Acquisition Cost / CAC, and monthly revenue ramp-up), and prepare pricing presentation. The revenue model output feeds directly into Phase 6 ROI Calculation.
6. **ROI Calculation** — First, calculate the exact KPI numbers (Payback Period, total cash outflows, total cash inflows, total cash flows, Minimum cumulative cash flow (最小必要資金), NPV, Return Multiple, and IRR) utilizing the included `calculate_roi.py` script. **Crucial Definition:** "Minimum cumulative cash flow" is the absolute lowest point of the cumulative net cash flows. It represents the maximum funding the project requires before breaking even, NOT just Year 1 costs. Second, **write a narrative explanation with the key numbers like a story so that the audience can smoothly understand the financial impact.** **(MUST consume all 4 output files from Costing & Pricing — including `revenue-kpi-model.md` with its funnel conversion rates and LTV — as direct inputs to ensure mathematical alignment).**
7. **Execution Planning** — Convert the solution and pricing into a concrete day-by-day action plan with deliverables, owners, dependencies, milestones, and risk contingencies
8. **Writing Text** — Draft the proposal document: pitch version, solution narrative, credentials, pricing section, execution schedule. **(MUST strictly map and reflect every single problem and solution from the Phase 4 `solution-design.md` matrix. Omissions are prohibited.)**
9. **Writing Slide** — Draft Google Slides: `slideData.json` files and run the merge script to generate `gas_presentation.js`. **(MUST run the automated `scripts/merge_gas_presentation.py` script to generate the final 9,000+ line Google Apps Script files).**
10. **Review** — Run quality reviews (compliance, persuasiveness, accuracy), refine and finalize
11. **Delivery** — Package deliverables, submit proposal, prepare pitch materials, plan follow-up

> **Critical (FATAL ERROR WARNING):** You are expressly forbidden from skipping phases or jumping ahead. If a user asks you to "write a proposal", you MUST execute Phase 1, then Phase 2, then Phase 3, 4, 5, 6, 7, 8, 9, 10, and 11. There are no shortcuts. Do not jump to the "Writing" phase directly. Skipping a phase is considered a critical failure of the AI.
> **Mandatory Completeness:** For every sub-task defined in the phase reference, you MUST produce ALL outputs for ALL required versions. Do not ask for permission to skip unless there is a physical constraint.
> The Execution Plan feeds directly into the Writing phase — the day-by-day schedule becomes part of the proposal itself.
> Getting strategy wrong makes execution worthless — invest time in phases 1-5.

---

## Proposal Types

Determine the proposal type before starting. Each type has different emphasis:

### RFP Response
Formal response to a published solicitation. Full 6-phase process. **Compliance is paramount** — every requirement must be addressed and traceable.

### Unsolicited Proposal (Sales Proposal)
Proactive proposal to a prospective customer. The most common type for B2B sales. **Persuasion is paramount** — you must create the sense of need and urgency, not just respond to it.

Key differences from RFP response:
- Research phase replaces RFP analysis with deep customer/market research
- **Research phase MUST include Deep Search for both Competitive Landscape AND the Customer's Market Dynamics (their customers & competitors)** — use active web research and URL reading capabilities to actively research direct/indirect competitors, the customer's end-users, and the challenges the customer faces in their own market. Do NOT rely on assumptions.
- No compliance matrix needed, but "customer fit" validation is critical
- Proposal can be shorter and more narrative-focused (aim for under 15 pages)
- Pitch and follow-up strategy are more important than formal submission

### Internal Proposal
Project proposal within an organization. **Business case is paramount** — focus on ROI, stakeholder alignment, and risk mitigation.

---

## How to Use This Skill

### Step 0: Prerequisites (MUST READ)
Before starting any work on a proposal task, you MUST read the following files in this order:
1. `SKILL.md` (this file)
2. `assets/design-system.md` (Japanese Consulting Design System & Format Rules)

### Step 1: Determine Scope and Type

Ask the user:
1. What type of proposal? (RFP response / unsolicited / internal)
2. Who is the customer? (name, industry, size, geography)
3. What is the opportunity? (project description, estimated value, deadlines)
4. Any existing materials? (RFP documents, customer research, past proposals, company profiles, case studies)
5. Which phases to include? (full / selective — default: full)

### Step 2: Set Up Output

Create the output directory structure:

```
{output_folder}/proposal/
├── research/
├── problem/
├── strategy/
├── solution/
├── costing/
├── roi/
├── execution/
├── writing-text/
├── writing-slide/
├── review/
└── delivery/
```

### Step 3: Execute Phases Sequentially (STRICT REQUIREMENT)

**FATAL ERROR WARNING**: You cannot jump to Phase 8 (Writing Text) just because the user asked for a proposal. You must complete Phases 1-7 first.

**Mandatory Progress Tracker**: Before beginning the first phase, you MUST create a master checklist file: `{output_folder}/proposal/progress-tracker.md`. You must list every phase and sub-task defined in the reference files, and check them off only when they are 100% complete.

For each phase:
1. **Load Reference**: Read the corresponding phase reference file (e.g., read `references/strategy-phase.md` ONLY when you reach Phase 2).
2. **Execute Every Sub-task**: Review the sub-task index in the reference file. You are strictly required to execute EVERY sub-task. Before drafting any file, ensure the prior steps in the phase are complete. Do not ask the user if you should skip unless there is a specific technical reason.
3. **Draft & Save**: For each sub-task: analyze → draft → validate → finalize. Save the output to the designated path.
4. **Iterative Batch Processing:** If a sub-task requires multiple outputs, generate them all in a single turn if possible, do not stop until the set is complete.
5. **Update Tracker**: Update your `progress-tracker.md` to check off the completed sub-task before moving to the next one.
6. Summarize phase outputs before moving to the next phase.

### Step 4: Validate and Consolidate

After all phases complete, consolidate into:
- Overall readiness assessment
- Compliance score (for RFP responses: percentage of requirements addressed)
- Unresolved risks and mitigations
- Follow-up actions with owners and deadlines

---

## Phase Reference Files

Load the relevant reference file **only when working on that phase**:

| Phase | Reference File |
|---|---|
| 0. Design System | [assets/design-system.md](assets/design-system.md) |
| 1. Research | [references/research-phase.md](references/research-phase.md) |
| 2. Problem & Opportunity Definition (Look Inward, Outward & Reframe) | [references/problem-opportunity-definition-phase.md](references/problem-opportunity-definition-phase.md) |
| 3. Strategy | [references/strategy-phase.md](references/strategy-phase.md) |
| 4. Solution Design | [references/solution-design-phase.md](references/solution-design-phase.md) |
| 5. Costing & Pricing | [references/costing-pricing-phase.md](references/costing-pricing-phase.md) |
| 6. ROI Calculation | [references/roi-calculation-phase.md](references/roi-calculation-phase.md) |
| 7. Execution Planning | [references/execution-planning-phase.md](references/execution-planning-phase.md) |
| 8. Writing Text | [references/writing-text-phase.md](references/writing-text-phase.md) |
| 9. Writing Slide | [references/writing-slide-phase.md](references/writing-slide-phase.md) |
| 10. Review | [references/review-phase.md](references/review-phase.md) |
| 11. Delivery | [references/delivery-phase.md](references/delivery-phase.md) |

For persuasive writing patterns applicable across all writing sub-tasks, see:
[assets/persuasive-writing-guide.md](assets/persuasive-writing-guide.md)

---

## Output Conventions

All deliverables follow these conventions:
- **Customer-first language** — Write about the customer's needs, not your capabilities. Use "you/your" 3× more than "we/our"
- **Quantitative & Qualitative metrics** — Wherever Opportunity Cost (機会損失) or Benefits (利点) are defined, you **MUST** use both a quantitative metric and a qualitative narrative.
- **Bilingual labels** (JP/EN) for key terms when requested
- **Emphasizing Key Words:** In markdown text files (Phase 8), use standard markdown formatting (e.g. **bold**) to emphasize key words. In JSON slide data (Phase 9), use double square brackets (e.g. `[[keyword]]`) to emphasize key words.
- **Source citations** for every claim or data point
- **Concise prose** — Short sentences (≤25 words), short paragraphs (≤5 sentences), active voice
- **Standard footer** on each deliverable:

```markdown
---
## Status & Next Steps
- **Decisions made:**
- **Risks / blockers + owners:**
- **Open items / research backlog:**
```

---

## Validation Checklist

After each sub-task:
- [ ] Customer needs explicitly addressed with evidence
- [ ] Win themes reinforced with proof points
- [ ] Every claim cites a source
- [ ] Compliance references annotated where applicable (RFP responses)
- [ ] Output saved to the correct path

After each phase:
- [ ] All selected sub-tasks completed
- [ ] Deliverables stored in output folder
- [ ] Risks/blockers documented in summary
- [ ] Phase status communicated to user
