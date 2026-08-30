# Pedagogy assessment — Quadratics and Complex Numbers (algebra, course 6)

First assessment, formed from all fourteen lesson dicts in
`content/algebra/c6_quadratics/` (`part_a.py`, `part_b.py`, `__init__.py`) as
they stood on `pedagogy/openai-algebra` at `bb34d25`. No lesson was sampled:
every body block, method, worked example, quiz explanation, misconception,
completion standard and attached lab configuration was read before the source
was changed. The shared quadratic lab was also read in full, together with the
complex and inequality modes this course uses, so claims about what a learner
sees are based on the rendered interaction rather than its panel copy alone.

The published order was and remains
`quadratic-equations-and-the-zero-product-property`, `solving-by-factoring`,
`the-square-root-property`, `completing-the-square`,
`the-quadratic-formula`, `the-discriminant`, `complex-numbers`,
`operations-with-complex-numbers`, `complex-roots-of-quadratics`,
`graphs-of-quadratic-functions`, `vertex-form-and-the-axis-of-symmetry`,
`maximum-and-minimum-problems`, `quadratic-inequalities`, and
`equations-reducible-to-quadratic-form`.

The prerequisite trail through courses 1–5 is sound. Course 1 supplies signed
arithmetic, exponents, principal roots and exact radicals; course 2 supplies
equation solving, inequality reversal, absolute-value equations and interval
notation; course 3 supplies functions, domain, graph transformations and the
coordinate plane; course 4 supplies all factoring methods, multiplicity and
polynomial graphs; course 5 supplies radical simplification, conjugates,
domain restrictions and sign analysis. No earlier course needs to change for
this course to work.

## What the course teaches well

- **The solving sequence is principled rather than mnemonic.**
  `quadratic-equations-and-the-zero-product-property` proves the licence behind
  factor splitting and explicitly rejects division by an unknown.
  `solving-by-factoring` retrieves Course 4 rather than reteaching it.
  `the-square-root-property` separates the principal radical from the two
  solutions of an equation, `completing-the-square` makes the needed constant
  from `(x + p)²`, and `the-quadratic-formula` derives rather than merely states
  the formula. `the-discriminant` then names the quantity that the derivation
  naturally produced.
- **The complex-number extension answers a mathematical need.**
  `complex-numbers` locates the new system in the earlier history of number
  extensions and defines equality by real and imaginary parts.
  `operations-with-complex-numbers` derives multiplication and division from
  distribution, `i² = -1` and the conjugate product.
  `complex-roots-of-quadratics` returns to the negative-discriminant equations
  left open earlier and proves the conjugate-pair condition with its necessary
  real-coefficient hypothesis.
- **The graph work is tied back to the algebra.**
  `graphs-of-quadratic-functions` connects real roots to x-intercepts and proves
  symmetry about `x = -b/(2a)`.
  `vertex-form-and-the-axis-of-symmetry` reuses completing the square and proves
  the extreme-value statement from the sign of a square.
  `maximum-and-minimum-problems` spends that theorem on models, while
  `quadratic-inequalities` turns the same graph into a sign chart. The course
  therefore presents roots, intercepts, symmetry, extrema and signs as views of
  one object rather than unrelated procedures.
- **Predictable misconceptions are unusually visible.**
  The course confronts splitting a non-zero product
  (`quadratic-equations-and-the-zero-product-property`), treating failure to
  factor as absence of roots (`solving-by-factoring`), losing `±` and writing
  `sqrt(9) = ±3` (`the-square-root-property`), completing before dividing by
  `a` (`completing-the-square`), mishandling a signed `b`
  (`the-quadratic-formula`), reading `D = 0` as no roots
  (`the-discriminant`), calling `bi` the imaginary part (`complex-numbers`),
  applying radical product laws to negative radicands
  (`operations-with-complex-numbers`), dropping the denominator from only the
  imaginary term (`complex-roots-of-quadratics`), reading a vertex bracket with
  the wrong sign (`vertex-form-and-the-axis-of-symmetry`), confusing where an
  optimum occurs with its value (`maximum-and-minimum-problems`), cancelling an
  unknown in an inequality (`quadratic-inequalities`), and stopping at the
  temporary variable (`equations-reducible-to-quadratic-form`).
- **Most quiz feedback is already diagnostic.** Wrong choices generally encode
  a named sign, reciprocal, omitted-root, endpoint, coefficient or distribution
  error, and the explanation identifies that error rather than saying only that
  another choice is correct. The repair did not replace this strength.
- **The lab architecture supports exact comparison.** The quadratic lab
  independently searches for a rational factorisation, applies the square-root
  property when its hypothesis holds, completes the square and uses the
  formula. It draws the parabola from evaluated function values and marks exact
  roots and vertex values from the same coefficient input. The complex and
  inequality labs likewise keep the number-system and interval distinctions
  visible.

## What failed, or what the course claimed without teaching

### Performance was inferred from complete demonstrations

1. **None of the fourteen incoming lessons had a faded rehearsal.** Every page
   moved from a complete worked solution to multiple-choice recognition. A
   learner never received the first strategic decision on a novel problem and
   then had to execute the remaining algebra and check. The gap was costly in
   `completing-the-square`, `the-quadratic-formula`,
   `operations-with-complex-numbers`, `maximum-and-minimum-problems`,
   `quadratic-inequalities` and `equations-reducible-to-quadratic-form`, where
   the stated act is a multi-step performance.
2. **The course promised deliberate method choice without independently
   assessing it.** The course home says to choose factoring, the square-root
   property or the formula deliberately, but the quizzes in
   `solving-by-factoring`, `the-square-root-property`,
   `completing-the-square` and `the-quadratic-formula` announce their method by
   the page on which they appear. `the-discriminant` classified roots but did
   not require a mixed decision among all four routes.
3. **The syllabus lines described topics more often than observable acts.**
   “The parabola, its direction, and its intercepts” in
   `graphs-of-quadratic-functions` and “Arithmetic, and the conjugate that makes
   division work” in `operations-with-complex-numbers` did not say what a
   learner should be able to produce. The same problem appeared in all fourteen
   one-line objectives, even where the completion standard later supplied a
   measurable act.

### The interaction crossed the prerequisite boundary

4. **Three pre-complex lessons displayed complex roots before defining `i`.**
   The prose in `the-square-root-property` and `the-discriminant` foreshadowed
   exact answers using `i`. More seriously, the shared quadratic lab always
   computed and printed a conjugate pair for a negative discriminant, so the
   negative presets in `the-square-root-property`, `the-quadratic-formula` and
   `the-discriminant` used an unexplained symbol even though their own panels
   promised to stop at “no real solution.” `complex-numbers` is the first place
   where that symbol has a definition; the interaction had silently reordered
   the prerequisite.
5. **The course footer misdescribed the lab.** It claimed that every quadratic
   was solved by all four methods and that four answers were compared. The lab
   correctly reports that factoring is unavailable without rational roots and
   that the square-root property is unavailable when `b` is non-zero. The two
   universal methods agree; four answers do not always exist.

### Four mathematical descriptions needed correction or scope

6. **`completing-the-square` said the completing constant is always positive.**
   It is `(b/2)²`, hence non-negative, and it is zero when `b = 0`. The page had
   just said that `b` may be zero earlier in the course, so the universal claim
   contradicted a legitimate quadratic shape.
7. **`vertex-form-and-the-axis-of-symmetry` said a function definition was not
   an equation with two sides.** It is an equation, and balance operations are
   legal. The pedagogically relevant distinction is narrower: when rewriting
   the rule while keeping `y` isolated, the expression on the right must retain
   the same value for every input. Add-and-subtract does that.
8. **`maximum-and-minimum-problems` overgeneralised the endpoint rule.** It said
   an unavailable vertex puts the optimum at an endpoint, and its method said
   the nearer endpoint. That is valid for an available endpoint of a closed
   interval and adapts to nearby permitted integers. It is not valid when the
   relevant endpoint is excluded: a bound may be approached without any
   maximum or minimum being attained. Its proof also stated both missing global
   extrema but explicitly justified only the upward parabola's lack of a
   maximum.
9. **`equations-reducible-to-quadratic-form` defined the general pattern too
   narrowly.** It required one exponent to be twice another, then later used
   `u = x² - 3` on a repeated bracket. The real definition is an expression
   `f(x)` appearing to the first and second powers; doubled exponents are one
   common recognition cue.

## Where a learner gets stuck

- After the polished demonstrations in
  `quadratic-equations-and-the-zero-product-property` through
  `the-quadratic-formula`: the author has made every strategic choice, so the
  learner can recognise a finished line without being able to start a novel
  equation.
- At `the-discriminant`: a positive perfect square suggests factoring, but
  shape may make the square-root property still shorter, and a near-square may
  reward completing the square. The incoming page did not make the learner
  compare those cues.
- At a negative preset in the pre-complex quadratic lab: the prose says “stop,”
  while the interaction used `i` and a conjugate pair. A learner could not tell
  whether “no real solution” was complete or merely avoidance.
- In `operations-with-complex-numbers`: addition and multiplication transfer
  readily, but division adds conjugation, two expansions and standard-form
  reduction at once. Without a partially supported quotient there was no bridge
  from watching to performing.
- In `graphs-of-quadratic-functions` and
  `vertex-form-and-the-axis-of-symmetry`: several features agree only if signs,
  roots and `f(h)` are all correct. The incoming work showed that agreement but
  did not ask the learner to generate it on a new quadratic.
- In `maximum-and-minimum-problems`: the vertex calculation is easier than
  naming the variable, eliminating the second quantity, stating the domain and
  answering with units. Multiple-choice retrieval under-sampled that modelling
  chain.
- In `quadratic-inequalities`: finding roots and deciding endpoints can collapse
  into one guess; a faded sign table is needed to keep interval signs separate
  from strict-versus-inclusive notation.
- In `equations-reducible-to-quadratic-form`: the exponent-only test conflicted
  with the repeated-bracket example, so a learner had no single recognition
  rule that covered both.

## Repairs made in this pass

All fourteen lesson URLs and their order remain unchanged. No lesson was added,
removed, renamed or moved, so none of the five URL declarations changed.

- **Observable objectives:** every lesson's syllabus line now names a visible
  act: classify and split, choose factoring, isolate a square, complete a square,
  derive and apply the formula, classify and choose a method, write complex
  standard form, compute and divide, solve a conjugate pair, recover graph
  features, convert to vertex form, build and constrain a model, justify an
  interval set, or substitute and return to `x`.
- **Worked → faded → independent:** every worked panel now ends with a novel
  faded rehearsal. Each supplies the first structural decision and leaves the
  algebra, exact simplification and diagnostic check to the learner. The course
  directions explicitly tell the learner to cover the complete example, do the
  faded task, then use the quiz for independent retrieval.
- **Mixed method selection:** `the-discriminant` now ends its worked panel with
  four differently shaped equations and adds a fourth independent quiz item
  requiring the shortest justified method for another four. Its feedback names
  the integer-factor, missing-linear-term, near-square and negative-discriminant
  cues and diagnoses universality-versus-efficiency.
- **Prerequisite repair:** the pre-complex prose no longer prints unexplained
  complex answers. The quadratic lab now suppresses complex-form output in the
  lesson 3–6 modes and reports “no real solution” until `complex-numbers` has
  defined the larger system. Later graph, vertex, optimisation and reducible
  modes may retrieve the conjugate pair because they occur after that lesson.
- **Claim repair:** the course footer now says the lab tests four methods,
  identifies inapplicable ones and compares the two universal exact methods.
  It no longer promises four answers where the mathematics does not provide
  them.
- **Correctness and scope repair:** `completing-the-square` says non-negative;
  `vertex-form-and-the-axis-of-symmetry` distinguishes legal equation balancing
  from preserving an isolated function rule; `maximum-and-minimum-problems`
  handles closed, discrete and open domain boundaries and completes the
  unboundedness proof; `equations-reducible-to-quadratic-form` uses the general
  `f(x)`/`[f(x)]²` pattern.

## Residual boundary

The course remains an algebra course, not a course in complex geometry or
calculus. It does not add polar complex form, De Moivre's theorem, complex
inequalities, general conics, calculus-based optimisation, or a general quartic
formula. Quadratic inequalities are solved over the reals, optimisation models
state their permitted real or discrete domains, and the final substitution
lesson distinguishes real return values from additional complex ones. Those
boundaries are now explicit and do not obstruct any stated outcome.
