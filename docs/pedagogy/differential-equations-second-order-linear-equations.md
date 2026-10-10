# Pedagogy assessment — Second-Order Linear Equations (differential equations, course 7)

Formed from the ten lesson dicts in `content/differential_equations/c7_second_order/`
(`part_a.py`, lessons 1–5; `part_b.py`, lessons 6–10; `__init__.py`, the course
dict), the spoken forms in `content/spoken/differential_equations_c7_second_order.py`,
and the kits they render through (`scripts/mathpath/labs/calckit.py` mode
`transcendental`; `scripts/mathpath/labs/dekit.py` mode `verify`;
`scripts/mathpath/labs/dekit_b.py` modes `char` and `phase`), on branch
`feat/differential-equations` before the Subject was wired into the site. The
design authority is `docs/differential-equations/PLAN.md` §0 (the exactness
rule), §C (course 7), §D.2 (`transcendental`), §D.3 (`verify`, `char`,
`phase`), §D.5 and §F; the course was written in two parts, so the seam at
lesson 6 is assessed as well.

Every lesson was read in full before anything was changed. Every pinned figure
and every figure quoted in prose was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py differential_equations --course second-order-linear-equations`),
every rounded figure was recomputed in double precision and every exact one in
`fractions.Fraction`, including the 24-step and 12-step Euler endpoints the
`phase` lab prints, which came out equal to the tiles, and the radius squared
after 24 steps, which is `(17/16)²⁴` exactly as the lesson claims. Every math
run's `data-say` was read, including the runs inside the quiz, which the page
carries as an escaped JSON literal and a scan of the HTML spans does not see.
Lessons, in course order: `sine-cosine-and-their-rates`,
`the-second-order-equation`, `the-characteristic-equation`,
`real-distinct-roots`, `repeated-roots`, `complex-roots-and-oscillation`,
`fitting-the-initial-conditions`, `superposition-and-the-wronskian`,
`from-second-order-to-a-system`, `euler-on-an-oscillator`. The course may
assume First-Order Linear Equations and everything before it, plus the Algebra
Subject; it is judged against that.

## Verdict

The course teaches its subject. A reader who finishes it can read the rates of
sine and cosine off a rounded table with their signs and use them twice, check
a candidate against a second-order equation by substituting it and say how many
starting values it needs, turn `a·y″ + b·y′ + c·y = 0` into its quadratic and
name the kind of root before solving, write and fit the general solution for
distinct real, repeated and complex roots and read growth, decay or oscillation
off the roots, set up and solve the two-by-two pair for the constants and say
what a dash from the lab means, compute `W(0)` and say what a nonzero value
guarantees, rewrite the equation as a system whose trace and determinant
reproduce the quadratic, and step the oscillator with Euler's method and prove
the factor `1 + h²`. Those are the acts the `standard` fields measure and the
labs compute, and no objective is "understand X". The `mistakes[0]` of every
lesson is the §C misconception, each refuted with a specific residual, fraction
or step. Every pinned tile matched the lab. Every figure quoted in prose agreed
with the lab or with a recomputation, except the seven three-figure roundings in
`euler-on-an-oscillator`, which were right as far as they went and are now six
figures. The PLAN's own "Worked" arithmetic holds in all ten lessons; where the
kit deviates from §C and §D (roots numbered larger first, `W(0) = −√5` rather
than `√5` for the surd preset, the order of `ceGeneral`), the lessons follow
the kit and explain the sign as the order of the two roots, which is right.

The defects found were local and are repaired below: one key block whose
reading lost two lines to an apparent HTML tag, one key block that read "every
solution to 0", a steps introduction counting four moves above five, two
sentences crediting `e^(kt)` to the wrong course, one sentence describing the
irrational-root case as a "cosine-and-exponential solution", seven roundings
to three figures and three bare decimals, one numbered cross-reference and
five descriptive ones where the convention is a title, a lab tile that
contradicts the previous lesson's constants without a word of explanation, and
a family of readings (bare `sin` and `cos`, a bracket followed by a prime,
`cos′ 0`) that misread aloud. Nothing needs splitting, merging or reordering
within the URL space the course has.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names what is produced: the rate
  with its sign read off a rounded table and used twice
  (`sine-cosine-and-their-rates`); the residual `y″ + y` simplified and the
  count of starting values (`the-second-order-equation`); the quadratic, the
  discriminant and the kind of root before the roots
  (`the-characteristic-equation`); the two equations for the constants solved
  and the long run forecast from the signs (`real-distinct-roots`); `t·e^(rt)`
  checked by substitution and `r·C₁ + C₂ = y′(0)` solved (`repeated-roots`);
  `α` and `β` read off and the motion read off `α`
  (`complex-roots-and-oscillation`); the pair set up by putting `t = 0` in the
  solution and in its rate, and the meaning of a dash
  (`fitting-the-initial-conditions`); `y₁·y₂′ − y₁′·y₂` at `0` and a pair for
  which the fit fails (`superposition-and-the-wronskian`); the division by `a`,
  the matrix, and `λ² − τ·λ + Δ = 0` against the characteristic equation
  (`from-second-order-to-a-system`); the ratio tile predicted before it is read
  and two step sizes compared at one end time (`euler-on-an-oscillator`).
- **The exactness rule is kept, and the tiers are named in the sentence that
  reports the number.** `sine-cosine-and-their-rates` puts `≈` on every
  quotient and says that no entry in its tables is exact; the limit is written
  `cos(1) ≈ 0.540302` and called a claim, and the last quotient `≈ 0.533706` is
  "near but not equal to" it. `the-characteristic-equation` prints
  `(1 ± √5)/2` as a surd and says the rounded `≈ 1.61803` is "for the eye
  only". `fitting-the-initial-conditions` gives the surd constants
  `(5 − √5)/10` and `(5 + √5)/10` by hand and checks that they add to `1`.
  `superposition-and-the-wronskian` prints `−√5` and says it is an exact surd,
  not a rounded number. `euler-on-an-oscillator` says `17/16` "is not a rounded
  `1.0625`" and that `289/256` is exactly its square.
- **Claims are stated as claims, once, where it matters.** `sin′ = cos` is "a
  claim, and the lab demonstrates it at the places you choose without proving
  it… no table can"; the second-rate proof is "only as firm as the two claims
  it uses". `(e^(rt))′ = r·e^(rt)` is named as the claim an earlier course
  demonstrated. That the general solution has no other members is "the part
  this course states and does not prove in full" in `real-distinct-roots`,
  `repeated-roots` and `complex-roots-and-oscillation`, each pointing to the
  Wronskian lesson for the part the reader can use. Abel's identity appears as
  "stated as a pattern, not proved", and uniqueness as a fact "the course uses
  and does not prove". The proofs that are given (combinations are solutions,
  the characteristic equation, `t·e^(rt)`, the complex pair, the Wronskian
  guarantee, the matrix's trace and determinant, `(1 + h²)` per step) use only
  algebra the reader has.
- **The method is kept apart from the solution.** `euler-on-an-oscillator` is
  the material clause made concrete: "The fractions the lab prints are exact,
  and they show an exactly wrong answer"; "the growth is in the recipe"; a
  smaller step "slows the growth and cannot remove it". The polygon is never
  called the solution, and the true circle behind it is named as drawn in
  floating point.
- **The lab's limit is stated in the lesson that leans on it.** The refusal to
  fit surd constants, with the banner's reason, is the subject of a whole
  section of `fitting-the-initial-conditions` and of its quiz 4 and
  `mistakes[2]`; `the-second-order-equation` says the lab refuses a candidate
  that is not linear in `C` and `D`, which is what `vfCompute` does;
  `sine-cosine-and-their-rates` says the quotients are computed in ordinary
  floating point and why.
- **The misconceptions are refuted with the specific number.** `cos′ = +sin`
  would make the column at `a = 1` positive, and `cos` would not satisfy
  `y″ + y = 0` (`sine-cosine-and-their-rates`); `C·cos t` with `y(0) = 1`
  forces `y′(0) = 0` (`the-second-order-equation`); `r² + 3r + 2 = y` asks a
  number to equal a function of `t` (`the-characteristic-equation`); the bare
  sum has `y(0) = 2` and `y′(0) = r₁ + r₂` for every equation
  (`real-distinct-roots`); `e^(−2t)` alone has `y′(0) = −2`, not `1`
  (`repeated-roots`); `cos(2t)` substituted into `y″ + 2y′ + 5y` leaves
  `cos(2t) − 4·sin(2t)` (`complex-roots-and-oscillation`); `y(0) = 0` does not
  make `y′(0) = 0`, and the preset's solution rises at rate `1`
  (`fitting-the-initial-conditions`); `e^(−t)` and `2·e^(−t)` have Wronskian
  `0` and every combination has `y′(0) = −y(0)` (`superposition-and-the-wronskian`);
  the swapped bottom row turns real roots into a spiral
  (`from-second-order-to-a-system`); `(1, −1/4)` has `x² + v² = 17/16`
  (`euler-on-an-oscillator`).
- **Worked example, then faded guidance, then independent practice.** The
  three root lessons each take one kind of root through a worked fit and a
  substitution check, `fitting-the-initial-conditions` then shows the three
  fits are one computation and does the elimination once in general; the
  `steps` of each lesson are the worked example as a recipe, and every quiz
  asks for the same act on a new instance (`y″ − 5y′ + 6y = 0`,
  `y″ + 6y′ + 9y = 0`, roots `−3 ± 4i`, `2x″ + 8x′ + 6x = 0`, `h = 1/2`). The
  panel intros ask the reader to compute before pressing the button.
- **Figures agree with the lab.** Every pinned tile on the ten pages matched
  the observed tile, and every tile the prose quotes was found in the observed
  output: `≈ 0.841471`, `≈ 0.999959`, `≈ −0.459698`, `≈ −0.00781234`,
  `≈ −0.956449`, `≈ −0.845658`, `cos(1) ≈ 0.540302`, `−sin(1) ≈ −0.841471`;
  `−2·sin(t)`, `C = 1, D = −2`; `1`, `0`, `−16`, `5`, `−2, −1`,
  `−2 (repeated)`, `−1 ± 2i`, `(1 ± √5)/2`, `two real roots (irrational)`;
  `2·e^(−t) − e^(−2t)`, `C₁ = 0, C₂ = 1`, `e^(3t) − e^(2t)`;
  `(C₁ + C₂·t)·e^(−2t)`, `C₁ = 1, C₂ = 3`, `3·t·e^(−2t) + e^(−2t)`,
  `0 (repeated)`, `−1/3 (repeated)`; `e^(−t)·sin(2t)`, `±2i`,
  `3·cos(2t) − 2·sin(2t)`, `1 ± i`; `C₁ = 1, C₂ = −1`,
  `2·e^(−t)·cos(2t) + e^(−t)·sin(2t)`, `—`; `−1`, `2`, `1`, `−√5`; `−3`, `2`,
  `0`, `4`, `−2`, `5`, `stable node`, `centre`, `stable spiral`; `17/16`,
  `65/64`, `5/4`, `(11753/4096, 1287/512)`. The gap ratios the first lesson
  describes were recomputed: the sine column at `0` shrinks its gap by
  `0.260, 0.252, 0.251…` and the cosine column at `1` by
  `0.849, 0.598, 0.540, 0.518, 0.509, 0.504`, which is "about a quarter" and
  "from the third row on, about a half".
- **The seam at lesson 6 is nearly invisible.** `complex-roots-and-oscillation`
  opens on `y″ + 2y′ + 5y = 0` with "The discriminant is `4 − 20 = −16`", the
  preset `the-characteristic-equation` introduced three lessons earlier, and
  uses part A's vocabulary (kind of root, general solution, the fit, the
  residual in the status line). Both parts spell British (`recognise`,
  `centre`), both write curly quotes as entities, both cite lessons by title
  and courses by name, and both use the lab's convention that the larger root
  is `r₁`.

## What it taught badly, or said wrongly

### Facts a reader would trust that were wrong or misattributed

- **`the-characteristic-equation`, body, and the course `blurb`:** "The
  previous course met `y′ = k·y` and its solution `e^(kt)`." The previous
  course is First-Order Linear Equations; `y′ = k·y` and `e^(kt)` are the work
  of Separable Equations, Growth and Decay, which the previous course then
  leaned on. Repaired in both places.
- **`fitting-the-initial-conditions`, the declining paragraph:** "Exact
  fractions cannot hold a surd inside a cosine-and-exponential solution." The
  preset that is declined, `y″ − y′ − y = 0`, has two real irrational roots and
  a solution made of two exponentials; there is no cosine. Repaired to say
  what the lab actually needs (rational exponents and constants, so that it
  can differentiate and substitute without rounding), and the lab's other
  refusal is now named too: a complex pair whose `β` is a surd, as in
  `y″ + 3y = 0` with roots `±√3·i`, is declined with a banner that names the
  irrational frequency, which a reader who types that equation would otherwise
  meet unexplained.
- **`sine-cosine-and-their-rates`, `concepts[0]`:** "the entry that is exact
  has no `≈`" tells a reader that one entry in the table is exact. None is: the
  `transcendental` mode's only exact entry is the exponential at `h = 1` with a
  rational base, which these presets never show. Repaired.
- **`the-characteristic-equation`, `steps_intro`:** "Four moves" above five
  steps. Repaired.

### Prose looser than the lab

- **`from-second-order-to-a-system` shows ten tiles and explains four.** The
  page prints eigenvectors, a general solution, constants fitted to the start
  and two Euler tiles that the lesson never mentions, and one of them
  contradicts the lesson before it: for the first preset `ppC` says
  `C₁ = −1, C₂ = 2`, while `real-distinct-roots` fitted `C₁ = 2, C₂ = −1` to
  the same equation and start. The `phase` kit numbers eigenvalues from the
  smaller up and the `char` kit numbers roots from the larger down, so the two
  labs name the same two constants in opposite order. A paragraph now says which
  tiles belong to Systems and the Phase Plane, names the order, and shows that
  the first component is `2·e^(−t) − e^(−2t)` either way.
- **`sine-cosine-and-their-rates` leaves the fourth tile unexplained.**
  `tqRatio` divides the last quotient by `f(a)`; it was built for the
  exponential, prints `—` for sine at `0` and a meaningless `≈ 0.634254` for
  sine at `1`. One sentence now says what it is for and that the first three
  tiles are the ones to read.
- **The same lesson gives two convergence rates without the reason.** The sine
  column at `0` closes its gap by a quarter per halving and the cosine column
  at `1` by a half, and a reader who notices is given nothing. One sentence
  now says why: the leading error of a one-sided quotient is proportional to
  `h` times the second rate at `a`, and `sin″ 0 = −sin 0 = 0`, so at `0` that
  term is absent and the `h²` term is what remains. The sentence uses the
  lesson's own second claim, which is why it belongs here.
- **`from-second-order-to-a-system`, math block:** `−4e^(−t)` without the
  product dot, beside lines that carry it. Cosmetic; fixed.

### The exactness rule

- **`euler-on-an-oscillator`:** `(17/16)²⁴ ≈ 4.28`, `(65/64)⁴⁸ ≈ 2.1`,
  `(5/4)¹² ≈ 14.6`, the logarithms `≈ 2.68`, `≈ 1.46`, `≈ 0.744` and the
  radius ratio `≈ 2.07` were rounded to three figures with no stated rule, in
  the example, quiz 3 and `mistakes[1]`. All now print the Subject's six
  significant figures: `4.28444`, `2.10476`, `14.5519`, `2.67772`, `1.45499`,
  `0.744201`, `2.06989`, each recomputed.
- **`sine-cosine-and-their-rates`:** "`π/180`, about `0.0174533`" is now
  `π/180 ≈ 0.0174533`, rounded; quiz 4's "ending near `0.5337`" and "about
  `0.5337`" are now `≈ 0.533706`, the figure the tile prints; quiz 1's
  distractor `cos′ 0 = −0.459698` now carries `≈`, and is still wrong for the
  reason the `why` gives.

### Cross-references

- `real-distinct-roots` cited "the combination rule from the second lesson", a
  number. Now “The Second-Order Equation”. "The lesson on the Wronskian"
  (`real-distinct-roots`, `repeated-roots`, `complex-roots-and-oscillation`),
  "the repeated-root lesson" (`superposition-and-the-wronskian`, quiz 4), "the
  earlier course demonstrated with rounded quotients"
  (`the-characteristic-equation`) and "an earlier course ran the same recipe"
  (`euler-on-an-oscillator`) are now titles. `superposition-and-the-wronskian`'s
  note said "The first half of the course has solved one equation at a time",
  which is the authoring split the reader never sees; now "The course so far".

### Prerequisite order

- `from-second-order-to-a-system` uses the words trace and determinant, which
  PLAN §B assumes from Algebra's Systems and Matrices only for course 9. The
  lesson defines both for the two-by-two it needs and now says where the words
  come from. Not a defect; recorded.
- `complex-roots-and-oscillation`'s proof differentiates `cos(βt)`, which needs
  the chain rule the Subject verified on polynomials. The proof now says the
  chain rule supplies the factor `β`, the same way the lesson treats the
  exponential's rate as a stated claim. Everything else the course uses is in
  place: complex numbers from Algebra's Quadratics and Complex Numbers (named
  in `assumes_long`), the product rule from Rates of Change and the Derivative,
  Euler's steps from Differential Equations and Euler's Method, and `e^(kt)`
  from Separable Equations, Growth and Decay.

### Pins

- `real-distinct-roots` presets `mixed` and `grow` and
  `complex-roots-and-oscillation` preset `growing` did not pin `ceGeneral`,
  which §C lists for those lessons. The observed strings (`C₁·e^t + C₂·e^(−t)`,
  `C₁·e^(3t) + C₂·e^(2t)`, `e^t·(C₁·cos(t) + C₂·sin(t))`) are now pinned.

### Speech

- **`complex-roots-and-oscillation`, key block:** the `data-say` read "disc,
  0. … alpha, 0 grows." The mathblock reading treats anything between a `<`
  and a `>` on one line as a tag and drops it, so "`< 0: roots α ± βi, β >`"
  and "`< 0 shrinks, α = 0 level, α >`" vanished from the reading while the
  visible text was intact. Rewritten in words (disc negative, `β` positive,
  `α` negative, `α` positive) so that no key line carries both signs. The
  renderer behaviour is recorded under remaining issues.
- **`real-distinct-roots`, key block:** "every solution → 0" read "every
  solution to 0"; the arrow reads "goes to" between math and "to" after a
  word. Both forecast lines are now words ("every solution decays", "it
  grows").
- **Bare `sin`, `cos`, `−sin`, `−cos`, `+cos`, `cos′`, `cos″`, `sin″`,
  `−(sin′)`** read as abbreviations ("negative sin", "cos prime", "plus cos")
  in some sixty runs across the first two lessons and the course home. Each
  now has a spoken form. A bare function name has exactly one meaning wherever
  it appears as a math run, and the engine's own `FUNCTIONS` table says the
  same, so the readings are safe to share globally; none is a lone symbol
  whose meaning changes with context.
- **A bracket followed by a prime loses "the quantity":** `(t·e^(rt))′` read
  "t times e to the power r t prime", which is `t·(e^(rt))′`, a different
  function. Spoken forms added for the six such runs (`(e^(rt))′`,
  `(t·e^(rt))′`, `(t·e^(rt))″`, `(C·e^(−2t))′`, the two `(C·y₁ + D·y₂)″`
  identities) and for the two square-bracket groupings in `repeated-roots`,
  whose brackets read as nothing.
- **Quiz runs `cos′ 0 = 1`, `cos′ 0 = 0`, `cos′ 0 = −1`, `sin′ 1`,
  `sin′ 1 = cos 1`** read "cos prime 0 equals 1", and `y″(0)` in
  `the-second-order-equation`'s quiz 2 read "y double prime 0", because the
  §D.5 call rule stops at a double prime; spoken forms added. These were
  visible only after decoding the `QUIZ` literal.
- `x² + v² = cos² t + sin² t = 1` read "cos squared t"; spoken form added.
- Not changed: lowercase `a` reads as the letter name "A" everywhere
  (`a·y″ + b·y′ + c·y = 0`), the global engine's rule; `(x, v)` and `(1, 0)`
  read "x, v" and "1, 0", the engine's tuple rule, which the speech contract
  says not to override per run. Both are chrome, not content.

### Course home

- The `blurb`'s attribution of `e^(kt)` (above). `footer_lead`'s claim that
  "each solution is checked by substituting it into the equation" is honoured:
  `ceSolve` computes the residual of the fitted solution and the banner prints
  it, which is more than the `linear1` kit of the previous course does.

## Where a learner gets stuck

- **The first lesson is a calculus lesson at the head of a differential
  equations course.** It carries one hard idea (the rates of sine and cosine as
  a demonstrated claim), radians, and the second rates, and it is a `calckit`
  page whose tiles were designed for the exponential. It is as good as the
  design allows: the lab paragraph now says which tiles to read, the
  convergence-rate sentence turns the one oddity a reader would notice into a
  use of the lesson's own claim, and the quiz covers each of the three ideas.
- **`complex-roots-and-oscillation` is the heaviest lesson** (the complex pair
  as two real numbers, a proof with the product rule, a hand check, the fit,
  and reading the motion off `α`). PLAN §C puts all of it under one slug and
  the quiz covers each piece. Left as designed; see remaining issues.
- **The two labs number the constants in opposite orders**
  (`real-distinct-roots` against `from-second-order-to-a-system`). Now said in
  the lesson where the reader meets it.
- **A dash in `fitting-the-initial-conditions`** is the one place the lab
  declines, and the lesson spends a section, a quiz item and a misconception
  on it, which is the right weight: the reader who types `y″ + 3y = 0` is now
  told about the second banner too.
- **`euler-on-an-oscillator`'s `ppLast` for `h = 1/8`** is a pair of
  forty-four-digit fractions. The lesson does not quote it and does not need
  to; the ratio tile carries the lesson, and the size of the endpoint is the
  digit growth that “Blow-Up and the Interval of Existence” taught.

## Repairs made in this pass

In `content/differential_equations/c7_second_order/__init__.py`: the `blurb`'s
attribution of `y′ = k·y`. In `part_a.py`: `sine-cosine-and-their-rates`
`concepts[0]`, the lab paragraph (the fourth tile), the column-at-zero
paragraph (the quarter against the half), `mistakes[2]` (`π/180`), quiz 1's
third choice, quiz 4's question and fourth choice;
`the-second-order-equation` `concepts[0]` wording; `the-characteristic-equation`
the opening paragraph, the exponential-rate paragraph, `steps_intro`;
`real-distinct-roots` key lines 4–5, the paragraph after the theorem, and
`ceGeneral` pins on `mixed` and `grow`; `repeated-roots` the proof's last
paragraph. In `part_b.py`: `complex-roots-and-oscillation` key lines 1, 3 and
4, the proof's first and third paragraphs, `steps[3]`, and the `ceGeneral` pin
on `growing`; `fitting-the-initial-conditions` the declining paragraph;
`superposition-and-the-wronskian` quiz 4 `why` and the note;
`from-second-order-to-a-system` the matrix paragraph, the math block's product
dots, and a new paragraph on the six unexplained tiles;
`euler-on-an-oscillator` the Euler-recipe paragraph, the total-growth example,
quiz 3 `why` and `mistakes[1]`. In
`content/spoken/differential_equations_c7_second_order.py`: twenty-seven new
exact-run readings (the bare function names and their signed and primed forms,
the bracket-then-prime identities, the two square-bracket groupings, the
`cos′ 0` and `y″(0)` quiz runs, `sin″ 0 = −sin 0 = 0`, the Pythagorean line); every
earlier key is still a live run, including the three that live only in quiz
choices.

Slugs, lesson count, modules, lab keys and modes are as
`docs/differential-equations/COURSES.json` lists them.
`scripts/preview_subject.py differential_equations --course second-order-linear-equations`
reports OK: 11 pages, every lab executes and survives the sweep, every pinned
figure on the ten pages matches, no math run without a spoken form, none
ambiguous, every key line within the 46-character box.

## Remaining issues

- **No split or cut is believed in.** If one lesson were to be split it would
  be `complex-roots-and-oscillation`, into the solution for a complex pair and
  the reading of the motion off `α` and `β`, which is the next course's
  business as much as this one's; PLAN §C puts both here and the quiz covers
  each, so it is left as designed.
- **The mathblock reading strips an apparent tag.** A key line or math line
  that carries `<` and later `>` loses everything between them from its
  `data-say` while the visible text is intact (`complex-roots-and-oscillation`
  before this pass). The content convention that avoids it is to write a
  comparison in words in key lines; the renderer behaviour belongs to the
  chrome-renderer tier and is not changed here.
- **Quiz runs are invisible to a `data-say` scan of the HTML.** The quiz is
  carried as an escaped JSON literal in the page script; the readings inside
  it are only seen by decoding `QUIZ`. Three of this course's spoken keys and
  six of the misreadings fixed in this pass live only there. A reviewer who
  reads `data-say` off the page should decode the literal too.
- **PLAN §C and §D.3 disagree with the kit on two strings** for the `char`
  mode: `W(0) = √5` where the kit prints `−√5`, and `ceGeneral` written
  `C₁·e^(−2t) + C₂·e^(−t)` where the kit, which numbers the larger root first,
  prints `C₁·e^(−t) + C₂·e^(−2t)`. The kit's header records the deviation and
  the lessons follow the kit; the PLAN is the file to update.
- **Lowercase `a` is read aloud as "A"** on every page that writes
  `a·y″ + b·y′ + c·y = 0`, the engine's global rule for the article. Recorded,
  not changed, as in the previous course's assessment.
