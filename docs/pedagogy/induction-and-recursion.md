# Pedagogy assessment — Induction and Recursion (discrete mathematics, course 3)

First assessment, formed from the twelve lesson dicts in
`content/discrete_math/c3_induction/` (`part_a.py`, `part_b.py`, `__init__.py`)
and the lab kits they render through (`scripts/mathpath/labs/induction.py`
for the induction lab and the recurrence lab; `scripts/mathpath/labs/algorithms.py`
for the three lessons that borrow course 8's algorithm lab), as they stand on
`main` at 3df909f. No prior assessment exists for this course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `the-well-ordering-principle`, `mathematical-induction`,
`induction-with-sums-and-products`,
`induction-with-inequalities-and-divisibility`, `strong-induction`,
`recursive-definitions`, `structural-induction`, `recursive-algorithms`,
`recurrence-relations`, `solving-linear-recurrences`,
`divide-and-conquer-recurrences`, `loop-invariants-and-correctness`. The
course declares courses 1–2 as prerequisites ("proof technique and set
notation"), so it is judged against what those teach: direct proof of a
conditional, contradiction, `a | b`, the sum-of-two-odds theorem of course 1
lesson 12, and course 1 lesson 14's point that checking cases is not a
proof — which this course's home says is the gap it exists to close.

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** Derive
  induction from well-ordering unaided (`the-well-ordering-principle`); prove
  `2 + 4 + ⋯ + 2n = n(n+1)` and mark the line where the hypothesis entered
  (`mathematical-induction`); prove the sum of the odd squares
  (`induction-with-sums-and-products`); count the base cases from the reach
  of the step before writing any, for 4¢ and 7¢ stamps from 18
  (`strong-induction`); define the no-`11` strings recursively and unroll
  `2, 3, 5, 8, 13, 21` (`recursive-definitions`); match a proof to a
  definition clause by clause, with the concatenation case flagged as the one
  that needs thought (`structural-induction`); discharge termination and
  correctness for a recursive Fibonacci in a paragraph
  (`recursive-algorithms`); derive the domino-tiling recurrence and check
  `a₁` to `a₄` by drawing (`recurrence-relations`); solve
  `6aₙ₋₁ − 9aₙ₋₂` and check the closed form at a term not used in the fitting
  (`solving-linear-recurrences`); decide the case from the tree before the
  formula (`divide-and-conquer-recurrences`); state an invariant strong enough
  that the exit condition closes the argument
  (`loop-invariants-and-correctness`). None is "understand X".
- **The induction lab is adversarial on purpose, and the course is built
  around it.** `n² + n + 41` is prime for `n = 0` to 39 and `40² + 40 + 41 =
  1681 = 41²`; the chord-region count reads `1, 2, 4, 8, 16` and then 31.
  Both are computed in exact integers by the shipped JavaScript, both survive
  every check a reasonable reader runs, and the status line refuses to call a
  run of confirmations a proof. The course home's `how_to`, `footer_lead`
  and lesson 1's panel all say so. That is the lesson course 1 lesson 14 set
  up, delivered where it lands.
- **The recurrence lab computes the closed form and the iteration
  separately and compares them**, as its docstring promises, and every preset
  agrees on every term (executed: `fib`, `hanoi`, `geo`, `two`, `rep`, `lin`,
  `merge` all match through 12 terms). `two` is the lesson-10 worked example
  with the same constants `A = −2`, `B = 3`; `rep` is quiz question 1's
  recurrence; `merge` is lesson 11's substitution `n = 2ᵏ` made concrete.
- **The three failure modes are named at the point of error and they are
  the real ones**: no base case (`n = n + 1`), an unused hypothesis, and a
  step proved for one `k` — plus the horses, with the flaw located at `k = 1`
  exactly (`mathematical-induction`); the base case moved by the claim, and
  the sign of a factor before multiplying an inequality
  (`induction-with-inequalities-and-divisibility`); too few base cases when
  the step reaches back several, and the case outside the hypothesis range
  (`strong-induction`); the recursion that does not decrease and the missing
  closure sentence (`recursive-definitions`); the forgotten clause and the
  hypothesis used for one part only (`structural-induction`); "correct if it
  terminates" mistaken for correct (`recursive-algorithms`,
  `loop-invariants-and-correctness`); overlapping cases in the split
  (`recurrence-relations`); the missing `n` on a repeated root and the
  collision case (`solving-linear-recurrences`); `a` and `b` swapped and `Θ`
  read as running time (`divide-and-conquer-recurrences`); the invariant too
  weak to close (`loop-invariants-and-correctness`).
- **The worked examples are chosen to expose the mechanism.** The
  minimal-counterexample proof of the division algorithm shows why the set
  must be shown nonempty and must lie in `ℕ`; the `n! > 2ⁿ` proof writes
  "`k + 1 > 0`" beside the multiplication; the 4¢/5¢ proof says in so many
  words why four bases and not one, and the `after` gives the Frobenius
  number `20 − 4 − 5 = 11` as the reason the claim starts at 12; the
  fast-exponentiation proof shows an even branch that reaches `n/2`, so the
  reader sees why ordinary induction supplies the wrong hypothesis; the
  lesson-10 example checks `a₂ = 19` against the recurrence, a term not used
  in the fitting, and the `after` says why that makes it a check; Euclid's
  invariant is "the gcd never changes", which the `after` correctly calls
  more informative than what the loop does.
- **The arithmetic a reader would trust is right.** `2⁵ = 32 > 25`;
  `(k−1)² ≥ 2` for `k ≥ 3`; `2k² + 7k + 6 = (k+2)(2k+3)`; the geometric
  step; `Σ i·i!` at `n = 1`; `3(m + k² + k + 1)`; the postage bases
  `8, 9, 10` and `12, 13, 14, 15`; `H₆₄` in seconds is about 585 billion
  years (`2⁶⁴ / 31 557 600 ≈ 5.85 × 10¹¹`); the codeword recurrence
  `aₙ = aₙ₋₁ + 3ⁿ⁻¹` with `a₂ = 5`; the unrolled Hanoi sum; Binet's
  constants; `A = −2, B = 3` and `a₂ = 19` both ways; `(1 + n)3ⁿ` at `a₃ =
  108` both ways for the standard; `log₂ 3 ≈ 1.585`, `log₂ 7 ≈ 2.807`;
  `T(n) = 3T(n/4) + n` shrinking by `3/4` per level. The lab's binary
  search worst case equals `⌊log₂ n⌋ + 1` for every `n` from 2 to 64
  (executed), which is what the lesson-8 panel claims.
- **Prerequisite order across the path is sound in both directions.**
  Inbound: course 5's geometric series → lesson 3; course 4's case split →
  lesson 9 and Binet → lesson 10; course 6's loop invariant → lesson 12 and
  its well-ordering proof of the division algorithm opens where lesson 1's
  worked example ends; course 7's structural induction → lesson 7 and binary
  trees → lesson 6; course 8's termination → lesson 8, correctness → lesson
  12, recurrences → lesson 11, sums → lesson 3. Every one lands on a lesson
  that teaches what is cited. Inside the course, induction (1–5) → recursion
  (6–8) → recurrences (9–11) → correctness (12) is the only order that works:
  lesson 5's strong induction is what lesson 7's two-subtree hypothesis and
  lesson 8's `n/2` branch need, lesson 3's geometric sum finishes lesson 9's
  unrolling, and lesson 10's substitution is what lesson 11 reads back.

## What it teaches badly, or claims and does not deliver

### Facts a reader would trust that are wrong

1. **`divide-and-conquer-recurrences` numbers the master-theorem cases one
   way in its worked example and quiz, the other way in its mistakes, and
   the lab on the page numbers them the second way.** The worked example
   has `log₂2 = 1 < 2 → CASE 1` (root dominates) and `log₂8 = 3 > 2 → CASE
   3` (leaves dominate); quiz question 1 marks "Case 3, `Θ(n²)`" correct for
   `4T(n/2) + n`. Mistake 2 then says `f(n) = n log n` "falls between cases
   2 and 3" — but `n log n` sits between the balanced case and the case
   where the *root* dominates, which the lesson has just called case 1. That
   sentence is using the textbook numbering (CLRS: case 1 = leaves), while
   the rest of the lesson uses the reverse. The lab's table prints
   `case 1 (a > b^d)` for the leaf-dominated rows, so a reader who does the
   standard ("check that the master theorem gives the case your tree
   predicted") finds `8T(n/2) + n²` labelled case 1 in the lab and CASE 3 in
   the worked example above it. Course 8 lesson 7, the other page that uses
   this lab, also says "in case 3 the cost is all at the leaves", so the
   course's convention is the path's convention and the lab's labels are
   the one thing on both pages that disagree.
2. **`recursive-definitions` says "course 4 lesson 14 counts" the
   well-formed parenthesis strings.** No lesson on the path counts them:
   there is no Catalan number anywhere in `content/discrete_math/`, and
   course 4 lesson 14 is `choosing-a-counting-method`. The same lesson sends
   the reader to "course 7 lesson 12" to traverse binary trees; that is
   `spanning-trees`, and tree traversals are lesson 11.
3. `recursive-algorithms`' standard says the exponential call count of naive
   Fibonacci is something "lesson 11 and course 8 both return to". Lesson
   11 is the master theorem and never mentions Fibonacci; the growth rate
   `φⁿ` that the lesson's own note quotes as "about `1.6ⁿ`" is lesson 10's
   Binet formula. The course home's `not_covered` sends the reader to
   "course 4 lesson 13" for generating functions; that is
   `combinatorial-proof`, and generating functions are lesson 12.
4. `divide-and-conquer-recurrences` uses `Θ(·)` in its key, theorem, three
   examples, worked example, quiz and mistakes, and never says what it
   means. The notation is defined in course 8 lesson 4, five courses later.
   Mistake 3 even corrects a misreading of `Θ` ("it describes asymptotic
   growth") on a page that has not said what it describes. A one-line
   definition — between two constant multiples of `g(n)` for all large `n`
   — is all the theorem needs and all the reader has.

### Practice that repeats the worked example

5. **`induction-with-inequalities-and-divisibility`'s standard is the
   lesson's own theorem.** The body proves `2ⁿ > n²` for `n ≥ 5` in full,
   with the bridge `2k² ≥ (k+1)²` isolated and its range `k ≥ 3` stated;
   the lab on the page has that statement selected and the panel says why
   the base case is 5; the quiz asks for the base case. The standard then
   asks: "Determine the smallest `n` for which `n² < 2ⁿ` holds and stays
   true, prove it from there, and state explicitly the side inequality your
   step needed." Every part of that has been done on the page. It is a
   worked example re-asked, not independent practice, and the act the
   lesson names — "locate a base case by testing rather than by assuming"
   — is not tested by a claim whose base case the page has printed three
   times.
6. **`induction-with-sums-and-products` has no product.** The title, slug
   and `Π` in the summation definition promise one; the key is four sums,
   the body proves two sums and shows two sum arguments without induction,
   the worked example is a sum, and the standard is a sum. A reader who
   arrives at course 8 lesson 5's products has been shown the word and
   nothing else. One telescoping product, proved by the same peel-substitute-
   factor moves, is the whole gap.
7. `solving-linear-recurrences`' standard says the repeated root "makes this
   the case people get wrong", and the lesson agrees: mistake 1 and quiz
   questions 1 and 2 are about it. The body gives the theorem, the reason
   for the extra `n`, and no example of it being solved; the only worked
   solution is the distinct-roots case. The lab's `rep` preset is exactly
   the missing example (`4aₙ₋₁ − 4aₙ₋₂`, `a₀ = 1`, `a₁ = 4`, closed form
   `(1 + n)2ⁿ`) and the panel does not point at it. Worked example → faded
   guidance → independent practice is missing its middle step in the case
   the lesson itself says matters most.

### Distractors that are also true

8. **`structural-induction`, question 2: "For a tree `node(v, L, R)`, the
   inductive hypothesis is: … the claim for trees of smaller height."**
   That is a correct inductive hypothesis — strong induction on height
   proves the lesson's own node-count theorem — and it is marked wrong with
   a `why` that does not mention it. The lesson's point is that structural
   induction assumes the claim for the *parts*, which is what the marked
   answer says; the distractor needs to be something that is not a
   hypothesis at all.

### Labs that do not agree with their own lessons

9. **`the-well-ordering-principle`'s lab shows the lesson's idea and the
   panel does not say so.** The lab's "First failure" figure is the least
   element of `S = {n : P(n) is false}` — the set the lesson's derivation
   of induction builds and the set every minimal-counterexample proof takes
   the least element of. The panel talks only about the two false
   statements (rightly), and the "Inductive step" note under the controls
   speaks lesson 2's language one lesson early without being fenced.
10. **The first false statement is never named.** Lesson 1's panel says two
    statements are false and tells the reader to find them; lesson 5's panel
    names the chord count. `n² + n + 41` is named nowhere in any lesson. A
    reader who did not find it on lesson 1 leaves the course not knowing what
    it was, and the course home's `how_to` ("meeting them is the reason this
    course exists") has promised a meeting that may not happen. Lesson 2 —
    whose body is "three ways to get it wrong" and whose lab note for that
    statement reads "there is no inductive step here" — is where it belongs.
11. `recursive-definitions` and `recurrence-relations` both open the
    recurrence lab on the Tower of Hanoi, whose lab preset is `a₀ = 0` while
    both lessons define `H₁ = 1` as the base. The sequences agree from `a₁`
    on (0, 1, 3, 7, 15, …), and the difference is a small instance of the
    lesson's own point about base clauses; neither panel mentions it, so a
    careful reader sees a base case that does not match the one on the page.
12. `loop-invariants-and-correctness`' lab counts comparisons — course 8's
    question — on a page about correctness, and the panel describes the
    count without saying that a count is not a proof or what, if anything,
    on the lab is this lesson's. Executed at the shipped `n = 20`: bubble
    190 (`= 20·19/2`), insertion 112, merge 66; only the insertion figure
    depends on the data, because its inner `while` loop stops at the gap —
    the same exit the maintenance argument reasons about.
13. `recursive-algorithms`' panel gives the bound and not the caveat the
    lesson is built on: the array the lab searches is sorted, which is what
    correctness needs and termination does not, so on unsorted data the
    counted worst case would be identical and the answer wrong — quiz
    question 3, on the lab. At `n = 32` the counts are 32 and 6.
14. `solving-linear-recurrences`' panel says each preset shows its
    characteristic equation and constants, which is true, and says nothing
    about which presets are this lesson's cases: `rep` is the repeated root
    and `lin` (`aₙ = aₙ₋₁ + n`) is the collision case from the lesson's own
    table — root 1, `f(n) = n`, so the particular solution is quadratic.
    `recurrence-relations`' panel could send the reader to `lin` for the
    same reason from the other side: it unrolls to the triangular numbers,
    lesson 3's first identity arrived at as a recurrence.

### Quiz feedback that does not answer the wrong answer

15. The `why` fields are specific where the lesson has a named error
    (`mathematical-induction` Q2 and Q3; `strong-induction` Q2;
    `recurrence-relations` Q1, which answers all three distractors;
    `recursive-algorithms` Q3). Where they are not, the reader who chose a
    particular wrong answer gets the rule restated:
    `the-well-ordering-principle` Q1 says nothing about the least elements
    of the other three sets (6, 2, 2) and Q3 nothing about why "the set
    being infinite" or "assuming the claim is true" is not the lever;
    `mathematical-induction` Q1 does not say that "`P(n)` for all `n`" is
    the circularity mistake 3 names; `induction-with-sums-and-products` Q1
    does not say what `n(n+1)(2n+1)/6` is, or that `n⁴/4` is only the
    leading term; `strong-induction` Q2 does not say what `3 + 5 = 8`
    explains (where the claim starts, not how many bases);
    `recursive-definitions` Q1 and `recurrence-relations` Q2 do not say that
    the values and the coefficients change the sequence, never the count;
    `solving-linear-recurrences` Q1 does not identify `r² = 4r + 4` as the
    sign of `c₂` lost or `r = 4` as the first-order recurrence, and Q3 does
    not say when each of the other three guesses is the right one;
    `divide-and-conquer-recurrences` Q1 does not say what `Θ(n)` and the
    balanced case would have needed; `loop-invariants-and-correctness` Q3
    does not address "correct on some inputs", which is the everyday reading
    the term exists to displace.

### Cognitive load and structure

16. **`solving-linear-recurrences` carries the characteristic equation,
    distinct roots, repeated roots, the nonhomogeneous decomposition, the
    particular-solution table and the collision case.** It is the strongest
    split candidate in the course and I have chosen not to split it: the
    lesson's `concepts_intro` correctly says it rests on one guess and one
    fact (solutions add), the repeated root and the collision are the same
    move (multiply by `n`) and the body says so, and the lab shows every case
    on one control. What it lacked was the middle rung of the ladder for the
    repeated root (item 7), which is added rather than a lesson.
17. `induction-with-inequalities-and-divisibility` teaches two families in
    one lesson and says so in its title; the shared idea is that the base
    case and the target of the step both move, and the four steps state it
    as one method. Not split.
18. `recursive-algorithms` proves three algorithms and works a fourth; the
    single idea is the two obligations, and each algorithm is there to show
    a different decreasing quantity. Not split.
19. The course outcomes name four acts and omit the one lessons 8 and 12
    share and the `syllabus_intro` singles out ("12 applies all three to
    program correctness"): prove an algorithm correct, termination and
    correctness separately. Course 8 lesson 2 cites this course for exactly
    that act.
20. The induction lab's column header reads `Σ i` on lessons 1 and 2, one
    lesson before lesson 3 defines the notation; the select label spells the
    sum out, so nothing is lost. Recorded, not repaired — it is lab core,
    and the path's prerequisites page says `Σ` is explained "where it first
    appears", which lesson 3 does.

## Where a learner gets stuck

- At `divide-and-conquer-recurrences`' standard, with the worked example
  saying CASE 3 for `8T(n/2) + n²` and the lab on the same page printing
  `case 1` for the same row (item 1); and at mistake 2, trying to place
  `n log n` "between cases 2 and 3" on the lesson's own numbering.
- At `induction-with-inequalities-and-divisibility`'s standard, asked to
  locate a base case the page has already printed (item 5).
- At `solving-linear-recurrences`' standard, solving a repeated root with no
  solved example of one to compare against (item 7).
- At `structural-induction` question 2, having answered "trees of smaller
  height" for a correct reason (item 8).
- At `recursive-definitions`, sent to course 4 lesson 14 for a count that is
  not there and to course 7 lesson 12 for a traversal that is in lesson 11
  (item 2).
- At the end of `strong-induction`, knowing one of the two false statements
  and never told the other (item 10).
- At `divide-and-conquer-recurrences`' key, reading `Θ(n log n)` with no
  definition to look up (item 4).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered, so the five URL declarations are untouched. Every content edit is
in `content/discrete_math/c3_induction/` and the pages are rebuilt from it.
One edit is in lab core, `scripts/mathpath/labs/algorithms.py`, and is
label-only: the master-theorem table's case labels are swapped so `a < bᵈ`
reads case 1 and `a > bᵈ` case 3, matching this lesson and course 8 lesson
7, the two pages that render it; no arithmetic in the lab changes. Every
figure a panel now states was obtained by executing the shipped lab
JavaScript at the shipped preset and `n`.

- `the-well-ordering-principle`: the panel names the "First failure" figure
  as the least element of `S = {n : P(n) is false}` and fences the
  "Inductive step" note as lesson 2's; question 1's `why` gives the least
  element of each other set; question 3's `why` answers the three
  distractors.
- `mathematical-induction`: the panel names `n² + n + 41` as the first false
  statement, with `40² + 40 + 41 = 1681 = 41²`, and reads its lab note
  ("there is no inductive step here") as the difference between it and the
  identity above it; question 1's `why` answers "`P(n)` for all `n`" and
  "`P(k+1)`".
- `induction-with-sums-and-products`: a product section added after the
  telescoping sums — `Π_{i=2}^{n} (1 − 1/i²) = (n+1)/(2n)` for `n ≥ 2`,
  proved by peeling the last factor, substituting and factoring
  `1 − 1/(k+1)²` as `k(k+2)/(k+1)²`, with the base `3/4` checked; the
  summary and step 2 say the pattern peels a factor as readily as a term;
  the standard adds the two-line product `Π_{i=2}^{n} (1 − 1/i) = 1/n`; the
  panel names the cubes columns as question 1's identity; question 1's
  `why` identifies each distractor.
- `induction-with-inequalities-and-divisibility`: standard replaced by
  `2ⁿ > n³`, true at `n = 1`, false from 2 to 9, true from `n = 10` on
  (`1024 > 1000`), so the reader must keep testing past the first failure;
  the bridge `2k³ ≥ (k+1)³` is false at `k = 3` (`54 < 64`) and true from
  `k = 4` (`128 ≥ 125`), and the standard asks for that range and for the
  observation that the base case sits well past where the bridge starts.
- `strong-induction`: question 2's `why` says what `3 + 5 = 8` explains and
  that the worked example's step reaches back four.
- `recursive-definitions`: the parenthesis strings are counted by the
  Catalan numbers, which the path does not reach; binary trees are traversed
  in course 7 lesson 11; the panel notes the lab's `a₀ = 0` against the
  lesson's `H₁ = 1` and that the two agree from `a₁`; question 1's `why`
  says the values change the sequence, not the count.
- `structural-induction`: question 2's fourth option is now "the claim for
  the root value `v`", and the `why` answers all three — `L` alone leaves
  `R` unproved, the whole tree is what is to be proved, and `v` is not a
  tree.
- `recursive-algorithms`: standard's pointer now says the `φⁿ` growth is
  lesson 10's root and the fix is course 8 lesson 10's; the panel gives the
  counts at `n = 32` (32 and 6) and says the array is sorted, which
  correctness needs and termination does not.
- `recurrence-relations`: the panel notes the `a₀ = 0` base and sends the
  reader to `aₙ = aₙ₋₁ + n`, which unrolls to `0, 1, 3, 6, 10, 15`;
  question 2's `why` says the coefficients change the values, not the count.
- `solving-linear-recurrences`: a solved repeated-root example added after
  the theorem — `4aₙ₋₁ − 4aₙ₋₂`, `a₀ = 1`, `a₁ = 4`, `(A + Bn)2ⁿ` with
  `A = 1`, `B = 1`, checked at `a₂ = 12` both ways, and the contradiction
  (`C = 1` and `C = 2`) that appears when the `n` is forgotten; the panel
  points at the `rep` preset as that example and at `lin` as the collision
  case; question 1's `why` identifies `r² = 4r + 4` and `r = 4`; question
  3's `why` says when each other guess is right.
- `divide-and-conquer-recurrences`: a definition of `Θ(g(n))` added before
  the theorem, deferring the precise version to course 8 lesson 4; the key
  labels the cases 1, 2, 3 in the order of the comparison; the body says
  some texts number them the other way and to name a case by what dominates
  when in doubt; mistake 2 places `n log n` between the balanced case and
  the root-dominated case by name; the panel says the lab numbers the cases
  as the lesson does and that the last row (`log₄ 2 = 0.5 < 1`) is the
  standard's case; question 1's `why` says what `Θ(n)` and the balanced
  case would have needed; the lab labels are swapped to match.
- `loop-invariants-and-correctness`: panel rewritten — a count is course
  8's question and not a proof; at `n = 20` bubble 190, insertion 112, merge
  66; only the insertion figure depends on the data, because its inner loop
  stops at the gap, and the invariant holds however many comparisons that
  took; question 3's `why` answers "correct on some inputs".
- Course home (`__init__.py`): a fifth outcome names the act lessons 8 and
  12 share (termination by a decreasing bounded quantity, correctness by
  induction on the input or by an invariant); `outcomes_intro` includes it;
  `how_to` item 2 says lessons 2 and 5 name the two false statements; the
  generating-functions pointer says course 4 lesson 12.
