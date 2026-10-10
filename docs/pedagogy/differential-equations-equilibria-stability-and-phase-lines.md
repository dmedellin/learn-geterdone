# Pedagogy assessment — Equilibria, Stability and Phase Lines (differential equations, course 5)

Formed from the eight lesson dicts in `content/differential_equations/c5_phase_lines/`
(`part_a.py`, lessons 1–4, and `part_b.py`, lessons 5–8, written by two authors
from `docs/differential-equations/PLAN.md` §C), the course dict in
`__init__.py`, the spoken forms in
`content/spoken/differential_equations_c5_phase_lines.py`, and the pages as
`scripts/preview_subject.py` renders them, with every preset's tiles read off
the built page by `labcheck.js --observe` and every `data-say` reading on the
rendered pages dumped and read. The course may assume the four courses before
it and the Algebra Subject, and nothing else. All eight lessons were read
before any was changed; the last two sections record what was changed and
what was not.

Lessons, in course order: `autonomous-equations`, `the-phase-line`,
`stable-unstable-and-semistable`, `linearisation-and-the-sign-of-f-prime` |
`long-run-behaviour-without-solving`, `one-parameter-families`,
`bifurcation-diagrams`, `sketching-solutions-from-the-phase-line`. The bar
marks the seam between the two authors.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.** Test
  for a `t` on the right and list the equilibria exactly
  (`autonomous-equations`); draw the phase line from the roots and one test
  value per gap and read where a start goes (`the-phase-line`); classify every
  equilibrium from the signs alone (`stable-unstable-and-semistable`); compute
  `f′` exactly at each equilibrium, classify with its sign, and name the case
  it cannot decide (`linearisation-and-the-sign-of-f-prime`); state the limit
  of a solution from any start and say when it is infinite
  (`long-run-behaviour-without-solving`); list a family's equilibria at a
  value of the parameter and find where two meet (`one-parameter-families`);
  read solid and dashed branches and name the fork and the crossing
  (`bifurcation-diagrams`); sketch the curves with the inflection level
  computed (`sketching-solutions-from-the-phase-line`). None is "understand".
- **The one hard idea per lesson is the right one, in the right order.** The
  definition and the uniqueness fact that makes an equilibrium a wall
  (`autonomous-equations`); the sign of `f` as a direction and not a speed
  (`the-phase-line`); the two-sided sign test with the semistable case as a
  case and not a hedge (`stable-unstable-and-semistable`); the shift
  `u = y − y*` done exactly on `y² − 1`, with nothing dropped, so that the
  reader sees `u′ = −2u + u²` before being told which term to neglect
  (`linearisation-and-the-sign-of-f-prime`); then the limit, the parameter,
  the diagram, the sketch. Each lesson's `note` hands over to the next by
  title.
- **The figures are right and the prose agrees with every tile.** All
  pinned strings across eight pages match the page (`labcheck`), and every
  figure quoted in prose was recomputed by hand: the cubic at `−1, 1/2, 2, 4`
  is `−8, 5/8, −2, 12`; `|f(2)|/|f(1/2)| = 16/5`; `y²·(1 − y)` at `−1, 1/2, 2`
  is `2, 1/8, −4` with `f′(0) = 0`, `f′(1) = −1`; `(u − 1)² − 1 = u² − 2u`;
  `−2/10 + 1/100 = −19/100`; `e^(−2) ≈ 0.135335`, `e^(−1) ≈ 0.367879`,
  `e² ≈ 7.38906`; the cubic's slopes `3, −2, 6`; Euler from `4` with `h = 1/4`
  gives `19/4` then `409/64`, from `2` gives `7/4, 97/64`, and from `5/2` with
  `h = 1` the rocking column `5/2, 7/4, 13/16, 313/256`; the digit budget at
  step 11 for a quadratic and step 7 for a cubic (both observed); `a + y²` at
  `a = −4, −1, 0, 1`; the critical values `a = 1` for `y² − 2y + a` and `a = 4`
  for `y² − 4y + a`; `f′(0) = a` and `f′(±√a) = −2a` on the pitchfork, `−8` and
  `4` at `a = 4`, `−18` and `9` at `a = 9`; `y″ = (2y − 4)·(y − 1)·(y − 3)`
  with `−3/4` at `5/2` and `3/4` at `3/2`; the logistic slopes
  `7/16, 3/4, 1, 3/4, 0`; `(4 ± √7)/3`.
- **The exactness rule is kept and said aloud.** `(1 ± √5)/2` is printed as a
  surd with the rounded pair named as rounded (`autonomous-equations`); every
  exponential factor is `≈` and called rounded
  (`linearisation-and-the-sign-of-f-prime`); the diagram is "drawn from
  floating-point roots" while the critical values are exact
  (`one-parameter-families`, `bifurcation-diagrams`); the curves are "drawn
  by stepping in floating point" and the inflection tile is exact
  (`sketching-solutions-from-the-phase-line`). The material clause is in the
  course footer and `long-run-behaviour-without-solving` makes it the lesson's
  point: a column of exact steps is evidence for an arrow, not a proof of a
  limit.
- **Claims are stated as claims.** The slope test is a `thm` with no proof,
  followed by what the lab demonstrates and what it does not, and the course
  home's `not_covered` says the same (`linearisation-and-the-sign-of-f-prime`).
  The limit theorem names which of its three pieces is the one not proved
  (`long-run-behaviour-without-solving`). The even-and-odd-roots rule is a
  stated shortcut and the sign test is "the one to trust"
  (`stable-unstable-and-semistable`). Where a proof is algebra the reader has
  (sliding a solution, `y″ = f′(y)·f(y)`), it is given.
- **The misconceptions are the real ones and each is refuted with a
  number.** An equilibrium is a pause, refuted by uniqueness through `(2, 1)`;
  arrow length is speed, refuted by `16/5`; semistable is a hedge, refuted by
  `+, +` at `0`; `f′ = 0` means semistable, refuted by `y³`, `−y³`, `y²`;
  solutions oscillate between equilibria, refuted by the `h = 1` column that
  rocks where no solution does; small change in `a`, refuted by `±1/10`
  against none at `a = ±1/100`; the count only rises, refuted by three
  families; a straight line or parabola, refuted by the logistic slope column.
  Every `mistakes[0]` is the §C misconception.
- **Retrieval practice is real and the distractors are false.** Every quiz
  item's `why` addresses the wrong choices, and the questions test the idea:
  "`y(2) = 1`, what is `y(0)`", "why is `f(2)` enough for all of `(1, 3)`",
  "which `f` has a semistable point at `2`", "what does the rocking column
  show", "which `a` makes `y(0) = 0` rise without bound". Each distractor was
  argued for and none is true; the one that came closest, "one rising from `0`
  and levelling off at `1`" when only the equilibria `1` and `3` are given, is
  possible for some `f` and so is correctly not the answer.

## What the course teaches badly, or wrongly

1. **One rounded figure was wrong.** `sketching-solutions-from-the-phase-line`
   gave the cubic's inflection levels `(4 ± √7)/3` as "about `0.45140` and
   `2.21525`". The smaller root is `0.4514162…`; `0.45140` is wrong in its
   fifth decimal, and neither figure carried the `≈` the exactness rule
   requires of a rounded value. Now `≈ 0.451416` and `≈ 2.21525`, six
   significant figures, labelled rounded, with the surd named as exact.
2. **The course home's key could not be read aloud.** The line
   `f′(y*) < 0  stable;  > 0  unstable` renders correctly (the renderer
   escapes it) but the read-out took `< 0  stable;  >` for a tag and spoke
   "f prime of y star, 0, unstable", which is the opposite of what the line
   says. It is now two lines, `f′(y*) < 0  stable` and
   `f′(y*) > 0  unstable;  f′(y*) = 0  undecided`, which also puts the
   undecided case on the course home, where it belonged.
3. **One ratio was misstated.** `linearisation-and-the-sign-of-f-prime` said
   the neglected `1/100` was "one part in twenty of the whole", but the whole
   is `−19/100`, so it is one part in nineteen; it is a twentieth of the
   linear term `−20/100`. Now "a twentieth of the first term".
4. **The limit theorem was silent about finite-time blow-up.** The `thm` in
   `long-run-behaviour-without-solving` said a solution "as `t` grows"
   approaches its equilibrium or goes to `±∞`, while the paragraph below it
   correctly said the climb from `4` "ends at a finite time". The theorem now
   says "for as long as the solution exists", so the two agree.
5. **The parameter lesson never retrieved the bifurcation the reader had
   already met.** `one-parameter-families` teaches "solve `f = 0` and
   `f′ = 0` together" on `a + y²`, and the course home's `assumes_long`
   promises that harvesting with its threshold is "read again" here, but
   neither lesson of the Parameters module mentioned “Harvesting and the
   Threshold”, where `y′ = y·(1 − y/4) − H` had two equilibria at `H = 3/4`,
   one at `H = 1`, none above, and the reader was told the threshold came
   from the peak of the growth. That is a saddle-node with the harvest as the
   parameter, and the new test finds the same value by a different route
   (`1 − y/2 = 0` at `y = 2`, `f(2, H) = 1 − H`). The lesson now says so and
   tells the reader to type it; the lab prints `1, 3`, `1 unstable; 3 stable`
   and `a = 1`, checked on the built page before the paragraph was written.
   For the same reason `stable-unstable-and-semistable` now names the
   harvested equation at its threshold, `−(y − 2)²/4`, as a semistable point
   the reader has already seen, and the complementary case to the lesson's
   own example: the same sign on both sides, negative this time.
6. **`sketching-solutions-from-the-phase-line` recomputed what “Logistic
   Growth” had printed without saying so.** That lesson in the previous
   course found `f′(y) = 1 − y/2 = 0` at `y = K/2` as the point of fastest
   growth and its inflection tile read `y = 2`. The logistic example here
   reaches the same level and now says that it is the same level, and what
   the phase line adds: why the fastest point and the change of bend are one.
7. **A sentence that said less than it meant.** `one-parameter-families`
   said "the family does not change type while the number of roots stays the
   same, and it can change type when that number changes", where "type" of a
   family is undefined. Now: the phase line keeps its shape while the number
   of roots stays the same, and can change it only at a value of `a` where
   that number changes. In the same lesson "the equilibria moved by `1/10`,
   ten times as far as the parameter did" followed a sentence about two
   values of `a` that are `1/50` apart; the sentence now names the interval
   it is about (`a = −1/100` to `a = 0`, where `a` moved `1/100`).
8. **"The first of the two methods."** `linearisation-and-the-sign-of-f-prime`
   called the slope test "the first of the two methods this Subject uses for
   stability" in a course that had just spent a lesson on the other one. It
   is the one that carries over to systems, and the sentence now says that
   and nothing about order.
9. **Three read-out faults.** `long-run-behaviour-without-solving` put the
   ASCII `y^2 - 4y + 3` in a prose run, which the plan forbids outside a
   label and which read "y squared negative 4 y plus 3"; it is now
   `y² − 4y + 3` in the library's notation. `stable-unstable-and-semistable`
   asked the reader to "write it as `+` or `−`", and a lone `−` reads
   "negative"; now words. The sign patterns `−, +, −, +` and `+, +, −` in
   `the-phase-line` read "negative, plus, negative, plus"; they now have
   spoken forms, which cannot misread the same text anywhere.
10. **A description of the kit that was loose at a surd.** `the-phase-line`
    said the lab tests "the integers one beyond the ends"; for the golden
    preset the kit tests at `−2` and `3`, beyond `(1 ∓ √5)/2`, which is two
    integers beyond the lower end. Now "an integer beyond each end".

## What it claims to teach but does not, and where a learner gets stuck

- **The semistable case arrives with one sign pattern.** The lesson's
  example `y²·(1 − y)` has `+, +` at `0`; the reader could leave with
  "semistable means positive on both sides". The harvested equation at its
  threshold, now in the lesson, is `−, −` at `2`, and the two together are the
  whole of the case.
- **`linearisation-and-the-sign-of-f-prime` is the heaviest lesson.** It
  carries the shift and expansion, the slope as a rate (`e^(f′(y*)·t)`, with
  three rounded factors), and the zero-slope failure with three equations.
  PLAN §C puts all three there and the lesson keeps them in that order, with
  the rate in its own `h3`. It is one lesson by the manifest; see remaining
  issues.
- **The reader is told that `y → +∞` can happen in finite time but is not
  told how to tell.** `long-run-behaviour-without-solving` says the quadratic
  climb "ends at a finite time, as “Blow-Up and the Interval of Existence”
  found for `y′ = y²`" and leaves the criterion to that lesson, which is
  right: the phase line gives the direction and not the time, and the lesson
  says that is all it gives.

## Prerequisite order

Checked backwards across the path. `autonomous-equations` needs substitution
as a check (“Checking a Proposed Solution”), the slope field as a grid of
`f(t, y)` (“Slope Fields”), the chain rule on `y(t − c)` (“The Chain Rule” in
Rates of Change and the Derivative) and uniqueness through a point, which
“Blow-Up and the Interval of Existence” states in words as a `thm` with no
proof; all earlier, all cited by title except the chain rule, which is used
as the reader's own algebra. `stable-unstable-and-semistable` and
`one-parameter-families` now cite “Harvesting and the Threshold”, and
`sketching-solutions-from-the-phase-line` cites “Logistic Growth”, both in
Separable Equations, Growth and Decay; that course's `autonomous`-mode pages
already printed `0 unstable; 4 stable`, `y = 2` in the inflection tile, and
used the word semistable once, so this course is reading again what the
reader has computed, as its `assumes_long` promises.
`linearisation-and-the-sign-of-f-prime` needs the expansion of a polynomial
in a small step (“The Difference Quotient as a Polynomial in h”) and the
power rule, both of the first course and cited by course title; it points
forward to “Linearisation and the Jacobian” in Systems and the Phase Plane,
which exists under that title. The quadratic formula and surds come from
Algebra's Quadratics and Complex Numbers. No violation sits in an earlier
course. Inside the course the order is right: definition and wall, direction,
two-sided classification, one-sided classification with its failure, limit,
parameter, picture, sketch.

## Mathematical accuracy

- Autonomy, equilibria as roots, the constant solution with residual zero,
  and the slide `y(t − c)` with its proof by the chain rule: right, and the
  proof says exactly where it fails for `y′ = t·y`.
- The sign of a polynomial between consecutive roots, the test points the
  kit uses (`floor(min) − 1`, midpoints, `ceil(max) + 1`, all exact), and
  the no-crossing argument from uniqueness: right.
- The two-sided classification and the even/odd multiplicity shortcut: right
  for polynomials, which is all the lab takes.
- The expansion `u′ = f′(y*)·u + O(u²)`, the exponential rate as the
  behaviour of the linear part, and the three zero-slope equations with their
  three verdicts: right. The remark that `y′ = −y³` approaches `0` more
  slowly than any exponential is right (`y ~ (2t)^(−1/2)`).
- The limit theorem, with the finite-time qualification now added; the
  rocking Euler column for `h = 1` is the polygon crossing an equilibrium
  and is correctly diagnosed as a step-size fault.
- The saddle-node on `a + y²`, the test `f = 0`, `f_y = 0`, the critical
  values of `y² − 2y + a` and `y² − 4y + a`, the pitchfork and transcritical
  slopes `a`, `−2a`, `a`, `−a`: right. The kit's critical values are the
  rational roots of the discriminant of `f` in `y`, which is the same
  condition.
- `y″ = f′(y)·f(y)`, the concavity table, the inflection at a level where
  `f′` changes sign and `f ≠ 0`, the steepest point as the inflection, and
  the logistic S-curve: right. The cubic's inflection levels are now stated
  to six figures and labelled.

## The seam between part A and part B

The two authors agree on voice (careful prose, British spelling, no filler),
on the `_p` helper and the preset shape, and on the hand-over: part A's last
note names the limit and the parameter as the next two questions, and part B's
first lesson opens with the no-crossing fact at the right altitude. They
differed in one visible way, now closed: part A wrote every typographic quote
in prose as `&ldquo;`/`&rdquo;`, and part B wrote three of its prose
cross-references with the characters “ ” while using entities in its notes
(`long-run-behaviour-without-solving`, `one-parameter-families`,
`bifurcation-diagrams`; now entities, with `f&prime;` in the one title that
carries a prime, as part A's own note does). Part B's `_b` helper for the
`bifurcate` mode is the right addition and matches `_p` in shape.

## Changes made

- `__init__.py`: the key line `f′(y*) < 0  stable;  > 0  unstable`, which the
  read-out spoke as its opposite, is now two lines, the second carrying the
  undecided case; seven lines, each within the 46-character box.
- `the-phase-line`: "an integer beyond each end".
- `stable-unstable-and-semistable`: a paragraph naming the harvested
  equation at its threshold as a semistable point already met, with the
  negative-negative sign pattern; the first step says "a plus or a minus
  sign" in words.
- `linearisation-and-the-sign-of-f-prime`: "a twentieth of the first term";
  the slope test is "the one that carries over to systems" and not "the
  first of the two methods".
- `long-run-behaviour-without-solving`: the `thm` says "for as long as the
  solution exists"; `y² − 4y + 3` in notation instead of ASCII in prose; the
  quoted title as entities.
- `one-parameter-families`: the harvest paragraph (the family, the two
  equations finding `H = 1`, the tiles the reader will see); "the phase line
  keeps its shape"; the `1/10` against `1/100` sentence names its interval;
  the quoted title as entities.
- `bifurcation-diagrams`: the quoted title as entities with `f&prime;`.
- `sketching-solutions-from-the-phase-line`: `≈ 0.451416` and `≈ 2.21525`,
  labelled rounded beside the exact surd; the logistic example names
  “Logistic Growth” and what the phase line adds to it.
- `content/spoken/differential_equations_c5_phase_lines.py`: spoken forms
  for the two sign patterns `−, +, −, +` and `+, +, −`.

Lesson slugs, count and order are as `COURSES.json` lists them; no preset
instance changed, so every pinned tile still matches. The preview
(`scripts/preview_subject.py differential_equations --course
equilibria-stability-and-phase-lines`) reports OK: nine pages, eight labs
executed and swept, eight pages with pinned figures all matching, no math run
guessed at; `tests/test_speech.py` passes with the two new spoken forms.

## Remaining issues

- `linearisation-and-the-sign-of-f-prime` carries three ideas: the exact
  shift and expansion, the slope as a rate with three rounded exponential
  factors, and the zero-slope case. It is one lesson by PLAN §C and the URL
  space is fixed. If the Subject is ever re-cut, "the rate" (`e^(f′(y*)·t)`,
  the `0.135335` and `7.38906` factors, and the remark that `−y³` is slower
  than any exponential) is the natural second half, and would let the first
  half end on the three zero-slope equations, which is the lesson's
  misconception.
- Math blocks that are tables are announced to a listener as "a table, shown
  on the page", so the `f(y)` row of the test-value table in `the-phase-line`
  is not spoken; the worked example below it carries the same four values in
  readable lines, which is why nothing was changed. A sign row in a block
  (`−  +  −  +`) still reads its first `−` as "minus" and its third as
  "negative"; block lines are not override keys, and the inconsistency is
  the engine's, not the course's.
- The read-out speaks a lone `a` as the letter name, so `a = 4` is "A equals
  4" and `f(y, a)` is "f of y and A". That is the engine's rule for a letter
  that is also a word, applied everywhere; the lessons were not rewritten
  around it.
- `long-run-behaviour-without-solving` tells the reader a start at `3` reads
  `at equilibrium` in the limit tile, which is true on the page but is not a
  shipped preset; the reader has to type it. A fourth preset would pin it,
  and the plan's three were kept.
