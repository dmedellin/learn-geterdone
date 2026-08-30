# Pedagogy assessment — Combinatorics and Counting (discrete mathematics, course 4)

First assessment, formed from the fourteen lesson dicts in
`content/discrete_math/c4_counting/` (`part_a.py`, `part_b.py`, `__init__.py`)
and the lab kit they render through, `scripts/mathpath/labs/counting.py`
(the four-rule counting lab, the Pascal lab and the inclusion–exclusion lab),
as they stand on `main` at b6daf82. No prior assessment exists for this
course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `sum-and-product-rules`, `counting-with-restrictions`,
`permutations`, `combinations`, `binomial-coefficients`,
`the-binomial-theorem`, `permutations-with-repetition`,
`combinations-with-repetition`, `inclusion-exclusion`, `derangements`,
`generalized-pigeonhole`, `generating-functions`, `combinatorial-proof`,
`choosing-a-counting-method`. The course declares courses 1–3 as
prerequisites ("sets, functions and induction"), so it is judged against
what those teach: `|A × B| = |A|·|B|` and `|P(A)| = 2ⁿ` (course 2 lessons 5
and 2), bijections and their two obligations (course 2 lesson 11), the
pigeonhole principle in its plain form (course 2 lesson 14), proof by cases
(course 1 lesson 14), and the recurrence case split of course 3 lesson 9.
Every figure quoted below was recomputed in exact arithmetic, and every
lab figure by executing the shipped JavaScript at the shipped preset.

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** State the
  rule and its condition before computing (`sum-and-product-rules`); check a
  restricted count two ways (`counting-with-restrictions`); justify the
  divisor in a symmetry argument (`permutations`); prove an identity by
  counting one set twice (`binomial-coefficients`); extract a coefficient
  with constants and signs present (`the-binomial-theorem`); handle an
  adjacency constraint by gaps (`permutations-with-repetition`); translate
  between balls-in-boxes, an equation and a stars-and-bars row
  (`combinations-with-repetition`); set up the sets so the intersections are
  easy (`inclusion-exclusion`); count "exactly `k` fixed points" unaided
  (`derangements`); invent a classification for a new problem
  (`generalized-pigeonhole`); write the generating function for a
  constrained selection (`generating-functions`); prefer the counting proof
  (`combinatorial-proof`); classify before computing
  (`choosing-a-counting-method`). None is "understand X".
- **The course is built around one diagnosis and repeats it until it
  sticks:** almost every wrong answer is a right calculation of the wrong
  quantity. `sum-and-product-rules`' `concepts_intro`, `combinations`' step
  1, `combinations-with-repetition`'s four-rule table with the four answers
  `60, 10, 125, 35` at `n = 5`, `r = 3`, and the whole of
  `choosing-a-counting-method` say so in different words, and the counting
  lab shows all four totals on every page that carries it so the reader
  cannot compute one without seeing the other three.
- **The labs compute rather than assert, and they check themselves.** The
  counting lab enumerates every selection while the total is at most 400
  and compares the list's length with the formula; the Pascal lab sums the
  cells it highlights and compares the sum with the cell the identity
  claims; the inclusion–exclusion lab walks `1 … N` one integer at a time
  beside the alternating sum and reports both. All of it is in `BigInt`, so
  `24!/12! = 1 295 295 050 649 600` is the number and not an approximation
  of it, as the course home's `footer_lead` promises.
- **The proofs are right and they are the explanatory ones.** `P(n, r)` by
  the product rule with the factor count made explicit; `C(n, r)` by a
  double count of ordered selections, named as a double count one lesson
  before `combinatorial-proof`; symmetry by complementation, with the
  bijection argued in both directions; Pascal's rule by a fixed element;
  the alternating row sum by add-or-remove, with the `n = 0` exception
  stated; the hockey stick by largest element; Vandermonde by two groups;
  the binomial theorem as "expanding is choosing"; stars and bars as a
  bijection with the bar count justified; inclusion–exclusion by the
  per-element contribution collapsing through the alternating sum;
  derangements twice, by inclusion–exclusion and by the case split on where
  element 1 goes; Erdős–Szekeres with the boxes named as the whole
  difficulty; `R(3,3) = 6` with both halves and the five-cycle
  construction; the `n = 0` value `D₀ = 1` as what makes
  `Σ_k C(n,k)·D_{n−k} = n!` close.
- **The misconceptions named are the real ones, at the point of error.**
  Adding when cases overlap and multiplying when the second count varies
  (`sum-and-product-rules`); the second digit having 9 options, not 8, once
  0 is freed (`counting-with-restrictions`); ending the factor list at
  `n − r` (`permutations`); `n` bars instead of `n − 1`
  (`combinations-with-repetition`); a sign lost on an odd power
  (`the-binomial-theorem`); `m − 1` gaps instead of `m + 1`
  (`permutations-with-repetition`); `D₀ = 1` forgotten (`derangements`);
  rounding `⌈n/k⌉` down and proving only the pigeonhole half of a Ramsey
  equality (`generalized-pigeonhole`); worrying about convergence
  (`generating-functions`); asserting a bijection without defining it
  (`combinatorial-proof`).
- **The arithmetic a reader would trust is right, with three exceptions
  recorded below.** `3380 + 676 − 130 = 3926`; the three password lengths
  and their total `2 684 483 063 360`; `9 · 9 · 8 · 7 = 4536`; `69 760`;
  `(7−1)!·2 = 1440`, `5040 − 1440 = 3600`, `1440/5040 = 2/7`; `C(52,5) =
  2 598 960` and `48/2 598 960 ≈ 1.85 × 10⁻⁵`; `840 + 420 + 56 = 1316 <
  2002`; `56 · 32 · (−27) = −48 384`; `28 · 64 = 1792`; `11!/(4!·4!·2!) =
  34 650`; `52!/(13!)⁴ ≈ 5.36 × 10²⁸`; BANANA's `60`, `3 · 4 = 12`, `48`;
  `C(7,5) = 21`, `C(8,6) = 28`, `C(14,12) = 91`; `1000 − 1033 + 332 − 33 =
  266`; surjections `243 − 93 = 150`; `D₁ … D₈`; `15 · 9 = 135` and the
  seven-term check summing to `720`; `⌈50/7⌉ = 8`; `R(4,4) = 18` and
  `43 ≤ R(5,5) ≤ 46`; the twelve ways to make 25 cents; `P(26,5) −
  P(21,5) = 5 451 720` and the six-string small case.
- **Prerequisite order across the path is sound in both directions.**
  Inbound: course 2 sends the reader to lesson 1 for the two rules, lesson
  5 for the row sum, lesson 9 for inclusion–exclusion and lesson 11 for
  the generalised pigeonhole; course 3 to lesson 12 for generating
  functions; course 5 to lessons 2, 5, 6, 9 and 10; course 6 to lessons 1
  and 9; course 7 to lessons 4 and 13; course 8 to the permutation count.
  Every one lands on a lesson that teaches what is cited. Outbound, every
  pointer resolves: course 2 lessons 2, 5, 11, 12, 14; course 1 lesson 14;
  course 3 lessons 9 and 10; course 7 lesson 2; course 8 lesson 11.

## What it teaches badly, or claims and does not deliver

### Order: a formula used two lessons before it is taught

1. **`counting-with-restrictions`' worked example is built from `C(11,4) =
   330`, `C(6,4) = 15`, `C(5,4) = 5` and six more binomial coefficients,
   and its standard asks for "cases on the number of `a`s", which needs
   `C(5,k)`.** Combinations are defined in lesson 4. The lesson's own body
   is careful — every example in it is a product-rule count — and then the
   example the reader is meant to imitate uses a formula the course has
   not stated, with no pointer. A reader who has followed the course in
   order cannot do the standard.

### Facts a reader would trust that are wrong

2. **`generating-functions` says `[x¹⁰](1 + x + x² + x³)⁴` is 4.** It is
   10: a selection of 10 from four types with at most 3 each is short of
   the maximum 12 by 2, and the shortfalls are a stars-and-bars count,
   `C(5, 2) = 10`. Executed: the coefficient is 10. The example is the one
   place the lesson shows a constraint being encoded by a polynomial
   factor, and the number under it is wrong.
3. **`derangements`' table gives `D₈/8!` as `.3678792`; that is `D₉/9!`.**
   `14833/40320 = 0.3678819`. Two lines below, the hat-check example says
   the proportion "for `n ≥ 5` is 0.3679 to four places whatever `n` is";
   at `n = 5` it is 0.3667 and at `n = 6` it is 0.3681. The lesson's own
   concept 3 says "by `n = 7`", which is right, and its mistake 3 says "8
   people", which is right; the example contradicts both.
4. `permutations` says `52!` "exceeds the number of atoms in the Milky
   Way". The stars alone hold about `10⁶⁸`, so the claim is at best a
   coin-flip; the Earth's `10⁵⁰` is the comparison that is true by
   seventeen orders of magnitude. `binomial-coefficients`' note attributes
   the "binary digits of `k` are a subset of those of `n`" criterion to
   Kummer; that statement is Lucas's theorem read modulo 2 (Kummer's counts
   carries, and gives the criterion only as a corollary).
5. `inclusion-exclusion`'s divisibility example computes every intersection
   as `⌊1000/ab⌋`, which is right only because 2, 3 and 5 are pairwise
   coprime, and never says so. The lab on the page computes them as
   `⌊N/lcm(a,b)⌋` — set `b = 4` and the two methods disagree — and nothing
   on the page explains why. The predictable error (`⌊100/24⌋` for
   "divisible by 4 and 6") is not named anywhere in the course.

### Labs that do not agree with their own lessons

6. **`derangements` renders the inclusion–exclusion lab, which counts
   multiples of `a`, `b`, `c` in `1 … N`.** Nothing on the lab is a
   derangement; the panel says only that derangements are "this alternating
   structure applied to fixed points" and tells the reader to watch a
   running total that is about divisibility. The lesson's own content — the
   alternating sum, the recurrence, the `1/e` limit, the nine derangements
   of four — is exactly what a lab could compute and compare, and none of
   it is computed anywhere on the page.
7. **`generating-functions`' lab is set to `n = 4`, `r = 10`, where the
   count `C(13,10) = 286` is under the 400 the lab lists but `r = 10` is
   over the lab's `r ≤ 8` guard, so the page reads "Too many to list (286
   selections)"** under a lesson whose home says the lab "lists the actual
   selections up to 400 of them". The panel promises nothing the lab then
   does.
8. `permutations`' panel says "raise `n` past 20 and the enumeration
   stops". At the shipped `r = 3` it stops at `n = 9` (`P(9,3) = 504`); the
   `n ≤ 20` guard is reached only at `r ≤ 1`. A reader who tries the
   instruction sees the list vanish eleven steps early.
9. `generalized-pigeonhole` renders the counting lab at `n = 12`, `r = 3`
   with a panel that concedes the lab is not about the lesson ("pigeonhole
   arguments are about ratios rather than enumerations"). The lesson's own
   theorem is about the 15 pairs and 20 triples among six people, which the
   same lab lists at `n = 6`.
10. The panels on `sum-and-product-rules`, `combinations`,
    `binomial-coefficients`, `the-binomial-theorem`,
    `permutations-with-repetition`, `combinations-with-repetition`,
    `inclusion-exclusion` and `combinatorial-proof` describe the lab
    correctly and quote none of its figures, so the reader is not told what
    to look for. Executed at the shipped presets: 125 strings in five
    alphabetical blocks of 25 (the sum rule inside the product rule); `120/20
    = 6 = 3!`; `5 + 10 = 15`; row 5 summing to 32 with coefficients `1, 5,
    10, 10, 5, 1` printed; the 64 strings splitting as `4 + 36 + 24` with
    `aab, aba, baa` the `3!/2!` arrangements of one multiset; `** | | ***`
    as the chip `aaccc`; `74` both ways at `N = 100`, naive `103`, `26`
    divisible by none; `1 + 3 + 6 + 10 + 15 = 35`.

### Practice that repeats, or does not practise, the lesson

11. **`binomial-coefficients`' standard is `combinatorial-proof`'s worked
    example** (`C(n,k)·C(k,j) = C(n,j)·C(n−j,k−j)`, both by "choose the
    inner set before or after the outer"), and **`combinatorial-proof`'s
    standard is a special case of an example on its own page** (`Σ C(n,k)²
    = C(2n,n)` is Vandermonde at `m = n = r`, and Vandermonde is the third
    example in the body). Between them, the two lessons ask the reader to
    do one thing that is worked eight lessons later and one thing that is
    on the page.
12. `combinations`' standard ("take five problems from anywhere in this
    lesson and classify each") is `choosing-a-counting-method`'s standard
    ("take any five counting problems, write the classification for each")
    ten lessons early, and neither names a problem. The capstone's standard
    is the right act for the course but gives the reader nothing to
    retrieve.
13. `combinatorial-proof` teaches two techniques, and its worked example,
    standard and three quiz questions exercise only the first. The
    bijection method gets three examples and no practice, though step 4
    ("define the map both ways") is the obligation the lesson says people
    skip.

### Distractors that are also true

14. **`combinations`, question 2: "Why is `C(n, r) = C(n, n−r)`? — The
    formula is symmetric."** That is a valid reason; the lesson's own body
    calls it "the algebraic one" and says it is a proof that merely
    explains less. It is marked wrong.
15. **`binomial-coefficients`, question 1: "Pascal's rule is proved by: —
    algebra with factorials."** It is; the `why` says so ("the algebraic
    verification works"). Marked wrong.
16. `binomial-coefficients`, question 3's `why` says "odd rows are symmetric
    too and their alternating sum is 0 for the same bijective reason". For
    odd `n` symmetry alone does give it — `C(n,k)` and `C(n,n−k)` have
    opposite parity and cancel — and it is the even rows where symmetry
    fails and the bijection is needed. The explanation has the cases
    backwards.

### Quiz feedback that does not answer the wrong answer

17. Of the 42 `why` fields, only `sum-and-product-rules` Q1 and
    `permutations` Q1 address a second distractor by name. The rest restate
    the rule or identify one wrong answer. The reader who chose `300` for
    "at least one 5" (three cases added, `155` counted twice) is not told
    that; nor the reader who chose `5040` for four-digit distinct numbers
    (a leading 0 allowed), `64` for strings of length 4 over three letters
    (base and exponent swapped — the standard slip), `10!/(2!·3!)` for
    BOOKKEEPER (one repeated pair lost), `C(12,10)` for positive solutions
    (the non-negative count), `41` or `26` for `|A ∪ B|` (the overlap added,
    or subtracted twice — and `26` is neither), `0` for the limit of
    `Dₙ/n!` (the everyday guess, which is wrong for a reason worth
    saying), `9` for `⌈50/7⌉` (false, and refutable by `8, 7, 7, 7, 7, 7,
    7`), `x²` for "at most two", or `4¹⁰` for identical balls
    (distinguishable balls).

### Cognitive load and structure

18. `sum-and-product-rules` carries the two rules, their conditions, the
    overlap example (inclusion–exclusion "arriving early"), the "second
    count varies" discussion and complementary counting; `counting-with-
    restrictions` then teaches complementary counting again as one of
    three repairs. I have chosen not to split or move it: lesson 1's quiz
    and standard use the complement, lesson 2's treatment is the general
    one with the "at least" signal, and the repetition is spaced practice
    of the course's most-used move rather than overload.
19. `binomial-coefficients` proves five identities and works a sixth, which
    is most of `combinatorial-proof`'s double-counting half eight lessons
    early. The single idea is one classification (fixed element, largest
    element, two groups) and the lab shows each on one control; lesson 13
    then adds bijections and "when to use which". Not split; the course
    home's `how_to` says to do the proofs twice on purpose. What was wrong
    was that the two lessons' practice overlapped (item 11), which is
    repaired.
20. `permutations` never says what happens when the chairs are numbered.
    The circular count `(n−1)!` is derived from "rotations are considered
    identical", and the predictable error — dividing by `n` when the seats
    are distinguishable — is not named in body, mistakes or quiz.
21. The course home lists four outcomes and omits the acts lessons 11 and
    12 close on — invent the classification, write the factor — though
    `syllabus_intro` calls 12–14 "the techniques that generalise" the rest.

## Where a learner gets stuck

- At `counting-with-restrictions`' worked example and standard, needing a
  formula from lesson 4 (item 1).
- At `generating-functions`' restricted-selection example, expanding
  `(1 + x + x² + x³)⁴` and getting 10 against the page's 4 (item 2); and at
  its lab, being told 286 selections are too many to list (item 7).
- At `derangements`' lab, looking for a derangement and finding multiples
  of 2, 3 and 5 (item 6); and at the hat-check example, checking the
  four-place claim at `n = 5` against the table two lines above (item 3).
- At `combinations` question 2 and `binomial-coefficients` question 1,
  having answered with a proof the lesson itself calls valid (items 14,
  15).
- At `binomial-coefficients`' standard, and again at `combinatorial-proof`'s
  worked example, meeting the same identity (item 11).
- At `inclusion-exclusion`'s lab with `b = 4`, seeing `⌊N/4⌋` where the
  lesson's method gives `⌊N/8⌋` (item 5).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered, so the five URL declarations are untouched. Every content edit is
in `content/discrete_math/c4_counting/` and the pages are rebuilt from it.
One addition is in lab core, `scripts/mathpath/labs/counting.py`: a
`derangement` lab, registered in `scripts/mathpath/labs/__init__.py` and
used by one page. Its arithmetic (`BIGINT_JS` and the new `DERANGE_JS`) is
now exercised by a counting section in `scripts/mathcheck.js`, which also
checks `comb`, `perm` and `fact` for the first time; the section was shown
to fail when the sign in the alternating sum was removed, and passes with
it. Every figure a panel now states was obtained by executing the shipped
lab JavaScript at the shipped preset.

- `sum-and-product-rules`: the panel reads the 125 listed strings as five
  alphabetical blocks of 25 — the sum rule inside the product rule; every
  quiz `why` answers each distractor, including `300` as three overlapping
  cases.
- `counting-with-restrictions`: worked example replaced by one that uses
  only this lesson's tools — strings of length 4 over `{a, b, c}` with at
  least two `a`s, by cases (the six position pairs listed by hand, `24 + 8
  + 1 = 33`) and by complement (`81 − 16 − 32 = 33`), with the `after`
  saying lesson 4 will name the six pairs `C(4, 2)`; the standard is now
  the 4-digit numbers containing at least one 7, by complement and by cases
  on the position of the first 7 (`3168` both ways); the body paragraph
  points at the worked example; every `why` answers each distractor.
- `permutations`: a paragraph on numbered chairs (`n!`, nothing is
  identified) after the circular proof; `52!` compared with the Earth's
  `10⁵⁰`; the worked example's check sentence rewritten so it says what it
  means; the panel says the list stops at `n = 9` and gives `24!/12!`;
  every `why` answers each distractor.
- `combinations`: question 2 now asks which option is a *bijective* proof,
  with the algebraic proof as a distractor the `why` calls valid but not
  bijective; the standard is hands with at least two aces by cases and by
  complement (`108 336` both ways), with the independence and disjointness
  to be stated; the panel gives `120/20 = 6`; every `why` answers each
  distractor.
- `binomial-coefficients`: question 1 asks what the counting proof
  classifies by, with "largest element" (the hockey-stick proof) as the
  distractor; question 3's `why` has the odd and even cases the right way
  round; the standard is `C(2n, 2) = 2·C(n, 2) + n²` by two halves, checked
  at `n = 3`; the note says Lucas; the panel gives `5 + 10 = 15`; question
  2's `why` names `6²`, `2·6` and `6!`.
- `the-binomial-theorem`: the panel gives row 5's coefficients and `32`,
  and sends the reader to the alternating sum; every `why` answers each
  distractor, including `C(7,4) = C(7,3)` so the third option's error is
  the power.
- `permutations-with-repetition`: the panel finds the multiset formula in
  the list (`aab, aba, baa`; `4 + 36 + 24 = 64`); question 1's `why` names
  `4³` as base and exponent swapped; the other `why`s answer each
  distractor.
- `combinations-with-repetition`: the panel gives `C(7, 5) = 21` and reads
  `** | | ***` as the chip `aaccc`; every `why` answers each distractor,
  with `C(12,10) = 66` identified as the non-negative count.
- `inclusion-exclusion`: a paragraph after the divisibility example says
  the intersection is `⌊N/lcm(a,b)⌋`, with `⌊100/12⌋ = 8` against
  `⌊100/24⌋ = 4`, and that the lab does it that way; the panel gives `74`,
  `103`, `26` and says to set `b = 4`; question 1's fourth option is `23`
  (the overlap subtracted twice) and the `why` answers all three.
- `derangements`: the `D₈/8!` entry corrected to `.3678819`; the hat-check
  example says `n ≥ 7`, with the values at 5 and 6; the lab is the new
  derangement lab at `n = 6` — the alternating sum term by term with its
  running total `720, 0, 360, 240, 270, 264, 265`, the recurrence, the
  listed derangements for `n ≤ 8` (printed for `n ≤ 5`), `Dₙ/n!` to seven
  places beside `1/e`, and the nearest integer to `n!/e` — and the panel
  says what to look at; every `why` answers each distractor, including why
  the limit is not 0.
- `generalized-pigeonhole`: the lab preset is `n = 6`, `r = 3` and the
  panel reads the 20 triples and 15 pairs as the objects of the `R(3,3)`
  proof, with `n = 5` as the five-cycle's case; the worked title says
  "block"; every `why` answers each distractor, with `9` refuted by an
  explicit distribution.
- `generating-functions`: the restricted-selection count is 10, with the
  shortfall argument as a check; the lab preset is `n = 4`, `r = 6` so the
  84 multisets are listed, and the panel asks the reader to count the 40
  that a factor `1 + x + x² + x³` excludes, leaving `44 = [x⁶](1 + x + x² +
  x³)⁴`; every `why` answers each distractor.
- `combinatorial-proof`: `Σ C(n,k)² = C(2n,n)` moved into the body as
  Vandermonde at `m = n = r` with the symmetry step shown; the standard is
  now one double count (`Σ 2ᵏ C(n,k) = 3ⁿ`, which lesson 6 obtained by
  substitution) and one bijection (`k`-subsets with no two consecutive
  integers, `C(n − k + 1, k)`, with the map, its inverse and a check at `n
  = 5`, `k = 2`); the panel gives `1 + 3 + 6 + 10 + 15 = 35`; every `why`
  answers each distractor.
- `choosing-a-counting-method`: the standard names five problems from the
  course (PINs, podium, hands, doughnuts, BANANA) that land on four
  different rules and one multiset, and asks for the doughnuts to be
  listed; every `why` answers each distractor.
- Course home (`__init__.py`): a fifth outcome names the acts of lessons 11
  and 12; `outcomes_intro` includes it.
