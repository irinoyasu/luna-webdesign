# Execution Planning Phase Reference

## Purpose

Create a concrete, actionable roadmap for the next 12-24 months. This phase translates the broad strategy into specific workstreams, owners, and timelines. It bridges the gap between strategy (Phases 1-14) and writing (Phase 16) — ensuring the business plan includes a credible, actionable execution schedule that demonstrates operational readiness and investor confidence.

## Inputs

**Process Dependencies:**
- **Phase 1-14 (Mandatory):** Execution is the culmination of all preceding strategy phases.
- **Phase 4: Technology (Mandatory):** Dev roadmap dictates the technical milestones.
- **Phase 11: Team (Mandatory):** Resource availability and hiring speed.
- **Phase 13: Financials (Mandatory):** Funding dates and cash runway constraints.

**You MUST synthesize information from ALL previously completed phases before drafting.** 
The business plan is a cumulative pipeline. Your inputs include:
1. **Previous Phase Outputs:** All documents and research logs generated in Phases 1-14.
2. **Existing Workspace Data:** Always check the output directory (`{output_folder}/businessplan-writing/`) for any existing `execution/` folder or data from preceding phases. If files already exist from a previous execution, you must incorporate their content to ensure continuity and avoid duplication.
3. **Primary Direct Dependencies:** Phase 4: Technology (development roadmap), Phase 9: GTM (sales/marketing tactics), and Phase 10: Operations (recruitment timelines).

---

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Extract Deliverables & Dependencies | `execution/deliverables-map.md` | List every deliverable from Solution (Phase 3) and Operations (Phase 9), identify dependencies and owner assignments |
| 2 | Build Day-by-Day Schedule | `execution/daily-schedule.md` | Map each deliverable and sub-task to specific calendar days with start/end dates |
| 3 | Assign Owners & Resources | `execution/resource-plan.md` | Assign team members/roles to each task, identify resource constraints and conflicts |
| 4 | Define Milestones & Checkpoints | `execution/milestones.md` | Set key milestones, review checkpoints, and go/no-go gates |
| 5 | Risk & Contingency Plan | `execution/risk-contingency.md` | Identify execution risks, define contingency actions and buffer days |

---

## Detailed Sub-Task Instructions

### 1. Extract Deliverables & Dependencies

**Dependencies:**
- **Phase 3: Solution:** Extract every feature and capability into a deliverable item.
- **Phase 10: Operations:** Extract every functional process (HR, Finance, Legal) into setup deliverables.
- **Phase 4: Technology:** Align development milestones with technical feasibility.
- **Phase 6: Traction & Progress:** Use the roadmap to define the target release timing of product.

**Inputs:**
- Solution (Phase 3)
- Operations (Phase 9)
- Technology Roadmap (Phase 10)

**Process:**
1. List **every discrete deliverable** required to launch and scale the business (e.g., "MVP v1.0," "Beta Test Group," "First 100 Customer Acquisition").
2. For each deliverable, identify:
   - **External dependencies** (e.g., regulatory approvals, supplier contracts).
   - **Internal dependencies** (e.g., tech stack setup, hiring key personnel).
   - **Inter-deliverable dependencies** (e.g., "Product launch requires hiring sales lead").
3. Classify each deliverable as:
   - **Critical Path** — Delay here delays the entire launch.
   - **Parallel** — Can proceed independently alongside other work.
   - **Nice-to-Have** — Can be deferred without blocking the core launch.

### 2. Build Day-by-Day Schedule

**Inputs:**
- Deliverables Map (Sub-task 1)
**Dependencies:**
- **Phase 6: Traction:** Use the growth roadmap as the baseline for sequencing deliverables.
- **Phase 9: GTM:** Sales and Marketing launch events must be mapped to specific calendar days.

**Process:**
1. Set **Day 0** = the start of the execution phase or funding date.
2. Work forward from Day 0, placing each task on specific calendar days.
3. Apply the following scheduling rules:
   - **Regulatory/External dependencies** must have buffer days (assume response lags).
   - **Hiring/Onboarding** needs realistic lead times (e.g., 30-60 days).
   - **Technical work** estimated with 20% buffer.
4. Create both a **summary view** (month-by-month for the first year) and a **detail view** (day-by-day for the first quarter).

### 3. Assign Owners & Resources

**Inputs:**
- Day-by-Day Schedule (Sub-task 2)
**Dependencies:**
- **Phase 11: Team:** Use the organization chart and member profiles to assign owners.
- **Phase 13: Financials:** Budget constraints drive the ability to hire or outsource specific tasks.

**Process:**
1. For each task in the schedule, assign a **primary owner** and an **approver**.
2. Identify tasks where **partners/suppliers** are the owners.
3. Flag any **resource conflicts** (e.g., the same person assigned to overlapping critical tasks).
4. Document **escalation paths** for blocked tasks.

### 4. Define Milestones & Checkpoints

**Inputs:**
- Day-by-Day Schedule (Sub-task 2)
**Dependencies:**
- **Phase 13: Financials:** Milestones must align with funding rounds and value inflection points.
- **Phase 16: Ask:** Use the milestones to justify use of proceeds.

**Process:**
1. Set **3-5 key milestones** that correspond to major value inflection points (e.g., Product Launch, First Revenue, Series A readiness) based on the release timing of product.
2. For each milestone, define:
   - **Completion criteria** (what "done" looks like).
   - **Verification method** (how we confirm it's done).
   - **Go/No-Go decision** (impact on subsequent phases).
3. Schedule **regular status check-ins** for the internal team.

### 5. Risk & Contingency Plan

**Dependencies:**
- **Sub-task 1 (Deliverables Map):** Identify execution risks related to the critical path items.
- **Phase 14: Insight:** Use the contrarian hypothesis and identified timing risks as a basis for high-level strategic risk.

**Process:**
1. Identify **top 5 execution risks** (e.g., technical delay, hiring failure, market shift).
2. For each risk:
   - **Probability** (High / Medium / Low).
   - **Impact** (Critical / Major / Minor).
   - **Mitigation** (proactive action to reduce probability).
   - **Contingency** (reactive action if the risk materializes).
   - **Buffer days** allocated in the schedule.
3. Define the **overall project buffer** (recommended: 15-20% of total duration).

---

## Phase Validation Checklist

- [ ] Every major deliverable from the solution and operations phases is accounted for.
- [ ] All critical dependencies have explicit due dates and owners.
- [ ] Critical path is clearly identified and has buffer time.
- [ ] Resource conflicts are resolved or flagged based on the Team phase data.
- [ ] Milestones have clear completion criteria aligned with Financials.
- [ ] Risk register covers at least 5 execution risks.
- [ ] The schedule is realistic for the proposed team size.
- [ ] Output saved to the `execution/` folder.
