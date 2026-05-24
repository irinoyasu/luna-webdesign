# ROI concepts and components

Reference for calculating Return on Investment based on standard financial modeling and the included presentation methodology.

## Component Breakdown

### 1. Cash Outflow (Investment & Costs)
- **Investing Cash Outflow**: Hardware/software installation costs, system development expenses (internal labor + outsourcing), real estate, M&A shares.
- **Operating Cash Outflow**: SG&A, travel, daily consumables, salaries post-launch. Includes allocation of overhead and full-time equivalent personnel cost.
- **Financing Cash Outflow**: Loan repayments (rare for standard business projects).

### 2. Cash Inflow (Returns & Savings)
- **Operating Cash Inflow**: Incremental sales growth or direct revenue from project.
- **Cost Savings**: Reduction in working hours × number of people × hourly rate (e.g., reduction of prototypes, less design man-hours). Treat as inflow.
- **Investing Cash Inflow**: Sale of assets, return of deposits.
- **Financing Cash Inflow**: Usually zero unless raising capital.

### 3. Key Cash Flow Metrics
- **Total Cash Flow**: `Cash Inflow - Cash Outflow` per month.
- **Cumulative Cash Flow**: Running total of the monthly cash flows.
- **Required Funding**: The minimum visible value in the Cumulative Cash Flow line.
- **Timing of Min Cumulative Cash Flow**: The month in which required funding reaches its lowest absolute negative value (often corresponds to the start of monthly profit).
- **Payback Period**: The month when the Cumulative Cash Flow returns to zero and becomes positive.
- **Return Multiple**: `Total Cash Inflow / Total Cash Outflow`.

## 4. Advanced ROI Metrics

### Internal Rate of Return (IRR)
- The discount rate at which the Net Present Value (NPV) of a project is exactly zero.
- It is an indicator of investment efficiency (a kind of interest rate).
- **Benchmarks**: 
  - Over 13.27% is often required for standard large companies (Hurdle Rate).
  - 30%+ for new business risk, 52%+ for startup series investments.

### Discount Rate & Cost of Capital
- Used to translate future money into present value terms. Evaluates the risk and time value of money.
- **WACC (Weighted Average Cost of Capital)** = Cost of Debt (weighted) + Cost of Equity (weighted). Serves as the standard generic Discount Rate.
- **Cost of Debt** = `[Debt / (Debt + Equity)] × Interest Rate × (1 - Tax Rate)`
- **Cost of Equity** = `Risk-Free Rate + (Market Risk Premium × Levered Beta) + Size Risk + Illiquidity Risk + New Business Risk`
- Example inputs for WACC: Tax rate (~34.7%), Risk free rate (0.25%), Market Premium (6%), Levered Beta (0.6).

## Metric vs Yield
- Unlike general "yield", IRR accounts for time value of money, uneven cashflows across periods, and evaluates the entire project period instead of a single year.
