"""Course 9 -- Mind, Language and Meaning.

Split across two lesson modules: part_a is the philosophy of mind where it can
be checked (dualism, behaviourism, functionalism, the Chinese room and the
knowledge argument), part_b is language (truth conditions, names, descriptions,
scope and vagueness).
"""

from . import part_a, part_b

COURSE = {
    "slug": "mind-language-and-meaning",
    "title": "Mind, Language and Meaning",
    "level": "Advanced",
    "summary": (
        "The philosophy of mind where it can be checked, and the philosophy of "
        "language where it can be computed: conceivability in a possible-worlds "
        "model, the Turing test as a Bayes factor, functionalism as one table "
        "with many circuits, the Chinese room as a counted table and the "
        "knowledge argument as a valid form; then truth conditions in a finite "
        "model, names, Russell's descriptions, scope and vagueness."
    ),
    "blurb": (
        "Test the arguments that mind and language are made of. Evaluate a "
        "necessity claim with and without the world it needs, compute what a "
        "mimic does to a judge, count a lookup table, and then read a sentence "
        "in a model, find the scope it hides, and run the heap under four "
        "treatments of vagueness."
    ),
    "key": [
        "□(p ↔ c): p ↔ c at every world in view",
        "a perfect mimic: Bayes factor 1",
        "a lookup table: nʳ entries",
        "valid + denied premise: a reply",
        "sentence + model  →  True or False",
        "the F is G  =  one F, and it is G",
        "¬ before or after the F: two readings",
        "each step true, the end false: sorites",
    ],
    "assumes_short": "Identity, Modality and Freedom",
    "assumes_long": (
        "Identity, Modality and Freedom, whose possible-worlds models are used "
        "from the first lesson, and through it Arguments and Validity, Knowledge "
        "and Evidence for updating on evidence"
    ),
    "outcomes_intro": (
        "By the end you can state a position in the philosophy of mind or of "
        "language as something with a checkable structure, and say which premise "
        "or which model carries it."
    ),
    "outcomes": [
        ("Evaluate a conceivability argument",
         "Build the model with and without the world the argument needs, "
         "evaluate the necessity claim in each, and name the step from "
         "conceivable to possible as the choice to include that world."),
        ("Compute what a test shows",
         "Treat a judge as an updater, compute the Bayes factor of an answer, "
         "and say what a pass and a failure of the Turing test do and do not "
         "establish."),
        ("Compare a table with a program",
         "Show two circuits with one function, count the entries a lookup "
         "table needs for a conversation, and state what Block and Searle each "
         "infer from their devices."),
        ("Place a reply to an argument",
         "Formalise the knowledge argument, show it valid, and say which "
         "premise or which atom each reply denies or splits."),
        ("Evaluate a sentence in a model",
         "Read a first-order sentence in a finite model, give the witness or "
         "the counterexample, and separate what a name refers to from what it "
         "means."),
        ("Resolve an ambiguity and run a sorites",
         "Expand a description in Russell's way, give both scopes of a "
         "negation or a pair of quantifiers, and run the heap argument under "
         "each treatment of vagueness, saying what each gives up."),
    ],
    "syllabus_intro": (
        "Five lessons on mind, each with a lab that computes the structure of an "
        "argument, then five on language, each with a lab that computes the "
        "value of a sentence."
    ),
    "how_to": [
        "Know what each lesson leans on. “Dualism and the Conceivability "
        "Argument” uses the possible-worlds models of Identity, Modality and "
        "Freedom, and the language lessons build on “Compositional Truth "
        "Conditions”, on which the three after it depend.",
        "Change the model and watch the verdict. In each lab the premises, "
        "worlds, likelihoods or extensions are text you can edit. The most "
        "useful minute in a lesson is the one in which you try to break its "
        "example.",
        "Keep the two questions apart. A lab here tells you what follows from "
        "the model you built, whether a world, a table or a domain. It does not "
        "tell you whether the model is right, and in this course that is "
        "usually where the philosophy is.",
        "Say the position at its strongest before you reply to it. Each lesson "
        "gives both sides a valid argument. The reply is a premise to deny or a "
        "reading to prefer, and you should be able to say which.",
    ],
    "not_covered": [
        "Theories of consciousness and the hard problem as a whole. The "
        "conceivability and knowledge arguments are taught as arguments with a "
        "checkable form. Neuroscientific theories of consciousness, "
        "eliminativism and panpsychism have no table to check them against, and "
        "are left out.",
        "Phenomenology and the history of the subject. Nothing here is about "
        "what a philosopher said or which school held what. Several lessons are "
        "about an argument a philosopher made, taught as the argument.",
        "Validity in full first-order logic. A sentence is evaluated in the "
        "finite model you build, so the lab computes truth in that model and "
        "does not search every possible model for a countermodel. Quantified "
        "modal logic and counterpart theory are not taught.",
        "Pragmatics, speech acts and the causal theory of reference. Names, "
        "descriptions and scope are taught through what a model can compute. "
        "What speakers mean by an utterance, and how a name gets attached to "
        "its bearer, are not of a shape a lab can test without misrepresenting "
        "them.",
        "Continuous and probabilistic theories of vagueness. The heap is run "
        "under four treatments, one of which uses degrees of truth, in exact "
        "arithmetic over a finite chain. Supervaluation proper and the "
        "epistemic view beyond what the lesson says of it are not developed.",
    ],
    "footer_lead": (
        "Every verdict in this course is computed in your browser from the "
        "model, the table or the likelihoods the lesson states. A lab can show "
        "that an argument is valid and that a sentence is true in a model; it "
        "cannot show that a world is possible, that a model is the right one, or "
        "that a premise is true. Those are the questions the arguments turn on."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
