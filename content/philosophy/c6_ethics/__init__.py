"""Course 6 -- Ethics and the Arithmetic of Welfare.

Split across two lesson modules. part_a is metaethics in outline and
consequentialism (the first six lessons); part_b is deontology, virtue and
method. The design is docs/philosophy/PLAN.md, section C, course 6.
"""

from . import part_a, part_b

COURSE = {
    "slug": "ethics-and-welfare",
    "title": "Ethics and the Arithmetic of Welfare",
    "level": "Intermediate → Advanced",
    "summary": (
        "Moral theories taught as the structures they are made of: is and ought as a validity question, definitions of “good” tested against cases, utilitarian aggregation and its population paradoxes, priority and equality, the trolley problem as a decision matrix with a side constraint, Kant’s test as an outcome at universal adoption, double effect as a path in a causal model, omissions as causes, dilemmas as inconsistent sets, the function argument and slippery slopes."
    ),
    "blurb": (
        "Put a number on a moral view and see what it commits you to. Add up welfare and find who the sum ignores, count the people needed to beat a flourishing life, weigh the worse off, forbid an act and watch a recommendation flip, and test a duty by asking what happens when everyone does it."
    ),
    "key": [
        "facts alone never entail an ought",
        "a definition fails: too broad, too narrow",
        "total welfare cannot see who gets what",
        "n·ε > total(A): the crowd that beats A",
        "priority: a gain counts more the lower down",
        "a side constraint deletes an act first",
        "double effect: is the harm the means?",
    ],
    "assumes_short": "Decision and Rationality; Games and the Social Contract; Science, Induction and Causation",
    "assumes_long": (
        "decision matrices and expected value from Decision and Rationality, the n-player dilemma from Games and the Social Contract, and the causal models of Science, Induction and Causation"
    ),
    "outcomes_intro": (
        "By the end you can state a moral position as something with a checkable structure, compute what it recommends on a case, and say which premise a critic would reject."
    ),
    "outcomes": [
        ("Show where an argument needs a moral premise",
         "Find the counterexample row for an argument from facts to a duty, write the bridging premise that closes it, and say what accepting that premise commits the arguer to."),
        ("Test a definition against cases",
         "Evaluate a proposed definition of “good” on a table of cases, classify each failure as too broad or too narrow, and see which definitions survive the verdicts you accept."),
        ("Compare distributions of welfare",
         "Rank two outcomes by total, average, priority-weighted score and Gini coefficient, and compute the population at a tiny welfare level that beats a flourishing one."),
        ("Apply a side constraint to a decision matrix",
         "Lay a trolley case out as acts against outcomes, apply total welfare, forbid an act, and name the case in which the recommendation changes."),
        ("Model the structure behind a deontic claim",
         "Test a universalisation, a means-or-side-effect distinction and an omission in a small model, and write a dilemma as a set of principles that cannot all hold."),
        ("Mark where a method breaks down",
         "Formalise a function argument and a slippery slope, find the premise each one needs, and say what each of four treatments of vagueness does to the slope."),
    ],
    "syllabus_intro": (
        "The course runs from the logic of moral argument, through the theories that add welfare up, to the theories that forbid acts whatever the sum, and ends with two methods that cut across the divide."
    ),
    "how_to": [
        "Work forward. The consequentialist lessons assume the earlier ones: “Total, Average and the Repugnant Conclusion” leans on the totals computed in “Utilitarianism and the Sum of Welfare”, and “The Trolley Problem as a Decision Matrix” needs the decision matrix from Decision and Rationality.",
        "Change the numbers. Every lab accepts a distribution, a payoff table or a set of sentences typed by you, and every verdict is recomputed exactly. The quickest way to see what a position commits you to is to make the case a little worse for it and watch where it gives way.",
        "Separate the arithmetic from the premise. The labs compute what follows from the welfare numbers, the forbidden acts or the sentences a lesson states. They do not say whether a number is the right measure of a life, whether an act belongs on the forbidden list, or whether a principle is true. Each lesson says where its own stipulation sits.",
        "Expect questions left open on purpose. A lesson shows an argument is valid and says what accepting its conclusion or rejecting a premise would cost. Choosing is yours.",
    ],
    "not_covered": [
        "Metaethics beyond is and ought and the open question. Expressivism, error theory and the arguments for moral realism are not here; none of them has a verdict a lab can compute without misrepresenting it. The Frege–Geach problem, which asks whether arguments with embedded moral terms stay valid, can be posed as a validity check, and is a candidate for a later lesson.",
        "Virtue ethics beyond the function argument. The doctrine of the mean, practical wisdom and moral education have no structure a lab can test, and the lesson on the function argument says so rather than invent one.",
        "Welfare itself. Every lab takes welfare as a number supplied by the example. How lives are measured, whether they can be compared between people, and what makes a life go well are open questions the numbers assume away.",
        "Applied ethics. No lesson tells you what to think about a particular policy, profession or practice. The cases are chosen because their structure is clear, not because they settle anything outside the course.",
        "The history of ethics as history. Arguments are taught as arguments; dates, schools and influence are not computable and are not here.",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every verdict on this course is computed in your browser from what the lesson states: a validity check from every row of a truth table, a ranking from exact sums and fractions, a recommendation from the acts left after a constraint, a causal verdict from re-evaluating the equations. Nothing is rounded except where a lesson says so. What the labs cannot do is tell you whether a welfare number measures a life, whether an act is rightly forbidden, or whether a premise is true &mdash; and those are the questions the arguments turn on."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
