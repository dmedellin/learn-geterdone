"""Accumulation and the Integral -- adding up a rate.

Total change as rate times width summed across pieces; the left and right sums
and the exact gap between them; refining the partition and what the exact
sums show against what they do not prove; the trapezoid and midpoint rules.

Every sum below is an exact fraction read off the calckit riemann mode
(scripts/mathpath/labs/calckit.py) with node scripts/labcheck.js --observe,
and cross-checked by hand with Fractions. The exact total the lab prints
beside a sum is F(b) - F(a) for a polynomial rate; the lessons here use it as
the number the sums are compared with and say plainly that the method which
produces it is the subject of a later lesson.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "total-change-from-a-rate",
        "title": "Total Change from a Rate",
        "module": "Adding up a rate",
        "one_line": "Total change is rate times width added across pieces, and the sum is only as good as the assumption that the rate holds still inside each piece.",
        "summary": (
            "A rate says how fast a quantity changes right now; the total change over an "
            "interval is what that rate adds up to. When the rate is constant the sum is "
            "a single multiplication and it is exact. When the rate moves, cut the "
            "interval into pieces, freeze the rate in each piece, and add rate times width. "
            "The result is an exact fraction and an estimate, and the lesson is about "
            "keeping those two facts apart."
        ),
        "key": [
            "total change ≈ Σ (rate · width)",
            "n pieces, each of width h = (b − a)/n",
            "left sum: the rate at each piece's left end",
            "constant rate: the sum is the total",
            "changing rate: the sum is an estimate",
        ],
        "key_label": "Adding up a rate, one frozen piece at a time",
        "concepts_intro": (
            "Three ideas, in the order a reader meets them: the case where nothing "
            "needs estimating, the device that handles every other case, and the "
            "cost of that device."
        ),
        "concepts": [
            ("A constant rate times a duration is the total change",
             "Water enters a tank at `3` litres per minute for the `4` minutes from "
             "`t = 1` to `t = 5`: the tank gains `3·4 = 12` litres. Nothing else is "
             "needed, and the lab agrees: on the constant preset every sum it prints is "
             "`12`, whatever number of pieces you ask for."),
            ("A moving rate is handled by freezing it in pieces",
             "Cut the interval into `n` pieces of equal width `h = (b − a)/n`. Inside "
             "one piece, pretend the rate is the number it has at the piece's left end. "
             "That piece then contributes rate times width, a constant-rate product, "
             "and the pieces are added. This is the <em>left sum</em>, written `Lₙ`."),
            ("The frozen rate is an assumption, and a rising rate makes it low",
             "In the real situation the rate keeps changing inside each piece. If it is "
             "climbing, the left-end value is the smallest the rate takes in that piece, "
             "so every piece is short and the whole sum is short. The sum is an exact "
             "fraction, and it is still only an estimate of the total."),
        ],
        "read_title": "From speed times time to a sum of pieces",
        "read_intro": "The constant case, the device for everything else, and what the device quietly assumes.",
        "body": [
            ("p", "Distance is speed times time, and the same sentence is true of every "
                  "rate: the change in a quantity is the rate of change times the elapsed "
                  "time, <em>provided the rate does not change</em>. A tank filling at a "
                  "steady `3` litres per minute gains `3·4 = 12` litres in `4` minutes. "
                  "The proviso is the whole difficulty, because most rates worth asking "
                  "about move."),
            ("def", ("Total change from a rate, in n pieces",
                     "Let a rate `f(t)` be given on the interval from `a` to `b`. Cut the "
                     "interval into `n` pieces of equal width `h = (b − a)/n`, with left "
                     "ends `a, a + h, a + 2h, …`. The <strong>left sum</strong> is the "
                     "total of rate times width, using the rate at each left end.",
                     "`Lₙ = h·(f(a) + f(a + h) + f(a + 2h) + … + f(b − h))`. It is exact "
                     "when `f` is constant, and an estimate otherwise.")),
            ("p", "Take the rate `2t` on the interval from `0` to `2`: a tap that opens "
                  "slowly, so that `t` minutes after it opens it is delivering `2t` "
                  "litres per minute. With `n = 4` the width is `h = 1/2`, the left ends "
                  "are `0, 1/2, 1, 3/2`, and the rates there are `0, 1, 2, 3`. Each piece "
                  "contributes its rate times `1/2`."),
            ("math", [
                "piece          rate used     rate · h",
                "0 to 1/2           0           0",
                "1/2 to 1           1           1/2",
                "1 to 3/2           2           1",
                "3/2 to 2           3           3/2",
                "                       sum:    3",
            ]),
            ("h3", "What the sum assumes"),
            ("p", "The sum is `3`. The lab's exact-total tile prints `4`, and the gap is "
                  "not a rounding: the tap is still opening during every piece, and each "
                  "piece used the smallest rate it contains. On a piece from `1` to `3/2` "
                  "the rate climbs from `2` to `3`, and the sum charged the whole piece at "
                  "`2`. The missing part of each piece is a small triangle of width `1/2` "
                  "and height `1`, of area `1/4`, and four of them make the missing `1`."),
            ("p", "Where the total `4` comes from is the work of “The Antiderivative and "
                  "the Fundamental Theorem”, later in this course. For now it is the number "
                  "the sums are compared with, and the next lessons show them closing in "
                  "on it. What matters here is the direction of the error: a rising rate "
                  "and a left sum give a sum that is too low."),
            ("example", ("Why the end rate times the elapsed time is not the total",
                         "A tempting shortcut for `2t` on the interval from `0` to `2` is "
                         "the rate at the end, `4`, times the elapsed time, `2`, which gives "
                         "`8`. That is twice the lab's total of `4`.",
                         "The shortcut treats the rate as `4` for the whole two minutes, "
                         "but it was `4` only at the very end. It was `0` at the start. "
                         "Freezing the rate at its last value overstates the total by the "
                         "same kind of error the left sum understates it, in the other "
                         "direction and by more.")),
            ("p", "A steeper rate shows the same thing at a larger scale. The speed preset "
                  "is `t² + 1` on the interval from `0` to `3` in `n = 3` pieces of width "
                  "`1`. The left ends are `0, 1, 2`, the rates there `1, 2, 5`, and "
                  "`Lₙ = 1·(1 + 2 + 5) = 8`, against an exact total of `12`. Three pieces "
                  "are far too few for a rate that climbs from `1` to `10`."),
            ("p", "Raising the number of pieces helps, and the ramp shows it plainly: with "
                  "`n = 8` the left sum of `2t` is `7/2`, and with `n = 16` it is `15/4`. "
                  "Both are still below `4`, both are exact fractions, and neither is the "
                  "total. How far the process can be pushed, and what it approaches, are "
                  "the questions of the next two lessons."),
        ],
        "lab": ("calckit", {
            "mode": "riemann",
            "rule": "left",
            "preset": "ramp",
            "presets": [
                {"id": "ramp", "label": "Ramp: 2t from 0 to 2, four pieces",
                 "f": "2t", "a": 0, "b": 2, "n": 4, "expect": {"rsSum": "3", "rsExact": "4"}},
                {"id": "speed", "label": "Speed: t² + 1 from 0 to 3, three pieces",
                 "f": "t^2 + 1", "a": 0, "b": 3, "n": 3, "expect": {"rsSum": "8", "rsExact": "12"}},
                {"id": "constant", "label": "Constant: 3 from 1 to 5, four pieces",
                 "f": "3", "a": 1, "b": 5, "n": 4, "expect": {"rsSum": "12", "rsExact": "12"}},
            ],
            "panel_title": "Choose a rate, cut the interval, add rate times width",
            "panel_intro": "The table lists each piece, the rate used and rate times "
                           "width; the sum tile adds them as a fraction. The exact total "
                           "is shown beside it for comparison. Move the pieces control "
                           "and watch the sum change on the ramp but not on the constant.",
        }),
        "steps_title": "Estimating a total change from a rate",
        "steps_intro": "Five moves. The last one is the one that is easy to skip and the one that tells you how far to trust the answer.",
        "steps": [
            ("State the rate and the interval",
             "Write `f(t)` and the two ends `a` and `b`. Say what the units are: litres "
             "per minute times minutes is litres. If the rate is constant, multiply and "
             "stop; nothing below is needed."),
            ("Choose the number of pieces and find the width",
             "Pick `n`, then `h = (b − a)/n`. For the ramp, `(2 − 0)/4 = 1/2`. Equal "
             "widths keep every later step a single multiplication."),
            ("Read the rate at each left end",
             "The left ends are `a, a + h, …, b − h`: `n` values and not `n + 1`, because "
             "the point `b` is the left end of no piece. Evaluate `f` at each."),
            ("Multiply by the width and add",
             "Add the rates first and multiply by `h` once, or multiply piece by piece; "
             "the result is the same fraction. If you find yourself adding the rates and "
             "stopping, you have forgotten the width."),
            ("Say what you assumed and which way it errs",
             "The rate was frozen at the left end of each piece. If it rises across the "
             "interval the sum is low; if it falls the sum is high. Say so beside the "
             "number, because the number alone looks exact."),
        ],
        "worked": {
            "title": "The ramp 2t over two minutes, in four pieces",
            "intro": [
                "A tap opens slowly and delivers `2t` litres per minute, `t` minutes after "
                "it opens. Estimate the water collected over the first two minutes with "
                "four pieces, using the rate at each left end.",
            ],
            "lines": [
                "f(t) = 2t on [0, 2],  n = 4,  h = (2 − 0)/4 = 1/2",
                "left ends:   0     1/2     1     3/2",
                "rates:       0      1      2      3",
                "L₄ = (1/2)·(0 + 1 + 2 + 3) = (1/2)·6 = 3",
                "the lab's exact total: 4",
                "missed per piece: (1/2)·(1/2)·1 = 1/4;  4 · 1/4 = 1",
                "3 + 1 = 4",
                "end rate times time:  4 · 2 = 8   (wrong)",
                "constant 3 on [1, 5]:  3 · 4 = 12, for every n",
            ],
            "after": [
                "The left sum is `3` and the total is `4`; the difference is exactly the "
                "four small triangles the frozen rate cut off. The shortcut `8` is further "
                "out than the estimate, which is a reason to prefer an honest estimate "
                "over a convenient formula.",
                "For a rehearsal, use the speed preset and write out the three left ends "
                "and rates yourself. The supplied first move is that the rates are "
                "`1, 2, 5`. Add them, multiply by the width `1`, and then say in one "
                "sentence why the answer is below `12`.",
            ],
        },
        "quiz_title": "Rates, widths and frozen pieces",
        "quiz": [
            {"q": "A tank gains water at a constant `5` litres per minute from `t = 2` to `t = 6`. How much does it gain?",
             "a": ["10 litres", "20 litres", "30 litres", "It depends on how many pieces you use"],
             "c": 1,
             "why": "A constant rate times the elapsed time is the total change: `5·4 = 20`. "
                    "`10` and `30` come from using the wrong width or the wrong endpoint. "
                    "The number of pieces matters only when the rate moves; for a constant "
                    "rate every cutting gives `20`, which is what the constant preset shows."},
            {"q": "The ramp `2t` on the interval from `0` to `2` has left sum `3` with four pieces and exact total `4`. Which statement explains the shortfall?",
             "a": ["The lab rounds its sums down",
                   "Four pieces always give a sum of 3, whatever the rate",
                   "The rate is rising, so the rate at a left end is the smallest value it takes in that piece",
                   "The left sum leaves out the last piece"],
             "c": 2,
             "why": "Within each piece the rate climbs from its left-end value, and the sum "
                    "charged the whole piece at that smallest value. The lab does not round; "
                    "all its sums are exact fractions. The sum depends on the rate, so four "
                    "pieces do not always give `3`. And the left sum includes all four "
                    "pieces: the left ends are `0, 1/2, 1, 3/2`, one per piece."},
            {"q": "The rate `t² + 1` on the interval from `0` to `3`, with `n = 3` pieces. What is the left sum?",
             "a": ["12", "17", "9", "8"],
             "c": 3,
             "why": "The width is `1` and the left-end rates are `1, 2, 5`, so the sum is "
                    "`1 + 2 + 5 = 8`. `12` is the exact total the lab prints beside it, not "
                    "a left sum. `17` is what the right ends `2, 5, 10` give. `9` would "
                    "come from adding `1 + 2 + 5` and an extra piece that does not exist."},
            {"q": "For which rates is the left sum guaranteed to equal the total change, whatever number of pieces is chosen?",
             "a": ["A constant rate", "A rate that rises steadily", "A rate that is zero at the left end of the interval", "No rate: a sum is never exact"],
             "c": 0,
             "why": "When the rate is constant, freezing it loses nothing, so every cutting "
                    "gives the same product. A steadily rising rate is exactly the case "
                    "where the left sum is low. Being zero at one end does not stop the "
                    "rate changing inside the pieces. And the first option is a counter-"
                    "example to the last: the constant preset prints `12` for every sum."},
        ],
        "mistakes": [
            ("Taking the total change to be the rate at the end times the elapsed time",
             "For `2t` on the interval from `0` to `2` this gives `4·2 = 8`, twice the "
             "lab's total of `4`. The rate was `4` only at the last instant, and it was "
             "`0` at the first. A rate times a time is a total only when the rate is the "
             "same throughout, and the left sum is the honest way to say what happens "
             "when it is not."),
            ("Adding the rates and forgetting to multiply by the width",
             "The four rates of the ramp add to `6`, and `6` litres is not the answer; the "
             "answer is `6` times the width `1/2`, which is `3`. A rate is litres per "
             "minute and only a rate times a time is litres. The table's last column, rate "
             "times width, exists to make that multiplication visible."),
            ("Reading the sum as the total",
             "The left sum `3` is an exact fraction and it is also not the total `4`. "
             "Exact arithmetic on an estimate gives an exact estimate. The lab prints the "
             "two side by side so that the difference is a number you can read, not a "
             "suspicion."),
        ],
        "standard": ("Finish when you can add up a rate across pieces and say what the sum assumed.",
                     "You should be able to compute the width and the left ends for a given "
                     "number of pieces, evaluate the rate at each, form the left sum as an "
                     "exact fraction, and say whether it is below or above the total for a "
                     "rising or falling rate and why. You should also be able to say, in "
                     "one sentence, what is wrong with the end rate times the elapsed time."),
        "note": "The ramp's left sum was low, and its right-end counterpart will turn out to be high by a gap that can be computed before either sum is. &ldquo;Left and Right Sums&rdquo; builds both and brackets the total between them.",
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "left-and-right-sums",
        "title": "Left and Right Sums",
        "module": "Adding up a rate",
        "one_line": "The left and right sums differ by exactly h times the change in the rate across the interval, and for a monotone rate the total lies between them.",
        "summary": (
            "Freezing each piece at its left end gives one estimate; freezing it at its "
            "right end gives another. Their difference can be written down before either "
            "is computed, because every term but two cancels. When the rate only rises or "
            "only falls, the total change is trapped between the two sums, and which sum "
            "is the larger depends on the direction of the rate and on nothing else."
        ),
        "key": [
            "Lₙ uses left ends, Rₙ uses right ends",
            "Rₙ − Lₙ = h·(f(b) − f(a))",
            "rising rate:  Lₙ ≤ total ≤ Rₙ",
            "falling rate: Rₙ ≤ total ≤ Lₙ",
            "which sum is larger follows the rate",
        ],
        "key_label": "Two frozen estimates and the gap between them",
        "concepts_intro": (
            "Three ideas: a second estimate, the formula for how far apart the two are, "
            "and the condition under which the pair brackets the truth."
        ),
        "concepts": [
            ("The right sum freezes each piece at its right end",
             "The same pieces, the same widths, but the rate is read at the right end of "
             "each piece: `Rₙ = h·(f(a + h) + f(a + 2h) + … + f(b))`. The two sums use "
             "almost the same list of rates. The left sum uses `f(a)` and not `f(b)`; "
             "the right sum uses `f(b)` and not `f(a)`."),
            ("The gap is h times the change in the rate",
             "Subtract the two sums and every interior rate appears once with each sign. "
             "What survives is `Rₙ − Lₙ = h·(f(b) − f(a))`. The gap can be written down "
             "from the end values alone, and it halves each time the number of pieces "
             "doubles, because `h` does."),
            ("A monotone rate puts the total between the two sums",
             "If the rate only rises, each piece's true contribution lies between its "
             "left-end estimate and its right-end estimate, so the total lies between "
             "`Lₙ` and `Rₙ`. If it only falls, the roles swap. The bracket is the first "
             "honest statement about the total that needs no further information."),
        ],
        "read_title": "Two estimates, one exact gap, one bracket",
        "read_intro": "The right sum, the telescoping gap and its proof, and the conditions on the rate that the bracket needs.",
        "body": [
            ("p", "The previous lesson froze the rate at the left end of each piece. "
                  "Freezing it at the right end is equally defensible, and the two give "
                  "different numbers. Using the same four pieces on the square rate "
                  "`t²` over the interval from `0` to `1`, the width is `1/4`, the left "
                  "rates are `0, 1/16, 4/16, 9/16`, and the right rates are `1/16, 4/16, "
                  "9/16, 16/16`."),
            ("def", ("The right sum and the gap",
                     "With the pieces of the previous lesson, the <strong>right sum</strong> "
                     "uses the rate at each right end: `Rₙ = h·(f(a + h) + … + f(b))`. "
                     "The <strong>gap</strong> is `Rₙ − Lₙ`.",
                     "A rate is <strong>rising</strong> if `f` never decreases from `a` "
                     "to `b`, and <strong>falling</strong> if it never increases. "
                     "<strong>Monotone</strong> means one or the other.")),
            ("math", [
                "t² on [0, 1], n = 4, h = 1/4",
                "",
                "L₄ = (1/4)·(0 + 1/16 + 4/16 + 9/16)  = (1/4)·(14/16) = 7/32",
                "R₄ = (1/4)·(1/16 + 4/16 + 9/16 + 16/16) = (1/4)·(30/16) = 15/32",
                "R₄ − L₄ = 8/32 = 1/4",
                "h·(f(1) − f(0)) = (1/4)·(1 − 0) = 1/4",
            ]),
            ("thm", ("The gap between the right and left sums",
                     "For any rate `f` on the interval from `a` to `b` cut into `n` equal "
                     "pieces of width `h`, `Rₙ − Lₙ = h·(f(b) − f(a))`.")),
            ("proof", ["Write the left ends as `t₀ = a, t₁, …, tₙ₋₁` and the right ends as "
                       "`t₁, …, tₙ = b`. Then `Lₙ = h·(f(t₀) + f(t₁) + … + f(tₙ₋₁))` and "
                       "`Rₙ = h·(f(t₁) + … + f(tₙ₋₁) + f(tₙ))`.",
                       "The terms `f(t₁), …, f(tₙ₋₁)` appear in both, so they cancel in "
                       "the difference. What remains is `h·(f(tₙ) − f(t₀))`, which is "
                       "`h·(f(b) − f(a))`. Nothing was assumed about `f`: this holds for "
                       "a rate that wanders as much as you like."]),
            ("p", "The proof has no condition on the rate, and the bracket does. Suppose "
                  "the rate rises. On any one piece the rate is at least its left-end "
                  "value and at most its right-end value, so the true change over that "
                  "piece is at least rate-at-left times width and at most rate-at-right "
                  "times width. Adding over the pieces, `Lₙ ≤ total ≤ Rₙ`. For a falling "
                  "rate every inequality reverses."),
            ("h3", "Which sum is the larger"),
            ("p", "The right sum is not always the overestimate. The falling preset is "
                  "`4 − t` on the interval from `0` to `2`, with four pieces. Its "
                  "left-end rates are `4, 7/2, 3, 5/2`, giving `Lₙ = 13/2`, and its "
                  "right-end rates are `7/2, 3, 5/2, 2`, giving `Rₙ = 11/2`. The gap "
                  "`Rₙ − Lₙ` is `−1`, which is `(1/2)·(2 − 4)`, the formula applied "
                  "without change. The lab's exact total is `6`, between the two with "
                  "the larger sum on the left."),
            ("example", ("A rate that is not monotone",
                         "Type `t - t^2` as the rate, with the interval from `0` to `1` "
                         "and one piece. The rate is `0` at both ends, so both sums are "
                         "`0`, and the lab's exact total is `1/6`.",
                         "The total is outside the pair. The bracket needed the rate to "
                         "move one way only; this rate rises and then falls, and the "
                         "two end values say nothing about the middle. The gap formula "
                         "still holds, and gives `0`.")),
            ("p", "Every number the lab prints for the gap is an exact fraction, and so "
                  "is the bracket. On the square preset the total `1/3` lies between "
                  "`7/32` and `15/32`, a window of width `1/4`. That is a statement the "
                  "page can prove by arithmetic rather than assert, and doubling the "
                  "pieces halves the window."),
        ],
        "lab": ("calckit", {
            "mode": "riemann",
            "rule": "left",
            "preset": "ramp",
            "presets": [
                {"id": "ramp", "label": "Ramp: 2t from 0 to 2, four pieces",
                 "f": "2t", "a": 0, "b": 2, "n": 4, "expect": {"rsSum": "3", "rsGap": "2"}},
                {"id": "square", "label": "Square: t² from 0 to 1, four pieces",
                 "f": "t^2", "a": 0, "b": 1, "n": 4, "expect": {"rsSum": "7/32", "rsGap": "1/4"}},
                {"id": "falling", "label": "Falling: 4 − t from 0 to 2, four pieces",
                 "f": "4 - t", "a": 0, "b": 2, "n": 4, "expect": {"rsSum": "13/2", "rsGap": "−1"}},
            ],
            "panel_title": "Set the rate, then compare the left and right sums",
            "panel_intro": "The shipped rule is the left sum; switch the rule to right "
                           "ends to see the other. The gap tile is the right sum minus the "
                           "left sum for the current rate and pieces. Try the falling "
                           "preset and read the sign of the gap.",
        }),
        "steps_title": "Bracketing a total between two sums",
        "steps_intro": "The order matters: decide the direction of the rate before you decide which sum is the lower one.",
        "steps": [
            ("Decide whether the rate is monotone on the interval",
             "Rising, falling, or neither. For a polynomial rate, check the ends and "
             "ask whether it turns around in between. If it is not monotone, the "
             "bracket is not available and the rest is only two estimates."),
            ("Compute the gap before either sum",
             "`h·(f(b) − f(a))` from the end values and the width. It is the width of "
             "the window the total will sit in, and it is a check on your sums: they "
             "must differ by exactly this."),
            ("Compute the left sum",
             "Rates at `a, a + h, …, b − h`, added and multiplied by `h`."),
            ("Compute the right sum, or add the gap",
             "Rates at `a + h, …, b`; or simply `Lₙ + h·(f(b) − f(a))`, which is the "
             "same fraction and a useful independent check."),
            ("Name the lower and the higher",
             "For a rising rate the left sum is lower and the right sum higher; for a "
             "falling rate the reverse. State the bracket as lower ≤ total ≤ higher, "
             "and nothing stronger."),
        ],
        "worked": {
            "title": "The square t² in four pieces, bracketed",
            "intro": [
                "The rate `t²` on the interval from `0` to `1` is rising. Compute both "
                "sums with four pieces and check the gap formula.",
            ],
            "lines": [
                "t² on [0, 1],  n = 4,  h = 1/4",
                "left rates:   0   1/16   4/16   9/16",
                "L₄ = (1/4)·(0 + 1/16 + 4/16 + 9/16) = 7/32",
                "right rates:  1/16  4/16  9/16  16/16",
                "R₄ = (1/4)·(1/16 + 4/16 + 9/16 + 1) = 15/32",
                "R₄ − L₄ = 15/32 − 7/32 = 8/32 = 1/4",
                "h·(f(1) − f(0)) = (1/4)·(1 − 0) = 1/4   agrees",
                "7/32 ≤ 1/3 ≤ 15/32      (7/32 is about 0.21875)",
            ],
            "after": [
                "The two sums differ by `1/4` and the formula said they would, before "
                "either sum was computed. The total `1/3` lies between them, and it is "
                "much nearer the left sum than the right. Nothing in the bracket tells "
                "you that; it is only a window.",
                "For a rehearsal, take the falling preset. The supplied first move is "
                "that the rate drops by `2` across the interval. Predict the gap from "
                "that, then check it against the lab, and say which sum is the larger "
                "and why.",
            ],
        },
        "quiz_title": "Gaps and brackets",
        "quiz": [
            {"q": "For the rate `t²` on the interval from `0` to `3` cut into `n = 6` pieces, what is `Rₙ − Lₙ`?",
             "a": ["9/2", "9", "3/2", "1/2"],
             "c": 0,
             "why": "The width is `h = 1/2` and the rate changes from `0` to `9`, so the "
                    "gap is `(1/2)·9 = 9/2`. `9` forgets the width. `3/2` uses the wrong "
                    "change in the rate, `3` instead of `9`; the rate is `t²`, not `t`. "
                    "`1/2` is only the width."},
            {"q": "On the interval from `0` to `2`, the rate `4 − t` gives `Lₙ = 13/2` and `Rₙ = 11/2` with four pieces. What does that show?",
             "a": ["Something is wrong, since the right sum must exceed the left",
                   "The rate is falling, so the left sum is the larger and the total lies between them",
                   "The total is 13/2",
                   "The total is 11/2"],
             "c": 1,
             "why": "For a falling rate the left-end value is the largest in each piece, so "
                    "the left sum overestimates. Nothing is wrong: the right sum is not "
                    "always the larger. The total lies between the two sums, and the lab's "
                    "total `6` does. It equals neither sum."},
            {"q": "For `t²` on the interval from `0` to `1` with four pieces, `Lₙ = 7/32` and `Rₙ = 15/32`. What is the strongest conclusion about the total change?",
             "a": ["It equals 11/32, the average of the two",
                   "It is below 7/32",
                   "It is at least 7/32 and at most 15/32",
                   "It equals 15/32, since a right sum is the safe overestimate"],
             "c": 2,
             "why": "The rate rises, so the total is bracketed by the two sums. That is "
                    "what the pair proves, and the average is not implied: the lab's total "
                    "is `1/3`, not `11/32`. Below `7/32` contradicts the bracket. And a "
                    "right sum is an overestimate only for a rising rate."},
            {"q": "The number of pieces doubles from `4` to `8` on the same rate and interval. What happens to the gap `Rₙ − Lₙ`?",
             "a": ["It doubles", "It stays the same", "It is multiplied by 4", "It halves"],
             "c": 3,
             "why": "The gap is `h·(f(b) − f(a))`, the end values do not change, and `h` "
                    "halves when `n` doubles. On the square it goes from `1/4` to `1/8`. "
                    "It does not stay fixed, and it does not grow."},
        ],
        "mistakes": [
            ("Believing the right sum is always the overestimate",
             "That is true when the rate rises and false when it falls. On `4 − t` over "
             "the interval from `0` to `2` the left sum `13/2` is above the right sum "
             "`11/2`, and the total `6` is between them. Which sum is higher follows the "
             "direction of the rate and not the name of the sum."),
            ("Using the bracket on a rate that turns around",
             "The window from the left sum to the right sum is guaranteed only for a "
             "monotone rate. The rate `t − t²` is `0` at both ends of the interval from "
             "`0` to `1`; both sums are `0` with one piece and the total is `1/6`, "
             "outside the pair."),
            ("Treating the average of the two sums as the total",
             "For the square, `(7/32 + 15/32)/2 = 11/32`, and the total is `1/3`. The "
             "average is a better estimate than either end, and the next lessons find "
             "out how much better. It is still an estimate, not the number."),
        ],
        "standard": ("Finish when you can compute both sums, predict their gap, and say where the total sits.",
                     "You should be able to compute the left and right sums as exact "
                     "fractions, predict the gap from the end values of the rate and the "
                     "width alone, say which sum is the larger for a rising and a falling "
                     "rate, and state the bracket for a monotone rate without claiming more "
                     "than it gives."),
        "note": 'A window of width `1/4` around `1/3` is a long way from knowing `1/3`. &ldquo;Refining the Partition&rdquo; doubles the pieces again and again and watches what the exact sums do.',
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "refining-the-partition",
        "title": "Refining the Partition",
        "module": "Adding up a rate",
        "one_line": "Doubling the number of pieces moves the exact sums toward a single number, and the table shows that without proving it.",
        "summary": (
            "Cutting the interval into more pieces shrinks the window around the total. "
            "Doubling the pieces over and over gives a column of exact sums; the lab "
            "prints their errors against the exact total and the ratio of one error to "
            "the next. On a straight-line rate that ratio is exactly two. On a curved one "
            "it is close to two and is not two, and the lesson separates what the table "
            "shows from what it would take to prove."
        ),
        "key": [
            "n → 2n:  the pieces halve in width",
            "square t² on [0, 1]:  7/32, 35/128, 155/512",
            "error(n) / error(2n):  44/23, then 92/47",
            "straight-line rate: the ratio is exactly 2",
            "the sums approach 1/3: a claim, not a proof",
        ],
        "key_label": "Doubling the pieces and reading the errors",
        "concepts_intro": (
            "Three ideas: what refining changes, how to measure progress with an exact "
            "ratio, and how not to over-read a table."
        ),
        "concepts": [
            ("Refining means more, thinner pieces, and the width halves",
             "Doubling `n` halves `h` and keeps every old left end as a left end of the "
             "new partition. The new sum has twice as many terms, each with half the "
             "width, and each term uses a rate read closer to where the rate is "
             "actually being added."),
            ("The error ratio measures progress without knowing the total",
             "The error of a sum is the sum minus the total. The ratio "
             "`error(n) / error(2n)` says how many times smaller the error became when "
             "the pieces doubled. A ratio of `2` is the error halving. The lab prints "
             "it as an exact fraction."),
            ("A column of sums suggests a limit and does not prove one",
             "The sums `7/32, 35/128, 155/512` climb, and their errors shrink. The "
             "claim that they approach the total is stated here as a claim. The table "
             "is evidence for three values of `n`, and evidence is not an argument "
             "about all of them."),
        ],
        "read_title": "What doubling the pieces does to an exact sum",
        "read_intro": "A column of sums, two exact ratios, a rate for which the ratio is exactly two, and the line between demonstrating and proving.",
        "body": [
            ("p", "The square rate `t²` on the interval from `0` to `1` has left sums "
                  "that can be computed for any `n`. At `n = 4` the left sum is `7/32`; "
                  "at `n = 8` it is `35/128`; at `n = 16` it is `155/512`. The lab's "
                  "exact total is `1/3`. Each sum is below it and each is closer than "
                  "the one before."),
            ("math", [
                "t² on [0, 1], left sums",
                "",
                "  n      left sum    sum minus total    error ratio",
                "  4      7/32        −11/96",
                "  8      35/128      −23/384            44/23  ≈ 1.91304",
                "  16     155/512     −47/1536           92/47  ≈ 1.95745",
            ]),
            ("p", "The lab prints the error as the sum minus the total, so the errors "
                  "of these low sums are negative: `−11/96`, `−23/384`, `−47/1536`. "
                  "The ratio of one to the next is positive, because the signs cancel. "
                  "The decimals are marked `≈` because they are rounded; `44/23` and "
                  "`92/47` are the exact figures."),
            ("p", "Each doubling cuts the error to a little more than half. If it were "
                  "exactly half the ratio would be `2`, and the ratios are `44/23` and "
                  "`92/47`, which are below `2` and creeping toward it. The reason has "
                  "a simple core: the error is about half of the gap `h·(f(b) − f(a))`, "
                  "and the gap halves exactly."),
            ("h3", "The one rate for which the ratio is exactly two"),
            ("p", "The ramp `2t` on the interval from `0` to `2` is a straight line. "
                  "For a straight line the true total is exactly the average of the "
                  "left and right sums, so the left sum falls short by exactly half the "
                  "gap: `h·(f(b) − f(a))/2 = h·4/2 = 2h`. At `n = 4`, `h = 1/2` and "
                  "the error is `−1`. At `n = 8` it is `−1/2`. The ratio is exactly "
                  "`2`, every time."),
            ("thm", ("The sums approach the total",
                     "For a polynomial rate on a fixed interval, the left sums "
                     "`Lₙ` for `n = 4, 8, 16, …` approach a single number, and that "
                     "number is the exact total change.")),
            ("p", "This is stated as a claim. The table above is the lab demonstrating "
                  "it at three values of `n` for one rate, and the ramp's error `2h` "
                  "proves it for that one rate because `2h` goes to zero as `h` does. "
                  "For a rate like `t²` there is no such formula in sight, and nothing "
                  "the lab prints is a proof for all `n`. The proof is the job of a "
                  "first analysis course; the lab supplies the numbers that make the "
                  "claim believable and specific."),
            ("example", ("A cubic whose ratio is further from two",
                         "The cubic preset is `t³` on the interval from `0` to `2` with "
                         "four pieces. The left sum is `9/4`, the total is `4`, and the "
                         "error is `−7/4`. At `n = 8` the sum is `49/16` and the error "
                         "is `−15/16`.",
                         "The ratio is `(7/4)/(15/16) = 28/15`, about `1.86667`, "
                         "further from `2` than the square's `1.91304` at the same "
                         "`n`. A rate that bends more needs thinner pieces before its "
                         "error settles into halving, and `n = 4` is still coarse for "
                         "it.")),
            ("p", "Doubling the pieces is a measurement, and what it measures is a "
                  "property of the rate. A ratio of exactly `2` identifies a rate "
                  "whose left sum errs by a fixed multiple of `h`. A ratio near `2` "
                  "and below it identifies one that errs by about that. Neither "
                  "ratio is a verdict on the sum's correctness: every figure is "
                  "exact, and the error is the method's."),
        ],
        "lab": ("calckit", {
            "mode": "riemann",
            "rule": "left",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "Square: t² from 0 to 1, four pieces",
                 "f": "t^2", "a": 0, "b": 1, "n": 4, "expect": {"rsSum": "7/32", "rsError": "−11/96", "rsRatio": "44/23"}},
                {"id": "cubic", "label": "Cubic: t³ from 0 to 2, four pieces",
                 "f": "t^3", "a": 0, "b": 2, "n": 4, "expect": {"rsSum": "9/4", "rsError": "−7/4", "rsRatio": "28/15"}},
                {"id": "ramp", "label": "Ramp: 2t from 0 to 2, four pieces",
                 "f": "2t", "a": 0, "b": 2, "n": 4, "expect": {"rsSum": "3", "rsError": "−1", "rsRatio": "2"}},
            ],
            "panel_title": "Double the pieces and read the error and its ratio",
            "panel_intro": "The error tile is the sum minus the exact total; the ratio "
                           "tile divides it by the error at twice as many pieces. Set the "
                           "pieces to 4, 8 and 16 in turn on the square and note the sums. "
                           "On the ramp the ratio is exactly 2; on the others it is not.",
        }),
        "steps_title": "Measuring a refinement",
        "steps_intro": "Four or five numbers from one lab, and one sentence that says what they show.",
        "steps": [
            ("Fix the rate and the interval, and choose a starting n",
             "Everything is compared against one exact total, so only the number of "
             "pieces changes between rows."),
            ("Record the sum and the error at n",
             "The sum tile and the error tile, as fractions. Keep the sign of the "
             "error: a left sum on a rising rate is below the total."),
            ("Double n and record again",
             "Set the pieces to `2n`. The old left ends are still left ends, and "
             "the new sum uses all of them and the midpoints between."),
            ("Divide one error by the next",
             "The ratio tile does this. Compare it with `2`: exactly `2` means the "
             "error halved; slightly under `2` means a little more than half is left."),
            ("State the claim apart from the evidence",
             "Write what the table shows (the sums at these `n`, the ratios) in one "
             "sentence and what you believe it approaches in another. Do not merge "
             "them."),
        ],
        "worked": {
            "title": "The left sum of t² at eight pieces, and the ratio",
            "intro": [
                "From the square at `n = 4`, double the pieces and find the new error "
                "and the ratio, by hand.",
            ],
            "lines": [
                "t² on [0, 1],  n = 8,  h = 1/8",
                "left rates:  0  1  4  9  16  25  36  49   (all over 64)",
                "L₈ = (1/8)·(140/64) = 140/512 = 35/128",
                "total − L₈ = 1/3 − 35/128 = (128 − 105)/384 = 23/384",
                "total − L₄ = 11/96 = 44/384",
                "ratio = (44/384)/(23/384) = 44/23",
                "44/23 is about 1.91304:  close to 2, and not 2",
            ],
            "after": [
                "The squares `0, 1, 4, …, 49` add to `140`, and the sum is `140/512`. "
                "The ratio `44/23` is below `2`, so the error at `n = 8` is a little "
                "more than half of the error at `n = 4`. Had the ratio been exactly "
                "`2` the lab would print `2`, and for `t²` it never does.",
                "For a rehearsal, repeat the computation at `n = 16`. The supplied first "
                "move is that the sixteen left rates are `0, 1, 4, …, 225` over `256`. "
                "You should land on `155/512` and a ratio of `92/47`.",
            ],
        },
        "quiz_title": "Errors, ratios and claims",
        "quiz": [
            {"q": "On the ramp `2t` over the interval from `0` to `2`, the left sum at `n = 4` has error `−1` and at `n = 8` has error `−1/2`. What is the error ratio?",
             "a": ["Exactly 2", "Exactly 4", "Close to 2 but not equal to it", "It cannot be found without the total"],
             "c": 0,
             "why": "`(−1)/(−1/2) = 2`. It is exactly `2` because for a straight-line "
                    "rate the left sum errs by exactly `2h`, and `h` halves. The lab "
                    "prints the total, so the ratio can be found; and unlike the "
                    "curved rates, there is nothing approximate about it."},
            {"q": "On `t²` over the interval from `0` to `1` the ratio of the errors at `n = 4` and `n = 8` is `44/23`. What does that tell you?",
             "a": ["The error at 8 is exactly half the error at 4",
                   "The error at 8 is a little more than half the error at 4",
                   "The error at 8 is a little less than half the error at 4",
                   "The sum at 8 is below the sum at 4"],
             "c": 1,
             "why": "`44/23` is about `1.913`, below `2`, so the old error divided by the "
                    "new one is under `2` and the new error is above half the old. It "
                    "is not exactly half: that would be a ratio of `2`. And the sum at "
                    "`8` is `35/128`, above `7/32`, because the rising rate's left sums "
                    "climb toward the total."},
            {"q": "Which is the most accurate description of what the column `7/32, 35/128, 155/512` establishes?",
             "a": ["That the left sums equal 1/3 at n = 16",
                   "That the sums are proved to converge",
                   "That three left sums of this rate lie below 1/3 and closer to it as n doubles; that they approach 1/3 is the claim they support",
                   "That every rising rate has an error ratio of 44/23"],
             "c": 2,
             "why": "The table is three exact values with their errors. It supports the "
                    "claim that the sums approach the total, and it does not prove it for "
                    "all `n`. The sums are not equal to `1/3` at any of these `n`; `44/23` "
                    "is the ratio for this rate at these two sizes, and other rates "
                    "have other ratios."},
            {"q": "The cubic `t³` over the interval from `0` to `2` has left sums `9/4` at `n = 4` and `49/16` at `n = 8`, and total `4`. What is the error ratio?",
             "a": ["28/15", "2", "15/7", "4"],
             "c": 0,
             "why": "The errors are `4 − 9/4 = 7/4` and `4 − 49/16 = 15/16`, and "
                    "`(7/4)/(15/16) = 28/15`. It is not `2`: only the straight-line rate "
                    "has an exact ratio of `2`. `15/7` takes the two error numerators "
                    "upside down and drops their denominators `4` and `16`; `4` is the "
                    "ratio the trapezoid rule gives on a quadratic, not what the left "
                    "sum gives."},
        ],
        "mistakes": [
            ("Assuming that doubling the pieces halves the error exactly, for every rate",
             "That holds for a straight-line rate, where the error is exactly `2h`. For "
             "`t²` the ratio is `44/23`, then `92/47`: near `2`, creeping toward it, "
             "and never `2`. Treating `2` as a law would lead you to predict the "
             "`n = 8` error of `t²` as `11/192`, and the lab prints `23/384`."),
            ("Reading the ratio as a measure of correctness",
             "A ratio far from `2` does not mean the arithmetic went wrong. Every sum "
             "the lab prints is the exact value of the rule it names; the ratio says "
             "how that rule behaves on this rate at this size."),
            ("Calling a table a proof that the sums approach the total",
             "Three rows, or sixty-four, show what happened at those `n`. The claim "
             "that the sums approach a single number as `n` grows without bound goes "
             "past the table. Here it is stated and demonstrated, and that is the "
             "honest description of the status."),
        ],
        "standard": ("Finish when you can refine a partition, measure the error ratio exactly, and keep the claim apart from the table.",
                     "You should be able to compute left sums at `n` and `2n`, find the "
                     "error and the exact ratio from the lab's total, say why a straight-"
                     "line rate gives exactly `2` and a curved one does not, and state in "
                     "words what the table demonstrates and what it leaves unproved."),
        "note": "A ratio near two means each doubling buys about one extra bit of accuracy, which is slow. &ldquo;The Trapezoid and Midpoint Rules&rdquo; changes the rule and finds ratios of four.",
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "trapezoid-and-midpoint-rules",
        "title": "The Trapezoid and Midpoint Rules",
        "module": "Adding up a rate",
        "one_line": "Averaging the left and right sums, or reading the rate at the middle of each piece, makes the error fall by about four when the pieces double, and by exactly four on a quadratic.",
        "summary": (
            "The trapezoid rule averages the left and right sums; the midpoint rule reads "
            "the rate at the middle of each piece. On a quadratic rate both errors are "
            "exact multiples of the square of the width, so doubling the pieces divides "
            "each by exactly four, and the midpoint error is half the trapezoid error with "
            "the opposite sign. Neither rule is exact for every polynomial."
        ),
        "key": [
            "Tₙ = (Lₙ + Rₙ)/2, Mₙ from midpoint rates",
            "t² on [0, 1]:  T₄ = 11/32,  M₄ = 21/64",
            "errors: T₄ is 1/96 high, M₄ is 1/192 low",
            "doubling n: the error divides by 4",
            "exact for straight lines only",
        ],
        "key_label": "Two better rules and what they cost",
        "concepts_intro": (
            "Three ideas: two ways to use the same pieces better, the error they leave on "
            "a quadratic, and the limit of what either rule can do."
        ),
        "concepts": [
            ("The trapezoid rule averages the two ends",
             "Replace the flat top of each piece by the straight line between the "
             "rate at the left end and the rate at the right end. The area of that "
             "trapezoid is the average of the two end rates times the width, and the "
             "sum of the pieces is `Tₙ = (Lₙ + Rₙ)/2`."),
            ("The midpoint rule reads the rate in the middle",
             "Freeze each piece at the rate in the middle of the piece instead of at "
             "an end. The overshoot on one half of the piece largely cancels the "
             "undershoot on the other. The sum is `Mₙ`."),
            ("Both rules err by the square of the width, on a quadratic",
             "For `t²` the trapezoid error is exactly `h²/6` on the interval from "
             "`0` to `1`, and the midpoint error is exactly `−h²/12`. Halving `h` "
             "divides each by `4`. Neither is zero: the rules are exact for straight "
             "lines, and on a curve only by accident."),
        ],
        "read_title": "Two rules, one exact ratio, and a limit",
        "read_intro": "The definitions, the arithmetic on a quadratic, the proof that the ratio is four there, and the rate for which it is only close to four.",
        "body": [
            ("def", ("The trapezoid and midpoint sums",
                     "With the pieces of the earlier lessons and width `h`, the "
                     "<strong>trapezoid sum</strong> is `Tₙ = (Lₙ + Rₙ)/2`, equivalently "
                     "the sum over pieces of `h·(f(left) + f(right))/2`.",
                     "The <strong>midpoint sum</strong> is `Mₙ = h·(f(m₁) + … + f(mₙ))`, "
                     "where `mₖ` is the middle of the `k`th piece.")),
            ("p", "On the square `t²` over the interval from `0` to `1` with four "
                  "pieces, the earlier lessons found `L₄ = 7/32` and `R₄ = 15/32`. "
                  "The average is `T₄ = (7/32 + 15/32)/2 = 11/32`. The lab's total is "
                  "`1/3`, and `11/32 − 1/3 = 1/96`: the trapezoid sum is high, "
                  "because the rate curves upward and the chord lies above the curve."),
            ("p", "The midpoints of the four pieces are `1/8, 3/8, 5/8, 7/8`, and "
                  "the squares of those are `1, 9, 25, 49` over `64`. So "
                  "`M₄ = (1/4)·(1 + 9 + 25 + 49)/64 = 84/256 = 21/64`. Switch the "
                  "rule control to midpoints and the lab prints `21/64` with error "
                  "`−1/192`. The midpoint sum is low, by half as much as the "
                  "trapezoid sum is high."),
            ("math", [
                "t² on [0, 1]       sum        error (sum − 1/3)",
                "",
                "T₄                 11/32       1/96",
                "T₈                 43/128      1/384",
                "M₄                 21/64       −1/192",
                "M₈                 85/256      −1/768",
                "",
                "T error ratio:  (1/96)/(1/384) = 4",
            ]),
            ("thm", ("Both errors are fixed multiples of the square of the width",
                     "For `t²` on the interval from `0` to `1`, `Tₙ − 1/3 = h²/6` and "
                     "`Mₙ − 1/3 = −h²/12`, where `h = 1/n`.")),
            ("proof", ["Take one piece from `x` to `x + h`. The total over it is "
                       "`((x + h)³ − x³)/3 = h·(x² + xh + h²/3)`, which is the claim "
                       "the lab confirms on the whole interval at `1/3`; the next "
                       "lesson, “The Antiderivative and the Fundamental Theorem”, "
                       "shows where it comes from. The trapezoid contributes "
                       "`h·(x² + (x + h)²)/2 = h·(x² + xh + h²/2)`, which exceeds "
                       "it by `h·h²/6 = h³/6`. The midpoint contributes "
                       "`h·(x + h/2)² = h·(x² + xh + h²/4)`, which falls short by "
                       "`h³/12`.",
                       "Neither excess depends on `x`, so over `n` pieces they add "
                       "to `n·h³/6` and `−n·h³/12`; with `n·h = 1` that is `h²/6` and "
                       "`−h²/12`. Halving `h` divides both by exactly `4`."]),
            ("p", "That is the exact ratio of `4` the lab prints: `T₄` and `T₈` have "
                  "errors `1/96` and `1/384`. The proof is for the square; the lab "
                  "does not extend it to other rates, and the ratio for a cubic is "
                  "a separate computation."),
            ("h3", "Exact for straight lines, and not for what bends"),
            ("p", "The trapezoid rule uses both ends, which makes it tempting to "
                  "think it is exact whenever it has enough information. It is exact "
                  "for every straight-line rate; on a curve it is exact only by "
                  "accident, and on `t²` it is high by `h²/6` at every `n`. The "
                  "quartic preset, `t⁴` on the interval from "
                  "`0` to `1`, makes the same point and adds a refinement. Its "
                  "trapezoid errors are `53/2560` at `n = 4` and `213/40960` at "
                  "`n = 8`, and their ratio is `848/213`, about `3.98122`. It "
                  "approaches `4` and is not `4`."),
            ("p", "A cubic is kinder: on `t³` over the interval from `0` to `1` the "
                  "trapezoid errors are exactly `1/64`, `1/256`, `1/1024` for "
                  "`n = 4, 8, 16`, and the ratio is exactly `4`. Type the cubic into "
                  "the rate box and read it. On every quadratic and cubic rate the "
                  "trapezoid error is a fixed multiple of `h²`, so whenever that error "
                  "is not already zero its ratio is exactly `4`; `t⁴` is the first "
                  "power whose error is not such a multiple."),
        ],
        "lab": ("calckit", {
            "mode": "riemann",
            "rule": "trap",
            "preset": "trap",
            "presets": [
                # rsRule is a redraw-only select and ships one value: trap. The mid
                # preset therefore pins what the page prints under trap; the
                # midpoint figures (21/64, error -1/192) are in the lesson prose and
                # come from switching the Rule control to midpoints.
                {"id": "trap", "label": "Trapezoid: t² from 0 to 1, four pieces",
                 "f": "t^2", "a": 0, "b": 1, "n": 4, "expect": {"rsSum": "11/32", "rsError": "1/96", "rsRatio": "4"}},
                {"id": "mid", "label": "Square again, then switch the rule to midpoints",
                 "f": "t^2", "a": 0, "b": 1, "n": 4, "expect": {"rsSum": "11/32", "rsError": "1/96", "rsRatio": "4"}},
                {"id": "quartic", "label": "Quartic: t⁴ from 0 to 1, four pieces",
                 "f": "t^4", "a": 0, "b": 1, "n": 4, "expect": {"rsSum": "113/512", "rsError": "53/2560", "rsRatio": "848/213"}},
            ],
            "panel_title": "Switch the rule and double the pieces",
            "panel_intro": "The rule control chooses left ends, right ends, trapezoid or "
                           "midpoints; it ships on trapezoid. The error tile is the sum "
                           "minus the exact total and the ratio tile is the error at n "
                           "divided by the error at twice n. Change the pieces from 4 to "
                           "8 and read the ratio for each rule.",
        }),
        "steps_title": "Choosing and checking a rule",
        "steps_intro": "Compute with whichever rule you like, then check it against the exact errors the square gives you.",
        "steps": [
            ("Compute the left and right sums, or the midpoint rates",
             "For the trapezoid rule you can reuse the two sums you already have. For "
             "the midpoint rule list the middle of each piece: left end plus `h/2`."),
            ("Form the sum",
             "`Tₙ = (Lₙ + Rₙ)/2`, or `Mₙ = h` times the midpoint rates added. Keep the "
             "fraction exact."),
            ("Compare with the exact total and note the sign",
             "On a rising, upward-bending rate the trapezoid sum is above the total "
             "and the midpoint sum below. The signs, not just the sizes, say how the "
             "rules relate."),
            ("Double the pieces and take the ratio",
             "For a quadratic or a cubic, expect exactly `4`. For a higher power, expect a ratio "
             "near `4`; a figure far from `4` means the rate is not smooth enough for "
             "the pieces you chose."),
            ("Say which rule is exact for what",
             "Straight lines only. A rule that is exact for lines and off by `h²/6` on "
             "a parabola is a good rule and not an exact one."),
        ],
        "worked": {
            "title": "The trapezoid and midpoint sums of t², exactly",
            "intro": [
                "Compute `T₄`, `T₈` and `M₄` for `t²` on the interval from `0` to `1`, "
                "their errors against the total `1/3`, and the trapezoid error ratio.",
            ],
            "lines": [
                "T₄ = (7/32 + 15/32)/2 = 11/32;  11/32 − 1/3 = 1/96",
                "T₈ = 43/128;  43/128 − 1/3 = 1/384",
                "ratio (1/96)/(1/384) = 4   exactly",
                "midpoints of 4 pieces:  1/8  3/8  5/8  7/8",
                "squares over 64:        1    9    25   49",
                "M₄ = (1/4)·(1 + 9 + 25 + 49)/64 = 84/256 = 21/64",
                "M₄ − 1/3 = −1/192:  half of 1/96, opposite sign",
            ],
            "after": [
                "At four pieces the trapezoid sum is high by `1/96`, about a hundredth, and "
                "the midpoint sum is low by half that, with the opposite sign. That opposition "
                "is why a weighted combination of the two can do better than either, "
                "which is a numerical-analysis topic left alone here.",
                "For a rehearsal, switch the lab's rule to midpoints and set the pieces "
                "to `8`. The supplied first move is that the midpoints are `1/16, 3/16, "
                "…, 15/16`. You should find `85/256` and an error of `−1/768`, a ratio "
                "of `4` again.",
            ],
        },
        "quiz_title": "Trapezoids and midpoints",
        "quiz": [
            {"q": "For `t²` on the interval from `0` to `1` with four pieces, which of these is nearest the exact total `1/3`?",
             "a": ["The left sum 7/32", "The right sum 15/32", "The trapezoid sum 11/32", "The midpoint sum 21/64"],
             "c": 3,
             "why": "The errors are `11/96` (left), `13/96` (right), `1/96` (trapezoid) "
                    "and `1/192` (midpoint) in size. The midpoint sum `21/64` is "
                    "closest, at half the trapezoid's distance. The trapezoid is "
                    "better than either end rule but not better than the midpoint."},
            {"q": "On `t²`, the trapezoid sum is above the total and the midpoint sum is below it. Why do they miss in opposite directions?",
             "a": ["The trapezoid's chord lies above the upward-curving rate, while the midpoint's flat top gains on one side and loses on the other, with a net shortfall",
                   "The lab rounds one up and one down",
                   "The trapezoid rule uses more points",
                   "It happens for every rate, not just curved ones"],
             "c": 0,
             "why": "A chord between two points of an upward-bending curve lies above "
                    "it, so the trapezoid overshoots. A flat top at the middle sits "
                    "below the curve at both ends of the piece by different amounts, "
                    "and the net is a small undershoot. The lab does not round. For a "
                    "straight line both are exact, so it does not happen for every rate."},
            {"q": "The trapezoid errors for `t²` are `1/96` at `n = 4` and `1/384` at `n = 8`. What is their ratio?",
             "a": ["Close to 2, creeping toward it", "Exactly 2", "Exactly 4", "Close to 4, and not 4"],
             "c": 2,
             "why": "`(1/96)/(1/384) = 4` exactly, because the error is `h²/6` and "
                    "halving `h` divides it by `4`. A ratio near `2` belongs to the left "
                    "sum. A ratio near `4` and not `4` is what the quartic gives, not "
                    "the square."},
            {"q": "On the quartic `t⁴` over the interval from `0` to `1`, the trapezoid error ratio from `n = 4` to `n = 8` is `848/213`. What is the best reading?",
             "a": ["The ratio is exactly 4",
                   "The trapezoid rule is exact on the quartic",
                   "The ratio is near 4 and is not 4, since the rate is not a quadratic or a cubic",
                   "The arithmetic must have a mistake"],
             "c": 2,
             "why": "`848/213` is about `3.98122`: near `4`, below it. Exactly `4` holds "
                    "for a polynomial of degree two or three, and `t⁴` is neither. The "
                    "trapezoid errors are `53/2560` and `213/40960`, nonzero, so "
                    "the rule is not exact. Every figure is exact; the ratio is just "
                    "not `4`."},
        ],
        "mistakes": [
            ("Believing the trapezoid rule is exact for every polynomial because it uses both ends",
             "Using both ends gives a straight-line approximation in each piece, and a "
             "straight line is exact only for a straight line. On `t²` the trapezoid sum "
             "is `11/32`, the total is `1/3`, and the error is `1/96` at four pieces, "
             "`1/384` at eight: smaller each time and never zero."),
            ("Expecting the same sign of error from both rules",
             "On `t²` the trapezoid sum is high and the midpoint sum is low, by half as "
             "much. Calling both errors &ldquo;the error&rdquo; and averaging their sizes loses "
             "the fact that they have opposite signs."),
            ("Taking a ratio of 4 as a law for all smooth rates",
             "The ratio is exactly `4` for `t²` and for `t³`, and `848/213` for `t⁴`. "
             "Near `4` for a smooth rate is a reasonable expectation; exactly `4` is a "
             "property of particular rates, and the lab tells you which."),
        ],
        "standard": ("Finish when you can compute trapezoid and midpoint sums exactly and predict how their errors fall.",
                     "You should be able to form `Tₙ` from `Lₙ` and `Rₙ`, list the "
                     "midpoints and form `Mₙ`, find both errors against the exact total "
                     "with their signs, show that on a quadratic the trapezoid error "
                     "divides by exactly `4` when the pieces double, and say why neither "
                     "rule is exact beyond straight lines."),
        "note": "All four rules are now sums of rate times width that approach a number the lab prints as an exact total. &ldquo;The Antiderivative and the Fundamental Theorem&rdquo; shows where that number comes from without any sum.",
    },
]
