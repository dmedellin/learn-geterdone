"""Foundations of Algebra."""

from . import part_a, part_b

_LESSONS_BY_SLUG = {
    lesson["slug"]: lesson for lesson in part_a.LESSONS + part_b.LESSONS
}

# The records remain split by subject matter in part_a and part_b, while the
# teaching order puts numeric notation first and defines a variable before any
# lesson asks the reader to justify a symbolic rearrangement.
_LESSON_ORDER = (
    "real-numbers-and-the-number-line",
    "order-of-operations",
    "algebraic-expressions-and-terms",
    "properties-of-the-real-numbers",
    "absolute-value",
    "integer-exponents",
    "scientific-notation",
    "roots-and-radicals",
    "rational-exponents",
    "the-distributive-law",
    "combining-like-terms",
    "evaluating-expressions",
    "translating-words-into-algebra",
)

COURSE = {
    "slug": "algebra-foundations",
    "title": "Foundations of Algebra",
    "level": "Beginner",
    "summary": (
        "The real numbers and the rules for operating on them: order of operations, "
        "what a letter and a term mean, the properties that license a rearrangement, "
        "integer and rational exponents, radicals, absolute value, and the translation "
        "from a stated quantity to an expression."
    ),
    "blurb": (
        "Arithmetic, made general. Why a letter can stand for a number, which rearrangements are always allowed and which only look allowed, and the exponent and radical rules that everything after this course leans on."
    ),
    "key": [
        "a(b + c) = ab + ac                 the distributive law",
        "x^m · x^n = x^(m+n)                exponents add",
        "x^(1/n) = the n-th root of x",
        "|x| = x if x ≥ 0, −x if x < 0",
    ],
    "assumes_short": "Arithmetic",
    "assumes_long": "fractions, negatives, and long division",
    "outcomes_intro": (
        "By the end you can read, evaluate and simplify the real-number expressions the "
        "next courses use, with a stated reason for every rearrangement."
    ),
    "outcomes": [
        ("Evaluate without ambiguity",
         "Apply the order of operations to an expression with nested brackets, exponents and a fraction bar, and get the value a marker gets."),
        ("Name the property you used",
         "Say which of commutativity, associativity, distribution or the identity you just applied &mdash; and notice when you have used one that does not exist."),
        ("Simplify powers and radicals under their conditions",
         "Combine powers with a common base, handle zero and negative exponents, convert "
         "between `x^(1/n)` and roots, decide whether a real root exists, and simplify "
         "a numerical radical exactly."),
        ("Turn a sentence into an expression",
         "Translate an English quantity into algebra, keeping track of what the letter stands for &mdash; which is where most word-problem errors are made."),
    ],
    "syllabus_intro": (
        "Lessons 1 and 2 settle the numbers and how notation is read; lesson 3 names the "
        "parts of an expression before lesson 4 licenses rearrangements. Lessons 5 to 9 "
        "cover absolute value, exponents and radicals; lessons 10 to 13 expand, collect, "
        "evaluate and translate expressions."
    ),
    "how_to": [
        "Do the arithmetic yourself before you read the answer. Every lab shows its steps, and the steps are worth more than the result &mdash; the result you could have got from a calculator.",
        "Take the property lessons seriously even if the arithmetic is easy. Lesson 4 is "
        "the reason `-(x - 3)` is `-x + 3`, and that single sign is the most common error "
        "in the next two courses.",
        "When a lab disagrees with you, find which step differs rather than which answer. The step is the thing you will repeat a thousand times.",
    ],
    "not_covered": [
        "Proof of the field axioms. This course states the properties of the real numbers and uses them; constructing the reals from the rationals belongs to analysis.",
        "Complex numbers. `sqrt(-4)` has no value on this course and is said to have none; course 6 introduces `i` and gives it one.",
        "Trigonometry and logarithms. Logarithms arrive in course 7, where exponentials make them necessary; trigonometry is not on this path at all.",
    ],
    "footer_lead": (
        "Every value on this course is computed in your browser by applying the rule the lesson states, and the arithmetic is exact &mdash; a third is `1/3` through every step, not `0.3333`. Where a lesson is about approximation it says so and shows the rounding it did."
    ),
    "lessons": [_LESSONS_BY_SLUG[slug] for slug in _LESSON_ORDER],
}
