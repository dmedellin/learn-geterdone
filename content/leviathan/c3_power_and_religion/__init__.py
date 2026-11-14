"""Course 3 -- Power, Manners and Religion: Leviathan, Part I, Chapters 10-12.

One module, five lessons in part_a: two on Chapter 10 (power and worth; honour,
dignity and worthiness), one on Chapter 11 (the difference of manners) and two on
Chapter 12 (the natural seeds of religion; religion and policy).
"""

from . import part_a

COURSE = {
    "slug": "leviathan-power-manners-religion",
    "title": "Power, Manners and Religion",
    "level": "Introductory",
    "summary": (
        "Leviathan, Part I, Chapters 10 to 12. What Hobbes means by power and by a "
        "man's worth, how honour and dignity differ from both, why he thinks every man "
        "wants power after power, and where he finds the seeds of religion and what he "
        "says the founders of religions did with them."
    ),
    "blurb": (
        "Price four men's powers for three buyers and see why no ranking is absolute, "
        "set a title beside the prices, play Hobbes's restless desire of power as a "
        "table for two neighbours, weigh how far a sign seen once or twice should move "
        "you, and test his argument that a priest who teaches contradictions loses his "
        "hearers."
    ),
    "key": [
        "worth = price = what a buyer would give",
        "dignity: the value the commonwealth sets",
        "power after power, ceasing only in death",
        "four seeds of religion, one a mistaken sign",
        "contradiction discredits the teacher",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no philosophy or political theory is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can say what Hobbes defines in these three chapters and compute "
        "the small figures each lesson builds on his definitions."
    ),
    "outcomes": [
        ("Price a man's powers",
         "Given each man's powers and each buyer's needs, compute each buyer's price, "
         "rank the men, and say whether the buyers' rankings agree."),
        ("Tell dignity from worth",
         "Compare the dignity a commonwealth sets with each buyer's price, and say "
         "which of honour, dignity, worth and worthiness each comparison concerns."),
        ("Read a restless desire as a table",
         "Mark best replies in a table for two neighbours who may hold or add, and say "
         "whether a moderate temperament can still end in the arming equilibrium."),
        ("Weigh a sign",
         "Update a credence in a sign on one or two observations from stated chances, "
         "and say when the sign is no evidence."),
        ("Test an argument about religion",
         "Set out Hobbes's argument that enjoining contradictories discredits a teacher, "
         "decide whether it is valid, and name the premise it depends on."),
    ],
    "syllabus_intro": (
        "Two lessons read Chapter 10, one reads Chapter 11 and two read Chapter 12, "
        "from the price of a man to the way a religion loses its hold."
    ),
    "how_to": [
        "This course is a read-along of Thomas Hobbes, <em>Leviathan</em> (1651). Every "
        "lesson opens with Hobbes's words and then goes back through them a phrase at a "
        "time, so the passage is worth a second reading once the lesson is done. "
        "Quotations are from Hobbes's text of 1651, in its original spelling; the "
        "lessons themselves use modern spelling, and the examples are written for these "
        "lessons.",
        "Use the labs to change one thing at a time. Each preset changes a single "
        "figure against the one before: a buyer's need, a title, a payoff, one more "
        "observation of a sign. The point of the lesson is in what moves and what does not.",
        "Keep what Hobbes says apart from what the figures show. Every figure is "
        "computed from numbers the lesson states, and shows what follows from them on "
        "Hobbes's definitions. Whether men are as he describes them is what the book "
        "argues, and each lesson says where the strongest objection comes from.",
    ],
    "not_covered": [
        "Hobbes's physics of the passions. Chapter 10 uses the account of good, appetite "
        "and power that Chapters 1 to 9 build, and this course takes it as given.",
        "A history of honour, titles and heraldry. Chapter 10 closes, just before "
        "worthiness, with a long digression on coats of arms and titles, from the Germans and the Romans; the lessons mention "
        "it and do not teach it.",
        "Revealed religion. Chapter 12 says the religion of Abraham, Moses and Christ is "
        "divine politics, and leaves the Kingdom of God for later; Of a Christian Commonwealth takes it up.",
        "The Gentile religions in detail. The long list of gods and divinations in "
        "Chapter 12 is read once, as evidence for Hobbes's point, and not catalogued.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the powers, needs, "
        "payoffs and chances a lesson states, and shows what follows from them on "
        "Hobbes's definitions. Whether men are as he describes them is what the book "
        "argues and no figure here can settle."
    ),
    "lessons": part_a.LESSONS,
}
