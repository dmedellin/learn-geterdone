# Pedagogy assessment — Differential Equations and Euler's Method (differential equations, course 3)

Formed from the ten lesson dicts in `content/differential_equations/c3_euler/`
(`part_a.py`, lessons 1–5, and `part_b.py`, lessons 6–10, written by two
authors from `docs/differential-equations/PLAN.md` §C), the course dict in
`__init__.py`, the spoken forms in
`content/spoken/differential_equations_c3_euler.py`, and the pages as
`scripts/preview_subject.py` renders them, with every preset's tiles read off
the built page by `labcheck.js --observe` and every `data-say` attribute read
off the rendered HTML. The course may assume Rates of Change and the
Derivative, Accumulation and the Integral, and the Algebra Subject, and
nothing else. All ten lessons were read before any was changed; every figure
the prose quotes was recomputed independently in exact rational arithmetic
(`fractions.Fraction`) before the kit's tiles were compared with it. The last
two sections record what was changed and what was not.

Lessons, in course order: `what-a-differential-equation-is`,
`checking-a-proposed-solution`, `initial-value-problems`, `slope-fields`,
`reading-a-slope-field` | `eulers-method`, `eulers-error-and-the-step-size`,
`the-improved-euler-method`, `runge-kutta-four-slopes-per-step`,
`blow-up-and-the-interval-of-existence`. The bar marks the seam between the
two authors.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.** Name
  the order and decide a candidate from its residual
  (`what-a-differential-equation-is`); substitute two derivatives, collect like
  terms, classify as linear or not (`checking-a-proposed-solution`); fix a
  constant and say how many values an equation needs
  (`initial-value-problems`); compute a slope exactly, draw it, solve for the
  nullcline (`slope-fields`); list what a field settles and what it only
  suggests (`reading-a-slope-field`); take three Euler steps as fractions and
  say what each assumes (`eulers-method`); measure three errors, form two
  ratios, read the order (`eulers-error-and-the-step-size`); take an improved
  step and show the error quarters (`the-improved-euler-method`); write the
  four slopes and weights and read the ratio 16
  (`runge-kutta-four-slopes-per-step`); show a solution ends, step past it,
  read the digit budget (`blow-up-and-the-interval-of-existence`). None is
  "understand".
- **The figures are right, and the prose agrees with every tile.** All
  thirty-one presets across ten pages pin tiles that match the page
  (`labcheck`), and every figure quoted in prose was recomputed: the residuals
  `3t² − 2t`, `−2·eᵗ`, `−5t`, `−2/(1 − t)²`; `C = 4`, `C = −3`, `C = 2`,
  `C = 1, D = −2`; the slopes `2, 0, −2, 2` and the nullcline `y = t`;
  `(5/4)⁴ = 625/256` short of `e` by `≈ 0.276876` and `(9/8)⁸` short by
  `≈ 0.152497`; `19/16` against `1 + 3e^(−2) ≈ 1.40601`; the Euler errors
  `1/4, 1/8, 1/16` on `y′ = 2t` and `11/96, 23/384, 47/1536` on `y′ = t²`
  with ratios `44/23, 92/47` and order `≈ 0.968973`, which the lesson's own
  formula `h/2 − h²/6` reproduces; the trapezoid errors `1/96, 1/384, 1/1536`
  and `h²/6`; `53/2560, 213/40960, 853/655360` on `y′ = t⁴` with ratios
  `848/213, 3408/853`; `41/32` for one improved step on `y′ = y`; `5/24`,
  `1/120`, `h⁴/120`, `1/30720, 1/491520, 1/7864320` and the Euler comparison
  `19627/655360` at sixteen readings, 920 times larger; `5/4, 105/64,
  37905/16384`, the error `27631/16384`, `y₅` over `2⁶²`, denominators of
  `1, 2, 5, 10, 19, 38, 77, …` digits and the stop after step 11 at 1233
  digits with a numerator of 1257. Every one is as printed.
- **The exactness rule is kept throughout.** Every fraction is called the
  exact value of the method and never the solution; every irrational figure
  carries `≈` and the word "rounded" in the sentence that reports it
  (`eulers-method` on `e`, `eulers-error-and-the-step-size` on the `y′ = y`
  errors, `the-improved-euler-method` on `e^(1/4)`, `blow-up-and-the-interval-of-existence`
  on `≈ 2.31354`); the only bare decimal, `2.44`, is introduced by "about".
  The lab's limits are stated in the lessons that lean on them: the five-point
  floating check for a transcendental candidate in a nonlinear equation
  (`checking-a-proposed-solution`), the refusal to fit an exponential anywhere
  but `t = 0` and the dash when one value is given for two constants
  (`initial-value-problems`), the drawn (not computed) curve
  (`slope-fields`, `reading-a-slope-field`), the digit budget
  (`blow-up-and-the-interval-of-existence`).
- **Claims are stated as claims, each `thm` followed by what the lab shows.**
  First, second and fourth order, existence and uniqueness, and what linearity
  buys are each a `thm` block followed by a `p` saying the lab demonstrates
  the claim on chosen equations and does not prove it. The two places the
  ratio is exactly `2` or `4` are explained by the arithmetic (Euler on
  `y′ = 2t` is the left sum; the improved step on `y′ = t²` is the trapezoid
  rule, whose error on a quadratic or a cubic has no `h⁴` term), and the
  places it is not are named (`y′ = t²`, `y′ = t⁴`, `y′ = y`).
- **The misconceptions are the real ones and each is refuted with a figure.**
  A differential equation has a number for an answer (refuted by `t²`,
  `t² + 3`, `t² − 7`); a function that fits at one `t` is a solution (`5t` in
  `t·y′ = 2y`, zero at `t = 0` only); the initial value is where `t` starts
  (`t² + 4` lives on both sides of `t = 1`); a segment shows where the
  solution goes next (`(2, 0)` with slope 2 does not reach `(3, 2)`);
  Euler's method gives the solution and more steps make it exact (`625/256`,
  then `43046721/16777216`, closer and not there); the error is the last
  step's error (`1/16` against `1/4`); a second-order method has half the
  error (`1/96` against `11/96`); RK4 is four Euler steps (`1/30720` against
  `19627/655360`); a smooth right side gives a solution for all `t`
  (`1/(1 − t)` ends at `1`). Every `mistakes[0]` is the §C misconception.
- **The worked examples progress and the rehearsals fade the guidance.** Each
  lesson works one example in full, then hands the reader a variant to do
  alone with the answer stated once (`y(2) = 1` giving `C = −3`; the slope at
  `(3, 1)`; the start `y = 2` on the logistic field; `y′ = 2y` with `h = 1/2`;
  `h = 1/10` giving `1/10`; the single RK4 step on `y′ = t³` landing on `1/4`;
  the start `y(0) = 2` ending at `t = 1/2`). The panel intros then ask for a
  prediction before the tile is read, which is the right order.
- **The stepping half is unusually honest about cost.** `the-improved-euler-method`
  compares the two methods at equal numbers of slope readings (eight: `23/384`
  against `4/384`), and `runge-kutta-four-slopes-per-step` does the same at
  sixteen. Order is taught as a rate of fall and not as a size, which is the
  distinction readers most often lose.

## What the course teaches badly, or wrongly

1. **`reading-a-slope-field` proved the wrong thing at the place the course
   exists to teach.** The lesson's thesis is "say what the arithmetic settles
   and what the picture only suggests", and it put "a curve from `1/2` never
   reaches `y = 1`" in the settled tier with this argument: if the curve
   reached the line there would be two solutions through one point, "the
   horizontal one and this one, arriving with a positive slope", and the
   field has one slope per point. That is false as stated. A curve that
   reached `y = 1` would arrive with slope `f(t, 1) = 0`, the same slope as
   the line, so the one-slope argument forbids nothing. What forbids the
   touch is uniqueness — through a given point there is exactly one solution,
   and the horizontal line is already it — which is a theorem the course
   takes on trust (and which fails for non-Lipschitz right sides such as
   `y′ = −2√y`, where solutions do reach the equilibrium in finite time). The
   `thm` block half-knew this ("that two solutions cannot even touch without
   coinciding is the uniqueness statement") while the body, the worked
   example, quiz 2, quiz 3 and `mistakes[0]` all used the slope argument for
   the touch. The lesson now has three tiers: the arithmetic settles the
   horizontal solutions, the sign in each region and that curves never cross
   at an angle; the uniqueness claim, stated and used on trust and true for
   every polynomial right side, adds that they never touch, so a curve stays
   between two horizontal solutions; the picture suggests the limit. Concept
   two, the body paragraph, the `thm` and its follower, step three, the worked
   lines and `after`, both quiz questions and `mistakes[0]` were rewritten to
   say so. The PLAN §C "Worked" line uses the loose argument; the lesson now
   does the correct thing and this note reports the disagreement.
2. **`initial-value-problems` leaned on a fact the path has not taught.** Its
   second-order example fits `C·cos(t) + D·sin(t)` to `y″ + y = 0` and needs
   `sin′ = cos` and `cos′ = −sin`, which this Subject demonstrates only in
   “Sine, Cosine and Their Rates”, the first lesson of Second-Order Linear
   Equations, four courses on; the Algebra Subject has no trigonometry. PLAN
   §C prescribes the instance, so it stays, and two things were done. The
   lesson now says the two derivatives are taken on trust and names where they
   are demonstrated, and that the fit needs only `cos 0 = 1` and `sin 0 = 0`.
   And a second-order example the reader can check with what they have was
   added before it: `y″ − y′ − 2y = 0` with the family `C·e^(2t) + D·e^(−t)`,
   whose two exponentials `checking-a-proposed-solution` verified one lesson
   earlier, fitted to `y(0) = 1, y′(0) = −2` through the genuine `2 × 2`
   system `C + D = 1, 2C − D = −2` to `C = −1/3, D = 4/3`. It is also the
   better teaching example: the trigonometric pair's system is diagonal at
   `t = 0`, so a reader never sees why "two values give two equations"
   matters, and step three had been reduced to saying the system "solved as
   soon as the cosine and sine took their values". A fourth preset `two-exps`
   pins `C = −1/3, D = 4/3` and `satisfied`.
3. **`runge-kutta-four-slopes-per-step` misstated what exactness requires.**
   `mistakes[2]` said RK4 is exact "only on equations whose solution is a
   polynomial of degree three or less"; the lesson's own exact preset is
   `y′ = t³`, whose solution `t⁴/4` has degree four. The exactness comes from
   the right side being a polynomial in `t` of degree at most three (the step
   is then Simpson's rule), and the text now says so, adding that on `y′ = y`
   the error is never zero. Quiz 2's `why` said "a fourth-order method is
   exact on cubics only", which is the same error compressed; it now says
   fourth order is a rate, not a promise, with `h⁴/120` on `y′ = t⁴` as the
   example. Quiz 1's `why` said the distractor `(k₁ + 4k₂ + k₃)/6` "is
   Simpson's rule, which is what the formula reduces to when `k₂ = k₃`"; the
   formula reduces to `(k₁ + 4k₂ + k₄)/6`, and the distractor as written never
   reads the slope at the end of the step, which is now what the `why` says.
4. **One rounded figure did not match the tile the reader is sent to.** The
   Euler comparison quoted `19627/655360 ≈ 0.02995` and then said "switch the
   Method menu to Euler and read the third error"; the tile prints
   `≈ 0.0299484` by the stated six-figure rule. The prose now quotes the
   tile.
5. **Part B's worked lines were in the typed grammar, not the library's
   notation, and the speech engine misread them.** `3t^2 - 2t` reads "3 t
   squared negative 2 t", `(t + h)^2 - t^2` "the quantity t plus h, squared
   negative t squared", `y1` "y 1", `y''` "y prime prime"; the sibling
   courses (Accumulation and the Integral, Separable Equations) write
   `t²`, `−`, `y₁`, `y″` in their lines, so this was also a seam defect. Part
   A's lines had the same shapes in lessons 1–5. Every worked line in the
   course is now in the library's notation and reads as a sentence.
6. **Three lines were read as HTML tags and silently dropped from the
   spoken page.** `y < 0:      y < 0, 1 - y > 0  ->  slope < 0` and its two
   neighbours (`reading-a-slope-field`), the key line
   `0 < y < 1 rising;  y < 0 or y > 1 falling`, and
   `below the line y < t:  t - y > 0, rising` (`slope-fields`) each contain
   `<` … `>` in one line, which `speech.say` strips as markup: the first read
   aloud as "y, 0, to, slope is less than 0". Each is rewritten with words for
   the signs, or with only one of the two symbols, and the readings were
   confirmed on the rebuilt pages.
7. **`1/h` read as "1 per h", the arrow `->` as "to", and `≈ 6.77729e23` as
   "e 23".** The key line `one step errs h²;  1/h steps total h` is now
   `one step errs h²;  N steps total N·h² = h`, which is also the better
   statement; `halve h:  ratio E(h)/E(h/2) → 2` is in words; worked lines
   say `N steps with N·h = 1`; the arrows in `what-a-differential-equation-is`,
   `checking-a-proposed-solution` and `slope-fields` are "so"; the typed
   candidate `t^2 - 7` suggested in the first lesson's panel, read as "t
   squared negative 7", is now `t^2 + 5`; and the five prose runs that must
   keep `1/h`, plus the scientific-form figure, have spoken forms (`1 over
   h`; `6.77729 times 10 to the power 23`).
8. **The course home put a bare `≈` beside "to" and "and".** The renderer
   wrapped `≈ to` in the footer as "is approximately to six figures" on every
   page of the course, and `≈` alone in `how_to`. Both sentences now say
   "marked as approximate" / "printed as approximate" in words.
9. **Small prose faults.** "measured rather than hoped about" (`summary`);
   "the constants tile reads — and the banner says" with a literal dash for a
   dash the tile shows (`initial-value-problems`); cross-references by
   description where the plan asks for titles ("the course on accumulation",
   "the course on second-order equations", "a later course"), and a course
   title in the curly quotes reserved for lessons (“First-Order Linear
   Equations”) in `reading-a-slope-field`; `Runge-Kutta` with a hyphen in one
   panel intro against the en dash everywhere else; `assumes_long` claimed the
   left sum is "used from the first lesson", which it is not (it arrives in
   `eulers-method`); the definition of a linear equation in
   `checking-a-proposed-solution` omitted the forcing term, though the quiz's
   own correct answer `t·y′ + y = t²` has one.

## What it claims to teach but does not, and where a learner gets stuck

- **The no-touching rule is used from `reading-a-slope-field` on and proved
  nowhere**, which is right for this Subject (§G leaves Picard–Lindelöf out),
  but before the fix the lesson implied it had been proved by the one-slope
  arithmetic, so a careful reader who noticed that a curve meets `y = 1` flat
  would have concluded the course's argument was broken, and been right. It is
  now a named claim with a named home (`blow-up-and-the-interval-of-existence`),
  and that lesson's `thm` already states the condition correctly (continuous
  `f` and `∂f/∂y` near the start).
- **`checking-a-proposed-solution` carries two hard ideas.** The residual on
  harder equations (two derivatives, a coefficient in `t`) is the lesson; the
  linear/nonlinear classification and what linearity buys is a second idea
  that PLAN §C assigns to the same lesson, and the "five points only" limit of
  the lab is a third thing to hold. The lesson handles all three cleanly and
  within the body budget, and nothing was moved, but it is the heaviest lesson
  of part A; recorded under remaining issues.
- **`blow-up-and-the-interval-of-existence` carries three.** The interval of
  existence with the existence-and-uniqueness statement, Euler past the
  asymptote, and the digit budget as a fact about exact arithmetic. PLAN §C
  puts all three here and the lesson keeps them in that order with one `h3`
  each, which is the right shape; the quiz tests each once. It is the
  heaviest lesson of the course.

## Prerequisite order

Checked backwards across the path. `what-a-differential-equation-is` needs
the derivative of a polynomial and of a constant (“The Derivative as a
Function”) and the antiderivative with its constant (“The Constant of
Integration”), both earlier and the second now cited by course title.
`checking-a-proposed-solution` needs `(e^(kt))′ = k·e^(kt)`, which is “The
Exponential and Its Rate” together with “The Chain Rule” on `k·t`; the lesson
states the combined rule in one clause, which is enough. `initial-value-problems`
needed `sin′` and `cos′` from a course four ahead (item 2 above, now
declared) and uses a `2 × 2` linear system, now credited to Algebra's Systems
and Matrices. `slope-fields` needs only substitution into a polynomial.
`eulers-method` needs the left sum of “Total Change from a Rate” and the
geometric sequence of Algebra's Sequences and Series, both cited.
`eulers-error-and-the-step-size` and `the-improved-euler-method` need the
left-sum and trapezoid errors of “Refining the Partition” and “The Trapezoid
and Midpoint Rules”, whose figures `11/96, 23/384, 47/1536` and `1/96, 1/384`
they reuse exactly; the Euler–Maclaurin form `h²·(f′(b) − f′(a))/12` of the
trapezoid error is stated here, not derived, and is true for the composite
rule on any quadratic or cubic. `runge-kutta-four-slopes-per-step` names
Simpson's rule, which no earlier lesson teaches; the lesson defines it in the
sentence that uses it (`(f(start) + 4·f(middle) + f(end))/6`) and the worked
step shows it on `t⁴`, which is enough for a reader who has the trapezoid
rule. `blow-up-and-the-interval-of-existence` needs the chain rule on
`1/(1 − t)` and the residual test; both earlier. No violation sits in an
earlier course. Inside the course the order is right: what the object is,
then the picture, then the computation in order of cost, then the failure.

## Mathematical accuracy

- The residual test as "left side minus right side, simplified symbolically,
  zero for every `t`": right, and the kit does exactly that over rational
  functions and exponential polynomials, with the nonlinear-transcendental
  case honestly demoted to a five-point check.
- Linear defined as degree at most one jointly in `y, y′, y″` with
  coefficients in `t`: matches the kit's test and the standard definition
  once the forcing term is admitted (now).
- The nullcline of `y′ = t − y` as `y = t`, "none in `y`" for `y′ = 2t`, and
  horizontal solutions as common roots of every coefficient of `f` in `t`:
  right, and the kit's `sfEquil` prints `none` for `t − y` and
  `y = 0, y = 1` for the logistic field.
- Euler on `y′ = 2t` as the left sum with error exactly `h`, on `y′ = t²`
  with error exactly `h/2 − h²/6`: both verified by closed-form summation.
- The improved step on `y′ = f(t)` as the composite trapezoid rule, exact
  error `h²/6` on `t²` and `h²/4` on `t³`, `h²/3 − h⁴/30` on `t⁴` (the
  lesson says "a smaller term in `h⁴`", which is that term): verified.
- RK4 on `y′ = f(t)` as Simpson's rule, exact on cubics, error `h⁵/120` per
  step on `t⁴` and `h⁴/120` over the unit interval: verified; the Euler
  comparison `19627/655360` at `h = 1/16` is the left sum `Σ k⁴/16⁵`.
- `y₀/(1 − y₀·t)` solves `y′ = y²` and ends at `t = 1/y₀`: verified by
  differentiation. The denominators `2^(2ⁿ⁺¹ − 2)` with digit counts
  `1, 1, 2, 5, 10, 19, 38, 77, 154, 308, 616, 1233` and `2466` at step 12:
  verified; the lab stops after step 11, as the lesson says, and the tile's
  `(exact: 1257 digits over 1233)` matches the recomputed numerator.
- The existence-and-uniqueness statement (continuous `f` and `∂f/∂y` near
  the start give exactly one solution on some interval, with no statement of
  its length): correct as stated and correctly limited.

## The seam between part A and part B

The two authors agree on voice (careful prose, British spelling, no filler),
on the entity conventions in prose fields, on typographic quotes in the
`note` fields, and on the two-tier reporting of every figure. They differed
in two ways, both now closed: part B marked hand arithmetic as such ("this is
hand arithmetic from the formula") where part A had nothing to mark, which is
fine; and both parts wrote worked lines in the typed grammar where the
sibling courses write the library's notation (item 5 above, now uniform).
Part A's closing note hands over correctly ("segments end to end give a path,
and the question of how good a path is leads to a method"), and part B's
first paragraph is the PLAN §F exemplar nearly verbatim, so the altitude does
not change at the seam. `slope-fields`' `mistakes[0]` already names Euler's
method as "joining segments end to end", which is the right foreshadowing.

## Changes made

- `__init__.py`: "guessed at" for "hoped about"; `assumes_long` says where
  the constant and the left sum are each used; `how_to` and `footer_lead` say
  "approximate" in words instead of a bare `≈` beside "and" / "to".
- `what-a-differential-equation-is`: Accumulation and the Integral by title;
  worked lines in the library's notation with "so" for the arrows.
- `checking-a-proposed-solution`: the forcing term admitted in the
  definition of linear; the `thm`'s follower says the lab demonstrates and
  does not prove; Second-Order Linear Equations by title; worked lines in the
  library's notation.
- `initial-value-problems`: a new paragraph fitting `C·e^(2t) + D·e^(−t)` to
  `y″ − y′ − 2y = 0` through `C + D = 1, 2C − D = −2`; the sine–cosine
  derivatives declared as taken on trust with “Sine, Cosine and Their Rates”
  named; "the constants tile shows a dash"; step three names the system and
  Algebra's Systems and Matrices; a fourth preset `two-exps` pinning
  `C = −1/3, D = 4/3`; worked lines in the library's notation.
- `slope-fields`: worked lines in the library's notation, with the tag-shaped
  line rewritten.
- `reading-a-slope-field`: the uniqueness rewrite of concept two, the body
  paragraph, the `thm` and its follower, step three, the worked lines and
  `after`, quiz 2 and quiz 3 (question and `why`), and `mistakes[0]`; the key
  line in words; First-Order Linear Equations and Equilibria, Stability and
  Phase Lines by plain title.
- `eulers-method`: worked lines in the library's notation.
- `eulers-error-and-the-step-size`: two key lines rewritten (`N·h² = h`; the
  ratio "approaches 2" in words); `[0, 1]` as "from `t = 0` to `t = 1`";
  worked lines in the library's notation with `N·h = 1` for `N = 1/h`.
- `the-improved-euler-method`: worked lines in the library's notation with
  `N·h = 1`.
- `runge-kutta-four-slopes-per-step`: quiz 1 and quiz 2 `why`s corrected;
  `mistakes[2]` corrected; `≈ 0.0299484` to match the tile; `[0, 1]` in words
  twice; `Runge–Kutta` with the en dash in the panel; worked lines in the
  library's notation.
- `blow-up-and-the-interval-of-existence`: worked lines in the library's
  notation.
- `content/spoken/differential_equations_c3_euler.py`: spoken forms for
  `1/h`, `N = 1/h`, `h²·(1/h) = h`, `(1/h)·h² = h` and `≈ 6.77729e23`.

Lesson slugs, count and order are as `COURSES.json` lists them. The preview
(`scripts/preview_subject.py differential_equations --course
differential-equations-and-eulers-method`) reports OK: eleven pages, ten labs
executed and swept, ten pages with pinned figures all matching.

## Remaining issues

- `scripts/speechcheck.py` does not list Differential Equations, because the
  Subject is not yet in `build_paths.GENERATED_PATHS` on this branch; the
  speech audit above was done by reading every `data-say` attribute off the
  rendered pages instead. When the orchestrator wires the Subject,
  `speechcheck --list differential_equations` should be run once; every run
  on these ten pages read as a sentence at the time of writing.
- The speech engine strips any `<` … `>` pair inside one run as markup
  (item 6), and reads a hyphen-minus after a caret exponent as "negative"
  (item 5). Both are instrument behaviours that other courses on this path
  may also trip; the fix here was to the content, and the instrument belongs
  to the chrome-renderer tier.
- `checking-a-proposed-solution` is the heaviest lesson of part A (the
  residual on harder equations, the linear/nonlinear classification and what
  it buys, the five-point limit). It is one lesson by PLAN §C and the URL
  space is fixed; if the Subject is ever re-cut, "linear against not" is the
  natural second half, and `initial-value-problems` would then follow it
  directly.
- `blow-up-and-the-interval-of-existence` is the heaviest lesson of the
  course (interval of existence with the theorem, Euler past the asymptote,
  the digit budget). It is right as PLAN §C designed it and nothing was moved;
  a future re-cut would separate the digit budget, which is a fact about the
  Subject's method rather than about the equation.
- `initial-value-problems` keeps the PLAN's trigonometric preset ahead of the
  course that teaches `sin′` and `cos′`; the lesson now declares the trust
  and the exponential pair carries the teaching. If the plan is ever revised,
  swapping the prescribed instance for the exponential pair alone would
  remove the forward dependence entirely.
- PLAN §C's "Worked" line for `reading-a-slope-field` ("reaching it would
  mean two solutions through one point") uses the one-slope argument for the
  touch; the lesson now attributes the touch to uniqueness, and the plan
  should say the same if it is edited.
