# Costing & Pricing Phase Reference

## Purpose

Estimate the true cost of delivering the proposed solution, then build a strategic pricing model that maximizes win probability while protecting margins. This phase answers two distinct questions: **"What does this cost us to deliver?"** (costing) and **"What should we charge the customer?"** (pricing).

**Key principle:** Costing is an internal exercise (accuracy matters). Pricing is a strategic decision (perception matters). Never confuse the two — your price should reflect customer *value*, not just your *cost*.

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Estimate Delivery Costs (Bottom-Up) | `costing/cost-estimate.md` | Calculate the true cost of delivering each solution element |
| 2 | Build Pricing Strategy | `costing/pricing-strategy.md` | Choose pricing model and set strategic price points |
| 3 | Revenue KPI Modeling (Funnel, LTV, Conversion) | `costing/revenue-kpi-model.md` | Model the sales funnel (Awareness → Interest → Consideration → Purchase), estimate conversion rates at each stage, and calculate Customer Lifetime Value (LTV). These revenue assumptions become the direct input for the ROI Calculation phase. |
| 4 | Prepare Pricing Presentation | `costing/pricing-presentation.md` | Package pricing for maximum persuasive impact in the proposal |

---

## Detailed Sub-Task Instructions

### 1. Estimate Delivery Costs (Bottom-Up)

Calculate what it will *actually cost you* to deliver each element of the solution. This is your internal floor — the minimum you must recover.

**Inputs:**
- Solution architecture and deliverables (from Solution Design phase)
- Historical cost data from similar projects (if available)
- Staff rates, material costs, third-party fees

**Instructions:**

1. **Decompose Solution into Cost Elements:**
   Break every deliverable into its cost components:
   | Solution Element | Cost Category | Description | Estimated Hours / Qty | Unit Cost | Total Cost |
   |---|---|---|---|---|---|
   | e.g., EPC-Ready Hub | Engineering Labor | Web portal development | 80 hrs | $XX/hr | $XXXX |
   | | Design | UI/UX design | 20 hrs | $XX/hr | $XXXX |
   | | Infrastructure | Hosting, domain, CDN | 12 months | $XX/mo | $XXXX |
   | e.g., Video Production | Creative Labor | Scripting, filming, editing | 40 hrs | $XX/hr | $XXXX |
   | | Equipment / Studio | Rental, props | 1 session | $XXXX | $XXXX |

2. **Categorize All Costs:**
   | Cost Category | One-Time Costs | Recurring Costs (Monthly/Annual) | Notes |
   |---|---|---|---|
   | **Direct Labor** | | | Staff directly working on deliverables |
   | **Materials / Equipment** | | | Physical goods, software licenses |
   | **Subcontractors / Third Party** | | | External vendors, freelancers |
   | **Travel & Expenses** | | | On-site visits, trade shows |
   | **Infrastructure / Hosting** | | | Servers, domains, storage |
   | **Overhead / Management** | | | Project management, admin, insurance |
   | **Contingency (10-20%)** | | | Buffer for unforeseen work |
   | **Total Estimated Cost** | **$XXXX** | **$XXXX/mo** | |

3. **Identify Cost Risks:**
   | Risk | Impact on Cost | Probability | Mitigation |
   |---|---|---|---|
   | Scope creep (customer requests extras) | +20-30% labor | Medium | Document assumptions clearly in proposal |
   | Customer delays (late CAD file delivery) | +1-2 month timeline | Medium | Include customer responsibility clause |
   | Currency fluctuation (JPY/USD) | ±5-10% | Low | Price in customer's currency |

4. **Calculate Break-Even & Minimum Required Funding:**
   What is the minimum revenue needed to cover all costs, and what is the maximum cash dip?
   - Total one-time costs: $____
   - Monthly recurring costs: $____/month
   - Break-even revenue: $____
   - **Minimum Required Funding:** At what point will the cumulative cash flow hit its absolute lowest point (the trough)? This represents the maximum out-of-pocket cash required before the project becomes self-sustaining. Note: This is NOT just "Year 1 cost" or "Setup fee" — it is strictly the lowest point of total cumulative cash inflows vs outflows over time.

**Outputs:**
- Detailed cost estimate with line-item breakdown
- Cost risk register
- Break-even calculation

---

### 2. Build Pricing Strategy

Transform your cost estimate into a strategic price that wins the deal while protecting margins. Pricing is NOT "cost + markup" — it's a strategic lever.

**Inputs:**
- Cost estimate (from sub-task 1)
- Competitor pricing intelligence (from Research phase competitive landscape)
- Customer budget expectations (from Research)
- Value proposition and win themes (from Strategy phase)

**Instructions:**

1. **Choose Pricing Model:**
   | Model | When to Use | Advantage | Risk |
   |---|---|---|---|
   | **Fixed Price** | Well-defined scope, mature solution | Customer certainty, easy to compare | Agent bears overrun risk |
   | **Retainer + Performance** | Ongoing services, shared risk/reward | Aligns incentives, lower entry barrier | Revenue uncertainty |
   | **Time & Materials** | Uncertain scope, research-heavy | Flexible, honest | Customer may resist open-ended |
   | **Phased / Pilot-First** | Risk-averse customer, new relationship | Proves value before full commitment | Smaller initial deal size |
   | **Subscription / Recurring** | Platform, SaaS, ongoing service | Predictable for both parties | Customer may resist lock-in |
   | **Hybrid** | Complex deals with multiple components | Optimizes for different elements | Harder to explain |

   **Selected Model:** ________________
   **Rationale:** ________________

2. **Set Price Points Using Value Anchoring:**
   Your price should be positioned between your cost floor and the customer's "cost of doing nothing" (or the cost of the next-best alternative).

   ```
   [Your Cost]  ←  Your Price  →  [Customer's Cost of Status Quo / Alternative]
      Floor                              Ceiling (Value Anchor)
   ```

   | Metric | Value |
   |---|---|
   | Your total delivery cost (floor) | $ |
   | Customer's cost of status quo (annual) | $ |
   | Cost of next-best alternative (competitor or in-house) | $ |
   | Your proposed price | $ |
   | Implied margin | % |
   | Customer savings vs. alternatives | $ |

3. **Build Pricing Tiers (Optional but Recommended):**
   Offering 2-3 tiers anchors the customer to the middle/premium option (the "Goldilocks effect"):
   | Tier | Scope Summary | Price | Target Audience |
   |---|---|---|---|
   | **Essential** | Core solution only | $____ | Budget-conscious / pilot |
   | **Standard (Recommended)** | Full solution + support | $____ | Most customers |
   | **Premium** | Full solution + custom + accelerated | $____ | Strategic partnerships |

4. **Price-to-Value Linkage:**
   For every significant price component, articulate the customer value it delivers:
   | Price Component | Amount | Customer Value Delivered | Win Theme Supported |
   |---|---|---|---|
   | | | | |

5. **Compare Against Alternatives:**
   Show the customer that your price is the best value in context:
   | Alternative | Estimated Total Cost (3yr) | Time to Value | Risk Level | Key Weakness |
   |---|---|---|---|---|
   | **Your Proposal** | $ | | Low | |
   | Alternative A (competitor) | $ | | | |
   | Alternative B (in-house) | $ | | | |
   | Do Nothing (status quo) | $ (opportunity cost) | N/A | | |

**Outputs:**
- Pricing strategy document with model selection rationale
- Price-to-value linkage table
- Alternative comparison table
- Pricing tiers (if applicable)

---

### 3. Revenue KPI Modeling (Funnel, LTV, Conversion)

Model how the proposed solution generates revenue for the customer. Without explicit funnel-stage conversion rates and Lifetime Value estimates, the revenue projections fed into the ROI Calculation phase are nothing more than wishful thinking. This sub-task forces you to build a grounded, stage-by-stage revenue model.

**Key principle:** Every revenue number in the proposal must be traceable back to a specific funnel stage and a defensible conversion rate. "We expect $X in sales" is not acceptable unless you can show exactly how many people enter the top of the funnel and what percentage converts at each stage.

**Inputs:**
- Solution architecture (from Solution Design phase)
- Market size and customer research (from Research phase)
- Competitor benchmarks and industry conversion rates (from Research phase)
- Pricing strategy (from sub-task 2 above)

**Instructions:**

1. **Define the Sales Funnel Stages:**
   Map the customer's sales process (or the process your solution creates) into clear funnel stages. Use this standard framework and customize as needed:

   | Stage | Definition | Example Activity |
   |---|---|---|
   | **Awareness** | Potential customer learns that the product/company exists | Google Ad impression, trade show foot traffic, website visit |
   | **Interest** | Potential customer engages and wants to learn more | Clicks ad, visits booth, watches demo video, downloads brochure |
   | **Consideration** | Potential customer actively evaluates the product against alternatives | Requests quote, downloads CAD file, schedules demo visit, attends meeting |
   | **Purchase** | Customer commits to buying | Signs contract, places first order |

2. **Estimate Volume and Conversion Rate at Each Stage:**
   For each funnel stage, estimate the number of people/companies entering and the percentage that advance to the next stage. Use industry benchmarks, competitor data, or historical data where available. Clearly cite the source of each assumption.

   | Stage | Volume In (per month) | Conversion Rate to Next Stage | Volume Out (per month) | Source / Justification |
   |---|---|---|---|---|
   | Awareness | e.g., 10,000 ad impressions | 2.0% CTR | 200 visitors | Google Ads industry avg. |
   | Interest | 200 visitors | 5.0% | 10 inquiries | Industry B2B benchmark |
   | Consideration | 10 inquiries | 30% | 3 qualified leads | Internal historical data |
   | Purchase | 3 qualified leads | 33% | 1 new customer | Conservative estimate |

   **Monthly new customers:** ____
   **Annual new customers:** ____

3. **Calculate Customer Lifetime Value (LTV):**
   Estimate the total revenue a single customer generates over their entire relationship. This is critical for justifying acquisition costs and long-term ROI.

   | Component | Value | Source / Justification |
   |---|---|---|
   | Average order value (AOV) | $ | |
   | Purchase frequency (orders/year) | | |
   | Average customer lifespan (years) | | |
   | **Annual revenue per customer** | $ (= AOV × frequency) | |
   | **Customer Lifetime Value (LTV)** | $ (= annual revenue × lifespan) | |

   Optional advanced metrics:
   - Gross margin per customer: $____
   - Customer Acquisition Cost (CAC): $____ (from sub-task 1 costs ÷ monthly new customers)
   - **LTV:CAC Ratio:** ____ (target: ≥3:1)

4. **Model Monthly Revenue Ramp-Up:**
   New solutions do not generate full revenue from Day 1. Model a realistic ramp-up curve showing how funnel volume and conversion rates improve over time (e.g., Month 1-3: ramp-up, Month 4-12: steady state, Month 13+: growth).

   | Month | Awareness Volume | Funnel Conversion (end-to-end) | New Customers | Revenue | Notes |
   |---|---|---|---|---|---|
   | 1 | | | | $ | Setup period |
   | 2 | | | | $ | |
   | 3 | | | | $ | First leads expected |
   | ... | | | | | |
   | 12 | | | | $ | Steady state |

5. **Sensitivity Analysis (What-If Scenarios):**
   Show how the revenue changes if key assumptions shift. This builds credibility and pre-empts buyer skepticism.

   | Scenario | Key Change | Monthly New Customers | Annual Revenue |
   |---|---|---|---|
   | **Pessimistic** | Conversion rates 50% lower | | $ |
   | **Base Case** | As modeled above | | $ |
   | **Optimistic** | Conversion rates 50% higher | | $ |

**Outputs:**
- Sales funnel model with stage-by-stage conversion rates
- Customer Lifetime Value (LTV) calculation
- Monthly revenue ramp-up schedule (this feeds directly into ROI Calculation phase `cashflows.json`)
- Sensitivity analysis (pessimistic / base / optimistic)

---

### 4. Prepare Pricing Presentation

Package the pricing for maximum impact in the proposal. Raw pricing tables are not persuasive — pricing must be *presented* as value.

**Instructions:**

1. **Create Financial Summary (for proposal inclusion):**
   Distill the 3-4 most compelling financial metrics for prominent placement:
   - Headline ROI figure (e.g., "267% ROI in Year 1")
   - Payback period (e.g., "Investment recovered in 3 months")
   - Top savings metric (e.g., "Saves $261,000 vs. building a US subsidiary")
   - Cost comparison vs. alternatives (e.g., "1/8th the cost of in-house expansion")

2. **Draft Pricing Section Narrative:**
   Write the pricing section following BLUF + Proof Triangle:
   - **Lead with value** (not the number): "Your investment of $X delivers $Y in savings."
   - **Justify each component**: Why the customer should care about this cost element.
   - **Anchor against alternatives**: "Compared to the $300,000+ cost of a traditional approach..."
   - **Address price objections proactively**: "If the initial cost seems high, consider that..."

3. **Prepare Pricing Q&A:**
   Anticipate pricing objections:
   | Question | Key Message | Supporting Data |
   |---|---|---|
   | "Can you reduce the price?" | | |
   | "Why is this more expensive than [alternative]?" | | |
   | "What happens if results don't meet projections?" | | |
   | "Can we start with a smaller scope?" | | |

**Outputs:**
- Financial summary metrics for proposal
- Pricing narrative draft
- Pricing Q&A preparation

---

## Phase Validation Checklist

- [ ] All solution elements have bottom-up cost estimates with line items
- [ ] Cost risks identified with mitigations
- [ ] Break-even point calculated
- [ ] Pricing model selected with clear rationale
- [ ] Price positioned between cost floor and value ceiling
- [ ] Price-to-value linkage documented for every major component
- [ ] Pricing compared against customer alternatives
- [ ] Sales funnel stages defined with conversion rates at each stage
- [ ] Conversion rate sources cited (industry benchmark, historical data, or conservative estimate)
- [ ] Customer Lifetime Value (LTV) calculated with clear assumptions
- [ ] Monthly revenue ramp-up schedule modeled (feeds into ROI phase `cashflows.json`)
- [ ] Sensitivity analysis completed (pessimistic / base / optimistic)
- [ ] Financial summary metrics ready for proposal (top savings)
- [ ] Pricing narrative drafted with value anchoring
- [ ] Pricing Q&A prepared for objection handling
- [ ] Phase deliverables stored in `costing/` folder
