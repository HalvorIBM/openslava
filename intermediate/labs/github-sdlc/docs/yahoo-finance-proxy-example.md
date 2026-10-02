# Yahoo Finance API — Proxy Example

Minimal working examples for calling the Yahoo Finance v8 API from a Node.js proxy.
See [`yahoo-finance-api-notes.md`](yahoo-finance-api-notes.md) for full field reference and response structure.

---

## curl Examples

### Current quote + intraday candles for IBM

```bash
# interval=5m gives 5-min candles AND up-to-date meta — use this, not interval=1d
curl -s \
  -H "User-Agent: Mozilla/5.0" \
  -H "Accept: application/json" \
  "https://query2.finance.yahoo.com/v8/finance/chart/IBM?interval=5m&range=1d" \
  | jq '.chart.result[0].meta | {symbol, regularMarketPrice, chartPreviousClose, fiftyTwoWeekHigh, fiftyTwoWeekLow}'
```

### Intraday candles (first 3 ticks)

```bash
curl -s \
  -H "User-Agent: Mozilla/5.0" \
  -H "Accept: application/json" \
  "https://query2.finance.yahoo.com/v8/finance/chart/IBM?interval=5m&range=1d" \
  | jq '[.chart.result[0].timestamp[:3][] | . * 1000 | . / 1000 | todate]'
# → ["2026-07-13T13:30:00Z", "2026-07-13T13:35:00Z", "2026-07-13T13:40:00Z"]
```

### 7-day history for IBM

```bash
# period1 and period2 are Unix timestamps in seconds
curl -s \
  -H "User-Agent: Mozilla/5.0" \
  -H "Accept: application/json" \
  "https://query2.finance.yahoo.com/v8/finance/chart/IBM?interval=1d&period1=1719792000&period2=1720396800" \
  | jq '.chart.result[0] | {timestamps: .timestamp[:3], first_close: .indicators.quote[0].close[:3]}'
```

---

## Minimal Node.js Proxy Route (Express + native fetch)

```typescript
import express from 'express';

const app = express();

const YF_HEADERS = {
  'User-Agent': 'Mozilla/5.0 (compatible; finance-dashboard/1.0)',
  'Accept': 'application/json',
};

// GET /api/quote/:symbol
app.get('/api/quote/:symbol', async (req, res) => {
  const symbol = req.params.symbol.toUpperCase();
  const url = `https://query2.finance.yahoo.com/v8/finance/chart/${symbol}?interval=1d&range=1d`;

  const raw = await fetch(url, { headers: YF_HEADERS }).then(r => r.json());
  const meta = raw.chart.result[0].meta;

  const price     = Number(meta.regularMarketPrice);
  const prevClose = Number(meta.chartPreviousClose);  // ← use chartPreviousClose, not previousClose
  const change    = price - prevClose;

  res.json({
    symbol:                     meta.symbol,
    longName:                   meta.longName ?? meta.shortName,
    regularMarketPrice:         price,
    regularMarketChange:        change,                           // ← computed, not from API
    regularMarketChangePercent: (change / prevClose) * 100,       // ← computed, not from API
    regularMarketVolume:        meta.regularMarketVolume,
    fiftyTwoWeekHigh:           meta.fiftyTwoWeekHigh,
    fiftyTwoWeekLow:            meta.fiftyTwoWeekLow,
    regularMarketTime:          meta.regularMarketTime,
  });
});

// GET /api/history/:symbol?period1=YYYY-MM-DD&period2=YYYY-MM-DD
app.get('/api/history/:symbol', async (req, res) => {
  const symbol  = req.params.symbol.toUpperCase();
  const { period1, period2 } = req.query as { period1: string; period2: string };

  // Yahoo Finance expects Unix seconds, not date strings
  const p1 = Math.floor(new Date(period1).getTime() / 1000);
  const p2 = Math.floor(new Date(period2).getTime() / 1000);
  const url = `https://query2.finance.yahoo.com/v8/finance/chart/${symbol}?interval=1d&period1=${p1}&period2=${p2}`;

  const raw       = await fetch(url, { headers: YF_HEADERS }).then(r => r.json());
  const result    = raw.chart.result[0];
  const timestamps = result.timestamp as number[];
  const ohlcv      = result.indicators.quote[0];

  const history = timestamps
    .map((t: number, i: number) => ({
      date:   new Date(t * 1000).toISOString().slice(0, 10),
      open:   ohlcv.open[i]   ?? 0,
      high:   ohlcv.high[i]   ?? 0,
      low:    ohlcv.low[i]    ?? 0,
      close:  ohlcv.close[i]  ?? 0,
      volume: ohlcv.volume[i] ?? 0,
    }))
    .filter((p: { close: number }) => p.close > 0);  // skip non-trading rows

  res.json(history);
});

app.listen(3001);
```

---

## Notes

- `native fetch` is available in Node ≥ 18 — no `node-fetch` package needed.
- Add in-memory caching (Map + TTL) to avoid hitting Yahoo Finance on every browser request.
- Add a deduplication guard so simultaneous requests for the same symbol only trigger one upstream call.
