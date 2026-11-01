"""Graph Algorithms, lessons 6-9 -- Chapters 24 (continued), 25 and 26.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT
Press, 2009): Sections 24.3-24.5 (pp. 658-683), Chapter 25, All-Pairs
Shortest Paths (pp. 684-707), and Chapter 26, Maximum Flow, Sections
26.1-26.3 (pp. 708-736). Every quotation is copied from the operator's copy
with its printed page in the comment beside the lesson. The graphs are written
for these lessons; none of the book's figures is reproduced. As in part_a,
each graph is one constant in the lab's notation, and every figure the prose
quotes for it was read off the lab with that graph typed in.
"""

# ---------------------------------------------------------------- graphs

# Dijkstra's Algorithm: five vertices, seven undirected edges (the relax lab
# reads edges, not arcs).
DIJKSTRA_GRAPH = "1-2 4, 1-3 1, 2-3 2, 2-4 5, 3-4 8, 4-5 3, 3-5 9"

# All-Pairs Shortest Paths: four vertices, six arcs, one negative, no negative
# cycle.
APSP_GRAPH = "1>2 3, 2>3 4, 3>1 -2, 1>4 7, 4>3 1, 2>4 2"

# Flow Networks and Ford-Fulkerson: source 1, sink 5.
FLOW_GRAPH = "1>2 2, 1>3 1, 2>3 2, 2>4 1, 3>4 2, 4>5 3"

# Maximum Bipartite Matching: four on each side, seven allowed pairs.
MATCH_PAIRS = "1-1, 1-2, 2-1, 3-2, 3-3, 4-3, 4-4"


LESSONS = [
    # ---------------------------------------------------------------- 06
    # CLRS Sections 24.3-24.5, pp. 658-683.
    # Quote: p. 658, 22 words, quotes.py OK. Lesson total: 22 words.
    # DIJKSTRA, S and Q, nonnegative weights (p. 658); Theorem 24.6 and its
    # invariant, Corollary 24.7 (pp. 659-661); array O(V^2), binary heap
    # O((V + E) lg V), Fibonacci heap O(V lg V + E), likeness to BFS and Prim
    # (pp. 661-662); difference constraints, constraint graph, Lemma 24.8,
    # Theorem 24.9, Bellman-Ford on n + 1 vertices (pp. 664-669); Section 24.5
    # properties, Lemmas 24.10-24.17 (pp. 671-676).
    {
        "slug": "dijkstra-and-difference-constraints",
        "title": "Dijkstra's Algorithm and Difference Constraints",
        "module": "Chapter 24 · Single-Source Shortest Paths",
        "one_line": "With no negative weights, settle the nearest unsettled vertex and relax its edges, and each arc is relaxed once; a system of difference constraints is a shortest-path problem in disguise.",
        "summary": (
            "Section 24.3 relaxes each arc exactly once, in the order its tail is settled, and "
            "proves the order right when no weight is negative; Section 24.4 turns a system of "
            "inequalities into a graph that Bellman-Ford can solve; Section 24.5 proves the "
            "relaxation properties the chapter has used. Run Dijkstra's algorithm on a "
            "five-vertex graph under three schedules, and break it by hand with one negative "
            "arc."
        ),
        "key": [
            "settle the least d, then relax its arcs",
            "settled means final: d = δ(s, u)",
            "needs every weight nonnegative",
            "array O(V²); binary heap O(E lg V)",
            "Fibonacci heap: O(V lg V + E)",
            "x_j − x_i ≤ b: an arc from i to j",
        ],
        "key_label": "Sections 24.3 to 24.5 in six lines",
        "concepts_intro": (
            "Three ideas: a set that only grows, the condition that keeps it right, and a "
            "translation from inequalities to arcs."
        ),
        "concepts": [
            ("The settled set S",
             "Dijkstra's algorithm keeps a set S of vertices whose estimate already equals the "
             "true distance. Each step moves the unsettled vertex of least estimate into S and "
             "relaxes the arcs leaving it. A min-priority queue holds the unsettled vertices, "
             "keyed by estimate."),
            ("Why nonnegative weights matter",
             "The proof that a vertex is final when it is settled argues that any other route "
             "to it must leave S somewhere and can only get longer from there. A negative arc "
             "later on the route could make it shorter, and the argument fails."),
            ("A constraint graph",
             "A system of inequalities each of the form x_j − x_i ≤ b becomes a graph with one "
             "vertex per variable, an arc from i to j of weight b per inequality, and an extra "
             "vertex with a 0-weight arc to every other. Shortest distances from the extra "
             "vertex solve the system, or a negative cycle proves it has no solution."),
        ],
        "read_title": "The sections' argument first, then the schedules",
        "read_intro": (
            "Read Sections 24.3 to 24.5 in your own copy first. The lesson sets out the "
            "argument in its own words, then runs Dijkstra's algorithm on a graph written for "
            "the lesson and solves a small system of constraints by hand."
        ),
        "body": [
            ("p", "&ldquo;As we shall see, with a good implementation, the running time of "
                  "Dijkstra&rsquo;s algorithm is lower than that of the Bellman-Ford "
                  "algorithm.&rdquo; Section 24.3 of CLRS buys that speed with one condition: "
                  "every weight must be nonnegative. Bellman-Ford relaxed every arc in every "
                  "round because it could not know which estimates were final. Dijkstra's "
                  "algorithm always knows one, the smallest estimate not yet settled, and so it "
                  "relaxes each arc once."),
            ("p", "The authors' DIJKSTRA initialises as before, puts every vertex into a "
                  "min-priority queue keyed by its estimate, and repeats: extract the vertex of "
                  "least estimate, add it to the settled set S, and relax every arc leaving it. "
                  "Theorem 24.6 proves that each vertex's estimate equals its true distance at "
                  "the moment it is extracted. The proof takes the first vertex `u` for which that "
                  "fails and a shortest path to it. The path leaves S at some arc into a vertex "
                  "`y`, which already has its true distance by convergence; with no negative "
                  "weights the rest of the path cannot be negative, so δ(s, y) ≤ δ(s, u) ≤ u.d; "
                  "and `u` was extracted ahead of `y`, so u.d ≤ y.d = δ(s, y). The chain closes, "
                  "and u.d = δ(s, u) after all. "
                  "Corollary 24.7 adds that the predecessors form a shortest-paths tree."),
            ("p", "The running time depends on the queue. There are |V| extractions and at most "
                  "|E| decreases of a key. With a plain array indexed by vertex, a decrease "
                  "is O(1) and an extraction scans all V entries: O(V²). With a binary heap "
                  "both cost O(lg V): O((V + E) lg V), better when the graph is sparse. With a "
                  "Fibonacci heap a decrease is O(1) amortized: O(V lg V + E), and the authors "
                  "note that Dijkstra's many decreases were the motivation for that heap. The "
                  "section ends on a likeness: S plays the part of breadth-first search's black "
                  "vertices, and the queue the part of Prim's."),
            ("p", "Section 24.4 is an application. Linear programming in general is the subject "
                  "of Chapter 29, but when every inequality has the form `x_j − x_i ≤ b`, a "
                  "difference of two variables bounded by a constant, the system is a graph. "
                  "Make a vertex per variable and an arc from `i` to `j` of weight `b` for each "
                  "inequality, then add a vertex `v₀` with an arc of weight 0 to every other. "
                  "Theorem 24.9: if this constraint graph has no negative cycle, the distances "
                  "from `v₀` are a solution; if it has one, the system has none. Bellman-Ford "
                  "solves it, since weights can be negative. Lemma 24.8 adds that a solution "
                  "plus any constant is another solution."),
            ("p", "Section 24.5 proves what the chapter has been using: the triangle inequality "
                  "for distances, the upper-bound property, the no-path property, convergence, "
                  "path relaxation and the predecessor-subgraph property, each a lemma about "
                  "any sequence of relaxations after initialisation. Read the proofs in the "
                  "book; this lesson uses the statements."),
            ("p", "The lab works on undirected edges, each relaxed from whichever end is settled, "
                  "and runs three schedules: nearest unsettled first from a heap (Dijkstra's), "
                  "nearest unsettled first by scanning every vertex (the array version), and "
                  "every edge in typed order, over and over (Bellman-Ford's). After every step it "
                  "checks the upper-bound property against distances computed another way. Its "
                  "heap pushes a second entry when a label improves instead of decreasing a key "
                  "in place, so its counts are pushes and pops, and stale entries are skipped. It "
                  "opens on its preset <code>stale</code>, built to fill the heap with stale entries: 12 relaxations, 6 pushes and 6 pops. "
                  "The preset <code>dense</code>, ten edges on five vertices, makes 20 "
                  "relaxations against a reference E·lg V of 20 (the page rounds lg V down to a "
                  "whole number, here lg 5 to 2); <code>far</code>, a chain of "
                  "seven, makes 12 with all 7 labels exact."),
            ("p", "This lesson's graph has five vertices and seven edges: <code>"
                  + DIJKSTRA_GRAPH + "</code>, shortest paths from 1. With the heap the lab "
                  "settles 1 at 0, then 3 at 1, then 2 at 3, then 4 at 8, then 5 at 10. It "
                  "performs 14 relaxations, every edge once from each end, with 7 pushes and 7 "
                  "pops; the reference E·lg V, with lg 5 taken as 2, is 14; the upper-bound "
                  "invariant is never violated; and all 5 labels equal the true distances. The "
                  "paths are 1 → 3 → 2 for vertex 2, 1 → 3 → 2 → 4 for 4 and 1 → 3 → 5 for 5."),
            ("p", "Switch the schedule. Scanning every vertex instead of using a heap gives the "
                  "same 14 relaxations and the same labels, with no heap at all and 30 reads in "
                  "all to find the nearest vertices: the array implementation's trade. Relaxing every "
                  "edge in typed order, over and over, takes 2 rounds and 28 relaxations to "
                  "reach the same labels. The answer is the same three ways; the order decides "
                  "the work. The Algorithms Subject's lesson Relaxation and Dijkstra's Schedule "
                  "runs the same lab."),
            ("p", "The lab's edges point both ways, so it cannot show the directed failure the "
                  "section warns about: an undirected negative edge is already a negative "
                  "cycle, and the lab says so. Do it by hand on the arcs <code>1>2 1, 1>3 4, "
                  "3>2 -4, 2>4 1</code>. Dijkstra settles 1 at 0, then 2 at 1, then 4 at 2, "
                  "then 3 at 4; relaxing `3 → 2` then lowers vertex 2 to 0, but vertex 4 was "
                  "settled at 2 and is never revisited, while its true distance is 1, along "
                  "1 → 3 → 2 → 4. Bellman-Ford, from the lesson before, gets it right."),
            ("p", "Now a system of difference constraints, by hand: `x₂ − x₁ ≤ 3`, `x₃ − x₂ ≤ −1`, "
                  "`x₃ − x₁ ≤ 1` and `x₁ − x₃ ≤ 2`. The arcs are 1 to 2 of weight 3, 2 to 3 of "
                  "weight −1, 1 to 3 of weight 1 and 3 to 1 of weight 2, plus 0-weight arcs from "
                  "`v₀`. Distances from `v₀` are 0 to vertex 1, 0 to vertex 2 and −1 to vertex 3, "
                  "through vertex 2; no cycle is negative. So x = (0, 0, −1), and each inequality "
                  "checks: 0 ≤ 3, −1 ≤ −1, −1 ≤ 1 and 1 ≤ 2."),
            ("h3", "Exercise"),
            ("p", "Take the graph <code>1-2 7, 1-3 2, 2-3 3, 2-4 1, 3-4 6, 3-5 8, 4-5 2</code> "
                  "and run Dijkstra's algorithm from 1 by hand, writing the order of settling "
                  "and every estimate after each step. Type it into the lab and compare the "
                  "heap and scan schedules. Then write the constraint graph for `x₁ − x₂ ≤ 1`, "
                  "`x₂ − x₃ ≤ −2` and `x₃ − x₁ ≤ 0`, and decide whether the system has a "
                  "solution."),
            ("p", "Single-source algorithms run once per source answer every pair, at a price. "
                  "The next lesson, All-Pairs Shortest Paths, reads Chapter 25, which does "
                  "better with a matrix."),
        ],
        "lab": ("graphkit", {
            "mode": "relax",
            "preset": "stale",
            "panel_title": "One relaxation step, three schedules",
            "panel_intro": (
                "Type weighted edges as one-other w and a source, then choose the schedule: "
                "nearest unsettled first from a heap, the same by scanning, or every edge in "
                "order, repeatedly. The upper-bound property is checked after every step. Paste "
                "the lesson's graph from source 1."
            ),
        }),
        "steps_title": "Running Dijkstra's algorithm by hand",
        "steps_intro": "Five steps, the last on a graph of your own.",
        "steps": [
            ("Check the weights",
             "Confirm that no weight is negative. If one is, use Bellman-Ford instead."),
            ("Initialise and settle the source",
             "Set every estimate to infinity and the source's to 0. The source is the first "
             "vertex settled."),
            ("Relax the arcs out of the vertex just settled",
             "For each arc out of it, lower the head's estimate if the route through the "
             "settled vertex is shorter, and record the predecessor."),
            ("Settle the least unsettled estimate, and repeat",
             "Pick the unsettled vertex with the smallest estimate, settle it, and go back to "
             "relaxing. Stop when every reachable vertex is settled."),
            ("Do it on a graph of your own",
             "Write the travel times between six places you know as weighted edges and type "
             "them into the lab. Note the order of settling and compare the relaxations under "
             "the heap and the repeated schedule."),
        ],
        "worked": {
            "title": "The lesson's graph from vertex 1",
            "intro": [
                "Settle the least estimate each time and relax the edges out of it.",
            ],
            "lines": [
                "settle 1 at 0: d[2] = 4, d[3] = 1",
                "settle 3 at 1: d[2] = 3, d[4] = 9",
                "  and d[5] = 10",
                "settle 2 at 3: d[4] = 8",
                "settle 4 at 8: 8 + 3 is not below 10",
                "settle 5 at 10",
                "order 1, 3, 2, 4, 5",
            ],
            "after": [
                "Each vertex's estimate was final the moment it was settled, as Theorem 24.6 "
                "promises for nonnegative weights. Vertex 2 improved once, from 4 to 3, and the "
                "lab's heap shows that improvement as a second push and a stale pop.",
            ],
        },
        "quiz_title": "Settling, failing and constraints",
        "quiz": [
            {"q": "In what order does Dijkstra's algorithm settle the vertices of the lesson's "
                  "graph from vertex 1?",
             "a": ["1, 2, 3, 4, 5", "1, 3, 2, 4, 5", "1, 3, 2, 5, 4", "1, 3, 4, 2, 5"],
             "c": 1,
             "why": "After 1 (0), the least estimate is 3 (1); relaxing from 3 lowers 2 to 3, "
                    "so 2 comes next; then 4 at 8 before 5 at 10. Numeric order ignores the "
                    "estimates, and 5 cannot come before 4 since 10 is more than 8."},
            {"q": "Run the book's DIJKSTRA, whose RELAX does not check whether a vertex is "
                  "settled, on the arcs 1 → 2 of weight 1, 1 → 3 of 4, 3 → 2 of −4 and 2 → 4 of 1, from 1. Which final "
                  "estimate is wrong?",
             "a": ["Vertex 2 ends at 1, but its distance is 0",
                   "Vertex 3 ends at 4, but its distance is 0",
                   "Vertex 4 ends at 2, but its distance is 1",
                   "None: there is no negative cycle, so the answer is right"],
             "c": 2,
             "why": "Vertex 4 is settled at 2 before 3 is reached; relaxing `3 → 2` then lowers "
                    "vertex 2 to 0, but nothing relaxes `2 → 4` again, so 4 keeps 2 while "
                    "1 → 3 → 2 → 4 costs 1. Vertex 2 does end at 0, because this RELAX updates "
                    "it, and 3's distance is 4. No negative cycle is not enough: Dijkstra needs "
                    "no negative weight."},
            {"q": "For the system `x₂ − x₁ ≤ 3`, `x₃ − x₂ ≤ −1`, `x₃ − x₁ ≤ 1`, `x₁ − x₃ ≤ 2`, "
                  "which solution do the distances from `v₀` in the constraint graph give?",
             "a": ["(0, 0, 0)", "(0, 0, −1)", "(1, 1, 0)", "(0, 3, 2)"],
             "c": 1,
             "why": "Every vertex starts at distance at most 0 through its arc from `v₀`, and "
                    "vertex 3 reaches −1 through vertex 2. (1, 1, 0) also satisfies the system, "
                    "being (0, 0, −1) plus 1 as Lemma 24.8 allows, but distances from `v₀` "
                    "cannot exceed 0. (0, 0, 0) breaks `x₃ − x₂ ≤ −1`, and (0, 3, 2) breaks "
                    "`x₃ − x₁ ≤ 1`."},
            {"q": "On a dense graph, with E close to V², which implementation of Dijkstra's "
                  "queue does the section's analysis favour?",
             "a": ["A binary heap, since O(E lg V) is the better bound",
                   "A plain array, since O(V²) beats O(V² lg V)",
                   "Either: the two bounds are equal on a dense graph",
                   "Neither: dense graphs need Bellman-Ford"],
             "c": 1,
             "why": "With E near V², the binary heap's O((V + E) lg V) is O(V² lg V), while the "
                    "array's O(V²) does not grow with E. The heap wins only when "
                    "E = o(V²/lg V). Density says nothing about negative weights, so "
                    "Bellman-Ford is not needed."},
        ],
        "mistakes": [
            ("Thinking Dijkstra's algorithm works whenever there is no negative cycle",
             "No negative cycle is Bellman-Ford's condition. Dijkstra's proof needs every "
             "weight nonnegative, because it assumes a route can only get longer after it "
             "leaves the settled set. On the lesson's four arcs with one weight of −4, it "
             "settles vertex 4 at 2 and never revisits it, though 1 → 3 → 2 → 4 costs 1."),
            ("Crediting the heap with the algorithm's correctness",
             "The heap only finds the least estimate quickly. Correctness comes from settling "
             "in order of least estimate with nonnegative weights. On the lesson's graph the "
             "lab's scanning schedule, with no heap, settles the same vertices in the same "
             "order and reaches the same five labels; it pays 30 reads instead."),
            ("Expecting a system of difference constraints to have one solution",
             "Lemma 24.8: add the same constant to every variable of a solution and the "
             "differences do not change, so it is still a solution. The lesson's system is "
             "solved by (0, 0, −1) and equally by (1, 1, 0). The constraint graph returns the "
             "one whose largest value is 0."),
        ],
        "standard": (
            "Finish when you can run Dijkstra's algorithm by hand and know when it fails.",
            "For a nonnegatively weighted graph of five or six vertices, give the order of "
            "settling and the final estimates; construct a small directed example where a "
            "negative arc makes it wrong; and solve a system of three difference constraints."
        ),
        "note": (
            "The lab reads undirected edges and keeps a heap with repeated entries rather than "
            "a decrease-key, so its pushes differ from the book's operation count; it cannot "
            "show a directed negative arc fooling the algorithm, which the lesson does by hand. "
            "That settling is final on every nonnegative graph is Theorem 24.6, not a run."
        ),
    },
    # ---------------------------------------------------------------- 07
    # CLRS Chapter 25, Sections 25.1-25.3, pp. 684-707.
    # Quote: p. 684, 19 words, quotes.py OK. Lesson total: 19 words.
    # Running Dijkstra or Bellman-Ford |V| times (p. 684); outline, Theta(V^3
    # lg V), Theta(V^3), Johnson O(V^2 lg V + VE) (p. 686); l_ij^(m) and the
    # extension as matrix multiplication, Theta(n^4), repeated squaring
    # (pp. 686-691); d_ij^(k), FLOYD-WARSHALL, Theta(n^3), predecessor matrix,
    # transitive closure (pp. 693-699); Lemma 25.1, reweighting with h from
    # Bellman-Ford on G', Dijkstra from each vertex (pp. 700-704).
    {
        "slug": "all-pairs-shortest-paths",
        "title": "All-Pairs Shortest Paths",
        "module": "Chapter 25 · All-Pairs Shortest Paths",
        "one_line": "Fill a matrix of distances by allowing one more edge, or one more interior vertex, at a time; or reweight the arcs so that Dijkstra can run from every vertex.",
        "summary": (
            "Chapter 25 answers the shortest-path question for every pair at once. Section "
            "25.1 lets paths grow one edge at a time and finds matrix multiplication inside; "
            "Section 25.2's Floyd-Warshall algorithm lets in one interior vertex at a time in "
            "Θ(V³); Section 25.3's Johnson reweights so that Dijkstra can run from every "
            "vertex. Watch Floyd-Warshall's matrix change on a four-vertex graph with a "
            "negative arc, and reweight it by hand."
        ),
        "key": [
            "L(m): best paths of at most m edges",
            "min-plus product extends L by one edge",
            "repeated squaring: Θ(V³ lg V)",
            "D(k): interior vertices among 1 to k",
            "Floyd-Warshall: k outermost, Θ(V³)",
            "negative diagonal: a negative cycle",
            "Johnson: w + h(u) − h(v), then Dijkstra",
        ],
        "key_label": "Chapter 25 in seven lines",
        "concepts_intro": (
            "Three ways to cut the same problem into subproblems, each giving one of the "
            "chapter's algorithms."
        ),
        "concepts": [
            ("Paths of at most m edges",
             "Section 25.1's subproblem: the least weight of a path from i to j using at most m "
             "edges. Going from m − 1 to m means trying every last edge, which is a matrix "
             "product with minimum in place of sum and addition in place of product. With no "
             "negative cycle, m = n − 1 gives the distances."),
            ("Paths through the first k vertices",
             "Floyd-Warshall's subproblem: the least weight of a path from i to j whose "
             "interior vertices all lie among vertices 1 to k. Allowing vertex k either does not "
             "help or splits the path at k into two paths through the first k − 1 vertices."),
            ("Reweighting",
             "Johnson's device: give each vertex a number h(v) and replace each arc's weight w "
             "by w + h(u) − h(v). Every path from u to v changes by the same h(u) − h(v), so "
             "shortest paths stay shortest (Lemma 25.1); with h taken as distances from an "
             "added vertex, every new weight is nonnegative."),
        ],
        "read_title": "The chapter's argument first, then the matrix",
        "read_intro": (
            "Read Sections 25.1 to 25.3 in your own copy first. The lesson sets out each "
            "argument in its own words, then runs Floyd-Warshall on a graph written for the "
            "lesson and reweights it by hand."
        ),
        "body": [
            ("p", "&ldquo;This problem might arise in making a table of distances between all "
                  "pairs of cities for a road atlas.&rdquo; Chapter 25 of CLRS wants the whole "
                  "table at once. The obvious answer runs a single-source algorithm from every "
                  "vertex: Dijkstra |V| times if no weight is negative, O(V³) with an array, or "
                  "Bellman-Ford |V| times otherwise, O(V²E), which is O(V⁴) on a dense graph. "
                  "The chapter does better, and most of it works on an adjacency matrix rather "
                  "than lists."),
            ("p", "Section 25.1 builds a dynamic program from the subpaths lemma. Let the entry "
                  "in row `i` and column `j` of a matrix L(m) be the least weight of a path from "
                  "`i` to `j` with at most `m` edges. L(1) is the weight matrix itself. A path of "
                  "at most `m` edges is a path of at most `m − 1` edges followed by one more "
                  "edge, so L(m) comes from L(m − 1) by trying every possible last edge. Written "
                  "out, that step is a matrix product in which minimum replaces sum and "
                  "addition replaces multiplication. With no negative cycle, shortest paths are "
                  "simple, so L(n − 1) is the answer."),
            ("p", "Computing L(2), L(3), up to L(n − 1) one product at a time costs Θ(n⁴). But "
                  "the product is associative, and any L(m) with m at least n − 1 is the same "
                  "answer, so the section squares instead: L(2), L(4), L(8), until the exponent "
                  "passes n − 1. That is ⌈lg(n − 1)⌉ products, Θ(n³ lg n) in all. The "
                  "authors' point is the shape, shortest paths as repeated matrix "
                  "multiplication, more than the bound."),
            ("p", "Section 25.2 changes the subproblem and wins the logarithm back. Let `D(k)` "
                  "hold, for each pair, the least weight of a path whose interior vertices all "
                  "come from vertices 1 to `k`. A best such path either avoids vertex `k`, so "
                  "its weight is the entry of `D(k − 1)`, or passes through `k` once and splits "
                  "there into two paths that use only vertices 1 to `k − 1`. Each entry of "
                  "`D(k)` is the smaller of those two. FLOYD-WARSHALL computes `D(1)` up to "
                  "`D(n)` with three nested loops, `k` outermost, Θ(n³) in all, and a "
                  "predecessor matrix alongside rebuilds the paths. The same scheme with "
                  "logical or and and computes a graph's transitive closure."),
            ("p", "Section 25.3's Johnson's algorithm suits sparse graphs. Add a new vertex with "
                  "a 0-weight arc to every vertex, run Bellman-Ford from it, and stop if it "
                  "finds a negative cycle; otherwise call the distances `h`. Replace each arc's "
                  "weight `w` from `u` to `v` by `w + h(u) − h(v)`. The triangle inequality makes "
                  "every new weight nonnegative, and Lemma 25.1 shows every path between the "
                  "same two vertices shifts by the same amount, so shortest paths are unchanged. "
                  "Then Dijkstra from every vertex, with a Fibonacci heap, gives "
                  "O(V² lg V + VE) in all."),
            ("p", "The lab runs Floyd-Warshall in your browser. A slider sets how many interior "
                  "vertices are allowed, so you can watch the matrix after each value of `k`, "
                  "and it rebuilds the path between two chosen vertices and compares every entry "
                  "with Bellman-Ford run from each source. It opens on its preset "
                  "<code>interior</code>, four arcs where the route from 1 to 3 needs two "
                  "interior vertices: distance 23, along 1 → 2 → 4 → 3. The preset "
                  "<code>sparse</code>, a chain of eight vertices, does 512 relaxations for 512 "
                  "cell visits, against a reference of 168 for running a heap-based single "
                  "source from each vertex; <code>negcycle</code>, five arcs with a loop through a −3, reports the negative diagonal "
                  "entries 2, 3, 4."),
            ("p", "This lesson's graph has four vertices, six arcs and one negative weight: "
                  "<code>" + APSP_GRAPH + "</code>. Rebuild the path from 4 to 2. The lab "
                  "prints distance 2 along 4 → 3 → 1 → 2, 64 relaxations for 64 cell visits "
                  "(four cubed), no negative diagonal, and agreement on every pair with the "
                  "rounds method. Its reference for a heap-based pass from every source is 48, "
                  "which this graph's negative arc would not allow anyway."),
            ("p", "Now step the slider. Through vertex 1, two cells move: 3 to 2 becomes 1, along "
                  "3 → 1 → 2, and 3 to 4 becomes 5. Through vertex 2, 1 to 3 becomes 7, 1 to 4 "
                  "becomes 5 and 3 to 4 falls to 3. Through vertex 3, row 4 fills in, 4 to 1 at "
                  "−1 and 4 to 2 at 2, and 2 to 1 becomes 2. Through vertex 4, three cells "
                  "improve: 1 to 3 to 6, 2 to 1 to 1 and 2 to 3 to 3. The final rows are "
                  "0, 3, 6, 5; 1, 0, 3, 2; −2, 1, 0, 3; and −1, 2, 1, 0. The entry for 4 to 2 "
                  "first appears at `k` = 3, because its path needs both 3 and 1 inside."),
            ("p", "Reweight the same graph by hand as Johnson would. From an added vertex with "
                  "0-weight arcs to all four, Bellman-Ford gives `h` = (−2, 0, 0, 0): only vertex "
                  "1 gains, through 3. The new weights are 1 for `1 → 2`, 4 for `2 → 3`, 0 for "
                  "`3 → 1`, 5 for `1 → 4`, 1 for `4 → 3` and 2 for `2 → 4`, all nonnegative. The shortest "
                  "reweighted route from 1 to 3 is 1 → 2 → 4 → 3 at 4, and undoing the shift, "
                  "4 − h(1) + h(3) = 6, matches the matrix."),
            ("h3", "Exercise"),
            ("p", "Add the arc <code>3>4 -6</code> to the lesson's graph. Before typing it, "
                  "predict which diagonal entries Floyd-Warshall will make negative and why, "
                  "then check in the lab. Then remove it, and compute L(2) for the original "
                  "graph by hand with the min-plus product: which entries differ from L(1)?"),
            ("p", "Every algorithm so far has moved along paths. The next lesson, Flow Networks "
                  "and Ford-Fulkerson, opens Chapter 26 and asks how much can move along all of "
                  "them at once."),
        ],
        "lab": ("graphkit", {
            "mode": "floyd",
            "preset": "interior",
            "panel_title": "Let in one interior vertex at a time",
            "panel_intro": (
                "Type weighted arcs as tail&gt;head w, then slide how many interior vertices "
                "are allowed and watch which cells of the matrix move. The path between two "
                "chosen vertices is rebuilt, and every entry is checked against Bellman-Ford "
                "from each source. Paste the lesson's graph and rebuild the path from 4 to 2."
            ),
        }),
        "steps_title": "Running Floyd-Warshall by hand",
        "steps_intro": "Five steps, the last on a graph of your own.",
        "steps": [
            ("Write the weight matrix",
             "Row i, column j holds the weight of the arc from i to j, 0 on the diagonal and "
             "infinity where there is no arc. This is D(0)."),
            ("Allow vertex k",
             "For each pair, compare the current entry with the entry from i to k plus the "
             "entry from k to j, and keep the smaller. Note which cells move."),
            ("Repeat for k from 1 to n",
             "Keep k as the outer loop: every entry must be finished for vertices 1 to k − 1 "
             "before vertex k is allowed."),
            ("Read the diagonal",
             "A negative entry on the diagonal means a negative cycle through that vertex, and "
             "the other entries are not distances."),
            ("Do it on a graph of your own",
             "Write the costs between four or five places of your own as arcs, one of them "
             "negative such as a refund, and type them into the lab. Step k from 1 to n and note "
             "which entries move at each step."),
        ],
        "worked": {
            "title": "Four steps on the lesson's graph",
            "intro": [
                "Start from the weight matrix and allow one interior vertex at a time.",
            ],
            "lines": [
                "k = 1: 3 to 2 is 1, 3 to 4 is 5",
                "k = 2: 1 to 3 is 7, 1 to 4 is 5",
                "  and 3 to 4 falls to 3",
                "k = 3: 4 to 1 is −1, 4 to 2 is 2",
                "  and 2 to 1 is 2",
                "k = 4: 1 to 3 is 6, 2 to 3 is 3",
                "  and 2 to 1 is 1",
            ],
            "after": [
                "Sixty-four comparisons, one per cell per value of k, and the final matrix "
                "matches the lab's. The path from 4 to 2 rebuilt from the predecessors is "
                "4 → 3 → 1 → 2, of weight 1 − 2 + 3 = 2.",
            ],
        },
        "quiz_title": "Matrices and reweighting",
        "quiz": [
            {"q": "On the lesson's graph, what is the shortest distance from 4 to 2, and along "
                  "which path?",
             "a": ["2, along 4 → 3 → 1 → 2", "3, along 4 → 3 → 2",
                   "Infinity: there is no arc from 4 toward 2", "6, along 4 → 3 → 1 → 4 → 2"],
             "c": 0,
             "why": "From 4 the only arc is `4 → 3` (1), then `3 → 1` (−2), then `1 → 2` (3): "
                    "1 − 2 + 3 = 2. There is no arc from 3 to 2, so the second path does not "
                    "exist; the lack of a direct arc does not mean no path; and the last "
                    "repeats vertex 4."},
            {"q": "After Floyd-Warshall has allowed only vertex 1 as an interior vertex, what is "
                  "the entry from 3 to 2 on the lesson's graph?",
             "a": ["Infinity", "1", "3", "−2"],
             "c": 1,
             "why": "With vertex 1 allowed, 3 → 1 → 2 costs −2 + 3 = 1. Before that there is "
                    "no route, so infinity is the entry of D(0), not D(1). 3 is the weight of "
                    "`1 → 2` alone, and −2 the weight of `3 → 1` alone."},
            {"q": "Why must `k` be the outermost of Floyd-Warshall's three loops?",
             "a": ["It makes the algorithm run faster but gives the same answer in any order",
                   "Each entry of D(k) needs the entries of D(k − 1) for every pair, which "
                   "must all be finished first",
                   "The innermost loop must run over the largest index",
                   "So that the diagonal is filled last"],
             "c": 1,
             "why": "The recurrence builds D(k) from D(k − 1) for every pair. With `k` inside, "
                    "an entry would be finalised before the later interior vertices were "
                    "allowed, which computes something else. The loop order is the dynamic "
                    "program's order, not an optimisation."},
            {"q": "With `h` = (−2, 0, 0, 0) on the lesson's graph, what is the reweighted "
                  "weight of the arc `3 → 1`?",
             "a": ["−2", "−4", "0", "2"],
             "c": 2,
             "why": "The new weight is w + h(3) − h(1) = −2 + 0 − (−2) = 0. −4 subtracts in "
                    "the wrong order, h(1) − h(3), and −2 is the old weight. 2 is the old weight "
                    "with its sign flipped, as if the shift were the negation."},
        ],
        "mistakes": [
            ("Reading Floyd-Warshall's k as the number of edges on a path",
             "Section 25.1's index m counts edges; Section 25.2's k bounds the labels of "
             "interior vertices, however many edges the path has. On the lesson's graph the "
             "entry from 4 to 2 first appears at k = 3 with a path of three edges, and the "
             "entry from 3 to 2 at k = 1 with two."),
            ("Treating the loop order as a detail",
             "With the pair loops outside and k inside, each entry would be computed once with "
             "whatever its neighbours held at the time, which is not the recurrence. The lab's "
             "hint makes the same point: the outer k loop is the subproblem order, and putting "
             "it anywhere else computes something that often looks right."),
            ("Thinking reweighting can add one constant to every arc",
             "Adding the same constant to every arc does make weights nonnegative, but it "
             "penalises a path once per edge, so paths with more edges lose and the shortest "
             "paths change. Johnson's shift w + h(u) − h(v) moves every path between the same "
             "two ends by the same amount, which is why Lemma 25.1 can say nothing changes."),
        ],
        "standard": (
            "Finish when you can run Floyd-Warshall by hand and reweight a graph for Johnson.",
            "For a weighted digraph of four vertices, write D(k) for each k, rebuild one path, "
            "detect a negative cycle from the diagonal, and compute Johnson's h and the new "
            "weights."
        ),
        "note": (
            "The lab runs Floyd-Warshall and checks it against Bellman-Ford from each source on "
            "your graph; it does not run Section 25.1's products or Johnson's algorithm, which "
            "the lesson does by hand. That D(n) is correct on every graph without a negative "
            "cycle is the recurrence's proof, not the agreement on one."
        ),
    },
    # ---------------------------------------------------------------- 08
    # CLRS Sections 26.1-26.2, pp. 708-732.
    # Quote: p. 708, 22 words, quotes.py OK. Lesson total: 22 words.
    # Flow networks, capacity and conservation, antiparallel edges, multiple
    # sources and sinks (pp. 709-714); the Ford-Fulkerson method, residual
    # networks, cancellation, Lemma 26.1, augmenting paths, Lemma 26.2,
    # cuts, Lemma 26.4, Theorem 26.6 (pp. 714-723); FORD-FULKERSON,
    # O(E |f*|) with integer capacities, Edmonds-Karp, Lemma 26.7, Theorem
    # 26.8, O(VE^2) (pp. 724-730).
    {
        "slug": "maximum-flow",
        "title": "Flow Networks and Ford-Fulkerson",
        "module": "Chapter 26 · Maximum Flow",
        "one_line": "Push flow along a path in the residual network, where undoing earlier flow counts as a path, until none is left; the vertices still reachable then form a cut whose capacity equals the flow.",
        "summary": (
            "Sections 26.1 and 26.2 define a flow network and the Ford-Fulkerson method: "
            "repeatedly find a path in the residual network and push its bottleneck along it. "
            "The max-flow min-cut theorem says the method stops exactly at the maximum, with a "
            "cut of equal capacity as proof. Run it on a five-vertex network written for the "
            "lesson and see a first-found path get stuck until flow may be sent back."
        ),
        "key": [
            "capacity and conservation define a flow",
            "residual: spare capacity, plus undo",
            "augment by the path's bottleneck",
            "no augmenting path: flow is maximum",
            "max flow value = min cut capacity",
            "integer capacities: O(E·|f*|)",
            "Edmonds-Karp, shortest paths: O(V·E²)",
        ],
        "key_label": "Sections 26.1 and 26.2 in seven lines",
        "concepts_intro": (
            "Three objects carry the method and its proof."
        ),
        "concepts": [
            ("A flow network and a flow",
             "A directed graph with a capacity on each arc, a source and a sink. A flow assigns "
             "each arc a value between 0 and its capacity, and at every vertex but the source "
             "and sink, flow in equals flow out. Its value is the net flow out of the source."),
            ("The residual network",
             "For a flow f, an arc with spare capacity gives a residual arc of that spare "
             "amount, and an arc carrying flow gives a residual arc the other way, of the "
             "amount carried: sending along it cancels flow already sent. An augmenting path is "
             "a path from source to sink in this network."),
            ("A cut and its capacity",
             "A cut splits the vertices into a set S holding the source and a set T holding the "
             "sink. Its capacity is the total capacity of arcs from S to T. The net flow across "
             "every cut equals the flow's value (Lemma 26.4), so no flow exceeds any cut."),
        ],
        "read_title": "The sections' argument first, then the augmentations",
        "read_intro": (
            "Read Sections 26.1 and 26.2 in your own copy first. The lesson sets out the "
            "argument in its own words, then pushes flow through a network written for the "
            "lesson."
        ),
        "body": [
            ("p", "&ldquo;Imagine a material coursing through a system from a source, where the "
                  "material is produced, to a sink, where it is consumed.&rdquo; Chapter 26 of "
                  "CLRS turns that picture into a graph. Arcs are conduits with capacities, "
                  "vertices are junctions where nothing collects, and the question is the "
                  "greatest rate at which material can move from source to sink."),
            ("p", "Section 26.1 makes it precise. A flow network is a directed graph with a "
                  "nonnegative capacity on each arc, a source `s` and a sink `t`. A flow "
                  "respects two constraints: the capacity constraint, flow on each arc between 0 "
                  "and its capacity, and flow conservation, flow into every other vertex equal "
                  "to flow out. Its value is the flow out of `s` minus the flow into it. The "
                  "section also shows how to model what the definition forbids: a pair of arcs "
                  "in opposite directions is split with a new vertex, and several sources or "
                  "sinks are joined to a supersource or supersink of unlimited capacity."),
            ("p", "Section 26.2 gives the Ford-Fulkerson method, a method rather than one "
                  "algorithm because it leaves open how to choose each path. Start with zero "
                  "flow. Build the residual network: for each arc, the spare capacity forward, "
                  "and the flow already carried as capacity backward, since sending against an "
                  "arc's flow cancels some of it. Find any route from `s` to `t` through the residual "
                  "network, an augmenting path; push along it the least residual capacity on "
                  "the path, its bottleneck; repeat until no such path remains. Lemma 26.1, "
                  "Lemma 26.2 and Corollary 26.3 show each push yields a flow whose value has "
                  "grown by the bottleneck."),
            ("p", "Why stop exactly at the maximum? Lemma 26.4 says the net flow across any cut "
                  "equals the flow's value, so every flow is at most every cut's capacity. "
                  "Theorem 26.6, the max-flow min-cut theorem, says three things are "
                  "equivalent: the flow is maximum; the residual network has no augmenting "
                  "path; and the flow's value equals some cut's capacity. When the method "
                  "stops, the vertices still reachable from `s` in the residual network form "
                  "that cut: every arc leaving them is full and every arc entering them is "
                  "empty."),
            ("p", "The analysis depends on the choice. With integer capacities each push adds "
                  "at least 1, so FORD-FULKERSON makes at most |f*| augmentations, the maximum "
                  "flow's value, each found in O(E): O(E·|f*|), which can be terrible when "
                  "capacities are large. Edmonds and Karp choose each augmenting path by "
                  "breadth-first search, fewest arcs first. Lemma 26.7 shows the residual "
                  "distance from `s` to every vertex never decreases; each arc can be the "
                  "bottleneck only O(V) times; so Theorem 26.8 bounds the augmentations by "
                  "O(VE), and the running time by O(VE²), whatever the capacities."),
            ("p", "The lab pushes flow in your browser and checks every result: conservation at "
                  "each vertex and every arc within capacity. Two controls matter. One chooses "
                  "the path, the first a depth-first search finds or the shortest in arcs, which "
                  "is Edmonds-Karp. The other puts the backward arcs into the residual network "
                  "or leaves them out; the lab opens with them out, so that you can see what "
                  "they are for. Its preset <code>forwardonly</code>, four vertices with every "
                  "capacity 1, reaches 1 against a true maximum of 2 with them out; "
                  "<code>zigzag</code>, one thin arc between two fat ones, reaches 199 against "
                  "200 with them out, and with them in needs 4 augmentations to reach 200, "
                  "against 2 for the shortest-path rule."),
            ("p", "This lesson's network has five vertices and six arcs, source 1 and sink 5: "
                  "<code>" + FLOW_GRAPH + "</code>. With the first path found and backward arcs "
                  "out, the lab pushes 2 along 1 → 2 → 3 → 4 → 5 in 1 augmentation and stops at "
                  "2, against a true maximum of 3. Nothing out of the source is full; the arc "
                  "`3 → 4` is, and the only way past it is to take back flow sent along `2 → 3`."),
            ("p", "Put the backward arcs in. The same rule now makes 2 augmentations and reaches "
                  "3: the second path is 1 → 3, then back along 2 → 3 against its flow, then "
                  "2 → 4 → 5, with bottleneck 1. That push cancels one unit on `2 → 3`, sending it "
                  "by `2 → 4` instead. Switch to the shortest-path rule and the lab makes 3 "
                  "augmentations, 1 → 2 → 4 → 5, 1 → 3 → 4 → 5 and 1 → 2 → 3 → 4 → 5, none of "
                  "them backward, and also reaches 3. In both runs the search finally reaches "
                  "only vertex 1, and the cut {1} has capacity 2 + 1 = 3: flow equals cut."),
            ("p", "That cut is not the only one of capacity 3. The arcs into 4 make another, "
                  "`2 → 4` and `3 → 4` at 1 + 2, and the arc `4 → 5` alone a third. The lab's list of "
                  "full arcs at the end has five entries, `1 → 2`, `1 → 3`, `2 → 4`, `3 → 4` and `4 → 5`, "
                  "but the cut the final search marks, {1}, has two. The Algorithms Subject's lessons Augmenting "
                  "Paths and Max Flow and Min Cut run both labs on more networks."),
            ("h3", "Exercise"),
            ("p", "Take the network <code>1>2 3, 1>3 2, 2>3 1, 2>4 2, 3>4 3, 4>5 4</code> with "
                  "source 1 and sink 5. Run the Ford-Fulkerson method by hand with "
                  "shortest augmenting paths, writing each residual network, and name a "
                  "minimum cut. Then type it into the lab and try the first-found rule with "
                  "backward arcs out: does it get stuck?"),
            ("p", "A flow with every capacity 1 can only use an arc or not. The next lesson, "
                  "Maximum Bipartite Matching, turns that into an algorithm for pairing."),
        ],
        "lab": ("flowkit", {
            "mode": "augment",
            "preset": "forwardonly",
            "panel_title": "Push flow, with and without the arcs that undo it",
            "panel_intro": (
                "Type arcs with capacities as tail&gt;head c, a source and a sink. Choose the "
                "path rule and whether backward arcs are in the residual network; each "
                "augmentation is listed with its bottleneck, and the result is checked to be a "
                "flow. Paste the lesson's network with source 1 and sink 5."
            ),
        }),
        "steps_title": "Running Ford-Fulkerson by hand",
        "steps_intro": "Five steps, the last on a network of your own.",
        "steps": [
            ("Start with zero flow",
             "Write 0 on every arc. The residual network is the original, every arc at full "
             "capacity."),
            ("Find an augmenting path",
             "Look for a path from source to sink using arcs with spare capacity forward, or "
             "arcs carrying flow, crossed backward. Breadth-first search finds the shortest."),
            ("Push the bottleneck",
             "Add the least residual capacity on the path to each forward arc and subtract it "
             "from each arc crossed backward. Check conservation at the vertices you touched."),
            ("Stop, and read the cut",
             "When no augmenting path remains, mark every vertex still reachable from the "
             "source. The arcs from marked to unmarked vertices are full, and their capacities "
             "add up to the flow's value."),
            ("Do it on a network of your own",
             "Write a delivery or bandwidth network of five or six places with capacities and "
             "type it into the lab. Find the maximum with both path rules, and note which cut "
             "proves it."),
        ],
        "worked": {
            "title": "The lesson's network, first-found paths",
            "intro": [
                "Push along the first path a depth-first search finds, arcs in typed order.",
            ],
            "lines": [
                "path 1 → 2 → 3 → 4 → 5, bottleneck 2",
                "flow 2; 1 → 2, 2 → 3, 3 → 4 now full",
                "forward only: 1 reaches 3, then stops",
                "with undo: 1 → 3, back to 2, 2 → 4 → 5",
                "bottleneck 1: flow 3",
                "residual: 1 reaches nothing else",
                "cut {1}: 2 + 1 = 3",
            ],
            "after": [
                "Value 3, cut 3, so the flow is maximum and the cut proves it, as Theorem 26.6 "
                "says. Without the backward arc the method stopped at 2 with spare capacity "
                "out of the source, which is the run the lab shows first.",
            ],
        },
        "quiz_title": "Residual networks and cuts",
        "quiz": [
            {"q": "On the lesson's network, after pushing 2 along 1 → 2 → 3 → 4 → 5, what "
                  "residual capacity runs from 3 back to 2?",
             "a": ["0", "1", "2", "4"],
             "c": 2,
             "why": "The arc `2 → 3` carries 2, so the residual network has an arc from 3 to 2 "
                    "of capacity 2: up to 2 units can be cancelled. Its forward residual is "
                    "2 − 2 = 0, which is the number a forward-only view sees. 4 adds the "
                    "capacity and the flow."},
            {"q": "What is the maximum flow of the lesson's network, and which cut proves it?",
             "a": ["2, the cut {1, 2, 3}", "3, the cut {1}", "3, the cut {1, 2}",
                   "4, the cut {1, 2, 3, 4}"],
             "c": 1,
             "why": "The cut {1} has capacity 2 + 1 = 3 and a flow of 3 exists, so both are "
                    "extreme. The cut {1, 2, 3} has capacity 1 + 2 = 3, not 2, and 2 is where "
                    "the forward-only run stopped. {1, 2} has capacity 1 + 2 + 1 = 4, and "
                    "{1, 2, 3, 4} has capacity 3."},
            {"q": "Which of these is NOT one of the conditions Theorem 26.6 proves equivalent?",
             "a": ["f is a maximum flow",
                   "The residual network of f has no augmenting path",
                   "|f| equals the capacity of some cut",
                   "Every arc leaving the source is saturated by f"],
             "c": 3,
             "why": "The theorem's three conditions are the first three. A maximum flow need "
                    "not fill every arc out of the source: when the bottleneck is further on, "
                    "some stay partly empty. On the lesson's network they happen to be full, "
                    "which is a fact about this network."},
            {"q": "What bounds the number of augmentations in the Edmonds-Karp algorithm "
                  "regardless of the capacities?",
             "a": ["Each augmentation adds at least 1 to the flow",
                   "Residual distances from the source never decrease, so each arc is a "
                   "bottleneck O(V) times",
                   "Breadth-first search never uses a backward arc",
                   "Each augmentation saturates an arc out of the source"],
             "c": 1,
             "why": "Lemma 26.7 and Theorem 26.8: with shortest paths, distances in the residual "
                    "network only grow, and between two times an arc is critical its distance "
                    "rises by 2, giving O(VE) augmentations. Adding at least 1 gives the "
                    "capacity-dependent O(E·|f*|) bound instead. Shortest paths can cross arcs "
                    "backward, and a bottleneck need not be at the source."},
        ],
        "mistakes": [
            ("Thinking flow, once sent along an arc, can only be added to",
             "Without backward arcs the method is greedy and can stop below the maximum. On "
             "the lesson's network the first path found sends 2 through `2 → 3`, and with "
             "backward arcs left out the lab stops at 2 against a maximum of 3. Cancelling one "
             "unit on `2 → 3` is what lets the third unit through, and it is why the residual "
             "network carries backward arcs at all."),
            ("Taking the full arcs to be the minimum cut",
             "Every arc of a minimum cut is full at a maximum flow, but full arcs need not form "
             "a cut, or the minimum one. On the lesson's network five arcs end full and the "
             "cut the method returns, {1}, has two. A cut is a fact about a set of vertices, "
             "not about which arcs are saturated."),
            ("Assuming Ford-Fulkerson's time depends only on the graph's size",
             "With an arbitrary choice of path the bound is O(E·|f*|), which grows with the "
             "capacities. With backward arcs in, the lab's preset zigzag needs 4 augmentations with "
             "first-found paths against 2 with shortest ones, and Section 26.2 shows a poor choice of paths "
             "needing a number of augmentations that grows with the capacities. Edmonds and Karp's shortest-path choice removes the dependence: O(VE²)."),
        ],
        "standard": (
            "Finish when you can run Ford-Fulkerson by hand and prove the result maximum.",
            "For a network of five or six vertices, list each augmenting path and bottleneck, "
            "draw the final residual network, and give a cut whose capacity equals the flow."
        ),
        "note": (
            "The lab checks that its result is a flow, and the mincut mode lists every cut, so "
            "on a small network the theorem's equality can be seen. It counts the augmentations "
            "one rule needs on one network; the O(VE) bound on every network is Theorem 26.8's "
            "proof."
        ),
    },
    # ---------------------------------------------------------------- 09
    # CLRS Section 26.3, pp. 732-736; Sections 26.4-26.5 named.
    # Quote: p. 732, 25 words, quotes.py OK. Lesson total: 25 words.
    # Matching, maximum matching, bipartite graphs, machines and tasks
    # (p. 732); the corresponding flow network with unit capacities, Lemma
    # 26.9, integer-valued flows (p. 733); Theorem 26.10, Corollary 26.11,
    # O(VE) (pp. 734-735); push-relabel O(V^2 E) and relabel-to-front O(V^3)
    # named (p. 736).
    {
        "slug": "maximum-bipartite-matching",
        "title": "Maximum Bipartite Matching",
        "module": "Chapter 26 · Maximum Flow",
        "one_line": "Give every edge of a bipartite graph capacity 1, add a source and a sink, and a maximum flow is a maximum matching, because Ford-Fulkerson's flows are whole numbers.",
        "summary": (
            "Section 26.3 solves a problem that looks nothing like flow: pair as many vertices "
            "on one side of a bipartite graph with vertices on the other as possible. Unit "
            "capacities and the integrality theorem turn a maximum flow into a maximum "
            "matching in O(VE). Run it on four machines and four tasks written for the lesson, "
            "beside a greedy pairing that gets stuck."
        ),
        "key": [
            "matching: no vertex in two edges",
            "source to L, L to R, R to sink",
            "every capacity 1",
            "integer capacities give integer flow",
            "flow value = matching size",
            "O(V) augmentations: O(V·E)",
        ],
        "key_label": "Section 26.3 in six lines",
        "concepts_intro": (
            "Three ideas: the problem, the network that encodes it, and the theorem that makes "
            "the encoding exact."
        ),
        "concepts": [
            ("A maximum matching",
             "A matching is a set of edges with no vertex in two of them. A maximum matching "
             "has as many edges as any matching can. A matching that cannot be extended by "
             "adding an edge is maximal, which is weaker: it may still be smaller than the "
             "maximum."),
            ("The corresponding flow network",
             "For a bipartite graph with sides L and R, add a source with an arc to every "
             "vertex of L and a sink with an arc from every vertex of R, direct every edge from "
             "L to R, and give every arc capacity 1. A matching of size k gives a flow of value "
             "k, and an integer flow of value k gives a matching of size k (Lemma 26.9)."),
            ("The integrality theorem",
             "Theorem 26.10: when every capacity is an integer, the Ford-Fulkerson method "
             "produces a maximum flow whose value and every arc's flow are integers. With unit "
             "capacities each arc then carries 0 or 1, so the arcs from L to R carrying 1 are a "
             "matching."),
        ],
        "read_title": "The section's argument first, then the pairing",
        "read_intro": (
            "Read Section 26.3 in your own copy first. The lesson sets out the argument in its "
            "own words, then solves a matching written for the lesson as a flow."
        ),
        "body": [
            ("p", "&ldquo;Some other combinatorial problems seem on the surface to have little "
                  "to do with flow networks, but can in fact be reduced to maximum-flow "
                  "problems.&rdquo; Section 26.3 of CLRS takes one such problem, matching in "
                  "a bipartite graph, and reduces it to the flow of the lesson before. The "
                  "authors' example is machines and tasks: an edge says a machine can do a "
                  "task, and a maximum matching keeps as many machines busy as possible at "
                  "once."),
            ("p", "First the definitions. A matching is a set of edges in which no vertex "
                  "appears twice; a vertex in one of its edges is matched. A maximum matching "
                  "has the largest number of edges any matching can have. The section restricts "
                  "attention to bipartite graphs, whose vertices split into two sides L and R "
                  "with every edge running between them, and assumes every vertex has at least "
                  "one edge."),
            ("p", "Then the network. Add a source `s` with an arc to every vertex in L and a sink "
                  "`t` with an arc from every vertex in R, direct each edge from L to R, and give "
                  "every arc capacity 1. Lemma 26.9 shows that a matching of size `k` gives an "
                  "integer-valued flow of value `k`, one unit along each matched edge, and that "
                  "an integer-valued flow of value `k` gives a matching of size `k`: each vertex "
                  "of L receives at most one unit from `s`, so it sends at most one unit on, and "
                  "each vertex of R passes at most one unit to `t`."),
            ("p", "The gap is that a maximum flow could in principle split units in half. "
                  "Theorem 26.10, the integrality theorem, closes it: with integer capacities "
                  "the Ford-Fulkerson method only ever pushes whole bottlenecks, so the flow it "
                  "returns is integer-valued on every arc. Corollary 26.11 concludes that the "
                  "size of a maximum matching equals the value of a maximum flow in the "
                  "network, and the method finds both."),
            ("p", "The running time is the method's own bound with a small maximum. A matching "
                  "has at most min(|L|, |R|) edges, which is O(V), so there are O(V) "
                  "augmentations, each found in O(E) time: O(VE) in all. Section 26.4, which "
                  "follows, develops push-relabel algorithms, which push "
                  "excess flow from vertex to vertex guided by a height function instead of "
                  "following whole paths, and bounds the generic version at O(V²E); Section "
                  "26.5's relabel-to-front algorithm runs in O(V³). Both sections are starred, "
                  "and their proofs are left to the book."),
            ("p", "The lab builds the network from the pairs you type, finds a maximum flow, and "
                  "reads the matching off the middle arcs. It also checks the answer three other "
                  "ways that make good evidence: every subset "
                  "of the pairs is tried; the cut is read back as a vertex cover, a set of "
                  "vertices touching every pair, which can never be smaller than a matching; and "
                  "Hall's condition, that every set of left vertices has at least as many "
                  "neighbours, is tested (the section's text never uses it; it appears only in "
                  "Exercise 26.3-4). Beside them it runs a greedy pass that takes pairs in "
                  "typed order whenever both ends are free."),
            ("p", "It opens on its preset <code>maximal</code>, two vertices a side and three "
                  "pairs: a matching of 2, while the greedy pass stops at 1, maximal and not "
                  "maximum. The preset <code>perfect</code>, three a side and six pairs, matches all three left vertices, "
                  "with a cover of 3 and Hall's condition holding; <code>hall</code> puts three "
                  "left vertices against two and reports the condition failing at {1, 2}; "
                  "<code>star</code> has one popular right vertex, a matching of 2 of 5 pairs, "
                  "and the condition failing at {1, 2, 3}."),
            ("p", "This lesson's graph has four machines on the left, four tasks on the right, "
                  "and seven allowed pairs. Set both sides to 4 and type <code>" + MATCH_PAIRS
                  + "</code>. The lab finds a matching of 4 of the 7 pairs, L1 with R2, L2 with "
                  "R1, L3 with R3 and L4 with R4: every machine busy. The cover read from the "
                  "cut has 4 vertices, all 128 subsets of the pairs agree on 4, every flow value "
                  "is a whole number, and Hall's condition holds."),
            ("p", "The greedy pass takes L1 with R1, then L3 with R2, then L4 with R3, and stops "
                  "at 3, because L2's only task is taken. Nothing can be added to its three "
                  "pairs, yet one more is possible. The flow finds it along an augmenting path "
                  "from L2: to R1, back from R1 to L1, on to R2, back to L3, on to R3, back to "
                  "L4, and on to R4. Three greedy pairs are undone and four new ones made. The "
                  "network for this graph has 10 vertices, with `s` and `t`, and 4 + 7 + 4 = 15 "
                  "arcs. The Algorithms Subject's lesson Bipartite Matching runs the same lab."),
            ("h3", "Exercise"),
            ("p", "Take three people and four shifts with the pairs <code>1-1, 1-2, 2-2, 3-2, "
                  "3-3, 3-4</code>. Draw the flow network, find a maximum matching by hand with "
                  "augmenting paths, and check whether a greedy pass in that order finds it. "
                  "Then set the lab to 3 on the left and 4 on the right and compare."),
            ("p", "This lesson ends Part VI. The next course, Parallel, Matrix, Linear and Number "
                  "Algorithms, reads the first chapters of Part VII, beginning with "
                  "multithreaded algorithms."),
        ],
        "lab": ("flowkit", {
            "mode": "matching",
            "preset": "maximal",
            "panel_title": "Pair the two sides through a unit-capacity flow",
            "panel_intro": (
                "Choose the number of vertices on each side and type the allowed pairs as "
                "left-right. The lab builds the unit-capacity network, reads the matching off a "
                "maximum flow, and checks it by trying every subset of the pairs. Paste the "
                "lesson's pairs with 4 on each side."
            ),
        }),
        "steps_title": "Solving a matching as a flow",
        "steps_intro": "Five steps, the last on a pairing of your own.",
        "steps": [
            ("Build the network",
             "Add a source with an arc to every left vertex and a sink with an arc from every "
             "right vertex, direct each pair from left to right, and give every arc capacity 1."),
            ("Augment from a free left vertex",
             "Find a path from the source through a free left vertex, alternating between "
             "unused pairs forward and matched pairs backward, to a free right vertex and the "
             "sink."),
            ("Flip the path",
             "Each unused pair on the path joins the matching and each matched pair on it "
             "leaves. The matching grows by exactly one."),
            ("Stop when no path remains",
             "When no augmenting path exists, the matching is maximum by the max-flow min-cut "
             "theorem, and its size is the flow's value."),
            ("Do it on a pairing of your own",
             "Write who on a small team can cover which of four duties as pairs and type them "
             "into the lab. Note the maximum matching and whether a greedy pass in your order "
             "found it."),
        ],
        "worked": {
            "title": "Growing the greedy matching by one",
            "intro": [
                "Start from the greedy pairs and look for a path from the free machine L2.",
            ],
            "lines": [
                "greedy: L1 with R1, L3 with R2, L4 with R3",
                "free: L2 on the left, R4 on the right",
                "L2 to R1, back to L1",
                "L1 to R2, back to L3",
                "L3 to R3, back to L4",
                "L4 to R4: path found",
                "now L2 with R1, L1 with R2, L3 with R3,",
                "  and L4 with R4",
            ],
            "after": [
                "One augmenting path undid three greedy pairs and made four, raising the "
                "matching from 3 to 4, which is the maximum the lab reports. No vertex can be "
                "in two pairs, so 4 on four machines is also the most possible.",
            ],
        },
        "quiz_title": "Matchings and flows",
        "quiz": [
            {"q": "On the lesson's graph, how large is a maximum matching, and how large is the "
                  "matching the greedy pass in typed order finds?",
             "a": ["4 and 4", "4 and 3", "3 and 3", "7 and 4"],
             "c": 1,
             "why": "L1–R2, L2–R1, L3–R3 and L4–R4 match all four machines. The greedy pass "
                    "takes L1–R1 first, which leaves L2 with nothing, and stops at 3. A matching "
                    "cannot have 7 edges among 4 machines, since no machine can be in two."},
            {"q": "How many vertices and arcs does the flow network for the lesson's graph have?",
             "a": ["8 vertices and 7 arcs", "10 vertices and 11 arcs",
                   "10 vertices and 15 arcs", "10 vertices and 22 arcs"],
             "c": 2,
             "why": "Four machines, four tasks, a source and a sink make 10 vertices; 4 arcs from "
                    "the source, 7 for the pairs and 4 into the sink make 15. 8 and 7 forget the "
                    "source and sink; 11 forgets one side's extra arcs; 22 counts residual "
                    "backward arcs, which are not arcs of the network."},
            {"q": "Why is a maximum flow in the unit-capacity network a matching, and not a set "
                  "of half-units?",
             "a": ["Because the network is acyclic",
                   "Because the integrality theorem gives an integer flow on every arc, so each "
                   "carries 0 or 1",
                   "Because every maximum flow of any network is integer-valued",
                   "Because the source has only one arc to each left vertex"],
             "c": 1,
             "why": "Theorem 26.10: with integer capacities Ford-Fulkerson returns a flow with "
                    "an integer on every arc. In other networks some maximum flows split "
                    "units, so not every maximum flow is integral; the method's is. Acyclicity "
                    "and the source's arcs do not rule out fractions."},
            {"q": "The augmenting path from L2 in the worked example turns the greedy matching "
                  "into a maximum one. How many greedy pairs does it remove?",
             "a": ["1", "2", "3", "4"],
             "c": 2,
             "why": "It runs backward along L1–R1, L3–R2 and L4–R3, removing all three, and "
                    "forward along four unused pairs, adding L2–R1, L1–R2, L3–R3 and L4–R4. An "
                    "augmenting path always adds one more pair than it removes."},
        ],
        "mistakes": [
            ("Thinking a matching nothing can be added to is maximum",
             "A maximal matching only says no edge can be added as it stands. On the lesson's "
             "graph the greedy pass stops at 3 pairs, maximal, while 4 are possible. Reaching 4 "
             "requires undoing all three greedy choices along one augmenting path, which is "
             "what the residual network's backward arcs make possible."),
            ("Believing every maximum flow in the network is a matching",
             "The reduction relies on the flow being integral, and Theorem 26.10 promises that "
             "for the flow Ford-Fulkerson returns, not for every maximum flow. If L1 and L2 are "
             "both joined to R1 and R2, half a unit on each of the four middle arcs is a "
             "maximum flow of value 2 that is no matching. The lab "
             "checks the whole-number property on its own flow: yes, every one."),
            ("Expecting push-relabel to be needed for matching",
             "The push-relabel methods of Sections 26.4 and 26.5 give better bounds for general flow, O(V²E) and O(V³), but "
             "matching already has O(VE) from Ford-Fulkerson because its maximum is at most "
             "O(V). The book presents push-relabel as the route to faster flow algorithms, not "
             "as a requirement for matching."),
        ],
        "standard": (
            "Finish when you can solve a bipartite matching as a flow by hand.",
            "For a bipartite graph of three or four vertices a side, build the unit-capacity "
            "network, find a maximum matching by augmenting paths, and explain with the "
            "integrality theorem why the flow is a matching."
        ),
        "note": (
            "The lab solves one bipartite graph of up to four vertices a side and checks the "
            "matching by trying every subset of pairs, so its answer is complete for that "
            "graph. The cover and Hall's condition it reports go beyond Section 26.3. That the "
            "method finds a maximum matching on every bipartite graph is Corollary 26.11."
        ),
    },
]
