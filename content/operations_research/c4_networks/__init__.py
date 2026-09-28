"""Networks: Flows, Paths and Assignments."""


from . import part_a, part_b


COURSE = {
    "slug": "networks-flows-paths-and-assignments",
    "title": "Networks: Flows, Paths and Assignments",
    "level": "Advanced",
    "summary": (
        "One linear programme with one matrix in it, and every network problem there is as a "
        "different right-hand side: shipping, shortest paths, maximum flow, transportation and "
        "assignment all solved by the machinery already built &mdash; and then the reason the "
        "answers come out in whole units, which is a property of the matrix and is proved here "
        "rather than observed."
    ),
    "blurb": (
        "Draw a network, write the node equations, and the simplex method solves it. What makes "
        "this a course rather than a worked example is that the same matrix &mdash; one column "
        "per arc, a plus one at the tail and a minus one at the head &mdash; is every problem on "
        "it: change the supplies and a minimum-cost flow becomes a shortest path, a maximum "
        "flow, a transportation plan or an assignment. That matrix is totally unimodular, so "
        "every corner of every one of those programmes is whole on whole data, with no "
        "integrality constraint and no rounding; and the specialised methods that came before "
        "the simplex &mdash; potentials on a tableau, augmenting paths, the Hungarian reductions "
        "&mdash; turn out to be the dual programme, worked by hand."
    ),
    "key": [
        "min cᵀx   s.t.  N x = b,  0 ≤ x ≤ u",
        "   one column per arc, one row per node",
        "N has +1 at the tail, −1 at the head,",
        "and zero everywhere else in the column",
        "Σ bᵢ = 0 or nothing is feasible: add",
        "the rows and every flow cancels",
        "N totally unimodular ⟹ every corner is",
        "whole, on whole data, with no rounding",
        "shortest path   πⱼ − πᵢ ≤ cᵢⱼ,",
        "   maximise πₜ − πₛ; the labels are dual",
        "max flow = min cut   a cut is a 0/1",
        "   feasible point of the dual programme",
        "uᵢ + vⱼ = cᵢⱼ on a basis of m + n − 1",
        "cells; reduced cost cᵢⱼ − uᵢ − vⱼ elsewhere",
        "assignment: smallest cover = largest",
        "matching; the reductions add to the dual",
    ],
    "assumes_short": "Linear Programming Models through Duality and Sensitivity Analysis; graphs, and determinants",
    "assumes_long": (
        "linear programming models, the simplex method, and duality and sensitivity analysis "
        "from this path — the dual of a programme with equality rows, complementary slackness, "
        "and a shadow price read off a final tableau are all used as tools rather than "
        "re-derived; from discrete mathematics, graphs and trees, in particular paths and "
        "connectivity, bipartite graphs and Hall's marriage theorem, spanning trees, and "
        "shortest paths as Dijkstra's algorithm computes them; and from algebra, matrix "
        "products, determinants and Cramer's rule, and inverse matrices, because the reason a "
        "network corner is whole is a statement about determinants"
    ),
    "outcomes_intro": (
        "By the end you can write any network problem as the same linear programme, prove why "
        "its answer is whole, read the dual of four different network problems as a labelling, "
        "a cut, a set of potentials and a set of reductions, and say in each case what the "
        "certificate is."
    ),
    "outcomes": [
        ("Write a network down as data, and check a flow",
         "Ordered arcs with capacities and costs, supplies that sum to zero, and a proposed "
         "flow tested twice &mdash; conservation node by node, capacity arc by arc &mdash; with "
         "the failing nodes and the overfull arcs named rather than a single verdict given."),
        ("Recognise one programme wearing five faces",
         "The minimum-cost flow programme `min cᵀx` subject to `Nx = b` and `0 ≤ x ≤ u`, with "
         "transportation, assignment, shortest path and maximum flow obtained from it by "
         "changing `b`, `u` and `c` alone &mdash; and nothing else."),
        ("Prove that the corners are whole",
         "Total unimodularity checked determinant by determinant on a node-arc matrix, the "
         "Cramer's-rule argument that turns it into integrality, and the undirected odd cycle "
         "whose determinant is two and whose optimal corner is genuinely halves."),
        ("Run the tableau methods, and know what they are",
         "A transportation problem balanced with a dummy, started two ways and solved by "
         "potentials and a stepping-stone cycle; an assignment problem solved by reductions "
         "whose running total is a dual objective climbing to meet the primal."),
        ("Read the dual of a path and of a cut",
         "Node potentials as a feasible dual solution for shortest paths, a negative cycle as "
         "dual infeasibility, and a cut exhibited as a zero-one point of the maximum-flow dual "
         "whose objective is exactly that cut's capacity."),
        ("Produce the certificate, not just the answer",
         "A deficient set with `|N(S)| &lt; |S|` when no complete matching exists, a minimum cover "
         "the size of a maximum matching when one does, the critical path that holds a project's "
         "length, and in every case the number that proves the answer cannot be beaten."),
    ],
    "syllabus_intro": (
        "The object first, then the programme that is every network problem at once; then the "
        "tableau half &mdash; transportation and assignment, where the method predates the "
        "simplex and is worth knowing because it is the dual by hand &mdash; with the "
        "integrality theorem placed where a reader has just watched whole numbers come out of "
        "an algorithm that never asked for them; then the project network, which is the one "
        "network on the course with nothing flowing along it; and last the three duality "
        "readings that make a path, a cut and a matching the same theorem."
    ),
    "how_to": [
        "Add the supplies up before you solve anything. If they do not come to zero the "
        "programme is infeasible and no amount of arithmetic will say so more clearly than the "
        "sum does &mdash; and the lab prints the total beside the drawing for exactly that "
        "reason.",
        "Say which arc you mean, out loud, with the direction in it. Half the errors on this "
        "course are an undirected habit surviving into a directed setting: `a` to `b` and `b` to "
        "`a` are two variables, with two capacities, two costs, and no reason at all to carry "
        "the same flow.",
        "When a method gives you a whole number, ask whether it had to. It did, on a network, "
        "and the reason is one determinant argument; it did not on an odd cycle, and the lab of "
        '&ldquo;Total Unimodularity and Integer Corners&rdquo; will hand you the halves. Treating '
        "integrality as luck is how a reader later rounds an integer programme and believes it.",
        "Produce the certificate before you believe the answer. Every optimum on this course "
        "comes with one &mdash; a cut, a cover, a set of potentials, a critical path &mdash; and "
        "each is a small object you can check by hand in less time than it took to find.",
    ],
    "not_covered": [
        "The augmenting-path algorithm as an algorithm. Why a backward arc is necessary is shown "
        "on the residual network here, because the theorem needs a flow to be a theorem about; "
        "how the choice of path bounds the running time belongs to the Algorithms path and is "
        "named rather than developed.",
        "Dijkstra's algorithm. Discrete Mathematics has it, and this course deliberately does "
        "not put it beside Bellman-Ford: the question here is what the labels <em>are</em> "
        "&mdash; a feasible dual solution &mdash; and a second algorithm for the same numbers "
        "answers a different question.",
        "The network simplex method, and successive shortest paths. Both are the simplex or the "
        "residual network specialised for speed, both need a spanning-tree basis maintained as a "
        "data structure, and the reference solution for every instance on this course is the "
        "exact simplex on the programme itself.",
        "Minimum spanning trees. A spanning tree turns up here as the basis of a transportation "
        "tableau, which is a different use of the same word; finding a cheapest one is a greedy "
        "argument and it is Discrete Mathematics' in &ldquo;Spanning Trees and Minimum Spanning "
        "Trees&rdquo;.",
        "Multicommodity flow, and anything with two goods sharing an arc. The integrality that "
        "makes this course work fails as soon as two commodities share a capacity, which is "
        "worth knowing and is as far as this course takes it.",
    ],
    "footer_lead": (
        "Every flow, cost, determinant, potential and cut capacity on this course is an exact "
        "fraction, and nothing here is rounded, because nothing here needs to be: the data are "
        "rational and the arithmetic stays rational. That matters more on this course than on "
        "most, since the central claim is that certain corners are exactly whole. A flow "
        "reported as `0.9999999` would not be evidence of anything. Where a corner is genuinely "
        "not whole &mdash; the odd cycle's `1/2` &mdash; the lab prints the halves as halves, "
        "which is the point."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
