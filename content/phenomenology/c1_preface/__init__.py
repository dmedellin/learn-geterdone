"""Course 1 -- What Phenomenology Is: the Preface (Smith pp. vii-xxiv).

Four lessons, one module: part_a follows the Preface's own themes, from
description through the reduction and essences to intentionality and
rationality.
"""

from . import part_a

COURSE = {
    "slug": "perception-what-phenomenology-is",
    "title": "What Phenomenology Is",
    "level": "Beginner",
    "summary": (
        "The Preface. Merleau-Ponty asks what phenomenology is and answers by working "
        "through its themes: description rather than explanation or analysis, the "
        "phenomenological reduction and why it cannot be completed, essences as a means "
        "of understanding existence, and intentionality and the rationality of "
        "perspectives that confirm one another. The Preface has no figures and no cases, "
        "so the four labs illustrate the method rather than computing the Preface's own "
        "examples."
    ),
    "blurb": (
        "Read the Preface slowly, a theme at a time. Compute the moon's angle at the "
        "horizon and overhead and say what the figures leave out, find what a drawing of "
        "a cube does not decide, compute what stays through a set of variations, and put "
        "several viewpoints on one cube to see how they fit."
    ),
    "key": [
        "describe; do not explain or analyse",
        "angular size = size / distance",
        "reduction: suspend, do not doubt",
        "no complete reduction is possible",
        "essence: a means, not the end",
        "core = what every variant keeps",
        "rationality: views confirm each other",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no philosophy and no earlier course is assumed, and school geometry is enough "
        "for the labs"
    ),
    "outcomes_intro": (
        "By the end you can say, in the Preface's terms, what each of its themes asks "
        "of a philosopher, and do the lab's arithmetic for each."
    ),
    "outcomes": [
        ("Separate a figure from a description",
         "Compute an angle subtended from a size and a distance, compare two such "
         "figures, and state which question they answer and which they leave to "
         "description."),
        ("Find what a drawing does not decide",
         "Compare a drawing's two readings edge for edge, decide how many solids it fits, "
         "and name what a viewer who saw one reading supplied."),
        ("Compute an invariant core",
         "From a coded set of variations, compute what every variant of the kind keeps, "
         "what varies and what each excluded variant lacks, and say what the core is for."),
        ("Compute what several views see",
         "Given whole-number view directions, compute the faces each sees and their "
         "foreshortening, the faces no view sees, and whether each report fits its "
         "direction."),
        ("State the Preface's claims at strength",
         "State the opponent each theme answers, scientific explanation, analytical "
         "reflection, Cartesian doubt, the Vienna Circle and the idealist's view from "
         "above, and the Preface's reply to each."),
    ],
    "syllabus_intro": (
        "Four lessons follow the Preface's own order: description, the reduction, "
        "essences, and intentionality with the rationality the Preface ends on."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with a short passage "
        "and then goes back through the section a phrase at a time, so read the whole "
        "section in your own copy first. Quotations are from Colin Smith's translation "
        "(Routledge Classics), short extracts quoted for commentary, and page numbers are "
        "that edition's.",
        "Expect the Preface to be hard. It is a summary of a book you have not yet read, "
        "and many readers find it clearer after the rest. You can read it again at the "
        "end, and Classical Prejudices does not depend on these labs.",
        "Use the labs as illustrations. The Preface has no figures and no cases, so the "
        "moon, the cube, the tone and the melody are the lessons' examples, and each lesson "
        "says what its lab computes and what it cannot.",
        "Watch whose voice a sentence is in. Merleau-Ponty often states a view he is "
        "about to reject in its own words, and the Preface reads Husserl in a way of its "
        "own. Each lesson says whose view it is reporting.",
    ],
    "not_covered": [
        "Husserl's own texts. The Preface reads Husserl through Eugen Fink and the "
        "unpublished manuscripts, and how far that reading is Husserl's is disputed. The "
        "lessons say so where it matters and do not try to settle it.",
        "Heidegger, Kant and Descartes at length. Each appears where the Preface argues "
        "with him, briefly and at his strongest; their own books are not read.",
        "The Preface's pages on history. The paragraphs on understanding a revolution or a "
        "doctrine from every angle at once are summarised in “Intentionality and "
        "Rationality”, not read line by line.",
        "Free variation as Husserl sets it out. The Preface names the eidetic reduction but "
        "does not describe the procedure; the lab's version is a simplified illustration.",
        "Merleau-Ponty's other works. The Structure of Behaviour and the late work in which "
        "he revised some of this book's claims are not read.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: an angle as a size over a distance, a drawing's readings by comparing "
        "edges, a core by intersecting the lesson's coding, a cube's faces from "
        "whole-number directions. The moon's figures are modern astronomy's; the rest are "
        "illustrative. None of them is an experience, which is what the Preface is about."
    ),
    "lessons": part_a.LESSONS,
}
