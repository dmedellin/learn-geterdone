# Review (accuracy and teaching): Accelerate, Course 7 — Surveys, Data and Statistical Methods

Course `accelerate-surveys-and-data` (`content/accelerate/c7_surveys_and_data/`), six lessons,
reviewed 2026-11-01 against the private extraction (PDF pages). I read Ch. 14–15, App. C
pp. 266–273, the foreword and pp. 49 and 185–186 with `page.py`/`book.py`. I did not read
`site/` and wrote only this file.

## Gates

- **Preview:** `preview_subject.py accelerate --course accelerate-surveys-and-data` rendered
  7 pages; labcheck 6 executed, 6 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 6 quotations, all OK.** L1 p. 198 (14 words), L2 p. 205 (14), L3 p. 214 (17),
  L4 p. 268 (10), L5 p. 270 (19), L6 p. 271 (12). One quotation per lesson, all under 40.
- **`overlap.py … 8`:** every run is a title or a counted quotation. "In Chapter 15, The Data
  for the Project" is the title plus "in".
- **Browser (Playwright, chromium, `file://`):** all six lessons at 375 px and 1280 px, with
  scrollWidth = clientWidth, no page errors and no console errors. I loaded every preset and
  typed in every exercise. Every tile matches the pinned figures and my own arithmetic.
- **Statistics re-derived by hand: all right.**
  - **Chi-square.** E = row·column/N and χ² = Σ(O−E)²/E. The four tables give 2/9, 12.5, 1.6
    and 16/3. 3.841 and 5.991 are the correct 0.05 critical values.
  - **AVE and CR.** Σλ²/k and (Σλ)²/((Σλ)² + Σ(1−λ²)) are the standard standardized-loading
    forms. Every AVE, CR and √AVE tile, and the test counts 14/10/15/13, match exact rationals
    (e.g. 483/800 and 1,922/2,239). release-readiness passes 0.80 only because 0.64125 > 0.64.
  - **Pearson and least squares.** r = Sxy/√(SxxSyy), b = Sxy/Sxx and a = ȳ − b·x̄ give 0.8,
    −0.4 and 0 on the three presets, and 0.5 with ŷ(8) = 3.5 on the exercise.
  - **The rest.** The L2 means (4.85, 119/24, 54/11) and the shift formula (s − m)/n are right,
    and so are the L1 medians and the L3 trees and shares.

## MUST-FIX

1. **L1: the lab prints the durations differently from the prose.**
   - `part_a.py:277,282,287,290,292,441` give 37 hours, 26 hours, 2.5 hours and "11 hours too
     long". The tiles read `1 d 13 h`, `1 d 2 h` and `2 h 30 min`.
   - The exercise and quiz 1 (`:389–400`) give 35 and 25 hours; the lab prints `1 d 11 h` and
     `1 d 1 h`.
   - Add the lab's form at first use:
     - `:277`: "a median lead time of 37 hours (the lab prints 1 d 13 h)".
     - `:287`: "26 hours (1 d 2 h)".
     - `:282`: "2.5 hours (2 h 30 min)".
     - Quiz 1 `why`: "…so the median is 25 hours, which the lab prints as 1 d 1 h."
2. **L2: the lesson overstates what Appendix C's tests catch** (`part_a.py:608–610` and
   `:780–783`).
   - The lesson says the bias tests "address" a bias many respondents share, "such as being
     told to answer well". It also says "That is why Appendix C runs tests for bias".
   - The book's footnote (p. 208) warns against telling people to answer positively. Appendix C
     (pp. 267–268) lists early-against-late and common-method tests and gives no such purpose.
     Neither test can detect respondents who were told to answer well.
   - Replace `:608–610` with: "…the pooled estimate does not reach a bias shared by many
     respondents. Appendix C's tests, read in Tests for Bias, look for two such patterns,
     early against late answering and common method bias; a survey that tells people to answer
     well is guarded against only by how it is run, as the chapter's footnote says."
   - Replace `:781–783` with: "Appendix C does test for two shared patterns, early against late
     responders and common method bias, and the authors describe the survey as giving a
     reasonable assurance, not proof."
3. **L2: the passage closely paraphrases pp. 203–205** (`part_a.py:547–571`).
   - At 6 and 7 words, the overlap scanner finds seven runs in two paragraphs, in the book's
     order: "it takes only one bad actor to", "carefully identified measures, latent constructs,
     and statistical", "one or a few people can change", "a highly motivated bad actor with",
     "one or a few data points", "depends on the size of the group", and "to make a noticeable
     difference—that is".
   - That is close paraphrase of a passage (PLAN §E). Rewrite both paragraphs in the lesson's own
     syntax. For example: "A log can be bent by a single person, whether by intent or by an
     unreviewed mistake, and because a business usually watches a handful of its numbers, the
     error can sit there for a long time. A survey's liars are diluted by everyone else who
     answered…". Keep the quiz option, which the rules allow as an answer option.

## SHOULD-FIX

1. **L1 quiz 1 `why` (`:399–400`).** "not the one the book's lead-time question asks for" has
   no support: p. 49 offers options and names no statistic. Use instead: "…which is a different
   statistic; the question asks for the median."
2. **L1 exercise (`:317`).** "Find the measure the log gets right": none of the measures you
   compute is right. Deploys, median and fail rate all differ, and there is no incident to give
   a time to restore. Only the answer options agree (both "between one day and one week";
   frequency "between once per day and once per week"). Use instead: "Find the measure the log
   gets most wrong, and the answer options that stay the same."
3. **L2 `:553`.** "Engineers trust logs because they understand…" The book says "Perhaps it is
   because" (p. 204). Use instead: "The authors suggest engineers trust logs because…"
4. **L2 quiz 3 `why` (`:750–752`).** 7 − answer gives 0 for a 7; it does not give 6. Use
   instead: "The 0 comes from taking 7 minus the answer, which sends the scale to 0–6; the 6 is
   one less than 7, with nothing reversed correctly."
5. **L3 `:895`.** "the marketing databases of Puppet and of two of the authors": p. 212 calls
   only Puppet's lists marketing databases. Kim's and Humble's were their own readers'
   databases. Use instead: "Puppet's marketing databases and the databases of Gene Kim's and
   Jez Humble's readers".
6. **L4: the lesson never says which test the book used for early against late.** The appendix
   says t-tests were used for early against late (p. 267), and the lab runs a chi-square test on
   that split. Add after `:1203`: "The lab applies the chi-square test, which the appendix lists
   for categorical answers, to the early and late split; that pairing is the lesson's."
7. **L4 `:1213–1215`.** The continuum assumption is stated as a fact, though the lab's own
   status line calls it "an assumption, not a finding". Use instead: "The assumption is that
   people who answer late are, a little, more like…"
8. **L4 exercise (`:1284`).** "which cell contributes least": two cells tie (both early cells
   give 1). Use instead: "which cells contribute least".
9. **L5 `:1520–1521` and `:1707`.** "the confirmatory kind was used once": p. 269 says "in
   almost all cases" EFA was used and calls transformational leadership "one notable
   exception". Use instead: "the notable exception was…" and "which it names as an exception".
10. **L5: the CR threshold differs between prose and lab.** The prose and steps say CR "above
    0.70" (`:1465`, `:1475`, `:1647`). The lab tests "CR at least 0.7" (status line), and the
    book's word is "cutoff" (p. 270). Use "at least 0.70" for reliability, or set `cr_min` and
    the rule to match.
11. **L5 quiz 2 stem (`:1694–1697`).** The stem leaves out cross-loading, which the appendix
    also requires (p. 269), so the right answer can be argued against. Add "and no item
    cross-loads".
12. **Near-paraphrase of definitions and narrative.**
    - L1 `:252–260` (the disk-storage story, with runs "on enterprise disk storage systems" and
      "team had instrumented every level of the").
    - L4 `:1200–1202`: "variables that take only categorical values, such as gender" and "take
      scale values, such as Likert answers".
    - L6 `part_b.py:112`: "a mutual relationship or connection between". Rephrase it, e.g.
      "Correlation says how two constructs vary together".

## NOTE

1. **L3 `:922–923`.** "The lesson Inferential Predictive Analysis returns to" points to a lesson
   in the previous course. "discusses" reads better.
2. **L5 `:1576`.** "fails three others" counts the two loading failures as one test, while the
   tile counts four. This is consistent, but "fails three kinds of test" is clearer.
3. **Faithful to the book.** L4 reports the book's "second-lowest" marker correlation
   (pp. 267–268). L5's aside that the appendix writes "CR" where it means alpha is right
   (p. 269), and so is L6's caution on Tukey and normality. Reverse coding is indeed absent from
   the book. No lab uses the book's data, and Chapter 16 is credited to the Bells.

**Verdict:** the arithmetic is correct throughout, and the book's positions are stated faithfully
with three exceptions. Fix the duration mismatch in L1, the overclaim in L2 and the paraphrased
passage in L2; the rest is polish.
