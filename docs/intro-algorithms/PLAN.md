# Introduction to Algorithms, Read Along — the build specification

The curriculum, lab and authoring contract for the fifteenth Subject: a
read-along of Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and
Clifford Stein, *Introduction to Algorithms*, third edition (Cambridge, MA: The
MIT Press, 2009; ISBN 978-0-262-03384-8), Parts I to VII in the book's own
order, one lesson per chapter or per group of sections. The operator asked for
it "the same way as the previous ones", all the way to live.

It is built the way *Code Complete* (`docs/code-complete/PLAN.md`) and
*Patterns of Enterprise Application Architecture* (`docs/enterprise-patterns/PLAN.md`)
were, and adopts their conventions by reference wherever this one is silent:
their §E (package, quoting, author's checklist), §F (voice) and §R lessons.
Read before this: `AGENTS.md` §0, §1, §1a, §7, §8; `content/AGENTS.md`;
`docs/enterprise-patterns/AUTHORING.md`.

**This Subject differs from the two read-alongs before it in one large way:
the library already has an Algorithms Subject** (`content/algorithms/`, nine
courses, 112 lessons, path slug `algorithms`) whose labs run most of the
algorithms in this book. The read-along reuses those kits — `seqkit`, `heap`,
`hash`, `tree`, `sortkit`, `greedy`, `dpkit`, `graphkit`, `flowkit`, `random`,
`strings`, `geometry`, `reduction`, `coping` — and the Operations Research and
Discrete Mathematics kits `simplex`, `duality` and `number`, configured with
this Subject's own presets. One new kit, `itakit` (§D), covers the chapters
none of them reaches. Where a lesson's chapter has a matching Algorithms
lesson, the read-along lesson names it by title as the place to practise
further; it never copies its prose.

Contents: §0 the one question · §A PATH · §B courses · §C every lesson ·
§D the new kit · §E package, text, quoting · §F voice · §G left out

---

## §0 The one question: what does the reader compute?

The book's own method: it states an algorithm, proves it correct with a loop
invariant or an exchange or a cut argument, and bounds its running time by
counting — comparisons, recursive calls, nodes visited, pivots, relaxations,
splits — and solving the recurrence or summation the count obeys. The reader
of this Subject does exactly that, on an instance written for the lesson:

1. **Run and count.** The lab executes the algorithm on the lesson's instance
   (or the reader's) and prints the counts the chapter analyses, beside the
   bound the chapter proves.
2. **Check the invariant.** Where the chapter's proof is a loop invariant or a
   structural property (heap order, red-black properties, B-tree occupancy, the
   residual network), the lab checks the property at each step and says where
   it holds and where it would fail.
3. **Solve the recurrence or the sum.** Where the chapter's analysis is a
   recurrence (Chapter 4, Chapter 7, Chapter 9, Chapter 20, Chapter 27), the
   lab evaluates it exactly at the reader's sizes and sets the closed form or
   the master-method case beside it.

**What the lab never does** is turn a count on one input into a bound. The
material clause (§A) says so, and every lesson closes on the gap: the count is
evidence about this instance; the book's proof is about every instance.

## §A PATH fields (`content/intro_algorithms/__init__.py`)

```
"slug": "intro-algorithms",
"title": "Introduction to Algorithms, Read Along",
"level": "Intermediate → Advanced",
"level_note": "you can program, and you know induction, sums and logarithms",
```

Catalog: `short_title` `"Introduction to Algorithms"`, last in the computing
group (after Enterprise Application Patterns), card note: "Cormen, Leiserson,
Rivest and Stein's textbook, read chapter by chapter, with each algorithm run
and counted in the lab." Course slug prefix `intro-algorithms-`; check-id prefix
`ita`; package `intro_algorithms` → slug `intro-algorithms` needs no
`PACKAGE_OF_SLUG` entry. No `"speech"` key (the math read-out, as on the
Algorithms Subject).

**material** (unique; required by `TestGeneratedPathIsCurrent`):
"every count on this path is produced by running the algorithm in your browser
on the instance a lesson states, and a count on one instance is evidence about
that instance &mdash; the bound the book proves holds for every input, and only
its proof establishes that."

tagline / description: written by course 1's author from the final counts
(`test_the_tagline_and_description_state_the_real_counts`). Tagline names the
book with `<em>`, says each algorithm is run and counted, and ends "Eight
courses and N lessons are available."

## §B The eight courses

| # | slug | title | Part, chapters | lessons | module dir |
|---|---|---|---|---|---|
| 1 | `intro-algorithms-foundations` | Foundations | I, 1–5 | 8 | `c1_foundations` |
| 2 | `intro-algorithms-sorting` | Sorting and Order Statistics | II, 6–9 | 7 | `c2_sorting` |
| 3 | `intro-algorithms-data-structures` | Data Structures | III, 10–14 | 8 | `c3_data_structures` |
| 4 | `intro-algorithms-design-techniques` | Advanced Design and Analysis Techniques | IV, 15–17 | 9 | `c4_design_techniques` |
| 5 | `intro-algorithms-advanced-structures` | Advanced Data Structures | V, 18–21 | 5 | `c5_advanced_structures` |
| 6 | `intro-algorithms-graphs` | Graph Algorithms | VI, 22–26 | 9 | `c6_graphs` |
| 7 | `intro-algorithms-algebraic-topics` | Parallel, Matrix, Linear and Number Algorithms | VII, 27–31 | 7 | `c7_algebraic_topics` |
| 8 | `intro-algorithms-strings-geometry-hardness` | Strings, Geometry and Hardness | VII, 32–35 | 8 | `c8_strings_geometry_hardness` |

61 lessons. Part VII is split in two because it holds nine chapters. Part VIII
(Appendices A–D, mathematical background) is not a course; lessons point to
the appendix where they lean on it (§G).

Modules (the `module` field) are the book's chapter titles, e.g.
`"Chapter 6 · Heapsort"`.

## §C Every lesson

Format: slug — Title — sections (printed pages) — lab `kit/mode` — focus.
Printed page p is PDF page p + 21 in the operator's copy. The **matching
Algorithms lesson** (where one exists) is the shape reference for configuring
the lab: read its `lab` cfg in `content/algorithms/` and write new presets.
Instances are the lesson's own, never the book's figures' arrays or graphs.

### Course 1 — Foundations (Part I)
1. `algorithms-as-a-technology` — Algorithms as a Technology — 1.1–1.2 (5–14) — `itakit/growth` — what an algorithm and an instance are; the two-computers comparison of an n² and an n lg n sort as arithmetic: at what n does the slower machine running the better algorithm win.
2. `insertion-sort-and-loop-invariants` — Insertion Sort and Loop Invariants — 2.1 (16–22) — `itakit/sorting` view `insertion` — the invariant's three parts (initialisation, maintenance, termination) checked pass by pass.
3. `analyzing-insertion-sort` — Analyzing Insertion Sort — 2.2 (23–29) — `itakit/sorting` view `cost` — the RAM model, the line-cost sum with t_j, best and worst case, order of growth.
4. `merge-sort-and-divide-and-conquer` — Merge Sort and Divide-and-Conquer — 2.3 (29–42) — `itakit/sorting` view `merge` — divide, conquer, combine; merge comparisons per level; T(n)=2T(n/2)+Θ(n) by the recursion tree.
5. `asymptotic-notation` — Asymptotic Notation — 3.1–3.2 (43–64) — `itakit/growth` view `bounds` — Θ, O, Ω, o, ω as statements with witnesses c and n₀; checking a claimed witness; standard functions (lg, lg*, factorial, Fibonacci) compared.
6. `the-maximum-subarray-problem-and-strassen` — The Maximum-Subarray Problem and Strassen's Method — 4.1–4.2 (68–83) — `itakit/maxsub` — brute force vs divide-and-conquer counts; Strassen's 7 vs 8 multiplications as the recurrence T(n)=7T(n/2)+Θ(n²).
7. `solving-recurrences` — Solving Recurrences — 4.3–4.5 (83–97) — `itakit/recurrence` — substitution, recursion tree, master method: the exact T(n) at powers of b beside n^(log_b a) and f(n); which case, and the gap the master method leaves.
8. `the-hiring-problem-and-randomized-algorithms` — The Hiring Problem and Randomized Algorithms — 5.1–5.3 (114–130; 5.4 named) — `itakit/hiring` — hires on an order; expected hires H_n by indicator random variables, checked by averaging over every permutation at small n; randomizing the input.

### Course 2 — Sorting and Order Statistics (Part II)
1. `heaps` — Heaps and Building a Heap — 6.1–6.3 (151–159) — `heap/build` (match: building-a-heap-in-linear-time) — the heap property, MAX-HEAPIFY's sift-down, BUILD-MAX-HEAP's linear bound by the sum over heights.
2. `heapsort-and-priority-queues` — Heapsort and Priority Queues — 6.4–6.5 (159–169) — `heap/heapsort` (match: heapsort) — the sort as n − 1 extractions; the priority-queue operations and their costs.
3. `quicksort` — Quicksort and Partitioning — 7.1–7.2 (170–179) — `sortkit/partition` or `sortkit/quick` (match: partitioning, quicksort-and-its-worst-case) — the partition loop invariant; worst, best and balanced splits.
4. `analysis-of-randomized-quicksort` — Randomized Quicksort and Its Analysis — 7.3–7.4 (179–190) — `sortkit/expected` (match: randomised-quicksort) — expected comparisons by the indicator X_ij and the probability 2/(j−i+1).
5. `lower-bounds-and-counting-sort` — The Sorting Lower Bound and Counting Sort — 8.1–8.2 (191–197) — `sortkit/counting` (match: counting-sort) — the decision-tree argument, ⌈lg n!⌉, and a sort that is not a comparison sort; stability.
6. `radix-sort-and-bucket-sort` — Radix Sort and Bucket Sort — 8.3–8.4 (197–212) — `sortkit/radix` (match: radix-sort) — digit-by-digit with a stable sort; bucket sort's average-case argument, named.
7. `medians-and-order-statistics` — Medians and Order Statistics — 9.1–9.3 (213–227) — `sortkit/select` or `sortkit/mom` (match: quickselect, median-of-medians) — min and max together in 3⌊n/2⌋ comparisons; randomized select's expected linear time; the groups-of-five guarantee.

### Course 3 — Data Structures (Part III)
1. `stacks-queues-and-linked-lists` — Stacks, Queues and Linked Lists — 10.1–10.4 (232–252) — `seqkit/arraylist` or `seqkit/twostack` — the dynamic-set operations and their cost in each representation; sentinels; rooted-tree representations named.
2. `hash-tables` — Direct Addressing and Hashing with Chaining — 11.1–11.2 (254–262) — `hash/chaining` (match: hashing-with-chaining) — load factor α, Θ(1 + α) under simple uniform hashing.
3. `hash-functions` — Hash Functions and Universal Hashing — 11.3 (262–269) — `hash/universal` (match: universal-hashing) — division and multiplication methods; a universal family and the collision bound.
4. `open-addressing` — Open Addressing — 11.4–11.5 (269–285) — `hash/probing` (match: open-addressing-and-linear-probing) — probe sequences; 1/(1 − α) expected probes; perfect hashing named.
5. `binary-search-trees` — Binary Search Trees — 12.1–12.4 (286–307) — `tree/bst` (match: binary-search-trees) — the BST property, walks, search/min/successor, insert and delete by transplant; height of randomly built trees named with `tree/orders` as an alternative.
6. `red-black-trees` — Red-Black Trees and Rotations — 13.1–13.2 (308–315) — `itakit/rbtree` view `check` — the five properties, black-height, height ≤ 2 lg(n + 1); rotations preserve the BST property.
7. `red-black-insertion-and-deletion` — Red-Black Insertion and Deletion — 13.3–13.4 (315–338) — `itakit/rbtree` view `insert` — the fix-up cases, counted: recolorings and at most two rotations per insertion.
8. `augmenting-data-structures` — Augmenting Data Structures — 14.1–14.3 (339–355) — `tree/augment` (match: augmenting-a-tree) — order-statistic trees, the four-step method, interval trees named.

### Course 4 — Advanced Design and Analysis Techniques (Part IV)
1. `rod-cutting` — Rod Cutting and Dynamic Programming — 15.1 (360–370) — `itakit/rod` — naive recursion's 2^(n−1) calls vs memoized and bottom-up n²/2; reconstructing the cuts.
2. `matrix-chain-multiplication` — Matrix-Chain Multiplication — 15.2 (370–378) — `dpkit/chain` (match: the-fill-order-is-part-of-the-algorithm) — the m and s tables, the Catalan count of parenthesizations.
3. `elements-of-dynamic-programming` — Elements of Dynamic Programming — 15.3 (378–390) — `dpkit/memo` (match: overlapping-subproblems-and-the-memo) — optimal substructure, overlapping subproblems, the subproblem graph; why the longest simple path lacks optimal substructure.
4. `longest-common-subsequence` — Longest Common Subsequence — 15.4 (390–397) — `itakit/lcs` — the c and b tables, the three cases, reconstruction.
5. `optimal-binary-search-trees` — Optimal Binary Search Trees — 15.5 (397–413) — `itakit/obst` — expected search cost with key and dummy probabilities; the e, w and root tables.
6. `activity-selection-and-the-greedy-strategy` — Activity Selection and the Greedy Strategy — 16.1–16.2 (415–428) — `greedy/intervals` (match: greedy-rules-and-the-optimum) — the greedy choice property and why earliest finish is safe.
7. `huffman-codes` — Huffman Codes — 16.3 (428–437) — `greedy/huffman` (match: huffman-codes) — prefix codes, cost B(T), the merge order.
8. `matroids-and-greedy-methods` — Matroids and Greedy Methods — 16.4–16.5 (437–450) — `greedy/matroid` (match: independence-systems-and-matroids) — heredity and exchange; unit-task scheduling with deadlines as a matroid.
9. `amortized-analysis` — Amortized Analysis and Dynamic Tables — 17.1–17.4 (451–480) — `itakit/amortized` — aggregate, accounting and potential methods on the binary counter and the multipop stack; table expansion and contraction with Φ.

### Course 5 — Advanced Data Structures (Part V)
1. `b-trees` — B-Trees — 18.1–18.3 (484–504) — `itakit/btree` — minimum degree t, height ≤ log_t((n + 1)/2), splits on the way down, disk accesses.
2. `fibonacci-heaps` — Fibonacci Heaps — 19.1–19.2 (505–518) — `itakit/fibheap` view `ops` — the root list, potential t(H) + 2m(H), lazy insert and union, consolidation in EXTRACT-MIN.
3. `decrease-key-and-the-degree-bound` — Decreasing a Key and Bounding the Degree — 19.3–19.4 (518–530) — `itakit/fibheap` view `cascade` — cuts and cascading cuts, marks; size ≥ F_(k+2) ≥ φ^k.
4. `van-emde-boas-trees` — van Emde Boas Trees — 20.1–20.3 (531–560) — `itakit/veb` — high/low/index, clusters and summary, T(u) = T(√u) + O(1) = O(lg lg u), calls counted.
5. `disjoint-sets` — Disjoint Sets — 21.1–21.4 (561–585) — `seqkit/unionfind` (match: union-find) — linked lists with weighted union; forests with union by rank and path compression; α(n) named.

### Course 6 — Graph Algorithms (Part VI)
1. `breadth-first-search` — Graph Representations and Breadth-First Search — 22.1–22.2 (589–602) — `itakit/bfs` — adjacency lists vs matrix; BFS distances, the breadth-first tree, O(V + E).
2. `depth-first-search` — Depth-First Search — 22.3 (603–612) — `graphkit/dfstimes` (match: depth-first-search-and-the-timestamps) — discovery and finish times, the parenthesis theorem, edge classification.
3. `topological-sort-and-strong-components` — Topological Sort and Strongly Connected Components — 22.4–22.5 (612–623) — `graphkit/topo` or `graphkit/scc` — sort by decreasing finish time; the transpose-graph algorithm.
4. `minimum-spanning-trees` — Minimum Spanning Trees: Kruskal and Prim — 23.1–23.2 (624–642) — `graphkit/cutproperty` or `graphkit/kruskal` — the generic method, safe edges and the cut theorem; the two algorithms.
5. `bellman-ford-and-dag-shortest-paths` — Bellman-Ford and Shortest Paths in DAGs — 24.1–24.2 (643–658) — `graphkit/bellmanford` (match: negative-weights-and-bellman-ford) — relaxation, |V| − 1 passes, negative-cycle detection; DAG shortest paths in topological order.
6. `dijkstra-and-difference-constraints` — Dijkstra's Algorithm and Difference Constraints — 24.3–24.5 (658–683) — `graphkit/relax` (match: relaxation-and-dijkstras-schedule) — the greedy schedule and why nonnegative weights are needed; difference constraints as a graph, named.
7. `all-pairs-shortest-paths` — All-Pairs Shortest Paths — 25.1–25.3 (684–707) — `graphkit/floyd` — the matrix-multiplication view, Floyd-Warshall's d^(k), Johnson's reweighting named.
8. `maximum-flow` — Flow Networks and Ford-Fulkerson — 26.1–26.2 (708–732) — `flowkit/augment` or `flowkit/mincut` — residual networks, augmenting paths, max-flow min-cut; Edmonds-Karp's BFS.
9. `maximum-bipartite-matching` — Maximum Bipartite Matching — 26.3 (732–736; 26.4–26.5 named) — `flowkit/matching` (match: bipartite-matching) — matching as unit-capacity flow; push-relabel named.

### Course 7 — Parallel, Matrix, Linear and Number Algorithms (Part VII, 27–31)
1. `multithreaded-algorithms` — Multithreaded Algorithms — 27.1–27.3 (772–812) — `itakit/workspan` — spawn/sync DAGs, work T₁, span T∞, parallelism, the greedy-scheduler bound T_P ≤ T₁/P + T∞; P-FIB and multithreaded merge sort as recurrences.
2. `solving-linear-systems` — Solving Systems of Linear Equations — 28.1–28.3 (813–842) — `itakit/lup` — LU and LUP decomposition by elimination with pivoting, forward and back substitution, exact fractions.
3. `linear-programming-and-the-simplex-algorithm` — Linear Programming and the Simplex Algorithm — 29.1–29.3 (843–879) — `simplex/pivot` or `simplex/walk` — standard and slack forms; a pivot; the walk to the optimum.
4. `duality-and-the-initial-solution` — Duality and the Initial Basic Feasible Solution — 29.4–29.5 (879–897) — `duality/certificate` and/or `simplex/phase1` — the dual, weak duality, the auxiliary program L_aux.
5. `polynomials-and-the-fft` — Polynomials and the FFT — 30.1–30.3 (898–925) — `itakit/fft` — coefficient vs point-value, the DFT at complex roots of unity, the butterfly recursion, n lg n vs n² multiplications.
6. `number-theoretic-algorithms` — GCD and Modular Arithmetic — 31.1–31.6 (926–958) — `number/bezout` or `number/modexp` — Euclid's step count, extended Euclid, modular linear equations, the CRT, repeated squaring.
7. `rsa-and-primality-testing` — RSA and Primality Testing — 31.7–31.8 (958–975; 31.9 named) — `random/witness` (match: witnesses-liars-and-one-sided-error) or `number/modexp` — RSA's key setup as arithmetic; Miller-Rabin's witnesses and the error bound.

### Course 8 — Strings, Geometry and Hardness (Part VII, 32–35)
1. `naive-and-rabin-karp-matching` — Naive and Rabin-Karp String Matching — 32.1–32.2 (985–995) — `strings/rabin` or `strings/naive` — valid shifts, (n − m + 1)m comparisons, the rolling hash and spurious hits.
2. `automata-and-knuth-morris-pratt` — Finite Automata and Knuth-Morris-Pratt — 32.3–32.4 (995–1013) — `strings/kmp` or `strings/automaton` — the transition function, the prefix function π and its amortized linear bound.
3. `line-segment-properties` — Line-Segment Properties and Intersection — 33.1–33.2 (1015–1029) — `geometry/segments` or `geometry/sweep` — cross products, orientation, the any-segments-intersect sweep.
4. `convex-hull-and-closest-pair` — Convex Hull and the Closest Pair — 33.3–33.4 (1029–1047) — `geometry/hull` or `geometry/closest` — Graham's scan and Jarvis's march; the divide-and-conquer closest pair and the strip.
5. `polynomial-time-and-verification` — Polynomial Time and Verification — 34.1–34.2 (1053–1067) — `reduction/selfreduce` (match: decision-search-and-the-certificate) — abstract problems, encodings, P, certificates and NP.
6. `np-completeness-and-reductions` — NP-Completeness and Reducibility — 34.3–34.5 (1067–1105) — `reduction/independentset` or `reduction/subsetsum` — ≤_P, NP-hard and NP-complete, the chain from CIRCUIT-SAT; one reduction built.
7. `vertex-cover-and-tsp-approximation` — Approximating Vertex Cover and TSP — 35.1–35.2 (1106–1117) — `coping/vertexcover` or `coping/tsp` — approximation ratio; the matching-based 2-approximation; the MST tour under the triangle inequality.
8. `set-cover-randomization-and-subset-sum` — Set Cover, Randomization and Subset Sum — 35.3–35.5 (1117–1139) — `coping/setcover` or `coping/fptas` (or `random/max3sat`) — greedy set cover's H(max |S|) ratio; MAX-3-CNF's 8/7; the trimming FPTAS.

## §D The new kit: `itakit`

Built on `eakit_core` exactly as `eakit` is (import it as `ea`; one pure JS
`<xx>Compute(view, inst, opts)` per mode returning `{tiles, status, table}` or
`{refuse}`; a Python `check` per view mirroring every JS refusal; presets with
`expect`; listed in `build_paths.KITS_WITH_EXPECTATIONS`; mathcheck cases in
`scripts/mathcheck.js`, each seen to fail when its function is broken). Two
modules: `itakit.py` (entry point + modes of family A) and `itakit_b.py`
(family B). Report for authors: `docs/intro-algorithms/kit-report.md`, same
shape as `docs/enterprise-patterns/kit-report.md`.

All arithmetic exact (BigInt rationals via `RATIONAL_JS`); where a mode must
use floating point (FFT's complex roots) it says so in its rules and prints
values rounded to a stated number of places, and the rounding is checked
against an exact route where one exists (FFT products of integer
polynomials are integers: round and compare with the schoolbook product).

**Family A (`itakit.py`)**: numeric and analytic.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `growth` (gr) | `race`, `bounds` | race: two cost formulas from a small fixed menu (c·n², c·n·lg n, c·n, c·2ⁿ, c·n³, c·lg n) with constants and machine speeds; bounds: f, g from the menu, claimed c and n₀, relation (O/Ω/Θ) | crossover n, time each at given n; whether the witness holds at every n in [n₀, n₀ + 10⁴] and the first n where it fails |
| `sorting` (st) | `insertion`, `cost`, `merge` | an integer array (≤ 40) | insertion: per pass the sorted prefix, shifts, comparisons, invariant holds; cost: t_j list, total comparisons and shifts, best n − 1 and worst n(n − 1)/2 beside; merge: comparisons per level, levels ⌈lg n⌉, total ≤ n⌈lg n⌉ − 2^⌈lg n⌉ + 1 |
| `recurrence` (rc) | `master`, `tree` | a, b, f(n) as c·n^k·lg^p n (k, p small rationals/integers), base T(1) | exact T(n) at n = b^j for j up to a cap, n^(log_b a), the case (1/2/3 or "falls in the gap"), level sums of the recursion tree, ratio T(n)/predicted |
| `maxsub` (ms) | `compare` | integer array (≤ 60) | max subarray (l, r, sum) by three routes (brute force pairs, divide-and-conquer, linear scan) with step counts each |
| `hiring` (hr) | `order` | a ranking order (permutation ≤ 9, or ≤ 40 for one run) | hires on that order, exact average over all n! orders (n ≤ 8) = H_n as fraction, cost c_i·n + c_h·hires |
| `workspan` (ws) | `dag`, `recurrence` | dag: strands with costs and edges (spawn/sync DAG ≤ 40 strands); recurrence: P-FIB n or merge-sort n | work, span, parallelism, greedy bound for given P, critical path |
| `lup` (lu) | `decompose` | square matrix ≤ 5×5 of integers/fractions, optional b | L, U, P (permutation), pivots, solution x, exact; refuse singular |
| `fft` (ft) | `multiply` | two integer coefficient lists, length ≤ 16 | n (padded power of 2), schoolbook product and multiplication count, FFT product (rounded) and butterfly count, agree yes/no |

**Family B (`itakit_b.py`)**: structures and tables.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `rod` (rd) | `cut` | price list p₁..p_n (n ≤ 20; naive route capped at n ≤ 20 by count not run) | r_n, the cuts, naive call count 2ⁿ, memo calls, bottom-up inner iterations n(n+1)/2 |
| `lcs` (lc) | `table` | two strings ≤ 30 | LCS length, one LCS, cells filled m·n, table printed when small |
| `obst` (ob) | `table` | key probabilities p₁..p_n and dummy q₀..q_n as fractions or decimals summing to 1 (n ≤ 8) | expected cost e[1,n], root table, the tree (as nested text), cost checked by brute force over all trees at n ≤ 7 |
| `amortized` (am) | `counter`, `stack`, `table` | counter: k bits, n increments; stack: op list push/pop/multipop k; table: insert/delete sequence with expansion ×2 at full, contraction at ¼ | actual costs, total, aggregate bound, credit balance (accounting), Φ before/after and amortized cost per op (potential), max amortized |
| `rbtree` (rb) | `check`, `insert` | check: a tree in a parenthesized text form with colors; insert: key sequence (≤ 31) | properties 1–5 each holds/fails with the first violating node, black-height, height, 2lg(n+1); insert: per key the fix-up case sequence, recolorings, rotations, final tree |
| `btree` (bt) | `insert` | t (2..5), key sequence (≤ 60) | height, nodes, splits, disk reads/writes counted per CLRS's B-TREE-INSERT, bound log_t((n+1)/2), final tree by level |
| `fibheap` (fh) | `ops`, `cascade` | op list: insert k, min, extract, decrease k→v, delete k | per op: actual cost, t(H), m(H), Φ, amortized cost; root list; max degree vs ⌊log_φ n⌋ |
| `veb` (vb) | `ops` | u = 2^(2^k) (k ≤ 4), ops member/insert/successor/delete | per op recursive calls in proto-vEB and vEB, lg lg u, final members, summary/cluster contents at top level |
| `bfs` (bf) | `search` | undirected or directed edge list (≤ 30 vertices), source | distances, parents (breadth-first tree), vertices by layer, enqueue count V and edge examinations (2E or E), unreachable list |

**Never**: quote a complexity class as a measured figure; carry a book figure
as a constant (every input arrives in a preset); run typed text as script.

## §E Package, text, quoting

Package `content/intro_algorithms/`, one directory per course (§B), each with
`__init__.py` (COURSE dict, same fields as `content/code_complete/c2_high_quality_code/__init__.py`)
and `part_a.py` (and `part_b.py` past five lessons). Spoken forms in
`content/spoken/intro_algorithms.py`, one block per course.

**The text** is the operator's copy, extracted privately outside the
repository (see `docs/intro-algorithms/AUTHORING.md`). The book is in
copyright: never copy any stretch of it into the repository, the project files
or a report.

**Quoting** (as Code Complete §E.3): one opening quotation of at most 40 words,
at most 60 words of quotation per lesson, character for character, with a
`# printed p. N` comment beside the dict. Never reproduce the book's
pseudocode, figures, tables, worked examples' data or exercises; describe an
algorithm in prose steps of your own and point to the procedure by its book
name (e.g. MAX-HEAPIFY, PARTITION, RB-INSERT-FIXUP) and section. Cite by
chapter and section in prose, never by page. Exercises may be pointed to by
number ("Exercise 6.3-3") but not restated.

**Overlap scan**: no run of 8+ consecutive words shared with the book except
titles, procedure names, counted quotations and standard mathematical phrases
("if and only if", a theorem's formula). The scanner is in AUTHORING.md.

## §F Voice

The read-along for a working programmer working through the book. Each lesson:
which sections, what they set out to show, the argument in the lesson's own
words (the invariant, the recurrence, the exchange), then the lab on an
instance written for the lesson, a worked example by hand, and a quiz whose
distractors are each arguable-for and wrong. Credit the book's authors as
"the authors" or "CLRS" (the common name) — not to one author. Where the
Algorithms Subject has a lesson on the same algorithm, name it once by title.
Notation is the book's: lg for log₂, Θ/O/Ω, A[1..n] one-based, T(n).

## §G What is left out, and why

- Part VIII (Appendices A–D): mathematical background; lessons point to it.
- Starred sections are named, and read where §C lists them; their full proofs
  (4.6, 5.4's streaks, 11.5, 12.4's proof, 21.4, 26.4–26.5, 31.9) are left to
  the book.
- The book's pseudocode, figures, tables and exercises (copyright, §E).
- Chapter notes and problems at chapter ends: named, not restated.
