"""Geometric Algorithms, lessons 01-06 - the sign of a determinant, and the hull."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-orientation-test",
        "title": "The Orientation Test",
        "module": "The sign of a determinant",
        "one_line": "Every question this course asks reduces to the sign of one 2×2 determinant, computed three ways on the page.",
        "summary": (
            "Which side of a line a point falls on, whether two segments cross, which way a "
            "polygon is wound, whether a corner survives on a hull: all of them are the sign of "
            "the same determinant. The magnitude is twice the area of a triangle and is worth "
            "knowing, but almost every algorithm here throws it away and keeps the sign. The lab "
            "computes that one number by three different routes so that a transposed term shows "
            "up as a disagreement rather than as a plausible answer."
        ),
        "key": [
            "orient(a, b, c) = (bx − ax)(cy − ay) − (by − ay)(cx − ax)",
            "sign 1 left turn      sign −1 right turn      sign 0 collinear",
            "the magnitude is twice the area of the triangle a b c",
            "(0, 0), (4, 0), (2, 3):  determinant 12, so the area is 6",
            "(0, 0), (7, 3), (5, 2):  determinant −1, the smallest nonzero there is",
            "three routes to one number: 2×2 in BigInt, 3×3 by cofactors, doubles",
        ],
        "key_label": "One determinant, the sign it carries, and the area its magnitude is",
        "concepts_intro": (
            "One idea, and two things that follow from it. The determinant is a signed area; the "
            "sign answers a question about sides; and both of those are only true if the "
            "arithmetic is exact, which is what the rest of this module is about."
        ),
        "concepts": [
            ("A determinant is a signed area",
             "Put `b − a` and `c − a` side by side as the columns of a 2&times;2 matrix. Its "
             "determinant, `(bx − ax)(cy − ay) − (by − ay)(cx − ax)`, is twice the area of the "
             "triangle `a b c`, and it carries a sign. On the lab's opening points "
             "`(0, 0)`, `(4, 0)`, `(2, 3)` it is 12, so the triangle has area 6 and the turn from "
             "`a` to `b` to `c` is to the left. Nothing about that needs a picture; it is an "
             "integer computed from six integers."),
            ("The sign is what the algorithms actually use",
             "A convex-hull step asks &ldquo;did that turn go the wrong way&rdquo;; a segment "
             "test asks &ldquo;are these two endpoints on opposite sides&rdquo;; a polygon's "
             "winding asks &ldquo;is the total signed area positive&rdquo;. Each of those is a "
             "comparison of the determinant against zero, and the magnitude is discarded. That "
             "is why this course cares enormously about whether the sign is right and hardly at "
             "all about whether the value is close."),
            ("Exact means integers, and the input has to be one",
             "The lab refuses a coordinate with a decimal point rather than rounding it, and "
             "refuses anything past `2⁵³`. The second refusal is the interesting one: the "
             "determinant of huge integers is fine in arbitrary precision, but a coordinate "
             "beyond `2⁵³` is already the wrong number before any determinant is taken, so an "
             "exact answer about it would be an exact answer to a question nobody asked."),
        ],
        "read_title": "One determinant, and the three things it tells you",
        "read_intro": "The definition, the area theorem, the three routes the lab computes it by, and what each of them is for.",
        "body": [
            ("def", ("The orientation determinant",
                     "For points `a`, `b`, `c` in the plane, "
                     "<strong>orient(a, b, c)</strong> is "
                     "`(bx − ax)(cy − ay) − (by − ay)(cx − ax)`. Its "
                     "<strong>sign</strong> is `1` when the path `a → b → c` turns left "
                     "(counter-clockwise), `−1` when it turns right, and `0` when the three "
                     "points lie on one line. All three of `a`, `b`, `c` are ordered arguments: "
                     "swapping any two negates the determinant.")),
            ("p", "Two properties are worth having in hand before anything else. Negating on a "
                  "swap means `orient(a, b, c) = −orient(b, a, c)`, so &ldquo;left of the line "
                  "through `a` and `b`&rdquo; and &ldquo;right of the line through `b` and "
                  "`a`&rdquo; are the same statement. And the determinant depends only on the "
                  "DIFFERENCES `b − a` and `c − a`, so translating all three points by the same "
                  "vector changes nothing at all."),
            ("thm", ("The magnitude is twice the area",
                     "For any three points, `|orient(a, b, c)|` equals twice the area of the "
                     "triangle `a b c`. In particular the determinant is zero exactly when the "
                     "triangle is degenerate, which is exactly when the three points are "
                     "collinear.")),
            ("proof", ("Translate so that `a` is the origin; the determinant is unchanged and so "
                       "is the area. Write `u = b − a` and `v = c − a`. The parallelogram "
                       "spanned by `u` and `v` has area `|u| |v| sin θ`, where `θ` is the angle "
                       "from `u` to `v`, and the triangle is half of it.",
                       "Now `|u| |v| sin θ` is exactly `ux·vy − uy·vx` up to sign: expand "
                       "`|u| |v| sin(β − α)` with `u = |u|(cos α, sin α)` and "
                       "`v = |v|(cos β, sin β)` and the angle-difference identity gives "
                       "`|u| |v| (sin β cos α − cos β sin α)`, which is `ux·vy − uy·vx`. The sign "
                       "of `sin θ` is positive when `v` is counter-clockwise from `u` and "
                       "negative when it is clockwise, which is the sign claim, and the area is "
                       "half the absolute value, which is the magnitude claim.")),
            ("p", "So a determinant of 1 &mdash; the smallest nonzero value an integer "
                  "determinant can have &mdash; is a triangle of area one half. The lab's "
                  "`(0, 0)`, `(7, 3)`, `(5, 2)` example is exactly that: the determinant is `−1`, "
                  "the three points are very nearly on a line, and they are definitively not. "
                  "There is no room between &ldquo;area one half&rdquo; and &ldquo;area "
                  "zero&rdquo; for an integer to be uncertain about."),
            ("example", ("The same number by three different products",
                         "The lab's opening points are `(0, 0)`, `(4, 0)`, `(2, 3)`. The "
                         "2&times;2 route computes `(4 − 0)(3 − 0) − (0 − 0)(2 − 0) = 12`. The "
                         "3&times;3 route expands the determinant of the matrix whose rows are "
                         "`(0, 0, 1)`, `(4, 0, 1)`, `(2, 3, 1)` by cofactors along the last "
                         "column, giving `0·(0 − 3) − 0·(4 − 2) + (4·3 − 2·0) = 12`. The double "
                         "route runs the first expression in ordinary floating point and also "
                         "reports 12. Three routes, one number, and the lab prints all three "
                         "side by side.")),
            ("p", "Why bother with the second route at all, when it is algebraically the same "
                  "determinant? Because it is not the same ARITHMETIC. The 2&times;2 form "
                  "multiplies differences of coordinates; the 3&times;3 form multiplies the "
                  "coordinates themselves. A transposed subscript in either one produces a "
                  "number that looks entirely reasonable, and the only thing that catches it is "
                  "another route that would have to be wrong in precisely the same way. The lab "
                  "flags a disagreement in red and declines to say which side is right."),
            ("h3", "The sign answers four questions, and they are the same question"),
            ("p", "Is `c` to the left of the directed line `a → b`? That is `orient(a, b, c) "
                  "&gt; 0`. Do the segments `p₁p₂` and `q₁q₂` cross properly? That is four such "
                  "tests with opposite signs in pairs. Is the polygon `v₁ … vₙ` wound "
                  "counter-clockwise? That is the sum of `n` such determinants being positive. "
                  "Did the last point pushed onto a hull stack make a non-left turn, so the one "
                  "below it is not a corner after all? Same test again."),
            ("p", "Every page on this course is one of those four, which is why it is worth "
                  "spending a lesson on a single arithmetic expression. Get the sign wrong once "
                  "and the hull loses a vertex, the segment test answers about the wrong pair, "
                  "and the polygon reports the wrong orientation &mdash; each of them silently, "
                  "each of them returning a well-formed answer to a question it was asked "
                  "correctly."),
            ("h3", "Why the magnitude is kept as an integer even when it is thrown away"),
            ("p", "The lab prints the determinant, not just its sign, and the polygon page "
                  "prints twice the area rather than the area. Doubling is what keeps it an "
                  "integer: a lattice polygon's area can be a half, and a half is not "
                  "representable as an integer, but twice it always is. Halving is left to the "
                  "very end, and the result is printed as an exact fraction rather than as a "
                  "decimal close to it."),
            ("p", "That habit &mdash; postpone the division, keep the integer &mdash; is the "
                  "whole of exactness in this course. Distances are kept squared for the same "
                  "reason, since `√2` is not a number this library can write down exactly and "
                  "`2` is. Comparing squared distances orders pairs exactly as comparing "
                  "distances does, so nothing is lost by never taking the root."),
        ],
        "lab": ("geometry", {
            "mode": "orient",
            "preset": "turn",
            "panel_title": "Type three points and read the sign",
            "panel_intro": "The determinant is computed in BigInt, again by the cofactor "
                           "expansion of a 3&times;3 matrix, and a third time in ordinary double "
                           "arithmetic. The first two must agree on every input; the worked "
                           "examples at the foot of the list are where the third one stops "
                           "agreeing, and the next lesson is about them.",
        }),
        "steps_title": "Taking an orientation by hand",
        "steps_intro": "Subtract first, multiply second, and compare against zero third. Never divide.",
        "steps": [
            ("Subtract the first point from the other two",
             "Write `u = b − a` and `v = c − a` as two pairs of integers. This is where a "
             "hand computation goes wrong most often, and it is also where the arithmetic is "
             "guaranteed exact: a difference of two integers under `2⁵³` is an integer."),
            ("Form the two products and subtract them",
             "`ux·vy` and `uy·vx`, then the first minus the second. Keep both products whole; "
             "there is no intermediate quantity here that wants a decimal point."),
            ("Compare against zero and stop",
             "Positive is a left turn, negative is a right turn, zero is collinear. If the "
             "question you are answering is a side question, you are finished &mdash; do not "
             "compute a slope, an angle or a distance to confirm it, because each of those "
             "introduces a division the determinant did not need."),
            ("Use the magnitude only when you want the area",
             "Twice the area of the triangle, and nothing else. In particular the magnitude is "
             "not a distance from the line: that would be the determinant divided by `|b − a|`, "
             "and the moment you divide you are back in approximate arithmetic."),
        ],
        "worked": {
            "title": "Three points, three routes, one integer",
            "intro": [
                "Take `a = (0, 0)`, `b = (4, 0)`, `c = (2, 3)`, which is what the lab opens on, "
                "and then the near-degenerate triple `(0, 0)`, `(7, 3)`, `(5, 2)`.",
            ],
            "lines": [
                "a = (0, 0)   b = (4, 0)   c = (2, 3)",
                "",
                "  u = b − a = (4, 0)        v = c − a = (2, 3)",
                "  2x2:   4·3 − 0·2                     =  12",
                "  3x3:   0·(0 − 3) − 0·(4 − 2) + (4·3 − 2·0)  =  12",
                "  double: (4−0)·(3−0) − (0−0)·(2−0)    =  12",
                "  sign = 1  -> left turn,  area = 12/2 = 6",
                "",
                "a = (0, 0)   b = (7, 3)   c = (5, 2)",
                "",
                "  u = (7, 3)   v = (5, 2)",
                "  2x2:   7·2 − 3·5                     =  14 − 15  =  −1",
                "  3x3:   0·(3 − 2) − 0·(7 − 5) + (7·2 − 5·3)  =  −1",
                "  double:                                       =  −1",
                "  sign = −1 -> right turn,  area = 1/2",
            ],
            "after": [
                "The second triple is the smallest nonzero determinant there is, and it is worth "
                "sitting with. Those three points are visibly almost on a line: `(7, 3)` and "
                "`(5, 2)` differ from the slope `3/7` by a hair. But `14 − 15` is `−1` and not "
                "`0`, and an integer has no way of being nearly zero. The turn is a right turn, "
                "definitely, and the area is one half, definitely.",
                "Notice also that the 3&times;3 expansion does not compute a single one of the "
                "same products the 2&times;2 form does. It multiplies `7` by `2` and `5` by `3`, "
                "where the other multiplies the same numbers because `a` happens to be the "
                "origin. Move `a` to `(1, 1)` and the two routes share nothing at all: the "
                "2&times;2 form works with `(6, 2)` and `(4, 1)` and the 3&times;3 form still "
                "works with the original six coordinates. Redo both and confirm the answer is "
                "still `−1`.",
                "For a faded rehearsal, predict the determinant of `(0, 0)`, `(5, 2)`, `(7, 3)` "
                "&mdash; the same three points with the last two swapped &mdash; before "
                "computing it. The supplied first move is the swap rule: exchanging two "
                "arguments negates the determinant, so the answer is `+1` and the turn is a left "
                "turn. Then say what `orient(b, c, a)` is, and why a CYCLIC rotation of the three "
                "arguments leaves the sign alone while a swap does not.",
            ],
        },
        "quiz_title": "Signs, areas, and what a determinant does not tell you",
        "quiz": [
            {"q": "`orient(a, b, c) = −6`. What can you say about the triangle `a b c`?",
             "a": ["Its area is 6 and the vertices are listed counter-clockwise",
                   "Its area is 3 and the vertices are listed clockwise",
                   "Its area is −3, which is why the sign is negative",
                   "Its area is 6 and nothing about the ordering follows"],
             "c": 1,
             "why": "The magnitude is TWICE the area, so the area is 3, and an area is never "
                    "negative. The sign is the orientation: negative means the path `a → b → c` "
                    "turns right, which is a clockwise listing. Both halves of the answer come "
                    "from the one number, and neither is optional."},
            {"q": "Two implementations compute an orientation. One multiplies differences of coordinates, the other expands a 3×3 matrix of the coordinates themselves. Both return 48. What has been established?",
             "a": ["Nothing, since they are algebraically the same determinant",
                   "That 48 is correct, because two independent routes agree",
                   "That 48 is correct provided the arithmetic was exact, and the agreement is evidence because the two routes multiply different pairs of numbers",
                   "That the double-precision route would also return 48"],
             "c": 2,
             "why": "Algebraically the same and arithmetically different is exactly the point: a "
                    "transposed subscript in one expression does not produce the same wrong "
                    "answer in the other. The agreement is real evidence, not a tautology. It is "
                    "still conditional on exactness &mdash; two floating-point routes can agree "
                    "on the same wrong number, which is what the next lesson measures."},
            {"q": "You need to know how far a point is from a line, not just which side. Which is true?",
             "a": ["The determinant is that distance",
                   "The determinant divided by the length of the segment is that distance, and the division leaves exact arithmetic",
                   "The determinant is the distance provided the segment has unit length, and no algorithm on this course needs the distance anyway",
                   "Distance from a line cannot be computed from a determinant"],
             "c": 1,
             "why": "The perpendicular distance is `|orient(a, b, c)| / |b − a|`, so the "
                    "determinant is a numerator and the length is a square root. That division "
                    "is precisely what every algorithm on this course avoids, which is why the "
                    "predicates compare determinants against zero and against each other rather "
                    "than turning them into distances. The third option smuggles in a false "
                    "claim about what the course needs."},
        ],
        "mistakes": [
            ("Reading the determinant as a distance",
             "It is twice an area, and an area is a product of two lengths. A point twice as far "
             "from a long line can give the same determinant as a point close to a short one. "
             "Every time a page here compares two determinants it is comparing them across the "
             "SAME base pair, where the comparison is legitimate; comparing them across "
             "different bases is comparing areas of different triangles and means nothing."),
            ("Forgetting that the order of the arguments is data",
             "`orient(a, b, c)`, `orient(b, a, c)` and `orient(a, c, b)` differ in sign, and a "
             "predicate written with two of its arguments swapped answers the negation of the "
             "question. This is the single most common way a hull comes back inside out. The "
             "lab's cofactor column exists for exactly this: a swap in one route and not the "
             "other shows up as two different numbers."),
            ("Treating a near-zero determinant as zero",
             "With integer coordinates there is no such thing as near-zero. The smallest nonzero "
             "determinant is 1, which is a triangle of area one half, and `(0, 0)`, `(7, 3)`, "
             "`(5, 2)` is one. A tolerance that collapses small values to zero turns that "
             "genuine right turn into a false collinearity &mdash; and the following lesson "
             "shows double-precision arithmetic doing the same thing to itself, without anyone "
             "choosing a tolerance."),
        ],
        "standard": ("Finish when you can take an orientation by hand on three integer points and say what its sign and its magnitude each mean.",
                     "You should be able to write the determinant from the definition, predict "
                     "how it changes when two arguments are swapped or all three are translated, "
                     "state the area theorem and why doubling keeps it an integer, and explain "
                     "why a second route to the same number is worth computing."),
        "note": ("The whole of this course is that one sign, so it is worth knowing exactly when "
                 "the sign can be trusted. &ldquo;The Magnitude Where Doubles Lose the "
                 "Sign&rdquo; sweeps one family of triples up through the magnitudes and counts "
                 "the ones where the double-precision route stops agreeing &mdash; and proves a "
                 "sharper thing than &ldquo;floating point is unreliable&rdquo; about the way it "
                 "fails."),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-magnitude-where-doubles-lose-the-sign",
        "title": "The Magnitude Where Doubles Lose the Sign",
        "module": "The sign of a determinant",
        "one_line": "Sweep one family of triples up through the magnitudes and count the ones the double-precision predicate gets wrong.",
        "summary": (
            "At `(0, 0)`, `(2ᵏ + 1, 2ᵏ)`, `(2ᵏ, 2ᵏ − 1)` the determinant is `−1` for every `k`: "
            "the same right turn at every magnitude. In double arithmetic the two products "
            "collide once `2k` passes 53 and the predicate reports collinear. The lab sweeps 29 "
            "magnitudes and counts the failures rather than warning about them, and the failure "
            "has a shape: the double test can lose a turn, and it cannot invent the opposite one."
        ),
        "key": [
            "a = (0, 0),  b = (2ᵏ + 1, 2ᵏ),  c = (2ᵏ, 2ᵏ − 1)   for k = 20 … 48",
            "exact determinant = (2ᵏ+1)(2ᵏ−1) − 2ᵏ·2ᵏ = −1, at every magnitude",
            "29 magnitudes swept, 22 wrong, the first at 2²⁷",
            "the two products are 2²ᵏ − 1 and 2²ᵏ: one double once 2k > 53",
            "the double can collapse a turn to 0; it can never report the other turn",
            "coordinate differences under 2⁵³ are exact, and rounding to nearest is monotone",
        ],
        "key_label": "One family of triples, 29 magnitudes, and the count of wrong signs",
        "concepts_intro": (
            "One construction, one count, and one theorem about the shape of the failure. The "
            "theorem is the part worth carrying away, because it is stronger and more useful "
            "than the count."
        ),
        "concepts": [
            ("A family that is the same turn at every size",
             "Fix `k` and take `a = (0, 0)`, `b = (2ᵏ + 1, 2ᵏ)` and `c = (2ᵏ, 2ᵏ − 1)`. The "
             "determinant is `(2ᵏ + 1)(2ᵏ − 1) − 2ᵏ·2ᵏ`, which is `2²ᵏ − 1 − 2²ᵏ = −1`, for "
             "every `k` with no exceptions. So sweeping `k` upward is not sweeping through "
             "harder and harder geometry; it is asking one question &mdash; is this a right "
             "turn &mdash; whose answer is fixed, at larger and larger magnitudes."),
            ("What goes wrong is a collision, not an accumulation",
             "In double precision the two products are `2²ᵏ − 1` and `2²ᵏ`. A double has 53 bits "
             "of significand, so once `2k` exceeds 53 those two integers round to the SAME "
             "double, their difference is exactly `0`, and the predicate says collinear. There "
             "is no drift and no accumulation of small errors: below the threshold the answer is "
             "exactly right, above it the answer is exactly `0`, and the lab prints both "
             "columns so the step is visible as a step."),
            ("The failure has a direction, and that is the useful part",
             "Every disagreement the lab finds is the double reporting `0` where the exact test "
             "reports a turn. It never reports the opposite turn. The coordinate differences "
             "here are integers below `2⁵³` and so are exact, and rounding to nearest is "
             "monotone, so the rounded product of the larger pair cannot fall below the rounded "
             "product of the smaller one &mdash; it can only tie. So a hull built with the "
             "double predicate can be missing a corner, and cannot have a corner in the wrong "
             "place, which is a much more specific defect to go looking for."),
        ],
        "read_title": "One family, 29 magnitudes, and the shape of the failure",
        "read_intro": "The construction, the exact count, the threshold that is not an estimate, and the theorem that says how the failure can and cannot go.",
        "body": [
            ("def", ("The swept family",
                     "For an integer `k`, the <strong>needle at 2ᵏ</strong> is the triple "
                     "`a = (0, 0)`, `b = (2ᵏ + 1, 2ᵏ)`, `c = (2ᵏ, 2ᵏ − 1)`. Its exact "
                     "orientation determinant is `−1` for every `k`, so every member of the "
                     "family is the same right turn. The lab sweeps `k` from 20 to 48 and "
                     "reports, for each one, the exact determinant, the double determinant, and "
                     "whether the two signs agree.")),
            ("p", "The arithmetic is worth doing once by hand. With `a` at the origin the "
                  "determinant is `bx·cy − by·cx`, which is `(2ᵏ + 1)(2ᵏ − 1) − 2ᵏ·2ᵏ`. The "
                  "first product is a difference of squares, `2²ᵏ − 1`, and the second is "
                  "`2²ᵏ`. Subtract and everything cancels but the `−1`."),
            ("thm", ("The threshold, and the count",
                     "In IEEE double precision the needle at `2ᵏ` is evaluated correctly for "
                     "`k ≤ 26` and reports `0` for `k ≥ 27`. Over the 29 magnitudes from 20 to "
                     "48 the double predicate is therefore wrong on 22 of them, every one from "
                     "`2²⁷` upward, and right on the seven below.")),
            ("proof", ("A double holds a significand of 53 bits, so every integer up to `2⁵³` is "
                       "representable, and in the interval from `2ᵉ⁻¹` to `2ᵉ` the representable "
                       "numbers are spaced `2^(e − 53)` apart.",
                       "The two products are `2²ᵏ − 1` and `2²ᵏ`. For `2k ≤ 53` both are at most "
                       "`2⁵³` and so are represented exactly, their difference is computed "
                       "exactly, and the answer is `−1`. That is `k ≤ 26`.",
                       "For `2k ≥ 54`, the representable numbers just below `2²ᵏ` are spaced "
                       "`2^(2k − 53) ≥ 2` apart, so `2²ᵏ − 1` is not one of them: its neighbours "
                       "are `2²ᵏ − 2^(2k − 53)` and `2²ᵏ`, and it is at least as close to the "
                       "second as to the first. Where `2k = 54` the two are equidistant and "
                       "round-to-nearest breaks the tie towards the even significand, which is "
                       "`2²ᵏ`; where `2k &gt; 54` the second is strictly nearer. Either way both "
                       "products become the same double, their difference is exactly `0`, and "
                       "the subtraction introduces no further error. That is `k ≥ 27`. The sweep "
                       "from 20 to 48 is 29 values, of which 27 through 48 is 22.")),
            ("p", "Nothing in that argument is an estimate and nothing in it is a rule of thumb. "
                  "The lab does not quote the threshold either &mdash; it evaluates both routes "
                  "at all 29 magnitudes and counts, and the count it reports is 22 with the "
                  "first failure at `2²⁷`. Move the slider to highlight a row and the "
                  "corresponding triple appears in the upper table with all three routes beside "
                  "one another."),
            ("example", ("The two magnitudes either side of the threshold",
                         "At `k = 26` the points are `(0, 0)`, `(67108865, 67108864)`, "
                         "`(67108864, 67108863)`. The products are `4503599627370495` and "
                         "`4503599627370496`, both under `2⁵³`, both exact, and the difference "
                         "is `−1`: the double agrees. At `k = 27` the points are `(0, 0)`, "
                         "`(134217729, 134217728)`, `(134217728, 134217727)`. The products are "
                         "`18014398509481983` and `18014398509481984`, the first of which is not "
                         "representable, and both become `18014398509481984`. The double "
                         "determinant is `0` and the predicate calls a right turn collinear. One "
                         "power of two apart, and the answer changes from right to wrong.")),
            ("p", "That pair is the reason the preset list on this page has both of them in it. "
                  "Switching between the two worked examples changes one bit of the input and "
                  "flips the verdict of a predicate that most textbooks present without "
                  "qualification, which is a more convincing argument than any amount of prose "
                  "about machine epsilon."),
            ("h3", "The failure is one-sided, and that is provable"),
            ("thm", ("A collapse, never a flip",
                     "Let `a`, `b`, `c` have integer coordinates whose pairwise differences are "
                     "at most `2⁵³` in absolute value. If the double-precision evaluation of "
                     "`orient(a, b, c)` disagrees in sign with the exact one, then the "
                     "double-precision sign is `0`. It is never the opposite nonzero sign.")),
            ("proof", ("The four differences `bx − ax`, `cy − ay`, `by − ay`, `cx − ax` are "
                       "integers of magnitude at most `2⁵³`, so each is represented exactly and "
                       "the subtractions that produce them introduce no error at all. The only "
                       "rounding happens in the two products and in the final subtraction.",
                       "Write the two exact products as `P` and `Q`, so the exact determinant is "
                       "`P − Q`. IEEE multiplication returns the representable number nearest "
                       "its exact result, and round-to-nearest is monotone: if `P ≤ Q` then "
                       "`fl(P) ≤ fl(Q)`. Suppose the exact determinant is negative, so `P &lt; "
                       "Q`; then `fl(P) ≤ fl(Q)`, so `fl(P) − fl(Q) ≤ 0`, and the final "
                       "subtraction of two doubles cannot change the sign of a nonpositive "
                       "quantity. The computed determinant is therefore `≤ 0`: it can be the "
                       "right sign or it can be `0`, and it cannot be positive. The case `P &gt; "
                       "Q` is the same argument with the inequalities reversed.")),
            ("p", "This is a theorem and not a measurement, but the lab supplies the measurement "
                  "beside it: across the swept family every one of the 22 failures is the double "
                  "reporting `0`, and the arithmetic checker that runs over this kit throws "
                  "thirty thousand random near-collinear triples at `2²⁶` and above at both "
                  "routes. On those thirty thousand the two routes disagree 1,258 times, and "
                  "not once does the double report the opposite turn."),
            ("h3", "What a count on 29 magnitudes is and is not"),
            ("p", "The count is a measurement on one family. It says nothing about a triple "
                  "chosen some other way, and in particular &ldquo;22 of 29&rdquo; is not a "
                  "failure rate for double-precision geometry in general &mdash; the family was "
                  "constructed to fail, which is the only honest way to find the threshold. What "
                  "generalises is the theorem above it: the 53-bit argument applies to any "
                  "integer input, and the one-sidedness applies to any input at all."),
            ("p", "That distinction is the whole method of this path. A lab can run an algorithm "
                  "on an input; it cannot quantify over inputs. Here the two happen to line up "
                  "unusually well, because the threshold the sweep finds by measurement is the "
                  "same `2k &gt; 53` the proof gives, and a reader can check one against the "
                  "other on the page."),
        ],
        "lab": ("geometry", {
            "mode": "orient",
            "preset": "needle",
            "panel_title": "The sweep, and the magnitude where the double test stops agreeing",
            "panel_intro": "The lower table runs the same triple at 29 magnitudes and reports "
                           "both determinants and both signs for each. Nothing in it is quoted: "
                           "every row is computed in your browser, and the count of failures and "
                           "the first failing magnitude are read off those rows. Move the slider "
                           "to highlight a magnitude and it appears above with all three routes.",
        }),
        "steps_title": "Deciding whether a predicate can be trusted at a given size",
        "steps_intro": "Count the bits in the products, not the digits in the coordinates.",
        "steps": [
            ("Bound the coordinate differences, not the coordinates",
             "The determinant multiplies DIFFERENCES, so what matters is the spread of the point "
             "set, not its distance from the origin. Three points a millimetre apart on the far "
             "side of the world have small differences and behave well; the needle family is bad "
             "because the differences themselves are large."),
            ("Double the bit count and compare with 53",
             "If the differences fit in `m` bits then the products need about `2m`, and a double "
             "holds 53. Below `2m = 53` every product is exact and so is the subtraction. Above "
             "it, two products that differ by a little can land on the same double. This is why "
             "the threshold here is `2²⁷` and not `2⁵³`."),
            ("Ask what the algorithm does with a zero",
             "A predicate that collapses to zero is not harmless: a hull step reads zero as "
             "&ldquo;not a left turn&rdquo; and pops a real corner, and a segment test reads "
             "zero as &ldquo;collinear&rdquo; and takes a branch written for a different case. "
             "Find the branch the zero takes before deciding how bad the collapse is."),
            ("Use the one-sidedness to say what the defect can look like",
             "Since the double result can only lose a turn, a hull computed with it can be "
             "missing a vertex and cannot contain a point that is not on the true hull. That "
             "narrows a hunt for a bug from &ldquo;something is wrong&rdquo; to &ldquo;a vertex "
             "is missing&rdquo;, which the next lesson takes up."),
        ],
        "worked": {
            "title": "The sweep, read row by row across the threshold",
            "intro": [
                "Every row is the same right turn. The two columns in the middle are the exact "
                "determinant and the double one; the last two are the signs read off them.",
            ],
            "lines": [
                "  k        b                exact     double    ex  fl   verdict",
                " 24   (16777217, 16777216)     −1        −1      −1  −1   agree",
                " 25   (33554433, 33554432)     −1        −1      −1  −1   agree",
                " 26   (67108865, 67108864)     −1        −1      −1  −1   agree",
                " 27  (134217729, 134217728)    −1         0      −1   0   the double says collinear",
                " 28  (268435457, 268435456)    −1         0      −1   0   the double says collinear",
                " 29  (536870913, 536870912)    −1         0      −1   0   the double says collinear",
                "",
                " swept        20 … 48        29 magnitudes",
                " agreeing     20 … 26         7",
                " wrong        27 … 48        22,  every one reporting 0",
            ],
            "after": [
                "Three things to notice. First, the transition is a step and not a slope: there "
                "is no row where the double is close but not exactly right. Either the products "
                "are both representable and the answer is `−1`, or they collide and the answer "
                "is `0`.",
                "Second, the threshold is where `2k` passes 53 and not where `k` does. At "
                "`k = 26` the coordinates are around 67 million, which is nowhere near the "
                "largest integer a double holds; it is the PRODUCTS, around `4.5 × 10¹⁵`, that "
                "are up against the limit. A reader who checks the size of the inputs and "
                "concludes that everything is comfortable has checked the wrong quantity.",
                "Third, every failing row fails the same way. For a faded rehearsal, predict "
                "what the table would look like if the family were `c = (2ᵏ, 2ᵏ + 1)` instead, "
                "which makes the exact determinant `+1`. The supplied first move is that the "
                "products become `2²ᵏ + 1` and `2²ᵏ`, and `2²ᵏ + 1` rounds down to `2²ᵏ` above "
                "the threshold for exactly the same reason. Say what the failing rows then "
                "report, and confirm that the one-sidedness theorem predicted it.",
            ],
        },
        "quiz_title": "The threshold, the count, and what each one licenses",
        "quiz": [
            {"q": "The lab reports that the double predicate is wrong on 22 of 29 swept magnitudes. What follows about double-precision geometry generally?",
             "a": ["That roughly three quarters of orientation tests in doubles are wrong",
                   "Nothing about a rate: the family was constructed to fail, and the count locates the threshold on this family",
                   "That the double predicate is safe below 2²⁷ on any input",
                   "That an exact predicate is unnecessary below 2²⁷"],
             "c": 1,
             "why": "A count on a constructed family is a measurement of that family. It "
                    "pinpoints where THIS family breaks, which is what makes the threshold "
                    "concrete, and it says nothing about the frequency of failure on inputs "
                    "chosen some other way. The third and fourth options generalise a bound from "
                    "one family to all inputs, which is the mistake this whole path is "
                    "organised around."},
            {"q": "Why is the threshold at `k = 27` rather than at `k = 53`?",
             "a": ["Because doubles hold 27 bits of significand",
                   "Because the determinant multiplies two coordinates together, so the products need about `2k` bits and `2k` passes 53 at `k = 27`",
                   "Because the subtraction loses half the bits",
                   "Because the coordinates are of the form `2ᵏ + 1` rather than `2ᵏ`"],
             "c": 1,
             "why": "The inputs are comfortable; the products are not. Each coordinate is around "
                    "`2²⁷`, each product around `2⁵⁴`, and `2⁵⁴` is past the 53-bit significand. "
                    "The subtraction itself is exact in this case &mdash; both operands are the "
                    "same double, so their difference is exactly zero &mdash; and the "
                    "`+1` in the coordinate is what makes the determinant nonzero, not what "
                    "causes the rounding."},
            {"q": "A hull is built with the double predicate on coordinates around 2³⁰. Which defect is possible, given the one-sidedness theorem?",
             "a": ["A reported hull vertex that is strictly inside the true hull",
                   "A true hull vertex missing from the reported hull",
                   "Both of those, since a wrong sign can go either way",
                   "Neither: the theorem says the hull is correct"],
             "c": 1,
             "why": "The double determinant can only collapse to zero, so a turn can be read as "
                    "collinear but never as the opposite turn. A collinear reading makes the "
                    "chain pop a corner it should have kept, which loses a vertex. Inventing a "
                    "vertex would require a sign to flip, which the theorem rules out &mdash; "
                    "and that is why the theorem is worth more than the count."},
        ],
        "mistakes": [
            ("Checking the size of the inputs instead of the size of the products",
             "Coordinates around 67 million look modest and are modest; the products around "
             "`4.5 × 10¹⁵` are not. The rule of thumb that matters is to double the bit width "
             "before comparing with 53, and the lab's two adjacent worked examples exist so that "
             "this can be seen rather than reasoned about."),
            ("Reading “22 of 29” as a failure rate",
             "The family was built so that the determinant is `−1` at every magnitude, which is "
             "the hardest possible case and deliberately so. The count tells you where the "
             "threshold is; it does not tell you how often a randomly chosen triple is "
             "misjudged. Every page on this path puts a measured count beside a proved bound "
             "precisely so the two are not confused, and here the proof is the `2k &gt; 53` "
             "argument."),
            ("Fixing it with a tolerance",
             "Declaring the determinant zero when its absolute value is below some `ε` makes the "
             "problem worse in both directions: it converts genuine turns of area one half into "
             "collinearities, and it does nothing about the case here, where the computed value "
             "is exactly `0` and no tolerance can distinguish it from a real collinearity. The "
             "fix is exact arithmetic on the predicate, which costs BigInt multiplication and "
             "buys a sign that is simply right."),
        ],
        "standard": ("Finish when you can say at what magnitude a double-precision orientation test fails on integer input, and why the failure can only go one way.",
                     "You should be able to derive `2k &gt; 53` from the 53-bit significand, "
                     "read the sweep's count off the page as a measurement rather than a rate, "
                     "state the one-sidedness theorem and its monotonicity argument, and predict "
                     "which defects a hull built on the double predicate can and cannot have."),
        "note": ("A wrong sign is only interesting if something downstream acts on it. &ldquo;The "
                 "Vertex a Rounded Determinant Deletes&rdquo; takes the same three points to the "
                 "convex-hull page, runs Andrew's monotone chain with each predicate in turn, "
                 "and watches the stack pop a real corner."),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "the-vertex-a-rounded-determinant-deletes",
        "title": "The Vertex a Rounded Determinant Deletes",
        "module": "The sign of a determinant",
        "one_line": "Run one hull algorithm twice, changing only the predicate, and count the corners that come back.",
        "summary": (
            "Andrew's monotone chain sweeps the points in sorted order and pops from a stack "
            "whenever the last three do not turn left. Swap the exact predicate for the "
            "double-precision one and change nothing else: on the needle triple the exact chain "
            "returns three vertices and the double chain returns two. The lost corner is not "
            "recoverable downstream, because the hull that comes back is a perfectly well-formed "
            "hull of the wrong set."
        ),
        "key": [
            "pop while orient(second-from-top, top, p) ≤ 0, then push p",
            "a determinant that rounds to 0 is read as a non-left turn, and pops",
            "needle triple: exact chain 3 vertices, double chain 2",
            "the missing corner is (134217728, 134217727), the middle point in sorted order",
            "a vertex can be lost; by the one-sidedness theorem one cannot be invented",
            "the definition is checked separately, so the page knows which answer is wrong",
        ],
        "key_label": "One algorithm, two predicates, and the corner that disappears",
        "concepts_intro": (
            "The algorithm first, because the failure is a consequence of exactly one line of "
            "it; then what the pop does; then why nothing later can repair it."
        ),
        "concepts": [
            ("The chain is a stack and one comparison",
             "Sort the points by `x` then `y`. Walk them left to right keeping a stack; before "
             "pushing the next point `p`, pop while the last two on the stack and `p` fail to "
             "turn left. Then walk back right to left doing the same, and concatenate the two "
             "chains without their duplicated endpoints. The whole algorithm is a sort and that "
             "one comparison, which is why swapping the comparison is a clean experiment: "
             "everything else is identical."),
            ("A zero pops, and a pop is permanent",
             "The condition is `orient(s₂, s₁, p) ≤ 0`, so a determinant of zero pops. That is "
             "the right convention with exact arithmetic &mdash; it discards points that lie "
             "strictly inside an edge, which are not vertices. With a rounded determinant it is "
             "a catastrophe, because a genuine corner whose determinant rounded to zero is "
             "popped off and never looked at again. The lab's step-by-step trace shows the pop "
             "happening at a numbered step."),
            ("The wrong answer is well formed",
             "The hull the double predicate returns is a convex polygon with all its vertices "
             "among the input points. It passes every sanity check a downstream consumer would "
             "think to apply. The only way to know it is wrong is to compare it against the "
             "definition, and the lab does: every point is independently classified as a vertex, "
             "a boundary point or an interior point by rotating a separating line about it, with "
             "no sort and no stack anywhere in that computation."),
        ],
        "read_title": "One line of the algorithm, and what a rounded sign does to it",
        "read_intro": "The chain, the pop condition, the trace where the corner goes, and the definition that referees the two answers.",
        "body": [
            ("def", ("Andrew's monotone chain",
                     "Sort the distinct points lexicographically by `x` then `y`. Build the "
                     "<strong>lower chain</strong> by scanning left to right: maintain a stack, "
                     "and before pushing `p`, repeatedly pop the top while the stack has at "
                     "least two points and `orient(s₂, s₁, p) ≤ 0`, where `s₁` is the top and "
                     "`s₂` the one below it. Build the <strong>upper chain</strong> the same way "
                     "over the reversed order. The hull is the two chains concatenated with each "
                     "one's last point dropped, since it is the other's first.")),
            ("p", "The sort costs `n log n` and dominates; the scan is linear, because each "
                  "point is pushed once per chain and popped at most once per chain. The two "
                  "chains between them push exactly `2n` times and pop no more than they pushed, "
                  "so the stack work is at most `4n` operations. On the square-with-midpoints "
                  "example further down this course the lab measures 18 pushes and 12 pops, and "
                  "30 operations is inside the 36 that argument allows."),
            ("thm", ("What the chain computes",
                     "With an exact orientation predicate, the monotone chain returns exactly "
                     "the vertices of the convex hull of the input, in counter-clockwise order, "
                     "each once. Points strictly inside the hull and points lying in the "
                     "interior of a hull edge are both excluded.")),
            ("proof", ("Take the lower chain. Its invariant is that the stack is a sequence of "
                       "points increasing in `x` that turns strictly left at every interior "
                       "point of the sequence. The pop loop restores that invariant before each "
                       "push, and a push of a point with larger `x` cannot violate the part of "
                       "the sequence below it.",
                       "At the end, every point of the input lies on or above the lower chain: "
                       "if some point were below it, it would have been scanned at its own turn "
                       "and would have popped whatever lay above it. So the lower chain is the "
                       "lower boundary of the hull, and its interior points are exactly the hull "
                       "vertices whose neighbours lie to either side in `x`.",
                       "The upper chain is the mirror image and gives the upper boundary. Their "
                       "concatenation is the boundary of a convex polygon whose vertices are the "
                       "points at which it genuinely turns, because the pop condition was `≤ 0` "
                       "and so removed every point at which it does not.")),
            ("example", ("Three points, two predicates, and one missing corner",
                         "Take the needle triple `(0, 0)`, `(134217729, 134217728)`, "
                         "`(134217728, 134217727)`. Sorted, it is `(0, 0)`, then "
                         "`(134217728, 134217727)`, then `(134217729, 134217728)`. The exact "
                         "determinant of those three in that order is `+1`, a left turn, so the "
                         "lower chain pushes all three and the hull has 3 vertices. The double "
                         "determinant of the same three is `0`, which satisfies `≤ 0`, so the "
                         "middle point is popped at step 3 and the hull comes back with 2. The "
                         "lab prints both counts side by side and labels the shortfall.")),
            ("p", "Read the two traces beside each other in the lab's lower table. The exact run "
                  "is `push (0, 0)`, `push (134217728, 134217727)`, `push (134217729, "
                  "134217728)` on the lower chain: six pushes and one pop across both chains. "
                  "The double run is `push (0, 0)`, `push (134217728, 134217727)`, then `POP "
                  "(134217728, 134217727)`, then `push (134217729, 134217728)`. One extra pop, "
                  "one fewer vertex, and the pop is at the step where the rounded determinant "
                  "was consulted."),
            ("h3", "Nothing downstream can put the corner back"),
            ("p", "Suppose the hull is fed to the rotating-calipers diameter computation, or to "
                  "a point-in-polygon test, or to anything else that consumes a hull. It "
                  "receives a convex polygon on two of the three points. Every invariant it "
                  "would check holds: the points are input points, the polygon is convex, the "
                  "winding is consistent. The consumer has no evidence that anything is missing, "
                  "and the diameter it computes will be a real distance between two real points "
                  "&mdash; just not the right one when the missing corner was an endpoint."),
            ("p", "This is the argument for exact predicates stated as a number rather than as a "
                  "principle. It is not that floating point is imprecise; it is that a predicate "
                  "returning a discrete answer either returns the right discrete answer or "
                  "corrupts the data structure built on it, and there is no third option and no "
                  "amount of downstream care that recovers it."),
            ("h3", "What the lab checks the algorithms against"),
            ("p", "The page does not decide which hull is right by trusting either chain. Before "
                  "either algorithm runs, every point is classified from the definition: `p` is "
                  "a hull VERTEX when some line through `p` has every other point weakly on one "
                  "side and every point lying ON that line strictly beyond `p` along it. That is "
                  "a cubic-time test with no sort, no stack and no incremental step in it, and "
                  "the colours in the drawing come from it rather than from either algorithm."),
            ("p", "So the table in the middle of the lab is a comparison and not a restatement. "
                  "On the needle triple the definition says all three points are vertices, the "
                  "exact chain agrees, and the double chain is one short &mdash; and the row for "
                  "the missing point is marked. If the chain and the definition ever disagreed, "
                  "the status line would say so in red and decline to pick a winner, because a "
                  "page that reports two exact routes disagreeing is not entitled to guess which "
                  "one is broken."),
        ],
        "lab": ("geometry", {
            "mode": "hull",
            "preset": "needle",
            "panel_title": "Switch the predicate to doubles and count the vertices again",
            "panel_intro": "Both chains are run on every redraw, so the two vertex counts are "
                           "always side by side; the predicate control chooses which one the "
                           "drawing and the stack trace show. Every point's colour comes from the "
                           "definition, computed by brute force before either algorithm runs, so "
                           "the table is a check on both of them rather than a restatement of "
                           "one.",
        }),
        "steps_title": "Running the experiment yourself",
        "steps_intro": "Change one thing, and make sure the referee is not one of the things you changed.",
        "steps": [
            ("Fix everything but the predicate",
             "Same points, same sort, same stack, same pop condition. The lab's two arms are "
             "literally the same function with the comparison passed in as an argument, which is "
             "the only way the difference in the answer can be attributed to the comparison."),
            ("Read both counts, not the drawing",
             "The two hulls on the needle triple differ by one vertex out of three, and at this "
             "aspect ratio the drawing cannot show it: the three points are collinear to the "
             "width of a pixel. The counts differ, the table's row for the missing point is "
             "marked, and neither fact is visible in the picture."),
            ("Check both against something that is neither",
             "The brute-force classification from the definition is the referee. Where the "
             "chain and the definition agree, the page says so; where they do not, it says "
             "that too and stops. An experiment whose referee is one of the two arms has "
             "established nothing."),
            ("Try the same switch where it changes nothing",
             "Type points with small coordinates and switch the predicate back and forth: the "
             "two counts stay equal. That is the control. Without it, &ldquo;the double "
             "predicate gives a different answer&rdquo; could just as well be a bug in how the "
             "second arm was wired up."),
        ],
        "worked": {
            "title": "Both stacks, step by step, on the same three points",
            "intro": [
                "The points sorted are `(0, 0)`, `(134217728, 134217727)`, "
                "`(134217729, 134217728)`. Call them `A`, `B`, `C`. Only the lower chain differs "
                "between the two runs.",
            ],
            "lines": [
                "EXACT predicate                 orient(A, B, C) = +1",
                "  1 lower push A                depth 1",
                "  2 lower push B                depth 2",
                "  3 lower push C                depth 3     +1 is a left turn: no pop",
                "  4 upper push C                depth 1",
                "  5 upper push B                depth 2",
                "  6 upper pop  B                depth 1",
                "  7 upper push A                depth 2",
                "  hull = A B C                  h = 3       pushes 6, pops 1",
                "",
                "DOUBLE predicate                orient(A, B, C) = 0",
                "  1 lower push A                depth 1",
                "  2 lower push B                depth 2",
                "  3 lower POP  B                depth 1     0 satisfies ≤ 0",
                "  4 lower push C                depth 2",
                "  5 upper push C                depth 1",
                "  6 upper push B                depth 2",
                "  7 upper pop  B                depth 1",
                "  8 upper push A                depth 2",
                "  hull = A C                    h = 2       one corner short",
                "",
                "by the definition:  A, B, C are all three hull vertices",
            ],
            "after": [
                "The pop at step 3 is the entire defect. Every other step of the two runs is "
                "identical, and the eighth step in the double run exists only because the third "
                "one removed a point that had to be pushed again later. A reader watching the "
                "counts alone would see 3 against 2; a reader watching the trace sees the exact "
                "moment and the exact comparison responsible.",
                "Notice that `B` is popped from the UPPER chain in both runs, at step 6 and step "
                "7 respectively. That is correct and has nothing to do with rounding: the upper "
                "chain visits the points right to left, and on this triple `B` is below the line "
                "from `C` to `A`, so it belongs to the lower boundary and not the upper one. "
                "Only the lower-chain pop is the failure.",
                "For a faded rehearsal, work out what the two runs do on `(0, 0)`, "
                "`(67108865, 67108864)`, `(67108864, 67108863)`, which is the same shape one "
                "power of two smaller. The supplied first move is from the previous lesson: at "
                "`2²⁶` the two products are both under `2⁵³`, so the double determinant is `+1` "
                "as well. Predict both traces, then check that the lab reports 3 and 3.",
            ],
        },
        "quiz_title": "Pops, predicates, and what a well-formed answer proves",
        "quiz": [
            {"q": "The pop condition is `orient(s₂, s₁, p) ≤ 0` rather than `< 0`. With exact arithmetic, what does the `=` case do?",
             "a": ["It removes points that lie in the interior of a hull edge, which are not vertices",
                   "It removes duplicate points",
                   "It is a defensive tolerance against rounding",
                   "It makes no difference, since exact determinants are rarely zero"],
             "c": 0,
             "why": "A zero determinant means the three are collinear, so the middle one lies on "
                    "the segment between the other two and is on the boundary but not a corner. "
                    "Popping it is the convention that makes the chain return a VERTEX list. "
                    "Duplicates are removed separately and counted, before either algorithm "
                    "runs; and nothing about the condition is a tolerance &mdash; it is exactly "
                    "the behaviour that turns into a defect when the determinant is rounded."},
            {"q": "The double-predicate run returns a convex polygon whose vertices are all input points. Why is that not evidence that it is correct?",
             "a": ["Because convexity is hard to check",
                   "Because those properties also hold of the hull of any subset of the true vertices, so they cannot distinguish the right answer from a hull that is missing one",
                   "Because the polygon might have the wrong winding",
                   "Because the input points might not be exact"],
             "c": 1,
             "why": "Removing a vertex from a convex polygon leaves a convex polygon on input "
                    "points. Every structural invariant survives, which is exactly why the "
                    "defect is invisible downstream and why the page checks against the "
                    "definition rather than against a plausibility test."},
            {"q": "On the needle triple the double chain returns two vertices and the exact one returns three. Which claim does that support?",
             "a": ["That the double predicate is wrong on all near-collinear input",
                   "That a rounded predicate can delete a hull vertex, on this input, and by the one-sidedness theorem cannot add one on any input",
                   "That the monotone chain is the wrong algorithm for near-collinear input",
                   "That exact arithmetic is always slower"],
             "c": 1,
             "why": "The measurement is about the three points on screen. What generalises is "
                    "the theorem proved in the previous lesson: a rounded determinant can "
                    "collapse to zero and never flips sign, so deletion is possible everywhere "
                    "and insertion is possible nowhere. The algorithm is fine; it is the "
                    "predicate it was handed that was not."},
        ],
        "mistakes": [
            ("Blaming the algorithm rather than the predicate",
             "The monotone chain is correct: with an exact predicate it returns the vertex set "
             "on this input and on every other one the lab has been given, checked against the "
             "definition point by point. Replacing it with gift wrapping or with an incremental "
             "method changes nothing, because all of them are built on the same comparison. The "
             "experiment is designed to isolate this &mdash; two arms, one difference."),
            ("Expecting the drawing to show the problem",
             "On the needle triple the three points are collinear to well within a pixel, so "
             "both hulls look like a line segment. Every geometric defect on this course is a "
             "count or a set difference, never a shape that looks wrong. The page is built to "
             "show the numbers because the picture cannot."),
            ("Assuming a missing vertex is a small error",
             "It is not an error in a value, it is a change of answer. A diameter computed from "
             "the two-vertex hull is a real distance between two real points and simply not the "
             "largest; a point-in-polygon test against it will place points outside the shape "
             "that are inside it. Approximate inputs give approximate answers, but an incorrect "
             "predicate gives a confident answer to a different question."),
        ],
        "standard": ("Finish when you can point at the line of the monotone chain that a rounded determinant corrupts, and say what the corrupted output looks like.",
                     "You should be able to state the pop condition and why it uses `≤`, trace "
                     "both runs on the needle triple and name the step where they diverge, "
                     "explain why the wrong answer passes every structural check, and say which "
                     "defects the one-sidedness theorem permits and which it forbids."),
        "note": ("With the predicate settled, the rest of the course can take exactness for "
                 "granted and ask harder questions. &ldquo;The Convex Hull and Its "
                 "Definition&rdquo; starts that by asking what a hull actually IS, and by "
                 "checking the algorithm's answer against that definition rather than against "
                 "another algorithm."),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-convex-hull-and-its-definition",
        "title": "The Convex Hull and Its Definition",
        "module": "Convex hulls and degeneracy",
        "one_line": "Define a hull vertex without reference to any algorithm, then check two algorithms against that definition.",
        "summary": (
            "The convex hull is the smallest convex set containing the points, and its vertices "
            "are the points that cannot be written as combinations of the others. The lab "
            "computes that definition directly, by rotating a separating line about each point, "
            "and uses it as the referee for Andrew's monotone chain and for gift wrapping. On "
            "nine points in general position all three agree on the same four corners, and the "
            "two algorithms' costs do not resemble each other at all."
        ),
        "key": [
            "hull = the smallest convex set containing the points",
            "p is a vertex  iff  p is outside the convex hull of the other points",
            "nine points, four vertices, four boundary points: the sets coincide here",
            "monotone chain: sort, then 2n pushes and at most 2n pops",
            "gift wrapping: n work per vertex, so n·h in total",
            "measured on these nine points: 30 stack operations, and n·h = 36",
        ],
        "key_label": "One definition, two algorithms, and the work each one does",
        "concepts_intro": (
            "A definition that mentions no algorithm, a test that computes it directly, and two "
            "algorithms whose costs are quoted in different quantities."
        ),
        "concepts": [
            ("The hull is defined by containment, not by construction",
             "The convex hull of a finite point set is the smallest convex set that contains it "
             "&mdash; equivalently, the intersection of every half-plane containing all the "
             "points, or the set of all weighted averages of them. None of those mentions "
             "sorting, stacking or wrapping. A vertex is a point of the set that is not in the "
             "hull of the others, so removing it changes the hull and removing any other point "
             "does not."),
            ("A separating line is how you test the definition",
             "`p` is outside the hull of the others exactly when some line through `p` has all "
             "of them weakly on one side, with every point lying ON that line strictly beyond "
             "`p` along it. That second clause is what separates a corner from a point sitting "
             "in the middle of an edge. The lab tests it by taking the line through `p` and each "
             "other point in turn, which is enough: rotate a separating line about `p` until it "
             "first touches the set."),
            ("Two algorithms, costed in different quantities",
             "The monotone chain sorts and then makes a linear pass, so it costs `n log n` "
             "regardless of the answer. Gift wrapping walks from vertex to vertex, doing `n` "
             "work to find each one, so it costs `n·h` where `h` is the number of hull points "
             "&mdash; a quantity that is not known until the algorithm finishes. On these nine "
             "points the lab measures 36 comparisons for gift wrapping and prints `n log₂ n = 27` "
             "beside it for reference."),
        ],
        "read_title": "What a hull is, and how to check that you computed one",
        "read_intro": "Three equivalent definitions, the separating-line test, and the two algorithms measured against each other and against the definition.",
        "body": [
            ("def", ("The convex hull, and its vertices",
                     "The <strong>convex hull</strong> of a finite set `S` is the smallest "
                     "convex set containing `S`. Equivalently it is the intersection of all "
                     "half-planes containing `S`, and equivalently the set of all convex "
                     "combinations of points of `S`. A point `p ∈ S` is a <strong>vertex</strong> "
                     "of the hull when `p` is not in the convex hull of `S` minus `p`, and a "
                     "<strong>boundary point</strong> when `p` lies on the hull's boundary. Every "
                     "vertex is a boundary point; the converse fails exactly where three points "
                     "of `S` are collinear.")),
            ("p", "Those three descriptions are genuinely the same set, and it is worth knowing "
                  "which one to reach for. &ldquo;Smallest convex set&rdquo; is the one to use "
                  "when arguing that some construction returns the hull. &ldquo;Intersection of "
                  "half-planes&rdquo; is the one that turns into a separating-line test. "
                  "&ldquo;Convex combinations&rdquo; is the one that makes &ldquo;`p` is not a "
                  "vertex&rdquo; mean something concrete: `p` is an average of other points of "
                  "the set."),
            ("thm", ("The separating-line characterisation",
                     "Let `p ∈ S` and let `T = S` minus `p`. Then `p` is a hull vertex of `S` if "
                     "and only if there is a line through `p` such that every point of `T` lies "
                     "weakly on one side of it, and every point of `T` lying on the line lies "
                     "strictly beyond `p` along the line. Moreover, if such a line exists then "
                     "one exists that passes through `p` and some point of `T`.")),
            ("proof", ("If `p` is a vertex, then `p` is not in the convex hull of `T`, which is a "
                       "compact convex set, so by the separating hyperplane theorem there is a "
                       "line strictly separating `p` from it. Translate that line to pass "
                       "through `p`: every point of `T` is now strictly on one side, which is a "
                       "stronger condition than the statement requires.",
                       "Conversely, suppose such a line exists. Any convex combination of points "
                       "of `T` lies weakly on the chosen side, and if it equalled `p` then every "
                       "point with nonzero weight would have to lie on the line itself; but all "
                       "of those lie strictly beyond `p` along it, so their average does too and "
                       "cannot be `p`. Hence `p` is not in the hull of `T`.",
                       "For the last part, rotate the separating line about `p`. Since `T` is "
                       "finite, rotating until the line first meets a point of `T` preserves the "
                       "one-sidedness, and the point it meets satisfies the beyond-`p` clause "
                       "because it was strictly on one side before the rotation. So testing the "
                       "`n − 1` lines through `p` and each other point suffices, which is what "
                       "makes this a finite check.")),
            ("p", "That last paragraph is why the lab can compute the definition at all. A "
                  "quantifier over every line through `p` is not something a browser can "
                  "evaluate; a quantifier over the `n − 1` lines through `p` and another point "
                  "is a loop. The whole test is cubic in the number of points, which is "
                  "extravagant and exactly right for a referee: it shares no code, no data "
                  "structure and no idea with either algorithm it is judging."),
            ("example", ("Nine points, four corners",
                         "The lab opens on `(0, 0)`, `(6, 0)`, `(6, 6)`, `(0, 6)`, `(3, 3)`, "
                         "`(2, 1)`, `(4, 5)`, `(1, 4)`, `(5, 2)` &mdash; a square with five "
                         "points scattered inside it. The definition marks four of them as "
                         "vertices and four as boundary points, which is the same four: no "
                         "point of this set lies in the interior of a hull edge. The monotone "
                         "chain returns those four, gift wrapping returns those four, and the "
                         "table's four columns agree row by row.")),
            ("p", "One correction to make while looking at that input: these nine points are NOT "
                  "in general position, although both the worked example's own label and the "
                  "status line under the widget say they are. Four collinear triples exist among "
                  "them &mdash; `(0, 0)`, `(3, 3)`, `(6, 6)`, and three more through that same "
                  "centre point. What the page is entitled to say, and what actually matters "
                  "here, is narrower: none of those triples puts a point between two hull "
                  "vertices, so the boundary set and the vertex set coincide and the two "
                  "algorithms cannot be told apart on this input. Collinearity strictly inside "
                  "the hull is invisible to both of them."),
            ("h3", "The two algorithms cost different things"),
            ("p", "The chain's work is a sort plus a linear scan. The lab counts the scan: on "
                  "these nine points, 18 pushes and 12 pops, 30 stack operations in all. Each "
                  "chain pushes every point exactly once, so the two together push `2n = 18`, "
                  "and neither can pop more than it pushed, so the ceiling is `4n = 36`. The "
                  "sort is not counted here because Sorting and Selection already costed it."),
            ("p", "The widget's own stack figure reads &ldquo;18 + 12 = 30 against 2n = 18&rdquo;, "
                  "and the caption above its trace says the two chains cost `2n` stack "
                  "operations and no more. Take the `4n` in the previous paragraph instead: `2n` "
                  "is the number of PUSHES, since each chain pushes each point once, and the "
                  "pops are a second `2n` at worst. The measured 30 is genuinely below its "
                  "ceiling, and the ceiling is 36. A reference figure smaller than the "
                  "measurement beside it is always worth checking rather than believing, which "
                  "is the habit this whole path is trying to install."),
            ("p", "Gift wrapping does something quite different: from the current vertex it "
                  "scans all `n` points to find the next one, and repeats until it returns to "
                  "the start. Its work is therefore `n` per hull vertex. The lab reports 36 "
                  "comparisons on this input and prints `n·⌊log₂ n⌋ = 27` beside it as a "
                  "reference column. Here the output-sensitive algorithm is doing MORE work than "
                  "the sort-based bound, because `h = 4` is not small enough relative to "
                  "`log₂ 9` to pay for the difference."),
            ("h3", "Output-sensitive is a promise about `h`, not about this input"),
            ("p", "`n·h` beats `n log n` when `h` is smaller than `log n`, and on nine points "
                  "`log₂ 9` is about 3.17 while `h` is 4. So the reference column is larger "
                  "than the measured count, and the lesson is not that gift wrapping is a bad "
                  "algorithm: it is that its advantage is a claim about inputs whose hull is "
                  "tiny relative to their size, and this input is not one of them. Type a "
                  "thousand points inside a triangle and the ratio inverts."),
            ("p", "This is the shape every page on this path takes. The measured number and the "
                  "bound sit in the same row, they disagree, and the disagreement is explained "
                  "rather than hidden. The reference column carries no verdict and the page says "
                  "so: it is a drawing of a function, evaluated at the `n` on screen. It is not "
                  "hard to make the comparison go the other way either &mdash; 24 points with "
                  "only three on the hull give `n·h = 72` against the same reference at 96."),
            ("p", "One last thing to type into the box, because it is why Sorting and Selection "
                  "is a prerequisite for this course. Enter `5, 25; 1, 1; 9, 81; 3, 9; 7, 49`, "
                  "which is the numbers 5, 1, 9, 3, 7 each lifted to `(x, x²)`. All five come "
                  "back as hull vertices, and the lower chain reads `(1, 1)`, `(3, 9)`, "
                  "`(5, 25)`, `(7, 49)`, `(9, 81)` &mdash; the inputs in sorted order. Any hull "
                  "algorithm therefore sorts, so the comparison lower bound proved there applies "
                  "here unchanged, and the monotone chain's `n log n` is not an implementation "
                  "choice a cleverer method could avoid."),
        ],
        "lab": ("geometry", {
            "mode": "hull",
            "preset": "general",
            "panel_title": "Nine points, and three independent answers about each one",
            "panel_intro": "Every point is classified from the definition before either "
                           "algorithm runs, by rotating a separating line about it &mdash; no "
                           "sort, no stack, nothing shared with the algorithms it referees. The "
                           "table then reports, for each point, what the definition says and "
                           "which of the three runs put it on the hull.",
        }),
        "steps_title": "Establishing that a hull is the hull",
        "steps_intro": "Answer the definition's question about each point, then compare with whatever the algorithm returned.",
        "steps": [
            ("Deduplicate first, and count what you removed",
             "Both hull algorithms misbehave on a repeated point: the chain can return it twice "
             "and gift wrapping does. The lab removes duplicates before anything else and "
             "reports how many, because that count is information about the input and not an "
             "implementation detail to hide."),
            ("Ask the definition about each point separately",
             "For each `p`, look for a line through `p` and one other point with everything else "
             "weakly on one side. If you find one, and every point on that line is beyond `p`, "
             "then `p` is a corner. This is slow and it is not how you would compute a hull; it "
             "is how you check one."),
            ("Compare the sets, not the counts",
             "Two answers of the same size can still be different sets. The lab compares the "
             "sorted keys of the two point lists, and the per-point table shows which run "
             "included which point, so a swap of one vertex for another is visible rather than "
             "hidden behind a matching total."),
            ("Read the cost columns as measurements of this input",
             "The stack count and the gift-wrapping work are counts on the points on screen. "
             "Change the input and both move; change it so that everything is inside a triangle "
             "and they move in opposite directions. Neither number is a bound and the page never "
             "calls one."),
        ],
        "worked": {
            "title": "The definition applied to all nine points, by hand",
            "intro": [
                "The points are `(0, 0)`, `(6, 0)`, `(6, 6)`, `(0, 6)`, `(3, 3)`, `(2, 1)`, "
                "`(4, 5)`, `(1, 4)`, `(5, 2)`. For each one, look for a line through it with "
                "everything else on one side.",
            ],
            "lines": [
                "point      a separating line through it        verdict",
                "(0, 0)     through (6, 0):  all others y ≥ 0    VERTEX",
                "(6, 0)     through (6, 6):  all others x ≤ 6    VERTEX",
                "(6, 6)     through (0, 6):  all others y ≤ 6    VERTEX",
                "(0, 6)     through (0, 0):  all others x ≥ 0    VERTEX",
                "(3, 3)     none: it is the centre               inside",
                "(2, 1)     none                                 inside",
                "(4, 5)     none                                 inside",
                "(1, 4)     none                                 inside",
                "(5, 2)     none                                 inside",
                "",
                "vertices by definition      4",
                "boundary points by definition  4      (the same four)",
                "monotone chain              4      (0,0) (6,0) (6,6) (0,6)",
                "gift wrapping               4      the same four",
                "stack operations            18 pushes + 12 pops = 30,  ceiling 4n = 36",
                "gift wrapping comparisons   36,  reference column n·log2 n = 27",
            ],
            "after": [
                "The four interior points are interior for different reasons, and it is worth "
                "seeing that the test does not care. `(3, 3)` is the centre and lies on two "
                "diagonals; `(2, 1)` is near an edge; `(4, 5)` is near a corner. Every line "
                "through any of them has points of the set strictly on both sides, and that is "
                "the whole verdict.",
                "The two cost figures are the interesting part of this table. The chain's 30 "
                "stack operations are a count of work it actually did; the 36 gift-wrapping "
                "comparisons are the same; and the 27 beside them is `n` times the integer part "
                "of `log₂ n`, which is a function evaluated at `n = 9` and not a measurement of "
                "anything. Reading &ldquo;36 against 27&rdquo; as &ldquo;gift wrapping is 33 per "
                "cent worse&rdquo; would be comparing a count with a drawing.",
                "For a faded rehearsal, delete `(3, 3)` and predict every figure in the table "
                "before rerunning. The supplied first move is that the four corners are "
                "unaffected: `(3, 3)` is in the hull of the others, so removing it cannot change "
                "which points are vertices. Say what happens to the 18, the 12 and the 36, and "
                "then say why one of those three does not move in proportion to the other two.",
            ],
        },
        "quiz_title": "Definitions, referees, and costs",
        "quiz": [
            {"q": "A point set has 20 points, 5 of which are hull vertices. You remove one vertex. What happens to the hull?",
             "a": ["Nothing, since the remaining points still span the same region",
                   "It shrinks, because a vertex is by definition not in the hull of the others",
                   "It shrinks only if that vertex was on the boundary",
                   "It may grow, since the algorithm will find different corners"],
             "c": 1,
             "why": "That is exactly the definition: `p` is a vertex when `p` is not in the "
                    "convex hull of the rest, so the hull of the rest is strictly smaller. "
                    "Removing a non-vertex leaves the hull unchanged, which is the same "
                    "statement from the other side."},
            {"q": "Why does the lab compute the definition by brute force when it already has two hull algorithms?",
             "a": ["To make the page slower and therefore more convincing",
                   "Because a third algorithm would be a third chance to make the same mistake, and the definition shares no code, no sort and no stack with either",
                   "Because brute force is faster on small inputs",
                   "Because the two algorithms return different answers"],
             "c": 1,
             "why": "A check is only worth running if it can fail independently. The "
                    "separating-line test rotates a line about each point in turn; it has no "
                    "sort, no stack and no incremental step, so an error in the chain's pop "
                    "condition or in gift wrapping's tie-break cannot be replicated in it. Cost "
                    "is not the point &mdash; it is cubic and deliberately so."},
            {"q": "On these nine points gift wrapping does 36 comparisons and the reference column reads 27. What is the honest reading?",
             "a": ["Gift wrapping is 33 per cent slower than the monotone chain on this input",
                   "The measured count exceeds a reference value because `h = 4` is not small relative to `log₂ 9`; the reference is a function evaluated at `n`, not a measurement",
                   "The monotone chain would do 27 comparisons here",
                   "The reference column is wrong"],
             "c": 1,
             "why": "36 is a count of comparisons gift wrapping made. 27 is `n·⌊log₂ n⌋`, which "
                    "is not a measurement of anything on this page and certainly not the "
                    "monotone chain's comparison count. Putting them in one row shows where the "
                    "output-sensitive promise does and does not pay, and the page labels the "
                    "reference column as carrying no verdict."},
        ],
        "mistakes": [
            ("Defining the hull by the algorithm that computes it",
             "&ldquo;The hull is what the monotone chain returns&rdquo; makes the correctness "
             "question unaskable and makes the previous lesson's failure undetectable. The "
             "definition has to come from containment, and then the algorithm is a claim about "
             "it &mdash; a claim this page checks point by point on whatever you type."),
            ("Assuming a point set with collinear triples is degenerate for hull purposes",
             "The nine points here contain four collinear triples and both algorithms still "
             "agree, because every one of those triples lies strictly inside the hull. What "
             "makes an input degenerate for a hull is collinearity ON THE BOUNDARY, which is a "
             "much narrower condition. The following lesson constructs one on purpose."),
            ("Reading an output-sensitive bound as a promise about your input",
             "`n·h` is smaller than `n log n` only when `h &lt; log n`, and nothing guarantees "
             "that. On nine points with four on the hull it is larger, measurably, on the page. "
             "The right question is never &ldquo;which algorithm is faster&rdquo; but "
             "&ldquo;what is `h` on the inputs I actually have&rdquo;, and that is a fact about "
             "the data rather than about the algorithm."),
        ],
        "standard": ("Finish when you can state what a hull vertex is without naming an algorithm, and check a computed hull against that statement.",
                     "You should be able to give the three equivalent definitions and say which "
                     "is useful for what, prove or reconstruct the separating-line "
                     "characterisation including why lines through pairs suffice, and read the "
                     "two cost columns as a measurement and a reference respectively."),
        "note": ("On this input the boundary and the vertex set are the same four points, so the "
                 "two algorithms cannot be told apart. &ldquo;Three Right Answers on a Square "
                 "with Midpoints&rdquo; makes them different on purpose, and gets three "
                 "different counts from three procedures that are all correct."),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "three-answers-on-a-square-with-midpoints",
        "title": "Three Right Answers on a Square with Midpoints",
        "module": "Convex hulls and degeneracy",
        "one_line": "Put a point in the middle of each side of a square and three correct procedures return 4, 6 and 8.",
        "summary": (
            "A collinear point on the boundary is not an edge case to exclude; it is a question "
            "about what you meant by &ldquo;the hull&rdquo;. The monotone chain returns the four "
            "corners, the boundary oracle returns all eight boundary points, and gift wrapping "
            "returns six &mdash; two of the four midpoints and not the other two, because its "
            "tie-break is the order the points were sorted in. None of the three is a bug, and "
            "only one of them is a vertex list."
        ),
        "key": [
            "square plus a midpoint per side: 9 points typed, 9 distinct",
            "monotone chain 4      the vertices",
            "boundary oracle 8      every point on the boundary",
            "gift wrapping 6      a boundary walk whose tie-break is the sort order",
            "gift wrapping keeps (2, 0) and (4, 2); it drops (2, 4) and (0, 2)",
            "duplicates are removed and counted before any of the three runs",
        ],
        "key_label": "Nine points, three procedures, and three different counts",
        "concepts_intro": (
            "Two questions that sound like one, a third procedure that answers neither exactly, "
            "and the reason a course should show all three rather than pick one."
        ),
        "concepts": [
            ("Vertex and boundary are different questions",
             "A point is a boundary point when some line through it has every other point on one "
             "side. It is a vertex when, in addition, every point ON that line is strictly "
             "beyond it. A midpoint of a side satisfies the first and fails the second: the line "
             "along that side has everything on one side of it, but the two corners of the side "
             "lie on the line in opposite directions. So the midpoint is on the boundary and is "
             "not a corner, and on this input there are four such points."),
            ("Gift wrapping walks the boundary, and its tie-break decides what it reports",
             "Wrapping repeatedly asks &ldquo;which point makes the most clockwise turn from "
             "here&rdquo;. When several points are collinear with the current one, they all give "
             "the same determinant, and which of them is chosen is decided by the order the scan "
             "happens to reach them &mdash; here, the lexicographic sort order. On this square "
             "that keeps `(2, 0)` and `(4, 2)` and drops `(2, 4)` and `(0, 2)`. The result is a "
             "correct boundary walk and an arbitrary subset of the collinear boundary points."),
            ("Deduplication is the lesson, not the workaround",
             "A point typed twice breaks both algorithms: the chain can return it twice and gift "
             "wrapping does. The lab removes duplicates first and reports the count, and that "
             "count is a genuine fact about the input. Hiding it would make the two algorithms "
             "look robust on an input they are not robust on."),
        ],
        "read_title": "One input, three procedures, and what each one is answering",
        "read_intro": "The two definitions, the wrapping tie-break, the counts the lab measures, and why the disagreement is pinned rather than fixed.",
        "body": [
            ("def", ("Boundary point and vertex, side by side",
                     "For a finite set `S` and `p ∈ S`, say `p` is a <strong>boundary "
                     "point</strong> when some line through `p` has every point of `S` weakly on "
                     "one side, and a <strong>vertex</strong> when in addition every point of "
                     "`S` lying on that line lies strictly beyond `p` along it. Vertices are "
                     "boundary points. The two sets differ exactly at points lying in the "
                     "relative interior of a hull edge.")),
            ("p", "Both questions are legitimate and different consumers want different answers. "
                  "A renderer drawing the hull wants the vertices, because a polygon with a "
                  "redundant collinear vertex draws the same shape and costs more. A "
                  "point-location structure may want every boundary point. A convex-position "
                  "test wants to know whether the two sets are equal to the whole input. The "
                  "error is not choosing one; it is not saying which you chose."),
            ("example", ("The square with a midpoint on each side",
                         "Type `(0, 0)`, `(2, 0)`, `(4, 0)`, `(4, 2)`, `(4, 4)`, `(2, 4)`, "
                         "`(0, 4)`, `(0, 2)`, `(2, 2)`: the four corners of a square of side 4, "
                         "the midpoint of each side, and the centre. The lab reports 4 hull "
                         "vertices, 8 boundary points, and 6 from gift wrapping. The centre is "
                         "the only point of the nine that is neither a vertex nor on the "
                         "boundary.")),
            ("p", "Read the per-point table and the shape of the disagreement is immediate. The "
                  "four corners are marked as vertices and appear in all three runs. The four "
                  "midpoints are marked as being on an edge; the chain excludes all four; and "
                  "gift wrapping includes `(2, 0)` and `(4, 2)` while excluding `(2, 4)` and "
                  "`(0, 2)`. Nothing geometric distinguishes the two pairs. The wrapping walk "
                  "starts at the lexicographically smallest point and goes round one way, and "
                  "the collinear ties resolve in the scan's favour on the first two sides and "
                  "against it on the last two."),
            ("thm", ("Where the two sets coincide",
                     "The vertex set and the boundary set of a finite point set `S` are equal if "
                     "and only if no point of `S` lies in the relative interior of a segment "
                     "joining two other points of `S` that both lie on the hull boundary. In "
                     "particular, if no three points of `S` are collinear the two sets are "
                     "equal.")),
            ("proof", ("A vertex is always a boundary point, so only one inclusion is at issue. "
                       "Suppose `p` is on the boundary but not a vertex. Then `p` lies in the "
                       "hull of the others, and since it is on the boundary it lies on some hull "
                       "edge; being in the hull of the others and on that edge, it lies in the "
                       "relative interior of the segment between the edge's two endpoints, both "
                       "of which are on the boundary.",
                       "Conversely, if `p` lies strictly between two boundary points `u` and "
                       "`v`, then `p` is a convex combination of `u` and `v` and so is in the "
                       "hull of the others, hence not a vertex &mdash; and it is on the boundary "
                       "because the segment `uv` lies in the hull and its endpoints do not "
                       "permit `p` to be interior. The collinearity condition is necessary "
                       "rather than sufficient on its own, which is exactly the case the "
                       "previous lesson's nine points illustrate: they contain collinear triples "
                       "and the two sets still coincide, because those triples are interior.")),
            ("h3", "The two shipped algorithms are pinned against each other, on purpose"),
            ("p", "The gift-wrapping routine this course runs is a boundary walk, not a vertex "
                  "list, and its tie-break is the sort order rather than a geometric decision. "
                  "That is a real property of the implementation and the lab labels it as one: "
                  "the mode checks gift wrapping against the boundary oracle rather than against "
                  "the vertex set, and asserts only that every point it returns is on the "
                  "boundary. The disagreement with the chain is recorded rather than smoothed "
                  "over, so an upstream change that altered either one would fail loudly instead "
                  "of quietly changing what this page teaches."),
            ("p", "This is a deliberate editorial choice and it is the right one for a course "
                  "about degeneracy. Making the wrapping return all eight, or exactly four, "
                  "would remove the most instructive input on the page. What matters is that the "
                  "page never calls its six the hull's vertex count, and never calls the chain's "
                  "four the boundary."),
            ("h3", "The hull that is a segment, and the hull that is a point"),
            ("p", "Push the degeneracy further. Five collinear points have a hull that is a "
                  "segment: the chain returns the two ends, the boundary oracle returns all "
                  "five, and gift wrapping returns all five. A single point, typed twice, has a "
                  "hull that is that point; the deduplication reports one duplicate removed and "
                  "the chain returns the one point. Both of those are in the preset list, and "
                  "both are answers rather than errors."),
            ("p", "The shipped monotone chain in the shared algorithm library returns an EMPTY "
                  "hull for a single point, because the lower and upper chains are both that "
                  "point and both are sliced away when they are concatenated. The hull of one "
                  "point is that point, so that is a defect; the geometry kit works around it "
                  "with its own predicate-parameterised chain, and the arithmetic checker pins "
                  "the disagreement so that a fix upstream cannot land silently. It is recorded "
                  "here because a reader who runs the library routine directly will see the "
                  "empty answer and should know why."),
        ],
        "lab": ("geometry", {
            "mode": "hull",
            "preset": "edges",
            "panel_title": "Four, six and eight, on the same nine points",
            "panel_intro": "Switch the algorithm control between the chain and gift wrapping and "
                           "watch the drawn polygon change while the point colours do not: the "
                           "colours come from the definition and the polygon comes from whichever "
                           "algorithm you asked for. The per-point table is where the two "
                           "midpoints gift wrapping keeps and the two it drops are visible.",
        }),
        "steps_title": "Handling a collinear boundary without excluding it",
        "steps_intro": "Decide which question you are asking before you compare two answers.",
        "steps": [
            ("Deduplicate, and keep the count",
             "Do it before anything else and report how many were removed. Both hull algorithms "
             "return a repeated point when handed one, so this is not tidying &mdash; it is a "
             "precondition, and the count belongs on the page next to the answer."),
            ("Decide between vertices and boundary points explicitly",
             "Write down which one the consumer needs. A renderer wants vertices; a "
             "point-location structure may want the boundary. Two correct procedures answering "
             "different questions will disagree, and the disagreement is not evidence that "
             "either is broken."),
            ("Find out what your wrapping implementation does with ties",
             "Ask it for the hull of a square with a midpoint on each side. If it returns six, "
             "its tie-break is decided by scan order and its output is a boundary walk. If it "
             "returns four or eight, it has made a deliberate choice. Whatever the answer, you "
             "now know it rather than assuming it."),
            ("Check against the definition rather than against a second algorithm",
             "Two algorithms agreeing is weak evidence when they share a convention about "
             "collinear points, and no evidence at all when they share code. The "
             "separating-line test answers the question directly and cannot share a convention "
             "with anything, because it has no incremental step in which to hold one."),
        ],
        "worked": {
            "title": "All nine points, and what each of the three runs says",
            "intro": [
                "The square is `(0, 0)`, `(4, 0)`, `(4, 4)`, `(0, 4)`; the midpoints are "
                "`(2, 0)`, `(4, 2)`, `(2, 4)`, `(0, 2)`; and `(2, 2)` is the centre.",
            ],
            "lines": [
                "point     definition      chain   wrapping   boundary oracle",
                "(0, 0)    vertex          yes     yes        yes",
                "(2, 0)    on an edge      no      yes        yes",
                "(4, 0)    vertex          yes     yes        yes",
                "(4, 2)    on an edge      no      yes        yes",
                "(4, 4)    vertex          yes     yes        yes",
                "(2, 4)    on an edge      no      no         yes",
                "(0, 4)    vertex          yes     yes        yes",
                "(0, 2)    on an edge      no      no         yes",
                "(2, 2)    inside          no      no         no",
                "",
                "totals                     4       6          8",
                "",
                "the wrapping walk, in order:",
                "  (0, 0) -> (2, 0) -> (4, 0) -> (4, 2) -> (4, 4) -> (0, 4) -> back to (0, 0)",
            ],
            "after": [
                "The walk is the explanation. Wrapping starts at `(0, 0)`, the lexicographically "
                "smallest point, and looks for the point that turns furthest clockwise. Along "
                "the bottom edge, `(2, 0)` and `(4, 0)` are tied at determinant zero, and the "
                "scan's comparison keeps whichever it reached in a position it cannot improve "
                "on, which here is `(2, 0)`. The same thing happens at `(4, 2)`. On the way back "
                "along the top and down the left side the ties resolve the other way, so "
                "`(2, 4)` and `(0, 2)` are skipped.",
                "Nothing geometric distinguishes those two pairs from the other two, and here is "
                "the argument that settles it. Reflecting the whole input in the line `y = x` "
                "maps this point set onto ITSELF &mdash; it swaps `(2, 0)` with `(0, 2)` and "
                "`(4, 2)` with `(2, 4)` and fixes the rest. So the reflection is a symmetry of "
                "the input, and any answer determined by the geometry alone would have to be "
                "carried onto itself by it. Reflecting the six points the wrapping returned "
                "gives `(0, 0)`, `(0, 2)`, `(0, 4)`, `(2, 4)`, `(4, 4)`, `(4, 0)`, which is a "
                "different set. The output is therefore not decided by the geometry, and the "
                "only other thing in the algorithm is the order the scan walks in.",
                "For a faded rehearsal, predict the three counts for the same square with "
                "midpoints but WITHOUT the centre point &mdash; eight points instead of nine. "
                "The supplied first move is that the centre is neither a vertex nor a boundary "
                "point, so removing it cannot change any of the three sets. Say what the three "
                "counts become, then say what happens to the 18 pushes and 12 pops, which do "
                "change.",
            ],
        },
        "quiz_title": "Three answers, and the question each one answers",
        "quiz": [
            {"q": "The chain returns 4, the boundary oracle returns 8, and gift wrapping returns 6. Which is the convex hull?",
             "a": ["The chain's 4, since a hull is a polygon and a polygon has vertices",
                   "The oracle's 8, since all eight are on the hull",
                   "All three describe the same hull; they report different things about it, and only the chain reports its vertex set",
                   "Gift wrapping's 6, since it is between the two"],
             "c": 2,
             "why": "The hull is one region, and all three procedures agree about the region: a "
                    "square of side 4. What differs is which points of the input they list. The "
                    "chain lists the vertices, the oracle lists the boundary points, and gift "
                    "wrapping lists a subset of the boundary chosen by its tie-break. The fourth "
                    "option is the tempting one and it is meaningless &mdash; there is no sense "
                    "in which an answer is right for being in the middle."},
            {"q": "Gift wrapping keeps `(2, 0)` and `(4, 2)` and drops `(2, 4)` and `(0, 2)`. What does that asymmetry indicate?",
             "a": ["A bug in the determinant, since the four midpoints are geometrically equivalent",
                   "That collinear ties are resolved by the order the points were sorted in, which is a property of the implementation rather than of the geometry",
                   "That the two dropped points are inside the hull",
                   "That the walk went round the wrong way"],
             "c": 1,
             "why": "The four midpoints are geometrically interchangeable, so an answer that "
                    "distinguishes them must be using something other than geometry &mdash; here "
                    "the lexicographic order the scan walks in. The determinant is exact and "
                    "correct; all four ties really are ties. That is why the page checks gift "
                    "wrapping against the boundary rather than against the vertex set."},
            {"q": "You need a hull for a renderer that will fill the polygon. Which answer do you want, and why?",
             "a": ["The boundary, so no information is lost",
                   "The vertices, because collinear boundary points add vertices that draw the same shape and cost more",
                   "Whatever gift wrapping returns, since it is the standard algorithm",
                   "It does not matter, because all three draw the same shape"],
             "c": 1,
             "why": "All three do draw the same shape, which is why the last option is tempting; "
                    "but the vertex list is strictly smaller and carries the same information, "
                    "so the redundant points are pure cost. The point of the lesson is that this "
                    "is a decision about the consumer, made deliberately, rather than a fact "
                    "about which algorithm is correct."},
        ],
        "mistakes": [
            ("Calling a disagreement about collinear points a bug",
             "Three procedures returning 4, 6 and 8 on the same input looks like two of them are "
             "broken, and none of them is. Before reaching for a fix, ask what each one was "
             "computing; on this input the answer is three different things, and the lab labels "
             "each column with which."),
            ("Perturbing the input to make the degeneracy go away",
             "Nudging a midpoint by one unit does make all three agree, and it also answers a "
             "question about a different point set. Real inputs are full of collinear points "
             "&mdash; grids, rectilinear layouts, anything snapped to a lattice &mdash; and a "
             "procedure that only works once you have jittered the data is a procedure that does "
             "not work."),
            ("Treating a repeated point as harmless",
             "Both algorithms return a duplicated point when handed one, so the answer is not a "
             "set. The lab deduplicates first and reports the count, and the reason the count is "
             "shown rather than hidden is that it changes what `n` means in every cost figure "
             "below it."),
        ],
        "standard": ("Finish when you can predict all three counts on a degenerate input and say, for each one, which question it answers.",
                     "You should be able to state the vertex and boundary definitions and the "
                     "condition under which they coincide, explain why a collinear tie-break "
                     "makes gift wrapping's output implementation-defined, and say what "
                     "deduplication changes and why its count is published."),
        "note": ("A hull is rarely the end of a computation; it is what makes the next one cheap. "
                 "&ldquo;The Two Furthest Points&rdquo; uses it that way, walking the hull once "
                 "to find the diameter of the whole set and then checking that answer against "
                 "every pair of input points."),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-two-furthest-points",
        "title": "The Two Furthest Points",
        "module": "Convex hulls and degeneracy",
        "one_line": "The diameter of a set is the diameter of its hull, so a walk over h antipodal pairs replaces a scan over all of them.",
        "summary": (
            "The two furthest-apart points of a set are both hull vertices, so the sixteen-point "
            "cloud in the lab reduces to a four-vertex square before anything is measured. The "
            "rotating calipers then walk the hull once and examine only antipodal pairs &mdash; "
            "four of them here, against 120 pairs of points. The answer is a squared distance, "
            "which is an integer, and two different pairs attain it."
        ),
        "key": [
            "the diameter of a set is the diameter of its convex hull",
            "sixteen points, four on the hull, twelve interior and free",
            "4 antipodal pairs examined against 120 pairs of points",
            "squared diameter 225, attained by two different pairs",
            "distances stay squared: comparing squares orders pairs the same way",
            "h is a property of this input, not a bound: on a circle h is n",
        ],
        "key_label": "Sixteen points, four hull vertices, four pairs examined",
        "concepts_intro": (
            "One reduction, one walk, and one honest remark about what the saving depends on."
        ),
        "concepts": [
            ("The furthest pair is a pair of hull vertices",
             "If `q` is strictly inside the hull then it is a convex combination of hull "
             "vertices, and for any other point `r` at least one of those vertices is at least "
             "as far from `r` as `q` is. So no interior point can be an endpoint of the longest "
             "segment, and the diameter of the set is the diameter of its hull. On the lab's "
             "sixteen-point cloud that discards twelve points before any distance is computed."),
            ("Antipodal pairs are the only candidates",
             "A pair of hull vertices can be the diameter only if they admit parallel supporting "
             "lines &mdash; if you can lay a ruler against the hull at each of them with the two "
             "rulers parallel. Such a pair is called antipodal. Walking two indices round the "
             "hull in step enumerates all of them in linear time, and there are `O(h)` of them "
             "rather than `h(h − 1)/2`. The lab reports 4 on the cloud, against 120 pairs of "
             "input points."),
            ("Squared distances, and what a tie means",
             "No square root is taken anywhere. The squared distance between lattice points is "
             "an integer, comparing squared distances orders pairs exactly as comparing "
             "distances does, and so the comparison that picks the winner never rounds. On the "
             "cloud the squared diameter is 225 and two different pairs attain it, so the "
             "ANSWER is a value and the pair printed is one of several &mdash; a distinction the "
             "page makes explicitly rather than leaving to the reader."),
        ],
        "read_title": "From the whole set to the hull, and from the hull to h pairs",
        "read_intro": "The reduction, the antipodal characterisation, the measured counts, and the input where the saving vanishes.",
        "body": [
            ("def", ("Diameter, and antipodal pairs",
                     "The <strong>diameter</strong> of a finite set is the largest distance "
                     "between two of its points. Two points `u`, `v` of a convex polygon are an "
                     "<strong>antipodal pair</strong> when there exist parallel supporting lines "
                     "of the polygon, one through `u` and one through `v` &mdash; that is, lines "
                     "touching the polygon with the whole polygon on one side of each.")),
            ("thm", ("The diameter is attained by an antipodal pair of hull vertices",
                     "Let `S` be a finite set with at least two points and let `u`, `v` attain "
                     "its diameter. Then `u` and `v` are both vertices of the convex hull of "
                     "`S`, and they are an antipodal pair of that hull.")),
            ("proof", ("Suppose `u` is not a hull vertex. Then `u` is a convex combination "
                       "`Σ λᵢ pᵢ` of other points. The function `x ↦ |x − v|` is convex, so "
                       "`|u − v| ≤ Σ λᵢ |pᵢ − v|`, and therefore some `pᵢ` is at least as far "
                       "from `v` as `u` is. That `pᵢ` is a different point, so the pair "
                       "`(pᵢ, v)` also attains the diameter, and repeating the argument reaches "
                       "a hull vertex. The same runs for `v`.",
                       "For antipodality, let `ℓᵤ` be the line through `u` perpendicular to the "
                       "segment `uv`, and `ℓᵥ` the line through `v` perpendicular to it. These "
                       "are parallel. If some point `w` of `S` lay strictly on the far side of "
                       "`ℓᵤ` from `v`, then `|w − v|` would exceed `|u − v|`, contradicting the "
                       "diameter; so everything is weakly on one side of `ℓᵤ`, and likewise for "
                       "`ℓᵥ`. Both are therefore supporting lines, and `u`, `v` are antipodal.")),
            ("p", "That proof is the whole justification for the algorithm and it is worth "
                  "noticing what it does NOT say. It does not say every antipodal pair is a "
                  "candidate worth examining because it is nearly the diameter; it says the "
                  "diameter is among them, so examining all of them suffices. The calipers are "
                  "an exhaustive search over a set that has been proved to contain the answer, "
                  "which is why they can be confident rather than heuristic."),
            ("example", ("Sixteen points, four on the hull, four pairs",
                         "The lab's cloud is the four corners of a 12-by-9 rectangle plus twelve "
                         "points scattered inside it. The hull is the rectangle, `h = 4`, and "
                         "the calipers examine 4 antipodal pairs. The squared diameter is 225, "
                         "between `(0, 0)` and `(12, 9)` &mdash; and also between `(12, 0)` and "
                         "`(0, 9)`, since `12² + 9² = 225` either way. Testing all "
                         "`16·15/2 = 120` pairs of input points returns the same value.")),
            ("p", "The two figures to hold on to are 4 and 120. The brute force is run on every "
                  "redraw, on the same points, because an algorithm that visits the wrong pairs "
                  "returns a distance that is real and simply not the largest &mdash; there is "
                  "no internal inconsistency for it to trip over. As with the hull, the check is "
                  "a different computation and not a second opinion from the same one."),
            ("h3", "Twelve interior points cost nothing, and that is the whole saving"),
            ("p", "Once the hull is built, the twelve interior points are never looked at again. "
                  "That is where the reduction from 120 to 4 comes from, and it is worth being "
                  "precise that the hull itself was not free: it cost a sort. The honest "
                  "statement is that the diameter of `n` points costs a hull plus `O(h)`, which "
                  "is `O(n log n)` in total, against `O(n²)` for the scan. On sixteen points "
                  "neither of those constants means much, and the page prints counts rather than "
                  "claiming a speed."),
            ("h3", "The input where `h` is `n`"),
            ("p", "Take eight points in convex position &mdash; the lab has one such preset "
                  "&mdash; and every point is a hull vertex. The hull has bought nothing, the "
                  "calipers walk the whole input, and the antipodal-pair count is 8 against 28 "
                  "pairs of points. The saving is smaller and still real. Now imagine `n` points "
                  "on a circle: `h = n`, the hull costs a sort and discards nothing, and the "
                  "calipers' linear walk is linear in `n` rather than in something smaller."),
            ("p", "So `h` is a property of the input, not a bound on it. The lab says this "
                  "directly in its status line, and it is the geometry version of the one thing "
                  "this whole path keeps insisting on: the count you just watched is a "
                  "measurement of the points on screen. `4` and `120` are true about this cloud. "
                  "`O(n log n)` is the claim about every input, and it is proved by the hull "
                  "bound and the linear walk rather than by either number."),
        ],
        "lab": ("geometry", {
            "mode": "calipers",
            "preset": "cloud",
            "panel_title": "Sixteen points, four on the hull, and the pairs the walk examined",
            "panel_intro": "The hull is drawn in outline and the diameter heavy. Every pair of "
                           "input points is tested separately on each redraw, so the squared "
                           "diameter is checked against a route that knows nothing about hulls "
                           "or antipodality. Switch to the convex-position example and watch the "
                           "hull stop discarding anything.",
        }),
        "steps_title": "Finding a diameter without measuring every pair",
        "steps_intro": "Reduce to the hull, walk the hull, and keep everything squared.",
        "steps": [
            ("Take the hull first and discard the interior",
             "The proof licenses this completely: no interior point can be an endpoint of the "
             "longest segment. The lab reports how many points the hull kept, and on the cloud "
             "that is 4 of 16."),
            ("Walk two indices round the hull in step",
             "Advance the second index while it keeps moving away from the current edge, then "
             "advance the first. Each index goes round once, so the walk is linear in `h` and "
             "enumerates the antipodal pairs without ever forming a pair twice."),
            ("Compare squared distances and never take a root",
             "Squared lattice distances are integers, and `a &lt; b` for nonnegative reals is "
             "the same as `a² &lt; b²`. So the comparison that decides the winner is an integer "
             "comparison, exactly as the orientation tests elsewhere are."),
            ("Report ties as ties",
             "On the cloud two pairs attain 225, and on the square in the preset list two "
             "diagonals attain 72. The diameter is a value; the pair is one witness among "
             "possibly several, and a page that prints one pair without saying so invites a "
             "reader to think it is the pair."),
        ],
        "worked": {
            "title": "The cloud, from sixteen points down to four pairs",
            "intro": [
                "The four corners are `(0, 0)`, `(12, 0)`, `(12, 9)` and `(0, 9)`; the other "
                "twelve points are inside the rectangle.",
            ],
            "lines": [
                "n = 16 distinct points          hull vertices h = 4",
                "hull:  (0, 0)  (12, 0)  (12, 9)  (0, 9)",
                "",
                "antipodal pairs examined:",
                "  1   (0, 0)  -  (12, 9)      squared distance 225   <- diameter",
                "  2   (12, 0) -  (0, 9)       squared distance 225   <- diameter",
                "  3   (12, 9) -  (0, 0)       squared distance 225",
                "  4   (0, 9)  -  (12, 0)      squared distance 225",
                "",
                "pairs examined                4",
                "pairs of input points         16·15/2 = 120",
                "squared diameter, calipers    225",
                "squared diameter, every pair  225",
                "pairs of points attaining it  2",
            ],
            "after": [
                "The rectangle is 12 by 9, so both diagonals have squared length "
                "`144 + 81 = 225` and actual length 15. Two genuinely different pairs are at the "
                "diameter, and the calipers happen to visit each of them twice as the walk goes "
                "round. The page reports the value as the answer and names one pair as a "
                "witness.",
                "Twelve of the sixteen points appear nowhere in this table, and that is the "
                "entire content of the reduction. They were used once, to build the hull, and "
                "then discarded on the strength of a proof rather than of a heuristic. Note that "
                "225 is exact: no square root was taken, and the number 15 appears only in this "
                "paragraph, as a remark.",
                "For a faded rehearsal, predict what the table becomes if you move `(0, 0)` to "
                "`(0, 3)`, so that the hull is a pentagon rather than a rectangle. The supplied "
                "first move is that `h` rises and so does the antipodal-pair count; the squared "
                "diameter, however, is now `12² + 9² = 225` between `(12, 0)` and `(0, 9)` "
                "alone. Say how many pairs attain it, and check whether the number of pairs of "
                "input points changed at all.",
            ],
        },
        "quiz_title": "Reductions, candidates, and what h is",
        "quiz": [
            {"q": "Why can the twelve interior points be discarded before any distance is measured?",
             "a": ["Because they are closer to the centre, and the diameter is about extremes",
                   "Because distance is a convex function, so an interior point is never further from anything than some hull vertex is",
                   "Because the algorithm would be too slow otherwise",
                   "Because they were not typed first"],
             "c": 1,
             "why": "The argument is the convexity of `x ↦ |x − v|`: an interior point is a "
                    "convex combination of hull vertices, so its distance to any `v` is at most "
                    "the largest of theirs. That licenses the discard for every input, not just "
                    "this one, which is why it is a proof rather than an optimisation."},
            {"q": "The lab reports 4 antipodal pairs against 120 pairs of points. What is the honest generalisation?",
             "a": ["That the calipers are 30 times faster than the brute force",
                   "That the calipers examine `O(h)` pairs, and on this input `h` is 4; on points in convex position `h` is `n` and the walk examines `n` pairs",
                   "That the calipers examine at most 4 pairs on any input",
                   "That the hull is free"],
             "c": 1,
             "why": "`4` and `120` are counts on the points on screen. The generalisation is "
                    "about `h`, and `h` is a property of the input: the same lab's "
                    "convex-position example has `h = n = 8`. The hull is not free either "
                    "&mdash; it costs a sort, which is where the `n log n` in the overall bound "
                    "comes from."},
            {"q": "Two pairs attain the squared diameter 225. What should a page report?",
             "a": ["One of the two pairs, since the algorithm found it first",
                   "The value, with a note that more than one pair attains it and the printed pair is one witness",
                   "Both pairs and no value",
                   "Neither, since the answer is ambiguous"],
             "c": 1,
             "why": "The diameter is a well-defined value; the pair attaining it need not be "
                    "unique. Printing one pair silently invites the reader to treat it as the "
                    "pair, and refusing to answer treats a tie as an error. The lab counts how "
                    "many pairs attain the value and says so in its status line."},
        ],
        "mistakes": [
            ("Taking the square root",
             "It converts an exact integer into an approximation, for no benefit: every "
             "comparison the algorithm makes is between two distances, and squaring is monotone "
             "on nonnegative numbers. The only reason to take a root is to print a length for a "
             "human, and then it should be labelled as a reading aid rather than used as the "
             "value."),
            ("Calling `n·h` or `O(h)` a bound on the work for your data",
             "It is a bound in terms of `h`, and `h` can be `n`. Points on a circle, points in "
             "convex position, or any input whose extremes dominate give `h = n` and no saving "
             "at all. The right question is what `h` looks like on the inputs you have, which is "
             "a measurement, and the lab lets you make it."),
            ("Trusting the walk without an independent check",
             "A calipers implementation that advances its second index one step too few returns "
             "a real distance between two real hull vertices &mdash; just not the largest. "
             "Nothing about the output looks wrong. That is why the brute force runs on every "
             "redraw on the same input, and why the page prints both numbers rather than one."),
        ],
        "standard": ("Finish when you can justify discarding the interior points, enumerate the antipodal pairs of a small hull by hand, and say what the pair count depends on.",
                     "You should be able to prove that the diameter is attained by hull vertices, "
                     "explain what makes a pair antipodal and why those are the only candidates, "
                     "work with squared distances throughout, and read `h` as a measurement of "
                     "the input rather than as a bound."),
        "note": ("Everything so far has been about points and the sign of one determinant. The "
                 "next module asks the same question about two segments, where four signs are "
                 "computed instead of one and the interesting inputs are the ones where some of "
                 "them are zero."),
    },
]
