# Pedagogy assessment — Trading Risk Management (trading, course 6)

First-pass assessment, formed from the sixteen lessons, the course home, the
published schema and the shared lab script as they stand on `main` at
14c48ee. There is no prior assessment of this course, so there is no delta
section.

Course home: `site/trading-risk-management/index.html`. Lessons, in course
order: `risk-management-fundamentals`, `account-risk-and-risk-budget`,
`risk-per-trade`, `stop-loss-and-structural-invalidation`, `position-sizing`,
`reward-to-risk-and-r-multiples`, `win-rate-average-win-loss-and-expectancy`,
`losing-streaks-and-drawdown`, `risk-of-ruin`, `volatility-and-atr-based-risk`,
`gap-slippage-liquidity-and-execution-risk`, `leverage-and-margin-risk`,
`correlation-concentration-and-portfolio-exposure`, `options-risk-management`,
`daily-and-weekly-risk-limits`, `trading-risk-plan`. The published asset
`trading-risk-plan-schema.json` is the export shape lesson 16 claims.

Every lesson ships one shared script — all sixteen labs, the price-series
generator, the participation-reading table and the quiz engine — and a
`window.LESSON.lab` key selects which lab runs. Twelve copies were byte-identical
and four (`stop-loss-and-structural-invalidation`, `position-sizing`,
`reward-to-risk-and-r-multiples`, `options-risk-management`) each carried one
reading string corrected on the page that uses it and left stale on the
other fifteen. No figure is written into the static HTML: every number is
produced by script, so what can be wrong is the arithmetic, the labs'
verdicts, and whether a drill measures what its lesson promised. Every
number below was obtained by executing the shipped script in a stub DOM, not
by reading it.

Courses 1–5 are the declared predecessors and the home says nothing is loaded
from them. What it assumes is vocabulary: "swing", "protected low", "range
boundary" and "candle-close or wick rules" (courses 1–2) in lessons 04 and 06,
"tested value areas" (course 5) in lesson 06, "American-style" and
"assignment" (course 3) in lesson 14, each used with enough in-place gloss to
stand alone. Two terms were not glossed anywhere and now are: *beta* in
lesson 13's lab (the calculation depended on it and the page never said what
it was) and *theta* / *vega* in lesson 14's practical rules. Inside the course
the order holds and the home states the dependency chain correctly: the
budget (02) is what risk per trade (03) spends, the stop (04) is what size
(05) divides by, R (06) is the unit expectancy (07) is measured in, drawdown
(08) is what makes ruin (09) a number. Lesson 05 uses "slippage" six lessons
before lesson 11 defines it; the process step now defines it in place and
names the lesson it belongs to.

## What the course teaches well

- **Size is an output.** The home, the stage-2 blurb, lessons 04 and 05 and
  every one of their verdicts say the same thing in the same order: the stop
  goes where the idea is wrong, the risk is fixed in dollars, and the quantity
  is whatever is left to solve for. The course never lets a share count be
  chosen first.
- **The fixed-percentage arithmetic is right.** `risk-per-trade`'s table —
  ten 1% losses leave $45,219 (−9.6%, +10.6% to recover), ten 2% losses
  $40,854 (−18.3%, +22.4%), ten 5% losses $29,937 (−40.1%, +67.0%) — and
  `losing-streaks-and-drawdown`'s recovery rule 1 ÷ (1 − d) − 1 were
  reproduced exactly.
- **Expectancy is shown as arithmetic, not asserted.** `win-rate-average-
  win-loss-and-expectancy` prints E = (42% × 2.00R) − (58% × 1.00R) − 0.08R
  = 0.18R beside a synthetic sequence, and its breakeven win rate of 36.0% is
  the correct (loss + cost) ÷ (win + loss).
- **The margin arithmetic is right.** `leverage-and-margin-risk`: $25,000 at
  2× is $50,000 of exposure; −8% is −$4,000 = −16% of equity; the $46,000
  position at 30% requires $13,800 against $21,000, no deficit. The lesson
  says buying power is a permission and not a limit, and says it three times.
- **The execution reading is honest about what a chart can show.** Every
  participation reading in `gap-slippage-liquidity-and-execution-risk` states
  that the drawn gap (5.00 with nothing printed between, true range 5.72
  against a median of 1.15) is the plan and the fill is the outcome, and that
  they separate exactly where no trade occurred.
- **The plan export validates.** 118,098 combinations of the lab's controls
  (every slider at its minimum, default and maximum, both option toggles) were
  generated from the shipped `riskPlanSpec` and validated against the
  published schema with Draft 2020-12 semantics: 0 failures, before and
  after. The home is explicit that no performance object exists in the shape.
- **Misconceptions are named.** Every lesson's common-mistakes card names the
  predictable wrong model — confidence as a sizing input, the stop that feels
  comfortable, the same share count for every setup, buying power as budget,
  premium received as the amount at risk, the recovery trade after the limit.

## What the course teaches badly

### The drawdown lab compares different outcomes and calls them the same

`losing-streaks-and-drawdown`: the verdict on the Clustered tab says "The
same total outcomes create a deeper and longer drawdown when losses cluster",
and quiz question 3's answer is that "the same set of outcomes can create
different drawdowns depending on order". The Clustered sequence was eight wins
and twelve losses; the Distributed and Early sequences were nine wins and
eleven losses. Checked by execution: Clustered ended at $51,418 and the other
two at $52,976, so a reader comparing the Ending equity KPI across tabs was
shown that clustering *loses money*, which is not the lesson and not true.
The three sequences are now permutations of one multiset (nine wins of
2, 1.5, 2.2, 1.4, 2, 1.8, 2.4, 1.7, 2 and eleven losses of −1). Because
fixed-percentage sizing compounds multiplicatively, the ending equity is now
identical on all three tabs — $52,976 — while the maximum drawdown is 10.5%
over 11 trades (Clustered), 4.9% over 7 (Early) and 2.0% over 4
(Distributed). The formula block prints the peak, the trough, the division
and the recovery, and says in words that the ending equity is the same in all
three orders. That fact is the lesson; before, the lab contradicted it.

### The correlation lab makes lower correlation cost more

`correlation-concentration-and-portfolio-exposure`: the stress loss was
computed as value × shock × (corr + (1 − corr) × beta), so at correlation 0
a 1.3-beta position fell 10.4% on an 8% shock and at correlation 1 it fell
8%. Checked by execution: total stress P/L −$3,864 at correlation 0, −$3,414
at 0.75, −$3,264 at 1 — the loss *shrinks* as correlation rises — while the
reading at low correlation says "Lower correlation reduces combined
movement". The model is now value × shock × beta × correlation, with the
slider labelled *stress correlation* (0.25–1) and defined in the formula
block as the share of each position's beta-move that the common shock passes
through. Now −$966 at 0.25, −$1,932 at 0.5, −$2,898 at 0.75 and −$3,864 at
1.0, which is the direction every sentence on the page asserts. The formula
block prints each position's product and the sum against the $1,170 of
planned stops (2.5× the heat at the default), which is the point the lesson
is making: a shock through every stop at once is not bounded by any one of
them. Planned risk per position now scales with the position's value
(2.5%, 2.5%, 2.5%, 1.5%) rather than staying fixed when the value slider is
moved to zero.

### The options lab's sensitivity adjustment has the wrong sign for short premium

`options-risk-management`: the modeled P/L added iv × premium × 0.35 and
subtracted days × premium × 0.25 for every structure. For a long option that
is the right direction; for a call credit spread, a covered call or a
cash-secured put it is backwards — those structures *gain* as time passes
and as implied volatility falls. Checked by execution at the defaults (IV
−10%, 7 days): the credit spread showed −$18 where the expiration payoff was
+$10 and the adjustment should have added $28, not removed it. The sign is
now reversed for the three short-premium structures (+$38), and the formula
block prints the expiration payoff at the scenario price, the adjustment with
its stated conventions and direction, and the sum.

The verdicts were wrong in the same lab for other reasons. A short-premium
structure with the underlying *falling* was read as "The underlying moved
against the short-premium position" — for a call credit spread a fall is the
best case (payoff +$300 at −5%). A call debit spread with the underlying up
8% (payoff +$200) was read as "The underlying did not move enough in the
required direction" because the branch only recognised a long call or a long
put. The short-premium verdict now reads the sign of the expiration payoff at
the scenario price (negative: "the structure's expiration payoff is negative
… premium received is not the amount at risk: the maximum loss is $X";
otherwise: "keeps some or all of the premium at expiration; the obligation
remains open"); the long-premium verdict treats the debit spread as the long
call it is. Checked for all six structures in both directions. The covered
call's maximum risk was the string "Stock downside less premium"; it is now
the number, (spot − premium) × 100, as the cash-secured put's already was.

### The loss-limit lab demonstrates that the limit costs money

`daily-and-weekly-risk-limits`: one synthetic day, −1, −1, +0.6, −1, −1, +2,
−1, +1.2, −1, +2.1. With the hard limit on, trading stops at −3.4R after
trade five; with it off the day finishes at −0.1R. The verdict admits that
"later synthetic trades would have won" and says "the rule controls damage,
not hindsight", but the only numbers the reader can compare say that
ignoring the limit was worth 3.3R. The lab now has a second day type,
Keeps losing (−1, −1, +0.6, −1, −1, −1, +0.5, −1, −1, −1), which the same
limit holds to −3.4R and which runs to −6.9R without it; the verdict on the
recovering day says in figures what the rule cost on this day and what it
saved on the other, and that at trade five the two days cannot be told apart.
The weekly limit, which the lesson title promises, could not bind before:
the lab had one session and the weekly figure was compared against the same
number as the daily one. There is now an "already lost this week" input
(default 2R), the weekly remainder is drawn as its own line, and the stop
reports which limit it was (at 4.5R carried, the weekly limit stops the day at
−2.0R after two trades). A running-total line prints the addition.

### The risk-budget lab does not allocate what the objective says it allocates

`account-risk-and-risk-budget` promises to "allocate risk across individual
trades, open positions, daily limits, and weekly limits". The lab had no
individual trade in it — nothing to fit or refuse — and the weekly limit was
a KPI that entered no calculation. It now takes the next trade's planned
loss and what was lost earlier in the week, computes the daily and weekly
remainders separately, reports which one binds, and says whether the trade
fits: at the defaults, $1,000 − $300 − $400 = $300 of daily budget against a
$250 trade (fits); at 0.75% it does not; at 4% lost earlier in the week the
weekly budget is gone while $300 of daily budget remains, and the verdict says
so. The concept card that described open risk as "adjusted for shared
exposure" — an adjustment the lab does not make and lesson 13 owns — now says
where that adjustment lives. The bar chart's heights are clamped; before, a
realized loss above the daily limit drew off the canvas.

### Stop-limit filled worse than market with no gap

`gap-slippage-liquidity-and-execution-risk`: the stop-limit branch filled at
a fixed trigger − 0.25 whenever the gap was at most 0.5, so with no gap at all
it lost $2,125 against $2,020 for the stop-market order — a limit order
protecting price and getting a *worse* price. The "Manual market" option was
arithmetically identical to "Stop → market" and demonstrated nothing; the
lesson's objective names "available liquidity is insufficient" and the lab
had no depth in it. The stop-limit now names its limit (trigger − 0.50),
fills at the same price a market order would when that price is inside the
limit, and reports unfilled — with the reason — when it is not or when the
quantity exceeds what is available inside the limit. The third order type is
gone, and a depth input takes its place: shares beyond the size available at
the first price fill a stated 0.50 lower (2,000 shares against 1,000 of
depth: fill 93.71 instead of 93.96, $12,580 against $8,000 planned). The
formula line prints the fill's four subtractions and the loss multiplication.

### The quantity the lab reports is not the one its own figures give

`volatility-and-atr-based-risk` reported 212 shares beside "ATR $1.18, stop
distance $2.36": $500 ÷ $2.36 is 211.9, and the lab was dividing by the
unrounded 2.358. A reader who checks the arithmetic gets a different answer
from the page. The distance is now rounded to the cent before the division,
in this lab and in `stop-loss-and-structural-invalidation` and
`position-sizing` (where it happened not to matter at the defaults). The ATR
table's header said "2× ATR distance" while the column used the multiplier
slider; it now says `${mult}×`. The formula block prints the sum of the
last N true ranges, the division, the multiplication and the size, and says
that it is a simple average where most platforms apply Wilder's smoothing —
the concept card said "smoothed", which a reader moving to a platform would
have found to be a different number.

### Figures shown to the dollar that needed the cent

`position-sizing`: the KPI "Risk per unit" printed $4 for a unit risk of
$4.12 and "Unused risk budget" printed $0 for $0.08, because `money()` rounds
to whole dollars. Both now show cents, and the formula block prints the
budget multiplication, the per-unit addition and the division ($375 ÷ $4.12 =
91.02 → 91).

### The plan validator misses the contradiction lesson 15 sets up

`trading-risk-plan`: lesson 15 says the daily limit counts realized loss
*plus open risk*. The default plan allowed 3% of open risk under a 2.5%
daily limit, so a plan with every open stop hit is over its daily limit
before anything is realized, and the validator called it "internally
consistent". The check is added (as a hard failure, with lesson 15 cited),
the default daily limit is 3%, and the over-count warning now prints the
arithmetic (4 × 1.00% = 4.00%). `requireAssignmentBuyingPower` was exported
as a constant `true` while the home described it as one of the options rules
the reader sets; it is now a control.

### A reading that describes a chart the lab does not draw

`reward-to-risk-and-r-multiples`: the drawn series is fixed and the exit is a
slider, so the structural verdicts "Buyers moved price higher, but not by a
full initial-risk distance" (partial) and "Sellers moved price below entry"
(adverse) described a chart that goes 7.30 above entry on the partial tab
and 10.08 below on the adverse one. The page's own copy had already been
patched for the full-R case; all three verdicts now say what they can
honestly say — what the exit *you entered* is relative to entry — and the
participation readings carry the qualification. The target ratio was an
absolute value, so a target below entry on a long read +0.75R; it is signed.
A formula block prints 1R, the result, the division and the target ratio.

### Drills that do not test what the lesson promised

Every lesson's objective is an act of calculation — "define a planned loss",
"allocate", "measure … the return required to recover", "size the position",
"calculate shares or contracts", "express trade outcomes in units of initial
risk", "combine … to estimate the average outcome", "measure peak-to-trough
decline", "estimate … the probability", "adapt stop distance and position
size", "model the difference between the planned stop and the actual fill",
"measure how positions … behave like one oversized trade", "compare premium
risk". The labs compute them; the quizzes asked for a number in only five
places (lessons 03, 06, 07, 08, 12 — the 50% recovery, $400 ÷ $200, the 40%
expectancy, the 20% drawdown, 4× × 5%). Each lesson gains one question whose
answer is a number the lesson's formula produces, with the arithmetic worked
in the feedback:

| lesson | question | answer |
| --- | --- | --- |
| 01 | $40,000 at 1.25% | **$500** |
| 02 | $1,000 limit, $300 realized, $400 open, next trade $350 | $300 left → **does not fit** |
| 03 | three 2% losses at a fixed percentage | 0.98³ = 0.9412 → **5.9%** (not 6.0%) |
| 04 | entry 113.80, protected low 108.50, stop 0.15 under, $500 | $500 ÷ $5.45 = 91.7 → **91** |
| 05 | $40,000 at 1%, 52.00/50.00, 0.10 reserve | $400 ÷ $2.10 = 190.5 → **190** |
| 06 | half out at +2R, half stopped at −1R on $300 | **+0.5R**, +$150 |
| 07 | wins 1.5R, losses 1R, no cost | 1 ÷ 2.5 → **40%** breakeven |
| 08 | peak $60,000, trough $51,000 | **15%**, recovery **17.6%** |
| 09 | 5% per trade to a −50% threshold | 0.95¹⁴ = 0.488 → **14** losses (69 at 1%) |
| 10 | ATR 1.50, 2× ATR, $600 | **3.00 and 200 shares** |
| 11 | 500 shares, trigger 40.00, fill 39.70 | 0.30 × 500 = **$150** |
| 12 | $25,000 at 4×, −15%, 30% maintenance | **$10,000 equity, $15,500 short** |
| 13 | three $400 stops gapped 2.5 stop-distances | **$3,000** against $1,200 of heat |
| 14 | short 50 put for $1.20, stock to zero | (50 − 1.20) × 100 = **$4,880** |
| 15 | 3R limit, −1.5R realized, 1R open, 1R trade | 0.5R left → **no** |
| 16 | 1% × 4 positions against a 5% open-risk cap | **cap exceeds 4%, never binds** |

The quiz engine showed one explanation per question, so a reader who picked
"6.0%" and one who picked "8.0%" on lesson 03 were told the same thing. The
engine now accepts a `data-why` on each choice and, on a wrong pick, prefixes
the feedback with that choice's own correction; every distractor on every
page has one (64 questions, 128 distractors, checked by parse). The engine
was driven through a wrong click, a repeated click and a right click in a
stub DOM: the wrong one shows its `why` then the rule, the repeat is ignored,
the right one shows the rule alone.

### No lab showed its arithmetic being done

Only `stop-loss-and-structural-invalidation`, `win-rate-average-win-loss-and-
expectancy` and `gap-slippage-liquidity-and-execution-risk` printed a
formula. Every lab now prints a worked block under its chart — the planned
loss multiplication (01), the two budget subtractions and the fit test (02),
the compounding power beside the same losses at a fixed dollar amount (03:
ten 1% losses leave $45,219 against $45,000 at a fixed $500; twenty-five 5%
losses leave $13,869 while the fixed-dollar account is gone), the distance
and the division (04, 05, 10), 1R and the R-multiple (06), the breakeven
division and the sample's own win count (07), the peak-to-trough division
and the recovery (08), the per-trade expectancy and the number of consecutive
average losses that reach the threshold from the start (09: 35 at 2%, 69 at
1%, 14 at 5%), the exposure, P/L and requirement (12) with the move at which
the requirement is reached (−28.6% at 2× and 30%; "below the requirement at
entry" at 4×), each position's product and the sum against the heat (13),
the expiration payoff and the adjustment (14), the running total against the
limit (15) — so the progression is worked example (the lab), faded (the
reading, which quotes the figures), independent (the quiz).

### Objectives written as "understand"

`risk-management-fundamentals` ("Understand which trading risks can be
controlled…"), `losing-streaks-and-drawdown` ("…understand recovery
requirements…") and `leverage-and-margin-risk` ("Understand how leverage
magnifies…") — in the hero, the three description metas, the course-home
card, the README table and the manifest the home calls authoritative.
Rewritten as acts ("Sort a trade's variables into the ones you set and the
ones you absorb, state the planned loss in dollars before entry…", "…compute
the gain required to recover it…", "Compute how far a price move reaches
account equity through leverage, check a position against a maintenance
requirement, and say why buying power is not a risk limit") in all seven
places.

### Copy errors a reader would trust

- `stop-loss-and-structural-invalidation`'s reading: "Lows rise from 108.50
  at bar 30 to 112.27 at bar 42" on fifteen copies; the page that uses it had
  been corrected to bar 41, which is right (bar 42's low is 112.12). All
  sixteen copies now carry the verified sentence, and the four patched
  strings are unified the same way; the scripts are byte-identical again.
- `reward-to-risk-and-r-multiples`, adverse reading: "after the entry bar it
  … never trades more than 0.82 above" — 0.82 is the entry bar's own high;
  after it the figure is 0.31. Both are now stated.
- Every other figure in the participation table was reproduced: the
  protected low 108.35, the entry 113.80, the tight stop 1.05 above, the two
  lows of 109.25 and 108.50 inside the swing, the wide stop at a price last
  traded twenty-nine bars before entry; the sizing series' 5.86 and 0.33
  under entry with nothing 6.00 under in the last thirty-one bars; the quiet
  regime's 100.40 → 107.74 with ATR 1.13–1.29 at every period and 26 of 65
  closes below their opens; the volatile regime's 2.31–2.55 ending 5.49 below
  its start after a 105.73 high; the gap series' 0.86 above and 4.14 below.

## What it claims to teach but does not

- `account-risk-and-risk-budget` promises allocation across the trade and
  the week and had neither in the lab. Fixed as above.
- `losing-streaks-and-drawdown` promises that order alone changes drawdown
  and changed the outcomes too. Fixed as above.
- `gap-slippage-liquidity-and-execution-risk` names insufficient liquidity in
  its objective and had no depth in the lab. Fixed as above.
- `daily-and-weekly-risk-limits` promises a weekly limit that could not bind.
  Fixed as above.
- `correlation-concentration-and-portfolio-exposure` promises to show
  positions behaving like one oversized trade *as correlation rises*, and its
  arithmetic showed the reverse. Fixed as above.
- `trading-risk-plan` promises to "check contradictions" and passed the one
  its own predecessor lesson defines. Fixed as above.
- `risk-of-ruin`'s reading "Include rare losses larger than the planned
  stop" describes an input the lab does not have (every loss is exactly the
  average loss). Left, and recorded here: adding a fat-tail control is a
  larger change than this pass warrants, and the formula block now says in
  words that the simulation reshuffles an assumed distribution.

## Where a learner gets stuck

- **Lesson 02, the lab**: told that a trade fits by count, never shown one
  that does not fit by dollars. Fixed.
- **Lesson 05, "slippage"**: a term from six lessons ahead, used as a given.
  Fixed by definition in place.
- **Lesson 08, the Clustered tab**: the ending equity says clustering loses
  money. Fixed.
- **Lesson 10, the KPI**: the reader's division gives 211 and the page says
  212. Fixed.
- **Lesson 13, "beta"**: the number the lab multiplies by is never named on
  the page. Fixed in the formula block.
- **Lesson 14, a credit spread with the underlying falling**: the verdict
  says the market moved against it. Fixed.
- **Lesson 15, the Limit-ignored tab**: the rule cost 3.3R and the page has
  no other day to show. Fixed.

## Structural changes considered

None made. No lesson carries more than one hard idea; lesson 14's six
structures are six instances of one payoff-plus-obligation reading, and
lesson 11's three named risks are three ways a fill leaves the trigger. The
order is the dependency order the home states. No URL is added, removed or
renamed; the five declarations are untouched.

## Verification performed

- Every lab's arithmetic executed from the shipped script in a stub DOM,
  before and after, for every tab and every control position that changes a
  verdict: the fundamentals lab's four outcomes; the budget lab at the
  defaults and with the next trade, the week and the day each pushed past
  their limits; the losing-streak table at 1%–5% and 10 and 25 losses; the
  three stop placements; sizing at three multipliers; the R-multiple lab at
  three exits and a target below entry; the drawdown lab's three orders; the
  ruin simulation at 1%, 2% and 5%; ATR at four period/multiple pairs in
  both regimes; execution at nine order/gap/depth combinations; leverage at
  the margin-call boundary (−28% no deficit, −29% $150 short) and at 4×; the
  portfolio at four correlations; all six option structures in both
  directions; the limits lab in seven combinations of day type, enforcement
  and carried loss; the plan validator at the defaults and at the two
  contradictions the quiz names.
- 118,098 plan exports validated against the published schema: 0 invalid.
- Every quiz answer index checked against its choices after the rewrite;
  every distractor carries a `why`; no correct choice does; every worked
  answer recomputed by hand in this document.
- The sixteen shared scripts are byte-identical (one md5).
- The gates in AGENTS.md §7–8 and the CI steps run locally, listed in the
  commit message.
