"""
Financial ratio calculation module for the businessplan-writing skill.
Adapted from analyzing-financial-statements/calculate_ratios.py.

Customizations for the 120-month business plan pipeline:
- Reads monthly_values arrays (120 entries) from post-fundraising JSON files.
- Outputs bilingual (EN/JA) labels on every ratio.
- Per-share metrics separated as a first-class category.
- Safe division guard: denominator == 0 → 0.0 (never null/NaN/Infinity).
- Annual aggregation via trailing-twelve-month (TTM) for P&L flow items
  and period-end snapshots for B/S stock items.
"""

import json
import math
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
MONTHS = 120
YEARS = 10

# Bilingual label registry  (ratio_key → (label_en, label_ja))
LABELS: dict[str, tuple[str, str]] = {
    # Profitability
    "roe": ("Return on Equity", "自己資本利益率"),
    "roa": ("Return on Assets", "総資産利益率"),
    "gross_margin": ("Gross Margin", "売上総利益率"),
    "operating_margin": ("Operating Margin", "営業利益率"),
    "net_margin": ("Net Margin", "純利益率"),
    # Liquidity
    "current_ratio": ("Current Ratio", "流動比率"),
    "quick_ratio": ("Quick Ratio", "当座比率"),
    "cash_ratio": ("Cash Ratio", "現金比率"),
    # Leverage
    "debt_to_equity": ("Debt-to-Equity Ratio", "負債資本倍率"),
    "interest_coverage": ("Interest Coverage Ratio", "インタレスト・カバレッジ・レシオ"),
    "debt_service_coverage": ("Debt Service Coverage Ratio", "DSCR"),
    # Efficiency
    "asset_turnover": ("Asset Turnover", "総資産回転率"),
    "inventory_turnover": ("Inventory Turnover", "棚卸資産回転率"),
    "receivables_turnover": ("Receivables Turnover", "売掛金回転率"),
    "days_sales_outstanding": ("Days Sales Outstanding", "売掛金回転日数"),
    # Valuation
    "pe_ratio": ("Price-to-Earnings Ratio", "株価収益率"),
    "pb_ratio": ("Price-to-Book Ratio", "株価純資産倍率"),
    "ps_ratio": ("Price-to-Sales Ratio", "株価売上高倍率"),
    "ev_to_ebitda": ("EV/EBITDA", "企業価値倍率"),
    "peg_ratio": ("PEG Ratio", "PEGレシオ"),
    # Per-share
    "eps": ("Earnings Per Share", "一株当たり当期純利益"),
    "book_value_per_share": ("Book Value Per Share", "一株当たり純資産"),
    "dividend_per_share": ("Dividend Per Share", "一株当たり配当金"),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Divide safely. Returns *default* when denominator is zero."""
    if denominator == 0:
        return default
    result = numerator / denominator
    if math.isnan(result) or math.isinf(result):
        return default
    return result


def _ttm(monthly: list[float], month_idx: int) -> float:
    """Trailing-twelve-month sum ending at *month_idx* (0-based)."""
    start = max(0, month_idx - 11)
    return sum(monthly[start : month_idx + 1])


def _annual_from_monthly(monthly: list[float], is_flow: bool = True) -> list[float]:
    """Collapse 120 monthly values into 10 annual values.

    For flow metrics (P&L): sum each 12-month block.
    For stock metrics (B/S): take the period-end (month 12, 24, …).
    """
    annual: list[float] = []
    for y in range(YEARS):
        if is_flow:
            annual.append(sum(monthly[y * 12 : (y + 1) * 12]))
        else:
            annual.append(monthly[min((y + 1) * 12 - 1, MONTHS - 1)])
    return annual


def _load_json(path: str | Path) -> dict[str, Any]:
    """Load a JSON file and return its contents."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _get_monthly(data: dict[str, Any], key: str = "monthly_values") -> list[float]:
    """Extract 120-element monthly array from a loaded JSON dict."""
    values = data.get(key, [0.0] * MONTHS)
    # Pad to 120 if shorter
    if len(values) < MONTHS:
        values = values + [0.0] * (MONTHS - len(values))
    return [float(v) for v in values[:MONTHS]]


def _ratio_json(
    ratio_key: str,
    monthly: list[float],
    *,
    is_flow: bool = False,
    driver: str = "",
    source_sub_tasks: list[str] | None = None,
    notes: str = "",
) -> dict[str, Any]:
    """Build the standard output envelope for one ratio series."""
    label_en, label_ja = LABELS.get(ratio_key, (ratio_key, ratio_key))
    return {
        "metadata": {
            "ratio_key": ratio_key,
            "label_en": label_en,
            "label_ja": label_ja,
            "currency": "ratio",
            "driver": driver,
            "source_sub_tasks": source_sub_tasks or [],
            "notes": notes,
        },
        "monthly_values": [round(v, 6) for v in monthly],
        "annual_values": [round(v, 6) for v in _annual_from_monthly(monthly, is_flow=is_flow)],
    }


# ---------------------------------------------------------------------------
# Category calculators — each returns a list of ratio-JSON dicts
# ---------------------------------------------------------------------------

def calculate_profitability(
    pl: dict[str, Any],
    bs: dict[str, Any],
) -> list[dict[str, Any]]:
    """Sub-task 22-1: ROE, ROA, Gross Margin, Operating Margin, Net Margin."""
    net_income = _get_monthly(pl.get("net_income", pl), "monthly_values")
    revenue = _get_monthly(pl.get("revenue", pl), "monthly_values")
    gross_profit = _get_monthly(pl.get("gross_profit", pl), "monthly_values")
    operating_income = _get_monthly(pl.get("operating_income", pl), "monthly_values")
    total_assets = _get_monthly(bs.get("total_assets", bs), "monthly_values")
    equity = _get_monthly(bs.get("shareholders_equity", bs), "monthly_values")

    roe = [safe_divide(ni, eq) for ni, eq in zip(net_income, equity)]
    roa = [safe_divide(ni, ta) for ni, ta in zip(net_income, total_assets)]
    gm = [safe_divide(gp, r) for gp, r in zip(gross_profit, revenue)]
    om = [safe_divide(oi, r) for oi, r in zip(operating_income, revenue)]
    nm = [safe_divide(ni, r) for ni, r in zip(net_income, revenue)]

    return [
        _ratio_json("roe", roe, driver="Net Income ÷ Shareholders' Equity", source_sub_tasks=["21-1", "21-2"]),
        _ratio_json("roa", roa, driver="Net Income ÷ Total Assets", source_sub_tasks=["21-1", "21-2"]),
        _ratio_json("gross_margin", gm, driver="Gross Profit ÷ Revenue", source_sub_tasks=["21-1"]),
        _ratio_json("operating_margin", om, driver="Operating Income ÷ Revenue", source_sub_tasks=["21-1"]),
        _ratio_json("net_margin", nm, driver="Net Income ÷ Revenue", source_sub_tasks=["21-1"]),
    ]


def calculate_liquidity(bs: dict[str, Any]) -> list[dict[str, Any]]:
    """Sub-task 22-2: Current Ratio, Quick Ratio, Cash Ratio."""
    current_assets = _get_monthly(bs.get("current_assets", bs), "monthly_values")
    current_liabilities = _get_monthly(bs.get("current_liabilities", bs), "monthly_values")
    inventory = _get_monthly(bs.get("inventory", bs), "monthly_values")
    cash = _get_monthly(bs.get("cash_and_deposits", bs), "monthly_values")

    cr = [safe_divide(ca, cl) for ca, cl in zip(current_assets, current_liabilities)]
    qr = [safe_divide(ca - inv, cl) for ca, inv, cl in zip(current_assets, inventory, current_liabilities)]
    cashr = [safe_divide(c, cl) for c, cl in zip(cash, current_liabilities)]

    return [
        _ratio_json("current_ratio", cr, driver="Current Assets ÷ Current Liabilities", source_sub_tasks=["21-2"]),
        _ratio_json("quick_ratio", qr, driver="(Current Assets − Inventory) ÷ Current Liabilities", source_sub_tasks=["21-2"]),
        _ratio_json("cash_ratio", cashr, driver="Cash & Deposits ÷ Current Liabilities", source_sub_tasks=["21-2"]),
    ]


def calculate_leverage(
    pl: dict[str, Any],
    bs: dict[str, Any],
) -> list[dict[str, Any]]:
    """Sub-task 22-3: Debt-to-Equity, Interest Coverage, DSCR."""
    total_debt = _get_monthly(bs.get("total_debt", bs), "monthly_values")
    equity = _get_monthly(bs.get("shareholders_equity", bs), "monthly_values")
    operating_income = _get_monthly(pl.get("operating_income", pl), "monthly_values")
    interest_expense = _get_monthly(pl.get("interest_expense", pl), "monthly_values")
    current_lt_debt = _get_monthly(bs.get("current_portion_long_term_debt", bs), "monthly_values")

    de = [safe_divide(d, e) for d, e in zip(total_debt, equity)]
    ic = [safe_divide(oi, ie) for oi, ie in zip(operating_income, interest_expense)]
    dscr = [safe_divide(oi, ie + cpd) for oi, ie, cpd in zip(operating_income, interest_expense, current_lt_debt)]

    return [
        _ratio_json("debt_to_equity", de, driver="Total Debt ÷ Shareholders' Equity", source_sub_tasks=["21-2"]),
        _ratio_json("interest_coverage", ic, driver="Operating Income ÷ Interest Expense", source_sub_tasks=["21-1", "21-2"]),
        _ratio_json("debt_service_coverage", dscr, driver="Operating Income ÷ (Interest + Current LT Debt)", source_sub_tasks=["21-1", "21-2"]),
    ]


def calculate_efficiency(
    pl: dict[str, Any],
    bs: dict[str, Any],
) -> list[dict[str, Any]]:
    """Sub-task 22-4: Asset Turnover, Inventory Turnover, Receivables Turnover, DSO."""
    revenue = _get_monthly(pl.get("revenue", pl), "monthly_values")
    cogs = _get_monthly(pl.get("cost_of_goods_sold", pl), "monthly_values")
    total_assets = _get_monthly(bs.get("total_assets", bs), "monthly_values")
    inventory = _get_monthly(bs.get("inventory", bs), "monthly_values")
    ar = _get_monthly(bs.get("accounts_receivable", bs), "monthly_values")

    at = [safe_divide(_ttm(revenue, i), ta) for i, ta in enumerate(total_assets)]
    it = [safe_divide(_ttm(cogs, i), inv) for i, inv in enumerate(inventory)]
    rt = [safe_divide(_ttm(revenue, i), a) for i, a in enumerate(ar)]
    dso = [safe_divide(365, r) for r in rt]

    return [
        _ratio_json("asset_turnover", at, driver="TTM Revenue ÷ Total Assets", source_sub_tasks=["21-1", "21-2"]),
        _ratio_json("inventory_turnover", it, driver="TTM COGS ÷ Inventory", source_sub_tasks=["21-1", "21-2"]),
        _ratio_json("receivables_turnover", rt, driver="TTM Revenue ÷ Trade AR", source_sub_tasks=["21-1", "21-2"]),
        _ratio_json("days_sales_outstanding", dso, driver="365 ÷ Receivables Turnover", source_sub_tasks=["21-1", "21-2"]),
    ]


def calculate_valuation(
    pl: dict[str, Any],
    bs: dict[str, Any],
    market: dict[str, Any],
) -> list[dict[str, Any]]:
    """Sub-task 22-5: P/E, P/B, P/S, EV/EBITDA, PEG."""
    net_income = _get_monthly(pl.get("net_income", pl), "monthly_values")
    revenue = _get_monthly(pl.get("revenue", pl), "monthly_values")
    ebitda = _get_monthly(pl.get("ebitda", pl), "monthly_values")
    equity = _get_monthly(bs.get("shareholders_equity", bs), "monthly_values")
    total_debt = _get_monthly(bs.get("total_debt", bs), "monthly_values")
    cash = _get_monthly(bs.get("cash_and_deposits", bs), "monthly_values")

    share_price = _get_monthly(market.get("share_price", market), "monthly_values")
    shares = _get_monthly(market.get("diluted_shares_outstanding", market), "monthly_values")

    eps_m = [safe_divide(ni, s) for ni, s in zip(net_income, shares)]
    bvps = [safe_divide(eq, s) for eq, s in zip(equity, shares)]
    mcap = [p * s for p, s in zip(share_price, shares)]

    pe = [safe_divide(p, e) for p, e in zip(share_price, eps_m)]
    pb = [safe_divide(p, b) for p, b in zip(share_price, bvps)]
    ps = [safe_divide(mc, r) for mc, r in zip(mcap, revenue)]
    ev = [mc + d - c for mc, d, c in zip(mcap, total_debt, cash)]
    ev_ebitda = [safe_divide(e, eb) for e, eb in zip(ev, ebitda)]

    # PEG: YoY earnings growth → use annual NI change
    annual_ni = _annual_from_monthly(net_income, is_flow=True)
    yoy_growth = [0.0] + [
        safe_divide(annual_ni[y] - annual_ni[y - 1], abs(annual_ni[y - 1]))
        for y in range(1, YEARS)
    ]
    # Expand annual growth back to monthly for alignment
    monthly_growth = []
    for y in range(YEARS):
        monthly_growth.extend([yoy_growth[y]] * 12)
    peg = [
        safe_divide(p, g * 100) if g > 0 else 0.0
        for p, g in zip(pe, monthly_growth)
    ]

    return [
        _ratio_json("pe_ratio", pe, driver="Share Price ÷ EPS", source_sub_tasks=["21-1", "16-3"]),
        _ratio_json("pb_ratio", pb, driver="Share Price ÷ BVPS", source_sub_tasks=["21-2", "16-3"]),
        _ratio_json("ps_ratio", ps, driver="Market Cap ÷ Revenue", source_sub_tasks=["21-1", "16-3"]),
        _ratio_json("ev_to_ebitda", ev_ebitda, driver="(MCap + Debt − Cash) ÷ EBITDA", source_sub_tasks=["21-1", "21-2", "16-3"]),
        _ratio_json("peg_ratio", peg, driver="P/E ÷ (Earnings Growth × 100)", source_sub_tasks=["21-1", "16-3"]),
    ]


def calculate_per_share(
    pl: dict[str, Any],
    bs: dict[str, Any],
    market: dict[str, Any],
) -> list[dict[str, Any]]:
    """Sub-task 22-6: EPS, Book Value Per Share, Dividend Per Share."""
    net_income = _get_monthly(pl.get("net_income", pl), "monthly_values")
    equity = _get_monthly(bs.get("shareholders_equity", bs), "monthly_values")
    shares = _get_monthly(market.get("diluted_shares_outstanding", market), "monthly_values")
    dividends = _get_monthly(market.get("total_dividends", {"monthly_values": [0.0] * MONTHS}), "monthly_values")

    eps_m = [safe_divide(ni, s) for ni, s in zip(net_income, shares)]
    bvps = [safe_divide(eq, s) for eq, s in zip(equity, shares)]
    dps = [safe_divide(d, s) for d, s in zip(dividends, shares)]

    return [
        _ratio_json("eps", eps_m, driver="Net Income ÷ Diluted Shares", source_sub_tasks=["21-1", "16-3"]),
        _ratio_json("book_value_per_share", bvps, driver="Shareholders' Equity ÷ Diluted Shares", source_sub_tasks=["21-2", "16-3"]),
        _ratio_json("dividend_per_share", dps, driver="Total Dividends ÷ Diluted Shares", source_sub_tasks=["16-3"],
                     notes="Set to 0 for all months if no dividend policy is defined (typical for startups)."),
    ]


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def calculate_all_ratios(
    pl_data: dict[str, Any],
    bs_data: dict[str, Any],
    market_data: dict[str, Any],
) -> dict[str, list[dict[str, Any]]]:
    """Calculate every ratio category and return grouped results.

    Returns a dict keyed by sub-task id → list of ratio JSON envelopes.
    """
    return {
        "22-1-profitability-ratios": calculate_profitability(pl_data, bs_data),
        "22-2-liquidity-ratios": calculate_liquidity(bs_data),
        "22-3-leverage-ratios": calculate_leverage(pl_data, bs_data),
        "22-4-efficiency-ratios": calculate_efficiency(pl_data, bs_data),
        "22-5-valuation-ratios": calculate_valuation(pl_data, bs_data, market_data),
        "22-6-per-share-metrics": calculate_per_share(pl_data, bs_data, market_data),
    }


def write_ratio_files(
    output_dir: str | Path,
    pl_data: dict[str, Any],
    bs_data: dict[str, Any],
    market_data: dict[str, Any],
) -> list[Path]:
    """Calculate all ratios and write one JSON file per sub-task.

    Returns list of written file paths.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    all_ratios = calculate_all_ratios(pl_data, bs_data, market_data)
    written: list[Path] = []
    for filename, ratios_list in all_ratios.items():
        path = output_dir / f"{filename}.json"
        payload = {
            "metadata": {
                "sub_task": filename,
                "label_en": filename.replace("-", " ").title(),
                "label_ja": LABELS.get(filename, (filename, filename))[1],
                "count": len(ratios_list),
            },
            "ratios": ratios_list,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        written.append(path)
    return written


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Usage: python calculate_ratios.py <pl.json> <bs.json> <market.json> [output_dir]")
        sys.exit(1)

    pl = _load_json(sys.argv[1])
    bs = _load_json(sys.argv[2])
    mkt = _load_json(sys.argv[3])
    out = sys.argv[4] if len(sys.argv) > 4 else "./financials"

    paths = write_ratio_files(out, pl, bs, mkt)
    for p in paths:
        print(f"  ✓ {p}")
    print(f"\nWrote {len(paths)} ratio files to {out}/")
