# Pedagogy assessment — The Inner Voice and Flashing Words (Reading Faster, course 4)

Formed from the six lesson dicts in `content/reading/c4_inner_voice/part_a.py`
and the course dict in `content/reading/c4_inner_voice/__init__.py`, the ten
passages their drills and warm-up use (`P25`–`P31` from
`content/reading/passages/bank_b.py`, `P19` and `P20` from `bank_a.py`, `Q20`
from `pool.py`), and the kit they render through
(`scripts/mathpath/labs/readkit*.py`: `drill/compare` with the `aloud`,
`suppress`, `rsvp`, `phrases` and `pacer` sides and `ratioOf: wpm`,
`drill/single` with `rsvp`, `eye/required` with `claim`, and the `warmup`
slot), on branch `feat/reading-subject` before the Subject was wired. The
design authority is `docs/reading/PLAN.md` §0, §B, the Course 4 entries in §C,
§D.3 as recorded in `docs/reading/kit-report.md` (items 12 and 13: the 600 wpm
cap, the aloud fallback and the suppression tick), §E and §F, read beside
`docs/reviews/reading-spec-pedagogy-review.md`, whose findings 19, 26, 27 and
31 shaped this course.

Every lesson was read in full before anything was changed. The course was
rendered with `python3 scripts/preview_subject.py reading --course
reading-inner-voice-and-flashing-words`; every pinned tile on the six pages
(47 strings) was read off the rendered page with `node scripts/labcheck.js
--observe`; every figure in prose was recomputed by hand (both ratios, every
rate and effective rate in the eight compare presets, the three times per
word, the mean time per phrase from 438 words and 127 phrases, the three
glance figures and three book times); every passage was counted by the kit's
own word rule, its phrase rule and its readability formula; and the drills
were done in Chromium through Playwright against the served preview on a
controlled clock: the aloud fallback and then a real aloud reading and the
silent reading with three baselines in the log; the normal and counting pair
with the "kept counting" tick; the word stream at the baseline median after
pressing "Use my baseline median", and the refusal at 700 wpm; the word
stream against the phrase stream; the pacer against the stream at 300; and
the `Q20` warm-up. Fifty-five checks across both courses, none failing, no
console or page error. Lessons, in course order: `the-inner-voice`,
`silencing-the-inner-voice` | `one-word-at-a-time`, `reading-in-phrases`,
`rsvp-without-looking-back`, `testing-a-speed-claim`. The bar marks the seam
between the two modules.

## Verdict

The course teaches what §C says it teaches, and each drill is the experiment
its text describes: every one of the tradition's techniques is tried against
a control at one rate, on the reader's own reading, and reported as an
effective rate beside a rate. A reader who finishes it can divide a silent
rate by an aloud rate and say what a ratio above 1 does to the advice that
the inner voice must go; score a suppression pair as two effective rates and
a difference and say why a reading in which the counting lapsed is void;
compute the milliseconds a word is on screen at a rate and explain, with 30
of 255 ms, why removing eye movements saves a tenth; compute the time a
phrase is shown and say what the word-against-phrase pair isolates and what it
cannot; say what a garden-path question tests and why a stream cannot let
the reader repair it; and follow any speed claim through three computations
to the test that would settle it. Those are the acts the `standard` fields
name, each written as "Finish when you can…" with a pass level, and the
quizzes ask them on fresh instances.

The reader also leaves with a log. The silent reading of lesson 1 is a
`test`, the aloud reading `other`, the suppression pair and every streamed
reading `condition`, and the `Q20` warm-up `practice`, exactly as §C assigns
them, so the curve the Subject promises is not polluted by a stream at 600
wpm; each lesson's last step is the Daily Drill. The `steps` are protocols
for another day, not summaries ("Choose two fresh, easy passages", "Read the
first aloud at a natural pace", "Divide the silent rate by the aloud rate";
"Set one rate for both streams", "Stream a fresh passage one word at a time",
"Stream a matched passage one phrase at a time"). One Word at a Time, the
course's drill-first lesson, keeps its `summary`, `one_line` and `concepts` to
the question and the method and never states the expected result.

The arithmetic is right. All 47 pinned strings matched the page, and every
figure in prose agreed with the lab or a recomputation (`238/183 ≈ 130.1%`,
`16/9 ≈ 177.8%`; `≈ 174.7` and `≈ −70.3` as pinned, then `≈ 178.7` and
`≈ −71.3` after the repair below; `240`, `120`, `100` ms; `≈ 11.8%`;
`≈ 827.7` ms and `960`; `300 × 4/6 = 200`; `19.125`, `38.25`, `267.75`;
`≈ 378` minutes, `120`, `60`). The garden paths are where §C says: "The
guests served the soup first complained that it was cold" in `P30`, with its
question 2, and "The ferryman rowed across the river waved a red flag" in
`P31`, with its question 3, and `P31` has no later cue that gives the answer
away. `P20` is marked into 127 phrases of two to five words, as the concept
says.

One defect was more than local, and is repaired below: the `typical` preset
of Silencing the Inner Voice gave its reader 392 and 393 words on passages
that the kit counts at 409 and 402, so a reader who did the drill saw a words
box that disagreed with the preset and the prose by seventeen words on one
side and nine on the other, in a lesson whose whole point is a matched pair.
The remaining repairs are a sentence each. Nothing needs splitting, merging
or reordering within the URL space the course has.

## The voice, judged against §F

- **"You", about the reader's own numbers.** "Now read your own pair. A ratio
  above 1 means you already read silently faster than you can speak" (lesson
  1); "If the counting reading's effective rate is lower, you have seen in
  your own numbers the cost the studies describe" (lesson 2); "If your
  comprehension in the stream matched your baselines, the stream at your own
  rate cost you little on this story" (lesson 3). The §C sentence about a
  result that goes the other way is in every compare lesson once, and in the
  single-reading lesson as "one reading of one passage".
- **Try first, then explain.** Lesson 3 opens "Do the drill before you read
  on" and its second paragraph starts from what the reader probably found
  ("Many readers find the first few lines strange and then settle into the
  rhythm"). Lessons 1, 2, 4, 5 and 6 send the reader to the drill or the
  warm-up in their first paragraph.
- **The tradition at its strongest first.** "The advice you are testing is
  old and widely repeated… Readers who practise this often say the voice
  grows fainter as they speed up, and the experience is real enough to take
  seriously" (lesson 1); "If the voice were only a brake, this should make
  reading faster and cost nothing" (lesson 2); "the stream can feel
  effortless" (lesson 3); "The claims are made at their strongest" (lesson
  6). The research follows with its limits named: "the studies are few and
  small", "suppression also adds a second task", "the drill copies the
  display, not their procedure", "the lesson takes only the design of Just,
  Carpenter and Masson's study, not its figures".
- **History with people in it, once a lesson where it explains something.**
  Spritz and "the apps that made the display famous in 2014" in lesson 3;
  Hardyck and Petrinovich's throat electrodes in lesson 2; Carver going
  "looking for the world's best readers" in lesson 6.
- **One light remark.** Woody Allen's *War and Peace* line, once, in lesson
  6, where §F and §C put it. Nothing at the reader's expense.
- **No promises; no slang; no first person; no "let's".** None found.
- **The `note` as the limit, and pointing forward by title.** Every `note`
  names the two confounds of a two-reading comparison and the lab's distance
  from the study it copies; every body ends with the next lesson's title and
  question, and lesson 6 ends with the next course by its §B title and "the
  honest version of reading a book in an hour".

## What the course teaches well

- **A control for every technique, at one rate.** Aloud against silent (a
  ratio of rates, with the body saying why not effective rates); normal
  against counting on a matched pair; word stream against phrase stream,
  "both at one rate in the same box, and neither lets you look back"; pacer
  against stream with the page left on screen. Lesson 4's `concepts[2]` and
  quiz 2 make the design explicit: what the pair isolates and what it cannot.
- **The effective rate as the judge, and the rate shown beside it.** Lesson 2
  gives a reader who went 18 words a minute faster and lost two questions and
  says "the product says the trade was a bad one"; lesson 3's `at-500` preset
  is allowed to come out *higher* in effective rate than the baseline reading
  (250 against 208.3) and the body says so and says why that is a choice
  about purpose, pointing to the skimming course, rather than hiding it.
- **The misconceptions are the ones readers arrive with, each refuted with a
  figure.** "The voice limits you to speaking speed" by 238 against 183;
  "eliminating subvocalisation is the key" by comprehension falling on hard
  text; "removing eye movements removes their time" by 30 of 255 ms; "phrase
  reading means several words in one fixation" by the eyes still fixating
  most content words; "RSVP is reading with the waste removed" by Schotter,
  Tran and Rayner; "a testimonial is a measured claim" by the three parts of
  a test.
- **Fallbacks and ticks are taught, not just present.** Lesson 1 tells the
  reader what "I can't read aloud here" writes (183 in 60 s, labelled, not
  logged), calls the result "a weaker comparison" and says to do the aloud
  reading another day; the browser showed exactly that label and no log
  entry. Lesson 2 tells the reader to tick "I kept counting the whole way"
  only if they did, and the body, `steps[3]`, quiz 2 and `mistakes[1]` all
  say a lapsed reading is void; the tick reached the log as `extra.kept`.
- **The 600 wpm cap is a finding, not a limitation.** Lesson 3 says "Above
  600 the drill refuses, because the display becomes a flicker rather than
  something to read"; lesson 6 turns the same fact into the felt reading of a
  claimed pace ("Beyond 600 the drill will not go… and that is itself the
  finding") and tells the reader to press Reset at the questions because the
  story has been read before. The refusal message in the browser matched.
- **The quizzes test the act and their distractors are named errors.** 1.5
  against 9/8 (word counts divided) and 2/3 (the ratio inverted); ≈ −28.3
  against +20 (rate alone) and −16.7 (points, not wpm); 150 ms against 6.7
  (words a second) and 2.5 (a second for a minute); 600 ms against 200 (one
  word's time); 25.5 against 12.75 and 38.25; 2 hours against 1 hour (the
  1,500 figure). Every wrong answer was argued for and could not be defended.
- **The seam at lesson 3 is invisible.** Lesson 2 ends "Next, the tradition's
  other way past the voice: show the words one at a time, faster than any
  voice could say them"; lesson 3 opens with the drill. Both modules use the
  same tile vocabulary and cite How the Eyes Read by title for the model.

## Per-lesson findings

### `the-inner-voice`

Teaches the Do and the Standard. Both presets are in the body with their
figures; the fallback is explained; the body says why the lab divides rates
and not effective rates and that the silent side still prints its effective
rate "so you can see that the rate was a reading and not a skim". In the
browser, with three baselines in the log, the silent reading was logged
`test` and the verdict tile read "inside the baseline range" from a range
filled at load; the body did not say that tile would appear or why. One
clause added. The `typical` preset's silent side is "476 words in 120
seconds" so that the rate is exactly 238, while `P26` has 453 words; the
body frames the preset as "those averages as one reader", which is a fair
reading of §C, but a reader who has just done the drill sees 453 in the box
and 476 in the prose. Recorded below, not changed.

### `silencing-the-inner-voice`

Teaches the Do and the Standard, with the matched pair, the tick, the
second-task caveat and both studies' findings stated within their limits.
**The `typical` preset did not describe the lesson's passages**: it read "392
words normally in 96 seconds" and "393 words while counting in 90 seconds",
and §C recorded those figures, but the kit counts `P27` at 409 words and `P28`
at 402, and the drill writes those counts into the boxes. Repaired below with
an instance on the real counts whose rates are exact (409 words in 98.16 s is
250 wpm; 402 words in 90 s is 268 wpm), the body, worked example and
`mistakes[2]` rewritten to match, and the pins re-verified. The `easy-text`
preset (403 and 399 words) is explicitly "a reader on easier text", so it is
not the lesson's passages and need not match them. The page prints a verdict
tile for the counting reading's rate against the baseline range; one clause
added saying what a rate above the range once means here (the experience the
advice is built on, in a number, not a result).

### `one-word-at-a-time`

Teaches the Do and the Standard and is the course's drill-first lesson done
properly: the first paragraph sends the reader to the drill with the exact
box label and the fallback value, and nothing above the body states a result.
All three presets are in the body; the requested-against-measured tiles are
explained before the reader meets them; the saccade share is worked. In the
browser "Use my baseline median" wrote 250 from three baselines, 700 was
refused with the sentence the body quotes, the stream showed one word at a
time and ended by itself, and the entry logged `condition` with its target.
The comparison the lesson asks for, comprehension in the stream against the
baselines' comprehension, is done by the reader looking in their log; the kit
has a `vsLog` option for `drill/single` that would put the effective rate
against the baseline range on the page. Recommended below; §C does not list
it, so not changed.

### `reading-in-phrases`

Teaches the Do and the Standard. The arithmetic of a phrase on screen is
worked for a four-word phrase and for `P20`'s mean, and the body is careful
to separate the stream finding from the page claim ("Chunking groups words by
meaning; it does not widen the glance"). Both presets are in the body; the
button fills both target boxes, as the body says. In the browser the phrase
stream showed "bought in a pot" a second and a half in, both streams ended by
themselves, and the phrases box read 127. No change needed.

### `rsvp-without-looking-back`

Teaches the Do and the Standard. The garden path is explained with an example
the reader can feel, the two presets are in the body, the Schotter, Tran and
Rayner result is stated with its ordinary-sentence finding, and the body tells
the reader where to look after Score ("find the question about the misleading
sentence in each story"). Both passages' garden paths were checked against
their questions. The pacer and the stream both ran at 300 and ended by
themselves. No change needed.

### `testing-a-speed-claim`

Teaches the Do and the Standard: three computations and the three parts of a
test. All three presets are in the body with every figure, the settings
needed to bring 1,500 inside the perceptual span are worked (100 ms for a
fixation and its saccade together), photoreading is named once and tested the
same way, and the felt-pace instruction is correct about the kit. The
bookshelf paragraph gave the book time for three rates but not for the
`whole-page` preset the tile prints (≈ 8.6 min); one clause added. The `Q20`
warm-up logged `practice` with 423 words.

## Repairs made in this pass

In `content/reading/c4_inner_voice/part_a.py` only:

- `silencing-the-inner-voice`: the `typical` preset's instance, from (392
  words, 96 s, 6/6; 393 words, 90 s, 4/6) to (409 words, 98.16 s, 6/6; 402
  words, 90 s, 4/6), its label, and its `expect` from `245 wpm / ≈ 174.7 wpm /
  ≈ −70.3 wpm` to `250 wpm / ≈ 178.7 wpm / ≈ −71.3 wpm`, read off the rendered
  page after the change; the body paragraph that explains the preset (now
  naming both passages and their counts); the worked example (`268 × 4/6 =
  536/3`, `536/3 − 250 = −214/3`); `mistakes[2]` (18 words a minute faster, not
  17). The quiz was not touched: its instance was already a fresh one.
- `silencing-the-inner-voice`, the "Look at the rates as well" paragraph: one
  sentence on the verdict tile.
- `the-inner-voice`, the "Only the silent reading has questions" paragraph:
  one clause on the verdict tile for the test reading.
- `testing-a-speed-claim`, the bookshelf paragraph: the `whole-page` book
  time.

No slug, module, lab key, mode, view or passage changed. **`docs/reading/PLAN.md`
§C, Course 4, lesson 2 still records the old `typical` instance (392 words in
96 s → 245; 393 in 90 s → 262 → ≈ 174.7; ≈ −70.3)** and should be brought to
the new one in the same commit, as §C's preamble requires; it was left for the
orchestrator because the file is shared with the other courses' reviews
running concurrently. After the edits `python3 scripts/preview_subject.py
reading --course reading-inner-voice-and-flashing-words` reports `7 page(s)
rendered … 6 page(s) executed and swept, 6 with pinned figures, 0 failing …
OK`.

## Recommendations (taste, or outside this course's files)

- **`one-word-at-a-time`: pass `vsLog: True`.** The lesson's comparison is
  the stream's comprehension against the baselines', and the kit can put it
  on the page as `drVsBase` (effective rate against the baseline range of
  effective rates) and `drVsRecent`, filled from the log at load and after
  Score. The body would then point at a tile instead of sending the reader to
  the log. A §C change, so for the orchestrator.
- **`the-inner-voice`, `typical` preset:** the silent side's 476 words is not
  `P26`'s 453. An instance on 453 words cannot give exactly 238 (453 × 60 /
  238 = 114.2017… s), so the clean alternatives are to keep the averages as
  they are and add a clause that the box will show 453 after the drill, or to
  move the preset to a round rate on 453 words (453 words in 113.25 s is 240
  wpm; ratio 240/183 ≈ 131.1%). The first keeps Brysbaert's figures, which is
  the preset's point.
- **`Q20` is a near-twin of `P21`** (a young telegraph operator taught the
  code by her father, a message that does not sound right, a check by wire,
  a train saved), and `P21` is Reading A of Fewer Needless Regressions one
  course earlier. The questions are independent, but the warm-up will read as
  a repeat. For the passages owner.
- **`the-inner-voice`, concept 1** says the ratio is "how many times faster
  your eyes and your inner voice go than your mouth", which half-concedes the
  picture the lesson refutes (that the inner voice has a speed of its own).
  "how many times faster you read silently than you speak" is cleaner.
- **`assumes_short`** reads "Courses 1–3" where the other courses name the
  prerequisite courses by title; `assumes_long` does name them. Cosmetic.
- **Carver 1985 and the 600 wpm figure** appear in `mistakes[0]` here and in
  The Speed Ceiling. Both lessons need Carver; the second could cite the first
  by title in a clause rather than restate the finding.
