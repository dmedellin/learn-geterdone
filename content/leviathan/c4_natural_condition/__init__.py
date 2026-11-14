"""Course 4 -- The Natural Condition and the Laws of Nature: Chapters 13-15.

Split across two lesson modules: part_a is Chapter 13 and Chapter 14 to the end of
'merit' (four lessons); part_b is Chapter 14 from mutual trust and Chapter 15
(three lessons).
"""

from . import part_a, part_b

COURSE = {
    "slug": "leviathan-natural-condition",
    "title": "The Natural Condition and the Laws of Nature",
    "level": "Beginner \u2192 Intermediate",
    "summary": (
        "Chapters 13 to 15 of Hobbes's Leviathan. The equality of ability from which Hobbes starts the war, the "
        "three causes of quarrel and the condition he calls the war of every man against every man, the right "
        "of nature and the first and second laws, contracts and covenants and when a covenant is void, the "
        "third law and the Fool who denies it, and the other laws of nature that make up moral philosophy."
    ),
    "blurb": (
        "Read the chapter the book is remembered for with the arithmetic beside it. Add up strengths to see "
        "who can be overcome, put competition and diffidence into two-person games, check the derivation of "
        "the second law, work out what a covenant is worth to the man who goes first and what a sanction does to "
        "it, run the Fool's calculation, and play a repeated dilemma against Hobbes's laws of gratitude and pardon."
    ),
    "key": [
        "strength: a coalition beats whom it outweighs",
        "diffidence: peace pays only if q > 2/3",
        "second law: lay down the right, if others do",
        "keep if the sanction beats the cost of keeping",
        "Fool: break if gain > chance times loss",
        "pardon on caution of the future",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no philosophy or political theory is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can say what Chapters 13 to 15 argue, and work out the figures that each argument "
        "turns on."
    ),
    "outcomes": [
        ("State the argument from equality",
         "Say what Hobbes claims about the equality of body and mind, and compute for a stated set of strengths "
         "who can be overcome by how few, and how large a difference would break the claim."),
        ("Say what war is and what follows from it",
         "State Hobbes's three causes of quarrel and his definition of war, and find the equilibria of the "
         "games that put competition, diffidence and one man's pleasure in conquest into a table."),
        ("Distinguish right from law",
         "State the right of nature and the first and second laws, and check the derivation of the second law "
         "for validity and name the premise that carries its condition."),
        ("Work out a covenant",
         "For a covenant in which one side performs first, compute the second party's gain from keeping and "
         "from breaking, with and without a sanction, and find the least sanction that makes keeping at least "
         "as good."),
        ("State the Fool's argument and Hobbes's reply",
         "Compute when breaking a covenant pays for a stated gain, loss and chance, and say which input "
         "Hobbes's reply to the Fool challenges."),
        ("Say what the laws of nature are",
         "Name the laws of gratitude, complaisance, pardon and revenge, say what each does in a repeated "
         "dilemma, and say what Hobbes means by obliging in foro interno and by calling the laws theorems."),
    ],
    "syllabus_intro": (
        "Two lessons read Chapter 13, two read the first half of Chapter 14, one reads the rest of Chapter 14, "
        "and two read Chapter 15, from the third law to the Fool and from gratitude to the end."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's words and then goes back "
        "through them a phrase at a time. Quotations are from Hobbes's text of 1651, in its original spelling, "
        "and the lessons' own prose uses modern spelling.",
        "Keep what the book says apart from what the lab shows. The figures are computed from numbers the "
        "lessons choose, and they show what follows on Hobbes's definitions as written there. Whether men are "
        "as he describes them is what the chapters argue, and each lesson says where the strongest objections "
        "come from.",
        "The chapters build on one another. Chapter 13's war is the question, Chapter 14's right and law are the first "
        "answer, and Chapter 15's covenants and Fool are where the answer is tested. A lesson that seems to "
        "leave a question open usually hands it to the next.",
        "Use the labs to change one thing at a time. Each preset changes a single figure against the one "
        "before: a man's strength, a payoff, a sanction, a chance of being found out, a strategy. The point "
        "of the lesson is in what moves.",
    ],
    "not_covered": [
        "Glory, the third cause of quarrel. Hobbes's quarrels over a word or a smile have no payoff the "
        "labs could attach to them, so Chapter 13's games leave glory out.",
        "The Philosophy course's game-theoretic reading of the state of nature. The lesson 'Hobbes and the "
        "State of Nature' in Games and the Social Contract writes competition, diffidence and a sovereign's "
        "fine as tables. This course reads the chapters and does not repeat it.",
        "How the laws of nature relate to civil law. Chapter 26 takes that up, and the courses on the "
        "commonwealth follow it.",
        "The Latin Leviathan of 1668, and Hobbes's earlier statements of the argument in The Elements of "
        "Law and De Cive. The course reads Leviathan as published in 1651.",
        "The scholarly dispute over whether Hobbes's obligations are prudential or moral. The seventh lesson "
        "names the two readings and does not decide between them.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the strengths, payoffs, sanctions and "
        "chances a lesson states, on Hobbes's definitions as written there. The figures are the lessons' own "
        "and no lab can tell you whether men are as Hobbes says they are."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
