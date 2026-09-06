"""Course 1 — Logic and Proof.

Split across two lesson modules because fourteen lessons in one file is a file
nobody reviews. part_a is propositional logic, part_b is quantifiers and proof.
"""

from . import part_a, part_b

COURSE = {
    "slug": "logic-and-proof",
    "title": "Logic and Proof",
    "level": "Beginner",
    "summary": (
        (
        "Propositional and predicate logic from truth values to written proofs: connectives, "
        "truth tables, equivalence, normal forms, quantifiers and their negations, inference "
        "rules, and direct, contrapositive, contradiction, and case proofs."
    )
    ),
    "blurb": (
        (
        "Translate statements into propositional and predicate logic, test equivalence, "
        "negate quantified claims, check inferences, and write proofs that another reader can "
        "verify."
    )
    ),
    "key": [
        "p → q   ≡   ¬p ∨ q            the conditional, in disjunctive form",
        "¬(p ∧ q)  ≡  ¬p ∨ ¬q          De Morgan",
        "¬∀x P(x)  ≡  ∃x ¬P(x)         negation flips the quantifier",
        "p → q   ≡   ¬q → ¬p           contraposition: the basis of a proof method",
    ],
    "assumes_short": "School algebra",
    "assumes_long": "school algebra is enough",
    "outcomes_intro": (
        "By the end you can read a theorem statement exactly as written, and write a "
        "proof someone else can check."
    ),
    "outcomes": [
        ("Read a formula unambiguously",
         "Parse a compound statement, apply precedence correctly, and build its truth "
         "table without guessing at what `→` means when its hypothesis is false."),
        ("Prove two statements equivalent",
         "Either by a full truth table, or by a chain of named equivalences &mdash; and "
         "know that one separating assignment refutes the claim outright."),
        ("Handle quantifiers with care",
         "Distinguish `∀x ∃y` from `∃x ∀y`, negate a quantified statement mechanically, "
         "and recognise the vacuous truth that catches everyone once."),
        ("Write the four standard proofs",
         "Direct, contrapositive, contradiction and cases &mdash; knowing which shape of "
         "claim invites which technique, and what each one owes the reader."),
    ],
    "syllabus_intro": (
        "Lessons 1 to 7 are propositional logic, 8 to 10 add quantifiers, and 11 to 14 "
        "turn all of it into proofs."
    ),
    "how_to": [
        (
            "Use truth tables to check equivalences, and distinguish an implication from its "
            "contrapositive."
        ),
        (
            "Try your own formulas and predicates in the labs. Look for an assignment that "
            "makes a proposed equivalence false."
        ),
        (
            "Write the practice proofs out. Reading an argument and producing one exercise "
            "different skills."
        ),
        (
            "The continuity and convergence examples practise reading and negating "
            "quantifiers; they do not require calculus."
        )
    ],
    "not_covered": [
        "Formal proof systems. This course teaches proof as mathematicians write it "
        "&mdash; rigorous prose &mdash; not natural deduction trees, sequent calculus, or "
        "a machine-checkable proof assistant.",
        "Completeness and soundness of first-order logic, model theory, and G&ouml;del's "
        "incompleteness theorems. Those are the subject of a logic course; this is the "
        "logic a discrete mathematics course needs.",
        "Fuzzy, modal and intuitionistic logics. Everything here is classical and "
        "two-valued: every proposition is either true or false, and `p ∨ ¬p` always holds.",
    ],
    "footer_lead": (
        (
        "Truth tables, equivalences and quantifier evaluations are computed in your browser "
        "under every assignment. Checking finitely many cases does not prove a claim over an "
        "infinite domain."
    )
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
