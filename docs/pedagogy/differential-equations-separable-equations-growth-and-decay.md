# Pedagogy assessment — Separable Equations, Growth and Decay (differential equations, course 4)

Formed from the ten lesson dicts in `content/differential_equations/c4_separable/`
(`part_a.py`, lessons 1–5, and `part_b.py`, lessons 6–10, written by two
authors from `docs/differential-equations/PLAN.md` §C), the course dict in
`__init__.py`, the spoken forms in
`content/spoken/differential_equations_c4_separable.py`, and the pages as
`scripts/preview_subject.py` renders them, with every preset's tiles read off
the built page by `labcheck.js --observe` and every figure in the prose
recomputed with `fractions.Fraction` and double precision. The course may
assume the three courses before it and the Algebra Subject, and nothing else.
All ten lessons were read before any was changed; the last two sections record
what was changed and what was not.

Lessons, in course order: `separable-equations`, `why-separation-works`,
`implicit-and-explicit-solutions`, `exponential-growth`,
`doubling-time-and-half-life` | `radioactive-decay-and-dating`,
`newtons-law-of-cooling`, `mixing-problems`, `logistic-growth`,
`harvesting-and-the-threshold`. The bar marks the seam between the two authors.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.** Take
  an equation and an initial value to its relation without help
  (`separable-equations`); differentiate an implicit relation and show the
  equation comes back (`why-separation-works`); go from relation and initial
  value to the explicit branch and its interval
  (`implicit-and-explicit-solutions`); solve the growth equation two ways and
  say how far apart the answers are (`exponential-growth`); derive the
  doubling time, quote it rounded, find the crossing step
  (`doubling-time-and-half-life`); convert a half-life to a rate and back and
  date a sample (`radioactive-decay-and-dating`); reduce Newton's law to decay
  by a substitution (`newtons-law-of-cooling`); set up the balance for a tank
  and find its steady amount (`mixing-problems`); find the equilibria and the
  steepest growth of a logistic equation (`logistic-growth`); classify the
  equilibria of a harvested one and compute the threshold
  (`harvesting-and-the-threshold`). No head says "understand".
- **One method, taught once, then justified, then qualified.** The first
  three lessons are the right three in the right order: run the four moves
  (`separable-equations`), prove them legitimate as the chain rule read
  backwards, with a `thm` whose proof is algebra the reader has and runs in
  both directions (`why-separation-works`), then confront what the method
  hands back, a relation and not a function
  (`implicit-and-explicit-solutions`). The second lesson's insistence that the
  derivative check and the point check are two different jobs, and that a
  wrong `C` passes every derivative check, is exactly the habit the rest of
  the course relies on.
- **The exactness rule is kept in every tile and every sentence.** Every
  fraction a reader is told is a fraction (`625/256`, `43046721/8388608`,
  `725/16`, `4108933742199/51200000000`, `935/512`, `247/250`, `122/125`), and
  every figure with `e` or `ln 2` in it carries `≈` and is introduced with
  "rounded" at least once per lesson, as PLAN §E item 8 asks: `≈ 2.71828`,
  `≈ 0.276876`, `≈ 1.38629`, `≈ 5776.23`, `≈ 11552.5`, `≈ 49.4304`,
  `≈ 78.6939`, `≈ 13.8629`. `exponential-growth` says which tier each number
  is in within the sentence that reports it, as §F requires. All eighty-nine
  pinned tile strings across ten pages match the page, and every prose figure
  was recomputed and found right, including the ones that are not tiles:
  `(9/8)⁵ = 59049/32768`, `(9/8)⁶ = 531441/262144`, `(11/10)⁷ = 19487171/10000000`,
  `e^(0.7) ≈ 2.01375`, `1141/40`, `231/256`, `279/400`, `−21/400`, `−5/16`,
  `2025/64`, the warming cup's `5, 25/2, 65/4, 145/8, 305/16`, and the
  bracket `≈ 11552.5` to `≈ 17328.7`.
- **Euler's method is called what it is.** Every lesson that prints `yₙ`
  says it is a geometric sequence, that the closed form is the other thing,
  and why they differ ("each step assumed the rate stayed at its starting
  value"). `exponential-growth`'s second misconception is PLAN's own material
  clause in miniature ("exact arithmetic applied to an approximate method"),
  and `doubling-time-and-half-life` and `radioactive-decay-and-dating` both
  distinguish the grid time from the true time and print both so the gap is
  visible. `logistic-growth` teaches the digit budget as the lab's limit and
  not the population's, in a paragraph and again in `mistakes[2]`.
- **The lab's limits are stated where they bite.** The accepted `g` (a
  polynomial, `1/y`, `1/y^2`) in the first definition; `implicit only` for
  the cubic and what it means; the rational carbon rate `3/25000` chosen so
  Euler stays exact, with the resulting half-life `≈ 5776.23` named as a
  consequence of that choice and not a measurement; the step of 200 years in
  the quarter preset; the digit budget. Nothing is dressed up as more than
  the lab computes, and every application names its assumptions (constant
  volume, perfect stirring, a closed sample, constant surroundings).
- **The misconceptions are the real ones and each is refuted with a figure.**
  Moving `y` across and leaving `y′` behind, refuted by differentiating the
  wrong answer to `y′ = t/(2y − 2)`; cancelled differentials, refuted by the
  check view's exact `equal`; the positive root alone, refuted by
  `√4 = 2 ≠ −2`; exponential means fast, refuted by the factor `401/400`; the
  doubling time depends on the start, refuted by two presets printing the
  same `≈ 1.38629`; nothing left after two half-lives, refuted by `(247/250)ⁿ`
  positive for every `n`; a constant cooling rate, refuted by the rate column
  `−20, −15, −45/4, −135/16`; the tank fills in finite time, refuted by
  `(19/20)ⁿ > 0`; the exponential that stops at `K`, refuted by `f(5) = −5/4`;
  any harvest below the growth rate is safe, refuted by `279/400 < 300/400`.
  Every `mistakes[0]` is the §C misconception.
- **Retrieval practice is real.** Every quiz asks the reader to compute or
  classify, not to recall a word, and every `why` names what the wrong
  choices compute instead (`y₁` for `y₂`; the rate in grams per minute for
  the steady amount in grams; `1/k` for `ln 2/k`; `r·K` for `r·K/4`). The
  distractor PLAN warns about, the one true at one step size, was looked for
  and not found: "Step 7" in `doubling-time-and-half-life` is the trap and
  the `why` says why it is a trap.
- **The modelling lessons share one skeleton on purpose.** Cooling, mixing
  and decay are all `y′ = −k·(y − A)` with the shift read off the balance, and
  each lesson says so by name of the previous one; the reader meets the gap
  substitution once and reuses it twice. The last two lessons then change the
  shape (two equilibria, then a quadratic that counts them) and the course
  home's `syllabus_intro` describes that arc accurately.

## What the course teaches badly, or wrongly

1. **`doubling-time-and-half-life` generalised a fact that its own third
   preset refutes.** The body said "the true curve passes 2 at `T ≈ 1.38629`,
   between steps 5 and 6, so the step is the first grid point at or after
   it", and the third concept said the crossing "in general lies a step or
   part of a step later". For the slow preset the first grid point after
   `T ≈ 6.93147` is `t = 7`, where the closed form already reads `≈ 2.01375`,
   and the exact sequence crosses at step 8: a whole step after that grid
   point, as the lesson's own example and `after` correctly say. The
   paragraph now states what is true (for growth the sequence lies below the
   curve, so it cannot cross before the curve; the crossing is at or after
   the first grid point past `T`, and can be later), and the concept says how
   much later depends on the step. The worked `after` also said the decay
   preset crosses at step 6 "for the same reason"; for decay the factor `7/8`
   is below `e^(−1/8)`, the sequence falls faster than the curve and could
   cross early, and the two cross at the same step here only because both
   land between steps 5 and 6. It now says that.
2. **`implicit-and-explicit-solutions` claimed that "a solution of
   `y·y′ = t` cannot change sign by passing through zero".** `y = t` is a
   solution of `y·y′ = t` and passes through zero at the origin. The claim is
   true of `y′ = t/y`, which has no slope at `y = 0`, and the two forms are
   not equivalent on the axis; the lesson's own definition takes `g(y)·y′ =
   h(t)` as the equation. The paragraph and the worked `after` now make the
   claim about `y′ = t/y`, and add the fact that matters for the preset: the
   branch through `(0, 2)` never reaches the axis because `t² + 4 ≥ 4`. The
   step "If `y₀` is zero, both do not, and the equation itself has no slope
   there" was ungrammatical and said less than the lab does (it prints
   `implicit only` with a note that the branches meet there); it now says
   that. The third misconception's "the equation does not hold at the join"
   now gives the reason a reader can check: each branch arrives with an
   infinite slope.
3. **`newtons-law-of-cooling` mixed its two sign conventions in one
   sentence.** The lesson writes `y′ = −k·(y − A)` with `k > 0`, so its
   factor is `1 − kh`, which the key line, the `math` table and the worked
   lines all use; the body then said "the gap is multiplied by
   `1 + kh = 1 − 1/4 = 3/4`", borrowing the lab's signed `k` without saying
   so. A reader who has just been told `k = 1/4` reads `1 + kh` as `5/4`. The
   sentence now uses `1 − kh` and says in a bracket that the lab's factor
   tile, which takes the signed rate `−1/4`, writes the same number as
   `1 + kh`.
4. **`mixing-problems` wrote its balance in unit abbreviations that a voice
   cannot read.** The `math` block and the worked lines carried `5 L/min × 2
   g/L = 10 g/min`, spoken as "5 L over min times 2 g over L equals 10 g over
   min". The lesson's prose already says "litres per minute" and "grams per
   litre" in words; the blocks now do too (`5 × 2 = 10 grams per minute`),
   and the steady amount line is `A = 2 × 100 = 200 grams`. The hero key's
   `(inflow conc.)` read "inflow conc"; it is now `(inflow concentration)`.
5. **`harvesting-and-the-threshold`'s key line was silently gutted by the
   reader.** `H < 1: two;  H = 1: one;  H > 1: none` contains a `<` and a
   later `>`, which `speech.say` strips as an HTML tag, so the line was
   spoken as "H, 1, none". It now reads `H below 1: two;  H = 1: one;  H
   above 1: none`. The same mechanism threatens any key or worked line that
   compares in both directions; recorded under remaining issues for the
   renderer.
6. **Four plain fields were cut into fragments by the renderer's island
   detector.** In a plain field (a title, a `one_line`, a concept or
   misconception title) the renderer finds math on its own and gives each
   island a spoken form; a run beginning with `y′` loses its `y′` ("= k·y",
   "= −k·y", "= y·(1 −") and a bracketed term after a space is cut
   (`y = √(t² +`, with ` 4)` read as prose). The worked titles of
   `why-separation-works` and `logistic-growth`, the first misconception
   title of `implicit-and-explicit-solutions`, the `one_line`s of
   `exponential-growth` and `radioactive-decay-and-dating`, the `steps_title`
   of `exponential-growth` and the first concept title of
   `separable-equations` are reworded so that what the detector finds is
   whole (the retitled misconception is "Reading `y² = t² + 4` as the positive
   root alone", which is the model, not a formula). What remains in plain
   fields reads completely: `y² = t² + 4`, `y·y′ = t`, `y₀·e^(kt)`, `yₙ`, `tₙ`.
7. **Two `math` blocks read in pieces.** In `newtons-law-of-cooling` the rate
   column's heading `−(1/4)·gap` was spoken "times g A p"; it is now
   `−(1/4)·(yₙ − 20)`. In `exponential-growth` the table of `(1 + 1/n)ⁿ` had
   two rows of bare numbers and two with `≈`, so the reader said "a table,
   shown on the page" and then read the last two rows aloud; each row now
   begins `n = …:` and all four are read.
8. **Two crossing-step tiles were quoted in prose without the spoken form
   the other three have.** `step 6 (t = 3/2)` and `step 8 (t = 8)` read
   "step 6 t equals 3 over 2" while `step 3 (t = 3)` read "step 3, at t
   equals 3". Both are now in the spoken map, keyed by the exact tile text,
   which collides with nothing in any other Subject.
9. **Small faults in the mathematics of the prose.** `separable-equations`'s
   first misconception said the wrong slope field `t/(2y − 2)` and the right
   one `t/y` agree "at the starting point, where `y = 2`, … and nowhere
   else"; they agree wherever `t = 0` or `y = 2`, and what makes the error
   survive a first check is that both slopes are zero at `t = 0`. It now says
   that and that the check fails one step later. `exponential-growth`'s proof
   opened "take `y₀ > 0`; the other signs are the same with `|y|`", which is
   false for `y₀ = 0`, where division by `y` is not available and the
   constant solution is the answer; the line now says so. `why-separation-works`
   said the cube relation "has no simple explicit solution" one lesson after
   `separable-equations` said it has one, a cube root; it now says the lab
   does not solve it and the check does not need it to. The worked line "gap
   to the true T: `3/2 − 1.38629 ≈ 0.11371`" subtracted a rounded value and
   printed five figures; it is now `3/2 − T ≈ 0.113706`, six figures by the
   stated rule. `harvesting-and-the-threshold`'s second misconception said
   the stable level "vanishes together with the repelling equilibrium at
   `H = 1`", where in fact the two meet at `H = 1` and are gone past it.
10. **One quiz `why` left a distractor unexplained.** `exponential-growth`'s
    factor question offered `31/30` and said nothing about it; the `why` now
    says it divides by `k` instead of multiplying. The antiderivative `−1/y`
    in `separable-equations` is now credited to “The Derivative of 1/t”,
    which is where the reader met `(1/t)′ = −1/t²`.

## What it claims to teach but does not, and where a learner gets stuck

- **The `growth` mode's `grLast` tile is labelled "(exact)" and prints a
  rounded figure on the carbon presets.** For `k = −3/25000`, `h = 100`,
  `n = 64` the exact `yₙ` has 154 digits over 154, and the kit prints
  `≈ 0.46179 (exact: 154 digits over 154)`. That is honest and labelled, but
  a reader of `radioactive-decay-and-dating` who has just been told every
  Euler step is an exact fraction meets a `≈` in a tile called exact. The
  lesson does not quote this tile and the tile's own bracket explains
  itself; not changed, recorded.
- **`doubling-time-and-half-life` carries two ideas by design.** The
  doubling time and its independence from the start are one idea; the lag
  between the exact sequence's crossing step and `T` is a second, subtler
  one, and the lesson's original wrong generalisation (item 1 above) is the
  kind of slip a second idea invites. PLAN §C asks for both in this lesson,
  and the second is what the `grHit` tile exists to show, so the lesson keeps
  both; the prose now states the lag as an inequality and lets the three
  presets show its range.
- **`radioactive-decay-and-dating` is the densest lesson in the course**: a
  sign convention, two conversions, counting half-lives, the bracket, the
  rational-rate caveat and three presets with two step sizes. It is one hard
  idea (a half-life and a rate are one fact, through `ln 2`) with several
  consequences, and the `steps` list holds it together. If the Subject is
  ever re-cut, the carbon-specific material (the measured 5730 years against
  the lab's `≈ 5776.23`, and the quarter preset's 200-year grid) is the
  natural second half.
- **The forward references to stability vocabulary are acknowledged but
  heavy.** `logistic-growth` and `harvesting-and-the-threshold` print and
  use `stable`, `unstable`, `semistable` and the sign of `f′` at an
  equilibrium, which Equilibria, Stability and Phase Lines defines. The
  first says so ("in words the next course defines carefully") and the second
  says "the lab calls it semistable"; a reader is told the words are coming
  rather than left to guess, which is the right handling, but a reader who
  wants the definition now has to wait a course.

## Prerequisite order

Checked backwards across the path. `separable-equations` needs
antiderivatives of polynomials and the constant of integration (“The
Antiderivative and the Fundamental Theorem”, “The Constant of Integration” in
Accumulation and the Integral), `(1/t)′ = −1/t²` (“The Derivative of 1/t”, now
cited), and what an initial value fixes (“Initial Value Problems”).
`why-separation-works` needs the chain rule on polynomials (“The Chain Rule”
in Rates of Change and the Derivative, cited by title) and the fact that a
function with zero rate is constant (“The Constant of Integration”, cited by
course). `implicit-and-explicit-solutions` needs the quadratic formula and
square roots from Algebra's Quadratics and Complex Numbers, and the blow-up
of “Blow-Up and the Interval of Existence” (cited). `exponential-growth` needs
`∫ dt/t` (“The Integral of 1/t”, cited), `(e^(kt))′` (“The Exponential and Its
Rate”, cited), the geometric sequence (“Geometric Sequences and Series” in
Algebra's Sequences and Series, cited) and `e` as a limit of `(1 + 1/n)ⁿ`
(“The Number e” in Algebra's Exponential and Logarithmic Functions, cited),
and Euler's error ratio (“Euler's Error and the Step Size”, cited); every
cited title exists. `doubling-time-and-half-life` needs `ln` as the inverse
of `e^x`, Algebra. `logistic-growth` needs `y″ = f′(y)·y′` by the chain rule
and concavity from “The Second Derivative”, used without citation but with
the rule written out. `harvesting-and-the-threshold` needs the discriminant,
Algebra. No violation sits in an earlier course, and the course home's
`assumes_long` names the right courses by title. Inside the course the order
is right: method, justification, meaning; then one equation seen twice; then
the same equation shifted three times; then a second equilibrium and a
parameter that removes it.

## Mathematical accuracy

- Every pinned tile was observed on the built page and every prose figure
  recomputed. Two of PLAN §C's hand-checked figures are off in their last
  digit and the lab is right: `e − 625/256 = 0.2768755…` prints `≈ 0.276876`
  (PLAN: `0.276875`), and `20 + 80/e = 49.43035…` prints `≈ 49.4304` (PLAN:
  `49.4305`). The authors used the lab's figures, as §C instructs, and the
  disagreement is recorded here.
- Three presets differ from PLAN §C's instances, each for a reason the lab
  forces: `quarter` steps by 200 years, not 100, because a quarter is
  reached near `t ≈ 11552` and 64 steps of 100 end at 6400; `coffee` runs 4
  steps, not 8, so that `grLast` is the worked example's `y₄ = 725/16`; and
  the circle preset PLAN calls `hyperbola` is named `arc`, since `y² = 1 − t²`
  is a circle. `grHit` on `quarter` is `step 58 (t = 11600)`, within one step
  of `2T ≈ 11552.5`, as the prose says.
- The separation theorem, its proof and the direction a check uses are
  stated correctly, including the interval hypothesis. The exponential
  theorem's proof assumes uniqueness, which the previous course stated in
  words; the lesson calls the result "a solution in closed form" and the
  course home's `not_covered` says uniqueness is not proved here.
- The domain claims are right: `−1 < t < 1` with the ends excluded because
  `y′ = −t/y` has no value at `y = 0`; `t < 1` as the piece containing the
  initial `t`; `all t` for `t² + 4`. The lab also prints `−√2 < t < √2` for
  the reciprocal preset, which no lesson quotes.
- `1 + x ≤ e^x` is what makes "the exact sequence is always below the curve
  for growth" true; the lesson states it as the geometry of the step, which
  is the right level. For decay the same inequality puts Euler below the
  curve too, which is why the crossing can be early; the corrected `after` in
  `doubling-time-and-half-life` says so.
- The carbon-14 half-life "commonly quoted as about 5730 years" is the
  Cambridge value; `3/25000 = 0.00012` exactly; `1/k = 25000/3 ≈ 8333` is the
  mean lifetime, correctly described as the time to fall to `1/e`.
- The harvested quadratic, its discriminant `16·(1 − H)`, the factorisations
  at `H = 3/4` and `H = 1`, `f′(1) = 1/2`, `f′(3) = −1/2`, `H* = rK/4` and the
  dip check `−21/400` are all right, and `auInflect` prints `none` at
  `H = 1` because `f(2) = 0` there, which the lesson correctly does not call
  an inflection.

## The seam between part A and part B

The two authors agree on voice (careful prose, British spelling, no filler,
no exclamation marks), on the entity conventions in prose fields, on citing
by title, on marking every rounded figure, and on the sign convention
`y′ = −k·(y − A)` with `k > 0` in the prose against the signed rate in the
lab's box, which part B states in every lesson that uses it. Part A's closing
note hands over correctly ("how old is a sample that has lost three quarters
of its carbon?") and part B's first lesson works exactly that sample. The
only drift was the one sign slip in `newtons-law-of-cooling` (item 3), now
closed. Part B uses a `_p` helper for its `autonomous` presets and part A
writes its dicts out; that is source style, invisible on the page.

## Changes made

- `separable-equations`: the first concept title no longer carries notation
  the island detector cuts; `−1/y` credited to “The Derivative of 1/t”; the
  first misconception says the two slope fields agree where `t = 0` and that
  the check fails one step later.
- `why-separation-works`: the worked title retitled; the cube example says
  the lab does not solve the relation and the check does not need it to.
- `implicit-and-explicit-solutions`: the "cannot change sign" claim made
  about `y′ = t/y`, with the preset's own reason added; the worked `after`
  likewise; the branch concept says "the positive root" and "the negative
  one" instead of `+√` and `−√`; the `y₀ = 0` step rewritten; the
  branch-switching misconception gives the infinite slope; the first
  misconception retitled.
- `exponential-growth`: the `one_line` and `steps_title` reworded for the
  detector; the proof's opening line covers `y₀ = 0`; the `(1 + 1/n)ⁿ` table
  rewritten row by row so every row is read; the factor quiz's `why`
  explains `31/30`.
- `doubling-time-and-half-life`: the third concept, the crossing paragraph
  and the worked `after` corrected as item 1 describes; the gap line is
  `3/2 − T ≈ 0.113706`.
- `radioactive-decay-and-dating`: the `one_line` reworded for the detector.
- `newtons-law-of-cooling`: the factor sentence uses the lesson's own
  `1 − kh` and explains the lab's `1 + kh`; the rate column heading is
  `−(1/4)·(yₙ − 20)`.
- `mixing-problems`: the balance block and the worked lines carry units as
  words; the key line says `(inflow concentration)`; the outflow
  misconception names the unit error it describes.
- `logistic-growth`: the worked title retitled.
- `harvesting-and-the-threshold`: the key line no longer pairs `<` with `>`;
  the second misconception says the equilibria meet at `H = 1` and are gone
  past it.
- `content/spoken/differential_equations_c4_separable.py`: spoken forms for
  `step 6 (t = 3/2)` and `step 8 (t = 8)`, matching the three already there.

Lesson slugs, count and order are as `COURSES.json` lists them. The preview
(`scripts/preview_subject.py differential_equations --course
separable-equations-growth-and-decay`) reports OK: eleven pages, ten labs
executed and swept, ten pages with eighty-nine pinned figures all matching,
no math run guessed at; `tests/test_speech.py` passes with the two new
spoken forms.

## Remaining issues

- `speech.say` strips any `<…>` pair as an HTML tag before speaking, so a
  single key or worked line that compares in both directions (`H < 1 … H >
  1`) loses its middle silently. This course now avoids the shape; the fix
  belongs in `scripts/mathpath/speech.py` (strip only real tags, or escape
  comparison operators before the strip) and is the chrome renderer's, not
  the course's. Every other Subject's hero keys should be grepped for the
  same shape.
- `speech.islands` cuts a run that begins with a primed letter (`y′ = k·y`
  becomes `= k·y`) and a bracketed term after a space (`√(t² + 4)` becomes
  `√(t² +`) in plain fields. This course's plain fields are reworded around
  it; the other nine courses of the Subject, whose `one_line`s and titles
  are full of `y′ = …`, almost certainly read the same way and should be
  checked with the same scan (every `<span data-say=…>` without
  `class="math"` on a rendered page). The fix is to the detector.
- `labcheck.js --observe` and the lab are right, but the `growth` kit's
  `grLast` tile is labelled "(exact)" and prints `≈ 0.46179 (exact: 154
  digits over 154)` when the fraction is too long to show. A label such as
  "Last yₙ" with the exactness stated in the value would be more honest
  than a `≈` under a heading that says exact. The kit is `@lab-arithmetic`'s.
- `radioactive-decay-and-dating` is the lesson most worth splitting if the
  Subject is ever re-cut: the conversion `k·T = ln 2` with the bracket in
  half-lives is one lesson, and carbon dating with the rational-rate caveat
  and the two step sizes is another. It is one lesson by PLAN §C and the URL
  space is fixed; recorded, not done.
- `doubling-time-and-half-life` now states the lag between the crossing step
  and `T` as an inequality for growth only. For decay the sequence can cross
  early, which the worked `after` says for the halving preset; no preset
  shows an early crossing, and one would (for instance `k = −1/2`, `h = 1`,
  factor `1/2`, which halves at `t = 1` against `T ≈ 1.38629`). Adding a
  fourth preset is a change to the lab data an author may make; the three
  §C instances are kept as shipped.
- The two kits print the equilibrium types `stable`, `unstable`,
  `semistable` and `f′` at each one in this course, a course before the
  lessons that define them. Both lessons say the definitions are coming.
  Whether `logistic-growth` should instead say only "approached" and
  "left" is a question for the Subject's pedagogical review of course 5, not
  this course's.
