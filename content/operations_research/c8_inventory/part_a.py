"""Inventory Models -- the first four lessons: the quantity, and what moves it.

The deterministic half. One item, a demand rate that does not vary, and the one
decision there is: how much to order at a time. The quantity arrives from a
DISCRIMINANT rather than from a derivative, because the path's prerequisites
promise a reader there is no calculus on it, and the flatness of the cost curve
around that quantity arrives from a second discriminant rather than from a
sentence. Then the two things that move the answer: a price that depends on how
much is ordered, and a run that takes time and may be allowed to finish late.

Every figure below is READ OFF the kit -- scripts/mathpath/labs/inventory.py --
by extracting its shipped JavaScript with the regex scripts/mathcheck.js uses
and executing it under node, rather than transcribed from a plan. Where the
plan and the kit disagreed, the kit won and the lesson says what the kit does.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-economic-order-quantity",
        "title": "The Economic Order Quantity",
        "module": "The order quantity",
        "one_line": "Order often and pay for the orders; order big and pay to store it — find the quantity where the two costs balance, then measure how flat the bottom is.",
        "summary": (
            "One item, a steady demand rate, and one decision. Ordering cost falls like "
            "`K·D/Q` and holding cost rises like `h·Q/2`, so the total has a minimum where "
            "neither is small, and at that minimum the two halves are exactly equal "
            "&mdash; which is the equation `Q² = 2KD/h` and therefore the answer. The "
            "second half of the lesson is the part textbooks assert: the cost curve really "
            "is flat around the optimum, the width of the flat part is computable, and it "
            "does not depend on `K`, `D` or `h` at all."
        ),
        "key": [
            "C(Q) = K·D/Q + h·Q/2          ordering falls like 1/Q, holding rises like Q",
            "at the optimum the two halves are EQUAL:  K·D/Q = h·Q/2  ⟹  Q² = 2KD/h",
            "Q* = √(2KD/h)       C* = √(2KDh)       both irrational unless the data are kind",
            "C(t·Q*)/C* = (t + 1/t)/2      no K, no D, no h — that ratio is the flatness",
            "within 1% of the minimum:  0.8682·Q* to 1.1518·Q*   =  13.2% below, 15.2% above",
            "K = 100, D = 1200, h = 6  ⟹  Q* = 200 and C* = 1200, as 600 of each half",
        ],
        "key_label": "One cost in two halves, and the width of its flat bottom",
        "concepts_intro": (
            "Three ideas. The first is the only modelling assumption the whole formula "
            "rests on, the second is the derivation in one line, and the third is the one "
            "that changes what you do on a Monday."
        ),
        "concepts": [
            ("Average stock is Q/2 because the sawtooth is straight",
             "A batch of `Q` arrives, demand drains it at a constant rate, it hits zero, "
             "the next batch arrives. The stock level is a straight line falling from `Q` "
             "to `0`, over and over, so its average over a cycle is `Q/2` and the holding "
             "bill is `h·Q/2` per unit time. Every part of that sentence is an assumption "
             "&mdash; constant demand, instant replenishment, no shortages &mdash; and the "
             "panel draws the sawtooth so that what is being assumed is visible rather "
             "than tucked into a symbol."),
            ("The optimum is where the two halves are equal, and nothing is differentiated",
             "`K·D/Q` and `h·Q/2` are the two costs pulling opposite ways. Set them equal "
             "and you get `Q² = 2KD/h` in one line. That is not a proof on its own "
             "&mdash; the crossing has to be shown to be the minimum &mdash; and the proof "
             "is a discriminant, which is the sibling lesson &ldquo;The Order Quantity as "
             "a Discriminant&rdquo;. What matters here is that the answer and the reason "
             "for it are both algebra a reader can check."),
            ("Flat is a measurement, not an adjective",
             "Ordering `t` times the best quantity costs `(t + 1/t)/2` times the minimum. "
             "That expression contains none of `K`, `D` or `h`, so the penalty for being "
             "wrong by a given factor is the same in every warehouse there has ever been. "
             "Twice the best quantity and half of it both cost `5/4` of the minimum; on "
             "the worked instance that is `1500` against `1200`, at `Q = 400` and at "
             "`Q = 100` alike."),
        ],
        "read_title": "The model, the quantity, and how much it matters to miss it",
        "read_intro": "What is being assumed, the one-line derivation, and then the measurement that says how much precision the answer deserves.",
        "body": [
            ("def", ("The economic order quantity model",
                     "One item is drawn from stock at a constant <strong>demand rate</strong> "
                     "`D` per unit time. Replenishing costs a fixed <strong>ordering "
                     "cost</strong> `K` per order, whatever the size, and arrives all at "
                     "once the moment stock reaches zero. Carrying stock costs a "
                     "<strong>holding rate</strong> `h` per unit per unit time.",
                     "The decision is the <strong>order quantity</strong> `Q`. Orders are "
                     "placed every `Q/D` units of time, so the cost per unit time is "
                     "`C(Q) = K·D/Q + h·Q/2`: the first term is the ordering bill, the "
                     "second is the holding bill.")),
            ("p", "Read the two terms rather than the sum. `K·D/Q` is `D/Q` orders per unit "
                  "time at `K` each, and it falls as the batch grows. `h·Q/2` is the "
                  "holding rate times the average stock, and it rises. Neither can be made "
                  "small without making the other large, which is why there is an answer at "
                  "all: a cost with only one of those terms in it is minimised by ordering "
                  "everything at once, or by ordering nothing, and neither is a decision."),
            ("math", [
                "K = 100 per order,   D = 1200 a year,   h = 6 per unit per year",
                "",
                "   Q      ordering K·D/Q      holding h·Q/2       total",
                "  100        1200                 300             1500",
                "  150         800                 450             1250",
                "  200         600                 600             1200      equal halves",
                "  250         480                 750             1230",
                "  300         400                 900             1300",
                "  400         300                1200             1500",
                "",
                "  the total is least where the two columns meet, and only there",
            ]),
            ("p", "The panel samples that curve on exact rationals and draws the three "
                  "lines together, because the crossing IS the optimum and a reader should "
                  "watch the two halves meet rather than be told they do. Underneath it the "
                  "sawtooth redraws at whatever `Q` you pick, so the cycle length `Q/D` and "
                  "the average level `Q/2` move while you look at them."),
            ("h3", "Where the two halves cross"),
            ("thm", ("The economic order quantity",
                     "`K·D/Q = h·Q/2` rearranges to `Q² = 2KD/h`, so the crossing is at "
                     "`Q* = √(2KD/h)`. The cost there is `C* = √(2KDh)`, and the two halves "
                     "are each `√(2KDh)/2`.",
                     "That the crossing is the <em>minimum</em> rather than merely a "
                     "landmark is the content of the discriminant argument, and it is done "
                     "in the next lesson rather than asserted here.")),
            ("p", "Nothing above was differentiated. This path does not have calculus and "
                  "does not need it: the sibling lesson turns &ldquo;is there a quantity "
                  "costing at most `T`&rdquo; into a quadratic inequality and reads the "
                  "minimum off its discriminant, which is the same argument Algebra makes "
                  "in &ldquo;The Discriminant&rdquo; and &ldquo;Quadratic "
                  "Inequalities&rdquo;, applied to a cost."),
            ("example", ("A workshop whose answer is a whole number",
                         "At `K = 100`, `D = 1200`, `h = 6` the panel reports "
                         "`Q* = 200` and `C* = 1200`, split as `600` of ordering and `600` "
                         "of holding. Both are rational here &mdash; `2KD/h = 40000` and "
                         "`2KDh = 1440000` are perfect squares &mdash; so the panel says so "
                         "and every digit it prints is exact.",
                         "This is the only kind of instance on which a reader can check the "
                         "whole page by hand, which is why it is the one the lab opens "
                         "with. It is also, in the arithmetic sense, a coincidence.")),
            ("example", ("A bench whose answer is not",
                         "Switch the worked example to `K = 50`, `D = 600`, `h = 5` and "
                         "`2KD/h = 12000`, which is not a square. The panel now prints "
                         "`Q* = 20√30` and `C* = 100√30`, tags both as irrational, and puts "
                         "`109.5445` and `547.7226` beside them with the sentence that "
                         "names the rounding and the method &mdash; four places, from the "
                         "exact surd, by integer square root with three guard digits.",
                         "The cheapest WHOLE quantity there is `110`, and the panel finds "
                         "it by pricing every whole quantity rather than by rounding: `109` "
                         "really does cost more than `110`, `119405/218` against "
                         "`6025/11`, and that is a comparison of two fractions with no "
                         "decimal in it.")),
            ("h3", "How flat is flat"),
            ("p", "&ldquo;The cost curve is flat around the optimum&rdquo; is the sentence "
                  "every account of this model contains and almost none of them measures. "
                  "It is measurable. Order `t` times the best quantity and the cost is "
                  "`(t + 1/t)/2` times the minimum &mdash; substitute `t·Q*` into `C(Q)` "
                  "and every one of `K`, `D` and `h` cancels. The penalty for being out by "
                  "a factor is a property of the factor alone."),
            ("math", [
                "t        C(t·Q*)/C*      on K = 100, D = 1200, h = 6:  Q = t·200, cost",
                "",
                "  1/2        5/4                  100        1500",
                "  3/4       25/24                 150        1250",
                "    1          1                  200        1200",
                "  6/5       61/60                 240        1220",
                "    2        5/4                  400        1500",
                "",
                "  t and 1/t give the SAME ratio, so half the batch and twice the batch",
                "  cost the same 25% extra — the curve is symmetric in t, not in Q",
            ]),
            ("p", "So &ldquo;within a fraction `e` of the minimum&rdquo; is "
                  "`(t + 1/t)/2 ≤ 1 + e`, which is `t² − 2(1 + e)t + 1 ≤ 0`: a second "
                  "quadratic, with a second discriminant `4e(2 + e)`, whose roots are "
                  "`(1 + e) ± √(e(2 + e))`. At `e = 1/100` the discriminant is `201/2500` "
                  "and the ends of the band are `101/100 ± √201/100`. Those are irrational, "
                  "and the panel prints that exact form beside the decimals rather than "
                  "only the decimals."),
            ("p", "In quantities, on the worked instance, the band runs from `173.6451` to "
                  "`230.3549`: you may order 13.2% too little or 15.2% too much and still "
                  "be within one per cent of the best cost there is. Those two percentages "
                  "are the same on every instance the panel can be given, because they come "
                  "from `t` and `t` has no `K`, `D` or `h` in it. The two decimals are the "
                  "midpoints of rational brackets under `10⁻¹³` wide, so every digit shown "
                  "is a digit of the true number &mdash; a statement about the printing, "
                  "not a hope about it."),
            ("p", "Widen the tolerance and the band widens the way the ratio says it must: "
                  "5% of the minimum allows `145.9688` to `274.0312`, and 25% allows "
                  "exactly `100` to `400`. That last one is the one case where the ends come "
                  "out rational, and the panel switches its wording to say so: at `e = 1/4` "
                  "the roots are `1/2` and `2`, which is the same `5/4` seen from the other "
                  "side."),
            ("p", "What the model left out is a list worth keeping. Demand is constant and "
                  "known; the order arrives complete and instantly; nothing is ever short; "
                  "the price per unit does not depend on how much is bought, so it is a "
                  "constant `D·price` that no choice of `Q` can change and it is left out "
                  "of `C(Q)` altogether. The three lessons after this one put the last three "
                  "of those back, one at a time, and each one changes the answer."),
        ],
        "lab": ("inventory", {
            "mode": "eoq",
            "preset": "workshop",
            "panel_title": "Move Q off the optimum and watch how little the total cares",
            "panel_intro": "The two cost curves are sampled on exact rationals and drawn "
                           "with their total, so the crossing is visible rather than "
                           "asserted. The sawtooth beneath redraws at your `Q`. The shaded "
                           "band is every quantity costing at most the chosen percentage "
                           "more than the best one, and it comes from the discriminant of "
                           "`t² − 2(1 + e)t + 1` rather than from trying quantities until "
                           "one is close enough. The last row prices every whole quantity "
                           "in range, because a warehouse cannot order a surd.",
        }),
        "steps_title": "Working an instance from the three numbers",
        "steps_intro": "Four steps, and the fourth is the one that decides whether the first three were worth doing to four decimal places.",
        "steps": [
            ("Get K, D and h onto the same clock",
             "`D` is per unit time and `h` is per unit per unit time, and they must agree: "
             "a demand of 1200 a year with a holding rate quoted per month gives an answer "
             "wrong by a factor of `√12`. `K` has no time in it at all &mdash; it is per "
             "order &mdash; which is exactly why it is easy to misread."),
            ("Compute 2KD/h and look at it before taking the root",
             "If it is a perfect square the answer is a whole number and everything on the "
             "page is exact. If it is not, the answer is irrational and stays a surd: "
             "`20√30`, not `109.5445`. The decimal is for reading, and it is only ever "
             "produced at the last moment."),
            ("Check the crossing rather than the formula",
             "Price `K·D/Q*` and `h·Q*/2` separately. They must be equal, and if they are "
             "not, the arithmetic is wrong &mdash; this is a one-line check that needs no "
             "second formula, and it catches a mis-typed `h` immediately."),
            ("Round to something you can actually order, and price that",
             "Cases of twelve, a pallet of 200, a minimum of 500. Round the surd to the "
             "quantity you can buy, then price it: the band tells you in advance how much "
             "the rounding costs, and it is almost always less than a reader expects."),
            ("Ask which of the four assumptions your situation breaks",
             "Constant demand, instant arrival, no shortages, a price that does not depend "
             "on the quantity. Whichever one is false is the lesson you need next, and "
             "there is one for each."),
        ],
        "worked": {
            "title": "One instance priced by hand, and the band around it",
            "intro": [
                "`K = 100` per order, `D = 1200` a year, `h = 6` per unit per year. Every "
                "figure below is what the panel prints on that instance, and all of them "
                "are exact.",
            ],
            "lines": [
                "2KD/h = 2(100)(1200)/6 = 40000          Q* = √40000 = 200      exactly",
                "2KDh  = 2(100)(1200)(6) = 1440000       C* = √1440000 = 1200   exactly",
                "",
                "check the crossing:   K·D/Q* = 120000/200 = 600",
                "                      h·Q*/2 = 6(200)/2   = 600      equal, as it must be",
                "",
                "the flat bottom, from the second discriminant:",
                "",
                "  (t + 1/t)/2 ≤ 1 + e     ⟺     t² − 2(1 + e)t + 1 ≤ 0",
                "  discriminant 4e(2 + e);  at e = 1/100 that is 201/2500",
                "  ends  101/100 ± √201/100  =  0.8682…  and  1.1518…",
                "",
                "  in quantities:  173.6451 … 230.3549     13.2% below, 15.2% above",
                "  at e = 5/100:   145.9688 … 274.0312     27.0% below, 37.0% above",
                "  at e = 25/100:  100      … 400          exactly half Q* and twice Q*",
                "",
                "cheapest WHOLE quantity, by pricing every one of them: 200, at 1200",
            ],
            "after": [
                "The two percentages are the whole point of the exercise. They were "
                "produced without ever mentioning `K`, `D` or `h`, because the ratio "
                "`(t + 1/t)/2` does not contain them &mdash; so &ldquo;13.2% below, 15.2% "
                "above&rdquo; is the 1% band for every instance of this model, not for this "
                "one. Change the three inputs in the panel and watch those two numbers sit "
                "still while everything around them moves.",
                "The asymmetry is worth a second look. `13.2` and `15.2` are not equal, and "
                "yet half the quantity and twice the quantity cost the same. Both facts "
                "come from the same place: the ratio is symmetric under `t ⟼ 1/t`, which "
                "is a symmetry of multiplication rather than of addition, and a band that "
                "is symmetric in the factor cannot be symmetric in the difference.",
                "For a rehearsal, switch the panel to the bench example, `K = 50`, "
                "`D = 600`, `h = 5`. The first move is given: `2KD/h = 12000 = 400 × 30`, "
                "so `Q* = 20√30` and nothing about it is a whole number. Predict what "
                "happens to the two band percentages before you look, and then say why the "
                "cheapest whole quantity is `110` rather than `109`.",
            ],
        },
        "quiz_title": "The quantity, the crossing and the flat part",
        "quiz": [
            {"q": "Demand doubles and nothing else changes. What happens to the economic order quantity?",
             "a": ["It doubles", "It is multiplied by `√2`", "It is unchanged, because `D` cancels",
                   "It is halved, because orders become more frequent"],
             "c": 1,
             "why": "`Q* = √(2KD/h)`, so `D` enters under a root: doubling it multiplies "
                    "the answer by `√2` and not by `2`. The number of orders per unit time, "
                    "`D/Q*`, therefore also rises by `√2` rather than staying put &mdash; "
                    "which is the useful form of the same fact. `D` does not cancel; it "
                    "cancels out of the flatness ratio, which is a different statement."},
            {"q": "On an instance with `Q* = 200` and `C* = 1200`, what does ordering `400` cost?",
             "a": ["`1200`, because the curve is flat", "`1500`", "`2400`", "`1250`"],
             "c": 1,
             "why": "`t = 2`, so the ratio is `(2 + 1/2)/2 = 5/4` and the cost is "
                    "`5/4 × 1200 = 1500`. Ordering `100` costs the same `1500`, because "
                    "`t = 1/2` gives the same ratio. &ldquo;Flat&rdquo; means a 1% penalty "
                    "over a band roughly `±14%` wide, not that doubling the batch is free."},
            {"q": "The panel reports `Q* = 20√30 ≈ 109.5445` and separately that the cheapest whole quantity is `110`. Why does it price every whole quantity instead of rounding the surd?",
             "a": ["Because rounding a surd is not defined", "Because the cost curve is not symmetric about `Q*`, so the nearer integer is a claim that has to be checked",
                   "Because `110` is nearer to `109.5445` than `109` is", "Because the surd is only an approximation to the real optimum"],
             "c": 1,
             "why": "The nearer integer usually is the answer, and here it is &mdash; but "
                    "&ldquo;usually&rdquo; is the problem. The curve rises more slowly above "
                    "`Q*` than below it, so the cheaper of the two neighbours is a fact "
                    "about the instance. The lab checks it by pricing both, and the "
                    "comparison `119405/218` against `6025/11` is exact. The surd is not an "
                    "approximation to anything: it is the exact optimum of the model."},
            {"q": "Which quantity on the panel is genuinely irrational on the instance `K = 100`, `D = 1200`, `h = 6`?",
             "a": ["`Q*`, which is `200`", "`C*`, which is `1200`", "The two ends of the 1% band, `173.6451` and `230.3549`",
                   "The cost at `Q = 250`, which is `1230`"],
             "c": 2,
             "why": "`40000` and `1440000` are perfect squares, so `Q*` and `C*` come out "
                    "rational on this particular instance and the panel says so. The band "
                    "ends do not: they are `101/100 ± √201/100` times `Q*`, and `201` is "
                    "not a square. Every cost at a rational `Q` is a ratio of whole numbers, "
                    "which is why `1230` is exact."},
        ],
        "mistakes": [
            ("Charging holding cost on the whole batch",
             "The batch is `Q` only at the instant it arrives. Averaged over the cycle the "
             "level is `Q/2`, and using `h·Q` instead of `h·Q/2` reports an order quantity "
             "`√2` too small and a cost `√2` too large. The sawtooth in the panel is there "
             "to make the halving something you can see rather than a factor to remember."),
            ("Hearing “flat” as “anything will do”",
             "The band is finite and it is computed. Within 1% of the minimum the order "
             "quantity may move 13.2% down or 15.2% up &mdash; a real tolerance, and a good "
             "argument for rounding to a pallet &mdash; but `t = 2` costs 25% more and "
             "`t = 5` costs 160% more. Flat near the bottom is not flat everywhere, and "
             "the panel will draw you the difference at any tolerance you like."),
            ("Quoting the decimal as the answer",
             "`109.5445` is not the economic order quantity; `20√30` is, and the decimal is "
             "that surd rounded to four places for reading. The distinction matters as soon "
             "as the number is used again: comparing two plans by their decimals can invert "
             "the comparison, which is exactly why the lab compares surd-valued costs by "
             "squaring rather than by printing."),
        ],
        "standard": ("Finish when you can say what it costs to be wrong, not only what the right answer is.",
                     "You should be able to write `C(Q)` from a described situation, derive "
                     "`Q* = √(2KD/h)` by setting the two halves equal, say why the crossing "
                     "is the minimum and where that is proved, keep an irrational answer as "
                     "a surd and name what rounding does to it, and compute the band of "
                     "quantities within a given percentage of the best cost &mdash; "
                     "including the fact that the band does not depend on the data."),
        "note": "The crossing is where the minimum is; it is not yet a proof that it is a minimum. The next lesson asks the question the other way round &mdash; &ldquo;is there a quantity costing at most `T`&rdquo; &mdash; and gets the whole answer, existence and optimality together, out of one discriminant.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-order-quantity-as-a-discriminant",
        "title": "The Order Quantity as a Discriminant",
        "module": "The order quantity",
        "one_line": "Ask for a budget instead of an optimum, and the whole answer falls out of a quadratic whose two roots collide.",
        "summary": (
            "&ldquo;Minimise the cost&rdquo; needs calculus. &ldquo;Is there an order "
            "quantity costing at most `T`&rdquo; needs a quadratic: multiply "
            "`K·D/Q + h·Q/2 ≤ T` through by `Q` and it becomes "
            "`h·Q²/2 − T·Q + K·D ≤ 0`, which holds exactly between the two roots. Lower "
            "`T` and the roots move together; they meet when the discriminant reaches "
            "exactly zero, and the single quantity left at that moment is the economic "
            "order quantity. Existence, uniqueness and optimality arrive together, and "
            "nothing is differentiated."
        ),
        "key": [
            "K·D/Q + h·Q/2 ≤ T   and Q > 0   ⟺   h·Q²/2 − T·Q + K·D ≤ 0",
            "leading coefficient h/2 > 0, so the parabola is at or below zero BETWEEN its roots",
            "discriminant  T² − 2hKD:   positive ⟹ an interval,  zero ⟹ one point,  negative ⟹ nothing",
            "it is zero at T = √(2hKD) = C*, and the merged root is T/h = √(2KD/h) = Q*",
            "on K = 100, D = 1200, h = 6:   3Q² − T·Q + 120000 ≤ 0,   2hKD = 1440000",
            "T = 1300 ⟹ roots 400/3 and 300;   T = 1200 ⟹ 200 twice;   T = 1199 ⟹ none",
        ],
        "key_label": "One inequality, one discriminant, and three things it can say",
        "concepts_intro": (
            "Three ideas. The first is the change of question that makes the algebra "
            "possible, the second is the step that has a condition attached, and the third "
            "is what the collision actually proves."
        ),
        "concepts": [
            ("A feasibility question is easier than an optimisation question",
             "&ldquo;What is the smallest cost&rdquo; is a search over all quantities. "
             "&ldquo;Is there a quantity costing at most `T`&rdquo; is a yes-or-no question "
             "about one inequality, and inequalities in one variable with a squared term in "
             "them are something Algebra already solves. Lowering `T` until the answer "
             "turns from yes to no is then a complete method, and the turning point is "
             "exact rather than approached."),
            ("Multiplying an inequality by Q is legal here for a reason worth stating",
             "Multiplying both sides by a negative number reverses an inequality. The step "
             "from `K·D/Q + h·Q/2 ≤ T` to `h·Q²/2 − T·Q + K·D ≤ 0` multiplies by `Q`, and "
             "it keeps the direction only because an order quantity is positive. That is "
             "not pedantry: it is the one place in this derivation where a condition on the "
             "variable is doing real work, and the lab refuses a zero or negative `Q` for "
             "the same reason."),
            ("A double root is a proof, not a coincidence",
             "While the discriminant is positive there are many quantities cheap enough, "
             "and the budget is not tight. When it is negative there are none, and the "
             "budget is impossible. Exactly one budget separates those two cases, the "
             "interval of affordable quantities has shrunk to a single point there, and "
             "that point is therefore the unique cheapest quantity. Nothing else can be: "
             "any cheaper one would make the discriminant negative and it would not exist."),
        ],
        "read_title": "The budget question, and what its discriminant says",
        "read_intro": "The rearrangement, the three regimes of the discriminant, and the collision that produces the answer.",
        "body": [
            ("p", "Fix the model and ask a different question. Instead of &ldquo;what is the "
                  "cheapest order quantity&rdquo;, ask &ldquo;is there an order quantity "
                  "costing at most `T` per unit time&rdquo;. That is "
                  "`K·D/Q + h·Q/2 ≤ T` with `Q > 0`, and multiplying through by the "
                  "positive quantity `Q` turns it into a polynomial inequality:"),
            ("math", [
                "      K·D/Q + h·Q/2  ≤  T                 Q > 0",
                "",
                "  ⟺   K·D + h·Q²/2   ≤  T·Q              multiply by Q, which is positive",
                "",
                "  ⟺   h·Q²/2 − T·Q + K·D  ≤  0            a quadratic in Q",
                "",
                "  leading coefficient h/2 > 0  ⟹  the parabola opens upward,",
                "  so it is at or below zero exactly BETWEEN its roots, and nowhere else",
            ]),
            ("def", ("The budget discriminant",
                     "For the quadratic `h·Q²/2 − T·Q + K·D` the "
                     "<strong>discriminant</strong> is "
                     "`T² − 4·(h/2)·(K·D) = T² − 2hKD`. Its sign decides everything:",
                     "positive, and there is an interval of order quantities meeting the "
                     "budget; zero, and there is exactly one; negative, and there is none "
                     "&mdash; the parabola never reaches the axis and no quantity is that "
                     "cheap.")),
            ("p", "So the budget can be walked down. Each step is a fresh quadratic with a "
                  "fresh discriminant, and the interval of affordable quantities closes as "
                  "the budget tightens. The panel does exactly that, on `K = 100`, "
                  "`D = 1200`, `h = 6`, where the quadratic is `3Q² − T·Q + 120000` and "
                  "`2hKD = 1440000`."),
            ("math", [
                "  budget T    T² − 2hKD        roots of 3Q² − T·Q + 120000        width",
                "",
                "    1920        2246400        320 ± 40√39   ≈  70.20 … 569.80    499.600",
                "    1680        1382400        280 ± 80√6    ≈  84.04 … 475.96    391.918",
                "    1440         633600        240 ± 40√11   ≈ 107.34 … 372.67    265.330",
                "    1320         302400        220 ± 20√21   ≈ 128.35 … 311.65    183.303",
                "    1300         250000        400/3 and 300      exactly         500/3",
                "    1260         147600        210 ± 10√41   ≈ 145.97 … 274.03    128.062",
                "    1200              0        200, twice                              0",
                "    1199          −2399        none: the parabola misses the axis",
            ]),
            ("h3", "The collision, and what survives it"),
            ("thm", ("The economic order quantity, from a double root",
                     "`T² − 2hKD = 0` exactly when `T = √(2hKD)`. At that budget the two "
                     "roots coincide at `Q = T/h = √(2hKD)/h = √(2KD/h)`.",
                     "No smaller budget is met by any quantity, since the discriminant is "
                     "then negative; and that single `Q` meets this one. So `√(2hKD)` is "
                     "the least achievable cost and `√(2KD/h)` is the unique quantity "
                     "achieving it.")),
            ("p", "That is the whole derivation. It uses the quadratic formula, the sign of "
                  "a leading coefficient, and the fact that a positive variable may be "
                  "multiplied through an inequality. It proves existence, uniqueness and "
                  "optimality in one motion, and it never mentions a rate of change. Where "
                  "a calculus treatment differentiates `C(Q)`, sets the result to zero and "
                  "then checks a second derivative to rule out a maximum, this argument has "
                  "no second case to rule out: an upward parabola cannot be below zero "
                  "outside its roots."),
            ("example", ("A budget that is not tight",
                         "Set `T = 1300` on the worked instance. The discriminant is "
                         "`1300² − 1440000 = 250000`, a perfect square, and the roots are "
                         "`400/3` and `300` exactly. Every order quantity between them "
                         "costs at most `1300`: the panel prices `134`, `200` and `299` "
                         "and all three clear the budget, while `133` and `301` do not.",
                         "Both endpoints cost exactly `1300` &mdash; they are where the "
                         "cost curve crosses the budget line &mdash; so the interval is "
                         "closed at both ends, which is what `≤` in the original question "
                         "asked for.")),
            ("example", ("A budget one unit too tight",
                         "`T = 1199` gives `1199² − 1440000 = −2399`. The parabola "
                         "`3Q² − 1199Q + 120000` stays strictly above the axis, and the "
                         "panel draws it in red with no shaded interval at all.",
                         "This is the informative failure. The answer is not &ldquo;the "
                         "arithmetic went wrong&rdquo; but &ldquo;no order quantity "
                         "whatsoever costs as little as 1199 per unit time on this "
                         "data&rdquo;, and the discriminant is the proof of it.")),
            ("h3", "The same quadratic, read as a tolerance"),
            ("p", "Setting the budget as a percentage of `C*` connects this page to the "
                  "flat band of &ldquo;The Economic Order Quantity&rdquo;, because they are "
                  "the same interval computed two ways. At `T = 1260`, which is 105% of "
                  "`1200`, the roots are `210 ± 10√41 ≈ 145.9688 … 274.0312`; the flatness "
                  "band at a 5% tolerance is `145.9688 … 274.0312`. At 110% the roots are "
                  "`220 ± 20√21 ≈ 128.3485 … 311.6515` and the 10% band is `128.3485 … "
                  "311.6515`. One is a discriminant in `Q`, the other a discriminant in "
                  "`t`, and they agree because they are the same question."),
            ("p", "The panel's budget slider is a percentage of `C*`, and where `C*` is "
                  "irrational that percentage is applied to a rounded decimal of it. The "
                  "argument itself never touches that decimal &mdash; it runs on whatever "
                  "rational `T` the slider produced &mdash; but it does mean that on an "
                  "irrational instance the 100% row is very close to a merge rather than "
                  "exactly one, and the panel says so rather than pretending the roots met. "
                  "On the worked instance `C* = 1200` exactly, so the merge really is a "
                  "merge and the discriminant prints as exactly zero."),
            ("p", "One consequence is worth carrying into the rest of the course. The width "
                  "of the affordable interval shrinks to zero, but it shrinks slowly: at a "
                  "budget 5% above the minimum the interval is still 128 units wide out of "
                  "an optimum of 200. That is the flatness of the cost curve seen from "
                  "underneath, and it is why the models in the rest of this course can "
                  "afford to round their answers to a case size, a pallet or a whole "
                  "number of units."),
        ],
        "lab": ("inventory", {
            "mode": "discriminant",
            "preset": "workshop",
            "panel_title": "Walk the budget down and watch the interval close",
            "panel_intro": "The curve drawn is the quadratic `h·Q²/2 − T·Q + K·D`, not the "
                           "cost: the shaded strip is where it sits at or below zero, and "
                           "those are exactly the order quantities meeting the budget. "
                           "Lower `T` and the two roots move towards each other. The table "
                           "walks the budget down in steps so that the collision is "
                           "something you watch rather than something the page announces, "
                           "and the economic order quantity is nowhere assumed &mdash; it "
                           "is what is left when the interval closes.",
        }),
        "steps_title": "Running the discriminant argument on an instance",
        "steps_intro": "Five steps. The third is where most of the errors live, and it is the one that costs nothing to check.",
        "steps": [
            ("Write the budget question as an inequality in Q",
             "`K·D/Q + h·Q/2 ≤ T`. Not an equation: the question is whether anything is "
             "cheap enough, and the set of answers is generally an interval rather than a "
             "point."),
            ("Multiply by Q and say why the direction is preserved",
             "`Q > 0`, so the inequality keeps its direction and becomes "
             "`h·Q²/2 − T·Q + K·D ≤ 0`. Write the reason down. A reader who omits it has "
             "the right answer by accident and will lose it the first time a variable can "
             "be negative."),
            ("Check the sign of the leading coefficient before reading the roots",
             "`h/2 > 0`, so the parabola opens upward and the inequality holds BETWEEN the "
             "roots. If it opened downward the solution set would be everything outside "
             "them &mdash; two rays, no bounded interval, and no collision to find."),
            ("Compute T² − 2hKD and read its sign",
             "Positive: an interval of affordable quantities, ends at "
             "`(T ± √(T² − 2hKD))/h`. Zero: exactly one, at `T/h`. Negative: none, and the "
             "budget is impossible rather than merely demanding."),
            ("Set the discriminant to zero to get the optimum",
             "`T = √(2hKD)` is the least achievable cost and `T/h = √(2KD/h)` is the "
             "quantity that achieves it. Keep both as surds; the decimal is a printing "
             "step, and doing it earlier makes the merge look approximate when it is not."),
        ],
        "worked": {
            "title": "One instance, five budgets, and the exact moment the interval closes",
            "intro": [
                "`K = 100`, `D = 1200`, `h = 6`, so the quadratic is "
                "`3Q² − T·Q + 120000` and `2hKD = 1440000`. Every root below is what the "
                "panel reports, and the surds are the panel's own.",
            ],
            "lines": [
                "budget T   discriminant T² − 1440000   roots                     verdict",
                "",
                "  1560           993600                260 ± 20√69               interval",
                "                                       ≈ 93.87 … 426.13",
                "  1300           250000                400/3 and 300             interval",
                "  1260           147600                210 ± 10√41               interval",
                "                                       ≈ 145.97 … 274.03",
                "  1200                0                200, a double root        THE OPTIMUM",
                "  1199            −2399                none                      impossible",
                "",
                "the merge:   T = √(2hKD) = √1440000 = 1200",
                "             Q = T/h     = 1200/6   = 200 = √(2KD/h) = √40000",
                "",
                "check it against the cost function, which was never used above:",
                "             C(200) = 120000/200 + 6(200)/2 = 600 + 600 = 1200   ✓",
            ],
            "after": [
                "The last line is the only place the cost function appears, and it is a "
                "check rather than a step. Everything above it came from factorising a "
                "quadratic, which is why the argument survives the path's promise of no "
                "calculus: `1200` and `200` were produced by the discriminant and then "
                "confirmed by the thing they are supposed to minimise.",
                "Notice that `T = 1300` gives rational roots and `T = 1260` does not, on "
                "the same instance. Whether the ends of the interval are nice has nothing "
                "to do with whether the optimum is: `1300² − 1440000 = 250000 = 500²` is "
                "luck, while `1200² − 1440000 = 0` is the theorem. A page that printed both "
                "as decimals would have hidden the difference.",
                "For a rehearsal, take `K = 50`, `D = 600`, `h = 5`, where `2hKD = 300000` "
                "and `C* = 100√30`. The first move is given: the merge budget is irrational, "
                "so the panel's percentage slider is working from a rounded `547.7226` and "
                "the 100% row shows a very small positive discriminant instead of zero. "
                "Say what the two roots look like just before they meet, and why the panel "
                "is right to report that rather than to round the discriminant to zero.",
            ],
        },
        "quiz_title": "Signs, roots and what a collision proves",
        "quiz": [
            {"q": "Why does `K·D/Q + h·Q/2 ≤ T` become `h·Q²/2 − T·Q + K·D ≤ 0` rather than `≥ 0`?",
             "a": ["Because multiplying an inequality always preserves it",
                   "Because `Q > 0`, so multiplying by `Q` preserves the direction",
                   "Because `h/2` is positive", "Because the cost is being minimised rather than maximised"],
             "c": 1,
             "why": "Multiplying by a negative number reverses an inequality; multiplying by "
                    "a positive one does not. An order quantity is positive, so the step is "
                    "legal and the direction is kept. The sign of `h/2` matters at the next "
                    "step &mdash; it says the solution set is between the roots rather than "
                    "outside them &mdash; and has nothing to do with this one."},
            {"q": "On `K = 100`, `D = 1200`, `h = 6`, what does a budget of `1199` produce?",
             "a": ["An interval of very small quantities", "A single quantity, near `200`",
                   "A negative discriminant and no quantity at all", "Two roots that are complex conjugates and therefore two order quantities"],
             "c": 2,
             "why": "`1199² − 1440000 = −2399`, so the parabola never reaches the axis and "
                    "no order quantity costs as little as `1199` per unit time. Complex "
                    "roots are not order quantities: a quantity is a positive real number, "
                    "and &ldquo;the roots are complex&rdquo; is precisely the statement that "
                    "the budget cannot be met."},
            {"q": "What makes the double root the MINIMUM, rather than just a quantity the budget happens to allow?",
             "a": ["That the two roots are equal", "That any smaller budget has a negative discriminant, so no quantity meets it",
                   "That the cost function was checked at that point", "That the parabola is tangent to the axis there"],
             "c": 1,
             "why": "Tangency and equal roots are the same observation restated, and "
                    "checking the cost is a confirmation rather than a proof. The argument "
                    "is the comparison with every smaller budget: below `√(2hKD)` the "
                    "discriminant is negative and nothing at all is that cheap, so no "
                    "quantity can beat the one surviving at the boundary."},
            {"q": "At a budget 5% above the minimum the affordable interval on the worked instance runs from about `145.97` to about `274.03`. What does that width say?",
             "a": ["That the arithmetic has lost precision near the optimum",
                   "That the cost curve is flat near its minimum, measured from underneath",
                   "That the discriminant is a poor way to find the optimum",
                   "That there are two distinct local minima"],
             "c": 1,
             "why": "It is the flatness of the cost curve, read as a width rather than as a "
                    "slope: paying 5% more buys a tolerance of `128` units around an optimum "
                    "of `200`. It is the same interval the other lesson's band computes from "
                    "the discriminant of `t² − 2(1 + e)t + 1`, and the two agree to every "
                    "digit printed."},
        ],
        "mistakes": [
            ("Forgetting that the multiplication needs `Q > 0`",
             "The step is correct and the reason is load-bearing. Omit it and the same "
             "manipulation, applied to a variable that can be negative, silently flips an "
             "inequality &mdash; which is the single most common way a correct-looking "
             "algebraic argument produces a wrong feasible set. Say it out loud every time."),
            ("Reading the discriminant's sign backwards",
             "A positive discriminant means the budget is generous: two roots, an interval "
             "of quantities, room to spare. A negative one means the budget is impossible. "
             "It is easy to associate &ldquo;negative&rdquo; with &ldquo;small answer&rdquo; "
             "rather than with &ldquo;no answer&rdquo;, and the panel colours the parabola "
             "red in that case for exactly that reason."),
            ("Rounding the surd before the collision",
             "`√(2hKD)` is the budget at which the roots meet. Round it to four places "
             "first and the discriminant at that rounded value is a small non-zero number, "
             "the roots are two distinct quantities a few thousandths apart, and the merge "
             "&mdash; the whole argument &mdash; disappears into rounding. The lab keeps "
             "the surd and rounds only to print, and it tells you when the percentage "
             "slider has forced it to do otherwise."),
        ],
        "standard": ("Finish when a budget you cannot meet reads as a negative discriminant rather than as an error.",
                     "You should be able to turn a cost target into a quadratic inequality "
                     "with the positivity condition stated, read all three regimes off the "
                     "discriminant, locate the budget at which the roots merge, derive "
                     "`Q* = √(2KD/h)` and `C* = √(2KDh)` from that merge, and explain why "
                     "the collision proves optimality without any appeal to a rate of "
                     "change."),
        "note": "Everything so far has assumed the unit price is a constant, so that `D·price` is a term no choice of `Q` can move and can be left out of the cost. The next lesson removes that assumption: when the price depends on how much is ordered, the total-cost curve breaks into pieces and the cheapest plan is no longer the one nearest this quantity.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "all-units-price-breaks",
        "title": "All-Units Price Breaks",
        "module": "What changes the cycle",
        "one_line": "A discount that reprices the whole order makes the cost curve jump, so the cheapest plan is chosen band by band and compared without rounding.",
        "summary": (
            "Under all-units pricing, crossing a break reprices every unit in the order and "
            "not only the ones above it, so the total-cost curve drops by `D` times the "
            "price difference at each break. It is discontinuous, drawing it as one line "
            "asserts costs no quantity has, and the minimum is found band by band: each "
            "band contributes its own economic order quantity if that lands inside it, and "
            "its floor otherwise. The candidates are then compared exactly, because some "
            "of them are irrational and two decimals that differ are not a proof."
        ),
        "key": [
            "all-units:  the WHOLE order is priced at the band's price, not just the excess",
            "total(Q) = D·price(Q) + K·D/Q + h(Q)·Q/2        price and holding both step",
            "the curve DROPS by D·(p − p′) at a break: a step, not a slope",
            "one candidate per band: its own √(2KD/h) if inside, otherwise the band's floor",
            "K = 40, D = 1200, bands 0/10/2, 500/9/(9/5), 1000/8/(8/5)",
            "candidates 219.09 at 12000 + 80√30,  500 at 11346,  1000 at 10448  —  the last wins",
        ],
        "key_label": "A stepped price, a broken curve, and one candidate from each piece",
        "concepts_intro": (
            "Three ideas. The first is what &ldquo;all-units&rdquo; actually means, the "
            "second is why one candidate per band is enough, and the third is about the "
            "comparison rather than the candidates."
        ),
        "concepts": [
            ("All-units repricing makes the curve jump, and a jump is not a slope",
             "Buy 999 at ten each and the bill is 9990; buy 1000 at eight each and it is "
             "8000. One more unit made the order cheaper in total, which cannot happen if "
             "price is a smooth function of quantity. So the total-cost curve has a genuine "
             "discontinuity at every break, the panel draws one segment per band, and a "
             "single polyline joining them would assert costs that no order quantity has."),
            ("Within a band the curve is an ordinary EOQ curve, which is why one candidate is enough",
             "Fix the band and the price is constant, so `D·price` is a constant and the "
             "shape is `K·D/Q + h·Q/2` again: one minimum, falling to the left of it and "
             "rising to the right. If that band's own economic order quantity lies inside "
             "the band, it is the band's best. If it lies below the band, the curve is "
             "rising throughout the band and the floor is the best; if above, the ceiling "
             "is. Checking one quantity per band is therefore a complete search, and the "
             "lab still prices every whole quantity in range as a check on the claim."),
            ("The comparison is where the rounding would do damage",
             "A band's candidate cost is a rational purchase bill plus, where the candidate "
             "is that band's economic order quantity, an irrational `√(2KDh)`. Deciding "
             "which of two such numbers is smaller by printing both to four places and "
             "looking is a decision that can be wrong. The lab settles same-radicand pairs "
             "by one squaring and different-radicand pairs by rational brackets refined "
             "until they separate, so the winner is proved rather than observed."),
        ],
        "read_title": "A price that depends on the order, and what it does to the curve",
        "read_intro": "The pricing rule, the shape it produces, the rule for finding the minimum, and the comparison that decides between candidates.",
        "body": [
            ("def", ("All-units quantity discount",
                     "A price schedule is a list of <strong>breaks</strong>: a quantity at "
                     "which a band starts, the unit price in that band, and the holding "
                     "rate there. Under <strong>all-units</strong> pricing, an order of `Q` "
                     "in a band is charged that band's price on <em>every</em> unit.",
                     "The cost per unit time becomes "
                     "`D·price(Q) + K·D/Q + h(Q)·Q/2`. The purchase term now depends on `Q` "
                     "&mdash; which is exactly why it could be ignored in the plain model "
                     "and cannot be here.")),
            ("p", "The holding rate usually depends on the price, because holding cost is "
                  "commonly charged as a fraction of the value sitting on the shelf. In the "
                  "worked schedule it is 20% of price throughout: `2` at a price of ten, "
                  "`9/5` at nine, `8/5` at eight. That means each band has a different "
                  "economic order quantity, which is the second reason the bands must be "
                  "treated separately."),
            ("math", [
                "K = 40,  D = 1200.        bands, as  “from   price   holding”:",
                "",
                "      0    10    2            500    9    9/5           1000    8    8/5",
                "",
                "band   price   its own √(2KD/h)          inside the band?   candidate",
                "",
                "  1      10    √(96000/2)  = 40√30 ≈ 219.09     yes            219.09",
                "  2       9    √(96000/(9/5)) = (400/3)√3 ≈ 230.94   no, below   500",
                "  3       8    √(96000/(8/5)) = 100√6 ≈ 244.95       no, below  1000",
            ]),
            ("p", "Two of the three bands cannot have their own best quantity, because that "
                  "quantity is smaller than the band's floor. In those bands the cost curve "
                  "is rising from the floor onward, so the cheapest reachable point is the "
                  "floor itself &mdash; the smallest order that still qualifies for the "
                  "price. That is the usual situation, and it is why quantity discounts "
                  "work as a sales device: they are offers to buy more than you want at a "
                  "price that makes it worth it, or not."),
            ("h3", "Pricing the three candidates"),
            ("math", [
                "candidate   purchase D·price   cycle cost K·D/Q + h·Q/2   total",
                "",
                " 219.09        12000            80√30 ≈ 438.1780          12000 + 80√30",
                "                                                        ≈ 12438.1780",
                "    500        10800            96 + 450 = 546                11346",
                "   1000         9600            48 + 800 = 848                10448",
                "",
                "cheapest: 1000, at 10448 per unit time",
                "",
                "check, with no notion of a candidate in it: price every whole quantity",
                "from 1 to 1800 under the all-units rule.  Cheapest: 1000, at 10448.",
            ]),
            ("p", "The purchase bill is doing all the work. Moving from the first band to "
                  "the third saves `D·(10 − 8) = 2400` per unit time on purchases and costs "
                  "a few hundred in a larger cycle, which is not close. A reader who "
                  "compared only the cycle costs &mdash; `438.18`, `546`, `848` &mdash; "
                  "would pick exactly the wrong plan, and would do so on figures that are "
                  "all correct."),
            ("example", ("A discount that is not worth taking",
                         "Switch the panel to the two-band schedule: the same `K = 40` and "
                         "`D = 1200`, a price of ten below 900 and `39/4` at 900 and above, "
                         "with holding at 20% of price as before. The first band's candidate "
                         "is `40√30 ≈ 219.09` costing `12000 + 80√30 ≈ 12438.1780`; the "
                         "second band's is its floor, `900`, costing `75785/6 ≈ 12630.83`.",
                         "The deeper price loses. Buying 900 units at a time to save a "
                         "quarter each costs more in holding than it saves at the till, and "
                         "the panel's exhaustive scan of 1620 whole quantities agrees, "
                         "landing at `219` &mdash; below the break, where no discount "
                         "applies at all.")),
            ("h3", "Why the comparison is done on surds"),
            ("p", "The first band's candidate cost is `12000 + 80√30`. The third band's is "
                  "`10448`. Those are not the same kind of object: one is a rational plus an "
                  "irrational multiple of `√30`, the other is a whole number, and the lab "
                  "compares them by bracketing each with rationals and refining the brackets "
                  "until they separate. No decimal is compared with another decimal anywhere "
                  "in that. The decimal `12438.1780` appears on the page beside the exact "
                  "form, rounded to four places from the surd, with the sentence that names "
                  "the rounding &mdash; and the winner was decided before it was printed."),
            ("p", "This matters more than it looks. Two candidates in a real schedule can be "
                  "within a fraction of a per cent of each other, and a comparison that goes "
                  "through four-place decimals is a comparison that can be settled by the "
                  "rounding rather than by the costs. A pair sharing a radicand is settled by "
                  "one squaring &mdash; two rational totals share the radicand `1`, and their "
                  "comparison collapses to the sign of a difference, which is how `10448` "
                  "beats `11346` &mdash; while a pair that does not share one, which here is "
                  "any comparison involving the band whose candidate is its own economic "
                  "order quantity, is settled by refining rational brackets. Neither route "
                  "produces a decimal."),
            ("h3", "What the scan is for"),
            ("p", "&ldquo;One candidate per band&rdquo; is a rule, and a rule is a claim. "
                  "The panel prices every whole quantity in the drawn range under the "
                  "all-units schedule &mdash; 1800 of them on the three-band example, 1620 "
                  "on the two-band one &mdash; and reports whether the scan agrees with the "
                  "candidate rule to the nearest unit. It agrees on both, which is the only "
                  "kind of confirmation a scan of whole numbers can give about a candidate "
                  "that is a surd. If it ever disagreed the panel would say so in red rather "
                  "than printing the answer it preferred."),
            ("p", "The model has been extended in one way and left alone in every other. "
                  "Demand is still constant and known, the order still arrives all at once, "
                  "nothing is still ever short. What has changed is that the purchase bill "
                  "is now a decision variable, and the geometry of the answer changed with "
                  "it: a continuous curve with one minimum became a broken curve with one "
                  "candidate per piece."),
        ],
        "lab": ("inventory", {
            "mode": "discount",
            "preset": "threeband",
            "panel_title": "Set the bands and watch which candidate wins",
            "panel_intro": "Each band is drawn as its own segment, because joining them "
                           "would assert costs that no quantity has. Every band "
                           "contributes one candidate &mdash; its own economic order "
                           "quantity when that falls inside the band, its floor when it "
                           "does not &mdash; and the winner is chosen by exact comparison "
                           "of surd-valued costs. Beneath that, every whole quantity in "
                           "range is priced as an independent check on the rule, and the "
                           "panel reports whether the two agree.",
        }),
        "steps_title": "Choosing an order quantity against a price schedule",
        "steps_intro": "Five steps, and the fourth is the one that separates this from the plain model.",
        "steps": [
            ("Write the schedule down with its holding rates",
             "Each band needs a floor, a price and a holding rate. If holding is charged as "
             "a fraction of value, the rate differs band by band and each band has its own "
             "economic order quantity &mdash; leaving that out is the quiet error in this "
             "model, because the answer still looks plausible."),
            ("Compute each band's own EOQ with that band's holding rate",
             "`√(2KD/h)` with the band's `h`. Keep it as a surd. This is the quantity the "
             "band would want if the band went on forever in both directions."),
            ("Replace each unreachable EOQ by the nearest reachable quantity",
             "If the band's EOQ is below the band, use the floor; if above, use the "
             "ceiling; if inside, use it. Within a band the curve has one minimum, so the "
             "nearest reachable point to that minimum is the band's best &mdash; this is "
             "the whole justification for one candidate per band."),
            ("Price every candidate with its purchase bill included",
             "`D·price + K·D/Q + h·Q/2`. The purchase term is the one that makes the "
             "discount worth anything and it dwarfs the other two here: `9600` against "
             "`848` in the winning band. Comparing cycle costs alone inverts the answer."),
            ("Compare exactly, then round for reading",
             "Some totals carry a `√(2KDh)` and some do not. Settle the comparison on the "
             "exact forms, and only then print a decimal &mdash; labelled as rounded, "
             "beside the exact form it came from."),
        ],
        "worked": {
            "title": "Three bands, three candidates, and a scan that agrees",
            "intro": [
                "`K = 40`, `D = 1200`, holding at 20% of price. Bands start at `0`, `500` "
                "and `1000`, priced `10`, `9` and `8`. Everything below is what the panel "
                "reports on that schedule.",
            ],
            "lines": [
                "band  from   price   h      its own EOQ        reachable?   candidate",
                "",
                "  1      0     10     2     40√30 ≈ 219.09        yes         219.09…",
                "  2    500      9    9/5    (400/3)√3 ≈ 230.94    no          500",
                "  3   1000      8    8/5    100√6 ≈ 244.95        no         1000",
                "",
                "pricing them:",
                "",
                "  band 1   12000 + 80√30                     ≈ 12438.1780   (irrational)",
                "  band 2   10800 + 40(1200)/500 + (9/5)(500)/2",
                "         = 10800 + 96 + 450                  =  11346       (exact)",
                "  band 3    9600 + 40(1200)/1000 + (8/5)(1000)/2",
                "         =  9600 + 48 + 800                  =  10448       (exact)",
                "",
                "winner: band 3, ordering 1000 at a price of 8, for 10448 per unit time",
                "",
                "independent check: price all 1800 whole quantities from 1 to 1800",
                "under the all-units rule.  Cheapest is 1000, at 10448.   agrees",
            ],
            "after": [
                "The order of the three totals is the reverse of the order of the three "
                "candidate quantities, and that is the shape of the whole model: buying "
                "more is cheaper here because the saving is `D` times a price difference "
                "and it applies to every unit bought forever, while the extra holding is "
                "paid on half a batch. The step beats the slope, and it beats it by a wide "
                "margin.",
                "Exactly one of the three totals is irrational, and it is the one whose "
                "candidate is a genuine economic order quantity: `12000 + 80√30`, where "
                "`80√30 = √(2KDh)` with this band's `h = 2`. The other two candidates are "
                "band floors, whole numbers, so their totals are whole numbers too. The "
                "panel prints `12438.1780` beside the exact form with the rounding named, "
                "and the comparison that chose the winner never used it.",
                "For a rehearsal, keep `K` and `D` and change the third band's price from "
                "`8` to `19/2` with holding `19/10`. The supplied first move is that the "
                "purchase saving against the first band falls from `2400` to `600` per unit "
                "time. Predict whether band 3 still wins before you type it, and say which "
                "of the two comparisons the lab would then have to settle by bracket "
                "refinement rather than by a sign.",
            ],
        },
        "quiz_title": "Steps, bands and exact comparisons",
        "quiz": [
            {"q": "Why is the total-cost curve under all-units pricing drawn as one segment per band rather than as a single line?",
             "a": ["To colour the winning band differently", "Because the curve is genuinely discontinuous at each break, and a joining line would assert costs no quantity has",
                   "Because each band has a different holding rate", "Because the bands have different widths"],
             "c": 1,
             "why": "Crossing a break reprices every unit, so the total drops by `D` times "
                    "the price difference at that point &mdash; a step. The different "
                    "holding rates change the shape within each band but do not create the "
                    "jump; repricing the whole order does. Drawing a segment from the "
                    "left-hand value to the right-hand one would place a line through costs "
                    "that no order quantity has."},
            {"q": "A band's own economic order quantity works out at `230.94`, and the band runs from `500` upward. What is that band's candidate?",
             "a": ["`230.94`, since that is the quantity minimising its cost",
                   "`500`, because the curve rises throughout the band and the floor is the nearest reachable point",
                   "The band has no candidate and is skipped",
                   "The midpoint of the band"],
             "c": 1,
             "why": "Within the band the shape is an ordinary EOQ curve whose minimum lies "
                    "to the left of the band, so the curve is rising from `500` onward and "
                    "the floor is the cheapest reachable quantity. Skipping the band would "
                    "be wrong: on the worked schedule the winning candidate is exactly such "
                    "a floor."},
            {"q": "Comparing candidate totals of `12000 + 80√30` and `10448`, why does the lab refuse to compare `12438.1780` with `10448.0000`?",
             "a": ["Because the decimals have different numbers of digits",
                   "Because a comparison of two rounded decimals can be settled by the rounding rather than by the costs",
                   "Because `√30` cannot be approximated",
                   "Because the two totals are in different units"],
             "c": 1,
             "why": "On this pair the gap is large and any method would get it right. The "
                    "rule exists for the pairs that are close, where four places is not "
                    "enough to separate two costs and the printed digits decide the answer "
                    "instead of the arithmetic. `√30` approximates perfectly well; the point "
                    "is that the decision is made on the exact forms and the decimal is "
                    "produced afterwards, for reading."},
            {"q": "The panel also prices every whole quantity from 1 to 1800 and reports whether the scan agrees with the candidate rule. What does that add?",
             "a": ["A faster way to find the answer",
                   "A check on the rule itself, from a computation with no notion of a candidate in it",
                   "The exact answer, since the scan considers more quantities",
                   "Nothing, since the scan and the rule are the same computation"],
             "c": 1,
             "why": "&ldquo;One candidate per band&rdquo; is a claim about where the minimum "
                    "can be, and the scan is an independent computation that can refute it. "
                    "It is not more exact &mdash; it only looks at whole numbers, and a "
                    "candidate can be a surd &mdash; and it is much slower. What it can do "
                    "is disagree, and the panel is built to report that in red rather than "
                    "quietly print the answer it prefers."},
        ],
        "mistakes": [
            ("Pricing only the units above the break",
             "That is incremental pricing, a different schedule with a continuous cost "
             "curve and a different answer. All-units means the whole order takes the new "
             "price, which is why the curve jumps and why buying up to a break can be worth "
             "it. Read the contract before choosing the model: the two are easy to confuse "
             "in words and produce visibly different plans."),
            ("Using one holding rate for every band",
             "When holding is charged as a fraction of value, a cheaper price means a "
             "cheaper unit to hold, so each band has its own `h` and its own economic order "
             "quantity. Carrying the first band's rate through all of them gives candidates "
             "that are wrong in each band and a comparison between them that is wrong in a "
             "way no scan of the same wrong model would reveal."),
            ("Comparing cycle costs and forgetting the purchase bill",
             "On the worked schedule the cycle costs are `438.18`, `546` and `848` and the "
             "totals are `12438.18`, `11346` and `10448`: the cheapest cycle belongs to the "
             "most expensive plan. The purchase term `D·price` is the entire reason a "
             "discount exists, and leaving it out of the comparison reliably chooses the "
             "smallest order quantity, which is reliably the wrong one."),
        ],
        "standard": ("Finish when a schedule of price breaks reads as a list of candidates rather than as a single formula.",
                     "You should be able to state what all-units pricing charges, say why "
                     "that makes the cost curve discontinuous, compute each band's own "
                     "economic order quantity with that band's holding rate, replace an "
                     "unreachable one by the band floor or ceiling and justify the "
                     "replacement, and compare candidate totals exactly &mdash; naming "
                     "which of them is irrational and why."),
        "note": "The purchase price was the first of the plain model's assumptions to go. The next lesson removes two more at once: that an order arrives all at once, and that stock is never allowed to run out. Both turn out to be the same correction applied in two places, and the panel shows one sawtooth changing shape as each is switched on.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "production-runs-and-planned-backorders",
        "title": "Production Runs and Planned Backorders",
        "module": "What changes the cycle",
        "one_line": "A run that takes time and a shortage you chose to allow are the same correction applied twice, and one formula covers both.",
        "summary": (
            "Replenishment is rarely instantaneous and shortages are not always a failure. "
            "If stock is produced at a finite rate `P` while demand `D` continues, it "
            "builds only at `P − D`, so the effective holding rate is scaled by `1 − D/P`. "
            "If a backorder costs `π` per unit per unit time, carrying a unit short is "
            "cheaper than carrying it in stock and the holding rate is divided again by "
            "`(h + π)/π`. Those are the only two changes: the economic production quantity "
            "and the backorder model are one formula with two switches."
        ),
        "key": [
            "finite production rate:   effective holding rate  h·(1 − D/P)",
            "planned backorders:       divide again by (h + π)/π",
            "Q* = √( 2KD / (h(1 − D/P)) · (h + π)/π )      both switches, one expression",
            "at a fixed Q the best backorder level is b = (1 − D/P)·Q·h/(h + π), a rational",
            "K = 100, D = 1200, h = 6, P = 2400, π = 6:  factors 1/2 and 2, Q* = 400, C* = 600",
            "each switch alone multiplies Q* by √2:  200 → 200√2 ≈ 282.843 → 400",
        ],
        "key_label": "Two corrections to one holding rate, and what each does to the answer",
        "concepts_intro": (
            "Three ideas, and the third is the one that decides whether this model has an "
            "answer at all."
        ),
        "concepts": [
            ("Stock builds at the difference between the rates, not at the production rate",
             "While the machine runs, demand keeps drawing stock away, so the level climbs "
             "at `P − D` rather than at `P`. The run lasts `Q/P` of the cycle and the peak "
             "reached is `(1 − D/P)·Q`, not `Q`. Average stock is half that peak, so every "
             "holding term in the plain model is multiplied by `1 − D/P` &mdash; a factor "
             "between zero and one that is the whole of the production correction."),
            ("A planned shortage is a cheaper place to keep a unit",
             "If stock costs `h` to hold and a backorder costs `π`, the cycle splits into a "
             "part spent in stock and a part spent short, and the model chooses the split. "
             "The arithmetic comes out as a second scaling of the holding rate, by "
             "`π/(h + π)`, which is smaller than one whenever backorders are penalised at "
             "all. A big `π` makes shortages expensive and the factor approaches one; the "
             "model stops planning them and becomes the previous one."),
            ("Zero penalty is not a small penalty, and a slow machine is not a small machine",
             "With `π = 0` every unit backordered is free, so the cheapest plan is to "
             "backorder everything forever and there is no finite answer &mdash; the panel "
             "says the model has run out rather than printing a number. With `P ≤ D` the "
             "factor `1 − D/P` is zero or negative, the machine can never build stock, and "
             "there is no cycle to optimise. Both are refusals rather than edge cases, and "
             "both are informative."),
        ],
        "read_title": "One sawtooth, two switches",
        "read_intro": "What a finite production rate does to the picture, what a planned shortage does to it, and why the two combine into a single formula.",
        "body": [
            ("p", "The plain model draws a vertical rise: a batch of `Q` appears and the "
                  "level falls in a straight line to zero. Two of its assumptions are worth "
                  "removing, and they turn out to change the same thing."),
            ("def", ("The economic production quantity",
                     "Stock is produced at a constant rate `P > D` while demand continues "
                     "at `D`. The level therefore climbs at `P − D` for the `Q/P` of the "
                     "cycle in which the machine runs, peaks at "
                     "`(1 − D/P)·Q`, and then falls at `D`.",
                     "Average stock over the cycle is half that peak, so the holding cost "
                     "is `h·(1 − D/P)·Q/2`. Everything else is unchanged, which means the "
                     "answer is the plain economic order quantity computed with a holding "
                     "rate of `h·(1 − D/P)`.")),
            ("def", ("Planned backorders",
                     "Shortages are permitted and cost `π` per unit per unit time "
                     "backordered. A cycle now spends part of its time with stock on hand "
                     "and part of it short by up to `b`, the planned "
                     "<strong>backorder level</strong>.",
                     "At a fixed order quantity the cost is a quadratic in `b` whose "
                     "minimum is at `b = (1 − D/P)·Q·h/(h + π)`, and minimising over `Q` "
                     "as well divides the effective holding rate by a further "
                     "`(h + π)/π`.")),
            ("p", "So there is one formula and it has two switches. Set `P` to infinity and "
                  "the first factor is one; set `π` to infinity and the second is one; do "
                  "both and it is the plain economic order quantity. The panel puts all four "
                  "readings in one table, each produced by the same function with different "
                  "arguments, so that they are visibly one result rather than four to "
                  "memorise."),
            ("math", [
                "K = 100,   D = 1200,   h = 6,   P = 2400,   π = 6",
                "",
                "   1 − D/P = 1/2            (h + π)/π = 2",
                "",
                "  model                                 1−D/P  (h+π)/π    Q*        C*",
                "",
                "  plain EOQ (P infinite, no shortages)     1       1      200      1200",
                "  production quantity (finite P)          1/2      1    200√2      600√2",
                "                                                       ≈ 282.843  ≈ 848.528",
                "  EOQ with backorders (P infinite)         1       2    200√2      600√2",
                "                                                       ≈ 282.843  ≈ 848.528",
                "  both at once                            1/2      2      400       600",
            ]),
            ("p", "The two middle rows are the same pair of numbers, and that is not a "
                  "typing error. Each switch on its own multiplies the effective holding "
                  "rate by `1/2` here, and the answer depends on the holding rate alone: "
                  "halving it multiplies `Q*` by `√2` and divides `C*` by `√2`. Applying "
                  "both quarters the rate, so `Q*` doubles to `400` and `C*` halves to "
                  "`600`. A finite machine and a tolerated shortage are, on this instance, "
                  "interchangeable."),
            ("p", "On this instance `Q* = 400` and `C* = 600` are rational and every digit "
                  "of them is exact. The two middle rows are not: `200√2` and `600√2` are "
                  "irrational, and the table prints them as surds with `282.843` and "
                  "`848.528` beside them, rounded to three places. Change the production "
                  "rate to `12000` and the penalty to `3` and the headline pair becomes "
                  "irrational too &mdash; `(200/3)√30` and `120√30` &mdash; at which point "
                  "the panel tags them and prints the sentence naming the rounding."),
            ("h3", "The backorder level, at a quantity you chose"),
            ("p", "The panel prints the best backorder level at the run size YOU set, not at "
                  "`Q*`. That is deliberate. At a fixed rational `Q` the cost is a quadratic "
                  "in `b` with rational coefficients, so its vertex "
                  "`b = (1 − D/P)·Q·h/(h + π)` is a rational number and can be printed "
                  "exactly. At an irrational `Q*` the same expression is irrational, and "
                  "printing a rounded backorder level beside an exact run size would be "
                  "mixing two kinds of number in one sentence."),
            ("example", ("Four hundred units a run, and a hundred of them owed",
                         "At `Q = 400` on the worked instance the best backorder level is "
                         "`(1/2)(400)(6)/12 = 100`, and the cost there is `600` per unit "
                         "time &mdash; which is also `C*`, because `400` happens to be "
                         "`Q*` on this instance.",
                         "Move `b` either side and the cost rises: `99` and `101` both cost "
                         "`60003/100`, three hundredths more, and `b = 0` &mdash; refusing "
                         "to plan any shortage at all &mdash; costs `900`. Refusing to be "
                         "short costs half as much again as planning it, because a "
                         "backordered unit is not occupying a warehouse.")),
            ("h3", "Where the model refuses"),
            ("example", ("A machine that cannot keep up",
                         "Set `P = 1200` against `D = 1200`. The factor `1 − D/P` is zero, "
                         "the stock level never rises, and the panel reports that there is "
                         "no cycle to optimise rather than dividing by zero and printing "
                         "something.",
                         "This is a modelling statement, not an arithmetic one. A machine "
                         "that cannot outpace demand does not have a run size problem; it "
                         "has a capacity problem, and the answer is to raise `P`, not to "
                         "choose `Q` more carefully.")),
            ("example", ("A shortage that costs nothing",
                         "Set `π = 0`. Every unit backordered is free, so the cheapest "
                         "policy is to hold no stock at all and owe everybody forever. "
                         "There is no finite optimum, and the panel says the model has run "
                         "out.",
                         "The useful reading is that `π` is not a nuisance parameter to "
                         "leave at zero. It is the price of a promise, and a model with no "
                         "price on a broken promise will always recommend breaking it.")),
            ("p", "Both refusals share a shape with the negative discriminant of the "
                  "sibling lesson &ldquo;The Order Quantity as a Discriminant&rdquo;: the "
                  "arithmetic is not failing, the model is reporting that the question has "
                  "no answer as posed. Those are the most useful outputs an inventory model "
                  "produces, because they are the ones a spreadsheet silently converts into "
                  "a plausible number."),
            ("p", "What is still assumed is the thing the rest of the course removes. "
                  "Demand is constant and known. Everything so far &mdash; the quantity, "
                  "the discount, the run, the planned shortage &mdash; has been a decision "
                  "made against a rate that never varies. The remaining lessons put a "
                  "probability distribution where that rate was, and the question changes "
                  "from &ldquo;how much&rdquo; to &ldquo;how much, given that you do not "
                  "know&rdquo;."),
        ],
        "lab": ("inventory", {
            "mode": "epq",
            "preset": "machine",
            "panel_title": "Turn each effect on and watch the sawtooth change shape",
            "panel_intro": "The top picture is stock over three cycles: a finite production "
                           "rate tilts the rise, and a planned shortage drops the whole "
                           "shape below the axis. Beneath it is the cost against run size, "
                           "with the backorder level already at its best for each one. The "
                           "table is four models produced by one function with different "
                           "switches, and the backorder level is reported at the run size "
                           "you set &mdash; where the answer is rational and exact.",
        }),
        "steps_title": "Setting a run size and a backorder level",
        "steps_intro": "Four steps, and the first is the one that decides whether the other three are worth doing.",
        "steps": [
            ("Check that P exceeds D before anything else",
             "`1 − D/P` must be positive. If it is not, there is no cycle and no run size: "
             "the machine cannot build stock and the model has nothing to say. This is one "
             "comparison and it costs nothing, and it is the same discipline as adding the "
             "supplies before solving a network."),
            ("Scale the holding rate once for each effect that applies",
             "Multiply `h` by `1 − D/P` if production takes time. Multiply again by "
             "`π/(h + π)` if shortages are allowed and penalised. Then run the plain "
             "economic order quantity on the scaled rate &mdash; there is no second formula "
             "to learn."),
            ("Take the root last, and keep it as a surd",
             "`Q* = √(2KD/h_effective)` and `C* = √(2KD·h_effective)`. Whether they come "
             "out rational depends on the data, and the model does not care; what matters "
             "is that a rounded decimal is never fed into the next step."),
            ("Compute the backorder level at the quantity you will actually run",
             "`b = (1 − D/P)·Q·h/(h + π)` at a rational `Q` is a rational number. Verify it "
             "is the vertex by pricing `b − 1` and `b + 1`: both must cost more, and if "
             "they do not the arithmetic is wrong."),
            ("Say what you have promised about shortages",
             "A planned backorder level is a commitment to run out, on purpose, by a stated "
             "amount. It is defensible when `π` is a real cost that somebody has agreed to; "
             "it is not defensible when `π` was set to make the answer come out, and no "
             "amount of correct arithmetic afterwards fixes that."),
        ],
        "worked": {
            "title": "One instance, four readings, and the cost of refusing to be short",
            "intro": [
                "`K = 100`, `D = 1200`, `h = 6`, `P = 2400`, `π = 6`. The two correction "
                "factors are `1 − D/P = 1/2` and `(h + π)/π = 2`, and every figure below is "
                "the panel's own.",
            ],
            "lines": [
                "effective holding rate:   h × (1 − D/P) ÷ ((h + π)/π) = 6 × 1/2 ÷ 2 = 3/2",
                "",
                "  Q* = √(2KD / (3/2)) = √(240000/(3/2)) = √160000 = 400      exactly",
                "  C* = √(2KD × 3/2)   = √360000                   = 600      exactly",
                "",
                "the four readings of the one formula:",
                "",
                "  switches off        Q* = 200         C* = 1200",
                "  production only     Q* = 200√2       C* = 600√2     ≈ 282.843 / 848.528",
                "  backorders only     Q* = 200√2       C* = 600√2     ≈ 282.843 / 848.528",
                "  both                Q* = 400         C* = 600",
                "",
                "at Q = 400, choosing the backorder level:",
                "",
                "  b* = (1 − D/P)·Q·h/(h + π) = (1/2)(400)(6)/12 = 100      cost 600",
                "  b  =  99                                                cost 60003/100",
                "  b  = 101                                                cost 60003/100",
                "  b  =   0    (refuse to be short at all)                 cost 900",
            ],
            "after": [
                "The last block is the argument for the model rather than a detail of it. "
                "Refusing to plan any shortage costs `900` where planning one costs `600` "
                "&mdash; half as much again &mdash; and the reason is that a unit owed "
                "costs `π = 6` while a unit held costs `h = 6` and the owed unit is not "
                "sitting in a warehouse. When `π` is genuinely equal to `h`, refusing to "
                "backorder is simply choosing the more expensive of two identical storage "
                "options.",
                "The two middle rows being identical is the fact worth taking away. `1/2` "
                "and `2` act on the same quantity &mdash; the effective holding rate "
                "&mdash; so a machine running at twice demand and a backorder penalty equal "
                "to the holding rate are the same correction wearing different words. That "
                "is why one formula covers both, and why an account that teaches them as "
                "two results with two derivations is teaching one result twice.",
                "For a rehearsal, set `P = 1440` and `π = 12`, keeping the rest. The "
                "supplied first move is that the factors become `1 − D/P = 1/6` and "
                "`(h + π)/π = 3/2`. Work out the effective holding rate, predict `Q*` and "
                "`C*`, and then say &mdash; before the panel does &mdash; whether the "
                "backorder level at `Q = 400` comes out rational.",
            ],
        },
        "quiz_title": "Rates, factors and refusals",
        "quiz": [
            {"q": "Production runs at `P = 2400` against demand `D = 1200`. What is the peak stock level on a run of `Q`?",
             "a": ["`Q`", "`Q/2`", "`(1 − D/P)·Q = Q/2`, reached at the end of the run", "`P − D` times the cycle length"],
             "c": 2,
             "why": "Demand keeps drawing stock while the machine runs, so the level climbs "
                    "at `P − D` for the `Q/P` of the cycle spent producing, reaching "
                    "`(1 − D/P)·Q`. Here that is `Q/2` &mdash; numerically the same as the "
                    "average stock in the plain model, which is a coincidence of this "
                    "instance and not the same quantity. The peak is `Q` only when the run "
                    "is instantaneous."},
            {"q": "The backorder penalty `π` is set to zero. What does the model say?",
             "a": ["That backorders should be zero, since they cost nothing to avoid",
                   "That the optimum is the plain economic order quantity",
                   "That there is no finite optimum, because backordering everything is free",
                   "That `π = 0` is the same as `π` very large"],
             "c": 2,
             "why": "A free shortage makes the cheapest policy an unbounded one: hold "
                    "nothing, owe everyone. The panel reports that the model has run out "
                    "rather than printing a number. A very large `π` is the opposite "
                    "extreme &mdash; it drives the second factor towards one and recovers "
                    "the model with no shortages, which is the answer a reader often means "
                    "when they type a zero."},
            {"q": "On the worked instance, why do the production-only and backorders-only rows give identical answers?",
             "a": ["Because the panel computes them with the same function",
                   "Because both corrections scale the effective holding rate by `1/2` here, and the answer depends on that rate alone",
                   "Because `P = 2400` is twice `D` and `π = 6` equals `h`, which is always the same model",
                   "Because the two effects cancel"],
             "c": 1,
             "why": "`1 − D/P = 1/2` and `π/(h + π) = 1/2` on this data, and the economic "
                    "order quantity depends on `K`, `D` and the effective holding rate and "
                    "on nothing else. Sharing a function is how the panel computes them, "
                    "not why they agree; and the coincidence is a property of these "
                    "numbers, not a general identity between the two models."},
            {"q": "Why does the panel report the best backorder level at the run size you choose rather than at `Q*`?",
             "a": ["Because `Q*` is not always the best run size",
                   "Because at a rational `Q` the answer is rational and exact, while at an irrational `Q*` it is a surd",
                   "Because the backorder level does not depend on `Q`",
                   "Because the slider only accepts whole numbers"],
             "c": 1,
             "why": "`b = (1 − D/P)·Q·h/(h + π)` is linear in `Q`, so a rational `Q` gives a "
                    "rational `b` that can be printed with every digit exact. At an "
                    "irrational optimum the same expression is irrational, and a page that "
                    "printed a rounded backorder level beside an exact run size would be "
                    "mixing two kinds of number without saying so."},
        ],
        "mistakes": [
            ("Using the raw holding rate with a finite production rate",
             "Stock builds at `P − D`, so the peak is `(1 − D/P)·Q` and the holding bill is "
             "scaled accordingly. Forgetting the factor reports a run size that is too "
             "small by `√(1/(1 − D/P))` and a cost that is too large by the same factor "
             "&mdash; on the worked instance, `200` where the answer is `282.84`, which is "
             "a plausible-looking number and completely wrong."),
            ("Treating a planned shortage as a failure to be avoided",
             "When `π` is a real, agreed cost, planning to be short is an economic choice "
             "like any other: on the worked instance it saves a third of the total cost. "
             "The failure to avoid is an <em>unplanned</em> shortage, which this model does "
             "not describe at all &mdash; that is what the safety-stock lessons later in "
             "this course are for."),
            ("Reading a refusal as a bug",
             "`1 − D/P ≤ 0` and `π = 0` both produce a panel that declines to print an "
             "answer. Neither is a numerical problem. One says the machine cannot meet "
             "demand and the other says nothing has been charged for a broken promise, and "
             "in both cases the fix is to the model rather than to the arithmetic."),
        ],
        "standard": ("Finish when a production rate and a shortage penalty read as two adjustments to one holding rate.",
                     "You should be able to derive the factor `1 − D/P` from the geometry "
                     "of the sawtooth, state what `π` buys and why it divides the holding "
                     "rate by `(h + π)/π`, produce all four models from one expression, "
                     "compute the optimal backorder level at a given run size and verify it "
                     "is a minimum, and say precisely what the model reports when `P ≤ D` "
                     "or `π = 0`."),
        "note": "Every lesson so far has known the demand rate exactly. The rest of the course does not. The next one is the smallest possible version of that change: a single order, a single season, a demand that is a random variable, and no second chance to correct the decision.",
    },
]
