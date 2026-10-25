"""Course 1 -- Laying the Foundation: Part I of Code Complete, Chapters 1-4.

Three lessons, one module each: what construction is and which metaphor to
think about it with (Chapters 1 and 2 together), what must be settled
upstream (Chapter 3), and the decisions taken at the start of construction
(Chapter 4). Page references are to the second edition (Microsoft Press,
2004). The course has the least code of any: the book's first Part is about
the work around the code, so all three labs do the arithmetic of figures the
lessons state, and the one Java snippet is a convention, not a computation.
"""

from . import part_a

COURSE = {
    "slug": "code-complete-laying-the-foundation",
    "title": "Laying the Foundation",
    "level": "Beginner",
    "summary": (
        "Part I of the book, Chapters 1 to 4: Welcome to Software Construction; Metaphors for "
        "a Richer Understanding of Software Development; Measure Twice, Cut Once: Upstream "
        "Prerequisites; and Key Construction Decisions. McConnell says what he means by "
        "construction and why it is the activity every project does, which picture of "
        "software development to think with, what has to be settled before construction "
        "starts and how much, and which decisions the programmers themselves take at the "
        "start. The labs compute construction's share of a project's hours, the cost of "
        "defects found late by the book's cost table, and the size of a program in another "
        "language by the book's statement ratios."
    ),
    "blurb": (
        "Read Part I, a chapter or two at a time. Mark a project's activities as construction "
        "or not and compute their share, price a set of defects by the phase each was made "
        "in and the phase it was found in, and supply in Java, by convention, a facility the "
        "language does not have."
    ),
    "key": [
        "construction: the activity sure to happen",
        "metaphors: heuristics, not algorithms",
        "share: construction hours / all hours",
        "fix a defect near where it was made",
        "late cost: count times the table cell",
        "program into a language, not in it",
        "a count is a reason to look",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no earlier course; you can read a short Java routine, and the arithmetic is "
        "adding, multiplying and dividing"
    ),
    "outcomes_intro": (
        "By the end you can say what Part I argues, chapter by chapter, and do each "
        "chapter's arithmetic by hand."
    ),
    "outcomes": [
        ("Classify construction activities",
         "Mark a project's activities as construction or not by the list in Section 1.1, "
         "and compute construction's share of the hours as a fraction and a percentage."),
        ("Compare the chapter's metaphors",
         "State what the writing, farming, accretion and building metaphors each suggest "
         "about software development, and which of them McConnell rejects and why."),
        ("Price defects found late",
         "Given defects by the phase each was introduced in and the phase it was found in, "
         "compute their relative cost from the book's table, the cost had each been found "
         "where it was made, and the ratio between the two."),
        ("Place a project's upstream work",
         "State the kind of software a project is, what Section 3.2 says that implies for "
         "how much is settled before construction, and the book's figures for the effort "
         "and schedule a well-run project spends upstream."),
        ("Program into a language",
         "Convert a size in statements of C by one of the book's ratios and say what the "
         "ratio does not measure, and write the Java convention that supplies a facility "
         "the language lacks."),
    ],
    "syllabus_intro": (
        "Three lessons follow the book's first Part in order. Chapters 1 and 2 are short "
        "and share a lesson; Chapters 3 and 4 have one each."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Steve McConnell's "
        "<em>Code Complete</em>, second edition (Microsoft Press, 2004). Each lesson opens "
        "with one short quotation, then sets out the chapter's argument in its own words, "
        "section by section, and names the pages; the section numbers and pages are that "
        "edition's. The code in the lessons is written for them, and none of the book's "
        "listings, tables or checklists is reproduced; read those in your copy.",
        "Expect little code in this course. The book's first Part is about the work around "
        "the code: what construction is, what has to be settled before it, and what to "
        "decide at its start. All three labs therefore do arithmetic on figures the lesson "
        "states, and the one Java snippet, in the third lesson, is a convention rather than "
        "a computation. From the next course on, many labs read Java.",
        "Treat the book's figures as other people's averages. Construction's share of a "
        "project, the cost of a late fix and the statement ratios are syntheses of studies "
        "from the 1970s to 2003, collected by Jones, Boehm and others. Each lesson says "
        "whose figure it is the first time it uses one, and your own records can test it; "
        "the lab cannot.",
        "Keep a project of your own in mind. Every lesson ends by sending you to your own "
        "work, a week's calendar, the last few defects in a tracker or a facility your "
        "language lacks, with something to compute or write.",
    ],
    "not_covered": [
        "Requirements engineering and software architecture as disciplines. Chapter 3 says "
        "how to tell whether they have been done well enough to start construction, not how "
        "to do them, and so do the lessons; the book's further reading names the works "
        "that teach them.",
        "The book's checklists for requirements, architecture, upstream prerequisites and "
        "major construction practices. The lessons name them and paraphrase two or three "
        "points; the lists themselves are the book's and are better used from your copy.",
        "The language descriptions in Section 4.1. The book's thumbnail histories of Ada, "
        "Cobol, Fortran, Java and the rest are named, not summarised, and no lesson says "
        "one language is better than another.",
        "Process methodologies. Extreme Programming, Scrum, the Rational Unified Process "
        "and evolutionary delivery appear where the book names them, as examples of "
        "iterative or sequential approaches; none is taught.",
        "What has changed since 2004 in how much teams settle before they build. Upstream "
        "Prerequisites states the book's position and the later agile view once, in its "
        "note, and does not settle between them.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "a share is the hours you mark divided by all the hours, a cost is each count times "
        "the cell the lesson gives from the book's table, and a size in another language is "
        "a size in C divided by the book's ratio. The hours are illustrative; the table and "
        "the ratios are the book's, after the sources it names. None of the figures says "
        "whether a project is well run."
    ),
    "lessons": part_a.LESSONS,
}
