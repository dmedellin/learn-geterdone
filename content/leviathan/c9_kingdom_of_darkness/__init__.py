"""Course 9 -- The Kingdom of Darkness, and the Review and Conclusion: Part IV
(Chapters 44-47) and the Review and Conclusion that closes the book.

One lesson module: five lessons. LEVKIT_LESSONS joins LESSONS once the levkit
lab kit is registered.
"""

from . import part_a

COURSE = {
    "slug": "leviathan-kingdom-of-darkness",
    "title": "The Kingdom of Darkness, and the Review and Conclusion",
    "level": "Advanced",
    "summary": (
        "Part IV and the end of the book. Hobbes's account of the kingdom of darkness as a "
        "confederacy of deceivers, how the present church came to be taken for the kingdom of "
        "God, why the demons and images of the Gentiles and the philosophy of the schools "
        "count as its materials, who gained by the doctrines, and the Review and Conclusion "
        "in which he reconciles the faculties, adds a law of nature and says when a subject "
        "may submit to a conqueror."
    ),
    "blurb": (
        "Read the last Part of Leviathan, where the argument turns on Scripture and on words. "
        "Test Hobbes's case against the church as God's kingdom for validity, work his "
        "definitions of images and spirits and of the schoolmen's terms, count who each "
        "doctrine served, and compute when a subject's obedience is owed and when "
        "protection has failed."
    ),
    "key": [
        "valid: no counterexample row",
        "a name is the sum of simpler names",
        "an insignificant name stands for nothing",
        "cui bono: count each doctrine's beneficiaries",
        "keep = benefit − cost; break = benefit − risk",
        "obedience is owed while protection lasts",
    ],
    "assumes_short": "The earlier courses help",
    "assumes_long": (
        "the argument of Parts I to III is used throughout, above all the definitions of "
        "Chapters 4 and 5, the sovereign of Chapters 17 to 21 and the Christian commonwealth of "
        "Chapters 32 to 43; school arithmetic is enough for the labs"
    ),
    "outcomes_intro": (
        "By the end you can state, test and compute the last Part's arguments yourself, and "
        "say what each figure is a figure of."
    ),
    "outcomes": [
        ("Test the argument against the present church",
         "Write Hobbes's reply to the claim that the church is the kingdom of God as premises "
         "and a conclusion, test it for validity and name the premise that carries it."),
        ("Classify claims about demons and spirits",
         "Given definitions of body, phantasm, image and spirit, say which affirmations about "
         "demons, ghosts and spirits are true, false or absurd on them."),
        ("Separate insignificant speech from false speech",
         "Given a vocabulary, say which of the schoolmen's affirmations are insignificant "
         "because a name stands for nothing, and which are absurd."),
        ("Count who a doctrine served",
         "Given Hobbes's list of doctrines and the parties each benefits, count the "
         "doctrines for each party and name the party served by the most."),
        ("Compute when obedience is owed",
         "Given what protection is worth and obedience costs, and a stated sanction, say when "
         "a subject does better to obey, the least sanction that makes it so, and what changes "
         "when protection fails."),
    ],
    "syllabus_intro": (
        "Four lessons take the four chapters of Part IV in order, one chapter each: the "
        "misreading of Scripture, the demonology of the Gentiles, vain philosophy, and who "
        "benefited. The last reads the Review and Conclusion and ends the book."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's words and "
        "then goes back through them a phrase at a time. This course takes up a subject "
        "he never leaves out of the book, Scripture, and the lessons present what he argues "
        "and what it did in 1651, fairly, and neither mock it nor defend it as theology. "
        "Quotations are from Hobbes's text of 1651, in its original spelling, and the "
        "examples are written for these lessons.",
        "This is the last course and it leans on the first. The labs on images and on the "
        "schoolmen reuse the names-and-definitions lab from Courses 1 and 2; if "
        "&ldquo;insignificant&rdquo; or &ldquo;absurd&rdquo; is unfamiliar, read "
        "&ldquo;Of Speech&rdquo; and &ldquo;Absurdity and Science&rdquo; again.",
        "Use the labs to change one thing at a time. Each preset changes a single premise, "
        "definition, doctrine or payoff against the one before, and the point is in what "
        "moves and what does not.",
        "Keep the definitions apart from the verdict. Every figure is computed from what the "
        "lesson states. Whether Hobbes's definitions describe men, churches and "
        "commonwealths is what the book argues, and each lesson says where the strongest "
        "objections come from.",
    ],
    "not_covered": [
        "The theology of the questions. Whether purgatory, transubstantiation or the immortality "
        "of the soul is true is a question for the churches. The lessons report what Hobbes "
        "argues about each from Scripture and what the argument was for, and compute only "
        "what follows from the premises stated.",
        "The Latin Leviathan of 1668 and its appendix, which are not in the text this course "
        "reads, and Tuck's introduction and notes, which are in copyright and are never "
        "quoted.",
        "Who was right about the Church of Rome, the Presbyterians or the universities. The "
        "benefit lab counts doctrines against the parties Hobbes names. It does not say "
        "that benefit shows authorship, which is Hobbes's presumption and not a proof.",
        "The English civil wars and the Engagement. They are the occasion of the Review and "
        "Conclusion and are named where the text names them; the course does not retell "
        "them.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the premises, names, "
        "doctrines and payoffs a lesson states, and shows what follows from them on "
        "Hobbes's definitions. Whether those definitions are true of men and commonwealths "
        "is what the book argues, and no lab can settle it."
    ),
    "lessons": part_a.LESSONS + part_a.LEVKIT_LESSONS,
}
