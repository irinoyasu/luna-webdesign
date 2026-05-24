# Competition Phase Reference

## Purpose

Analyze the competitive landscape to identify direct and indirect threats. This phase defines the company's "unfair advantage" and competitive positioning to ensure defensibility.

## Inputs

**Process Dependencies:**
- **Phase 1: Research (Mandatory):** Initial competitor lists and technical intelligence from the research log.
- **Phase 7: Market (Mandatory):** The Five Forces analysis and market structure must be understood.
- **Phase 2: Problem & Opportunity (Mandatory):** Underserved needs and Pains/Gains from the Canvas are the criteria for comparison.

**You MUST synthesize information from ALL previously completed phases before drafting.** 
The business plan is a cumulative pipeline. Your inputs include:
1. **Previous Phase Outputs:** All documents and research logs generated in Phases 1-7.
2. **Existing Workspace Data:** Always check the output directory (`{output_folder}/businessplan-writing/`) for any existing `competition/` folder or data from preceding phases. If files already exist from a previous execution, you must incorporate their content to ensure continuity and avoid duplication.
3. **Primary Direct Dependencies:** Phase 1: Research (competitor intelligence), Phase 3: Solution (value proposition and win themes), and Phase 7: Market (market structure and 5 Forces analysis).

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Research Competitors | `competition/research-log.md` | Web search for direct/indirect competitors, substitutes, and industry positioning |
| 2 | Write Direct Competitors | `competition/direct-competitors.md` | Analyze direct competitors |
| 3 | Write Indirect Competitors | `competition/indirect-competitors.md` | Analyze indirect competitors |
| 4 | Write Substitutes | `competition/substitutes.md` | Analyze substitutes |
| 5 | Write Comparison Criteria | `competition/comparison-criteria.md` | Define comparison criteria and differentiating outcomes |
| 6 | Write Competitive Advantage | `competition/competitive-advantage.md` | Define defensible outcomes and strategic moats |
| 7 | Write Competitive Positioning Statement | `competition/positioning-statement.md` | Draft a Geoffrey Moore-style positioning statement |

---

## Detailed Sub-Task Instructions

### 1. Research Competitors

**Dependencies:**
- **Phase 1: Research:** Use the initial competitor lists and technical intelligence identified in research logs.
- **Phase 7: Market:** Use the market structure and Five Forces analysis to categorize competitors (Direct vs. Indirect).
- **Phase 2: Problem & Opportunity:** Identify the pain points being addressed to find companies solving the same problem.

Use web search tools to gather comprehensive data on the competitive landscape.

**Research objectives:**
- Identify at least 3–5 direct competitors.
- Identify major indirect competitors and substitute solutions.
- Gather data on market share, pricing models, and key feature sets.
- Find recent news, funding rounds, or strategic shifts in the industry.
- Locate customer reviews or third-party comparisons (G2, Capterra, etc.).

**Deliverable:**
- `competition/research-log.md` containing search queries, URLs visited, and key notes per source.

### 2. Write Direct Competitors

**Dependencies:**
- **Phase 1: Research:** Use the detailed competitor profiles and technological intelligence.
- **Phase 3: Solution:** compare with the proposed solution's core features.

**Use web search tools** to gather real-time data. For each competitor document:
- Company overview (founding, HQ, size, funding)
- Product/service offering (features, pricing, deployment model)
- Pricing strategy with comparison table
- Target market and customer segments
- Estimated market share / positioning
- Strengths and weaknesses (SWOT elements)
- Key differentiators
- Recent news, product launches, partnerships

**Use frameworks:** Porter's "Rivalry Among Existing Competitors" + SWOT

**Evaluation questions:**
- Are these *truly* direct competitors (same problem, same customer)?
- Is pricing information accurate or a reasonable estimate?
- Why do customers choose them over alternatives?

### 3. Write Indirect Competitors

**Dependencies:**
- **Phase 2: Problem & Opportunity:** Identify alternative approaches customers use to solve the same pain.
- Different technology or approach
- Different business model
- Different customer segment but adjacent
- For each: how they approach the problem, strengths, when customers prefer them

### 4. Write Substitutes

**Dependencies:**
- **Phase 2: Problem & Opportunity:** Identify non-consumption or manual workarounds (Excel, paper) described in customer interviews.
- Manual processes / spreadsheets / "do nothing"
- Internal custom-built tools
- General-purpose tools adapted for the use case
- For each: cost, effort, limitations, switching friction

### 5. Write Comparison Criteria

**Dependencies:**
- **Phase 2: Problem & Opportunity:** Use the underserved needs and "Importance vs. Satisfaction" data to weight criteria.
- **Phase 3: Solution:** Use core capabilities as benchmark features.
- **Outcome Comparison:** Define criteria based on the "underserved needs" identified in Phase 2 (e.g., "Time to Value," "Integration Complexity," "Total Cost of Ownership").
- **Feature Matrix:** Include a traditional feature comparison for baseline expectations.
- **Performance Benchmarks:** Document quantitative metrics where your solution outperforms alternatives.
- **Technology & Maturity:** Evaluate the underlying tech stack and readiness level.
- **Weighting:** Assign a weight (1-5) to each criterion based on its importance to the target persona.
- **Deliverable:** Weighted comparison matrix in `competition/comparison-criteria.md`.

**Dependencies:**
- **Phase 4: Technology:** Identify technical moats like proprietary code or internal architecture.
- **Sub-task 1 (Competitor Research):** Advantage must be defined *relative* to specific competitor gaps (SWOT).
- **Phase 11: Team:** Identify unfair advantages related to the team's unique domain experience.

Articulate your sustainable competitive advantage, focusing on **Defensibility** and **Outcome Framing**.
- **Identify Moats:** Define what makes your advantage durable (e.g., IP/Patents, Proprietary Data, Network Effects, High Switching Costs, Ecosystem Lock-in).
- **Outcome Advantage:** Describe the specific outcome you deliver that competitors cannot easily copy (e.g., "Unlike X, we reduce processing time by 80% through [Moat]").
- **Assess Copy-ability:** Be honest—could a competitor replicate this in 6 months? If yes, look for a deeper differentiator.
- **Team/Expertise Moat:** Document "Unfair Advantages" related to the founding team's unique domain expertise or relationships.
- **Deliverable:** Defensibility analysis and strategic advantage summary in `competition/competitive-advantage.md`.

### 7. Write Competitive Positioning Statement

**Dependencies:**
- **Phase 3: Solution:** Use the product name and core differentiating features identified in the capabilities document.
- **Phase 2: Problem & Opportunity:** Use the specific persona and their primary unmet need/JTBD.
- **Phase 6: Traction & Progress:** Positioning must be time-bound to the release timing of product.

Synthesize the competitive landscape into a crisp, strategic summary using the **Geoffrey Moore Framework**.

**Value Proposition:**
- **For:** [Specific target customer/persona identified in Phase 2]
- **that need:** [Underserved need—focus on pains/JTBD]
- **[Product Name]:** Your solution's name
- **is a:** [Product Category—how buyers mentally file you]
- **that:** [Benefit statement—focus on the primary outcome]

**Differentiation Statement:**
- **Unlike:** [Primary competitor or real competitive alternative like "Excel"]
- **[Product Name]:** Your solution's name
- **provides:** [Unique differentiation—the defensible outcome identified in Sub-Task 6]

**Deliverable:**
- `competition/positioning-statement.md` containing the formal strategic positioning.

---

## Phase Validation Checklist

- [ ] Competitive landscape research documented in `competition/research-log.md`
- [ ] 3–5 direct competitors profiled with evidence
- [ ] Indirect competitors and substitutes identified
- [ ] Comparison criteria defined and weighted
- [ ] Competitive advantage articulated with defensibility analysis (IP, data moats, etc.).
- [ ] **Competitive Positioning Statement drafted using the Geoffrey Moore framework (For/That/Unlike).**
- [ ] All competitor data sourced from web research with citations.
