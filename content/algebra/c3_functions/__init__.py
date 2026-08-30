"""Lines, Functions and Graphs."""

from . import part_a, part_b

_LESSONS_BY_SLUG = {
    lesson["slug"]: lesson for lesson in part_a.LESSONS + part_b.LESSONS
}

# Keep the source records grouped by topic, but finish the line sequence before
# functions begin.  The inequality lesson needs only the six line lessons and
# Course 2; leaving it after inverses made the course change subjects twice.
_LESSON_ORDER = (
    "the-coordinate-plane",
    "graphing-a-linear-equation",
    "slope",
    "slope-intercept-form",
    "point-slope-and-standard-form",
    "parallel-and-perpendicular-lines",
    "linear-inequalities-in-two-variables",
    "what-a-function-is",
    "function-notation",
    "domain-and-range",
    "piecewise-functions",
    "transformations-of-graphs",
    "composition-of-functions",
    "inverse-functions",
)

COURSE = {
    "slug": "lines-functions-and-graphs",
    "title": "Lines, Functions and Graphs",
    "level": "Beginner → Intermediate",
    "summary": (
        "The plane, the line, and the idea of a function: slope and the forms of a linear equation, parallel and perpendicular, what makes a rule a function, domain and range, piecewise definitions, transformations, composition and inverses."
    ),
    "blurb": (
        "Put algebra on a picture. Slope and every form of a line, then the definition that organises the rest of the path &mdash; a function &mdash; with its notation, its domain, the transformations that move its graph, and its inverse."
    ),
    "key": [
        "m = (y₂ − y₁)/(x₂ − x₁)",
        "y = mx + b        y − y₁ = m(x − x₁)",
        "m₁m₂ = −1         perpendicular",
        "(f ∘ g)(x) = f(g(x))         f⁻¹(f(x)) = x",
    ],
    "assumes_short": "Courses 1–2",
    "assumes_long": "solving and rearranging linear equations",
    "outcomes_intro": (
        "By the end you can turn a linear equation or function rule into a checked "
        "graph, value or related rule, and justify each decision from the definition "
        "rather than from the picture alone."
    ),
    "outcomes": [
        ("Read and write a line four ways",
         "Move between slope-intercept, point-slope, standard form and two given points, and pick the form that makes the question easy."),
        ("Apply the definition of a function",
         "Decide whether a rule, a table or a graph defines a function, and say which input breaks it when one does."),
        ("State a domain and a range",
         "Find what a formula excludes &mdash; a zero denominator or a negative under "
         "a square root &mdash; write the domain in interval notation, and justify the "
         "range of a line, square or absolute-value rule from its outputs."),
        ("Transform, compose and invert",
         "Map a known point under `a·f(b(x − h)) + k`, compose two functions in the "
         "right order with the correct domain, and find and verify the inverse of a "
         "line or a restricted square."),
    ],
    "syllabus_intro": (
        "Lessons 1 to 7 are lines and the half-planes they bound. Lesson 8 defines a "
        "function; lessons 9 to 14 develop its notation, domain and range, piecewise "
        "rules, graph transformations, composition and inverse."
    ),
    "how_to": [
        "After each complete example, cover its answer and finish the faded rehearsal. "
        "The supplied first decision is guidance; the remaining algebra, graph check "
        "and explanation are yours.",
        "Sketch or predict before you reveal a lab result. A graph is most useful when "
        "it tests a claim you already made, not when it makes the claim for you.",
        "For transformations and composition, trace one input or one known point all "
        "the way through. The order becomes visible in the intermediate value, and a "
        "wrong order cannot hide behind a plausible final formula.",
    ],
    "not_covered": [
        "Continuity and limits. The word \"smooth\" is used informally here; making it precise is calculus.",
        "Polynomial and rational graphs beyond lines, which need factoring and arrive in courses 4 and 5.",
        "Conic sections. Circles and ellipses are not functions of `x`, and this course is about functions.",
    ],
    "footer_lead": (
        "Every curve on this course is drawn by evaluating the function at hundreds of points and joining them; nothing is a stored shape. When a lab marks a vertex or an intercept, the label and the picture come from the same computation, so the drawing cannot flatter the answer."
    ),
    "lessons": [_LESSONS_BY_SLUG[slug] for slug in _LESSON_ORDER],
}
