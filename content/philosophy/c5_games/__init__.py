"""Course 5 -- Games and the Social Contract.

Split across two lesson modules so each is a file a reviewer can read.
part_a is one-shot games and repeated games (strategic form to the shadow of
the future); part_b is the social contract and the many-player games. The
design is docs/philosophy/PLAN.md, section C, course 5.
"""

from . import part_a, part_b

COURSE = {
    "slug": "games-and-the-social-contract",
    "title": "Games and the Social Contract",
    "level": "Intermediate",
    "summary": (
        "Strategic interaction from the payoff table up: best responses, the prisoner's dilemma, Nash equilibrium "
        "in pure and mixed strategies, conventions and the stag hunt, repeated play and the shadow of the future, "
        "and the many-player games in which Hobbes's state of nature, the commons and the public good are all "
        "the same dilemma at different sizes."
    ),
    "blurb": (
        "Take a social-contract argument and write it as a game. Read a payoff table, find every cell where no one "
        "gains by moving alone, see why the cell can be worse for everyone than another, and compute exactly what "
        "changes it: a repeated game, a sovereign's penalty, a fee, a change in who meets whom."
    ),
    "key": [
        "Nash: no player gains by moving alone",
        "dilemma: each defects, both do worse",
        "convention: stable because others conform",
        "GRIM holds if δ ≥ (T − R) / (T − P)",
        "commons: the gain is mine, the cost is shared",
        "replicator: shares follow relative payoff",
    ],
    "assumes_short": "Decision and Rationality",
    "assumes_long": "Decision and Rationality, for the idea that a payoff stands for what an outcome is worth and that a "
                    "player prefers the larger expected one, and nothing else",
    "outcomes_intro": (
        "By the end you can take a situation of interdependent choice, write it as a table or a pair of payoff "
        "expressions, and compute what follows from it."
    ),
    "outcomes": [
        ("Mark a bimatrix",
         "Read a two-player table, mark each player's best response to each move of the other, and name the cells "
         "where both marks fall."),
        ("Show that a game is a dilemma",
         "Establish that a strategy strictly dominates, locate the equilibrium it leads to, and show that another cell "
         "pays every player more."),
        ("Compute an equilibrium and a threshold",
         "Solve a two-by-two game for its mixed equilibrium exactly, and read the same number as the belief at which a "
         "risky choice is worth taking."),
        ("Derive the discount factor",
         "Compute the continuation probability above which cooperation is stable against a punishing partner, "
         "and state why a known last round removes it."),
        ("Model the state of nature and the commons",
         "Write Hobbes's argument, the herders' commons and the public-goods game as games, find each equilibrium and "
         "optimum, and show what a penalty or a fee changes."),
        ("Run the replicator step",
         "Update a population's share of cooperators generation by generation in exact fractions, and say where it ends up."),
    ],
    "syllabus_intro": (
        "One-shot games come first, then the same dilemma repeated, then many players at once."
    ),
    "how_to": [
        "Work forward. Each lesson uses the table-reading of “Strategic Form and Best Responses” and the idea of an "
        "equilibrium from “Nash Equilibrium in Pure and Mixed Strategies”. The repeated games in “Repeated Games and "
        "Reciprocity” make no sense without the one-shot dilemma in “The Prisoner's Dilemma”.",
        "Change the payoffs. Every lab here lets you retype the table, and most of the course is a claim that one "
        "number matters or does not: the temptation in the dilemma, the crash in chicken, the hare in the stag hunt, "
        "the fee on a commons. Make the claim false and watch which tile says so.",
        "Keep the payoffs and the people apart. A game is a table of numbers, and which numbers describe a real "
        "pair of hunters, drivers or states is a judgment the lab cannot make. The arguments on this course are "
        "conditional: if the payoffs are these, then this follows.",
        "Read the quizzes for the reason, not the answer. Each wrong choice is the answer someone gives from one "
        "of the course's standing misconceptions, and the explanation says which one.",
    ],
    "not_covered": [
        "Games played in turns. Every game here is in strategic form, with the players choosing at once. Trees, "
        "backward induction as a general method, subgame perfection and credible threats are not built; the only "
        "backward argument is the unravelling of a known last round.",
        "Games of incomplete information. The players know the payoffs and each other's strategies. Bayesian "
        "games, signalling, and reputation built on doubt about a partner's type are left out.",
        "Cooperative game theory, bargaining and mechanism design. Shapley values, the Nash bargaining solution "
        "and the design of rules to produce a chosen outcome are different subjects; the course stops where a "
        "sovereign's penalty changes the payoffs.",
        "Proofs. Nash's theorem that a finite game has a mixed equilibrium is stated and the equilibria are "
        "computed, but the theorem is not proved, and the replicator step is given as a rule rather than derived "
        "from a model of selection.",
        "The history of social contract theory as history. Hobbes and Hume appear as arguments, written as games "
        "and tested; what they said, to whom, and why is not here, and nor is the experimental evidence on how "
        "real people play these games.",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every equilibrium on this course is found by checking "
        "every cell, every threshold is a ratio of exact fractions, and every repeated match is played out "
        "round by round in your browser. What the labs cannot do is tell you that a payoff is the right "
        "number for a real prisoner, farmer or state, and the arguments turn on that."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
