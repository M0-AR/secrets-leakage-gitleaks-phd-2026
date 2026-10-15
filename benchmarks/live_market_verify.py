"""Live-market verification (recorded 2026-10-15 UTC, re-fetchable).

Recorded via agent-reach_stock_quote (yfinance) + openresearch_get_company_financials (SEC EDGAR):
- UBER $69.69 (+0.55%), mcap $142.35B, PE 15.73, 2026-10-15.
- Revenue 2025 $52.017B; $148M settlement = 0.284% of revenue, 1.47% of 2025 net income.
- FTC 20-year order (until ~2038) dwarfs the fine: biennial audits + covered-incident reporting.

Run: python3 live_market_verify.py [--offline]  (offline uses recorded snapshot).
"""
import json, sys, urllib.request

SNAPSHOT = {
    "date_utc": "2026-10-15", "symbol": "UBER", "price": 69.69, "mcap": 142346027008,
    "revenue_2025": 52017000000, "net_income_2025": 10053000000,
    "settlement_usd": 148000000,
}

def try_live():
    try:
        with urllib.request.urlopen(
            "https://query1.finance.yahoo.com/v8/finance/chart/UBER?interval=1d&range=1d",
            timeout=8) as r:
            d = json.load(r)
            px = d["chart"]["result"][0]["meta"]["regularMarketPrice"]
            return float(px)
    except Exception as e:
        return None

if __name__ == "__main__":
    live = None if "--offline" in sys.argv else try_live()
    s = dict(SNAPSHOT)
    if live:
        s["price_live"] = live
    s["settlement_pct_revenue"] = round(148_000_000 / 52_017_000_000 * 100, 4)
    s["settlement_pct_net_income"] = round(148_000_000 / 10_053_000_000 * 100, 3)
    print(json.dumps(s, indent=2))
    print("\nInterpretation: fine <0.3% revenue; real cost = 20-yr FTC audits + "
          "cover-up criminal exposure (Sullivan convicted 2022 per DOJ non-prosecution 2022).")
