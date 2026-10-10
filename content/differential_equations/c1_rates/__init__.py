"""Rates of Change and the Derivative."""


from . import part_a, part_b


COURSE = {
    "slug": "rates-of-change-and-the-derivative",
    "title": "Rates of Change and the Derivative",
    "level": "Beginner → Intermediate",
    "summary": (
        "How fast a quantity is changing, computed as a fraction and then asked a better "
        "question: what do those fractions approach? The average rate over a step `h` is an "
        "exact difference quotient, the quotient of a polynomial turns out to be a polynomial "
        "in `h`, and its part that does not depend on `h` is the derivative &mdash; read off "
        "by algebra, with no limit to believe. Then the rules that make it fast, where the "
        "rate is zero, the rate of the rate, and the one family of functions whose rate is "
        "itself a multiple of the function."
    ),
    "blurb": (
        "Every differential equation in this Subject is a sentence about a rate, so the rate "
        "has to be something you can compute and not only something you can recite. Here it "
        "is computed first and named second. The average rate of change over `[a, a + h]` is "
        "a fraction, and the lab prints it as one for a column of halving steps; the "
        "derivative is the number that column heads for, stated as a claim the table "
        "illustrates and does not prove. For a polynomial the claim is not even needed, "
        "because the quotient simplifies to a polynomial in `h` and the derivative is its "
        "constant term. The power, product and chain rules are then checked exactly on "
        "polynomials by expanding both sides, and the course ends on the exponential, the "
        "one place where a quotient cannot be exact and the lab says so by rounding and "
        "labelling every figure."
    ),
    "key": [
        "(f(a + h) − f(a))/h   exact, for each h",
        "a polynomial's quotient is a polynomial in h",
        "f′(a) = what the quotients approach",
        "tangent: y = f(a) + f′(a)·(t − a)",
        "(tⁿ)′ = n·tⁿ⁻¹",
        "(f·g)′ = f′·g + f·g′",
        "p′ = 0 where the graph turns; p″ the bend",
        "(bᵗ)′ = bᵗ·(a constant); e makes it 1",
    ],
    "assumes_short": "Algebra's Lines, Functions and Graphs and Polynomials and Factoring; its law of exponents for the last lesson",
    "assumes_long": (
        "the Algebra Subject's Lines, Functions and Graphs, for function notation, slope and what a "
        "graph is, its Polynomials and Factoring, for expanding a power such as `(t + h)³` "
        "and cancelling a common factor, and, for the last lesson only, the law "
        "`b^(a + h) = b^a·b^h` from its Exponential and Logarithmic Functions; nothing from "
        "calculus, and fractions read "
        "comfortably, since every page uses them and the lab does the arithmetic"
    ),
    "outcomes_intro": (
        "By the end you can compute a rate of change exactly, say precisely what the "
        "derivative claims, find it for a polynomial by algebra and by rule, and use it to "
        "describe how a graph moves."
    ),
    "outcomes": [
        ("Compute an average rate of change exactly",
         "The quotient `(f(a + h) − f(a))/h` as a single fraction for a given function, point "
         "and step, read as the slope of a secant, with the division carried out rather than "
         "dropped."),
        ("Simplify a difference quotient to a polynomial in h",
         "Expand `p(t + h)`, cancel the `h` that every surviving term shares, and read off "
         "the part that does not depend on `h` &mdash; without setting `h` to zero first."),
        ("State what the derivative claims, and what a table shows",
         "A column of exact quotients for halving `h`, the number it heads for, and one "
         "sentence that separates the claim about every `h` from the seven rows on the page."),
        ("Write the tangent line and measure what it gets wrong",
         "`y = f(a) + f′(a)·(t − a)`, the estimate it gives at `a + h`, and the exact error "
         "&mdash; a fraction, not a feeling about nearness."),
        ("Differentiate and read the graph from the sign",
         "The power rule, term by term; where `p′` is positive, negative or zero; the product "
         "and chain rules checked by expanding both sides; and the second derivative as the "
         "rate of the rate."),
        ("Recognise the exponential by its rate",
         "The quotient of `bᵗ` as `bᵗ` times a factor that does not depend on `t`, that "
         "factor read off a rounded and labelled table, and `e` as the base whose factor is 1."),
    ],
    "syllabus_intro": (
        "Rates come first as fractions: the average rate, then the average rate of a "
        "polynomial as a polynomial in the step. Only then is the question asked that gives "
        "the course its name, what the quotients approach, and it is answered at a point, "
        "with the tangent line, and for one function that is not a polynomial. The second "
        "half turns the point into a function and uses it: the rules, the places where the "
        "rate vanishes, the rate of the rate, and the exponential."
    ),
    "how_to": [
        "Compute before you name. Each lesson starts from quotients you can check by hand "
        "&mdash; a handful of fractions &mdash; and only then gives the quantity they head "
        "for a name. If a figure on the page surprises you, type the function into the lab "
        "and watch the column.",
        "Keep two statements apart: what the table shows and what the lesson claims. A table "
        "has a finite number of rows and every claim about a rate is about every step, "
        "however small. For polynomials the gap is closed by algebra, and the lessons say "
        "where; for the exponential it is not, and the lesson says that too.",
        "Do the cancelling yourself at least once per lesson. Expand `(t + h)²`, subtract, "
        "divide by `h`. The labs print the result, but the habit of seeing the `h` factor out "
        "of every surviving term is what makes the derivative a computation rather than a "
        "definition to memorise.",
        "Read every rounded figure as rounded. Wherever the lab prints `≈`, the digits are a "
        "decimal approximation to a number that has none; everywhere else the figure is an "
        "exact fraction and you can check it with pencil.",
    ],
    "not_covered": [
        "Limits as a theory. There is no epsilon-and-delta definition here, no limit laws and "
        "no definition of continuity. The derivative is what exact quotients head for, "
        "demonstrated as a column and, for polynomials, read off by algebra. A reader who "
        "wants the theory is at the start of a first analysis course, which is where it "
        "properly begins.",
        "Differentiation of general functions. The quotient rule, implicit differentiation, "
        "inverse trigonometric functions and the derivatives of logarithms are left out; the "
        "later courses need the power, product and chain rules on polynomials and the stated "
        "derivatives of the exponential, sine and cosine, and nothing else.",
        "Optimisation as a craft. Where the rate is zero is found and classified, and the "
        "second derivative is read, but word problems about boxes, fences and ladders are "
        "not set; they are an application of this course and not a part of it.",
        "<strong>The result this course states and does not prove.</strong> That the "
        "quotients of a function that is not a polynomial settle on one number. The "
        "exponential's quotient is shown as a rounded column heading for a constant, and the "
        "constant is named; that the column really converges is the claim the table "
        "illustrates.",
    ],
    "footer_lead": (
        "Every difference quotient, simplified polynomial, tangent line, derivative and "
        "interval of rising and falling on this course is an exact fraction or an exact "
        "polynomial with rational coefficients, computed in your browser. <strong>One lab "
        "rounds, and says so</strong>: the quotients of `bᵗ` in the last lesson are "
        "irrational for most steps, so each is printed with `≈` to six figures and labelled "
        "rounded, and the number they head for is shown as a name such as `ln 2` beside its "
        "rounded value. One idea is stated and not proved, and says so: that a column of "
        "quotients settles on a single number. For a polynomial the algebra proves it; for "
        "everything else the table is evidence, and the lessons say which is which."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
