"""Graph Algorithms, lessons 1-5 -- Chapters 22 and 23.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT
Press, 2009): Chapter 22, Elementary Graph Algorithms (pp. 589-623), and
Chapter 23, Minimum Spanning Trees (pp. 624-642). Every quotation is copied
from the operator's copy with its printed page in the comment beside the
lesson. The graphs are written for these lessons; none of the book's figures
is reproduced. Each graph is one constant below, written in the lab's own
notation, so the text the reader pastes and the text the prose describes are
the same string.

The graphkit and flowkit labs carry their own presets (the kits fix them), so
each of those lessons' own graph is given for the reader to type into the lab's editor, and
every figure the prose quotes for it was read off the lab with that graph
typed in.
"""

# ---------------------------------------------------------------- graphs

# Graph Representations and Breadth-First Search: ten vertices, eleven
# undirected edges, in two pieces.
BFS_GRAPH = "s, a; s, b; a, c; b, c; b, d; c, e; d, e; d, f; e, g; f, g; h, i"

# Depth-First Search: six vertices, eight arcs, all four classes from root 1.
DFS_GRAPH = "1>2, 1>4, 1>3, 2>4, 4>1, 3>4, 5>3, 5>6"

# Topological Sort and Strongly Connected Components.
SCC_GRAPH = "1>2, 2>3, 3>1, 3>4, 4>5, 5>4, 2>6, 6>4, 7>6"
DAG_GRAPH = "1>3, 2>3, 3>4, 2>5, 5>4, 4>6"

# Minimum Spanning Trees: six vertices, nine weighted edges, one tie at 3.
MST_GRAPH = "1-2 3, 1-3 1, 2-3 3, 2-4 2, 3-5 4, 4-5 5, 4-6 6, 5-6 2, 3-4 7"

# Bellman-Ford and Shortest Paths in DAGs: five vertices, three negative arcs,
# no cycle at all.
BF_GRAPH = "1>2 4, 1>3 5, 2>4 -2, 3>2 -3, 3>4 3, 4>5 2, 2>5 6"
BF_REVERSED = "4>5 2, 2>5 6, 3>4 3, 3>2 -3, 2>4 -2, 1>3 5, 1>2 4"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS Sections 22.1-22.2, pp. 589-602.
    # Quote: p. 594, 20 words, quotes.py OK. Lesson total: 20 words.
    # Lists and matrices, Theta(V + E) and Theta(V^2) memory, weights,
    # attributes (pp. 589-592); BFS, colours, the queue, d and pi (pp. 594-596);
    # aggregate analysis O(V + E) (pp. 596-597); delta(s, v), Lemmas 22.1-22.3,
    # Corollary 22.4, Theorem 22.5 (pp. 597-600); breadth-first trees, Lemma
    # 22.6, PRINT-PATH (pp. 600-601).
    {
        "slug": "breadth-first-search",
        "title": "Graph Representations and Breadth-First Search",
        "module": "Chapter 22 · Elementary Graph Algorithms",
        "one_line": "Store a graph as adjacency lists, then search it from one source with a queue, and every vertex's distance in edges falls out of the order it is discovered.",
        "summary": (
            "Sections 22.1 and 22.2 choose a representation and run the first search on it. "
            "Adjacency lists take memory in proportion to V + E, an adjacency matrix V². "
            "Breadth-first search discovers vertices in layers by distance from the source, "
            "builds a breadth-first tree of shortest paths, and runs in O(V + E). Run it on a "
            "ten-vertex graph written for the lesson and count what it enqueues and examines."
        ),
        "key": [
            "lists: Θ(V + E) memory; matrix: Θ(V²)",
            "undirected lists hold 2E entries",
            "a FIFO queue holds the grey frontier",
            "d = d[u] + 1 when v is discovered",
            "each list is scanned once: O(V + E)",
            "d ends equal to the fewest edges",
            "parents form a breadth-first tree",
        ],
        "key_label": "Sections 22.1 and 22.2 in seven lines",
        "concepts_intro": (
            "Three ideas: how a graph sits in memory, what the search keeps, and what it finds."
        ),
        "concepts": [
            ("Adjacency lists and the adjacency matrix",
             "Adjacency lists keep, for each vertex, a list of its neighbours: Θ(V + E) memory, "
             "and the usual choice for a sparse graph. An adjacency matrix keeps a V-by-V table "
             "of 0s and 1s: Θ(V²) memory whatever the number of edges, but it answers whether an "
             "edge exists in constant time."),
            ("The frontier and the queue",
             "Breadth-first search colours vertices white, grey and black. Grey vertices have "
             "been discovered but not yet scanned; they are the frontier between the found and "
             "the unfound, and a first-in, first-out queue holds them in the order discovered."),
            ("Shortest-path distance and the breadth-first tree",
             "The distance δ(s, v) is the fewest edges on any path from the source s to v, or "
             "infinity when there is none. Breadth-first search records a parent for each vertex "
             "it discovers, and the parents form a tree whose path from s to any vertex is a "
             "shortest one."),
        ],
        "read_title": "The sections' argument first, then the search",
        "read_intro": (
            "Read Sections 22.1 and 22.2 in your own copy first. The lesson sets out the "
            "argument in its own words, then runs the search on a graph written for the lesson."
        ),
        "body": [
            ("p", "&ldquo;Breadth-first search is one of the simplest algorithms for searching a "
                  "graph and the archetype for many important graph algorithms.&rdquo; So CLRS "
                  "introduce it in Section 22.2, and they name two of its descendants straight "
                  "away: Prim's minimum-spanning-tree algorithm and Dijkstra's shortest paths, "
                  "both later in this course. Part VI opens with Chapter 22's two plain tasks, "
                  "storing a graph and searching it, because nearly every algorithm after them "
                  "starts by doing both."),
            ("p", "Section 22.1 compares two representations. Adjacency lists give each vertex "
                  "a list of the vertices it has an edge to. In a directed graph the lists hold "
                  "|E| entries in all, in an undirected graph 2|E|, since each edge appears in "
                  "the lists of both its ends; either way the memory is Θ(V + E). An adjacency "
                  "matrix is a |V|-by-|V| table with a 1 where an edge exists, Θ(V²) memory "
                  "regardless of how many edges there are. The authors prefer lists for sparse "
                  "graphs, where E is much smaller than V², and the matrix for dense ones or "
                  "when the question is whether one particular edge exists. Either form takes "
                  "weights by storing a weight beside each entry."),
            ("p", "Section 22.2's procedure BFS takes a graph and a source `s`. It colours every "
                  "vertex white, gives it distance infinity and no parent, then colours `s` grey "
                  "with distance 0 and puts it in a queue. While the queue is not empty it takes "
                  "the vertex `u` at the head, looks at every entry `v` on `u`'s list, and for "
                  "each white `v` sets its distance to `d[u] + 1`, its parent to `u`, colours it "
                  "grey and puts it at the tail. When `u`'s list is done, `u` turns black. The "
                  "queue is why the search spreads evenly: every vertex at distance `k` is "
                  "discovered before any at distance `k + 1`."),
            ("p", "The running time is an aggregate count. No vertex is ever whitened again, so "
                  "each is enqueued and dequeued at most once, O(V) for the queue. Each "
                  "adjacency list is scanned once, when its vertex is dequeued, and the lists "
                  "hold Θ(E) entries, so scanning is O(E). With Θ(V) to initialise, the total is "
                  "O(V + E), linear in the size of the lists. It is O and not Θ because a vertex "
                  "the source cannot reach is never enqueued and its list is never read."),
            ("p", "The section then proves that the distances are right. Lemma 22.1 says that "
                  "along any edge from `u` to `v`, δ(s, v) is at most δ(s, u) + 1. Lemma 22.2 "
                  "says the search never sets a distance below the true one. Lemma 22.3 says "
                  "the queue always holds distances in nondecreasing order from head to tail, "
                  "with the tail at most one more than the head. Theorem 22.5 puts them "
                  "together: every vertex reachable from `s` is discovered, its recorded "
                  "distance equals δ(s, v), and following parents back from it gives a shortest "
                  "path. Lemma 22.6 calls the parents' subgraph a breadth-first tree, and the "
                  "procedure PRINT-PATH prints a path from it by recursion."),
            ("p", "The lab runs the search in your browser on edges you type as records "
                  "<code>from, to</code>, one per semicolon, with any names for the vertices. "
                  "Adjacency lists follow the order of the edges, so you can see the order's "
                  "effect. Its tiles are the distance of every vertex, the parent of every "
                  "discovered vertex, the vertices by layer, how many vertices were enqueued, "
                  "how many adjacency entries were examined out of the total in the lists, and "
                  "which vertices were never reached."),
            ("p", "This lesson's graph has ten vertices and eleven undirected edges: <code>"
                  + BFS_GRAPH + "</code>. The preset <code>two-pieces</code> searches it from "
                  "`s`. The layers are 0: s; 1: a b; 2: c d; 3: e f; 4: g. The lab enqueues 8 of "
                  "10 vertices and examines 20 of the 22 adjacency entries; h and i are not "
                  "reachable and keep distance ∞, which is why the bound is O(V + E) rather than "
                  "a count of every entry. The parents are a ← s, b ← s, c ← a, d ← b, e ← c, "
                  "f ← d and g ← e, and the path back from g, g ← e ← c ← a ← s, has 4 edges, "
                  "its distance."),
            ("p", "The preset <code>directed-from-s</code> reads the same eleven records as arcs "
                  "pointing from the first name to the second. Every arc here points away from "
                  "`s`, so the distances are unchanged, but the lists now hold 11 entries, not "
                  "22, and the lab examines 10 of 11. The preset <code>directed-from-c</code> "
                  "starts at `c` instead: only e and g can be reached, at distances 1 and 2, the "
                  "lab enqueues 3 of 10 vertices and examines 2 of 11 entries, and 7 vertices "
                  "are not reachable. Undirected, from the same `c`, every vertex but h and i "
                  "would be found; direction decides what a search can see."),
            ("p", "The preset <code>hexagon</code> is a cycle of six vertices searched from 1. "
                  "The far vertex, 4, is at distance 3 by either way round, and the lab gives it "
                  "the parent 3, because the edge to 3 was dequeued first: layers 0: 1; 1: 2 6; "
                  "2: 3 5; 3: 4. Type the edge <code>6, 1</code> first instead and 4's parent becomes 5. "
                  "The distances cannot change, since Theorem 22.5 fixes them as δ(s, v); the "
                  "tree can, and the theorem promises only that it is a breadth-first tree."),
            ("p", "Section 22.1's comparison, counted by hand on the lesson's graph: the "
                  "adjacency lists hold 2 × 11 = 22 entries beside 10 list heads, while the "
                  "matrix would have 10 × 10 = 100 cells, 22 of them 1. To find a vertex's "
                  "neighbours the matrix scans a whole row of 10 cells; the list holds only the "
                  "neighbours. That is the case for lists on a sparse graph, and the search's "
                  "20 examined entries are the lists' advantage made into a count."),
            ("h3", "Exercise"),
            ("p", "Take the undirected graph <code>p, q; p, r; q, s; r, s; s, t; t, u; r, u; v, "
                  "w</code> and search it by hand from p, writing the queue after each dequeue, "
                  "every distance and every parent. How many adjacency entries does the search "
                  "examine, out of how many? Then type it into the lab, and try reading it as "
                  "directed from p."),
            ("p", "Breadth-first search spreads from one source a layer at a time. The next "
                  "lesson, Depth-First Search, goes as deep as it can instead, and stamps every "
                  "vertex with two times."),
        ],
        "lab": ("itakit", {
            "mode": "bfs",
            "view": "search",
            "preset": "two-pieces",
            "presets": [
                {"id": "two-pieces",
                 "label": "Ten vertices in two pieces, undirected, from s",
                 "edges": BFS_GRAPH, "graph": "undirected", "source": "s",
                 "expect": {"bfiDist": "s 0, a 1, b 1, c 2, d 2, e 3, f 3, g 4, h ∞, i ∞",
                            "bfiLayers": "0: s; 1: a b; 2: c d; 3: e f; 4: g",
                            "bfiEnqueued": "8 of 10 vertices", "bfiScanned": "20 of 22 (2E)",
                            "bfiUnreached": "2: h, i"}},
                {"id": "directed-from-s",
                 "label": "The same records as arcs, from s",
                 "edges": BFS_GRAPH, "graph": "directed", "source": "s",
                 "expect": {"bfiEnqueued": "8 of 10 vertices", "bfiScanned": "10 of 11 (E)"}},
                {"id": "directed-from-c",
                 "label": "The same records as arcs, from c",
                 "edges": BFS_GRAPH, "graph": "directed", "source": "c",
                 "expect": {"bfiLayers": "0: c; 1: e; 2: g", "bfiEnqueued": "3 of 10 vertices",
                            "bfiScanned": "2 of 11 (E)", "bfiUnreached": "7: s, a, b, d, f, h, i"}},
                {"id": "hexagon",
                 "label": "A cycle of six vertices, from 1",
                 "edges": "1, 2; 2, 3; 3, 4; 4, 5; 5, 6; 6, 1", "graph": "undirected",
                 "source": "1",
                 "expect": {"bfiParent": "2 ← 1, 6 ← 1, 3 ← 2, 5 ← 6, 4 ← 3",
                            "bfiLayers": "0: 1; 1: 2 6; 2: 3 5; 3: 4", "bfiScanned": "12 of 12 (2E)"}},
            ],
            "panel_title": "Search from one source, a layer at a time",
            "panel_intro": (
                "Type edges as from, to records separated by semicolons, choose undirected or "
                "directed and a source. The lab runs breadth-first search with the adjacency "
                "lists in the order you typed, and counts the vertices enqueued and the "
                "adjacency entries examined."
            ),
        }),
        "steps_title": "Running breadth-first search by hand",
        "steps_intro": "Five steps, the last on a graph of your own.",
        "steps": [
            ("Write the adjacency lists",
             "For each edge, add each end to the other's list (or the head to the tail's list, "
             "if directed), in the order the edges are given."),
            ("Start the queue at the source",
             "Give the source distance 0 and put it in the queue. Every other vertex is white, "
             "at distance infinity, with no parent."),
            ("Dequeue and scan",
             "Take the vertex at the head and read its whole list. Each white neighbour gets "
             "distance one more, this vertex as parent, and goes to the tail."),
            ("Read the layers and the tree",
             "When the queue is empty, group vertices by distance, draw each parent edge, and "
             "list any vertex left at infinity."),
            ("Do it on a graph of your own",
             "Write a few friendships, station links or web links of your own as records and "
             "type them into the lab. Note each vertex's distance from one of them and how many "
             "adjacency entries the search examined."),
        ],
        "worked": {
            "title": "The queue on the lesson's graph",
            "intro": [
                "Search from s, each list in the order the edges are typed.",
            ],
            "lines": [
                "dequeue s: enqueue a, b at 1",
                "dequeue a: enqueue c at 2",
                "dequeue b: c is grey; enqueue d at 2",
                "dequeue c: enqueue e at 3",
                "dequeue d: enqueue f at 3",
                "dequeue e: enqueue g at 4",
                "dequeue f, then g: nothing new",
                "8 enqueued, 20 entries read; h, i never",
            ],
            "after": [
                "The queue held distances 1 and 2, then 2 and 3, then 3 and 4: never more than "
                "two values at once, as Lemma 22.3 says. Every distance is the number of edges "
                "on the path the parents give back to s.",
            ],
        },
        "quiz_title": "Lists, queues and distances",
        "quiz": [
            {"q": "On the lesson's undirected graph, searched from s, what is the distance of g?",
             "a": ["3", "4", "5", "∞"],
             "c": 1,
             "why": "g is adjacent only to e and f, both at distance 3, so it is at 4, along "
                    "s, a, c, e, g or s, b, d, f, g. Nothing at distance 2 is adjacent to g, so it "
                    "cannot be 3; 5 would need a longer path to be the shortest; and g is "
                    "reachable, so it is not ∞."},
            {"q": "How many entries do the adjacency lists of the lesson's undirected graph hold, "
                  "and how many cells does its adjacency matrix have?",
             "a": ["11 entries and 100 cells", "22 entries and 100 cells",
                   "22 entries and 121 cells", "20 entries and 100 cells"],
             "c": 1,
             "why": "Eleven undirected edges appear twice each in the lists, 22 entries, and ten "
                    "vertices make a 10-by-10 matrix of 100 cells. Eleven counts each edge once, "
                    "as a directed graph would; 121 sizes the matrix by edges; 20 is the number "
                    "the search examined, which leaves out the unreachable h and i."},
            {"q": "Which statement does Lemma 22.3 make about the queue during breadth-first "
                  "search?",
             "a": ["Its distances never decrease from head to tail, and the tail's is at most "
                   "the head's plus 1",
                   "It never holds more than two vertices at once",
                   "Every vertex in it has the same distance",
                   "Its distances strictly increase from head to tail"],
             "c": 0,
             "why": "The lemma bounds the distances, not the length: a source with five "
                    "neighbours puts five vertices in the queue at once. On the lesson's graph "
                    "the queue holds c and d together, both at 2, so distances need not strictly "
                    "increase, and later d at 2 with e at 3, so they need not all be equal."},
            {"q": "The preset directed-from-c searches the lesson's records as arcs from c. How "
                  "many adjacency entries does it examine, out of how many?",
             "a": ["2 of 11", "11 of 11", "2 of 22", "3 of 11"],
             "c": 0,
             "why": "Read as arcs, the lists hold 11 entries, one per record. From c the search "
                    "dequeues c (one entry, e), e (one entry, g) and g (none): 2 entries. 22 is "
                    "the undirected total, 11 would mean every list was read, and 3 is the "
                    "number of vertices enqueued, not entries examined."},
        ],
        "mistakes": [
            ("Thinking the breadth-first tree is a property of the graph",
             "The distances are: Theorem 22.5 fixes each one as δ(s, v). The tree is not. It "
             "depends on the order of the adjacency lists, because a vertex takes as parent "
             "whichever neighbour is dequeued first. On the lab's hexagon, vertex 4 is at "
             "distance 3 either way round and gets parent 3 with the edges in the order given; "
             "type the edge from 6 to 1 first and it gets 5."),
            ("Expecting breadth-first search to find shortest weighted paths",
             "Its distance counts edges, with every edge worth 1. Give the edges weights and "
             "the path with fewest edges need not be the lightest. Weighted shortest paths need "
             "Chapter 24's algorithms, which the course reaches in two lessons' time; Dijkstra's "
             "algorithm is breadth-first search's descendant there."),
            ("Assuming the search visits every vertex",
             "Breadth-first search, as the book sets it up, explores from one source and finds "
             "only what that source can reach. On the lesson's graph h and i keep distance ∞, "
             "the lab enqueues 8 of 10 vertices, and their two adjacency entries are never "
             "read. Depth-first search, next, restarts from every vertex still white."),
        ],
        "standard": (
            "Finish when you can run breadth-first search by hand and say what it counts.",
            "For a graph of eight to ten vertices, write the adjacency lists, the queue after "
            "each dequeue, every distance and parent, and the numbers of vertices enqueued and "
            "entries examined."
        ),
        "note": (
            "The lab runs one search with the adjacency order you type and counts what it "
            "enqueues and examines on that graph; it does not build the adjacency matrix, whose "
            "cost the lesson counts by hand. That the distances are right on every graph is "
            "Theorem 22.5, not the run."
        ),
    },
    # ---------------------------------------------------------------- 02
    # CLRS Section 22.3, pp. 603-612.
    # Quote: p. 603, 19 words, quotes.py OK. Lesson total: 19 words.
    # Colours and timestamps (pp. 603-604); Theta(V + E) by aggregate analysis
    # (p. 606); parenthesis theorem 22.7 and Corollary 22.8 (pp. 606-608);
    # white-path theorem 22.9 (p. 608); edge classes and the colour rule
    # (pp. 609-610); Theorem 22.10 (p. 610); Exercise 22.3-8 (p. 611).
    {
        "slug": "depth-first-search",
        "title": "Depth-First Search",
        "module": "Chapter 22 · Elementary Graph Algorithms",
        "one_line": "One walk that goes deeper whenever it can, a clock that ticks twice per vertex, and four classes of edge decided by the times alone.",
        "summary": (
            "Section 22.3 runs a search that always leaves from the most recently discovered "
            "vertex, stamps each vertex with a discovery time and a finish time, and proves that "
            "the intervals between them nest or are disjoint. Run it on a six-vertex digraph, "
            "classify its eight arcs as tree, back, forward and cross, and see which of those "
            "facts belong to the graph and which to the walk."
        ),
        "key": [
            "d when discovered, f when finished",
            "time runs from 1 to 2|V|",
            "intervals nest or are disjoint",
            "white head: tree; grey head: back",
            "black head: forward or cross, by d",
            "undirected: only tree and back",
            "running time: Θ(V + E)",
        ],
        "key_label": "Section 22.3 in seven lines",
        "concepts_intro": (
            "Three ideas carry the section. The rest of Chapter 22 uses each of them as a tool."
        ),
        "concepts": [
            ("Discovery and finish times",
             "A single clock ticks when a vertex is first reached, giving its discovery time "
             "<strong>d</strong>, and again when every edge out of it has been explored, giving "
             "its finish time <strong>f</strong>. With |V| vertices the clock stops at 2|V|. "
             "Between d and f the vertex is grey: open, with a call still running for it."),
            ("The parenthesis theorem",
             "Theorem 22.7: for any two vertices, their intervals [d, f] are either disjoint, "
             "with neither a descendant of the other, or one lies entirely inside the other, "
             "and the inner vertex is a descendant of the outer. Write each discovery as an "
             "opening bracket and each finish as a closing one, and the brackets balance."),
            ("Tree, back, forward and cross edges",
             "A tree edge discovered its head. A back edge runs to an ancestor, a forward edge "
             "to a descendant that is not its child in the tree, and a cross edge to a vertex "
             "that is neither. The colour of the head when the edge is first explored decides "
             "the class: white for tree, grey for back, black for forward or cross."),
        ],
        "read_title": "The section's argument first, then the walk",
        "read_intro": (
            "Read Section 22.3 in your own copy first. The lesson sets out its argument in its "
            "own words and then runs the search on a graph written for the lesson."
        ),
        "body": [
            ("p", "&ldquo;The strategy followed by depth-first search is, as its name implies, "
                  "to search &ldquo;deeper&rdquo; in the graph whenever possible.&rdquo; So "
                  "Section 22.3 of CLRS opens. Breadth-first search, in the lesson before, "
                  "spreads out from one source a layer at a time; depth-first search follows "
                  "one edge after another from the vertex it reached last, and only when that "
                  "vertex has nothing new to offer does it back up to the vertex it came from. "
                  "When everything reachable from the first source is done, it starts again "
                  "from any vertex still untouched, so its result is a forest rather than one "
                  "tree."),
            ("p", "The authors' procedure, DFS with its recursive helper DFS-VISIT, keeps three "
                  "colours as breadth-first search does: white for undiscovered, grey for "
                  "discovered but not finished, black for finished. What it adds is a clock. "
                  "Each time a vertex turns grey the clock ticks and the vertex records the "
                  "time as `d`; each time one turns black the clock ticks again and it records "
                  "`f`. Every vertex is discovered once and finished once, so the times run "
                  "from 1 to 2|V| and `d < f` for every vertex. The section notes that the "
                  "result depends on the order in which the outer loop tries vertices and the "
                  "order of each adjacency list, and that any such order serves."),
            ("p", "The running time is an aggregate count, as for breadth-first search. "
                  "DFS-VISIT is called exactly once per vertex, because the first thing it does "
                  "is turn its vertex grey and it is only ever called on a white one. Inside "
                  "the call, the loop over the adjacency list runs once per entry, and the "
                  "lists hold Θ(E) entries in all. Add the Θ(V) of the outer loops and the "
                  "total is Θ(V + E). The count is exact, not just a bound: one call per "
                  "vertex, one look per adjacency entry."),
            ("p", "Then the properties. The predecessor subgraph is a forest whose shape "
                  "mirrors the recursive calls, and a vertex is a descendant of `u` exactly when "
                  "it was discovered while `u` was grey. From that comes the parenthesis "
                  "theorem: two intervals either do not meet or one contains the other, and "
                  "containment means descent. The proof is two cases on which vertex was "
                  "discovered first and whether the second was discovered before the first "
                  "finished. Corollary 22.8 restates it as a test: `v` is a proper descendant "
                  "of `u` if and only if `d[u] < d[v] < f[v] < f[u]`."),
            ("p", "The white-path theorem, Theorem 22.9, says which vertices end up below `u`: "
                  "exactly those that, at the moment `u` is discovered, can be reached from `u` "
                  "along a path of vertices that are all still white. Reachability alone is not "
                  "enough. A path that runs through a grey or black vertex at that moment does "
                  "not make its far end a descendant, and that is the misconception this "
                  "lesson's graph is built to break."),
            ("p", "Last, the classification. The four classes are defined from the forest, and "
                  "the section shows the search can assign them as it goes: when an edge is "
                  "first explored, a white head makes it a tree edge, a grey head a back edge "
                  "(the grey vertices are always the chain of open calls, so a grey head is an "
                  "ancestor), and a black head a forward edge if the tail was discovered first "
                  "and a cross edge otherwise. For an undirected graph Theorem 22.10 shows that "
                  "forward and cross edges never occur: every edge is a tree edge or a back "
                  "edge."),
            ("p", "Now the lab. It runs the walk in your browser, classifies every arc from the "
                  "two times at its ends, and checks the parenthesis theorem on every pair of "
                  "vertices. It opens on its own preset <code>dag</code>, five arcs on four "
                  "vertices: 0 back arcs and 1 forward arc, and with no back arc the graph is "
                  "acyclic, which the next lesson turns into an algorithm. The preset "
                  "<code>nested</code>, a five-cycle with an extra arc back to 1, has 2 back arcs "
                  "and all 10 pairs of intervals nested; <code>diamond</code> has 3 tree arcs, "
                  "0 forward and 1 cross, and switching the reading to undirected shows the "
                  "cross arc become a tree arc."),
            ("p", "This lesson's graph has six vertices and eight arcs. Paste it into the arcs "
                  "box and start the walk at 1: <code>" + DFS_GRAPH + "</code>. Adjacency lists "
                  "follow the order you type, so vertex 1 tries 2, then 4, then 3. The lab "
                  "prints 4 tree arcs, 1 back arc, 1 forward arc and 2 cross arcs; it finds 5 "
                  "pairs of intervals nested, 10 disjoint, and 0 overlapping without nesting, "
                  "as the theorem says. The intervals are 1 [1, 8], 2 [2, 5], 4 [3, 4], 3 [6, 7], "
                  "5 [9, 12] and 6 [10, 11]: two trees, rooted at 1 and at 5."),
            ("p", "Read the classes off those intervals. `4 → 1` is back, since 4 is inside 1's "
                  "interval and 1 was still grey. `1 → 4` is forward: 4 is a finished descendant "
                  "of 1, reached first through 2. `3 → 4` is cross, because [3, 4] and [6, 7] are "
                  "disjoint, and so is `5 → 3`, which crosses from the second tree into the first. "
                  "Now look at 2 and 3. Vertex 3 is reachable from 2, along `2 → 4`, `4 → 1`, `1 → 3`, "
                  "and it was discovered later, at 6 against 2. Yet [6, 7] is not inside [2, 5]: "
                  "3 is not a descendant of 2, because when 2 was discovered the path ran "
                  "through 1, which was grey. That is the white-path theorem at work."),
            ("p", "Two more runs separate the graph from the walk. Move the start to 5 and the "
                  "lab prints 5 tree arcs, 3 back arcs and no forward or cross arcs at all, with "
                  "11 nested pairs: the same eight arcs, classified differently, because the "
                  "classes describe one walk. Put the start back at 1 and switch the reading to "
                  "undirected: 5 tree edges, 3 back edges, 0 forward, 0 cross, which is Theorem "
                  "22.10 holding on this graph. What does not change is whether there is a back "
                  "arc at all; the next lesson proves that this one fact belongs to the graph."),
            ("p", "The lab does not print the work count, so do it by hand: from root 1 the walk "
                  "makes 6 calls, one per vertex, and examines 8 arcs, one per adjacency entry. "
                  "That is the Θ(V + E) count on this graph, exactly. The Algorithms Subject's "
                  "lesson Depth-First Search and the Timestamps runs the same lab on other "
                  "graphs if you want more practice."),
            ("h3", "Exercise"),
            ("p", "Take the digraph <code>1>2, 2>3, 3>1, 3>4, 4>2, 1>5</code> and run depth-first "
                  "search by hand from 1, with each adjacency list in the order written. Write "
                  "down every interval, classify all six arcs, and find a vertex reachable from "
                  "another and discovered after it that is nevertheless not its descendant, if "
                  "one exists. Then type the graph into the lab and compare."),
            ("p", "A depth-first search with no back arcs is a promise about the graph. The "
                  "next lesson, Topological Sort and Strongly Connected Components, uses that "
                  "promise and the finish times to order a dag and to split any digraph into "
                  "its components."),
        ],
        "lab": ("graphkit", {
            "mode": "dfstimes",
            "preset": "dag",
            "panel_title": "Run the walk, then read the classes off the times",
            "panel_intro": (
                "Type arcs as tail&gt;head, choose where the walk starts, and the lab stamps "
                "each vertex with its discovery and finish times and classifies every arc from "
                "the two times at its ends. The parenthesis theorem is checked on every pair. "
                "Paste the lesson's graph to reproduce its figures."
            ),
        }),
        "steps_title": "Running depth-first search by hand",
        "steps_intro": "Five steps, the last on a graph of your own.",
        "steps": [
            ("Keep a clock and a stack of open vertices",
             "Start the clock at 0. Each time you reach a white vertex, tick and write the time "
             "as its d; it is now grey and on top of the stack of open calls."),
            ("Explore edges in list order",
             "From the vertex on top, take the next untried edge. If its head is white, go "
             "there. If not, note the head's colour for the classification and try the next "
             "edge."),
            ("Finish and back up",
             "When a vertex has no untried edges, tick and write the time as its f, colour it "
             "black and return to the vertex below it. When the stack empties, start again from "
             "the next white vertex."),
            ("Classify every edge",
             "White head: tree. Grey head: back. Black head: forward if the tail's d is smaller, "
             "cross if it is larger. Check that no two intervals overlap without nesting."),
            ("Do it on a graph of your own",
             "Write the import or call graph of a few modules of your own as arcs, run the walk "
             "by hand, then type it into the lab. Note any back arc the lab finds: it closes a "
             "cycle among your modules."),
        ],
        "worked": {
            "title": "The lesson's graph from vertex 1",
            "intro": [
                "Walk the lesson's graph from 1, taking each adjacency list in typed order.",
            ],
            "lines": [
                "open 1 at 1, then 2 at 2, then 4 at 3",
                "4 → 1 meets grey 1: back",
                "close 4 at 4, then 2 at 5",
                "1 → 4 meets black 4, opened later: forward",
                "open 3 at 6; 3 → 4 meets black 4: cross",
                "close 3 at 7, then 1 at 8",
                "root 5 at 9; 5 → 3 cross; 6 from 10 to 11",
                "6 calls, 8 arcs examined",
            ],
            "after": [
                "Four tree arcs (1 → 2, 2 → 4, 1 → 3, 5 → 6), one back, one forward, two cross, as the "
                "lab prints. The count of 6 calls and 8 examinations is the Θ(V + E) bound met "
                "exactly on this graph; the proof is what says it is met on every graph.",
            ],
        },
        "quiz_title": "Timestamps and classes",
        "quiz": [
            {"q": "On the lesson's graph, walked from 1, what class is the arc `5 → 3`?",
             "a": ["Tree", "Back", "Forward", "Cross"],
             "c": 3,
             "why": "When 5 is discovered at time 9, vertex 3 is already black with interval "
                    "[6, 7], which is disjoint from 5's [9, 12]. A black head discovered before "
                    "the tail makes a cross arc. It is not a tree arc, since 3 was not white; "
                    "not back, since 3 is not an ancestor of 5 (5 is a root); and not forward, "
                    "since 3 is not inside 5's interval."},
            {"q": "In one depth-first search, `u` has interval [3, 10] and `v` has [5, 6]. An "
                  "arc runs from `v` to `u`. What class is it?",
             "a": ["Tree", "Back", "Forward", "Cross"],
             "c": 1,
             "why": "[5, 6] lies inside [3, 10], so `v` is a descendant of `u`, and the arc runs "
                    "from the descendant up to its ancestor: a back arc. A tree or forward arc "
                    "would run the other way, from `u` down to `v`, and a cross arc needs "
                    "disjoint intervals."},
            {"q": "Which pair of intervals cannot belong to two vertices of one depth-first "
                  "search?",
             "a": ["[1, 8] and [2, 5]", "[2, 5] and [6, 7]", "[2, 7] and [5, 9]",
                   "[9, 12] and [10, 11]"],
             "c": 2,
             "why": "By the parenthesis theorem two intervals nest or are disjoint. [2, 7] and "
                    "[5, 9] overlap without either containing the other, which cannot happen. "
                    "The first and last pairs nest, and [2, 5] and [6, 7] are disjoint; all "
                    "three appear on the lesson's graph."},
            {"q": "Searching an undirected graph depth first, which edge classes can appear?",
             "a": ["Tree and back only", "Tree, back and cross", "Tree and forward only",
                   "All four, depending on the start"],
             "c": 0,
             "why": "Theorem 22.10: in an undirected graph, when an edge is first explored from "
                    "the endpoint discovered first, the other end is white (a tree edge); if it "
                    "is first explored from the other end, the first end is still grey (a back "
                    "edge). The lab's undirected reading of the lesson's graph prints 5 tree, 3 "
                    "back, 0 forward and 0 cross."},
        ],
        "mistakes": [
            ("Thinking every vertex reachable from u and discovered after it is u's descendant",
             "Reachability plus a later discovery time sounds like descent, and Exercise 22.3-8 "
             "asks for a counterexample. The white-path theorem gives the real condition: the "
             "path must be all white when u is discovered. On the lesson's graph, 3 is "
             "reachable from 2 and discovered later, at 6 against 2, but the path from 2 runs "
             "through 1, which was grey, and 3's interval [6, 7] is not inside 2's [2, 5]."),
            ("Treating the edge classes as properties of the graph",
             "The classes describe one walk. Start the lesson's graph at 1 and the lab prints "
             "4 tree, 1 back, 1 forward and 2 cross arcs; start it at 5 and the same arcs come "
             "out 5 tree, 3 back and nothing else. Whether some back arc exists does not "
             "depend on the walk, and the next lesson proves it; how many, and which, does."),
            ("Expecting depth-first search to produce one tree",
             "Breadth-first search, as the book sets it up, explores from one source. "
             "Depth-first search restarts from every vertex still white, so its predecessor "
             "subgraph is a forest. On the lesson's graph, vertex 5 cannot be reached from 1 "
             "and becomes the root of a second tree, with interval [9, 12]."),
        ],
        "standard": (
            "Finish when you can run depth-first search by hand and classify every edge.",
            "For a digraph of six to eight vertices, write each vertex's interval, classify "
            "every arc by the colour rule, and check the parenthesis theorem on every pair."
        ),
        "note": (
            "The lab runs one walk with the adjacency order you type and the start you choose, "
            "and classifies its arcs; it shows the theorem holding on that walk. It does not "
            "print the call and examination counts, which you count by hand, and it cannot show "
            "that the theorem holds on every graph. The proofs in Section 22.3 do that."
        ),
    },
    # ---------------------------------------------------------------- 03
    # CLRS Sections 22.4-22.5, pp. 612-623.
    # Quote: p. 615, 18 words, quotes.py OK. Lesson total: 18 words.
    # Topological sort definition and TOPOLOGICAL-SORT, Theta(V + E) (pp. 612-613);
    # Lemma 22.11 and Theorem 22.12 (p. 614); Exercise 22.4-5 (in-degree method,
    # p. 615); SCC definition, transpose, Lemma 22.13 (pp. 615-617); f(U),
    # Lemma 22.14, Corollary 22.15, Theorem 22.16 (pp. 617-620).
    {
        "slug": "topological-sort-and-strong-components",
        "title": "Topological Sort and Strongly Connected Components",
        "module": "Chapter 22 · Elementary Graph Algorithms",
        "one_line": "Sort a dag by decreasing finish time, then use the same order on the reversed graph to peel any digraph into its strongly connected components.",
        "summary": (
            "Sections 22.4 and 22.5 put depth-first search to work twice. A dag is sorted by "
            "listing its vertices in decreasing finish time; any digraph is split into strongly "
            "connected components by a second search on its transpose, started in that same "
            "order. Run both on graphs written for the lesson and see why the order of the "
            "second search is the whole algorithm."
        ),
        "key": [
            "dag: no back edge, in any search",
            "sort: decreasing finish time",
            "both run in Θ(V + E)",
            "transpose: every arc reversed",
            "same components in G and its transpose",
            "latest finish: in a source component",
        ],
        "key_label": "Sections 22.4 and 22.5 in six lines",
        "concepts_intro": (
            "Three ideas, each a fact about finish times that one of the two algorithms rests on."
        ),
        "concepts": [
            ("A topological sort",
             "A linear order of a dag's vertices in which every arc points forward, from an "
             "earlier vertex to a later one. A graph with a cycle has none, and a dag usually "
             "has several. Topological sorting arranges vertices, not values, which is why the "
             "authors remark that it differs from the sorting of Part II."),
            ("A strongly connected component",
             "A largest set of vertices in which every vertex can reach every other along "
             "arcs. Each vertex belongs to exactly one. Contract each component to a single "
             "vertex and the resulting component graph is always a dag (Lemma 22.13): two "
             "components that reached each other would be one."),
            ("The transpose",
             "The same vertices with every arc reversed. It has exactly the same strongly "
             "connected components as the original, since mutual reachability survives "
             "reversing every arc, and it can be built from adjacency lists in O(V + E) time."),
        ],
        "read_title": "The sections' argument first, then the two passes",
        "read_intro": (
            "Read Sections 22.4 and 22.5 in your own copy first. The lesson sets out each "
            "argument in its own words, then runs the two-pass algorithm on graphs written for "
            "the lesson."
        ),
        "body": [
            ("p", "&ldquo;We now consider a classic application of depth-first search: "
                  "decomposing a directed graph into its strongly connected components.&rdquo; "
                  "That sentence opens Section 22.5, but Section 22.4 has already shown the "
                  "first application. Both rest on one observation about the finish times "
                  "from the lesson before: along an arc that is not a back arc, the tail "
                  "finishes after the head."),
            ("p", "Section 22.4 starts from a dag, a directed graph with no cycle, and asks for "
                  "a linear order of its vertices with every arc pointing forward. Such orders "
                  "model precedence: tasks before the tasks that need them. The authors' "
                  "TOPOLOGICAL-SORT is three lines of prose in effect: run DFS, and as each "
                  "vertex finishes put it at the front of a list. The list then holds the "
                  "vertices in decreasing finish time. Depth-first search costs Θ(V + E) and "
                  "each insertion at the front costs O(1), so the sort is Θ(V + E)."),
            ("p", "The correctness proof needs Lemma 22.11: a digraph has no cycle exactly when "
                  "one depth-first search of it finds no back edge. One direction is direct, "
                  "since a back edge closes a cycle with the tree path it returns to. For the "
                  "other, take the first vertex of a cycle the search discovers; at that moment "
                  "the rest of the cycle is a white path from it, so by the white-path theorem "
                  "the vertex just before it on the cycle becomes its descendant, and the arc "
                  "back is a back edge. With that, Theorem 22.12 shows that for every arc from "
                  "`u` to `v` in a dag, `f[v] < f[u]`: when the arc is explored, `v` cannot be "
                  "grey, and white or black both finish it before `u`."),
            ("p", "Section 22.5 drops the requirement that the graph be acyclic. Any digraph "
                  "splits into strongly connected components, and the authors' procedure "
                  "STRONGLY-CONNECTED-COMPONENTS finds them with two depth-first searches. The "
                  "first runs on the graph and records finish times. The second runs on the "
                  "transpose, with its outer loop taking vertices in decreasing order of those "
                  "finish times. Each tree of the second forest is one component. Two searches "
                  "and one transpose: Θ(V + E) in all."),
            ("p", "Why that order? The section extends finish times to sets, writing `f(C)` for "
                  "the latest finish of any vertex in a component `C`, and proves Lemma 22.14: "
                  "if an arc runs from component `C` to component `C′`, then `f(C) > f(C′)`. So "
                  "the vertex that finishes last lies in a component with no arcs coming into "
                  "it from other components: a source of the component graph. In the transpose "
                  "every arc out of that component points into it instead, so a search started "
                  "there cannot leave it. Corollary 22.15 carries the argument to every later "
                  "tree, and Theorem 22.16 completes it by induction on the trees found."),
            ("p", "The lab runs both passes in your browser, checks the components against "
                  "mutual reachability computed straight from the definition, and draws the "
                  "condensation, the component graph. It opens on its preset <code>dag</code>, "
                  "four arcs on four vertices: 4 components of 1 vertex each, as an acyclic "
                  "graph must give. The preset <code>three</code> has 3 components, the largest "
                  "with 3 vertices, and 2 arcs in the condensation; <code>onebig</code> is a "
                  "single cycle, 1 component of 4 vertices; <code>sourcefirst</code> has 2 "
                  "components and reports where the latest finish landed: component 1, with 0 "
                  "arcs into it."),
            ("p", "First the sort. Type this lesson's dag, six tasks and six arcs: <code>"
                  + DAG_GRAPH + "</code>. The first pass, listed in decreasing finish time, "
                  "takes 2 (finish 12), 5 (11), 1 (8), 3 (7), 4 (6), 6 (5), and the lab finds "
                  "6 components of one vertex each. Read the vertex column top to bottom: 2, 5, "
                  "1, 3, 4, 6 is the order TOPOLOGICAL-SORT returns. Check each arc: `1 → 3`, "
                  "`2 → 3`, `3 → 4`, `2 → 5`, `5 → 4`, `4 → 6` all point forward in it. Sorting by "
                  "discovery time instead would give 1, 3, 4, 6, 2, 5, and `2 → 3` would point "
                  "backward."),
            ("p", "Now the components. Type this graph of seven vertices and nine arcs: <code>"
                  + SCC_GRAPH + "</code>. The lab prints 4 components, the largest of 3 "
                  "vertices, 4 arcs in the condensation, and agreement with mutual "
                  "reachability. The first pass finishes 7 last, at 14, then 1 at 12, 2 at 11, "
                  "6 at 10, 3 at 8, 4 at 7 and 5 at 6. The second pass, on the reversed arcs, "
                  "peels {7}, then {1, 2, 3}, then {6}, then {4, 5}: two sources, a middle and "
                  "a sink of the condensation. Where did the latest finish land? In component "
                  "1, {7}, with 0 arcs into it, as Lemma 22.14 requires."),
            ("p", "Look at what the order protects against. A search of the original graph from "
                  "7 would follow `7 → 6`, `6 → 4` and `4 → 5` and report {7, 6, 4, 5} as one piece, "
                  "which is wrong: 7 reaches 6, but 6 never reaches 7. In the transpose those "
                  "arcs point the other way, and the search from 7 stops at 7. The latest "
                  "finishing component times are, by component, 14, 12, 10 and 7 in the order "
                  "peeled: decreasing, and that order is itself a topological sort of the "
                  "condensation. The Algorithms Subject's lesson Strongly Connected Components "
                  "has more graphs for the same lab."),
            ("h3", "Exercise"),
            ("p", "Take the digraph <code>1>2, 2>1, 2>3, 3>4, 4>5, 5>3, 5>6, 6>7, 7>6</code>. "
                  "Run the first depth-first search by hand from 1, with vertices and adjacency "
                  "lists in numeric and typed order, list the vertices by decreasing finish "
                  "time, then run the second search on the reversed arcs in that order. Name "
                  "the components and draw the condensation, then type the graph into the lab "
                  "to check."),
            ("p", "The next lesson leaves directed graphs for weighted undirected ones. Minimum "
                  "Spanning Trees: Kruskal and Prim reads Chapter 23, where a greedy choice is "
                  "proved safe by a cut."),
        ],
        "lab": ("graphkit", {
            "mode": "scc",
            "preset": "dag",
            "panel_title": "Two passes: finish times on the graph, then the reversed arcs",
            "panel_intro": (
                "Type arcs as tail&gt;head. The first pass records finish times; the second "
                "runs on the reversed arcs in decreasing finish order, and each of its trees is "
                "one component, checked against mutual reachability. Paste the lesson's dag to "
                "read a topological sort off the first pass."
            ),
        }),
        "steps_title": "Sorting a dag and peeling components",
        "steps_intro": "Five steps, the last on a graph of your own.",
        "steps": [
            ("Run the first search and record finish times",
             "Do depth-first search over every vertex and write each finish time. If you meet a "
             "back edge, the graph has a cycle and no topological sort exists."),
            ("For a dag, list by decreasing finish time",
             "Write the vertices from the latest finish to the earliest. Check that every arc "
             "points from left to right."),
            ("Reverse every arc",
             "Write the transpose: each arc from u to v becomes an arc from v to u. Its "
             "components are the original's."),
            ("Search the transpose in decreasing finish order",
             "Start from the unvisited vertex with the latest first-pass finish, collect "
             "everything the search reaches, and call it a component. Repeat until every vertex "
             "is in one."),
            ("Do it on a graph of your own",
             "Write the dependencies among a dozen tasks or modules of your own as arcs and "
             "type them into the lab. Note how many components there are; any component with "
             "more than one vertex is a dependency cycle."),
        ],
        "worked": {
            "title": "The lesson's seven-vertex graph",
            "intro": [
                "Run the first pass from 1, vertices in numeric order and arcs in typed order.",
            ],
            "lines": [
                "finish times: 5 at 6, 4 at 7, 3 at 8",
                "then 6 at 10, 2 at 11, 1 at 12",
                "7 is a second root, finishing at 14",
                "by finish: 7, 1, 2, 6, 3, 4, 5",
                "transpose from 7: {7}",
                "from 1: {1, 2, 3}; from 6: {6}",
                "from 4: {4, 5}",
            ],
            "after": [
                "Four components, as the lab prints, and the condensation's four arcs run "
                "{7} to {6}, {1, 2, 3} to {6}, {1, 2, 3} to {4, 5} and {6} to {4, 5}. Each "
                "component's latest finish (14, 12, 10, 7) falls along those arcs, which is "
                "Lemma 22.14 on this graph.",
            ],
        },
        "quiz_title": "Orders and components",
        "quiz": [
            {"q": "Which of these is NOT a topological sort of the lesson's dag, "
                  "`1 → 3, 2 → 3, 3 → 4, 2 → 5, 5 → 4, 4 → 6`?",
             "a": ["2, 5, 1, 3, 4, 6", "1, 2, 3, 5, 4, 6", "1, 3, 2, 5, 4, 6",
                   "2, 1, 5, 3, 4, 6"],
             "c": 2,
             "why": "In 1, 3, 2, 5, 4, 6 the arc `2 → 3` points backward, from 2 to a vertex placed "
                    "before it. The other three put every arc's tail before its head. The first "
                    "is the order the lab's first pass gives; the others are valid too, which "
                    "is why a dag can have many topological sorts."},
            {"q": "Why does the second pass of STRONGLY-CONNECTED-COMPONENTS take vertices in "
                  "decreasing first-pass finish time?",
             "a": ["The latest-finishing vertex lies in a sink component, so a search of the "
                   "original graph from it stays inside",
                   "The latest-finishing vertex lies in a source component, and in the "
                   "transpose no arc leaves that component",
                   "Any order works on the transpose; decreasing order only makes the search "
                   "faster",
                   "Decreasing finish time lists each component's vertices consecutively"],
             "c": 1,
             "why": "Lemma 22.14 puts the latest finish in a component with no arcs coming in "
                    "from other components, a source of the component graph. Reversing every "
                    "arc turns its outgoing arcs into incoming ones, so the search cannot "
                    "escape. It is a source, not a sink; another order can merge components; "
                    "and on the lesson's graph the order 7, 1, 2, 6, 3, 4, 5 interleaves "
                    "components."},
            {"q": "On the lesson's seven-vertex graph, how many strongly connected components "
                  "are there, and how many arcs does the condensation have?",
             "a": ["4 components, 4 arcs", "4 components, 9 arcs", "3 components, 3 arcs",
                   "5 components, 4 arcs"],
             "c": 0,
             "why": "The components are {1, 2, 3}, {4, 5}, {6} and {7}. Of the nine arcs, five "
                    "lie inside a component, and the other four join different components. "
                    "Merging 6 with {4, 5} would need a path from 4 back to 6, and there is "
                    "none."},
            {"q": "A depth-first search of a digraph finds 0 back arcs, 1 forward arc and 2 "
                  "cross arcs. What follows?",
             "a": ["The graph has a cycle through the cross arcs",
                   "Nothing yet: another start vertex might find a back arc",
                   "The graph is acyclic and has a topological sort",
                   "The graph is acyclic only if the forward arcs are also removed"],
             "c": 2,
             "why": "Lemma 22.11: a digraph has no cycle exactly when a depth-first search "
                    "finds no back edge, and the lemma is about any one search, so no other "
                    "start can find one. Cross and forward arcs never close a cycle, and "
                    "Theorem 22.12 then gives the sort."},
        ],
        "mistakes": [
            ("Running the second pass on the original graph, or in any order",
             "It is tempting to think the transpose is a detail and any search order will do. "
             "Lemma 22.14 says otherwise: the latest finish lies in a source component, whose "
             "arcs lead out to other components. On the lesson's graph a search of the "
             "original arcs from 7 reaches 6, 4 and 5 and would report them as one component. "
             "Only on the reversed arcs, taken in decreasing finish order, does each search "
             "stop at its component's edge."),
            ("Sorting a dag by discovery time",
             "Discovery time looks like the natural order of a search, but Theorem 22.12 is "
             "about finish times. On the lesson's dag, increasing discovery time gives 1, 3, 4, "
             "6, 2, 5, and the arc `2 → 3` points backward. Decreasing finish time gives 2, 5, 1, "
             "3, 4, 6, and every arc points forward."),
            ("Expecting one topological sort",
             "A dag usually has several. The lesson's dag has 2, 5, 1, 3, 4, 6 from the lab's "
             "first pass, and also 1, 2, 3, 5, 4, 6 and others. The sort is unique only when "
             "consecutive vertices are always joined by an arc, as in a chain."),
        ],
        "standard": (
            "Finish when you can sort a dag and find a digraph's components by hand.",
            "For a digraph of six to nine vertices, list the first-pass finish times, give a "
            "topological sort if the graph is acyclic, and peel the components with the "
            "second pass, naming the condensation's sources and sinks."
        ),
        "note": (
            "The lab runs the two passes with the vertex and adjacency order you type, and "
            "checks the components against mutual reachability on your graph. It shows "
            "Lemma 22.14 holding there. That the latest finish lands in a source on every "
            "graph is the lemma's proof, not a run."
        ),
    },
    # ---------------------------------------------------------------- 04
    # CLRS Sections 23.1-23.2, pp. 624-642.
    # Quote: p. 624, 14 words, quotes.py OK. Lesson total: 14 words.
    # Problem and O(E lg V), Fibonacci-heap Prim (p. 624); GENERIC-MST and its
    # invariant (pp. 625-626); cuts, respect, light edges, Theorem 23.1 and its
    # exchange proof (pp. 626-628); |V| - 1 iterations (p. 628); Corollary 23.2
    # (p. 629); Exercise 23.1-2 (p. 629); Kruskal with disjoint sets, O(E lg V)
    # (pp. 631-633); Prim with a min-priority queue, O(E lg V), O(E + V lg V)
    # (pp. 634-636).
    {
        "slug": "minimum-spanning-trees",
        "title": "Minimum Spanning Trees: Kruskal and Prim",
        "module": "Chapter 23 · Minimum Spanning Trees",
        "one_line": "Grow a spanning tree one safe edge at a time, where a light edge across any cut that respects the edges so far is always safe.",
        "summary": (
            "Chapter 23 grows a minimum spanning tree greedily and proves the greed safe with "
            "one theorem about cuts. Kruskal's algorithm takes edges in increasing weight and "
            "Prim's grows one tree from a root, and both add only edges the theorem calls "
            "safe. Test the theorem on a six-vertex graph written for the lesson against every "
            "one of its 55 spanning trees, and run both algorithms by hand."
        ),
        "key": [
            "a spanning tree has |V| − 1 edges",
            "cut respects A: no edge of A crosses",
            "light edge: least weight across a cut",
            "light edge across such a cut is safe",
            "Kruskal: sorted edges, disjoint sets",
            "Prim: one tree, a min-priority queue",
            "both O(E lg V) with binary heaps",
        ],
        "key_label": "Sections 23.1 and 23.2 in seven lines",
        "concepts_intro": (
            "Three definitions make the chapter's one theorem possible to state."
        ),
        "concepts": [
            ("A safe edge",
             "The generic method keeps a set A of edges that is contained in some minimum "
             "spanning tree. An edge is safe for A if adding it keeps that true. The whole "
             "chapter is a search for a cheap way to recognise safe edges."),
            ("A cut, and a cut that respects A",
             "A cut splits the vertices into a set S and the rest. An edge crosses the cut if "
             "one end is in S and the other is not. A cut respects A if no edge of A crosses "
             "it: the edges chosen so far all lie on one side or the other."),
            ("A light edge",
             "An edge crossing a cut whose weight is the least of all crossing edges. With "
             "ties, a cut can have several light edges, and that is where minimum spanning "
             "trees stop being unique."),
        ],
        "read_title": "The chapter's argument first, then the cut",
        "read_intro": (
            "Read Sections 23.1 and 23.2 in your own copy first. The lesson sets out the "
            "argument in its own words and then tests the cut theorem on a graph written for "
            "the lesson."
        ),
        "body": [
            ("p", "&ldquo;The greedy strategy advocates making the choice that is the best at "
                  "the moment.&rdquo; Chapter 23 of CLRS quotes the strategy of Chapter 16 in "
                  "its first page and then does what Chapter 16 said must always be done: "
                  "prove that the greedy choice is safe. The problem is to connect every vertex "
                  "of a weighted, connected, undirected graph using edges of least total "
                  "weight. The cheapest such set has no cycle, so it is a tree that spans the "
                  "graph, with exactly |V| − 1 edges."),
            ("p", "Section 23.1 states a generic method before either algorithm. Keep a set A "
                  "of edges with one invariant: A lies inside some minimum spanning tree. "
                  "Start with A empty, which satisfies it trivially. While A is not yet a "
                  "spanning tree, find an edge that is safe for A, meaning A plus that edge "
                  "is still inside some minimum spanning tree, and add it. The loop runs |V| − 1 "
                  "times, and at every moment A is a forest. Everything depends on finding a "
                  "safe edge without knowing the tree."),
            ("p", "Theorem 23.1 gives the rule. Take any cut that respects A and any light edge "
                  "crossing it; that edge is safe for A. The proof is an exchange. Let T be a "
                  "minimum spanning tree containing A. If T already holds the light edge, done. "
                  "If not, adding it to T closes a cycle, and that cycle must cross the cut "
                  "somewhere else, at an edge of T that A cannot contain, since no edge of A crosses. "
                  "Swap that edge out for the light one: the result is still a spanning tree, "
                  "and no heavier, so it is minimum too, and it contains A and the light edge."),
            ("p", "Corollary 23.2 is the form both algorithms use: a light edge joining one tree "
                  "of the forest A to a different tree is safe, taking the cut around that one "
                  "tree. Exercise 23.1-2 warns against the converse: a safe edge need not be "
                  "light for every cut that respects A."),
            ("p", "Section 23.2 gives two ways to find such an edge quickly. Kruskal's algorithm "
                  "sorts all the edges by weight and takes them in order, keeping each edge "
                  "whose ends lie in different trees of the forest and skipping each edge "
                  "whose ends are already connected; the authors' MST-KRUSKAL decides that with "
                  "the disjoint-set forest of Chapter 21, one FIND-SET per end and a UNION per "
                  "edge kept. Sorting costs O(E lg E), the set operations are cheaper, and since "
                  "E is less than V², lg E is O(lg V): O(E lg V) in all."),
            ("p", "Prim's algorithm grows a single tree from a root. Each vertex outside the tree "
                  "carries a key, the weight of its lightest edge to the tree, in a "
                  "min-priority queue; the procedure MST-PRIM repeatedly extracts the vertex "
                  "of least key, adds it with that edge, and lowers the keys of its neighbours. "
                  "With a binary heap the |V| extractions and up to |E| key decreases cost "
                  "O(E lg V); with a Fibonacci heap, whose decrease-key is O(1) amortized, "
                  "O(E + V lg V). Each step adds a light edge across the cut around the tree, "
                  "so Corollary 23.2 again calls it safe."),
            ("p", "The lab tests the theorem rather than stating it. You type a weighted graph "
                  "and the set S on one side of a cut; it lists the crossing edges, finds the "
                  "lightest, enumerates every spanning tree of the graph (it can, up to seven "
                  "vertices), and reports whether the light edge is in some minimum tree and in "
                  "every one. It opens on its preset <code>distinct</code>, seven edges with "
                  "distinct weights: 2 edges cross, 1 minimum tree of weight 17, and the light "
                  "edge is in every minimum tree. The preset <code>tie</code> has 2 crossing "
                  "edges tied at the lightest, 2 minimum trees of weight 7; <code>cycle</code> "
                  "shows a cycle's heaviest edge left out of the 1 minimum tree, of weight 6."),
            ("p", "This lesson's graph has six vertices, nine edges and one tie: <code>"
                  + MST_GRAPH + "</code>. Type it, with S set to <code>1, 3</code>. The lab "
                  "finds 4 edges crossing the cut, 2 of them tied at the lightest weight 3 "
                  "(`1–2` and `2–3`); it lists all 55 spanning trees, of which 2 have the "
                  "minimum weight 12; and it reports that the light edge `1–2` is in at least "
                  "one minimum tree but not in every one. That is exactly the theorem's "
                  "promise. It says a light edge is safe, which means some minimum tree holds "
                  "it; with a tie, the other light edge `2–3` is in the other tree."),
            ("p", "The table of every edge says more. `1–3`, `2–4`, `5–6` and `3–5` are in every "
                  "minimum tree; `4–5`, `4–6` and `3–4` are in none, each being the heaviest "
                  "edge on some cycle. The lab also takes each vertex's own lightest edge, a "
                  "safe edge by Corollary 23.2, and finds that together they make 3 edges of "
                  "weight 5, leaving the graph in 3 pieces: safe edges, but not yet a tree."),
            ("p", "Run Kruskal's algorithm by hand on the same graph, taking tied edges in typed "
                  "order. Sorted: `1–3` 1, `2–4` 2, `5–6` 2, `1–2` 3, `2–3` 3, `3–5` 4, then 5, 6 "
                  "and 7. Keep `1–3`, `2–4`, `5–6` and `1–2`; skip `2–3`, whose ends are now "
                  "joined; keep `3–5`; skip the last three. Five edges, weight 12. Prim's "
                  "algorithm from 1 adds `1–3` (key 1), then one of the two edges of weight 3, "
                  "then `2–4`, `3–5` and `5–6`: weight 12 again. The Algorithms Subject's lessons "
                  "The Cut Property, Kruskal's Algorithm and Prim's Algorithm run each step in "
                  "its own lab."),
            ("h3", "Exercise"),
            ("p", "Take the graph <code>1-2 2, 1-3 2, 2-3 1, 2-4 4, 3-4 3, 3-5 5, 4-5 2</code>. "
                  "Run Kruskal's algorithm and Prim's algorithm from 1 by hand, listing each "
                  "edge kept and the cut that makes it light. Is the minimum spanning tree "
                  "unique? Check your answer by typing the graph into the lab with S set to "
                  "<code>1</code>, then <code>1, 2, 3</code>."),
            ("p", "Spanning trees connect everything cheaply; shortest paths connect one vertex "
                  "to each other vertex cheaply, and the two are different problems. The next "
                  "lesson, Bellman-Ford and Shortest Paths in DAGs, opens Chapter 24."),
        ],
        "lab": ("graphkit", {
            "mode": "cutproperty",
            "preset": "distinct",
            "panel_title": "Choose a cut, then check its light edge against every tree",
            "panel_intro": (
                "Type weighted edges as one-other w and the vertices on one side of the cut. "
                "The lab finds the crossing edges and the lightest, lists every spanning tree, "
                "and says whether the light edge is in some minimum tree and in every one. "
                "Paste the lesson's graph with S set to 1, 3."
            ),
        }),
        "steps_title": "Finding safe edges by hand",
        "steps_intro": "Five steps, the last on a graph of your own.",
        "steps": [
            ("Pick a cut that respects A",
             "Write a set S so that no edge already chosen has one end in S and one outside. "
             "At the start, with nothing chosen, every cut respects A."),
            ("List the crossing edges and find the light ones",
             "Write every edge with exactly one end in S and its weight. The least weight marks "
             "the light edges; if two tie, either is safe."),
            ("Run Kruskal's order",
             "Sort the edges by weight, then keep each edge whose ends are in different trees "
             "of the forest so far and skip each edge that would close a cycle."),
            ("Run Prim's order",
             "From a root, repeatedly add the lightest edge from the tree to a vertex outside "
             "it, and update the keys of that vertex's neighbours."),
            ("Do it on a graph of your own",
             "Draw six to seven places you could link, such as rooms to cable or offices to "
             "network, with costs, and type the graph into the lab. Choose two different cuts "
             "and note whether each light edge is in every minimum tree."),
        ],
        "worked": {
            "title": "Kruskal on the lesson's graph",
            "intro": [
                "Sort the nine edges by weight, ties in typed order, and keep or skip each.",
            ],
            "lines": [
                "1–3 at 1: keep; 2–4 at 2: keep",
                "5–6 at 2: keep; 1–2 at 3: keep",
                "2–3 at 3: skip, 2 and 3 joined",
                "3–5 at 4: keep; five edges now",
                "4–5, 4–6, 3–4: skip",
                "weight 1 + 2 + 2 + 3 + 4 = 12",
            ],
            "after": [
                "Five edges of weight 12, matching the lab's minimum. Had `2–3` come before "
                "`1–2` in the order, Kruskal would have kept it instead, giving the other "
                "minimum tree the lab lists, also of weight 12.",
            ],
        },
        "quiz_title": "Cuts, light edges and safe edges",
        "quiz": [
            {"q": "On the lesson's graph with S = {1, 3}, which edges are light for the cut?",
             "a": ["`1–3` only", "`1–2` and `2–3`", "`1–2`, `2–3` and `3–5`", "`3–4` only"],
             "c": 1,
             "why": "The crossing edges are `1–2` (3), `2–3` (3), `3–5` (4) and `3–4` (7). The "
                    "least weight is 3, shared by `1–2` and `2–3`. `1–3` has both ends in S and "
                    "does not cross; `3–5` crosses but is heavier."},
            {"q": "With A = {`1–3`, `2–4`} on the lesson's graph, which set S gives a cut that "
                  "respects A?",
             "a": ["{1, 2}", "{1, 4}", "{1, 3}", "{3, 4}"],
             "c": 2,
             "why": "A cut respects A when no edge of A crosses it. With S = {1, 3}, `1–3` lies "
                    "inside S and `2–4` outside it. {1, 2} and {1, 4} split `1–3` and `2–4`, "
                    "and {3, 4} splits both."},
            {"q": "Which statement is Theorem 23.1?",
             "a": ["A light edge crossing a cut that respects A is safe for A",
                   "An edge safe for A is light for every cut that respects A",
                   "The lightest edge in the graph is in every minimum spanning tree",
                   "The heaviest edge in the graph is in no minimum spanning tree"],
             "c": 0,
             "why": "The theorem goes from light to safe. The converse fails (Exercise 23.1-2). "
                    "With ties the lightest edge is in some minimum tree but need not be in "
                    "every one, and a heaviest edge that is the only link to a vertex must be in "
                    "every spanning tree."},
            {"q": "How many minimum spanning trees does the lesson's graph have, and of what "
                  "weight?",
             "a": ["1, of weight 12", "2, of weight 12", "2, of weight 15", "55, of weight 12"],
             "c": 1,
             "why": "The lab lists 55 spanning trees, and 2 of them reach the minimum weight 12: "
                    "one with `1–2`, one with `2–3`, the two tied light edges of the cut "
                    "S = {1, 3}. The other 53 are heavier."},
        ],
        "mistakes": [
            ("Thinking a light edge must be in every minimum spanning tree",
             "The theorem says a light edge is safe: some minimum spanning tree containing A "
             "also contains it. With ties that is weaker than every tree. On the lesson's "
             "graph the lab lists 2 minimum trees of weight 12 and finds the light edge `1–2` "
             "in only 1 of them; its tied rival `2–3` is in the other."),
            ("Taking every vertex's lightest edge and calling it a tree",
             "Each vertex's lightest edge is safe by Corollary 23.2, so it is tempting to take "
             "them all at once. On the lesson's graph they are 3 edges of weight 5 and leave "
             "the graph in 3 pieces. The generic method needs |V| − 1 edges and keeps choosing "
             "until the forest is one tree."),
            ("Expecting Kruskal and Prim to return the same tree",
             "They return trees of the same weight, but where weights tie they may choose "
             "different edges. On the lesson's graph Kruskal with ties in typed order keeps "
             "`1–2`. Prim rooted at 3 gives vertex 2 the key 3 through `2–3` first, and when 1 "
             "joins, `1–2` offers 3 again, which is not smaller, so it keeps `2–3`. Both trees "
             "weigh 12."),
        ],
        "standard": (
            "Finish when you can find a safe edge from a cut and run both algorithms by hand.",
            "For a weighted graph of six or seven vertices, name a cut that respects a given "
            "A, its light edges, and the edges Kruskal's and Prim's algorithms add, with the "
            "total weight."
        ),
        "note": (
            "The lab enumerates every spanning tree, so on a graph of seven or fewer vertices "
            "its verdict on the light edge is complete for that graph. It does not take a set A, "
            "so it tests cuts against an empty A; the theorem for every A and every graph is "
            "the exchange proof in Section 23.1."
        ),
    },
    # ---------------------------------------------------------------- 05
    # CLRS Chapter 24 introduction and Sections 24.1-24.2, pp. 643-658.
    # Quote: p. 655, 21 words, quotes.py OK. Lesson total: 21 words.
    # delta(u, v), variants, Lemma 24.1, negative edges and cycles,
    # representing paths, relaxation, the properties listed (pp. 643-650);
    # BELLMAN-FORD, |V| - 1 passes, O(VE), Lemma 24.2, Theorem 24.4
    # (pp. 651-654); DAG-SHORTEST-PATHS, Theta(V + E), Theorem 24.5, PERT
    # critical paths (pp. 655-657).
    {
        "slug": "bellman-ford-and-dag-shortest-paths",
        "title": "Bellman-Ford and Shortest Paths in DAGs",
        "module": "Chapter 24 · Single-Source Shortest Paths",
        "one_line": "Relax every edge |V| − 1 times and the shortest paths are found unless a negative cycle is reachable; in a dag one pass in topological order is enough.",
        "summary": (
            "Chapter 24 opens with the one operation every shortest-path algorithm shares, "
            "relaxing an edge, and Sections 24.1 and 24.2 apply it in two orders. Bellman-Ford "
            "relaxes every edge in rounds and detects a negative cycle; the dag algorithm "
            "relaxes each edge once, in topological order. Run both on a five-vertex graph "
            "with three negative arcs and count the rounds and the relaxations."
        ),
        "key": [
            "relax: d[v] > d[u] + w lowers d[v]",
            "d[v] never falls below δ(s, v)",
            "|V| − 1 rounds fix every simple path",
            "one more improvement: negative cycle",
            "Bellman-Ford: O(V·E)",
            "dag: topological order, Θ(V + E)",
        ],
        "key_label": "Sections 24.1 and 24.2 in six lines",
        "concepts_intro": (
            "Three ideas from the chapter's introduction carry every algorithm in it."
        ),
        "concepts": [
            ("Shortest-path weight",
             "The least total weight δ(u, v) of any path from u to v, or infinity when there is "
             "none. Weights may be negative. If a cycle of negative total weight can be reached "
             "on the way, going round it again always helps, and the authors set δ to minus "
             "infinity for every vertex beyond it."),
            ("Relaxation",
             "Each vertex keeps an estimate d, infinity at first and 0 at the source. Relaxing "
             "the arc from u to v asks whether going through u improves v: if d[u] plus the "
             "arc's weight is less than d[v], lower d[v] to it and record u as v's "
             "predecessor. The algorithms of Chapter 24 differ only in which arcs they relax and "
             "in what order."),
            ("The upper-bound and path-relaxation properties",
             "Relaxation never makes d[v] smaller than δ(s, v), and once equal it stays equal. "
             "If the arcs of a shortest path are relaxed in path order, with anything else "
             "relaxed in between, d at the path's end becomes exact. Section 24.5 proves both."),
        ],
        "read_title": "The chapter's argument first, then the rounds",
        "read_intro": (
            "Read the introduction to Chapter 24 and Sections 24.1 and 24.2 in your own copy "
            "first. The lesson sets out the argument in its own words, then runs both "
            "algorithms on a graph written for the lesson."
        ),
        "body": [
            ("p", "&ldquo;Shortest paths are always well defined in a dag, since even if there "
                  "are negative-weight edges, no negative-weight cycles can exist.&rdquo; That "
                  "sentence from Section 24.2 states the chapter's real worry. A negative edge "
                  "is not a problem in itself. A negative cycle reachable from the source is, "
                  "because no path through it is ever the cheapest. Chapter 24 asks for the "
                  "shortest path from one source to every vertex, and its introduction sets out "
                  "the vocabulary every algorithm in it uses."),
            ("p", "First the problem. A path's weight is the sum of its arcs' weights, and "
                  "δ(s, v) is the least weight over all paths from s to v. Lemma 24.1 gives the "
                  "optimal substructure: any part of a shortest path is itself a shortest path "
                  "between its ends. A shortest path can be taken to be simple, since removing a "
                  "cycle of nonnegative weight never hurts, so it has at most |V| − 1 arcs. The "
                  "answer is kept as a predecessor for each vertex, and the predecessors form a "
                  "shortest-paths tree rooted at s."),
            ("p", "Then the operation. INITIALIZE-SINGLE-SOURCE sets every estimate `d[v]` to "
                  "infinity, `d[s]` to 0 and every predecessor to nil; RELAX on an arc from `u` "
                  "to `v` lowers `d[v]` to `d[u] + w` when that is smaller. The introduction "
                  "lists the properties relaxation has, and Section 24.5 proves them: `d[v]` "
                  "never drops below δ(s, v) and never rises; relaxing the arcs of a shortest "
                  "path in order, with any other relaxations interleaved, makes the last "
                  "estimate exact. Every algorithm in the chapter is a schedule of relaxations "
                  "that guarantees that order."),
            ("p", "Section 24.1's Bellman-Ford algorithm is the bluntest schedule. Make |V| − 1 "
                  "passes, and in each pass relax every arc once, in any fixed order. Pass `i` "
                  "relaxes the `i`-th arc of every shortest path at the latest, so by the "
                  "path-relaxation property every estimate is exact after |V| − 1 passes "
                  "(Lemma 24.2). Then one more look at every arc: if any arc could still lower "
                  "an estimate, a negative cycle is reachable, and the procedure returns FALSE; "
                  "otherwise it returns TRUE with the distances (Theorem 24.4). |V| − 1 passes "
                  "over E arcs make the running time O(VE)."),
            ("p", "Section 24.2 shows that on a dag one pass is enough. Sort the vertices "
                  "topologically, as in the lesson before last, and relax the arcs leaving each "
                  "vertex as you reach it in that order. Every path visits its vertices in "
                  "topological order, so every shortest path has its arcs relaxed in path "
                  "order, and Theorem 24.5 follows from path relaxation. The sort is Θ(V + E) "
                  "and each arc is relaxed once: Θ(V + E) in all. The section's application is "
                  "the critical path of a PERT chart, the longest path, found by negating the "
                  "weights."),
            ("p", "The lab runs Bellman-Ford in your browser, table by round, and checks its "
                  "answer against an all-pairs matrix computed another way. One difference from "
                  "the book's procedure: it stops as soon as a round changes nothing, and "
                  "counts the checking pass among the |V| rounds it allows. It counts a "
                  "relaxation only when the arc's tail already has a finite label. It opens on "
                  "its preset <code>worstorder</code>, a chain typed backwards: 6 of the 6 "
                  "allowed rounds and 20 relaxations. The preset <code>bestorder</code>, the "
                  "same chain typed forwards, needs 2 of the 6 and 10 relaxations; "
                  "<code>negcycle</code> reports the negative cycle 2 → 3 → 4 → 2 itself."),
            ("p", "This lesson's graph has five vertices, seven arcs, three of them negative, "
                  "and no cycle: <code>" + BF_GRAPH + "</code>, with labels from 1. The lab "
                  "runs 3 of the 5 allowed rounds and 21 relaxations, finds no negative cycle, "
                  "and agrees with the all-pairs matrix. After round 1 the labels are 0, 2, 5, "
                  "2, 4; after round 2 they are 0, 2, 5, 0, 2, and round 3 changes nothing. The "
                  "longest shortest path, 1 → 3 → 2 → 4 → 5, has 4 arcs, and every label was "
                  "final no later than its own path's arc count, as the induction says; 2 of "
                  "the 5 exactly at it."),
            ("p", "Now type the same arcs in the reverse order: <code>" + BF_REVERSED + "</code>. "
                  "The lab needs 4 of the 5 rounds. The distances are the same and the bound of "
                  "|V| − 1 = 4 changing passes still holds, but the arc order decides how close "
                  "a run comes to it. The book's procedure would make all 4 passes regardless, "
                  "28 calls to RELAX, and then its check of 7 arcs. Finally add one arc, "
                  "<code>5>3 -1</code>, to the original: the lab reports the negative cycle "
                  "2 → 4 → 5 → 3 → 2, of weight −4, and refuses to call anything a distance."),
            ("p", "The graph is a dag, so do Section 24.2 by hand. A topological order is 1, 3, "
                  "2, 4, 5. From 1: `d[2]` becomes 4 and `d[3]` 5. From 3: `d[2]` falls to 2 "
                  "and `d[4]` becomes 8. From 2: `d[4]` falls to 0 and `d[5]` becomes 8. From 4: "
                  "`d[5]` falls to 2. Seven relaxations, one per arc, and the same distances, "
                  "0, 2, 5, 0, 2, with three negative arcs on the way. The Algorithms Subject's "
                  "lessons Negative Weights and Bellman–Ford and Shortest and Longest Paths in "
                  "a DAG take both further."),
            ("h3", "Exercise"),
            ("p", "Take the arcs <code>1>2 6, 1>3 2, 3>2 3, 2>4 -4, 3>4 5, 4>5 1, 3>5 4</code> "
                  "from source 1. Run Bellman-Ford by hand with the arcs in that order, writing "
                  "the labels after each pass, then run the dag algorithm in a topological "
                  "order. Count the relaxations each needs, and check against the lab."),
            ("p", "Bellman-Ford pays for its generality with O(VE). The next lesson, Dijkstra's "
                  "Algorithm and Difference Constraints, gives up negative weights to relax "
                  "each arc only once on any graph."),
        ],
        "lab": ("graphkit", {
            "mode": "bellmanford",
            "preset": "worstorder",
            "panel_title": "Relax every arc, round after round",
            "panel_intro": (
                "Type weighted arcs as tail&gt;head w, negatives allowed, and a source. The lab "
                "relaxes every arc each round until a round changes nothing, prints the table, "
                "and reports a negative cycle as the cycle itself. Paste the lesson's graph from "
                "source 1, then the same arcs reversed."
            ),
        }),
        "steps_title": "Running Bellman-Ford and the dag pass by hand",
        "steps_intro": "Five steps, the last on a graph of your own.",
        "steps": [
            ("Initialise",
             "Set every estimate to infinity, the source's to 0, and every predecessor to "
             "nil."),
            ("Relax every arc, in a fixed order, per pass",
             "For each arc from u to v with u's estimate finite, lower v's estimate to u's plus "
             "the weight if that is smaller. Write the row of estimates after each pass."),
            ("Stop at |V| − 1 passes and check",
             "After |V| − 1 passes, look at every arc once more. If any could still lower an "
             "estimate, a negative cycle is reachable and there are no distances."),
            ("On a dag, sort first and relax once",
             "Put the vertices in a topological order and relax the arcs out of each vertex in "
             "that order: one relaxation per arc."),
            ("Do it on a graph of your own",
             "Write a small schedule or currency table of your own as weighted arcs, with at "
             "least one negative weight, and type it into the lab. Note the rounds it needs, "
             "then reverse the arc order and note them again."),
        ],
        "worked": {
            "title": "Round 1 on the lesson's graph",
            "intro": [
                "Relax the seven arcs in typed order, starting from 0 at vertex 1.",
            ],
            "lines": [
                "1 → 2: d[2] = 0 + 4 = 4",
                "1 → 3: d[3] = 0 + 5 = 5",
                "2 → 4: d[4] = 4 − 2 = 2",
                "3 → 2: d[2] = 5 − 3 = 2",
                "3 → 4: 5 + 3 = 8 is not below 2",
                "4 → 5: d[5] = 2 + 2 = 4",
                "2 → 5: 2 + 6 = 8 is not below 4",
                "after round 1: 0, 2, 5, 2, 4",
            ],
            "after": [
                "Round 2 lowers `d[4]` to 0 through the improved `d[2]`, and then `d[5]` to 2. "
                "Round 3 finds nothing to lower, which is where the lab stops. The book's "
                "procedure would run a fourth pass and then its check.",
            ],
        },
        "quiz_title": "Rounds, cycles and the dag pass",
        "quiz": [
            {"q": "On the lesson's graph, relaxing arcs in typed order from source 1, what are "
                  "the labels of vertices 1 to 5 after round 1?",
             "a": ["0, 4, 5, 2, 4", "0, 2, 5, 2, 4", "0, 2, 5, 0, 2", "0, 4, 5, 8, 6"],
             "c": 1,
             "why": "Within round 1, `2 → 4` uses `d[2]` = 4 to set `d[4]` = 2, then `3 → 2` lowers "
                    "`d[2]` to 2, and `4 → 5` sets `d[5]` = 4. 0, 4, 5, 2, 4 forgets the `3 → 2` "
                    "relaxation that comes later in the same round. 0, 2, 5, 0, 2 is the state "
                    "after round 2."},
            {"q": "Why are |V| − 1 passes enough when no negative cycle is reachable?",
             "a": ["Each pass settles at least one more vertex for good",
                   "A shortest path can be taken simple, so it has at most |V| − 1 arcs, and "
                   "pass i relaxes its i-th arc at the latest",
                   "Each pass halves the largest error in any estimate",
                   "After |V| − 1 passes every arc has been relaxed |V| − 1 times, which is "
                   "the most any estimate can change"],
             "c": 1,
             "why": "Lemma 24.2 rests on the path-relaxation property: once a shortest path's "
                    "arcs have been relaxed in order, its end is exact. A simple path has at "
                    "most |V| − 1 arcs, and each pass relaxes every arc. A pass need not "
                    "settle any particular vertex, and an estimate can change more often than "
                    "the number of passes."},
            {"q": "Which one arc, added to the lesson's graph, makes Bellman-Ford from 1 return "
                  "FALSE?",
             "a": ["5 → 3, weight 4", "5 → 1, weight −1", "4 → 1, weight 1", "5 → 3, weight −1"],
             "c": 3,
             "why": "An arc 5 → 3 of weight −1 closes 3 → 2 → 4 → 5 → 3 with weight −3 − 2 + 2 − 1 = −4. Weight 4 instead "
                    "makes that cycle +1. An arc 5 → 1 of weight −1 makes cycles through 1 of weight at least 1 "
                    "(1 → 3 → 2 → 4 → 5 → 1 is 5 − 3 − 2 + 2 − 1 = 1), and 4 → 1 of weight 1 makes "
                    "1 → 3 → 2 → 4 → 1 of weight 1. A negative arc alone does not make a "
                    "negative cycle."},
            {"q": "How many relaxations does the dag algorithm of Section 24.2 perform on the "
                  "lesson's graph?",
             "a": ["5", "7", "21", "28"],
             "c": 1,
             "why": "It relaxes the arcs leaving each vertex once, in topological order, so "
                    "each of the 7 arcs once. 21 is the lab's Bellman-Ford count over 3 "
                    "rounds, 28 the book's Bellman-Ford over 4 passes, and 5 is the number of "
                    "vertices."},
        ],
        "mistakes": [
            ("Thinking a negative weight makes shortest paths undefined",
             "What breaks shortest paths is a negative cycle reachable from the source, "
             "because going round it again always lowers the total. The lesson's graph has "
             "three negative arcs and no cycle at all, and the lab finds every distance: 0, 2, "
             "5, 0, 2. Add an arc 5 → 3 of weight −1 and a cycle of weight −4 appears, and only then are there "
             "no distances."),
            ("Expecting Bellman-Ford to need all |V| − 1 rounds on every graph",
             "|V| − 1 passes is the bound the proof needs for the worst order. The lab, which "
             "stops when a round changes nothing, finishes the lesson's graph in 3 rounds "
             "typed one way and 4 the other, and its own presets go from 2 rounds to 6 on one "
             "chain. The book's procedure always runs all |V| − 1 passes, which is why its "
             "bound is Θ(VE) on every input rather than only the worst."),
            ("Believing the dag algorithm needs nonnegative weights",
             "It needs no cycle, not nonnegative weights. Its proof is the path-relaxation "
             "property, which holds whatever the signs. The by-hand pass over the lesson's "
             "graph meets three negative arcs and still returns the distances Bellman-Ford "
             "finds, in 7 relaxations rather than 21."),
        ],
        "standard": (
            "Finish when you can run Bellman-Ford and the dag pass by hand.",
            "For a weighted digraph of five or six vertices, write the estimates after each "
            "pass, say whether a negative cycle is reachable, and give the dag algorithm's "
            "relaxations when the graph is acyclic."
        ),
        "note": (
            "The lab stops early where the book's procedure always makes |V| − 1 passes, and "
            "counts only relaxations from a finite tail, so its counts are smaller than the "
            "book's. It shows how many rounds this graph and this order need; the bound for "
            "every graph is Lemma 24.2's proof."
        ),
    },
]
