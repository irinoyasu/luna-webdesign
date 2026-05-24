# Technology Phase Reference

## Purpose

Define the technological foundation of the solution, including architecture, tech stack, and intellectual property. This phase translates product features into technical requirements and defines the roadmap for development and innovation.

## Inputs

**Process Dependencies:**
- **Phase 3: Solution (Mandatory):** Core capabilities, feature lists, and prioritized feature ROI must be finalized before designing the technical architecture.

**You MUST synthesize information from ALL previously completed phases before drafting.** 
The business plan is a cumulative pipeline. Your inputs include:
1. **Previous Phase Outputs:** All documents and research logs generated in Phases 1-3.
2. **Existing Workspace Data:** Always check the output directory (`{output_folder}/businessplan-writing/`) for any existing `technology/` folder or data from preceding phases. If files already exist from a previous execution, you must incorporate their content to ensure continuity and avoid duplication.
3. **Primary Direct Dependencies:** Phase 2: Problem & Opportunity Definition (customer pains and gaps) and Phase 3: Solution (features and system architecture).

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Define Core Technology | `technology/core-technology.md` | Define the core technology stack, architecture, and framework |
| 2 | Define Underlying Magic | `technology/underlying-magic.md` | Define the unfair advantage and secret sauce for the pitch deck |
| 3 | Write Intellectual Property | `technology/intellectual-property.md` | Intellectual property strategy |
| 4 | Research Technology | `technology/research-log.md` | Web search for technology trends, IP landscapes, and developer tools |
| 5 | Write Development Roadmap | `technology/roadmap.md` | Outcome-driven release plan sequenced by strategic themes (Now/Next/Later) |
| 6 | Write Research Items | `technology/research-items.md` | Research items and priorities |

---

## Detailed Sub-Task Instructions

### 1. Define Core Technology

**Dependencies:**
- **Phase 3: Solution:** System architecture must support the specific features and user stories defined.
- **Phase 5: Business Model:** Align the tech stack and infrastructure choice with cost and gross margin targets.

Clearly define the actual technology stack, system architecture, and technical mechanism of your solution.

**Instructions:**
1. **Architecture Overview:** Provide a high-level explanation of how the system works (e.g., frontend, backend, database, AI models, hardware components).
2. **Technology Stack:** List specific programming languages, frameworks, cloud infrastructure, and third-party APIs used.
3. **Data Flow & Integration:** Explain how data moves through the system and integrates with existing customer workflows or external platforms.
4. **Scalability & Security:** Document the measures taken to ensure the system can handle growth and protect customer data/privacy.

**Deliverables:**
- `technology/core-technology.md` detailing the system architecture, tech stack, data flow, and security.

### 2. Define Underlying Magic

**Dependencies:**
- **Phase 3: Solution:** Translate core features into the "magic" that delivers unique value.
- **Phase 8: Competition:** Use differentiation data to highlight the "magic" that competitors lack.

Translate the raw technological architecture into an investor-ready "Secret Sauce" narrative built for a pitch deck.

**Instructions (based on Y Combinator / Sequoia best practices):**
1. **Emphasize Value Over Features:** For every technical component listed, explicitly state how it solves a customer problem (e.g., "Our proprietary data pipeline" -> "Reduces processing time from 3 days to 4 seconds").
2. **Apply the "Grandma Test":** Simplify complex backend architecture into easily digestible analogies or high-level concepts. Remove all unnecessary jargon. 
3. **Showcase Defensibility (The Moat):** Explicitly state why this technology is an "unfair advantage." Why can't a well-funded competitor easily replicate it? Link this explanation back directly to the Intellectual Property strategy (Sub-Task 3).
4. **Visual Concepting:** Describe a simple diagram, schematic, or flowchart that could visually represent the technology stack in a presentation slide. Less text, more visual impact.

**Deliverables:**
- `technology/underlying-magic.md` containing the simplified tech value proposition, defensibility statement, and visual concept diagram description.

### 3. Write Intellectual Property

**Dependencies:**
- **Phase 1: Research:** Check for existing patents or prior art identified in the initial research.
- **Phase 8: Competition:** Analyze competitor IP strategies.

Define IP strategy:

**Current IP:**
- Patents (filed, granted, pending)
- Trademarks and brand assets
- Copyrights (code, content, designs)
- Trade secrets and proprietary algorithms
- Domain names and digital assets

**IP Protection Plan:**
- Filing strategy (when, where, what to protect)
- Defensive vs. offensive IP strategy
- Freedom-to-operate analysis
- IP budget and timeline
- Legal counsel and patent agents

**IP Competitive Landscape:**
- Competitor patents and potential conflicts
- Licensing opportunities
- Open-source dependencies and compliance

**Dependencies:**
- **Sub-task 1 (Core Technology):** Research must validate the feasibility and benchmarks of the chosen stack.
- **Sub-task 3 (Intellectual Property):** Identify technical whitepapers and patents to support the IP strategy.

Use web search tools to gather technological intelligence and IP data.

**Research objectives:**
- Identify emerging technologies, frameworks, and tools relevant to the solution.
- Search for competitor patents, open-source projects, and technical Whitepapers.
- Research industry standards, security protocols, and compliance requirements.
- Find potential Technology partners, vendors, or acquisition targets.
- Locate developmental benchmarks and typical Technology stacks for similar products.

**Deliverable:**
- `technology/research-log.md` containing search queries, URLs visited, and key notes per source.

### 5. Write Development Roadmap

**Dependencies:**
- **Phase 3: Solution:** Roadmap sequencing (Now/Next/Later) must be driven by the feature ROI analysis.
- **Phase 13: Financials:** Roadmap must align with available funding and R&D budget milestones.
- **Phase 6: Traction & Progress:** Roadmap must be anchored in the target release timing of product.

Create an outcome-driven release plan that translates strategy into execution, avoiding a simple feature list. Use the `roadmap-planning` methodology.

- **Define Strategic Themes:** Organize the roadmap into 3-5 high-level themes (e.g., "Onboarding Friction," "Enterprise Readiness," "Data Reliability").
- **Sequence by Horizon (Now/Next/Later):**
    - **Now (Current Quarter):** High-confidence initiatives with committed resources and defined epics.
    - **Next (Following 3-6 Months):** Planned initiatives with clear hypotheses but flexible scope.
    - **Later (6+ Months):** Future exploration areas and strategic bets based on anticipated market shifts.
- **Define Epic Hypotheses:** For each major initiative, include a brief hypothesis: "We believe [Building X] will achieve [Outcome Y] because [Assumption Z]."
- **Effort Estimation:** Provide T-shirt sizes (S, M, L, XL) for each initiative based on engineering complexity and resource needs.
- **Map to Business Outcomes:** Explicitly link each initiative to a business goal or OKR (e.g., "Retention," "Acquisition," "Scale").
- **Identify Dependencies:** Document critical technical or resource-based blockers (e.g., "Mobile App depends on API Redesign").

**Deliverable:**
- `technology/roadmap.md` containing the themed, sequenced roadmap with hypotheses and business outcome mapping.

**Dependencies:**
- **Sub-task 4 (Technology Research):** Use research findings to prioritize items for the R&D backlog.
- **Sub-task 5 (Roadmap):** Align research priorities with the "Later" horizon strategic bets.

Prioritize Technology research:
- Technology exploration (emerging tech, frameworks, tools)
- Customer-driven research (feature requests, usability studies)
- Market-driven research (new market opportunities, adjacent solutions)
- Academic/scientific collaboration opportunities
- Proof-of-concept projects

**For each item:** Priority, estimated effort, expected impact, owner, deadline

---

## Phase Validation Checklist

- [ ] The "Core Technology" architecture and stack are defined
- [ ] The "Underlying Magic / Secret Sauce" narrative is defined, simplified, and tied to defensibility
- [ ] IP strategy addresses protection, licensing, and compliance
- [ ] Technology and IP research documented in `technology/research-log.md`
- [ ] **Development roadmap uses outcome-driven Now/Next/Later framework with strategic themes.**
- [ ] **Major roadmap initiatives include hypotheses and are mapped to business outcomes.**
- [ ] Milestones are specific, measurable, and time-bound.
- [ ] Research items prioritized with owners and timelines
