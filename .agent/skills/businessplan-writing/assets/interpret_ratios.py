"""
Financial ratio interpretation module for the businessplan-writing skill.
Adapted from analyzing-financial-statements/interpret_ratios.py.

Customizations:
- Startup-specific industry benchmarks added.
- 120-month trend analysis with annual windowing.
- Bilingual (EN/JA) output on ratings and recommendations.
- Overall health scoring aligned with Task 22 pipeline.
"""

from typing import Any


class RatioInterpreter:
    """Interpret financial ratios with industry context and bilingual output."""

    BENCHMARKS: dict[str, dict[str, dict[str, float]]] = {
        "startup": {
            "current_ratio": {"excellent": 2.0, "good": 1.5, "acceptable": 1.0, "poor": 0.7},
            "debt_to_equity": {"excellent": 0.3, "good": 0.6, "acceptable": 1.5, "poor": 3.0},
            "roe": {"excellent": 0.25, "good": 0.15, "acceptable": 0.05, "poor": -0.10},
            "gross_margin": {"excellent": 0.70, "good": 0.50, "acceptable": 0.30, "poor": 0.10},
            "operating_margin": {"excellent": 0.20, "good": 0.10, "acceptable": 0.0, "poor": -0.20},
            "net_margin": {"excellent": 0.15, "good": 0.05, "acceptable": 0.0, "poor": -0.30},
            "pe_ratio": {"undervalued": 15, "fair": 30, "growth": 50, "expensive": 80},
        },
        "technology": {
            "current_ratio": {"excellent": 2.5, "good": 1.8, "acceptable": 1.2, "poor": 1.0},
            "debt_to_equity": {"excellent": 0.3, "good": 0.5, "acceptable": 1.0, "poor": 2.0},
            "roe": {"excellent": 0.25, "good": 0.18, "acceptable": 0.12, "poor": 0.08},
            "gross_margin": {"excellent": 0.70, "good": 0.50, "acceptable": 0.35, "poor": 0.20},
            "pe_ratio": {"undervalued": 15, "fair": 25, "growth": 35, "expensive": 50},
        },
        "retail": {
            "current_ratio": {"excellent": 2.0, "good": 1.5, "acceptable": 1.0, "poor": 0.8},
            "debt_to_equity": {"excellent": 0.5, "good": 0.8, "acceptable": 1.5, "poor": 2.5},
            "roe": {"excellent": 0.20, "good": 0.15, "acceptable": 0.10, "poor": 0.05},
            "gross_margin": {"excellent": 0.40, "good": 0.30, "acceptable": 0.20, "poor": 0.10},
            "pe_ratio": {"undervalued": 12, "fair": 18, "growth": 25, "expensive": 35},
        },
        "financial": {
            "current_ratio": {"excellent": 1.5, "good": 1.2, "acceptable": 1.0, "poor": 0.8},
            "debt_to_equity": {"excellent": 1.0, "good": 2.0, "acceptable": 4.0, "poor": 6.0},
            "roe": {"excellent": 0.15, "good": 0.12, "acceptable": 0.08, "poor": 0.05},
            "pe_ratio": {"undervalued": 10, "fair": 15, "growth": 20, "expensive": 30},
        },
        "manufacturing": {
            "current_ratio": {"excellent": 2.2, "good": 1.7, "acceptable": 1.3, "poor": 1.0},
            "debt_to_equity": {"excellent": 0.4, "good": 0.7, "acceptable": 1.2, "poor": 2.0},
            "roe": {"excellent": 0.18, "good": 0.14, "acceptable": 0.10, "poor": 0.06},
            "gross_margin": {"excellent": 0.35, "good": 0.25, "acceptable": 0.18, "poor": 0.12},
            "pe_ratio": {"undervalued": 14, "fair": 20, "growth": 28, "expensive": 40},
        },
        "healthcare": {
            "current_ratio": {"excellent": 2.3, "good": 1.8, "acceptable": 1.4, "poor": 1.0},
            "debt_to_equity": {"excellent": 0.3, "good": 0.6, "acceptable": 1.0, "poor": 1.8},
            "roe": {"excellent": 0.22, "good": 0.16, "acceptable": 0.11, "poor": 0.07},
            "gross_margin": {"excellent": 0.65, "good": 0.45, "acceptable": 0.30, "poor": 0.20},
            "pe_ratio": {"undervalued": 18, "fair": 28, "growth": 40, "expensive": 55},
        },
        "saas": {
            "current_ratio": {"excellent": 2.5, "good": 1.8, "acceptable": 1.2, "poor": 0.8},
            "debt_to_equity": {"excellent": 0.2, "good": 0.5, "acceptable": 1.0, "poor": 2.0},
            "roe": {"excellent": 0.30, "good": 0.20, "acceptable": 0.10, "poor": 0.0},
            "gross_margin": {"excellent": 0.80, "good": 0.70, "acceptable": 0.60, "poor": 0.40},
            "operating_margin": {"excellent": 0.25, "good": 0.10, "acceptable": 0.0, "poor": -0.30},
            "pe_ratio": {"undervalued": 20, "fair": 40, "growth": 60, "expensive": 100},
        },
    }

    # Bilingual rating labels
    RATING_LABELS: dict[str, tuple[str, str]] = {
        "Excellent": ("Excellent", "優秀"),
        "Good": ("Good", "良好"),
        "Acceptable": ("Acceptable", "許容範囲"),
        "Poor": ("Poor", "要改善"),
        "Potentially Undervalued": ("Potentially Undervalued", "割安の可能性"),
        "Fair Value": ("Fair Value", "適正水準"),
        "Growth Premium": ("Growth Premium", "成長プレミアム"),
        "Expensive": ("Expensive", "割高"),
        "N/A": ("N/A", "該当なし"),
    }

    # Ratios where higher = better
    HIGHER_IS_BETTER = {
        "current_ratio", "quick_ratio", "cash_ratio",
        "roe", "roa", "gross_margin", "operating_margin", "net_margin",
        "interest_coverage", "debt_service_coverage",
        "asset_turnover", "inventory_turnover", "receivables_turnover",
        "eps", "book_value_per_share",
    }
    # Ratios where lower = better
    LOWER_IS_BETTER = {"debt_to_equity", "days_sales_outstanding"}
    # Context-dependent ratios
    CONTEXT_DEPENDENT = {"pe_ratio", "pb_ratio", "ps_ratio", "ev_to_ebitda", "peg_ratio"}

    def __init__(self, industry: str = "startup"):
        self.industry = industry.lower()
        self.benchmarks = self.BENCHMARKS.get(self.industry, self._general())

    def _general(self) -> dict[str, dict[str, float]]:
        return {
            "current_ratio": {"excellent": 2.0, "good": 1.5, "acceptable": 1.0, "poor": 0.8},
            "debt_to_equity": {"excellent": 0.5, "good": 1.0, "acceptable": 1.5, "poor": 2.5},
            "roe": {"excellent": 0.20, "good": 0.15, "acceptable": 0.10, "poor": 0.05},
            "gross_margin": {"excellent": 0.40, "good": 0.30, "acceptable": 0.20, "poor": 0.10},
            "pe_ratio": {"undervalued": 15, "fair": 22, "growth": 30, "expensive": 45},
        }

    def get_benchmarks_for_ratio(self, ratio_name: str) -> dict[str, float]:
        """Return benchmark thresholds for a given ratio, or empty dict."""
        return self.benchmarks.get(ratio_name, {})

    def interpret_ratio(self, ratio_name: str, value: float) -> dict[str, Any]:
        """Interpret a single ratio value with bilingual output."""
        result: dict[str, Any] = {
            "value": round(value, 6),
            "rating_en": "N/A",
            "rating_ja": "該当なし",
            "message_en": "",
            "message_ja": "",
            "recommendation_en": "",
            "recommendation_ja": "",
            "benchmark": self.get_benchmarks_for_ratio(ratio_name),
        }

        bm = result["benchmark"]
        if not bm:
            result["message_en"] = "No benchmark available for this ratio"
            result["message_ja"] = "このレシオのベンチマークはありません"
            result["recommendation_en"] = "Continue monitoring this metric"
            result["recommendation_ja"] = "引き続きモニタリングしてください"
            return result

        rating = self._rate(ratio_name, value, bm)
        en, ja = self.RATING_LABELS.get(rating, (rating, rating))
        result["rating_en"] = en
        result["rating_ja"] = ja
        result["message_en"], result["message_ja"] = self._message(ratio_name, rating)
        result["recommendation_en"], result["recommendation_ja"] = self._recommend(ratio_name, rating)
        return result

    def _rate(self, name: str, value: float, bm: dict[str, float]) -> str:
        if name in self.HIGHER_IS_BETTER:
            if value >= bm.get("excellent", float("inf")):
                return "Excellent"
            if value >= bm.get("good", float("inf")):
                return "Good"
            if value >= bm.get("acceptable", float("inf")):
                return "Acceptable"
            return "Poor"
        if name in self.LOWER_IS_BETTER:
            if value <= bm.get("excellent", 0):
                return "Excellent"
            if value <= bm.get("good", 0):
                return "Good"
            if value <= bm.get("acceptable", 0):
                return "Acceptable"
            return "Poor"
        # PE-style context-dependent
        if "undervalued" in bm:
            if value <= 0:
                return "N/A"
            if value < bm["undervalued"]:
                return "Potentially Undervalued"
            if value < bm["fair"]:
                return "Fair Value"
            if value < bm.get("growth", float("inf")):
                return "Growth Premium"
            return "Expensive"
        return "N/A"

    def _message(self, name: str, rating: str) -> tuple[str, str]:
        msgs: dict[str, tuple[str, str]] = {
            "Excellent": (
                f"Performance significantly exceeds {self.industry} standards",
                f"{self.industry}業界基準を大幅に上回るパフォーマンス",
            ),
            "Good": (
                f"Above average for {self.industry} industry",
                f"{self.industry}業界の平均を上回る水準",
            ),
            "Acceptable": ("Meets industry standards", "業界基準を満たしています"),
            "Poor": ("Below industry standards — attention needed", "業界基準を下回っています — 要対応"),
            "Potentially Undervalued": ("Trading below typical multiples", "一般的な倍率を下回る水準"),
            "Fair Value": ("In line with industry averages", "業界平均と同水準"),
            "Growth Premium": ("Market pricing in growth expectations", "市場が成長期待を織り込んでいます"),
            "Expensive": ("High valuation relative to industry", "業界比で高い評価水準"),
        }
        return msgs.get(rating, ("", ""))

    def _recommend(self, name: str, rating: str) -> tuple[str, str]:
        recs: dict[str, dict[str, tuple[str, str]]] = {
            "current_ratio": {
                "Poor": ("Improve working capital or reduce short-term debt", "運転資本の改善もしくは短期借入金の削減を検討"),
                "Acceptable": ("Monitor liquidity and build cash reserves", "流動性を注視し、現金準備金の積み増しを検討"),
                "Good": ("Maintain current liquidity practices", "現在の流動性管理を維持"),
                "Excellent": ("Consider productive use of excess cash", "余剰資金の有効活用を検討"),
            },
            "debt_to_equity": {
                "Poor": ("Consider debt reduction strategies", "借入金削減戦略を検討"),
                "Acceptable": ("Monitor debt and ensure interest coverage", "借入金水準を注視し、利払い余力を確保"),
                "Good": ("Balanced structure — maintain", "均衡の取れた資本構成 — 維持"),
                "Excellent": ("May consider strategic debt for growth", "成長のための戦略的借入を検討可能"),
            },
            "roe": {
                "Poor": ("Focus on operational efficiency", "業務効率の改善に注力"),
                "Acceptable": ("Explore return enhancement opportunities", "リターン向上の機会を探索"),
                "Good": ("Solid returns — continue strategies", "堅実なリターン — 現行戦略を継続"),
                "Excellent": ("Ensure sustainability of high returns", "高リターンの持続可能性を確保"),
            },
        }
        default = ("Continue monitoring this metric", "引き続きモニタリングしてください")
        return recs.get(name, {}).get(rating, default)

    # ------------------------------------------------------------------
    # Trend analysis (120-month aware)
    # ------------------------------------------------------------------
    def analyze_trend(
        self, ratio_name: str, values: list[float], periods: list[str]
    ) -> dict[str, Any]:
        """Analyze trend over time. Works with monthly or annual series."""
        if len(values) < 2:
            return {"trend": "Insufficient data", "message_en": "Need ≥2 periods", "message_ja": "2期間以上必要"}

        first, last = values[0], values[-1]
        change = last - first
        pct = (change / abs(first)) * 100 if first != 0 else 0.0

        if abs(pct) < 5:
            trend = "Stable"
        elif ratio_name in self.LOWER_IS_BETTER:
            trend = "Improving" if pct < 0 else "Deteriorating"
        else:
            trend = "Improving" if pct > 0 else "Deteriorating"

        return {
            "trend": trend,
            "change": round(change, 6),
            "pct_change": round(pct, 2),
            "message_en": f"{ratio_name} {'increased' if change > 0 else 'decreased'} by {abs(pct):.1f}% from {periods[0]} to {periods[-1]}",
            "message_ja": f"{ratio_name}は{periods[0]}から{periods[-1]}にかけて{abs(pct):.1f}%{'上昇' if change > 0 else '低下'}しました",
        }

    # ------------------------------------------------------------------
    # Report generators
    # ------------------------------------------------------------------
    def generate_report(self, ratios: dict[str, Any]) -> str:
        """Generate a text report across all categories."""
        lines = [
            f"Financial Ratio Report — {self.industry.title()} Industry",
            "=" * 60, "",
        ]
        for category, category_ratios in ratios.items():
            lines.append(f"\n{category.upper()}")
            lines.append("-" * 40)
            for name, val in category_ratios.items():
                if isinstance(val, (int, float)):
                    interp = self.interpret_ratio(name, val)
                    lines.append(f"  {name}: {val:.4f}  [{interp['rating_en']}]  {interp['message_en']}")
        return "\n".join(lines)


# ------------------------------------------------------------------
# Comprehensive analysis entry point
# ------------------------------------------------------------------
def perform_comprehensive_analysis(
    ratios: dict[str, Any],
    industry: str = "startup",
    historical_data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Run full interpretation across all ratio categories."""
    interpreter = RatioInterpreter(industry)
    analysis: dict[str, Any] = {
        "current_analysis": {},
        "trend_analysis": {},
        "overall_health": {},
        "recommendations": [],
    }

    for category, cat_ratios in ratios.items():
        analysis["current_analysis"][category] = {}
        for name, val in cat_ratios.items():
            if isinstance(val, (int, float)):
                analysis["current_analysis"][category][name] = interpreter.interpret_ratio(name, val)

    if historical_data:
        for name, hist in historical_data.items():
            if "values" in hist and "periods" in hist:
                analysis["trend_analysis"][name] = interpreter.analyze_trend(
                    name, hist["values"], hist["periods"]
                )

    analysis["overall_health"] = _assess_health(analysis["current_analysis"])
    analysis["recommendations"] = _top_recommendations(analysis)
    analysis["report"] = interpreter.generate_report(ratios)
    return analysis


def _assess_health(current: dict[str, Any]) -> dict[str, Any]:
    score_map = {
        "Excellent": 4, "Good": 3, "Acceptable": 2, "Poor": 1,
        "Fair Value": 3, "Potentially Undervalued": 3,
        "Growth Premium": 2, "Expensive": 1, "N/A": 2,
    }
    scores = []
    for cat in current.values():
        for ratio in cat.values():
            r = ratio.get("rating_en", "N/A")
            scores.append(score_map.get(r, 2))
    avg = sum(scores) / len(scores) if scores else 0

    if avg >= 3.5:
        status, msg_en, msg_ja = "Excellent", "Strong health across metrics", "各指標が全般的に良好"
    elif avg >= 2.5:
        status, msg_en, msg_ja = "Good", "Healthy with some improvement areas", "概ね健全、一部改善余地あり"
    elif avg >= 1.5:
        status, msg_en, msg_ja = "Fair", "Mixed indicators — attention needed", "指標にばらつきあり — 注意が必要"
    else:
        status, msg_en, msg_ja = "Poor", "Significant challenges requiring action", "重大な課題があり早急な対応が必要"

    return {"status": status, "score": f"{avg:.1f}/4.0", "message_en": msg_en, "message_ja": msg_ja}


def _top_recommendations(analysis: dict[str, Any]) -> list[dict[str, str]]:
    recs: list[dict[str, str]] = []
    for cat in analysis["current_analysis"].values():
        for name, info in cat.items():
            if info.get("rating_en") == "Poor":
                recs.append({
                    "priority": "High",
                    "ratio": name,
                    "action_en": info.get("recommendation_en", ""),
                    "action_ja": info.get("recommendation_ja", ""),
                })
    for name, trend in analysis.get("trend_analysis", {}).items():
        if trend.get("trend") == "Deteriorating":
            recs.append({
                "priority": "Medium",
                "ratio": name,
                "action_en": f"Monitor: {name} showing negative trend",
                "action_ja": f"要注視: {name}が悪化傾向",
            })
    if not recs:
        recs.append({
            "priority": "Low",
            "ratio": "general",
            "action_en": "Continue current financial management practices",
            "action_ja": "現在の財務管理方針を継続",
        })
    return recs[:5]
