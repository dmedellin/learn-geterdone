"""Geometric Algorithms, lessons 07-12 - segments, sweeps, area and distance."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "do-two-segments-meet",
        "title": "Do Two Segments Meet",
        "module": "Segments, and the zero sign",
        "one_line": "Four orientation signs decide a proper crossing, and every remaining case is a zero that has to be finished on the segment.",
        "summary": (
            "Two segments cross properly when each one has the other's endpoints strictly on "
            "opposite sides, which is four orientation tests with opposite signs in pairs. That "
            "covers the case everybody draws and none of the cases that are hard. A zero "
            "anywhere among the four means collinear, and collinear is a one-dimensional "
            "question the determinant cannot answer. The lab checks the four-sign verdict "
            "against an exact solve for the two parameters, which has no orientation sign in it "
            "at all."
        ),
        "key": [
            "proper crossing: orient(q1, q2, p1) and orient(q1, q2, p2) opposite,",
            "                 and orient(p1, p2, q1) and orient(p1, p2, q2) opposite",
            "the crossing example: signs −1, 1, 1, −1, determinants −36, 36, 36, −36",
            "a zero sign means collinear, and the case moves onto the segment",
            "bounding boxes are a filter and never an answer",
            "the oracle: p1 + t(p2 − p1) = q1 + u(q2 − q1), with 0 ≤ t, u ≤ 1",
        ],
        "key_label": "Four determinants, the verdict they settle, and the one they do not",
        "concepts_intro": (
            "The proper case, the reason it is not the whole answer, and a second route that "
            "reaches the same verdict without computing a single orientation."
        ),
        "concepts": [
            ("Straddling is two questions, asked both ways round",
             "The segment `p₁p₂` crosses the LINE through `q₁` and `q₂` when `q₁q₂` has `p₁` and "
             "`p₂` strictly on opposite sides, which is `orient(q₁, q₂, p₁)` and "
             "`orient(q₁, q₂, p₂)` differing in sign. That alone is not enough: the segments "
             "might cross each other's lines in places neither segment reaches. Asking the same "
             "question the other way round as well gives the proper-crossing test, and the two "
             "together are exactly right when no determinant is zero."),
            ("A zero sign is a different question, not a boundary of the same one",
             "If any of the four is zero then three of the four points are collinear, and the "
             "verdict now depends on WHERE along the line things sit &mdash; which is a "
             "question a determinant is structurally unable to answer, since it is zero for "
             "every point on the line. The test has to fall back on comparing coordinates along "
             "the segment. Four of the seven worked examples on this page are cases the "
             "proper test alone gets wrong, and the lab counts them."),
            ("A second route, with no sign in it",
             "Solve `p₁ + t(p₂ − p₁) = q₁ + u(q₂ − q₁)` for `t` and `u`. Both are ratios of "
             "determinants, and the conditions `0 ≤ t ≤ 1` and `0 ≤ u ≤ 1` can be checked by "
             "comparing numerators against the denominator after forcing it positive &mdash; so "
             "nothing is ever divided and the whole thing stays in integers. The lab runs it "
             "beside the four-sign test on every input and reports whether the two agree."),
        ],
        "read_title": "The proper test, the cases it misses, and the route that does not use signs",
        "read_intro": "The four determinants, the theorem that makes them sufficient in general position, and the parametric solve that finishes the rest.",
        "body": [
            ("def", ("Proper crossing, touching, and meeting",
                     "Segments `p₁p₂` and `q₁q₂` <strong>cross properly</strong> when "
                     "`orient(q₁, q₂, p₁)` and `orient(q₁, q₂, p₂)` are nonzero with opposite "
                     "signs and `orient(p₁, p₂, q₁)` and `orient(p₁, p₂, q₂)` are too. They "
                     "<strong>touch</strong> when an endpoint of one lies on the other segment. "
                     "They <strong>meet</strong> when they share at least one point, which is "
                     "exactly when they cross properly or touch.")),
            ("thm", ("The four signs are sufficient when none of them is zero",
                     "If all four orientation determinants are nonzero, then the segments meet "
                     "if and only if they cross properly.")),
            ("proof", ("Suppose they cross properly. Then `p₁` and `p₂` are strictly on opposite "
                       "sides of the line through `q₁q₂`, so the segment `p₁p₂` meets that line "
                       "at a single interior point `x`. Symmetrically the segment `q₁q₂` meets "
                       "the line through `p₁p₂` at a single interior point `y`. Both `x` and "
                       "`y` lie on both lines, and two distinct lines meet in at most one point "
                       "&mdash; they are distinct because all four determinants are nonzero "
                       "&mdash; so `x = y`, and that point is interior to both segments.",
                       "Conversely, suppose they meet at some point `z` and that no determinant "
                       "is zero. Then no endpoint of either lies on the other's line, so `z` is "
                       "interior to both segments; hence each segment has points strictly on "
                       "both sides of the other's line, and since its endpoints are not on that "
                       "line they must be on opposite sides. That is a proper crossing.")),
            ("p", "The hypothesis is doing all the work, and it is the hypothesis that almost "
                  "never holds on real data. Rectilinear layouts, lattice coordinates, anything "
                  "snapped to a grid, anything sharing endpoints: all of them produce zeros. An "
                  "implementation that ships the proper test alone is correct on general "
                  "position and wrong on the inputs people actually have."),
            ("example", ("The crossing everybody draws",
                         "Take `p₁p₂` from `(0, 0)` to `(6, 6)` and `q₁q₂` from `(0, 6)` to "
                         "`(6, 0)`. The four determinants are `−36`, `36`, `36`, `−36`, so the "
                         "signs are `−1, 1, 1, −1`: opposite in each pair, none of them zero. "
                         "The proper test says yes, the parametric solve says yes, and the "
                         "bounding boxes overlap. Everything agrees, which is what makes this "
                         "the wrong example to test an implementation on.")),
            ("p", "The magnitude `36` is the same for all four here because the configuration "
                  "is symmetric, and it is worth remembering from &ldquo;The Orientation "
                  "Test&rdquo; what those numbers mean: `|orient(q₁, q₂, p₁)| = 36` says the "
                  "triangle `q₁ q₂ p₁` has area 18. The test discards every bit of that and "
                  "keeps four signs."),
            ("h3", "The box filter is a filter"),
            ("p", "Two segments whose bounding boxes do not overlap cannot meet, and that test "
                  "is four comparisons with no multiplication in it. It is worth doing first, "
                  "and it is never an answer: boxes that overlap say nothing at all. The lab "
                  "prints the box verdict as its own row so that the distinction between a "
                  "filter and a decision is on the page. None of the seven worked examples "
                  "happens to have overlapping boxes and segments that miss, so type "
                  "`0, 0; 4, 4; 2, 0; 4, 1` to see one: the boxes overlap, the four signs are "
                  "`1, 1, −1, −1`, and the segments do not meet."),
            ("h3", "The parametric route, and why it is the check"),
            ("p", "Write a point of the first segment as `p₁ + t(p₂ − p₁)` and of the second as "
                  "`q₁ + u(q₂ − q₁)`. Setting them equal gives two linear equations in `t` and "
                  "`u`, whose determinant is the cross product of the two direction vectors. "
                  "When that is nonzero, `t` and `u` are ratios of determinants and the "
                  "segments meet exactly when both lie in `[0, 1]`. Force the denominator "
                  "positive by negating both numerators if necessary, and the test becomes four "
                  "integer comparisons with no division."),
            ("p", "When the denominator IS zero the directions are parallel, and there are two "
                  "sub-cases: not collinear, where they cannot meet at all; and collinear, "
                  "where the question becomes whether two intervals on a line overlap. The "
                  "oracle handles that by projecting onto the first segment's direction with a "
                  "dot product, which is a different computation from anything the four-sign "
                  "test does. That is what makes it a check rather than a restatement, and the "
                  "page reports a disagreement in red and declines to say which route is right."),
        ],
        "lab": ("geometry", {
            "mode": "segments",
            "preset": "proper",
            "panel_title": "Two segments, four signs, and two independent verdicts",
            "panel_intro": "The four-orientation test and an exact solve for the two parameters "
                           "answer the same question by different arithmetic, and both verdicts "
                           "are printed on every redraw. Work down the worked-example list: the "
                           "first is the textbook crossing, and four of the seven are cases the "
                           "four-sign test alone gets wrong.",
        }),
        "steps_title": "Deciding whether two segments meet",
        "steps_intro": "Box filter, four signs, and then the case the signs cannot settle.",
        "steps": [
            ("Reject on the bounding boxes if you can",
             "Four comparisons, no multiplications, and it disposes of most pairs in a large "
             "input. Never conclude anything from boxes that DO overlap: that is the filter "
             "failing to reject, not evidence of a crossing."),
            ("Compute all four orientations before deciding anything",
             "Not two, and not two with an early exit. You need to know whether any of them is "
             "zero before you know which branch you are in, and an implementation that "
             "short-circuits on the first pair has already thrown away the information that "
             "would have told it to take the collinear branch."),
            ("If none is zero, the proper test is the whole answer",
             "Opposite signs in each pair means yes, anything else means no, and the theorem "
             "above says that is exact. This is the only case where the four signs are the "
             "complete story."),
            ("If any is zero, finish on the segment, not on the line",
             "A zero means three points are collinear, so ask whether the relevant endpoint "
             "lies BETWEEN the other two &mdash; a coordinate comparison, not a determinant. "
             "The next lesson is built on a pair of inputs with identical signs and opposite "
             "answers, which is what makes this step unskippable."),
        ],
        "worked": {
            "title": "The crossing, the T-junction, and the difference between them",
            "intro": [
                "First `(0, 0)–(6, 6)` against `(0, 6)–(6, 0)`; then `(0, 0)–(6, 0)` against "
                "`(3, 0)–(3, 5)`, where one segment ends on the other.",
            ],
            "lines": [
                "PROPER CROSSING    p1 (0,0)  p2 (6,6)   q1 (0,6)  q2 (6,0)",
                "  orient(q1, q2, p1)   −36     sign −1",
                "  orient(q1, q2, p2)    36     sign  1     opposite: p straddles q's line",
                "  orient(p1, p2, q1)    36     sign  1",
                "  orient(p1, p2, q2)   −36     sign −1     opposite: q straddles p's line",
                "  proper  yes     touching  no     boxes overlap  yes",
                "  verdict from the signs      they meet",
                "  verdict from the parameters they meet",
                "",
                "T-JUNCTION         p1 (0,0)  p2 (6,0)   q1 (3,0)  q2 (3,5)",
                "  orient(q1, q2, p1)    15     sign  1",
                "  orient(q1, q2, p2)   −15     sign −1     opposite",
                "  orient(p1, p2, q1)     0     sign  0     q1 is ON p's line",
                "  orient(p1, p2, q2)    30     sign  1     not opposite: NOT proper",
                "  proper  no      touching  yes    boxes overlap  yes",
                "  verdict from the signs      they meet",
                "  verdict from the parameters they meet",
            ],
            "after": [
                "The second case is the whole lesson in one table. A test that computed "
                "`proper` and returned it would answer NO here, and the segments plainly meet: "
                "`q₁` is the point `(3, 0)`, which is on the first segment. The zero in the "
                "third row is the signal that the proper test has run out of information, and "
                "the `touching` column is what finishes the job.",
                "Notice that the first pair of signs is still opposite in the T-junction. Three "
                "quarters of the proper test is satisfied, which is exactly why this case "
                "survives so long in implementations: it fails only on the last row, and only "
                "when the reader thinks to construct it.",
                "For a faded rehearsal, work out all four signs for `(0, 0)–(4, 0)` against "
                "`(4, 0)–(4, 5)`, which share the endpoint `(4, 0)` and nothing else. The "
                "supplied first move is that two of the four will be zero, because `(4, 0)` "
                "lies on both lines. Predict which two, predict both verdicts, and then say why "
                "`proper` is false on an input where the right answer is obviously yes.",
            ],
        },
        "quiz_title": "Four signs, and the boundary of what they decide",
        "quiz": [
            {"q": "All four orientation determinants are nonzero and the first pair has opposite signs, but the second pair does not. Do the segments meet?",
             "a": ["Yes, since one straddle is enough",
                   "No: with no zeros the proper test is exact, and it fails",
                   "Only if the bounding boxes overlap",
                   "Not enough information without the parametric solve"],
             "c": 1,
             "why": "With no determinant zero, the theorem says meeting and proper crossing are "
                    "the same thing, so a failed proper test settles it. One straddle is not "
                    "enough: the first segment crosses the second's LINE, but somewhere the "
                    "second segment does not reach. The box test adds nothing once the exact "
                    "test has answered."},
            {"q": "Why does an implementation that short-circuits after the first pair of signs get the wrong answer more often than one that computes all four?",
             "a": ["Because the first pair is computed in the wrong order",
                   "Because it never learns whether a determinant was zero, so it cannot tell that it is in a collinear case at all",
                   "Because four determinants are more accurate than two",
                   "Because the short-circuit skips the bounding box"],
             "c": 1,
             "why": "The zeros are the signal to change branch. Short-circuiting means the code "
                    "commits to the proper-crossing answer before it has seen the evidence that "
                    "the proper-crossing answer does not apply. Accuracy is not the issue "
                    "&mdash; every determinant here is exact."},
            {"q": "The parametric solve never computes an orientation sign. Why is that the reason to run it?",
             "a": ["Because it is faster",
                   "Because a check that shares the algorithm's arithmetic cannot catch an error in that arithmetic; different products can",
                   "Because it handles the collinear case and the sign test does not",
                   "Because it avoids BigInt"],
             "c": 1,
             "why": "Both routes are exact and both handle every case; the sign test finishes "
                    "collinear pairs with coordinate comparisons and the oracle finishes them "
                    "with a dot product. The value of the second route is independence: it "
                    "multiplies different numbers, so a transposed term in one does not "
                    "reproduce itself in the other."},
        ],
        "mistakes": [
            ("Shipping the proper test as the intersection test",
             "It is exactly right in general position and wrong on every input with a shared "
             "endpoint, a T-junction, or a collinear overlap &mdash; which is most real data. "
             "Four of the seven worked examples here are in that category, and the page counts "
             "them rather than mentioning them."),
            ("Using bounding boxes as a decision",
             "Non-overlapping boxes prove the segments miss; overlapping boxes prove nothing. "
             "Type `0, 0; 4, 4; 2, 0; 4, 1` into the box: overlapping boxes, no crossing, and a "
             "status line that says the filter has not decided anything."),
            ("Dividing to find the intersection point",
             "The parameters `t` and `u` are ratios of determinants, and the moment you evaluate "
             "them as decimals the comparison against 0 and 1 stops being exact. The oracle "
             "compares numerators against the denominator after forcing the denominator "
             "positive, which answers the yes-or-no question without ever producing the "
             "intersection point. If you genuinely need the point, get the verdict exactly "
             "first and then compute the point, knowing it is an approximation."),
        ],
        "standard": ("Finish when you can classify any pair of segments by hand, including every case where a determinant is zero.",
                     "You should be able to write down the four orientations in the right order, "
                     "state and prove why they are sufficient in general position, name the "
                     "three degenerate families a zero can indicate, and explain why the "
                     "parametric route is worth running even though both routes are exact."),
        "note": ("The zeros are where the work is. &ldquo;Four Zero Signs and Two Different "
                 "Answers&rdquo; takes two inputs whose four determinants are identical &mdash; "
                 "all four zero in both &mdash; and whose correct answers are opposite, which "
                 "settles once and for all that the signs cannot be the whole test."),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "four-zero-signs-and-two-different-answers",
        "title": "Four Zero Signs and Two Different Answers",
        "module": "Segments, and the zero sign",
        "one_line": "Two inputs with identical determinants and opposite correct verdicts, which no refinement of the sign test can separate.",
        "summary": (
            "Collinear segments produce four zero determinants whatever they do. Two of the "
            "lab's worked examples have exactly the same four signs &mdash; 0, 0, 0, 0 &mdash; "
            "and opposite answers: one pair overlaps and one pair has a gap. Since the inputs "
            "agree on every quantity the sign test computes, no amount of care with the signs "
            "can distinguish them, and the collinear case has to be finished as a "
            "one-dimensional interval question."
        ),
        "key": [
            "overlap:  (0, 0)–(6, 0) and (4, 0)–(10, 0)     signs 0, 0, 0, 0     they meet",
            "apart:    (0, 0)–(4, 0) and (6, 0)–(10, 0)     signs 0, 0, 0, 0     they miss",
            "identical four signs, opposite answers: the signs are not a sufficient statistic",
            "the bounding boxes do separate these two: overlapping, and not",
            "a degenerate segment is a point, and all four signs are zero again",
            "the collinear case is an interval overlap along one direction",
        ],
        "key_label": "One pair of inputs that settles what the four signs can decide",
        "concepts_intro": (
            "A pair of inputs, the argument they make, and the machinery that actually finishes "
            "the case."
        ),
        "concepts": [
            ("A determinant is zero everywhere on a line",
             "That is not a defect of the orientation test, it is what the test means: "
             "`orient(a, b, c) = 0` says `c` is on the line through `a` and `b`, with no "
             "information about where. Once all four points are collinear, all four "
             "determinants are zero and every one of them will stay zero however you perturb "
             "the points along the line. There is simply no more signal to extract."),
            ("Two inputs, one signature, opposite answers",
             "`(0, 0)–(6, 0)` against `(4, 0)–(10, 0)` overlaps on the interval from 4 to 6. "
             "`(0, 0)–(4, 0)` against `(6, 0)–(10, 0)` has a gap from 4 to 6. Both produce "
             "`0, 0, 0, 0`. Any function of the four signs must give them the same answer, and "
             "the right answers are different, so no such function is the intersection test. "
             "That is a proof and not a warning, and it takes two lines of the lab to "
             "demonstrate."),
            ("What finishes it is a one-dimensional question",
             "Project both segments onto the direction of the first: `t₀ = (q₁ − p₁)·r` and "
             "`t₁ = t₀ + (q₂ − q₁)·r`, where `r = p₂ − p₁`. The first segment occupies "
             "`[0, r·r]` in that coordinate, the second occupies the interval between `t₀` and "
             "`t₁`, and the two meet exactly when those intervals overlap. Every quantity there "
             "is an integer dot product, so the whole test is exact, and it uses no "
             "determinant."),
        ],
        "read_title": "Why no sign test can work, and what does",
        "read_intro": "The impossibility argument, the interval test that finishes the case, and the degenerate inputs that reach it.",
        "body": [
            ("def", ("Collinear segments, and the projection coordinate",
                     "Two segments are <strong>collinear</strong> when all four endpoints lie on "
                     "one line, which makes all four orientation determinants zero. For "
                     "collinear segments with `r = p₂ − p₁` nonzero, define the "
                     "<strong>projection coordinate</strong> of a point `x` as `(x − p₁)·r`. In "
                     "this coordinate `p₁` is at 0 and `p₂` is at `r·r`, and both are integers "
                     "whenever the endpoints are.")),
            ("thm", ("No function of the four signs is the intersection test",
                     "There exist two pairs of segments whose four orientation signs are equal, "
                     "one of which meets and one of which does not. Consequently any "
                     "intersection test computed from the four signs alone is wrong on at least "
                     "one of them.")),
            ("proof", ("Take `p₁p₂ = (0, 0)–(6, 0)` with `q₁q₂ = (4, 0)–(10, 0)`, and "
                       "`p₁p₂ = (0, 0)–(4, 0)` with `q₁q₂ = (6, 0)–(10, 0)`. In both, all four "
                       "points lie on the line `y = 0`, so all four determinants are zero and "
                       "the sign vectors are both `(0, 0, 0, 0)`.",
                       "The first pair shares every point with `4 ≤ x ≤ 6`, so it meets. The "
                       "second pair has the first segment ending at `x = 4` and the second "
                       "starting at `x = 6`, so no point is on both and it does not meet. A "
                       "function of the sign vector returns one value on that vector, and it "
                       "cannot be both `true` and `false`.")),
            ("p", "That argument is short and it is worth stating as a theorem rather than as a "
                  "remark, because the usual reaction to the collinear case is to look for a "
                  "cleverer combination of the signs. There is none, and the reason is "
                  "structural: the signs are a function of which side of each line each point "
                  "is on, and when everything is on the line, every input with that property "
                  "has the same signature."),
            ("example", ("The two inputs, side by side",
                         "Select the overlapping collinear worked example and read the KPI row: "
                         "proper crossing no, touching yes, bounding boxes overlap yes, verdict "
                         "they meet. Select the one with the gap: proper crossing no, touching "
                         "no, bounding boxes overlap NO, verdict they miss. The four-sign table "
                         "above is byte-for-byte identical between the two runs, and every "
                         "other row on the page changes.")),
            ("p", "One label to distrust while you are there. The worked example with the gap is "
                  "offered as &ldquo;collinear, boxes touching, no overlap&rdquo;, and the boxes "
                  "are not touching: they are the intervals from 0 to 4 and from 6 to 10, with "
                  "two units between them, and the widget's own bounding-box row reports NO on "
                  "that input. Read the row, not the label. While you are checking: none of the "
                  "seven worked examples has overlapping boxes AND segments that miss, so the "
                  "one case that shows the filter failing to decide has to be typed. "
                  "`0, 0; 4, 4; 2, 0; 4, 1` does it &mdash; boxes overlapping, no crossing, and "
                  "the status line then says the boxes are a filter and never an answer."),
            ("p", "The bounding boxes DO separate these two, and it is worth working out why, "
                  "because the answer is more interesting than a coincidence. Along a line, both "
                  "coordinates are monotone in the parameter: if the direction has `rx ≠ 0` then "
                  "`x` increases or decreases steadily, and if `rx = 0` the segment is vertical "
                  "and `y` does. So for COLLINEAR segments, overlapping boxes and overlapping "
                  "intervals along the line are the same condition, and the box test is not a "
                  "filter at all here &mdash; it is exact. Running 197,506 random collinear "
                  "pairs past both tests produces not one disagreement."),
            ("p", "That does not make the box test the answer, for two reasons. It stops being "
                  "exact the moment the segments are not collinear, which is the whole of the "
                  "rest of the problem and where `0, 0; 4, 4; 2, 0; 4, 1` lives. And it says "
                  "nothing about the degenerate case below, where one segment is a point. The "
                  "projection coordinate is the form worth learning because it is the same "
                  "computation in both, and because it states the question in the coordinate the "
                  "answer actually lives in rather than in two coordinates that happen to agree "
                  "with it."),
            ("h3", "Degenerate segments reach the same branch"),
            ("p", "A segment whose two endpoints coincide is a point. The lab has one: the "
                  "point `(3, 2)` against the segment from `(0, 0)` to `(6, 4)`, which passes "
                  "through it. All four determinants are zero again, `proper` is false, and the "
                  "right answer is yes. The parametric route handles this by noticing that "
                  "`r·r = 0` and falling back to asking whether the point lies on the other "
                  "segment; a route that divided by `r·r` would have failed here instead."),
            ("p", "That is the third distinct family that produces four zeros: collinear and "
                  "overlapping, collinear and disjoint, and degenerate. A fourth is nearly "
                  "there &mdash; a shared endpoint gives two zeros rather than four. The lab's "
                  "preset list walks all of them deliberately, and four of its seven entries "
                  "are inputs the proper test alone gets wrong."),
            ("h3", "How the interval test is kept exact"),
            ("p", "The projection coordinates `t₀` and `t₁` are dot products of integer vectors, "
                  "so they are integers, and the first segment occupies `[0, r·r]` which is also "
                  "an integer interval. The test is then `max(t₀, t₁) ≥ 0` and `min(t₀, t₁) ≤ "
                  "r·r`, two integer comparisons. No normalisation, no direction vector of unit "
                  "length, no division."),
            ("p", "It is worth appreciating how little this costs. The entire collinear branch "
                  "is a handful of multiplications and two comparisons, and it converts a test "
                  "that is right on general position into one that is right on everything. The "
                  "usual reason it is missing from an implementation is not cost; it is that "
                  "the author never constructed an input that reaches it."),
        ],
        "lab": ("geometry", {
            "mode": "segments",
            "preset": "overlap",
            "panel_title": "Switch between the two collinear examples and watch only the verdict change",
            "panel_intro": "The four-orientation table is identical on the overlapping pair and "
                           "on the pair with a gap, and the two verdicts are opposite. Everything "
                           "the sign test can see is the same; everything that decides the "
                           "answer is somewhere else. The parametric solve is run on both and "
                           "gets both right.",
        }),
        "steps_title": "Finishing a collinear pair",
        "steps_intro": "Once the determinant is zero, stop thinking about sides and start thinking about intervals.",
        "steps": [
            ("Confirm the case rather than assuming it",
             "Four zeros means all four points are on one line. Two zeros usually means a shared "
             "or touching endpoint. One zero means one endpoint is on the other's line. Each "
             "leads somewhere different, so read all four before branching."),
            ("Choose a direction and project",
             "Take `r = p₂ − p₁` and compute `(x − p₁)·r` for the other segment's endpoints. If "
             "`r·r` is zero the first segment is a point, and the question is just whether that "
             "point lies on the other segment."),
            ("Compare the two intervals with integers",
             "The first segment is `[0, r·r]`; the second is the interval between the two "
             "projected values, in whichever order they came out. They meet when the intervals "
             "overlap, which is two comparisons. Everything here is an integer and nothing is "
             "normalised."),
            ("Test both members of the identical-signature pair",
             "Any implementation of this branch should be run on the overlapping pair and the "
             "pair with a gap. They are the minimal pair of inputs that distinguishes a correct "
             "collinear branch from a missing one, and a test suite without something like them "
             "will pass on an implementation that has no collinear branch at all."),
        ],
        "worked": {
            "title": "The two inputs, and every quantity the page computes for each",
            "intro": [
                "Both are horizontal and both give four zero determinants. Only one of them "
                "meets.",
            ],
            "lines": [
                "                             OVERLAP              APART",
                "  p1, p2                   (0,0) (6,0)         (0,0) (4,0)",
                "  q1, q2                   (4,0) (10,0)        (6,0) (10,0)",
                "",
                "  orient(q1, q2, p1)          0                   0",
                "  orient(q1, q2, p2)          0                   0",
                "  orient(p1, p2, q1)          0                   0",
                "  orient(p1, p2, q2)          0                   0",
                "  signs                    0, 0, 0, 0          0, 0, 0, 0",
                "",
                "  proper crossing            no                  no",
                "  touching                   yes                 no",
                "  bounding boxes overlap     yes                 no",
                "  verdict from the signs     they meet           they miss",
                "  verdict from the parameters they meet          they miss",
                "",
                "  projection coordinate, r = (6,0) so r·r = 36   r = (4,0) so r·r = 16",
                "    q1 at (q1 − p1)·r          24                  24",
                "    q2 at (q2 − p1)·r          60                  40",
                "    first segment occupies    [0, 36]             [0, 16]",
                "    second occupies           [24, 60]            [24, 40]",
                "    intervals overlap?         yes                 no",
            ],
            "after": [
                "The top half of that table is the same twice, and the bottom half is where the "
                "answer lives. That is the argument in its most compact form: everything the "
                "sign test computes is identical, so the sign test cannot be the answer.",
                "The projection rows are worth reading carefully, because they show the general "
                "machinery producing the right answer on both. In the overlapping case the "
                "second segment's interval starts at 24 and the first ends at 36, so they "
                "share `[24, 36]`. In the other case the first ends at 16 and the second starts "
                "at 24, so they do not. Note that `24` appears in both columns and means "
                "different things, because `r` is different &mdash; the coordinate is relative "
                "to the first segment's own direction and length.",
                "For a faded rehearsal, construct a diagonal version: `(0, 0)–(6, 6)` against "
                "`(4, 4)–(10, 10)`, and then against `(8, 8)–(10, 10)`. The supplied first move "
                "is that `r = (6, 6)` so `r·r = 72` in both. Compute the two projection "
                "intervals for each and predict the verdicts; then check that the bounding boxes "
                "agree with them, as the monotonicity argument above says they must, and say "
                "what would have to change about the input for them to stop agreeing.",
            ],
        },
        "quiz_title": "What the signs can and cannot decide",
        "quiz": [
            {"q": "Two inputs produce the sign vector `(0, 0, 0, 0)`; one meets and one does not. What does that establish?",
             "a": ["That one of the determinants was computed wrongly",
                   "That no function of the four signs is the intersection test, since a function returns one value on one input",
                   "That the four-sign test needs a tolerance",
                   "That collinear segments are a special case best excluded"],
             "c": 1,
             "why": "It is an impossibility argument, not a bug report. The four signs are equal "
                    "on the two inputs and the correct answers differ, so anything computed from "
                    "the signs alone must be wrong on one of them. Excluding the case is not "
                    "available either: collinear segments are routine on grid-aligned data."},
            {"q": "The bounding boxes do separate these two inputs. What is the reason?",
             "a": ["Coincidence: both inputs happen to be horizontal",
                   "Both coordinates are monotone along a line, so for collinear segments box overlap and interval overlap are the same condition and the box test is exact",
                   "The box test uses the determinant",
                   "The box test is the correct general intersection test"],
             "c": 1,
             "why": "It is not a coincidence and it is not general. Along any line each "
                    "coordinate moves monotonically with the parameter, so two sub-segments have "
                    "overlapping `x` ranges exactly when their parameter intervals overlap "
                    "&mdash; or `y` ranges, if the line is vertical. That makes the box test "
                    "exact on the collinear branch and still only a filter everywhere else, "
                    "where `0, 0; 4, 4; 2, 0; 4, 1` has overlapping boxes and no crossing."},
            {"q": "A segment has two identical endpoints. What does the parametric oracle do?",
             "a": ["Divides by zero and reports a failure",
                   "Notices that `r·r` is zero and asks instead whether that point lies on the other segment",
                   "Treats it as a proper crossing",
                   "Rejects the input"],
             "c": 1,
             "why": "A degenerate segment is a point, and the right answer is whether the point "
                    "is on the other segment. The oracle tests `r·r` before using it, which is "
                    "the same discipline as forcing the denominator positive instead of "
                    "dividing: check the quantity you are about to rely on. The lab has this "
                    "input as a worked example and both routes answer it."},
        ],
        "mistakes": [
            ("Looking for a cleverer combination of the four signs",
             "There is not one, and the two-input argument on this page proves it in three "
             "lines. The instinct is natural because the proper test is so nearly complete, but "
             "the missing information is not hiding in the signs; it was never in them."),
            ("Concluding from the collinear case that the box test is enough",
             "It really is exact on collinear segments &mdash; that is proved above and checked "
             "on nearly two hundred thousand random collinear pairs &mdash; and that is a "
             "genuinely narrow result. On segments that are not collinear the boxes overlap "
             "whenever the two rectangles do, which has nothing to do with whether the segments "
             "meet: `0, 0; 4, 4; 2, 0; 4, 1` has overlapping boxes and no crossing. The correct "
             "reading is that the box test decides the collinear branch and filters the rest."),
            ("Testing an intersection routine only on crossings",
             "A test suite of properly crossing and clearly separate pairs passes on an "
             "implementation with no collinear branch whatsoever. The minimum useful suite is "
             "the seven worked examples on this page, or something like them: a proper "
             "crossing, a T-junction, a shared endpoint, a parallel pair, a degenerate segment, "
             "and the two collinear cases with the same signs and opposite answers."),
        ],
        "standard": ("Finish when you can prove that the four signs are insufficient and implement the branch that finishes the case.",
                     "You should be able to construct the identical-signature pair from memory, "
                     "state why no function of the signs can separate them, project a collinear "
                     "pair onto the first segment's direction and decide the overlap in "
                     "integers, and say which degenerate families produce four zeros and which "
                     "produce two."),
        "note": ("One pair of segments is a question about two objects. &ldquo;The Sweep Line "
                 "and the Work It Does Not Save&rdquo; asks it about many at once, and measures "
                 "how many of the possible pairs a sweep actually tests &mdash; including an "
                 "input where the answer is all of them."),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "the-sweep-line-and-the-work-it-does-not-save",
        "title": "The Sweep Line and the Work It Does Not Save",
        "module": "Segments, and the zero sign",
        "one_line": "Sorting the endpoints lets a sweep skip pairs whose x ranges never overlap, and on one input it skips none of them.",
        "summary": (
            "A sweep line moves left to right over the endpoints, keeping a status list of the "
            "segments it currently crosses, and tests a new segment only against that list. On "
            "six spread-out segments that is 3 pair tests instead of 15. On four segments that "
            "all cross the middle of the picture it is 6 out of 6: the status list holds "
            "everything at once, and sorting the endpoints bought nothing at all. Both numbers "
            "are measured, and only one of them is what people remember."
        ),
        "key": [
            "events: two per segment, sorted by x; status list = what the line crosses now",
            "a start event tests the new segment against the list it joins",
            "spread out: 6 segments, 12 events, 3 pair tests against 15 pairs",
            "all crossing: 4 segments, 8 events, 6 pair tests against 6 pairs",
            "the crossings found are checked against testing every pair, every redraw",
            "the saving is in the work and never in the answer",
        ],
        "key_label": "Events, the status list, and the pairs a sweep does not test",
        "concepts_intro": (
            "The mechanism, the reason it can skip anything, and the input on which it skips "
            "nothing."
        ),
        "concepts": [
            ("The status list is what makes the skipping legal",
             "Two segments whose `x` ranges do not overlap are never on the sweep line at the "
             "same moment, and two segments that cross are both on the line at the crossing's "
             "`x`. So testing each new segment against the segments currently on the list "
             "cannot miss a crossing. That is the correctness argument, and it is completely "
             "independent of how much work it saves."),
            ("The work is the sum of the status-list sizes",
             "Each start event makes as many pair tests as there are segments already on the "
             "list. So the total is the sum over start events of the list size at that moment, "
             "which is exactly what the event table on the page displays column by column. On "
             "six spread-out segments the list never holds more than two, and the total is 3."),
            ("The saving depends on the input, and can be zero",
             "Put four segments so that all of them span the middle of the picture. The list "
             "reaches size four, every start event tests against everything before it, and the "
             "sweep makes 6 tests out of 6 possible. It has done every test the brute force "
             "would, plus a sort. That is not a flaw in the sweep: it is what its bound says, "
             "because the bound is about the output size as well as the input."),
        ],
        "read_title": "What a sweep skips, and the input where it skips nothing",
        "read_intro": "The events, the correctness argument, the two measured counts, and the honest reading of the difference between them.",
        "body": [
            ("def", ("Events, the status list, and the sweep",
                     "Given `k` segments, the <strong>events</strong> are their `2k` endpoints "
                     "sorted by `x`, each labelled as the start or the end of its segment. The "
                     "sweep processes events in order, maintaining a <strong>status "
                     "list</strong> of the segments whose start has been seen and whose end has "
                     "not. On a start event the new segment is tested against every segment "
                     "currently on the list; on an end event its segment is removed.")),
            ("thm", ("The sweep finds every crossing",
                     "Every pair of segments that intersect is tested by the sweep.")),
            ("proof", ("Let segments `A` and `B` intersect at a point with abscissa `x*`. Both "
                       "`A` and `B` have their start event at or before `x*` and their end event "
                       "at or after it, since an intersection point lies on both segments and "
                       "therefore inside both `x` ranges.",
                       "Consider whichever of the two has the later start event; say it is `B`. "
                       "At the moment `B`'s start event is processed, `A` has already started "
                       "and has not yet ended, so `A` is on the status list. The start event for "
                       "`B` therefore tests `B` against `A`. (Ties in `x` are broken so that "
                       "start events precede end events at the same abscissa, which is what "
                       "makes this argument hold when two segments share an endpoint.)")),
            ("p", "Notice what the proof does not claim: it does not say the sweep tests FEWER "
                  "pairs, only that it tests enough of them. Those are separate questions, and "
                  "the second one has an answer that depends on the input while the first does "
                  "not. The lab checks the first by re-testing every pair on every redraw and "
                  "comparing the two crossing sets."),
            ("example", ("Four segments, six tests, six pairs",
                         "Take `(0, 0)–(8, 8)`, `(0, 8)–(8, 0)`, `(0, 4)–(8, 4)` and "
                         "`(4, 0)–(4, 8)`: two diagonals, a horizontal and a vertical, all "
                         "spanning the same square. The lab reports 4 segments, 8 events, 6 "
                         "pair tests, 6 pairs there are, and 6 crossings found. The status list "
                         "reaches size 4. The sweep did every test the brute force would do, "
                         "and paid for a sort on top."),),
            ("p", "This is the preset that stops the saving being read as a bound, and it is "
                  "worth dwelling on. Nothing has gone wrong: the algorithm is correct, the "
                  "answer is right, and the crossing set matches the brute force exactly. What "
                  "is absent is the improvement. The comparison in the status line reads "
                  "&ldquo;the sweep made every test the brute force would&rdquo;, and it says "
                  "so in amber rather than hiding it."),
            ("h3", "The same algorithm on an input it likes"),
            ("p", "Six segments strung out along the `x` axis in three separated pairs give a "
                  "very different picture. The lab reports 6 segments, 12 events, 3 pair tests "
                  "against 15 pairs, and 3 crossings. Twelve pairs were skipped because their "
                  "`x` ranges never overlapped, and no test could have found a crossing between "
                  "two segments that are never on the line together."),
            ("p", "Three tests against fifteen is a real saving and it is a measurement of those "
                  "six segments. The general claim is different and weaker: the sweep does "
                  "`O((k + I) log k)` work for `k` segments and `I` intersections, and when `I` "
                  "is `Θ(k²)` &mdash; as in the four-segment bundle, where 6 of the 6 pairs "
                  "cross &mdash; that is no better than quadratic. The bound is honest about "
                  "this and the intuition usually is not."),
            ("h3", "Shared endpoints are a decision the page states"),
            ("p", "A staircase of four segments, each ending where the next begins, has three "
                  "shared endpoints. Do those count as crossings? This kit says yes: "
                  "&ldquo;meet&rdquo; is the relation from the previous two lessons, and a "
                  "shared endpoint is a shared point. The lab reports 3 crossings on that input "
                  "and the brute force, using the parametric oracle, agrees. A different "
                  "convention would be defensible and would have to be stated; what is not "
                  "defensible is leaving it to the reader to find out."),
            ("p", "That matters more than it sounds, because the status-list machinery makes it "
                  "easy to get inconsistent: a sweep that skips the test when one segment's end "
                  "event and another's start event share an abscissa will silently adopt a "
                  "different convention from its own brute-force check. The lab's tie-break "
                  "puts start events before end events at equal `x`, which is what keeps the "
                  "two agreeing on the staircase."),
        ],
        "lab": ("geometry", {
            "mode": "sweep",
            "preset": "bundle",
            "panel_title": "Four segments where the sweep saves nothing, and the count that says so",
            "panel_intro": "Step the line across the events and watch the status list grow to "
                           "hold all four at once. The two counts to compare are the pair tests "
                           "the sweep made and the number of pairs there are; on this input they "
                           "are equal. Switch to the spread-out worked example and they become 3 "
                           "and 15.",
        }),
        "steps_title": "Measuring what a sweep actually saved",
        "steps_intro": "Count the tests, not the segments, and then look at the status list that produced the count.",
        "steps": [
            ("Count the pair tests, not the events",
             "The event count is always twice the segment count and tells you nothing about the "
             "work. What varies is how many segments each start event finds already on the "
             "list, and the sum of those is the figure to compare against `k(k − 1)/2`."),
            ("Read the maximum status-list size",
             "It is the single best predictor of whether the sweep helped. A list that never "
             "exceeds two on six segments means almost everything was skipped; a list that "
             "reaches `k` means nothing was."),
            ("Check the crossing set against every pair",
             "Correctness and efficiency are separate claims and only one of them is in "
             "question here. The lab tests all `k(k − 1)/2` pairs on every redraw and compares "
             "the two sets, so a sweep that skipped something it should not have would show as "
             "a set difference rather than as a smaller count."),
            ("State your convention on shared endpoints before measuring anything",
             "Whether touching counts as crossing changes the answer on the staircase input and "
             "on any layout with abutting segments. Decide, write it down, and make sure the "
             "checking route uses the same convention &mdash; otherwise a disagreement between "
             "them is a disagreement about the question."),
        ],
        "worked": {
            "title": "Two inputs, and the event tables that explain the difference",
            "intro": [
                "First the bundle: two diagonals, a horizontal and a vertical, all spanning the "
                "same square. Then six segments strung out in three separated pairs.",
            ],
            "lines": [
                "BUNDLE     4 segments, 8 events",
                "  segment 1 (0,0)-(8,8)   2 (0,8)-(8,0)   3 (0,4)-(8,4)   4 (4,0)-(4,8)",
                "",
                "  event  at      kind    segment   status list after   size",
                "    1    x = 0   start      3        3                   1",
                "    2    x = 0   start      2        3, 2                2",
                "    3    x = 0   start      1        3, 2, 1             3",
                "    4    x = 4   start      4        3, 2, 1, 4          4",
                "    5    x = 4   end        4        3, 2, 1             3",
                "    6    x = 8   end        1        3, 2                2",
                "    7    x = 8   end        2        3                   1",
                "    8    x = 8   end        3        empty               0",
                "  pair tests made   0 + 1 + 2 + 3 = 6",
                "  pairs there are   4·3/2 = 6",
                "  crossings found   6        by testing every pair   6",
                "",
                "SPREAD OUT     6 segments, 12 events",
                "  status list never exceeds 2",
                "  pair tests made   3",
                "  pairs there are   6·5/2 = 15",
                "  skipped           12",
                "  crossings found   3        by testing every pair   3",
            ],
            "after": [
                "Read the bundle's size column downwards: 1, 2, 3, 4. The pair tests made at "
                "each start event are the size of the list it JOINED, so 0, 1, 2 and 3, and "
                "those sum to 6. There are 6 pairs. The arithmetic is not a coincidence "
                "&mdash; when every segment is on the list when every other one arrives, the "
                "sum telescopes to exactly `k(k − 1)/2`.",
                "The other half of the picture is that the bundle also has 6 crossings. Every "
                "pair of those four segments really does cross, so the output is quadratic in "
                "the input, and a bound that is linear in the output size cannot be subquadratic "
                "here. The sweep is not failing to exploit structure; there is no structure to "
                "exploit.",
                "For a faded rehearsal, predict the pair-test count for five segments all "
                "spanning the same interval, then for five segments in a diagonal staircase "
                "where each overlaps only its neighbour in `x`. The supplied first move is that "
                "the first is the telescoping sum again. Work out both, and then say what "
                "maximum status-list size each one reaches.",
            ],
        },
        "quiz_title": "Saving, correctness, and what each count means",
        "quiz": [
            {"q": "On the bundle the sweep makes 6 pair tests and there are 6 pairs. What has gone wrong?",
             "a": ["The status list is not being cleared on end events",
                   "Nothing: every pair really is on the line together, so no pair can be skipped, and the algorithm is correct and unhelpful here",
                   "The events are sorted incorrectly",
                   "The sweep is testing pairs twice"],
             "c": 1,
             "why": "Skipping is only legal for pairs whose `x` ranges never overlap, and here "
                    "all four segments span the same interval. The sweep does the maximum "
                    "possible work and returns the right answer. This is the input that "
                    "prevents &ldquo;3 tests instead of 15&rdquo; from being read as a property "
                    "of the algorithm."},
            {"q": "Six spread-out segments give 3 pair tests against 15 pairs. Which statement is supported?",
             "a": ["The sweep is five times faster than the brute force in general",
                   "On this input the sweep skipped 12 pairs whose `x` ranges never overlapped; the general bound is `O((k + I) log k)` and depends on the number of intersections",
                   "The sweep never tests more than `k` pairs",
                   "Sorting the endpoints always pays for itself"],
             "c": 1,
             "why": "The counts are measurements of the six segments on screen. What is proved "
                    "is the correctness of the skipping and a bound that involves the output "
                    "size `I`; when `I` is quadratic, as on the bundle, the bound gives nothing. "
                    "The third option is flatly contradicted by the bundle's 6."},
            {"q": "Why does the lab re-test every pair on every redraw when the sweep already answered?",
             "a": ["To measure how much slower the brute force is",
                   "Because a sweep that wrongly skips a pair returns a smaller crossing set that looks entirely plausible, and only an independent enumeration reveals it",
                   "Because the sweep cannot handle collinear segments",
                   "To compute the pair count for the status line"],
             "c": 1,
             "why": "A missing crossing is invisible from the output alone: fewer crossings is "
                    "what a correct sweep on a sparse input also produces. Comparing the two "
                    "SETS, not the two counts, is what would catch a tie-break error at a shared "
                    "abscissa. The brute force runs through the parametric oracle, so it also "
                    "shares no code with the sweep's own intersection test."},
        ],
        "mistakes": [
            ("Quoting the tests-skipped figure as the algorithm's behaviour",
             "&ldquo;3 instead of 15&rdquo; is a measurement of six particular segments. The "
             "same algorithm on four segments in the same lab makes every test there is. Any "
             "sentence beginning &ldquo;the sweep reduces the work to&rdquo; needs to end with "
             "a quantity that mentions the output size, not just the input size."),
            ("Confusing the event count with the work",
             "Events are always `2k` and are sorted once. The pair tests are what vary, and "
             "they are the sum of the status-list sizes at start events. A page that reported "
             "the event count as the cost would report the same number for the bundle and for "
             "a set of four segments that never meet."),
            ("Leaving the shared-endpoint convention implicit",
             "It changes the answer on any layout with abutting segments, and it has to match "
             "between the sweep and whatever is checking it. This kit counts a shared endpoint "
             "as a crossing, states it, and orders start events before end events at equal `x` "
             "so that the sweep's own tie-break agrees with that decision."),
        ],
        "standard": ("Finish when you can predict a sweep's pair-test count from the status-list sizes, and name an input on which it saves nothing.",
                     "You should be able to build the event list and trace the status list, "
                     "prove that no crossing can be skipped, compute the pair tests as a sum "
                     "over start events, and state the bound in terms of both the input and the "
                     "output size rather than the input alone."),
        "note": ("Segments are done. The last module changes the object: a closed polygon, where "
                 "the same determinant summed over the edges gives an area and a sign, and where "
                 "&ldquo;is this point inside&rdquo; turns out to have two different definitions "
                 "that agree only under a hypothesis the page checks."),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "the-doubled-area-and-what-its-sign-carries",
        "title": "The Doubled Area and What Its Sign Carries",
        "module": "Area, distance and the measured column",
        "one_line": "Sum one determinant over the edges of a polygon and the total is twice the area, with the winding direction in its sign.",
        "summary": (
            "The shoelace formula adds `xᵢyᵢ₊₁ − xᵢ₊₁yᵢ` over the edges of a closed polygon. "
            "The total is twice the signed area: the magnitude is what you wanted and the sign "
            "says which way round the vertices were typed. Keeping it doubled keeps it an "
            "integer on lattice input, so the page prints `2A` and halves it only at the end. "
            "A second formula that multiplies entirely different pairs of coordinates runs "
            "beside it, and a degenerate polygon of zero area is an answer rather than an error."
        ),
        "key": [
            "2A = Σ (xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ)   over the edges, wrapping round",
            "sign positive counter-clockwise, negative clockwise, zero degenerate",
            "the clockwise square: 2A = −50, so the area is 25",
            "doubling keeps it an integer; halving is the last step and prints a fraction",
            "the trapezoid rule Σ (xᵢ − xᵢ₊₁)(yᵢ + yᵢ₊₁) is the same total, different products",
            "reversing the vertex order negates 2A and changes nothing else",
        ],
        "key_label": "One sum over the edges, its magnitude, and its sign",
        "concepts_intro": (
            "The sum, what the sign is for, and why the value is kept doubled all the way to the "
            "last line."
        ),
        "concepts": [
            ("Each term is the determinant of one edge against the origin",
             "The term `xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ` is `orient(O, vᵢ, vᵢ₊₁)` with `O` the origin: twice "
             "the signed area of the triangle from the origin to that edge. Summing over the "
             "edges adds up triangles that overlap and cancel, and what survives is twice the "
             "area of the polygon. So the shoelace formula is not a new idea; it is the same "
             "determinant as everything else on this course, summed."),
            ("The sign is the winding, and it is information",
             "A positive total means the vertices were listed counter-clockwise, a negative one "
             "clockwise. That is not an error to take an absolute value of: half the algorithms "
             "in computational geometry require a known orientation, and the cheapest way to "
             "get one is to compute the signed area and reverse the list if it came out "
             "negative. The lab's clockwise worked example has `2A = −50` and the page reports "
             "the orientation rather than hiding it."),
            ("Doubling is what keeps it exact",
             "The area of a lattice polygon can be a half-integer &mdash; a triangle of area "
             "`1/2` is the smallest nonzero one there is. Twice the area is always an integer, "
             "so the sum is exact in every intermediate step. The halving happens once, at the "
             "end, and the result is printed as an exact fraction with a decimal beside it "
             "rather than instead of it."),
        ],
        "read_title": "The sum, the sign, and the second formula that checks it",
        "read_intro": "Where the formula comes from, what its sign means, and the independent route the page runs beside it.",
        "body": [
            ("def", ("The doubled signed area",
                     "For a closed polygon with vertices `v₁, …, vₙ` in order, the "
                     "<strong>doubled signed area</strong> is "
                     "`2A = Σᵢ (xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ)`, with the index wrapping so that `vₙ₊₁` is "
                     "`v₁`. Its absolute value is twice the area enclosed; it is positive when "
                     "the vertices are in counter-clockwise order, negative when clockwise, and "
                     "zero when the polygon encloses no area.")),
            ("thm", ("The shoelace formula",
                     "For a simple polygon with vertices listed in order, "
                     "`Σᵢ (xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ)` is twice the enclosed area, signed by the "
                     "orientation of the listing.")),
            ("proof", ("Take the polygon to be counter-clockwise; the clockwise case follows by "
                       "reversing the list, which negates every term. Triangulate it by fanning "
                       "from `v₁`, which is possible for any simple polygon. The signed area of "
                       "the triangle `v₁ vᵢ vᵢ₊₁` is `orient(v₁, vᵢ, vᵢ₊₁) / 2`, and summing "
                       "those over `i` from 2 to `n − 1` gives the area, because the fan covers "
                       "the polygon and the signed areas of any parts that fall outside cancel "
                       "against parts counted twice.",
                       "Now `orient(v₁, vᵢ, vᵢ₊₁)` expands to "
                       "`(xᵢ − x₁)(yᵢ₊₁ − y₁) − (yᵢ − y₁)(xᵢ₊₁ − x₁)`, which is "
                       "`(xᵢ yᵢ₊₁ − xᵢ₊₁ yᵢ)` plus terms in `x₁` and `y₁`. Summing over the fan, "
                       "the `x₁` and `y₁` terms telescope to zero, and the edges `v₁v₂` and "
                       "`vₙv₁` contribute nothing of their own since they lie in the fan's apex. "
                       "What remains is `Σᵢ (xᵢ yᵢ₊₁ − xᵢ₊₁ yᵢ)`, doubled area.")),
            ("p", "The triangulation step is where simplicity is used. A self-intersecting "
                  "polygon still has a shoelace sum, and it is still well defined; what it "
                  "means is a signed count of how many times each region is enclosed, which is "
                  "the winding number by another name. The page checks whether the polygon is "
                  "simple before making claims that require it."),
            ("example", ("The same square, typed both ways",
                         "Type `(0, 0)`, `(5, 0)`, `(5, 5)`, `(0, 5)` and the lab reports "
                         "`2A = 50`, area `25`, counter-clockwise. Type `(0, 0)`, `(0, 5)`, "
                         "`(5, 5)`, `(5, 0)` &mdash; the same four corners in the opposite order "
                         "&mdash; and it reports `2A = −50`, area `25`, clockwise. Nothing about "
                         "the SHAPE changed; the sign is reporting the listing.")),
            ("p", "This is the lab's fourth worked example and it is there to make the sign "
                  "concrete. A reader who has been taking absolute values without thinking will "
                  "see a negative number, assume something has gone wrong, and be exactly wrong: "
                  "the negative number is the answer to a question the absolute value throws "
                  "away."),
            ("h3", "The second formula, and why it is worth running"),
            ("p", "The trapezoid rule computes `Σᵢ (xᵢ − xᵢ₊₁)(yᵢ + yᵢ₊₁)`, which is "
                  "algebraically the same total. Arithmetically it is not: it multiplies "
                  "differences of `x` by sums of `y`, where the shoelace multiplies coordinates "
                  "directly. A transposed subscript in either gives a plausible number, and the "
                  "only thing that catches it is a route that would have to be wrong in exactly "
                  "the same way. The lab prints both and marks a disagreement in red."),
            ("p", "The arithmetic checker behind this kit adds a third route, fanning triangles "
                  "from the first vertex and summing orientation determinants, and requires all "
                  "three to agree on every preset and on hundreds of random convex polygons. "
                  "Three routes to one integer is more than is strictly needed and it is the "
                  "reason a page can print an area without hedging."),
            ("h3", "Zero area is an answer"),
            ("p", "Three collinear vertices give `2A = 0`, and the lab's degenerate worked "
                  "example is exactly that: `(0, 0)`, `(3, 3)`, `(6, 6)`. The area is zero, "
                  "there is no orientation to report, and there is no interior for a point to "
                  "be inside. The page says all three of those things rather than dividing by "
                  "zero or refusing the input. A degenerate case that still answers is what "
                  "distinguishes a complete implementation from one that has never been given "
                  "anything unusual."),
            ("p", "It is worth noticing what does NOT break. The sum is still computed, still "
                  "exactly, and still agrees between the two formulas. The orientation is the "
                  "only field that has no value, and it says so in words instead of picking "
                  "one. The next lesson's inside test also still answers on this polygon, and "
                  "puts every point of the segment on the boundary."),
        ],
        "lab": ("geometry", {
            "mode": "polygon",
            "preset": "clockwise",
            "panel_title": "A square typed clockwise, and the sign that says so",
            "panel_intro": "The doubled area is printed rather than the area, because doubling "
                           "it keeps it an integer; the halved value appears beside it as an "
                           "exact fraction. A second formula multiplying different pairs of "
                           "coordinates runs on every redraw, and the per-edge table shows each "
                           "edge's contribution to the total.",
        }),
        "steps_title": "Computing an area exactly",
        "steps_intro": "Sum first, halve last, and keep the sign until you have used it.",
        "steps": [
            ("List the vertices in order and wrap round",
             "The formula needs a cyclic order, and the final edge from the last vertex back to "
             "the first is a term like any other. Forgetting it is the single most common error "
             "and it produces a number that is wrong by one triangle &mdash; plausible, and not "
             "detectably so without a second route."),
            ("Add the terms as integers",
             "Each term is `xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ`, and on lattice input every one of them is an "
             "integer. Do not halve as you go: the running total can be odd, and halving an odd "
             "integer is where a decimal first enters a computation that did not need one."),
            ("Read the sign before taking the absolute value",
             "Positive is counter-clockwise, negative is clockwise. If a later algorithm needs "
             "a known orientation &mdash; and most of them do &mdash; this is where you learn "
             "it, for free. Then take the magnitude for the area."),
            ("Halve once, and report it as a fraction",
             "`2A` divided by 2 is exact as a rational number and generally not an integer. The "
             "page prints the fraction and puts a decimal beside it as a reading aid; the "
             "fraction is the value and the decimal is a convenience."),
        ],
        "worked": {
            "title": "The clockwise square, edge by edge",
            "intro": [
                "The vertices are `(0, 0)`, `(0, 5)`, `(5, 5)`, `(5, 0)`, in that order, which "
                "goes round clockwise.",
            ],
            "lines": [
                "edge                    x1·y2 − x2·y1",
                "(0, 0) -> (0, 5)        0·5 − 0·0   =    0",
                "(0, 5) -> (5, 5)        0·5 − 5·5   =  −25",
                "(5, 5) -> (5, 0)        5·0 − 5·5   =  −25",
                "(5, 0) -> (0, 0)        5·0 − 0·0   =    0",
                "                                  2A =  −50",
                "",
                "  shoelace          2A = −50",
                "  trapezoid rule    2A = −50",
                "  area              50/2 = 25",
                "  orientation       clockwise",
                "",
                "the same four corners, reversed:",
                "  (0, 0) (5, 0) (5, 5) (0, 5)     2A = +50,  area 25,  counter-clockwise",
            ],
            "after": [
                "Two of the four terms are zero, which is what happens when an edge passes "
                "through the origin's row or column: the term is the doubled area of a triangle "
                "with the origin, and that triangle is flat. The whole area comes from the two "
                "edges that do not touch the axes, and each contributes `−25`.",
                "Move the entire square by adding `(7, 3)` to every vertex and recompute. Every "
                "individual term changes &mdash; none of them is zero any more &mdash; and the "
                "total is still `−50`. The determinant depends only on differences, and the "
                "shoelace sum inherits that: the fan from the origin is a computational device, "
                "not a geometric one.",
                "For a faded rehearsal, compute `2A` for the L-shaped polygon `(0, 0)`, "
                "`(6, 0)`, `(6, 2)`, `(2, 2)`, `(2, 6)`, `(0, 6)` by hand. The supplied first "
                "move is that six vertices means six terms and the last one runs from "
                "`(0, 6)` back to `(0, 0)`. Then check your answer against the area you get by "
                "cutting the L into two rectangles, and say why the shoelace sum handles the "
                "reflex corner without any special case.",
            ],
        },
        "quiz_title": "Signs, doubling, and second routes",
        "quiz": [
            {"q": "A polygon's shoelace sum comes out `−50`. What should a program do with the sign?",
             "a": ["Take the absolute value immediately, since an area is positive",
                   "Use it to learn the vertex ordering, then take the magnitude for the area",
                   "Reverse the vertex list and recompute",
                   "Report an error, since the polygon was typed wrongly"],
             "c": 1,
             "why": "The sign is the orientation of the listing, and most later algorithms need "
                    "to know it. Discarding it immediately throws away information that is free "
                    "here and costs a separate computation later. Reversing and recomputing "
                    "would also work and does twice the arithmetic for the same answer."},
            {"q": "Why does the page print `2A` rather than `A`?",
             "a": ["Because the formula is easier to remember that way",
                   "Because `2A` is an integer on lattice input and `A` may be a half-integer, so doubling keeps every intermediate value exact",
                   "Because the area is measured in half-units",
                   "Because halving is expensive"],
             "c": 1,
             "why": "A lattice triangle can have area `1/2`, so `A` is not always an integer "
                    "while `2A` always is. Keeping the doubled value means no division happens "
                    "until the last line, and the final halving is reported as an exact fraction "
                    "rather than as a decimal close to it."},
            {"q": "The trapezoid rule is algebraically identical to the shoelace formula. What does running both accomplish?",
             "a": ["Nothing, since identical formulas give identical answers",
                   "It catches an implementation error, because the two multiply different pairs of numbers and a transposed subscript in one does not reproduce itself in the other",
                   "It improves the precision",
                   "It handles non-simple polygons"],
             "c": 1,
             "why": "Algebraic identity is exactly what makes the agreement meaningful and "
                    "arithmetic difference is what makes it informative. Neither route rounds, "
                    "so precision is not in play, and both are equally defined on a non-simple "
                    "polygon &mdash; the question of what the number means there is separate "
                    "from whether it was computed correctly."},
        ],
        "mistakes": [
            ("Forgetting the closing edge",
             "The term from the last vertex back to the first is not optional, and omitting it "
             "gives an answer that is off by one triangle: a real number, of a plausible size, "
             "with nothing in it that looks wrong. This is the error the second formula is most "
             "likely to catch, because an implementation that forgets the wrap in one place "
             "usually remembers it in the other."),
            ("Taking the absolute value inside the sum",
             "The terms are supposed to cancel &mdash; that is how the fan from the origin adds "
             "up to the polygon rather than to a pile of overlapping triangles. Summing "
             "magnitudes gives a number that is larger than the area and has no geometric "
             "meaning at all."),
            ("Halving as you go",
             "The running total can be odd at any point, so halving early is where a "
             "half-integer, and then a floating-point value, first enters a calculation that "
             "was exact. Every figure on this course that could be a fraction is carried as a "
             "numerator and a denominator for precisely this reason."),
        ],
        "standard": ("Finish when you can compute a polygon's doubled area by hand, read its orientation off the sign, and say why the value is kept doubled.",
                     "You should be able to derive the formula from the fan of orientation "
                     "determinants, explain what simplicity is used for in that derivation, "
                     "predict what reversing or translating the vertex list does to the total, "
                     "and say what a second formula over different products buys."),
        "note": ("The area is the easy half of what a polygon is asked. &ldquo;Inside, by Parity "
                 "and by Winding&rdquo; asks whether a point is enclosed, which turns out to "
                 "have two different definitions that agree on a simple polygon and are "
                 "genuinely different questions when it is not."),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "inside-by-parity-and-by-winding",
        "title": "Inside, by Parity and by Winding",
        "module": "Area, distance and the measured column",
        "one_line": "Cast a ray and count crossings, or count how many times the boundary goes round the point; the two agree only under a hypothesis worth checking.",
        "summary": (
            "A horizontal ray from the query point crosses the boundary an odd number of times "
            "exactly when the point is inside &mdash; provided the rule for counting a crossing "
            "is written so that a ray passing through a vertex is not counted twice. A "
            "different definition counts how many times the boundary winds around the point. On "
            "a simple polygon the two agree; on a self-intersecting one they are different "
            "questions, and the page tests for simplicity before claiming they must match."
        ),
        "key": [
            "count the edge when exactly one endpoint is strictly above the ray",
            "odd crossings inside, even outside; the ray's direction does not matter",
            "the comb at height 4: 6 crossings outside, 5 crossings inside, same line",
            "the winding number counts signed turns of the boundary around the point",
            "simple polygon: parity and winding agree, and the page checks simplicity first",
            "on the boundary is a third answer, and both routes report it",
        ],
        "key_label": "Two definitions of inside, and the hypothesis that makes them one",
        "concepts_intro": (
            "The half-open rule that makes ray casting work, the second definition, and the "
            "condition under which they are the same question."
        ),
        "concepts": [
            ("The vertex case is handled by a rule, not by a nudge",
             "A ray that passes exactly through a vertex touches two edges, and counting both "
             "or neither gives the wrong parity. The fix is to count an edge only when exactly "
             "one of its endpoints is STRICTLY above the ray's height: a vertex at exactly the "
             "ray's height belongs to whichever of its two edges has its other end above. That "
             "makes each genuine crossing count once, with no perturbation of the input and no "
             "tolerance."),
            ("Winding is a different question with the same answer here",
             "The winding number counts how many times the boundary travels counter-clockwise "
             "around the point, minus the clockwise times. For a simple polygon it is `+1` or "
             "`−1` inside and `0` outside, so `winding ≠ 0` and `crossings odd` agree. For a "
             "figure-eight they do not: a point in one lobe can have winding `0` and odd "
             "parity, or winding `2` and even parity, depending on the shape. The page reports "
             "both numbers and checks simplicity before saying they must match."),
            ("On the boundary is a third answer",
             "A point lying exactly on an edge is neither inside nor outside, and both routes "
             "detect it directly by testing each edge with an exact on-segment predicate. The "
             "page reports it as its own verdict rather than forcing it into one of the other "
             "two, because which of them a boundary point falls into is a convention and not a "
             "fact."),
        ],
        "read_title": "Casting a ray correctly, and the second definition beside it",
        "read_intro": "The half-open rule, the parity theorem, the winding number, and the simplicity test the page runs before comparing them.",
        "body": [
            ("def", ("Ray parity, with the half-open rule",
                     "For a query point `q` and a polygon with vertices `v₁, …, vₙ`, cast the "
                     "horizontal ray from `q` in the direction of increasing `x`. An edge "
                     "`vᵢvᵢ₊₁` is <strong>counted</strong> when exactly one of `yᵢ`, `yᵢ₊₁` is "
                     "strictly greater than `qy`, and the intersection of the edge's line with "
                     "the ray's line lies at `x ≥ qx`. The point is <strong>inside</strong> when "
                     "the number of counted edges is odd.")),
            ("p", "The strictly-above test is doing the delicate work. Written as `yᵢ &gt; qy` "
                  "on one end and `yᵢ₊₁ ≤ qy` on the other, the condition treats the horizontal "
                  "line through `q` as half-open: a vertex exactly at that height counts as "
                  "below. So a ray through a vertex where the boundary passes from below to "
                  "above counts exactly one of the two edges, and a ray through a vertex where "
                  "the boundary touches and turns back counts either both or neither &mdash; "
                  "which is the right answer in both cases."),
            ("thm", ("The Jordan parity theorem, as an algorithm",
                     "For a simple polygon and a point `q` not on the boundary, the number of "
                     "edges counted by the rule above is odd if and only if `q` is in the "
                     "interior.")),
            ("proof", ("Take the ray from `q` and travel along it to infinity. Beyond the "
                       "polygon's bounding box the point is certainly outside. Every time the "
                       "ray properly crosses the boundary, the side changes; every time it "
                       "touches a vertex without passing through, it does not. The counting "
                       "rule is exactly a bookkeeping of the first kind of event and not the "
                       "second: a vertex at the ray's height is assigned to the edge going "
                       "strictly above it, so a pass-through contributes one and a touch-and-"
                       "return contributes zero or two.",
                       "Hence the parity of the count equals the number of side changes between "
                       "`q` and infinity. Since the far end is outside, `q` is inside exactly "
                       "when that number is odd.")),
            ("example", ("A comb, and the same horizontal line at seven places",
                         "The lab's comb has 14 vertices and three upward teeth, with doubled "
                         "area 96 so an area of 48. Query at `(−1, 4)`, outside to the left: "
                         "the ray crosses 6 edges, even, outside. Query at `(3, 4)`, inside the "
                         "first tooth: 5 crossings, odd, inside. At `(5, 4)`, in the notch "
                         "between teeth: 4 crossings, outside. At `(7, 4)`: 3, inside. At "
                         "`(9, 4)`: 2, outside. At `(11, 4)`: 1, inside. Every one of those is "
                         "on the same horizontal line, and the count falls by one at each "
                         "boundary crossing exactly as the theorem says.")),
            ("p", "That sequence &mdash; 6, 5, 4, 3, 2, 1, 0 as the query point moves right "
                  "&mdash; is the proof made visible. Each step to the right passes one edge, "
                  "reducing the number of edges still ahead of the ray by one, and flipping the "
                  "parity. It is worth typing those seven query points into the lab in order."),
            ("h3", "The winding number, and where it separates"),
            ("def", ("The winding number",
                     "The <strong>winding number</strong> of a closed polygon about a point `q` "
                     "not on it is the net number of counter-clockwise revolutions the boundary "
                     "makes around `q`. It is computed by walking the edges and adding `+1` "
                     "each time an edge crosses the horizontal line through `q` upward on the "
                     "right, and `−1` each time one crosses it downward on the right &mdash; "
                     "where &ldquo;on the right&rdquo; is decided by an orientation "
                     "determinant.")),
            ("p", "For a simple polygon the winding number is `+1` inside if the vertices were "
                  "typed counter-clockwise, `−1` if clockwise, and `0` outside. So "
                  "`winding ≠ 0` and odd parity agree. The lab's L-shaped example has winding "
                  "`1` at an interior point; the clockwise square from the previous lesson has "
                  "winding `−1` at its centre, and the point is inside both times."),
            ("p", "For a polygon that crosses itself the two genuinely differ. A doubly wound "
                  "loop has winding `2` at its centre and even parity, so parity says outside "
                  "and winding says inside twice over. Neither is wrong; they answer different "
                  "questions, and which one a consumer wants depends on whether it is filling a "
                  "region or integrating around a contour. The page tests non-adjacent edge "
                  "pairs for intersection before reporting that the two must agree, and says so "
                  "in amber when the polygon is not simple."),
            ("h3", "Three routes, because two agreeing could be two copies of one mistake"),
            ("p", "Besides parity and winding, the arithmetic checker behind this kit casts the "
                  "ray UPWARD instead of rightward and requires that verdict to agree too, on "
                  "every preset and on thousands of random query points against random convex "
                  "hulls. A ray cast in a different direction shares no sub-expression with one "
                  "cast rightward, so a mistake in the half-open comparison shows as a "
                  "disagreement rather than as a consistent wrong answer."),
            ("p", "That is the same discipline as the two area formulas and the three "
                  "determinant routes. It is not belt and braces for its own sake: a "
                  "point-in-polygon test that is wrong only on rays through vertices will pass "
                  "any test suite whose query points were chosen carelessly, and the vertex case "
                  "is the one that actually occurs on grid-aligned data."),
        ],
        "lab": ("geometry", {
            "mode": "polygon",
            "preset": "comb",
            "panel_title": "A comb, a horizontal ray, and the crossings it counts",
            "panel_intro": "The per-edge table shows which edges straddle the ray's height and "
                           "which of them the half-open rule actually counted, so the vertex "
                           "case is visible rather than asserted. Move the query point along the "
                           "line `y = 4` and watch the count fall by one at each boundary "
                           "crossing.",
        }),
        "steps_title": "Testing a point against a polygon",
        "steps_intro": "Decide the boundary convention first, then count with a rule that has no ties in it.",
        "steps": [
            ("Test for the boundary separately and first",
             "Run an exact on-segment predicate against every edge. A point on the boundary is "
             "its own verdict, and forcing it into inside or outside is a convention that the "
             "consumer, not the geometry, should choose."),
            ("Count with the strictly-above rule",
             "An edge counts when exactly one endpoint is strictly above the ray's height. "
             "Write it that way rather than as a pair of inequalities you reason about "
             "case-by-case, because the whole point of the rule is that it removes the cases."),
            ("Use the orientation determinant to place the crossing, not a division",
             "Whether the crossing is at `x ≥ qx` can be decided by the sign of "
             "`orient(vᵢ, vᵢ₊₁, q)` combined with which way the edge runs, and that is exact. "
             "Computing the intersection's `x` coordinate and comparing it introduces a "
             "division for no reason."),
            ("Check simplicity before claiming the two definitions agree",
             "Test every pair of non-adjacent edges for intersection. If any pair meets, parity "
             "and winding are answering different questions and the page should report both "
             "rather than asserting either. On a convex hull, which is always simple, the "
             "question does not arise."),
        ],
        "worked": {
            "title": "The comb, at seven points on one horizontal line",
            "intro": [
                "The comb has 14 vertices, three teeth rising from `y = 2` to `y = 6`, and "
                "doubled area 96. Every query below is at height `y = 4`.",
            ],
            "lines": [
                "query      crossings   parity   verdict",
                "(−1, 4)        6        even    outside",
                "( 1, 4)        6        even    outside     the leftmost notch",
                "( 3, 4)        5        odd     INSIDE      the first tooth",
                "( 5, 4)        4        even    outside     a notch",
                "( 7, 4)        3        odd     INSIDE      the second tooth",
                "( 9, 4)        2        even    outside     a notch",
                "(11, 4)        1        odd     INSIDE      the third tooth",
                "",
                "  2A  = 96,  area 48,  counter-clockwise",
                "  simple polygon: yes, no two non-adjacent edges meet",
                "  winding number at (−1, 4) = 0,  at (3, 4) = 1",
                "  parity and winding agree at every one of the seven",
            ],
            "after": [
                "The count decreases by exactly one at each step to the right, and the parity "
                "therefore alternates. That is not a property of combs; it is the proof of the "
                "parity theorem, made into a table. Each step to the right passes exactly one "
                "edge, so exactly one edge stops being ahead of the ray.",
                "The two leftmost queries are both outside and both have 6 crossings, which is "
                "the one place the pattern pauses. `(1, 4)` sits above the leftmost notch, whose "
                "floor is the edge at `y = 2`; the polygon's left side runs only from `(0, 2)` "
                "down to `(0, 0)`, so at height 4 there is no boundary at all to its left. The "
                "six edges that straddle `y = 4` are the vertical ones at `x = 2, 4, 6, 8, 10` "
                "and `12`, and the ray from `(1, 4)` meets every one of them just as the ray "
                "from `(−1, 4)` does.",
                "For a faded rehearsal, predict the crossing count for a query at `(13, 4)`, to "
                "the right of everything. The supplied first move is that a ray from outside to "
                "the right of the whole polygon crosses nothing. Then predict the winding "
                "number there, and say what the parity would be for a query at `(6, 4)` "
                "&mdash; a point exactly on a vertical edge &mdash; and which of the three "
                "verdicts the page would report.",
            ],
        },
        "quiz_title": "Rays, vertices, and two definitions",
        "quiz": [
            {"q": "A ray passes exactly through a vertex of the polygon. Why does the strictly-above rule get the right answer without perturbing anything?",
             "a": ["Because it rounds the vertex to one side",
                   "Because the vertex is assigned to whichever of its two edges goes strictly above the ray, so a pass-through counts once and a touch-and-return counts zero or two",
                   "Because it ignores horizontal edges",
                   "Because vertices are rare"],
             "c": 1,
             "why": "The rule makes the horizontal line half-open, which turns the ambiguous "
                    "case into a determinate one. A boundary that passes through the vertex from "
                    "below to above has exactly one edge strictly above; one that comes up and "
                    "goes back down has zero or two. Both give the right parity, and no "
                    "coordinate was changed."},
            {"q": "A polygon crosses itself. Parity says outside and the winding number is 2. Which is right?",
             "a": ["Parity, since it matches the visual region",
                   "The winding number, since it is more informative",
                   "Both: they answer different questions, and the page reports both and says the polygon is not simple",
                   "Neither, since the input is invalid"],
             "c": 2,
             "why": "Agreement between them is a theorem about SIMPLE polygons, and its "
                    "hypothesis has failed. A filling algorithm using the even-odd rule wants "
                    "the parity; a contour integral wants the winding number. The page tests "
                    "non-adjacent edge pairs and reports the failure of simplicity rather than "
                    "picking a winner."},
            {"q": "Why does the checker behind this kit also cast the ray upward?",
             "a": ["To handle polygons that are wider than they are tall",
                   "Because a second ray direction shares no sub-expression with the first, so a mistake in the half-open comparison shows as a disagreement instead of as a consistent wrong answer",
                   "Because the rightward ray fails on horizontal edges",
                   "To speed up the query"],
             "c": 1,
             "why": "It is the same independence discipline as the second area formula and the "
                    "third determinant route. A rightward ray and an upward ray answer the same "
                    "question with different comparisons, so the agreement is evidence. The "
                    "rightward ray does handle horizontal edges correctly, which is exactly what "
                    "the half-open rule is for."},
        ],
        "mistakes": [
            ("Nudging the query point to avoid a vertex",
             "It changes the question, and on grid-aligned data the nudged point often lands on "
             "another vertex. The half-open rule costs nothing and removes the case entirely, "
             "which is the general pattern here: degenerate inputs get a rule, not a "
             "perturbation."),
            ("Assuming parity and winding are the same test",
             "They agree on simple polygons, which is most of what anyone draws, so the "
             "difference goes unnoticed until a self-intersecting input arrives &mdash; and "
             "then the disagreement looks like a bug in one of them. The page checks simplicity "
             "explicitly, in quadratic time, and reports what it found."),
            ("Folding “on the boundary” into inside or outside silently",
             "It is a convention, and different consumers want different ones: a filling "
             "algorithm and an adjacency test disagree about it deliberately. Detect it, report "
             "it as a third verdict, and let whatever consumes the answer decide. Both routes "
             "on this page detect it with an exact on-segment test, so the detection itself is "
             "never in doubt."),
        ],
        "standard": ("Finish when you can write the ray-crossing rule so that a ray through a vertex needs no special case, and say when winding and parity part company.",
                     "You should be able to state the half-open condition and justify it on both "
                     "vertex cases, prove the parity theorem from the side-change argument, "
                     "define the winding number and say what it is inside a simple polygon, and "
                     "name the hypothesis that has to be checked before treating the two as one "
                     "test."),
        "note": ("The last lesson of this course leaves predicates behind and goes back to "
                 "distance. &ldquo;The Closest Pair and the Strip&rdquo; is a divide-and-conquer "
                 "recursion whose whole correctness rests on a pair that might straddle the "
                 "dividing line, and whose famous bound of seven neighbours per strip point is "
                 "measured on the page against the number of comparisons actually made."),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "the-closest-pair-and-the-strip",
        "title": "The Closest Pair and the Strip",
        "module": "Area, distance and the measured column",
        "one_line": "Split the points, recurse on both halves, and then handle the pair that might straddle the line with a strip of bounded width.",
        "summary": (
            "Sorting by `x` and recursing gives two candidate distances; the only pair the "
            "recursion can miss is one with a point on each side, and such a pair must lie "
            "within the smaller of those distances of the dividing line. Sorting that strip by "
            "`y` lets each point be compared with at most seven others, which is the classic "
            "bound. The lab measures the comparisons actually made and puts them beside `7n`, "
            "and on twelve points the two are 5 and 84."
        ),
        "key": [
            "split by x, recurse, take d = the smaller of the two answers",
            "a missed pair must have one point each side and be within d of the line",
            "in the strip, sorted by y, each point needs at most 7 later neighbours",
            "twelve points: 17 comparisons against 66 for every pair",
            "strip comparisons 5, against the bound 7n = 84",
            "squared distances throughout: 2 is an integer and √2 is not",
        ],
        "key_label": "The split, the strip, and the measured count against the bound",
        "concepts_intro": (
            "What the recursion can miss, why the strip is enough to catch it, and what the "
            "seven-neighbour bound is and is not."
        ),
        "concepts": [
            ("The only pair at risk is a straddling pair",
             "Sort by `x`, split at the median, recurse on each half. A pair with both points on "
             "the same side was considered by that side's recursive call. So the only pair the "
             "recursion can have missed has one point on each side &mdash; and if its distance "
             "is less than `d`, the better of the two recursive answers, then both of its points "
             "are within `d` of the dividing line. That is the whole of the merge step's "
             "obligation."),
            ("Seven is a packing argument, not an average",
             "Sort the strip by `y`. If two strip points are more than `d` apart in `y` they "
             "cannot beat `d`, so only a window matters. That window is a `2d`-by-`d` rectangle, "
             "and it cannot contain more than eight points that are pairwise at least `d` apart "
             "&mdash; divide it into eight squares of side `d/2` and note that two points in one "
             "such square would be closer than `d`. So each point needs at most seven "
             "comparisons, whatever the input."),
            ("The measured count is far below the bound, and that is not slack in the proof",
             "On the lab's twelve points the strip comparisons total 5 against a bound of "
             "`7n = 84`, and the busiest single strip ran at `4/5 = 0.80` comparisons per strip "
             "point. The bound is a worst case over every input; `4/5` is a measurement of one. "
             "A gap between them is not evidence that the proof is loose, and the page says so "
             "in the status line."),
        ],
        "read_title": "The recursion, the pair it can miss, and the strip that catches it",
        "read_intro": "The split, the merge obligation, the packing argument behind the seven, and the counts the lab measures against it.",
        "body": [
            ("def", ("The divide-and-conquer closest pair",
                     "Sort the points by `x`. If there are at most three, compare all pairs. "
                     "Otherwise split at the median into `L` and `R`, recurse on each, and let "
                     "`d` be the smaller of the two distances returned &mdash; held throughout "
                     "as `d²`, which is an integer. Form the <strong>strip</strong>: the points "
                     "whose `x` is within `d` of the dividing coordinate, tested as "
                     "`(x − mid)² &lt; d²` so that nothing is rooted, and sorted by `y`. For "
                     "each strip point, compare it with the following strip points until the `y` "
                     "gap alone reaches `d`, again tested as `(Δy)² ≥ d²`. Return the smallest "
                     "distance seen.")),
            ("thm", ("The merge step is sufficient",
                     "If the closest pair has one point in `L` and one in `R`, then both lie "
                     "within `d` of the dividing line, and in the strip sorted by `y` they are "
                     "at most seven positions apart.")),
            ("proof", ("Let `p ∈ L` and `q ∈ R` be a pair at distance less than `d`. Then "
                       "`|px − qx| &lt; d`, and the dividing coordinate lies between `px` and "
                       "`qx`, so each of them is within `d` of it. Both are therefore in the "
                       "strip, and `|py − qy| &lt; d` as well, so the scan's early exit on the "
                       "`y` gap does not skip the pair.",
                       "For the position bound, consider the `2d`-by-`d` rectangle centred on "
                       "the dividing line and running from `py` to `py + d`. Every strip point "
                       "between `p` and `q` in the `y` order lies in it. Cut the rectangle into "
                       "eight squares of side `d/2`; the diagonal of such a square is "
                       "`d/√2 &lt; d`, so two points in one square would be closer than `d`, "
                       "which contradicts `d` being the best distance within `L` and within "
                       "`R`. Hence the rectangle holds at most eight points including `p`, so "
                       "`q` is at most seven positions after it.")),
            ("p", "Read the second half of that proof carefully, because it is where the "
                  "constant comes from and it is not an estimate. The eight squares are a "
                  "packing argument: two points within one half-`d` square would violate the "
                  "recursive guarantee, so there is at most one per square. The 7 is `8 − 1`, "
                  "and a different rectangle partition gives a slightly different constant "
                  "&mdash; the literature has versions with 6 and with 4 &mdash; without "
                  "changing the asymptotics at all."),
            ("example", ("Twelve points, and where the answer was found",
                         "The lab opens on twelve points running left to right, with `(11, 4)`, "
                         "`(12, 5)` and `(13, 4)` bunched together near the middle. The closest "
                         "squared distance is 2, between `(11, 4)` and `(12, 5)` &mdash; and "
                         "also between `(12, 5)` and `(13, 4)`, so two pairs tie. The recursion "
                         "made 17 comparisons; testing all 66 pairs gives the same answer. Five "
                         "of those 17 were inside a strip, against a bound of `7n = 84`.")),
            ("p", "It is worth being precise about where the winning pair was found, because "
                  "the story about straddling pairs is easy to over-tell. Sorted by `x`, the "
                  "top-level split is at `x = 14` and the left half's split is at `x = 11`; "
                  "`(11, 4)`, `(12, 5)` and `(13, 4)` all land in the same three-point base "
                  "case, and the pair is found by brute force there. The strip at the level "
                  "above re-examines it and confirms it. So on this input the strip caught "
                  "nothing the base cases had not already found &mdash; which is common, and is "
                  "exactly why the strip cannot be dropped: nothing in the algorithm knows in "
                  "advance that it was unnecessary here."),
            ("h3", "The measured column and the proved column"),
            ("p", "The lab's per-merge table gives, for each merge, the number of points, the "
                  "size of the strip, and the comparisons made inside it. On the twelve points "
                  "it reads: one merge with a strip of 2 making 1 comparison, one with a strip "
                  "of 5 making 4, and the top-level merge with a strip of 2 making none. Total "
                  "5. The rightmost column is comparisons per strip point, as an exact fraction, "
                  "and the largest is `4/5`."),
            ("p", "Beside it sits `7n = 84`. Those two numbers are not the same kind of thing "
                  "and the page labels them as such: 5 is a count of comparisons this run made, "
                  "and 84 is a bound evaluated at `n = 12`. Their ratio is not a measure of "
                  "anything, and in particular it is not a measure of how loose the proof is. "
                  "The proof is about the worst input; this is one input."),
            ("h3", "What every pair costs, and when the recursion is worth it"),
            ("p", "17 comparisons against 66 is a real saving at `n = 12` and it is a small one "
                  "in absolute terms. The lab's five-point worked examples show the recursion "
                  "doing 4 comparisons against 10, and its two-point example doing 1 against 1, "
                  "where the recursion never happens at all. The crossover is where "
                  "`n log n` falls below `n(n − 1)/2`, and at these sizes the constants matter "
                  "more than the asymptotics."),
            ("p", "The reason to build it anyway is the reason to build any of this: the bound "
                  "is `O(n log n)` for every input, and the quadratic scan is `Θ(n²)` for every "
                  "input. The lab runs both on the same points precisely because a recursion "
                  "that drops a straddling pair returns a number that is real, plausible and "
                  "too large, with no internal sign that anything went wrong."),
        ],
        "lab": ("geometry", {
            "mode": "closest",
            "preset": "scatter",
            "panel_title": "Twelve points, the strip, and the comparisons it actually made",
            "panel_intro": "Distances here are squared, so the comparison that decides the "
                           "answer is an integer comparison and nothing is rounded. Every pair "
                           "is tested separately on each redraw, because a recursion that misses "
                           "a pair across the dividing line still returns a plausible number. "
                           "The per-merge table is where the seven-neighbour claim meets the "
                           "count.",
        }),
        "steps_title": "Running the recursion, and checking it",
        "steps_intro": "Recurse, then take seriously the one pair the recursion could not see.",
        "steps": [
            ("Sort by x once, not at every level",
             "The split needs the points in `x` order and re-sorting at every level would add a "
             "logarithmic factor. Sort once at the top and pass slices down; the strip needs a "
             "`y` order, which is a separate and much smaller sort."),
            ("Take `d` as the better of the two halves before building the strip",
             "The strip reaches `d` either side of the line, so it cannot be built until both recursive calls have "
             "returned. This is the step that makes the algorithm a merge rather than two "
             "independent computations."),
            ("Scan forward only, and stop on the y gap",
             "For each strip point compare it with the following ones and break as soon as the "
             "`y` difference alone is at least `d`. Comparing backwards as well would double "
             "the work and find nothing new, and omitting the break is what turns a linear "
             "merge into a quadratic one on a strip that holds everything."),
            ("Check the answer against every pair on small inputs",
             "A recursion that drops a straddling pair returns a real distance between two real "
             "points. There is no invariant it violates and no assertion it fails. The only "
             "check is an independent enumeration, and the lab runs one on every redraw."),
        ],
        "worked": {
            "title": "The twelve points, merge by merge",
            "intro": [
                "Sorted by `x` the points are `(2, 9)`, `(5, 1)`, `(8, 14)`, `(11, 4)`, "
                "`(12, 5)`, `(13, 4)`, `(14, 12)`, `(17, 2)`, `(20, 10)`, `(23, 6)`, `(26, 15)`, "
                "`(29, 3)`.",
            ],
            "lines": [
                "the recursion tree",
                "  split all 12 at x = 14",
                "    split the left 6 at x = 11",
                "      base  (2, 9) (5, 1) (8, 14)          3 comparisons, best 61",
                "      base  (11, 4) (12, 5) (13, 4)        3 comparisons, best 2",
                "    split the right 6 at x = 23",
                "      base  (14, 12) (17, 2) (20, 10)      3 comparisons",
                "      base  (23, 6) (26, 15) (29, 3)       3 comparisons",
                "",
                "merge   depth   points   in the strip   comparisons   per strip point",
                "  1       1        6          2              1            1/2",
                "  2       1        6          5              4            4/5",
                "  3       0       12          2              0            0",
                "",
                "  comparisons, divide and conquer   17",
                "  comparisons, every pair           66",
                "  strip comparisons                 5      against 7n = 84",
                "  squared distance                  2      pair (11, 4) (12, 5)",
                "  pairs attaining it                2",
            ],
            "after": [
                "Twelve of the seventeen comparisons are in the four base cases, three each. "
                "The merges account for five, and the top-level merge for none at all: by the "
                "time it runs, `d` is 2, so the strip about `x = 14` holds only points within "
                "`√2` of it, which is two of them, and they are far enough apart in `y` that "
                "the scan breaks immediately.",
                "The winning pair was found in a base case, not in a strip. That is worth "
                "stating plainly because the strip is usually introduced as the thing that "
                "finds the answer; its actual job is to make sure the answer cannot be missed. "
                "On this input it had nothing to find, and the algorithm has no way of knowing "
                "that in advance &mdash; which is why the merge runs regardless.",
                "For a faded rehearsal, predict the whole table for the ten points in two "
                "columns at `x = 0` and `x = 1`, which is another of the lab's worked examples. "
                "The supplied first move is that every point is within `d` of the dividing line "
                "there, so the strip at the top level holds all ten. Say how many comparisons "
                "the top-level merge then makes, and check whether the per-strip-point figure "
                "gets anywhere near seven.",
            ],
        },
        "quiz_title": "Strips, bounds, and measured counts",
        "quiz": [
            {"q": "Why is it enough for the merge step to look only at points within `d` of the dividing line?",
             "a": ["Because points further away are unlikely to be close to each other",
                   "Because a pair beating `d` must have one point on each side, and then each point is within `d` of the line in `x`",
                   "Because the recursion already compared them",
                   "Because the strip is sorted by `y`"],
             "c": 1,
             "why": "A same-side pair was handled by that side's recursive call, so only a "
                    "straddling pair can be missed; and if such a pair is closer than `d` then "
                    "its `x` gap is under `d` and the line sits between the two coordinates, so "
                    "each point is within `d` of it. That is a proof, not a likelihood argument."},
            {"q": "The lab measures 5 strip comparisons against a bound of `7n = 84`. What does the gap show?",
             "a": ["That the seven-neighbour proof is loose and could be improved",
                   "That the bound is a worst case over all inputs and 5 is a count on this one; the gap is not evidence about the proof",
                   "That the strip was built incorrectly",
                   "That `n` should be the strip size, not the point count"],
             "c": 1,
             "why": "Measured and proved are different kinds of claim, and this whole path is "
                    "organised around not confusing them. The bound says no input can exceed "
                    "`7n`; this input used 5. Neither number is wrong and neither is evidence "
                    "about the other. Sharper constants than 7 do exist, and that is a separate "
                    "matter from the gap on one input."},
            {"q": "On these twelve points the closest pair was found inside a base case rather than in a strip. What follows about the merge step?",
             "a": ["It can be skipped when the halves are far apart",
                   "It is unnecessary on this input and cannot be skipped, because nothing in the algorithm can tell in advance that it is unnecessary",
                   "It was implemented incorrectly",
                   "The split should have been made elsewhere"],
             "c": 1,
             "why": "The merge's job is to rule out a straddling pair, and on this input there "
                    "is none that beats `d`. That is a fact about the input, discovered by "
                    "running the merge. Skipping it would require knowing the answer first, "
                    "which is the same shape of error as reading a measured count as a bound."},
        ],
        "mistakes": [
            ("Rebuilding the sort at every level",
             "Sorting by `x` inside the recursion turns `n log n` into `n log² n`. Sort once and "
             "pass slices. The `y` sort of the strip is unavoidable at each merge unless you "
             "carry a second ordering through the recursion, and at the sizes this lab handles "
             "it is not the dominant cost anyway."),
            ("Comparing every pair within the strip",
             "The strip can hold every point &mdash; one of the lab's worked examples is two "
             "columns one unit apart, where the top-level strip holds all ten points. Without "
             "the `y` sort and the early break, the merge becomes quadratic and the whole "
             "recursion degrades to `Θ(n²)`. The seven-neighbour argument is what licenses the "
             "break, and the break is what makes the merge linear."),
            ("Taking a square root anywhere",
             "The answer is a squared distance, and squared lattice distances are integers. "
             "Rooting them introduces an approximation into the one comparison that decides the "
             "result. Two coincident points give squared distance 0, which is exactly "
             "representable and needs no special case; the lab has that as a worked example."),
        ],
        "standard": ("Finish when you can state exactly which pair the recursion can miss, and justify the constant in the strip scan.",
                     "You should be able to explain why only straddling pairs are at risk and "
                     "why they lie in the strip, reproduce the packing argument that bounds the "
                     "forward scan, read the per-merge table as measurements, and say why a "
                     "measured count far below `7n` says nothing about the tightness of the "
                     "proof."),
        "note": ("That closes this course. Every page of it reduced to the sign of one "
                 "determinant, computed exactly, and every page put a count from the input on "
                 "screen beside a claim about all inputs &mdash; 22 wrong signs out of 29 swept "
                 "magnitudes, 6 pair tests out of 6 possible, 5 strip comparisons against 84. "
                 "Randomised Algorithms takes up the same distinction from the other side, "
                 "where the count is a random variable and the claim is about its expectation."),
    },
]
