"""Course 1, lessons 01-05 - ranges, rates, and the first two things a rate sizes."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "orders-of-magnitude",
        "title": "Orders of Magnitude",
        "module": "Ranges and rates",
        "one_line": "Multiply three factors that are ranges and report the interval and its width, not a single number.",
        "summary": (
            "An estimate is not a number. It is an interval, because every factor "
            "that goes into it is one, and intervals multiply end to end. The "
            "arithmetic takes a line; the consequence takes the rest of the course. "
            "Three factors each known to within a factor of two give a product "
            "known to within a factor of eight, and an answer that arrives as a "
            "single number is not more precise than that, it is only quieter about it."
        ),
        "key": [
            "known to ±2×        is the interval [c/2, 2c]",
            "[a₁,a₂] · [b₁,b₂]  =  [a₁b₁, a₂b₂]      positive factors",
            "±2× · ±2× · ±2×  ⟹  ÷8 … ×8            the half-widths MULTIPLY",
            "10⁷ · 10² · 10³ = 10¹²  centre          [1.25·10¹¹, 8·10¹²]",
            "width = hi/lo = 64×                     centre = √(lo·hi), not (lo+hi)/2",
        ],
        "key_label": "One factor as an interval, and what three of them make",
        "concepts_intro": (
            "One idea, carried through three steps: the factors are intervals, the "
            "product of intervals is an interval, and the middle of that interval "
            "is not where addition would put it."
        ),
        "concepts": [
            ("An estimate is an interval, and the interval is the estimate",
             "Nobody knows that a service has ten million daily users. What is "
             "known is that it has somewhere between five and twenty million, and "
             "`10⁷` is the middle of that. Writing the factor as `[5·10⁶, 2·10⁷]` "
             "rather than as `10⁷` loses nothing and records what was actually "
             "known. A factor known to within a factor of `k` is the interval "
             "`[c/k, ck]`, and `k = 1` &mdash; a factor you measured &mdash; is the "
             "case where the interval has one point in it."),
            ("Intervals multiply end to end",
             "For positive factors the smallest product comes from the smallest "
             "ends and the largest from the largest ends, so `[a₁,a₂]·[b₁,b₂]` is "
             "`[a₁b₁, a₂b₂]` and nothing in between needs checking. The half-widths "
             "therefore multiply rather than add: `2 · 2 · 2 = 8`, so three factors "
             "at `±2×` give a product at `÷8 … ×8`, and the interval is `64×` wide "
             "from end to end."),
            ("The centre of a multiplicative range is its geometric mean",
             "The interval `[1.25·10¹¹, 8·10¹²]` has arithmetic midpoint "
             "`4.0625·10¹²`, which is `65/16` times the product of the central "
             "values it was built from. Averaging an end that is eight times too "
             "small with an end that is eight times too large does not land in the "
             "middle of a range built by multiplying; `√(lo·hi)` does, and here it "
             "returns `10¹²` exactly."),
        ],
        "read_title": "Factors that are ranges, and the range their product lives in",
        "read_intro": "What a factor known to within a factor means, how two of them multiply, and where the middle of the answer is.",
        "body": [
            ("def", ("Ranged factor",
                     "A quantity known to within a factor of `k > 1`, with central "
                     "value `c`, is the interval `[c/k, ck]`. `k` is its "
                     "<strong>half-width</strong>, written `±k×` and read &ldquo;to "
                     "within a factor of `k`&rdquo;. The interval&rsquo;s "
                     "<strong>width</strong> is the ratio of its ends, `hi/lo = k²`, "
                     "and `k = 1` describes a quantity that is known.")),
            ("p", "The half-width is a factor and not a percentage, and the "
                  "difference is the whole reason this works. A factor of two "
                  "downward is `-50%` and a factor of two upward is `+100%`, so a "
                  "quantity known to `±2×` is not known to `±50%` of anything; it "
                  "is known to one multiplicative step either side. Multiplicative "
                  "steps are what a capacity estimate is made of, and they compose "
                  "by multiplying."),
            ("thm", ("The product of two positive intervals",
                     "If `a ∈ [a₁, a₂]` and `b ∈ [b₁, b₂]` with all four ends "
                     "positive, then `ab ∈ [a₁b₁, a₂b₂]`, and both ends are attained.")),
            ("proof", [
                "Multiplication by a positive number preserves order. From "
                "`a ≥ a₁ > 0` and `b ≥ b₁ > 0` we get `ab ≥ a₁b ≥ a₁b₁`, and from "
                "`a ≤ a₂` and `b ≤ b₂` we get `ab ≤ a₂b ≤ a₂b₂`. So every product "
                "lies in `[a₁b₁, a₂b₂]`.",
                "Both ends are reached: `a = a₁, b = b₁` gives the low end and "
                "`a = a₂, b = b₂` gives the high end. The interval is therefore "
                "exactly the set of possible products and not merely a bound on it.",
            ]),
            ("p", "Applied to `[c/k, ck]` and `[d/m, dm]`, the product is "
                  "`[cd/(km), cd·km]` &mdash; a ranged factor again, with central "
                  "value `cd` and half-width `km`. That is the whole result: "
                  "<strong>half-widths multiply</strong>. Three factors at `±2×` "
                  "give `÷8 … ×8`; four give `÷16 … ×16`; and a factor you know "
                  "exactly contributes `k = 1` and does not widen anything."),
            ("math", [
                "daily users            10⁷        ±2×     [5·10⁶,  2·10⁷]",
                "actions per user/day   10²        ±2×     [50,      200]",
                "bytes per action       10³        ±2×     [500,     2 000]",
                "",
                "product                10¹²       ÷8 … ×8 [1.25·10¹¹, 8·10¹²]",
                "width                  8 · 8 = 64×",
            ]),
            ("example", ("Ten million users, a hundred actions, a kilobyte",
                         "The central values multiply to `10¹²` bytes a day &mdash; "
                         "a terabyte, on the decimal convention this course uses "
                         "throughout. The low end is `1.25·10¹¹` bytes and the high "
                         "end is `8·10¹²`, so the honest report is &ldquo;between "
                         "125 gigabytes and 8 terabytes a day, centred on a "
                         "terabyte&rdquo;. Every one of those figures is in the lab, "
                         "and moving any slider moves all of them at once.")),
            ("h3", "Reporting the width"),
            ("p", "There are two useful ways to say how wide an answer is and they "
                  "are not the same number. `÷8 … ×8` is the half-width and is what "
                  "you carry into the next multiplication. `64×` is the width end "
                  "to end, `hi/lo`, and is what tells you whether the answer is "
                  "worth acting on. The lab prints both, and prints the width in "
                  "powers of ten as well: `64×` sits between `10¹` and `10²`, which "
                  "is `1.81` powers of ten."),
            ("p", "The bracket is the form worth remembering. &ldquo;This answer is "
                  "good to within two orders of magnitude&rdquo; is a sentence a "
                  "reader can act on; `1.81` is a decimal that suggests a precision "
                  "the estimate does not have. The decimal is a gloss on the "
                  "bracket, and the lab labels it as one."),
            ("h3", "Where the middle is"),
            ("p", "The interval `[1.25·10¹¹, 8·10¹²]` has an arithmetic midpoint of "
                  "`4.0625·10¹²`. That is `65/16` times the product of the central "
                  "values, so the midpoint of the range is four times the estimate "
                  "the range was built around. Nothing has gone wrong: an average "
                  "of two numbers that differ by a factor of sixty-four is dragged "
                  "to the larger one, because `8·10¹²` is sixty-four times the "
                  "weight of `1.25·10¹¹` on a number line and the same distance "
                  "from the centre on a ratio scale."),
            ("p", "The centre of a range built by multiplying is the geometric mean "
                  "`√(lo·hi)`. Here `√(1.25·10¹¹ · 8·10¹²) = 10¹²` exactly, which is "
                  "where the estimate started. Whenever the half-widths are "
                  "symmetric &mdash; every `±k×` factor &mdash; the geometric centre "
                  "comes out exactly at the product of the central values, and the "
                  "lab says so; where a factor is skewed, say `÷2 … ×3`, the root is "
                  "irrational and the lab prints it rounded and labels it."),
            ("p", "The point of carrying the range is not humility, it is "
                  "direction. Three factors at `±2×` contribute equally, so there is "
                  "nothing to choose between them; make one of them `±10×` and it "
                  "supplies `10` of the `40` half-width on its own, and measuring "
                  "<em>that</em> factor is the only thing that narrows the answer. "
                  "The widest factor is the work item."),
        ],
        "lab": ("estimate", {
            "mode": "magnitude",
            "preset": "ten-million-users",
            "panel_title": "Set each factor, then say how well you know it",
            "panel_intro": "Move the three central values and the three half-widths. "
                           "The product interval, its width as a factor and in powers "
                           "of ten, the geometric centre and the arithmetic midpoint "
                           "all redraw together. Set one factor to &ldquo;known "
                           "exactly&rdquo; and watch which part of the width goes away.",
        }),
        "steps_title": "Estimating a quantity that is a product of three things",
        "steps_intro": "The factors first, then how well each is known, then one multiplication down each column.",
        "steps": [
            ("Write the factors on separate lines, with units",
             "One line per factor, each carrying the unit it contributes: `users`, "
             "`actions / user / day`, `bytes / action`. The units have to cancel "
             "down to the unit you asked for, and if they do not, the factor list "
             "is wrong before any arithmetic happens."),
            ("Give each factor a half-width, as a factor and not a percentage",
             "`±2×` for something you have seen a number for, `±10×` for something "
             "you are inventing, `±1×` for something you measured. Guessing the "
             "half-width is easier than guessing the value and it is the input that "
             "decides how much the answer is worth."),
            ("Multiply the low ends, then multiply the high ends",
             "Two independent multiplications, each down one column. The central "
             "values multiply too, and the three half-widths multiply into the "
             "product&rsquo;s half-width. Nothing in between the ends ever has to "
             "be checked, because all the factors are positive."),
            ("Report the interval, the width and the centre",
             "`[lo, hi]`, the width as `hi/lo`, and the geometric centre. Quote the "
             "width in powers of ten as well: an answer good to one order of "
             "magnitude and an answer good to three are different kinds of object "
             "and only the bracket says which you have."),
            ("Name the widest factor, and say what would narrow it",
             "The factor with the largest half-width supplies most of the product's "
             "width, and it is the only one worth measuring. An estimate that ends "
             "&ldquo;and the number to go and find out is bytes per action&rdquo; is "
             "finished; one that ends with a single number is not."),
        ],
        "worked": {
            "title": "10⁷ users × 10² actions × 10³ bytes, each known to ±2×",
            "intro": [
                "The quantity wanted is bytes written per day. Three factors, each "
                "known to within a factor of two, and two multiplications."
            ],
            "lines": [
                "factor                  central     known to    low          high",
                "daily users             10 000 000  ±2×         5 000 000    20 000 000",
                "actions / user / day    100         ±2×         50           200",
                "bytes / action          1 000       ±2×         500          2 000",
                "",
                "low end    5 000 000 · 50 · 500      = 125 000 000 000        = 1.25·10¹¹",
                "high end   20 000 000 · 200 · 2 000  = 8 000 000 000 000      = 8·10¹²",
                "centre     10 000 000 · 100 · 1 000  = 1 000 000 000 000      = 10¹²",
                "",
                "half-width      2 · 2 · 2 = 8              ÷8 … ×8",
                "width           8 000 000 000 000 / 125 000 000 000 = 64×",
                "                10¹ ≤ 64 < 10²             1.81 powers of ten",
                "",
                "geometric centre   √(1.25·10¹¹ · 8·10¹²) = √(10²⁴) = 10¹²   exact",
                "arithmetic midpoint (1.25·10¹¹ + 8·10¹²)/2 = 4 062 500 000 000",
                "                    4.0625·10¹² / 10¹² = 65/16 = 4.0625×",
            ],
            "after": [
                "The two lines at the bottom are the ones to sit with. The "
                "geometric centre lands exactly on the product of the central "
                "values, which is the sense in which `10¹²` was the estimate all "
                "along. The arithmetic midpoint lands at `65/16` of it &mdash; four "
                "times the answer &mdash; not because of a mistake but because "
                "averaging is the wrong operation on a range built by multiplying.",
                "For a faded rehearsal, keep the same three factors and change one "
                "thing: make bytes per action `±10×` instead of `±2×`. The supplied "
                "first move is that the half-width is now `2 · 2 · 10 = 40`. Work "
                "out the new `[lo, hi]`, the new width as a factor, and which decade "
                "bracket it falls in &mdash; then check all three against the lab "
                "by moving that one slider.",
                "Then answer the question the numbers are for: of the three "
                "factors, which one would you go and measure, and how much would "
                "measuring it narrow the answer? Say the new half-width out loud "
                "before you look.",
            ],
        },
        "quiz_title": "Intervals and their products",
        "quiz": [
            {"q": "Three factors are each known to `±2×`. The low end of their product is the product of the central values divided by what?",
             "a": ["`2`", "`6`", "`8`", "`64`"],
             "c": 2,
             "why": "The half-widths multiply: `2 · 2 · 2 = 8`, so the product is "
                    "`÷8 … ×8`. `6` adds them instead. `2` treats the width as "
                    "though it did not accumulate at all. `64` is the width from "
                    "end to end, `hi/lo`, which is `8 · 8` &mdash; a correct figure "
                    "about the same interval, but not the divisor that reaches the "
                    "low end from the centre."},
            {"q": "The product interval is `[1.25·10¹¹, 8·10¹²]` and the central values multiply to `10¹²`. What is the arithmetic midpoint of the interval?",
             "a": ["`10¹²`", "`4.0625·10¹²`", "`4.5·10¹²`", "`2·10¹²`"],
             "c": 1,
             "why": "`(1.25·10¹¹ + 8·10¹²)/2 = 4.0625·10¹²`, which is `65/16` times "
                    "the estimate. `10¹²` is the geometric centre, which is a "
                    "different average of the same two numbers. `4.5·10¹²` is the "
                    "midpoint of `[10¹², 8·10¹²]`, ignoring the low end. `2·10¹²` "
                    "is nothing in particular, which is what a plausible-looking "
                    "capacity figure usually is."},
            {"q": "A fourth factor is added to the estimate, and it is a quantity you have measured. What happens to the width of the product?",
             "a": ["It is unchanged", "It doubles", "It grows by whatever the fourth factor is", "It cannot be computed until the fourth factor is ranged too"],
             "c": 0,
             "why": "A measured factor is the interval `[c, c]`, half-width `1`, and "
                    "`8 · 1 = 8`. The product moves &mdash; the central value is "
                    "four factors now &mdash; but the width does not, which is the "
                    "whole argument for going and measuring something: it is the "
                    "only operation that makes an estimate narrower rather than "
                    "merely larger."},
        ],
        "mistakes": [
            ("Averaging the two ends of a multiplicative range",
             "For `[1.25·10¹¹, 8·10¹²]` the arithmetic midpoint is `4.0625·10¹²`, "
             "which is `65/16` times the estimate the interval was built around. "
             "The reason is not subtle once seen: the high end is sixty-four times "
             "the low end, so it dominates any sum they appear in. The centre of a "
             "range made by multiplying is `√(lo·hi)`, which returns `10¹²` here, "
             "exactly."),
            ("Adding the half-widths instead of multiplying them",
             "Three factors at `±2×` are reported as `±6×`, and the answer looks "
             "eight times narrower than it is. The rule follows from the interval "
             "product: `[c/2, 2c]` times `[d/2, 2d]` is `[cd/4, 4cd]`, a half-width "
             "of `4` and not of `4`&mdash;added. Any time the reported half-width is "
             "close to the sum of the inputs rather than their product, this is what "
             "happened."),
            ("Taking the high end of every factor and calling it conservative",
             "Twenty million users at two hundred actions at two kilobytes is "
             "`8·10¹²` bytes a day, which is not a safety margin on the estimate "
             "&mdash; it <em>is</em> the high end of the interval, eight times the "
             "central value, and the interval already told you that. Stacking worst "
             "cases produces one end of a range you have already computed, and it "
             "produces it without saying how unlikely that end is."),
        ],
        "standard": ("Finish when a capacity figure quoted as a single number reads as an answer with its error bar removed.",
                     "You should be able to turn three guessed factors into "
                     "`[lo, hi]`, a half-width and a width in powers of ten without "
                     "reaching for the lab, say why the geometric mean and not the "
                     "midpoint is the centre, and name which of your factors is "
                     "worth measuring and what it would buy."),
        "note": "Every factor from here on is a rate, and a rate is where the first real unit trap lives. &ldquo;Rates: the Day Has 10&#8309; Seconds&rdquo; turns a population into requests per second, and takes seriously the shortcut everyone uses for the division &mdash; a day of `10⁵` seconds instead of `86 400` &mdash; by computing exactly what it costs and in which direction.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "rates-and-the-day-in-seconds",
        "title": "Rates: the Day Has 10⁵ Seconds",
        "module": "Ranges and rates",
        "one_line": "Convert a daily volume to a per-second rate both ways, and state the size and direction of the rounding error.",
        "summary": (
            "Turning a population into requests per second is one multiplication "
            "and one division, and the division is where estimates go wrong. A day "
            "is `86 400` seconds; everyone divides by `10⁵` instead. That shortcut "
            "is worth having and it is not free: the shortcut day is `125/108` of a "
            "real one, and the rate it produces lands `13.6%` low &mdash; which is "
            "not the same percentage, and not in the direction most people quote it."
        ),
        "key": [
            "req/day ÷ (s/day) = req/s          the units decide the direction",
            "86 400 s/day       the real day",
            "10⁵ s/day          the shortcut",
            "10⁵ / 86 400 = 125/108             the shortcut day is 15.74% too long",
            "86 400 / 10⁵ = 108/125             so the rate lands 13.6% low",
            "10⁹ req/day ÷ 86 400 = 11 574.074 req/s",
            "10⁹ req/day ÷ 10⁵    = 10 000 req/s",
        ],
        "key_label": "The conversion, the shortcut, and the two percentages it costs",
        "concepts_intro": (
            "The arithmetic is a division. What the lesson is about is which way up "
            "the division goes, and what happens to the answer when the divisor is "
            "rounded to a power of ten."
        ),
        "concepts": [
            ("The unit chain decides the direction",
             "`10⁹ req/day ÷ 86 400 s/day = 11 574.074 req/s`: the `day` cancels and "
             "`s` moves to the denominator. Multiplying instead would give "
             "`req·s/day²`, which is not a unit anybody wants and is the visible "
             "symptom of the most common error in this arithmetic. Writing the unit "
             "on every row costs a few characters and makes a wrong-way division "
             "impossible to miss."),
            ("A longer day is a smaller rate",
             "The shortcut replaces `86 400` with `10⁵`, which is a day `125/108` as "
             "long. The same daily volume spread over a longer day arrives more "
             "slowly, so the shortcut rate is the reciprocal fraction of the truth: "
             "`108/125`. `10⁹` requests a day is `11 574.074` per second exactly and "
             "`10 000` per second through the shortcut, and `10 000` is the smaller "
             "of the two, every time, for every input."),
            ("One approximation, two different percentages",
             "`125/108` is `15.74%` more than one and `108/125` is `13.6%` less "
             "than one, and both describe the same shortcut. The day is `15.74%` too "
             "long; the rate is `13.6%` too low. The reason they differ is that a "
             "percentage is not symmetric under taking a reciprocal, and quoting the "
             "first figure as though it applied to the rate is the error this lesson "
             "is really about."),
        ],
        "read_title": "Per day to per second, and what a power of ten costs",
        "read_intro": "The chain that gets the units right, the shortcut everyone uses, and the two exact fractions that say what it costs.",
        "body": [
            ("def", ("Rate conversion",
                     "A <strong>rate</strong> is a quantity per unit of time. To "
                     "convert a volume per day into a rate per second, divide by the "
                     "number of seconds in a day: `req/day ÷ (s/day) = req/s`. The "
                     "seconds-per-day figure is a <strong>conversion factor</strong> "
                     "and appears in the denominator, whichever direction feels "
                     "natural.")),
            ("p", "Start from a population. Daily active users times actions per "
                  "user per day is a volume per day; the division by seconds is the "
                  "last step and not the first. Doing it in that order means the "
                  "intermediate figure &mdash; requests per day &mdash; is itself "
                  "worth reading, and it is usually the number you can check against "
                  "something somebody measured."),
            ("math", [
                "daily users                10 000 000   users",
                "× actions / user / day     100          actions / user / day",
                "                           ----------------------------------",
                "                           1 000 000 000   actions / day",
                "÷ seconds per day          86 400       s / day",
                "                           ----------------------------------",
                "                           11 574.074   actions / s",
            ]),
            ("p", "`86 400` is `60 · 60 · 24`, and there is nothing approximate "
                  "about it. What is approximate is what almost everybody does with "
                  "it, which is to divide by `10⁵` because a power of ten can be "
                  "done in the head while standing at a whiteboard. The shortcut is "
                  "good practice. The lesson is that it has a size and a direction, "
                  "and both are exact fractions."),
            ("def", ("The 10⁵-second day",
                     "The <strong>shortcut day</strong> is `10⁵` seconds. Its ratio "
                     "to a real day is `10⁵/86 400 = 125/108`, so the shortcut day is "
                     "`15.74%` longer than a real one. A rate computed by dividing by "
                     "it is `108/125` of the true rate, which is `13.6%` low.")),
            ("math", [
                "10⁵ / 86 400  =  100 000 / 86 400  =  125/108  =  1.157407…",
                "86 400 / 10⁵  =  86 400 / 100 000  =  108/125  =  0.864      exact",
                "",
                "125/108 − 1   =  17/108  =  15.74%      how much longer the day is",
                "1 − 108/125   =  17/125  =  13.6%       how much lower the rate is",
            ]),
            ("p", "`108/125` is `0.864` exactly, which is the pleasant part of this "
                  "shortcut: the correction is a two-digit decimal. A rate computed "
                  "the fast way, multiplied by `0.864`, is the rate computed the "
                  "slow way, and the lab prints both columns so the correction can "
                  "be checked rather than remembered."),
            ("example", ("Ten million users, a hundred actions each",
                         "The daily volume is `10⁹` requests. Divided by `86 400` "
                         "that is `11 574.074` requests a second; divided by `10⁵` it "
                         "is `10 000` requests a second, which is a number you can "
                         "hold in your head for the rest of the meeting. The ratio "
                         "between them is `125/108`, and reading the chain back "
                         "upward &mdash; `11 574.074 req/s × 86 400 s/day` &mdash; "
                         "returns `10⁹` requests a day, which is where it started.")),
            ("h3", "The two percentages, and why they are not the same one"),
            ("p", "If a quantity is `15.74%` too large, its reciprocal is not "
                  "`15.74%` too small. `1/1.157407… = 0.864`, a shortfall of "
                  "`13.6%`. This is not a subtlety about rounding; it is the same "
                  "asymmetry as a factor of two being `+100%` upward and `-50%` "
                  "downward, seen at a smaller scale. Both are exact fractions &mdash; "
                  "`17/108` and `17/125`, which the lab prints as the percentages "
                  "`425/27%` and `68/5%` &mdash; and they have the same numerator "
                  "over different denominators, which is a compact way to see that "
                  "they cannot be equal."),
            ("p", "Which one you want depends on what you are correcting. Going "
                  "from the shortcut rate to the true rate, multiply by `125/108`. "
                  "Going from the true rate to the shortcut rate, multiply by "
                  "`108/125`. The lab labels the two columns by what was divided by, "
                  "not by which is right, because both are right about their own "
                  "question."),
            ("h3", "When 13.6% matters"),
            ("p", "Usually it does not. An estimate whose factors are known to "
                  "`±2×` carries a range `64×` wide, and a systematic `13.6%` is "
                  "invisible inside it &mdash; that is the argument for the "
                  "shortcut, and it is a good one. What the width does not license "
                  "is forgetting the bias is there."),
            ("ul", [
                "<strong>It compounds.</strong> A shortcut rate multiplied by a "
                "retention window, then by a replication factor, carries its `13.6%` "
                "into every one of those products unchanged.",
                "<strong>It does not average out.</strong> A range is symmetric "
                "around its centre and a bias is not: the shortcut lands low every "
                "time, so ten estimates made this way are all low together.",
                "<strong>It is not a range.</strong> Adding `13.6%` to the ± of a "
                "factor hides a systematic error inside a random one, and they behave "
                "differently under multiplication and under comparison.",
                "<strong>It shows up against a measurement.</strong> Comparing a "
                "shortcut estimate with a figure somebody measured and finding it "
                "`13.6%` low is not a discovery about the system.",
            ]),
            ("p", "So the rule is the ordinary one for any approximation: use it, "
                  "and say you used it. &ldquo;About ten thousand a second, on the "
                  "`10⁵` day, so call it twelve thousand if you want the real "
                  "one&rdquo; is a complete sentence and takes no longer to say."),
        ],
        "lab": ("estimate", {
            "mode": "rate",
            "preset": "day-in-seconds",
            "panel_title": "Move the users and the actions, and watch both columns",
            "panel_intro": "The chain carries its unit on every row, so a division "
                           "done the wrong way up is visible rather than merely "
                           "wrong. The two result columns are the same daily volume "
                           "divided by `86 400` and by `10⁵`; the ratio between them "
                           "is `125/108` whatever you set the sliders to.",
        }),
        "steps_title": "Turning a population into a rate",
        "steps_intro": "Volume per day first, seconds last, and the unit written on every line.",
        "steps": [
            ("Write the chain with units before any arithmetic",
             "`users × actions/user/day` gives `actions/day`, and the units cancel "
             "on the page rather than in your head. Nearly every wrong capacity "
             "estimate is a unit error, and this is the step that catches them while "
             "they are still cheap."),
            ("Get to a volume per day, and stop there for a moment",
             "Requests per day is the figure most likely to be checkable against "
             "something real &mdash; a log line count, a billing report, a number "
             "somebody quoted last quarter. Reading it out before dividing is free "
             "and occasionally ends the estimate early."),
            ("Divide by the seconds in a day, and say which day you used",
             "`86 400` if the number is going into a document, `10⁵` if it is going "
             "into a conversation. Either is fine; leaving it unsaid is not, because "
             "the two answers differ by a factor the reader cannot recover from the "
             "result alone."),
            ("Correct in the right direction if you need to",
             "Shortcut rate to true rate is `×125/108`. True rate to shortcut rate "
             "is `×108/125 = ×0.864`. If you can only keep one of them, keep `0.864`: "
             "it is exact, it is two digits, and it is the one that undoes the "
             "shortcut you actually used."),
            ("Carry the range through the division",
             "Dividing an interval by a positive constant divides both ends by it, "
             "so a daily volume known to `÷8 … ×8` is a rate known to `÷8 … ×8`. The "
             "conversion changes the units and the width of the answer not at all."),
        ],
        "worked": {
            "title": "10⁷ daily users, 100 actions each, in requests per second",
            "intro": [
                "Both routes through the same chain, side by side, and the exact "
                "fraction between them."
            ],
            "lines": [
                "daily users                 10 000 000      users",
                "× actions / user / day      100             actions / user / day",
                "= daily volume              1 000 000 000   req / day",
                "",
                "the real day        1 000 000 000 / 86 400  = 11 574.074   req/s",
                "the shortcut day    1 000 000 000 / 100 000 = 10 000       req/s",
                "",
                "ratio               11 574.074 / 10 000     = 125/108      exact",
                "                    10 000 / 11 574.074     = 108/125 = 0.864",
                "",
                "the day   10⁵ / 86 400 = 125/108      15.74% longer than a real day",
                "the rate  86 400 / 10⁵ = 108/125      13.6%  lower than the truth",
                "",
                "check upward   11 574.074 req/s × 86 400 s/day = 1 000 000 000 req/day",
            ],
            "after": [
                "The last line is the one that catches a wrong-way division. "
                "Multiplying the rate back by the seconds in a day has to return the "
                "daily volume you started from; if it returns something a factor of "
                "`86 400²` away, the division went the wrong way up and the units "
                "would have said so.",
                "Notice that `15.74%` and `13.6%` both describe this one shortcut. "
                "The first is about the day and the second is about the rate, and "
                "the lab prints them on separate tiles with separate labels for "
                "exactly that reason.",
                "For a faded rehearsal: a service has `5·10⁶` daily users doing `20` "
                "actions each. The supplied first move is the daily volume, `10⁸` "
                "requests a day. Produce both rates, predict their ratio before "
                "computing it, and then say what the shortcut rate would have to be "
                "multiplied by to recover the true one. Check all three against the "
                "lab by setting the two sliders.",
            ],
        },
        "quiz_title": "The conversion and its shortcut",
        "quiz": [
            {"q": "A daily volume is converted to a per-second rate by dividing by `10⁵` rather than by `86 400`. How does the answer compare with the truth?",
             "a": ["`15.74%` high", "`15.74%` low", "`13.6%` low", "Exact, because `10⁵` is only a relabelling"],
             "c": 2,
             "why": "Dividing by a day that is `125/108` too long gives a rate "
                    "`108/125 = 0.864` of the truth, which is `13.6%` low. "
                    "`15.74%` is how much longer the shortcut day is &mdash; a true "
                    "statement about the divisor, not about the quotient &mdash; and "
                    "reading it onto the rate is the single most common way to "
                    "misuse this shortcut. High is the wrong direction: a longer day "
                    "always yields a smaller rate."},
            {"q": "A service handles `4·10⁸` requests a day. Which expression gives requests per second?",
             "a": ["`4·10⁸ × 86 400`", "`4·10⁸ ÷ 86 400`", "`86 400 ÷ 4·10⁸`", "`4·10⁸ ÷ 24`"],
             "c": 1,
             "why": "`req/day ÷ (s/day) = req/s`: the days cancel and the seconds "
                    "land underneath. Multiplying gives `req·s/day²`, which names "
                    "nothing. The third option inverts the quotient and produces "
                    "seconds per request, which is a real quantity and the answer to "
                    "a different question. The fourth converts to requests per hour."},
            {"q": "An estimate&rsquo;s three factors are each known to `±2×`, and the rate is computed on the `10⁵`-second day. What has the shortcut done to the estimate?",
             "a": ["Widened the range from `64×` to about `73×`",
                   "Added a systematic `13.6%` shortfall inside a range that is `64×` wide",
                   "Nothing at all: the shortcut is exact once the range is taken into account",
                   "Doubled the range, because the error applies at both ends"],
             "c": 1,
             "why": "The shortcut does not widen anything &mdash; dividing an "
                    "interval by a constant divides both ends by it. What it does is "
                    "shift the whole interval down by a fixed `13.6%`, every time, "
                    "in the same direction. Inside a `64×` range that is invisible, "
                    "which is the argument for using it; it is still a bias and not "
                    "a range, so it compounds through later multiplications and does "
                    "not average out over several estimates."},
        ],
        "mistakes": [
            ("Multiplying by 86 400 when the conversion divides",
             "The belief underneath is reasonable: `86 400` is the number that "
             "connects days to seconds, so it goes in the calculation. Which "
             "operation it takes is decided by the units, not by the number: "
             "`req/day ÷ (s/day) = req/s`, while multiplying gives `req·s/day²`. The "
             "check is to multiply the answer back by `86 400` and see whether the "
             "daily volume comes back."),
            ("Applying the 15.74% to the rate",
             "&ldquo;The shortcut day is `15.74%` long, so the rate is `15.74%` "
             "low&rdquo; is wrong in a way that looks right. The rate is low by "
             "`1 − 108/125 = 13.6%`, because a reciprocal does not preserve a "
             "percentage. The two figures are `17/108` and `17/125`: same numerator, "
             "different denominators, and therefore not the same number."),
            ("Folding the shortcut into the error bar",
             "`13.6%` is not a ± on anything. It lands low on every estimate made "
             "this way, so it survives averaging, it multiplies through a retention "
             "window unchanged, and it turns a comparison against a measured figure "
             "into a false finding. A range is symmetric about its centre; a bias is "
             "a shift of the whole interval, and the two have to be reported "
             "separately."),
        ],
        "standard": ("Finish when the direction of the division is settled by the units and not by which answer looks reasonable.",
                     "You should be able to take a user count and an actions figure "
                     "to a rate in one chain with units on every row, quote both the "
                     "`86 400` and the `10⁵` answers, say which of `15.74%` and "
                     "`13.6%` applies to which quantity, and name a situation where "
                     "the shortcut would actually mislead someone."),
        "note": "One rate is rarely the end of it. &ldquo;Read/Write Ratio&rdquo; splits a single request rate into two that size completely different things &mdash; reads size caches and bandwidth, writes size storage and replication &mdash; and it turns on an arithmetic detail that catches almost everyone: a ratio of `r:1` gives a write share of `1/(r+1)`, which for `100:1` is not one percent.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "read-write-ratio",
        "title": "Read/Write Ratio",
        "module": "Ranges and rates",
        "one_line": "Split a total request rate by a stated read-to-write ratio and report both rates as exact shares.",
        "summary": (
            "A single request rate is almost never the quantity you want, because "
            "reads and writes size different parts of a system. Splitting one rate "
            "into two is a line of algebra with one trap in it: a ratio of `r:1` "
            "counts reads against writes, so the write share is `1/(r+1)` and not "
            "`1/r`. At `100:1` that is the difference between `1%` and `0.990099%`, "
            "which is small, and the habit of being wrong about it is not."
        ),
        "key": [
            "r:1 reads to writes        r = reads / writes",
            "T = R + W                  the total is both parts",
            "W = T / (r + 1)            writes per second",
            "R = T · r / (r + 1)        reads per second",
            "r = 100, T = 10 000 req/s:",
            "   writes 10 000/101 = 99.01 /s      share 1/101",
            "   reads  1 000 000/101 = 9 900.99 /s  share 100/101",
            "   the instinct 1/r overstates the writes by 101/100",
        ],
        "key_label": "One rate, two rates, and the share that is not 1/r",
        "concepts_intro": (
            "The algebra is two lines. What it is for is the part worth arguing "
            "about: the two rates you end up with are consumed by different lessons "
            "of this course and by different courses after it."
        ),
        "concepts": [
            ("A ratio names a split, and the total is both parts",
             "`r:1` says reads divided by writes is `r`. If `W` is the write rate "
             "then reads are `rW`, and the total is `R + W = (r+1)W`, so "
             "`W = T/(r+1)`. The `+1` is the writes themselves, which are part of "
             "the traffic being split and not something outside it. This is the "
             "whole content of the arithmetic and it is also the whole misconception."),
            ("Two rates, because they size different things",
             "The write rate is what sizes storage, the replication factor and the "
             "durability budget; the read rate is what sizes caches, bandwidth and "
             "fan-out. Splitting the total and then sizing both paths off the total "
             "again does the arithmetic and throws the result away. At `100:1` the "
             "writes are `99.01` a second out of `10 000`, and every hard problem on "
             "the rest of this path lives in those ninety-nine."),
            ("The instinct 1/r is high by a factor of (r+1)/r",
             "Reading `100:1` as &ldquo;one percent writes&rdquo; gives `100` writes "
             "a second where the truth is `99.01`, an overstatement by `101/100`. "
             "The error shrinks as `r` grows and it is nowhere near negligible at "
             "small `r`: at `2:1` the instinct says half the traffic is writes when "
             "a third of it is, an overstatement by `3/2`."),
        ],
        "read_title": "Splitting one rate into two",
        "read_intro": "What a ratio claims, the two shares it implies, and why the split is worth doing at all.",
        "body": [
            ("def", ("Read/write ratio",
                     "A workload with read rate `R` and write rate `W` has "
                     "<strong>read/write ratio</strong> `r = R/W`, usually written "
                     "`r:1`. The <strong>write share</strong> is `W/(R+W)` and the "
                     "<strong>read share</strong> is `R/(R+W)`; the two shares are "
                     "positive and sum to `1`.")),
            ("p", "The ratio and the shares carry the same information and they are "
                  "not the same number. A ratio compares the two parts to each "
                  "other; a share compares one part to the whole. Confusing them is "
                  "what makes `100:1` sound like `1%`, and the conversion between "
                  "them is exactly the `+1` in the denominator."),
            ("thm", ("Shares from a ratio",
                     "If `R/W = r` and `T = R + W`, then `W = T/(r+1)` and "
                     "`R = Tr/(r+1)`. The write share is `1/(r+1)` and the read "
                     "share is `r/(r+1)`.")),
            ("proof", [
                "From `R = rW` and `T = R + W` we get `T = rW + W = (r+1)W`, so "
                "`W = T/(r+1)`. Then `R = T − W = T − T/(r+1) = Tr/(r+1)`.",
                "The shares follow by dividing by `T`, and they sum to "
                "`1/(r+1) + r/(r+1) = (r+1)/(r+1) = 1`, which is the check worth "
                "doing: any pair of shares that does not add to one has been read "
                "off the wrong denominator.",
            ]),
            ("math", [
                "r = 100,  T = 10 000 req/s",
                "",
                "write share   1/(r+1)  = 1/101    = 0.990099…%",
                "read share    r/(r+1)  = 100/101  = 99.009900…%",
                "                         1/101 + 100/101 = 1     ✓",
                "",
                "writes        10 000/101      =     99.01 req/s",
                "reads         1 000 000/101   =  9 900.99 req/s",
                "",
                "the instinct  1/r = 1/100     =    100    req/s",
                "              (1/100)/(1/101) = 101/100   1% too many writes",
            ]),
            ("p", "The two shares adding to one is the check that survives any "
                  "value of `r`. The instinct&rsquo;s pair does not: `1/100` for "
                  "writes and `99/100` for reads gives a ratio of `99:1`, not "
                  "`100:1`. So the fast way to catch this error is to convert back "
                  "&mdash; take your two shares, divide one by the other, and see "
                  "whether the ratio you started with comes out."),
            ("h3", "Why one percent is not a rounding error"),
            ("p", "Ninety-nine writes a second against ten thousand requests is "
                  "easy to describe as noise, and for the read path it is. For "
                  "everything else on this path it is the whole story. Those writes "
                  "are what accumulates in &ldquo;Storage from Ingest and "
                  "Retention&rdquo;, what gets multiplied by the replication factor, "
                  "what has to be ordered and made durable, and what a partitioning "
                  "scheme has to route consistently. The read path is the one that "
                  "can be absorbed by a cache; the write path is the one that cannot."),
            ("example", ("Ten thousand a second at a hundred to one",
                         "Reads are `9 900.99` a second and writes are `99.01` a "
                         "second, exactly `1 000 000/101` and `10 000/101`. Sizing "
                         "the storage from the total instead would overstate the "
                         "ingest by a factor of `101`, and sizing the cache from the "
                         "total instead would overstate the read load by about one "
                         "percent. The same error in the two directions costs "
                         "wildly different amounts, which is the practical argument "
                         "for doing the split at all.")),
            ("h3", "Where the ratio comes from, and what it is a fact about"),
            ("p", "A read/write ratio is measured over a window, and it is a "
                  "property of that window rather than of the system. A daily figure "
                  "of `100:1` can be `5:1` during the hour a batch import runs, and "
                  "the hour that matters for sizing is the busiest one rather than "
                  "the average one. &ldquo;Peak to Average&rdquo; is where that gets "
                  "a number attached to it; here it is enough to write down which "
                  "window the ratio came from."),
            ("p", "The other thing worth writing down is that the ratio is a "
                  "ranged factor like any other. A ratio quoted as `100:1` is "
                  "usually known to a factor of two or three either way, and the "
                  "write rate it implies inherits that width. The interesting part "
                  "is that the width is asymmetric in its consequences: a ratio that "
                  "is wrong by `3×` barely moves the read rate and moves the write "
                  "rate by nearly the same `3×`."),
        ],
        "lab": ("estimate", {
            "mode": "rate",
            "preset": "read-write",
            "panel_title": "Set the total rate and the ratio, and read both shares",
            "panel_intro": "Both shares print as exact fractions, and so does the "
                           "factor by which the instinct `1/r` overstates the write "
                           "rate. Drag the ratio down toward `2:1` and watch that "
                           "factor grow: the shortcut is closest to right exactly "
                           "where the writes matter least.",
        }),
        "steps_title": "Splitting a rate you have been given",
        "steps_intro": "Ratio to shares, shares to rates, and a check that the pair is consistent.",
        "steps": [
            ("Write down which quantity the ratio counts",
             "`100:1` is reads against writes, so `r = R/W = 100`. A ratio with no "
             "named direction is not usable, and the failure mode is silent: the "
             "arithmetic works perfectly with the two rates swapped and produces a "
             "system sized backwards."),
            ("Convert the ratio to shares, with the `+1`",
             "Write share `1/(r+1)`, read share `r/(r+1)`. Check that they add to "
             "`1` before going any further; a pair that does not add to one has been "
             "built from the wrong denominator and every number after it will be "
             "wrong by the same factor."),
            ("Multiply the total by each share",
             "`T/(r+1)` writes a second and `Tr/(r+1)` reads a second. Keep both, "
             "with their units, and keep the exact fractions if the numbers are "
             "going to be multiplied again &mdash; `10 000/101` is easier to carry "
             "through a chain than `99.0099`."),
            ("Send each rate to the thing it sizes",
             "The write rate goes into storage, retention, replication and "
             "durability. The read rate goes into cache sizing, bandwidth and "
             "fan-out. If both paths end up being sized from the same figure, the "
             "split was not used and did not need doing."),
            ("Record the window the ratio came from",
             "A ratio measured over a day and a ratio measured over the busiest hour "
             "are different numbers about the same system, and sizing wants the "
             "second one. Writing down which you have is what makes the estimate "
             "auditable later."),
        ],
        "worked": {
            "title": "10 000 req/s at 100:1 reads to writes",
            "intro": [
                "One rate in, two rates out, with the shares as exact fractions and "
                "the instinct&rsquo;s answer alongside for comparison."
            ],
            "lines": [
                "given      T = 10 000 req/s        r = 100 reads per write",
                "",
                "R = rW  and  T = R + W",
                "     T = rW + W = (r + 1)W = 101W",
                "     W = T/101      R = 100T/101",
                "",
                "write share    1/101    = 0.990099…%",
                "read share   100/101    = 99.009900…%",
                "check        1/101 + 100/101 = 101/101 = 1        ✓",
                "",
                "writes       10 000/101      =    99.01 req/s",
                "reads     1 000 000/101      = 9 900.99 req/s",
                "check        99.01 + 9 900.99 = 10 000 req/s      ✓",
                "",
                "instinct     1/r = 1/100  ⟹  100 writes/s, 9 900 reads/s",
                "             100/9 900 = 1/99   ⟹  a 99:1 ratio, not 100:1",
                "             overstatement (1/100)/(1/101) = 101/100 = 1%",
            ],
            "after": [
                "The line worth keeping is the one that converts back. The "
                "instinct&rsquo;s pair of rates, divided into each other, gives "
                "`99:1` &mdash; not the ratio it started from. That round trip "
                "catches the error without needing to remember which of `1/r` and "
                "`1/(r+1)` is correct.",
                "The `1%` looks harmless and the lesson is not that it is dangerous. "
                "It is that the same mistake at `2:1` says half the traffic is "
                "writes when a third of it is, and that a person who has the rule "
                "wrong will apply it at whatever `r` the next system hands them.",
                "For a faded rehearsal: a service does `6 000` requests a second at "
                "`5:1`. The supplied first move is `r + 1 = 6`. Produce both shares, "
                "both rates, and the factor by which `1/r` would overstate the "
                "writes; then set the lab&rsquo;s ratio slider to `5` and check all "
                "five figures. Say the overstatement factor before you look at it.",
            ],
        },
        "quiz_title": "Ratios, shares and rates",
        "quiz": [
            {"q": "A workload is `100:1` reads to writes. What fraction of all requests are writes?",
             "a": ["`1/100`", "`1/101`", "`100/101`", "`1/99`"],
             "c": 1,
             "why": "The ratio counts reads against writes, and the total is both: "
                    "`T = (r+1)W`, so the write share is `1/(r+1) = 1/101`. `1/100` "
                    "is the instinct, and it implies a `99:1` workload rather than a "
                    "`100:1` one. `100/101` is the read share. `1/99` is what you "
                    "get by subtracting the one from the wrong side."},
            {"q": "`10 000` requests a second at `100:1`. How many writes a second?",
             "a": ["`100`", "`99.01`", "`9 900.99`", "`101`"],
             "c": 1,
             "why": "`10 000/101 = 99.0099…`, which the lab prints as `99.01`. `100` "
                    "is the `1/r` answer and is high by a factor of `101/100`. "
                    "`9 900.99` is the read rate, `1 000 000/101`. `101` is the "
                    "denominator itself, which is not a rate at all."},
            {"q": "At which ratio does the `1/r` shortcut do the most damage?",
             "a": ["`1000:1`, because the numbers are largest there",
                   "`100:1`, the ratio it is usually quoted at",
                   "`2:1`, where it claims half the traffic is writes rather than a third",
                   "It is equally wrong at every ratio, by exactly one percent"],
             "c": 2,
             "why": "The overstatement factor is `(r+1)/r`, which is `3/2` at `r = 2` "
                    "and `1001/1000` at `r = 1000`. The shortcut is most accurate "
                    "where `r` is large &mdash; and that is exactly where the write "
                    "rate is small and the error matters least. At low ratios it is "
                    "both largest and most consequential, which is the opposite of "
                    "the intuition that a big ratio makes a big error."},
        ],
        "mistakes": [
            ("Reading 100:1 as one percent writes",
             "The ratio counts reads against writes; the share counts writes against "
             "the total, and the total includes the writes. So the share is `1/101` "
             "and the write rate at `10 000` requests a second is `99.01`, not `100`. "
             "The check that catches it in a line: divide your two answers into each "
             "other and see whether the original ratio comes back. `100` and `9 900` "
             "give `99:1`."),
            ("Treating a one percent write share as negligible",
             "Those `99.01` writes a second are what accumulates over a retention "
             "window, what the replication factor multiplies, what has to be "
             "durable, and what a partitioning scheme has to route. The reads can be "
             "absorbed by a cache; the writes cannot. A split that concludes "
             "&ldquo;writes are noise&rdquo; has identified the one rate the rest of "
             "this path is about and then discarded it."),
            ("Taking one ratio to hold all day",
             "A read/write ratio is measured over a window and moves inside it. A "
             "workload that is `100:1` over a day can be `5:1` during the hour an "
             "import runs, and sizing wants the busiest hour rather than the mean "
             "one. A ratio with no window attached is not wrong so much as "
             "unfalsifiable, and the fix is one clause: say what it was measured over."),
        ],
        "standard": ("Finish when a ratio and a share are visibly different objects and the conversion between them is automatic.",
                     "You should be able to turn any `r:1` into both shares and both "
                     "rates, check the pair by converting back to the ratio, say what "
                     "each of the two rates goes on to size, and state the factor by "
                     "which `1/r` overstates the write rate at any `r`."),
        "note": "The write rate is now a number, and the first thing it sizes is the disk. &ldquo;Storage from Ingest and Retention&rdquo; accumulates it over a retention window, which turns out to be a sum rather than a product &mdash; an arithmetic series while the ingest is flat, a geometric one as soon as it grows &mdash; and then multiplies the whole thing by the number of copies you keep.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "storage-from-ingest-and-retention",
        "title": "Storage from Ingest and Retention",
        "module": "Storage and bandwidth",
        "one_line": "Size storage after a retention window with a stated monthly growth rate and a stated number of copies.",
        "summary": (
            "Storage is not a rate times a time. It is a sum of a rate over a "
            "window, which happens to equal rate times time only while the rate is "
            "constant. Let the ingest grow and the sum becomes geometric, and the "
            "answer pulls away from the product. Then the replication factor "
            "multiplies everything, and the three-line calculation that everyone "
            "does in their head has two missing factors in it."
        ),
        "key": [
            "constant ingest   S = rate · days                  an arithmetic series",
            "growth g a month  S = 30 · rate · Σ (1+g)ᵐ         a geometric one",
            "                  m = 0 … blocks − 1",
            "then              × copies                         the last step",
            "500 GB/day, 90 days, +5%/month, 3 copies:",
            "   one copy 47.29 TB        all copies 141.86 TB",
            "   if it never grew 135 TB  growth costs 1.0508×",
        ],
        "key_label": "Storage as a sum, under growth, times the copies",
        "concepts_intro": (
            "One idea with three consequences: a window is a sum of terms, the terms "
            "are equal only when nothing is growing, and the copies multiply the sum "
            "rather than the rate."
        ),
        "concepts": [
            ("Storage is a sum over a window, not a product",
             "What is on disk after `R` days is the total of what arrived on each of "
             "those days. While the daily ingest is constant, all the terms are "
             "equal and the sum collapses to `rate × days` &mdash; an arithmetic "
             "series with common difference zero, which is why the product ever "
             "works. It is a special case, and treating it as the definition is "
             "what breaks the moment anything grows."),
            ("Growth makes the series geometric",
             "At `5%` a month the ingest is `1.05ᵐ` times its starting value in "
             "month `m`, so the window is a run of monthly blocks each at its own "
             "constant rate and the total is a geometric sum. Over ninety days the "
             "blocks add `15 TB`, `15.75 TB` and `16.54 TB` for a total of "
             "`47.29 TB`, against `45 TB` if the ingest had stayed flat. The last "
             "block runs at `551.25 GB` a day, `1.103×` where it started."),
            ("Replication multiplies the sum, and comes last",
             "Three copies of `47.29 TB` is `141.86 TB`. The copies multiply the "
             "accumulated total rather than the ingest rate, which gives the same "
             "answer here and stops giving it as soon as anything else in the chain "
             "is not linear. Keeping replication as the final step also keeps the "
             "unique-data figure visible, and that is the figure a retention policy "
             "is actually about."),
        ],
        "read_title": "A rate over a window, under growth, times the copies",
        "read_intro": "Why the answer is a series, what growth does to it, and the two factors the quick calculation leaves out.",
        "body": [
            ("def", ("Retention window",
                     "The <strong>retention window</strong> `R` is how long data is "
                     "kept before it is deleted. Steady state is reached once the "
                     "system is older than `R`: each day&rsquo;s arrivals are matched "
                     "by one day&rsquo;s deletions, and the total held stops growing "
                     "for that reason and starts growing again for any other.")),
            ("p", "So the quantity to size is what accumulates across `R` days of "
                  "arrivals. Write `iₘ` for the ingest per day during block `m`; the "
                  "unique data held is `Σ iₘ · (days in block m)`, and everything "
                  "that follows is about what the terms of that sum look like."),
            ("p", "If the ingest never changes, every term is the same and the sum "
                  "is `rate × days`. That is an arithmetic series with common "
                  "difference zero, and it is the only case in which storage is a "
                  "product. It is also the case everyone has in mind when they "
                  "multiply, which is why the product feels like a definition rather "
                  "than a special case."),
            ("def", ("Monthly compounded growth",
                     "An ingest <strong>growing at `g` a month</strong> is multiplied "
                     "by `(1 + g)` once per month, so during month `m` &mdash; "
                     "counting from `m = 0` &mdash; the daily ingest is "
                     "`i₀ · (1 + g)ᵐ`. The window is a run of 30-day blocks, each "
                     "with its own constant rate, and the total is a geometric sum. "
                     "Growth here steps once a month rather than compounding "
                     "continuously, which keeps every term an exact fraction.")),
            ("math", [
                "i₀ = 500 GB/day     R = 90 days     g = 5%/month     copies = 3",
                "",
                "block  days   ingest/day     bytes added    held (one copy)",
                "   1     30     500.00 GB       15.00 TB        15.00 TB",
                "   2     30     525.00 GB       15.75 TB        30.75 TB",
                "   3     30     551.25 GB       16.54 TB        47.29 TB",
                "",
                "one copy                                        47.29 TB",
                "× 3 copies                                     141.86 TB",
                "",
                "if the ingest never grew   500 GB · 90 · 3   = 135 TB",
                "growth costs               141.86 / 135      = 1.0508×",
            ]),
            ("p", "Each block&rsquo;s rate is an exact power: month `m` runs at "
                  "`i₀ · (21/20)ᵐ`, with both ends integers, so the lab never prints "
                  "a figure it had to round on the way. The table in the lab is the "
                  "series term by term, and the total underneath it is the sum "
                  "&mdash; which is worth watching once, because it is the only way "
                  "to see that the curve pulls away from the straight line "
                  "gradually rather than at a point."),
            ("example", ("Half a terabyte a day, kept ninety days, in triplicate",
                         "The unique data is `47.29 TB` and the storage is "
                         "`141.86 TB`. The quick calculation &mdash; half a terabyte "
                         "times ninety days &mdash; gives `45 TB`, which is short by "
                         "the growth and short again by the copies. Both factors are "
                         "recoverable: the growth costs `1.0508×` against the flat "
                         "case and the copies cost exactly `3×`.")),
            ("h3", "Growth is not a correction you add at the end"),
            ("p", "Over ninety days at `5%` a month the growth is worth `1.0508×`, "
                  "which is small enough to feel like a rounding. That feeling is "
                  "about the window, not about growth. Take the lab&rsquo;s "
                  "fast-growth example &mdash; `100 GB` a day, kept two years, "
                  "growing `15%` a month &mdash; and the same arithmetic gives "
                  "`581.13 TB` of unique data against `73 TB` if it had stayed flat. "
                  "Growth is worth `7.9607×` there, and the daily ingest in the last "
                  "month has reached `2.86 TB`."),
            ("p", "The reason is the one the two prerequisite algebra courses make: "
                  "a geometric sum is dominated by its last terms, and how much it "
                  "is dominated by them depends on how many terms there are. Ninety "
                  "days is three terms and two years is twenty-five, which is the "
                  "whole difference between a `5%` correction and a factor of eight."),
            ("h3", "What this model does not say"),
            ("p", "The growth here steps once a month and is flat within the month, "
                  "which is a modelling choice and is visible in the lab as a "
                  "staircase rather than a curve. It keeps every term exact, and it "
                  "means a figure read off for day forty-five is the second "
                  "block&rsquo;s rate rather than something interpolated. Nothing on "
                  "this course needs finer resolution than that, and the alternative "
                  "&mdash; a continuously compounded day &mdash; would make every "
                  "term irrational for no gain in what the estimate can tell you."),
            ("p", "The units are decimal throughout: a kilobyte is `1000` bytes and "
                  "a terabyte is `10¹²`, which is what a disk is sold in. Mixing in "
                  "`1024`-based units partway through a chain produces an error that "
                  "grows with every thousand-step and looks like nothing at all, "
                  "because both numbers are plausible."),
        ],
        "lab": ("estimate", {
            "mode": "accumulate",
            "preset": "event-log",
            "panel_title": "Set the ingest, the window, the growth and the copies",
            "panel_intro": "The table is the series, term by term, and the total "
                           "underneath it is the sum times the copies. Drag the "
                           "growth to zero and the terms become equal; drag the "
                           "window out to two years and watch the last terms take "
                           "over the total.",
        }),
        "steps_title": "Sizing a store from an ingest rate",
        "steps_intro": "A rate per day, a window, a growth rate, a replication factor, in that order.",
        "steps": [
            ("Get the ingest to bytes per day",
             "Usually this is the write rate from &ldquo;Read/Write Ratio&rdquo; "
               "times the bytes a write carries, converted from per-second to "
               "per-day. Do the conversion once, at the start, so the retention "
               "window can be in days and the arithmetic can be a sum of daily terms."),
            ("Write the window as a run of blocks, one per growth step",
             "Ninety days at monthly growth is three blocks of thirty. Within a "
               "block the rate is constant, so each term is a rate times a count of "
               "days; across blocks the rate is multiplied by `(1+g)` each time."),
            ("Sum the blocks, and keep the unique-data figure",
             "The sum is what one copy of the data occupies, and it is the number a "
               "retention policy is about. Write it down separately before "
               "multiplying by anything, because it is the figure you will be asked "
               "to justify."),
            ("Multiply by the replication factor last",
             "Copies multiply the accumulated total. Three copies of `47.29 TB` is "
               "`141.86 TB`; the replication factor is a count of complete copies and "
               "belongs at the end of the chain, where it is visible and easy to "
               "change."),
            ("Compare against the flat answer, and quote the ratio",
             "`rate × days × copies` is the estimate somebody else will do in their "
               "head, so quoting the ratio between your answer and theirs &mdash; "
               "`1.0508×` here, from growth alone &mdash; is the fastest way to "
               "explain where the difference came from."),
        ],
        "worked": {
            "title": "500 GB a day, kept 90 days, growing 5% a month, 3 copies",
            "intro": [
                "Three monthly blocks, one term each, then the copies. Every figure "
                "below is in the lab under the same settings."
            ],
            "lines": [
                "i₀ = 500 GB/day      R = 90 days      g = 5%/month      copies = 3",
                "",
                "blocks = 90 / 30 = 3           growth factor 1 + g = 21/20",
                "",
                "block 1   rate 500 · (21/20)⁰ = 500.00 GB/day   × 30 =  15.00 TB",
                "block 2   rate 500 · (21/20)¹ = 525.00 GB/day   × 30 =  15.75 TB",
                "block 3   rate 500 · (21/20)² = 551.25 GB/day   × 30 =  16.54 TB",
                "                                                        --------",
                "unique data held                                        47.29 TB",
                "",
                "× copies    47.29 TB × 3                             = 141.86 TB",
                "",
                "flat comparison   500 GB/day × 90 days              =  45 TB   one copy",
                "                  500 GB/day × 90 days × 3          = 135 TB   all copies",
                "growth costs      141.86 / 135                      = 1.0508×",
                "last block runs at 551.25 / 500                     = 1.103× the first",
            ],
            "after": [
                "The three block totals are not equal, and that is the entire "
                "difference between this and `rate × days`. They are also not very "
                "unequal, because ninety days is only three terms &mdash; which is "
                "why growth looks like a rounding error at short windows and stops "
                "looking like one at long ones.",
                "Switch the lab to its fast-growth example to see the other end of "
                "that: `100 GB` a day kept two years at `15%` a month is "
                "twenty-five blocks, `581.13 TB` of unique data, `1.74 PB` across "
                "three copies, and a growth factor of `7.9607×` against the flat "
                "answer. Same arithmetic, same three inputs, an answer that is "
                "nothing like a product.",
                "For a faded rehearsal, take `2 TB` a day kept a year with no growth "
                "and two copies. The supplied first move: with `g = 0` every term is "
                "equal, so the sum really is `rate × days`. Predict the unique data "
                "and the total, then check them in the lab &mdash; and then turn the "
                "growth up to `5%` and say, before you look, roughly what factor the "
                "twelve blocks will cost you.",
            ],
        },
        "quiz_title": "Windows, growth and copies",
        "quiz": [
            {"q": "An ingest of `500 GB` a day is kept for `90` days and grows `5%` a month, with `3` copies. Which figure is the unique data held?",
             "a": ["`45 TB`", "`47.29 TB`", "`135 TB`", "`141.86 TB`"],
             "c": 1,
             "why": "`47.29 TB` is the sum of the three monthly blocks for one copy. "
                    "`45 TB` is the same window with the growth left out. `135 TB` "
                    "is `45 TB` across three copies, growth still missing. "
                    "`141.86 TB` is the right answer to a different question: total "
                    "storage occupied, which is the unique data times the copies."},
            {"q": "Why is `rate × days` ever the right answer for storage?",
             "a": ["Because storage is defined as a rate times a time",
                   "Because it is the sum of the daily terms when all the terms are equal",
                   "Because growth and deletion cancel in steady state",
                   "Because the replication factor is usually 1"],
             "c": 1,
             "why": "Storage is the sum of what arrived on each day of the window. "
                    "With a constant ingest all those terms are equal and the sum "
                    "collapses to a product &mdash; an arithmetic series with common "
                    "difference zero. It is a special case, not a definition, and it "
                    "stops holding the moment the ingest moves. Deletion sets the "
                    "window; it does not make the terms equal."},
            {"q": "Growth of `5%` a month costs `1.0508×` over a `90`-day window. What does the same `5%` do over a window ten times as long?",
             "a": ["About `1.05×` again: the monthly rate has not changed",
                   "About `1.5×`: ten times the correction",
                   "Substantially more, because a geometric sum is dominated by its last terms",
                   "Nothing: at steady state the growth is absorbed by deletion"],
             "c": 2,
             "why": "The correction depends on how many terms the sum has, not on "
                    "the monthly rate alone. Ninety days is three blocks and the "
                    "growth is worth `5%`; the lab&rsquo;s two-year example at `15%` "
                    "a month is twenty-five blocks and growth is worth `7.9607×`. "
                    "Deletion fixes the width of the window but does nothing to the "
                    "inequality of the terms inside it."},
        ],
        "mistakes": [
            ("Multiplying the rate by the window and stopping",
             "`500 GB × 90 days` is `45 TB`, and the answer is `141.86 TB` &mdash; "
             "short by the growth and short again by the copies. The product is the "
             "sum of the daily terms only when every term is equal, which requires a "
             "flat ingest, and the copies were never in the calculation at all. Both "
             "omissions are multiplicative, so they compound rather than partly "
             "cancelling."),
            ("Applying the final month's rate to the whole window",
             "The ingest reaches `551.25 GB` a day by the third block, and "
             "multiplying that by all ninety days treats the fastest rate as if it "
             "had held from the start. It is the same error as the flat calculation "
             "with the sign reversed: one uses the first term for every term and the "
             "other uses the last. The sum has a different rate in every block, and "
             "the lab lists them so the difference is on the page."),
            ("Filing growth as a second-order correction",
             "At `5%` a month over ninety days growth is worth `1.0508×`, which "
             "genuinely is small &mdash; and the conclusion &ldquo;growth is a "
             "rounding&rdquo; does not follow, because the size of the correction "
             "depends on the number of terms. The lab&rsquo;s two-year, `15%`-a-month "
             "example is `7.9607×` from the same arithmetic. The question to ask is "
             "never &ldquo;is the growth rate large&rdquo; but &ldquo;how many growth "
             "steps does the window contain&rdquo;."),
        ],
        "standard": ("Finish when storage reads as a sum over a window, with rate times time as the flat special case of it.",
                     "You should be able to turn an ingest rate, a retention window, "
                     "a monthly growth rate and a replication factor into a storage "
                     "figure, state the unique-data total separately from the "
                     "replicated one, and say what factor the growth was worth and "
                     "why that factor depends on the length of the window."),
        "note": "The same write rate that filled the disk also has to cross a wire, and the wire is sold in different units from the payload. &ldquo;Bandwidth: Bits, Bytes and Overhead&rdquo; takes a request rate to megabits a second, which is where a factor of eight hides, and then asks what per-request headers do to the total &mdash; a question with a surprisingly clean answer about which payload sizes are mostly header.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "bandwidth-bits-and-overhead",
        "title": "Bandwidth: Bits, Bytes and Overhead",
        "module": "Storage and bandwidth",
        "one_line": "Compute the megabits per second a request rate needs, with per-request headers included, and find the payload at which headers are half the traffic.",
        "summary": (
            "A link is sold in bits a second and a payload is measured in bytes, so "
            "every bandwidth estimate contains a factor of eight that is easy to "
            "drop and impossible to notice afterwards. The second thing in it is "
            "overhead: headers are charged once per request whatever the payload, "
            "which makes them a fixed cost with a clean crossover &mdash; the "
            "payload below which most of what crosses the wire is not your data."
        ),
        "key": [
            "bytes per request  =  payload + header      the header is per REQUEST",
            "bit/s   =  8 · rate · (payload + header)",
            "Mbit/s  =  bit/s / 10⁶                      decimal, as a link is sold",
            "2 000 req/s · 1 200 B · 8  =  19 200 000 bit/s  =  19.2 Mbit/s",
            "header share  200/1 200 = 1/6               16.7% of the wire",
            "headers ≥ half  ⟺  payload ≤ header         crossover at 200 B",
        ],
        "key_label": "Bytes to bits, and what the header costs",
        "concepts_intro": (
            "Two units and one fixed cost. The units are where the factor of eight "
            "lives; the fixed cost is why small requests are expensive in a way that "
            "does not scale with their size."
        ),
        "concepts": [
            ("A link is bits a second, a payload is bytes",
             "`2 000` requests a second at `1 200` bytes each is `2 400 000` bytes a "
             "second, and the same traffic is `19 200 000` bits a second, which is "
             "`19.2 Mbit/s`. The `8` is not a correction or a safety factor; it is "
             "the conversion between the unit the payload is measured in and the "
             "unit the link is sold in, and an answer that omits it is exactly an "
             "eighth of the truth for every possible input."),
            ("The header is charged once per request",
             "`200` bytes of headers on a `1 000`-byte payload is `1 200` bytes on "
             "the wire, and the headers are `1/6` of it. Double the payload and the "
             "header share falls; halve it and the share rises. Overhead is a fixed "
             "cost per request rather than a percentage of the payload, which means "
             "&ldquo;add ten percent for overhead&rdquo; is a rule that is wrong in "
             "one direction for large requests and in the other for small ones."),
            ("The crossover payload is the header size itself",
             "Headers are at least half the bytes on the wire exactly when the "
             "payload is no larger than the header: `h/(p+h) ≥ 1/2` rearranges to "
             "`h ≥ p`. So with `200` bytes of headers, a `200`-byte payload is "
             "exactly half overhead and anything smaller is mostly overhead. It is a "
             "one-line result and it is the thing to remember about small requests."),
        ],
        "read_title": "From a request rate to a link rate",
        "read_intro": "The unit chain in full, the factor of eight, and what per-request overhead does to small payloads.",
        "body": [
            ("def", ("Bandwidth",
                     "<strong>Bandwidth</strong> is a rate of data across a link, "
                     "measured in <strong>bits per second</strong>. A megabit per "
                     "second is `10⁶` bits a second &mdash; decimal, like the rest of "
                     "the units on this course, because that is what a link is sold "
                     "in. A byte is `8` bits, so bytes per second times `8` is bits "
                     "per second.")),
            ("p", "The chain runs requests per second, bytes per request, bits per "
                  "byte, bits per megabit. Four rows, three of which are conversion "
                  "factors, and each one carries the unit it leaves behind. Written "
                  "out like that the factor of eight is unmissable; done in the head "
                  "it is the single most common defect in a bandwidth estimate, and "
                  "it is invisible in the answer because an eighth of a plausible "
                  "number is another plausible number."),
            ("math", [
                "requests per second          2 000        req/s",
                "× bytes per request          1 200        B/req",
                "                             2 400 000    B/s",
                "× bits per byte              8            bit/B",
                "                             19 200 000   bit/s",
                "÷ bits per megabit           1 000 000    bit/Mbit",
                "                             19.2         Mbit/s",
            ]),
            ("p", "Skipping the third row gives `2.4`, and calling that Mbit/s is "
                  "the truth divided by eight. The lab prints both columns side by "
                  "side with the ratio between them, which is `8` regardless of what "
                  "the sliders say, because the error is a missing constant and not "
                  "an approximation."),
            ("def", ("Per-request overhead",
                     "<strong>Overhead</strong> is the bytes a request costs beyond "
                     "its payload &mdash; request and response headers, framing, "
                     "acknowledgements. It is charged <strong>per request</strong> "
                     "and does not scale with the payload, so the bytes on the wire "
                     "are `payload + header` and the <strong>header share</strong> "
                     "is `h/(p+h)`.")),
            ("thm", ("The crossover payload",
                     "Headers are at least half the bytes on the wire if and only if "
                     "the payload is no larger than the header: `h/(p+h) ≥ 1/2` "
                     "exactly when `p ≤ h`.")),
            ("proof", [
                "`p` and `h` are positive, so `p + h > 0` and the inequality "
                "`h/(p+h) ≥ 1/2` may be multiplied through by `2(p+h)` without "
                "changing direction, giving `2h ≥ p + h`, that is `h ≥ p`.",
                "Every step is reversible, so the two conditions are equivalent and "
                "the crossover sits at `p = h` exactly, where the share is `1/2`.",
            ]),
            ("example", ("Two thousand requests a second, a kilobyte each",
                         "With `200` bytes of headers, each request is `1 200` bytes "
                         "on the wire and the link carries `19.2 Mbit/s`. Headers "
                         "are `1/6` of that &mdash; `16.7%` &mdash; and the "
                         "crossover is at a `200`-byte payload, where they would be "
                         "exactly half. Drag the payload slider down past `200` in "
                         "the lab and the header share crosses `1/2` at precisely "
                         "the header size, which is what the theorem says it must.")),
            ("h3", "Why the fixed cost matters more than its size"),
            ("p", "Two hundred bytes is nothing. Two hundred bytes per request, at a "
                  "rate high enough to matter, is a fixed cost on every one of them, "
                  "and its share of the traffic is set by the payload rather than by "
                  "anything about the link. A system whose requests carry kilobytes "
                  "pays `16.7%`; the same system after someone splits those requests "
                  "into ten smaller ones pays far more, for the same data, without "
                  "any line of the estimate looking different."),
            ("p", "This is the bandwidth version of an argument that recurs on this "
                  "path: a per-operation cost is the thing to count, and the number "
                  "of operations is the thing to control. &ldquo;Latency Numbers on "
                  "a Log Scale&rdquo; is the same point about time, and "
                  "&ldquo;Round Trips, Not Bytes&rdquo; on Latency and the Tail is "
                  "the same point again about the network."),
            ("h3", "Keep one base"),
            ("p", "This course is decimal end to end: `1 kB` is `1000` bytes, "
                  "`1 MB` is `10⁶`, `1 Mbit/s` is `10⁶` bits a second. Disks and "
                  "links are both sold that way. What produces silent errors is "
                  "mixing the conventions inside one chain &mdash; a `1024`-based "
                  "kilobyte multiplied into a decimal megabit &mdash; because the "
                  "discrepancy compounds at every thousand-step and every "
                  "intermediate figure still looks like a sensible number."),
            ("p", "So state the base once, at the top, and use it everywhere. If a "
                  "figure arrives from somewhere else in the other base, convert it "
                  "at the boundary rather than partway through, where the conversion "
                  "is visible in the chain and can be argued with."),
        ],
        "lab": ("estimate", {
            "mode": "rate",
            "preset": "bandwidth",
            "panel_title": "Set the rate, the payload and the header size",
            "panel_intro": "The chain converts bytes to bits explicitly, and the "
                           "column beside it is the same traffic with the `×8` left "
                           "out &mdash; the ratio between them is `8` whatever the "
                           "sliders say. Drag the payload down to the header size and "
                           "watch the header share arrive at exactly `1/2`.",
        }),
        "steps_title": "Sizing a link from a request rate",
        "steps_intro": "Bytes per request first, then bits, then the unit the link is sold in.",
        "steps": [
            ("Add the header to the payload before anything else",
             "The bytes on the wire are `payload + header`, per request. Doing this "
             "first means the rest of the chain multiplies a single figure and there "
             "is no temptation to add a percentage for overhead at the end, which is "
             "the wrong shape of correction."),
            ("Multiply by the request rate to get bytes per second",
             "`req/s × B/req = B/s`, with the requests cancelling. This is the last "
             "figure in the chain that is still in the units the payload was "
             "measured in, and it is worth reading out for that reason."),
            ("Multiply by eight, and say the word bits",
             "`B/s × 8 bit/B = bit/s`. Say it out loud as a unit change rather than "
             "a factor: the number has not been corrected, it has been re-expressed "
             "in the unit the link is sold in."),
            ("Divide by `10⁶` for megabits, in the same base as everything else",
             "`1 Mbit/s` is `10⁶` bits a second. Decimal, like the storage units, "
             "and stated rather than assumed &mdash; a chain that silently changes "
               "base partway through produces an error that grows at every step and "
               "looks like nothing."),
            ("Check the header share against the payload",
             "Divide the header size by the bytes per request. If the share is "
             "anywhere near a half, the payload is near the header size and the "
             "estimate is mostly about overhead, which usually means the right fix "
               "is fewer, larger requests rather than a bigger link."),
        ],
        "worked": {
            "title": "2 000 req/s, 1 kB payload, 200 B of headers",
            "intro": [
                "The full chain with a unit on every row, then the header share and "
                "the crossover payload."
            ],
            "lines": [
                "bytes per request    1 000 B payload + 200 B header  = 1 200 B/req",
                "",
                "2 000 req/s × 1 200 B/req                            = 2 400 000 B/s",
                "2 400 000 B/s × 8 bit/B                              = 19 200 000 bit/s",
                "19 200 000 bit/s ÷ 10⁶ bit/Mbit                      = 19.2 Mbit/s",
                "",
                "the ×8 forgotten   2 400 000 / 10⁶ = 2.4  \"Mbit/s\"",
                "                   19.2 / 2.4 = 8         the whole difference",
                "",
                "header share       200 / 1 200 = 1/6 = 16.7% of the wire",
                "crossover          h/(p+h) ≥ 1/2  ⟺  p ≤ h  ⟹  200 B payload",
                "",
                "at p = 200 B       200/400 = 1/2          exactly half",
                "at p =  50 B       200/250 = 4/5          80% overhead",
            ],
            "after": [
                "The two lines in the middle are the lesson about units. `2.4` and "
                "`19.2` are both plausible link rates, and nothing about the smaller "
                "one looks wrong; it is wrong by exactly a factor of eight, for "
                "every set of inputs, which means it can never be caught by "
                "sanity-checking the answer and can always be caught by writing the "
                "units down.",
                "The two lines at the bottom are the lesson about overhead. The "
                "share is not a property of the system, it is a property of the "
                "payload, and it moves fast once the payload gets near the header "
                "size. A design that halves the request size does not halve the "
                "bandwidth.",
                "For a faded rehearsal: `5 000` requests a second, `300`-byte "
                "payloads, `200` bytes of headers. The supplied first move is the "
                "bytes per request, `500`. Produce the link rate in Mbit/s, the "
                "header share as an exact fraction, and the payload at which headers "
                "would be half &mdash; then set the three sliders in the lab and "
                "check. Say the header share before you look; it is larger than most "
                "people expect.",
            ],
        },
        "quiz_title": "Bits, bytes and headers",
        "quiz": [
            {"q": "`2 000` requests a second carry `1 200` bytes each. What link rate is that?",
             "a": ["`2.4 Mbit/s`", "`19.2 Mbit/s`", "`2.4 MB/s`", "`192 Mbit/s`"],
             "c": 1,
             "why": "`2 000 × 1 200 = 2 400 000` bytes a second; times `8` is "
                    "`19 200 000` bits a second, which is `19.2 Mbit/s`. `2.4 Mbit/s` "
                    "is the same traffic with the `×8` dropped &mdash; exactly an "
                    "eighth of the truth. `2.4 MB/s` is right as a figure and wrong "
                    "as an answer: it is megabytes, and a link is not sold in those. "
                    "`192` is an order of magnitude out."},
            {"q": "Requests carry `200` bytes of headers. Below what payload are headers more than half the bytes on the wire?",
             "a": ["`100 B`", "`200 B`", "`400 B`", "It depends on the request rate"],
             "c": 1,
             "why": "`h/(p+h) ≥ 1/2` rearranges to `h ≥ p`, so the crossover is at "
                    "`p = h`: a `200`-byte payload is exactly half overhead and "
                    "anything smaller is mostly overhead. The rate does not enter, "
                    "because both the payload and the header are charged on every "
                    "request and the rate multiplies them equally. `400` is where "
                    "the share is a third, not a half."},
            {"q": "A team splits each `1 000`-byte request into five `200`-byte requests, with `200` bytes of headers on each. What happens to the traffic?",
             "a": ["It is unchanged: the same payload crosses the wire",
                   "It falls, because each request is smaller",
                   "It rises, because the header is charged five times instead of once",
                   "It rises by `5×`, because there are five times as many requests"],
             "c": 2,
             "why": "Set the payload slider to `200 B` and the lab reports `400 B` "
                    "per request and a header share of `1/2`. Five of those carry "
                    "`2 000` bytes where one `1 200`-byte request used to &mdash; "
                    "the payload total is unchanged and the overhead has gone from "
                    "`200` bytes to `1 000`. Not `5×`, because the request count "
                    "rose while the payload per request fell to match; the whole "
                    "increase is overhead, which is the practical form of the "
                    "fixed-cost argument."},
        ],
        "mistakes": [
            ("Dividing bytes by a million and calling it Mbit/s",
             "`2 400 000` bytes a second becomes `2.4`, which looks like a link "
             "rate and is the truth divided by eight, for every input. The factor of "
             "eight is not a correction, it is the conversion between the unit the "
             "payload is measured in and the unit the link is sold in, so the answer "
             "cannot be checked for plausibility &mdash; an eighth of a reasonable "
             "figure is another reasonable figure. Writing `bit/B` on its own row is "
             "the fix."),
            ("Mixing 1024-based and decimal units in one chain",
             "A kilobyte is `1000` bytes on this course and a megabit is `10⁶` bits, "
             "because that is what disks and links are sold in. The failure is not "
             "picking the wrong base; it is picking both, in different rows of the "
             "same chain. The discrepancy compounds at every thousand-step and is "
             "undetectable in the result, since every intermediate figure remains a "
             "perfectly sensible number."),
            ("Adding a flat percentage for overhead",
             "&ldquo;Add ten percent for headers&rdquo; treats a per-request cost as "
             "if it scaled with the payload. With `200` bytes of headers the real "
             "share is `1/6` at a kilobyte payload, `1/2` at a `200`-byte payload "
             "and `4/5` at fifty bytes &mdash; the same headers, three different "
             "percentages. The overhead has to be added per request, before the rate "
             "is multiplied in, or the answer is wrong in a direction that depends "
             "on the payload."),
        ],
        "standard": ("Finish when a link rate quoted without the word bits reads as an unfinished sentence.",
                     "You should be able to run a request rate to Mbit/s with a unit "
                     "on every row, say what dropping the `×8` does and why it "
                     "cannot be caught by inspection, compute a header share as an "
                     "exact fraction, and give the crossover payload for any header "
                     "size without computing anything."),
        "note": "Two of the four things a rate sizes are done. Before the other two &mdash; machines and memory &mdash; the course needs two quantities that are not rates at all. &ldquo;Latency Numbers on a Log Scale&rdquo; is the first: the operations a system is built out of span a range so wide that only a ratio scale holds them, and the ratios between them are the part worth carrying around.",
    },
]
