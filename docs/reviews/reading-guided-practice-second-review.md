# Second review — Guided Practice (Reading Faster, course 2)

Independent second read of `content/reading/c2_guided/` (`__init__.py`,
`part_a.py`) against `docs/reading/PLAN.md` (§0, §B, Course 2 in §C, §D.3,
§F, §G, §S, §R), `docs/reviews/reading-spec-accuracy-review.md`,
`docs/reading/AUTHORING.md` and `docs/reading/kit-report.md`, following
`docs/reading/SECOND-REVIEW.md`. The findings below were written before the
pedagogy assessment (`docs/pedagogy/reading-guided-practice.md`) was read;
the disagreements are at the end.

## Method

- Every lesson dict read in full; the questions of every passage the course
  uses (`P12`–`P18`, `P23`, `P24`) read, with the text consulted for the
  doubtful ones; the pool's bands listed (`Q01`–`Q08` easy, `Q09`–`Q15`
  standard, `Q26`–`Q28` hard). Word counts as the kit counts them: `P12` 442,
  `P13` 418 (the steadier preset's figures are the real passages'), `P14`–`P16`
  457, 452, 444, `P17` 484, `P18` 474, `P23` 451, `P24` 454.
- Rendered with `python3 scripts/preview_subject.py reading --course
  reading-guided-practice --out <scratch>/sr-reading-guided-practice`; every
  preset's tiles read with `node scripts/labcheck.js --observe`.
- Every figure recomputed by hand.
- The course done in Chromium (Playwright, controlled clock) in the same
  profile as Course 1, so the log was a real reader's: the pacer compare
  (order BA from the log's parity; the paced side ended by itself at exactly
  the target; A logged `test`, B `condition`), the ladder after "Use my
  baseline median" (it filled 251, 301, 376 from a median of 250.91), a Daily
  Drill session with the pacer and the attention tick, the sprint and its test
  (the range boxes filled from the log after Score, verdict "above … once"),
  and the four repeat readings (kinds condition ×3, test). Also checked: "Use
  my baseline median" on the pacer and sprint pages (241 and 483 from a median
  of ≈ 241.5), the paste box sits above Start, and Done is visible during a
  paced run. The passage was hidden during every question; no console or page
  error.
- Research claims against §S and the accuracy review; Rayner et al. (2016)
  additionally against its published abstract (Washington University profile,
  APS press release).

## Arithmetic (all correct)

| Where | Figure | Check |
| --- | --- | --- |
| 1 presets | 442 × 60 / 110.5 = 240; 418 × 60 / 100.32 = 250; 160, ≈ 208.3, ≈ +48.3; 200, ≈ +8.3 | ✓ |
| 1 body | 250 / 6 ≈ 41.7; 250 × 4/6 ≈ 166.7 (≈ 6.7 above 160); 10 × 5/6 ≈ 8.3 | ✓ |
| 1 worked / quiz | 60,000 / 250 = 240; 12 × 240 = 2,880; 8 × 240 = 1,920; 15 × 240 = 3,600; 10 × 60,000 / 300 = 2,000 | ✓ |
| 2 presets | 450 in 112.5, 93.75, 75 s → 240, 288, 360; 240/192/120 and 200/240/240; tie to 288 | ✓ |
| 2 quiz | 200, 240, 300; hold 300; 250 × 5/6 ≈ 208.3, 200, 187.5 | ✓ |
| 3 presets / quiz | 288 × 21/20 = 302.4; × 19/20 = 273.6; 302.4 × 21/20 = 317.52; 300 → 315; 260 → 247; test-due: last three 3, 5, 4 not all holds, last two 5, 4 not misses | ✓ |
| 4 presets | 484 × 60 / 60.5 = 480; 469 × 60 / 105 = 268, ≈ 223.3, 17 above 251; 494 × 60 / 120 = 247, ≈ 205.8; 12 × 60,000 / 480 = 1,500 = half of 3,000 at 240 | ✓ |
| 4 quiz | 241 − 236 = 5 above | ✓ |
| 5 presets / quiz | 442 in 110.5, 88.4, 78 s → 240, 300, 340; 465 / 112.5 → 248; 451 / 98.4 → 275; +100, +8, +35; +90, +12 | ✓ |

## Findings

### 1. Course `how_to` and The Daily Drill: Rayner et al. (2016) stated more strongly than it concludes (fixed)

`how_to` said "the research on the tradition's techniques finds modest rate
gains with comprehension held", and The Daily Drill said the 2016 review
"finds that the gains from training without loss of comprehension are
modest". The review's conclusion (abstract) is narrower: there is a trade-off
between speed and accuracy, readers are **unlikely to double or triple** their
rate while understanding as well, and the way to read faster with
comprehension held is practice in reading and language skill. It does not
report a measured "modest gain". (Raised also by the Course 8 second review
through the coordinator.)
*Changed:* both sentences now attribute that conclusion to Rayner and
colleagues at its own strength; §C's Course 2 header, which asked for the old
wording, now describes the attributed sentence.

### 2. The Daily Drill: the first tests fall on easy passages (fixed in text; recommendation)

The pool is served in order, easy first (`Q01`–`Q08`), and a test is "the
next pool passage at natural pace". The ladder's three rungs count as
practice sessions (the lesson says so), so in the browser the test was due
after the **first** Daily Drill session — on `Q02`, an easy passage — and it
is judged against baselines taken on standard passages. Early Daily Drill
tests are therefore biased toward "above the baseline range", which is the
verdict Your Training Plan later reads back.
*Changed:* a short paragraph after the description of the three tiles says
the pool starts with eight easy passages, that a test on one will come out
faster for that reason alone, and that the tests that compare fairly with the
baselines are on standard passages (from "The Engineer of the Pond" on) and
in the later lessons.
*Recommend (kit or pool):* serve tests only from standard-band pool passages,
or order the pool so that the passages a test can fall on are standard.

### 3. Course `how_to`: the target boxes (fixed)

`how_to` said "The labs know your log, but a pacer's target is a box you
fill", while three lessons tell the reader to press "Use my baseline median"
or "Use my next target", which fill it from the log. *Changed* to say the
buttons fill it, or the reader types it.

### 4. Reading with a Pacer: the tradition is not stated at its strongest (recommendation)

§F asks for the tradition's claims at their strongest before the evidence.
The lesson gives the Evelyn Wood hand only its modest claims (keeps the
reader moving, stops drifting and going back). The courses' best-known claim —
that with the hand a reader could take in whole lines or groups of lines at a
glance, at rates of thousands of words a minute — appears only by implication
("no guide can widen what the eye takes in"). Suggest one clause stating it,
attributed through Rayner et al. 2016, before the rebuttal. Also: the claim
that the review "explains why no guide can widen what the eye takes in at each
stop" fits the review's argument but could not be checked against its full
text; §C 2.1 cites it the same way.

### 5. The paced side's verdict and order (no change; noted)

Reading with a Pacer alternates order; for a course-following reader it came
out BA, so the unpaced `test` follows a paced reading at the reader's own
baseline median. Unlike Course 1's pair (finding 1 there) the paced reading is
not a sprint, and the note names the order confound, so I left it. The kit
rightly drops `drVerdictB` for a paced B.

### 6. Smaller points (recommendations)

- **The Daily Drill, "Read the tiles" step and `rdPool`:** after Score the
  pool line still named the passage just read ("Next unread passage: The Lamp
  at Gull Rock.") until reload; Start served the right one. A kit display
  point.
- **Repeated Reading and Transfer, status line (kit):** the kit's status says
  "Only the second is a change in the reader", stronger than the lesson's "the
  only part that could belong to the reader". Suggest "could be".
- **Repeated Reading and Transfer:** "eight is well inside the difference two
  passages make on their own" is supported by Course 1's ranges (13 and 56)
  only loosely; "inside what two passages can differ by" is safer. "Measured
  against this reader's baseline range, it would be at best above the range
  once" holds for the reading on its own; with two earlier high tests it could
  complete a median. Fine as a statement about one reading.
- **Choosing a Target Pace:** "the tradition's advice is to push … on the view
  that understanding catches up with the pace" is a fair statement of the
  tradition and is marked as its view.

## Research claims checked

- Evelyn Wood courses from 1959 (Rayner et al. 2016 abstract: "Reading
  Dynamics training program in 1959"); the 2016 review "published after his
  death" — correct.
- Ericsson, Krampe and Tesch-Römer (1993): musicians, the size of practice's
  role disputed — as the accuracy review asks.
- Samuels (1979) and Therrien (2004): school-age students with and without
  learning disabilities, gains on new passages smaller than on practised ones,
  adults not the population — as the accuracy review's finding 11, stated
  identically in body, mistake and quiz.

## Quiz and passages

One defensible answer per question; every distractor argued and fails.
Passage questions answerable without reading (report only): `P13` Q4 (the
telegraph closed the Pony Express — common history) and Q2 (station spacing,
by reasoning), `P12` Q5 (letters more than doubled — guessable from the
question's "confirmed"), `P15` Q3 and Q6 (cables in tension, wind — general
engineering knowledge), `P18` Q2 and Q4, `P23` Q2, Q3 and Q5, `P24` Q3 and Q5.
Expository passages on familiar topics will always leave some of this; it is
one more reason a one-question difference is not a result. No question has
two defensible answers on my reading.

## Voice (§F)

Coached and warm; every compare lesson has the "you have not refuted … and
it has not refuted you" sentence and names both confounds; no promises (the
"Why practise at the hold" paragraph says the course does not promise a
gain). No changes beyond the above.

## Preview after the changes

`python3 scripts/preview_subject.py reading --course reading-guided-practice`:
`5 page(s) executed and swept, 5 with pinned figures, 0 failing` — `OK`.

## Where I disagree with the pedagogy assessment

(Read after the findings above were written.)

- **`how_to`'s "Expect modest numbers".** The assessment calls it "the
  sentence that will keep a reader going" and lists it as honest. Its
  research clause ("the research … finds modest rate gains with comprehension
  held") was stated more strongly than Rayner et al. (2016) conclude, and was
  unattributed; the same claim was in The Daily Drill's body (finding 1).
  Both now attribute the review's actual conclusion.
- **The early test.** The assessment found that the ladder's rungs make the
  first test fall due after one Daily Drill session and added that to the
  prose. It did not follow the consequence: the pool is served easy-first, so
  that test (and the next few) are on easy passages judged against standard
  baselines (finding 2). Added a caution; a kit or pool change is recommended.
- **"Stated at its strongest".** The assessment says each technique's claim
  is stated at its strongest before it is measured. True for the ladder and
  the sprint; for the pacer the Evelyn Wood courses' central claim (whole
  lines or more at a glance, thousands of words a minute) is not stated, only
  its modest version (finding 4). Recommendation, not changed.
- **`P16` Q4.** The assessment calls the keyed answer and its mirror image
  "a coin to toss". I read it as a fair detail question: the passage states
  which mill turns whole and which turns its cap, and a reader who read it
  can answer; a mirror-image distractor is what makes it a detail question.
  No change needed.
- Agreed: the arithmetic, the hold/best-run teaching, the sprint as a
  treatment, the repeat drill, the stale "Next unread passage" line, the
  ladder counting toward "sessions since your last test", the pool's length,
  and the unpaced reading of lesson 1 being logged `test` as an open §C
  question.
