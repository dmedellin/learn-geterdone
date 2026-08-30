# Pedagogy assessment — Backtesting and Trading Systems (trading, course 7)

First-pass assessment, formed from the sixteen lessons, the course home, the
published schema and the per-lesson lab scripts as they stand on `main` at
87504fc. There is no prior assessment of this course, so there is no delta
section.

Course home: `site/backtesting-and-trading-systems/index.html`. Lessons, in
course order: `backtesting-fundamentals`, `testable-trading-rules-and-hypotheses`,
`historical-data-and-data-quality`, `survivorship-selection-and-corporate-actions`,
`timeframes-sessions-and-bar-construction`,
`signal-timing-look-ahead-bias-and-data-leakage`, `trade-execution-simulation`,
`position-sizing-and-portfolio-accounting`,
`transaction-costs-spread-slippage-and-liquidity`,
`trade-log-equity-curve-and-drawdown`, `performance-metrics-and-expectancy`,
`benchmarking-and-risk-adjusted-performance`,
`in-sample-validation-and-out-of-sample-data`, `walk-forward-testing`,
`overfitting-sensitivity-monte-carlo-and-stress-testing`,
`trading-system-specification-and-backtest-report`. The published asset
`trading-system-specification-schema.json` is the export shape lesson 16
claims.

Unlike course 6, each page here ships its own lab: 224 lines are shared
verbatim (the helpers, the bar generator, the two strategy simulators, the
statistics, the three chart painters, the participation-reading table and the
quiz engine) and `initLabSpecific()` is written per lesson. Fourteen of the
sixteen shared blocks were byte-identical; `testable-trading-rules-and-hypotheses`
and `historical-data-and-data-quality` each carried one reading string
corrected on the page that uses it and left stale on the other fifteen. No
figure is written into the static HTML — every number the reader sees is
produced by script — so what can be wrong is the arithmetic, the labs'
verdicts, whether a control does what its label says, and whether a drill
measures what its lesson promised. Every number below was obtained by
executing the shipped script in a stub DOM, not by reading it.

The home says the course "assumes that vocabulary — R-multiples, drawdown and
expectancy are measured here, not introduced here" and that is honest: lessons
07, 08, 10 and 11 use R, drawdown and expectancy with a one-line gloss each,
and course 6 defines them. Inside the course the order holds and the home
states the dependency chain correctly: rules (02) are what the data (03–06) is
fed to, fills (07) and costs (09) are what the equity curve (10) is made of,
the split (13) is what makes walk-forward (14) and stress (15) a test rather
than a second look. Nothing relies on a later lesson. Two things a reader
would need are used before they are said: lesson 02's rule builder exits on a
close-based "opposite condition" at that same close, which lesson 06 will call
impossible; and lesson 01's assumptions table prints parameters the simulator
silently replaced. Both are fixed below.

## What the course teaches well

- **The participation readings are honest about what a synthetic sample can
  show.** The table's own preamble is the best paragraph in the course: a
  backtest is a statement about one past sample under one ruleset, a curve
  built from trades is accounting with no participants to read, and eight labs
  that never draw a price series get no reading on purpose. Where a labelled
  state does not match the generated series (`rules` "bull",
  `dataQuality` "clean:bull") the entry was left empty rather than written
  wrong. Every figure in the readings that could be checked was checked:
  `backtesting-fundamentals` (bull +29.7%, setback 3.5%, final-third low
  123.43; bear −16.2%, high 103.82 at bar 48, low 81.36 at bar 186; range
  95.72–106.11; mixed +19% into bar 53, 93.36 near bar 186; volatile 30% into
  bar 90, 18.7% setback, 112.70 close), `timeframes-sessions-and-bar-construction`
  (seven 60-minute bars, 2.12% against 0.38%, the minute-360 bar at
  110.04/112.25/109.99/111.43, 337 against 1,994 of volume, 110.34 → 106.19,
  10 → 13 signals, the 102.66–104.54 shelf), `trade-execution-simulation`
  (98.66–110.78, 109.49, the 2.61-point close setback, bar 26 at
  102.87 → 106.70, the gap bar at 103.80 with a 103.51 low, 1.81 → 4.61 and
  1.68 → 4.48 of widened range, 103.65 at bar 26 and 94.37 at bar 49),
  `survivorship-selection-and-corporate-actions` (all four single-cause
  states), `benchmarking-and-risk-adjusted-performance` (all four regimes,
  including 137 up steps of 252 under a falling index and the 3.89% largest
  step). Three figures were off and are corrected: "never trade back below
  101.71" (the low is 101.70; the page-local patch was right and is now on
  all sixteen copies), "89.10" (89.07), "94.24" (94.18), and "within a third
  of a percent" (−0.37%; now "within half a percent").
- **The survivorship lab is a complete argument in three switches.** The
  point-in-time universe ends +1.8% while the survivors-only universe ends
  +16.2% with no price changed, the outcome-sorted selection +22.5% with a
  0.5% deepest setback, and the unadjusted split reads as a six-point
  sell-off that nobody sold. The reading says in each case what the chart
  cannot show and why.
- **Expectancy and breakeven are right.** `performance-metrics-and-expectancy`
  computes E = 0.42 × 2.10 − 0.58 × 1.00 − 0.08 = 0.222R and a breakeven of
  (1.00 + 0.08) ÷ (2.10 + 1.00) = 34.8%, both reproduced; the 80-trade sample
  it draws has 34 winners (42.5%), a realized mean of 0.244R and a profit
  factor of 1.39.
- **The split lab hides what it should hide.** `in-sample-validation-and-
  out-of-sample-data` blanks the out-of-sample segment of the equity curve,
  prints "Hidden" in the KPI and the table, and un-reveals whenever the
  parameter or the split moves, so the reader cannot peek and forget.
- **The export validates.** 1,527 specifications generated from the shipped
  `spec()` across the lab's controls (each slider at its minimum and maximum,
  then 1,500 random combinations of every control including the two text
  fields) were validated against the published schema with Draft 2020-12
  semantics: every export the lab marked as passing or review validated;
  the only failures were the empty-name exports the lab itself blocks.
- **Misconceptions are named.** Every lesson's common-mistakes card names the
  predictable wrong model — historical profit as prediction, changing rules
  after each losing period, today's index members for a ten-year test, the
  split that looks like a 50% loss, buying at the close that made the signal,
  filling every touched limit, sizing from ending equity, costs charged only
  to losses, judging risk by final return, optimizing win rate, cash as the
  only benchmark, retuning after each final-test failure, reporting only
  successful windows, choosing the single best cell.

## What the course teaches badly

### The leakage lab makes the leak lose money

`signal-timing-look-ahead-bias-and-data-leakage`: the hero says "Future
information can make weak rules look precise" and the lab's own instruction
is "Add future leakage and observe the inflated result." Checked by
execution at the defaults: the causal baseline returns +11.1% (8 trades, one
loser); the future filter returns +4.7%; same-close execution +7.1%; both
together +5.2%. Every invalid state is *worse* than the honest one, and the
check line prints "Performance difference versus honest baseline: −6.4%" in
amber. The reading had already been written to excuse this ("leakage does
not have to flatter a result"), which is true and beside the point: a reader
who turns the leak on to see inflation sees a penalty, and nothing on the
page shows the thing the lesson exists to warn about. Two causes. The filter
kept a signal only if price added 1.2% inside the next three bars, which on
this sample discards profitable eight-bar trades; and the sample is a
breakout series on which the honest rule already wins seven of eight, so no
filter has losers to remove. The future filter is now the purest leak there
is — it keeps a signal only if the bar the trade will exit on opens above
the entry after costs, i.e. it reads the outcome — and the sample is a mixed
series on which the honest rule is weak: causal −0.9% (7 trades, 4 losers);
future filter +5.4% (3 trades, no losers); same-close −2.8%; both +5.0%.
Verified at every holding period from 2 to 20 bars at the default lookback:
the leaked return exceeds the causal one by at least 5.5 points everywhere;
and across every lookback from 8 to 35 and every hold from 2 to 20 (532
combinations) the leaked run is never below the causal one and never holds
a losing trade, because it cannot. The lab also left a position open at the
end of its signal window and marked it into the KPI while the closed trades
said something else; every position now closes at its exit, so the KPI and
the worked block agree. All four readings are rewritten from the new series.

### The drawdown lab compares different outcomes and calls them the same

`trade-log-equity-curve-and-drawdown`: the hero says "the same average trade
can produce very different account stress when losses cluster", the lab
says "change the order of the same trade outcomes", the Clustered verdict
says "the same average outcomes produce deeper account stress", and quiz
question 3's answer is that the same final return can carry different
drawdowns. The Distributed sequence was eighteen wins summing to 20.2R and
twelve losses; the Clustered sequence was seventeen wins summing to 19.8R and
thirteen losses. Checked by execution at the 1% default: Distributed ends at
$54,172 and Clustered at $53,416, so the Ending equity KPI told the reader
that clustering loses money. The Clustered sequence is now a permutation of
the Distributed one (the same eighteen wins and twelve losses, with the
losses gathered into runs of five, three, two and singles). Because
fixed-percentage sizing compounds multiplicatively the ending equity is now
identical on both — $54,172 — while the maximum drawdown is 4.9% over 11
trades on Clustered against 1.4% over 4 on Distributed (9.6% against 2.8% at
2% risk; 14.1% against 4.2% at 3%). The third sequence, "Large uneven
outcomes", is a different distribution and was always labelled as one; it
stays, and the verdict says so. A worked block prints the peak, the trough,
the division and the recovery required, and says in words that the ending
equity is the same in both orders. That fact is the lesson; before, the lab
contradicted it.

### The walk-forward lab labels folds by arithmetic, not by data

`walk-forward-testing`: each fold card said "Trend", "Balance" or
"Transition" — assigned by fold number modulo three. The market is seven
50-bar segments (bull, range, bear, breakout, volatile, range, bull) and at
the defaults fold 1's forward window (bars 80–109) is range then bear, fold 2
(110–139) is bear, fold 4 (170–199) is breakout: the labels "Trend",
"Balance", "Transition" matched none of them, and at a 15-bar forward
window all twenty folds cycled through the three words regardless of what
they covered. The label is now derived from the segment or segments the
forward window actually spans, and the verdict quotes the fold count
arithmetic the objective promises: with 350 bars, an 80-bar training window
and a 30-bar forward window, the number of folds is ⌊(350 − 80 − 30) ÷ 30⌋ + 1
= 9, and the lab prints that line with the reader's own values.

### A "Bull trend" that falls

`testable-trading-rules-and-hypotheses`: the scenario select offers "Bull
trend" and the series it generates (seed 29, 150 bars) opens at 100.00 and
closes at 89.46, lower in each of its three thirds. The participation table
had noticed — the entry is absent, with a comment explaining why — but the
option was still offered under a name it does not deserve, and the shared
`behaviorFor('bull')` reading had been softened to "This sample is generated
with an upward drift. Whether it actually closes higher is a property of this
sample" to cover it. The same defect in `historical-data-and-data-quality`:
"Bull trend" (seed 41, 120 bars) ends at 98.19 after opening at 100.00, with
its low at bar 90. Both now use a seed on which the bull series is a bull
series — lesson 02: 100.00 → 139.14, third-means 105.3 / 113.2 / 130.0, low
99.10 at bar 2; lesson 03: 100.00 → 127.56, thirds 103.6 / 110.8 / 121.0 —
and each gains a participation entry written from the verified series.

### Two entry rules that are the same rule

`testable-trading-rules-and-hypotheses`: "Close crosses moving average" fired
when the close was above the average and the previous close at or below it;
"Pullback recovers moving average" fired when the close was above the
average and the previous close strictly below it. On this data those are
identical: both produce 4 signals and +4.0% on the breakout scenario at the
defaults, and the exported rule differs only in the word in the `condition`
field. A lesson about determinism offered two labels for one rule. The
pullback rule now is one: the bar's low must have traded below the average
and its close above it (the mirror for shorts), which is what "a pullback
that recovers the average" means and which produces different signals.

### The exported rule is not the rule that ran

Same lesson. The simulation applies the protective stop in every exit mode —
a time exit still leaves at the stop if the stop is hit first — but the JSON
the lab prints under "Time exit" and "Opposite condition" omitted the stop
entirely, so the document the reader is told is the reproducible
specification described a rule with no invalidation while the chart showed
exits at the stop. Under "Opposite moving-average condition" the exit was
filled at the close that produced the condition — the same-close fill lesson
06 spends its whole length forbidding. The export now carries the stop
distance in every mode and the opposite-condition exit fills at the next
bar's open, with the JSON saying so. The KPI "Rule status: Testable" was a
constant string; it is replaced by a count of the lifecycle parts the rule
defines, which is what the lesson asks the reader to verify.

### The assumptions table prints parameters the simulator did not use

`backtesting-fundamentals`: with the fast period set to 30 and the slow to
30 the check says "Fast period must be shorter than slow period", the table
prints "30 / 30", and the simulator quietly runs 30 / 32 (`Math.max(a+2,b)`)
and reports its return. Under "Breakout" the second slider is labelled "Slow
period / holding input" and the hold actually used is ⌊b ÷ 3⌋ = 10 bars,
which appears nowhere. A lesson whose first concept is "rules before results"
showed a result beside a rule that did not produce it. The table now prints
the effective parameters (the periods the averages were computed with, the
lookback and the hold in bars), and a worked block prints the trade returns
and their product: on the mixed sample the two trades are +7.54% and −1.12%,
1.0754 × 0.9888 = 1.0633, the +6.3% in the KPI.

### The accounting lab has no unrealized P/L and no reason codes

`position-sizing-and-portfolio-accounting` promises to "track cash, equity,
buying power, open positions, realized and unrealized P/L, rejected orders".
Its quiz answers that unrealized P/L "affects current equity and exposure",
and lesson 10's common mistake is "ignoring open-position mark-to-market
changes". The lab's equity curve moved only when a trade closed: a position
open for seven signals contributed nothing until its exit, so the chart the
lab drew is exactly the mistake the course names. The one rejected order
said "Rejected" and not why. The curve now marks each open position along a
straight line from entry to its exit value (stated as the assumption it is;
a real test marks at every close), a ledger prints cash, open notional,
unrealized P/L and marked equity at every signal, the rejection names the
limit that bound it ("3 open — position limit" or "exposure would exceed
1.5×"), and a worked block prints the sizing division for the first signal:
$50,000 × 1% = $500 ÷ $2.00 = 250 shares, $12,500 notional.

### The execution lab lacks two of the six order behaviours it promises

`trade-execution-simulation`'s objective names "market, limit, stop,
stop-limit, target, and cancellation"; the lab had market, limit and stop.
Its process step 3 is "Fill, partially fill, cancel, expire, stop, or target
the order" and nothing could cancel or expire. A stop-limit order is added
(trigger at the order price, limit 0.50 beyond it, stated on the page): on
the gap path a long stop-limit at 102 is triggered by bar 22's 103.80 open,
which is outside its 102.50 limit, so it rests and fills at bar 23's 100.41
open — a better price at the cost of not being sure of one, which is the
order's whole character. A time-in-force control cancels a resting limit,
stop or stop-limit after N bars, and the status says "Cancelled after N
bars" with the reason. The target exit also filled at the target level when a
bar opened beyond it — on the gap path, an exit booked at 103.09 on a bar
whose low was 103.51, which the reading itself called "a price that never
traded on that bar". The simulator's stop logic already used the open in
that case; the target now does the same (103.80, 2.36R instead of 2.00R),
and the reading is rewritten from the new figures.

### The robustness lab can never show a stable region

`overfitting-sensitivity-monte-carlo-and-stress-testing`: the only sample is
a mixed series on which the breakout rule has no edge anywhere — the hold-8
row of the surface is 7, 8, −3, 1, −3, −5, −2, −3, −1, −1, −5 percent — so
the "broad stable region" the concept card and quiz question 1 describe
cannot be produced by any control, and every base lookback yields the amber
verdict. The stability score compared the neighbourhood of the *selected*
cell with the *peak* of the row, so at the default (lookback 18, +1.8%) it
printed 0/100 against a flat neighbourhood, and would have printed 0 for a
perfectly stable plateau that happened not to contain the row's best cell.
A second sample is added (a trending series whose hold-8 row is 17, 24, 19,
16, 16, 14, 18, 17, 17, 17, 17 percent — every lookback positive), the
default base is moved to the mixed sample's narrow peak (lookback 9: +8.0%
selected, +1.5% across its neighbours at 5, 13 and 17), and the score is
defined and printed: the share of the selected return retained by the
average of its neighbours, 1.5 ÷ 8.0 = 19% on the narrow peak, against
17.5 ÷ 24.1 = 72% on the plateau. The Monte Carlo and stress modes print
their arithmetic: 300 paths of 15 resampled trades, the 10th percentile as
the 31st-lowest ending return, the round-trip cost multiplied, the best
trades removed by value.

### The split lab shows a selection without the candidates

`in-sample-validation-and-out-of-sample-data`: the button "Select best
in-sample parameter" picks the lookback with the best in-sample return (34
bars, +5.4%) and the reader sees the winner but not the field. The
candidates' in-sample and validation returns disagree — 6 bars is +2.7% /
−0.1%, 34 bars is +5.4% / −0.7%, 40 bars is +1.1% / +0.4% — and that
disagreement is the content of concept card 2 ("Validation: compare
alternatives"). A candidate table now prints every lookback's in-sample and
validation return and trade count, with the out-of-sample column hidden
until the reveal, so the selection is a worked example instead of a button.

### Cost arithmetic asserted, not shown

`transaction-costs-spread-slippage-and-liquidity` prints a bar chart of the
four cost components and a total but never the sum, the impact formula, or
the comparison with the edge that decides the sign of the net result. A
worked block now prints 1.0 + 8.0 + 2 × 5.0 + 1.8 × √1.5 = 21.2 bps against a
14 bps gross edge, net −7.2 bps per round trip in a range (+21 − 21.2 = −0.2
in a trend), and the commission label says it is a round-trip figure, which
the arithmetic assumed and the page did not say.

### The benchmark lab never decomposes

`benchmarking-and-risk-adjusted-performance`'s objective is to "separate
market exposure from independent performance and risk taken". The lab draws
both curves and prints a ratio, but nothing on the page says what part of the
+3.5% is the 1.0 × 6.7% of exposure and what part is independent. A worked
block prints exposure = β × benchmark return, the remainder, and the ratio's
own arithmetic (mean daily excess return ÷ daily standard deviation × √252),
and says the thing the reader most needs to hear on this page: with 10% of
independent volatility, one year cannot distinguish the +4% you set from the
−3.2% the sample delivered.

### A validated dataset that invents prices without saying so

`historical-data-and-data-quality`: the process step is "apply a documented
treatment without inventing unknown prices", the quiz's wrong answer is
"silently invent a price", and the "Validated" view replaced each flagged bar
with the midpoint of its two neighbours and said nothing. The treatment is
now documented on the page as what it is — an interpolation, applied
identically every time, marked as a repair and still an estimate — which is
the difference between a documented treatment and a silent one.

### The specification builder exports what it has just refused

`trading-system-specification-and-backtest-report`: with a same-close fill
on a close-based signal, or risk per trade above the open-risk cap, or a
split that does not total 100, the check says "Blocked" and the Export
button exports anyway. The lesson's own practical rule is "reject incomplete
or contradictory systems before automation". Export now refuses while any
check is a hard failure and says which one. `walkForward` was a constant
`true` while the home describes it as part of the validation plan the reader
sets; it is a control. The delisted name's "Full-period change" in lesson 04
was measured on prices printed after the delisting (−84.3%); it is now
measured to the delisting (−83.6%).

### Distributions promised, not modelled

`survivorship-selection-and-corporate-actions` promises to "adjust splits
and distributions" and its process step separates "price adjustment from
actual cash distributions"; the lab had a split and no distribution. One
name now pays a cash distribution, the ex-date drop is in its quoted price,
and the Adjusted switch adds the cash back while Unadjusted books the drop
as a loss; the readings are rewritten from the re-verified series.

### Drills that do not test what the lesson promised

Every objective is an act — "detect", "build", "define", "prevent", "model",
"track", "deduct", "create … and measure", "calculate", "compare",
"separate", "repeat … and stitch", "test … and verify", "combine". The labs
compute these; the quizzes asked for a number nowhere. Each lesson gains one
question whose answer is a figure the lesson's own formula produces, worked
in the feedback and here:

| lesson | question | answer |
| --- | --- | --- |
| 01 | two trades, +7.5% and −1.1%, compounded | 1.075 × 0.989 = 1.063 → **+6.3%**, not +6.4% |
| 02 | close 104.20 above the 20-bar high of 104.00, signal at the close | **next bar's open**, not 104.20 |
| 03 | a 12-bar breakout count with one missing bar | the hole disqualifies **12** later bars |
| 04 | 2-for-1 split, $110 → $55, adjusted return that step | **0%**; unadjusted −50% |
| 05 | 390-minute session at 60 minutes | 390 ÷ 60 = 6.5 → **7 bars**, the last 30 minutes long |
| 06 | signal on bar 40's close, fill on bar 41's open | **bar 41**; bar 40's close is not available |
| 07 | stop at 100, bar opens 98.50, long | exit **98.50**, the open, not 100 |
| 08 | $50,000 × 1% ÷ $2.00 stop | **250 shares**, $12,500 notional |
| 09 | 1 + 8 + 2 × 5 + 2.2 bps against 14 bps of edge | 21.2 bps → **−7.2 bps** per trade |
| 10 | peak $51,974, trough $49,427 | **4.9%**; recovery 5.2% |
| 11 | 42%, 2.1R wins, 1R losses, 0.08R cost | **0.22R**; breakeven 34.8% |
| 12 | β 1.5, benchmark +6.7%, strategy +1.9% | exposure +10.0% → independent **−8.1%** |
| 13 | 260 bars at 50 / 25 / 25 | **130 / 65 / 65** |
| 14 | 350 bars, train 80, forward 30 | ⌊240 ÷ 30⌋ + 1 = **9 folds** |
| 15 | selected +8.0%, neighbours average +1.5% | 1.5 ÷ 8.0 = **19%** retained |
| 16 | risk per trade 3.5%, open-risk cap 3% | **blocked**; the cap cannot bind |

The quiz engine showed one explanation per question, so the reader who
picked "Guaranteed future profitability" and the one who picked "The next
market direction" were told the same thing. The engine now accepts a
`data-why` on each choice and, on a wrong pick, prefixes the feedback with
that choice's own correction; every distractor on every page has one (64
questions, 128 distractors, checked by parse).

### No lab showed its arithmetic being done

Only the data-quality and survivorship labs printed a table a reader could
check by hand. Every lab now prints a worked block under its chart — the
product of trade returns (01), the parts of the rule that ran (02), the
repair rule and the disqualified-bar count (03), the split step and the
distribution step (04), the bar count division (05), the two returns and
their difference with the number of trades each run kept (06), the fill
arithmetic with the spread and slippage added (07), the sizing division and
the ledger (08), the cost sum against the edge (09), the peak-to-trough
division and the recovery (10), the expectancy and breakeven and the
sample's realized figures beside the modelled ones (11), the exposure
decomposition and the ratio (12), the candidate table (13), the fold count
(14), the retained share, the percentile index and the stress subtraction
(15), the check that blocked the export (16) — so the progression is worked
example (the lab), faded (the reading, which quotes the figures), independent
(the quiz).

### An objective written as "understand"

`backtesting-fundamentals`: "…and understand what a backtest can and cannot
establish" — in the hero, the three description metas, the course-home card,
the README table and the manifest the home calls authoritative. Rewritten as
an act ("…and state what a backtest can and cannot establish") in all seven
places.

## What it claims to teach but does not

- `signal-timing-look-ahead-bias-and-data-leakage` promises an inflated
  result and showed a penalty. Fixed as above.
- `trade-log-equity-curve-and-drawdown` promises that order alone changes
  drawdown and changed the outcomes too. Fixed as above.
- `trade-execution-simulation` names stop-limit orders and cancellation and
  had neither. Fixed as above.
- `position-sizing-and-portfolio-accounting` names unrealized P/L and cash and
  the lab tracked neither. Fixed as above.
- `survivorship-selection-and-corporate-actions` names distributions and had
  only a split. Fixed as above.
- `walk-forward-testing` promises "coverage across regimes" and labelled the
  regimes by fold number. Fixed as above.
- `overfitting-sensitivity-monte-carlo-and-stress-testing` describes a broad
  stable region and had no sample that has one. Fixed as above.
- `timeframes-sessions-and-bar-construction`'s objective says timeframe
  changes "indicators, signals, and fills"; the lab shows signals. The
  reading states what a 60-minute bar cannot say about a stop and a target
  inside it, which is the fill point; an indicator on the bars is not drawn.
  Left, and recorded here: the breakout count is itself an indicator of the
  aggregation, and adding a moving average to the candle chart is a smaller
  gain than the cost of a fourth control on a lab about the clock.
- `performance-metrics-and-expectancy`'s objective lists "return, volatility,
  trade frequency"; the lab shows equity, expectancy, profit factor,
  breakeven and sample uncertainty, and the worked block now adds the realized
  return and the trade count per hundred bars is not modelled. Left: the
  distribution calculator has no clock.

## Where a learner gets stuck

- **Lesson 01, fast 30 / slow 30**: told the rule is invalid and shown its
  return. Fixed.
- **Lesson 02, "Bull trend"**: the chart falls. Fixed.
- **Lesson 02, the JSON**: the stop that closed the last trade is not in the
  document. Fixed.
- **Lesson 06, the Future filter**: the return goes down. Fixed.
- **Lesson 08, the chart**: equity is flat while five positions are open.
  Fixed.
- **Lesson 10, the Ending equity KPI**: differs between "the same outcomes".
  Fixed.
- **Lesson 14, "Fold 1 · Trend"**: over a range-then-bear window. Fixed.
- **Lesson 15, every base**: the verdict is always amber and the score is
  0/100 at the default. Fixed.
- **Lesson 16, Export while Blocked**: the file downloads. Fixed.

## Structural changes considered

None made. No lesson carries more than one hard idea; lesson 15's three modes
are three instruments for one question (does the result survive away from one
exact history), and lesson 04's three switches are three ways a universe can
know the future. The order is the dependency order the home states. No URL is
added, removed or renamed; the five declarations are untouched.

## Verification performed

- Every lab's arithmetic executed from the shipped script in a stub DOM,
  before and after, for every tab and every control position that changes a
  verdict: the fundamentals lab's five regimes under both rules, the invalid
  period pair, and cost 0 and 0.5%; the rule builder's four scenarios, three
  entries, three exits and both sides; the data lab's five defects at 1, 4 and
  5 counts on three markets and both views; the universe lab's five
  combinations; bars at four intervals in both sessions; timing under all four
  states at every hold from 2 to 20 and both samples; execution for all
  eighteen side/path/order combinations plus the unfilled, cancelled and
  stop-limit cases; sizing under three methods and with the limits released;
  costs in three regimes at three sizes and two edges; the three drawdown
  sequences at 1–3% risk; metrics at four win-rate/payoff pairs and three
  sample sizes; the benchmark's four regimes and β ∈ {0, 1, 1.5}; the split
  lab through optimize and reveal at two allocations; walk-forward at four
  window pairs, both candidate sets and a minimum-trade filter; robustness at
  seven bases, 300 and 1,000 paths, and 5× cost with three trades removed; the
  specification builder at the defaults, each slider's extremes and 1,500
  random combinations.
- 1,527 specification exports validated against the published schema: 0
  passed by the lab and rejected by the schema, before and after.
- Every quiz answer index checked against its choices after the rewrite;
  every distractor carries a `why`; no correct choice does; every worked
  answer recomputed by hand in this document.
- The sixteen shared script blocks are byte-identical after the unification
  (one md5).
- The gates in AGENTS.md §7–8 and the CI steps run locally, listed in the
  commit message.
