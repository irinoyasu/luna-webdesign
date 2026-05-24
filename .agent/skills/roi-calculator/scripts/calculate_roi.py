import argparse
import sys
import numpy_financial as npf

def calculate_roi_metrics(cashflows, discount_rate):
    """
    Calculate essential ROI metrics given a series of monthly cashflows.
    Cashflow array: [Month_0_CF, Month_1_CF, Month_2_CF, ...]
    Discount rate: Annual discount rate, which will be converted to monthly.
    """
    if not cashflows:
        print("Error: No cashflows provided.")
        sys.exit(1)

    monthly_discount_rate = (1 + discount_rate) ** (1/12) - 1

    # Total Cash Outflow (sum of all negative cashflows)
    total_outflow = sum(cf for cf in cashflows if cf < 0)
    
    # Total Cash Inflow (sum of all positive cashflows)
    total_inflow = sum(cf for cf in cashflows if cf > 0)
    
    # Total Cash Flow
    total_cashflow = sum(cashflows)

    # Cumulative Cash Flows
    cumulative_cashflows = []
    current_sum = 0
    for cf in cashflows:
        current_sum += cf
        cumulative_cashflows.append(current_sum)

    # Required Funding: Minimum cumulative cash flow
    required_funding = min(cumulative_cashflows)
    timing_of_minimum_months = cumulative_cashflows.index(required_funding)

    # Payback Period (Time when cumulative cash flow returns to zero and stays >= 0)
    payback_period_months = None
    for i in range(len(cumulative_cashflows)):
        if cumulative_cashflows[i] >= 0:
            if i > 0 and cumulative_cashflows[i-1] < 0:
                # Linear interpolation for more precise payback period
                fraction = abs(cumulative_cashflows[i-1]) / (cumulative_cashflows[i] - cumulative_cashflows[i-1])
                payback_period_months = (i - 1) + fraction
                break
            elif i == 0:
                payback_period_months = 0
                break

    # Net Present Value (NPV)
    # Using npf.npv which assumes cashflows start at period 0 (today)
    npv = npf.npv(monthly_discount_rate, cashflows)
    
    # Internal Rate of Return (IRR) - Monthly IRR converted to Annual
    try:
        monthly_irr = npf.irr(cashflows)
        if monthly_irr is not None and monthly_irr > -1:
            annual_irr_percentage = ((1 + monthly_irr) ** 12 - 1) * 100
        else:
            annual_irr_percentage = float('nan')
    except:
        annual_irr_percentage = float('nan')

    # Return Multiple
    return_multiple = total_inflow / abs(total_outflow) if total_outflow != 0 else float('inf')

    print("=" * 40)
    print("ROI Analysis Results")
    print("=" * 40)
    print(f"Total Cash Inflow:  {total_inflow:,.2f}")
    print(f"Total Cash Outflow: {total_outflow:,.2f}")
    print(f"Total Cash Flow:    {total_cashflow:,.2f}")
    print(f"Required Funding (Min Cumulative CF): {required_funding:,.2f} at month {timing_of_minimum_months}")
    if payback_period_months is not None:
         print(f"Payback Period:     {payback_period_months:.1f} months")
    else:
         print("Payback Period:     Never")
    print(f"Return Multiple:    {return_multiple:.2f}x")
    print(f"NPV (Annual Rate={discount_rate*100:.2f}%): {npv:,.2f}")
    print(f"IRR (Annualized):   {annual_irr_percentage:.2f}%")
    print("=" * 40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate ROI Metrics based on monthly cashflows.")
    parser.add_argument("--cashflows", type=float, nargs="+", required=True,
                        help="List of monthly cash flows starting exactly from Month 0 (e.g., -50000 10000 20000).")
    parser.add_argument("--rate", type=float, default=0.10,
                        help="Annual discount rate as a decimal (e.g., 0.125 for 12.5%%). Default is 0.10.")
    
    args = parser.parse_args()
    try:
        calculate_roi_metrics(args.cashflows, args.rate)
    except ModuleNotFoundError:
        print("Please install numpy-financial: pip install numpy-financial")
        sys.exit(1)
