---
name: roi-calculator
description: Calculate Return on Investment (ROI) metrics such as NPV, IRR, Return Multiple, and Payback Period. Use this skill when evaluating the profitability of a project, startup investment, sales proposal, or pricing strategy by generating and analyzing monthly financial cash flows.
license: Complete terms in LICENSE.txt
---

# ROI Calculator

This skill guides the process of financial modeling and Return on Investment (ROI) calculating for business plans, products, or investments.

## Core Workflow

When the user asks to calculate the ROI or profitability of a project, follow these steps:

### 1. Identify Cash Inflows and Outflows
Work with the user to outline the duration of the project (typically 24 to 60 months).
Identify the following components:
- **Investing/Operating Outflows**: Development costs, salaries (Headcount x FTE x Salary), travel expenses, server costs.
- **Operating Inflows**: Revenues from sales, unit price x volume. 
- **Cost Savings (Inflows)**: E.g., saved labor hours x hourly rate.

*For detailed definitions of the concepts, refer to [roi_concepts.md](references/roi_concepts.md).*

### 2. Determine Discount Rate
Establish an appropriate annual discount rate, or WACC (Weighted Average Cost of Capital). If the user does not specify one, a general default hurdle rate is ~12-15%, though new risky businesses justify 30%+.
*Reference WACC breakdown in [roi_concepts.md](references/roi_concepts.md) if you need to calculate WACC manually.*

### 3. Calculate Metrics
Use the included python script to calculate the financial metrics based on the monthly totals. Calculate the Net Cashflow for each month from Month 0 up to Month N, and feed it into the calculator.

```bash
# Example syntax to calculate metrics over 6 months: Month 0..5
pip install numpy-financial
python scripts/calculate_roi.py --cashflows -500000 -100000 -50000 20000 80000 200000 --rate 0.125
```

The script outputs crucial ROI measures: Total Inflow, Total Outflow, Required Funding, Payback Period, Return Multiple, Net Present Value (NPV), and Internal Rate of Return (IRR).

### 4. Present the Results
Format the findings clearly for the user:
- Present a markdown table of the monthly cash flows if requested.
- State the absolute metrics (Total Inflow, Required Funding, Payback Period).
- Highlight the relative efficiency metrics (IRR, NPV, Return Multiple).
- Provide commentary explaining whether the project exceeds generic IRR benchmarks (e.g. >13%).
