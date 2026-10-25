# Pedagogy assessment — Guided Practice (Reading Faster, course 2)

Formed from the five lesson dicts in `content/reading/c2_guided/part_a.py`
and the course dict in `content/reading/c2_guided/__init__.py`, the
twenty-seven passages their drills use (`P12`–`P18`, `P23`, `P24` in
`content/reading/passages/bank_a.py`; the Daily Drill's pool `Q01`–`Q15` and
`Q26`–`Q28` in `content/reading/passages/pool.py`, every paragraph and all
162 questions read), and the kit they render through (`readkit`, views
`drill/compare` with the `pacer` display, `drill/ladder`, `drill/practice`,
`drill/repeat`, as `docs/reading/kit-report.md` records them), on branch
`feat/reading-subject` before the Subject is wired. The design authority is
`docs/reading/PLAN.md` §0, §B (practice starts here and does not stop), the
Course 2 entries of §C, §D.3 (items 4, 6, 11, 13), §E, §F and §G; the
pre-authoring pedagogy review was read for findings 1–3, 7, 8, 16–17, 22, 33
and 35, all of which land in this course.

Every lesson was read in full before anything was changed. The course was
rendered with `scripts/preview_subject.py reading --course
reading-guided-practice`; every preset's tiles were read off the rendered
pages with `node scripts/labcheck.js --observe` (35 pinned strings on five
pages, and the unpinned tiles beside them); every figure in prose was
recomputed by hand, and the presets' word counts were compared with the
passages' counts by the kit's Python mirror (`P12` 442 and `P13` 418 are the
passages' own; `P17` 484 is `P17`'s). Then the course was done in Chromium
with Playwright (`ped-c12-drills.js` in the session scratchpad), on the log
Course 1's pass had left — three baselines at 245.5, 240 and 253.2 words a
minute and one test — in course order: "Use my baseline median" and the two
readings of the pacer comparison (the page put the paced one first); the
ladder's three rungs from the same button; three Daily Drill sessions, two
paced with the attention tick and one ticked as a test; the sprint at twice
the median and the test after it; and the four readings of the repeat
drill. After each, the script checked that the passage was hidden while the
questions were on screen, that one entry of the kind §C names was written,
that self-ending displays ended by themselves, and that the tiles agreed
with the arithmetic. Lessons, in course order: `reading-with-a-pacer`,
`choosing-a-target-pace`, `the-daily-drill` | `sprints-above-comfort`,
`repeated-reading-and-transfer`. The bar marks the seam between the two
modules, The pacer | Pushing the pace. The course assumes Measure Your
Reading and a log that holds its readings, and is judged against that.

## Verdict

The course does what §B put it second to do: by the end of lesson 3 the
reader has a routine running, with a target found from their own scores, a
pool of fresh passages served in order, a tile that reads the next target
and the next test off their log, and a rule for every day. Each lesson's
objective is an act and the `standard` names it: compute a pacer's time per
line and say whether a two-reading difference is more than one question's
worth; name the hold target and the best run of a ladder and say why they
differ; state the routine's four rules and apply them to a log excerpt;
give the verdict on a reading after a sprint and say what more would make
it evidence; compute the repeat and transfer gains and name the one that
measures the reader. The quizzes ask those acts on fresh instances (10 words
at 300; a ladder at 250, 300, 375 scoring 5, 4, 3; three holds at 300; a
range of 220–236 and a test at 241; 220, 270, 310 then 232) and every
distractor was argued for and failed. The `mistakes[0]` of every lesson is
the §C misconception and is refuted with a preset's figure.

The honesty the specification asked for is kept under pressure, which is
where it matters: the tradition's claim for each technique is stated at its
strongest before it is measured ("set the guide faster than is comfortable
and keep raising it, on the view that understanding catches up with the
pace"; "after a minute at a pace you cannot follow, your ordinary pace feels
slow, and you read faster without trying"), the result is read by Course
1's rule, and every lesson says, in its own voice, that a reader whose
result went the other way has refuted nobody. The Daily Drill's `note` says
plainly that its numbers are the Subject's, chosen to be easy to keep, not a
finding; the `how_to` says to expect modest numbers and where the large
savings are. All 35 pinned strings matched the lab; every figure in prose
agreed with the lab or a recomputation; the drills ran as the prose
describes them, with one surprise and two gaps now repaired. The surprise:
the Daily Drill's "next test" tile counts every paced practice reading in
the log, so the three rungs of the ladder put a first-time reader one
session from a test; the body now says so. The gaps: the sprint page's
pacer tile (1,500 ms at 480) had no sentence, and the pacer lesson never
said which of its two readings counts in the log. The remaining defects
were the speech-engine split of inline `a × b/c = d` runs, repaired with
backticks, and the "is ≈" shape that the voice reads as "is is
approximately", reworded where the prose is the course's own.

## The voice, judged against §F

- **About the reader's numbers, warmly.** "Your two effective rates say
  which happened today"; "Read your own ladder the same way. If you answered
  four or more on every rung, your hold is the top rung and the ladder did
  not find your edge: next time, start it at your top rung"; "If your
  attention left the text, say so. It goes into your log, and it means
  tomorrow's session should be shorter, not the pacer slower." This is the
  coach §F asked for, giving the reader something to do with each outcome.
- **Try first.** Lesson 1 opens "Before you read on, do the drill below"
  and names the button to press before the paced reading; lesson 3 opens
  "Today's session is in the lab below". The `summary` and `concepts` of the
  drill-first lesson state method and question only ("None of them says what
  you will find; that is what the drill is for").
- **History as people, once a lesson.** Evelyn Wood's courses from 1959 and
  the hand swept down the page; Rayner's review "with four colleagues,
  published in 2016 after his death"; Ericsson, Krampe and Tesch-Römer's
  musicians, "and how much of expert performance such practice explains is
  disputed"; S. Jay Samuels in 1979 and Therrien's 2004 meta-analysis of
  school-age students. Each is given with what it measured and its limit.
- **Presented, not endorsed, both ways.** "Some readers find the highlight
  steadies them and their score holds; others find it hurries them past a
  sentence they wanted to read again"; "Whether practice at that edge raises
  your natural rate is a question your log will answer; this course does not
  promise that it will"; "None of this makes repeated reading worthless."
- **No promises.** The strongest sentence the course allows itself is "What
  the routine guarantees is a log in which your tests can show what
  happened, whichever way it goes."
- **One light remark**: "it is tempting to stop there." No slang, no
  first-person anecdote, no "let's".
- **Every `note` names the confounds** — two passages and a fixed or
  alternating order — and every body ends by pointing forward by title;
  from lesson 3 on, "Then today's Daily Drill" closes the body and is the last
  `step`, as §B requires.

## What the course teaches well

- **The sequence is right and each lesson uses only what came before.** The
  pacer is taught before anything is paced; the target is found before the
  routine that uses it; the routine before the two lessons that push the
  pace; and the sprint's test and the repeat drill's fourth reading are
  judged by Course 1's range and rule. In the browser, "Use my baseline
  median" filled 246 on the pacer page, 246/295/368 on the ladder and 491 on
  the sprint from the same three Course 1 baselines, which is the
  dependency the course claims.
- **The one-question yardstick is applied, not announced.** Lesson 1's
  decomposition of the steadier preset — B's rate is only 10 higher, "nearly
  all the difference is one more question right", one question at 250 is
  `250/6 ≈ 41.7` understood words a minute, give B four right and the 48.3
  becomes 6.7 — is the best paragraph in the course and the pattern the
  later compare lessons should keep.
- **`drBestTarget` is the hold, as the review asked, and the lesson teaches
  why the hold and the best run differ.** The holds-at-288 preset (hold
  288, best run 240) and holds-at-360 (hold 360, best run 240 at 288 by the
  tie rule) are both in the prose with their arithmetic, and the "Why
  practise at the hold" section gives the purpose of each figure without
  promising that practice at the hold moves anything.
- **The routine is stated as four rules a reader can keep, with a reason
  for each** that the reader has already met: the test has no pacer
  "because a paced rate is the target's, not yours"; the target moves by a
  twentieth "so that one good day or one bad one cannot move it"; "three
  holds against two misses makes it a little harder to go up than to come
  down". The attention tick is treated as the review asked (finding 22):
  shorten the session, keep the target.
- **The sprint is measured as a treatment.** Order fixed and the reason
  given; the sprint logged `condition` with no questions and the reader told
  its rate "is the target you typed"; the test after it logged `test`; the
  verdict by rate "because the range is made of rates"; and the body says
  what tests without sprints would be needed to attribute anything to the
  sprint, which is the control the drill cannot give in one sitting.
- **Repeated reading is the course's clearest experiment**, as the review
  said it would be: the repeat gain "belongs to the passage", the transfer
  gain is the only candidate, and even that "is one reading against one
  other reading, which is why it is read against your baseline range as
  well". The run here produced +100.9 and −2.8, and the prose covers both.
- **The quizzes test the act with one defensible answer**: "Because the hold
  always has the higher effective rate" and "Because the hold is proven to
  raise a reader's natural rate" as distractors for why the Daily Drill
  practises at the hold; "A test that feels faster than before" as the
  distractor for evidence; "Repeated reading raised adult readers' speed on
  new texts" for Therrien.

## What it taught badly, or said wrongly

### What the drill does that the prose did not say

- **`the-daily-drill`, body:** "The next test counts the practice sessions
  since your last test; four of them make the fifth a test." The kit counts
  every `practice` drill reading in the log, from any lesson. A reader who
  arrives from Choosing a Target Pace has three (the rungs), so the tile
  read "after 1 more practice session" before any Daily Drill session and
  "due now: make the next reading a test" after the first — not the fifth
  session the body promised. Two sentences added: paced practice readings
  from other lessons count, the ladder's rungs already stand in the count,
  and the first test may fall due sooner than the fifth session here.
- **`the-daily-drill`, body:** "Your own text has no questions, so it is
  logged as practice and its comprehension is not scored: it keeps the habit
  going, and the tests keep the measurement going." After the pool's
  eighteen passages, a reader on their own text has no scored passage for a
  test, and the sentence implied otherwise. Now says that pasted text cannot
  be a test and that tests come from the pool while it lasts and afterwards
  from the readings later lessons log as tests.
- **`reading-with-a-pacer`, body:** nothing on the page said which of the
  two readings counts in the log. The unpaced reading is logged `test` (as
  §C says) and the paced one `condition`; Course 1 taught the kinds, so one
  sentence now says which is which and that only the first counts toward a
  verdict. The same paragraph now says where "a sentence in your log" goes
  (the Add note box in Keeping a Practice Log), since this page has none.
- **`sprints-above-comfort`, body:** the after-sprint preset's paragraph
  gave `drWpmB`, `drErrB` and the verdict but not the page's fifth tile,
  "Pacer time for a line of 12 words", which reads 1,500 ms at 480 (§E rule
  2: every figure a preset shows appears in the prose). One sentence added,
  with the arithmetic and the comparison with 240.

### Speech

Every `data-say` on the six rendered pages was read. The key lines, math
blocks and worked lines read well ("one word equals 60000 over 250 equals
240 milliseconds"; "rung 1, 240 times 6 over 6 equals 240"). In prose, the
engine split every `240 × 4/6 = 160`, `288 × 21/20 = 302.4` and `268 × 5/6 ≈
223.3` into a "times" fragment, a bare fraction and an "equals" fragment,
and once ran across a full stop ("is approximately 208.3, B"); nineteen runs
in bodies, worked paragraphs, concepts, mistakes and quiz explanations are
now in the library's backtick shorthand and read as one run each. Four
places wrote "is ≈ 16.7", which the voice reads "is is approximately 16.7";
they now say "about 16.7". The kit's own panel sentence has the same shape
and is recorded below.

## Can a reader fresh from Course 1 keep the routine?

Yes, if they do lesson 3 on the day they finish lesson 2, which the
`syllabus_intro` and the last paragraph of lesson 2 steer them to. The
mechanics are explicit at every step — which box to type in, which box to
tick, which button fills what — and the browser pass found them accurate:
"Use my next target" writes the tile's figure and says why ("stay at 288
wpm"), the pool serves `Q01`, `Q02`, `Q03` in order and refuses a passage
already logged, the attention tick is stored and printed. Two things will
puzzle a careful reader and are now in the prose: the early test (above),
and that the hold tile says "not yet" until three paced readings at one
target exist, which the body already explained. The `how_to`'s third item,
"Expect modest numbers", is the sentence that will keep a reader going past
the second week, and it is in the right place.

## Repairs made in this pass

In `content/reading/c2_guided/part_a.py`: `reading-with-a-pacer`
`concepts[0]`, the layout paragraph, the steadier and no-difference
paragraphs, the one-question paragraph, `mistakes[2]`, quiz 1–3 `why`
(backticks; "about" for "is ≈"), the three-questions paragraph (where the
note goes; which reading counts); `choosing-a-target-pace` the opening and
holds-at-288 paragraphs, the one-question paragraph, `note`, `worked.after`,
quiz 1 and 3 `why` (backticks; "about"); `the-daily-drill` the three-figures
paragraph (sessions from other lessons count), the three-holds and
two-misses paragraphs, `worked.after`, quiz 1 and 2 `why` (backticks), the
own-text paragraph (what a test needs); `sprints-above-comfort` the
after-sprint paragraph (backticks; the 1,500 ms tile) and the no-effect
paragraph. No preset, `expect`, slug, module, lab key, mode, view, pool,
passage or `__init__.py` field changed, and no §C entry needed correcting.

`scripts/preview_subject.py reading --course reading-guided-practice`
reports OK after the changes: 6 pages, every lab executes and survives the
sweep, 5 pages with pinned figures, 0 failing; the Daily Drill page is
64,352 bytes gzipped, under the 67 KB ceiling, and no other page is above
42.2 KB. The Playwright pass over the five lessons reports 0 failing checks
and no console or page errors, before and after the edits, and no horizontal
overflow at 360 px on the Daily Drill and ladder pages. `python3 -m unittest
tests.test_speech` passes.

## Remaining issues and recommendations

- **The pool lasts about three and a half weeks.** Eighteen passages at one
  session a day, with every fifth a test, is fourteen paced sessions and
  four tests before the reader is on their own text, where nothing can be
  scored. After that the only scored tests in the Subject are the warm-ups
  later lessons log as `test` (one in How the Eyes Read, three in Your
  Training Plan). The review's floor was twenty-four; page weight cut it to
  eighteen on one page. A second practice page carrying `Q16`–`Q25` and
  `Q29`–`Q30` (the kit-report measured twenty passages at 64.4 KB) is a
  URL-space decision for `site-architect`; the body now at least says what
  a test needs. Not done.
- **"Sessions since your last test" counts the ladder.** The prose now
  explains it; the better fix is in the kit — count only `drill/practice`
  readings, or label the tile "practice readings since your last test" —
  and belongs to `lab-arithmetic`. The same counter would also count the
  paced practice readings of later lessons' drills, which is arguably right.
- **The "Next unread passage" line is stale after Score.** It still named
  `Q01` after `Q01` had been logged; the next Start served `Q02` correctly.
  A reader who reads the line before the second session is told the wrong
  title. Kit tier.
- **The kit's panel sentence reads "One question is is approximately 16.7
  points."** As recorded for Course 1: `One question is ≈ 16.7 points` is
  the kit's (D.3.1) and the voice reads `≈` as "is approximately". Kit
  tier.
- **`a × b/c = d` in prose** is split by the speech engine's island
  finder; worked around with backticks here, and the same shape is in the
  six courses that follow. A `speech.py` rule is the chrome-renderer tier's.
- **Lesson 1 logs its unpaced reading as `test`.** §C says so and the body
  now says so, but it means the reader's first "test" is taken minutes
  before a paced reading of a matched passage, in whichever order the log's
  parity gives. Logging it `practice` would keep the test series for the
  Daily Drill's natural-pace readings alone; logging it `test` gives the
  log an early point. Either is defensible; recorded as a §C question, not
  changed.
- **The pacer comparison is between an expository pair** (`P12`, `P13`) and
  the ladder between three expository passages; every narrative in the
  course is in the pool or the sprint. A reader who finds exposition slower
  than story will see a lower hold than their baselines (two of three
  narrative) suggest, and lesson 2's "the passages may have been harder for
  you than your baseline passages" covers it. Taste.
- **`P16`'s fourth question** offers the keyed answer and its mirror image
  ("A tower mill turns its whole body … a post mill turns only its cap") as
  two of four options, so a reader who remembers only that the two differ
  this way has a coin to toss between them. Passages are not this pass's to
  change; recorded for the passage owner.
