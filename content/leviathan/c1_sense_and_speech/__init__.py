"""Course 1 -- Sense, Imagination and Speech: the Epistle, the Introduction and Chapters 1-4.

Five lessons in part_a: the Introduction, Chapters 1 and 2 together, Chapter 3,
and Chapter 4 in two halves. Quotations are from Hobbes's text of 1651.
"""

from . import part_a

COURSE = {
    "slug": "leviathan-sense-and-speech",
    "title": "Sense, Imagination and Speech",
    "level": "Beginner",
    "summary": (
        "The Epistle Dedicatory, the Introduction and Chapters 1 to 4 of Part I, Of Man. "
        "What the commonwealth is and how the book means to be checked; what sense, "
        "imagination, memory and dreams are on Hobbes's account; how thoughts follow one "
        "another and what prudence is; and what speech, names, truth and definitions are."
    ),
    "blurb": (
        "Read the opening of Leviathan slowly, with something to check beside every "
        "argument. Set out Hobbes's rule that you can read others by reading yourself, "
        "and his argument from the echo, as premises and look for the bridge; update a "
        "prudent man's presumption on what he has seen; and reckon with names."
    ),
    "key": [
        "commonwealth = an artificial man",
        "sense: pressure on an organ, seen as fancy",
        "imagination = decaying sense",
        "prudence = presumption from experience",
        "A is B: every part of B is a part of A",
        "absurd names cannot be added",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no philosophy and no earlier course is assumed, and the reading is in modern spelling around Hobbes's own",
    "outcomes_intro": (
        "By the end you can say what the first four chapters argue and check one "
        "argument from each of the three kinds of lab."
    ),
    "outcomes": [
        ("Say what the artificial man is",
         "State what Hobbes means by calling the commonwealth an artificial man, list "
         "the correspondence of its parts, and give the order of the four Parts of the "
         "book."),
        ("Set out an argument and find its bridge",
         "Put the rule that reading oneself reads others, and the argument from the "
         "echo, as premises and a conclusion, find the counterexample row when one "
         "exists, and name the premise that would close it or that a critic would deny."),
        ("Say what sense and imagination are",
         "Give Hobbes's account of sense as the seeming caused by pressure, "
         "imagination as decaying sense, memory as the same thing under another name "
         "and dreams as imagination in sleep."),
        ("Update a presumption",
         "Compute what a run of observations does to a presumption on a stated "
         "model, and say why prudence stays short of certainty."),
        ("Reckon with names",
         "Expand defined names into simple ones, test an affirmation as true or false by "
         "the parts, and tell an absurd or insignificant affirmation from a false one."),
    ],
    "syllabus_intro": (
        "The first lesson reads the Epistle and the Introduction, the second reads "
        "Chapters 1 and 2, the third reads Chapter 3, and the last two take Chapter 4 in "
        "halves, speech and names first and then truth and definitions."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's own "
        "words and then goes through them a phrase at a time. Quotations are from "
        "Hobbes's text of 1651, in its original spelling, so expect &ldquo;Common-wealth&rdquo; "
        "and &ldquo;warre&rdquo;; the explanations around them are in modern spelling. "
        "The examples and the figures are written for these lessons.",
        "Use the labs to change one thing at a time. Each preset is a single change "
        "against the one before it, a premise added, a hanging observed, a definition "
        "altered, and the point of the lesson is in what moves and what does not.",
        "Keep the computation apart from the verdict. Each lab shows what follows "
        "from what the lesson states, on Hobbes's definitions as written. Whether "
        "men and commonwealths are as Hobbes describes them is what the book "
        "argues, and each lesson says where its critics stand.",
    ],
    "not_covered": [
        "The natural philosophy behind Chapters 1 and 2. Hobbes says himself that the "
        "natural cause of sense is not very necessary to the business in hand, and "
        "the lessons take his account as stated and do not test it against optics or "
        "physiology.",
        "The wider history of the problem of universals. Chapter 4 takes a side in "
        "an argument the schools had carried on for centuries, and the lessons say "
        "so in a sentence without going into the medieval positions.",
        "Hobbes's other writings. The Elements of Law, De Cive and the Objections to "
        "Descartes are not read, and the lessons do not say what they argue.",
        "The Latin Leviathan of 1668 and the editor's apparatus. Only Hobbes's text of "
        "1651 is read, and only its own marginal headings are quoted.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the premises, "
        "observations and definitions a lesson states, and shows what follows from them "
        "on Hobbes's definitions. Quotations are from Hobbes's text of 1651. No lab "
        "can tell you whether the passions are alike in all men, whether sense is a "
        "motion, or whether names are all there is to reasoning."
    ),

    "lessons": part_a.LESSONS,
}
