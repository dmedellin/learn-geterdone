# Pedagogy assessment — Polynomials and Factoring (algebra, course 4)

**Second assessment. It supersedes `prior/polynomials-and-factoring.md` and it
changes no source.** Nothing under `content/` or `site/` was touched in this
pass: the prose is settled and a contract snapshot is pinned to it, so every
finding below ends in a recommendation rather than an edit. The repairs the
first pass describes are live on `main` and are not being reverted; where this
pass disagrees with one of its claims, the disagreement is recorded in *What
this pass caught, and what it disputes*.

Formed from all thirteen lesson dicts in `content/algebra/c4_polynomials/`
(`part_a.py`, `part_b.py`, `__init__.py`) as they stand on
`review/course-ui-standardization` at `d0a238a`, and from the two lab kits the
lessons attach — `polynomial_lab` and `factoring_lab` in
`scripts/mathpath/labs/algebra_polynomials.py`, plus `grapher_lab` in
`scripts/mathpath/labs/algebra_functions.py`, which lesson 13 borrows. Every
body block, method step, worked example, faded rehearsal, quiz option, quiz
explanation, misconception, completion standard and lab configuration was read
before anything was written, and every lab claim below was checked against the
JavaScript that ships, not against the panel copy that describes it.

Lessons, in course order: `polynomials-degree-and-standard-form`,
`adding-and-subtracting-polynomials`, `multiplying-polynomials`,
`special-products`, `factoring-out-the-greatest-common-factor`,
`factoring-by-grouping`, `factoring-simple-trinomials`, `the-ac-method`,
`factoring-special-forms`, `polynomial-long-division`,
`synthetic-division-and-the-remainder-theorem`,
`the-factor-theorem-and-rational-roots`, `graphs-of-polynomial-functions`.
39 quiz items and 39 named misconceptions in all.

The course declares "Expressions and functions — exponents, distribution,
function notation" as its prerequisite, so it is judged against what courses 1–3
actually teach: integer and rational exponents, the distributive law, like
terms, exact substitution, function notation and graph reading. It is also
judged *forwards*, because courses 5 and 6 declare this one: Rational and
Radical Expressions needs factored denominators and a difference of squares on
almost every page, and Quadratics and Complex Numbers needs the ac search and
the multiplicity vocabulary. Those two directions are checked explicitly below,
because this is the head of a three-course dependency chain and a defect here
propagates twice.

## What the course teaches well

- **Every lesson closes on an act, and the act is what the worked example
  demonstrated.** Reject a non-polynomial and *name the exponent that spoils
  it* (`polynomials-degree-and-standard-form`); make a subtraction as safe as an
  addition by writing the negation on its own line
  (`adding-and-subtracting-polynomials`); state degree, leading term, constant
  term and product count *before* multiplying (`multiplying-polynomials`);
  produce `9x² − 25` without writing a middle term (`special-products`); take
  the GCF out without thinking and then ask which technique comes next
  (`factoring-out-the-greatest-common-factor`); say "grouping does not work
  here" without claiming more than that (`factoring-by-grouping`); defend a
  negative result by naming the pairs you tested (`factoring-simple-trinomials`);
  read an empty pair list as a result rather than a dead end (`the-ac-method`);
  refuse a sum of squares as confidently as you accept a difference
  (`factoring-special-forms`); write the full identity `f = dq + r` rather than
  a quotient (`polynomial-long-division`); state a remainder without dividing
  (`synthetic-division-and-the-remainder-theorem`); treat a complete search that
  finds nothing as a proof (`the-factor-theorem-and-rational-roots`); sketch from
  the factored form without plotting points (`graphs-of-polynomial-functions`).
  Not one of these is "understand X", and each names something a marker could
  watch happen.
- **The negative result is taught as a result, at the right scope, three times
  over.** `factoring-simple-trinomials` runs the divisor pairs of `1` to
  exhaustion on `x² + x + 1` and then argues separately why a monic trinomial
  cannot escape into the rationals; `the-ac-method` proves the converse it needs
  (`.body` theorem "Why an empty pair list rules out integer brackets": if
  `ax² + bx + c = (rx + s)(tx + u)` then the two middle products `ru` and `st`
  satisfy `mn = ac` and `m + n = b`, so any integer factorisation *must* appear
  on the list); `the-factor-theorem-and-rational-roots` exhausts eight candidates
  on `2x³ − 3x² − 8x − 3` and four on `x³ − 2` and states exactly what each
  empty list has and has not ruled out. The course home's `footer_lead` says the
  discipline out loud — "no rational linear factor is not the same claim as no
  factor of any kind" — and `not_covered[1]` volunteers the limit the search
  does not reach (a quartic with no rational root may still split into two
  quadratics). That is unusually honest for school algebra, and it is the
  course's best feature.
- **Checking is built into the method rather than recommended after it.**
  Substitution at `x = 1` in `adding-and-subtracting-polynomials`; the four
  free predictions (degree, leading term, constant term, product count) in
  `multiplying-polynomials`; expansion after every factorisation; the full
  division identity rather than the quotient in `polynomial-long-division`; and
  two checks of different kinds in
  `synthetic-division-and-the-remainder-theorem` — expanding
  `(x − 3)(2x² + x + 6) + 11` confirms the whole division, evaluating `f(3)`
  confirms only the remainder, and `.worked.after[0]` says which is which. These
  target different error classes and each is faster than redoing the work.
- **The arithmetic is right, and it is right in the places where it is
  load-bearing.** I recomputed every displayed number. The long division
  `2x⁴ − 3x³ + 5x − 1 ÷ (x² − x + 2)` gives `q = 2x² − x − 5`, `r = 2x + 9`, and
  the stated check `(x² − x + 2)(2x² − x − 5) = 2x⁴ − 3x³ + 3x − 10` is correct.
  Both synthetic rows are right (`2, 1, 6, 11` and `1, −2, 3, −11`), and both
  remainder-theorem confirmations (`f(3) = 11`, `g(−4) = −11`) check.
  `2x³ − 3x² − 8x − 3 = (x + 1)(2x + 1)(x − 3)` with roots `−1, −1/2, 3`, all
  three on the eight-candidate list, as the lesson claims. In
  `graphs-of-polynomial-functions` the expansion
  `(x + 2)(x − 1)²(x − 3) = x⁴ − 3x³ − 3x² + 11x − 6` is correct and all four
  sample values (`96, −6, −4, 54`) are right, as is the faded rehearsal's
  y-intercept `g(0) = 2`. The ac worked example's pair list for `72` is complete
  and its sums are right.
- **Misconceptions are named at the point of error and they are the real
  ones.** Reading degree before collecting; a fractional *coefficient* mistaken
  for a disqualifying exponent; a factored expression called "not a polynomial";
  distributing a minus to the first term only; adding exponents during addition
  and multiplying them during multiplication; trusting FOIL past a `2 × 2`;
  dropping the `2ab`; expecting `a² + ab + b²` to be a perfect square; dropping
  the quotient `1` in a GCF; extracting `+4` from a negative second pair;
  stopping at the first product; matching the product but not the sum; treating
  an exhausted search as an unfinished one; skipping the middle-term test;
  omitting `0x²`; using the sign printed in the divisor as `c`; reading the
  remainder as part of the quotient; getting `p` and `q` the wrong way round;
  drawing every root as a crossing; pretending a qualitative sketch locates
  every turn. Each is corrected with an instance, and several with a
  counterexample the reader can check in one line.
- **The factoring decision list is explicit, and grouping is made to earn its
  place twice.** `factoring-out-the-greatest-common-factor` makes the first move
  non-optional and says why (`.note`: `6x² + 15x + 6` is hard work until the `3`
  comes out); `factoring-by-grouping` tests pairings and distinguishes failure
  of a method from failure to factor; `the-ac-method` then deliberately splits a
  trinomial into four terms so grouping can finish it, and `factoring-by-grouping`
  `.note` forecasts that ("Getting the signs reliable now pays for itself two
  lessons from now"). Teaching one technique as the engine of a later one is
  better than teaching two techniques.
- **The forward references into courses 5 and 6 land on real lessons.**
  `polynomials-degree-and-standard-form` `.body` sends `2/x` and `√x` to Rational
  and Radical Expressions and `2ˣ` to Exponential and Logarithmic Functions —
  all three correct. `factoring-special-forms` `.note` says Rational and Radical
  Expressions "cancels a difference of squares out of a rational expression on
  almost every page" (true: `simplifying-rational-expressions`,
  `multiplying-and-dividing-rational-expressions` and `graphs-and-asymptotes` all
  do) and that Quadratics and Complex Numbers "returns to `a² + b²` once `i`
  exists and factors it properly" (true: `complex-roots-of-quadratics` factors
  `x² − 6x + 13` as `(x − 3 − 2i)(x − 3 + 2i)`). `the-factor-theorem-and-rational-roots`
  `.note` names exactly the three downstream consumers that exist. This is the
  half of the prerequisite check that usually fails on a generated path, and
  here it does not.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **`the-ac-method` `.quiz[2].why` still uses the discriminant, which this
   course's own home page says it does not teach.** The question is "No integer
   factor pair of `ac` sums to `b`. What follows?" and its explanation ends:
   "The pair search is complete, so an empty result is a proof. Equivalently
   `b² − 4ac` is not a perfect square." `b² − 4ac` is defined in Quadratics and
   Complex Numbers, two courses later, in `the-discriminant`; and
   `__init__.COURSE["not_covered"][0]` states in terms that "Quadratics and
   Complex Numbers teaches the discriminant, the quadratic formula and `i`; this
   course stops after proving that no rational factor exists." A reader who takes
   the `why` at face value now believes the finite search is trustworthy because
   of a later theorem, which is the precise inversion the lesson's own theorem
   was written to prevent — the search justifies itself from the two middle
   products of hypothetical brackets, and needs nothing from course 6. This is
   the only surviving discriminant reference in the course, and it survives in
   the one field a reader reads *after* getting the question wrong. The first
   pass claimed to have removed every one of them; see item 26.

2. **The `factoring` lab's grouping mode answers lesson 12's question on lesson
   6's page.** `factoring-by-grouping` `.body` ends on the example
   `x³ + x² + 2x + 6`, whose entire point is that the honest conclusion is
   "grouping fails here" and *not* "this does not factor" — the lesson says so
   explicitly, and adds that the second claim "needs 'The Factor Theorem and
   Rational Roots'." That polynomial is the lab's fifth preset, labelled
   "(grouping fails, nothing factors)", and `modeGrouping`'s no-winner branch
   prints the rational-root verdict on the spot: "Grouping fails, and this
   polynomial has no rational linear factor. … At degree 3 that settles it: a
   polynomial of this degree that factors at all must have a linear factor, and
   there is none, so `x³ + x² + 2x + 6` does not factor over the rationals."
   The verdict is true and the branch that prints it is well written; the
   problem is that it is on the page six lessons before the theorem that
   licenses it, on the one polynomial the lesson chose to teach restraint with.
   The reader is told to conclude less than the lab concludes, on the same
   screen, with no explanation of where the lab's extra knowledge came from. The
   non-four-term branch does the same thing more bluntly: "For the record, the
   full factorisation over the rationals of … is …, found by the rational root
   search rather than by grouping."

3. **`factoring-simple-trinomials` `.body` needs a result it defers to lesson
   12, and does not fence the gap.** The paragraph "Why a finite search settles
   the question" asserts that for a monic trinomial with integer coefficients,
   rational linear factors are necessarily integer ones, then says
   `the-factor-theorem-and-rational-roots` "proves this as part of the rational
   root theorem. For now, take it as the reason the search is trustworthy."
   Taking a theorem on credit is defensible; what makes it a defect here is that
   lesson 12 *does not* prove it. Its rational root theorem is stated for the
   general `p/q` case and its proof is not given at all — only the two-line
   factor theorem is proved. So the promissory note is never redeemed anywhere
   in the course, and the `.standard` of lesson 7 asks the reader to "defend a
   negative result" using a claim the course never establishes.

### Facts a reader would trust that are wrong

4. **`the-factor-theorem-and-rational-roots` `.worked.after[2]` names a wrong
   answer that no error produces.** The faded rehearsal is
   `2x³ − 3x² − 5x + 6` with `f(1) = 0` supplied, and it closes: "If your
   quotient is `2x² + x − 6`, the synthetic addition under the `−3` coefficient
   used the wrong sign." The correct row is `1 │ 2, −3, −5, 6 → 2, −1, −6, 0`,
   so the quotient is `2x² − x − 6` and the answer `(x − 1)(2x + 3)(x − 2)` is
   right. But the named error does not produce `2x² + x − 6`: treating `−3` as
   `+3` gives `2x² + 5x + …`, subtracting instead of adding gives `2x² − 5x + 0`
   with remainder `6`, and the only way to reach `+1` in that column is to use
   `c = 2`, which is a different mistake and yields `2x² + x − 3`. The
   diagnostic is the one sentence in the rehearsal a reader consults *because*
   they got it wrong, and it sends them to look for a sign error they did not
   make. The same defect recurs in the sibling courses (see the course 6
   assessment, item on `vertex-form-and-the-axis-of-symmetry`), which suggests
   these closing diagnostics were written without being executed.

5. **`the-ac-method` `.quiz[2].why`'s discriminant claim is also stated more
   broadly than it is true.** "No integer pair sums to `b`" is equivalent to
   "`b² − 4ac` is not a perfect square" only for a *primitive* trinomial; the
   lesson's own step 1 removes the content first, so the equivalence happens to
   hold on every example the course shows, but the sentence as printed carries
   no such condition. Given that the sentence should not be in a course-4 lesson
   at all (item 1), this is secondary — but the repair should not simply add the
   qualifier, it should delete the sentence.

### Distractors that are also true

The failure `content/AGENTS.md` warns about by name: "Before committing a
question, try to argue for each wrong answer. If you can, rewrite it." The data
model carries one `why` per question, so a defensible distractor is marked wrong
with an explanation that has to argue against a true statement — and in both
cases below, the `why` concedes the point in writing.

6. **`factoring-out-the-greatest-common-factor` `.quiz[0]`: "Factor
   `8x³ + 12x²`", with `2x²(4x + 6)` among the wrong answers.** Expand it:
   `8x³ + 12x²`. It is a factorisation of exactly the polynomial asked about.
   The question does not say "factor completely", and the lesson's own
   definition (`.body` def "Factoring") distinguishes *a* factorisation from a
   *complete* one. The `why` admits it — "The second option is true but
   incomplete" — which is the tell: a reader who answered it reasoned correctly
   about the instruction they were given. The fix is one word in the stem.

7. **The same lesson's `.quiz[1]`: "Factor `7x² + 7x`", with `7(x² + x)` among
   the wrong answers.** Same defect, in the same lesson, one question later.
   `7(x² + x)` expands to `7x² + 7x`, and the `why` again concedes it — "The
   last option is true but has not taken out the `x`." Two of the three
   questions on the lesson that introduces the word *greatest* are decided by a
   word the questions do not use. A reader who has internalised the lesson's
   actual content — that "greatest" is a further condition beyond "common" —
   has been given no way to express that in the answer.

8. **`the-ac-method` `.quiz[1]`, option (c), is defensible and unanswered.**
   The question is "Why may `bx` be replaced by `mx + nx`?" and option (c) is
   "Because factoring allows any regrouping of terms". `factoring-by-grouping`
   `.body` states, two lessons earlier, that "Rearranging terms of a sum is
   always legal", so a reader who read that lesson has been told something very
   close to (c) by the course itself. The correct answer (b) is better, and (c)
   is not the *reason*, but the `why` addresses only option (d) and leaves (a)
   and (c) undiagnosed — so the reader who chose (c) is told why `mn = ac` is
   not the licence, which is not their error.

### Quiz feedback that does not answer the wrong answer

9. The standard is that every distractor is diagnosed by name, because the
   reader who reaches the `why` reached it by choosing one. Roughly a third of
   this course's 39 items meet it — `the-ac-method` `.quiz[0]` is a model,
   working out the middle coefficient each wrong bracket actually produces
   (`−11`, `17`, `4`); `polynomial-long-division` `.quiz[2]` identifies the
   fourth option as the dividend's own coefficients copied out;
   `polynomials-degree-and-standard-form` `.quiz[2]` names `7` as the constant,
   `1` as the coefficient of `x²` and `5` as the degree. The rest restate the
   rule. Specifically:
   - `polynomials-degree-and-standard-form` `.quiz[0]` gives the general
     principle (exponents are restricted, coefficients are not) but never says
     which rule each of `x² + 2ˣ`, `4/x² + x` and `√x + x²` breaks — the three
     distinctions the lesson's `.body` bullet list was written to teach, and
     the exact act the `.standard` demands ("point at the specific exponent").
     `.quiz[1]` says nothing about `3`, `1` or `0`.
   - `special-products` `.quiz[0]` explains the cancellation but leaves
     `16x² + 9`, `16x² − 24x − 9` and `16x² − 12x − 9` unnamed. Those three
     encode three different models — the sum-of-squares error, applying the
     square pattern instead of the conjugate, and using `ab` where the identity
     needs `2ab` — and the third is the lesson's own mistake 2.
   - `factoring-by-grouping` `.quiz[0]` explains the right answer and says
     nothing about `(x² + 2)(x + 5)` (the brackets swapped),
     `(x + 2)(x² − 5)` (the second GCF's sign lost) or the claim that it does
     not factor by grouping — three distinct errors, one explanation.
   - `synthetic-division-and-the-remainder-theorem` `.quiz[0]` never mentions
     `1/5` or `−1/5`, which encode the reciprocal model — a reader who thinks
     `c` inverts the divisor is told the correct rule and not their error.
     `.quiz[1]` ignores "f has degree 0" and "f(0) = 2".
   - `the-factor-theorem-and-rational-roots` `.quiz[1]` is the worst of them.
     The distractor is `x + 2` — the sign error, the single most common failure
     of the factor theorem, and the one the lesson's `key` line is written to
     prevent — and the `why` does not mention it, nor "f has degree 2", nor "2
     is the only root".
   - `graphs-of-polynomial-functions` `.quiz[1]` leaves "vertical asymptote" and
     "`f` is undefined there" undiagnosed. Both are the rational-function model
     arriving early, and the course has a mistake entry for neither; naming them
     here would cost one clause and would pre-empt a confusion that
     `graphs-and-asymptotes` in course 5 has to clear up from scratch.
   - `factoring-simple-trinomials` `.quiz[1]` gives the sign reasoning but does
     not say that `(x − 2)(x + 10)` has product `−20` and sum `+8`, which is the
     product-matched-sum-missed model the lesson's mistake 1 names.

### Labs that do not agree with their own lessons

The `factoring_lab` has one text box, labelled "The polynomial", plus a preset
select. The `polynomial_lab` has one or two boxes and, in one mode, a pattern
selector. Four lesson panels describe controls that do not exist, and both labs
refuse the variables three lessons teach in.

10. **`factoring-simple-trinomials` `.lab[1].panel_intro`: "Enter `b` and `c`.
    … Try `b = 1`, `c = 1`."** There are no `b` and `c` boxes. The reader types
    a whole polynomial, and the instruction as written cannot be carried out.
    The intended experience — watching a complete search come back empty, which
    the `.note` calls "the point of it" — requires typing `x^2 + x + 1`, which
    is preset 4, and nothing on the page says so.

11. **`the-ac-method` `.lab[1].panel_intro`: "Enter `a`, `b` and `c`. … Try
    `2x² + 3x + 4` and watch the list run out with nothing marked."** Same
    defect. There is one box. Worse, `2x² + 3x + 4` is the lesson's own
    `.body` example of an empty search and it is *not* in the preset list; the
    lab's "no pair works" preset is `3x² + 2x + 5`. So the reader is told to
    enter three numbers into a single box and to look for a polynomial that is
    not offered.

12. **`the-factor-theorem-and-rational-roots` `.lab[1].panel_intro`: "Enter the
    coefficients."** One box, taking an expression. The rest of the sentence is
    accurate and the mode is excellent — it builds the divisor lists, forms
    every `± p/q`, de-duplicates and evaluates each in exact fractions — so the
    only thing wrong is the first three words, and they are the ones that tell
    the reader what to do.

13. **`synthetic-division-and-the-remainder-theorem` `.lab[1].panel_intro`:
    "Enter the coefficients and a value of `c`."** Half right: `c` is a real
    field, but `f` is a polynomial box, not a coefficient list. The distinction
    matters in this lesson more than elsewhere, because the lesson's mistake 2
    is about *writing the zero coefficients into the row* and the lab's own
    "The zeros are not optional" block explains it — a reader told to enter
    coefficients may well try to type `1, 0, 0, -8`.

14. **The `factoring` lab's gcf mode contradicts the integer-content convention
    the lesson exists to establish.** `factoring-out-the-greatest-common-factor`
    `.body` states it — "Problems in this course use integer coefficients for
    the GCF decision" — and `.mistakes[1]` is built on it: pulling a `3` out of
    `6x³ + 9x² + 4x` "is an algebraically true rational rescaling, but not an
    integer GCF." The lab's fourth shipped preset is
    `(1/2)x^2 + (3/4)x   (fractions)`, and `modeGcf` clears the denominators,
    reports "the greatest of them … over the common denominator 4, so the
    numerical factor is 1/4", and prints `(1/4)x(2x + 3)` as *the* common
    factor, verified. That is precisely the rational rescaling the lesson has
    just refused to call a GCF, offered as a preset on the same page, with no
    sentence reconciling the two. The lesson's own panel says "Type a polynomial
    with integer coefficients", which is advice the preset list contradicts in
    one click.

15. **The same panel promises multivariable behaviour the lab refuses, and the
    refusal takes out the lesson's worked example, its key line and one of its
    three quiz questions.** `.lab[1].panel_intro` says the lab "computes the gcd
    of the coefficients and the lowest power of each variable". There is one
    variable: `readPoly`/`whyNotPoly` in `algebra_polynomials.py` rejects
    anything else with "the letter 'y' is a second variable, and these labs work
    in x alone". The lesson's `key[2]` is
    `12x⁴y − 18x³y² + 6x³y = 6x³y(2x − 3y + 1)`; its entire `.worked` block is
    that polynomial; `.steps[1]` is "For each variable, take the lowest power
    that appears in every term"; and `.quiz[2]` asks for the GCF of `10x³y`,
    `15x²` and `25x²y²`. None of it can be entered. The reader who types the
    lesson's headline example gets an error message.

16. **The same single-variable limit hits two more lessons.**
    `polynomials-degree-and-standard-form` `.worked` line 2 is
    `4x²y − 3xy + y³`, and its `.body` def explains that a multivariable term's
    degree is the *sum* of the exponents (`4x²y` has degree 3) — a rule the lab
    cannot demonstrate and cannot check. `factoring-by-grouping` `.body`'s
    regrouping section is `ax + by + ay + bx`, in four letters, none of them
    `x` in the lab's sense; the one idea in that lesson that requires trying a
    second pairing is the one idea the lab cannot be shown. Taken with item 15,
    the pattern is course-wide: the prose teaches polynomials in several
    variables and every lab is an exact-arithmetic engine over `ℚ[x]`. That is a
    defensible engineering decision, but no lesson says so, and three panels
    imply the opposite.

17. **`special-products`' lab cannot expand two of the five identities the
    lesson puts in its `key`.** The lesson's `key` lists the conjugate product,
    both squares, and both cube identities
    (`(a + b)(a² − ab + b²) = a³ + b³` and its partner); `.note` calls those
    five "the only things in the course worth committing to memory"; `.steps[2]`
    is a test for the cube pattern; and `.worked` line 4 is
    `(x + 2)(x² − 2x + 4) = x³ + 8`. The `polynomial_lab`'s `special` mode
    offers exactly five patterns — `sqsum`, `sqdiff`, `conj`, `cubesum`,
    `cubediff` — and the last two are `(A ± B)³`, the *cube of a binomial*,
    which the lesson mentions in a single aside ("Also worth having"). So the
    lab's dropdown has five entries, the lesson has five identities, and two of
    them do not correspond: a reader looking for the sum of cubes finds
    `(A + B)^3` and gets `x³ + 6x² + 12x + 8` where the worked example says
    `x³ + 8`. The lab's own `PATTERNS.cubesum.lesson` string knows the
    difference and says so — "A^3 + B^3 … is the FACTORISATION of a sum of
    cubes that has the familiar bracket, not the expansion of a cube" — which
    makes this a gap in the mode list rather than a misunderstanding.

18. **Several labs do not open on the lesson's worked example, and one preset is
    a near-miss.** `factoring-by-grouping`'s worked example A is
    `x³ + 3x² − 4x − 12`; the lab opens on `x³ + 3x² + 2x + 6`.
    `factoring-simple-trinomials`' worked example A is `x² − 7x + 12`; the lab
    opens on `x² + 7x + 12` — the same polynomial with the sign of `b` flipped,
    so the reader comparing the page with the panel sees a different pair list
    and a different answer to what looks like the same question.
    `factoring-out-the-greatest-common-factor` opens on `6x³ + 9x² − 15x`,
    which is not on the page at all. Where a preset does match — `the-ac-method`
    opening on `6x² + 11x + 3`, `factoring-special-forms` offering `x³ − 8` and
    `x⁴ − 16`, `graphs-of-polynomial-functions` opening on the worked *and*
    faded polynomials — the page and the panel reinforce each other, which is
    the argument for doing it everywhere.

### Cognitive load and structure

19. **Thirteen lessons, and the load is well distributed except at lesson 12.**
    `the-factor-theorem-and-rational-roots` carries the factor theorem with a
    two-direction proof, the rational root theorem, the candidate-generation
    procedure, the divide-and-repeat loop, the stop-at-degree-2 rule, the
    empty-search scope statement and the root-count bound — seven things, of
    which two are new theorems and one is a new algorithm. It is the heaviest
    page in the course and the `.note` says as much ("This is the lesson the
    course was arranged around"). I do not recommend splitting it: the factor
    theorem is one line from the remainder theorem the previous lesson proved,
    the rational root theorem is only used as a list generator, and the quiz
    keeps its weight on the scope of an empty search rather than on the
    algorithm. Recorded as a judgement, not an oversight.

20. **`factoring-special-forms` is the natural split candidate and should not be
    split either.** Four patterns, a non-pattern, a coefficient-system qualifier
    and a retest rule. But the four patterns are the four `special-products`
    derived forwards, the retest rule is one idea applied to the output of the
    others, and the lab tests all four against one input and explains each
    verdict — which is the right shape for a recognition lesson. Recorded.

21. **The course home's outcome list omits division's most useful
    consequence.** `outcomes[2]` is "Divide polynomials — Carry out long
    division, use synthetic division where it applies, and read the remainder as
    a function value." Correct, but the act the course actually depends on is
    `.standard` of lesson 11: *state the remainder without dividing*. That is
    the act `the-factor-theorem-and-rational-roots` runs dozens of times, and it
    is the one thing the remainder theorem buys. It deserves to be the outcome.

22. **`graphs-of-polynomial-functions` is the only lesson whose closing act the
    lab cannot verify, and it is the only lesson whose lab was given custom
    presets.** The `.standard` is "sketch from the factored form without
    plotting points … using sample values only to confirm the signs, never to
    discover them." The grapher evaluates and draws; there is nothing on the
    page that lets a reader submit a sketch and be told what is wrong with it.
    The presets fix the *inputs* (the worked and faded polynomials are both
    there, which is right) but there is no faded-to-independent rung. This is a
    limit of the medium rather than a defect of the lesson, and it is worth
    recording because it is the only place in the course where the closing
    standard and the shipped interaction do not meet.

## Where a learner gets stuck

- At `factoring-out-the-greatest-common-factor`'s lab, typing the lesson's own
  `12x^4y - 18x^3y^2 + 6x^3y` and being told it is not a polynomial in `x`
  (item 15); and then, one preset over, being shown `(1/4)x` offered as a
  common factor on a page that has just said a rational rescaling is not one
  (item 14).
- At the same lesson's first two quiz questions, having chosen a factorisation
  that is a factorisation, and being told it is wrong for a reason the question
  never asked about (items 6 and 7).
- At `factoring-simple-trinomials`' and `the-ac-method`'s panels, looking for
  the `b` and `c` boxes the page says to fill in (items 10 and 11).
- At `special-products`' lab, wanting to watch `(x + 2)(x² − 2x + 4)` collapse
  to `x³ + 8` — which `.worked.after[1]` says is "worth expanding by hand once"
  — and finding that the dropdown's cube entries expand something else
  (item 17).
- At `factoring-by-grouping`'s fifth preset, reading "this polynomial has no
  rational linear factor … it does not factor over the rationals" beside a
  lesson that has just insisted the honest conclusion is only "grouping fails
  here" (item 2).
- At `the-ac-method`'s third quiz question, having answered it correctly, and
  being handed `b² − 4ac` as the real reason — two courses before it is defined,
  and in direct contradiction of the course home (item 1).
- At `the-factor-theorem-and-rational-roots`' faded rehearsal, hunting for a
  sign error under the `−3` coefficient that cannot produce the quotient the
  text says it produces (item 4).
- At `the-factor-theorem-and-rational-roots`' second quiz question, having
  answered `x + 2`, and being told what the factor theorem says rather than why
  the sign is the other way round (item 9).

## What this pass caught that the first missed, and what it disputes

The prior assessment (now `prior/polynomials-and-factoring.md`) was a competent
audit of the *prose*, and most of its repairs are live and verified here. Its
domain-discipline work is the best of it: the integer-content convention is
stated in `factoring-out-the-greatest-common-factor` `.body`; the coefficient
system is named at each point it matters in lessons 7, 8, 9 and 12; the course
home now excludes an arbitrary quartic algorithm by name. Its negative-result
repairs landed: `factoring-special-forms` `.concepts[1]` now distinguishes a
failed conjugate pattern from irreducibility and proves the `x² + b²` case by
positivity; the grouping lab's empty branch says "no rational linear factor";
the rational-root lab separates the cubic guarantee from the unresolved
quadratic case. Its graph repairs landed: the unproved `n − 1` turning-point
bound is gone from key, method, worked example, quiz and misconceptions; the
lesson calls its output a qualitative sketch and says the data do not locate
every turn; the grapher presets open on the worked and faded polynomials. And
its faded-rehearsal programme landed in all thirteen lessons.

**Disputed.** Its repair summary states: "every discriminant and exact
quadratic-root use was removed from Course 4 content and from the trinomial,
ac, rational-root and polynomial-grapher outputs used here." The *lab* half is
true — I read `modeTrinomial`, `modeAc`, `modeRoots` and the grapher's
polynomial branch and found no discriminant in any of them. The *content* half
is false: `the-ac-method` `.quiz[2].why` still says "Equivalently `b² − 4ac` is
not a perfect square" (item 1). One grep for `4ac` over
`content/algebra/c4_polynomials/` returns it. A claim of exhaustive removal that
misses the single remaining instance is worse than no claim, because it
discourages the next reader from looking.

**Not attempted by the first pass.** Its methodology says the lab modes "were
then checked against the acts and conclusions their lesson panels promised" —
that is the right check, and it was run in one direction only. It caught the
grapher panel asking for roots and multiplicities that the control does not
accept, and it did not catch the same defect in four other panels (items 10–13),
the single-variable refusal that removes a whole worked example (items 15–16),
the missing cube-factorisation modes (item 17), or the preset that contradicts
the convention the pass itself introduced (item 14). Its item 11 groups
"several retrieval items repeated displayed arithmetic or assessed only a verbal
rule" — a real observation, but it names no option and no `why` field, and the
two audits `content/AGENTS.md` asks for by name were not run at all: no
distractor was argued for (items 6–8), and no `why` was checked against the
distractors it is supposed to diagnose (item 9). Its "New feedback identifies
the sign, exponent, missing product, pattern, coefficient-copy or wrong-`c`
model represented by the distractors" is true of some questions and not of the
ones listed in item 9, including the factor theorem's sign distractor.

**Confirmed and extended.** Its finding 10 — the worked-example progression
stopping before performance — was correct and its repair is present in all
thirteen lessons. What it could not have known is that two of those rehearsals
close on a diagnostic that does not reproduce (item 4 here, and the
corresponding item in the course 6 assessment): the rehearsals were added, and
at least two were not executed.

## Repairs this pass recommends

None of these is applied. All are inside the existing URL space — no lesson is
added, removed, renamed or reordered — so the five URL declarations in
`AGENTS.md` §1 are untouched by every item below. Each names the file, the
field, the change and the reason.

**Content, `content/algebra/c4_polynomials/part_b.py`:**

- `the-ac-method` `.quiz[2].why` — delete the final sentence "Equivalently
  `b² − 4ac` is not a perfect square." and replace it with the justification the
  lesson already proves: "Any integer-coefficient product `(rx + s)(tx + u)`
  would have produced the pair `ru`, `st` on the list above, and the list is
  exhausted." Reason: the course home's `not_covered[0]` promises the
  discriminant is course 6's; the substitute is the lesson's own theorem, so
  nothing is lost. *(item 1; this is the highest-priority repair in the
  course.)*
- `the-factor-theorem-and-rational-roots` `.worked.after[2]` — replace the final
  diagnostic. The correct quotient is `2x² − x − 6`; a reader who used `c = 2`
  instead of `c = 1` gets `2x² + x − 3`, and a reader who subtracted instead of
  adding gets `2x² − 5x` with remainder `6`. Name one of those and its cause
  instead of the unreachable `2x² + x − 6`. *(item 4)*
- `the-factor-theorem-and-rational-roots` `.lab[1].panel_intro` — "Enter the
  coefficients" → "Type a polynomial". *(item 12)*
- `the-ac-method` `.lab[1].panel_intro` — "Enter `a`, `b` and `c`" → "Type the
  trinomial"; and change the closing instruction from `2x² + 3x + 4` to
  `3x² + 2x + 5`, which is the shipped preset, or add `2x² + 3x + 4` to
  `FACTOR_PRESETS["ac"]` in `scripts/mathpath/labs/algebra_polynomials.py` so
  the lesson's own example is one click away. *(item 11)*
- `synthetic-division-and-the-remainder-theorem` `.lab[1].panel_intro` — "Enter
  the coefficients and a value of `c`" → "Type `f`, and a value of `c`", so the
  reader does not try to enter a coefficient list on the one page that teaches
  coefficient lists. *(item 13)*
- `the-factor-theorem-and-rational-roots` `.quiz[1].why` — add the sign
  diagnosis: `x + 2` is `x − (−2)`, so it is a factor exactly when `f(−2) = 0`,
  which is not what was given. Also name the other two options. *(item 9)*
- `synthetic-division-and-the-remainder-theorem` `.quiz[0].why` — add a clause
  naming `1/5` and `−1/5` as the reciprocal model: `c` is the number that makes
  the divisor zero, not the number that inverts it. *(item 9)*
- `graphs-of-polynomial-functions` `.quiz[1].why` — add a clause saying that a
  polynomial has no asymptotes and is defined at every real number, so options
  (c) and (d) describe a rational function; name Rational and Radical
  Expressions as where those arrive. *(item 9)*

**Content, `content/algebra/c4_polynomials/part_a.py`:**

- `factoring-out-the-greatest-common-factor` `.quiz[0].q` and `.quiz[1].q` —
  change "Factor" to "Factor completely" in both stems. This is the whole fix
  for items 6 and 7; the existing `why` text then diagnoses correctly instead of
  conceding. If a stronger question is wanted, replace `.quiz[0]`'s stem with
  "Which of these is the *greatest* common factor of `8x³ + 12x²`?" and keep the
  same options. *(items 6, 7)*
- `factoring-out-the-greatest-common-factor` `.lab[1].panel_intro` — replace
  "the lowest power of each variable" with "the lowest power of `x`", and add
  one sentence: "The lab works in `x` alone, so the two-variable example above
  is one to do on paper." Reason: the panel currently promises behaviour the lab
  refuses, on the lesson whose worked example is two-variable. *(items 15, 16)*
- `polynomials-degree-and-standard-form` `.lab[1].panel_intro` — add the same
  one-sentence fence, so line 2 of the worked example does not send a reader to
  a lab that rejects it. *(item 16)*
- `factoring-simple-trinomials` `.lab[1].panel_intro` — "Enter `b` and `c`. …
  Try `b = 1`, `c = 1`." → "Type a monic trinomial. … Try `x^2 + x + 1` and
  watch the list run out." *(item 10)*
- `factoring-simple-trinomials` `.body` — the paragraph beginning "'The Factor
  Theorem and Rational Roots' proves this as part of the rational root theorem"
  should either be honoured (add the three-line proof to lesson 12, below) or
  softened to "states", so the course does not promise a proof it never gives.
  *(item 3)*
- `factoring-by-grouping` `.lab[1].panel_intro` — add a sentence fencing the
  lab's extra knowledge: "When no pairing works the lab also reports what the
  rational-root search of 'The Factor Theorem and Rational Roots' finds. That is
  six lessons ahead; for now the conclusion this lesson supports is only that
  grouping failed." Reason: the lab's verdict is correct and worth keeping; what
  is missing is the sentence that tells the reader it comes from elsewhere.
  *(item 2)*
- `special-products` `.lab[1].panel_intro` — add "The dropdown's cube entries
  expand `(A ± B)³`; the sum and difference of cubes in the key are the *reverse*
  direction, and 'Factoring Special Forms' runs them." Reason: this is the
  cheapest fix for item 17 and needs no lab change. The better fix is below.
- `the-factor-theorem-and-rational-roots` `.body` — add a three-line proof of
  the rational root theorem after its statement (substitute `p/q`, multiply by
  `qⁿ`, read the divisibility off both ends). It costs no new idea, it redeems
  the promise lesson 7 makes, and it is the only theorem in the course that is
  stated and not proved. *(item 3)*
- `__init__.py` `outcomes[2]` — add the act the course actually uses: "…and read
  the remainder as a function value, so that a remainder can be stated without
  dividing." *(item 21)*

**Labs, `scripts/mathpath/labs/algebra_polynomials.py`** (shared with no other
course, but check `node scripts/labcheck.js --generated` and
`node scripts/mathcheck.js` after any change here):

- `POLY_PATTERN_OPTIONS` and `PATTERNS` — add two modes, `cubesumfac`
  (`(A + B)(A² − AB + B²) = A³ + B³`) and `cubedifffac`
  (`(A − B)(A² + AB + B²) = A³ − B³`), each with `factors` returning the two
  brackets and `naive` returning `(A + B)³` — which is exactly the confusion the
  pair creates, so the "wrong answer this identity is famous for" row writes
  itself. Then change the `special` preset `("(x + 2)^3", "x", "2", "cubesum")`
  to `("(x + 2)(x^2 - 2x + 4)", "x", "2", "cubesumfac")`, which is
  `special-products` `.worked` line 4. *(item 17)*
- `FACTOR_PRESETS["gcf"]` — remove `("(1/2)x^2 + (3/4)x   (fractions)", …)` or
  relabel it `"(1/2)x^2 + (3/4)x   (clear the denominators first)"` and have
  `modeGcf` say, when `den !== 1n`, that the factor it found is a rational
  rescaling and that the integer GCF is taken after clearing denominators —
  which is what `factoring-out-the-greatest-common-factor` `.body` instructs.
  *(item 14)*
- `FACTOR_PRESETS["grouping"][0]` → `x^3 + 3x^2 - 4x - 12`;
  `FACTOR_PRESETS["trinomial"][0]` → `x^2 - 7x + 12`;
  `FACTOR_PRESETS["gcf"][0]` → a polynomial from the lesson. Reason: a lab that
  opens on the worked example lets the page and the panel check each other, and
  the trinomial preset currently differs from the lesson's example by one sign,
  which is worse than differing entirely. *(item 18)*

**Not recommended.** Do not make the labs multivariable. The exact-arithmetic
core is `ℚ[x]`, three courses depend on it, and the cost is not justified by
three lessons' worth of two-variable examples — fencing the limit in the panels
(above) is the proportionate repair. Do not split
`the-factor-theorem-and-rational-roots` or `factoring-special-forms`; see items
19 and 20. Do not add a sketch-checking mode to the grapher for item 22; the
faded rehearsal already supplies the rung, and the lab's job there is to be the
metric picture the lesson says it is.
