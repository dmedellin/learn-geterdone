"""The Operations Research path, as data.

Ten courses in one order. The content lives here and only here; scripts/
turns it into pages. Nothing in this package emits markup beyond the inline
`x` shorthand, and nothing in scripts/ decides what a lesson says.

Every solve on this path is exact arithmetic. That is not a stylistic choice:
Beale's cycling example and the Klee-Minty pivot count cannot be reproduced
in floating point at all, and a degenerate pivot that a decimal rounds away
is the thing those two lessons are about.
"""

from . import (
    c1_lp_models,
    c2_simplex,
    c3_duality,
    c4_networks,
    c5_integer,
    c6_scheduling,
    c7_sequential,
    c8_inventory,
    c9_markov,
    c10_simulation,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_lp_models.COURSE,
    c2_simplex.COURSE,
    c3_duality.COURSE,
    c4_networks.COURSE,
    c5_integer.COURSE,
    c6_scheduling.COURSE,
    c7_sequential.COURSE,
    c8_inventory.COURSE,
    c9_markov.COURSE,
    c10_simulation.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "operations-research",
    "title": "Operations Research",
    "level": "Intermediate → Advanced",
    "level_note": 'algebra for the first three courses; discrete probability after that',
    "tagline": (
        'Decisions with a number attached and a constraint in the way: what to make, what to ship, what to schedule, what to stock and when to stop &mdash; each written as a model, solved exactly, and then read back to find out what the answer cost and what would change it. Ten courses and 94 lessons are available.'
    ),
    "description": (
        'The Operations Research Subject: ten courses in one order, from linear programming models and the simplex method through duality and sensitivity, networks, integer programming, scheduling, sequential decisions, inventory, Markov chains and queues, to simulation. Every solve on this path is exact arithmetic &mdash; tableaux in fractions, expectations as fractions, steady states from a linear system &mdash; and every lesson ends by asking what the model assumed. All ten courses and 94 lessons are available.'
    ),
    "key": [
        "max cᵀx  s.t. Ax ≤ b, x ≥ 0    ⟷    min bᵀy  s.t. Aᵀy ≥ c, y ≥ 0",
        "cᵀx ≤ bᵀy for every feasible pair; equal only at the optimum",
        "yᵢ = the change in the optimum per unit of bᵢ — within a range, then it moves",
        "an integer optimum is not a rounded LP optimum",
        "Q* = √(2KD/h)                  and the cost curve is flat either side of it",
        "πP = π                         a steady state is a linear system, not a limit",
    ],
    "sequence_intro": (
        'Each course assumes the ones before it. The first three build one object &mdash; the linear program, the algorithm that solves it, and the second program hidden inside the first &mdash; and a reader who stops after Duality and Sensitivity Analysis has a complete subject. Network Optimisation and Integer Programming are that object with structure added; the four courses after them replace the linear program with exchange arguments, backward recursion and linear systems; Simulation is what is left when none of those applies.'
    ),
    "why_order": [
        'Linear Programming Models comes first, and it is a course about writing models rather than solving them, because the modelling error is the one that survives a correct solve. A reader who can pivot flawlessly through a tableau built from the wrong constraint has learned a technique and not a subject, and nothing later in the path will tell them.',
        'The Simplex Method precedes Duality and Sensitivity Analysis because the dual vector is read off the final tableau. Meeting duality first as a theorem and second as six numbers already sitting in the row above the slack columns is worth more than either half alone &mdash; and the sensitivity ranges are ratio tests on that same tableau, so the machinery is already built when the ideas arrive.',
        'Network Optimisation and Integer Programming come fourth and fifth because both are linear programs with structure, and the contrast between them is the point: a network LP has integer corners for a reason that can be proved, and a general integer program does not, which is why one is solved by the simplex method and the other by a search that uses it. That contrast is invisible before duality and obvious after it.',
        'Scheduling, Dynamic Programming and Sequential Decisions, Inventory Models, and Markov Chains, Decisions and Queues each replace the linear program with a different exact method &mdash; an adjacent exchange, a backward recursion, a discriminant, a linear system &mdash; and are ordered by how much probability they need. Simulation comes last because it is the method of last resort, and it is the only course on the path whose answers arrive with an error bar rather than a proof.',
    ],
    "prerequisites": [
        'The Algebra path through Sequences and Series for the first three courses, and the Discrete Mathematics path through Algorithms and Complexity for the rest. The first three courses need algebra only &mdash; systems of equations, inequalities, matrices, and the geometry of a region cut out by half-planes. The rest add five Discrete Mathematics courses: graphs, counting, probability, expectation and variance, and the seeded generator. Each course names the slugs it uses.',
        'No calculus. Where a textbook differentiates, this path does not: the economic order quantity is found by the discriminant of a quadratic, every scheduling rule is proved by an adjacent exchange, and a shadow price is the change per unit within a range rather than a derivative. Those are complete arguments, not workarounds for the missing tool.',
        'No programming, and no solver. The labs run the simplex method in front of you on exact fractions; nothing here asks you to write code or to trust a package whose arithmetic you cannot see.',
        'Willingness to write the model down before solving anything. Most of the work on this path is in the formulation, and the labs are built so that a changed constraint moves a corner while you watch &mdash; which is the one thing a printed tableau cannot do.',
    ],
    # Each path names its own hazard. Algebra's is the invented law, Discrete
    # Mathematics' that a worked example is not a proof, System Design's that a
    # model is only as true as its assumptions, Algorithms' that a count on one
    # input is not a bound. This path's is the one that looks least like an
    # error, because the arithmetic is right: the optimum of the wrong model is
    # exactly, confidently, provably wrong.
    "material": (
        "every figure on this path is computed in your browser from the model "
        "the lesson states, and a solution proved optimal is optimal for the "
        "model you wrote down rather than for the situation it came from "
        "&mdash; each lesson names what the model left out."
    ),
    "footer_lead": (
        '<strong>Educational course material.</strong> Every figure on this path is computed in your browser from the model the lesson states, and the arithmetic is exact. Tableau entries, dual values, sensitivity ranges, reduced costs, expectations, steady-state probabilities and every sample statistic are carried as fractions &mdash; which is not a stylistic choice: Beale&rsquo;s cycling example and the Klee&ndash;Minty pivot count cannot be reproduced in floating point at all, and a degenerate pivot that a decimal rounds away is the thing those two lessons are about. Four quantities on the path are genuinely irrational &mdash; the economic order quantity and its cost, a standard error, `e^(−λ)` in the Poisson limit, and the secretary problem&rsquo;s `n/e` &mdash; and every lesson that prints one says that it is rounded and how. Three results are stated and not proved, and say so: the convergence of `Pⁿ` to the steady state, Hall&rsquo;s theorem as Discrete Mathematics states it, and the asymptotics of the maximum load. What the labs cannot do is check a model against the world it came from.'
    ),
    "courses": COURSES,
}
