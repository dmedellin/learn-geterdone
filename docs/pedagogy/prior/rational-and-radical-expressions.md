# Pedagogy assessment — Rational and Radical Expressions (algebra, course 5)

First assessment, formed from all twelve lesson dicts in
`content/algebra/c5_rational/` (`part_a.py`, `part_b.py`, `__init__.py`) as they
stood on `pedagogy/openai-algebra` at `7e90553`. No lesson was sampled: every
body block, method, worked example, quiz explanation, misconception, completion
standard and attached lab configuration was read before the source was changed.
The seven `rationalfn` modes, the four `radicals` modes used here and the
radical `grapher` mode were then checked against what their lesson panels
promised.

The published order was and remains `rational-expressions-and-their-domains`,
`simplifying-rational-expressions`,
`multiplying-and-dividing-rational-expressions`,
`adding-and-subtracting-rational-expressions`, `complex-fractions`,
`solving-rational-equations`, `graphs-and-asymptotes`,
`simplifying-radical-expressions`, `operations-with-radicals`,
`rationalizing-denominators`, `solving-radical-equations`, and
`radical-functions-and-their-graphs`. Courses 1–4 already teach the needed
prerequisites: exact fractions and absolute value; linear equations and
inequalities; function notation, domain, range and transformations; and
factoring over the rationals. Course 1 also teaches principal roots, even/odd
index conditions and numerical radical simplification, so lesson 8 should
retrieve those ideas and extend them to variable expressions rather than
present them as wholly new.

## What the course teaches well

- **The large-scale sequence is coherent.**
  `rational-expressions-and-their-domains` records exclusions before
  `simplifying-rational-expressions` can hide them. Multiplication and division
  precede the LCD work in `adding-and-subtracting-rational-expressions`; both
  feed `complex-fractions` and `solving-rational-equations`. Only then does
  `graphs-and-asymptotes` distinguish a cancelled exclusion from a surviving
  denominator zero. The radical half similarly places principal-root and
  simplification rules before operations, conjugates, equations and graphs.
  No URL or lesson move is justified.
- **Domain is treated as mathematical data rather than aftercare.**
  `rational-expressions-and-their-domains` separates numerator zeros from
  denominator zeros and makes `0/0` explicitly undefined.
  `simplifying-rational-expressions`,
  `multiplying-and-dividing-rational-expressions`, `complex-fractions` and
  `graphs-and-asymptotes` repeatedly show that a reduced formula cannot recover
  an original exclusion. `simplifying-radical-expressions` and
  `radical-functions-and-their-graphs` transfer the same habit to even-root
  inequalities.
- **The course gives reasons for its rules.** Cancellation is multiplication
  by `K/K`; the LCD is built from maximal factor powers; clearing denominators
  is a one-way implication where the LCD can be zero; the principal-root
  convention explains `sqrt(x²) = |x|`; like radicals combine by distribution;
  and a conjugate works by the difference of squares. These explanations in
  `simplifying-rational-expressions`,
  `adding-and-subtracting-rational-expressions`,
  `solving-rational-equations`, `simplifying-radical-expressions`,
  `operations-with-radicals` and `rationalizing-denominators` are more
  transferable than mnemonics.
- **Extraneous candidates are handled honestly.**
  `solving-rational-equations` and `solving-radical-equations` both show the
  irreversible implication, keep every candidate visible and substitute into
  the original. Their labs likewise display rejected candidates rather than
  silently deleting them.
- **Many predictable wrong models are already named.** The course confronts
  cancelling terms (`simplifying-rational-expressions`), overlooking a
  divisor's zero (`multiplying-and-dividing-rational-expressions`), adding
  denominators and dropping a subtraction sign
  (`adding-and-subtracting-rational-expressions`), ignoring a zero lower half
  (`complex-fractions`), confusing a hole with an asymptote
  (`graphs-and-asymptotes`), reading `sqrt(9)` as `±3`
  (`simplifying-radical-expressions`), adding radicands and dropping a binomial
  middle term (`operations-with-radicals`), choosing the same cube-root factor
  instead of the missing one (`rationalizing-denominators`), and treating the
  check as optional (`solving-radical-equations`).
- **The lab architecture supports the intended distinctions.** The rational
  lab keeps an unreduced expression and its original ban list; its solve modes
  check the original in exact arithmetic. The radical arithmetic lab preserves
  surd forms and labels decimals as checks. The radical grapher solves the
  domain conditions before drawing only the real-valued pieces.

## What failed, or what the course claimed without teaching

### The worked-example progression stopped before performance

1. **None of the twelve incoming lessons had a faded rehearsal.** Every page
   moved from a complete example to a multiple-choice quiz. The learner was
   never given a novel expression with the first strategic decision supplied
   and the remaining factoring, restriction, algebra and check withheld. That
   is most costly in `complex-fractions`, `solving-rational-equations`,
   `graphs-and-asymptotes`, `rationalizing-denominators` and
   `solving-radical-equations`, where choosing and executing a multi-step method
   is the stated objective.
2. **Several retrieval items repeated displayed work or tested recognition
   instead of execution.** `operations-with-radicals` asked for the exact
   `sqrt(50) - sqrt(18)` subtraction already printed in its worked panel.
   `radical-functions-and-their-graphs` repeated both `sqrt(5 - x)` and
   `sqrt(x² - 9)` from its body and worked example. `complex-fractions` asked
   only which LCD would clear an expression, not for the resulting fraction
   and restrictions. Correct selection there did not show that the learner
   could run either promised method.
3. **Feedback was unevenly diagnostic.** Many explanations justified the right
   answer but did not identify the wrong operation represented by every
   distractor. A learner who added denominator zeros, lost a factor sign,
   copied an output as an input or stopped before a final reduction was told the
   rule again rather than which step to repair.

### Prerequisite and scope claims were inaccurate

4. **`solving-rational-equations` invoked Course 6 before Course 6.** It said
   the cleared equation came from “courses 2 and 6” and offered the quadratic
   formula in its method. Every example on the page factors with Course 4
   techniques; the formula and discriminant belong to the next course and are
   unnecessary here.
5. **The course outcome overgeneralised radical domains.** The course home
   promised to exclude every value making “a radicand negative,” although
   negative radicands are allowed under odd roots. The correct act is to solve
   the non-negative condition for every even-index radicand while retaining the
   other restrictions of the original expression.
6. **`simplifying-radical-expressions` briefly required index reduction without
   teaching or practising it.** Its simplified-form list introduced
   `4th-root(9) = sqrt(3)`, while its worked examples, method and quiz all
   assessed extraction of perfect powers. Worse, the attached lab selected the
   `reduce` mode, whose whole subject is index reduction, even though the panel
   promised to factor a radicand and pull perfect powers out. The page's prose,
   practice and lab were assessing different acts.
7. **`rationalizing-denominators` made a universal claim from numerical
   examples.** It said the conjugate multiplier can never be zero and that
   rationalising can never affect a domain. Before simplification,
   `sqrt(2) + sqrt(2)` has the zero conjugate
   `sqrt(2) - sqrt(2)` despite having a nonzero denominator. For symbolic
   radical denominators a proposed multiplier may vanish at legal inputs. The
   lab and all worked examples treat numerical denominators; the prose needed
   that scope and the instruction to simplify and combine first.
8. **`rational-expressions-and-their-domains` overpromised arbitrary exact
   roots in its panel and note.** The lab names rational roots and irrational
   quadratic roots exactly, but it deliberately reports an unresolved
   higher-degree factor when a rational-root search cannot name all of its real
   zeros. Saying it “reports every zero exactly” contradicted that honest
   behaviour.

### Three mathematical descriptions were wrong or too narrow

9. **`simplifying-radical-expressions` gave the wrong domain for
   `sqrt(48x⁵y⁴)`.** It concluded `x >= 0`, overlooking every point with
   `y = 0`: there the original radicand is zero even when `x < 0`. Its proposed
   reduced form then contained `sqrt(3x)` and was undefined at those valid
   points. This is not a cosmetic edge case; the simplification changed the
   domain.
10. **`graphs-and-asymptotes` defined a hole only when a common factor had the
    same multiplicity upstairs and downstairs.** A denominator factor that
    cancels completely also gives a hole when the numerator has greater
    multiplicity, for example `(x - 2)²/[(x - 2)(x + 1)]`, whose hole is
    `(2, 0)`.
11. **`radical-functions-and-their-graphs` spoke of one endpoint where a
    quadratic radicand may create two.** Its own `sqrt(x² - 9)` example has
    boundary points at both `-3` and `3`. The method needed to ask for every
    boundary point and distinguish the one-ray linear model from a two-ray or
    interval domain.

## Where a learner gets stuck

- After the complete domain or simplification trace in
  `rational-expressions-and-their-domains` and
  `simplifying-rational-expressions`: the learner has seen the author make all
  the decisions but has not yet had to preserve an exclusion through a new
  cancellation.
- At division in `multiplying-and-dividing-rational-expressions`: three sources
  of exclusions are named, but without a faded quotient it is easy to record
  only the denominators visible before flipping.
- At the first lower half that equals zero in `complex-fractions`: “collect all
  small denominators” does not itself reveal the additional condition that the
  entire divisor be nonzero.
- When a factorable quadratic appears in `solving-rational-equations`: the text
  pointed forward to Course 6, so a learner could reasonably think the next
  course's formula was required instead of retrieving Course 4 factoring.
- At the transition from a cancelled factor to a graph feature in
  `graphs-and-asymptotes`: the equal-multiplicity definition made a valid hole
  with zero height look like an exception.
- In `simplifying-radical-expressions`: Course 1 material, variable-domain
  extensions and an unpractised index-reduction rule were presented at once,
  and the attached lab then practised only the last of those.
- In `rationalizing-denominators`: “use the conjugate” appeared unconditional,
  even though the first step must simplify and combine the denominator before
  deciding that it truly has two unlike terms.
- In `radical-functions-and-their-graphs`: the singular word “endpoint” fits
  `sqrt(x - h)` but conflicts with the two boundaries the quadratic example
  visibly produces.

## Repairs made in this pass

All twelve lesson URLs and their order remain unchanged. No lesson was added,
removed, renamed or moved, so none of the five URL declarations changed.

- **Observable objectives:** every lesson's syllabus line now names a visible
  act: factor and exclude, cancel and retain restrictions, flip and account for
  the divisor, construct an LCD, clear a complex fraction, solve and check,
  classify graph features, simplify under the correct root conditions,
  combine or distribute, choose a rationalising multiplier, reject extraneous
  candidates, or solve a domain inequality and sketch exact features.
- **Worked → faded → independent:** every worked panel now ends with a novel
  faded rehearsal. The first factorisation, flip, LCD, multiplier, sign
  condition or inequality is supplied; the remaining algebra and diagnostic
  check belong to the learner. Course-level directions make the order explicit.
- **Independent retrieval and diagnostic feedback:** repeated radical and
  domain questions were replaced with novel inputs, and the complex-fraction
  quiz now requires a complete reduction with restrictions. Explanations name
  the specific numerator-zero, denominator-product, sign-distribution,
  reciprocal, cancellation, middle-term, endpoint or inequality error behind
  the distractors.
- **Prerequisite repair:** `solving-rational-equations` now retrieves linear
  solving from Course 2 and factorable quadratics from Course 4. It neither
  invokes nor requires Course 6.
- **Scope repair:** the course home distinguishes even- from odd-index
  radicands. The domain lab description states exactly which roots it can name.
  Rationalising is scoped to the numerical radical denominators taught and
  exercised here, with simplification and combining required before choosing a
  conjugate.
- **Correctness repair:** the invalid two-variable radical example became a
  one-variable example whose domain really is `x >= 0`; the hole definition now
  covers a completely cancelled denominator factor at any numerator
  multiplicity; and the radical-graph method asks for every boundary point.
- **Lab alignment:** `simplifying-radical-expressions` now requests the
  `simplify` mode, which factors the radicand and extracts complete groups as
  the panel promises. No shared lab arithmetic needed to change.

## Residual boundary

The refactor deliberately stays within the course's real-number and school-
algebra scope. It does not add complex radicals, a general algorithm for the
real zeros of arbitrary high-degree denominator polynomials, symbolic
rationalisation across parameter-dependent domains, partial fractions, or
calculus proofs of asymptotic behaviour. Those omissions are now stated or
scoped rather than silently crossed.
