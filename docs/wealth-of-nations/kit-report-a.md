# wonkit, family A (Book I modes): report

The Wealth of Nations, Read Along. Spec: `docs/wealth-of-nations/PLAN.md` §0, §D.0, §D.1. Authors configure lessons from this report, never from the code.

## Files changed (nothing committed)

- `scripts/mathpath/labs/wonkit.py` (new). Seven modes, eighteen views, and the entry point `wonkit_lab(cfg)`. It dispatches `division, money, price, wages, advantage, rent, interest` from its own `SPECS`, and any other mode through `wonkit_b.MODES[mode](cfg)`, imported lazily on first use with `importlib.import_module(".wonkit_b", __package__)`. If `wonkit_b.py` is missing, family B's modes are simply absent; any other import error is raised. An unknown mode raises `wonkit_lab: unknown mode 'x'; the modes are division, …, system`, naming family B's modes when they load.
- `scripts/mathpath/labs/__init__.py`: `wonkit` is in the import list and `"wonkit": wonkit.wonkit_lab` is in REGISTRY.
- `scripts/build_paths.py`: `"wonkit"` is in `KITS_WITH_EXPECTATIONS`, so every wonkit page's preset `expect` strings are gated by `labcheck.js`, and a wonkit page with none fails.
- `scripts/mathcheck.js`: the block `// ---- wonkit (Wealth of Nations), family A ----` … `// ---- end wonkit family A ----` sits immediately after `// ---- end acckit family B ----`. Family B's block follows it. Family B had first inserted theirs at the same marker, ahead of mine; I moved my block, untouched, back to its place, and B's text is byte for byte as they wrote it.
- `docs/wealth-of-nations/kit-report-a.md`: this file.

`wonkit_core.py` was not touched.

**No £sd cell kind.** PLAN D.0 makes it optional, and I did not add one. A new cell kind would have to be read by `aktRead`, which lives in acckit and in the seam. Every money amount is typed in the one unit the lesson names: `money_unit: "d"` for pence, `"s"` for shillings, `"£"` for pounds, `"oz silver"`, and so on. Fractions are allowed (`1/2`, `7/3`), so ½d and similar amounts can be typed exactly. Family B has nothing of mine to import for money. `WNA_JS` (below) is exported in case B wants the same printers, but B has its own `WNB_SHARED_JS`.

## Conventions (every family A view)

- **Building.** Every view is built through `wonkit_core.mode_lab(cfg, mode, SPEC)`. A page ships, in order:
  - RATIONAL_JS, EA_CORE_JS, AKT_CORE_JS and WNK_CORE_JS;
  - `WNA_JS` with `%P%` replaced by the mode's prefix;
  - the mode's base block and its own view's block, and nothing from another view or mode. I checked: the pins page holds no `WDV_VIEW.supply` or `WDV_VIEW.exchange`.

  A built page is about 30 KB.
- **cfg keys.** Every view takes the common keys `mode`, `view`, `presets`, `preset`, `title`, `panel_title` and `panel_intro`, plus the lesson-level unit keys listed under the view. A field's key may also be set at lesson level, where it becomes the default for every preset that omits it. Any other key is refused: `wonkit/<mode>/<view>: cfg sets X, which this view does not take (it takes …)`.
- **Unit keys** (`money_unit`, `qty_unit`, `measure_unit`, `period`) are lesson-level only, because a preset may not set them. Each must match `^[A-Za-z£$€](?:[A-Za-z£$€ .-]{0,22}[A-Za-z.])?$`, with no double space. That allows 1–24 characters: letters, spaces, dots, hyphens and £ $ €. Anything else is refused: `wonkit/<mode>/<view>: cfg['money_unit'] should be a short plain word or symbol (letters, spaces, dots, hyphens, £ $ €; at most 24 characters), not '<b>'`. Setting `money_unit` on a view that prints no money (pins, exchange, barter, coin, growth, wit profit) is refused as a stray key.
- **Presets.** `cfg["presets"]` is a non-empty list of `{id, label, <field>: value, …, expect: {tile_id: "exact text"}}`.
  - `id` is `[a-z0-9][a-z0-9-]*` and unique.
  - `label` is plain text without `<>&`.
  - A field missing from a preset takes the lesson-level cfg value, then the field's default. A required field (default "required" below) missing from both is refused: `… preset 'id': needs <field>`.
  - A value may be written as the exact box text (`"savage, 1000, 900, 10; civilized, 1000, 500, 40"`), or for records as a list of lists or strings.
  - `cfg["preset"]` picks the preset shown first (default: the first).
  - `expect` maps this view's tile ids to the exact string the page prints. `labcheck.js` selects each preset on the built page and compares, and a wrong string fails CI. I checked this with a scratch manifest: `240×` passed, and `241×` failed with `#wdvMultiple should read "241×", the page printed "240×"`.
  - Read the strings off a built page with `node scripts/labcheck.js --observe <page.html>`. Never copy them from this report without checking.
- **Input ids** are `<prefix>In<Key>` (`wdvInWorkers`, `wprInWage_rise`). The preset select is `<prefix>Preset`, the status line `<prefix>Status` and the table `<prefix>Table`.
- **Records** are written `a, 1, 2; b, 3, 4`. Lists are separated by spaces or commas. A name is letters, digits, dots, hyphens or underscores (`edward-i`, `north-america`, `1700`). A "rational" cell is a decimal of at most 6 places, or a fraction `p/q` of whole numbers (at most 8 digits each, q not 0). A `-` cell means none where the table says so.
- **Hostile input.** Every text box survives `''`, `banana`, `0`, `-1`, `1/0` and `A>B`. The page paints one red sentence and blanks every tile to `—`. My scratch harness ran all six values into every input of every view, 18 views and 54 inputs: no throw, no blank-less red, and no `NaN`, `undefined`, `Infinity` or `null` in a tile. `labcheck.js` with its own sweep also passed on all 20 scratch pages. Where 0 is allowed (alone, wage, brought, yield, succeed, cost …), the view prints a sentence rather than divide by it. Those cases are listed under each view.
- **Status line.** Each status line is one sentence of the result, then `; it follows from the figures stated, not from any economy’s records.` through `wnkStatus`. mathcheck checks that the ending is there.

### Printers (`WNA_JS`, one copy per mode, names prefixed: `wdvMoney`, `wprRate` …)

| printer | prints | examples |
|---|---|---|
| `Money(r, unit, signed)` | a whole amount as is, grouped. An amount exact at 2 places prints with 2 places. Any other amount is rounded half away from zero to 2 places, with `≈ ` in front. `£ $ €` go before the figure, `s` and `d` after it with no space, any other unit after a space. The sign goes before the unit, and `signed` adds `+` to a gain | `£1.50`, `−£10`, `≈ £1.33`, `30s`, `3.50d`, `5 oz silver`, `≈ +0.33d`, `≈ −£0.33` |
| `Rate(p)` | a percentage typed or derived as a number of percent | `5%`, `2.5%`, `10/3 ≈ 3.33%` |
| `Ch(r)` | a signed change or share, from eaPct (exact fraction, then the percent: whole, or one place with `≈`) | `+1/5 = +20%`, `−2/5 = −40%`, `0 = 0%`, `+1/3 ≈ +33.3%` |
| `Unit(r, word)` | eaNum and a unit, with the final `s` dropped at exactly ±1 for a one-word unit | `1 pin`, `9/5 = 1.80 operations`, `1 days of labour` (multi-word units keep their form) |
| `Two(r)` | a non-money quantity: whole, or 2 places with `≈` when not exact | `106.12`, `≈ 106.12` |
| `X(r)` | a multiple: eaNum and `×` | `240×`, `20/9 ≈ 2.22×` |
| `Sg(r)` | eaNum with `+` for a positive | `+5`, `−32/5 = −6.40` |

eaNum prints a whole number grouped, or `p/q = d.dd` when exact at 2 places, or `p/q ≈ d.dd`. A figure past 30 digits prints as `≈ 1.23 × 10^45`. eaPct prints `p/q = x%`, or `≈ x.x%` at one place. Shares and rates use these. Money that compounds (fund, parts) is shown to two places with `≈` and has no fraction.

## Modes, views, cfg fields, tiles

Every example string below was read off the shipped script of a built page, run with the example preset. The presets are scratch, written for the kit (not Smith's) unless marked as Smith's.

### division (`wdv`)


#### division/supply — produce per head from the share at work and the output of each

Lesson-level cfg keys: `qty_unit` (default `units`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `nations` (`wdvInNations`) | Nations (nation, population, workers at useful labour, output per worker a year) | records `a, b; c, d`, 1–12 records, first cell unique: nation (name), population (whole 1–10,000,000), workers (whole 0–10,000,000), output (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000) | required |

Example preset (scratch, written for the kit): `{"nations": "savage, 1000, 900, 10; civilized, 1000, 500, 40"}`

| tile id | label | printed for the example |
|---|---|---|
| `wdvShare` | Share of the people at useful labour | `savage 9/10 = 90%; civilized 1/2 = 50%` |
| `wdvProduce` | Annual produce | `savage 9,000 units; civilized 20,000 units` |
| `wdvPerHead` | Produce per head | `savage 9 units; civilized 20 units` |
| `wdvBest` | Better supplied per head | `civilized, 20 units a head` |
| `wdvRatio` | Best per head over the next | `20/9 ≈ 2.22× (civilized over savage)` |

Status: `civilized is the better supplied: 20 units a head against 9 units for savage; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): A nation's annual produce is its workers times the output of each a year; produce per head divides it by the whole population, workers or not. Smith gives the rule (Introduction): supply per head depends on the skill of the labour and the proportion of people usefully employed. The share at work is workers over population, exact. Nations are listed in the order given; the better supplied is the highest produce per head (equal ones tie), and the ratio is the highest per head over the next highest (the earlier given wins a tie for second place).


#### division/pins — output per worker when the operations are divided

Lesson-level cfg keys: `qty_unit` (default `pins`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `workers` (`wdvInWorkers`) | Workers in the team | whole 1–10,000 | `10` |
| `operations` (`wdvInOperations`) | Distinct operations | whole 1–10,000 | `18` |
| `together` (`wdvInTogether`) | The team's output a day, divided | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | `48000` |
| `alone` (`wdvInAlone`) | One worker's output a day alone (0 for none) | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | `20` |

Example preset (scratch, written for the kit): `{}`

| tile id | label | printed for the example |
|---|---|---|
| `wdvPerWorker` | Output per worker, divided | `4,800 pins a day` |
| `wdvAloneTeam` | The team's output if each worked alone | `200 pins a day` |
| `wdvMultiple` | Multiple (per worker divided over alone) | `240×` |
| `wdvExtra` | Extra output of the team a day | `+47,800 pins a day` |
| `wdvOpsEach` | Operations per worker | `9/5 = 1.80 operations a worker` |

Status: `Dividing 18 operations among 10 workers, each makes 4,800 pins a day against 20 pins alone, 240× as many; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Output per worker divided is the team's output over its workers; the team alone is the workers times one worker's output alone; the multiple is per worker divided over alone, and when alone is 0 no multiple is finite (Smith: perhaps not one). The extra output is the team's divided output less its output alone. Operations per worker is the operations over the workers, exact. Smith gives the figures of I.1 (ten workers, eighteen operations, upwards of 48,000 pins a day, certainly not twenty alone); the lab takes the figures typed and says nothing of which of his three causes accounts for the multiple.


#### division/exchange — two producers' output, self-sufficient and specialised

Lesson-level cfg keys: none beyond the common ones.

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `goods` (`wdvInGoods`) | The two goods (two names) | list (spaces or commas), 2–2 entries, each name, unique | required |
| `producers` (`wdvInProducers`) | Producers (producer, hours available, hours a unit of the first good, hours a unit of the second) | records `a, b; c, d`, 2–2 records, first cell unique: producer (name), hours (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000), a (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000), b (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000) | required |

Example preset (scratch, written for the kit): `{"goods": "bows venison", "producers": "maker, 12, 1, 2; hunter, 12, 3, 1"}`

| tile id | label | printed for the example |
|---|---|---|
| `wdvSelfEach` | Self-sufficient: each makes equal quantities of both | `maker 4 of each; hunter 3 of each` |
| `wdvSelfTotal` | Self-sufficient totals | `bows 7; venison 7` |
| `wdvWho` | Specialised: who makes what | `maker makes bows (relative cost 1/2 = 0.50 against 3); hunter makes venison` |
| `wdvSpecTotal` | Specialised totals | `bows 12; venison 12` |
| `wdvGain` | Gain in each good | `bows +5; venison +5` |
| `wdvCase` | Who is better at what | `each is better at one good: maker at bows, hunter at venison (Smith’s case)` |

Status: `Specialised, maker makes bows and hunter makes venison: bows +5 and venison +5 against each making equal quantities of both; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Self-sufficient, each producer splits the hours to make equal quantities of both goods: hours over (hours a unit of the first + hours a unit of the second). Specialised, each makes only one good with all the hours: the producer whose relative cost of the first good (its hours a unit over the second's) is the lower makes the first, the other makes the second. That relative-cost rule is Ricardo's (1817), not Smith's; it agrees with Smith's case, where each producer is better (fewer hours a unit) at one good, and it still divides the work when one producer is better at both. Equal relative costs are refused: the rule then names no division. A gain is specialised less self-sufficient, signed; it may be negative in one good. Every figure is exact.


#### division/market — how many specialists a market of a given size can keep

Lesson-level cfg keys: `qty_unit` (default `units`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `places` (`wdvInPlaces`) | Places (place, demand a year) | records `a, b; c, d`, 1–12 records, first cell unique: place (name), demand (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000) | required |
| `output` (`wdvInOutput`) | One specialist's output a year | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `days` (`wdvInDays`) | Working days a year | whole 1–366 | `300` |

Example preset (scratch, written for the kit): `{"places": "village, 50; town, 300; city, 5000", "output": "200"}`

| tile id | label | printed for the example |
|---|---|---|
| `wdvKeeps` | Specialists the demand keeps | `village 0; town 1; city 25` |
| `wdvYearShare` | Share of one specialist's year | `village 1/4 = 25%; town 3/2 = 150%; city 25 = 2,500%` |
| `wdvLive` | Where a full-time trade can live | `2 of 3 places: town, city` |
| `wdvPerDay` | One specialist's output a day | `2/3 ≈ 0.67 units a day` |

Status: `One specialist makes 200 units a year; a full-time trade can live in 2 of 3 places: town, city; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): The specialists a place keeps is its demand a year over one specialist's output a year, rounded down to a whole number (the lab's rule: a part of a year's work does not keep a person at the trade). The share is the same quotient, exact, and may pass 100%. A full-time trade can live where it keeps at least one specialist; Smith's rule (I.3) is that the division of labour is limited by the extent of the market. Output a day is the output a year over the working days. Places are listed in the order given.


### money (`wmo`)


#### money/barter — exchange ratios without money and with a common measure

Lesson-level cfg keys: none beyond the common ones.

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `goods` (`wmoInGoods`) | Goods (2 to 12 names) | list (spaces or commas), 2–12 entries, each name, unique | required |
| `traders` (`wmoInTraders`) | Traders (trader, has, wants; empty for none) | records `a, b; c, d`, 0–12 records, first cell unique: trader (name), has (name), wants (name) | empty |

Example preset (scratch, written for the kit): `{"goods": "meat beer bread", "traders": "butcher, meat, beer; brewer, beer, bread; baker, bread, meat"}`

| tile id | label | printed for the example |
|---|---|---|
| `wmoWithout` | Ratios to quote without money | `3 ratios` |
| `wmoWith` | Prices to quote in a common measure | `2 prices` |
| `wmoFewer` | Quotations saved | `1 quotation fewer` |
| `wmoDirect` | Pairs who can trade directly | `0: none` |
| `wmoViaMoney` | Traders who can trade only through a money | `3: butcher, brewer, baker` |
| `wmoNoBuyer` | Traders whose good no other trader wants | `0: none` |

Status: `3 goods need 3 exchange ratios without money and 2 prices in a common measure; 0 pairs of traders can trade directly; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Without money every pair of n goods needs its own ratio, n(n − 1)/2; with a common measure each good needs one price, n − 1 (the measure itself needs none). Two traders can trade directly when each has what the other wants (Smith's want of a double coincidence, I.4). A trader can trade only through a money when another trader wants their good but no direct pair includes them; a trader whose good no other trader wants has no buyer among those listed. The trader lists are the lab's reading of Smith's butcher, brewer and baker. Traders are listed in the order given.


#### money/coin — the silver in a penny as the pound is debased

Lesson-level cfg keys: none beyond the common ones.

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `periods` (`wmoInPeriods`) | Periods (period, pence coined from a pound weight of silver) | records `a, b; c, d`, 1–12 records, first cell unique: period (name), coined (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000) | required |
| `sum` (`wmoInSum`) | A fixed sum in pence (- for none) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000, or `-` | `-` |

Example preset (scratch, written for the kit): `{"periods": "edward-i, 240; elizabeth, 744", "sum": "240"}`

| tile id | label | printed for the example |
|---|---|---|
| `wmoSilver` | Silver in a penny, against the first period | `edward-i 1 = 100%; elizabeth 10/31 ≈ 32.3%` |
| `wmoPound` | The first period's pound (240 of its pence) in each period's pence | `edward-i 240d (£1); elizabeth 744d (£3 2s)` |
| `wmoSumSilver` | Silver in the fixed sum | `edward-i 1 lb silver; elizabeth 10/31 ≈ 0.32 lb silver` |
| `wmoLoss` | Silver a creditor loses when paid the same sum, against the first period | `elizabeth 21/31 ≈ 67.7% of the silver` |
| `wmoLossSum` | The creditor's loss in the first period's pence | `elizabeth 5,040/31 ≈ 162.58d lost, in edward-i’s pence` |

Status: `From edward-i to elizabeth a penny comes to hold 10/31 ≈ 32.3% of its silver, and edward-i’s pound is 744d (£3 2s) in elizabeth’s pence; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): A penny holds 1/coined of a pound weight of silver, so against the first period it holds (first coined)/(this coined). The first period's pound is 240 of its pence; its silver, in a later period's pence, is 240 × (this coined)/(first coined), shown also in pounds, shillings and pence when whole. A fixed sum holds sum/coined pounds weight of silver. A creditor owed the sum in the first period's coin and paid the same sum later loses 1 − (first coined)/(later coined) of the silver (a gain when fewer pence are coined later); the loss in the first period's pence is the sum times that share. Smith gives the rule (I.4, I.5) and figures such as 240 and 744 pence from the pound weight. Periods are compared with the first given.


### price (`wpr`)


#### price/real — a price in money against a price in labour or in corn

Lesson-level cfg keys: `measure_unit` (default `days of labour`), `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `years` (`wprInYears`) | Years (year, money price of the good, money price of the measure) | records `a, b; c, d`, 2–12 records, first cell unique: year (name), price (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000), measure (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000) | required |

Example preset (scratch, written for the kit): `{"years": "1700, 10, 1/2; 1750, 12, 1"}`

| tile id | label | printed for the example |
|---|---|---|
| `wprReal` | Real price each year, in the measure | `1700 20 days of labour; 1750 12 days of labour` |
| `wprMoneyCh` | Change in the money price | `1700 → 1750: +1/5 = +20%` |
| `wprRealCh` | Change in the real price | `1700 → 1750: −2/5 = −40%` |
| `wprWay` | Did they move the same way? | `not the same way: the money price rose and the real price fell` |

Status: `From 1700 to 1750 the money price rose (+1/5 = +20%) and the real price, in days of labour, fell (−2/5 = −40%); it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): The real price in a year is the money price of the good over the money price of the measure (a day's labour, or a quarter of corn): how much of the measure the good commands. Smith gives the rule (I.5): labour is the real measure, money the nominal one. A change is last less first over first, exact, signed; first and last are the first and last years given, in the order given. Each moved the same way when both rose, both fell or both held.


#### price/parts — a price resolved into wages, profit and rent through the stages of production

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `stages` (`wprInStages`) | Stages (stage, wages paid, rent paid, profit rate % on everything advanced) | records `a, b; c, d`, 1–12 records, first cell unique: stage (name), wages (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000), rent (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000), rate (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1,000) | required |
| `wage_rise` (`wprInWage_rise`) | A rise of wages, % (0 for none) | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1,000 | `0` |
| `profit_rise` (`wprInProfit_rise`) | A rise of profit, points added to every rate (0 for none) | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1,000 | `0` |

Example preset (scratch, written for the kit): `{"stages": "grower, 10, 4, 10; miller, 3, 0, 10; baker, 5, 0, 10"}`

| tile id | label | printed for the example |
|---|---|---|
| `wprStages` | Price after each stage | `grower £15.40; miller £20.24; baker ≈ £27.76` |
| `wprFinal` | Final price | `≈ £27.76` |
| `wprResolved` | Resolved into wages, rent and profit | `wages £18, rent £4, profit ≈ £5.76` |
| `wprShares` | Shares of the final price | `wages 4,500/6,941 ≈ 64.8%; rent 1,000/6,941 ≈ 14.4%; profit 131/631 ≈ 20.8%` |
| `wprWageRise` | With the wage rise | `no wage rise given` |
| `wprProfitRise` | With the profit rise | `no profit rise given` |
| `wprBothRise` | With both rises | `give both rises to combine them` |

Status: `The final price is ≈ £27.76: wages 4,500/6,941 ≈ 64.8%, rent 1,000/6,941 ≈ 14.4%, profit 131/631 ≈ 20.8%; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): At each stage the undertaker advances the price of what the last stage sold, the wages and the rent, and takes the profit rate on all of it: price after = (previous price + wages + rent) × (1 + rate/100), starting from nothing. The final price is then exactly the sum of all the wages, rents and profits paid at every stage (Smith, I.6: every price resolves into the three). A wage rise multiplies every stage's wages by (1 + rise/100); a profit rise adds its points to every stage's rate. Each is worked through all the stages again. A wage rise adds the extra wages and the profit charged on them; a profit rise is charged on prices that already carry profit, so it compounds: compare the price's rise with the profit on the old advances (Smith, I.9: like compound interest against simple). Stages run in the order given.


#### price/market — the market price against the natural price

Lesson-level cfg keys: `money_unit` (default `£`), `qty_unit` (default `units`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `natural` (`wprInNatural`) | Natural price a unit | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `effectual` (`wprInEffectual`) | Effectual demand (units at the natural price) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `brought` (`wprInBrought`) | Units brought to market | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |
| `buyers` (`wprInBuyers`) | Buyers' schedule (price, quantity buyers take at it; empty for none) | records `a, b; c, d`, 0–12 records: price (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000), quantity (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000) | empty |

Example preset (scratch, written for the kit): `{"natural": "10", "effectual": "100", "brought": "80", "buyers": "8, 120; 10, 100; 12, 85; 14, 70"}`

| tile id | label | printed for the example |
|---|---|---|
| `wprPosition` | Market price against the natural price | `above the natural price: less is brought (80) than the effectual demand (100)` |
| `wprGap` | Shortfall or excess | `shortfall of 20 units` |
| `wprMarketPrice` | Market price from the schedule | `£12 a unit` |
| `wprUnitGap` | Its gap to the natural price | `+£2 a unit above the natural price` |
| `wprAllGap` | The gap over the quantity brought | `+£160 over the 80 units brought` |

Status: `With 80 units brought against an effectual demand of 100, the price is above the natural price; the schedule clears at £12 against a natural price of £10; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Smith's rule (I.7): when less is brought to market than the effectual demand the market price rises above the natural price, when more it sinks below, and when the two are equal it is the natural price; the lab says which, from brought against effectual. The schedule is the lesson's, never Smith's: buyers' quantities must not increase as the price rises (a price listed twice is refused). The market price is the highest listed price at which buyers take at least the quantity brought (the lab's rule, not Smith's); when none does, there is no market price on the schedule. Its gap is the market price less the natural price, a unit and over the quantity brought.


### wages (`wwg`)


#### wages/subsistence — a family's subsistence against a wage

Lesson-level cfg keys: `money_unit` (default `£`), `period` (default `week`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `items` (`wwgInItems`) | A family's needs (item, cost each period) | records `a, b; c, d`, 1–12 records, first cell unique: item (name), cost (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000) | required |
| `wage` (`wwgInWage`) | The wage each period | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |
| `maintenance` (`wwgInMaintenance`) | The worker's own maintenance each period (- for none) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000, or `-` | `-` |
| `multiple` (`wwgInMultiple`) | Multiple of the worker's own maintenance | rational (decimal ≤ 6 places or p/q) > 0, ≤ 100 | `2` |

Example preset (scratch, written for the kit): `{"items": "bread, 3; rent, 1.5; fuel, 1; clothes, 1", "wage": "6", "maintenance": "2.5"}`

| tile id | label | printed for the example |
|---|---|---|
| `wwgFamily` | Family subsistence | `£6.50 a week` |
| `wwgCover` | The wage against it | `falls short by £0.50` |
| `wwgMinimum` | Maintenance × multiple | `£5 a week (2 × £2.50)` |
| `wwgCoverMin` | The wage against that minimum | `covers it, with £1 over` |

Status: `A wage of £6 a week against a family’s needs of £6.50: it falls short by £0.50; against 2 × the worker’s own maintenance, it covers it, with £1 over; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): The family's subsistence is the sum of its needs each period. The wage covers it when it is at least the sum; the lab says by how much it is over or short. With the worker's own maintenance, the minimum is that maintenance times the multiple: Smith (I.8) reports Cantillon's double the labourer's own maintenance, so that two working parents can bring up two children; the multiple is the lesson's to state. The needs and the wage are the lesson's figures.


#### wages/fund — the wage when the fund and the workers grow at stated rates

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `fund` (`wwgInFund`) | Funds destined for maintaining labour, a year | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `workers` (`wwgInWorkers`) | Workers | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `fund_growth` (`wwgInFund_growth`) | Growth of the fund, % a year (may be negative) | rational (decimal ≤ 6 places or p/q) > -100, ≤ 1,000 | `0` |
| `worker_growth` (`wwgInWorker_growth`) | Growth of the workers, % a year (may be negative) | rational (decimal ≤ 6 places or p/q) > -100, ≤ 1,000 | `0` |
| `years` (`wwgInYears`) | Years | whole 0–50 | `10` |

Example preset (scratch, written for the kit): `{"fund": "1000", "workers": "100", "fund_growth": "3", "worker_growth": "2", "years": "3"}`

| tile id | label | printed for the example |
|---|---|---|
| `wwgWageFirst` | Wage in the first year | `£10 a worker` |
| `wwgWageLast` | Wage in the last year | `≈ £10.30 a worker (year 3)` |
| `wwgTrend` | Does the wage rise, hold or fall? | `the wage rises every year: the fund grows faster than the workers` |
| `wwgFactor` | The wage's factor each year | `103/102 ≈ 1.01 a year` |
| `wwgFundLast` | The fund in the last year | `≈ £1,092.73` |
| `wwgWorkersLast` | Workers in the last year | `≈ 106.12` |

Status: `Over 3 years the wage goes from £10 to ≈ £10.30 a worker: it rises every year; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Each year the fund is multiplied by (1 + its growth/100) and the workers by (1 + theirs/100), exactly, by repeated multiplication; the wage is the fund over the workers. The workers are not rounded: they stand for a rate of population, not a head count. The wage's factor each year is (1 + fund growth/100)/(1 + worker growth/100), so the wage rises when the fund grows faster than the workers, whatever the fund's size: Smith's rule (I.8) that wages follow the increase of the funds, not their greatness. Year 0 is the first year. Money and workers not exact at two places are shown to two with ≈.


#### wages/growth — population doubling in a stated number of years

Lesson-level cfg keys: none beyond the common ones.

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `population` (`wwgInPopulation`) | Population | whole 1–10,000,000 | required |
| `doubling` (`wwgInDoubling`) | Doubling time, years | whole 1–200 | `25` |
| `years` (`wwgInYears`) | Years (a whole number of doublings) | whole 0–200 | `100` |
| `doubling2` (`wwgInDoubling2`) | A second doubling time to compare, years (0 for none) | whole 0–200 | `0` |

Example preset (scratch, written for the kit): `{"population": "1000000", "doubling2": "20"}`

| tile id | label | printed for the example |
|---|---|---|
| `wwgDoublings` | Doublings | `4` |
| `wwgAfter` | Population after | `16,000,000` |
| `wwgTimes` | The factor | `16×` |
| `wwgCompare` | The two doubling times compared | `in 100 years: every 25 years 16×, every 20 years 32× (32,000,000); the second ends 2× the first` |

Status: `Doubling every 25 years, a population of 1,000,000 doubles 4 times in 100 years and ends at 16,000,000; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Doublings are the years over the doubling time; the population after is the population times 2 to that power, exactly. The years must be a whole number of doublings (of both doubling times when two are given): a part of a doubling needs a root, which the lab does not take, and it refuses with that reason. Smith (I.8) reports doubling in twenty or five-and-twenty years in the North American colonies; the population is the lesson's. With a second doubling time the two factors and the ratio of the second to the first are shown.


### advantage (`wad`)


#### advantage/net — the whole advantages and disadvantages of employments

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `employments` (`wadInEmployments`) | Employments (employment, wage a day, days a year, cost of learning, working years to replace it, other advantages a year, signed) | records `a, b; c, d`, 1–12 records, first cell unique: employment (name), wage (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000), days (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 366), learning (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000), years (rational (decimal ≤ 6 places or p/q) > 0, ≤ 100), other (rational (decimal ≤ 6 places or p/q) ≥ -10000000, ≤ 10,000,000) | required |
| `profit` (`wadInProfit`) | Ordinary profit the cost of learning must also earn, % a year | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 100 | `0` |
| `limit` (`wadInLimit`) | Limits on entry (employment, entrants allowed, pay rise %; empty for none) | records `a, b; c, d`, 0–12 records, first cell unique: employment (name), entrants (whole 0–10,000,000), pay_rise (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1,000) | empty |

Example preset (scratch, written for the kit): `{"employments": "smith, 1.5, 300, 60, 20, 0; labourer, 1, 300, 0, 20, 0; collier, 1.5, 280, 0, 20, -40", "profit": "10", "limit": "smith, 3, 20"}`

| tile id | label | printed for the example |
|---|---|---|
| `wadAnnual` | Money wage a year | `smith £450; labourer £300; collier £420` |
| `wadLearnYear` | Cost of learning replaced a year | `smith £9; labourer £0; collier £0` |
| `wadNet` | Net advantage a year | `smith £441; labourer £300; collier £380` |
| `wadRank` | Ranking, highest first | `smith > collier > labourer` |
| `wadSpread` | Spread, highest less lowest | `£141 (smith over labourer)` |
| `wadLimited` | With the limits on entry | `smith (entry capped at 3): wage £1.50 → £1.80 a day, net £441 → £531` |
| `wadRankAfter` | Ranking with the limits | `smith > collier > labourer` |

Status: `Net advantage a year: smith £441; labourer £300; collier £380; the spread is £141 (smith over labourer); it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): The money wage a year is the wage a day times the days worked. The cost of learning is replaced over the working years with the ordinary profit on it each year: learning/years + learning × profit/100 (the lab's simple rule; Smith, I.10, asks that it be replaced 'with at least the ordinary profits'). Other advantages are the lesson's money value a year for agreeableness, constancy, trust or risk, signed (a disadvantage is negative): Smith names the circumstances, the lab does not price them. Net advantage = money wage − learning replaced + other. Ranking is by net advantage, highest first; = marks a tie, which keeps the order given. A limit on entry is the lesson's: the capped employment's wage rises by its pay rise % and its net is worked again; the entrants allowed are shown, not used, since the lab does not derive the pay rise from them.


#### advantage/lottery — a profession as a lottery, its prizes against its tickets

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `entrants` (`wadInEntrants`) | Entrants to the profession | whole 1–10,000,000 | `20` |
| `succeed` (`wadInSucceed`) | How many succeed | whole 0–10,000,000 | `1` |
| `prize` (`wadInPrize`) | Income a year of one who succeeds | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |
| `years` (`wadInYears`) | Working years | rational (decimal ≤ 6 places or p/q) > 0, ≤ 100 | required |
| `cost` (`wadInCost`) | Each entrant's cost of education | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |

Example preset (scratch, written for the kit): `{"prize": "300", "years": "30", "cost": "1000"}`

| tile id | label | printed for the example |
|---|---|---|
| `wadChance` | Chance of success | `1/20 = 5%` |
| `wadPrizes` | Total prizes | `£9,000` |
| `wadTickets` | Total cost of the tickets | `£20,000` |
| `wadExpected` | Expected prize per entrant | `£450 an entrant (against £1,000 a ticket)` |
| `wadFair` | Prizes against the tickets | `short by £11,000: the prizes repay 9/20 = 45% of the tickets` |
| `wadNeeded` | Prize a year that would repay the tickets | `≈ £666.67 a year (against £300)` |

Status: `1 in 20 succeed: the prizes come to £9,000 against £20,000 of tickets, short by £11,000; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): The chance is the successful over the entrants. Total prizes = successful × income a year × working years; total cost = entrants × cost of education; the expected prize is the total prizes over the entrants. The prizes are fair when they equal the cost, short or over otherwise. The prize that would repay the tickets is the total cost over (successful × working years). The lab adds no interest and no discounting, and counts no income for those who fail (its rules, not Smith's). Smith (I.10) says perhaps one in twenty succeeds in the law; the other figures are the lesson's.


#### advantage/profit — the apothecary's profit split into wages and profit

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `sales` (`wadInSales`) | Sales a year | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |
| `cost` (`wadInCost`) | Cost of the goods sold (stock laid out) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `wages` (`wadInWages`) | What the trader's own labour would earn as wages a year | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |
| `stock` (`wadInStock`) | Capital employed if not the cost (- for the cost) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000, or `-` | `-` |

Example preset (scratch, written for the kit): `{"sales": "330", "cost": "30", "wages": "250"}`

| tile id | label | printed for the example |
|---|---|---|
| `wadApparent` | Apparent profit | `+£300` |
| `wadApparentRate` | Its rate on the stock | `+10 = +1,000% on £30` |
| `wadTrue` | True profit, after the wages of the trader's labour | `+£50` |
| `wadTrueRate` | Its rate | `+5/3 ≈ +166.7% on £30` |
| `wadWageShare` | Share of the apparent profit that is wages | `5/6 ≈ 83.3%` |

Status: `The apparent profit is +£300, +10 = +1,000% on the stock; less the wages of the trader’s labour, +£50, +5/3 ≈ +166.7%; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Apparent profit = sales − cost, and its rate is over the stock (the cost unless another capital is given). True profit takes off the wages the trader's own labour would earn; its rate is over the same stock. The share that is wages is the wages over the apparent profit (it passes 100% when the true profit is negative). Smith (I.10) reads the apothecary's 'thousand per cent' as mostly the reasonable wages of his labour; the wages figure is the lesson's.


### rent (`wre`)


#### rent/residual — rent as what is left after wages and ordinary profit

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `lands` (`wreInLands`) | Lands (land, units produced a year, wages paid, other stock advanced) | records `a, b; c, d`, 1–12 records, first cell unique: land (name), output (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000), wages (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000), stock (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000) | required |
| `price` (`wreInPrice`) | Price of a unit of the produce | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `rate` (`wreInRate`) | Ordinary profit, % on wages and stock | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1,000 | `10` |
| `price2` (`wreInPrice2`) | A second price to compare (- for none) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000, or `-` | `-` |

Example preset (scratch, written for the kit): `{"lands": "rich, 100, 200, 100; middling, 80, 200, 100; poor, 60, 200, 100", "price": "5", "price2": "6"}`

| tile id | label | printed for the example |
|---|---|---|
| `wreValue` | Value of the produce | `rich £500; middling £400; poor £300` |
| `wreCosts` | Wages and stock with ordinary profit | `rich £330; middling £330; poor £330` |
| `wreRent` | Rent left | `rich £170; middling £70; poor no rent (a loss of £30)` |
| `wreTotal` | Total rent | `£240` |
| `wreNoRent` | Lands yielding no rent | `1: poor` |
| `wreLowest` | Lowest price that affords rent | `rich £3.30 a unit; middling ≈ £4.13 a unit; poor £5.50 a unit` |
| `wreRent2` | Rent at the second price | `rich £270; middling £150; poor £30` |
| `wreTotal2` | Total rent at the second price | `£450 at £6 a unit` |

Status: `At £5 a unit the lands pay £240 of rent in all; 1 land yields none (poor); it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): A land's produce is worth its output times the price. Smith's rule (I.11): rent is what is left after the wages and the stock advanced are replaced with the ordinary profit, (wages + stock) × (1 + rate/100). When nothing or less than nothing is left the land yields no rent, and the lab shows the loss; total rent adds only the rents above 0 (the lab's rule: a land that cannot pay is not counted as paying a negative rent). The lowest price that affords rent is (wages + stock) × (1 + rate/100) over the output: any price above it leaves a rent. Lands are listed in the order given.


#### rent/tenure — whether the occupier gains from an improvement under each tenure

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `cost` (`wreInCost`) | The improvement's cost | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |
| `added` (`wreInAdded`) | Value of the produce it adds a year | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000 | required |
| `years` (`wreInYears`) | Years the improver gets the benefit | rational (decimal ≤ 6 places or p/q) > 0, ≤ 200 | required |
| `tenures` (`wreInTenures`) | Tenures (tenure, share of the added produce the occupier keeps, share of the cost the occupier pays; each from 0 to 1) | records `a, b; c, d`, 1–12 records, first cell unique: tenure (name), share (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1), bears (rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1) | required |

Example preset (scratch, written for the kit): `{"cost": "100", "added": "20", "years": "9", "tenures": "owner, 1, 1; metayer, 1/2, 1; steelbow, 1/2, 1/2"}`

| tile id | label | printed for the example |
|---|---|---|
| `wreWhole` | The improvement's whole gain | `+£80 (£180 added over 9 years, less £100)` |
| `wreGain` | The occupier's gain under each tenure | `owner +£80; metayer −£10; steelbow +£40` |
| `wreImproves` | Tenures under which the occupier improves | `2: owner, steelbow` |
| `wreLandlord` | The landlord's part | `owner £0; metayer +£90; steelbow +£40` |

Status: `The improvement is worth +£80 to occupier and landlord together; the occupier makes it under owner, steelbow; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Over the years the improvement adds its yearly produce times the years. The occupier keeps the share of that and pays the share of the cost: gain = share × added × years − bears × cost. The occupier improves when the gain is above 0 (the lab's rule; Smith, III.2, argues that a tenant who keeps only part of the produce, or whose lease is short, has little interest in improving). The landlord's part is the rest of the produce less the rest of the cost. Shares are fractions from 0 to 1 (1/2 for a metayer). No interest or discounting is applied.


#### rent/silver — the price of corn in silver, averaged by period

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `prices` (`wreInPrices`) | Prices (year, price of a quarter of wheat) | records `a, b; c, d`, 1–60 records, first cell unique: year (whole 1–3,000), price (rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000) | required |
| `periods` (`wreInPeriods`) | Periods (period, from year, to year) | records `a, b; c, d`, 1–12 records, first cell unique: period (name), from (whole 1–3,000), to (whole 1–3,000) | required |

Example preset (scratch, written for the kit): `{"prices": "1595, 40; 1596, 50; 1597, 60; 1598, 30; 1600, 35; 1601, 45", "periods": "first, 1595, 1597; second, 1598, 1601"}`

| tile id | label | printed for the example |
|---|---|---|
| `wreYears` | Years listed in each period | `first 3 years; second 3 years` |
| `wreAverage` | Average price of a quarter | `first £50; second ≈ £36.67` |
| `wreRatio` | Average against the first period | `first 1×; second 11/15 ≈ 0.73×` |
| `wreCorn` | The value of silver in corn | `first 1/50 = 0.02 quarters for £1; second 3/110 ≈ 0.03 quarters for £1` |

Status: `The average price of a quarter goes from £50 in first to ≈ £36.67 in second, 11/15 ≈ 0.73×; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): A period's average is the mean of the prices of the years listed from its first year to its last, inclusive, exact (shown to two places with ≈ when not exact); a year not listed is not counted, and a period with no year listed is refused. Periods may overlap. The ratio is each average over the first period's. The value of silver in corn is the quarters one unit of money buys at the average, 1/average. Smith averages Windsor market prices this way in the Digression (I.11); the lab takes the prices typed and says nothing of the price in any year not listed. Up to 60 prices.


### interest (`wit`)


#### interest/purchase — the price of land in years' purchase

Lesson-level cfg keys: `money_unit` (default `£`).

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `rent` (`witInRent`) | Rent a year (or any yearly revenue sold) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 10,000,000 | required |
| `rate` (`witInRate`) | Rate of interest, % | rational (decimal ≤ 6 places or p/q) > 0, ≤ 100 | required |
| `rate2` (`witInRate2`) | A second rate to compare, % (- for none) | rational (decimal ≤ 6 places or p/q) > 0, ≤ 100, or `-` | `-` |
| `yield` (`witInYield`) | What the asset yields its present owner a year (- for none) | rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 10,000,000, or `-` | `-` |

Example preset (scratch, written for the kit): `{"rent": "100", "rate": "5", "rate2": "4", "yield": "1"}`

| tile id | label | printed for the example |
|---|---|---|
| `witYp` | Years' purchase | `20 years’ purchase at 5%` |
| `witPrice` | Price | `£2,000` |
| `witYp2` | Years' purchase at the second rate | `25 years’ purchase at 4%` |
| `witPrice2` | Price at the second rate | `£2,500 (+£500, +1/4 = +25%)` |
| `witFetches` | What it fetches against what it yields | `£2,000, 2,000 years of its present yield of £1` |

Status: `At 5% a rent of £100 sells for 20 years’ purchase, £2,000; at 4%, 25 years’ purchase, £2,500; it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Years' purchase = 100 / the rate of interest: the number of years' rent the price equals, so that the rent is the interest on the price. Price = rent × years' purchase. Smith (II.4) gives the rule that the price of land rises as interest falls. With a second rate both are shown and the change in price. With a present yield (the crown lands of V.2, which yield their owner less than the rent a private owner would draw), the price over that yield is the number of years of the present yield the sale fetches.


#### interest/profit — interest as the index of profit

Lesson-level cfg keys: none beyond the common ones.

| field (input id) | label | format and limits | default |
|---|---|---|---|
| `rows` (`witInRows`) | Periods (period, market rate of interest %, then the multiple and a stated profit rate %, each optional; - for none) | records `a, b; c, d`, 1–12 records, first cell unique: period (name), interest (rational (decimal ≤ 6 places or p/q) > 0, ≤ 100); then 0–2 further cells, each rational (decimal ≤ 6 places or p/q) ≥ 0, ≤ 1,000, or `-` | required |

Example preset (scratch, written for the kit): `{"rows": "henry-viii, 10; james-i, 8, -, 15; anne, 5, 3"}`

| tile id | label | printed for the example |
|---|---|---|
| `witImplied` | Implied ordinary profit (interest × multiple) | `henry-viii 10% × 2 = 20%; james-i 8% × 2 = 16%; anne 5% × 3 = 15%` |
| `witLeft` | A stated profit less interest | `james-i 15% − 8% = 7%` |
| `witFall` | First to last | `interest 10% → 5% (−5 points); implied profit 20% → 15% (−5 points)` |

Status: `From henry-viii to anne interest 10% → 5% (−5 points); implied profit 20% → 15% (−5 points); it follows from the figures stated, not from any economy’s records.`

Rules (printed under "How the lab counts."): Smith (I.9) takes the market rate of interest as the index of the ordinary rate of profit, and double interest as a 'reasonable, moderate' profit. The implied profit is interest × the multiple (2 when none is given or it is -). A stated profit less the interest is what is left to the borrower for the risk and trouble of employing the stock. The fall compares the first and last periods given, in percentage points.

## Build-time refusals (Python `check` mirrors the page, sentence for sentence)

Each is raised as `wonkit/<mode>/<view> preset '<id>': <sentence>`, and the page paints the same sentence in red when a reader types the same thing. mathcheck tests the JS side of each one marked †. Every one was raised from Python by a scratch preset (scratchpad `refuse.py`).

| view | sentence |
|---|---|
| division/supply † | `Nations, record 1 (a): 11 at work is more than the population of 10` |
| division/exchange † | `The two producers have the same relative cost (1/2 = 0.50 hours of x for an hour of y), so neither has the lower cost of either good and the relative-cost rule names no division` |
| money/barter | `Traders, record 1 (t): c is not one of the goods` (for has or for wants) |
| money/barter † | `Traders, record 1 (t) has and wants the same good, a` |
| price/parts † | `Every stage’s wages and rent are 0, so there is no price to resolve` |
| price/market | `Buyers, record 2: the price 1 is listed twice` |
| price/market † | `Buyers: at the price 2 buyers take 5, more than the 4 they take at the lower price 1; quantities must not increase as the price rises` (records may be in any order; they are sorted by price) |
| wages/growth † | `The years (30) are not a whole number of doublings of 25 years; a part of a doubling needs a root, which the lab does not take` |
| wages/growth | `The years (100) are not a whole number of doublings of 30 years (the second doubling time); a part of a doubling needs a root, which the lab does not take` |
| advantage/net † | `Limits, record 1: b is not one of the employments` |
| advantage/lottery † | `The successful (3) cannot be more than the entrants (2)` |
| rent/silver | `Periods, record 1 (a): from 1700 is after to 1600` |
| rent/silver † | `Periods, record 1 (a): no year from 1700 to 1800 is listed in the prices` |
| interest/profit † | `Rows, record 1 (a): a multiple of 0 makes profit nothing; give a multiple above 0, or - for 2` |

Every view also gets the field parser's refusals, the same on the page and at build time:
- an empty field;
- not a number or a name;
- a bound broken (`must be more than 0, and it is 0`; `is a whole number from 1 to 10,000, and it is −1`);
- a divide by zero in `p/q`;
- more than 6 decimal places;
- a wrong number of cells in a record;
- too few or too many records (`this lab needs at least 2 records, and there is 1`);
- a name given twice.

The lesson-level refusals are:
- an unknown or stray cfg key;
- a bad unit word;
- a preset key that is not an input (`… is not an input of this view (its inputs are …)`);
- a bad preset id or label;
- an `expect` naming a tile that is not this view's;
- `cfg['preset']` not among the presets;
- an unknown `view` (`wonkit/<mode>: unknown view 'x'; the views are …`);
- an unknown mode.

## Where a rule is the lab's own, not Smith's

Each of these is also said in the view's printed rules sentence.

- **division/market.** Specialists kept are floored to a whole number, and a full-time trade "can live" at ≥ 1.
- **division/exchange.** The relative-cost rule is Ricardo's (1817), and the rules sentence names it as his. Self-sufficiency means equal quantities of both goods. Equal relative costs are refused.
- **money/barter.** What "only through a money" and "no buyer" mean among the traders listed is the lab's reading of Smith's butcher, brewer and baker.
- **price/market.** The market price is the highest listed price at which buyers take at least the quantity brought. The schedule is always the lesson's.
- **price/parts.** Profit is charged on everything advanced at a stage, including the previous stage's price. That is the reading that makes the price resolve exactly into wages, rent and profit (I.6) and makes a profit rise compound (I.9). A wage rise is a % of every stage's wages, and a profit rise is points added to every stage's rate.
- **wages/fund.** Workers are not rounded, because they stand for a rate of population.
- **advantage/net.**
  - Learning is replaced as learning/years + learning × profit% each year (simple, not an annuity).
  - "Other" is the lesson's own money value for Smith's non-money circumstances.
  - A limit's pay rise is stated by the lesson, not derived from the entrants, which are shown and not used.
- **advantage/lottery.** There is no interest, no discounting, and no income for those who fail.
- **rent/residual.** Total rent sums only positive rents.
- **rent/tenure.** The occupier improves exactly when their gain is above 0. There is no discounting.
- **rent/silver.** Years not listed are not counted, and periods may overlap.
- **interest/profit.** The multiple defaults to 2, Smith's "double interest".

## Verification

- **`node scripts/mathcheck.js` passes.** My block prints `wealth of nations: wonkit family A, seven modes` and then nothing (eq prints only on failure). The run ends with `every arithmetic assertion passes`.
  - The block has 45 `eq` assertions, 2 on the printers and 43 across the 18 views (every view has at least one exact-string case, and most also have a refusal or edge case), plus one check that the status of every mode ends with the caution.
  - It runs the shipped JS extracted from `wonkit.py`, `wonkit_core.py`, `acckit.py` (AKT_CORE_JS), `eakit_core.py` and `algebra_core.py`. Inputs are read by `aktRead` with the field specs of `wonkit.py`.
  - The cases use Smith's figures: ten workers, 18 operations, 48,000 pins and 20 alone give `4,800 pins a day | 200 pins a day | 240×`; 240 → 744 pence gives `10/31 ≈ 32.3%`, `744d (£3 2s)` and the creditor's `21/31 ≈ 67.7%`; one in twenty in the law; legal interest at 10, 8, 6 and 5 percent with double interest; doubling every 25 years. Every other figure was worked by hand.
- **Deliberate breaks.** For each view I applied one mutation to a copy of `wonkit.py`, ran the block against the copy, and confirmed that view's case FAILED. The real file was never edited. The mutations:

  | view | mutation | failed |
  |---|---|---|
  | supply | produce = population × output | division/supply |
  | pins | per worker = together / operations | division/pins |
  | exchange | maker of the first good chosen by the higher relative cost | division/exchange |
  | market (wdv) | ceiling instead of floor | division/market |
  | barter | n(n − 1) without /2 | money/barter |
  | coin | 240 × first/this | money/coin |
  | real | measure / price | price/real |
  | parts | profit only on this stage's wages and rent | price/parts |
  | market (wpr) | `>` instead of `≥` against brought | price/market |
  | subsistence | maintenance + multiple | wages/subsistence |
  | fund | workers grown at the fund's rate | wages/fund |
  | growth | 2 × k instead of 2^k | wages/growth |
  | net | no profit on learning | advantage/net |
  | lottery | prizes without the years | advantage/lottery |
  | profit (wad) | true = sales − wages | advantage/profit |
  | residual | no ordinary profit | rent/residual |
  | tenure | occupier bears the whole cost | rent/tenure |
  | silver | period end exclusive | rent/silver |
  | purchase | rate / 100 | interest/purchase |
  | profit (wit) | interest + multiple | interest/profit |
  | printer | unit always before the figure | printers, wages/subsistence, rent/silver |

  The `≥` mutation first survived, because no case had buyers taking exactly the quantity brought. I added `brought 85 → £12 a unit | +£170`, and then it failed.
- **Pages.** I built 20 scratch pages, every view with one or more presets, as markup + controls + script.
  - `node scripts/labcheck.js pages/*/index.html` gave `20 page(s) executed and swept, … 0 failing`.
  - `--observe` printed the tiles quoted above.
  - The `--expect` gate was seen to pass and to fail (Conventions).
- **Tests.**
  - `python3 -m unittest tests.test_speech`: 51 tests OK.
  - `python3 -m unittest tests.test_site_invariants.TestEveryLabBuilds`: 7 tests OK. It builds every registered kit's modes and every lesson's lab, including the `content/wealth_of_nations` package now present.

## Deviations from PLAN §D.1, and choices the table left open

1. **No £sd cell.** This is optional in D.0; see the top of this report. Amounts are in one `money_unit`. coin's `wmoPound` prints whole pence also as £sd (`744d (£3 2s)`), from the pence alone.
2. **Extra unit keys.**
   - `qty_unit` is also on pins (default `pins`), division/market (`units`) and price/market (`units`).
   - `money_unit` is on every view that prints money.
   - `measure_unit` (default `days of labour`) and `period` (default `week`) are where D.1 names them.
3. **exchange is exactly two producers and two goods.** The relative-cost rule as stated compares two.
4. **market (wdv) `days`** is a whole number from 1 to 366, default 300, used only for the output a day.
5. **coin `sum`** is optional (`-`). Without it, `wmoLoss` still gives the share lost, and the money amount (`wmoLossSum`) says `no sum given`. The loss is shown for every later period against the first, not only the last. A later period that coins fewer pence prints `gains … more silver`.
6. **parts rises are ≥ 0.** wage_rise and profit_rise run from 0 to 1,000 (a fall is not modelled). 0 means none. "Both" needs both rises.
7. **wages/growth `doubling2`** uses 0 for none, because a whole field cannot take `-`.
8. **advantage/net `limit` records** are `employment, entrants, pay_rise%`. The pay rise multiplies that employment's wage a day.
9. **interest/profit rows** are `period, interest[, multiple[, profit]]`, with `-` for a skipped multiple (`charles-ii, 6, -, 15`). A multiple of 0 is refused.
10. **silver** allows up to 60 price records ("unless stated" in D.0), because the Windsor tables are long. Years are whole numbers from 1 to 3000.
11. **interest/purchase `rate`** is > 0 and ≤ 100. A yield of 0 prints a sentence rather than divide.
12. **Percentages** come from eaPct: an exact fraction, then the percent whole or to one place with `≈`. A rate typed in percent (Rate) is exact or `p/q ≈ x.xx%`.
