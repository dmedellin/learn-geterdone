# Pedagogy assessment — Systems and Matrices (algebra, course 8)

**This assessment supersedes `docs/pedagogy/prior/systems-and-matrices.md` and makes
no source change.** Nothing under `content/` or `site/` was edited in this pass: the
prose is settled and a downstream contract snapshot is pinned to it. The closing
section describes each repair precisely enough to execute later, and the section after
it records the delta against the superseded document.

Formed from all ten lesson dicts in `content/algebra/c8_systems/` (`part_a.py`
lessons 01–07, `part_b.py` lessons 08–10, plus `__init__.py`), read front to back,
together with the two lab kits they render through — `system_lab` and `matrix_lab` in
`scripts/mathpath/labs/algebra_systems.py`, including their preset tables, KPI labels
and the `drawRows` rendering path — and the path-level `content/algebra/__init__.py`.
Every number a reader would trust was recomputed by hand.

Lessons in course order: `systems-of-two-linear-equations`, `solving-by-substitution`,
`solving-by-elimination`, `systems-in-three-variables`, `matrices-and-row-operations`,
`gaussian-elimination`, `matrix-arithmetic` (titled "Matrix Products"),
`determinants-and-cramers-rule`, `inverse-matrices`,
`systems-of-inequalities-and-linear-programming`.

The course declares `assumes_long` "lines, functions, and exact fraction arithmetic",
so it is judged backwards against courses 1–3 and 5: fraction arithmetic and the
properties that license a rearrangement (course 1), solving a linear equation in one
variable and reading a contradiction or identity (`what-it-means-to-solve-an-equation`,
`identities-and-contradictions` in course 2), the graph of `ax + by = c` and the last
lesson of course 3, `linear-inequalities-in-two-variables`, and the irreversibility of
squaring from `solving-radical-equations` in course 5. All four back-references check
out — see the sixth bullet below.

## What the course teaches well

- **One system runs through four consecutive lessons, and it is the same system every
  time.** `x + y + z = 6`, `2x − y + 3z = 9`, `−x + 2y + 4z = 15` is solved by hand in
  `systems-in-three-variables`, rewritten as rows in `matrices-and-row-operations`
  (whose `.worked.intro` says "Every number below appears in the worked example there;
  only the layout has changed"), carried to reduced row echelon form in
  `gaussian-elimination`, and written as `Ax = b` in `matrix-arithmetic` with the
  triple `(1, 2, 3)` substituted back in. That is the single best structural decision
  in the course: it makes "a matrix is elimination with the letters deleted" — the
  course `blurb`'s claim — something the reader watches happen to numbers they already
  recognise, rather than something asserted.
- **Every legal move is justified by reversibility, and the illegal ones are named by
  the same criterion.** `solving-by-elimination`'s theorem is proved in both
  directions and its `.body[4]` spells out why `E₁` must be kept: "from `x = 1` and
  `y = 1` you may add each to the other and reach `x + y = 2` twice, which has a whole
  line of solutions." `matrices-and-row-operations` then names the inverse of each of
  the three row operations, and its `.body[9]` rules out three non-operations —
  scaling by `0`, operating on columns, and performing two at once — each for a stated
  reason. The `standard[1]` closes the loop: "If you cannot name the inverse, the step
  you performed was probably not one of the three." A reader finishes the course with
  a criterion rather than a list.
- **The degenerate cases are treated as answers, not as failures.** `0 = 14` and
  `0 = 0` are introduced in `solving-by-substitution` and `solving-by-elimination`
  with their geometry attached, read off a matrix in `gaussian-elimination`, and
  diagnosed by the determinant in `determinants-and-cramers-rule`. The course insists
  four separate times that "infinitely many" is a count and not an answer —
  `systems-of-two-linear-equations` `.mistakes[2]`, `solving-by-substitution`'s
  parameter-form example, `solving-by-elimination` `.mistakes[2]`,
  `gaussian-elimination` `.mistakes[2]` — and each time it supplies the parameter form
  the reader is supposed to write instead. That repetition is earned: it is the error
  that survives being corrected once.
- **`determinants-and-cramers-rule` is honest about what its own tool cannot do.**
  `.concepts[2][1]`: "`D = 0` … rules out uniqueness and says nothing else."
  `.steps[2]` is titled "If D = 0, stop" and sends the reader back to row reduction.
  `.body[9]` gives two systems with the same `D = 0`, one inconsistent and one
  dependent, and says outright that the determinant "genuinely cannot tell them
  apart". And `.body[10]` refuses to oversell Cramer's rule: "For a 4 by 4 system it
  asks for five 4 by 4 determinants, where one row reduction would have finished the
  job. Gaussian Elimination remains the method; this lesson is the criterion." A
  course that teaches a formula and then tells the reader not to use it is doing
  something unusual and right.
- **The worked examples are chosen so that the wrong answer is visible.**
  `solving-by-substitution` `.worked.after[0]` computes what the sign error actually
  produces (`x = −22`, failing the first check); `solving-by-elimination`
  `.worked.after[0]` works the longer route to show it costs two multiplications
  instead of one; `gaussian-elimination` `.worked.after[0]` replaces `−1/3` with
  `−0.33` and shows the final rows become `1.01` and `1.99` — "and the matrix looks
  exactly as convincing as the correct one";
  `systems-of-inequalities-and-linear-programming`'s worked example evaluates the
  objective at the two *rejected* crossings and finds `P = 40` against the true
  maximum of `34`, so the reader sees that an untested crossing does not add a
  harmless candidate, it wins.
- **Prerequisite order backwards across the path is sound, and every back-reference
  lands.** `systems-of-two-linear-equations` `.body[2]` cites Lines, Functions and
  Graphs for the graph of `ax + by = c` (course 3 teaches it in
  `graphing-a-linear-equation` and `point-slope-and-standard-form`);
  `solving-by-substitution` `.concepts[1][1]` and `solving-by-elimination` `.steps[2]`
  cite Linear Equations and Inequalities for one-variable solving (course 2);
  `solving-by-substitution` `.body[8]` cites the same course for contradictions and
  identities, which is `identities-and-contradictions`;
  `solving-by-elimination` `.concepts[2][1]` cites Rational and Radical Expressions
  for squaring as the irreversible operation, which is `solving-radical-equations`;
  `matrix-arithmetic` `.concepts[0][1]` cites Foundations of Algebra for the rules of
  addition; and `systems-of-inequalities-and-linear-programming` `.body[0]` says
  "Lines, Functions and Graphs ended with a single linear inequality in two
  variables", which is exactly true —
  `linear-inequalities-in-two-variables` is the fourteenth and last lesson of course 3.
  That last one is the most precise cross-course claim on the Algebra path and it is
  correct.
- **The arithmetic is right.** Everything checkable was recomputed: the crossing
  `(5/3, 2/3)` and its drawn approximation `(1.7, 0.7)`; all three classified systems
  and the `0 = 5` that (b) produces; every substitution and elimination worked
  example and its check; the three-variable spine, `E2 + 2E3 = 3y + 11z = 39` and
  `2E2 + E3 = 3x + 10z = 33`; the dependent variant `(9 − 4t, t, 3t − 3)` at `t = 1`
  and `t = 2`; the full six-operation reduction to `(1, 2, 3)` and the `0.33` corruption
  giving `1.01` and `1.99`; the free-variable example `{(−1 − 2t, t, 2)}` checked at
  `t = 1`; both matrix products `AB` and `BA`, the `CD` entries `2, −5, 26, 14`, and
  the entrywise product `0, 2, 3, 0`; the `3 × 3` determinant `−61` and the `−51` the
  sign error gives; Cramer's `D = −17`, `Dx = −16`, `Dy = −29` with `x = 16/17`,
  `y = 29/17` and the rounding artefact `7.01`; the inverse `[3/5, −7/10; −1/5, 2/5]`
  by formula and by reduction, and the solution `(−5, 3)`; every corner of the
  feasible region, the two rejected crossings at `P = 40`, and the non-linear
  counterexample `P = xy` peaking at `(2.5, 5)` — which is genuinely the constrained
  maximum, and a nice piece of work. No figure was wrong.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **`matrices-and-row-operations`' lab reports determinants three lessons before the
   determinant exists.** The lesson attaches `("matrix", {"mode": "rows"})`, and
   `drawRows()` in `scripts/mathpath/labs/algebra_systems.py` emits a table titled
   *"What each one did to the determinant, recomputed from the entries each time"*
   with a row per operation and a "factor" column (`−1` for a swap, `k` for a scaling,
   `1` for a replacement), plus a KPI tile hard-labelled **"det A"** in the lab's
   `setkpi` call, plus a status banner beginning "Three operations, three effects on
   the determinant." The word *determinant* appears nowhere in lesson 5's prose. It is
   defined in lesson 8. This is the same defect the sibling assessment of Discrete
   Mathematics course 2 found in `binary-relations`, where a lab reported next
   lesson's verdicts unexplained — except here the gap is three lessons and the
   material is a whole new object rather than a vocabulary item.
2. **That same lab contradicts the lesson's central discipline.** The panel
   (`.lab[1].panel_intro`) says "apply a **single row operation at a time**"; the
   lesson's `.steps[2]` says "Operate on rows only, one operation at a time"; and quiz
   question 3's `why` says "One elementary operation writes one new row … if it were
   altered at the same time the step would not be reversible, which is exactly the
   simultaneous-operation trap." `drawRows()` applies all three operations — swap,
   scale, add — to `A` from one set of controls, prints all three results, and then
   composes them in a fourth block titled "All three in order, each acting on the
   result of the last". The reader cannot perform one operation on that widget; the
   page's own warning about doing several at once sits above a widget that does three.
3. **The panel tells the reader to run operations the lab has no preset for.** It
   says "Run the operations from 'Systems in Three Variables' — `R2 − 2R1` and
   `R3 + R1` — and compare the entries with the equations there". `MAT_PRESETS["rows"]`
   offers `2 1 -1; -3 -1 2; -2 1 2` and five others; the course's spine matrix,
   `1 1 1 6; 2 -1 3 9; -1 2 4 15`, is not among them, and the reader must type twelve
   entries to follow the instruction.

### Facts a reader would trust that are wrong

4. **The course home states the corner point theorem without its hypothesis.**
   `content/algebra/c8_systems/__init__.py` `key[3]`: "the optimum of a linear
   objective sits at a corner." The lesson is scrupulous about this — `.thm` in
   `.body[8]` requires the region to be non-empty, closed and bounded, `.concepts[2][1]`
   repeats it, `.body[11]` gives the unbounded counterexample where no maximum exists,
   and the `standard` demands "exhibit a feasible ray or a global bound instead of
   citing the bounded theorem". The course home's headline drops all of it, and the
   course home is what the reader meets first and what a course search surfaces.
5. **The path page says this course comes last, and it does not.**
   `content/algebra/__init__.py` `why_order[3]`: "Systems and matrices come last
   because row reduction is elimination performed on exact fractions, and it is
   unreadable to anyone not already fluent in both." The path has nine courses;
   Systems and Matrices is eighth and Sequences and Series is ninth. The same list
   gives a reason for the position of every course except the one that is actually
   last. Recorded identically in the sibling assessments for courses 7 and 9.
6. **The theorem's hypothesis uses a word the path never defines.** "Closed" appears
   in `.thm`, `.concepts[2][1]`, `.steps[3]` and `.standard[1]` of
   `systems-of-inequalities-and-linear-programming` and nowhere else in nine courses.
   `.body[12]` glosses it in passing ("A strict inequality removes its boundary line
   from the region, so an optimum sitting on that line is approached but never
   reached"), which is the right gloss, but it arrives four blocks after the theorem
   and it is never attached to the word. A reader asked to check three conditions can
   check two.
7. `systems-of-inequalities-and-linear-programming` `.worked.after[2]` ends "explain
   why the bounded closed, bounded region makes the corner comparison conclusive" —
   "bounded closed, bounded", a copy-editing failure in the faded rehearsal's final
   instruction. The same phrase appears in three grammatical variants across the
   lesson ("not empty, closed and bounded", "nonempty closed, bounded", "a nonempty
   closed, bounded region"), of which the theorem's own "If the feasible region is not
   empty, closed and bounded" parses ambiguously as *not (empty, closed and bounded)*.
8. `matrix-arithmetic` has slug `matrix-arithmetic` and title "Matrix Products", and
   every cross-reference in the course — `gaussian-elimination`'s `note`,
   `inverse-matrices` `.body[0]` and `.concepts[0][1]`,
   `determinants-and-cramers-rule`'s `note` — calls it "Matrix Products". The
   published URL is `/systems-and-matrices/matrix-arithmetic/`. Not a pedagogy defect
   and not worth a URL change (retiring a slug costs the five-place update), but a
   reader who searches the site for the lesson they were told to read will not find
   it by name.

### Distractors that are also true

The failure `content/AGENTS.md` warns about. Two of the thirty questions have one.

9. **`matrix-arithmetic` question 3, option (c).** The question is: "`A` and `B` are
   both `2 × 2`, so `AB` and `BA` both exist and have the same size. What follows?"
   and option (c) is **"Both products are found entry by entry"**. Under the reading
   the lesson itself uses two screens earlier, that is true and is the method:
   `.steps[1]` is "Take one row and one column at a time", `.steps[2]` is "Add the
   products and place the entry", and the `def` in `.body[5]` specifies the product one
   entry at a time. The `why` reads the option as the *entrywise* product — "Entrywise
   multiplication is a different operation" — which is the other reading, and the
   reader who chose (c) meaning "one entry at a time" is told they are wrong without
   being told which sense was intended.
10. **`inverse-matrices` question 3, option (d)**, "There is no formula; multiply `AB`
    out and invert the result", is half true: the procedure it names works, and for a
    `2 × 2` it is a perfectly good route to `(AB)⁻¹`. Only the clause "There is no
    formula" is false. The `why` covers option (a) and the correct answer and says
    nothing about (d), so the reader who liked the procedure never learns which half
    of the sentence failed.
11. Borderline, recorded rather than charged: `solving-by-elimination` question 2
    option (c), "zero is not a number you are allowed to multiply by", is a true
    statement of the rule inside this method, stated circularly. It is undiagnosed
    (item 16), which is what makes it read as arbitrary rather than as question-begging.

### Labs that do not agree with their own lessons

This is the course's systematic weakness, and it is worth stating as one finding
before the instances. **Nine of the ten lessons attach a lab whose presets cannot
reproduce the lesson's own worked example**, and in four of those the lab ships a
*near-identical* system with one number changed — which is worse than an unrelated
one, because a reader checking hand-work against the lab gets a different answer and
cannot tell whether they or the lab is wrong. The exception is `matrix-arithmetic`,
whose first preset is `1 2; 3 4` against `0 1; 1 0`, exactly the worked example. For
contrast, the neighbouring Exponential and Logarithmic Functions course opens two of
its twelve labs on the lesson's own worked example.

12. **The course's spine example is in no preset of any of the four labs that teach
    it.** `systems-in-three-variables`, `matrices-and-row-operations`,
    `gaussian-elimination` and `matrix-arithmetic` all work
    `x + y + z = 6`, `2x − y + 3z = 9`, `−x + 2y + 4z = 15`. `SYS_PRESETS["three"][0]`
    is `x + y + z = 6`, `2x − y + z = 3`, `x + 2y − z = 2` and
    `MAT_PRESETS["rref"][0]` is its augmented matrix `1 1 1 6; 2 -1 1 3; 1 2 -1 2`.
    Both are *different systems with the same solution* `(1, 2, 3)`. A reader who opens
    `gaussian-elimination`'s lab to follow the six operations in the worked example
    diverges at the first row operation and arrives at the same triple by a different
    route, with nothing on the page to explain why.
13. **`systems-in-three-variables`' panel describes a user interface that does not
    exist.** `.lab[1].panel_intro`: "**Set the nine coefficients and three constants**;
    the lab reports the triple". `SYS_FIELDS` for the `three` mode is three free-text
    equation boxes (`syEq1`–`syEq3`), parsed by `Lequation`. There are no coefficient
    boxes. The same class of instruction appears in `systems-of-two-linear-equations`
    ("**Move the coefficients** and watch the crossing point"),
    `systems-of-inequalities-and-linear-programming` ("**Drag a constraint**, watch the
    corner move") and `matrix-arithmetic` ("**Set the two sizes first**" — the lab
    infers size from the text you type and then refuses a bad product, which is the
    right behaviour described as the wrong control).
14. **`systems-of-two-linear-equations`' inconsistent preset is the lesson's own
    example with one digit changed.** The lesson's `.body[7]`, its worked example (b)
    and its quiz question 2 all use `2x + 3y = 6` with `4x + 6y = 7`.
    `SYS_PRESETS["graph"][1]` is `2x + 3y = 12` with `4x + 6y = 7` — which is also
    inconsistent, so the lab behaves correctly and the numbers on screen are not the
    numbers in the quiz the reader just failed.
15. **`systems-of-inequalities-and-linear-programming`'s panel prescribes an
    experiment with no preset behind it.** "Watch which corner wins as you tilt the
    objective from `5x + 4y` toward `3x + 4y`" is exactly right — it is the lesson's
    worked example against its quiz question 2, on one region, and it is the best
    single instruction in any panel in this course. Neither objective, and not the
    region `x ≥ 0, y ≥ 0, x + y ≤ 8, 2x + y ≤ 10`, appears in
    `SYS_PRESETS["linprog"]`. The reader must type four constraints and two objectives
    to run it.
16. Smaller instances of the same pattern, each one preset away from being right:
    `solving-by-substitution`'s worked example is `5x − 2y = 4`, `3x + y = 9` and the
    nearest preset is `3x + 2y = 7`, `5x − y = 3`; `solving-by-elimination`'s body
    works `2x + 3y = 5` with `5x − 2y = −16` and the nearest preset is `2x + 3y = 5`
    with `3x − 2y = 14` — first equation identical, second changed;
    `determinants-and-cramers-rule` works `2x + 3y = 7`, `5x − y = 3` and its
    `det` presets offer a `3 × 3` by default while the panel speaks of "`D`, `Dx` and
    `Dy`" (two variables); `inverse-matrices` inverts `4 7; 2 6` and the presets offer
    `2 1; 1 1`, `1 2; 3 4` and four others, while its singular example `2 3; 4 6` is
    shipped as `1 2; 2 4`.

### Quiz feedback that does not answer the wrong answer

17. The `why` fields are strong wherever the wrong answers are arithmetic, and weak
    wherever they are conceptual. The good ones are genuinely diagnostic:
    `solving-by-substitution` Q1 names all three sign and bracket failures;
    `solving-by-elimination` Q1 computes what each wrong multiplier leaves (`8y`,
    `+4y`, `8y` against `−2y`); `systems-in-three-variables` Q2 traces `−2`, `−6` and
    `0` to three specific slips; `matrix-arithmetic` Q2 identifies `19` as the row-1
    entry, `21` as the entrywise product and `15` as the first of two products;
    `determinants-and-cramers-rule` Q1 derives `7`, `−23` and `−7` from one dropped
    sign, one reversal, and both; `inverse-matrices` Q1 explains all three.
    Twelve of the thirty fall short, and the pattern is consistent — the conceptual
    distractor is left unnamed:
    - `systems-of-two-linear-equations` Q2 answers the proportionality distractor and
      not "Exactly one" or "Two"; "Two" is worth refuting, because the lesson proves
      in `.body[3]` that exactly two is impossible and the question is the only place
      that is tested.
    - `systems-of-two-linear-equations` Q3 answers "the solution is `(1.7, 0.7)`" and
      "Nothing whatever" and not "That the system is inconsistent".
    - `solving-by-substitution` Q2 answers `(6, 1)` and the `6 = 6` case and not "has
      been solved incorrectly, necessarily", which is the belief the lesson's whole
      degenerate-case section exists to correct.
    - `solving-by-elimination` Q2 answers only "`0 = 0` is false"; Q3 names no
      distractor at all, though `{(0, 14)}` and "every pair on either of the two
      lines" are both specific misreadings the lesson has warned about.
    - `systems-in-three-variables` Q1 leaves "A contradiction" and "The solution, up to
      back-substitution" unaddressed; Q3 answers "the whole of space" and not "empty"
      or "a single triple".
    - `matrices-and-row-operations` Q1 answers two of three and says nothing about
      `0 2 0 | −5`, which is the row a reader writes who transcribes the equation
      without rearranging — the exact error `.mistakes[1]` is about.
    - `gaussian-elimination` Q1 names no distractor; Q3 leaves "are the same only if
      both avoided fractions" and "only if neither swapped rows" unaddressed, and both
      are beliefs the uniqueness theorem is there to kill.
    - `determinants-and-cramers-rule` Q3 and `inverse-matrices` Q3 each leave two
      (items 10 and 11).

### Cognitive load and structure

18. **`determinants-and-cramers-rule` is the strongest split candidate in the
    course.** It carries the `2 × 2` determinant, the `3 × 3` cofactor expansion with
    its alternating signs, a mention of Sarrus's rule, the uniqueness theorem, and
    Cramer's rule at two sizes — five things, on an eleven-block body, with three quiz
    questions. Two of those three test the determinant and one tests Cramer's column
    replacement, so the `3 × 3` expansion — the thing `.mistakes[1]` says is "the single
    most common way a 3 by 3 determinant comes out wrong" — is never retrieved. The
    natural cut is after `.body[7]`: "Determinants" ending on the uniqueness theorem,
    and "Cramer's Rule" starting from the `def`. **I am not recommending the split**:
    it changes the URL space and needs the five-place update and `@site-architect`,
    and the lesson's best sentence — `standard`, "the right answer is 'not exactly one
    solution, and I need to reduce it to say more'" — depends on the criterion and the
    formula being on one page. Recorded as a judgement.
19. **This is the shortest course on the path — ten lessons against twelve to
    fourteen everywhere else — and the shortfall is concentrated at the end.** Four
    lessons introduce and solve systems, three introduce matrices, and three
    (determinants, inverses, linear programming) each carry a full topic. Lessons 8, 9
    and 10 have bodies of eleven, thirteen and thirteen blocks and three quiz
    questions apiece, the same as `matrices-and-row-operations`, which carries a
    notation and nothing else.
20. **Every lesson has exactly three concepts, four steps, three mistakes and three
    quiz questions.** That is the floor of the range
    `TestLessonDataMatchesTheRenderer` enforces, and no lesson takes the room
    `content/AGENTS.md` says a lesson may earn. So retrieval density is constant while
    lesson weight varies by a factor of three or more.
21. **There is no modelling lesson.** Every system in the first nine lessons arrives
    as bare equations; the only word problem on the course is the linear programming
    objective in lesson 10, and even it arrives as four inequalities already written
    down. The course outcomes do not promise translation from a situation, so this is
    not a broken promise — but Systems and Matrices is the last solving course on the
    path, and a reader finishes it able to solve any system put in front of them and
    with no practice at writing one down. Recorded as a structural observation for
    whoever revisits the course's length.
22. The faded-rehearsal discipline is kept: all ten `worked.after` blocks close with
    one that supplies the first strategic decision and withholds the rest, and they
    are well chosen —
    `systems-of-two-linear-equations` uses a vertical line, so the reader has to
    notice that the slope comparison does not apply; `gaussian-elimination` hands over
    a matrix with a zero row so the answer has to be a family. The course `how_to[0]`
    promises exactly this and it is delivered ten times out of ten.

## Where a learner gets stuck

- At `matrices-and-row-operations`' lab, reading a table of determinants and a tile
  labelled "det A" three lessons before the determinant is defined (item 1).
- At the same lab, having been told twice on the same page to apply one operation at a
  time, in front of a widget that applies three and then composes them (item 2).
- At `systems-in-three-variables`' lab, looking for the nine coefficient boxes the
  panel promises and finding three text fields (item 13).
- At `gaussian-elimination`'s lab, following the worked example's six operations on a
  default matrix that is a different system with the same answer (item 12).
- At `systems-of-two-linear-equations` question 2, having just been shown
  `2x + 3y = 6` with `4x + 6y = 7` three times, and opening the lab to find
  `2x + 3y = 12` (item 14).
- At `systems-of-inequalities-and-linear-programming`'s theorem, asked to check that a
  region is "closed" with no definition of the word anywhere on the path (item 6), and
  again at its faded rehearsal, reading "the bounded closed, bounded region" (item 7).
- At the course home, having learned the corner point theorem with three hypotheses,
  reading `key[3]` state it with none (item 4).
- At `matrix-arithmetic` question 3, having chosen "found entry by entry" because that
  is how the lesson said to find them (item 9).
- At `gaussian-elimination` question 3, having believed that avoiding fractions or
  avoiding swaps is what makes two reduced forms agree, and getting a `why` that never
  mentions either (item 17).

## Repairs this pass recommends

No lesson is added, removed, renamed or reordered, so the five URL declarations in
`AGENTS.md` §1 are untouched by all of them. Items marked **(lab kit)** edit
`scripts/mathpath/labs/algebra_systems.py` and belong to `@chrome-renderer`;
everything else is `content/algebra/c8_systems/`.

- **(lab kit) `MAT_PRESETS["rows"]`: add the course's spine matrix as the first
  preset** — `{"label": "the system from 'Systems in Three Variables'", "a": "1 1 1 6;
  2 -1 3 9; -1 2 4 15", "i": "2", "j": "1", "k": "-2"}` — so that selecting it performs
  `R2 − 2R1` and produces the row `0 -3 1 | -3` the lesson names. Add the same matrix
  as the first preset of `MAT_PRESETS["rref"]` (`"1 1 1 6; 2 -1 3 9; -1 2 4 15"`),
  displacing the present first entry rather than replacing it. *Why:* items 3 and 12 —
  four consecutive lessons work one system and no lab offers it.
- **(lab kit) `drawRows()`: gate the determinant block behind a config flag.** The
  function currently always renders the "What each one did to the determinant" table
  and sets a `det A` KPI. Add `cfg.get("show_det", True)` and have
  `matrices-and-row-operations` pass `"show_det": False`, leaving the block for
  whichever lesson wants it later. If a flag is unwelcome, the cheaper alternative is
  the panel fence below. *Why:* item 1.
- **`matrices-and-row-operations`.lab[1].panel_intro:** rewrite to describe what the
  lab does and to fence what is not yet the reader's — "Type an augmented matrix,
  choose two rows and a multiplier, and the lab performs each of the three operations
  on the matrix as typed, then all three in sequence. Select the first preset and set
  `i = 2`, `j = 1`, `k = −2`: the third block is `R2 − 2R1`, and its row reads
  `0 −3 1 | −3`, which is equation `A` of 'Systems in Three Variables' entry for
  entry. The determinant table underneath belongs to 'Determinants and Cramer's Rule'
  three lessons from now; nothing on this page depends on it." *Why:* items 1, 2 and
  3, and it is the fix that costs nothing if the flag above is rejected.
- **`c8_systems/__init__.py` `key[3]`:** "the optimum of a linear objective sits at a
  corner" becomes "**on a closed, bounded feasible region**, the optimum of a linear
  objective sits at a corner". *Why:* item 4; the lesson is careful and the headline
  is not, and the headline is what a course search returns.
- **`systems-of-inequalities-and-linear-programming`.body[8]:** define the word in the
  theorem's own second paragraph — "*Closed* here means the region contains its
  boundary, which is what `≤` and `≥` give and what `<` and `>` take away; *bounded*
  means it fits inside some circle." Then `.body[12]`'s existing gloss becomes a
  reminder rather than the first mention. *Why:* item 6 — the hypothesis is currently
  two-thirds checkable.
- **`systems-of-inequalities-and-linear-programming`.worked.after[2]:** "the bounded
  closed, bounded region" becomes "the closed, bounded region". Regularise the other
  three variants of the phrase, and rewrite the theorem's opening from "If the
  feasible region is not empty, closed and bounded" to "If the feasible region is
  non-empty and is closed and bounded", which removes the ambiguous parse. *Why:*
  item 7.
- **(lab kit) `SYS_PRESETS["graph"][1]`:** change `"2x + 3y = 12"` to `"2x + 3y = 6"`
  so the inconsistent preset is the lesson's own example, the one quiz question 2 asks
  about. The preset stays inconsistent and the label needs no change. *Why:* item 14 —
  a one-character edit that removes a whole class of reader confusion.
- **(lab kit) `SYS_PRESETS["linprog"]`: add the lesson's own problem** —
  `{"label": "the worked example: maximise 5x + 4y", "eq": ["x >= 0", "y >= 0",
  "x + y <= 8", "2x + y <= 10"], "obj": "5x + 4y", "sense": "max"}` — and a second
  entry identical but with `"obj": "3x + 4y"`, labelled "the same region, a different
  objective, a different winning corner". *Why:* item 15; the panel already prescribes
  exactly this comparison and currently makes the reader type it.
- **Four panels lose a control that does not exist** (item 13):
  `systems-in-three-variables` — "Set the nine coefficients and three constants"
  becomes "Type the three equations"; `systems-of-two-linear-equations` — "Move the
  coefficients" becomes "Edit either equation"; `systems-of-inequalities-and-linear-programming`
  — "Drag a constraint, watch the corner move" becomes "Change a constraint and watch
  the corner move" (and the `panel_title`, which is "Drag a constraint, watch the
  corner move", needs the same edit); `matrix-arithmetic` — "Set the two sizes first:
  the lab refuses a product whose inner dimensions disagree" becomes "Type a matrix
  into each box; the lab reads their sizes and refuses a product whose inner
  dimensions disagree, which is the shape rule delivered as an error message."
- **`matrix-arithmetic`.quiz[2].a[2]:** "Both products are found entry by entry"
  becomes **"Both products are the matrix of products of matching entries"**, which is
  unambiguously the entrywise operation the `why` already refutes. *Why:* item 9 — the
  option as written is true under the lesson's own method.
- **`inverse-matrices`.quiz[2].why:** append "The fourth is not wrong about the
  procedure — multiplying `AB` out and inverting it does give `(AB)⁻¹` — only about
  there being no formula; and for a `3 × 3` it is two full reductions where
  `B⁻¹A⁻¹` is none." *Why:* item 10.
- **`matrix-arithmetic`:** add one sentence to `.body[0]` or the `def` noting that the
  lesson is titled "Matrix Products" and published at `/matrix-arithmetic/`, or — the
  better option if `@site-architect` is consulted anyway — leave it and accept the
  mismatch. Recorded, not urged. *Why:* item 8.
- **Twelve `why` fields gain one clause each**, naming the distractor they currently
  skip (item 17): `systems-of-two-linear-equations` Q2 ("Two" is impossible by the
  theorem two blocks above) and Q3 ("inconsistent" would need parallel lines, and
  these cross); `solving-by-substitution` Q2 ("a number-only statement is not evidence
  of an error; it is the answer"); `solving-by-elimination` Q2 (zero is a perfectly
  good number to multiply *by*; what fails is that nothing undoes it) and Q3 (`{(0,
  14)}` reads a false statement as a pair; "either of the two lines" is the union, and
  a system asks for the intersection); `systems-in-three-variables` Q1 ("a
  contradiction" would need a false numeric statement, and nothing here is false) and
  Q3 ("empty" needs a `0 = k` row, which was excluded; "a single triple" needs three
  pivots); `matrices-and-row-operations` Q1 (`0 2 0 | −5` transcribes the equation
  as written, before standard form); `gaussian-elimination` Q1 (all three distractors
  read a false row as information) and Q3 (fractions and swaps change the *route*, and
  the theorem is about the destination); `determinants-and-cramers-rule` Q3 ("both
  columns replaced" is not a determinant of anything the rule uses).
- **Path-level, recorded not fixed here:** `content/algebra/__init__.py`
  `why_order[3]` says Systems and Matrices comes last. It is eighth of nine, and the
  list gives no reason for Sequences and Series' position. Belongs in one commit with
  the sibling assessments (item 5).

## Delta against the superseded assessment

The prior document is at `docs/pedagogy/prior/systems-and-matrices.md` (226 lines,
Codex lane). Its repairs are live on `main` and nothing here reverts them.

**What this pass caught that the first missed.**
- The first pass did not open a lab kit. Ten of this document's findings (items 1–3,
  12–16) live in `scripts/mathpath/labs/algebra_systems.py` or in the disagreement
  between a `panel_intro` and the widget beneath it — including the two most serious
  findings in the course: a determinant table three lessons early, and a lab that
  performs three row operations on the page of the lesson that insists on one.
- No distractor audit was performed. Items 9, 10 and 11 are new, and item 9 is the
  kind `content/AGENTS.md` names explicitly: an option that is true under the reading
  the lesson's own method section supplies.
- No per-distractor feedback audit was performed. Item 17 lists twelve `why` fields,
  and the pattern in them is a finding in itself — the arithmetic distractors are
  diagnosed almost without exception and the conceptual ones almost never.
- The systematic preset/worked-example divergence (the preamble to the lab section)
  is new, and it is the course-level finding rather than nine unrelated ones. Four of
  the nine are near-misses with one number changed, which is the variety that actively
  misleads.
- The corner point theorem's missing hypothesis on the course home (item 4) and the
  undefined word "closed" (item 6) are new; so is the "bounded closed, bounded" typo
  (item 7), the slug/title split (item 8), and the path-page error (item 5).
- The arithmetic was not previously checked. This pass recomputed every figure in the
  course, including the linear programming counterexample `P = xy` peaking at
  `(2.5, 5)` — which required solving a constrained maximisation to confirm — and found
  none wrong.

**What the first pass claimed that this pass disputes.**
- The prior document treats the four-lesson spine example (one system carried from
  hand elimination through matrices to `Ax = b`) as a structural virtue, and it is.
  What it does not say, and what this pass found, is that the labs attached to all four
  of those lessons ship a different system (item 12), so the virtue is confined to the
  prose and is contradicted by the interactive half of every one of those pages.
- The prior document credits the course with careful hypothesis-keeping in the linear
  programming lesson. The lesson's body earns that credit; the course home does not
  (item 4), and "closed" is never defined (item 6). The care is real and one layer
  thinner than claimed.
- Not disputed and worth recording because it is verifiable: the faded-rehearsal
  discipline the first pass reports as installed is present in all ten lessons, and
  the reversibility argument it credits as the course's organising idea does run
  unbroken from `solving-by-elimination`'s theorem through
  `matrices-and-row-operations`' three inverses to `inverse-matrices`' definition.
