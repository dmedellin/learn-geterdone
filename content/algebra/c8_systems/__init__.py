"""Systems and Matrices."""


from . import part_a, part_b


COURSE = {
    "slug": "systems-and-matrices",
    "title": "Systems and Matrices",
    "level": "Advanced",
    "summary": (
        "Several equations at once, and the array that makes solving them mechanical: substitution, elimination, three-variable systems, row operations, Gaussian elimination, matrix arithmetic, determinants, inverses, and linear programming."
    ),
    "blurb": (
        "Solve for several unknowns together, then find the notation that removes the bookkeeping. A matrix is elimination with the letters deleted, which is why this course does elimination by hand first and only then writes it down as rows."
    ),
    "key": [
        "one solution, none, or infinitely many  —  and nothing else",
        "R2 → R2 − 3R1        an elimination step, written as a row operation",
        "det A = 0   ⟺   A has no inverse",
        "the optimum of a linear objective sits at a corner",
    ],
    "assumes_short": "Courses 1\u20137",
    "assumes_long": "lines, functions, and exact fraction arithmetic",
    "outcomes_intro": (
        "By the end you can choose and carry out an exact method for the two- and "
        "three-variable systems studied here, classify every outcome, and check the "
        "result against the original constraints."
    ),
    "outcomes": [
        ("Choose and execute a solving method",
         "Use a graph to classify and estimate, choose substitution or elimination for an exact two-variable solution, and extend elimination to three variables."),
        ("Translate and row reduce",
         "Write a system as an augmented matrix, perform reversible row operations, carry it to reduced row echelon form, and read unique, empty and parameterised solution sets."),
        ("Test and invert a coefficient matrix",
         "Compute a determinant, use it to decide uniqueness and invertibility, construct an inverse when one exists, and verify it by multiplication."),
        ("Optimise over linear constraints",
         "Build a closed, bounded feasible region, solve boundary pairs for its corners, reject infeasible crossings, and compare an objective at the surviving corners."),
    ],
    "syllabus_intro": (
        "Lessons 1 to 4 classify and solve systems by hand. Lessons 5 to 7 turn "
        "that work into row operations, reduction and matrix products; lessons 8 "
        "and 9 add determinants and inverses. Lesson 10 returns to two-variable "
        "systems to optimise over a bounded feasible region."
    ),
    "how_to": [
        "After each complete example, cover its answer and finish the faded rehearsal. The first decision is supplied; the remaining elimination, row operation, classification and check are yours.",
        "Keep everything in fractions. Row reduction produces thirds and sevenths immediately, and a decimal here compounds into a visibly wrong answer three rows later &mdash; which is why every lab on this course is exact.",
        "Predict the case or next operation before revealing a lab result. Then check a system in its original equations and an inverse by multiplying: a tidy derived matrix cannot certify the arithmetic that produced it.",
    ],
    "not_covered": [
        "Vector spaces, linear independence, rank as a general concept, and eigenvalues. This is the matrix algebra a school course needs, not a linear algebra course.",
        "Systems with more equations than unknowns, least squares, and numerical conditioning.",
        "The simplex algorithm. Linear programming here is done by evaluating the objective at every corner of a feasible region you can draw.",
    ],
    "footer_lead": (
        "Row reduction and every system solution on this course are computed in exact fractions &mdash; the arithmetic that goes visibly wrong in floating point is exactly the arithmetic these lessons are about. Where a lab reports an inverse it multiplies the two matrices together in front of you rather than claiming the result."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
