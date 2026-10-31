"""Course 6 -- Graph Algorithms: Part VI of Introduction to Algorithms, Chapters 22-26.

Nine lessons in five modules: part_a reads Chapter 22 (representations,
breadth-first and depth-first search, topological sort and strongly connected
components) and Chapter 23 (minimum spanning trees); part_b reads Chapters 24,
25 and 26 (single-source and all-pairs shortest paths, maximum flow and
bipartite matching). Section numbers are to Cormen, Leiserson, Rivest and
Stein, Introduction to Algorithms, 3rd ed. (MIT Press, 2009). The design is
docs/intro-algorithms/PLAN.md, section C, Course 6.
"""

from . import part_a, part_b

COURSE = {
    "slug": "intro-algorithms-graphs",
    "title": "Graph Algorithms",
    "level": "Intermediate",
    "summary": (
        "Part VI of the book, Chapters 22 to 26: Elementary Graph Algorithms; Minimum "
        "Spanning Trees; Single-Source Shortest Paths; All-Pairs Shortest Paths; and Maximum "
        "Flow. Each lesson sets out a chapter's argument, section by section, in its own "
        "words, and then runs the algorithm on a small graph written for the lesson, counting "
        "what the chapter counts: vertices enqueued and edges examined, discovery and finish "
        "times, components peeled, spanning trees of least weight, relaxation rounds, matrix "
        "cells, augmentations and the cut that proves a flow is maximum."
    ),
    "blurb": (
        "Read Part VI a section group at a time, from searching a graph to maximum flow. "
        "Run breadth-first and depth-first search and read the layers, the timestamps and the "
        "edge classes; peel strongly connected components with two searches; test the cut "
        "theorem against every spanning tree; watch Bellman-Ford, Dijkstra and Floyd-Warshall "
        "relax the same kind of edge in different orders; and push flow until a cut of equal "
        "capacity proves no more will fit."
    ),
    "key": [
        "search once, read the structure off it",
        "decreasing finish time orders a dag",
        "a light edge across a cut is safe",
        "relaxation never undershoots",
        "the order of relaxing is the algorithm",
        "flow equals cut: the proof of maximum",
    ],
    "assumes_short": "Advanced Data Structures",
    "assumes_long": (
        "Advanced Data Structures, for disjoint sets and Fibonacci heaps; and Sorting and "
        "Order Statistics, for heaps and priority queues. Appendix B of the book defines "
        "graphs, trees and paths, and the lessons lean on it"
    ),
    "outcomes_intro": (
        "By the end you can run each of Part VI's algorithms by hand on a small graph, count "
        "what its analysis counts, and say which lemma or theorem makes its answer right on "
        "every graph rather than on the one in front of you."
    ),
    "outcomes": [
        ("Search a graph two ways",
         "Run breadth-first search for distances and a breadth-first tree, and depth-first "
         "search for discovery and finish times, and classify every edge from the times."),
        ("Use a search as a subroutine",
         "Sort a dag by decreasing finish time and find strongly connected components with a "
         "second search on the transpose, saying why the order of the second search matters."),
        ("Grow a minimum spanning tree",
         "Find the light edges across a cut, run Kruskal's and Prim's algorithms by hand, and "
         "explain with the cut theorem why each edge they add is safe."),
        ("Compute shortest paths in the right order",
         "Run Bellman-Ford, the dag algorithm, Dijkstra's algorithm and Floyd-Warshall on a "
         "small graph, count their relaxations, and say which weights each one allows."),
        ("Find a maximum flow and its certificate",
         "Push flow along augmenting paths in a residual network, read off a minimum cut of "
         "equal capacity, and solve a bipartite matching as a unit-capacity flow."),
    ],
    "syllabus_intro": (
        "Nine lessons follow Part VI in the book's order: three on Chapter 22, one on "
        "Chapter 23, two on Chapter 24, one on Chapter 25 and two on Chapter 26."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, 2009), "
        "Part VI, with instances written for these lessons. Each lesson names its sections, "
        "opens with at most one short quotation, and sets out the argument in its own words; "
        "the book's pseudocode, figures and exercises are better read in the book, and the "
        "graphs in the lessons are not the book's.",
        "Hold one idea throughout. Nearly every algorithm in Part VI is a search or a "
        "sequence of relaxations, and what distinguishes them is the order: a queue or a "
        "stack, sorted edges or a heap, rounds over every edge or one pass in topological "
        "order, one interior vertex at a time, the shortest augmenting path first. Each "
        "lesson asks why its order is the one that makes the answer right.",
        "Type the lesson's graph into the lab. The labs open on a worked example of their "
        "own; each lesson gives you its graph in the lab's notation, one arc or edge per "
        "clause, and you paste it into the editor. Every lab figure a lesson quotes was read "
        "off the lab with that graph typed in; the rest are worked by hand.",
        "Treat each count as evidence about one graph. The labs run the algorithm and count "
        "what the chapter counts, and several check the answer by a second route, such as "
        "every spanning tree or every cut listed. None of that proves a bound. The bound holds "
        "for every graph, and only the chapter's proof establishes it.",
    ],
    "not_covered": [
        "The book's pseudocode, figures and exercises. They are the book's; the lessons "
        "describe each procedure in prose and name it, and point to exercises by number.",
        "The starred sections' proofs. Section 26.4 (push-relabel) and Section 26.5 "
        "(relabel-to-front) are named in the matching lesson and left to the book, as are "
        "the chapter notes and problems.",
        "Section 24.5's proofs of the shortest-path properties are summarised, not "
        "reproduced, and Johnson's algorithm in Section 25.3 is described without a lab.",
        "Implementation detail the labs simplify. The Dijkstra lab keeps a heap with "
        "repeated entries rather than a decrease-key handle, and the depth-first labs take "
        "adjacency lists in the order the arcs are typed; each lesson says where that matters.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from a graph a lesson "
        "states: layers and distances by a queue, timestamps and edge classes by a "
        "depth-first walk, components by two passes, minimum trees checked against every "
        "spanning tree, distances by relaxation in three orders and by a matrix, and flows "
        "checked against every cut. The graphs are written for these lessons. A count on one "
        "graph is evidence about that graph; the book's proofs are about all of them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
