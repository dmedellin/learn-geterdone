# capkit_b report: Volumes II and III modes

## Files changed

- `scripts/mathpath/labs/capkit_b.py`: new file. It holds the eight modes, `capkit_b_lab(cfg)` and the JS blocks
  KB_COMMON_JS, TURNOVER_JS, SCHEMES_JS, PROFIT_JS, PRICES_JS, TENDENCY_JS, INTEREST_JS, RENT_JS and REVENUE_JS.
- `scripts/mathcheck.js`: one block inserted between `// ---- capkit_b (Volumes II and III modes) ----` and
  `// ---- end capkit_b ----`, immediately after `// ---- end capkit (Volume I modes) ----` and before the final verdict. It has 77 cases.
- Not touched: capkit.py, capkit_core.py, the registry, and anything under site/. capkit.py already dispatches the
  B modes to `capkit_b.capkit_b_lab`. No commits, no branch switches.
- Scratch work, outside the repo, under `/tmp/claude-0/-home-claude/52c4c1c4-2505-5c40-a28f-55e7509d8718/scratchpad/kit-b/`:
  - `fixtures.py`: 46 cfgs with hand-derived pinned tiles.
  - `build.py`: renders them through `render.lesson_page_with_lab` with the registry key "capkit".
  - `out/pages/*.html` and `out/manifest/expect.json`: the rendered pages and their manifest.
  - `observe.txt`: the `--observe` output.
  - `kb_block.js`: the mathcheck block, byte-identical to the one in mathcheck.js.
  - `harness.js` and `mutate.py`: the mutation-testing tools.
  - `mutations.json`: the mutation results.
- Updated `kit-b-requests.md`. The earlier requests are now satisfied by core. One optional request remains: digit grouping inside a fractional penny.

## Verification

- `node scripts/labcheck.js --expect .../kit-b/out/manifest/expect.json` (hostile-input sweep on) gave **46 pages executed and swept, 46 with pinned figures, 0 failing**.
  - The pages cover every view of every mode, plus all four dr2 price_cases.
  - `--observe` on all 46 printed no NaN, undefined, Infinity or object text.
  - The first run had 4 mismatches, and all 4 were wrong fixture expectations, not code errors:
    - Rent with A–D plus E: 60+180+300+420 = 960s, not 1,080s.
    - The worst-soil fixture lists only A and B, so its rents are 60s, 180s.
    - capPct now groups digits: 1,000%.
    - capMoney prints shillings as s/d.
- `capkit_lab({"mode": "nope"})` and an unknown view both raise ValueError.
- `node scripts/mathcheck.js`: the capkit_b section passes in full.
  - The first full run after inserting the block printed "every arithmetic assertion passes", exit 0.
  - My last runs each showed exactly one FAIL, every time in the **Volume I** section, and a different case each time: moCompute twice, then ciCompute.
  - capkit.py's mtime was changing between runs, so the other engineer was mutation-testing capkit.py in place. None of those failures touches capkit_b.

## Modes and views built (cfg["mode"] / cfg["view"])

| mode | prefix | views |
|---|---|---|
| turnover | tu | time, phases, fixed, aggregate, classify, working, advance, annual, merchant |
| schemes | sc | sort, simple, fixed, hoard, expanded (iterates) |
| profit | pr | cost, rate, relation, turnover, economy, price, books |
| prices | pp | rates, production, wage-rise, merchant, merchant-turnover |
| tendency | te | law (iterates), counter (iterates), overaccumulation |
| interest | in | split, bounds, capitalise, compound, usury |
| rent | rt | price, waterfall, dr1, dr2, absolute |
| revenue | rv | trinity, dogma, added-up, classes |

## cfg fields as implemented

Top-level keys:
- `mode`
- `view`
- `money_unit`: "£", "s" or "hours"; the default is "£".
- `qty_unit`
- `presets`: a list of {id, label?, ...fields, expect?}.
- `periods`: only on iterating views; the default is 4. On any other view it raises.
- `price_case`: rent/dr2 only. It is one of constant, falling, rising or worst-soil. Each preset is checked against it at build time.
- `stage`, `hold` and `test`: rejected.

Preset fields by view:

- turnover
  - time: production_weeks, working_weeks (opt), circulation_weeks, year_weeks, capital (opt)
  - phases: stage_weeks (3 nums)
  - fixed: fixed (records name, value, life_years, repairs_per_year opt, replacement_value opt, appears_year opt), age_years
  - aggregate: fixed, circulating, circ_turnovers
  - classify: items (records name, capital label, value, fixed yesno, variable yesno), s_rate
  - working: working_weeks, weekly_outlay
  - advance: working_weeks, circulation_weeks, weekly_outlay, new_outlay (opt), year_weeks
  - annual: variable, s_rate, working_weeks, circulation_weeks, year_weeks
  - merchant: merchant_capital, merchant_turnovers
- schemes
  - sort: products (records name, department, value opt)
  - simple: I and II, each {c, v, s} or [c, v, s]
  - fixed: I, II, wear_set_aside, renewals
  - hoard: I, I_accumulate_share, hoarders_share
  - expanded: I, II, I_accumulate_share, composition_I (opt), composition_II (opt)
- profit
  - cost and books: c, v, s, sale_price (opt)
  - rate and relation: c, v, s
  - turnover: c, v, s, turnovers
  - economy: c, v, s, c_change
  - price: c, v, s, c_change, price_passed_on
- prices
  - rates: spheres (records name, c, v, c_used opt, s_rate opt), s_rate
  - production: spheres, s_rate, premiums (records sphere, rate)
  - wage-rise: spheres, profit_rate, wage_rise, average (a sphere name or empty)
  - merchant: spheres, s_rate, merchant_capital, merchant_costs (opt)
  - merchant-turnover: profit_rate, merchant_turnovers, merchant_capital
- tendency
  - law: c, v, s_rate, c_step, capital_growth. The last two each take one figure or a list of one per period.
  - counter: the law fields, plus s_rate_step and c_cheapening
  - overaccumulation: c, v, s_rate, added_capital, devalued_share
- interest
  - split and bounds: capital, profit_rate, interest_rate, principal (opt), manager_salary (opt)
  - capitalise: income, interest_rate
  - compound: principal, interest_rate, years (0–5000), real_growth
  - usury: debt, interest_rate, surplus, holding_value, years (1–100)
- rent
  - price: rent, interest_rate, improvement_interest (opt)
  - waterfall: cost_steam, cost_water, profit_rate
  - dr1: soils (records soil, capital, output; in a cfg also {name, capital, outputs: [..]}), profit_rate, regulating ("auto", "B" or "B2"), market_limit (opt)
  - dr2: the dr1 fields, plus former_price (opt)
  - absolute: agri {c, v}, industry {c, v}, s_rate, market_limit (opt)
- revenue
  - trinity: c, v, s, split {interest, rent}. A cfg may also give split_interest and split_rent directly.
  - dogma: c, v, s
  - added-up: the trinity fields, plus wage_change
  - classes: people (records name, source; or {name, wages, profit, rent})

## Tile ids and exact formats (each example is observed on a built page)

### turnover

| view | tile | example |
|---|---|---|
| time | tuTurnover | `13 weeks` |
| time | tuTurnovers | `4 a year (a 52-week year)` |
| time | tuWorkingShare | `1 = 100%` |
| time | tuCirculationShare | `0 = 0%` |
| time | tuAggregate | `£1,600 turned over on £400 advanced` |
| phases | tuTurnover | `13 weeks` |
| phases | tuTurnovers | `4 a year (a 52-week year)` |
| phases | tuMoney | `1/13 = 7.69%` |
| phases | tuProductive | `8/13 = 61.54%` |
| phases | tuCommodity | `4/13 = 30.77%` |
| fixed | tuWear | `£1,000 a year` |
| fixed | tuRemaining | `£6,000 after 4 years` |
| aggregate | tuAggregate | `£108,000 a year on £100,000 advanced` |
| aggregate | tuAverage | `27/25 turnovers a year` |
| aggregate | tuWear | `£8,000 a year` |
| classify | tuFixed | `A: fixed £250, circulating £750; B: fixed £250, circulating £750` |
| classify | tuVariable | `A: constant £750, variable £250; B: constant £500, variable £500` |
| classify | tuS | `A £250, B £500` |
| working | tuAdvance | `£1,200` |
| advance | tuAdvance | `£1,200 = I £900 + II £300` |
| advance | tuFreed | `£300 each working period` |
| advance | tuTurnovers | `25/6 a year (a 50-week year)` |
| annual | tuTurnover | `5 weeks` |
| annual | tuTurnovers | `10 a year (a 50-week year)` |
| annual | tuAnnualRate | `10 = 1,000%` |
| annual | tuMassS | `£5,000 a year` |
| merchant | tuFreed | `£500` |

### schemes

| view | tile | example |
|---|---|---|
| sort | scDeptI | `400: coal for mills, machines` |
| sort | scDeptII | `50: bread` |
| simple | scDeptI | `4,000c + 1,000v + 1,000s = 6,000` |
| simple | scDeptII | `2,000c + 500v + 500s = 3,000` |
| simple | scBalance | `I(v + s) = 2,000 = IIc` |
| simple | scIExchange | `2,000 each way` |
| simple | scWithinI | `4,000` |
| fixed | scBalance | `I(v + s) = 2,000 = IIc` |
| fixed | scFixedGap | `0: renewals = wear hoarded` |
| hoard | scHoardGap | `+500: 500 of surplus product unsold` |
| expanded | scDeptI | `4,000c + 1,000v + 1,000s = 6,000` |
| expanded | scDeptII | `1,500c + 750v + 750s = 3,000` |
| expanded | scBalance | `I(v + s) = 2,000, IIc = 1,500: gap +500` |
| expanded | scYear2 | `I 4,400c + 1,100v; II 1,600c + 800v` |
| expanded | scGrowth | `9,000 to 9,800: 4/45 = 8.89%` |

### profit

| view | tile | example |
|---|---|---|
| cost | prCost | `£500` |
| cost | prProfit | `£100` |
| rate | prRate | `1/5 = 20%` |
| rate | prSRate | `1 = 100%` |
| relation | prRate | `1/5 = 20%` |
| relation | prSRate | `3/2 = 150%` |
| turnover | prAnnual | `1/2 = 50%` |
| turnover | prRate | `1/10 = 10%` |
| turnover | prSRate | `1 = 100%` |
| economy | prRate | `1/4 = 25%` |
| economy | prCost | `£400` |
| price | prRate | `1/6 = 16.67%` |
| price | prProfit | `£100` |
| price | prCost | `£600` |
| books | prProfit | `£100` |
| books | prRate | `1/5 = 20%` |
| books | prCost | `£500` |

### prices

| view | tile | example |
|---|---|---|
| rates | ppRates | `1/10 = 10%, 9/10 = 90%` |
| production | ppAverage | `11/50 = 22%` |
| production | ppPrices | `£92, £103, £113, £77, £37` |
| production | ppTotals | `values £422 = prices £422; s £110 = profit £110` |
| wage-rise | ppAverage | `1/7 = 14.29%` |
| wage-rise | ppPrices | `£900/7, £120, £816/7` |
| merchant | ppAverage | `9/50 = 18%` |
| merchant | ppMerchantPrice | `industrial £1,062; merchant £1,080` |
| merchant-turnover | ppMarkup | `3/100 = 3%` |
| merchant-turnover | ppMerchantPrice | `buys at £100, sells at £103` |

### tendency

| view | tile | example |
|---|---|---|
| law | teRate | `1/5 = 20%` |
| law | teMass | `£100` |
| counter | teRate | `1/4 = 25%` |
| counter | teMass | `£150` |
| counter | teOffset | `25/3 of 25/3 points` |
| overaccumulation | teRate | `1/15 = 6.67%` |
| overaccumulation | teMass | `£100` |

### interest

| view | tile | example |
|---|---|---|
| split | inInterest | `£5` |
| split | inEnterprise | `£15` |
| bounds | inInterest | `£5` |
| bounds | inEnterprise | `£15` |
| bounds | inBound | `0 < 5% < 20%` |
| capitalise | inPrice | `£2,000` |
| compound | inCompound | `1d × (21/20)^1780: 37 digits before the point, in shillings` |
| compound | inReal | `1d × (101/100)^1780: 7 digits before the point, in shillings` |
| usury | inInterest | `£15 in year 1` |
| usury | inYearsToRuin | `year 6` |

### rent

| view | tile | example |
|---|---|---|
| price | rtPrice | `£4,000` |
| price | rtTrueRent | `£200` |
| waterfall | rtPrice | `£115` |
| waterfall | rtSurplusProfit | `£10 against the steam user's profit; £11½ against its own price of production` |
| dr1 | rtPrice | `60s a qr` |
| dr1 | rtRents | `0s, 60s, 120s, 180s` |
| dr1 | rtTotal | `360s` |
| dr2 | rtPrice | `60s a qr` |
| dr2 | rtRents | `0s, 300s` |
| dr2 | rtTotal | `300s` |
| absolute | rtPrice | `£120` |
| absolute | rtAbsolute | `up to £5` |

### revenue

| view | tile | example |
|---|---|---|
| trinity | rvTotal | `£300` |
| trinity | rvWages | `£100` |
| trinity | rvRent | `£30` |
| trinity | rvInterest | `£20` |
| trinity | rvProfitShare | `£50` |
| dogma | rvTotal | `£9,000` |
| dogma | rvSmith | `v + s = £3,000; c = £6,000 missing` |
| added-up | rvWages | `£120` |
| added-up | rvRent | `£24` |
| added-up | rvInterest | `£16` |
| added-up | rvProfitShare | `£40` |
| classes | rvClassCount | `3 groups: wages, profit, rent` |


Other forms the same tiles take:
- scFixedGap: `−100: 100 of Department I's product unsold` or `+100: Department I 100 short`.
- scHoardGap: `0: hoarders' sales = investors' purchases` or `−500: 500 of demand without a product`.
- scIExchange: `2,000 each way; 100 of Department I's product unsold`.
- scGrowth and scYear2: `refused in period n`.
- tuFreed: `£600 released` (with new_outlay) or `£X more tied up`.
- tuAggregate in the time view prints `—` when capital is empty.
- teOffset: `no fall to offset`.
- inBound: `breached: 25% ≥ 20%`.
- inYearsToRuin: `repaid in year n` or `never within n years`.
- inCompound when short: `2,000s × (21/20)^10 = 3,257s 9 602934603/1280000000 d`.
- rtPrice in dr views: `120s a qr`.
- rtAbsolute: `up to £2`, with market_limit.
- ppMerchantPrice in the merchant-turnover view: `buys at £100, sells at £103`.

## mathcheck cases (77) and mutation evidence

- The block loads RATIONAL_JS, capkit_core's CAP_CORE_JS and the nine capkit_b blocks into its own vm context.
- Every pure helper is called on Marx's figures, and each mode's entry function is checked once on its exact tile string.
- Figures used:
  - Volume II: ch. 7 13 weeks/4 turnovers; ch. 8 £10,000 over 10 years; ch. 9 £108,000 on £100,000 = 27/25; ch. 15 £1,200 = I £900 + II £300, £300 freed; ch. 16 1,000% and 100%, mass £5,000; ch. 20 I(v + s) = 2,000 = IIc; ch. 21 4,400c + 1,100v / 1,600c + 800v, 9,000→9,800.
  - Volume III: ch. 1 500, 1/5; ch. 9 11/50 and prices 92, 103, 113, 77, 37, totals 422/422/110; ch. 11 1/7 and 900/7, 120, 816/7; ch. 13 2/3→1/5; ch. 15 1/10→1/15; ch. 17 9/50, 1,062, 1,080; ch. 18 3/100; ch. 21 £5/£15; ch. 29 £2,000; ch. 36 ruin in year 6; ch. 37 £4,000; ch. 38 10 and 11½; ch. 39 0, 60, 120, 180; ch. 44 worst soil pays 60; ch. 45 up to 5; ch. 48/50 30/20/50 → 24/16/40; Price's penny at 5% for 1,780 years: 37 digits in shillings.
- How the mutations were run (78 in all, covering every function):
  - `mutate.py` breaks one function in a copy of capkit_b.py.
  - It then runs the identical block, through `harness.js`, which has the same `blockFrom`/`eq` as mathcheck.js, against that copy.
  - Using a copy kept the shared file untouched during a full 78-run sweep.
  - Result: **78 of 78 caught**, and the clean source passes, 77/77.
  - The first sweep left 3 survivors: the growth/step order in kbTePath, the 40-character threshold in kbInSum, and the market limit met exactly in kbRtRegulate. I tightened the cases until all three were caught.
- Three mutations were also run on the real capkit_b.py under the full `node scripts/mathcheck.js`, restoring the exact bytes afterwards (sha256 e1ab925b… checked):

| mutation | full-run result |
|---|---|
| kbPpProduction: cost from c, not used-up c | exit 1; `FAIL kbPpProduction: Marx's ch. 9 table: got 11/50; 122, 122, 122, 122, 122 …`, `FAIL kbPrices: the prices tile` |
| kbTuAdvance: frees working, not circulation | exit 1; `FAIL kbTuAdvance: ch. 15 …: got 900, 300, 1200, 900` |
| kbRtCase: worst-soil comparison flipped | exit 1; `FAIL kbRtCase: ch. 44, the worst soil yields rent: got rising false` |

  After each restore, the capkit_b section passed. The other FAIL lines in those runs came from the Volume I section, which was being edited concurrently.

| function mutated | result | cases that failed |
|---|---|---|
| kbFloor | caught | kbFloor: toward minus infinity |
| kbFig | caught | kbFig and kbSigned; kbScTotal and kbScText; kbScSimple: ch. 20; kbScBalanceText: an imbalance; kbScStep: Marx's first example of expanded reproduction; kbSchemes: the growth tile |
| kbSigned | caught | kbFig and kbSigned; kbScBalanceText: an imbalance |
| kbWeeks | caught | kbWeeks, kbYears, kbTimes, kbPlural |
| kbYears | caught | kbWeeks, kbYears, kbTimes, kbPlural |
| kbTimes | caught | kbWeeks, kbYears, kbTimes, kbPlural |
| kbPlural | caught | kbWeeks, kbYears, kbTimes, kbPlural |
| kbPpCvR | caught | kbPpCvR: Chapter 45's agriculture |
| kbVulgar | caught | kbVulgar: Marx's 11½ (Vol. III ch. 38); kbMoneyV: pounds with a vulgar fraction |
| kbMoneyV | caught | kbMoneyV: pounds with a vulgar fraction |
| kbPctNum | caught | kbPctNum and kbPctShort |
| kbPctShort | caught | kbPctNum and kbPctShort |
| kbApprox | caught | kbApprox |
| kbGuard | caught | kbGuard: a thrown sentence becomes the refusal |
| kbTuTime | caught | kbTuTime: 9 + 4 weeks, 4 a year; kbTuTime: India, 12 weeks |
| kbTuFixed | caught | kbTuFixed: moral depreciation (ch. 8) |
| kbTuAggregate | caught | kbTuAggregate: Marx's ch. 9 figures; kbTurnover: the aggregate tile |
| kbTuClassify | caught | kbTuClassify: fixed/circulating against constant/variable |
| kbTuAdvance | caught | kbTuAdvance: ch. 15, working period longer: capital II set free |
| kbTuAdvance (multiple rule) | caught | kbTuAdvance: equal, a whole multiple, and the excess |
| kbTuRescale | caught | kbTuRescale: halving the outlay releases £600 |
| kbTuAnnual | caught | kbTuAnnual: ch. 16 capital A, 1,000% |
| kbTurnover | caught | kbTurnover: the aggregate tile |
| kbScTotal | caught | kbScTotal and kbScText; kbScRun: 9,000 to 9,800 in a year; kbSchemes: the growth tile |
| kbScText | caught | kbScDept |
| kbScSimple | caught | kbScSimple: ch. 20; kbScBalanceText: an imbalance |
| kbScBalanceText | caught | kbScBalanceText: an imbalance |
| kbScFixedGap | caught | kbScFixedGap: renewals less wear |
| kbScHoardGap | caught | kbScHoardGap: ch. 21 §1 |
| kbScStep | caught | kbScStep: Marx's first example of expanded reproduction; kbScRun: 9,000 to 9,800 in a year; kbSchemes: the growth tile |
| kbScStep (refusal) | caught | kbScStep: II cannot match I |
| kbScRun | caught | kbScRun: 9,000 to 9,800 in a year; kbSchemes: the growth tile |
| kbScDept | caught | kbScDept |
| kbSchemes | caught | kbSchemes: the growth tile |
| kbPrCost | caught | kbPrCost and kbPrRate: ch. 1 |
| kbPrRate | caught | kbPrCost and kbPrRate: ch. 1; kbProfit: the rate tile |
| kbPrAnnual | caught | kbPrAnnual: s per turnover times n |
| kbPrPriceChange | caught | kbPrPriceChange: nothing passed on |
| kbProfit | caught | kbProfit: the rate tile |
| kbPpCv | caught | kbPpCv |
| kbPpRates | caught | kbPpRates: ch. 9 spheres at value |
| kbPpProduction | caught | kbPpProduction: Marx's ch. 9 table; kbPrices: the prices tile |
| kbPpProduction (premiums) | caught | kbPpProduction: a premium comes out of the same total |
| kbPpNewRate | caught | kbPpNewRate: ch. 11, 15 on 105; kbPpWageRise: ch. 11, exact (Marx prints 128 7/12 for 128 4/7) |
| kbPpWageRise | caught | kbPpWageRise: ch. 11, exact (Marx prints 128 7/12 for 128 4/7) |
| kbPpMerchant | caught | kbPpMerchant: ch. 17 |
| kbPpMarkup | caught | kbPpMarkup: ch. 18 |
| kbPrices | caught | kbPrices: the prices tile |
| kbTeAt | caught | kbTeAt; kbTePath: ch. 13, c from 50 to 400 on v 100; kbTendency: the rate tile |
| kbTePath | caught | kbTePath: growth first, then the step: the mass rises 2 to 3 |
| kbTePath (s' step) | caught | kbTePath: s' up and c cheapened |
| kbTeOver | caught | kbTeOver: ch. 15, the same mass on more capital |
| kbTendency | caught | kbTendency: the rate tile |
| kbInSplit | caught | kbInSplit: ch. 21, £5 and £15 |
| kbInBound | caught | kbInBound: 0 < i < p' |
| kbInPrice | caught | kbInPrice: ch. 29 |
| kbInCompound | caught | kbInCompound: exact over BigInt; kbInSum: short enough to print exactly; kbInSum: 41 characters is past the 40-character limit |
| kbInDigits | caught | kbInDigits: Price's penny at 5% for 1,780 years, in shillings |
| kbInUsury | caught | kbInUsury: ch. 36, ruin in year 6; kbInterest: the ruin tile |
| kbInUsury (repaid) | caught | kbInUsury: repaid in year 1 |
| kbInSum | caught | kbInSum: 41 characters is past the 40-character limit |
| kbInterest | caught | kbInterest: the ruin tile |
| kbRtPrice | caught | kbRtPrice: ch. 37, £200 at 5% |
| kbRtWaterfall | caught | kbRtWaterfall: ch. 38, 10 and 11½ |
| kbRtInvestments | caught | kbRtInvestments: ch. 39, price of production per quarter; kbRtRegulate and kbRtRents: ch. 39, the worst soil regulates; kbRtRegulate: a market of 7 is met exactly by D and C; kbRtCase: ch. 44, the worst soil yields rent; kbRtCase: the price against the former price; kbRent: the rents tile |
| kbRtRegulate | caught | kbRtRegulate and kbRtRents: ch. 39, the worst soil regulates; kbRtCase: ch. 44, the worst soil yields rent; kbRent: the rents tile |
| kbRtRegulate (limit) | caught | kbRtRegulate: a market of 7 is met exactly by D and C |
| kbRtRegulate (named) | caught | kbRtRegulate: an unknown regulator |
| kbRtRents | caught | kbRtRegulate and kbRtRents: ch. 39, the worst soil regulates; kbRtCase: ch. 44, the worst soil yields rent; kbRent: the rents tile |
| kbRtCase | caught | kbRtCase: ch. 44, the worst soil yields rent |
| kbRtCase (former) | caught | kbRtCase: the price against the former price |
| kbRtAbsolute | caught | kbRtAbsolute: a market limit; a higher composition yields none |
| kbRtAbsolute (rate) | caught | kbRtAbsolute: ch. 45, up to 5; kbRtAbsolute: a market limit; a higher composition yields none |
| kbRent | caught | kbRent: the rents tile |
| kbRvTrinity | caught | kbRvTrinity: ch. 48; kbRvAddedUp: ch. 50, the wage rise comes out of s |
| kbRvAddedUp | caught | kbRvAddedUp: ch. 50, the wage rise comes out of s |
| kbRvClasses | caught | kbRvClasses: ch. 52 |
| kbRevenue | caught | kbRevenue: Smith's dogma |

## Deviations from §D (also in capkit_b.DEVIATIONS)

  * Fields D.2 does not list but a lesson in section C needs: turnover/time
    `capital` (the capital advanced, for tuAggregate); turnover/fixed
    `age_years` (tuRemaining is "after n years"); turnover/advance
    `new_outlay` (Chapter 31's change of scale: tuFreed then prints the
    capital released); prices `profit_rate` and `average` (Chapter 11 gives
    Marx's average rate and names the sphere of average composition; without
    `average` the whole of the spheres is the average capital); rent
    `industry` {c, v} (Chapter 45 compares agriculture with it); revenue
    `people` rows may give `source` (a named source of revenue) so that
    "landowners-split" can split rent finely; {name, wages, profit, rent}
    still works and the source is the kinds with a positive amount.
  * Rates are typed as fractions (1/5), as capkit_core reads them; a tile
    prints the percentage beside the fraction.
  * schemes tiles print Marx's notation bare (I(v + s) = 2,000 = IIc), as D.2's
    formats do; the banner names no unit. Every other money tile carries the
    lesson's money_unit, including ppTotals (values £422 = prices £422 ...).
  * section C says "years = 4" for schemes/expanded; D.0 names the key
    `periods`, which is what this kit reads.
  * prices/wage-rise: Marx's Chapter 11 low-composition figure. Exactly, 50c +
    62½v at 1/7 earns 225/14 = 16 1/14 and sells at 900/7 = 128 4/7 (= 128
    8/14); the Kerr text prints 16 1/12 and 128 7/12, 1/84 too much. The tile
    prints 900/7. The high-composition 116 4/7 (816/7) is exact.
  * tendency/law: Marx's Chapter 13 table raises c by 50, 100, 100, 100 at v =
    100, so c_step and capital_growth take a list (one figure per period) as
    well as one figure for every period. Each period: capital grows by
    capital_growth (c and v alike), then c_step is added to c, then c cheapens
    by c_cheapening, then s' rises by s_rate_step.
  * tendency/overaccumulation: absolute over-accumulation is modelled as D.2's
    figures read: the added capital sets no more labour in motion, so the mass
    of s is unchanged; devaluation removes a share of the swollen capital.
  * interest/usury: the whole surplus goes to the usurer each year and the
    interest it does not cover is added to the debt; years is the horizon
    (1 to 100); inYearsToRuin also prints "repaid in year n" when the surplus
    clears the debt.
  * interest/compound: years 0 to 5000; the tile prints the exact sum when it
    is at most 40 characters, else the closed form and the number of digits
    before the point.
  * rent/dr1 and dr2: the regulating investment is the least productive in use
    (`regulating: "auto"`), or a named one ("B" or "B1" for B's first dose,
    "B2" for its second). With `market_limit` the most productive investments
    are taken first until the market is supplied and the last taken
    regulates, which is how a price falls (A drops out) or rises. dr2 adds
    `former_price` (the regulating price before the change; empty: what the
    least productive first doses would set), because "rising" and "falling"
    are claims about a change and a new worse soil cannot be detected from
    the new instance alone. price_case "worst-soil" is Chapter 44's case: an
    additional dose regulates and the worst soil's first dose pays rent.
  * rent/waterfall prints rtSurplusProfit with Marx's mixed numbers (11½), the
    one tile in these modes that does, because D.2's format says so.
  * schemes/hoard: of Department I's accumulated surplus product, the
    `hoarders_share` is sold and hoarded with no purchase; the rest is bought
    with money hoarded before. scHoardGap = hoarders' sales − investors'
    purchases.


  * The tile formats in §D that print bare money figures (`values 422 = prices 422`) carry the lesson's money unit here (`values £422 = prices £422`). The exception is the schemes tiles, which keep Marx's bare notation.
  * Shilling sums print through capkit_core's capMoney (`3,257s 9 602934603/1280000000 d`). The fractional penny is not digit-grouped; that is requested of core, and is optional.
