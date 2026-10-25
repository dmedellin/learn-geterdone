# Pedagogy assessment — How the Eyes Read (Reading Faster, course 3)

Formed from the six lesson dicts in `content/reading/c3_eyes/part_a.py` and
the course dict in `content/reading/c3_eyes/__init__.py`, the seven passages
their drills and warm-ups use (`P06`, `P07`, `P08`, `P21`, `P22` and `P11`
from `content/reading/passages/bank_a.py`, `Q19` from `pool.py`), and the kit
they render through (`scripts/mathpath/labs/readkit*.py`: `eye/budget`,
`flash/span`, `drill/compare` with the `pacer` and `mask` displays and
`lapses`, `eye/required`, `flash/schulte`, and the `warmup` slot), on branch
`feat/reading-subject` before the Subject was wired. The design authority is
`docs/reading/PLAN.md` §0 (every figure is the reader's own measurement, a
stated model, or a count), §B, the Course 3 entries in §C, §D.3 as recorded
in `docs/reading/kit-report.md`, §E (the per-lesson procedure: do the drill
first, every preset in prose, steps as the protocol) and §F (the voice), read
beside `docs/reviews/reading-spec-pedagogy-review.md`, whose findings 11, 13,
16, 17, 28, 29 and 30 concern this course.

Every lesson was read in full before anything was changed. The course was
rendered with `python3 scripts/preview_subject.py reading --course
reading-how-the-eyes-read`; every pinned tile on the six pages (42 strings)
was read off the rendered page with `node scripts/labcheck.js --observe`;
every figure in prose was recomputed by hand (the budget at four settings,
the characters per fixation at eight rates, the two book times, both compare
presets, the table times); every passage was counted by the kit's own word
rule and its readability formula; and the drills were done in Chromium
through Playwright against the served preview, on a controlled clock: the
`P06` warm-up on the first page, twenty flashes of the span drill with three
cues each, the pacer and the mask at 300 wpm on Looking Back with three
baselines in the log, the unpaced and paced pair with lapse counts on Fewer
Needless Regressions, and a Schulte table followed by the `P11` test warm-up.
Fifty-five checks across both courses, none failing, no console or page
error. Every `data-say` on the key lines was read. Lessons, in course order:
`fixations-and-saccades`, `the-perceptual-span`, `looking-back`,
`fewer-needless-regressions` | `the-speed-ceiling`, `training-the-periphery`.
The bar marks the seam between the two modules.

## Verdict

The course teaches what §C says it teaches, and the drills do what the text
says they do. A reader who finishes it can compute fixations per word, time
per word and the rate a five-quantity budget allows, and say which quantity
moves the total most; read a letter span off accuracies by position and say
in two sentences why it is symmetric when the reading span is not; set two
scores at one pacer rate side by side as effective rates and say whether the
gap is more than one question; weigh a paced against an unpaced reading on
effective rate and on a lapse count they kept themselves; turn any claimed
rate into the characters a fixation would have to advance and give the
verdict with its settings; and set a falling Schulte time beside a run of
test readings and name what else could explain both. Those are the acts the
`standard` fields name, the quizzes ask them on fresh instances, and the
course `outcomes` are the same six acts.

More to the point for this Subject, the reader leaves with a log and not only
facts. Every lesson has a timed reading: three warm-ups (`P06` and `Q19`
logged `practice`, `P11` logged `test`), two compares logged `condition` with
Reading A of the fourth lesson logged `test`, a span drill and a Schulte
table logged `other`, exactly as §C assigns them, and every page's last step
sends the reader back to the Daily Drill. The `steps` are a protocol for
another day in all six lessons, not a summary of the body: "Watch eyes read"
is the oldest demonstration there is and needs no kit; "Set one rate for
both", "Read in the order given", "Compute both effective rates", "Decide
whether the difference is a result" is exactly what a reader does when they
repeat Looking Back on a fresh pair.

The arithmetic is right everywhere. All 42 pinned strings matched the page,
and every figure quoted in prose agreed with the lab or with a recomputation
(`15/17`, `225 ms`, `≈ 266.7`; `3/4`, `191.25`, `≈ 313.7`; `≈ 291.2`,
`≈ 206.1`; `25/31`, `≈ 205.6`, `≈ 291.8`; `12.75`, `25.5`, `637.5`, `8.925`,
`7.7`; `2.48`, `1.64`; the 400 stops on a 453-word warm-up, which is
`453 × 15/17 ≈ 399.7`). Every passage's word count in the presets is the
count the kit's rule gives (`P07` 447, `P08` 436, `P21` 484, `P22` 457), so a
reader who does the drill sees the same words figure the preset carries. The
research is cited within its limits and the tradition is stated at its
strongest before the evidence, as §F asks.

The defects were small and local, and are repaired below: the six `standard`
heads were written as labels where every other course in the Subject writes
"Finish when you can…"; the speed-ceiling page prints a book-time tile the
body never mentioned; and in both compare lessons the body tells the reader
to use their hold target while the only button on the page fills the boxes
with the baseline median, which a reader following the text would press and
be puzzled by. Nothing needs splitting, merging or reordering within the URL
space the course has.

## The voice, judged against §F

- **"You", about the reader's own numbers.** "If your warm-up came out at 240
  words a minute and the typical preset says 266.7, the gap is not a finding
  about your eyes" (lesson 1); "If your result looks like no-cost, you have
  not refuted the study, and the study has not refuted you" (lesson 3); "the
  exercise has not transferred, for you, so far" (lesson 6). The §C sentence
  about a result that goes the other way is in both compare lessons, once
  each.
- **Try first, then explain.** Lessons 1, 2, 5 and 6 send the reader to the
  drill in their first paragraph; lesson 3's `read_intro` sets the targets
  before anything is explained. Lesson 4 is the one exception, and rightly:
  it needs the pencil instruction before the drill.
- **History as a story with people in it, once.** Javal's laboratory, Lamare's
  observation and Hering's independent one, and the word "saccade", in lesson
  1 and nowhere else in the module; von Frisch and Spallanzani belong to the
  passages, not the lessons. McConkie and Rayner's moving window is explained
  in a sentence a reader can picture. Carver "went looking for the fastest
  readers he could find" in lesson 5.
- **Presented, not endorsed, both ways.** "The tradition's answer is that
  trained readers stop reading word by word and take in meaning by the line
  or the page; the trainees in speed-reading courses often report that it
  feels that way" comes before Carver (lesson 5); "readers who practise it do
  get faster at it, often quickly" before the transfer question (lesson 6);
  "Most readers who try this find the second number smaller… That is the
  experience the tradition reports, and it is worth having for yourself"
  (lesson 4). Nowhere does a lesson say "scam" or "science proves".
- **No promises.** The one figure that could read as one, the ≈ 25 words a
  minute of the regression example, is labelled "illustrative" three times
  and "the size of the prize, not a promise of it".
- **No slang, no first person, no "let's".** None found. No light remark in
  this course either, which is within the rule (at most one).
- **The `note` as the limit.** Each names what the measurement cannot settle:
  the model "does not track your eyes"; the span drill "is not the perceptual
  span in reading"; "the kit's line mask is not the word-by-word mask of the
  study"; the lapse count and the shares "neither is a measurement of your
  regressions"; "one day of either cannot settle" transfer.
- **Pointing forward by title.** Every body ends by naming the next lesson's
  title and question; lesson 6 names the next course by its §B title.

## What the course teaches well

- **One model, used three times.** The five-quantity budget is built in lesson
  1 with a `math` block of four lines and a worked example that is the first
  preset by hand; lesson 4 reuses it for a smaller regression share; lesson 5
  "runs it backwards" from a rate to the characters a stop needs. A reader
  who has done lesson 1 can follow lesson 5's `math` block line by line, and
  the course `key` carries the two formulas side by side.
- **The misconceptions are the ones readers hold, and each is refuted with a
  figure or a demonstration.** "The eyes glide" is answered by the mirror
  step and Javal; "a trained eye takes in a line" by the reader's own span
  ending "a few letters from the centre too" and the line of 65 characters
  being "about eight word-identification spans long"; "regressions are a bad
  habit" by `300 × 4/6 = 200` and Schotter, Tran and Rayner; "1,000 with full
  comprehension is technique" by `25.5` characters and Carver's 600;
  "faster tables make faster reading" by "practice improves the practised
  task".
- **The compare lessons are honest about what they can show.** Both panels
  carry the one-question sentence; both bodies compute the worth of one
  question at the preset's rate (50 at 300; 40 to 44 at 240 and 264); the
  `no-cost` and `no-change` presets are given the same weight as the ones
  where the technique shows; and lesson 4 says plainly that its effective
  rates "do not show a result" and that the lapse count is "the part worth
  noting, as a self-report". The verdict tile is correctly absent when B is
  paced, and lesson 4's body says why.
- **The span drill is explained before it is run** ("Read what it does before
  you start, so that the flash does not surprise you"), its timing is
  justified (150 ms against the 175–200 ms a saccade needs), its chance level
  is stated (one in four), and the body warns that twenty flashes of three
  cues ask each position only about four times. In the browser the drill
  behaved exactly as described: a `+`, a 15-letter string, a mask of `#`,
  three cued positions with four letter buttons and "not seen", and a message
  printing the requested and measured display times.
- **The quizzes test the lesson's point on fresh instances, and the
  distractors are named errors.** 191.25 against 225 (regressions in), 255
  (one fixation per word) and 168.75 (saccade left out); 225 and 180 against
  216 "as if there were five questions"; 12.75 against 11.25 (saccade left
  out) and 8.5 (the figure at about 333 wpm); 1.64 against 0.61 (cells per
  second) and 1.52 (divided by 27). Each wrong answer was argued for and
  could not be defended.
- **The seam at lesson 5 is invisible.** Lesson 4 ends "The next lesson, The
  Speed Ceiling, turns the window into a limit on speed"; lesson 5's
  `concepts_intro` opens "The budget in Fixations and Saccades turned stops
  and jumps into a rate. This lesson runs it backwards." Both modules use
  the same tile vocabulary, cite lessons by title and spell British.

## Per-lesson findings

### `fixations-and-saccades`

Teaches the §C Do (the five inputs to fixations per word and words a minute)
and its Standard. All three presets appear in the body with their figures;
the `ul` on return sweeps carries the fact the cut lesson Lines and Return
Sweeps used to hold, with its arithmetic right (64 / 8 = 8, one more for the
sweep, "roughly an eighth more"; 30 × 255 ms ≈ 7.7 s). The warm-up is
explained as filling none of the model's boxes, which the browser confirmed
(eye tiles unchanged after Score). The mirror step is `steps[0]`, as the
pre-authoring review asked. Quiz 2's correct option is the longest, but the
other three are each a stated property of the model and a reader cannot pick
it by length alone. No change needed beyond the `standard` head.

### `the-perceptual-span`

Teaches the Do and the Standard, and is careful about the thing most likely
to mislead: the drill's span is letters without context and is symmetric, and
the lesson says so four times (body, concepts, `mistakes[1]`, `note`). The
`_span_preset` generator writes out ten strings with every position asked, so
the preset is whole-report while the drill is partial-report; the body
explains the difference ("a reader whose every position was asked ten
times"). The worked example reads one side of the typical preset. The quiz's
first item asks what the lab prints, which is a weak item (it tests the
tile, not the act), but items 2 and 4 test the lesson's point. Recorded
below, not changed.

### `looking-back`

Teaches the Do and the Standard; both presets and the worth of one question
at 300 are in the body; the §C confounds are in the `note` and the
other-way sentence is in the body. The drill behaved as described: the
highlight lit 14 spans three seconds in, the mask had hidden 43 spans ten
seconds in, both displays ended by themselves, both entries logged
`condition` with the order recorded. **One mismatch between text and page:**
the body and `steps[0]` say "Put your hold target in both target boxes", but
the only button on the page is "Use my baseline median", which in the browser
wrote 250 into both boxes from three baselines. A reader following the text
would press it and get a number the lesson did not ask for. Repaired below
with a clause saying what the button does and to type the hold target over
it.

### `fewer-needless-regressions`

Teaches the Do and the Standard, and the body does what the pre-authoring
review's finding 29 asked: the lab is the compare of the two readings with
the lapse count as a logged input, and the budget's regression split is the
worked example only, labelled illustrative. The lapse box appeared after Done
and before the questions in both slots, and both counts reached the log
(`extra.lapses` 4 and 1) and the tiles. The preset's `103.864` seconds is
explained ("as the drill records time to the millisecond"). The same
hold-target-against-baseline-median mismatch as Looking Back; repaired the
same way. The page also prints `drRatio` (≈ 110.0%) and `drPacerLineMs`
(≈ 2,727.3 ms) that the body never mentions; recorded, not changed.

### `the-speed-ceiling`

Teaches the Do and the Standard. All three presets are in the body with their
figures and verdicts, the "at these settings" rule is applied to a worked
counter-example (350 wpm at 225 ms is 8.925, at 190 ms is 7.7), and the
lesson names skimming as what happens at 1,000. **The page prints a third
tile, "A 90,000-word book at that rate" (3 h, 1.5 h, 3.6 min), that the body
never mentioned.** One sentence added. The `Q19` warm-up (399 words) is
logged `practice` as §C says.

### `training-the-periphery`

Teaches the Do and the Standard. The §C arrangement — three tables logged
`other`, then the `P11` warm-up logged `test`, the table times in a log note
beside the test's effective rate because `log/history` has no Schulte series
— is exactly what the lesson instructs, and the browser confirmed a table
logs `other` with its time and the warm-up logs `test` with 488 words. The
body names three confounds for two rising lines (the Daily Drill, the
passages, attention) and the comparison that would separate them (weeks with
the tables and weeks without). The quiz's second item asks the Standard's
act on a fresh instance. No change needed beyond the `standard` head.

## Repairs made in this pass

In `content/reading/c3_eyes/part_a.py` only:

- The six `standard` heads, from labels ("Compute a budget by hand", "Read a
  span from accuracies", …) to the "Finish when you can…" form every other
  course in the Subject uses, so the rendered `<strong>` line reads the same
  way across the eight courses. The bodies of the standards are unchanged.
- `looking-back`, body paragraph 1: a parenthesis saying the button fills
  both boxes with the baseline median and that the reader types their hold
  target over it.
- `fewer-needless-regressions`, body paragraph 1: the same, for B's box.
- `the-speed-ceiling`, the thousand/twenty-five-thousand paragraph: one
  sentence naming the book tile and its three figures (3 hours, an hour and a
  half, 3.6 minutes), each recomputed.

No preset, `expect`, slug, module, lab key, mode, view or passage changed, and
no §C entry needs correcting: every instance the lessons carry is the one §C
records. After the edits `python3 scripts/preview_subject.py reading --course
reading-how-the-eyes-read` reports `7 page(s) rendered … 6 page(s) executed
and swept, 6 with pinned figures, 0 failing … OK`.

## Recommendations (taste, or outside this course's files)

- **A hold-target button.** Two lessons here, and the Daily Drill's routine,
  turn on the reader's hold target, but the kit's compare view offers only
  "Use my baseline median" (`fromBase` scales it; it cannot read `drHold`
  from the practice log). A second button, or a `fromHold` cfg, would let the
  body say "press Use my hold target" instead of the workaround now in the
  text. For the kit owner.
- **`the-perceptual-span`, quiz 1** asks which strings the lab prints for the
  typical preset. Replace with a fresh instance ("accuracy 7/10 at +2, 5/10 at
  +3, 3/10 at +4: what is the span on the right?") so that the item tests the
  Standard's act rather than the page.
- **`fewer-needless-regressions`** could pass `ratio: False` to drop the
  `drRatio` tile, which the body never uses and which invites the comparison
  of rates the lesson warns against. Kit-permitted; a one-key change the
  orchestrator may prefer to leave for consistency across compare pages.
- **`Q20` and `P21` are near-twin stories** (a young telegraph operator who
  learned the code from her father, a message that does not sound right, a
  check by wire with another station, a train saved). `P21` is Reading A
  here; `Q20` is the warm-up of Testing a Speed Claim two courses later. The
  questions are not answerable from the other story, but the second reading
  will feel like a repeat. A pool passage of another kind for that warm-up
  would be better. For the passages owner.
- **`the-speed-ceiling` and Testing a Speed Claim** both carry Carver 1985
  and the 600-wpm figure in their `mistakes[0]`. Each lesson needs it; the
  second could cite the first by title in one clause rather than restate it.
