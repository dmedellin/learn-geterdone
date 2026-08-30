# Pedagogy assessment — Foundations of Algebra (algebra, course 1)

First assessment, formed from all thirteen lesson dicts in
`content/algebra/c1_foundations/` (`part_a.py`, `part_b.py`, `__init__.py`) and
every lab mode they attach in `scripts/mathpath/labs/algebra_basics.py`, as they
stood on `pedagogy/openai-algebra` at `6ad45585c352`. No lesson was sampled: the
course metadata, every body block, method, worked example, quiz explanation,
misconception, completion standard and lab panel was read before any source was
changed.

The incoming order was `real-numbers-and-the-number-line`,
`properties-of-the-real-numbers`, `order-of-operations`, `absolute-value`,
`integer-exponents`, `scientific-notation`, `roots-and-radicals`,
`rational-exponents`, `algebraic-expressions-and-terms`,
`the-distributive-law`, `combining-like-terms`, `evaluating-expressions`,
`translating-words-into-algebra`. The course declares arithmetic — fractions,
negatives and long division — as its only prerequisite, and the path promises
that no prior algebra is required. That promise is the standard used here.

## What the course teaches well

- **It treats algebraic moves as licensed acts, not visual customs.**
  `properties-of-the-real-numbers` asks the reader to name commutativity,
  associativity or distribution one change at a time, and distinguishes a
  numerical check from a proof. `the-distributive-law` turns the invisible
  minus into a factor of `−1`; `combining-like-terms` derives collection by
  reading distribution backwards. This is exactly the intellectual habit the
  path footer promises: a step that works once is not thereby a rule.
- **The notation lessons diagnose the reading that produced an error.**
  `order-of-operations` separates equal-precedence left-to-right reading from
  the exponent's base and from the invisible grouping made by a fraction bar.
  `algebraic-expressions-and-terms` attaches a sign to its term and separates
  terms from factors. `evaluating-expressions` shows why replacing `x` by
  bare `−3` changes `x²` into the different string `−3²`. The attached
  expression lab computes both readings rather than printing one answer.
- **Exactness is a teaching decision rather than a footer claim.**
  `real-numbers-and-the-number-line` compares fractions and square roots
  exactly and says when a decimal is rounded. `integer-exponents` writes powers
  out as factors; `scientific-notation` checks the scientific calculation
  against the exact plain number; `roots-and-radicals` carries a simplified
  radical instead of replacing it by a decimal; `rational-exponents` runs the
  root-first and power-first routes separately. The labs make the distinction
  between an exact number and its display visible.
- **The predictable wrong models are named with real counterexamples.**
  Among them: a radical sign makes a number irrational
  (`real-numbers-and-the-number-line`); subtraction and division inherit
  commutativity or associativity (`properties-of-the-real-numbers`); the
  exponent includes an unbracketed minus (`order-of-operations`); `−x` means a
  negative output (`absolute-value`); a negative exponent makes the value
  negative (`integer-exponents`, `rational-exponents`); an exponent or root
  distributes over a sum (`integer-exponents`, `roots-and-radicals`,
  `the-distributive-law`); factors are terms
  (`algebraic-expressions-and-terms`); exponents add when like terms are added
  (`combining-like-terms`); and “less than” preserves spoken order
  (`translating-words-into-algebra`). Each is answered with a value that
  separates the wrong rule from the right one.
- **The closing acts are mostly observable.** `roots-and-radicals` asks for
  existence before simplification; `properties-of-the-real-numbers` asks for a
  property name on each line; `algebraic-expressions-and-terms` asks the reader
  to point to terms and signed coefficients; `translating-words-into-algebra`
  asks for a definition of the unknown with units and a test value that
  separates rival readings. Those are performances, not “understand” claims.
- **The final four-lesson chain is conceptually sound.**
  `the-distributive-law` exposes terms from brackets,
  `combining-like-terms` decides which exposed terms merge,
  `evaluating-expressions` substitutes a value without changing the structure,
  and `translating-words-into-algebra` builds that structure from a quantity.
  That order is the right preparation for course 2.

## What fails, or what the course claimed without teaching

### The no-prior-algebra promise was false in the incoming order

1. **A variable was formally defined in lesson 9 after the course had required
   one since lesson 2.** `properties-of-the-real-numbers` rearranged expressions
   in `a`, `b`, `c` and `x`; `integer-exponents` asked the learner to simplify a
   multi-variable power with restrictions; `roots-and-radicals` used
   `√(x²) = |x|`; and `rational-exponents` reasoned about `x^(p/q)`. Only then
   did `algebraic-expressions-and-terms` say that a letter stands for one number
   throughout a calculation and distinguish an expression from an equation.
   The path-level prerequisite copy said the course “starts from what a
   variable is”; the course did not. A learner entering with arithmetic alone
   had to infer the central object before the course named it.
2. `algebraic-expressions-and-terms` itself depended forward on three techniques
   while purporting to define the vocabulary they use. It reordered terms by a
   property then located in lesson 2, expanded `5(x + 2)` by the distribution
   lesson that followed it, and lowered the degree of `5x − 5x + 4` by the
   combination lesson two pages later. Those are useful previews only if they
   are fenced as previews; in the incoming page they read as assumed moves.

### Cognitive load and an unstated prerequisite

3. **`real-numbers-and-the-number-line` carried classification, decimal
   expansions, an exact ordering method, density and a three-line contradiction
   proof of the irrationality of `√2` on one beginner page.** Proof by
   contradiction and reduced-fraction parity were neither prerequisites nor
   completion acts. The proof was correct, but it introduced a hard method the
   learner was not asked to retrieve and displaced practice of the stated act:
   classify and order numbers exactly.
4. **`roots-and-radicals` told the learner to prime-factor a radicand but never
   taught a procedure for finding that factorisation.** Every worked line began
   after the hard step: `72 = 2³ · 3²`, `54 = 3³ · 2`, `75 = 5² · 3`.
   “Fractions, negatives, and long division” does not entail fluent prime
   factorisation. A learner who could apply the complete-groups rule but could
   not spot `108 = 2² · 3³` had no recovery method.
5. The same lesson disagreed with its lab about `√(1/2)`. The text said the
   root stayed in the denominator and deferred clearing it to course 5; the
   shipped `simplify` lab had a `sqrt(1/2)` preset and immediately reported
   `(1/2)sqrt(2)`, explicitly calling the move rationalising. Both values are
   equal, but a beginner page cannot call one form deferred while its lab calls
   the other the standard form without explaining the numerical step.
6. `absolute-value`'s lab displayed `√(a²)` three lessons before roots were
   defined and solved `|x − a| = c` by cases before course 2's equation method.
   The distance argument on the page is sufficient to locate the points, so
   neither preview is inherently wrong; the panel failed to say which figures
   were the present lesson's retrieval and which were previews.

### Statements a learner could trust that were wrong or incomplete

7. **`scientific-notation` defined a signed mantissa with
   `1 ≤ |a| < 10` and then described a positive exponent as making “the number
   bigger”.** For `−7.2 × 10⁴`, increasing the exponent increases the magnitude
   and makes the number smaller in the real-number order. Its sign check also
   said “anything bigger than 1” has non-negative exponent, which does not
   classify a large negative number. The method has to be stated in magnitude
   throughout if negative values are admitted.
8. **`rational-exponents` allowed `x ≥ 0` in the definition and then defined
   `x^(−p/q)` as its reciprocal without excluding `x = 0`.** At zero and a
   negative exponent that instruction divides by zero. The correct conditions
   for this course's convention are `x ≥ 0` for non-negative rational powers
   and `x > 0` for negative rational powers.
9. `properties-of-the-real-numbers` correctly called the field properties
   assumed, while its lab status said the surviving “field axioms and their
   consequences ... are proved once”. Axioms are stated or assumed; their
   consequences are proved. The lab contradicted the page on the epistemic
   status of the course's central rules.

### The worked-to-independent progression broke at the end

10. Every lesson had a worked example, a method and error-specific prose, but
    there was almost no **faded** guidance. The page generally moved from a
    complete solution to a multiple-choice item. Worse, the first two quiz
    questions in `rational-exponents` repeated `8^(2/3)` and `16^(−3/4)` from
    the worked table; `the-distributive-law` repeated `−2(x − 5)` and
    `−(x − 7)`; `evaluating-expressions` repeated `−x²` at `−3` and the exact
    polynomial at `−1/2`; `translating-words-into-algebra` repeated “five less
    than” and “twice the sum”. Recognition of the line just read is not
    independent practice.
11. Several completion standards repeated the page rather than measuring
    transfer. `real-numbers-and-the-number-line` re-used most of its worked
    mixed list; `order-of-operations` named the exact three trap strings from
    its body; `rational-exponents` again named `16^(−3/4)`; and
    `the-distributive-law` again named `−(x − 3)`. The course outcome promised
    a method the learner could use on a new expression, while these checks
    mostly measured recall of a displayed answer.
12. The course-level sentence “evaluate and rearrange any expression in this
    path” claimed far more than this course teaches. Rational expressions,
    polynomials, functions, logarithms and matrices all occur later on the
    path. This course teaches the real-number and elementary polynomial-shaped
    expressions those courses start from, not every later expression.

## Where a learner gets stuck

- At `properties-of-the-real-numbers` in the incoming order: `x` is already
  being moved before “variable”, “term” and “expression” have been defined.
- At the proof in `real-numbers-and-the-number-line`: the page changes from a
  classification lesson to parity and contradiction without making either a
  learner objective.
- At `roots-and-radicals`: “factor the radicand” is a demand to spot the first
  line, not a method for producing it; `sqrt(1/2)` then yields a lab form the
  reading said belonged to course 5.
- At a negative input in `scientific-notation`: “bigger than 1” and “makes the
  number bigger” pull in the wrong direction even though the formula uses
  absolute value.
- At `0^(−1/2)` after `rational-exponents`: the stated base condition admits
  zero and the stated negative-power rule immediately divides by it.
- At the quiz after `the-distributive-law`, `evaluating-expressions` or
  `translating-words-into-algebra`: a learner can select the remembered worked
  answer without demonstrating the method on a new case.

## Repairs made in this pass

All thirteen URLs remain published under the same slugs. No lesson was added,
removed or renamed at the URL level, so the membership of all five URL
declarations is unchanged. The content package now owns an explicit
pedagogical order; the one test tuple that deliberately mirrors content order
was reordered to match it without adding or removing a URL.

- **Course structure and objectives:** the order is now
  `real-numbers-and-the-number-line`, `order-of-operations`,
  `algebraic-expressions-and-terms`, `properties-of-the-real-numbers`,
  `absolute-value`, `integer-exponents`, `scientific-notation`,
  `roots-and-radicals`, `rational-exponents`, `the-distributive-law`,
  `combining-like-terms`, `evaluating-expressions`,
  `translating-words-into-algebra`. Numeric notation is settled before a
  variable is introduced, and a variable, term, sign, coefficient and factor
  are named before a symbolic property acts on them. Course copy now promises
  the expressions this course actually prepares, and the exponent/radical
  outcome names its domain decisions as observable work.
- **`real-numbers-and-the-number-line`:** the unsolicited contradiction proof
  was replaced by the usable whole-number-root classification and a clear note
  that proof is not the completion act. A faded mixed-list comparison and a
  novel independent list now require exact denominators and squaring.
- **`order-of-operations`:** the lab panel asks for the first queued operation
  before revealing it; the faded calculation combines left-associated division
  with a bracketed negative base; all three quiz questions and the completion
  task use new expressions rather than the page's trap strings.
- **`algebraic-expressions-and-terms`:** retitled “Variables, Expressions, and
  Terms” without changing its slug, moved to lesson 3, and rewritten so later
  distribution, collection and degree effects are explicitly previews. The lab
  panel fences its expanded count and degree column; the standard asks only for
  the as-written anatomy taught here.
- **`properties-of-the-real-numbers`:** “five properties” now means five named
  kinds rather than an ambiguous count of displayed equations. The lab asks for
  a prediction, the worked section fades a new signed distribution, and the
  standard requires both a named-line simplification and a valid
  counterexample. Lab copy now says field axioms are stated and consequences
  proved.
- **`absolute-value`:** the lab panel identifies `√(a²)` as lesson 8's preview
  and makes the negative-distance prediction a retrieval act. A new faded case
  diagnoses `−x` read as a negative output, and the completion task uses the
  distance meaning before course 2's general equation method.
- **`integer-exponents`:** the lab now asks the learner to predict the false
  power-of-a-sum row. A faded outer-power example diagnoses a forgotten
  coefficient and premature exponent collection; the completion task is a
  novel multi-variable simplification with restrictions.
- **`scientific-notation`:** every sign decision is now stated in magnitude, so
  negative mantissas agree with the definition and with the lab implementation.
  The lab's normalisation messages use the same language. Faded and independent
  work include negative values and a product that must be renormalised.
- **`roots-and-radicals`:** repeated division now produces the prime
  factorisation instead of assuming it can be spotted. The text and lab agree
  that `√(1/2) = √2/2` is the numerical standard form, while course 5 owns the
  general symbolic method. The panel names the actual radicand input (`−9`, not
  `sqrt(-9)`), and faded and independent radicals require an existence check,
  a factorisation and a raise-back check.
- **`rational-exponents`:** the domain now distinguishes `x ≥ 0` from `x > 0`
  when a reciprocal is required. The lab asks for both negative-base routes as
  a prediction; the two repeated quiz computations were replaced by
  `32^(3/5)` and `81^(−3/4)`; the completion task checks the zero restriction as
  well as both computational routes.
- **`the-distributive-law`:** lesson references now point to the reordered
  property lesson. The grid is used predictively, a partially supplied new
  expansion forms the faded step, the first two quiz questions no longer quote
  the worked examples, and the independent task includes both a trinomial and
  two brackets.
- **`combining-like-terms`:** property and expression references follow the new
  order. A faded case keeps swapped exponents apart, and the independent task
  requires expansion, signed grouping and a justification for every merge.
- **`evaluating-expressions`:** order-of-operations references now point to
  lesson 2. The lab asks for the substituted strings before their values, a
  faded negative substitution identifies the first divergent string, and the
  two repeated quiz calculations were replaced by novel signed expressions.
- **`translating-words-into-algebra`:** the lab asks for the unknown definition
  and a separating test value before showing its comparison. The faded and
  quiz phrases are new and distinguish reversal from missing grouping; the
  independent task requires units, dependent quantities and a rival-reading
  test rather than one more vocabulary match.

No arithmetic implementation was added or changed in the lab kit. The lab
source edits are explanatory copy only, so no arithmetic-checker mutation is
applicable to this pass.
