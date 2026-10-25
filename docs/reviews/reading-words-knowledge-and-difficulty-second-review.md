# Second review — Words, Knowledge and Difficulty (Reading Faster, course 6)

Independent second read of `content/reading/c6_difficulty/` (`__init__.py`,
`part_a.py`) against `docs/reading/PLAN.md` (§0, §B, the Course 6 entries in §C,
§D.3, §F, §G, §S, §R), `docs/reviews/reading-spec-accuracy-review.md`,
`docs/reading/AUTHORING.md` and `docs/reading/kit-report.md`, following
`docs/reading/SECOND-REVIEW.md`. The pedagogy assessment
(`docs/pedagogy/reading-words-knowledge-and-difficulty.md`) was read only after
the findings below were written.

## Method

- Every lesson and every passage the drills and warm-ups serve (`P38`–`P42`,
  `P01`, `Q22`, `Q23`, `Q30`) read in full; counts and grades recomputed with the
  kit's Python mirror: `P38` 395/21/504 (FRE 79.80, grade 6.80); `P39` 391/16/775
  (14.35, 17.33); `P01` 491/21/655 (70.25, 9.27); `P40` 380 words (grade 15.69);
  `P41` 385/16 (9.36); `P42` 375/18 (8.87); `Q23` and `Q30` hard band.
- Rendered with `python3 scripts/preview_subject.py reading --course
  reading-words-knowledge-and-difficulty --out <scratch>/sr-reading-words-knowledge-and-difficulty`
  and every preset's tiles read with `labcheck.js --observe`. Every figure in
  prose, worked lines, quiz answers and `why`s recomputed: all correct (300,
  170, 17/30 ≈ 56.7%, ≈ 141.7; 250, 240, 24/25, 120; 68.095 and 8.73; the
  ratios 24.44/18.81 ≈ 1.30 "about a third longer" and 1.982/1.276 ≈ 1.55 "more
  than half as many syllables again", with the word term 59.7 of the 65.5-point
  gap; 9.91; 25.38; 49/50, 19/20, 9/10, 50, 20, 10; 361/380 = 19/20, 380/19 = 20;
  240, 225, 150, 5/8, 250, 25/24 ≈ 104.2%, 6.25% "about 6%"; 15/26 ≈ 57.7%;
  1,825,000 ≈ 20.3, 2,190,000 ≈ 24.3, 2,737,500 ≈ 30.4, 912,500 ≈ 10.1 books,
  365,000 ≈ 4.1, 1,314,000).
- Every drill done in Chromium on port 8854: the easy/hard compare (both sides
  `test`, order AB on a fresh log, one-question note); the readability warm-up
  (`Q22`, `practice`) and presets; the coverage drill (380 clickable words, mark
  and unmark, "Count my marks", untimed, no questions, logged `other`); the
  familiar/unfamiliar compare (both `test`); the volume warm-ups (`Q23`, then
  `Q30`, then "already in your log"). The passage was hidden during every
  question. No console or page errors.
- Web checks: Rayner et al. (2016) full text, for the claim attributed to it in
  `what-you-already-know` (finding 6).

## Findings

### 1. "A practice reading from the Daily Drill's pool" — fixed

*Lesson:* `measuring-difficulty`, body. *Wrong:* the warm-up `Q22` is from the
Subject's practice pool but not one the Daily Drill serves (`DAILY_POOL` is
Q01–Q15 and Q26–Q28). *Changed* to "a practice reading from the Subject's
passage pool".

### 2. Verdicts beyond the evidence in `how-much-you-read` — fixed

- `concepts_intro`: "This course has shown that knowing words and knowing
  subjects change a rate more than technique does. Both come mostly from
  reading." The course measured no technique against knowledge, and "come
  mostly from reading" is causal, resting on Nagy and Herman's estimates and a
  correlational study. *Changed* to "This course has measured what knowing the
  words and knowing the subject do to a reading. Much of both is thought to come
  from reading itself."
- Body: "the order of the levers is plain … Reading more is the larger lever,
  and it is the one that makes the next text easier." The first half is earned
  by the arithmetic (on volume); the last clause is the causal reading of the
  correlation the paragraph before had just warned against. *Changed:* "Put the
  course together", "come, on the best estimates, largely from what you have
  read", and "Reading more is the larger lever on how much you read, and if the
  correlational studies point the right way, it is also the one that makes the
  next text easier."
- Course `outcomes_intro`: "four things that change a rate more than any
  technique" — the same unsupported comparison, and "how much you read" does
  not change a rate. *Changed* to "four things besides technique that shape a
  reading".

### 3. A promised result in the Daily Drill step — fixed

*Where:* the shared `DAILY` step on every lesson: "find your hold target again:
it will be lower". A prediction about the reader's own number in the lesson's
voice (§F: no promises). *Changed* to "it will probably be lower".

### 4. `unknown-words-and-coverage`, two overreaches — fixed

- "If your coverage was near 98% or above, the passage was hard for you mainly
  for the other reasons the formulas count, its long sentences and long words."
  The previous lesson's point is that the formulas miss things (dependence of
  one sentence on the last, unfamiliar ideas); the sentence told the reader what
  made it hard for them. *Changed* to "the unknown words were probably not the
  main difficulty: look instead at its long sentences and long words, which the
  formulas count, and at how much each sentence asks you to hold, which they do
  not."
- "a reader who … meets one unknown word in every 20 gains more from learning
  the field's words than from any change of pace" — no study cited compares the
  two. *Changed* to "is likely to gain more … than from a change of pace".
- "All of these studied learners of English": Nation (2006) is a corpus-based
  estimate, not a study of learners. *Changed* to "All of these concern learners
  of English". The Hu and Nation, Laufer and Ravenhorst-Kalovski and Schmitt,
  Jiang and Grabe sentences match §S and the accuracy review at the right
  strength (learners of English, one story, "some but most did not" at 95%,
  98% an estimate, contested threshold, extrapolation for native readers).

### 5. `what-you-already-know`, an unsourced inference and a stated fact — fixed

- "In a field you read often, the fastest gain available is usually to know
  more of the field" — the accuracy review's finding 14 asked for exactly this
  kind of sentence to be dropped or flagged. *Changed* to "the gain most within
  reach is often to know more of the field … That is an inference from studies
  of recall, not something they timed."
- Quiz 2: "Why did the formula not predict that most readers find the Gram stain
  harder?" asserts an unmeasured fact about most readers. *Changed* to "that a
  reader new to microbiology finds the Gram stain harder".

### 6. Rayner et al. 2016 on background knowledge — unverified; recommendation

The body and `mistakes[0]` say "Rayner and colleagues' 2016 review counts
background knowledge among the strongest influences on comprehension". This is
§C's wording and the accuracy review did not check it. In the parts of the
review I could read on the web, its emphasis is **language skill**, especially
vocabulary ("language skill is at the heart of reading speed"), and word
identification, not topic knowledge as such; I could not find a sentence that
ranks background knowledge. Not changed (it is §C's sanctioned claim and I
could not read the whole text). Recommended: either check the passage in the
review and cite it, or attribute the general claim at the strength
Recht and Leslie support and cite Rayner et al. only for "language skill,
including vocabulary, is at the heart of reading speed".

### 7. Research statements checked and right

Carver's constancy within the reader's level and the learning gear on harder
text, with units and population (college students, standard-length words);
Rayner 1998's longer fixations and more regressions on difficult text; Flesch
1948 and Kincaid et al. 1975 (Navy enlisted personnel) with the right
coefficients; Recht and Leslie's 64 junior-high students, recall and
reenactment, not speed; Anderson, Wilson and Fielding's 155 fifth-graders and
diaries, correlational; Nagy and Herman's estimate-based argument. None
stated more strongly than §S.

### 8. Passages — reported, not edited

- **`P41` Q4** ("What is the main purpose of the passage?") is answerable from
  the title, "Packing for a Week Away", alone; **Q5** (a change of clothes "in
  case your suitcase is delayed") and **Q3** (rolled clothes "crease less") are
  common travel advice. On the familiar side of a familiarity comparison some
  of this is the effect being measured, but §P rule 4 says a question must not
  be answerable from general knowledge; the guessable ones inflate the familiar
  side's score beyond what reading it earned, which overstates the familiarity
  effect. Proposed: rewrite Q4 to ask what the writer says to do two or three
  days before leaving, and Q5 to ask where the liquids bag goes and why.
- No question with two defensible answers found in `P38`, `P39`, `P41`, `P42`.

### 9. Recommendations (taste or cross-course)

- I agree with the pedagogy assessment that the hard (`P39`) and unfamiliar
  (`P42`) sides logged as `test` put hard-text rates into the standard-text
  medians of Reading Your Curve and The Full Battery, against this course's
  own thesis. Logging them `condition` is the simpler fix; §C would change
  with it.
- `your-rate-on-hard-text` body: "If your readings go the other way from
  Carver's account" — both presets are consistent with Carver, so "the other
  way" is unclear; "If your readings fit neither pattern" would say it.

## Voice

Warm, practical, about the reader's numbers; the research is cited with its
populations and limits. The failures were all of one kind, the lesson's own
voice going a step past its evidence (findings 2–5), and they are fixed. No
lesson calls a figure "your reading speed" except as the name of the
misconception it refutes.

## Where I disagree with the pedagogy assessment

1. **"No promises."** The assessment finds none; the `DAILY` step on every
   lesson promised "it will be lower" (finding 3).
2. **"Earns it with arithmetic rather than with the correlation."** True of
   "the larger lever", not of the clause that follows it ("makes the next text
   easier") or of the concepts intro ("has shown … more than technique does";
   "Both come mostly from reading") (finding 2). The course `outcomes_intro`'s
   "more than any technique" was not noticed.
3. **Rayner et al. 2016** is treated as checked ("is 'a review'"); the specific
   claim attributed to it is unverified (finding 6).
4. **The Daily Drill's pool.** The assessment praises the warm-up as working,
   which it does, but did not notice that `Q22` is not from the Daily Drill's
   pool as the body says (finding 1).
5. **Quiz.** Agreed that every distractor fails; the change to quiz 2 is to the
   stem, not to an answer.
6. Agreed with its other recommendations (hard text as `test`; pin
   `txSyllables`; the prose sentence rule is narrower than the kit's).

## Files changed

`content/reading/c6_difficulty/part_a.py` and `__init__.py`. No preset,
`expect`, slug, lab mode, view, passage or instance changed, so §C needs no
change. `python3 scripts/preview_subject.py reading --course
reading-words-knowledge-and-difficulty` after the changes: 5 page(s) executed
and swept, 5 with pinned figures, 0 failing; OK.
