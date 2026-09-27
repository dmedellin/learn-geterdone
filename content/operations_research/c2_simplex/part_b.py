"""The Simplex Method, lessons 06-09 - the three awkward tableaux, the matrix
identity behind every tableau, and the honest account of how fast the method is.

The two named pathologies here are measured by the kit and pinned by
`scripts/mathcheck.js`: Beale cycles in exactly 6 pivots under Dantzig's rule
and terminates in 6 at `1/20` under Bland's, and the Klee-Minty cube costs
Dantzig 3, 7 and 15 pivots at n = 2, 3, 4 against 3, 5 and 9 for Bland.
Neither figure is reproducible in floating point, which is a fact the pages say
out loud rather than a convention they follow quietly.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "unbounded-and-alternative-optima-in-the-tableau",
        "title": "Unbounded and Alternative Optima in the Tableau",
        "module": "Awkward tableaux",
        "one_line": "Diagnose an unbounded objective and a non-unique optimum from the tableau, and produce either the ray or the second corner.",
        "summary": (
            "Two of the three awkward cases have a signature you can see. An improving "
            "column with no positive entry means the objective is unbounded, and that "
            "column is the direction it escapes along, so the ray can be written down "
            "and evaluated. A zero reduced cost on a nonbasic column at optimality "
            "means a second optimal corner one pivot away, with every point of the edge "
            "between them optimal. Neither diagnosis is a statement about the shape of "
            "the region."
        ),
        "key": [
            "improving column, no positive entry ⟹ unbounded; that column is the ray",
            "x(t) = x + t·d     d_j = 1,  d for the basic rows = -(the column)",
            "optimal, and z_j = 0 on a NONBASIC column ⟹ a second optimal corner",
            "and then every point of the edge between the two corners is optimal",
            "an unbounded REGION does not make an unbounded objective",
            "z_j = 0 on a BASIC column is not a signature - it is always true",
        ],
        "key_label": "Two signatures, and the two things they are not",
        "concepts_intro": (
            "Both diagnoses are single columns of a single tableau. The hard part is "
            "that each one is easily confused with a statement about the region, and "
            "one of them is easily confused with degeneracy."
        ),
        "concepts": [
            ("An improving column with no positive entry is the ray",
             "The ratio test on such a column has no candidates: every basic variable "
             "either holds still or grows as the entering variable rises. So the point "
             "`x + t·d`, where `d` puts one unit on the entering variable and "
             "`-(column)` on the basic ones, is feasible for every `t ≥ 0`, and the "
             "objective rises along it at the column&rsquo;s rate. The word "
             "&ldquo;unbounded&rdquo; and the ray are the same fact."),
            ("A zero reduced cost off the basis is a second optimum",
             "At optimality every reduced cost is at or above zero. If one of them is "
             "exactly zero on a column that is not basic, pivoting that column in "
             "changes the basis and leaves the objective unchanged &mdash; rate zero "
             "times any step is zero. Two corners at the same value, and because the "
             "objective is linear, every point of the segment between them is optimal too."),
            ("Neither is a fact about the region",
             "A region can run on for ever and still have a best point, if the "
             "objective falls in the directions the region escapes along. Unboundedness "
             "is a property of one column of one tableau &mdash; of the region and the "
             "objective together. “Covering and Diet Models” made this distinction with a "
             "picture; here it is arithmetic."),
        ],
        "read_title": "The ray, the second corner, and what neither one says about the region",
        "read_intro": "Reading a direction off a column, sampling an optimal edge, and the two confusions this page exists to prevent.",
        "body": [
            ("def", ("Unbounded objective, read from a tableau",
                    "A feasible tableau in which some column `j` has `z_j &lt; 0` and "
                    "`a_ij ≤ 0` for every row `i` certifies that the objective is "
                    "<strong>unbounded</strong>. The <strong>ray</strong> is "
                    "`x(t) = x + t·d` where `d_j = 1`, `d` is `-a_ij` on the variable "
                    "basic in row `i`, and zero on the other nonbasic variables.")),
            ("p", "The proof is the ratio test read the other way round. Row `i` says "
                  "`x_{B(i)} = b_i - a_ij·t`, and with `a_ij ≤ 0` that value never "
                  "falls, so no row stops `t` growing. The objective changes at rate "
                  "`-z_j` per unit of `t`, which is positive. A feasible point for every "
                  "`t` with an objective that rises without limit is exactly what "
                  "unboundedness means."),
            ("example", ("A ray, evaluated at three values of `t`",
                         "Take `maximise x₁ + x₂` subject to `x₁ - x₂ ≤ 1` and "
                         "`-x₁ + x₂ ≤ 1`. One pivot brings `x₁` in and leaves the "
                         "tableau with `x₂`&rsquo;s column at `(-1, 0)` and reduced "
                         "cost `-2`: improving, and no positive entry.",
                         "The ray is `d = (1, 1, 0, 0)` from the point `(1, 0)` with "
                         "`s₁ = 0` and `s₂ = 2`. At `t = 1` it is `(2, 1)` with "
                         "`z = 3`; at `t = 10`, `(11, 10)` with `z = 21`; at `t = 100`, "
                         "`(101, 100)` with `z = 201`. Every one of those points "
                         "satisfies both constraints, which is what turns the word into "
                         "a proof.")),
            ("math", [
                "  max x1 + x2      x1 - x2 <= 1,   -x1 + x2 <= 1",
                "",
                "              x1    x2    s1    s2   |   rhs",
                "   x1          1    -1     1     0   |     1",
                "   s2          0     0     1     1   |     2",
                "   z           0    -2     1     0   |     1",
                "",
                "  column x2:  z_2 = -2 < 0  improving,   entries (-1, 0)  none positive",
                "",
                "   t        point        s1   s2    z = 1 + 2t",
                "   0        (1, 0)        0    2        1",
                "   1        (2, 1)        0    2        3",
                "  10       (11, 10)       0    2       21",
                " 100      (101, 100)      0    2      201",
            ]),
            ("def", ("Alternative optima",
                    "An optimal tableau with `z_j = 0` for some <strong>nonbasic</strong> "
                    "column `j` has <strong>alternative optima</strong>. Pivoting `x_j` "
                    "in reaches a second optimal basis at the same objective value, and "
                    "every point of the segment joining the two basic feasible "
                    "solutions is optimal.")),
            ("p", "The word <em>nonbasic</em> is doing all the work in that definition. "
                  "A basic column always has reduced cost zero &mdash; that is how the "
                  "tableau is held &mdash; so a zero in a basic column is the normal "
                  "state of affairs and means nothing at all. The signature is a zero "
                  "where an improving column could have been and is not."),
            ("example", ("A whole optimal edge",
                         "Take `maximise 3x₁ + 2x₂` subject to `3x₁ + 2x₂ ≤ 12`, "
                         "`x₁ ≤ 3` and `x₂ ≤ 5`. The objective is a positive multiple "
                         "of the first constraint&rsquo;s left-hand side, so it is "
                         "parallel to that boundary. The method stops at `(3, 3/2)` "
                         "with `z = 12`, and the nonbasic column `s₂` has reduced cost "
                         "`0`.",
                         "One pivot on that column moves to `(2/3, 5)`, also with "
                         "`z = 12`. Sampling the segment between them at "
                         "`t = 1/4, 1/3, 1/2, 3/4` gives `(29/12, 19/8)`, `(20/9, 8/3)`, "
                         "`(11/6, 13/4)` and `(5/4, 33/8)`, and the objective at every "
                         "one of them is exactly `12`.")),
            ("p", "Reporting this honestly matters more than it looks. A solver that "
                  "prints one optimal corner has told you the truth and not the whole "
                  "truth: any point of that edge is equally good for the objective, "
                  "which usually means a second criterion is free to choose among them. "
                  "Naming the second corner costs one pivot."),
            ("h3", "An unbounded region whose objective is not"),
            ("p", "Take `maximise 2x₁ - x₂` subject to `x₁ - x₂ ≤ 1` and `x₁ ≤ 6`. The "
                  "region runs on for ever: raise `x₂` as far as you like and both "
                  "constraints stay satisfied. The objective nevertheless has a best "
                  "value, `7` at `(6, 5)`, because it <em>falls</em> in exactly the "
                  "direction the region escapes along. The method stops with every "
                  "reduced cost non-negative and there is no ray to report."),
            ("p", "So the two claims come apart in both directions. A bounded region "
                  "always bounds the objective; an unbounded region bounds it or does "
                  "not, depending on the objective. This is why the diagnosis is made "
                  "from a column and never from the drawing &mdash; and why, in "
                  "practice, an unbounded objective on a model of something real is "
                  "nearly always a missing constraint rather than an interesting "
                  "discovery."),
            ("h3", "The third awkward tableau, which is not either of these"),
            ("p", "Alternative optima and degeneracy are confused constantly, and the "
                  "distinction is one word. Alternative optima are a zero reduced cost "
                  "on a <em>nonbasic</em> variable: a second corner, same value. "
                  "Degeneracy is a zero <em>value</em> on a <em>basic</em> variable: one "
                  "corner, two bases, and a pivot that may move nothing. Degeneracy, "
                  "Cycling and Bland&rsquo;s Rule is the second, and it is the case that "
                  "can stop the method finishing at all."),
        ],
        "lab": ("simplex", {
            "mode": "auto",
            "preset": "signatures",
            "panel_title": "Switch between the ray and the whole edge",
            "panel_intro": "The ray and the second corner are both produced from the "
                           "tableau rather than from the drawing, and the third preset "
                           "is a region that runs on for ever under an objective that "
                           "does not.",
        }),
        "steps_title": "Diagnosing a tableau that will not finish in the ordinary way",
        "steps_intro": "Look at the column, not the picture. Each of these verdicts is a pattern of signs in one column and a number in the objective row.",
        "steps": [
            ("Before the ratio test, check the entering column for a positive entry",
             "If the column improves the objective and has no positive entry, stop "
             "pivoting: the ratio test has no candidates and the diagnosis is "
             "unboundedness. Nothing about the tableau is wrong and there is no other "
             "column worth trying."),
            ("Write the ray down and evaluate it",
             "One unit on the entering variable, minus the column on each basic "
             "variable, zero elsewhere. Evaluate at two or three values of `t`, check "
             "each point against the original constraints, and report the objective at "
             "each &mdash; that is the difference between asserting unboundedness and "
             "exhibiting it."),
            ("At optimality, scan the nonbasic columns for a zero",
             "Every basic column holds zero and tells you nothing. A zero on a nonbasic "
             "column means the optimum is not unique, and one pivot on that column "
             "produces the second corner."),
            ("Sample the edge rather than asserting it",
             "Take two or three points strictly between the two optimal corners and "
             "evaluate the objective at each. Constant means the whole edge is optimal, "
             "which is the claim worth making to whoever asked the question."),
            ("Say which claim you are making about the region",
             "&ldquo;The objective is unbounded&rdquo; and &ldquo;the region is "
             "unbounded&rdquo; are different statements, and only the first is a "
             "conclusion of the method. A region that runs on for ever can have a "
             "perfectly ordinary optimum."),
        ],
        "worked": {
            "title": "One ray and one optimal edge, both read off a column",
            "intro": [
                "Two small programmes, one signature each. In both cases the diagnosis "
                "is a column and the evidence is arithmetic on the original constraints.",
            ],
            "lines": [
                "UNBOUNDED      max x1 + x2      x1 - x2 <= 1,   -x1 + x2 <= 1",
                "",
                "              x1    x2    s1    s2   |   rhs      after one pivot",
                "   x1          1    -1     1     0   |     1      x1 = 1",
                "   s2          0     0     1     1   |     2      s2 = 2",
                "   z           0    -2     1     0   |     1      z = 1",
                "",
                "   x2:  reduced cost -2  (improving),  column (-1, 0)  (no positive entry)",
                "   ray  d = (1, 1, 0, 0)        x(t) = (1 + t,  t),   z(t) = 1 + 2t",
                "",
                "     t = 1     (2, 1)       1 - 1 = 0 <= 1,  -2 + 1 = -1 <= 1     z = 3",
                "     t = 10   (11, 10)     11 - 10 = 1 <= 1, -11 + 10 = -1 <= 1   z = 21",
                "     t = 100 (101, 100)   101 - 100 = 1 <= 1                      z = 201",
                "",
                "   feasible at every t, objective rising without limit:  unbounded",
                "",
                "ALTERNATIVE OPTIMA    max 3x1 + 2x2",
                "   3x1 + 2x2 <= 12,    x1 <= 3,    x2 <= 5",
                "",
                "              x1    x2    s1    s2    s3   |   rhs     basis {x2, x1, s3}",
                "   x2          0     1    1/2  -3/2    0   |   3/2",
                "   x1          1     0     0     1     0   |     3",
                "   s3          0     0   -1/2   3/2    1   |   7/2",
                "   z           0     0     1     0      0  |    12",
                "",
                "   s2 is NONBASIC and its reduced cost is 0     ⟹  a second optimum",
                "   one pivot on s2:   (3, 3/2)  ->  (2/3, 5),   z = 12 at both",
                "",
                "   t          point on the segment      3x1 + 2x2",
                "   1/4      (29/12, 19/8)                  12",
                "   1/3      (20/9,  8/3)                   12",
                "   1/2      (11/6,  13/4)                  12",
                "   3/4      (5/4,   33/8)                  12",
            ],
            "after": [
                "The ray is not an extrapolation. Each of the three points was put back "
                "into both original constraints and satisfies them, so there is no "
                "largest feasible `t` and no largest objective value. That is a proof, "
                "and it is the reason this course evaluates rays instead of describing "
                "them.",
                "On the second programme, notice where the zero is and where it is not. "
                "The basic columns `x₁`, `x₂` and `s₃` all hold zero in the objective "
                "row, and none of them is a signature &mdash; that is simply how a "
                "tableau is maintained. `s₂` is nonbasic and holds zero, and that is "
                "the whole diagnosis. Getting these two cases the wrong way round is "
                "the single commonest misreading of a final tableau.",
                "For a faded rehearsal, run the third preset in the lab: "
                "`maximise 2x₁ - x₂` subject to `x₁ - x₂ ≤ 1` and `x₁ ≤ 6`. The "
                "supplied first move is that the region is unbounded &mdash; check it "
                "by raising `x₂` in either constraint. Now predict whether the method "
                "reports a ray, find the optimum and the corner it sits at, and say in "
                "one sentence why the two facts are consistent.",
            ],
        },
        "quiz_title": "Rays, second corners and what they are not",
        "quiz": [
            {"q": "An improving column has entries `(0, -3, 0)`. What does the ratio test return?",
             "a": ["A step of `0`, from the first row",
                   "No candidates at all, which certifies that the objective is unbounded",
                   "A step of `-3`, from the second row",
                   "A step from whichever row has the smallest right-hand side"],
             "c": 1,
             "why": "The ratio test uses only strictly positive entries and there are "
                    "none, so no row limits the entering variable and the objective "
                    "rises without bound. A zero entry gives no ratio, a negative entry "
                    "gives no ratio, and the right-hand sides are irrelevant once no "
                    "row is eligible."},
            {"q": "A final tableau has reduced cost `0` on the basic column `x₂` and reduced cost `0` on the nonbasic column `s₃`. What follows?",
             "a": ["The optimum is non-unique, and the `x₂` zero is the evidence",
                   "The optimum is non-unique, and the `s₃` zero is the evidence",
                   "Both zeros say the same thing, so the evidence is doubled",
                   "The tableau is degenerate"],
             "c": 1,
             "why": "Every basic column holds zero in the objective row by construction, "
                    "so `x₂`&rsquo;s zero carries no information. `s₃` is nonbasic, so "
                    "pivoting it in changes the basis at no cost to the objective: a "
                    "second optimal corner. Degeneracy is a zero <em>value</em> on a "
                    "basic variable, which is a different reading of a different part of "
                    "the tableau."},
            {"q": "A feasible region runs on for ever in the direction `(0, 1)`. What does that tell you about the objective?",
             "a": ["It is unbounded, because the region is",
                   "It is bounded, because a linear objective on a closed region always has a maximum",
                   "Nothing on its own: it depends on the objective's rate along that direction",
                   "It is unbounded unless the objective coefficient on `x₂` is zero"],
             "c": 2,
             "why": "`maximise 2x₁ - x₂` on `x₁ - x₂ ≤ 1`, `x₁ ≤ 6` has an unbounded "
                    "region and an optimum of `7`, because the objective falls along "
                    "`(0, 1)`. A positive rate along an escape direction gives "
                    "unboundedness, a negative one does not, and a coefficient of zero "
                    "is only one of the bounded cases rather than the condition."},
        ],
        "mistakes": [
            ("Reading an unbounded region as an unbounded objective",
             "The region of `x₁ - x₂ ≤ 1`, `x₁ ≤ 6` runs on for ever and "
             "`maximise 2x₁ - x₂` has the perfectly ordinary optimum `7` at `(6, 5)`, "
             "because the objective falls in the direction the region escapes along. "
             "Unboundedness is a property of one column of one tableau, which is the "
             "region and the objective together, and the drawing cannot settle it."),
            ("Taking a zero reduced cost on a basic column as alternative optima",
             "Every basic column has reduced cost zero in every tableau; it is how the "
             "tableau is held rather than a discovery. The signature is a zero on a "
             "column that is <em>not</em> basic, where an improving entry could have "
             "been. Reading the basic zeros this way finds alternative optima in every "
             "problem, which is how you can tell it is wrong."),
            ("Confusing alternative optima with degeneracy",
             "They live in different parts of the tableau and mean different things. "
             "Alternative optima: a zero reduced cost on a nonbasic variable, so a "
             "second corner exists at the same objective value. Degeneracy: a zero "
             "value on a basic variable, so one corner is described by two bases and a "
             "pivot can move nothing. The first is a reporting matter; the second can "
             "stop the method terminating."),
        ],
        "standard": ("Finish when you can produce the ray or the second corner from the tableau without drawing the region.",
                     "You should be able to recognise an improving column with no "
                     "positive entry, write down and evaluate the ray it defines, spot a "
                     "zero reduced cost on a nonbasic column at optimality, produce the "
                     "second corner and sample the edge, and say why an unbounded region "
                     "settles nothing about the objective."),
        "note": "The third awkward case is the only one that can stop the method rather than merely surprise it. A tie in the ratio test leaves a basic variable at zero, the next pivot can then change the basis without moving the point, and a sequence of such pivots can return to a basis already visited. “Degeneracy, Cycling and Bland&rsquo;s Rule” runs that to completion on a programme where it really happens, and gives the rule that makes it impossible.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "degeneracy-cycling-and-blands-rule",
        "title": "Degeneracy, Cycling and Bland's Rule",
        "module": "Awkward tableaux",
        "one_line": "Identify a degenerate tableau, reproduce a cycle that returns to its own starting tableau, and break it with a smallest-index rule.",
        "summary": (
            "A tie in the ratio test leaves a basic variable at zero, so the next pivot "
            "can change the basis without moving the point at all. A sequence of such "
            "pivots can return to a basis already visited, and then the method runs for "
            "ever: on one four-variable programme the tableau comes back to its "
            "starting form after six pivots, entry for entry. Bland's smallest-index "
            "rule makes that impossible, and since there are finitely many bases, that "
            "is what proves the method terminates."
        ),
        "key": [
            "tie in the ratio test ⟹ a basic variable lands at zero: a degenerate basis",
            "degenerate basis ⟹ the next pivot may have step 0 and move the point nowhere",
            "a basis can repeat: six degenerate pivots, and the tableau is back to the start",
            "Bland   enter the lowest-index improving column, leave by the lowest-index row",
            "under Bland no basis repeats, and there are finitely many ⟹ it terminates",
            "degeneracy is geometry - more boundaries through a corner than dimensions",
        ],
        "key_label": "A tie, a pivot of length zero, and the rule that ends the matter",
        "concepts_intro": (
            "The hard idea is that a pivot can be perfectly correct and accomplish "
            "nothing, and that a run of such pivots is not a stall but a loop."
        ),
        "concepts": [
            ("A tie leaves a basic variable at zero",
             "When two rows achieve the same minimum ratio, the step takes both of their "
             "basic variables to zero and only one of them leaves. The other stays in "
             "the basis at value zero, which is what <strong>degenerate</strong> means. "
             "Geometrically it is more constraint boundaries through one corner than the "
             "corner has dimensions: three lines through one point in two variables."),
            ("A pivot of length zero changes the basis and nothing else",
             "From a degenerate basis the ratio test can return a step of zero, because "
             "the winning row already has a right-hand entry of zero. The pivot is "
             "carried out, the basis changes, the objective does not move and neither "
             "does the point. Nothing is wrong: the method is walking between two bases "
             "that describe the same corner."),
            ("Enough zero-length pivots and a basis can repeat",
             "If the basis returns to one already visited with the same tableau, the "
             "method will make the same choices again and run for ever. That is "
             "<strong>cycling</strong>, it happens on constructed programmes with the "
             "most-negative rule, and it is defeated by choosing the entering column and "
             "the leaving row by lowest index instead."),
        ],
        "read_title": "Ties, zero-length pivots, a real cycle, and the rule that forbids it",
        "read_intro": "Where degeneracy comes from, what it does to a pivot, a programme that returns to its own first tableau, and why a smallest-index rule terminates.",
        "body": [
            ("def", ("Degenerate basic feasible solution",
                    "A basic feasible solution is <strong>degenerate</strong> when some "
                    "basic variable has value zero. Equivalently, more than `n` of the "
                    "constraint boundaries of an `n`-variable problem pass through the "
                    "point, so two or more different bases name it. A pivot from a "
                    "degenerate basis may have step zero.")),
            ("p", "Take `maximise 3x₁ + 9x₂` subject to `x₁ + 4x₂ ≤ 8` and "
                  "`x₁ + 2x₂ ≤ 4`. Both boundaries pass through `(0, 2)`, and so does "
                  "the axis `x₁ = 0`: three lines, one point, two variables. The ratio "
                  "test on the entering column `x₂` gives `8 ÷ 4 = 2` and `4 ÷ 2 = 2`, a "
                  "tie."),
            ("math", [
                "              x1    x2    s1    s2   |   rhs",
                "   s1          1     4     1     0   |     8       ratio 8/4 = 2",
                "   s2          1     2     0     1   |     4       ratio 4/2 = 2   tie",
                "   z          -3    -9     0     0   |     0",
                "",
                "  pivot 1:  x2 in,  row 1 leaves  (lowest row index on the tie)",
                "",
                "   x2        1/4     1    1/4     0   |     2",
                "   s2        1/2     0   -1/2     1   |     0       s2 basic AT ZERO",
                "   z        -3/4     0    9/4     0   |    18",
                "",
                "  pivot 2:  x1 in.   ratios  2 / (1/4) = 8   and   0 / (1/2) = 0",
                "            the step is 0, row 2 leaves, and the point does not move",
                "",
                "   x2          0     1    1/2  -1/2   |     2",
                "   x1          1     0    -1     2    |     0       x1 basic at zero",
                "   z           0     0    3/2   3/2   |    18       optimal",
            ]),
            ("p", "Two pivots, one of which moved nothing. The point was `(0, 2)` after "
                  "the first pivot and `(0, 2)` after the second; the objective was `18` "
                  "both times. What changed was the basis, from `{x₂, s₂}` to "
                  "`{x₂, x₁}`, and the second of those is the one whose objective row "
                  "certifies optimality. The zero-length pivot was not wasted: it was "
                  "the step that produced the certificate."),
            ("h3", "Cycling"),
            ("p", "If zero-length pivots can go on for a while, can they go round? They "
                  "can. The standard example is due to Beale, and it is worth stating in "
                  "full because the claim about it is exact:"),
            ("math", [
                "  maximise   (3/4)x1 - 150x2 + (1/50)x3 - 6x4",
                "",
                "     (1/4)x1 -  60x2 - (1/25)x3 + 9x4  <=  0",
                "     (1/2)x1 -  90x2 - (1/50)x3 + 3x4  <=  0",
                "                            x3         <=  1",
                "",
                "  all x >= 0.   Under the most-negative rule, with ties on the ratio",
                "  test broken by lowest row index, from the slack basis:",
                "",
                "   pivot   in    out   row   step   z after",
                "     1     x1    s1     1      0       0",
                "     2     x2    s2     2      0       0",
                "     3     x3    x1     1      0       0",
                "     4     x4    x2     2      0       0",
                "     5     s1    x3     1      0       0",
                "     6     s2    x4     2      0       0",
                "",
                "  basis after pivot 6 = {s1, s2, s3} = the basis it started from,",
                "  and the whole tableau is identical - entry for entry, objective",
                "  row included.  z = 0 at all seven tableaux; every step has length 0.",
            ]),
            ("p", "The right-hand sides of the first two rows are zero, so the starting "
                  "basic feasible solution is already degenerate, and every pivot after "
                  "that has step zero. Six pivots later the method is exactly where it "
                  "began, with the same tableau and therefore the same choices ahead of "
                  "it. Left alone it runs for ever at `z = 0`, and the true optimum of "
                  "the programme is `1/20`."),
            ("p", "That the sixth tableau <em>equals</em> the first is a claim about "
                  "equality of numbers, and it is the reason this course carries exact "
                  "fractions. The entries include `1/50` and `-1/25`; in floating point "
                  "the sixth tableau would come back nearly equal to the first and the "
                  "lesson would be a story about what nearly means. The comparison the "
                  "lab makes has no tolerance in it: four rows by eight columns plus the "
                  "objective row, entry for entry, and a difference of one millionth in "
                  "one entry is a difference."),
            ("h3", "Bland's rule"),
            ("def", ("Bland's rule",
                    "Among the columns with `z_j &lt; 0`, enter the one with the "
                    "<strong>lowest index</strong>. Among the rows achieving the minimum "
                    "ratio, leave from the one whose basic variable has the lowest "
                    "index. Neither choice looks at the size of a coefficient.")),
            ("thm", ("Bland's rule terminates",
                     "The simplex method with Bland&rsquo;s rule, started from a basic "
                     "feasible solution, reaches an optimal basis or a certificate of "
                     "unboundedness after finitely many pivots. On the programme above "
                     "it takes six pivots and stops at `1/20`.")),
            ("proof", [
                "There are at most `n` choose `m` bases, which is a finite number. Each "
                "pivot moves to a different basis, and no basis under Bland&rsquo;s rule "
                "is ever visited twice &mdash; that is the rule&rsquo;s content, and it "
                "is a case analysis on the lowest-indexed column that leaves and "
                "re-enters, which this course states and does not carry out.",
                "Granting it, termination follows immediately: a walk through a finite "
                "set that never repeats a member must stop, and it can only stop where "
                "the method stops, which is at an optimal tableau or at a column with no "
                "positive entry. Note what this does <em>not</em> claim &mdash; nothing "
                "about how many of those finitely many bases get visited, which is the "
                "subject of “Termination and the Klee&ndash;Minty Cube”.",
            ]),
            ("p", "On Beale&rsquo;s programme the two rules agree for four pivots and "
                  "then part company. Bland&rsquo;s fifth pivot brings `x₁` back in "
                  "leaving row `3` &mdash; a step of `2/125`, the first pivot of the run "
                  "that moves the point at all &mdash; and its sixth reaches "
                  "`x = (1/25, 0, 1, 0)` with `z = 1/20`. Six pivots either way: the "
                  "same count, a different ending, and that contrast is the lesson. "
                  "Greatest improvement and the largest-index rule both reach `1/20` in "
                  "two."),
            ("h3", "What degeneracy is not"),
            ("p", "It is not rounding, and it is not a symptom of arithmetic trouble. "
                  "Every number in the cycle above is an exact fraction and the cycle is "
                  "still there; degeneracy is three constraint boundaries through one "
                  "corner, which is a geometric fact about the constraints you wrote "
                  "down. It is also extremely common in practice &mdash; any model with "
                  "redundant rows or coincident boundaries has it &mdash; while cycling "
                  "itself is rare enough that many implementations do not defend against "
                  "it until a problem turns out to need it."),
        ],
        "lab": ("simplex", {
            "mode": "degenerate",
            "panel_title": "Run the cycle, then break it",
            "panel_intro": "The six tableaux are printed and the sixth is compared with "
                           "the first entry for entry, with no tolerance anywhere; "
                           "switching the rule ends the cycle on the same programme.",
        }),
        "steps_title": "Recognising degeneracy and dealing with a cycle",
        "steps_intro": "Watch the ratio test, not the objective. A tie is the announcement, and it arrives one pivot before anything looks wrong.",
        "steps": [
            ("Note every tie in the ratio test",
             "Two rows at the same minimum means the next basis is degenerate whichever "
             "row you take. Write down which one you took and which variable is left "
             "basic at zero; that variable is the one the next pivot may expel for "
             "nothing."),
            ("Check the right-hand column for a zero after each pivot",
             "A zero entry on a basic row is the signature of a degenerate basis. It is "
             "not an error, and nothing needs correcting &mdash; it is the warning that a "
             "step of length zero is now possible."),
            ("Distinguish an unchanged objective from a finished one",
             "A pivot with step zero leaves the objective exactly where it was. The "
             "stopping test is the objective row, never the objective value: keep "
             "pivoting while an improving column exists, however long the value has been "
             "still."),
            ("If a basis repeats, switch to Bland's rule and start again from there",
             "Compare bases rather than objective values, since the value is constant "
             "through a cycle. Under the lowest-index rule for both the entering column "
             "and the leaving row, no basis can repeat, so the run terminates."),
            ("Report a degenerate optimum as an optimum",
             "A basic variable at zero in the final tableau is fine. What it does mean is "
             "that the optimal basis is not unique, so anything read off the objective "
             "row &mdash; the dual values in “Duality and Sensitivity Analysis”, for "
             "instance &mdash; may depend on which of the tied bases you stopped at."),
        ],
        "worked": {
            "title": "Beale's programme: six pivots back to where it started",
            "intro": [
                "The right-hand sides of the first two rows are zero, so the run is "
                "degenerate from the first tableau onwards and every step has length "
                "zero. Follow the basis rather than the objective value, which never "
                "changes.",
            ],
            "lines": [
                "maximise  (3/4)x1 - 150x2 + (1/50)x3 - 6x4",
                "  (1/4)x1 -  60x2 - (1/25)x3 + 9x4 <= 0",
                "  (1/2)x1 -  90x2 - (1/50)x3 + 3x4 <= 0",
                "                         x3        <= 1",
                "",
                "             x1     x2     x3     x4    s1   s2   s3  |  rhs",
                "   s1       1/4    -60   -1/25     9     1    0    0  |   0",
                "   s2       1/2    -90   -1/50     3     0    1    0  |   0",
                "   s3         0      0      1      0     0    0    1  |   1",
                "   z       -3/4    150   -1/50     6     0    0    0  |   0",
                "",
                "MOST-NEGATIVE RULE, ties on the ratio test by lowest row",
                "",
                "  tableau   basis              z",
                "     0      {s1, s2, s3}       0",
                "     1      {x1, s2, s3}       0      pivot 1:  x1 in,  s1 out, row 1",
                "     2      {x1, x2, s3}       0      pivot 2:  x2 in,  s2 out, row 2",
                "     3      {x3, x2, s3}       0      pivot 3:  x3 in,  x1 out, row 1",
                "     4      {x3, x4, s3}       0      pivot 4:  x4 in,  x2 out, row 2",
                "     5      {s1, x4, s3}       0      pivot 5:  s1 in,  x3 out, row 1",
                "     6      {s1, s2, s3}       0      pivot 6:  s2 in,  x4 out, row 2",
                "",
                "  tableau 6 = tableau 0, entry for entry, objective row included.",
                "  every step has length 0.   the method will now repeat for ever.",
                "",
                "SMALLEST-INDEX RULE on the same programme",
                "",
                "  pivots 1 to 4 are the same four pivots as above, all of length 0",
                "  pivot 5   x1 in,  s3 out, row 3    step 2/125    z: 0 -> 1/125",
                "  pivot 6   s1 in,  x4 out, row 2    step 3/100    z: 1/125 -> 1/20",
                "",
                "  x = (1/25, 0, 1, 0)      z* = 3/4 · 1/25 + 1/50 · 1 = 3/100 + 2/100 = 1/20",
                "",
                "  6 pivots either way.  one ends where it began; the other ends at 1/20.",
                "  greatest improvement: 2 pivots to 1/20.  largest index: 2 pivots to 1/20.",
            ],
            "after": [
                "The first four pivots are identical under both rules, which is worth "
                "noticing: cycling is not caused by a run of bad choices but by the last "
                "one. At the fifth pivot the most-negative rule picks `s₁` and the "
                "lowest-index rule picks `x₁`, and that single difference is the "
                "difference between a loop and an answer.",
                "The claim that tableau `6` equals tableau `0` is checked, not asserted. "
                "The comparison covers the basis, all four rows including the right-hand "
                "column, and the objective row, with no tolerance: perturb one entry by "
                "a millionth and it reports a difference. In floating point the entries "
                "`1/50` and `-1/25` are not represented exactly at all, so the sixth "
                "tableau would come back <em>almost</em> equal and the exact claim could "
                "not be made in either direction. This is the clearest case on the path "
                "where exactness is the content rather than the presentation.",
                "For a faded rehearsal, go back to `maximise 3x₁ + 9x₂` with "
                "`x₁ + 4x₂ ≤ 8` and `x₁ + 2x₂ ≤ 4` and take the <em>other</em> row on "
                "the tie: leave from row `2` at the first pivot instead of row `1`. The "
                "supplied first move is that the step is `2` either way, so the point is "
                "`(0, 2)` after the first pivot in both runs. Say which variable is left "
                "basic at zero this time, whether the second pivot moves the point, and "
                "whether the optimum or the number of pivots changes.",
            ],
        },
        "quiz_title": "Ties, zero-length pivots and termination",
        "quiz": [
            {"q": "Two rows tie for the minimum ratio. What is true of the basis after the pivot?",
             "a": ["It is infeasible, because one basic variable is negative",
                   "It is degenerate: the row not chosen keeps its basic variable, at value zero",
                   "It is optimal, because the objective cannot improve further",
                   "It depends on which row is chosen &mdash; one choice is degenerate and the other is not"],
             "c": 1,
             "why": "The step takes both tied rows' basic variables to zero and only one "
                    "leaves, so the other stays in the basis at zero: degenerate, and "
                    "degenerate either way you break the tie. Nothing is negative and "
                    "nothing about the objective row has been established."},
            {"q": "Six consecutive pivots leave the objective value unchanged at `0`. What should be concluded?",
             "a": ["The method has finished, since the objective has stopped improving",
                   "The arithmetic has lost precision and should be redone",
                   "Nothing yet &mdash; the stopping test is the objective row, and a run of degenerate pivots is not a stop",
                   "The programme is infeasible"],
             "c": 2,
             "why": "A degenerate pivot has step zero and therefore no effect on the "
                    "objective, so a constant value is not evidence of anything. The "
                    "method stops when no reduced cost improves, and on Beale's "
                    "programme it never does &mdash; the true optimum is `1/20`, reached "
                    "only once the rule is changed. The run is exact throughout, so "
                    "precision is not involved, and a run of pivots requires a feasible "
                    "point to begin with."},
            {"q": "What does Bland's rule change about the method?",
             "a": ["It reduces the number of pivots",
                   "It guarantees termination, by making it impossible for a basis to repeat",
                   "It makes each pivot cheaper to compute",
                   "It prevents degenerate bases from arising"],
             "c": 1,
             "why": "Bland's rule is about which pivot is chosen, not how many or how "
                    "cheaply: it can be slower than the most-negative rule and often is. "
                    "Its content is that no basis is visited twice, and since there are "
                    "finitely many bases the run must end. Degeneracy is a property of "
                    "the constraints and no entering rule removes it."},
            {"q": "Why does the claim “the sixth tableau equals the first” require exact arithmetic rather than merely benefit from it?",
             "a": ["Because the entries are large, and floating point loses the high digits",
                   "Because the claim is an equality of numbers, and entries like `1/50` and `-1/25` are not representable, so the comparison could only ever be approximate",
                   "Because the pivot count would change",
                   "Because the objective value `0` cannot be represented exactly"],
             "c": 1,
             "why": "&ldquo;Returns to where it started&rdquo; is a statement that two "
                    "tableaux are identical entry for entry. With `1/50` and `-1/25` "
                    "among the entries, a floating-point run would produce two tableaux "
                    "that are nearly equal, and the claim would have to be about a "
                    "tolerance instead. The entries are small rather than large, the "
                    "pivot count is a separate matter, and `0` is representable exactly."},
        ],
        "mistakes": [
            ("Reading an unchanged objective as a finished method",
             "A degenerate pivot has step zero, so the objective value is exactly where "
             "it was; six of them in a row leave it unmoved and the method is nowhere "
             "near finished. The stopping test is the objective row and not the "
             "objective value, and on Beale&rsquo;s programme the value sits at `0` "
             "through a complete cycle while the true optimum is `1/20`."),
            ("Diagnosing a cycle as a precision problem",
             "Every entry in that cycle is an exact fraction and the cycle is still "
             "there. Degeneracy is three constraint boundaries through one corner, which "
             "is a geometric property of the constraints, and cycling is a consequence of "
             "the entering and leaving rules. Raising the precision of the arithmetic "
             "changes neither, and the fix is a rule rather than a tolerance."),
            ("Treating a degenerate optimum as a defective answer",
             "A basic variable at zero in a final tableau is a perfectly good optimal "
             "solution; the point is optimal and the value is exact. What it does signal "
             "is that the optimal basis is not unique, so anything read out of the "
             "objective row rather than the right-hand column &mdash; dual values, "
             "sensitivity ranges &mdash; may differ between the tied bases, and that is "
             "worth saying when you report it."),
        ],
        "standard": ("Finish when a tie in the ratio test reads as a prediction about the next pivot.",
                     "You should be able to spot a degenerate basis from the right-hand "
                     "column, carry out a pivot of length zero and say what it "
                     "accomplished, follow a cycle by its bases rather than its objective "
                     "value, state Bland&rsquo;s rule and the termination argument it "
                     "supports, and say why the exactness is load-bearing here."),
        "note": "Bland&rsquo;s rule settles whether the method stops and says nothing about when. Both rules took six pivots on the programme above and one of them was still going round; other rules took two. The count is the last question this course asks, and the answer has three parts that are each true and none of which implies another &mdash; “Termination and the Klee&ndash;Minty Cube”. Before that, one identity: every tableau on any of these runs is the original data seen through a single matrix.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-tableau-as-a-matrix-product",
        "title": "The Tableau as a Matrix Product",
        "module": "Behind the tableau",
        "one_line": "Extract the basis matrix from a tableau, invert it, and rebuild the tableau body and objective row by multiplication.",
        "summary": (
            "Let `B` be the columns of the original coefficient matrix belonging to the "
            "current basis. Then the body of every tableau on the path is `B⁻¹[A | b]` "
            "and its objective row is `c_BᵀB⁻¹[A | b] - [c | 0]`, with `B⁻¹` itself "
            "sitting in whichever columns started as the identity. A tableau twenty "
            "pivots in is a view of the original data rather than a degraded copy of it, "
            "and one of the three products on this page is the solution of a second "
            "programme hidden in the first."
        ),
        "key": [
            "B      the columns of the ORIGINAL A belonging to the current basis",
            "body   = B⁻¹[A | b]                right-hand column = B⁻¹b",
            "z-row  = c_BᵀB⁻¹[A | b] - [c | 0]",
            "B⁻¹ sits in the columns that STARTED as the identity - not in the slacks",
            "a ≥ row's surplus column is -1; the identity column beside it is artificial",
            "c_BᵀB⁻¹ is the dual solution, read straight out of the objective row",
        ],
        "key_label": "One identity, and where the inverse actually sits",
        "concepts_intro": (
            "Nothing new is computed here. What changes is what a tableau <em>is</em>: "
            "not a record of what has been done to the data, but the data multiplied by "
            "one matrix."
        ),
        "concepts": [
            ("Every pivot is a left multiplication",
             "A pivot is a sequence of elementary row operations, and each of those is "
             "left multiplication by an invertible matrix. So the whole run of pivots "
             "amounts to one invertible matrix `M` applied to `[A | b]`. Because the "
             "basic columns of the result are the identity, `M·B = I`, so `M` is `B⁻¹` "
             "and there is nothing else it could be."),
            ("`B` comes from the original data, not from the tableau",
             "The basis is a set of column indices. `B` is those columns of the "
             "<em>original</em> `A`, before any pivoting, assembled in the order the "
             "tableau&rsquo;s rows carry them. Taking them from the current tableau gives "
             "the identity and a vacuous check; the content of the identity is that the "
             "original data is enough to reproduce a tableau twenty pivots later."),
            ("`B⁻¹` sits in the columns that started as the identity",
             "Not &ldquo;the slack columns&rdquo;. Those coincide after a `≤`-only "
             "setup and part company the moment a `≥` or an `=` row appears: the surplus "
             "column of a `≥` row is `-1`, and the identity column beside it is the "
             "artificial. Learn the rule and the block is always in the right place; "
             "learn the slogan and it is in the right place on the easy examples only."),
        ],
        "read_title": "Why a tableau is a product, and which columns hold the inverse",
        "read_intro": "The identity and its one-paragraph proof, the three products checked entry for entry, and the misreading that survives every caps-only example.",
        "body": [
            ("def", ("The basis matrix",
                    "For a standard-form programme with coefficient matrix `A` and a "
                    "basis whose columns, in row order, are `B(1), …, B(m)`, the "
                    "<strong>basis matrix</strong> `B` is the `m × m` matrix whose `i`-th "
                    "column is column `B(i)` of `A`. It is invertible, which is part of "
                    "what it means to be a basis.")),
            ("thm", ("Every tableau is the original data times one matrix",
                     "The tableau at basis `B` has body `B⁻¹[A | b]` and objective row "
                     "`c_BᵀB⁻¹[A | b] - [c | 0]`, where `c_B` is the vector of objective "
                     "coefficients of the basic variables in row order. In particular the "
                     "right-hand column is `B⁻¹b` and the reduced cost of column `j` is "
                     "`c_BᵀB⁻¹A_j - c_j`.")),
            ("proof", [
                "Each elementary row operation on a matrix is left multiplication by an "
                "invertible matrix, and a pivot is a composition of finitely many of "
                "them. So the tableau body after any run of pivots is `M[A | b]` for a "
                "single invertible `M`, because a product of invertible matrices is "
                "invertible.",
                "The tableau is held so that the basic columns form the identity: the "
                "columns of `M A` indexed by the basis are `I`. Those columns of `A` are "
                "`B` by definition, so `M B = I` and therefore `M = B⁻¹`. The objective "
                "row is the same argument on the extra equation: it starts as `-[c | 0]` "
                "and each pivot adds multiples of body rows to it until the basic columns "
                "read zero, which is exactly the combination `c_BᵀB⁻¹[A | b]`.",
            ]),
            ("p", "Two consequences follow at once. A tableau is not a degraded copy of "
                  "the data &mdash; it is `B⁻¹` times the data, recoverable from `A`, `b` "
                  "and a list of column indices. And every entry of it is a ratio of "
                  "determinants of submatrices of the original data, by Cramer&rsquo;s "
                  "rule, so the denominators never grow beyond what the numbers you typed "
                  "can produce, however many pivots it takes."),
            ("h3", "The three products, on a programme with a requirement row"),
            ("p", "Take `maximise 3x₁ + 2x₂` subject to `x₁ + x₂ ≤ 4` (capacity) and "
                  "`x₁ + 3x₂ ≥ 6` (a contract). The `≥` row gets a surplus `e₂` with "
                  "column `-1` and an artificial `a₂` with column `+1`, so the columns "
                  "are `x₁, x₂, s₁, e₂, a₂` and the starting identity is `{s₁, a₂}`. The "
                  "method finishes at the basis `{x₁, x₂}`."),
            ("math", [
                "  original data",
                "        x1   x2   s1   e2   a2  |   b",
                "   A     1    1    1    0    0  |   4",
                "         1    3    0   -1    1  |   6",
                "   c     3    2    0    0    0",
                "",
                "  final tableau, basis {x1, x2}",
                "        x1   x2    s1    e2    a2   |  rhs",
                "   x1    1    0    3/2   1/2  -1/2  |   3",
                "   x2    0    1   -1/2  -1/2   1/2  |   1",
                "   z     0    0    7/2   1/2  -1/2  |  11",
                "",
                "  B   = the x1 and x2 columns of the ORIGINAL A       B⁻¹",
                "        [ 1   1 ]                                    [  3/2  -1/2 ]",
                "        [ 1   3 ]                                    [ -1/2   1/2 ]",
                "",
                "  B⁻¹A  = [ 1  0   3/2   1/2  -1/2 ]     B⁻¹b = [ 3 ]",
                "          [ 0  1  -1/2  -1/2   1/2 ]            [ 1 ]",
                "",
                "  c_B = (3, 2)      c_BᵀB⁻¹ = (7/2, -1/2)",
                "  c_BᵀB⁻¹A - c = (0, 0, 7/2, 1/2, -1/2)",
                "",
                "  all three products agree with the tableau, entry for entry",
            ]),
            ("p", "Now the misreading. `B⁻¹` is `[[3/2, -1/2], [-1/2, 1/2]]`, and it "
                  "appears in the final tableau under the columns `s₁` and `a₂` &mdash; "
                  "the two that started as the identity. The slack and surplus columns "
                  "are `s₁` and `e₂`, and `e₂`&rsquo;s column is `(1/2, -1/2)`, which is "
                  "the <em>negative</em> of `B⁻¹`&rsquo;s second column, because "
                  "`A`&rsquo;s surplus column is the negative of its artificial column. "
                  "Read `B⁻¹` out of the slack and surplus columns and you get a matrix "
                  "whose determinant has the wrong sign."),
            ("example", ("The caps-only case, where the slogan happens to be true",
                         "On `maximise 3x₁ + 5x₂` with `x₁ ≤ 4`, `2x₂ ≤ 12` and "
                         "`3x₁ + 2x₂ ≤ 18`, all three rows are `≤` rows, the three "
                         "slacks are the starting identity, and the final tableau really "
                         "does hold `B⁻¹` under `s₁, s₂, s₃`: "
                         "`[[1, 1/3, -1/3], [0, 1/2, 0], [0, -1/3, 1/3]]` against a basis "
                         "matrix built from the `s₁`, `x₂` and `x₁` columns of the "
                         "original `A`.",
                         "Every example a reader is likely to have met is of this kind, "
                         "which is why the slogan survives. It stops being true at the "
                         "first `≥` row, and it also stops being true after a first phase "
                         "of “Artificial Variables and Two-Phase Simplex”, where the "
                         "starting identity contains artificials by construction.")),
            ("p", "One detail of the requirement-row tableau is worth explaining rather "
                  "than passing over: the reduced cost of `a₂` is `-1/2`, which is "
                  "negative in an optimal tableau. That column is an artificial, dropped "
                  "after the first phase and barred from re-entering, so it is not a "
                  "candidate and the optimality test does not apply to it. Its entry is "
                  "still a perfectly meaningful number &mdash; it is the second component "
                  "of `c_BᵀB⁻¹`."),
            ("h3", "The product that is a second answer"),
            ("p", "`c_BᵀB⁻¹` is `(7/2, -1/2)` here, and those two numbers are sitting in "
                  "the objective row under the columns that started as the identity. They "
                  "are the solution of a second linear programme built from the same "
                  "data, they say what one more unit of each right-hand side would be "
                  "worth, and finding them already computed in a row you have been "
                  "carrying since the first pivot is the whole opening of Duality and "
                  "Sensitivity Analysis."),
        ],
        "lab": ("simplex", {
            "mode": "matrix",
            "panel_title": "Rebuild the tableau from the original data",
            "panel_intro": "`B`, `B⁻¹` from the same row-reduction trace the elimination "
                           "course used, and the three products laid out beside the "
                           "tableau entry for entry &mdash; on a preset whose starting "
                           "identity is not the slack columns.",
        }),
        "steps_title": "Checking a tableau against the data it came from",
        "steps_intro": "The point of the exercise is that nothing but the original matrix and a list of indices is needed. Resist every temptation to read a number off the tableau you are checking.",
        "steps": [
            ("Write the basis down as column indices, in row order",
             "Row `1` carries one basic variable, row `2` another, and the order matters "
             "because it fixes the order of `B`&rsquo;s columns and of `c_B`. A "
             "permuted `B` inverts to a permuted `B⁻¹` and nothing will match."),
            ("Assemble `B` from the original `A`",
             "Those columns as they were before any pivoting. If you find yourself "
             "copying from the current tableau you will get the identity, and the check "
             "will pass without testing anything."),
            ("Invert `B` by reducing `[B | I]`",
             "The same row reduction as “Inverse Matrices”, and the same trace: when the "
             "left block is the identity the right block is `B⁻¹`. Keep it as exact "
             "fractions; this is the one matrix every other figure on the page depends "
             "on."),
            ("Multiply out `B⁻¹A` and `B⁻¹b` and compare entry for entry",
             "The body of the tableau and its right-hand column, respectively. Any "
             "single mismatch means an error in the basis order, in `B`, or in the "
             "pivoting &mdash; and you can tell which by whether the basic columns came "
             "out as the identity."),
            ("Build the objective row from `c_B`, `B⁻¹` and `A`",
             "`c_BᵀB⁻¹A - cᵀ`, which should reproduce the objective row including the "
             "zeros on the basic columns. Then read `c_BᵀB⁻¹` off the columns that "
             "started as the identity and check those two readings agree."),
        ],
        "worked": {
            "title": "B and B inverse on a programme whose identity is not the slacks",
            "intro": [
                "A capacity row and a contract row, so the columns are `x₁, x₂, s₁, e₂` "
                "and an artificial `a₂`. Everything below is built from `A`, `b`, `c` and "
                "the two basis indices.",
            ],
            "lines": [
                "maximise  3x1 + 2x2      x1 +  x2 <= 4    capacity",
                "                         x1 + 3x2 >= 6    contract",
                "",
                "standard form   x1 +  x2 + s1            = 4",
                "                x1 + 3x2      - e2 +  a2 = 6",
                "",
                "        x1   x2   s1   e2   a2  |   b          c = (3, 2, 0, 0, 0)",
                "   A     1    1    1    0    0  |   4",
                "         1    3    0   -1    1  |   6",
                "",
                "starting identity columns:  s1 (a slack)  and  a2 (an ARTIFICIAL)",
                "final basis, in row order:  x1 (row 1),  x2 (row 2)",
                "",
                "  B from the ORIGINAL A       reduce [B | I] until the left block is I",
                "     [ 1   1 ]                     [ 1  1 | 1  0 ]",
                "     [ 1   3 ]                     [ 1  3 | 0  1 ]",
                "                               R2 - R1,  then R2 ÷ 2,  then R1 - R2",
                "  B⁻¹  =  [  3/2  -1/2 ]           [ 1  0 |  3/2  -1/2 ]",
                "          [ -1/2   1/2 ]           [ 0  1 | -1/2   1/2 ]",
                "",
                "  B⁻¹A  =  [ 1  0   3/2   1/2  -1/2 ]      B⁻¹b  =  [ 3 ]",
                "           [ 0  1  -1/2  -1/2   1/2 ]               [ 1 ]",
                "",
                "  c_B = (3, 2)     c_BᵀB⁻¹ = (3·3/2 + 2·(-1/2),  3·(-1/2) + 2·(1/2))",
                "                            = (7/2, -1/2)",
                "  c_BᵀB⁻¹A - c   =  (0, 0, 7/2, 1/2, -1/2)",
                "",
                "the tableau on screen",
                "        x1   x2    s1    e2    a2   |  rhs",
                "   x1    1    0    3/2   1/2  -1/2  |   3",
                "   x2    0    1   -1/2  -1/2   1/2  |   1",
                "   z     0    0    7/2   1/2  -1/2  |  11      x = (3, 1),  z = 11",
                "",
                "WHERE B⁻¹ IS",
                "   columns that started as the identity:   s1,  a2",
                "      s1 column  ( 3/2, -1/2)  = column 1 of B⁻¹     correct",
                "      a2 column  (-1/2,  1/2)  = column 2 of B⁻¹     correct",
                "   the slack and surplus columns:          s1,  e2",
                "      e2 column  ( 1/2, -1/2)  = MINUS column 2 of B⁻¹",
                "      det of that pair = -1/2,   det B⁻¹ = 1/2",
            ],
            "after": [
                "The reason `e₂`&rsquo;s column is the negative of the right one is "
                "already in `A`: the surplus column is `(0, -1)` and the artificial "
                "column is `(0, 1)`, so multiplying by `B⁻¹` keeps them negatives of each "
                "other. Nothing has gone wrong in the pivoting &mdash; the wrong block "
                "was read out.",
                "The two numbers `(7/2, -1/2)` are worth a second look. They are "
                "`c_BᵀB⁻¹`, they appear in the objective row under `s₁` and `a₂`, and "
                "they are the marginal value of one more unit of each right-hand side: "
                "capacity is worth `7/2` per unit and the contract requirement costs "
                "`1/2` per unit. That is the dual solution, sitting in a row that has "
                "been carried along since the first pivot, and Duality and Sensitivity "
                "Analysis begins by naming it.",
                "For a faded rehearsal, take the caps-only programme `maximise 3x₁ + 5x₂` "
                "with `x₁ ≤ 4`, `2x₂ ≤ 12`, `3x₁ + 2x₂ ≤ 18`, whose optimal basis is "
                "`{s₁, x₂, x₁}` in row order. The supplied first move is that `B`&rsquo;s "
                "three columns are the `s₁`, `x₂` and `x₁` columns of the original `A`, "
                "in that order: `[[1,0,1],[0,2,0],[0,2,3]]`. Invert it, produce `B⁻¹A` "
                "and `B⁻¹b`, and then say why the slogan about the slack columns happens "
                "to be true on this one and not on the one above.",
            ],
        },
        "quiz_title": "The identity, and where the inverse lives",
        "quiz": [
            {"q": "Where do the columns of `B` come from?",
             "a": ["The basic columns of the current tableau",
                   "The columns of the original `A` indexed by the basis, in row order",
                   "The columns of the original `A` indexed by the basis, in increasing index order",
                   "The slack columns of the original `A`"],
             "c": 1,
             "why": "`B` is built from the untouched data, and the order of its columns "
                    "has to match the order the tableau&rsquo;s rows carry the basic "
                    "variables &mdash; a permuted `B` inverts to a permuted `B⁻¹` and "
                    "nothing matches. The basic columns of the current tableau are the "
                    "identity, which makes the check vacuous."},
            {"q": "A programme has one `≤` row and one `≥` row. In the final tableau, which columns hold `B⁻¹`?",
             "a": ["The slack column and the surplus column",
                   "The slack column and the artificial column",
                   "The two decision-variable columns",
                   "Whichever two columns are currently basic"],
             "c": 1,
             "why": "`B⁻¹` sits in the columns that started as the identity, and the "
                    "`≥` row&rsquo;s identity column is the artificial &mdash; its "
                    "surplus column is `-1`. The currently basic columns hold the "
                    "identity, not `B⁻¹`, and the decision columns hold `B⁻¹A` for those "
                    "columns of `A`."},
            {"q": "Twenty pivots into a run, a reader worries that the tableau has accumulated error. What does the identity `B⁻¹[A | b]` say about that?",
             "a": ["Nothing: error accumulation is a separate question about the arithmetic",
                   "That the tableau is determined by the original data and the basis, so there is no history to accumulate in it",
                   "That the error is bounded by the number of pivots",
                   "That the error can be removed by recomputing `B⁻¹`"],
             "c": 1,
             "why": "The tableau after any run of pivots equals `B⁻¹[A | b]` for the "
                    "basis it is standing on, so two runs reaching the same basis by "
                    "different routes produce the same tableau: there is no path "
                    "dependence to accumulate. With exact fractions the arithmetic is "
                    "exact as well, and by Cramer&rsquo;s rule every entry is a ratio of "
                    "determinants of the original data, so the denominators do not grow "
                    "with the pivot count either."},
        ],
        "mistakes": [
            ("Reading `B⁻¹` out of the slack columns",
             "They hold it when the starting basis was an identity in those columns, "
             "which is true after a `≤`-only setup and false after a first phase, and "
             "false for a `≥` row whose surplus column is `-1`. On the contract "
             "programme the surplus column is the negative of the right one, so the "
             "matrix read out has a determinant of the wrong sign. The rule is &ldquo;the "
             "columns that started as the identity&rdquo;, and the slogan is a special "
             "case of it."),
            ("Building `B` from the tableau you are checking",
             "Those columns are the identity, so `B⁻¹` comes out as the identity and "
             "every product agrees with the tableau it was copied from. The check passes "
             "and tests nothing. `B` is columns of the <em>original</em> `A`, and that is "
             "the entire content of the claim: the data plus a list of indices is enough "
             "to reproduce the tableau."),
            ("Treating a tableau many pivots in as a degraded copy of the data",
             "It is `B⁻¹` times the data. Two runs that reach the same basis by different "
             "routes produce the same tableau entry for entry, so there is no drift and "
             "no history stored in it; and by Cramer&rsquo;s rule every entry is a ratio "
             "of determinants of submatrices of the original numbers, so the denominators "
             "are bounded by what you typed rather than by how long the run was."),
        ],
        "standard": ("Finish when you can rebuild a tableau from the original data and a list of column indices.",
                     "You should be able to assemble `B` in row order from the original "
                     "`A`, invert it by reduction, reproduce the body, the right-hand "
                     "column and the objective row by multiplication, name the columns "
                     "that hold `B⁻¹` and say why they are not always the slacks, and "
                     "point at `c_BᵀB⁻¹` in the objective row."),
        "note": "This identity is where the claim about bounded denominators in this course&rsquo;s closing note comes from, and it is also the opening of “Duality and Sensitivity Analysis”: the dual solution is `c_BᵀB⁻¹`, one of the three products above. One question is left, and it is the one a reader who has now run the method by hand will ask first: how many pivots does this take? “Termination and the Klee&ndash;Minty Cube” answers it in three parts.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "termination-and-the-klee-minty-cube",
        "title": "Termination and the Klee-Minty Cube",
        "module": "Behind the tableau",
        "one_line": "Count the pivots on a deformed cube under two rules, and say what the worst case does and does not imply.",
        "summary": (
            "Finiteness is not efficiency. A smallest-index rule proves the method stops; "
            "a deformed `n`-dimensional cube makes the most-negative rule visit all `2ⁿ` "
            "of its corners, taking exactly `2ⁿ - 1` pivots; and ordinary problems finish "
            "in a small multiple of the number of rows. Those three statements are each "
            "true, none implies another, and saying all three is the honest status of the "
            "algorithm."
        ),
        "key": [
            "terminates      finitely many bases, and under Bland's rule none repeats",
            "the cube, n dims:   2ⁿ vertices, and the most-negative rule visits them all",
            "                    pivots  3, 7, 15   at n = 2, 3, 4   =  2ⁿ - 1",
            "smallest index on the same cube:    3, 5, 9",
            "greatest improvement:               1 at every n",
            "in practice     a small multiple of the number of rows",
            "finite, exponential in the worst case, fast in practice - three claims",
        ],
        "key_label": "Three true statements about the same algorithm",
        "concepts_intro": (
            "The hard idea is a negative one: three facts about the method are "
            "independent, and almost every confident sentence about simplex speed is one "
            "of them being used to imply another."
        ),
        "concepts": [
            ("Termination is a finiteness argument and nothing more",
             "There are finitely many bases and a smallest-index rule never repeats one, "
             "so the run ends. That argument says nothing whatever about how many of "
             "those bases get visited, and the number available grows combinatorially. "
             "&ldquo;It stops&rdquo; and &ldquo;it stops soon&rdquo; are different "
             "claims and only the first has been proved."),
            ("The worst case is constructed, and exact",
             "A deformed cube can be built whose `2ⁿ` vertices the most-negative rule "
             "visits every one of, costing `2ⁿ - 1` pivots: `3`, `7`, `15` at `n = 2, 3, "
             "4`. The coefficients run from `1` to `10ⁿ⁻¹` and the comparisons that pick "
             "the entering column have to land exactly. Round one of them the other way "
             "and the count collapses, taking the example with it."),
            ("The pivot count belongs to the rule and the objective, never the region",
             "Keep the same cube and the same optimal vertex, turn the objective "
             "coefficients round, and the most-negative rule walks straight there in one "
             "pivot. The smallest-index rule takes exactly what it took before, because "
             "it never reads a coefficient. Same region, same answer, counts from `1` to "
             "`15`."),
        ],
        "read_title": "What terminates, what the worst case is, and what neither one proves",
        "read_intro": "The cube, the counts under four rules, the two false implications this lesson exists to separate, and the sentence that is actually true.",
        "body": [
            ("p", "“Degeneracy, Cycling and Bland&rsquo;s Rule” closed with a guarantee: "
                  "with the smallest-index rule the method reaches an optimal basis or a "
                  "certificate of unboundedness in finitely many pivots. That guarantee "
                  "is a counting argument over the set of bases, and the set of bases is "
                  "large: `n` choose `m`, which for a hundred rows and two hundred "
                  "columns is a number with more than fifty digits. Finiteness on its own "
                  "promises nothing useful."),
            ("def", ("The Klee-Minty cube",
                    "For `n ≥ 2`, the programme `maximise Σ 10ⁿ⁻ʲ x_j` subject to "
                    "`2 Σ_{j &lt; i} 10ⁱ⁻ʲ x_j + x_i ≤ 100ⁱ⁻¹` for `i = 1, …, n`, with "
                    "`x ≥ 0`. Its feasible region is a deformed `n`-cube with `2ⁿ` "
                    "vertices, its optimum is `100ⁿ⁻¹`, and the most-negative entering "
                    "rule starting from the origin visits every vertex, taking "
                    "`2ⁿ - 1` pivots.")),
            ("p", "At `n = 3` that is `maximise 100x₁ + 10x₂ + x₃` subject to `x₁ ≤ 1`, "
                  "`20x₁ + x₂ ≤ 100` and `200x₁ + 20x₂ + x₃ ≤ 10000`. Eight vertices, "
                  "seven pivots, optimum `10000` at `(0, 0, 10000)` &mdash; which the "
                  "method reaches by walking through all eight."),
            ("math", [
                "  n = 3     max 100x1 + 10x2 + x3",
                "              x1                  <=      1",
                "            20x1 +   x2           <=    100",
                "           200x1 + 20x2 +  x3     <=  10000",
                "",
                "  most-negative rule, from the origin",
                "   after   x1    x2      x3        z",
                "   start    0     0       0        0",
                "     1      1     0       0      100",
                "     2      1    80       0      900",
                "     3      0   100       0     1000",
                "     4      0   100    8000     9000",
                "     5      1    80    8200     9100",
                "     6      1     0    9800     9900",
                "     7      0     0   10000    10000",
                "",
                "  8 vertices, 8 corners stood at, 7 pivots  =  2³ - 1",
                "",
                "  pivots taken, by rule",
                "    n    vertices   2ⁿ - 1   most negative   smallest index   greatest improvement",
                "    2        4         3           3                3                  1",
                "    3        8         7           7                5                  1",
                "    4       16        15          15                9                  1",
                "",
                "  optimum   100ⁿ⁻¹ :   100,   10000,   1000000",
            ]),
            ("p", "The doubling is the whole point, and it is already plain at `15`. "
                  "At `n = 5` the count is `31` against `15`, and there is no new "
                  "information in watching it, which is why the lab&rsquo;s dimension "
                  "control stops at four."),
            ("h3", "The count is a property of the rule and the objective"),
            ("p", "Keep the region exactly as it is and reverse the objective "
                  "coefficients &mdash; `1, 10, 100` instead of `100, 10, 1`. The "
                  "optimal vertex does not move. The most-negative rule now takes one "
                  "pivot at every `n`. The smallest-index rule takes `3`, `5`, `9` as "
                  "before, unchanged, because it never looks at a coefficient at all."),
            ("p", "So `2ⁿ - 1` is not a fact about cubes and not a fact about the "
                  "simplex method. It is a fact about one rule on one objective over one "
                  "region, and the construction is exactly the work of arranging all "
                  "three to be adversarial together. That is what &ldquo;worst "
                  "case&rdquo; means, and it is why worst cases have to be built rather "
                  "than found."),
            ("h3", "The two false implications"),
            ("p", "The first is &ldquo;the simplex method is exponential, so it is "
                  "slow&rdquo;. The premise is about a worst case over all inputs and the "
                  "conclusion is about the inputs anyone actually has. Observed pivot "
                  "counts on real problems run at a small multiple of the number of rows, "
                  "which is why the method was in production use for decades before "
                  "anyone knew whether linear programming was tractable at all."),
            ("p", "The second is its mirror: &ldquo;linear programming is polynomial, so "
                  "the simplex method is&rdquo;. Linear programming is solvable in "
                  "polynomial time &mdash; the ellipsoid method established it and "
                  "interior-point methods made it practical &mdash; and those are "
                  "different algorithms. A problem being in a complexity class says "
                  "nothing about a particular algorithm for it, any more than sorting "
                  "being possible in `n log n` time makes bubble sort fast."),
            ("p", "The words in both sentences are borrowed: &ldquo;worst case&rdquo;, "
                  "&ldquo;polynomial&rdquo; and &ldquo;input size&rdquo; are defined in "
                  "“P, NP and NP-Completeness” on the Discrete Mathematics path. That is a "
                  "citation rather than a prerequisite &mdash; nothing on this course "
                  "needs anything else from there, and a reader who has not taken it "
                  "loses only the formal definitions of three phrases used here in their "
                  "ordinary sense."),
            ("h3", "What is actually true"),
            ("p", "Three statements, each true, none implying another. The method is "
                  "<strong>finite</strong>, because under a smallest-index rule no basis "
                  "repeats and there are finitely many. It is "
                  "<strong>exponential in the worst case</strong>, because this cube "
                  "exists and the count on it is exactly `2ⁿ - 1`. It is "
                  "<strong>fast in practice</strong>, because problems like this cube are "
                  "constructed rather than met. Reporting all three is the honest status "
                  "of the algorithm, and dropping any one of them produces a sentence "
                  "that is wrong in a direction someone will act on."),
            ("p", "One last thing this course has to say about its own arithmetic. "
                  "Neither of the two famous results is reproducible in floating point at "
                  "all. The cycling example returns to its starting tableau entry for "
                  "entry only if nothing has been rounded, and the count `2ⁿ - 1` holds "
                  "only if the comparisons among coefficients from `1` to `10ⁿ⁻¹` land "
                  "exactly. Every figure on these nine pages is an exact fraction, and "
                  "in these two lessons that is the content rather than the style."),
        ],
        "lab": ("simplex", {
            "mode": "auto",
            "preset": "kleeminty",
            "panel_title": "Raise the dimension, and change the rule",
            "panel_intro": "Nothing here is a quoted figure: every count is a run of the "
                           "method on the cube built in your browser, under the rule you "
                           "chose, with the objective reversible on the same region.",
        }),
        "steps_title": "Saying how fast the method is, honestly",
        "steps_intro": "Four questions, asked separately. Most wrong statements about simplex speed come from answering one of them and reporting the answer as another.",
        "steps": [
            ("Ask whether it terminates, and on what rule",
             "The smallest-index rule terminates on every programme; the most-negative "
             "rule can cycle. That is a yes-or-no question about the rule, answered by a "
             "counting argument, and it has no numbers in it."),
            ("Ask what the worst case is, and name the construction",
             "&ldquo;Exponential&rdquo; here means: there is a family of programmes on "
             "which this rule takes `2ⁿ - 1` pivots. Name the family, because a worst "
             "case with no construction attached is a rumour, and the construction is "
             "what shows the objective is doing as much work as the region."),
            ("Ask what happens on the problems you actually have",
             "Run the method and count. Observed counts on ordinary models are a small "
             "multiple of the number of rows, which is a measurement rather than a "
             "theorem, and it is the number that decides whether the method is usable."),
            ("Keep the algorithm and the problem apart",
             "Linear programming is solvable in polynomial time by other methods. That is "
             "a statement about the problem, it does not transfer to the simplex method, "
             "and the reverse transfer &mdash; from the simplex worst case to the "
             "difficulty of linear programming &mdash; fails as well."),
            ("Report all three claims when asked which one is true",
             "They are all true. Finite, exponential in the worst case, fast in practice: "
             "a summary that keeps only the first is useless, only the second is "
             "alarmist, and only the third is unjustified."),
        ],
        "worked": {
            "title": "The three-dimensional cube: seven pivots, then one",
            "intro": [
                "Eight vertices and every one of them visited. The same region and the "
                "same optimal vertex are then solved in a single pivot by turning the "
                "objective coefficients round, which is the clearest statement of what "
                "the count actually depends on.",
            ],
            "lines": [
                "max 100x1 + 10x2 + x3",
                "     x1                <=      1",
                "   20x1 +  x2          <=    100",
                "  200x1 + 20x2 +  x3   <=  10000",
                "",
                "MOST-NEGATIVE RULE",
                "  pivot    in    out       vertex reached          z",
                "  start                    (0,   0,     0)         0",
                "    1      x1    s1        (1,   0,     0)       100",
                "    2      x2    s2        (1,  80,     0)       900",
                "    3      s1    x1        (0, 100,     0)      1000",
                "    4      x3    s3        (0, 100,  8000)      9000",
                "    5      x1    s1        (1,  80,  8200)      9100",
                "    6      s2    x2        (1,   0,  9800)      9900",
                "    7      s1    x1        (0,   0, 10000)     10000",
                "",
                "  7 pivots = 2³ - 1,   8 distinct vertices out of 2³ = 8",
                "",
                "SAME REGION, OBJECTIVE REVERSED:   max x1 + 10x2 + 100x3",
                "  pivot 1   x3 in, s3 out     (0, 0, 10000)      z = 1000000",
                "  the same vertex, in 1 pivot",
                "",
                "  smallest index on the reversed objective:  5 pivots, exactly as before",
                "",
                "ALL FOUR RULES, ALL THREE DIMENSIONS",
                "    n   vertices   2ⁿ-1   most neg.   smallest idx   greatest impr.   largest idx",
                "    2       4        3        3             3              1               1",
                "    3       8        7        7             5              1               1",
                "    4      16       15       15             9              1               1",
                "",
                "  optimum at every n:    100ⁿ⁻¹  =  100,  10000,  1000000",
                "  n = 5 would be 31 against 15; the doubling is already plain at 15",
            ],
            "after": [
                "Read the reversal carefully, because it is the whole lesson in two "
                "lines. The constraints did not change. The optimal vertex did not change "
                "&mdash; `(0, 0, 10000)` both times. Only the objective coefficients were "
                "turned round, and the most-negative rule went from seven pivots to one, "
                "while the smallest-index rule took exactly what it took before because "
                "it never reads a coefficient. `2ⁿ - 1` is a property of a rule and an "
                "objective together, not of a shape.",
                "None of these counts survives rounding. The coefficients at `n = 4` run "
                "from `1` to `1000`, the right-hand sides to `1000000`, and the "
                "comparisons that choose the entering column have to land exactly; in "
                "floating point one of them lands the other way, the count collapses, and "
                "the example goes with it. That is why the cube is here rather than in a "
                "footnote &mdash; it can only be shown on a page whose arithmetic is "
                "exact.",
                "For a faded rehearsal, set the lab to `n = 4` and work through the three "
                "questions separately before looking at the panel. The supplied first "
                "move is the bound: `2⁴ - 1 = 15`. Predict the most-negative count, then "
                "the smallest-index count, then the greatest-improvement count; then "
                "reverse the objective and predict all three again. Finally write one "
                "sentence about the speed of the simplex method that would still be true "
                "if all six predictions were wrong.",
            ],
        },
        "quiz_title": "Finite, exponential, fast: which is which",
        "quiz": [
            {"q": "The smallest-index rule is proved to terminate. What does that establish about the number of pivots?",
             "a": ["That it is at most the number of rows",
                   "That it is polynomial in the size of the programme",
                   "Nothing: the argument is that no basis repeats and there are finitely many",
                   "That it is at most `2ⁿ - 1`"],
             "c": 2,
             "why": "Termination is a counting argument over the set of bases and puts no "
                    "useful ceiling on how many are visited &mdash; the set itself grows "
                    "combinatorially. `2ⁿ - 1` is a measured count on one constructed "
                    "family under one rule, not a bound the proof delivers, and nothing "
                    "here gives a polynomial bound or a bound in terms of the rows."},
            {"q": "On the cube at `n = 3` the most-negative rule takes seven pivots. What happens if the objective coefficients are reversed, leaving the constraints alone?",
             "a": ["The optimum changes, and the count stays at seven",
                   "The optimal vertex is the same, and the most-negative rule reaches it in one pivot",
                   "Both rules take one pivot, because the region is unchanged",
                   "The count doubles, because the objective is now adversarial in the other direction"],
             "c": 1,
             "why": "The same vertex `(0, 0, 10000)` is optimal for both objectives. The "
                    "most-negative rule takes one pivot on the reversed objective and "
                    "seven on the original, while the smallest-index rule takes five "
                    "either way because it never reads a coefficient. The objective value "
                    "at the optimum does change, since the objective did, but the vertex "
                    "and the region do not."},
            {"q": "“Linear programming can be solved in polynomial time, so the simplex method runs in polynomial time.” What is wrong with this?",
             "a": ["Nothing &mdash; both halves are true",
                   "The premise is false: linear programming is not solvable in polynomial time",
                   "The premise is true but is about the problem; a complexity class for a problem says nothing about one particular algorithm for it",
                   "The conclusion is true but for a different reason"],
             "c": 2,
             "why": "Linear programming really is solvable in polynomial time, by the "
                    "ellipsoid method and by interior-point methods. Those are different "
                    "algorithms, and the simplex method with the most-negative rule takes "
                    "`2ⁿ - 1` pivots on a constructed family, so it is not one of them. "
                    "A problem's complexity class constrains the best algorithm, not "
                    "every algorithm."},
            {"q": "Which single statement is the honest status of the simplex method?",
             "a": ["It is exponential, so it is slow",
                   "It is fast in practice, so the worst case is an academic curiosity",
                   "It is finite, exponential in the worst case, and fast in practice &mdash; three claims, none implying another",
                   "It is polynomial, because linear programming is"],
             "c": 2,
             "why": "All three claims hold and each is independent of the others: the "
                    "finiteness proof gives no bound, the constructed worst case says "
                    "nothing about ordinary inputs, and the observed speed is a "
                    "measurement rather than a theorem. Keeping only one of them produces "
                    "a statement that is wrong in whichever direction the omission points."},
        ],
        "mistakes": [
            ("Reading the worst case as a statement about ordinary problems",
             "&ldquo;Exponential in the worst case&rdquo; means a family of programmes "
             "exists on which the count is `2ⁿ - 1`, and that family had to be "
             "constructed by making the region, the objective and the rule adversarial "
             "together. Observed counts on real models are a small multiple of the number "
             "of rows. Both facts are true and neither one is evidence about the other."),
            ("Transferring a complexity class from the problem to the algorithm",
             "Linear programming is solvable in polynomial time; the simplex method with "
             "the most-negative rule is not one of the algorithms that does it. A class "
             "constrains the best available algorithm and says nothing about any "
             "particular one &mdash; which is the same error as concluding that bubble "
             "sort is efficient because sorting can be done in `n log n` time."),
            ("Reading `2ⁿ - 1` as a property of the region",
             "Reverse the objective on the same cube and the most-negative rule takes one "
             "pivot to the same optimal vertex, while the smallest-index rule takes "
             "exactly what it took before. The count belongs to the rule and the objective "
             "together; the region only supplies the corners that a badly matched pair can "
             "be marched around."),
        ],
        "standard": ("Finish when you can state all three claims and say which of them the other two do not imply.",
                     "You should be able to state the termination argument and what it "
                     "does not deliver, run the cube at two dimensions and count the "
                     "pivots against `2ⁿ - 1`, change the rule and the objective and "
                     "explain the new counts, separate the two false implications about "
                     "polynomial time, and say why neither famous result is reproducible "
                     "in floating point."),
        "note": "That completes the algorithm: a start, a pivot, a stopping rule, a diagnosis for each way it can refuse to finish, and an honest count. One object from the final tableau has been named three times and never used &mdash; `c_BᵀB⁻¹`, the row of numbers sitting under the columns that started as the identity. “Duality and Sensitivity Analysis” is about that row: what each of its entries is worth, over what range of the data it stays worth that, and the second linear programme it solves.",
    },
]
