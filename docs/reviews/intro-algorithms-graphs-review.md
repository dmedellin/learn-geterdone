# Review: Introduction to Algorithms, Course 6, Graph Algorithms

Independent accuracy and pedagogy review of `content/intro_algorithms/c6_graphs/`
(nine lessons, CLRS Chapters 22 to 26) against the book, the rendered labs and
docs/intro-algorithms/PLAN.md. Fixes were made in the course files and the
course's block of `content/spoken/intro_algorithms.py`.

## Method

- Every claim credited to the book (procedures, lemma and theorem numbers and
  statements, bounds, exercise numbers) was checked against the sections with
  `book.py` and `page.py`.
- Every number in the prose, the worked examples and the quiz was recomputed by
  hand: BFS queues and entry counts, DFS intervals for both roots and the
  undirected reading, both SCC passes, Kruskal and Prim with ties, every
  Bellman-Ford round in both arc orders, the dag pass, Dijkstra's settling order,
  the difference-constraint solution, Floyd-Warshall's D(1) to D(4), Johnson's h
  and the reweighted arcs, every augmentation and cut, and the matching.
- Every lab figure the prose cites was read off the rendered page in Chromium
  (Playwright) with the lesson's own graph typed in, and every kit preset the
  prose describes was loaded. All agreed with the prose after the fixes below.
- `quotes.py`: all nine quotations OK (14 to 25 words, one per lesson).
- `overlap.py 8`: only the nine counted quotations, two chapter titles, the
  name of Theorem 26.6 and two runs of digits.
- No lesson points at graphkit `negative`, flowkit `classic` or dfstimes
  `allfour`. No lesson graph is a book figure's.

## Errors found and fixed

1. **Lesson 9, worked example**: a missing comma joined two worked lines into one
   string ("...L3 with R3,  and L4 with R4"). Split back into two lines.
2. **Lesson 9**: the text said Section 26.3 "closes by pointing ahead" to
   push-relabel. That forward look is the opening of Section 26.4. Reworded. The
   mistake "Section 26.4's methods ... O(V²E) and O(V³)" now credits 26.4 and 26.5.
3. **Lesson 9, mistake 2**: "a half-unit on each of two arcs" was a vague and
   wrong-sized example of a fractional maximum flow. It is now L1 and L2 both
   joined to R1 and R2, half a unit on each of the four middle arcs, value 2.
   The lab paragraph now says Hall's condition appears only in Exercise 26.3-4.
4. **Lesson 8**: the augmentation step was credited to "Lemmas 26.1 and 26.2".
   The value increase is Corollary 26.3. Now all three are cited.
5. **Lesson 8, preset zigzag**: mistake 3 compared 3 first-found augmentations
   (which, with backward arcs off, stop at 199) with 2 shortest-path ones. With
   backward arcs on, the lab needs 4 first-found augmentations to reach 200.
   The body and the mistake now give both states correctly. "The cut it returns"
   became the cut the final search marks.
6. **Lesson 6, Theorem 24.6**: the proof sketch left out the step that makes it
   work (u was extracted ahead of y, so u.d ≤ y.d). It now gives the whole chain.
   The lab's "E·lg V" reference is E·⌊lg V⌋ (14 = 7 × 2 on the lesson graph), and
   the text now says so; it used to say "rounded down by the page".
7. **Lesson 4**: "Chapter 23 quotes the strategy of Chapter 16" was wrong (the
   chapter restates it). Exercise 23.1-2's converse was misstated as "light for
   every cut that respects A". It is now "light for that cut", the cut it
   crosses, and the quiz distractor was changed to match.
8. **Notation (PLAN §F)**: the 2nd-edition `d[u]`, `f[u]` became the 3rd
   edition's `u.d`, `u.f` in lessons 1, 2, 3 and 5, including key lines. Lesson 5
   says once that `d[2]` stands for vertex 2's estimate. The spoken entry for the
   changed key line was updated.
9. **Smaller fixes**: BFS hexagon ("the edge to 3 was dequeued first" became
   "3 is dequeued before 5"). DFS: the nested quotation mark, and a note that
   read undirected, `1 → 4` and `4 → 1` become two parallel edges, both back
   edges. The kit presets the prose named only by id (`negcycle` twice, `stale`,
   `perfect`, `three`, `sourcefirst`) now carry the description the lab's menu
   shows, so a reader can find them.

## Checked and left as written

The quizzes: every answer is right and no distractor can be argued for. The
"Exercise" paragraphs are the course's own instances. The early stop in the
Bellman-Ford lab and the lazy heap in the relax lab are both stated plainly in
the lessons and in the notes.

## Open

- `scripts/speechcheck.py` reads only GENERATED_PATHS, and intro_algorithms is
  not wired yet, so it cannot cover this course. The preview's own read-out check
  is clean.
- When this review ran, other courses (c1, c4) were part-written, so the package
  would not import. The preview was run through a scratch shim that loads the
  real c6 files and stubs only the missing modules of other courses. It printed
  OK. Run it again directly once the package imports.
