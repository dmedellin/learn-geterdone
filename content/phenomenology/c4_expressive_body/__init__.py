"""Course 4 -- The Expressive Body: Part One, Chapters 4-6 (Smith pp. 171-232).

Four lessons, one module: part_a reads the synthesis of one's own body, the
body in its sexual being, and the two halves of the chapter on expression and
speech.
"""

from . import part_a

COURSE = {
    "slug": "perception-the-expressive-body",
    "title": "The Expressive Body",
    "level": "Intermediate",
    "summary": (
        "Part One, The Body, its last three "
        "chapters: 4, The Synthesis of One's own Body; 5, The Body in its Sexual Being; and 6, "
        "The Body as Expression, and Speech. The body's unity is compared to a work of art's "
        "rather than a machine's or a law's; sexuality is read as a way of being in the world, "
        "through Schneider and Binswanger's patient who lost her voice; and speech is read as a "
        "gesture whose meaning is in the word. Two labs compute what stays through a set of "
        "variants, one counts the chapter's cases against two accounts, and one sets a sort by "
        "category beside a chain of resemblances."
    ),
    "blurb": (
        "Read the three chapters that close Part One. Compute what stays when one movement is "
        "made by different limbs, count where two accounts of sexuality fail on the chapter's "
        "cases, find the sample where a sort by resemblance leaves a colour category, and look "
        "for the bodily sign that every expression of anger shares."
    ),
    "key": [
        "the body: a work of art, not a machine",
        "core = what every variant keeps",
        "sexuality and existence are interfused",
        "an account survives if no case refutes it",
        "the word has a meaning",
        "speech accomplishes thought",
        "in man there is no natural sign",
    ],
    "assumes_short": "The Lived Body",
    "assumes_long": (
        "the body schema, Schneider's case, the intentional arc and habit as The Lived Body "
        "reads them, and the two opponents of Classical Prejudices"
    ),
    "outcomes_intro": (
        "By the end you can say, in the chapters' own terms, why the body's unity, its "
        "sexuality and its speech are each a kind of expression, and do each lab's count."
    ),
    "outcomes": [
        ("Compute what stays through a set of movements",
         "From a coded set of variants of one movement, compute the core, what varies and what "
         "an excluded variant lacks, and say why the chapter will not call the core the body's "
         "unity."),
        ("Count two accounts against the chapter's cases",
         "Given the lesson's coding of Schneider and of Binswanger's patient, compute each "
         "account's record and the observations on which the two part, and state the account "
         "the chapter gives instead, in prose."),
        ("Set a sort by category beside a sort by resemblance",
         "Compute a categorical sort and a chain of concrete resemblances over colour samples, "
         "name the sample where they part, and state Gelb and Goldstein's reading and the "
         "chapter's reply."),
        ("Look for a natural sign",
         "Compute the bodily sign common to a set of expressions of one emotion, and say what "
         "an empty core does and does not show about natural and conventional signs."),
        ("State the chapters' claims at strength",
         "State the opponents each chapter answers, the machine and the law, automatism and "
         "representation, the verbal image and the categorial act, the natural sign, and the "
         "chapter's reply to each."),
    ],
    "syllabus_intro": (
        "Four lessons follow the book's order: Chapter 4 in one lesson, because it is short; "
        "Chapter 5 in one; and Chapter 6 in two, the word's meaning and the aphasia it is read "
        "through, then the gesture, the emotions and the speaking word."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with a short passage and "
        "then goes back through the chapter a phrase at a time, so read the pages it names in "
        "your own copy first. Quotations are from Colin Smith's translation (Routledge "
        "Classics), short extracts quoted for commentary, and page numbers are that edition's.",
        "Expect the chapters to lean on The Lived Body. Schneider, the body schema (Smith's "
        "word is body image), the intentional arc and the blind man's stick all come back, and "
        "the lessons recall them briefly rather than teaching them again.",
        "Treat the cases as people. Schneider and the girl who lost her voice were patients, "
        "known to the book through their doctors' reports. Each lab codes a report, and each "
        "lesson says whose report it is.",
        "Watch whose voice a sentence is in. Merleau-Ponty states the mechanist, the "
        "intellectualist and the psychoanalyst in their own words before he answers, and reads "
        "Freud, and Gelb and Goldstein, in a way of his own. Each lesson says whose view it is "
        "reporting.",
    ],
    "not_covered": [
        "The later status of Schneider's case. Gelb and Goldstein's reports were questioned by "
        "the neurologists who re-examined him in 1949, and later reviews judged that the "
        "theoretical conclusions drawn from them went beyond the data. The lessons say in a "
        "sentence that the book's argument concerns the case as reported, and go no further.",
        "Freud and psychoanalysis in their own terms. The chapter reads psychoanalytic practice "
        "against Freud's theoretical declarations, and how far that reading is fair to Freud "
        "is disputed. The lessons say so and do not try to settle it.",
        "The footnote on historical materialism, pp. 198 to 201, is summarised in “The Body as "
        "a Sexed Being”, not read line by line, and Marx's own texts are not read.",
        "The aphasia literature beyond the book. Broca, Pierre Marie, Head and Goldstein appear "
        "as the chapter reports them; the lessons do not judge their neurology.",
        "Merleau-Ponty's other writings on language and on Cézanne, and the late work, are not "
        "read.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: a "
        "core by intersecting the lesson's coding of a set of variants, an account's record by "
        "counting the lesson's coding of the chapter's cases, and a chain of resemblances by "
        "the lesson's own printed rule. The coding is an interpretation of the text, and the "
        "lessons say so. None of the figures is an experience, which is what these chapters "
        "are about."
    ),
    "lessons": part_a.LESSONS,
}
