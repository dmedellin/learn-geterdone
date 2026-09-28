"""Linear Programming Models."""


from . import part_a, part_b


COURSE = {
    "slug": "linear-programming-models",
    "title": "Linear Programming Models",
    "level": "Intermediate → Advanced",
    "summary": (
        "Writing a situation down as a linear programme: decision variables with units, an "
        "objective that is an expression in them, and the four constraint families that recur "
        "&mdash; packing, covering, blending, balance &mdash; then the reformulations that keep "
        "a model linear, the standard form every solver wants, and what a corner becomes once "
        "there are too many variables to draw one."
    ),
    "blurb": (
        "Systems and Matrices ended with an objective and four inequalities already written "
        "down. This course is about writing them. It asks three questions in the same order "
        "&mdash; what do I decide, what do I want, what stops me &mdash; and answers them four "
        "times over on the model families that cover most of applied optimisation; then it "
        "shows which non-linear-looking requirements are secretly linear, converts everything "
        "to the one form the simplex method eats, and replaces the drawn corner with an "
        "algebraic object that survives ten variables. It ends with the single theorem that "
        "will later let an algorithm stop."
    ),
    "key": [
        "max cᵀx   s.t.  Ax ≤ b,  x ≥ 0     decisions, objective, constraints",
        "usage ≤ availability               slack   = the unused resource",
        "supply ≥ requirement               surplus = the over-fulfilment",
        "N ≥ 3/10 (N + R + B)               a share, linear once cleared",
        "Iₜ = Iₜ₋₁ + Pₜ − Dₜ                one balance equation per period",
        "standard form:   max cᵀx,  Ax = b,  x ≥ 0",
        "a corner = a basic feasible solution;  at most C(n + m, m) of them",
    ],
    "assumes_short": "Systems of inequalities, and row reduction on exact fractions",
    "assumes_long": (
        "Algebra: Systems of Inequalities and Linear Programming, Gaussian Elimination, "
        "Matrices and Row Operations, Systems in Three Variables, Modelling with Linear "
        "Equations, Translating Words into Algebra, Linear Inequalities in Two Variables, and "
        "Pascal’s Triangle. Nothing from Discrete Mathematics is needed: this course and the "
        "two that follow it rest on Algebra alone"
    ),
    "outcomes_intro": (
        "By the end you can turn a described situation into a linear programme that someone "
        "else could solve, recognise which of four families it belongs to, rewrite the "
        "requirements that look non-linear and are not, put the result in standard form, and "
        "say what a corner is without drawing one."
    ),
    "outcomes": [
        ("Write a linear programme from a paragraph",
         "Decision variables with units, a linear objective that is an expression in them, "
         "every constraint including the sign restrictions &mdash; and a candidate point "
         "checked against all of them, one at a time, each named."),
        ("Build the four recurring model families",
         "Product mix from per-unit rates and availabilities, a diet or covering model from "
         "requirements, a blend from percentage specifications, and a multiperiod plan from one "
         "balance equation per period &mdash; and read from each solution which constraints are "
         "tight."),
        ("Reformulate what looks non-linear and is not",
         "A free variable as a difference, an absolute value in a minimised objective, a "
         "minimised maximum with one auxiliary variable, and a convex piecewise-linear cost "
         "&mdash; each justified by the direction the optimiser pushes, and each checked by "
         "solving the original and the reformulation and comparing."),
        ("Convert to standard form and say what the new variables measure",
         "A slack added to every `≤` row, a surplus subtracted from every `≥` row, a free "
         "variable split, a minimisation negated and negated back &mdash; with each new "
         "variable given a meaning in the situation, not just a column."),
        ("Enumerate basic solutions and match them to corners",
         "Choose which variables are zero, solve the rest by row reduction, and classify every "
         "result as feasible, infeasible, singular or degenerate &mdash; then locate each on "
         "the picture while the picture still exists."),
        ("Prove the feasible set convex and draw the stopping principle from it",
         "The segment between two feasible points is feasible; a linear objective is affine "
         "along it; therefore a feasible point with no improving feasible direction cannot be "
         "beaten anywhere &mdash; which is the licence “The Simplex Method” needs in order to "
         "stop."),
    ],
    "syllabus_intro": (
        "Modelling first and four times over, because a reader who cannot write the constraints "
        "has nothing to solve; then the three rewrites that keep a model inside the class; then "
        "standard form, which is a modelling act rather than a clerical one; and last the two "
        "structural facts &mdash; what a corner is algebraically, and why a local optimum is "
        "global &mdash; that the simplex method will consume."
    ),
    "how_to": [
        "Answer the three questions separately and write them down in this order: what do I "
        "decide, what do I want, what stops me. Nearly every broken model on this course is an "
        "answer to the second question written in the first slot.",
        "Put a unit on every variable before writing a single constraint, and check that both "
        "sides of each constraint carry the same unit. The lab prints the unit chain for the "
        "worked situations; for your own model, write it in the margin.",
        "Test each model on a point you can check by hand before trusting the solver. The labs "
        "accept a typed candidate point and report it constraint by constraint, which is the "
        "fastest way to find a sign error.",
        "Do not skip “Basic Solutions and Corners” because the pictures still work in two "
        "variables. The algebraic corner is the whole reason “The Simplex Method” is possible, "
        "and it is much easier to learn while the picture is still there to check it against.",
    ],
    "not_covered": [
        "Solving anything beyond two variables by hand. Corner enumeration is what “Systems of "
        "Inequalities and Linear Programming” gave you and it does not scale; the algorithm "
        "that does is “The Simplex Method”.",
        "What a constraint is worth. Prices, ranges and sensitivity belong to “Duality and "
        "Sensitivity Analysis”; this course can say that a resource is exhausted and "
        "deliberately cannot yet say whether more of it would help.",
        "Integer restrictions. “Make three and a half tables” is answered in “Integer "
        "Programming”, which is also where the warning at the end of “Systems of Inequalities "
        "and Linear Programming” is finally discharged.",
        "Non-linear objectives and constraints of any kind. A product of two decisions, a ratio "
        "with a variable denominator that can vanish, a squared cost &mdash; each leaves the "
        "class, and this course's job is to know when that has happened.",
        "Where the data come from. Every coefficient here is given. Estimating them, and the "
        "fact that the optimum of the wrong model is exactly wrong, is this subject's standing "
        "warning rather than a lesson.",
    ],
    "footer_lead": (
        "Every model on this course is rebuilt from the data table in front of you: change a "
        "number and the linear programme, its corners, its slacks and its achieved percentages "
        "are recomputed, not looked up. All of it is exact &mdash; where a share is one third "
        "it prints `1/3`, and the candidate point you type is checked against each constraint "
        "separately, so that a failure names the constraint that failed rather than the model."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
