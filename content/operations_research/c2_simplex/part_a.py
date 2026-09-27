"""The Simplex Method, lessons 01-05 - the walk, the tableau, the ratio test,
the reduced cost, and manufacturing a start.

Every figure below is a figure the kit computes. `scripts/mathcheck.js` pins
the two named pathologies and the four-rule counts, so a number here that
disagrees with the lab is a defect in this file rather than a second opinion.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "adjacent-corners-and-the-simplex-idea",
        "title": "Adjacent Corners and the Simplex Idea",
        "module": "The walk",
        "one_line": "Trace a simplex path corner by corner, naming the basis at each and the single variable exchanged between them.",
        "summary": (
            "Every corner of a feasible region is named by a set of columns called a "
            "basis. Two corners are joined by an edge exactly when their bases differ "
            "in one column, and one step of the simplex method is one such exchange. "
            "So the method never enters the interior and never tries every corner: it "
            "walks a path along the boundary, uphill, and stops at the first corner "
            "with no improving edge leaving it."
        ),
        "key": [
            "basis       m columns of [A | b]; every other variable sits at zero",
            "corner      the point that basis reads off the right-hand column",
            "adjacent    two bases differing in EXACTLY one column",
            "edge        the segment joining two adjacent corners",
            "one pivot   one column in, one column out  =  one edge",
            "stop        no improving edge leaves this corner ⟹ it is optimal",
        ],
        "key_label": "A basis, a corner, and what counts as one step",
        "concepts_intro": (
            "“Standard Form, Slack and Surplus” wrote the programme as equations and "
            "“Basic Solutions and Corners” paired a choice of columns with a point. One "
            "idea is new here, and it is what makes a <em>step</em> mean something."
        ),
        "concepts": [
            ("A basis names the corner",
             "Choose `m` of the columns of the `m`-row system and set every other "
             "variable to zero; solving the `m` remaining equations gives one point. "
             "The chosen columns are the <strong>basis</strong>, their variables are "
             "<strong>basic</strong>, and when all of them come out at or above zero "
             "the point is a corner of the feasible region. The region of `maximise "
             "3x₁ + 5x₂` under `x₁ ≤ 4`, `2x₂ ≤ 12`, `3x₁ + 2x₂ ≤ 18` has five "
             "corners, and five bases to match."),
            ("Adjacent means one column different",
             "A basis is a set, so the distance between two of them is the size of "
             "their difference. `{s₁, s₂, s₃}` and `{s₁, x₂, s₃}` differ in one "
             "member: `x₂` in, `s₂` out. That is one edge of the region and one pivot "
             "of the method. `{s₁, s₂, s₃}` and `{x₁, s₂, x₂}` differ in two, and no "
             "single pivot goes there however short the line looks on the picture."),
            ("The method walks a path, not a census",
             "On the five-corner region above, the method starting from the origin "
             "reaches the optimum after two pivots, standing at three corners and "
             "never looking at the other two. Corner-counting and work are different "
             "quantities, which is why a region with a thousand corners is not a "
             "thousand times the work of one with ten."),
        ],
        "read_title": "Corners, bases, and the one exchange that is a step",
        "read_intro": "Which point a basis names, when two of them are one edge apart, and what licences the method to stop walking.",
        "body": [
            ("def", ("Basis, basic solution, basic feasible solution",
                    "For a standard-form system with `m` equations and `n ≥ m` "
                    "columns, a <strong>basis</strong> is a choice of `m` columns "
                    "whose matrix is invertible. Setting the other `n - m` variables "
                    "to zero and solving for the basic ones gives the "
                    "<strong>basic solution</strong> belonging to that basis. If every "
                    "basic variable comes out at or above zero it is a <strong>basic "
                    "feasible solution</strong>, and it is a corner of the feasible "
                    "region.")),
            ("p", "Nothing in that definition mentions the objective. A basis is a "
                  "choice of columns, the point follows from the choice, and the "
                  "objective only decides which of these points you want. Two "
                  "different bases can even name the same point &mdash; which is "
                  "degeneracy, and “Degeneracy, Cycling and Bland&rsquo;s Rule” is "
                  "where it matters."),
            ("example", ("The five corners of one small region, and their bases",
                         "Take `maximise 3x₁ + 5x₂` subject to `x₁ ≤ 4` (plant A "
                         "hours), `2x₂ ≤ 12` (plant B hours) and `3x₁ + 2x₂ ≤ 18` "
                         "(plant C hours), with one slack per row. Every column is "
                         "one of `x₁, x₂, s₁, s₂, s₃`, three of them are basic, and "
                         "the region has five corners.",
                         "`(0, 0)` stands on `{s₁, s₂, s₃}` at `z = 0`; `(0, 6)` on "
                         "`{s₁, x₂, s₃}` at `30`; `(2, 6)` on `{s₁, x₂, x₁}` at `36`; "
                         "`(4, 0)` on `{x₁, s₂, s₃}` at `12`; `(4, 3)` on "
                         "`{x₁, s₂, x₂}` at `27`. The basis at the origin is the three "
                         "slacks, which is what makes the origin the free starting "
                         "corner of a programme with only `≤` rows.")),
            ("def", ("Adjacent bases, and an edge",
                    "Two bases are <strong>adjacent</strong> when they differ in "
                    "exactly one column. The corners they name are then the two ends "
                    "of one <strong>edge</strong> of the feasible region, and one "
                    "<strong>pivot</strong> of the simplex method moves between them: "
                    "one column enters the basis and one leaves.")),
            ("p", "Read the two verdicts off the sets rather than off the drawing. "
                  "From `{s₁, s₂, s₃}` at the origin, `{s₁, x₂, s₃}` is one exchange "
                  "away and so is `{x₁, s₂, s₃}` &mdash; the two edges of the region "
                  "that leave the origin. `{x₁, s₂, x₂}` at `(4, 3)` needs `s₁` and "
                  "`s₃` out and `x₁` and `x₂` in: two changes at once, so no pivot "
                  "goes there. The lab refuses that move and prints the two columns "
                  "that would have had to change together."),
            ("h3", "The walk, and the licence to stop"),
            ("p", "From the origin the method takes the edge to `(0, 6)`, raising `z` "
                  "from `0` to `30`, then the edge to `(2, 6)`, raising it to `36`. "
                  "At `(2, 6)` every edge leaving the corner lowers `z`, so it stops. "
                  "Two pivots, three corners visited, two corners never examined."),
            ("thm", ("Why a corner with no improving edge is the best corner anywhere",
                     "A linear objective on a convex feasible region has no local "
                     "maximum that is not a global maximum. Convexity, and Why a "
                     "Local Optimum Is Global proves this, and it is the whole "
                     "licence for stopping: the method checks the edges at one corner "
                     "and concludes something about every point of the region.")),
            ("p", "That licence is what separates this from hill climbing. A method "
                  "that walks uphill on an arbitrary surface can only report a local "
                  "summit; here the surface is a plane and the region has no dents in "
                  "it, so a corner that beats its neighbours beats everything. "
                  "Without that theorem the method would be a heuristic."),
            ("p", "It also explains why the number of corners is not the amount of "
                  "work. A programme with `n` columns and `m` rows has at most `n` "
                  "choose `m` bases, which grows ferociously, and the region above "
                  "has ten possible choices of three columns from five, of which five "
                  "are corners. The method visited three. Termination and the "
                  "Klee&ndash;Minty Cube is where the honest count lives, and the news "
                  "there is mixed."),
            ("p", "One warning about reading a basis off a picture: the basis is not "
                  "&ldquo;the variables that are not zero&rdquo;. At a corner where "
                  "three boundary lines meet, one basic variable is zero as well, and "
                  "two different bases name that single point. That is the subject of "
                  "“Degeneracy, Cycling and Bland&rsquo;s Rule” and it is worth knowing "
                  "now, because it is the one case where corner and basis stop being "
                  "the same thing."),
        ],
        "lab": ("simplex", {
            "mode": "walk",
            "panel_title": "Choose two corners and ask for the move",
            "panel_intro": "Every corner's basis is built by pivoting to it, so the "
                           "verdict on a move is the size of the difference between "
                           "two sets of columns &mdash; not a distance on the picture.",
        }),
        "steps_title": "Following a simplex walk on a region you can draw",
        "steps_intro": "Bases first, objective last. A move that is not an exchange of one column is not a step, whatever it does to the objective.",
        "steps": [
            ("List the columns before looking for corners",
             "Write the programme in standard form and name every column, slacks "
             "included. On a three-row problem a basis is three of those names, and "
             "you cannot say which corners exist until you know what there is to "
             "choose from."),
            ("Read the point off the basis you are standing on",
             "Set the nonbasic variables to zero and solve for the rest. Check the "
             "signs: a negative basic variable means the choice of columns was not a "
             "corner of the feasible region at all, only a solution of the equations."),
            ("Ask which corners are one column away",
             "Compare the sets. One member different is an edge and a candidate for "
             "the next pivot; two or more is not reachable in one step, and that is "
             "true no matter how close the two corners look."),
            ("Take an improving edge, and stop when there is none",
             "Move along an edge that raises the objective, then repeat from the new "
             "corner. When every edge leaving the corner lowers it, stop and say why: "
             "a linear objective on a convex region has no local optimum that is not "
             "global."),
        ],
        "worked": {
            "title": "The walk on two products across three plants",
            "intro": [
                "Five corners, five bases, and a path that visits three of them. The "
                "objective is `3x₁ + 5x₂` and the three rows are the plant hours.",
            ],
            "lines": [
                "maximise  3x1 + 5x2",
                "    x1                 <= 4     plant A hours     s1 = 4  - x1",
                "          2x2          <= 12    plant B hours     s2 = 12 - 2x2",
                "    3x1 + 2x2          <= 18    plant C hours     s3 = 18 - 3x1 - 2x2",
                "",
                "corner    basis            z     one edge from (0, 0)?",
                "(0, 0)    {s1, s2, s3}     0     standing here",
                "(0, 6)    {s1, x2, s3}    30     yes:  x2 in,  s2 out",
                "(4, 0)    {x1, s2, s3}    12     yes:  x1 in,  s1 out",
                "(2, 6)    {s1, x2, x1}    36     no:   2 columns differ",
                "(4, 3)    {x1, s2, x2}    27     no:   2 columns differ",
                "",
                "the walk from the slack basis",
                "  pivot 1   x2 in, s2 out    (0, 0) -> (0, 6)    z: 0  -> 30",
                "  pivot 2   x1 in, s3 out    (0, 6) -> (2, 6)    z: 30 -> 36",
                "  stop: every edge leaving (2, 6) lowers z",
                "",
                "5 corners in the region, 3 stood at, 2 pivots",
            ],
            "after": [
                "The refusal is the part worth dwelling on. `(0, 0)` and `(4, 3)` are "
                "not far apart on the drawing, and a reader who thinks of the method "
                "as &ldquo;try corners, keep the best&rdquo; sees no reason not to go "
                "there. But `{s₁, s₂, s₃}` and `{x₁, s₂, x₂}` differ in two columns, "
                "and one pivot exchanges one column. There is no edge between those "
                "two corners, and the method walks the boundary rather than crossing "
                "the middle.",
                "For a faded rehearsal, change the objective to `2x₁ + 3x₂` in the "
                "lab and predict the walk before running it. The supplied first move "
                "is that the corner list and the five bases do not change &mdash; "
                "they are a property of the constraints. Say which corner is optimal "
                "now, how many pivots reach it from the origin, and which corners are "
                "skipped, then check all three against the panel.",
                "Then push the objective coefficient on `x₁` up to `9`. The walk goes "
                "the other way round the region, the corner list is still the same "
                "five points, and the number of pivots changes. That separation "
                "&mdash; the region fixes the corners, the objective fixes the path "
                "&mdash; is what the rest of this course is built on.",
            ],
        },
        "quiz_title": "Bases, edges and the count of work",
        "quiz": [
            {"q": "A three-row programme has columns `x₁, x₂, s₁, s₂, s₃`. How many pivots move from the basis `{x₁, s₂, s₃}` to the basis `{x₁, s₂, x₂}`?",
             "a": ["None &mdash; they name the same point",
                   "One",
                   "Two",
                   "It depends on the objective coefficients"],
             "c": 1,
             "why": "The two sets differ in one member: `x₂` enters and `s₃` leaves. "
                    "One column exchanged is one pivot, and the objective has no say "
                    "in whether the exchange is possible &mdash; only in whether the "
                    "method would choose it."},
            {"q": "On the five-corner region of the worked example the method reaches the optimum in two pivots. At how many corners does it stand along the way, counting the one it starts from?",
             "a": ["Two", "Three", "Five", "Ten"],
             "c": 1,
             "why": "It starts at `(0, 0)`, and each pivot moves it to one new "
                    "corner: `(0, 6)` then `(2, 6)`. Three corners. `Two` counts the "
                    "pivots instead of the corners, `five` assumes every corner is "
                    "examined, and `ten` is the number of ways to choose three "
                    "columns from five, most of which are not corners at all."},
            {"q": "Every edge leaving the current corner lowers the objective. Why does that settle the whole region rather than just this corner's neighbourhood?",
             "a": ["Because every other corner has already been evaluated",
                   "Because a linear objective on a convex region has no local maximum that is not global",
                   "Because the objective falls in every direction from every corner of any region",
                   "Because the method visits corners in order of decreasing objective value"],
             "c": 1,
             "why": "The licence comes from Convexity, and Why a Local Optimum Is "
                    "Global, and it is a statement about the region and the objective "
                    "rather than about the search. No other corner has been "
                    "evaluated, the objective certainly does not fall in every "
                    "direction from every corner, and the method visits corners in "
                    "increasing order of objective value, not decreasing."},
        ],
        "mistakes": [
            ("Treating the method as a search over all the corners",
             "Five corners were available in the worked example and three were stood "
             "at. The method follows one path and the corners off that path are never "
             "built, which is the only reason a programme with a hundred rows is "
             "solvable at all. &ldquo;Try every corner and keep the best&rdquo; is a "
             "correct algorithm and a different one, and it is what “Systems of "
             "Inequalities and Linear Programming” did on regions small enough to draw."),
            ("Calling two corners adjacent because they look close",
             "On a square region cut out by `x₁ ≤ 3` and `x₂ ≤ 3` the corners `(0, 0)` "
             "and `(3, 3)` are the diagonal: their bases differ in two columns, so no "
             "pivot joins them, while `(0, 0)` and `(0, 3)` differ in one and are one "
             "step apart. Adjacency is arithmetic on sets of columns and the picture "
             "has no vote."),
            ("Reading the basis as whichever variables are not zero",
             "That works until three constraint boundaries pass through one corner. "
             "Then one basic variable is zero as well, the non-zero variables are too "
             "few to fill the basis, and two different bases name the same point. "
             "“Degeneracy, Cycling and Bland&rsquo;s Rule” is about exactly that case, "
             "and it is why the basis is defined as the chosen columns rather than as "
             "the positive values."),
        ],
        "standard": ("Finish when you can say which corners are one pivot away without looking at the drawing.",
                     "You should be able to write a small programme in standard form, "
                     "list the basis at each corner, decide adjacency by comparing "
                     "sets of columns, and state the theorem that lets a check at one "
                     "corner settle the whole region."),
        "note": "Nothing above needed a tableau: the corners were found by drawing and the bases read off afterwards, which stops working the moment there are more than two decision variables. “The Simplex Tableau” is the bookkeeping that carries one basis and lets the next one be produced by arithmetic instead of by geometry &mdash; and the arithmetic is “Gaussian Elimination” from the Algebra path, with one extra row attached.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-simplex-tableau",
        "title": "The Simplex Tableau",
        "module": "One pivot",
        "one_line": "Build the initial tableau from standard form, read its basic feasible solution off it, and carry out one named pivot exactly.",
        "summary": (
            "A tableau is the standard-form system `[A | b]` with one extra row for "
            "the objective, `z - cᵀx = 0`. When the basic columns are identity "
            "columns the basic feasible solution can be read straight out of the "
            "right-hand column with no solving at all, and one step of the method is "
            "a single Gauss-Jordan pivot applied to every row of the tableau &mdash; "
            "the objective row included, because it is one more equation."
        ),
        "key": [
            "tableau     [A | b] of standard form, with one more row underneath",
            "z-row       z - cᵀx = 0,  so the row starts out holding  -c",
            "basic col   an identity column; that row's rhs IS the variable's value",
            "nonbasic    held at zero, which is what makes the reading free",
            "pivot (r,j) divide row r by a_rj, then clear column j in every other row",
            "            - the z-row included, because it is one more equation",
        ],
        "key_label": "The parts of a tableau, and what one pivot does to them",
        "concepts_intro": (
            "The arithmetic is “Gaussian Elimination” and nothing else. What is new is "
            "the extra row, and the habit of <em>reading</em> a solution instead of "
            "solving for one."
        ),
        "concepts": [
            ("The tableau is a system, not a table of workings",
             "Every row is an equation that stays true. The top `m` rows are the "
             "constraints in standard form, and the bottom row is the objective "
             "rearranged to `z - c₁x₁ - … - cₙxₙ = 0`, which is why it begins life "
             "holding the negated objective coefficients. Nothing in the tableau is a "
             "note to yourself; it is all the same system written in a different basis."),
            ("A basic feasible solution is read, not computed",
             "When the basic columns are identity columns, row `i` says `x_{B(i)} + "
             "(nonbasic terms) = b_i`, and the nonbasic terms are all zero. So the "
             "basic variable in row `i` equals that row's right-hand entry, every "
             "other variable is zero, and the bottom-right entry is `z`. That free "
             "reading is the entire reason for keeping the tableau in this shape."),
            ("A pivot is one Gauss-Jordan step on every row",
             "Choose an entry `a_rj` that is not zero. Divide row `r` by it so the "
             "entry becomes `1`, then subtract multiples of that row from every other "
             "row until the rest of column `j` is zero. Column `j` is now an identity "
             "column and the column that used to carry row `r`'s basic variable is "
             "not, so `x_j` has entered the basis and that variable has left."),
        ],
        "read_title": "Building the tableau, reading it, and pivoting it once",
        "read_intro": "Where every entry comes from, why the objective row is inside the row operations rather than beside them, and what an illegal pivot produces.",
        "body": [
            ("def", ("Simplex tableau",
                    "For a standard-form programme `maximise cᵀx` subject to "
                    "`Ax = b`, `x ≥ 0` with `A` of size `m × n`, the "
                    "<strong>tableau</strong> at a basis `B` is the `m` constraint "
                    "rows together with an <strong>objective row</strong> "
                    "representing `z - cᵀx = 0`. It is held so that each basic "
                    "column is an identity column and the objective row has a zero in "
                    "every basic column.")),
            ("p", "“Standard Form, Slack and Surplus” already did the work of turning "
                  "inequalities into equations. Take `maximise 3x₁ + 5x₂` subject to "
                  "`x₁ ≤ 4`, `2x₂ ≤ 12`, `3x₁ + 2x₂ ≤ 18`; add one slack per row and "
                  "the three slacks are already an identity, so the first tableau "
                  "needs no work beyond writing `-3` and `-5` in the objective row."),
            ("math", [
                "              x1    x2    s1    s2    s3   |   rhs",
                "   s1          1     0     1     0     0   |     4",
                "   s2          0     2     0     1     0   |    12",
                "   s3          3     2     0     0     1   |    18",
                "   z          -3    -5     0     0     0   |     0",
            ]),
            ("p", "Read it. The basic columns are `s₁, s₂, s₃`, so `s₁ = 4`, "
                  "`s₂ = 12`, `s₃ = 18`, the nonbasic `x₁` and `x₂` are zero, and "
                  "`z = 0`. That is the origin, and the three slacks at their full "
                  "values say that no plant hours have been used. Nothing was solved: "
                  "the right-hand column was copied out."),
            ("def", ("Pivot",
                    "A <strong>pivot</strong> on row `r` and column `j` with "
                    "`a_rj ≠ 0` is the pair of row operations: replace row `r` by "
                    "`row r ÷ a_rj`, then for every other row &mdash; "
                    "<strong>including the objective row</strong> &mdash; replace it "
                    "by `row - (its entry in column j) × (the new row r)`. The "
                    "<strong>entering</strong> variable is `x_j` and the "
                    "<strong>leaving</strong> variable is the one row `r` was "
                    "carrying.")),
            ("p", "Take the pivot on row `2`, column `x₂`, whose entry is `2`. "
                  "Halving row `2` makes it `1`. Row `1` has a zero in column `x₂` so "
                  "it does not change at all. Row `3` has a `2` there, so it loses "
                  "twice the new row `2`. The objective row has `-5`, so it gains five "
                  "times the new row `2`."),
            ("math", [
                "   R2' = R2 ÷ 2         [ 0    1    0   1/2   0  |   6 ]",
                "   R1' = R1 - 0·R2'     [ 1    0    1    0    0  |   4 ]",
                "   R3' = R3 - 2·R2'     [ 3    0    0   -1    1  |   6 ]",
                "   z'  = z  + 5·R2'     [-3    0    0   5/2   0  |  30 ]",
                "",
                "              x1    x2    s1    s2    s3   |   rhs",
                "   s1          1     0     1     0     0   |     4",
                "   x2          0     1     0    1/2    0   |     6",
                "   s3          3     0     0    -1     1   |     6",
                "   z          -3     0     0    5/2    0   |    30",
            ]),
            ("p", "The basis is now `{s₁, x₂, s₃}`. Reading again: `x₂ = 6`, `s₁ = 4`, "
                  "`s₃ = 6`, `x₁ = 0`, `z = 30`. That is the corner `(0, 6)` and the "
                  "objective value listed for it in “Adjacent Corners and the Simplex Idea”. One "
                  "pivot, one "
                  "edge, and the new reading is free for the same reason the old one was."),
            ("h3", "Why the objective row goes through the pivot"),
            ("p", "Because it is an equation. `z - 3x₁ - 5x₂ = 0` is as true as the "
                  "three constraint rows, and a row operation that keeps a system "
                  "equivalent has to be applied to all of it. Carry the objective row "
                  "along and the bottom-right entry is always the objective value at "
                  "the current basis, with no separate arithmetic to get wrong."),
            ("p", "Leave it out and the tableau still looks finished: the constraint "
                  "rows are right, the reading of `x` is right, and only `z` and the "
                  "objective row entries are stale. This is the same error as dropping "
                  "the constant column part-way through an elimination, which "
                  "“Gaussian Elimination” named on the Algebra path, and it fails the "
                  "same way &mdash; silently, with a plausible answer at the end."),
            ("h3", "A pivot you are allowed to do and should not"),
            ("p", "Any non-zero entry is a legal row operation, and the arithmetic "
                  "does not care whether the result is a corner. Pivot the same "
                  "tableau on row `3` and column `x₂` instead and you get `x₂ = 9`, "
                  "`s₂ = -6`, a bottom-right entry of `45` &mdash; higher than the "
                  "true optimum of `36` &mdash; and a point, `(0, 9)`, that is outside "
                  "the region because it uses `18` of plant B's `12` hours. The "
                  "tableau is a correct system throughout; what it has stopped "
                  "describing is a feasible point."),
            ("p", "Choosing the row so that this cannot happen is “The Ratio Test”, and "
                  "choosing the column so that the objective actually improves is "
                  "“Reduced Costs and the Optimality Test”. Until then, pivot by hand "
                  "and check the right-hand column for a negative entry every time."),
        ],
        "lab": ("simplex", {
            "mode": "pivot",
            "panel_title": "Name the row and the column yourself",
            "panel_intro": "Every row operation is printed, the objective row beside "
                           "the others, and an illegal pivot is carried out rather "
                           "than blocked &mdash; the negative right-hand side it "
                           "produces is the evidence.",
        }),
        "steps_title": "Building and pivoting a tableau by hand",
        "steps_intro": "Two minutes of setup saves the error that is hardest to find later: a tableau that is arithmetically perfect and describes the wrong system.",
        "steps": [
            ("Put the programme in standard form first",
             "One slack per `≤` row, and the objective rearranged to `z - cᵀx = 0`. "
             "Write the column names across the top and keep them; half the mistakes "
             "in a tableau are a column read in the wrong place."),
            ("Write the objective row as the negated coefficients",
             "`maximise 3x₁ + 5x₂` gives `-3` and `-5`, not `3` and `5`. The row is "
             "the equation `z - 3x₁ - 5x₂ = 0` with the `z` column left implicit, and "
             "the sign is what makes an improving column show up as a negative entry."),
            ("Read the solution before doing anything to it",
             "Name the basic variable of each row, copy the right-hand entry as its "
             "value, set the rest to zero, and read `z` from the bottom right. If any "
             "basic value is negative, stop: this tableau is not at a corner."),
            ("Pivot: divide the row, then clear the column everywhere",
             "New row `r` is the old one over `a_rj`. Then every other row, objective "
             "row included, loses its column-`j` entry times the new row `r`. Column "
             "`j` should end as an identity column with a zero in the objective row."),
            ("Read the new solution and sanity-check the objective",
             "Name the new basis, read the values and `z`, and check the change in `z` "
             "against the pivot: for a maximisation it should not have gone down. A "
             "negative right-hand entry means the leaving row was chosen badly, and "
             "choosing it well is the subject of “The Ratio Test”."),
        ],
        "worked": {
            "title": "One pivot on the plants tableau, every row operation shown",
            "intro": [
                "The entering column is `x₂` and the leaving row is row `2`. Watch the "
                "objective row: it is the fourth row of the arithmetic, not a summary "
                "written afterwards.",
            ],
            "lines": [
                "maximise  3x1 + 5x2      x1 <= 4,   2x2 <= 12,   3x1 + 2x2 <= 18",
                "standard form            x1 + s1 = 4",
                "                         2x2 + s2 = 12",
                "                         3x1 + 2x2 + s3 = 18",
                "objective row            z - 3x1 - 5x2 = 0",
                "",
                "              x1    x2    s1    s2    s3   |   rhs      basis {s1, s2, s3}",
                "   s1          1     0     1     0     0   |     4      s1 = 4",
                "   s2          0     2     0     1     0   |    12      s2 = 12",
                "   s3          3     2     0     0     1   |    18      s3 = 18",
                "   z          -3    -5     0     0     0   |     0      x = (0, 0),  z = 0",
                "",
                "pivot on row 2, column x2.   pivot entry a_22 = 2",
                "",
                "   R2' = R2 ÷ 2         [ 0    1    0   1/2   0  |   6 ]",
                "   R1' = R1 - 0·R2'     [ 1    0    1    0    0  |   4 ]   unchanged",
                "   R3' = R3 - 2·R2'     [ 3    0    0   -1    1  |   6 ]",
                "   z'  = z  + 5·R2'     [-3    0    0   5/2   0  |  30 ]",
                "",
                "              x1    x2    s1    s2    s3   |   rhs      basis {s1, x2, s3}",
                "   s1          1     0     1     0     0   |     4      s1 = 4",
                "   x2          0     1     0    1/2    0   |     6      x2 = 6",
                "   s3          3     0     0    -1     1   |     6      s3 = 6",
                "   z          -3     0     0    5/2    0   |    30      x = (0, 6),  z = 30",
            ],
            "after": [
                "Three things to notice. Row `1` did not change, because its entry in "
                "the pivot column was already zero &mdash; a row with a zero there is "
                "untouched by the pivot, which is worth knowing before “The Ratio "
                "Test” explains that such a row also imposes no limit. Column `x₂` "
                "is now an identity column with a zero in the objective row, which is "
                "the signature of a basic column. And `s₂` has left the basis: its "
                "column is `(0, 1/2, -1, 5/2)`, no longer an identity column.",
                "The objective row also carries a fact about `s₂`. Its entry is "
                "`5/2`, meaning that pushing `s₂` back up from zero &mdash; leaving "
                "plant B hours unused again &mdash; would cost `5/2` per hour. That "
                "number is a reduced cost, and “Reduced Costs and the Optimality Test” "
                "is about reading the whole row that way.",
                "For a faded rehearsal, pivot the same starting tableau on row `1`, "
                "column `x₁` instead. The supplied first move is that the pivot entry "
                "is `1`, so no division is needed and the fractions never appear. "
                "Carry out the other three row operations, read the new basis, point "
                "and `z`, and then say which column of the new tableau shows that the "
                "method is not finished. Check all four rows against the lab before "
                "opening the quiz.",
            ],
        },
        "quiz_title": "Reading and pivoting a tableau",
        "quiz": [
            {"q": "A tableau's rows are carrying `s₁, x₂, s₃` and its right-hand column is `4, 6, 6` with `30` in the bottom right. What is `x₁`?",
             "a": ["`4`, the first right-hand entry",
                   "`0`, because `x₁` is not a basic column",
                   "`30 ÷ 3`, from the objective value",
                   "It cannot be determined without another pivot"],
             "c": 1,
             "why": "The basis is `{s₁, x₂, s₃}`, so every other variable is held at "
                    "zero and `x₁ = 0`. `4` is the value of `s₁`, the row `x₁` does "
                    "not appear in; the objective value is an output of the reading, "
                    "not an equation to solve for a nonbasic variable."},
            {"q": "In a maximisation tableau, why is the objective row written with the negated coefficients?",
             "a": ["To make the arithmetic of the pivot come out positive",
                   "Because the row represents the equation `z - cᵀx = 0`",
                   "Because the objective is minimised internally",
                   "So that the bottom-right entry is never negative"],
             "c": 1,
             "why": "`maximise cᵀx` is rearranged to `z - cᵀx = 0` so that it is one "
                    "more equation of the same system, which is what lets a row "
                    "operation touch it. The sign is a consequence of that "
                    "rearrangement, and the bottom-right entry can perfectly well be "
                    "negative on a programme whose optimum is negative."},
            {"q": "A reader pivots correctly on all three constraint rows but keeps the objective value in a note at the side, recomputing it from `cᵀx` at the end. What goes wrong?",
             "a": ["Nothing: the final objective value is the same either way",
                   "The constraint rows come out wrong, because the pivot needs four rows",
                   "The objective row's entries are stale, so the stopping test and every reduced cost are read from the wrong numbers",
                   "The basis is no longer identifiable"],
             "c": 2,
             "why": "The final value of `cᵀx` at the final point really is the same, "
                    "which is exactly why this error survives: the constraint rows and "
                    "the reading of `x` are untouched. What is lost is the objective "
                    "row itself, and that row is where the entering column and the "
                    "decision to stop come from, so the method loses its steering "
                    "while still producing a plausible number."},
        ],
        "mistakes": [
            ("Keeping the objective row out of the row operations",
             "It is an equation, not a running total. Skipping it leaves the "
             "constraint rows correct and the objective row stale, which is the "
             "hardest kind of error to notice: the tableau reads consistently, the "
             "point is right, and the entering-column decision and the stopping test "
             "are both being made from numbers that belong to an earlier basis."),
            ("Reading a nonbasic variable's value off the right-hand column",
             "The right-hand entry of row `i` is the value of the variable that row is "
             "carrying, and of nothing else. A nonbasic variable is zero because it "
             "was set to zero; its column holds the rate at which the basic variables "
             "would have to move if it were raised, which is a different fact."),
            ("Pivoting on whatever entry looks convenient",
             "The row operations are legal on any non-zero entry, so nothing stops "
             "you, and the tableau stays a correct system. What can stop being true "
             "is feasibility: pivoting the plants tableau on row `3` in column `x₂` "
             "gives `s₂ = -6` and a bottom-right entry of `45`, which is larger than "
             "the real optimum. Check the right-hand column for a negative entry "
             "after every pivot until the ratio test makes it unnecessary."),
        ],
        "standard": ("Finish when you can build the first tableau, read its solution, and pivot once without looking anything up.",
                     "You should be able to write the objective row from a "
                     "maximisation, name the basic variable of every row, read the "
                     "point and `z` off the right-hand column, carry out a named pivot "
                     "with the objective row inside it, and say what a negative "
                     "right-hand entry afterwards means."),
        "note": "One choice has been made for you throughout: which row leaves. Pivot on the wrong row and the tableau is still a correct system describing a point outside the region, as the `s₂ = -6` above did. “The Ratio Test” is the rule that makes the choice, and it is a rule about staying inside the region rather than about the objective at all.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "the-ratio-test",
        "title": "The Ratio Test",
        "module": "One pivot",
        "one_line": "Compute every ratio with its reason, choose the leaving row, and show which basic variable goes negative under any other choice.",
        "summary": (
            "With the entering column fixed, the question is how far the entering "
            "variable can rise before some basic variable hits zero. Row `i` limits it "
            "only when its entry in the column is strictly positive, and then the "
            "limit is `b_i ÷ a_ij`. The smallest of those limits is the step, and the "
            "row that produced it leaves the basis. A row with a zero or negative entry "
            "imposes nothing, and a column with no positive entry at all is a column "
            "nothing limits."
        ),
        "key": [
            "column j is entering; how far can x_j rise?",
            "row i limits it only when a_ij > 0:      x_j ≤ b_i ÷ a_ij",
            "a_ij = 0  no limit - that basic variable does not move at all",
            "a_ij < 0  no limit - that basic variable grows as x_j does",
            "step  θ = min of b_i ÷ a_ij over a_ij > 0, and THAT row leaves",
            "no positive entry anywhere in the column ⟹ nothing limits it",
        ],
        "key_label": "Which rows bind, and the step the smallest one allows",
        "concepts_intro": (
            "One idea, and it is a feasibility argument rather than an optimisation "
            "one: the objective plays no part in this lesson at all."
        ),
        "concepts": [
            ("Raising the entering variable moves every basic variable",
             "Let `x_j` rise from zero to `θ` and hold the other nonbasic variables at "
             "zero. Row `i` says `x_{B(i)} = b_i - a_ij·θ`, so each basic variable "
             "moves at the rate given by its entry in the entering column. That single "
             "formula is the whole lesson: everything else is reading the sign of "
             "`a_ij`."),
            ("Only a strictly positive entry imposes a limit",
             "If `a_ij > 0` then `b_i - a_ij·θ` falls, and it reaches zero at "
             "`θ = b_i ÷ a_ij`. If `a_ij = 0` the basic variable does not move, and if "
             "`a_ij < 0` it rises. Neither of those two can ever go negative, so "
             "neither restricts `θ`, and including them in the minimum is not a "
             "harmless extra check &mdash; it produces a smaller-looking ratio that is "
             "meaningless."),
            ("The minimum is a step, and the row that gave it leaves",
             "Take `θ` to be the smallest of the eligible ratios. At that value the "
             "basic variable of the winning row is exactly zero, so it can be dropped "
             "from the basis and `x_j` put in its place &mdash; which is what pivoting "
             "on that row does. Go further and that variable is negative and the point "
             "has left the region."),
        ],
        "read_title": "How far the entering variable can go, and which row says so",
        "read_intro": "The one-line derivation, the two kinds of row that impose nothing, and what a column with no positive entry is telling you.",
        "body": [
            ("p", "The entering column is chosen by the objective and Reduced Costs "
                  "and the Optimality Test is where that choice comes from. Take it as "
                  "given here: column `j` is coming in, every other nonbasic variable "
                  "stays at zero, and `x_j` is going to rise from zero to some `θ ≥ 0`."),
            ("p", "Row `i` of the tableau reads `x_{B(i)} + a_ij·x_j = b_i` once the "
                  "other nonbasic terms are dropped, so `x_{B(i)} = b_i - a_ij·θ`. "
                  "Feasibility is the requirement that every one of those stays at or "
                  "above zero, and that is a set of inequalities in the single unknown "
                  "`θ`."),
            ("def", ("The ratio test",
                    "With entering column `j` and a feasible tableau, the "
                    "<strong>ratio</strong> of row `i` is `b_i ÷ a_ij`, defined only "
                    "for rows with `a_ij > 0`. The <strong>step</strong> is the "
                    "smallest such ratio, and the <strong>leaving</strong> variable is "
                    "the basic variable of a row achieving it. If no row has "
                    "`a_ij > 0`, the ratio test has no candidates and `x_j` is "
                    "unlimited.")),
            ("thm", ("The minimum ratio is exactly the largest feasible step",
                     "Let `θ* = min { b_i ÷ a_ij : a_ij > 0 }`. Then every basic "
                     "variable stays at or above zero for `0 ≤ θ ≤ θ*`, and some basic "
                     "variable is negative for every `θ > θ*`.")),
            ("proof", [
                "Split the rows by the sign of `a_ij`. If `a_ij ≤ 0` then "
                "`-a_ij·θ ≥ 0` for `θ ≥ 0`, so `b_i - a_ij·θ ≥ b_i ≥ 0` and that row "
                "never complains. If `a_ij > 0` then `b_i - a_ij·θ ≥ 0` is exactly "
                "`θ ≤ b_i ÷ a_ij`.",
                "So the feasible values of `θ` are the intersection of the intervals "
                "`[0, b_i ÷ a_ij]` over the positive entries, which is `[0, θ*]`. For "
                "`θ > θ*` the row achieving the minimum has `b_i - a_ij·θ &lt; 0`, so "
                "some basic variable is negative. Both halves follow from the sign "
                "split and nothing else.",
            ]),
            ("h3", "The two kinds of row that impose nothing"),
            ("p", "A zero entry means the pivot leaves that row alone &mdash; the "
                  "plants tableau’s row `1` was untouched by the pivot in “The Simplex Tableau” "
                  "for exactly this reason "
                  "&mdash; and its basic variable is unchanged however far `x_j` goes. "
                  "A negative entry means `b_i - a_ij·θ` grows with `θ`: raising the "
                  "entering variable makes that basic variable larger, and a variable "
                  "getting larger is not about to become negative."),
            ("p", "Neither row is excluded by convention or for tidiness. A negative "
                  "entry would produce a negative ratio, which looks like the smallest "
                  "of the set and is not a step at all; a zero entry would produce a "
                  "division by zero. Writing the ratio column with the ineligible rows "
                  "struck out <em>and the reason beside them</em> is the habit that "
                  "makes this reliable."),
            ("example", ("Every ratio on the plants tableau, with the reasons",
                         "The starting tableau has rows `s₁, s₂, s₃` with right-hand "
                         "column `4, 12, 18`, and column `x₂` is `(0, 2, 2)`. Row `1` "
                         "has a zero entry: no limit, `s₁` will not move. Row `2` has "
                         "`2`, so its ratio is `12 ÷ 2 = 6`. Row `3` has `2`, so its "
                         "ratio is `18 ÷ 2 = 9`.",
                         "The minimum is `6`, row `2` leaves, `x₂` enters at `6`, and "
                         "the new point is `(0, 6)`. Row `3`'s basic variable `s₃` "
                         "drops from `18` to `18 - 2(6) = 6`, and `s₁` stays at `4` "
                         "&mdash; both exactly as `b_i - a_ij·θ` predicts.")),
            ("h3", "What the other choice does"),
            ("p", "Pivot on row `3` instead, taking the ratio `9` rather than `6`. "
                  "Then `x₂ = 9`, and `s₂ = 12 - 2(9) = -6`. The tableau is still a "
                  "correct system and its bottom-right entry reads `45`, higher than "
                  "the true optimum of `36`, because it is the objective value at a "
                  "point outside the region: `(0, 9)` uses `18` of plant B's `12` "
                  "hours. A negative right-hand entry is the signature, and the "
                  "constraint that has been broken is the one whose slack went negative."),
            ("h3", "A column no row limits at all"),
            ("p", "On `maximise x₁ + x₂` subject to `x₁ - x₂ ≤ 4` and `x₁ - 2x₂ ≤ 6`, "
                  "one pivot brings `x₁` in and then the column of `x₂` has no "
                  "positive entry anywhere. The ratio test has no candidates, and the "
                  "honest reading is not that the tableau is broken: it is that `x₂` "
                  "can rise for ever with every basic variable staying non-negative, "
                  "so the objective is unbounded. Unbounded and Alternative Optima in "
                  "the Tableau turns that column into an explicit ray."),
            ("p", "The last case is a tie: two rows achieving the same minimum. Both "
                  "are legal choices and the step is the same either way, but whichever "
                  "row you do not take is left with a basic variable at zero. That is "
                  "degeneracy, it is the subject of Degeneracy, Cycling and "
                  "Bland&rsquo;s Rule, and it is the one place where the tie-break rule "
                  "turns out to matter."),
        ],
        "lab": ("simplex", {
            "mode": "ratio",
            "panel_title": "Override the leaving row and watch the point leave",
            "panel_intro": "The ratio column is printed with every excluded row and "
                           "its reason, and the point an overridden choice lands on is "
                           "drawn outside the region with the constraint it breaks named.",
        }),
        "steps_title": "Running the ratio test without a slip",
        "steps_intro": "Write the whole column down, including the rows that do not qualify. The ones you strike out are the ones that cause the error.",
        "steps": [
            ("Write the entering column beside the right-hand column",
             "Two columns of numbers, one row per constraint. Everything in this lesson "
             "is a comparison between those two, and the rest of the tableau is not "
             "needed."),
            ("Mark the sign of each entry before dividing anything",
             "Strictly positive: eligible. Zero: no limit, the basic variable does not "
             "move. Negative: no limit, the basic variable grows. Write the reason next "
             "to the struck-out rows rather than just omitting them."),
            ("Divide only the eligible rows and take the minimum",
             "`b_i ÷ a_ij` for each eligible row. The smallest is the step `θ`, and the "
             "row achieving it is the leaving row. On a tie, either row is legal &mdash; "
             "note that it happened, because the next basis will be degenerate."),
            ("Pivot on that row, then check the right-hand column",
             "Every entry of the new right-hand column should be at or above zero. A "
             "negative one means an ineligible row was included or the minimum was "
             "taken the wrong way round, and the point is now outside the region."),
            ("Read the new values and confirm them against `b_i - a_ij·θ`",
             "Each old basic variable should have moved by exactly its entry in the "
             "entering column times the step. That check is independent of the pivot "
             "arithmetic, so it catches a slip in either one."),
        ],
        "worked": {
            "title": "The ratio test on the plants tableau, and the override that fails",
            "intro": [
                "Column `x₂` is entering. Three rows, one ineligible, and two "
                "candidates whose ratios differ by three.",
            ],
            "lines": [
                "              x1    x2    s1    s2    s3   |   rhs      basis {s1, s2, s3}",
                "   s1          1     0     1     0     0   |     4",
                "   s2          0     2     0     1     0   |    12",
                "   s3          3     2     0     0     1   |    18",
                "   z          -3    -5     0     0     0   |     0",
                "",
                "entering column x2",
                "   row   a_i2    b_i    ratio        eligible?",
                "    1      0       4      -          no: zero entry, s1 does not move",
                "    2      2      12    12/2 = 6     yes",
                "    3      2      18    18/2 = 9     yes",
                "",
                "   step  θ = min(6, 9) = 6      row 2 leaves,  s2 out,  x2 in",
                "",
                "   check   s1 = 4  - 0(6) = 4        s3 = 18 - 2(6) = 6      x2 = 6",
                "   point (0, 6),  every value at or above zero,  z = 30",
                "",
                "the override:  leave from row 3 instead,  taking the ratio 9",
                "",
                "              x1    x2    s1    s2    s3   |   rhs      basis {s1, s2, x2}",
                "   s1          1     0     1     0     0   |     4",
                "   s2         -3     0     0     1    -1   |    -6      s2 = -6",
                "   x2         3/2    1     0     0    1/2  |     9      x2 = 9",
                "   z          9/2    0     0     0    5/2  |    45      z reads 45",
                "",
                "   point (0, 9):   2x2 = 18 > 12,  plant B hours broken by 6",
                "   the true optimum of this programme is 36",
            ],
            "after": [
                "The tableau after the override is not wrong arithmetic. Every row "
                "operation was legal and the system it represents is equivalent to the "
                "original one. What it has stopped doing is describing a point of the "
                "feasible region, and the `-6` in the right-hand column is the "
                "announcement. The `45` is the objective evaluated at `(0, 9)`, which "
                "is a real number about an unreal plan.",
                "Note which constraint broke. `s₂` is the slack of plant B hours, so a "
                "negative `s₂` is that row and no other, by exactly `6` hours. This is "
                "why a slack is worth naming when the programme is written: the "
                "violation reads itself.",
                "For a faded rehearsal, take the tableau at `(0, 6)` from “The Simplex "
                "Tableau” and run the ratio test on column `x₁`, whose entries are "
                "`(1, 0, 3)` against a right-hand column of `4, 6, 6`. The supplied "
                "first move is that row `2` is the ineligible one this time. Compute "
                "both ratios, name the leaving variable, predict the new point from "
                "`b_i - a_ij·θ` before pivoting, and then pivot and compare.",
            ],
        },
        "quiz_title": "Ratios, limits and the rows that do not bind",
        "quiz": [
            {"q": "An entering column has entries `(-3, 4, 0)` against a right-hand column of `(6, 8, 5)`. What is the step?",
             "a": ["`-2`, from the first row", "`0`, from the third row", "`2`, from the second row", "`5/4`"],
             "c": 2,
             "why": "Only the second row has a strictly positive entry, so it is the "
                    "only candidate and the step is `8 ÷ 4 = 2`. `-2` divides by a "
                    "negative entry, `0` divides by zero, and `5/4` pairs the third "
                    "row's right-hand side with the second row's entry."},
            {"q": "Why is a row with a negative entry in the entering column excluded from the ratio test?",
             "a": ["Because its ratio would be negative, and negative steps are not allowed",
                   "Because its basic variable increases as the entering variable rises, so it can never reach zero",
                   "Because a negative entry means the tableau is infeasible",
                   "Because the pivot would divide by a negative number"],
             "c": 1,
             "why": "Row `i` holds `x_{B(i)} = b_i - a_ij·θ`; with `a_ij &lt; 0` that "
                    "value rises with `θ` and stays non-negative for ever, so the row "
                    "imposes no limit. The negative ratio is a symptom of that, not "
                    "the reason; a negative entry says nothing about feasibility; and "
                    "dividing by a negative number is perfectly ordinary arithmetic."},
            {"q": "A reader takes the minimum over all three rows of the column `(0, 2, 2)` with right-hand side `(4, 12, 18)`, treating the first row's ratio as `4 ÷ 0` and discarding it, but keeps the rest. What happens?",
             "a": ["Nothing: the answer is the same, because the excluded row was going to lose anyway",
                   "The step comes out as `4`, from the first row",
                   "The step is right here, but the same habit gives a leaving row that puts the point outside the region whenever a negative entry is present",
                   "The pivot fails because one ratio is undefined"],
             "c": 2,
             "why": "On this particular column the ineligible row is a zero entry, so "
                    "discarding it is what the rule says anyway and the answer is "
                    "unaffected. That is precisely what makes the habit dangerous: it "
                    "passes here and fails on the next column, where a negative entry "
                    "yields a negative ratio that wins the minimum and hands back a "
                    "leaving row whose pivot drives a basic variable below zero."},
        ],
        "mistakes": [
            ("Taking the minimum over every row instead of the eligible ones",
             "A negative entry produces a negative ratio, which is smaller than any "
             "genuine candidate and wins the minimum. The pivot that follows is legal "
             "arithmetic on an infeasible point: the right-hand column comes back with "
             "a negative entry and the objective value it reports is larger than the "
             "true optimum, which is the single most convincing wrong answer this "
             "course can produce."),
            ("Reading a zero entry as a ratio of zero",
             "`b_i ÷ 0` is not `0` and it is not a very small number; the row simply "
             "does not restrict the step, because its basic variable does not move. "
             "Treating it as a zero ratio makes it win every tie and pivots on an entry "
             "that cannot be pivoted on at all."),
            ("Reading a column with no positive entry as a broken tableau",
             "It is a diagnosis, not a fault. Every basic variable stays non-negative "
             "however far the entering variable rises, so the objective has no maximum "
             "and the column itself is the direction along which it escapes. Unbounded "
             "and Alternative Optima in the Tableau produces the ray; starting the "
             "problem again with a different entering column produces nothing."),
        ],
        "standard": ("Finish when you strike out a row and give the reason in the same breath.",
                     "You should be able to write the ratio column with the ineligible "
                     "rows marked and explained, take the step, name the leaving "
                     "variable, predict every new basic value from `b_i - a_ij·θ`, and "
                     "say what a column with no positive entry means."),
        "note": "Both choices in a pivot are now accounted for, but only one of them has a reason yet: the leaving row keeps the point inside the region, and the entering column has so far been handed to you. “Reduced Costs and the Optimality Test” is where that choice comes from, and it is also where the method learns how to stop &mdash; the two turn out to be the same reading of the same row.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "reduced-costs-and-the-optimality-test",
        "title": "Reduced Costs and the Optimality Test",
        "module": "One pivot",
        "one_line": "Read the reduced costs off a tableau, choose an entering column, and state the stopping condition and what licences it.",
        "summary": (
            "A nonbasic variable's entry in the objective row is a rate: how much the "
            "objective changes per unit of that variable, with every basic variable "
            "adjusting to keep the equations true. When no rate improves the objective, "
            "the corner has no improving edge and is globally optimal. The improvement "
            "a column actually delivers is that rate times the step the ratio test "
            "allows, which is why the steepest column is routinely not the best one."
        ),
        "key": [
            "objective-row entry     z_j = c_Bᵀ B⁻¹ A_j - c_j        the rate is -z_j",
            "improving (maximise)    z_j < 0: one more unit of x_j raises z by -z_j",
            "Dantzig     enter the most negative z_j, lowest column index on a tie",
            "Bland       enter the lowest-index column with z_j < 0",
            "Δz = rate × step        the step comes from the ratio test, not the rate",
            "stop        no z_j < 0 ⟹ this corner is optimal over the whole region",
            "minimise    negate the objective; every rule then reads the same way",
        ],
        "key_label": "The objective row as a row of rates, and the test it carries",
        "concepts_intro": (
            "The hard idea here is a distinction, not a formula: a rate per unit and a "
            "total improvement are different quantities, and the rule most textbooks "
            "teach optimises the first one."
        ),
        "concepts": [
            ("The objective row is a row of rates",
             "For a nonbasic column `j` the objective-row entry `z_j` answers: if `x_j` "
             "rises by one unit and every basic variable adjusts to keep the equations "
             "true, how does `z` change? It changes by `-z_j`. So a negative entry is "
             "an improving direction for a maximisation, its size is the rate, and the "
             "whole row is a price list on the columns currently sitting at zero."),
            ("No improving rate means optimal, everywhere",
             "If every `z_j ≥ 0` then no edge leaving this corner raises the "
             "objective, and “Convexity, and Why a Local Optimum Is Global” upgrades "
             "that from a statement about the corner to a statement about the region. "
             "This is the licence to stop, and it is the reason the method can finish "
             "without ever seeing most of the corners."),
            ("Improvement is rate times step",
             "A rate of `9` on a column the ratio test stops after `4` units moves the "
             "objective by `36`. A rate of `3` on a column that can run to `20` moves "
             "it by `60`. Both figures come from one tableau of one real programme, and "
             "they are why &ldquo;take the most negative entry&rdquo; is a heuristic "
             "about rates rather than a rule about improvement."),
        ],
        "read_title": "What the objective row means, which column to take, and when to stop",
        "read_intro": "The rate interpretation, the rule almost everyone uses and what it costs, the stopping test, and the one adjustment a minimisation needs.",
        "body": [
            ("def", ("Reduced cost",
                    "In a tableau at basis `B`, the <strong>reduced cost</strong> of "
                    "column `j` is its objective-row entry `z_j = c_Bᵀ B⁻¹ A_j - c_j`. "
                    "Every basic column has `z_j = 0`. For a maximisation, column `j` "
                    "is <strong>improving</strong> when `z_j &lt; 0`, and the "
                    "<strong>rate</strong> at which `z` rises per unit of `x_j` is "
                    "`-z_j`.")),
            ("p", "The formula is worth seeing even though you never need it to run the "
                  "method, because it says where the number comes from: `c_j` is what "
                  "one unit of `x_j` earns directly, and `c_Bᵀ B⁻¹ A_j` is what the "
                  "basic variables have to give up to make room for it. The reduced "
                  "cost is the difference, which is why it can be negative for a "
                  "profitable column. “The Tableau as a Matrix Product” is where that "
                  "expression is computed rather than quoted."),
            ("p", "In the initial tableau of a `≤`-only programme the basis is the "
                  "slacks, `c_B = 0`, and the reduced costs are just `-c_j`. That is "
                  "the familiar row of negated objective coefficients from The Simplex "
                  "Tableau, and it is a special case rather than the definition."),
            ("h3", "Choosing the entering column"),
            ("p", "Any improving column may enter. The rules in common use are: "
                  "<strong>Dantzig&rsquo;s rule</strong>, take the most negative "
                  "reduced cost, breaking ties by lowest column index; "
                  "<strong>Bland&rsquo;s rule</strong>, take the lowest-index improving "
                  "column; and <strong>greatest improvement</strong>, compute the step "
                  "for every improving column and take the largest rate times step. "
                  "Each terminates at the same optimal value when it terminates at all; "
                  "they differ in the path and in how many pivots it takes."),
            ("example", ("The steepest column is the wrong one",
                         "Take `maximise 5x₁ + 9x₂ + 3x₃` subject to "
                         "`3x₁ + 2x₂ ≤ 20`, `x₁ + 3x₂ ≤ 12` and "
                         "`4x₁ + 4x₂ + x₃ ≤ 20`. At the origin the three rates are "
                         "`5`, `9` and `3`, and the ratio test allows steps of `5`, `4` "
                         "and `20` respectively. So the products are `25`, `36` and "
                         "`60`.",
                         "`x₂` is the steepest column and moves `z` by `36`. `x₃` has "
                         "a third of that rate and moves it by `60`, which is the "
                         "entire optimum of the programme. Dantzig&rsquo;s rule takes "
                         "`x₂` and needs three pivots; greatest improvement takes `x₃` "
                         "and needs one.")),
            ("math", [
                "at the origin of  max 5x1 + 9x2 + 3x3",
                "",
                "   column   reduced cost   rate   step   rate × step",
                "     x1          -5          5      5         25",
                "     x2          -9          9      4         36      Dantzig takes this",
                "     x3          -3          3     20         60      the whole optimum",
                "",
                "   pivots to reach z* = 60:   Dantzig 3    Bland 4",
                "                              greatest improvement 1    largest index 1",
            ]),
            ("p", "Dantzig&rsquo;s rule survives anyway, for a reason worth being "
                  "honest about: computing the step for every improving column to find "
                  "the greatest improvement costs a ratio test per column per pivot, "
                  "and on a real problem that is more arithmetic than the extra pivots "
                  "it saves. The rule is a cheap approximation to the thing you want, "
                  "and this page exists so that you know which is which."),
            ("h3", "Stopping"),
            ("thm", ("The optimality test",
                     "If every reduced cost in a feasible tableau satisfies `z_j ≥ 0`, "
                     "the basic feasible solution it reads is an optimal solution of "
                     "the programme. The test looks only at the current tableau, and "
                     "its conclusion is about every feasible point.")),
            ("p", "The two halves of that sentence are worth separating. That no edge "
                  "leaving this corner improves the objective is arithmetic on one row. "
                  "That therefore no point of the region improves it is the convexity "
                  "result from “Convexity, and Why a Local Optimum Is Global”. Quote the "
                  "second half when you stop; a tableau alone only ever tells you about "
                  "its own corner."),
            ("h3", "A minimisation, and the one adjustment it needs"),
            ("p", "`minimise cᵀx` is `maximise -cᵀx` with the answer negated at the "
                  "end, and that is exactly what the lab does. Take `minimise "
                  "2x₁ - 3x₂` subject to `x₁ + x₂ ≤ 8` and `2x₁ + x₂ ≤ 10`. The "
                  "internal objective is `-2x₁ + 3x₂`, so the objective row starts at "
                  "`(2, -3)` &mdash; the original coefficients &mdash; and the "
                  "stopping rule is still &ldquo;no negative entry&rdquo;. One pivot "
                  "brings `x₂` in at `8`, the tableau reads `24`, and the answer to "
                  "the question asked is `-24`."),
            ("p", "So nothing about the test flips. What flips is the sign of the "
                  "number you report, and the discipline is to write down which "
                  "convention you are in before the first pivot rather than to "
                  "reconstruct it from the answer. A minimisation whose optimum is "
                  "negative is the case where guessing goes wrong."),
            ("p", "One last reading of the row: a zero reduced cost on a column that "
                  "is <em>not</em> basic satisfies the stopping test and still means "
                  "something. It says a pivot on that column would move to a different "
                  "corner at the same objective value, so the optimum is not unique. "
                  "“Unbounded and Alternative Optima in the Tableau” is where that "
                  "signature is read."),
        ],
        "lab": ("simplex", {
            "mode": "auto",
            "preset": "rules",
            "panel_title": "Switch the entering rule and count the pivots",
            "panel_intro": "Every candidate column carries its own rate, step and "
                           "product at every pivot, and `rate × step` is compared with "
                           "the change in `z` as exact fractions rather than to six "
                           "decimal places.",
        }),
        "steps_title": "Choosing a column, and deciding whether to",
        "steps_intro": "Read the whole objective row before choosing anything. The decision to stop is made from the same numbers as the decision where to go.",
        "steps": [
            ("Read the objective row for nonbasic columns only",
             "Basic columns always hold zero there and carry no information. What is "
             "left is one number per nonbasic column, and each is a rate per unit of "
             "that variable."),
            ("If no entry is negative, stop and say why",
             "No improving edge leaves this corner, and a linear objective on a convex "
             "region has no local optimum that is not global. Report the point, the "
             "objective value, and that second sentence &mdash; the tableau on its own "
             "does not licence the claim."),
            ("Otherwise choose a column, and know which rule you used",
             "Dantzig takes the most negative entry; Bland takes the lowest index; "
             "greatest improvement runs the ratio test on every candidate first. Name "
             "the rule, because the pivot count and the path depend on it and the "
             "optimum does not."),
            ("Run the ratio test on the column you chose",
             "The rate told you the direction; only the step tells you how far. This is "
             "where a steep column with a short step gets found out."),
            ("Check `rate × step` against the change in the objective value",
             "They are equal, exactly, at every pivot. It is a free check on both the "
             "ratio test and the pivot arithmetic, and it is the arithmetic that makes "
             "the rate-versus-improvement distinction concrete rather than a slogan."),
        ],
        "worked": {
            "title": "Three products, where the steepest column loses to a flatter one",
            "intro": [
                "One programme, one tableau, four entering rules. The rates and the "
                "steps are both read from the starting tableau, so the comparison needs "
                "no pivoting at all.",
            ],
            "lines": [
                "maximise  5x1 + 9x2 + 3x3",
                "   3x1 + 2x2        <= 20     assembly",
                "    x1 + 3x2        <= 12     finishing",
                "   4x1 + 4x2 +  x3  <= 20     packing",
                "",
                "              x1    x2    x3    s1    s2    s3   |   rhs",
                "   s1          3     2     0     1     0     0   |    20",
                "   s2          1     3     0     0     1     0   |    12",
                "   s3          4     4     1     0     0     1   |    20",
                "   z          -5    -9    -3     0     0     0   |     0",
                "",
                "   column   z_j    rate   ratios eligible        step   rate × step",
                "     x1     -5      5     20/3, 12/1, 20/4        5         25",
                "     x2     -9      9     20/2, 12/3, 20/4        4         36",
                "     x3     -3      3     row 3 only: 20/1       20         60",
                "",
                "   Dantzig takes x2:  Δz = 9 × 4  = 36,  then two more pivots to 60",
                "   greatest improvement takes x3:  Δz = 3 × 20 = 60,  and it is done",
                "",
                "   pivot counts on this one programme",
                "     Dantzig                6 -> 3 pivots        z* = 60",
                "     Bland                       4 pivots        z* = 60",
                "     greatest improvement        1 pivot         z* = 60",
                "     largest index               1 pivot         z* = 60",
            ],
            "after": [
                "Every rule reached `60`. That is not luck and it is not a property of "
                "this programme: the optimum is a property of the feasible region and "
                "the objective, and an entering rule chooses a route to it. What the "
                "rule buys or costs is pivots, and here the spread is one against four.",
                "The reason `x₃` wins is visible in the ratio column. It appears in "
                "only one constraint, so only one row limits it, and that row lets it "
                "run to `20`. `x₂` earns nearly three times as much per unit and is cut "
                "off after `4` by the finishing row. A rate with no room to move is "
                "worth nothing, which is the sentence the whole lesson is built on.",
                "For a faded rehearsal, take `minimise 4x₁ - 8x₂ - 6x₃` subject to "
                "`3x₁ + 2x₂ + x₃ ≤ 13`, `4x₁ + 2x₃ ≤ 17` and `2x₁ + 4x₂ ≤ 21`. The "
                "supplied first move is that the objective row starts as `(4, -8, -6)` "
                "&mdash; the original coefficients, because the solver negated the "
                "objective on the way in &mdash; so `x₁` is not a candidate at all. "
                "Work out the rate, the step and the product for `x₂` and `x₃`, say "
                "which column Dantzig takes and which greatest improvement takes, and "
                "then check the pivot counts and the optimum of `-69` in the lab.",
            ],
        },
        "quiz_title": "Rates, improvements and the stopping test",
        "quiz": [
            {"q": "In a maximisation tableau the nonbasic columns have objective-row entries `-2`, `-7` and `0`. Which statement is correct?",
             "a": ["The tableau is optimal, because one entry is zero",
                   "Two columns improve the objective, and the `-7` column has the larger rate per unit",
                   "Two columns improve the objective, and the `-7` column gives the larger improvement",
                   "The `0` column is basic, so it should be ignored"],
             "c": 1,
             "why": "A negative entry is an improving column and its size is the rate "
                    "per unit, so `-7` is the steeper of the two. Which one gives the "
                    "larger <em>improvement</em> depends on the steps, which are not "
                    "shown. The tableau is not optimal while any entry is negative, and "
                    "a zero entry on a nonbasic column is a signal about alternative "
                    "optima rather than something to ignore."},
            {"q": "Two entering rules are run on the same programme and one takes three pivots while the other takes one. What differs in the answers?",
             "a": ["Nothing: both reach the same optimal objective value",
                   "The optimal objective values differ, and the rule taking fewer pivots finds the better one",
                   "The three-pivot run is more accurate, because it examined more corners",
                   "The optimal point differs, but the objective value is the same"],
             "c": 0,
             "why": "The optimum is fixed by the region and the objective; a rule "
                    "chooses the path to it. Both runs end at an optimal basis with the "
                    "same objective value. The optimal <em>point</em> can differ only "
                    "when the optimum is not unique, which is a separate signature, and "
                    "no arithmetic here is approximate, so “accuracy” is not a "
                    "difference between them."},
            {"q": "Column `x₂` has rate `9` and the ratio test allows a step of `4`. Column `x₃` has rate `3` and a step of `20`. Which column does Dantzig's rule take, and which moves the objective further?",
             "a": ["`x₂`, and `x₂` moves it further",
                   "`x₂`, but `x₃` moves it further",
                   "`x₃`, and `x₃` moves it further",
                   "`x₃`, but `x₂` moves it further"],
             "c": 1,
             "why": "Dantzig looks only at the reduced cost, so it takes the steeper "
                    "column `x₂`. The improvement is rate times step: `9 × 4 = 36` "
                    "against `3 × 20 = 60`, so `x₃` moves the objective further. That "
                    "gap is the whole reason the rule is a heuristic."},
            {"q": "A programme is `minimise 2x₁ - 3x₂`, and the lab reports a final tableau whose bottom-right entry is `24`. What is the optimum?",
             "a": ["`24`", "`-24`", "`24`, and the sign convention only affects the objective row",
                   "It cannot be read without the values of `x₁` and `x₂`"],
             "c": 1,
             "why": "The solver maximises `-2x₁ + 3x₂` and reports `24` for that "
                    "internal problem, so the minimum of the original objective is "
                    "`-24`. The values of `x` do confirm it &mdash; `x₂ = 8` gives "
                    "`-3(8) = -24` &mdash; but the negation alone settles it, and the "
                    "convention affects the reported value and not only the row."},
        ],
        "mistakes": [
            ("Believing the most negative reduced cost gives the biggest improvement",
             "It gives the biggest rate. The improvement is rate times the step the "
             "ratio test allows, and a steep column pinned by a tight row routinely "
             "moves the objective less than a flat column with room to run: `9 × 4` "
             "against `3 × 20` on one tableau of one small programme. Dantzig&rsquo;s "
             "rule is worth using because it is cheap, not because it is best."),
            ("Expecting the stopping test to flip on a minimisation",
             "The objective is negated on the way in, so the objective row of "
             "`minimise 2x₁ - 3x₂` starts as `(2, -3)` and the test is still &ldquo;no "
             "negative entry&rdquo;. What changes is the sign of the number you report: "
             "the internal `24` is an optimum of `-24`. Reconstructing the convention "
             "from the answer is where this goes wrong, and it goes wrong hardest when "
             "the true optimum is negative."),
            ("Reporting optimality as a property of the tableau",
             "A tableau with no negative reduced cost says that no edge leaving this "
             "corner improves the objective &mdash; a fact about one corner. The claim "
             "that no point of the region improves it needs the convexity result, and "
             "saying so is not pedantry: it is the difference between a proof and a "
             "search that happened to stop."),
        ],
        "standard": ("Finish when a reduced cost reads as a rate per unit and never as an amount of improvement.",
                     "You should be able to identify the improving columns in a "
                     "tableau, apply any of the three entering rules and say which you "
                     "used, verify `rate × step` against the change in `z`, state the "
                     "stopping test with the theorem that licences it, and report a "
                     "minimisation with the right sign."),
        "note": "Everything so far has begun at the origin, where the slacks are already an identity and the first basis is free. A programme with a `≥` row or an `=` row has no such gift: there is no obvious basis to start from and the origin is usually not even feasible. “Artificial Variables and Two-Phase Simplex” manufactures a start, and the same machinery turns out to prove infeasibility when no start exists.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "artificial-variables-and-two-phase-simplex",
        "title": "Artificial Variables and Two-Phase Simplex",
        "module": "Awkward tableaux",
        "one_line": "Set up and run a first phase on a mixed-constraint programme, and either hand a basis to the second phase or certify infeasibility.",
        "summary": (
            "A `≥` row's surplus column is `-1`, and an `=` row has no extra column at "
            "all, so neither offers the identity column a starting basis needs. An "
            "artificial variable is added to supply one, and minimising the sum of the "
            "artificials is itself a linear programme. Its optimum is either zero, "
            "which hands over a genuine basic feasible solution, or positive, which "
            "proves the original programme has no feasible point and carries the proof "
            "as a number."
        ),
        "key": [
            "≤ row     a·x + s = b            s ≥ 0, and s is an identity column",
            "≥ row     a·x - e + A = b        e ≥ 0 surplus; its column is -1",
            "= row     a·x + A = b            the artificial is the only identity column",
            "phase I   minimise the sum of the artificials, starting from them",
            "value 0   ⟹ a genuine basic feasible solution: drop them, run phase II",
            "value > 0 ⟹ INFEASIBLE, and that value is the certificate",
            "an artificial left basic AT ZERO is degeneracy, not failure",
        ],
        "key_label": "Where the identity column comes from, and what the first phase decides",
        "concepts_intro": (
            "One hard idea: a phase of the method whose objective is not the "
            "programme&rsquo;s objective, and whose <em>answer</em> is a yes-or-no "
            "about feasibility."
        ),
        "concepts": [
            ("A surplus column is not an identity column",
             "Turning `x₁ + x₂ ≥ 4` into an equation gives `x₁ + x₂ - e₁ = 4`, and the "
             "column of `e₁` is `-1`. Starting from that basis would read `e₁ = -4`, "
             "which is not feasible. An `=` row is worse: it contributes no new column "
             "at all. Either way there is nothing to start from, which is a different "
             "problem from the programme being hard."),
            ("An artificial variable measures nothing",
             "A slack measures something real &mdash; the unused part of a resource "
             "&mdash; and may well be positive at the optimum. An artificial is put "
             "into a row purely to occupy an identity column, it corresponds to nothing "
             "in the situation, and any positive value it still has at the end of the "
             "first phase means the equations were satisfied only by cheating."),
            ("The first phase answers a question, the second solves the programme",
             "Minimise the sum of the artificials from the all-artificial basis. Reach "
             "zero and every artificial is out or at zero, so what is left is a genuine "
             "basic feasible solution of the original constraints and the second phase "
             "starts from it with the real objective. Stop above zero and the minimum "
             "amount of cheating required is positive, which is a proof that no "
             "feasible point exists."),
        ],
        "read_title": "Manufacturing a start, and what it means when you cannot",
        "read_intro": "Where the artificial columns go, what the first phase minimises, the handover, and the certificate a positive optimum hands you.",
        "body": [
            ("p", "Everything so far started at the origin because every row was a `≤` "
                  "row with a slack, and the slacks formed an identity. Standard Form, "
                  "Slack and Surplus wrote the other two kinds of row, and neither "
                  "helps: a `≥` row's surplus enters with coefficient `-1`, and an `=` "
                  "row adds no column. So the tableau has no starting basis, and one "
                  "has to be built."),
            ("def", ("Artificial variable",
                    "An <strong>artificial variable</strong> is a non-negative "
                    "variable added to one row with coefficient `+1`, for the sole "
                    "purpose of giving that row an identity column. It has no meaning "
                    "in the situation being modelled, and a solution of the original "
                    "programme is exactly a solution in which every artificial is "
                    "zero.")),
            ("p", "Take `minimise 2x₁ + 3x₂` subject to `x₁ + x₂ ≥ 4` (demand), "
                  "`2x₁ + x₂ ≥ 5` (a quality floor) and `x₁ ≤ 3` (capacity). The two "
                  "`≥` rows get a surplus and an artificial each; the `≤` row gets an "
                  "ordinary slack. The columns, in order, are "
                  "`x₁, x₂, e₁, A₁, e₂, A₂, s₃`."),
            ("math", [
                "   x1 +  x2 - e1 + A1               = 4      demand",
                "  2x1 +  x2           - e2 + A2     = 5      quality floor",
                "   x1                           + s3 = 3     capacity",
                "",
                "  the identity columns are  A1,  A2,  s3   - two artificials and a slack",
                "  the starting reading is   A1 = 4,  A2 = 5,  s3 = 3,  x = (0, 0)",
                "",
                "  phase I objective:   minimise  A1 + A2",
            ]),
            ("p", "That starting reading is feasible for the enlarged system and "
                  "meaningless for the original one: it satisfies the demand row by "
                  "putting `4` units of nothing into it. The first phase&rsquo;s job is "
                  "to drive that quantity to zero if it can."),
            ("def", ("Phase I and Phase II",
                    "<strong>Phase I</strong> is the linear programme `minimise` the "
                    "sum of the artificial variables, over the same constraints, "
                    "started from the basis of identity columns. Its optimum is "
                    "non-negative. If it is zero, drop the artificial columns and run "
                    "<strong>Phase II</strong>: the original objective, started from "
                    "the basis Phase I finished on. If it is positive, the original "
                    "programme is infeasible.")),
            ("example", ("The first phase reaches zero and hands over a basis",
                         "On the programme above, Phase I takes two pivots &mdash; "
                         "`x₁` in and `A₂` out, then `x₂` in and `A₁` out &mdash; and "
                         "its optimum is `0` with neither artificial left in the basis. "
                         "The basis it hands over is a genuine corner of the original "
                         "region.",
                         "Phase II then needs one pivot and finishes at `x = (3, 1)` "
                         "with `2(3) + 3(1) = 9`. Three pivots in total, and the only "
                         "unusual thing about them is that the first two were "
                         "optimising a different objective.")),
            ("h3", "When the first phase cannot reach zero"),
            ("p", "Take the empty region that “Systems of Inequalities and Linear "
                  "Programming” drew as a blank picture: `x₁ + x₂ ≤ 1` together with "
                  "`x₁ + x₂ ≥ 4`. Phase I stops at `3`. That is not a failure to "
                  "converge and not a numerical artefact; it is the smallest total "
                  "amount of artificial quantity that makes the two rows "
                  "simultaneously satisfiable, and it is positive."),
            ("thm", ("A positive first-phase optimum is a proof of infeasibility",
                     "If the minimum of the sum of the artificials is `v > 0`, the "
                     "original constraints have no non-negative solution. The value `v` "
                     "is exact, and the multipliers the final tableau carries turn it "
                     "into a contradiction that can be checked row by row: a "
                     "combination `y` of the rows with `yᵀA ≤ 0` and `yᵀb > 0`.")),
            ("p", "On the empty region the multipliers are `y = (-1, 1)`. Combining the "
                  "rows that way gives `0 ≥ 3`: the coefficient of every variable "
                  "cancels and the right-hand sides do not. That is a complete "
                  "argument, it fits on one line, and it is what a blank picture was "
                  "standing in for. “Duality and Sensitivity Analysis” is where those "
                  "multipliers get their name."),
            ("h3", "An artificial left basic at zero"),
            ("p", "Phase I can finish at zero with an artificial still in the basis, at "
                  "value zero. On `x₁ + x₂ = 4` together with `2x₁ + 2x₂ = 8` &mdash; "
                  "the same row doubled &mdash; and `x₂ ≤ 3`, the first phase reaches "
                  "`0` in one pivot and leaves the second artificial basic at zero, "
                  "because no real column can replace it: that row is redundant. This "
                  "is a degenerate basic feasible solution, not a failure. Phase II "
                  "runs from it and reaches `7`, and the artificial is held at zero or "
                  "driven out on the way."),
            ("p", "The one-phase alternative is worth naming and not running. "
                  "<strong>Big-M</strong> keeps the artificials in the real objective "
                  "with a large penalty coefficient `M`, so that a positive artificial "
                  "is never optimal unless it has to be. It reaches the same answers "
                  "and it needs `M` to be chosen large enough relative to data you have "
                  "not solved yet, which is the kind of decision this path avoids. Two "
                  "phases need no such constant."),
        ],
        "lab": ("simplex", {
            "mode": "phase1",
            "panel_title": "Watch the artificials leave, or fail to",
            "panel_intro": "The first phase runs pivot by pivot with the artificial "
                           "columns marked, and an infeasible preset ends on a positive "
                           "optimum whose multipliers are checked row by row rather "
                           "than asserted.",
        }),
        "steps_title": "Running two phases on a mixed-constraint programme",
        "steps_intro": "The bookkeeping is where this goes wrong, not the pivoting. Write the enlarged system out in full before starting.",
        "steps": [
            ("Convert every row and note what each new column is for",
             "A slack for a `≤` row, a surplus for a `≥` row, and an artificial "
             "wherever the row has no identity column of its own. Label them: a surplus "
             "and an artificial in the same row are two different variables doing two "
             "different jobs."),
            ("Start from the identity columns and minimise the artificials",
             "The first basis is whichever columns are `+1` in one row and zero "
             "elsewhere &mdash; some slacks, and every artificial. The first phase "
             "objective is the sum of the artificials and nothing else; the real "
             "objective is not in the tableau yet."),
            ("Read the first-phase optimum and decide",
             "Zero means feasible: drop the artificial columns and go on. Positive "
             "means infeasible, and the value is the answer rather than a symptom "
             "&mdash; report it, and read off the multipliers if you want the "
             "contradiction in one line."),
            ("Hand the basis over, not the point",
             "Phase II starts from the basis Phase I finished on, with the original "
             "objective written into a fresh objective row. Recompute that row from the "
             "current basis; the first phase&rsquo;s objective row is about a different "
             "objective and carrying it over is the commonest slip here."),
            ("Check no artificial is positive at the end of either phase",
             "An artificial at zero is degeneracy and is fine. One above zero after "
             "Phase I means the programme is infeasible; one above zero after Phase II "
             "means the handover was done wrong, because the second phase has no reason "
             "to raise it."),
        ],
        "worked": {
            "title": "Two requirements and a cap: the first phase hands over a basis",
            "intro": [
                "A minimisation with two `≥` rows, so two artificials. The first phase "
                "is a different programme on the same constraints, and its optimum is "
                "the only thing that decides whether the second phase happens at all.",
            ],
            "lines": [
                "minimise  2x1 + 3x2",
                "   x1 + x2 >= 4      demand",
                "  2x1 + x2 >= 5      quality floor",
                "   x1      <= 3      capacity",
                "",
                "enlarged system",
                "   x1 +  x2 -  e1 + A1                  = 4",
                "  2x1 +  x2            -  e2 + A2       = 5",
                "   x1                             +  s3 = 3",
                "",
                "  columns   x1   x2   e1   A1   e2   A2   s3",
                "  identity            -    A1   -    A2   s3",
                "  start     A1 = 4,  A2 = 5,  s3 = 3,   x = (0, 0)",
                "",
                "PHASE I    minimise A1 + A2      starting value 4 + 5 = 9",
                "   pivot 1   x1 in,  A2 out      sum of artificials  ->  3/2",
                "   pivot 2   x2 in,  A1 out      sum of artificials  ->  0",
                "",
                "   phase I optimum 0   ⟹  feasible.  Neither artificial is still basic.",
                "",
                "PHASE II   minimise 2x1 + 3x2 from that basis",
                "   pivot 1   one pivot to optimality",
                "   x = (3, 1),   2(3) + 3(1) = 9",
                "",
                "the same machinery on an EMPTY region:   x1 + x2 <= 1,  x1 + x2 >= 4",
                "   phase I optimum 3  >  0   ⟹  infeasible",
                "   multipliers y = (-1, 1):   (-1)(x1 + x2) + (1)(x1 + x2) = 0",
                "                              (-1)(1)       + (1)(4)       = 3",
                "   every coefficient cancels and 0 >= 3,   which is the contradiction",
            ],
            "after": [
                "The number `3` is the interesting one. It is not a residual and not a "
                "tolerance: it is the exact minimum amount of artificial quantity the "
                "two rows require, and it is positive, so no assignment of `x₁` and "
                "`x₂` satisfies both. The multipliers turn the same fact into an "
                "argument a reader can check in two lines without running anything.",
                "Note also what the first phase did <em>not</em> do on the feasible "
                "programme: it did not look at `2x₁ + 3x₂` once. The two pivots that "
                "reached feasibility were chosen to remove artificials, and the point "
                "they arrived at, `(0, 5)` moving to `(1, 3)`, has no claim to be good. "
                "Feasibility first, optimality second, and the objective is not "
                "consulted until the handover.",
                "For a faded rehearsal, run the redundant preset in the lab: "
                "`x₁ + x₂ = 4` with `2x₁ + 2x₂ = 8` and `x₂ ≤ 3`, maximising "
                "`x₁ + 2x₂`. The supplied first move is that the second row is the "
                "first one doubled, so one of the two artificials can never be replaced "
                "by a real column. Predict the first-phase optimum, predict which "
                "artificial is left basic and at what value, say whether that is a "
                "failure, and then check the optimum of `7` in the panel.",
            ],
        },
        "quiz_title": "Artificials, phases and certificates",
        "quiz": [
            {"q": "Why does `x₁ + x₂ ≥ 4` need an artificial variable rather than just a surplus?",
             "a": ["Because a surplus can be negative",
                   "Because the surplus column is `-1`, so starting from it would read a negative value",
                   "Because a `≥` row has no right-hand side to read",
                   "Because the row must be multiplied by `-1` first"],
             "c": 1,
             "why": "The row becomes `x₁ + x₂ - e₁ = 4`, and the column of `e₁` is "
                    "`-1` rather than an identity column; the basis it would give reads "
                    "`e₁ = -4`. A surplus is a non-negative variable like any other, "
                    "and multiplying the row by `-1` only moves the problem to the "
                    "right-hand side."},
            {"q": "The first phase finishes with optimum `0` and one artificial still in the basis at value `0`. What should you do?",
             "a": ["Start again: the setup was wrong",
                   "Report the programme as infeasible",
                   "Go on to the second phase &mdash; this is a degenerate basic feasible solution",
                   "Remove that row from the programme and re-run the first phase"],
             "c": 2,
             "why": "The optimum is zero, so every artificial is at zero and the "
                    "reading is a genuine feasible point of the original constraints. "
                    "An artificial basic at zero usually means the row it sits in is "
                    "redundant, which is degeneracy rather than an error; infeasibility "
                    "is a <em>positive</em> first-phase optimum."},
            {"q": "A first phase on a four-row programme stops at `7`. What has been established?",
             "a": ["That the optimum of the original programme is `7`",
                   "That the original constraints have no non-negative solution at all",
                   "That the first phase needs more pivots",
                   "That the original programme is unbounded"],
             "c": 1,
             "why": "A positive minimum for the sum of the artificials says the "
                    "equations can be satisfied only with artificial quantity left in "
                    "them, so no feasible point exists. `7` is the certificate value "
                    "and has nothing to do with the original objective; an infeasible "
                    "programme has no optimum to be unbounded."},
        ],
        "mistakes": [
            ("Treating an artificial variable as a slack with a different name",
             "A slack measures the unused part of a resource and is a perfectly good "
             "positive number at many optima. An artificial measures nothing, exists "
             "only to fill an identity column, and a positive one at the end of the "
             "first phase is not a solution but a proof that there is none. Keeping the "
             "two apart in the labelling is what keeps the final reading honest."),
            ("Carrying the first phase's objective row into the second phase",
             "The first phase optimised the sum of the artificials, so its objective row "
             "holds reduced costs for that objective. The second phase needs a fresh "
             "row computed from the real objective at the handover basis. Reuse the old "
             "one and the entering-column decisions are being made about the wrong "
             "objective, with a tableau that otherwise looks correct."),
            ("Reading a first-phase optimum above zero as a convergence problem",
             "It is the answer. The value is exact, it is the minimum artificial "
             "quantity the rows require, and the multipliers turn it into a "
             "two-line contradiction. Adding pivots, restarting, or loosening a "
             "tolerance cannot move a number that is already optimal &mdash; and "
             "&ldquo;infeasible&rdquo; is frequently the most useful thing a model can "
             "tell you."),
        ],
        "standard": ("Finish when a positive first-phase optimum reads as a proof rather than as a failure.",
                     "You should be able to enlarge a mixed-constraint programme with "
                     "the right surpluses and artificials, name the starting basis, run "
                     "the first phase, decide feasibility from its optimum, hand over a "
                     "basis with a freshly computed objective row, and recognise an "
                     "artificial left basic at zero for what it is."),
        "note": "The first phase can also fail to start a programme for the opposite reason: the constraints are satisfiable and the objective has no best value on them. That is one of three tableaux that refuse to finish in a recognisable way, and each one has a signature you can see without drawing anything. “Unbounded and Alternative Optima in the Tableau” takes two of them, and “Degeneracy, Cycling and Bland&rsquo;s Rule” takes the third.",
    },
]
