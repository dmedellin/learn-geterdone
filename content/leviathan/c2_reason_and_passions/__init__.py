"""Course 2 -- Reason, Science and the Passions: Leviathan, Part I, Chapters 5-9.

Split across two lesson modules: part_a is Chapters 5 and 6 (reason, absurdity
and science, the passions, deliberation and the will); part_b is Chapters 7 to 9
(discourse, belief and faith; wit and madness; the subjects of knowledge).
"""

from . import part_a, part_b

COURSE = {
    "slug": "leviathan-reason-and-passions",
    "title": "Reason, Science and the Passions",
    "level": "Introductory",
    "summary": (
        "Leviathan, Part I, Chapters 5 to 9. Reasoning as the adding and subtracting of "
        "names, the seven causes of absurd conclusions, science as knowledge of "
        "consequences, the passions as motions toward and away from things, deliberation "
        "and the will, belief and faith, wit and madness, and the table of the sciences."
    ),
    "blurb": (
        "Read the chapters in which Hobbes says thinking is a kind of arithmetic and "
        "feeling is a kind of motion. Add two affirmations into a syllogism and find the "
        "case that defeats a bad one, classify claims as true, false, absurd or "
        "insignificant from stated definitions, name the passion a case describes, watch "
        "a deliberation end in a will, and place each science in Hobbes's table."
    ),
    "key": [
        "reason = adding and subtracting names",
        "true by definition: every part is a part",
        "absurd: names that cannot be added",
        "passion = appetite or aversion plus opinion",
        "will = the last appetite before the act",
        "science is conditional knowledge",
    ],
    "assumes_short": "Sense, Imagination and Speech",
    "assumes_long": (
        "Chapter 4's account of names, which the first course reads, is used throughout, "
        "but each lesson restates what it needs and school arithmetic is enough"
    ),
    "outcomes_intro": (
        "By the end you can reckon with names as Hobbes describes it and say, for each "
        "of his definitions, what it makes true and what it leaves for the reader to "
        "argue."
    ),
    "outcomes": [
        ("Test a syllogism",
         "Add two affirmations into a conclusion, say whether it follows, and describe "
         "the case that defeats it when it does not."),
        ("Classify a claim",
         "Expand each name in a claim into the simple names it is defined by, and say "
         "whether the claim is true, false, absurd or insignificant, and why."),
        ("Name a passion",
         "Given a case of appetite or aversion and an opinion of attaining or of "
         "hurt, give the passion Hobbes's definitions assign to it."),
        ("Find the will",
         "Given a deliberation as a sequence of appetites and aversions, find the will, "
         "say whether the act was done or omitted, and count the earlier stops that "
         "would have given the opposite will."),
        ("Separate science from belief",
         "Say what a conditional chain of consequences proves, what it cannot prove "
         "about fact, and what is believed on a person's word."),
        ("Place a subject of knowledge",
         "Place a science in Hobbes's table of the sciences by the definitions it "
         "falls under, and spot one that has been misplaced."),
    ],
    "syllabus_intro": (
        "Two lessons read Chapter 5, two read Chapter 6, and one each reads Chapters 7, "
        "8 and 9."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's own "
        "words and then goes back through them a phrase at a time, so the passage is "
        "worth a second reading once the lesson is done. Quotations are from Hobbes's "
        "text of 1651, in its original spelling, and the examples are written for these "
        "lessons.",
        "Treat the labs as a way of making Hobbes's definitions do work. Four of the "
        "seven lessons give a small vocabulary of names and ask which claims follow from "
        "it. If a verdict surprises you, find the definition that produced it, which is "
        "the exercise Hobbes sets.",
        "Keep the definition apart from the verdict. Every figure shows what follows from "
        "the names a lesson states, on Hobbes's definitions as written there. Whether men "
        "think and feel as he says is what the book argues, and each lesson says where "
        "his critics stand.",
    ],
    "not_covered": [
        "Chapters 1 to 4 and the Introduction. The first course reads them, and this "
        "course uses their account of sense, imagination and names without repeating it.",
        "The theology and Scripture in these chapters. Chapters 7 and 8 reach the nature "
        "of faith and of possession by spirits, and the lessons say what Hobbes argues, "
        "briefly, and leave his Scripture to the course Of a Christian Commonwealth.",
        "Hobbes's physics and his mechanical account of the heart. The lessons use his "
        "language of motion and endeavour as definitions, and take no side on whether the "
        "passions are, in fact, motions of the body.",
        "The later philosophy of logic. De Morgan, Venn, Frege and the rest appear only "
        "where a lab's method differs from Hobbes's, in a sentence.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the names, "
        "payoffs and cases a lesson states, and shows what follows from them on Hobbes's "
        "definitions. The examples are written for these lessons, and no lab can say "
        "whether his account of reason and the passions is true."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
