# Pedagogy assessment — Trade Setup and Execution (trading, course 2)

First-pass assessment, formed from the fifteen lessons and the course home as
they stand on `main` at 04b1814. There is no prior assessment of this course,
so there is no delta section.

Course home: `site/trade-setup-execution/index.html`. Lessons, in course order:
`trade-thesis`, `support-resistance`, `confluence`, `breakout-setups`,
`pullback-setups`, `reversal-setups`, `entry-confirmation`,
`stop-loss-placement`, `profit-targets`, `risk-to-reward`, `position-sizing`,
`trade-management`, `backtesting`, `trading-journal`, `performance-review`.
Course 1 (`market-structure`) is the declared prerequisite and is assumed
here: swings, protected levels, breaks of structure, closes versus wicks,
"R", and the three entry models are not re-taught and should not be.

Every lesson page ships one shared JavaScript prelude (chart drawer, quiz
engine, helpers) and then its own scenario data, readings and drill. The
scenario data is where most of what follows was found, because that is where
the numbers a reader will trust actually live.

## What the course teaches well

- **The order is the order you would do it in, and the home page says why.**
  Plan (01–03) → recognise (04–06) → execute (07–09) → size and manage
  (10–12) → test, record, review (13–15). "How to work through it" states the
  real dependencies — the entry (07) needs a named setup, sizing (11) needs the
  stop distance from 08, the review (15) has nothing to read until 14 has
  written something — and they are true.
- **Reveal-gated labs where hindsight is the enemy.** `breakout-setups`,
  `reversal-setups` and `trade-management` hide the future candles and make the
  reader commit at the current one. In `trade-management` the discipline score
  is kept separate from the R result, which is exactly the lesson's point, and
  the shakeout tab lets a reader who moves to break-even early get stopped at
  0R on the next dip — the misconception is *experienced*, not described.
- **The "what this is normally read as" blocks** are step-aware wherever the
  chart is reveal-gated (`breakout-setups`, `reversal-setups`,
  `trade-management`), so a reading is never printed before the candles have
  earned it, and each one names the close that would end it.
- **Named misconceptions at the point of error.** "Bias presented as a trade
  plan" and "invalidation selected from desired dollar loss" (01); "a wick is
  not a confirmed breakout" (02, 04); "counting correlated indicators
  separately" (03); "redefining a failed breakout as a pullback" (04);
  "calling structural failure a deeper pullback" (05); "one big candle is not
  a reversal" (06); "changing from retest to breakout after a missed trade"
  (07); "sizing first and forcing the stop to fit" (08); "inventing a target
  to reach a preferred R" (09); "treating 2R as a universal minimum" and
  "assuming planned R equals realised average win" (10); "using buying power
  as position size" (11); "moving to break-even too early" (12); "selecting
  only obvious winners" (13); "writing the thesis after the outcome" (14);
  "changing many variables after one review" (15). The list is good and the
  wording is the author's.
- **The arithmetic that is computed live is right**, with one exception noted
  below. The sizing calculator (`$200 = 1% × $20,000`; `97 = ⌊200 / 2.05⌋`;
  `$198.85`; one contract at `$102` under a premium stop and zero under full
  premium), the target R-multiples (long trend 1.46R / 2.81R; short breakdown
  1.23R / 2.58R; range long 2.45R / 2.77R), the expectancy presets (+0.30R,
  −0.02R, +0.21R), the backtest profit factor, drawdown and streak, and the
  journal aggregates (sample net +8.80R, 75.0% adherence, 3.5 / 5) all check
  out against independent recomputation.
- **Lessons 14 and 15 are one workflow with a published contract**
  (`trade-journal-schema.json`), and the course home explains the hand-off in
  plain language. The review's "improvement rule" output is a measurable
  sentence with a sample size attached — the course ends in an act.

## What it teaches badly, or claims and does not deliver

### Charts that contradict their own readings (numbers a reader will trust)

1. **`reversal-setups`: the change of character never happens on the chart.**
   On the bottom tab the "countertrend structure" line is drawn at 104.0 and
   the step-4 reading says "the close at 104.2 is the first above the 104.0
   lower high". The closes are 104.1 (a *low*) and 105.0 (the actual last
   lower high, candle 9). 104.2 does not break 105.0; the first close that
   does is 106.3 at candle 18, which the lesson calls "continuation". The top
   tab mirrors it: the line sits at 108.0 and the reading calls 107.9 "the
   first below the 108.0 higher low", but the last higher low is 106.9 (candle
   9) and 107.9 is above it. A reader who hovers the candles — which the
   tooltip invites — finds that the lesson's central claim is false on its own
   data. The failed tab has the same 104.0-versus-105.0 mismatch.
2. **`reversal-setups`: the failed tab demands "no reversal" at the step its
   own reading calls indistinguishable.** `reversalExpected` returns
   `noTrade` from step 3 on the failed tab, while the step-3 reading says "so
   far this is indistinguishable from the bottom-reversal tab" — where the
   expected answer at step 3 is "wait". The reader is marked wrong for
   agreeing with the reading.
3. **`reversal-setups`: the evidence timeline runs one step ahead of the
   chart** (the code comment says so). At step 3 the panel shows
   "Countertrend structure break — Evidence is visible" while the reading on
   the same screen says "the 104.0 structure level is untouched".
4. **`support-resistance`: the drill scores against levels the candles do not
   support**, and the code comment admits it ("110.2 has no prior reaction in
   the series … 96.5 is the final close and is never tested twice. A reading
   of either would be invented"). On the role-reversal tab the reference
   support is 104.8 — the pullback low — while the lesson is teaching that the
   old 102.8–103.4 cap becomes support; a reader who places the zone on the
   old cap, i.e. does what the lesson says, is 1.7 points off and told to
   "recheck the strongest reactions".
5. **`risk-to-reward`: the break-even win rate ignores the average-loss
   input.** The page computes `1 / (1 + ratio)`, which is only correct when
   the average loss is 1R. Set the average loss to 0.5R with a 2R target and
   the page shows 33.3%; the break-even rate is 20.0%
   (`avgLoss / (avgWin + avgLoss)`). The formula card states the same
   special case as if it were the rule. This is the one live number in the
   course that is wrong.
6. **`entry-confirmation`: "closes at 110.8, back above the whole three-bar
   pullback"** — the pullback closes are 110.8, 109.2, 108.3. Candle B's close
   equals the first of them; it is not above it.
7. **`trade-thesis`: the reading and the evaluator disagree about the
   invalidation.** The bull-pullback reading says "the reading fails if price
   closes back under 108.1", the plan expects 107.0 with a tolerance of 0.9,
   so a reader who types the number the reading gave them is marked wrong.
8. **`breakout-setups`: the failed tab labels a close of 107.3 above a 106.2
   boundary "Trades above"**, on the lesson whose whole point is close versus
   wick.

### Drills that contradict the lesson's own rule

9. **`entry-confirmation`: the failed tab uses hindsight to score the
   reaction model.** The process card says "the first candle that satisfies
   the written model is the candidate — not the candle that later looks best".
   Candle A on the failed tab (108.4, a close up off the 107.3 area) is a
   reaction close by the pullback tab's own definition; a reaction-close rule
   fires there and is stopped out. The lesson scores "no valid entry" as
   correct for that model — which is only knowable from the candles that come
   after A. The honest answer is A, followed by the loss, which is the "more
   false starts" the trade-off table promises.
10. **`breakout-setups`: the acceptance rule changes between tabs.** On the
    confirmed tab, the close after the break (109.1, beyond the 107.8 break
    close) is acceptance and "enter" is expected the next candle. On the
    retest tab the close after the break is 108.8, beyond the 107.4 break
    close, and the expected answer stays "wait" for three more candles. A
    reader who applies tab 1's rule on tab 2 is told "the visible candles have
    not completed the breakout model" without being told why the same
    evidence no longer counts.
11. **`confluence`: the lab says "select only evidence visible in the
    scenario" and then penalises the reader for obeying.** The pullback tab's
    relevant set includes relative strength; nothing on the chart shows a
    benchmark. The breakout tab's includes relative strength and volume; the
    reading itself says "no volume is plotted here". Choosing exactly what is
    visible on the pullback tab scores 75% and fails with "Missing: Relative
    strength / weakness".
12. **`profit-targets`: the drill is pre-answered.** Both target sliders
    initialise on the reference objectives, so "Evaluate targets" passes
    without the reader touching anything. Nothing is retrieved.

### Objectives half-measured, or vocabulary used before it is taught

13. **The "Completion standard" is the same sentence on all fifteen pages**
    ("explain the rule before the chart resolves … decision, invalidation and
    risk remain consistent without using hindsight"). On `risk-to-reward`,
    `position-sizing`, `backtesting`, `trading-journal` and
    `performance-review` no chart resolves and nothing is decided under
    hindsight. The course-level objectives are observable; the lesson-level
    closing standard names no act. The lab section header is likewise
    identical on all fifteen ("evaluate the decision before revealing the
    answer") and false on the same five.
14. **`stop-loss-placement` uses "ATR" — as a readout and as the "too wide"
    threshold — and ATR is defined nowhere on the path.** Course 1 does not
    mention it either. The width rule (`buffer > 2.2 × ATR`) is applied to the
    reader's stop and never stated.
15. **`pullback-setups` asks the reader to toggle "Reaction candle" and
    "Local structure shift" without saying what either looks like.**
    `entry-confirmation`, two lessons later, is where the models are compared;
    it names them but does not define them operationally either. Course 1's
    entry-models lesson is the real source, and neither page points at it.
16. **`profit-targets` measures in R before `risk-to-reward` defines "R as a
    unit."** Course 1 glosses R, so a reader in order has met it, but the
    lesson that leans on it hardest gives no reminder.
17. **`trade-thesis` says "complete the plan without using the future
    candles" and shows every candle.** On the bearish-breakout tab price has
    already fallen to 96.8 against a 96.0 target when the reader is asked to
    plan the trade. Lessons 04, 06 and 12 hide the future; lesson 01, the one
    about not using hindsight, does not.
18. **`trade-thesis` has no worked example.** The reader is asked to build a
    thesis on the first tab with the expected components revealed only in the
    failure message. There is no complete thesis shown anywhere on the page
    to imitate.
19. **`risk-to-reward` has no worked example either.** The balanced preset is
    the example, but none of its arithmetic is shown; the formula card and
    the readout are the only bridge and the reader has to build it.
20. **`position-sizing` lists "check concentration and liquidity" as step 4
    and surfaces neither.** The default position is 97 shares at $100 —
    $9,700, 48.5% of a $20,000 account — and the page reports only that the
    risk budget is respected.
21. **`backtesting` silently moves the win rate.** The generator adds a
    setup-by-regime adjustment of up to ±0.08 to the "base win rate", so the
    realised win rate drifts from the input for a reason the page never
    gives. A reader checking the statistics against the inputs — which the
    lesson asks them to do — cannot reconcile them.

### Feedback that does not address the error

22. **Every drill on every page gives the same sentence for every wrong
    answer.** The shared `setupQuiz` engine renders `q.explanation`
    regardless of which distractor was chosen. The distractors are good —
    "widen the stop", "average down", "rename it a pullback", "double the
    risk budget" — and each names a specific misconception; none of them gets
    an answer. Course 1 fixed this in its pass; course 2 has the same gap.
23. **`trade-thesis` reveals the answer key on failure** ("Expected long,
    pullback, and closeAbove. Invalidation is near 107.0 …") rather than
    naming which component was wrong and why.

### Order, load and the course home

24. **`reversal-setups` and `stop-loss-placement` define a reversal's
    invalidation differently.** Lesson 06's concept card says the retest's
    opposite-side swing "provides … a usable invalidation point", its step-4
    reading says "a close back below 99.4 [the sweep low] would end the
    reading", and lesson 08 puts the line at 102.7 "the close the break
    started from" — neither the swing nor the low. One course, three
    definitions.
25. The course home's "What it teaches" is a table of contents, not a list
    of things the reader will be able to do.
26. Cognitive load is acceptable throughout: no lesson introduces more than
    one new hard idea, and the heaviest pages (`trading-journal`,
    `performance-review`) are applications rather than concepts. No split or
    merge is warranted, and the URL space should not change.

## Where a learner gets stuck

- **On `reversal-setups`, step 4, trying to see the break.** Told that 104.2
  breaks the lower high, they look for a lower high at 104.0 and find a low
  there and a high at 105.0. The honest conclusion — "the lesson is wrong" —
  is the one they reach, and it discredits the readings elsewhere that are
  right.
- **On `support-resistance`, role-reversal tab.** They put support on the
  old cap because that is the lesson, are told to recheck, press "Reveal
  reference", and see the reference sitting on a single pullback low above
  it. The lesson has just taught them that a single reaction is weak
  evidence.
- **On `confluence`, pullback tab**, choosing what they can see and scoring
  75%.
- **On `breakout-setups`, retest tab, candle 13**, applying the rule they
  learned on the previous tab and being told to wait.
- **On `stop-loss-placement`**, being told the stop is "too wide" against
  "the reference volatility buffer" with no way to know what the buffer is.
- **On `risk-to-reward`**, changing the average loss and watching the
  break-even rate not move.

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, split, merged or
renamed, so the five URL declarations are untouched.

- **Shared quiz engine (all fifteen pages, one identical edit):** a choice may
  carry a `why`; when a wrong answer is chosen its own `why` is shown, falling
  back to the question's explanation. Every drill on every page now has a
  `why` on every distractor, written against the misconception that
  distractor names.
- **Completion standard and lab header, all fifteen pages:** each lesson's
  closing card now names the act its drill measures; the five non-chart
  lessons' lab headers say what the lab actually is.
- `trade-thesis`: future candles hidden past the decision candle on the two
  directional tabs, with a "show what happened next" control and readings
  written against the visible candles; a worked thesis for the bull-pullback
  tab, every line justified; the reading's invalidation sentence reconciled
  with the evaluator (108.1 is the low; 107.0 is the line under it with room
  for a wick); the failure message names the components that were wrong.
- `support-resistance`: the role-reversal and downtrend series re-authored so
  both reference zones are evidenced by two reactions each (role reversal:
  support 103.3 on the old 102.8–103.4 cap retested at 103.6, resistance 107.0
  from 107.2 / 106.9; downtrend: resistance 101.6 from 101.8 / 101.5, support
  97.7 from 97.8 / 97.6), readings rewritten to match, the "invented level"
  comment removed because it is no longer true.
- `confluence`: relevant evidence limited to what each tab shows or states
  (pullback: structure, location, trigger; breakout: location, trigger, and
  the stated volume premise); the instruction reads "shown or stated"; and a
  correct set plus an unsupported claim no longer passes silently at 88% —
  the verdict names the claim and asks for it to be dropped.
- `breakout-setups`: the acceptance rule stated in the checklist (a later
  close beyond the break candle's close, or a retest that holds and closes
  away); the retest tab's post-break closes re-authored to hug the boundary
  (106.3, 106.9, 106.4) so "wait" is honest and consistent with the confirmed
  tab; "Trades above" corrected to "Closes above"; the limited-room verdict
  now gives the room in points and the best R it allows.
- `pullback-setups`: reaction candle and local structure shift defined beside
  the controls, with a pointer to lesson 07 and course 1; "closed at or
  through" at 100% depth.
- `reversal-setups`: the three series re-authored so the drawn structure
  level is the actual last lower high / higher low (bottom: candles 8–9 now
  103.2 / 104.0; top: 108.9 / 108.2 with the line at 108.2; failed: 103.3 /
  104.0); the evidence timeline relabelled to match what is on screen at each
  step; the failed tab expects "wait" at step 3 and "no reversal" from step
  4; the invalidation named consistently as the opposite-side swing (103.1 /
  109.0).
- `entry-confirmation`: the three models defined operationally in the side
  panel; candle B re-authored to 111.0 so it is above the pullback; the failed
  tab's reaction model answers "A", with feedback that names the false start
  as the model's cost.
- `stop-loss-placement`: ATR defined and the width rule stated; the reversal
  reading reconciled with lesson 06 (the 103.4 higher low is the swing the
  line sits under); the breakout reading's "closes down through 101.5"
  corrected.
- `profit-targets`: sliders initialise at the invented 2R and 3R prices, so
  the reader must move them to structure, and the verdict reports the first
  obstacle's R; R glossed at first use; the scale-percentage input disabled
  while "single target" is active.
- `risk-to-reward`: break-even computed as `avgLoss / (avgWin + avgLoss)` and
  the formula card corrected; a worked card for the balanced preset; the
  readout says the average win is the planned target.
- `position-sizing`: the verdict reports notional as a share of equity.
- `trade-management`: the plan text says reduce first, then trail.
- `backtesting`: the regime adjustment disclosed beside the inputs.
- `trading-journal`: an independent-practice prompt — journal the trade
  managed in lesson 12 as the first real entry.
- Course home: "What it teaches" rewritten as outcomes.
