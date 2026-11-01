# Review: Introduction to Algorithms, Course 7, Parallel, Matrix, Linear and Number Algorithms

Independent accuracy and pedagogy review of `content/intro_algorithms/c7_algebraic_topics/`
(seven lessons, CLRS Chapters 27 to 31) against the book, the rendered labs and
docs/intro-algorithms/PLAN.md. Fixes were made in the course files only; the
course's block of `content/spoken/intro_algorithms.py` needed no change.

## Method

- Claims credited to the book were checked against the sections with `book.py`
  and `page.py`: Theorem 27.1 and Corollaries 27.2–27.3, the P-FIB, matrix
  multiplication, MERGE-SORT′, P-MERGE and P-MERGE-SORT recurrences, LUP and
  Corollary 28.6, Theorems 28.1–28.2, Lemmas 29.4–29.6, Lemma 29.8, Corollary
  29.9, Theorem 29.10, L_aux, Lemmas 29.11–29.12, Theorem 29.13, Theorems
  30.1, 30.2, 30.7, 30.8, Corollary 30.4 and Lemmas 30.3–30.6, Lemma 31.10,
  Lamé's theorem, Theorem 31.20, the CRT, MODULAR-EXPONENTIATION, Theorem
  31.36, Corollary 31.35, Theorems 31.38–31.39 and the closing remarks of 31.8.
- Every number was recomputed by hand: P-FIB work and span from n = 0 to 25,
  MERGE-SORT′ on 1,024, the seven-strand example, all three LUP presets
  (including det and π's parity) and the worked solve, both simplex walks and
  the 5, 1 objective, the dual, the chain values, the L_aux worked example and
  its infeasible variant (−1/3), the size-4 DFT, every FFT count, Euclid on
  1147/851 and the Fibonacci pairs, the congruence, the CRT, 5^117 mod 391,
  the RSA key (n = 2881, d = 1109, 1000 → 962 → 1000, and the CRT check), the
  2047 strong-liar count (242 over 1..n−1 by the closed formula, 240 in the
  lab), base 3 on 2047, and the 1387 exercise.
- Every lab figure cited in prose was read off the rendered page (labcheck
  `--observe` and Playwright, with the lesson's inputs typed in).
- `quotes.py`: seven quotations, all OK (11 to 29 words, one per lesson).
- `overlap.py 8`: only the counted quotations and a run of ones from a preset.
- Preview read-out check clean; preview prints OK.

## Errors found and fixed

1. **Lesson 6, copyright**: the mistake on reducing late quoted `7^560`, the
   base and exponent of the book's Figure 31.4 (7, 560, 561). Replaced by `2^1000`.
2. **Lesson 3, copyright**: the four-repairs example had the same structure as
   the book's 29.1 conversion example, with numbers changed (minimize, one
   equality, one ≥ row, x₁ ≥ 0, x₂ free). Replaced by a program built
   differently (x₁ free, the ≥ row first).
3. **Lesson 4**: said the OR Subject's Phase I (simplex kit `phase1`) uses "one
   artificial per row". The kit adds one only for each ≥ or = row. Fixed in
   the body and the note.
4. **Lesson 7, how the lab counts**: the lab writes n − 1 = d·2ˢ and calls the
   number of bases t, the other way round from the book's 2ᵗ·u and s, and the
   lesson's own "t random bases ... (1/4)ᵗ" mixed the two up. The lab paragraph
   now names the swapped letters, the (1/4)-per-base bound against 2^(−s), the
   three-quarters tile against Theorem 31.38's half, and the base range 2..n−2
   against the book's RANDOM(1, n − 1).
5. **Lesson 6, modexp counts**: "differ by one" is now said plainly. On 117 the
   lab makes 6 squarings, the book's procedure makes 7 (one per bit, the first
   squaring 1), and both make 5 multiplications.
6. **Lesson 6**: "(89, 55) ... every quotient 1" is wrong, because the last
   quotient is 2. A quiz explanation called (23, −31) the zero row; the zero row
   is (−23, 31).
7. **Lesson 1**: the seven-strand DAG could not come from one procedure,
   because a sync waits for every child, including `load`. It now uses a helper
   procedure. "Theorem 27.1 shows it never takes more than twice" is
   Corollary 27.2. The worked P-FIB table now says it uses Figure 27.2's
   counting.
8. **Lesson 2**: "third pivot −2/3, negative, because the rule compares absolute
   values" now reads "chosen over −1/3 because ...".
9. **Lesson 7**: Bayes remark now gives the book's figure (about nine trials) and
   the (n − 1)/4 remark adds that some n reach it.
10. **Lesson 3, `orchard`**: the lesson never repeated the "five corners" label.
    It now says the page lists four, because all three lines meet at the
    degenerate corner (3, 4). This ties in with its degeneracy paragraph.

## Left open (kit issues, not edited)

- `simplex.py` WALK_PRESETS: `orchard`'s label "three resources, five corners"
  is false. The region has four corners, and (3, 4) is triply tight.
- `random` witness mode: its explanatory line says a base is a witness "if it
  never reaches 1 or n−1". Read alone, that leaves out a chain that reaches 1
  from a nontrivial root. The next sentence covers that case, and the tiles are
  correct. This is minor wording.
- The lesson-1 worked table passes through P-FIB(4)'s totals (17, 8), which are
  the book's Figure 27.2 numbers. They are kept because they come from the
  recurrence, and the DAG is not drawn.
