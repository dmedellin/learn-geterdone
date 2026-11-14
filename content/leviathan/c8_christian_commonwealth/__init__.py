"""Course 8 -- Of a Christian Commonwealth: Part III, Chapters 32-43.

Eight lessons: part_a is Chapters 32 to 36 (principles, Scripture, spirit,
the kingdom and the word of God); part_b is Chapters 37 to 43 (miracles, the
church, the sovereigns of Israel and Christ, ecclesiastical power).
Quotations are from Hobbes's text of 1651.
"""

from . import part_a, part_b

COURSE = {
    "slug": "leviathan-christian-commonwealth",
    "title": "Of a Christian Commonwealth",
    "level": "Introductory",
    "summary": (
        "Part III, Of a Christian Commonwealth, Chapters 32 to 43. How Hobbes reasons "
        "from Scripture: the two marks of a true prophet, the books of the canon and "
        "who made them law, what spirit, angel and inspiration mean, what a miracle is "
        "and how much it proves, the church as a commonwealth, the sovereigns of Israel "
        "and the offices of Christ, and what a Christian must do to be saved."
    ),
    "blurb": (
        "Read Hobbes's use of the Bible as an argument, with something to check beside "
        "each step. Test his two marks of a prophet as a conjunction, date a book by "
        "what it mentions, reckon on his definition of spirit, update a chance that a "
        "prophet or a wonder is genuine, and check the valid forms behind his claim "
        "that obeying the sovereign never costs a Christian his salvation."
    ),
    "key": [
        "true prophet: miracle AND the old religion",
        "a book is no older than what it mentions",
        "incorporeal substance cannot be added",
        "chance true = prior x likelihood / total",
        "a church = Christians united in a sovereign",
        "salvation: faith in Christ, obedience to law",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no theology and no earlier course is assumed; the Bible passages are quoted where Hobbes argues from them",
    "outcomes_intro": (
        "By the end you can follow Hobbes's arguments from Scripture, say what each "
        "rests on, and check one of each kind with a lab."
    ),
    "outcomes": [
        ("State the two marks of a prophet",
         "Say what Hobbes requires of a man who claims to speak for God, test a "
         "candidate against both marks together, and say why one mark alone fails on "
         "his text."),
        ("Date a book from its contents",
         "Find the latest event a book mentions, say whether it was written after its "
         "traditional author died, and say what the test does not show."),
        ("Reckon with the words of the Schools",
         "Expand spirit, angel and substance by Hobbes's definitions, and tell an "
         "absurd affirmation from a false or an empty one."),
        ("Update the chance that a prophet is true",
         "Compute the chance that a prophet is genuine after a fulfilled prophecy, "
         "from a stated base rate and stated likelihoods."),
        ("Weigh a reported miracle",
         "Compute what witnesses do to the chances of miracle, trick and mistake, and "
         "say what Hobbes leaves to the lawful church."),
        ("Apply Hobbes's definition of a church",
         "Test a gathering against the definition, and say which cases it admits and "
         "which it shuts out."),
        ("Check the argument from Moses",
         "Put the argument that Moses ruled by the people's covenant as premises and "
         "a conclusion, check that it is valid, and name the premise that carries it."),
        ("Check the argument from salvation",
         "Set out the argument that a Christian need never disobey his sovereign to be "
         "saved, check its form, and name the premise a Covenanter would deny."),
    ],
    "syllabus_intro": (
        "The first four lessons read Chapters 32 to 36, the principles, the books, the "
        "words and the prophets. The last four read Chapters 37 to 43, from miracles "
        "through the church and the sovereigns of Israel to power ecclesiastical and "
        "the one article necessary to salvation."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's own "
        "words and then goes through them a phrase at a time. Quotations are from "
        "Hobbes's text of 1651, in its original spelling, so expect &ldquo;Common-wealth&rdquo; "
        "and &ldquo;Soveraign&rdquo;; the explanations around them are in modern spelling. "
        "This course is a read-along of Thomas Hobbes, Leviathan (1651), and the "
        "examples and the figures are written for these lessons.",
        "Take Hobbes's Scripture arguments as arguments. He quotes the Bible at great "
        "length, and his readings were disputed in his own time. The lessons set out "
        "what he argues and what he rests it on, and say where his critics stood, "
        "without defending his theology or mocking it.",
        "Use the labs to change one thing at a time. Each preset is a single change "
        "against the one before it, a premise dropped, a witness added, a definition "
        "altered, and the point of the lesson is in what moves and what does not.",
        "Keep the computation apart from the verdict. Each lab shows what follows "
        "from what the lesson states, on Hobbes's definitions as written. Whether "
        "men, prophets and churches are as Hobbes describes them is what the book "
        "argues about.",
    ],
    "not_covered": [
        "The theology. The lessons do not say whether Hobbes's reading of a verse is "
        "right, only what he argues from it and what his argument needs.",
        "The Biblical scholarship since 1651. The dating of the books is Hobbes's "
        "argument from the text; modern criticism is not surveyed, and the lab's years "
        "are round figures for the exercise.",
        "The long answer to Cardinal Bellarmine. Chapter 42 is read for its argument "
        "that ecclesiastical power teaches and does not command, and for the cases "
        "Hobbes lists, not for the whole controversy with Rome.",
        "The Kingdom of Darkness. Chapters 44 to 47 are the next course, and Part IV "
        "is read there.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the premises, "
        "chances, dates and definitions a lesson states, and shows what follows from "
        "them on Hobbes's definitions. Quotations are from Hobbes's text of 1651. No "
        "lab can tell you whether Scripture is true, whether a miracle happened, or "
        "whether Hobbes read it rightly."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
