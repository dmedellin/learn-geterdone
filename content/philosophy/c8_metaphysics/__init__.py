"""Course 8 -- Identity, Modality and Freedom.

Split across two lesson modules: part_a is modality (possible worlds, frames,
the modal fallacies, the ontological argument, Leibniz's law) and the first
identity-over-time lesson, part_b is the rest of identity over time, freedom,
and the problem of evil.
"""

from . import part_a, part_b

COURSE = {
    "slug": "identity-modality-and-freedom",
    "title": "Identity, Modality and Freedom",
    "level": "Advanced",
    "summary": (
        "Possible-worlds models of necessity and possibility, the axioms a frame "
        "validates, and the arguments that turn on them; the ship of Theseus, "
        "psychological continuity and fission; free will as a question about "
        "consistency, the consequence argument and Frankfurt cases; and the problem "
        "of evil as an inconsistent set."
    ),
    "blurb": (
        "Treat the oldest questions in metaphysics as questions about structure. "
        "Evaluate a claim of necessity at a world, find out which axioms a frame "
        "forces, decide where a modal argument goes wrong, and see what each "
        "position on identity, freedom and evil has to give up."
    ),
    "key": [
        "□p at w  ⟺  p at every world w can see",
        "T: reflexive    4: transitive",
        "□p ∧ □(p → q)  →  □q   on every frame",
        "□(p ∨ ¬p) does not give □p ∨ □¬p",
        "inconsistent: drop one, a model appears",
    ],
    "assumes_short": "Arguments and Validity; Science, Induction and Causation",
    "assumes_long": (
        "Arguments and Validity, for validity, consistency and the counterexample, "
        "and Science, Induction and Causation, for the causal models used in one lesson"
    ),
    "outcomes_intro": (
        "By the end you can say what a claim of necessity, identity or freedom "
        "commits you to, and name the premise to doubt when an argument for it fails."
    ),
    "outcomes": [
        ("Evaluate a modal claim",
         "Compute `□p` and `◇p` at a world from the worlds it can see, and say which "
         "frame property each of the axioms T, D, B, 4 and 5 corresponds to."),
        ("Locate a modal fallacy",
         "Find the scope shift in the fatalist's argument, the premise the "
         "ontological argument needs from the frame, and the substitution "
         "that fails inside a box."),
        ("Run an identity puzzle as a chain",
         "State the ship of Theseus as a tolerance chain, and read off what "
         "each treatment says; separate connectedness from continuity as a "
         "relation from its transitive closure."),
        ("Write a puzzle as an inconsistent set",
         "Formalise fission, the free-will triad and the problem of evil, find "
         "the smallest subset that cannot hold together, and name the position "
         "each deletion yields."),
        ("Evaluate an argument about freedom",
         "Show the transfer step of the consequence argument is valid on every "
         "frame, and test a Frankfurt case in a structural model."),
    ],
    "syllabus_intro": (
        "Modality comes first, because three of the later arguments use it; then "
        "identity over time, then freedom, and the last lesson applies the "
        "inconsistent-set method to evil."
    ),
    "how_to": [
        "Work forward through the first five lessons. “Frames, Axioms and What "
        "Necessity Obeys” needs the evaluation rule from “Necessity, Possibility and "
        "Possible Worlds”, and “The Ontological Argument in S5” and “The Consequence "
        "Argument” both use the frame properties the second lesson establishes.",
        "Build the model before you read the verdict. Every modal lab lets you "
        "retype the arcs and the valuation. Predict the tile, then press on the "
        "model until the prediction fails; the arcs are the whole content of the "
        "theory, and a change of one arc often changes the axiom list.",
        "Keep the logic apart from the metaphysics. The labs decide whether an "
        "argument is valid on a frame, whether a set can all be true, whether "
        "a variable is a cause. They never decide whether the frame is the right "
        "one for God, for time, or for what is in anyone's power. That question "
        "is left open on purpose in every lesson.",
        "Take each puzzle to the end. The identity and freedom lessons each name "
        "an exit for every position, and a position whose exit you cannot state "
        "is a position you have only heard of.",
    ],
    "not_covered": [
        "Quantified modal logic and counterpart theory. Every model here has "
        "worlds, an accessibility relation and sentence letters, and no domain of "
        "individuals that varies from world to world, so questions such as whether "
        "I could have been a different person are left to the prose.",
        "Temporal logic. The sea battle is treated as a scope error with the box, "
        "not with a logic of past and future, so what the lab shows is the "
        "fallacy and not a theory of time.",
        "Bodily and narrative criteria of personal identity. They appear as "
        "prose beside the psychological criterion, and nothing computes whether "
        "a body or a story is the same one.",
        "Philosophy of religion beyond the two arguments taught. The "
        "ontological argument and the problem of evil are tested for validity and "
        "consistency; the cosmological argument, religious experience and "
        "the rest are not here.",
        "Neuroscience and the experimental literature on free will. The "
        "lessons test whether positions are consistent and whether arguments are "
        "valid. Whether determinism is true is an empirical question and "
        "is not decided here.",
    ],
    "footer_lead": (
        "Every verdict in this course is computed in your browser from the model, "
        "chain, set of sentences or causal equations the lesson states: a box is "
        "true at a world because every visible world agrees, a set is inconsistent "
        "because no row satisfies it. A lab cannot tell you that a frame is the "
        "right one for God or for time, that a sentence is true, or that the "
        "intervener in a Frankfurt case is described fairly, and those are the "
        "questions the arguments turn on."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
