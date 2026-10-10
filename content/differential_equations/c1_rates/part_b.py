"""Rates of Change and the Derivative -- the second half.

Where the rate is zero, the product rule, the chain rule, the second
derivative, and the exponential and its rate.

Every figure below is read off the calckit labs -- scripts/mathpath/labs/
calckit.py -- with scripts/labcheck.js --observe and pinned in each preset's
expect, rather than asserted here. The product and chain rules are never taken
on trust: the lab expands both sides as polynomials and compares them, and a
proof block follows each statement because the proof is algebra the reader has.
The exponential is the one lesson whose figures are rounded, and every rounded
figure carries the approximation sign.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "where-the-rate-is-zero",
        "title": "Where the Rate Is Zero",
        "module": "The derivative as a function",
        "one_line": "Solve p′ = 0 exactly, then use the sign of p′ on each side to say whether each zero is a maximum, a minimum or neither.",
        "summary": (
            "A zero of the derivative is a place where the tangent is level, and that is the "
            "only place a polynomial's graph can turn. It is necessary for a turn and not "
            "enough: the graph turns only where `p′` changes sign. Solve `p′ = 0`, test the "
            "sign on each side of every zero, and each one is a maximum, a minimum or a flat "
            "step that keeps going the same way."
        ),
        "key": [
            "a turn needs p′(t) = 0",
            "p′ = 0 is necessary, not sufficient",
            "rising then falling: a maximum",
            "falling then rising: a minimum",
            "no sign change: a flat step, no turn",
            "t³: p′ = 3t² is 0 at 0, yet no turn",
        ],
        "key_label": "Where p′ is zero, and what that does to the graph",
        "concepts_intro": (
            "Three ideas: why a turn needs a zero, why a zero does not need a turn, and what "
            "a maximum or minimum is a maximum or minimum of."
        ),
        "concepts": [
            ("A graph can turn only where the tangent is level",
             "Just before a turn the graph is rising, so `p′` is positive; just after, it is "
             "falling, so `p′` is negative. A polynomial's derivative is a polynomial, and a "
             "polynomial does not jump from positive to negative without passing through "
             "zero. So every turn sits at a zero of `p′`."),
            ("A level tangent is not always a turn",
             "The converse is false. For `p(t) = t³` the derivative `3t²` is zero at `t = 0`, "
             "and positive on both sides. The graph flattens for an instant and keeps "
             "rising. Whether a zero is a turn is decided by the sign of `p′` on each side "
             "of it, and by nothing at the zero itself."),
            ("Maximum and minimum are local",
             "A maximum at `t = c` is the highest point of the graph near `c`: higher than "
             "its neighbours on both sides. It need not be the highest point anywhere. A "
             "cubic climbs for ever, so any maximum it has is overtaken further along."),
        ],
        "read_title": "Zeros of the derivative, and what they do and do not say",
        "read_intro": "The idea in a sentence, one cubic carried all the way through, the zero that is not a turn, and the case with no zero at all.",
        "body": [
            ("p", "&ldquo;The Derivative as a Function&rdquo; ended on a warning: a zero of `p′` is "
                  "a place where the tangent is level, and it does not say whether the graph "
                  "rises or falls on either side. This lesson turns the warning into a method."),
            ("def", ("Critical point, maximum and minimum",
                     "A <strong>critical point</strong> of a polynomial `p` is a place where "
                     "`p′(t) = 0`.",
                     "It is a <strong>local maximum</strong> if `p′` changes from positive to "
                     "negative there, and a <strong>local minimum</strong> if `p′` changes "
                     "from negative to positive. If `p′` has the same sign on both sides, it "
                     "is neither.")),
            ("example", ("A cubic with two turns",
                         "Let `p(t) = 2t³ − 3t² − 12t + 1`. Then `p′(t) = 6t² − 6t − 12`, and "
                         "taking out the common factor 6 gives `6(t² − t − 2) = 6(t − 2)(t + 1)`.",
                         "The critical points are `t = −1` and `t = 2`. Test one place in "
                         "each region they cut the line into, and the whole shape of the "
                         "graph follows.")),
            ("math", [
                "p′(t) = 6(t − 2)(t + 1)",
                "",
                "   t < −1          p′ > 0     rising",
                "   −1 < t < 2      p′ < 0     falling",
                "   t > 2           p′ > 0     rising",
            ]),
            ("p", "At `t = −1` the graph stops rising and starts falling: a local maximum. At "
                  "`t = 2` it stops falling and starts rising: a local minimum. The height "
                  "comes from `p`, not from `p′`, because `p′` is zero at both: "
                  "`p(−1) = −2 − 3 + 12 + 1 = 8` and `p(2) = 16 − 12 − 24 + 1 = −19`."),
            ("p", "The word local matters. The maximum height is 8, but further right the "
                  "graph rises without limit: `p(4) = 128 − 48 − 48 + 1 = 33`. The height 8 is "
                  "the highest point near `t = −1` and nothing more."),
            ("h3", "A zero where nothing turns"),
            ("p", "Now `p(t) = t³`. Its derivative is `3t²`, which is zero at `t = 0` and "
                  "positive for every other `t`, because a square is never negative. So `p′` "
                  "is positive on both sides of its zero, and the graph rises before "
                  "`t = 0` and rises after it, level for an instant and not turning. The "
                  "lab marks such a zero as having no sign change, and its interval tile "
                  "reads rising on both sides."),
            ("p", "This is the case the necessary-but-not-sufficient wording is for. "
                  "Solving `p′ = 0` finds every place a turn could be, and the sign test "
                  "sorts the real turns from the flat steps."),
            ("h3", "A derivative that is never zero"),
            ("p", "For `p(t) = t³ + t` the derivative is `3t² + 1`. A square is at least 0, so "
                  "`3t² + 1` is at least 1 and never reaches zero. The graph has no level "
                  "tangent and no turn: it rises everywhere. The zero tile of the lab says "
                  "`none rational`, which is how it reports a polynomial with no zero it "
                  "can write as a fraction, and the interval tile gives the fuller "
                  "answer, rising for every `t`."),
        ],
        "lab": ("calckit", {
            "mode": "derivative",
            "order": 1,
            "preset": "two-turns",
            "presets": [
                {"id": "two-turns", "label": "2t³ − 3t² − 12t + 1, a maximum and a minimum",
                 "f": "2t^3 - 3t^2 - 12t + 1", "expect": {'dvZeros': '−1, 2', 'dvIntervals': 'rising t < −1; falling −1 < t < 2; rising t > 2'}},
                {"id": "flat-step", "label": "t³, level at 0 and still rising", "f": "t^3",
                 "expect": {'dvZeros': '0 (no sign change)', 'dvIntervals': 'rising t < 0; rising t > 0'}},
                {"id": "none", "label": "t³ + t, never level", "f": "t^3 + t",
                 "expect": {'dvZeros': 'none rational', 'dvIntervals': 'rising for every t'}},
            ],
            "panel_title": "Find the zeros of p′ and sort them by the sign",
            "panel_intro": "Type a polynomial in t. The lab differentiates it, lists the rational "
                           "zeros of the derivative, and tests the sign of p′ between them. A zero "
                           "marked no sign change is a flat step and not a turn. The green dots on "
                           "the plot sit on the graph of p at each zero of p′.",
        }),
        "steps_title": "Locating and sorting the critical points",
        "steps_intro": "Five moves. The fourth is the one that stops a flat step being called a turn.",
        "steps": [
            ("Differentiate",
             "Apply the power rule to each term and collect the result in descending powers."),
            ("Solve p′ = 0",
             "Factor, or use the quadratic formula. The zeros are the only places a turn can "
             "be. A zero that appears twice in the factoring, such as `3t²`, is a warning "
             "that the sign may not change."),
            ("Test the sign in every region",
             "Between and beyond the zeros, put in one value of `t` and note whether `p′` is "
             "positive or negative there. Use the factored form so the sign is easy to read."),
            ("Name each zero from its two neighbours",
             "Positive then negative is a maximum, negative then positive is a minimum, and "
             "the same sign on both sides is neither."),
            ("Find the height from p",
             "Put the zero into `p`, not `p′`. The height of the turn is a value of the "
             "original polynomial."),
        ],
        "worked": {
            "title": "A cubic with a maximum and a minimum",
            "intro": [
                "The polynomial is `p(t) = 2t³ − 3t² − 12t + 1`. The derivative, the signs and "
                "the heights are each exact.",
            ],
            "lines": [
                "p′(t) = 6t² − 6t − 12 = 6(t − 2)(t + 1)",
                "",
                "zeros:    t = −1,  t = 2",
                "t = −2:   p′ = 6·(−4)·(−1) = 24    rising",
                "t = 0:    p′ = 6·(−2)·1 = −12      falling",
                "t = 3:    p′ = 6·1·4 = 24          rising",
                "",
                "t = −1:   rising then falling   maximum   p = 8",
                "t = 2:    falling then rising   minimum   p = −19",
            ],
            "after": [
                "The lab's interval tile for this polynomial gives the same three regions as "
                "the table, and its zero tile gives the same two places. Neither height was "
                "found by plotting a point.",
                "For a rehearsal, take `p(t) = t³ − 3t`. The derivative is "
                "`3t² − 3 = 3(t − 1)(t + 1)`; work out the signs, then which of `t = −1` "
                "and `t = 1` is the maximum.",
            ],
        },
        "quiz_title": "Level tangents and turns",
        "quiz": [
            {"q": "For `p(t) = t³ − 3t`, the derivative is `3(t − 1)(t + 1)`. What happens to the graph at `t = 1`?",
             "a": ["A local maximum, because the tangent is level",
                   "A local minimum, because `p′` goes from negative to positive",
                   "Nothing, because the sign of `p′` does not change",
                   "A local maximum, because `p′` goes from positive to negative"],
             "c": 1,
             "why": "Just left of 1, say at `t = 0`, `p′ = 3·(−1)·1 = −3` is negative, and just "
                    "right of 1, say at `t = 2`, it is `3·1·3 = 9`, positive. Falling then "
                    "rising is a minimum. A level tangent alone decides nothing, the sign "
                    "does change at 1, and the order positive then negative would make it a "
                    "maximum, which is what happens at `t = −1`."},
            {"q": "Which polynomial has `p′ = 0` at `t = 0` and no turn there?",
             "a": ["t²", "t⁴", "t³", "t³ + t"],
             "c": 2,
             "why": "`t³` has `p′ = 3t²`, zero at 0 and positive on both sides. The graphs of "
                    "`t²` and `t⁴` both turn at 0, since `2t` and `4t³` change sign there, "
                    "and `t³ + t` has `p′ = 3t² + 1`, which is never zero."},
            {"q": "For `p(t) = 2t³ − 3t² − 12t + 1` the local maximum at `t = −1` has height 8. Why is 8 not the greatest value of `p`?",
             "a": ["Because `p(4) = 33` is higher, and the graph keeps rising to the right",
                   "Because the point at `t = −1` is really a minimum",
                   "Because `p′(−1)` is not zero",
                   "Because a graph has no greatest height"],
             "c": 0,
             "why": "A local maximum is the highest point nearby only. This cubic rises "
                    "for ever to the right, and `p(4) = 33` already exceeds 8. The point "
                    "at `t = −1` is a maximum, since `p′` goes from positive to negative, "
                    "and `p′(−1) = 0`. The last choice is false in general: some graphs "
                    "have a greatest height, such as an upside-down parabola."},
            {"q": "The derivative of `p(t) = t³ + t` is `3t² + 1`. How many turns does the graph have?",
             "a": ["Two, at `t = ±1/3`",
                   "One, at `t = 0`",
                   "One, at `t = −1/3`",
                   "None"],
             "c": 3,
             "why": "`3t² + 1` is at least 1 for every `t`, so it is never zero and the "
                    "tangent is never level. There is nothing to turn. The places named in "
                    "the other choices do not solve `3t² + 1 = 0`; a square is not negative."},
        ],
        "mistakes": [
            ("Calling every zero of p′ a maximum or a minimum",
             "For `p(t) = t³`, `p′ = 3t²` is zero at `t = 0`, and the graph is rising on "
             "both sides of it. If 0 were a maximum the graph would fall just after it; it "
             "does not. The zero says the tangent is level, and only the signs of `p′` "
             "either side say whether the graph turned."),
            ("Reading the height of a turn from p′",
             "At `t = −1` the derivative `6(t − 2)(t + 1)` is zero, and the height of the "
             "maximum is 8. The zero of `p′` tells you where to look, and the value of `p` "
             "there tells you how high. Writing 0 as the height of a turn is reading "
             "the wrong function."),
            ("Taking a local maximum for the largest value",
             "A maximum is the highest point near it. The cubic above has a local maximum of "
             "8 at `t = −1` and a value of 33 at `t = 4`. Say local, and where a question "
             "asks for the greatest value over an interval, compare the turns with the ends."),
        ],
        "standard": ("Finish when you can solve p′ = 0 exactly for a polynomial and say, from the signs on either side, whether each zero is a maximum, a minimum or neither.",
                     "You should be able to differentiate, factor the result, test the sign "
                     "of `p′` in every region, name each zero from its neighbours, and find "
                     "the height of each turn from `p`."),
        "note": "The lab finds the zeros of `p′` that are fractions, and for a quadratic "
                "derivative it places the others with square roots in the interval tile. "
                "The next two lessons build the two rules that let you differentiate "
                "something other than a sum of powers, starting with &ldquo;The Product "
                "Rule&rdquo;.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-product-rule",
        "title": "The Product Rule",
        "module": "The derivative as a function",
        "one_line": "The derivative of a product is f′·g + f·g′, verified here by expanding both sides, and it is not the product of the derivatives.",
        "summary": (
            "When two functions are multiplied and both are changing, the product changes "
            "twice over: once because the first factor moves and once because the second "
            "does. The product rule adds the two contributions, `f′·g + f·g′`. For "
            "polynomials it is checked by expanding the product and differentiating term by "
            "term, and the lab compares the two results exactly."
        ),
        "key": [
            "(f·g)′ = f′·g + f·g′",
            "each factor's rate, times the other factor",
            "it is a sum of two terms",
            "t² and t + 1: 2t·(t + 1) + t²·1",
            "which is 3t² + 2t, the rate of t³ + t²",
            "the product f′·g′ = 2t is not it",
        ],
        "key_label": "The product rule",
        "concepts_intro": (
            "Three ideas: why there are two terms, how the rule reads, and a quick check "
            "that catches the wrong rule."
        ),
        "concepts": [
            ("A product changes in two ways",
             "Picture a rectangle of width `f` and height `g`. Its area is `f·g`. If the "
             "width grows, the area gains a strip of the old height; if the height grows, "
             "it gains a strip of the old width. The rate of the area is the sum of the two "
             "strips' rates, and that is the rule."),
            ("Each rate multiplies the other factor",
             "The width's rate `f′` acts on the height as it stands, `g`, and the height's "
             "rate `g′` acts on the width as it stands, `f`. So the rule is "
             "`f′·g + f·g′`: a sum of two products, each holding one factor still and "
             "differentiating the other."),
            ("The degree gives the wrong rule away",
             "If `f` has degree 2 and `g` has degree 1, the product has degree 3 and its "
             "derivative has degree 2. The product of the derivatives has degree "
             "`1 + 0 = 1`. The two cannot agree, whatever the coefficients."),
        ],
        "read_title": "A sum of two products, checked against the expansion",
        "read_intro": "The temptation and its refutation first, then the statement and its proof, then two checks and the case of a square.",
        "body": [
            ("p", "A product of two polynomials can always be multiplied out and "
                  "differentiated term by term. The product rule is for the other case, when "
                  "the factors are better left as they are, and the way to trust it is to "
                  "check it against the expansion."),
            ("p", "Take `f(t) = t²` and `g(t) = t + 1`. Multiplied out, `f·g = t³ + t²`, and "
                  "the power rule gives the derivative of `t³ + t²` as `3t² + 2t`. The tempting rule is to "
                  "differentiate each factor and multiply: `f′ = 2t` and `g′ = 1`, so the "
                  "product is `2t·1 = 2t`. That is not `3t² + 2t`, and it cannot be, since "
                  "its degree is 1 and the true derivative's is 2."),
            ("thm", ("The product rule",
                     "For polynomials `f` and `g`, `(f·g)′ = f′·g + f·g′`.",)),
            ("proof", ["The numerator of the quotient of the product is "
                       "`f(t + h)·g(t + h) − f(t)·g(t)`. Add and subtract `f(t)·g(t + h)` and "
                       "regroup: `[f(t + h) − f(t)]·g(t + h) + f(t)·[g(t + h) − g(t)]`.",
                       "Divide by `h`. The quotient of the product is the quotient of `f` "
                       "times `g(t + h)`, plus `f(t)` times the quotient of `g`. Each "
                       "quotient is a polynomial in `h` after the cancelling, and so is "
                       "`g(t + h)`.",
                       "Read off the part free of `h`: the constant term of the quotient of "
                       "`f` is `f′(t)`, the constant term of `g(t + h)` is `g(t)`, and the "
                       "constant term of the quotient of `g` is `g′(t)`. The constant term "
                       "of a product is the product of the constant terms, which gives "
                       "`f′(t)·g(t) + f(t)·g′(t)`."]),
            ("example", ("The rule against the expansion",
                         "For `f = t²` and `g = t + 1`: `f′·g = 2t·(t + 1) = 2t² + 2t` and "
                         "`f·g′ = t²·1 = t²`. Their sum is `3t² + 2t`, which is the derivative "
                         "of the expanded product `t³ + t²` found above.",
                         "The lab does this on any pair of polynomials, and its rule tile "
                         "prints the correct sum beside the wrong product so the two can be "
                         "compared. Its equality tile says whether the expanded product's "
                         "derivative and the rule's output are the same polynomial.")),
            ("h3", "A product that is not worth expanding"),
            ("p", "With `f = t³ − t` and `g = t² + 2` the expansion is "
                  "`t⁵ + t³ − 2t`, and its derivative is `5t⁴ + 3t² − 2`. The rule reaches "
                  "the same polynomial from the factors: `f′·g = (3t² − 1)(t² + 2) = "
                  "3t⁴ + 5t² − 2` and `f·g′ = (t³ − t)·2t = 2t⁴ − 2t²`, which add to "
                  "`5t⁴ + 3t² − 2`. For larger factors the rule is less work than the "
                  "expansion, and for functions that cannot be multiplied out it is the "
                  "only route."),
            ("h3", "When both factors are the same"),
            ("p", "Put `g = f` and the rule says `(f²)′ = f′·f + f·f′ = 2·f·f′`. Take "
                  "`f = t + 1`: the square is `t² + 2t + 1`, whose derivative is `2t + 2`, "
                  "and the rule gives `2·(t + 1)·1`, the same. The derivative of a square "
                  "is twice the function times its own derivative, not `f′` squared and not "
                  "`2·f′`. The lab's second preset squares `t²`: the true derivative of "
                  "`t⁴` is `4t³` and the wrong rule gives `2t·2t = 4t²`. At `t = 0` and at "
                  "`t = 1` the two agree, so a check at one of those places would pass the "
                  "wrong rule; the degrees, 3 against 2, say the two polynomials are "
                  "different whatever any single place says. The next lesson carries the "
                  "square one step further, to every power."),
        ],
        "lab": ("calckit", {
            "mode": "hpoly",
            "preset": "basic",
            "presets": [
                {"id": "basic", "label": "t² times t + 1", "kind": "product", "f": "t^2", "g": "t + 1",
                 "a": None, "expect": {'hpConst': '3t² + 2t', 'hpRule': 'f′g + fg′ = 3t² + 2t; f′g′ = 2t', 'hpEqual': 'equal'}},
                {"id": "wrong-rule", "label": "t² times t², the wrong rule beside the right one",
                 "kind": "product", "f": "t^2", "g": "t^2", "a": None, "expect": {'hpConst': '4t³', 'hpRule': 'f′g + fg′ = 4t³; f′g′ = 4t²', 'hpEqual': 'equal'}},
                {"id": "cubic", "label": "t³ − t times t² + 2", "kind": "product", "f": "t^3 - t",
                 "g": "t^2 + 2", "a": None, "expect": {'hpConst': '5t⁴ + 3t² − 2', 'hpRule': 'f′g + fg′ = 5t⁴ + 3t² − 2; f′g′ = 6t³ − 2t', 'hpEqual': 'equal'}},
            ],
            "panel_title": "The product rule against the expansion",
            "panel_intro": "Type two polynomials in t. The lab multiplies them, forms the quotient "
                           "of the product, reads off its part free of h, and compares that with "
                           "f′g + fg′. The rule tile also prints f′g′, the product of the "
                           "derivatives, so the wrong rule can be seen failing.",
        }),
        "steps_title": "Using the product rule",
        "steps_intro": "Four moves. The second is the one the wrong rule skips.",
        "steps": [
            ("Differentiate each factor on its own",
             "Find `f′` and `g′` by the power rule. Write them down before combining "
             "anything."),
            ("Cross them with the other factor",
             "Form `f′·g`, the derivative of the first with the second as it stands, and "
             "`f·g′`, the first as it stands with the derivative of the second."),
            ("Add the two products",
             "The rule is a sum. Collect like powers and write the result in descending "
             "order."),
            ("Check the degree, or expand and compare",
             "The result has degree one less than `f·g`, namely the two degrees added, "
             "minus 1. If you have time, multiply out and differentiate; the two "
             "polynomials must be identical."),
        ],
        "worked": {
            "title": "t³ − t times t² + 2",
            "intro": [
                "Take `f = t³ − t` and `g = t² + 2`. Each line is exact, and the last two "
                "check the answer against the other route.",
            ],
            "lines": [
                "f′ = 3t² − 1,   g′ = 2t",
                "f′·g = (3t² − 1)(t² + 2) = 3t⁴ + 5t² − 2",
                "f·g′ = (t³ − t)·2t = 2t⁴ − 2t²",
                "sum:   5t⁴ + 3t² − 2",
                "",
                "expand first:  f·g = t⁵ + t³ − 2t",
                "differentiate: 5t⁴ + 3t² − 2     the same",
                "",
                "f′·g′ = (3t² − 1)·2t = 6t³ − 2t   degree 3, not 4",
            ],
            "after": [
                "The two routes agree, and the product of the derivatives is a different "
                "polynomial of the wrong degree. The lab's equality tile reads equal for this "
                "pair.",
                "For a rehearsal, differentiate `t·(t² + 1)` by the rule and by expanding, "
                "and compare.",
            ],
        },
        "quiz_title": "Two terms, not one",
        "quiz": [
            {"q": "What is the derivative of `t·(t² + 1)`, by the product rule?",
             "a": ["2t", "t² + 2t + 1", "3t² + 1", "t³ + t"],
             "c": 2,
             "why": "With `f = t` and `g = t² + 1`: `f′·g + f·g′ = 1·(t² + 1) + t·2t = 3t² + 1`. "
                    "The answer `2t` is `f′·g′`, the product of the derivatives. The answer "
                    "`t² + 2t + 1` is `f′·g + g′`, which drops the factor `f` from the second "
                    "term, and `t³ + t` is the product itself, not its derivative."},
            {"q": "Let `f(t) = g(t) = t`, so `f·g = t²`. Which pair of statements is correct?",
             "a": ["`(f·g)′ = 2t` and `f′·g′ = 1`",
                   "`(f·g)′ = 1` and `f′·g′ = 2t`",
                   "Both equal `2t`",
                   "Both equal 1"],
             "c": 0,
             "why": "The derivative of `t²` is `2t`, and each factor has derivative 1, so "
                    "the product of the derivatives is `1·1 = 1`. The two differ, which is the "
                    "whole case against the wrong rule. The rule's own output is "
                    "`1·t + t·1 = 2t`."},
            {"q": "`f` has degree 3 and `g` has degree 2. What is the degree of `(f·g)′`?",
             "a": ["5", "4", "3", "6"],
             "c": 1,
             "why": "The product has degree `3 + 2 = 5`, and differentiating lowers the "
                    "degree by 1, giving 4. The degree 3 is that of `f′·g′`, the wrong "
                    "rule, and 5 forgets to differentiate."},
            {"q": "`g(t) = 5` is a constant, so `g′ = 0`. What does the product rule give for `(5·f)′`?",
             "a": ["`f′`", "`5·f′ + 5·f`", "0", "`5·f′`"],
             "c": 3,
             "why": "The rule gives `f′·5 + f·0 = 5·f′`. A constant factor comes straight "
                    "through the derivative. The first answer drops the 5, and the second "
                    "adds a term `5·f` that would need `g′ = 5`."},
        ],
        "mistakes": [
            ("Taking the derivative of a product to be the product of the derivatives",
             "For `t²·(t + 1)` the true derivative is `3t² + 2t`, and `f′·g′ = 2t·1 = 2t` is "
             "not even the same degree. The simplest case shows it: `t·t = t²` has "
             "derivative `2t`, while the product of the two derivatives is `1·1 = 1`. A "
             "product has two ways of changing, and the wrong rule counts none of "
             "them correctly."),
            ("Keeping only one of the two terms",
             "The rule is a sum, and both terms matter. For `t·t` the first term "
             "`f′·g = 1·t` is `t` and the second `f·g′ = t·1` is also `t`; either alone is "
             "half of the true `2t`. When one term seems to vanish, check that the factor is "
             "a constant."),
            ("Reading the derivative of a square as f′ squared or twice f′",
             "For `f = t + 1` the square is `t² + 2t + 1`, with derivative `2t + 2`. The "
             "squared derivative is `1² = 1`, and twice the derivative is 2; neither is "
             "right. The rule gives `2·f·f′ = 2(t + 1)·1`, the function stays in it."),
        ],
        "standard": ("Finish when you can differentiate a product of polynomials by the rule f′·g + f·g′ and confirm it against the expanded product.",
                     "You should be able to differentiate each factor, form the two crossed "
                     "products and add them, check the degree of the result, expand to "
                     "verify, and say why the product of the derivatives is not the "
                     "derivative of the product."),
        "note": "The rule differentiates a function multiplied by another. A function "
                "applied to another function is a different shape, and it has a "
                "different rule, in &ldquo;The Chain Rule&rdquo;.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "the-chain-rule",
        "title": "The Chain Rule",
        "module": "The derivative as a function",
        "one_line": "The derivative of f(g(t)) is f′(g(t))·g′(t): the outer rate at the inner value, times the inner rate.",
        "summary": (
            "When one function is fed into another, the rate of the whole is a chain of two "
            "rates. The outer function's derivative is evaluated at the inner function's "
            "value, and multiplied by the inner function's derivative. Without the second "
            "factor the answer is wrong by exactly that factor. For polynomials the rule "
            "is proved from the product rule and checked by expanding."
        ),
        "key": [
            "(f(g(t)))′ = f′(g(t))·g′(t)",
            "outer rate, at the inner value",
            "times the inner rate",
            "(3t + 1)²: 2(3t + 1)·3 = 18t + 6",
            "the 3 is the derivative of 3t + 1",
            "(uⁿ)′ = n·uⁿ⁻¹·u′",
        ],
        "key_label": "The chain rule",
        "concepts_intro": (
            "Three ideas: what a composition is, why its rate is a product of two rates, "
            "and why the outer derivative is read at the inner value."
        ),
        "concepts": [
            ("A function of a function",
             "In `f(g(t))` the number `g(t)` is computed first and fed to `f`. With "
             "`f(t) = t²` and `g(t) = 3t + 1`, the composition is `(3t + 1)²`. Which one is "
             "inside matters: `g(f(t))` would be `3t² + 1`, a different function."),
            ("Rates multiply along the chain",
             "If `t` moves by a small step, the inner function moves by `g′` times that "
             "step. The outer function then moves by `f′` times what its input moved. "
             "The rate of the whole is the product of the two rates: the inner rate "
             "`g′(t)`, and the outer rate `f′` taken at the place the outer function is "
             "actually standing."),
            ("The outer derivative is read at g(t), not at t",
             "`f′(g(t))` means: differentiate `f`, then put `g(t)` into the result. For "
             "`f(t) = t²` the derivative is `2t`, and at the inner value `3t + 1` it is "
             "`2(3t + 1)`. Replacing `g(t)` by `t` throws away the inside of the "
             "composition."),
        ],
        "read_title": "Outer at the inner value, times the inner rate",
        "read_intro": "A first composition worked two ways, the rule and its proof, a power of a function, and the shift that leaves the multiplier alone.",
        "body": [
            ("p", "Take `f(t) = t²` and the inner function `g(t) = 3t + 1`, so that "
                  "`f(g(t)) = (3t + 1)²`. Multiplied out this is `9t² + 6t + 1`, and the "
                  "power rule gives the derivative at once: `18t + 6`."),
            ("p", "Now suppose the expansion is not wanted. The derivative of the outer "
                  "function `t²` is `2t`, and read at the inner value `3t + 1` it is "
                  "`2(3t + 1) = 6t + 2`. That is not `18t + 6`; it is off by a factor of "
                  "3, and 3 is the derivative of the inner function `3t + 1`. Multiplying "
                  "the two, `(6t + 2)·3`, gives `18t + 6`."),
            ("thm", ("The chain rule for polynomials",
                     "For polynomials `f` and `g`, `(f(g(t)))′ = f′(g(t))·g′(t)`.",)),
            ("proof", ["Write `u` for `g(t)`. For `f(t) = tⁿ` the claim is `(uⁿ)′ = n·uⁿ⁻¹·u′`. "
                       "It is true for `n = 1`, where it says `u′ = u′`.",
                       "If it holds for `n`, the product rule gives "
                       "`(uⁿ⁺¹)′ = (uⁿ·u)′ = n·uⁿ⁻¹·u′·u + uⁿ·u′ = (n + 1)·uⁿ·u′`, which is "
                       "the claim for `n + 1`.",
                       "So the claim passes from each power to the next: from `n = 1` to "
                       "2, from 2 to 3, and on to every power. A polynomial `f` is a sum of "
                       "constants times powers, and differentiating is done term by term, "
                       "so the claim holds for every polynomial `f`."]),
            ("p", "The proof is the product rule applied again and again, which is why this "
                  "lesson follows &ldquo;The Product Rule&rdquo;. It covers the cases the Subject "
                  "uses. In words: the rate of the whole is the outer function's rate, "
                  "taken where the outer function is standing, times the rate at which "
                  "the inner function is carrying it."),
            ("example", ("A power of a function",
                         "Let `f(t) = t³` and `g(t) = t² + 1`. The outer derivative is "
                         "`3t²`, read at the inner value it is `3(t² + 1)²`, and the inner "
                         "derivative is `2t`. The product is `6t·(t² + 1)²`, which "
                         "expands to `6t⁵ + 12t³ + 6t`.",
                         "Expanding first confirms it: `(t² + 1)³ = t⁶ + 3t⁴ + 3t² + 1`, "
                         "and its derivative is `6t⁵ + 12t³ + 6t`. The lab's equality "
                         "tile reads equal.")),
            ("h3", "A shift leaves the multiplier alone"),
            ("p", "With `f(t) = t²` and `g(t) = t − 4` the composition is `(t − 4)²`, and "
                  "the rule gives `2(t − 4)·1 = 2t − 8`. The inner derivative is 1, so the "
                  "chain factor is invisible. That is why a shift of the input is easy to "
                  "differentiate and a stretch is not: a shift moves the graph without "
                  "changing how steep it is, and a stretch by 3 makes every slope 3 "
                  "times as large."),
            ("p", "The pattern for a stretch and shift together, `f(k·t + c)`, is "
                  "`k·f′(k·t + c)`: the constant `c` never appears in the multiplier, and "
                  "`k` always does."),
        ],
        "lab": ("calckit", {
            "mode": "hpoly",
            "preset": "stretch",
            "presets": [
                {"id": "stretch", "label": "t² of 3t + 1, a stretch", "kind": "compose", "f": "t^2",
                 "g": "3t + 1", "a": None, "expect": {'hpConst': '18t + 6', 'hpRule': '18t + 6', 'hpEqual': 'equal'}},
                {"id": "power", "label": "t³ of t² + 1, a power of a function", "kind": "compose",
                 "f": "t^3", "g": "t^2 + 1", "a": None, "expect": {'hpConst': '6t⁵ + 12t³ + 6t', 'hpRule': '6t⁵ + 12t³ + 6t', 'hpEqual': 'equal'}},
                {"id": "shift", "label": "t² of t − 4, a shift", "kind": "compose", "f": "t^2",
                 "g": "t - 4", "a": None, "expect": {'hpConst': '2t − 8', 'hpRule': '2t − 8', 'hpEqual': 'equal'}},
            ],
            "panel_title": "The chain rule against the expansion",
            "panel_intro": "Type an outer polynomial f and an inner polynomial g. The lab "
                           "forms f(g(t)), expands it, and reads off the part of its quotient "
                           "free of h. The rule tile prints f′(g(t))·g′(t), and the equality "
                           "tile says whether the two polynomials are the same.",
        }),
        "steps_title": "Using the chain rule",
        "steps_intro": "Four moves. Leaving the inner function in place is the second, and forgetting the last is the common slip.",
        "steps": [
            ("Name the outer and the inner function",
             "In `(t² + 1)³` the inner function is `t² + 1` and the outer is the cube. The "
             "inner one is what you compute first."),
            ("Differentiate the outer, and leave the inner in place",
             "Take the derivative of the outer function and put the inner function where "
             "its variable was: `3·(t² + 1)²`, not `3t²`."),
            ("Differentiate the inner function",
             "The inner derivative of `t² + 1` is `2t`. It is a derivative, not the inner "
             "function repeated."),
            ("Multiply, then check",
             "Multiply the two results. Expand `f(g(t))` and differentiate it as a "
             "polynomial; the two answers must be the same polynomial."),
        ],
        "worked": {
            "title": "t³ of t² + 1",
            "intro": [
                "The outer function is `f(t) = t³` and the inner function is "
                "`g(t) = t² + 1`. Every line is exact.",
            ],
            "lines": [
                "f′(t) = 3t²,  so  f′(g(t)) = 3(t² + 1)²",
                "g′(t) = 2t",
                "product:  3(t² + 1)²·2t = 6t(t² + 1)²",
                "(t² + 1)² = t⁴ + 2t² + 1",
                "6t·(t⁴ + 2t² + 1) = 6t⁵ + 12t³ + 6t",
                "",
                "expand first:  (t² + 1)³ = t⁶ + 3t⁴ + 3t² + 1",
                "differentiate: 6t⁵ + 12t³ + 6t     the same",
            ],
            "after": [
                "Both routes give the same polynomial, and the lab's rule tile prints it "
                "for this pair. At `t = 1` the slope is `6 + 12 + 6 = 24`.",
                "For a rehearsal, differentiate `(2t + 5)³` by the rule: the outer "
                "derivative read at the inner value is `3(2t + 5)²`, and the inner "
                "derivative is 2.",
            ],
        },
        "quiz_title": "Outer, inner and the factor between",
        "quiz": [
            {"q": "What is the derivative of `(2t + 5)³`?",
             "a": ["`3(2t + 5)²`", "`6t²`", "`6(2t + 5)²`", "`3(2t + 5)³`"],
             "c": 2,
             "why": "The outer derivative read at the inner value is `3(2t + 5)²`, and the "
                    "inner derivative is 2, so the product is `6(2t + 5)²`. The first answer "
                    "omits the factor 2, `6t²` replaces the inner function by `t`, and "
                    "`3(2t + 5)³` has not lowered the exponent."},
            {"q": "What is the derivative of `(t − 4)²`?",
             "a": ["`2t − 8`", "`2t − 4`", "`2t`", "`t² − 8t + 16`"],
             "c": 0,
             "why": "The rule gives `2(t − 4)·1 = 2t − 8`. The expansion `t² − 8t + 16` has the "
                    "same derivative, `2t − 8`. The answer `2t − 4` keeps the 4 outside "
                    "the multiplication, `2t` ignores the shift, and `t² − 8t + 16` is the "
                    "function itself and not its derivative."},
            {"q": "In `18t + 6 = 2(3t + 1)·3`, where does the final factor 3 come from?",
             "a": ["The exponent of the outer function",
                   "The derivative of the inner function `3t + 1`",
                   "The constant term of `3t + 1`",
                   "The derivative of the outer function"],
             "c": 1,
             "why": "The inner function `3t + 1` has derivative 3: it is the slope of a "
                    "line. The exponent is 2 and gives the leading 2, the constant term 1 "
                    "has derivative 0, and the outer derivative is the `2(3t + 1)`."},
            {"q": "`(t²)³` is `t⁶`. Which product is its derivative by the chain rule?",
             "a": ["`3t²·2t`", "`3t²·t²`", "`3(t²)²`", "`3(t²)²·2t`"],
             "c": 3,
             "why": "The outer derivative `3(·)²` is read at the inner value `t²`, giving "
                    "`3(t²)²`, and the inner derivative is `2t`. Their product is `6t⁵`, the "
                    "derivative of `t⁶` by the power rule. The answer `3t²·2t` reads the "
                    "outer derivative at `t`, `3t²·t²` multiplies by the inner function, "
                    "and `3(t²)²` leaves out the inner derivative."},
        ],
        "mistakes": [
            ("Differentiating the outside and forgetting the inner derivative",
             "For `(3t + 1)²` the outer derivative read at the inner value is "
             "`2(3t + 1) = 6t + 2`. The derivative of the expanded `9t² + 6t + 1` is "
             "`18t + 6`, three times as large. The missing 3 is the slope of the inner "
             "`3t + 1`, and a stretch makes every slope as many times larger as the "
             "stretch."),
            ("Replacing the inner function by t in the outer derivative",
             "For `(t² + 1)³` the outer derivative read at the inner value is "
             "`3(t² + 1)²`. Writing `3t²` instead drops the inside. At `t = 1` the true "
             "slope is `6·1·(1 + 1)² = 24`, the lab's rule tile gives the same, and "
             "`3t²·2t` at `t = 1` is only 6."),
            ("Multiplying by the inner function instead of its derivative",
             "The factor to multiply by is `g′`, not `g`. For `(3t + 1)²`, writing "
             "`2(3t + 1)·(3t + 1)` gives a quadratic, `18t² + 12t + 2`, when the true "
             "derivative `18t + 6` is a line."),
        ],
        "standard": ("Finish when you can differentiate a function of a function by f′(g(t))·g′(t) and confirm it by expanding.",
                     "You should be able to name the outer and inner functions, "
                     "differentiate the outer one and read it at the inner value, multiply by "
                     "the inner derivative, expand to verify, and say what goes wrong when "
                     "the last factor is omitted."),
        "note": "That completes the rules the course needs: the power, product and chain "
                "rules. The last two lessons use them to read how a graph bends, in "
                "&ldquo;The Second Derivative&rdquo;, and then to meet a function whose rate "
                "is a multiple of itself.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "the-second-derivative",
        "title": "The Second Derivative",
        "module": "Second derivatives and the exponential",
        "one_line": "Differentiate twice to get p″, the rate of the rate, and read from its sign where the graph bends up and bends down.",
        "summary": (
            "The derivative is itself a polynomial, so it has a derivative: the second "
            "derivative `p″`, the rate at which the slope is changing. Where `p″` is "
            "positive the slope is rising and the graph bends up; where it is negative the "
            "graph bends down. A place where `p″` changes sign is an inflection point, and "
            "it is a different place from a turn."
        ),
        "key": [
            "p″ = (p′)′, the rate of the rate",
            "p″ > 0: the slope rises, graph bends up",
            "p″ < 0: the slope falls, graph bends down",
            "inflection: p″ changes sign",
            "t³ − 3t²: p″ = 6t − 6, inflection at 1",
            "not where p′ = 0",
        ],
        "key_label": "The second derivative and the bend of a graph",
        "concepts_intro": (
            "Three ideas: what a second derivative measures, how its sign reads as a bend, "
            "and what an inflection point is."
        ),
        "concepts": [
            ("The rate of the rate",
             "If `p` is a position, `p′` is a velocity and `p″` is an acceleration: how "
             "fast the velocity itself is changing. In general `p″` is the derivative of "
             "`p′`, found by applying the power rule a second time: `t³` gives `3t²` "
             "and then `6t`."),
            ("Its sign is the bend",
             "Where `p″` is positive, `p′` is increasing: the tangent slopes get larger as "
             "`t` grows, and the graph bends upward, like a cup. Where `p″` is negative the "
             "slopes get smaller and the graph bends downward, like a cap. A tangent "
             "line lies below a graph that bends up, which is why the estimates in "
             "&ldquo;The Derivative at a Point and the Tangent Line&rdquo; fell short for `t²`."),
            ("An inflection is where the bend changes",
             "An <strong>inflection point</strong> is a place where `p″` changes sign: the "
             "graph stops bending one way and starts bending the other. It is found "
             "from `p″ = 0`, not from `p′ = 0`, and it is not a turn."),
        ],
        "read_title": "Differentiating twice, and reading the bend",
        "read_intro": "The definition, one cubic carried through, the slopes that show the bend, and the two other presets of the lab.",
        "body": [
            ("def", ("The second derivative",
                     "The <strong>second derivative</strong> of a polynomial `p` is the "
                     "derivative of its derivative, written `p″`.",
                     "A graph is <strong>concave up</strong> where `p″ > 0` and "
                     "<strong>concave down</strong> where `p″ < 0`.")),
            ("example", ("A cubic with an S in it",
                         "Let `p(t) = t³ − 3t²`. Then `p′(t) = 3t² − 6t` and "
                         "`p″ = 6t − 6 = 6(t − 1)`.",
                         "The second derivative is negative for `t < 1`, zero at 1 and positive "
                         "for `t > 1`, so the graph bends down and then bends up, and "
                         "`t = 1` is an inflection point.")),
            ("p", "The slopes make the bend visible. For this cubic the slope "
                  "`p′ = 3t² − 6t` is 0 at `t = 0`, then −3 at `t = 1`, then 0 at `t = 2`, "
                  "then 9 at `t = 3`. Up to `t = 1` the slopes are shrinking from 0 to −3, "
                  "which is a falling slope, and after it they grow from −3 to 0 to 9. "
                  "The slope bottoms out at 1, exactly where `p″` is zero."),
            ("math", [
                "p″ = 6(t − 1)",
                "",
                "   t < 1      p″ < 0     slope falling    bends down",
                "   t > 1      p″ > 0     slope rising     bends up",
            ]),
            ("h3", "An inflection is not a turn"),
            ("p", "The turns of this graph are at the zeros of `p′ = 3t·(t − 2)`, which are "
                  "`t = 0`, a maximum, and `t = 2`, a minimum. The inflection at `t = 1` is "
                  "between them, and there `p′ = −3`, not zero: the graph is steeply "
                  "falling as it passes through. Of the two questions, where does the "
                  "graph turn and where does it change its bend, the first reads `p′` and "
                  "the second reads `p″`."),
            ("p", "The second derivative also corrects one reading of the sign. Concave up "
                  "does not mean rising. The parabola `t²` has `p″ = 2`, positive for every "
                  "`t`, and it falls for every negative `t`. The bend and the direction "
                  "are separate facts, one from `p″` and the other from `p′`."),
            ("example", ("A quartic with two inflections",
                         "Let `p(t) = t⁴ − 6t²`. Then `p′ = 4t³ − 12t` and "
                         "`p″ = 12t² − 12 = 12(t − 1)(t + 1)`.",
                         "The second derivative is positive for `t < −1`, negative for "
                         "`−1 < t < 1` and positive for `t > 1`, so there are two "
                         "inflection points, at `t = −1` and `t = 1`. The graph is a "
                         "W with its middle hump bending down.")),
            ("p", "This lab is set to show the second derivative as well, so it prints "
                  "`p″` and the inflection points beside the zeros and intervals of "
                  "`p′`. Its zero tile lists only zeros of `p′` that are fractions, so "
                  "for this quartic it names `t = 0` and leaves the turns at "
                  "`±√3` to the interval tile, which places them with square roots."),
            ("p", "A parabola is the plainest case: `p = t²` has `p″ = 2`, which never "
                  "changes sign, so the graph bends up everywhere and has no inflection."),
        ],
        "lab": ("calckit", {
            "mode": "derivative",
            "order": 2,
            "preset": "s-curve",
            "presets": [
                {"id": "s-curve", "label": "t³ − 3t², one inflection", "f": "t^3 - 3t^2",
                 "expect": {'dvSecond': '6t − 6', 'dvInflect': 't = 1'}},
                {"id": "quartic", "label": "t⁴ − 6t², two inflections", "f": "t^4 - 6t^2",
                 "expect": {'dvSecond': '12t² − 12', 'dvInflect': 't = −1, 1'}},
                {"id": "parabola", "label": "t², bends up everywhere", "f": "t^2",
                 "expect": {'dvSecond': '2', 'dvInflect': 'none'}},
            ],
            "panel_title": "Differentiate twice and find the bend",
            "panel_intro": "Type a polynomial in t. The lab differentiates it twice and prints p″ "
                           "and the places where p″ changes sign. The plot shows p, p′ and p″ "
                           "together; p bends up where the third curve is above the axis and bends "
                           "down where it is below.",
        }),
        "steps_title": "Reading the bend of a polynomial",
        "steps_intro": "Five moves. Differentiate twice, then treat p″ exactly as p′ was treated for turns.",
        "steps": [
            ("Differentiate twice",
             "Apply the power rule to `p`, and apply it again to the result. Write `p′` and "
             "`p″` in descending powers."),
            ("Solve p″ = 0",
             "These are the only places the bend can change. Factor the result if it "
             "factors."),
            ("Test the sign of p″ in every region",
             "Put one value of `t` from each region into `p″`. Positive is concave up, "
             "negative is concave down."),
            ("Mark an inflection only where the sign changes",
             "A zero of `p″` with the same sign on both sides is not an inflection. The "
             "bend has to change."),
            ("Keep it apart from the turns",
             "The turns are zeros of `p′` and the inflections are zeros of `p″`. Check by "
             "putting the inflection into `p′`: it is usually not zero."),
        ],
        "worked": {
            "title": "t³ − 3t², turns and bends",
            "intro": [
                "The polynomial is `p(t) = t³ − 3t²`. Both derivatives, the signs and the "
                "two kinds of special place are exact.",
            ],
            "lines": [
                "p′(t) = 3t² − 6t = 3t·(t − 2)",
                "p″ = 6t − 6 = 6(t − 1)",
                "",
                "t = 0:   p″ = −6    concave down",
                "t = 2:   p″ = 6     concave up",
                "p″ changes sign at t = 1:  inflection",
                "",
                "at t = 1:  p = −2,  p′ = −3  (not zero: no turn)",
                "turns, from p′ = 0:  t = 0 (maximum), t = 2 (minimum)",
            ],
            "after": [
                "The lab's second-derivative tile prints `6t − 6` and its inflection tile "
                "prints the single place `t = 1`. The three special places, 0, 1 and 2, "
                "are all different.",
                "For a rehearsal, find `p″` for `t⁴`, which is `12t²`. It is zero at 0 "
                "and positive on both sides; decide whether 0 is an inflection.",
            ],
        },
        "quiz_title": "Slopes of slopes",
        "quiz": [
            {"q": "What is the second derivative of `p(t) = t⁴`?",
             "a": ["`4t³`", "`12t`", "`24t`", "`12t²`"],
             "c": 3,
             "why": "The first derivative is `4t³`, and differentiating that gives `12t²`. "
                    "The answer `4t³` is only the first derivative, `12t` forgets the "
                    "exponent, and `24t` differentiates three times."},
            {"q": "If `p″ = 6t − 6`, on which values of `t` is the graph of `p` concave down?",
             "a": ["`t < 1`", "`t > 1`", "`t < 6`", "Every `t`"],
             "c": 0,
             "why": "`6t − 6 < 0` exactly when `t < 1`. Concave down is the negative case. "
                    "The set `t > 1` is where `p″` is positive, and `t < 6` comes from "
                    "dropping the coefficient of `t` in `6t < 6`."},
            {"q": "For `p(t) = t³`, both `p′ = 3t²` and `p″ = 6t` are zero at `t = 0`. Is `t = 0` an inflection point?",
             "a": ["No, because `p′` is zero there",
                   "Yes, because `p′` is zero there",
                   "Yes, because `p″` changes sign there, from negative to positive",
                   "No, because `p″` is zero there"],
             "c": 2,
             "why": "`6t` is negative for `t < 0` and positive for `t > 0`, so the bend does "
                    "change at 0: that is what makes it an inflection. A zero of `p′` is "
                    "irrelevant to inflections, and a zero of `p″` is necessary but "
                    "not enough, since the sign has to change."},
            {"q": "A graph's tangent slopes at `t = 0, 1, 2` are `−4, −1, 3`. What do they say about the bend there?",
             "a": ["The slope is falling, so the graph bends down",
                   "The slope is rising, so the graph bends up",
                   "The slope is constant, so the graph is a line",
                   "The graph is falling throughout"],
             "c": 1,
             "why": "The slopes increase from `−4` to `−1` to 3, so the slope is rising, which "
                    "is a positive second derivative and a bend upward. The graph falls at "
                    "first and rises by `t = 2`, so it is not falling throughout, and "
                    "slopes that change are not a line."},
        ],
        "mistakes": [
            ("Taking an inflection point to be where p′ is zero",
             "For `t³ − 3t²` the zeros of `p′ = 3t·(t − 2)` are 0 and 2, and those are the "
             "turns. The inflection is at 1, where `p′ = −3` is far from zero and the graph "
             "is falling steeply. Ask where the graph turns and read `p′`; ask where the "
             "bend changes and read `p″`."),
            ("Reading concave up as rising",
             "Concave up means the slope is increasing, not that it is positive. The "
             "parabola `t²` has `p″ = 2` everywhere and falls for all `t < 0`. A cup can be "
             "descending into its bottom as well as climbing out of it."),
            ("Calling every zero of p″ an inflection point",
             "The second derivative of `t⁴` is `12t²`, zero at 0 and positive on both "
             "sides. The graph bends up on both sides of 0 and does not change its "
             "bend, so there is no inflection. As with the turns, the zero is a place to "
             "look, and the sign on each side decides."),
        ],
        "standard": ("Finish when you can differentiate a polynomial twice, read where its graph bends up and down from the sign of p″, and locate the inflection points.",
                     "You should be able to apply the power rule twice, solve `p″ = 0`, test "
                     "the sign on each side, keep the inflections apart from the turns, and "
                     "say in a sentence what a second derivative measures."),
        "note": "With the rules and the second derivative the course has what it needs for "
                "polynomials. The last lesson meets a function that is not a polynomial and "
                "whose rate is a multiple of itself, in &ldquo;The Exponential and Its "
                "Rate&rdquo;.",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "the-exponential-and-its-rate",
        "title": "The Exponential and Its Rate",
        "module": "Second derivatives and the exponential",
        "one_line": "The quotient of bᵗ is bᵗ times a factor that does not depend on t, so the rate of an exponential is a constant multiple of itself.",
        "summary": (
            "An exponential has its variable in the exponent, and its difference quotient "
            "factors exactly: `bᵗ` times a quotient that does not contain `t`. That second "
            "factor is a column of rounded numbers, and the lesson states, without proving "
            "it, that the column settles on a constant. The rate of `bᵗ` is that constant "
            "times `bᵗ`, and `e` is the base whose constant is 1."
        ),
        "key": [
            "b^(a + h) − b^a = b^a·(b^h − 1)",
            "the quotient is b^a·(b^h − 1)/h",
            "the second factor does not contain a",
            "(bᵗ)′ = (a constant)·bᵗ",
            "the constant for 2 is ln 2 ≈ 0.693147",
            "e is the base whose constant is 1",
        ],
        "key_label": "The quotient of an exponential",
        "concepts_intro": (
            "Three ideas: the exact factoring, what the column of the remaining factor "
            "claims, and why this is not the power rule."
        ),
        "concepts": [
            ("The quotient factors exactly",
             "The law of exponents from Algebra's Exponential and Logarithmic Functions "
             "says `b^(a + h) = b^a·b^h`. So `b^(a + h) − b^a = b^a·(b^h − 1)`, and "
             "dividing by `h` gives `b^a·(b^h − 1)/h`. The second factor contains the "
             "step `h` and the base `b`, and nothing about the place `a`."),
            ("One column serves every place",
             "At `a = 0`, `b^a = 1`, so the quotient there is the second factor alone. "
             "That one column, for halving `h`, is the same at every place after "
             "multiplying by `b^a`. The lesson states that the column settles on one "
             "constant. A table of rounded rows illustrates this and does not prove it."),
            ("The variable is in the exponent",
             "The power rule differentiates `tⁿ`, with the variable in the base and the "
             "exponent fixed. In `2ᵗ` it is the other way round, and the rule does not "
             "apply. The rate of `2ᵗ` is proportional to `2ᵗ` itself, with a "
             "constant of proportion, and `e` is the base for which that constant is 1."),
        ],
        "read_title": "A column of rounded quotients and the constant it heads for",
        "read_intro": "The factoring, the column for the base 2, what is exact and what is rounded, the other bases, and the failure of the power rule.",
        "body": [
            ("p", "Apart from `1/t`, everything before this lesson was a polynomial, whose "
                  "quotient is a polynomial in the step and comes out exact. An exponential "
                  "is not a polynomial, and for most bases and steps its quotient is no "
                  "longer a fraction, so for the first time in the course some figures are "
                  "rounded."),
            ("math", [
                "b^(a + h) − b^a = b^a·b^h − b^a",
                "                = b^a·(b^h − 1)",
                "",
                "(b^(a + h) − b^a)/h = b^a·(b^h − 1)/h",
            ]),
            ("p", "That is exact algebra and nothing is dropped. Every quotient of `bᵗ` at "
                  "every place is the base raised to the place, times the quotient at the "
                  "place 0. Everything depends on the second factor, so look at it for "
                  "`b = 2`."),
            ("p", "At `h = 1` it is `(2 − 1)/1 = 1`, exactly, because the base is a whole "
                  "number and the step is 1. At `h = 1/2` it is `(√2 − 1)/(1/2) = "
                  "2(√2 − 1)`, which has no finite decimal, and the lab prints "
                  "`≈ 0.828427`. From the second row on, every figure in the table is rounded "
                  "to six significant figures and carries the sign `≈`."),
            ("math", [
                "b = 2,  a = 0,   (2^h − 1)/h",
                "",
                "   h        quotient",
                "   1          1          exact",
                "   1/2     ≈ 0.828427    rounded",
                "   1/4     ≈ 0.756828    rounded",
                "   1/8     ≈ 0.724062    rounded",
                "   1/16    ≈ 0.708381    rounded",
                "   1/32    ≈ 0.700709    rounded",
                "   1/64    ≈ 0.696914    rounded",
            ]),
            ("thm", ("The exponential's rate",
                     "For each base `b > 0` the quotients `(b^h − 1)/h` for halving `h` head "
                     "for a number written `ln b`. Then the rate of `bᵗ` at every `t` is "
                     "`ln b` times `bᵗ`. The base `e ≈ 2.71828` is the one with `ln e = 1`, "
                     "so `(eᵗ)′ = eᵗ`.",)),
            ("p", "This is stated and not proved. The factoring above is proved; that the "
                  "rounded column settles on one number is what the table suggests and the "
                  "lab shows for each base, and no table of seven rows establishes it for "
                  "every step. For `b = 2` the column heads for `ln 2 ≈ 0.693147`, "
                  "the way the quotients of `t²` headed for 2."),
            ("h3", "Other bases, and the one where the constant is 1"),
            ("p", "For `b = 3` the first quotient is `(3 − 1)/1 = 2`, exact, and the "
                  "column heads for `ln 3 ≈ 1.09861`. For `b = e`, entered in the lab as "
                  "`e`, every quotient is rounded, since `e` itself is not a fraction: "
                  "the first is `e − 1 ≈ 1.71828`, and the column heads for 1. "
                  "That is the definition of the number: of all the bases, `e` is the one for "
                  "which the exponential's rate is the exponential itself."),
            ("h3", "The same column at another place"),
            ("p", "At `a = 3`, with `b = 2`, the quotient at `h = 1` is `(16 − 8)/1 = 8`, "
                  "exactly `2³` times the first entry of the column above. Every later "
                  "row is `8` times the matching row of that column, so the rate of "
                  "`2ᵗ` at 3 is `8·ln 2 ≈ 5.54518`, rounded. The lab's ratio tile "
                  "divides the last quotient by `2³` and gets back the column at 0."),
            ("h3", "Why the power rule is not allowed here"),
            ("p", "Applying the power rule to `2ᵗ` would give `t·2^(t − 1)`. At `t = 0` that "
                  "is 0, but the quotients of `2ᵗ` at 0 head for `≈ 0.693147`. The "
                  "power rule belongs to a variable base and a fixed exponent. When the "
                  "variable is in the exponent, the rate is proportional to the function."),
            ("p", "A quantity whose rate is a constant multiple of itself is exactly what "
                  "the equation `y′ = k·y` says, and this lesson has shown that exponentials "
                  "have the property. That equation opens the second half of this Subject, "
                  "in Separable Equations, Growth and Decay."),
        ],
        "lab": ("calckit", {
            "mode": "transcendental",
            "preset": "two",
            "presets": [
                {"id": "two", "label": "2ᵗ at 0, six halvings", "kind": "exp", "b": "2", "a": 0,
                 "h": 1, "halvings": 6, "expect": {'tqFirst': '1', 'tqLimit': 'ln 2 ≈ 0.693147', 'tqRatio': '≈ 0.696914'}},
                {"id": "three", "label": "3ᵗ at 0, six halvings", "kind": "exp", "b": "3", "a": 0,
                 "h": 1, "halvings": 6, "expect": {'tqFirst': '2', 'tqLimit': 'ln 3 ≈ 1.09861', 'tqRatio': '≈ 1.1081'}},
                {"id": "e", "label": "eᵗ at 0, the base whose constant is 1", "kind": "exp", "b": "e",
                 "a": 0, "h": 1, "halvings": 6, "expect": {'tqFirst': '≈ 1.71828', 'tqLimit': 'ln e = 1', 'tqRatio': '≈ 1.00785'}},
                {"id": "two-at-3", "label": "2ᵗ at 3, eight times the column at 0", "kind": "exp",
                 "b": "2", "a": 3, "h": 1, "halvings": 6, "expect": {'tqFirst': '8', 'tqLimit': '8·ln 2 ≈ 5.54518', 'tqRatio': '≈ 0.696914'}},
            ],
            "panel_title": "The quotients of an exponential, rounded and labelled",
            "panel_intro": "Choose a base, a place and a first step. Each row halves the step. "
                           "The first row is exact when the base is a fraction such as 2 or 3/2, the "
                           "place is a whole number and the step is 1; every other figure is "
                           "rounded to six significant figures and "
                           "carries the sign ≈. The ratio tile divides the last quotient by the "
                           "function's value at the place.",
        }),
        "steps_title": "Reading the rate of an exponential",
        "steps_intro": "Five moves. The first is exact algebra and the rest read a rounded table, so keep the two apart.",
        "steps": [
            ("Factor the quotient",
             "Write `b^(a + h)` as `b^a·b^h`, take out `b^a`, and the quotient is "
             "`b^a·(b^h − 1)/h`. This step is exact."),
            ("Build the column at a = 0",
             "At `a = 0` the factor `b^a` is 1, so the quotient is `(b^h − 1)/h`. Halve the "
             "step row by row. For the bases 2 and 3 only the first entry is a fraction, and "
             "the lab prints every later one rounded."),
            ("Read each figure with its sign",
             "Every figure with `≈` is a rounded decimal of a number with no finite decimal. "
             "Never quote one as exact, and never read the last row as the constant itself."),
            ("Multiply by b^a for another place",
             "The quotient at `a` is `b^a` times the column at 0, so the constant the "
             "column heads for is the same at every place."),
            ("Name the constant",
             "For `b = 2` it is `ln 2 ≈ 0.693147`, for `b = 3` it is `ln 3 ≈ 1.09861`, and for "
             "`b = e` it is exactly 1."),
        ],
        "worked": {
            "title": "2ᵗ at 0, then at 3",
            "intro": [
                "The first row is exact. Every row after it is rounded to six "
                "significant figures, and the lab says so beside it.",
            ],
            "lines": [
                "a = 0:  b^a = 1, so the quotient is (2^h − 1)/h",
                "h = 1:    (2 − 1)/1 = 1                    exact",
                "h = 1/2:  2(√2 − 1)             ≈ 0.828427   rounded",
                "h = 1/64:                       ≈ 0.696914   rounded",
                "heads for  ln 2 ≈ 0.693147",
                "",
                "a = 3:  b^a = 8",
                "h = 1:    (16 − 8)/1 = 8                   exact",
                "h = 1/64: 8·(the column at 0)   ≈ 5.57531   rounded",
                "heads for  8·ln 2 ≈ 5.54518",
            ],
            "after": [
                "The factoring is exact, so the second block is the first multiplied by 8 "
                "row for row. The constant is claimed, and the lab shows the "
                "column sinking toward it.",
                "For a rehearsal, take `b = 3` at `a = 0`: the first entry is 2, and the "
                "column should head for `≈ 1.09861`, which is `ln 3`.",
            ],
        },
        "quiz_title": "Exponents, columns and constants",
        "quiz": [
            {"q": "Which expression is equal to `(3^(t + h) − 3^t)/h`?",
             "a": ["`3^t·(3^h − 1)/h`", "`3^h·(3^t − 1)/h`", "`(3^t·3^h)/h`", "`(3^t − 1)/h`"],
             "c": 0,
             "why": "Since `3^(t + h) = 3^t·3^h`, the numerator is `3^t·3^h − 3^t = 3^t·(3^h − 1)`. "
                    "The second choice takes out `3^h`, which `3^t` does not contain. The third "
                    "forgets to subtract, and the fourth drops the factor `3^h`."},
            {"q": "The quotients of `2ᵗ` at `t = 0` head for `≈ 0.693147`. What do the quotients at `t = 3` head for?",
             "a": ["`≈ 0.693147`, the same", "`≈ 2.07944`", "`≈ 5.54518`", "12"],
             "c": 2,
             "why": "The quotient at 3 is `2³ = 8` times the quotient at 0, so it heads for "
                    "`8·ln 2 ≈ 5.54518`. The same number would need no factor of 8, "
                    "`≈ 2.07944` is `3` times `ln 2`, and 12 is what the power rule would "
                    "give, `3·2²`."},
            {"q": "Which base `b` has `(bᵗ)′ = bᵗ`?",
             "a": ["`b = 1`", "`b = 2`", "`b = 3`", "`b = e`"],
             "c": 3,
             "why": "The base `e ≈ 2.71828` is the one whose column heads for 1. The base 1 gives "
                    "the constant function 1, whose derivative is 0, and the bases 2 and 3 "
                    "give the constants `≈ 0.693147` and `≈ 1.09861`."},
            {"q": "Why does the power rule give the wrong rate for `2ᵗ`?",
             "a": ["It is correct, because the power rule applies to every function",
                   "At `t = 0` it gives 0, but the quotients of `2ᵗ` head for `≈ 0.693147`",
                   "It gives a negative rate at `t = 0`",
                   "It would be correct if the base were `e`"],
             "c": 1,
             "why": "The power rule differentiates a variable raised to a fixed power. "
                    "`t·2^(t − 1)` is 0 at `t = 0`, while the rounded column there heads "
                    "for `≈ 0.693147`. The last choice is false too: `t·e^(t − 1)` is not "
                    "`eᵗ`, which is the rate of `eᵗ`."},
        ],
        "mistakes": [
            ("Applying the power rule to an exponential",
             "The derivative of `2ᵗ` is not `t·2^(t − 1)`. At `t = 0` that gives 0, but "
             "the quotients of `2ᵗ` at 0 are `1, ≈ 0.828427, ≈ 0.756828, …`, heading for "
             "`≈ 0.693147`. In `2ᵗ` the variable is in the exponent, and the rate is a "
             "constant times `2ᵗ`."),
            ("Quoting a rounded figure as if it were exact",
             "`≈ 0.828427` is a decimal approximation of `2(√2 − 1)`, and `ln 2 ≈ 0.693147` "
             "has no finite decimal either. Write `≈` whenever a figure was rounded, and "
             "read the last row of the column as a step on the way to the constant and not "
             "the constant."),
            ("Expecting the constant to change with the place",
             "The quotients at `a = 3` are eight times those at `a = 0`, but the factor "
             "`(2^h − 1)/h` is the same. The ratio tile divides the place's value out "
             "and gets the same column back. The rate depends on where you are only through "
             "the factor `b^a`."),
        ],
        "standard": ("Finish when you can factor the quotient of an exponential, read the remaining factor from a rounded column, and state the rate of bᵗ as a constant times bᵗ.",
                     "You should be able to write the quotient of `bᵗ` as `b^a·(b^h − 1)/h`, "
                     "say which entries of the column are exact and which are rounded, name the "
                     "constant for a given base, and say why the power rule does not apply."),
        "note": "That ends the course. A rate has been computed as a fraction, read as a "
                "derivative, found by rule, and applied to the shape of a graph. The next "
                "course, Accumulation and the Integral, runs the other way: given the "
                "rate, recover the quantity.",
    },
]
