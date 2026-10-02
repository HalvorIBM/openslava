# Workshop Context — IBM Bob Hints

This file provides context for Bob when working in this repository during the finance dashboard lab.
It is not part of the workshop material intended for participants.

---

## What This Repository Is

This is a workshop lab where participants ask Bob to build a React finance dashboard step by step.
The repository starts empty (only documentation). Bob generates the full application during the workshop.

The lab is hands-on: participants should see Bob build things from scratch, not find pre-written code.

---

## Yahoo Finance Integration — Critical Knowledge

**Do not use the `yahoo-finance2` npm package.** It has an unstable API across versions and the ESM build in v2.x removes most methods. Always implement the proxy using direct HTTP calls.

The correct implementation is documented in [`docs/yahoo-finance-api-notes.md`](../docs/yahoo-finance-api-notes.md) and [`docs/yahoo-finance-proxy-example.md`](../docs/yahoo-finance-proxy-example.md).

### Key facts to apply immediately when generating the proxy:

1. **Endpoint:** `https://query2.finance.yahoo.com/v8/finance/chart/{SYMBOL}`
2. **Quote + intraday params:** `?interval=5m&range=1d` — **not** `interval=1d`. Using `interval=1d` returns only 1 data point (end-of-day summary); `interval=5m` returns all 5-minute candles for the session and keeps `meta` current.
3. **History params (7d / quarter):** `?interval=1d&period1={UNIX_SECONDS}&period2={UNIX_SECONDS}` (convert YYYY-MM-DD dates to Unix seconds)
4. **Required headers:** `User-Agent: Mozilla/5.0`, `Accept: application/json`
5. **Response path:** `data.chart.result[0].meta` for quote metadata, `data.chart.result[0].indicators.quote[0]` for OHLCV arrays
6. **Change computation:** `regularMarketChange` and `regularMarketChangePercent` are **absent** from the response — compute manually: `price - meta.chartPreviousClose` (note: `chartPreviousClose`, not `previousClose`)
7. **Host:** Use `query2` — `query1` may time out on some networks
8. **Timestamp preservation:** For intraday candles, store the **full ISO timestamp** (`2026-07-13T13:30:00.000Z`), not just the date (`2026-07-13`). Truncating all intraday points to the same date string collapses the entire series into a single chart point.
9. **Intraday chart rendering:** Show absolute price (USD) on Y-axis, format X-axis ticks as `HH:MM`. Do not use % return for intraday — the range is too small and appears flat.
10. **Proxy route design:** Route `?range=day` to the intraday fetcher; route `?range=7d` and `?range=quarter` (with `period1`/`period2`) to the daily fetcher.

### Proxy architecture:

- Express server on port 3001 (Node, ESM, run with `tsx`)
- Vite dev server proxies `/api/*` → `localhost:3001`
- In-memory cache with per-key TTL (Map)
- Deduplication guard for simultaneous requests (inFlight Map)
- Run with: `npm run dev:full` (concurrently starts proxy + Vite)

---

## Workshop Flow

When a participant follows the workshop prompts in `WORKSHOP-part1-BUILD.md`:

- **Step A:** Analyse the repository — read `docs/yahoo-finance-api-notes.md` as part of the review
- **Step B:** Scaffold the React app with Vite + TypeScript + TanStack Query + Recharts
- **Step C:** Build the data layer — use direct HTTP calls as described above, **not** any npm Yahoo Finance wrapper
- **Step D:** Build dashboards for 3 time ranges (day, 7d, quarter) for Euro Stoxx 50, DAX, Nikkei 225, Dow Jones 30 Industrial, MSCI World
- **Step E:** Add tests (Vitest + React Testing Library + MSW)
- **Step F:** Review diff, write commit message and PR description

---

## Indices

Default index set:
- Euro Stoxx 50 — ISIN EU0009658145
- DAX — ISIN DE0008469008
- Nikkei 225 — ISIN XC0009692440
- Dow Jones 30 Industrial — ISIN US2605661048
- MSCI World — ISIN GB00BJDQQQ59

> **Note:** Yahoo Finance uses the ISIN or a specific symbol for indices (e.g. `^STOXX50E`, `^GDAXI`, `^N225`, `^DJI`, `URTH`). Use the Yahoo Finance symbol for API calls, not the ISIN.

---

## CI Workflow Note

The existing `.github/workflows/finance-app-ci.yml` uses `working-directory: finance-app` and
runs `npm run lint`, `npm run type-check`, `npm run test`, `npm run build` in sequence.
All four scripts must exist in `finance-app/package.json`.

**Node version:** Always use **Node 24** in the CI workflow (`node-version: 24`). Node 22 and below
are deprecated on GitHub Actions runners. `@types/node` is pinned to `^24.x` accordingly.

---

## Recharts Version

Use **Recharts v3** (`"recharts": "^3.0.0"`). The v2 branch is no longer maintained (npm install
prints a deprecation warning for every install).

### v2 → v3 breaking changes relevant to this project

The `Tooltip` prop types changed in v3:

- `formatter` receives `value: ValueType | undefined` (not `number`) — wrap with `Number(value)`
- `labelFormatter` receives `label: ReactNode` (not `string`) — wrap with `String(label)`

**Fix applied in [`src/components/StockChart/StockChart.tsx`](../finance-dashboard/src/components/StockChart/StockChart.tsx):**
```tsx
<Tooltip
  formatter={(value) => [formatPrice(Number(value)), '']}
  labelFormatter={(label) => formatTick(String(label), range)}
/>
```

---

## Testing — Known Pitfalls (from live test run)

These issues will silently break tests if not addressed upfront. Apply them when generating the test setup.

### 1. ResizeObserver not defined in jsdom
Recharts' `ResponsiveContainer` calls `ResizeObserver` internally. jsdom does not implement it.
**Fix:** Add this to `tests/setup.ts` (the Vitest setup file):
```ts
global.ResizeObserver = class ResizeObserver {
  observe() {}
  unobserve() {}
  disconnect() {}
};
```
Without this, every test that renders a chart component crashes with `ResizeObserver is not defined`,
and the component falls into its ErrorBoundary — making ticker assertions like `getByText('IBM')` fail.

### 2. CSS `text-transform: uppercase` is invisible to RTL queries
`screen.getByText('INTRADAY')` will fail if the DOM text node is `"Intraday"` and only CSS makes it appear uppercase.
**Fix:** Always match the actual DOM string: `screen.getByText('Intraday')`.

### 3. `vitest/globals` — correct tsconfig type reference
The correct entry in `tsconfig.json` `compilerOptions.types` is `"vitest/globals"` (not `"@vitest/globals"`).
`@vitest/globals` does not exist as a package. The missing type reference causes `beforeAll`, `afterEach`,
`afterAll`, `describe`, `it`, `expect` to be unknown to the TypeScript compiler.

### 4. `noUncheckedIndexedAccess: true` — array access needs guards
With strict TS config, `arr[0]` returns `T | undefined`. All array accesses in source and test files
need either a nullish check (`arr[0]?.field`) or a non-null assertion (`arr[0]!.field`).

### 5. `jsdom` must be an explicit devDependency
Vitest reports `Cannot find dependency 'jsdom'` at startup if `jsdom` is not listed explicitly in
`devDependencies`, even though it may be installed transitively as a peer dependency.
**Fix:** Always include `"jsdom": "^29.x"` (or latest) in `devDependencies` alongside `vitest`.

### 6. `@types/cors` required for proxy type-check
The `cors` npm package ships without bundled TypeScript declarations. Without `@types/cors`,
`tsc --noEmit` fails with TS7016 (`implicitly has 'any' type`) on the `import cors from 'cors'` line
in `proxy/server.ts`.
**Fix:** Add `"@types/cors": "^2.8.x"` to `devDependencies`.

### 7. Single validation command
Always generate a `check` script in `package.json` that runs the full pipeline in one shot:
```json
"check": "npm run lint && npm run type-check && npm run test && npm run build"
```
This is what participants use in Step E and what the CI workflow maps to individual steps.

### 8. CSS Modules — missing type declaration crashes typecheck
TypeScript does not know about `*.module.css` files by default. Without a declaration file every
`import styles from './Foo.module.css'` is a TS2307 error.
**Fix:** Add `src/vite-env.d.ts` (or any `.d.ts` in the `src/` include path):
```ts
declare module '*.module.css' {
  const classes: Record<string, string>;
  export default classes;
}
```

### 9. `tsconfig.json` — do not add `references` to the root typecheck config
Adding `"references": [{ "path": "./tsconfig.app.json" }]` to the root `tsconfig.json` triggers
TypeScript composite project mode and produces TS6305 errors ("output file has not been built from
source file") for every source file. The root config is the `--noEmit` typecheck config and must
stand alone. Only `tsconfig.app.json` (the emit config used by `vite build`) gets `"composite": true`.

### 10. `vitest/globals` — use triple-slash reference in setup file, not `compilerOptions.types`
The most reliable way to expose `beforeAll` / `afterAll` / `describe` / `it` / `expect` in the
Vitest setup file is a triple-slash directive at the top of `tests/setup.ts`:
```ts
/// <reference types="vitest/globals" />
```
This avoids having to modify `tsconfig.json` and works regardless of how `globals: true` is set
in `vitest.config.ts`.
