# Pedagogy assessment — Algorithms and Complexity (discrete mathematics, course 8)

First assessment, formed from the twelve lesson dicts in
`content/discrete_math/c8_algorithms/` (`part_a.py`, `part_b.py`, `__init__.py`)
and the one lab they all render through, the algorithm workbench in
`scripts/mathpath/labs/algorithms.py`, as they stand on `main` at f081e81. No
prior assessment exists for this course (`docs/pedagogy/prior/` holds none).

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `algorithms-and-pseudocode`, `correctness-and-termination`,
`growth-of-functions`, `big-o-notation`, `analysing-iterative-algorithms`,
`searching-and-sorting`, `divide-and-conquer`,
`recursion-trees-and-amortised-analysis`, `greedy-algorithms`,
`dynamic-programming`, `complexity-classes`,
`decidability-and-the-halting-problem`. The course declares courses 1–7 as
prerequisites ("especially induction, recurrences and graphs") and points
into courses 1, 2, 3, 4, 6 and 7, so it is judged against what those teach:
propositions and the exclusion of self-reference (course 1 lesson 1), SAT
(course 1 lesson 6), proof by contradiction (course 1 lesson 13),
counterexamples (course 1 lesson 14), Cantor's diagonal argument (course 2
lesson 13), the sum and geometric-series formulas (course 3 lesson 3), the
decreasing measure for a recursive algorithm (course 3 lesson 8), the master
theorem and its case numbering (course 3 lesson 11), loop invariants (course
3 lesson 12), the permutation count (course 4), modular exponentiation by
squaring (course 6 lesson 8), Euler against Hamilton (course 7 lesson 7),
Dijkstra (course 7 lesson 9), the binary-tree height bound (course 7 lesson
10) and the cut property (course 7 lesson 12). Every one of those
cross-course pointers was checked against the real lesson order of the
packages, and every one resolves; every intra-course pointer (lesson 1's map
of the course, lesson 5's sum rule "of lesson 4", lesson 6's "lesson 7's
master theorem", lesson 9's "lesson 10 handles it", lesson 11's "lesson 12")
is right too. Every figure quoted below was recomputed by hand, and every lab
figure by executing the shipped lab JavaScript at the shipped preset.

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** Write
  the specification before the pseudocode (`algorithms-and-pseudocode`);
  test the invariant at exit first (`correctness-and-termination`); find a
  crossover point (`growth-of-functions`); produce witnesses without being
  asked (`big-o-notation`); turn a triangular nest into a sum
  (`analysing-iterative-algorithms`); state the lower bound and why it
  holds (`searching-and-sorting`); say which parameter to attack
  (`divide-and-conquer`); produce the geometric series yourself
  (`recursion-trees-and-amortised-analysis`); attempt the exchange
  argument before trusting a greedy rule (`greedy-algorithms`); write the
  recurrence before any code (`dynamic-programming`); say what the
  classification changes (`complexity-classes`); reproduce the halting
  proof from memory (`decidability-and-the-halting-problem`). None is
  "understand X".
- **The course has one spine and states it at both ends.** Lesson 1 fixes
  the order — correctness, then cost, then a better method — and says why
  the temptation runs the other way; lesson 12's last paragraph reads the
  whole path back. Lesson 3 draws the polynomial/exponential line with a
  theorem (a `k`-fold speed-up buys `k`, `√k`, or `log₂ k` added) and
  lesson 11 makes that line the definition of tractable. Lesson 4's "the
  witnesses are the proof" is the course's method, and lesson 6's lower
  bound is the course's one impossibility result before lesson 12's.
- **The easy/hard contrasts are taught as content.** Euler against
  Hamilton (`complexity-classes`' worked example, picking up course 7
  lesson 7), shortest against longest simple path (`dynamic-programming`:
  "two problems whose statements differ by one word, on opposite sides of
  tractability"), amortised against average-case (`recursion-trees-and-
  amortised-analysis`), NP-complete against undecidable (lessons 11 and 12,
  each naming the other).
- **The misconceptions named are the real ones.** A step left to
  judgement; optimising before proving; an invariant that is too weak;
  comparing at one input size; hardware fixing exponential cost; `O` where
  `Θ` is meant; "at least `O(n)`"; "quicksort is `O(n log n)`";
  multiplying dependent loop bounds; binary search on unsorted data; the
  lower bound applied to all sorting; swapping `a` and `b`; optimising the
  combining step in the leaf-dominated case; amortised read as
  average-case; greedy trusted because it seems reasonable; testing
  instead of proving; memoising a divide-and-conquer algorithm; NP read as
  "not polynomial"; NP-complete read as unsolvable; undecidable read as
  very hard.
- **The numbers are almost all right.** Lesson 3's table (`log₂ 10⁶ =
  19.9`, `2¹⁰⁰ = 1.27 × 10³⁰`, `4 × 10¹³` years, three thousand times the
  age of the universe, 67% / 98% / 99.8%); `108n²` and `C = 5` at `n ≥
  10`; the `2·log₂ n` versus `n − 1` comparison at `n = 1000`; the three
  loop nests; `⌊log₂ 16⌋ + 1 = 5`; the master table (`log₂ 7 = 2.807`);
  Karatsuba's identity; the Fibonacci call counts 177, 2 692 537 and
  `4.07 × 10¹⁰`; the doubling array's 15 copies, total 31, worst 9, and
  120 for growing by one; the interval-scheduling instances; the coin
  table to 8; the halting proof. All recomputed and all correct. The
  exceptions are items 1–4 below.

## What it teaches badly, or claims and does not deliver

### Facts a reader would trust that are wrong

1. **`searching-and-sorting`'s worked example quotes counts the lab does
   not produce.** "Measured by running each algorithm on the same shuffled
   array": bubble 120, insertion 62, merge 48 at `n = 16`. The lab's
   shuffled array of 16 (`8 16 9 2 12 6 3 15 14 1 5 11 10 4 13 7`, the
   same for every reader by design) gives insertion sort **77**; 120 and
   48 are right. The `n = 1000` line says "merge ≈ 8 700"; on the lab's
   array it is **7 387** (bubble 499 500 is right). The course footer
   promises that "every operation count on this course is produced by
   executing the algorithm with a counter"; these two were not.
2. **`growth-of-functions` converts operations to time at two different
   rates in one paragraph.** "About 20 million operations and `10¹²` — the
   difference between a fraction of a second and about a fortnight." At
   the billion operations a second the same lesson uses two paragraphs
   later (`2¹⁰⁰` "at a billion operations per second … `4 × 10¹³` years"),
   `10¹²` is about seventeen minutes; a fortnight needs a million a second,
   at which `2 × 10⁷` is twenty seconds, not a fraction of one.
3. **`growth-of-functions`' worked example rounds the crossover into an
   equality.** "`n = 1000`: `100·10 = 1000 = 1000`, equal" and "loses on
   every input below 1000". `100 log₂ 1000 = 997`, and `100 log₂ n` first
   drops under `n` at `n = 996`. Close, and stated as exact.
4. **`algorithms-and-pseudocode`'s panel overstates the gap and opens
   where the reader cannot see it.** "At `n = 64` they differ by nineteen
   orders of magnitude": `2⁶⁴ / log₂ 64 = 1.8 × 10¹⁹ / 6 ≈ 3 × 10¹⁸`,
   eighteen and a half. The lab opened at `n = 16`, where the table ends
   at `2¹⁶ = 65 536`.
5. **`searching-and-sorting`'s lower-bound proof leans on Stirling's
   approximation**, which nothing on the path teaches, for a step that
   `n! ≥ (n/2)^{n/2}` covers in one line; and it cites course 7 lesson
   10's height bound "with `L` leaves" where that lesson states it in
   vertices (`2^{h+1} − 1`), so the reader who follows the pointer does
   not find the sentence quoted.

### A lab that reported wrong arithmetic

6. **`big-o-notation`'s witness search reported false relations as true.**
   The mode searched `C ≤ 1000`, `k ≤ 40` and checked the bound on
   `k ≤ n ≤ 4N` with `N ≤ 64`. At the shipped preset a reader who sets
   `f = n²`, `g = n` — the body's own disproof, directly above the lab —
   was told "**n² = O(n)**, witnessed by `C = 100` and `k = 1`: for every
   `n ≥ 1`, `f(n) ≤ 100·g(n)`". Likewise `n log₂ n = O(n)` with `C = 10`,
   `n³ = O(n²)` with `C = 100`, `log₂ n = O(1)` with `C = 10`, at every
   slider setting. The status even said "the search is honest: if no pair
   in the grid works, the lab says the relation looks false rather than
   inventing a constant" — true, and beside the point, since for any
   finite range some constant in the grid works. `labcheck` cannot see
   this and nothing in `mathcheck` covered the course. The correct pairs
   it found (`C = 4`, `k = 13` for `3n² + 5n + 100` against `n²`) were
   never quoted by the panel.

### Labs that do not agree with their own lessons

7. **`correctness-and-termination` opened on a sorting count.** The lesson
   is invariants and termination; its worked example is `POWER(x, n)` with
   the invariant `result · base^m = xⁿ`; the lab mode was `sort`, and the
   panel said "insertion sort's count depends on the data" on a lab that
   had no control for the data. Nothing on the page ran an invariant.
8. **`analysing-iterative-algorithms` counted nothing it analysed.** The
   worked example is three loop nests and the standard a fourth; the lab
   was `sort` at `n = 24`, again with the data-dependence panel and no
   input-order control, so the third mistake ("insertion sort is `Θ(n)` on
   sorted input and `Θ(n²)` on reversed input") could not be shown.
9. **`searching-and-sorting` opened at `n = 24` on a worked example at
   `n = 16`**, and its panel quoted no figure. The `search` mode — linear
   against binary, the one mode matching the lesson's title — was opened
   by no lesson on the course.
10. **`divide-and-conquer`'s master mode took no input.** A fixed
    eight-row table; the worked example's three recurrences (`4T(n/2) + n`,
    then `d = 0`, then `a = 3`) and the standard's `9T(n/3) + n²` could not
    be entered, so the lesson's act — say which parameter to attack —
    could not be tried.
11. **`recursion-trees-and-amortised-analysis` opened on the growth plot
    with a panel about the doubling array's copies.** Nothing on the page
    simulated an array. The worked example's "total cost 31 < 2n" and
    "amortised cost per insertion < 2" are facts about `n = 16`, a power
    of two; the proof above it says "under `3n`", and one insert later, at
    `n = 17`, the copies are 31 and the total 48 > 34 — the reader who
    generalises the worked example's 2 has been misled by an example that
    was correct.
12. **`greedy-algorithms` and `dynamic-programming` opened where their
    tables were off the page.** The greedy mode shows the last twelve
    amounts; at `n = 20` that is 9–20, so the row 6 the panel promised
    ("they part company at 6") was not in the table, only in a KPI. At
    `n = 24` (`dynamic-programming`) the rows are 13–24 and the worked
    example's table to 8 is nowhere.
13. **`complexity-classes`' panel promised "the gap at `n = 64`" and
    opened at `n = 24`.** The growth mode said nothing about time, though
    lesson 3's whole argument is in seconds and years.
    `decidability-and-the-halting-problem`'s panel is honest that no lab
    can show its theorem, and is left.

### Order, structure and the course home

14. **The course home's map and the module labels disagreed.**
    `syllabus_intro` and lesson 1's body say lessons 3–8 are analysis and
    9–10 design; the `module` fields on lessons 7 and 8 said "Design". The
    home's outcomes treat the master theorem as analysis and greedy/DP as
    "the two design techniques", so the labels were the odd ones out.
15. **`recursion-trees-and-amortised-analysis` carries two techniques.**
    Its act is amortised analysis (the worked example, the standard and
    two of three quiz questions); the recursion tree is course 3 lesson
    11's proof drawn, used for two examples the master theorem misses. Not
    split — the URL space stays and the recursion-tree half is a
    continuation of lesson 7 rather than a new hard idea — but noted.
16. **`big-o-notation`'s worked disproof uses limit language** ("`2ⁿ /
    n¹⁰⁰ → ∞`") on a path whose prerequisites promise growth is compared
    "by an explicit constant and threshold rather than by a limit". The
    words are "since exponential growth eventually dominates any fixed
    power", which is lesson 3's hierarchy; left, and noted.
17. **Three standards gave the reader nothing to check against**: the
    crossover of `50n log₂ n` and `n²` (`n = 439`), the witnesses for
    `5n³ + 2n² + n` (`C = 8`, `k = 1`), and the worked example's own
    crossover (996).
18. **The course home listed four outcomes** and omitted the acts of
    lessons 2, 6 and 8 — prove correct with an invariant, state the lower
    bound, bound a sequence.

### Distractors and feedback that does not answer

19. **`growth-of-functions` quiz 3 had a distractor that is also true.**
    "`3n² + 5n + 100` grows like: `n` / `n²` / `n³` / `3n²`" — `3n²` is
    literally what it grows like, and `Θ(3n²) = Θ(n²)` is the lesson's own
    point. A reader who chose it was marked wrong for being right.
20. **`greedy-algorithms` quiz 2's distractor is the body's own proof.**
    "The standard technique for proving a greedy algorithm optimal is:
    induction on the input size / an exchange argument / …" — the interval
    proof three paragraphs up begins "we show by induction that `gᵢ`
    finishes no later than `oᵢ`". The induction is bookkeeping and the
    exchange is the content, and the `why` said neither.
21. Of the 36 `why` fields, almost all restated the rule and answered no
    distractor: the reader who chose "finiteness" for a step left to
    judgement, "the algorithm terminates" for partial correctness, "`n²`"
    for the triangular nest, "combines faster" for Karatsuba, "every
    insertion costs `Θ(1)`" for amortised, "it is undecidable" for longest
    path, "not polynomial" for NP — none was told what their answer
    actually names.

## Where a learner gets stuck

- At `big-o-notation`'s lab, setting `n²` against `n` to try the body's
  disproof and being told it is true with `C = 100` (item 6).
- At `searching-and-sorting`'s worked example, looking for 62 in a lab
  that prints 77 (item 1).
- At `correctness-and-termination`, reading a lesson about invariants
  over a lab about sorting (item 7).
- At `divide-and-conquer`'s standard, trying to enter `9T(n/3) + n²` into
  a table with no inputs (item 10).
- At `greedy-algorithms`' lab, scanning amounts 9–20 for the failure at 6
  the panel promised (item 12).
- At `analysing-iterative-algorithms`' third mistake, with no way to sort
  a sorted array (item 8).
- At `growth-of-functions` quiz 3, choosing `3n²` (item 19).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered, so the five URL declarations are untouched. Every content edit
is in `content/discrete_math/c8_algorithms/` and the thirteen pages under
the slug (twelve lessons and the course home) are rebuilt from it. The lab
changes are in `scripts/mathpath/labs/algorithms.py`; because course 3
lessons 8, 11 and 12 render through the same lab, those three pages are
rebuilt too, and their panels' figures (32 and 6 at `n = 32` in search
mode; 190, 112 and 66 at `n = 20` in sort mode; `a = 2, b = 4, d = 1` as
the last row of the master table) were re-executed and still hold. Every
function the lab runs (the ten growth functions with their classes, the
witness search, the four counted sorts and searches, the loop nests, the
invariant trace, the dynamic array, the master theorem's cases, greedy and
DP coin change) is now an `ALGO_JS` block executed by an algorithms
section in `scripts/mathcheck.js` — 40 assertions, shown to fail when the
growth-class verdict was deliberately replaced by the old search and to
pass with it restored. Every figure a panel now states was obtained by
executing the shipped lab JavaScript at the shipped preset.

Lab (`algorithms.py`):

- **The witness mode is honest.** Each function carries its growth class
  (polynomial degree and log power, then exponential, then factorial);
  `f = O(g)` is decided by comparing classes, and the grid search for
  `(C, k)` runs only when the relation is true, then confirms the pair it
  found at `n = 10³, 10⁴, 10⁶, 10⁹`. When the relation is false the table
  shows the ratio `f(n)/g(n)` at `n = 10 … 10⁶` growing without bound —
  the disproof's shape — and the status says why no finite search could
  have decided it. `mathcheck` asserts that every true relation among the
  ten functions has a witness in the grid and that the six false ones the
  old search accepted are refused.
- New mode `invariant`: `POWER(x, n)` by repeated squaring in BigInt, with
  `result · base^m = xⁿ` evaluated exactly on every row, the squarings and
  multiplications counted against `n − 1`, and the wasted final squaring
  named (with the pointer to course 6 lesson 8's count of bits − 1).
- New mode `loops`: lesson 5's three nests and the standard's fourth, run
  with a counter for every `n` to the slider, beside `n³`, `n(n+1)/2`,
  `n ⌊log₂ n⌋` and `n(n+1)(n+2)/6`.
- New mode `amortised`: the dynamic array under three policies (double,
  ×1.5, +1), every resize listed with its copies, the total, the amortised
  cost, the worst single insertion, and the three policies' totals side by
  side; the status says when `n` is a power of two and what the next
  insert does.
- `master` takes the reader's own `a, b, d` as the top row of the table,
  reports the case with course 3's numbering and says which parameter to
  attack; the eight fixed rows keep their order, so course 3 lesson 11's
  "last row" is still `a = 2, b = 4, d = 1`. Results read `Θ(log n)` and
  `Θ(n log n)` rather than `Θ(n^0 log n)`.
- `sort` takes an input order (shuffled, sorted, reversed) and its status
  quotes insertion sort's count on all three at the current `n`.
- `growth` states `n²` and `2ⁿ` at the slider's `n` and the time the
  exponential curve takes at a billion operations a second.
- `greedy` lists every amount to the slider where greedy is wrong and
  shows the last sixteen rows rather than twelve.
- `search`'s worst case is computed by one function shared with the
  checker, which asserts it equals `⌊log₂ n⌋ + 1` for every `n` to 64.

Lessons:

- `algorithms-and-pseudocode`: the lab opens at `n = 64` and the panel
  reads 6 against `1.8 × 10¹⁹`, "more than eighteen orders of magnitude",
  and 585 years; every `why` answers each distractor, including the count
  of squarings and multiplications for `1000 = 1111101000₂`.
- `correctness-and-termination`: the lab is the `invariant` mode on the
  worked example's `POWER(3, 13)`, the panel reading four rows checked,
  `result = 1 594 323` at exit, four squarings and three multiplications
  against twelve, and sending the reader to `n = 64` for seven, one and
  63; every `why` answers each distractor.
- `growth-of-functions`: the time conversion is a fiftieth of a second
  against a quarter of an hour at a billion a second; the worked example
  reads `100·9.97 = 997 ≈ 1000`, the crossover, and "below 996"; the panel
  reads `1 024` against `4 294 967 296` and 4.3 seconds at `n = 32`; quiz
  3's `3n²` is now `n log n`; the standard gives 439 to check against;
  every `why` answers each distractor.
- `big-o-notation`: the panel reads `C = 4`, `k = 13` against the body's
  `C = 108`, `k = 1`, sends the reader to `n²` against `n` for the ratio
  column, and says why the verdict is not a search's; the standard gives
  `C = 8`, `k = 1`; every `why` answers each distractor, including why a
  big-O claim is not "only for large `n`".
- `analysing-iterative-algorithms`: the lab is the `loops` mode at
  `n = 16`, the panel reading 4 096, 136, 64 and 816 and sending the
  reader to the sort mode at `n = 16` for 15, 120 and 77; every `why`
  answers each distractor.
- `searching-and-sorting`: the worked example reads insertion 77 and, at
  `n = 1000` on the lab's array, 499 500 / 235 149 / 7 387; the lower
  bound is proved from `n! ≥ (n/2)^{n/2}` with Stirling as a remark, and
  the height bound is derived from course 7's vertex count; the lab opens
  at `n = 16`, the panel reading 120, 77, 48 and sending the reader to the
  input order and to the search mode for 16 against 5; every `why`
  answers each distractor.
- `divide-and-conquer`: module Analysis; the lab opens on `4T(n/2) + n`,
  the panel reading case 3, `Θ(n²)`, then `d = 0` (unchanged), `a = 3`
  (`Θ(n^1.585)`) and the standard's `9T(n/3) + n²` (case 2); every `why`
  answers each distractor.
- `recursion-trees-and-amortised-analysis`: module Analysis; the lab is
  the `amortised` mode on sixteen inserts, the panel reading the resizes
  at 2, 3, 5, 9, 15 copies, total 31, 1.94, worst 9, then 17 inserts for
  31, 48 and 2.82 "above 2 and still below 3", then growing by one for
  120; the worked example's `after` says why its "< 2n" is a fact about a
  power of two; every `why` answers each distractor.
- `greedy-algorithms`: the lab opens at `n = 12` so the row at 6 is on
  the page, the panel reading 6 and 10 and that `{1, 5, 10, 25}` never
  differs; quiz 2's `why` places the body's induction; every `why`
  answers each distractor.
- `dynamic-programming`: the lab opens at `n = 8`, the panel reading the
  worked example's optimal column 1, 2, 1, 1, 2, 2, 2, 2 and the routes at
  7 and 8; every `why` answers each distractor.
- `complexity-classes`: the lab opens at `n = 64`, the panel reading
  4 096 against `1.8 × 10¹⁹` and 585 years; every `why` answers each
  distractor, including what a faster machine buys.
- `decidability-and-the-halting-problem`: every `why` answers each
  distractor; the lab and panel are unchanged.
- Course home (`__init__.py`): a fifth outcome names the acts of lessons
  2, 6 and 8; `how_to` says the witness mode refuses false relations from
  the growth classes and which lesson's example each lab opens on.
