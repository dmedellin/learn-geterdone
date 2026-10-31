# Review: Introduction to Algorithms, Course 5, Advanced Data Structures

Course `intro-algorithms-advanced-structures` (`content/intro_algorithms/c5_advanced_structures/`),
five lessons on CLRS 3rd ed. Chapters 18–21. Independent review against the book's sections,
then fixes made in the course files. Date: 2026-10-31.

## Method

- Every attributed claim checked against the sections with `book.py` / `page.py`: Theorem 18.1,
  the disk conventions, B-TREE-INSERT's read and write calls, the deletion cases; Φ = t(H) + 2m(H),
  D(n) ≤ ⌊lg n⌋ (Problem 19-2(d)), CONSOLIDATE's bound and invariant, the 4 − c argument,
  Lemmas 19.1–19.4 and Corollary 19.5; the Section 8.1 lower bound, proto-vEB recurrences,
  Exercises 20.2-2/20.2-3, the O(u) space claim (Problem 20-1), the "negative progress" remark;
  Theorem 21.1, the O(m lg n) / path-compression bounds and their exercise numbers, A_k(j), α(n).
- Every number recomputed by hand or by independent scratch simulations (B-tree insertion, union-find
  in all four rule combinations); Fibonacci-heap and vEB worked examples, exercises and quiz answers
  traced by hand, call by call. Every lab figure cited in prose checked against `labcheck.js --observe`
  and the per-operation tables read in Playwright.
- Quotations: six, all `quotes.py` OK (18, 16 in two, 33, 20, 12 words per lesson). `overlap.py 8`:
  only the counted quotations, "O(lg lg u) time in the worst case", an exercise number pair and two
  runs of digits from tables.

## Findings and fixes

All five lessons were accurate on the book's argument and every lab figure; the errors were in
quiz details and lab descriptions.

1. Lesson 5 quiz (weighted union, 1,000 objects, answer 10): wrong as worded. Doubling caps the
   changes at ⌊lg 1000⌋ = 9; 10 is only the theorem's ⌈lg n⌉ bound. Changed to 1,024 objects, where
   10 is both the bound and attainable; distractors and explanation rewritten.
2. Lesson 5 mistake: "on `pairs` the worst find walks 3 even with both rules on" was false (both rules
   give 2; 3 is union by rank alone, the preset's setting). Corrected.
3. Lesson 5 lab description: the tallest-root tile with the rank rule off and compression on reports
   the depth the unions built, not the current depth (reads 11 on `chain` after compression flattened
   it), and "operations" leaves out the n MAKE-SETs that the book's m counts. Both now said plainly.
4. Lesson 3 quiz on Lemma 19.4: reworded to "the least size Lemma 19.4 allows", and its explanation no
   longer asserts something it does not show; explanation of the ΔΦ = 7 distractor made exact.
5. Lesson 3: the theorem paraphrase now names the original t(H) roots among the t(H) + c; the lemma tile's
   "closest 40" notes the tie with the leaves and the lab's tie rule.
6. Lesson 4: VEB-TREE-INSERT's swap with min (the old minimum is the element carried down) added to the
   prose; it had only been in the steps.
7. Lesson 5 quiz on ranks: the explanation of the "number of nodes" distractor rewritten (it said
   "not exactly r").

## Kit observations (not edited)

- `seqkit/unionfind`: with union by rank off, the "Depth of the tallest tree" tile is `rank[y] =
  max(rank[y], rank[x] + 1)`, which ignores compression. With compression on it shows a depth that
  is no longer there (11 on a 12-element chain whose final depth is 1).
- `seqkit/unionfind`: the status banner always prints, in red, "Union does not link the two roots
  either way.", which reads as false.

## Final state

`python3 scripts/preview_subject.py intro_algorithms --course intro-algorithms-advanced-structures`
prints OK (5 labs executed and swept, 4 pinned pages match). Read-out check clean.
