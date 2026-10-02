# Yahoo Finance API — Technical Notes

This document records the technical constraints and response structure of the Yahoo Finance public API as observed during development of this lab.
It exists so that any engineer or AI assistant working in this repository starts with correct assumptions rather than discovering these constraints through trial and error.

---

## Do Not Use an npm Wrapper

The `yahoo-finance2` npm package is **not reliable** for this use case:

- The package API changed significantly between major versions (v1 → v2)
- In v2.x, `historical()` and `quoteSummary()` were removed from the ESM build
- Only `quote()` and `autoc()` remain as instance methods in recent releases
- The wrapper adds an unnecessary dependency layer on top of a public HTTP API

**Use direct HTTP calls to the Yahoo Finance v8 API instead.** No npm wrapper is needed.

---

## Endpoints

### Quote (real-time snapshot) and Intraday history — same call

```
GET https://query2.finance.yahoo.com/v8/finance/chart/{SYMBOL}?interval=5m&range=1d
```

> Use `interval=5m&range=1d` — **not** `interval=1d&range=1d`.
> `interval=1d` returns only **1 data point** (end-of-day summary), which is useless for an intraday chart.
> `interval=5m` returns 5-minute candles for the full trading session **and** keeps `meta` up-to-date.

### Historical OHLCV (7-day and quarterly views)

```
GET https://query2.finance.yahoo.com/v8/finance/chart/{SYMBOL}?interval=1d&period1={UNIX_SECONDS}&period2={UNIX_SECONDS}
```

> **Note:** Use `query2.finance.yahoo.com` as the primary host.
> `query1` may time out depending on network routing. Both mirror the same data.

### Required request headers

```
User-Agent: Mozilla/5.0 (compatible; finance-dashboard/1.0)
Accept: application/json
```

---

## Response Structure

Both endpoints return the same JSON envelope:

```json
{
  "chart": {
    "result": [
      {
        "meta": { ... },
        "timestamp": [1720000000, 1720086400, ...],
        "indicators": {
          "quote": [{ "open": [...], "high": [...], "low": [...], "close": [...], "volume": [...] }],
          "adjclose": [{ "adjclose": [...] }]
        }
      }
    ],
    "error": null
  }
}
```

Access path: `data.chart.result[0]`

---

## Key Fields in `meta`

| Field | Notes |
|---|---|
| `symbol` | Ticker symbol |
| `longName` | Full company name |
| `shortName` | Short display name |
| `regularMarketPrice` | Current / last traded price |
| `chartPreviousClose` | Previous session close — **use this, not `previousClose`** |
| `regularMarketVolume` | Volume for the current session |
| `fiftyTwoWeekHigh` | 52-week high |
| `fiftyTwoWeekLow` | 52-week low |
| `regularMarketTime` | Unix timestamp (seconds) of the last price update |
| `marketCap` | Market capitalisation (not always present) |
| `averageDailyVolume3Month` | 3-month average daily volume (not always present) |

> **Important:** The fields `regularMarketChange` and `regularMarketChangePercent` are **not present** in the v8 chart API response. Compute them manually:
>
> ```
> change    = regularMarketPrice - chartPreviousClose
> changePct = (change / chartPreviousClose) × 100
> ```

---

## OHLCV History

The `timestamp` array and the arrays inside `indicators.quote[0]` are positionally aligned (same index = same candle).

Filter out rows where `close` is `null` or `0` — these appear on non-trading days or around corporate actions.

### Timestamp conversion — daily vs intraday

**Daily (7d / quarter):**
```js
new Date(unixSeconds * 1000).toISOString().slice(0, 10)  // → "2026-07-13"
```

**Intraday (5-minute candles):**
```js
new Date(unixSeconds * 1000).toISOString()  // → "2026-07-13T13:30:00.000Z"
```

> **Critical:** Do **not** truncate intraday timestamps to `YYYY-MM-DD`.
> If all intraday points share the same date string, chart libraries collapse them into a single data point — the chart shows only one tick with a flat line.
> Keep the full ISO timestamp for intraday data; only truncate to date for daily candles.

### Intraday display

When rendering intraday data in a chart:
- Format X-axis ticks as `HH:MM` (local time), not the raw ISO string
- Show **absolute price** on the Y-axis, not % return (the intraday price range is typically < 3%, so % return appears flat)
- Skip the volume bar chart for intraday — 5-minute volume bars are too granular to be readable

---

## Proxy Implementation Pattern

The React app cannot call Yahoo Finance directly due to CORS. A lightweight Node/Express proxy is the standard approach:

1. Vite dev server proxies `/api/*` → `localhost:3001`
2. Express server on port 3001 calls Yahoo Finance, applies caching and deduplication, returns normalised-ish JSON
3. The React app normalises the response into typed domain models (`StockQuote`, `HistoryPoint`)

Cache TTLs that work well:
- Quote / intraday: 60 s
- History (7d): 300 s (5 min)
- History (quarter): 3600 s (1 hr)

### Route design for the history endpoint

The "day" range requires a different URL pattern than 7d/quarter. Recommended proxy route signature:

```
GET /api/history/:symbol?range=day                                    → intraday, interval=5m
GET /api/history/:symbol?range=7d&period1=YYYY-MM-DD&period2=YYYY-MM-DD → daily, interval=1d
GET /api/history/:symbol?range=quarter&period1=...&period2=...        → daily, interval=1d
```

The client passes `range` so the proxy can choose the correct Yahoo Finance parameters without the React app needing to know the URL shape.
