# Pedagogy assessment — Graphs and Trees (discrete mathematics, course 7)

First assessment, formed from the fourteen lesson dicts in
`content/discrete_math/c7_graphs/` (`part_a.py`, `part_b.py`, `__init__.py`)
and the one lab they all render through, the fourteen-mode graph workbench in
`scripts/mathpath/labs/graph.py`, as they stand on `main` at e893ab3. No prior
assessment exists for this course (`docs/pedagogy/prior/` holds none).

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `graphs-and-graph-models`, `degree-and-the-handshake-theorem`,
`graph-representations`, `paths-and-connectivity`, `graph-isomorphism`,
`bipartite-graphs`, `euler-and-hamilton`, `graph-traversal`,
`shortest-paths`, `trees`, `tree-traversals`, `spanning-trees`,
`graph-colouring`, `planar-graphs`. The course declares courses 1–4 as
prerequisites ("proof, sets, relations and counting") and points into
courses 1, 2, 3, 4 and 8, so it is judged against what those teach:
precedence of connectives (course 1 lesson 2), SAT and its solvers (course 1
lesson 6), equivalence relations and partitions (course 2 lesson 8), partial
orders (course 2 lesson 9), the pigeonhole principle and its two-people-share-
a-degree example (course 2 lesson 14), recursive definitions and structural
induction (course 3 lessons 6 and 7), `Θ` as defined for the master theorem
(course 3 lesson 11), combinations (course 4 lesson 4), combinatorial proof
(course 4 lesson 13), binary search (course 8 lesson 6), greedy algorithms
and the `{1, 3, 4}` coin example (course 8 lesson 9), and NP-completeness
(course 8 lesson 11). Every one of those cross-course pointers was checked
against the real lesson order of the packages, and every one resolves. The
pointers that do not resolve are the ones inside this course (item 1).
Every figure quoted below was recomputed by hand, and every lab figure by
executing the shipped lab JavaScript at the shipped preset.

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** State
  what a vertex and an edge are before anything else
  (`graphs-and-graph-models`); check parity before attempting a
  construction (`degree-and-the-handshake-theorem`); predict which
  structure suits a problem (`graph-representations`); find the components
  and the bridges by hand (`paths-and-connectivity`); reach for invariants
  before a bijection (`graph-isomorphism`); produce the odd cycle from a
  failed colouring (`bipartite-graphs`); settle Euler in one pass and say
  why Hamilton is different (`euler-and-hamilton`); predict both visit
  orders (`graph-traversal`); say where the correctness proof uses
  non-negativity (`shortest-paths`); prove one characterisation from
  another (`trees`); produce all three orders from a drawing
  (`tree-traversals`); run Kruskal and justify each rejection
  (`spanning-trees`); bound `χ` from both sides (`graph-colouring`); rule
  out planarity by counting (`planar-graphs`). None is "understand X".
- **The course has one spine and names it at both ends.** The handshake
  theorem is proved as a double count in lesson 2 and then does the work in
  lesson 7 (Euler's parity condition), lesson 10 (the tree edge count) and
  lesson 14 (`3F ≤ 2E`, and the degree-5 vertex that seeds the five-colour
  theorem); lesson 14's last paragraph says so: "this course ends where it
  began". Lesson 4's edge bound is picked up by lesson 10 as the boundary
  trees sit on, and lesson 8's BFS is picked up by lesson 9 as Dijkstra's
  special case.
- **The easy/hard contrast is taught as content, not as a remark.** Euler
  against Hamilton (lesson 7's table "is the lesson"), 2-colouring against
  3-colouring (lessons 6 and 13), and the isomorphism problem's "unusual
  middle position" (lesson 5) are each stated with the proof or the
  evidence behind them, and each forward-points to course 8 lesson 11 for
  what NP-complete means rather than pretending to define it here. The
  workbench's Hamilton mode is exhaustive and the course home says why
  that caps the vertex count at eight.
- **The misconceptions named are the real ones.** A graph read as a plot;
  the drawing taken for the object; `Σ deg = |E|`; an even degree sum
  taken as realisability (`(5, 3, 3, 2, 1)`); walks confused with paths;
  matching invariants taken as isomorphism (two triangles against `C₆`);
  triangle-free taken as bipartite (`C₅`); Dirac read in reverse (`Cₙ`);
  connectivity forgotten in Euler's criterion; DFS used for distances;
  marking on removal; BFS on a weighted graph; adding a constant to make
  weights non-negative; `n − 1` edges alone taken as a tree; preorder
  expected to be sorted; greedy's answer taken as `χ`; "planar needs four";
  the outer face forgotten; the triangle-free bound applied to a graph
  with triangles.
- **The numbers are almost all right.** `K₅` 10, `K₁₀` 45, `K_{3,3}` 9,
  `n · 2^{n−1}`; the four existence questions; `(4, 3, 3, 2, 2)` realisable;
  `A` and `A²` for `C₄` and `trace(A³) = 0`; the seven-vertex worked graph's
  components, cut vertex and bridges; the bijection `1→a, 2→b, 3→d, 4→c`;
  the parity colourings of `C₆` and `C₅` with the conflict at `3–4`;
  Königsberg's `5, 3, 3, 3` and both repairs; the BFS and DFS orders and
  tree edges on the six-vertex graph; Dijkstra's four settlings to 6; the
  three six-vertex graphs; the expression tree and the six-key search tree
  in all four orders; Kruskal's seven decisions to 10; the exam schedule
  `{A, D}, {B, E}, {C}`; the cube, `K₅`, `K_{3,3}`, Petersen, `K_{4,4}` and
  `F = 7` — all recomputed and all correct. The exceptions are items 2–4
  below.

## What it teaches badly, or claims and does not deliver

### Pointers a reader would follow that point at the wrong lesson

1. **Seven intra-course lesson numbers are wrong, and the course home's
   map of the course is wrong.** `graphs-and-graph-models` says "Lessons 8
   and 10 attach weights" (weights arrive in lessons 9 and 12) and
   "Shortest paths are lesson 10" (lesson 9). `degree-and-the-handshake-
   theorem`'s note says "lesson 11's tree characterisation" (lesson 10).
   `graph-representations` says "the traversals of lesson 9" (lesson 8) and
   "Kruskal's algorithm in lesson 13" (lesson 12). `paths-and-connectivity`
   says "Breadth-first or depth-first (lesson 9)" (lesson 8) and "Lesson 11
   shows that `n − 1` edges suffice" (lesson 10). `bipartite-graphs` says
   "lesson 12's chromatic number" and "Lesson 12 returns to it" (lesson 13,
   both). The course home's `syllabus_intro` says "Lessons 1 to 5 are the
   basics, 6 to 10 are traversals and paths, 11 to 13 are trees, and 14 is
   planarity"; the lessons' own `module` fields say Basics 1–3, Structure
   4–6, Traversal 7–9, Trees 10–12, Colouring and planarity 13–14. Every
   pointer to another course is right; every wrong pointer is to this one.

### Facts a reader would trust that are wrong

2. **`graph-traversal`'s worked example names the wrong back edge.** The
   DFS trace is `1 → 2 → 4 → 3`, so `4–3` is a tree edge (3 is discovered
   from 4), and the `after` paragraph then says "The edge `3–4` is a back
   edge and closes the cycle `1–2–4–3–1`." The back edge is `3–1`: at vertex
   3 the neighbour 1 is already visited and is not 3's parent. The cycle is
   right; the edge named is the one edge in it that is not a back edge.
3. **`shortest-paths`' worked example claims a BFS result that depends on
   an order the example does not fix.** "shortest by EDGES: `s → b → t` two
   edges, weight 12 … BFS would have returned the two-edge route — twice
   the cost." `s → a → t` is also two edges, weight 11, and a BFS that lists
   `a` before `b` returns it. The point survives — either two-edge route
   costs at least 11 against 6 — but "twice" is true of one of them.
4. **`trees`' standard asks for a proof by a lemma that does not apply.**
   "Prove that a connected graph with `n − 1` edges is acyclic, using the
   leaf lemma and induction." The leaf lemma is about trees, and whether
   the graph is a tree is what is being proved; the body already proves
   this direction by cycle removal. What the body does not prove, and the
   standard could ask for, is (3) ⟹ (1): an acyclic graph with `n − 1`
   edges is connected — four lines from the forest edge count
   `|E| = n − c` that the lesson's own third mistake states. The same
   lesson says "the parent relation is a partial order": it is not
   transitive; the ancestor relation is.

### Labs that do not agree with their own lessons

5. **`graph-traversal`'s panel promises two trees on a preset where there
   can only be one.** "Switch to DFS and … the tree drawn changes shape
   completely on the same graph." The preset is `tree`, `n = 7`. A tree has
   no non-tree edges, so BFS and DFS from vertex 1 both draw every edge —
   the same tree, in both modes. The worked example's graph (`1–2, 1–3,
   2–4, 3–4, 4–5, 5–6`), which does produce different trees, cannot be
   loaded: the workbench has eight fixed presets and no way for a lesson
   to supply its own.
6. **`shortest-paths`' panel says the two distances "on most graphs …
   disagree", and the page opens on a graph where they agree.** At the
   preset (`complete`, `n = 6`, the formula weights) Dijkstra `1 → 6` is the
   direct edge of weight 3: one edge, and the fewest-edge distance is one.
   The status line under it says "Here the cheapest route happens to use
   the fewest edges too." The worked example — `s, a, b, t` with weights
   10, 3, 2, 1, 9, cheapest 6 by three edges against two-edge routes of 11
   and 12 — is exactly the disagreement the panel promises, and the lab
   cannot show it because its weights are a fixed function of the
   endpoints.
7. **`spanning-trees`' lab cannot run the lesson's Kruskal.** The worked
   example is `AB 1, BC 2, CD 3, DE 4, AE 5, AC 6, BD 7`; the lab's weights
   are `((7i + 13j) mod 9) + 1`, so no graph the reader builds carries
   them. The preset (`K₆`) gives total 12 with fifteen decisions, and the
   panel quotes none of them.
8. **`trees`' status line can describe a forest with a cycle.** For a
   disconnected graph with a cycle the lab prints "it is a forest with at
   least one cycle" — a forest is acyclic by definition, and the worked
   example's graph C (two components, one triangle) is exactly the case,
   which the lesson's own worked example gets right ("It is a forest? No").
9. **`tree-traversals` teaches three orders and its lab shows one.** The
   lab is DFS from vertex 1, whose visit order on the `tree` preset is the
   preorder `1 2 4 5 3 6 7`; inorder and postorder — the two the lesson's
   standard, quiz and first mistake are about — are not computed anywhere
   on the page. The panel says "the labels are visit order, not distance",
   which is true and is not the lesson.
10. **`planar-graphs`' panel says "check the bound yourself", and the lab
    computes nothing about planarity.** The mode is `degree` on `K₅`; the
    reader is told the numbers (ten edges against `3V − 6 = 9`) and left to
    do the arithmetic the page could do. Nothing on the page evaluates
    `3V − 6` or `2V − 4`, tests for triangles, or looks for `K₅` or
    `K_{3,3}`.
11. **`graph-colouring`'s lab computes a clique bound and throws it away,
    and mislabels the greedy bound.** The `colour` mode has a variable
    `clique` (2 or 3, from the bipartite test) that is never displayed; the
    fact row reads "Brooks-style bound `Δ + 1`", but Brooks's theorem gives
    `Δ`, and `Δ + 1` is the greedy bound the lesson proves. The lesson's
    method — clique lower bound, greedy upper bound, compare — is not what
    the lab does. The panel's "build a bipartite graph and check whether
    greedy finds the two-colouring — it does not always" gives the reader
    no graph on which it fails; one exists on six vertices (`1–4, 1–6, 3–2,
    3–6, 5–2, 5–4`: greedy in vertex order uses three colours).
12. **`paths-and-connectivity`'s lab finds components and not the
    bridges.** The standard is "find the components and the bridges by
    hand"; the lab colours components and has no mode that names a bridge
    or a cut vertex, and the worked example's graph (three components, cut
    vertex 3, bridges `3–4` and `5–6`) is not loadable.
13. **`graph-representations`, `graph-isomorphism`, `degree-and-the-
    handshake-theorem` and `graph-colouring` open on graphs that are not
    in their lessons.** Lesson 3's lab opens on "two triangles joined"
    (`trace(A³) = 12`, two triangles) when its worked example is `C₄`
    (`trace(A³) = 0`), a preset the lab has. Lesson 5's opens on `K_{3,3}`
    in degree mode; its worked example is `C₆` against two disjoint
    triangles, and the second cannot be built from a preset. Lesson 2's
    worked example includes the cube `Q₃`, eight vertices of degree 3,
    which fits the lab and is not on it. Lesson 13's opens on "two
    triangles joined" and not on the five exams. Every panel on the course
    describes the mode correctly and quotes none of its figures.
14. The preset the select calls "Two triangles joined" is keyed `petersen`
    in the source and in every lesson that uses it; the Petersen graph has
    ten vertices and does not fit the lab. This confuses the maintainer
    rather than the reader and is noted, not changed.

### Order and prerequisites

15. Lesson 1's worked example uses the handshake theorem "before it was
    stated" for `Qₙ`, and says so; lesson 2 states and proves it. This is
    a deliberate early use with the debt named, and I have left it.
16. Lesson 3 uses `O(1)`, `O(n²)`, `Θ(n + |E|)` and `O(n^ω)` without a
    pointer; `Θ` was defined on this path in course 3 lesson 11 "as much as
    is needed", and the full treatment is course 8 lesson 4. A pointer
    belongs where the notation first carries weight.
17. Lesson 10's rooted-tree paragraph points at course 2 lesson 9 for the
    partial order, which is right once the relation is the ancestor
    relation (item 4).

### Distractors and feedback that does not answer

18. Of the 42 `why` fields, almost all restate the rule and answer no
    distractor. The reader who chose 10 for the degree sum of ten edges is
    not told that is `|E|` with the halving forgotten (the lesson's own
    first mistake); who chose "`n` is prime" for a 3-regular graph is not
    shown `K₄`; who chose "paths" for `A²[i][j]` is not shown `A²[i][i]`;
    who chose "it has a cycle" for `K₅`'s non-planarity is not told `K₄`
    has cycles and is planar; who chose "always prime" — none is answered.
    No distractor was found to be arguably true; the shape of the questions
    is sound and the feedback is thin.

### Cognitive load and structure

19. `trees` carries the six-way equivalence, the leaf lemma, rooted trees,
    the binary-tree height bound and Cayley's formula. The act is one
    (recognise a tree from two of three conditions) and the standard and
    worked example both measure it; not split, but the standard is
    re-aimed (item 4).
20. `bipartite-graphs` carries Hall's theorem after the odd-cycle
    characterisation. Hall is context for the applications list and is
    not on the lab, the quiz or the standard; not split.
21. The course home lists four outcomes and omits the acts lessons 10–11
    and 14 close on — recognise a tree, produce the three orders, rule out
    planarity by counting. Its `how_to` says nothing about which lab mode a
    lesson opens on.

## Where a learner gets stuck

- At `graph-traversal`'s lab, switching to DFS and finding the same tree
  the panel said would change shape (item 5); then at the worked example,
  looking for the back edge `3–4` in a trace where it is a tree edge
  (item 2).
- At `shortest-paths`' lab, reading "Here the cheapest route happens to use
  the fewest edges too" under a panel that promised the opposite (item 6).
- At `spanning-trees`' lab, trying to enter weight 1 on `AB` (item 7).
- At `trees`' standard, trying to apply the leaf lemma to a graph not yet
  known to be a tree (item 4).
- At `tree-traversals`' standard, having no way to check an inorder or
  postorder (item 9).
- At `planar-graphs`' lab, told to check a bound the lab does not show
  (item 10).
- At `graphs-and-graph-models`, sent to "lesson 10" for shortest paths and
  arriving at trees (item 1).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered, so the five URL declarations are untouched. Every content edit
is in `content/discrete_math/c7_graphs/` and the fifteen pages under the
slug (fourteen lessons and the course home) are rebuilt from it. The lab
changes are in `scripts/mathpath/labs/graph.py`; the algorithms the lab
runs (presets, degrees, components with a vertex excluded, BFS, DFS,
Dijkstra, the parity 2-colouring, greedy colouring, the clique number,
Kruskal, the exhaustive Hamilton search, matrix powers, the rooted
traversal orders and the planarity counts) are now a `GRAPH_JS` block
executed by a graphs section in `scripts/mathcheck.js`, which was shown to
fail when Kruskal's cycle test was deliberately broken and passes with it
restored. Every figure a panel now states was obtained by executing the
shipped lab JavaScript at the shipped preset.

Lab (`graph.py`):

- A lesson may supply its own graph. A `"example"` entry in the lab config
  — an edge list, each edge optionally carrying a weight — adds a preset
  "This lesson's example" to the select, and the page opens on it when the
  lesson asks. While that preset is selected, the example's weights are
  used and any edge the reader adds takes the formula weight; every other
  preset keeps the formula, so two readers who build the same graph still
  get the same tree.
- New mode `cuts`: every bridge and every cut vertex, each found by
  removal and recounting, with the status line naming which components
  each separates.
- New mode `orders`: the tree rooted at vertex 1 with children in
  increasing order — preorder, inorder, postorder and level order. Inorder
  is reported only while no vertex has more than two children, and
  otherwise names the vertex that has three, which is the lesson's second
  mistake; on a graph that is not a tree the orders are those of the
  depth-first spanning tree and the status says how many edges were left
  out.
- New mode `planar`: `E` against `3V − 6`, the triangle test from
  `trace(A³)`, `E` against `2V − 4` when triangle-free, a search for `K₅`
  and `K_{3,3}` as subgraphs, and a verdict — not planar by a bound, not
  planar by a subgraph, planar because at most four vertices or at most
  eight edges (no subdivision of `K₅` or `K_{3,3}` fits in eight edges), or
  inconclusive, in which case the status says that subdivisions were not
  searched for.
- `colour` reports the clique number `ω` (exhaustive, `n ≤ 8`) beside the
  greedy count and `Δ + 1`, labels the second correctly as the greedy
  bound, and says whether the bounds meet — the lesson's method.
- `tree` no longer prints "a forest with at least one cycle"; a
  disconnected graph is reported as a forest or as neither, with the
  component and cycle counts.
- `walks` says how to edit the graph while `A²` is displayed.

Lessons:

- `graphs-and-graph-models`: weights are in lessons 9 and 12, shortest
  paths in lesson 9; the panel reads `|E| = 10 = C(5, 2)` on `K₅` and sends
  the reader to `K_{3,3}` for 9 and `C₆` for 6; every `why` answers each
  distractor.
- `degree-and-the-handshake-theorem`: the lab opens on the worked
  example's `Q₃` — eight vertices of degree 3, `Σ deg = 24`, `|E| = 12` —
  and the panel sends the reader to remove one edge for two odd vertices
  and to the empty preset for the standard's `(4, 4, 3, 3, 2, 2)`; the note
  points at lesson 10; every `why` answers each distractor, with `K₄`
  against "`n ≥ 6`" and 10 as the halving forgotten.
- `graph-representations`: the lab opens on `C₄` in walk mode and the
  panel reads the worked example's `A²`, `A²[1][4] = 0`, `A³[1][4] = 4`,
  `trace(A³) = 0`, then sends the reader to the two joined triangles for
  12 and 2; the standard states the list length `2|E| = 3 000 000` against
  `10¹²`; the traversals are lesson 8 and Kruskal lesson 12; `Θ` points at
  course 3 lesson 11; every `why` answers each distractor.
- `paths-and-connectivity`: the lab opens on the worked example in `cuts`
  mode, the panel reading cut vertex 3 and bridges `3–4`, `5–6`, and
  sending the reader to Components for `{1, 2, 3, 4}, {5, 6}, {7}` and to
  the Tree preset where every edge is a bridge; the search is lesson 8 and
  the tree characterisation lesson 10; every `why` answers each
  distractor.
- `graph-isomorphism`: the lab opens on two disjoint triangles in degree
  mode; the panel reads `2, 2, 2, 2, 2, 2`, sends the reader to the Cycle
  preset for the same sequence, and to Components for 2 against 1; every
  `why` answers each distractor.
- `bipartite-graphs`: the panel reads `X = {1, 3, 5}, Y = {2, 4, 6}` at
  `n = 6` and "vertices 3 and 4" at `n = 5`, the worked example's figures;
  the chromatic number is lesson 13 (twice); every `why` answers each
  distractor.
- `euler-and-hamilton`: the panel reads the circuit on `C₆`, sends the
  reader to remove `1–2` for odd vertices 1 and 2, an Euler path and a
  Hamilton path without a circuit, and says why Königsberg's parallel
  bridges cannot be drawn in a simple-graph lab and why the theorem holds
  for them anyway; every `why` answers each distractor.
- `graph-traversal`: the `after` names the back edge `3–1`; the lab opens
  on the worked example's graph, the panel reading distances `0, 1, 1, 2,
  3, 4`, BFS order `1 → 2 → 3 → 4 → 5 → 6`, DFS order `1 → 2 → 4 → 3 → 5 →
  6` and the one edge the two trees differ on, then sending the reader to
  the Tree preset to see that on a tree the two searches draw the same
  tree; every `why` answers each distractor.
- `shortest-paths`: the worked example lists both two-edge routes (11 and
  12) and says "nearly twice"; the lab opens on `s, a, b, t` as `1, 2, 3, 4`
  with the worked example's weights, the panel reading weighted distance
  6 by `1 → 3 → 2 → 4`, three edges, against a fewest-edge distance of 2;
  every `why` answers each distractor, including why an offset changes the
  answer.
- `trees`: the standard asks for (3) ⟹ (1) from the forest edge count;
  the body says which implications it proved and that the remaining ones
  are the standard; the ancestor relation is the partial order; the lab
  opens on the worked example's graph C, the panel reading two components,
  five edges, a cycle, "neither tree nor forest", and sending the reader to
  Path and Star for A and B; every `why` answers each distractor.
- `tree-traversals`: the lab is the `orders` mode on the seven-vertex
  tree, the panel reading preorder `1 2 4 5 3 6 7`, inorder `4 2 5 1 6 3 7`,
  postorder `4 5 2 6 7 3 1`, level `1 2 3 4 5 6 7`, and sending the reader
  to the Star preset for an inorder that does not exist; the standard gives
  the three orders to check against (`5 3 1 4 8 7 9`, `1 3 4 5 7 8 9`,
  `1 4 3 7 9 8 5`); every `why` answers each distractor.
- `spanning-trees`: the lab opens on the worked example with its weights,
  the panel reading total 10, the four takes and three rejections in
  order, and sending the reader to Dijkstra on the same graph for `1 → 5 =
  5` against the tree route of 10; the third mistake is now that a
  minimum spanning tree is not a shortest-path tree; every `why` answers
  each distractor.
- `graph-colouring`: the lab opens on the five exams, the panel reading
  `ω = 3`, greedy 3, `Δ + 1 = 4`, "the bounds meet, so `χ = 3`", and giving
  the six edges on which greedy uses three colours on a bipartite graph;
  every `why` answers each distractor.
- `planar-graphs`: the lab is the `planar` mode on `K₅`, the panel reading
  `10 > 9`, sending the reader to the Complete bipartite preset for
  `9 ≤ 12` then `9 > 8`, and to `K₄` for `6 ≤ 6` and planar; every `why`
  answers each distractor, including that `K₄` has cycles and is planar.
- Course home (`__init__.py`): `syllabus_intro` matches the modules; a
  fifth outcome names the acts of lessons 10, 11 and 14; `how_to` says
  every lab opens on its lesson's own example where the lesson has one
  and which modes are new.
