"""Course 5 -- Persons and the Generation of a Commonwealth: Chapters 16 to 19.

part_a is Chapters 16 and 17 (persons, the multitude made one, the generation of
a commonwealth); part_b is Chapter 18 (the rights of sovereigns) and Chapter 19
(the kinds of commonwealth and the right of succession).
"""

from . import part_a, part_b

_ALL = part_a.LESSONS + part_b.LESSONS


COURSE = {
    "slug": "leviathan-generation-of-commonwealth",
    "title": "Persons and the Generation of a Commonwealth",
    "level": "Introductory",
    "summary": (
        "Chapters 16 to 19 of Leviathan. What a person, an author and an actor are, how a "
        "multitude becomes one person and how an assembly's voices are counted, why a "
        "covenant needs a sword and what the covenant of every man with every man "
        "makes, the twelve rights of the sovereign and the argument that he cannot "
        "forfeit them, the three kinds of commonwealth, and who succeeds a monarch."
    ),
    "blurb": (
        "Read the chapters in which Hobbes builds the commonwealth, with the arguments "
        "beside you. Check who is bound by what an agent signs, count an assembly's "
        "voices, find the penalty that turns a peace of ten people from words into a "
        "fact, test the argument that the sovereign cannot breach a covenant, and "
        "work out who inherits a throne."
    ),
    "key": [
        "author is bound within the commission",
        "assembly: voice of the greater number",
        "even split chance = C(n, n/2) / 2^n",
        "covenants without the sword are but words",
        "no covenant by the sovereign, no forfeiture",
        "succession: testament, custom, presumption",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no philosophy or political theory is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can say what each argument of these four chapters needs, "
        "and check it on a case of your own."
    ),
    "outcomes": [
        ("Say who is bound by an agent's covenant",
         "Given an actor, an author and a commission, say who is bound by a covenant, "
         "and which condition of the argument a case fails."),
        ("Count an assembly's voice",
         "Say what a set of voices decides, when an assembly is mute, and how often an "
         "assembly of a stated size splits evenly on a stated model."),
        ("Show why a peace needs a power",
         "Write a peace among many people as a payoff table, find the equilibrium "
         "without a sovereign, and find the smallest penalty at which keeping it pays."),
        ("Test the argument against forfeiture",
         "Set out Hobbes's argument that the sovereign cannot breach a covenant he did "
         "not make, show that it is valid, and name the premise a critic denies."),
        ("Tell whether an assembly has a stable will",
         "From rankings of three proposals, find whether any beats both others, and "
         "show how the order of voting can decide the winner."),
        ("Name the successor",
         "Given a family, a testament and a custom, name the successor on Hobbes's "
         "order and the rule that chose him."),
    ],
    "syllabus_intro": (
        "Two lessons take Chapter 16 from the author to the assembly, one takes "
        "Chapter 17, one takes Chapter 18 and two take the two halves of Chapter 19."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's words "
        "and then goes back through them a phrase at a time. Quotations are from "
        "Hobbes's text of 1651, in its original spelling, and the examples that follow "
        "them are written for these lessons.",
        "Chapters 16 and 17 are short and carry a great deal. The word person, the "
        "difference between an author and an actor, and the covenant of every man with "
        "every man are the machinery of everything that follows, so it is worth "
        "reading Chapter 16 slowly.",
        "Use the labs to change one thing at a time. A premise, a voice, a penalty "
        "or a testament is the one thing that moves between presets, and the point "
        "is in what the figure does when it moves.",
        "Keep the computation apart from the verdict. Every figure is computed from "
        "what a lesson states, on Hobbes's definitions as written. Whether men are as "
        "he says, and whether a commonwealth can stand on his covenant, is what "
        "the book argues, and each lesson says where its critics stand.",
    ],
    "not_covered": [
        "Commonwealth by acquisition. Chapter 17 ends by distinguishing a commonwealth "
        "by institution from one by acquisition by force, and Chapter 20 takes "
        "the second; this course takes institution only, and the next course "
        "begins with Chapter 20.",
        "The rest of Chapter 18's argument about the sovereign's powers. The twelve "
        "rights are listed, and one is worked; the powers of doctrine, property, "
        "judicature and honour are taken up where the book returns to them in Part "
        "II and again in Parts III and IV.",
        "Hobbes's remarks on the persons of God, of idols and of inanimate things. "
        "Chapter 16 says what may be personated, and the lesson reports it briefly; "
        "the religious argument is the subject of Part III.",
        "Later theories of voting and representation. Condorcet's cycle appears "
        "once, plainly marked as a later finding, and no history of the theory of "
        "representation or of social choice is attempted.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the names, "
        "payoffs and numbers a lesson states, and shows what follows from them on "
        "Hobbes's definitions. The examples are written for these lessons, and no "
        "lab can tell you whether his definitions describe men and commonwealths."
    ),
    "lessons": _ALL,
}
