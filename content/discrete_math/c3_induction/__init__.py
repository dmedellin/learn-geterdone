"""Course 3 — Induction and Recursion."""

from . import part_a, part_b

COURSE = {
    "slug": "induction-and-recursion",
    "title": "Induction and Recursion",
    "level": "Intermediate",
    "summary": (
        "The technique that proves a statement for every natural number by proving one "
        "implication: well-ordering, ordinary and strong induction, structural "
        "induction, recursive definitions and algorithms, linear and "
        "divide-and-conquer recurrences, and loop invariants."
    ),
    "blurb": (
        (
        'Checking cases is not proving, as Logic and Proof explains. Establish a base case and prove `P(k) → P(k+1)` once, and the claim holds for every natural number from that base onward, including those you could never check. The same idea applies to definitions, data, algorithms and recurrences.'
    )
    ),
    "key": [
        "P(base)   and   ∀k ≥ base. P(k) → P(k+1)      ⟹   ∀n ≥ base. P(n)",
        "strong:   P(base ..k)  →  P(k+1)",
        "aₙ = c₁aₙ₋₁ + c₂aₙ₋₂   ⟹  characteristic equation r² = c₁r + c₂",
        "T(n) = aT(n/b) + nᵈ    ⟹  compare log_b a with d",
    ],
    "assumes_short": "Proof and set notation",
    "assumes_long": "proof technique and set notation",
    "outcomes_intro": (
        (
        "Prove statements about natural numbers and recursive objects, solve recurrences, and "
        "prove algorithm correctness."
    )
    ),
    "outcomes": [
        ("Write a correct induction proof",
         "Base case, explicit inductive hypothesis, and a step that actually uses it "
         "&mdash; the three parts a proof is graded on, and the three it usually loses."),
        ("Choose ordinary or strong induction",
         "Recognise the claims where `P(k)` alone is not enough, and state the stronger "
         "hypothesis correctly rather than reaching for it by habit."),
        ("Define and reason about recursive objects",
         "Recursive definitions of sequences, sets and structures, and the structural "
         "induction that proves things about them."),
        ("Solve a recurrence",
         "Linear homogeneous by characteristic roots, nonhomogeneous by a particular "
         "solution, and divide-and-conquer by the master theorem."),
        ("Prove an algorithm correct",
         'Termination by a quantity that strictly decreases and is bounded below, and correctness by strong induction on the input for a recursion or by an invariant for a loop &mdash; the two obligations of “Recursive Algorithms and Correctness” and “Loop Invariants and Program Correctness”, neither of which is worth anything alone.'),
    ],
    "syllabus_intro": (
        'Induction, recursion and recurrences support the program-correctness arguments in “Loop Invariants and Program Correctness”.'
    ),
    "how_to": [
        "Write every proof out in full, including the sentence that says where the "
        "inductive hypothesis was used. A step that never invokes `P(k)` is not an "
        "induction proof, however true its conclusion.",
        "Spend real time in “The Well-Ordering Principle”'s lab. Two of its statements are false and survive dozens of checks; meeting them is the reason this course exists. “Mathematical Induction” and “Strong Induction” explain these failures; try to identify the false statements yourself before reading those explanations.",
        "Do the recurrence arithmetic by hand once per lesson before using the lab. "
        "The lab compares your closed form against the iteration, which is only useful "
        "if you produced a closed form to compare.",
    ],
    "not_covered": [
        "Transfinite induction and induction over ordinals. Everything here is "
        "induction over `ℕ` or over a well-founded recursive structure.",
        (
            'Generating functions as a recurrence-solving technique. The “Generating Functions” Lesson in Combinatorics and Counting introduces them for counting; using them to solve recurrences is not covered here.'
        ),
        'Formal verification tools. The “Loop Invariants and Program Correctness” Lesson writes loop invariants as mathematics, not as annotations a checker consumes.',
    ],
    "footer_lead": (
        "The induction lab on this course checks a statement for the values you select "
        "and reports whether they held. That is deliberately not a proof, and two of "
        "its statements are false after passing every check a careful reader would run "
        "&mdash; which is the point the whole course is built on."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
