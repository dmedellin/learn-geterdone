# Second review — Skimming, Scanning and Previewing (Reading Faster, course 5)

Independent second read of `content/reading/c5_skim_scan/` (`__init__.py`,
`part_a.py`, `part_b.py`) against `docs/reading/PLAN.md` (§0, §B, the Course 5
entries in §C, §D.3, §F, §G, §S, §R), `docs/reviews/reading-spec-accuracy-review.md`,
`docs/reading/AUTHORING.md` and `docs/reading/kit-report.md`, following
`docs/reading/SECOND-REVIEW.md`. The pedagogy assessment
(`docs/pedagogy/reading-skim-scan-and-preview.md`) was read only after the
findings below were written.

## Method

- Every lesson, and every passage the drills serve (`S01`, `S02`, `P32`–`P37`,
  `B01`, warm-up `Q21`), read in full; passage counts and grades recomputed
  with the kit's Python mirror (`readkit_core.passage_counts`, `gist_words`,
  `section_starts`): `P32` 594 words, 141 shown by the gist display; `P33` 410,
  `P34` 387; `P35` 451, `P36` 433; `P37` 578, split 292 + 286; `S01` 613; `B01`
  586.
- Rendered with `python3 scripts/preview_subject.py reading --course
  reading-skim-scan-and-preview --out <scratch>/sr-reading-skim-scan-and-preview`
  and every preset's tiles read with `node scripts/labcheck.js --observe`,
  including the unpinned ones (`drRatio`, `drErrDiff`, `drVerdictB`,
  `scWordsPerSec` on inspect). Every figure in prose, worked lines, quiz answers
  and `why`s recomputed by hand: all correct (scan 40/5 = 8, 613/40 ≈ 15.3,
  919.5; 95/4 = 23.75; 47/198 ≈ 23.7%, 4.5 and 3 a minute, 891 and ≈ 668.25;
  615, 258, 307.5, 512.5; 246, 164, 173.2, +9.2, 205, ≈ 144.3, ≈ −60.7, 216.5,
  52.5; 75 and 42 s; 60, 43.2 (23/36), 40 (32/36 = 8/9), 333.3, 30 min and 7/9,
  15,000/275 ≈ 54.5, 15.6; 292, 165, ≈ 211.5, ≈ 176.2, 240, ≈ 238.3, ≈ 239.2,
  ≈ 159.4; every quiz key).
- Every drill done in Chromium (Playwright, controlled clock), served on port
  8853: the scan of `S01` (mouse, keyboard, one wrong click, one skip) and the
  second visit serving `S02`; the 40-second gist skim (ends by itself, four gist
  questions); the skim/read compare (A ends at 40 s, six questions per side, gist
  and detail tiles); the preview compare (preview replaced by the whole passage
  at 30 s, 150 s counted); the inspection of `B01` (one skip, and a run left to
  hit the 300 s limit, which ends the drill and logs 300 s); the triage warm-up
  (`Q21`, `practice`, plan tiles untouched) and the choice buttons; the
  two-section reading (Next section at 60 s, Done at 104 s, attention tick,
  questions in passage order with the last three on the report). In every slot
  the passage was hidden (`rdText` empty, `display:none`) during every question;
  every drill wrote one log entry with the kind the lesson states. 123 checks,
  0 failing, no console or page errors. Script:
  `<scratch>/sr3pw/drills.js`.
- Research claims beyond §S checked on the web: Duggan and Payne (2009) from the
  accepted manuscript's abstract and method (see finding 1).

## Findings

### 1. Duggan and Payne (2009) misstated in three lessons — fixed

*Lessons:* `skimming-for-gist` (body), `what-skimming-costs` (body and
`mistakes[0]`), `triaging-a-reading-list` (body); also §C 5.3's misconception.

*What was wrong.* Every lesson said Duggan and Payne found that skimmers "did
better on the important points than readers made to go through the whole text
at the same speed … and still worse than a full reading". The study (JEP:
Applied 15(3), abstract and method checked in the authors' manuscript) gave
readers time to read only half of each expository text. Experiment 1's
comparison condition was **reading half of the text at a normal pace**, not
being pushed through the whole text at the skimmer's speed; skimming improved
memory for **important ideas** but **not** for less important details or
inferences; Experiment 2 found no advantage of skimming over reading the first
or second half of every paragraph; Experiments 3A/3B found the advantage
depended on how easily readers could navigate the text. There was **no
untimed full-reading condition**, so "still worse than a full reading" is not
their finding (it is Masson 1982's comparison with normal reading, and the
lessons already cite Masson for it). The accuracy review's finding 10 introduced
the "forced through the whole text at the same speed" wording; it was then
carried into §C and all three lessons, and the pedagogy assessment quoted it as
"given at strength".

*Changed.* All three lessons now say: with time for only half a text, readers
who skimmed all of it remembered more of its important ideas than readers who
read half of it, but no more of its less important details (in
`triaging-a-reading-list`: and the advantage depended on how easily they could
move around the text). "Still below a full reading" is no longer attributed to
Duggan and Payne. §C 5.3's misconception updated to match, with "they had no
untimed full-reading condition".

### 2. "Five times and prices" — fixed

*Lesson:* `scanning-for-a-target`, `worked.after` and `mistakes[0]`.
*Wrong:* both said the reader took in "five times and prices". `S01`'s five
targets are two times (08:15, 23:15), a fare (£38.50), a ship's name
(Kittiwake) and a check-in rule (20 minutes). *Changed:* `worked.after` now
lists them; the mistake says "the five answers".

### 3. A quiz distractor that is partly true — fixed

*Lesson:* `scanning-for-a-target`, quiz 4 ("Why does only your first search of
the timetable count …"). *Wrong:* the distractor "The kit chooses different
targets on a second visit" describes something the kit does: a second visit
serves a different document (`S02`) with its own five targets, as the lesson's
own body says. A reader who remembers the body can defend it. *Changed* to "A
second search is given a shorter time limit", which nothing in the kit or the
lesson supports.

### 4. Course blurb: "fits an hour" — fixed

*Where:* `__init__.py` `blurb`. *Wrong:* "plan a reading list that fits an
hour". The pile takes an hour to read whole; the budget it must fit is 45
minutes. *Changed* to "fits a 45-minute budget".

### 5. "Nothing in this course is the practice pool" — fixed

*Where:* `__init__.py` `how_to[2]`. *Wrong:* `triaging-a-reading-list`'s warm-up
is `Q21`, which is from the practice pool (`pool.py`), though not one the Daily
Drill serves (its pool is Q01–Q15 and Q26–Q28). *Changed* to "None of this
course's drills replaces it".

### 6. "Choosing what not to read saves more time than any rate gain" — fixed

*Lesson:* `triaging-a-reading-list`, `mistakes[0]`. *Wrong:* a verdict in the
lesson's voice beyond what the lesson shows: in this pile triage saved 20
minutes, which a 50% rate gain (250 → 375) would also save. §F forbids
verdicts the evidence does not support. *Changed* to "saved more time here than
a rate gain you could count on".

### 7. Log kinds of the scan and the skim, and a side effect — §C fixed; kit gap reported

*Lessons:* `scanning-for-a-target`, `skimming-for-gist`. The lessons log `test`
(the pedagogy pass changed them from §C's `other` and `condition` so The Full
Battery's profile can read the scan and gist rows). Verified in Chromium:
`kind: test, mode: scan, view: find` and `kind: test, display: gist`; and in the
kit, `rdIsReading` keeps both out of every rate, range and median. §C 5.1 and
5.2 now record `test`, with the reason.

*Side effect not noted before:* `rdSinceTest` (`readkit.py`, the Daily Drill's
"test due" counter) resets on **any** log entry of kind `test`, including a scan
or a gist skim, which are not readings. A reader who does either lesson resets
the Daily Drill's "a test is due after four practice sessions" count without
having taken a test reading. Recommended kit fix (not made; `scripts/` is out of
scope): count only `rdIsReading(e)` entries in `rdSinceTest`'s reset.

### 8. Kit wording — reported

The scan result line reads "1 wrong clicks" (plural after 1). Kit; recorded.

### 9. Passages — reported, not edited

- **`P32` Q4** ("What is a fjord, as the passage describes it?") is asked after
  the gist display, which shows only headings and first sentences. The word
  "fjord" is in the *second* sentence of "Where the sea came in", so it is never
  on screen during the skim: the question can be answered only from general
  knowledge, or by matching the first sentence to the option. Proposed fix: ask
  "What happened when glaciers that reached the coast melted back?", which the
  shown first sentence answers.
- **`P32` Q2** (U against V valleys) is answerable from general knowledge by
  many readers; the shown first sentence does carry it, so it is a mild case.
- **`P34` Q2** ("The Latin word for a layer") is guessable from *stratum*.
- No question with two defensible answers was found in `P33`–`P37`.

### 10. Recommendations (taste)

- `what-skimming-costs` prints `drRatio` (172/205 ≈ 83.9%) and `drErrDiff`
  (−49.5 wpm) while its body argues the effective rate is the wrong basis;
  `ratio: False` would drop the first. (The pedagogy assessment says the same.)
- `shifting-gears`: the rigid preset's per-section split (3 of 3 on the story,
  1 of 3 on the report) is a stated example the kit cannot record; "say" rather
  than report it.
- `shifting-gears` body: "when a text is harder, their understanding tends to
  give way rather than their speed" is Carver's finding *within the reader's
  level*; add "within their level", as Course 6 lesson 1 does.

## Voice

Warm, practical and about the reader's numbers throughout; the speed-reading
tradition is not this course's subject, and no lesson promises a gain or calls
a figure "your reading speed". The two exceptions found (findings 4's "fits an
hour" is a fact error, finding 6 a verdict) are fixed.

## Where I disagree with the pedagogy assessment

1. **Duggan and Payne.** The assessment quotes "skimmers who choose where to
   look do better on the important points than readers forced through the whole
   text at the same speed … still below a full reading" as research "given at
   strength". Neither half is what the study compared (finding 1). This is the
   kind of error the second review exists to catch, and it came from the
   accuracy review's own suggested wording.
2. **"Five times and prices."** The assessment praises the mistake that says
   "nothing understood but five times and prices", and two paragraphs later
   lists the targets' forms correctly as "a time, a fare, a time, a name, a
   duration". The two cannot both be right (finding 2).
3. **"Every distractor … could not be defended."** Quiz 4's "different targets
   on a second visit" can be defended from the lesson's own body (finding 3).
4. **The log-kind change was judged safe.** It is safe for the rate curve, as
   the assessment shows, but it resets the Daily Drill's test-due counter
   (finding 7).
5. Not noticed by the assessment: the blurb's "fits an hour", the `how_to`'s
   "nothing … is the practice pool", and the "any rate gain" verdict
   (findings 4–6). I agree with its remaining recommendations (the two
   `drRatio` tiles, the rigid preset's per-section claim, the sections slot's
   pre-Start prompt).

## Files changed

`content/reading/c5_skim_scan/part_a.py`, `part_b.py`, `__init__.py`; the
Course 5 entries of `docs/reading/PLAN.md` §C (5.1 and 5.2 log kinds, 5.3
misconception). No preset, `expect`, slug, lab mode, view, passage or instance
changed. `python3 scripts/preview_subject.py reading --course
reading-skim-scan-and-preview` after the changes: 7 page(s) executed and
swept, 7 with pinned figures, 0 failing; OK.
