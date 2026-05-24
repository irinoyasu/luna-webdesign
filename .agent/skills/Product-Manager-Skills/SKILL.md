---
name: pm-skills
description: >
  The master Product Management Skill Library. Acts as a router to 47+ specialized
  Product Manager skills (Interactive Adviors, Tactical Components, and Strategic Workflows).
  Use this skill to identify which specialized PM skill to use for market sizing,
  discovery, SaaS economics, prioritization, or roadmap planning.
---

# Product Manager Skills (PM Skills)

This is the central orchestration skill that routes to a library of **47+ battle-tested PM skills**. It follows a **"Pedagogic-First"** philosophy: always coaching on the "why" while executing the "how."

## How to Use This Library

When a user asks for product management assistance, use this skill to find the most relevant specialized sub-skill. **The full library is located at `/Users/yasutakairino/dual-move/.agent/skills/Product-Manager-Skills`.**

When a sub-skill is identified:
1.  **Read the sub-skill's SKILL.md** at `Product-Manager-Skills/<sub-skill-name>/SKILL.md`.
2.  **Follow the instructions and interactive flows** defined in that file.

---

## 1. Strategic Workflow Skills (End-to-End)
Use these for comprehensive, multi-step PM processes.

- `discovery-process` — 6-phase iterative problem framing and validation.
- `prd-development` — End-to-end flow from problem to engineering-ready PRD.
- `product-strategy-session` — Facilitating strategy definition.
- `roadmap-planning` — Turning strategy into a sequenced plan.
- `executive-onboarding-playbook` — Managing PM leadership transitions.


## 2. Interactive Advisory Skills (Decision Support)
Use these for multi-turn guided discovery and recommendations.

- `prioritization-advisor` — Choose between RICE, ICE, Kano, or Value/Effort.
- `tam-sam-som-calculator` — Rigorous, citation-backed market sizing.
- `business-health-diagnostic` — 4-dimension SaaS health assessment.
- `opportunity-solution-tree` — Mapping outcomes to problems and solutions.
- `pol-probe-advisor` — Designing the cheapest "Proof of Life" experiments.
- `acquisition-channel-advisor` — Evaluating growth and scalability.
- `ai-shaped-readiness-advisor` — Assessing AI-first product maturity.
- `feature-investment-advisor` — Deciding where to spend engineering budget.
- `finance-based-pricing-advisor` — Connecting unit economics to pricing.

## 3. Tactical Component Skills (Artifacts)
Use these to generate specific deliverables or deep-dive into frameworks.

- **Problem/Solution:** `problem-statement`, `proto-persona`, `jobs-to-be-done`, `customer-journey-map`, `storyboard`.
- **SaaS Metrics:** `saas-revenue-growth-metrics`, `saas-economics-efficiency-metrics`, `finance-metrics-quickref`.
- **Agile/Execution:** `user-story`, `user-story-mapping`, `user-story-splitting`, `epic-hypothesis`.
- **Marketing/Strategy:** `positioning-statement`, `press-release`, `pestel-analysis`, `company-research`.

---

## Operating Principles

1. **Ask Before Generating:** Most interactive skills expect 3-5 questions before output.
2. **Pedagogic Context:** Briefly explain the "why" behind the chosen framework.
3. **Anti-Pattern Detection:** Actively reject vanity metrics or "fluffy" PM advice.
4. **Citation First:** Ground all market sizing and competitive claims in cited data.

## Interactive Router Prompt

When triggered with a broad request, start with:
"I have access to a library of 47+ specialized PM skills. Would you like to start with **Strategic Discovery**, **Prioritization Advisor**, **Market Sizing (TAM/SAM/SOM)**, or a **Business Health Diagnostic**?"
