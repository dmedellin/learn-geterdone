# Pedagogical assessment: Exponential and Logarithmic Functions

## Scope and method

This assessment covers all twelve source lessons in
`content/algebra/c7_exponentials/`, front to back: every concept, body block,
method, worked example, quiz explanation, misconception, completion standard
and lab brief. It also checks the stated prerequisites backwards through
Courses 1–6. The generated pages under `site/` were not treated as source.

## What already worked

- **The central inverse idea is coherent across the course.**
  `what-a-logarithm-is` defines a logarithm as an exponent and converts both
  directions; `logarithmic-functions-and-their-graphs` exchanges domain,
  range, points and asymptotes through reflection; and
  `solving-exponential-equations` and `solving-logarithmic-equations` use those
  inverse moves in opposite directions. The course does not ask learners to
  memorise four unrelated uses of a logarithm.
- **Most rules are justified rather than announced.**
  `exponential-functions` derives the constant ratio, `the-laws-of-logarithms`
  derives all three laws from exponent laws, `change-of-base` derives its
  quotient from `b^y = x`, and `compound-interest-and-continuous-growth`
  builds both formulas from repeated multiplication and a limit.
- **Domain restrictions carry mathematical meaning.**
  `what-a-logarithm-is` explains why the argument is positive;
  `logarithmic-functions-and-their-graphs` moves that restriction with a
  horizontal shift; `the-laws-of-logarithms` catches the failure of
  `log_b(x^2) = 2 log_b(x)` at negative `x`; and
  `solving-logarithmic-equations` explains exactly how condensing can admit two
  negative factors that the original equation rejected.
- **Exact and rounded values are usually distinguished carefully.**
  `the-number-e`, `change-of-base`, `solving-exponential-equations` and
  `compound-interest-and-continuous-growth` preserve fractions or logarithmic
  quotients until the last line and label decimal approximations.
- **The incoming misconceptions are unusually specific.**
  `growth-and-decay` separates a constant percentage from a constant amount;
  `the-laws-of-logarithms` attacks the invented sum law and the confused
  quotient; `change-of-base` catches an upside-down quotient;
  `solving-logarithmic-equations` rejects arguments rather than negative
  candidates; and `logarithmic-scales` adds physical quantities before taking
  their logarithm. Quiz explanations usually identify the particular wrong
  operation represented by each distractor.
- **The real prerequisite chain is mostly sound.** Rational and negative
  exponents come from Course 1, equation solving from Course 2, inverse
  functions from Course 3, factoring from Course 4 and quadratic solving from
  Course 6. Those skills appear where they are needed in
  `exponential-functions`, `logarithmic-functions-and-their-graphs`,
  `solving-exponential-equations` and `solving-logarithmic-equations`.

## What failed, or what the course claimed without teaching

### The worked-example progression stopped before performance

1. **None of the twelve incoming lessons supplied a faded rehearsal.** Every
   page moved from a fully completed example straight to multiple choice. That
   gap is most costly in `the-laws-of-logarithms`, `change-of-base`,
   `solving-exponential-equations`, `solving-logarithmic-equations`,
   `compound-interest-and-continuous-growth` and `logarithmic-scales`, where
   the stated outcome is a multi-step method rather than recognition.
2. **Every incoming syllabus line described content instead of learner
   performance.** “The variable moves into the exponent” in
   `exponential-functions` and “Why decibels, pH and magnitude are logarithms”
   in `logarithmic-scales` are good prose, but neither says what the closing
   drill observes. The same problem ran through all twelve lesson cards.
3. **Some retrieval repeated displayed work.** `the-number-e` asked for the
   exact value of `(1 + 1/4)^4` after computing it in the body and worked
   example. `compound-interest-and-continuous-growth` asked learners to recall
   the same yearly, monthly and continuous balances printed immediately above.
   Recognition of a displayed number did not establish that either idea could
   be used on a new case.

### Prerequisites and cognitive load were out of order

4. **`growth-and-decay` invoked `ln 2` before a logarithm had been defined.**
   The rule-of-70 paragraph named the natural logarithm in lesson 2, while
   `what-a-logarithm-is` does not define any logarithm until lesson 4 and
   `common-and-natural-logarithms` does not introduce `ln` until lesson 7.
   The preview made the shortcut depend on notation the learner could not yet
   read.
5. **`the-number-e` introduced an unproved factorial series as a second hard
   idea.** Courses 1–6 do not teach factorial notation or infinite series, yet
   the lesson displayed eight partial sums, asserted that they approach the
   same number, and told learners to use the series to compute digits. The
   course objective needs the compounding limit and the number it names; it
   neither derives nor later uses the series identity. The lab may use that
   series as an independent numerical check, but the learner is not equipped
   to treat it as a second definition or method.
6. **`common-and-natural-logarithms` made obsolete table bookkeeping the mastery
   target.** Most of the reading, the worked example and one third of retrieval
   concerned characteristics and mantissas. It also introduced floor notation
   in a digit-count formula, although no earlier Algebra course teaches that
   notation. Those details displaced the transferable acts: identifying the
   hidden base, applying the matching inverse identity, estimating a value and
   choosing a useful logarithm for an exponential expression.

### Three statements taught the wrong model

7. **`common-and-natural-logarithms` said expressions written with `e` are
   undone by `ln` “and by nothing else.”** `ln` is the direct inverse, but any
   legal logarithm can be applied to both sides; another base simply leaves a
   quotient such as `log 12 / log e`. The original claim contradicted both
   `change-of-base` and `solving-exponential-equations`.
8. **`growth-and-decay` said the base alone decides behaviour without carrying
   its positive-quantity condition into the summary.** The lesson's formulas
   later state `a > 0`, but with a negative coefficient the graph's increasing
   or decreasing direction reverses. The intended claim is about positive
   quantity models, where the starting amount is positive.
9. **`compound-interest-and-continuous-growth` called `1 + 0.05/12` inexact.**
   The expression is exact; only a truncated decimal expansion of `0.05/12` is
   inexact. Confusing a nonterminating decimal with an inexact number undercuts
   the course's otherwise careful exact-versus-rounded discipline.

### The course home under-described its own target

10. The incoming outcomes named graph reading, the definition, the three laws
    and equation solving, but not the promised modelling acts in
    `growth-and-decay`, `compound-interest-and-continuous-growth` or
    `logarithmic-scales`. A learner could satisfy the published outcomes while
    never translating a percentage, choosing a periodic formula or converting
    a scale difference into a factor.

## Where learners get stuck

- After the complete table in `exponential-functions`: they can recognise the
  author's ratio row but have not classified a new signed table or extracted
  its coefficient and asymptote.
- At the percentage sentence in `growth-and-decay`: “up 5%” is still liable to
  become base `0.05`, and the complete 20% example leaves no partially guided
  transfer before the quiz.
- In `the-number-e`: a learner new to limits must already coordinate a moving
  base and exponent; factorial series notation made that coordination compete
  with a second, unexplained infinity.
- Between `what-a-logarithm-is` and `the-laws-of-logarithms`: learners may
  perform exact conversions but still treat laws as symbol shuffling unless a
  new expansion forces them to choose the outermost operation and preserve the
  domain.
- In `common-and-natural-logarithms`: the characteristic/mantissa routine made
  it possible to finish the lesson without deciding why `ln(e^x)` cancels while
  `log(e^x)` leaves a scale factor.
- At the denominator in `change-of-base`: the reversed quotient is a valid
  number, so only a power bracket or a derivation detects the error.
- Before the first logarithm in `solving-exponential-equations`: the learner
  must isolate, decide whether powers match and reject a non-positive target;
  seeing those decisions completed is not the same as making them.
- After condensing in `solving-logarithmic-equations`: a candidate can satisfy
  every transformed line while violating the original. The check must be
  rehearsed against the original arguments, not merely named.
- In `compound-interest-and-continuous-growth`: nominal rate, rate per period,
  number of periods and term all appear at once, and a calculator accepts every
  unit error.
- In `logarithmic-scales`: learners naturally subtract readings and report the
  difference as though the scale were linear, or add two decibel readings when
  the intensities are what add.

## Repairs made in this pass

All twelve lesson URLs and their order remain unchanged. No lesson was added,
removed, renamed or moved, so none of the five URL declarations changed.

- **Observable objectives:** the course home now names modelling, inverse
  interpretation, transformation, solution and scale comparison as observable
  acts. Every lesson syllabus line now names the classification, construction,
  conversion, sketch, expansion, evaluation, solution or comparison its
  completion standard measures.
- **Worked → faded → independent:** every worked panel now ends with a novel
  faded rehearsal. The first ratio, base, exponential rewrite, domain,
  quotient, isolation, period count or scale difference is supplied; the
  remaining work and check belong to the learner. Course-level directions make
  the intended order explicit.
- **Independent retrieval and diagnostic feedback:** the repeated `e` arithmetic
  item now asks what finite table evidence can establish, and the repeated
  interest-balance item now asks learners to choose a comparison by effective
  annual rate. New explanations identify the overgeneralisation or unit error
  behind every distractor.
- **Prerequisite repair:** `growth-and-decay` defers the logarithmic derivation
  of the rule of 70 until logarithms have been introduced. `the-number-e`
  scopes the factorial series in its lab as an optional independent check, not
  a learner method. `common-and-natural-logarithms` no longer requires floor
  notation or printed-table terminology.
- **Cognitive-load repair:** `common-and-natural-logarithms` now concentrates on
  the two hidden bases, their inverse identities, estimation and the fact that
  `ln` is convenient rather than uniquely legal for expressions involving
  `e`. Scientific notation remains only as a quick base-10 bracket, not the
  lesson's mastery target.
- **Correctness repair:** growth/decay language is scoped to positive starting
  quantities; any legal logarithm may be applied to an exponential equation;
  and `1 + 0.05/12` is preserved as an exact expression whose decimal should
  not be truncated early.
- **Misconception handling:** the existing warnings about invented logarithm
  laws, negative logarithm values, upside-down change-of-base quotients,
  extraneous candidates and addition on log scales remain. The new faded tasks
  force each of those warnings to be used before independent retrieval.

## Residual boundary

The course remains an Algebra course. It does not prove the analytic existence
of the limit defining `e`, derive the factorial series used internally by the
lab as a numerical cross-check, introduce complex logarithms, perform
log-linear regression, or teach the chemistry and psychophysics behind pH and
perceived loudness. Those boundaries are now explicit and none is required by
the completion standards.
