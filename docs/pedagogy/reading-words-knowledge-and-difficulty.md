# Pedagogy assessment — Words, Knowledge and Difficulty (Reading Faster, course 6)

Formed from the five lesson dicts in `content/reading/c6_difficulty/`
(`part_a.py`, all five lessons: two in the module "Difficulty", three in
"Knowledge"; `__init__.py`, the course dict), the nine passages their drills
and warm-ups serve (`P38`–`P42` in `content/reading/passages/bank_b.py`,
`P01` in `bank_a.py`, `Q22`, `Q23` and `Q30` in `pool.py`), and the kit they
render through (`scripts/mathpath/labs/readkit.py` and `readkit_b.py`, modes
`drill` and `text`; views `compare`, `readability`, `coverage`, `volume`),
on branch `feat/reading-subject` before the Subject was wired. The design
authority is `docs/reading/PLAN.md` §0, §B, the Course 6 entries in §C, §D as
the kit built it (`docs/reading/kit-report.md`), §E and §F.

Every lesson and every passage was read in full before anything was changed.
The course was rendered with `python3 scripts/preview_subject.py reading
--course reading-words-knowledge-and-difficulty`; every preset's tiles on the
five pages were read off the rendered page with `node scripts/labcheck.js
--observe` (fifteen presets, 44 pinned strings); every figure in prose was
recomputed by hand, and every count over a passage (words, sentences,
syllables, Reading Ease, grade) by the kit's Python mirror in
`readkit_core`, which is the rule the page uses. Five drills were done end
to end in Chromium through Playwright on a controlled clock against the
served render: the easy-against-hard compare (395 words in 79 s, 6 of 6; 391
in 138 s, 5 of 6), the coverage marking of the heraldry passage (twenty
words marked, one unmarked, "Count my marks"), the warm-up on Endgame at the
Rosedal followed by the readability presets and a count of pasted text, and
the volume lesson's warm-up twice over (the violin passage, then the marrow
story on the second visit) followed by the calculator on fresh inputs. Every
`data-say` on the five pages was read. Lessons, in course order:
`your-rate-on-hard-text`, `measuring-difficulty` | `unknown-words-and-coverage`,
`what-you-already-know`, `how-much-you-read`. The bar marks the seam between
the two modules. The course assumes Courses 1 to 5 and is judged against
that.

## Verdict

The course teaches what §C says it teaches, and it keeps the promise the
pre-authoring review asked for: the reader measures the drop on their own
easy and hard reading before any formula is named, and the formula is then
computed on the two passages they have just read. A reader who finishes it
can compute the ratio of two rates and both effective rates and say which
of Carver's two patterns a pair of readings shows; compute Flesch Reading
Ease and the Flesch–Kincaid grade by hand from three counts and name two
things the formulas cannot see; turn a count of unknown tokens into coverage
and "one unknown in every N" and say what Hu and Nation found at 95% and for
whom; compare a familiar and an unfamiliar topic at the same grade in
effective rates; and compute a year of reading and the rate gain that
equals ten more minutes. Those are the acts the `standard` fields name and
the quizzes measure. The `mistakes[0]` of every lesson is the §C
misconception, each refuted with the lesson's own figure: a ratio of 96%
beside an effective rate that fell from 250 to 120; a grade of 6 for short
words about an unmet idea; one unknown in every 20 against one in every 50;
an effective rate of 240 on a suitcase and 150 on a slide at nearly the same
grade; 2,737,500 words a year from ten more minutes or from 375 words a
minute, against 2,190,000 from a gain to 300. All 44 pinned tile strings
matched the lab, and every figure in prose agreed with the lab or with a
recomputation: the kit counts The Octopus at 395 words, 21 sentences and 504
syllables (ease 79.798, grade 6.802), the continents passage at 391, 16 and
775 (14.346, 17.329), the church clock at 491, 21 and 655 (70.246, 9.270),
the suitcase at grade 9.364 and the Gram stain at 8.866, all as the lessons
say to one decimal.

The voice is §F's and the research is presented at strength and then
bounded: Carver's constancy with his units, Rayner's fixations and
regressions, Hu and Nation's learners against Laufer and Ravenhorst-Kalovski
and Schmitt, Jiang and Grabe ("they disagree about whether there is a
threshold at all"), Recht and Leslie's recall measure and young readers,
Anderson, Wilson and Fielding's diaries as a correlation. Both compare
lessons name the two confounds and say once that a contrary result refutes
nothing. The `steps` are protocols for repeating each measurement on the
reader's own texts, and every lesson ends on the Daily Drill with the
course's own instruction attached: find the hold target again when the pool
reaches its hard passages.

The defects were small and local: one sentence in `measuring-difficulty`
claimed every passage in the Subject sits inside the grade bands it names
when the three scanned documents (a timetable, a visitor guide and a book's
front matter) do not; and the same lesson's definition and its third step
wrote the two formulas with bracketed quotients that the speech engine split
into fragments ("negative 84.6 times"). Both are repaired below. Nothing
needs splitting, merging or reordering.

## The voice, judged against §F

- **"You", about the reader's numbers.** "Now put your two readings side by
  side and look at two things, not one: the rates, and the scores"
  (`your-rate-on-hard-text`); "Now read your own result against them. If your
  coverage of the heraldry passage was in the low nineties, you met an
  unknown word in almost every sentence, and you will probably have felt it"
  (`unknown-words-and-coverage`); "the minutes a day you actually read, not
  the minutes you mean to" (`how-much-you-read`).
- **Try first, then explain.** `your-rate-on-hard-text` is the course's
  drill-first lesson. Its `summary` is a question ("Does your rate stay the
  same when the text gets harder, or does your comprehension give way
  instead?"), its `concepts` give the two patterns without saying which the
  reader will show, and the first `p` sends them to the drill. The course
  `how_to` says the explanations "are written for a reader who has just seen
  their own numbers", which is true of every lesson here.
- **Presented, not endorsed, both ways.** Carver is given his finding and
  his units; Rayner et al. 2016 is "a review"; Hu and Nation's 98% is
  followed by the two studies that qualify it and the sentence "for a fluent
  native reader the figures are an extrapolation"; Recht and Leslie
  "measured recall, not speed, and their readers were young"; the volume
  evidence is "correlational or rest[s] on estimates". The lesson on volume
  still says, in its own voice, that more minutes is "the larger lever", and
  earns it with arithmetic rather than with the correlation.
- **The history as people, once a lesson.** Flesch in 1948 and Kincaid's
  Navy report in 1975; Wegener and the magnetic stripes are the passage's;
  Hu and Nation's learners in New Zealand. No Evelyn Wood, correctly.
- **No promises.** "Reading faster is worth training, and this Subject trains
  it every day. Reading more is the larger lever" is the nearest the course
  comes, and it is a comparison, not a promise.
- **One light remark.** "A grade of 8.73 sits in this Subject's standard
  band" is the closest; the course is drier than Course 5 and that suits a
  course about counting.
- **The limit admitted.** Every `note` names what the measurement cannot
  settle: "one pair of readings on one day … differ in topic as well as
  difficulty"; "another program will give slightly different scores";
  "Your marks are a judgement"; "Recht and Leslie measured recall in young
  readers; your drill measures one adult's rate and score on two texts";
  "for an adult reader they suggest a direction, not a size".
- **Pointing forward by title.** Every body ends with the next lesson's
  title; `how-much-you-read` ends with the next course by title and its
  question.
- **"Your reading speed"** appears once, as the title of the §C
  misconception in `your-rate-on-hard-text` ("Treating your reading speed as
  one number"), which is the belief being named and not a measurement
  printed. Acceptable under §D.2 and §0.

## What the course teaches well

- **The order is right, and the order is the argument.** Lesson 1 measures
  the drop; lesson 2 names the formula that would have predicted it and
  computes it on the same two passages ("about a third longer" sentences,
  "more than half as many syllables again": 24.4 against 18.8 words a
  sentence, 1.98 against 1.28 syllables a word, both as the kit counts
  them); lesson 3 measures the first thing the formula cannot see, lesson 4
  the second, lesson 5 the lever that moves both. The closing paragraph of
  `how-much-you-read` says the order out loud.
- **Two patterns, not one.** `your-rate-on-hard-text` is built on the
  distinction a single rate cannot make: big-drop (300 → 170, 17/30 ≈ 56.7%,
  5 of 6, effective ≈ 141.7) against held-rate (250 → 240, 24/25 = 96%, 3 of
  6, effective 120). The quiz's first item gives the held-rate pair and asks
  what it shows; the distractor "untroubled by difficulty" is exactly the
  reading of the ratio alone that the lesson teaches against.
- **The counting rule is stated and its approximation admitted.** The body
  gives the kit's word, sentence and syllable rules in words, says the
  syllable rule "miscounts some words", and the third `mistakes` entry warns
  against the second decimal. The `txSyllables` tile carries "(by the
  rule)". A reader who counts a 100-word sample by hand and gets 139
  syllables will not think the lab is wrong.
- **The coverage lesson measures what the formula misses on a text that
  shows it.** The heraldry passage is at grade 15.7 by the kit's count and
  carries its own vocabulary (or, argent, gules, fess, pale, bend, saltire,
  rampant, passant, dexter, sinister, impaled), so most readers will mark
  something; the body tells them what either result means. The drill is
  untimed and asks no questions, and the body says why in one sentence (the
  marking interrupts the reading). The token rule is taught three times (a
  concept, a quiz item, a mistake), which is the right weight for the one
  counting error readers make.
- **The matched pair in lesson 4 is matched by the kit's own count.** 385
  words in 16 sentences at 9.364 against 375 in 18 at 8.866; the formula
  does call the Gram stain slightly easier, as the body says, and both
  passages are step-by-step procedures. The expert preset is the right
  second instance: the same reader's suitcase, a different reader's slide,
  25/24 ≈ 104.2%.
- **The arithmetic is right.** 395 × 60 / 79 = 300, 391 × 60 / 138 = 170,
  170 × 5/6 ≈ 141.7; 395 × 60 / 94.8 = 250, 391 × 60 / 97.75 = 240; 206.835
  − 20.3 − 118.44 = 68.095 and 7.8 + 16.52 − 15.59 = 8.73; 0.39 × 20 + 11.8 ×
  1.5 − 15.59 = 9.91 and 84.6 × 0.3 = 25.38; 490/500 = 49/50, 500/10 = 50,
  361/380 = 19/20, 380/19 = 20; 385 × 60 / 96.25 = 240, 375 × 60 / 100 = 225,
  × 4/6 = 150, 150/240 = 5/8, 375 × 60 / 90 = 250; 20 × 250 × 365 =
  1,825,000, 1,825,000 / 90,000 ≈ 20.3, 912,500 ≈ 10.1 books, 365,000 ≈ 4.1
  books, 250 × 30/20 = 375, 15 × 240 × 365 = 1,314,000. The browser's
  calculator gave 2,098,750 words and ≈ 23.3 books for 25 minutes at 230.
- **Worked example, prediction, independent practice.** Every `worked` is a
  preset by hand; every quiz asks the same act on a fresh instance (260 and
  225 with 6 and 4 of 6; 200 words, 10 sentences, 300 syllables; 19 unknown in
  380; 15 minutes at 240) with the named error as a distractor (the ratio of
  the times, 79/138; 8.73 for the wrong syllable count; 361/380 with "one in
  every 19"; 225/260 for the rates without the scores; 87,600 for forgetting
  the minutes).
- **The drills do what the text says.** Verified in Chromium: the compare
  alternated from `AB` on a fresh log and logged both sides as `test` with
  the passage, words, milliseconds and score; the coverage drill's Done
  button reads "Count my marks", its intro says "Nothing is timed", a second
  click unmarks, and 19 of 380 gave `19/20 = 95%` and `one unknown in every
  20 tokens`, logged `other`; the readability warm-up served Q22 and logged
  `practice`, the `continents` preset wrote 391, 16 and 775 into the boxes,
  and a pasted text of 11 words in 2 sentences was counted; the volume
  warm-up served Q23 and, once Q23 was in the log, Q30, as the body says.
  No console or page errors on any page.
- **Every compare lesson meets §C's preamble.** Both `note`s name the two
  confounds, both bodies say once that a contrary result refutes nothing,
  and both `panel_intro`s end with the one-question sentence.
- **The Daily Drill step carries the course's own point.** The shared
  `DAILY` step tells the reader to find their hold target again when the
  pool reaches its hard passages, "and that is this course's subject measured
  on your own practice", which is the pre-authoring review's finding 7 done.

## What it taught badly, or said wrongly

### Prose that overstated what the counts show

- **`measuring-difficulty`, body:** "The passages in this Subject were
  sorted into bands with exactly these counts: easy at grades 5 to 7,
  standard at 8 to 11, hard at 13 and above." Run over the whole bank by the
  kit's rule, every timed reading passage sits in its band, but the three
  scanned documents do not: the ferry timetable is at grade 6.97, the museum
  guide at 7.89 and the book's front matter at 11.98, all labelled
  `standard`. They are not prose and nobody reads them for time, so the
  claim was true of what it meant and false as written. Now "The passages
  you read for time in this Subject were sorted into bands by exactly these
  counts".

### Speech

Every math run on the five pages was read from `data-say`. The key lines
read well: "ease equals 206.835 minus 1.015 times W over S minus 84.6 times
Y over W", "rate ratio equals hard rate over easy rate", "one in every N
equals tokens over unknown". Two places did not:

- **`measuring-difficulty`, `def`:** "206.835 − 1.015 × (W/S) − 84.6 ×
  (Y/W)" was split by the islands pattern into "206.835 minus 1.015 times",
  then the bracketed quotient as text, then "negative 84.6 times". The
  definition now gives both formulas in words ("206.835, less 1.015 times
  the words per sentence, less 84.6 times the syllables per word") and
  points to the key lines for the symbols, which read correctly as one run.
- **`measuring-difficulty`, `steps[2]`:** the same two formulas with
  bracketed words were split the same way. Now in words. The page's math
  runs went from eleven, seven of them fragments, to three whole ones.

### Quiz

Every distractor on the course was argued for and could not be defended.
The closest were `unknown-words-and-coverage` quiz 1's "361/380 = 95%, one
unknown in every 19 tokens" (the coverage is right and the density wrong,
and the `why` says so) and `your-rate-on-hard-text` quiz 3's "exactly twice
as long" (no fixed factor converts one kind of text into another, as the
`why` says). Nothing changed.

### Cross-references

Lessons are cited by title ("Measure Your Reading", "How the Eyes Read",
"Measuring Difficulty", "Unknown Words and Coverage", "What You Already
Know", "How Much You Read", "The Daily Drill"), each as the lesson or course
carries it; the next course by its §B title, Remembering What You Read. The
church clock is correctly placed as "the first passage you timed in Measure
Your Reading". No lesson is cited by number.

## Can a reader with Courses 1 to 5 follow it?

Yes. Lesson 1 needs only the rate, comprehension and effective rate of
Course 1 and the word "gear" from Course 5, and gives Carver's finding in
plain terms before his vocabulary. Lesson 2 is the one with new arithmetic,
and it is worked by hand on round numbers (100, 5, 140) before the passages'
counts appear, with the two scales' directions given their own concept and
their own mistake. Lesson 3's one idea, tokens not words, is given three
times. Lesson 4 adds nothing new to compute and says so ("The comparison is
in effective rates"). Lesson 5 is one multiplication and a comparison. The
place a reader will slow down is the readability definition, which is why
the `worked` example precedes the passages and the `steps` repeat the two
averages first; in words now, it reads aloud as well.

## Repairs made in this pass

In `content/reading/c6_difficulty/part_a.py`: `measuring-difficulty` the
bands sentence, the `def` block (both formulas in words, with the key lines
named for the symbols) and `steps[2]` (the same). No preset, `expect`, slug,
module, lab mode, view, passage or instance changed; every instance the
lessons carry is the one §C records. `scripts/preview_subject.py reading
--course reading-words-knowledge-and-difficulty` reports OK after the
changes: 5 pages executed and swept, 5 with pinned figures, 0 failing.

## Remaining issues and recommendations

- **Hard and unfamiliar readings enter the effective-rate curve as `test`.**
  §C logs both sides of `your-rate-on-hard-text` and of
  `what-you-already-know` as `test`, so the continents passage (grade 17.3)
  and the Gram stain become two of the reader's "last three tests" in
  `log/history`, `log/noise` and The Full Battery, where every baseline was
  standard text. The course's own thesis is that a rate is a rate on a kind
  of text; its drills put a hard-text rate into a standard-text median.
  Either the hard and unfamiliar sides log `condition` (the kit's compare
  default, listed but not charted), or Reading Your Curve and The Full
  Battery say that two tests in the log are on hard text. Cross-course and
  §C; recorded, not changed.
- **`txSyllables` is not pinned** on `measuring-difficulty`, although the
  body quotes 504 and 775 syllables and the mirror confirms them. Pinning
  `"txSyllables": "504 (by the rule)"` on `octopus` and `"775 (by the
  rule)"` on `continents` would make the body's counts a checked claim.
  Taste; recorded.
- **The sentence rule in prose is narrower than the kit's.** The body says a
  sentence ends at a stop "followed by a space"; the kit also accepts closing
  quotes or brackets after the mark and the end of the text. No passage here
  differs under the two rules; recorded.
- **The coverage drill's keyboard operation** (Tab or arrow keys, Enter or
  Space) is described in the body and the slot intro but was exercised here
  only by mouse; the kit report records it as verified in its own browser
  run.
