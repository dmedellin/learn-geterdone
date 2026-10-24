# capkit, first half (Volume I modes): report

## Files changed (nothing committed)

- `scripts/mathpath/labs/capkit_core.py` (new). The shared JS (`CAP_CORE_JS`: capMoney, capPct, capQty, capHours, capSigned, capNumText, capRead, capTable, capRefuse) and the generic wiring (`CAP_WIRE_JS`). The Python helpers are q, field_text, presets, units, pick_view, choice, periods, the *_html helpers and mode_lab. The names are stable.
- `scripts/mathpath/labs/capkit.py` (new). Nine modes and the entry point `capkit_lab(cfg)`. That function dispatches `turnover, schemes, profit, prices, tendency, interest, rent, revenue` to `capkit_b.capkit_b_lab` through a lazy import, and raises on an unknown mode or view.
- `scripts/mathpath/labs/__init__.py`: `capkit` is in the import list and `"capkit": capkit.capkit_lab` is in REGISTRY. It is not in KITS_WITH_EXPECTATIONS.
- `scripts/mathcheck.js`: the block `// ---- capkit (Volume I modes) ----` … `// ---- end capkit (Volume I modes) ----` sits just before THE VERDICT. It has its own vm context: RATIONAL_JS + CAP_CORE_JS + the nine mode blocks.

**Note on capkit_b.** The other engineer did not import capkit_core; they wrote their own KB_COMMON_JS. I aligned my formatter with theirs on the two places the two halves disagreed:
- A fraction of a penny other than ½, ¼ or ¾ prints as `1/3 d` or `3 3/5 d`.
- The whole part of a percentage is grouped: `10 = 1,000%`.

As far as I compared, both halves now print money and rates identically.

## Conventions as implemented

- **Input syntax.** Inputs are text boxes with id `<prefix>In<CamelField>`, for example `suInS` or `ciInEveryDays`. Records are written `a, 1, 2; b, 3, 4`, and yes/no fields take `yes` or `no`.
- **Shipped controls.** The preset menu is `<prefix>Preset`; the status banner is `<prefix>Status` and the table `<prefix>Table`. The workday bar is `wdBar`. Iterating views get a `<prefix>Periods` range (1 to 10) shipped from `cfg["periods"]`, default 5. A preset of an iterating view may carry its own `periods` (1 to 10): choosing it sets the range, choosing a preset without one sets the range back to the lesson's `cfg["periods"]`, and the range starts at the chosen preset's figure. The redraw-only selects are `foStage` (cfg `stage`), `wdHold` (cfg `hold`) and `maTest` (cfg `test`).
- **cfg keys.** Every mode takes `view`, `presets` and `preset`, plus `money_unit`, `qty_unit`, `title`, `panel_title` and `panel_intro`. The default money unit is £ for money, circuit, machine and accumulate, `s` for surplus and wages, and `hours` (the only one allowed) for value, form and workday.
- **Build-time refusals.** Each of these raises an error naming the preset:
  - a preset key that is not an input of its view, which catches typos;
  - a preset that sets a redraw-only key;
  - `periods` set on a view that does not iterate, or outside 1 to 10;
  - `stage`, `hold` or `test` set on a view without that control;
  - a size limit exceeded;
  - an unbalanced `marx` equation (form);
  - a `default` bill number out of range (money).
- **Hostile input.** Every text box survives `''`, `banana`, `0`, `-1`, `1/0` and `A>B`. The page paints a red banner with a sentence and blanks the tiles to `—`.

## Modes, views, cfg fields, tiles (exact format, with an example read off a built page)

Prefixes: va fo mo ci su wd ma wa ac. Money formats: `9/5 h`, `£12,000`, `−£10`, `30s`, `3d`, `1s 6d`, `1½d`, `¾d`, `1/3 d`, `0s`. Rates: `1 = 100%`, `2/3 = 66.67%`. Signed: `+1 h, 0 h, −1 h`.

**value** (money_unit `hours` only; qty_unit for output)
- `snlt` (default): producers `[{name,hours,output}]` (≤8), `basis` (`per-unit`|`total`, default per-unit), `lot`. Tiles: vaSnlt `9/5 h`, vaLotValue `36 h`.
- `skill`: the same fields plus `skill` (default 1). Tiles: vaSnlt, vaPerUnit `5 h`, vaLotValue.
- `ledger`: items `[{name,hours,output}]` (≤12; hours are totals). Tiles: vaTotalHours `20 h`, vaPerUnit `goats 5 h, fish 1/2 h, furniture 6 h`.
- `market`: groups `[{units,hours}]` (≤8; hours per unit). Tiles: vaMarketValue `2 h`, vaSurplus `+1 h, 0 h, −1 h` (gain per unit = market value − own value).

**form** (hours)
- `stage`: goods `[{name,qty,unit,hours}]` (2 to 7; unit may be ""), `equivalent`, and an optional preset-only `marx: ["20 linen = 1 coat", …]` that is checked at build time to balance in hours. The redraw-only `stage` takes elementary|expanded|general|money. Tiles:
  - foEquation, `20 yards linen = 1 coat`, with equations joined by `; `;
  - foGeneral, `none` in the elementary and expanded stages, `linen` in general, `gold (as money)` in money;
  - foRelative, `2 coats` (more than one is plural: the unit when there is one, `2 quarters corn`, else the name).
- `count`: goods, equivalent. Tiles: foPairs `15`, foWithEquivalent `5`.

**money**
- `circulate`: goods `[{name,value_hours}]` (≤6), `gold_hours_per_unit`, `velocity`. Tiles: moPriceSum `£8`, moNeeded `£2`.
- `payments`: the same plus `credit_sales`, `payments_due`, `cancelling` (default 0), `bills [{from,to,amount,backed}]` (0 to 12), and `default` (a 1-based bill number, or empty). Tiles: moPriceSum, moNeeded `£5/2`, moNetted `£100`, moUnbacked `£0`.
- `world`: `imports`, `exports`, `other_receipts` (signed, default 0). Tile: moDrain is `£200 out`, `£0`, or `£0 (£200 in)`.
- `fixed-rent`: `rent`, `price_index`, `wage_index`, `product`, `wages`. Tiles: moRealRent `£10`, moFarmerGain `£120`.
- `bank-act`: goods, gold_hours_per_unit, velocity, `issue`, `reserve`, `fiduciary`, `demand`. Tiles: moNeeded, moReturned `£3`, moCap `£24`, moGap `£6`.

**circuit**
- `formula`: `start` (money|commodity), `M`, `product`. Tiles: ciForm is `C–M–C` or `M–C–M′`; ciDelta is `+£10`, `£0` or `−£10` (product − M).
- `markup`: sellers `[{name,value,markup}]` (2 to 8, in a ring). Tiles: ciTotalBefore `£90`, ciTotalAfter `£90`.
- `labour-power`: subsistence `[{item,hours,every_days}]` (≤12). Tile: ciLpValue `8 h`.
- `stages`: `M`, `mp`, `lp`, `product`, `sold_share` (default 1). The page refuses unless M = mp + lp. Tiles: ciMprime `£60`, ciS `−£40`.
- `market`: `households`, subsistence, `self_supplied_value` (default 0). Tiles: ciLpValue `8 h` (per household per day), ciMarket `800 h`.
- `costs`: M, product, `pure_costs`, `value_adding_costs`. Tiles: ciS `£20`, ciSNet `£15`.
- `realise`: M, product, `consumption_advance`. Tiles: ciReturned `£120`, ciS `£20`.

**surplus** (days are refused above 24 h)
- `mill`: `materials`, `wear`, `wage`, `hours`, `necessary_hours`, `waste` (default 0). Tiles: suProduct `30s`, suS `3s` (product − capital advanced; `−2s` with waste).
- `transfer`: `machine_value`, `machine_days`, materials, wage, hours, necessary_hours. Tiles: suTransfer `£1`, suProduct.
- `rate`: `c`, `v`, `s`, `output`. Tiles: suRate `1 = 100%`, suParts `c: 16 lb, v: 2 lb, s: 2 lb`.
- `parts`: the same fields. Tiles: suProduct `30s`, suParts.
- `senior`: hours, necessary_hours. Tiles: suRate, suLastHour `19/23 = 82.61% (Senior: 0)`.
- `mass`: wage, `workers`, hours, necessary_hours. Tiles: suMass `300s`, suRate `2 = 200%`.
- `formulae`: hours, necessary_hours. Tiles: suRate, suFalse `2/3 = 66.67%`.

**workday** (hours; every view draws an SVG bar)
- `absolute`: day, necessary. Tiles: wdSurplus `6 h`, wdRate `1 = 100%`.
- `limit`: plus `limit`. Tiles: wdSurplus, wdRate `2/3 = 66.67%`.
- `relative`: plus `productivity` and `pioneer_productivity` (default 1). Tiles: wdSurplus, wdRate, wdExtra `+12 h`.
- `intensity`: plus `intensity`. Tiles: wdLabour `12 h`, wdSurplus, wdRate.
- `classify`: day, necessary, `new_day`, `new_necessary`. Tiles: wdKind (`absolute` | `relative` | `both` | `none`), wdSurplus, wdRate `9/5 = 180%`.
- `three`: day, necessary, productivity, intensity, `new_day`. The redraw-only `hold` takes productivity|intensity|length|combined. Tiles: wdLpValue `3 h`, wdRate `3 = 300%`.
- `separate`: day, necessary, `own_land` (true/false), `count` (default 1). Tiles: wdSurplus `600 h` (× count), wdRate `0 = 0%` on one's own land.
- `corvee`: `lord_days`, `own_days`. Tiles: wdSurplus `3 days`, wdRate.

**machine**
- `cooperate`: `workers`, `output_each`, `shared_c`, `c_each_if_alone`, `hours`. Tiles: maOutput `144 pieces`, maCPerUnit `alone 10d, together 5/6 d`, maCombinedDay `144 h`.
- `detail`: steps `[{name,rate}]` (≤8). Tiles: maWorkers `founders 4, breakers 2, rubbers 1`, maMinimum `7`.
- `adopt`: `machine_value`, `machine_life_units`, `wages_displaced`, `labour_saved_value`. The redraw-only `test` takes capitalist|society. Tiles:
  - maPerUnit, `£3/10`;
  - maVerdict, either `adopted (the capitalist’s test)` or `not adopted (society’s test)`. The apostrophe is ’, and the test is strict (cost < against).
- `displace`: `variable`, `wage_each`, `discharged`, `machine_spend`, `mb_composition`. Tiles: maDisplaced `50`, maReemployed `10 = 0 set free + 10 in machine-building`.

**wages**
- `form`: `lp_value`, `normal_hours`, `value_per_hour`. Tiles: waHourPrice `3d`, waValueCreated `6s in 12 h (6d an hour)`.
- `time`: lp_value, normal_hours, `hours_worked`. Tiles: waHourPrice, waDaily `1s 6d`.
- `piece`: lp_value, normal_hours, `pieces_normal`, `pieces_actual`, `rate_cut_to` (empty means no cut). Tiles: waPieceRate `1½d` or `¾d`, waDaily `3s`.
- `national`: `countries [{name,wage,output_per_hour}]` (exactly 2), `unit_value`. Tiles: waRelative `3/4`, waRate `England 5/3 = 166.67%, Continent 1 = 100%`.
- `statute`: `statutory_wage`, lp_value, `day`, `necessary`. Tiles: waGap (`1s below the value` | `at the value` | `… above the value`), waRate `2 = 200%`.

**accumulate**
- `simple`: `capital`, `consumed_per_year`. Tile: acYears `5 years`.
- `expand` (periods): capital, `c_v`, `s_rate`, `accumulate_share`, `invest_threshold` (default 0). Tiles: acCapital `£12,000` (5 periods: `£124,416/5`), acShareOriginal `5/6 = 83.33%`, acHoard `£0`.
- `labour` (periods): plus `labour_supply`, `supply_growth` (default 0), `wage_per_worker`. Tiles: acDemand `484`, acReserve `216`, acCapital `£13,310`.
- `composition` (periods): plus `composition_rise`. Tiles: acDemand `400`, acReserve `1,600`.
- `law` (periods): plus `wage_growth`. Tiles: acRatio `39/136 = 28.68%`, acReserve, acDemand.
- `centralise` (periods): `capitals [n…]` (≤10), `merge_rule` (largest-absorbs-smallest|none), `growth` (default 0). Tiles: acTopShare `3/5 = 60%`, acCount `5`.
- `colony` (periods): capital, `colonists`, `land_price_years`, `saving_share`. Tiles: acReserve `0` / `3,000`, acYearsToLand `4 years` / `0 years` / `never`.
- `thrift`: `wage`, saving_share, `target`. Tile: acDaysToTarget `200,000 working days`.

## Verification

- **Scratch pages.** I built 53 scratch pages, one or more preset-bearing cfgs for every mode and view, with expectations computed by hand from §C (scratchpad/kit/cfgs.py, build.py, out/).
  - `labcheck.js --expect` (including the hostile sweep): 53 pages, 53 pinned, 0 failing.
  - Plain `labcheck.js`: 0 failing.
  - Breaking one pinned string made the page FAIL, so the expectation gate is live.
  - Every preset's status banner was read through scratchpad/kit/status.js.
- **mathcheck.** It passes. My block has about 105 cases, built on Marx's figures throughout:
  - spinning mill, 27s advanced → 30s and 3s;
  - c 410 / v 90 / s 90 → `1 = 100%`;
  - 20 lb of yarn → `c: 16 lb, v: 2 lb, s: 2 lb`;
  - Senior → `19/23 = 82.61%`;
  - 100 yards in 180 h → `9/5 h`;
  - type-founding → 4:2:1;
  - piece-wages → `1½d` and `¾d`;
  - £10,000 → `£12,000`;
  - ten capitals → `3/5`;
  - £8 at velocity 4 → `£2`;
  - the pence and percentage formatters and capRead refusals.
- **Mutation testing.** scratchpad/kit/mutate.py made 69 mutations covering every pure function. Every one makes mathcheck fail, and every restore was hash-checked. Logs are in scratchpad/kit/mutation-log*.txt and tasks/bo2w2eckt.output.
  - Five mutations survived the first pass: pos refusing 0, moPricesOf at gold = 1, realise at product = money thrown in, wdKindOf's single branches, and centralise growth with equal shares. I added a case for each, and each was then seen to fail.
- **Incident.** The first background mutation run was killed at its time limit while the `waCompute statute` mutation was applied, so the restore never ran. I found it by scanning and restored the exact line. A final scan shows no mutation left in either file.
- **Tests.** `python3 -m unittest discover -s tests -p test_site_invariants.py` runs 101 tests, all OK, including TestEveryLabBuilds.

## Deviations from §D, each chosen to keep the arithmetic honest

1. **Form limit.** Form allows 7 commodities, against D.0's 6. Marx's own figure in §C lesson 3 has seven (linen, coat, tea, coffee, corn, gold, iron).
2. **`marx` field.** In form, the build-time check is read as an optional preset-only field `marx: ["<qty> <good> = <qty> <good>", …]`, checked to balance in hours. Printed equations are computed from hours, so they always balance.
3. **Money form.** The money stage prints the same equations as the general form; Marx says the only difference is gold in the equivalent's place. foGeneral appends ` (as money)`.
4. **Money unit.** Value, form and workday accept only `money_unit: "hours"`, because their inputs are labour-time. Any other unit is refused rather than mislabelled.
5. **`basis`.** It is a text input holding `per-unit` or `total`, since a preset may not rewrite a select. Ledger hours are totals.
6. **vaSurplus.** It is the gain per unit (market value − own value), not per group.
7. **The drain.** world's moDrain uses imports − exports − other_receipts as specified. A payment owed abroad is entered as negative other_receipts, which is what the `drain` preset in §C needs.
8. **New circuit field.** circuit/formula adds a field `start` (money|commodity), because nothing in §D's fields says which end a circuit starts from.
9. **circuit/market.** ciLpValue keeps its §D meaning, per household per day; ciMarket = households × (lp − self_supplied). The two are equal only for one household, so §C lesson 5.5's "one number from two sides" holds as market = households × wage, not as equal tiles.
10. **circuit/costs.** Value-adding costs enter outlay and product equally, so they leave s unchanged; pure costs come out of s. circuit/realise returns min(product, M + consumption_advance).
11. **surplus/mill.** suS = product − capital advanced. It equals new value − wage when there is no waste and shows waste as a loss.
12. **New workday fields.** classify and three need a before and an after, so I added `new_day` and `new_necessary`. three's `hold` gained a fourth option, `combined`, for §C lesson 3.8's `combined` preset. wdExtra = day × (pioneer_productivity − 1), at social value.
13. **machine/displace.** maReemployed counts machine-building jobs at the same wage and at `mb_composition`. The spec's `capital` and `capital`-style extras are not used.
14. **New wages field.** wages/national adds `unit_value`, the value of a unit on the world market, because without it the rate of surplus value cannot be computed from wage and output.
15. **New accumulate fields.**
    - `wage_growth`, for law's `boom` preset.
    - `growth`, for centralise's `grow` preset.
16. **accumulate engine rules.** Each period lays out the whole capital at that period's c/v. Value per worker is (1 + s′) × the first period's wage. When demand exceeds supply, the wage rises to v / supply and s falls. supply_growth is additive.
17. **Colony.** `land_price_years` is the price in years of the full wage, and years to land = land_price_years / saving_share. acReserve is the workers still for hire in the last period. `wage` is not used by colony.
18. **Pixel geometry.** The workday bar uses BigInt integer division, so no float is printed or computed.

Element ids such as vaPreset or acRatio also exist in other kits, but only on other pages; no module-level JS name collides. This is recorded in capkit.py's docstring.
