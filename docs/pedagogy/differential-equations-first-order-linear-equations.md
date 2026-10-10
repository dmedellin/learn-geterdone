# Pedagogy assessment — First-Order Linear Equations (differential equations, course 6)

Formed from the eight lesson dicts in `content/differential_equations/c6_linear/`
(`part_a.py`, lessons 1–4; `part_b.py`, lessons 5–8; `__init__.py`, the course
dict), the spoken forms in `content/spoken/differential_equations_c6_linear.py`,
and the kit they render through (`scripts/mathpath/labs/dekit_b.py`, modes
`linear1` and `stiff`), on branch `feat/differential-equations` before the
Subject was wired into the site. The design authority is
`docs/differential-equations/PLAN.md` §0 (the exactness rule), §C (course 6),
§D.3 (`linear1`, `stiff`), §D.5 and §F; the course was written in two parts, so
the seam at lesson 5 is assessed as well.

Every lesson was read in full before anything was changed. Every pinned figure
and every figure quoted in prose was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py differential_equations --course first-order-linear-equations`),
and every rounded figure was recomputed in double precision and every exact one
in `fractions.Fraction`. Lessons, in course order: `the-standard-form`,
`constant-coefficients-and-the-steady-state`, `the-integrating-factor`,
`homogeneous-plus-particular`, `polynomial-forcing`,
`exponential-and-sinusoidal-forcing`, `circuits-tanks-and-loans`,
`stiffness-when-the-step-is-too-big`. The course may assume Equilibria,
Stability and Phase Lines and everything before it, plus the Algebra Subject;
it is judged against that.

## Verdict

The course teaches its subject. A reader who finishes it can put a first-order
linear equation in standard form with the signs right, name the steady state of
`y′ + a·y = b` and say whether it attracts, build an integrating factor and say
why the left side becomes a derivative, split a solution into `y_p + y_h` and
fit the constant after the sum, choose and match a particular solution for a
polynomial, exponential or sinusoidal forcing including the resonant case,
write a capacitor, a tank and a loan as one equation, and compute Euler's
factor `1 − a·h` with the bound `h < 2/a`. Those are the acts the `standard`
fields measure and the labs compute, and no objective is "understand X". The
`mistakes[0]` of every lesson is the §C misconception, each refuted with a
specific residual, fraction or factor. Every pinned tile matched the lab, and
every figure quoted in prose agreed with the lab or with a recomputation.

The defects found were local and are repaired below: one arithmetic error
repeated three times in `polynomial-forcing` (the wrong-sign reading of `a`
gives `c₀ = −1`, not `1`, so the slipped solution is `2t − 1` and its residual
is `4 − 4t`, not `−4t`), one sentence in `homogeneous-plus-particular` that
says the opposite of what the algebra beside it shows, one mistake paragraph in
`circuits-tanks-and-loans` whose description of the slipped loan was wrong in
substance, two cross-references the reader cannot follow, two rational figures
rounded outside the exactness rule, a footer claim the lab does not honour, and
a prerequisite the course borrows from the next course without saying so.
Nothing needs splitting, merging or reordering within the URL space the course
has; one split is recorded under remaining issues.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names what is produced: the
  equation in standard form with `p` and `q` and their signs
  (`the-standard-form`); `b/a`, the starting gap, and Euler's value after `n`
  steps as a fraction (`constant-coefficients-and-the-steady-state`); a
  function with `μ′ = p·μ` checked by differentiating, and the constant divided
  by `μ` (`the-integrating-factor`); the constant computed after the two parts
  are added (`homogeneous-plus-particular`); the matching equations from the
  top power down, solved as fractions (`polynomial-forcing`); the decision
  whether the guess needs a factor of `t` (`exponential-and-sinusoidal-forcing`);
  the rate written as gain minus loss with the signs checked
  (`circuits-tanks-and-loans`); the factor, its sign and size, and the bound
  (`stiffness-when-the-step-is-too-big`).
- **The exactness rule is kept, and the tiers are named in the sentence that
  reports the number.** `constant-coefficients-and-the-steady-state` sets
  `45/16`, "exact arithmetic on Euler's approximation", beside
  `3 − 3·e^(−2) ≈ 2.59399`, "a rounded value of the curve", and names the
  difference `≈ 0.218506` as the error of the method and "the only part of the
  table that is not exact"; the four rounded entries in its table were
  recomputed and are right to six figures. `stiffness-when-the-step-is-too-big`
  does the same for `6561/256 ≈ 25.6289` against `e^(−20) ≈ 2.06115·10⁻⁹`.
  `the-integrating-factor` is the lesson that stays in fractions from start to
  finish and says so: "Nothing here was rounded, because `μ` was a power of
  `t` and the integral of a power is a power." `circuits-tanks-and-loans` says
  of the payoff time that the lab prints no logarithm tile, that `ln 6` is
  irrational, and that `≈ 35.8352` is the reader's own rounded computation.
- **The method is kept apart from the solution.** The material clause is
  earned rather than recited: "Every fraction in the column is right; none of
  them is the solution" (`constant-coefficients-and-the-steady-state`); "the
  method has turned a decay into a growth"
  (`stiffness-when-the-step-is-too-big`); and the backward method is "stable,
  not accurate", with `(2/7)⁸ = 256/5764801` set against the true value to show
  it. No lesson calls `yₙ` the solution at `tₙ`.
- **Claims are stated as claims.** The solution of `u′ = −a·u` is "a claim from
  Separable Equations, Growth and Decay that is not reproved here"; the rate of
  `e^(a·t)` is "a claim from the earlier courses"; the product rule is "verified
  exactly on polynomials in Rates of Change and the Derivative". The `thm`
  blocks that are proved (scaling, the shifted exponential, the integrating
  factor, superposition, one polynomial solution, exponential and sinusoidal
  forcing, the step bound) are proved with algebra the reader has.
- **The lab's limit is stated where the lesson leans on it, and never as a
  verdict on the mathematics.** `the-standard-form` says the lab refuses
  `y′ = 2y + t²·y` because its `p` is outside the two families the lab solves,
  "and the reason it gives is the lab's limit and not a verdict on the
  equation". `the-integrating-factor` lists the three refusals the kit makes
  (`p` outside constant or `a/t` with `a` from `−4` to `4`, an integral with a
  `ln t` in it, `t₀ = 0` for `p = a/t`) and they match `lfSolve` and `lfOverT`
  in the kit. `circuits-tanks-and-loans` says the lab prints no payoff time.
- **The misconceptions are refuted with the specific number.** `y = 6` gives
  `0 + 12 = 12`, not `6` (`constant-coefficients-and-the-steady-state`); the
  factor `e^(2/t)` has rate `−(2/t²)·e^(2/t)`, not `(2/t)·μ`
  (`the-integrating-factor`); fitting `C` before adding `y_p` leaves
  `y(0) = 7/9` (`homogeneous-plus-particular`); `c·t²` alone leaves the residual
  `2t` (`polynomial-forcing`); `A·cos(t)` alone leaves `−(1/2)·sin(t)`
  (`exponential-and-sinusoidal-forcing`); at year `17` the loan still owes
  `≈ 73.2071` (`circuits-tanks-and-loans`); `h = 1/4` wobbles to `1/65536` and
  is "inaccurate, but not unstable" (`stiffness-when-the-step-is-too-big`).
- **Worked example, then faded guidance.** Every `worked.after` ends with "For a
  rehearsal…" naming a second preset to predict before pressing the button, and
  the quiz then asks for the same act on a third instance. The progression from
  `homogeneous-plus-particular` (one guess, `A·t + B`, made for one equation)
  through `polynomial-forcing` (the guess as a rule with a proof that it always
  works) to `exponential-and-sinusoidal-forcing` (three shapes and the trap) is
  the right order and each lesson names the one before it.
- **Figures agree with the lab.** Every pinned tile on the eight pages matched
  the observed tile, and every tile the prose quotes was found in the observed
  output: `e^(3t)`, `C·e^(−3t)`, `1/t²`, `C·t²`, `2`; `3`, `45/16`, `25/8`,
  `−2 (repelling)`, `369/128`; `t²`, `y = t³/5 + (4/5)/t²`, `4/5`, `3/2`;
  `11/9`, `(2/3)·t − 2/9`, `−1/3`; `t² − 2t + 2`, `−2t − 1`,
  `t³ − 3t² + 6t − 6`; `(2/5)·cos(t) + (1/5)·sin(t)`, `t·e^(−2t)`, `2/3`;
  `5/2`, `200`, `120 (repelling)`, `B = 120 − 20·e^(t/20)`; `−3/2`,
  `oscillates and grows`, `h < 2/5`, `6561/256`, `≈ 2.06115e-9`, `2/7`,
  `256/5764801`. The claim that the `h = 1` Euler column of the loan crosses
  zero between years `35` and `36` was checked against the closed form
  (`B(35) ≈ 4.90795`, `B(36) ≈ −0.992949`), and the claim that the steps view
  shows a rounded closed-form column was verified in `lfRender`.
- **The seam at lesson 5 is nearly invisible.** `homogeneous-plus-particular`
  closes by naming what the second half does; `polynomial-forcing` opens with
  a failed guess on `y′ + y = t²` that the first half's `A·t` failure prepares.
  Both parts cite lessons by title and courses by name, both spell British
  (`behaviour`, `recognise`), and both use the same tile vocabulary. The one
  visible difference, part A's `A`, `B` against part B's `c₂`, `c₁`, `c₀`, is
  now bridged in one clause (below).

## What it taught badly, or said wrongly

### Facts a reader would trust that were wrong

- **`polynomial-forcing`, example "Why the sign of a matters here", quiz 2
  `why`, and `mistakes[2]`.** Reading `a` as `+2` in `y′ − 2y = 4t` was said to
  give `c₁ = 2` and `c₀ = 1`, hence `2t + 1` with residual `−4t`. The matching
  equations under that misreading are `2c₁ = 4` and `c₁ + 2c₀ = 0`, so
  `c₀ = −1`, the slipped solution is `2t − 1`, and substituting it into the real
  left side gives `2 − 2·(2t − 1) = 4 − 4t`. (The residual `−4t` quoted belongs
  to `2t + 1`, which no consistent misreading produces; it survives as quiz 3's
  distractor, where the arithmetic for it is right.) In quiz 2, the distractor
  `2c₂ = c₁`, `c₁ = c₀` gives `c₁ = 2`, `c₀ = 2` and a residual of `4t + 4`,
  not `4t`. Repaired in all three places.
- **`homogeneous-plus-particular`, body, after the check:** "The guess had no
  constant term in the first place for the reason the next lessons make into a
  rule" — the guess `A·t + B` has a constant term, and having it is the whole
  point of the sentence that follows. Repaired: the guess carried `B` although
  the forcing has no constant, because the derivative of `A·t` is a constant
  that something must cancel.
- **`circuits-tanks-and-loans`, `mistakes[2]`:** the slipped equation
  `B′ + B/20 = −6` from `B(0) = 100` was said to "decay toward `−120` without
  ever being repaid on schedule". Its solution `−120 + 220·e^(−t/20)` falls
  through zero at `20·ln(11/6) ≈ 12.1227` years, sooner than even the
  no-interest estimate, and then keeps falling. Repaired, and the impossibility
  (interest cannot clear a loan faster than no interest) is now named as the
  sign of the slip.

### Prose looser than the lab or the mathematics

- **`the-standard-form`, body:** "a positive constant `p` makes solutions die
  away" is false for a forced equation (`y′ + 2y = 6` settles to `3`); it is
  true of the homogeneous solutions, which is what the lesson means. Repaired.
  The lab paragraph said the lab "prints two things this lesson has not
  derived" while the page shows five tiles the lesson has not derived; it now
  says which two matter and that the rest are later lessons' business.
- **`the-integrating-factor`, body:** `μ′ = p·μ` for `μ = e^(∫p dt)` was
  attributed to "the chain rule" without saying that the chain rule was
  verified on polynomials and is applied to the exponential as a stated claim,
  which is how every other lesson handles the exponential's rate. Repaired.
- **`exponential-and-sinusoidal-forcing`, worked `after`:** "After a little
  while the exponential is gone" contradicts the course's own insistence
  (`constant-coefficients-and-the-steady-state`) that the gap is never zero.
  Repaired to "never zero, but soon smaller than the drawing can show".
- **`constant-coefficients-and-the-steady-state`, lab panel:** the reader is
  told to set `h = 1/2` and watch the factor change; at that step the factor is
  exactly `0` and the polygon lands on the steady state in one step, which the
  lesson did not mention and a reader would find alarming. One sentence added
  to the warning paragraph.
- **`circuits-tanks-and-loans`, body and panel:** the sign change "between year
  `35` and year `36`" needs the step count raised to at least `36`; the preset
  ships `n = 4`. Both now say so.

### Prerequisite order

- **`exponential-and-sinusoidal-forcing` uses the rates of sine and cosine**,
  which the Subject first demonstrates in “Sine, Cosine and Their Rates”, the
  opening lesson of the next course; Algebra has no trigonometry. PLAN §C puts
  the cosine forcing here, so the order is the design's. The honest handling is
  to state the two facts as the claim the matching rests on and name where
  they are demonstrated, which the lesson now does in one paragraph before the
  first cosine guess. Recorded for the PLAN rather than reaching into course 7.

### The exactness rule

- `100/6 ≈ 16.67` (three places in `circuits-tanks-and-loans`) and
  "`2/7` is nearer `0.2857`" (`stiffness-when-the-step-is-too-big`) rounded
  rational numbers to four figures with no stated rule; the quiz `why` said
  "about `35.8`". All now print six significant figures with `≈`
  (`16.6667`, `0.285714`, `35.8352`), which is the one rounding rule the
  Subject uses.

### Cross-references

- **`the-standard-form`, steps:** "the last lesson of this half" refers to the
  authoring split, which the reader never sees. Now “Homogeneous Plus
  Particular”, by title. `homogeneous-plus-particular`'s note says "the next
  half of the course", which is relative prose and stays.

### Speech

- Every math run on the eight rendered pages was read from `data-say`. The
  §D.5 call rule works throughout: `y(0) = 0`, `B(0) = 130`, `q(0) = 0`,
  `y(1) = 1`, `p(t)`, `q(t)` all read as calls; `μ(t₀)` and `y_p(t₀)` and every
  `(μ·y)′` have spoken forms; `∫p dt`, `tᵃ`, `|1 − a·h|`, `2.06115·10⁻⁹`,
  `ln 6`, `5%` read correctly; `speechcheck` reports no ambiguous run and no
  stale spoken form. Three runs read wrongly and were rewritten rather than
  given spoken forms: the key line "match cos and sin terms" read "cosine of
  and sine of" (now `cos(ωt) terms, sin(ωt) terms`), the matching lines
  `cos:` and `sin:` in the math block and worked example read as the bare word
  (now `cos(t) terms:`), and `the-standard-form`'s "inside `sin`, `e` or `ln`"
  read "sin, e or ln" (now "a sine, an exponential or a logarithm"). The
  mistake title "Using e^(p(t)) instead of e^(∫p dt)" was a plain field that the
  renderer split at the space, reading "e to the power the integral of p" and
  dropping "dt)"; retitled in words.
- Not changed: lowercase `a` reads as the letter name "A" everywhere, which is
  the global engine's rule for the article, and the renderer wraps math-looking
  fragments of plain `standard` heads (`+ p(t)·y =`) as it does on every
  Subject. Both are chrome, not content.

### Course home

- `footer_lead` said "each solution is checked by substitution into the
  equation". The `linear1` kit solves the coefficient system exactly but prints
  no residual; it is the lessons that check by substitution, line by line.
  Repaired to say so.

## Where a learner gets stuck

- **`the-standard-form` shows five tiles the lesson has not defined**, and one
  preset pins the steady state (`2`) a lesson before the word is defined. The
  lab paragraph now says which two tiles matter and that the rest are for
  later; the pin is harmless and matches `mistakes[2]`'s "settles to `2`".
  Recorded so nobody hides tiles per lesson.
- **The sign of `a` when a term crosses the equals sign** is the error the
  course names in four lessons (`the-standard-form`, `polynomial-forcing`,
  `circuits-tanks-and-loans` twice). That is the right amount of repetition
  for the slip that produces the wrong exponent in every later formula, and
  each refutation is a different residual.
- **`exponential-and-sinusoidal-forcing` carries three shapes of guess and the
  resonant case**, the most new material in the course, plus two facts about
  sine and cosine stated on credit. The quiz covers each piece, the worked
  example does the sinusoid and the rehearsal does the resonant case. It is as
  good as one URL makes it; see remaining issues.
- **Backward Euler is introduced and dismissed in one lesson**
  (`stiffness-when-the-step-is-too-big`). The lesson states the cost honestly
  (an equation to solve per step for a nonlinear right-hand side) and says the
  general theory is not here, which `not_covered` repeats. A reader wanting
  more is told where the course stops.

## Repairs made in this pass

In `content/differential_equations/c6_linear/__init__.py`: `footer_lead`. In
`part_a.py`: `the-standard-form` the sign paragraph, the lab paragraph,
`steps[3]`, `steps[4]`, `mistakes[1]`; `constant-coefficients-and-the-steady-state`
the warning paragraph (`h = 1/2` gives factor `0`); `the-integrating-factor`
the chain-rule paragraph and `mistakes[0]`'s title; `homogeneous-plus-particular`
the paragraph after the check. In `part_b.py`: `polynomial-forcing` the
substitution paragraph (seam bridge), the wrong-sign example, quiz 2 `why`,
`mistakes[2]`; `exponential-and-sinusoidal-forcing` the key line, a new
paragraph stating the sine and cosine rates as claims, the matching lines in
the math block and worked example, the worked `after`;
`circuits-tanks-and-loans` the sign-change sentence, the panel, three
`100/6` figures, quiz 4 `why`, `mistakes[2]`; `stiffness-when-the-step-is-too-big`
the `2/7` sentence. No preset or `expect` changed. No math run that has a
spoken form was removed or altered, so `content/spoken/differential_equations_c6_linear.py`
needed no change; every key in it is still a live run, and the rewritten runs
read correctly without one.

Slugs, lesson count, modules, lab keys and modes are as
`docs/differential-equations/COURSES.json` lists them.
`scripts/preview_subject.py differential_equations --course first-order-linear-equations`
reports OK: 9 pages, every lab executes and survives the sweep, every pinned
figure on the eight pages matches, no math run without a spoken form, none
ambiguous.

## Remaining issues

- **`exponential-and-sinusoidal-forcing` would be two lessons.** The sinusoid
  (a guess that must carry both functions, two equations, the general `A`, `B`
  formula) and the resonant case (a guess the left side annihilates, the factor
  of `t`) are each one hard idea; PLAN §C puts both under one slug with the
  exponential as well. If a reader stalls in this course it will be here, and
  the natural split is "Exponential and Sinusoidal Forcing" / "Resonance: When
  the Forcing Is a Solution", which the URL space does not have. Not done.
- **The sine and cosine rates are borrowed from the next course.** The lesson
  now says so; the PLAN could instead move “Sine, Cosine and Their Rates” (a
  `calckit` lesson with no dependence on second order) to the end of course 1,
  where the exponential's rate already lives. A PLAN change, not a course one.
- **Lowercase `a` is read aloud as "A"** on every page of this course
  (`y′ + a·y = b`, `1 − a·h`), the same letter name as the uppercase `A` of the
  undetermined coefficients in lessons 4 and 6, so "A times e to the power b t,
  A equals 1 over the quantity A plus b" is one letter to a listener. The
  engine's rule is global and the PLAN's notation is fixed; a course written
  for the ear would use `k` for the coefficient. Recorded, not changed.
