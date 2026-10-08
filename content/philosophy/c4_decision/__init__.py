"""Course 4 -- Decision and Rationality.

Split across two lesson modules. part_a is preference, the rules for ignorance
and the first two lessons on risk; part_b is the two paradoxes that close the
Risk module (Allais, Ellsberg) and the three puzzles of expected value.
"""

from . import part_a, part_b

COURSE = {
    "slug": "decision-and-rationality",
    "title": "Decision and Rationality",
    "level": "Intermediate",
    "summary": (
        "How to choose when you cannot be sure how things will turn out: preference "
        "and its structure, decision tables, the rules for ignorance, expected "
        "utility, and the paradoxes (Allais, Ellsberg, Pascal, Newcomb and St "
        "Petersburg) that test it."
    ),
    "blurb": (
        "Lay a choice out as acts against states and see what each rule says. "
        "Money pumps, dominance, maximin and regret, expected utility and the "
        "value of information, then five puzzles in which the rule seems to "
        "give the wrong answer, each computed to the figure at which it turns."
    ),
    "key": [
        "A ≻ B, B ≻ C, C ≻ A   a cycle: pumpable",
        "maximin: best of the row minimums",
        "regret = column best − your payoff",
        "EU(a) = Σ P(s)·u(a, s)   take the largest",
        "VPI = expected best − best expected",
        "Pascal wins when M > c / p",
    ],
    "assumes_short": "Knowledge and Evidence",
    "assumes_long": (
        "Knowledge and Evidence, for credence as a degree of belief and for the "
        "rule that probabilities add to 1"
    ),
    "outcomes_intro": (
        "By the end you can lay a decision out as a table, say what each rule "
        "recommends and why they differ, and compute the point at which a famous "
        "paradox turns."
    ),
    "outcomes": [
        ("Test a preference for order",
         "State completeness and transitivity, find the pair that breaks "
         "transitivity on a relation grid, and compute what a cycle costs a "
         "chooser per lap."),
        ("Choose without probabilities",
         "Apply dominance, maximin, maximax and minimax regret to one table, and "
         "find an instance in which the rules disagree."),
        ("Choose with probabilities",
         "Compute expected utility, the probability at which a choice flips, the "
         "effect of a concave utility, and the value of perfect information."),
        ("Pin down a paradox",
         "Show that the Allais choices are inconsistent with any utilities, that "
         "the Ellsberg choices fit no single proportion, and where Pascal's wager "
         "and Newcomb's problem turn."),
        ("Price an infinite expectation",
         "Show that the St Petersburg game's expected value diverges, and compute "
         "the finite value once the bank's bankroll is capped."),
    ],
    "syllabus_intro": (
        "Preference comes first, then the rules that need no probabilities, then "
        "the rules that do, and the paradoxes come last because each one "
        "presses on a different premise of what came before."
    ),
    "how_to": [
        "Work forward. “Expected Value and Expected Utility” assumes you can read a "
        "decision table, which “The Decision Matrix and Dominance” teaches, and the "
        "paradoxes assume expected utility.",
        "Change the numbers. Every lab here is a decision table you can edit, and "
        "most lessons turn on a figure at which a choice flips. Move a probability "
        "or a payoff across that figure and watch the recommendation change; it "
        "is faster than reading the argument for it.",
        "Hold the paradoxes loosely. Each lesson states the argument for the puzzling "
        "choice at its strongest and shows where it conflicts with the rule. Whether "
        "to give up the choice or the rule is left to you, on purpose.",
    ],
    "not_covered": [
        "The representation theorems. This course states what a consistent "
        "chooser's utilities are and uses them; it does not prove that preferences "
        "satisfying a list of axioms must be representable by expected utility.",
        "Causal decision theory in full. Newcomb's problem is computed under the "
        "evidential rule and under dominance, which is as far as the table goes; "
        "the machinery for the causal alternative is not built.",
        "Continuous probability and unbounded utilities. Every table is finite, "
        "and every probability a fraction. Pascal's mugging, which needs an "
        "unbounded utility, is named in the last course and not worked.",
        "Behavioural economics as a science. The Allais and Ellsberg patterns are "
        "treated as logical puzzles about consistency; how often people show them, "
        "and why, is a question for experiment and not for a table.",
    ],
    "footer_lead": (
        'Every figure on this course is computed in your browser from the table '
        'you can see: an expected utility is a sum of exact fractions and a '
        'tipping point is solved, not guessed. The labs cannot tell you that a '
        'payoff is the right number or that a probability is the right credence, '
        'and every paradox here lives in exactly that gap.'
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
