"""Course 6 -- Things, the World and Others: Part Two, Chapters 3-4 (Smith pp. 348-425).

Seven lessons in two modules' worth of chapters: part_a holds the first four
(Chapter 3's constancies of size and of colour, the thing, the natural world),
part_b the last three (hallucination, which closes Chapter 3, and the two
lessons on Chapter 4).
"""

from . import part_a, part_b

COURSE = {
    "slug": "perception-things-world-and-others",
    "title": "Things, the World and Others",
    "level": "Advanced",
    "summary": (
        "Part Two, The World as Perceived, Chapters 3 and 4: The Thing and the Natural "
        "World, and Other Selves and the Human World. Merleau-Ponty asks what it is for "
        "something to be real, starting from the constancies of size, shape and colour, "
        "and goes on to the thing, the world as the horizon of all horizons, and the "
        "hallucinations that lack what perception has. He then turns to cultural objects "
        "and other people, the argument from analogy, and a solipsism that he says cannot "
        "be overcome and does not have the last word."
    ),
    "blurb": (
        "Compute what two classical models predict for the size of a distant person and "
        "the colour of Gelb's disc, count two opponents' records over the chapter's "
        "observations about things and about other people, follow the cues by which a "
        "town on the horizon is identified, find what every perceived thing has and a "
        "hallucination lacks, and test the argument from analogy for validity."
    ),
    "key": [
        "inferred = retinal × distance / standard",
        "luminance = reflectance × illumination",
        "the thing: one style in all its qualities",
        "the world: the horizon of all horizons",
        "hallucination: no path to the rest",
        "analogy presupposes what it explains",
        "solitude and communication: one phenomenon",
    ],
    "assumes_short": "Sensing and Space",
    "assumes_long": (
        "the courses before it, especially Classical Prejudices for empiricism and "
        "intellectualism and Sensing and Space for the senses and the spatial level; the "
        "labs need fractions and nothing else"
    ),
    "outcomes_intro": (
        "By the end you can say, in the chapters' terms, what makes a thing real and "
        "another person present, and do the arithmetic each lab asks for."
    ),
    "outcomes": [
        ("Compute two predictions of constancy",
         "From a size, distances and an assumed distance, compute the retinal-image and "
         "inference predictions and Brunswik's ratio, and from reflectances and "
         "illuminations compute luminances and ratios to a surround."),
        ("Count two accounts against the cases",
         "From a coded table of the chapters' observations, compute each opponent's record, "
         "the observations on which two accounts part, and whether either absorbs them all."),
        ("Follow an interpretation from cues",
         "Count the interpretations a sequence of cues leaves standing, and say what was "
         "never among the candidates."),
        ("Find what perception has and hallucination lacks",
         "Compute the core of a coded set of perceived things and say which of its "
         "properties a reported hallucination lacks."),
        ("Test the argument from analogy",
         "Set out the argument in sentence letters, decide whether its premises force its "
         "conclusion, and say why the chapter's objection is not that it is invalid."),
        ("State the chapters' claims at strength",
         "State the psychologist's, Kant's, the empiricist's, the intellectualist's and the "
         "objectifying look's accounts in their own terms, and the chapters' reply to each."),
    ],
    "syllabus_intro": (
        "Seven lessons follow the two chapters in their order: five for Chapter 3 "
        "(constancies of size and shape, colour and lighting, the thing, the natural "
        "world, hallucination) and two for Chapter 4 (the cultural world and the argument "
        "from analogy, then the truth of solipsism and the social world)."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with a short passage "
        "and then goes back through the section a phrase at a time, so read the pages each "
        "lesson names in your own copy first. Quotations are from Colin Smith's translation "
        "(Routledge Classics), short extracts quoted for commentary, and page numbers are "
        "that edition's.",
        "Watch whose voice a sentence is in. These chapters state the psychologist's, "
        "Kant's and the objectifying look's views in their own words, some of them at "
        "length, before answering them, and a sentence lifted from those pages can say the opposite of "
        "what the chapter concludes. Each lesson says whose view it is reporting.",
        "Read every figure as a model's. The size and light labs compute what classical "
        "theories predict; the tables count the lesson's coding of the chapters' cases. "
        "None of them computes what a thing or a person is like for someone who perceives "
        "them, which is what the chapters describe.",
        "Treat the patients as the book does. The hallucination lesson rests on clinical "
        "reports the book takes from its sources; the lab codes the reports, not the people "
        "they describe.",
    ],
    "not_covered": [
        "Sartre's <em>Being and Nothingness</em> (1943). The view that the other's look "
        "makes me an object is widely read as Sartre's, and the chapter answers it without "
        "naming him; the lesson states it at strength and does not read Sartre's book.",
        "Scheler, Husserl and Hegel on other minds. Scheler and Hegel are named where the "
        "chapter draws on them, in a sentence; Husserl's Fifth Cartesian Meditation, which "
        "the chapter's problem recalls, is not read.",
        "The psychology of constancy beyond the chapter. Brunswik's ratio and Wallach's ratio "
        "principle are used as the lessons' additions; the later experimental literature "
        "on size and lightness constancy is not surveyed.",
        "The modern dispute over hallucination and prediction. One aside in the "
        "Hallucination lesson sets the chapter beside Anil Seth's description of perception "
        "as controlled hallucination, with both sides stated; the dispute is not settled.",
        "The chapter's pages on touch and weight, and Chapter 4's pages on history and "
        "class. The lessons summarise them where they bear on the argument and do not read "
        "them line by line.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: a size times a ratio of distances, a reflectance times an illumination, a "
        "count over the lesson's coding of the chapters' cases, a core by intersecting coded "
        "properties, a truth table. The distances, reflectances and reported sizes are "
        "illustrative. None of them is a thing or a person as perceived, which is what the "
        "chapters are about."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
