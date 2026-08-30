# Pedagogy assessment — Technical Indicators (trading, course 4)

First-pass assessment, formed from the sixteen lessons, the course home and
the published schema as they stand on `main` at 2d7e226. There is no prior
assessment of this course, so there is no delta section.

Course home: `site/technical-indicators/index.html`. Lessons, in course order:
`technical-indicator-fundamentals`, `moving-averages`,
`moving-average-crossovers`, `relative-strength-index`,
`stochastic-oscillator`, `macd`, `average-directional-index`,
`average-true-range`, `bollinger-bands`, `keltner-channels`,
`donchian-channels`, `rate-of-change-and-momentum`, `indicator-divergence`,
`combining-indicators`, `indicator-selection-by-market-regime`,
`indicator-based-trading-rules`. The published asset
`indicator-rule-schema.json` is the export shape lesson 16 claims.

Courses 1–3 are the declared predecessors and the home is explicit that this
course loads nothing from them. What it does assume from them is vocabulary:
"structure", "location", "invalidation" and "setup" appear in the process
cards of nearly every lesson as the thing an indicator observation must be
combined with, and they are course 1 and 2 words (`market-structure`,
`trade-setup-execution`). That is a fair assumption in position 4 and the
course never leans on an options concept, so the prerequisite chain across
the path holds.

Every lesson ships one shared JavaScript prelude — byte-identical on all
sixteen pages, checked by diff — holding the synthetic series generator, the
indicator arithmetic (`sma`, `ema`, `wilder`, `stddev`, `rsi`, `trueRange`,
`atr`, `stochastic`, `macd`, `adx`, `bollinger`, `keltner`, `donchian`, `roc`,
`momentum`), the chart drawers and the quiz engine — then its own lab and
drill. Unlike course 3, no readout is hand-written into the static HTML: every
figure is "—" until script fills it, so there is no static/live disagreement
to find. What can be wrong here is the arithmetic, the labs' verdicts, and
whether a drill measures what its lesson promised.

## What the course teaches well

- **The order is the order the ideas depend on, and the home says why.**
  Transformation, lookback and warm-up (01) → the two averages (02) → the
  trend-state model built on them (03) → three momentum oscillators and the
  directional-movement family (04–07) → true range and the three envelopes
  that consume a volatility estimate (08–11) → the reading skills (12–16).
  "How to work through it" names real dependencies — the smoothing in 02 is
  what every later envelope is built on, 13 needs 04–06, 16 asks for the
  filters 03, 07 and 08–11 compute — and each is true of the pages.
- **Every calculation lesson makes the reader watch the formula produce the
  number.** `technical-indicator-fundamentals` prints the window, the sum
  and the division for the selected bar; `average-true-range` prints all
  three true-range components and names the one that controls the bar;
  `rate-of-change-and-momentum` prints both prices in the comparison. This
  is the worked example the course's completion standards ask for
  ("reconstruct one value from its source data").
- **The arithmetic is the standard arithmetic and the calculation notes say
  which convention was chosen.** EMA seeded from the first complete SMA with
  α = 2/(p+1); Wilder smoothing for RSI, ATR and ADX; population standard
  deviation for Bollinger; %K raw → SMA → SMA for the stochastic; a prior
  completed channel for the Donchian signal. Each note also says that
  platforms differ, which is the one thing a reader comparing values against
  a charting package most needs to hear.
- **The labs are honest about what they cannot show.** The rule simulator
  (16) has no P/L and says so in three places; the export carries
  `performanceEvaluated: false`; the regime challenge (15) says its intended
  answers are for synthetic teaching paths; the combining lab (14) says its
  correlation is descriptive of one sample. "What this is normally read as"
  blocks are keyed to the scenario, never to an indicator value, and assert
  no order flow.
- **The misconceptions are the right ones and are named in the author's
  voice**: "calling EMA leading and SMA lagging" (02); "counting every bar
  above as a crossover" (03); "shorting every RSI reading above 70" (04);
  "confusing stochastic with price velocity" (05); "calling the histogram
  volume" (06); "calling high ADX bullish" (07); "reading rising ATR as
  bullish" (08); "assuming a squeeze predicts direction" (09); "calling a
  channel touch a confirmed breakout" (10); "using the current high to test
  itself" (11); "stacking RSI, stochastic, and ROC as three votes" (14);
  "writing subjective conditions" (16). Each is corrected in a sentence.
- **The divergence exercise is a genuine classification drill** — classify
  before revealing, then the anchors are drawn — and its answers are right.
  Executed from the shipped prelude: `bullDiv` gives price 94.25 → 90.55
  (lower) with RSI 5.04 → 12.61 and MACD histogram −0.53 → −0.33 (both
  higher); `bearDiv` gives 115.81 → 119.45 with RSI 94.88 → 87.60 and
  histogram 0.53 → 0.31 (both lower); `noDiv` gives 105.29 → 97.21 with RSI
  15.12 → 10.24 and histogram −0.19 → −0.61 (both lower, agreeing with price).
  The expected answer is keyed to the scenario label rather than to the
  computed relationship, so this had to be checked; it holds for both
  oscillators.
- **Lesson 16's export matches its schema field for field** (`schema`,
  `course`, `generatedAt`, `data{4}`, `rule{8, parameters{7}}`,
  `diagnostics{7}` with `performanceEvaluated` const false), and the home's
  interop section describes exactly that shape.

## What the course teaches badly

### The combining lab marks the lesson's own recommended set wrong

`combining-indicators` opens with EMA 20, RSI 14 and ATR % selected — a trend
reference, a bounded momentum measure and a volatility measure, three
distinct jobs, which is precisely the set the copy tells the reader to build.
The lab scores it 56/100, "Reduce or rebalance", and reports "1 pair is
highly correlated in this sample". The pair is EMA 20 / ATR %, correlation
−0.94 in the uptrend sample (−0.90 in the breakout sample, −0.66 in the
volatile one). Nothing about those two outputs is redundant: the EMA is a
price-level series, so its normalized curve is the price path, and ATR % is
a ratio to price, so in any trending sample the two are correlated by the
trend and by nothing else. Meanwhile the lesson's headline bad set — RSI,
stochastic and ROC as three votes — is caught correctly (0.93, 0.89, 0.91 in
the same sample). The fix is to say what is true: the EMA is drawn for
reference and left out of the correlation comparison because it is price,
not a transform of price on a comparable scale. Replacing it with a
comparable transform does not work — distance of close from the EMA
correlates 0.96–0.98 with RSI in every scenario, because that distance *is*
a momentum measure — and correlating bar-to-bar changes instead loses the
RSI/stochastic/ROC redundancy the lesson exists to show (0.67, 0.67, 0.54).

Two further gaps in the same lab. The status says "Purpose gap: the set is
missing at least one intended functional family" without naming the family
or the tool that would supply it, so the feedback restates the rule rather
than addressing the specific error. And the score never penalises two tools
in the same family unless their sample correlation happens to exceed 0.85 —
the lesson's own thesis ("one primary tool per job") is not what the score
measures.

### The regime challenge scores the classification but never says whether it was right

`indicator-selection-by-market-regime` computes `regimeOK` and awards 60 of
the 100 points for it, then reports "Persistent uptrend · 73/100" with the
suggested tools and the reader's selection. A reader who chose "range" for
the uptrend is left to infer from the label that the classification was the
part they got wrong; a reader who chose correctly but picked four extra
tools is not told that the extras cost them. The feedback should name the
intended regime, say whether the reader's matched, and list the picks that
were outside the suggested set.

### The ADX lab draws a value the formula does not produce

`average-directional-index`: the shared `adx()` seeds the smoothed true range
from bar 0 and the smoothed directional movement from bar 1, so at index
p−1 the smoothed TR exists and the smoothed DM does not; the code then
computes `100 * null / TR` = 0 and plots +DI = −DI = 0 at bar 14 before the
real values begin at bar 15 (checked by execution: `plusDI[13] = 0`,
`plusDI[14] = 19.45`). The DX at that bar is correctly null, so ADX is
unaffected, but the two DI lines start with a spurious zero and a vertical
jump. The same lab's status says ADX "is strengthening" for any positive
five-bar change while the readout beside it says "Flat" for anything inside
±0.5, so the two disagree for small slopes.

### Prerequisite order inside the course: true range is used one lesson before it is defined

`average-directional-index` (07) says +DI and −DI are "relative to true
range" and its process step is "Normalize with true range"; true range is
defined in `average-true-range` (08). Both are Wilder's and the dependency
is one line, so the fix chosen is to define the term where it is first used
and point forward, not to reorder. Reordering was considered: it changes no
URL, but it renumbers four lessons' eyebrows, breadcrumbs and prev/next
links and the home's stage grouping for a dependency that a clause resolves.
Rejected.

Likewise `bollinger-bands` (09) asks the reader to "compute rolling standard
deviation" without ever saying what that is. One clause in the process card.

### Drills that do not test what the lesson promised

The completion standards are observable acts — "reconstruct one value from
its source data" (01), "reconstruct %K from the recent range" (05),
"calculate and name every component" (06), "identify the true-range
component that controls the bar" (08), "explain width and %B as separate
outputs" (09), "reproduce the full channel" (10), "name both prices in the
calculation" (12) — and the labs let the reader do each of them. The drills
do not: no quiz in the course asks the reader to compute anything. Every
calculation lesson needs one question whose answer is a number the formula
produces. The added questions, with the arithmetic:

| lesson | question | answer |
| --- | --- | --- |
| 01 | closes 10, 12, 14, 16, 18 — SMA(5) | 70 ÷ 5 = **14** |
| 02 | EMA smoothing factor for period 9 | 2 ÷ (9 + 1) = **0.20** |
| 04 | average gain 2.0, average loss 1.0 | RS = 2; 100 − 100 ÷ 3 = **66.7** |
| 05 | lowest low 100, highest high 110, close 108 | 100 × 8 ÷ 10 = **80** |
| 06 | fast EMA 101.5, slow EMA 100.0, signal 1.0 | MACD **1.5**, histogram **0.5** |
| 07 | +DI 30, −DI 10 | DX = 100 × 20 ÷ 40 = **50** |
| 08 | previous close 100, bar high 103, low 101 | max(2, 3, 1) = **3** |
| 09 | basis 100, σ 2, multiplier 2, close 102 | bands 96/104; %B = 6 ÷ 8 = **75** |
| 10 | EMA 50.00, ATR 1.50, multiplier 2.0 | upper **53.00**, lower **47.00** |
| 11 | channel includes the current bar — can a close exceed the upper? | **never**: close ≤ high ≤ upper |
| 12 | price 50.00 → 52.00 | ROC **4%**, momentum **2.00** |
| 16 | why `performanceEvaluated` is false in every export | the lab computes no returns |

Every distractor in the course shares one explanation with the right answer,
so a reader who picked "the EMA uses fewer bars" and one who picked "it uses
future prices" are told the same thing. The shared quiz engine on course 3
already accepts a `why` per choice; this course's engine is the older one
that does not. The engine is upgraded on all sixteen pages and every
distractor gets its own sentence. The filler distractors that no reader
would choose ("Option assignment", "The chart background color", "Volume
becomes negative") are replaced with the misconception the lesson names.

### Objectives written as "understand"

The heroes of `technical-indicator-fundamentals` ("Learn how…"),
`moving-averages`, `stochastic-oscillator`, `macd`, `donchian-channels` and
`indicator-selection-by-market-regime` each end in "understand why…". The
completion standards on the same pages already name the act, so the heroes
are rewritten to name it too, and the course home's cards and the manifest
the home calls authoritative are changed in step.

### Copy errors a reader would trust

- `donchian-channels` calculation note: "displays either a channel including
  the current bar or one through the current bar" — the second is "through
  the previous bar". The common-mistakes card says including the current bar
  "can move the upper channel to the same new high"; the sharper fact is
  that it always does — a close cannot exceed a channel that contains its
  own bar's high — so a breakout rule written against it never fires.
- Course home, stage 3: "Four bounded readings of the same bars" — MACD is
  unbounded. Reworded.
- `relative-strength-index`: the readouts "Upper bars" and "Lower bars" count
  every bar at or beyond the threshold in the sample, while the process card
  asks the reader to "count how long RSI remains above or below a
  threshold" — a run length. The readouts are relabelled and the longest
  run is reported.
- `relative-strength-index`: the lower threshold is silently clamped to ten
  below the upper, and the slider is left showing the value the reader set.
  The slider now follows the clamp, as `moving-average-crossovers` already
  does for its periods.
- `average-true-range` is the one lab in the course whose scenarios carry no
  "What this is normally read as" block. The uptrend and high-volatility
  readings exist on other pages; the gap and low-volatility scenarios are
  written here.
- `indicator-based-trading-rules`: a rule that produces no entries in the
  sample is reported as "0 entry events and 0 exits were generated" with the
  same framing as one that fires. A rule whose filters and trigger never
  coincide is deterministic and useless, and the reader should be told which
  question that raises.

## What it claims to teach but does not

- `moving-average-crossovers` promises to "measure whipsaws" and the lab
  counts them as opposite crosses within eight bars, stated in the status
  line. The completion standard's "count rapid reversals" is therefore
  testable, and the drill now asks it.
- `combining-indicators` promises "compare normalized outputs and
  correlations" — it does, but see above for what it compares.
- Nothing else claimed is missing. The course is unusually careful about
  scope: it says in three places that performance belongs to courses 6 and 7.

## Where a learner gets stuck

- **Lesson 07 before lesson 08**: "true range" appears as a given. Fixed by
  definition in place.
- **Lesson 09**: "standard deviation" as a given. Fixed by definition in
  place.
- **Lesson 14's default state**: the reader builds the recommended set and
  is told to reduce it. Fixed as above.
- **Lesson 15's feedback**: the reader cannot tell which half of the answer
  was wrong. Fixed as above.

## Structural changes considered

None made. No lesson is carrying more than one hard idea; the two-lesson
pairs that could be merged (09/10, the two envelopes; 02/03, the averages
and the crossover) are each better as two because the second lesson's lab is
a different exercise. Reordering 07 and 08 was considered and rejected for
the reason given above. No URL is added, removed or renamed; the five
declarations are untouched.

## Verification performed

- Every lab's arithmetic executed from the shipped prelude in Node: the
  divergence anchors under both oscillators (six relationships, all as
  labelled); the DI seed artifact (`plusDI[13] = 0`); the correlation matrix
  for all nine outputs in all four scenarios, on levels and on differences.
- Every quiz answer index re-checked against its choices after the rewrite;
  every choice carries a `why`; no two choices on a question are identical.
- A stub-DOM harness that loads every page's script, drives every control
  through its range, every scenario, every classification, every regime
  case and every quiz choice, and asserts the lab verdicts named in this
  document (the default combining set is not flagged; the three-vote set
  is; the regime feedback names the intended regime; the export validates
  against the published schema for every trigger, exit and direction).
- The gates in AGENTS.md §7–8 and the CI steps run locally, listed in the
  commit message.
