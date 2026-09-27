"""The Simplex Method."""


from . import part_a, part_b


COURSE = {
    "slug": "the-simplex-method",
    "title": "The Simplex Method",
    "level": "Advanced",
    "summary": (
        "A walk from corner to adjacent corner: the tableau that carries the current basis, the reduced cost that chooses the direction, the ratio test that chooses the step, the artificial variables that manufacture a start, the three tableau signatures that diagnose unboundedness, ties and degeneracy, and the matrix identity `B⁻¹[A | b]` that says a tableau is a view of the original data."
    ),
    "blurb": (
        "“Systems and Matrices” declined the simplex algorithm by name. This is it. Each step is a Gauss&ndash;Jordan pivot, the entering variable is chosen by a rate and the leaving one by a ratio that keeps every variable non-negative, and the method stops on the licence “Convexity, and Why a Local Optimum Is Global” gave it. Everything is exact, which is what makes the two famous pathologies &mdash; a tableau that returns to itself after six pivots, and a cube that forces `2ⁿ - 1` of them &mdash; reproducible on your screen rather than described in a footnote."
    ),
    "key": [
        "tableau = [A | b] of standard form, plus a z-row   z - cᵀx = 0",
        "pivot   = one Gauss-Jordan step on a column, z-row included",
        "enter   a column whose reduced cost improves z      (a rate)",
        "leave   min b_i / a_ij over a_ij > 0                (the step length)",
        "Δz      = rate × step",
        "stop    no improving reduced cost ⟹ optimal, by the convexity licence",
        "every tableau on the path = B⁻¹[A | b]",
    ],
    "assumes_short": "Linear Programming Models; Gaussian elimination and matrix inverses",
    "assumes_long": (
        "the whole of Linear Programming Models, and from the Algebra path Gaussian "
        "Elimination, "
        "Matrices and Row Operations, Matrix Products, Inverse Matrices and Systems "
        "in Three Variables. Still nothing from Discrete Mathematics: “Termination and "
        "the Klee–Minty Cube” borrows three words from P, NP and NP-Completeness and says so "
        "in a note, which is a citation and not a prerequisite"
    ),
    "outcomes_intro": (
        "By the end you can run the method by hand on a small problem, choose both "
        "variables for the right reasons, start from a problem that gives you no "
        "obvious basis, name what a tableau is telling you when it refuses to finish, "
        "and write any tableau as a product involving the original data."
    ),
    "outcomes": [
        ("Set up a tableau and read it",
         "Build it from standard form; read the current basic feasible solution, the "
         "basis and the objective value off it without solving anything."),
        ("Choose both variables and pivot exactly",
         "Entering by reduced cost, leaving by the ratio test, the pivot as a "
         "Gauss&ndash;Jordan step with the objective row included &mdash; and a stated "
         "reason for stopping."),
        ("Manufacture a start, or prove there is none",
         "Artificial variables and a first-phase objective; a first-phase optimum of "
         "zero hands a basis to the second phase, and a positive one is a proof of "
         "infeasibility with the value as the certificate."),
        ("Diagnose the three awkward tableaux",
         "An improving column with no positive entry, a zero reduced cost on a "
         "nonbasic variable at optimality, and a tie in the ratio test &mdash; each "
         "recognised from the tableau and each answered."),
        ("Write the tableau as a matrix product",
         "Extract `B`, invert it, and reproduce the body and the objective row as "
         "`B⁻¹[A | b]` and `c_BᵀB⁻¹[A | b] - [c | 0]` &mdash; the identity “Duality and "
         "Sensitivity Analysis” reads the dual solution out of."),
        ("Say honestly how fast the method is",
         "Finite by a smallest-index rule, exponential in the worst case on a "
         "constructed example, and fast in practice &mdash; three statements that are "
         "each true and none of which implies another."),
    ],
    "syllabus_intro": (
        "The idea first, in two variables where the walk can still be seen; then the "
        "three mechanical pieces &mdash; the tableau, the ratio test, the reduced cost "
        "&mdash; one lesson each, because each is separately a place readers go wrong; "
        "then starting, then the three diagnoses, then the matrix view that makes the "
        "next course possible, and last the honest account of speed."
    ),
    "how_to": [
        "Pivot by hand at least twice before letting the lab do it. The lab traces "
        "every row operation for exactly this purpose, and a reader who has never "
        "carried an objective row through a pivot will drop it later under pressure.",
        "Whenever you make a choice, make the other one too. Both the ratio-test and "
        "the entering-rule labs let you override the correct choice, and the point of "
        "each is the wreckage that follows &mdash; a negative basic variable, or an "
        "extra twenty pivots.",
        "After each pivot, read the basic feasible solution off the tableau and locate "
        "it on the region. In two variables you can always do this, and it is the "
        "habit that makes four variables survivable.",
        "Treat the exactness as load-bearing, not as tidiness. Beale&rsquo;s example "
        "returns to its starting tableau <em>entry for entry</em>; in floating point it "
        "would return to something that merely looks like it, and the lesson would be a "
        "story.",
    ],
    "not_covered": [
        "Interior-point methods. They need limits, they are floating-point by nature, "
        "and they cannot be made exact &mdash; which would teach the opposite of this "
        "library&rsquo;s promise. Their existence is named in “Termination and the "
        "Klee&ndash;Minty Cube” and nothing more.",
        "The revised simplex method as a separate algorithm. “The Tableau as a Matrix "
        "Product” gives the identity it is built on; the data structures that exploit it "
        "are an implementation subject.",
        "Bounded-variable simplex, and upper bounds handled implicitly. Bounds here are "
        "ordinary constraints with ordinary slacks.",
        "Floating-point stability, conditioning and pivot-size heuristics. Nothing on "
        "this path floats, so none of it applies; the trade-off that makes those "
        "heuristics necessary is worth a sentence and gets one.",
        "Anticycling by perturbation or the lexicographic rule. Bland&rsquo;s rule is "
        "enough to prove termination and is the one a reader can execute.",
    ],
    "footer_lead": (
        "Every tableau on this course is exact, and that is not tidiness. Beale&rsquo;s cycling example returns to its starting tableau entry for entry only if nothing has been rounded, and the Klee&ndash;Minty pivot count is exactly `2ⁿ - 1` only if the comparisons among reduced costs spanning `1` to `10ⁿ⁻¹` land exactly, which in floating point one of them does not. Nor do the entries grow: every entry of a tableau is a ratio of determinants of submatrices of the original data, so the denominators are bounded by the data you typed, however many pivots it takes."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
