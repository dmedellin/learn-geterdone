"""Course 2 -- Knowledge and Evidence.

Split across two lesson modules. part_a is the analysis of knowledge, the
problem of justification and the opening of credence; part_b is conditional
credence through the lottery and preface paradoxes.
"""

from . import part_a, part_b

COURSE = {
    "slug": "knowledge-and-evidence",
    "title": "Knowledge and Evidence",
    "level": "Beginner → Intermediate",
    "summary": (
        "Knowledge analysed and tested against cases, skepticism and the regress of "
        "justification as arguments the labs can check, and then belief measured as "
        "credence: Dutch books, base rates, updating, testimony, reference classes, "
        "and the lottery and preface paradoxes where belief and credence come apart."
    ),
    "blurb": (
        "What it takes to know something, and what it takes to believe it to a degree. "
        "A definition of knowledge is tried against cases until one row disagrees; "
        "skepticism and the regress are written as arguments and sets of claims; and "
        "credence is computed with exact fractions, from a Dutch book to a posterior."
    ),
    "key": [
        "a definition: tested by cases, row by row",
        "credence: the price of a bet that pays 1",
        "P(H | E) = P(E | H)·P(H) / P(E)",
        "independent witnesses: Bayes factors multiply",
        "belief at a threshold is not closed under ∧",
    ],
    "assumes_short": "Arguments and Validity",
    "assumes_long": (
        "Arguments and Validity, which supplies validity, the counterexample row and "
        "consistency; no probability is assumed"
    ),
    "outcomes_intro": (
        "By the end you can test a theory of knowledge against a table of cases, and "
        "you can compute with degrees of belief instead of arguing about them."
    ),
    "outcomes": [
        ("Test a definition against cases",
         "Write the conditions of an analysis of knowledge, record a verdict for each "
         "case, and find the row where the definition and the verdict part company "
         "&mdash; and say whether the definition is too broad or too narrow there."),
        ("Formalise a skeptical argument and its reply",
         "Write the brain-in-a-vat argument and Moore’s answer as two valid "
         "arguments over one conditional, and say what choosing between them "
         "requires that validity cannot give."),
        ("Locate the exits from the regress",
         "Write Agrippa’s trilemma as a set of claims that cannot all be true, "
         "and name the position that each single deletion yields."),
        ("Check credences for coherence",
         "Assign degrees of belief to the events of a small outcome space, test them "
         "against the rules of probability, and construct the bets that lose for "
         "certain when the rules are broken."),
        ("Compute what evidence does",
         "Work out a posterior from a prior and likelihoods, read the Bayes factor as "
         "the weight of the evidence, and combine independent witnesses by "
         "multiplying their factors."),
        ("Explain why belief and credence come apart",
         "Show with the lottery and the preface that accepting every claim above a "
         "threshold does not leave a set of acceptances whose conjunction is likely."),
    ],
    "syllabus_intro": (
        "Knowledge is analysed first, then justification is put under pressure, then "
        "belief is measured, and last the measure is turned on statistics and on the "
        "two paradoxes where it fails to match belief."
    ),
    "how_to": [
        "Work forward, and keep the tables. “Belief, Truth and Justification” sets "
        "the method that “Gettier Cases and the Fourth Condition” and “Reliabilism "
        "and the Clairvoyant” reuse: a definition, a column of verdicts, and the "
        "first row where they differ. The verdicts are yours. The lab checks that "
        "the definition agrees with them, not that they are right.",
        "Treat each valid argument as a map of choices rather than a result. "
        "“Skepticism and the Closure Argument” and “The Regress of Justification” "
        "have labs that say an argument is valid or a set inconsistent, and then "
        "stop. Which premise to give up is the question the lesson leaves open on "
        "purpose.",
        "Do the credence arithmetic by hand once before the lab does it. “Credence "
        "and the Dutch Book”, “Conditional Credence and Base Rates” and “Updating "
        "on Evidence” each have a worked example small enough to finish on paper, "
        "and a result you will not believe until you have. Every number here is an "
        "exact fraction; nothing is rounded unless the lesson says so.",
        "Read the last three lessons as a single argument. “Reference Classes and "
        "Statistical Evidence”, “The Lottery Paradox” and “The Preface Paradox” "
        "turn the credence tools on belief itself, and both paradoxes end by "
        "asking which of two reasonable principles to give up.",
    ],
    "not_covered": [
        "The history of epistemology as history. Descartes, Hume and Gettier appear "
        "as arguments and cases to be tested, not as names with dates; who said what "
        "first is not something a lab can compute.",
        "Every theory of knowledge. Contextualism, virtue epistemology, "
        "knowledge-first epistemology and safety and sensitivity conditions are "
        "named at most in passing. The course teaches the method of cases on the "
        "tripartite analysis, its repair and one rival, and the method carries over.",
        "Formal epistemology beyond coherence. Imprecise credences, accuracy "
        "arguments and the logic of knowledge and announcement are not built. "
        "Credence here is a number on a finite outcome space.",
        "Statistics as inference. Significance tests, confidence intervals and "
        "regression estimate things from data; this course only updates exact "
        "priors on exact likelihoods over a few hypotheses, with no densities and "
        "no integrals.",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every verdict on this course "
        "is computed in your browser from what the lesson states: a definition is "
        "compared with a table of cases, a set of claims is searched for a model, a "
        "posterior is a ratio of exact fractions. What the labs cannot tell you is "
        "whether a verdict about a case is right, whether a premise is true, or "
        "whether a credence is a reasonable one rather than merely a coherent "
        "one &mdash; and those are the questions the course is about."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
