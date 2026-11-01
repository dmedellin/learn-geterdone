# Review (accuracy and teaching): Accelerate, Course 6 — The Science Behind the Book

Course: `accelerate-the-science` (`content/accelerate/c6_the_science/`, `__init__.py`,
`part_a.py`, `part_b.py`), seven lessons. Reviewed 2026-11-01 against the private extraction
(PDF pp. 15–16, 49–53, 170–196, 268–273). I wrote only this file.

## Gates

- **Preview:** `preview_subject.py accelerate --course accelerate-the-science` rendered
  8 pages. labcheck: 7 executed, 7 with pinned figures, 0 failing. **OK**.
- **`quotes.py`: 7 quotations, all OK.** L1 p. 170 (22 words), L2 p. 176 (16), L3 p. 178
  (20), L4 p. 180 (13), L5 p. 186 (14), L6 p. 191 (15), L7 p. 196 (15). Each lesson has one
  quotation, so every lesson is under 40 and under 60. None is a chapter's first sentence.
- **`overlap.py … 8`:** every run is a counted quotation, a section title, an answer
  option (deploy and lead-time options), the measure names, or the Course 7 lesson title.
  No other run.
- **Browser (Playwright, chromium, `file://`):** all seven lessons at 375 px and 1280 px.
  No page scrolls sideways and there are no page or console errors. Every preset's tiles
  match the pins and the prose. I typed in each exercise, and each agrees with its quiz
  `why` except L1 (range 5, then "none: every value occurs 4 times"; MF-1) and L7
  (signal 3 left out prints 0.140; MF-7). Flipping every L4 code (7 − x) leaves the
  groups and costs unchanged, as mistake 1 says.
- **Arithmetic, re-derived exactly (Fractions).** Every worked line and every figure in
  the prose is right, apart from MF-1, MF-6 and MF-7. I checked the L2 sums, the L3
  S's (pooled 1/6), the eight L4 Ward costs (sum 344/3), the L5 and L6 means, and L7's
  1114/1209 and 712/1167. The relation kr/(1 + (k − 1)r) holds for equal variances.

## MUST-FIX

1. **`part_a.py:370, 374, 376, 385` — L1 quiz 2 has the wrong range and the wrong mode.**
   For `1, 5, 5, 5, 6, 6, 6, 6` the range is 6 − 1 = **5**, and the lab prints 5. All
   three options that say "falls from 6 to 1" are wrong, the keyed one included. Change
   each to "falls from 5 to 1". For the changed set the lab prints "none: every value
   occurs 4 times", but the `why` says 5 and 6 tie as modes. Replace the last sentence with:
   "The mode also changes: 6 appears four times in the first set; in the second, 5 and 6
   each appear four times, which the lab reports as no mode, since every value occurs
   equally often."

2. **`part_a.py:1030–1031` (L3 Q3, flagged) and `896–898` — the keyed answer uses causal
   words.** "Runs through" is the word for mediation, and "large changes draw more
   comments" says size acts on comments. That is the reading the lesson warns against, and
   it lets a reader argue that the distractor "Size causes both" says the same thing. Use
   for the option: "Most of the correlation over all rows comes from the differences
   between the three sizes' averages". In the body use: "most of the correlation between
   comments and days comes from the differences between the sizes. Large changes have
   more comments and also took longer, …".

3. **`part_a.py:1206–1207, 1237–1241` — fail-rate bands credited to the book.** The book
   lists answer options for deployment frequency, lead time and restore (pp. 49–50), but
   none for change fail rate. Its 0–15% and the other ranges come from Tables 2.2 and 2.3
   (pp. 52–53). The kit report says 61–75% and 76–100% are "the lab's own". So "the lab
   reads in the book's words as … 76–100 percent" is false. Replacement: "…the second is
   2, 1, 2, 1, which reads as between once a month and once every six months, more than
   six months, between one month and six months, and 76–100 percent, the last a band the
   lab adds beyond the ranges the book reports". At 1206, write "the best answer on each
   scale (on demand, less than one hour, and the lowest fail-rate band, 0–15 percent)".

4. **`part_a.py:1686–1698` (L5 Q3, flagged) — "loaded" can be argued for.** The book
   defines a loaded question as one that forces an answer that isn't true for the
   respondent (p. 185). The `why` says that someone who finds releases quick but not safe
   "has no honest answer", which is that definition. Also, "A push poll" is ruled out by
   the stem's "four common weaknesses". Replacement stem: "Which survey weakness does
   &ldquo;Are releases quick and safe?&rdquo; show?" Replacement `why`: "It asks about two
   things at once, speed and safety, so the reader cannot tell which half a yes or a no
   was about. A loaded question presumes something about the respondent that may be false,
   as the chapter's example of asking where someone took an exam does; this one presumes
   nothing. It does not steer toward an answer, and it is not trying to persuade."

5. **`part_b.py:428` — alpha is misdefined as running "from 0 up to 1".** Alpha is at most
   1 and can be negative when items covary negatively. The kit report says so and prints
   −108 for its example. Use: "A figure of at most 1, and below 0 when items move
   against each other, for how well a set of items measure together, …".

6. **`part_b.py:529–532` and `680` — the explanation of the frozen signal is wrong.**
   Frozen "at 4 from day 5", signal 4 reads 1, 4, 4, 4, 4, 4, 4, 4. It still varies (spread
   63, variance 63/64). Alpha is 1352/1463 ≈ 0.924 because its one low day agrees with the
   others. It is not because it "does not vary". A truly constant signal would lower
   alpha to 206/251 ≈ 0.821. Replacement: "alpha in this sample would be 0.924, because the frozen
   readings sit in the middle of the others' range and its one low day, day 1, still
   agrees with them; a stuck signal that contradicts nothing does not pull alpha down." At
   680, "stays at 0.924" should be "is 0.924, slightly higher".

7. **`part_b.py:637` (L7 Q2, flagged) — 0.139 against 0.140.** 6/43 = 0.13953…, which is
   0.140 to three places. The lab prints 0.140 and the `why` says "(0.140)", but the option
   prints 0.139. Use "without signal 2 it is 0.140". The other distractors are wrong
   on a computable point and cannot be argued for.

## SHOULD-FIX

1. **`part_a.py:1167–1171, 1412` — the 2016 exception is left out.** Appendix C says the
   high-best and low-worst pattern held "in all years except 2016" (p. 273). In Table 2.2,
   the 2016 low performers' fail rate (16–30%) beats the medium group's (31–45%). The
   lesson cites Appendix C, so add: "(Appendix C notes one exception, 2016, which Chapter
   2 discusses)".
2. **`part_a.py:519–520, 731–736` — r as a percentage.** The book itself writes "94.71% or
   r = 0.9471" (p. 176). Say so, so that the lesson corrects a habit the reader will meet
   in the book: "The book itself writes the figure as 94.71 percent; r is not a percentage
   of anything."
3. **`part_a.py:907–909`.** The pooled 0.96726 is below the overall 0.96729, and the last
   tile says "smaller in size, the same sign". "Changes nothing" contradicts the tile. Use
   "barely changes it (the last tile still calls it smaller, in the fourth decimal)".
4. **`part_a.py:925–928`.** "The same scheme of hypothesis and test also serves for
   grouping teams without a hypothesis" contradicts itself. Use: "Not every analysis in
   the book starts from a hypothesis. The next lesson …".
5. **`part_a.py:1247–1250`.** In the group of six, only the fail median (4.5) falls between
   codes. The lead median is (4 + 6)/2 = 5, a code nobody in the group chose. Use "has
   medians that are means of two middle codes: the fail median, 4.5, prints both
   neighbours, and the lead median, 5, is an answer no team in the group gave".
6. **`part_b.py:355` — "The authors kept both".** The book says the tests revealed two
   constructs and that the second is predictive (pp. 194–195). It does not say the first
   was kept. Use "The authors report both".
7. **Close paraphrase** (5–7-word near-runs that the 8-word scan misses): `part_a.py:539–541`
   and `1070–1071` (fishing in the data and minds filling in the story, p. 176);
   `828–830` (profits and control groups, p. 178); `839–841` (more evidence, more
   confidence, p. 178); `220–221` (dataset "and, by extension", p. 173); `part_b.py:105–108`
   and `309` ("not supposed to be related are … unrelated", p. 191); `461–465` (the
   source-code change and its "better chance of being detected", p. 196). Recast each in
   the lesson's own syntax.
8. **Answer position.** 27 of the 28 quiz items key option A (`"c": 0`), and nothing
   shuffles them at render. Vary `c` (subject-wide, 145 of 181 items are `c: 0`).

## NOTE

1. `part_a.py:1097`: the comment says 14 words; `quotes.py` counts 13.
2. `part_a.py:1202`: "always increasing" should be "never decreases". Ward's costs are
   monotone, and ties are possible.
3. Appendix C (p. 269) says "cutoff for CR" under alpha, a typo; reading it as alpha's is right.
4. `__init__.py` `not_covered`: Chapters 12 and 13 do not name the bias tests; Appendix C
   does.

**Verdict:** exact labs, a fair reading; fix the seven MUST-FIX items before release.
