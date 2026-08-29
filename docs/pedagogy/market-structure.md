# Pedagogy assessment — Market Structure (trading, course 1)

Re-assessment, formed from the seven lessons and the course home as they stand
on `main` at 8874d34, before the prior assessment was opened. The delta against
that document is the last section.

Course home: `site/market-structure/index.html`. Lessons, in course order:
`market-structure`, `ranges-breakouts-liquidity`,
`multi-timeframe-market-structure`, `pullbacks-entry-models`,
`invalidation-stops-risk-reward`, `volume-relative-strength`,
`options-contract-selection`. This is course 1 of the path, so it is judged as
the entry point: nothing before it may be assumed.

## What the course teaches well

- **Every lesson ends in an act, and the hero names it.** `market-structure`
  promises "label an unmarked chart ... and name the level that would prove the
  label wrong"; `ranges-breakouts-liquidity` promises "classify a finished
  sequence ... from its closes alone"; `invalidation-stops-risk-reward`
  promises "pick the stop that expresses a stated thesis, then size the
  position". These are observable objectives, not "understand X".
- **The worked example → faded guidance → independent practice arc is real in
  lessons 01, 02 and 04.** The structure explorer in `market-structure` walks
  swing by swing with a per-step description; the toggles (labels, path,
  levels) let a reader strip the scaffolding; the quiz draws the same
  structures unlabelled. `ranges-breakouts-liquidity` does the same with a
  candle-by-candle evidence checklist (cross / close / hold) whose status is
  step-aware, and a drill with labels hidden. `pullbacks-entry-models` shows
  all three entries on one chart with their numbers, then drills rule → model.
- **The "what this is normally read as" blocks are the course's best idea.**
  They separate the shape from its conventional reading, name the close that
  would break the reading, and are step-aware in the labs (a reading is never
  printed before the chart has earned it). They also keep the course honest
  about synthetic data: no block claims to know who transacted.
- **Named misconceptions are addressed, in the author's voice, at the point of
  error.** "A trend is not invalidated by one red candle" (01); "wick ≠
  confirmed break" (02); "'lower timeframe bearish' does not automatically mean
  'short'" (03); "a lower price is not a better entry after the structure that
  justified the trade has failed" (04); "a 3R target is not automatically
  superior to a 1.5R target" (05); "not RSI" and "compare volume to its own
  baseline" (06); "direction can be right and P/L still disappoint" (07).
- **Prerequisite order inside the course is sound at the level of ideas.**
  Swings and the protected level (01) → boundaries and closes (02) → the same
  reading at two scales (03) → entries placed on those pullbacks (04) → stops at
  those levels and sizing from the distance (05) → participation and leadership
  as secondary evidence (06) → expressing the plan in a contract (07). The
  course home's "How to work through it" states the dependencies correctly.
- The arithmetic that is computed live is right. The lesson 05 planner
  (`$125 = 0.5% × $25,000`, `31 units = ⌊125 / 4⌋`, `$248`, `2.00R`), the
  lesson 06 volume baselines and relative-strength returns, and the
  Black–Scholes core in lesson 07 all check out against independent
  recomputation.

## What it teaches badly, or claims and does not deliver

### Entry-point gaps (a beginner is told nothing is assumed, and two things are)

1. **Candle anatomy is never taught** (`market-structure`). The course home
   says "no prior technical analysis is assumed — lesson 01 starts from a bare
   candlestick chart", and the whole course keys on *close* versus *wick*
   (rule 2 of lesson 01, the entire premise of lesson 02). Nowhere is a reader
   told what a candle's body, wick, open and close are, or that "the close" is
   the price the rules use. The legend says "Bull candle / Bear candle" and
   stops. A reader who does not already know this cannot follow "a wick can be
   a sweep, not a break".
2. **"Liquidity" is never defined** (`ranges-breakouts-liquidity`). The lesson
   is titled for liquidity sweeps and uses the phrase eleven times; the word
   "liquidity" is never explained — why a sweep is called one (resting orders
   beyond an obvious level), or what "sweeping" them means. It is jargon the
   lesson leans on and does not supply.

### Objectives half-measured

3. `market-structure` promises the reader will "name the level that would
   prove the label wrong". The quiz only asks for the label; the level is
   revealed in feedback and never asked for.
4. `invalidation-stops-risk-reward` promises "then size the position from the
   distance that stop imposes". The calculator is a tool, not a drill: the
   reader never has to produce a size. The drill asks only which stop.
5. `volume-relative-strength` says "the drills at the end measure both" the
   volume judgement and the leadership judgement. There is one drill, and it
   is leadership only. The volume half — the lesson's headline idea, "compare
   a bar to its own baseline" — is never tested.
6. `multi-timeframe-market-structure` promises "read regime, location, and
   trigger from a pair of charts". The drill's prompts do the reading for the
   learner ("Higher timeframe: bullish. ... Lower timeframe: the selloff forms a
   higher low and breaks its last lower high"), so the two charts beside them
   are decorative and the drill measures vocabulary → decision, not reading.
7. `options-contract-selection`'s drill labels its own answers: each choice
   carries an evaluative tag — "balanced fit", "aligned", "less friction",
   "wrong direction", "too little time" — so the learner can answer without
   reading the constraints.

### Feedback that does not address the error

8. **Every drill in the course gives the same feedback for every wrong
   answer.** `market-structure` ("This chart is bullish." + the rule),
   `ranges-breakouts-liquidity`, `multi-timeframe-market-structure`,
   `pullbacks-entry-models`, `volume-relative-strength` and
   `options-contract-selection` all render "Not quite." + the explanation of
   the correct answer regardless of what was chosen. Only
   `invalidation-stops-risk-reward` mentions the distractors (A and C) — and it
   never addresses D, "no stop; wait for recovery", which is the most dangerous
   choice on the page. The predictable confusions (transition vs range in 01;
   sweep vs rejection in 02; "wait" vs "aligned" in 03; "no trade" vs a cheaper
   aggressive entry in 04) are exactly where the feedback should differ, and it
   does not.

### Factual defects in numbers a reader will trust

9. **Lesson 04's stops sit inside the wicks the chart draws**
   (`pullbacks-entry-models`). The candles are generated from authored closes
   with deterministic noise, and the stops were set without checking the
   wicks. Recomputed: healthy-bull confirmation stop 108.20 versus reaction
   wicks at 107.71 / 107.87; continuation stop 109.70 versus the shift
   candle's low 109.12; healthy-bear aggressive stop 114.70 versus a bounce
   wick at 114.76 on the very next candle; deep-bull aggressive stop 102.10
   versus the entry candle's own low of 101.91, and its confirmation stop
   102.40 above that same low. The lesson therefore shows stops that would be
   hit before or on entry, then quotes a reward-to-risk on them.
10. **Lesson 05's drill labels a protected low the chart goes beneath**
    (`invalidation-stops-risk-reward`). Candle 11's low is set to 98.45 and
    labelled "Protected low"; candle 12's generated low is 98.22. The drawn
    swing low is not the labelled one.
11. **Lesson 07's static readouts disagree with its own model**
    (`options-contract-selection`). For the default contract (100 call, 30
    DTE, IV 35, r 4%) the shipped model returns premium $4.16, delta 0.53,
    breakeven $104.16, $416 at risk; the page's HTML says $4.58 / 0.55 /
    $104.58 / $458. The exit-simulator statics ($9.12, +$454, +99.1%) should
    be $8.97, +$481, +115.7%. The quote-evaluator defaults (4.45 / 4.71) are
    derived from the wrong premium. Script overwrites all of these on load, so
    a scripted reader never sees them — but the page's own noscript note says
    the written panels still read normally, and the hero's illustrated chain
    (95 → 0.68 / $7.12, 100 → 0.55 / $4.36, 105 → 0.38 / $2.25) and the drill's
    "|Δ| 0.55" for the same contract are wrong by the same drift.
12. **Lesson 06's static readout is off by rounding**
    (`volume-relative-strength`): "2.1K" and "2.3×" where the script renders
    2.2K and 2.4× (2,240 against a 948 baseline).

### Order and load

13. **"R" is used one lesson before it is defined.** `pullbacks-entry-models`
    reports "2.55R" in its panel; `invalidation-stops-risk-reward` is where the
    R multiple is introduced. One gloss at first use fixes it.
14. **Lesson 07 is a leap in load** (`options-contract-selection`). It uses
    call, put, strike, expiration/DTE, premium, moneyness, delta, theta, vega,
    implied volatility and breakeven with one-line definitions for the first
    two and none for the rest, in a course that promises no prior technical
    knowledge. Course 3 of the path (`options-trading`) is where these are
    taught. The lesson is defensible as a capstone that expresses the plan of
    lesson 05, but as written it needs a terms card so a reader can follow its
    own table. This is a cross-course ordering note as much as a lesson defect.
15. **Lesson 03's hierarchy card describes three tiers and its lab shows two**
    (`multi-timeframe-market-structure`): regime (weekly/daily), location
    ("the intermediate chart"), trigger (lower). The lab and the drill use
    daily + 1-hour, reading location off the daily. A learner will look for
    the intermediate chart and not find it.
16. The rejection/sweep boundary in lesson 02 is a matter of degree the lesson
    does not state (`ranges-breakouts-liquidity`): the rejection scenario's
    wick crosses the high by 0.25, the sweep's by 2.35, and the concept cards
    say only "without materially trading through it". A learner has no rule
    for "materially". The framework card also contains an editing artefact
    ("The failed break of the concept card, completed").

### Course home

17. "What it teaches" is a list of topics, not of acts. The lesson cards use
    verbs (read, classify, combine, compare, plan, interpret, choose); the
    course-level statement should too.

## Where a learner gets stuck

- At lesson 01, rule 2 ("Require a close"), if they do not already know what a
  candle is (item 1).
- At lesson 02's drill, between "range rejection" and "liquidity sweep" (item
  16), with feedback that does not say what separates them (item 8).
- At lesson 03's drill, not at all — which is the problem (item 6).
- At lesson 04's lab, if they inspect the deep-bull chart's tooltips and find
  the entry candle already through the stop (item 9).
- At lesson 07's table, on "Theta / day" and "Vega / IV pt" (item 14).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed or renamed.

- `market-structure`: a candle-anatomy panel before the three structures
  (open, close, high, low, body, wick, and why the rules use the close); a
  one-line definition of a swing point; the quiz gains a second step that asks
  for the invalidating level, generated from the scenario's own anchors, and
  both steps give feedback specific to the wrong answer chosen.
- `ranges-breakouts-liquidity`: liquidity defined where the sweep is
  introduced; the degree rule for rejection versus sweep stated; the artefact
  sentence rewritten; per-wrong-answer feedback.
- `multi-timeframe-market-structure`: drill prompts now state only the
  location and ask the reader to read regime and trigger from the two charts;
  per-wrong-answer feedback; the hierarchy card reconciled with the two-panel
  lab.
- `pullbacks-entry-models`: every stop moved beyond the wick it claims to sit
  under, reward-to-risk recomputed (healthy bull 5.29R / 2.00R / 1.00R; deep
  bull 4.88R / 1.54R / 0.53R; healthy bear 3.71R / 1.85R / 1.00R), the
  continuation notes rewritten to say the invalidation does not move up with
  the entry; "R" glossed at first use; per-wrong-answer feedback.
- `invalidation-stops-risk-reward`: candle 12's low authored above the
  labelled protected low; the drill gains a sizing step (budget $125, stop B
  ⇒ 17 units, with distractors 56 / 8 / 3,472 that each name the error that
  produces them); choice D addressed.
- `volume-relative-strength`: a participation drill added (event bar against
  its own baseline, including the absolute-versus-relative trap); static
  readouts corrected; per-wrong-answer feedback in both drills.
- `options-contract-selection`: a terms card defining the vocabulary the table
  uses; every static number recomputed from the shipped model; evaluative tags
  removed from the drill choices; per-choice feedback.
- Course home: "What it teaches" rewritten as outcomes.

## Delta against the prior assessment

Written after the above, on reading `docs/pedagogy/prior/market-structure.md`.

**Its repairs are live and I do not dispute any of them.** The 98.45 level
line, the "Course 1 · Lesson NN of 07" straplines on 02–07, the "By the end"
objective in each hero, the "Part N" kickers in lesson 01, the baseline
definition in lesson 06, the lesson 07 blurb, and the converged sweep
definition are all present and all improvements. Several of the strengths I
list above (observable objectives in every hero; step-aware readings) exist
because of that pass. One repair was left half-done: the "A/C/B → 1/2/3"
relabel changed the concept-card icons in `pullbacks-entry-models` but not
the chart markers, which still print A, C and B in both the lab overlay and
the drill overlay. Finished here.

**What it claimed that I dispute.**

- "Spot-checks of the arithmetic hold … lesson 07's breakeven (100 strike +
  $4.58 premium = $104.58) [is] internally consistent." The static numbers are
  consistent with each other and inconsistent with the model the page ships:
  the shipped Black–Scholes returns $4.16 for that contract, so every static
  figure derived from $4.58 is wrong (item 11). The check verified the page
  against itself rather than against the code.
- "Nothing in the course depends on an idea the learner has not met." Candle
  anatomy (item 1), "liquidity" (item 2), the R multiple one lesson early
  (item 13) and the Greeks in lesson 07 (item 14, which the prior does
  acknowledge as a load cliff) are all used before they are supplied.
- "Every lesson has the worked-example → practice arc." The arc exists, but in
  lessons 03, 05 and 06 the practice does not measure the objective the hero
  states (items 4–6), and in 07 the drill answers itself (item 7).
- Its own headline fix — the lesson 05 drill chart — was verified for the
  level line and not for the candles: candle 12 is still drawn beneath the
  level the fix moved (item 10).

**What it missed entirely.** Stops inside drawn wicks throughout lesson 04
(item 9); the lesson 07 static drift (item 11); the lesson 06 rounding (item
12); generic wrong-answer feedback in every drill (item 8); the giveaway
prompts in lesson 03 and giveaway tags in lesson 07 (items 6, 7); the missing
volume drill (item 5) and sizing step (item 4); the undefined terms (items 1,
2). It also missed that lesson 06's fourth leadership item punishes the
learner for doing what the lesson teaches: "$42 → $45 versus 5,100 → 5,250" is
answerable by normalising (+7.1% against +2.9%, the asset led), yet the key
is "cannot compare". Rewritten so the starting prices really are absent.

**Its cross-course note stands.** Whether an option is the right expression
at all, versus the linear instrument of lesson 05, is not taught here and is
scope for course 3 (`options-trading`). The terms card added to lesson 07 is a
bridge, not a substitute; the path-level fix is that course 3 exists.
