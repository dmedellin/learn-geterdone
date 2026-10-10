"""Systems and the Phase Plane."""

from . import part_a, part_b

COURSE = {
    "slug": "systems-and-the-phase-plane",
    "title": "Systems and the Phase Plane",
    "level": "Advanced",
    "summary": (
        "Two quantities that change together, each at a rate that depends on both. The "
        "matrix of a linear system decides everything: its eigenvectors give the straight "
        "lines the solutions can travel along, its trace and determinant sort the origin "
        "into a saddle, node, spiral or centre, and the signs of the same two numbers "
        "decide whether it is stable. The second half carries that vocabulary to nonlinear "
        "systems, through equilibria, the Jacobian, predators and prey, competing species "
        "and an epidemic."
    ),
    "blurb": (
        "A single equation gave a curve against time. A pair of equations gives a curve "
        "in a plane, and the plane has no time axis: time is the direction you travel "
        "along the curve. For a linear system `x′ = a·x + b·y`, `y′ = c·x + d·y` the whole "
        "picture follows from a two-by-two matrix. Its eigenvalues solve one quadratic, "
        "`λ² − τ·λ + Δ = 0`, whose coefficients are the trace and the determinant, so "
        "two exact numbers say whether solutions rush in, rush out, circle or do both. "
        "The labs keep that side exact: traces, determinants, eigenvalues, eigenvectors "
        "and fitted constants are fractions or surds. What is drawn rather than computed "
        "is the curve itself, which the legend says is stepped in floating point. The "
        "second half asks what survives when the system is not linear, and the honest "
        "answer is: near an equilibrium, most of it."
    ),
    "key": [
        "x′ = A·x:  the arrow at a point is A·x",
        "A·v = λ·v   gives   x = e^(λt)·v",
        "λ² − τ·λ + Δ = 0   τ = trace, Δ = det",
        "Δ < 0 saddle;  Δ > 0 node, spiral, centre",
        "stable exactly when  Δ > 0  and  τ < 0",
        "nonlinear: linearise at an equilibrium",
    ],
    "assumes_short": "Oscillators, Damping and Resonance",
    "assumes_long": (
        "the previous course, Oscillators, Damping and Resonance, for the phase ellipse "
        "and for what damping does to a motion, together with Second-Order Linear "
        "Equations for the characteristic equation, repeated and complex roots, and an "
        "equation rewritten as a system; Euler's steps as exact fractions from "
        "Differential Equations and Euler's Method; equilibria and their stability from "
        "Equilibria, Stability and Phase Lines; and Algebra's Systems and Matrices for "
        "the product of a matrix and a vector and for the determinant"
    ),
    "outcomes_intro": (
        "By the end you can read a pair of equations as a field of arrows, find the "
        "directions along which a linear system moves in a straight line, write and fit "
        "its general solution, classify the origin from two numbers, and carry the "
        "classification to the equilibria of a nonlinear system while saying where it "
        "stops being valid."
    ),
    "outcomes": [
        ("Read a system as a vector field and step it exactly",
         "Say what the arrow at a point is, apply Euler's step to both unknowns, and "
         "describe a solution as a curve in the plane rather than a graph against time."),
        ("Find eigenvalues and eigenvectors and write the straight-line solutions",
         "Solve `λ² − τ·λ + Δ = 0`, find each direction `A·v = λ·v`, and write "
         "`e^(λt)·v`."),
        ("Fit the general solution to a starting point",
         "Write `C₁·e^(λ₁t)·v₁ + C₂·e^(λ₂t)·v₂`, solve for the constants exactly, and say "
         "which term dominates as `t` grows."),
        ("Classify the origin and decide its stability",
         "Use `τ`, `Δ` and `τ² − 4Δ` to name a saddle, node, spiral or centre, and "
         "state the criterion for asymptotic stability with its borderline cases."),
        ("Find and linearise the equilibria of a nonlinear system",
         "Solve `f = g = 0`, compute the Jacobian exactly at each, classify it, and say "
         "when the linearisation is inconclusive."),
        ("Read a model in the phase plane",
         "Locate the equilibria of predator and prey, competing species and an epidemic, "
         "classify them, and say what the picture does and does not prove."),
    ],
    "syllabus_intro": (
        "Linear systems first, because they can be solved completely and because "
        "everything after them borrows their language. The first five lessons turn a "
        "matrix into a picture, and a picture into a stability verdict. The second half "
        "uses that verdict on three models whose equations are not linear."
    ),
    "how_to": [
        "Work with the matrix, not the picture. The trace and the determinant are two "
        "exact numbers, and the type of the origin is decided by them before anything is "
        "drawn. Compute them by hand first, name the type, and then let the lab confirm "
        "it.",
        "Keep the exact and the drawn apart. The tiles are exact fractions or surds. The "
        "curves behind them are stepped in floating point so that they can be seen, and "
        "the legend says so. Euler's polygon in particular is a recipe, and on some "
        "systems it drifts away from the true curve in a way you can compute.",
        "Check a solution by substitution. A pair of formulas is a solution when "
        "both differentiate to the right combination of the pair, and the check is "
        "short and exact. It catches an eigenvector written the wrong way round, which "
        "a picture does not.",
        "Treat a direction as a direction. An eigenvector stands for a whole line, "
        "and any non-zero multiple of it is the same answer. The lab prints the "
        "smallest whole-number version, with its first non-zero entry positive.",
    ],
    "not_covered": [
        "Systems of three or more equations. The classification by trace and "
        "determinant is complete in the plane and nothing like it exists in three "
        "dimensions, so every system on the course has exactly two unknowns.",
        "Limit cycles, the Poincar&eacute;&ndash;Bendixson theorem, Hopf bifurcations and "
        "chaos. The nonlinear lessons classify equilibria and draw trajectories; they "
        "do not prove that a closed orbit exists, and the predator&ndash;prey lesson "
        "states its conserved quantity and shows the drawing.",
        "A proof that the linearisation predicts the nonlinear behaviour. The lessons "
        "state when it does (a saddle, a node or a spiral, where no eigenvalue has real "
        "part zero) and when it does not (a centre), and demonstrate the first case; the "
        "theorem that guarantees it belongs to a first course in dynamical systems.",
        "Exact stepping of a nonlinear system. A quadratic right-hand side roughly "
        "doubles the digits of every denominator at each step, so the labs draw "
        "nonlinear trajectories by floating point and say so; no tile takes its value "
        "from a drawn curve.",
        "Modelling as a skill. Predator and prey, competing species and the epidemic are "
        "each given with their equations and their assumptions named. Deriving a model "
        "from data, fitting its parameters and validating it are not here.",
    ],
    "footer_lead": (
        "Every trace, determinant, eigenvalue, eigenvector, fitted constant, Jacobian "
        "entry and equilibrium check on this course is an exact fraction or an exact "
        "surd, and a figure that is rounded is printed with the approximation sign and "
        "says so. The Euler columns are exact arithmetic applied to an approximate "
        "method: the fractions are right, and each is only as close to the curve as the "
        "step allows."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
