"""Course 3 -- Science, Induction and Causation.

Split across two lesson modules. part_a is induction and confirmation up to the
raven paradox; part_b is the Duhem-Quine problem, Mill's methods and causation.
"""

from . import part_a, part_b

COURSE = {
    "slug": "science-induction-and-causation",
    "title": "Science, Induction and Causation",
    "level": "Intermediate",
    "summary": (
        "How evidence bears on a theory and how a cause differs from a correlation: induction as updating under a prior, grue, confirmation as a Bayes factor, falsification as a likelihood of zero, the ravens, the Duhem–Quine problem, Mill's methods, Simpson's paradox, and causation as a counterfactual in a structural model."
    ),
    "blurb": (
        "Hume said the future cannot be deduced from the past; here is exactly what must be added, and what it costs. Weigh evidence by a Bayes factor, see what a theory forbids, find what a failed test refutes, search a table of cases for a cause, watch a pooled rate reverse, and test a cause by flipping it in a model."
    ),
    "key": [
        "BF = P(E | H) / P(E | ¬H)   weight of E",
        "P(E | H) = 0 and E seen: H is refuted",
        "grue and green: same rows, BF = 1",
        "a failed test refutes the whole set",
        "pooled rates can reverse every group's",
        "cause: flip C and E flips, others held",
    ],
    "assumes_short": "Knowledge and Evidence",
    "assumes_long": (
        "Knowledge and Evidence, which teaches credence and updating by Bayes' rule, and through it Arguments "
        "and Validity, whose truth tables and consistency test return here; nothing beyond fractions"
    ),
    "outcomes_intro": (
        "By the end you can take a claim about evidence or about a cause, put it in a form that can be computed, "
        "and say which assumption the answer rests on."
    ),
    "outcomes": [
        ("Compute what a run of observations licenses",
         "Given a prior over hypotheses and a run of data, compute the exact probability of the next "
         "observation, and name the premise the prior supplies that no number of observations can."),
        ("Measure the weight of evidence",
         "Compute a Bayes factor, classify evidence as confirming, disconfirming or neutral, and explain "
         "why a surprising result weighs more than an expected one."),
        ("Locate what a failed prediction refutes",
         "Write a prediction as a set of claims that cannot all be true, find its smallest inconsistent "
         "subset, and say why the observation refutes the set and not one member of it."),
        ("Search a case table for a cause",
         "Apply the methods of agreement and difference to a table of cases, list every formula that fits, "
         "and say what the table cannot rule out."),
        ("Detect and explain a reversal",
         "Compute rates within groups and pooled, decide whether they reverse, and name the variable that "
         "explains the reversal."),
        ("Test a cause by flipping it",
         "Write a situation as Boolean equations, compute the actual values, and decide by recomputation "
         "whether a variable is a but-for cause, a cause once something is held fixed, or neither."),
    ],
    "syllabus_intro": (
        "Induction comes first because every later lesson needs its answer, confirmation comes second "
        "because it measures evidence, and causation comes last because it asks what evidence is evidence of."
    ),
    "how_to": [
        "Read the first two lessons together. “Enumerative Induction and Hume's Problem” shows what a prior "
        "supplies, and “Grue and the New Riddle” shows that the supply cannot come from the data. The "
        "confirmation lessons then treat the prior as given and ask only what the evidence adds.",
        "Change the prior and the likelihoods, not only the data. Almost every figure in the confirmation "
        "lessons is a ratio of two likelihoods, and the quickest way to see which one matters is to move it "
        "and watch the Bayes factor follow.",
        "Expect the causal lessons to be exact rather than intuitive. The structural models are small Boolean "
        "equations written out in full, and a verdict such as “a cause once something is held fixed” is the "
        "result of a recomputation you can repeat by hand in a minute.",
        "Keep Knowledge and Evidence to hand. “Updating on Evidence” is the one procedure used in every "
        "lesson of the first half, and nothing here re-derives it.",
    ],
    "not_covered": [
        "Statistical inference. Significance tests, confidence intervals and regression estimate a quantity "
        "from data; nothing here is estimated. Simpson's paradox is computed from counts, and every update "
        "runs over a handful of hypotheses stated in full.",
        "Continuous priors. The rule of succession appears as its five-point discretisation and says so. No "
        "densities, no integrals, and the lab will not tell you what the answer would be over a continuum.",
        "Causal inference from data, including the do-calculus and the question of when a cause is "
        "identifiable. The structural models here are Boolean and given; the labs do not learn them.",
        "The history and sociology of science. Paradigms, revolutions and the question of how scientists "
        "actually choose between theories are real subjects, but they are not of a shape a lab can compute "
        "without misrepresenting them. The Duhem–Quine lesson takes one episode as an example of "
        "the logic and says no more about the history.",
    ],
    "footer_lead": (
        "Every posterior and Bayes factor on this course is an exact fraction computed in your browser from the "
        "prior and likelihoods the lesson states, and every causal verdict is found by recomputing a "
        "model after one change. What the labs cannot do is tell you whether a prior is reasonable, whether a "
        "likelihood describes the world, or whether a model has left out a variable that matters &mdash; "
        "and those are the questions the arguments in these lessons turn on."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
