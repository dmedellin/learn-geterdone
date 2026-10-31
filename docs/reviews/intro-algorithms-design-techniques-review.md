# Review: Introduction to Algorithms, Course 4, Advanced Design and Analysis Techniques

Independent accuracy and pedagogy review of `content/intro_algorithms/c4_design_techniques/`
(nine lessons, CLRS Chapters 15 to 17) against the book, the rendered labs and
docs/intro-algorithms/PLAN.md. Fixes were made in the course files only; the
course's block of `content/spoken/intro_algorithms.py` needed no change.

## Method

- Every claim credited to the book was checked against its section with `book.py`
  and `page.py`. That covered rod cutting's 2^(n−1) cuttings, T(n) = 2^n and the
  n = 40 remark, the subproblem graph (reverse topological order, memoization as
  depth-first search), equations 15.6, 15.7, 15.9, 16.2 and 17.6, the Catalan and
  Ω(2^n) counts, O(n³) with Exercise 15.2-5, the four steps, subproblems times
  choices, the longest-simple-path argument (the lesson's graph is its own, not
  Figure 15.6), RECURSIVE-MATRIX-CHAIN's T(n) ≥ 2^(n−1), Theorem 15.1, OPTIMAL-BST's
  e, w and root, Theorem 16.1, the six and three steps, Lemmas 16.2 and 16.3,
  Theorems 16.5, 16.6 and 16.11 with Lemma 16.7, Corollary 16.9 and Lemma 16.10,
  Lemma 16.12 and Theorem 16.13, the chapter notes (Huffman 1952, Whitney 1935,
  Edmonds 1971), the starred status of 16.4 and 16.5, the three amortized methods,
  the half-full thrash sequence and the quarter rule's case analysis. Every
  exercise and problem number cited (15.1-1, 15.2-3, 15.3-4, 15.5-1, 15.5-4, 16.1-2,
  16.3-2, 16.3-4, 16.3-8, 16.4-1, 17.4-2, 12-4, 16-4) was also checked.
- Every number was recomputed by hand. That covered the rod tables (8, 9 and
  10 inches, call counts), both chain tables (all five bracketings of the
  four-matrix chain, every cell of the five-matrix one), the coin recursion
  C(0) to C(20) = 3,053 and the memo count 53, the TABLE/BLEAT c and b tables
  and arrow counts, both LCSs of the anagram pair and the tie path, every OBST
  cell (four-key and three-key) and the exercise tree (97/40), the activity
  schedule under three rules, the knapsack, the Huffman merges and B(T) = 144,
  the task schedule and its exercise variant, the 49 forests, both table
  sequences under both rules (35 and the half rule's 72), and the first five
  insertions' potentials.
- Every typed instance the prose cites was run on the built page in Chromium
  (Playwright): chain 6 2 10 4 8 3 in both orders (228, 1,064, row-major 36), coins
  1 4 6 at 8, 20 and 24, the ten activities under earliest finish and earliest
  start (with the exchange table), the Huffman alphabet with `faced`, and the
  two-triangle graphic matroid (49, rank 4, 867 pairs, greedy 28). The kit presets
  the prose describes (`square`, `canonical`, `startfails`, `shortestfails`,
  `conflictfails`, `skewed`, `uniform`, `matchings`) were loaded too. No lesson
  points the reader at chain `clrs`/`thin`, huffman `clrs` or intervals `eleven`.
- `quotes.py`: all nine quotations OK (11 to 30 words, one a lesson), checked
  character by character against the text.
- `overlap.py 8`: only the nine counted quotations and standard runs ("a p × q
  matrix by a q × r matrix", "c[i, j − 1] and c[i − 1, j]", "a longest common
  subsequence of X and Y") and runs of table digits.

## Errors found and fixed

1. **Lesson 3, memo count.** The lesson said 21 distinct amounts, 0 to 20, were
   "ever stored". The lab's memo holds 20 (the amounts 1 to 20; 0 is the base
   case). The body, the worked example's last line, quiz 4's explanation,
   mistake 3 and step 5 now agree with the lab. "Adds a few calls" at amount 24
   now gives the figures: 14,085 plain calls, and 65 memoized (twelve more).
2. **Lesson 9, quiz 3 explanation.** The −5 distractor was explained as
   "subtracts the actual cost". That gives −15, not −5. It is `1 + 2 − 8`: it keeps
   the drop in Φ and forgets the 8 items moved.
3. **Lesson 9, the half-rule thrash.** The sum behind the hand-computed 72 was
   left implicit, and "every round costs 19" overlooked the final partial round.
   The text now shows the whole sum: the nine opening insertions cost 24, then
   two rounds of 19, then the closing delete, delete, insert at 10 (3 under the
   quarter rule), so 24 + 19 + 19 + 10 = 72.
4. **Lesson 9, forward pointer.** Disjoint sets were said to be "priced by an
   aggregate count". Chapter 21 also uses a potential in starred 21.4, and the
   text now says so.
5. **Lesson 6, exercise.** It asked for the proof that Exercise 16.1-2 asks for,
   which restated the exercise. It now asks the reader to run the rule on the
   lesson's activities and leaves the proof to the book.

Everything else checked correct: book claims, hand figures, pinned and typed lab
figures, and quiz keys and distractors.

## Kit observations (not edited)

- **greedy/intervals.** After the reader types their own intervals, the status
  banner still ends with the selected preset's note. With the lesson's
  activities typed over `startfails`, it says the first interval "occupies the
  whole day", which is false for that instance. matroid does the same, harmlessly.
- **greedy/huffman.** The merge table leaves internal nodes' names blank ("b and",
  "and d", "and"), so merges 2, 4 and 5 read as incomplete.

## Final state

`python3 scripts/preview_subject.py intro_algorithms --course
intro-algorithms-design-techniques --out <dir>` prints OK: 9 pages executed,
9 with pinned figures, 0 failing.
