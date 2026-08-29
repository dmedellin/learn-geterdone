# Pedagogical assessment — Course 1, Market Structure

Assessed against every published page of the course: the course home
(`/market-structure/`) and the seven lessons
(`market-structure`, `ranges-breakouts-liquidity`,
`multi-timeframe-market-structure`, `pullbacks-entry-models`,
`invalidation-stops-risk-reward`, `volume-relative-strength`,
`options-contract-selection`), read in full before any change was made.

## What the course teaches well

**The prerequisite spine is real, and it is stated.** The course home says
"entries (04) are placed on the pullbacks defined in 01–03, stops (05) are
placed at the structural levels those lessons named, and contract selection
(07) prices the plan built in 05" — and the lessons actually honour that.
`pullbacks-entry-models` builds its comparator on the protected-low vocabulary
from `market-structure`; `invalidation-stops-risk-reward` sizes positions from
the structural stop that lesson 04's confirmation model produced; the option
lab's "define the chart invalidation first" step points straight back at 01
and 05. Nothing in the course depends on an idea the learner has not met, and
since this is course 1 of the path there is no earlier course to violate.

**Every lesson has the worked-example → practice arc.** Each page runs the
same progression: concept cards, then an interactive lab that *is* the worked
example (the scenario tabs are faded worked examples — same mechanism, new
data), then a scored drill (`Score 0 / 0`, streak tracking) that forces
retrieval without labels. `ranges-breakouts-liquidity` is the model of the
form: the boundary reader plays candle-by-candle with closes marked, the
decision framework names the four classifications, and the drill then hides
the labels and asks for the classification cold.

**Misconception handling is unusually explicit for this genre.** The course
names the predictable wrong models rather than talking around them:

- "A trend is not invalidated by one red candle" (`market-structure`);
- "A wick can be a sweep, not a break" (`market-structure` working rules, and
  the entire premise of `ranges-breakouts-liquidity`);
- "'Lower timeframe bearish' does not automatically mean 'short'"
  (`multi-timeframe-market-structure`, in a highlighted callout);
- "Buying because price 'looks cheap'" and "waiting for so much proof that
  location disappears" (`pullbacks-entry-models`, common-mistakes list);
- stop A/B/C — a stop can be too tight *and* "structurally unnecessary as
  well as too tight" (`invalidation-stops-risk-reward`);
- "This is not the RSI momentum indicator", twice
  (`volume-relative-strength`);
- "Why direction can be right and P/L still disappoint"
  (`options-contract-selection`).

**The epistemics are honest.** The recurring "What this is normally read as"
panels frame every reading as convention plus a falsifier ("A close below 108
breaks that reading"), never as prediction. Lesson 05's "R describes payoff
geometry" callout and lesson 07's model-limits box (European-style
Black–Scholes, no skew, no dividends, not for pricing a real order) are
correct and appropriately deflationary. Spot-checks of the arithmetic hold:
lesson 05's calculator ($25,000 × 0.5% = $125; $125 ÷ $4 risk/unit = 31
units; 2.00R geometry) and lesson 07's breakeven (100 strike + $4.58 premium
= $104.58) are internally consistent.

## Defects found, in order of severity

### 1. Lesson 05's stop drill contradicts its own chart (factual defect)

The drill chart in `invalidation-stops-risk-reward` marks the protected swing
at **98.45** (the annotated candle low, `{ 11: { l: 98.45 } }`) but draws the
"Protected low" level line at **98.5** — half a tick *above* the low it
names. The explanatory prose then rests the whole reading on 98.5: "What that
reading rests on is 98.5 — if price closes below it…". A careful learner —
exactly the learner this lesson is trying to produce — sees a level line that
price has already traded through at the very swing that defines it, in the
one drill whose stated rule is "the protected low breaks with enough room for
ordinary noise". In a lesson teaching that the *precise* structural level is
what a stop expresses, the marked level disagreeing with the marked swing is
a correctness defect, not a rounding nicety. **Fix: draw the level at 98.45
and let the prose cite the one number the chart actually shows.**

### 2. Lesson headers misstate what the lessons are (structural defect)

Lessons 02–07 all carry the brand strapline "Standalone interactive learning
lab" — a leftover from before these pages were a course. They are not
standalone; the course home explicitly says each lesson assumes the one
before it, and lesson 04's drill is unanswerable without lesson 01's
vocabulary. Lesson 01's strapline ("Read price before indicators") is the
only one that describes content. A learner who lands on lesson 05 from a
search result is told, in the header, that prerequisites don't exist.
**Fix: replace the strapline on 02–07 with the lesson's position in the
sequence ("Course 1 · Lesson NN of 07"), which is both true and navigational.**

### 3. No lesson states an observable objective (pedagogical defect)

Every hero states a topic or a philosophy ("Learn to read the story of
price"; "A stop should express where the trade idea is wrong") but none
states what the learner will be able to *do*. The material for the objective
already exists — each drill is the observable behaviour — but the promise is
never made, so the learner cannot check themselves against it. The course
*home* is actually better here ("Read bullish, bearish, ranging, and
transitioning structure from swing points…") than any lesson it links to.
**Fix: add a one-sentence "By the end" objective to each hero, phrased as the
observable act the drill already measures — classify, choose, compute,
justify — in the author's voice, not boilerplate.**

### 4. Lesson 01's internal "Lesson 0N" kickers collide with course numbering
(navigational defect)

`market-structure` labels its own *sections* "Lesson 01 · The map", "Lesson
02 · Interactive", "Lesson 03 · Vocabulary", "Lesson 04 · Context" — but the
page *is* Lesson 01 of a seven-lesson course, and the breadcrumb directly
above says so. A learner reading "Lesson 04 · Context" halfway down Lesson 01
has every reason to think they've somehow skipped three lessons — and the
actual Lesson 03 (`multi-timeframe-market-structure`) then re-teaches that
same "Context" section at full depth, so the collision is not hypothetical:
two different things in the course are both called "Lesson 04 · Context" (the
section) and "Lesson 03" (the page that owns the topic). This is intake debt:
the page was once a standalone lab with internal "lessons".
**Fix: rename the kickers to "Part 1–4" and neutralize the duplicated-topic
kicker; the sections are parts of one lesson, not lessons.**

### 5. Volume "baseline" is used before it is defined (cognitive-load defect)

`volume-relative-strength` leans on "baseline" as its central quantitative
idea (the metrics panel, the 2.3× expansion figure, the drawn baseline)
but never says what the number is: the mean of the ten bars before the
event bar (`data.slice(eventIndex - 10, eventIndex)`). The learner is asked
to reason about "2,240 against a baseline near 950" without being told
whether the baseline is a mean, a median, or over what window — the one
number in the course whose derivation is hidden. **Fix: one sentence in the
lab intro defining the baseline as the average of the ten bars before the
event bar.**

### 6. Smaller findings, addressed opportunistically

- **`pullbacks-entry-models` orders the three families A, C, B** (Aggressive,
  Confirmation, Continuation-breakout as "B") — the icons read A/C/B down the
  row. The order itself (by confirmation, earliest first) is right; the
  letters fight it. Relabelled to 1/2/3 to match the "earlier price ↔ less
  confirmation" axis the hero establishes.
- **Lesson 07's home-page blurb is a feature list**, not a description of a
  decision ("Explore long-call and long-put strike, expiration, Greeks…").
  Every other blurb on the course home describes an act of judgement.
  Rewritten to match the lesson's own framing: choose expiration, strike and
  acceptable friction so the contract survives the thesis.
- **`ranges-breakouts-liquidity` defines "liquidity sweep" twice with two
  different mechanisms** (concept card: "rejects and closes back inside";
  framework: "fails to remain outside, and often accelerates back through").
  These are compatible but a learner meeting the term for the first time
  should see the definition converge, not drift. The framework card now
  builds on the concept card's wording instead of restating it differently.

## What the course claims but does not teach

The course home claims the course teaches "how an options contract is chosen"
— and lesson 07 does teach selection *mechanics* well — but the course never
teaches the learner to decide **whether** an option is the right expression
at all versus the linear instrument lesson 05 modelled. Lesson 05 flags the
boundary honestly ("Options are nonlinear; use option premium… rather than
treating underlying price distance as exact contract risk") and lesson 07
picks up on the far side of it, but the decision between the two expressions
falls in the gap. This is deliberate scope (course 3 of the path takes "the
same plan into options") and is acceptable for course 1 — but it is a claim
boundary worth recording: the course teaches *how* to select a contract, not
*whether* to.

## Where a learner gets stuck

The single hardest transition is lesson 06 → 07. Lessons 01–06 build one
continuous scenario language (structure, location, trigger, stop, R); lesson
07 introduces, on one page: moneyness, DTE, delta, theta, vega, IV,
breakeven, spread-to-mid — eight new terms with only the "decision stack" as
scaffolding. It is the longest lesson (~30 min by its own estimate) and the
only one flagged "Intermediate → Advanced". This is a real cognitive-load
cliff, and the honest fix at path level is that course 3 exists to absorb it.
Within this course, the mitigation is that the chain explorer exposes one
variable at a time and both simulators derive from the same selected
contract. The cliff is documented here rather than papered over: splitting
lesson 07 would break the course's own promise that 07 prices the plan built
in 05, and the split content already exists as course 3.

## Structural verdict

Seven lessons, in this order, is the right structure. No lesson needs
splitting, merging, reordering, or removal; the defects above are all
in-place repairs. The refactor accompanying this assessment makes exactly
those repairs: the 98.45/98.5 correction in lesson 05, sequence-position
straplines on 02–07, an observable objective in every hero, "Part N" kickers
inside lesson 01, the baseline definition in lesson 06, and the three
opportunistic fixes listed above. URL space is unchanged; the five URL
declarations did not need to move.
