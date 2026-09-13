# Pedagogical assessment: Systems and Matrices

## Scope and method

This assessment covers all ten source lessons in
`content/algebra/c8_systems/`, front to back: every concept, body block,
method, worked example, quiz explanation, misconception, completion standard
and lab brief. It also checks the prerequisites the course actually uses
against the preceding Algebra courses. The generated pages under `site/` were
not treated as source.

## What already worked

- **The central sequence is coherent.**
  `systems-of-two-linear-equations` first defines a solution and the three
  possible solution sets. `solving-by-substitution` and
  `solving-by-elimination` then reduce two unknowns to one;
  `systems-in-three-variables` repeats elimination twice;
  `matrices-and-row-operations` deletes only the variable labels; and
  `gaussian-elimination` turns those same reversible moves into an algorithm.
  The matrix notation therefore arrives after the algebra it abbreviates.
- **The course distinguishes classification from computation.**
  `systems-of-two-linear-equations`, `solving-by-substitution`,
  `solving-by-elimination` and `gaussian-elimination` all preserve the
  difference between one solution, none and infinitely many. A contradiction
  is treated as a conclusion rather than a failed method, while a dependent
  answer is written as a line or parameterised family rather than merely
  labelled “infinitely many.”
- **Reversibility is used as the reason for each method.**
  `solving-by-substitution` keeps the isolated equation;
  `solving-by-elimination` excludes multiplication by zero and changing both
  equations simultaneously; and `matrices-and-row-operations` names the
  inverse of every legal row operation. The learner is not asked to trust a
  collection of unexplained moves.
- **Exactness and verification are unusually strong.**
  `systems-in-three-variables`, `gaussian-elimination`,
  `determinants-and-cramers-rule` and `inverse-matrices` keep fractions exact.
  System answers are checked in the original equations, not in rows produced
  by the learner's own arithmetic. `inverse-matrices` verifies an inverse by
  multiplication rather than by resemblance to a memorised formula.
- **The labs support the intended decisions rather than merely drawing.**
  The system modes let the learner change the isolation or eliminated
  variable and compare the traces in `solving-by-substitution` and
  `solving-by-elimination`. The matrix modes independently compare rank,
  determinant, Cramer's rule, row reduction and inverse products for
  `gaussian-elimination`, `determinants-and-cramers-rule` and
  `inverse-matrices`. The `systems-of-inequalities-and-linear-programming`
  mode recomputes feasibility and objective behaviour from the constraints.
- **Misconceptions are concrete and diagnostic.**
  `systems-of-two-linear-equations` separates a line of solutions from the
  whole plane; `solving-by-substitution` catches the missing bracket;
  `solving-by-elimination` catches an unscaled constant;
  `systems-in-three-variables` catches elimination of different variables;
  `matrices-and-row-operations` catches column swaps and omitted zeros;
  `gaussian-elimination` separates a free variable from a zero variable;
  `matrix-arithmetic` rejects entrywise multiplication and factor swapping;
  `determinants-and-cramers-rule` refuses to infer dependence from `D = 0`;
  `inverse-matrices` distinguishes swapping from negating entries; and
  `systems-of-inequalities-and-linear-programming` rejects infeasible boundary
  crossings before they can win the objective comparison. Quiz explanations
  generally identify the wrong operation represented by each distractor.

## What failed, or what the course claimed without teaching

### The course home overclaimed the performance

1. The incoming outcome “Solve a system three ways” included graphing, but
   `systems-of-two-linear-equations` used a graph to classify and estimate an
   intersection, not to produce the exact solution promised alongside
   substitution and elimination. The body correctly warned that a drawing
   cannot distinguish `5/3` from `1.7`; the course home contradicted that
   warning.
2. The incoming overview said the learner could solve a system “of any size by
   hand.” The worked instruction reaches two- and three-variable systems and a
   general row-reduction procedure, but it does not establish performance on
   arbitrary dimensions. It also said lesson 10 “applies” the matrix machinery,
   although `systems-of-inequalities-and-linear-programming` applies
   two-variable elimination to boundary pairs and does not use matrices.
3. The determinant outcome said “compute it two ways.”
   `determinants-and-cramers-rule` teaches the `2 × 2` formula and cofactor
   expansion for `3 × 3`; its lab independently checks a determinant by row
   reduction, but the lesson does not teach the determinant effects of row
   operations as a second learner method. The outcome measured a lab
   cross-check as though it were an instructed procedure.

### Worked examples stopped before transfer

4. All ten incoming lessons moved from a fully completed worked example
   directly to multiple choice. That gap was most costly in
   `solving-by-substitution`, `solving-by-elimination`,
   `systems-in-three-variables`, `gaussian-elimination`,
   `determinants-and-cramers-rule`, `inverse-matrices` and
   `systems-of-inequalities-and-linear-programming`, where the completion
   standard is a multi-step production rather than recognition of a rule.
5. Every incoming syllabus line described content rather than observable
   performance: “Two lines,” “replacing one unknown,” “three planes,” “the same
   elimination,” and “a feasible region” did not say what the learner had to
   classify, choose, construct, compute or verify.
6. The incoming quizzes already supplied useful error-specific feedback, but
   they could not bridge a complete demonstration to a fresh, multi-line
   solution. `matrix-arithmetic` went further in the wrong direction: its final
   retrieval item tested the zero-product exception after the lesson had
   already accumulated several facts beyond the row-column product that later
   lessons need.

### Prerequisite order and cognitive load drifted

7. `systems-of-two-linear-equations` placed
   `a₁b₂ − a₂b₁ ≠ 0` in the opening key and used it as a coefficient test seven
   lessons before `determinants-and-cramers-rule` defined the determinant. The
   first lesson already had a complete classification through slopes and
   proportional standard-form equations; the unexplained expression was a
   second route with no immediate use.
8. `matrix-arithmetic` introduced addition, scalar multiplication, matrix
   multiplication, associativity, two distributive laws, the identity matrix,
   failure of the zero-product property and failure of cancellation in one
   lesson. Only product existence, shape, row-column computation and order are
   prerequisites for `inverse-matrices`. The extra laws competed with the one
   operation learners predictably confuse with entrywise multiplication.
9. The remaining prerequisite chain is sound. Exact fraction arithmetic comes
   from Course 1, linear equations and identities from Course 2, and line forms,
   graphing and half-planes from Course 3. In particular,
   `systems-of-inequalities-and-linear-programming` does not introduce shading
   before the path has taught `linear-inequalities-in-two-variables`. No repair
   to an earlier signed-off course was required.

### The unbounded linear-programming claim was false as stated

10. `systems-of-inequalities-and-linear-programming` omitted closedness from
    the corner theorem even though its later strict-inequality warning explains
    that an excluded boundary can prevent an optimum from being attained. It
    also said that when an optimum exists on an unbounded feasible region, it
    is still at a corner. An
    unbounded strip can have a maximum along an entire boundary line and have
    no corners at all. The lesson's own example happened to have corners, but
    it used the bounded corner theorem to justify a conclusion outside that
    theorem's scope. This taught the wrong proof even where the numerical
    answer was right.

## Where learners get stuck

- In `systems-of-two-linear-equations`, a vertical line blocks the advertised
  slope-intercept comparison. Without a standard-form alternative, a learner
  can know the three cases and still have no classification procedure for
  `x = 3`.
- In `solving-by-substitution`, the isolated expression is liable to return to
  the equation that produced it, yielding an uninformative identity. A negative
  coefficient outside the substituted bracket is the next failure point.
- In `solving-by-elimination`, learners choose multipliers while already doing
  arithmetic, omit the constant from a scaling, or interpret `0 = 0` as a
  numerical solution instead of a lost restriction.
- In `systems-in-three-variables`, the first elimination feels successful even
  when the second removes a different variable. The error becomes visible only
  after the two new equations still involve three unknowns between them.
- In `matrices-and-row-operations`, meaning has moved from variable labels to
  positions. An omitted zero or untouched constant column makes a valid row
  operation act on the wrong system with no visual warning.
- In `gaussian-elimination`, exact fractions increase bookkeeping load just as
  pivot, free-variable and contradiction decisions arrive. A learner who sets
  a non-pivot variable to zero can report one correct point while failing to
  describe the solution set.
- In `matrix-arithmetic`, matching inner dimensions and producing the outer
  dimensions are separate decisions. Even after both are right, a learner may
  pair a row with the wrong column or compute `BA` when asked for `AB`.
- In `determinants-and-cramers-rule`, the alternating sign in a `3 × 3`
  expansion and the replaced column in `Dx` or `Dy` are independent sources of
  error. A zero denominator must trigger a method change, not a conclusion
  about which non-unique case holds.
- In `inverse-matrices`, “swap the diagonal, negate the off-diagonal” is easily
  blended into one incorrect action, and the order of multiplication matters
  again when `A⁻¹` is applied to `AX = B`.
- In `systems-of-inequalities-and-linear-programming`, a boundary crossing can
  produce the largest objective value precisely because it violates another
  constraint. On an unbounded region, a finite corner table can look complete
  while a feasible ray continues beyond it.

## Repairs made in this pass

All ten lesson URLs and their order remain unchanged. No lesson was added,
removed or moved, and no slug changed, so none of the five URL declarations
changed. The source title of `matrix-arithmetic` is now **Matrix Products**;
its stable slug remains `matrix-arithmetic`.

- **Truthful, observable outcomes:** the course home now distinguishes graphing
  for classification and estimation from exact algebraic methods, scopes the
  practised systems to two and three variables, describes the actual role of
  lesson 10, and names optimisation as a measured outcome. Every lesson's
  syllabus line now begins with an observable act: classify, choose, plan,
  translate, reduce, decide, compute, test or build.
- **Worked → faded → independent:** every worked panel now ends with one novel
  faded rehearsal. The first classification, isolation, multiplier, pair of
  eliminations, matrix row, pivot decision, product shape, determinant decision,
  invertibility decision or corner set is supplied. The learner must finish
  the arithmetic, describe the whole solution set where needed and perform the
  original-equation, identity-product or feasibility check. The existing quiz
  then supplies independent retrieval with diagnostic feedback.
- **Prerequisite repair:** `systems-of-two-linear-equations` no longer opens
  with an unexplained determinant expression. It handles vertical lines through
  proportional standard-form coefficients and leaves the numerical compression
  of that comparison to `determinants-and-cramers-rule`.
- **Cognitive-load repair:** `matrix-arithmetic` is retitled **Matrix Products**
  and concentrates on the operation later lessons use. Addition and scaling
  remain a brief entrywise warm-up; identity, inverse and cancellation are
  deferred to `inverse-matrices`. The obsolete zero-product retrieval item is
  replaced by a factor-order diagnosis.
- **Correctness repair:** the summary, concept card, theorem, unbounded example,
  retrieval feedback and completion standard in
  `systems-of-inequalities-and-linear-programming` now state the corner theorem
  for a nonempty closed, bounded feasible polygon. The unbounded example proves its
  minimum with a global lower bound and proves the missing maximum with a
  feasible ray instead of invoking the bounded theorem.
- **Practice and checking:** the course directions now tell the learner to
  cover the worked answer, complete the faded task, predict before revealing a
  lab result, keep fractions exact, and verify against source equations or an
  identity product. This makes the interactive lab a check on a prior claim
  rather than a substitute for making one.

## Residual boundary

This remains an Algebra course rather than a linear algebra or optimisation
course. It does not prove uniqueness of reduced row echelon form, develop rank
as a general invariant, teach vector spaces or eigenvalues, analyse numerical
conditioning, solve overdetermined systems, teach the simplex algorithm, or
solve integer programmes. Unbounded linear programmes are diagnosed here only
with explicit feasible rays or global bounds; a general recession-cone theory
is outside the completion standard.
