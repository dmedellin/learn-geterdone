"""Integer Programming."""


from . import part_a, part_b


COURSE = {
    "slug": "integer-programming",
    "title": "Integer Programming",
    "level": "Advanced",
    "summary": (
        "What happens when the variables have to be whole: why rounding is not an answer, how binary variables turn logical conditions into inequalities that can be checked row by row against a truth table, the two models almost every practical integer programme is built from, the big-M that links a fixed cost to a decision and the price of getting its size wrong, and the three honest tools &mdash; branching, bounding and cutting &mdash; whose deliverable is a gap."
    ),
    "blurb": (
        'Algebra&rsquo;s &ldquo;Systems of Inequalities and Linear Programming&rdquo; closes by saying that rounding an optimal corner is not guaranteed to give the best whole-number answer &mdash; and that this is a different subject. This is the subject. Binary variables turn logic into inequalities; a big-M links a fixed cost to a decision and charges you for being careless about its size; and because integer problems are hard in the precise sense Discrete Mathematics gave the word, the tools that remain are bounds &mdash; from a relaxation, from a cut, from a search tree &mdash; and the certificate you finish with is a gap of zero, or an honest number.'
    ),
    "key": [
        "relaxation:  drop integrality  ⟹  z_LP ≥ z_IP  (max)   a bound, not an answer",
        "at most k    Σy ≤ k        if A then B   y_A ≤ y_B",
        "A or B       y_A + y_B ≥ 1  exactly one   Σy = 1",
        "fixed charge  x ≤ M y       M as small as validity allows",
        "either–or     A + M(1 − y),  B + M y      one binary chooses",
        "branch on x = v fractional:  x ≤ ⌊v⌋  or  x ≥ ⌈v⌉;  re-solve by dual simplex",
        "gap = bound − incumbent;  the gap is what is proved",
    ],
    "assumes_short": "Linear Programming Models through Networks: Flows, Paths and Assignments; truth tables, and the vocabulary of hardness",
    "assumes_long": (
        "linear programming models, the simplex method, duality and sensitivity "
        "analysis — the dual simplex in particular — and network optimisation, for "
        "total unimodularity as the contrast case and the assignment problem as a "
        "relaxation; from discrete mathematics, logical connectives, truth tables, "
        "the complexity classes, greedy algorithms, euler and hamilton paths, "
        "permutations, and functions, which is where the floor and ceiling of a "
        "rational are defined and the cutting-plane lesson needs them; and from "
        "algebra, interval and set-builder notation"
    ),
    "outcomes_intro": (
        "By the end you can say why the integer answer is not near the fractional one, "
        "encode a logical condition as an inequality and <em>prove</em> the encoding "
        "right, size a big-M and price the choice, run a search tree by hand and prune "
        "for the right reason, derive a cut from a tableau row, and report a result with "
        "a gap attached."
    ),
    "outcomes": [
        ("Use a relaxation as a bound and refuse it as an answer",
         "Solve the relaxation, test every rounding of its optimum for feasibility, find "
         "the integer optimum by enumeration on a small instance, and state the bound "
         "relation between the three numbers."),
        ("Encode a logical condition and prove the encoding",
         "At-most-k, if-then, either-or, exactly-one and fixed-charge conditions as "
         "linear inequalities on binaries &mdash; each verified against the condition's "
         "truth table, assignment by assignment, with the row that would refute a wrong "
         "encoding named."),
        ("Build the two atoms and read their relaxations",
         "A knapsack and a set-covering model from data; the single fractional item in "
         "one relaxation and the spread halves in the other; and why each relaxation's "
         "value is a bound."),
        ("Size a big-M and pay for it",
         "The tightest valid `M` for a fixed-charge link, and the measured cost of a "
         "looser one &mdash; a weaker bound and more nodes for the same answer."),
        ("Run branch-and-bound and report a gap",
         "The tree by hand with each node's bound and status, pruning for one of the "
         "three right reasons, and an incumbent and a global bound reported together at "
         "every stage."),
        ("Cut, and solve a hard problem exactly",
         "A Gomory cut derived from a fractional tableau row and verified to remove no "
         "lattice point; and a six-city travelling salesman solved by relaxation, subtour "
         "cuts and branching, with a heuristic tour measured against the bound."),
    ],
    "syllabus_intro": (
        "The failure first, because a reader who has not seen rounding fail will keep "
        "reaching for it; then modelling &mdash; logic, the two atoms, the fixed charge, "
        "the disjunction &mdash; because an integer programme is mostly a modelling "
        "problem; and then the three tools, in the order that makes each one the answer "
        "to the previous one's weakness: branch, measure the gap, cut it."
    ),
    "how_to": [
        'Prove every encoding before using it. The lab of &ldquo;Binary Variables and Logical Constraints&rdquo; evaluates your inequality on all `2ⁿ` assignments against the condition&rsquo;s truth table, and a wrong encoding is refuted by a row rather than by an argument. Get into the habit there and keep it in the fixed-charge and either-or lessons, where the same check is harder to run.',
        "Solve the relaxation first, always, and look at what is fractional. A single "
        "split item, a pair of halves, a `y` at `1/20` &mdash; each of those tells you "
        "which constraint is doing the work and often which branching variable to pick.",
        'Make `M` as small as validity allows, and say <em>why</em> your value is valid. &ldquo;The facility&rsquo;s capacity&rdquo; and &ldquo;total demand, whichever is smaller&rdquo; are reasons; &ldquo;a million&rdquo; is not, and the lab of &ldquo;Fixed Charges, Facility Location and Big-M&rdquo; prices the difference on your own instance.',
        "Report a gap rather than an answer whenever the tree has not closed. A result "
        "with a stated gap is a proof; a result without one is a hope, and the difference "
        "is what this course is for.",
    ],
    "not_covered": [
        "Branch-and-cut as solvers implement it. Cut management, node presolve, "
        "pseudo-cost branching and restarts are engineering on top of the last four "
        "lessons, and naming them is as far as this course goes.",
        "Lagrangian relaxation and column generation. Both produce bounds by a different "
        "route and both need machinery &mdash; subgradients, pricing subproblems &mdash; "
        "this path does not have.",
        "Constraint programming. A different formalism with different propagation, and a "
        "genuinely different subject rather than a variant of this one.",
        "Nonlinear integer problems of any kind, including anything quadratic.",
        '<strong>The results this course cites and does not prove.</strong> The pseudo-polynomial dynamic programme for 0/1 knapsack, the knapsack approximation scheme, the `ln n` ratio for greedy set cover, Held&ndash;Karp for the travelling salesman, the metric two-approximation, and the hardness reductions &mdash; all six belong to the Algorithms path, in &ldquo;Dynamic Programming and Optimal Substructure&rdquo; and &ldquo;Intractability and Approximation&rdquo;. Each is stated in the lesson where it is needed, with its owner named.',
        'The exponential worst case, restated. The search tree and its worst case are the Algorithms path&rsquo;s &ldquo;Backtracking and Branch-and-Bound&rdquo;; the search lessons here cite it and add what is this course&rsquo;s own &mdash; that the bound is a linear programme and the child is re-solved from the parent tableau.',
    ],
    "footer_lead": (
        "Bounds, gaps, cut coefficients and node counts on this course are exact, and so "
        "are the floors the cuts are built from: `⌊n/d⌋` on a rational is a division, not "
        "a rounding. The one place a figure could be irrational is a Euclidean distance, "
        "so the travelling-salesman lab takes its costs as integers or rationals; if a "
        "coordinate preset is ever added, its distances are square roots of integers, "
        "printed as surds with a labelled rounding for display only, and every comparison "
        "between tours is made on the exact values."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
