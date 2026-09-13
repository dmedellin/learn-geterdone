# Pedagogy assessment — Sequences and Series (algebra, course 9)

**This assessment supersedes `docs/pedagogy/prior/sequences-and-series.md` and makes
no source change.** Nothing under `content/` or `site/` was edited in this pass: the
prose is settled and a downstream contract snapshot is pinned to it. The closing
section describes each repair precisely enough to execute later, and the section after
it records the delta against the superseded document.

Formed from all eleven lesson dicts in `content/algebra/c9_sequences/` (`part_a.py`
lessons 01–06, `part_b.py` lessons 07–11, plus `__init__.py`), read front to back,
together with `sequence_lab` in `scripts/mathpath/labs/algebra_systems.py` — all
eleven of its modes, their preset tables, field labels and the `paintGenterm`
rendering path — and the path-level `content/algebra/__init__.py`. Every number a
reader would trust was recomputed by hand. Because this course is the one that hands
off to another path, the two hand-off targets were opened as well:
`content/discrete_math/c3_induction/` and `content/discrete_math/c4_counting/`, along
with the Discrete Mathematics path page.

Lessons in course order: `sequences-and-recursion`, `sigma-notation`,
`arithmetic-sequences-and-series`, `geometric-sequences-and-series`,
`partial-sums-and-telescoping`, `infinite-geometric-series`,
`repeating-decimals-as-series`, `annuities-and-accumulated-payments`,
`pascals-triangle`, `the-binomial-theorem`, `the-general-term-of-an-expansion`.

The course declares `assumes_long` "exponents, functions, and exact fractions". It is
judged backwards against what the path actually delivered: functions and slope from
course 3, factoring and expansion of `(a + b)²` and `(a + b)³` from course 4, the
rational-or-irrational sorting of the reals from course 1, and — cited by name twice,
though not declared — exponential decay and compound interest from course 7. This
course does not use course 8, correctly.

## What the course teaches well

- **It never lets a check pass for a proof, and it says so every single time.** This
  is the course's organising virtue and it is unusually disciplined.
  `sequences-and-recursion` `.body[10]` produces the chord-and-regions sequence
  `1, 2, 4, 8, 16, 31` specifically so that five agreements stop feeling like
  certainty, and `.body[11]` then names what would settle it and where that lives.
  `arithmetic-sequences-and-series` proves `Sₙ` by pairing rather than asserting it.
  `geometric-sequences-and-series` `.worked.after[0]`: "Ten terms added directly agree
  with the formula exactly, which verifies this one instance — `a₁ = 3`, `r = 2`,
  `n = 10`. What makes the formula true for every `a₁` … is the `Sₙ − rSₙ`
  cancellation, not the check."
  `partial-sums-and-telescoping` `.worked.after[0]`, `infinite-geometric-series`
  `.worked.after[1]`, `repeating-decimals-as-series` `.worked.after[0]`,
  `annuities-and-accumulated-payments` `.worked.after[0]` and `pascals-triangle`
  `.worked.after[0]` each say the same thing about their own worked example. The
  course `footer_lead` promises every sum is computed twice and both printed, and the
  `standard` of the last lesson closes on it: "say exactly what a check has
  established and what it has not". That is the path's `material` clause turned into a
  habit rather than a disclaimer.
- **The edge cases are taught as part of the theorem, not as exceptions bolted on.**
  `geometric-sequences-and-series` handles `r = 1` (where the derivation's division is
  illegal and `Sₙ = na₁` by counting), `r = 0` (where the formula works and the
  *quotient* definition of `r` fails, so the multiplicative definition is the one that
  decides), and `r < 0`, and its `.body[7]` explains that `r = 1` produces `0 = 0` in
  the derivation — "contains no sum information" — rather than an undefined sum.
  `infinite-geometric-series` separates the all-zero series from `|r| < 1` in the
  theorem statement itself and its proof dispatches `|r| > 1`, `r = 1` and `r = −1`
  individually. `annuities-and-accumulated-payments` `.concepts[1][1]` then does the
  thing that makes all of it worth having: it names the *overcorrection* — "Refusing
  the formula because `r > 1` is an overcorrection: it withholds an exact answer to a
  question that has one" — and quiz question 3 tests exactly that. A reader who has
  over-learned `|r| < 1` is caught and corrected by name.
- **`partial-sums-and-telescoping` earns its place by unifying three things the
  reader already has.** `.concepts[2][1]` points out that
  `geometric-sequences-and-series`' `Sₙ − rSₙ` argument was a telescope; `.body[13]`
  proves it, putting `bₖ = a₁r^(k−1)` and recovering `Sₙ(1 − r) = a₁(1 − rⁿ)`; and the
  same block re-derives `1 + 3 + 5 + … = n²` with `bₖ = (k − 1)²`, which
  `arithmetic-sequences-and-series` got by pairing. It then refuses to overclaim:
  "A useful telescope has to reveal the sum from a `bₖ` that can be found without
  already knowing the partial sums; manufacturing one from the unknown answer would
  explain nothing." That sentence is the difference between a technique and a trick,
  and most treatments do not make it.
- **`infinite-geometric-series` makes "approaches" quantitative, which is the only
  honest way to do a limit without calculus.** `.concepts[2][1]` and the table in
  `.body[7]` give the gap `8 − Sₙ = 8(1/2)ⁿ` exactly and count the terms needed for
  `1/1000`: `8 − S₁₂ = 1/512`, `8 − S₁₃ = 1/1024`, so thirteen and no fewer. The
  worked example's third column is the signed gap `1/3 − Sₙ = (1/3)(−1/2)ⁿ`, which
  alternates, so the reader sees a limit approached from both sides. The `standard`
  then asks for the definition "without using the word 'add'". And `.body[9]` sets
  three wrong answers for `1 − 1 + 1 − 1 + …` side by side (`0`, `1`, `1/2`) and
  attributes all three to one illegal move, regrouping something that is not finite —
  with the harmonic series in `.body[10]` immediately afterwards to show what
  regrouping a *finite* partial sum is allowed to prove. That pair of paragraphs is
  the best writing in the course.
- **The applications are applications, not decoration.**
  `repeating-decimals-as-series` closes a loop opened in course 1: Foundations of
  Algebra asserted that a decimal terminates or repeats exactly when the number is
  rational, and `.body[15]` says "the geometric series is what turns the assertion
  into an argument", having proved both directions — the series for one, the
  remainder-recurrence argument in `.body[13]` for the other. It then constructs
  `0.101001000100001…` on demand. `annuities-and-accumulated-payments` puts every
  payment on its own clock, lists them backwards so the first term is `P`, and gets
  the accumulation from `Sₙ` with the letters changed; its `.body[6]` supplies two
  free checks (`n = 1` returns `P`; a positive rate cannot give less than `nP`) and
  its `.mistakes[1]` computes what the unit error actually costs — `69299` against
  `65` billion.
- **Quiz feedback is the best on the Algebra path.** Thirty-one of the thirty-three
  questions diagnose every distractor by name, and the diagnoses are causal rather
  than dismissive: `arithmetic-sequences-and-series` Q2 traces `1470`, `2850` and
  `1365` to three different slips (`n` steps instead of `n − 1`, a dropped `/2`, and
  `a₁` left out); `partial-sums-and-telescoping` Q2 explains that `19/20` "stops one
  bracket early: the last bracket is `1/20 − 1/21`, so `1/21` survives";
  `the-general-term-of-an-expansion` Q3 explains that `56` and `28` are the entries
  reached by rounding `k = 16/3` down and up, and adds that `28` *is* the constant
  term of a neighbouring expansion where the equation does have a whole-number
  solution. Two questions fall short and they are named in the relevant section below.
- **No distractor in the course is defensible.** I argued for every wrong answer in
  all thirty-three questions. The two that come closest are handled explicitly in
  their own `why`: `sequences-and-recursion` Q3 option (a), "Because it does not say
  what `a₀` is", is answered with "the missing piece is any one term, not specifically
  `a₀`"; `geometric-sequences-and-series` Q3 option (a), "It is not geometric because
  `0/0` is undefined", is answered with "a quotient is a diagnostic for nonzero terms
  rather than the definition". Given that `content/AGENTS.md` names this failure as one
  of the two that keep recurring, and given that the sibling courses 7 and 8 each have
  two or three, a clean result across thirty-three questions is a finding.
- **The arithmetic is right, including the parts that are easy to get wrong.**
  Everything was recomputed: the chord-and-regions counts; `2ⁿ⁺¹ − 1` against the
  recursion at `n = 6`; every sigma expansion and both re-indexings, including the
  `45 → 39` cost of shifting the limits without the summand; `a₂₀ = 81` and
  `S₂₀ = 860`; `S₁₀ = 3069` for `3, 6, 12, …` against the ten terms added;
  the telescoping partial sums `1/2, 2/3, 3/4, 4/5` and the two survivors;
  `8 − S₁₂ = 1/512`, `8 − S₁₃ = 1/1024`; `(9/10)¹⁰⁰ < 1/37000` (true, and tight —
  it is `2.656 × 10⁻⁵` against `2.703 × 10⁻⁵`); the harmonic bound `S₁₆ > 3`; the whole
  alternating worked example including the closed-form gap `(1/3)(−1/2)ⁿ`;
  `0.2454545… = 27/110` by both routes and `245/990 = 49/198 = 0.2474747…`;
  `0.25 = 0.24999…` via `6/25 + 1/100`; `1/13` having period six; the annuity total
  `6105.10`, the annuity-due `6715.61`, the perpetuity partial values
  `6144.57`, `9914.81` and `8.52`, and the `69299`-against-`65`-billion unit error;
  row sums and the `190` additions needed to reach `C(20,10) = 184756`;
  `(2x − 3)⁴` term by term; `C(9,6)·2³·(−3)⁶ = 489888` and the coincidence that the
  `k = 5` term is `−489888x³`; and `262440` as the coefficient of `x³` in `(x + 3)¹⁰`.
  Not one figure was wrong.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **The module labels contradict the course's own syllabus.** Lessons 1–4 carry
   `"module": "Sequences"`, lesson 5 alone carries `"module": "Arithmetic and
   geometric"`, and lessons 6–7 carry `"Infinite series"`. So the module named
   *Arithmetic and geometric* contains exactly one lesson, and that lesson —
   `partial-sums-and-telescoping` — is the one that is *not* about either family,
   while `arithmetic-sequences-and-series` and `geometric-sequences-and-series` sit
   under the generic heading. The course's own `syllabus_intro` groups them the other
   way: "Next the two standard families are classified and partial sums recovered or
   telescoped." The renderer draws module headings, so a reader scanning the syllabus
   sees a section boundary in the wrong place.
2. **`infinite-geometric-series`' proof outsources its one analytic step to a course
   that offered it as a picture.** `.body[5]`, second paragraph: "For `0 < |r| < 1`,
   Exponential and Logarithmic Functions's exponential-decay result says the positive
   sequence `|r|ⁿ` approaches `0`." Course 7 states no such result. What it has is
   `exponential-functions` `.body[9]` — "as `x` runs off to the left the values shrink
   without limit and the curve settles toward the horizontal line `y = 0` without
   arriving" — which is a description of an asymptote, plus `growth-and-decay`
   `.body[10]`, which reflects it to get decay. Both are true and neither is stated as
   a theorem with a name. The citation is therefore accurate in substance and
   overstated in form, and it is the load-bearing step of the course's central
   theorem: everything from lesson 6 to lesson 8 rests on `rⁿ → 0`. The honest options
   are to name it as a fact carried from course 7's graphs rather than as a "result",
   or to prove it here (for `|r| = p/q < 1` a two-line Bernoulli argument would do it
   with nothing the course lacks).
3. **The course declares a prerequisite list that omits two courses it cites by
   name.** `assumes_long` is "exponents, functions, and exact fractions". But
   `geometric-sequences-and-series` `.body[3]` and `infinite-geometric-series`
   `.body[5]` both cite Exponential and Logarithmic Functions, the second of them
   inside a proof (item 2); `annuities-and-accumulated-payments` is compound interest
   with the periods counted, which is course 7 lesson 11; and `the-binomial-theorem`
   `.body[0]` cites Polynomials and Factoring for `(a + b)²` and `(a + b)³`. A reader
   choosing where to start from the course home is told they need functions and
   exponents, and will meet a proof that leans on course 7.
4. `annuities-and-accumulated-payments`' `note` says "That is the last of the sums."
   Lesson 9 sums each row of Pascal's triangle and checks it against `2ⁿ`; lesson 10's
   theorem *is* a sum, written `Σ C(n,k) aⁿ⁻ᵏbᵏ`, and its `.body[9]` sums a row by
   setting `a = b = 1`. The sentence is a section transition doing duty as a claim,
   and it is false as a claim.
5. Two lessons close the course. `the-binomial-theorem`'s `note` ends with a
   peroration — "The algebra was the point, though. Every step of this path … was
   legal because some property of the real numbers said so, which is the thing
   Foundations of Algebra opened with" — and then `the-general-term-of-an-expansion`'s
   `note` opens "That closes the course" and delivers a second one. Both are good; one
   of them is in the wrong lesson.

### Facts a reader would trust that are wrong

6. **A lab preset on lesson 1 claims a mismatch it does not have.**
   `SEQ_PRESETS["define"][5]` is labelled *"a closed form that is nearly right, and
   parts company at n = 1"*, with `a1 = "5"`, `rec = "p + 3"`, `closed = "3n"`. The
   recursion generates `5, 8, 11, 14, 17, 20, 23, 26`; the closed form generates
   `3, 6, 9, 12, 15, 18, 21, 24`. They differ by `2` at **every** `n`, not at `n = 1`.
   This lands on `sequences-and-recursion`, the lesson whose entire second half is
   about testing a candidate closed form against terms it was not built from, and it
   is the one preset in the mode dedicated to that idea. A reader who selects it
   expecting a subtle disagreement at one index sees a table in which nothing matches,
   and has no way to tell whether the label, the lab or their own understanding is
   wrong. (The genuine "parts company at `n = 1`" phenomenon is taught two lessons
   later — `partial-sums-and-telescoping` `.body[5]`, where `Sₙ = n² + 5` gives
   `aₙ = 2n − 1` for `n ≥ 2` and `a₁ = 6` — so the course knows the shape and the
   preset is not it.)
7. **The path page says Systems and Matrices comes last, which would make this course
   eighth.** `content/algebra/__init__.py` `why_order[3]`: "Systems and matrices come
   last because row reduction is elimination performed on exact fractions." There are
   nine courses and this is the ninth. The same four-item list gives an ordering reason
   for Foundations, for the Equations-before-Functions decision, for Factoring's middle
   position and for Exponentials at seventh, and gives none at all for Sequences and
   Series — so the one course the list actively misplaces is also the one it never
   explains. `sequence_intro` has the same gap: it explains why Polynomials, Rational
   and Radical, Quadratics and Systems sit where they do and stops.

### Distractors that are also true

8. **None.** Recorded as a result rather than an omission: every wrong answer in all
   thirty-three questions was argued for, and none can be defended. The two nearest
   misses are pre-empted in their own `why` (see the seventh bullet of "What the
   course teaches well"). This is the audit `content/AGENTS.md` asks for and the
   course passes it outright, which neither of its two neighbours does.

### Labs that do not agree with their own lessons

The `sequence` lab is the best-matched kit on the Algebra path, and two of its modes
are exemplary: `SEQ_PRESETS["partial"][0]` is `1/(n(n+1))` with `bₙ = 1/n`, exactly
`partial-sums-and-telescoping`'s worked example, and preset `[5]` is the same term
with the *wrong* partner `1/(n+1)`, which is the panel's promise ("Hand it a split
that is wrong and it says which `n` the claim fails at") realised as a preset. All
four other telescoping partners in that mode were checked and all four are correct.
`SEQ_PRESETS["binomial"][1]` is `(2x − 3)^4`, exactly `the-binomial-theorem`'s worked
example. `SEQ_PRESETS["geometric"]` carries `r = 1`, `r = −1` and `r = 0`, exactly the
edge cases that lesson teaches, and `SEQ_PRESETS["infinite"]` carries all three
divergent cases the theorem's proof dispatches. Against that standard, three
mismatches stand out.

9. **`the-general-term-of-an-expansion`'s lab cannot accept a single one of the
   lesson's expressions.** `paintGenterm` parses both boxes with
   `Epolyof(ta, 'x')` — a polynomial parser — and its own failure message lists what
   it takes: "`x`, `2x`, `-3`, `x^2`, `-1/2`". Every expression in the lesson puts `x`
   in a denominator: the worked example `(2x² − 3/x)⁹`; `.concepts[1][1]`'s
   `(2x² − 3/x)⁹`; `.body[4]`'s table for `(x + 2/x)⁶`; `.body[5]`'s constant term of
   the same; `.body[7]`'s `(x² + 1/x)⁸`; quiz question 3's `(x² + 1/x)⁸`;
   `.mistakes[0]`'s `(2x² − 3/x)⁹`; and the faded rehearsal's `(x³ − 2/x)⁸`. All eight
   are rejected. The lesson's completion standard is "write the general term of any
   bracket, collect its power of `x` from both parts, solve for `k`, and say plainly
   when no such term exists" — and *collecting the power of `x` from both parts* is
   only a task when `b` carries a negative power, which is the one thing the lab
   cannot represent. What the lab can do is show `C(n,k)aⁿ⁻ᵏbᵏ` for a polynomial
   binomial, which is lesson 10's material.
10. **The same panel conflates two different "no such term" answers.**
    `.lab[1].panel_intro` ends "Set `k` past the exponent and read what it reports
    about a term that is not there." The lab's `k > n` branch does report that, well
    — the exponent on `a` would go negative and `C(n, k) = 0`. But the lesson's
    "no such term" is a different thing entirely: `16 − 3k = 0` gives `k = 16/3`, a
    `k` that is not a whole number, so the exponents step over `0` between the sixth
    and seventh terms. That is `.body[7]`, `.concepts[2]`, `.mistakes[1]` and quiz
    question 3 — the lesson's signature idea — and the lab never models it, because it
    does not solve exponent equations (the panel is honest about this: "solve the
    exponent equation for `k` yourself"). A reader who follows the panel's instruction
    learns the wrong one of the two.
11. **`annuities-and-accumulated-payments`' lab covers one of the lesson's three
    questions, and the lesson's own faded rehearsal needs one of the other two.** The
    `annuity` mode takes a payment, a rate per period and a period count, values each
    payment at the close, and prints `P[(1 + i)ⁿ − 1]/i` beside the total — the
    accumulated value. The lesson also teaches present value (`.body[7]`–`.body[10]`)
    and perpetuities (`.body[11]`–`.body[13]`), the course outcome 3 promises all
    three ("compute and check its accumulated value, present value **or** perpetuity
    value"), the lesson's `steps[1]` is a decision *between* accumulation and present
    value, and `.worked.after[2]` — the faded rehearsal, the thing the course
    `how_to[0]` tells the reader to do before the quiz — is a present-value pass:
    "value three end-of-year payments of `200` today at `25%` per year." None of it is
    reachable on the lab, and the panel does not say so.
12. Smaller instances, each one sentence or one preset from being right:
    - `infinite-geometric-series`' headline number is `13` terms to come within
      `1/1000` of the limit, computed for `a₁ = 4`, `r = 1/2`. The lab's first preset
      is `a₁ = 1`, `r = 1/2`, `tol = 1/1000`, for which the answer is `11`. The panel
      says "says how many terms it takes to come within the distance you chose" — true,
      and a reader arriving from `.body[7]` sees a different number with no explanation.
      Setting `a₁ = 4` reproduces the lesson exactly; nothing says so.
    - `sigma-notation`'s worked example shifts `Σ (3k − 1)` from `k = 2 … 6` *down* to
      `j = 1 … 5`. Every preset in `SEQ_PRESETS["sigma"]` that carries a shift starts
      at `lo = 1`, so the lesson's own direction of travel — moving a lower limit to
      `1`, which is what the `standard` asks for — has no example behind it.
    - `pascals-triangle`' panel says "Build it to row 10, highlight the entry `k = 3`
      in that row, and read off the number of ways to choose three people out of ten."
      `SEQ_PRESETS["pascal"][3]` is row 10 with `k = 5`. The instruction works, but the
      reader has to change a box the preset just set, and the lesson's own worked
      example reads `C(8,3) = 56` from row 8, which is not a preset either.
    - `repeating-decimals-as-series`' worked example is `0.2454545…` (head `2`, block
      `45`). The presets carry `0.1666…` and `0.1999…` for the delayed-block case and
      `0.135135…` for the plain one; `0.454545…`, which the lesson's body, its `key`
      and quiz question 3 all use, is not among them.

### Quiz feedback that does not answer the wrong answer

13. Two of thirty-three questions leave a distractor unnamed, and both are small:
    - `sequences-and-recursion` Q3 (`.quiz[2].why`) answers option (a) carefully and
      says nothing about "Because it cannot be turned into an explicit formula" or
      "Because doubling has no closed form" — both false, and the second is worth
      refuting on the page where `aₙ = 5·2ⁿ⁻¹` was just produced.
    - `the-binomial-theorem` Q2 (`.quiz[1].why`) explains `12` ("counting the exponent
      instead of the terms") and leaves `14` and `24` alone; `24` is `2n` and is the
      answer of a reader who has confused the number of terms with the `2ⁿ` products
      the lesson mentions two paragraphs earlier, which makes it the diagnostic one.

### Cognitive load and structure

14. **The most load-bearing lesson in the course has the thinnest reading.**
    `geometric-sequences-and-series` has an eight-block body, the shortest of the
    thirty-three lessons across courses 7, 8 and 9 (the next shortest is eleven).
    Everything from lesson 5 to lesson 8 depends on it: the telescoping identification
    in lesson 5, the whole of lesson 6, both directions of lesson 7, and all three
    annuity formulas in lesson 8. It carries the term formula, the finite-sum
    derivation, and three edge cases, and it does all of it in eight blocks with no
    worked example of a negative ratio in the body (the negative ratio appears only in
    the faded rehearsal and the quiz).
15. **`repeating-decimals-as-series` is the heaviest page in the course and carries
    three separate results.** A sixteen-block body holding: the block theorem with its
    proof; the shift-and-subtract method shown to be the same proof compressed;
    `0.999… = 1` with the two-names argument and the non-uniqueness of decimal names;
    and the converse — which fractions repeat — by the remainder-recurrence argument.
    Each is genuinely good and the third and fourth are independent of the first two.
    It is the strongest split candidate in the course, cutting at `.body[9]` ("`0.999…`
    and the number it is"). **I am not recommending the split**: it changes the URL
    space and needs the five-place update and `@site-architect`, and the lesson's real
    achievement is that all four results come out of one formula, which a split would
    hide. Recorded as a judgement.
16. **`annuities-and-accumulated-payments` carries three valuations and a units
    discipline on a fifteen-block body, with a lab that supports one of them** (item
    11) **and three quiz questions, of which one tests units and one tests the
    `|r| < 1` overcorrection.** So present value — two body blocks, an example, a step,
    and the faded rehearsal — is never retrieved.
17. **Every lesson has exactly three concepts, four method steps, three mistakes and
    three quiz questions.** That is the floor of the range
    `TestLessonDataMatchesTheRenderer` enforces, and no lesson in this course takes
    the room `content/AGENTS.md` says a lesson may earn. `geometric-sequences-and-series`
    (eight body blocks, four courses depending on it) and
    `repeating-decimals-as-series` (sixteen body blocks, three results) get the same
    three questions.
18. The ordering within the course is right and one decision in it is better than
    right: `partial-sums-and-telescoping` is placed *between* the two families and the
    infinite case, so that by the time `infinite-geometric-series` asks its question,
    `S₁, S₂, S₃, …` is already an object the reader has generated, tabulated and
    differenced. `.concepts[0][1]` makes the move explicit — "a rule assigning one
    number to each positive integer is a sequence by 'Sequences and Recursion's
    definition" — and `infinite-geometric-series` `.body[0]` picks it straight back up.
    Most treatments define the infinite sum before the reader has met the sequence of
    partial sums as a sequence, and then have to assert the definition.
19. The faded-rehearsal discipline is kept: all eleven `worked.after` blocks close
    with one, and they are the best-designed on the path — several supply a *strategic*
    move rather than a first line. `sequences-and-recursion` hands over `b₁ + 1` and
    `b₂ + 1` rather than the terms, which is the whole insight (`bₙ = 3ⁿ − 1`);
    `infinite-geometric-series` supplies the ratio and asks for the *signed* gap and
    which side of the limit `S₄` lies on; `pascals-triangle` supplies the two edge `1`s
    and nothing else.

## The hand-off to Discrete Mathematics

The course refers the reader to the other path three times, and the task of checking
those claims is the reason this section exists separately.

20. **Every hand-off names a course that exists and teaches what is claimed.**
    `sequences-and-recursion` `.body[11]` and `.worked.after[1]` send the reader to
    "the Induction and Recursion course on the Discrete Mathematics path" — that is
    `content/discrete_math/c3_induction/`, slug `induction-and-recursion`, and it
    contains `mathematical-induction`, `strong-induction` and, most to the point,
    `induction-with-sums-and-products`, which is exactly the technique this course
    declines to use. `pascals-triangle`'s proof (`.body[6]`, third paragraph) says
    "Stating that last step properly is what mathematical induction is for, and the
    Discrete Mathematics path does it" — true. `the-binomial-theorem`'s `note` sends
    `C(n,k)` to "the Combinatorics and Counting course", which is
    `content/discrete_math/c4_counting/` and contains both `binomial-coefficients` and
    its own `the-binomial-theorem`. The course home's `not_covered[2]` states the
    position plainly. All three claims are accurate, which is more than can be assumed.
21. **None of them mentions what stands in front of the target.** Induction and
    Recursion is the *third* course of the Discrete Mathematics path and declares
    `assumes_long` "proof technique and set notation"; Logic and Proof (14 lessons) and
    Sets, Relations, and Functions (14 lessons) come first. So a reader who follows
    `sequences-and-recursion`'s pointer to settle a closed form has 28 lessons to read
    before the one they were sent for. Combinatorics and Counting is the fourth course
    and declares "sets, functions and induction", so `the-binomial-theorem`'s pointer
    sits behind 40. Neither pointer says so, and both are phrased as though the target
    were a page to look up. The Discrete Mathematics path page is explicit that "Each
    course assumes the ones before it and nothing else", so the prerequisite is real.
22. **The hand-off is one-way.** Discrete Mathematics course 4 has its own
    `the-binomial-theorem` lesson and its own `binomial-coefficients`, and neither
    mentions Algebra. Grepping `content/discrete_math/c4_counting/` for any reference
    to the Algebra path returns nothing: the word "algebra" appears only as a common
    noun, in phrases like "prove identities without algebra". So the two paths teach
    the binomial theorem twice, once each, and a reader who has done both is told by
    neither. That is not this course's defect to repair — the rubric says a violation
    sitting in another course is recorded rather than reached into — but it is the
    context in which item 21's repair should be written.

## Where a learner gets stuck

- At `the-general-term-of-an-expansion`'s lab, typing `-3/x` — or `2/x`, or `1/x` —
  into the `b` box and being told it is "not a polynomial in `x` that I can read",
  having just read a lesson in which every example has exactly that shape (item 9).
- At the same lab, following the panel's instruction about "a term that is not there"
  and learning the `k > n` case instead of the `k = 16/3` case the lesson is about
  (item 10).
- At `sequences-and-recursion`'s lab, selecting the preset labelled "parts company at
  `n = 1`" and finding a table in which the two columns never agree (item 6).
- At `annuities-and-accumulated-payments`' faded rehearsal, told to value three
  payments *today*, on a page whose lab only values them at the close (item 11).
- At `infinite-geometric-series`' lab, having just read that `1/1000` takes thirteen
  terms, and reading `11` off the default preset (item 12).
- At `infinite-geometric-series`' proof, asked to accept `|r|ⁿ → 0` as "Exponential
  and Logarithmic Functions's exponential-decay result", and finding in course 7 a
  sentence about a curve settling toward a line (item 2).
- At `sequences-and-recursion`'s closing paragraph, sent to a Discrete Mathematics
  course that turns out to sit behind twenty-eight lessons of logic and set theory
  (item 21).
- At the syllabus, reading a module heading "Arithmetic and geometric" over a lesson
  about telescoping, with the two arithmetic and geometric lessons filed above it
  under "Sequences" (item 1).

## Repairs this pass recommends

No lesson is added, removed, renamed or reordered by any of these, so the five URL
declarations in `AGENTS.md` §1 are untouched. Items marked **(lab kit)** edit
`scripts/mathpath/labs/algebra_systems.py` and belong to `@chrome-renderer`;
everything else is `content/algebra/c9_sequences/`.

- **(lab kit) `paintGenterm`: accept a term with a negative power of `x`, or fence the
  lesson.** The substantive fix is to parse each box as a Laurent monomial rather than
  a polynomial — accept `c·x^m` with `m` any integer, which covers every expression in
  the lesson (`2x²`, `−3/x`, `x³`, `−2/x`, `x²`, `1/x`) and needs no general rational
  arithmetic, since the general term only ever multiplies two such monomials and adds
  their exponents. That also makes the exponent line the lesson is about — `18 − 3k` —
  computable and printable, which is what would let the panel's promise be kept. If
  that is out of scope, the cheap fix is **`.lab[1].panel_intro`**: say outright that
  the lab takes binomials whose two parts are `x` to a non-negative power, that the
  lesson's own `(2x² − 3/x)⁹` is outside it, and that what the lab shows is the
  coefficient table and the placement of one term. *Why:* item 9 — the lesson's
  completion standard currently has no widget behind it, and the widget it has teaches
  the previous lesson.
- **`the-general-term-of-an-expansion`.lab[1].panel_intro, last sentence:** replace
  "Set `k` past the exponent and read what it reports about a term that is not there"
  with a sentence that distinguishes the two cases — "Setting `k` past the exponent
  reports one kind of missing term, the one where `C(n, k) = 0`. The other kind, where
  the exponent equation has no whole-number solution and the powers of `x` step over
  the one you wanted, is worked on the page: the lab has no `k` to be given for it."
  *Why:* item 10.
- **(lab kit) `SEQ_PRESETS["define"][5]`: fix the preset or fix the label.** Either
  set `"closed": "3n + 2"` and relabel it "a closed form that agrees everywhere — test
  it at `n = 6` before believing it", or keep `3n` and relabel it "a closed form for a
  different sequence: every row disagrees". The first is better, because it gives
  lesson 1 the case its `.body[10]` is about (a formula that survives every check you
  make). *Why:* item 6 — the label is false as shipped, on the lesson about not
  trusting agreement.
- **(lab kit) `SEQ_PRESETS["annuity"]` and the panel:** the mode is accumulation only.
  Either add a `sense` field (`"accumulate"` / `"present"`) mirroring
  `SYS_PRESETS["linprog"]`'s existing `sense` key, and a sixth row in the payment
  table showing `P/(1 + i)ᵏ` when it is set to present value; or, if that is out of
  scope, amend **`annuities-and-accumulated-payments`.lab[1].panel_intro** to say
  "The lab values the payments at the close. Present value is the same list read the
  other way — divide by `(1 + i)` instead of multiplying — and a perpetuity is what
  the present-value series settles on; both are worked on the page." *Why:* item 11 —
  two of the course's three promised valuations and the lesson's own faded rehearsal
  have no figure.
- **Module labels:** change `partial-sums-and-telescoping`'s `"module"` from
  "Arithmetic and geometric" to "Sequences", and change
  `arithmetic-sequences-and-series` and `geometric-sequences-and-series` to
  "Arithmetic and geometric" — or, simpler and closer to `syllabus_intro`, set all of
  lessons 3, 4 and 5 to "Arithmetic and geometric" and leave 1 and 2 as "Sequences".
  *Why:* item 1 — the section boundary is currently drawn one lesson late.
- **`infinite-geometric-series`.body[5], second paragraph:** replace "Exponential and
  Logarithmic Functions's exponential-decay result says" with what course 7 actually
  provides — "Exponential and Logarithmic Functions drew this: for a base between `0`
  and `1` the curve settles toward `y = 0` without arriving, so the positive sequence
  `|r|ⁿ` is driven below any positive number you name." Optionally add the two-line
  Bernoulli argument for `|r| = 1/(1 + h)` with `h > 0`, since
  `(1 + h)ⁿ ≥ 1 + nh` needs nothing this course lacks and would make the central
  theorem self-contained. *Why:* item 2 — the course's most careful lesson currently
  cites a theorem that does not exist under that name.
- **`c9_sequences/__init__.py` `assumes_long`:** "exponents, functions, and exact
  fractions" becomes "exponents, functions, exact fractions, and the exponential decay
  of Exponential and Logarithmic Functions". Optionally extend `assumes_short` from
  "Functions and exponents" to "Functions, exponents and exponentials". *Why:* item 3.
- **`annuities-and-accumulated-payments`.note:** "That is the last of the sums"
  becomes "That is the last of the series". *Why:* item 4 — three lessons of sums
  follow.
- **`the-binomial-theorem`.note:** move the closing peroration ("The algebra was the
  point, though. Every step of this path…") to `the-general-term-of-an-expansion`'s
  `note`, merging it with the existing "That closes the course", and leave lesson 10's
  `note` with the forward pointer alone. *Why:* item 5.
- **`sequences-and-recursion`.body[11] and `the-binomial-theorem`.note:** name the
  position of each hand-off target. For induction: "…it is the subject of the
  Induction and Recursion course, which is the third course of the Discrete
  Mathematics path and assumes the two before it." For counting: "…the Combinatorics
  and Counting course, fourth on that path." *Why:* item 21 — both pointers currently
  read as page references and both are course references with prerequisites.
- **Two `why` fields gain one clause** (item 13): `sequences-and-recursion`.quiz[2]
  ("it *can* be turned into an explicit formula — `5·2ⁿ⁻¹` is one — once a first term
  is chosen"); `the-binomial-theorem`.quiz[1] ("`24` is `2n`, and `14` is `n + 2`;
  the count is `n + 1` because `k` runs from `0`").
- **Four panels or presets gain the lesson's own numbers** (item 12):
  `infinite-geometric-series`.lab[1].panel_intro — "Set `a₁ = 4` and `r = 1/2` and the
  lab is the reading's example: thirteen terms to come within `1/1000` of `8`, and no
  fewer"; **(lab kit)** add a `sigma` preset with `lo = 2`, `hi = 6`, `fk = "3k - 1"`
  and a shift that moves the lower limit down to `1`, which is the worked example;
  `pascals-triangle`.lab[1].panel_intro — change "row 10 … `k = 3`" to the preset's
  row 10, `k = 5`, or add a row-8/`k = 3` preset to match the worked example;
  **(lab kit)** add `0.454545…` (`pre` empty, `rep` `"45"`) to
  `SEQ_PRESETS["repeating"]`.
- **Path-level, recorded not fixed here:** `content/algebra/__init__.py`
  `why_order[3]` says Systems and Matrices comes last; it is eighth of nine, and this
  course is ninth with no stated reason for its position. A fifth `why_order` entry —
  sequences and series come last because an infinite sum needs a limit of partial
  sums, and the only limit the path can honestly reach is the one exponential decay
  already gave it — would fix both halves at once. Belongs in one commit with the
  sibling assessments (item 7).

## Delta against the superseded assessment

The prior document is at `docs/pedagogy/prior/sequences-and-series.md` (253 lines,
Codex lane). Its repairs are live on `main` and nothing here reverts them.

**What this pass caught that the first missed.**
- The first pass did not open the lab kit. Items 6 and 9–12 all live in
  `scripts/mathpath/labs/algebra_systems.py` or in the gap between a `panel_intro` and
  the widget beneath it, and two of them are the most serious findings in the course:
  a lab that cannot accept any of its lesson's eight expressions, and a preset whose
  label states a mismatch that is not there.
- The hand-off to Discrete Mathematics was not verified. This pass opened
  `content/discrete_math/c3_induction/` and `c4_counting/` and the Discrete
  Mathematics path page. The result is mixed and worth having both halves of: every
  hand-off claim is *accurate* (item 20), which is the harder thing to get right, and
  none of them mentions the 28 or 40 lessons standing in front of the target (item
  21), nor that the target course re-teaches the binomial theorem without
  acknowledgement (item 22).
- The distractor audit was not performed. Item 8 reports its result — thirty-three
  questions, no defensible wrong answer — which is a credit the first pass could not
  claim because it did not check.
- The per-distractor feedback audit was not performed. Item 13 reports two shortfalls
  out of thirty-three, which is the best figure on the path and is itself the finding.
- The prerequisite check backwards across the path is new: items 2 and 3 come from it
  (a cited "result" that course 7 never states as one, and a declared prerequisite
  list that omits two courses the text cites by name).
- The arithmetic was not previously checked. Every figure in the course was
  recomputed, including the tight inequality `(9/10)¹⁰⁰ < 1/37000`, the perpetuity
  partial values, the `65`-billion unit error and the `489888` coincidence between the
  `k = 5` and `k = 6` terms of `(2x² − 3/x)⁹`. None was wrong.
- The module-label defect (item 1), the "last of the sums" claim (item 4), the doubled
  peroration (item 5) and the path-page error (item 7) are all new.

**What the first pass claimed that this pass disputes.**
- The prior document treats `annuities-and-accumulated-payments` as a fully supported
  application. It is fully *taught* and one-third supported: the lab values payments
  only at the close, the course outcome promises three valuations, and the lesson's own
  faded rehearsal asks for one of the two the lab cannot do (item 11).
- The prior document does not distinguish between the two kinds of missing term in
  `the-general-term-of-an-expansion` and credits the lab with demonstrating the
  lesson's "no such term" case. The lab demonstrates the other one (item 10).
- Where the first pass credits the course with keeping "a check is not a proof"
  visible throughout, this pass agrees and can now say how thoroughly: seven separate
  `worked.after` blocks say it about their own worked example, and the last lesson's
  `standard` closes on it. Recorded rather than disputed, because it is the claim in
  the prior document that this pass can verify outright — and because it is the reason
  the one place the course *does* overstate a citation (item 2) is worth repairing
  rather than shrugging at.
