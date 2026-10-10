# Pedagogy assessment — Accumulation and the Integral (differential equations, course 2)

Formed from the eight lesson dicts in `content/differential_equations/c2_accumulation/`
(`part_a.py`, lessons 1–4; `part_b.py`, lessons 5–8; `__init__.py`, the course
dict), the spoken forms in `content/spoken/differential_equations_c2_accumulation.py`,
and the two `calckit` modes they render through (`scripts/mathpath/labs/calckit.py`
`riemann` and `antiderivative`), on branch `feat/differential-equations` before
the Subject was wired into the site. The design authority is
`docs/differential-equations/PLAN.md` §C (course 2), §D.2 and §F; the course
was written in two parts, so the seam at lesson 5 is assessed as well.

Every lesson was read in full before anything was changed. Every pinned figure
and every figure quoted in prose was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through `scripts/preview_subject.py`),
not out of the kit source, and recomputed by hand with exact fractions.
Lessons, in course order: `total-change-from-a-rate`, `left-and-right-sums`,
`refining-the-partition`, `trapezoid-and-midpoint-rules`,
`the-antiderivative-and-the-fundamental-theorem`, `the-constant-of-integration`,
`the-integral-sign-and-its-rules`, `the-integral-of-one-over-t`. The course
assumes Rates of Change and the Derivative and the Algebra Subject, and is
judged against those alone.

## Verdict

The course teaches its subject. A reader who finishes it can cut an interval
into equal pieces and form a left sum as an exact fraction while saying which
way it errs; compute left and right sums, predict their gap from the end values
alone and state the bracket a monotone rate allows; double the pieces and
measure the error ratio exactly, keeping the claim that the sums approach the
total apart from the three rows that support it; form trapezoid and midpoint
sums and show the error quartering on a quadratic; reverse the power rule,
check the result by differentiating, and evaluate `F(b) − F(a)`; fix the
constant from one value and say why one is exactly enough; read the integral
sign aloud and check linearity and additivity by computing both sides; and
bracket `∫₁² dt/t` between exact fractions while quoting the total rounded and
labelled. Those are the acts the eight `standard` fields measure and the labs
compute, and none is "understand X".

Every figure the lessons quote agrees with the lab and with hand computation:
roughly sixty fractions, from `7/32` to `52279/72072`, and every rounded figure
is marked `≈` or "about" and never printed bare. The defects found were local.
Two quiz explanations were wrong, one of them arithmetically; one sentence
claimed a ratio of exactly `4` for every cubic, which a cubic with equal end
slopes refutes; one paragraph listed contributions as if they were rates; one
"about a hundredth of the total" was a thirty-second of it; and both parts
said "the total change of the rate `f`" where the course's own quiz marks that
reading wrong. A few math runs read badly aloud, three key lines carried a
second column, and the course home had no outcome for the eighth lesson. All
are repaired below. Nothing needs splitting, merging or reordering.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names what is produced: the
  width, the left ends, the sum and the direction of its error
  (`total-change-from-a-rate`); both sums, the predicted gap and the bracket
  stated without more than it gives (`left-and-right-sums`); the error and the
  exact ratio at `n` and `2n`, with the claim stated apart from the table
  (`refining-the-partition`); `Tₙ` from `Lₙ` and `Rₙ`, the midpoints and `Mₙ`,
  both errors with their signs (`trapezoid-and-midpoint-rules`); `F`, its check,
  `F(b) − F(a)` (`the-antiderivative-and-the-fundamental-theorem`); the family,
  the equation `F(t₀) + C = y₀`, both checks (`the-constant-of-integration`);
  the symbol read aloud and both sides of each rule computed
  (`the-integral-sign-and-its-rules`); the bracket and the rounded, labelled
  quotation (`the-integral-of-one-over-t`).
- **The exactness rule is kept, and the prose says which tier every number is
  in.** Sums, gaps, errors and ratios are fractions and are called exact;
  `1/3` is "the lab's exact total" and never `0.333`; the one irrational total
  on the course is introduced with the tile's own text, `≈ 0.693147 (ln 2,
  rounded)`, and the sentence explains why the `≈` and the word are there
  (`the-integral-of-one-over-t`). Decimals in prose are prefixed "about" or
  `≈` (`1.91304`, `1.86667`, `3.98122`), and `mistakes[1]` of the last lesson
  refutes `693147/1000000` as a value of `ln 2`.
- **A claim is stated as a claim, and the proofs stop where the algebra does.**
  `thm` blocks carry the three things the course demonstrates and does not
  prove: that the left sums approach the total (`refining-the-partition`), the
  fundamental theorem (`the-antiderivative-and-the-fundamental-theorem`), and
  `∫₁ˣ dt/t = ln x` (`the-integral-of-one-over-t`); each is followed by a
  paragraph saying what the lab showed, for which rates and which `n`, and
  what a first analysis course does instead. Proofs appear only where the
  reader has the algebra: the telescoping gap `h·(f(b) − f(a))`
  (`left-and-right-sums`), the per-piece excesses `h³/6` and `−h³/12` summed
  to `h²/6` and `−h²/12` (`trapezoid-and-midpoint-rules`), two polynomial
  antiderivatives differing by a constant (`the-constant-of-integration`),
  linearity and additivity from `F` (`the-integral-sign-and-its-rules`), and
  the scaling identity for sums of `1/t` (`the-integral-of-one-over-t`). Each
  of those was checked line by line and holds.
- **Every misconception is named as a model someone holds and refuted with a
  fraction.** The §C misconception is `mistakes[0]` in all eight lessons: end
  rate times time gives `8` against the total `4`; the right sum is the
  overestimate only until `4 − t` prints `13/2` above `11/2`; "doubling halves
  the error" would predict `11/192` where the lab prints `23/384`; the
  trapezoid rule "uses both ends" and is still high by `1/96` then `1/384`;
  `(t³)′ = 3t²` exposes the forgotten division; `C` is `4` and then `−8`,
  neither zero; `1/3` is not `1/4`; `t⁰/0` names no function.
- **Worked example, faded rehearsal, quiz, in every lesson.** Each `worked`
  ends with a rehearsal on another preset whose first move is supplied and
  whose target is stated, so the reader can check without the lab: `1, 2, 5`
  then "say why the answer is below `12`"; the rate drops by `2`, predict the
  gap; the sixteen left rates over `256` land on `155/512` and `92/47`; the
  midpoints `1/16, 3/16, …` give `85/256` and `−1/768`; the three terms
  become `t³`, `−2t²`, `t`; `t³ + C = 0` at `t = 2`; the coefficients `6` and
  `−2`; the left ends `1, 3/2, 2, 5/2` give `77/60` and `19/20`.
- **The lab's limit is stated in the lesson that leans on it.** The Rule
  control is redraw-only, so the `mid` preset of `trapezoid-and-midpoint-rules`
  pins what the page prints under the shipped trapezoid rule, and the prose
  says in so many words that `21/64` and `−1/192` come from switching the
  control; the pole refusal is named in the steps of `the-integral-of-one-over-t`;
  the sign convention of the error tile (sum minus total, so a low left sum has
  a negative error) is stated in `refining-the-partition` before the first
  negative fraction appears.
- **Figures agree with the lab.** Read off the observed tiles and recomputed:
  `3`, `4`; `8`, `12`; `12`, `12` (`total-change-from-a-rate`); `7/32`,
  `15/32`, gap `1/4`; `13/2`, `11/2`, gap `−1`, total `6`
  (`left-and-right-sums`); `−11/96`, `44/23`, `92/47`; `9/4`, `−7/4`, `28/15`;
  error `−1`, ratio `2` (`refining-the-partition`); `11/32`, `1/96`, `43/128`,
  `1/384`, ratio `4`; `21/64`, `−1/192`; `85/256`, `−1/768`; `113/512`,
  `53/2560`, `213/40960`, `848/213`; the cubic's `1/64`, `1/256`, `1/1024`
  (`trapezoid-and-midpoint-rules`); `t³/3 + C`, `t² + C`, `t³ − 2t² + t + C`
  with `1/3`, `4`, `12`, and the table's `51/128`, `187/512`, `651/2048`,
  `715/2048` (`the-antiderivative-and-the-fundamental-theorem`); `C = 4`,
  `−8`, `1/2` (`the-constant-of-integration`); `equal: 12 = 8 + 4`,
  `equal: 1 = 2 − 1`, `equal: 12 = 2 + 10` (`the-integral-sign-and-its-rules`);
  `319/420`, `533/840`, `1171/1680`, `52279/72072`, `≈ 0.709016`, `223/140`,
  `341/280`, `77/60`, `19/20`, and the three labelled logarithms
  (`the-integral-of-one-over-t`).
- **Prerequisites are met, and the cross-references are real.** The sum and
  constant rules cited from “The Derivative as a Function” are stated there
  (`(p + q)′ = p′ + q′`, `(c·p)′ = c·p′`) beside a proved power rule; “The
  Product Rule” is a lesson of the first course; “Common and Natural
  Logarithms” is a lesson of Algebra's Exponential and Logarithmic Functions;
  `t⁻¹` and `(t + h)³` are Algebra. Nothing is used before it is taught, with
  one honest forward reference: the per-piece exact total in the proof of
  `trapezoid-and-midpoint-rules` is deferred to the next lesson by name.
- **The seam at lesson 5 is clean.** Part A deferred the "exact total" tile
  twice by title (`total-change-from-a-rate`, `trapezoid-and-midpoint-rules`);
  part B opens by paying that debt ("That total came from a different method,
  and this lesson is the method") and quotes part A's own column `7/32, 35/128,
  155/512` three times. Spelling is British in both parts (litres), every
  cross-reference in both is by title, and the worked examples share the same
  two rates (`2t` on `[0, 2]`, `t²` on `[0, 1]`) across the seam.

## What it taught badly, or said wrongly

### Facts a reader would trust that were wrong

- **`refining-the-partition`, quiz 4 `why`:** "`15/7` is the ratio of the
  sums' numerators" — the sums are `9/4` and `49/16`, whose numerators give
  `49/9`. `15/7` is the two error numerators (`7/4`, `15/16`) upside down with
  their denominators dropped. Repaired to say so.
- **`the-integral-sign-and-its-rules`, quiz 2:** the distractor `2.5` was
  explained as the average of `2` and `5`, which is `7/2`. The distractor is
  now `7/2`, which also removes a bare decimal from a course that writes
  fractions.
- **`trapezoid-and-midpoint-rules`, body:** "Every polynomial rate of degree
  two or three gives a ratio of exactly `4` here." For any quadratic or cubic
  the trapezoid error is `(h²/12)·(f′(b) − f′(a))` exactly, so a cubic with
  equal end slopes — `t³ − (3/2)t²` on `[0, 1]` — has error `0` at every `n`
  and the ratio tile prints `—`. Repaired: the error is a fixed multiple of
  `h²`, so the ratio is exactly `4` whenever the error is not already zero;
  `t⁴` is the first power whose error is not such a multiple. The same lesson
  said twice that the rules are exact "for nothing curved" / "for no curve";
  both now say "only by accident", and step 4 now expects exactly `4` for a
  cubic as well as a quadratic, as the body claims.
- **`trapezoid-and-midpoint-rules`, worked `after`:** "about a hundredth of
  the total away" — `1/96` is about `0.0104` in size but a thirty-second of
  the total `1/3`. Repaired to the absolute figure, with the midpoint error
  as half of it.
- **`the-antiderivative-and-the-fundamental-theorem`, body:** "charges each
  piece at the rate at its left end: `0, 1/2, 1, 3/2`" — those are the
  contributions (rate times `1/2`); the rates are `0, 1, 2, 3`. The sentence
  now gives both.

### A conceptual slip that ran through both parts

A rate has no total change; the quantity whose rate it is does. Seven places
said "the total change of the rate `f`" or "of `f`", including the definition
of the integral sign and the statement of the fundamental theorem, while quiz 4
of `the-integral-sign-and-its-rules` marks "`g(5) − g(1)`" wrong precisely
because it is "a change of `g` itself, not of its antiderivative". The prose
was teaching the distractor. Repaired in `the-antiderivative-and-the-fundamental-theorem`
(`summary`, `concepts[2]`, first body paragraph, the theorem, step 5, worked
intro) and in `the-integral-sign-and-its-rules` (`one_line`, `summary`, first
body paragraph, the definition) to "the total change a rate produces" or "the
total change of a quantity whose rate is `f`". The `one_line` of the latter
also said the sign "does not turn a product into a product"; it now says what
is meant.

### Prose looser than the lab

- **`the-integral-sign-and-its-rules`, example:** "Type `t^2` into the lab's
  rate box and then `t` to see both numbers" — under the shipped `linear`
  preset the limits are `0` and `2`, so the tile would print `8/3` and then
  `2`, not the `1/3` and `1/2` the example is about. The instruction now uses
  the `scaled` preset, whose limits are `0` and `1` and whose definite tile
  already prints `1/3` for `t²`.
- **`trapezoid-and-midpoint-rules`, `one_line`:** stated the quartering as a
  general law; it is exact on a quadratic and approximate otherwise, which is
  the lesson's own point. Qualified.
- **`trapezoid-and-midpoint-rules`, proof:** "a later lesson shows where it
  comes from" now names “The Antiderivative and the Fundamental Theorem”.

### Reading aloud

Every `data-say` on the eight rendered pages was read. The general rules read
this course well — `∫ₐᵇ f(t) dt` is "the integral from A to b of f of t d t",
`y(1) = 5` is "y of 1 equals 5", `ln 2 ≈ 0.693147` is "the natural log of 2 is
approximately 0.693147" — with these exceptions, all repaired:

- `the-constant-of-integration`, math block: the marker `<- the one given`
  was read "gets the one given". It is now a parenthesis, which reads as a
  pause.
- `the-integral-sign-and-its-rules`: the key line `∫ₐᵐ + ∫ₘᵇ = ∫ₐᵇ` read "the
  integral from A to m of plus the integral from m to b of equals…"; the
  steps said "compute `∫ₐᵐ` and `∫ₘᵇ`"; two worked lines began `∫₀¹ = …`.
  Each now carries its integrand, and the key line is 30 characters.
- `the-integral-sign-and-its-rules`: the quoted readings “the integral from
  `a` to `b` of `f` of `t` `dt`” were a string of one-letter math runs ending
  in a lone `dt` that reads "dt". A reading is words, so the three quotations
  are now plain prose ("…of f of t, d t"). The two sentences that name the
  symbol itself keep `dt` as a run, and the course's spoken file gives it the
  reading "d t" that the rules already give it inside an integral; `dt` is a
  lone run nowhere else in the library.
- `the-integral-of-one-over-t`: "The `ln` is the natural logarithm…" read
  "the ln is"; now `ln x`.
- Three runs put a prime on a bracket — `(c·F + d·G)′ = c·f + d·g`, `(F·G)′`,
  `(t³/3)′ = 3t²/3 = t²` — and the rules read the prime onto the last letter,
  so a listener hears `F` times `G′`. Each has a spoken form keyed to the exact
  run ("the derivative of…"), the phrasing the second-order course already
  uses for `(cos)′`. Runs such as `(t³)′ = 3t²`, which the first course also
  carries and reads "t cubed prime", are left as that course reads them.

### Keys

Three key lines carried a second column separated by a run of spaces
(`Lₙ: rates at left ends     Rₙ: at right ends`; `Tₙ = (Lₙ + Rₙ)/2     Mₙ: rate
at midpoints`; the same on the course home), against PLAN §E's "no second
column". Each is now one clause, under 46 characters.

### Course home

Five outcomes covered seven lessons; the eighth, the integral of `1/t`, had
none although it is the course's only irrational total and the one place the
exactness rule is exercised. A sixth outcome, "Bracket an integral that is not
a fraction", was added.

### Quiz distractors

Every distractor in the course was argued for and none could be defended. The
ones that looked closest were checked by hand: in `left-and-right-sums` quiz 3,
"it equals `11/32`, the average" fails because the total is `1/3`; in
`trapezoid-and-midpoint-rules` quiz 1 the four errors in size are `11/96`,
`13/96`, `1/96`, `1/192`, so only the midpoint sum is nearest; in
`the-integral-of-one-over-t` quiz 4, `319/840`, `319/210` and `533/840` are
each a different number from `319/420`; in `refining-the-partition` quiz 1,
"it cannot be found without the total" fails because both errors are given;
in `the-constant-of-integration` quiz 4, `C = 9/2` fits neither value. The
distractor PLAN §E warns of, one true at a single `t` or step size, does not
occur.

## Where a learner gets stuck

- **`trapezoid-and-midpoint-rules` is the heaviest lesson.** It carries two
  rules, a proof with per-piece algebra, the `h²` law, and the cubic-against-
  quartic distinction. It is one idea — the error is a multiple of `h²` — but
  it is the most algebra on the path so far, and the `mid` preset is
  indistinguishable from `trap` until the Rule control is moved, because a
  redraw-only select ships one value. The prose and the preset label both say
  to move it. Not a defect in the content; recorded so nobody "fixes" the
  preset by pinning a tile it cannot pin.
- **`the-integral-of-one-over-t` adds a second idea** beyond PLAN §C's one: the
  scaling theorem and `ln 4 = 2·ln 2` as an exact equality of sums. It is
  short, exact, proved in two lines, and PLAN's own `ln4` preset invited the
  remark; a fourth preset (`scaled`) was added and is pinned. Kept.
- **"Why the claim is plausible"** in `the-antiderivative-and-the-fundamental-theorem`
  is an argument and says so. A reader who wants the proof stalls here by
  design; `not_covered` names a first analysis course as the place.
- **The error sign.** The lab prints the error as sum minus total, so a low
  left sum has a negative error, while the worked lines of
  `refining-the-partition` compute total minus sum and get positive fractions.
  The body states the convention before the first negative fraction, and the
  worked lines label their subtraction; a reader comparing tile and line has
  to notice the order. Acceptable.
- **`total-change-from-a-rate` shows six tiles**, three of which (error, gap,
  ratio) are defined in the next two lessons. The panel intro points the
  reader to the sum and the total only. Acceptable, as the first philosophy
  course accepted the same thing.

## Repairs made in this pass

In `content/differential_equations/c2_accumulation/__init__.py`: the third
`key` line; a sixth outcome. In `part_a.py`: `left-and-right-sums` `key[0]`;
`refining-the-partition` quiz 4 `why`; `trapezoid-and-midpoint-rules`
`one_line`, `key[0]`, `concepts[2]`, the proof's forward reference, the two
"exact for straight lines" paragraphs, step 4, and the worked `after`. In
`part_b.py`: `the-antiderivative-and-the-fundamental-theorem` `summary`,
`concepts[2]`, the first body paragraph, the left-sum paragraph, the theorem,
step 5 and the worked intro; `the-constant-of-integration` the math block and
quiz 4; `the-integral-sign-and-its-rules` `one_line`, `summary`, `key[3]`,
`concepts[0]`, the first and third body paragraphs, the definition, the
product example, steps 1 and 4, two worked lines and quiz 2;
`the-integral-of-one-over-t` the `ln` sentence. In
`content/spoken/differential_equations_c2_accumulation.py`: four spoken forms
(`dt` and the three primed brackets), each keyed to a run that exists only in
this course.

Slugs, lesson count, modules, lab keys and modes are as
`docs/differential-equations/COURSES.json` lists them; no preset instance or
`expect` was changed. `scripts/preview_subject.py differential_equations
--course accumulation-and-the-integral` reports OK: 9 pages, every lab
executes and survives the sweep, every pinned figure on the eight calckit pages
matches, no math run without a spoken form and none the rules guess at.
`tests/test_speech.py` passes (17 tests).

## Remaining issues

- None requires a structural change. No lesson should be split, merged or cut;
  the eight lessons carry one idea each and the heaviest
  (`trapezoid-and-midpoint-rules`) is heavy in algebra, not in ideas.
- The `mid` preset of `trapezoid-and-midpoint-rules` pins the trapezoid
  figures because the Rule select is redraw-only (PLAN §C, rule 6 of
  `scripts/mathpath/AGENTS.md`). If `labcheck.js` ever learns to pin a
  redraw-only control per preset, that preset should pin `21/64` and `−1/192`.
- `scripts/speechcheck.py` lists only wired Subjects, so until the
  orchestrator wires Differential Equations the speech audit for this course
  is the one `preview_subject.py` runs. It passes.
- Runs of the shape `(t³)′ = 3t²` read "t cubed prime" throughout the Subject,
  and the first course relies on that reading. If a chrome-level rule for a
  primed bracket lands in `speech.py`, the three bracket forms in this
  course's spoken file become redundant and should be removed then.
- The corrected cubic claim in `trapezoid-and-midpoint-rules` could carry its
  counterexample (`t³ − (3/2)t²` on `[0, 1]`, error `0` at every `n`). It was
  left out to keep the lesson's load where it is.
