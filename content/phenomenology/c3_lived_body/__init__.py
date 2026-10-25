"""Course 3 -- The Lived Body: Part One, its introduction and Chapters 1-3 (Smith pp. 77-170).

Eight lessons in two modules split at the midpoint: part_a is the introduction,
Chapter 1 (two lessons) and Chapter 2; part_b is Chapter 3 in four lessons, the
body schema, Schneider, the intentional arc and habit.
"""

from . import part_a, part_b

COURSE = {
    "slug": "perception-the-lived-body",
    "title": "The Lived Body",
    "level": "Intermediate",
    "summary": (
        "Part One, The Body: its introduction, Experience and Objective Thought. The "
        "Problem of the Body, and Chapters 1 to 3, The Body as Object and Mechanistic "
        "Physiology, The Experience of the Body and Classical Psychology, and The "
        "Spatiality of One's own Body and Motility. Objective thought posits the house "
        "seen from nowhere and treats the body as one more object; the phantom limb, the "
        "body that never leaves, the body schema, Schneider's case and the acquisition of "
        "habit each show the body escaping that treatment, until motility appears as "
        "intentionality in its own right."
    ),
    "blurb": (
        "Read Part One's first half a chapter at a time. Count what a set of views of a "
        "house reaches, score two explanations of the phantom limb and two accounts of "
        "Schneider over their reported observations, find what appeals to a hand that is "
        "gone, convert a position into the body's frame, and compute the reach of a cane "
        "and the clearance of a feathered hat, which the chapter says a habit never "
        "computes."
    ),
    "key": [
        "objective thought: the body as object",
        "phantom: neither nerves nor memory",
        "habit-body and body at this moment",
        "the body: with me, never in front",
        "body schema: a hold on tasks",
        "grasping is not pointing",
        "the intentional arc goes limp",
        "habit: motor grasp of a meaning",
    ],
    "assumes_short": "Classical Prejudices",
    "assumes_long": (
        "the Introduction's two opponents, empiricism and intellectualism, as Classical "
        "Prejudices sets them out, and What Phenomenology Is for the idea of description; "
        "the labs need only school geometry and fractions"
    ),
    "outcomes_intro": (
        "By the end you can say, in the terms of Part One, why the body is not an object "
        "among objects, and do each lab's count or arithmetic yourself."
    ),
    "outcomes": [
        ("Count what a set of views reaches",
         "From whole-number view directions on a box, compute each view's faces, the union, "
         "the smallest cover and, for one's own body, the faces no view reaches, and say "
         "what no set of views supplies."),
        ("Score accounts over a case",
         "Given reported observations coded for two opponent accounts, compute each "
         "record, the survivors and the split, and explain a survivor on a short table or "
         "one that survives by silence."),
        ("Model the body's two frames and two layers",
         "Convert a room position into the body's frame as it turns and walks, classify a "
         "target as given in the body's situation or as a position, and find what appeals "
         "only to the habit-body."),
        ("Compute a body extended by its instruments",
         "Compute the reach of an arm and a cane and the clearance of a body and what it "
         "carries, and state why the chapter says habit makes no such comparison."),
        ("State Part One's claims at strength",
         "State the physiological and psychological explanations of the phantom limb, "
         "classical psychology's characteristics of the body, the visual and the "
         "intellectualist readings of Schneider and the two classical accounts of habit, "
         "and the book's reply to each."),
    ],
    "syllabus_intro": (
        "One lesson reads the introduction to Part One, two read Chapter 1, one reads "
        "Chapter 2, and four follow Chapter 3 from the body schema through Schneider's case "
        "to habit, which closes the chapter."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with a short passage "
        "and then goes back through the section a phrase at a time, so read the whole "
        "section in your own copy first; each lesson gives the pages. Quotations are from "
        "Colin Smith's translation (Routledge Classics), short extracts quoted for "
        "commentary, and page numbers are that edition's.",
        "Expect cases rather than arguments in the abstract. Part One argues from patients: "
        "the amputees and the anosognosics of Chapter 1, and Gelb and Goldstein's patient "
        "Schneider in Chapter 3. The lessons code the reports the book cites, not the "
        "patients, and say where a report was later questioned.",
        "Read every table as a count of a reading. Two lessons score opponent accounts over "
        "the chapter's observations; the count is exact and each cell is the lesson's "
        "coding, which you can check against the page. Merleau-Ponty's own account is "
        "stated in the prose and never scored.",
        "Watch whose voice a sentence is in. The chapters state the physiologist's, the "
        "classical psychologist's and the intellectualist's views at length, in their own "
        "words, before answering them, and each lesson says whose view it is reporting.",
    ],
    "not_covered": [
        "The later fate of Schneider's case. Bay, Lauenstein and Cibis, and Jung, re-examined "
        "the patient in 1949 and questioned the reports; of the modern reviews, Goldenberg's in "
        "Classic Cases in Neuropsychology II (2003) doubts that it deserves to be a classic "
        "case, and Marotta and Behrmann's in Neuropsychologia (2004) proposes reading it as an "
        "integrative visual agnosia. The lessons say so and read the book's argument "
        "about the case as Gelb and Goldstein reported it; the dispute is not taken further.",
        "Modern neuroscience of the body. The phantom limb lesson sets Ramachandran's mirror "
        "box beside the chapter once, with its caveats; body-schema research since 1945 is "
        "otherwise not read, and no lab computes from it.",
        "The sources' own texts. Lhermitte, Head, Schilder, Gelb and Goldstein, Cassirer and "
        "Bergson appear as the chapters cite and argue with them, not read in their own "
        "books.",
        "Merleau-Ponty's other works. The Structure of Behaviour, which these chapters cite "
        "for the insect and for reflexes, is not read, and The Visible and the Invisible, "
        "which recasts the touching hands as reversibility, is named only to keep it out of "
        "this book.",
        "The footnotes on Bergson, Janet and Liepmann's apraxic patient, and the long "
        "middle of Chapter 3 on perception, story-telling and number in Schneider, which are "
        "summarised rather than read line by line.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "the faces a set of views reaches, an account's record over coded observations, a "
        "reach or a clearance in centimetres, a position in the room and relative to the "
        "body. The positions and lengths are illustrative and the codings are the lessons' "
        "readings of the chapters. None of them is the lived body, which is what Part One "
        "is about."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
