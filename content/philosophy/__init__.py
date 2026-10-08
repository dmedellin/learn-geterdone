"""The Philosophy path, as data.

Ten courses in one order. The content lives here and only here; scripts/
turns it into pages. Nothing in this package emits markup beyond the inline
`x` shorthand, and nothing in scripts/ decides what a lesson says.

Every verdict on this path is computed from what a lesson states: a validity
check from every row of a truth table, a posterior from exact fractions, an
equilibrium from every cell. The design is docs/philosophy/PLAN.md.
"""

from . import (
    c1_arguments,
    c2_knowledge,
    c3_science,
    c4_decision,
    c5_games,
    c6_ethics,
    c7_justice,
    c8_metaphysics,
    c9_mind_language,
    c10_paradoxes,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_arguments.COURSE,
    c2_knowledge.COURSE,
    c3_science.COURSE,
    c4_decision.COURSE,
    c5_games.COURSE,
    c6_ethics.COURSE,
    c7_justice.COURSE,
    c8_metaphysics.COURSE,
    c9_mind_language.COURSE,
    c10_paradoxes.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "philosophy",
    "title": "Philosophy",
    "level": "Beginner \u2192 Advanced",
    "level_note": "school arithmetic only; the logic is taught inside",
    "tagline": (
        "Arguments you can test, beliefs you can measure, choices you can rank: philosophy taught through the structures it is made of &mdash; validity, consistency, credence, expected value, equilibrium, collective choice and possible worlds &mdash; from the first argument to the hardest paradox. Ten courses and 108 lessons are available."
    ),
    "description": (
        "The Philosophy Subject: ten courses in one order, from arguments and validity through knowledge and evidence, science and causation, decision, games and the social contract, ethics, justice and collective choice, identity, modality and freedom, mind, language and meaning, to the paradoxes. Every lesson computes something from the premises, cases or payoffs it states &mdash; a counterexample row, a posterior, an equilibrium, a winner &mdash; in exact arithmetic in your browser. All ten courses and 108 lessons are available."
    ),
    "key": [
        "valid \u27fa no row: premises T, conclusion F",
        "P(H | E) = P(E | H)\u00b7P(H) / P(E)",
        "EU(a) = \u03a3 P(s)\u00b7u(a, s)   take the largest",
        "Nash: no player gains by moving alone",
        "A beats B, B beats C, C beats A   a cycle",
        "\u25a1p at w  \u27fa  p at every world w can see",
        "a paradox: valid, plausible, unacceptable",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. Knowledge and Evidence uses the validity and consistency tests of Arguments and Validity; Decision and Rationality uses the credences of Knowledge and Evidence; Games and the Social Contract uses expected utility; Ethics and the Arithmetic of Welfare uses decision matrices, the n-player dilemma and the causal models of Science, Induction and Causation; Identity, Modality and Freedom introduces modal logic and Mind, Language and Meaning builds on it; Paradoxes and Their Exits uses all of it."
    ),
    "why_order": [
        "Arguments come first because everything that follows is an argument. Validity, consistency and the counterexample are the three tools every later lesson reaches for, and a reader who cannot yet tell a valid argument from a persuasive one will misread the strongest positions in the Subject as the weakest.",
        "Knowledge and evidence come second because credence is the currency of the next six courses. Updating on evidence is introduced there once, with exact fractions, and used without re-derivation in Science, Induction and Causation, in Decision and Rationality and in every paradox of probability at the end.",
        "Decision precedes games, and both precede ethics and justice, because expected utility, equilibrium and the n-player dilemma are the instruments with which the ethical theories are compared rather than merely described. Utilitarianism is an aggregation rule; Kant&rsquo;s test is an outcome at universal adoption; the social contract is a game.",
        "Metaphysics, mind and language come late because they need modal logic and first-order models, which are introduced where they are first used and nowhere earlier. Paradoxes come last because a paradox is where all of these tools are needed at once, and because by then the reader has met most of them in passing and can be asked to classify the exit.",
    ],
    "prerequisites": [
        "School arithmetic: fractions, percentages, and the willingness to add up a column. Every number on this path is a fraction or a whole number, and the labs do the arithmetic; what is asked of you is to read it.",
        "No logic. Arguments and Validity teaches every piece of logic the Subject uses, starting from what an argument is. If you have met truth tables before you will move quickly through its first half; if you have not, it is where to start.",
        "No probability. Knowledge and Evidence introduces credence and Bayes&rsquo; rule from a table of a million people, and nothing later assumes more than that lesson gives. Discrete Probability on the Discrete Mathematics path covers the same ground more formally and is a fine companion, not a prerequisite.",
        "Patience with premises. The hard part of philosophy is not following an argument but deciding which premise to doubt, and the labs cannot do that for you. They will tell you an argument is valid; whether to accept its conclusion or reject a premise is the question every lesson leaves open on purpose.",
    ],
    # Each path names its own hazard. This one's is that a lab can check every
    # step from the premises and none of the premises.
    "material": (
        "every verdict on this path is computed in your browser from the premises, "
        "cases and payoffs the lesson states, and a verdict is only as good as the "
        "premises it was computed from &mdash; which is the part no lab can check, "
        "and the part philosophy is about."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every verdict on this path is computed in your browser from what the lesson states: a truth table is built by evaluating the formula under every assignment, a posterior is a ratio of exact fractions, an equilibrium is found by checking every cell, a winner by counting every ballot. Nothing is rounded except where a lesson says so. What the labs cannot do is tell you whether a premise is true, whether a case has been described fairly, or whether a payoff is the right number &mdash; and those are the questions the arguments turn on."
    ),
    "courses": COURSES,
}
