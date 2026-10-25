# Second review: Remembering What You Read (Reading Faster, course 7)

Independent second read of `content/reading/c7_remembering/` (`__init__.py`,
`part_a.py`), done under `docs/reading/SECOND-REVIEW.md`. The pedagogy
assessment (`docs/pedagogy/reading-remembering-what-you-read.md`) was read
only after the findings below were written.

## Method

- Read: AGENTS.md §0, §7 and §8; `content/AGENTS.md`; PLAN §0, §B, the Course 7
  entries in §C, §D.3, §F, §G, §S and §R; the accuracy review; AUTHORING.md;
  kit-report.md; every passage the course uses (P43, P44, P45, P46, Q24, Q29),
  including their questions and idea units.
- Rendered the course with `preview_subject.py` into the scratchpad
  (`sr-reading-remembering-what-you-read/`). Read every preset's tiles with
  `labcheck.js --observe` and recomputed every figure in prose, worked lines,
  quiz answers and `why`s exactly.
- Did every drill in Chromium with Playwright, served on port 8837:
  - the free recall with questions;
  - both sides of the delayed comparison;
  - the delayed test, after moving the log's due dates back, and the due
    banner on Spacing Your Reviews in place of the warm-up;
  - the hard-band warm-up;
  - the summary variant.
- Checked against the primary source (WebFetch of the published PDF of
  Roediger and Karpicke 2006): Experiment 1's participants, passages,
  timings, initial-test recall and final-test figures.

## Arithmetic

Every figure checks:
- 383 × 60 / 95.75 = 240; 240 × 7/12 = 140; 240 × 10/12 = 200; 84/7 = 120/10 = 12 words per unit.
- 4/6 − 2/6 = 1/3; 68 − 54 = 14; 75 − 81 = −6.
- Gaps 1, 2, 4, 8, 16 → days 1, 3, 7, 15, 31; 5 × 10 = 50; quiz gaps 2, 6, 18, 54 → days 2, 8, 26, 80.
- 377 × 60 / 94.25 = 240; 240 × 6/10 = 144; 240 × 4/10 = 96; 40/6 ≈ 6.7; 90/4 = 22.5.
- "Less than a third as many words on each idea" (6.7/22.5 ≈ 0.30) and "half as many ideas again" (6 = 1.5 × 4).
- Quiz figures: 400 × 60 / 120 = 200, × 9/12 = 150; 5/6 − 3/6 ≈ +33.3; 60/5 = 12; 30/5 = 6 against 45/5 = 9.

The idea-unit counts (12, 11, 10) match the passages, and the units the
bodies quote exist verbatim. All 14 pinned tiles matched.

## The drills

Each did what its lesson says:
- **Free Recall.** The passage is hidden from Done onward, including during the
  questions. The textarea and the idea-unit checklist come in that order, and
  the entry is logged `test` with `extra.units`/`recalled`.
- **Retrieval Beats Rereading.**
  - Side A is "Read it again" with no test; side B is free recall with 11
    units. Both are logged `condition` with a due date.
  - The delayed test shows neither passage. It writes `delA`, `delB` and
    `total`, and B's units and recalled from the log, and logs `delayed-test`.
  - The banner hides the warm-up on Spacing Your Reviews.
- **Spacing Your Reviews.** The warm-up Q24 is logged `practice`.
- **Notes in Your Own Words.** It asks for "a summary of three sentences",
  counts the words correctly (31 for a 31-word summary), asks no questions and
  logs `other` with `summary: true`.

## Findings

1. **Retrieval Beats Rereading: the published-shape preset put the wrong study
   figure in "Recall at the time" (fixed).**
   - **What was wrong:** the tile `reRecallB` is labelled "Recall at the time
     (recalled passage)". The preset filled it with 75, which the body called
     "the tested group's score on the five-minute test, the nearest thing in
     these figures to a recall at the time". The study reports the recall at
     the time directly. On the initial free-recall test (the one that replaced
     the second reading), students recalled 20.9 of 30 idea units, "approximately
     70%" (Roediger and Karpicke 2006, Exp. 1, checked in the paper). The 75 is
     a final-test score, taken after a further five minutes.
   - **What I changed:**
     - preset `recalled` 75 → 70, and the pin `3/4 = 75%` → `7/10 = 70%`;
     - the body sentence now reads "Its last box holds 70 of 100, the recall at
       the time: on the free-recall test that took the place of a second
       reading, students wrote down about 70% of the passage's idea units";
     - §C 7.2 was updated to match, with the 20.9-of-30 source.
   - **Scope:** this figure is not in the accuracy review's table. It is the
     same paper and experiment as the 81/75/54/68 that §S already allows.
2. **Free Recall `concepts[1]`: "Recall scores lower for the same reading" stated
   as a law (fixed).** The two scores are on different scales: idea units
   against six questions. The body and the quiz already say "usually". The
   concept now says "Recall usually scores lower".
3. **Research claims elsewhere match §S and the accuracy review at the right
   strength.** No change was needed for these:
   - **Roediger and Karpicke 2006:** college students, short prose passages
     (256 and 275 words), free recall without feedback, 81/75 at five minutes,
     54/68 at two days, the tested group still ahead at a week.
   - **The recognition test:** the drill's multiple-choice test is flagged as
     showing a smaller effect.
   - **Spacing sources:** Ebbinghaus on his own memory for nonsense syllables;
     Cepeda et al. 2006 on spacing beating massing, with the best gap growing
     with the retention interval; Karpicke and Roediger 2007 with equal gaps
     "as well or better over the longer term".
   - **Expanding gaps:** called "one reasonable schedule, not a finding".
   - **Dunlosky et al. 2013:** highlighting, rereading and summarisation are all
     low; practice testing and distributed practice are high; trained summaries
     help.
   - **The retrieval point:** that a summary written from memory is retrieval
     is stated as the lesson's inference, which is fair.
4. **Recommendations on wording (not changed):**
   - "Ten minutes covers an article" (Spacing Your Reviews) is advice without
     a source. It is harmless but could read "Ten minutes is enough for most
     articles".
   - "the longer you need a text, the longer the gaps between reviews can be"
     extends Cepeda's verbal-recall tasks to texts. The `note` names the
     materials, which is enough.
5. **Quiz.** Every distractor was argued and failed. Each question has one
   defensible answer.
6. **Passages (report only; passages not edited).**
   - **P43 Q1** ("the ways a camel's body avoids losing water") is the longest
     and most inclusive option, and is guessable by elimination. **Q6** ("wastes
     very little of the water it has") is also guessable for a reader who knows
     the hump myth is a myth.
   - **P44 Q6 and P45 Q6** ("sums up") follow the bank's pattern of a long,
     nuanced correct option.
   - **P45 Q6** option B ("survived because it proved useful") also cues Q5.
   - None of these has two defensible answers.
7. **Voice.** It is warm, concrete and about the reader's own ticks. It makes no
   promises. The study is "presented, not endorsed" in both directions.
   Nothing is performed or preachy.

## Where I disagree with the pedagogy assessment

- **The 75.** The assessment says the published figures in the presets "are
  the published ones" and pins `3/4 = 75%` as right. The 75 is published, but
  it is not the recall at the time that the tile names. The paper gives that
  figure as about 70% (finding 1).
- **"Recall scores lower".** It was not flagged (finding 2). This one is minor.
- I agree with its other findings and repairs. It is right that P44's subject
  (penicillin) is better known than P45's, which favours the reread side. That
  is a sharper passage observation than mine.

## Final preview output

`python3 scripts/preview_subject.py reading --course reading-remembering-what-you-read`
reports: 4 page(s) executed and swept, 4 with pinned figures, 0 failing — **OK**.
