"""Course 7 -- Justice and Collective Choice.

Split across two lesson modules. part_a is distributive justice and the first
lesson on collective choice; part_b is the rest of social choice and the jury
theorem. The design is docs/philosophy/PLAN.md, section C, course 7.
"""

from . import part_a, part_b

COURSE = {
    "slug": "justice-and-collective-choice",
    "title": "Justice and Collective Choice",
    "level": "Advanced",
    "summary": (
        "Justice and group decision taken as the arguments and procedures they are: the original position as a choice between "
        "maximin and equal chances, the difference principle as leximin, entitlement against pattern measured by the Gini "
        "coefficient, fairness statistics and disparate rates, then majority rule and its paradox, plurality, runoff and Borda, "
        "Arrow's theorem on a profile, strategic voting, the discursive dilemma and the Condorcet jury theorem."
    ),
    "blurb": (
        "Choose a society from behind a veil and watch two rules disagree, rank distributions by their worst-off member, "
        "measure what a free exchange does to equality, and tell a gap in treatment from a gap in outcome. Then count the "
        "ballots: find the profile where the majority goes in a circle, the one where three rules elect three "
        "candidates, the voters who gain by lying, the court whose majorities contradict themselves, and the electorate "
        "that gets wiser as it grows only when its voters are better than chance."
    ),
    "key": [
        "maximin: take the best worst case",
        "leximin: the worst off first, then the next",
        "Gini = 0 for equal shares, up with the gaps",
        "A beats B, B beats C, C beats A   a cycle",
        "no rule meets Arrow's three on every profile",
        "premises can pass while their conclusion fails",
        "p above 1/2: a majority beats one voter",
    ],
    "assumes_short": "Ethics and the Arithmetic of Welfare",
    "assumes_long": (
        "Ethics and the Arithmetic of Welfare, for the aggregation rules and the argument about priority and levelling down, "
        "and the courses it builds on for decision tables, the n-player dilemma and probability"
    ),
    "outcomes_intro": (
        "By the end you can state a theory of justice or a voting rule as a computation, run it on a case, and say which "
        "premise a disagreement turns on."
    ),
    "outcomes": [
        ("Model a choice behind the veil",
         "Lay the original position out as a decision matrix with the chooser's place as the unknown state, and show that "
         "maximin and equal chances choose different societies from the same table."),
        ("Rank distributions and measure inequality",
         "Order two distributions by leximin, compute a Gini coefficient before and after a round of voluntary transfers, and "
         "state what an unequal distribution must do for the worst off to be allowed."),
        ("Separate unequal treatment from unequal outcome",
         "Compute acceptance rates within groups and pooled, standardise them, and say which notion of fairness each "
         "comparison tests."),
        ("Tabulate a vote under several rules",
         "Count pairwise majorities, find a Condorcet winner or a cycle, and run plurality, runoff, instant runoff and Borda on "
         "one profile to show that they can elect different candidates."),
        ("State and test the impossibility results",
         "Check unanimity, independence and non-dictatorship on a profile, find a group that gains by misreporting its "
         "ranking, and say what Arrow's and Gibbard and Satterthwaite's theorems do and do not claim."),
        ("Aggregate judgments and compute a jury",
         "Show a court whose majorities on the premises contradict its majority on the conclusion, and compute the probability "
         "that a majority of independent voters is right and that one vote decides."),
    ],
    "syllabus_intro": (
        "Distributive justice comes first, because it asks what a fair arrangement is. The second half asks how a group could "
        "reach any arrangement at all, and the answers are less comfortable than the question."
    ),
    "how_to": [
        "Work forward. The later lessons on voting assume you can read the table of pairwise counts that "
        "“Majority Rule and the Condorcet Paradox” introduces, and the lessons on distribution assume the "
        "aggregation rules of Ethics and the Arithmetic of Welfare.",
        "Change the profile and the table. Each lab is a small instance you can edit, and each lesson turns on a figure, "
        "a winner or a rate that moves when the input does. Edit a number, predict the verdict, and then read it off; "
        "the prediction is where the learning is.",
        "Hold the positions loosely. Each argument is stated at its strongest and its premises are marked. Whether to accept "
        "Rawls's veil, Nozick's history or Harsanyi's equal chances is left to you on purpose, and so is the choice between "
        "equal treatment and equal outcome.",
    ],
    "not_covered": [
        "The proofs of the impossibility theorems. Arrow's theorem and the Gibbard&ndash;Satterthwaite theorem are stated, "
        "and their conditions are checked on profiles you can edit, but the arguments that no rule satisfies them all are not "
        "reproduced.",
        "Sen's liberal paradox. It needs a machinery of rights and rankings that the lab does not build, and a version "
        "that omitted the machinery would misstate it.",
        "Statistics as inference. The fairness lesson computes rates from counts; nothing is estimated, no test of "
        "significance is run, and nothing here says how large a disparity must be before it is real.",
        "Political philosophy beyond these arguments. Legitimacy, authority, rights, the justice of war and of global "
        "distribution have no computation attached, and the course does not pretend otherwise. Rawls and Nozick appear "
        "as arguments with premises, not as authors with systems.",
    ],
    "footer_lead": (
        "Every figure on this course is computed in your browser from the profile, the table or the distribution you can see: "
        "a winner is found by counting every ballot, a Gini coefficient by summing every gap and a jury's probability by "
        "adding exact fractions. The labs cannot tell you whether a welfare number measures welfare, whether a "
        "voter's ranking is sincere or whether the voters are independent, and the arguments here turn on exactly those things."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
