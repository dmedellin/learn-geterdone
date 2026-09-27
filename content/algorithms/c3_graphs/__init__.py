"""Graph Algorithms."""


from . import part_a, part_b


COURSE = {
    "slug": "graph-algorithms",
    "title": "Graph Algorithms",
    "level": "Advanced",
    "summary": (
        "What one depth-first walk writes down and the four things read off it, the single "
        "lemma both minimum spanning tree algorithms rest on, shortest paths as one relaxation "
        "step applied on three schedules, and flow, where the algorithm stops only when it can "
        "hand back a proof that it is finished."
    ),
    "blurb": (
        "Discrete Mathematics defined graphs and ran two algorithms on them. This course builds "
        "eleven, proves each correct, and counts what each one does on the graph you type. It is "
        "also where an algorithm first certifies its own answer: everywhere else on this path a "
        "lesson puts a measured count beside a proved bound, and here the maximum flow comes "
        "back with a cut of equal capacity attached."
    ),
    "key": [
        "d[v], f[v]      two times per vertex; the intervals nest or are disjoint",
        "low[v] > d[u]   the tree edge above v is a bridge",
        "cut property    the lightest edge leaving S is in some minimum spanning tree",
        "relax(u, v)     d[v] = min(d[v], d[u] + w)      the whole of shortest paths",
        "max flow = min cut      the failed search IS the certificate",
    ],
    "assumes_short": "Graphs and trees, heaps, union-find, big-O",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: Graphs and Graph Models, Graph "
        "Representations, Paths and Connectivity, Bipartite Graphs, Breadth-First and "
        "Depth-First Search, Shortest Paths and Dijkstra's Algorithm, Trees, Spanning Trees and "
        "Minimum Spanning Trees, Big-O, Big-Omega and Big-Theta, Analysing Iterative Algorithms, "
        "Loop Invariants and Program Correctness, and Strong Induction; and from the data "
        "structures course on this path, Priority Queues and Binary Heaps and Union–Find, "
        "whose costs are quoted here and re-derived nowhere"
    ),
    "outcomes_intro": (
        "By the end you can read four different facts off one traversal, justify every edge a "
        "minimum-tree algorithm takes by naming a cut, choose a shortest-path method from what "
        "the weights and the cycles allow, and produce the certificate that proves a flow "
        "maximum."
    ),
    "outcomes": [
        ("Read a graph from one walk",
         "Discovery and finish times, the four edge classes, bridges and cut vertices, "
         "topological order and strongly connected components &mdash; each one arithmetic on the "
         "same two numbers, and each with the count it cost."),
        ("Justify an edge by naming a cut",
         "State and prove the cut and cycle properties, then show that both minimum-tree "
         "algorithms are the same lemma with a different rule for choosing the cut &mdash; and "
         "say whether the tree you found is the only one."),
        ("Choose a shortest-path method from the input",
         "Nearest-first where no weight is negative, rounds where they are, one pass where there "
         "are no cycles at all; and in each case say what the method assumes rather than what it "
         "costs."),
        ("Produce a certificate, not just an answer",
         "Run the augmenting-path method, read the minimum cut off the search that failed, check "
         "its capacity against the flow's value, and translate both back into a matching and a "
         "vertex cover."),
    ],
    "syllabus_intro": (
        "One traversal first, because four of the thirteen results are it read differently; then "
        "weights, and the lemma that justifies a greedy choice; then shortest paths, as one step "
        "under three schedules and two special cases; then flow, where the certificate arrives "
        "with the answer."
    ),
    "how_to": [
        "Move the starting vertex before you write a number down. The class of an arc, the work "
        "a heap does and the number of rounds a sweep needs all change with where the algorithm "
        "began; the distances, the tree weight and the flow value do not. Every lab on this "
        "course lets you move it, and the split between what moves and what does not is the "
        "course's main lesson about measurement.",
        "Read a schedule as a separate thing from the step it schedules. &ldquo;Relaxation and "
        "Dijkstra's Schedule&rdquo;, &ldquo;Negative Weights and Bellman&ndash;Ford&rdquo; and "
        "&ldquo;Shortest and Longest Paths in a DAG&rdquo; perform identical arithmetic in three "
        "orders; what separates them is what each order assumes about the input.",
        "Distrust a run that merely stopped. Three lessons here turn on the difference between "
        "&ldquo;my search found nothing more&rdquo; and &ldquo;nothing more exists&rdquo; "
        "&mdash; a maximal matching, a maximal flow, and a greedy pass that is neither. Only "
        "&ldquo;Max Flow and Min Cut&rdquo; closes that gap, and it closes it with an object you "
        "can check by hand.",
    ],
    "not_covered": [
        "All-pairs shortest paths. The one-source methods here are enough for every claim the "
        "course makes, and filling a whole matrix is a dynamic program over which interior "
        "vertices are allowed &mdash; a shape this path develops later rather than here.",
        "Modelling transformations on flow networks: splitting a vertex to cap what passes "
        "through it, unit capacities to count arc-disjoint routes, a super-source over several "
        "starts. They change the network and not the algorithm, and the catalogue is a separate "
        "skill from proving an algorithm correct.",
        "Preflow-push, capacity scaling and the polynomial bounds on the number of "
        "augmentations. The augmenting-path method is developed and counted; how many "
        "augmentations it needs in the worst case is stated nowhere here.",
        "Tarjan's one-pass strongly connected components, and Fibonacci heaps. Both are "
        "improvements on algorithms this course builds, neither changes a correctness argument, "
        "and the second changes a bound no lesson here depends on.",
    ],
    "footer_lead": (
        "Every count on this course is produced by running the algorithm on the graph you typed. "
        "Distances, weights, low-links, cut capacities, matching sizes and component counts are "
        "integers, and no page here rounds anything. Three claims are checked against an "
        "independently written implementation from another Subject &mdash; bridges against "
        "delete-and-recount, the minimum tree against a second method, and the distances against "
        "a Dijkstra that knows nothing about this representation &mdash; and where a reader's "
        "graph has two edges between the same pair, that check declines rather than answering "
        "about a different graph. Four more are checked against a complete enumeration at a cap "
        "the page states: every spanning tree, every topological order, every cut, every subset "
        "of the pairs. Two columns are labelled for reference and carry no verdict: `E` times "
        "the integer part of `log₂ V`, on the two pages that print it."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
