# Pedagogy assessment — Oscillators, Damping and Resonance (differential equations, course 8)

Formed from the nine lesson dicts in `content/differential_equations/c8_oscillators/`
(`part_a.py`, lessons 1–5; `part_b.py`, lessons 6–9; `__init__.py`, the course
dict), the spoken forms in `content/spoken/differential_equations_c8_oscillators.py`,
and the kit they render through (`scripts/mathpath/labs/dekit_b.py`, mode
`oscillator`), on branch `feat/differential-equations` before the Subject was
wired into the site. The design authority is `docs/differential-equations/PLAN.md`
§0 (the exactness rule), §C (course 8), §D.3 (`oscillator`), §D.5 and §F; the
course was written in two parts, so the seam at lesson 6 is assessed as well.

Every lesson was read in full before anything was changed. Every pinned figure
and every figure quoted in prose was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py differential_equations --course oscillators-damping-and-resonance`),
every rounded figure was recomputed in double precision and every exact one in
`fractions.Fraction`, and every math run on the ten rendered pages was read from
its `data-say`. Lessons, in course order: `the-mass-spring-model`,
`amplitude-phase-and-period`, `energy-and-the-phase-ellipse`,
`overdamped-critical-and-underdamped`, `underdamped-motion-and-the-envelope` |
`critical-damping-and-design`, `forced-oscillation`, `resonance-and-beats`,
`damped-forcing-and-the-amplitude-curve`. The bar marks the seam between the
two authors. The course may assume Second-Order Linear Equations and everything
before it, plus the Algebra Subject; it is judged against that.

## Verdict

The course teaches its subject. A reader who finishes it can write
`m·x″ + c·x′ + k·x = 0` from two laws and read `ω₀² = k/m` and the period off
it, turn a start into an amplitude squared and a rounded phase, compute the
energy and draw the ellipse it fixes, classify a damper by the sign of
`c² − 4mk` and compute `c_crit`, read the pseudo-frequency, the envelope rate
and the peak ratio off an underdamped motion, fit a critically damped motion
and decide exactly whether it crosses zero, compute the forced amplitude with
its sign, write the resonant ramp and the beat period, and locate the finite
peak of a damped response below `ω₀`. Those are the acts the `standard` fields
measure and the tiles compute, and no objective is "understand X". The
`mistakes[0]` of every lesson is the §C misconception, each refuted with a
specific fraction, root or tile. Every pinned tile matched the lab (ninety-eight
pins over thirty-five presets on nine pages), and every figure quoted in prose
agreed with the lab or with a recomputation.

The defects found were local and are repaired below: one proof with a false
sentence at its centre (`underdamped-motion-and-the-envelope`), one area claim
that left out the mass (`energy-and-the-phase-ellipse`), two trigonometric
identities used as if the path had taught them, a seam reference to "the
previous lesson" that pointed at the wrong lesson, an ambiguous `e^(−ct/2m)` in
two key boxes, a panel that promised a drawn envelope the kit does not draw at
resonance, a rounded figure outside the exactness rule in a quiz choice, a
footer claim the kit does not honour, and three families of math runs that
read wrongly aloud. Nothing needs splitting, merging or reordering within the
URL space the course has; two splits are recorded under remaining issues.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names the output: `ω₀² = k/m`
  exactly and the period as a symbol and a rounded number
  (`the-mass-spring-model`); `C₁ = x₀`, `C₂ = v₀/ω₀`, `A² = C₁² + C₂²` exactly
  and the phase from `tan(φ) = C₂/C₁` rounded (`amplitude-phase-and-period`);
  `E₀` exactly, `E′ = v·(m·x″ + k·x) = 0`, the ellipse with its semi-axes
  (`energy-and-the-phase-ellipse`); the sign of `c² − 4mk`, the form and roots
  of each class, `c_crit` as an integer or a surd
  (`overdamped-critical-and-underdamped`); `ω_d²`, `c/(2m)`, `2π/ω_d` and the
  peak ratio marked `≈` (`underdamped-motion-and-the-envelope`); `C₂ = v₀ − r·x₀`
  and the crossing time `−C₁/C₂` with its sign (`critical-damping-and-design`);
  `A = F₀/(m·(ω₀² − ω²))` as a fraction and its sign (`forced-oscillation`);
  the ramp `(F₀/(2m·ω₀))·t·sin(ω₀t)` checked by substitution and the beat
  period (`resonance-and-beats`); `P`, `Q`, `F₀²/(P² + Q²)`, `ω_r²`, `A_max²`
  and the no-peak condition (`damped-forcing-and-the-amplitude-curve`).
- **The exactness rule is kept and the tier is named in the sentence that
  reports the number.** "The period is `2π/2 = π`, which is about `3.14159`
  and is rounded"; "`A² = 5/4` is exact. Its root `A = √5/2` is exact too, and
  the lab prints it with its rounded value, about `1.11803`, beside it"; "the
  lab prints `A² = 9/20`, an exact fraction. It prints the square and not `A`,
  because `A` is a square root"; "`A² = 2304/4097`. That is just under `9/16`:
  `2304·16 = 36864` while `9·4097 = 36873`". Every rounded figure the prose
  quotes was recomputed: `3.14159`, `3.97384`, `2.0944`, `4.44288`,
  `0.927295`, `0.463648`, `1.11803`, `4.47214`, `2.80993`, `0.0432139`,
  `0.453116`, `0.123145`, `12.5664`, `25.1327`, `4.18879`, `3.02372`, and
  `4 < √21 < 5` for the slow root `−5 + √21`.
- **The figures are right and the prose agrees with every tile.** All
  ninety-eight pinned strings match the page, and every exact figure in the
  prose was recomputed: `A² = 25`, `E₀ = 50`, semi-axes `5` and `10`, the
  start `(3, 8)` on `x²/25 + v²/100 = 1`; the discriminants `9`, `0`, `−16`,
  `84`, `−7`; `ω_d² = 4`, `63/16`, `9/4`; `C₂ = 3` and `−3` with the crossing
  at `1/3`; `A = 1`, `12/7`, `16/5`, `−3/5`, `4/5`; `B = 3/4` and the check
  `x_p″ + 4x_p = 3·cos(2t)`; `2A = 24/7` and the beat periods `4π`, `8π`,
  `4π/3`; `A² = 9/20`, `2304/4097`, `9`, `1/2`, `9/25`; `ω_r² = 3`, `31/8`;
  `A_max = 3/4`, `8√7/7`; and every quiz answer and distractor figure
  (`6/(8 − 2) = 1`, `10/(9 − 4) = 2`, `12/33 = 4/11`, `ω_r² = 5/2 − 4/8 = 2`,
  `A_max² = 9/1`).
- **Claims are stated as claims and proofs are given where the reader has
  the algebra.** The period's independence of the start, the amplitude
  squared, conservation of energy, the single crossing of a critically damped
  motion, the forced amplitude and its uniqueness, the resonant solution, and
  the steady amplitude squared are each a `thm` with a `proof` the reader can
  follow line by line. The one limit the course demonstrates and does not
  prove, that the beat envelope tends to the resonant ramp as `ω → ω₀`, says
  so: "That the ramp is the limit is what the lab demonstrates, and it is not
  proved here" (`resonance-and-beats`).
- **The misconceptions are the real ones, and each is refuted with a
  number.** Heavier is faster, refuted by `π` against `2π/√2`; the amplitude is
  the initial displacement, refuted by `x(0) = 3` and `A² = 25`; energy is lost
  at the turning point, refuted by `½·4·25 = 50 = E₀`; more damping is a faster
  return, refuted by `e^(−2t)` at `c = 4` against `e^(−t)` at `c = 5` and the
  slow root `−5 + √21` at `c = 10`; damping leaves the frequency alone, refuted
  by `ω_d² = 5 − 1 = 4` against `ω₀² = 5`; critical damping is quickest in
  every sense, refuted by the rate `1`, `3/2`, `2`, `1` across `c = 2, 3, 4, 5`
  and by the underdamped `c = 3` reaching rest in finite time; the response is
  in phase with the push, refuted by `A = −3/5`; resonance is infinite at once,
  refuted by `3t/4` at `t = 4` and `t = 40`; the damped peak is at `ω₀`,
  refuted by `9/20 < 9/16`. Every `mistakes[0]` is the §C misconception.
- **The lab's limit is stated where the lesson leans on it.** "The lab does not
  fit them, but the envelope it draws is built from them"
  (`underdamped-motion-and-the-envelope`); "`ω_r = √3` is irrational, and the
  lab takes a rational `ω`" (`damped-forcing-and-the-amplitude-curve`); "the
  lab's period tile reads the beat period of the two cosines when the natural
  frequency is rational" (`forced-oscillation`), which is exactly the kit's
  `r.beat` condition; "the lab reports the steady amplitude only"
  (`damped-forcing-and-the-amplitude-curve`), which matches a kit that prints
  no transient.
- **Worked example, then faded guidance, then independent practice.** Every
  `worked.after` names the preset the arithmetic belongs to, every panel asks
  the reader to predict a tile before reading it ("type your own frequency and
  predict the tile before you read it"; "change `c` alone in the damping box
  and find the value at which the class changes"), and the quizzes then ask
  the same act on a fresh instance (`m = 3`, `k = 12`; `x″ + 9x = 0` from
  `(0, 6)`; `m = 2`, `k = 8`; `m = 1`, `c = 6`, `k = 9`; `m = 2`, `k = 8`,
  `6·cos(t)`; `ω₀ = 4`, `ω = 7/2`; `m = 1`, `c = 1`, `k = 5/4`).
- **The progression inside each module is right.** Free motion fixes `ω₀`,
  then the amplitude, then the conserved quantity that gives the amplitude a
  second derivation (`A² = 2E₀/k`, which the third lesson's key says "the
  lab's `A²` and `E₀` agree"). Damping sorts the three kinds, then follows the
  oscillating kind, then the borderline. Forcing computes the amplitude, then
  breaks it at `ω₀`, then restores a finite peak with a damper. Each lesson's
  `note` hands to the next by title.
- **Three lessons go beyond their brief in the right direction.**
  `the-mass-spring-model` adds a `double` preset (`m = 2`, `k = 4`) so that the
  "heavier is slower" comparison is one the reader presses rather than reads.
  `overdamped-critical-and-underdamped` adds `very-over` (`c = 10`) so that the
  slow root's creep toward zero is a tile and not an assertion.
  `damped-forcing-and-the-amplitude-curve` adds `gap` (`c = 3`, underdamped,
  `c² = 9 > 2mk = 8`, no peak), which is the one instance that separates "rings
  freely" from "has a resonant peak" and is the refutation of `mistakes[1]`.

## What it taught badly, or said wrongly

### A proof with a false step

- **`underdamped-motion-and-the-envelope`, proof of "The ratio of successive
  peaks".** The second paragraph said "Peaks of `x` are the points where the
  bracket's peaks occur". They are not: `x = e^(αt)·B(t)` has `x′ = 0` where
  `α·B + B′ = 0`, not where `B′ = 0`, so each peak of `x` comes a little before
  the bracket's and the envelope touches the curve at the bracket's peaks, not
  at the motion's. The theorem is nonetheless true, for a reason the proof had
  in hand and did not use: `x(t + T_d) = e^(α·T_d)·x(t)` for every `t`
  differentiates to `x′(t + T_d) = e^(α·T_d)·x′(t)`, so a zero of `x′` at `t₁`
  gives a zero at `t₁ + T_d`, and the next peak is exactly one pseudo-period
  on and `e^(α·T_d)` times the first. The proof now says this, and says
  where the peaks actually sit.

### Facts a reader would trust that were loose or wrong

- **`energy-and-the-phase-ellipse`, body:** the area of the ellipse,
  `π·A·(A·ω₀)`, was said to be "fixed by the energy and the spring". It is
  `2π·E₀/√(mk)`, which has the mass in it. Repaired, with the closed form.
- **`energy-and-the-phase-ellipse`, quiz 2 `why`:** "A half-and-half split
  happens at one particular point on the way". It happens where `x² = A²/2`,
  at four instants in every period. Repaired.
- **`amplitude-phase-and-period`, quiz 3 `why`:** the amplitude changes when
  `v₀` is doubled "unless `x₀ = v₀ = 0`". The condition is `v₀ = 0`: a mass
  released from rest has its velocity doubled to nothing. Repaired. Quiz 2's
  `why` said `11` and `17` "add the start without squaring or without
  dividing"; it now says what each is (`3 + 8`; `9 + 8`).
- **`the-mass-spring-model`, concept 3:** "When `ω₀` is an integer the period
  is a rational multiple of `π`" — rational suffices, and the course's first
  surd preset has `ω₀ = √10/2`, which is neither. Repaired to "rational".
- **`overdamped-critical-and-underdamped`, `mistakes[1]`:** "never needs to
  cross zero" for the overdamped start `(1, 0)`. The motion
  `(4/3)·e^(−t) − (1/3)·e^(−4t)` is positive for every `t ≥ 0`; it never
  crosses. Repaired to say so.
- **`damped-forcing-and-the-amplitude-curve`, example "Typing ω near the
  peak":** "the nearest to try is `ω = 7/4`" contradicted the next sentence,
  "a rational push can come as near to the peak as you like". Now "a
  convenient one to try".

### Prerequisites the course borrowed without saying so

- **Two trigonometric identities the path has never taught.**
  `amplitude-phase-and-period` rests on the subtraction formula
  `cos(θ − φ) = cos(θ)·cos(φ) + sin(θ)·sin(φ)` and on `cos(φ)² + sin(φ)² = 1`;
  `resonance-and-beats` rests on the difference-of-cosines identity. Algebra
  has no trigonometry, and the only earlier use on the path is
  `cos² t + sin² t = 1` in “Euler on an Oscillator”, stated without comment.
  The honest handling, which the course now uses, is to call each an identity
  of trigonometry that this path takes as given and does not derive, as it
  takes the rates of sine and cosine, and to say in `resonance-and-beats`
  that its identity follows from the addition and subtraction formulas that
  “Amplitude, Phase and Period” took as given. Recorded for the PLAN below.
- **The phase plane is older than the course said.** `energy-and-the-phase-ellipse`
  introduced the plane of `x` against `v` and said only that "the next course
  returns to it in earnest"; the previous course drew it in “From Second Order
  to a System” and `euler-on-an-oscillator` stepped round it. Both sentences
  (concept 3, and the closing `note` of
  `damped-forcing-and-the-amplitude-curve`) now name that lesson.
- **`the-mass-spring-model`, `mistakes[0]`** refutes "more energy" with
  `½·k·x₀²` two lessons before energy is defined. The misconception itself
  speaks of energy, so the word belongs there; the sentence now names
  “Energy and the Phase Ellipse” as the lesson that defines it.

### The exactness rule

- `underdamped-motion-and-the-envelope`, quiz 3, offered "`e^(−π)`, about
  `0.0432`" as a choice: a rounded figure to four places with no stated rule.
  Now `e^(−π) ≈ 0.0432139`, the one rounding the Subject uses.

### Notation

- `e^(−ct/2m)` in the course key (`__init__.py`) and in the key of
  `underdamped-motion-and-the-envelope` reads as `(ct/2)·m` on the page; the
  same lesson's third key line wrote `e^(−ct/(2m))`. The course key now
  brackets the denominator, and the lesson's key is rebuilt around `α`:
  `x = e^(αt)·(…)`, `α = −c/(2m)`, `envelope ±A·e^(αt)`,
  `peaks shrink by e^(α·T_d) = e^(−c·T_d/(2m))`, which is also the notation its
  body and proof use.
- `(C₁ + C₂t)·e^(−2t)` in three places of `overdamped-critical-and-underdamped`
  against `(C₁ + C₂·t)·e^(rt)` everywhere else, including the kit's own
  `ceGeneral` tile. Now dotted, per §F.

### What the lab shows

- **`resonance-and-beats`, panel:** "watch the envelope climb in a straight
  line". The kit draws envelope curves only for a free underdamped motion
  (`osRender`: `r.type === 'underdamped' && F0 === 0`); at resonance it draws
  the motion alone. Now "watch the peaks climb in a straight line", which is
  what the reader sees.
- **Course home, `footer_lead`:** "every closed form is checked by substituting
  it, never by evaluating it". The `oscillator` kit computes `ω₀²`, the
  discriminant, `A²`, `E₀`, the forced amplitude and the rest exactly and
  prints no residual; it is the lessons that check by substitution, line by
  line, and the lab draws the motion by stepping in floating point. Repaired
  to say so.

### Speech

- Every math run on the ten rendered pages was read from `data-say`. The §D.5
  call rule works throughout: `x(0) = 3`, `x′(0) = 8`, `x(t + T_d)`, `E(t)`
  all read as calls; `ω_d`, `ω_r`, `x_p`, `T_d`, `A_max`, `c_crit` read "omega
  sub d", "x sub p", "A sub max", "c sub crit"; `2π/|ω₀ − ω|` reads "the
  absolute value of"; `≈` reads "is approximately"; `½m·v²` reads "one half m
  times v squared"; `−5 ± √21` reads "negative 5 plus or minus the square root
  of 21". `speechcheck` reports no ambiguous run and no stale spoken form.
- Three families read wrongly and were rewritten to the §F conventions rather
  than given spoken forms. `cos φ`, `sin φ`, `tan φ` and `cos²φ + sin²φ = 1`
  (`amplitude-phase-and-period`, nine runs in the key, concepts, body, proof,
  steps, worked example and standard) read as the abbreviations "cos phi",
  "sin phi", "tan phi"; with brackets they read "cosine of phi", "tangent of
  phi" and "cosine of phi squared plus sine of phi squared equals 1". The
  lowercase coefficients `a`, `b` of the damped steady response
  (`damped-forcing-and-the-amplitude-curve`, eleven runs) read as the letter
  name "A", so a listener heard "the amplitude of A cosine plus b sine is the
  square root of A squared plus b squared" with the amplitude `A` and the
  coefficient `a` as one sound; they are now `G` and `H`, letters nothing else
  in the course uses. The identity letters `a`, `b` of
  `cos(a) − cos(b) = …` (`resonance-and-beats`) had the same collision with
  `2A` in the line below and are now `θ`, `ψ`, matching the `θ` of
  “Amplitude, Phase and Period”. `content/spoken/differential_equations_c8_oscillators.py`
  stays empty and its docstring records the rewrites.
- Not changed: `C₁cos(ω₀t)` without a dot reads "C sub 1 cosine of omega sub 0
  t", which is clear, and the form is the one PLAN §C writes; `2·|A|` reads
  "2 times the size of A" where `|ω₀ − ω|` reads "the absolute value of", which
  is the global engine's choice and is understandable either way.

## Where a learner gets stuck

- **`damped-forcing-and-the-amplitude-curve` is the heaviest lesson.** It
  carries the two-coefficient response and its 2×2 system, the amplitude
  squared, the parabola in `u = ω²`, `ω_r²`, `D_min = c²·ω_d²`, `A_max`, the
  no-peak threshold `c² ≥ 2mk`, and the three-way ordering
  `ω_r² < ω_d² < ω₀²`. The quiz covers each piece and the `gap` preset earns
  the threshold, but it is two hard ideas (the steady amplitude; where it
  peaks) under one slug. See remaining issues.
- **`resonance-and-beats` carries both the ramp and the beats.** The lesson
  joins them well ("The two descriptions join…"), and PLAN §C puts both here,
  but a reader meeting `t·sin(ω₀t)` for the first time and the
  difference-of-cosines identity in the same sitting has two new tools to
  hold. See remaining issues.
- **The period tile changes meaning when a forcing is on.** From
  `forced-oscillation` onward the "Period, or beat period when forced" tile
  prints `2π` for `ω = 1` on a spring whose own period is `π`. The lesson
  warns ("One tile will look odd…") and the next lesson explains; the warning
  is in the right place and the tile label says what it is.
- **`A` means three things across the course**: the free amplitude
  (`A² = x₀² + v₀²/ω₀²`), the forced amplitude (`A = F₀/(m·(ω₀² − ω²))`, which
  may be negative), and the steady amplitude (`A² = F₀²/(P² + Q²)`). Each
  lesson defines its own and the kit's tiles keep them apart (`osAmp` against
  `osForced`), but the sign of the forced `A` against the `A ≥ 0` of the
  definition in `amplitude-phase-and-period` is a point a reader may trip on;
  `forced-oscillation` handles it by calling `|A|` the size and the sign the
  direction, which is right.
- **Nothing is stepped.** This is the one `dekit` course with no exact Euler
  column, so the material clause's "exact arithmetic applied to an approximate
  method" has no bite here; the lessons instead keep "the curve is drawn by
  stepping in floating point; the tiles are exact" in every panel, which is
  the honest version for this course.

## Prerequisite order

Checked backwards across the path. `the-mass-spring-model` needs the general
solution of `x″ + ω₀²·x = 0` (“Complex Roots and Oscillation”, cited) and the
periodicity of sine and cosine (“Sine, Cosine and Their Rates”).
`amplitude-phase-and-period` needs the two-constant fit (“Fitting the Initial
Conditions”) and two trigonometric identities, now stated as given.
`energy-and-the-phase-ellipse` needs the chain rule on a square (“The Chain
Rule” in Rates of Change and the Derivative) and the phase plane (“From Second
Order to a System”, now cited). `overdamped-critical-and-underdamped` and
`critical-damping-and-design` need the three root cases (“The Characteristic
Equation”, “Repeated Roots”, cited). `forced-oscillation` needs undetermined
coefficients and `y_p + y_h` (“Exponential and Sinusoidal Forcing”,
“Homogeneous Plus Particular”, cited) and the resonant guess with a factor of
`t`, which that course taught for first order and “Repeated Roots” for second.
`damped-forcing-and-the-amplitude-curve` needs a 2×2 linear system solved by
elimination (Algebra's Systems and Matrices) and the amplitude of
`G·cos + H·sin` (“Amplitude, Phase and Period”, cited). No violation sits in
an earlier course. Inside the course the order is right: frequency, then
amplitude, then energy; classification, then the oscillating case, then the
border; the forced amplitude, then its failure, then its repair.

## Mathematical accuracy

- `ω₀² = k/m`, `T = 2π/ω₀`, the surds `√10/2`, `√2`, `2√5`, `2√10`, `4√2`
  and the `c_crit` tile: all right, and the "heavier is slower" direction is
  stated correctly in every place it appears.
- `C₁ = x₀`, `C₂ = v₀/ω₀`, `A² = C₁² + C₂²`, the phase in the quadrant of
  `(C₁, C₂)`, the lag `φ/ω₀`, the check that `3cos(2t) + 4sin(2t)` peaks at
  `9/5 + 16/5 = 5`: right.
- `E = ½m·v² + ½k·x²`, `E′ = v·(m·x″ + k·x)`, `E′ = −c·v²` with a damper,
  `A² = 2E₀/k`, the ellipse `x²/A² + v²/(A·ω₀)² = 1`, clockwise traversal:
  right.
- The discriminant classes, `c_crit = 2√(mk)`, the roots `−1, −4`, `−2`
  twice, `−1 ± 2i`, `−5 ± √21`, the product of the roots `k/m`, the long-run
  rate rising to `c_crit` and falling past it, at most one zero in the
  overdamped and critical cases: right.
- `ω_d² = k/m − c²/(4m²)`, `α = −c/(2m)`, `x(t + T_d) = e^(α·T_d)·x(t)`, the
  peak ratios `e^(−π)`, `e^(−2π/√63)` and `e^(−2π/3)` (printed `≈ 0.0432139`,
  `≈ 0.453116`, `≈ 0.123145`), and the envelope amplitude the kit builds from
  `C₁ = x₀`, `C₂ = (v₀ − α·x₀)/ω_d`: right; the proof's claim about where the
  peaks sit was wrong and is repaired.
- `C₂ = v₀ − r·x₀`, the crossing at `−C₁/C₂` when positive, the door released
  from rest never crossing, `x′ = (6t − 5)·e^(−2t)`, `x″ = (16 − 12t)·e^(−2t)`
  and the zero residual: right.
- `A = F₀/(k − m·ω²)`, the sign by `ω` against `ω₀`, the whole motion from
  rest `cos(t) − cos(2t)` and `−(3/5)·cos(3t) + (3/5)·cos(2t)`, the limits
  `F₀/k` and `0⁻`: right.
- The resonant `x_p″ = 2B·ω₀·cos(ω₀t) − B·ω₀²·t·sin(ω₀t)`, `B = F₀/(2m·ω₀)`,
  the identity with `θ`, `ψ`, `x = (24/7)·sin(7t/4)·sin(t/4)`, the beat period
  `2π/|ω₀ − ω|` against the sine factor's `4π/|ω₀ − ω|`, the small-`t`
  envelope `F₀·t/(m·(ω₀ + ω))` tending to the ramp: right.
- `P·G + Q·H = F₀`, `−Q·G + P·H = 0`, `G² + H² = F₀²/(P² + Q²)`,
  `D = m²u² + (c² − 2mk)u + k²`, `ω_r² = k/m − c²/(2m²)`, `D_min = c²·ω_d²`,
  `A_max = F₀/(c·ω_d)`, no peak when `c² ≥ 2mk`, `(u + 4)²` for `c = 4`,
  `k = 4`, `2304/4097 < 9/16`: right.

## The seam between part A and part B

The two authors agree on voice (careful prose, British spelling: `centred`,
`behaviour`, `modelling`), on the entity conventions in prose fields, on the
tile vocabulary and on the notation for products and exponentials. Part A's
closing `note` hands over correctly ("The border between this lesson and the
one before it… is a choice in engineering, taken up in “Critical Damping and
Design”"), and part B's `concepts_intro` picks up at the right altitude. The
one seam defect was part B's opening sentence, "The previous lesson sorted
dampers into three kinds", which was true of the lesson before the previous
one; it now names “Overdamped, Critical and Underdamped” and says the lesson
after it followed the underdamped kind. Part A wrote `(C₁ + C₂t)` in three
places and part B `(C₁ + C₂·t)` throughout; part A now matches.

## Changes made

- `__init__.py`: the key line `e^(−ct/(2m))`; `footer_lead` no longer claims
  the lab checks by substitution.
- `the-mass-spring-model`: "rational" for "an integer" in concept 3;
  `mistakes[0]` names the lesson that defines energy.
- `amplitude-phase-and-period`: `cos(φ)`, `sin(φ)`, `tan(φ)`,
  `cos(φ)² + sin(φ)² = 1` in the key, concepts 2 and 3, the body paragraph
  and math block, the proof, the surd example, step 5, the worked line and the
  standard; the subtraction identity stated as taken as given; quiz 2 and
  quiz 3 `why`.
- `energy-and-the-phase-ellipse`: concept 3 names “From Second Order to a
  System”; the area as `2π·E₀/√(mk)` with the mass; quiz 2 `why`.
- `overdamped-critical-and-underdamped`: `C₂·t` in the key, the long-run
  paragraph and quiz 4 `why`; `mistakes[1]` "never crosses zero".
- `underdamped-motion-and-the-envelope`: the key rebuilt around `α`; the
  proof's second paragraph rewritten; quiz 3's rounded choice.
- `critical-damping-and-design`: the opening sentence names the lesson it
  means.
- `resonance-and-beats`: the identity in `θ`, `ψ` with its status; the panel
  says "peaks", not "envelope".
- `damped-forcing-and-the-amplitude-curve`: `G`, `H` for the response
  coefficients in concept 1, both math blocks, the proof and the example; "a
  convenient one to try"; the closing `note` credits “From Second Order to a
  System”.
- `content/spoken/differential_equations_c8_oscillators.py`: no entries; the
  docstring records what was rewritten instead.

No preset or `expect` changed. Lesson slugs, count, order, modules, lab keys
and modes are as `docs/differential-equations/COURSES.json` lists them.
`scripts/preview_subject.py differential_equations --course oscillators-damping-and-resonance`
reports OK: ten pages, nine labs executed and swept, nine pages with pinned
figures all matching, no math run without a spoken form, none ambiguous.

## Remaining issues

- **`damped-forcing-and-the-amplitude-curve` would be two lessons.** The
  steady response with its 2×2 system and `A² = F₀²/(P² + Q²)` is one hard
  idea; the amplitude curve, `ω_r²`, `A_max` and the no-peak threshold are
  another. PLAN §C puts both under one slug and the URL space is fixed. If
  the Subject is ever re-cut, "The Steady Response" / "The Amplitude Curve and
  Its Peak" is the natural split, and the `gap` preset belongs to the second.
  Not done.
- **`resonance-and-beats` would be two lessons** for the same reason:
  "Resonance" (the failed guess, the ramp, the check) and "Beats" (the
  identity, the envelope, the beat period, the limit). Not done.
- **Three trigonometric identities are taken as given on the path**: the
  subtraction formula, `cos² + sin² = 1`, and the difference-of-cosines
  identity, with the first use of `cos² t + sin² t = 1` in “Euler on an
  Oscillator” (course 7) unannounced. The lessons now say they are given; the
  PLAN could instead give “Sine, Cosine and Their Rates” one `thm` stating the
  Pythagorean identity and the addition formulas as the demonstrated claims
  the Subject uses, so that every later use has a title to cite. A PLAN
  change, not a course one.
- **The resonant ramp has no drawn envelope.** The kit draws `±A·e^(αt)` for a
  free underdamped motion and nothing for the forced cases, so the reader of
  `resonance-and-beats` sees the peaks climb but not the line `±3t/4` they
  climb along, and the reader of the beats presets sees no `±(24/7)·sin(t/4)`.
  Both lines are closed forms the kit has in hand. A kit change for
  `@lab-arithmetic`; the panels now describe what is drawn.
- **`A` is overloaded** across the three modules (free, forced and steady
  amplitude). Each lesson defines its own and the tiles keep them apart; a
  reader who carries `A ≥ 0` from “Amplitude, Phase and Period” into
  “Forced Oscillation” meets `A = −3/5` and is told the sign is a direction,
  which is right but is a second meaning. Recorded, not changed: PLAN §C fixes
  the notation.
