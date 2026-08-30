"""Exponential and Logarithmic Functions."""

from . import part_a, part_b

COURSE = {
    "slug": "exponential-and-logarithmic-functions",
    "title": "Exponential and Logarithmic Functions",
    "level": "Intermediate → Advanced",
    "summary": (
        "Growth that compounds, and the function that undoes it: exponential functions and their graphs, decay, the number e, the logarithm as an inverse, the three laws, change of base, solving equations of both kinds, and the scales built on logarithms."
    ),
    "blurb": (
        "The variable moves into the exponent, and ordinary algebra stops working. A logarithm is the tool that brings it back down &mdash; defined as an inverse, with three laws that are the exponent laws read backwards."
    ),
    "key": [
        "log_b(x) = y   ⟺   b^y = x",
        "log(MN) = log M + log N        log(M/N) = log M − log N",
        "log(M^p) = p·log M              the law that solves equations",
        "A = P·e^(rt)        e = 2.71828…",
    ],
    "assumes_short": "Courses 1–6",
    "assumes_long": "exponents, inverse functions, and graphing",
    "outcomes_intro": (
        "By the end you can model constant-ratio change, use logarithms as inverse "
        "functions, solve both kinds of equation, and convert a logarithmic-scale "
        "difference into the factor it represents."
    ),
    "outcomes": [
        ("Model exponential change",
         "Classify a formula or equally spaced table, translate a fixed percentage "
         "into a multiplier, and state the starting value, direction and asymptote."),
        ("Use logarithms as inverses",
         "Convert between `b^y = x` and `log_b(x) = y`, identify the bases hidden by "
         "`log` and `ln`, and evaluate exact values before rounding."),
        ("Transform logarithmic expressions",
         "Expand or condense with the three laws, preserve the domain, and use change "
         "of base with the argument in the numerator and the original base in the "
         "denominator."),
        ("Solve and interpret",
         "Choose matching powers or logarithms, test logarithmic candidates in the "
         "original domain, build a compounding model, and turn a log-scale difference "
         "into a ratio."),
    ],
    "syllabus_intro": (
        "Lessons 1 to 3 are exponential functions and `e`; 4 to 8 define the logarithm and its laws; 9 to 12 solve and apply."
    ),
    "how_to": [
        "After each complete worked example, cover its answer and do the faded "
        "rehearsal before the quiz. The first strategic move is supplied; the "
        "remaining algebra, interpretation and check are yours.",
        "Say the definition out loud until it is automatic: a logarithm is an exponent. Almost every error in this course is a step taken without that sentence in mind.",
        "Check the domain of every solution to a logarithmic equation. `log(x - 5)` has nothing to say about `x = 2`, and the algebra will happily produce it.",
        "Use the log-scale lesson on numbers you know. The distance from 1 to 10 being the same as 10 to 100 is either obvious or wrong-feeling, and it is worth being the first.",
    ],
    "not_covered": [
        "The derivative of `e^x` and the reason `e` is the natural base for calculus. This course gives `e` by compounding, which is honest and complete for algebra.",
        "Logarithms of negative and complex numbers.",
        "Curve fitting and regression on transformed data, which is a statistics topic.",
    ],
    "footer_lead": (
        "Exponential and logarithmic values are irrational, so this is the one course on the path where the labs show rounded decimals &mdash; and they say where they rounded. The exact statements, the laws and the domains, are computed exactly and the rounding never enters them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
