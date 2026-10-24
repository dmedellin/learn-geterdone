"""Course 7 -- The Cogito, Time and Freedom: Part Three (Smith pp. 429-530).

Eight lessons in three modules, one per chapter: part_a reads the Cogito
(three lessons) and the opening of Temporality; part_b reads the rest of
Temporality and Freedom, and ends where the book does.
"""

from . import part_a, part_b

COURSE = {
    "slug": "perception-cogito-time-and-freedom",
    "title": "The Cogito, Time and Freedom",
    "level": "Advanced",
    "summary": (
        "Part Three, Being-for-Itself and Being-in-the-World: 1 The Cogito; 2 Temporality; "
        "3 Freedom. Merleau-Ponty asks what the thinking subject becomes after a book about "
        "the perceiving body. He keeps Descartes's cogito and gives it a temporal thickness, "
        "finds beneath the cogito in words a tacit one, reads the subject as time itself, and "
        "answers a theory of absolute freedom with a freedom that always works in a field. "
        "The labs test the cogito as an inference, draw the geometer's construction, count "
        "Husserl's diagram of time and code the chapters' cases against the opponents' "
        "accounts."
    ),
    "blurb": (
        "Read the book's last hundred pages a section at a time. Set out the cogito as an "
        "inference, compute a triangle's construction at each vertex, classify a river's "
        "water from two standpoints, follow a moment down Husserl's diagram, and count "
        "determinism and absolute freedom over the chapter's cases."
    ),
    "key": [
        "certain of seeing only if seeing",
        "the cogito is spoken; beneath it, tacit",
        "a construction is a gesture",
        "time presupposes a view of time",
        "retention: held through later moments",
        "time as the subject, subject as time",
        "never determinism, never absolute choice",
    ],
    "assumes_short": "The earlier courses",
    "assumes_long": (
        "the earlier courses, especially the body schema and motor intentionality from The "
        "Lived Body and the perceived thing from Things, the World and Others; school "
        "geometry is enough for the labs"
    ),
    "outcomes_intro": (
        "By the end you can say, in the book's terms, what becomes of the thinking subject, "
        "of time and of freedom, and do the lab's work for each chapter."
    ),
    "outcomes": [
        ("Test the cogito as an inference",
         "Write an argument in sentence letters, find its counterexample rows and the "
         "premise that would make it valid, and say why the chapter does not read the "
         "cogito as an inference."),
        ("Compute a geometric construction",
         "Compute a triangle's third angle, the alternate angles at the parallel through "
         "each vertex and the straight angle, and say what the construction adds to the "
         "definition."),
        ("Count opponent accounts over a chapter's cases",
         "From a coding of cases against two accounts, compute each record, the survivors, "
         "the split and the cases both fail, and state the chapter's own account without "
         "scoring it."),
        ("Read Husserl's diagram of time",
         "For any present, compute the depth of each retained moment, the column and the "
         "protended moments, and follow one moment across several presents."),
        ("State the chapters' claims at strength",
         "State Descartes's, Kant's, Husserl's, Heidegger's and Sartre's positions as the "
         "chapters meet them, and the reply to each, saying where the reading is disputed."),
    ],
    "syllabus_intro": (
        "Eight lessons in the book's order: three on the Cogito, three on Temporality and two "
        "on Freedom. The last lesson ends where the book does."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with a short passage "
        "and then goes back through the section a phrase at a time, so read the whole "
        "section in your own copy first. Quotations are from Colin Smith's translation "
        "(Routledge Classics), short extracts quoted for commentary, and page numbers are "
        "that edition's.",
        "Watch whose voice a sentence is in. The Cogito spends six pages on an idealist "
        "reading before answering it, and Freedom opens with pages in the voice of the "
        "theory of absolute freedom. Each lesson says whose view a sentence states.",
        "Take the labs for what they say they compute. One is propositional logic, one "
        "school geometry, four are the lesson's models of the chapter's images, and two "
        "count the lesson's coding of the cases. None computes an experience, a moment of "
        "time or anyone's freedom.",
        "Expect disputes. The tacit cogito was called impossible by Merleau-Ponty himself in "
        "his late notes, and how fairly Freedom treats Sartre, and Temporality Heidegger and "
        "Husserl, is argued over still. The lessons say where, and do not settle it.",
    ],
    "not_covered": [
        "Descartes's, Kant's, Husserl's, Heidegger's and Sartre's own books. Each is met "
        "where the chapters argue with him, briefly and at his strongest; their texts are "
        "not read, and the lessons' few references to them are named as the lessons'.",
        "The Cogito's pages on evidence and truth, Spinoza and the contingency of the world "
        "(pp. 459-464), which are summarised rather than read line by line.",
        "The detail of the passages on Bonaparte and the French Revolution in Freedom (pp. "
        "521-523), which the lessons pass over for the cases they code.",
        "The secondary literature on Merleau-Ponty's relation to Sartre and to Husserl's "
        "late manuscripts. The lessons say where a reading is disputed and go no further.",
        "Merleau-Ponty's late work, The Visible and the Invisible, named only where it "
        "revises the tacit cogito.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "a truth table from sentence letters, a triangle's angles from two given angles, a "
        "river's past and future from positions, the depths of Husserl's diagram from a list "
        "of moments, obstacles from rock heights and two thresholds, and a count over the "
        "lesson's coding of the cases. The models are the "
        "lessons' and the heights illustrative. None of them is a moment of time or an act of "
        "freedom, which is what Part Three is about."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
