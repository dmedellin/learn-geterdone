# Pedagogy assessment — Systems and the Phase Plane (differential equations, course 9)

Formed from the ten lesson dicts in `content/differential_equations/c9_systems/`
(`part_a.py`, lessons 1–5, and `part_b.py`, lessons 6–10, written by two
authors from `docs/differential-equations/PLAN.md` §C), the course dict in
`__init__.py`, the spoken forms in
`content/spoken/differential_equations_c9_systems.py`, and the pages as
`scripts/preview_subject.py differential_equations --course systems-and-the-phase-plane`
renders them, with every preset's tiles read off the built page by
`labcheck.js --observe` and every `data-say` read off the rendered HTML. The
design authority is PLAN §0 (the exactness rule), §C (course 9), §D.3 (`phase`,
`jacobian`), §D.5 and §F. The course may assume the eight courses before it and
the Algebra Subject, and nothing else. All ten lessons were read before any was
changed; the last two sections record what was changed and what was not.

Lessons, in course order: `systems-of-two-equations`,
`straight-line-solutions-and-eigenvectors`,
`the-general-solution-of-a-linear-system`, `saddles-nodes-spirals-and-centres`,
`stability-of-the-origin` | `nonlinear-systems-and-equilibria`,
`linearisation-and-the-jacobian`, `predator-and-prey`, `competing-species`,
`an-epidemic-model`. The bar marks the seam between the two authors.

## Verdict

The course teaches its subject. A reader who finishes it can read a pair of
equations as an arrow at every point and step both unknowns exactly, find the
eigenvalues from `λ² − τ·λ + Δ = 0` and one eigenvector per root from a single
equation, write and fit `C₁·e^(λ₁t)·v₁ + C₂·e^(λ₂t)·v₂` in fractions, name the
origin from `τ`, `Δ` and `τ² − 4Δ`, state the stability criterion with its two
borderline cases, find the equilibria of a polynomial system by hand and reject
a near miss with the number that rules it out, linearise at a chosen point and
say when the verdict does not transfer, and read three models whose answers are
a centre settled by a conserved quantity, a saddle that forbids coexistence, and
a line of equilibria with a threshold. Every `standard` names an act. Every
`mistakes[0]` is the §C misconception and is refuted with a specific fraction,
matrix or sign. Every pinned tile on the ten pages matched the lab, and every
figure quoted in prose agreed with the lab or with an exact recomputation.

The defects found were local and are repaired below: one false sentence about
the shape of a node's orbits, one letter used for both a vector and its first
coordinate, two key lines that the speech engine read as "tau, 0" because it
drops a tag-like `< … >` span, a product-rule derivative that read aloud as the
product of a derivative, three matrices written `2 1 / 1 2` that read "2 1 over
1 2", three key lines that were number soup aloud, three facts borrowed from
earlier courses without saying so, a kit rule misquoted twice, and small prose
faults. Nothing needs splitting, merging or reordering within the URL space the
course has; one split is recorded under remaining issues.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** "Describe
  where it goes" from a system and a start (`systems-of-two-equations`); write
  the straight-line solutions `e^(λt)·v` from the matrix alone
  (`straight-line-solutions-and-eigenvectors`); fit the general solution to any
  start and say which term wins at each end of time
  (`the-general-solution-of-a-linear-system`); classify from three exact numbers
  (`saddles-nodes-spirals-and-centres`); decide stability, borderline cases
  included (`stability-of-the-origin`); find every equilibrium by hand and say
  what a bounded search could not have found
  (`nonlinear-systems-and-equilibria`); linearise and say when the answer can be
  trusted (`linearisation-and-the-jacobian`); set up and analyse each of three
  models (`predator-and-prey`, `competing-species`, `an-epidemic-model`). None
  is "understand".
- **The exactness rule is kept and the tier is named where a number is
  reported.** Every trace, determinant, discriminant, eigenvalue, eigenvector,
  fitted constant, Jacobian entry and threshold is a fraction or a surd, and the
  three rounded figures on the course are each labelled in the sentence that
  reports them: `(−3 + √5)/2 ≈ −0.381966` and `≈ −2.61803` "rounded"
  (`linearisation-and-the-jacobian`), `3 − 2·ln 2 ≈ 1.61371`, "rounded"
  (`predator-and-prey`, twice). `(1 ± √5)/2` is printed as a surd and the lab's
  dash for its eigenvectors is explained as "a limit of the lab, not of the
  mathematics" (`straight-line-solutions-and-eigenvectors`); the same lesson
  says the lab fits constants only while they are rational.
- **The method is kept apart from the solution, with two fractions.** The
  opening lesson proves `x·y` is conserved by `x′ = x`, `y′ = −y` and shows the
  Euler polygon has `(125/64)·(27/64) = 3375/4096 = (15/16)³` instead of `1`,
  "not a slip in the arithmetic"; then `17/16 = 1 + h²` on the rotation. The
  stability lesson sets the exact ratio `5/4 = 1 + 4·h²` on the centre against
  the circle `(x² + y²)′ = 0` and says the classification is a statement about
  the equation, the polygon a method applied to it. The nonlinear lessons say
  the trajectory is drawn in floating point and that "a drawing is evidence;
  the reason is the conserved quantity" (`predator-and-prey`), and that a
  closed-looking loop "is also what a very slow spiral would look like at this
  step size".
- **Claims are stated as claims and proofs are the reader's algebra.** The
  `thm` blocks that are proved (the conserved product, where the eigenvalues
  come from, the straight-line solution, superposition, the trace–determinant
  classification, the stability criterion, `V′ = 0`, `W′ = 0`) are proved with
  the product rule, the quadratic, and substitution. The one theorem the course
  states and does not prove, linearisation near a hyperbolic equilibrium, is
  followed by a paragraph saying the lab demonstrates it on two examples and
  that the proof "belongs to a first course in dynamical systems", which
  `not_covered` repeats.
- **The misconceptions are the real ones and each is refuted with a number.**
  The phase plane is `x` against time, refuted by the table whose rows carry a
  step number and no axis; an eigenvector is a point, refuted by
  `A·(2, 2) = (6, 6) = 3·(2, 2)`; the solution through a point is the nearest
  eigenvector solution, refuted by `C₁ = 3/5, C₂ = 9/5`; a negative determinant
  means stable, refuted by `Δ = −6` with eigenvalues `−2` and `3`; one negative
  eigenvalue is enough, refuted by the single stable line out of the whole
  plane; a nonlinear system has one equilibrium, refuted by `(1, 1)`; the
  Jacobian's verdict is always the system's, refuted by `D′ = 2x⁴ + 2y⁴ > 0`
  under a centre; predators and prey settle, refuted by `V = 2` against
  `V = 3 − 2·ln 2`; competition always excludes, refuted by `(4/3, 4/3)` with
  `τ = −8/3`, `Δ = 4/3`; an epidemic ends because everyone was infected,
  refuted by `S + I − (1/2)·ln S` constant.
- **Worked example, then faded guidance.** Each lesson's worked example is the
  first preset in full; the steps are then the procedure in general ("Factor,
  pair, linearise four times, and then answer the question about the
  species"); the quiz asks for the same act on a different instance (trace `5`,
  determinant `6`; start `(3, 1)`; `τ = −4`, `Δ = 3`; eigenvalues `−3` and
  `+1`; `x′ = x² − 1`, `y′ = y`; `τ = −3`, `Δ = 1`; `(3, 0)` with rows `−3 −6`
  and `0 −1`). The progression from one model whose Jacobian is inconclusive
  (`predator-and-prey`) to one where four Jacobians settle everything
  (`competing-species`) to one where the Jacobian is degenerate everywhere and
  the equations must be read directly (`an-epidemic-model`) is the right order
  and each lesson names the one before it.
- **The figures are right.** Every pinned string matched (`labcheck`), and every
  figure in prose was recomputed in `fractions.Fraction` or checked against the
  observed tiles: `(390625/65536, 6561/65536)`, `(−31679/65536, −2415/2048)`,
  `(6561/32768, 1/128)`, `17/16`, `5/4`, `(125/64, 27/64)`, `3375/4096`;
  `1, 3` with `(1, −1), (1, 1)`; `−2, 3` with `(2, −3), (1, 1)`;
  `(1 ± √5)/2`; `C₁ = 1/2, C₂ = 1/2`; `C₁ = 3/5, C₂ = 9/5`; `C₁ = 2, C₂ = 2`;
  discriminants `25, 1, −16, −16, 0`; `1 ± 2i`, `−1 ± 2i`, `±2i`,
  `−1 (repeated)`; the zero-determinant line's `C₁ = 1/2, C₂ = 1/2` and end
  point `(257/512, 255/512)` → `(1/2, 1/2)`; `f = 0, g = −2: not an
  equilibrium`; `found 2: (0, 0), (1, 1)`; `(1/5, 1/5)` off the grid; `0 1; 1
  −1` with `(−1 ± √5)/2`; `−2 1; 1 −1` with `(−3 ± √5)/2`; `0 −1; 1 0` with
  `±i`; `0 −1; 2 0` with `±i√2`; `0 −1; 1/2 0` with `Δ = 1/2`; `−1 −2; −1 −1`
  with `Δ = −1`; `−3 −6; 0 −1`; `−1 0; −2 −2`; `−4/3 −2/3; −2/3 −4/3` with
  roots `−2, −2/3`; `found 4: (0, 0), (0, 2), (1, 1), (3, 0)`; `R₀ = 9/5; I
  peaks at S = 1/2`; `R₀ = 9/20; I falls from the start`; `R₀ = 99/50`; `0
  −9/20; 0 1/5`; and `found 65` on the `S`-axis, which is exactly the number of
  distinct `p/q` with `|p| ≤ 12`, `q ≤ 4`. `V′ = 0`, `W′ = 0` and
  `D′ = 2x⁴ + 2y⁴` were recomputed symbolically.
- **The course is better than its brief in four places.** PLAN §C's presets
  are all present and the authors added one to each of four lessons, each
  carrying a point the lesson makes: the zero-determinant line
  `[[−1, 1], [1, −1]]` (`stability-of-the-origin`), a system whose second
  equilibrium `(1/5, 1/5)` the grid cannot see
  (`nonlinear-systems-and-equilibria`), the saddle at the origin of
  Lotka–Volterra (`predator-and-prey`), and the third stable node `(0, 2)`
  (`competing-species`). The last of these is what makes "classify all four"
  honest.

## What the course taught badly, or said wrongly

1. **`the-general-solution-of-a-linear-system` said both eigenlines of a node
   are asymptotes of the orbit.** For rows `2 1` and `1 2` from `(1, 0)` the
   orbit is `(1/2)·e^(t)·(1, −1) + (1/2)·e^(3t)·(1, 1)`; its direction tends to
   `(1, 1)` but its distance from the diagonal is `e^(t)/√2` and grows without
   bound, so the diagonal is not an asymptote, and "the curve is almost on the
   line through `(1, 1)`" was false in the sense a reader would take it. The
   slow eigenline is approached at the origin end; the fast one is only run
   parallel to. For a saddle both eigenlines are approached in distance, one at
   each end of time, which is the right contrast and the second preset shows
   it. The paragraph now says this, and the third concept says "bends to run
   parallel to that eigenline".
2. **`linearisation-and-the-jacobian` used `u` for the displacement vector and
   for its first coordinate in one breath.** The key and the definition have
   `u′ = J·u` with `u = (x − x*, y − y*)`; the second concept wrote
   "`u = x − x*` and `v = y − y*`" and then "`u′ = J·u`". The concept now keeps
   `u` as the vector, writes the first-order changes in `x − x*` and `y − y*`,
   and names them as the tangent-line estimate of “The Derivative at a Point
   and the Tangent Line” made once in each unknown, which is the prerequisite
   the lesson was silently leaning on.
3. **Two key lines read aloud as "stable, tau, 0".** `stability-of-the-origin`'s
   first key line and the course's own key both wrote `τ < 0  and  Δ > 0`; the
   speech engine strips a tag-like `< … >` span, so the comparison and the
   conjunction vanished. Both now read `Δ > 0  and  τ < 0`, in the order the
   steps apply the criterion anyway. The second key line, `every Re λ < 0`,
   read "every Re lambda" and now says "real parts of both λ negative".
4. **`(x·y)′ = x′·y + x·y′` read aloud as "x times y prime equals …"**, which
   is the right-hand side's second term, not a derivative. The run is the
   product rule as the opening lesson's proof writes it; it has a spoken form
   now, "the derivative of x times y equals x prime times y plus x times y
   prime", in the same shape as the existing one for `(x² + y²)′`.
5. **Three worked examples wrote the matrix as `A =  2 1 / 1 2`**, which reads
   "2 1 over 1 2", a fraction. The course's own convention everywhere else is
   "rows `2 1` and `1 2`"; the three lines (`straight-line-solutions-and-eigenvectors`,
   `saddles-nodes-spirals-and-centres`, `stability-of-the-origin`) now follow
   it, and the one `math` block that set a matrix as a two-line array beside
   other text (so the rows interleaved with `τ = 4, Δ = 3` when read) is
   restructured one statement per line.
6. **Three key lines were unreadable aloud.** `equilibria: (0, 0) (3, 0) (0, 2)
   (1, 1)` read "0, 0 3, 0 0, 2 1, 1" (`competing-species`; now "origin, two
   axis points, (1, 1)"); `grows at first iff R₀ > 1` read "iff"
   (`an-epidemic-model`; now `R₀ = β·S₀/γ > 1:  I grows at first`); the course
   key's `stable iff` likewise (now "exactly when").
7. **Three facts were borrowed from earlier courses without saying so.** The
   rate of `ln`, used in the proofs of `V′ = 0` (`predator-and-prey`) and
   `W′ = 0` (`an-epidemic-model`), is the claim “The Integral of 1/t” made and
   Separable Equations, Growth and Decay used, and the chain rule it goes
   through was verified on polynomials only; the proof now says both in one
   sentence, and the SIR proof points back to it. The fact that a two-by-two
   system has a non-zero solution exactly when its determinant is zero is
   Algebra's Systems and Matrices (`straight-line-solutions-and-eigenvectors`,
   now cited). The real solutions for complex roots being `e^(αt)` times
   cosines and sines is “Complex Roots and Oscillation” (`stability-of-the-origin`,
   now cited). The factor `1 + h²` on the rotation was proved in “Euler on an
   Oscillator” for the same system written `x′ = v`, `v′ = −x`;
   `systems-of-two-equations` now says so instead of re-deriving it in a
   clause.
8. **The kit rule for eigenvectors was misquoted twice.** The course `how_to`
   and the definition in `straight-line-solutions-and-eigenvectors` said the
   lab prints the smallest whole-number vector "with a positive first entry";
   for a diagonal matrix the lab prints `(0, 1)`, whose first entry is zero.
   The kit's rule is "first non-zero entry positive", and both now say so, with
   `(0, 1)` and `(1, 0)` as the example.
9. **Small prose faults.** "with length `λ` times the distance" for a field
   that may point inward (now `|λ|`); "orbits move along curves that never
   turn" for a node (they bend; they do not wind round the origin); "a multiple
   of the identity has the same repeated root" (it has a repeated root, not the
   same one); "The origin is an equilibrium whenever `A` is applied to zero"
   (now "of every linear system, since `A·0 = 0`"); "we get" in a quiz `why`;
   "each rate is zero on the line or on its axis" (now "on its own line or
   where its own species is zero"); "the two species-extinct outcomes" for the
   two points lost by dividing by `x` (now "both outcomes in which the first
   species is extinct"); "the coefficient of `S·I` is `β`" when the equation
   reads `−β·S·I` (now "read `β` as the size of the `S·I` coefficient"); a
   quiz `why` in `predator-and-prey` that left the saddle distractor
   unanswered (now "A saddle would need `Δ < 0`, and here `Δ = 2`").

## What it claims to teach but does not, and where a learner gets stuck

- **`nonlinear-systems-and-equilibria` shows eight tiles and defines two.** The
  Jacobian, its trace, determinant, eigenvalues and "Linearised type" are all
  printed (and the first preset pins `saddle`) a lesson before linearisation is
  taught. The lesson's last paragraph now says that the check tile and the
  table are this lesson's and the rest are the next lesson's. The pin is
  harmless and left.
- **`linearisation-and-the-jacobian` carries the most new material in the
  course**: partial derivatives are new calculus (nothing before this lesson
  differentiates in one variable while holding another fixed), the Jacobian as
  a linear system is the hard idea, and the inconclusive case is settled by a
  second hard idea, a quantity `D = x² + y²` shown to increase along every
  solution. The course prepared the third (`systems-of-two-equations`' fifth
  step is "ask what is conserved or lost", and `stability-of-the-origin` uses
  `(x² + y²)′ = 0`), and the partial derivative is kept to the power rule on
  polynomials, which is honest and enough. It is as good as one URL makes it;
  see remaining issues.
- **The proofs of `V′ = 0` and `W′ = 0` are the only places on the course
  where a derivative is taken outside the polynomial class.** They now say
  what they borrow and from where. A reader who wants `(ln t)′ = 1/t` proved
  is told, correctly, that the Subject claims it.
- **Pairs are read aloud as bare lists.** `(1, −1), (1, 1)` is "1, negative 1,
  1, 1" and `found 4: (0, 0), (0, 2), (1, 1), (3, 0)` is "found 4, 0, 0, 0, 2,
  1, 1, 3, 0". This is the engine's convention for every Subject, and a spoken
  form keyed on `(1, 1)` would misread the same text elsewhere, so the key
  lines that depended on it were rewritten in words and the rest is recorded
  below.

## Prerequisite order

Checked backwards across the path. `systems-of-two-equations` needs Euler's
step (“Euler's Method”), the product rule (“The Product Rule”, verified on
polynomials and applied here to `x·y` as every earlier course applies it) and
the phase plane, which “Energy and the Phase Ellipse” introduced and “From
Second Order to a System” rewrote an equation into; the `1 + h²` factor is
“Euler on an Oscillator”'s, now cited. `straight-line-solutions-and-eigenvectors`
needs the quadratic formula (Algebra's Quadratics and Complex Numbers), the
determinant and the zero-determinant fact (Algebra's Systems and Matrices, now
cited) and `(e^(λt))′ = λ·e^(λt)` (“The Exponential and Its Rate” with the
chain rule, a claim the whole Subject makes). `saddles-nodes-spirals-and-centres`
and `stability-of-the-origin` need complex roots and their real solutions
(“Complex Roots and Oscillation”, now cited) and repeated roots (“Repeated
Roots”). `nonlinear-systems-and-equilibria` needs equilibria from “Autonomous
Equations” and factoring without dropping a root. `linearisation-and-the-jacobian`
introduces the partial derivative itself and now cites the tangent line it
generalises. `predator-and-prey` and `an-epidemic-model` need the rate of `ln`
(“The Integral of 1/t”, Separable Equations, Growth and Decay; now cited).
`competing-species` needs logistic growth (“Logistic Growth”) for the phrase
"grows logistically alone", which it uses as a word and does not re-derive. No
violation sits in an earlier course. Inside the course the order is right:
field, eigenlines, the sum of two eigenline solutions, the classification of the
sum, its stability; then the same five numbers applied at an equilibrium of a
nonlinear system, three times, with the Jacobian's authority shrinking at each
step (decisive, inconclusive, degenerate).

## Mathematical accuracy

- The trace–determinant classification, its proof and the table are correct,
  including the two borderline rows (`τ² − 4Δ = 0` degenerate or star;
  `Δ = 0` not isolated, kept out of the table and treated in the next lesson).
  The parabola `Δ = τ²/4` is the right dividing curve.
- The stability criterion `τ < 0` and `Δ > 0` is proved in both directions,
  with the centre named as stable and not asymptotically stable and the zero
  root named as a line of equilibria. The worked zero-determinant example is
  right: `[[−1, 1], [1, −1]]` sends `(1, 1)` to zero, the start `(1, 0)` has
  `C₁ = C₂ = 1/2` and ends at `(1/2, 1/2)`.
- The linearisation theorem is stated for the hyperbolic case only, which is
  the true statement; "centre or `Δ = 0`: inconclusive" is the complete list
  of exceptions in the plane. The cubic counterexample is right:
  `D′ = 2x⁴ + 2y⁴ > 0` off the origin, and the angular rate is `1` to leading
  order, so "unstable spiral" is the correct name for what the Jacobian calls
  a centre.
- Lotka–Volterra: equilibria `(0, 0)` saddle and `(1, 2)` centre of the
  linearisation; `V = x − ln x + y − 2·ln y` is conserved (recomputed), has its
  minimum at `(1, 2)` (both partials vanish there and `V` is convex), and the
  anticlockwise traversal with the predator peak after the prey peak follows
  from the signs of `x·(2 − y)` and `y·(x − 1)` in each quadrant about the
  point.
- Competition: all four Jacobians are right, including `(0, 0)` as an unstable
  node with roots `2, 3`; the weak-competition point `(4/3, 4/3)` has
  `τ = −8/3`, `Δ = 4/3`, discriminant `16/9`, roots `−2/3` and `−2`. The claim
  that almost every start near the saddle ends at `(3, 0)` or `(0, 2)` is the
  standard consequence of the saddle's stable curve separating the basins and
  is stated as the model's prediction.
- SIR: `R₀ = β·S₀/γ`, the peak at `S = γ/β`, the line of equilibria with
  `J = [[0, −β·S], [0, β·S − γ]]` and roots `0`, `β·S − γ`, the conserved
  `W = S + I − (γ/β)·ln S` (recomputed) and the argument that `S` stays
  positive are all right, and the lesson draws the correct conclusion that an
  epidemic ends for want of infected, not for want of susceptibles.
- The Euler facts are exact: `(1 + h)·(1 − h) = 15/16` per step on the saddle,
  `1 + h²` on the rotation, `1 + 4·h² = 5/4` on `[[0, 2], [−2, 0]]`, all three
  recomputed in `Fraction`; "sixteen steps of `h = 1/16` would stay much
  closer" is true (`(255/256)¹⁶ ≈ 0.939` against `(15/16)⁴ ≈ 0.772` at
  `t = 1`).

## The seam between part A and part B

The two authors agree on voice (careful prose, British spelling: centre,
linearise, behaviour), on "rows `a b` and `c d`" for matrices, on `τ` and `Δ`,
on the tile vocabulary including "non-isolated equilibria", which part A
introduces for `Δ = 0` and part B uses for the `S`-axis, and on citing lessons
by title in curly quotes. Part A's closing note hands over on the right
question ("what a classification says about a nonlinear equation near an
equilibrium"), and part B's first body paragraph picks it up at the right
altitude ("Where the first half of the course asked what the origin does, the
first question now is how many places there are to ask it"). The one visible
difference was that part A wrote three worked matrices as `A =  2 1 / 1 2`
while part B always wrote rows; part A now writes rows too. No vocabulary is
introduced in part B that part A should have introduced, and nothing part A
promises is left undone.

## Changes made

- `__init__.py`: the key line `stable iff  τ < 0  and  Δ > 0` is now
  `stable exactly when  Δ > 0  and  τ < 0` (the engine dropped the span
  between `<` and `>`); `how_to` says "first non-zero entry positive".
- `systems-of-two-equations`: the rotation example cites “Euler on an
  Oscillator” for `1 + h²`.
- `straight-line-solutions-and-eigenvectors`: the definition's kit rule
  corrected with `(0, 1)`, `(1, 0)` as the example; the proof cites Algebra's
  Systems and Matrices; the matrix `math` block restructured one statement per
  line with `·` for the matrix–vector products; the worked title retitled in
  words and its first line written as rows; `|λ|` in quiz 4's `why`.
- `the-general-solution-of-a-linear-system`: the "asymptotes" paragraph
  rewritten (direction against distance; node against saddle); the third
  concept's "bends towards" made "bends to run parallel to".
- `saddles-nodes-spirals-and-centres`: "never turn" made "bend but never wind
  round the origin"; "the same repeated root" corrected; the worked matrix as
  rows.
- `stability-of-the-origin`: both key lines rewritten; the proof cites
  “Complex Roots and Oscillation”; the worked matrix as rows; quiz 3's `why`
  gives `A·0 = 0`.
- `nonlinear-systems-and-equilibria`: the last body paragraph says which tiles
  are this lesson's.
- `linearisation-and-the-jacobian`: the second concept keeps `u` as the vector
  and cites the tangent line.
- `predator-and-prey`: the proof's first line names the source of the rate of
  `ln` and the status of the chain rule; quiz 1's `why` loses "we get"; quiz
  2's `why` answers the saddle distractor.
- `competing-species`: the key line in words; "on its axis" clarified; the
  lost-points mistake says which outcomes are lost.
- `an-epidemic-model`: the key line `R₀ = β·S₀/γ > 1:  I grows at first`; the
  coefficient step reads `β` and `γ` as sizes; the proof points to
  “Predator and Prey” for the rate of `ln`.
- `content/spoken/differential_equations_c9_systems.py`: a spoken form for
  `(x·y)′ = x′·y + x·y′`.

No preset, `expect`, slug, module, lab key or mode changed. Lesson slugs, count
and order are as `docs/differential-equations/COURSES.json` lists them. The
preview (`scripts/preview_subject.py differential_equations --course systems-and-the-phase-plane`)
reports OK: eleven pages, ten labs executed and swept, ten pages with pinned
figures all matching. Every key line is within 46 characters and every worked
line within 60; every lesson has exactly three concepts and three mistakes,
four to five steps, seven to eighteen body blocks and three or four quiz items
with four distinct choices.

## Remaining issues

- **`linearisation-and-the-jacobian` would be two lessons.** Partial
  derivatives and the Jacobian as a linear system are one hard idea; the
  inconclusive case, with a quantity shown to grow along every solution under
  a centre, is a second. PLAN §C puts both under one slug and the URL space is
  fixed. The natural split is "Partial Derivatives and the Jacobian" /
  "Linearisation and Where It Fails"; `predator-and-prey` would then open on
  the second. Not done.
- **The speech engine drops any tag-like `< … >` span inside a run**, so a
  comparison chain `a < 0 and b > 0` reads "a, 0" on every Subject. This course
  no longer contains the pattern, but the rule is a landmine for any author who
  writes a less-than before a greater-than in one run; it is the
  chrome-renderer tier's, not the course's.
- **Pairs read as bare comma lists** (`(1, −1), (1, 1)` → "1, negative 1, 1,
  1"; `found 4: (0, 0), (0, 2), (1, 1), (3, 0)` → a run of eight numbers). The
  engine has no reading for a parenthesised pair, and a spoken form keyed on a
  pair would misread the same text elsewhere. The key lines that depended on
  pairs were rewritten; the body runs are recorded, not changed.
- **Lowercase `a` is read aloud as "A"** (`τ = a + d`, `x′ = a·x + b·y`), the
  global engine's rule for the article, which is the same letter name as the
  matrix `A` on these pages. Recorded as on course 6; a course written for the
  ear would not use `a` for a matrix entry beside a matrix called `A`.
- **The renderer wraps math-looking fragments of plain titles**, so worked
  titles such as `x′ = x, y′ = −y from (1, 1), h = 1/4` are read in fragments.
  One title whose fragment read oddly ("to e to the power 3 t times 1") was
  retitled in words; the others read tolerably and are chrome.
- **`scripts/speechcheck.py` cannot be run for this Subject yet**: it lists the
  seven wired subjects and `differential_equations` is not in
  `GENERATED_PATHS` until the orchestrator wires it. The preview's own speech
  pass is what gated this course; `data-say` on all eleven pages was read by
  hand.
- **`nonlinear-systems-and-equilibria` pins `jbType: saddle` on its first
  preset** a lesson before linearisation is taught. The pin is correct and
  harmless, and the lesson now tells the reader which tiles are its own; it is
  recorded so that nobody hides tiles per lesson.
