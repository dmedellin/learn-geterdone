# Pedagogical assessment: Sequences and Series

## Scope and method

This assessment covers all eleven source lessons in
`content/algebra/c9_sequences/`, front to back: every concept card, body block,
method, worked example, quiz explanation, misconception, completion standard
and lab brief. It also checks each prerequisite the course actually uses
against the preceding Algebra courses. The generated pages under `site/` were
not treated as source.

## What already worked

- **The finite-sequence spine is coherent.** `sequences-and-recursion` treats a
  sequence as a function before `sigma-notation` gives compact notation for a
  sum. `arithmetic-sequences-and-series` and
  `geometric-sequences-and-series` then derive term and finite-sum formulas,
  and `partial-sums-and-telescoping` turns the collection of those finite sums
  into a sequence in its own right. The course usually tells the learner why a
  formula is true rather than merely naming it.
- **Checks are scoped honestly.** `sequences-and-recursion` distinguishes a
  candidate formula that agrees with six terms from a proof.
  `arithmetic-sequences-and-series`, `geometric-sequences-and-series` and
  `partial-sums-and-telescoping` compare closed forms with direct computation
  while saying exactly what one numerical agreement establishes.
  `the-binomial-theorem` checks a complete expansion by substitution, and
  `the-general-term-of-an-expansion` correctly replaces that unavailable check
  with an independent exponent check for one isolated term.
- **The infinite-series meaning is concrete.** `infinite-geometric-series`
  defines a sum through the sequence of finite partial sums, gives an exact
  error term, and separates growth without bound from oscillation.
  `repeating-decimals-as-series` then uses that definition to explain why a
  repeating decimal is a fraction and why `0.999…` is exactly `1`, rather than
  appealing to a slogan.
- **Applications preserve the mathematics.**
  `annuities-and-accumulated-payments` derives accumulation, present value and
  perpetuity formulas from one geometric series. It keeps the payment period
  and rate period aligned, distinguishes the two ends of the timeline, keeps
  exact values until the final rounding, and explains why `|r| < 1` is not a
  condition on a finite accumulation.
- **The binomial sequence is motivated by counting.** `pascals-triangle`
  connects the addition rule to choices that include or exclude a fixed
  object. `the-binomial-theorem` then counts which brackets supplied `b`, and
  `the-general-term-of-an-expansion` turns the resulting term into an exponent
  equation. The coefficients therefore arrive as counts rather than as an
  unexplained numerical pattern.
- **Independent retrieval already has diagnostic feedback.** Across all eleven
  lessons, quiz explanations identify the operation represented by the wrong
  answer: a shifted starting index in `sequences-and-recursion`, a missing
  endpoint in `sigma-notation`, term-versus-sum confusion in
  `arithmetic-sequences-and-series`, an illegal infinite formula in
  `infinite-geometric-series`, a misplaced decimal block in
  `repeating-decimals-as-series`, one extra interest period in
  `annuities-and-accumulated-payments`, one-based Pascal indexing in
  `pascals-triangle`, and a swapped or fractional `k` in the final two lessons.

## What failed, or what the course claimed without teaching

### The published objectives did not describe the whole course

1. The course-home outcome “Move between the two definitions” promised to turn
   a recursive rule into a closed form and back without restricting the claim.
   `sequences-and-recursion` correctly says there is no general conversion
   method and only develops the arithmetic and geometric cases later. The
   objective was broader than the instruction.
2. The incoming outcomes stopped at sequence families and infinite geometric
   sums. A learner could satisfy every published outcome without converting a
   repeating decimal in `repeating-decimals-as-series`, valuing a payment stream
   in `annuities-and-accumulated-payments`, constructing a row in
   `pascals-triangle`, expanding a power in `the-binomial-theorem`, or isolating
   a term in `the-general-term-of-an-expansion`.
3. Every incoming lesson syllabus line described content rather than observable
   performance. “A function on the positive integers,” “a constant ratio,” and
   “each entry the sum of the two above it” did not name what the learner had to
   generate, classify, sum, convert, value, construct, expand or isolate.
4. The course direction said every lab computes “the sum” in two ways. That was
   false of the definition, Pascal and general-term modes, even though those
   modes do perform useful independent checks of their own.

### The sequence order taught infinity before giving it a meaning

5. `geometric-sequences-and-series` introduced the infinite-sum formula, the
   `|r| < 1` condition and `0.999… = 1` while also introducing constant ratio,
   the n-th term and the finite-sum derivation. The worked example and two of
   its three retrieval items assessed convergence. Yet
   `partial-sums-and-telescoping` had not made the partial sums into a sequence,
   and `infinite-geometric-series` had not defined what an infinite sum means.
   Lesson 4 therefore carried two hard ideas and made lessons 5 and 6 partly
   retrospective.
6. The interactive `geometric` mode reinforced that premature sequence by
   plotting finite partial sums against an infinite limit and reporting
   convergence. The separate `infinite` mode already exists for lesson 6, so
   the duplication was in the presentation rather than a missing lab
   capability.

### Three mathematical edge cases were internally inconsistent

7. `sequences-and-recursion` defined every sequence as a function on all
   positive integers and then immediately allowed finite sequences. A finite
   sequence instead has a finite initial segment of those integers as its
   domain. Its summary also said there was “no last” term while claiming to
   introduce both finite and infinite sequences.
8. `geometric-sequences-and-series` excluded both `a₁ = 0` and `r = 0` because
   consecutive quotients become undefined. The lab, however, defines the
   sequence multiplicatively, accepts both cases, and correctly notes that the
   all-zero series converges for any chosen multiplier. The quotient is a way
   to *find* `r` when the denominator is nonzero; the recurrence or closed form
   is the definition that covers the edge cases. Consequently,
   `infinite-geometric-series` also misstated the complete convergence theorem.
9. `partial-sums-and-telescoping` said every series “strictly” telescopes by
   taking `bₖ = -Sₖ₋₁`, immediately after insisting that `S₀` had not been
   defined. Defining `S₀ = 0` would repair the notation, but the observation
   supplies no usable way to find a sum and adds load to a lesson already
   coordinating partial sums, term recovery and useful telescoping.

### A proof used a prerequisite four lessons before it was taught

10. `infinite-geometric-series` justified `rⁿ → 0` by expanding
    `(1 + h)ⁿ` and retaining its positive terms. That is the binomial theorem,
    which `the-binomial-theorem` does not teach until lesson 10; making the
    row-by-row argument general also points toward the induction explicitly
    left to another path. Course 7 has already taught exponential decay and its
    horizontal asymptote, so this course can retrieve that prerequisite and use
    the exact geometric error term without importing a later theorem.

### Complete examples still stopped before transfer

11. Every incoming lesson went from a fully completed worked example directly
    to independent multiple choice. That gap is especially costly in
    `sigma-notation`, `partial-sums-and-telescoping`,
    `infinite-geometric-series`, `annuities-and-accumulated-payments`,
    `the-binomial-theorem` and `the-general-term-of-an-expansion`, where the
    completion standard is a multi-line production rather than recognition.
12. `the-binomial-theorem` already taught how to isolate the `x⁵` term of a
    large expansion and used two retrieval questions about single terms.
    `the-general-term-of-an-expansion` then announced that act as its new idea.
    This duplicated the later lesson's target while adding coefficient
    calculation to the earlier lesson's already substantial load of factorials,
    counting, full expansion and signs.
13. `the-binomial-theorem` stated its theorem only for positive `n` while the
    same lesson displayed the `n = 0` expansion and its lab included an
    exponent-zero preset. The correct scope is a nonnegative integer exponent.

## Where learners get stuck

- In `sequences-and-recursion`, the notation `aₙ₋₁` is liable to become
  `aₙ - 1`, and a guessed formula that survives familiar terms feels proved.
  The missing bridge is a new recursion for which only the first strategic
  transformation is supplied.
- In `sigma-notation`, learners can count endpoints correctly and still move
  the limits without substituting into the summand. A shifted first term is the
  cheapest diagnostic and needs to be rehearsed, not merely shown.
- In `arithmetic-sequences-and-series`, `n` terms are confused with `n` steps,
  a negative difference loses its sign, and `aₙ` is reported when the question
  asks for `Sₙ`.
- In `geometric-sequences-and-series`, subtraction remains the reflex from the
  prior lesson, the exponent is shifted by one, and the `r = 1` case is forced
  into a finite-sum formula whose denominator is zero.
- In `partial-sums-and-telescoping`, learners subtract consecutive sums one
  place too far, extend an `n ≥ 2` formula back to the first term, or leave
  `bₙ` instead of `bₙ₊₁` at the uncancelled end.
- In `infinite-geometric-series`, shrinking terms are mistaken for a sufficient
  test, a limit is treated as a partial sum eventually reached, and a negative
  ratio is mistaken for divergence even when its magnitude is below `1`.
- In `repeating-decimals-as-series`, a delayed repeating block is put over the
  wrong power of ten or given the wrong number of nines. The learner may then
  defend `0.999… < 1` by transferring a property of every truncation to their
  limit.
- In `annuities-and-accumulated-payments`, the annual rate and monthly count are
  mixed, the final ordinary-annuity payment earns an invented period of
  interest, or present value and accumulated value are computed at opposite
  ends of the timeline.
- In `pascals-triangle`, both row and position are counted from `1`, an
  interior entry uses the visually nearest rather than immediately adjacent
  parents, and an attractive diagonal pattern is trusted over the building
  rule.
- In `the-binomial-theorem`, a power is applied only to `x` rather than to its
  coefficient, or signs are alternated by memory rather than obtained from
  `(-b)ᵏ`.
- In `the-general-term-of-an-expansion`, only one factor's contribution to the
  power of `x` is counted, `k` is confused with the term number, or a fractional
  `k` is rounded into a term the expansion does not contain.

## Prerequisite audit

- Exact fractions, exponent laws and long division are established in
  `algebra-foundations`; linear equation solving is established in
  `linear-equations-and-inequalities`; functions and discrete graphs are
  established in `lines-functions-and-graphs`; polynomial expansion is
  established in `polynomials-and-factoring`; and exponential growth, decay
  and periodic interest are established in
  `exponential-and-logarithmic-functions`.
- Those prerequisites occur before their uses here. In particular,
  `sequences-and-recursion` explicitly retrieves the function definition,
  `the-general-term-of-an-expansion` needs only a linear equation in `k`, and
  `annuities-and-accumulated-payments` extends rather than presupposes the
  single-deposit interest model.
- Course 8 is not needed by this course, so the existing “Courses 1–7”
  assumption is truthful even though Sequences and Series follows it in the
  published path.
- The one incoming violation was the binomial expansion inside
  `infinite-geometric-series`; it has been replaced by retrieval of the earlier
  exponential-decay result. No change to an earlier signed-off course was
  required.

## Repairs made in this pass

All eleven lesson URLs and their order remain unchanged. No lesson was added,
removed, renamed or moved, and no slug changed, so none of the five URL
declarations changed.

- **Observable objectives:** the course home now scopes conversion to the
  arithmetic and geometric families and names decimal conversion, payment
  valuation, Pascal construction, binomial expansion and single-term
  isolation. Every lesson syllabus line names an observable act measured by
  its completion standard.
- **Worked → faded → independent:** every worked panel now ends with a novel
  faded rehearsal. The first definition choice, shift substitution, family
  classification, partial-fraction split, convergence test, decimal split,
  timeline decision, Pascal row, binomial setup or exponent equation is
  supplied; the learner completes the computation and an independent check
  before using the existing diagnostic quiz.
- **Prerequisite and load repair:**
  `geometric-sequences-and-series` now stops at terms and finite sums, while
  its lab plots and checks those finite sums without announcing a limit.
  `infinite-geometric-series` owns the convergence condition and retrieves
  exponential decay from Course 7. `the-binomial-theorem` owns complete
  expansions; single-term extraction is left to
  `the-general-term-of-an-expansion`. Optional Pascal diagonal and powers-of-11
  excursions no longer compete with construction, indexing and counting.
- **Correctness repair:** finite sequences use a finite initial integer domain;
  geometric sequences are defined by multiplication so `r = 0` and the
  all-zero sequence are handled consistently; the convergence theorem states
  the all-zero exception; the circular “every series telescopes” aside is
  removed; and the binomial theorem includes `n = 0`.
- **Retrieval and misconception handling:** the lesson-4 retrieval now tests
  finite-sum decisions rather than borrowing lesson 6's convergence target,
  and lesson 10 retrieves a complete signed expansion rather than lesson 11's
  single-term method. Existing explanations continue to diagnose every
  distractor rather than restating only the correct rule.
- **Lab alignment:** the existing `geometric` mode is now the finite companion
  to lesson 4, while the existing `infinite` mode remains the convergence lab
  for lesson 6. No new arithmetic algorithm was added; the change removes the
  premature limit presentation from the finite mode.

## Residual boundary

This remains an Algebra course. It does not supply a general method for solving
recurrences, teach induction, develop convergence tests beyond the geometric
case, justify the completeness or Archimedean properties of the real numbers,
price payment streams under changing rates, or develop combinatorics beyond
the coefficients needed for a binomial expansion. Those limits are explicit
and none is required by the revised completion standards.
