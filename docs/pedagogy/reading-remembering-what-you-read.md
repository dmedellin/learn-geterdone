# Pedagogy assessment — Remembering What You Read (Reading Faster, course 7)

Formed from the four lesson dicts in `content/reading/c7_remembering/part_a.py`
and the course dict in `__init__.py`, the four passages their drills use
(`P43` How a Camel Saves Water, `P44` The Mould on the Plate, `P45` The Tower
That Was Meant to Come Down, `P46` Where Autumn Colours Come From, in
`content/reading/passages/bank_b.py`) and the two hard-band pool passages the
third lesson's warm-up serves (`Q24` Grafting an Apple Tree, `Q29` Two Names
for One Hill, in `passages/pool.py`), on branch `feat/reading-subject` before
the Subject was wired. The design authority is `docs/reading/PLAN.md` §0, §B,
the Course 7 entries in §C, §D.3, §F and §G, with `docs/reading/kit-report.md`
as the record of what `readkit` does as built. The pre-authoring pedagogy
review (`docs/reviews/reading-spec-pedagogy-review.md`, findings 13, 23 and
25) asked for this course's two largest redesigns, and both are checked here.

Every lesson was read in full before anything was changed. The course was
rendered with `python3 scripts/preview_subject.py reading --course
reading-remembering-what-you-read`, every preset's tiles were read off the
rendered pages with `node scripts/labcheck.js --observe`, every figure in
prose was recomputed by hand, every math run's `data-say` on the four pages
was read, and three of the four drills were done in a real browser
(Playwright, Chromium, against the rendered site served on port 8827): the
free recall end to end with questions, both sides of the delayed comparison
followed by the twelve-question delayed test (the due date moved back in the
log) and the banner it raises on another page, the hard-band warm-up on
Spacing Your Reviews, and the summary variant on Notes in Your Own Words.
Lessons, in course order: `free-recall`, `retrieval-beats-rereading` |
`spacing-your-reviews`, `notes-in-your-own-words`. The bar marks the seam
between the two modules, Recall and Keeping it. The course assumes the timed
drill and the effective rate from Measure Your Reading and the Daily Drill
from Guided Practice, and is judged against that.

## Verdict

The course teaches its subject, and a reader who finishes it has a skill and a
log, not only facts. The skill is a protocol: read once at the usual pace,
write with the page hidden, tick the idea units strictly, compute the share
and the recalled rate, and compare with your own next recall. The log carries
a free recall logged as a test (which The Full Battery later reads as the
recall row of the profile), two study conditions with a due date, a delayed
test the Subject brings to the reader on any page, a warm-up, and a summary
logged as `other` so that it never enters the recall series. Every `standard`
names an act with a pass level, every `steps` list is a protocol for repeating
the drill on the reader's own texts, and the misconceptions are the ones §C
names, refuted with the lesson's own figures.

All 14 pinned tile strings on the four pages matched the lab (`7/12 ≈ 58.3%`,
`140 wpm`, `5/6 ≈ 83.3%`; `5/6 ≈ 83.3%`, `200 wpm`, `1 = 100%`; `1/3 ≈ 33.3%`,
`2/3 ≈ 66.7%`, `≈ +33.3 points`, `7/11 ≈ 63.6%`; `27/50 = 54%`, `17/25 = 68%`,
`+14 points`, `3/4 = 75%`; `1, 3, 7, 15, 31`/`day 31`/`50 min`,
`6, 12, 18, 24, 30`/`day 30`, `1, 1, 1, 1, 1`/`day 1`; `3/5 = 60%`,
`≈ 6.7 words`, `144 wpm`; `2/5 = 40%`, `22.5 words`, `96 wpm`), and every
figure in prose agreed with a recomputation: `383 × 60 / 95.75 = 240`,
`240 × 7/12 = 140`, `240 × 10/12 = 200`, `84 / 7 = 12` words per unit,
`4/6 − 2/6 = 1/3`, `68 − 54 = 14`, `75 − 81 = −6`, gaps `1, 2, 4, 8, 16`
summing to `1, 3, 7, 15, 31`, `377 × 60 / 94.25 = 240`, `40 / 6 ≈ 6.7`,
`90 / 4 = 22.5`, `240 × 6/10 = 144`, `240 × 4/10 = 96`. The passages' word
counts (383, 400, 381, 377) and idea-unit counts (12, 11, 11, 10) are what the
bodies say, and the published figures from Roediger and Karpicke (2006),
Experiment 1 (81/75 at five minutes, 54/68 at two days) are the published
ones.

The redesign the pre-authoring review asked for is in place and works: the
reread side takes no immediate test (the browser confirmed no question
appears after either reading of `P44`), the retrieve side is the free-recall
flow with ticked units, the due date is written to the log, the test is
offered once on the lesson page when due and announced by a banner on every
other `readkit` page, and the banner takes the warm-up's place on Spacing Your
Reviews exactly as that lesson's first paragraph says. The misconception for
Spacing Your Reviews is the fluency illusion the review asked for, not the
strawman it replaced.

The defects were local and are repaired below: one false instruction in
Retrieval Beats Rereading (the body told the reader to note today's unit count
and type it in on the day, when the kit writes it from the log entry), one
misconception paragraph whose figure did not match the preset it cited, one
ambiguous cross-reference ("the last lesson"), and one `how_to` sentence that
promised a due test on a timetable it could not guarantee. Nothing needs
splitting, merging or reordering.

## The voice, judged against §F

- **"You", warmly, about the reader's own numbers.** "The kit never reads your
  writing, so the count is exactly as honest as you are" (lesson 1); "Rereading
  also feels better. The second pass is smooth and every sentence is familiar,
  and that fluency is easy to take for knowing" (lesson 2); "Spaced reviews feel
  worse, because each one starts with something forgotten" (lesson 3). The
  target sentence of §F is met wherever the reader has a number of their own.
- **Try first, then explain.** Lesson 1's first `p` sends the reader to the
  drill in six sentences and the second starts from the ticking rule. Lesson 4
  does the same. Lessons 2 and 3 are correctly explanation-first, because their
  result arrives in two days or is a schedule.
- **Presented, not endorsed, both ways.** "A reader whose result goes the other
  way has not refuted the study, and the study has not refuted them" appears
  once, in lesson 2, as §C asks; the drill's recognition test is named as a
  gentler test than the study's free recall three times (body, `mistakes[0]`,
  `note`), which is once more than it needs. Expanding gaps are "one
  reasonable schedule, not a finding", with Karpicke and Roediger (2007) on
  the other side. Dunlosky's low rating of summarisation is stated and then
  the drill is shown to change the act it rates.
- **History as story with people in it**, once a lesson at most: Fleming's
  holiday and the policeman's urine are in the passage, not the lesson;
  Ebbinghaus testing his own memory on nonsense syllables is the lesson's one
  such paragraph. No light remark at all, which §F permits.
- **No promises.** No lesson says what the reader will retain. The `note` of
  each says what the measurement cannot settle: one passage, how strictly you
  tick, a recognition test, word lists in a laboratory.
- **Pointing forward by title.** Each body ends by naming the next lesson's
  title and its question; lesson 4 names the next course and its first lesson.

## Per-lesson findings

### `free-recall`

Teaches what §C says: the recall share, the recalled rate, and why recall is
lower than recognition. The drill does what the text says: Start, Done (the
passage hidden, confirmed), a textarea, Finished writing, the twelve units with
checkboxes, Score, then the six questions with the passage still hidden, then
the inputs filled (units 12, recalled 7, words 383, seconds to the
millisecond, summary words counted by the kit, 5 of 6) and one log entry of
kind `test` with `extra.units`, `extra.recalled`, `extra.summary: false`. The
`reWordsPerUnit` tile is on the page unpinned; the body's "12 words written
for each unit recalled" (84 / 7) matches what it prints for both presets.

The idea units are the passage's claims and the body quotes two of them
exactly ("the hump stores fat, not water; the droppings are dry enough to
burn"); quiz 3 quotes a third verbatim ("Its oval red blood cells keep flowing
when the blood thickens"). The `ul` on why recall scores lower is the right
depth for a first meeting with the distinction. Quiz 1's distractors are the
named errors (the rate before recall, 9 of 10 units, the words rather than the
rate); quiz 3's three "Yes" options are the three ways a reader talks
themself into a tick, each refuted in the `why`. The `standard` asks for both
figures and the reason.

One mismatch: `mistakes[0]` said "a reader who picks four of six right options
may … give back only about half of its ideas: the typical preset recalls 7 of
12", but the typical preset answers 5 of 6, and 7 of 12 is more than half.
Repaired to five of six and "little more than half", naming both of the
preset's figures.

### `retrieval-beats-rereading`

Teaches the delayed difference and the reversal, and the drill is the
redesign: the browser pass confirmed that side A reads twice with no question
(the Start button relabels to "Read it again"), that side B is the free-recall
flow on `P45` with eleven units, that both entries carry `due`, `title` and
`url` and the kind `condition`, that the banner "A delayed test is due: open
the test on “The Mould on the Plate” to take it" appears on another lesson's
page and hides its warm-up box, that the test asks the twelve questions with
neither passage shown, that it writes `delA`, `delB`, `total` **and B's
`units` and `recalled`** into the boxes, logs `delayed-test`, and is not
offered again after a reload. The tiles then read `1/3 ≈ 33.3%`,
`2/3 ≈ 66.7%`, `≈ +33.3 points`, `7/11 ≈ 63.6%` from the reader's own answers.

The body's second paragraph contradicted that last behaviour: "The last box,
the recall at the time, keeps the preset's count after the test: note the
number of units you ticked when you score the recall today, and type it in on
the day." The kit reads the count from side B's log entry (kit-report, recall
`delayed`: "it also writes B's `units` and `recalled` back into the boxes").
Repaired: the paragraph now says the test writes the delayed scores and
today's ticked units, so that every figure is the reader's own.

The published-shape preset is labelled and rounded as §C asks, with the
five-minute figures in the body and a `math` table, and the reader-example is
called "an illustration, not a study". The body says once that a reader whose
result goes the other way has not refuted the study. Quiz 2 tests the
reversal (who won at five minutes), quiz 3 the one-question sentence, quiz 4
the recognition-test caveat; each distractor was argued for and failed
("Its test comes sooner than the study's two days" is false by the `days: 2`
cfg). The `steps` are a usable two-day protocol on the reader's own texts,
including the swap of methods and order next time.

What the page does not do: the `reDelayed` line ("Both conditions are logged.
The delayed test is due on …") fills only when the page is opened, so after
the second side scores it stays hidden until a reload; the date reaches the
reader anyway through each side's own output ("The test on this passage is
due on 2026-10-27; this page will offer it then"), so the body's "when both
are logged, the page gives the date" holds. Recorded, not changed.

### `spacing-your-reviews`

Teaches a schedule as arithmetic, spaced against massed, and the unsettled
question of expanding gaps, with the sources §C names. The three presets are
explained in prose with their figures and the massed preset's trick (first
gap 1, multiplier 0) is explained in a parenthesis so that "all five on
day 1" is not a mystery. Quiz 1's first distractor lists the gaps instead of
the days, the error the `worked` example is built to prevent. Quiz 2's "The
massed reviews do better if the test is multiple choice" has no defence; the
`why` of quiz 3 reminds the reader that both schedules are spaced.

The warm-up is the hard-band pair `Q24`, `Q29` logged `practice`, as §C says,
and the body's first paragraph says what happens when a delayed test is due
(the banner takes the warm-up's place), which the browser confirmed on this
very page. The `steps` are a planning protocol whose second step is honestly
"a choice, not a formula".

One ambiguity: "A review of a reading is best done as the last lesson
suggests" could mean the previous lesson or the course's final one. The
suggestion is Retrieval Beats Rereading's; the sentence now names it.

### `notes-in-your-own-words`

Teaches coverage and cost and what a good summary leaves out, and makes the
Dunlosky point correctly: summarisation was rated low, and the drill changes
the act by hiding the passage so that the summary becomes retrieval. The
browser confirmed the summary variant asks for "a summary of three
sentences", ticks ten units, asks no questions, counts the words, and logs
`other` with `extra.summary: true`, which is what keeps it out of the
profile's recall row (the kit's fill excludes `extra.summary`). The `ul` of
what to leave out is tied to this passage's own units (the maple and the
birch, the word tannins, the layer of cells), which is the right way to make
an abstract rule concrete. Quiz 4's two "A" options and "Neither" are the
three ways to misread cost. The `worked` example's "less than a third as many
words on each idea and holds half as many ideas again" is right (6.7/22.5 ≈
0.30; 6 = 4 × 1.5).

## What the course teaches well

- **The honesty of self-scoring is taught, not assumed.** Lesson 1 spends a
  paragraph, a `mistakes` entry, a quiz item and a `steps` entry on the one
  rule that makes the number mean anything (tick only what the writing
  contains), and the course `how_to` repeats it first. The kit's refusal to
  score the writing (D.2) is turned into a lesson about recognition.
- **Immediate and delayed tests disagree** is stated as the lesson's spine in
  `concepts[1]` and then made the reader's own problem: the drill cannot be
  finished today, the course `how_to` says to start it early, and the
  Subject's banner brings the test back. No other course in the library
  carries a two-day experiment, and this one handles the return path.
- **Every figure is tied to a preset the reader can press.** Both presets of
  every lesson appear in a body paragraph with their figures and what they
  are figures of (§E.2), the `math` blocks repeat them in a form the voice
  reads well ("240 times 7 over 12 equals 140"), and the `worked` example is
  always the first preset by hand.
- **The log is used as a log.** Free recall as `test`, conditions as
  `condition`, the warm-up as `practice`, the summary as `other`: each kind is
  explained in the lesson that logs it ("logged as other, apart from the free
  recall from Free Recall, so a summary does not enter your recall tests"),
  which is what lets The Full Battery read the recall row later.

## Repairs made in this pass

In `content/reading/c7_remembering/part_a.py`: `free-recall` `mistakes[0]`
(five of six, both figures of the typical preset); `retrieval-beats-rereading`
body paragraph 2 (the delayed test writes today's ticked units; the
instruction to type them was removed); `spacing-your-reviews` the review
paragraph ("as Retrieval Beats Rereading suggests"). In `__init__.py`:
`how_to[1]` now says the test is waiting at Spacing Your Reviews when that
lesson is taken two or more days on. No preset, `expect`, slug, module, lab
key, mode, view, passage or log kind changed, and no §C entry needed
correcting. `scripts/preview_subject.py reading --course
reading-remembering-what-you-read` reports OK: 5 pages, 4 labs executed and
swept, 4 with pinned figures, 0 failing.

## Recommendations (not done)

- **A `due on` line that updates without a reload.** `reDelayed` is filled by
  an IIFE at load; a call to the same routine after each side's Score would
  show "due on <date>" the moment both conditions are logged. Kit change,
  `readkit_b.py` `DELAYED_UI_JS`; low priority, since each side's output
  already gives the date.
- **The two passages of the delayed comparison differ in familiarity.**
  Penicillin's story (`P44`, the reread side) is better known than the Eiffel
  Tower's permit (`P45`), so general knowledge helps the reread side on the
  delayed test, which works against the lesson's point rather than for it.
  The lesson names "content and difficulty" as a confound; a passage author
  could swap `P44` for something less famous. Passage change; not this
  course's file.
- **"Tends to show a smaller effect"** for the recognition test appears three
  times in lesson 2 (body, `mistakes[0]`, `note`). Once in the body and once
  in the `note` would do.
- **The course has no light remark** and does not need one, but §F allows one
  and the camel passage offers it.
