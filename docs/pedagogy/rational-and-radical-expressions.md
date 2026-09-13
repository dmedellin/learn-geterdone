# Pedagogy assessment — Rational and Radical Expressions (algebra, course 5)

**Second assessment. It supersedes `prior/rational-and-radical-expressions.md`
and it changes no source.** Nothing under `content/` or `site/` was touched:
the prose is settled and a contract snapshot is pinned to it, so every finding
below ends in a recommendation precise enough to execute later rather than in
an edit. The repairs the first pass describes are live on `main`, verified here,
and are not being reverted; where this pass disagrees with one of its claims,
the disagreement is recorded in *What this pass caught, and what it disputes*.

Formed from all twelve lesson dicts in `content/algebra/c5_rational/`
(`part_a.py`, `part_b.py`, `__init__.py`) as they stand on
`review/course-ui-standardization` at `d0a238a`, and from every lab kit the
lessons attach: the seven `rationalfn` modes and the `complex` mode in
`scripts/mathpath/labs/algebra_rational.py`, the four `radicals` modes in
`scripts/mathpath/labs/algebra_basics.py`, and the `radical` mode of
`grapher_lab` in `scripts/mathpath/labs/algebra_functions.py`. Every body block,
method step, worked example, faded rehearsal, quiz option, quiz explanation,
misconception, completion standard and lab configuration was read before
anything was written. Every displayed number was recomputed by hand. Every lab
claim below was checked against the JavaScript that ships — including the
expression parsers, which is where three of the findings live.

Lessons, in course order: `rational-expressions-and-their-domains`,
`simplifying-rational-expressions`,
`multiplying-and-dividing-rational-expressions`,
`adding-and-subtracting-rational-expressions`, `complex-fractions`,
`solving-rational-equations`, `graphs-and-asymptotes`,
`simplifying-radical-expressions`, `operations-with-radicals`,
`rationalizing-denominators`, `solving-radical-equations`,
`radical-functions-and-their-graphs`. 41 quiz items and 36 named misconceptions.

The course declares "Factoring and functions — factoring, domain inequalities,
and function notation". It is judged backwards against courses 1–4 and
**forwards against course 6**, because this is the middle link of a three-course
chain: Polynomials and Factoring feeds it the factored denominators every rule
in the first half is stated in terms of, and Quadratics and Complex Numbers
declares it as a prerequisite in turn. That forward check is where the most
serious finding in this assessment is, and it is not a finding about a sentence.

## What the course teaches well

- **One idea carries twelve lessons, and it is stated as an act on every one.**
  Write the excluded values down before the algebra starts, because the answer
  will not remember them. `rational-expressions-and-their-domains` `.standard`
  is "Finish when you write the exclusions before you write anything else";
  `simplifying-rational-expressions` shows `(x + 3)/(x + 4)` taking the value
  `6/7` at an `x` the original could not reach;
  `multiplying-and-dividing-rational-expressions` makes the divisor's numerator
  a third source of exclusions and shows it cancelling out of sight;
  `complex-fractions` finds a restriction that comes from no denominator at all
  (the lower half of `(1/x + 1/y)/(1/x − 1/y)` vanishing at `x = y`);
  `solving-rational-equations` turns the same fact into the definition of an
  extraneous root; `graphs-and-asymptotes` draws the hole it leaves; and the
  radical half repeats the move with an inequality in place of an equation. The
  `.note` of lesson 7 forecasts that transfer and the `.note` of lesson 12
  closes on it. Very few school courses have a through-line this strong, and
  this one earns it by naming the same act twelve times in twelve different
  situations rather than by asserting a theme.
- **The two irreversible steps are taught as one idea in two costumes, and the
  parallel is stated rather than left for the reader to notice.**
  `solving-rational-equations` `.body` theorem: "`A = B` implies `AM = BM`
  always. `AM = BM` implies `A = B` only when `M ≠ 0` … so the solution set can
  only grow, never shrink." `solving-radical-equations` `.body` theorem: "If
  `a = b` then `aⁿ = bⁿ` … For even `n`, `aⁿ = bⁿ` gives `a = ±b`." Both
  `.concepts[1]` say the extraneous root "is not a mistake"; lesson 6
  `.worked.after[1]` points forward to lesson 11 and lesson 11 `.body` opens by
  pointing back; and lesson 11 `.note` says outright that the two "are the same
  lesson in two costumes." Lesson 11 then goes one better and shows the
  extraneous root solving a *nameable* other equation
  (`√(x + 7) = −(x − 5)`), which converts "it failed the check" into "here is
  what it is a solution of."
- **The distractor hygiene is genuinely good, and better than the sibling
  courses'.** I argued for every wrong answer in all 41 items and could not
  defend one on the stem as written. Where an option is a true statement about
  the value, the stem names the criterion that rules it out:
  `simplifying-radical-expressions` `.quiz[2]` offers `2√18`, which *equals*
  `√72`, and the stem is "`√72` in simplified form is"; `complex-fractions`
  `.quiz[0]` offers the right expression with an incomplete restriction list and
  the stem says "and retain every restriction". That is exactly the discipline
  `content/AGENTS.md` asks for, and it is the discipline course 4 fails twice on
  its GCF lesson. It is worth recording as a strength precisely because it is
  the audit that most often turns something up.
- **The quiz feedback diagnoses distractors by name far more consistently than
  the sibling courses.** `rational-expressions-and-their-domains` `.quiz[0].why`
  works through all three ("Choosing `5` tests the numerator instead of the
  denominator; choosing `16` copies a constant without solving `x² = 16`;
  choosing all reals never tested the denominator");
  `multiplying-and-dividing-rational-expressions` `.quiz[1].why` explains why
  `x = 7` is excluded *and* why it stays visible, which is the actual content of
  the question; `radical-functions-and-their-graphs` `.quiz[0].why` names the
  un-reversed inequality, the lost sign and the negative radicand separately.
  Roughly three quarters of the items meet the standard. The exceptions are
  listed below, but they are exceptions.
- **The arithmetic is right, and the faded rehearsals were executed.** I
  recomputed all twelve. `(2x − 1)/(x² + x − 12)` keeps `1/2` and excludes
  `−4, 3`; `(x² − 16)/(x² + x − 20)` reduces to `(x + 4)/(x + 5)` with
  `x ≠ 4, −5`; `(x² − 1)/(x² + 3x + 2) ÷ (x − 1)/(x + 2)` is `1` with
  `x ≠ −2, −1, 1`; `2/(x² − x − 6) − 1/(x − 3)` is `−x/[(x − 3)(x + 2)]`, and
  the named wrong numerator `4 − x` really is what dropping the minus on the
  `+2` produces; `(1/x + 1/2)/(1/x − 1/2)` is `(x + 2)/(2 − x)` with
  `x ≠ 0, 2`; `1/(x − 1) + 1/(x + 1) = (x² − x + 2)/(x² − 1)` gives candidates
  `1` and `2` and solution `{2}`; `g(x) = (x² − 1)/(x² + x − 2)` has its hole at
  `(1, 2/3)`, asymptote `x = −2`, zero `−1`, horizontal asymptote `y = 1`;
  `√(18t²) = 3|t|√2` for every real `t`; `√12 + 2√27 − √75 = 3√3` and
  `(√6 + √2)(√6 − √2) = 4`; `2/∛9 = 2∛3/3` and `4/(3 + √5) = 3 − √5`, and the
  named wrong denominator `14 + 6√5` really is `(3 + √5)²`; `√(2x + 3) = x`
  gives `{3}`; `g(x) = −√(6 − 2x) + 1` has domain `x ≤ 3`, endpoint `(3, 1)`,
  range `y ≤ 1` and passes through `(1, −1)` and `(−5, −3)`. Every decimal check
  in the radical lessons is right to the digits shown. This matters more here
  than usual, because a course whose whole method is "check it" cannot afford a
  check that does not.
- **Misconceptions are named at the point of error and several are named twice,
  from different directions.** Excluding numerator zeros; reading the domain off
  the simplified form; `0/0` as a number; cancelling a term rather than a
  factor; missing an opposite pair; forgetting the divisor can be zero;
  looking for a common denominator in a product; subtracting only the first
  term of a numerator; adding denominators; multiplying only part of a complex
  fraction by the LCD; losing the main denominator's exclusion; a lower half
  that is zero without a denominator being zero; checking in the cleared
  equation; reporting no solution as an error; taking the domain from the
  cancelled form; substituting into the original to find a hole's height;
  assuming a graph never crosses its horizontal asymptote; `√(x²) = x`;
  distributing a root over a sum; `√9 = ±3`; adding radicands; judging likeness
  before simplifying; losing the middle term when squaring; multiplying a cube
  root by itself; negating the whole denominator instead of one sign; squaring
  term by term; squaring before isolating; reading a domain off the formula;
  forgetting to reverse an inequality; excluding the endpoint. Each is corrected
  with an instance, and `simplifying-rational-expressions` `.note` states the
  epistemics of the numerical check correctly — it "cannot confirm your answer,
  and it will reliably refute a wrong one."
- **The `rationalfn` lab's central design decision is the lesson.** It carries
  the reader's expression as an *unreduced* pair of polynomials plus the list of
  everything it divided by, and cancels only when a mode asks. The module
  docstring states why: "once `(x² − 4)/(x − 2)` has become `x + 2` there is
  nothing left in the formula that knows `x = 2` was ever forbidden, and every
  lab on this course would be quietly lying from that moment on." The hole in
  the graph is drawn from the same list. That is architecture serving pedagogy,
  and it is the reason `simplify` and `graph` cannot disagree about where a hole
  is.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson — here, one whole course — before it is taught

This is the section that matters. Courses 5 and 6 each declare the other's
material as available, and neither can be right.

1. **`radical-functions-and-their-graphs` requires quadratic sign analysis and
   attributes it to a course that does not teach it.** `.concepts[0][1]` reads:
   "Finding the domain is therefore an inequality problem from Linear Equations
   and Inequalities, and when `g` is a quadratic it is a sign-analysis problem
   from Polynomials and Factoring." The first half is true — course 2 has
   `linear-inequalities`. The second half is false. Polynomials and Factoring
   contains no inequality lesson and never states the theorem that licenses one
   test value per interval; the closest thing in it is the "sign of f" row in
   `graphs-of-polynomial-functions` `.worked`, which is presented as a *check*
   that multiplicities were read correctly, not as a method for solving
   anything. The technique this lesson needs is `quadratic-inequalities`, course
   6 lesson 13 — *after* this course. The lesson works around the gap with a
   one-off argument ("A product of two factors is non-negative when both have
   the same sign"), and then `.quiz[2]` asks the reader to run it unaided on
   `√(x² − 16)`, and `.worked` (b) and the faded rehearsal both depend on it. So
   the course assesses an act it does not teach and points at a course that does
   not teach it either.

2. **Course 6 returns the favour, which makes the dependency circular.**
   `quadratic-inequalities` `.note` (course 6 lesson 13) says: "Sign analysis is
   the same tool Rational and Radical Expressions used on rational expressions,
   with one addition there: the sign can also change where a denominator is
   zero, and that value is excluded rather than included." This course never
   analyses the sign of a rational expression. There is no rational-inequality
   lesson, and the phrase "sign analysis" occurs exactly once in
   `content/algebra/c5_rational/` — in the false attribution of item 1. Each
   course tells the reader the other one already did this. Neither did. A
   reader who follows either pointer arrives at nothing, and a reader who
   follows both arrives back where they started. This is the most serious
   finding in the assessment and it cannot be fixed inside one course. It is
   also the kind of defect a reference audit does not catch: the de-numbering
   commit `d0a238a` reports that "all 959 references resolve to a real lesson,
   and the cross-course ones are exact", and both of these *do* name a real
   course. They name the wrong one, which no check on the form of a reference
   can see.

3. **The `rationalfn` lab prints the discriminant, by name and with its value,
   in three of this course's lessons.** `zerosOf` in
   `scripts/mathpath/labs/algebra_rational.py` sends any leftover quadratic
   factor to `quadroots`, and `zerosentence` then emits "`(x² + 1)` has
   discriminant -4, so it is never 0 for a real x". That path is reachable on
   `rational-expressions-and-their-domains` (mode `domain`) from its own shipped
   preset 5, `1/(x^2 + 1)`, labelled "nothing is excluded". `solving-rational-equations`
   (mode `solve`) has two more: "the quadratic factor `(…)` has discriminant `D`,
   so it contributes no real candidate at all", and a status banner reading
   "whose discriminant is `D` — negative, so no real x satisfies it. Quadratics
   and Complex Numbers gives those roots a home." `graphs-and-asymptotes` (mode
   `graph`) shares the same helper. `b² − 4ac` is defined in course 6 lesson 6.

4. **The `radicals` lab does it a fourth time, in `solving-radical-equations`.**
   `SR_BODY["solve"]` pushes a step row headed "the discriminant of that
   quadratic" whenever the squared equation is a quadratic — which is the
   ordinary case, and is true of four of the six shipped presets. So four of
   this course's twelve lessons put the word *discriminant* and a number in
   front of a reader who has not met it, on pages whose own prose is careful to
   defer it: `solving-rational-equations` `.steps[2]` says in terms that "The
   quadratic formula arrives in Quadratics and Complex Numbers and is not
   required here."

5. **`rational-expressions-and-their-domains` `.note` endorses the crossing
   rather than fencing it.** "The lab names rational zeros as exact fractions
   and irrational zeros of quadratic factors as exact surds." Naming the
   irrational zeros of a quadratic exactly *is* the quadratic formula. The note
   is an accurate description of the lab — the first pass repaired it to be one,
   and that repair is good — but accuracy here documents the prerequisite
   violation instead of resolving it. The lesson has no way to explain where
   `(1 ± √3)/2` came from, and does not try.

6. **"Parabola" is used as a known object one course before it is defined.**
   `radical-functions-and-their-graphs` `.concepts[2]` ("half of a sideways
   parabola, not all of one"), `.body` theorem ("the upper half of the parabola
   `x = y²`") and `.quiz[3]`, whose distractors are "A parabola" and "Half a
   parabola, for `x ≥ 0` only" — so the reader has to *discriminate between two
   descriptions* of a curve the path has not named. The word occurs nowhere in
   courses 1–3; `graphs-of-quadratic-functions` (course 6 lesson 10) defines it:
   "The graph of a quadratic function is a curve called a parabola." Minor
   beside items 1–5, and on the same fault line.

### Facts a reader would trust that are wrong

7. The only outright false statements I found in this course are the two
   cross-course attributions of items 1 and 2. Every theorem, every worked
   line, every decimal check and every faded rehearsal is correct — see the
   fourth bullet above, which lists what was recomputed. That is worth stating
   plainly rather than leaving as an absence: on a generated path where
   `mathcheck.js` executes the labs' arithmetic but nothing executes the prose,
   twelve clean lessons is the outcome you want and not the one you get by
   default. The defects in this course are of placement and of interaction, not
   of mathematics.

### Distractors that are also true

8. None. I argued for every wrong answer in all 41 items against the stem as
   written and could not sustain one. Three come close and survive because the
   stem carries the criterion: `simplifying-radical-expressions` `.quiz[2]`
   ("in simplified form" rules out `2√18`, which is equal to `√72`);
   `complex-fractions` `.quiz[0]` ("and retain every restriction" rules out the
   option with the right expression and a short list);
   `adding-and-subtracting-rational-expressions` `.quiz[1]` (option `(3 − x + 1)/x`
   is the correct numerator left undistributed, and the stem's "equals" makes it
   an unfinished answer rather than a defensible one). The contrast with
   `factoring-out-the-greatest-common-factor` in course 4, where the same shape
   of question omits the criterion twice and the `why` has to concede the point,
   is instructive: this course's authors knew where to put the qualifier.

9. One stem has drifted the other way, into testing a qualifier instead of an
   act. `rationalizing-denominators` `.quiz[3]` reads "For the simplified
   numerical denominators in this lesson, rationalizing can change the value:"
   — a true/false about a scope condition, with a sixteen-word preamble
   protecting it. It is correct and it is the direct descendant of the first
   pass's item 7, which was a real correction. But the lesson has four
   questions and this is the only one that does not ask the reader to choose or
   produce a multiplier, so the repair spent a retrieval slot on a caveat. The
   act it should be measuring is in `.standard[1]`: "name the form of `1` before
   doing any arithmetic, and say what the denominator will become."

### Quiz feedback that does not answer the wrong answer

10. Three quarters of this course's `why` fields diagnose every distractor by
    name; the exceptions cluster in the radical half:
    - `simplifying-radical-expressions` `.quiz[0].why` ("What is `√(x²)`?")
      handles `x`, `±x` and `x²` — good — but `.quiz[1].why` groups `∛(−8)` and
      `∛(−1)` as "Both cube roots use odd indices and accept negatives" without
      distinguishing them, and a reader who picked one of the two is told about
      both.
    - `operations-with-radicals` `.quiz[0].why` says `2√5` "both combines unlike
      terms and invents a coefficient", which names two errors and attributes
      neither to a step the reader took. The lesson's own mistake 2 ("judging
      likeness before simplifying") is the model behind that answer and is not
      named.
    - `rationalizing-denominators` `.quiz[0].why` explains `3`, `√5` and `√15`
      — this one is a model. `.quiz[2].why` explains all three. So the lesson is
      inconsistent with itself rather than uniformly weak.
    - `solving-radical-equations` `.quiz[3].why` ("You should substitute your
      candidates into:") collapses "the squared equation" and "the factored
      quadratic" into one clause ("both derived lines that every candidate
      already satisfies"). They are the same error, so this is defensible; it is
      listed because the standard is *by name*, and a reader who chose "the
      factored quadratic" specifically may believe factoring changed something.
    - `graphs-and-asymptotes` `.quiz[0].why` is excellent and should be the
      template: it explains the hole, rules out the zero, rules out the ordinary
      point, and says why no vertical asymptote remains — four clauses, four
      options.

### Labs that do not agree with their own lessons

The `radicals` lab is numeric and single-radical. The `rationalfn` lab is
single-variable in `x`. Both are the right engineering decisions for an
exact-arithmetic core, and in four lessons the panel copy promises otherwise.

11. **`rationalizing-denominators`' lab cannot accept a cube root at all, and
    the cube root is the lesson's headline case.** The `rationalize` mode parses
    both boxes through `SVof`, whose function case reads:
    `if (node.v === 'sqrt') return SVsqrt(SVof(node.a)); throw new Error(node.v
    + '(...) is not part of this lesson; sqrt is')`. So `cbrt(2)` raises, and
    the lab prints "One of the two did not come out." Now look at what the
    lesson puts on that page: `.key[1]` is "1/∛2 = ∛4 / 2 — needs ∛4, not ∛2";
    `.body` gives "A higher index" its own `h3` and says "Here the reflex
    fails"; `.worked` line (b) is `1/∛2` and `.worked.after[0]` calls it "the
    one that separates the technique from the reflex"; the faded rehearsal is
    `2/∛9`; `.quiz[1]` is `1/∛5`; and `.mistakes[0]` is "Multiplying a cube root
    denominator by itself". The single idea the lesson is built around is the
    one input its lab refuses, and the error message tells the reader the idea
    "is not part of this lesson" — which is the opposite of true.

12. **`simplifying-radical-expressions`' lab takes a number, and the lesson's
    identity is about a variable.** `SR_FIELDS["simplify"]` is one field,
    "Radicand"; `SR_HINTS["simplify"]` says "a whole number or a fraction". The
    lesson's `thm` is `√(x²) = |x|` and it is called "The identity that catches
    everyone"; `.steps[2]` is "For an even index with a variable base, this is
    where `|x|` appears unless the domain already forces the base non-negative";
    `.worked` (c) is `√(48x⁵)`; `.worked.after[1]` turns on `√(50x³)` and when
    the bars survive; the faded rehearsal is `√(18t²) = 3|t|√2`; and `.quiz[0]`
    is `√(x²)`. The lab can do `√200` and `∛(−108)` — worked lines (a) and (b),
    and doing those well is worth something — and it can do nothing else on the
    page. The panel ("The factorisation of the radicand is shown as it is
    found") does not say so.

13. **`solving-radical-equations`' lab is hard-wired to one radical, and half
    the lesson is about two.** `SR_HINTS["solve"]` states the shape: "The
    equation is `sqrt(px + q) = rx + s`." The lesson's `.worked` (b) is
    `√(x + 5) − √x = 1`; `.steps[2]` is "Repeat if a radical remains";
    `.mistakes[1]` is "Squaring before isolating", argued on that same equation;
    and `.body` has an `h3` called "Two radicals". None of it can be entered.
    Separately, the lab's third preset is `sqrt(x + 7) = x + 5` and the lesson's
    worked example (a) is `√(x + 7) = x − 5` — the same equation with one sign
    changed, producing candidates `−3` and `−6` instead of `2` and `9`. A reader
    who picks the preset that looks like the worked example gets a different
    problem with the same *shape* (one solution, one extraneous) and different
    numbers, which is the most confusing possible near-miss.

14. **`complex-fractions`' lab is single-variable, and the lesson's second
    example and one of its three quiz questions are in two variables.**
    `ErfBuild` is called as `ErfBuild(tree, 'x', bans)` throughout
    `algebra_rational.py`; every `complex` preset is in `x`. The lesson's
    `.body` example "Two variables" is `(1/x + 1/y)/(1/x − 1/y)`, and it is the
    example that carries the lesson's third and best idea — a restriction
    (`x ≠ y`) that comes from no denominator at all. `.quiz[1]` is entirely
    about that expression. The panel says "The lab clears the same complex
    fraction twice … and prints the two results for comparison", which reads as
    a promise about any complex fraction.

15. **Two panels overwrite an accurate default with a less accurate one.** The
    `radicals` lab ships its own panel copy in `SR_PANEL`, and for `solve` it
    reads "Choose the four coefficients" — which tells the reader what the
    controls are. `solving-radical-equations` `.lab[1].panel_intro` replaces
    that with "The lab solves the squared equation and then substitutes each
    candidate back into the ORIGINAL" — true, valuable, and silent about the
    four boxes. The same happens on `rationalizing-denominators`, whose default
    would have said "Choose a numerator and a denominator". Overriding a panel
    is right when the lesson has something more specific to say; it should add
    to the control description, not replace it.

16. **Presets that miss the lesson's worked example.**
    `rational-expressions-and-their-domains` `.worked` is
    `(x + 1)/(x² − x − 6)`; the lab's "two exclusions" preset is
    `(x + 1)/(x² − 5x + 6)` — the same numerator with a different quadratic, so
    the exclusions are `2, 3` where the page says `3, −2`.
    `multiplying-and-dividing-rational-expressions` `.worked` divides by
    `(x² + 6x + 9)`; the lab's first preset divides by `(x² − 9)`.
    `simplifying-rational-expressions` `.worked` is `(x² − 9)/(x² + x − 12)` and
    the lab opens on `(x² − 4)/(x − 2)`. Where the preset does match — lesson 1
    opening on `(x² − 4)/(x − 2)`, which is the lesson's `key` line, and
    `graphs-and-asymptotes` offering `(x² − 4)/(x − 2)` as "a hole and no
    asymptote" — the page and the panel reinforce each other.

### Cognitive load and structure

17. **Twelve lessons, two halves, and the seam is handled well.**
    `graphs-and-asymptotes` `.note` closes the rational half by naming the
    pattern the radical half will repeat ("write the domain down first, then
    simplify, and expect the simplified form to have forgotten something …
    with squaring in place of cancelling"), and `simplifying-radical-expressions`
    opens by saying the same thing from the other side. That is the right way
    to spend a transition, and nothing needs to move.

18. **`simplifying-radical-expressions` is the heaviest page and is correctly
    not split.** Principal roots, even/odd index behaviour, `√(x²) = |x|`, the
    product and quotient rules with their hypotheses, simplified form, and
    variables under an even root. Six things — but `√(x²) = |x|` is the same
    fact as "even index needs a non-negative radicand" seen from the output
    side, the product rule's hypothesis is the same fact again, and the lesson
    says so. Recorded as a judgement.

19. **`complex-fractions` is the lesson with nothing of its own, and that is
    its point.** `.summary` says it outright: "Nothing new is needed here — only
    'Multiplying and Dividing Rational Expressions' and 'Adding and Subtracting
    Rational Expressions' applied in one of two orders." A lesson whose content
    is a *choice between two prior methods* is exactly what a retrieval-practice
    slot should look like at that point in a course, and its `.standard` ("do
    one both ways and get the same thing twice") is the strongest self-check
    standard in the three courses I read.

20. **The course home's `how_to[2]` is the only place the faded rehearsals are
    explained, and it is worth keeping.** "After each complete example, cover
    its answer and do the faded rehearsal before the quiz." Twelve lessons carry
    a rehearsal and none of them says what it is for; the course home does.
    Recorded because the sibling courses do the same thing and it is easy to
    lose in an edit.

## Where a learner gets stuck

- At `rationalizing-denominators`' lab, typing the lesson's own `1/cbrt(2)` and
  being told "cbrt(...) is not part of this lesson; sqrt is" (item 11).
- At `simplifying-radical-expressions`' faded rehearsal, wanting to check
  `√(18t²) = 3|t|√2` in the lab and finding a box that takes a number (item 12).
- At `solving-radical-equations`' worked example (b), wanting to watch the
  second squaring happen, and finding a lab that accepts one radical (item 13);
  and then picking the preset that looks like example (a) and getting different
  candidates because of one sign (item 13).
- At `complex-fractions`' second quiz question, which is about the two-variable
  expression, with a lab that works in `x` alone (item 14).
- At `radical-functions-and-their-graphs`' third quiz question, asked to solve
  `x² − 16 ≥ 0` by a method the lesson names, attributes to Polynomials and
  Factoring, and does not teach — because Polynomials and Factoring does not
  teach it either (item 1).
- At the same lesson's theorem, reading "the upper half of the parabola
  `x = y²`" without having met a parabola, and then being asked in `.quiz[3]` to
  tell "a parabola" from "half a parabola" (item 6).
- At `rational-expressions-and-their-domains`' fifth preset, reading "`x² + 1`
  has discriminant −4, so it is never 0 for a real x" on the first page of the
  course (item 3); and again at `solving-rational-equations`, on the lesson
  whose own method step says the quadratic formula is not required here
  (items 3–4).
- At `operations-with-radicals`' first quiz question, having chosen `2√5`, and
  being told two things are wrong with it without being told which step
  produced it (item 10).

## What this pass caught that the first missed, and what it disputes

The prior assessment (now `prior/rational-and-radical-expressions.md`) was a
careful audit of the prose and its repairs are live. Verified here: the
two-variable radical example that changed its own domain is gone —
`.worked` (c) is now `√(48x⁵)`, whose domain really is `x ≥ 0` (its item 9); the
hole definition now covers a denominator factor that cancels completely at any
numerator multiplicity, and `.quiz[0]` tests exactly the `(x − 2)²/[(x − 2)(x + 1)]`
case it named (its item 10); `.steps[2]` of lesson 12 now says "a linear
radicand usually gives one endpoint, while a quadratic may give two" (its item
11); `simplifying-radical-expressions` now requests the `simplify` mode rather
than `reduce`, so the panel and the lab describe the same act (its item 6);
`rationalizing-denominators` now scopes itself to simplified numerical
denominators and warns that `√2 − √2` is not a form of `1` (its item 7); the
course home now distinguishes even from odd indices (its item 5); and all twelve
lessons carry a faded rehearsal, every one of which I recomputed and found
correct (its item 1).

**Disputed.** Its "Prerequisite repair" states: "`solving-rational-equations`
now retrieves linear solving from Course 2 and factorable quadratics from Course
4. It neither invokes nor requires Course 6." The first two sentences are true
of the *prose*. The third is false of the *page*. The lab that lesson attaches
prints "the quadratic factor `(…)` has discriminant `D`" and "Quadratics and
Complex Numbers gives those roots a home" (item 3). Its methodology paragraph
says "The seven `rationalfn` modes, the four `radicals` modes used here and the
radical `grapher` mode were then checked against what their lesson panels
promised" — that check was run against the panels and not against the modes'
output, which is how four lessons kept a course-6 quantity on the page while the
assessment recorded the prerequisite as repaired.

**Also disputed, more importantly.** Its opening paragraph says "Courses 1–4
already teach the needed prerequisites", and the sibling assessment for course 6
says "course 5 supplies … sign analysis". Both are wrong in the same place, and
between them they close the loop: course 5's assessment says the prerequisite is
upstream, course 6's says it is in course 5, and neither course contains it
(items 1 and 2). This is the defect a per-course review is structurally least
likely to find and most likely to launder, and it is the reason the brief for
this pass asked for the backwards check to be done explicitly.

**Not attempted by the first pass.** Its item 3 — "Feedback was unevenly
diagnostic … A learner who added denominator zeros, lost a factor sign, copied
an output as an input or stopped before a final reduction was told the rule
again" — is the right observation and cites no lesson slug, no question and no
option, which makes it a critique that would fit any course. The per-distractor
audit is item 10 above. The "distractors that are also true" audit that
`content/AGENTS.md` names was not run either; running it here found nothing,
which is a result worth having (item 8) and one the first pass could not claim.
Its item 8 repaired the accuracy of lesson 1's `.note` without noticing that an
accurate description of that lab documents a course-6 computation (item 5). And
it did not reach the parsers: the cube root the `rationalize` mode cannot accept
(item 11), the numeric-only `simplify` mode (item 12), the single-radical
`solve` mode (item 13) and the single-variable `complex` mode (item 14) are all
findings about what the shipped JavaScript will take as input, and all four
remove a lesson's own worked example from its own lab.

## Repairs this pass recommends

None applied. All are inside the existing URL space — no lesson added, removed,
renamed or reordered — so the five URL declarations in `AGENTS.md` §1 are
untouched by every item below.

**The cross-course repair, which must be decided before the others** *(items 1
and 2)*. Three options, in order of preference:

- **A. Move sign analysis earlier and let both courses point at it.** The
  natural home is `graphs-of-polynomial-functions` (course 4 lesson 13), which
  already builds a sign row and already proves the sign-change mechanism in its
  `.body` ("`(x − c)` changes sign, so `(x − c)^k` changes sign exactly when `k`
  is odd. The other factors are non-zero near `c` and keep their signs"). Adding
  four lines that state the row as a method — the roots are the only places the
  sign can change, so one test value speaks for an interval — costs course 4 no
  new idea, gives `radical-functions-and-their-graphs` a true reference, and
  gives `quadratic-inequalities` a genuine "you have done this before". Then fix
  `radical-functions-and-their-graphs` `.concepts[0][1]` to cite that lesson by
  name, and `quadratic-inequalities` `.note` to say Polynomials and Factoring
  rather than Rational and Radical Expressions.
- **B. Keep the technique in course 6 and make course 5 honest.** Rewrite
  `radical-functions-and-their-graphs` `.concepts[0][1]` to say the quadratic
  case is settled here by one argument about the signs of two factors, and that
  `quadratic-inequalities` in Quadratics and Complex Numbers turns it into a
  method; and delete the false sentence from `quadratic-inequalities` `.note`.
  Cheapest, and it leaves `.quiz[2]` of lesson 12 assessing a one-off argument.
- **C. Do nothing and record it.** Not recommended: the two false attributions
  actively mislead, and a reader who chases either wastes a session.

**Content, `content/algebra/c5_rational/part_b.py`:**

- `radical-functions-and-their-graphs` `.concepts[0][1]` — per option A or B
  above. *(item 1)*
- `radical-functions-and-their-graphs` `.body` theorem and `.concepts[2]` — on
  first use of "parabola", add four words: "a parabola — the curve Quadratics
  and Complex Numbers is about". Alternatively change `.quiz[3]`'s distractors
  so the reader is not asked to tell two parabola descriptions apart before the
  word is defined. *(item 6)*
- `rationalizing-denominators` `.lab[1].panel_intro` — add the control
  description the override discarded, and fence the index limit: "Numerator and
  denominator in their own boxes. The lab reads `sqrt(...)` only, so the
  cube-root case above is one to do on paper." Reason: the reader currently
  meets an error message that says the lesson's main idea is not part of the
  lesson. *(items 11, 15)*
- `simplifying-radical-expressions` `.lab[1].panel_intro` — add "The radicand
  box takes a number, so the variable work above — `√(48x⁵)`, `√(50x³)` and the
  rehearsal — is on paper; the lab is for the numeric factorisation that sits
  underneath it." *(item 12)*
- `solving-radical-equations` `.lab[1].panel_intro` — restore the control
  description and fence the shape: "Set `p`, `q`, `r`, `s` in
  `√(px + q) = rx + s`. Example (b) has two radicals and is outside what this
  control can build." *(items 13, 15)*
- `complex-fractions` `.lab[1].panel_intro` — add "in `x`", so the two-variable
  example and `.quiz[1]` are not implied to be enterable. *(item 14)*
- `rationalizing-denominators` `.quiz[3]` — replace the true/false about scope
  with an act: "Which multiplier clears `2/(√7 − √3)`, and what does the
  denominator become?" with the conjugate, the same-sign binomial, `√7 + 3` and
  `√21` as options. Keep the scope sentence where it belongs, in `.body`, where
  it already is. *(item 9)*
- `operations-with-radicals` `.quiz[0].why` — name the model behind `2√5`:
  adding the radicands *and* the coefficients, which is what the lesson's
  mistake 1 and mistake 2 describe between them. *(item 10)*
- `simplifying-radical-expressions` `.quiz[1].why` — separate `∛(−8) = −2` from
  `∛(−1) = −1` instead of grouping them. *(item 10)*

**Content, `content/algebra/c5_rational/part_a.py`:**

- `rational-expressions-and-their-domains` `.note` — after the existing
  sentence, add one that fences the surds: "Naming the irrational zeros of a
  quadratic exactly is Quadratics and Complex Numbers' method; here they are
  reported so the domain is not overstated, and nothing on this course asks you
  to produce them." Reason: the note is accurate and the accuracy is the
  problem; one sentence converts an unexplained appearance into a deliberate
  one. *(items 3, 5)*
- `solving-rational-equations` `.lab[1].panel_intro` — same fence, in one
  clause, since the mode shows the discriminant on any equation whose cleared
  form is an irreducible quadratic. *(item 3)*
- Presets: change `RF_PRESETS["domain"][1]` to `(x + 1)/(x^2 - x - 6)` and
  `RF_PRESETS["simplify"][0]` to `(x^2 - 9)/(x^2 + x - 12)` in
  `scripts/mathpath/labs/algebra_rational.py`, so lessons 1 and 2 open on their
  own worked examples. *(item 16)*

**Labs** (run `node scripts/labcheck.js --generated` and
`node scripts/mathcheck.js` after any of these):

- `scripts/mathpath/labs/algebra_basics.py`, `SVof` — extend the `fn` case to
  accept `cbrt` (and optionally `root3`), mapping to an `SVcbrt`. This is the
  only change that makes `rationalizing-denominators` a coherent page, because
  the lesson's key identity, worked example (b), faded rehearsal and `.quiz[1]`
  are all cube roots. If the surd representation cannot carry a cube root
  cheaply, the fallback is the panel fence above, and the lesson should then say
  so in `.body` rather than leaving the reader to find the error message.
  *(item 11)*
- `scripts/mathpath/labs/algebra_basics.py`, `SR_PRESETS["solve"][2]` — change
  `("sqrt(x + 7) = x + 5", "1|7|1|5")` to `("sqrt(x + 7) = x - 5", "1|7|1|-5")`,
  which is `solving-radical-equations` `.worked` example (a) exactly, with
  candidates `2` and `9`. A one-character change that removes the worst
  near-miss in the three courses. *(item 13)*
- `scripts/mathpath/labs/algebra_rational.py`, `zerosentence` — when a quadratic
  factor has no real zero, print "is positive for every real `x`" (or negative,
  from the sign of the leading coefficient) instead of "has discriminant `D`, so
  it is never 0 for a real x". The conclusion is the same, the argument is the
  positivity argument `factoring-special-forms` already taught in course 4, and
  no course-6 quantity appears. Apply the same substitution to the two `solve`
  rows and the `solve` status banner. *(items 3, 4)*
- `scripts/mathpath/labs/algebra_basics.py`, `SR_BODY["solve"]` — drop the "the
  discriminant of that quadratic" step row, or gate it behind a `cfg` flag the
  way `algebra_quadratic.py` gates complex output with `SHOW_COMPLEX`. The
  gating pattern already exists in the codebase and was applied to exactly one
  quantity; this is the second. *(item 4)*

**Not recommended.** Do not make the `rationalfn` or `radicals` labs
multivariable; the exact core is `ℚ[x]` and three courses depend on it, so
fencing the limit in four panels is the proportionate repair. Do not split
`simplifying-radical-expressions` (item 18) or fold `complex-fractions` into its
neighbours (item 19). Do not rewrite the quiz feedback wholesale — three
quarters of it already meets the standard, and `graphs-and-asymptotes`
`.quiz[0].why` is the template the four exceptions should be brought up to.
