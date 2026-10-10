# Pedagogy assessment — Laplace Transforms (differential equations, course 10)

Formed from the eight lesson dicts in `content/differential_equations/c10_laplace/`
(`part_a.py`, lessons 1–4; `part_b.py`, lessons 5–8; `__init__.py`, the course
dict), the spoken forms in `content/spoken/differential_equations_c10_laplace.py`,
and the kit they render through (`scripts/mathpath/labs/dekit_b.py`, mode
`laplace`, kinds `table`, `derivative`, `solve`, `partial`, `step`), on branch
`feat/differential-equations` before the Subject was wired into the site. The
design authority is `docs/differential-equations/PLAN.md` §0 (the exactness
rule), §C (course 10), §D.3 (`laplace`), §D.5 and §F; the course was written in
two parts, so the seam at lesson 5 is assessed as well.

Every lesson was read in full before anything was changed. Every pinned figure
and every figure quoted in prose was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py differential_equations --course laplace-transforms`),
every rounded figure was recomputed in double precision with the lab's own
Simpson rule (2000 panels) and against the closed form, and every exact one in
`fractions.Fraction`. Every math run on the nine rendered pages was read from
its `data-say`. Lessons, in course order: `the-laplace-transform`,
`linearity-and-the-table`, `the-transform-of-a-derivative`,
`solving-an-initial-value-problem` | `partial-fractions-exactly`,
`the-transfer-function-and-its-poles`, `the-unit-step-and-switched-forcing`,
`three-methods-one-equation`. The bar marks the seam. The course may assume
Systems and the Phase Plane and everything before it, plus the Algebra Subject;
it is judged against that.

## Verdict

The course teaches its subject. A reader who finishes it can write the defining
integral and compute `ℒ[1]` and `ℒ[e^(at)]` from truncated integrals, transform a
sum of table entries into one fraction in lowest terms, state both derivative
rules with their initial values and verify the first on a signal, solve a
constant-coefficient initial value problem with no constants fitted at the end,
decompose a fraction with linear, repeated and irreducible quadratic factors,
read stability from the poles of the transfer function, solve a switched forcing
in pieces, and solve one equation by two routes and say why they must agree.
Those are the acts the `standard` fields measure and the labs compute, and no
objective is "understand X". The `mistakes[0]` of every lesson is the §C
misconception, each refuted with a specific fraction, residual or value. All 48
pinned tiles on the eight pages matched the lab, every figure quoted in prose
agreed with the lab or with a recomputation, and the cross-references into
Second-Order Linear Equations (“Real Distinct Roots”, “The Characteristic
Equation”) point at lessons that carry the exact instance cited.

The defects found were local and are repaired below. The largest was not in the
mathematics but in the reading aloud: every bare number over `s` on the course
(`1/s`, `6/s³`, `4/s`, …) was read as the unit "per second", `e^(at)` and
`e^(−st)` were read with "at" and "st" as English words, `∫₀^∞` was read "the
integral over 0 of to the power infinity", `ℒ[f](s)` was read "f s", the
derivative rule's proof lost its grouping, and five plain titles containing
`ℒ[…]` were handed to the voice unread. In the content itself: a prerequisite
the course home borrows from Algebra that Algebra explicitly declines to teach,
one figure rounded outside the exactness rule, one theorem whose "if and only
if" is false in an edge case, two quiz distractors that are true, two
circular or misleading sentences about what the lab checks, a lone `ℒ` read
as "the Laplace transform of" with nothing after it, and the word "pole" used
and pinned a lesson before it was defined. Nothing needs splitting, merging or
reordering within the URL space the course has; one split is recorded under
remaining issues.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names what is produced: the
  defining integral and the two first entries (`the-laplace-transform`); any sum
  of the five families as one fraction (`linearity-and-the-table`); both rules
  with their initial values, verified on a signal
  (`the-transform-of-a-derivative`); an initial value problem solved with no
  constants fitted at the end (`solving-an-initial-value-problem`); a fraction
  with all three kinds of factor decomposed and inverted
  (`partial-fractions-exactly`); the transfer function, its poles and the
  verdict from their real parts (`the-transfer-function-and-its-poles`); a
  switched equation written in pieces (`the-unit-step-and-switched-forcing`);
  one problem by two routes, compared, with the better tool named
  (`three-methods-one-equation`).
- **The one hard idea of the course is named first and returned to.** "The
  transform is a whole function, not an answer" is `concepts[0]` of
  `the-laplace-transform`, its `mistakes[0]`, a quiz item that asks for the
  value at one `s` and then refuses the reading "it is not a number" as the
  answer to that question, and the sentence that closes the body: "The
  transform of one signal is never a number." Every later lesson's algebra on
  `Y(s)` rests on it and says so.
- **Claims are stated as claims, and the lab's evidence is kept apart from the
  lab's exactness.** `ℒ[1]` and `ℒ[e^(at)]` are proved from the antiderivative
  of an exponential; `ℒ[t] = 1/s²` "is a claim here and not a computation",
  because the antiderivative of `t·e^(−st)` needs a rule the Subject does not
  develop; the rest of the table "is stated here as claims". The truncated
  integrals `≈ 0.632121, 0.864665, 0.993262` (and `≈ 0.264241, 0.593994,
  0.959572` for the ramp) are recomputed and right, are introduced with
  "rounded" and `≈`, and are called "evidence for the claim" that "close in on
  it without ever proving it". The product rule and the fundamental theorem
  carry the proof of `ℒ[y′] = s·Y − y(0)`, with the condition
  `e^(−sT)·y(T) → 0` stated and called "not decoration".
- **The exactness rule is kept and the tiers are named in the sentence that
  reports the number.** "The transform it prints in the first tile is an exact
  rational function in lowest terms. The integrals in the status line are
  floating-point sums, rounded to six figures and marked with `≈`"
  (`the-laplace-transform`). `e^(10)` is "`≈ 22026.5`, rounded", `e²` is
  "`≈ 7.38906`, rounded", `1 − e^(−2)` is "`≈ 0.864665`, rounded", `1 − e²` is
  "`≈ −6.38906`, rounded" (`the-transfer-function-and-its-poles`,
  `the-unit-step-and-switched-forcing`); each was recomputed to six figures.
- **The misconceptions are refuted with the specific number.** `ℒ[1] = 1`
  "has evaluated at one point and thrown the rest away"; `1/(s − 2)` at `s = 1`
  is `−1`, "an impossible area for a positive function"
  (`the-laplace-transform`). `ℒ[1]·ℒ[1] = 1/s²` against `ℒ[1·1] = 1/s`, and
  `ℒ[t]·ℒ[e^(3t)]` has "a pole at `0` that the real transform does not"
  (`linearity-and-the-table`). The forgotten `y(0)` leaves `s/(s − 2)`, "`1`
  too large", and is invisible on `sin(t)` and `t²`, which is why it survives
  (`the-transform-of-a-derivative`). Starting values left out give `Y = 0`
  and `y = 0` with `y(0) = 0`, "not `1`"; dropping `b·y(0)` gives
  `−e^(−t) + 2e^(−2t)` with `y′(0) = −3`, not `0`
  (`solving-an-initial-value-problem`). The dropped middle term forces `A = 0`
  and `A = 1` at once (`partial-fractions-exactly`). `(1/3)·e^(2t)` at `t = 5`
  is `≈ 7342.16` and has no ceiling (`the-transfer-function-and-its-poles`).
  `u(t − 2)·(1 − e^(−t))` jumps to `≈ 0.864665` at the switch; `1 − e^(−(t − 2))`
  without the step starts at `≈ −6.38906` (`the-unit-step-and-switched-forcing`).
  `2 − 2e^(−t) + 2e^(−2t)` "has `y(0) = 2` and not `0`, so it is wrong on its
  face" (`three-methods-one-equation`).
- **Worked example, then faded guidance, then independent practice.** Every
  worked example is the first preset solved by hand and then "read against the
  lab"; every `panel_intro` then asks the reader to predict before pressing
  ("write the transform term by term and combine it yourself", "write the form
  the denominator demands and count the unknowns", "predict the first time the
  solution is not zero", "solve it by the other route on paper"); the quizzes
  ask for the same act on a fresh instance. The progression across lessons 4–5
  is right: one trick (multiply by a factor, substitute the root) does lesson
  4's three cases, and lesson 5 opens by saying "That trick covers one case"
  before the repeated factor refuses to yield to it.
- **The lab's limit is stated in the lesson that leans on it, and never as a
  verdict on the mathematics.** The irrational frequency `s² + 2`, the
  irreducible cubic, the improper fraction, the shift `c ≤ 0` and `u(t − π)` are
  each named where they bite, and each time with "the mathematics is still
  fine; the lab is limited" or its equivalent. The refusals match `LP_factor`,
  `LP_proper` and `LP_forcing` in the kit.
- **The lab's own check is explained rather than trusted.** "The lab does not
  trust any of this arithmetic. After it finds the coefficients and writes the
  inverse, it transforms the inverse back and compares the result with the
  original fraction exactly" (`partial-fractions-exactly`) is what `LP_invert`
  does; "the residual of that solution in the original equation" is what
  `LP_solve` prints as `residual 0`, and the lessons add the two starting
  values to the check by hand.
- **Figures agree with the lab.** Every pinned tile on the eight pages matched
  the observed tile, and every tile the prose quotes was found in the observed
  output: `1/s`, `1/(s − 2)`, `1/s²`; `(−2s³ + 6s + 6)/(s³(s + 1))`,
  `6/s³ − 2/(s + 1)`, `s/(s² + 4)`, `±2i`, `1/(s − 3)²`; `2/(s − 2)`,
  `s/(s² + 1)`, `2/s²`, `equal`; `(s + 3)/((s + 1)(s + 2))`,
  `2/(s + 1) − 1/(s + 2)`, `2·e^(−t) − e^(−2t)`, `3/s − 3/(s + 2)`,
  `2/((s + 1)² + 4)`, `e^(−t)·sin(2t)`; `1/s − 1/(s + 1) − 1/(s + 1)²`,
  `(1/5)/s − (s/5 + 2/5)/((s + 1)² + 4)`,
  `1/5 − (1/5)·e^(−t)·cos(2t) − (1/10)·e^(−t)·sin(2t)`; `−2, −1`, `−1 ± 2i`,
  `−1, 2`, `1/2 − e^(−t) + (1/2)·e^(−2t)`,
  `1 − e^(−t)·cos(2t) − (1/2)·e^(−t)·sin(2t)`; `e^(−2s)/(s(s + 1))`,
  `0 for t < 2; 1 − e^(−(t − 2)) for t ≥ 2`, the three-piece pulse,
  `1/4 − (1/4)·cos(2(t − 1))`; `2/s − 4/(s + 1) + 2/(s + 2)`,
  `cos(t) − cos(2t)`, `(1/3)·e^t − (1/3)·e^(−2t)`, `residual 0`. The claim that
  the status line shows the integrals "at `s = 3`" for `e^(2t)` was checked
  against the kit's choice of `s₀` (one above the largest pole), and the claim
  that those three numbers coincide with the constant's at `s = 1` holds to six
  figures under the lab's Simpson rule.
- **The seam at lesson 5 is nearly invisible.** `solving-an-initial-value-problem`
  closes with "The next lesson takes it apart on its own, with repeated and
  irreducible factors"; `partial-fractions-exactly` opens with "The previous
  lesson ended with fractions such as `(s + 3)/((s + 1)(s + 2))` and handled
  them with one trick." Both parts cite lessons by title and courses by name,
  both spell British (`behaviour`, `favours`; part A has no occasion to choose),
  and both use the same tile vocabulary and the same `A`, `B`, `C` for
  coefficients. The one visible difference is that part A writes `1/(s(s + 1))`
  without a product dot in worked lines where part B writes `s·(s + 1)`; that
  is now uniform (below), for the voice's sake as much as the eye's.

## What it taught badly, or said wrongly

### Facts a reader would trust that were wrong

- **`__init__.py`, `assumes_long`:** the course home said it assumes "Algebra's
  Rational and Radical Expressions for adding, reducing and decomposing
  fractions". That Algebra course's own `not_covered` says "Partial fractions,
  which are a technique for integration and belong to calculus." Nothing in
  the library teaches partial fractions before lessons 4 and 5 of this course,
  which build them from the substitution trick up. Repaired: the prerequisite
  is adding and reducing fractions; partial fractions "are not assumed, since
  that course leaves them out, and are built here from scratch".
- **`the-transfer-function-and-its-poles`, `thm` "The stability criterion":**
  "Every term in the response that comes from a pole of `H` tends to zero as
  `t` grows if and only if every pole of `H` has negative real part." The
  "only if" fails when a zero of `ℒ[q]` cancels a pole of `H`: for
  `y″ − y′ − 2y = q` with `ℒ[q] = (s − 2)/((s + 3)(s + 4))` the pole `2` never
  reaches the response, every term that does tends to zero, and the equation
  still has a pole on the right. Repaired by quantifying over the inputs:
  "whatever the forcing and the starting values", which makes both directions
  true, since starting values can excite any pole.
- **`partial-fractions-exactly`, quiz 1, distractor 3:**
  `A/s + (B·s + C)/(s + 1)²` was offered as a wrong form, and the `why` said a
  two-part numerator "belongs to an irreducible quadratic and not to a linear
  factor". But `(B·s + C)/(s + 1)² = B/(s + 1) + (C − B)/(s + 1)²`, so that form
  spans exactly the right space and solves cleanly (`A = 1`, `B = −1`,
  `C = −2`). A reader who chose it was right. Replaced with
  `A/s + B/(s + 1) + C/(s + 1)³`, which runs past the multiplicity.
- **`partial-fractions-exactly`, quiz 4, distractor 2:** "`B = A·C`" gives
  `1·(−1) = −1`, which is the correct `B` on this instance; the `why` even
  conceded the "coincidence of sign". A distractor that yields the right number
  is not a distractor. Replaced with the misconception that the coefficients
  add to the numerator (`A + B + C = 1`, so `B = 1`), refuted at `s = 1` where
  the identity reads `1 = 4A + 2B + C`.

### Prose looser than the lab or the mathematics

- **`linearity-and-the-table`, body:** "The rest of the table is stated here as
  claims, and the lab checks each against the transform of the signal: it
  computes every transform by exactly these rules." A lab that computes by the
  rules cannot check the rules; the sentence was circular. What the lab does
  offer is its status line, where the truncated integrals of the weighted
  signal close in on the fraction's value at one `s`. Repaired to say so, and
  to call that evidence rather than confirmation.
- **`linearity-and-the-table`, `concepts[1]`:** "A signal outside these families
  is outside this course" is contradicted by lesson 7's unit step. Now "apart
  from the switch that the last module adds".
- **`the-laplace-transform`:** the lab's second tile is labelled "Poles", it is
  pinned on all three presets (`0`, `2`, `0 (repeated)`), and quiz 1's `why`
  says "both have their pole at `0`" — but the word is defined nowhere before
  `linearity-and-the-table` uses it in passing and
  `the-transfer-function-and-its-poles` defines it. One sentence added where
  the three denominators are compared: the tile lists these values "under the
  name they carry for the rest of the course: the poles of the fraction, the
  values of `s` at which its denominator is zero".
- **`solving-an-initial-value-problem`, body:** "Two limits of the lab" was
  followed by one limit (the irrational frequency). The kit refuses two
  different things: a linear factor with an irrational root (`s² − 2`, roots
  `±√2`) and an irreducible quadratic with an irrational frequency (`s² + 2`,
  inverse with `cos(√2·t)`). Both are now named, each with its refusal.
- **`the-transfer-function-and-its-poles`, body:** the prose writes the unstable
  solution as `−1 + (1/3)·e^(2t) + (2/3)·e^(−t)` while the tile prints
  `(1/3)·e^(2t) − 1 + (2/3)·e^(−t)`. One clause added: the lab prints the same
  three terms with the growing one first.
- **`the-transfer-function-and-its-poles`, quiz 4:** "Under the criterion as
  this lesson states it, with a strict inequality, does the transient die?"
  asked the criterion to decide a fact about the solutions, which it does not;
  the solutions of `y″ + 4y = 0` neither shrink nor grow whatever the criterion
  says. Rewritten as two questions in one ("What does the criterion say, and
  what do the solutions do?") with four answers that pair a verdict with a
  behaviour, only one pair right.
- **`the-unit-step-and-switched-forcing`, proof of the shift rule:** the
  substitution `t = c + τ` is a change of variable inside an integral, which
  Accumulation and the Integral does not develop (§G leaves substitution out).
  It is honest here because it is only a translation of the time axis, and the
  proof now says what it uses: "sliding a graph along the axis does not change
  the area under it".
- **`three-methods-one-equation`, key line:** "the answers agree: one solution
  exists" says existence where the lesson's theorem is uniqueness. Now "the
  solution is unique". The proof of “The routes agree” ended "because the 2×2
  system for the constants has a nonzero determinant" without saying that this
  is the Wronskian the reader has already met; it now cites “Superposition and
  the Wronskian” in Second-Order Linear Equations by title.
- **`solving-an-initial-value-problem`, `concepts[0]`:** "Apply `ℒ` to every
  term" put a lone `ℒ` in a run, which the voice reads as "the Laplace transform
  of" with nothing after it. Now "Transform every term of the equation".

### The exactness rule

- **`the-transfer-function-and-its-poles`, `mistakes[0]`:** "every further unit
  of time multiplies it by about `7.4`" rounded `e²` to two figures with no
  `≈` and no stated rule, on a page whose body gives the same number as
  "`≈ 7.38906`, rounded" two paragraphs earlier, and under a course footer
  that promises every rounded figure "is printed with `≈`". Now "multiplies it
  by `e²`, which is `≈ 7.38906`, rounded". No other figure on the course was
  found outside the rule.

### Speech

Every math run on the nine rendered pages (1 084 spoken spans) was read from
`data-say`. The §D.5 changes work throughout: `ℒ[y′] = s·Y − y(0)` reads "the
Laplace transform of y prime equals s times Y minus y of 0", `u(t − c)` reads
"u of the quantity t minus c", `y(0) = 1`, `d(0) = 0`, `F(s)`, `H(s)`, `Y(s)`
all read as calls, `∫₀ᵀ` reads "the integral from 0 to T of", `±2i`,
`−1 ± 2i`, `α ± βi`, `n!`, `n·(n − 1)·⋯·1`, `≈ 0.632121` and `e^(−2t)` read as
§F lists them. `speechcheck` reports no ambiguous run and no unspoken symbol.
Six shapes read wrongly all the same, and none is flagged by the checker
because each is all words:

- **A number over `s` read as the unit "per second".** `1/s` read "1 per
  second", `1/s²` "1 per second squared", `6/s³` "6 per second cubed", and so
  on through 34 runs, because the engine's unit rule fires on a numeric
  numerator over the word `s` (System Design writes `req/s`). The notation is
  the Subject's and cannot change. Spoken forms were written for every such
  run the page speaks, keyed by the complete run. The bare `1/s` needed a
  check before it was keyed: the only other `1/s` in the library is System
  Design's `c10_measuring`, where `s` is a sampling fraction and "1 over s" is
  the correct reading too, so the form corrects that page rather than
  misreading it. Quiz-only runs (`4/s + 12/s³`, `3/s − 3/(s + 2)`, …) were left
  alone, since `readout.py` never reads the quiz.
- **`e^(at)` read "e to the power at" and `e^(−st)` "the quantity negative
  st".** The engine splits `kt` into letters but keeps `at` and `st` as words,
  because both are in its common-word list. Spoken forms for the 17 runs that
  carry them, including the defining integral, the proof of linearity and the
  product-rule line of the derivative proof.
- **`∫₀^∞` read "the integral over 0 of to the power infinity".** The §D.5 rule
  reads a subscript followed by a superscript token, and there is no
  superscript infinity to write. The three runs with `∫₀^∞` have spoken forms.
  The two runs written `∫₀^T` were rewritten to `∫₀ᵀ`, which is how PLAN §C
  writes the truncated integral and which the rule reads correctly.
- **`ℒ[f](s)` read "the Laplace transform of f s".** Spoken form: "the Laplace
  transform of f, as a function of s"; likewise `ℒ[e^(2t)](s)`.
- **`(e^(−st)·y)′` read without its grouping**, as "e to the power … times y
  prime", which is the right-hand side's last term and not the derivative of
  the product. Spoken form with "the rate of", the phrasing the Second-Order
  spoken forms use for a prime on a bracket.
- **Plain titles handed to the voice unread.** `ℒ` is not in the islands
  pattern that wraps math written into plain fields, so five titles (`Taking
  ℒ[f] to be a number`, `ℒ[y′] for y = e^(2t), both ways`, `Writing ℒ[y′] = s·Y
  and …`, `Giving ℒ[y″] only one correction`, and the quiz stem `check ℒ[y′] =
  s·Y`) reached the voice as a raw symbol followed by a fragment. Retitled in
  words; the quiz stem now carries its run in backticks. Three more plain
  titles were split at their spaces into fragments ("plus 1 squared"):
  `1/(s(s + 1)²) and its inverse`, `Inverting (s + 2)/((s + 1)² + 4) as a pure
  cosine`, `Inverting 2/((s + 1)² + 4) without the exponential`; retitled in
  words. Two `standard` bodies that wrote a formula with spaces into plain
  prose (`e^(−(s − a)t)`, `s·Y − y(0)`) were reworded.
- **`s(s + 1)` read "s of the quantity s plus 1"** in four worked lines and two
  mistake bodies, as a call. The product dot was added (`s·(s + 1)`,
  `A·(s + 1)²`), which is the §F convention; the one such string that must stay
  as the lab prints it, `(−2s³ + 6s + 6)/(s³(s + 1))`, has a spoken form.
- **`1 ≤ t < 3`** read "1 is at most t is less than 3"; spoken form "t is at
  least 1 and less than 3".

Not changed: lowercase `a` reads as the letter name "A" everywhere, which is the
global engine's rule for the article, and `e^(at)` therefore reads "e to the
power A t" in its spoken form, as the sibling courses' forms do; the typed-grammar
hints in `panel_intro` (`1/(s^2 (s + 2))`, `e^(-3t)`) are split by the
islands pattern as they are on every Subject. Both are chrome, not content.

### Cross-references

- `“Real Distinct Roots” in Second-Order Linear Equations` is cited for the
  instance `y″ + 3y′ + 2y = 0`, `y(0) = 1`, `y′(0) = 0`; that lesson's `decay`
  preset carries exactly that instance. `“The Characteristic Equation”` exists
  under that title. `“Superposition and the Wronskian”` is now cited where the
  uniqueness proof leans on it. No reference is by number; "the previous
  lesson", "the next lesson" and "the last module" are relative prose and
  stay. Course names (Second-Order Linear Equations, Systems and the Phase
  Plane, Accumulation and the Integral, Algebra's Rational and Radical
  Expressions) are plain, as §C requires.

## Where a learner gets stuck

- **`the-laplace-transform` asks for a function as an answer, from a reader
  whose every answer so far was a function of `t` fitted to a start.** The
  lesson spends its first concept, its first mistake, a quiz item and the
  closing paragraph on "the transform is a whole function". That is the right
  amount. The lab's second tile (poles) and fourth (partial fractions) show
  before the words are taught; the pole is now named in the body, and the
  partial-fractions tile simply repeats the transform on these presets.
- **`solving-an-initial-value-problem` carries the whole method and three
  cases**, including a complex-roots case that needs completing the square and
  the shifted sine entry before `partial-fractions-exactly` teaches the
  irreducible quadratic properly. The lesson gets away with it because the
  complex case's numerator is already the `2` the entry needs, so no
  two-part numerator appears; the next lesson picks up exactly there with
  `(s + 2)/((s + 1)² + 4)`. The order is the PLAN's and it holds.
- **The sign of `a` in `e^(at)` against `s − a`** (`e^(−t)` has `a = −1`, so
  `s + 1`) is the slip the course names in `the-laplace-transform`
  (`mistakes[2]`), `linearity-and-the-table` (`steps[1]`, `mistakes[2]`, quiz 4)
  and `solving-an-initial-value-problem` (the first-order example). Three
  lessons is the right amount of repetition for the slip that moves a pole
  across the axis, and each refutation is a different fraction.
- **The unit step's two operations** (replace `t` by `t − c`; multiply by the
  step) are separated into two mistakes with two different wrong values
  (`≈ 0.864665` at the switch; `≈ −6.38906` at the start), which is how a
  reader learns that both are needed. The pulse's three stretches are checked
  to meet at `t = 3` (both pieces `1 − e^(−2)`), which the lab's solution tile
  does not say in words.
- **`three-methods-one-equation` is titled for three methods and shows two on
  the headline equation**, with the third (the integrating factor) on a
  first-order equation, because the third does not exist for second order.
  The summary and the first paragraph say so plainly, and the course home now
  says so too. A reader who expects three columns for one equation is told
  within two sentences why there are two.

## Repairs made in this pass

In `content/differential_equations/c10_laplace/__init__.py`: `summary`,
`assumes_long`. In `part_a.py`: `the-laplace-transform` the two `∫₀^T` lines
(now `∫₀ᵀ`), the pole sentence, `standard[1]`, `mistakes[0]` title;
`linearity-and-the-table` `concepts[1]`, the paragraph after the table;
`the-transform-of-a-derivative` the worked title, quiz 3 stem, `mistakes[0]`
and `mistakes[2]` titles, `standard[1]`; `solving-an-initial-value-problem`
`concepts[0]`, the two-limits paragraph, `mistakes[2]` title. In `part_b.py`:
`partial-fractions-exactly` the worked title and two worked lines, quiz 1
distractor and `why`, quiz 4 distractor and `why`, `mistakes[0]` body,
`mistakes[2]` title; `the-transfer-function-and-its-poles` the theorem, the
unstable paragraph, quiz 4, `mistakes[0]`; `the-unit-step-and-switched-forcing`
the proof, two worked lines; `three-methods-one-equation` key line 3, the
proof, one worked line. In `content/spoken/differential_equations_c10_laplace.py`:
the two existing forms kept, 56 added, every key a complete live run, none a
tuple or a lone symbol, none clashing with another Subject's form. No preset,
`expect`, slug, module, lab key or mode changed.

Slugs, lesson count, modules, lab keys and modes are as
`docs/differential-equations/COURSES.json` lists them.
`scripts/preview_subject.py differential_equations --course laplace-transforms`
reports OK: 9 pages, every lab executes and survives the sweep, every pinned
figure on the eight pages matches, no math run without a spoken form, none
ambiguous; and a second pass over every `data-say` on the nine pages finds no
"per second", no "at"/"st" as words, no "to the power infinity", no "f s", no
"s of the quantity", and no plain field with an unread `ℒ`.

## Remaining issues

- **`solving-an-initial-value-problem` would be two lessons.** The method (four
  moves, the first-order case, the real-roots case) and the complex-roots case
  (complete the square, recognise the shifted sine, read the decay off the
  shift) are each one hard idea; PLAN §C puts both under one slug, and the
  complex case is then retaught a lesson later with the two-part numerator. The
  natural split is "Solving an Initial Value Problem" / "Complex Roots in the
  Transform", which the URL space does not have. Not done.
- **The speech engine's unit rule is wrong for every mathematics Subject.** A
  bare `1/s` meaning "per second" exists nowhere in the library (System
  Design's is a sampling fraction), yet the rule turns every numeric-over-`s`
  run into a rate. Fifty-odd spoken forms in this course exist only to undo
  it, and the next course that uses `s` as a variable will need the same. The
  fix belongs in `speech.py` (fire the unit rule only after a unit or a
  quantity with units, or only for `req/s`-shaped runs), which is the
  chrome-renderer tier's and not a course author's. Recorded, not changed.
- **`at` and `st` as exponent letters.** Likewise global: the engine keeps any
  two-letter common word whole, so `e^(at)` and `e^(−st)` need spoken forms
  wherever they appear, while `e^(kt)` does not. A rule that splits a
  common-word token when it sits inside `^(…)` or touches a `·` would retire
  nineteen of this course's forms. A `speech.py` change, not a course one.
- **The quiz is never read aloud** (`readout.py` skips `.quiz`), so sixteen
  quiz-only runs on this course still read "per second" if a reader has their
  own screen reader speak the quiz. The choice is the chrome's; recorded so
  nobody adds spoken forms for runs the reader will not hear.
- **The partial-fractions tile shows on the table presets** of the first two
  lessons, repeating the transform (`1/s`, `6/s³ − 2/(s + 1)`) under a heading
  the course has not yet taught. It does no harm, and the second lesson uses it
  ("its fourth tile keeps the term-by-term form"); a per-kind tile set is a kit
  change and was not made.
