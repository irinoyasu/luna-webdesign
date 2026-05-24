# Phase 5: Execution Planning

## Purpose

Transform the solution design and pricing into a **concrete, day-by-day action plan** that assigns every deliverable, dependency, and milestone to specific dates and owners. This phase bridges the gap between strategy (Phases 1-4) and writing (Phase 6) — ensuring the proposal includes a credible, actionable execution schedule that demonstrates operational readiness.

> **When to run:** After Costing & Pricing (Phase 4) is complete and before the Writing phase (Phase 6). The execution plan becomes a key input to the proposal document itself.

---

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 5.1 | Extract Deliverables & Dependencies | `execution/deliverables-map.md` | List every deliverable from Solution Design (Phase 3), identify dependencies, prerequisites, and owner assignments |
| 5.2 | Build Day-by-Day Schedule | `execution/daily-schedule.md` | Map each deliverable and sub-task to specific calendar days with start/end dates |
| 5.3 | Assign Owners & Resources | `execution/resource-plan.md` | Assign team members/roles to each task, identify resource constraints and conflicts |
| 5.4 | Define Milestones & Checkpoints | `execution/milestones.md` | Set key milestones, review checkpoints, and go/no-go gates |
| 5.5 | Risk & Contingency Plan | `execution/risk-contingency.md` | Identify execution risks, define contingency actions and buffer days |

---

## Sub-Task 5.1: Extract Deliverables & Dependencies

### Inputs
- Solution Design document (`solution/solution-design.md`)
- Timeline from the proposal
- Customer dependencies identified during Research (Phase 1)

### Process
1. List **every discrete deliverable** promised in the proposal (e.g., "EPC-Ready Hub," "60-Second Teardown Video," "ROI Calculator Web App")
2. For each deliverable, identify:
   - **Prerequisites from the customer** (e.g., CAD files, sample Choke Valve)
   - **Prerequisites from your team** (e.g., dev environment setup, Avatar API)
   - **Inter-deliverable dependencies** (e.g., "Chicago Lab requires physical valve → Valve must arrive before Day 15")
3. Classify each deliverable as:
   - **Critical Path** — Delay here delays the entire project
   - **Parallel** — Can proceed independently alongside other work
   - **Nice-to-Have** — Can be deferred without blocking launch

### Output Format (`execution/deliverables-map.md`)

```markdown
# Deliverables Map

## Critical Path Items
| # | Deliverable | Prerequisites (Customer) | Prerequisites (Internal) | Depends On | Est. Duration |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | X days |

## Parallel Items
| # | Deliverable | Prerequisites (Customer) | Prerequisites (Internal) | Est. Duration |
|---|---|---|---|---|
| 1 | ... | ... | ... | X days |

## Nice-to-Have / Deferred
| # | Deliverable | Notes |
|---|---|---|
| 1 | ... | ... |
```

---

## Sub-Task 5.2: Build Day-by-Day Schedule

### Inputs
- Deliverables Map (5.1)
- Proposed project timeline from Solution Design
- Customer availability and constraints

### Process
1. Set **Day 0** = the date of the kick-off meeting or contract signing
2. Work forward from Day 0, placing each task on specific calendar days
3. Apply the following scheduling rules:
   - **Customer-dependent tasks** must have buffer days (assume 2-3 day response lag)
   - **Review/approval gates** need at least 1 business day
   - **Creative work** (video, design) estimated at 1.5× the "optimistic" duration
   - **Technical work** (web dev, integration) estimated with 20% buffer
4. Create both a **summary view** (week-by-week) and a **detail view** (day-by-day)

### Output Format (`execution/daily-schedule.md`)

```markdown
# Day-by-Day Execution Schedule

## Project Parameters
- **Day 0 (Kick-off):** [DATE]
- **Target Launch:** Day [N] ([DATE])
- **Total Working Days:** [N]
- **Buffer Days Built In:** [N]

## Week-by-Week Summary
| Week | Key Activities | Milestone | Owner |
|---|---|---|---|
| Week 1 (Day 1-5) | ... | ... | ... |
| Week 2 (Day 6-10) | ... | ... | ... |
| ... | ... | ... | ... |

## Day-by-Day Detail

### Week 1: Foundation & Data Transfer
| Day | Date | Task | Owner | Deliverable | Status |
|---|---|---|---|---|---|
| 1 | [DATE] | Kick-off MTG: CAD data review, video storyboard | Both | Meeting notes | ☐ |
| 2 | [DATE] | ... | ... | ... | ☐ |
| ... | ... | ... | ... | ... | ☐ |

### Week 2: Build Phase
| Day | Date | Task | Owner | Deliverable | Status |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ☐ |
```

---

## Sub-Task 5.3: Assign Owners & Resources

### Inputs
- Day-by-Day Schedule (5.2)
- Team roster (from Solution Design phase)
- Customer-side contacts

### Process
1. For each task in the schedule, assign a **primary owner** and an **approver**
2. Identify tasks where the **customer** is the owner (e.g., provide CAD files, approve video script)
3. Flag any **resource conflicts** (e.g., the same person assigned to overlapping tasks)
4. Document **escalation paths** for blocked tasks

### Output Format (`execution/resource-plan.md`)

```markdown
# Resource Plan

## Team Roster
| Role | Name | Availability | Notes |
|---|---|---|---|
| Project Lead | ... | Full-time | Primary point of contact |
| ... | ... | ... | ... |

## Customer-Side Contacts
| Role | Name | Responsibility | Response SLA |
|---|---|---|---|
| ... | ... | ... | ... |

## Resource Allocation by Week
| Week | [Person 1] | [Person 2] | [Customer Contact] |
|---|---|---|---|
| Week 1 | Task A, Task B | Task C | Provide CAD files |
| ... | ... | ... | ... |

## Escalation Path
1. Task blocked → Notify project lead within 24h
2. Customer dependency delayed → Escalate to [name] via [channel]
3. Critical path at risk → Emergency sync meeting within 48h
```

---

## Sub-Task 5.4: Define Milestones & Checkpoints

### Inputs
- Day-by-Day Schedule (5.2)
- Contract terms or proposal commitments

### Process
1. Set **3-5 key milestones** that correspond to major handoffs or completions
2. For each milestone, define:
   - **Completion criteria** (what "done" looks like)
   - **Verification method** (how we confirm it's done)
   - **Go/No-Go decision** (what happens if the milestone is missed)
3. Schedule **weekly status check-ins** with the customer

### Output Format (`execution/milestones.md`)

```markdown
# Milestones & Checkpoints

## Key Milestones
| # | Milestone | Target Day | Completion Criteria | Go/No-Go |
|---|---|---|---|---|
| M1 | Data Transfer Complete | Day 5 | All CAD files and compliance docs received | Proceed / Reschedule build |
| M2 | ... | Day X | ... | ... |

## Weekly Checkpoints
| Week | Checkpoint Focus | Attendees | Format |
|---|---|---|---|
| Week 1 | Kick-off + data transfer status | Both teams | 30-min video call |
| ... | ... | ... | ... |
```

---

## Sub-Task 5.5: Risk & Contingency Plan

### Inputs
- Deliverables Map (5.1)
- Day-by-Day Schedule (5.2)
- Pain points from Research (Phase 1)

### Process
1. Identify **top 5 execution risks** (e.g., customer delays in providing data, technical complexity underestimated, key resource unavailable)
2. For each risk:
   - **Probability** (High / Medium / Low)
   - **Impact** (Critical / Major / Minor)
   - **Mitigation** (proactive action to reduce probability)
   - **Contingency** (reactive action if the risk materializes)
   - **Buffer days** allocated in the schedule
3. Define the **overall project buffer** (recommended: 15-20% of total duration)

### Output Format (`execution/risk-contingency.md`)

```markdown
# Execution Risk & Contingency Plan

## Risk Register
| # | Risk | Probability | Impact | Mitigation | Contingency | Buffer |
|---|---|---|---|---|---|---|
| 1 | Customer delays CAD file delivery | Medium | Critical | Send reminder on Day 2; provide file format checklist | Use placeholder geometry; reschedule video shoot | +3 days |
| 2 | ... | ... | ... | ... | ... | ... |

## Overall Project Buffer
- **Total scheduled days:** [N]
- **Buffer days:** [N] (X% of total)
- **Hard deadline:** Day [N] ([DATE])
```

---

## Validation Checklist

After completing this phase:

- [ ] Every deliverable from the proposal is accounted for in the schedule
- [ ] All customer dependencies have explicit due dates and owners
- [ ] Critical path is clearly identified and has buffer time
- [ ] Resource conflicts are resolved or flagged
- [ ] Milestones have clear completion criteria
- [ ] Risk register covers at least 5 execution risks
- [ ] The schedule is realistic (no single person assigned 2 full-time tasks on the same day)
- [ ] Customer-facing version of the schedule is ready for sharing at the kick-off meeting

---

## Status & Next Steps
- **Decisions made:**
- **Risks / blockers + owners:**
- **Open items / research backlog:**
