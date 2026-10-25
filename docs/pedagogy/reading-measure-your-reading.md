# Pedagogy assessment — Measure Your Reading (Reading Faster, course 1)

Formed from the five lesson dicts in `content/reading/c1_measure/part_a.py`
and the course dict in `content/reading/c1_measure/__init__.py`, the seven
passages their drills and warm-ups use (`P01`–`P05`, `P09`, `P10` in
`content/reading/passages/bank_a.py`, every paragraph and all forty-two
questions read), and the kit they render through (`readkit`, views
`drill/single`, `drill/compare`, `log/noise`, `log/gears`, `log/history`, as
`docs/reading/kit-report.md` records it), on branch `feat/reading-subject`
before the Subject is wired. The design authority is `docs/reading/PLAN.md`
§0 (the one question: the reader measures themself), §B (the median rule and
its one-in-five false-positive rate), the Course 1 entries of §C, §D.3, §E,
§F (the coach's voice) and §G; the pre-authoring pedagogy review in
`docs/reviews/reading-spec-pedagogy-review.md` was read for what it asked of
this course (findings 9, 10, 13, 14, 34, 36).

Every lesson was read in full before anything was changed. The course was
rendered with `scripts/preview_subject.py reading --course
reading-measure-your-reading`; every preset's tiles were read off the rendered
pages with `node scripts/labcheck.js --observe` (51 pinned strings on five
pages); every figure in prose was recomputed by hand, and the word and
character counts the lessons quote were recomputed from the passages with the
kit's own Python mirror (`readkit_core.passage_counts`). Then the course was
*done*: a Playwright script (`ped-c12-drills.js` in the session scratchpad)
opened the five pages in order in Chromium on one shared log and did what a
reader does — the `P01` drill with its six questions, the two-sided
comparison (the page put the fast reading first, since the log had one
entry), the two warm-ups of lesson 3 followed by "Use my baselines", the
warm-up and "Use my baseline median" of lesson 4, and the warm-up, "Show my
log" and the CSV export of lesson 5 — checking after each that the passage
was hidden while its questions were on screen, that one entry of the right
kind was written, and that the tiles agreed with the arithmetic. Lessons, in
course order: `words-per-minute`, `comprehension-and-effective-rate` |
`one-reading-is-one-measurement`, `typical-rates-and-reading-gears`,
`keeping-a-practice-log`. The bar marks the seam between the two modules,
Rate and comprehension | Reading your numbers. The course assumes fluent
reading and a division, and is judged against that.

## Verdict

The course teaches its subject, and a reader who finishes it has what §B
promises: three baseline readings and a test logged in the browser, with the
characters recorded so that the later unit conversion is possible, and the
rule by which every later number in the Subject will be read. The acts the
`standard` fields name are the acts the quizzes test: compute a rate in words
and in standard-length words from three numbers and say which reference uses
which unit (240 and 222 from 520 words, 2,880 characters and 130 seconds);
compute two effective rates and name the larger (250 against 200); give the
range of three baselines and the median of three tests and say whether the
Subject's rule is met (236–249, median 251, yes; 247 alone, no); convert a
rate to Carver's unit and name the nearest gear (286, rauding, 14 away); pick
the counted entries out of a mixed log and state the verdict. No objective is
"understand X". The `mistakes[0]` of every lesson is the §C misconception
("Most adults read about 300 words a minute, so I am slow"; "The faster
reading is the better reading"; "My rate on one test is my reading speed";
"There is one right speed, and faster is always better"; "Practice that feels
faster is faster"), each refuted with a figure from a preset on the page.

The measurement honesty the specification asked for is in the lessons, not
only in the spec. `P01` is scored (the body says "the next lesson is about
them, so for now look only at the rate"), so the baseline median is defined
from the first reading; the as-fast-as-you-can reading is logged `condition`
and the body says no verdict counts it; the one-in-four fact is taught as
arithmetic (each of four interchangeable readings is the top one time in
four) before the median-of-three rule, and the `note` adds the one-in-five
rate at which the rule itself is fooled, with the reason (the two fastest of
six readings are both tests). The page order the pedagogy review worried
about (finding 34) is handled: the two drill-first lessons' `summary` and
`concepts` state the question and the method, and the body's first paragraph
sends the reader to the drill. All 51 pinned tile strings matched the lab;
every figure in prose agreed with the lab or with a recomputation; `P01` has
491 words and 2,652 characters by the kit's rule, as the lesson says, and its
5.4 characters a word is the figure lesson 4 reuses.

In the browser the course behaves as the prose says, with two exceptions
now repaired. Lesson 2's body said the verdict tile would set rate B against
a range that "is a single reading" after one baseline; the kit prints "needs
two more baseline readings" (then "needs one more"), which is better than the
prose, and the prose now says so. And a reader who follows lesson 3 to
lesson 5 sees the same test reading judged twice, by its rate on one page
and by its effective rate on the other, and the two verdicts can differ (in
the run here, "above the baseline range once" at 276.6 words a minute became
"inside" at 184.4 understood words a minute); lesson 5 named the unit but not
the consequence, and now does. The remaining defects were a mistaken
comparison in one `mistakes` entry and a speech-engine habit of splitting
every `a × b/c = d` run in prose into three fragments, which is repaired in
the content with the library's backtick shorthand.

## The voice, judged against §F

- **"You", about the reader's own numbers.** "The drill counted the passage,
  491 words, and timed you from Start to Done to the millisecond"; "Your
  passage goes the other way"; "So when you see your own fourth reading,
  read it as what it is." Lesson 2's second paragraph is §F's exemplary
  paragraph, word for word, in the place §F put it.
- **Try first, then explain.** Lessons 1 and 2 open "Before you read on, do
  the drill below" and "Do the drill below before reading on", and the
  second paragraph of each starts from what the reader probably found. The
  three warm-up lessons open by naming the warm-up and its log kind.
- **History as people, once.** Rayner's 2016 review "published after Rayner's
  death in 2015" appears once, in lesson 2, where it explains why the
  questions were written to fail a guess. Brysbaert and Carver are named with
  years and with what each measured. Nothing is quoted at length.
- **Presented, not endorsed.** Lesson 2 says in the lesson's voice that a
  reader whose fast reading came out ahead "has not refuted the usual
  result, and the usual result has not refuted" them; lesson 4 says Carver's
  figures are for college students and that the nearest gear is "a
  comparison of numbers, not a description of what you were doing".
- **No promises, no slang, no anecdote.** None found. The one light remark
  is "a fast reader from a fast page-turner", which is §F's own.
- **Every `note` names what the measurement cannot settle**, and every body
  ends by pointing to the next lesson by title; lesson 5 points to Guided
  Practice by title and names its first three things.

What later courses should copy from here: the first paragraph that names the
passage by title and says exactly which buttons to press; the paragraph
that walks through each preset by name with its arithmetic; the `steps` that
are a protocol for another day, not a summary (lesson 1's "Stop the clock at
the last word … time spent on the questions does not" is the right grain).

## What the course teaches well

- **One idea per lesson, in the order a measurement needs them.** Rate
  (lesson 1) before comprehension (2), both before noise (3), noise before
  the reference figures (4), and the log that keeps the kinds apart last
  (5). Each lesson uses only what came before: lesson 3's "Use my baselines"
  draws on readings lessons 1 and 2 logged, lesson 4's median on lesson 3's
  three, and lesson 5 reads the four sessions the course has produced. In
  the browser the log page showed exactly four counted sessions after the
  course, as the body predicts.
- **The unit lesson is honest about what it does to the reader's number.**
  Lesson 4 says in advance that on this course's short-worded passages the
  reader's standard rate will likely land nearer learning than rauding
  ("below about 278 words a minute, 5.4 characters a word puts you under 250
  standard words"), and that this is the unit at work. The browser confirmed
  the shape: a 245.5 words-a-minute median became 223.7 standard words and
  the nearest gear was learning, against the average 103.2%.
- **The chance arithmetic is taught as a counting argument the reader can
  check**, not as a statistic: four interchangeable readings, each equally
  likely to be the fastest; a median that "moves only when at least two of
  the three move". Quiz 4 of lesson 3 asks for the reason and offers "Carver
  found that rates vary by about a quarter" as the distractor that a reader
  who memorised the number would pick.
- **Every preset is in the prose with its figures and what it is a figure
  of.** The `speed-only` log is the course's best teaching instrument: three
  tests at 288, 354 and 488 words a minute with 5, 4 and 3 right come to 240,
  236 and 244 understood words a minute, "inside the baseline range", and the
  mistake it refutes ("Practice that feels faster is faster") is the one the
  Daily Drill will tempt the reader into.
- **Protocols, not summaries.** Lesson 2's fourth step, "Discount one
  question … call it a tie and repeat the comparison another day, in the
  other order", and lesson 5's "Do not repeat a drill to replace a bad
  reading" are the rules a reader needs on day thirty, and they are written
  as rules.
- **The quizzes test the lesson's act with one defensible answer.** Every
  distractor was argued for: 400 from reading 150 seconds as 1.5 minutes,
  278 from dividing by 5.4 instead of multiplying, "It fell by a third" for
  5/6 to 4/6, "It replaces the lowest baseline" for a pacer reading, "No
  verdict until a fourth test". None could be defended.

## What it taught badly, or said wrongly

### Prose that disagreed with the lab

- **`comprehension-and-effective-rate`, body:** "The last tile sets rate B
  against your baseline range, and with one baseline so far that range is a
  single reading: leave the tile until One Reading Is One Measurement has
  given you three." In the browser the tile reads "needs two more baseline
  readings" at load and "needs one more baseline reading" once reading A is
  scored, and the note under the drill says "From your log: 1 baseline
  reading; a verdict needs three." Now: "The last tile will set rate B
  against your baseline range once your log holds three baselines; until
  then it says how many more it needs, and One Reading Is One Measurement
  supplies them."
- **`keeping-a-practice-log`, body:** the sentence that "Lights on the
  Coast" was "set against the range by its rate" in lesson 3 stopped there,
  and a reader whose test was above the range on one page and inside it on
  the next would not know why. Two sentences added: the log scores by
  effective rate, so the two pages can give one reading different verdicts,
  and a fast reading with a question wrong is the case.

### A comparison that was not true

- **`one-reading-is-one-measurement`, `mistakes[0]`:** "the tight reader's 13
  is still more than many claimed gains." The speed-reading tradition's
  claimed gains are hundreds of words a minute, so a 13-word range is not
  more than them, and the research's modest gains are not "claimed". Now:
  "even the tight reader's 13 is wider than the difference most comparisons
  in this Subject will show", which is what the lesson needs the sentence
  for (lesson 2's presets differ by 8 and 48 understood words a minute, and
  Guided Practice's by 8 and 48 again).

### Speech

Every `data-say` on the six rendered pages was read. The math blocks and key
lines read well ("491 times 60 over 120 equals 245.5", "range, equals 238 to
251. one test, equals 262, above once"). But the speech engine's island
finder splits every inline run of the shape `320 × 5/6 ≈ 266.7` into "320
times", a bare "5/6" left to the voice, and "is approximately 266.7"; nine
such runs were in the course's prose, quiz explanations and worked
paragraphs, and two bare formulas (`rate × right / asked`, `rate ×
comprehension`) were read as the one word "times". All are now in the
library's backtick shorthand and read as one run ("320 times 5 over 6 is
approximately 266.7"; "rate times right over asked"). Written math in the
`steps` was already clean. This is the same engine habit the Capital
assessment recorded for `n·(n − 1)/2` in steps; a `speech.py` rule for
`a/b` after `×` belongs to the chrome-renderer tier and is recorded below.

## Can a reader with no technique follow the five lessons?

Yes. Lesson 1 asks for one reading and one division; lesson 2 for two
readings and one multiplication, and it says before the drill that the
second reading is the different one ("in the box labelled 'As fast as you
can'"), so the reader is not surprised when the page puts it first. Lesson 3
is the one that could lose a reader, because it asks for two more readings
before anything is explained; it earns them by saying what each is for
("The first is logged as a baseline and the second as a test … that one is
the experiment") and by making the explanation about the reader's own
fourth reading. The two reference lessons are light, and are meant to be.
The course's `how_to` protects the reader in the right places: do the drill
before the explanation, never practise on a passage already read, keep the
browser you started in.

## Repairs made in this pass

In `content/reading/c1_measure/part_a.py`: `words-per-minute` `steps[3]`
(backticks); `comprehension-and-effective-rate` the worth-it paragraph
(backticks), the verdict-tile paragraph (reworded to the kit's behaviour),
`steps[2]`, `worked.after`, quiz 1 and 2 `why` (backticks);
`one-reading-is-one-measurement` `mistakes[0]` (the comparison);
`keeping-a-practice-log` the four-sessions paragraph (the two verdicts),
`concepts[1]` and quiz 2 `why` (backticks). No preset, `expect`, slug,
module, lab key, mode, view, passage or `__init__.py` field changed, and no
§C entry needed correcting: every instance the lessons carry is the one §C
records.

`scripts/preview_subject.py reading --course reading-measure-your-reading`
reports OK after the changes: 6 pages, every lab executes and survives the
sweep, 5 pages with pinned figures, 0 failing. `node scripts/labcheck.js
--observe` on the five pages shows every preset's tiles as the lessons
describe them. The Playwright pass over the five lessons reports 0 failing
checks and no console or page errors, before and after the edits; a second
pass at 360 px found no horizontal overflow. `python3 -m unittest
tests.test_speech` passes.

## Remaining issues and recommendations

- **The kit's one-question sentence reads "One question is is
  approximately 16.7 points."** The sentence `One question is ≈ 16.7 points;
  a one-question difference is not a result.` is the kit's (D.3.1), added to
  every panel with questions, and the voice reads `≈` as "is approximately"
  after the word "is". The course's own prose no longer has the shape (it
  says "about 16.7 points"), but the panel sentence does on four of the five
  pages. Kit tier: drop the "is" or write "about".
- **`a × b/c = d` in prose.** The speech engine's islands stop at a fraction
  after `×`. Worked around here with backticks; a rule in `speech.py` would
  fix it for the other six reading courses, which write the same shape in
  prose (chrome-renderer tier).
- **`lgMean` sits beside a lesson that argues against it.** `log/noise`
  prints "Baseline mean" first (kit deviation 12) while `mistakes[2]` of the
  same lesson says a test beside the mean "says even less than a test
  beside the range". The body mentions the mean once, neutrally. Either the
  tile goes (kit) or the body should say in one clause why it is shown.
  Taste; not changed.
- **Lesson 2's `key` states the expected result.** `480 × 2/6 = 160 < 240 ×
  6/6 = 240` is above the body of a drill-first lesson (pedagogy review
  finding 34). It is the preset's arithmetic rather than a prediction about
  the reader, and the `summary` and `concepts` are clean, so it was left;
  `comprehension = right / asked` repeated with the preset's numbers in the
  `worked` block instead would be stricter.
- **`P05`'s first question** ("What problem did Fresnel's design solve?") is
  keyed to the lens's thickness, and the passage's third paragraph opens "A
  strong light, however, raised a new problem", which the second option
  names. A careful reader answers it from the second paragraph, so it stands,
  but it is the one question in the course's seven passages that two
  readers could argue about. Passages are not this pass's to change.
- **The baseline kind is set in only three places** (`P01`, `P02`, `P04`),
  and nothing later in the Subject logs a baseline, so the range a reader
  carries for eight courses is three readings from one day. The §B remark
  that "a fourth baseline widens the range" has no lesson that takes one.
  A fourth baseline warm-up somewhere in Course 2 would be cheap; recorded
  for the orchestrator, not done (it is another course's file).
