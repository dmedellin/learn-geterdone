"""Intractability and Approximation."""


from . import part_a, part_b


COURSE = {
    "slug": "intractability-and-approximation",
    "title": "Intractability and Approximation",
    "level": "Advanced",
    "summary": (
        "What a reduction actually is, built four times rather than drawn as an arrow, and the "
        "six honest responses to a problem that has no fast algorithm &mdash; each with the "
        "quantity its guarantee is proved against, and never a ratio without the optimum it is a "
        "ratio to."
    ),
    "blurb": (
        "Every course so far built algorithms that work. This one starts where none is known to, "
        "and it does two things with that. First it makes hardness constructive: a reduction is a "
        "construction, so each one here is built in front of you, both instances are solved "
        "exhaustively, and the map between their solution sets is checked for soundness, for "
        "injectivity and for surjectivity as three separate questions &mdash; because two of them "
        "have answers that change with the instance. Then it builds the six things that can "
        "honestly be done instead, and for each one it prints the algorithm's answer, the true "
        "optimum from an exhaustive search, the realised ratio and the promise, on one axis."
    ),
    "key": [
        "A ≤p B        hardness flows from A to B, tractability the other way",
        "a certificate is checked in polynomial time; finding one is a different question",
        "",
        "|cover| = 2|M| ≤ 2·OPT       a ratio is proved against a LOWER BOUND, not the optimum",
        "MST ≤ OPT ≤ tour ≤ 2·MST     four computed numbers, and the chain IS the proof",
        "",
        "a count on one input is not a bound, and nor is a count on every input of one size",
    ],
    "assumes_short": "Reductions as definitions, greedy and dynamic programming, flow and matching",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: P, NP and NP-Completeness, where the classes "
        "and reductions were met as definitions; Satisfiability and Normal Forms, for conjunctive "
        "normal form; Big-O, Big-Omega and Big-Theta; Analysing Iterative Algorithms; Strong "
        "Induction; and Graphs and Trees in full. From this path: Graph Algorithms, for Prim's "
        "algorithm, for Max Flow and Min Cut and for Bipartite Matching, which supply the minimum "
        "spanning tree these pages use as a lower bound and the theorem that makes vertex cover "
        "tractable on bipartite graphs; Greedy Algorithms and Matroids, for the exchange argument "
        "and for fractional knapsack, which is the bound branch and bound prunes with; Dynamic "
        "Programming and Optimal Substructure, for the subset-sum and knapsack tables that explain "
        "weak hardness and that the approximation scheme shrinks; and Randomised Algorithms, for "
        "the probabilistic method and the expectation arguments this course compares its "
        "deterministic guarantees against"
    ),
    "outcomes_intro": (
        "By the end you can build a reduction rather than cite one, say what it does and does not "
        "preserve, choose among six responses to a problem you cannot solve exactly, and read "
        "every number on the page as a statement about the thing it is actually a statement about."
    ),
    "outcomes": [
        ("Build a reduction, and check the map it induces",
         "Construct the instance, prove both directions, then ask separately whether every "
         "solution maps back, whether two share an image, and whether every solution is an image "
         "&mdash; and name which of the three answers depends on the instance rather than on the "
         "construction."),
        ("Prove a guarantee against a lower bound the algorithm can see",
         "A matching for vertex cover, a spanning tree for the metric tour, a per-element charge "
         "for set cover: in each case write the chain from the lower bound through the optimum to "
         "the answer and the promise, and identify the single link that mentions the optimum at "
         "all."),
        ("Choose among the six responses, and say what each gives up",
         "Prune an exact search; parameterise the exponential; approximate with a guarantee; "
         "approximate under a hypothesis you have tested; buy accuracy by the epsilon; or "
         "restrict to a special case that is genuinely tractable. Each is built here with the "
         "measurement that justifies it."),
        ("Separate what was counted from what was proved",
         "Node counts, realised ratios and cell counts are measurements on the instance on "
         "screen. Promises, harmonic bounds and the expressions `2^k · n` and `2^n` are not. Four "
         "pages here have the asymptotically better method losing on the instance shown, and one "
         "has a guarantee failing completely because its hypothesis was switched off."),
    ],
    "syllabus_intro": (
        "The line first, and why stating everything for yes-or-no questions costs nothing; then "
        "four reductions, each built and each with its solution map measured; then the two "
        "responses that keep an exact answer and pay in an exponential; then the four guarantees, "
        "in order of what they assume; and last, one algorithm measured on one instance, on every "
        "instance of a size, and against what was proved."
    ),
    "how_to": [
        "Read every figure as a statement about something, and say what. This course prints "
        "measurements and proved bounds in the same panels on purpose: 14 nodes against 44 is "
        "this instance, `2^k · n` against `2^n` is two expressions evaluated at this instance's "
        "numbers, and a promise of 2 is a theorem. Confusing any two of those three is the only "
        "way to leave this course with a false belief.",
        "Break something on every page that lets you. Raise a distance until the triangle "
        "inequality fails and watch a factor-2 guarantee return a tour of 53 against its own "
        "promise of 6; switch a "
        "bound off and watch the node count triple while the answer does not move; add a clause "
        "and watch a reduction's solution map become surjective. The controls are there because a "
        "guarantee you have never seen fail is a guarantee you cannot state the conditions of.",
        "Never accept a ratio without its denominator. Every mode of both kits on this course "
        "computes the true optimum by exhaustive search at a cap it states, and prints it beside "
        "the ratio, because a ratio against an unknown optimum is a fraction with an invented "
        "denominator. Hold every other source to the same standard.",
    ],
    "not_covered": [
        "That satisfiability is NP-complete at all. Cook and Levin's theorem &mdash; that a "
        "polynomial-time verifier can be encoded as a formula &mdash; is the base of every "
        "hardness result quoted here and it is stated rather than proved: its construction is "
        "about machines rather than about combinatorial structure, and nothing in this library "
        "executes a machine. The reductions on these pages are all from satisfiability onwards.",
        "The middle of the standard chain into Hamilton circuits. An honest gadget for the "
        "three-colouring or Hamilton-circuit reductions needs more vertices than the labs here can "
        "solve exhaustively, and showing half a gadget would be showing a reduction that does not "
        "reduce anything. Circuits to tours is built; independent set to circuits is named.",
        "Kernelisation, and parameterised complexity beyond one bounded search tree. Shrinking an "
        "instance to a size depending only on the parameter before searching is the other half of "
        "the subject, and the first reduction rule &mdash; a vertex of degree above `k` must be in "
        "any cover of size `k` &mdash; is named on the page rather than built.",
        "The hardness of approximation itself, apart from one case. That no constant factor is "
        "possible for the general travelling salesman is proved here, because the gadget is the one "
        "already on the page with a larger number in it. That greedy set cover's logarithmic factor "
        "cannot be beaten, and the modern inapproximability results behind it, are quoted with "
        "their consequences and proved nowhere in this library.",
        "Linear-programming methods for approximation: rounding a fractional solution, the primal "
        "&mdash; dual method, and derandomising a randomised rounding by conditional expectations. "
        "The last of those belongs beside the randomised satisfiability argument in the previous "
        "course rather than here, and the first two need duality, which Operations Research owns.",
        "DPLL and modern satisfiability solving. Unit propagation, pure literals, clause learning "
        "and the phase transition at the satisfiability threshold are a search with a bound on a "
        "different problem, and they would repeat the shape of branch and bound without adding an "
        "argument. The oracle on the first page here is deliberately brute force, because the "
        "claim being made is about the number of calls.",
    ],
    "footer_lead": (
        "Every count on this course is produced by running the algorithm on the instance you "
        "typed. Node counts, cover sizes, cell counts, tour lengths, oracle calls and the sizes of "
        "solution sets are exact integers; ratios, charges, epsilons, scale factors, harmonic "
        "numbers and promised losses are exact fractions over arbitrary-precision integers, and "
        "the digit-table reduction's numbers leave the exact range of a double and are computed as "
        "big integers throughout. No verdict anywhere on this course is read off a decimal. Every "
        "approximation ratio is printed with the optimum it is a ratio to, and that optimum comes "
        "from an exhaustive search &mdash; over subsets, assignments, tours or subfamilies &mdash; "
        "at a cap each page states and refuses above. Every reduction is checked twice over: the "
        "two instances are solved by routines sharing no code, and the map between their full "
        "solution sets is reported as three separate verdicts rather than one word. Four figures "
        "here are not measurements and each page says so: the promised ratios of 2, the harmonic "
        "bound for greedy set cover, the promised loss of an approximation scheme, and the "
        "expressions `2^k · n` and `2^n`, which are evaluated at the instance's numbers rather "
        "than counted. Two exhaustive sweeps do quantify over every instance of a size &mdash; "
        "every graph on the chosen number of vertices, and every metric instance on four cities "
        "with distances up to 3 &mdash; and each names the family it searched, because a worst "
        "case over a finite family is a stronger claim than a count on one input and a weaker one "
        "than a proof."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
