import argparse
import sys
import json
import math

def irr(cashflows, iterations=1000):
    """
    Calculate the Internal Rate of Return (IRR) using Newton-Raphson with a Bisection fallback.
    """
    if not cashflows or all(c >= 0 for c in cashflows) or all(c <= 0 for c in cashflows):
        return float('nan')

    # Try Newton-Raphson first
    rate = 0.005 # 0.5% per month initial guess
    for _ in range(iterations):
        npv_rate = sum(c / (1 + rate)**i for i, c in enumerate(cashflows))
        derivative = sum(-i * c / (1 + rate)**(i+1) for i, c in enumerate(cashflows))
        if derivative == 0: break
        new_rate = rate - npv_rate / derivative
        if abs(new_rate - rate) < 1e-7:
            return new_rate
        rate = new_rate
        
    # Fallback to Bisection method
    def npv_func(r):
        return sum(c / (1 + r)**i for i, c in enumerate(cashflows))
    
    low = -0.99
    high = 1.0
    if npv_func(high) > 0:
        while npv_func(high) > 0 and high < 100:
            high *= 2
    
    if npv_func(low) * npv_func(high) > 0:
        return float('nan')
        
    for _ in range(100):
        mid = (low + high) / 2
        if abs(high - low) < 1e-7:
            return mid
        if npv_func(low) * npv_func(mid) < 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

def calculate_roi_metrics(data_dict, annual_discount_rate):
    """
    Calculate and print comprehensive ROI metrics.
    """
    net_cf = data_dict["net_cashflows"]
    monthly_rate = (1 + annual_discount_rate) ** (1/12) - 1

    # 1. Totals & Summaries
    total_inflow = sum(cf for cf in net_cf if cf > 0)
    total_outflow = sum(cf for cf in net_cf if cf < 0)
    
    # 2. Cumulative & Funding
    cumulative_cf = []
    curr = 0
    for cf in net_cf:
        curr += cf
        cumulative_cf.append(curr)
    
    lowest_val = min(cumulative_cf) if cumulative_cf else 0
    lowest_month = cumulative_cf.index(lowest_val) if cumulative_cf else 0

    # 3. Payback Period (Interpolated)
    payback_months = None
    for i in range(len(cumulative_cf)):
        if cumulative_cf[i] >= 0:
            if i > 0 and cumulative_cf[i-1] < 0:
                fraction = abs(cumulative_cf[i-1]) / (cumulative_cf[i] - cumulative_cf[i-1])
                payback_months = (i - 1) + fraction
                break
            elif i == 0:
                payback_months = 0
                break

    # 4. MOIC (Multiple on Invested Capital)
    # Best practice: Total Inflow / Absolute Total Investing Outflow (Invested Capital)
    invested_capital = abs(data_dict["totals"]["investing_outflows"])
    moic = total_inflow / invested_capital if invested_capital > 0 else float('inf')

    # 5. NPV & IRR
    npv = sum(cf / ((1 + monthly_rate) ** i) for i, cf in enumerate(net_cf))
    m_irr = irr(net_cf)
    annual_irr = ((1 + m_irr) ** 12 - 1) * 100 if not math.isnan(m_irr) else float('nan')

    # OUTPUT
    print("\n" + "="*60)
    print(f"{'FINANCIAL PERFORMANCE SUMMARY':^60}")
    print("="*60)
    
    print(f"{'Category':<20} | {'Inflow':>12} | {'Outflow':>12} | {'Net':>12}")
    print("-" * 60)
    cats = [
        ("Operating", data_dict["totals"]["operating_inflows"], data_dict["totals"]["operating_outflows"]),
        ("Investing", data_dict["totals"]["investing_inflows"], data_dict["totals"]["investing_outflows"]),
        ("Financing", data_dict["totals"]["financing_inflows"], data_dict["totals"]["financing_outflows"])
    ]
    for name, inf, out in cats:
        print(f"{name:<20} | {inf:12,.0f} | {out:12,.0f} | {(inf-out):12,.0f}")
    print("-" * 60)
    print(f"{'TOTAL NET CASH FLOW':<47} | {sum(net_cf):12,.0f}")
    
    print("\n" + "-"*60)
    print(f"{'KEY INVESTMENT METRICS':^60}")
    print("-"*60)
    print(f"NPV (at {annual_discount_rate*100:.1f}%):           {npv:,.2f}")
    print(f"IRR (Annualized):            {annual_irr:.2f}%")
    print(f"MOIC (on Invested Capital):  {moic:.2f}x")
    if payback_months is not None:
        print(f"Payback Period:              {payback_months:.1f} months")
    else:
        print(f"Payback Period:              Not reached")
    
    print("\n" + "-"*60)
    print(f"{'LIQUIDITY & FUNDING':^60}")
    print("-"*60)
    print(f"Max Funding Requirement:     {abs(lowest_val):,.2f}")
    print(f"Peak Deficit Month:          Month {lowest_month}")
    print(f"Final Cumulative Cash Flow:  {cumulative_cf[-1] if cumulative_cf else 0:,.2f}")
    print("="*60 + "\n")

def process_detailed_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    cashflows_list = data.get("cashflows", [])
    discount_rate = data.get("discount_rate", 0.10)
    
    totals = {
        "operating_inflows": 0, "operating_outflows": 0,
        "investing_inflows": 0, "investing_outflows": 0,
        "financing_inflows": 0, "financing_outflows": 0
    }
    
    net_cashflows = []
    
    for month_data in cashflows_list:
        op_in = sum(month_data.get("operating_inflows", {}).values())
        op_out = sum(month_data.get("operating_outflows", {}).values())
        inv_in = sum(month_data.get("investing_inflows", {}).values())
        inv_out = sum(month_data.get("investing_outflows", {}).values())
        fin_in = sum(month_data.get("financing_inflows", {}).values())
        fin_out = sum(month_data.get("financing_outflows", {}).values())
        
        totals["operating_inflows"] += op_in
        totals["operating_outflows"] += op_out
        totals["investing_inflows"] += inv_in
        totals["investing_outflows"] += inv_out
        totals["financing_inflows"] += fin_in
        totals["financing_outflows"] += fin_out
        
        net_cf = (op_in - op_out) + (inv_in - inv_out) + (fin_in - fin_out)
        net_cashflows.append(net_cf)
        
    return {
        "net_cashflows": net_cashflows,
        "totals": totals
    }, discount_rate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Professional ROI Calculator for Corporate Finance.")
    parser.add_argument("--file", type=str, required=True, help="Path to JSON with detailed cashflows.")
    parser.add_argument("--rate", type=float, help="Override annual discount rate (e.g. 0.12).")
    
    args = parser.parse_args()
    
    try:
        data_dict, file_rate = process_detailed_json(args.file)
        rate = args.rate if args.rate is not None else file_rate
        calculate_roi_metrics(data_dict, rate)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
