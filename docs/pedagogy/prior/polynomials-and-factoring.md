# Pedagogy assessment — Polynomials and Factoring (algebra, course 4)

First assessment, formed from all thirteen lesson dicts in
`content/algebra/c4_polynomials/` (`part_a.py`, `part_b.py`, `__init__.py`) as
they stood on `pedagogy/openai-algebra` at `d68de53`. No lesson was sampled:
every body block, method, worked example, quiz explanation, misconception,
completion standard and attached lab configuration was read before the source
was changed. The relevant `polynomial`, `factoring` and `grapher` lab modes were
then checked against the acts and conclusions their lesson panels promised.

The published order was and remains `polynomials-degree-and-standard-form`,
`adding-and-subtracting-polynomials`, `multiplying-polynomials`,
`special-products`, `factoring-out-the-greatest-common-factor`,
`factoring-by-grouping`, `factoring-simple-trinomials`, `the-ac-method`,
`factoring-special-forms`, `polynomial-long-division`,
`synthetic-division-and-the-remainder-theorem`,
`the-factor-theorem-and-rational-roots`, and
`graphs-of-polynomial-functions`. Courses 1–3 already teach the prerequisites
this sequence needs: integer and rational exponents, roots and radicals, the
distributive law, like terms, exact substitution, function notation, the
coordinate plane and basic graph reading. Quadratic discriminants and the
quadratic formula are deliberately Course 6 material.

## What the course teaches well

- **The large-scale sequence is coherent and cumulative.**
  `polynomials-degree-and-standard-form` establishes membership, degree and
  missing coefficients before the operations use them.
  `adding-and-subtracting-polynomials` makes sign distribution explicit before
  `multiplying-polynomials` increases the bookkeeping load. `special-products`
  derives the identities forwards before `factoring-special-forms` later asks
  learners to recognise them backwards. Long division precedes synthetic
  division; the remainder theorem precedes the factor theorem; and roots
  precede graph behaviour. No lesson needs to move or change URL.
- **The course usually gives a reason instead of a mnemonic.**
  `adding-and-subtracting-polynomials` and
  `factoring-out-the-greatest-common-factor` present collecting and factoring
  as the distributive law in opposite directions. `multiplying-polynomials`
  replaces FOIL as a general method with an `m × n` product count.
  `special-products` expands every identity. `the-ac-method` explains why
  splitting `bx` preserves the expression. `polynomial-long-division` states
  the division identity and its degree stopping rule, while
  `synthetic-division-and-the-remainder-theorem` proves the remainder theorem
  from that identity.
- **Checking is treated as part of the act.**
  `adding-and-subtracting-polynomials` uses substitution to expose sign errors;
  `multiplying-polynomials` predicts degree, leading term, constant and product
  count; every factoring lesson expands the result; and
  `polynomial-long-division` requires the full identity `f = dq + r` rather
  than a quotient alone. These checks target different error classes and are
  faster than redoing the original work.
- **The factoring decision sequence is unusually explicit.**
  `factoring-out-the-greatest-common-factor` makes the first move non-optional.
  `factoring-by-grouping` tests all three pairings and distinguishes failure of
  a method from failure to factor. `factoring-simple-trinomials` and
  `the-ac-method` display complete finite pair searches, including empty
  results. `factoring-special-forms` makes term count and exact pattern tests
  precede recognition. This is substantially better than teaching factoring
  as inspired inspection.
- **The root theorems are connected rather than listed.**
  `synthetic-division-and-the-remainder-theorem` shows that its last row entry
  is `f(c)`. `the-factor-theorem-and-rational-roots` then proves both directions
  of `f(c) = 0` if and only if `(x - c)` is a factor, generates `±p/q` rather
  than guessing, divides out a hit, and states that an empty result rules out
  rational roots rather than all roots.
- **Many predictable misconceptions were already named.** These include
  reading degree before collecting (`polynomials-degree-and-standard-form`),
  negating only the first term (`adding-and-subtracting-polynomials`), adding
  exponents during addition or multiplying them during multiplication
  (`adding-and-subtracting-polynomials`, `multiplying-polynomials`), trusting
  FOIL outside a two-by-two product (`multiplying-polynomials`), dropping the
  middle `2ab` (`special-products`), dropping the quotient `1` in a GCF
  (`factoring-out-the-greatest-common-factor`), extracting the wrong sign from
  the second group (`factoring-by-grouping`, `the-ac-method`), matching product
  but not sum (`factoring-simple-trinomials`), inventing a sum-of-squares
  conjugate (`factoring-special-forms`), omitting zero coefficients
  (`polynomial-long-division`,
  `synthetic-division-and-the-remainder-theorem`), swapping the numerator and
  denominator divisibility conditions
  (`the-factor-theorem-and-rational-roots`), and drawing every root as a
  crossing (`graphs-of-polynomial-functions`).
- **The strongest lab behaviours expose the search.** The grouping mode shows
  every pairing, including a polynomial which factors by another route. The
  trinomial and ac modes print every product-sum pair. The rational-root mode
  constructs, deduplicates and evaluates the complete candidate list in exact
  arithmetic. Polynomial division prints every subtraction and verifies
  `d·q + r`; synthetic division evaluates `f(c)` independently. Those are the
  right things to make visible.

## What failed, or what the course claimed without teaching

### The coefficient domain changed without warning

1. **“Factor completely” alternated among integers, rationals and reals.**
   `factoring-out-the-greatest-common-factor` defined a coefficient gcd while
   the opening definition allowed arbitrary numerical coefficients, then said
   extracting `3` from coefficients `6, 9, 4` was disallowed because it leaves
   `4/3`. The equality is algebraically valid; what fails is the unstated
   integer-content convention. `factoring-simple-trinomials` alternated between
   “over the integers” and “over the rationals.” `the-ac-method` used an
   integer pair search but sometimes promoted its result to a claim about all
   rational factors. `factoring-special-forms` switched to the reals. A learner
   could execute every method correctly and still not know what “finished”
   meant.
2. **The course home overpromised arbitrary factorisation.** It said the learner
   could factor “any polynomial a school course will hand you” and say when one
   cannot be factored. But `the-factor-theorem-and-rational-roots` only rules out
   rational linear factors. A quartic with no rational root may still split
   into two rational quadratics, a limitation the shared lab itself correctly
   knew. The course did not teach a complete higher-degree factorisation
   algorithm and should not claim one.

### Course 6 material was used before it was taught

3. **`the-ac-method` introduced the discriminant as an equivalent test and
   made it part of the completion standard.** The discriminant belongs to
   Course 6. Its presence turned a finite integer-pair method into a method
   whose negative result appeared to require a later theorem. The attached ac
   lab repeated the discriminant and printed quadratic roots.
4. **`factoring-special-forms` invoked a discriminant to reject `x² + 4`.**
   Positivity proves the needed claim with current prerequisites: `x² + 4 > 0`
   for every real `x`, so there is no real linear factor. The later formula was
   unnecessary.
5. **`the-factor-theorem-and-rational-roots` told the learner to use the
   discriminant after division reached degree 2.** Its attached root lab then
   printed exact irrational or complex quadratic roots. The correct Course 4
   action is to use the already-taught pair or ac search, state that no rational
   factor remains, and leave the real/complex classification to Course 6.
6. The polynomial `grapher` mode also used a negative discriminant to upgrade
   “no rational zero” to “no real zero.” That conclusion may be true for a
   particular quadratic, but the lab taught it with a theorem the reader had
   not yet met.

### Several negative claims were broader than their evidence

7. **`factoring-special-forms` said `a² + b²` never factors over the reals.**
   The useful identity-level claim is only that a plus sign does not match
   `(a - b)(a + b)`. The quadratic `x² + b²` for nonzero real `b` has no real
   linear factor, but a higher-degree sum of square expressions can factor.
   For example the cube-pattern factor `x⁴ + x² + 1` factors over the rationals
   as `(x² + x + 1)(x² - x + 1)`. The same lesson's statement that the
   quadratic-looking cube factor “never factors further over the reals” was
   therefore also too broad when `a` and `b` stand for expressions rather than
   single linear terms.
8. The grouping lab's empty branch used the heading “nothing else would have
   worked either.” Its later qualification was about rational linear factors,
   but the heading stated a broader conclusion than the search proved. A
   learner scanning the verdict could easily acquire exactly the method-versus-
   polynomial confusion that `factoring-by-grouping` otherwise handles well.
9. The rational-root lab said every degree-2-or-3 polynomial with an empty
   candidate list still crossed the axis. That is correct for an odd-degree
   cubic and false for a quadratic such as `x² + 1`. The search establishes no
   rational root; it does not decide whether a quadratic's other roots are real
   or complex.

### The worked-example progression stopped before performance

10. **None of the thirteen incoming lessons included a faded rehearsal.** A
    complete example was followed by a multiple-choice quiz. The learner never
    received a novel polynomial with the first strategic decision supplied and
    the remaining algebra, stopping decision and check withheld. That gap is
    especially serious in `factoring-by-grouping`, `the-ac-method`,
    `polynomial-long-division`,
    `synthetic-division-and-the-remainder-theorem`, and
    `the-factor-theorem-and-rational-roots`, where the procedure is the stated
    objective.
11. **Several retrieval items repeated displayed arithmetic or assessed only a
    verbal rule.** `polynomials-degree-and-standard-form` repeated the worked
    leading-coefficient example. `multiplying-polynomials` repeated its opening
    monomial product. `factoring-special-forms` repeated the exact perfect-square
    and cube examples from the body. `polynomial-long-division` and
    `synthetic-division-and-the-remainder-theorem` had no independent division
    calculation, and `the-ac-method` asked for `ac` rather than requiring the
    factorisation. Recognition of a recently displayed answer is not evidence
    that the learner can run the method.

### The graph lesson overclaimed what a qualitative sketch determines

12. **`graphs-of-polynomial-functions` said degree, leading coefficient and
    roots were everything distinguishing polynomial graphs, then instructed the
    learner to draw “the only” smooth curve consistent with a few features.**
    Those data determine end directions and axis behaviour, not the exact
    locations of every turn or a unique metric curve. The lesson was teaching a
    qualitative sketch but described it as a determined plot.
13. The same lesson asserted and assessed the `n - 1` turning-point bound
    without the calculus needed to justify it, even though exact turning-point
    analysis was explicitly outside the course. The root-count bound already
    proved from factors was sufficient for the stated sketching objective.
14. The same lesson's panel told the learner to enter roots and their
    multiplicities. The shipped grapher accepts a polynomial expression,
    searches only its rational zeros and derives multiplicity by division. The
    promised controls did not exist, and the default presets did not open on
    the worked polynomial.

## Where a learner gets stuck

- At the GCF definition in `factoring-out-the-greatest-common-factor`: the
  learner has already been told coefficients may be any number, but is now
  expected to know that “greatest” refers to an integer normalisation rather
  than arbitrary rational rescaling.
- At an empty search in `factoring-simple-trinomials` or `the-ac-method`: the
  text alternates between integer, rational and real factorisations, so the
  learner cannot state the conclusion at the right scope.
- At the no-pair theorem in `the-ac-method`: a later-course discriminant appears
  to be the reason the finite search is trustworthy, even though the search can
  be justified directly from the middle products of two hypothetical brackets.
- At the sum-of-squares section of `factoring-special-forms`: “the conjugate
  identity does not apply,” “there is no rational linear factor,” and “there is
  no real factorisation of any kind” are treated as interchangeable claims.
- At the first independent-looking division question: the page has shown a
  complete trace, but `polynomial-long-division` and
  `synthetic-division-and-the-remainder-theorem` do not require a new trace from
  the learner before testing terminology.
- When `the-factor-theorem-and-rational-roots` reaches a quadratic quotient:
  the stated next move uses an untaught discriminant instead of retrieving the
  pair and ac methods from two lessons earlier.
- In `graphs-of-polynomial-functions`: the side panel asks for roots and
  multiplicities although the control asks for `y = f(x)`, then the method
  implies a few qualitative features locate an exact curve. Both mismatches
  make a correct learner look for information or controls the page cannot give.

## Repairs made in this pass

All thirteen lesson URLs and their order remain unchanged. No lesson was added,
removed, renamed or moved, so none of the five URL declarations changed.

- **Observable objectives:** every lesson's syllabus line now names an act the
  learner must perform: classify and standardise, align and subtract, predict
  and multiply, recognise a product, extract and verify a GCF, test groupings,
  exhaust a pair list, run ac, retest special factors, divide and state
  `f = dq + r`, run a synthetic row, exhaust rational-root candidates, or
  sketch named graph features.
- **Worked → faded → independent:** every lesson now ends its worked panel with
  one novel faded rehearsal. The first classification, sign decision, degree
  prediction, pattern match, GCF, pairing, `ac`, missing-power setup, synthetic
  setup, first root or end-behaviour decision is supplied. The learner must
  complete the algebra and the diagnostic check before opening the lab or
  selecting a quiz answer. Course-level use instructions make that sequence
  explicit.
- **Independent retrieval:** repeated answers were replaced in
  `polynomials-degree-and-standard-form`, `multiplying-polynomials` and
  `factoring-special-forms`. `the-ac-method` now requires a full novel
  factorisation. `polynomial-long-division` and
  `synthetic-division-and-the-remainder-theorem` now require a new quotient and
  remainder. New feedback identifies the sign, exponent, missing product,
  pattern, coefficient-copy or wrong-`c` model represented by the distractors.
- **Domain discipline:** the course home now promises the standard
  integer-coefficient techniques and rational-root conclusions it actually
  teaches. `factoring-out-the-greatest-common-factor` states the integer-content
  convention and explains why a rational rescaling is true but not an integer
  GCF. `factoring-simple-trinomials`, `the-ac-method`,
  `factoring-special-forms` and
  `the-factor-theorem-and-rational-roots` name integers, rationals or reals at
  the point where the qualifier matters. The course home explicitly excludes a
  complete arbitrary quartic algorithm.
- **Prerequisite repair:** every discriminant and exact quadratic-root use was
  removed from Course 4 content and from the trinomial, ac, rational-root and
  polynomial-grapher outputs used here. Empty pair lists are justified from the
  two middle products of hypothetical integer brackets. Quadratic leftovers
  stop at “no rational linear factor,” with Course 6 named as the later source
  of the real/complex classification.
- **Negative-result repair:** `factoring-special-forms` now distinguishes a
  failed conjugate pattern from general irreducibility, proves the simple
  quadratic `x² + b²` claim by positivity, and tells learners to retest a cube
  factor instead of assuming it can never split. The grouping lab verdict now
  says exactly “no rational linear factor.” The rational-root lab separates the
  cubic guarantee of an irrational real zero from the unresolved quadratic
  real/complex case.
- **Graph repair:** `graphs-of-polynomial-functions` now calls its output a
  qualitative sketch, states that the named data do not locate every turning
  point, and removes the false claim of a unique curve. The unproved
  turning-point bound was removed from the key, method, worked example, quiz
  and misconceptions; root multiplicity and the y-intercept now carry that
  retrieval load. Its course-local
  grapher presets open on the worked and faded polynomials, and its panel now
  accurately asks for a polynomial expression while explaining that rational
  zeros and multiplicities are derived.

No arithmetic operation or checker case was added. The shared lab changes
remove later-course calculations and narrow conclusions; the new numerical
lesson examples use already-shipped polynomial arithmetic rather than changing
its implementation. The new-arithmetic mutation requirement therefore does not
apply to this pass.
