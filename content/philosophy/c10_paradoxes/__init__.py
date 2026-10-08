"""Course 10 -- Paradoxes and Their Exits.

Split across two lesson modules. part_a is the method and the infinite (the
barber, the liar, Zeno, Achilles and the lamp); part_b is the paradoxes of
probability and belief.
"""

from . import part_a, part_b

COURSE = {
    "slug": "paradoxes-and-their-exits",
    "title": "Paradoxes and Their Exits",
    "level": "Advanced",
    "summary": (
        "What a paradox is and the three exits from one, then nine of them worked "
        "through: the barber, the liar, Zeno's dichotomy, Achilles and the tortoise, "
        "Thomson's lamp, the two envelopes, Sleeping Beauty, Monty Hall and Moore's "
        "paradox. Each lesson ends by asking you to name the exit and what it costs."
    ),
    "blurb": (
        "A paradox is a valid-looking argument from plausible premises to a conclusion "
        "no one can accept. Here each one is computed: a sentence with no satisfying "
        "row, a series with an exact limit, a posterior that depends on a likelihood "
        "model, a modal sentence true at one world and believed at none. The labs find "
        "where the argument turns, and the choice of exit is left to you."
    ),
    "key": [
        "a paradox: valid, plausible, unacceptable",
        "exit: deny a premise, fault a step, accept",
        "p ↔ ¬p is false in every row",
        "1/2 + 1/4 + 1/8 + ... has the limit 1",
        "P(H | E) = P(E | H)·P(H) / P(E)",
        "p ∧ ¬□p can be true, and cannot be known",
    ],
    "assumes_short": "everything before it",
    "assumes_long": (
        "the rest of the Subject, since a paradox is where its tools are needed at "
        "once: the truth tables and counterexamples of Arguments and Validity, the "
        "credences and updating of Knowledge and Evidence, the expected values of "
        "Decision and Rationality, and the possible worlds of Identity, Modality and "
        "Freedom"
    ),
    "outcomes_intro": (
        "By the end you can take a paradox apart into its premises, test what can be "
        "tested by computation, and say which exit a reply takes and what it costs."
    ),
    "outcomes": [
        ("Classify a paradox by its exit",
         "Set an argument out as premises and a conclusion, check the steps, and name "
         "whether the best reply denies a premise, faults a step or accepts the "
         "conclusion."),
        ("Show a sentence has no satisfying row",
         "Build the model or the truth table for the barber and the liar, and say why "
         "the failure of every row does not by itself say which premise to give up."),
        ("Compute an infinite sum exactly",
         "Sum Zeno's halves and Achilles' gaps as geometric series, state the limit and "
         "the remainder after any number of steps, and say when there is no limit."),
        ("Separate what a series settles from what it leaves open",
         "For Thomson's lamp, compute the time of every switch and show that the state "
         "after them has no limit."),
        ("Compute the posterior a paradox depends on",
         "For the two envelopes, Sleeping Beauty and Monty Hall, write the likelihood "
         "model, compute the posterior and the best act, and say which assumption the "
         "disagreement is about."),
        ("Show a true sentence that cannot be believed",
         "In a possible-worlds model, find the world where Moore's sentence is true and "
         "show that its believed form is true at no world of a reflexive frame."),
    ],
    "syllabus_intro": (
        "The method comes first, with the barber as the plainest case. The paradoxes "
        "of the infinite follow, because their arithmetic is exact, then those of "
        "probability, where the figures depend on a model, and the last paradox is "
        "about belief itself."
    ),
    "how_to": [
        "Work forward. “The Liar” uses the form that “The Barber and the Anatomy of a "
        "Paradox” ends with, and the lessons on the infinite assume the geometric series of "
        "“Zeno's Dichotomy”. The three exits are introduced once and used in every lesson "
        "afterwards.",
        "Expect to meet old paradoxes again. The sorites was taught in “Vagueness and the "
        "Sorites” and the slippery slope in “Slippery Slopes and Small Differences”; the "
        "lottery paradox in “The Lottery Paradox”; Newcomb's problem in “Newcomb's "
        "Problem”; Simpson's paradox in “Correlation, Confounding and Simpson's Paradox”; "
        "the ravens in “The Raven Paradox”; grue in “Grue and the New Riddle”; Gettier "
        "cases in “Gettier Cases and the Fourth Condition”; the ship of Theseus in “The "
        "Ship of Theseus”; and the Condorcet paradox in “Majority Rule and the Condorcet "
        "Paradox”. Each was worked where its tools were introduced, and the question "
        "asked of each there, which premise to doubt and at what cost, is given its "
        "general form in the first lesson here and asked of the rest.",
        "Compute before you argue. Every lab here gives a figure that decides something: "
        "a row that is absent, a limit, a remainder, a posterior, a world. Read the "
        "figure first, then ask which premise it leaves standing.",
        "Hold the exits loosely. Each lesson states the argument at its strongest and "
        "each exit at its strongest, with what it costs. Which exit to take is left to "
        "you, on purpose, and the labs cannot choose it.",
    ],
    "not_covered": [
        "The surprise examination and the unexpected hanging. They need an epistemic "
        "logic with announcements that the Subject does not build, and a "
        "treatment that leaves them as stories would misrepresent them.",
        "Curry's paradox and the logics built to avoid it. It needs a consequence "
        "relation weaker than the classical one, and every lab here uses the classical "
        "table.",
        "The Ross–Littlewood paradox, which needs a limit of sets and not of numbers, "
        "and Pascal's mugging, which needs an unbounded utility. Both are named here "
        "and not worked.",
        "The full theory of truth. The liar is taught through the table and Tarski's "
        "hierarchy; the fixed-point constructions, revision theories and the arguments "
        "about revenge are not built.",
        "Continuous probability and infinite outcome spaces. Every posterior is over "
        "finitely many hypotheses, and the two envelopes are treated under a bounded "
        "prior for that reason.",
    ],
    "footer_lead": (
        "Every figure on this course is computed in your browser from what the lesson "
        "states: a truth table by evaluating the formula in every row, a series by exact "
        "fractions, a posterior as a ratio of exact fractions, a modal sentence by "
        "checking every world. The labs cannot tell you which premise of a paradox to "
        "give up, and that choice is what each paradox is about."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
