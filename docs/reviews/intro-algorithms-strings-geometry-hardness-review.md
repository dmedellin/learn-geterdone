# Review: Introduction to Algorithms, Course 8 — Strings, Geometry and Hardness

Independent accuracy and pedagogy review of
`content/intro_algorithms/c8_strings_geometry_hardness/` (8 lessons, CLRS 3rd ed.
Chapters 32–35) against the book's sections, the rendered labs and
`docs/intro-algorithms/AUTHORING.md` / `PLAN.md`.

## Method

- Every attributed claim checked against the sections with `book.py` / `page.py`
  (theorem and lemma numbers 34.1–34.15, 35.1–35.8, Corollary 35.5; Exercise
  34.4-6; the O(m·|Σ|) remark in 32.3; the sweep's assumptions and total
  preorder; Jarvis's chains; the convex-hull assumptions; the closest-pair
  eight-point argument).
- Every number in prose, worked examples and quiz answers recomputed by hand or
  with a scratch script (Rabin-Karp residues and the modulus sweep, π tables and
  fallbacks, all four segment determinants, the Graham traces, self-reduction
  models, subset-sum digit tables, vertex covers, set-cover charges and harmonic
  numbers, the trimming run).
- Every preset figure read with `labcheck.js --observe`; every typed instance the
  prose cites (lesson and exercise instances in all eight labs) entered in the
  rendered page with Playwright and its tiles read.
- `quotes.py`: all eight quotations OK (23, 26, 21, 18, 31, 34, 10, 13 words; one
  per lesson). `overlap.py 8`: only the counted quotations, "Graham's scan runs in
  O(n lg n)", "a loop invariant at the start of each iteration", "a
  polynomial-time algorithm for an NP-complete problem", and digit/edge-list
  coincidences.

## Findings and changes

Errors (fixed):

1. **Convex hull, worked example.** The turn at (4, 3) when (6, 6) arrives was
   given as −3; it is −11. Fixed.
2. **Convex hull, the book's assumption misstated.** One mistake said the book
   assumes "no three colinear on the hull"; the book assumes distinct points with
   at least three not colinear. The preset paragraph said that assumption
   excludes the last four presets; it excludes `segment`, `duplicate` and
   `single`, but `needle` (a valid triangle that fails only in floating point) and
   `edges` satisfy it. Both rewritten, with how GRAHAM-SCAN treats points in the
   middle of a side (the farthest-only rule of its sort, and popping on a colinear
   turn).
3. **Jarvis's march** was described as taking the smallest angle "relative to the
   last edge"; the book measures polar angle about the last vertex from the
   positive x-axis (right chain) and the negative x-axis (left chain). Fixed.
4. **Monotone chain vs GRAHAM-SCAN.** The lab paragraph said the kit "differs
   from GRAHAM-SCAN in one respect" and the panel called it "a Graham's scan". It
   has no p0 and no angular sort and builds two chains. Now stated plainly: the
   lab does not run GRAHAM-SCAN; hull same, pushes and pops differ; trace
   GRAHAM-SCAN by hand.
5. **Hull quiz on n·h vs n·lg n** turned on a tie (h = lg n) with a distractor
   that differed only by "is below" vs "equals". Replaced by h = 4 (256 against
   384), with distractors for overgeneralising, n² mistaken for n·lg n, and h
   confused with lg n; the explanation notes hidden constants.
6. **Closest-pair quiz answer** said eight points "with pairwise distance at least
   δ" fit in the rectangle; the book's argument is four per half, points on one
   side being δ apart (cross pairs may be closer). Reworded.
7. **Subset-sum exercise formula** `1 2 3; -1 -2 -3` was two clauses of the
   book's own worked instance in 34.5.5. Replaced by `1 2 -3; -1 2 3` with the
   assignment x1 true, x2 false, x3 true (uses all four slack numbers, and x2
   false is a number with no clause digit); quiz 1 rewritten and checked in the
   lab (11144, 6 subsets, 6 of 8 models).
8. **KMP lesson relied on the `ababaca` preset** by inviting the reader to follow
   the book's figures with it. Sentence removed; the lesson uses only its own
   patterns (the preset remains in the kit's menu, unadvertised).
9. **"Positive is a left turn"** was set in quotation marks, so it read as a book
   quotation (quotes.py MISS). Now italic.
10. **"Sorting is in NP"** (NP is a class of languages): replaced by a decision
    problem in P.

Minor (fixed): the KMP quotation is in the last paragraph of 32.1, not its
closing sentence; the lab's π inner-loop tile for `aaaab` is 3 (construction)
while the mistake counts the matcher's 4 falls on `aaaac`, now said; the P/NP
quiz explanation no longer says the section draws the relations "without
choosing one" (the body says which the authors expect).

Checked and correct: every other number in the course, including all Rabin-Karp
figures (34 characters, valid shifts 3, 5, 19, 31; 1 spurious hit at 11, 8 at 13,
17 of 46 primes, largest 181), the π tables, the segment determinants and lab
signs, both Graham traces' vertex sets and pop counts, the self-reduction runs,
all vertex-cover and set-cover figures, H values, and the trimming run (answer
63, optimum 65, 8 sums kept against 11).

## Left open

- The `strings/kmp` kit's default menu still contains `ababaca`, the book's
  example pattern; changing the kit is outside this course's files.
- The hull kit runs the monotone chain, not GRAHAM-SCAN; the lesson now says so,
  and the Graham trace is by hand.
- The set-cover kit bounds by H(|X|), not the book's H(max |S|); the lesson
  computes both.
