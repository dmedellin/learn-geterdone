# Pedagogy assessment — Lines, Functions and Graphs (algebra, course 3)

First assessment, formed from all fourteen lesson dicts in
`content/algebra/c3_functions/` (`part_a.py`, `part_b.py`, `__init__.py`) as they
stood on `pedagogy/openai-algebra` at `b356944b0ac1`. No lesson was sampled:
every body block, method, worked example, quiz explanation, misconception,
completion standard and attached lab configuration was read before the source
was changed. The controls and output contracts of the relevant `grapher`,
`line`, `transform`, `funcops` and `system` modes were checked against the
claims the lesson panels made.

The incoming order was `the-coordinate-plane`, `graphing-a-linear-equation`,
`slope`, `slope-intercept-form`, `point-slope-and-standard-form`,
`parallel-and-perpendicular-lines`, `what-a-function-is`, `function-notation`,
`domain-and-range`, `piecewise-functions`, `transformations-of-graphs`,
`composition-of-functions`, `inverse-functions`,
`linear-inequalities-in-two-variables`. The course declares Courses 1 and 2 as
its prerequisites: elementary real-number expressions, exponents and roots,
absolute value, substitution, one-variable linear equations and inequalities,
and interval notation. Factoring is course 4, rational and radical expressions
are course 5, and quadratic methods and graphs are course 6. That published
order is the prerequisite standard used here.

## What the course teaches well

- **The first six lessons make a line one object seen several ways.**
  `the-coordinate-plane` begins with a graph as a solution set rather than a
  drawing. `graphing-a-linear-equation` derives intercepts from axis
  coordinates and correctly treats two points as enough to determine a line
  but a third as an error detector, not proof that the original equation was
  copied correctly. `slope` explains invariance by similar triangles and keeps
  zero slope separate from undefined slope. `slope-intercept-form` and
  `point-slope-and-standard-form` derive their forms and verify conversions in
  the original equation. `parallel-and-perpendicular-lines` states the scope
  of the product rule and handles the vertical-horizontal pair outside it.
- **The line lessons use exact checking as an intellectual habit.**
  `slope` keeps exact ratios and sanity-checks signs;
  `slope-intercept-form` substitutes into both the original and rearranged
  equations; `point-slope-and-standard-form` reserves the unused point for a
  genuine check; `parallel-and-perpendicular-lines` checks both incidence and
  slope relationship. These checks diagnose different failure modes instead
  of decorating a finished answer.
- **`what-a-function-is` teaches the asymmetry in the definition unusually
  clearly.** It distinguishes many-to-one from one-to-many in equations,
  tables, pairs and graphs, requires a witness input for failure, and derives
  the vertical line test from shared x-coordinates. It also connects the
  vertical line exception back to undefined slope and the impossibility of
  slope-intercept form.
- **Several predictable misconceptions are already named with separating
  examples.** These include swapped coordinate order
  (`the-coordinate-plane`), an intercept found by zeroing the wrong variable
  (`graphing-a-linear-equation`), run over rise and mixed subtraction order
  (`slope`), partial division and sign loss (`slope-intercept-form`), a dropped
  double negative (`point-slope-and-standard-form`), half of the negative-
  reciprocal operation (`parallel-and-perpendicular-lines`), repeated outputs
  mistaken for repeated inputs (`what-a-function-is`), `f(x)` read as a
  product (`function-notation`), a square-root endpoint opened
  (`domain-and-range`), endpoint ownership skipped (`piecewise-functions`), an
  inside shift read forwards (`transformations-of-graphs`), composition read
  left-to-right (`composition-of-functions`), inverse notation read as a
  reciprocal (`inverse-functions`), and `>` read as “above”
  (`linear-inequalities-in-two-variables`).
- **The best quiz explanations diagnose the distractor, not just repeat a
  rule.** The incoming `function-notation`, `domain-and-range`,
  `piecewise-functions`, `transformations-of-graphs`,
  `composition-of-functions`, `inverse-functions`, and
  `linear-inequalities-in-two-variables` items generally identified the exact
  bracket, sign, order, endpoint or input/output confusion behind each choice.
  That is the right feedback model for the whole course.
- **The labs expose their computations rather than asking the picture to carry
  proof.** The line modes derive exact fractions from selected points; the
  function-definition mode names a repeated input; the composition mode shows
  both orders; the transformation mode prints a point map and checks the drawn
  curve; and the inverse mode labels sampled evidence as evidence. The
  distinction between a computation and a visual impression is pedagogically
  sound.

## What fails, or what the course claimed without teaching

### Prerequisites from later courses were used as though already fluent

1. **`function-notation` turned a notation lesson into an unannounced quadratic
   lesson.** Its central worked set solved `x² - 4x + 5 = 5` by factoring,
   rejected `f(x) = 0` with a discriminant, and ended with a difference
   quotient for calculus. Factoring is introduced in course 4; the
   discriminant is course 6 lesson 6; and the difference quotient was neither
   an objective nor retrieval work here. A learner could understand perfectly
   that `f(3)` is an output and still be blocked by algebra the path had not
   taught.
2. **`domain-and-range` hid three later techniques inside a beginner
   objective.** It required factoring `x² - 5x + 6`, cancelling a difference
   of squares in a rational expression, finding a hole's missing range value,
   and completing the square in `x² - 6x + 7`. Those belong to courses 4, 5
   and 6 respectively. The lesson claimed only Courses 1–2 and “the two
   exclusions,” but its range standard required completed-square fluency.
3. **`transformations-of-graphs` assumed graph families before their courses
   taught them.** The parent list included reciprocal and radical functions;
   the complete example solved irrational intercepts of a transformed
   quadratic; and the decisive horizontal example relied on the endpoint and
   domain of `sqrt(2x + 6)`. Radical-function graphs are course 5 and quadratic
   graph structure is course 6. The transformation idea does not require
   either: it can be taught from supplied points.
4. **`composition-of-functions` assessed polynomial multiplication, factoring,
   a discriminant and nested rational simplification.** The first pair expanded
   `(2x + 3)²`, the commentary solved where two quadratics cross with a
   discriminant and factored one, and the hidden-domain example simplified a
   quotient inside a quotient. It then added associativity and decomposition
   for a future chain rule. The stated act was only to compose in the right
   order and carry the domain.
5. **`inverse-functions` made rational-function and shifted-quadratic algebra
   part of the completion standard.** A learner had to collect a variable from
   a rational denominator, find a rational range exclusion, and solve a shifted
   square before courses 5 and 6. The conceptual objective—test one-to-one,
   restrict if needed, swap, solve, and verify—can be fully demonstrated with
   a non-horizontal line and `x²` restricted to one half-axis.

### The worked-example progression stopped before practice

6. **None of the fourteen incoming lessons supplied a genuine faded pass.** A
   complete example was followed by a recognition quiz. The learner was not
   given a new line, relation or function with only the strategic first move
   supplied and the remaining work withheld. This is especially damaging in
   `point-slope-and-standard-form`, `parallel-and-perpendicular-lines`,
   `domain-and-range`, `transformations-of-graphs`,
   `composition-of-functions` and `inverse-functions`, where choosing the
   representation or order is the hard act.
7. **Several quizzes repeated displayed answers.**
   `the-coordinate-plane` repeated `(-3, 6)` and `(0, -3)`;
   `slope` repeated the vertical pair `(5, 2)`, `(5, 9)`;
   `piecewise-functions` asked again for `f(-1)` and which of the two displayed
   joins jumped; `transformations-of-graphs` asked for the exact y-intercept
   and radical transformation from its worked material;
   `composition-of-functions` repeated `(f o g)(2)` and the nested rational
   domain; and `inverse-functions` repeated the rational inverse and shifted
   square. Those items measured recent-answer recognition rather than transfer.
8. The course-level outcome “predict the graph of
   `a*f(b(x-h))+k`” named a broad performance but supplied only verbal move
   labels in the completion standard. It did not require the learner to map a
   landmark, and so did not reveal whether `b` and `h` had been assigned to the
   input coordinate or merely memorised as a slogan.

### Some lesson and lab claims were false

9. **`piecewise-functions` contradicted itself about overlap.** Its key and
   definition said conditions must not overlap and must partition the domain;
   its final body paragraph correctly said an overlap is harmless when all
   applicable formulas agree. Both cannot be the criterion. Conflicting
   outputs violate functionhood; overlapping descriptions that name the same
   point do not.
10. The same lesson said the off-branch result `10` at `x = -1` was “a value
    this function never takes anywhere,” then later proved that the range was
    every real number. In fact the first piece produces `10` at `x = -11`.
    What the failed condition proves is only that `10` is not `f(-1)`.
11. **Five lab panels promised controls the shipped widgets did not have.**
    `the-coordinate-plane` said to drag a point although the lab accepts a text
    list; `what-a-function-is` said to drag a vertical line although the lab
    searches and draws a witness; `function-notation` offered a nonexistent
    solve mode; `inverse-functions` offered nonexistent draggable domain
    markers; and `linear-inequalities-in-two-variables` said to click a test
    point although the systems lab has constraint text fields and no click
    handler. These are not cosmetic discrepancies: each panel assigned a
    retrieval act the learner could not perform.

### The course changed subject twice and overloaded the final function block

12. `linear-inequalities-in-two-variables` depended only on Courses 1–2 and the
    six line lessons, yet it appeared after inverse functions. The incoming
    sequence was lines, then functions, then back to lines for one page. That
    delayed a direct application of line graphing and broke the notation →
    domain → piecewise → transformation → composition → inverse chain.
13. `transformations-of-graphs` introduced four constants, two reflections,
    two scalings, two shifts, factoring the input, transformation order,
    quadratic intercepts and a radical domain on one page. Its useful unifying
    point map existed in the lab but not in the lesson objective or method.
14. `composition-of-functions` and `inverse-functions` each added future-
    calculus material after an already demanding core. Associativity and
    decomposition for the chain rule, and the rational inverse, were correct
    mathematics but not completion acts. They displaced rehearsal of order,
    domain and two-sided verification.

## Where a learner gets stuck

- At the solve section of `function-notation`: a learner who has mastered
  substitution is suddenly expected to factor and use a discriminant that the
  path has scheduled later.
- At the first denominator of `domain-and-range`: the page says the domain
  checklist is mechanical, but the first line requires producing an untaught
  factorisation. The later completed square creates the same failure for range.
- At `piecewise-functions`: the key says all overlap is illegal while the body
  says one overlap is harmless; the learner has no stable criterion to apply.
- At `transformations-of-graphs`: four verbal moves have to be held at once,
  while the reliable coordinate map is visible only after opening the lab.
- At the first independent-looking calculation in
  `composition-of-functions`: expansion skill, not composition order, decides
  whether the learner can continue.
- At the rational example in `inverse-functions`: collecting a variable from a
  denominator and finding a missing range value consume the working memory
  needed for the new one-to-one and swap ideas.
- At each mismatched lab panel: the learner looks for a drag, click or mode
  switch that does not exist, so the intended prediction-check cycle cannot
  even begin.
- At `linear-inequalities-in-two-variables`: the course has spent seven lessons
  building functions and inverses, then asks the learner to retrieve line
  graphing after an unnecessary delay.

## Repairs made in this pass

All fourteen lesson URLs remain unchanged. No lesson was added, removed or
renamed at the URL level, so the membership of the five URL declarations is
unchanged. The teaching order now places
`linear-inequalities-in-two-variables` seventh, immediately after
`parallel-and-perpendicular-lines`; the generated-order tuple in
`tests/test_site_invariants.py` was updated to mirror the content package.

- **Course structure and objectives:** the course now has seven line lessons
  followed by seven function lessons. Outcomes require checked actions:
  justify a simple range, map a known point under a transformation, carry a
  composite domain, and verify a line or restricted-square inverse. Course use
  instructions explicitly require complete example → faded rehearsal → quiz.
- **Worked to faded to independent:** every lesson now ends its worked panel
  with a novel faded rehearsal. Each supplies the first strategic decision and
  withholds the remaining calculation, check and explanation. Repeated quiz
  items were replaced with new coordinates, equations, functions, cut points
  or restrictions, and the feedback names the error represented by every
  distractor.
- **`the-coordinate-plane`:** the lab panel now describes typed points rather
  than dragging. Membership retrieval uses a new equation and axis
  classification uses a new point.
- **`graphing-a-linear-equation`:** a faded line starts from one supplied
  intercept and requires the other, a third point and original-equation checks.
  Intercept feedback now distinguishes every wrong coordinate placement.
- **`slope`:** a signed faded ratio withholds the denominator and requires the
  reverse-order confirmation. The repeated vertical pair was replaced and all
  reciprocal/sign distractors are diagnosed.
- **`slope-intercept-form`:** the faded pass supplies only the isolation line,
  then requires division of every term, a slope step and an original-equation
  check. Distractor feedback identifies a stopped rearrangement separately
  from partial division and sign loss.
- **`point-slope-and-standard-form`:** a new two-point construction moves
  through all three forms and reserves the unused point for verification. The
  independent vertical example no longer repeats the body.
- **`parallel-and-perpendicular-lines`:** a new standard-form line requires both
  companions and both checks. The parallel and vertical quiz items use unseen
  lines and explain the coincident/perpendicular alternatives.
- **`linear-inequalities-in-two-variables`:** moved to lesson 7. Its lab presets
  now contain one inequality each rather than systems of four, and the panel
  accurately requires the learner to choose and substitute a test point off
  the widget. Faded and independent items use new boundaries and negative
  y-coefficients.
- **`what-a-function-is`:** the lab panel now describes its actual point-list or
  solved-for-x witness search. Faded work groups a relation by input and asks
  the learner to repair it; quiz relations are new and preserve the central
  many-to-one misconception.
- **`function-notation`:** factoring, the discriminant and the difference
  quotient were removed. A quadratic-shaped rule is used only for bracketed
  substitution; solving is demonstrated on a linear function using Course 2.
  The lab panel accurately says it evaluates and compares `f(x+1)` with
  `f(x)+1`, not that it has a solve mode.
- **`domain-and-range`:** multi-zero denominators are supplied already factored.
  Ranges use a line, `x²`, absolute value and a simple root, with
  non-negativity or a recovered input as the reason. Cancelled rational holes
  and completing the square were removed from assessed work. The lab presets
  are restricted to prerequisite-safe examples.
- **`piecewise-functions`:** the criterion is now “no conflicting outputs,”
  with exclusive conditions preferred but agreeing overlap allowed. The false
  claim about `10` was corrected to the precise statement that it is not
  `f(-1)`. New retrieval covers endpoint ownership, a computed join, a legal
  gap, harmless overlap and conflicting overlap.
- **`transformations-of-graphs`:** the organising method is now
  `(x0, y0) -> (x0/b + h, ay0 + k)`. Core examples use supplied points on a
  line, absolute value and a cube; future radical, reciprocal and quadratic
  graph knowledge is not assessed. The lab presets foreground those safe
  parents, and a mapped point must be checked in the transformed rule.
- **`composition-of-functions`:** the order example now uses two lines. The
  hidden-domain example is `(sqrt(x))² = x` with domain `[0, inf)`, so the
  restriction survives simplification without nested rational algebra.
  Associativity and chain-rule decomposition were removed from completion
  work; new practice builds and checks both orders.
- **`inverse-functions`:** assessed inverses are a non-horizontal line and
  `x²` on one half-axis. Both symbolic compositions are displayed and required.
  The rational inverse and shifted quadratic were removed, and the lab panel
  accurately describes its fixed restriction display rather than draggable
  markers.

No shared lab implementation or arithmetic checker was changed. Course-local
lab presets and panel copy changed, but no new arithmetic operation or shipped
formula was introduced. The new-arithmetic mutation requirement therefore does
not apply to this pass.
