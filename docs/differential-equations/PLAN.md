# Differential Equations — the build specification

This is the curriculum, lab and authoring contract for the ninth Subject.
Everything an author, a kit engineer or a reviewer needs is here; nothing in it
is a suggestion. Where it says "exactly", a test or a gate enforces it. Where it
says "never", a published page has already been wrong for that reason somewhere
in this library.

Read before this: `AGENTS.md` §0, §1, §1a, §2 and the page-weight note;
`content/AGENTS.md` (all of it, and "Write math a voice can read" twice);
`scripts/mathpath/AGENTS.md` ("a preset's two claims"); `docs/philosophy/PLAN.md`
§D.0, whose kit conventions this document inherits and does not repeat except
where this Subject changes them.

Contents

- §0 The one question, answered for this Subject; the exactness rule; the
  material clause
- §A PATH fields
- §B The ten courses, in order
- §C Every lesson: 92 entries
- §D The two lab kits: `calckit` (7 modes) and `dekit` (15 modes), the shared
  `de_core` blocks, and the existing JavaScript they reuse
- §E Package layout and the author's field checklist
- §F Voice and style, with one exemplary paragraph
- §G What is left out, and why
- §H Wiring notes for the orchestrator

---

## §0 The one question

`docs/FUTURE-SUBJECTS.md` asks of every proposed Subject: **what does the reader
compute?** For Differential Equations the answer is "the next value, and how
far it can be trusted". A differential equation says how a quantity changes;
everything a reader does with one is either to step it forward, to check a
proposed answer against it, or to read its long-run behaviour off its sign.
All three are arithmetic a browser can do exactly, and the whole Subject is
built on that.

The library has avoided calculus until now (`docs/FUTURE-SUBJECTS.md`,
"fields"). That was a per-Subject statement — Algebra and Discrete Mathematics
each say "no calculus" about *themselves* — and not a library rule. This
Subject teaches the calculus it needs, in the library's honest way: a rate of
change is a difference quotient computed exactly; the derivative is the number
those quotients approach, shown as a column of exact fractions and *stated* as
a claim the lab demonstrates and does not prove; the integral is accumulated
change, computed as exact left, right, trapezoid and midpoint sums. For
polynomials the "approach" is not even a limit: the difference quotient of a
polynomial is a polynomial in `h`, and its constant term is the derivative,
read off by algebra alone. That is the first course, and it is as much calculus
as the rest of the Subject uses: two courses, nineteen lessons, before the
first differential equation.

Twenty-two kinds of computation carry the Subject:

| what the reader computes | mode | from |
| --- | --- | --- |
| the average rate over `[a, a + h]` as an exact fraction, for a column of halving `h` | `calckit/quotient` | a polynomial or `1/t`, a point, a step |
| the difference quotient simplified to a polynomial in `h`, and its constant term | `calckit/hpoly` | a polynomial (or a product, or a composition) |
| the tangent line and the exact error of the linear approximation | `calckit/tangent` | a polynomial, a point, a step |
| `p′`, `p″`, their rational zeros, the sign chart | `calckit/derivative` | a polynomial |
| the quotients of `bᵗ`, `sin`, `cos`, rounded and labelled, and what they approach | `calckit/transcendental` | a base or a trig function, a point |
| left, right, trapezoid and midpoint sums as exact fractions, and their exact error | `calckit/riemann` | a rate function, an interval, `n` |
| an antiderivative, its constant from an initial value, `F(b) − F(a)` | `calckit/antiderivative` | a polynomial, limits, an initial value |
| the residual when a candidate is substituted into an equation: zero or not | `dekit/verify` | an equation, a candidate solution |
| the exact slope at a grid point, the nullcline, the horizontal solutions | `dekit/field` | `f(t, y)` |
| Euler's steps as exact fractions, with the exact error against a known solution | `dekit/euler` | `f(t, y)`, a start, `h`, `n` |
| the error at three step sizes, their exact ratios, the observed order | `dekit/order` | an equation with a known solution, a method |
| `G(y) = H(t) + C`: both antiderivatives, the constant, the explicit branch | `dekit/separable` | `g(y)·y′ = h(t)`, an initial value |
| `yₙ = A + (y₀ − A)(1 + kh)ⁿ` exactly beside `e^(kt)` rounded; the doubling step | `dekit/growth` | `k`, a start, a shift, `h` |
| equilibria, their stability from the sign of `f`, `f′(y*)`, the limit of a start | `dekit/autonomous` | a polynomial `f(y)` |
| equilibria as a parameter moves, and the value where two of them meet | `dekit/bifurcate` | a polynomial in `y` and `a` |
| `μ`, `y_h`, `y_p` and the fitted constant for a first-order linear equation | `dekit/linear1` | `p(t)`, `q(t)`, an initial value |
| the Euler factor `1 − a·h`, the step bound `2/a`, the backward factor | `dekit/stiff` | a decay rate, a step |
| the roots of `a·r² + b·r + c`, their kind, the general solution, `C₁`, `C₂` | `dekit/char` | three coefficients, two initial values |
| `ω₀²`, the damping class, `c_crit`, amplitudes squared, the resonant frequency | `dekit/oscillator` | `m`, `c`, `k`, a forcing |
| trace, determinant, eigenvalues, eigenvectors, the portrait type, exact Euler steps | `dekit/phase` | a 2×2 matrix, a start |
| whether a point is an equilibrium, the Jacobian there, its type | `dekit/jacobian` | two polynomials, candidate points |
| `ℒ[f]` as an exact rational function, partial fractions, the inverse, the residual | `dekit/laplace` | a signal, an equation, initial values |

No lesson carries a decorative lab. Where a classical topic has nothing a
browser can compute exactly or demonstrate honestly, it is left out and named
in §G.

**Deviation from one-kit-per-course.** Two kits for the Subject, one kit per
lesson, as Philosophy does: `calckit` for the two calculus courses and one
lesson of the second-order course, `dekit` for everything else. Both are listed
in the registry comment the way Operations Research records its two-kit courses.

### The exactness rule

The library promises exact rational arithmetic, and most differential
equations have solutions in `e`, `sin`, `cos` and `ln`. The rule that keeps the
promise true has three parts, and every mode in §D obeys all three:

1. **Step methods run exactly.** Euler, improved Euler and Runge–Kutta step a
   right-hand side that is a polynomial in `t` and `y` (or `t`, `x`, `y`) with
   rational coefficients, from a rational start with a rational step. Every
   `yₙ` is a fraction and is printed as one. The error against a closed form is
   exact whenever the closed form is rational at `tₙ` — `y = t²`, `y = 1/(1 − t)`,
   `yₙ = (1 + kh)ⁿ` — and is rounded and labelled otherwise.
2. **Closed-form solutions are symbolic, and are checked by substitution,
   exactly.** A candidate solution lives in one of two classes the kit can
   differentiate without rounding: rational functions of `t`, and the
   exponential-polynomial class `Σ c·tᵏ·e^(at)·{1, cos(bt), sin(bt)}` with
   rational `c`, `a`, `b`. Both are closed under differentiation, so "`y`
   satisfies the equation" is decided by computing the residual and comparing
   it with zero — not by evaluating anything. A candidate is *evaluated* only
   where that is exact: at `t = 0` for the exponential-polynomial class, and
   anywhere for a rational function.
3. **Any irrational figure printed is rounded by a stated rule and labelled.**
   The rule is: double-precision evaluation, printed to six significant figures
   with trailing zeros dropped, always preceded by `≈`. A tile that may hold
   either kind prints `3/4` for an exact value and `≈ 0.693147` for a rounded
   one, and never a bare decimal. Square roots are carried as surds
   (`(−1 ± √5)/2`) and printed exactly, with the rounded value in a separate
   tile where a lesson wants it. The one other place floating point appears is
   where it appears in every Algebra lab: the pixels. A curve without a closed
   form is drawn by stepping in floating point and the legend says "drawn";
   every number a reader is told in a tile comes from the exact side.

A fourth rule follows from the first and is the reason this Subject can be
honest about its own method: **exact arithmetic exposes what floating point
hides.** A quadratic right-hand side doubles the number of digits in the
denominators at every Euler step; the labs run to a stated digit budget and
then stop, visibly, rather than round silently (§D.1). The lesson that first
meets this ("Blow-Up and the Interval of Existence") teaches it as a fact about
the method.

### The material clause

The hazard of learning this Subject from interactive examples is not the one
any other Subject names. Algebra's is the invented rule, Discrete Mathematics'
the unproved example, Operations Research's the model that was not the
situation. Here the labs are exact and the *method* is approximate: a column
of correct fractions is not the solution of the equation, it is Euler's
polygon, and a reader who has watched sixty-four exact steps land near the
closed form has learned something true about one step size. The clause:

> every figure on this path is computed in your browser from the equation the
> lesson states, and a numerical solution is exact arithmetic applied to an
> approximate method &mdash; the fractions are right, and the answer is still
> only as close as the step allows.

`tests/test_site_invariants.py` needs

```
DE_DISCLAIMER_RE = re.compile(r"(?i)exact arithmetic applied to an approximate method")
```

in `PATH_MATERIAL_DISCLAIMER`, labelled `"the exact-arithmetic-on-an-approximate-method disclaimer"`.
The pinned phrase stops short of the em dash and carries no apostrophe, for the
reason the OR and Philosophy comments give.

---

## §A PATH fields (`content/differential_equations/__init__.py`)

```
"slug": "differential-equations",
"title": "Differential Equations",
"level": "Intermediate → Advanced",
"level_note": "assumes the Algebra Subject; the calculus is taught inside",
```

**tagline** (the counts are checked against the package by
`test_the_tagline_and_description_state_the_real_counts`; re-verify at wiring):

> Change described by its rate: the derivative and the integral built from
> exact difference quotients and sums, then the equations that say how a
> quantity changes and the methods that recover the quantity &mdash; slope
> fields, Euler's steps as exact fractions, separable and linear equations,
> equilibria and phase lines, oscillators and resonance, systems in the phase
> plane, and the Laplace transform. Ten courses and 92 lessons are available.

**description**:

> The Differential Equations Subject: ten courses in one order, from rates of
> change and the derivative and accumulation and the integral, through what a
> differential equation is and Euler's method, separable equations and growth,
> equilibria and phase lines, first- and second-order linear equations,
> oscillators and resonance and systems in the phase plane, to Laplace
> transforms. Every step method runs in exact fractions in your browser, every
> closed form is checked by substitution, and every rounded number says so. All
> ten courses and 92 lessons are available.

**key** (every line ≤ 46 characters, measured without combining marks; no line
carries a second column; lengths were measured, re-measure if edited):

```
Δy/Δt exactly, then what it approaches: y′
∫ₐᵇ f(t) dt = F(b) − F(a)
yₙ₊₁ = yₙ + h·f(tₙ, yₙ)   every yₙ a fraction
y′ = k·y  ⟹  y = y₀·e^(kt)
f(y*) = 0, f′(y*) < 0  ⟹  stable
a·r² + b·r + c = 0   roots decide the motion
x′ = A·x:  τ and Δ of A pick the portrait
ℒ[y′] = s·Y − y(0)   calculus becomes algebra
```

**material**: the clause in §0, verbatim.

**prerequisites** (paragraphs):

1. The Algebra Subject, and specifically four of its courses: Lines, Functions
   and Graphs (function notation, slope, what a graph is), Polynomials and
   Factoring (expanding `(t + h)²`, which the first course does on every
   page), Quadratics and Complex Numbers (the quadratic formula and `i`, which
   decide every second-order equation here), and Exponential and Logarithmic
   Functions (`e`, `ln`, and why `e^(kt)` doubles in a fixed time). Systems and
   Matrices helps with the phase plane and is named where it is used.
2. No calculus. Rates of Change and the Derivative starts from a difference
   quotient computed as a fraction and reaches the derivative without taking a
   limit you have to believe: for a polynomial the quotient is a polynomial in
   `h` and the derivative is its constant term. Accumulation and the Integral
   does the same for sums. If you have met calculus before you will move
   quickly; if you have not, those two courses are the whole of what is
   assumed later.
3. Fractions, and patience with them. Every Euler step on this path is an
   exact fraction, and after twenty steps the denominators are long. The labs
   do the arithmetic; what is asked of you is to read a fraction beside a
   decimal and know which one is the true value of the method.
4. No programming. Nothing here asks you to write code. The labs run so that
   you can change a step size and watch the error halve, which is the one
   thing a printed page cannot do.

**why_order** (paragraphs):

1. The derivative comes first because a differential equation is a statement
   about one, and a reader who thinks `dy/dt` is a fraction will misread every
   equation that follows. It is taught as what exact difference quotients
   approach, and for polynomials as the constant term of a polynomial in `h`,
   so that the first course asks for no faith.
2. The integral comes second and is kept short, because the Subject needs
   exactly two things from it: that accumulated change is a sum that refines
   to a number, and that reversing the power rule recovers a function up to a
   constant. The constant is the whole reason an initial value is needed, and
   it is met here, once, before any equation.
3. Euler's method comes before any closed form, because it is what a
   differential equation *means*: the next value is this value plus the rate
   times the step. Every closed form later in the Subject is checked against
   those exact steps, and every step method's error is measured against a
   closed form, so the two halves of the Subject keep each other honest.
4. First-order equations fill four courses before second-order ones because
   growth, equilibria and stability are where the ideas live; the
   second-order theory is then one quadratic equation, and oscillators, systems
   and the Laplace transform are three readings of its roots.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. Accumulation and
> the Integral reverses the rules of Rates of Change and the Derivative;
> Differential Equations and Euler's Method uses both; Separable Equations,
> Growth and Decay and Equilibria, Stability and Phase Lines read first-order
> equations two different ways; First-Order Linear Equations needs the product
> rule and the integral; Second-Order Linear Equations needs the quadratic
> formula from Algebra and nothing new; Oscillators, Damping and Resonance,
> Systems and the Phase Plane and Laplace Transforms each take the second-order
> theory somewhere else.

**footer_lead**:

> <strong>Educational course material.</strong> Every figure on this path is
> computed in your browser from the equation the lesson states, in three
> honest tiers: every step method runs in exact fractions, and prints them;
> every closed-form solution is checked by substituting it into the equation
> symbolically and reading the residual, never by evaluating it; and every
> number that is genuinely irrational &mdash; a value of `e^(kt)`, a doubling
> time, a period &mdash; is printed with `≈` to six figures and labelled
> rounded. Curves that have no closed form are drawn by stepping in floating
> point and the legend says so; the numbers in the tiles never are. What the
> labs cannot do is make a numerical method into the solution: a correct
> fraction is a correct value of Euler's polygon, and how close that is to the
> curve is the question every error tile on this path answers for one step
> size only.

---

## §B The ten courses

Course slugs are global URL segments; none below collides with the 68 existing
course slugs. Release-contract check ids use the prefix `de`, so
`de-course10-lesson-` leaves 53 characters for a lesson slug; the longest id
here is 64 (`de-course2-lesson-the-antiderivative-and-the-fundamental-theorem`).
Every slug is ≤ 47 characters. Levels use the library's vocabulary.

| n | slug | package | title | level | lessons |
| --- | --- | --- | --- | --- | --- |
| 1 | `rates-of-change-and-the-derivative` | `c1_rates` | Rates of Change and the Derivative | Beginner → Intermediate | 11 |
| 2 | `accumulation-and-the-integral` | `c2_accumulation` | Accumulation and the Integral | Intermediate | 8 |
| 3 | `differential-equations-and-eulers-method` | `c3_euler` | Differential Equations and Euler's Method | Intermediate | 10 |
| 4 | `separable-equations-growth-and-decay` | `c4_separable` | Separable Equations, Growth and Decay | Intermediate | 10 |
| 5 | `equilibria-stability-and-phase-lines` | `c5_phase_lines` | Equilibria, Stability and Phase Lines | Intermediate → Advanced | 8 |
| 6 | `first-order-linear-equations` | `c6_linear` | First-Order Linear Equations | Advanced | 8 |
| 7 | `second-order-linear-equations` | `c7_second_order` | Second-Order Linear Equations | Advanced | 10 |
| 8 | `oscillators-damping-and-resonance` | `c8_oscillators` | Oscillators, Damping and Resonance | Advanced | 9 |
| 9 | `systems-and-the-phase-plane` | `c9_systems` | Systems and the Phase Plane | Advanced | 10 |
| 10 | `laplace-transforms` | `c10_laplace` | Laplace Transforms | Advanced | 8 |

Total: 92 lessons, 10 course homes, 1 path page = 103 pages (853 become 956).

**1. Rates of Change and the Derivative** (Beginner → Intermediate; assumes
Algebra's Lines, Functions and Graphs and Polynomials and Factoring). The
average rate of change as an exact difference quotient; the quotient of a
polynomial as a polynomial in `h` and its constant term; what the quotients
approach, shown as a halving column and stated as a claim; the derivative at a
point, the tangent line and the exact error of local linearity; the derivative
of `1/t`; the derivative as a function, the power rule, where the rate is zero;
the product and chain rules verified exactly on polynomials; the second
derivative and concavity; the exponential, whose quotients are rounded and
labelled, and the base `e` where the rate equals the value.

**2. Accumulation and the Integral** (Intermediate; assumes Rates of Change
and the Derivative). Total change as a sum of rate times step; left and right
sums and the exact gap between them; refining the partition; trapezoid and
midpoint rules with exact errors and exact error ratios; the antiderivative
and the fundamental theorem as a demonstrated claim — the sums approach
`F(b) − F(a)`, which is printed beside them; the constant of integration fixed
by an initial value; the integral sign and its rules; and `∫ dt/t`, whose
exact sums bracket a number that is not a fraction.

**3. Differential Equations and Euler's Method** (Intermediate; assumes
Accumulation and the Integral). What a differential equation is and what a
solution is; checking a candidate by substitution, exactly; initial value
problems and the constant; slope fields and how to read one; Euler's method as
exact fractions; its error and the step size, with the ratio exactly 2 on one
equation; the improved Euler method with ratio exactly 4; Runge–Kutta, exact
on cubics; blow-up, the interval of existence, and the digit budget.

**4. Separable Equations, Growth and Decay** (Intermediate; assumes
Differential Equations and Euler's Method). Separable equations and why
separating works (the chain rule in reverse); implicit against explicit
solutions and the branch an initial value picks; `y′ = ky`, with Euler's exact
geometric sequence beside `e^(kt)`; doubling time and half-life; decay and
dating; Newton's law of cooling and mixing problems as shifted exponentials;
logistic growth and harvesting with the threshold `rK/4`.

**5. Equilibria, Stability and Phase Lines** (Intermediate → Advanced;
assumes Separable Equations, Growth and Decay). Autonomous equations; the
phase line from the sign of `f`; stable, unstable and semistable equilibria;
linearisation and the sign of `f′(y*)`; long-run behaviour read without
solving; one-parameter families and bifurcation diagrams; sketching solution
curves from the phase line, with the inflection level computed.

**6. First-Order Linear Equations** (Advanced; assumes Equilibria, Stability
and Phase Lines). The standard form; constant coefficients and the steady
state; the integrating factor as the product rule run backwards, with
`μ = tᵃ` cases that are exact throughout; homogeneous plus particular;
polynomial, exponential and sinusoidal forcing by undetermined coefficients;
circuits, tanks and loans as one equation; stiffness, where Euler's factor
`1 − ah` leaves `(−1, 1)` and the backward method does not.

**7. Second-Order Linear Equations** (Advanced; assumes First-Order Linear
Equations and Algebra's Quadratics and Complex Numbers). Sine and cosine as
each other's rates; the second-order equation and its two constants; the
characteristic equation; real distinct, repeated and complex roots, each
verified by exact substitution; fitting initial conditions as a 2×2 system;
superposition and the Wronskian; the equation rewritten as a system; and Euler
on an oscillator, where the radius grows by exactly `1 + h²` per step.

**8. Oscillators, Damping and Resonance** (Advanced; assumes Second-Order
Linear Equations). The mass–spring model; amplitude, phase and period; energy
and the phase ellipse; overdamped, critical and underdamped motion; the
underdamped envelope; critical damping as a design choice; forced oscillation
and its exact amplitude; resonance and beats; damped forcing and the amplitude
curve, with the resonant frequency exact.

**9. Systems and the Phase Plane** (Advanced; assumes Oscillators, Damping
and Resonance and Algebra's Systems and Matrices). Systems of two equations;
straight-line solutions and eigenvectors; the general solution; saddles,
nodes, spirals and centres on the trace–determinant plane; stability of the
origin; nonlinear systems and their equilibria; linearisation and the
Jacobian; predator and prey; competing species; an epidemic model with its
threshold.

**10. Laplace Transforms** (Advanced; assumes Systems and the Phase Plane and
Algebra's Rational and Radical Expressions). The transform as an exact
rational function of `s`; linearity and the table; the transform of a
derivative; solving an initial value problem by algebra; partial fractions,
exactly; the transfer function and its poles; the unit step and switched
forcing; and the same equation solved three ways.

---
## §C Every lesson

Format of each entry:

- **slug** — Title — *module*
- **Do:** the observable objective (what the reader can do at the end; the
  `standard` field measures it).
- **Lab:** key / mode; the presets by id with their instance; the shipped
  values of redraw-only controls; which tiles each preset must pin.
- **Misconception:** the one wrong model the lesson must name in `mistakes[0]`.
- **Worked:** the single worked example, in one line, with its arithmetic.

Preset ids are suggestions an author may rename; the INSTANCES are not optional.
Every preset pins at least one tile; "pin" names the tiles that say why the
preset exists (rule 4 of `scripts/mathpath/AGENTS.md`). Expected strings are
read off the built page with `node scripts/labcheck.js --observe`, never
predicted — the formats in §D tell you what shape to expect. The arithmetic in
every "Worked" line below was checked by hand while this document was written;
an author who finds the lab disagreeing with it reports the disagreement rather
than copying either.

Right-hand sides, candidates and polynomials are typed in the ASCII the parser
reads (`t^2`, `2e^(-t)`, `y'`) and written in the prose in the library's
notation (`t²`, `2·e^(−t)`, `y′`). The two are never mixed in one place.

Cross-references in prose are by TITLE, in curly quotes for lessons (“Euler's
Method”) and plain for courses (Accumulation and the Integral). Never a number.
Algebra lessons are cited the same way, with the course named: “The Quadratic
Formula” in Algebra's Quadratics and Complex Numbers.

### Course 1 — Rates of Change and the Derivative (`rates-of-change-and-the-derivative`, 11)

Modules: *Average rates* (1–2), *The derivative at a point* (3–5), *The
derivative as a function* (6–9), *Second derivatives and the exponential*
(10–11).

1. **average-rate-of-change** — Average Rate of Change — *Average rates*
   - Do: compute the average rate of change of a function over `[a, a + h]` as an exact fraction, read it as the slope of a secant, and say what changes when `h` changes.
   - Lab: `calckit`/`quotient`, `show_limit: false`. Presets: `square` (`t^2`, a = 1, h = 1, 4 halvings), `cubic` (`t^3 - t`, a = 2, h = 1, 4 halvings), `line` (`3t + 1`, a = 5, h = 1: every quotient is 3). Pin `qtFirst`, `qtLast`.
   - Misconception: the average rate is `f(a + h)/h`, or is `f(a + h) − f(a)` with the division forgotten.
   - Worked: `f(t) = t²` at `a = 1`: `h = 1` gives `(4 − 1)/1 = 3`; `h = 1/2` gives `(9/4 − 1)/(1/2) = 5/2`; `h = 1/4` gives `9/4`; the slope of the secant through `(1, 1)` and `(1 + h, (1 + h)²)` is `2 + h`.

2. **the-quotient-as-a-polynomial-in-h** — The Difference Quotient as a Polynomial in h — *Average rates*
   - Do: expand `(p(t + h) − p(t))/h` for a polynomial `p`, cancel the `h`, and read off the part that does not depend on `h`.
   - Lab: `calckit`/`hpoly`, `kind: single`. Presets: `square` (`t^2`: quotient `2t + h`), `cube` (`t^3`: `3t² + 3th + h²`), `quartic` (`t^4 - 2t^2`: `4t³ − 4t + 6t²h + 4th² + h³ − 2h`). Shipped `a` empty (symbolic `t`). Pin `hpQ`, `hpConst`.
   - Misconception: the `h` in the denominator can be set to zero before it is cancelled.
   - Worked: `p(t) = t³`: `(t + h)³ − t³ = 3t²h + 3th² + h³`; divide by `h`: `3t² + 3th + h²`; the constant term in `h` is `3t²`.

3. **what-the-quotients-approach** — What the Quotients Approach — *The derivative at a point*
   - Do: produce the column of exact quotients for halving `h`, state the number they approach, and say in one sentence what "approach" claims and what the table shows.
   - Lab: `calckit`/`quotient`. Presets: `square` (`t^2`, a = 1, h = 1, 6 halvings: `3, 5/2, 9/4, 17/8, 33/16, 65/32, 129/64 → 2`), `cube` (`t^3`, a = 1, h = 1, 6 halvings → 3), `flat` (`t^2`, a = 0: every quotient is `h` itself → 0). Pin `qtLast`, `qtGap`, `qtLimit`.
   - Misconception: the quotients reach the limit at some finite `h`, or the limit is "the last entry in the table".
   - Worked: `t²` at `1`: the gaps `|quotient − 2|` are `1, 1/2, 1/4, 1/8, …`, exactly `h`, because the quotient is `2 + h`; the table shows seven rows and the claim is about every `h`.

4. **the-derivative-at-a-point** — The Derivative at a Point and the Tangent Line — *The derivative at a point*
   - Do: define `f′(a)` as the number the quotients approach, write the tangent line `y = f(a) + f′(a)·(t − a)`, and compute the exact error of the linear approximation at `a + h`.
   - Lab: `calckit`/`tangent`. Presets: `square` (`t^2`, a = 2, h = 1/10: error exactly `1/100`), `cube` (`t^3`, a = 1, h = 1/10: error `31/1000`), `recip` (`1/t`, a = 1, h = 1/2: approximation `1/2`, true `2/3`, error `1/6`). Pin `tgSlope`, `tgLine`, `tgError`.
   - Misconception: the tangent line "touches at one point only", so it cannot be used to estimate nearby values.
   - Worked: `f(t) = t²`, `a = 2`: `f(2) = 4`, `f′(2) = 4`, tangent `y = 4t − 4`; at `t = 21/10` the line gives `22/5 = 440/100` and `f` gives `441/100`; the error is `1/100 = h²`.

5. **the-derivative-of-one-over-t** — The Derivative of 1/t — *The derivative at a point*
   - Do: compute the quotients of `1/t` exactly by combining fractions, show the quotient simplifies to `−1/(a(a + h))`, and state `f′(a) = −1/a²`.
   - Lab: `calckit`/`quotient`. Presets: `two` (`1/t`, a = 2, h = 1, 5 halvings: `−1/6, −1/5, −2/9, −4/17, −8/33, −16/65 → −1/4`), `one` (`1/t`, a = 1: `−1/2, −2/3, −4/5, −8/9, … → −1`), `half` (`1/t`, a = 1/2 → −4). Pin `qtFirst`, `qtLast`, `qtLimit`.
   - Misconception: the derivative of `1/t` is `1/1 = 1`, or is `ln t`.
   - Worked: `a = 2`, `h = 1/4`: `1/(9/4) − 1/2 = 4/9 − 1/2 = −1/18`; divided by `1/4` is `−2/9`, which is `−1/(2·(9/4))`; as `h → 0` this goes to `−1/4`.

6. **the-derivative-as-a-function** — The Derivative as a Function — *The derivative as a function*
   - Do: differentiate a polynomial term by term with the power rule, and read where the graph rises and falls off the sign of `p′`.
   - Lab: `calckit`/`derivative`, `order: 1`. Presets: `hill` (`t^3 - 6t^2 + 9t`: `p′ = 3t² − 12t + 9`, zeros `1, 3`), `bowl` (`t^2 - 4t`: `2t − 4`, zero 2), `wave` (`t^4 - 2t^2`: `4t³ − 4t`, zeros `−1, 0, 1`). Pin `dvDeriv`, `dvZeros`.
   - Misconception: the derivative of `tⁿ` is `tⁿ⁻¹` (the coefficient `n` forgotten), or the derivative of a constant is 1.
   - Worked: `p(t) = t³ − 6t² + 9t`: `p′(t) = 3t² − 12t + 9 = 3(t − 1)(t − 3)`; `p′ > 0` for `t < 1`, `p′ < 0` on `(1, 3)`, `p′ > 0` for `t > 3`, which is what the graph does.

7. **where-the-rate-is-zero** — Where the Rate Is Zero — *The derivative as a function*
   - Do: solve `p′(t) = 0` exactly for a polynomial with rational critical points, classify each as a maximum or minimum from the sign change, and say why `p′ = 0` is necessary and not sufficient.
   - Lab: `calckit`/`derivative`, `order: 1`. Presets: `two-turns` (`2t^3 - 3t^2 - 12t + 1`: `p′ = 6(t − 2)(t + 1)`), `flat-step` (`t^3`: `p′ = 3t²`, zero at 0 with no sign change), `none` (`t^3 + t`: `3t² + 1`, no real zero). Pin `dvZeros`, `dvIntervals`.
   - Misconception: every point where `p′ = 0` is a maximum or a minimum.
   - Worked: `p = t³`: `p′ = 3t²` is zero at `t = 0` and positive on both sides; the graph flattens and keeps rising, and the lab's interval tile reads `rising t < 0; rising t > 0`.

8. **the-product-rule** — The Product Rule — *The derivative as a function*
   - Do: state `(f·g)′ = f′g + fg′`, verify it exactly on two polynomials by comparing the expanded derivative with the rule's output, and explain why it is not `f′g′`.
   - Lab: `calckit`/`hpoly`, `kind: product`. Presets: `basic` (`f = t^2`, `g = t + 1`: both sides `3t² + 2t`), `wrong-rule` (same, with the tile `hpRule` also printing `f′g′ = 2t` so the two can be compared), `cubic` (`f = t^3 - t`, `g = t^2 + 2`). Pin `hpConst`, `hpRule`, `hpEqual`.
   - Misconception: the derivative of a product is the product of the derivatives.
   - Worked: `f = t²`, `g = t + 1`: `fg = t³ + t²`, `(fg)′ = 3t² + 2t`; the rule gives `2t·(t + 1) + t²·1 = 3t² + 2t`; `f′g′ = 2t` is not it.

9. **the-chain-rule** — The Chain Rule — *The derivative as a function*
   - Do: differentiate `f(k·t + c)` and `(u(t))ⁿ` with the chain rule, verify exactly on polynomials, and name the inner derivative that the rule multiplies by.
   - Lab: `calckit`/`hpoly`, `kind: compose`. Presets: `stretch` (`f = t^2`, inner `3t + 1`: `18t + 6`), `power` (`f = t^3`, inner `t^2 + 1`: `6t(t² + 1)² = 6t⁵ + 12t³ + 6t`), `shift` (`f = t^2`, inner `t - 4`: `2t − 8`). Pin `hpConst`, `hpRule`, `hpEqual`.
   - Misconception: `(f(3t + 1))′ = f′(3t + 1)` with the factor 3 missing.
   - Worked: `f(t) = t²` composed with `3t + 1` is `9t² + 6t + 1`, whose derivative is `18t + 6`; the chain rule gives `2·(3t + 1)·3 = 18t + 6`.

10. **the-second-derivative** — The Second Derivative — *Second derivatives and the exponential*
    - Do: compute `p″`, read concavity off its sign, locate inflection points as its rational zeros, and say what a second derivative measures in words (the rate of the rate).
    - Lab: `calckit`/`derivative`, `order: 2`. Presets: `s-curve` (`t^3 - 3t^2`: `p″ = 6t − 6`, inflection at 1), `quartic` (`t^4 - 6t^2`: `12t² − 12`, inflections `±1`), `parabola` (`t^2`: `p″ = 2`, no inflection). Pin `dvSecond`, `dvInflect`.
    - Misconception: an inflection point is where `p′ = 0`.
    - Worked: `p = t³ − 3t²`: `p′ = 3t² − 6t`, `p″ = 6t − 6`; `p″ < 0` for `t < 1` (concave down) and `p″ > 0` for `t > 1`; the inflection is at `t = 1`, where `p′ = −3 ≠ 0`.

11. **the-exponential-and-its-rate** — The Exponential and Its Rate — *Second derivatives and the exponential*
    - Do: show that the quotient of `bᵗ` factors as `bᵗ·(bʰ − 1)/h`, read the second factor off a rounded table, and state that the derivative of `bᵗ` is a constant times `bᵗ`, with `e` the base whose constant is 1.
    - Lab: `calckit`/`transcendental`, `kind: exp`. Presets: `two` (b = 2, a = 0, h = 1 with 6 halvings: `1, ≈ 0.828427, ≈ 0.756828, … → ln 2 ≈ 0.693147`), `three` (b = 3: `2, … → ≈ 1.09861`), `e` (b = e, typed as `e`: `≈ 1.71828, … → 1`). Pin `tqFirst`, `tqLimit`, `tqRatio`.
    - Misconception: the derivative of `2ᵗ` is `t·2ᵗ⁻¹` (the power rule applied to an exponential).
    - Worked: `2ᵗ` at `a = 0`: `h = 1` gives exactly `1`; `h = 1/2` gives `2(√2 − 1) ≈ 0.828427`, rounded and labelled; the column heads for `ln 2 ≈ 0.693147`, and the quotient at any `a` is `2ᵃ` times the same column.

### Course 2 — Accumulation and the Integral (`accumulation-and-the-integral`, 8)

Modules: *Adding up a rate* (1–4), *The exact total* (5–6), *Notation and a
second integral* (7–8).

1. **total-change-from-a-rate** — Total Change from a Rate — *Adding up a rate*
   - Do: compute total change over an interval from a rate by adding rate × step across the pieces, exactly, and state what is being assumed about the rate inside each piece.
   - Lab: `calckit`/`riemann`, `rule: left`. Presets: `ramp` (`2t` on `[0, 2]`, n = 4: `L = 3`, `R = 5`, exact 4), `speed` (`t^2 + 1` on `[0, 3]`, n = 3: `L = 8`, exact 12), `constant` (`3` on `[1, 5]`, n = 4: every sum is 12). Pin `rsSum`, `rsExact`.
   - Misconception: total change is the rate at the end times the elapsed time.
   - Worked: rate `2t` over `[0, 2]` in four pieces of width `1/2`, using the rate at each left end: `(1/2)(0 + 1 + 2 + 3) = 3`; the true total is `4`, and the lesson says why the left sum is low.

2. **left-and-right-sums** — Left and Right Sums — *Adding up a rate*
   - Do: compute `Lₙ` and `Rₙ` exactly, show their gap is `h·(f(b) − f(a))` for a monotone rate, and bracket the true total between them.
   - Lab: `calckit`/`riemann`. Presets: `ramp` (`2t`, `[0, 2]`, n = 4: gap `2`), `square` (`t^2`, `[0, 1]`, n = 4: `L = 7/32`, `R = 15/32`, gap `1/4`), `falling` (`4 - t`, `[0, 2]`, n = 4: `L > R`). Shipped `rule = left`. Pin `rsSum`, `rsGap`.
   - Misconception: the right sum is always the overestimate.
   - Worked: `t²` on `[0, 1]`, `n = 4`: `L₄ = (1/4)(0 + 1/16 + 4/16 + 9/16) = 7/32`, `R₄ = 15/32`; `R₄ − L₄ = (1/4)(1 − 0) = 1/4`; the true value `1/3` lies between.

3. **refining-the-partition** — Refining the Partition — *Adding up a rate*
   - Do: double `n` repeatedly, watch the exact sums close in on a number, and state the claim (they approach the exact total) separately from what the table shows.
   - Lab: `calckit`/`riemann`. Presets: `square` (`t^2`, `[0, 1]`, n = 4 → 8 → 16: `7/32, 35/128, 155/512`; errors `11/96, 23/384, 47/1536`; ratios `44/23 ≈ 1.91304`, `92/47 ≈ 1.95745`), `cubic` (`t^3`, `[0, 2]`, n = 4), `ramp` (`2t`, `[0, 2]`: error exactly `h·2`, ratio exactly 2). Shipped `rule = left`. Pin `rsSum`, `rsError`, `rsRatio`.
   - Misconception: doubling `n` halves the error exactly for every rate.
   - Worked: `t²` on `[0, 1]`: `L₈ = (1/512)(0 + 1 + 4 + 9 + 16 + 25 + 36 + 49) = 140/512 = 35/128`; the error `1/3 − 35/128 = 23/384`, against `11/96` at `n = 4`: the ratio `44/23` is close to 2 and is not 2.

4. **trapezoid-and-midpoint-rules** — The Trapezoid and Midpoint Rules — *Adding up a rate*
   - Do: compute `Tₙ = (Lₙ + Rₙ)/2` and the midpoint sum `Mₙ` exactly, and show that on a quadratic the trapezoid error quarters exactly when `n` doubles while the midpoint error is half of it and opposite in sign.
   - Lab: `calckit`/`riemann`. Presets: `trap` (`t^2`, `[0, 1]`, n = 4, rule trap: `11/32`, error `1/96`; at n = 8 `43/128`, error `1/384`, ratio exactly `4`), `mid` (same, rule mid: `21/64`, error `−1/192`), `quartic` (`t^4`, `[0, 1]`, trap: ratio approaches 4 and is not 4 — on a cubic it is still exactly 4, which the lesson may mention and must not pin as "approaches"). Shipped `rule` as the preset names (`trap` for the first and third, `mid` for the second — a redraw-only select can ship one value only; ship `trap`, and the `mid` preset's `expect` pins what the page prints under `trap`, with the midpoint figure in the lesson prose and a comment, rule 6). Pin `rsSum`, `rsError`, `rsRatio`.
   - Misconception: the trapezoid rule is exact for every polynomial because it "uses both ends".
   - Worked: `t²` on `[0, 1]`: `T₄ = (7/32 + 15/32)/2 = 11/32`, error `1/96`; `T₈ = 43/128`, error `1/384`; `(1/96)/(1/384) = 4` exactly; `M₄ = (1/4)(1 + 9 + 25 + 49)/64 = 21/64`, error `1/3 − 21/64 = 1/192`.

5. **the-antiderivative-and-the-fundamental-theorem** — The Antiderivative and the Fundamental Theorem — *The exact total*
   - Do: find `F` with `F′ = f` by reversing the power rule, compute `F(b) − F(a)` exactly, and state the fundamental theorem as the claim the refining sums demonstrated.
   - Lab: `calckit`/`antiderivative`. Presets: `square` (`t^2`, `[0, 1]`: `F = t³/3 + C`, `F(1) − F(0) = 1/3`), `ramp` (`2t`, `[0, 2]`: `t² + C`, 4), `mixed` (`3t^2 - 4t + 1`, `[1, 3]`: `t³ − 2t² + t`, value `12`). Pin `adF`, `adDefinite`.
   - Misconception: the antiderivative of `tⁿ` is `tⁿ⁺¹` (the division by `n + 1` forgotten), or `F(b) − F(a)` depends on which `C` was chosen.
   - Worked: `f = t²`: `F = t³/3`; `F(1) − F(0) = 1/3`, the number the sums `7/32, 35/128, 155/512, …` of “Refining the Partition” were closing in on.

6. **the-constant-of-integration** — The Constant of Integration — *The exact total*
   - Do: write the family `F + C`, fix `C` from one given value, and say why one value is exactly enough.
   - Lab: `calckit`/`antiderivative`. Presets: `through-five` (`2t`, ic `y(1) = 5`: `C = 4`, `y = t² + 4`), `through-zero` (`3t^2`, ic `y(2) = 0`: `C = −8`), `cubic` (`t^3 - t`, ic `y(0) = 1/2`: `C = 1/2`). Pin `adF`, `adC`.
   - Misconception: the constant is "always zero unless told otherwise".
   - Worked: `y′ = 2t`, `y(1) = 5`: `y = t² + C`, `1 + C = 5`, `C = 4`; the lab draws the family and the one member through `(1, 5)`.

7. **the-integral-sign-and-its-rules** — The Integral Sign and Its Rules — *Notation and a second integral*
   - Do: read `∫ₐᵇ f(t) dt` aloud and in words, and check linearity and additivity over adjacent intervals by computing both sides exactly.
   - Lab: `calckit`/`antiderivative`. Presets: `linear` (`f = 3t^2`, `g = 2t`, coefficients `1, 1`, `[0, 2]`: `∫(3t² + 2t) = 12 = 8 + 4`), `scaled` (`f = t^2`, `g = t`, coefficients `6, −2`, `[0, 1]`: `2 − 1 = 1`), `split` (`3t^2 + 2t`, `[0, 2]` split at 1: `2 + 10 = 12`). Pin `adDefinite`, `adLinear`, `adSplit`.
   - Misconception: `∫ f·g = ∫f · ∫g`.
   - Worked: `∫₀² (3t² + 2t) dt = [t³ + t²]₀² = 12`; separately `∫₀² 3t² dt = 8` and `∫₀² 2t dt = 4`; `∫₀¹ + ∫₁² = (1 + 1) + (7 + 3) = 12`.

8. **the-integral-of-one-over-t** — The Integral of 1/t — *Notation and a second integral*
   - Do: compute exact left, right and trapezoid sums for `∫₁² dt/t`, show they bracket a number with no fraction form, and state the claim `∫₁ˣ dt/t = ln x`.
   - Lab: `calckit`/`riemann`. Presets: `ln2` (`1/t`, `[1, 2]`, n = 4: `L = 319/420 ≈ 0.759524`, `R = 533/840 ≈ 0.634524`; exact tile `≈ 0.693147 (ln 2, rounded)`), `ln4` (`[1, 4]`, n = 6: brackets `ln 4 ≈ 1.38629 = 2 ln 2`), `ln3` (`[1, 3]`). Shipped `rule = left`. Pin `rsSum`, `rsExact`.
   - Misconception: `∫ dt/t = t⁰/0`, by the power rule.
   - Worked: `n = 4`, `h = 1/4`: `L₄ = (1/4)(1 + 4/5 + 2/3 + 4/7) = 319/420`, `R₄ = 533/840`, `T₄ = 1171/1680 ≈ 0.697024`; `ln 2 ≈ 0.693147` sits between `R₄` and `L₄`, and no refinement makes it a fraction.

### Course 3 — Differential Equations and Euler's Method (`differential-equations-and-eulers-method`, 10)

Modules: *What a differential equation is* (1–3), *Pictures of solutions*
(4–5), *Stepping* (6–9), *When solutions misbehave* (10).

1. **what-a-differential-equation-is** — What a Differential Equation Is — *What a differential equation is*
   - Do: say what a differential equation is (an equation whose unknown is a function, stated through its rate), name its order, and test a candidate by substituting and reading the residual.
   - Lab: `dekit`/`verify`. Presets: `square` (`y' = 2t`, candidate `t^2`: residual 0), `shifted` (`y' = 2t`, candidate `t^2 + 3`: 0), `cube` (`y' = 2t`, candidate `t^3`: residual `3t² − 2t`, not a solution). Pin `vfOrder`, `vfResidual`, `vfVerdict`.
   - Misconception: a differential equation has a number for an answer.
   - Worked: `y′ = 2t` with `y = t³`: `y′ = 3t²`, residual `3t² − 2t ≠ 0`; with `y = t² + 3`: `y′ = 2t`, residual `0`, so it is a solution, and so is `t² + C` for every `C`.

2. **checking-a-proposed-solution** — Checking a Proposed Solution — *What a differential equation is*
   - Do: substitute an exponential or a power into a second-order or variable-coefficient equation, simplify the residual symbolically, and decide; classify the equation as linear or not.
   - Lab: `dekit`/`verify`. Presets: `two-exps` (`y'' - y' - 2y = 0`, candidate `e^(2t)`: `4 − 2 − 2 = 0`), `wrong-exp` (same, candidate `e^t`: residual `−2·e^t`), `power` (`t y' = 2y`, candidate `5t^2`: 0), `nonlinear` (`y' = y^2`, candidate `1/(1 - t)`: residual 0, `vfLinear` = `Nonlinear`). Pin `vfLinear`, `vfResidual`, `vfVerdict`.
   - Misconception: a function that satisfies the equation at one value of `t` is a solution.
   - Worked: `y″ − y′ − 2y = 0` with `y = e^(2t)`: `y′ = 2e^(2t)`, `y″ = 4e^(2t)`; `4e^(2t) − 2e^(2t) − 2e^(2t) = 0`; with `y = eᵗ` the residual is `−2eᵗ`, which is never zero.

3. **initial-value-problems** — Initial Value Problems — *What a differential equation is*
   - Do: fix the constant in a family of solutions from one initial value, state how many values a first- and a second-order equation need, and check the result.
   - Lab: `dekit`/`verify`. Presets: `first` (`y' = 2t`, candidate `t^2 + C`, ic `y(1) = 5`: `C = 4`), `growth` (`y' = 3y`, candidate `C e^(3t)`, ic `y(0) = 2`: `C = 2`), `second` (`y'' + y = 0`, candidate `C cos(t) + D sin(t)`, ic `y(0) = 1, y'(0) = −2`: `C = 1, D = −2`). Pin `vfFamily`, `vfIC`.
   - Misconception: the initial condition is "where `t` starts" rather than a value that selects one solution.
   - Worked: `y′ = 2t`, `y(1) = 5`: `y = t² + C`, `1 + C = 5`, `C = 4`; the lab reports `C = 4 from y(1) = 5` and the residual stays `0`.

4. **slope-fields** — Slope Fields — *Pictures of solutions*
   - Do: compute the slope `f(t, y)` at a grid point exactly, draw the short segment, and find the nullcline where the slope is zero.
   - Lab: `dekit`/`field`. Presets: `t-minus-y` (`t - y`, window `−3..3`, point `(1, 1)`: slope `0`; nullcline `y = t`), `y-only` (`y`, point `(0, 1)`: slope 1; nullcline `y = 0`), `t-only` (`2t`, point `(1, 2)`: slope 2; nullcline `t = 0`, printed as `none in y`). Shipped `grid = 15`. Pin `sfSlope`, `sfZero`.
   - Misconception: the segment at `(t, y)` shows where the solution goes next, rather than its slope there.
   - Worked: `y′ = t − y` at `(2, 0)`: slope `2`; at `(1, 1)`: slope `0`; the points with slope zero are the line `y = t`, and every solution crosses it horizontally.

5. **reading-a-slope-field** — Reading a Slope Field — *Pictures of solutions*
   - Do: read horizontal solutions, long-run behaviour and where solutions cannot cross off a slope field, and say which of those the field settles and which it only suggests.
   - Lab: `dekit`/`field`. Presets: `logistic` (`y(1 - y)`: horizontal solutions `y = 0, y = 1`), `t-minus-y` (`t - y`, start `(0, 2)`: the drawn solution approaches the line `y = t − 1`), `square` (`y^2`, start `(0, 1)`: the drawn solution leaves the window before `t = 1`). Shipped `grid = 15`. Pin `sfEquil`, `sfSlope`.
   - Misconception: solution curves can cross each other.
   - Worked: `y′ = y(1 − y)`: the slope is `0` exactly on `y = 0` and `y = 1`, positive between them and negative outside; a solution starting at `y = 1/2` rises towards `1` and never reaches it, because reaching it would mean two solutions through one point.

6. **eulers-method** — Euler's Method — *Stepping*
   - Do: carry out `yₙ₊₁ = yₙ + h·f(tₙ, yₙ)` by hand for three steps as exact fractions, read the table, and say what the method assumes inside each step.
   - Lab: `dekit`/`euler`. Presets: `growth` (`y`, start `(0, 1)`, h = 1/4, n = 4, exact `e^t`: `5/4, 25/16, 125/64, 625/256 ≈ 2.44141`; exact `≈ 2.71828`), `ramp` (`2t`, start `(0, 0)`, h = 1/4, n = 4, exact `t^2`: `y₄ = 3/4`, error exactly `1/4`), `mixed` (`t - y`, start `(0, 2)`, h = 1/2, n = 4, exact `t - 1 + 3e^(-t)`). Pin `euLast`, `euError`.
   - Misconception: Euler's method gives the solution, and more steps make it exact.
   - Worked: `y′ = y`, `y(0) = 1`, `h = 1/4`: `y₁ = 1 + (1/4)·1 = 5/4`, `y₂ = 5/4 + (1/4)(5/4) = 25/16`, `y₃ = 125/64`, `y₄ = 625/256 ≈ 2.44141`; the true `y(1) = e ≈ 2.71828`; every `yₙ` is `(5/4)ⁿ`.

7. **eulers-error-and-the-step-size** — Euler's Error and the Step Size — *Stepping*
   - Do: measure the error at `T` for `h, h/2, h/4`, form the exact ratios, and state Euler's method is first order: halving `h` roughly halves the error, and on `y′ = 2t` exactly.
   - Lab: `dekit`/`order`, `method: euler`. Presets: `ramp` (`2t`, `(0, 0)`, `T = 1`, exact `t^2`, `h = 1/4, 1/8, 1/16`: errors `1/4, 1/8, 1/16`, ratios `2, 2`, order `1`), `square` (`t^2`, `(0, 0)`, exact `t^3/3`: errors `11/96, 23/384, 47/1536`, ratios `44/23, 92/47`, order `≈ 0.969`), `growth` (`y`, `(0, 1)`, exact `e^t`: errors rounded). Pin `odE1`, `odRatio`, `odOrder`.
   - Misconception: the error is the error of the last step, rather than the accumulation of every step.
   - Worked: `y′ = 2t` to `T = 1`: Euler is the left sum of `2t`, so `E(h) = 1 − (1 − h) = h` exactly; `1/4, 1/8, 1/16`; ratio `2` twice; first order, and here exactly.

8. **the-improved-euler-method** — The Improved Euler Method — *Stepping*
   - Do: take a trial Euler step, average the slopes at both ends, and show the error quarters when `h` halves — exactly on `y′ = t²`.
   - Lab: `dekit`/`order`, `method: heun`. Presets: `square` (`t^2`, `(0, 0)`, `T = 1`, exact `t^3/3`: errors `1/96, 1/384, 1/1536`, ratios `4, 4`, order `2`), `quartic` (`t^4`, exact `t^5/5`: ratios approach 4 and are not 4; on `t^3` the ratio is still exactly 4, because the trapezoid error on any cubic is exactly `h²·(f′(b) − f′(a))/12`), `growth` (`y`, exact `e^t`, rounded). Shipped `method = heun`. Pin `odE1`, `odRatio`, `odOrder`.
   - Misconception: a second-order method has half the error of a first-order one.
   - Worked: on `y′ = t²` the improved step is the trapezoid rule, so `E(h) = Tₙ − 1/3`: `1/96, 1/384, 1/1536`; the ratio is exactly `4`, because the trapezoid error on a quadratic is exactly proportional to `h²`.

9. **runge-kutta-four-slopes-per-step** — Runge–Kutta: Four Slopes per Step — *Stepping*
   - Do: write the four slopes of RK4 and their weights `1, 2, 2, 1`, show the method is exact on `y′ = t³`, and that on `y′ = t⁴` the error ratio is exactly 16.
   - Lab: `dekit`/`order`, `method: rk4`. Presets: `cubic` (`t^3`, `(0, 0)`, `T = 1`, exact `t^4/4`: every error `0`), `quartic` (`t^4`, exact `t^5/5`: errors `1/30720, 1/491520, 1/7864320`, ratios `16, 16`, order `4`), `growth` (`y`, exact `e^t`: rounded errors, order `≈ 4`). Shipped `method = rk4`. Pin `odE1`, `odRatio`, `odOrder`.
   - Misconception: RK4 is "four Euler steps", so it costs the same as Euler with `h/4` and does no better.
   - Worked: `y′ = t⁴`, one step `h = 1` from 0: `(1/6)(0 + 4·(1/2)⁴ + 1) = 5/24`; true `1/5`; error `1/120`, which is `h⁴/120`; at `h = 1/4` over `[0, 1]` the error is `1/30720`, and halving `h` divides it by exactly `16`.

10. **blow-up-and-the-interval-of-existence** — Blow-Up and the Interval of Existence — *When solutions misbehave*
    - Do: show `y = 1/(1 − t)` solves `y′ = y²` and ceases to exist at `t = 1`, watch Euler step past the asymptote without noticing, and read the digit budget: a quadratic right-hand side doubles the digits each step.
    - Lab: `dekit`/`euler`. Presets: `square` (`y^2`, `(0, 1)`, h = 1/4, n = 3, exact `1/(1 - t)`: `5/4, 105/64, 37905/16384`; exact at `3/4` is `4`; error `27631/16384`), `past` (same, n = 5: Euler produces a finite `y₅` at `t = 5/4` where no solution exists; the exact tile reads `undefined at t = 5/4`), `budget` (same, n = 16: `euStopped` = `stopped after step 11: digit budget`). Pin `euLast`, `euExact`, `euStopped`.
    - Misconception: a differential equation with a smooth right-hand side has a solution for all `t`.
    - Worked: `y′ = y²`, `y(0) = 1`: `y₁ = 5/4`, `y₂ = 5/4 + (1/4)(25/16) = 105/64`, `y₃ = 105/64 + (1/4)(105/64)² = 37905/16384 ≈ 2.31354`; the true `y(3/4) = 4`; the denominators `4, 64, 16384 = 2³⁰` have `1, 2, 5, 10` digits and then `19, 38, 77, …`, doubling — the lab stops when one passes 2000 digits, after step 11.

### Course 4 — Separable Equations, Growth and Decay (`separable-equations-growth-and-decay`, 10)

Modules: *Separating variables* (1–3), *Exponential change* (4–7), *Shifted
and bounded growth* (8–10).

1. **separable-equations** — Separable Equations — *Separating variables*
   - Do: recognise `g(y)·y′ = h(t)`, integrate both sides exactly, and write the implicit solution with its constant fixed by an initial value.
   - Lab: `dekit`/`separable`, `view: solve`. Presets: `circle` (`g = y`, `h = t`, ic `y(0) = 2`: `y²/2 = t²/2 + C`, `C = 2`, `y² = t² + 4`, explicit `y = √(t² + 4)`), `recip` (`g = 1/y^2`, `h = t`, ic `y(0) = 1`: `−1/y = t²/2 + C`, `C = −1`, `y = 2/(2 − t²)`), `poly` (`g = 3y^2`, `h = 2t + 1`, ic `y(0) = 1`: `y³ = t² + t + 1`). Pin `spG`, `spC`, `spImplicit`.
   - Misconception: "separating" means moving `y` to the other side with `y′` left alone.
   - Worked: `y·y′ = t`: `∫y dy = ∫t dt` gives `y²/2 = t²/2 + C`; `y(0) = 2` gives `C = 2`; `y² = t² + 4`.

2. **why-separation-works** — Why Separation Works — *Separating variables*
   - Do: justify the method as the chain rule read backwards — `(G(y(t)))′ = g(y)·y′` — and check an explicit solution by differentiating both sides of the implicit one.
   - Lab: `dekit`/`separable`, `view: check`. Presets: `circle` (as above: `d/dt[y²/2] = y·y′ = t`, `spCheck` = `equal`), `recip` (`d/dt[−1/y] = y′/y² = t`), `poly` (`d/dt[y³] = 3y²·y′ = 2t + 1`). Shipped `view = check`. Pin `spCheck`, `spImplicit`.
   - Misconception: `dy` and `dt` are quantities that were cancelled, so the method is a trick.
   - Worked: with `y = √(t² + 4)`, `y·y′ = √(t² + 4)·t/√(t² + 4) = t`; the chain rule is what made `∫y dy` mean `∫y·y′ dt`.

3. **implicit-and-explicit-solutions** — Implicit and Explicit Solutions — *Separating variables*
   - Do: solve an implicit relation for `y` where a quadratic allows it, pick the branch the initial value demands, and state the domain on which the explicit solution exists.
   - Lab: `dekit`/`separable`, `view: solve`. Presets: `lower` (`g = y`, `h = t`, ic `y(0) = −2`: `y = −√(t² + 4)`, all `t`), `hyperbola` (`g = y`, `h = -t`, ic `y(0) = 1`: `y² = 1 − t²`, `y = √(1 − t²)`, domain `−1 < t < 1`), `blow` (`g = 1/y^2`, `h = 1`, ic `y(0) = 1`: `y = 1/(1 − t)`, domain `t < 1`). Pin `spExplicit`, `spDomain`.
   - Misconception: `y² = t² + 4` means `y = √(t² + 4)`.
   - Worked: `y·y′ = t`, `y(0) = −2`: `y² = t² + 4` as before, but `y(0) = −2 < 0` selects `y = −√(t² + 4)`; the other branch never passes through `(0, −2)`.

4. **exponential-growth** — Exponential Growth — *Exponential change*
   - Do: solve `y′ = k·y` by separation to `y = y₀·e^(kt)`, run Euler exactly to get `yₙ = y₀·(1 + kh)ⁿ`, and recognise the geometric sequence from Algebra's Sequences and Series.
   - Lab: `dekit`/`growth`. Presets: `unit` (k = 1, y₀ = 1, A = 0, h = 1/4, n = 4: factor `5/4`, `y₄ = 625/256`, true `≈ 2.71828`), `half` (k = 1/2, y₀ = 2, h = 1/4, n = 8: factor `9/8`), `fine` (k = 1, h = 1/16, n = 16: `(17/16)¹⁶ ≈ 2.63793`, closer to `e`). Pin `grFactor`, `grLast`, `grTrue`.
   - Misconception: exponential growth means "grows quickly"; a geometric sequence and an exponential function are unrelated.
   - Worked: `y′ = y`, `y(0) = 1`, `h = 1/n`: Euler gives `yₙ = (1 + 1/n)ⁿ`, which for `n = 4` is `625/256 ≈ 2.44141` and heads for `e ≈ 2.71828` as `n` grows — the sequence “The Number e” in Algebra's Exponential and Logarithmic Functions built directly.

5. **doubling-time-and-half-life** — Doubling Time and Half-Life — *Exponential change*
   - Do: derive `T = ln 2/k` from `e^(kT) = 2`, state it as rounded, and find exactly the first Euler step at which the exact sequence passes double.
   - Lab: `dekit`/`growth`. Presets: `double` (k = 1/2, y₀ = 1, h = 1/4, n = 8, target 2: `T ≈ 1.38629`; `grHit` = `step 6 (t = 3/2)`), `halve` (k = −1/2, y₀ = 8, target 4: `T ≈ 1.38629`, hit `step 6 (t = 3/2)`), `slow` (k = 1/10, h = 1, n = 16, target 2: `T ≈ 6.93147`, hit `step 8 (t = 8)`). Pin `grT`, `grHit`.
   - Misconception: the doubling time depends on the starting amount.
   - Worked: `k = 1/2`, `h = 1/4`: the factor is `9/8`; `(9/8)⁵ ≈ 1.80203 < 2` and `(9/8)⁶ ≈ 2.02729 ≥ 2`, so the exact sequence first doubles at step 6, `t = 3/2`; the true doubling time is `2 ln 2 ≈ 1.38629`, and Euler, which underestimates growth, is late.

6. **radioactive-decay-and-dating** — Radioactive Decay and Dating — *Exponential change*
   - Do: write decay as `y′ = −k·y` with `k > 0`, convert a half-life to `k` and back (rounded), and compute an age from a remaining fraction.
   - Lab: `dekit`/`growth`. Presets: `carbon` (k = −3/25000 per year, y₀ = 1, h = 100, n = 64, target 1/2: `T ≈ 5776.23`), `quarter` (same `k`, target 1/4: `T ≈ 11552.5`), `fast` (k = −1/4, y₀ = 100, h = 1, target 50: `T ≈ 2.77259`). Pin `grFactor`, `grT`.
   - Misconception: after two half-lives nothing is left.
   - Worked: half-life `T` means `e^(−kT) = 1/2`; a sample at a quarter of its original carbon has been through two half-lives, `2T`; with `k = 3/25000` that is `≈ 11552.5` years, and with the exact factor `1 − 300/25000 = 247/250` per century the Euler sequence reaches a quarter at a step the lab names.

7. **newtons-law-of-cooling** — Newton's Law of Cooling — *Exponential change*
   - Do: write `y′ = −k·(y − A)`, substitute `u = y − A` to recover pure decay, and read the equilibrium and the approach to it.
   - Lab: `dekit`/`growth`. Presets: `coffee` (k = −1/4, y₀ = 100, A = 20, h = 1, n = 8: factor `3/4`, `y₄ = 725/16`, true `≈ 49.4305`, steady `20`), `warming` (k = −1/2, y₀ = 5, A = 20), `fridge` (k = −1/10, y₀ = 25, A = 4). Pin `grSteady`, `grLast`, `grTrue`.
   - Misconception: a hot object cools at a constant rate.
   - Worked: `y′ = −(1/4)(y − 20)`, `y(0) = 100`, `h = 1`: `yₙ = 20 + 80·(3/4)ⁿ`; `y₄ = 20 + 80·81/256 = 725/16 = 45.3125`; the true `y(4) = 20 + 80·e^(−1) ≈ 49.4305`.

8. **mixing-problems** — Mixing Problems — *Shifted and bounded growth*
   - Do: set up `y′ = (rate in) − (rate out)·y/V` for a well-stirred tank, find the equilibrium concentration, and check the Euler sequence against the closed form.
   - Lab: `dekit`/`growth`. Presets: `tank` (`y′ = 10 − y/20`: k = −1/20, A = 200, y₀ = 0, h = 1, n = 10: factor `19/20`, `y₁₀ = 200·(1 − (19/20)¹⁰)`, true `≈ 78.6939`), `flush` (k = −1/10, A = 0, y₀ = 50), `salt` (k = −1/50, A = 300, y₀ = 100). Pin `grSteady`, `grLast`.
   - Misconception: the tank reaches the inflow concentration in a finite time.
   - Worked: inflow `5 L/min` at `2 g/L` into `100 L`, outflow `5 L/min`: `y′ = 10 − 5y/100 = −(1/20)(y − 200)`; the equilibrium is `200 g`; from `y₀ = 0`, `y = 200(1 − e^(−t/20))`.

9. **logistic-growth** — Logistic Growth — *Shifted and bounded growth*
   - Do: write `y′ = r·y·(1 − y/K)`, find the equilibria `0` and `K` and their stability, locate the inflection at `K/2` from `f′(y) = 0`, and read the S-curve against exact Euler steps.
   - Lab: `dekit`/`autonomous`, `view: steps`. Presets: `four` (`y(1 - y/4)`, starts `1`, h = 1/2, n = 12: `11/8, 935/512, …`; equilibria `0, 4`; `auSteps` = `11 exact steps, then digit budget`; inflection `y = 2`), `above` (same, start `6`: decreasing to 4), `small` (`y(1 - y/10)`, start `1/2`). Pin `auEquil`, `auTypes`, `auInflect`.
   - Misconception: the logistic curve is exponential growth that "stops at `K`".
   - Worked: `y′ = y(1 − y/4)`, `y(0) = 1`, `h = 1/2`: `y₁ = 1 + (1/2)(1)(3/4) = 11/8`, `y₂ = 11/8 + (1/2)(11/8)(21/32) = 935/512 ≈ 1.82617`; `f′(y) = 1 − y/2` is zero at `y = 2 = K/2`, where the growth rate `f(y)` is largest.

10. **harvesting-and-the-threshold** — Harvesting and the Threshold — *Shifted and bounded growth*
    - Do: add a constant harvest `H` to the logistic equation, find the equilibria from a quadratic, and compute the threshold `H* = rK/4` above which the population collapses.
    - Lab: `dekit`/`autonomous`, `view: line`. Presets: `light` (`y(1 - y/4) - 3/4`: equilibria `1, 3`; `1 unstable; 3 stable`), `critical` (`y(1 - y/4) - 1`: one equilibrium `2`, semistable), `heavy` (`y(1 - y/4) - 5/4`: none; every start falls). Shipped `view = line`. Pin `auEquil`, `auTypes`.
    - Misconception: harvesting at any rate below the natural growth rate at `K` is sustainable.
    - Worked: `y(1 − y/4) − 3/4 = 0` is `y² − 4y + 3 = 0`, roots `1` and `3`; at `H = 1` the quadratic is `(y − 2)²`, one root, and at `H = 5/4` there is none — `H* = rK/4 = 1`.
### Course 5 — Equilibria, Stability and Phase Lines (`equilibria-stability-and-phase-lines`, 8)

Modules: *Autonomous equations* (1–2), *Classifying equilibria* (3–5),
*Parameters* (6–7), *Sketching* (8).

1. **autonomous-equations** — Autonomous Equations — *Autonomous equations*
   - Do: recognise `y′ = f(y)` (no `t` on the right), find its equilibria as the exact roots of `f`, and explain why the slope field is the same on every vertical line.
   - Lab: `dekit`/`autonomous`, `view: line`. Presets: `quad` (`y^2 - 1`: equilibria `−1, 1`), `cubic` (`y(y - 1)(y - 3)`, typed `y^3 - 4y^2 + 3y`: `0, 1, 3`), `golden` (`y^2 - y - 1`: `(1 ± √5)/2`, printed as surds with the rounded values in the banner). Pin `auEquil`.
   - Misconception: an equilibrium is where the solution "stops changing for a while".
   - Worked: `y′ = y² − 1`: `f(y) = 0` at `y = ±1`; the constant functions `y = 1` and `y = −1` are solutions, and every other solution moves towards or away from them without crossing.

2. **the-phase-line** — The Phase Line — *Autonomous equations*
   - Do: draw the phase line from the sign of `f` between consecutive equilibria, and read the direction of every solution off it.
   - Lab: `dekit`/`autonomous`, `view: line`. Presets: `cubic` (`y^3 - 4y^2 + 3y`: falling below 0, rising on `(0, 1)`, falling on `(1, 3)`, rising above 3), `quad` (`y^2 - 1`), `single` (`2 - y`: one equilibrium, arrows towards it). Pin `auEquil`, `auTypes`.
   - Misconception: the arrows on a phase line show how fast the solution moves, so a long arrow means a steep solution.
   - Worked: `f(y) = y(y − 1)(y − 3)` at test values: `f(−1) = −8`, `f(1/2) = 5/8`, `f(2) = −2`, `f(4) = 12`; signs `−, +, −, +`; the arrows point down, up, down, up.

3. **stable-unstable-and-semistable** — Stable, Unstable and Semistable — *Classifying equilibria*
   - Do: classify each equilibrium from the sign of `f` on either side, and produce an equilibrium that attracts from one side and repels from the other.
   - Lab: `dekit`/`autonomous`, `view: line`. Presets: `cubic` (`y^3 - 4y^2 + 3y`: `0 unstable; 1 stable; 3 unstable`), `semi` (`y^2 - y^3`, i.e. `y²(1 − y)`: `0 semistable; 1 stable`), `quad` (`y^2 - 1`: `−1 stable; 1 unstable`). Pin `auTypes`, `auSlope`.
   - Misconception: an equilibrium is either stable or unstable; "semistable" is a hedge.
   - Worked: `f(y) = y²(1 − y)`: positive for `y < 0` and for `0 < y < 1`, so solutions below `0` rise to it and solutions just above `0` rise away from it; `f′(0) = 0`, and the sign test, not the derivative, decides.

4. **linearisation-and-the-sign-of-f-prime** — Linearisation and the Sign of f′ — *Classifying equilibria*
   - Do: compute `f′(y*)` exactly at each equilibrium, use its sign to classify when it is nonzero, and name the case it cannot decide.
   - Lab: `dekit`/`autonomous`, `view: line`. Presets: `cubic` (`y^3 - 4y^2 + 3y`: `f′(0) = 3; f′(1) = −2; f′(3) = 6`), `flat-unstable` (`y^3`: `f′(0) = 0`, unstable by the sign test), `flat-stable` (`-y^3`: `f′(0) = 0`, stable). Pin `auSlope`, `auTypes`.
   - Misconception: `f′(y*) = 0` means the equilibrium is semistable.
   - Worked: near a stable equilibrium `u = y − y*` obeys `u′ ≈ f′(y*)·u`, so the approach is like `e^(f′(y*)t)`; for `y′ = y² − 1` at `y = −1`, `f′(−1) = −2` and the gap closes like `e^(−2t)`.

5. **long-run-behaviour-without-solving** — Long-Run Behaviour Without Solving — *Classifying equilibria*
   - Do: state the limit of a solution from any starting value using only the phase line, and say when the answer is `±∞`.
   - Lab: `dekit`/`autonomous`, `view: steps`. Presets: `two` (`y^2 - 4y + 3`, i.e. `(y − 1)(y − 3)`, starts `0, 2, 4`, h = 1/4, n = 12: limits `→ 1`, `→ 1`, `→ +∞`), `cubic` (`y^3 - 4y^2 + 3y`, starts `1/2, 2, 7/2`), `quad` (`y^2 - 1`, starts `−2, 0, 2`). Pin `auLimit`, `auSteps`.
   - Misconception: a solution starting between two equilibria may oscillate between them.
   - Worked: `y′ = (y − 1)(y − 3)`: `f′(1) = −2`, `f′(3) = 2`; from `y(0) = 2` the solution falls to `1`; from `y(0) = 4`, `f(4) = 3 > 0` and nothing above `3` stops it, so `y → ∞`; the exact Euler steps from `4` with `h = 1/4` are `19/4, 409/64, …` and climb.

6. **one-parameter-families** — One-Parameter Families — *Parameters*
   - Do: track the equilibria of `y′ = f(y, a)` as `a` changes, and find the value of `a` at which two equilibria meet and vanish.
   - Lab: `dekit`/`bifurcate`. Presets: `saddle-node` (`a + y^2`, a = −4, range `[−4, 1]`: equilibria `−2, 2`; critical `a = 0`), `at-zero` (same, a = 0: one equilibrium, semistable), `gone` (same, a = 1: none). Pin `bfEquil`, `bfCount`, `bfCritical`.
   - Misconception: a small change in a parameter makes a small change in the behaviour.
   - Worked: `y′ = a + y²`: equilibria at `y = ±√(−a)` when `a < 0` — `±2` at `a = −4`, `±1` at `a = −1` — one at `a = 0`, none for `a > 0`; the two meet where `f = 0` and `f′ = 2y = 0` together, which is `a = 0`.

7. **bifurcation-diagrams** — Bifurcation Diagrams — *Parameters*
   - Do: read a bifurcation diagram — equilibrium against parameter, stable solid, unstable dashed — and name the pitchfork and transcritical shapes from the equilibria the lab computes.
   - Lab: `dekit`/`bifurcate`. Presets: `pitchfork` (`a y - y^3`, a = 4, range `[−2, 4]`: `−2, 0, 2`; `−2 stable; 0 unstable; 2 stable`; critical `a = 0`), `pitchfork-before` (same, a = −1: `0 stable`), `transcritical` (`a y - y^2`, a = 2: `0 unstable; 2 stable`; critical `a = 0`). Pin `bfEquil`, `bfTypes`, `bfCritical`.
   - Misconception: the number of equilibria can only go up as a parameter increases.
   - Worked: `y′ = ay − y³ = y(a − y²)`: for `a ≤ 0` only `y = 0`, stable; for `a > 0`, `0` becomes unstable and `±√a` appear, stable — at `a = 4`, `±2`; the diagram is a fork opening at `a = 0`.

8. **sketching-solutions-from-the-phase-line** — Sketching Solutions from the Phase Line — *Sketching*
   - Do: sketch solution curves in the `t`–`y` plane from the phase line alone, placing the inflection where `f′(y) = 0`, and check the sketch against the drawn curves.
   - Lab: `dekit`/`autonomous`, `view: curves`. Presets: `two` (`y^2 - 4y + 3`, starts `0, 3/2, 5/2, 4`: inflection level `y = 2`), `logistic` (`y(1 - y/4)`, starts `1/2, 1, 6`: inflection `y = 2`), `cubic` (`y^3 - 4y^2 + 3y`: inflections at the rational roots of `3y² − 8y + 3`, which are irrational — tile reads `none rational`). Shipped `view = curves`. Pin `auInflect`, `auEquil`.
   - Misconception: a solution curve between two equilibria is a straight line or a parabola.
   - Worked: `y′ = (y − 1)(y − 3)`: `y″ = f′(y)·y′ = (2y − 4)·f(y)`, zero at `y = 2`; a solution from `y(0) = 5/2` falls towards `1`, is concave down while it is above `2` (both factors of `y″` have opposite signs there) and concave up once it has passed `y = 2`.

### Course 6 — First-Order Linear Equations (`first-order-linear-equations`, 8)

Modules: *The linear form* (1–2), *Integrating factors* (3–4), *Forcing*
(5–7), *Stiffness* (8).

1. **the-standard-form** — The Standard Form — *The linear form*
   - Do: rewrite a first-order linear equation as `y′ + p(t)·y = q(t)`, identify `p` and `q`, and say whether it is homogeneous.
   - Lab: `dekit`/`linear1`, `view: solve`. Presets: `scaled` (`2y' + 6y = 4t` → `p = 3`, `q = 2t`), `power` (`t y' - 2y = 0` → `p = −2/t`, `q = 0`, homogeneous), `constant` (`y' = 4 - 2y` → `p = 2`, `q = 4`). Pin `lfMu`, `lfYh`.
   - Misconception: `y′ = 2y + t²·y` is not linear because of the `t²`.
   - Worked: `2y′ + 6y = 4t`: divide by `2`: `y′ + 3y = 2t`, so `p(t) = 3`, `q(t) = 2t`, not homogeneous; `μ = e^(3t)` and `y_h = C·e^(−3t)`.

2. **constant-coefficients-and-the-steady-state** — Constant Coefficients and the Steady State — *The linear form*
   - Do: solve `y′ + a·y = b` as a shifted exponential, name the steady state `b/a`, and compare exact Euler steps with the closed form.
   - Lab: `dekit`/`linear1`, `view: steps`. Presets: `three` (`y' + 2y = 6`, ic `y(0) = 0`, h = 1/4, n = 4: steady `3`; Euler factor `1/2`; `y₄ = 45/16`; true `3 − 3e^(−2) ≈ 2.59399`), `from-above` (same, `y(0) = 5`), `negative` (`y' - y = 2`, `y(0) = 0`: steady `−2`, repelling). Shipped `view = steps`. Pin `lfSteady`, `lfSolution`.
   - Misconception: the steady state is the initial value, or is reached in finite time.
   - Worked: `y′ + 2y = 6`, `y(0) = 0`: `y = 3 − 3e^(−2t)`; Euler with `h = 1/4` gives `yₙ = 3 − 3·(1/2)ⁿ`, `y₄ = 45/16 = 2.8125`, against `y(1) ≈ 2.59399`.

3. **the-integrating-factor** — The Integrating Factor — *Integrating factors*
   - Do: construct `μ = e^(∫p dt)`, show `(μ·y)′ = μ·q` is the product rule read backwards, and solve a case with `μ = tᵃ` entirely in fractions.
   - Lab: `dekit`/`linear1`, `view: solve`. Presets: `t-squared` (`y' + (2/t) y = t^2`, ic `y(1) = 1`: `μ = t²`, `y = t³/5 + (4/5)/t²`), `exp` (`y' + 2y = e^t`: `μ = e^(2t)`, `y = e^t/3 + C·e^(−2t)`), `t-one` (`y' + y/t = 1`, ic `y(1) = 2`: `μ = t`, `y = t/2 + (3/2)/t`). Pin `lfMu`, `lfSolution`, `lfC`.
   - Misconception: the integrating factor is `e^(p(t))` rather than `e^(∫p dt)`.
   - Worked: `y′ + (2/t)y = t²`: `μ = e^(∫2/t dt) = t²`; `(t²y)′ = t⁴`; `t²y = t⁵/5 + C`; `y = t³/5 + C/t²`; `y(1) = 1` gives `C = 4/5` — every step a fraction.

4. **homogeneous-plus-particular** — Homogeneous Plus Particular — *Integrating factors*
   - Do: split the general solution into `y_h` (all solutions of the homogeneous equation) and one `y_p`, explain why adding them is allowed, and fit the constant last.
   - Lab: `dekit`/`linear1`, `view: parts`. Presets: `ramp` (`y' + 3y = 2t`, ic `y(0) = 1`: `y_h = C·e^(−3t)`, `y_p = (2/3)t − 2/9`, `C = 11/9`), `constant` (`y' + 2y = 6`: `y_p = 3`), `exp` (`y' + 2y = e^t`, ic `y(0) = 0`: `y_p = e^t/3`, `C = −1/3`). Shipped `view = parts`. Pin `lfYh`, `lfYp`, `lfC`.
   - Misconception: the constant is fitted to `y_h` before `y_p` is added.
   - Worked: `y′ + 3y = 2t`, `y(0) = 1`: `y_h = C·e^(−3t)`; try `y_p = At + B`: `A + 3At + 3B = 2t` gives `A = 2/3`, `B = −2/9`; `y(0) = C − 2/9 = 1`, `C = 11/9`.

5. **polynomial-forcing** — Polynomial Forcing and Undetermined Coefficients — *Forcing*
   - Do: guess a particular solution of the same degree as the forcing, match coefficients to get an exact linear system, and solve it.
   - Lab: `dekit`/`linear1`, `view: parts`. Presets: `square` (`y' + y = t^2`: `y_p = t² − 2t + 2`), `line` (`y' - 2y = 4t`: `y_p = −2t − 1`), `cubic` (`y' + y = t^3`: `y_p = t³ − 3t² + 6t − 6`). Shipped `view = parts`. Pin `lfYp`.
   - Misconception: the particular solution for forcing `t²` is `A·t²` alone.
   - Worked: `y′ + y = t²`, try `At² + Bt + C`: `2At + B + At² + Bt + C = t²`; `A = 1`, `2A + B = 0`, `B + C = 0`; `y_p = t² − 2t + 2`.

6. **exponential-and-sinusoidal-forcing** — Exponential and Sinusoidal Forcing — *Forcing*
   - Do: fit `A·e^(bt)` and `A·cos(ωt) + B·sin(ωt)` particular solutions with exact coefficients, and handle the resonant case where the forcing matches the homogeneous solution.
   - Lab: `dekit`/`linear1`, `view: parts`. Presets: `cosine` (`y' + 2y = cos(t)`: `y_p = (2/5)·cos(t) + (1/5)·sin(t)`), `exp` (`y' + 2y = e^t`: `e^t/3`), `resonant` (`y' + 2y = e^(-2t)`: `y_p = t·e^(−2t)`). Shipped `view = parts`. Pin `lfYp`, `lfSolution`.
   - Misconception: the particular solution for `cos(t)` forcing is `A·cos(t)` alone.
   - Worked: `y′ + 2y = cos t` with `y_p = A·cos t + B·sin t`: `−A sin t + B cos t + 2A cos t + 2B sin t = cos t`; `2A + B = 1`, `2B − A = 0`; `A = 2/5`, `B = 1/5`.

7. **circuits-tanks-and-loans** — Circuits, Tanks and Loans — *Forcing*
   - Do: write three situations as one equation `y′ + a·y = b`, read the steady state in each, and compute when a loan balance reaches zero (rounded).
   - Lab: `dekit`/`linear1`, `view: solve`. Presets: `rc` (`q' + 2q = 5`, ic `q(0) = 0`: steady `5/2`), `loan` (`B' - B/20 = -6`, ic `B(0) = 100`: steady `120`, `B = 120 − 20·e^(t/20)`, zero at `t = 20·ln 6 ≈ 35.8352`), `tank` (`y' + y/20 = 10`, `y(0) = 0`: steady `200`). Pin `lfSteady`, `lfSolution`.
   - Misconception: a loan at 5% repaid at 6 a year on a balance of 100 is paid off in about 17 years (100/6).
   - Worked: `B′ = B/20 − 6`, `B(0) = 100`: steady `B* = 120`; `B = 120 − 20·e^(t/20)`; `B = 0` when `e^(t/20) = 6`, `t = 20·ln 6 ≈ 35.8352` years — twice the naive estimate, because interest is charged on the way down.

8. **stiffness-when-the-step-is-too-big** — Stiffness: When the Step Is Too Big — *Stiffness*
   - Do: show Euler's factor `1 − a·h` on `y′ = −a·y`, derive the bound `h < 2/a` for decay, and show the backward factor `1/(1 + a·h)` decays for every `h`.
   - Lab: `dekit`/`stiff`, `scheme: forward`. Presets: `grows` (a = 5, y₀ = 1, h = 1/2, n = 8: factor `−3/2`, `oscillates and grows`, bound `h < 2/5`), `wobbles` (a = 5, h = 1/4: factor `−1/4`, `oscillates and decays`), `fine` (a = 5, h = 1/10: `1/2`, `decays`). Shipped `scheme = forward`. Pin `skFactor`, `skVerdict`, `skLimit`.
   - Misconception: a smaller error per step always means a better answer, so any `h` that is "small" will do.
   - Worked: `y′ = −5y`, `h = 1/2`: `yₙ₊₁ = (1 − 5/2)·yₙ = −(3/2)·yₙ`, so `y₈ = (3/2)⁸ = 6561/256 ≈ 25.6` while the true `y(4) = e^(−20) ≈ 2.06115·10⁻⁹`; the backward step `yₙ₊₁ = yₙ/(1 + 5/2) = (2/7)·yₙ` decays.

### Course 7 — Second-Order Linear Equations (`second-order-linear-equations`, 10)

Modules: *Sines, cosines and two constants* (1–2), *The characteristic
equation* (3–6), *Fitting the constants* (7–8), *The systems view* (9–10).

1. **sine-cosine-and-their-rates** — Sine, Cosine and Their Rates — *Sines, cosines and two constants*
   - Do: read the quotients of `sin` and `cos` off a rounded, labelled table, state `sin′ = cos` and `cos′ = −sin` as the demonstrated claims, and conclude `cos″ = −cos`.
   - Lab: `calckit`/`transcendental`, `kind: sin`. Presets: `sin-at-zero` (kind `sin`, a = 0, h = 1, 6 halvings: `≈ 0.841471, ≈ 0.958851, … → 1`), `cos-at-zero` (kind `cos`, a = 0: `≈ −0.459698, … → 0`), `sin-at-one` (kind `sin`, a = 1: `→ cos(1) ≈ 0.540302`). Pin `tqLast`, `tqLimit`.
   - Misconception: the derivative of `sin t` is `cos t` because "that is the other one"; the sign of `cos′` is forgotten.
   - Worked: `(sin h)/h` at `h = 1, 1/2, 1/4, 1/8` is `≈ 0.841471, 0.958851, 0.989616, 0.997398`, heading for `1 = cos 0`; every entry is rounded and the tile says so; the lesson states the limit as a claim and uses it for the rest of the course.

2. **the-second-order-equation** — The Second-Order Equation — *Sines, cosines and two constants*
   - Do: verify `cos t`, `sin t` and any `C·cos t + D·sin t` solve `x″ + x = 0` by exact substitution, and explain why two initial values are needed.
   - Lab: `dekit`/`verify`. Presets: `cos` (`y'' + y = 0`, candidate `cos(t)`: residual `0`), `combo` (candidate `3cos(t) - 2sin(t)`: `0`), `not` (candidate `t cos(t)`: residual `−2·sin(t)`), `fit` (candidate `C cos(t) + D sin(t)`, ic `y(0) = 1, y'(0) = −2`: `C = 1, D = −2`). Pin `vfResidual`, `vfVerdict`, `vfFamily`.
   - Misconception: a second-order equation has one arbitrary constant, like a first-order one.
   - Worked: `x = t·cos t`: `x′ = cos t − t·sin t`, `x″ = −2·sin t − t·cos t`; `x″ + x = −2·sin t ≠ 0`; while `x = 3cos t − 2sin t` gives `x″ = −3cos t + 2sin t = −x`.

3. **the-characteristic-equation** — The Characteristic Equation — *The characteristic equation*
   - Do: substitute `y = e^(rt)` into `a·y″ + b·y′ + c·y = 0`, obtain `a·r² + b·r + c = 0`, and solve it exactly with the quadratic formula from Algebra's Quadratics and Complex Numbers.
   - Lab: `dekit`/`char`, `view: roots`. Presets: `distinct` (`1, 3, 2`: disc `1`, roots `−2, −1`), `repeated` (`1, 4, 4`: disc `0`, `−2 (repeated)`), `complex` (`1, 2, 5`: disc `−16`, `−1 ± 2i`), `surd` (`1, −1, −1`: disc `5`, `(1 ± √5)/2`). Pin `ceDisc`, `ceKind`, `ceRoots`.
   - Misconception: the characteristic equation is `a·r² + b·r + c = y`.
   - Worked: `y″ + 3y′ + 2y = 0` with `y = e^(rt)`: `(r² + 3r + 2)·e^(rt) = 0`; `e^(rt)` is never zero, so `r² + 3r + 2 = 0`, `r = −1` or `r = −2`.

4. **real-distinct-roots** — Real Distinct Roots — *The characteristic equation*
   - Do: write `y = C₁·e^(r₁t) + C₂·e^(r₂t)`, verify it exactly, and read growth or decay off the signs of the roots.
   - Lab: `dekit`/`char`, `view: solution`. Presets: `decay` (`1, 3, 2`, ic `y(0) = 1, y′(0) = 0`: `y = 2·e^(−t) − e^(−2t)`), `mixed` (`1, 0, −1`: roots `±1`; ic `y(0) = 1, y′(0) = −1`: `y = e^(−t)`), `grow` (`1, −5, 6`: roots `2, 3`). Shipped `view = solution`. Pin `ceRoots`, `ceGeneral`, `ceSolution`.
   - Misconception: the general solution is `e^(r₁t) + e^(r₂t)` with no constants.
   - Worked: `y″ + 3y′ + 2y = 0`, `y(0) = 1`, `y′(0) = 0`: `C₁ + C₂ = 1`, `−C₁ − 2C₂ = 0`; `C₂ = −1`, `C₁ = 2`; `y = 2e^(−t) − e^(−2t)`; the residual of this `y` is `0` exactly.

5. **repeated-roots** — Repeated Roots — *The characteristic equation*
   - Do: show that one root gives one solution, verify `t·e^(rt)` as the second by exact substitution, and fit both constants.
   - Lab: `dekit`/`char`, `view: solution`. Presets: `critical` (`1, 4, 4`, ic `y(0) = 1, y′(0) = 1`: `y = (1 + 3t)·e^(−2t)`), `zero-root` (`1, 0, 0`: `r = 0` repeated, `y = C₁ + C₂t`), `third` (`9, 6, 1`: `r = −1/3` repeated). Shipped `view = solution`. Pin `ceKind`, `ceGeneral`, `ceC`.
   - Misconception: with one root the general solution is `C·e^(rt)` and one initial value is enough.
   - Worked: `y″ + 4y′ + 4y = 0`, `y = t·e^(−2t)`: `y′ = (1 − 2t)e^(−2t)`, `y″ = (4t − 4)e^(−2t)`; `(4t − 4) + 4(1 − 2t) + 4t = 0`; with `y(0) = 1`, `y′(0) = 1`: `C₁ = 1`, `C₂ − 2 = 1`, `y = (1 + 3t)e^(−2t)`.

6. **complex-roots-and-oscillation** — Complex Roots and Oscillation — *The characteristic equation*
   - Do: turn `α ± βi` into `e^(αt)·(C₁·cos(βt) + C₂·sin(βt))`, verify it exactly, and read the oscillation frequency and the decay rate off the root.
   - Lab: `dekit`/`char`, `view: solution`. Presets: `damped` (`1, 2, 5`, ic `y(0) = 0, y′(0) = 2`: `y = e^(−t)·sin(2t)`), `pure` (`1, 0, 4`: `±2i`, `y = C₁·cos(2t) + C₂·sin(2t)`), `growing` (`1, −2, 2`: `1 ± i`). Shipped `view = solution`. Pin `ceRoots`, `ceGeneral`, `ceSolution`.
   - Misconception: a complex root means the equation has no real solution.
   - Worked: `y″ + 2y′ + 5y = 0`: `r = −1 ± 2i`; `y = e^(−t)(C₁cos 2t + C₂sin 2t)`; `y(0) = 0` gives `C₁ = 0`; `y′(0) = −C₁ + 2C₂ = 2` gives `C₂ = 1`; `y = e^(−t)·sin 2t`, and the residual is `0`.

7. **fitting-the-initial-conditions** — Fitting the Initial Conditions — *Fitting the constants*
   - Do: set up the 2×2 linear system for `C₁, C₂` from `y(0)` and `y′(0)`, solve it exactly, and say when the lab refuses (irrational roots) and why that is a limit of the arithmetic, not of the method.
   - Lab: `dekit`/`char`, `view: solution`. Presets: `decay` (`1, 3, 2`, `y(0) = 0, y′(0) = 1`: `C₁ = 1, C₂ = −1`), `damped` (`1, 2, 5`, `y(0) = 2, y′(0) = 0`: `C₁ = 2, C₂ = 1`), `surd` (`1, −1, −1`, `y(0) = 1, y′(0) = 0`: `ceC` = `—`, the banner names the irrational roots). Shipped `view = solution`. Pin `ceC`, `ceSolution`.
   - Misconception: `y′(0)` is found by differentiating the number `y(0)`.
   - Worked: `y″ + 2y′ + 5y = 0`, `y(0) = 2`, `y′(0) = 0`: `C₁ = 2`; `y′(0) = −C₁ + 2C₂ = 0`, `C₂ = 1`; `y = e^(−t)(2cos 2t + sin 2t)`.

8. **superposition-and-the-wronskian** — Superposition and the Wronskian — *Fitting the constants*
   - Do: show that a combination of two solutions is a solution (linearity), compute the Wronskian at `0` exactly, and say what a nonzero Wronskian guarantees about fitting any initial values.
   - Lab: `dekit`/`char`, `view: wronskian`. Presets: `decay` (`1, 3, 2`: `W(0) = −1`), `pure` (`1, 0, 4`: `W(0) = 2`), `repeated` (`1, 4, 4`: `W(0) = 1`), `surd` (`1, −1, −1`: `W(0) = √5`). Shipped `view = wronskian`. Pin `ceW`.
   - Misconception: any two solutions can be used to fit any initial values.
   - Worked: `y₁ = e^(−t)`, `y₂ = e^(−2t)`: `W = y₁y₂′ − y₁′y₂ = −2e^(−3t) + e^(−3t) = −e^(−3t)`, `W(0) = −1 ≠ 0`; the system for `C₁, C₂` has determinant `W(0)` and so always has one solution.

9. **from-second-order-to-a-system** — From Second Order to a System — *The systems view*
   - Do: rewrite `a·x″ + b·x′ + c·x = 0` as `x′ = v`, `v′ = −(c/a)x − (b/a)v`, and show the matrix's trace and determinant reproduce the characteristic equation.
   - Lab: `dekit`/`phase`, `view: field`. Presets: `decay` (`A = [[0, 1], [−2, −3]]`: `τ = −3`, `Δ = 2`, eigenvalues `−2, −1`, stable node), `pure` (`[[0, 1], [−4, 0]]`: `τ = 0`, `Δ = 4`, `±2i`, centre), `damped` (`[[0, 1], [−5, −2]]`: `−1 ± 2i`, stable spiral). Pin `ppTrace`, `ppDet`, `ppEig`, `ppType`.
   - Misconception: the system has different solutions from the equation.
   - Worked: `x″ + 3x′ + 2x = 0`: `x′ = v`, `v′ = −2x − 3v`; `A = [[0, 1], [−2, −3]]`, `τ = −3`, `Δ = 2`, `λ² + 3λ + 2 = 0` — the characteristic equation, roots `−1, −2`.

10. **euler-on-an-oscillator** — Euler on an Oscillator — *The systems view*
    - Do: step `x′ = v, v′ = −x` exactly with Euler, show `xₙ₊₁² + vₙ₊₁² = (1 + h²)(xₙ² + vₙ²)` so the method spirals outward from a circle, and compute the exact growth factor.
    - Lab: `dekit`/`phase`, `view: exact`. Presets: `quarter` (`[[0, 1], [−1, 0]]`, start `(1, 0)`, h = 1/4, n = 24: `ppRatio` = `17/16`), `eighth` (h = 1/8, n = 48: `65/64`), `coarse` (h = 1/2, n = 12: `5/4`). Shipped `view = exact`. Pin `ppRatio`, `ppLast`, `ppType`.
    - Misconception: Euler's method conserves what the equation conserves.
    - Worked: from `(1, 0)` with `h = 1/4`: `(1, −1/4)`, radius² `17/16`; then `(15/16, −1/2)`, radius² `289/256 = (17/16)²`; each step multiplies `x² + v²` by exactly `1 + h²`, so the drawn polygon spirals out of the circle the true solution stays on.
### Course 8 — Oscillators, Damping and Resonance (`oscillators-damping-and-resonance`, 9)

Modules: *Free oscillation* (1–3), *Damping* (4–6), *Forcing* (7–9).

1. **the-mass-spring-model** — The Mass–Spring Model — *Free oscillation*
   - Do: derive `m·x″ + c·x′ + k·x = 0` from Newton's law and Hooke's law, compute `ω₀² = k/m` exactly, and give the period as a symbol and as a rounded number.
   - Lab: `dekit`/`oscillator`, `view: motion`. Presets: `unit` (m = 1, c = 0, k = 4, ic `(1, 0)`: `ω₀² = 4`, `ω₀ = 2`, period `π ≈ 3.14159`), `heavy` (m = 2, c = 0, k = 5: `ω₀² = 5/2`, `ω₀ = √10/2 ≈ 1.58114`, period `≈ 3.97384`), `stiff` (m = 1, c = 0, k = 9: period `2π/3 ≈ 2.0944`). Pin `osType`, `osOmega0Sq`, `osPeriod`.
   - Misconception: a heavier mass oscillates faster because it "has more energy".
   - Worked: `m = 1`, `k = 4`: `x″ = −4x`, `ω₀ = 2`, `x = C₁cos 2t + C₂sin 2t`, period `2π/2 = π`; doubling `m` divides `ω₀²` by 2 and multiplies the period by `√2`.

2. **amplitude-phase-and-period** — Amplitude, Phase and Period — *Free oscillation*
   - Do: convert `C₁cos(ω₀t) + C₂sin(ω₀t)` to `A·cos(ω₀t − φ)`, compute `A² = x₀² + v₀²/ω₀²` exactly, and read `φ` as rounded.
   - Lab: `dekit`/`oscillator`, `view: motion`. Presets: `five` (m = 1, c = 0, k = 4, ic `(3, 8)`: `A² = 25`, `A = 5`, `φ ≈ 0.927295`), `pure-cos` (ic `(2, 0)`: `A = 2`, `φ = 0`), `surd` (ic `(1, 1)`: `A² = 5/4`, `A = √5/2 ≈ 1.11803`). Pin `osAmpSq`, `osAmp`.
   - Misconception: the amplitude is the initial displacement.
   - Worked: `x″ + 4x = 0`, `x(0) = 3`, `x′(0) = 8`: `C₁ = 3`, `C₂ = 8/2 = 4`; `A² = 9 + 16 = 25`, `A = 5`; `tan φ = C₂/C₁ = 4/3`, `φ ≈ 0.927295`.

3. **energy-and-the-phase-ellipse** — Energy and the Phase Ellipse — *Free oscillation*
   - Do: compute `E₀ = ½m·v₀² + ½k·x₀²` exactly, state that it is conserved along the motion, and read the phase-plane ellipse `x²/A² + v²/(A·ω₀)² = 1`.
   - Lab: `dekit`/`oscillator`, `view: phase`. Presets: `five` (m = 1, c = 0, k = 4, ic `(3, 8)`: `E₀ = 50`, ellipse semi-axes `5` and `10`), `pure-cos` (ic `(2, 0)`: `E₀ = 8`), `heavy` (m = 2, k = 5, ic `(1, 0)`: `E₀ = 5/2`). Shipped `view = phase`. Pin `osEnergy`, `osAmpSq`.
   - Misconception: energy is lost at the turning points because the mass stops.
   - Worked: `E₀ = ½·1·64 + ½·4·9 = 32 + 18 = 50`; on the ellipse `x = 5` when `v = 0` (`½·4·25 = 50`) and `v = 10` when `x = 0` (`½·100 = 50`).

4. **overdamped-critical-and-underdamped** — Overdamped, Critical and Underdamped — *Damping*
   - Do: classify the motion from the sign of `c² − 4mk`, write the solution form for each case, and compute `c_crit = 2√(mk)` exactly.
   - Lab: `dekit`/`oscillator`, `view: motion`. Presets: `over` (m = 1, c = 5, k = 4, ic `(1, 0)`: disc `9`, roots `−1, −4`, `overdamped`), `critical` (c = 4: disc `0`, `critically damped`, `c_crit = 4`), `under` (m = 1, c = 2, k = 5: disc `−16`, `−1 ± 2i`, `underdamped`). Pin `osType`, `osDisc`, `osCcrit`.
   - Misconception: more damping always means the mass returns to rest faster.
   - Worked: `m = 1`, `k = 4`: `c_crit = 2√4 = 4`; `c = 5` gives `r² + 5r + 4 = (r + 1)(r + 4)`, two decays and no oscillation; `c = 2` with `k = 5` gives `r = −1 ± 2i`, a decaying oscillation.

5. **underdamped-motion-and-the-envelope** — Underdamped Motion and the Envelope — *Damping*
   - Do: compute the pseudo-frequency `ω_d² = k/m − c²/(4m²)` exactly, the envelope rate `c/(2m)`, and the ratio of successive peaks (rounded).
   - Lab: `dekit`/`oscillator`, `view: motion`. Presets: `two-five` (m = 1, c = 2, k = 5, ic `(2, 0)`: `ω_d² = 4`, envelope `e^(−t)`, pseudo-period `π`, peak ratio `e^(−π) ≈ 0.0432139`), `light` (m = 1, c = 1/2, k = 4, ic `(1, 0)`: `ω_d² = 4 − 1/16 = 63/16`), `heavy` (m = 2, c = 2, k = 5: `ω_d² = 5/2 − 1/4 = 9/4`, `ω_d = 3/2`). Pin `osOmegaD`, `osEnvelope`.
   - Misconception: damping changes the amplitude but not the frequency.
   - Worked: `x″ + 2x′ + 5x = 0`: `r = −1 ± 2i`, so `x = e^(−t)(C₁cos 2t + C₂sin 2t)`; `ω_d = 2 < ω₀ = √5`; the envelope `e^(−t)` shrinks each pseudo-period `π` by `e^(−π) ≈ 0.0432139`.

6. **critical-damping-and-design** — Critical Damping and Design — *Damping*
   - Do: write the critically damped solution `(C₁ + C₂t)e^(rt)`, decide exactly whether it crosses zero (at `t = −C₁/C₂` if positive), and explain why critical damping is the design choice for a door closer.
   - Lab: `dekit`/`oscillator`, `view: motion`. Presets: `no-cross` (m = 1, c = 4, k = 4, ic `(1, 1)`: `C₁ = 1, C₂ = 3`, no zero for `t > 0`), `one-cross` (ic `(1, −5)`: `C₂ = −3`, zero at `t = 1/3`), `compare-over` (m = 1, c = 5, k = 4, ic `(1, 0)`: slower return, `e^(−t)` term). Pin `osType`, `osCcrit`, `osDisc`.
   - Misconception: critical damping is the damping that stops the motion fastest in every sense.
   - Worked: `m = 1`, `c = 4`, `k = 4`, `x(0) = 1`, `x′(0) = −5`: `x = (1 + C₂t)e^(−2t)`, `x′(0) = C₂ − 2 = −5`, `C₂ = −3`; `x = 0` at `t = 1/3`, one crossing, then a return from below.

7. **forced-oscillation** — Forced Oscillation — *Forcing*
   - Do: fit `x_p = A·cos(ωt)` to `m·x″ + k·x = F₀·cos(ωt)` and compute `A = F₀/(m(ω₀² − ω²))` exactly; read its sign.
   - Lab: `dekit`/`oscillator`, `view: motion`. Presets: `below` (m = 1, c = 0, k = 4, F₀ = 3, ω = 1: `A = 1`), `above` (ω = 3: `A = −3/5`), `near` (ω = 3/2: `A = 12/7`). Pin `osForced`.
   - Misconception: the response is always in phase with the push.
   - Worked: `x″ + 4x = 3cos t`, try `A·cos t`: `−A + 4A = 3`, `A = 1`; for `ω = 3`: `−9A + 4A = 3`, `A = −3/5`, the mass moves against the force.

8. **resonance-and-beats** — Resonance and Beats — *Forcing*
   - Do: show the fitted amplitude fails when `ω = ω₀`, write the resonant solution `(F₀/(2mω₀))·t·sin(ω₀t)`, and compute the beat period `2π/|ω₀ − ω|` near resonance.
   - Lab: `dekit`/`oscillator`, `view: motion`. Presets: `resonant` (m = 1, c = 0, k = 4, F₀ = 3, ω = 2, ic `(0, 0)`: `osForced` = `resonance: (3/4)·t·sin(2t)`), `beats` (ω = 3/2: `A = 12/7`, beat period `4π ≈ 12.5664`), `far` (ω = 1/2). Pin `osForced`, `osPeriod`.
   - Misconception: resonance means the amplitude becomes infinite at once.
   - Worked: `x″ + 4x = 3cos 2t`: `x_p = (3/4)·t·sin 2t`; check: `x_p″ = 3cos 2t − 3t·sin 2t`, and `x_p″ + 4x_p = 3cos 2t`; the amplitude `3t/4` grows without bound, linearly.

9. **damped-forcing-and-the-amplitude-curve** — Damped Forcing and the Amplitude Curve — *Forcing*
   - Do: compute the steady-state amplitude squared `A² = F₀²/((k − mω²)² + (cω)²)` exactly, the resonant frequency `ω_r² = k/m − c²/(2m²)`, and the peak amplitude.
   - Lab: `dekit`/`oscillator`, `view: amplitude`. Presets: `curve` (m = 1, c = 2, k = 5, F₀ = 3, ω = 1: `A² = 9/20`; `ω_r² = 3`; `A_max² = 9/16`, `A_max = 3/4`), `at-peak` (ω typed as `√3` is not rational — ship ω = 7/4: `A² = 9/((5 − 49/16)² + 49/4)`), `overdamped-no-peak` (m = 1, c = 4, k = 4: `ω_r² = 4 − 8 < 0`, `none`). Shipped `view = amplitude`. Pin `osForced`, `osResonant`.
   - Misconception: the resonant frequency of a damped oscillator is `ω₀`.
   - Worked: `m = 1`, `c = 2`, `k = 5`, `F₀ = 3`: `A²(ω) = 9/((5 − ω²)² + 4ω²)`; the denominator is least at `ω² = 5 − 2 = 3`, where it is `4 + 12 = 16`; `A_max = 3/4`, below `ω₀ = √5`.

### Course 9 — Systems and the Phase Plane (`systems-and-the-phase-plane`, 10)

Modules: *Linear systems* (1–5), *Nonlinear systems* (6–10).

1. **systems-of-two-equations** — Systems of Two Equations — *Linear systems*
   - Do: read `x′ = ax + by, y′ = cx + dy` as a vector field, step it exactly with Euler, and describe a solution as a curve `(x(t), y(t))` in the phase plane.
   - Lab: `dekit`/`phase`, `view: field`. Presets: `saddle` (`[[1, 0], [0, −1]]`, start `(1, 1)`, h = 1/4, n = 8), `rotate` (`[[0, 1], [−1, 0]]`, start `(1, 0)`), `decay` (`[[−1, 0], [0, −2]]`, start `(2, 2)`). Pin `ppTrace`, `ppDet`, `ppLast`.
   - Misconception: the phase plane plots `x` against `t`.
   - Worked: `x′ = x`, `y′ = −y` from `(1, 1)` with `h = 1/4`: `(5/4, 3/4)`, `(25/16, 9/16)`, `(125/64, 27/64)`; the curve heads along the `x`-axis away from the origin — a saddle.

2. **straight-line-solutions-and-eigenvectors** — Straight-Line Solutions and Eigenvectors — *Linear systems*
   - Do: find the directions along which `A·v` is a multiple of `v`, solve `λ² − τλ + Δ = 0` exactly, and write the straight-line solutions `e^(λt)·v`.
   - Lab: `dekit`/`phase`, `view: field`. Presets: `symmetric` (`[[2, 1], [1, 2]]`: `τ = 4`, `Δ = 3`, `λ = 1, 3`, vectors `(1, −1), (1, 1)`), `saddle` (`[[1, 2], [3, 0]]`: `λ = −2, 3`, vectors `(2, −3), (1, 1)`), `surd` (`[[1, 1], [1, 0]]`: `λ = (1 ± √5)/2`, vectors `—`). Pin `ppEig`, `ppVectors`.
   - Misconception: an eigenvector is a point rather than a direction, so `(2, 2)` and `(1, 1)` are different answers.
   - Worked: `A = [[2, 1], [1, 2]]`: `λ² − 4λ + 3 = 0`, `λ = 1, 3`; for `λ = 1`, `(A − I)v = 0` gives `v₁ + v₂ = 0`, `v = (1, −1)`; for `λ = 3`, `v = (1, 1)`; along `(1, 1)` the solution is `e^(3t)·(1, 1)`.

3. **the-general-solution-of-a-linear-system** — The General Solution of a Linear System — *Linear systems*
   - Do: write `C₁e^(λ₁t)v₁ + C₂e^(λ₂t)v₂`, fit `C₁, C₂` from a start exactly, and read which term dominates as `t → ∞`.
   - Lab: `dekit`/`phase`, `view: solution`. Presets: `symmetric` (`[[2, 1], [1, 2]]`, start `(1, 0)`: `C₁ = 1/2, C₂ = 1/2`), `saddle` (`[[1, 2], [3, 0]]`, start `(3, 0)`: on no eigenline; `C₁, C₂` exact), `node` (`[[−1, 0], [0, −2]]`, start `(2, 2)`: `C₁ = 2, C₂ = 2`). Shipped `view = solution`. Pin `ppGeneral`, `ppC`.
   - Misconception: the solution through a point is the eigenvector solution nearest to it.
   - Worked: `A = [[2, 1], [1, 2]]`, start `(1, 0)`: `C₁(1, −1) + C₂(1, 1) = (1, 0)`; `C₁ + C₂ = 1`, `−C₁ + C₂ = 0`; `C₁ = C₂ = 1/2`; for large `t` the `e^(3t)(1, 1)` term wins and the curve bends towards the diagonal.

4. **saddles-nodes-spirals-and-centres** — Saddles, Nodes, Spirals and Centres — *Linear systems*
   - Do: classify the origin from `τ`, `Δ` and `τ² − 4Δ`, locate the system on the trace–determinant plane, and match each region to a picture.
   - Lab: `dekit`/`phase`, `view: field`. Presets: `saddle` (`[[1, 2], [3, 0]]`: `Δ = −6`), `node` (`[[−1, 0], [0, −2]]`: stable node), `spiral` (`[[1, 2], [−2, 1]]`: `τ = 2`, `Δ = 5`, disc `−16`, `1 ± 2i`, unstable spiral), `centre` (`[[0, 2], [−2, 0]]`: `±2i`), `degenerate` (`[[−1, 1], [0, −1]]`: disc `0`, degenerate node). Pin `ppType`, `ppDisc`.
   - Misconception: a negative determinant means the origin is stable.
   - Worked: `A = [[1, 2], [−2, 1]]`: `τ = 2`, `Δ = 5`, `τ² − 4Δ = −16 < 0`, so `λ = 1 ± 2i`: an unstable spiral, since the real part `1` is positive.

5. **stability-of-the-origin** — Stability of the Origin — *Linear systems*
   - Do: state the criterion (asymptotically stable iff `τ < 0` and `Δ > 0`), locate the borderline cases, and connect it to the sign of the real parts of the eigenvalues.
   - Lab: `dekit`/`phase`, `view: field`. Presets: `stable-spiral` (`[[−1, 2], [−2, −1]]`: `τ = −2`, `Δ = 5`), `centre` (`[[0, 2], [−2, 0]]`: `τ = 0`, neutrally stable), `unstable-node` (`[[2, 1], [1, 2]]`), `saddle` (`[[1, 2], [3, 0]]`). Pin `ppType`, `ppTrace`, `ppDet`.
   - Misconception: if one eigenvalue is negative the origin is stable.
   - Worked: `[[−1, 2], [−2, −1]]`: `τ = −2 < 0`, `Δ = 5 > 0`, disc `−16`: `λ = −1 ± 2i`, both real parts `−1`, a stable spiral; change the sign of `τ` and the same picture unwinds.

6. **nonlinear-systems-and-equilibria** — Nonlinear Systems and Their Equilibria — *Nonlinear systems*
   - Do: find the equilibria of a polynomial system by solving `f = g = 0` by hand, check each candidate exactly in the lab, and say what the bounded search did and did not search.
   - Lab: `dekit`/`jacobian`, `view: field`, `search: off`. Presets: `parabola` (`f = y - x^2`, `g = x - y`, points `(0, 0), (1, 1)`: both equilibria), `wrong` (same, points `(2, 4)`: `f = 0, g = −2: not an equilibrium`), `search` (same, `search: grid` shipped off; the lesson instructs switching it on and reads `jbFound` in the banner — rule 6; pin `jbCheck`). Pin `jbCheck`.
   - Misconception: a nonlinear system has one equilibrium, at the origin.
   - Worked: `x′ = y − x²`, `y′ = x − y`: `y = x` and `x = x²`, so `x = 0` or `x = 1`: equilibria `(0, 0)` and `(1, 1)`; at `(2, 4)`, `f = 0` but `g = −2`, so it is not one.

7. **linearisation-and-the-jacobian** — Linearisation and the Jacobian — *Nonlinear systems*
   - Do: compute the Jacobian matrix of partial derivatives exactly at an equilibrium, classify it as a linear system, and name the case (centre, `Δ = 0`) where the classification does not transfer.
   - Lab: `dekit`/`jacobian`, `view: linearised`. Presets: `parabola-origin` (`f = y - x^2`, `g = x - y`, at `(0, 0)`: `J = 0 1; 1 −1`, `τ = −1`, `Δ = −1`, saddle), `parabola-one` (at `(1, 1)`: `J = −2 1; 1 −1`, `τ = −3`, `Δ = 1`, stable node, `λ = (−3 ± √5)/2`), `inconclusive` (`f = -y + x^3`, `g = x + y^3`, at `(0, 0)`: `J = 0 −1; 1 0`, `centre (linearisation inconclusive)`). Shipped `view = linearised`. Pin `jbJ`, `jbType`.
   - Misconception: the Jacobian's classification is always the nonlinear system's behaviour.
   - Worked: `f = y − x²`, `g = x − y`: `J = [[−2x, 1], [1, −1]]`; at `(1, 1)`: `[[−2, 1], [1, −1]]`, `τ = −3`, `Δ = 1`, disc `5 > 0`: a stable node; at `(0, 0)`: `Δ = −1`, a saddle.

8. **predator-and-prey** — Predator and Prey — *Nonlinear systems*
   - Do: write the Lotka–Volterra system, find both equilibria exactly, show the interior one is a centre of the linearisation (`τ = 0`), and read the cycles off the drawn trajectory while saying the drawing is not a proof.
   - Lab: `dekit`/`jacobian`, `view: trajectory`. Presets: `classic` (`f = 2x - x y`, `g = -y + x y`, points `(0, 0), (1, 2)`, start `(1, 1)`: at `(1, 2)`: `J = 0 −1; 2 0`, `τ = 0`, `Δ = 2`, `centre (linearisation inconclusive)`; at `(0, 0)`: saddle), `slow` (`f = x - x y/2`, `g = -y/2 + x y/4`: interior `(2, 2)`), `start-near` (`classic`, start `(1, 2)` itself: stays). Shipped `view = trajectory`. Pin `jbCheck`, `jbType`.
   - Misconception: predators and prey settle to constant populations.
   - Worked: `x′ = 2x − xy`, `y′ = −y + xy`: equilibria `(0, 0)` and `(1, 2)`; `J = [[2 − y, −x], [y, x − 1]]`; at `(1, 2)`: `[[0, −1], [2, 0]]`, `τ = 0`, `Δ = 2`: the linearisation is a centre, and the true orbits are the closed curves `x − ln x + y − 2ln y = const` the lesson states and the drawing shows.

9. **competing-species** — Competing Species — *Nonlinear systems*
   - Do: find the four equilibria of a two-species competition model, classify each from its Jacobian, and conclude whether the species coexist.
   - Lab: `dekit`/`jacobian`, `view: linearised`. Presets: `exclusion` (`f = x(3 - x - 2y)`, `g = y(2 - x - y)`, points `(0, 0), (3, 0), (0, 2), (1, 1)`, at `(1, 1)`: `J = −1 −2; −1 −1`, `τ = −2`, `Δ = −1`, saddle — coexistence unstable), `exclusion-corner` (at `(3, 0)`: `J = −3 −6; 0 −1`, stable node), `coexist` (`f = x(2 - x - y/2)`, `g = y(2 - y - x/2)`, at `(4/3, 4/3)`: `Δ > 0`, stable node). Shipped `view = linearised`. Pin `jbCheck`, `jbDet`, `jbType`.
   - Misconception: two competing species always drive one to extinction.
   - Worked: `x + 2y = 3`, `x + y = 2` give `(1, 1)`; `J = [[3 − 2x − 2y, −2x], [−y, 2 − x − 2y]]` there is `[[−1, −2], [−1, −1]]`, `Δ = 1 − 2 = −1 < 0`: a saddle, so almost every start leaves it for `(3, 0)` or `(0, 2)`, both stable nodes.

10. **an-epidemic-model** — An Epidemic Model — *Nonlinear systems*
    - Do: write the SIR equations in `S` and `I`, compute `R₀ = βS₀/γ` exactly, find where `I` peaks (`S = γ/β`), and explain why the equilibria are not isolated.
    - Lab: `dekit`/`jacobian`, `view: trajectory`. Presets: `outbreak` (`f = -S I/2`, `g = S I/2 - I/4`, variables named `S, I`, points `(9/10, 0)`, start `(9/10, 1/10)`: `R₀ = 9/5`, peak at `S = 1/2`, `jbExtra` = `R₀ = 9/5; I peaks at S = 1/2`; `jbType` = `non-isolated equilibria`), `contained` (`g = S I/2 - I`, start `(9/10, 1/10)`: `R₀ = 9/20 < 1`), `everyone-susceptible` (start `(99/100, 1/100)`). Shipped `view = trajectory`. Pin `jbExtra`, `jbType`.
    - Misconception: an epidemic ends because everyone has been infected.
    - Worked: `S′ = −βSI`, `I′ = βSI − γI` with `β = 1/2`, `γ = 1/4`, `S₀ = 9/10`: `R₀ = (1/2)(9/10)/(1/4) = 9/5 > 1`, so `I` rises at first; `I′ = 0` when `S = γ/β = 1/2`, the peak; afterwards `I` falls while `S` is still `1/2` of the population — it ends because too few remain susceptible, not because none do.

### Course 10 — Laplace Transforms (`laplace-transforms`, 8)

Modules: *The transform* (1–3), *Solving with it* (4–6), *Switched forcing
and a comparison* (7–8).

1. **the-laplace-transform** — The Laplace Transform — *The transform*
   - Do: state `ℒ[f](s) = ∫₀^∞ e^(−st)·f(t) dt`, compute `ℒ[1] = 1/s` and `ℒ[e^(at)] = 1/(s − a)` as the claims the truncated integrals demonstrate, and read the transform of a signal as an exact rational function of `s`.
   - Lab: `dekit`/`laplace`, `kind: table`. Presets: `one` (`f = 1`: `1/s`; banner shows `∫₀ᵀ e^(−t) dt` at `T = 1, 2, 5`: `≈ 0.632121, 0.864665, 0.993262`), `exp` (`f = e^(2t)`: `1/(s − 2)`), `ramp` (`f = t`: `1/s²`). Pin `lpF`.
   - Misconception: `ℒ[f]` is a number.
   - Worked: `ℒ[e^(2t)] = ∫₀^∞ e^(−(s − 2)t) dt = 1/(s − 2)` for `s > 2`; the lab prints the rational function exactly and, for `f = 1` at `s = 1`, the truncated integrals `1 − e^(−T)` closing in on `1`.

2. **linearity-and-the-table** — Linearity and the Table — *The transform*
   - Do: use linearity and the table (`tⁿ`, `e^(at)`, `cos(bt)`, `sin(bt)`, `t·e^(at)`) to transform a signal, exactly.
   - Lab: `dekit`/`laplace`, `kind: table`. Presets: `mixed` (`f = 3t^2 - 2e^(-t)`: `6/s³ − 2/(s + 1)`, combined `(6s + 6 − 2s³)/(s³(s + 1))`), `cosine` (`f = cos(2t)`: `s/(s² + 4)`), `shifted` (`f = t e^(3t)`: `1/(s − 3)²`). Pin `lpF`.
   - Misconception: `ℒ[f·g] = ℒ[f]·ℒ[g]`.
   - Worked: `ℒ[3t² − 2e^(−t)] = 3·(2/s³) − 2·(1/(s + 1)) = 6/s³ − 2/(s + 1)`; over a common denominator `(6s + 6 − 2s³)/(s³(s + 1))`, which the lab prints in lowest terms.

3. **the-transform-of-a-derivative** — The Transform of a Derivative — *The transform*
   - Do: state `ℒ[y′] = s·Y − y(0)` and `ℒ[y″] = s²·Y − s·y(0) − y′(0)`, and verify the first on a signal by transforming `f′` directly and comparing.
   - Lab: `dekit`/`laplace`, `kind: derivative`. Presets: `exp` (`f = e^(2t)`: `ℒ[f′] = 2/(s − 2)`; `sF − f(0) = s/(s − 2) − 1 = 2/(s − 2)`; `equal`), `sine` (`f = sin(t)`: `s/(s² + 1)` both ways), `poly` (`f = t^2`: `2/s²` both ways). Pin `lpF`, `lpEqual`.
   - Misconception: `ℒ[y′] = s·Y` (the initial value forgotten).
   - Worked: `f = e^(2t)`, `f′ = 2e^(2t)`: `ℒ[f′] = 2/(s − 2)`; `s·ℒ[f] − f(0) = s/(s − 2) − 1 = (s − (s − 2))/(s − 2) = 2/(s − 2)`; the two rational functions are equal.

4. **solving-an-initial-value-problem** — Solving an Initial Value Problem — *Solving with it*
   - Do: transform both sides of a constant-coefficient equation, solve for `Y(s)` as a rational function, invert through partial fractions, and verify the result by substitution.
   - Lab: `dekit`/`laplace`, `kind: solve`. Presets: `decay` (`y'' + 3y' + 2y = 0`, ic `(1, 0)`: `Y = (s + 3)/((s + 1)(s + 2)) = 2/(s + 1) − 1/(s + 2)`, `y = 2e^(−t) − e^(−2t)`), `first-order` (`y' + 2y = 6`, ic `y(0) = 0`: `Y = 6/(s(s + 2)) = 3/s − 3/(s + 2)`), `damped` (`y'' + 2y' + 5y = 0`, ic `(0, 2)`: `Y = 2/((s + 1)² + 4)`, `y = e^(−t)·sin(2t)`). Pin `lpY`, `lpPartial`, `lpSolution`.
   - Misconception: the initial conditions are applied after inverting, as in the characteristic-equation method.
   - Worked: `y″ + 3y′ + 2y = 0`, `y(0) = 1`, `y′(0) = 0`: `(s² + 3s + 2)Y − s − 3 = 0`; `Y = (s + 3)/((s + 1)(s + 2)) = 2/(s + 1) − 1/(s + 2)`; `y = 2e^(−t) − e^(−2t)` — the answer “Real Distinct Roots” found by fitting constants.

5. **partial-fractions-exactly** — Partial Fractions, Exactly — *Solving with it*
   - Do: decompose a rational function with linear, repeated and irreducible-quadratic factors into the table's forms, with exact coefficients, and invert each piece.
   - Lab: `dekit`/`laplace`, `kind: partial`. Presets: `two-linear` (`F = (s + 3)/(s^2 + 3s + 2)`: `2/(s + 1) − 1/(s + 2)`), `repeated` (`F = 1/(s (s + 1)^2)`: `1/s − 1/(s + 1) − 1/(s + 1)²`, inverse `1 − e^(−t) − t·e^(−t)`), `quadratic` (`F = 1/(s (s^2 + 2s + 5))`: `1/(5s) − (s + 2)/(5((s + 1)² + 4))`, inverse `1/5 − (1/5)e^(−t)cos(2t) − (1/10)e^(−t)sin(2t)`). Pin `lpPartial`, `lpSolution`.
   - Misconception: a repeated factor `(s + 1)²` needs only the term `A/(s + 1)²`.
   - Worked: `1/(s(s + 1)²) = A/s + B/(s + 1) + C/(s + 1)²`: `s = 0` gives `A = 1`; `s = −1` gives `C = −1`; the `s²` coefficient gives `A + B = 0`, `B = −1`; inverse `1 − e^(−t) − t·e^(−t)`.

6. **the-transfer-function-and-its-poles** — The Transfer Function and Its Poles — *Solving with it*
   - Do: write `H(s) = 1/(a·s² + b·s + c)` for zero initial conditions, identify its poles with the characteristic roots, and state the stability criterion (every pole has negative real part).
   - Lab: `dekit`/`laplace`, `kind: solve`. Presets: `stable` (`y'' + 3y' + 2y = 1`, ic `(0, 0)`: poles `−2, −1`, `y = 1/2 − e^(−t) + (1/2)e^(−2t)`), `oscillatory` (`y'' + 2y' + 5y = 5`, ic `(0, 0)`: poles `−1 ± 2i`), `unstable` (`y'' - y' - 2y = 2`, ic `(0, 0)`: poles `2, −1`, the `e^(2t)` term grows). Pin `lpPoles`, `lpSolution`.
   - Misconception: a pole on the right makes the forced response larger but still bounded.
   - Worked: `y″ + 3y′ + 2y = 1` from rest: `Y = 1/(s(s² + 3s + 2)) = (1/2)/s − 1/(s + 1) + (1/2)/(s + 2)`; the poles `−1, −2` are the characteristic roots and the transient dies; with `s² − s − 2` the pole `2` makes `e^(2t)` appear.

7. **the-unit-step-and-switched-forcing** — The Unit Step and Switched Forcing — *Switched forcing and a comparison*
   - Do: use `ℒ[u(t − c)·f(t − c)] = e^(−cs)·F(s)` to solve an equation whose forcing switches on at `t = c`, and write the solution in two pieces.
   - Lab: `dekit`/`laplace`, `kind: step`. Presets: `switch-on` (`y' + y = u(t - 2)`, ic `y(0) = 0`: `Y = e^(−2s)/(s(s + 1))`, `y = 0 for t < 2; 1 − e^(−(t − 2)) for t ≥ 2`), `pulse` (`y' + y = u(t - 1) - u(t - 3)`), `second-order` (`y'' + y = u(t - π)` is not rational — ship `y'' + 4y = u(t - 1)`, ic `(0, 0)`). Pin `lpY`, `lpSolution`.
   - Misconception: the solution before `t = c` is affected by what happens after.
   - Worked: `y′ + y = u(t − 2)`, `y(0) = 0`: `(s + 1)Y = e^(−2s)/s`; `Y = e^(−2s)(1/s − 1/(s + 1))`; `y = u(t − 2)·(1 − e^(−(t − 2)))`: nothing until `t = 2`, then the charging curve shifted to start there.

8. **three-methods-one-equation** — Three Methods, One Equation — *Switched forcing and a comparison*
   - Do: solve one forced initial value problem by undetermined coefficients with fitted constants, and by Laplace transform, and check the two agree by exact substitution; say when each method is the better tool.
   - Lab: `dekit`/`laplace`, `kind: solve`. Presets: `constant-force` (`y'' + 3y' + 2y = 4`, ic `(0, 0)`: `Y = 4/(s(s + 1)(s + 2)) = 2/s − 4/(s + 1) + 2/(s + 2)`, `y = 2 − 4e^(−t) + 2e^(−2t)`), `cosine-force` (`y'' + 4y = 3cos(t)`, ic `(0, 0)`: `y = cos(t) − cos(2t)`), `exp-force` (`y' + 2y = e^t`, ic `y(0) = 0`: `y = e^t/3 − e^(−2t)/3`). Pin `lpSolution`, `lpCheck`.
   - Misconception: the three methods are three different theories that may disagree.
   - Worked: `y″ + 3y′ + 2y = 4` from rest: by undetermined coefficients `y_p = 2`, `y_h = C₁e^(−t) + C₂e^(−2t)`, `C₁ + C₂ = −2`, `−C₁ − 2C₂ = 0`, so `C₂ = 2`, `C₁ = −4`; by Laplace `Y = 4/(s(s + 1)(s + 2)) = 2/s − 4/(s + 1) + 2/(s + 2)`; both give `y = 2 − 4e^(−t) + 2e^(−2t)`, and the residual is `0`.

---
## §D The lab kits

### D.0 Conventions every mode obeys

`docs/philosophy/PLAN.md` §D.0 binds every mode here — presets are lesson
data, one preset menu per lab, a `label` names the instance and an outcome
goes in `expect`, build-time `ValueError` on a malformed instance and never on
a missing `expect`, hostile text survives inside a try/catch that paints the
banner and blanks every tile to `—`, tiles are `<strong id>` written by
`textContent`, a status banner `id="XXStatus"` says what was computed and from
what, every pure function has a `mathcheck.js` case seen to fail, refusals are
printed and specific. What differs here:

- **Files.** `scripts/mathpath/labs/de_core.py` (shared JavaScript blocks, no
  lab), `scripts/mathpath/labs/calckit.py` (`calckit_lab(cfg)`) and
  `scripts/mathpath/labs/dekit.py` (`dekit_lab(cfg)`); registry keys
  `"calckit"` and `"dekit"`; both join `build_paths.KITS_WITH_EXPECTATIONS` as
  the LAST step (rule 7). Entry points dispatch on `cfg["mode"]` and RAISE on an
  unknown mode, exactly as `markov_lab` does.
- **Per-mode script assembly.** A page ships `algebra_core.RATIONAL_JS` +
  `POLY_JS` + `EXPR_JS` + `PLOT_JS` (always), `SURD_JS` where a mode takes
  square roots, and from `de_core` only the blocks the mode names below
  (`MPOLY_JS`, `EP_JS`, `RF_JS`, `STEP_JS`, `DRAW_JS`, `SHOW_JS`), then that
  mode's own block. Budget: ≤ 45 KB gzipped per lesson page, measured with the
  snippet in `AGENTS.md` before the kit is called done; the heaviest mode is
  `laplace` (`EP_JS` + `RF_JS` + partial fractions) and it is the one to
  measure first.
- **ES5 plus BigInt literals.** `var`, `function`, `prototype`; no arrow
  functions, `let`, `const`, template literals, classes, spread or
  destructuring. BigInt literals (`0n`) are used exactly as `RATIONAL_JS` uses
  them. The whole page shares one `<script>`, so every module-level name is
  prefixed (`DE_`, `CK_`) and nothing is declared twice. No network access of
  any kind (`AGENTS.md` §2).
- **Three printing functions, no fourth** (`SHOW_JS`): `Rtext(r)` for an exact
  rational (`3/4`, `−2`, `0`); `DE_dec(x)` for a double — six significant
  figures, trailing zeros dropped, prefixed `≈ ` (`≈ 0.693147`, `≈ 2.5`); and
  `DE_root(p, s, imaginary)` for a surd or complex pair — `(−1 ± √5)/2`,
  `−1 ± 2i`, `√5`, `2√6` — built on `SURD_JS` but printing `√` rather than
  `sqrt(`. A tile that may hold an exact value or a rounded one prints
  whichever applies and never a bare decimal. `≈` goes through `textContent` as
  the character, never as an entity.
- **Digit budget.** `DE_DIGITS = 2000`. After every exact step, if any
  numerator or denominator in the state has more than 2000 decimal digits, the
  stepper stops, the table shows the steps it completed, the tile named in the
  mode reads `stopped after step n: digit budget`, and the banner says why
  ("a quadratic right-hand side doubles the digits each step"). Nothing is
  rounded to continue. The budget is a constant in `STEP_JS` and is quoted in
  “Blow-Up and the Interval of Existence”.
- **Step caps.** Euler and improved Euler: `n ≤ 64`; RK4: `n ≤ 32`; a step
  `h` must be a positive rational with denominator ≤ 10⁶; `n·h` must keep the
  final `t` within `|t| ≤ 10⁶`. A range control's markup carries the cap.
- **Right-hand sides are polynomials.** Every typed `f(t, y)`, `f(y)`,
  `f(x, y)`, `g(x, y)` is parsed by `EXPR_JS` and converted by `MPOLY_JS`; a
  non-polynomial (`sin`, `sqrt`, `1/y`, `e^t`) is refused with the banner
  "this lab steps polynomial right-hand sides exactly; `sin(t)` is not one".
  Degree ≤ 6, ≤ 24 terms. The two modes that take non-polynomial input
  (`separable`'s `1/y`, `1/y^2`; `linear1`'s `a/t`) say so in their spec.
- **Drawings.** `PLOT_JS`'s `Plot` draws axes, curves (`curve(fn)` samples a
  float function), points, segments and labels; `NumberLine` draws phase lines.
  `DRAW_JS` adds `DE_arrows(plot, f, grid)` (a slope or vector field as short
  segments), `DE_polyline(plot, pts, cls)` and `DE_rk4float(f, start, h, n)`
  (a float trajectory for drawing only, 400 steps, labelled in the legend as
  "drawn by stepping in floating point"). Every exact polygon is drawn with a
  distinct class from every float curve, and the legend names both.

### D.1 `de_core` — the shared blocks

- **`MPOLY_JS`** — polynomials over Q in up to four named variables. A
  polynomial is `{vars: ['t','y'], terms: [{e: [i, j], c: R}]}` normalised
  (sorted exponents, no zero coefficients). `MPadd`, `MPsub`, `MPmul`,
  `MPscale`, `MPeval(p, point)` (exact at rational points), `MPpartial(p,
  var)`, `MPdegree`, `MPtext(p)` in the library's notation (`t² − y`,
  `r·y·(1 − y/K)` is printed expanded: `y − y²/4`), `MPfromExpr(node, vars)`
  (null when the tree is not polynomial: a division by a non-constant, a
  non-integer power, a function call), `MPtoPoly(p, var)` (one-variable
  coefficient list for `POLY_JS` when only `var` appears), `MPsubst(p, var, q)`
  (substitute a polynomial for a variable).
- **`RF_JS`** — rational functions in one variable over Q: `{num, den}` as
  `POLY_JS` lists, normalised by `Pgcd` with a monic denominator. `RFadd`,
  `RFmul`, `RFdiv`, `RFderiv` (quotient rule), `RFeval` (exact; null at a
  pole), `RFtext`, `RFzero`, `RFfromExpr` (null when not rational), and
  `RFpartial(F)`: factor the denominator with `Pfactor`; linear factors of any
  multiplicity and at most one irreducible quadratic remainder (`complete`
  true) are decomposed by solving the exact linear system for the
  coefficients; anything else returns `{refused: "the denominator has an
  irreducible factor of degree 3 or more"}`.
- **`EP_JS`** — exponential-polynomial expressions `Σ c·tᵏ·e^(at)·T(bt)` with
  `T ∈ {1, cos, sin}`, `c, a, b` rational, `k ≥ 0` integer, stored as a sorted
  list of terms `{c, k, a, b, trig}` with like terms merged and zero terms
  dropped (`b = 0` forces `trig = 1`; `sin(0·t)` terms are dropped). `EPadd`,
  `EPscale`, `EPmulpoly(e, p)` (by a polynomial in `t`), `EPderiv` (exact:
  `(tᵏe^(at)cos bt)′ = k·tᵏ⁻¹e^(at)cos bt + a·tᵏe^(at)cos bt − b·tᵏe^(at)sin bt`),
  `EPzero`, `EPtext` (canonical order: by `a`, then `b`, then trig, then `k`;
  the library's notation: `2·e^(−t) − e^(−2t)`, `e^(−t)·(2·cos(2t) + sin(2t))`
  is printed as the flat sum `2·e^(−t)·cos(2t) + e^(−t)·sin(2t)`),
  `EPevalExact(e, t0)` (exact when every term has `a = 0, b = 0`, or when
  `t0 = 0`; else null), `EPevalFloat(e, t)`, `EPparse(text)` for the grammar
  below, `EPlaplace(e)` → `RF_JS` (term rule: `ℒ[tᵏ·g] = (−1)ᵏ·dᵏ/dsᵏ ℒ[g]`
  with `ℒ[e^(at)] = 1/(s − a)`, `ℒ[e^(at)cos bt] = (s − a)/((s − a)² + b²)`,
  `ℒ[e^(at)sin bt] = b/((s − a)² + b²)`, differentiated by `RFderiv`),
  `EPfromPartial(terms)` (the inverse: `1/(s − a)ᵏ ↔ tᵏ⁻¹e^(at)/(k − 1)!`, and
  `(A·s + B)/((s − α)² + β²) ↔ e^(αt)(A·cos βt + ((B + Aα)/β)·sin βt)`,
  refusing when `β²` is not a perfect square rational).
  Candidate grammar (ASCII, what the reader types): terms joined by `+`/`-`;
  a term is an optional rational coefficient, optional `t` or `t^k`, optional
  `e^(r t)` / `e^(rt)` / `e^(-t)` / `e^(t/3)` with `r` rational, optional
  `cos(b t)` / `sin(b t)` with `b` rational, optional symbolic `C` or `D` as a
  coefficient; spaces optional. `C` and `D` are handled by parsing three times
  with `(C, D) = (0, 0), (1, 0), (0, 1)` and once more with `(1, 1)` to check
  linearity; a candidate that is not linear in `C, D` is refused.
- **`STEP_JS`** — exact steppers over `MPOLY_JS` right-hand sides in one or
  two unknowns: `DE_euler(f, t0, y0, h, n)`, `DE_heun`, `DE_rk4`, each returning
  `{rows: [{t, y}], stopped: n | k, digits}` and honouring the digit budget;
  `DE_eulerSys(f, g, t0, x0, y0, h, n)` for systems; `DE_digits(state)`.
- **`DRAW_JS`**, **`SHOW_JS`** as in D.0.

Every function above is module-level and named, and `scripts/mathcheck.js`
gets at least one case per function that was seen to FAIL when the function
was broken on purpose. The cases to write first, because they are the ones a
wrong implementation passes by accident: `EPderiv` on `t·e^(−2t)` (product
rule inside the class), `EPlaplace` on `t·e^(3t)` (`1/(s − 3)²`), `RFpartial`
on `1/(s(s + 1)²)` (the repeated factor), `DE_rk4` on `y′ = t³` over `[0, 1]`
with `h = 1/4` (error exactly `0`), `DE_euler` on `y′ = y²` to the digit
budget (stops after step 11 with `h = 1/4`).

### D.2 `calckit` — seven modes

Tile ids are prefixed per mode; the preset menu is `XXPreset`, the banner
`XXStatus`. Common cfg: `mode`, `preset`, `presets[{id, label, …, expect}]`,
`panel_title`, `panel_intro`.

#### quotient (`qt`)
- Purpose: the exact difference quotient at a point for a halving column of `h`.
- cfg: `presets[{id, label, f: str, a: rational, h: rational, halvings: int (0–12)}]`, `show_limit` (bool, default true).
- Controls: `qtPreset`; `qtF` (text; polynomial or rational function in `t`, via `RFfromExpr`); `qtA`, `qtH` (text); `qtHalvings` (range 0–12).
- Computation: for `k = 0…halvings`, `hₖ = h/2ᵏ`, `Qₖ = (f(a + hₖ) − f(a))/hₖ` exactly by `RFeval`; the limit `f′(a) = RFeval(RFderiv(f), a)`; gaps `|Qₖ − f′(a)|`. Stage: the table (`h`, `f(a + h)`, quotient, gap) and the plot of `f` with the secant for the current smallest `h` and the tangent.
- Tiles: `qtFirst` (`Q₀`, `Rtext`); `qtLast` (the last quotient); `qtGap` (`|last − f′(a)|`); `qtLimit` (`f′(a)`; the tile is omitted from the markup when `show_limit` is false).
- Refusals: not a rational function; `a` or `a + hₖ` a pole; `h ≤ 0`.
- Serves: 1.1, 1.3, 1.5.

#### hpoly (`hp`)
- Purpose: the difference quotient as a polynomial in `h`; the product and chain rules verified.
- cfg: `presets[{id, label, kind: single | product | compose, f: str, g: str | null, a: rational | null}]`.
- Controls: `hpPreset`; `hpF`, `hpG` (text; `hpG` labelled "inner function" under `compose`, "second factor" under `product`, hidden under `single`); `hpA` (text, may be empty).
- Computation (`MPOLY_JS` in `t, h`): single: `Q = (f(t + h) − f(t))/h`, exact polynomial division by `h`; `hpConst` = the `h⁰` coefficient as a polynomial in `t`. product: `Q` for `f·g`, and `rule = f′g + fg′` (`Pderiv`); equality `MPsub(const, rule)` zero. compose: `Q` for `f(g(t))`, `rule = f′(g(t))·g′(t)`.
- Tiles: `hpQ` (`MPtext`, e.g. `2t + h`); `hpConst` (`2t`); `hpRule` (`3t² + 2t` | `—` under single; under product the tile text is `f′g + fg′ = 3t² + 2t; f′g′ = 2t`); `hpEqual` (`equal` | `differ` | `—`); `hpAt` (`Q` at `t = a`, `h = 1/8` as a fraction | `—`).
- Refusals: not a polynomial; degree of the composition > 12.
- Serves: 1.2, 1.8, 1.9.

#### tangent (`tg`)
- Purpose: the tangent line and the exact error of the linear approximation.
- cfg: `presets[{id, label, f: str, a: rational, h: rational}]`.
- Controls: `tgPreset`; `tgF` (rational function); `tgA`, `tgH` (text).
- Computation: `f(a)`, `f′(a)` by `RFderiv`; line `y = f(a) + f′(a)(t − a)` printed expanded; `approx = f(a) + f′(a)·h`; `true = f(a + h)`; `error = true − approx` (signed). Stage: `f`, the tangent, the two points.
- Tiles: `tgValue`, `tgSlope`, `tgApprox`, `tgTrue`, `tgError` (fractions); `tgLine` (`y = 4t − 4`).
- Serves: 1.4.

#### derivative (`dv`)
- Purpose: `p′` and `p″`, their rational zeros, sign charts.
- cfg: `presets[{id, label, f: str, order: 1 | 2, window: [tmin, tmax]}]`.
- Controls: `dvPreset`; `dvF` (polynomial); `dvOrder` (redraw-only select `1 | 2`, shipped from cfg).
- Computation: `Pderiv` once or twice; `Prationalroots` of `p′` and of `p″`; sign of `p′` on the intervals between its rational roots (test at the midpoint, exact); inflection = rational roots of `p″` where the sign of `p″` changes. Stage: `p`, `p′` (and `p″`) on one plot, the zeros marked.
- Tiles: `dvDeriv` (`Ptext`); `dvSecond` (`Ptext` | `—`); `dvZeros` (`1, 3` | `none rational` | `0 (no sign change)` when a root does not change sign — the text appends the note); `dvIntervals` (`rising t < 1; falling 1 < t < 3; rising t > 3`); `dvInflect` (`t = 1` | `t = −1, 1` | `none` | `—` when order 1).
- Serves: 1.6, 1.7, 1.10.

#### transcendental (`tq`)
- Purpose: rounded, labelled quotients of `bᵗ`, `sin`, `cos`, and what they approach.
- cfg: `presets[{id, label, kind: exp | sin | cos, b: rational | "e", a: rational, h: rational, halvings: int}]`.
- Controls: `tqPreset`; `tqKind` (redraw-only select, set by the preset); `tqB` (text; `e` accepted); `tqA`, `tqH` (text); `tqHalvings` (range 0–12).
- Computation: quotients in doubles; the only exact entry is `exp` at `h = 1`, `(b − 1)·bᵃ` when `b` is rational, and it is printed with `Rtext`; the limit: `exp` → `bᵃ·ln b`, `sin` → `cos a`, `cos` → `−sin a`, printed `DE_dec` with the symbolic form first (`ln 2 ≈ 0.693147`, `cos(1) ≈ 0.540302`, `cos(0) = 1`); `tqRatio` = the last quotient divided by `f(a)` (for `exp`, the factor that does not depend on `a`).
- Tiles: `tqFirst`, `tqLast` (`1` | `≈ 0.841471`); `tqLimit` (`ln 2 ≈ 0.693147`); `tqRatio` (`≈ 0.700` | `—` when `f(a) = 0`).
- Refusals: `b ≤ 0`; `h ≤ 0`.
- Serves: 1.11, 7.1.

#### riemann (`rs`)
- Purpose: exact left, right, trapezoid and midpoint sums; exact error and error ratio on doubling.
- cfg: `presets[{id, label, f: str, a: rational, b: rational, n: int}]`, `rule` (`left | right | trap | mid`).
- Controls: `rsPreset`; `rsF` (polynomial or `1/t`-type rational function); `rsA`, `rsB` (text); `rsN` (range 1–64); `rsRule` (redraw-only select).
- Computation: `h = (b − a)/n`; the sum under the rule, exact by `RFeval`; `rsExact`: for a polynomial, `F(b) − F(a)` exactly; for `1/t` with `0 < a < b`, `≈ ln(b/a)` as `DE_dec` with the suffix ` (ln 2, rounded)` naming the log when `a = 1` and `b` an integer, else ` (rounded)`; error `sum − exact` (exact or `≈`); the sum at `2n` and the ratio `error(n)/error(2n)` (exact fraction when both exact, else `≈`); `rsGap` = `Rₙ − Lₙ`.
- Tiles: `rsSum` (`7/32`); `rsSumDec` (`≈ 0.21875`); `rsExact` (`1/3` | `≈ 0.693147 (ln 2, rounded)`); `rsError` (`−11/96` | `≈ …`); `rsGap` (`1/4`); `rsRatio` (`2` | `44/23` | `≈ 1.913` | `—` when the error is 0).
- Refusals: `b ≤ a`; a pole of `f` in `[a, b]`; `n > 64`.
- Serves: 2.1, 2.2, 2.3, 2.4, 2.8.

#### antiderivative (`ad`)
- Purpose: `F`, its constant, `F(b) − F(a)`, linearity and additivity checked.
- cfg: `presets[{id, label, f: str, g: str | null, coeffs: [c, d] | null, ic: [t0, y0] | null, a: rational | null, b: rational | null, split: rational | null}]`.
- Controls: `adPreset`; `adF`, `adG` (text; `adG` hidden when `g` is null), `adCoeffs` (text `c d`), `adIC` (text `t0 y0`), `adA`, `adB`, `adSplit` (text).
- Computation: `F` by the reverse power rule (`Pintegral`, written here); `C` from `F(t0) + C = y0`; `F(b) − F(a)`; with `g`: `∫(c·f + d·g)` directly and `c∫f + d∫g`, compared; with `split = m`: `∫ₐᵐ + ∫ₘᵇ` against `∫ₐᵇ`.
- Tiles: `adF` (`t³/3 + C`); `adC` (`4` | `—`); `adDefinite` (`1/3` | `—`); `adLinear` (`equal: 12 = 8 + 4` | `—`); `adSplit` (`equal: 12 = 2 + 10` | `—`).
- Serves: 2.5, 2.6, 2.7.

### D.3 `dekit` — fifteen modes

Common cfg as in D.2. Equations are typed with ASCII primes (`y'`, `y''`) and
`t`; systems use `x`, `y` (and `S`, `I` where a preset names variables — the
`vars` field).

#### verify (`vf`)
- Purpose: substitute a candidate into an equation and read the residual.
- cfg: `presets[{id, label, equation: str, candidate: str, ic: [t0, y0] | [t0, y0, v0] | null}]`.
- Controls: `vfPreset`; `vfEq` (text: `lhs = rhs` in `t, y, y', y''`); `vfCand` (text: the EP grammar, or a rational function of `t`); `vfIC` (text `t0 y0` or `t0 y0 v0`, may be empty).
- Computation: `vfEq` → `MPOLY` in `t, y, y1, y2` (`y'` → `y1`, `y''` → `y2`) as `lhs − rhs`; order = highest of `y1, y2` present; linear iff degree ≤ 1 in `(y, y1, y2)` jointly. Candidate class: `RF` if `RFfromExpr` succeeds; else `EP` via `EPparse`. Residual: RF — substitute `y, y′, y″` as rational functions and evaluate the polynomial over `RF_JS`; zero iff the numerator is zero. EP in a linear equation whose coefficients are polynomials in `t` — `EPmulpoly` and `EPderiv`, residual an EP; zero iff `EPzero`. EP in a nonlinear equation — not decidable in the class: residual evaluated in doubles at `t = 0, 1/2, 1, 3/2, 2`, verdict `Checked at 5 points only`, residual tile `≈ max |r| = …`. `C`, `D`: the three-way parse; the residual must vanish for the `(0,0)` part and each unit direction; IC solves the exact linear system for `C` (and `D`) using `EPevalExact` at `t0` (refused when `t0 ≠ 0` for a transcendental candidate: `—` and the banner).
- Tiles: `vfOrder` (`1` | `2`); `vfLinear` (`Linear` | `Nonlinear`); `vfResidual` (`0` | `3t² − 2t` | `−2·e^t` | `≈ 0.0417 at most`); `vfVerdict` (`Solution` | `Not a solution` | `Checked at 5 points only`); `vfIC` (`satisfied` | `fails: y(0) = 3/2` | `—`); `vfFamily` (`C = 4 from y(1) = 5` | `C = 1, D = −2` | `C free` | `—`).
- Stage: the candidate drawn (floats), and for a first-order equation the slope field behind it.
- Refusals: parse error; order > 2; an unknown letter.
- Serves: 3.1, 3.2, 3.3, 7.2.

#### field (`sf`)
- Purpose: a slope field; the exact slope at one grid point; nullcline; horizontal solutions.
- cfg: `presets[{id, label, f: str, window: [tmin, tmax, ymin, ymax], start: [t0, y0] | null, point: [t, y]}]`, `grid` (`11 | 15 | 21`).
- Controls: `sfPreset`; `sfF` (polynomial in `t, y`); `sfWindow` (text `tmin tmax ymin ymax`); `sfStart` (text, may be empty); `sfPoint` (text `t y`); `sfGrid` (redraw-only select).
- Computation: arrows at the grid (floats); `sfSlope = MPeval(f, point)` exact; `sfSign` from its sign; nullcline: if `f` has degree 1 in `y`, solve for `y` as a rational function of `t` and print `y = t`; if `f` has no `y`, `none in y`; if `f` has no `t`, its rational roots `y = 0, y = 1`; else `—`; `sfEquil`: the rational roots when `f` has no `t` (the horizontal solutions), else `none`. The solution through `start` is drawn by `DE_rk4float` and labelled "drawn".
- Tiles: `sfSlope` (`0` | `−3/4`); `sfSign` (`rising` | `falling` | `flat`); `sfZero` (`y = t` | `y = 0, y = 1` | `none in y` | `—`); `sfEquil` (`y = 0, y = 1` | `none`).
- Serves: 3.4, 3.5.

#### euler (`eu`)
- Purpose: exact Euler steps and the exact error against a known solution.
- cfg: `presets[{id, label, f: str, t0, y0, h, n, exact: str | null}]`.
- Controls: `euPreset`; `euF`; `euStart` (text `t0 y0`); `euH` (text); `euN` (range 1–64); `euExact` (text, EP or RF, may be empty).
- Computation: `DE_euler`; the table `tₙ, yₙ, f(tₙ, yₙ)`, and when `exact` is given `y(tₙ)` (exact if RF, or EP with `tₙ = 0`; else `DE_dec`) and `|yₙ − y(tₙ)|`; `euExact` reads `undefined at t = 5/4` when `RFeval` hits a pole.
- Tiles: `euLast` (`625/256`); `euLastDec` (`≈ 2.44141`); `euExact` (`4` | `≈ 2.71828` | `undefined at t = 5/4` | `—`); `euError` (`1/4` | `≈ 0.276875` | `—`); `euDigits` (integer: the widest denominator); `euStopped` (`all 16 steps` | `stopped after step 11: digit budget`).
- Serves: 3.6, 3.10.

#### order (`od`)
- Purpose: errors at three step sizes, their exact ratios, the observed order.
- cfg: `presets[{id, label, f: str, t0, y0, T, exact: str, hs: [h1, h2, h3]}]`, `method` (`euler | heun | rk4`).
- Controls: `odPreset`; `odF`, `odStart`, `odT`, `odExact`, `odHs` (text `1/4 1/8 1/16`); `odMethod` (redraw-only select).
- Computation: `N = (T − t0)/h` must be an integer within the cap; `E(h) = |y_N − y(T)|` (exact when `y(T)` is exact); ratios `E(h₁)/E(h₂)`, `E(h₂)/E(h₃)`; order = `log₂` of the last ratio: printed as an integer when the ratio is exactly a power of 2, else `≈`.
- Tiles: `odE1`, `odE2`, `odE3` (`1/4` | `≈ 0.0286` | `0`); `odRatio` (`2, 2` | `44/23, 92/47` | `≈ 1.91, ≈ 1.96` | `—` when an error is 0); `odOrder` (`1` | `2` | `4` | `≈ 0.969` | `exact (error 0)`).
- Refusals: `(T − t0)/h` not an integer; `N` over the cap; `exact` unparseable.
- Serves: 3.7, 3.8, 3.9.

#### separable (`sp`)
- Purpose: `g(y)·y′ = h(t)` integrated on both sides, exactly.
- cfg: `presets[{id, label, g: str, h: str, ic: [t0, y0] | null}]`, `view` (`solve | check`).
- Controls: `spPreset`; `spG` (text: a polynomial in `y`, or exactly `1/y` or `1/y^2`); `spH` (polynomial in `t`); `spIC` (text); `spView` (redraw-only).
- Computation: `G = ∫g` (polynomial; `1/y` → `ln|y|`, `1/y^2` → `−1/y`), `H = ∫h`; `C = G(y0) − H(t0)` exact (for `ln|y|` the constant is kept as `ln|y0|` symbolically and the explicit form `y = y0·e^(H(t) − H(t0))` printed, since `g = 1/y` is the growth equation); implicit `G(y) = H(t) + C`; explicit when `deg G = 1` (polynomial) or `deg G = 2` (quadratic in `y` with coefficients polynomial in `t`: `y = (−b ± √(b² − 4ac))/(2a)`, branch by the sign of `y0 − vertex`), or `G = −1/y` (`y = −1/(H + C)`), else `implicit only`; domain: where the radicand ≥ 0 (its rational roots give the interval) or where the denominator ≠ 0. `check` view: differentiate `G(y(t))` via the chain rule for the explicit solution as an RF or a surd expression and compare with `h(t)`: `equal`.
- Tiles: `spG` (`y²/2`); `spH` (`t²/2`); `spC` (`2` | `—`); `spImplicit` (`y² = t² + 4`); `spExplicit` (`y = √(t² + 4)` | `y = −√(t² + 4)` | `y = 2/(2 − t²)` | `implicit only`); `spDomain` (`all t` | `−1 < t < 1` | `t < 1`); `spCheck` (`equal` | `—`).
- Refusals: `g` not in the accepted set; `g(y0) = 0` for the reciprocal forms; a radicand negative at `t0`.
- Serves: 4.1, 4.2, 4.3.

#### growth (`gr`)
- Purpose: `y′ = k·(y − A)` exactly by Euler and symbolically.
- cfg: `presets[{id, label, k, y0, A: rational (default 0), h, n, target: rational | null}]`.
- Controls: `grPreset`; `grK`, `grY0`, `grA`, `grH` (text); `grN` (range 1–64); `grTarget` (text, may be empty).
- Computation: factor `1 + kh`; `yₙ = A + (y0 − A)(1 + kh)ⁿ` exact (and checked against the recursion); true `A + (y0 − A)e^(k·nh)` rounded; error rounded; `T = ln 2/|k|` (doubling for `k > 0`, halving for `k < 0`; the symbolic text `ln 2/(1/2)` then `≈`); hit: the first `m ≤ n` with `yₘ` past `target` in the direction of travel (`step 6 (t = 3/2)` | `never within 8 steps`); steady state `A`.
- Tiles: `grFactor` (`5/4`); `grLast` (`625/256`); `grTrue` (`≈ 2.71828`); `grError` (`≈ 0.276875`); `grT` (`≈ 1.38629` | `—` when `k = 0`); `grHit` (`step 6 (t = 3/2)` | `never within 8 steps` | `—`); `grSteady` (`20` | `200` | `0 (repelling)` — the equilibrium `A` exists for every `k ≠ 0`; the tile prints `A` and appends ` (repelling)` when `k > 0`).
- Refusals: `k = 0` ("not a growth equation"); `h ≤ 0`.
- Serves: 4.4, 4.5, 4.6, 4.7, 4.8.

#### autonomous (`au`)
- Purpose: `y′ = f(y)`: equilibria, stability, `f′(y*)`, limits, exact steps, inflection levels.
- cfg: `presets[{id, label, f: str, starts: [rational], h, n, window: [tmax, ymin, ymax]}]`, `view` (`line | steps | curves`).
- Controls: `auPreset`; `auF` (polynomial in `y`, degree ≤ 4); `auStarts` (text `0 2 4`); `auH`; `auN` (range 1–64); `auView` (redraw-only select).
- Computation: equilibria = `Prationalroots(f)` plus, when `Pfactor(f).rest` is quadratic, its surd roots (`DE_root`); signs of `f` between consecutive equilibria (test at midpoints, and at `min − 1`, `max + 1`), each equilibrium classified `stable | unstable | semistable`; `f′` at each rational equilibrium exactly; for each start, its limit from the phase line (`→ 4` | `→ +∞` | `→ −∞` | `at equilibrium`); exact Euler from each start to the budget; inflection levels = rational roots of `f′` at which `f′` changes sign. Stage: `line` → `NumberLine` with arrows and the equilibria; `steps` → the exact polygons on a `t`–`y` plot with the equilibria as horizontal lines; `curves` → float-drawn solution curves (labelled) plus the exact first steps.
- Tiles: `auEquil` (`0, 4` | `0, (1 ± √5)/2` | `none`); `auTypes` (`0 unstable; 4 stable`); `auSlope` (`f′(0) = 1; f′(4) = −1`); `auLimit` (for the first start: `→ 4` | `→ +∞`); `auSteps` (`12 exact steps` | `11 exact steps, then digit budget`); `auInflect` (`y = 2` | `none rational`).
- Serves: 4.9, 4.10, 5.1, 5.2, 5.3, 5.4, 5.5, 5.8.

#### bifurcate (`bf`)
- Purpose: equilibria of `y′ = f(y, a)` against a parameter.
- cfg: `presets[{id, label, f: str, a: rational, range: [amin, amax]}]`.
- Controls: `bfPreset`; `bfF` (polynomial in `y` and `a`, degree ≤ 3 in `y`); `bfA` (text); `bfRange` (text `amin amax`).
- Computation: at the current `a`: substitute, then as `autonomous` (equilibria, types); critical values: where `f` and `∂f/∂y` share a root — for `deg_y f ≤ 2`, the discriminant in `y` as a polynomial in `a`, its rational roots; for degree 3, the resultant `Res_y(f, f_y)` via `MPOLY_JS` and its rational roots; `bfCount`. Stage: the diagram — for 61 values of `a` across the range, the real roots of `f(·, a)` in floats (drawing), solid where `f_y < 0`, dashed where `f_y > 0`, the current `a` marked.
- Tiles: `bfEquil` (`−2, 2` | `0` | `none`); `bfTypes` (`−2 stable; 2 unstable`); `bfCount` (`2 equilibria`); `bfCritical` (`a = 0` | `a = 0, 1/4` | `none rational in [−4, 1]`).
- Serves: 5.6, 5.7.

#### linear1 (`lf`)
- Purpose: `y′ + p(t)·y = q(t)` solved symbolically.
- cfg: `presets[{id, label, equation: str, ic: [t0, y0] | null, h, n}]`, `view` (`solve | parts | steps`).
- Controls: `lfPreset`; `lfEq` (text: any first-order linear equation whose normalisation gives `p` a rational constant or `a/t` with `a` an integer `1…4` or `−1…−4`, and `q` an EP or a polynomial); `lfIC`; `lfH`, `lfN` (steps view, constant coefficients only); `lfView` (redraw-only).
- Computation: normalise (divide by the coefficient of `y′`); `μ`: `e^(at)` for constant `p = a`, `tᵃ` for `p = a/t`; `y_h`: `C·e^(−at)` or `C·t^(−a)`; `y_p`: constant `p`, polynomial `q` → polynomial of the same degree by exact coefficient matching (one degree higher when `a = 0`); constant `p`, EP `q` → EP with the same `(a, b)` support, coefficients by exact matching, multiplied by `t` on the resonant support (`q` containing `e^(−at)`); `p = a/t`, polynomial `q` → `y = (∫tᵃq dt + C)/tᵃ` as an RF; `C` from the IC: exact when `y_p` is evaluable exactly at `t0` (always at `t0 = 0`; anywhere for polynomial or RF); steady state `b/a` when `p = a ≠ 0` and `q = b` constant, `none` otherwise; `steps`: exact Euler as `growth`.
- Tiles: `lfMu` (`e^(3t)` | `t²`); `lfYh` (`C·e^(−3t)` | `C/t²`); `lfYp` (`(2/3)·t − 2/9` | `(2/5)·cos(t) + (1/5)·sin(t)` | `t·e^(−2t)` | `t³/5`); `lfC` (`11/9` | `—`); `lfSteady` (`3` | `−2 (repelling)` | `none`); `lfSolution` (`y = (2/3)·t − 2/9 + (11/9)·e^(−3t)` | with `C` when unfitted).
- Refusals: not linear; `p` outside the accepted forms; `q` outside EP/polynomial; an IC at `t0 ≠ 0` with a transcendental `y_p`; `t0 = 0` for `p = a/t`.
- Serves: 6.1–6.7.

#### stiff (`sk`)
- Purpose: Euler's factor on `y′ = −a·y`.
- cfg: `presets[{id, label, a, y0, h, n}]`, `scheme` (`forward | backward`).
- Controls: `skPreset`; `skA`, `skY0`, `skH` (text); `skN` (range 1–64); `skScheme` (redraw-only).
- Computation: forward factor `1 − ah`, backward `1/(1 + ah)`; the sequence under the shipped scheme exactly; verdict from the factor `ρ`: `ρ > 1` grows, `0 < ρ ≤ 1` decays (`= 1` constant), `−1 < ρ < 0` oscillates and decays, `ρ ≤ −1` oscillates and grows; bound `h < 2/a`; true `y0·e^(−a·nh)` rounded.
- Tiles: `skFactor` (`−3/2`); `skVerdict` (`decays` | `constant` | `grows` | `oscillates and decays` | `oscillates and grows`); `skLimit` (`h < 2/5`); `skLast` (`6561/256`); `skTrue` (`≈ 2.06115e-9` — six significant figures in scientific form when `|x| < 10⁻⁴`); `skBackward` (`2/7`).
- Serves: 6.8.

#### char (`ce`)
- Purpose: `a·y″ + b·y′ + c·y = 0`: roots, kind, general solution, constants, Wronskian.
- cfg: `presets[{id, label, a, b, c, ic: [y0, v0] | null}]`, `view` (`roots | solution | wronskian`).
- Controls: `cePreset`; `ceA`, `ceB`, `ceC` (text); `ceIC` (text `y0 v0`, may be empty); `ceView` (redraw-only).
- Computation: `quadroots(a, b, c)`; kind `rational | irrational | double | complex` printed as in the tile; general solution text per kind; constants: solve the 2×2 system at `t = 0` exactly when the roots are rational, or double, or complex with rational `α, β`; else `—` with the banner "the roots are irrational; the constants would be surds and this lab fits only rational ones"; Wronskian at 0: `r₂ − r₁` for distinct real (rational or surd), `β` for complex, `1` for double; the fitted solution as an EP, and its residual (always `0`, printed in the banner as the check).
- Tiles: `ceDisc` (`1` | `−16`); `ceKind` (`two real roots` | `two real roots (irrational)` | `one repeated root` | `complex pair`); `ceRoots` (`−2, −1` | `−2 (repeated)` | `−1 ± 2i` | `(1 ± √5)/2`); `ceGeneral` (`C₁·e^(−2t) + C₂·e^(−t)` | `(C₁ + C₂·t)·e^(−2t)` | `e^(−t)·(C₁·cos(2t) + C₂·sin(2t))`); `ceC` (`C₁ = 2, C₂ = −1` | `—`); `ceSolution` (`EPtext` | `—`); `ceW` (`−1` | `2` | `1` | `√5`).
- Refusals: `a = 0`.
- Serves: 7.3, 7.4, 7.5, 7.6, 7.7, 7.8.

#### oscillator (`os`)
- Purpose: `m·x″ + c·x′ + k·x = F₀·cos(ωt)`: every exact quantity of the free, damped and forced oscillator.
- cfg: `presets[{id, label, m, c, k, ic: [x0, v0], F0: rational (0 for free), w: rational}]`, `view` (`motion | phase | amplitude`).
- Controls: `osPreset`; `osM`, `osC`, `osK` (text); `osIC` (text); `osF0`, `osW` (text); `osView` (redraw-only).
- Computation: `ω₀² = k/m`; `ω₀` surd; period `2π/ω₀` (`π` when `ω₀ = 2`; `2π/√5` with `≈`); disc `c² − 4mk` and the class; `c_crit = 2√(mk)` surd; free amplitude `A² = x0² + v0²/ω₀²` exact, `A` surd/`≈`, phase `atan2(v0/ω₀, x0)` rounded; `ω_d² = k/m − c²/(4m²)`, envelope rate `c/(2m)`, peak ratio `e^(−c·T_d/(2m))` rounded (underdamped); critical: `C₁ = x0`, `C₂ = v0 − r·x0`, zero at `−C₁/C₂` if positive; forced undamped: `A = F0/(m(ω₀² − ω²))` or `resonance: (F0/(2mω₀))·t·sin(ω₀t)` when `ω² = ω₀²` (with `ω₀` surd text if needed), beat period `2π/|ω₀ − ω|` when `ω₀` is rational; forced damped: `A² = F0²/((k − mω²)² + (cω)²)`, `ω_r² = k/m − c²/(2m²)` (or `none` when ≤ 0), `A_max²` at `ω_r`; energy `E₀ = m·v0²/2 + k·x0²/2`. Stage: `motion` → `x(t)` from the exact solution (EP, drawn by evaluation) with the envelope; `phase` → the `x`–`v` curve; `amplitude` → `A(ω)` drawn with `ω_r` marked.
- Tiles: `osType` (`undamped` | `underdamped` | `critically damped` | `overdamped`); `osDisc` (fraction); `osOmega0Sq` (`4`); `osOmega0` (`2` | `√10/2 ≈ 1.58114`); `osPeriod` (`π ≈ 3.14159` | `2π/√5 ≈ 2.80993` | `4π ≈ 12.5664` for the beat period in the `beats` case — the tile label reads "period, or beat period when forced"); `osAmpSq` (`25`); `osAmp` (`5` | `√5/2 ≈ 1.11803`); `osPhase` (`≈ 0.927295` | `0`); `osCcrit` (`4` | `2√6 ≈ 4.89898`); `osOmegaD` (`ω_d² = 4` | `—`); `osEnvelope` (`c/(2m) = 1; peaks shrink by ≈ 0.0432139` | `—`); `osForced` (`A = 1` | `A = −3/5` | `resonance: (3/4)·t·sin(2t)` | `A² = 9/20` when damped | `—` when `F0 = 0`); `osResonant` (`ω_r² = 3; A_max = 3/4` | `none` | `—`); `osEnergy` (`50`).
- Refusals: `m ≤ 0`, `k ≤ 0`, `c < 0`, `ω ≤ 0` with `F0 ≠ 0`.
- Serves: 8.1–8.9.

#### phase (`pp`)
- Purpose: `x′ = A·x` in the plane: trace, determinant, eigen-data, type, exact Euler, closed-form curves.
- cfg: `presets[{id, label, A: [[a, b], [c, d]], start: [x0, y0], h, n}]`, `view` (`field | exact | solution`).
- Controls: `ppPreset`; `ppA` (text `a b; c d`); `ppStart`, `ppH` (text); `ppN` (range 1–64); `ppView` (redraw-only).
- Computation: `τ, Δ, disc`; `quadroots(1, −τ, Δ)`; eigenvectors for rational `λ` as integer vectors in lowest terms with the first nonzero entry positive (`(1, −1)`), `—` otherwise; type as in the tile vocabulary; general solution text for rational real, double (`(C₁ + C₂t)e^(λt)` plus the eigen/generalised vector), complex with rational `α, β`; constants from the start (exact under the same conditions as `char`); exact Euler `(xₙ, yₙ)` and `ppRatio = (xₙ² + yₙ²)/(xₙ₋₁² + yₙ₋₁²)` at the last step (exact; constant `1 + h²` for the rotation matrix). Stage: `field` → arrows plus eigenlines; `exact` → the exact Euler polygon with the true circle/curve behind it (drawn from the closed form); `solution` → closed-form curves from several starts (drawn by evaluation).
- Tiles: `ppTrace`, `ppDet`, `ppDisc` (fractions); `ppEig` (`−2, −1` | `−1 ± 2i` | `±2i` | `(1 ± √5)/2` | `−1 (repeated)`); `ppType` (`saddle` | `stable node` | `unstable node` | `stable spiral` | `unstable spiral` | `centre` | `degenerate node` | `star node` | `non-isolated equilibria`); `ppVectors` (`(1, −1), (1, 1)` | `—`); `ppGeneral` (text | `—`); `ppC` (`C₁ = 1/2, C₂ = 1/2` | `—`); `ppRatio` (`17/16`); `ppLast` (`(125/64, 27/64)`).
- Serves: 7.9, 7.10, 9.1–9.5.

#### jacobian (`jb`)
- Purpose: a polynomial system `x′ = f, y′ = g`: equilibrium checks, Jacobians, local types, a bounded exact search.
- cfg: `presets[{id, label, f: str, g: str, vars: ["x", "y"] | ["S", "I"], points: [[x, y]…], start: [x0, y0] | null, window, extra: "sir" | null}]`, `view` (`field | linearised | trajectory`), `search` (`off | grid`).
- Controls: `jbPreset`; `jbF`, `jbG`; `jbPoints` (text `0 0; 1 1`); `jbAt` (redraw-only select over the listed points, options rebuilt by `jbPoints`' handler, reset to the first by the preset handler); `jbSearch` (redraw-only); `jbView` (redraw-only).
- Computation: `f, g` exact at each listed point (`is an equilibrium` | `f = 0, g = −2: not an equilibrium`); Jacobian `[[f_x, f_y], [g_x, g_y]]` at the selected point exactly; `τ, Δ, disc`, eigenvalues, type as in `phase` with the addition `centre (linearisation inconclusive)` when `τ = 0, Δ > 0` and `non-isolated equilibria` when `Δ = 0`; `grid` search: every `(p/q, r/q)` with `|p|, |r| ≤ 12`, `q ∈ {1, 2, 3, 4}`, exact test, hits listed (`found 2: (0, 0), (1, 1)`), with the banner stating the search bounds; `extra: "sir"`: with `f = −βSI`, `g = βSI − γI`, read `β, γ` off the coefficients and print `R₀ = β·S₀/γ; I peaks at S = γ/β` from the start. Stage: `field` → arrows and the listed points; `linearised` → the phase portrait of `J` about the selected point (closed-form curves, drawn); `trajectory` → `DE_rk4float` from `start` (labelled) and the exact Euler first steps to the budget.
- Tiles: `jbCheck` (`is an equilibrium` | `f = 0, g = −2: not an equilibrium`); `jbJ` (`−2 1; 1 −1`); `jbTrace`, `jbDet` (fractions); `jbEig` (as `ppEig`); `jbType` (as `ppType` plus `centre (linearisation inconclusive)`); `jbFound` (`found 2: (0, 0), (1, 1)` | `—` when off); `jbExtra` (`R₀ = 9/5; I peaks at S = 1/2` | `—`).
- Refusals: not polynomial; degree > 3; more than 6 points.
- Serves: 9.6–9.10.

#### laplace (`lp`)
- Purpose: the transform as an exact rational function; derivative rule; IVPs by algebra; partial fractions; switched forcing.
- cfg: `presets[{id, label, kind: table | derivative | solve | partial | step, f: str (EP, for table/derivative), equation: str (for solve/step), ic: [y0] | [y0, v0], F: str (a rational function in s, for partial)}]`.
- Controls: `lpPreset`; `lpKind` (redraw-only, set by the preset); `lpF` (text, EP grammar; for `partial` a rational function in `s`; for `step` the forcing may contain `u(t - c)` factors with rational `c`); `lpEq` (text, `solve`/`step`); `lpIC` (text). Inputs not used by the kind are shown disabled, never hidden, so the hostile sweep reaches them and they must survive it.
- Computation: table — `EPlaplace`, printed in lowest terms; derivative — `EPlaplace(EPderiv(f))` against `s·F − f(0)` (`EPevalExact` at 0), `equal | differ`; solve — `(a·s² + b·s + c)·Y = a·(s·y0 + v0) + b·y0 + ℒ[rhs]` (first order: `(s + a)Y = y0 + ℒ[rhs]`), `Y` as an RF, `RFpartial`, `EPfromPartial`, the EP solution, and the residual of that solution in the original equation (`residual 0`); poles = roots of the denominator (`quadroots` for degree 2, `Prationalroots` for the forcing's part); partial — `RFpartial` and the inverse; step — the forcing's `u(t − c)` factors carry `e^(−cs)` tags: `Y` is a list of `(c, RF)` pieces, each inverted and shifted, printed as `0 for t < 2; 1 − e^(−(t − 2)) for t ≥ 2`.
- Tiles: `lpF` (`1/(s − 2)` | `(s + 1)/((s + 1)² + 4)`); `lpPoles` (`−2, −1` | `−1 ± 2i` | `—`); `lpY` (`(s + 3)/((s + 1)(s + 2))` | `e^(−2s)/(s(s + 1))`); `lpPartial` (`2/(s + 1) − 1/(s + 2)`); `lpSolution` (`2·e^(−t) − e^(−2t)` | `0 for t < 2; 1 − e^(−(t − 2)) for t ≥ 2`); `lpCheck` (`residual 0` | `—`); `lpEqual` (`equal` | `differ` | `—`).
- Refusals: a candidate outside EP; `β²` not a perfect square in an irreducible quadratic factor (the banner prints the factor and says the solution has an irrational frequency this lab does not print); a denominator with an irreducible cubic or higher; a step shift `c ≤ 0`.
- Serves: 10.1–10.8.

### D.4 Existing JavaScript reused, kits considered and not reused

Reused as blocks (never as whole kits): `algebra_core.RATIONAL_JS` (`R`,
`Radd`, `Rmul`, `Rcmp`, `Rtext`, `Rdec`, `Rparse`, `Rsqrt`), `POLY_JS`
(`Padd`, `Pmul`, `Pderiv`, `Pdivmod`, `Pgcd`, `Peval`, `Ptext`,
`Prationalroots`, `Pfactor`), `EXPR_JS` (`Eparse`, `Eeval`, `Epoly`),
`PLOT_JS` (`Plot`, `NumberLine`, `svgel`), `SURD_JS` (`Rsurd`, `quadroots`).
`algebra_core` is frontier-tier shared code and is NOT edited; `de_core`
adds what the Subject needs beside it.

Kits looked at and not used, and why: `sequence` (its `define` mode runs a
recursion, which Euler is, but takes `aₙ₋₁` not `f(t, y)`, and the page would
carry the whole 260 KB systems kit); `expo` (its `e` mode builds `(1 + 1/n)ⁿ`,
which “Exponential Growth” cites by title instead of shipping the kit);
`quadratic` (its `formula` mode solves `ar² + br + c` but draws a parabola;
`char` reuses `quadroots` and draws the solution curve); `grapher`
(`transform`/`funcops` draw functions from a stored list of modes; `verify`
draws the one candidate); `realline` (a number line for inequalities;
`autonomous` uses `NumberLine` directly); `markov`, `simulate`, `seqkit`
(nothing in common beyond `RATIONAL_JS`). `matrix` (Algebra's `det`/`inverse`
modes) was considered for the Jacobian and rejected: a 2×2 trace and
determinant are two subtractions and the page weight of `algebra_systems.py`
is the largest in the repository.

### D.5 Listen: the speech changes the kits and courses need

Every notation the courses use was run through `speech.say` on 2026-10-10
(the full list is in §F); most reads correctly today, and the courses are
written to the readings that work. Four changes to `scripts/mathpath/speech.py`
(chrome-renderer tier, one commit, before the first content lands), each
checked against every other Subject's content by grep:

1. **`SYMBOLS`**: `"‴": "triple prime"` (unspoken today; used only in prose
   about order), `"ℒ": "the Laplace transform of"` (absent today; no content
   uses it). `ℒ[f]` then reads "the Laplace transform of f" because `[` after
   a non-word says nothing and `]` is silent; `ℒ[y′] = s·Y(s) − y(0)` reads
   "the Laplace transform of y prime equals s times Y of s minus y of 0" once
   change 3 is in. Authors write `ℒ[…]` with square brackets, never `ℒ{…}`
   (braces read "the set").
2. **`FUNCTIONS`**: `"tr": "the trace"`, so `tr(J)` reads "the trace of J".
   No math run in any Subject contains the token `tr` today.
3. **A call rule for `t`-rooted and numeric arguments.** `y(0)`, `y(t)`,
   `x(t)`, `y(tₙ)`, `y(t + h)`, `p(t)`, `q(t)`, `u(t − c)` are the Subject's
   everyday notation and today read "y times 0", "y times t" (`y`, `x` are in
   `SINGLE_LETTER_PRODUCTS`) or are flagged ambiguous (`p`, `q`, `u` are not
   in `_FUNCTION_LETTERS`). Add `_time_call(tokens, i)`: true when the letter
   token at `i` is immediately followed by `(`, is not preceded by `_` or
   `^`, and the bracket's content either (a) begins with the word `t`
   (optionally subscripted, optionally followed by an operator and more) and
   does not contain the calling letter as a standalone word, or (b) is exactly
   one `num` token, or `num / num`, optionally with a leading minus. Use it in
   two places: in `_say`, the branch `elif call and tok in
   SINGLE_LETTER_PRODUCTS …` gets `and not _time_call(tokens, i)` so the
   letter reads as a call ("y of 0"); in `_settled_call`, return true when the
   match satisfies the same test so `ambiguous()` stops flagging it. Blast
   radius, enumerated by grep over every `` `…` `` run in `content/`: runs
   whose lowercase letter touches `(t` are `g(t) = 2t + 1`, `f(t)`,
   `(t, f(t))` (function letters, unchanged), `p(t − r) = q(t + s)` (a
   product; it has a spoken form in `content/spoken/algebra.py`, which wins,
   so unchanged), `t(the rest)` (first word `the`, not `t`, unchanged),
   `w_a(t + p_a)` (preceded by `_`, unchanged); runs whose letter touches `(`
   and a digit are `f(1)`, `f(2)`, `g(f(3))`, `log_c(1)`, `log_x(16)` (function
   letters or preceded by `_`, unchanged), `n(1 + 1/2 + ⋯ + 1/n)` and
   `n(2n−1)(2n+1)/3` (contain `n` and an operator, unchanged), `p^k(1−p)` (`k`
   is preceded by `^` and the argument has an operator, unchanged),
   `a(1 − qx₀)` (operator, unchanged), `x(1) = 0`, `x(2) = 5` (OR; spoken forms
   present and winning, unchanged). Nothing else changes.
4. **`∫` with limits, and the differential.** `∫ₐᵇ f(t) dt` reads today "the
   integral of sub A to the power b f of t dt". Add: when `∫` is immediately
   followed by a `sub` token (and optionally a `sup` token), say "the integral
   from ⟨sub⟩ to ⟨sup⟩ of" and skip those tokens; and when a run contains `∫`,
   a trailing `word` token of the form `d` + one letter (`dt`, `dx`, `ds`,
   `dy`) reads "d t". The only existing run with `∫` is Operations Research's
   `(1/T)∫N(t) dt`, which changes from "… N of t dt" to "… N of t d t", an
   improvement; no spoken form pins it.

Not changed, and the convention that avoids the change: `dy/dt` reads "d y
over d t" and `d²y/dt²` "d squared y over d t squared", which are standard, so
they stay. `lim` is not written anywhere on the path (write `Q → 2 as h → 0`,
which reads "Q goes to 2 as h goes to 0"); `ẏ`, `ẍ` are never written (primes
only); matrices are `math` blocks, one row per line, never `[[a, b], [c, d]]`
in prose; `μ(t)` is written `μ` (a Greek letter touching a bracket reads as a
call but is flagged); `y(b) − y(a)` is written `F(b) − F(a)`; products are
written with `·` (`r·y·(1 − y/K)`, `m·x″ + c·x′ + k·x`); `cos(2t)` with the
bracket, never `cos 2t` beside a coefficient. Runs that still read wrongly get
a line in `content/spoken/differential_equations.py`, which starts empty.

---
## §E Package layout and the author's checklist

```
content/differential_equations/
  __init__.py                 PATH, COURSES (filter COURSE = None), numbering loop
  c1_rates/__init__.py        COURSE dict; lessons = part_a.LESSONS + part_b.LESSONS
  c1_rates/part_a.py          LESSONS = [...]   lessons 1–6
  c1_rates/part_b.py          LESSONS = [...]   lessons 7–11
  c2_accumulation/ … c10_laplace/   same shape; split a course at its midpoint
                              (8 → 4 + 4, 9 → 5 + 4, 10 → 5 + 5, 11 → 6 + 5)
content/spoken/differential_equations.py  SPOKEN = {run: words}   starts empty
scripts/mathpath/labs/de_core.py          the shared blocks of §D.1
scripts/mathpath/labs/calckit.py          calckit_lab
scripts/mathpath/labs/dekit.py            dekit_lab
tests/test_calckit.py, tests/test_dekit.py  every §C (mode, cfg) built through
                              labs.build, presets reach the menu and the
                              expectation table, refusals raise — the shape of
                              tests/test_argkit.py
```

Mirror `content/operations_research/__init__.py` exactly for the package
`__init__`, and `content/philosophy/c1_arguments/__init__.py` for a course
`__init__`. A course not yet written exports `COURSE = None`.

**Course fields** (all required; `assumes_short` is consumed nowhere but every
existing course carries it — carry it): `slug`, `title`, `level`, `summary`,
`blurb`, `key` (4–8 lines, each ≤ 46 characters, no second column),
`assumes_short`, `assumes_long` (lowercase start, no trailing period, names
courses by TITLE), `outcomes_intro`, `outcomes` (4–6 pairs), `syllabus_intro`,
`how_to` (3–4 paragraphs), `not_covered` (3–6 paragraphs; the honest list from
§G for that course), `footer_lead`, `lessons`.

**Lesson fields** — every one required; the renderer uses `.get` for some but
`TestLessonDataMatchesTheRenderer` reads them directly:

| field | shape | enforced |
| --- | --- | --- |
| `slug` | lowercase, hyphens, ≤ 48 chars, unique in the course, as in `COURSES.json` | URL space |
| `title` | plain text, no backticks, no entities (`′` and `–` are characters, fine) | `test_fields_that_reach_metadata_stay_plain`, `test_escaped_fields_carry_no_html` |
| `module` | plain text, one of the course's module names in §C | same |
| `one_line` | one sentence, no entities/tags | escaped |
| `summary` | 2–4 sentences, prose (entities and `x` runs allowed) | metadata via `plain()` |
| `key` | 3–8 lines, each ≤ 46 chars, no entities, no second column | range (3, 8) |
| `key_label` | plain | escaped |
| `concepts_intro` | prose | — |
| `concepts` | EXACTLY 3 `(title, body)`; titles plain | exact |
| `read_title`, `read_intro` | plain / prose | escaped / — |
| `body` | 7–18 blocks of kinds `p h3 math ul ol def thm example proof`; `h3` and `math` lines plain | range (7, 18) |
| `lab` | `(key, cfg)`; cfg per §D; `cfg["mode"]` as in `COURSES.json` | `TestEveryLabBuilds`, labcheck |
| `steps_title`, `steps_intro` | plain / prose | escaped |
| `steps` | 4–5 `(title, body)` | range (4, 5) |
| `worked` | `{title (plain), intro: [prose], lines: [plain, ≤ 60 chars], after: [prose]}` | escaped |
| `quiz_title` | plain | escaped |
| `quiz` | 3–4 items `{q, a: [exactly 4 distinct], c: index, why}`; one defensible answer | `test_every_quiz_question_is_answerable` |
| `mistakes` | EXACTLY 3 `(title, body)`; the first is the §C misconception | exact |
| `standard` | `(head plain, body prose)` | escaped |
| `note` | prose | — |

Prose fields may use `&mdash;`, `&ldquo;`, `<strong>`, `<em>` and the `x`
math shorthand. Escaped fields take real characters (—, “ ”) and no shorthand.
`thm` blocks state the claims this Subject demonstrates and does not prove
(the limit of the quotients, the fundamental theorem, `sin′ = cos`, existence
and uniqueness); a `proof` block follows a `thm` only where the proof is
algebra the reader has (the product rule on polynomials, `(1 + h²)` per Euler
step on the oscillator). A `thm` without a `proof` is followed by a `p` that
says what the lab demonstrates and what it does not.

**Per-lesson procedure.**

1. Write the dict from the §C entry. The §C misconception is `mistakes[0]`.
2. Write the presets with `expect` left as `{}`. Type right-hand sides and
   candidates in the ASCII grammar of §D; write them in prose in the library's
   notation.
3. `python3 scripts/build_paths.py` (Differential Equations must already be
   in `GENERATED_PATHS` on the branch — §H).
4. `node scripts/labcheck.js --observe site/<course>/<lesson>/index.html`;
   copy the tile strings the preset exists to show into `expect`; rebuild. If
   a figure disagrees with the §C "Worked" line, stop and report; do not copy
   either.
5. `node scripts/labcheck.js site/<course>/<lesson>/index.html` and
   `/usr/bin/python3 scripts/speechcheck.py`; fix any unspoken or ambiguous
   run by rewriting to the §F conventions first, and with a line in
   `content/spoken/differential_equations.py` only when the notation must
   stay.
6. Check every quiz distractor by trying to argue for it; if you can,
   rewrite. The distractor that recurs in this Subject is the one that is
   true at one value of `t` or for one step size.
7. Read the page aloud in your head: every `x` run must read as a sentence.
   `y(0) = 1` must say "y of 0 equals 1"; if it says "times", the speech
   change in §D.5 has not landed and you stop.
8. Every tile that prints a rounded figure is introduced in the prose with
   the word "rounded" or the `≈` sign at least once; a lesson that quotes a
   rounded value as if exact (`e = 2.718`) is a defect.

---

## §F Voice and style

This library is written in careful prose by someone who has thought about the
thing and is telling you what they found. Not a textbook, not a lecture, not a
chat. The rules that follow are what that sounds like, and the ones specific
to this Subject come first.

- **Say which tier a number is in, in the sentence that reports it.** "The lab
  prints `625/256`, which is `(5/4)⁴` exactly, beside `e ≈ 2.71828`, which is
  rounded" — never "the lab shows the answer is about 2.44".
- **A claim is stated as a claim.** "The quotients approach 2" is what the
  table suggests and the lesson asserts; it is not what the table proves. Say
  so once per lesson where it matters, plainly, and move on.
- **The method is not the solution.** Euler's polygon, the improved step,
  RK4: each is described as what it is, a recipe whose output is a column of
  exact numbers that are near the solution for reasons the error lessons
  measure. The material clause in every footer says this; the lessons do not
  contradict it by calling `yₙ` "the solution at `tₙ`".
- **Name the act, not the understanding.** Objectives, `standard` heads and
  outcome titles are verbs the closing check can measure: compute, verify,
  classify, fit, read off, locate, bound. "Understand" is a defect.
- **One hard idea per lesson.** Everything else in the lesson serves it. If a
  second hard idea appears, it is the next lesson's.
- **The misconception is named as a model someone holds**, then corrected
  with the specific fraction, residual or step that refutes it. "A common
  error is…" without the refutation is a defect.
- **The lab's limit is stated in the lesson that leans on it.** The digit
  budget in “Blow-Up and the Interval of Existence”; the refusal to fit surd
  constants in “Fitting the Initial Conditions”; the five-point check for a
  transcendental candidate in a nonlinear equation; the drawn (not computed)
  trajectory in “Predator and Prey”. Say so where it matters, once.
- **Cross-references by title, never by number.** “Euler's Method” for a
  lesson, Accumulation and the Integral for a course, “The Quadratic Formula”
  in Algebra's Quadratics and Complex Numbers for another Subject. Relative
  prose ("the next course", "earlier in this course") is fine.
- **Math a voice can read.** The notation list below is the whole of what the
  courses use, with the reading `speech.say` gives after §D.5:
  `dy/dt` "d y over d t"; `d²y/dt²` "d squared y over d t squared"; `y′`, `y″`
  "y prime", "y double prime"; `y(0) = 1` "y of 0 equals 1"; `y(t)` "y of t";
  `f(t, y)` "f of t and y"; `Δy/Δt` "delta y over delta t"; `h → 0` "h goes
  to 0"; `∫ₐᵇ f(t) dt` "the integral from A to b of f of t d t"; `e^(kt)` "e
  to the power k t"; `e^(−2t)` "e to the power the quantity negative 2 t";
  `C₁·e^(r₁t)` "C sub 1 times e to the power r sub 1 t"; `cos(2t)` "cosine of
  2 t"; `ω₀` "omega sub 0"; `λ² − τ·λ + Δ = 0` "lambda squared minus tau times
  lambda plus delta equals 0"; `tr(J)`, `det(J)` "the trace of J", "the
  determinant of J"; `ℒ[y′] = s·Y(s) − y(0)` "the Laplace transform of y prime
  equals s times Y of s minus y of 0"; `(1 ± √5)/2` "the quantity 1 plus or
  minus the square root of 5, over 2"; `−1 ± 2i` "negative 1 plus or minus 2
  i"; `yₙ₊₁ = yₙ + h·f(tₙ, yₙ)` "y sub n plus 1 equals y sub n plus h times f
  of t sub n and y sub n"; `≈ 0.693147` "is approximately 0.693147". Write
  products with `·`; `cos(βt)` with brackets; `ℒ[…]` with square brackets;
  `F(b) − F(a)` for an antiderivative's values; `μ` without an argument;
  arrows, never `lim`; primes, never dots; matrices in `math` blocks.
- **Quiz questions test the idea, not the vocabulary**, and every wrong
  choice gets the reason it is wrong in `why`.
- **No filler.** No "In this lesson we will", no "Let's", no exclamation
  marks, no rhetorical questions in a row, no emoji. British or American
  spelling as the author pleases but consistent within a course.

**One exemplary paragraph** (a `p` block for “Euler's Method”):

> Euler's method is the sentence "the next value is this value plus the rate
> times the step", written as `yₙ₊₁ = yₙ + h·f(tₙ, yₙ)` and applied over and
> over. On `y′ = y` from `y(0) = 1` with `h = 1/4` the first step is
> `1 + (1/4)·1 = 5/4`, the second `5/4 + (1/4)·(5/4) = 25/16`, and after four
> steps the lab prints `625/256`, which is `(5/4)⁴` exactly and about `2.44`.
> The true value at `t = 1` is `e ≈ 2.71828`, so the column of exact fractions
> is a little more than a quarter short &mdash; not because any step was
> computed wrongly, but because every step assumed the rate stayed at its
> starting value while the real rate was climbing. That is the whole of what
> Euler's method does, and the whole of what is wrong with it; the next lesson
> measures how wrong, and the one after that fixes half of it.

---

## §G What is left out, and why

Stated here so every course's `not_covered` can draw on it, and so no author
invents a decorative lab to fill a gap.

- **Limits as a theory.** No ε–δ, no limit laws, no continuity as a defined
  property. The derivative is what exact quotients approach, demonstrated, and
  for polynomials read off exactly; the integral likewise. A reader who wants
  the theory is told, in Rates of Change and the Derivative's `not_covered`,
  that this is where a first analysis course begins.
- **Differentiation and integration of general functions.** The quotient
  rule, implicit differentiation, inverse trigonometric functions,
  integration by parts, trigonometric substitution, partial-fraction
  integration of rational functions in `t`. The Subject uses the power,
  product and chain rules on polynomials exactly, states `(e^(kt))′`,
  `sin′`, `cos′` and `∫ dt/t` as demonstrated claims, and needs nothing else.
- **Existence and uniqueness proofs.** The Picard–Lindelöf theorem is stated
  in words in “Blow-Up and the Interval of Existence” (a continuous `f` with a
  continuous `∂f/∂y` near the start gives exactly one solution through it);
  the proof, Lipschitz conditions and Peano's example are not here.
- **Exact equations and integrating factors for non-linear equations,
  Bernoulli and Riccati equations, homogeneous-degree substitutions.** They
  are techniques for finding closed forms that the Subject's classes cannot
  verify exactly, and the Subject is built around exact verification.
- **Series solutions, special functions, Frobenius, Bessel, Legendre.** No
  power series on this path; Algebra's Sequences and Series says the same.
- **Variable-coefficient second-order equations beyond `p = a/t` in first
  order**: Euler–Cauchy equations, reduction of order in general, variation of
  parameters. Undetermined coefficients covers every forcing the Subject
  uses; variation of parameters is named in Second-Order Linear Equations'
  `not_covered` as the general tool.
- **Higher-order equations and `n × n` systems.** Everything is first- or
  second-order, or a 2×2 system. The trace–determinant classification is the
  reason: it is complete for the plane and nothing like it exists in three
  dimensions.
- **Numerical analysis as a subject.** Adaptive step size, error estimators,
  multistep methods, implicit Runge–Kutta, the theory of A-stability. The
  Subject shows order of accuracy by exact ratios and stiffness by one exact
  factor, and stops.
- **Floating-point stepping as a computed result.** Trajectories without a
  closed form are DRAWN by floating-point RK4 and labelled as drawings;
  nothing in a tile comes from them. A reader who wants a nonlinear orbit's
  numbers is told the honest truth: exact stepping of a quadratic right-hand
  side reaches the digit budget in about eleven steps, and floating point
  hides that by rounding at every step.
- **Partial differential equations**, Fourier series, separation of variables
  for the heat and wave equations, boundary-value problems, Sturm–Liouville
  theory. A different Subject, with different machinery.
- **Chaos, the Lorenz system, Poincaré–Bendixson, limit cycles, Hopf
  bifurcations.** The phase-plane course classifies linearisations and draws
  nonlinear trajectories; it does not prove the existence of a cycle (the
  predator–prey lesson states the conserved quantity and shows the drawing).
- **Laplace transforms beyond the rational-function case.** The Dirac delta
  (needs distributions), convolution and the convolution theorem, transforms
  of periodic functions, the inversion integral, the region of convergence as
  theory. Irrational frequencies in an irreducible quadratic factor are
  refused with the factor named rather than printed with a surd inside a
  cosine.
- **Delay, stochastic and difference equations**, except that Euler's
  recursion is named as the difference equation it is and the Algebra path's
  Sequences and Series is cited for geometric sequences.
- **Modelling as a skill.** Each application (cooling, mixing, loans,
  circuits, predator–prey, SIR) is stated with its equation given and its
  assumptions named; deriving models from data, parameter fitting and
  validation are not here.

---

## §H Wiring notes for the orchestrator

Not an author's job; recorded so nobody asks.

- Register `differential_equations` in `scripts/build_paths.py`
  `GENERATED_PATHS` at the START of the branch, with every course
  `COURSE = None`, so authors can build and observe pages as they land.
  `tests/test_review_remediation.py` `content_errors` will demand
  `content_preservation.json` entries for every `.py` in the package from that
  moment; generate them with `/usr/bin/python3` via `content_fingerprint`
  imported from the test module, never re-derived.
- `speech.py` changes (§D.5) land FIRST, in one chrome-renderer commit with
  `tests/test_speech.py` cases pinning `y(0) = 1` → "y of 0 equals 1",
  `∫ₐᵇ f(t) dt` → "the integral from A to b of f of t d t", `ℒ[f]`, `tr(J)`,
  `y‴`, and the unchanged readings `n(n + 1)/2`, `p^k(1−p)^{n−k}`,
  `x(40 − x)`, `(1/T)∫N(t) dt` → "… N of t d t".
- `de_core.py`, `calckit.py`, `dekit.py` land next (lab-arithmetic tier), with
  `mathcheck.js` cases and `tests/test_calckit.py`, `tests/test_dekit.py`,
  before any course is authored. The kit engineer reads §D and §C together:
  every preset instance in §C must build, and the test files enumerate them.
- `tests/test_site_invariants.py`: `DE_DISCLAIMER_RE`, the path page constant
  `DE_PATH_PAGE` and its entry in `PATH_MATERIAL_DISCLAIMER`, course home
  constants, the slug tuples, `TestLessonDataMatchesTheRenderer.setUpClass`
  and `TestEveryLabBuilds.setUpClass` import lists (they import four paths
  today; add this one), `REQUIRED_PAGES`.
- `test_public_copy`'s `differential_equations_semantic_copy` block, derived
  from RENDERED text.
- The two dozen declaration sites in `AGENTS.md` §0, with the check-id prefix
  `de`. The longest check id is 64 characters.
- `KITS_WITH_EXPECTATIONS`: add `"calckit", "dekit"` only after every preset
  on the branch carries `expect` (rule 7).
- `site/index.html`: a subject card and one entry per course in the inline
  search array (text nodes — no entities). `site/progress/index.html` and the
  OAuth callback page: re-run `scripts/build_auth_pages.py`.
- Page weight re-measured and the table in `AGENTS.md` updated; the `laplace`
  pages are the ones to measure first (§D.0).
- `AGENTS.md` §0 and §1 counts: nine Subjects, 78 courses, 864 lessons, 956
  pages; `README.md`'s URL layout; the `docs/FUTURE-SUBJECTS.md` "fields"
  entry gains one sentence saying the library now teaches calculus in this
  Subject and that a fields Subject could assume it.
- `docs/differential-equations/COURSES.json` is the fan-out manifest for
  authors; it and §C were generated from one table
  (`de_table.py`, kept with the orchestrator's scratch) and a script checked
  that every slug in §C appears in it and vice versa before this document was
  handed over. Re-run that check after any retitling.
