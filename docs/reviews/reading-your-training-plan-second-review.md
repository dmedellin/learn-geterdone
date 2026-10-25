# Second review: Your Training Plan (Reading Faster, course 8)

Independent second read of `content/reading/c8_training_plan/` (`__init__.py`,
`part_a.py`), done under `docs/reading/SECOND-REVIEW.md`. The pedagogy
assessment (`docs/pedagogy/reading-your-training-plan.md`) was read only after
the findings below were written.

## Method

- Read:
  - AGENTS.md §0, §7 and §8 and `content/AGENTS.md`;
  - PLAN §0, §B, the Course 8 entries in §C, §D.3, §F, §G, §S and §R;
  - the accuracy review, AUTHORING.md and kit-report.md;
  - the course's passages, with their questions: P47, P48, P49 and Q16;
  - the Daily Drill pool's bands and kinds;
  - The Daily Drill's routine and Sprints Above Comfort, for cross-references;
  - the `log/profile` fill code, read-only.
- Rendered the course into the scratchpad (`sr-reading-your-training-plan/`)
  and read every preset's tiles with `labcheck.js --observe`. Recomputed every
  figure exactly.
- Did every drill in Chromium with Playwright on port 8838, with a seeded log
  of 3 baselines, 1 practice, 1 test, 1 free recall (`test`) and 1 summary
  (`other`):
  - A Practice Week: the warm-up P49 logged `test`, and "Save this plan" logged
    a `plan` entry of kind `other`.
  - Reading Your Curve: the warm-up Q16 logged `test`. The tiles did not move
    until Show my log was pressed, which is what the body says. After the
    press, the count rose and the recall entry was not counted.
  - Plateaus and Transfer: P47 hidden during questions and logged `other`.
    With three tests in the log, `recent` filled on Score. With one test, the
    box kept the example's 270, as the body warns.
  - The Full Battery: the warm-up P48 logged `test`. "Fill from my log" listed
    the tests, the verdict used the median rule, and the recall row read
    `5/12 → 5/12` from the single free-recall test.
- Checked the Rayner et al. 2016 abstract and APS release for the
  "modest gains" sentence.

## Arithmetic

Every figure checks:
- **A Practice Week:**
  - 5 × 15 + 2 × 15 = 105; 30/105 = 2/7 ≈ 28.6%; 120 − 105 = 15; 2 × 60 = 120, 1/2; 7 × 15 = 105.
  - Quiz: 48 + 12 + 30 = 90, 12/90 = 2/15 ≈ 13.3%. "Four to six times" the session: 60/15 to 60/10.
- **Reading Your Curve:**
  - Baselines: 285.6, 294 and 251 at 5/6, 5/6 and 6/6 → 238, 245, 251.
  - real-gain tests: 314.4 and 324 at 5/6, then 281 → 262, 270, 281; median 270, 19 above.
  - noise: 292.8, 314.4, 286.8 → 244, 262, 239.
  - rate-only: 354, 360, 357 at 4/6 → 236, 240, 238.
  - Practice: 275, 280, 290 and 240 effective.
  - "Sixty or more" is 354 − 294.
- **Plateaus and Transfer:** 389 × 60 / 97.25 = 240; / 77.8 = 300; 300 × 4/6 = 200; 238 − 200 = 38; −30 and −70.
- **The Full Battery:** median(262, 270, 266) = 266, 15 above. Scan 12 → 8 is a third; 7/12 is "a little over half".
- Quiz medians: 250 and 250.

All 25 pinned tiles matched.

## Findings

1. **Plateaus and Transfer said the practice pool held no argument. It holds one
   (fixed).**
   - **What was wrong:**
     - The body called P47 "the kind of prose the practice pool did not give
       you".
     - `concepts[0]` said "a kind of text the pool did not contain".
     - `concepts[2]` said "A hard argument has never been measured for you
       before today".
     - The Daily Drill's pool is Q01–Q15 and Q26–Q28. Q27, *In Praise of the
       Dark*, is a hard-band argument. A reader who kept the routine has read
       it, possibly as a test.
   - **What I changed:**
     - The body now says "a kind of prose the practice gave you rarely, if at
       all (the Daily Drill's eighteen pool passages hold one argument)".
     - The concept now says "the pool hardly contained".
     - `concepts[2]` now says "has never been among your baselines … the
       first of its kind in your series".
     - `one_line` and the course summary now say "hardly practised".
   - The lesson's logic, that there is no baseline of the kind, stands.
2. **Plateaus and Transfer: "slower than the practised kind, as harder text is
   for everyone" (fixed).**
   - **What was wrong:** this states a universal that the Subject's own
     correction contradicts. Carver's first law is a relatively constant
     rauding rate, and accuracy finding 13 says the drop depends on how far
     above the reader's level the text is.
   - **What I changed:** "as harder text often is".
3. **"The research finds modest rate gains with comprehension held" was
   unattributed and stronger than the source (fixed in lessons 1 and 3).**
   - **What was wrong:** the sentence names no study. The source the Subject
     uses, Rayner et al. 2016, concludes that the trade-off makes doubling or
     tripling a rate with comprehension held unlikely. It does not report
     positive "modest gains" from practice. The abstract says comprehension
     at speed depends on practice and language skill.
   - **What I changed:** A Practice Week now reads "Rayner and colleagues (2016)
     concluded that doubling or tripling a rate with comprehension held is
     unlikely". Plateaus and Transfer now reads "On reading itself, Rayner and
     colleagues concluded that a large gain in rate with comprehension held is
     unlikely".
   - **Not changed:** the same sentence in Guided Practice's `how_to`
     (c2 `__init__.py`). That is another course; this is recommended to its
     reviewer.
4. **Plateaus and Transfer `mistakes[0]`: "A new kind of text tells which" (fixed,
   with §C).**
   - **What was wrong:** the body says "one reading cannot say which", but the
     misconception asserted that the does-not reading was "a gain tied to the
     practice material". That is a verdict in the lesson's own voice beyond
     the evidence.
   - **What I changed:**
     - "Readings of a new kind of text help tell which";
     - "fits a gain tied to …" and "points more toward the practice";
     - an added closing sentence: "One reading each is a start, not the
       answer";
     - §C 8.3's misconception, to match.
5. **A Practice Week: weekend-only "five days of the seven are empty, so every
   reading of the week shares one day's conditions" (fixed).**
   - **What was wrong:** two sittings with five empty days is two days, not one.
   - **What I changed:** "so the week's readings share two days' conditions,
     not five".
6. **The Full Battery: the skim and scan rows were said to keep the example
   (fixed).**
   - **What was wrong:** Course 5 now logs Scanning for a Target (`scan/find`)
     and Skimming for Gist (`gist` display) as `test`, and the profile fill
     reads `baseline` and `test` entries. Those rows therefore fill. Where the
     log holds one reading of a kind, then and now are the same reading. The
     browser showed this for recall: `5/12 → 5/12`.
   - **What I changed:** the body now says those three lessons log their drills
     as tests, so the rows fill from the log, and that with one reading of a
     kind, then and now are that same reading.
7. **The Full Battery: the closing paragraph attributed the wrong argument to
   Words, Knowledge and Difficulty (fixed).**
   - **What was wrong:** it said that course "argued that the large savings are
     in the second and third" places, a skim being enough and finding a fact.
     Words, Knowledge and Difficulty argues that knowledge, vocabulary and
     reading volume move a rate, and that ten more minutes outweighs a rate
     gain.
   - **What I changed:** the sentence now gives each course its own argument.
8. **The Full Battery quiz 3: a distractor that is arithmetically true (fixed).**
   - **What was wrong:** "A 50% gain in skimming" is a correct description of
     2/3 → 1 as a relative change.
   - **What I changed:**
     - the option is now "A gain in skimming, by the Subject's rule";
     - the `why` adds "so it is not a gain by the rule".
9. **Other research claims are at the right strength.** No change was needed:
   - Ericsson, Krampe and Tesch-Römer 1993 is cited as musicians, with the
     contested share and "borrows its shape, not a promise".
   - Rayner et al. 2016 on eye exercises is one sentence, as §G allows.
   - The median rule is called a rule of thumb, not a significance test.
   - "One time in four" matches §B.
10. **Recommendations (not changed):**
    - Reading Your Curve quiz 3 says "test rates rose from about 290". The
      baseline rates are 251–294, with a median of 285.6. "from 251–294" or
      "from about 286" would be exact.
    - Concept 1 of A Practice Week ("one long Saturday … measured five times")
      and the weekend-only preset describe different weeks. That is fine, but
      the image could name two sittings.
11. **Passages (report only; passages not edited).**
    - **P47 Q1** (main claim) is answerable from the title, *In Praise of
      Maintenance*: only one option says maintenance is undervalued. **P47 Q6**
      is close to answerable from the question's own wording.
    - **P49 Q1** is answerable from the title, *Salt from the Sea*, and the
      headings. **P49 Q6** (rain dilutes the ponds) is guessable by common
      sense.
    - **Q16 Q1 and Q4** are answerable from general knowledge of optics.
    - **P48 Q5** ("time order") is guessable from the dates in the other
      questions.
    - None has two defensible answers.
12. **Voice.** It is practical and about the reader's log. It makes no promises.
    "A plan the lab says fits is a plan, not a promise" is the right register.
    The fixes above remove the three places where the lesson's own voice
    claimed more than the evidence.

## Where I disagree with the pedagogy assessment

- **"Modest rate gains".** It praises "The research finds modest rate gains with
  comprehension held …" as the sentence the pre-authoring review asked for. I
  find it unattributed and stronger than Rayner et al. 2016, which argues the
  ceiling, not a measured gain (finding 3).
- **P47 and the pool.** It calls P47 "the Subject's only hard-band argument" and
  accepts "the kind of prose the practice pool did not give you". Q27 in the
  Daily Drill pool is a hard-band argument (finding 1).
- **The gist and scan rows.** It says those rows cannot fill because Course 5
  logs the skim `condition` and the scan `other`, and its repair named them as
  the rows that keep the example. Course 5 as it now stands logs both as
  `test` (c5 `part_a.py`, the scan/find and gist cfgs), so that repair became
  wrong. The real behaviour is "then and now are the same reading" (finding 6).
- **Missed findings.** It did not flag:
  - "as harder text is for everyone" (finding 2);
  - the misattribution to Words, Knowledge and Difficulty (finding 7);
  - the weekend-only "one day" slip (finding 5);
  - the arithmetically true distractor (finding 8).
- I agree with its browser findings, which I reproduced: Show my log is needed
  after the warm-up, and `recent` fills only with three tests. I also agree
  with its kit recommendations.

## Final preview output

`python3 scripts/preview_subject.py reading --course reading-your-training-plan`
reports: 4 page(s) executed and swept, 4 with pinned figures, 0 failing — **OK**.
