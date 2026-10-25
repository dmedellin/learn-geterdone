# Second review — How the Eyes Read (Reading Faster, course 3)

Independent second read of `content/reading/c3_eyes/` (`__init__.py`,
`part_a.py`) against `docs/reading/PLAN.md` (§0, §B, Course 3 in §C, §D.3,
§F, §G, §S, §R), `docs/reviews/reading-spec-accuracy-review.md`,
`docs/reading/AUTHORING.md` and `docs/reading/kit-report.md`, following
`docs/reading/SECOND-REVIEW.md`. Findings were written before the pedagogy
assessment (`docs/pedagogy/reading-how-the-eyes-read.md`) was read; the
disagreements are at the end.

## Method

- Every lesson dict read in full, and every passage the course uses (`P06`,
  `P07`, `P08`, `P21`, `P22`, `P11`, `Q19`) counted with the kit's own rule
  (`readkit_core.passage_counts`): 453, 447, 436, 484, 457, 488, 399 words,
  all standard band.
- Rendered with `python3 scripts/preview_subject.py reading --course
  reading-how-the-eyes-read --out <scratch>/sr-reading-how-the-eyes-read`;
  every preset's tiles read with `node scripts/labcheck.js --observe` on all
  six pages.
- Every figure in prose, worked lines, quiz answers and `why`s recomputed by
  hand (below).
- Every drill done in Chromium (Playwright, controlled clock) against the
  served preview: the `P06` warm-up; twenty flashes of the span drill, three
  cues each; Looking Back's pacer and mask at 300; Fewer Needless
  Regressions' unpaced and paced pair with lapse counts 4 and 1; The Speed
  Ceiling's `Q19` warm-up and the 350-wpm settings the body describes; three
  Schulte tables and the `P11` test warm-up; "Use my baseline median" with
  three baselines in the log; every page at 360 px. 51 checks across both
  courses, none failing, no console or page error.
- Research claims checked against §S and the accuracy review; Schotter, Tran
  and Rayner (2014) additionally against its published abstract (SAGE, APS
  and a press summary): trailing mask, comprehension lower with it, "not
  confined to ambiguous sentences" — all as the lessons say. The claim that
  in normal reading, trials with and without regressions were understood
  about equally well is in the accuracy review but not in the public
  abstract; I could not reach the full text to confirm it, and it is stated
  at the review's strength.

## Arithmetic (all correct)

`(6/8)/(17/20) = 15/17`, `× 255 = 225 ms`, `60,000/225 ≈ 266.7`; reg 0:
`3/4 × 255 = 191.25`, `≈ 313.7`; fix 300: `15/17 × 330 ≈ 291.2 ms`, `≈ 206.1`;
"sixty words a minute" (60.6); 453 × 15/17 ≈ 399.7 stops ("about four
hundred"); 64/8 = 8 fixations a line and one sweep, 30 × 255 ms = 7.65 s;
quiz distractors 225, 255, 168.75 (= 3/4 × 225) and 200 (= 60,000/300) each
named correctly. Span: `_span_preset` gives exactly `hits[d]` right of ten at
each distance (for each position the ten values `(i + p) mod 10` are 0–9
once), so typical prints 1 = 100%, edge 4/20 = 1/5, span left 3, right 3;
strong left 4, right 4; 60 asks over 15 positions = 4 on average; 65/8 ≈ 8.1
spans a line. Looking Back: 447/89.4 and 436/87.2 → 300; ×4/6 = 200;
270 × 5/6 = 225, × 4/6 = 180, × 4/5 = 216. Regressions: 484/121 → 240,
×5/6 = 200; 457/103.864 → 263.999 (prints ≈ 264.0), ≈ 220.0, ≈ +20.0; 116.16
and 109.68 → 250; 7/100: (3/4)/(93/100) = 25/31, × 255 = 6375/31 ≈ 205.6,
≈ 291.8, gain 25.1; one question 40–44. Speed Ceiling: 12.75, 25.5, 637.5
(≈ 9.8 lines of 65); 3 h, 1.5 h, 3.6 min; 350 → 8.925, at 190 ms → 7.7 (the
browser printed ≈ 8.9 and 7.7 with the verdicts the body gives); 1,000 needs
≤ 80 ms; 8.5 ↔ 333.3 wpm; 11.25 leaves out the saccade. Schulte: 62/25 = 2.48,
41/25 = 1.64, 21/62 ≈ a third, 25/41 ≈ 0.61, 41/27 ≈ 1.52.

## Findings and changes

Changes are in `content/reading/c3_eyes/part_a.py` only. No preset,
`expect`, slug, mode, view or passage changed; §C needs no change for these.
After them: `7 page(s) rendered … 6 page(s) executed and swept, 6 with pinned
figures, 0 failing … OK`.

1. **the-perceptual-span — a citation that attributes a finding to the wrong
   study.** "The span is also smaller on hard text and somewhat larger in
   faster, more skilled readers (Rayner, Slattery and Bélanger 2010)" puts
   both findings on RSB 2010, which is about reading speed; the hard-text
   (foveal load) effect is reported in Rayner 1998, as the accuracy review's
   finding 5(b) gives it. **Changed:** "smaller on hard text (Rayner 1998)
   and somewhat larger in faster, more skilled readers (Rayner, Slattery and
   Bélanger 2010)".
2. **the-perceptual-span — the reader's result asserted.** "Your own drill
   puts a number on why that is a large claim: past three or four letters
   either side, even unrelated letters with your full attention on them were
   mostly guesses" (body) and "it ended a few letters from the centre too"
   (`mistakes[0]`) tell the reader what their drill showed before knowing it;
   a reader can score 3/4 at ±5 by luck with four asks. The lesson is not
   drill-first, but §F's "about the reader's own numbers" cuts the other way
   here. **Changed:** "If your own drill came out like the typical preset, it
   puts a number on…"; `mistakes[0]` now says "in the typical preset it ends
   three letters from the centre".
3. **the-perceptual-span — the sampling caution understates the noise.** The
   body says twenty flashes of three cues "ask each position only about four
   times". That is the mean; in the browser one run asked position −4 not at
   all, the centre once and −1 nine times (the cues are drawn at random). A
   position asked once or never cannot carry a "half or more" verdict.
   **Changed:** body adds "on average (the positions are drawn at random, so
   some are asked more and some hardly at all)"; `mistakes[2]` adds "on
   average, and by chance some far fewer". The page's accuracy table already
   prints each position's count (`2 of 10`); the lesson could point at it
   (recommendation below).
4. **looking-back — an unsupported comparative claim.** "If anything, it
   costs less than their mask did" is a guess, and the kit's mask works on
   the pacer's schedule, not the eyes': in the browser, 20 s into the masked
   reading, 99 spans above the highlight were hidden, so a reader who lags
   the highlight loses the end of a line before reading it — a cost the
   study's trailing mask never imposed. **Changed:** "It is a different
   manipulation, so its cost need not match theirs: it hides less of what you
   have read, but it hides lines on the pacer's schedule, not your eyes', so
   a reader who falls behind the highlight can lose the end of a line before
   finishing it." This is also a confound worth a line in the `note`
   (recommendation).
5. **fewer-needless-regressions — a result predicted in the lesson's voice.**
   "Most readers who try this find the second number smaller" is an
   empirical claim about readers with no source in §S, and it predicts the
   reader's own result. §F: the tradition's experience is stated as the
   tradition's. **Changed:** "The pacer's advocates expect the second number
   to be smaller: the pacer gives the eyes a place to be…", keeping the rest
   of the paragraph ("That is the experience the tradition reports…").
6. **fewer-needless-regressions — the count the body asks for is not the
   count the page asks for.** The body says to count "how many times you lost
   your place or re-read for no reason"; the box after Done reads "Times my
   attention left the text". A reader whose attention drifted without losing
   the place would not know which to count. **Changed:** the body now asks
   for "the times your attention left the text: you lost your place, or
   re-read for no reason" and quotes the box's label.
7. **training-the-periphery — log wording.** "logged as a test, so it joins
   your baseline and tests" — a test reading joins the tests, not the
   baseline. **Changed:** "so it joins your test readings".
8. **the-speed-ceiling — "fixations under 50 ms, a quarter of the
   average".** 50/225 ≈ 22%. **Changed:** "less than a quarter of the
   average".

## Checked and sound

- Javal/Lamare/Hering as Wade and Tatler; Rayner 1998's 200–250 ms, 7–9
  letters, 20–35 ms, 10–15% of saccades, 3–4 left / 14–15 right, 7–8
  identified; 175–200 ms latency; Pollatsek et al. 1981 for Hebrew;
  McConkie and Rayner 1975 described as the moving window with the
  asymmetric figures attributed to "Rayner's 1998 review" (as the accuracy
  review asks); Carver 1985's "about 600" with speed-reading graduates among
  those tested; Rayner et al. 2016 for skipping and short fixations at
  350–400 and for weak transfer from eye exercises; "brain-training games"
  in one sentence, as §G allows. Brysbaert's 238/260. Nothing promised;
  the 25-wpm figure is labelled illustrative three times.
- The drills match their text: warm-ups fill none of the model boxes; the
  span drill is a +, 15 letters for 150 ms (measured 150 to 150 ms on the
  controlled clock), a `#` mask, three cued positions with four letters and
  "not seen", logged `other`; both compare pages hide the passage during
  every question (checked on all 24 questions), log `condition`/`test` as
  §C says, alternate the order and record it; B's verdict is absent when B is
  paced, as both bodies say; Schulte logs `other` with its time, `P11` logs
  `test`; "Use my baseline median" fills both boxes on Looking Back and B's
  on Fewer Needless Regressions, as the bodies now say.
- Quiz: one defensible answer in each of 21 items; every distractor argued
  for and rejected. Weakest: the-perceptual-span Q1 tests what the tile
  prints (the pedagogy assessment's point; agreed).
- Passages: `P07`/`P08` and `P21`/`P22` are matched within 11 and 27 words
  and under one grade. No question found guessable without reading.

## Recommendations (not changed)

- Looking Back's `note` could add the pacer-schedule confound of finding 4.
- The span page could tell the reader to read the "n of m" column before the
  span tile, since the drill's asks are uneven.
- `Q20` (warm-up in Course 4) is a near-twin of `P21` used here (the pedagogy
  assessment's point; agreed) — for the passages owner.

## Where I disagree with the pedagogy assessment

- It quotes "Most readers who try this find the second number smaller… That
  is the experience the tradition reports" as an example of presenting the
  tradition fairly. The first sentence is the lesson's own unsourced claim
  about readers and predicts the reader's result; changed (finding 5).
- It praises the span misconception as refuted "by the reader's own span
  ending 'a few letters from the centre too'". That asserts a result the
  reader may not have; changed (finding 2).
- It accepts "about four times" per position as the sampling caution; the
  browser showed asks from 0 to 9 per position in one run (finding 3).
- It did not flag "If anything, it costs less than their mask did" (finding
  4), the misattributed hard-text finding (finding 1), or the mismatch
  between the body's count and the box's label (finding 6).
- Agreed with its repairs (the "Finish when you can…" heads, the
  baseline-median button clauses, the book-time sentence) and with its
  recommendations on the span quiz item and the `P21`/`Q20` twins.
