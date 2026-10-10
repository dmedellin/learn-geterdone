# Pedagogy assessment — Rates of Change and the Derivative (differential equations, course 1)

Formed from the eleven lesson dicts in `content/differential_equations/c1_rates/`
(`part_a.py`, lessons 1–6, and `part_b.py`, lessons 7–11, written by two
authors from `docs/differential-equations/PLAN.md` §C), the course dict in
`__init__.py`, the spoken forms in
`content/spoken/differential_equations_c1_rates.py`, and the pages as
`scripts/preview_subject.py` renders them, with every preset's tiles read off
the built page by `labcheck.js --observe` and every `data-say` attribute read
back. The course is the first on its path, so it may assume the Algebra Subject
and nothing else. All eleven lessons were read before any was changed, and
every figure quoted in prose was recomputed by hand before the tiles were
compared with it; the last two sections record what was changed and what was
not.

Lessons, in course order: `average-rate-of-change`,
`the-quotient-as-a-polynomial-in-h`, `what-the-quotients-approach`,
`the-derivative-at-a-point`, `the-derivative-of-one-over-t`,
`the-derivative-as-a-function` | `where-the-rate-is-zero`, `the-product-rule`,
`the-chain-rule`, `the-second-derivative`, `the-exponential-and-its-rate`. The
bar marks the seam between the two authors.

## What the course teaches well

- **The order is the argument.** Compute a quotient as a fraction
  (`average-rate-of-change`); notice the quotient of a polynomial is a
  polynomial in `h` and its constant term needs no limit
  (`the-quotient-as-a-polynomial-in-h`); only then ask what a column heads
  for, and separate the claim from the table (`what-the-quotients-approach`);
  name the number and attach a line with an exact error
  (`the-derivative-at-a-point`); do one function that is not a polynomial by
  hand (`the-derivative-of-one-over-t`); turn the point into a function
  (`the-derivative-as-a-function`). That is PLAN §0's "computed first and
  named second" carried out lesson by lesson, and it is the right order for a
  reader who has never met a limit: the hard idea (approach) arrives in lesson
  three, after two lessons in which everything is algebra the reader can
  check.
- **Every objective is an act and the closing `standard` measures it.**
  Compute the rate as a fraction and say which line has that slope; expand,
  cancel and name the constant term; produce the column, state the number and
  say what the claim covers; find `f′(a)`, write the line, compute the exact
  error; derive the quotient of `1/t` by combining fractions; differentiate
  term by term and read the sign; solve `p′ = 0` and sort the zeros by the sign
  change; differentiate a product by the rule and confirm against the
  expansion; differentiate a composition and confirm; differentiate twice and
  locate the inflections; factor the exponential's quotient and read the
  constant off a rounded column. None is "understand".
- **The figures are right, and the prose agrees with every tile.** All
  ninety-six pinned strings across eleven pages match the page (`labcheck`),
  the author's one deviation from §C's instances is an improvement (below), and
  every figure quoted in prose was recomputed: `3, 5/2, 9/4, 17/8, 33/16` and
  `2913/256` for the cubic (`average-rate-of-change`); `61/16` both ways
  (`the-quotient-as-a-polynomial-in-h`); `129/64`, `12481/4096` with gap
  `193/4096` (`what-the-quotients-approach`); `22/5` against `441/100`, error
  `1/100 = h²`; `13/10` against `1331/1000`, error `31/1000 = 3h² + h³`; `1/2`
  against `2/3`, error `1/6` (`the-derivative-at-a-point`); `−1/6, −1/5, −2/9,
  −4/17, −8/33, −16/65`, `−32/33`, `−64/17` (`the-derivative-of-one-over-t`);
  `3(t − 1)(t − 3)`, heights 4 and 0 (`the-derivative-as-a-function`);
  `6(t − 2)(t + 1)`, heights 8, −19 and 33 (`where-the-rate-is-zero`);
  `5t⁴ + 3t² − 2` by both routes and `6t³ − 2t` for the wrong rule
  (`the-product-rule`); `6t⁵ + 12t³ + 6t` by both routes, slope 24 at 1
  (`the-chain-rule`); slopes `0, −3, 0, 9`, inflections at 1 and at `±1`, the
  turns of the quartic at `±√3` left to the interval tile exactly as the lab
  prints them (`the-second-derivative`); `≈ 0.828427` as `2(√2 − 1)`,
  `≈ 0.696914` at `h = 1/64`, `ln 3 ≈ 1.09861`, `e − 1 ≈ 1.71828`,
  `8·ln 2 ≈ 5.54518` and `≈ 5.57531` for the last row at `a = 3`
  (`the-exponential-and-its-rate`).
- **The exactness rule is kept, and the one rounding lesson says so at every
  turn.** Ten lessons print nothing but fractions and polynomials with
  rational coefficients. `the-exponential-and-its-rate` opens by saying that
  for the first time some figures are rounded, marks every rounded row in its
  own table, has a mistake entry about quoting a rounded figure as exact, and
  states the convergence of the column as a claim ("stated and not proved"),
  which is exactly PLAN §0's position. The one slip (a rounded `5.54518`
  without `≈`) is recorded below and fixed.
- **The claim/evidence distinction is taught, not merely announced.**
  `what-the-quotients-approach` gives "approach" its sense (any bound, a step
  below which every quotient is within it), says no row equals 2, and then
  separates the polynomial case, where the algebra `2 + h` is a proof, from
  the case where the table is the only evidence. The same sentence recurs,
  shorter, in `the-derivative-at-a-point`, `the-derivative-of-one-over-t` and
  `the-exponential-and-its-rate`, each time where it matters. The lab's own
  banner says it too ("the claim that they approach it is about every h, not
  about the last row").
- **The misconceptions are the real ones and each is refuted with a specific
  fraction.** `f(a + h)/h` gives `9/2` and the forgotten division gives `5/4`
  where the rate is `5/2`; `h = 0` before cancelling is `0/0`; the limit is
  not `129/64`; the tangent "touches once" yet estimates `22/5` against
  `441/100`; `1/t` has no positive derivative because every quotient at 1 is
  negative; `(t³)′` is not `t²` because `t²` gives slope 1 where the quotients
  head for 3; `t³` has `p′ = 0` at 0 and no turn; `f′g′ = 2t` has the wrong
  degree; the missing 3 is the slope of `3t + 1`; the inflection of `t³ − 3t²`
  sits where `p′ = −3`; the power rule on `2ᵗ` gives 0 at `t = 0` where the
  column heads for `≈ 0.693147`. Every `mistakes[0]` is the §C misconception.
- **The proofs are the algebra the reader has, and nothing more.** The
  product rule's proof adds and subtracts `f(t)·g(t + h)` and reads constant
  terms; the chain rule's proof is the product rule applied `n` times; `1/t`
  is one common denominator. Each `thm` without a `proof` is followed by a
  paragraph that says what the lab shows and what it does not, as PLAN §E
  asks.
- **Retrieval practice is real.** Every quiz item has a `why` that names the
  error behind each wrong choice, and several questions test the idea at a
  place the lesson did not compute (`t²` over `[1, 3]`; `(2t + 5)³`;
  `t⁴`'s second derivative; the slopes `−4, −1, 3`). The recurring trap of
  this Subject, a distractor true at one value of `t`, was looked for and not
  found: no distractor is defensible.
- **The author improved on two of §C's instances.** §C's `wrong-rule` preset
  for `the-product-rule` repeats `basic`'s pair (`t²`, `t + 1`); the author
  used `t²` times `t²`, which is not a duplicate and (as of this pass) is used
  in the prose for the point it makes. `the-exponential-and-its-rate` has a
  fourth preset, `2ᵗ` at 3, whose ratio tile recovers the column at 0 and so
  demonstrates the "one column serves every place" claim the lesson rests on.

## What the course teaches badly, or wrongly

1. **`what-the-quotients-approach` named the derivative in a `thm` block and
   then told the reader the next lesson would name it.** The block read "that
   number is the derivative of `f` at `a`, written `f′(a)`", which is a
   definition and not a claim, and the closing note said "what the next lesson
   calls the derivative there". `the-derivative-at-a-point`'s `def` then
   defined it again. The `thm` is now the claim the lesson exists to state (the
   quotients of `t²` at 1 approach 2, with "approach" spelled out), followed
   by the general sense and the fact that the lab's tile labels the number
   `f′(a)` and the next lesson takes it as the definition. The note now agrees.
   The block also said "we say", the only first-person plural in the course.
2. **`the-derivative-as-a-function` used `→` to mean "becomes" three lessons
   after `→` was given the meaning "approaches".** "The pattern `t² → 2t`,
   `t³ → 3t²` is `tⁿ → n·tⁿ⁻¹`" sat in the second concept of the lesson that
   follows `what-the-quotients-approach`'s `Q → 2 as h → 0`. A reader who
   learned the arrow as "goes to" reads "t squared goes to 2 t" as a limit.
   The concept now says `t²` has derivative `2t`, and the arrow keeps its one
   meaning in the course.
3. **Two proofs leaned on tools the prerequisites do not supply.**
   `the-derivative-as-a-function` expanded `(t + h)ⁿ` "by the binomial
   theorem"; the course assumes Algebra's Polynomials and Factoring, which
   multiplies polynomials and has no binomial theorem. The proof now gives the
   one-line reason (take `t` from every copy; take `h` from one copy in `n`
   ways; everything else has `h²`), and points at the `(t + h)³` of the
   polynomial lesson as the case the reader has seen. `the-chain-rule`'s
   proof is by induction, which Algebra does not teach (the Discrete
   Mathematics Subject does, and it is not assumed); one sentence now says
   how the step reaches every power ("from `n = 1` to 2, from 2 to 3, and on").
4. **`the-product-rule`'s second preset was never mentioned, and it carries the
   lesson's best point.** The lab squares `t²`: the true derivative `4t³` and
   the wrong rule's `4t²` agree at `t = 0` and `t = 1`, so a single check at
   one place passes the wrong rule while the degree fails it everywhere. That
   is the Subject's recurring trap (true at one value of `t`) in the one
   lesson built to refute a wrong rule, and the body walked past it. The
   "When both factors are the same" paragraph now says it.
5. **Three figures or conditions were stated more loosely than the lab.**
   `the-exponential-and-its-rate` wrote the rate of `2ᵗ` at 3 as "about
   `5.54518`", a rounded figure without `≈`, against the exactness rule; and
   its quiz computed `8·0.693147 ≈ 5.54518`, a rounded value used inside an
   arithmetic step. Both now read `8·ln 2 ≈ 5.54518`. The panel said the first
   row is exact "when the base is a whole number and the step is 1"; the kit
   also needs the place to be a whole number (at `a = 1/2` the first quotient
   is `√2`, printed rounded), and it accepts any positive fraction as a base.
   The steps said "only the first entry can be exact", which is false for
   `b = 4` at `h = 1/2` (exactly 2; the lab prints `≈ 2`, which over-labels
   and is recorded below). Both now say what is true for the bases the lesson
   uses. `what-the-quotients-approach` called `129/64` "a little over 2.0156"
   when it is `2.015625` exactly.
6. **The course home's prerequisites omitted the Algebra course the last
   lesson cites.** `the-exponential-and-its-rate` takes `b^(a + h) = b^a·b^h`
   from Algebra's Exponential and Logarithmic Functions, by title, and the
   course's `assumes_long` named only Lines, Functions and Graphs and
   Polynomials and Factoring. It now names the law and its course, for the
   last lesson only.
7. **One quiz `why` did not say what the error was.**
   `the-derivative-as-a-function`'s first question offered `4t³ − 4t + 1` and
   explained it as "treats something as a constant that is not"; the error is
   giving a constant term a derivative of 1, and this polynomial has no
   constant term. The `why` now says so.
8. **The seam.** `the-derivative-as-a-function`'s closing note was the only
   note in the course that did not name the next lesson by title; it hands
   over to part B in general terms. It now names “Where the Rate Is Zero”, and
   part B's opening paragraph, which cites “The Derivative as a Function” and
   says "this lesson turns the warning into a method", picks it up correctly.
9. **Math that read wrongly aloud** (every `data-say` on the twelve pages was
   read back):
   - `3t(t − 2)`, three times in `the-second-derivative`, read "3 t of the
     quantity t minus 2": a letter touching a bracket is a function call in
     this library's read-out. Now `3t·(t − 2)`, the convention of
     `content/AGENTS.md`.
   - `p″(t) = …`, four times in `the-second-derivative`, read "p double prime t
     equals": the call rule fires on a letter before `(`, and `″` is not one.
     Now `p″ = …`, which is how PLAN §C's own worked line writes it.
   - `3h/h = 3`, `16/h`, `1/h`, `0/h = 0` and `3^t·3^h/h` read "per h": the
     speech rules take `h` after `/` as hours. Each is rewritten
     (`(16 + 3h)/h` and `1/((a + h) − a)` as quiz distractors that are the
     lessons' own misconceptions, `(5 − 5)/h = 0`, `(3^t·3^h)/h`, and the
     `3h/h` sentence said in words).
   - `Q → 2` read "Q to 2": a capital letter before `→` is read as a
     function's type. The sentence now writes the quotient out,
     `(f(1 + h) − f(1))/h → 2`, which reads "goes to 2". Two runs in
     `the-derivative-of-one-over-t` read "to" because a colon earlier in the
     run triggers the same rule (`a = 2:  … → −1/4`, `as h gets small:  …`);
     the colons are gone.
   - `(t + 5)′` read "t plus 5 prime" and `(t³ + t²)′` read "t cubed plus t
     squared prime": the rules say "the quantity …, squared" for `(…)²` but
     drop the grouping for `(…)′`. Where the prose could say "the derivative
     of" in words it now does; the rule statements that must keep the notation
     (`(f·g)′ = f′·g + f·g′`, `(f(g(t)))′ = f′(g(t))·g′(t)`,
     `(uⁿ)′ = n·uⁿ⁻¹·u′`, the induction line, `(eᵗ)′ = eᵗ`, `(tⁿ)′ = n·tⁿ⁻¹`
     and the rest) have spoken forms, in the "the derivative of" convention
     First-Order Linear Equations' spoken file already uses. The course key
     line that carried two rules at once (`(tⁿ)′ = n·tⁿ⁻¹   (f·g)′ = f′g +
     f·g′`, with `f′g` reading "f prime g") is now two lines.
   - `n·tⁿ⁻¹ + h·(…)` read "plus h times and so on"; now "plus terms that each
     contain `h`".

## What it claims to teach but does not, and where a learner gets stuck

- **The derivative of `1/t` is used one lesson before it is derived.**
  `the-derivative-at-a-point`'s third example and third preset take the slope
  `−1` at `a = 1` on the lab's word ("which the next lesson derives"). The
  text is honest about it and the example earns its place (it is the course's
  first error that is not `h²` plus higher terms), so it is left; a reader
  who wants the derivation has it one lesson on.
- **"Factor, or use the quadratic formula"** (`the-derivative-as-a-function`,
  `where-the-rate-is-zero`) assumes Algebra's Quadratics and Complex Numbers,
  which the course does not list. Every preset and every quiz factors, so no
  reader is stopped; the course home's prerequisites were not widened for a
  method the pages never need, and this is the one place a reader might reach
  for it.
- **The lab's `[a, a + h]` reads "A, A plus h".** The interval notation is
  PLAN §C's own and is used across the Subject; a listener hears a pair of
  values, not an interval. An engine-level reading ("the interval from A to A
  plus h") would fix every Subject at once and is not this course's to make.

## Prerequisite order

Checked backwards across the path. The course is first on its path, so only
the Algebra Subject is available. `average-rate-of-change` needs function
notation, evaluating at a fraction, and slope as rise over run (Lines,
Functions and Graphs). `the-quotient-as-a-polynomial-in-h` needs the
expansion of `(t + h)²` and `(t + h)³` and cancelling a common factor
(Polynomials and Factoring, cited by title). `the-derivative-of-one-over-t`
needs a common denominator (Rational and Radical Expressions, not cited; the
move is done in full on the page). `the-exponential-and-its-rate` needs
`b^(a + h) = b^a·b^h` (Exponential and Logarithmic Functions, cited by title
and now in `assumes_long`); `ln` is introduced on the page as the name of the
constant and is not assumed. Inside the course the order is right and each
lesson leans only on earlier ones: the constant term (lesson 2) is what lesson
4 reads the derivative off; the power rule (lesson 6) is what lessons 7, 8, 9
and 10 differentiate with; the product rule (lesson 8) is what the chain rule's
proof (lesson 9) applies; the tangent's error falling short (lesson 4) is what
concavity (lesson 10) explains. The one forward reference, `1/t`'s slope in
lesson 4, is acknowledged in the text. No violation sits in an earlier course,
because there is none.

## Mathematical accuracy

- Every derivation was checked: `(1 + h)² − 1 = 2h + h²`; `(t + h)³` and
  `(t + h)⁴` expansions; `1/(a + h) − 1/a = −h/(a(a + h))`; the product rule's
  add-and-subtract; `(uⁿ·u)′ = n·uⁿ⁻¹·u′·u + uⁿ·u′ = (n + 1)·uⁿ·u′`;
  `b^(a + h) − b^a = b^a·(b^h − 1)`. All correct.
- The gap for `t³` at 1 is `3h + h²`, and the lesson's claim that halving the
  step "slightly more than halves" it is right: the ratio of successive gaps
  is `(6 + h)/(12 + 4h) < 1/2`.
- `where-the-rate-is-zero` says a polynomial "does not jump from positive to
  negative without passing through zero", which is the intermediate value
  property stated for the one class of functions the course differentiates;
  it is true and it is the right amount of analysis for this Subject.
- The `derivative` mode's `none rational` for `3t² + 1` is read correctly by
  the lesson as "no zero it can write as a fraction", with the interval tile
  giving the full answer; for the quartic `t⁴ − 6t²` the lesson says the zero
  tile names `t = 0` and the interval tile places `±√3`, which is what the
  tile prints.
- `the-exponential-and-its-rate`'s `thm` states that `(b^h − 1)/h` heads for a
  number written `ln b` and that `e` is the base with `ln e = 1`, as a claim
  demonstrated and not proved; the lesson says so in the next sentence. The
  table's seven rows were recomputed in double precision and match to six
  significant figures.

## The seam between part A and part B

The two authors agree on voice (careful prose, British spelling throughout:
cancelling, labelled, neighbours, recognise), on `&ldquo;` in prose fields and
typographic quotes in escaped fields, on the shape of every block, and on the
claim/evidence sentence. They differed in two ways, both closed: part A's last
note handed over without a title (item 8); part B writes `p″(t)` where part A
writes `f′(a)`, and the read-out treats the two differently (item 9). Part B's
opening lesson cites part A's last by title and takes its warning as its
premise, which is the right join.

## Changes made

- `__init__.py`: the key line carrying two rules is two lines, with `f′·g`;
  `assumes_short` and `assumes_long` name the law of exponents and Algebra's
  Exponential and Logarithmic Functions for the last lesson.
- `average-rate-of-change`: the quiz distractor `16/h` is `(16 + 3h)/h`, the
  lesson's own misconception, and its `why` says `3h` divided by `h` in words.
- `what-the-quotients-approach`: the `thm` states the claim about `t²` at 1
  and the general sense of "approach", then names the tile's label and defers
  the definition; the note agrees; the arrow sentence writes the quotient out;
  `129/64` is `2.015625` exactly.
- `the-derivative-of-one-over-t`: the key line and the worked line lose the
  colon that made `→` read "to"; the quiz distractor `1/h` is
  `1/((a + h) − a)`, the subtract-the-denominators error, with its `why`.
- `the-derivative-as-a-function`: the second concept says "has derivative"
  instead of `→`; the proof expands `(t + h)ⁿ` by counting choices rather than
  by "the binomial theorem" and names the `(t + h)³` of the polynomial lesson;
  the error list and the first mistake say "the derivative of" in words and
  `(5 − 5)/h = 0`; the first quiz `why` names the constant-term error; the note
  names “Where the Rate Is Zero”.
- `the-product-rule`: "the derivative of `t³ + t²`" in words; the second
  preset is used for the one-place trap.
- `the-chain-rule`: the induction step is said to reach every power.
- `the-second-derivative`: `3t·(t − 2)` three times; `p″ = …` four times
  (example, math block, worked line, quiz).
- `the-exponential-and-its-rate`: `8·ln 2 ≈ 5.54518` in the body and the
  quiz; the panel's exact-row condition includes the place and a fractional
  base; the step says which entries are fractions for the bases used; the
  quiz distractor `(3^t·3^h)/h`.
- `content/spoken/differential_equations_c1_rates.py`: eighteen spoken forms
  for the rule statements written as `(…)′`, each read as "the derivative of
  …", and one for the key line `p″ = (p′)′`; the existing form for the
  chain-rule worked line is kept.

Lesson slugs, count and order are as `COURSES.json` lists them. The preview
(`scripts/preview_subject.py differential_equations --course
rates-of-change-and-the-derivative`) reports OK: twelve pages, eleven labs
executed and swept, eleven pages with ninety-six pinned figures all matching,
no math run guessed at; `tests/test_speech.py` passes with the new spoken
forms.

## Remaining issues

- **The read-out rules drop the grouping of `(…)′`.** `(x)²` says "the
  quantity x, squared" and `(x)′` says "x prime", so every bracketed
  derivative in the Subject needs a spoken form or a rewrite into words. This
  course now has nineteen such forms and First-Order Linear Equations has more.
  The fix belongs in `scripts/mathpath/speech.py` (chrome-renderer tier): read
  a `′` or `″` after `)` as "the derivative of" the group, or as "the quantity
  …, prime". It would retire most of two Subjects' spoken files.
- **`/h` reads "per h" when a number or letter precedes the slash**, because
  `h` is in the speech rules' unit list (hours). Every run in this course has
  been rewritten around it, and the Subject writes `/h` on most pages; a
  bracket before the slash avoids it (`(…)/h` reads "over"), which authors of
  the later courses should know. Also chrome-tier.
- **The `transcendental` mode over-labels one exact case.** For `b = 4` at
  `h = 1/2` the quotient `(2 − 1)/(1/2) = 2` is a fraction and the lab prints
  `≈ 2`. Over-labelling is the safe direction of error and no preset reaches
  it, but the kit's exactness test (`exp` at `h = 1` with an integer place)
  could be widened to perfect-power bases. `@lab-arithmetic`'s, not the
  course's.
- **`the-derivative-at-a-point` uses `1/t`'s slope before it is derived.**
  Left as is, with the text's own acknowledgement, because the example is the
  course's first non-`h²` error and removing it would leave the error tile
  with nothing but polynomials to show.
- **`the-exponential-and-its-rate` is the heaviest lesson in the course**: the
  factoring, a rounded column, three bases, `e`, the same column at another
  place and the power-rule misconception. It is one lesson by PLAN §C and the
  URL space is fixed; if the Subject is ever re-cut, "the same column at
  another place" (the fourth preset and its ratio tile) is the natural second
  half, and `e` as the base whose constant is 1 would then close the course on
  its own page.
- **"Factor, or use the quadratic formula"** in two step lists assumes a
  method the course does not list among its prerequisites and never needs;
  if a later pass widens the presets to a non-factoring derivative, the step
  should cite “The Quadratic Formula” in Algebra's Quadratics and Complex
  Numbers by title.
