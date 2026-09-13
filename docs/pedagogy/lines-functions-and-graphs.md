# Pedagogy assessment — Lines, Functions and Graphs (algebra, course 3)

**Second assessment. It supersedes
`docs/pedagogy/prior/lines-functions-and-graphs.md` and it changes no source.**
Nothing under `content/` or `site/` was edited in this pass: the prose is settled
and a downstream contract snapshot is pinned to it. Everything below that would
have been a repair is written as a recommendation precise enough to execute
later. One finding is a live defect on a shipped page (item 12) rather than a
pedagogical one, and it is flagged as such.

Formed from all fourteen lesson dicts in `content/algebra/c3_functions/`
(`part_a.py`, `part_b.py`, `__init__.py`), the course home, every mode of the
`grapher`, `line`, `transform`, `funcops` and `system` labs those lessons attach
in `scripts/mathpath/labs/algebra_functions.py` and
`scripts/mathpath/labs/algebra_systems.py`, and the page shape in
`scripts/mathpath/render.py`, `scripts/mathpath/labs/common.py` and
`scripts/mathpath/theme.py`, as they stand on `review/course-ui-standardization`
at `d0a238a`. (The branch tip has since moved to `19b6b0b`, which carried the
supersession move itself along with a test-suite change; it touched nothing under
`content/` or `scripts/`, so every line cited below is unchanged at the tip.)
No lesson was sampled; every `body` block, `concepts` card, `steps`
entry, `worked` panel, `quiz` item, `mistakes` row, `standard` and `lab` panel
was read, and every preset the lessons select or supply was read against the
lesson text and against the controls that receive it.

The order is the one `__init__.py`'s `_LESSON_ORDER` ships, with
`linear-inequalities-in-two-variables` moved to seventh by the first pass:
`the-coordinate-plane`, `graphing-a-linear-equation`, `slope`,
`slope-intercept-form`, `point-slope-and-standard-form`,
`parallel-and-perpendicular-lines`, `linear-inequalities-in-two-variables`,
`what-a-function-is`, `function-notation`, `domain-and-range`,
`piecewise-functions`, `transformations-of-graphs`, `composition-of-functions`,
`inverse-functions`. Declared prerequisites are Courses 1 and 2; factoring is
course 4, rational and radical algebra course 5, quadratic graphs course 6, and
that published order is the standard used here.

## What the course teaches well

- **`graphing-a-linear-equation`'s `worked.after` contains the single best
  paragraph in the three Algebra courses I read.** The lesson's third point
  `(3, 2)` falls exactly midway between the two intercepts, and instead of
  presenting that as confirmation the page says what it is and then destroys it:
  "Misread the constant as `24` and you get `(12, 0)`, `(0, 8)` and `(6, 4)`,
  which pass the midway check just as cleanly while every one of them is wrong
  for this equation. Correctness still rests on the substitutions: a third point
  can reveal an error, not certify its absence." All three of those figures
  check. That is the epistemics of a check, taught on the page where a learner
  first has a check to misuse.
- **`transformations-of-graphs` replaces four verbal moves with one computation
  and proves the part everyone memorises.** The `proof` block solves `x − 3 = t`
  for `x` and says where the sign inversion comes from — "That single
  rearrangement is the entire reason horizontal effects are inverted" — and the
  point map `(x₀, y₀) → (x₀/b + h, ay₀ + k)` is then the method, the worked
  example, the `standard` and the lab's table. The lesson supplies its own
  presets and the "all four constants" one, `"ab|-4|2|3|5"`, is exactly the
  worked example `−2|x − 3| + 5` once the `tfHint`'s half-step slider units are
  read. The first pass's finding 13 is discharged and I verified the encoding.
- **`composition-of-functions` puts the domain before the simplification and
  supplies the presets that make the point.** `(√x)² = x` has domain `[0, ∞)`,
  the `body` says why — "`g(−1)` never produces a real number, so `f` is never
  reached" — and the lesson's own preset list carries `x^2|sqrt(x)` under the
  label "A square after a root: hidden domain" alongside `2x + 3|x - 4` and
  `sqrt(x)|x - 5`, which are the two worked examples. Lesson and lab agree
  exactly, which is not true of most of the course.
- **`what-a-function-is` demands a witness rather than a verdict.** `steps[3]` —
  "'Not a function' is half an answer. 'Not a function: `x = 4` gives both `2`
  and `−2`' is the whole one" — is repeated in `mistakes[2]`, enforced in the
  `standard`, and matched by the lab, which "groups points by input or searches
  for a witness, then draws the vertical line through the repeated input it
  actually found." The lesson also closes three earlier loose ends at once: a
  vertical line has no slope, cannot be written `y = mx + b`, and is not a
  function, "all three because a single `x` is paired with many `y`."
- **Two true-but-irrelevant distractors are handled the way the content
  package's `AGENTS.md` asks.** `inverse-functions` question 1 offers "Because
  `x²` is never negative" against "why does `x²` have no inverse", and the `why`
  concedes it outright — "the first choice describes the range and is true but
  irrelevant — `x³` has range every real number and `√x` has range `[0, ∞)`, and
  both are invertible." `linear-inequalities-in-two-variables` question 3 does
  the same for "Because the origin belongs to no quadrant": "The first is true of
  the origin but irrelevant." Conceding a true option and separating truth from
  relevance is the correct move and it is rare.
- **The first pass's reorder reads correctly from both ends.**
  `linear-inequalities-in-two-variables`' `note` says "That closes the line
  block. 'What a Function Is' changes the question…", and
  `what-a-function-is`' `concepts_intro` says "The first seven lessons used
  points and lines as solution sets." Both sentences are true only in the new
  order, and neither is true in the old one.
- **`piecewise-functions`' two corrected claims verify.** The overlap criterion
  is now "conflicting outputs are what violate the function definition" rather
  than "must not overlap", and the `10` claim reads "The number `10` is in fact
  produced elsewhere by this function" — which it is, at `x = −11`, since the
  first piece is `−x − 1` on `x < −1`. The first pass's findings 9 and 10 are
  discharged and both were checked.
- **`domain-and-range`, `composition-of-functions`, `inverse-functions`,
  `transformations-of-graphs` and `linear-inequalities-in-two-variables` all
  override the shared lab's presets from the lesson dict rather than accepting
  the defaults.** `domain-and-range`'s override is the clearest case: the shared
  `FUNCOPS_PRESETS["domain"]` carries `(x + 1)/(x^2 - 4)` and
  `(x^2 - 4)/(x - 2)`, both of which need factoring, and the lesson replaces them
  with five that do not, matching its own statement that "Producing such a
  factorisation is Polynomials and Factoring work, not a hidden prerequisite
  here." That is the right mechanism and it is used well in five places.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **`function-notation`'s lab teaches `transformations-of-graphs`' contrast
   three lessons early, and does not teach this lesson's.** The `funcops`
   notation mode's headline table is titled "f(x + 1) is not f(x) + 1"
   (`algebra_functions.py:2578` and `:2613`), its KPI row is
   `("f(a)", "f(x + 1)", "f(x) + 1")`, and the lesson's panel advertises it: "The
   panel also computes `f(x + 1)` and `f(x) + 1` separately." Inside versus
   outside is `transformations-of-graphs`' whole subject at lesson 12.
   `function-notation`'s own theorem is a different statement — "Functions do not
   distribute": `f(a + b)` against `f(a) + f(b)` — and the lesson works it in
   full (`f(a + 1) = a² − 2a + 2` against `f(a) + f(1) = a² − 4a + 7`, agreeing
   only at `a = 5/2`, which checks). The lab has no row for it. The lesson's
   theorem has no lab and the lab's contrast has no lesson until three pages
   later.
2. **`slope`'s central theorem rests on similar triangles, which are on no
   course of this path.** The `thm` "Slope is well defined" argues "Two choices
   of point pair produce similar right triangles … and similar triangles have
   proportional sides, so the ratio rise/run agrees", and the lesson then says
   the theorem is "the reason a single number can stand in for a whole line's
   steepness in every formula that follows."
   `parallel-and-perpendicular-lines` reaches for the same geometry: "a quarter
   turn swaps the horizontal and vertical legs of the slope triangle." Neither
   the Algebra path's `__init__.py` nor its `prerequisites` list mentions
   geometry, and the course's `assumes_long` is "solving and rearranging linear
   equations". This is not a reason to change the argument — it is a good one —
   but it is an unstated prerequisite doing load-bearing work, and nothing on the
   page says so.
3. Not a violation, but worth recording because it is the one the course could
   easily have had: `domain-and-range` uses interval notation from its first
   `key` line and solves `9 − x² ≥ 0` by rewriting it as `|x| ≤ 3`. Both are
   Course 2, lessons 13 and 12, and both are declared prerequisites. The lesson
   cites them by name in `body` and in `mistakes[2]`.

### Facts a reader would trust that are wrong

4. **`parallel-and-perpendicular-lines`' third quiz question asks about one line
   and its correct answer names a different one.** The stem is "Why does the
   product test fail to show that **`x = −2`** and `y = 5` are perpendicular?" and
   the correct option, index 1, reads "**`x = 3`** has no slope, so there is no
   product to form." `x = 3` appears nowhere else in the lesson. The `why`
   half-covers the seam — "neither passing through the origin nor the particular
   constants matter" — which is a sentence that only makes sense if someone
   noticed the mismatch and decided to work around it.
5. **`domain-and-range`'s faded rehearsal asks the reader to do something the
   definition of a function forbids.** `worked.after[2]` ends: "Then find the
   range of `t(x) = |x + 1| − 3` from its minimum and **show an input that
   produces two different allowed output values**." No input of a function does
   that, `t` is a function, and `what-a-function-is` is two lessons earlier and
   exists to say so. The act the sentence was reaching for is the mirror image —
   two inputs sharing one output, `x = 0` and `x = −2` both giving `−2` — which
   is the property that costs `t` its inverse in lesson 14.
6. **`linear-inequalities-in-two-variables` question 2 misassigns its fourth
   distractor's error.** Solving `2x − 4y > 12` gives `y < (1/2)x − 3`, and the
   `why` says "the fourth gets the constant sign wrong." Option (d) is
   `y < −(1/2)x − 3`: the constant `−3` is correct and it is the `x`-coefficient
   whose sign is wrong. The third option's diagnosis in the same sentence is
   right.
7. **`point-slope-and-standard-form` question 1 invents a derivation for an
   unreachable distractor.** For the line through `(2, 5)` with slope `−4` the
   answer is `y = −4x + 13`, and the `why` says "`y = −4x + 22` adds `5` and `8`
   twice." `5 + 8` twice is `26`; `5 + 8 + 8` is `21`. I enumerated the natural
   mis-derivations of the intercept from `y − 5 = −4(x − 2)` and the reachable
   values are `13`, `3`, `−3`, `−13` and `26`; `22` is not among them. The
   distractor has no error behind it and the feedback supplies one that does not
   compute.

### Distractors that are also true

8. **None that the feedback does not already concede.** I tried to argue for each
   of the course's forty-two wrong answers. Two are true statements —
   `inverse-functions` q1(a) and `linear-inequalities-in-two-variables` q3(a) —
   and both are explicitly granted and separated from relevance by their `why`
   (quoted above). Three more come close and are closed on the page:
   `what-a-function-is` q2(c) ("the range has fewer elements than the domain"),
   whose premise is true and whose conclusion the `why` refutes;
   `piecewise-functions` q3(a), an overlap that is harmless because both formulas
   give `3` at `x = 1`, which the `why` says; and `graphing-a-linear-equation`
   q3(c) ("The axes are scaled differently"), closed by "unequal axis scales
   stretch a line but never bend it." This is the strongest single property of
   the course and it is the standard courses 1 and 2 should be held to.

### Labs that do not agree with their own lessons

9. **`function-notation`'s lab opens on a function the lesson never mentions,
   and the lesson's own function is not in the preset list at all.**
   `FUNCOPS_PRESETS["notation"]`'s first entry is `2x^2 - 5x + 1`, which is what
   the page loads with; the lesson's `f(x) = x² − 4x + 5` runs through its `body`,
   its worked panel, all three quiz questions and its `standard`, and does not
   appear among the six presets. The lesson does not override `presets`, although
   five of its siblings do. See also item 1: what the lab computes is the wrong
   contrast as well as the wrong function.
10. **`composition-of-functions`' own preset contradicts its own concept card.**
    `concepts[1]` says "Composition is not commutative even when both functions
    and both composites are lines", and the preset list the lesson supplies
    contains `("Two shifts: this pair commutes", "x + 1|x + 2")` — two lines
    whose composites agree. The lab is right and the concept card, read as
    written, is refuted by a preset the lesson itself chose. Nothing in the panel
    reconciles them.
11. **`graphing-a-linear-equation` and `slope-intercept-form` run the lab in the
    opposite direction to the lesson, and it hands over the act the `standard`
    measures.** Both lessons take an equation and ask the reader to produce
    something: lesson 2's `steps[1]`/`[2]` are "Set y = 0 and solve for x" and
    "Set x = 0 and solve for y", and its `standard` is "graph any `ax + by = c`
    from its intercepts"; lesson 4's `steps` are the isolation of `y` and its
    `standard` is "convert any non-vertical line to `y = mx + b`". The `line`
    lab's `graph` and `forms` modes take two points from four coordinate selects
    and print the intercepts, the table and all three forms. There is no way to
    enter `2x + 3y = 12`, and the lab computes for free exactly what both
    completion standards ask for. Neither panel says so; lesson 2's says "The
    line, its two intercepts and the table of values are all computed from the
    points you choose."
12. **`point-slope-and-standard-form`'s lab loads in an error state, because two
    of its six presets set a coordinate the control cannot hold.** The line lab
    builds its coordinate selects from `range(-8, 9)`
    (`algebra_functions.py:630`), and `LINE_PRESETS["pointslope"]` contains
    `("(2, 5) and (6, 13)", "2|5|6|13|2|-3")` and
    `("(2, 3) and (2, 9): vertical", "2|3|2|9|2|-3")`. The preset handler does
    `selY2.value = parts[3]`; setting a `<select>`'s value to an option that does
    not exist deselects every option, so `selY2.value` becomes `""`,
    `readR("")` returns `null` (`Rparse` returns `null` on anything that is not a
    number), and `redraw()` takes the branch that prints "**Both coordinates of
    both points are needed.** Choose a whole number for each of the four" with an
    empty work panel and no line. The first of the two is the default preset, so
    that is the state the page loads in; the second is the vertical case, which
    is the lesson's `quiz[2]` and one of the three forms the lesson exists to
    compare. I scanned all thirty coordinate pairs across the five `line` modes:
    these two are the only ones out of range, and the mode is used by this lesson
    alone. This passes `labcheck.js` because the lab degrades to an explanation
    rather than throwing.
13. **`slope`'s panel says the well-definedness theorem is "checked rather than
    asserted" by an action the controls do not support.** The panel reads "Slide
    the two points along the line without leaving it and the slope does not move
    — that is the well-definedness theorem, checked rather than asserted." The
    controls are four `<select>` elements of integers; there is no slide, and
    staying on the line means finding another integer lattice point on it by
    hand. On the default preset, `(0, 0)` to `(4, 3)`, that means multiples of
    `(4, 3)` and the only other reachable one is `(8, 6)`. The lesson's own
    worked example does the check properly — `(−2, 1)`, `(4, 10)` and `(0, 4)`,
    all giving `3/2` — and `(4, 10)` cannot be entered at all, since the selects
    stop at `8`.
14. **`piecewise-functions` accepts the default presets and preset 6 is its own
    quiz question 3 with the formulas swapped.** `FUNCOPS_PRESETS["piecewise"]`'s
    last entry is `("an overlap: two values at x = 2", "x on (-inf, 2]; 5 - x on
    [2, inf)")`, which gives `2` and `3` at the cut; question 3's correct answer
    is `{x + 1 if x ≤ 2; 4 − x if x ≥ 2}`, which gives `3` and `2`. The lesson's
    own three-piece function — printed in its `key`, its `body` and its `worked`
    — is not among the six presets, although the formula field is free text and
    would accept it.
15. `inverse-functions` overrides its presets, which is right, and then picks
    two that are not the lesson's: the line preset is `2x + 3` where the worked
    example and every check on the page use `3x − 7`, and the constant preset is
    `3` where the faded rehearsal says "explain why the horizontal line
    `h(x) = 4` cannot pass the same test."
16. `the-coordinate-plane`'s six worked points are not a preset, and the two
    presets that are not about quadrants — "a 3-4-5 triangle" and "a distance
    that is irrational" — are correctly fenced by the panel as "previews, not
    completion work here". The fence is good; the absence of the lesson's own
    data is the same pattern as items 9, 13 and 14.

### Quiz feedback that does not answer the wrong answer

17. **`parallel-and-perpendicular-lines` question 1 identifies distractors by a
    number the page does not print, and leaves the most tempting one
    unaddressed.** The `why` is "Flip and negate: `2/5` becomes `−5/2`, and
    `(2/5)(−5/2) = −1`. Option 2 flips without negating; option 4 negates without
    flipping." `common.py`'s `QUIZ_SCRIPT` renders each choice as
    `<button class="choice">` with `b.innerHTML = text` and no index, and
    `theme.py:721` makes `.choice-grid` a bare one-column grid with no counter,
    so nothing on screen is numbered 2 or 4. And option 1 is `2/5` — the
    *parallel* slope offered against a perpendicular question, which is the error
    the lesson's `mistakes[0]` is about — and the `why` never mentions it.
18. **`graphing-a-linear-equation` question 2 never names the confusion its
    second option is made of.** The item is "What does the graph of `x = 5` look
    like?" and option (b) is "A horizontal line through `(0, 5)`" — `x = 5`
    mistaken for `y = 5`, which is `mistakes[2]`'s subject and the lesson's
    stated reason for teaching the two special shapes. The `why` addresses (a)
    and (d) and stops.
19. `the-coordinate-plane` question 1's `why` is two sentences and answers one of
    three distractors: "`x` is negative and `y` is positive, which is the upper
    left. Quadrant III would need both negative." Quadrants I and IV are not
    mentioned. Question 3's `why` never addresses "The equation has no graph".
20. `point-slope-and-standard-form` question 1 invents `22`'s derivation
    (item 7); question 2's `why` explains the correct answer and none of its
    three distractors individually.
21. `slope` question 2's `why` says the option `1` "is not produced by either
    difference." That is a statement that the option is arbitrary, not a
    diagnosis of a reader's reasoning, and it is the only one of the course's
    forty-two explanations that admits the distractor is filler.
22. `linear-inequalities-in-two-variables` question 2 misassigns option (d)
    (item 6). Its question 1 answers three distractors as a block — "The other
    three points each give `6`" — which is true (all of `(0, 6)`, `(2, 0)` and
    `(3, −3)` give `6`) and is the one place a block answer is better than three
    separate ones, because the block *is* the insight.

### Cognitive load and structure

23. **The quiz and the worked example are the two cells of one `grid-2`, so the
    faded rehearsal the first pass added sits beside the question it was meant to
    precede.** `render.py`'s `#practice` section emits `labs.QUIZ_MARKUP` and the
    worked panel — including every paragraph of `worked.after` — inside a single
    `<div class="grid-2">`. The collisions:
    - `domain-and-range`: the faded item is "take `s(x) = √(x + 2)/(x − 4)`" and
      question 1 is "What is the domain of `f(x) = √(x + 2)/(x − 4)`?" — the same
      function, with the root condition `x ≥ −2` supplied in the faded text. The
      second half of the same faded paragraph is "find the range of
      `t(x) = |x + 1| − 3` from its minimum", and question 2 is the range of
      `g(x) = |x + 3| − 4`.
    - `slope`: question 1 is "What is the slope through `(1, 7)` and `(3, 1)`?",
      and `−3` is printed twice in the `body` above it — once in the `example`
      ("`(1, 7)` to `(3, 1)`: `−6/2 = −3`, falling") and once in the closing
      paragraph ("`−3` passes the glance").
    - `transformations-of-graphs`: question 2 is the `example` block verbatim —
      "`(4, −2)` lies on `y = f(x)` … `y = 3f(x − 5) + 1` … `(9, −5)`" — including
      both coordinates of the answer.
    - `composition-of-functions`: question 1 uses `f(x) = 3x − 1` and
      `g(x) = x + 2`, which are the faded rehearsal's `u` and `v` renamed.
    This is the first pass's own finding 7 reappearing in a new place: the repair
    moved the recognition target from the worked example to the faded rehearsal,
    and the layout puts the two side by side.
24. **`transformations-of-graphs` is still the heaviest page and the decision not
    to split it is now defensible.** It carries four constants, two reflections,
    two scalings, the factoring step, a proof, a coordinate map and two worked
    formulas. What changed is that the map is now the organising idea rather than
    a seventh thing, and the `standard` requires mapping at least three points
    and verifying one in the rule — which is the check the first pass's finding 8
    asked for and did not get. Recorded as a judgement; not recommended for a
    split.
25. **`domain-and-range` carries domain, range, interval notation and the
    "an excluded input removes an output" example.** It is the second-heaviest
    page. I do not recommend splitting it: the range half is three short tools
    (non-negativity, track the outer operation, solve for the input), the
    `standard` measures both halves, and the lesson's own `body` says why they
    are different kinds of question. Recorded as a judgement.
26. **Two of the fourteen lessons appear in no course outcome.** `__init__.py`'s
    four `outcomes` cover the line forms, the function definition, domain and
    range, and transform/compose/invert. `piecewise-functions` is absent, and so
    is `linear-inequalities-in-two-variables` — which the first pass deliberately
    promoted to lesson 7, which closes the line block, and which
    Systems and Matrices' feasible region is built on (its own `note` says so).
    A reader deciding whether to take the course is not told it teaches either.
27. The `syllabus_intro` still describes the pre-reorder shape in one respect:
    "Lines and the half-planes they bound come first. 'What a Function Is'
    defines a function; the rest of the course develops its notation, domain and
    range, piecewise rules, graph transformations, composition and inverse." That
    is accurate. `not_covered` is accurate too. No finding; checked because the
    reorder was the first pass's biggest structural change and this is where a
    stale sentence would have survived.

## Where a learner gets stuck

- At `point-slope-and-standard-form`'s lab, on load, in front of "Both
  coordinates of both points are needed" and an empty panel, on a lesson whose
  entire method is a two-point construction (item 12). Selecting the vertical
  preset, which is the lesson's third quiz question, produces the same banner.
- At `parallel-and-perpendicular-lines` question 3, reading an answer about
  `x = 3` to a question about `x = −2` (item 4).
- At `domain-and-range`'s faded rehearsal, asked for an input with two outputs
  two lessons after being taught that no such input exists (item 5).
- At `function-notation`'s lab, in front of `2x² − 5x + 1` — which the lesson
  never mentions — computing a contrast between inside and outside that the
  lesson does not teach and will not teach for three more pages, while the
  theorem the lesson does prove has no row (items 1, 9).
- At `slope`'s lab, told to slide two points along a line that has four integer
  dropdowns, and unable to enter the worked example's `(4, 10)` at all (item 13).
- At `composition-of-functions`' second preset, watching two lines commute
  immediately after reading that composition "is not commutative even when both
  functions and both composites are lines" (item 10).
- At `parallel-and-perpendicular-lines` question 1, having answered `2/5` — the
  parallel slope — and receiving feedback that names options 2 and 4 on a page
  that numbers nothing (item 17).
- At `graphing-a-linear-equation`'s and `slope-intercept-form`'s labs, watching
  the widget produce the intercepts and the slope-intercept form that the
  completion standard asks the reader to produce (item 11).

## What the first pass caught, what it missed, and what I dispute

The prior assessment was the strongest of the three I superseded and most of its
repairs verify. The prerequisite excisions landed: `function-notation` has no
factoring, no discriminant and no difference quotient; `domain-and-range`
supplies multi-zero denominators already factored and says so in `steps[0]`;
`transformations-of-graphs` uses a line, `|x|` and `x³` and fences the root and
reciprocal parents in its `def` as "not part of this lesson's completion
standard"; `composition-of-functions`' hidden-domain example is `(√x)²`;
`inverse-functions` assesses a line and a restricted square. The reorder is
coherent from both sides. `piecewise-functions`' two false claims are corrected
and I re-derived both. The point map is now the organising idea. Four of the five
lab panels it called false are now accurate — `the-coordinate-plane` says "the
points are entered in a text box, not dragged", `what-a-function-is` describes
the witness search, `inverse-functions` says "there are no draggable domain
controls", and `linear-inequalities-in-two-variables` says "it does not accept a
clicked test point".

**What it missed.** It ran neither of the two audits this pass ran, and it did
not read the preset values against the controls that receive them. Not trying to
argue for each wrong answer left the `x = 3` option standing in a question about
`x = −2` (item 4), the `22` with no derivation (item 7), and the misassigned
sign in the two-variable inequality (item 6). Not reading the presets left the
lab that loads in an error state (item 12) — which is a live defect on a
published page, not a pedagogical judgement — and the lesson whose lab opens on a
function it never mentions (item 9), and the preset that refutes its own lesson's
concept card (item 10). It also did not read `render.py`, so it did not see that
the faded rehearsals it added render in the column beside the quiz, which turned
its own finding 7 into item 23.

**What I dispute.** Its finding 11 said `function-notation`'s panel "offered a
nonexistent solve mode", and its repair reads: "The lab panel accurately says it
evaluates and compares `f(x+1)` with `f(x)+1`, not that it has a solve mode." The
repair is correct and the reasoning stops one question short. Making a panel
honest about a lab is not the same as checking that the lab rehearses the lesson,
and here it does not: `f(x + 1)` against `f(x) + 1` is the inside/outside
distinction that `transformations-of-graphs` owns, while the theorem this lesson
proves — `f(a + b) ≠ f(a) + f(b)` — has no row anywhere in the widget (item 1).
The panel is now accurate about a lab that is teaching lesson 12.

I also read its finding 7 differently. It listed `slope` as repeating "the
vertical pair `(5, 2)`, `(5, 9)`" and the repair replaced it — question 2 now
uses `(−4, 6)` and `(−4, −1)`, which is new. But question 1 was left alone, and
question 1 is the `example` block's pair `(1, 7)` and `(3, 1)` with its answer
`−3` printed twice in the body above it (item 23). The repetition it fixed was
the smaller of the two on that page.

## Repairs this pass recommends

Item 12 is a defect and should be fixed first; it is also the only recommendation
here that touches a shared lab file, which `@chrome-renderer` owns. None of these
changes the URL space, so the five declarations in root `AGENTS.md` §1 are
untouched. After any of them, `python3 scripts/build_paths.py`,
`node scripts/labcheck.js --generated`, `node scripts/mathcheck.js` and the gate
set in `AGENTS.md` §7 must run, with `/usr/bin/python3`.

1. **`scripts/mathpath/labs/algebra_functions.py`, `LINE_PRESETS["pointslope"]`
   (item 12).** Both out-of-range presets need coordinates inside `−8 … 8`.
   `("(2, 5) and (6, 13)", "2|5|6|13|2|-3")` was chosen for slope `2`; `(2, 5)`
   and `(5, 11)` has the same slope and is still out of range, so use `(−1, −3)`
   and `(3, 5)`, slope `2`, encoded `-1|-3|3|5|2|-3`.
   `("(2, 3) and (2, 9): vertical", "2|3|2|9|2|-3")` needs only its second
   `y` brought inside: `(2, 3)` and `(2, 8)`, encoded `2|3|2|8|2|-3`. Then add a
   guard so this class cannot recur: in the preset handler and the initial-load
   block, set each select through a helper that checks the option exists and
   falls back to the nearest in-range value with a visible note, or — cheaper and
   better — add a unit assertion to `tests/` that every numeric preset in
   `LINE_PRESETS` lies within the select's range. `@chrome-renderer` and
   `@invariants` own the two halves.
2. `parallel-and-perpendicular-lines`, `quiz[2].a[1]` (item 4). Change "`x = 3`
   has no slope" to "`x = −2` has no slope", matching the stem. Then trim the
   `why`'s closing clause, which currently has to say the particular constants do
   not matter; with the option fixed it can say instead that the pair *is*
   perpendicular and that the failure is of the test's scope, not of the claim.
3. `domain-and-range`, `worked.after[2]` (item 5). Replace "show an input that
   produces two different allowed output values" with "show two different inputs
   that produce the same output" — `x = 0` and `x = −2` both give `−3` for
   `t(x) = |x + 1| − 3` — and add the sentence that makes it worth asking: that
   is why `t` will need a restriction before `inverse-functions` can invert it.
4. `linear-inequalities-in-two-variables`, `quiz[1].why` (item 6). Change "the
   fourth gets the constant sign wrong" to "the fourth keeps the constant right
   and flips the sign of the `x`-term, which is what happens when only one term
   of `−2x + 12` is divided by `−4`."
5. `point-slope-and-standard-form`, `quiz[0]` (item 7). `22` is unreachable.
   Replace it with `y = −4x + 3`, which is `−4(x − 2)` distributed correctly and
   then the `5` subtracted instead of added, and rewrite that clause of the `why`
   accordingly. Keep `−4x − 3` with its current diagnosis (the mis-distribution
   `−4x − 8`) and `−4x + 5` with its current one (the point's `y`-value copied
   into the intercept).
6. `function-notation`, `lab` (items 1, 9). Two edits, and the second is the one
   that matters. First, override the presets from the lesson dict the way
   `domain-and-range` does, putting `x^2 - 4x + 5` first so the lab opens on the
   function the whole page uses. Second, rewrite `panel_intro` so the `f(x + 1)`
   table is fenced as a preview of `transformations-of-graphs` — the lab's own
   comment already frames it as inside-versus-outside — and give the reader this
   lesson's theorem to do with the `f(a)` control they already have: read `f(1)`,
   then `f(2)`, then `f(3)`, and check that `f(1 + 2)` is not `f(1) + f(2)`. For
   `x² − 4x + 5` that is `f(3) = 2` against `f(1) + f(2) = 2 + 1 = 3`. It needs
   no lab change, and it turns
   the lesson's own theorem into something the widget can witness. Adding a
   genuine `f(a) + f(b)` row would be better still, and is a shared-lab
   arithmetic change that `@chrome-renderer` and `@lab-arithmetic` own and that
   `mathcheck.js` gates.
7. `composition-of-functions`, `concepts[1]` (item 10). One clause: order changes
   the answer in general, and some particular pairs do commute — two shifts, for
   instance — which is why "not commutative" is a statement about the operation
   and not about every pair. That makes the lesson's own second preset
   informative instead of contradictory. Alternatively relabel the preset, but
   the concept card is the thing that is wrong as written.
8. `graphing-a-linear-equation` and `slope-intercept-form`, `lab.panel_intro`
   (item 11). Say what the lab does that the lesson does not: it runs the
   construction backwards, from two points to the equation and its intercepts, so
   the honest use is to work the lesson's direction on paper first and then use
   the lab to check the answer. Lesson 2's panel should also say that
   `2x + 3y = 12` cannot be entered as an equation and that the way to see it is
   to select the two intercepts, `(6, 0)` and `(0, 4)`, both of which are in
   range.
9. `slope`, `lab.panel_intro` (item 13). Replace "Slide the two points along the
   line" with what the controls allow: from `(0, 0)` and `(4, 3)`, move the
   second point to `(8, 6)` and watch the ratio stay `3/4`, then move the first to
   `(−4, −3)`. Also add `(−2, 1)` and `(2, 4)` to the mode's presets, or supply
   them from the lesson dict, so the lesson's own well-definedness check has a
   pair inside the select's range — `(4, 10)` does not and never will.
10. `piecewise-functions`, `lab` (item 14). Override the presets from the lesson
    dict and put the lesson's own three-piece function first:
    `"-x - 1 on (-inf, -1); x^2 on [-1, 2); 8 - 2x on [2, inf)"`. Keep "|x|,
    written out" and "a gap"; drop or renumber the overlap preset, which is
    question 3's answer.
11. The four faded-versus-quiz collisions (item 23). Change the *quiz* item each
    time, since the faded rehearsal is the scarcer thing.
    `domain-and-range` q1 should use a function whose denominator zero lies
    strictly inside the root's interval and is not the faded one —
    `√(x + 5)/(x − 2)`, domain `[−5, 2) ∪ (2, ∞)` — with the four options rebuilt
    from the same four errors, and q2 should use a shifted absolute value with
    different constants. `slope` q1 should use a new pair: `(−2, 6)` and
    `(2, −2)` gives `−2`, with `2` for the lost sign, `−1/2` for run over rise
    and `1/2` for both. `transformations-of-graphs` q2 should use a new landmark
    and a new rule: `(−3, 5)` on `y = f(x)` under `y = 2f(x + 4) − 3` lands at
    `(−7, 7)`, with `(1, 7)` reading the inside shift forwards, `(−7, 13)` adding
    the `3` instead of subtracting it, and `(−3, 7)` changing only the output.
    `composition-of-functions` q1 should use a pair that is not the faded
    rehearsal's `u` and `v`, and all four options recomputed against it.
12. `parallel-and-perpendicular-lines`, `quiz[0].why` (item 17). Replace
    "Option 2 … option 4" with the values, and add the missing clause: `2/5` is
    the slope of a line *parallel* to the given one, which is the other half of
    `mistakes[0]` and the answer a reader gives when they read "perpendicular"
    and reach for the easier relationship.
13. `graphing-a-linear-equation`, `quiz[1].why` (item 18). Add the sentence the
    item exists for: a horizontal line through `(0, 5)` is `y = 5`, a different
    equation, and the two are told apart by which variable the equation
    constrains.
14. `the-coordinate-plane` q1 and q3, `point-slope-and-standard-form` q2, and
    `slope` q2's `1` (items 19, 20, 21). Give each unaddressed distractor a
    named error rather than a restatement or a note that it is arbitrary. For
    `slope` q2, replace `1` with `−7`, which is the rise taken with the run
    dropped rather than its magnitude, and diagnose it as such.
15. `__init__.py`, `outcomes` (item 26). Add a fifth outcome covering the two
    orphaned lessons: evaluate and sketch a piecewise rule by reading the
    condition before the formula and saying at each join whether the graph steps
    or connects, and graph a linear inequality in two variables with the right
    line style and the side justified by a substitution. Both are assessed acts
    with `standard` fields already written; the course home simply does not
    mention them.
16. `slope` and `parallel-and-perpendicular-lines` (item 2). Add one sentence to
    each naming similar triangles and the quarter-turn as geometry the argument
    borrows and the path does not teach, in the same voice the course already
    uses for calculus in `slope`'s `note`. No content moves; the reader is told
    which step is being taken on trust.
