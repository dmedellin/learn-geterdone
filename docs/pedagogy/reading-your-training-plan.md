# Pedagogy assessment — Your Training Plan (Reading Faster, course 8)

Formed from the four lesson dicts in `content/reading/c8_training_plan/part_a.py`
and the course dict in `__init__.py`, the three warm-up passages (`P49` Salt
from the Sea, `Q16` Where the Rainbow Stands, `P48` Land Made from Water) and
the one drill passage (`P47` In Praise of Maintenance, the Subject's only
hard-band argument), on branch `feat/reading-subject` before the Subject was
wired. The design authority is `docs/reading/PLAN.md` §0, §B (the Subject's
rule for a real change and its one-in-five false-positive rate), the Course 8
entries in §C, §D.3 items 2 and 3 (log kinds; the three verdict tiers), §F
and §G, with `docs/reading/kit-report.md` for what the `log` views and the
`drill/single` `vsLog` comparison do as built. The pre-authoring review's
findings 4, 10, 15 and 21 reshaped this course (kinds in the log, the
median-of-three rule, the battery's worked line, and the plateaus lesson's
single-reading design), and each is checked here.

Every lesson was read in full before anything was changed. The course was
rendered with `python3 scripts/preview_subject.py reading --course
reading-your-training-plan`, every preset's tiles were read off the rendered
pages with `node scripts/labcheck.js --observe`, every figure in prose was
recomputed by hand, every math run's `data-say` on the four pages was read,
and every drill was done in a real browser (Playwright, Chromium, against the
rendered site served on port 8828), twice: once with an empty log and once
with a seeded log of three baselines, tests, two pacer practice readings and
one free recall, so that each `log` view's fill could be read against known
figures. Lessons, in course order: `a-practice-week`, `reading-your-curve` |
`plateaus-and-transfer`, `the-full-battery`. The bar marks the seam between
the two modules, The plan and The test. The course assumes the first seven,
above all a log kept since The Daily Drill, and is judged against that.

## Verdict

The course does what the Subject's last course must: it hands the reader the
routine, the log and the rule for reading it, and makes each of them do
something on the reader's own numbers. A reader who finishes it can write a
week of sessions under a budget and name the rule an unbalanced week breaks;
strike the entries of a log that do not count, compute the baseline range and
the median of the last three tests and give the verdict in the Subject's three
tiers; set a first reading of a new kind of text beside the range and the
recent median and say why one reading of a new kind settles nothing; and read
a four-row profile by how many readings stand behind each row. Those are the
acts the `standard` fields name and the quizzes measure. The misconceptions
are the §C four, each refuted with a preset's figure: `all-sprints` with "no
test in the week"; the `noise` log's 262 against its median 244; `does-not`'s
300 wpm becoming 200 effective; `rate-flat`'s 245 → 244 beside a scan time
halved.

All 25 pinned tile strings on the four pages matched the lab, and every
figure in prose agreed with a recomputation: `5 × 15 + 2 × 15 = 105`,
`30/105 = 2/7 ≈ 28.6%`, `120 − 105 = 15`; `285.6 × 5/6 = 238`, `294 × 5/6 =
245`, `251 × 6/6 = 251`, `314.4 × 5/6 = 262`, `324 × 5/6 = 270`, `292.8 × 5/6
= 244`, `286.8 × 5/6 = 239`, `354 × 4/6 = 236`, `360 × 4/6 = 240`, `357 × 4/6
= 238`, the practice entries' `275, 280, 290, 240`; `389 × 60 / 97.25 = 240`,
`389 × 60 / 77.8 = 300`, `300 × 4/6 = 200`, `238 − 200 = 38`, `240 − 270 =
−30`, `200 − 270 = −70`; the median of `262, 270, 266` is `266`, `266 − 251 =
15`. The passages' word counts (397, 399, 375, 389) are what the bodies and
§C say, `Q16` is standard band as the §R reconciliation moved it, and `P47`
is the hard-band argument whose six questions (main claim, the budget
asymmetry, the reply to the objection, the drainage example, the two
remedies, the photograph line) test the reading of an argument rather than
recall of a fact.

The browser pass found the kit doing what §C and the kit report say, and the
lessons describing it accurately in all but three places, each repaired
below: Reading Your Curve told the reader to take the warm-up "so that your
own curve ends with today" without saying that the panel reads the log at
load and on Show my log, not when the warm-up scores (the tiles did not move
after the warm-up until the button was pressed); The Full Battery's `steps`
and `note` said today's rate must be typed by hand and that the verdict tile
judges one rate alone, when the fill reads the warm-up as the latest test and
lists the tests so that the verdict follows the median rule (the fill gave
`tests: 262, 270, …` with the two warm-ups appended, and the verdict tier
"on the median of the last three tests"); and Plateaus and Transfer said the
lab fills the recent test median from the log without saying it does so only
once the log holds three tests (with two, the box kept the preset's 270 while
the range updated to the log's). Nothing needs splitting, merging or
reordering; one cross-course dependency is recorded under recommendations.

## The voice, judged against §F

- **The reader's own numbers.** "Open your log and count last week's days with
  a session, and the sessions that were tests" (lesson 1); "A single test
  above the top of that range happens about one time in four by chance"
  (lesson 2); "Suppose your recent test median is 270 … and suppose the tests
  have stayed near 270 for some weeks. That is a plateau" (lesson 3); "What it
  leaves you with is not a speed but a method" (lesson 4). The course never
  says "your reading speed" or "your level" except inside the misconception it
  refutes ("My best session is my new level").
- **Presented, not endorsed.** Ericsson, Krampe and Tesch-Römer are cited with
  their limit in the same breath: "How much of expert performance such
  practice explains is contested, and their study was of music, not reading;
  the routine borrows its shape, not a promise." Rayner and colleagues (2016)
  on eye exercises and the brain-training games get the one sentence §G
  allows. "The research finds modest rate gains with comprehension held; the
  large savings are in Skimming, Scanning and Previewing and in Words,
  Knowledge and Difficulty" is the sentence the pre-authoring review (35c)
  asked the practice lessons to carry, and both lessons 1 and 3 carry it.
- **No promises.** The course `footer_lead` ends "a plan the lab says fits is a
  plan, not a promise", and `not_covered` says the routine's numbers are the
  Subject's choices, not a prescription measured for reading.
- **Scenes only where the object is in the reader's life.** "One long Saturday
  gives it one day, measured five times" is the course's one image and it is
  the misconception's.
- **Pointing forward by title**, and at the end, back: "Tomorrow, go back to The
  Daily Drill" is the right last sentence for a Subject built on a routine.

## Per-lesson findings

### `a-practice-week`

Teaches planning under a budget with rules the lab cannot check, and says so:
"It checks the arithmetic and the fourth rule only. The other three are yours
to check, and the presets are chosen so that the tiles look fine on weeks that
break them." That sentence is the lesson's best move, because `weekend-only`
then fits exactly, shows 50% testing, and breaks two rules the body names;
quiz 3 asks which. The routine restated in paragraph 2 matches The Daily
Drill's `ol` item for item (ten to fifteen minutes; one pool passage with the
pacer at the hold target; every fifth session a test; × 21/20 after three
holds, × 19/20 after two misses; at most two timed readings a sitting; a
shorter session, not a slower pacer, after a lapse), so quiz 4's answer is the
routine's and not the lesson's invention. Quiz 2 tests the one trap in the
lab (shares are of minutes, not sessions: `12/90 = 2/15`). The browser
confirmed the warm-up `P49` logs as `test`, "Save this plan to my log" writes
a `plan` entry with the rows as text, and a second visit refuses to serve
`P49` again ("reading one again would measure your memory of it").

### `reading-your-curve`

Teaches the Subject's rule and the entries it leaves out, on three example
logs that share their baselines, which is the right design: the reader sees
the same range give three verdicts. The bodies work every figure of every
preset, including the practice entries drawn lighter. The kit's `lgTiers`
rule (median of the last three first; if inside, the latest test decides
between "once" and "inside") is what quiz 1 tests, and its keyed answer
states both parts. The browser confirmed: with an empty log the boxes hold
`real-gain` and `lgMsg` says so; with the seeded log the fill puts every
baseline first, sets `baseN`, writes the practice entries to their own box,
lists every entry under the chart with the uncounted ones greyed, adds a
note entry, and exports CSV; after the warm-up `Q16`, Show my log brings the
session count from 6 to 7 and the latest effective rate to the warm-up's.

What the lesson did not say is that last step. The warm-up scores into the
log but not into the panel; the first paragraph promised "your own curve ends
with today" and a reader following it would have seen yesterday's tiles.
Repaired in the body and in `steps[1]`: press Show my log after the test.
The body's hard-passage caveat (the pool grows harder toward its end, so a
fall that coincides with it is the passages until standard tests say
otherwise) is the one thing the rule cannot see, and the lesson's `note`
names it too.

### `plateaus-and-transfer`

This is the redesign the pre-authoring review's finding 21 asked for, and it
is right: one reading of `P47`, logged `other` with the reason explained in
the first paragraph and tested by quiz 3, and three figures side by side with
the range and the recent median read from the log. The browser confirmed the
preset boxes at load, the fill of `baseLo`, `baseHi`, `baseN` and `recent`
after Score from a seeded log of three baselines and three tests (200/220/240
from effective rates 200, 210, 220 and 230, 240, 250), the "Use my baseline
range" button, and a log entry of kind `other` on `P47`. The two presets are
the two readings of a plateaued reader and the body says what each is
consistent with and what neither can settle; `does-not` is tied back to the
rate-only log of the previous lesson, which is the right cross-reference.
The `steps` are a protocol the reader can run on a contract or a paper, with
an own-text variant ("write down its three main points and then check them").

One omission, repaired: the kit fills `recent` only when the log holds three
tests (`rdBaseFill`: `slice(-3).length === 3`); with fewer the box keeps
whatever it shows, which after a preset is the example's 270, and the
`drVsRecent` tile then compares the reader's reading with a number that is
not theirs while `drVsBase` is. The body now says so and tells the reader to
clear the box or read that tile as a comparison with the example.

### `the-full-battery`

Teaches a profile and the honest reading of it: one row with a range and
three tests behind it, three rows with one reading each side. The
`after-practice` body works the median of the last three (262, 270, 266 →
266) as the review's finding 15 asked, and explains why the preset's tile
prints the "once" tier instead (no `tests` list), with quiz 2 testing exactly
that. `rate-flat` is the reader the one-number view forgets, and the body
says what its scan row is worth: "one reading each, so not yet a result, but
the row that says where to measure next."

The browser confirmed the fill: after the warm-up `P48`, Fill from my log
wrote `errThen` 245 from the seeded baselines with their range, `errNow` as
the warm-up's effective rate, `tests` as the seeded tests with the two
warm-ups appended (the one from Reading Your Curve and this page's), the
verdict in the median-of-three tier, the recall row from the seeded free
recall (`5/12 → 5/12`, one entry so first and latest coincide), and the gist
and scan rows unchanged ("boxes your log cannot fill keep the example").

Three statements contradicted that and are repaired: `steps[2]` ("type today's
effective rate into the box for now"), the `note` ("the profile's fill does
not read it, so today's rate is typed by hand … the verdict tile judges one
effective rate alone") and `mistakes[2]`, which described the tile as always
the one-in-four comparison. §C says the fill reads the latest test "warm-ups
included", the kit does, and the body's second paragraph already said so; the
lesson now says it in one voice: the fill lists your tests, today's warm-up
included, and the verdict follows the median rule on them; the presets list
none, so their tile judges one rate alone.

The gist and scan rows have a dependency outside this course. The fill reads
only entries of kind `baseline` or `test`, and the drills that produce gist
and scan entries (Skimming for Gist, logged `condition`; Scanning for a
Target, logged `other` by the kit's default) are not in those kinds as
Course 5 is authored, so for a reader who has done every lesson those two
rows still keep the example. The body already hedged ("A row your log cannot
fill keeps the example"); it now names the two rows so that a reader does not
hunt for a skim the fill will not find. The fix that would make the rows fill
is recorded under recommendations.

## What the course teaches well

- **Rules the lab cannot check are taught as the lesson's content**, not hidden
  behind tiles that look fine. Lesson 1 says which three of its four rules the
  tiles cannot see and builds a preset that passes the tiles and fails the
  rules.
- **The verdict is taught as a rule of thumb with a known false-positive
  rate**, in the course `not_covered`, in lesson 2's body and `note`, and in
  the kit's own verdict string ("a fourth reading does this about one time in
  four"). The reader is never handed a significance test they do not have.
- **Like is compared with like, and the lesson says which entries are unlike.**
  Lesson 2's "Which entries does the verdict leave out?" paragraph gives the
  reason for each kind (the pacer set the rate; a technique on trial; measures
  something else; no questions, no effective rate), and lesson 3 applies the
  same logic to its own reading by logging it `other`.
- **A first reading of a new kind is treated as the start of a series**, not a
  failed test: `mistakes[1]` of lesson 3 and the `standard`'s "what further
  readings would settle it" make the reader plan the next measurement rather
  than draw a conclusion.
- **The seam between modules is invisible.** Lesson 2 ends by asking what a
  flat curve means and promising a new kind of text; lesson 3 opens on that
  text and ends with the other three measures; lesson 4 opens with them.
  Every cross-reference is by title (The Daily Drill, Sprints Above Comfort,
  One Reading Is One Measurement, Skimming for Gist, Scanning for a Target,
  Free Recall), each as that lesson carries it.

## Repairs made in this pass

In `content/reading/c8_training_plan/part_a.py`: `reading-your-curve` body
paragraph 1 and `steps[1]` (press Show my log after the warm-up);
`plateaus-and-transfer` body paragraph 2 (the recent median fills only with
three tests); `the-full-battery` body paragraph 2 (the skim and scan rows
named as the ones that keep the example), `steps[2]`, `mistakes[2]` and
`note` (the fill reads today's warm-up and lists the tests; the presets' tile
judges one rate). No preset, `expect`, slug, module, lab key, mode, view,
passage or log kind changed, and no §C entry needed correcting.
`scripts/preview_subject.py reading --course reading-your-training-plan`
reports OK: 5 pages, 4 labs executed and swept, 4 with pinned figures, 0
failing. No page overflows at 360 px and no page or console error was raised
in either browser pass.

## Recommendations (not done)

- **Log the skim and the scan as `test`, so the profile's gist and scan rows
  can fill.** `log/profile` reads `baseline` and `test` entries only
  (D.3.2). Skimming for Gist's `drill/single` with `display: gist` is logged
  `condition`, and Scanning for a Target's `scan/find` defaults to `other`.
  Neither entry can enter the effective-rate curve whatever its kind (a gist
  display is not a reading by `rdIsReading`, and a scan entry's mode is
  `scan`), so changing those two cfg kinds to `test` would fill the battery's
  rows at no cost to the curve. The kit report's "Proposed PLAN edits" asks
  for the same. Course 5's files; for the orchestrator.
- **Refill the history panel after a warm-up scores on the same page.** The
  kit refreshes `drill/practice` and the compare range after Score but not
  `log/history`; a call to the fill after the warm-up's Score would make
  "your curve ends with today" literally true without the button. Kit change
  (`readkit_b.py`, history UI); low priority now that the lesson says to press
  the button.
- **Fill `recent` with the median of however many tests the log has, or blank
  the box when it has fewer than three.** Leaving a preset's 270 in the box
  beside a range that has just been replaced by the reader's own is the one
  place on the course where a tile can compare the reader with a number that
  is not theirs. Kit change (`readkit.py`, `rdBaseFill`); the lesson now warns.
- **A `how_to` for a reader whose log is thin.** The course says the labs
  "teach the rule but say nothing about you" with an empty log, which is
  right; a reader with three baselines and one test, the common case for
  someone who reached this course quickly, gets "needs a reading after the
  three baselines" and "after 6 sessions" without being told that two more
  tests, a week apart, are what the rule is waiting for. One sentence in
  `how_to[1]`.
