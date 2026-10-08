"""Course 1 -- Arguments and Validity.

Split across two lesson modules: part_a is what an argument is and propositional
logic up to equivalence, part_b is consistency, categorical logic, quantifiers
and the fallacies.
"""

from . import part_a, part_b

COURSE = {
    "slug": "arguments-and-validity",
    "title": "Arguments and Validity",
    "level": "Beginner",
    "summary": (
        "What an argument is and what it is for a conclusion to follow: premises in "
        "standard form, validity against soundness, truth tables, equivalence, "
        "consistency, categorical syllogisms on Venn regions, quantifiers and the "
        "counterexample method."
    ),
    "blurb": (
        "Tell a valid argument from a persuasive one. Set out a passage as premises "
        "and a conclusion, test it by looking for a counterexample row, decide whether "
        "a set of beliefs can all be true, and refute a bad form with a better case."
    ),
    "key": [
        "valid ⟺ no row: premises T, conclusion F",
        "¬(p ∧ q)  ≡  ¬p ∨ ¬q    De Morgan",
        "p → q  ≡  ¬q → ¬p       contrapositive",
        "inconsistent: no row makes all true",
        "∀x ∃y is not ∃y ∀x      order matters",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no logic is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can say what an argument claims, test whether its conclusion "
        "follows, and say what rejecting that conclusion commits you to giving up."
    ),
    "outcomes": [
        ("Set out an argument",
         "Rewrite a passage as numbered premises and one conclusion, strike the "
         "sentences that do no work, and say what the rest are offered in support of."),
        ("Test validity by counterexample",
         "Build the table, find or rule out a row with true premises and a false "
         "conclusion, and keep validity apart from soundness."),
        ("Rewrite without changing the claim",
         "Decide equivalence by comparing columns, negate with De Morgan, and give "
         "a conditional's contrapositive without its converse."),
        ("Test a set of beliefs",
         "Decide whether sentences can all be true, and find the smallest subset "
         "that cannot."),
        ("Test categorical arguments",
         "Read All, No and Some as claims about regions, test a syllogism, and "
         "state what changes when existential import is assumed."),
        ("Read quantifier order, and refute a fallacy",
         "Read quantifiers over a finite universe in the right order, and answer "
         "an invalid form with an argument of the same form that has true premises "
         "and a false conclusion."),
    ],
    "syllabus_intro": (
        "An argument is set out first, then tested by tables, then by regions, then "
        "with quantifiers, and the last lesson turns the test into a method of refutation."
    ),
    "how_to": [
        "Work forward. “Validity by Truth Table” assumes you can fill the table of a "
        "conditional, and “Consistency and Belief Sets” assumes you can test an "
        "argument by table. The second half uses the first throughout.",
        "Use the labs to look for the row. Almost every lab here lists the cases and "
        "marks the ones that matter. Edit a premise and watch the verdict move; "
        "a minute spent trying to break an argument teaches more than reading its "
        "verdict.",
        "Keep two questions apart. Every lab in this course decides whether a "
        "conclusion follows from premises. None decides whether the premises are "
        "true, and “Validity and Soundness” is where that line is drawn. The rest "
        "of the Subject asks that second question.",
        "Say each verdict in words. After the lab reports a counterexample, state "
        "in a sentence the case it describes. If you cannot, you have a result and "
        "not yet an understanding.",
    ],
    "not_covered": [
        "Proofs and derivations. Validity here is decided by truth table and by "
        "countermodel, never by deriving a conclusion step by step. Logic and Proof "
        "on the Discrete Mathematics path teaches proof technique.",
        "Validity in full first-order logic. Quantified sentences are read over a "
        "finite universe you build, so the lab computes truth in that universe and "
        "does not search every possible one for a countermodel.",
        "Informal fallacies and rhetoric. Ad hominem, straw men and the like are "
        "failures of relevance and fairness, and there is no table to check them "
        "against. They are left to the reader's judgement.",
        "The history of logic. The syllogism is taught as a way of testing "
        "arguments, not as Aristotle's own system, and nothing here is about who "
        "said what.",
    ],
    "footer_lead": (
        "Every verdict in this course is computed in your browser by listing the "
        "cases and checking each one, so a counterexample is a row you can read. "
        "Showing that an argument is valid is not showing that its conclusion is "
        "true: that needs the premises to be true, and no lab checks that."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
