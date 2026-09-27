"""Inventory Models."""


from . import part_a, part_b


COURSE = {
    "slug": "inventory-models",
    "title": "Inventory Models",
    "level": "Advanced",
    "summary": (
        "How much to order, and when. The deterministic half derives the economic order "
        "quantity from the discriminant of a quadratic rather than from a derivative, "
        "and then measures the flatness that every account of it asserts; the random "
        "half replaces the demand rate with a distribution and turns the question into a "
        "quantile. Along the way, the two numbers everyone calls the service level turn "
        "out to be different numbers, and the panel prints both."
    ),
    "blurb": (
        "This is the course where the answer is a formula, which makes it the course "
        "where the formula most needs taking apart. The economic order quantity is "
        "`√(2KD/h)` and it arrives here from a quadratic inequality whose two roots "
        "collide &mdash; the same discriminant Algebra uses, applied to a budget "
        "&mdash; so that existence, uniqueness and optimality come out of one argument "
        "with no calculus in it. The claim that the cost curve is flat either side of "
        "the optimum is then computed rather than repeated: ordering `t` times the best "
        "quantity costs `(t + 1/t)/2` times the minimum, an expression containing none "
        "of the data, so &ldquo;within one per cent&rdquo; is 13.2% below to 15.2% above "
        "in every warehouse there has ever been. After that the assumptions come off one "
        "at a time &mdash; a price that depends on the order, a run that takes time, a "
        "shortage that was planned, and finally a demand that is a random variable "
        "rather than a rate."
    ),
    "key": [
        "C(Q) = K·D/Q + h·Q/2          the two halves are equal exactly at the optimum",
        "K·D/Q + h·Q/2 ≤ T   ⟺   h·Q²/2 − T·Q + K·D ≤ 0      discriminant T² − 2hKD",
        "the roots merge at T = √(2hKD) = C*, leaving Q = T/h = √(2KD/h) = Q*",
        "C(t·Q*)/C* = (t + 1/t)/2      free of K, D and h — flatness, as a formula",
        "all-units discounts: one candidate per band, and the curve JUMPS at every break",
        "finite production rate and planned backorders: h·(1 − D/P) and then ÷ (h + π)/π",
        "newsvendor: order the smallest Q with P(D ≤ Q) ≥ cᵤ/(cᵤ + cₒ)",
        "cycle service = P(no stockout in a cycle);  fill rate = 1 − E[short]/Q    NOT the same",
    ],
    "assumes_short": "algebra: quadratics, the discriminant and surds; discrete probability, expectation and the distribution of a sum",
    "assumes_long": (
        "from algebra, quadratics in full — the quadratic formula, the discriminant and "
        "what its sign says, quadratic inequalities and the fact that an upward parabola "
        "is below zero exactly between its roots, and radical expressions kept in surd "
        "form, because the economic order quantity is one and this course carries it "
        "exactly to the point of printing. From discrete mathematics, Discrete "
        "Probability through variance: random variables, expected value, linearity of "
        "expectation, and the distribution of a sum of independent variables, which is "
        "what a lead time of several periods is. Nothing from earlier on this path is "
        "required to follow the arguments, although Linear Programming Models is worth "
        "having met for what it says about naming a model's assumptions before solving "
        "it. There is no calculus here and none is wanted: where a textbook "
        "differentiates the cost, this course lowers a budget until two roots collide"
    ),
    "outcomes_intro": (
        "By the end you can derive the economic order quantity without calculus, say how "
        "much it costs to miss it and over what range, adjust it for price breaks, a "
        "finite production rate and planned shortages, and choose a quantity, a reorder "
        "point or a base-stock level when demand is a distribution &mdash; stating in "
        "each case which service level you have measured."
    ),
    "outcomes": [
        ("Build the model and know what it assumed",
         "Constant demand, instantaneous replenishment, no shortages and a price "
         "independent of the order, each written down as an assumption rather than "
         "absorbed into a formula &mdash; with the sawtooth drawn so that `Q/2` is "
         "something seen rather than remembered, and each of the four removed in turn "
         "later in the course."),
        ("Derive the order quantity from a discriminant",
         "The budget question `K·D/Q + h·Q/2 ≤ T` turned into "
         "`h·Q²/2 − T·Q + K·D ≤ 0` with the positivity condition stated, its three "
         "regimes read off `T² − 2hKD`, and the collision of the roots at `T = √(2hKD)` "
         "producing `Q* = √(2KD/h)` together with the proof that nothing beats it."),
        ("Measure the flatness instead of asserting it",
         "`C(t·Q*)/C* = (t + 1/t)/2`, the second quadratic `t² − 2(1 + e)t + 1 ≤ 0` it "
         "produces, and the band `(1 + e) ± √(e(2 + e))` &mdash; which on any instance "
         "at all is 13.2% below to 15.2% above for one per cent, and exactly half to "
         "double for twenty-five."),
        ("Handle a price that depends on the order",
         "All-units breaks, the genuine discontinuity they put in the total-cost curve, "
         "one candidate per band with the band floor where its own economic order "
         "quantity is unreachable, and a comparison of surd-valued totals settled by "
         "exact arithmetic rather than by two printed decimals."),
        ("Correct the cycle for production time and planned shortages",
         "The factor `1 − D/P` derived from the geometry of a tilted sawtooth, the "
         "further division by `(h + π)/π` that a priced backorder buys, all four named "
         "models produced from one expression, and the two refusals &mdash; `P ≤ D` and "
         "`π = 0` &mdash; reported as statements about the model rather than as errors."),
        ("Choose against a distribution, and name the service you measured",
         "The critical ratio `cᵤ/(cᵤ + cₒ)` read as a probability, the reorder point as a "
         "quantile of lead-time demand built by convolution, the base-stock level over "
         "`R + L` periods, and cycle service printed beside fill rate every time because "
         "on one worked policy they are 68.75% and 99.625%."),
    ],
    "syllabus_intro": (
        "The plain model first, because everything else on the course is it with one "
        "assumption removed, and the derivation immediately after it rather than inside "
        "it &mdash; the crossing of the two cost curves is where the answer is, and the "
        "discriminant is why it is a minimum, and separating those two makes both "
        "clearer. Then the assumptions come off in order of how much they change the "
        "shape of the answer: a price break breaks the curve into pieces, a production "
        "rate and a planned shortage rescale it, and a random demand replaces it. The "
        "random half is ordered by how much machinery it needs &mdash; one season, then "
        "a lead time, then a review interval &mdash; and it ends on the misconception "
        "this course would keep if it could keep only one."
    ),
    "how_to": [
        "Say which of the four assumptions your situation breaks before choosing a "
        "model. Constant demand, instant arrival, no shortages, a price that does not "
        "depend on the quantity: there is a lesson for each, and picking the model by "
        "which formula you remember is how a plain economic order quantity ends up "
        "answering a question about a machine that takes three days to produce a batch.",
        "Keep the root until the last moment. `√(2KD/h)` is either a whole number or an "
        "irrational one, and the difference is a property of the data rather than of the "
        "method. Rounding early makes a merge of two roots look like a near-miss, makes "
        "two candidate costs look separated when they are not, and makes an exact "
        "statement into a decimal the reader cannot check.",
        "Price the mistake rather than warning about it. Every panel on this course "
        "computes the wrong answer beside the right one &mdash; the band floor against "
        "the band's own quantity, `b = 0` against the optimal backorder level, the "
        "lead-time-only base-stock level against `R + L` &mdash; because a reader who "
        "has seen 34.38% printed where 90% was asked for does not make that mistake "
        "again, and a reader who has read a caution about it does.",
        'Never write &ldquo;service level&rdquo; without saying which one. Cycle service and fill rate are computed from the same policy and on the worked instance of &ldquo;Reorder Points, and Two Numbers Called Service&rdquo; they are 68.75% and 99.625%. Both are correct, both are in general use, and a target quoted without its definition has specified nothing at all.',
    ],
    "not_covered": [
        "Calculus, anywhere. The economic order quantity is found here by the "
        "discriminant of a quadratic, and the flatness of the cost curve by the "
        "discriminant of a second one. That is a complete argument rather than a "
        "workaround: it proves existence, uniqueness and optimality at once, where a "
        "derivative gives a stationary point and then needs a second test to say what "
        "kind it is.",
        "Incremental quantity discounts. Only all-units pricing is built, because it is "
        "the one whose cost curve is discontinuous and therefore the one whose answer "
        "cannot be found by a single formula. Incremental pricing has a continuous curve "
        "and is a straightforward variation; the reason for choosing the harder one is "
        "that the candidate-per-band argument is what this course is teaching.",
        "Joint optimisation of the order quantity and the reorder point. The two are "
        "treated as separate decisions here, which is the standard working assumption "
        "and is close to optimal, and it lets the risk question be asked cleanly: the "
        "exposure window is the lead time, and the order quantity does not appear in it. "
        "Solving the pair together needs an iteration that would obscure exactly that.",
        "Continuous demand distributions, and the normal approximation to lead-time "
        "demand. Every distribution on this course is discrete with rational "
        "probabilities, so every convolution, quantile and service level is an exact "
        "fraction. The standard textbook route &mdash; a normal lead-time demand and a "
        "safety factor read from a table &mdash; would replace those with decimals from "
        "an approximation this path has not built, and would hide the overshoot that "
        "makes a discrete target interesting.",
        "Multi-echelon inventory, perishability, and lost sales as distinct from "
        "backorders. All three are real and all three change the model rather than its "
        "parameters: a second stocking location couples two policies, a shelf life makes "
        "the cost depend on age, and a customer who leaves rather than waits removes the "
        "backorder term this course prices. Naming them is as far as it goes.",
    ],
    "footer_lead": (
        "Every cost, probability, convolution, expected shortage and service level on "
        "this course is an exact fraction, and the distributions are rational so nothing "
        "in the second half of the course rounds at all: `11/16` is printed as `68.75%` "
        "and `63/64` as `98.44%`, which are exact fractions shown to two places rather "
        "than approximations. Two quantities here are genuinely irrational &mdash; the "
        "economic order quantity `√(2KD/h)` and its cost `√(2KDh)`, together with the "
        "band ends and candidate totals built on them &mdash; and they are carried as "
        "exact surds from end to end, with one function doing all the rounding and one "
        "sentence naming it: four decimal places, from the exact surd, by integer square "
        "root with three guard digits, printed beside the surd rather than instead of "
        "it. Where the data make the radicand a perfect square the answer is a whole "
        "number and the panel says so, which is why `200` and `20√30` are both shown as "
        "what they are. Comparisons between costs are settled on the exact forms and "
        "never on two decimals, because two decimals that differ in the fourth place are "
        "not evidence about the numbers behind them. What none of this can do is check a "
        "demand distribution, a holding rate or a shortage penalty against the situation "
        "it was taken from."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
