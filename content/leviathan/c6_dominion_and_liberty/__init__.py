"""Course 6 -- Dominion, Liberty and the Parts of a Commonwealth: Chapters 20-23.

Four lessons in part_a, all on levkit (docs/leviathan/PLAN.md section C).
"""

from . import part_a

COURSE = {
    "slug": "leviathan-dominion-and-liberty",
    "title": "Dominion, Liberty and the Parts of a Commonwealth",
    "level": "Intermediate",
    "summary": (
        "Chapters 20 to 23 of Leviathan. A commonwealth made by conquest has the "
        "rights of one made by agreement, a child's obedience and a servant's rest on "
        "consent, a subject's liberty lies where the law is silent and in what no "
        "covenant can give away, and the groups and officers inside a commonwealth "
        "are limited by the letters that made them."
    ),
    "blurb": (
        "Read Hobbes on what a victory does and does not give, what liberty is, "
        "what a subject may refuse, and who pays when an assembly borrows. Test a "
        "vanquished man's covenant, sort actions under a set of laws, and name the "
        "members answerable for a vote."
    ),
    "key": [
        "dominion rests on consent, not on victory",
        "keep = gain − cost; break = gain − odds·fine",
        "free = neither commanded nor forbidden",
        "no covenant gives up defence of one's body",
        "answerable = those who voted yes",
    ],
    "assumes_short": "The two courses before it",
    "assumes_long": "the covenants and persons of The Natural Condition and the Laws of Nature and Persons and the Generation of a Commonwealth; Chapter 14's void covenants and Chapter 16's authors and actors come back here",
    "outcomes_intro": (
        "By the end you can state what Hobbes argues in Chapters 20 to 23 and work "
        "each argument as a short calculation on figures a lesson gives."
    ),
    "outcomes": [
        ("Say what gives a conqueror his right",
         "State that on Hobbes's account the vanquished man's covenant, not the victory, "
         "binds him, and compute whether keeping that covenant pays at a stated penalty "
         "and chance."),
        ("Place a parent's dominion",
         "Say whose dominion a child falls under in the state of nature with and without "
         "a contract, and why Hobbes rejects begetting as the ground."),
        ("Find a subject's liberty",
         "Given a list of actions and the laws in force, sort them into commanded, "
         "forbidden and free, and say what Hobbes means by the silence of the law."),
        ("Name what a subject may refuse",
         "State the liberties no covenant can transfer, find the commands that fall "
         "on them, and say how long a subject's obligation lasts."),
        ("Say who answers for an assembly's decree",
         "Given an assembly's voices on a motion, say whether it passes, fails or is "
         "mute and who is answerable for a debt it voted, and name the public ministers."),
    ],
    "syllabus_intro": (
        "One lesson reads Chapter 20, two read Chapter 21, one for liberty and one for "
        "what a subject may refuse, and the last reads Chapters 22 and 23 together."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's words "
        "and goes back through them a phrase at a time. This course is a read-along of "
        "Thomas Hobbes, Leviathan (1651). Quotations are from Hobbes's text of 1651, in "
        "its original spelling, and the examples are written for these lessons.",
        "Read Chapters 20 and 21 as one argument. Chapter 20 makes the sovereign's power "
        "as great as it can be, and Chapter 21 asks what is left to the subject. The "
        "answer in the second is meant to be read against the first.",
        "Use the labs to change one thing at a time. Each preset changes a single figure "
        "against the one before, a fine, a statute, a vote, and the point of the lesson is "
        "in what moves and what does not.",
        "Keep the definitions apart from the verdict. Every figure follows from the "
        "definitions the lesson states. Whether men and commonwealths are as Hobbes "
        "describes them is what the book argues about, and each lesson says where the "
        "strongest objection comes from.",
    ],
    "not_covered": [
        "The scriptural half of Chapter 20 and the biblical cases in Chapter 21. Hobbes "
        "reads the king's right in Samuel and the story of Uriah for his argument, and "
        "the lessons mention them and go no further; Part III takes up his way of reading "
        "Scripture.",
        "The Bramhall controversy at length. Liberty and necessity are read as Chapter 21 "
        "states them; the exchange with the bishop, and later accounts of free will, are "
        "outside the course.",
        "The English law of the courts in Chapter 23. His praise of the twelve men and the "
        "Lords' privilege is mentioned and not studied; no lab models a court.",
        "Merchant companies as history. Hobbes's case against their double monopoly is "
        "summarised, and the economics of the chartered companies is not.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the payoffs, laws "
        "and votes a lesson states, in exact arithmetic, on Hobbes's definitions as "
        "stated. The figures are invented for the lessons, and no lab can tell you whether "
        "men or commonwealths are as Hobbes describes them."
    ),
    "lessons": part_a.LESSONS,
}
