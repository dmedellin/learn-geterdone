# Pedagogy assessment — Volume and Order Flow (trading, course 5)

First-pass assessment, formed from the sixteen lessons, the course home, the
published schema and the shared lab script as they stand on `main` at
fabd5ef. There is no prior assessment of this course, so there is no delta
section.

Course home: `site/volume-and-order-flow/index.html`. Lessons, in course
order: `volume-fundamentals`, `price-volume-relationships`,
`relative-volume-and-volume-spikes`, `volume-confirmation`,
`on-balance-volume`, `accumulation-distribution-and-chaikin-money-flow`,
`volume-weighted-average-price`, `anchored-volume-weighted-average-price`,
`volume-profile`, `value-area-poc-hvn-lvn`, `bid-ask-spread-and-order-types`,
`time-and-sales`, `footprint-charts-and-bid-ask-delta`,
`cumulative-volume-delta`, `order-book-and-market-depth`,
`volume-and-order-flow-trading-rules`. The published asset
`volume-order-flow-rule-schema.json` is the export shape lesson 16 claims.

Every lesson ships one shared script — all sixteen labs, the synthetic series
generator, the participation-reading table and the quiz engine — and a
`window.LESSON.lab` key selects which lab runs. The copies are byte-identical
except for six reading strings that were corrected on the page that uses
them and left stale on the fifteen that do not (details below). No readout is
written into the static HTML: every figure is produced by script, so what
can be wrong is the arithmetic, the labs' verdicts, and whether a drill
measures what its lesson promised. Every number below was obtained by
executing the shipped script in a stub DOM, not by reading it.

Courses 1–4 are the declared predecessors and the home says nothing is
loaded from them. What it assumes is vocabulary: "resistance", "structural
invalidation", "range boundary" and "setup" (courses 1–2) in the
confirmation lesson and the rule builder, and "moving average" in the
audience note. Inside the course the order holds: the quote (11) precedes
the classification built on it (12), which precedes the footprint (13), its
running total (14) and the book (15); VWAP (07) precedes anchored VWAP
(08); the profile (09) precedes its landmarks (10). Lesson 11's lab does
show displayed depth, which lesson 15 treats properly, but it shows it as
the thing a market order consumes, which is the right amount for a lesson on
execution cost.

## What the course teaches well

- **The central misconception is named on the home, in the audience note,
  in the first lab's formula card and in every participation reading.**
  Volume counts contracts, every one of which had a buyer and a seller;
  delta is a classification of where a print landed, not a count of
  participants; displayed size is cancellable. The course never lets a
  reader leave a lesson thinking a green number means "more buyers".
- **Every lab verdict states its own invalidation.** The participation
  readings end with the condition that would end the reading — "a close
  back under 101.10 is what would return this to a failed break", "price
  beginning to travel on that same slope would make it an ordinary advance
  instead". This is the discipline the rule lesson later asks for.
- **The order-book arithmetic is right to the cent.** Normal book 3,940 bid
  against 4,070 offered; a 700-lot market buy at 100.0146; the thin book's
  same order walking four levels to 100.0285; 3,000 lots exhausting 1,019
  displayed; the ask wall making a 3,000-lot buy *cheaper* (100.0187 against
  100.0299). The wall scenarios replenish 4,200 → 3,400 → 4,500 → 4,600 and
  then vanish, and near-touch depth drops 6,010 → 2,330 exactly as the
  reading says.
- **The tape and CVD numbers are the numbers.** Twenty-five of forty-two
  prints at the ask carrying 8,110 against 5,139; a 5.6 : 1 bid-side
  imbalance moving price four cents; +14,011 cumulative delta on a 14.09
  point advance; −7,748 on a 16.39 point advance for the divergence case;
  every figure quoted in a reading was reproduced.
- **The rule export validates.** All 1,440 combinations of context × side ×
  participation × location × flow × confirmation were generated from the
  shipped `ruleSpec` and validated against the published schema with
  Draft 2020-12 semantics: 0 failures. The home's interop section describes
  exactly the shape that comes out, and is explicit that no performance
  object exists in it.
- **The lab labels its own conventions.** The value area is "approximately
  70%" and the home says it is a convention; footprint classification is
  "simplified and explicitly labeled"; the CVD card lists venue, feed,
  aggregation, classification and reset as things that move the line.

## What the course teaches badly

### Two labs draw the opposite of what their tab says

`price-volume-relationships`: the tab "Price ↑ / Volume ↓" builds its series
from `makeSeries("bull-volumedown")`, and the generator tests
`kind.includes("down")` for a downtrend, so the string that asks for rising
price on falling volume produces a *falling* price (−10.5% over the window,
volume −39%). The structural reading beside it says "Buyers are moving
price higher with less participation" and the KPI beside that says
"Price −10.5%". The shared-script comment admits this and leaves the
participation reading blank rather than lie. The fix is in the generator:
the price regime is the first token of the kind string, and only that token
may set the drift. Checked by execution that no other kind used anywhere in
the course changes (thirty-four kind/length/seed combinations compared
byte-for-byte; only `bull-volumedown` differs, and it now rises 14.2% on
volume −39%).

`on-balance-volume`: the tabs "Bear divergence" and "Bull divergence" use
the same broken kinds, so both show a falling price with OBV falling beside
it (−15.6% / OBV to its low; −16.4% / OBV to its low). There is no
divergence on either tab, the reading beside each says there is, and the
lesson's third concept card — the one thing this lesson adds to lesson 02 —
is therefore never demonstrated. Fixing the generator alone does not fix
this: a rising price on contracting volume still puts most of the volume on
up closes, so OBV still rises. The divergence has to be built: from bar 24
the down-closing bars carry three times their volume and the up-closing
bars 0.45 of it. Checked by execution: price then finishes +16.9% with its
high on the last bar while OBV peaks at bar 37 and ends −14,231 (the bear
case); price finishes −10.7% with its low on the last bar while OBV bottoms
at bar 24 and ends +8,915 (the bull case). That is the shape the concept
card describes.

### The Balanced CMF tab reads "bear"

`accumulation-distribution-and-chaikin-money-flow`: the "Balanced" tab
places closes at 42% ± 16% of the bar, which is below the midpoint on
average, so CMF sits between −0.16 and −0.18 at every lookback the slider
offers and the lab prints the *distribution* verdict — a red bar, "High-
volume bars are generally closing nearer their lows", "Sellers are
maintaining weaker closes" — on the tab labelled Balanced. The participation
reading was patched on this one page to say "the reading is negative, but
only mildly", which describes the bug rather than fixing it. Closes centred
at 50% put CMF inside ±0.07 at every lookback from 8 to 30 (checked), so the
flat branch fires; that branch had no participation reading, and now does.

### The two-way VWAP tab's KPIs contradict its reading

`volume-weighted-average-price`, "Two-way": the reading says "Price
repeatedly crosses a flat VWAP" and the participation text (correctly)
reports thirteen crossings and 27 of 64 closes above. The KPIs beside them
say "VWAP slope: Falling" and "Bars above: 0/10", because the slope
threshold is ±0.08 over ten bars (the flat case moves −0.14) and the
location count looks only at the last ten bars, all of which happen to be
below. The slope threshold becomes ±0.25 (the trend cases move 1.13, −1.31
and 0.92, so nothing else reclassifies) and the count becomes the whole
session's closes above, which is the number the reading quotes.

### The breakout profile's two readings disagree with each other

`volume-profile`, "Breakout": the structural reading says "Buyers left the
prior value area and began building activity above it. The upper
distribution indicates acceptance"; the KPI says "Two distributions"; the
participation reading, derived from the same data, says "the profile still
shows a single node low down … the second distribution that would make it
acceptance has not formed". The participation reading is the true one — at
18 bins exactly one bin exceeds half the POC's volume, and it is in the old
range — because `breakout-volumeup` trends for the rest of the window and
never rotates. The series now rotates around the level reached at bar 50
for its last fifteen bars at breakout volume, and the profile shows two
nodes at every bin count from 10 to 30 (checked: nodes above half the POC
at ~99.7–100.0 and ~104.6–105.0). The structural reading and the KPI were
right about what the tab should show; now the data shows it. The
participation reading is rewritten with the new figures, and gains the
observation the two-distribution shape makes possible: a single value area
drawn across both nodes spans the thin middle as well, which is why a
double distribution is usually read as two profiles.

### The footprint prints volume at prices the candle never traded

`footprint-charts-and-bid-ask-delta`: each candle carries nine bid × ask
rows, and the grid draws them against one nine-rung ladder spanning the
window's low to high — so every candle shows executions at every rung,
including the six or seven rungs outside its own high–low range (checked:
two to four rungs per candle are actually inside it). A footprint records
executions, and nothing executed where the candle did not trade; a reader
who has seen a real footprint will notice, and one who has not will learn
the wrong picture. Rebuilt: one ladder for the window, each candle prints
only at the rungs inside its range (three to five of them), delta and volume
sum only those, and untraded rungs render blank. Every verdict still holds
after the rebuild (checked: aligned-buy deltas all positive with every close
above its open, absorb-buy deltas all positive with every close at or below
its open, and the mirrors), and the readings' figures are rewritten from
the new data. The imbalance highlight compares ask and bid *at the same
level*; platforms usually compare diagonally, and the formula card now says
so, since a reader moving to a real footprint would otherwise carry the
wrong test.

### The LVN tab sits inside the value area

`value-area-poc-hvn-lvn`, "LVN transition": the current-price line is
placed a third of a bin above the value-area low — inside the value area,
in a bin holding 40–50% of the POC's volume, with the KPI reading "Inside
value". The reading says price is "moving through a thinner-volume
transition area". The line now sits in the thinnest non-empty bin below the
value-area low (2–20% of the POC's volume depending on bin count, checked
for every slider position), the KPI reads "Below value", and the verdict
order is corrected so the LVN reading fires before the generic below-value
one would claim "Sellers are maintaining trade below the prior value area".

### The rule validator misses the lesson's own example, and flags what is not a contradiction

`volume-and-order-flow-trading-rules`: the quiz's second question describes
"price below VWAP and sustained acceptance above VWAP at the same bar" as
the contradiction to recognise. The lab cannot produce that verdict: its
validator checks side against confirmation and side against flow, never
location against confirmation, so "Below VWAP" + "Hold above VWAP" passes
as "internally consistent". Added. Meanwhile a short in an uptrend is
reported as an *issue* with the verdict "The rule asks the market to show
conflicting behavior … Revise the conditions before backtesting" — but a
countertrend rule is not internally inconsistent, it is a choice. It is
now a note beneath a passing validation rather than a failure.

### Drills that do not test what the lesson promised

Every lesson's completion standard is an act of measurement — "normalize
current volume against a baseline", "accumulate volume by closing
direction", "measure where price closes inside each bar's range and weight
that location by volume", "calculate session VWAP", "compare executed volume
at the bid and ask", "accumulate bid-ask delta through time" — and the labs
compute each of them. Only two quizzes in the course ask the reader to
compute anything (RVOL on 03, a single delta on 13). Each calculation lesson
gains one question whose answer is a number the formula produces, with the
arithmetic worked in the feedback:

| lesson | question | answer |
| --- | --- | --- |
| 01 | a bar prints 5,000 contracts: how many bought, how many sold | **5,000 and 5,000** |
| 02 | last-14 average 1,250 against first-14 average 1,000 | 1,250 ÷ 1,000 → **+25%** |
| 03 | baseline 1,000, bar 2,400, threshold 1.5× | **2.4×**, a spike |
| 04 | break bar 2,700 against an 18-bar average of 1,500 | **1.8×** |
| 05 | closes 100, 101, 100, 102 on volumes 500, 800, 300, 400 | 800 − 300 + 400 = **+900** |
| 06 | H 110, L 100, C 108, V 1,000 | multiplier (8 − 2) ÷ 10 = **0.6**, MFV **+600** |
| 07 | TP 100 on 100 then 102 on 300 | 40,600 ÷ 400 = **101.50** |
| 08 | anchored at bar 10: TP 50 and 52 on 200 each | 20,400 ÷ 400 = **51.00** |
| 09 | bins 400 / 1,200 / 900 / 300 | POC the 1,200 bin; the pair holds 2,100 of 2,800 = **75%** |
| 10 | value area at 6,600 of 10,000, next neighbour 800 | 66% < 70%, add it → **74%** |
| 11 | bid 99.99, asks 300 @ 100.01 and 600 @ 100.02, market buy 500 | spread **0.02**, average **100.014** |
| 12 | six ask prints 1,800, four bid prints 1,500 | **+300** ask-classified; direction still from price |
| 13 | levels 200×500, 300×300, 400×100 | delta **0** on 1,800 |
| 14 | deltas +300, −100, +200, −500 | CVD **−100**, high **+400** |
| 15 | bids 420, 690; asks 380, 610 | near-touch **2,100**, spread **0.02** |
| 16 | long rule with ask-side absorption as flow and a break above resistance | **conflict**, and the validator says why |

The quiz engine shows one explanation per question, so a reader who picked
"the bid" and one who picked "yesterday's close" on lesson 11 are told the
same thing. The engine now accepts a `data-why` on each choice and shows the
chosen one's; every distractor on every page has one. The filler distractors
no reader would choose ("Depth has no units", "Pace determines earnings",
"Profit", "Volume is removed", "A stop-loss rule") are replaced by the
misconception the lesson's own common-mistakes card names.

### No lesson shows its arithmetic being done

The course 4 assessment praised calculation lessons that "print the window,
the sum and the division for the selected bar". No lesson here does: OBV,
CMF, VWAP, anchored VWAP, CVD, relative volume, the confirmation ratio and
the footprint delta are all plotted or reported as a finished number, and
the reader's first attempt at the arithmetic is the quiz. Each of those
labs now prints a worked block under the chart — the last bars' closes,
volumes and running OBV; the selected bar's multiplier, money-flow volume
and the period sums; typical price, its product with volume and the two
cumulative sums; the twenty-bar baseline and the division; the selected
candle's ask and bid sums — so the progression is worked example (the lab),
faded (the reading, which quotes the figures), independent (the quiz).

### Objectives written as "understand"

`volume-fundamentals` ("Understand what volume measures…") and
`bid-ask-spread-and-order-types` ("Understand quoted prices…") — in the
hero, the three description metas, the course-home card and the manifest
the home calls authoritative. Rewritten as acts ("Say what a volume figure
counts and what it cannot say…", "Read a quote, name the spread, and choose
between a market and a limit order…") in all six places.

### Copy errors a reader would trust

- The six reading strings that were corrected on the page that uses them and
  left stale elsewhere: "several times" / "about three times" (the closing
  stretch of the absorption case runs 3.5× the earlier bars — neither);
  "seventeen bars" / "sixteen" (sixteen); "without giving any of it back" /
  "with small pullbacks" (eight down-steps: pullbacks); "a fifth" / "a
  quarter" of normal size (0.25 and 0.28: a quarter); "Nothing on this book
  has been tested" / "Little"; and a `wallCancel` reading that on fifteen
  pages says nothing traded against the wall when 800 lots did. All sixteen
  copies are now identical and carry the verified sentence.
- `volume-fundamentals`, absorption reading: "price covers a little over a
  point" — across the whole window; across the heavy-volume stretch it is
  half a point. Both are now stated.
- `volume-confirmation`, weak case: "the volume trend through the window
  falling" — the last twenty bars average 1.03× the first twenty. What is
  true is that the baseline thins into the break (1,459 → 1,223) and the
  break bars barely exceed it (1,491). Reworded.
- `volume-profile`, breakout: "About 61% of the window's volume trades after
  price leaves the old range" — measured from the pivot bar, not from the
  bar that leaves the range (42), which gives 59%. Moot after the series
  rebuild; the new figure (53%) is stated as computed.
- `relative-volume-and-volume-spikes`, climax: the KPI labelled "Spike RVOL"
  reports 1.53× for the marked bar while the reading talks about "close to
  six times baseline on the final bars". The climax case has no spike bar;
  the KPI now reports the window's peak RVOL (6.18×) under that label.
- `volume-weighted-average-price`: "typical price" appears in the formula
  card and is defined only on the course home. Defined in place.

## What it claims to teach but does not

- `on-balance-volume` promises divergence and could not show one. Fixed as
  above.
- `price-volume-relationships` promises "the four basic combinations" and
  showed three (two of them twice). Fixed as above.
- `volume-profile` promises to identify "multiple value areas" (concept
  card 3) and its breakout tab showed one. Fixed as above.
- `volume-and-order-flow-trading-rules` promises to flag "combinations that
  contradict each other" and did not flag the one its own quiz uses. Fixed
  as above.
- `anchored-volume-weighted-average-price` carries an "unaligned" verdict
  branch that no anchor position on any tab can reach (checked, all 165
  combinations). Nothing false is shown; the third state is simply never
  demonstrated. Left, and recorded here.

## Where a learner gets stuck

- **Lesson 02, third tab**: the chart falls while the copy says it rises.
  Fixed.
- **Lesson 05, divergence tabs**: the reader is told to see a divergence and
  cannot. Fixed.
- **Lesson 06, Balanced tab**: the lab's verdict is red. Fixed.
- **Lesson 07**: "typical price" as a given. Fixed by definition in place.
- **Lesson 10, LVN tab**: the KPI says inside value. Fixed.
- **Lesson 13**: a footprint that does not look like a footprint. Fixed.

## Structural changes considered

None made. No lesson carries more than one hard idea; lesson 10's four terms
are four names for the landmarks of one object, and lesson 11's four are the
parts of one quote. The order is the dependency order. No URL is added,
removed or renamed; the five declarations are untouched.

## Verification performed

- Every lab's arithmetic executed from the shipped script in a stub DOM,
  for every tab and every slider position that changes a verdict: the
  makeSeries regression (34 kind/length/seed combinations, one differs, as
  intended); OBV extremes and their bar indices on all four tabs; CMF at
  seven lookbacks on all three tabs; VWAP crossings, closes above and slope
  on all four tabs; the anchored branch for all 165 anchor/tab
  combinations; profile nodes above half-POC at five bin counts on all
  three tabs; value-area location and bin volume at nine bin counts on all
  five tabs; tape counts and volumes on all five tabs; footprint signs,
  closes and traded rungs on all four tabs; CVD extremes on all six tabs;
  every book scenario at every event; every one of the 1,440 rule exports
  against the schema.
- Every quiz answer index re-checked against its choices after the rewrite;
  every choice carries a `why`; every worked answer recomputed by hand in
  this document.
- The gates in AGENTS.md §7–8 and the CI steps run locally, listed in the
  commit message.
