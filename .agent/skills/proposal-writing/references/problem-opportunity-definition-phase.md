# Problem & Opportunity Definition Phase Reference

## Purpose

Extract insights from the Research phase to accurately and deeply define the customer's problem and the resulting opportunity before designing a solution. Defining the problem and opportunity correctly is the most critical step in the entire proposal effort.

## Core Philosophy: The "55 Minutes" Rule
(Albert Einstein: *"If I had an hour to solve a problem I would spend 55 minutes thinking about the problem and 5 minutes thinking about the solution."*)
If you define the problem incorrectly, even a perfect solution will fail because it solves the wrong thing.

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 0 | Proposer-Led Problem Framing & Bias Audit (Look Inward) | `problem/bias-audit.md` | Examine proposer team assumptions, biases (confirmation, internal, survivorship), and solution-first thinking before framing the customer's problem |
| 1 | Problem & Opportunity Definition & Priority Mapping (Look Outward & Reframe) | `problem/problems_opportunities.md` | Define customer problems and the desired future state opportunities, mapped with evidence and competitive context using an empathetic narrative |
| 2 | Persona & Jobs-To-Be-Done (JTBD) Analysis | `problem/persona-jtbd.md` | Analyze the personas and JTBD for both the direct customer and the customer's customers |
| 3 | Customer Journey Mapping | `problem/customer-journey.md` | Map the end-to-end journey and friction points for the customer and the customer's customers |

---

## Detailed Sub-Task Instructions

### 0. Proposer-Led Problem Framing & Bias Audit (Look Inward)

Before defining the customer's problem, you MUST perform a "Look Inward" audit of the proposer team (you and the user/client you are assisting). This ensures the proposal isn't blinded by internal assumptions or premature solutioning.

**Instructions:**
1. **Examine Assumptions:** What are we *assuming* we know about the customer without direct evidence?
2. **Audit Biases:** Check for:
   - **Confirmation Bias:** Are we only looking for data that supports our preferred solution?
   - **Internal/Team Bias:** Are we building what's easy for *us* rather than what's valuable for *them*?
   - **Survivorship/Majority Bias:** Are we focusing on the "average" user while ignoring marginalized segments or edge cases?
3. **Challenge Solution-First Thinking:** Are we already saying "we need [feature X]" before we've verified the root problem?

**Output (`problem/bias-audit.md`):**
- List of internal assumptions to challenge.
- Identification of potential proposer-side biases.
- "Solution-first" risks to mitigate.

---

### 1. Problem & Opportunity Definition & Priority Mapping (Look Outward & Reframe)

Translate research intelligence into actionable, empathetic problem and opportunity statements. This phase demands executing **three phases** across **two approaches**:

#### The Empathy-Driven Problem Framework
Based on Jobs-to-be-Done and empathy mapping, all customer-facing problems MUST be structured using this narrative:
- **Persona:** Who is experiencing the problem? (Role/Title)
- **Trying to:** What is the desired outcome (JTBD) the persona cares about? (Focus on results, not tasks)
- **But:** What are the specific barriers/roadblocks preventing the outcome?
- **Because:** What is the **Root Cause** of the problem? (Push past symptoms)
- **Which makes them feel:** What is the emotional/human impact? (Frustrated, anxious, stuck, overwhelmed)

---

#### Detailed Phases:

**Phase 2: Look Outward (Broader Exploration)**
- **Who experiences it:** Define specific personas and the context (when/where).
- **Who else has it:** Who in the industry/market shares this pain?
- **Who doesn't have it:** Who has avoided this problem and what is different about them?
- **Who's been left out:** Which marginalized or "non-standard" users have been ignored so far?
- **Who benefits from the status quo:** Who loses if the problem is solved? (Political resistance)

**Phase 3: Reframe (Actionable Synthesis)**
- **Final Problem Statement Formula:** `[Persona] needs a way to [desired outcome] because [root cause], which currently [emotional/practical impact].`
- **Actionable "How Might We" (HMW):** `How might we [action] as we aim to [objective/desired condition]?`

---

#### Execution Approaches:

**Approach A: Customer-Led Problem Definition (Problem ➔ Opportunity)**
Define the problems strictly from the viewpoint of the customer pain points derived from Research data.

**Approach B: Solution-Led Opportunity Definition (Solution ➔ Problem)**
Define opportunities strictly from the viewpoint of your innovative technologies or products, mapping them back to *latent* problems the customer might not yet realize they have.

**Inputs:**
- All outputs from the Research Phase (`customer-research.md`, `competitive-landscape.md`, etc.)
- Proposer solution documents (capabilities, products).
- Proposer Bias Audit (`problem/bias-audit.md`).

**Best Practices for Defining a Problem:**
1. **Separate Problem from Solution:** Focus on the *pain point*, not the missing *feature*.
2. **Focus on the "Who" (Human-Centricity):** Use the narrative: *"As a [role], I am trying to [outcome] but [barrier] because [root cause], which makes me feel [emotion]."*
3. **Distinguish Symptoms from Root Causes:** Use the "5 Whys" method to find systemic failure.
4. **Quantify the Impact / Opportunity Cost:** Include both a **quantitative metric** ($ lost, hours wasted) and a **qualitative narrative**.
5. **ONE Problem per statement:** Do not group distinct issues. If there are two root causes or two solutions, they are TWO different problems.
6. **Investigate Ecosystem assumptions:** Do problems stem from lack of integration into the customer's *default* tools (ERP, CAD, etc.)?

**Summary Checklist:**
- [ ] Is the statement **solution-agnostic** (for the As-Is state)?
- [ ] Is it backed by **data/evidence**?
- [ ] Does it address the **root cause**, not the symptom?
- [ ] Does it capture the **emotional impact/frustration** of the user?
- [ ] Is the **HMW statement** actionable and broad enough to allow multiple solutions?

**Instructions:**

1. **Execute Approach A & B: Define Top Problems & Opportunities:**
   Write these into `problems_opportunities.md` using the empathetic schema.

   **1.1 Approach A: Customer-Led Problem Definition**
   | # | Problem Name | Persona | Trying to (Outcome) | But (Barrier) | Because (Root Cause) | Makes them feel (Emotion) | Opportunity Cost (Metric + Narrative) | HMW Statement | Evidence | Priority |
   |---|---|---|---|---|---|---|---|---|---|---|
   | A1| | | | | | | | | | Crit / High |

   **1.2 Approach B: Solution-Led Opportunity Definition**
   | # | Opportunity Name | Persona | Trying to (Outcome) | But (Barrier) | Because (Root Cause) | Makes them feel (Emotion) | Opportunity Cost (Metric + Narrative) | HMW Statement | Evidence | Priority |
   |---|---|---|---|---|---|---|---|---|---|---|
   | B1| | | | | | | | | | Crit / High |

2. **Align Your Proof Points & Competitor Advantage:**
   | Linked Problem / Opportunity | Your Proof Point | Your Advantage vs Competitors |
   |---|---|---|
   | | | |

3. **Map Competitor Positioning:**
   | Pain Point | How Competitor A Addresses It | How Competitor B Addresses It | Your Advantage |
   |---|---|---|---|
   | | | | |

4. **Identify Intelligence Gaps:**
   | Gap | How to Fill It | Owner | Deadline |
   |---|---|---|---|
   | | | | |

**Outputs:**
- Proposer Bias Audit (`problem/bias-audit.md`)
- Problem & Opportunity definition matrix (`problem/problems_opportunities.md`)
- Proof points and competitor advantages (appended)
- Intelligence gaps with collection actions (appended)

---

### 2. Persona & Jobs-To-Be-Done (JTBD) Analysis

Analyze exactly who experiences the problem and what they are fundamentally trying to achieve. Use insights from the empathetic narrative ("I am", "Trying to") developed in Sub-Task 1.

**Instructions:**
Execute Approach A & B for Persona & JTBD Analysis for both the direct customer and the end-user.

**2.1 Approach A: Customer-Led Persona & JTBD (As-Is State)**
| Persona (Role/Title) | Core Responsibilities | Jobs To Be Done (Functional, Emotional, Social) | Pains (The "But" & "Because") | Gains (Desired Outcomes / "Trying to") |
|---|---|---|---|---|
| | | | | |

**2.2 Approach B: Solution-Led Persona & JTBD (To-Be State)**
| Persona (Role/Title) | New Capabilities Unlocked | Elevated Jobs To Be Done | Eliminated Pains | Unique Gains (Delivered by Solution) |
|---|---|---|---|---|
| | | | | |

**Outputs:**
- Persona and JTBD analysis document (`problem/persona-jtbd.md`)

---

### 3. Customer Journey Mapping

Map the step-by-step experience using the "Emotional State" derived from the narrative's "Which makes me feel" section. Identify exactly where friction occurs.

**Instructions:**
Execute Approach A & B for Customer Journey Mapping, contrasting the current friction-filled workflow (As-Is) with the optimized workflow (To-Be).

**3.1 Approach A: Customer-Led Journey Mapping (As-Is State)**
| Journey Stage | Customer Actions | Touchpoints | Pain Points / Friction (The "But") | Emotional State (The "Makes me feel") |
|---|---|---|---|---|
| awareness | | | | |
| consideration | | | | |
| decision | | | | |
| implementation | | | | |
| loyalty | | | | |

**3.2 Approach B: Solution-Led Journey Mapping (To-Be State)**
| Journey Stage | New Actions Enabled | Upgraded Touchpoints | Transformed State | Emotional State |
|---|---|---|---|---|
| awareness | | | | |
| consideration | | | | |
| decision | | | | |
| implementation | | | | |
| loyalty | | | | |

**Outputs:**
- Customer journey mapping document (`problem/customer-journey.md`)
