"""Duality and Sensitivity Analysis."""


from . import part_a, part_b


COURSE = {
    "slug": "duality-and-sensitivity-analysis",
    "title": "Duality and Sensitivity Analysis",
    "level": "Advanced",
    "summary": (
        "The second linear programme every linear programme carries: how to write it, why any "
        "feasible point of it certifies a bound on the first, why the two optima are equal, and "
        "what the final tableau will therefore tell you &mdash; what one more unit of a resource "
        "is worth and over what range, whether a product you have never made would pay, how to "
        "re-optimise after a change without starting over, and why a two-player game has a "
        "value."
    ),
    "blurb": (
        "Every linear programme carries a second one whose variables are prices, and the simplex "
        "method has been solving both of them the whole time. That single fact is a tool: a final "
        "tableau will price a resource, bound the change that price survives, price a column that "
        "is not in the model yet, and reject a new constraint without a re-solve. The course ends "
        "where duality stops being bookkeeping &mdash; a Pareto front traced by one parameter, "
        "and a zero-sum game whose minimax theorem is strong duality with different nouns."
    ),
    "key": [
        "primal  max cᵀx,  Ax ≤ b,  x ≥ 0",
        "dual    min bᵀy,  Aᵀy ≥ c,  y ≥ 0        (= ↔ free, one y per row)",
        "weak    cᵀx ≤ yᵀAx ≤ bᵀy                 for every feasible pair",
        "strong  cᵀx* = bᵀy*,   y* = c_BᵀB⁻¹      read off the final tableau",
        "CS      yᵢ > 0 ⟹ row i tight;  xⱼ > 0 ⟹ dual column j tight",
        "yᵢ = Δz* per unit of bᵢ, over a range from a ratio test — not a derivative",
    ],
    "assumes_short": "Linear Programming Models and The Simplex Method, especially the tableau as an inverted basis times the original data",
    "assumes_long": (
        "linear programming models and the simplex method from this path, in particular the "
        "final tableau read as the inverse of the basis times the original data, plus inverse "
        "matrices, matrix arithmetic, gaussian elimination, piecewise functions, interval and "
        "set-builder notation and linear inequalities from algebra, and nothing at all from "
        "discrete mathematics, which is what makes this the last course an algebra-only reader "
        "can take and a complete story on its own"
    ),
    "outcomes_intro": (
        "By the end you can write the dual of anything, prove a bound without solving, certify "
        "or refute a claimed optimum without solving, read four different sensitivity answers off "
        "one final tableau, re-optimise after a change, and recognise strong duality when it "
        "turns up wearing a different name."
    ),
    "outcomes": [
        ("Write the dual and interpret it",
         "One dual variable per constraint, one dual constraint per variable, the direction and "
         "sign rules applied correctly to a mixed-form problem &mdash; and each dual variable "
         "given units of objective per unit of right-hand side."),
        ("Certify a bound and certify an optimum",
         "Weak duality from any feasible pair, with the two sign restrictions that produce it; "
         "and complementary slackness used to confirm or refute a claimed primal optimum without "
         "running the algorithm."),
        ("Read the dual solution off a final tableau",
         "`y = c_BᵀB⁻¹` from the columns that started as the identity, checked for dual "
         "feasibility column by column and for `bᵀy = z*` exactly."),
        ("Compute every range the solution is valid over",
         "A shadow price with its right-hand-side range, an objective coefficient's range for a "
         "basic and for a nonbasic variable, and the statement of which of the solution and its "
         "value changes in each case."),
        ("Decide about something not in the model",
         "Price a proposed new activity by `cₙₑw − yᵀaₙₑw` and test a proposed new constraint at "
         "the current optimum &mdash; and re-optimise by the dual simplex only when one of them "
         "says you must."),
        ("Recognise duality elsewhere",
         "Trace a two-objective Pareto front by one parameter with exact breakpoints, and solve "
         "a zero-sum game as a pair of dual linear programmes whose common value is the value of "
         "the game."),
    ],
    "syllabus_intro": (
        "Construction, then the two theorems, then the four things a final tableau will tell "
        "you, then the two ways to use them on a problem that has changed, and last two places "
        "where duality is the content rather than the method."
    ),
    "how_to": [
        "Put units on every dual variable the moment you write it. A dual variable whose units "
        "you cannot state is a dual variable you have paired with the wrong constraint, and the "
        "check costs ten seconds.",
        "Never quote a shadow price without its range. The lab prints them together and this "
        "course never separates them; a price outside its range is not approximately right, it is "
        "a different number.",
        "Before running the dual simplex, try to say which basis the answer will end up in. You "
        "are usually wrong, and being wrong deliberately is how the ratio test on the objective "
        "row stops being a rule and starts being a reason.",
        'Do “Complementary Slackness” with a degenerate instance as well as a clean one. It is '
        "where degeneracy first bites, and a reader who has only seen the conditions behave will "
        "assert the converse for years.",
    ],
    "not_covered": [
        "Farkas' lemma and the theorems of the alternative as a topic. Strong duality is obtained "
        "constructively from the final tableau, which is the version a reader can execute; the "
        "separating-hyperplane route is named and declined.",
        "Lagrangian duality, and duality for anything non-linear. Both need machinery this path "
        "refuses.",
        "Parametric analysis of the constraint matrix `A`. Ranging here is on `b` and on `c`; "
        "changing `A` changes the basis matrix itself and is a different subject.",
        "Degeneracy's full effect on sensitivity. This course says what goes wrong &mdash; a "
        "tight constraint can have a zero price, and a range can end at the value the "
        "right-hand side already has &mdash; and does not develop the theory of the multiple dual "
        "solutions that cause it.",
        "Interpreting a shadow price as a market price. The course says repeatedly what it is (a "
        "rate of change over a range, inside this model) and declines the economics.",
    ],
    "footer_lead": (
        "Shadow prices, ranges and breakpoints on this course are exact fractions, and the range "
        "is printed with the price every time &mdash; a price without its range is a number with "
        "no claim attached, and this course never prints one. Nothing here is a derivative: `z*` "
        "is piecewise linear in each right-hand side and has a corner at every breakpoint, where "
        "a slope from the left and a slope from the right are both true and different."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
