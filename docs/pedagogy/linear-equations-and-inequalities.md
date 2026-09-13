# Pedagogy assessment — Linear Equations and Inequalities (algebra, course 2)

**Second assessment. It supersedes
`docs/pedagogy/prior/linear-equations-and-inequalities.md` and it changes no
source.** Nothing under `content/` or `site/` was edited in this pass: the prose
is settled and a downstream contract snapshot is pinned to it. Everything below
that would have been a repair is written as a recommendation precise enough to
execute later.

Formed from all thirteen lesson dicts in `content/algebra/c2_equations/`
(`part_a.py`, `part_b.py`, `__init__.py`), the course home, every mode of the
`equation` and `inequality` labs in
`scripts/mathpath/labs/algebra_equations.py` that those lessons attach, and the
page shape in `scripts/mathpath/render.py` and
`scripts/mathpath/labs/common.py`, as they stand on
`review/course-ui-standardization` at `d0a238a`. (The branch tip has since
moved to `19b6b0b`, which carried the supersession move itself along with a
test-suite change; it touched nothing under `content/` or `scripts/`, so every
line cited below is unchanged at the tip.) No lesson was sampled; every
`body` block, `concepts` card, `steps` entry, `worked` panel, `quiz` item,
`mistakes` row, `standard` and `lab` panel was read, and the preset list behind
every panel was read against the lesson text.

The order is the one `__init__.py` ships, `part_a.LESSONS + part_b.LESSONS`:
`what-it-means-to-solve-an-equation`, `one-and-two-step-equations`,
`variables-on-both-sides`, `equations-with-fractions`,
`literal-equations-and-formulas`, `identities-and-contradictions`,
`ratio-proportion-and-percent`, `modelling-with-linear-equations`,
`linear-inequalities`, `compound-inequalities`, `absolute-value-equations`,
`absolute-value-inequalities`, `interval-and-set-builder-notation`. The declared
prerequisite is Foundations of Algebra — "expressions, exponents, the
distributive law" — and that course, as reordered, does supply them. Course 3
(`lines-functions-and-graphs`) comes after this one, which matters below.

## What the course teaches well

- **Reversibility, not ritual, is the reason a step is allowed.**
  `what-it-means-to-solve-an-equation`'s `body` states it in one sentence — "A
  move that can be reversed cannot lose a solution, because the reverse move
  would have to put it back, and it cannot invent one either, for the same
  reason" — and then pays for the `c ≠ 0` in the theorem by multiplying `2x = 6`
  by zero and watching the information go. `equations-with-fractions` makes that
  the assessed act: question 3's correct answer is "Because the LCD is a nonzero
  number, so the multiplication can be undone by dividing", and its distractor
  "Because the LCD is the smallest such number" is the exact confusion between a
  convenience and a licence. `ratio-proportion-and-percent`'s `proof` derives
  `ad = bc` by multiplying by `bd` and then says "The proof is where the
  conditions come from." Three lessons, one idea, stated the same way each time.
- **The quiz explanations are the best in the three Algebra courses I read, and
  the good ones are specific to the arithmetic.** `equations-with-fractions`
  question 2 diagnoses all three wrong answers by the step that produces them,
  and all three check: for `(x − 2)/5 + (x + 1)/2 = 4`, `37/7` is the multiplier
  dropped from the `−2`, `3/7` is the right side left unmultiplied, `31/7` is
  `x − 2` expanded as `x + 2`. `variables-on-both-sides` question 2 does the same
  for `3`, `−1/2` and `1/2`, including the two-step slip that produces `−1/2`
  ("subtracting `3x` on the left while cancelling it on the right, which leaves
  `2 − 4x = 4`"). This is the standard the course sets for itself, and the places
  it falls short are visible only because the rest is this good.
- **`identities-and-contradictions` proves the trichotomy instead of naming it.**
  It reduces every linear equation to `px = q`, proves the three cases, and then
  separates `0 = 0` from `x = 0` in four places — `concepts[2]`, the two `h3`
  paragraphs, `steps[3]` and `mistakes[0]`. Its worked panel varies one constant
  to turn an identity into a contradiction, then adds line D, where distributing
  a minus sign wrongly manufactures a contradiction out of an identity: "A sign
  error can manufacture any of the three outcomes, which is why the simplifying
  comes first and gets checked."
- **Extraneous candidates are taught as part of the method rather than as a
  safety net.** `absolute-value-equations`' `steps[3]` says to substitute into
  the original "Not into a line halfway down your working, which has already had
  the bars removed", and its `worked` panel is the case where *both* candidates
  die — the rarest and most instructive shape, since the answer is the empty set
  and the page has to say that an empty answer is complete. It then shows the
  same two cases surviving when the right side changes from `x − 5` to `x + 3`,
  so the difference is visibly in the check and not in the algebra. Both
  calculations verify.
- **`modelling-with-linear-equations`' worked panel is the strongest single page
  element in the course.** The same mixture is accepted at 25% and refused at
  60%, the refusal passes its own substitution check (`x = −100` really does
  satisfy the equation), and it is then rejected on the situation with a reason
  that needs no algebra: "Mixing a 10% solution with a 50% solution always lands
  somewhere between 10% and 50%". Question 3, on `b = 9/2` buses, refuses to let
  rounding be the answer and says why.
- **`linear-inequalities` proves the reversal rule and then forbids the move that
  looks like it.** Three lines from `b − a > 0` and `−c > 0`, then a worked
  counterexample showing that dividing `3x > 5x` by `x` concludes "no solutions"
  when the answer is every negative number. `mistakes[0]` separates the rule from
  its lookalike: "The rule is about the sign of what you multiply or divide *by*,
  not about whether a negative number is on the page."
- **The first pass's lab-leak repair is real and I verified it in the lab
  source.** `check` is absent from `EQ_PLOT_MODES`, so lesson 1's lab draws no
  graph. In `inequality_lab`, the `linear` mode calls `preNotationRows` — "as an
  inequality / in words / on the number line", with the comment "Before the
  notation lesson, an inequality, words and the number-line drawing are the
  representations the reader has actually been taught" — and the `compound` and
  `absolute` modes use only `setIneq` and `setWords`. `setText` and `setBuilder`
  appear in the `notation` mode and nowhere else on this course. `INEQ_KPIS`
  confirms it: the `linear` headline is "solution / set shape / sign reversed?",
  not an interval.

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **Five of the equation lab's nine modes draw a coordinate-plane graph, and
   only one lesson tells the reader what it is.**
   `EQ_PLOT_MODES = ("solve", "sides", "type", "model", "absolute")` puts an SVG
   with `EQ_LEGEND_PLOT` — "left side / right side / where they agree" — on
   `one-and-two-step-equations` (2), `variables-on-both-sides` (3),
   `identities-and-contradictions` (6), `modelling-with-linear-equations` (8)
   and `absolute-value-equations` (11). `identities-and-contradictions` fences
   it properly: "Draw each side as a graph, as the lab does. … The graphs are a
   preview — lines are Lines, Functions and Graphs — and the argument above does
   not depend on them." The other four panels never mention the graph at all. So
   on lesson 2 of course 2 a reader meets two plotted lines and a marked
   intersection point, and the lesson that defines an ordered pair, an axis and
   the graph of an equation is `the-coordinate-plane`, the first lesson of the
   *next* course. The first pass removed exactly this leak from the `check` lab
   — its finding 4 — and did not look at the other five modes.
2. **`compound-inequalities` (10) writes set-builder braces three lessons before
   `interval-and-set-builder-notation` (13) defines them.** Its `worked.lines`
   read `sets       A = { x : x ≥ 2 }      B = { x : x < 4 }`, and its `def`
   introduces `∩` and `∪` as notation to be used. The lesson is careful about
   *interval* notation — it says `(−∞, −2) ∪ [3, ∞)` is "the compact form … and
   'Interval and Set-Builder Notation' is about it" — and is silent about the
   brace-and-colon form it has just used in its own worked panel. Lesson 13's
   `def` then teaches `{ x ∈ ℝ : P(x) }` as if new, and its `concepts[2]` makes a
   point of the `∈ ℝ` that lesson 10 omitted.
3. `what-it-means-to-solve-an-equation` (1) `steps[1]` requires substituting a
   bracketed negative — "`3(−2) − 4`, never `3−2 − 4`" — which is Foundations of
   Algebra lesson 12 and is correctly a declared prerequisite. No violation;
   recorded because it is the one place the course could easily have had one and
   does not.

### Facts a reader would trust that are wrong

4. **`absolute-value-inequalities` counts four items in a list of six.** After
   the "Right-hand sides that end the question" `ul` — which holds
   `|2x + 1| < 0`, `|2x + 1| ≤ 0`, `|2x + 1| ≥ 0`, `|x + 3| < −1`,
   `|x + 3| > −1` and `|2x + 1| > 0` — the next `body` paragraph begins "None of
   these four needs a split". The `standard` asks the reader to "classify all
   four statements `|x| < 0`, `|x| ≤ 0`, `|x| > 0`, and `|x| ≥ 0`", which is where
   the four came from. This is the first pass's own repair 10 leaving a seam: it
   added the missing relations to the list and did not update the sentence that
   counts it. A reader following the section heading is told the enumeration is
   complete at four when six are printed.
5. **`ratio-proportion-and-percent` question 1's feedback names an operation that
   does not produce the number.** For `y/7 = 12/21` the cross products give
   `21y = 84` and `y = 4`; the `why` says "`28` divides by the wrong
   denominator." There is no denominator in the problem by which 84 yields 28.
   `28` is `4 × 7` — the correct answer multiplied by the denominator instead of
   divided by it, which is the standard reversal and is worth naming as such.
   The other two diagnoses in the same `why` are right (`9/4` inverts the final
   quotient; `84` is the cross product reported before the division).
6. **`interval-and-set-builder-notation` question 3 answers three distractors
   with a disjunction and leaves the reader to sort them.** For
   `{ x ∈ ℤ : 1 < x ≤ 4 }` the `why` ends "The other options either ignore the
   integer domain or include the excluded endpoint." Two of the three ignore the
   domain and one includes the endpoint, and the sentence does not say which is
   which — on the one question in the course whose whole subject is that `ℤ` and
   `ℝ` give different answers to the same condition.

### Distractors that are also true

7. **`modelling-with-linear-equations` question 3, option (b).** The stem is "A
   correct model for the required number of buses gives `b = 9/2`. Each bus must
   be whole. What should be reported?" and option (b) is "Use 5 buses, because
   9/2 rounds up." Five buses is the operationally correct answer to "the
   required number of buses", and the `why` concedes it in as many words:
   "whether 5 is acceptable depends on a different question, such as asking for
   at least enough capacity." A reader who read "required" as a capacity
   requirement — which is what the word means outside an equation — reasoned
   correctly and is told "Not quite." The correct option (c) is defensible too
   ("The exact-equality model has no allowable whole-number answer; revisit the
   question before rounding"), and the item is a good one; what it needs is a
   stem that says which question is being asked.
8. **`one-and-two-step-equations` question 3, option (c), is half true and the
   feedback has to open by saying so.** The stem is "Which first line of working
   on `4(x − 2) = 20` is wrong?" and option (c) is "Subtract 2 from both sides,
   giving `4x = 18`." The `why` begins "Subtracting 2 from both sides is legal,
   but it leaves `4(x − 2) − 2 = 18`". So the operation named in the option is
   correct and only the asserted result is wrong, while options (a), (b) and (d)
   pair a correct operation with a correct result. A reader who parses "first
   line of working" as the move rather than the move-plus-result has a defence,
   and the question would be airtight if the stem said "Which of these first
   lines is incorrectly completed?"
9. Beyond those two, the wrong answers hold up. I tried to argue for each of the
   thirty-nine and the remaining thirty-seven have no defence — including the
   three that come closest: `equations-with-fractions` q3 option (d) ("It can
   change them, which is why the answer must be checked"), which is true of a
   *variable* multiplier and is explicitly closed by the `why`; and
   `literal-equations-and-formulas` q3 option (c) ("Exactly when `c ≠ b`"), closed
   by "`c = b` merely makes the answer `0`, which is a perfectly good value."
   Both are the right way to handle a tempting distractor.

### Labs that do not agree with their own lessons

10. **`literal-equations-and-formulas`' lab answers two of its three quiz
    questions, and the quiz sits in the column beside it.**
    `EQ_PRESETS["literal"]` contains `("A = (1/2)bh,  for h", …)`, which is
    question 1, and `("ax + b = c,  for x", …)`, which is question 3. The lab
    returns the rearranged expression and, at `algebra_equations.py:1106`, the
    sentence "the answer is valid exactly when that expression is not zero" —
    which is question 3's correct option, "Exactly when `a ≠ 0`". Both answers
    are computed on the page by the widget the panel tells the reader to run.
11. **`absolute-value-equations`' lab opens on its own question 1.** The first
    entry of `EQ_PRESETS["absolute"]` is `|x - 3| = 5`, the preset the lab loads
    before the reader touches anything, and the lab splits it into cases,
    substitutes both candidates and marks the survivors. Question 1 is "Solve
    `|x − 3| = 5`", answer "`x = 8` or `x = −2`".
12. **`variables-on-both-sides`' lab preset 3 is its question 2.**
    `("2 - x = 4 - 3x", …)` is in `EQ_PRESETS["sides"]`, and the mode's whole
    output is both collecting routes solved to `x = 1`.
13. `modelling-with-linear-equations`' `model` presets are parameterised
    (`("consec", "3", "1", "48", "0")` fills `eqP1`–`eqP4`), so a reader can type
    5, 1, 65 and read question 2's answer off the lab. That is a weaker version
    of the same shape and is the price of a parameterised widget; it is worth
    naming only because two of the course's thirteen quizzes already leak this
    way outright.
14. **`ratio-proportion-and-percent` leaves four of its six presets outside the
    lesson's own scope.** `5/x = 15/9`, `2/3 = 8/x`, `2/(x + 1) = 3/(x - 1)` and
    `x/(x - 2) = 2/(x - 2)` all have a variable denominator, which the lesson
    repeatedly says is Rational and Radical Expressions' work. The panel does
    fence them and does name the two that are not — "Before running the first or
    third preset" — so this is honest; but a selector in which two entries are
    the lesson and four are a preview of a course five ahead is a strange
    instrument to hand a beginner, and the fencing sentence is the only thing
    standing between them.
15. The `linear` inequality mode's faded item (`7 − 4x > −9`) and the `solve`
    mode's faded item (`5 − 3x = −7`) are not presets. Both labs take free text,
    so both are enterable; `one-and-two-step-equations`' phrasing — "before
    opening the same equation in the lab" — reads as if a preset exists.

### Quiz feedback that does not answer the wrong answer

16. **Eleven `why` fields identify a distractor by its position among buttons
    the page never numbers.** `common.py`'s `QUIZ_SCRIPT` builds each option as
    `<button class="choice">` with `b.innerHTML = text` and no index, and
    `theme.py`'s `.choice-grid` is a bare one-column grid with no counter. The
    ordinals are countable, because the buttons do stack in source order, but the
    reader must count, and the course's own better explanations name the value
    instead. The instances are `what-it-means-to-solve-an-equation` q1,
    `equations-with-fractions` q1 (implicitly) and q3,
    `literal-equations-and-formulas` q2 and q3,
    `modelling-with-linear-equations` q1, `linear-inequalities` q2,
    `compound-inequalities` q1, `absolute-value-inequalities` q1 and q3, and
    `interval-and-set-builder-notation` q1 and q2.
17. `ratio-proportion-and-percent` q1 misdiagnoses `28` (item 5).
18. `interval-and-set-builder-notation` q3 answers three options at once (item 6).
19. `absolute-value-equations` q3 never mentions "Every real number", one of its
    four options, and it is the option a reader who solved only case 1 —
    `x − 1 = x + 3`, a contradiction — might reach for by elimination.
20. `what-it-means-to-solve-an-equation` q2 has two "Yes" distractors with
    different reasoning — (a) "because `0.66` rounds to `2/3`" and (c) "because
    `0.66` and `2/3` are the same number" — and the `why` answers only the
    second: "a nearby terminating decimal is a different number." (a)'s claim is
    true (`0.66` does round to `2/3` at two places) and its *inference* is what
    fails; that distinction is the lesson's whole subject and the feedback does
    not draw it.
21. `modelling-with-linear-equations` q2 says "`17` comes from using the wrong
    total offset." That is right — `5n = 65` gives `n = 13` and a largest of `17`
    — but "wrong total offset" does not name the offset or say it is the `+10`
    from `n + (n+1) + … + (n+4)`. It is the one vague clause in an otherwise
    precise `why`.

### Cognitive load and structure

22. **The quiz and the worked example render as the two cells of one `grid-2`,
    so the faded rehearsal is beside the question.** `render.py`'s `#practice`
    section emits `labs.QUIZ_MARKUP` and the worked panel — including every
    paragraph of `worked.after` — inside one `<div class="grid-2">`. The first
    pass's central repair was to add a faded rehearsal to every `worked.after`.
    The collisions in this course are milder than in course 1 but real:
    `identities-and-contradictions`' faded item is `4(x − 2) + 3 = 4x − 5` with
    the instruction to "predict the outcome and solution set", and question 1 is
    `5(x − 2) + 3 = 5x − 7` — the same shape with one digit changed, and the same
    answer type. `interval-and-set-builder-notation`' faded item converts
    `x ≤ −3 or x > 2` and question 1 converts `x < −1 or x ≥ 4`, with the
    bracket decision at the finite ends being the whole of both. Neither is a
    verbatim repeat; both are close enough that a reader can transfer the
    bracket pattern without re-deriving it.
23. **`ratio-proportion-and-percent` still carries seven ideas.** Ratio as a
    quotient; proportion as an equation; the unit-order discipline; the
    cross-product theorem with proof; the three percent questions; percent
    change with its base rule; and the successive-percent example — plus the
    fenced rational-equation preview. The first pass found this (its item 8) and
    responded by fencing the preview rather than by moving anything, so the fence
    works and the load is unchanged. The cheapest real cut is the percent-change
    material: `body`'s "For a change rather than a share, the whole is the
    *original* amount", the `example` about 20% up then 20% down, and
    `mistakes[2]`. All three are modelling decisions about which quantity is the
    base, and `modelling-with-linear-equations` is the next lesson and already
    owns "the equation's answer and the question's answer are different things".
    Moving them is content-only and changes no URL.
24. **`interval-and-set-builder-notation`'s retrieval now reaches what the first
    pass said it did not.** Question 1 is a union, question 2 is a set-builder
    read, question 3 is the `ℤ`-versus-`ℝ` distinction, and the faded item is a
    two-piece conversion. The first pass's finding 11 is discharged; I checked
    all four.
25. **The course outcomes cover the course, which is not true of courses 1 or
    3.** All four `outcomes` in `__init__.py` map onto lessons, and `not_covered`
    correctly fences quadratics, systems and sign-analysis inequalities. The
    first pass's finding 12 — that "solve any linear statement" overclaimed — is
    discharged: the outcome now reads "the one-variable linear equations and
    inequalities taught here".
26. A documentation-only seam: the module docstring of
    `scripts/mathpath/labs/algebra_equations.py` still says an inequality's
    answer is "printed in interval and set-builder notation from the same
    structure — so the four representations on screen cannot disagree." After the
    first pass's repair that is true of the `notation` and `quadratic` modes only.
    No learner sees it; anyone maintaining the lab does.

## Where a learner gets stuck

- At `one-and-two-step-equations`' lab, the second lesson of the second course,
  in front of two plotted lines, an intersection point and a legend reading
  "where they agree", with nothing on the page having defined an axis (item 1).
- At `compound-inequalities`' worked panel, at `A = { x : x ≥ 2 }`, three
  lessons before the brace notation is introduced (item 2).
- At `absolute-value-inequalities`' right-hand-side section, told that "none of
  these four" needs a split under a list of six (item 4).
- At `modelling-with-linear-equations` question 3, having answered "Use 5 buses"
  for a reason the feedback then grants (item 7).
- At `one-and-two-step-equations` question 3, having read "first line of
  working" as the operation, which the feedback agrees is legal (item 8).
- At `literal-equations-and-formulas`' quiz, able to answer two of three
  questions by running the preset named in the column beside it (item 10); and
  at `absolute-value-equations` question 1, where the lab has already loaded the
  question and solved it (item 11).
- At `ratio-proportion-and-percent`' quiz, told that `28` came from dividing by
  the wrong denominator when there is no such denominator (item 5).

## What the first pass caught, what it missed, and what I dispute

The prior assessment's diagnosis was sound and most of its repairs verify. The
faded rehearsals exist in all thirteen `worked.after` fields. The `check` lab no
longer plots or solves. The three inequality labs report inequalities, words and
a number line, and I confirmed this in the lab source rather than from the panel
copy: `preNotationRows` for `linear`, `setIneq`/`setWords` for `compound` and
`absolute`, `notationRows` only in `notation` and `quadratic`.
`equations-with-fractions` now teaches two ways to produce an LCD — listing
multiples and taking prime powers, with `6, 8, 12 → 24` worked and checked.
`literal-equations-and-formulas` now demonstrates a target on opposite sides
(`ax + b = cx + d`) and reads `b = 0` in `A = (1/2)bh` algebraically rather than
as "no triangle". `interval-and-set-builder-notation`'s retrieval reaches the
union, the set-builder form and the integer domain.

**What it missed.** It ran neither of the two audits this pass ran. It did not
try to argue for each wrong answer, so it did not find the two defensible
distractors (items 7 and 8) or the `28` that no named operation produces
(item 5). It did not read the preset lists against the quiz items, so it did not
find that the lab answers two of `literal-equations-and-formulas`' three
questions (item 10), opens on `absolute-value-equations`' question 1 (item 11),
and carries `variables-on-both-sides`' question 2 as preset 3 (item 12). It also
stopped at the `check` lab when it found the graph leak, and the same leak is
live in four other modes on four other lessons (item 1) — the fix it applied was
to one mode, not to the class. And its own repair to
`absolute-value-inequalities` left the sentence that counts the list behind
(item 4).

**What I dispute.** Two things.

First, its finding 4 said the `check` lab's panel "repeatedly said that it never
solves anything" while the implementation solved and revealed. The repair is
right and the framing is not quite: the problem was never that a lab computes
more than it says, it is that this lab computed *the next lesson's* act. The
same is true of the four graph modes it did not examine, and stating the finding
as a general rule — a lab may not display a representation the path has not
taught — is what would have caught them. I have stated it that way in item 1.

Second, its finding 8 said `ratio-proportion-and-percent`'s attached lab "went
further and accepted proportions whose cross product is quadratic", and its
repair fenced variable denominators as a course-5 preview. That fence is in
place and it is well written. But the finding understated the result: four of the
six presets are now outside the lesson's assessable scope, so the fence does not
reduce the load, it relabels two-thirds of the widget (item 14). And the load
finding itself — that the lesson carries too much — was correct and was not acted
on at all; the repair list addresses the preview and not the seven ideas. I have
named the specific cut that would.

## Repairs this pass recommends

None of these changes the URL space, so the five declarations in root `AGENTS.md`
§1 are untouched. Content edits are in `content/algebra/c2_equations/`; two items
touch `scripts/mathpath/labs/algebra_equations.py` and would need
`@chrome-renderer`. After any of them, `python3 scripts/build_paths.py` and the
gate set in `AGENTS.md` §7 must run, with `/usr/bin/python3`.

1. `absolute-value-inequalities`, the `body` paragraph after the right-hand-side
   `ul` (item 4). Change "None of these four needs a split" to "None of these
   needs a split", or to "six" if a count is wanted. Then check the `standard`,
   which asks for four statements and is correct as it stands, and leave it.
2. The four unfenced graph panels (item 1). Add one sentence to
   `one-and-two-step-equations`, `variables-on-both-sides`,
   `modelling-with-linear-equations` and `absolute-value-equations`'
   `lab.panel_intro`, modelled on the sentence
   `identities-and-contradictions` already has: the picture draws each side as a
   line and marks where they agree; lines are Lines, Functions and Graphs, and
   the trace above it is the argument. Four one-sentence additions, no lab change.
   The alternative — dropping those four modes from `EQ_PLOT_MODES` — is a lab
   change with a wider blast radius and loses a genuinely good figure; the fence
   is the better trade.
3. `compound-inequalities`, `worked.lines` (item 2). Either write the two sets as
   inequalities (`first: x ≥ 2`, `second: x < 4`) or add one clause to the `body`
   paragraph that already fences interval notation, saying that the brace-colon
   form is read "the set of `x` such that" and that lesson 13 gives it its rules.
   The first is the smaller edit and matches what the lab now prints.
4. `ratio-proportion-and-percent`, `quiz[0].why` (item 5). Replace "`28` divides
   by the wrong denominator" with "`28` is `4 × 7`: the cross product was divided
   correctly and then multiplied by the denominator again instead of left alone."
5. `interval-and-set-builder-notation`, `quiz[2].why` (item 6). Split the closing
   sentence: "Every real number between 1 and 4" and "`(1, 4]` as a real
   interval" ignore the `ℤ`; `{ 1, 2, 3, 4 }` respects the domain and keeps the
   endpoint the strict `<` excludes.
6. `modelling-with-linear-equations`, `quiz[2]` (item 7). Tighten the stem so the
   conceded reading is closed: "A model that sets capacity exactly equal to
   demand gives `b = 9/2` buses, and each bus must be whole. What should be
   reported about *that* model?" Keep option (b) and keep the `why`'s concession,
   which is the most useful sentence in the item.
7. `one-and-two-step-equations`, `quiz[2]` (item 8). Change the stem from "Which
   first line of working … is wrong?" to "Which of these first lines states its
   result incorrectly?" Nothing else in the item needs to move; the `why` already
   makes the distinction and would then be answering the question asked.
8. `literal-equations-and-formulas`, `quiz[0]` and `quiz[2]` (item 10). Replace
   both with formulas that are not in `EQ_PRESETS["literal"]`. For question 1,
   `V = (1/3)Bh` solved for `B` keeps the same act and the same distractor shapes
   (`3V/h`, `V/(3h)`, `3V − h`, `h/(3V)`). For question 3, state the condition
   question about a formula the lab does not carry — `px + q = rx + s` solved for
   `x` gives `(s − q)/(p − r)`, valid when `p ≠ r` — which also drills the
   collecting step the lesson added and the current item does not reach.
9. `absolute-value-equations`, `quiz[0]` (item 11). Change the numbers so the
   item is not the lab's default preset: `|x + 5| = 2`, with `x = −3` or
   `x = −7`, and distractors `x = −3` only, `x = −3` or `x = 3`, and `x = 3` or
   `x = 7`. Alternatively override `presets` from the lesson dict — `equation_lab`
   already honours `cfg.get("presets")` — and put a different two-case equation
   first. Changing the question is the smaller edit.
10. `variables-on-both-sides`, `quiz[1]` (item 12). Replace `2 − x = 4 − 3x` with
    an equation not in `EQ_PRESETS["sides"]`, keeping the same shape so the three
    diagnoses survive. `3 − 2x = 7 − 4x` gives `x = 2`, and the lesson's three
    named slips then give `5` (writing `2x = 7 + 3`), `−2/3` (subtracting `4x` on
    the left while cancelling it on the right, leaving `3 − 6x = 7`) and `2/3`
    (that slip with the sign lost in the division). Rewrite the `why` against
    those recomputed values rather than transplanting the current one.
11. `absolute-value-equations`, `quiz[2].why` (item 19). Add a clause for "Every
    real number": the first case reduces to `−1 = 3`, which rules out nothing and
    grants nothing; only the second case produces a candidate, and it is one
    number.
12. `what-it-means-to-solve-an-equation`, `quiz[1].why` (item 20). Answer option
    (a) separately from (c): `0.66` does round to `2/3`, and rounding is a
    statement about how close two numbers are, not about whether the equation
    comes out true — which is the difference the lesson is for.
13. All ordinal references in `why` fields (item 16). Replace "the second
    option", "the last two", "the third option" and "the last option" with the
    option's own value. The eleven sites are listed in item 16; the course's own
    `equations-with-fractions` q2 is the model to copy.
14. `ratio-proportion-and-percent` (item 23). Move the percent-change material —
    the `body` paragraph beginning "For a change rather than a share", the
    `example` "Why percents do not cancel out", and `mistakes[2]` — into
    `modelling-with-linear-equations`, where the base decision is a modelling
    decision. Rewrite `ratio-proportion-and-percent`'s question 2 (the 80-to-92
    increase) as a straight part/whole question and give
    `modelling-with-linear-equations` a percent-change item in its place. Content
    only; no URL changes.
15. `scripts/mathpath/labs/algebra_equations.py`, module docstring (item 26).
    Amend the paragraph about `inequality_lab` to say that the four
    representations are printed together in the notation mode and that the
    earlier modes print only what the path has taught by then, which is what
    `preNotationRows` implements and why. `@chrome-renderer` owns this file.
