# Problem & Opportunity Definition Phase Reference

## Purpose

Extract insights from the Research phase to accurately and deeply define the customer's problem and the resulting opportunity before designing a solution. Defining the problem and opportunity correctly is the most critical step in the entire business plan formulation.

## Inputs

**Process Dependencies:**
- **Phase 1: Research (Mandatory):** Technical constraints, competitor lists, and initial market scanning must be complete before defining specific customer problems.

**You MUST synthesize information from ALL previously completed phases before drafting.** 
The business plan is a cumulative pipeline. Your inputs include:
1. **Previous Phase Outputs:** All documents and research logs generated in Phase 1 (Research).
2. **Existing Workspace Data:** Always check the output directory (`{output_folder}/businessplan-writing/`) for any existing `problem/` folder or `research/` data. If files already exist from a previous execution, you must incorporate their content to ensure continuity and avoid duplication.
3. **Primary Direct Dependencies:** Phase 1: Research (company context, customer search, competitive landscape).

## Core Philosophy: The "As-Is" First Rule
**CRITICAL:** Before defining a "problem" or proposing a "solution," you MUST research and document the **As-Is state** of the customer objectively. Customers are often unaware that they have a "problem" or that a "solution" exists; they simply exist within a current workflow or context. Observing this state without judgment is the only way to identify latent needs and disruptive opportunities.

## Core Philosophy: The "55 Minutes" Rule
(Albert Einstein: *"If I had an hour to solve a problem I would spend 55 minutes thinking about the problem and 5 minutes thinking about the solution."*)
If you define the problem incorrectly, even a perfect solution will fail because it solves the wrong thing.

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Identify Customers & Stakeholders | `problem/customers.md` | Map users, buyers, beneficiaries, and the decision-making ecosystem |
| 2 | Conduct Deep Search by AI | `problem/research-log.md` | Deep search for current workflows, industry trends, and hidden friction |
| 3 | Write Proto-Persona | `problem/proto-persona.md` | Hypothesis-driven personas with behavioral traits and assumption tagging |
| 4 | Conduct User Interview by AI | `problem/interviews.md` | **Simulate discovery interviews with multiple personas using AI to capture qualitative depth** |
| 5 | Conduct Survey by AI | `problem/surveys.md` | **Simulate cohort-wide responses using AI to gather directional quantitative data** |
| 6 | Validate Customer-Problem Fit | `problem/fit-check.md` | Evaluate the alignment between the identified customer and the problem |
| 7 | Write Empathy Map | `problem/empathy-map.md` | Map what the customer thinks, feels, says, and does in their current state |
| 8 | Write Customer Journey | `problem/customer-journey.md` | Map end-to-end current experience across stages, actions, touchpoints, emotions, and KPIs |
| 9 | Write As-Is State | `problem/as-is-state.md` | Objective documentation of the current workflow without judgment |
| 10 | Write Jobs-To-Be-Done | `problem/jtbd.md` | Define functional, social, and emotional jobs, plus associated pains and gains |
| 11 | Write To-Be State | `problem/to-be-state.md` | Define the desired future state and the unique gains to be unlocked |
| 12 | Apply Problem Framing Canvas | `problem/framing-canvas.md` | Explore the problem space through Look Inward, Look Outward, and Reframe phases |
| 13 | Write Problem Statement | `problem/problem-statement.md` | Formal definition of the gaps identified between As-Is and To-Be |
| 14 | Write User Story Map | `problem/user-story-map.md` | Organize activities, steps, and tasks into a narrative flow |
| 15 | Define User Stories | `problem/user-stories.md` | Create development-ready stories with Mike Cohn format, Gherkin AC, and splitting |
| 16 | Write Consequences of Problem | `problem/consequences.md` | Quantify the impact of the problem and the cost of inaction |
| 17 | Write Existing Attempts | `problem/existing-attempts.md` | Analyze why previous or homegrown solutions failed |
| 18 | Synthesize Discovery Insights | `problem/discovery-synthesis.md` | Perform thematic analysis and update problem statement based on research |

---

## Detailed Sub-Task Instructions

### 1. Identify Customers & Stakeholders

**Dependencies:**
- **Phase 1: Research:** Use the initial company/market context and team background to define the target ecosystem.
- **Phase 1: Research:** Use the initial customer deep search data to identify primary roles.

Map every human actor touched by, paying for, or impacted by the solution to ensure the problem statement aligns with real-world dynamics.
- **Identify Core Roles:** 
    - **End-Users:** Those who interact with the product daily.
    - **Economic Buyer:** The person with budget authority and a focus on ROI.
    - **Technical Buyer:** Evaluators focused on features, security, and integration (e.g., IT, Security).
    - **Beneficiaries:** Indirect gainers who benefit from the user's increased efficiency.
- **Map Gatekeepers & Blockers:** 
    - **Gatekeepers:** Those who control access to decision-makers or data (e.g., Executive Assistants, Data Privacy Officers).
    - **Blockers:** Identify those with veto power and document their specific "Risk Triggers" (what makes them say 'No').
- **Map Champions:** Identify respected internal advocates who feel the pain most acutely and can translate value into the organization's language.
- **Analyze Influence & Motivations:** Create a map showing reporting lines and informal influence paths. Define the "Adoption Trigger" for each role (what specific event makes them want to change?).
- **Rule of Evidence:** Cite specific sources (interviews, market scans) for every claim. Use bilingual (JP/EN) labeling for all key insights.
- **Deliverable:** Comprehensive Customer Matrix and Decision Ecosystem Map in `problem/customers.md`.

### 2. Conduct Advanced Market & Customer Search

**Dependencies:**
- **Sub-task 1 (Stakeholders):** Use the identified target segments and specific roles to focus search queries.
- **Phase 1: Research:** Incorporate initial competitor and market scan data.

Perform targeted deep searches to validate the size and intensity of pain points for each stakeholder role.
- **Unmet Needs Discovery:** List specific unknowns regarding customer pains. Search specifically for "current workarounds" and "manual hacks" to see how people solve the problem today.
- **Review Mining:** Instruct the AI to analyze negative reviews of current/competing solutions (e.g., G2, Reddit, App Store) to identify recurring friction points.
- **Artifact Simulation:** Prompt the AI to generate examples of the artifacts (e.g., reports, spreadsheets, emails) the customer currently uses. Analyze these for "Hidden Costs" (time, error risk).
- **Iterative Drilling:** Use initial AI outputs to probe deeper into specific workflows, "hidden" costs, or emerging regulatory shifts.
- **Synthesize & Verify:** Consolidate AI-generated insights into a coherent report. Cross-verify critical data points (metrics, feature claims) against cited sources.
- **Deliverable:** Synthesized research report and a log of advanced prompts in `problem/research-log.md`.

### 3. Write Proto-Persona

**Dependencies:**
- **Phase 1: Research:** Use the demographic and firmographic data gathered during the "Customer Deep Search" phase.
- **Sub-task 1 (Stakeholders):** Personas must represent the specific roles identified in the decision-making ecosystem.
- **Sub-task 2 (Market Search):** Incorporate findings on current workarounds and pain intensity to build high-fidelity profiles.

Create an initial, hypothesis-driven **Proto-Persona** that synthesizes available user research and market data into a working customer profile.
- **Define Identity:**
    - **Name:** Assign an alliterative, memorable name (e.g., "Manager Mike," "Logistic Larry").
    - **Bio & Demographics:** Describe their role, industry, seniority, and **behavioral traits** (e.g., "works remotely," "active in industry Slacks"). Avoid demographics without behavior.
- **Capture Their Voice:**
    - **Quotes:** Use real or representative quotes that expose mindset and frustrations. If quotes are absent, use `[PLACEHOLDER—NEEDS RESEARCH]`.
- **Document Their Context:**
    - **Pains:** List specific frustrations related to the problem space.
    - **What is This Person Trying to Accomplish?**: Observable behaviors or outcomes they are pursuing.
    - **Goals:** Document both tactical ("ship faster") and aspirational ("get promoted") outcomes.
- **Understand Their Influences:**
    - **Decision-Making Authority:** Document their budget power and procurement role (e.g., "Buyer," "User," "Gatekeeper").
    - **Decision Influencers:** Identify who shapes their choices (peers, analysts, bosses, social media).
- **Validate and Iterate:**
    - **Tag Assumptions:** Mark any uncertain claims with `[ASSUMPTION—VALIDATE]`.
    - **Identify Gaps:** Note what isn't known yet about the persona to guide the AI Interview phase.
- **Deliverable:** 1-3 detailed proto-persona profiles in `problem/proto-persona.md`.

### 4. Conduct User Interview by AI

**Dependencies:**
- **Sub-task 3 (Persona):** AI agents MUST be prompted with the specific attributes, quotes, and mindsets defined in the personas.
- **Sub-task 2 (Market Search):** Use identified friction points to guide the interview probing.

Plan and conduct simulated one-on-one interviews with priority customer personas using "The Mom Test" principles to extract real-world behavior.
- **Set Simulation Constraints:** Prompt the AI to act as specific personas (e.g., one end user, one economic buyer). Instruct the AI to respond based on *past behavior and current pain*, not hypothetical future interest.
- **Structure the Interview:**
    - **Opening:** Build rapport and set the context ("This is for research, not a sales pitch").
    - **Core (Past Behavior):** Ask "Tell me about the last time you..." or "Walk me through what you did step-by-step." Avoid leading questions.
    - **Closing & Referral:** Ask "Who else should I talk to?" and "Is there anything I should have asked but didn't?"
- **Probe & Avoid Bias:** Dig deeper into specific friction points ("What made that hard?"). Actively avoid confirmation bias (don't pitch your solution).
- **Define Success Criteria:** The simulation is successful if you identify *surprising* friction points, uncover *failed* past workarounds, and can capture *verbatim quotes* representing high pain.
- **Deliverable:** Full transcripts for all interviews and a synthesized cross-persona insight summary in `problem/interviews.md`.

### 5. Design Cohort Survey by AI

**Dependencies:**
- **Sub-task 1 (Stakeholders) & 2 (Research):** Use the demographic and pain-point hypotheses to structure the survey questions.
- **Sub-task 3 (Persona):** Ensure the virtual cohort reflects the persona diversity and seniority levels.

Draft a specialized survey for AI personas or target crowdsourcing to gather quantitative data on pain point frequency.
- **Define the Virtual Cohort:** Describe the target group (e.g., "200 logistics managers at mid-sized firms").
- **Design the Survey:** Create clear, unbiased questions (multiple-choice, Likert scales, open-ended).
- **Configure the AI Cohort Agent:** Instruct the AI to generate a specified number of unique, realistic responses that reflect the cohort's likely biases and diversity.
- **Analyze Results:** Identify trends, common themes, and response frequencies.
- **Deliverable:** Survey questions, raw structured data (CSV/JSON), and analysis report in `problem/surveys.md`.

### 6. Write Customer Profile Mapping

**Dependencies:**
- **Sub-task 1 (Stakeholders):** Profile specific representative organizations or users from the stakeholder map.
- **Sub-task 4 (Interviews) & 5 (Surveys):** Use the qualitative and quantitative evidence to confirm if the profile matches the segment.

Apply the Alexander Osterwalder Customer Profile framework to map specific gains and pains.
- **Alignment Check:** Compare the identified pain points and JTBD against the selected customer segment.
- **Re-evaluate:** If the fit is poor (e.g., the problem isn't critical for this segment), re-evaluate the customer selection or the problem scope.
- **Deliverable:** Validation report in `problem/fit-check.md`.

### 7. Build Empathy Map

**Dependencies:**
- **Sub-task 3 (Persona):** Every empathy map must be anchored in a specific persona's worldview.
- **Sub-task 4 (Interviews):** Populate the map using the verbatim quotes and emotional signals captured in AI interviews.

Synthesize interview notes into a visual empathy map to identify emotional drivers.
- **Quadrants:** Fill in the four sections: Says (quotes), Thinks (motivations), Does (behaviors), and Feels (emotions).
- **Identify Pains & Gains:** Note the specific pain points and desired positive outcomes.
- **Deliverable:** Completed empathy map in `problem/empathy-map.md`.

### 8. Write Customer Journey

**Dependencies:**
- **Sub-task 3 (Persona):** The journey must be specific to the primary persona's goals and context.
- **Sub-task 4 (Interviews) & 5 (Surveys):** Qualitative and quantitative behavior captured in interviews/surveys must feed the journey's emotional map.

Document the end-to-end current experience to identify touchpoints, emotional shifts, and moments of friction.
- **Define Horizontal Stages:** Map the journey across Awareness, Consideration, Decision, Service, and Loyalty.
- **Define Vertical Lanes:** For each stage, document:
    - **Customer Actions:** What the customer *actually* does.
    - **Touchpoints:** Where and how they interact (digital, physical, human).
    - **Customer Experience:** Emotions and thoughts (use verbatim quotes from AI interviews when possible).
    - **KPIs:** Measurable indicators for the success of that stage.
    - **Business Goals:** What the organization aims to achieve.
    - **Teams Involved:** Cross-functional owners.
- **Highlight Friction:** Identify "pain points" where negative emotions and low KPIs intersect.
- **Deliverable:** Detailed Customer Journey table mapping the end-to-end experience in `problem/customer-journey.md`.

### 9. Write As-Is State

**Dependencies:**
- **Phase 1: Research:** Use industry standard workflows found in competitive research to baseline the "status quo".
- **Sub-task 8 (Journey):** Document the literal workflow corresponding to the actions in the customer journey.

**The foundation of the phase.** Objective documentation of the current workflow.
- **Describe Situation:** Summarize the present context and symptoms without judgment.
- **Rule:** Do not use the words "problem," "bad," "inefficient," or "solution."
- **Baseline Data:** Include relevant metrics or observations of the current state.
- **Deliverable:** Objective as-is state documentation in `problem/as-is-state.md`.

### 10. Write Jobs-To-Be-Done

**Dependencies:**
- **Sub-task 4 (Interviews) & 8 (Journey):** Extract functional and emotional goals from the interview transcripts and journey touchpoints.
- **Sub-task 9 (As-Is):** Jobs must be defined in the context of the current situation.

Clarify what users are trying to achieve and the underlying motivations using the Jobs-to-be-Done framework.
- **Identify Customer Jobs:**
    - **Functional Jobs:** Specific tasks or problems they want to solve (e.g., "reconcile expenses").
    - **Social Jobs:** How they want to be perceived by others (e.g., "appear professional to clients").
    - **Emotional Jobs:** Emotional states they want to achieve or avoid (e.g., "feel in control," "avoid anxiety").
- **Map Pains:** Document obstacles and negative outcomes:
    - **Challenges & Costliness:** Barriers and what's too expensive in time/money.
    - **Common Mistakes:** Frequent errors that could be prevented.
    - **Unresolved Problems:** Gaps current solutions fail to address.
- **Uncover Gains:** Document expected or surprising benefits:
    - **Savings & Expectations:** Time/money reductions and "must-have" benefits.
    - **Adoption Factors:** What would make them "fire" their current solution and "hire" yours.
    - **Life Improvement:** How life is better when the job is easier.
- **Quality Checks:**
    - **Solution-Agnostic:** Ensure you're describing the *need*, not the tool (e.g., "Communicate with team," not "Use Slack").
    - **Verb-Driven:** Use active verbs ("send," "analyze," "coordinate").
    - **Grounded in Evidence:** Use verbatim quotes from AI interviews to validate each pain/gain.
- **Deliverable:** Structured list of jobs, pains, and gains for each persona in `problem/jtbd.md`.

### 11. Write To-Be State

**Dependencies:**
- **Sub-task 9 (As-Is):** The To-Be state must explicitly solve the friction points identified in the As-Is state.
- **Sub-task 10 (JTBD):** Use the desired "Gains" as the definition of success for the To-Be state.
- **Phase 6: Traction & Progress:** The transition from As-Is to To-Be depends on the release timing of product.

Describe the ideal scenario where the problem is resolved and the gap between current and future state.
- **Ideal Scenario:** Articulate what success looks like if the problem no longer exists.
- **Define Gap:** Clearly illustrate the difference between the As-Is and To-Be states.
- **Deliverable:** Ideal state description and gap analysis in `problem/to-be-state.md`.

### 12. Apply Problem Framing Canvas

**Dependencies:**
- **Phase 1: Research:** Incorporate ecosystem dynamics and industry barriers.
- **Sub-task 10 (JTBD):** Use identified "Pains" and "Gains" to frame the re-statement.

Explore the problem space through the MITRE Problem Framing Canvas (Look Inward, Look Outward, and Reframe).
- **Phase 1: Look Inward:**
    - **Symptoms:** Describe the problem as currently understood.
    - **Barriers:** Why hasn't this been solved? (New, hard, low priority, lack of authority).
    - **Biases:** How is the team part of the problem? Identify confirmation bias or solution-first thinking.
- **Phase 2: Look Outward:**
    - **Experience:** Who experiences this, when, where, and with what consequences?
    - **Stakeholders:** Who else has this problem? Who doesn't?
    - **Dynamics:** Who's been left out? **Who benefits when the problem exists?** (Status quo gainers).
- **Phase 3: Reframe:**
    - Restate the problem using insights from the inward/outward analysis.
    - Develop "How Might We" (HMW) statements: `How might we [action] as we aim to [objective]?`
- **Deliverable:** Completed Problem Framing Canvas and HMW statements in `problem/framing-canvas.md`.

### 13. Write Problem Statement

**Dependencies:**
- **Sub-task 3 (Proto-Persona):** The primary persona is the protagonist of the narrative.
- **Sub-task 10 (JTBD):** Requires the functional, social, and emotional jobs.
- **Sub-task 12 (Framing Canvas):** Use the reframed problem and HMW statements as the foundation.

Refine the framed problem into a user-centered, empathy-driven narrative and formal statement.
- **Task 13-1: Problem Framing Narrative (First-Person):**
    - **I am:** [Persona description with 3-4 key characteristics]
    - **Trying to:** [Desired outcomes/results, not tasks]
    - **But:** [Specific barriers preventing the outcomes]
    - **Because:** [Identify the **Root Cause**, avoiding surface symptoms]
    - **Which makes me feel:** [Authentic emotional impact - e.g., "stuck," "anxious," "invisible"]
- **Task 13-2: Document Context & Constraints:** List factors like offline requirements, time sensitivity, or technical literacy levels.
- **Task 13-3: Craft the Final Problem Statement:** Synthesize into a single, high-impact sentence.
    - **Formula:** `[Persona] needs a way to [desired outcome] because [root cause], which currently [emotional/practical impact].`
- **Deliverable:** Structured narrative, constraints, and final problem statement in `problem/problem-statement.md`.

### 14. Write User Story Map

**Dependencies:**
- **Sub-task 8 (Journey) & 11 (To-Be):** Use the desired future state and customer journey as the basis for the activities.
- **Sub-task 10 (JTBD):** Ensure the map activities address the functional and emotional jobs.
- **Sub-task 13 (Problem Statement):** The narrative flow must be focused on solving the core problem.

Visualize the future user journey by creating a hierarchical map using the Jeff Patton framework.
- **Identify Backbone (Activities):** List 3-5 high-level activities the user performs (e.g., "Onboard," "Analyze Data," "Export Report").
- **Break into Steps:** For each activity, define the sequential steps a user takes.
- **Detail Tasks:** For each step, list granular tasks required.
- **Prioritize Vertically:** Arrange tasks by priority (Top = MVP/Release 1, Bottom = Future).
- **Deliverable:** Hierarchical user story map (Backbone, Steps, Tasks) in `problem/user-story-map.md`.

### 15. Define User Stories

**Dependencies:**
- **Sub-task 14 (Mapping):** Tasks from the user story map are converted into formal user stories.
- **Sub-task 13 (Problem Statement):** Every story must directly contribute to mitigating the root cause or emotional impact.

Translate tasks and needs into actionable outcomes using the Mike Cohn format and Gherkin-style acceptance criteria.
- **Draft Use Cases (Mike Cohn format):** 
    - **As a:** [Specific persona from `problem/proto-persona.md`]
    - **I want to:** [Action user takes]
    - **So that:** [Value/Outcome — avoid restating the action]
- **Apply Splitting Patterns:** If a story feels too large for a single sprint, apply patterns from `skills/user-story-splitting/SKILL.md`:
    - Workflow steps, Business rule variations, Data variations, Acceptance criteria complexity.
- **Define Acceptance Criteria (Gherkin format):**
    - **Given:** [Precondition]
    - **When:** [Event that triggers the 'I want to' action]
    - **Then:** [Expected outcome aligned to 'so that']
- **INVEST Check:** Ensure stories are Independent, Negotiable, Valuable, Estimable, Small, and Testable.
- **Deliverable:** List of structured, vertically sliced user stories with Gherkin acceptance criteria in `problem/user-stories.md`.

### 16. Write Consequences of Problem

**Dependencies:**
- **Sub-tasks 9 (As-Is) & 10 (JTBD):** The consequences are the direct results of the failure to solve the JTBD within the current workflow.
- **Sub-task 13 (Problem Statement):** Consequences must validate the "Which makes me feel" impact.

Quantify the impact of the problem and the cost of inaction.
- **Explain Impact:** Describe negative effects on finance, operations, or customer satisfaction.
- **Quantify:** Use statistics, metrics, or examples to establish the importance of solving the problem.
- **Deliverable:** Impact analysis and opportunity cost in `problem/consequences.md`.

### 17. Write Existing Attempts

**Dependencies:**
- **Phase 1 (Research):** Use the competitive intelligence to list and critique why current products fall short.
- **Sub-task 9 (As-Is):** Compare existing attempts against the documented status quo.

Analyze why previous or homegrown solutions failed or are insufficient.
- **Research Solutions:** Identify current workarounds, legacy systems, or competitor attempts.
- **Assess Effectiveness:** Evaluate the strengths, weaknesses, and persistent gaps of these attempts.
- **Deliverable:** Analysis of existing attempts and identified gaps in `problem/existing-attempts.md`.

### 18. Synthesize Discovery Insights

**Dependencies:**
- **Sub-tasks 1-17 (Cumulative):** This sub-task is the final summary of all qualitative and quantitative discovery in this phase.
- **Phase 1: Research:** Discovery insights must account for the current market window and the release timing of product.

Consolidate qualitative and quantitative data from interviews, surveys, and deep searches to identify recurring patterns.
- **Thematic Analysis (Affinity Mapping):** Group insights and customer quotes into themes (e.g., "setup complexity," "data silos," "high cost").
- **Frequency & Intensity Counting:** Document how many personas mentioned each theme and the perceived severity of the pain.
- **Saturation Check:** Confirm if patterns have stabilized (hearing the same things from 3+ independent sources). If not, identify remaining "unknowns."
- **Prioritize Pain Points:** Rank themes based on Frequency × Intensity × Strategic Fit.
- **Refine Problem Statement:** Update the initial problem statement based on research evidence (did the hypothesis hold?).
- **Deliverable:** Synthesized discovery report with affinity map and ranked pain points in `problem/discovery-synthesis.md`.
---

## Phase Validation Checklist

- [ ] As-Is state documented objectively without using "problem" or "solution" terminology.
- [ ] **AI-driven user interviews and cohort surveys conducted to validate hypotheses.**
- [ ] **Thematic analysis and frequency counting performed to synthesize discovery insights.**
- [ ] Stakeholder ecosystem mapped with role definitions (User, Buyer, Blocker).
- [ ] **Hypothesis-driven proto-personas created with identity, voice (quotes), pains/goals, behavioral traits, and assumption tagging.**
- [ ] Customer-Problem Fit validated; if fit was poor, customer selection was re-evaluated.
- [ ] Customer Journey (As-Is) mapped across horizontal stages and vertical lanes (actions, touchpoints, emotions, KPIs).
- [ ] **JTBD defined at Functional, Emotional, and Social levels with specific Pains and Gains documented.**
- [ ] **Problem Framing Canvas applied to explore internal biases, stakeholder dynamics (who benefits/loses), and reframing.**
- [ ] **Problem reframed into actionable "How Might We" statements.**
- [ ] **User story map created with Backbone, Steps, and prioritized Tasks.**
- [ ] User stories follow the "As a [role]..." construct and include specific "So that" outcomes.
- [ ] **User stories vertically sliced to deliver value within a single sprint.**
- [ ] **Acceptance criteria defined in Gherkin (Given/When/Then) format and independently testable.**
- [ ] Every problem includes a quantified Opportunity Cost (Metric + Narrative).
- [ ] "Cost of Inaction" and "Failed Attempts" analyzed to justify the new solution.
