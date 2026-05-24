# ROI Calculation Phase Reference

## Purpose

To calculate the precise Return On Investment (ROI), **specifically Net Present Value (NPV) and Internal Rate of Return (IRR)**, for the customer based on our proposed pricing and their anticipated cost savings or revenue generation.

This phase relies on generating cash flow records and using the included `calculate_roi.py` script to ensure accurate calculations of modern investment metrics.

## Prerequisites
Before beginning this phase, you must have established and fully reviewed all deliverables from the previous phases, specifically:
- All Costing & Pricing files from Phase 5: `costing/cost-estimate.md`, `costing/pricing-strategy.md`, `costing/revenue-kpi-model.md`, and `costing/pricing-presentation.md`. **You must use all of these files as direct inputs to ensure your ROI calculations are perfectly aligned with both our internal delivery cost floors, the sales funnel conversion assumptions (Awareness → Interest → Consideration → Purchase), Customer Lifetime Value (LTV), and the final strategic pricing model.**
- The Customer's Cost of Status Quo and anticipated benefits from Phase 1 and 2 (Research and Problem & Opportunity Definition).

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Determine Detailed Cash Inflows and Outflows | `roi/cashflows.json` | Categorize monthly flows into Operating, Investing, and Financing |
| 2 | Identify Risk Free Rate ($R_f$) | `roi/risk-free-rate.json` | Research and record 10-year government bond yield |
| 3 | Identify Market Risk Premium ($MRP$) | `roi/market-risk-premium.json` | Establish benchmark equity market premium |
| 4 | Select Comparable Peers | `roi/comparable-peers.json` | Select 3-5 public companies for benchmarking |
| 5 | Extract Peer Unlevered Beta | `roi/peer-unlevered-beta.json` | Gather levered betas and calculate unlevered beta |
| 6 | Calculate Levered Beta | `roi/levered-beta.json` | Re-lever the beta for the target capital structure |
| 7 | Calculate CAPM Risk Premium | `roi/capm-risk-premium.json` | Calculate levered beta multiplied by MRP |
| 8 | Identify Size Risk Premium | `roi/size-risk-premium.json` | Apply small-cap or startup risk premiums |
| 9 | Identify Illiquidity Premium | `roi/illiquidity-premium.json` | Model non-marketability risk for private shares |
| 10 | Calculate New Business Risk Premium | `roi/business-premium.json` | Define risk based on the funding stage |
| 11 | Summarize Cost of Equity ($R_e$) | `roi/cost-of-equity.json` | Aggregate all equity risk components |
| 12 | Identify Cost of Debt | `roi/cost-of-debt.json` | Calculate the after-tax cost of debt |
| 13 | Define Capital Structure | `roi/capital-structure.json` | Determine target weight of debt and equity |
| 14 | Derive WACC | `roi/wacc.json` | Calculate Weighted Average Cost of Capital |
| 15 | Calculate Hurdle Rate Multiple | `roi/hurdle-rate-multiple.json` | Calculate required equity return divided by WACC |
| 16 | Calculate Discount rate | `roi/discount-rate.json` | Final valuation rate (WACC x Multiple) |
| 17 | Calculate Categorical Cash Flow Totals | `roi/financial-metrics.md` | Report totals for Operating, Investing, and Financing (In/Out/Net) |
| 18 | Calculate Cumulative CF & Lowest Value | `roi/financial-metrics.md` | Identify the "trough" (Max Funding Requirement) and its timing |
| 19 | Calculate Payback Period | `roi/financial-metrics.md` | Determine the month when the project reaches break-even |
| 20 | Calculate Multiple on Invested Capital (MOIC) | `roi/financial-metrics.md` | Calculate return relative to Invested Capital (Investing Outflows) |
| 21 | Calculate Net Present Value (NPV) | `roi/financial-metrics.md` | Calculate the discounted value of all future cash flows |
| 22 | Calculate Internal Rate of Return (IRR) | `roi/financial-metrics.md` | Extract and verify the annualized IRR from the calculation results |
| 23 | Validate and Troubleshoot IRR | `roi/irr-validation.md` | Ensure IRR is a valid number and justify if manual calculation is needed |
| 24 | Write Narrative Financial Impact | `roi/financial-impact.md` | Explain the metrics as a time-series story for executive decision-makers |

> **Important Tooling Requirement:** You must utilize the `scripts/calculate_roi.py` script included in this skill to perform the financial math. Include its output entirely in the `financial-impact.md`.

---

## Detailed Sub-Task Instructions

### 1. Determine Detailed Cash Inflows and Outflows

Gather all necessary financial components to build a detailed monthly JSON array representing the cash flow from `Month 0` to `Month N` (typically 36 to 60 months).

**Instructions:**
You **must** calculate and break down cash flows into the following categories for each month. This level of detail is required for the categorical ROI report:

1. **Operating Inflows**:
   - E.g., Revenues from sales, recurring SaaS fees, savings recognized as cash.
2. **Operating Outflows**:
   - E.g., Salaries, OpEx, cloud costs, marketing, maintenance.
3. **Investing Inflows**:
   - E.g., Salvage value, sale of equipment, exit proceeds.
4. **Investing Outflows (Invested Capital)**:
   - E.g., Initial R&D, CapEx, setup fees, implementation costs.
5. **Financing Inflows**:
   - E.g., Equity injections, loan proceeds.
6. **Financing Outflows**:
   - E.g., Debt servicing, dividends.

> **CRITICAL IRR PRE-REQUISITE:** To calculate a valid Internal Rate of Return (IRR), your monthly cash flows MUST contain at least one month of net negative cash flow (initial investment) followed by periods of net positive cash flow.

**Output `roi/cashflows.json` Structure:**
```json
{
  "discount_rate": 0.10,
  "cashflows": [
    {
      "month": 0,
      "operating_inflows": { "revenue": 0 },
      "operating_outflows": { "salaries": 5000 },
      "investing_inflows": {},
      "investing_outflows": { "setup": 10000 },
      "financing_inflows": {},
      "financing_outflows": {}
    }
  ]
}
```

> **CRITICAL ALIGNMENT RULE:** The profit figures you insert for the projected sales must *algebraically align* with the unit economics established in the Phase 5 Costing outputs (e.g., `pricing-presentation.md`).

---

### 2. Identify Risk Free Rate ($R_f$)
**Target File:** `risk-free-rate.json`

**Detailed Steps:**
1. **Research Benchmark Yields:** Identify the current yield on 10-year government bonds in the target market (e.g., JGB for Japan).
2. **Assign Risk-Free Value:** Record the yield for use as the baseline $R_f$ in the Cost of Equity calculation.
3. **Document Source:** Record the source and date of the yield data.

### 3. Identify Market Risk Premium ($MRP$)
**Target File:** `market-risk-premium.json`

**Detailed Steps:**
1. **Define Benchmark Premium:** Establish the excess return of the broad equity market over the risk-free rate.
2. **Apply Standard Range:** Use a benchmark range of 5.0% to 6.0% for the 2024-2025 period.
3. **Document Rationale:** Record the source or market study used to define the $MRP$.

### 4. Select Comparable Peers (類似企業選定)
**Target File:** `comparable-peers.json`

**Detailed Steps:**
1. **Identify Public Peers:** Select 3-5 public companies in the same or closely related industry.
2. **Review Business Similarity:** Ensure peers share similar revenue models, target markets, and growth profiles.
3. **Document Peer Rationale:** Briefly explain why each peer was selected for the valuation benchmarking.

### 5. Extract Peer Unlevered Beta (アンレバードベータ)
**Target File:** `peer-unlevered-beta.json`

**Detailed Steps:**
1. **Gather Levered Betas:** Research the current levered beta ($\beta_L$) for each selected peer.
2. **Identify Peer Capital Structures:** Extract the Debt-to-Equity (D/E) ratios and tax rates for the selected peers.
3. **Calculate Unlevered Beta ($\beta_U$):** Use the Hamada equation or similar: $\beta_U = \beta_L / (1 + ((1 - Tax) * (D / E)))$.

### 6. Calculate Levered Beta (レバードベータ)
**Target File:** `levered-beta.json`

**Detailed Steps:**
1. **Define Target Capital Structure:** Determine the target Debt-to-Equity (D/E) ratio and effective tax rate for the target company.
2. **Re-lever the Beta:** Calculate the target company's levered beta ($\beta_L$) using the average unlevered beta from Sub-task 5. **Formula:** $\beta_L = \text{Avg}(\beta_U) * (1 + ((1 - Tax) * (D / E)))$.
3. **Assign Valuation Beta:** Record this final $\beta_L$ for use in the CAPM calculation.

### 7. Calculate CAPM Risk Premium (CAPMリスクプレミアム)
**Target File:** `capm-risk-premium.json`

**Detailed Steps:**
1. **Apply CAPM Formula:** Calculate the equity risk premium as $\beta_L * MRP$.
2. **Verify Inputs:** Use the final levered beta from Sub-task 6 and the market risk premium from Sub-task 3.
3. **Summarize CAPM Results:** Record the calculated risk premium for inclusion in the total Cost of Equity ($R_e$).

### 8. Identify Size Risk Premium (サイズリスクプレミアム)
**Target File:** `size-risk-premium.json`

**Detailed Steps:**
1. **Apply Benchmark Statistics:** Use a long-term average mean of 2.0% to 3.5% for small-cap vs. large-cap.
2. **Identify Small-cap/Startup Risk:** For startups or micro-cap companies (Kroll/Duff & Phelps Decile 10z), establish a benchmark between 11.2% and 12.0%.
3. **Document Distribution Logic:** Note that the median is typically lower than the mean due to skewed return distributions.

### 9. Identify Illiquidity Premium (非流動性プレミアム)
**Target File:** `illiquidity-premium.json`

**Detailed Steps:**
1. **Model Non-Marketability Risk:** Compensate for the inability to quickly convert private shares into cash.
2. **Apply Average Benchmarks:** Use a typical mean of 3.0% (Range: 2.0% to 4.0%) for the incremental risk premium.
3. **Assign Valuation Premium:** Record the selected percentage for inclusion in the total Cost of Equity calculation.

### 10. Calculate New Business Risk Premium (新規事業リスクプレミアム)
**Target File:** `business-premium.json`

**Detailed Steps:**
1. **Define New Business Risk:** Identify the additional rate of return required by investors specifically due to the inherent uncertainty and execution risk of a new venture.
2. **Apply Stage-Based Benchmarks:** Set the risk premium based on the current funding stage of the company:
    - **Seed Stage (シード):** 40%
    - **Series A (シリーズA):** 30%
    - **Series B (シリーズB):** 25%
    - **Series C (シリーズC):** 20%
    - **Existing Business (既存事業):** 0%
3. **Assign Valuation Premium:** Record the selected percentage for inclusion in the total Cost of Equity ($R_e$) calculation.

### 11. Summarize Cost of Equity ($R_e$)
**Target File:** `cost-of-equity.json`

**Detailed Steps:**
1. **Apply Build-up Formula:** Calculate $R_e$ as $R_f$ (Sub-task 2) + ($Beta$ (Sub-task 6) * $MRP$ (Sub-task 3)) + Size Risk Premium (Sub-task 8) + Illiquidity Premium (Sub-task 9) + New Business Risk Premium (Sub-task 10).
2. **Verify Statistical Selection:** Use **Median** values for long-term modeling to minimize the impact of outliers.
3. **Sanity Check with Mode:** Document a \"market standard\" comparison using the **Mode** to ensure the result aligns with practitioner expectations.

### 12. Identify Cost of Debt (負債コスト)
**Target File:** `cost-of-debt.json`

**Detailed Steps:**
1. **Define Nominal Interest Rate:** Establish the average interest rate for current and projected debt (Sub-task 26).
2. **Calculate After-Tax Cost:** Apply the effective tax rate from Sub-task 28 to calculate the after-tax cost of debt: $R_d * (1 - Tax Rate)$.
3. **Summarize Debt Costs:** Record the final after-tax rate for inclusion in the WACC calculation.

### 13. Define Capital Structure (資本構成)
**Target File:** `capital-structure.json`

**Detailed Steps:**
1. **Target Weight Distribution:** Determine the target weight of debt ($W_d$) and equity ($W_e$) for the company's optimal capital structure.
2. **Review Comparable Structures:** Benchmark against peer capital structures identified in Sub-task 3.
3. **Verify Weighted Percentages:** Ensure $W_d + W_e = 100\%$.

### 14. Derive WACC (加重平均資本コスト)
**Target File:** `wacc.json`

**Detailed Steps:**
1. **Apply WACC Formula:** Calculate the weighted average cost of capital as $(W_e * R_e) + (W_d * \text{After-Tax } R_d)$.
2. **Verify Input Integration:** Use results from Sub-tasks 11, 12, and 13.
3. **Assign WACC:** Record this value for use in the Hurdle Rate and final Discount Rate calculations.

### 15. Define Hurdle Rate Multiple between WACC and Discount Rate
**Target File:** `wacc-discount-rate-multiple.json`
**Description:** Calculate the ratio of the required equity return to the weighted average cost of capital.

**Detailed Steps:**
1. **Define Hurdle Rate Multiple:** Calculate the ratio of the required equity return to the weighted average cost of capital. **Formula:** `Multiple = Discount Rate / WACC`.
2. **Identify CFO's Benchmarks:**
    - **Average:** 2.37x.
    - **Range (Min-Max):** 1.0x to 2.5x+ depending on the stage and risk profile.
3. **Document Strategic Rationale:** Record the CFO's required hurdle multiple for internal capital allocation.

### 16. Calculate Discount rate (割引率)
**Target File:** `discount-rate.json`

**Detailed Steps:**
1. **Apply Hurdle Logic:** Calculate the final valuation discount rate as `WACC x Hurdle Rate Multiple`.
2. **Integrate Inputs:** Use the WACC from Sub-task 14 and the Hurdle Rate Multiple from Sub-task 15.
3. **Assign Valuation Rate:** Record this final discount rate for use in the DCF analysis (Sub-task 17 and beyond).

---

### 17. Calculate Categorical Cash Flow Totals
**Target File:** `roi/financial-metrics.md`
**Detailed Steps:**
1. Execute the `calculate_roi.py` script using the prepared `roi/cashflows.json`.
2. Extract and report the Inflow, Outflow, and Net totals for each category:
   - **Operating Cash Flows**: Performance of core business operations.
   - **Investing Cash Flows**: Capital deployment and asset recovery.
   - **Financing Cash Flows**: External funding and debt management.
3. Report the **Total Net Cash Flow** (sum of all categories).

### 18. Calculate Cumulative CF & Lowest Value
**Target File:** `roi/financial-metrics.md`
**Detailed Steps:**
1. Identify the **Final Cumulative Cash Flow** from the script output.
2. Identify the **Lowest value of cumulative cash flow** (Max Funding Requirement).
3. Record the **Peak Deficit Month** (when this lowest value occurs). This is a critical risk metric for liquidity planning.

### 19. Calculate Payback Period
**Target File:** `roi/financial-metrics.md`
**Detailed Steps:**
1. Identify the "Payback Period" from the `calculate_roi.py` output.
2. This is the month when the project's cumulative net cash flow first crosses or hits zero.
3. Use the decimal value (e.g., 14.5 months) for precision in the narrative.

### 20. Calculate Multiple on Invested Capital (MOIC)
**Target File:** `roi/financial-metrics.md`
**Detailed Steps:**
1. Identify "MOIC (on Invested Capital)" from the script output.
2. **Standard Definition:** Total Inflow divided by the absolute value of **Investing Outflows** (Invested Capital). 
3. This metric measures the cash-on-cash return specifically for the capital deployed, ignoring operating expenses which are captured in IRR/NPV.

### 21. Calculate Net Present Value (NPV)
**Target File:** `roi/financial-metrics.md`
**Detailed Steps:**
1. Identify the "NPV" from the script output.
2. Use the discount rate established in Sub-task 16 (WACC x Hurdle Multiple).
3. Report the NPV as the absolute dollar value created today.

---

### 22. Calculate Internal Rate of Return (IRR)
**Target File:** `roi/financial-metrics.md`
**Detailed Steps:**
1. Identify the "IRR (Annualized)" from the script output.
2. IRR is the discount rate that would result in an NPV of zero, representing the project's inherent yield.
3. **CRITICAL MANDATE:** You MUST ensure the IRR is a valid numerical percentage. If the script outputs `nan%`, you MUST proceed to Sub-Task 23 to troubleshoot and resolve the issue.

---

### 23. Validate and Troubleshoot IRR

Internal Rate of Return (IRR) is often the most critical metric for executive decision-makers. A failure to provide a valid IRR is considered a phase failure.

**Instructions:**
1. **Verify Sign Change:** IRR calculation requires at least one negative cash flow (investment) followed by at least one positive cash flow (return). Ensure your `cashflows.json` contains both.
2. **Handle `nan%` Outputs:** If the script returns `nan%`, it is likely because the mathematical solver diverged. You must manually verify the cash flow series:
   - If `Total Inflow < Total Outflow` over the entire period, the IRR is effectively negative or non-existent. You must state this clearly.
   - If the project is profitable but IRR is still `nan`, try a different initial guess for the monthly rate (e.g., using a spreadsheet tool or a manual iterative check).
3. **Annualization Check:** Ensure the monthly IRR is correctly annualized using the formula: $Annual IRR = (1 + Monthly IRR)^{12} - 1$.
4. **Justification:** If the IRR is unusually high (e.g., >100%) or low (e.g., < WACC), provide a technical justification based on the unit economics or market conditions.

**Outputs:**
- `roi/irr-validation.md` documenting the verification steps and the final confirmed IRR value.

---

### 24. Write Narrative Financial Impact

The calculated KPIs are mathematical, but the customer needs a story to understand *why* this makes business sense. 

**Instructions:**
1. Extract the exact KPI numbers generated from Sub-Tasks 17 through 22 (`roi/financial-metrics.md`), specifically:
  - Categorical Cash Flows (Operating, Investing, Financing Inflows/Outflows)
  - Final Cumulative Cash Flow
  - Lowest value of cumulative cash flow (Max Funding Requirement)
  - Payback Period
  - MOIC (on Invested Capital)
  - NPV
  - IRR
2. **Understand \"Cumulative Cash Flow\" :** This represents the running total of net cash flows. The **lowest point** (the \"trough\") dictates the maximum out-of-pocket funding the customer will need to float the project.
3. **Narrative Explanation (STRICT RULE):** You MUST write a narrative explanation explaining these numbers like a story with time-series so that the audience can smoothly understand the financial impact.
   - *Example for early stage:* \"In the initial 24 months, the project focuses on infrastructure deployment, resulting in a net investing outflow of $28M.\"
   - *Example for Required Funding:* \"The project reaches its peak deficit of $28M in Month 23; this is the maximum liquidity required to see the project through to profitability.\"
   - *Example for Breakeven:* \"Break-even is achieved in Month 105, at which point the project becomes a significant cash generator.\"
   - *Example for MOIC:* \"With an MOIC of 2.30x, every dollar of invested capital generates $2.30 in returns over the project lifecycle.\"
   - *Example for NPV:* \"With an NPV of $15.4M, the project is expected to create significant value above the required return, representing a highly attractive investment opportunity.\"
   - *Example for IRR:* \"With an annualized IRR of 48.5%, the project yield significantly outperforms the market benchmark and the internal hurdle rate, confirming a highly efficient deployment of capital.\"
4. *Crucially, these exact numbers* must be clearly stated and highly visible within the story, as they MUST be perfectly extracted and placed onto the presentation slides during the Writing Phase.

**Outputs:**
- Comprehensive `roi/financial-impact.md` document that contains the narrative story wrapping the precise financial metrics from Sub-Tasks 17 through 22.

---

## Phase Validation Checklist

- [ ] Monthly cash flow list constructed with Operating, Investing, and Financing categories
- [ ] Invested Capital (Investing Outflows) correctly identified for MOIC calculation
- [ ] Appropriate discount rate (WACC x Hurdle Multiple) applied
- [ ] Resulting metrics (NPV, IRR, Payback, MOIC) generated using the `calculate_roi.py` script
- [ ] Lowest value of cumulative cash flow and peak deficit month identified
- [ ] IRR explicitly verified as a valid number (non-NaN)
- [ ] Financial impact document crafted to frame these numbers persuasively for the proposal
