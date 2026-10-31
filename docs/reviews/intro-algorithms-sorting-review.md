# Review: Introduction to Algorithms, Course 2, Sorting and Order Statistics

Independent accuracy and pedagogy review of `content/intro_algorithms/c2_sorting/`
(seven lessons, CLRS 3rd ed., Chapters 6 to 9) against the book's sections, the
rendered labs and the authoring rules in `docs/intro-algorithms/AUTHORING.md`.

## Method

- Every claim the lessons pin on the book was checked against the sections,
  using `book.py` and `page.py`: the in-place and virtual-memory remarks, the
  BUILD-MAX-HEAP invariant, the 2n/3 subtree bound, the exercise numbers 6.1-2,
  6.1-7, 6.2-2, 8.3-2 and 8.3-3, equation (3.19), Lemma 7.1, random sampling's
  simpler analysis, Theorem 8.1 and Corollary 8.2, Lemmas 8.3 and 8.4,
  E[n_i^2] = 2 - 1/n, the tournament argument, the lower median, and the
  groups-of-five bound with its constant 140. Chapter-end problem titles were
  listed and compared with what `not_covered` names.
- Every number was recomputed by hand or with a scratch simulator: the sum over
  heights at n = 8, 10, 20 and 31; both by-hand heap builds; the heapsort trace
  of six keys (7 + 10 comparisons); the extract-and-insert exercise; both
  partitions and the whole quicksort on the lab array (19 comparisons); E[X] at
  n = 3, 4, 5 and 7 by pairs and by 2(n+1)H_n - 4n; ceil(lg n!) for n = 3, 4, 5,
  10, 16 and 1024; counting sort's tallies, prefix sums and placements; the
  Lemma 8.4 table; the bucket indices and squared sizes; all radix passes; the
  min-and-max traces; and the groups-of-five count at n = 60.
- Every lab figure the prose cites was read from the rendered page: with
  `labcheck.js --observe` for presets and selects, and with a Playwright script
  for slider-dependent values (heap build at n = 20 and n = 10, pivot positions
  9 and 1, the step table, the expected-comparisons table for every input and
  at n = 5, selection at seeds 7, 8, 9 and 10, the last-element rule on sorted
  input, the radix variants' pass tables, counting sort placed from the front).
  All matched the prose.
- Quotations: eight runs, all `quotes.py` OK (9, 20, 17, 13, 14, 17, 15 and
  2 words; no lesson over 60). `overlap.py 8` prints only those quotations, the
  standard phrases "it runs in O(n lg n) time" and "run in O(lg n) time on an
  n", and the PARTITION invariant written as mathematics.

## Findings and changes

1. **Wrong problem names (course `not_covered`).** It named "stooge sort" for
   Chapter 7 and "the nuts-and-bolts problem" for Chapter 8; neither is in the
   3rd edition (stooge sort was dropped after the 2nd). Replaced by Problems
   7-5 (median-of-3 partition) and 8-4 (water jugs).
2. **Misdescribed proofs (course `not_covered`).** It said the expected-time
   bound for randomized selection and the constant 140 are left to the
   exercises. Both are proved in full in Sections 9.2 and 9.3. Reworded: the
   substitution proofs are outlined in the lesson and left to the book.
3. **Wrong cross-reference (Heapsort and Priority Queues).** "Section 7.4 and
   Chapter 8 return to both properties" (stability, non-adaptivity). Section
   7.4 is about neither. Now: Chapter 8 defines stability and Exercise 8.3-2
   asks which earlier sorts are stable; the book does not take up the second
   property.
4. **Lower bound misapplied (Heapsort and Priority Queues).** The prose said
   the lab's counts "sit inside those limits on every array", but merge sort
   makes 32 comparisons on sorted input, below ceil(lg 16!) = 45. The paragraph
   now gives heapsort's range (72 to 85), says the 32 is below 45, and explains
   why that is no contradiction (the bound is about each sort's worst input).
   The matching quiz explanation was tightened the same way.
5. **Overclaim in the groups-of-five sketch (Medians and Order Statistics).**
   The math block and prose said the two recursive calls handle "at most nine
   tenths" of the keys and each level costs "at most" 9/10 of the one above.
   With the ceiling and the + 6 that is false for every n. Now "about", with a
   sentence saying the sketch ignores those terms and that this is why the book
   proves the bound by substitution with the 140 threshold.
6. **Quiz explanation that did not explain (Randomized Quicksort).** The 1/2
   distractor was said to "ignore the three keys between them", which gives
   probability 1, not 1/2. Now: 1/2 is 2/(j - i), a four-key set that leaves one
   key out.
7. **Loose wording (Heaps).** "The bound is met, so on this input it cannot be
   improved" now says that at 31 keys no smaller number could bound every
   arrival order.

Everything else checked out: all worked examples, exercises, quiz answers and
lab figures are right, each distractor is wrong for the reason its explanation
gives, and each lesson sets out the book's argument (invariant, recurrence or
counting argument) before the lab, with notes saying what the lab cannot show.

## Left open

- `scripts/speechcheck.py` does not yet list the intro-algorithms Subject, so
  the read-out was checked through the preview's own read-out pass, which is
  clean.
- The heap lab builds a min-heap from the keys 1 to n only; the lesson says so
  and works the max-heap and the reader's own arrays by hand (a kit limit, not
  a content error).

Final preview: `python3 scripts/preview_subject.py intro_algorithms --course
intro-algorithms-sorting` prints OK (7 labs executed, 0 failing).
