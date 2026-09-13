# Pedagogy assessment — Linear Equations and Inequalities (algebra, course 2)

First assessment, formed from all thirteen lesson dicts in
`content/algebra/c2_equations/` (`part_a.py`, `part_b.py`, `__init__.py`) and all
thirteen lab modes they attach in
`scripts/mathpath/labs/algebra_equations.py`, as they stood on
`pedagogy/openai-algebra` at `a7c9b9892311`. No lesson was sampled: every body
block, method, worked example, quiz explanation, misconception, completion
standard and attached lab panel was read before the source was changed.

The incoming order was `what-it-means-to-solve-an-equation`,
`one-and-two-step-equations`, `variables-on-both-sides`,
`equations-with-fractions`, `literal-equations-and-formulas`,
`identities-and-contradictions`, `ratio-proportion-and-percent`,
`modelling-with-linear-equations`, `linear-inequalities`,
`compound-inequalities`, `absolute-value-equations`,
`absolute-value-inequalities`, `interval-and-set-builder-notation`. Course 1
now supplies the declared prerequisites in a defensible order: variables and
terms precede properties, and distribution, collection, exact fractions,
absolute value and translation all precede their use here.

## What the course teaches well

- **It makes equivalence the reason a procedure works.**
  `what-it-means-to-solve-an-equation` defines a solution by substitution and
  an equivalent equation by an unchanged solution set.
  `one-and-two-step-equations` and `variables-on-both-sides` name the operation
  applied to both sides instead of teaching terms to “cross” an equals sign.
  `equations-with-fractions` derives clearing denominators from multiplication
  by a nonzero constant, and `ratio-proportion-and-percent` similarly derives
  cross products rather than presenting a diagonal trick.
- **Exact checking is a course-wide intellectual habit.**
  `what-it-means-to-solve-an-equation` separates `0.333` from `1/3` by testing
  both in `3x = 1`; `one-and-two-step-equations` keeps fractional answers exact;
  `literal-equations-and-formulas` distinguishes a numerical spot check from
  the algebraic argument; `linear-inequalities` tests a boundary, an interior
  value and an exterior value. The equation lab checks the expression trees as
  typed rather than checking a simplified surrogate.
- **The three linear-equation outcomes are explained rather than named.**
  `identities-and-contradictions` reduces every linear equation to `px = q`
  and uses the cases `p != 0`, `p = q = 0`, and `p = 0 != q` to justify why
  the solution set has one, all or no real numbers. It explicitly separates
  `x = 0`, `0 = 0` and `0 = 5`, a misconception that otherwise survives into
  systems of equations.
- **The inequality reversal has a reason and a diagnostic.**
  `linear-inequalities` proves the negative-multiplier rule, distinguishes it
  from subtracting a negative number, prohibits division by an expression of
  unknown sign, and asks for values from both sides of the boundary.
  `compound-inequalities` then builds *and* as intersection and inclusive *or*
  as union before absolute-value inequalities need those connectors.
- **Absolute value is consistently read as distance.**
  `absolute-value-equations` derives its two cases from the two points at a
  given distance and treats a variable right side by checking candidates in
  the original. `absolute-value-inequalities` gets the band or two rays from
  the same picture, so *and* and *or* are consequences rather than a mnemonic.
- **The predictable errors are unusually specific.**
  The course names multiplying one side only (`one-and-two-step-equations`),
  distributing a minus over only one term (`variables-on-both-sides`), leaving
  a whole term untouched by the LCD (`equations-with-fractions`), cancelling a
  term as though it were a factor (`literal-equations-and-formulas`), pairing
  unlike units (`ratio-proportion-and-percent`), accepting an impossible model
  (`modelling-with-linear-equations`), reading mathematical *or* as exclusive
  (`compound-inequalities`), splitting before the bars are isolated
  (`absolute-value-equations`, `absolute-value-inequalities`), and treating
  infinity or zero as a set member by accident
  (`interval-and-set-builder-notation`). Quiz explanations generally identify
  the line of reasoning behind each distractor.

## What fails, or what the course claimed without teaching

### The worked-example progression stopped after the worked example

1. **None of the thirteen incoming lessons contained a genuine faded pass.**
   A complete derivation was followed immediately by a three-option or
   four-option recognition question. The learner was never handed a new
   statement with the first strategic decision supplied and the remaining
   steps withheld. This is most damaging in `variables-on-both-sides`,
   `literal-equations-and-formulas`, `modelling-with-linear-equations` and
   `absolute-value-inequalities`, where the difficult act is choosing a
   representation or a case structure rather than performing arithmetic.
2. **Several quizzes simply asked for a displayed answer again.**
   `one-and-two-step-equations` repeated `7 - 2x = 19` and the exact
   `2(x + 3) = 14` bracket trap; `variables-on-both-sides` repeated
   `3x - 7 = 8x + 3` and the simplified equation whose solution was `0`;
   `equations-with-fractions` repeated the complete
   `(x + 1)/3 - (x - 2)/4 = 1` example;
   `literal-equations-and-formulas` repeated `S = C + rC`;
   `modelling-with-linear-equations` repeated the consecutive-number and
   impossible-mixture examples; `compound-inequalities` repeated both the
   whole-line union and the one-point intersection; and
   `absolute-value-equations` repeated the two-candidate rejection from its
   worked panel. Those items measure short-term answer recognition, not use of
   the method on a new statement.
3. The completion standards were observable in grammar but not operational in
   practice. “Given any equation” in `equations-with-fractions`, “isolate any
   letter” in `literal-equations-and-formulas`, and “for any linear inequality”
   in `linear-inequalities` named broad performances without supplying a novel
   item on which to demonstrate them.

### Two labs violated the course's own prerequisite order

4. **The `check` lab contradicted `what-it-means-to-solve-an-equation`.** The
   panel repeatedly said that it “never solves anything,” but its implementation
   solved every linear statement internally, printed the unique solution after
   the candidate verdict, and marked the crossing point on a graph. A learner
   asked only to decide whether one value passes was handed the answer to a
   different task, and was shown function graphs before course 3 teaches them.
5. **The inequality labs taught notation by output before lesson 13 taught it
   by instruction.** `linear-inequalities`, `compound-inequalities`, and
   `absolute-value-inequalities` said that interval and set-builder notation
   would arrive in `interval-and-set-builder-notation`, while their panels
   already printed every answer in both forms and put interval notation in the
   headline KPI. The result looked like review of a prerequisite the path had
   never supplied.

### Local prerequisite and cognitive-load gaps

6. **`equations-with-fractions` defined an LCD but did not teach how to find
   one.** The learner was shown that the LCD of 2 and 3 is 6 and of 4 and 6 is
   12, then told to take the least common multiple for any list. Neither the
   course prerequisite (“fractions, negatives, and long division”) nor course 1
   guarantees a least-common-multiple procedure. The first line of the method
   therefore depended on an unstated skill.
7. **`literal-equations-and-formulas` claimed the target could appear twice but
   demonstrated only two appearances already on the same side.** Factoring
   `S = C + rC` does not teach the extra collecting decision in
   `ax + b = cx + d`. The method mentioned gathering target terms on one side,
   but no worked line did it. Its claim to isolate “any letter” also omitted
   “linear in the target,” despite correctly rejecting `A = s^2` later.
   Finally, saying that `b = 0` in `A = bh/2` merely describes “no triangle”
   hid the algebraic cases: when `b = 0`, the original is true for every `h` if
   `A = 0` and for no `h` otherwise.
8. **`ratio-proportion-and-percent` carried too many endpoints of the idea at
   once.** It taught unit order, proved cross products, introduced excluded
   values from variable denominators, manufactured an extraneous candidate,
   taught all three percent-question forms, taught percent change, and added
   successive percent changes. The attached lab went further and accepted
   proportions whose cross product is quadratic. Rational equations and their
   domain machinery belong to course 5; they were consuming working memory on
   the page where a beginner still needed to decide which quantity was the
   whole.
9. **`modelling-with-linear-equations` moved from simple plan and consecutive
   number models to a concentration model without teaching conservation of the
   dissolved quantity as a modelling principle.** Its worked panel was the
   hardest context on the page and then immediately varied it to an impossible
   target. The lab prompt told the learner to run the two mixture presets rather
   than first retrieving the unknown, common quantity and equation in a simpler
   situation.
10. **The zero boundary in `absolute-value-inequalities` was incomplete.** The
    method named `|X| <= 0` and `|X| > 0`, but did not complete the four-way
    classification with `|X| < 0` (empty) and `|X| >= 0` (all reals). A learner
    following “look at the right side” still needed to improvise two of the four
    relations.

### The final notation outcome was under-assessed

11. `interval-and-set-builder-notation` promised conversion among inequality,
    interval, set-builder and number-line forms “including for a set in two
    pieces.” Its lab could construct only one interval, and its three quiz items
    assessed one bounded interval, a bracket at infinity and `(4, 4)`. There was
    no retrieval item for a union, none for set-builder notation, and none that
    distinguished a real domain from an integer domain. The lesson explained
    those acts but did not find out whether the learner could perform them.
12. The course-level promise “solve any linear statement” was broader than the
    course. It does not solve systems, nonlinear statements, rational equations
    in general, or inequalities with variable divisors. The defensible outcome
    is one-variable real linear equations and inequalities in the forms this
    course teaches, with literal formulas restricted to being linear in the
    target.

## Where a learner gets stuck

- At the first lab in `what-it-means-to-solve-an-equation`: the page asks for a
  candidate verdict, while the panel reveals the actual solution and a graph
  the learner has not yet learned to read.
- At the first unsupplied LCD in `equations-with-fractions`: the procedure says
  “take the least common multiple,” but the course has never shown how to
  produce it for 6, 8 and 12 rather than recognise it for 2 and 3.
- At a target on both sides in `literal-equations-and-formulas`: all displayed
  target repetitions factor in place, so the collecting step exists only in
  the prose.
- At `ratio-proportion-and-percent`: the learner is simultaneously tracking
  unit orientation, a domain exclusion, an extraneous candidate and which
  amount is the percent base. A correct but advanced rational-equation warning
  displaces the stated beginner act.
- At the mixture in `modelling-with-linear-equations`: “pure substance counted
  two ways” appears as the equation source without a prior faded model asking
  the learner to identify what is conserved.
- At the output panel in `linear-inequalities`: interval and set-builder forms
  look like assumed knowledge four lessons before their notation lesson.
- At `interval-and-set-builder-notation`: a learner can answer all three
  incoming quiz questions without ever writing or reading a union or a
  set-builder condition, yet the course then declares that four-way conversion
  complete.

## Repairs made in this pass

All thirteen lesson URLs and their order remain unchanged. No page was added,
removed or renamed, so none of the five URL declarations changes.

- **Course scope and use:** course outcomes now say one-variable real linear
  equations and inequalities rather than “any linear statement,” restrict
  literal rearrangement to formulas linear in the target, and require a learner
  to use a worked example, a faded pass and a novel independent item rather
  than reading the page straight through.
- **Worked to faded to independent:** every lesson now supplies a novel faded
  rehearsal after its complete example, with the strategic first move given
  and later work withheld. Completion standards name a concrete new item, and
  repeated quiz calculations were replaced by transfer items while preserving
  distractor-specific feedback.
- **`what-it-means-to-solve-an-equation`:** the quiz now tests candidate
  substitution rather than asking the learner to solve before that procedure
  has been taught. Its lab no longer computes or reveals the unique solution
  and no longer displays the course-3 graph; it reports only what the chosen
  candidate establishes.
- **`one-and-two-step-equations`:** the repeated negative-coefficient and
  bracket questions are replaced by new equations, and the faded pass withholds
  the final division and original-equation check.
- **`variables-on-both-sides`:** a new signed equation requires a deliberate
  choice of collecting side, the quiz no longer quotes the two displayed
  examples, and the independent item includes brackets.
- **`equations-with-fractions`:** listing multiples and prime-factor powers now
  give two usable ways to produce an LCD. A new multi-term fraction equation is
  faded after the clearing line, and independent work includes exact decimals.
- **`literal-equations-and-formulas`:** the page now demonstrates a target on
  opposite sides, states the `a - c != 0` condition, and reads the `b = 0`
  triangle formula algebraically rather than hiding the identity/contradiction
  cases behind physical language. New practice is explicitly linear in the
  target.
- **`identities-and-contradictions`:** the lab asks for a classification before
  revealing one, and faded and independent items force the learner to simplify
  before deciding rather than classify by appearance.
- **`ratio-proportion-and-percent`:** variable-denominator cancellation and
  quadratic cross products are fenced as course-5 previews, not completion
  work. The assessable line is now consistent ratio order, constant-denominator
  proportions and identifying the percent whole; new questions retrieve each.
- **`modelling-with-linear-equations`:** the lab starts with plans and
  consecutive numbers, while mixture presets are labelled as a conservation
  challenge. The faded pass supplies an unknown and expressions but withholds
  the equality, solve and situational judgement; new quiz contexts replace the
  displayed consecutive-number and mixture answers.
- **`linear-inequalities`, `compound-inequalities`, and
  `absolute-value-inequalities`:** their labs now report answers as inequalities,
  words and number lines only. Interval and set-builder notation are withheld
  until their lesson. Each page asks for a prediction before the panel reveals
  a reversal, intersection/union, or band/ray result, then supplies a faded
  transfer item.
- **`absolute-value-equations`:** the repeated all-extraneous quiz item is
  replaced by a new one-survivor case, and faded practice requires isolating the
  bars before completing both branches.
- **`absolute-value-inequalities`:** the zero right-hand side is now classified
  for all four relations, and the independent item requires both an outer
  negative reversal and the correct connector.
- **`interval-and-set-builder-notation`:** the faded pass converts a two-piece
  set, and retrieval now includes a union, a set-builder condition and the
  distinction between real and integer domains. The lab is accurately framed
  as a one-interval rehearsal rather than evidence for the whole outcome.

No new arithmetic operation or formula was added to the shipped lab
implementation. The lab changes remove premature output and solution leakage;
the exact-arithmetic core and all computed solution sets are unchanged, so the
new-arithmetic mutation requirement does not apply.
