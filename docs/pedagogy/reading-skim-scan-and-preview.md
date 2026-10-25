# Pedagogy assessment — Skimming, Scanning and Previewing (Reading Faster, course 5)

Formed from the seven lesson dicts in `content/reading/c5_skim_scan/`
(`part_a.py`, lessons 1–4, module "Scanning and skimming"; `part_b.py`,
lessons 5–7, module "Reading strategically"; `__init__.py`, the course dict),
the ten passages their drills serve (`S01`, `S02`, `P32`–`P37`, `B01` in
`content/reading/passages/bank_b.py`; `Q21` in `pool.py`), and the kit they
render through (`scripts/mathpath/labs/readkit.py` and `readkit_b.py`, modes
`drill`, `scan`, `triage`; views `single`, `compare`, `sections`, `find`,
`inspect`, `plan`), on branch `feat/reading-subject` before the Subject was
wired. The design authority is `docs/reading/PLAN.md` §0 (the reader measures
themself), §B, the Course 5 entries in §C, §D as the kit built it
(`docs/reading/kit-report.md`, which wins where it differs), §E (the author's
checklist) and §F (a coach who has read the research).

Every lesson and every passage was read in full before anything was changed.
The course was rendered with `python3 scripts/preview_subject.py reading
--course reading-skim-scan-and-preview`; every preset's tiles on the seven
pages were read off the rendered page with `node scripts/labcheck.js
--observe` (sixteen presets, 55 pinned strings); every figure in prose was
recomputed by hand and, where it is a count over a passage, by the kit's
Python mirror in `readkit_core`. Seven drills were then done end to end in
Chromium through Playwright on a controlled clock against the served render:
the scan of the ferry timetable (five targets by mouse, 8 s a target, the
museum guide served on the second visit), the 40-second skim of the glacier
passage, the skim-against-reading compare, the preview compare with the clock
run through both parts, the inspection of the imaginary book (one skip, one
wrong click, and a second run that let the 300-second limit end the drill),
the triage buttons, and the two-section reading with its attention tick.
Every `data-say` on the seven pages was read. Lessons, in course order:
`scanning-for-a-target`, `skimming-for-gist`, `what-skimming-costs`,
`previewing-before-reading` | `inspectional-reading`,
`triaging-a-reading-list`, `shifting-gears`. The bar marks the seam between
the two modules. The course assumes Measure Your Reading and a running Daily
Drill, and is judged against that.

## Verdict

The course teaches what §C says it teaches, and the drill is the lesson in
every one of the seven. A reader who finishes it has done, not read about,
the three ways of reading less of a text: timed a search and priced it per
target found and in words passed over, skimmed by headings and first
sentences under a limit set from their own baseline and scored it in gist
answers a minute, skimmed one passage and read a matched one and scored gist
and detail apart, previewed a passage with the preview's 30 seconds inside
the clock, answered five structural questions about a book from its front
and back matter against a five-minute limit, planned a 15,000-word pile into
a 45-minute budget, and read a story-then-report passage with a rate for
each half. Those are the acts the `standard` fields name and the quizzes
measure. The `mistakes[0]` of every lesson is the §C misconception, each
refuted with the lesson's own figure: 919.5 words a minute "passed" with
nothing understood but five times and prices; a first sentence about a
boulder on a beach that is not the paragraph's point; a skim whose effective
rate of 307.5 beats the reading's 258 while keeping one detail in three; a
preview that turns 173.2 into 216.5 when its 30 seconds are left out; a
preface that says to begin at chapter four, on page 63; a pile that needs
333.3 words a minute to read whole and fits at 250 with four documents
skimmed; a rigid reader at 240 through both halves who loses two of three
report questions. All 55 pinned tile strings matched the lab, and every
figure in prose agreed with the lab or with a recomputation.

The voice is §F's: "you", about the reader's own numbers, the research
presented with its limits ("laboratory tasks, and your two passages are not
theirs"), no promise anywhere, both compare lessons saying once that a
contrary result refutes nothing and is refuted by nothing. The `steps` are
protocols for repeating each drill on a document of the reader's own, and
every lesson ends on the Daily Drill. The sequence is right: nothing is used
before it is taught, the gist display and the gist-per-minute score come
before the gist/detail split, the compare comes before the preview compare,
and the inspection is introduced as "the scanning drill with a five-minute
limit", which is exactly what it is.

The defects were three sentences that described the lab wrongly, and they
mattered because each told the reader to look for something the page does
not show or to disregard a prompt the page does not make: the skim lesson
said the drill's result line prints 891 words a minute and the panel refuses
to multiply it (the line prints "Skimmed for 40 s, 2 of 4 right" and there
is no rate anywhere); the skim-against-reading lesson said the skim side's
prompt tells the reader to read at their usual pace and must be
disregarded (the prompt said the passage disappears after 40 seconds, and
nothing on the side said to skim); the inspection lesson named a tile by a
label the panel does not use. A fourth, raised by the Course 8 review, was a
log kind: the scan and the skim were logged as `other` and `condition`, which
The Full Battery's profile never reads, so its gist and scan rows could not
fill from this course. All four are repaired below. Nothing needs splitting,
merging or reordering.

## The voice, judged against §F

- **"You", warmly, about the reader's numbers.** "Look at your score before
  anything else, because whatever it was, it came from under a quarter of the
  text" (`skimming-for-gist`); "Some readers skim well, and this drill is how
  you find out whether you are one of them; one pair of passages is not
  enough to tell" (`what-skimming-costs`); "So the rigid preset is not a poor
  reader. By Carver's account it is the usual one. This lesson asks you to do
  the unusual thing on purpose" (`shifting-gears`). The exemplary register of
  §F, held in every lesson.
- **Try first, then explain.** `skimming-for-gist` is the course's drill-first
  lesson and its `summary`, `one_line` and `concepts` state the question and
  the method ("how much of a text's point you can get from a small, chosen
  part of it") and not the expected result; the body's first `p` sends the
  reader to Start, and the second begins "Look at your score".
- **Presented, not endorsed, both ways.** Masson 1982 and Duggan and Payne
  2009 are given at strength ("skimmers who choose where to look do better
  on the important points than readers forced through the whole text at the
  same speed") and then bounded ("still below a full reading"; "laboratory
  tasks"). Robinson's SQ3R and Adler and Van Doren are "advice, and the drill
  is a way to test it on your own reading". Carver's constancy finding is
  stated and his units ("six-character words for students on his
  materials") are named where they could mislead.
- **The history as people, once a lesson.** Robinson 1946 and the 1972
  revision of *How to Read a Book* with its four levels; Carver's five gears
  and his word "rauding"; the cinder cone that grew in a Mexican cornfield in
  front of the farmer is the passage's, not the lesson's. No Javal, Wood or
  Allen here, correctly: they belong to other courses.
- **One light remark, not at the reader's expense.** "Five minutes on a book
  you then decide not to read is the cheapest reading you will do"
  (`inspectional-reading`).
- **The limit admitted.** Every `note` names what the measurement cannot
  settle: "a scan's figures depend heavily on the layout"; "a single question
  is a quarter of the score"; "Two passages compared once … which is why the
  order alternates"; "The drill can show a preview paying only through
  comprehension"; "more guided than an inspection on your own"; "The model is
  stated, not measured"; "The second section is harder and also second".
- **Pointing forward by title.** Every body ends with the next lesson's title
  and its question; `shifting-gears` ends with the next course by title and
  its first drill.
- **No slang, no "let's", no first person, no "your reading speed".** None
  found on the seven pages.

## What the course teaches well

- **Every score is the purpose's score.** The course's one idea is that a
  skim, a scan and a preview are scored on what they were for, and it is
  carried through the kit as much as the prose: the gist display prints no
  `drWpm` or `drErr` (verified on the page), the skim-against-reading panel
  prints gist and detail apart, the preview's clock starts at the preview
  (verified: 30 s of 133 words, then 433 words, 150 s → 173.2 wpm), the
  triage tiles are minutes, value covered and fit. The `how_to` says it in
  one sentence: "A rate in words a minute is the right number only for a
  full reading."
- **The misconceptions are the ones readers hold, and the drill shows them
  up.** "Scanning is fast reading" meets 919.5 words a minute passed with
  five facts kept. "A skim is a fast read with a little less understanding"
  meets a higher effective rate and a lost detail in three. "A preview is
  free" meets a 30-second cost that is a fifth of the time. "Reading a book
  means starting at page one" meets a preface that says otherwise. "The
  fastest way through a pile is to read faster" meets 333.3 against a plan
  that fits at 250.
- **The arithmetic is right and the counts are the kit's.** 613 / 40 ≈ 15.3
  and 613 × 60 / 40 = 919.5; 95 / 4 = 23.75 against the 19 a reader would
  get by dividing by the five asked; 141 / 594 = 47/198 ≈ 23.7%, and the
  display shows exactly 141 word spans; 410 × 60 / 40 = 615 and 387 × 60 /
  90 = 258, the two passages 23 words apart as the concept says; 451 × 60 /
  110 = 246, 433 × 60 / 150 = 173.2, 246 × 5/6 = 205, 173.2 × 5/6 ≈ 144.3,
  −60.7; 300 / 4 = 75 and 210 / 5 = 42; 10,800 / 250 = 43.2 with 23 of 36
  covered, 7,500 / 250 + 7,500 / 750 = 40 with 32 of 36, 15,000 / 275 ≈ 54.5
  saving about 5.5 against 3,900 / 250 = 15.6; 292 × 60 / 60 = 292, 286 × 60 /
  104 = 165, 578 × 60 / 164 ≈ 211.5, × 5/6 ≈ 176.2, and the rigid reader's
  578 × 60 / 145 ≈ 239.2, × 4/6 ≈ 159.4. The section split is the passage's
  (292 + 286 by the kit's word rule), and the three story questions do come
  before the three report questions, as the body says.
- **The passages do what the lessons need.** The glacier passage's "Stones
  far from home" section does put its point last ("In other words, the land
  itself keeps a record") after a first sentence about a boulder, which is
  the skim lesson's refutation; its four gist questions are answerable from
  headings and first sentences, and the one about that section is rescued
  by its heading, as the body says. The reef and volcano passages are both
  headed exposition with three gist and three detail questions each; the
  bridge and refrigerator passages both have a first and last paragraph that
  frame the whole. The timetable's five targets have the forms the lesson
  names (a time, a fare, a time, a name, a duration) and one sits inside a
  paragraph; the book's five targets are answered in the contents, the
  index, the title page and the preface, and the preface does say what the
  lesson says it says. The two-section passage is a story at grade 5.8 and a
  report at 16.8 by the kit's own count (292 words in 18 sentences; 286 in
  13), with the seam where `sections` puts it.
- **Worked example, prediction, independent practice.** Every `worked` is
  the first preset by hand; the `panel_intro` of the scan says what fills
  the boxes and when; every quiz asks the same act on a fresh instance (3
  of 5 in 60 s; 120 of 600 words for 30 s; a 9,000-word pile and a 30-minute
  budget; 300 words in 60 s and 300 in 100 s) with the named error as a
  distractor (12 s for dividing by the targets asked; 1,200 words a minute for
  a rate on words never shown; 12 minutes for the pile at the skimming rate;
  225 for the whole-passage rate that hides the shift).
- **Every compare lesson meets §C's preamble.** Both `note`s name the two
  confounds (different passages; the order, which alternates) and both
  bodies say once that a reader whose result goes the other way has not
  refuted the study and the study has not refuted them. The one-question
  sentence is in both panels and in both bodies. The order was `AB` on a
  fresh log in every browser run, as the kit's parity rule says.
- **The `steps` are protocols.** "Name five targets first … write next to
  each the form its answer will take"; "Set a limit from your baseline …
  under a third"; "State the purpose first"; "Preview the other, clock
  running"; "Write three questions and set five minutes"; "List and value the
  pile … before you read any of them"; "Name the gear before you start". A
  reader can repeat each drill on a document of their own without the kit,
  which is what §E asks for.
- **The seam at lesson 5 is invisible.** `previewing-before-reading` ends
  "a preview of a whole book takes a few minutes, and Inspectional Reading,
  which opens the next module, times one", and `inspectional-reading`'s
  `read_intro` calls itself "the scanning drill with a five-minute limit".
  Both modules keep the same tile vocabulary and the same "then today's
  Daily Drill" closing step.

## What it taught badly, or said wrongly

### Prose that described the lab wrongly

- **`skimming-for-gist`, body:** "The line under the drill reports the
  passage's 594 words over your 40 seconds, 891 words a minute, because it
  reports every drill that way; the panel does not go on to multiply that by
  your score." In Chromium the line under a gist drill reads "Skimmed for
  40 s, 2 of 4 right" and no rate is printed anywhere on the page; the
  tiles are `594 words` and `40 s`. A reader sent to look for 891 would not
  find it. Repaired: the paragraph now says the panel shows the words and
  the seconds as two tiles and stops there, does not divide one by the other
  (which would be 891), and does not multiply that by the score.
- **`what-skimming-costs`, body and lab:** "The prompt under it says to read
  at your usual pace; for this one, skim instead, however you skim, because
  the passage disappears when the 40 seconds run out." The side's prompt
  actually read "The passage disappears after 40 seconds; press Done if you
  finish first", and while it ran, "The passage disappears after 40 s; press
  Done if you finish first." Nothing on the side told the reader to skim;
  the instruction lived only in the body and the label. The kit gives a
  compare side its own instruction (`intro`, kit report, drill side cfg), so
  side A now carries "Skim this one, however you skim: the passage disappears
  after 40 seconds", which the page prints before Start and (with "Press Done
  when you finish") while the clock runs; verified in Chromium, and the
  passage still disappears by itself at 40 s. The body sentence now says
  that. No preset, `expect` or instance changed.
- **`inspectional-reading`, body:** "Seconds per target found is the same
  figure as in Scanning for a Target." On the inspect view the kit labels
  the tile "Seconds per right answer" and the found tile "Answered". The
  sentence now names the label the panel uses and says the arithmetic is the
  same.

### Log kinds that The Full Battery could not read

- **`scanning-for-a-target` and `skimming-for-gist`, lab and body** (raised
  by the Course 8 review): Course 8's profile fills its gist and scan rows
  from log entries of kind `baseline` or `test` only (`readkit_b.py`, the
  `lgMine` handler for `profile`: `c = log.filter(kind baseline or test)`,
  then `display === 'gist'` for the gist row and `mode === 'scan' && view
  === 'find'` for the scan row), and its body says the rows come "from
  Skimming, Scanning and Previewing". The scan logged `other` (the kit's
  default for `scan/find`, and §C) and the skim `condition` (§C), so those
  rows could never fill. Verified in the kit that changing the kind is safe
  for the rate curve: `rdIsReading` (`readkit_core.py`) counts only `drill`
  and `warmup` entries whose display is not `gist`, and every rate, median,
  range and verdict in `log/history`, `log/noise` and the profile's
  effective-rate rows goes through it (`lgCounted`, `rdKindRates`), so a
  `scan` entry and a `gist` entry of kind `test` enter no range and no
  median. Both lessons now log `test`; verified in Chromium that the skim
  entry is `kind: test, display: gist` and the scan entry `kind: test, mode:
  scan, view: find`. The two body sentences that named the kind now say the
  result is logged as a skim test or a scan test, never enters the rate
  curve, and is read by The Full Battery (first and latest), which with the
  museum guide served on the second visit gives the scan row a genuine
  "then" and "now". §C's kinds for these two drills (`other`, `condition`)
  should be updated to `test` by the orchestrator.

### Quiz

Every distractor on the course was argued for and could not be defended. The
closest were `skimming-for-gist` quiz 4 ("A and B have the same gist rate":
4.5 against 3), `triaging-a-reading-list` quiz 3 ("It went over the budget":
43.2 fits), and `shifting-gears` quiz 3 ("A rigid reader who held one
speed": 250 to 170 is not one speed). Nothing changed.

### Speech

Every math run on the seven pages was read from `data-say`. All read
correctly: "613 over 40 is approximately 15.3 words a second", "433 times 60
over the quantity 30 plus 120, equals 173.2", "7500 over 250 plus 7500 over
750 equals 40 minutes", "286 times 60 over 104 equals 165 words a minute".
The pound sign in the timetable is passage text, not a math run, and is not
spoken as math. Nothing changed.

### Cross-references

Lessons are cited by title ("The Daily Drill", "Measure Your Reading",
"Skimming for Gist", "What Skimming Costs", "Previewing Before Reading",
"Inspectional Reading", "Triaging a Reading List", "Shifting Gears"), each
as the lesson carries it; the next course by its §B title, Words, Knowledge
and Difficulty. No lesson is cited by number.

## Can a reader with Course 1 and a running Daily Drill follow it?

Yes. Lesson 1 asks only for a clock and a count and defines both figures
before the preset uses them. Lesson 2 asks the reader to set a limit "from
your baseline", which Course 1 gave them, and tells them the limit it chose
and why (148.5 s at 240, so 40 s is under a third). Lesson 3 opens by naming
what the effective rate from Measure Your Reading cannot do, and the split
score is introduced as the repair. Lesson 4 adds one thing, the clock
through the preview, and the `worked.after` shows what leaving it out does.
Lesson 5 is lesson 1 with a limit and a book, and says so. Lesson 6's model
is three sentences and the reader changes it with buttons. Lesson 7 is the
first time a reader meets a rate per section and the body says the
whole-passage rate "hides the shift" before the tiles show it. The two
places a reader will slow down are the gist-answers-a-minute unit, which is
new and is given its own concept, and the triage model's half-credit for a
skim, which the body calls "an assumption in the spirit of What Skimming
Costs" and lets the reader change.

## Repairs made in this pass

In `content/reading/c5_skim_scan/part_a.py`: `scanning-for-a-target` the
lab cfg (`kind: "test"`) and the first body paragraph's sentence on the log;
`skimming-for-gist` the lab cfg (`kind` from `condition` to `test`), the
first body paragraph's sentence on the log, and the "Notice what the panel
does not print" paragraph; `what-skimming-costs` the first body paragraph
(the skim side's instruction) and the side `a` cfg, which gains `intro`. In
`part_b.py`: `inspectional-reading` the "Seconds per target found"
paragraph. No preset, `expect`, slug, module, lab mode, view, passage or
instance changed; every instance the lessons carry is the one §C records.
The two log kinds differ from §C and §C should follow (above). `scripts/preview_subject.py reading --course
reading-skim-scan-and-preview` reports OK after the changes: 7 pages
executed and swept, 7 with pinned figures, 0 failing.

## Remaining issues and recommendations

- **§C, Course 5 lessons 1 and 2, log kinds.** Now `test` in the lessons
  (above); §C still says `other` and `condition`, and the kit report's
  "Proposed PLAN edits" item on D.3.2 / profile should be resolved the same
  way. For the orchestrator.
- **`what-skimming-costs` prints two tiles the body argues against.**
  `drRatio` ("B / A, effective rate", 172/205 ≈ 83.9% on the typical preset)
  and `drErrDiff` (−49.5 wpm) sit under the gist and detail tiles while the
  body says the effective rate is the wrong basis for the choice. The
  compare view takes `ratio: False`, which drops `drRatio`; `drErrDiff` has
  no switch. Taste; recorded.
- **`previewing-before-reading` prints `drRatio` 433/410 ≈ 105.6%** and the
  body works only `drErrDiff` (+9.2). Harmless, unmentioned; the same
  `ratio: False` would remove it.
- **`shifting-gears`'s rigid preset is given a per-section split the kit
  cannot record.** The body says the rigid reader "got all three story
  questions and one of the three report questions" and that "the whole loss
  was in the dense section"; the preset carries `correct: 4` and nothing
  else, because `drill/sections` has no per-section score (kit report, "Not
  done, by choice"). A preset is "a plausible reader's result written out",
  so the sentence is allowed, but it should say "say" rather than report.
  The `standard` asks for "the questions right on each", which the reader
  gets from the result list (the last three are on the report), not from a
  tile; that is said in the body. Recorded, not changed.
- **The sections slot's pre-Start prompt says only "Read at your usual
  pace."** The two-section instruction appears when Start is pressed
  ("Section 1 of 2. Press Next section when you reach its end"). The body
  gives the flow, so no reader is lost; a kit change would put it in the
  slot intro as `readkit.py` line 761 intends. Kit; recorded.
- **On a second visit to `scanning-for-a-target` the words box holds 613
  until the search ends**, although the museum guide (590 words) is being
  served; the tiles are the preset's until then. Correct by the kit's "two
  sources, one computation" rule, and the `panel_intro` says the boxes hold
  a worked example until the search ends. Recorded.
