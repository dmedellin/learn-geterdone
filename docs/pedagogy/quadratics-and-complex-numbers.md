# Pedagogy assessment — Quadratics and Complex Numbers (algebra, course 6)

**Second assessment. It supersedes `prior/quadratics-and-complex-numbers.md`
and it changes no source.** Nothing under `content/` or `site/` was touched:
the prose is settled and a contract snapshot is pinned to it, so every finding
below ends in a recommendation precise enough to execute later rather than in
an edit. The repairs the first pass describes are live on `main`, verified here,
and are not being reverted; where this pass disagrees with one of its claims,
the disagreement is recorded in *What this pass caught, and what it disputes*.

Formed from all fourteen lesson dicts in `content/algebra/c6_quadratics/`
(`part_a.py`, `part_b.py`, `__init__.py`) as they stand on
`review/course-ui-standardization` at `d0a238a`, and from every lab the lessons
attach: `quadratic_lab` in `scripts/mathpath/labs/algebra_quadratic.py` (ten
modes, nine of them used here), `complex_lab` in
`scripts/mathpath/labs/algebra_rational.py` (three modes), and the `quadratic`
mode of `inequality_lab` in `scripts/mathpath/labs/algebra_equations.py`. Every
body block, method step, worked example, faded rehearsal, quiz option, quiz
explanation, misconception, completion standard and lab configuration was read
before anything was written; every displayed number was recomputed; and every
lab claim was checked against the JavaScript that ships, including which
controls each mode renders and which rows it prints unconditionally.

Lessons, in course order:
`quadratic-equations-and-the-zero-product-property`, `solving-by-factoring`,
`the-square-root-property`, `completing-the-square`, `the-quadratic-formula`,
`the-discriminant`, `complex-numbers`, `operations-with-complex-numbers`,
`complex-roots-of-quadratics`, `graphs-of-quadratic-functions`,
`vertex-form-and-the-axis-of-symmetry`, `maximum-and-minimum-problems`,
`quadratic-inequalities`, `equations-reducible-to-quadratic-form`. 43 quiz items
and 42 named misconceptions — the largest course of the three.

The course declares "Factoring and radicals" and is judged backwards against
courses 1–5. It is also judged *as the tail of a three-course chain*, because
Polynomials and Factoring supplies the ac search and the multiplicity vocabulary
and Rational and Radical Expressions supplies the surds, and one of those two
relationships turns out to run in both directions at once.

## What the course teaches well

- **Four methods are taught as one method with the hypotheses removed a piece
  at a time, and the course says so.** `solving-by-factoring` `.note`: "the
  square root property handles anything with no `x` term, completing the square
  handles everything, and the formula is completing the square carried out once
  and kept." `the-square-root-property` `.concepts[1]` shows its own property is
  the zero product property one layer down (`x² = k` is
  `(x − √k)(x + √k) = 0`); `.note` says the whole of `completing-the-square`
  exists to reach the shape it can already solve. `completing-the-square`
  `.note` says the procedure pays twice — the formula from `ax² + bx + c = 0`,
  the vertex from `y = ax² + bx + c` — and `vertex-form-and-the-axis-of-symmetry`
  `.note` collects on it. `the-quadratic-formula` `.note` refuses to let the
  formula subsume the others. Read end to end, the first six lessons are one
  argument rather than six techniques, and the reader who finishes them can say
  why each method exists.
- **The proofs are real proofs and they are proved at the right length.** The
  zero product property is proved from the existence of reciprocals, and then —
  unusually, and correctly — the lesson shows the hypothesis failing, in
  arithmetic modulo 12, where `3 · 4 = 0` with neither factor zero. That single
  paragraph converts "the other side must be zero" from a rule into a fact about
  the number system. The quadratic formula is derived in six steps and the
  derivation handles `√(4a²) = 2|a|` explicitly rather than sliding past it.
  `the-discriminant` proves all three cases and then proves the perfect-square
  criterion in both directions. `graphs-of-quadratic-functions` proves
  `f(h + t) = f(h) + at²`, and `maximum-and-minimum-problems` then spends that
  identity three times — for the optimum, for the strictness away from `h`, and
  for the unboundedness in the other direction. `complex-numbers` proves
  equality of complex numbers by showing `i` would otherwise be a quotient of
  reals. `operations-with-complex-numbers` proves the conjugate product is real,
  non-negative, and zero only at the origin, and then uses all three parts.
- **Every closing standard names an act, and several name the act's failure
  mode.** "Finish when you refuse to split a product unless the other side is
  zero"; "when factoring is a first attempt you abandon quickly"; "when the `±`
  appears at the same moment the radical does"; "when an odd `b` does not slow
  you down"; "when you can derive the formula, not only quote it"; "when `D` is
  the first thing you compute on any quadratic"; "when `a + bi` is the only form
  you leave an answer in"; "when a negative discriminant makes you reach for `i`
  rather than stop"; "when you can sketch without a table of values"; "when the
  model, not the algebra, is what takes the time"; "when the answer is a set and
  you can say why each endpoint is in or out"; "when the substitution is written
  down explicitly, with its restriction." Not one of these is "understand X",
  and `maximum-and-minimum-problems`' is the sharpest completion standard on the
  path — it tells the reader that if the setup took no longer than the vertex
  did, something was assumed rather than read.
- **The number-system extension is motivated historically and then used
  carefully.** `complex-numbers` `.body` lists the three previous extensions
  (`x + 3 = 1`, `3x = 1`, `x² = 2`) with the equation each was forced by, points
  out that each new class was called unnatural, absurd, irrational and imaginary
  in turn, and says that "'Imaginary' is a seventeenth-century insult that
  hardened into a technical term." It then withholds the ordering — "No ordering
  of the complex numbers is compatible with their arithmetic, so the words
  'positive', 'greater than' and 'between' are not available for them" — which
  is a restriction most school treatments never mention and which
  `operations-with-complex-numbers` `.concepts[1]` repeats at the point it could
  bite ("`3 + 2i < 5` is not a false statement, it is not a statement at all").
  `complex-roots-of-quadratics` then proves the conjugate-pair theorem *with*
  its real-coefficient hypothesis and supplies the counterexample that shows the
  hypothesis is doing work (`x² − ix = 0` has roots `0` and `i`).
- **The arithmetic is right, including in the places most likely to be wrong.**
  I recomputed all fourteen faded rehearsals and every worked line.
  `12x² − 11x − 5 = 0` splits with `−15` and `4` into `(4x − 5)(3x + 1)`, giving
  `5/4` and `−1/3`; `3(x − 2)² = 14` gives `x = 2 ± √42/3`; `3x² + 6x − 1 = 0`
  gives `−1 ± 2√3/3`; `3x² + 2x − 7 = 0` gives `(−1 ± √22)/3`;
  `(5 − 2i)/(1 + i)` is `3/2 − (7/2)i` and the named wrong answer
  `7/2 − (7/2)i` really is what replacing `2i²` by `+2` produces;
  `3x² − 6x + 10 = 0` gives `1 ± (√21/3)i`, whose sum is `2 = −b/a` and product
  `10/3 = c/a`; `y = −2x² − 4x + 6` has intercepts `−3` and `1`, axis `x = −1`,
  vertex `(−1, 8)`, y-intercept `(0, 6)`; a rectangle of perimeter 54 optimises
  at `13.5 × 13.5` with area `729/4`; `2x² − x − 6 > 0` is
  `(−∞, −3/2) ∪ (2, ∞)`; `2x⁴ − 5x² + 2 = 0` gives `±√2` and `±√2/2`. The
  projectile's landing time `2 + √105/5 ≈ 4.05` s is right, and so is the
  substitution check of `−1/2 + (3/2)i` in `2x² + 2x + 5`, line by line.
- **Misconceptions are named at the point of error and the course does not
  soften them.** Splitting a product that is not zero; dividing both sides by a
  variable; reading solutions off the brackets without changing the sign;
  factoring before there is a zero; inverting a factor instead of solving it;
  reporting "does not factor" as "no solutions"; writing only the positive root;
  `√9 = ±3`; rooting term by term; adding the completing constant to one side;
  completing before dividing by `a`; losing the subtracted constant in an
  expression; reading `a`, `b`, `c` before standard form; writing `b²` as a
  negative; dividing only part of the numerator; dropping the sign in `−4ac`;
  reading `D = 0` as "no solutions"; saying "no solutions" when "no *real*
  solutions" is meant; `√(−9) = −3`; calling the imaginary part `bi`; treating
  the reals and complex numbers as rivals; leaving `i²` in an answer; using
  `√a·√b = √(ab)` on negatives; deciding a parabola's direction from `c`;
  sampling on one side of the axis; bringing the subtracted square out without
  multiplying by `a`; reading `h` with the wrong sign; reporting the location
  when the value was wanted; assuming the vertex is a maximum; dividing an
  inequality by `x`; writing a two-interval answer as a chain; assuming the sign
  alternates at every root; stopping at `u`; keeping a `u` no real `x` produces.
  `the-discriminant` `.mistakes[2]` is the one I would keep above all the
  others: "The sentence you write today should still be true three lessons from
  now."

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson — here, five lessons — before it is taught

1. **The shared `quadratic_lab` computes and prints all four methods on every
   redraw, in every mode, so lesson 1's page gives away lessons 2 through 6.**
   This is the central finding of the assessment and it is a property of the
   lab's structure rather than of any one string. `redraw()` in
   `algebra_quadratic.py` calls `byFactoring`, `bySquareRoot`, `byCompleting`
   and `byFormula` unconditionally, and then always appends the block "The four
   methods, computed separately" with a row for each. It also always writes the
   KPI strip, whose first cell is hard-coded `<span>Discriminant</span>`, and it
   always ends with a status banner that opens "The discriminant is `D`, …".
   On `quadratic-equations-and-the-zero-product-property` — lesson 1, whose
   entire content is one property and the two ways it is misapplied — the reader
   therefore sees: a KPI labelled *Discriminant* with a number in it; a row
   headed *completing the square* with a finished answer; a row headed *the
   formula* with a finished answer; and a status banner reading, on the shipped
   default preset, "The discriminant is 1, a perfect square. That is exactly the
   condition for this quadratic to factor over the rationals, which is why
   factoring works here and fails on the next preset." The discriminant is
   defined in lesson 6. Completing the square is lesson 4. The formula is
   lesson 5. The perfect-square criterion is `the-discriminant` `.body`'s second
   theorem. The course home's `how_to[2]` says "Use the discriminant before you
   solve, every time" — good advice, addressed to a reader who has met it, and
   the lab has been saying it since lesson 1.

2. **The gate that would have fixed this already exists, and was applied to
   exactly one quantity.** Line 120 of `algebra_quadratic.py`:
   `var SHOW_COMPLEX = ['graph', 'vertex', 'optimise', 'reducible'].indexOf(MODE) >= 0;`
   with a comment above it explaining the reasoning precisely — "Lessons 3-6
   classify a negative discriminant as 'no real solution' before lesson 7
   defines `i`. … presentation follows lesson order even though the exact-
   arithmetic core can already compute both cases." That is the right idea,
   correctly implemented, and it fences `i` and nothing else. The same mechanism
   applied to the discriminant KPI, the four-method block and the status
   banner's opening clause would resolve item 1 without touching the exact
   core. The first pass built the gate; what is missing is the rest of the list.

3. **`the-square-root-property`'s lab refuses the lesson's own shifted form, and
   the lesson calls that form the one everything else depends on.**
   `bySquareRoot(a, b, c)` opens `if (!Rzero(b)) return { ok: false, text:
   'only applies when there is no linear term; here b = ' + Rtext(b) }`. The
   lesson's `.body` has an `h3` called "The shifted form" which says the
   property "does not care what is being squared", derives `x = h ± √k` from
   `(x − h)² = k`, and ends: "That is the form every completed square arrives
   at, which is why the whole of 'Completing the Square' depends on this one."
   Worked examples B (`(x − 4)² = 20`) and C (`2(x + 3)² − 5 = 0`) are both
   shifted, and both expand to a quadratic with `b ≠ 0` — so a reader who enters
   B as `a = 1, b = −8, c = −4` is told the square root property does not apply
   to it. The lesson's faded rehearsal (`3(x − 2)² = 14`) has the same problem.
   The property applies; the lab's implementation of it is the special case
   `h = 0`.

4. **`quadratic-inequalities` `.note` attributes sign analysis to a course that
   does not contain it, and Rational and Radical Expressions returns the
   compliment.** The note reads: "Sign analysis is the same tool Rational and
   Radical Expressions used on rational expressions, with one addition there:
   the sign can also change where a denominator is zero, and that value is
   excluded rather than included. Here the expression is defined everywhere, so
   the roots are the only critical values." Course 5 has no rational-inequality
   lesson and never analyses the sign of a rational expression; the phrase "sign
   analysis" occurs once in `content/algebra/c5_rational/`, in
   `radical-functions-and-their-graphs` `.concepts[0][1]`, which says the
   technique comes "from Polynomials and Factoring" — and course 4 has no
   inequality lesson either, only a sign row used as a check in
   `graphs-of-polynomial-functions`. So course 5 needs this lesson's method one
   course early, cites course 4 for it, and this lesson cites course 5 for it.
   The dependency is circular and no course on the path teaches the technique
   before it is required. See the companion assessment for course 5, which
   carries the same finding from the other side and sets out three ways to
   resolve it.

5. **`solving-by-factoring` `.standard[1]` still carries an orphaned lesson
   number.** "…spend a few seconds looking for an integer factorisation, and
   move to 'Completing the Square' or 5 without regret when none appears." The
   "or 5" is the surviving half of "lesson 4 or 5" — the de-numbering pass
   replaced the first reference with a title and left the second as a bare
   digit. A reader meets "or 5" as a sentence fragment on the completion
   standard of lesson 2. The line is unchanged by the de-numbering commit, so it
   predates that work and the first pedagogy pass did not catch it either. It is
   also a counterexample to that commit's own summary — "all 959 references
   resolve to a real lesson, and the cross-course ones are exact" (`d0a238a`).
   This one resolves to nothing, and items 4 above and 1 in the course 5
   assessment are two cross-course references that resolve to the wrong course.
   Three counterexamples is not a large number against 959; the point is that
   the claim is stated as exhaustive and a single grep for a bare digit after a
   lesson title finds the first of them.

### Facts a reader would trust that are wrong

6. **`vertex-form-and-the-axis-of-symmetry` `.worked.after[2]` names a wrong
   answer that the named error does not produce.** The faded rehearsal is
   `y = 3x² + 12x + 5` with `3(x² + 4x) + 5` supplied, and it closes: "Compare
   with `y = 3(x + 2)² − 7` and vertex `(−2, −7)`; a constant of `−3` instead of
   `−7` exposes the missing multiplication by `a`." The answer is right
   (`h = −2`, `k = f(−2) = 12 − 24 + 5 = −7`). But the named error —
   bringing the `−4` out of the bracket without multiplying by `3` — gives
   `3(x + 2)² − 4 + 5 = 3(x + 2)² + 1`, a constant of `+1`. Nothing plausible
   produces `−3`. This is the one sentence a reader consults *because* they got
   the rehearsal wrong, and it sends them to look for an error that does not
   have that signature. The identical defect is in course 4's
   `the-factor-theorem-and-rational-roots` `.worked.after[2]`, which suggests
   these closing diagnostics were written alongside the rehearsals and not
   executed against them.

7. **The course home's headline formula is missing the bracket the course
   insists on.** `__init__.COURSE["key"][1]` reads
   `x = (−b ± sqrt(b² − 4ac)) / 2a`. Read as written, `/ 2a` divides by `2` and
   multiplies by `a`. `the-quadratic-formula` `.key` renders it correctly as a
   stacked fraction, its theorem writes `(−b + √(b² − 4ac))/(2a)` with the
   bracket, and `.mistakes[2]` is *about* dividing only part of the numerator —
   so the one place the formula appears without its bracket is the course home,
   which is the first place a reader sees it and the one they will copy.

### Distractors that are also true

8. I argued for every wrong answer in all 43 items. Nothing is defensible
   outright; two are close enough to record, and both are close for the same
   reason — the stem asks for a complete answer without saying so.
   - `the-square-root-property` `.quiz[0]`: "Solve `x² = 49`", with `x = 7`
     among the wrong answers. `7` is a solution. The convention that "solve"
     means "find every solution" is stated in
     `quadratic-equations-and-the-zero-product-property` `.concepts[2]` ("an
     answer carrying one number is usually half an answer"), and the `why` here
     calls it "the standard loss of half the answer" — so the course has laid
     the ground and the question is defensible. It survives; it is listed
     because the same shape of question in course 4's
     `factoring-out-the-greatest-common-factor` does *not* survive, and the
     difference is one sentence of groundwork.
   - `solving-by-factoring` `.quiz[2]`: "Why does `5(x − 2)(x + 7) = 0` have two
     solutions rather than three?", with "A quadratic has at most two, so one of
     the three is dropped" among the wrong answers. Its first clause is true and
     is proved in course 4 (`the-factor-theorem-and-rational-roots` `.body`, "A
     polynomial of degree `n` has at most `n` roots"). Its second clause is
     false, and the `why` addresses neither it nor option (c) — so a reader who
     chose it because the first half is a theorem they were taught is told
     nothing about the half that is wrong. Fixing the `why` fixes the question.

### Quiz feedback that does not answer the wrong answer

9. This course's feedback is the best of the three and it is not uniform. The
   models are `quadratic-equations-and-the-zero-product-property` `.quiz[1]`,
   which works out what each of the four options does to the original equation
   and even solves the question properly at the end (`x² − 7x − 8 = 0`, roots
   `8` and `−1`, "neither of them visible in the original brackets"), and
   `the-discriminant` `.quiz[3]`, which diagnoses all three wrong plans by the
   reasoning error behind each ("assumes integer factors always exist",
   "confuses universality with efficiency", "assigns methods without checking
   their hypotheses"). Against that standard:
   - `quadratic-equations-and-the-zero-product-property` `.quiz[0].why` explains
     only option (b) — the sign-copying model — and leaves `x = 4` or `x = 2`
     and `x = −4` or `x = −2` unnamed, though those are two *different* partial
     sign errors and the lesson's mistake 3 is about exactly this.
   - `solving-by-factoring` `.quiz[2].why` — see item 8.
   - `the-quadratic-formula` `.quiz[1].why` diagnoses options (b) and (c) and
     says nothing about (d), `x = 3` or `x = −1/2`, which is the one that gets
     one root right and inverts the sign of the other — the hardest error to
     see in your own work and the one most worth naming.
   - `operations-with-complex-numbers` `.quiz[1].why` ("Written in standard
     form, `1/i` is") spends its whole length on why `i` is wrong and never
     mentions `−1` or `1`, which encode the two different ways of mishandling
     `i · i`.
   - `graphs-of-quadratic-functions` `.quiz[0].why` is one sentence and
     dismisses three options together ("`b` and `c` move the parabola around the
     plane; no value of either can turn it over"). Correct and slightly too
     brisk: options (a) and (c) name *different* coefficients, and the reader
     who chose one is told about both.
   - `complex-roots-of-quadratics` `.quiz[0].why` names all three — a model —
     while `.quiz[2].why` leaves "One repeated solution" undiagnosed, which is
     the `D = 0` boundary `the-discriminant` `.mistakes[1]` was written to
     protect.

### Labs that do not agree with their own lessons

10. **`quadratic-equations-and-the-zero-product-property`'s panel describes two
    controls that do not exist, and they are the two the lesson needs.**
    `.lab[1].panel_intro`: "Set the two factors and the number on the right.
    With `0` there, the lab splits the equation and solves each factor. With
    anything else there it refuses, and shows what substituting the false answer
    actually produces." The `quadratic_lab` renders a preset select and three
    boxes labelled `a`, `b`, `c`. There is no factor control and no right-hand
    side: every equation the lab can express is `ax² + bx + c = 0`, always with
    zero on the right. So the interaction the panel promises — the one that
    demonstrates the lesson's single misconception, the one its whole worked
    example ("One equation done twice, once illegally") is built on, the one its
    `.mistakes[0]` and `.quiz[1]` both test — cannot be performed, and the lab
    cannot represent `(x − 3)(x + 5) = 9` at all. This is the most consequential
    panel-versus-control mismatch in the three courses, because the missing
    control is the lesson.

11. **`the-square-root-property`'s panel promises a shifted form the controls
    cannot build and a step-by-step isolation the mode does not print.**
    `.lab[1].panel_intro`: "Build an equation of the form `a(x − h)² + c = 0`
    and watch the isolation happen a step at a time." There is no `h` box. And
    in `sqrt` mode the lab's own block is a single row —
    `table('The square root property', [row('applies here?', sqp.text)])` — one
    line of verdict, not a step-by-step isolation. (The step-by-step trace
    exists: it is `byCompleting`, which `complete` and `vertex` modes print.)
    Combined with item 3, the lesson that teaches `x = h ± √k` has a lab that
    can only do `h = 0` and will not show its working.

12. **`equations-reducible-to-quadratic-form`'s lab is hard-wired to `u = x²`,
    and three of the lesson's four substitutions are something else.** In
    `reducible` mode `QUARTIC` is true and the back-substitution table is
    emitted as `row('substitute u = x^2', …)` with the interpretation `x² = u`
    baked in; every preset is a quartic in `x²`. The lesson teaches `u = √x`
    (worked in `.body`, tested in `.quiz[1]`), `u = 1/x` (`.body` example
    `x⁻² − x⁻¹ − 6 = 0`), `u = x³` (`.steps[0]`, and `.quiz[2]` is entirely
    about choosing it for `x⁶ − 9x³ + 8 = 0`), and `u = x² − 3` (`.body`, the
    example that carries the lesson's general definition — "the repeated object
    may be a whole expression"). The `.def` says in terms that "doubled
    exponents are one common clue, not the definition", and the lab implements
    the clue rather than the definition. What the lab does do, it does well: the
    panel's instruction — "Choose a preset whose `u` comes out negative and
    watch two of the four solutions disappear" — works on presets 3 and 5, and
    that is the lesson's `.mistakes[1]`.

13. **`maximum-and-minimum-problems`' lab has no way to restrict the domain, and
    the domain is the half of the lesson the algebra does not cover.** The
    `optimise` mode reports the unconstrained vertex and nothing else. The
    lesson's `.concepts[2]` is "The situation restricts the variable", and it
    goes further than most courses do — "An excluded endpoint may leave a bound
    that is approached but never attained, so an optimum need not exist";
    `.steps[3]` is about testing the vertex against the domain; `.body` works
    the `P(x) = −3x² + 30x − 12` case where the vertex at `x = 5` is outside
    `0 ≤ x ≤ 4`, and the integer case where the vertex sits at `5/2`; and
    `.quiz[2]` is the out-of-range vertex. None of it is in the lab, and the
    panel ("Each preset is a model: an area, a profit, a height") implies the
    modelling is what the lab is for. The presets are well chosen — the fence
    and the projectile are both the lesson's own `.body` examples — which makes
    the missing constraint more conspicuous, not less.

14. **Preset matching is excellent in the last five lessons and poor-to-near-miss
    in the first six.** `equations-reducible-to-quadratic-form` is the model:
    four of its five presets are the lesson's `.body` math, its worked example,
    its `.body` example and its faded rehearsal, in that order.
    `vertex-form-and-the-axis-of-symmetry` offers both of the lesson's `.body`
    examples; `graphs-of-quadratic-functions` offers its `.body` example;
    `maximum-and-minimum-problems` offers two. In the first six lessons not one
    worked example is a preset, and three of them are *near misses* — the same
    `a` and `b` with a different `c`, which is the worst case because the reader
    believes they are looking at the page:
    - `solving-by-factoring` `.worked` B is `6x² + x − 12 = 0`, roots `−3/2` and
      `4/3`; the lab's fourth preset is `6x² + x − 2`, roots `−2/3` and `1/2`.
    - `completing-the-square` `.worked` A is `x² + 6x − 7 = 0`, solutions `1` and
      `−7`; the lab opens on `x² + 6x + 5`, solutions `−1` and `−5`.
    - `vertex-form-and-the-axis-of-symmetry`'s faded rehearsal is
      `y = 3x² + 12x + 5`; the lab's fourth preset is `3x² + 6x + 1`.
    `the-quadratic-formula` and `quadratic-inequalities` have no overlap at all
    between their worked examples and their presets.

15. **What the labs get right, so the recommendations do not damage it.** The
    `quadratic_lab`'s core decision — four methods computed independently and
    printed together, so that agreement is evidence rather than assertion — is
    correct and is exactly what lessons 4, 5 and 6 need; the problem in item 1
    is only that it is shown from lesson 1. The `complex_lab`'s three modes
    match their panels exactly (`intro` has "Real part a" and "Imaginary part
    b"; `arith` has `Re z`, `Im z`, `Re w`, `Im w`; `roots` has `a`, `b`, `c`),
    and `roots` mode multiplies the conjugate pair back together and compares
    `2p` and `p² + q²k` against `−b/a` and `c/a` formed independently — which is
    `complex-roots-of-quadratics` `.body`'s sum-and-product check, computed
    rather than asserted. The `inequality_lab`'s `quadratic` mode matches its
    panel ("Set the quadratic and the direction of the sign") and generates the
    inequality, the interval, the set-builder form and the number line from one
    interval structure so they cannot disagree. Those three are not in scope for
    any repair below.

### Cognitive load and structure

16. **Fourteen lessons, four modules, and the module boundaries are where they
    should be.** Solving quadratics (1–6), complex numbers (7–9), parabolas
    (10–14). The one oddity is that `quadratic-inequalities` and
    `equations-reducible-to-quadratic-form` are filed under "Parabolas" while
    being about sign sets and substitution respectively — lesson 13 earns it
    (its method 2 *is* reading the parabola) and lesson 14 does not. Minor, and
    a module rename would cost more than it returns.

17. **`the-discriminant` is the load-bearing lesson and carries the right
    amount.** Definition, three cases with proofs, the perfect-square criterion
    with a two-direction proof, what `D` does not tell you, and the method
    choice. That is a lot, but the three cases are one theorem, the criterion is
    the only genuinely new idea, and the fourth quiz question — pick the
    shortest justified method for four differently shaped equations — is the
    best single retrieval item in the three courses. Not split. Recorded as a
    judgement.
18. **`operations-with-complex-numbers` is the strongest split candidate and
    should not be split.** Addition, multiplication, powers of `i`, the failure
    of `√a·√b = √(ab)`, the conjugate, the conjugate product theorem, division,
    and closure under all four operations. Eight items — but six of them are
    consequences of `i² = −1` applied to arithmetic the reader already has, the
    lesson says so in `.concepts[0]` ("Treat `i` as a variable until the last
    step"), and the division method is one idea (multiply by a form of `1`) that
    Rational and Radical Expressions already taught with `2 + √3`. Recorded.
19. **The course home's method-choice outcome omits the method the course calls
    its centre.** `outcomes[0]` reads: "Use factoring when it is quick, the
    square root property when there is no linear term, and the formula when
    nothing else applies — not always the formula." Three methods. The `blurb`
    says "Completing the square is the centre of the course", `how_to[1]` says
    to do it by hand five times, `outcomes[1]` is a whole outcome about it, and
    `the-discriminant` `.quiz[3]` requires a four-way choice that includes it.
    The outcome that names the decision is the one place it is missing.
20. **`how_to[0]` is where the faded rehearsals are explained, and it is the
    only place.** "On each lesson, cover the complete worked example before
    attempting the faded rehearsal beneath it. The rehearsal supplies the first
    strategic decision but leaves the algebra and check to you; only then use
    the quiz as independent retrieval." Fourteen lessons carry a rehearsal and
    none of them says what it is for. Recorded so it is not lost in an edit.

## Where a learner gets stuck

- On the first page of the course, looking for the two factor boxes and the
  right-hand side the panel says to set, and finding `a`, `b` and `c` (item 10);
  and then reading a KPI headed *Discriminant*, a row headed *completing the
  square* and a status banner about perfect squares, five lessons before any of
  them is defined (item 1).
- At `the-square-root-property`'s worked examples B and C, entering the
  expanded form and being told the square root property does not apply to the
  lesson's own shifted squares (items 3 and 11).
- At `solving-by-factoring`'s completion standard, reading "move to 'Completing
  the Square' or 5 without regret" and looking for what 5 refers to (item 5).
- At `completing-the-square`'s lab, opening on `x² + 6x + 5` while the page
  works `x² + 6x − 7` — same `a`, same `b`, different answers (item 14).
- At `vertex-form-and-the-axis-of-symmetry`'s faded rehearsal, having got `+1`
  for the constant, and being told that the missing multiplication by `a`
  produces `−3` (item 6).
- At `equations-reducible-to-quadratic-form`'s third quiz question, which asks
  the reader to choose `u = x³`, with a lab whose back-substitution row is
  headed `u = x²` (item 12).
- At `maximum-and-minimum-problems`' third quiz question, on an out-of-range
  vertex, with a lab that has no domain to go out of (item 13).
- At `quadratic-inequalities`' closing note, told that Rational and Radical
  Expressions has already done this — it has not, and the lesson in that course
  that needed this method was told to look in Polynomials and Factoring, which
  does not have it either (item 4).
- At `the-quadratic-formula`'s second quiz question, having chosen `x = 3` or
  `x = −1/2`, and being told about the two options they did not choose (item 9).

## What this pass caught that the first missed, and what it disputes

The prior assessment (now `prior/quadratics-and-complex-numbers.md`) is the
strongest of the three Algebra documents it belongs to, and most of its repairs
are live and verified. Confirmed here: the pre-complex modes no longer print
`i`, via the `SHOW_COMPLEX` gate (its item 4); the course footer now says the
lab "tests all four solution methods independently … A method that does not
apply says why", which is what the lab does (its item 5);
`completing-the-square` `.body` now says the completing constant is
"non-negative … it is `0` only when the linear coefficient is already `0`" (its
item 6); `vertex-form-and-the-axis-of-symmetry` `.concepts[2]` now distinguishes
legal equation balancing from preserving an isolated rule, and `.mistakes[2]`
works the distinction out in full (its item 7);
`maximum-and-minimum-problems` `.concepts[2]` and `.steps[3]` now handle closed,
discrete and excluded-endpoint domains, and the unboundedness proof completes
both directions (its item 8); `equations-reducible-to-quadratic-form` `.def` now
gives the general `a[f(x)]² + b[f(x)] + c` pattern and demotes doubled exponents
to a clue (its item 9); `the-discriminant` gained the four-shape rehearsal and
the fourth quiz item (its "mixed method selection"); and all fourteen lessons
carry a faded rehearsal.

**Disputed, and it is the important one.** Its opening paragraph states: "The
prerequisite trail through courses 1–5 is sound. … course 5 supplies radical
simplification, conjugates, domain restrictions and sign analysis. No earlier
course needs to change for this course to work." Course 5 does not supply sign
analysis — it *needs* it, one course early, for
`radical-functions-and-their-graphs`, and cites course 4 for it, and course 4
does not have it either (item 4). The assessment that declared the trail sound
is the same document whose course's lesson 13 `.note` asserts that course 5
already did this. A per-course review is structurally the least likely place to
catch a circular dependency and the most likely to launder one, which is why the
brief for this pass asked for the backwards check to be performed and stated
rather than assumed.

**Also disputed.** Its item 4 is titled "The interaction crossed the
prerequisite boundary" and identifies exactly one crossing — the complex pair
printed before `i` — and its repair summary says "the quadratic lab now
suppresses complex-form output in the lesson 3–6 modes and reports 'no real
solution' until `complex-numbers` has defined the larger system." True, and
well done. But the lab crosses the boundary in at least three other ways on the
same pages, and two lessons earlier than the ones it names: the discriminant
KPI, the four-method block and the perfect-square status banner are all
unconditional (item 1). Its methodology paragraph says "The shared quadratic lab
was also read in full … so claims about what a learner sees are based on the
rendered interaction rather than its panel copy alone" — which makes the miss a
matter of what was looked for rather than of access. Reading `redraw()` for what
it always emits, rather than for what each mode emits, is the check that turns
this up.

**Not attempted by the first pass.** Its "Most quiz feedback is already
diagnostic" is broadly fair and is not a substitute for the audit: six items
diagnose fewer than all three distractors, including the two in the formula and
the `1/i` question (item 9). The "distractors that are also true" audit that
`content/AGENTS.md` names was not run; running it here found nothing
indefensible and two near cases worth recording (item 8). Its claim that "claims
about what a learner sees are based on the rendered interaction" did not extend
to which *controls* each mode renders: lesson 1's panel describes a factor pair
and a right-hand side that do not exist (item 10), lesson 3's describes an `h`
box and a step-by-step trace that do not exist (item 11), lesson 14's lab is
`u = x²` only (item 12), and lesson 12's has no domain restriction (item 13). It
did not check the faded rehearsals it introduced against the errors they claim
to diagnose (item 6), did not notice the orphaned "or 5" in lesson 2's
completion standard (item 5), and did not check the course home's key formula
against the bracket discipline lesson 5 teaches (item 7).

## Repairs this pass recommends

None applied. All are inside the existing URL space — no lesson added, removed,
renamed or reordered — so the five URL declarations in `AGENTS.md` §1 are
untouched by every item below.

**The cross-course repair** *(item 4)*: decide it together with the course 5
assessment, which sets out the three options. The preferred one adds four lines
to `graphs-of-polynomial-functions` (course 4 lesson 13) stating the sign row as
a method, and then both `radical-functions-and-their-graphs` `.concepts[0][1]`
and `quadratic-inequalities` `.note` point at a lesson that exists. The minimum
repair, if that is not taken, is to delete the false clause from
`quadratic-inequalities` `.note` and replace it with what is true: that
Rational and Radical Expressions solved one quadratic sign condition by hand in
`radical-functions-and-their-graphs`, and this lesson turns that into a method.

**Labs, `scripts/mathpath/labs/algebra_quadratic.py`** (run
`node scripts/labcheck.js --generated` and `node scripts/mathcheck.js` after
any change here; `mathcheck` executes this file's shipped arithmetic, so a mode
gate must not change any computed value):

- Add a second gate beside `SHOW_COMPLEX`, in the same style and with the same
  kind of comment — for example
  `var SHOW_DISCRIMINANT = ['discriminant', 'graph', 'vertex', 'optimise', 'reducible'].indexOf(MODE) >= 0;`
  and `var SHOW_ALL_METHODS = ['complete', 'formula', 'discriminant', …]`. Then:
  (a) make the first KPI's label and value conditional — `Real roots` and
  `Vertex` are fine on every lesson, `Discriminant` is not before lesson 6;
  (b) emit the "The four methods, computed separately" block only where the
  reader has met the methods — on `zero` and `factor` it should be a two-row
  block (factoring, and the square root property where `b = 0`); (c) rewrite the
  status banner's opening clause so that on `zero` and `factor` it does not lead
  with the discriminant or the perfect-square criterion. The four methods should
  still be *computed* on every redraw — that is the design and it is right — but
  what is printed should follow lesson order, exactly as the existing comment at
  line 116 says it should. *(items 1, 2)*
- `bySquareRoot` — accept a shifted square. Either add an `h` control in
  `sqrt` mode (so the lesson's `a(x − h)² + c = 0` can be built directly, which
  is what its panel already promises), or detect a perfect-square trinomial
  (`D = 0` after removing the content, or more simply: complete the square and
  report `x = h ± √k` whenever `k ≥ 0`) and say "the square root property
  applies after completing the square: `(x + b/2a)² = k`". The second is
  cheaper and matches the lesson's own argument that the property "does not care
  what is being squared". Either way, `sqrt` mode should print the isolation
  trace its panel promises — `byCompleting` already produces one. *(items 3,
  11)*
- `reducible` mode — generalise the substitution beyond `u = x²`, or narrow the
  lesson's claim on the page. The full fix is a `sub` config key
  (`x^2`, `x^3`, `sqrt(x)`, `1/x`) selecting both the display string and the
  back-substitution rule; `QUARTIC`'s plotting function and the
  `row('substitute u = x^2', …)` line are the two places that hard-code it.
  *(item 12)*
- `optimise` mode — add an optional domain (`xmin`, `xmax`, and an
  integers-only toggle), report whether the vertex is inside it, and compare the
  permitted endpoints when it is not. This is the lesson's `.concepts[2]`,
  `.steps[3]` and `.quiz[2]`, and it is the only part of
  `maximum-and-minimum-problems` the lab cannot currently reach. *(item 13)*
- Presets — set `PRESETS["factor"]` to include `6x² + x − 12`,
  `PRESETS["complete"][0]` to `x² + 6x − 7`, `PRESETS["vertex"]` to include
  `3x² + 12x + 5`, `PRESETS["formula"]` to include `2x² − 7x + 3` and
  `x² + 4x + 1`, and `INEQ_PRESETS["quadratic"]` in
  `scripts/mathpath/labs/algebra_equations.py` to include `x² − x − 6 ≤ 0` and
  `2x² − x − 6 > 0`. A near-miss preset is worse than no preset. *(item 14)*

**Content, `content/algebra/c6_quadratics/part_a.py`:**

- `quadratic-equations-and-the-zero-product-property` `.lab[1].panel_intro` —
  rewrite to describe the controls that exist and to say what the lab cannot do:
  "Set `a`, `b` and `c`. The lab works on `ax² + bx + c = 0`, which is why it
  always has zero on the right — the illegal route above cannot be built here,
  and that is the point: getting the zero is step 1 of every method in this
  course." That turns the mismatch into the lesson. *(item 10)*
- `the-square-root-property` `.lab[1].panel_intro` — describe the `a`, `b`, `c`
  boxes, and either promise the shifted form only after the lab change above, or
  say plainly that the property row applies when `b = 0` and that a shifted
  square has to be expanded first. *(items 3, 11)*
- `solving-by-factoring` `.standard[1]` — "…move to 'Completing the Square' or
  5 without regret…" → "…move to 'Completing the Square' or 'The Quadratic
  Formula' without regret…". *(item 5)*
- `solving-by-factoring` `.quiz[2].why` — add a clause for option (d): a
  quadratic does have at most two solutions, and that is *why* a constant factor
  cannot contribute a third — not because one of three was dropped. Add a clause
  for option (c) naming `x = 5` as reading a constant factor as if it contained
  `x`. *(items 8, 9)*
- `quadratic-equations-and-the-zero-product-property` `.quiz[0].why` — name the
  third and fourth options separately: one flips both signs, one flips neither.
  *(item 9)*
- `the-quadratic-formula` `.quiz[1].why` — add option (d): `x = 3` is right and
  `x = −1/2` inverts the sign of the second root, which is the error that
  survives a partial check. *(item 9)*

**Content, `content/algebra/c6_quadratics/part_b.py`:**

- `vertex-form-and-the-axis-of-symmetry` `.worked.after[2]` — replace the
  diagnostic. Bringing the `−4` out without multiplying by `3` gives
  `3(x + 2)² + 1`, so the sentence should read "a constant of `+1` instead of
  `−7` exposes the missing multiplication by `a`", which is both true and a
  stronger clue (the reader can see `5 − 4` in their own working). *(item 6)*
- `quadratic-inequalities` `.note` — per the cross-course repair above.
  *(item 4)*
- `equations-reducible-to-quadratic-form` `.lab[1].panel_intro` — until the lab
  change lands, fence it: "The control is a quadratic in `u = x²`; the `√x`,
  `1/x` and `x³` substitutions above are on paper." *(item 12)*
- `maximum-and-minimum-problems` `.lab[1].panel_intro` — add "The lab reports
  the unconstrained vertex; deciding whether the situation allows it is the part
  that is yours." *(item 13)*
- `operations-with-complex-numbers` `.quiz[1].why` — name `−1` and `1` as the
  two ways `i · i` goes wrong. *(item 9)*
- `complex-roots-of-quadratics` `.quiz[2].why` — add a clause for the `D = 0`
  option. *(item 9)*
- `graphs-of-quadratic-functions` `.quiz[0].why` — split the single sentence
  into one clause for `c` and one for `b`. *(item 9)*

**Content, `content/algebra/c6_quadratics/__init__.py`:**

- `key[1]` — `"x = (−b ± sqrt(b² − 4ac)) / 2a"` → `"x = (−b ± √(b² − 4ac)) / (2a)"`.
  One pair of brackets, on the course's headline formula, matching what lesson 5
  proves and what its `.mistakes[2]` protects. *(item 7)*
- `outcomes[0]` — add completing the square to the method-choice list: "…the
  square root property when there is no linear term, completing the square when
  the quadratic is one constant from a square, and the formula when nothing else
  applies". *(item 19)*

**Not recommended.** Do not stop the lab computing all four methods on every
redraw — the independent computation is the evidence the course is built on, and
the repair in item 1 is about what is *printed*, not about what is computed. Do
not split `the-discriminant` or `operations-with-complex-numbers` (items 17 and
18). Do not rename the "Parabolas" module for lesson 14's sake (item 16). Do not
rewrite the quiz feedback wholesale: this course's is the best of the three, and
`quadratic-equations-and-the-zero-product-property` `.quiz[1].why` and
`the-discriminant` `.quiz[3].why` are the templates the six exceptions should be
brought up to.
