"""Geometric Algorithms."""


from . import part_a, part_b


COURSE = {
    "slug": "geometric-algorithms",
    "title": "Geometric Algorithms",
    "level": "Advanced",
    "summary": (
        "One 2&times;2 determinant, and the sign of it. Which side of a line, whether two "
        "segments meet, which corners survive on a hull, how much area a polygon encloses, "
        "which pair is closest &mdash; every one of them is that sign, and the course is "
        "about what happens when the arithmetic that produces it is not exact."
    ),
    "blurb": (
        "Every other course on this path measures an algorithm. This one measures a "
        "PREDICATE: the same orientation test in exact integers and in double precision, on "
        "29 magnitudes of the same input, with the wrong answers counted rather than warned "
        "about. The failure turns out to have a shape &mdash; the rounded test can lose a "
        "turn and provably cannot invent the opposite one &mdash; and the rest of the course "
        "is what that sign is used for, with degenerate input treated as the subject rather "
        "than excluded from it."
    ),
    "key": [
        "orient(a, b, c) = (bx − ax)(cy − ay) − (by − ay)(cx − ax)",
        "sign 1 left, −1 right, 0 collinear   -   the magnitude is twice an area",
        "in doubles: 22 of 29 swept magnitudes wrong, the first at 2²⁷",
        "the rounded predicate collapses to 0 and never reports the other turn",
        "a square with a midpoint per side: 4 vertices, 6 wrapped, 8 on the boundary",
        "four zero signs, two inputs, opposite answers",
    ],
    "assumes_short": "Sorting, divide and conquer, the 2×2 determinant, big-O",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: Big-O, Big-Omega and Big-Theta, "
        "Analysing Iterative Algorithms, Recursion Trees and the Master Theorem, Loop "
        "Invariants and Program Correctness, and Strong Induction, which every proof here "
        "uses. From Algebra, The Coordinate Plane, and the 2×2 determinant, which is defined "
        "inline on the opening page so that a reader who has not taken Algebra's course on "
        "systems and matrices loses nothing. From this path: Data Structures, for the sorted "
        "order a sweep line maintains and the balanced tree behind it; Sorting and "
        "Selection, whose comparison count is quoted here and re-derived nowhere, and whose "
        "lower bound is what the convex-hull reduction is a reduction to; and Graph "
        "Algorithms, for nothing beyond the habit of putting a measured count beside a "
        "proved bound"
    ),
    "outcomes_intro": (
        "By the end you can reduce a geometric question to the sign of a determinant, say at "
        "what magnitude a floating-point version of that determinant stops being reliable "
        "and what its failure can and cannot look like, handle collinear and duplicate input "
        "as cases with answers rather than as input to reject, and read every count on these "
        "pages as a measurement of the points on screen."
    ),
    "outcomes": [
        ("Reduce the question to one sign",
         "Side of a line, segment crossing, polygon orientation, hull corner, and the "
         "comparison that drives a rotating caliper &mdash; each written as a determinant "
         "compared against zero, with no division, no square root and no angle anywhere."),
        ("Say when the arithmetic can be trusted, and what it does when it cannot",
         "Derive the `2k &gt; 53` threshold from the width of a double's significand, read "
         "the swept count off the page as a measurement of a constructed family, and prove "
         "that a rounded orientation can only collapse to zero &mdash; so a hull can lose a "
         "vertex and cannot gain one."),
        ("Treat degeneracy as the subject",
         "Three collinear points, a duplicate point, a hull that is a segment, a segment "
         "that is a point, a ray through a vertex, two collinear segments with identical "
         "signs and opposite answers. Each is a case with a right answer, and in one of them "
         "three correct procedures give 4, 6 and 8."),
        ("Read a count as a count",
         "Every figure on these pages comes from running the algorithm on the input shown. "
         "Three pages here have the measured column and the proved bound disagreeing "
         "sharply &mdash; 5 strip comparisons against 84, 36 wrapping comparisons against a "
         "reference of 27, and a sweep that makes every test the brute force makes &mdash; "
         "and each one says which number is which."),
    ],
    "syllabus_intro": (
        "The determinant first, then the magnitude at which a floating-point version of it "
        "loses the sign, then the corner that costs; then hulls, where a collinear point "
        "produces three different right answers, and the diameter the hull makes cheap; "
        "then segments, where four signs settle the easy case and two inputs with identical "
        "signs have opposite answers; and last area, inside, and distance, where the "
        "measured column and the proved bound sit furthest apart."
    ),
    "how_to": [
        "Type the near-degenerate worked example before the ordinary one. Every lab on this "
        "course opens on a case chosen to be interesting, and the preset lists are ordered "
        "so that the textbook input comes first and the input that breaks the textbook "
        "method comes later. A reader who only ever looks at the first entry will see a "
        "course in which nothing goes wrong.",
        "Change one control at a time and watch which figures move. The hull page runs both "
        "predicates on every redraw, so the two vertex counts are always side by side; the "
        "sweep page's status list is what explains its pair-test count; the polygon page's "
        "sign flips when you reverse the vertex order and the area does not. A figure that "
        "moves with a control you did not expect to matter is the most useful thing on the "
        "page.",
        "Read every count as a fact about the points on screen. The sweep saves twelve pair "
        "tests out of fifteen on one input and none out of six on another; gift wrapping does "
        "36 comparisons against a reference of 27 on the nine points the hull page opens "
        "with, and 72 against 96 on 24 points with only three on the hull. None of those is "
        "a property of an algorithm, and every page that prints one says so.",
    ],
    "not_covered": [
        "Voronoi diagrams, Delaunay triangulation, and the lifting to a paraboloid that "
        "connects them to hulls in three dimensions. The lifting of points to a parabola "
        "appears here only as the reduction that gives the convex-hull lower bound; the "
        "structures themselves are a course of their own and nothing on this one depends on "
        "them.",
        "Linear programming in fixed dimension, smallest enclosing circles, and the "
        "randomised incremental methods that solve both in expected linear time. They are "
        "geometry and they are also an application of the probabilistic analysis this path "
        "develops later, so they belong beside that rather than here.",
        "Floating-point filters and adaptive exact arithmetic &mdash; evaluating a predicate "
        "in doubles with an error bound and falling back to exact arithmetic only when the "
        "bound is too loose to decide. It is what production geometry kernels actually do, "
        "and it is a numerical-analysis argument rather than a geometric one; these pages "
        "compute every predicate exactly and say so.",
        "Geometry in three or more dimensions, and range-searching structures. A k-d tree "
        "and a two-dimensional range query are in the kit this course draws on and no lesson "
        "here uses them: the pruning a range query achieves is a property of the window "
        "rather than of the tree, which is the same lesson the sweep-line page already "
        "carries, and building the tree is a balanced-search-tree question that Data "
        "Structures owns.",
    ],
    "footer_lead": (
        "Every count on this course is produced by running the algorithm on the points you "
        "typed. Determinants, doubled areas, squared distances, hull sizes, pair tests, "
        "stack operations and crossing counts are exact integers, computed in "
        "arbitrary-precision arithmetic, and no page here rounds one. Areas and "
        "comparisons-per-point are exact fractions, printed as fractions with a decimal "
        "beside them for reading rather than instead of them. Three quantities on these "
        "pages are not exact and each is labelled where it appears: the double-precision "
        "determinant, which &ldquo;The Magnitude Where Doubles Lose the Sign&rdquo; measures "
        "rather than a defect; the "
        "`n` times `log₂ n` reference column on the convex-hull page, which is a function "
        "evaluated at the number of points on screen and carries no verdict; and the decimal "
        "printed beside each exact fraction. Every algorithm is checked against a route that "
        "shares no code with it &mdash; the hull against the separating-line definition by "
        "brute force, the four-sign segment test against an exact solve for the two "
        "parameters, the shoelace area against the trapezoid rule, ray parity against the "
        "winding number, and the sweep, the calipers and the closest-pair recursion each "
        "against testing every pair &mdash; and where two exact routes disagree the page "
        "says so and declines to name a winner. What the labs cannot do is quantify over "
        "inputs: 22 wrong signs out of 29 magnitudes, 6 pair tests out of 6, and 5 strip "
        "comparisons against a bound of 84 are all measurements of the input shown, and each "
        "page names the proof that the corresponding claim rests on instead."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
