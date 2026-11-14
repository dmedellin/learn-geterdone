# wonkit, family B (Books II to V): report

Configure a lesson from this report, not from the code. Every example tile
string below was read off a built scratch page (the lab's own JavaScript run in
`labcheck.js`'s DOM shim, every preset selected), and the figures were also
worked by hand; the same strings are pinned in `scripts/mathcheck.js`.

## Files changed (nothing committed)

- `scripts/mathpath/labs/wonkit_b.py` (new). Exposes `MODES` (seven builders,
  `builder(cfg) -> common.Lab`), `SPECS` (the seven spec dicts) and
  `WNB_SHARED_JS`. It imports only `wonkit_core` (never `wonkit.py`).
  `wonkit.wonkit_lab` dispatches any mode it does not own to
  `wonkit_b.MODES[mode](cfg)`.
- `scripts/mathcheck.js`: the block `// ---- wonkit (Wealth of Nations), family B ----`
  … `// ---- end wonkit family B ----`. It sits right after
  `// ---- end acckit family B ----`, and family A's block follows it.
- This report.

## Conventions (every view)

- **Lab cfg.** `("wonkit", {"mode": ..., "view": ..., "presets": [...], "preset": id?, ...})`.
  Every view takes the common keys `mode`, `view`, `presets`, `preset`,
  `title`, `panel_title` and `panel_intro`. It also takes `money_unit` and the
  extra words listed for it below. Any other cfg key is refused, and the
  refusal names the keys the view does take. The default view is the first
  one listed for each mode.
- **Words (cfg, lesson level only).** Each is a string of 1 to 24 characters:
  letters, spaces, dots, hyphens, or `£ $ €`. It must start with a letter or
  one of those symbols, and must not end with a space or hyphen. Anything else
  is refused at build time.
  - `money_unit`. Default `£`. Taken by every view. `£`, `$` and `€` print in
    front with no space (`£1,000`, `−£300`). Any other unit prints after the
    figure with a space (`12.5 s`, `5 s`, `1,000 d`). So `£m` prints
    `1,000 £m`.
  - `qty_unit`. Default `units`. Taken by trade/make, trade/bounty,
    trade/drawback and tax/arithmetic. When the figure is exactly 1, one final
    `s` is dropped (`quarter`, `hogshead`).
  - `silver_unit`. Default `oz`. Taken by debt/debase.
  - `pupil_word`. Default `pupils`. Taken by public/fees (for example
    `suitors`).

  The words also appear in the box labels (`Gross revenue: the whole annual
  produce, in £`) and in some tile labels.
- **Presets.** Each preset is a dict: `id` (lowercase letters, digits and
  hyphens), a plain-text `label`, one value per input, and `expect`. An input
  missing from a preset is taken from the cfg's key of the same name, and
  then from the default listed below. A field with default "required" must be
  given in one of those places.
  - Scalars may be strings (`"1/100"`, `"0.5"`) or ints.
  - Records may be written three ways. As a string: `"food, 20, consumption; loom, 30, fixed"`.
    As a list of cell lists: `[["food", 20, "consumption"], ...]`. Or, a
    family-B addition, as a list of dicts keyed exactly by the cell names
    below: `[{"year": 1700, "rent": 100}, ...]`. A dict with a missing or extra
    key is refused, with the keys named.
  - `expect` maps tile ids to the exact text printed (`{"wbkAbroad": "£800,000"}`).
    Python checks only that the keys are this view's tile ids. `labcheck.js`
    compares the text on the built page, and once `wonkit` is in
    `KITS_WITH_EXPECTATIONS` every preset must pin at least one tile. I
    confirmed this on scratch pages with `labcheck.js --expect`, including a
    preset written with dict records.
- **Numbers typed.**
  - "Rational" means a decimal of at most 6 places, or a fraction `p/q` of
    whole numbers with at most 8 digits on each side. `-` is accepted only
    where a box says "(- for none)".
  - "Whole" means an integer.
  - A name is letters, digits, `.`, `_` or `-`, with **no spaces**: write
    `home-trade`, not `home trade`.
  - `<`, `>`, `&` and `"` are refused in every value.
  - Percentages are typed as percents: `20` means 20%, so one fifth is typed
    `20`. The one exception is the share under arms in public/soldiers, which
    is a fraction (`1/100`).
- **Size limits.** At most 12 records in any list. Money amounts and
  populations may run up to 10,000,000,000.
- **Printing.**
  - Money: a finite decimal is printed as it is, grouped (`£49.5`,
    `£4.125`). Any other fraction prints as the fraction and its value to 2
    places (`£64,000,000/3 ≈ £21,333,333.33`).
  - Compounded or long figures (accumulate, redraw, sinking) are printed to 2
    places by an exact rounding, half away from zero, and marked `≈` when
    rounded (`≈ £11,467.40`).
  - Percentages are exact when they have at most 2 decimal places (`25%`,
    `87.5%`); otherwise they are rounded to 2 places and marked (`≈ 33.33%`).
  - Signed figures carry `+` or `−` (`+£300`, `≈ +2.94%`, `+3 points`).
  - A ratio is printed `12.00×` (acckit's `aktTimes`).
  - No float is ever printed.
- **Every status line** is one sentence of the result and ends with `; it
  follows from the figures stated, not from any economy’s records.`
  (`wnkStatus`). Every view prints its rules under the tiles. The rules say
  which rule is Smith's and which is the lab's own.
- **Hostile input.** Every text box survives `''`, `banana`, `0`, `-1`, `1/0`
  and `A>B`: the page shows a red sentence and the tiles blank to `—`. On all
  20 scratch pages `labcheck.js` reports 0 failing, sweep included.
- **Ids.**
  - An input is `<prefix>In<Field>` (`wstInParts`, `wdbInNew`).
  - The menus and panels are `<prefix>Preset`, `<prefix>Status` and
    `<prefix>Table`.
  - Tiles are the ids listed below.
  - The prefixes are `wst wbk wtr wtx wdb wpb wsy`.
- **Build-time refusals common to all views:**
  - a stray cfg key;
  - a bad word;
  - an unknown view;
  - a preset input that the view does not take;
  - a bad id or label, or an id used twice;
  - an `expect` key that is not a tile id;
  - any field-parse error (the same sentence the page would show, prefixed
    `wonkit/<mode>/<view> preset '<id>': `);
  - the view's own refusals listed below. Python mirrors every one of them,
    in the same words.

---

## stock (wst)

### division
Fields:
- `parts` (required). Records, 1–12, the part name must be unique:
  - `part`: name
  - `amount`: rational ≥ 0
  - `kind`: `consumption`, `fixed` or `circulating`

Tiles (example: food 20 consumption; loom 30 fixed; yarn 40 circulating; cash 10 circulating):

| id | label | example |
|---|---|---|
| wstWhole | Whole stock | `£100` |
| wstConsumption | Reserved for immediate consumption | `£20 (20%)` |
| wstFixed | Fixed capital | `£30 (30%)` |
| wstCirculating | Circulating capital | `£50 (50%)` |
| wstCapital | Capital (fixed and circulating) of the whole | `£80 of £100 (80%)` |
| wstLargest | Largest part of each kind | `consumption food £20; fixed loom £30; circulating yarn £40` |

- A kind with no part reads `none` in wstLargest and `£0 (0%)` in its own tile.
- Ties for the largest part go to the first one given. That is the lab's rule.
- Refusal: `The parts add to nothing, so there is no stock to divide`.

### revenue
Fields:
- `gross` (required): rational > 0.
- `fixed` (required): rational ≥ 0. The upkeep of the fixed capital.
- `money` (required): rational ≥ 0. The upkeep of the money in circulation.
- `saving`: rational ≥ 0 or `-`. Default `-`.

| id | label | example (1000, 120, 30, saving 25) |
|---|---|---|
| wstKeep | Fixed capital and money maintained | `£150 (15% of the gross)` |
| wstNet | Net revenue | `£850` |
| wstNetShare | Net revenue, share of the gross | `85%` |
| wstNew | Net revenue with the saving | `£875 (87.5% of the gross)`; `no saving given` when there is none |
| wstGain | Gain from the saving | `+£25 (≈ +2.94% on the net revenue)` |

Refusals:
- `The maintenance of the fixed capital and of the money, £110, is more than the gross revenue, £100`
- `The saving, £6, is more than the maintenance of the money, £5`

### accumulate
Fields:
- `capital` (required): rational > 0.
- `return` (required): rational 0–100, in % of capital a year. The revenue
  above replacing the capital.
- `saved` (required): rational −100 to 100, in %. Negative values model
  Smith's prodigal.
- `years` (required): whole 0–50.
- `wage`: rational > 0 or `-`. Default `-`. A year's maintenance of one
  productive worker.
- `saved2`: rational −100 to 100 or `-`. Default `-`.

The rule: capital × (1 + return × saved) each year, exactly.

| id | label | example (1000, 10, 50, 2 years, wage 20, saved2 −50) |
|---|---|---|
| wstFirst | First year's revenue | `revenue £100: £50 added to the capital, £50 spent`; with saved −50: `revenue £100: £150 spent, £50 of it taken from the capital` |
| wstRate | Change in the capital a year | `+5% a year` (or `−5% a year`) |
| wstAfter | Capital after the years | `£1,102.5 after 2 years`; at 50 years `≈ £11,467.40 after 50 years` |
| wstChange | Change over the years | `+10.25%`; `no years` at 0 |
| wstLabour | Productive workers maintained, first and last | `50 → ≈ 55.13 workers`; `no wage given` |
| wstSecond | At the second share saved | `£902.5 at −50% saved (−£200 against the first)`; `no second saving given` |

- There are no view-specific refusals. The bounds keep the yearly factor at
  0 or above.
- The table lists every year (0 to n).

### turnover
Fields:
- `trades` (required). Records, 1–12, the trade name must be unique:
  - `trade`: name
  - `capital`: rational > 0
  - `returns`: rational > 0, at most 365. Returns a year: `4`, `1`, `1/3`.
- `wage`: rational > 0 or `-`. Default `-`.

| id | label | example (home 1000 × 4; foreign 1000 × 1; distant 1000 × 1/3; wage 25) |
|---|---|---|
| wstWork | Stock put to work over a year | `home £4,000; foreign £1,000; distant £1,000/3 ≈ £333.33` |
| wstTotal | All the trades together | `£16,000/3 ≈ £5,333.33` |
| wstLabour | Productive workers it maintains | `home 160; foreign 40; distant ≈ 13.33` (`no wage given`) |
| wstOrder | Most to least | `home, foreign, distant`. Ties keep the order given |
| wstRatio | Most against least | `12.00× (home against distant)`; `one trade only` |

No view-specific refusals.

### spend
Fields:
- `revenue` (required): rational > 0.
- `maintenance` (required): rational > 0. One person's maintenance a year.
- `purchases` (required). Records, 1–12, the trade name must be unique:
  - `trade`: name
  - `amount`: rational > 0
  - `makers`: whole 1–10,000,000

| id | label | example (10000, 10; buckles 2000/400, coach 3000/1000, claret 5000/2500) |
|---|---|---|
| wstRetainers | Retainers the revenue could maintain | `1,000 people`; with 105/10: `10.5 people (10 wholly)` |
| wstSpent | Spent on the purchases | `£10,000 of £10,000 (100%)` |
| wstShares | Each maker's share of a maintenance | `buckles 50%; coach 30%; claret 20%` |
| wstPeople | People partly maintained | `3,900 people` (makers summed; a maker in two purchases counts twice) |
| wstDependent | Makers wholly dependent on the buyer | `no one: every maker’s share is under one maintenance`; or `1: a (each maker wholly maintained by the purchase)` |

- The even spread of a purchase over its makers is the lab's rule.
- Refusal: `The purchases add to £110, more than the revenue, £100`.

## bank (wbk)

### paper
Fields:
- `circulation` (required): rational > 0. The coin needed to circulate the
  produce.
- `notes` (required): rational ≥ 0.
- `reserve` (required): rational 0–100, in % of the notes.

| id | label | example: Smith's million (1000000, 1000000, 20) | notes 1,200,000 |
|---|---|---|---|
| wbkKept | Coin kept by the banks | `£200,000` | `£240,000` |
| wbkBefore | Paper and coin poured into the channel | `£1,800,000 (£1,000,000 of notes, £800,000 of coin)` | `£1,960,000 (…)` |
| wbkAbroad | Gold and silver free to go abroad | `£800,000` | `not determined: the notes exceed the circulation` |
| wbkCoin | Coin still circulating | `£0` (with notes 500,000: `£500,000`) | `none` |
| wbkExcess | Notes beyond the circulation, returned on the banks | `none: the notes do not exceed the circulation` | `£200,000` |
| wbkNeeded | Coin the banks need | `£200,000 (the reserve kept)` | `£400,000 (£160,000 more than the reserve kept)` |

The rules:
- abroad = notes − coin kept, while notes ≤ circulation;
- coin still circulating = circulation − notes;
- coin needed = reserve × min(notes, circulation) + (notes − circulation, if
  positive). This rule is the lab's.

Refusal: `The reserve, £500, is more than all the gold and silver in circulation, £100, so the banks could not gather it`.

### redraw
Fields (all required):
- `sum`: rational > 0.
- `interest`: rational 0–100, in % a year.
- `commission`: rational 0–100, in % per draw.
- `months`: whole 1–12. Only 1, 2, 3, 4, 6 or 12 are accepted.
- `years`: whole 1–50.

| id | label | example: Smith's bills (1000, 5, 0.5, 2 months, 3 years) |
|---|---|---|
| wbkDraws | Draws a year | `6 draws a year` |
| wbkSimple | Cost a year, simple | `8% a year, £80` |
| wbkCompound | Cost a year, compound | `≈ 8.27% a year, ≈ £82.71` |
| wbkTotal | Cost over the years | `simple £240, compound ≈ £269.23 over 3 years` |
| wbkExcess | Above the interest stated | `simple +3 points, compound ≈ +3.27 points` |

- Simple = interest + commission × draws.
- Compound: the sum is multiplied by (1 + interest × months/12 + commission)
  at each draw.
- Refusal: `A bill of 5 months does not go a whole number of times into a year; the lab takes bills of 1, 2, 3, 4, 6 or 12 months`.

## trade (wtr)

### make (cfg `qty_unit`)
Fields:
- `goods` (required). Records, 1–12, the good name must be unique:
  - `good`: name
  - `quantity`: rational > 0
  - `home`: rational > 0
  - `foreign`: rational ≥ 0
  - `duty`: rational ≥ 0

| id | label | example (wine 1000, 30, 1, 1/2; cloth 500, 2, 3, 1) |
|---|---|---|
| wtrAbroad | Cost a unit bought abroad, with the duty | `wine £1.5; cloth £4` |
| wtrCheaper | Cheaper | `wine abroad; cloth home` (equal: `either (the same)`) |
| wtrProhibit | Cost to the country of making all at home | `£29,000 a year` |
| wtrDuty | Duty collected | `£500 a year` |
| wtrBuyers | Buyers pay more than at the cheaper price | `£500 a year` |
| wtrLoss | Paid by buyers and not collected as duty | `£0 a year`. For a protective duty (x 100, 5, 4, 2): `£100 a year` |

The rules:
- A good is bought abroad only when the foreign price + duty is less than
  the home cost. When the two are equal it is bought at home. This is the
  lab's rule.
- The prohibition's cost counts the foreign price without the duty, because
  the duty stays within the country.

No view-specific refusals.

### balance
Fields:
- `countries` (required). Records, 1–12, the country name must be unique:
  - `country`: name
  - `exports`: rational ≥ 0
  - `imports`: rational ≥ 0

| id | label | example (france 200/500; portugal 600/300; holland 400/400) |
|---|---|---|
| wtrBalances | Balance with each country | `france −£300; portugal +£300; holland £0` |
| wtrTotal | Balance with all | `£0` |
| wtrUnfavourable | Countries with an unfavourable balance | `1: france` (`0: none`) |
| wtrTwoWay | Two-way trade | `£2,400` |

- The rules and the status line say that the balance is the mercantile
  measure, which Smith rejects.
- No view-specific refusals.

### bounty (cfg `qty_unit`)
Fields (all required, all rational ≥ 0):
- `exported`
- `bounty`
- `home`: the quantity bought at home.
- `rise`: the rise in the home price per unit, as the lesson supposes it.

| id | label | example: Smith IV.5 (1, 5, 31, 4; money_unit `s`, qty_unit `quarters`) |
|---|---|---|
| wtrTreasury | Cost to the treasury | `5 s` |
| wtrConsumers | Cost to home buyers | `124 s` (Smith's £6 4s.) |
| wtrTotal | Together | `129 s` |
| wtrPerUnit | Together, a unit exported | `129 s a quarter exported`; `nothing is exported` |
| wtrRatio | Home buyers' part against the bounty's | `24.8 paid by home buyers for each 1 paid to the bounty`; `no bounty is paid` |

- For a prohibition's cost to consumers, set the bounty to 0.
- No view-specific refusals.

### drawback (cfg `qty_unit`)
Fields:
- `quantity` (required): rational > 0.
- `duty` (required): rational ≥ 0.
- `exported` (required): rational ≥ 0.
- `share`: rational 0–100, in %. Default `100`.

| id | label | example (1000, 3, 600, 75; qty_unit `hogsheads`) |
|---|---|---|
| wtrPaid | Duty paid | `£3,000` |
| wtrDrawn | Drawn back | `£1,350` |
| wtrNet | Net duty | `£1,650` |
| wtrKept | Net duty a unit kept at home | `£4.125 a hogshead on 400 hogsheads`; `nothing is kept at home` |

Refusal: `The quantity re-exported, 11 units, is more than the quantity imported, 10 units`.

## tax (wtx)

### incidence
Fields (both required):
- `wage`: rational > 0.
- `rate`: rational > 0, at most 100, in %.

| id | label | example: Smith V.2 (10, 20; money_unit `s`) |
|---|---|---|
| wtxWage | Wage that leaves the same subsistence | `12.5 s` |
| wtxRise | Rise in the wage | `25% (+2.5 s)` |
| wtxTax | Tax paid | `2.5 s` |
| wtxOver | The rise against the rate | `the rise exceeds the rate by 5 points` |
| wtxAdvances | Who advances the tax | `the employer, in the higher wage` (fixed text; Smith's rule) |

Refusal: `A tax of 100% of the wage takes all of it, and no wage could leave the worker anything`.

**Note for authors:** Smith's own second example (V.2, art. III, l. ≈28333) says
a tax of one tenth raises wages "not one-tenth part only, but one-eighth". His
own rule, wage ÷ (1 − rate), gives one ninth, and the lab prints
`100/9 s ≈ 11.11 s | ≈ 11.11% (+10/9 s ≈ 1.11 s)`. A lesson quoting that
sentence should say that the figure is a slip, or use only the fifth.

### arithmetic (cfg `qty_unit`)
Fields:
- `rows` (required). Records, 2–12, with the duties strictly rising:
  - `duty`: rational ≥ 0
  - `quantity`: rational ≥ 0. The lesson's figure for what pays at that
    duty.

| id | label | example (1,1000; 2,800; 3,500; 4,250; money_unit `d`) |
|---|---|---|
| wtxRevenues | Revenue at each duty | `1 d: 1,000 d; 2 d: 1,600 d; 3 d: 1,500 d; 4 d: 1,000 d` |
| wtxBest | The duty that yields most | `2 d, yielding 1,600 d`. Ties go to the lowest duty (the lab's rule): `£1, yielding £60 (as much at £2, £3)` |
| wtxFalls | Higher duties that yield less | `2: 3 d yields 1,500 d, less than the 1,600 d at 2 d; 4 d yields 1,000 d, less than the 1,500 d at 3 d` (`0: none`) |
| wtxEnds | Highest duty against lowest | `duty 4× the lowest, revenue 1× the lowest’s`. When the lowest duty is 0: `the lowest duty is nothing: revenue from … to …` |

Refusal: `Rows, record 2: the duty £1 is not above the one before it, £1; list the duties from lowest to highest`.

### land
Fields (all required):
- `valuation`: rational > 0.
- `rate`: rational > 0, at most 100, in %.
- `rents`: records, 1–12, with the years strictly rising:
  - `year`: whole 0–9999. Printed ungrouped.
  - `rent`: rational > 0

| id | label | example (100, 20; 1700 100; 1730 150; 1760 300) |
|---|---|---|
| wtxTax | Tax on the valuation | `£20 every year` |
| wtxShares | As a share of the actual rent | `1700 20%; 1730 ≈ 13.33%; 1760 ≈ 6.67%` |
| wtxFollow | The same rate on the actual rent | `1700 £20; 1730 £30; 1760 £60` |
| wtxTotals | Totals over the years | `fixed £60, on the actual rent £110, over 3 years` (only the years listed) |
| wtxDifference | On the rent against on the valuation | `+£50: the tax on the actual rent raises more`; `none: the two raise the same` |

Refusal: `Rents, record 2: the year 1700 is not after the one before it, 1700`.

## debt (wdb)

### sinking
Fields:
- `debt` (required): rational > 0.
- `interest` (required): rational 0–100, in %.
- `payment` (required): rational ≥ 0.
- `years` (required): whole 0–200.
- `borrow`: records, 0–12. Default empty.
  - `year`: whole 1–200
  - `amount`: rational > 0

| id | label | example (1000, 4, 100, 20 years, borrow `5, 200`) |
|---|---|---|
| wdbFirst | Interest of the first year | `£40` |
| wdbOff | Paid off | `in year 16`; `not paid off within 3 years`; `no years computed` |
| wdbEnd | Debt at the end | `£0 after 20 years` |
| wdbInterest | Interest paid | `≈ £398.42` |
| wdbPaid | Paid in all | `≈ £1,598.42` |
| wdbBorrowed | Borrowed again | `£200` |

The rules:
- Interest is paid first, and the rest of the payment goes to the debt.
- The final payment is only what is owed.
- A year with no debt bears no interest and takes no payment.
- A loan is added at the end of its year.
- "Paid off" is the first year from which the debt stays at 0 to the end of
  the years computed.

These are the lab's rules. I checked the 20-year example against an
independent Fraction loop.

Refusals, checked in this order:
1. `Borrow, record 1: year 6 is beyond the 5 years computed`
2. `Borrow names year 2 twice`
3. `A payment of £4 a year is less than the interest of the first year, £5, so the debt grows every year`

### debase (cfg `silver_unit`)
Fields (all required):
- `debt`: rational > 0.
- `old`: rational > 0. The silver in a unit of coin before.
- `new`: rational > 0. The silver in a unit of coin after.

| id | label | example: Smith V.3, the as (128000000, 12, 2; silver_unit `oz copper`) |
|---|---|---|
| wdbOwed | Silver owed | `1,536,000,000 oz copper` |
| wdbSilver | Silver paid | `256,000,000 oz copper` |
| wdbLoss | Lost by the creditor | `≈ 83.33% (1,280,000,000 oz copper)` |
| wdbPretended | The pretended payment | `£128,000,000 paid in name, worth £64,000,000/3 ≈ £21,333,333.33 in the old coin` (Smith's £21,333,333 6s. 8d.) |

Refusal: `The coin after holds more silver, 2 oz, than before, 1 oz; raising the denomination lowers the silver in a unit`.

## public (wpb)

### soldiers
Fields:
- `population` (required): whole 1 to 10,000,000,000.
- `share` (required): rational > 0, at most 1. A fraction, for example
  `1/100`.
- `cost`: rational > 0 or `-`. Default `-`.

| id | label | example: Smith V.1 (1000000, 1/100, 12) |
|---|---|---|
| wpbSoldiers | Soldiers | `10,000`; with 1001: `10.01 (10 whole soldiers)` |
| wpbOthers | Others at work for each soldier | `99` |
| wpbCost | Cost a year | `£120,000 a year`; `no cost given` |
| wpbPerHead | Cost per head of the population | `£0.12 a head a year` |

- There is no table.
- No view-specific refusals.

### fees (cfg `pupil_word`)
Fields:
- `people` (required). Records, 1–12, the person name must be unique:
  - `person`: name
  - `salary`: rational ≥ 0
  - `pupils`: whole ≥ 0
  - `fee`: rational ≥ 0

| id | label | example (endowed 200,10,1; paid 20,60,3; idle 0,0,2) |
|---|---|---|
| wpbFees | Income from fees | `endowed £10; paid £180; idle £0` |
| wpbIncome | Income in all | `endowed £210; paid £200; idle £0` |
| wpbShare | Share of income from fees | `endowed ≈ 4.76%; paid 90%; idle no income` |
| wpbMore | Added by one more of the pupils | `endowed +£1; paid +£3; idle +£2` |
| wpbMost | Depends most on diligence | `paid (90% from fees)`. Ties name everyone: `a, b (100% from fees)`. With no income at all: `no one has an income` |

No view-specific refusals.

### tolls
Fields (both required):
- `carriages`: records, 1–12, the carriage name must be unique:
  - `carriage`: name
  - `weight`: rational > 0, in tons per trip
  - `trips`: whole ≥ 0
- `toll`: rational ≥ 0, per ton per trip.

| id | label | example (coach 2,100; waggon 4,50; cart 1,300; toll 1/4) |
|---|---|---|
| wpbTolls | Toll each pays a year | `coach £50; waggon £50; cart £75` |
| wpbTotal | All the tolls | `£175 a year` |
| wpbHeaviest | The heaviest carriage | `waggon £50 (≈ 28.57% of the total)`. This is the largest weight per trip, first of equals (the lab's rule). With nothing paid: `a £0, and no toll is paid` |
| wpbTons | Tons carried a year | `700 tons` |
| wpbPerTon | Toll a ton carried | `£0.25 a ton`; `nothing is carried` |

No view-specific refusals.

## system (wsy)

### classes
Fields:
- `classes` (required). Records, 2–12, the class name must be unique:
  - `class`: name
  - `produce`: rational ≥ 0
  - `consumption`: rational ≥ 0
  - `advances`: rational ≥ 0

| id | label | example (proprietors 0,2,0; cultivators 5,2,1; artificers 2,1,1) |
|---|---|---|
| wsyNet | Net product of each class | `proprietors −£2; cultivators +£2; artificers £0` |
| wsyProductive | Classes with a net product | `1: cultivators` |
| wsyBarren | Classes with none (barren under these figures) | `1: artificers` |
| wsyShort | Classes producing less than they use | `1: proprietors` |
| wsyTotal | Net product of the whole table | `£0` |

- The rules and the status line say that the figures are the table's
  assumption, not a measurement.
- No view-specific refusals.

---

## Deviations from PLAN §D.2, and why

1. **bank/paper.**
   - PLAN gives "coin replaced and free to go abroad = circulation − reserve
     coin". That holds only when notes = circulation, as in Smith's case. The
     lab uses notes − coin kept, which is Smith's mechanism for any issue up
     to the circulation and gives his £800,000.
   - When notes exceed the circulation, what goes abroad is printed as "not
     determined", because the inputs do not fix it.
   - The coin-needed rule is the lab's, and the rules say so.
   - Added: the tiles wbkBefore (Smith's "eighteen hundred thousand pounds")
     and wbkCoin, and a refusal of a reserve larger than all the coin.
2. **bank/redraw.** The term must go a whole number of times into a year, so
   that compounding is over whole draws. Years must be 1–50.
3. **stock/accumulate.** The comparison path is `saved2`, the input PLAN
   names. Two presets also compare, as separate presets.
   - `return` is bounded to 0–100 and `saved` to −100 to 100, so the capital
     never goes below 0 and no refusal is needed.
   - The "share spent on unproductive hands" in lesson 8.1 is 100 − saved,
     shown in wstFirst.
4. **trade/make.** The duty is not counted in a prohibition's cost to the
   country, since it is a transfer within the country. Two tiles say what
   the duty costs buyers and how much of it the treasury does not collect.
5. **tax/arithmetic, tax/land.** Rows must be in rising order of duty or year.
   PLAN does not say how to order "a higher duty" otherwise.
6. **tax/incidence.** wtxAdvances is a fixed sentence (Smith's rule), not a
   figure. Note Smith's one-eighth slip, above.
7. **Extra cfg words** beyond `money_unit`: `qty_unit`, `silver_unit` and
   `pupil_word`. PLAN's "(or suitors and fee)" in public/fees is `pupil_word`.
   public/tolls weighs only in tons, a fixed word.
8. **Record values as lists of dicts** are accepted (family B only). Every
   other kit takes strings or cell lists.
9. **No £sd cell.** Family A did not add one. Amounts are decimals or
   fractions in `money_unit`: £21,333,333 6s. 8d. prints as
   `£64,000,000/3 ≈ £21,333,333.33`.

## Content found failing against this kit (not mine to edit; for the content authors)

I built every lesson cfg in `content/wealth_of_nations/c*/part_*.py` that
uses a family-B mode. 23 build. 4 fail because a record name contains a
space, which ea.NAME refuses:

- c07 `stock-must-be-accumulated-first` (`loom and tools`)
- c07 `fixed-and-circulating-capital` (`clothes and furniture`)
- c08 `home-foreign-and-carrying-trade` (`home trade`)
- c09 `how-commerce-improved-the-country` (`retainers and tenants`)

The fix is hyphens: `loom-and-tools`. Their `expect` dicts are empty: every
preset needs at least one pinned tile before `wonkit` joins
`KITS_WITH_EXPECTATIONS`.

## Verification

- `node scripts/mathcheck.js`: passes. Family B's block runs 69 assertions,
  each a case on stated inputs, one or more per view, with Smith's figures
  where the PLAN names them. It also confirms that `''`, `banana`, `0`, `-1`,
  `1/0` and `A>B` are refused with a sentence.
- **Deliberate breaks.** I broke the code 29 times, one line each:
  - every view's central formula, plus a second break in division (tie),
    accumulate (year count), paper (needed), redraw (simple), make (tie and
    the prohibition's cost) and sinking (the paid-off reset);
  - three shared printers.

  Each break made the block fail, and the file was restored and hash-checked.
- Every view's preset builds in Python. On 20 scratch pages `labcheck.js` (with
  its sweep) reports 0 failing, and the pinned expectations matched
  (`--expect`).
