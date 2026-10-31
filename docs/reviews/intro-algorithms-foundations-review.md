# Review: Introduction to Algorithms, Course 1, Foundations

Course `intro-algorithms-foundations` (`content/intro_algorithms/c1_foundations/`)
and the PATH fields in `content/intro_algorithms/__init__.py`. Independent
review against CLRS 3rd ed., Chapters 1 to 5, after the first draft.

## Method

- Read every claim attributed to the book against the sections (1.1–1.2,
  2.1–2.3, 3.1–3.2, 4 opening, 4.1–4.5, 5.1–5.4).
- Recomputed by hand every number in prose, worked examples, exercises and
  quiz answers: the race times and crossovers (81,580; 13,747; 6,312; n = 30),
  every insertion-sort pass (comparisons, shifts, t_j, line sums 5n − 4 and
  (3n² + 7n − 8)/2), every merge level, each witness (n₀ = 100, 997, 8 for
  lg*), the maximum subarrays and crossing scans, closed forms of every
  recurrence preset (Strassen (7·7ʲ − 4·4ʲ)/3, the gap 4ʲ(1 + j(j + 1)/2), the
  T(1) = 50 variant), H_4, H_8, H_9, H_20 and every hiring cost.
- Read every tile off the rendered labs with `labcheck.js --observe` and
  compared with the prose, including tiles not pinned.
- Argued for every distractor.
- `quotes.py` on all eight quotations; `overlap.py 8` on the course and on
  the path `__init__.py`.

## Errors found and fixed

1. Lesson 1: Section 1.1 closes with four threads (data structures,
   technique, hard problems, parallelism), not three; "technique" was missing.
2. Lesson 1: the opening quotation is placed at "the end of Section 1.2";
   it opens the subsection "Algorithms and other technologies", the last part
   of 1.2. Reworded.
3. Lesson 1, quiz 2 explanation: said the crossover "falls by more than half
   a power of ten but not by exactly ten"; it falls by a factor of about 13
   (81,580 to 6,312). Corrected.
4. Lesson 2, quiz 2 explanation: said 4a is shifted twice, by keys 1 and 2;
   it is shifted three times (by both 2s and the 1), and the rebuttal of the
   fourth answer did not follow. Rewritten: neither 4 starts in its final
   place, so the cited rule never applies.
5. Lesson 3, mistake 1: "neither bound is Θ on every input" was unclear;
   now "over all inputs it is neither Θ(n²) nor Θ(n)".
6. Lesson 5, step 5: "fails one step earlier" holds only for the least n₀;
   qualified.
7. Lesson 7: Section 4.4 does not bound the uneven-split tree "from both
   sides"; it reads off an O(n lg n) guess and verifies it by substitution.
   Corrected.
8. Lesson 7, mistake 3: T(1) = 50 multiplies T(1,024) by about 22, not
   "about twenty"; corrected.

## Checked and found right

Definitions of Θ/O/Ω/o/ω, Theorem 3.1, the master theorem's three cases with
regularity and the gaps, the RAM model, the loop-invariant parts, MERGE's
invariant, Lemmas 5.1–5.5, PERMUTE-BY-SORTING's 1 − 1/n, the on-line hiring
1/e, every section and exercise number cited. All lab figures cited in prose
match the rendered labs. PATH: tagline and description state eight courses
and 61 lessons (the real count); material clause identical to PLAN §A; fields
mirror Enterprise Patterns' (no `speech`, as PLAN says).

## Copyright

Quotations (words, quotes.py): L1 15 OK, L2 13 OK, L3 14 OK, L4 19 OK, L5 23
OK, L6 14 OK, L7 30 OK, L8 16 OK. `overlap.py 8`: course 21 runs, all
counted quotations, chapter titles, Theorem 3.1 and Theorem 4.1's statements,
or trivial number runs (1 … 8, 8 … 1, a t_j list of ones); path `__init__.py`
0 runs. No book arrays, figures, pseudocode or exercises reproduced.

## Kit note (not edited)

growth/race prints a same-order ratio below 1 as "1/5,000 ≈ 0.0× B's time"
(seen when the reader switches fnA to n lg n on lesson 1); the rounded figure
reads as zero. Not reached by any preset.

## Final state

`preview_subject.py intro_algorithms --course intro-algorithms-foundations`:
OK (8 labs execute, 8 with pinned figures match).
