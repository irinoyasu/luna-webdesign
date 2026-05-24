# Financials Phase Reference

## Overview

The financials phase is the most comprehensive phase, covering financial projections, valuation, and fundraising. This skill uses structured JSON files as the primary target for all financial data entry and output, following standard accounting principles and startup valuation methodologies.

**Process Dependencies:**
- **Phases 1-12 (Mandatory):** GTM, Operations, Team, and Business Model are direct inputs for revenue, costs, and personnel drivers.
- **Phase 14: Insight (Mandatory):** "Why Now" and "Contrarian Hypothesis" drive the growth assumptions.

**You MUST synthesize information from ALL previously completed phases before drafting.** 
The business plan is a cumulative pipeline. 

**CRITICAL RULES & GLOBAL CONSTRAINTS:**
1. **10-Year Duration:** EVERY monthly financial statement (P&L, Balance Sheet, Cash Flow, etc.) MUST contain 120 months (10 years) of data. EVERY annual summary must contain 10 years of data. A projection shorter than 10 years is a failure.
2. **Atomic JSON Output:** Every numbered sub-task (002-288) MUST result in a dedicated JSON file output. Partial or batched outputs are failures.
3. **Zero Placeholders:** THE USE OF 'PLACEHOLDER' TEXT, GENERIC STRINGS, OR EMPTY STRUCTURES IS STRICTLY PROHIBITED. Each file must contain specific, calculated, or benchmarked data relevant to the business context.
4. **Task Integrity:** Each file must follow its specific 'Detailed Sub-Task Instructions' without deviation.
5. **Mathematical Traceability:** Values must be mathematically consistent across the entire 120-month pipeline (e.g., Net Profit in P&L must match the B/S Retained Earnings increase).
6. **Bilingual Requirement:** ALL labels, descriptions, and notes must be provided in both Japanese and English. In Google Sheets outputs (Task 23), **Column E** is reserved for English labels and **Column F** for Japanese labels.
7. **Vagueness Audit (CFO Mode):** If a strategy document uses qualitative terms (e.g., "high profit," "efficient distribution," "proportional growth") as a source for a financial assumption, you MUST challenge the input. You are prohibited from using "Placeholder" or "Assumed" values. Instead, you MUST propose a specific, benchmarked numeric value (e.g., "Industry standard for transit DOOH is 43% GM") and request user confirmation before generating the JSON.
8. **Immediate Sheet Population (Tasks 1-6):** Every sub-task under Tasks 1, 2, 3, 4, 5, and 6 MUST immediately populate its designated row in the master Google Sheet (initialized in Task 0) using the `google-sheets` skill upon successful JSON generation. The JSON file serves as the audit trail, while the spreadsheet row serves as the operational model.

**SUCCESS CRITERIA:**
- **Google Sheet Consistency:** The final output of the "Generate Google Sheets" sub-tasks must generate exactly the same Google Sheet as the following Google Sheet range (https://docs.google.com/spreadsheets/d/1RRy1ssmt71gn3zY6cvztFxIjevQ0B4aJLH8WdamMWDo/edit?gid=295174920#gid=295174920&range=1:262).

**MANDATORY NAMING & METADATA CONVENTION:**
1. **Exact File Naming:** The output file name for each sub-task is FIXED. It MUST exactly match the value shown in the `Target File` column of the Sub-Task Index table below (e.g., `030-directors-bonuses.json`).
2. **Explicit Label Matching:** The `label_en` and `label_ja` fields in each JSON file MUST match the specific account name or item name provided in the detailed instructions, NOT a generic category name.
3. **No Dynamic Patterns:** DO NOT invent file names or use patterns like `NNN-sga-item-NN.json`. If your output file name does not exactly match the index, it is a FAILURE.

## Human-Readable JSON Standards

To ensure that the outputs are easy to understand for humans, adhere to the following formatting and structural rules:

1. **Pretty Printing:** Always use 2-space indentation for JSON outputs.
2. **Descriptive Keys:** Use clear, self-explanatory snake_case keys (e.g., `monthly_rent_amount` instead of `m_rent`).
3. **Labels & Metadata:** Include `label_ja` and `label_en` fields for financial line items.
4. **Narrative Notes:** Every significant entry or calculation should include a `description` or `notes` field explaining the logic or source.
5. **Logical Grouping:** Use nested objects to group related data (e.g., grouping `headcount` and `salary` under an employee object).
6. **Currency Clarity:** Specify the currency in a top-level `metadata` object or within the key names (e.g., `amount_jpy`).

## Mandatory JSON Output Template

Every sub-task involving monthly series or valuation (P&L, B/S, C/F, Valuation, Funding Needs) MUST follow this structure. Do NOT deviate.

```json
{
  "metadata": {
    "sub_task_number": "029",
    "label_en": "Directors' compensation",
    "label_ja": "役員報酬",
    "currency": "JPY",
    "driver": "Headcount × Annual Compensation / 12",
    "source_sub_tasks": ["004"],
    "notes": "CEO compensation starts at ¥600,001/month from M1. CTO joins at M7 at ¥500,001/month."
  },
  "monthly_values": [
    600000, 600000, 600000, 600000, 600000, 600000,
    1100000, 1100000, 1100000, 1100000, 1100000, 1100000,
    "... 120 values total ..."
  ],
  "annual_values": [
    9800000, 13200000, "... 10 values total ..."
  ]
}
```

## General Principles

1. **JSON-First Data Entry:** All data must be structured in the designated JSON files in `{output_folder}/financials/`.
2. **Dynamic Formulas:** While results are stored in JSON, the logic must follow Excel-style dynamic relationships (e.g., Opening + Increase - Decrease = Ending).
3. **Bilingual Consistency:** Use both Japanese and English labels for all financial line items from the standard **Chart of Accounts**.
4. **Driver-Based Modeling:**

### Task 0: Project Setup & Initialization
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 0-1 | Create Master Google Sheet File | Initialize automated spreadsheet. | `0-1-gs-master.json` |

### Task 1: Define Assumptions about P&L
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 1-1 | Define Assumptions about Revenue | Row 263 in "all" tab. | `1-1-assumptions-revenue.json` |
| 1-2 | Define Assumptions about Cost of Goods Sold | Row 264 in "all" tab. | `1-2-assumptions-cogs.json` |
| 1-3 | Define Assumptions about People costs | Row 265 in "all" tab. | `1-3-assumptions-people.json` |
| 1-4 | Define Assumptions about Rent and Overhead | Row 266 & 267 in "all" tab. | `1-4-assumptions-rent-overhead.json` |

### Task 2: Define Assumptions about Balance Sheet
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 2-1 | AR/DSO Assumptions | Row 268 in "all" tab. | `2-1-ar-assumptions.json` |
| 2-2 | Inventory/DIO Assumptions | Row 269 in "all" tab. | `2-2-inventory-assumptions.json` |
| 2-3 | AP/DPO Assumptions | Row 270 in "all" tab. | `2-3-ap-assumptions.json` |
| 2-4 | CAPEX Assumptions | Row 271 in "all" tab. | `2-4-capex-assumptions.json` |
| 2-5 | Depreciation Assumptions | Row 272 in "all" tab. | `2-5-depreciation-assumptions.json` |
| 2-6 | Tax Rate Assumptions | Row 273 in "all" tab. | `2-6-tax-assumptions.json` |

### Task 3: Define Assumptions about Cash Flow
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 3-1 | Debt Issuance Assumptions | Row 274 in "all" tab. | `3-1-debt-assumptions.json` |
| 3-2 | Equity Issuance Assumptions | Row 275 in "all" tab. | `3-2-equity-assumptions.json` |
| 3-3 | Interest Rate Assumptions | Row 276 in "all" tab. | `3-3-interest-assumptions.json` |
| 3-4 | Extraordinary Item Assumptions | Row 277 in "all" tab. | `3-4-extraordinary-assumptions.json` |

### Task 4: Generate Income Statement (Profit & Loss)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 4-1 | Revenue | Calculate monthly values based on drivers. | `4-1-revenue.json` |
| 4-2 | Sales returns | Calculate monthly based on return rate. | `4-2-sales-returns.json` |
| 4-3 | Net sales | Derived: Revenue - Returns. | `4-3-net-sales.json` |
| 4-4 | Cost of purchased goods sold | Formula-based COGS component. | `4-4-cost-purchased-goods.json` |
| 4-5 | Cost of finished goods sold | Formula-based COGS component. | `4-5-cost-finished-goods.json` |
| 4-6 | Cost of Goods Sold | Total COGS (Merchandise + Finished Goods). | `4-6-cost-of-goods-sold.json` |
| 4-7 | Beginning inventory (Merchandise) | Row 9 in "all" tab. | `4-7-beginning-inventory-merchandise.json` |
| 4-8 | Purchases of merchandise | Row 11 in "all" tab. | `4-8-purchases-merchandise.json` |
| 4-9 | Transfer to other account (Merchandise) | Row 12 in "all" tab. | `4-9-transfer-account-merchandise.json` |
| 4-10 | Ending inventory (Merchandise) | Row 13 in "all" tab. | `4-10-ending-inventory-merchandise.json` |
| 4-11 | Beginning inventory (Finished Goods) | Row 16 in "all" tab. | `4-11-beginning-inventory-fg.json` |
| 4-12 | Cost of finished goods manufactured | Row 17 in "all" tab. | `4-12-cost-fg-manufactured.json` |
| 4-13 | Transfer to other account (Finished Goods) | Row 18 in "all" tab. | `4-13-transfer-account-fg.json` |
| 4-14 | Ending inventory (Finished Goods) | Row 19 in "all" tab. | `4-14-ending-inventory-fg.json` |
| 4-15 | Gross profit | Derived: Net Sales - COGS. | `4-15-gross-profit.json` |
| 4-16 | Directors’ compensation | Monthly based on Comp plan. | `4-16-directors-compensation.json` |
| 4-17 | Directors’ bonuses | Performance-based bonuses. | `4-17-directors-bonuses.json` |
| 4-18 | Salaries | Monthly staff payroll. | `4-18-salaries.json` |
| 4-19 | Bonuses | Staff seasonal/performance bonuses. | `4-19-bonuses.json` |
| 4-20 | Share-based compensation expense | ESOP vesting amortization. | `4-20-share-based-compensation.json` |
| 4-21 | Legal welfare expense | ~15.5% of payroll (Japan). | `4-21-legal-welfare-expense.json` |
| 4-22 | Welfare expense | Extra-legal benefits. | `4-22-welfare-expense.json` |
| 4-23 | Recruiting expense | Cost-per-hire × headcount. | `4-23-recruiting-expense.json` |
| 4-24 | Training expense | HC-driven training costs. | `4-24-training-expense.json` |
| 4-25 | Subcontract expense | Third-party service costs. | `4-25-subcontract-expense.json` |
| 4-26 | Freightage expense | Shipping and logistics. | `4-26-freightage-expense.json` |
| 4-27 | Advertising expense | Marketing CAC spend. | `4-27-advertising-expense.json` |
| 4-28 | Entertainment expense | Sales-related entertainment. | `4-28-entertainment-expense.json` |
| 4-29 | Conference expenses | Meeting and conference costs. | `4-29-conference-expenses.json` |
| 4-30 | Traveling expense | Travel based on sales HC. | `4-30-traveling-expense.json` |
| 4-31 | Communication expense | IT, phone, and messaging. | `4-31-communication-expense.json` |
| 4-32 | Sales commission | Revenue-based commission. | `4-32-sales-commission.json` |
| 4-33 | Supplies expense | Consumable costs. | `4-33-supplies-expense.json` |
| 4-34 | Stationery expense | Office supply costs. | `4-34-stationery-expense.json` |
| 4-35 | Repair and maintenance expense | Asset maintenance. | `4-35-repair-maintenance.json` |
| 4-36 | Utilities expense | Office power and water. | `4-36-utilities-expense.json` |
| 4-37 | Books and subscription expense | Subscriptions and research. | `4-37-books-subscriptions.json` |
| 4-38 | Membership fee | Dues and memberships. | `4-38-membership-fees.json` |
| 4-39 | Printing and binding fee | Marketing materials printing. | `4-39-printing-binding.json` |
| 4-40 | Commission fee | Misc third-party fees. | `4-40-commission-fees.json` |
| 4-41 | Rent expenses on real estates | Office lease payments. | `4-41-rent-real-estate.json` |
| 4-42 | Rent expense | Equipment or misc rent. | `4-42-rent-expense.json` |
| 4-43 | Insurance expense | Corporate insurance premiums. | `4-43-insurance-expense.json` |
| 4-44 | Sundry taxes | Non-income taxes and fees (租税公課). | `4-44-sundry-taxes.json` |
| 4-45 | Professional fees | Legal and accounting retainer. | `4-45-professional-fees.json` |
| 4-46 | Donations expense | Charitable contributions. | `4-46-donations-expense.json` |
| 4-47 | Patent royalties | Intellectual property royalties. | `4-47-patent-royalties.json` |
| 4-48 | Miscellaneous expense | Other SG&A costs. | `4-48-miscellaneous-expense.json` |
| 4-49 | Research and development expense | R&D spending per plan. | `4-49-rd-expense.json` |
| 4-50 | Provision of allowance for doubtful accounts | Provision for bad debt. | `4-50-bad-debt-provision.json` |
| 4-51 | Depreciation expense | Non-current asset depreciation. | `4-51-depreciation-expense.json` |
| 4-52 | Amortization of deferred assets | Deferred asset write-downs. | `4-52-amortization-deferred.json` |
| 4-53 | Total of operating expenses | Derived: Sum of all SG&A items. | `4-53-operating-expenses-total.json` |
| 4-54 | Operating income | Derived: Gross Profit - SG&A Total. | `4-54-operating-income.json` |
| 4-55 | Interest income | Interest on cash reserves. | `4-55-interest-income.json` |
| 4-56 | Interest expense | Interest on debt obligations. | `4-56-interest-expense.json` |
| 4-57 | Dividend income | Income from investments. | `4-57-dividend-income.json` |
| 4-58 | Subsidy income | Government grants or subsidies. | `4-58-subsidy-income.json` |
| 4-59 | Miscellaneous income (Non-Op) | Other non-operating gains. | `4-59-misc-income.json` |
| 4-60 | Commission fee (Non-Op) | Non-operating commission costs. | `4-60-commission-non-op.json` |
| 4-61 | Miscellaneous loss (Non-Op) | Other non-operating losses. | `4-61-misc-loss.json` |
| 4-62 | Ordinary income | Derived: Operating ± Non-Op. | `4-62-ordinary-income.json` |
| 4-63 | Reversal of allowance for doubtful accounts | Extraordinary income item. | `4-63-reversal-bad-debt.json` |
| 4-64 | Loss on retirement of non-current assets | Extraordinary loss item. | `4-64-loss-retirement-assets.json` |
| 4-65 | Profit (or loss) before income taxes | Derived: Ordinary ± Extraordinary. | `4-65-pbt.json` |
| 4-66 | Income taxes - current | Row 75 in "all" tab. | `4-66-income-taxes-current.json` |
| 4-67 | Income taxes - deferred | Row 76 in "all" tab. | `4-67-income-taxes-deferred.json` |
| 4-68 | Net profit (or loss) | Final Net Profit for 120 months. | `4-68-net-profit.json` |
| 4-69 | Consolidate P&L data | Master JSON for P&L. | `4-69-pnl-grid.json` |

### Task 5: Generate Balance Sheet (BS)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 5-1 | Cash and deposits (BS) | Closing Monthly cash balance as a plug. | `5-1-cash-bs.json` |
| 5-2 | Cash (Deposit branch 1) | Balance of first bank account. | `5-2-cash-account-1.json` |
| 5-3 | Cash (Deposit branch 2) | Balance of second bank account. | `5-3-cash-account-2.json` |
| 5-4 | Cash (Deposit branch 3) | Balance of third bank account. | `5-4-cash-account-3.json` |
| 5-8 | Trade accounts receivable | AR based on Rev/DSO. | `5-8-trade-ar.json` |
| 5-9 | Allowance for doubtful accounts | Contra-asset for collections risk. | `5-9-bad-debt-allowance.json` |
| 5-10 | Merchandise | Inventory of purchased goods. | `5-10-merchandise.json` |
| 5-11 | Supplies | Office and operating supplies. | `5-11-supplies.json` |
| 5-12 | Work in process | Partially completed products. | `5-12-wip.json` |
| 5-13 | Finished goods | Completed products for sale. | `5-13-finished-goods.json` |
| 5-14 | Advance payments – trade | Prepays to vendors. | `5-14-advance-payments-trade.json` |
| 5-15 | Advance payments – other | Non-trade prepays. | `5-15-advance-payments-other.json` |
| 5-16 | Accounts receivable-other (Tatekaekin) | Employee/Director advances. | `5-16-ar-other-tatekaekin.json` |
| 5-17 | Prepaid expense | Monthly amortizable prepays. | `5-17-prepaid-expense.json` |
| 5-18 | Accrued revenue | Earned but unbilled revenue. | `5-18-accrued-revenue.json` |
| 5-19 | Loans receivable | Loans granted to third parties. | `5-19-loans-receivable.json` |
| 5-20 | Loans receivable from directors | Loans to company leadership. | `5-20-loans-receivable-directors.json` |
| 5-21 | Accounts receivable-other (Mishuunyuukin) | Non-trade receivables. | `5-21-ar-other-mishuunyuukin.json` |
| 5-22 | Temporary payment | Suspense/Unclassified payments. | `5-22-temporary-payment.json` |
| 5-23 | Suspense consumption tax | Interim consumption tax tracking. | `5-23-suspense-cons-tax.json` |
| 5-24 | Short-term loans receivable | Current portion of loans. | `5-24-short-term-loans-rec.json` |
| 5-25 | Other current assets | Misc current items. | `5-25-other-current-assets.json` |
| 5-26 | Facilities attached to buildings | Building improvements. | `5-26-facilities.json` |
| 5-27 | Tools, furniture and fixtures | Office and tech equipment. | `5-27-tools-furniture.json` |
| 5-28 | Software | Capitalized internal software. | `5-28-software.json` |
| 5-29 | Patents | Capitalized patent costs. | `5-29-patents.json` |
| 5-30 | Other non-current asset | Misc fixed assets. | `5-30-other-non-current.json` |
| 5-31 | Start-up costs | Row 124 in "all" tab. | `5-31-startup-costs.json` |
| 5-32 | Development expenses | Row 126 in "all" tab. | `5-32-development-expenses.json` |
| 5-33 | Bond issuance cost | Row 127 in "all" tab. | `5-33-bond-issuance-cost.json` |
| 5-34 | Security deposit | Row 118 in "all" tab. | `5-34-security-deposit.json` |
| 5-35 | Guarantee deposit | Row 119 in "all" tab. | `5-35-guarantee-deposit.json` |
| 5-36 | Investments in capital | Row 120 in "all" tab. | `5-36-investments-capital.json` |
| 5-37 | Deferred assets | Row 123 (Header) in "all" tab. | `5-37-deferred-assets.json` |
| 5-38 | Total Assets | Sum of all asset categories. | `5-38-total-assets.json` |
| 5-39 | Trade accounts payable | AP based on COGS/DPO. | `5-39-trade-ap.json` |
| 5-40 | Short-term loans payable | Current bank loans. | `5-40-short-term-loans-pay.json` |
| 5-41 | Current portion of long-term debt | Long-term debt due <12mo. | `5-41-current-portion-lt-debt.json` |
| 5-42 | Accounts payable - other | Row 136 in "all" tab. | `5-42-ap-other.json` |
| 5-43 | Accrued expenses | Monthly service accruals. | `5-43-accrued-expenses.json` |
| 5-44 | Accrued expenses(Card1) | Corporate card accruals. | `5-44-accrued-expenses-card1.json` |
| 5-45 | Income tax payable | Corporate tax liability. | `5-45-income-tax-payable.json` |
| 5-46 | Consumption tax payable | Net consumption tax liability. | `5-46-cons-tax-payable.json` |
| 5-47 | Advance received | Unearned revenue deposits. | `5-47-advance-received.json` |
| 5-48 | Withholdings | Payroll tax withholdings. | `5-48-withholdings.json` |
| 5-49 | Suspense payments | Unclassified bank payments. | `5-49-suspense-payments.json` |
| 5-50 | Suspense received Accrued consumption tax | Liability: Interim tax collection (仮受消費税). | `5-50-suspense-cons-tax.json` |
| 5-51 | Loans payable to directors | Debt owed to leadership. | `5-51-loans-pay-directors.json` |
| 5-52 | Long-term debt | Multi-year bank debt. | `5-52-long-term-debt.json` |
| 5-53 | Capital stock | Paid-in capital from rounds. | `5-53-capital-stock.json` |
| 5-54 | Capital reserve | Surplus capital from rounds. | `5-54-capital-reserve.json` |
| 5-55 | Retained earnings | Accumulated net income/loss. | `5-55-retained-earnings.json` |
| 5-56 | Total Equity | Sum of all equity components. | `5-56-total-equity.json` |
| 5-57 | Consolidate Balance Sheet data | Master JSON for BS. | `5-57-bs-grid.json` |
| 5-58 | Suspense taxes | Asset: Interim tax payments (仮払税金). | `5-58-suspense-taxes.json` |
| 5-59 | Accrued consumption tax | Asset: Receivable tax (未収消費税). | `5-59-accrued-cons-tax-asset.json` |
| 5-60 | Accumulated depreciation | Contra-Asset: Total depreciation to date. | `5-60-accumulated-depreciation.json` |
| 5-61 | Share issuance cost | Deferred Asset: Amortizable equity fees. | `5-61-share-issuance-cost.json` |
| 5-62 | Other capital surplus | Equity: Non-reserve surplus. | `5-62-other-capital-surplus.json` |
| 5-63 | Reserve for advanced depreciation of non-current assets | Equity: Tax-deferral reserves. | `5-63-reserve-advanced-depreciation.json` |
| 5-64 | Valuation and translation adjustments | Equity: Unrealized gains/losses. | `5-64-valuation-adjustments.json` |
| 5-65 | Share acquisition rights | Equity: Options and warrants. | `5-65-share-acquisition-rights.json` |
| 5-66 | Other retained earnings | Equity: Misc accumulated earnings. | `5-66-other-retained-earnings.json` |

### Task 6: Generate Cash Flow Statement (CF)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 6-1 | Starting Net Profit for Cash Flow | Base for indirect method. | `6-1-net-profit-cf.json` |
| 6-2 | Adjustment for Income Taxes | Add back non-cash tax accruals. | `6-2-adj-income-taxes.json` |
| 6-3 | Adjustment for Depreciation & Amortization | Add back non-cash D&A. | `6-3-adj-depreciation.json` |
| 6-4 | Adjustment for Amortization of Deferred Assets | Add back non-cash amortization. | `6-4-adj-amortization-deferred.json` |
| 6-5 | Adjustment for Provision of Allowance | Add back bad debt provisions. | `6-5-adj-provision-bad-debt.json` |
| 6-6 | Adjustment for Interest Expense | Netting interest impact. | `6-6-adj-interest-expense.json` |
| 6-7 | Adjustment for Interest Income | Netting interest impact. | `6-7-adj-interest-income.json` |
| 6-8 | Adjustment for Miscellaneous Income | Removing non-cash income. | `6-8-adj-miscellaneous-income.json` |
| 6-9 | Adjustment for Subsidy Income | Removing non-cash subsidies. | `6-9-adj-subsidy-income.json` |
| 6-10 | Adjustment for Reversal of Allowance | Subtracting non-cash reversals. | `6-10-adj-reversal-bad-debt.json` |
| 6-11 | Adjustment for Loss on Retirement | Adding back disposal losses. | `6-11-adj-loss-retirement.json` |
| 6-12 | Change in AR | Row 190 in "all" tab. | `6-12-inc-trade-ar.json` |
| 6-13 | Change in Merchandise | Row 191 in "all" tab. | `6-13-inc-merchandise.json` |
| 6-14 | Change in Supplies | Row 192 in "all" tab. | `6-14-inc-supplies.json` |
| 6-15 | Change in Work in process | Row 193 in "all" tab. | `6-15-inc-wip.json` |
| 6-16 | Change in Finished goods | Row 194 in "all" tab. | `6-16-inc-finished-goods.json` |
| 6-17 | Change in AP | Row 195 in "all" tab. | `6-17-inc-trade-ap.json` |
| 6-18 | Change in Suspense taxes | Row 196 in "all" tab. | `6-18-inc-suspense-taxes.json` |
| 6-19 | Change in Advance payments – trade | Row 197 in "all" tab. | `6-19-inc-advance-trade.json` |
| 6-20 | Change in Advance payments – other | Row 198 in "all" tab. | `6-20-inc-advance-other.json` |
| 6-21 | Change in Accrued consumption tax | Row 199 in "all" tab. | `6-21-inc-accrued-cons-tax.json` |
| 6-22 | Change in AR-other (Tatekaekin) | Row 200 in "all" tab. | `6-22-inc-ar-other-tatekaekin.json` |
| 6-23 | Change in Prepaid expense | Row 201 in "all" tab. | `6-23-inc-prepaid-expense.json` |
| 6-24 | Change in Accrued revenue | Row 202 in "all" tab. | `6-24-inc-accrued-revenue.json` |
| 6-25 | Change in Loans receivable | Row 203 in "all" tab. | `6-25-inc-loans-receivable.json` |
| 6-26 | Change in Loans receivable (Director) | Row 204 in "all" tab. | `6-26-inc-loans-director.json` |
| 6-27 | Change in AR-other (Mishuunyuukin) | Row 205 in "all" tab. | `6-27-inc-ar-other-mishuunyuukin.json` |
| 6-28 | Change in Temporary payment | Row 207 in "all" tab. | `6-28-inc-temp-payment.json` |
| 6-29 | Change in Suspense consumption tax | Row 208 in "all" tab. | `6-29-inc-suspense-cons-tax.json` |
| 6-30 | Change in Loans payable to directors | Row 209 in "all" tab. | `6-30-inc-loans-pay-director.json` |
| 6-31 | Change in AP-other | Row 210 in "all" tab. | `6-31-inc-ap-other.json` |
| 6-32 | Change in Accrued expenses | Row 211 in "all" tab. | `6-32-inc-accrued-expenses.json` |
| 6-33 | Change in Accrued expenses(Card1) | Row 212 in "all" tab. | `6-33-inc-accrued-expenses-card1.json` |
| 6-34 | Change in Income tax payable | Row 213 in "all" tab. | `6-34-inc-income-tax-pay.json` |
| 6-35 | Change in Consumption tax payable | Row 214 in "all" tab. | `6-35-inc-cons-tax-pay.json` |
| 6-36 | Change in Advance received | Row 215 in "all" tab. | `6-36-inc-advance-received.json` |
| 6-37 | Change in Withholdings | Row 216 in "all" tab. | `6-37-inc-withholdings.json` |
| 6-38 | Change in Suspense payments | Row 217 in "all" tab. | `6-38-inc-suspense-payments.json` |
| 6-39 | Change in Suspense received | Row 218 in "all" tab. | `6-39-inc-suspense-rec-cons-tax.json` |
| 6-40 | Interest Expense Paid | Actual monthly cash outflow. | `6-40-interest-expense-paid.json` |
| 6-41 | Subsidy Income Received | Actual monthly cash inflow. | `6-41-subsidy-income-received.json` |
| 6-42 | Interest Income Received | Actual monthly cash inflow. | `6-42-interest-income-received.json` |
| 6-43 | Miscellaneous Income Received | Actual monthly cash inflow. | `6-43-miscellaneous-income-received.json` |
| 6-44 | Capex: Facilities attached to buildings | Row 230 in "all" tab. | `6-44-inc-facilities.json` |
| 6-45 | Capex: Tools and Tech | Row 231 in "all" tab. | `6-45-inc-tools.json` |
| 6-46 | Capex: Software | Row 232 in "all" tab. | `6-46-inc-software.json` |
| 6-47 | Capex: Patents | Row 233 in "all" tab. | `6-47-inc-patents.json` |
| 6-48 | Capex: Other non-current asset | Row 234 in "all" tab. | `6-48-inc-other-non-current.json` |
| 6-49 | Startup: Start-up costs | (Part of Investing Outflow subtotal). | `6-49-inc-startup-costs.json` |
| 6-50 | Startup: Development expenses | (Part of Investing Outflow subtotal). | `6-50-inc-development-expenses.json` |
| 6-51 | Startup: Security deposit | Row 235 in "all" tab. | `6-51-inc-security-deposit.json` |
| 6-52 | Startup: Guarantee deposit | Row 236 in "all" tab. | `6-52-inc-guarantee-deposit.json` |
| 6-53 | Investing: Capital Investments | Row 237 in "all" tab. | `6-53-inc-investments-capital.json` |
| 6-54 | Financing: Capital stock | Row 243 in "all" tab. | `6-54-inc-capital-stock.json` |
| 6-55 | Financing: Capital reserve | Row 244 in "all" tab. | `6-55-inc-capital-reserve.json` |
| 6-56 | Financing: Long-term debt | Row 245 in "all" tab. | `6-56-inc-long-term-debt.json` |
| 6-57 | Financing: Debt current maturities | Row 252 in "all" tab (Repayment). | `6-57-inc-lt-debt-current.json` |
| 6-58 | Financing: Short-term loans | Inflow from current lines. | `6-58-inc-short-term-loans.json` |
| 6-59 | Financing: Repay Long-term debt | Scheduled principal outflow. | `6-59-dec-long-term-debt.json` |
| 6-60 | Financing: Share issuance cost | Row 250 in "all" tab. | `6-60-inc-share-issuance-cost.json` |
| 6-61 | Effect of Exchange Rate Changes | Non-cash FX adjustments. | `6-61-effect-exchange-rate.json` |
| 6-62 | (Reserved) | Placeholder for summary aggregation. | `6-62-reserved.json` |
| 6-63 | Net Change in Cash | Sum of all activities by month. | `6-63-net-change-cash.json` |
| 6-64 | Consolidate Cash Flow data | Master JSON for CF. | `6-64-cf-grid.json` |
| 6-65 | Operating Cash flow (Before Changes in NWC) | Sub-total: Profit + Non-cash adjustments. | `6-65-ocf-pre-nwc.json` |
| 6-66 | Changes in Net Working Capital (Summary) | Sub-total: Move in Current Assets/Liabilities. | `6-66-nwc-change-summary.json` |
| 6-67 | Beginning cash position | Carry-forward from prior period end. | `6-67-beginning-cash.json` |
| 6-68 | End cash position | Final reconciled cash at period end. | `6-68-end-cash.json` |

### Task 7: Calculate Ratios
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 7-1 | Calculate Profitability Ratios | ROE, ROA, Gross Margin, Operating Margin, Net Margin. | `7-1-profitability-ratios.json` |
| 7-2 | Calculate Liquidity Ratios | Current Ratio, Quick Ratio, Cash Ratio. | `7-2-liquidity-ratios.json` |
| 7-3 | Calculate Leverage Ratios | Debt-to-Equity, Interest Coverage, Debt Service Coverage. | `7-3-leverage-ratios.json` |
| 7-4 | Calculate Efficiency Ratios | Asset Turnover, Inventory Turnover, Receivables Turnover. | `7-4-efficiency-ratios.json` |
| 7-5 | Calculate Valuation Ratios | P/E, P/B, P/S, EV/EBITDA, PEG. | `7-5-valuation-ratios.json` |
| 7-6 | Calculate Per-Share Metrics | EPS, Book Value per Share, Dividend per Share. | `7-6-per-share-metrics.json` |

### Task 8: Calculate Cost of Capital & Discount Rate
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 8-1 | Calculate Risk Free Rate | Identify the risk-free rate based on long-term government bond yields. | `8-1-risk-free-rate.json` |
| 8-2 | Calculate Market Risk Premium | Determine the expected return of the market over the risk-free rate. | `8-2-market-risk-premium.json` |
| 8-3 | Calculate Levered Beta (Equity Beta) | Determine the levered beta for the company based on peer comparisons. | `8-3-levered-beta.json` |
| 8-4 | Calculate Unlevered Beta (Asset Beta) | Remove the effect of leverage to find the pure business risk beta. | `8-4-unlevered-beta.json` |
| 8-5 | Calculate Equity Risk Premium | Apply Beta to the Market Risk Premium to find the specific equity risk. | `8-5-equity-risk-premium.json` |
| 8-6 | Calculate Size Risk Premium | Determine the additional risk premium for small-cap companies. | `8-6-size-risk-premium.json` |
| 8-7 | Calculate Illiquidity Risk Premium | Determine the premium for private or illiquid assets. | `8-7-illiquidity-risk-premium.json` |
| 8-8 | Calculate New Business Risk Premium | Determine the premium for startup or new business uncertainty. | `8-8-new-business-risk-premium.json` |
| 8-9 | Calculate Cost of Equity | Sum the risk-free rate and all relevant risk premiums. | `8-9-cost-of-equity.json` |
| 8-10 | Calculate Cost of Debt | Determine the after-tax cost of borrowing for the company. | `8-10-cost-of-debt.json` |
| 8-11 | Define Capital Structure | Determine the target weight of debt and equity for the company's optimal capital structure. | `8-11-capital-structure.json` |
| 8-12 | Calculate Weighted Average Cost of Capital (WACC) | Calculate the overall WACC based on capital structure weights. | `8-12-wacc.json` |
| 8-13 | Define Hurdle Rate Multiple between WACC and Discount Rate | Calculate the ratio of the required equity return to the weighted average cost of capital. | `8-13-wacc-discount-rate-multiple.json` |
| 8-14 | Calculate Discount Rate | Finalize the monthly discount rate applied to cash flows. | `8-14-discount-rate.json` |

### Task 9: Perform Valuation (DCF)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 9-1 | Calculate Free Cash Flow | Derive Free Cash Flow by analyzing the Operating and Investing cash flow lines. | `9-1-free-cash-flow.json` |
| 9-2 | Calculate Monthly Discount Rate | Calculate the 120-month monthly discount rate series based on the annual WACC. | `9-2-dcf-discount-rate.json` |
| 9-3 | Calculate Discount Factors | Calculate the monthly discount factors based on the referenced discount rate. | `9-3-dcf-discount-factors.json` |
| 9-4 | Calculate Present Value of FCF | Apply discount factors to forecasted FCF to determine Net Present Value. | `9-4-dcf-pv-fcf.json` |
| 9-5 | Define Terminal Growth Rate (g) | Establish the expected long-term perpetual growth rate (g) for each month. | `9-5-dcf-terminal-growth-rate.json` |
| 9-6 | Calculate Terminal Value (TV) | Apply Perpetual Growth Rate and calculate Terminal Value at the projection exit. | `9-6-dcf-terminal-value.json` |
| 9-7 | Calculate Enterprise Value (EV) | Sum PV of FCF and PV of Terminal Value to derive Enterprise Value. | `9-7-dcf-enterprise-value.json` |
| 9-8 | Calculate Net Debt | Calculate total debt minus cash and cash equivalents. | `9-8-dcf-net-debt.json` |
| 9-9 | Calculate Minority Interest | Calculate the portion of subsidiaries owned by minority shareholders. | `9-9-dcf-minority-interest.json` |
| 9-10 | Calculate Preferred Equity | Calculate the value of preferred stock outstanding. | `9-10-dcf-preferred-equity.json` |
| 9-11 | Calculate Equity Method Investments | Calculate the value of investments in associates. | `9-11-dcf-equity-method-investments.json` |
| 9-12 | Calculate Enterprise to Equity Bridge | Bridge Enterprise Value to Equity Value with Net Debt and other claims. | `9-12-dcf-enterprise-to-equity-bridge.json` |
| 9-13 | Derive Equity Value | Finalize Equity Value deducting debt from Enterprise Value from the Bridge. | `9-13-dcf-equity-value.json` |
| 9-14 | Calculate Value Per Share | Calculate the per share equity value using diluted shares outstanding. | `9-14-dcf-value-per-share.json` |
| 9-15 | Perform Sensitivity Analysis | Generate scenario analysis (Bull/Base/Bear) and standard sensitivity tables. | `9-15-dcf-sensitivity-analysis.json` |

### Task 10: Perform Valuation (PER)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 10-1 | Select Benchmark PER Multiple | Identify the representative PER multiple based on comparable public companies. | `10-1-per-benchmark.json` |
| 10-2 | Calculate Diluted Shares Outstanding | Calculate the diluted shares outstanding factoring in options/warrants. | `10-2-per-diluted-shares.json` |
| 10-3 | Apply IPO Discount to PER Multiple | Define and apply an IPO discount (e.g., 70%) to adjust for private market illiquidity. | `10-3-per-ipo-discount.json` |
| 10-4 | Calculate Effective PER after Discount | Derive the final effective PER multiple after the IPO discount. | `10-4-per-effective-multiple.json` |
| 10-5 | Identify Net Profit for Valuation Base | Pull the relevant historical or forecasted net profit to be used as the valuation base. | `10-5-per-net-profit-base.json` |
| 10-6 | Derive Equity Value from PER | Multiply the effective PER by the net profit to calculate the implied Equity Value. | `10-6-per-equity-value.json` |
| 10-7 | Calculate Value Per Share | Calculate the per share equity value using diluted shares outstanding. | `10-7-per-value-per-share.json` |

### Task 11: Perform Valuation (PBR)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 11-1 | Select Benchmark PBR Multiple | Identify the representative PBR multiple based on comparable public companies. | `11-1-pbr-benchmark.json` |
| 11-2 | Apply IPO Discount to PBR Multiple | Define and apply an IPO discount (e.g., 70%) to adjust for valuation differences. | `11-2-pbr-ipo-discount.json` |
| 11-3 | Calculate Effective PBR after Discount | Derive the final effective PBR multiple after the IPO discount. | `11-3-pbr-effective-multiple.json` |
| 11-4 | Identify Total Net Assets for Valuation Base | Pull the company's total net assets (book value) to be used as the valuation base. | `11-4-pbr-net-assets-base.json` |
| 11-5 | Derive Equity Value from PBR | Multiply the effective PBR by the net assets to calculate the implied Equity Value. | `11-5-pbr-equity-value.json` |
| 11-6 | Calculate Value Per Share | Calculate the per share equity value using diluted shares outstanding. | `11-6-pbr-value-per-share.json` |

### Task 12: Perform Valuation (EV/EBITDA)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 12-1 | Select Benchmark EV/EBITDA Multiple | Identify the representative EBITDA multiple based on peer benchmarks. | `12-1-ev-ebitda-benchmark.json` |
| 12-2 | Apply IPO Discount to EV/EBITDA Multiple | Adjust for liquidity and size using an IPO discount. | `12-2-ev-ebitda-ipo-discount.json` |
| 12-3 | Calculate Effective EV/EBITDA | Final multiple after standard industry discounts. | `12-3-ev-ebitda-effective-multiple.json` |
| 12-4 | Identify EBITDA for Valuation Base | Forecasted EBITDA for calculation base. | `12-4-ev-ebitda-base.json` |
| 12-5 | Derive Enterprise Value from EV/EBITDA | Imply EV using specific EBITDA methodology. | `12-5-ev-ebitda-enterprise-value.json` |
| 12-6 | Calculate Net Debt | Calculate total debt minus cash and cash equivalents. | `12-6-ev-ebitda-net-debt.json` |
| 12-7 | Calculate Minority Interest | Calculate the portion of subsidiaries owned by minority shareholders. | `12-7-ev-ebitda-minority-interest.json` |
| 12-8 | Calculate Preferred Equity | Calculate the value of preferred stock outstanding. | `12-8-ev-ebitda-preferred-equity.json` |
| 12-9 | Calculate Equity Method Investments | Calculate the value of investments in associates. | `12-9-ev-ebitda-equity-method-investments.json` |
| 12-10 | Calculate Enterprise to Equity Bridge | Bridge Enterprise Value to Equity Value with Net Debt and other claims. | `12-10-ev-ebitda-enterprise-to-equity-bridge.json` |
| 12-11 | Derive Equity Value | Finalize Equity Value deducting debt from Enterprise Value from the Bridge. | `12-11-ev-ebitda-equity-value.json` |
| 12-12 | Calculate Value Per Share | Calculate the per share equity value using diluted shares outstanding. | `12-12-ev-ebitda-value-per-share.json` |

### Task 13: Perform Valuation (PSR)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 13-1 | Select Benchmark PSR Multiple | Identify the representative PSR multiple based on peers. | `13-1-psr-benchmark.json` |
| 13-2 | Apply IPO Discount to PSR Multiple | Adjust for liquidity. | `13-2-psr-ipo-discount.json` |
| 13-3 | Calculate Effective PSR | Final multiple after discounts. | `13-3-psr-effective-multiple.json` |
| 13-4 | Identify Revenue for Valuation Base | Company revenue pool for PSR. | `13-4-psr-revenue-base.json` |
| 13-5 | Derive Equity Value from PSR | Imply value using Revenue methodology. | `13-5-psr-equity-value.json` |
| 13-6 | Calculate Value Per Share | Final PSR-based share price. | `13-6-psr-value-per-share.json` |

### Task 14: Perform Valuation (PCFR)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 14-1 | Select Benchmark PCFR Multiple | Identify peer Cash Flow multiples. | `14-1-pcfr-benchmark.json` |
| 14-2 | Apply IPO Discount to PCFR Multiple | Adjust for liquidity. | `14-2-pcfr-ipo-discount.json` |
| 14-3 | Calculate Effective PCFR | Final multiple after discounts. | `14-3-pcfr-effective-multiple.json` |
| 14-4 | Identify OCF for Valuation Base | Operating Cash Flow base. | `14-4-pcfr-operating-cf-base.json` |
| 14-5 | Derive Equity Value from PCFR | Imply value using Cash Flow methodology. | `14-5-pcfr-equity-value.json` |
| 14-6 | Calculate Value Per Share | Final PCFR-based share price. | `14-6-pcfr-value-per-share.json` |

### Task 15: Perform Valuation (Comparable Company Method)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 15-1 | Select Peer Group | Identify similar public companies. | `15-1-cca-peer-group.json` |
| 15-2 | Calculate Trading Multiples | Peer EV/Revenue, EV/EBITDA, P/E. | `15-2-cca-trading-multiples.json` |
| 15-3 | Adjust for Premiums and Discounts | Apply private company discounts (15-30%). | `15-3-cca-adjustments.json` |
| 15-4 | Determine Appropriate Multiple Range | Set the multiple bracket for the target. | `15-4-cca-multiple-range.json` |
| 15-5 | Apply Multiples to Target Metrics | Apply the range to company stats. | `15-5-cca-apply-multiples.json` |
| 15-6 | Derive Equity Value from CCA | Final value utilizing the CCA method. | `15-6-cca-equity-value.json` |
| 15-7 | Calculate Value Per Share | Final CCA-based share price. | `15-7-cca-value-per-share.json` |

### Task 16: Perform Valuation (Comparable Transaction Method)
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 16-1 | Identify Comparable Transactions | Search recently similar M&A/funding deals. | `16-1-cta-comparable-transactions.json` |
| 16-2 | Gather Transaction Financial Data | Extract metrics for the selected deals. | `16-2-cta-transaction-financials.json` |
| 16-3 | Calculate Transaction Multiples | Compute multiples for comparable deals. | `16-3-cta-transaction-multiples.json` |
| 16-4 | Select Representative Multiple | Median/Average check for target application. | `16-4-cta-representative-multiple.json` |
| 16-5 | Apply Multiple to Target Financials | Multiply multiple by operating metrics. | `16-5-cta-apply-multiple.json` |
| 16-6 | Derive Equity Value from CTA | Final value utilizing the CTA method. | `16-6-cta-equity-value.json` |
| 16-7 | Calculate Value Per Share | Final CTA-based share price. | `16-7-cta-value-per-share.json` |

### Task 17: Summarize Valuation
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 17-1 | Compare Valuations | Cross-compare results from all methodologies. | `17-1-compare-valuations.json` |
| 17-2 | Calculate Pre-money Valuation | Valuation before new capital. | `17-2-pre-money-valuation.json` |
| 17-3 | Finalize Stock Price | Final determination of value and price per share. | `17-3-finalize-stock-price.json` |

### Task 18: Calculate Funding Needs
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 18-1 | Calculate Operating Working Capital | Calculate 経常運転資金. | `18-1-operating-working-capital.json` |
| 18-2 | Calculate Net Working Capital | Calculate 正味運転資本. | `18-2-net-working-capital.json` |
| 18-3 | Calculate Capital Expenditure @BS | Calculate 設備投資. | `18-3-capex-bs.json` |
| 18-4 | Calculate Development Expenses @BS | Calculate 開発費. | `18-4-development-expenses-bs.json` |
| 18-5 | Calculate Research and Development Expenses @PL | Calculate 研究開発費. | `18-5-rd-expenses-pl.json` |
| 18-6 | Calculate Lowest Accumulated FCF | Identify the max cash outflow point. | `18-6-lowest-accumulated-fcf.json` |
| 18-7 | Calculate Burn Rate | Determine the monthly cash consumption rate. | `18-7-burn-rate.json` |
| 18-8 | Calculate Runway Before Fundraising | Determine how many months cash will last. | `18-8-runway-before-fundraising.json` |
| 18-9 | Calculate Amount for Runway Tiers | Capital needed for 6/12/18/24m tiers. | `18-9-runway-tiers-needed.json` |

### Task 19: Plan Debt Financing from Japan Finance Corporation
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 19-1 | Plan bank for loan application | Identify institution and branch. | `19-1-loan-bank-plan.json` |
| 19-2 | Plan loan program | Select appropriate JFC menu. | `19-2-loan-program-plan.json` |
| 19-3 | Plan loan amount | Principal based on needs analysis. | `19-3-loan-amount-plan.json` |
| 19-4 | Plan interest rate | Based on current JFC benchmarks. | `19-4-loan-interest-rate-plan.json` |
| 19-5 | Plan repayment schedule | Principal schedule and grace periods. | `19-5-loan-repayment-plan.json` |

### Task 20: Plan Equity Financing
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 20-1 | Plan Multi-Stage Equity Roadmap | Timing, amount, valuation Pre-seed to IPO. | `20-1-funding-roadmap.json` |
| 20-2 | Define Deal Terms by Round | Vehicle and key terms for each round. | `20-2-equity-terms-by-round.json` |
| 20-3 | Map Investors and Syndicates | Targets per funding stage. | `20-3-investor-allocation.json` |
| 20-4 | Plan ESOP Expansion | Reserved blocks for milestones. | `20-4-esop-expansion-plan.json` |
| 20-5 | Calculate Cumulative Dilution | CAP table math round-to-round. | `20-5-multi-round-captable.json` |
| 20-6 | Generate Simple Captable Summary | Executive ownership summary. | `20-6-simple-captable-summary.json` |
| 20-7 | Reconcile Valuations | Confirm final pre/post valuation values. | `20-7-valuation-reconciliation.json` |
| 20-8 | Establish Strike Price Evolution | Exercise price estimate per stage. | `20-8-strike-price-evolution.json` |
| 20-9 | Write Term Sheet | Draft a professional term sheet based on best practices. | `20-9-term-sheet.json` |

### Task 21: Analyze Exit and Waterfall
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 21-1 | Define Exit Scenario and Valuation | Exit month and project Enterprise Value. | `21-1-exit-scenario.json` |
| 21-2 | Model Liquidation Preferences | Payout priority Common vs. Preferred. | `21-2-liquidation-preferences.json` |
| 21-3 | Calculate Exit Waterfall | simulation across stakeholder classes. | `21-3-exit-waterfall.json` |
| 21-4 | Calculate Investor ROI | MOIC and IRR for round participants. | `21-4-investor-roi.json` |
| 21-5 | Calculate Founder Realization | Final wealth realized by founders. | `21-5-founder-realization.json` |

### Task 22: Calculate PL, BS, CF after fundraising
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 22-1 | Calculate P&L after fundraising | Reflect interest and reserve impact. | `22-1-pl-post-fund.json` |
| 22-2 | Calculate Balance Sheet after fundraising | Reflect capital and debt liabilities. | `22-2-bs-post-fund.json` |
| 22-3 | Calculate Cash Flow after fundraising | Reflect financing and debt service. | `22-3-cf-post-fund.json` |
| 22-4 | Verify Financial Health | Audit for positive cash and buffer constraints. | `22-4-verify-financial-health.json` |

### Task 23: Generate Google Sheets
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 23-2 | Populate P&L Section | Rows 1-77 in "all" tab. | `23-2-gs-pnl-section.json` |
| 23-3 | Populate Balance Sheet Section | Rows 79-171 in "all" tab. | `23-3-gs-bs-section.json` |
| 23-4 | Populate Cash Flow Section | Rows 173-259 in "all" tab. | `23-4-gs-cf-section.json` |
| 23-5 | Populate Captable Tab | Detailed ownership population in "captable" tab. | `23-5-gs-captable.json` |
| 23-6 | Populate Captable Summary Tab | Summary view of ownership in "captable" tab. | `23-6-gs-captable-summary.json` |
| 23-7 | Populate Valuation Comparison Tab | Comparison of all methodologies in "valuation" tab. | `23-7-gs-valuation-comparison.json` |
| 23-8 | Populate Orders Tab | Detailed revenue driver data in "orders" tab. | `23-8-gs-orders.json` |

### Task 24: Finalize Financial Plan
| # | Sub-task Name | Description | Target File |
|---|---|---|---|
| 24-1 | Write Financial Story | Final narrative summary. | `24-1-write-financial-story.json` |


### Task 0: Project Setup & Initialization

#### Sub-task 0-1: Create Master Google Sheet File

**Description:** Create master spreadsheet and initialize tab structure.

**Output:**
- `0-1-gs-master.json`

**Detailed Steps:**
1. Use the `google-sheets` skill to create the master spreadsheet and initialize tabs: "all", "orders", "captable", "valuation".
2. **Bilingual Label Mandate:** 
    - **Column E:** English labels (e.g., "Net Profit").
    - **Column F:** Japanese labels (e.g., "当期純利益").
3. **Formula Engine Mandate:** The master spreadsheet MUST be initialized with the core 120-month timeline across Column G to Column DV (Month 1-120).
4. **Named Range Mandate (Bi-Directional Logic):** Every driver used in the calculations (e.g., Unit Price, CAC, Churn, Interest Rate) MUST be defined as a **Named Range** in the "Assumptions" or "all" tab. Resulting P&L and BS formulas MUST reference these Named Ranges rather than hardcoded values.

### Task 1: Define Assumptions about P&L

**Process Dependencies:**
- **Pre-Financial Phases:** Business Model, GTM, Team, and Operations.

#### Sub-task 1-1: Define Assumptions about Revenue

**Description:** Define key revenue assumptions. Corresponds to **Row 263** in the 'all' tab.

**Input:**
- `{output_folder}/businessplan-writing/businessmodel/`
- `{output_folder}/businessplan-writing/go-to-market/`
- `{output_folder}/businessplan-writing/strategy/`

**Dependencies:**
- **Product/Solution Phase:** Unit price, product specs, and release timing of product.
- **Go-To-Market Phase:** Sales volume, channel mix, and launch timing.
- **Business Model Phase:** Revenue streams (SaaS, Transactional, etc.).

**Output:**
- `1-1-assumptions-revenue.json` (Aggregate Metrics)
- `1-1-assumptions-revenue-orders.json` (Specific Orders)
- `1-1-revenue-growth.json` (MoM Growth)

**Proactive Benchmarking Policy (Logic Engine):**
- If the business plan is vague (e.g., "high growth," "dominant market share"), you are FORBIDDEN from asking the user for numbers. Instead, you MUST search for the **Target Market Average Growth Rate** or use the **YC Continuity Benchmark** (5-7% MoM for early stage).
- Propose a specific, month-by-month trajectory and request user confirmation.

**Detailed Steps:**

1. **Determine Revenue Methodology:** Evaluate available inputs and user instructions to select the most appropriate modeling branch.

    - **IF Approach 1: Specific Order List (Bottom-up/Detailed):**
        - Generate a 120-month list of customer orders. Each entry MUST include:
            - **Order ID**
            - **Customer name:** (Actual name for known customers, "Generalized Customer [Segment]" for others)
            - **Opportunity name:** (Specific problem/opportunity being addressed)
            - **Product/Service name**
            - **Price (Tax Excluded):** From Solution phase.
            - **Sales volume:** From GTM phase.
            - **Total Revenue:** Price * Sales volume
            - **Order Date**
        - **Target File:** `1-1-assumptions-revenue-orders.json`

    - **ELSE IF Approach 2: Aggregate Metrics (Top-down/Driver-based):**
        - Define the foundational drivers for each month of the 120-month projection:
            - **Unit Price:** Monthly price per unit or average monthly contract value (ACV).
            - **Sales Volume:** Monthly number of units or customers by channel (Organic, Paid, Outbound).
            - **Growth Rate:** Month-over-Month (MoM) growth percentages per segment.
            - **Churn/Retention:** For subscription models, define monthly churn rate and net revenue retention (NRR).
            - **Seasonality:** Monthly seasonal weighting factors (e.g., higher volume in Q4).
        - **Target File:** `1-1-assumptions-revenue.json`

    - **ELSE IF Approach 3: Revenue Growth (% Change) Month-over-Month (MoM):**
        - Define Month-over-Month (MoM) growth targets for each revenue stream or segment (e.g., 5% MoM growth for Year 1-2).
        - **Target File:** `1-1-revenue-growth.json`

2. **Assume 120-Month Continuity:** Regardless of the chosen approach, the data MUST be projected for exactly 120 months to ensure consistency with the master financial grid.

3. **Establish Metric Lock:** Define exactly how each metric is calculated to prevent definition "softening" during later execution phases.

4. **Logic Engine Check (Vagueness Audit):**
    - If the GTM or Strategy docs imply a "low" or "high" value without a number, the agent MUST perform a web search or use industry benchmarks (e.g., SaaS CAC Payback < 12 months) to populate the JSON with a defensible starting point.

5. Consolidate into json format. Monthly based for 120 months.
6. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 263) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 1-2: Define Assumptions about Cost of Goods Sold

**Description:** Define key COGS assumptions. Corresponds to **Row 264** in the 'all' tab.

**Input:**
- `{output_folder}/businessplan-writing/businessmodel/`
- `{output_folder}/businessplan-writing/go-to-market/`
- `{output_folder}/businessplan-writing/operations/`

**Dependencies:**
- **Sub-task 1-1 (Revenue):** COGS volume must scale with net sales.
- **Operations Phase:** Direct labor, material costs, and logistics.
- **Business Model Phase:** Gross margin targets and cost structure.

**Output:**
- `1-2-assumptions-cogs.json` (Specific Drivers)
- `1-2-assumptions-cogs-percentage.json` (Percentage of Revenue)

**Detailed Steps:**

1. **Determine COGS Methodology:** Evaluate available inputs and user instructions to select the most appropriate modeling branch.

    - **IF Approach 1: Specific Drivers (Detailed/Bottom-up):**
        - Identify and document the foundational drivers for each month of the 120-month projection:
            - **Direct Material/Unit Cost:** Monthly cost of raw materials or purchased goods per unit.
            - **Direct Labor:** Monthly wages for staff directly involved in production or service delivery.
            - **Hosting/Infrastructure:** Monthly cloud hosting costs (AWS/Azure) scaled by user or data volume.
            - **Customer Success:** Monthly headcount and salary for staff dedicated to post-sale support.
            - **Payment Processing:** Percentage fees for credit card or payment gateways (e.g., 3.5% of monthly revenue).
        - **Target File:** `1-2-assumptions-cogs.json`

    - **ELSE Approach 2: Percentage of Revenue (Aggregate/Top-down):**
        - **Cost of Goods Sold = % of Net Sales:** Define the monthly COGS percentage based on industry benchmarks and internal cost structures.
        - **Apply Industry Benchmarks (Standard % Range):**
            - **Wholesale:** ~85% (High volume, low margin).
            - **Manufacturing:** ~78-79% (Includes materials, direct labor, and factory overhead).
            - **Transport / Postal:** ~76% (Fuel, vehicle costs, site labor).
            - **Construction:** ~76% (Materials, site labor, subcontractors).
            - **Retail:** ~70% (Pure inventory purchase cost).
            - **Service (Leisure/Life):** ~58% (Direct service delivery costs).
            - **Real Estate / Rental:** ~53% (Depreciation and maintenance).
            - **IT / InfoComm:** ~52% (Software dev labor, server/hosting, outsourcing).
            - **Professional / Technical:** ~43% (Primarily expert labor).
            - **Accommodations / Food:** ~30-36% (Food/Beverage only; Labor is typically in SG&A, but monitor **FL Ratio (Food + Labor)** to keep it within 50-60%).
        - **Accounting Logic Constraints:**
            - **Labor Inclusion:** For Manufacturing, Construction, and IT, ensure **Direct Labor** (engineers/workers) is included in COGS. For Retail/Wholesale, COGS should strictly be the purchase price.
            - **Profitability Audit:** If the projected COGS % is 5-10 points above the industry average, identify causes (procurement costs, waste/loss, or low productivity) and model improvements.
        - **Target File:** `1-2-assumptions-cogs-percentage.json`

2. **Assume 120-Month Continuity:** Regardless of the chosen approach, the data MUST be projected for exactly 120 months to ensure consistency with the master financial grid.

3. **Logic Engine Check (Vagueness Audit):**
    - If the business model implies "profitability" as a goal but the resulting GM is below the industry benchmark (Approach 2), the agent MUST notify the user and suggest an optimized driver set (e.g., "To hit the 43% target for transit spatial media, we must reduce material costs by 15% in Year 3").

4. Consolidate into json format. Monthly based for 120 months.
5. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 264) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 1-3: Define Assumptions about People costs

**Description:** Define monthly salary benchmarks, headcount growth, social insurance, and granular outsourcer (subcontractor) assumptions, including travel, hardware, and AI tools. Corresponds to **Row 265** in the 'all' tab.

**Input:**
- `{output_folder}/businessplan-writing/team/`
- `{output_folder}/businessplan-writing/businessmodel/`
- `{output_folder}/businessplan-writing/operations/`

**Dependencies:**
- **Team Phase:** Role definitions, seniority levels, and hiring plan.
- **Sub-task 1-1 (Revenue):** Hiring speed must be consistent with revenue growth and capacity.
- **Sub-task 1-2 (COGS):** Direct labor costs must align with direct personnel assumptions.

**Output:**
- `1-3-assumptions-people.json`

**Proactive Benchmarking Policy (Japan-Specific Standard):**
- You MUST use the following **Fully-Loaded Monthly Cost** (Take-home + Social Insurance) benchmarks for Japan-based personnel if specific salaries are not provided:
    - **20-24 yrs (Entry):** ¥341,675
    - **25-29 yrs (Junior):** ¥580,500
    - **30-34 yrs (Intermediate):** ¥661,940
    - **35-39 yrs (Middle):** ¥676,315
    - **40-44 yrs (Senior):** ¥759,140
    - **45-49 yrs (Director):** ¥843,230
    - **50-54 yrs (Exec/Senior Dir):** ¥913,648
    - **55-59 yrs (Executive):** ¥900,002
    - **60-65 yrs (Expert/Part-time):** ¥614,730

**Detailed Steps:**
1. **Define Salary Benchmarks:** Establish monthly gross salary by role level (C-level, Director, Manager, Staff).
2. **Standardized Calculations (Japan-Specific):** You MUST use the logic found in `payroll_tax_calculator.js` (located in `.agent/skills/businessplan-writing/assets/`) to calculate the following for each role:
    - **Gross Salary:** The base monthly pay.
    - **Social Insurance (Employer & Employee):** Use `getSocialInsurance(salary, kaigo)` from the script.
    - **Income Tax:** Use `getIncomeTax(salary, type, numberOfDependents)` from the script.
3. **Fully-Loaded Cost Calculation:** For modeling purposes, the "People Expense" recorded in the financial statements must include Gross Salary + Employer-side Social Insurance (approximately ~15.5% of gross, but use the script for precision).
4. **Define Headcount Roadmap:** Specify monthly headcount increases/decreases (Opening, New, Resignee, Ending) for the 120-month period for all categories (Full-time, Part-time, Outsourcers).
5. **Define Outsourcer (Subcontractor) Assumptions:** You MUST model outsourcer costs based on the following drivers:
    - **Utilization:** Define a monthly utilization % (e.g., 100% for full-time equivalents, 50% for half-time).
    - **Full Time Equivalent (FTE):** Calculate as `Ending Headcount * Utilization`.
    - **Recurring Costs (per FTE):** Define monthly unit costs for Subcontract Expense, Commission Fees, Bonuses, Social Insurance (if applicable), Fringe Benefits, Training, Travel, and Communication.
    - **One-time Costs (per New Member):** Define unit costs for Recruiting and initial Hardware (Tools/PC) procurement.
    - **Hardware Depreciation:** Project depreciation over the defined life for tools purchased for new members.
6. **Define Non-Salary People Costs:**
    - **Travel Expenses:** Estimate monthly travel/transit costs per role (Full-time vs. Outsourcer).
    - **Hardware (PC/Hardware):** Define one-time or amortized costs for equipment (PC, Monitors, etc.) upon hiring or refresh.
    - **AI Tools & Subscriptions:** Define monthly subscription costs per head for AI enhancement tools (Gemini, Copilot, Claude Code, etc.).
7. **Consolidate and Export:** Synchronize all calculations (Full-time employees and Outsourcers) into `1-3-assumptions-people.json`. Ensure the data is monthly-based for 120 months.
8. **Google Sheets Population:** Use the `google-sheets` skill to populate the corresponding row (Row 265) in the 'all' tab of the master spreadsheet.

#### Sub-task 1-4: Define Assumptions about Rent and Overhead

**Description:** Define key SG&A and fixed overhead assumptions excluding salaries. Corresponds to **Row 266 and Row 267** in the 'all' tab.

**Input:**
- `{output_folder}/businessplan-writing/businessmodel/`
- `{output_folder}/businessplan-writing/go-to-market/`

**Dependencies:**
- **Sub-task 1-3 (People):** Headcount-driven costs (office rent, software, admin).
- **Go-To-Market Phase:** Marketing spend, customer acquisition costs (CAC), and channel budgets.
- **Operations Phase:** Fixed facility costs, utilities, and general overhead.

**Output:**
- `1-4-assumptions-rent-overhead.json`

**Proactive Benchmarking Policy (Logic Engine):**
- **Marketing (CAC):** If not specified, use the **LTV:CAC 3:1 Rule**. Derive LTV from Revenue assumptions and back-solve the maximum permissible CAC. Or, search for channel-specific benchmarks (e.g., LinkedIn B2B CPC).
- **Software/SaaS:** Monthly cost of internal tools (Slack, CRM, ERP) scaled by headcount.
- **Rent:** Use **¥25,000/tsubo/month** for Central Tokyo Grade B offices as a default for startups.

**Detailed Steps:**
1. **Identify and document SG&A and Overhead drivers:**
    - **Marketing (CAC):** Monthly Customer Acquisition Cost per channel and monthly budget allocation.
    - **Software/SaaS:** Monthly subscription costs for core operational tools.
    - **Rent & Utilities:** Monthly office rent, utilities, and general administrative fixed costs.
2. Consolidate into json format. Monthly based for 120 months.
3. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding rows (Row 266 and Row 267) in the 'all' tab of the master spreadsheet.

### Task 2: Define Assumptions about Balance Sheet

**Process Dependencies:**
- **Task 1 (Assumptions):** Inventory turnover and collection cycles scale with revenue/cogs.

#### Sub-task 2-1: AR/DSO Assumptions

**Description:** Define collection cycles. Corresponds to **Row 268** in the 'all' tab.

**Mandatory Output:** `label_en`: "AR/DSO Assumptions", `label_ja`: "売掛金・回収日数前提"

**Output:** `2-1-ar-assumptions.json`

**Dependencies:**
- **Sub-task 1-1 (Revenue):** DSO must be categorized by the customer segments defined in revenue modeling.
- **Go-To-Market Phase:** Payment terms offered to different tiers (Enterprise vs. SME).

**Detailed Steps:**

**Proactive Benchmarking Policy (Logic Engine):**
- You MUST auto-detect the customer segment from the GTM phase.
- **IF B2B Enterprise:** Default to **60 days** (End of next month + 30).
- **IF B2B SME / SaaS:** Default to **30 days** (Credit card / Direct debit).
- **IF B2C:** Default to **0-7 days**.
- DO NOT ask the user. Propose and confirm. 

1. **Assume Accounts Receivable (Days):** Define monthly DSO by customer segment.
2. Benchmarks: 30-45 days for SMEs, 60-90 days for Enterprise.
3. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 268) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 2-2: Inventory/DIO Assumptions

**Description:** Define inventory turnover. Corresponds to **Row 269** in the 'all' tab.

**Mandatory Output:** `label_en`: "Inventory/DIO Assumptions", `label_ja`: "棚卸資産・滞留日数前提"

**Output:** `2-2-inventory-assumptions.json`

**Dependencies:**
- **Sub-task 1-2 (COGS):** Inventory turnover (DIO) must scale with the cost of purchased or manufactured goods.
- **Operations Phase:** Lead times and safety stock requirements.

**Detailed Steps:**

**Proactive Benchmarking Policy (Logic Engine):**
- **IF SaaS/Service:** Auto-set to **0 days**.
- **IF Hardware/Retail:** Default to **45 days** (Safety stock + Lead time).

1. **Assume Inventory (Days):** Define monthly DIO per product category.
2. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 269) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 2-3: AP/DPO Assumptions

**Description:** Define payment cycles. Corresponds to **Row 270** in the 'all' tab.

**Mandatory Output:** `label_en`: "AP/DPO Assumptions", `label_ja`: "買掛金・支払日数前提"

**Output:** `2-3-ap-assumptions.json`

**Dependencies:**
- **Sub-task 1-2 (COGS):** Payment cycles for raw materials and merchandise.
- **Sub-task 1-4 (Overhead):** Payment terms for rent, utilities, and vendors.

**Detailed Steps:**
1. **Assume Accounts Payable (Days):** Define monthly DPO (usually 30 days).
2. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 270) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 2-4: CAPEX Assumptions

**Description:** Define monthly asset spend. Corresponds to **Row 271** in the 'all' tab.

**Dependencies:**
- **Product/Solution Phase:** Identify specific hardware/equipment required for the solution.
- **Operations Phase:** Facility setup costs and specialized equipment lead times.

**Output:** `2-4-capex-assumptions.json`

**Detailed Steps:**
1. **Assume Capital Expenditures (JPY):** List planned asset purchases by month for 120 months.
2. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 271) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 2-5: Depreciation Assumptions

**Description:** Define useful life and method. Corresponds to **Row 272** in the 'all' tab.

**Dependencies:**
- **Sub-task 2-4 (CAPEX):** Depreciation is calculated based on the assets acquired and their designated life.

**Output:** `2-5-depreciation-assumptions.json`

**Detailed Steps:**
1. **Assume Depreciation & Amortization (% of PP&E):** Define useful life and depreciation method (e.g., straight-line) per asset class according to Japan Tax Law.
2. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 272) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 2-6: Tax Rate Assumptions

**Description:** Define corporate tax rates. Corresponds to **Row 273** in the 'all' tab.

**Dependencies:**
- **Operations Phase:** Jurisdiction and corporate structure affect local tax rates.

**Output:** `2-6-tax-assumptions.json`

**Detailed Steps:**

**Proactive Benchmarking Policy (Logic Engine):**
- **Corporate Tax:** Auto-set to **30.6%** (Combined effective rate for large SMEs in Tokyo).
- **Consumption Tax:** Auto-set to **10%**.
- **Inhabitant Tax (Min):** ¥70,000/year per capita.

1. **Assume Tax Rate (% of EBT):** Set the combined effective tax rate (National + Local, typically ~30-34% for Japan).
2. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 273) in the 'all' tab of the master spreadsheet with the calculated values.


### Task 3: Define Assumptions about Cash Flow

**Process Dependencies:**
- **Task 6 (Cash Flow):** Financing needs are determined by the projected cash GAP.
- **Task 1 & 2:** Payment cycles and tax rates impact the scale of cash requirements.

#### Sub-task 3-1: Debt Issuance Assumptions

**Description:** Define loan terms. Corresponds to **Row 274** in the 'all' tab.

**Dependencies:**
- **Phase 13 (Financials):** Financing amounts are driven by the cash gap identified in the master statement logic.
- **Ask Phase:** Terms of the debt financing (if already determined).

**Output:** `3-1-debt-assumptions.json`

**Detailed Steps:**
1. **Assume Debt Issuance (Repayment) (JPY):** Define monthly loan principal inflows and repayment schedules (amortization).
2. Project 120-month values.
3. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 274) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 3-2: Equity Issuance Assumptions

**Description:** Define funding round timing. Corresponds to **Row 275** in the 'all' tab.

**Dependencies:**
- **Phase 13 (Financials):** Equity needs are driven by the cash gap identified in the master statement logic.
- **Ask Phase:** Specific terms of the fundraising round ( SAFE, Equity, etc.).

**Output:** `3-2-equity-assumptions.json`

**Proactive Benchmarking Policy (Logic Engine):**
- If funding rounds are mentioned without amounts, use the **J-Curve / Japan Startup Standard**:
    - **Seed:** ¥50M - ¥100M (Post-money ¥500M)
    - **Series A:** ¥300M - ¥500M (Post-money ¥1.5B - ¥2.5B)
    - **Series B:** ¥1B+ (Post-money ¥5B+)
- Default to **15-20% Dilution** per round if not specified.

**Detailed Steps:**
1. **Assume Equity Issued (Repaid) (JPY):** Define the timing and amount of capital raised (e.g., Series A, B) and any share buybacks.
2. Project 120-month values.
3. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 275) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 3-3: Interest Rate Assumptions

**Description:** Define annual interest rate. Corresponds to **Row 276** in the 'all' tab.

**Mandatory Output:** `label_en`: "Interest Rate Assumptions", `label_ja`: "金利前提"

**Output:** `3-3-interest-assumptions.json`

**Dependencies:**
- **Sub-task 3-2 (Debt):** Interest expense is calculated based on the outstanding debt balance each month.

**Detailed Steps:**

**Proactive Benchmarking Policy (Logic Engine):**
- **IF Japan Finance Corp (JFC):** Default to **2.1%** (Startup base rate).
- **IF Megabank (Trust):** Default to **1.5% - 1.8%**.
- **IF Unsecured Short-term:** Default to **3.0%**.

1. **Assume Interest (% of Debt):** Define the annual interest rate per loan type and convert to a monthly interest percentage.
2. Project 120-month values.
3. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 276) in the 'all' tab of the master spreadsheet with the calculated values.

#### Sub-task 3-4: Extraordinary Item Assumptions

**Description:** Define extraordinary items. Corresponds to **Row 277** in the 'all' tab.

**Output:** `3-4-extraordinary-assumptions.json`

**Detailed Steps:**
1. Identify and document the drivers for Extraordinary items:
    - **Asset Retirement:** Projected gains or losses from the sale or disposal of non-current assets.
    - **Restructuring:** One-time legal, severance, or relocation costs.
2. Project 120-month values.
3. **Google Sheets Population**: Use the `google-sheets` skill to populate the corresponding row (Row 277) in the 'all' tab of the master spreadsheet with the calculated values.


### Task 4: Generate Income Statement (Profit & Loss)

**Process Dependencies:**
- **Task 1 (Assumptions):** All P&L line items are directly driven by Task 1 JSON exports.
- **Task 2 (Assumptions):** Tax and depreciation rates impact Net Profit and EBITDA.

**Mandatory Dual Output:** In addition to the JSON output, each sub-task in this section MUST immediately populate the corresponding row in the master Google Sheet (initialized in Task 0) using the `google-sheets` skill (as per Global Rule 8).

#### Sub-task 4-1: Revenue (Row 3)

**Description:** Calculate monthly gross revenue (売上高). Corresponds to **Row 3** in the 'all' tab.

**Input:**
- 1-1-assumptions-revenue-orders.json
- 1-1-assumptions-revenue.json
- 1-1-revenue-growth.json

**Dependencies:**
- **Sub-task 1-1 (Revenue):** This sub-task retrieves the 120-month revenue drivers or total values to populate the Revenue row.

**Output:**
- `4-1-revenue.json`

**Detailed Steps:**
> **VC-Ready Standard (Bottom-Up Revenue Build):** Reject "top-down" market share logic (e.g., "1% of a $10B market"). Projections must be driven by operational metrics: Leads × Conversion Rate × Sales Cycle × Average Contract Value (ACV).
> **VC-Ready Standard (Quality of Revenue):** Strictly separate Recurring Revenue (ARR/MRR) from one-time fees (consulting, pilots). Monitor Net Revenue Retention (NRR) and Churn at a cohort level.
1. **Driver Selection**: Identify the specific operational driver (e.g., Headcount, Customer Count, Marketing Spend) from the Metadata Lookup Table.
2. **Parameter Retrieval**: Access the 120-month values of the driver from the corresponding assumption file (Sub-tasks 1-1 to 1-15).
3. **Formula Execution**: Multiply driver counts by unit economics (CAC, ACV, Salary) defined in the assumptions.
4. **Project 120-month values** and summarize into annual totals.
5. Calculate monthly revenue based on:
    - **New Customer Acquisition:** Total Marketing Spend / CAC.
    - **Existing Customer Revenue:** (Previous Month Total Customers - Churn) * Average Contract Value (ACV).
    - **Expansion Revenue:** Upsell percentage * Total Existing ARR.
6. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-2: Sales returns (Row 5)

**Description:** Calculate monthly sales returns (売上戻り高). Corresponds to **Row 5** in the 'all' tab.

**Mandatory Output:** `label_en`: "Sales returns", `label_ja`: "売上戻り高"

**Input:**
- 4-1-revenue.json
- 1-1-assumptions-revenue.json

**Dependencies:**
- **Sub-task 4-1 (Revenue):** Returns are calculated as a percentage of gross monthly revenue.

**Output:** `4-2-sales-returns.json`

**Detailed Steps:**
1. **Driver:** Percentage of monthly Revenue (Sub-task 4-1). Typical range: 1-3% for SaaS, 5-10% for e-commerce.
2. **Formula:** `Sales Returns = Revenue * Return Rate`
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG). Return rate may decrease as product matures.

#### Sub-task 4-3: Net sales (Row 6)

**Description:** Calculate monthly net sales (純売上高). Corresponds to **Row 6** in the 'all' tab.

**Mandatory Output:** `label_en`: "Net sales", `label_ja`: "純売上高"

**Input:**
- 4-1-revenue.json
- 4-2-sales-returns.json

**Dependencies:**
- **Sub-task 4-1 & 4-2:** Net Sales is the direct subtraction of Returns from Revenue.

**Output:** `4-3-net-sales.json`

**Detailed Steps:**
1. **Formula:** `Net Sales = Revenue (4-1) - Sales Returns (4-2)`
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG). Every value must equal the difference of the two inputs.

#### Sub-task 4-6: Cost of Goods Sold (Row 7)

**Description:** Calculate monthly total COGS (売上原価). Corresponds to **Row 7** in the 'all' tab.

**Mandatory Output:** `label_en`: "Cost of Goods Sold", `label_ja`: "売上原価"

**Input:**
- 1-2-assumptions-cogs.json
- 1-2-assumptions-cogs-percentage.json
- 4-1-revenue.json
- 4-4-cost-purchased-goods.json
- 4-5-cost-finished-goods.json

**Dependencies:**
- **Sub-task 1-2 (COGS Assumptions):** COGS values are derived from unit cost or percentage drivers.
- **Sub-task 4-1 (Revenue):** For percentage-based COGS, revenue is the base.

**Output:** `4-6-cost-of-goods-sold.json`

**Detailed Steps:**
> **VC-Ready Standard (COGS Purity):** Customer Success, hosting (AWS/Azure), and direct support costs MUST be in COGS to show the *true* gross margin, not hidden in OPEX.
1. **Formula:** `COGS = Cost of purchased goods sold (4-4) + Cost of finished goods sold (4-5)`. For service/SaaS businesses without inventory, COGS = direct costs (hosting, customer success salaries) as a percentage of Revenue.
2. **Driver:** Apply COGS % from Sub-task 1-2 (Approach 2) to Revenue (4-1).
3. Project 120-month values.

#### Sub-task 4-7: Beginning inventory of merchandise (Row 9)

**Description:** Calculate monthly beginning inventory of merchandise (期首商品棚卸). Corresponds to **Row 9** in the 'all' tab.

**Mandatory Output:** `label_en`: "Beginning inventory of merchandise", `label_ja`: "期首商品棚卸"

**Input:**
- 4-10-ending-inventory-merchandise.json
- 1-2-assumptions-cogs.json

**Output:** `4-7-beginning-inventory-merchandise.json`

**Detailed Steps:**
1. **Formula:** `Beginning Inventory (Month N) = Ending Inventory (Month N-1)` (Sub-task 4-10).
2. For SaaS/software businesses with no physical merchandise, set all values to 0 and explain in `notes`: "No physical merchandise — SaaS/service business model."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-8: Purchases of merchandise (Row 11)

**Description:** Calculate monthly purchases of merchandise (当期商品仕入). Corresponds to **Row 11** in the 'all' tab.

**Mandatory Output:** `label_en`: "Purchases of merchandise", `label_ja`: "当期商品仕入"

**Input:**
- 1-2-assumptions-cogs.json
- 4-1-revenue.json

**Output:** `4-8-purchases-merchandise.json`

**Detailed Steps:**
1. **Driver:** For businesses with physical goods, calculate purchases needed to maintain target inventory levels.
2. For SaaS/software businesses, set all values to 0 with `notes`: "No physical merchandise purchases — SaaS/service business model."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-9: Transfer to other account (Merchandise) (Row 12)

**Description:** Calculate monthly transfers (他勘定振替高(商)). Corresponds to **Row 12** in the 'all' tab.

**Mandatory Output:** `label_en`: "Transfer to other account (Merchandise)", `label_ja`: "他勘定振替高(商)"

**Input:** 1-2-assumptions-cogs.json

**Output:** `4-9-transfer-account-merchandise.json`

**Detailed Steps:**
1. Record any merchandise reclassified to other accounts (e.g., samples, donations).
2. For most startups, set all values to 0 with `notes`: "No merchandise reclassification expected."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-10: Ending inventory of merchandise (Row 13)

**Description:** Calculate monthly ending inventory of merchandise (期末商品棚卸). Corresponds to **Row 13** in the 'all' tab.

**Mandatory Output:** `label_en`: "Ending inventory of merchandise", `label_ja`: "期末商品棚卸"

**Input:**
- 4-7-beginning-inventory-merchandise.json to 4-8-purchases-merchandise.json
- 1-2-assumptions-cogs.json

**Output:** `4-10-ending-inventory-merchandise.json`

**Detailed Steps:**
1. **Formula:** `Ending Inventory = Beginning Inventory (2-5) + Purchases (2-6) - Transfers (2-7) - Cost of Purchased Goods Sold (2-9)`
2. For SaaS/software businesses, set all values to 0 with `notes`: "No physical merchandise inventory."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-4: Cost of purchased goods sold (Row 15)

**Description:** Calculate monthly cost of purchased goods sold (商品売上原価). Corresponds to **Row 15** in the 'all' tab.

**Mandatory Output:** `label_en`: "Cost of purchased goods sold", `label_ja`: "商品売上原価"

**Input:**
- 4-7-beginning-inventory-merchandise.json to 4-9-transfer-account-merchandise.json
- 1-2-assumptions-cogs.json

**Output:** `4-4-cost-purchased-goods.json`

**Detailed Steps:**
1. **Formula:** `Cost of Purchased Goods Sold = Beginning Inventory (2-5) + Purchases (2-6) - Transfers (2-7) - Ending Inventory (2-8)`
2. For SaaS/software businesses, set all values to 0 with `notes`: "No physical merchandise — SaaS/service business model."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-11: Beginning inventory of finished goods (Row 16)

**Description:** Calculate monthly beginning inventory. Corresponds to **Row 16** in the 'all' tab.

**Mandatory Output:** `label_en`: "Beginning inventory of finished goods", `label_ja`: "期首製品棚卸"

**Input:**
- 4-14-ending-inventory-fg.json
- 1-2-assumptions-cogs.json

**Output:** `4-11-beginning-inventory-fg.json`

**Detailed Steps:**
1. **Formula:** `Beginning Finished Goods (Month N) = Ending Finished Goods (Month N-1)` (Sub-task 4-14).
2. For SaaS/software businesses, set all values to 0 with `notes`: "No physical finished goods — SaaS/service business model."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-12: Cost of finished goods manufactured (Row 17)

**Description:** Calculate monthly manufacturing costs. Corresponds to **Row 17** in the 'all' tab.

**Mandatory Output:** `label_en`: "Cost of finished goods manufactured", `label_ja`: "当期製品製造原価"

**Input:** 1-2-assumptions-cogs.json

**Output:** `4-12-cost-fg-manufactured.json`

**Detailed Steps:**
1. **Driver:** For manufacturing businesses, sum direct materials + direct labor + manufacturing overhead.
2. For SaaS/software businesses, set all values to 0 with `notes`: "No manufactured products — SaaS/service business model."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-13: Transfer to other account (Finished Goods) (Row 18)

**Description:** Calculate monthly transfers. Corresponds to **Row 18** in the 'all' tab.

**Mandatory Output:** `label_en`: "Transfer to other account (Finished Goods)", `label_ja`: "他勘定振替高(製)"

**Input:** 1-2-assumptions-cogs.json

**Output:** `4-13-transfer-account-fg.json`

**Detailed Steps:**
1. Record any finished goods reclassified (e.g., used internally, donated).
2. For most startups, set all values to 0 with `notes`: "No finished goods reclassification expected."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-14: Ending inventory of finished goods (Row 19)

**Description:** Calculate monthly ending inventory. Corresponds to **Row 19** in the 'all' tab.

**Mandatory Output:** `label_en`: "Ending inventory of finished goods", `label_ja`: "期末製品棚卸"

**Input:**
- 4-11-beginning-inventory-fg.json to 4-12-cost-fg-manufactured.json
- 1-2-assumptions-cogs.json

**Output:** `4-14-ending-inventory-fg.json`

**Detailed Steps:**
1. **Formula:** `Ending FG = Beginning FG (4-11) + Cost of FG (4-12) - Transfers (4-13) - Cost of FG Sold (4-5)`
2. For SaaS/software businesses, set all values to 0 with `notes`: "No finished goods inventory."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-5: Cost of finished goods sold (Row 20)

**Description:** Calculate monthly cost. Corresponds to **Row 20** in the 'all' tab.

**Mandatory Output:** `label_en`: "Cost of finished goods sold", `label_ja`: "製品売上原価"

**Input:**
- 4-11-beginning-inventory-fg.json to 4-13-transfer-account-fg.json
- 1-2-assumptions-cogs.json

**Output:** `4-5-cost-finished-goods.json`

**Detailed Steps:**
1. **Formula:** `Cost of FG Sold = Beginning FG (4-11) + Cost of FG (4-12) - Transfers (4-13) - Ending FG (4-14)`
2. For SaaS/software businesses, set all values to 0 with `notes`: "No manufactured products sold."
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-15: Gross profit (Row 21)

**Description:** Calculate monthly gross profit. Corresponds to **Row 21** in the 'all' tab.

**Mandatory Output:** `label_en`: "Gross profit", `label_ja`: "売上総利益"

**Input:**
- 4-3-net-sales.json
- 4-6-cost-of-goods-sold.json

**Output:** `4-15-gross-profit.json`

**Detailed Steps:**
1. **Formula:** `Gross Profit = Net Sales (4-3) - COGS (4-6)`
2. Every monthly value MUST equal exactly the difference of the two inputs.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-16: Directors’ compensation (Row 23)

**Description:** Calculate monthly compensation. Corresponds to **Row 23** in the 'all' tab.

**Mandatory Output:** `label_en`: "Directors' compensation", `label_ja`: "役員報酬"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Headcount Roadmap

**Output:**
- `4-16-directors-compensation.json`

**Detailed Steps:**
1. Identify specific CXO roles (CEO, CTO, CFO, etc.) and their planned hiring/start dates.
2. Define annual base compensation for each CXO.
3. Calculate monthly compensation (Annual / 12) including any planned increases post-funding.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-17: Directors' bonuses (Row 24)

**Description:** Calculate monthly bonuses. Corresponds to **Row 24** in the 'all' tab.

**Mandatory Output:** `label_en`: "Directors' bonuses", `label_ja`: "役員賞与"

**Input:**
- 4-16-directors-compensation.json
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `4-17-directors-bonuses.json`

**Detailed Steps:**
1. Define bonus percentage of annual compensation for each CXO (e.g., 10-20%).
2. Define payout timing (e.g., June and December in Japan).
3. Accrue monthly bonus liability if using accrual accounting, or record cash payout in the target months.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-18: Salaries (Row 25)

**Description:** Calculate monthly salaries. Corresponds to **Row 25** in the 'all' tab.

**Mandatory Output:** `label_en`: "Salaries", `label_ja`: "給与手当"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Headcount Roadmap

**Dependencies:**
- **Phase 11: Team:** Use the headcount roadmap, hiring cadence, and seniority levels.
- **Phase 10: Operations:** Use the functional roles and departmental structure to categorize costs.
- **Phase 6: Traction & Progress:** Align hiring dates with the release timing of product.

**Detailed Steps:**
> **VC-Ready Standard (Sales Capacity Realism):** Account for sales rep quotas, ramp time (3-6 months), and an underperformance buffer (typically 30% of reps failing to hit quota).
1. Map the headcount roadmap by department (Sales, R&D, G&A) and seniority level.
2. Apply average annual salary benchmarks for each role.
3. Calculate monthly gross salary based on hiring dates and ramp-up periods.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-19: Bonuses (Row 26)

**Description:** Calculate monthly bonuses. Corresponds to **Row 26** in the 'all' tab.

**Mandatory Output:** `label_en`: "Bonuses", `label_ja`: "賞与"

**Input:**
- 4-18-salaries.json
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `4-19-bonuses.json`

**Detailed Steps:**
1. Define bonus percentage of monthly or annual salary (e.g., 1-2 months' salary).
2. Project payments based on the **Salaries** roadmap (Sub-task 4-18).
3. Apply payout timing (e.g., Summer/Winter bonuses in June and December).
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-20: Share-based compensation expense (Row 27)

**Description:** Calculate monthly share-based compensation. Corresponds to **Row 27** in the 'all' tab.

**Mandatory Output:** `label_en`: "Share-based compensation expense", `label_ja`: "株式報酬費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries)

**Output:**
- `4-20-share-based-compensation.json`

**Detailed Steps:**
1. **Driver:** Link to the **Headcount Roadmap** or **Salaries** (Sub-task 4-18). Apply monthly cost-per-head assumptions or percentage of salary.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-21: Required Payroll Related Expenses (Row 28)

**Description:** Calculate monthly employer-side social insurance. Corresponds to **Row 28** in the 'all' tab.

**Mandatory Output:** `label_en`: "Legal welfare expense", `label_ja`: "法定福利費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 4-18-salaries.json
- 4-16-directors-compensation.json
- Asset: `payroll_tax_calculator.js` (located in `.agent/skills/businessplan-writing/assets/`)

**Output:**
- `4-21-legal-welfare-expense.json`

**Detailed Steps:**
1. **Calculation Method:** Use the `getSocialInsurance(salary, kaigo)` function from `payroll_tax_calculator.js` for every employee/director record.
2. **Parameters:**
   - `salary`: Use monthly gross salary from Sub-task 4-18 or 4-16.
   - `kaigo`: Use "1" if person is aged 40-64, or "0" otherwise (as per assumptions from Sub-task 1-3).
3. **Extraction:** The individual legal welfare expense (employer share) is returned by the script.
4. **Aggregation:** Sum the legal welfare expenses for all personnel to get the monthly total.
5. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-22: Fringe Benefits (Row 29)

**Description:** Calculate monthly welfare costs. Corresponds to **Row 29** in the 'all' tab.

**Mandatory Output:** `label_en`: "Welfare expense", `label_ja`: "福利厚生費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries)
- Sub-task 2-16 (Directors' compensation)

**Output:**
- `4-22-welfare-expense.json`

**Detailed Steps:**
1. Link to the **Headcount Roadmap** or **Salaries** (Sub-task 2-18).
2. Apply monthly cost-per-head assumptions or percentage of salary.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-23: Recruiting expense (Row 30)

**Description:** Calculate monthly recruiting costs. Corresponds to **Row 30** in the 'all' tab.

**Mandatory Output:** `label_en`: "Recruiting expense", `label_ja`: "採用費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Headcount Roadmap

**Output:**
- `4-23-recruiting-expense.json`

**Detailed Steps:**
1. Calculate monthly recruiting costs based on the **Headcount Roadmap**.
2. Apply assumptions for cost-per-hire (e.g., agency fees at 30-35% of annual salary or job board costs).
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-24: Training expense (Row 31)

**Description:** Calculate monthly training costs. Corresponds to **Row 31** in the 'all' tab.

**Mandatory Output:** `label_en`: "Training expense", `label_ja`: "研修費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries)

**Output:**
- `4-24-training-expense.json`

**Detailed Steps:**
1. Link to the **Headcount Roadmap** or **Salaries** (Sub-task 2-18).
2. Apply monthly cost-per-head assumptions or percentage of salary.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-25: Subcontract expense (Row 32)

**Description:** Calculate monthly subcontracting costs. Corresponds to **Row 32** in the 'all' tab.

**Mandatory Output:** `label_en`: "Subcontract expense", `label_ja`: "外注費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 1-2-assumptions-cogs.json

**Output:**
- `4-25-subcontract-expense.json`

**Detailed Steps:**
1. **Driver:** Monthly contract cost per function Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-26: Freightage expense (Row 33)

**Description:** Calculate monthly shipping/freight costs. Corresponds to **Row 33** in the 'all' tab.

**Mandatory Output:** `label_en`: "Freightage expense", `label_ja`: "荷造運賃"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 4-1-revenue.json

**Output:**
- `4-26-freightage-expense.json`

**Detailed Steps:**
1. **Driver:** Orders × Shipping cost/order Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-27: Advertising expense (Row 34)

**Description:** Calculate monthly marketing costs. Corresponds to **Row 34** in the 'all' tab.

**Mandatory Output:** `label_en`: "Advertising expense", `label_ja`: "広告宣伝費"

**Input:**
- 1-1-assumptions-revenue.json
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Dependencies:**
- **Phase 9: GTM:** Use the marketing channel strategy, funnel conversion targets, and CAC benchmarks to derive spend requirements.
- **Phase 7: Market:** Account for market competitiveness and saturation trends in the CAC assumptions.

**Detailed Steps:**
> **VC-Ready Standard (Unit Economics Granularity):** Break down CAC by channel (Paid, Organic, Outbound). Avoid "blended CAC" which masks unprofitable channels. Target a CAC Payback period of 12-18 months.
> **VC-Ready Standard (Diminishing Returns):** Model a rising CAC as marketing spend scales. Early adopters are cheap; mass market is expensive.
1. Calculate required marketing spend to hit revenue targets: New Customers Needed * CAC.
2. Break down spend by channel (Google Ads, Facebook, LinkedIn, Offline).
3. Adjust monthly spend based on channel scalability and diminishing returns assumptions.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-28: Entertainment expense (Row 35)

**Description:** Calculate monthly entertainment costs. Corresponds to **Row 35** in the 'all' tab.

**Mandatory Output:** `label_en`: "Entertainment expense", `label_ja`: "交際費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries/Headcount)

**Output:**
- `4-28-entertainment-expense.json`

**Detailed Steps:**
1. **Driver:** Sales HC × ¥20k/head/month Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-29: Conference expenses (Row 36)

**Description:** Calculate monthly meeting costs. Corresponds to **Row 36** in the 'all' tab.

**Mandatory Output:** `label_en`: "Conference expenses", `label_ja`: "会議費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries/Headcount)

**Output:**
- `4-29-conference-expenses.json`

**Detailed Steps:**
1. **Driver:** HC × ¥3k/head/month Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-30: Traveling expense (Row 37)

**Description:** Calculate monthly travel costs. Corresponds to **Row 37** in the 'all' tab.

**Mandatory Output:** `label_en`: "Traveling expense", `label_ja`: "旅費交通費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries/Headcount)

**Output:**
- `4-30-traveling-expense.json`

**Detailed Steps:**
1. Project monthly travel costs based on Sales headcount and expected site visit frequency.
2. Apply average cost per trip assumptions.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-31: Communication expense (Row 38)

**Description:** Calculate monthly communication costs. Corresponds to **Row 38** in the 'all' tab.

**Mandatory Output:** `label_en`: "Communication expense", `label_ja`: "通信費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries/Headcount)

**Output:**
- `4-31-communication-expense.json`

**Detailed Steps:**
2. Project monthly costs for phone, internet, and messaging services scaled by total headcount.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-32: Sales commission (Row 39)

**Description:** Calculate monthly sales commissions. Corresponds to **Row 39** in the 'all' tab.

**Mandatory Output:** `label_en`: "Sales commission", `label_ja`: "販売手数料"

**Input:**
- 4-1-revenue.json
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `4-32-sales-commission.json`

**Detailed Steps:**
1. **Driver:** Revenue × Commission% (3-10%) Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-33: Supplies expense (Row 40)

**Description:** Calculate monthly supplies costs. Corresponds to **Row 40** in the 'all' tab.

**Mandatory Output:** `label_en`: "Supplies expense", `label_ja`: "消耗品費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries/Headcount)

**Output:**
- `4-33-supplies-expense.json`

**Detailed Steps:**
1. **Driver:** HC × ¥3k/head/month Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-34: Stationery expense (Row 41)

**Description:** Calculate monthly stationery costs. Corresponds to **Row 41** in the 'all' tab.

**Mandatory Output:** `label_en`: "Stationery expense", `label_ja`: "事務用品費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Sub-task 2-18 (Salaries/Headcount)

**Output:**
- `4-34-stationery-expense.json`

**Detailed Steps:**
1. **Driver:** HC × ¥1k/head/month Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-35: Repair and maintenance expense (Row 42)

**Description:** Calculate monthly repair costs. Corresponds to **Row 42** in the 'all' tab.

**Mandatory Output:** `label_en`: "Repair and maintenance expense", `label_ja`: "修繕費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 2-4-capex-assumptions.json

**Output:**
- `4-35-repair-maintenance.json`

**Detailed Steps:**
1. **Driver:** Fixed assets × 2-5%/yr / 12 Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-36: Utilities expense (Row 43)

**Description:** Calculate monthly utility costs. Corresponds to **Row 43** in the 'all' tab.

**Mandatory Output:** `label_en`: "Utilities expense", `label_ja`: "水道光熱費"

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- Headcount Roadmap

**Output:**
- `4-36-utilities-expense.json`

**Detailed Steps:**
1. **Driver:** Office sqm × ¥500/sqm/month Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-37: Books and subscription expense (Row 44)

**Description:** Calculate monthly subscription costs. Corresponds to **Row 44** in the 'all' tab.

- Sub-task 4-18 (Salaries/Headcount)

**Output:**
- `4-37-books-subscriptions.json`

**Detailed Steps:**
1. **Driver:** HC × ¥3k/head/month Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-38: Membership fee (Row 45)

**Description:** Calculate monthly membership fees. Corresponds to **Row 45** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 4-18-salaries.json

**Output:**
- `4-38-membership-fees.json`

**Detailed Steps:**
1. **Driver:** Fixed annual dues / 12 Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-39: Printing and binding fee (Row 46)

**Description:** Calculate monthly printing costs. Corresponds to **Row 46** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 4-1-revenue.json

**Output:**
- `4-39-printing-binding.json`

**Detailed Steps:**
1. **Driver:** Per-project cost Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-40: Commission fee (Row 47)

**Description:** Calculate monthly commission fees. Corresponds to **Row 47** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 4-1-revenue.json

**Output:**
- `4-40-commission-fees.json`

**Detailed Steps:**
1. Project monthly commission costs based on **Revenue** targets (Sub-task 4-1).
2. Apply commission percentage per sale or per contract value.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-41: Rent expenses on real estates (Row 48)

**Description:** Calculate monthly real estate rent. Corresponds to **Row 48** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 4-18-salaries.json

**Dependencies:**
- **Phase 10: Operations:** Use the IT/Offices and facilities plan to determine square footage and location costs.
- **Phase 11: Team:** Headcount growth drives the timing and scale of office space needs.

**Detailed Steps:**
1. Calculate square footage requirements based on the headcount roadmap (e.g., 100 sqft per head).
2. Apply market unit price per sqft for the target office location.
3. Include Common Area Maintenance (CAM) fees and 10% consumption tax.
4. Account for office moves or expansions at specific headcount triggers.
5. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-42: Rent expense (Row 49)

**Description:** Calculate monthly equipment/other rent. Corresponds to **Row 49** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 2-4-capex-assumptions.json

**Output:**
- `4-42-rent-expense.json`

**Detailed Steps:**
1. **Driver:** Equipment lease / coworking Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-43: Insurance expense (Row 50)

**Description:** Calculate monthly insurance costs. Corresponds to **Row 50** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 2-4-capex-assumptions.json
- 4-18-salaries.json

**Output:**
- `4-43-insurance-expense.json`

**Detailed Steps:**
1. **Driver:** Annual premium / 12 Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-44: Sundry taxes (Row 51)

**Description:** Calculate monthly taxes and public dues. Corresponds to **Row 51** in the 'all' tab.

**Mandatory Output:** `label_en`: "Sundry taxes", `label_ja`: "租税公課"

**Detailed Steps:**
1. Include non-income taxes like enterprise tax (proportional part), stamp duties, and fixed asset taxes.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-45: Professional fees (Row 52)

**Description:** Calculate monthly professional fees. Corresponds to **Row 52** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `4-45-professional-fees.json`

**Detailed Steps:**
1. **Driver:** Monthly retainer (accountant/lawyer) Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-46: Donations expense (Row 53)

**Description:** Calculate monthly donation costs. Corresponds to **Row 53** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `4-46-donations-expense.json`

**Detailed Steps:**
1. **Driver:** Discretionary; 0 for startups Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` corresponding to this sub-task.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-47: Patent royalties (Row 54)

**Description:** Calculate monthly patent royalties. Corresponds to **Row 54** in the 'all' tab.

**Input:**
- 4-1-revenue.json
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `4-47-patent-royalties.json`

**Detailed Steps:**
1. Project royalties based on % of revenue.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-48: Miscellaneous expense (Row 55)

**Description:** Calculate monthly miscellaneous costs. Corresponds to **Row 55** in the 'all' tab.

**Input:**
**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `4-48-miscellaneous-expense.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-49: Research and development expense (Row 56)

**Description:** Calculate monthly R&D costs. Corresponds to **Row 56** in the 'all' tab.

**Input:**
- 1-3-assumptions-salaries.json
- 1-4-assumptions-rent-overhead.json
- 4-18-salaries.json

**Output:**
- `4-49-rd-expense.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-50: Provision of allowance for doubtful accounts (Row 57)

**Description:** Calculate monthly bad debt provision. Corresponds to **Row 57** in the 'all' tab.

**Input:**
- 4-1-revenue.json
- 2-1-ar-assumptions.json

**Output:**
- `4-50-bad-debt-provision.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-51: Depreciation expense (Row 58)

**Description:** Calculate monthly depreciation. Corresponds to **Row 58** in the 'all' tab.

**Output:**
- `4-51-depreciation-expense.json`

**Detailed Steps:**
1. **Calculate Depreciation:** Based on Sub-task 2-5 assumptions and asset balances.
2. **Link to Cash Flow:** Add back as a non-cash item in Sub-task 6-3.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-52: Amortization of deferred assets

**Description:** Calculate monthly amortization of deferred assets.

**Output:**
- `4-52-amortization-deferred.json`

**Detailed Steps:**
1. **Calculate Amortization:** Based on Sub-task 2-5 assumptions.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-53: Total of operating expenses (Row 59)

**Description:** Sum all SG&A items (Sub-tasks 4-16 through 4-52) for every month. Corresponds to **Row 59** in the 'all' tab.

**Input:**
- 4-16-directors-compensation.json through 4-52-amortization-deferred.json

**Output:** `4-53-operating-expenses-total.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-54: Operating income (Row 60)

**Description:** Calculate monthly operating income. Corresponds to **Row 60** in the 'all' tab.

**Mandatory Output:** `label_en`: "Operating income", `label_ja`: "営業利益"

**Input:**
- 4-15-gross-profit.json
- 4-53-operating-expenses-total.json

**Output:** `4-54-operating-income.json`
**Detailed Steps:**
1. **Formula:** `Gross Profit (4-15) - Total Operating Expenses (4-53)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-55: Interest income (Row 63)

**Description:** Calculate monthly interest income. Corresponds to **Row 63** in the 'all' tab.
**Output:** `4-55-interest-income.json`
**Detailed Steps:**
1. Calculate monthly interest income from cash reserves.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-56: Interest expense (Row 67)

**Description:** Calculate monthly interest expense. Corresponds to **Row 67** in the 'all' tab.

**Input:**
- 3-3-interest-assumptions.json
- 5-46-cons-tax-payable.json
- 5-47-advance-received.json

**Output:** `4-56-interest-expense.json`
**Detailed Steps:**
1. Calculate monthly interest expense based on debt assumptions.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-57: Dividend income (Row 64)
**Output:** `4-57-dividend-income.json`
**Detailed Steps:**
1. Record any projected dividend receipts.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-58: Subsidy income (Row 65)
**Output:** `4-58-subsidy-income.json`
**Detailed Steps:**
1. Record any projected government subsidies or grants.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-59: Miscellaneous income (Non-Op) (Row 66)
**Output:** `4-59-misc-income.json`
**Detailed Steps:**
1. Record any other non-operating income.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-60: Commission fee (Non-Op) (Row 68)
**Output:** `4-60-commission-non-op.json`
**Detailed Steps:**
1. Record any non-operating commission fees.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-61: Miscellaneous loss (Non-Op) (Row 69)
**Output:** `4-61-misc-loss.json`
**Detailed Steps:**
1. Record any other non-operating losses.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-62: Ordinary income (Row 70)

**Description:** Calculate monthly ordinary income. Corresponds to **Row 70** in the 'all' tab.
**Output:** `4-62-ordinary-income.json`
**Detailed Steps:**
1. **Formula:** `Operating Income (4-54) + Non-Operating Income (4-55 to 4-59) - Non-Operating Expenses (4-56, 4-60, 4-61)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Calculate ordinary income (経常利益).

**Mandatory Output:** `label_en`: "Ordinary income", `label_ja`: "経常利益"

#### Sub-task 4-63: Reversal of allowance for doubtful accounts (Row 72)

**Description:** Record reversal of bad debt provisions (貸倒引当金戻入). Corresponds to **Row 72** in the 'all' tab.

**Output:** `4-63-reversal-bad-debt.json`
**Detailed Steps:**
1. Record any reversals of previous provisions.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Record reversal of bad debt provisions (貸倒引当金戻入).

#### Sub-task 4-64: Loss on retirement of non-current assets (Row 74)

**Description:** Record losses on disposal or retirement of assets (固定資産除却損). Corresponds to **Row 74** in the 'all' tab.

**Output:** `4-64-loss-retirement-assets.json`

**Description:** Record losses on disposal or retirement of assets (固定資産除却損).

#### Sub-task 4-65: Profit (or loss) before income taxes (Row 75)

**Description:** Calculate monthly profit before taxes. Corresponds to **Row 75** in the 'all' tab.

**Mandatory Output:** `label_en`: "Profit (or loss) before income taxes", `label_ja`: "税引前当期純利益"

**Output:** `4-65-pbt.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-66: Income taxes – current (Row 77)

**Description:** Calculate monthly income taxes. Corresponds to **Row 77** in the 'all' tab.

**Mandatory Output:** `label_en`: "Income taxes – current", `label_ja`: "法人税等"

**Output:** `4-66-income-taxes-current.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-67: Income taxes – deferred (Row 78)

**Description:** Record deferred tax adjustments (法人税等調整額). Corresponds to **Row 78** in the 'all' tab.

**Mandatory Output:** `label_en`: "Income taxes – deferred", `label_ja`: "法人税等調整額"

**Output:** `4-67-income-taxes-deferred.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 4-68: Net profit (or loss) (Row 79)

**Description:** Calculate monthly net profit. Corresponds to **Row 79** in the 'all' tab.

**Mandatory Output:** `label_en`: "Net profit (or loss)", `label_ja`: "当期純利益"

**Output:** `4-68-net-profit.json`

**Detailed Steps:**
1. **Driver:** Identify the specific driver for this line item from the Sub-Task Metadata Lookup Table at the end of this document. Apply it to the business context.
2. **Mandatory Labels:** Use the exact `label_en` and `label_ja` from the Sub-Task Metadata Lookup Table.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).


#### Sub-task 4-69: Consolidate P&L data

**Description:** Merge all 120-month P&L sub-tasks into a unified master JSON grid.

**Input:**
- 4-1-revenue.json through 4-68-net-profit.json

**Output:** `4-69-pnl-grid.json`

**Detailed Steps:**
1. **Load All P/L Files:** Read every individual JSON file from `4-1-revenue.json` through `4-68-net-profit.json`.
2. **Standardize Structure (Master Grid):**
   The output MUST follow this grid-based structure to ensure easy population of 120xN spreadsheets:
   ```json
   {
     "metadata": {
       "sub_task_number": "080",
       "label_en": "Consolidated P&L Grid",
       "label_ja": "損益計算書集計グリッド",
       "columns": 121,
       "rows": 60
     },
     "headers": ["Account", "Month 1", "Month 2", ..., "Month 120"],
     "rows": [
       {
         "account_en": "Revenue",
         "account_ja": "売上高",
         "values": [1000, 1100, ..., 50000]
       },
       ...
     ]
   }
   ```
   **CRITICAL REQUIREMENTS:**
   1. **120-Month Data:** Every row in the "rows" array MUST contain exactly 120 values. **MISSING VALUES OR BLANKS WILL CAUSE SPREADSHEET POPULATION FAILURE.**
   2. **Account Labels:** Both `account_en` and `account_ja` must be present for every row.
   3. **No Missing Values:** DO NOT use null or empty strings. Use `0` for inactive months.
   4. **No Annual Summaries:** Consolidation grids contain ONLY periodic (monthly) values.
3. **Map Metrics:** Extract `label_en`, `label_ja`, and `monthly_values` (exactly 120 values) from each file to populate the `rows` array.
4. **Consistency Audit:** Check that for each line item, the values are exactly 120 Periodic values.
5. **Save Result:** Save the consolidated data as `4-69-pnl-grid.json`.



### Task 5: Generate Balance Sheet (BS)

**Process Dependencies:**
- **Task 4 (Income Statement):** Net profit impacts Retained Earnings.
- **Task 2 (Assumptions):** DSO, DIO, and DPO determine Working Capital assets/liabilities.

**Mandatory Dual Output:** In addition to the JSON output, each sub-task in this section MUST immediately populate the corresponding row in the master Google Sheet (initialized in Task 0) using the `google-sheets` skill (as per Global Rule 8).

#### Sub-task 5-1: Cash and deposits (BS) (Row 83)

**Description:** Closing monthly cash balance. Corresponds to **Row 83** in the 'all' tab.

**Input:**
- 6-63-net-change-cash.json
- 2-1-ar-assumptions.json

**Output:**
- `5-1-cash-bs.json`

**Detailed Steps:**
1. **The Final Cash Plug:** Because cash reflects all business activities, it is the final BS item resolved. The **closing cash balance is plugged into the top of the balance sheet**.
2. **Determine Monthly Closing:** `Opening Balance + Net Increase/Decrease in Cash (from Sub-task 6-63)`.
3. **Verification:** Total Assets (5-38) MUST equal Total Liabilities + Equity.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-2: Bank Account 1 (Row 84)

**Description:** Calculate monthly values. Corresponds to **Row 84** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 6-63-net-change-cash.json

**Output:**
- `5-2-cash-account-1.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-3: Bank Account 2 (Row 85)

**Description:** Calculate monthly values. Corresponds to **Row 85** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 6-63-net-change-cash.json

**Output:**
- `5-3-cash-account-2.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-4: Bank Account 3 (Row 86)

**Description:** Calculate monthly values. Corresponds to **Row 86** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 6-63-net-change-cash.json

**Output:**
- `5-4-cash-account-3.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-8: Trade accounts receivable (Row 87)

**Description:** Calculate monthly values. Corresponds to **Row 87** in the 'all' tab.

**Input:**
- 4-3-net-sales.json
- 2-1-ar-assumptions.json

**Output:**
- `5-8-trade-ar.json`

**Detailed Steps:**
1. **Working Capital Tie-in:** **Accounts receivable is a function of net sales**.
2. **Calculate Monthly Balance:** `Previous Month AR + Current Month Net Sales (4-3) - Monthly Collections`.
3. **Determine Collections:** Apply **DSO (Days Sales Outstanding)** from Sub-task 2-1 to current and prior month revenue.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-9: Allowance for doubtful accounts (Row 88)

**Description:** Calculate monthly allowance value. Corresponds to **Row 88** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 4-50-bad-debt-provision.json

**Output:**
- `5-9-bad-debt-allowance.json`

**Detailed Steps:**
1. **Calculate Monthly Balance:** `Previous Month Balance + Current Month Provision (4-50) - Actual Write-offs`.
2. **Consistency Check:** Ensure the incremental change matches the SG&A provision exactly.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-10: Merchandise and inventory (Row 89)

**Description:** Calculate monthly merchandise balance. Corresponds to **Row 89** in the 'all' tab.

**Input:**
- 2-2-inventory-assumptions.json
- 4-6-cost-of-goods-sold.json

**Output:**
- `5-10-merchandise.json`

**Detailed Steps:**
1. **Working Capital Tie-in:** **Inventory is a function of COGS**.
2. **Calculate Monthly Balance:** `Previous Month Inventory + Purchases - COGS (4-6)`.
3. **Determine Purchases:** Apply **Inventory Days** from Sub-task 2-2 to future P&L requirements.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-11: Supplies (Row 90)

**Description:** Calculate monthly supplies balance. Corresponds to **Row 90** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 4-16-directors-compensation.json to 4-53-operating-expenses-total.json (Operating Expenses)

**Detailed Steps:**
1. **Consolidation:** This sub-task groups all minor current asset accounts (Supplies, Prepaid Expenses, Accrued Revenue).
2. **Calculate Monthly Balance:** Based on prepayments or consumption lags defined in Task 1.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-12: Work in process (Row 91)

**Description:** Calculate monthly WIP. Corresponds to **Row 91** in the 'all' tab.

**Input:**
- 2-2-inventory-assumptions.json
- 4-6-cost-of-goods-sold.json

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-13: Finished goods (Row 92)

**Description:** Calculate monthly finished goods. Corresponds to **Row 92** in the 'all' tab.

**Input:**
- 2-2-inventory-assumptions.json
- 4-11-beginning-inventory-fg.json to 4-14-ending-inventory-fg.json (Finished Goods P&L)

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-23: Suspense consumption tax (Row 93)

**Description:** Calculate monthly values. Corresponds to **Row 93** in the 'all' tab.

**Input:**
- 2-6-tax-assumptions.json
- 3-1-debt-assumptions.json

**Detailed Steps:**
1. **Identify Payments:** Record interim corporate tax payments (usually 50% of prior year tax) as per Sub-task 2-6.
2. **Identify Withholding:** Record any tax withheld from interest income or other receipts.
3. **Determine Monthly Closing:** `Prior Closing Balance + Monthly Payments - Reversals (when final tax is settled)`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-14: Advance payments – trade (Row 94)

**Description:** Calculate monthly values. Corresponds to **Row 94** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 4-8-purchases-merchandise.json

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-15: Advance payments – other (Row 95)

**Description:** Calculate monthly values. Corresponds to **Row 95** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-59: Accrued consumption tax (Row 96)

**Description:** Calculate monthly accrued consumption tax. Corresponds to **Row 96** in the 'all' tab.

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-16: Accounts Receivable-Other (Tatekaekin) (Row 97)

**Description:** Calculate monthly values. Corresponds to **Row 97** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 4-59-misc-income.json

**Output:**
- `5-16-ar-other-tatekaekin.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-17: Prepaid expense (Row 98)

**Description:** Calculate monthly prepaid expenses. Corresponds to **Row 98** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- Sub-tasks 029-060 (SG&A Expenses)

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-18: Accrued revenue (Row 99)

**Description:** Calculate monthly accrued revenue. Corresponds to **Row 99** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 4-1-revenue.json

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-19: Loans Receivable (Row 100)

**Description:** Calculate monthly loans receivable. Corresponds to **Row 100** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json

**Output:**
- `5-19-loans-receivable.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-20: Loans Receivable from Directors (Row 101)

**Description:** Calculate monthly loans to directors. Corresponds to **Row 101** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json

**Output:**
- `5-20-loans-receivable-directors.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-21: Accounts Receivable-Other (Mishuunyuukin) (Row 102)

**Description:** Calculate monthly values. Corresponds to **Row 102** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json

**Output:**
- `5-21-ar-other-mishuunyuukin.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-22: Temporary payment (Row 103)

**Description:** Calculate monthly values. Corresponds to **Row 103** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json

**Output:**
- `5-22-temporary-payment.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Record temporary payments based on business logic.
   - Reductions: Record settlement of temporary payments.
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-23: Suspense Consumption Tax (Row 104)

**Description:** Calculate monthly suspense consumption tax. Corresponds to **Row 104** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 2-6-tax-assumptions.json

**Output:**
- `5-23-suspense-cons-tax.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-26: Facilities attached to buildings (Row 108)

**Description:** Calculate monthly balances. Corresponds to **Row 108** in the 'all' tab.

**Input:**
- 2-4-capex-assumptions.json
- 4-51-depreciation-expense.json
- 2-5-depreciation-assumptions.json

**Output:**
- `5-26-facilities.json`

**Detailed Steps:**
1. **Consolidation:** Groups Buildings, Tools, Software, and Patents.
2. **Calculate Monthly Balance:** `Previous Month Balance + Current CapEx (2-4) - Current Depreciation (4-51)`.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-27: Tools, furniture and fixtures (Row 109)

**Description:** Calculate monthly balances. Corresponds to **Row 109** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 2-4-capex-assumptions.json

**Output:**
- `5-27-tools-furniture.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-60: Accumulated Depreciation (Row 110)

**Description:** Calculate monthly accumulated depreciation. Corresponds to **Row 110** in the 'all' tab.

**Input:**
- 2-5-depreciation-assumptions.json
- 4-51-depreciation-expense.json

**Output:**
- `5-60-accumulated-depreciation.json`

**Detailed Steps:**
1. **Compute Opening Balance:** Use initial balance from Sub-task 2-1.
2. **Calculate Monthly Balance:** `Previous Month Balance + Current Month Depreciation Expense (4-51)`.
3. **Consistency Check:** Ensure the incremental change matches the P&L expense exactly. If assets are retired, reduce balance by the accumulated depreciation of the retired asset.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-28: Software (Row 113)

**Description:** Calculate monthly software balance. Corresponds to **Row 113** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 2-4-capex-assumptions.json

**Output:**
- `5-28-software.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-29: Patents (Row 114)

**Description:** Calculate monthly patent balance. Corresponds to **Row 114** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 2-4-capex-assumptions.json

**Output:**
- `5-29-patents.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-30: Other Non-Current Asset (Row 115)

**Description:** Calculate monthly balances. Corresponds to **Row 115** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 2-4-capex-assumptions.json

**Output:**
- `5-30-other-non-current-asset.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-34: Security Deposit (Row 118)

**Description:** Calculate monthly balances. Corresponds to **Row 118** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json
- 1-4-assumptions-rent-overhead.json

**Output:**
- `5-34-security-deposit.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-35: Guarantee Deposit (Row 119)

**Description:** Calculate monthly balances. Corresponds to **Row 119** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json

**Output:**
- `5-35-guarantee-deposit.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-36: Investments in Capital (Row 120)

**Description:** Calculate monthly balances. Corresponds to **Row 120** in the 'all' tab.

**Input:**
- 2-1-ar-assumptions.json

**Output:**
- `5-36-investments-capital.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-37: Deferred assets (Row 123)

**Description:** Calculate monthly balances. Corresponds to **Row 123** in the 'all' tab.

**Input:**
- 2-5-depreciation-assumptions.json
- 4-52-amortization-deferred.json

**Output:**
- `5-37-deferred-assets.json`

**Detailed Steps:**
1. **Calculate Monthly Balance:** `Previous Month Balance - Current Amortization (4-52)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-33: Bond Issuance Cost

**Description:** Calculate monthly values.

**Input:**
- 2-1-ar-assumptions.json
- Sub-task 010 (Equity Assumptions)

**Output:**
- `5-33-bond-issuance-cost.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-32: Development Expenses

**Description:** Calculate monthly values.

**Input:**
- 2-1-ar-assumptions.json
- Sub-task 062 (R&D Expense)

**Output:**
- `5-32-development-expenses.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balance defined in Sub-task 2-1 (Existing Assets) for the first month.
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., CapEx in 012, Revenue in 014).
   - Reductions: Map from the relevant driver (e.g., Depreciation in 064, Collections in 011).
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Reductions`.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG) ensuring mathematical consistency across the entire timeline.

#### Sub-task 5-38: Total Assets
**Output:**
- `5-38-total-assets.json`

**Description:** Derived monthly total of all asset categories.

**Input:**
- Sub-tasks 3-1 to 3-8 (All Asset sub-tasks)

**Output:**
- `5-38-total-assets.json`

**Detailed Steps:**
1. **Formula:** `Total Assets = Sum(5-1 through 5-37)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).
3. **Verification:** This total must match Liabilities + Equity.

#### Sub-task 5-40: Short-term loans payable (Row 134)

**Description:** Calculate monthly short-term loans. Corresponds to **Row 134** in the 'all' tab.

**Input:**
- Sub-task 020 (Purchases of merchandise)
- 2-3-ap-assumptions.json

**Output:**
- `5-40-short-term-loans.json`

**Detailed Steps:**
1. **Compute Opening Balance:** Use initial balance from Sub-task 010.
2. **Calculate Monthly Balance:** `Previous Month Short-term loans + New Issuance - Monthly Repayments`.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-39: Trade accounts payable (Row 132)

**Description:** Calculate monthly trade A/P balance. Corresponds to **Row 132** in the 'all' tab.

**Input:**
- 2-3-ap-assumptions.json
- 4-8-purchases-merchandise.json

**Output:**
- `5-39-trade-ap.json`

**Detailed Steps:**
1. **Working Capital Tie-in:** **Accounts payable is a function of purchases**.
2. **Calculate Monthly Balance:** `Previous Month AP + Current Month Purchases (4-8) - Monthly Payments`.
3. **Determine Payments:** Apply **DPO (Days Payable Outstanding)** from Sub-task 2-3 to purchases.
4. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-41: Current portion of long-term debt (Row 133)

**Description:** Calculate monthly current portion. Corresponds to **Row 133** in the 'all' tab.

**Input:**
- Sub-task 1-11 (Liability Assumptions)
- Sub-task 1-15 (Funding Roadmap)

**Input:**
- Sub-task 1-11 (Liability Assumptions)
- Sub-task 1-15 (Funding Roadmap)

**Output:**
- `5-41-current-portion-debt.json`

**Detailed Steps:**
1. **Consolidation:** Groups Short-term loans and the current portion of long-term debt.
2. **Calculate Monthly Balance:** Based on the repayment schedule from Task 1.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-51: Loans Payable to Directors (Row 135)

**Description:** Calculate monthly loans from directors. Corresponds to **Row 135** in the 'all' tab.

**Input:**
- 2-3-ap-assumptions.json
- Sub-task 013 (Financing Policy)

**Output:**
- `5-51-loans-pay-directors.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balances defined in Sub-task 3-1 (Existing Liabilities).
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., New Loans from 013).
   - Repayments: Apply the principal repayment schedule defined in Sub-task 013.
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Repayments`.
4. **Project 120-month values** ensuring mathematical consistency across the entire timeline and 10-year annual values (Column DX-EG).

#### Sub-task 5-43: Accrued expenses
**Output:**
- `5-43-accrued-expenses.json`

**Description:** Calculate monthly values for unpaid SG&A and corporate taxes.

**Input:**
- Sub-task 4-75 (Income taxes – current)
- 4-16-directors-compensation.json to 4-53-operating-expenses-total.json (Operating Expenses)

**Output:**
- `5-45-income-tax-payable.json`

**Detailed Steps:**
1. **Accruals:** Link to SG&A items recognized but not yet paid (from Task 1 terms).
2. **Taxes:** Link to Income taxes current (4-75) net of interim payments (from 5-23).
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-43: Accrued expenses (Row 137)

**Description:** Calculate monthly accrued expenses. Corresponds to **Row 137** in the 'all' tab.

**Input:**
- Sub-tasks 029-060 (SG&A Expenses)
- 2-3-ap-assumptions.json

**Output:**
- `5-43-accrued-expenses.json`

**Detailed Steps:**
1. **Compute Opening Balance:** Use initial balances from Sub-task 010.
2. **Calculate Monthly Accrual:** Link to total SG&A expenses (Sub-tasks 029-060) that are recognized but not yet paid (e.g., utility bills, commission fees).
3. **Determine Payments:** Apply payment delay assumptions (e.g., N+1 month) from Sub-task 2-3.
4. **Calculate Monthly Closing:** `Previous Month Balance + Current Accrual - Current Payment`.
5. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-44: Accrued expenses(Card1) (Row 138)

**Description:** Calculate monthly card liabilities. Corresponds to **Row 138** in the 'all' tab.

**Input:**
- 2-3-ap-assumptions.json

**Output:**
- `5-44-accrued-expenses-card1.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balances defined in Sub-task 3-1 (Existing Liabilities).
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., New Loans from 013).
   - Repayments: Apply the principal repayment schedule defined in Sub-task 013.
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Repayments`.
4. **Project 120-month values** ensuring mathematical consistency across the entire timeline and 10-year annual values (Column DX-EG).

#### Sub-task 5-45: Income tax payable (Row 139)

**Description:** Calculate monthly income tax payable. Corresponds to **Row 139** in the 'all' tab.

**Input:**
- Sub-task 076 (Income taxes – current P&L)
- Sub-task 007 (Tax Assumptions - Payment timing)

**Output:**
- `5-45-income-tax-payable.json`

**Detailed Steps:**
1. **Compute Opening Balance:** Use initial balance from Sub-task 010.
2. **Calculate Monthly Accrual:** Link to current period tax expense from P&L (Sub-task 076).
3. **Determine Payment timing:** In Japan, tax is typically paid twice a year (Interim and Final). Use Sub-task 007 to trigger these cash outflows.
4. **Calculate Monthly Closing:** `Previous Month Balance + Current Accrual - Tax Payments`.
5. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-47: Advance received
**Output:**
- `5-47-advance-received.json`

**Description:** Calculate monthly values for advances from customers and misc liabilities.

**Input:**
- Sub-task 1-11 (Liability Assumptions)
- 2-1-ar-assumptions.json

**Output:**
- `5-42-ap-other.json`

**Detailed Steps:**
1. **Consolidation:** Groups Accounts Payable - Other. Corresponds to **Row 136** in the 'all' tab.
2. **Calculate Monthly Balance:** Based on non-trade liability accruals.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-46: Consumption tax payable (Row 140)

**Description:** Calculate monthly net consumption tax liability. Corresponds to **Row 140** in the 'all' tab.

#### Sub-task 5-47: Advance received (Row 141)

**Description:** Calculate monthly advances received. Corresponds to **Row 141** in the 'all' tab.

#### Sub-task 5-48: Withholdings (Row 142)

**Description:** Calculate monthly payroll withholdings. Corresponds to **Row 142** in the 'all' tab.


#### Sub-task 5-49: Suspense payments (Row 143)

**Description:** Calculate monthly suspense payments. Corresponds to **Row 143** in the 'all' tab.

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balances defined in Sub-task 3-1 (Existing Liabilities).
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., New Loans from 013).
   - Repayments: Apply the principal repayment schedule defined in Sub-task 013.
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Repayments`.
4. **Project 120-month values** ensuring mathematical consistency across the entire timeline and 10-year annual values (Column DX-EG).

#### Sub-task 5-50: Suspense received Accrued consumption tax (Row 144)

**Description:** Calculate monthly suspense consumption tax. Corresponds to **Row 144** in the 'all' tab.

**Input:**
- 2-3-ap-assumptions.json

**Output:**
- `5-50-accrued-cons-tax.json`

**Detailed Steps:**
1. **Compute Opening Balance**: Use the initial balances defined in Sub-task 3-1 (Existing Liabilities).
2. **Calculate Monthly Changes**:
   - Additions: Map from the relevant driver (e.g., New Loans from 013).
   - Repayments: Apply the principal repayment schedule defined in Sub-task 013.
3. **Determine Monthly Closing**: `Prior Closing Balance + Monthly Additions - Monthly Repayments`.
4. **Project 120-month values** ensuring mathematical consistency across the entire timeline and 10-year annual values (Column DX-EG).

#### Sub-task 5-52: Long-term debt (Row 147)

**Description:** Calculate monthly long-term debt balance. Corresponds to **Row 147** in the 'all' tab.

**Input:**
- Sub-task 1-15 (Funding Roadmap)

**Output:**
- `5-52-long-term-debt.json`

**Detailed Steps:**
1. **Loan Linkage:** This balance drives interest expense (4-56).
2. **Calculate Monthly Balance:** `Previous Month Balance + New Issuance (from 6-56/6-58 Financing CF) - Current Portion reclass (5-41)`.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-53: Capital stock (Row 152)

**Description:** Calculate monthly capital stock. Corresponds to **Row 152** in the 'all' tab.

**Output:**
- `5-53-capital-stock.json`

**Detailed Steps:**
1. **Equity Linkage:** Reflects funding rounds (Seed, Series A, etc.).
2. **Calculate Monthly Balance:** `Previous Month Balance + New Capital Contribution (from 6-54)`.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-54: Capital reserve (Row 154)

**Description:** Calculate monthly capital reserve. Corresponds to **Row 154** in the 'all' tab.

**Output:**
- `5-54-capital-reserve.json`

**Detailed Steps:**
1. **Compute Monthly Balance:** `Opening Balance + Current Month Financing Surplus (from 6-55)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-55: Retained earnings (Row 160)

**Description:** Calculate monthly retained earnings (brought forward). Corresponds to **Row 160** in the 'all' tab.

**Output:**
- `5-55-retained-earnings.json`

**Detailed Steps:**
1. **Compute Monthly Balance:** `Prior Closing Balance + Monthly Net Profit (from 4-78)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-56: Total Equity

**Description:** Calculate the sum of all equity components.

**Output:**
- `5-56-total-equity.json`

**Detailed Steps:**
1. **Formula:** `Total Equity = Capital Stock + Capital Reserve + Retained Earnings`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-57: Consolidate Balance Sheet data

**Description:** Merge all 120-month BS sub-tasks into a unified master JSON grid.

**Input:**
- 5-1-cash-bs.json through 5-56-total-equity.json

**Output:**
- `5-57-bs-grid.json`

**Detailed Steps:**
1. **Load All BS Files:** Read every individual JSON file from `5-1-cash-bs.json` through `5-56-total-equity.json`.
2. **Standardize Structure (Master Grid):** Follow the 120xN grid format for spreadsheet population.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 5-58: Suspense taxes
**Output:** `5-58-suspense-taxes.json`
**Detailed Steps:** Record interim tax payments not yet finalized (仮払税金).

#### Sub-task 5-59: Accrued consumption tax
**Output:** `5-59-accrued-cons-tax-asset.json`
**Detailed Steps:** Record refundable consumption tax as a current asset (未収消費税).

#### Sub-task 5-60: Accumulated depreciation
**Output:** `5-60-accumulated-depreciation.json`
**Detailed Steps:** Calculate the cumulative depreciation to date for all tangible fixed assets (減価償却累計額).

#### Sub-task 5-61: Share issuance cost
**Output:** `5-61-share-issuance-cost.json`
**Detailed Steps:** Track amortizable fees associated with issuing company shares (株式交付費).

#### Sub-task 5-62: Other capital surplus
**Output:** `5-62-other-capital-surplus.json`
**Detailed Steps:** Record capital surplus items outside of the legal reserve (その他資本剰余金).

#### Sub-task 5-63: Reserve for advanced depreciation of non-current assets
**Output:** `5-63-reserve-advanced-depreciation.json`
**Detailed Steps:** Track tax-deferred reserves for specialized asset accounting (固定資産圧縮積立金).

#### Sub-task 5-64: Valuation and translation adjustments
**Output:** `5-64-valuation-adjustments.json`
**Detailed Steps:** Record unrealized gains or losses from asset revaluations or FX translations (評価・換算差額等).

#### Sub-task 5-65: Share acquisition rights
**Output:** `5-65-share-acquisition-rights.json`
**Detailed Steps:** Record the value of outstanding stock options and warrants (新株予約権).

#### Sub-task 5-66: Other retained earnings
**Output:** `5-66-other-retained-earnings.json`
**Detailed Steps:** Record miscellaneous retained earnings adjustments (その他利益剰余金).

### Task 6: Generate Cash Flow Statement (CF)

**Process Dependencies:**
- **Task 4 (Income Statement):** Starting point (Net Profit) and non-cash items (Depreciation).
- **Task 5 (Balance Sheet):** Changes in Working Capital and Investing/Financing balances.

**Mandatory Dual Output:** In addition to the JSON output, each sub-task in this section MUST immediately populate the corresponding row in the master Google Sheet (initialized in Task 0) using the `google-sheets` skill (as per Global Rule 8).

**Description:** Pull monthly net profit. Corresponds to **Row 177** in the 'all' tab.

**Dependencies:**
- **Sub-task 4-68 (Net Profit):** Net profit from the Income Statement is the starting point for the indirect cash flow method.
**Detailed Steps:**
1. Retrieve net profit from Sub-task 4-68.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Add back income tax expense. Corresponds to **Row 178** in the 'all' tab.
**Detailed Steps:**
1. Retrieve income taxes from Sub-task 4-66 and 4-67.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Add back D&A. Corresponds to **Row 179** in the 'all' tab.
**Detailed Steps:**
1. Retrieve depreciation from Sub-task 4-51.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Add back amortization. Corresponds to **Row 180** in the 'all' tab.
**Detailed Steps:**
1. Retrieve amortization from Sub-task 4-52.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Add back bad debt provision. Corresponds to **Row 181** in the 'all' tab.
**Detailed Steps:**
1. Retrieve provision from Sub-task 4-50.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Adjust monthly interest expense. Corresponds to **Row 182** in the 'all' tab.
**Detailed Steps:**
1. Retrieve interest expense from Sub-task 4-56.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Adjust monthly interest income. Corresponds to **Row 183** in the 'all' tab.
**Detailed Steps:**
1. Retrieve interest income from Sub-task 4-55.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Adjust monthly misc income. Corresponds to **Row 184** in the 'all' tab.
**Detailed Steps:**
1. Retrieve misc income from Sub-task 4-59.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Adjust monthly subsidy income. Corresponds to **Row 185** in the 'all' tab.
**Detailed Steps:**
1. Retrieve subsidy income from Sub-task 4-58.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Adjust monthly reversal. Corresponds to **Row 186** in the 'all' tab.
**Detailed Steps:**
1. Retrieve reversal from Sub-task 4-63.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Adjust monthly loss on retirement. Corresponds to **Row 187** in the 'all' tab.
**Detailed Steps:**
1. Retrieve loss from Sub-task 4-64.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Calculate monthly change in A/R. Corresponds to **Row 190** in the 'all' tab.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`. Link to Sub-task 5-8.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Calculate monthly change in finished goods. Corresponds to **Row 194** in the 'all' tab.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`. Link to Sub-task 5-13.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-13: Change in Merchandise (Row 191)
**Description:** Monthly change. Link to 5-10.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-14: Change in Supplies (Row 192)
**Description:** Monthly change. Link to 5-11.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-15: Change in Work in process (Row 193)
**Description:** Monthly change. Link to 5-12.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-16: Change in Finished goods (Row 194)
**Description:** Monthly change. Link to 5-13.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

**Description:** Calculate monthly change. Corresponds to **Row 219** in the 'all' tab.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`. Link to Sub-tasks 5-14 to 5-50.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-17: Change in AP (Row 195)
**Description:** Monthly change. Link to 5-39.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-18: Change in Suspense taxes (Row 196)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-19: Change in Advance payments – trade (Row 197)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-20: Change in Advance payments – other (Row 198)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-21: Change in Accrued consumption tax (Row 199)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-22: Change in AR-other (Tatekaekin) (Row 200)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-23: Change in Prepaid expense (Row 201)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-24: Change in Accrued revenue (Row 202)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-25: Change in Loans receivable (Row 203)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-26: Change in Loans receivable (Director) (Row 204)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-27: Change in AR-other (Mishuunyuukin) (Row 205)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-28: Change in Temporary payment (Row 206)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-29: Change in Suspense consumption tax (Row 207)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-30: Change in Loans payable to directors (Row 208)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-31: Change in AP-other (Row 209)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-32: Change in Accrued expenses (Row 210)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-33: Change in Accrued expenses(Card1) (Row 211)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-34: Change in Income tax payable (Row 212)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-35: Change in Consumption tax payable (Row 213)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-36: Change in Advance received (Row 214)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-37: Change in Withholdings (Row 215)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-38: Change in Suspense payments (Row 216)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-39: Change in Suspense received (Row 217)
**Description:** Monthly change.
**Detailed Steps:**
1. **Formula:** `BS(Month N) - BS(Month N-1)`.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-40: Interest Expense Paid (Row 220)
**Description:** Cash out.
**Detailed Steps:**
1. Record interest paid.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-41: Subsidy Income Received (Row 221)
**Description:** Cash in.
**Detailed Steps:**
1. Record subsidy received.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-42: Interest Income Received (Row 222)
**Description:** Cash in.
**Detailed Steps:**
1. Record interest received.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-43: Miscellaneous Income Received (Row 223)
**Description:** Cash in.
**Detailed Steps:**
1. Record misc cash in.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-44: Capex: Facilities attached to buildings (Row 229)
**Description:** Cash out.
**Detailed Steps:**
1. Record investment.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-45: Capex: Tools and Tech (Row 230)
**Description:** Cash out.
**Detailed Steps:**
1. Record investment.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-46: Capex: Software (Row 231)
**Description:** Cash out.
**Detailed Steps:**
1. Record investment.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-47: Capex: Patents (Row 232)
**Description:** Cash out.
**Detailed Steps:**
1. Record investment.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-48: Capex: Other non-current asset (Row 233)
**Description:** Cash out.
**Detailed Steps:**
1. Record investment.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-49: Startup: Start-up costs (Row 234)
**Description:** Cash out.
**Detailed Steps:**
1. Record costs.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-50: Startup: Development expenses (Row 235)
**Description:** Cash out.
**Detailed Steps:**
1. Record costs.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-51: Startup: Security deposit (Row 236)
**Description:** Cash out/in.
**Detailed Steps:**
1. Record deposit changes.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-52: Startup: Guarantee deposit (Row 237)
**Description:** Cash out/in.
**Detailed Steps:**
1. Record deposit changes.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-53: Investing: Capital Investments (Row 238)
**Description:** Cash out.
**Detailed Steps:**
1. Record investment.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-54: Financing: Capital stock (Row 245)
**Description:** Cash in from equity.
**Detailed Steps:**
1. Record issuance.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-55: Financing: Capital reserve (Row 245)
**Description:** Cash in from equity.
**Detailed Steps:**
1. Record issuance surplus.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-56: Financing: Long-term debt (Row 243)
**Description:** Cash in from loans.
**Detailed Steps:**
1. Record new debt.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-57: Financing: Debt current maturities (Row 250)
**Description:** Cash out for principal.
**Detailed Steps:**
1. Record repayments.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-58: Financing: Short-term loans (Row 244)
**Description:** Net cash flow.
**Detailed Steps:**
1. Record net changes.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-59: Financing: Bond issuance (Row 246)
**Description:** Cash in.
**Detailed Steps:**
1. Record proceeds.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-60: Financing: Share issuance cost (Row 250)
**Description:** Cash out.
**Detailed Steps:**
1. Record costs.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-61: Financing: Cash dividends paid (Row 250)
**Description:** Cash out.
**Detailed Steps:**
1. Record payments.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-62: Opening Cash Balance (Row 258)
**Description:** Monthly beginning cash.
**Detailed Steps:**
1. Pull opening balance.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-63: Net Change in Cash (Row 259)
**Description:** Monthly ending cash.
**Detailed Steps:**
1. Sum activity totals.
2. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-64: Consolidate Cash Flow data
**Output:** `6-64-cf-grid.json`

**Detailed Steps:**
1. Consolidate all individual CF JSON files into a master 120-month grid.
2. Verify that Opening Cash + Net Change = Closing Cash.
3. Project 120-month values (Column G-DV) and 10-year annual values (Column DX-EG).

#### Sub-task 6-65: Operating Cash flow (Before Changes in NWC)
**Output:** `6-65-ocf-pre-nwc.json`
**Detailed Steps:** Sum Net Profit (6-1) and all non-cash adjustments (6-2 through 6-11).

#### Sub-task 6-66: Changes in Net Working Capital (Summary)
**Output:** `6-66-nwc-change-summary.json`
**Detailed Steps:** Sum all working capital changes (6-12 through 6-39).

#### Sub-task 6-67: Beginning cash position
**Output:** `6-67-beginning-cash.json`
**Detailed Steps:** Pull the Closing Cash balance of the previous month (Sub-task 6-68).

#### Sub-task 6-68: End cash position
**Output:** `6-68-end-cash.json`
**Detailed Steps:** Calculate `Beginning Cash (6-62) + Net Change in Cash (6-63)`. Verify this matches BS Cash (5-1) and Row 259.

### Task 7: Calculate Ratios

**Process Dependencies:**
- **Task 4 (P&L):** Revenue, COGS, Gross Profit, Operating Income, Net Income, Interest Expense, EBITDA from the consolidated P&L grid (`4-72-pl-grid.json`).
- **Task 5 (BS):** Total Assets, Current Assets, Current Liabilities, Inventory, Cash, Shareholders' Equity, Total Debt, Accounts Receivable from the consolidated BS grid (`5-68-bs-grid.json`).
- **Task 6 (CF):** Operating, Investing, and Financing cash flows from the consolidated CF grid (`6-64-cf-grid.json`).

**Reference Skill:** This task follows the methodology defined in the `analyzing-financial-statements` skill (`calculate_ratios.py` and `interpret_ratios.py` under `businessplan-writing/assets/`). All formulas, safe-division guards (denominator == 0 → return 0), and industry benchmark interpretations MUST be applied.

**General Rules for All Ratio Sub-Tasks:**
1. **120-Month Granularity:** Every ratio MUST be calculated for each of the 120 months individually, producing a `monthly_values` array of 120 entries.
2. **Annual Aggregation:** Compute `annual_values` (10 entries) using the trailing-twelve-month (TTM) method for flow metrics (P&L items) and period-end values for stock metrics (B/S items).
3. **Safe Division:** If the denominator is zero for any month, the ratio value for that month MUST be `0.0` (not `null`, `NaN`, or `Infinity`).
4. **Interpretation:** Each ratio entry MUST include a `benchmark` object with `excellent`, `good`, `acceptable`, and `poor` thresholds sourced from the `interpret_ratios.py` industry benchmarks.
5. **Bilingual Labels:** All `label_en` and `label_ja` fields must be populated.

#### Sub-task 7-1: Calculate Profitability Ratios

**Description:** Calculate ROE, ROA, Gross Margin, Operating Margin, and Net Margin for 120 months.

**Input:**
- `4-72-pl-grid.json` (Net Income, Revenue, Gross Profit, Operating Income)
- `5-68-bs-grid.json` (Total Assets, Shareholders' Equity)

**Output:**
- `7-1-profitability-ratios.json`

**Detailed Steps:**
1. **ROE (自己資本利益率):** `Net Income ÷ Shareholders' Equity`. Use monthly net income and period-end equity.
2. **ROA (総資産利益率):** `Net Income ÷ Total Assets`. Use monthly net income and period-end total assets.
3. **Gross Margin (売上総利益率):** `(Revenue - COGS) ÷ Revenue`. Derived from P&L gross profit line.
4. **Operating Margin (営業利益率):** `Operating Income ÷ Revenue`. From P&L operating income.
5. **Net Margin (純利益率):** `Net Income ÷ Revenue`. From P&L net income.
6. **Project 120-month values.**

#### Sub-task 7-2: Calculate Liquidity Ratios

**Description:** Calculate Current Ratio, Quick Ratio, and Cash Ratio for 120 months.

**Input:**
- `5-68-bs-grid.json` (Current Assets, Current Liabilities, Inventory, Cash)

**Output:**
- `7-2-liquidity-ratios.json`

**Detailed Steps:**
1. **Current Ratio (流動比率):** `Current Assets ÷ Current Liabilities`.
2. **Quick Ratio (当座比率):** `(Current Assets - Inventory) ÷ Current Liabilities`. Inventory = sum of Merchandise (5-10), Supplies (5-11), WIP (5-12), Finished Goods (5-13).
3. **Cash Ratio (現金比率):** `Cash and Deposits ÷ Current Liabilities`. Cash = Cash and Deposits (5-1).
4. **Project 120-month values.**

#### Sub-task 7-3: Calculate Leverage Ratios

**Description:** Calculate Debt-to-Equity, Interest Coverage, and Debt Service Coverage Ratio for 120 months.

**Input:**
- `4-72-pl-grid.json` (Operating Income, Interest Expense)
- `5-68-bs-grid.json` (Total Debt, Shareholders' Equity, Current Portion of Long-Term Debt)

**Output:**
- `7-3-leverage-ratios.json`

**Detailed Steps:**
1. **Debt-to-Equity Ratio (負債資本倍率):** `Total Debt ÷ Shareholders' Equity`.
2. **Interest Coverage Ratio (インタレスト・カバレッジ・レシオ):** `Operating Income ÷ Interest Expense`. If Interest Expense is zero, return 0.0.
3. **Debt Service Coverage Ratio (DSCR):** `Operating Income ÷ (Interest Expense + Current Portion of Long-Term Debt)`. Total debt service = interest payments + scheduled principal repayments due within 12 months.
4. **Project 120-month values.**

#### Sub-task 7-4: Calculate Efficiency Ratios

**Description:** Calculate Asset Turnover, Inventory Turnover, and Receivables Turnover for 120 months.

**Input:**
- `4-72-pl-grid.json` (Revenue, COGS)
- `5-68-bs-grid.json` (Total Assets, Inventory, Accounts Receivable)

**Output:**
- `7-4-efficiency-ratios.json`

**Detailed Steps:**
1. **Asset Turnover (総資産回転率):** `Revenue ÷ Total Assets`. Annualized revenue (TTM) divided by period-end total assets.
2. **Inventory Turnover (棚卸資産回転率):** `COGS ÷ Inventory`. Annualized COGS (TTM) divided by period-end inventory.
3. **Receivables Turnover (売掛金回転率):** `Revenue ÷ Accounts Receivable`. Annualized revenue (TTM) divided by period-end trade AR.
4. **Days Sales Outstanding (売掛金回転日数):** `365 ÷ Receivables Turnover`. Derived from step 3.
5. **Project 120-month values.**

#### Sub-task 7-5: Calculate Valuation Ratios

**Description:** Calculate P/E, P/B, P/S, EV/EBITDA, and PEG ratios for 120 months.

**Input:**
- `4-72-pl-grid.json` (Net Income, Revenue, EBITDA)
- `5-68-bs-grid.json` (Shareholders' Equity, Total Debt, Cash)
- Market data: Share Price, Diluted Shares Outstanding (from user assumptions or valuation tasks).

**Output:**
- `7-5-valuation-ratios.json`

**Detailed Steps:**
1. **P/E Ratio (株価収益率):** `Share Price ÷ EPS`. EPS = Net Income ÷ Diluted Shares Outstanding.
2. **P/B Ratio (株価純資産倍率):** `Share Price ÷ Book Value Per Share`. BVPS = Shareholders' Equity ÷ Diluted Shares Outstanding.
3. **P/S Ratio (株価売上高倍率):** `Market Cap ÷ Revenue`. Market Cap = Share Price × Diluted Shares Outstanding.
4. **EV/EBITDA (企業価値倍率):** `Enterprise Value ÷ EBITDA`. EV = Market Cap + Total Debt - Cash.
5. **PEG Ratio:** `P/E Ratio ÷ (Earnings Growth Rate × 100)`. Earnings growth rate = YoY Net Income growth. If growth rate ≤ 0, set PEG to 0.0.
6. **Project 120-month values.**

#### Sub-task 7-6: Calculate Per-Share Metrics

**Description:** Calculate EPS, Book Value per Share, and Dividend per Share for 120 months.

**Input:**
- `4-72-pl-grid.json` (Net Income)
- `5-68-bs-grid.json` (Shareholders' Equity)
- Market data: Diluted Shares Outstanding.

**Output:**
- `7-6-per-share-metrics.json`

**Detailed Steps:**
1. **EPS (一株当たり当期純利益):** `Net Income ÷ Diluted Shares Outstanding`.
2. **Book Value Per Share (一株当たり純資産):** `Shareholders' Equity ÷ Diluted Shares Outstanding`.
3. **Dividend Per Share (一株当たり配当金):** `Total Dividends ÷ Diluted Shares Outstanding`. If no dividend policy is defined, set to 0 for all months (typical for startups).
4. **Project 120-month values.**

### Task 8: Calculate Cost of Capital & Discount Rate

**Process Dependencies:**
- **Benchmarks:** Risk-free rates and Peer Betas from external databases or web search.
- **Task 5 (BS):** D/E ratio for levering/unlevering beta.

#### Sub-task 8-1: Calculate Risk Free Rate

**Description:** Identify the risk-free rate based on long-term government bond yields.

**Input:**
- Market benchmark (e.g., JGB 10Y)

**Output:**
`8-1-risk-free-rate.json`
- **Phase 1: Research:** Use the initial financial and market research for local risk-free rate benchmarks (e.g., 10-year bond yields).

**Detailed Steps:**
1. Identify the 10-year Government Bond yield.
2. Define the baseline risk-free rate for each of the 120 months.
3. **Project 120-month values.**

#### Sub-task 8-2: Calculate Market Risk Premium

**Description:** Determine the monthly expected return of the market over the risk-free rate.

**Input:**
- 7-1-risk-free-rate.json

**Output:**
`8-2-market-risk-premium.json`

**Detailed Steps:**
1. Research historical market returns for the target region.
2. Subtract the risk-free rate from the expected market return to derive the Market Risk Premium (MRP) for each month.
3. **Formula:** `MRP_m = Expected Market Return_m - Risk-Free Rate_m`.
4. **Project 120-month values.**

#### Sub-task 8-3: Calculate Levered Beta (Equity Beta)

**Description:** Determine the monthly levered beta for the company based on peer comparisons.

**Input:**
- Peer company benchmarks
- 3-1-debt-assumptions.json

**Output:**
- `8-3-levered-beta.json`

**Detailed Steps:**
1. Select a set of comparable public companies.
2. Pull their levered betas and calculate the average or median.
3. Adjust for the target company's specific operating leverage for each of the 120 months.
4. **Project 120-month values.**

#### Sub-task 8-4: Calculate Unlevered Beta (Asset Beta)

**Description:** Remove the effect of leverage to find the monthly pure business risk beta.

**Input:**
- 7-3-levered-beta.json
- 2-6-tax-assumptions.json

**Output:**
- `8-4-unlevered-beta.json`

**Detailed Steps:**
1. Pull the average peer levered beta and their average Debt-to-Equity ratios.
2. Unlever the beta using the formula: `Unlevered Beta_m = Levered Beta_avg / (1 + (1 - Tax Rate_m) * (Peer D/E_avg))`.
3. **Project 120-month values.**

#### Sub-task 8-5: Calculate Equity Risk Premium

**Description:** Apply Beta to the Market Risk Premium to find the specific monthly equity risk.

**Input:**
- 7-2-market-risk-premium.json
- 7-4-unlevered-beta.json

**Output:**
- `8-5-equity-risk-premium.json`

**Detailed Steps:**
1. Re-lever the beta using the target company's projected monthly D/E ratio (from Task 3).
2. **Formula:** `Levered Beta_m = Unlevered Beta_m * (1 + (1 - Tax Rate_m) * (Target D/E_m))`.
3. Multiply the re-levered Beta by the Market Risk Premium: `ERP_m = Beta_m * MRP_m`.
4. **Project 120-month values.**

#### Sub-task 8-6: Calculate Size Risk Premium

**Description:** Additional monthly risk premium for small-cap companies.

**Output:**
- `8-6-size-risk-premium.json`

**Detailed Steps:**
1. **Apply Benchmark Statistics:** Use long-term averages (2.0% - 12.0% depending on stage).
2. **Project 120-month values.**

#### Sub-task 8-7: Calculate Illiquidity Risk Premium

**Description:** Monthly premium for private or illiquid assets.

**Output:**
- `8-7-illiquidity-risk-premium.json`

**Detailed Steps:**
1. **Apply Average Benchmarks:** Use a typical mean of 3.0% for private asset risk.
2. **Project 120-month values.**

#### Sub-task 8-8: Calculate New Business Risk Premium

**Description:** Monthly premium for startup or new business uncertainty.

**Input:**
- Sub-task 1-15 (Funding Roadmap)

**Output:**
- `8-8-new-business-risk-premium.json`

**Detailed Steps:**
1. **Apply Stage-Based Benchmarks:** Set premium based on month-specific funding stage (Seed: 40%, Series A: 30%, Series B: 25%, etc.).
2. **Project 120-month values.**

#### Sub-task 8-9: Calculate Cost of Equity

**Description:** Sum the monthly risk-free rate and all risk premiums.

**Input:**
- 7-1-risk-free-rate.json to 7-8-new-business-risk-premium.json

**Output:**
- `8-9-cost-of-equity.json`

**Detailed Steps:**
1. **Formula:** `Re_m = 7-1_m + 7-5_m + 7-6_m + 7-7_m + 7-8_m`.
2. **Project 120-month values.**

#### Sub-task 8-10: Calculate Cost of Debt

**Description:** Monthly after-tax cost of borrowing.

**Input:**
- 3-3-interest-assumptions.json
- 2-6-tax-assumptions.json

**Output:**
- `8-10-cost-of-debt.json`

**Detailed Steps:**
1. **Formula:** `Rd_m = Pre-tax Kd_m * (1 - Tax Rate_m)`.
2. **Project 120-month values.**

#### Sub-task 8-11: Define Capital Structure

**Description:** Target weight of debt and equity for each month.

**Input:**
- 3-2-equity-assumptions.json
- 5-57-bs-grid.json

**Output:**
- `8-11-capital-structure.json`

**Detailed Steps:**
1. Calculate the weight of Equity and Debt for each of the 120 months based on the BS Grid and Funding Roadmap.
2. **Formula:** `Weight of Equity_m = Equity_m / (Equity_m + Debt_m)`.
3. **Project 120-month values.**

#### Sub-task 8-12: Calculate Weighted Average Cost of Capital (WACC)

**Description:** Calculate the monthly overall WACC based on capital structure weights.

**Input:**
- 7-9-cost-of-equity.json
- 7-10-cost-of-debt.json
- 7-11-capital-structure.json

**Output:**
- `8-12-wacc.json`

**Detailed Steps:**
1. **Formula:** `WACC_m = (Equity Weight_m * Re_m) + (Debt Weight_m * Rd_m)`.
2. **Project 120-month values.**

#### Sub-task 8-13: Define Hurdle Rate Multiple between WACC and Discount Rate

**Description:** Ratio of required equity return to WACC.

**Input:**
- 1-1-revenue-growth.json

**Output:**
- `8-13-wacc-discount-rate-multiple.json`

**Detailed Steps:**
1. Define the strategic hurdle multiple (e.g., 2.37x).
2. **Project 120-month values.**

#### Sub-task 8-14: Calculate Discount Rate

**Description:** Finalize the monthly discount rate applied to cash flows.

**Input:**
- 7-12-wacc.json
- 7-13-wacc-discount-rate-multiple.json

**Output:**
- `8-14-discount-rate.json`

**Detailed Steps:**
1. **Formula:** `Discount Rate_m = WACC_m * 7-13_m`.
2. Calculate monthly discount factors.
3. **Project 120-month values.**

### Task 9: Perform Valuation (DCF)

**Process Dependencies:**
- **Task 6 (Cash Flow):** Unlevered Free Cash Flow (UFCF) derived from OCFI and ICFI.
- **Task 8 (Cost of Capital):** Discount rate and WACC.

#### Sub-task 9-1: Calculate Free Cash Flow (FCF)
**Output:** `9-1-free-cash-flow.json`

**Detailed Steps:**
1. Retrieve component CF files (6-1 through 6-64).
2. Sum OCF and ICF for each month.
3. Project 120-month values.

#### Sub-task 9-2: Calculate Monthly Discount Rate

**Description:** Calculate the 120-month monthly discount rate series based on the annual WACC from Task 4.

**Input:**
- 7-14-discount-rate.json

**Output:**
- `9-2-dcf-discount-rate.json`

**Detailed Steps:**
1. Retrieve the annual **Discount Rate** from Sub-task 8-14.
2. Convert to monthly compounded rate: `r_m = (1 + R_annual)^(1/12) - 1`.
3. **Project 120-month values.**

#### Sub-task 9-3: Calculate Discount Factors

**Description:** Calculate the monthly discount factors based on the referenced discount rate from 8-2.

**Input:**
- 8-2-dcf-discount-rate.json

**Output:**
- `9-3-dcf-discount-factors.json`

**Detailed Steps:**
1. For each month `t` from 1 to 120, calculate: `DF_t = 1 / (1 + r_m)^t`.
2. **Project 120-month values.**

#### Sub-task 9-4: Calculate Present Value of FCF

**Description:** Apply discount factors to forecasted FCF.

**Input:**
- 8-1-free-cash-flow.json
- 8-3-dcf-discount-factors.json

**Output:**
- `9-4-dcf-pv-fcf.json`

**Detailed Steps:**
1. Multiply monthly **FCF** by **Discount Factor**.
2. **Project 120-month values.**

#### Sub-task 9-5: Define Terminal Growth Rate (g)

**Description:** Establish the expected long-term perpetual growth rate (g) for each month.

**Output:**
- `9-5-dcf-terminal-growth-rate.json`

**Dependencies:**
- **Phase 7: Market:** Use the long-term market growth projections and maturity assessment to justify the terminal growth rate.
- **Phase 1: Research:** Use macro trends (GDP, Inflation) found in the initial research.

  **Detailed Steps:**
  1. **Research Macroeconomic Indicators:** Perform a deep search for the long-term **nominal GDP growth rate** and **inflation rate** (Consumer Price Index) for the target region (e.g., Japan, US, Global). These serve as the logical upper bound and baseline for the terminal growth rate.
  2. **Apply Regional & Industry Benchmarks:** Determine the sustainable perpetuity growth rate ($g$) based on the following guidelines:
      - **General Range:** Typically 0% to 3%.
      - **Regional Context:** Japan (Domestic): 0% to 1%; Global/US: 2% to 3%.
      - **Industry Lifecycle:** Growth/Stable industries: 1% to 2.5% (approx. inflation rate); Mature/Declining: 0% or negative (e.g., -1%).
  3. **Adhere to Absolute Constraints:**
      - **Rule 1:** The rate MUST NOT exceed the long-term nominal GDP growth rate of the economy.
      - **Rule 2:** Use the inflation rate as a conservative proxy for price pass-through, rather than assuming real business expansion in perpetuity.
4. **Assume Conservative Stance:** Given the extreme sensitivity of Terminal Value to $g$ (where a 0.5% shift drastically impacts valuation), prioritize a conservative (lower) estimate to prevent overvaluation.
5. **Project 120-month values.**

#### Sub-task 9-6: Calculate Terminal Value (TV)

**Description:** Calculate the Terminal Value at month `m`.

**Input:**
- 8-1-free-cash-flow.json
- 8-2-dcf-discount-rate.json
- 8-5-dcf-terminal-growth-rate.json

**Output:**
- `9-6-dcf-terminal-value.json`

**Detailed Steps:**
1. Retrieve the monthly **FCF** and **Discount Rate**.
2. Retrieve the **Terminal Growth Rate (g)** from Sub-task 9-5.
3. **Formula:** `TV_m = [ (FCF_m * 12) * (1 + g_m) ] / (r_annual - g_m)`.
4. **Project 120-month values.**

#### Sub-task 9-7: Calculate Enterprise Value (EV)

**Description:** Monthly trajectory of total core value.

**Input:**
- Sub-task 9-4 (PV of FCF)
- Sub-task 9-6 (Terminal Value)
- Sub-task 9-3 (Discount Factors)

**Output:**
- `9-7-dcf-enterprise-value.json`

**Detailed Steps:**
1. **Formula:** `EV_m = Σ (PV_FCF) + (TV_m * DF_m)`.
2. **Project 120-month values.**

#### Sub-task 9-8: Calculate Net Debt

**Description:** Monthly total debt minus cash.

**Input:**
- 3-1-debt-assumptions.json
- Sub-task 5-40 (Short Term Debt)
- Sub-task 5-52 (Long Term Debt)

**Output:**
- `9-8-dcf-net-debt.json`

**Detailed Steps:**
1. **Formula:** `Net Debt_m = (5-40_m + 5-41_m + 5-52_m) - 5-1_m`.
2. **Project 120-month values.**

#### Sub-task 9-9: Calculate Minority Interest

**Description:** Portion of subsidiaries owned by minority shareholders.

**Output:**
- `9-9-dcf-minority-interest.json`

**Detailed Steps:**
1. Retrieve value from Task 5 BS.
2. **Project 120-month values.**

#### Sub-task 9-10: Calculate Preferred Equity

**Description:** Value of preferred stock outstanding.

**Output:**
- `9-10-dcf-preferred-equity.json`

**Detailed Steps:**
1. Retrieve value from Task 5 BS.
2. **Project 120-month values.**

#### Sub-task 9-11: Calculate Equity Method Investments

**Description:** Value of investments in associates.

**Output:**
- `9-11-dcf-equity-method-investments.json`

**Detailed Steps:**
1. Retrieve value from Task 5 BS.
2. **Project 120-month values.**

#### Sub-task 9-12: Calculate Enterprise to Equity Bridge

**Description:** Bridge EV to Equity Value.

**Input:**
- Sub-task 9-7 (Enterprise Value)
- 8-8-dcf-net-debt.json
- Sub-task 9-9 (Minority Interest)
- Sub-task 9-10 (Preferred Equity)
- Sub-task 9-11 (Equity Method Investments)

**Output:**
- `9-12-dcf-enterprise-to-equity-bridge.json`

**Detailed Steps:**
1. **Formula:** `Equity Value_m = 8-7_m - 8-8_m - 8-9_m - 8-10_m + 8-11_m`.
2. **Project 120-month values.**

#### Sub-task 9-13: Derive Equity Value

**Description:** Finalize monthly Equity Value from the bridge.

**Input:**
- Sub-task 9-12 (Enterprise to Equity Bridge)

**Output:**
- `9-13-dcf-equity-value.json`

**Detailed Steps:**
1. Extract the final Equity Value trajectory from the bridge.
2. **Project 120-month values.**

#### Sub-task 9-14: Calculate Value Per Share

**Description:** Finalize the DCF-based share price trajectory.

**Input:**
- Sub-task 9-13 (Equity Value)
- Sub-task 10-2 (Diluted Shares)

**Output:**
- `9-14-dcf-value-per-share.json`

**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

#### Sub-task 9-15: Perform Sensitivity Analysis

**Description:** Generate scenario analysis (Bull/Base/Bear) and standard sensitivity tables.

**Input:**
- 8-13-dcf-equity-value.json
- 8-6-dcf-terminal-value.json

**Output:**
- `9-15-dcf-sensitivity-analysis.json`

**Detailed Steps:**
1. Vary key drivers (Revenue Growth, WACC, Terminal Growth) by +/- 10-20%.
2. Calculate the impact on Equity Value.
3. Generate sensitivity tables showing Equity Value across different WACC and terminal growth rate combinations.
4. **Project 120-month values.**

### Task 10: Perform Valuation (PER)

#### Sub-task 10-1: Select Benchmark PER Multiple

**Description:** Identify the representative PER multiple based on comparable public companies.

**Output:** 
- `10-1-per-benchmark.json`

**Dependencies:**
- **Phase 8: Competition:** Use the identified competitors and peers as the basis for the comparable company peer group.

**Detailed Steps:**
1. Identify a peer group of public companies.
2. Retrieve their current PER multiples.
3. Determine the median/average benchmark PER for the target sector.
4. **Project 120-month values.**

#### Sub-task 10-2: Calculate Diluted Shares Outstanding

**Description:** Monthly trajectory of diluted shares factoring in options/warrants.

**Input:** 
- 19-5-multi-round-captable.json

**Output:** 
- `10-2-per-diluted-shares.json`

**Detailed Steps:**
1. Sum issued shares and all dilutive securities (ESOP, warrants).
2. **Project 120-month values.**

#### Sub-task 10-3: Apply IPO Discount to PER Multiple

**Description:** Apply a discount to the benchmark multiple to reflect private market illiquidity.

**Output:** 
- `10-3-per-ipo-discount.json`

**Detailed Steps:**
1. Define the IPO Discount (typically 70% of public multiple).
2. **Project 120-month values.**

#### Sub-task 10-4: Calculate Effective PER after Discount

**Description:** Derive the final effective PER multiple.

**Input:** 
- `10-1-per-benchmark.json`
- `10-3-per-ipo-discount.json`

**Output:** 
- `10-4-per-effective-multiple.json`

**Detailed Steps:**
1. **Formula:** `Effective PER_m = Benchmark PER_m * (1 - IPO Discount_m)`.
2. **Project 120-month values.**

#### Sub-task 10-5: Identify Net Profit for Valuation Base

**Description:** Pull the net profit to be used as the valuation base.

**Input:** 
- 4-68-net-profit.json

**Output:** 
- `10-5-per-net-profit-base.json`

**Detailed Steps:**
1. Retrieve monthly Net Profit from the 120-month P&L.
2. **Project 120-month values.**

#### Sub-task 10-6: Derive Equity Value from PER

**Description:** Multiply the effective PER by the net profit.

**Input:** 
- `10-4-per-effective-multiple.json`
- `10-5-per-net-profit-base.json`

**Output:** 
- `10-6-per-equity-value.json`

**Detailed Steps:**
1. **Formula:** `Equity Value_m = Effective PER_m * Net Profit_m`.
2. **Project 120-month values.**

#### Sub-task 10-7: Calculate Value Per Share

**Description:** Finalize the PER-based share price trajectory.

**Input:** 
- `10-6-per-equity-value.json`
- `10-2-per-diluted-shares.json`

**Output:** 
- `10-7-per-value-per-share.json`

**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

### Task 11: Perform Valuation (PBR)

#### Sub-task 11-1: Select Benchmark PBR Multiple
**Description:** Identify representative PBR multiple from comparable companies.
**Output:** 
- `11-1-pbr-benchmark.json`

**Dependencies:**
- **Phase 8: Competition:** Select comparable peers from the competitive landscape analysis.
**Detailed Steps:**
1. Identify peer group.
2. Determine median PBR multiple.
3. **Project 120-month values.**

#### Sub-task 11-2: Apply IPO Discount to PBR Multiple
**Description:** Adjust for private market status.
**Output:** 
- `11-2-pbr-ipo-discount.json`
**Detailed Steps:**
1. Define IPO Discount.
2. **Project 120-month values.**

#### Sub-task 11-3: Calculate Effective PBR after Discount
**Description:** Derive final PBR multiple.
**Output:** 
- `11-3-pbr-effective-multiple.json`
**Detailed Steps:**
1. **Formula:** `Effective PBR_m = Benchmark PBR_m * (1 - IPO Discount_m)`.
2. **Project 120-month values.**

#### Sub-task 11-4: Identify Total Net Assets for Valuation Base
**Description:** Pull book value from Balance Sheet.
**Input:** 
- 5-57-bs-grid.json
**Output:** 
- `11-4-pbr-net-assets-base.json`
**Detailed Steps:**
1. Retrieve monthly Total Net Assets from the BS.
2. **Project 120-month values.**

#### Sub-task 11-5: Derive Equity Value from PBR
**Description:** Multiply effective PBR by net assets.
**Output:** 
- `11-5-pbr-equity-value.json`
**Detailed Steps:**
1. **Formula:** `Equity Value_m = Effective PBR_m * Net Assets_m`.
2. **Project 120-month values.**

#### Sub-task 11-6: Calculate Value Per Share
**Description:** Final PBR-based share price.
**Output:** 
- `11-6-pbr-value-per-share.json`
**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

### Task 12: Perform Valuation (EV/EBITDA)

#### Sub-task 12-1: Select Benchmark EV/EBITDA Multiple
**Description:** Identify representative EBITDA multiple.
**Output:** 
- `12-1-ev-ebitda-benchmark.json`
**Detailed Steps:**
1. Identify peer benchmarks.
2. **Project 120-month values.**

#### Sub-task 12-2: Apply IPO Discount to EV/EBITDA Multiple
**Description:** Adjust for liquidity.
**Output:** 
- `12-2-ev-ebitda-ipo-discount.json`
**Detailed Steps:**
1. Define Discount.
2. **Project 120-month values.**

#### Sub-task 12-3: Calculate Effective EV/EBITDA
**Description:** Final multiple after discounts.
**Output:** 
- `12-3-ev-ebitda-effective-multiple.json`
**Detailed Steps:**
1. **Formula:** `Effective EV/EBITDA_m = Benchmark Multiple_m * (1 - Discount_m)`.
2. **Project 120-month values.**

#### Sub-task 12-4: Identify EBITDA for Valuation Base
**Description:** Pull EBITDA from P&L.
**Output:** 
- `12-4-ev-ebitda-base.json`
**Detailed Steps:**
1. Retrieve monthly EBITDA from P&L.
2. **Project 120-month values.**

#### Sub-task 12-5: Derive Enterprise Value from EV/EBITDA
**Description:** Imply EV based on EBITDA multiples.
**Output:** 
- `12-5-ev-ebitda-enterprise-value.json`
**Detailed Steps:**
1. **Formula:** `Enterprise Value_m = Effective Multiple_m * EBITDA_m`.
2. **Project 120-month values.**

#### Sub-task 12-6: Calculate Net Debt
**Description:** Monthly total debt minus cash.
**Output:** 
- `12-6-ev-ebitda-net-debt.json`
**Detailed Steps:**
1. **Formula:** `Net Debt_m = (Term Debt_m + Short Term Debt_m) - Cash_m`.
2. **Project 120-month values.**

#### Sub-task 12-7: Calculate Minority Interest
**Description:** Portion of subsidiaries owned by minority shareholders.
**Output:** 
- `12-7-ev-ebitda-minority-interest.json`
**Detailed Steps:**
1. Retrieve value from Balance Sheet.
2. **Project 120-month values.**

#### Sub-task 12-8: Calculate Preferred Equity
**Description:** Value of preferred stock outstanding.
**Output:** 
- `12-8-ev-ebitda-preferred-equity.json`
**Detailed Steps:**
1. Retrieve value from Balance Sheet.
2. **Project 120-month values.**

#### Sub-task 12-9: Calculate Equity Method Investments
**Description:** Value of investments in associates.
**Output:** 
- `12-9-ev-ebitda-equity-method-investments.json`
**Detailed Steps:**
1. Retrieve value from Balance Sheet.
2. **Project 120-month values.**

#### Sub-task 12-10: Calculate Enterprise to Equity Bridge
**Description:** Bridge EV to Equity Value.
**Input:** 
- `12-5-ev-ebitda-enterprise-value.json`
- `12-6-ev-ebitda-net-debt.json`
- `12-7-ev-ebitda-minority-interest.json`
- `12-8-ev-ebitda-preferred-equity.json`
- `12-9-ev-ebitda-equity-method-investments.json`
**Output:** 
- `12-10-ev-ebitda-enterprise-to-equity-bridge.json`
**Detailed Steps:**
1. **Formula:** `Equity Value_m = Enterprise Value_m - Net Debt_m - Minority Interest_m - Preferred Equity_m + Equity Method Investments_m`.
2. **Project 120-month values.**

#### Sub-task 12-11: Derive Equity Value
**Description:** Finalize monthly Equity Value from the bridge.
**Input:** 
- `12-10-ev-ebitda-enterprise-to-equity-bridge.json`
**Output:** 
- `12-11-ev-ebitda-equity-value.json`
**Detailed Steps:**
1. Extract the final Equity Value trajectory.
2. **Project 120-month values.**

#### Sub-task 12-12: Calculate Value Per Share
**Description:** Final EBITDA-based share price.
**Input:** 
- `12-11-ev-ebitda-equity-value.json`
- `10-2-per-diluted-shares.json`
**Output:** 
- `12-12-ev-ebitda-value-per-share.json`
**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

### Task 13: Perform Valuation (PSR)

#### Sub-task 13-1: Select Benchmark PSR Multiple

**Description:** Identify the representative PSR multiple based on comparable public companies.

**Output:** 
- `13-1-psr-benchmark.json`

**Dependencies:**
- **Phase 8: Competition:** Select comparable revenue-based peers from the competitive analysis.

**Detailed Steps:**
1. Identify a peer group of public companies.
2. Retrieve their current PSR (Price-to-Sales Ratio).
3. Determine the median/average benchmark PSR for the target sector.
4. **Project 120-month values.**

#### Sub-task 13-2: Apply IPO Discount to PSR Multiple

**Description:** Apply a discount to the benchmark multiple to reflect private market illiquidity.

**Output:** 
- `13-2-psr-ipo-discount.json`

**Detailed Steps:**
1. Define the IPO Discount (typically 70% of public multiple).
2. **Project 120-month values.**

#### Sub-task 13-3: Calculate Effective PSR

**Description:** Derive the final effective PSR multiple.

**Input:** 
- `13-1-psr-benchmark.json`
- `13-2-psr-ipo-discount.json`

**Output:** 
- `13-3-psr-effective-multiple.json`

**Detailed Steps:**
1. **Formula:** `Effective PSR_m = Benchmark PSR_m * (1 - IPO Discount_m)`.
2. **Project 120-month values.**

#### Sub-task 13-4: Identify Revenue for Valuation Base

**Description:** Pull the revenue to be used as the valuation base.

**Input:** 
- 4-1-revenue.json

**Output:** 
- `13-4-psr-revenue-base.json`

**Detailed Steps:**
1. Retrieve monthly Revenue from the 120-month P&L.
2. **Project 120-month values.**

#### Sub-task 13-5: Derive Equity Value from PSR

**Description:** Multiply the effective PSR by the revenue.

**Input:** 
- `13-3-psr-effective-multiple.json`
- `13-4-psr-revenue-base.json`

**Output:** 
- `13-5-psr-equity-value.json`

**Detailed Steps:**
1. **Formula:** `Equity Value_m = Effective PSR_m * Revenue_m`.
2. **Project 120-month values.**

#### Sub-task 13-6: Calculate Value Per Share

**Description:** Finalize the PSR-based share price trajectory.

**Input:** 
- `13-5-psr-equity-value.json`
- 8-14-dcf-value-per-share.json

**Output:** 
- `13-6-psr-value-per-share.json`

**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

### Task 14: Perform Valuation (PCFR)

#### Sub-task 14-1: Select Benchmark PCFR Multiple

**Description:** Identify representative Price-to-Cash-Flow multiples from peer benchmarks.

**Output:** 
- `14-1-pcfr-benchmark.json`

**Dependencies:**
- **Phase 8: Competition:** Select comparable cash-flow-based peers from the competitive analysis.

#### Sub-task 14-2: Apply IPO Discount to PCFR Multiple

**Description:** Adjust for private market illiquidity.

**Output:** 
- `14-2-pcfr-ipo-discount.json`

#### Sub-task 14-3: Calculate Effective PCFR

**Description:** Final multiple after discounts.

**Output:** 
- `14-3-pcfr-effective-multiple.json`

#### Sub-task 14-4: Identify OCF for Valuation Base

**Description:** Pull Operating Cash Flow from the CF statement.

**Input:** 
- 6-63-net-change-cash.json

**Output:** 
- `14-4-pcfr-operating-cf-base.json`

#### Sub-task 14-5: Derive Equity Value from PCFR

**Description:** Multiply effective PCFR by the cash flow base.

**Output:** 
- `14-5-pcfr-equity-value.json`

#### Sub-task 14-6: Calculate Value Per Share

**Description:** Final PCFR-based share price trajectory.

**Input:** 
- `14-5-pcfr-equity-value.json`
- 8-14-dcf-value-per-share.json

**Output:** 
- `14-6-pcfr-value-per-share.json`

**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

### Task 15: Perform Valuation (Comparable Company Method)

#### Sub-task 15-1: Select Peer Group

**Description:** Identify a set of comparable public companies for relative valuation.

**Output:** 
- `15-1-cca-peer-group.json`

**Dependencies:**
- **Phase 8: Competition:** Ensure the peer group used for CCA matches the strategic competitors identified in Phase 8.

**Detailed Steps:**
1. Identify 5-10 public companies with similar business models, size, and growth profiles to the target.
2. Document Peer Name, Ticker, and rationale for inclusion.
3. **Project 120-month values.**

#### Sub-task 15-2: Calculate Trading Multiples

**Description:** Calculate EV/Revenue, EV/EBITDA, and P/E multiples for the selected peer group.

**Input:** 
- `15-1-cca-peer-group.json`

**Output:** 
- `15-2-cca-trading-multiples.json`

**Detailed Steps:**
1. Retrieve financial data (Enterprise Value, Revenue, EBITDA, Net Income) for peers.
2. Calculate multiples for each peer.
3. Calculate mean and median multiples for the group.
4. **Project 120-month values.**

#### Sub-task 15-3: Adjust for Premiums and Discounts

**Description:** Apply private company discounts or small-cap premiums.

**Input:** 
- `15-2-cca-trading-multiples.json`

**Output:** 
- `15-3-cca-adjustments.json`

**Detailed Steps:**
1. Apply Private Company Discount (typically 15-30% for illiquidity).
2. **Project 120-month values.**

#### Sub-task 15-4: Determine Appropriate Multiple Range

**Description:** Set the low, median, and high multiple brackets for the target company.

**Input:** 
- `15-3-cca-adjustments.json`

**Output:** 
- `15-4-cca-multiple-range.json`

**Detailed Steps:**
1. Establish the "Benchmark Multiple" bracket for each period.
2. **Project 120-month values.**

#### Sub-task 15-5: Apply Multiples to Target Metrics

**Description:** Multiply target financial metrics by the selected multiple ranges.

**Input:** 
- `15-4-cca-multiple-range.json`
- 4-1-revenue.json

**Output:** 
- `15-5-cca-apply-multiples.json`

**Detailed Steps:**
1. Apply the adjusted multiples to the target's projected metrics.
2. Derive implied Enterprise Value trajectory.
3. **Project 120-month values.**

#### Sub-task 15-6: Derive Equity Value from CCA

**Description:** Convert Enterprise Value to Equity Value by adjusting for net debt.

**Input:** 
- `15-5-cca-apply-multiples.json`
- 8-8-dcf-net-debt.json

**Output:** 
- `15-6-cca-equity-value.json`

**Detailed Steps:**
1. **Formula:** `Equity Value_m = Enterprise Value_m - Net Debt_m`.
2. **Project 120-month values.**

#### Sub-task 15-7: Calculate Value Per Share

**Description:** Finalize the CCA-based share price trajectory.

**Input:** 
- `15-6-cca-equity-value.json`
- 8-14-dcf-value-per-share.json

**Output:** 
- `15-7-cca-value-per-share.json`

**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

### Task 16: Perform Valuation (Comparable Transaction Method)

#### Sub-task 16-1: Identify Comparable Transactions

**Description:** Search recently similar M&A or funding deals.

**Output:** 
- `16-1-cta-comparable-transactions.json`

**Dependencies:**
- **Phase 8: Competition:** Precedent transactions should be searched based on the key exits and funding rounds of competitors in Phase 8.

**Detailed Steps:**
1. Identify 3-5 relevant precedent transactions.
2. Document deal size, date, and implied multiples.
3. **Project 120-month values.**

#### Sub-task 16-2: Gather Transaction Financial Data

**Description:** Extract metrics for the selected deals.

**Input:** 
- `16-1-cta-comparable-transactions.json`

**Output:** 
- `16-2-cta-transaction-financials.json`

**Detailed Steps:**
1. Collect historical Revenue, EBITDA, and Net Income for each transaction company at the time of the deal.
2. Verify Enterprise Value (Deal Price + Net Debt).
3. **Project 120-month values.**

#### Sub-task 16-3: Calculate Transaction Multiples

**Description:** Compute multiples for comparable deals.

**Output:** 
- `16-3-cta-transaction-multiples.json`

**Detailed Steps:**
1. Calculate EV/Revenue, EV/EBITDA, and P/E for each deal.
2. Note any premiums paid for control.
3. **Project 120-month values.**

#### Sub-task 16-4: Select Representative Multiple

**Description:** Median/Average check for target application.

**Input:** 
- `16-3-cta-transaction-multiples.json`

**Output:** 
- `16-4-cta-representative-multiple.json`

**Detailed Steps:**
1. Determine the appropriate multiple bracket based on transaction benchmarks.
2. **Project 120-month values.**

#### Sub-task 16-5: Apply Multiple to Target Financials

**Description:** Multiply multiple by operating metrics.

**Output:** 
- `16-5-cta-apply-multiple.json`

**Detailed Steps:**
1. Apply the transaction multiples to the target's projected metrics.
2. Derive implied Enterprise Value trajectory.
3. **Project 120-month values.**

#### Sub-task 16-6: Derive Equity Value from CTA

**Description:** Final value utilizing the CTA method.

**Input:** 
- `16-5-cta-apply-multiple.json`
- 8-8-dcf-net-debt.json

**Output:** 
- `16-6-cta-equity-value.json`

**Detailed Steps:**
1. **Formula:** `Equity Value_m = Enterprise Value_m - Net Debt_m`.
2. **Project 120-month values.**

#### Sub-task 16-7: Calculate Value Per Share

**Description:** Calculate final CTA-based share price.

**Input:**
- `16-6-cta-equity-value.json`
- 8-14-dcf-value-per-share.json

**Output:**
- `16-7-cta-value-per-share.json`

**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**

**Description:** Final CTA-based share price trajectory.

**Input:** 
- `16-6-cta-equity-value.json`
- 8-14-dcf-value-per-share.json

**Output:** 
- `16-7-cta-value-per-share.json`

**Detailed Steps:**
1. **Formula:** `Value Per Share_m = Equity Value_m / Diluted Shares_m`.
2. **Project 120-month values.**


### Task 17: Summarize Valuation

**Process Dependencies:**
- **Tasks 9-15:** All valuation methodology sub-tasks must be processed to determine the average or selected FMV.

#### Sub-task 17-1: Compare Valuations

**Description:** Cross-compare monthly results from all methodologies.

**Input:**
- Task 8 (DCF)
- Tasks 9-15 (PER, PBR, EV/EBITDA, PSR, PCFR, CCA, CTA)

**Output:**
- `17-1-compare-valuations.json`

**Detailed Steps:**
1. Consolidate 120-month results from all valuation JSONs.
2. Side-by-side comparison.
3. **Project 120-month values.**

#### Sub-task 17-2: Calculate Pre-money Valuation

**Description:** Valuation before new capital injections.

**Input:**
- 16-1-compare-valuations.json

**Output:**
- `17-2-pre-money-valuation.json`

**Detailed Steps:**
1. `Equity Value_m - New Funding_m`.
2. **Project 120-month values.**

#### Sub-task 17-3: Finalize Stock Price

**Description:** Determine final valuation and price per share.

**Output:**
- `17-3-finalize-stock-price.json`

**Detailed Steps:**
1. `Equity Value_m / Total Shares Outstanding_m`.
2. **Project 120-month values.**


### Task 18: Calculate Funding Needs

**Process Dependencies:**
- **Task 6 (Cash Flow):** Projected cash gaps determine the magnitude and timing of funding.
- **Task 5 (BS):** Working capital requirements.

#### Sub-task 18-1: Calculate Operating Working Capital

**Description:** Calculate monthly 経常運転資金.

**Input:**
- 5-8-trade-ar.json
- 5-10-merchandise.json
- 5-39-trade-ap.json

**Output:**
- `18-1-operating-working-capital.json`

**Detailed Steps:**
1. **Formula:** `(AR + Inventories) - AP`.
2. **Project 120-month values.**

#### Sub-task 18-2: Calculate Net Working Capital

**Description:** Calculate monthly 正味運転資本.

**Input:**
- Task 5 Current Assets/Liabilities

**Output:**
- `18-2-net-working-capital.json`

**Detailed Steps:**
1. **Formula:** `Non-cash Current Assets - Non-debt Current Liabilities`.
2. **Project 120-month values.**

#### Sub-task 18-3: Calculate Capital Expenditure @BS

**Description:** Calculate 設備投資 trajectories.

**Output:**
- `18-3-capex-bs.json`

**Detailed Steps:**
1. Pull monthly balances for Fixed Assets from Task 5.
2. **Project 120-month values.**

#### Sub-task 18-4: Calculate Development Expenses @BS

**Description:** Calculate 開発費 trajectories.

**Output:**
- `18-4-development-expenses-bs.json`

**Detailed Steps:**
1. Identify monthly balances for Development Expenses (Task 5).
2. **Project 120-month values.**

#### Sub-task 18-5: Calculate R&D Expenses @PL

**Description:** Calculate 研究開発費 trajectories.

**Output:**
- `18-5-rd-expenses-pl.json`

**Detailed Steps:**
1. Identify monthly balances for Research and Development Expenses (Task 4).
2. **Project 120-month values.**

#### Sub-task 18-6: Calculate Max Cumulative Outflow

**Description:** Identify lowest accumulated free cash flow point.

**Input:**
- 5-1-cash-bs.json

**Output:**
- `18-6-lowest-accumulated-fcf.json`

**Dependencies:**
- **Phase 16: Ask:** Use the identified funding trough to justify the target raise amount and timing.

**Detailed Steps:**
1. Sum FCF over 120 months.
2. Identify the peak negative point.
3. **Project 120-month values.**

#### Sub-task 18-7: Calculate Burn Rate

**Description:** Determine monthly cash consumption rate.

**Input:**
- Task 6 Cash Flow

**Output:**
- `18-7-burn-rate.json`

**Detailed Steps:**
1. `Gross Burn = Total Expenditures`.
2. `Net Burn = (Inflows - Outflows)`.
3. **Project 120-month values.**

#### Sub-task 18-8: Calculate Runway Before Fundraising

**Description:** Months of remaining cash before fundraising.

**Input:**
- 5-1-cash-bs.json
- 17-7-burn-rate.json

**Output:**
- `18-8-runway-before-fundraising.json`

**Detailed Steps:**
1. `Runway = Ending Cash / Net Burn`.
2. **Project 120-month values.**

#### Sub-task 18-9: Calculate Target Runway Amounts

**Description:** Funding needed for 6/12/18/24 month runways.

**Output:**
- `18-9-runway-tiers-needed.json`

**Detailed Steps:**
1. Sub-task 18-7 (Burn Rate) used to sum periods.
2. **Project 120-month values.**


### Task 19: Plan Debt Financing from Japan Finance Corporation

**Process Dependencies:**
- **Task 18 (Funding Needs):** The total debt amount is limited by debt capacity and funding gaps.

#### Sub-task 19-1: Plan bank for loan application

**Description:** Plan target bank, loan amount, rates, and repayment schedule for Japan Finance Corporation loans.

**Input:**
- 7-12-wacc.json

**Output:**
- `19-1-loan-bank-plan.json`

**Detailed Steps:**
1. Identify JFC branch and appropriate loan menu.
2. Define loan amount based on 18-month runway need (17-9).
3. Set interest rate and repayment/grace period.
4. Generate monthly repayment schedule.
5. **Project 120-month values.**


### Task 20: Plan Equity Financing

**Process Dependencies:**
- **Task 18 (Funding Needs):** Equity rounds are used to cover the final funding shortfall.
- **Task 17 (Valuation):** Share price for issuance is set by the summarized valuation.

These sub-tasks sequentially build a professional, multi-round Cap Table modeling the evolution of ownership from founding to exit.

#### Sub-task 20-1: Plan Multi-Stage Equity Roadmap

**Description:** Define timing, amount, and valuation for rounds.

**Input:**
- 7-12-wacc.json

**Output:**
- `20-1-funding-roadmap.json`

**Dependencies:**
- **Phase 16: Ask:** The funding roadmap must be consistent with the round terms, valuations, and target raise amounts defined in the 'Ask' phase.

**Detailed Steps:**
1. Define raise dates and amounts for Founding, Seed, Series A, B, and Exit.
2. **Project 120-month values.**

#### Sub-task 20-4: Plan ESOP Expansion Plan

**Description:** Calculate Option Pool Shuffle.

**Output:**
- `20-4-esop-expansion-plan.json`

**Detailed Steps:**
1. Aim for 10-15% post-money pool.
2. **Project 120-month values.**

#### Sub-task 20-5: Calculate Cumulative Dilution

**Description:** Consolidate into professional grid.

**Output:**
- `20-5-multi-round-captable.json`

**Detailed Steps:**
1. Generate professional 2D cap table grid.
2. **Project 120-month values.**

#### Sub-task 20-6: Generate Simple Captable Summary

**Description:** Executive summary of ownership.

**Output:**
- `20-6-simple-captable-summary.json`

**Detailed Steps:**
1. Summary JSON with event, date, valuations, and ownership ratios.
2. **Project 120-month values.**

#### Sub-task 20-7: Reconcile Valuations

**Description:** Reconcile final valuation deltas after ESOP shuffle.

**Output:**
- `20-7-valuation-reconciliation.json`

**Detailed Steps:**
1. Compare effective vs target post-money valuation.
2. **Project 120-month values.**

#### Sub-task 20-8: Establish Strike Price Evolution

**Description:** Estimate stock option exercise price progression.

**Output:**
- `20-8-strike-price-evolution.json`

**Detailed Steps:**
1. Estimate FMV for ordinary shares.
2. **Project 120-month values.**

#### Sub-task 20-9: Write Term Sheet

**Description:** Draft a professional term sheet based on best practices from the `startup-fundraising` skill.

**Output:**
- `20-9-term-sheet.json`

**Detailed Steps:**
1. **Economics First:** Define Pre-money Valuation, Option Pool (prefer post-money sizing or <10% pre-money), and Liquidation Preference (1x non-participating).
2. **Anti-Dilution:** Use broad-based weighted average.
3. **Control Terms:** Define Board Composition (ensure founders maintain majority control early) and Protective Provisions (avoid operational vetoes like budget/hiring approvals).
4. **Vesting:** Set 4-year vesting with 1-year cliff and double-trigger acceleration.
5. **Data Room Readiness:** Ensure all financials and legal docs are ready for due diligence as per standard structure.
6. **Project 120-month values.** (Consistency with the grid)




### Task 21: Analyze Exit and Waterfall

**Process Dependencies:**
- **Task 17 (Valuation):** Exit value at terminal year or specified exit month.
- **Task 20 (Equity Plan):** Dilution and liquidation preference structure from previous rounds.
- **Team Phase:** Initial founder ownership.

#### Sub-task 21-1: Define Exit Scenario and Valuation

**Description:** Project exit month, valuation, and proceeds distribution.

**Output:**
- `21-1-exit-scenario.json`

**Dependencies:**
- **Phase 1: Research:** Use identified acquisition trends and IPO sizes of industry peers.
- **Phase 8: Competition:** Use the exit paths of direct competitors (e.g., M&A by specific incumbents) to justify the exit scenario.

**Detailed Steps:**
1. Define exit scenario (IPO/M&A) and timing.
2. Model liquidation preferences.
3. Generate proceeds distribution waterfall across all share classes.
4. **Project 120-month values.**

#### Sub-task 21-4: Calculate Investor ROI

**Description:** Calculate MOIC and IRR for round participants.

**Output:**
- `21-4-investor-roi.json`

**Detailed Steps:**
1. Calculate individual round returns.
2. **Project 120-month values.**

#### Sub-task 21-5: Calculate Founder Realization

**Description:** Final wealth realization projection for founders.

**Output:**
- `21-5-founder-realization.json`

**Detailed Steps:**
1. Track founder shares and proceeds through the waterfall.
2. **Project 120-month values.**


### Task 22: Calculate PL, BS, CF after fundraising

**Process Dependencies:**
- **Tasks 19 & 19:** New debt and equity inflows must be integrated back into the core statements to reflect interest and cash impacts.

#### Sub-task 22-1: Calculate P&L after fundraising

**Description:** Statements reflecting interest and cash impact from fundraising.

**Output:**
- `22-1-pl-post-fund.json`

**Detailed Steps:**
1. Integrate interest expense from debt and interest income from cash injections.
2. **Project 120-month values.**

#### Sub-task 22-2: Calculate Balance Sheet after fundraising

**Description:** B/S with capital injections and liabilities.

**Output:**
- `22-2-bs-post-fund.json`

**Detailed Steps:**
1. Reflect new cash, debt balances, and equity capital.
2. **Project 120-month values.**

#### Sub-task 22-3: Updated Final Cash Flow

**Description:** C/F with financing inflows and debt service.

**Output:**
- `22-3-cf-post-fund.json`

**Detailed Steps:**
1. Reflect financing activities in the 120-month trajectory.
2. **Project 120-month values.**

#### Sub-task 22-4: Verify Financial Health

**Description:** Final audit for positive cash and buffer constraints.

**Output:**
- `22-4-verify-financial-health.json`

**Detailed Steps:**
1. Audit for no negative cash months.
2. Verify buffer compliance.
3. **Project 120-month values.**


### Task 23: Generate Google Sheets

**Process Dependencies:**
- **Tasks 4, 5, 6:** All P&L, BS, and CF sub-tasks must be finalized and exported to the target directory.
- **Task 0:** The spreadsheet must be initialized with the master template structure.

#### Sub-task 23-2: Populate P&L rows

**Description:** Populate P&L rows to the "all" tab with Google Sheets formulas.

**Input:**
- 21-1-pl-post-fund.json

**Output:**
- `23-2-gs-pnl-section.json`

**Detailed Steps:**
1. **Row Mapping (1-77) - Formula Mandate:** Populate the P&L rows in the "all" tab using the following logic in Column G (then dragged to DV):
    - **Revenue (Row 4):** SUM calculated from orders/revenue data.
    - **Net Sales (Row 6):** Formula `=G4-G5`.
    - **Gross Profit (Row 21):** Formula `=G6-G20`.
    - **Total Operating Expenses (SG&A) (Row 59):** Formula `=SUM(G23:G58)`.
    - **Operating Profit (or Loss) (Row 60):** Formula `=G21-G59`.
    - **Ordinary Profit (or Loss) (Row 68):** Formula `=G60+SUM(G61:G64)-SUM(G65:G67)`.
    - **Net Profit (Row 77):** Formula `=G73-G74` (Income Before Tax - Income Taxes).
2. Use `update-range` with `formula` input to ensure the sheet remains dynamic.

#### Sub-task 23-3: Populate Balance Sheet rows

**Description:** Populate Balance Sheet rows to the "all" tab with formulas.

**Input:**
- 21-2-bs-post-fund.json

**Output:**
- `23-3-gs-bs-section.json`

**Detailed Steps:**
1. **Row Mapping (79-171) - Formula Mandate:** Populate the BS rows in the "all" tab using the following logic in Column G:
    - **Total Current Assets (Row 105):** Formula `=SUM(G81:G104)`.
    - **Total Non-current Assets (Row 122):** Formula `=SUM(G107:G121)`.
    - **Total Assets (Row 129):** Formula `=G105+G122+G128`.
    - **Total Current Liabilities (Row 145):** Formula `=SUM(G132:G144)`.
    - **Total Liabilities (Row 149):** Formula `=G145+G148`.
    - **Total Net Assets (Equity) (Row 170):** Formula `=SUM(G151:G169)`.
    - **Balance Check (Row 171):** Formula `=G149+G170`. Must match Row 129.
2. Ensure opening balances for Month 2 point to the results of Month 1.

#### Sub-task 23-4: Populate Cash Flow rows

**Description:** Populate Cash Flow rows to the "all" tab with formulas.

**Input:**
- 21-3-cf-post-fund.json

**Output:**
- `23-4-gs-cf-section.json`

**Detailed Steps:**
1. **Row Mapping (173-259) - Formula Mandate:** Populate the CF rows in the "all" tab using the following logic:
    - **Net Profit (Row 177):** Reference P&L via `=G77`.
    - **Operating Cash Flow (Before NWC) (Row 188):** Formula `=SUM(G177:G187)`.
    - **Change in Net Working Capital (Row 204):** Formula `=SUM(G190:G203)`.
    - **Net Cash from Operating Activities (Row 221):** Formula `=G188+G204`.
    - **Net Cash from Investing Activities (Row 240):** Formula `=G227-G239`.
    - **Net Cash from Financing Activities (Row 255):** Formula `=G248+G254`.
    - **Net Increase (Decrease) in Cash (Row 257):** Formula `=G221+G240+G255+G256`.
    - **Closing Cash Balance (Row 259):** Formula `=G257+G258`.
2. Link Month 2 Opening Cash (`H258`) to Month 1 Closing Cash (`G259`).

#### Sub-task 23-5: Populate Captable Tab

**Description:** Populate cap table tabs.

**Input:**
- 19-5-multi-round-captable.json
- 19-6-simple-captable-summary.json

**Output:**
- `23-5-gs-captable.json`
- `23-6-gs-captable-summary.json`

**Detailed Steps:**
1. Use the `google-sheets` skill to export the cap table grid and summary to the "captable" tab.
2. **Project 120-month values.**

#### Sub-task 23-7: Populate Valuation Comparison Tab

**Description:** Populate valuation methodology comparisons.

**Input:**
- 16-1-compare-valuations.json

**Output:**
- `23-7-gs-valuation-comparison.json`

**Detailed Steps:**
1. Use the `google-sheets` skill to export the valuation methodology comparison grid to the "valuation" tab.
2. **Project 120-month values.**

#### Sub-task 23-8: Populate Orders Tab

**Description:** Populate detailed revenue driver data.

**Output:**
- `23-8-gs-orders.json`

**Detailed Steps:**
1. Use the `google-sheets` skill to export the order list or detailed revenue driver data to the "orders" tab.
2. **Project 120-month values.**

### Task 24: Finalize Financial Plan

**Process Dependencies:**
- **Task 23 (Sheet Population):** The model must be fully populated and consistent.
- **Tasks 17-21:** Qualitative summaries, fundraising impacts, and ratio analysis must be reconciled with the final narrative.

#### Sub-task 24-1: Write Financial Story

**Description:** Draft final narrative summary.

**Output:**
- `24-1-write-financial-story.json`

**Dependencies:**
- **Phase 14: Insight:** The financial story must prove how the "Contrarian Hypothesis" translates into superior economic performance.
- **Phase 12: Purpose:** Align the narrative with the long-term vision and mission impact.

**Detailed Steps:**
1. Write 10-year comprehensive narrative.
2. **Project 120-month values.**

---

## Chart of Accounts (勘定科目)

Standardized categories for financial statement generation. Use these exact labels in Japanese and English for consistency across all outputs and spreadsheet tabs.

### Profit & Loss Statement (損益計算書)
- **Revenue (売上高)**
    - Revenue (売上高)
    - Sales returns (売上戻り高)
    - **Net sales (純売上高)**
- **Cost of Goods Sold (売上原価)**
    - Beginning inventory of merchandise (期首商品棚卸)
    - Purchases of merchandise (当期商品仕入)
    - Transfer to other account(Merchandise) (他勘定振替高(商))
    - Ending inventory of merchandise (期末商品棚卸)
    - Cost of purchased goods sold (商品売上原価)
    - Beginning inventory of finished goods (期首製品棚卸)
    - Cost of finished goods (当期製品製造原価)
    - Transfer to other account(finished goods) (他勘定振替高(製))
    - Ending inventory of finished goods (期末製品棚卸)
    - Cost of finished goods sold (製品売上原価)
- **Gross profit (売上総利益)** [Ref: Gross profit (or loss) / 売上総損益金額]
- **SG&A expenses (販売管理費)**
    - Directors’ compensation (役員報酬)
    - Directors’ bonuses (役員賞与)
    - Salaries (給与手当)
    - Bonuses (賞与)
    - Share-based compensation expense (株式報酬費)
    - Legal welfare expense (法定福利費)
    - Welfare expense (福利厚生費)
    - Recruiting expense (採用費)
    - Training expense (研修費)
    - Subcontract expense (外注費)
    - Freightage expense (荷造運賃)
    - Advertising expense (広告宣伝費)
    - Entertainment expense (交際費)
    - Conference expenses (会議費)
    - Traveling expense (旅費交通費)
    - Communication expense (通信費)
    - Sales commission (販売手数料)
    - Supplies expense (消耗品費)
    - Stationery expense (事務用品費)
    - Repair and maintenance expense (修繕費)
    - Utilities expense (水道光熱費)
    - Books and subscription expense (新聞図書費)
    - Membership fee (諸会費)
    - Printing and binding fee (印刷製本費)
    - Commission fee (支払手数料)
    - Rent expenses on real estates (地代家賃)
    - Rent expense (賃借料)
    - Insurance expense (保険料)
    - Sundry taxe (租税公課)
    - Professional fees (支払報酬料)
    - Donations expense (寄付金)
    - Patent royalties (特許使用料)
    - Miscellaneous expense (雑費)
    - Research and development expense (研究開発費)
    - Provision of allowance for doubtful accounts (貸倒引当金繰入)
    - Depreciation & Amortization expense (減価償却費)
    - **Total of operating expenses (販売管理費 計)**
- **Operating income (営業利益)** [Ref: Operating profit (or loss) / 営業損益金額]
- **Non-operating income (営業外収益)**
    - Subsidy income (補助金収入)
    - Interest income (受取利息)
    - Miscellaneous income (雑収入)
- **Non-operating expenses (営業外費用)**
    - Interest expense (支払利息)
    - Amortization of deferred assets (繰延資産償却)
- **Ordinary income (経常利益)** [Ref: Ordinary profit (or loss) / 経常損益金額]
- **Extraordinary income (特別利益)**
    - Reversal of allowance for doubtful accounts (貸倒引当金戻入)
- **Extraordinary loss (特別損失)**
    - Loss on retirement of non-current assets (固定資産除却損)
- **Income before income taxes (税引前当期純損益金額)**
- **Income taxes (法人税等)**
    - Income taxes – current (法人税等)
    - Income taxes – deferred (法人税等調整額)
- **Net income (当期純利益)** [Ref: Net profit / 当期純損益金額]

### Balance Sheet (貸借対照表)
- **Assets (資産の部)**
    - **Current assets (流動資産)**
        - Cash (現金)
        - Bank account 1-6 (銀行口座 1-6)
        - Trade accounts receivable (売掛金)
        - Allowance for doubtful accounts (貸倒引当金(売))
        - Merchandise (商品)
        - Supplies (貯蔵品)
        - Work in process (仕掛品)
        - Finished goods (製品)
        - Suspense taxes (仮払税金)
        - Advance payments – trade (前払金)
        - Advance payments – other (前渡金)
        - Accrued consumption tax (未収消費税)
        - Accounts receivable-other (立替金/未収入金)
        - Prepaid expense (前払費用)
        - Accrued revenue (未収収益)
        - Loans receivable (短期貸付金)
        - Loans receivable from directors (役員貸付金)
        - Temporary payment (仮払金)
        - Suspense consumption tax (仮払消費税)
        - **Total of current assets (流動資産 計)**
    - **Non-current assets (固定資産)**
        - **Tangible non-current assets (有形固定資産)**
            - Facilities attached to buildings (建物付属設備)
            - Tools (工具器具備品)
            - Accumulated depreciation (減価償却累計額)
            - **Total of tangible non-current assets (有形固定資産計)**
        - **Intangible non-current assets (無形固定資産)**
            - Software (ソフトウエア)
            - Patents (特許権)
            - Other non-current asset (その他無形固定資産)
            - **Total of non-current assets (無形固定資産 計)**
        - **Investment (投資その他の資産)**
            - Security deposit (敷金)
            - Guarantee deposit (差入保証金)
            - Investments in capital (出資金)
            - **Total of investment (投資その他の資産 計)**
        - **Total of non-current assets (固定資産計)**
    - **Deferred assets (繰延資産)**
        - Start-up costs (創立費)
        - Share issuance cost (株式交付費)
        - Development expenses (開発費)
        - **Total of deferred assets (繰延資産 計)**
    - **Total assets (資産合計)** [Ref: Total of assets / 資産 計]
- **Liabilities (負債の部)**
    - **Current liabilities (流動負債)**
        - Trade accounts payable (買掛金)
        - Long-term debt with current maturities (一年以内返済長期借入金)
        - Short-term loans payable (短期借入金)
        - Loans payable to directors (役員借入金)
        - Accounts payable - other (未払金)
        - Accrued expenses (未払費用)
        - Accrued expenses(Card1) (未払費用(クレジットカード1))
        - Income tax payable (未払法人税等)
        - Consumption tax payable (未払消費税等)
        - Advance received (前受金)
        - Withholdings (預り金)
        - Suspense payments (仮受金)
        - Suspense received Accrued consumption tax (仮受消費税)
        - **Total of current liabilities (流動負債 計)**
    - **Non-current liabilities (固定負債)** [Ref: Long-term liabilities / 固定負債]
        - Long-term debt (長期借入金)
        - **Total of long-term liabilities (固定負債 計)**
    - **Total liabilities (負債合計)** [Ref: Total of liabilities / 負債 計]
- **Net assets (純資産の部)**
    - **Shareholders' equity (株主資本)**
        - Capital stock (資本金)
        - **Capital surplus (資本剰余金計)**
            - Capital reserve (資本準備金)
            - Other capital surplus (その他資本剰余金)
        - **Retained earnings (利益剰余金 計)**
            - Other retained earnings
            - Reserve for advanced depreciation of non-current assets (固定資産圧縮積立金)
            - Retained earnings brought forward (繰越利益)
            - Auccumulated net income (当期純損益金額)
        - **Total of shareholders' equity (株主資本 計)**
    - **Valuation and translation adjustments (評価・換算差額等 計)**
    - **Share acquisition rights (新株予約権 計)**
    - **Total equity (純資産合計)** [Ref: Total of net assets / 純資産 計]
- **Total liabilities and equity (負債純資産合計)** [Ref: Total of liabilities and net assets / 負債及び純資産 計]

### Cash Flow Statement (キャッシュ・フロー計算書)
- **Cash flow from operating activities (営業活動によるキャッシュ・フロー)** [Ref: Net cash from operating activities]
    - **Operating Cash flow (営業収支)**
        - Net profit (当期純損益金額)
        - Plus: Income taxes (法人税等の加算調整)
        - Plus: Non-cash expense (非現金費用の加算調整)
        - Plus: Non-operating loss (営業外費用の加算調整)
        - Less: Non-operating income (営業外収益の減算調整)
        - Less: Non-cash extraordinary income (特別利益の減算調整)
        - Plus: Non-cash extraordinary loss (特別損失の加算調整)
        - **Operating Cash flow(Before Changes in Net Working Capital) (営業収支(正味運転資本の増減等調整前))**
    - **Changes in Net Working Capital (正味運転資本の増減)**
        - Trade accounts receivable (売上債権)
        - Inventory (棚卸資産)
        - Trade accounts payable (仕入債務)
        - Other current assets (その他流動資産)
        - Other current liabilities (その他流動負債)
        - **Total of Operating Cash flow (営業収支の合計)**
- **Cash flow from investing activities (投資活動によるキャッシュ・フロー)** [Ref: Total of Cash flows from investing activities]
    - Details of Investing Cash Inflow (投資収入内訳)
    - Details of Investing Cash Outflow (投資支出内訳)
- **Cash flow from financing activities (財務活動によるキャッシュ・フロー)** [Ref: Total of Financing Cash flow]
    - Details of cash inflow (収入内訳)
    - Details of cash outflow (支出内訳)
- **Effect of Exchange Rate Changes (現金及び現金同等物に係る換算差額)**
- **Changes in Cash (現金及び現金同等物の増減額)**
- **Beginning cash position (現金及び現金同等物の期首残高)**
- **End cash position (現金及び現金同等物の期末残高)**
---
