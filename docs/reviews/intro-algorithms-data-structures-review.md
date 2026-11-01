# Review: Introduction to Algorithms, Course 3 — Data Structures

Independent accuracy and pedagogy review of `content/intro_algorithms/c3_data_structures/`
(slug `intro-algorithms-data-structures`) against CLRS 3rd ed., Chapters 10–14.

## Method

- Every claim attributed to the book checked against the sections (book.py / page.py),
  including Theorems 11.1–11.3, 11.5, 11.6, 11.8, 11.9, Corollaries 11.4, 11.7, 11.11,
  Theorems 12.1–12.4, the five properties, Lemma 13.1, RB-INSERT-FIXUP and RB-DELETE-FIXUP
  cases, OS-SELECT/OS-RANK, Theorems 14.1–14.2, section numbers and attribute notation.
- Every worked example, exercise answer and quiz answer recomputed by hand (queue wrap,
  chains mod 7/11/8, residue-class counts at p = 5, 7, 11, 13, the multiplication hashes of
  77/78/79 at w = 8, linear and double probing on 11 slots, the ten-key BST, the eight-node
  red-black tree, the insertion sequences 10 30 20 50 40 / 15 5 10 25 20, the case-4
  deletion, the ten-key order-statistic tree).
- Every lab figure the prose cites checked on the rendered pages (`labcheck.js --observe`
  for presets, Playwright for the reader-typed instances).
- `quotes.py`: all eight quotations OK (11–19 words, one per lesson).
  `overlap.py 8`: only the eight counted quotations, a section title and the probe-sequence
  notation of 11.4.

## Findings and fixes

1. **hash/chaining's successful-search tile (kit bug, confirmed).** `algo_core.chainRun`
   computes 1 + α/2 − α/(2m); Theorem 11.2's analysis (p. 260) ends 1 + α/2 − α/(2n) =
   1 + (n − 1)/(2m). The lesson already flagged it, but called the difference "slight" and
   never showed the tile's value. Rewritten: the lesson says the tile is not the book's
   figure, gives the tile's value beside the book's on each cited example (67/32 vs 35/16,
   79/64 vs 39/32, 79/49 vs 23/14), says they agree only at n = m, and the note says the same.
2. **tree/bst deletes by copying the successor's key** (the first two editions' method,
   which the chapter notes contrast with the 3rd edition's TRANSPLANT). The lesson
   presented the lab as running TREE-DELETE and attributed "2 to reach 72" to it. Added a
   paragraph stating the departure and its consequence (same tree, but the lab's second
   search adds comparisons TREE-MINIMUM would not make); corrected the worked example's
   comparison breakdown and the note.
3. **hash/probing's quadratic rule** is h′(k) + i + i² (c₁ = c₂ = 1). Since i + i² is even,
   in the lab's power-of-two tables it reaches only half the slots, so it is not a
   permutation as 11.4 requires. The lesson only said "not the one Problem 11-3
   recommends"; it now says plainly what the rule is and why it is set aside.
4. Red-black insertion: "every third insertion bend inward" for 10 30 20 50 40 70 60 was
   wrong (the 3rd, 5th and 7th bend); fixed. A quiz distractor said case 2 "moves z down a
   level" (z's depth does not change); reworded so it is plainly wrong. The deletion
   paragraph said cases 1, 3 and 4 "end the loop"; case 1 leads into another case, so it
   now says how the loop stops after case 1.
5. Smaller: lesson 1's quiz explanation now says a front insertion costs the shifts plus
   one write; lesson 8's exercise says how to choose 39 on the rank slider (the lab picks a
   key by sorted position) and what to compare.

Everything else checked out: all quiz keys correct, every distractor wrong, every cited
lab figure matches the rendered page.

## Left open (kit, not edited)

- `algo_core.chainRun`: replace `alpha/(2m)` by `alpha/(2n)` (and the table's label
  "1 + α/2 − α/2m" in `hash.py`), then re-pin the hash-chaining presets.
- `algo_core.probeSlot` quadratic: `h + i + i*i` is not a permutation for m a power of 2;
  `h + (i + i*i)/2` (Problem 11-3's triangular rule) would be.
- `tree` bst: deletion copies keys rather than transplanting nodes; acceptable for shapes,
  stated in the lesson.

Final preview: `python3 scripts/preview_subject.py intro_algorithms --course
intro-algorithms-data-structures` prints OK.
