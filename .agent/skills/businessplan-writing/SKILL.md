---
name: businessplan-writing
description: >
  Comprehensive business plan creation following a 17-phase sequential methodology.
  Use when the user asks to "write a business plan", "create a business plan",
  "develop a startup plan", "build an investor pitch", "plan a new venture",
  "greenfield business planning", or mentions business plan phases such as
  problem definition, solution design, business model, market analysis,
  competition analysis, go-to-market strategy (marketing and sales),
  operations planning, technology roadmap, team planning, purpose/mission/vision,
  financial projections, investor insights, executive summary, or pitch deck creation.
  Supports bilingual (JP/EN) output with quantitative metrics and source citations.
  Includes a financials spreadsheet template for detailed financial modeling.
  Integrates with the `google-sheets` skill to generate live financial statements.
---

# Business Plan Skill

Create comprehensive, investor-ready business plans through a structured 17-phase sequential workflow. Each phase builds on the outputs of previous phases to produce a cohesive, evidence-based business plan.

## Workflow Overview

The business plan follows these **17 phases in strict sequential order**:

1. **Research** — Deep search on Company, Competitors, and Customer context
2. **Problem & Opportunity Definition** — Define customer problems (As-Is/To-Be) and solution-led opportunities, write personas, map JTBD, and plot customer journeys
3. **Solution** — Define features, user stories, product name, benefits, domain, catchphrase, pricing, value proposition canvas, and economic/emotional value
4. **Technology** — Write technology behind the solution, intellectual property strategy, development roadmap, research items
5. **Business Model** — Define business model name, cost structure, and revenue streams
6. **Traction & Progress** — Document current achievements, metrics, milestones, and product roadmap
7. **Market** — Analyze market size (TAM/SAM/SOM), characteristics, growth rate, PEST analysis, and five forces
8. **Competition** — Analyze direct/indirect competitors, substitutes, comparison criteria, and competitive advantage
9. **Go-To-Market (GTM)** — Integrated Marketing and Sales strategy: channel tactics, sales pipeline, funnel analysis, KPIs, traction proof points, and budget
10. **Operations** — Plan all operational functions (corporate planning, customer service, finance, HR, IT, logistics, marketing ops, production, sales ops)
11. **Team** — Create org chart, company profile, corporate culture, recruitment policy, team member profiles
12. **Purpose** — Define mission, vision, and values
13. **Financials** — Comprehensive financial modeling: P&L, balance sheet, cash flow, valuation (DCF, EBITDA, comparables), fundraising plan, investor terms. Managed via JSON data files with an Excel template for calculation reference. Integrates with Google Sheets for automated statement generation.
14. **Insight** — Write contrarian hypothesis, why now, why you
15. **Execution Planning** — Transform strategy into a concrete action plan, schedule, and resource allocation
16. **Ask** — Finalize fundraising round terms, use of proceeds, milestones, and investor next steps
17. **Writing Text & Slide** — Draft a highly structured, conversational 10-minute pitch text intended for Google TTS, and convert it into Google Slides `slideData.json` and generate presentation via GAS script

> **Critical:** Phases MUST run sequentially. Do not skip or reorder without stakeholder approval.

## How to Use This Skill

### Step 1: Determine Scope

Ask the user which phases to include. Options:
- **Full plan** — Run all 17 phases
- **Selective phases** — Run specific phases (e.g., "just problem + solution + market")
- **Single phase** — Deep-dive into one phase (e.g., "financials only")

### Step 2: Set Up Output

Create the output directory structure:

```
{output_folder}/businessplan-writing/
├── research/
├── problem/
├── solution/
├── technology/
├── business-model/
├── traction-progress/
├── market/
├── competition/
├── go-to-market/
├── operations/
├── team/
├── purpose/
├── financials/
├── insight/
├── execution/
├── ask/
├── writing-text/
├── writing-slide/
└── progress-tracker.md
```

### Step 3: Execute Phases Sequentially (STRICT REQUIREMENT)

**Mandatory Progress Tracker**: Before beginning the first phase, you MUST create a master checklist file: `{output_folder}/businessplan-writing/progress-tracker.md`. You must list every phase and sub-task defined in the reference files, and check them off only when they are 100% complete.

For each phase:
1. **Load Reference**: Read the corresponding phase reference file (see below).
2. **Execute Every Sub-task**: Review the sub-task index in the reference file. You are strictly required to execute EVERY sub-task. Before drafting any file, ensure the prior steps in the phase are complete. Do not ask the user if you should skip unless there is a specific technical reason.
3. **Draft & Save**: For each sub-task: research → draft → produce deliverable → validate. Save the output to the designated path.
4. **Iterative Batch Processing:** If a sub-task requires multiple outputs, generate them all in a single turn if possible, do not stop until the set is complete.
5. **Update Tracker**: Update your `progress-tracker.md` to check off the completed sub-task before moving to the next one.
6. **Prioritize Research:** For research-heavy phases (Problem, Market, Competition, GTM, Technology), **always start with the designated research/web-search sub-task** to ground the plan in real-world data and competitor intelligence.
7. Review the task index with the user and confirm which sub-tasks to execute.
8. Record status, key outputs, blockers, and owners in a progress log.
9. Summarize phase outputs before moving to the next phase.

### Step 4: Validate and Consolidate

After all phases complete, consolidate into:
- Overall readiness assessment
- Unresolved risks and mitigations
- Follow-up actions with owners and deadlines

## Phase Reference Files

Load the relevant reference file **only when working on that phase**:

| Phase | Reference File |
|---|---|
| 1. Research | [references/research-phase.md](references/research-phase.md) |
| 2. Problem & Opportunity Definition | [references/problem-opportunity-phase.md](references/problem-opportunity-phase.md) |
| 3. Solution | [references/solution-phase.md](references/solution-phase.md) |
| 4. Technology | [references/technology-phase.md](references/technology-phase.md) |
| 5. Business Model | [references/business-model-phase.md](references/business-model-phase.md) |
| 6. Traction & Progress | [references/traction-and-progress-phase.md](references/traction-and-progress-phase.md) |
| 7. Market | [references/market-phase.md](references/market-phase.md) |
| 8. Competition | [references/competition-phase.md](references/competition-phase.md) |
| 9. Go-To-Market (GTM) | [references/go-to-market-phase.md](references/go-to-market-phase.md) |
| 10. Operations | [references/operations-phase.md](references/operations-phase.md) |
| 11. Team | [references/team-phase.md](references/team-phase.md) |
| 12. Purpose | [references/purpose-phase.md](references/purpose-phase.md) |
| 13. Financials | [references/financials-phase.md](references/financials-phase.md) |
| 14. Insight | [references/insight-phase.md](references/insight-phase.md) |
| 15. Execution Planning | [references/execution-planning-phase.md](references/execution-planning-phase.md) |
| 16. Ask | [references/ask-phase.md](references/ask-phase.md) |
| 17. Writing Text & Slide | [references/writing-slide-phase.md](references/writing-slide-phase.md) |

## Financials Data Management

The financials phase uses a set of JSON files (assumptions, operating_expenses, personnel, sales_orders, valuation_data, fundraising_plan) for data storage and output. 

For the calculation logic, refer to the bundled Excel template:
`assets/businessplan_financials_template_ja_en_irino.xlsx`

This template remains the definitive source for formulas, matrix algebra for revenue spreading, and financial statement structures. Consult it to ensure JSON-based calculations are accurate and consistent with industry standards.

## Output Conventions

All deliverables follow these conventions:
- **Bilingual labels** (JP/EN) for key terms
- **Quantitative metrics** wherever possible (cite data sources)
- **Source citations** for every claim or data point
- **Standard footer** on each deliverable: Decisions, Risks/blockers + owners, Research backlog

### Deliverable Template

```markdown
# [Deliverable Title]

**Prepared For:** [User Name]
**Date:** [Date]

---

## [Section 1]
*Evidence-based content with bilingual labels, quantitative metrics, and clear ownership.*
- Key point (JP/EN): … [Source]

---

## Final Summary & Next Steps
- Decisions:
- Risks / blockers + owners:
- Research backlog:
```

## Validation Checklist

After each sub-task, verify:
- [ ] Research log documents ≥3 primary + ≥2 secondary sources with dates/owners
- [ ] Deliverable uses bilingual labels and quantified metrics
- [ ] Every claim or data row cites a source
- [ ] Decision makers, champions, blockers, and dependencies identified
- [ ] Final summary lists decisions, risks/blockers with owners, and research backlog
- [ ] Output saved to the correct path

After each phase, verify:
- [ ] All selected sub-task workflows completed
- [ ] Deliverables stored in output folder
- [ ] Risks/blockers documented in summary
- [ ] Phase status communicated to stakeholders
