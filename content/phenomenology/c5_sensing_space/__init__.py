"""Course 5 -- Sensing and Space: Part Two, introduction and Chapters 1-2 (Smith pp. 235-347).

Eight lessons in two parts: part_a reads Part Two's introduction and Chapter 1,
Sense Experience, in three lessons; part_b reads Chapter 2, Space, one lesson
per section (up and down, depth, movement, lived space).
"""

from . import part_a, part_b

COURSE = {
    "slug": "perception-sensing-and-space",
    "title": "Sensing and Space",
    "level": "Intermediate",
    "summary": (
        "Part Two of the book, The World as Perceived: its introduction, The Theory of the "
        "Body is already a Theory of Perception, and its first two chapters, Sense "
        "Experience and Space. Merleau-Ponty carries Part One's account of the body over to "
        "the perceived world: a colour is a way of moving before it is a quality, the "
        "subject of sensing is pre-personal, the senses communicate through the thing, and "
        "up and down, depth and movement are the body's hold on a world it lives in. The labs "
        "compute what the classical theories predict, the lesson's own model of a spatial "
        "level, and counts over the chapter's cases."
    ),
    "blurb": (
        "Read Part Two's introduction and its chapters on sensing and on space, a section at "
        "a time. Compute what a cube presents from a direction, what a pure quality predicts "
        "for the arm, what a glass keeps across four senses, tilt against a spatial level, "
        "the convergence of the eyes, the speed two alternating lights imply, and the "
        "records of two classical accounts against the chapters' cases."
    ),
    "key": [
        "the body is the subject of perception",
        "a colour has a motor physiognomy",
        "one perceives in me, not I perceive",
        "the senses communicate through the thing",
        "perceived tilt = image tilt − level",
        "depth: motives, not signs or causes",
        "what moves is identical in its moving",
        "existence is spatial",
    ],
    "assumes_short": "Classical Prejudices and The Lived Body",
    "assumes_long": (
        "Classical Prejudices for the two theories of perception the chapters argue with, "
        "and The Lived Body for the body schema and motor intentionality; The Expressive Body "
        "helps but is not needed, and school geometry is enough for the labs"
    ),
    "outcomes_intro": (
        "By the end you can do each lab's arithmetic and say, in the chapters' terms, what "
        "each figure is a prediction of and what the chapter puts in its place."
    ),
    "outcomes": [
        ("Compute what a view presents",
         "Given whole-number view directions on a cube, compute the faces each presents and "
         "the fraction at which parallel projection draws each, and say why the introduction "
         "calls the cube with six equal faces a limiting idea."),
        ("Compute a classical prediction and its gap",
         "Compute what a pure-quality account predicts for the arm under two colours, the "
         "convergence and disparity the classical theory of depth uses, and the speed two "
         "alternating lights imply, and state what each chapter says no perceiver computes."),
        ("Count two accounts against the cases",
         "From the lesson's coding of the chapters' observations, compute each classical "
         "account's record, the survivors and the split, and name the observation both fail."),
        ("Model a spatial level",
         "Compute the lesson's model of perceived tilt against a spatial level under a sudden "
         "and a gradual re-anchoring, and say which report each rule illustrates and what the "
         "model leaves out."),
        ("State the chapters' claims at strength",
         "State the views the chapters answer, Berkeley, the Cartesians, Kant, the "
         "associationists, the Gestalt psychologists and the logician of movement, and the "
         "chapters' reply to each."),
    ],
    "syllabus_intro": (
        "Eight lessons follow the book's order: the introduction to Part Two, Sense "
        "Experience in three lessons, and Space in four, one for each of its sections."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with a short passage and "
        "then goes back through the section a paragraph at a time, so read the whole section "
        "in your own copy first. Quotations are from Colin Smith's translation (Routledge "
        "Classics), short extracts quoted for commentary, and page numbers are that "
        "edition's.",
        "Find the sections of Space by their first sentences. Smith prints no headings inside "
        "that chapter; each lesson gives the page and the sentence where its section begins "
        "and ends.",
        "Read each figure as a model's. The labs compute the classical theories' predictions, "
        "one model the lesson builds itself, and counts over the lesson's coding of the "
        "cases; every panel says which, and none of them is a report of what anyone sees.",
        "Watch whose voice a sentence is in. These chapters let an objector, a logician or a "
        "psychologist speak for a page before answering. Each lesson says whose view a "
        "sentence states, and the cases are the reports of the book's clinical sources.",
    ],
    "not_covered": [
        "The later state of the experiments. Goldstein and Rosenthal's colour effects, "
        "Stratton's spectacles, Wertheimer's mirror and stroboscopic movement and von "
        "Senden's reports are read as the chapters report them; the later research on each is "
        "not followed, and this course sets no modern view beside the chapters.",
        "Kant, Berkeley, Descartes and Malebranche in their own texts. Each appears where the "
        "chapters argue with him, briefly and at his strongest.",
        "The temporal synthesis. The last pages of Sense Experience and several pages of Space "
        "say that the unity of perception is temporal; the lessons name the claim, and The "
        "Cogito, Time and Freedom reads it in Temporality.",
        "The closing pages of Space on illusion and the cogito, which are summarized in “Lived "
        "Space” and taken up in the courses that follow.",
        "Merleau-Ponty's other works, including The Structure of Behaviour, which these "
        "chapters cite.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "a face's drawn area from a whole-number direction, a pure quality's prediction, a "
        "core by intersecting the lesson's coding, tilt against the lesson's model of a level, "
        "convergence as a separation over a distance, a speed as a separation over an "
        "interval, and a record by counting the lesson's coding of the cases. Clinical and "
        "experimental figures are illustrative unless a label says otherwise. None of them is "
        "an experience, which is what these chapters are about."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
