"""Course 2 -- Classical Prejudices: the Introduction (Smith pp. 3-74).

Five lessons: Chapter 1 in two (pure sensation; the constancy hypothesis), then
one lesson each for Chapters 2, 3 and 4. part_a holds all five.
"""

from . import part_a

COURSE = {
    "slug": "perception-classical-prejudices",
    "title": "Classical Prejudices",
    "level": "Beginner",
    "summary": (
        "The Introduction, Traditional Prejudices and the Return to Phenomena, in its four "
        "chapters: 1 The &lsquo;Sensation&rsquo; as a Unit of Experience, 2 "
        "&lsquo;Association&rsquo; and the &lsquo;Projection of Memories&rsquo;, 3 "
        "&lsquo;Attention&rsquo; and &lsquo;Judgement&rsquo;, and 4 The Phenomenal Field. "
        "Merleau-Ponty builds up the two classical theories of perception, empiricism and "
        "intellectualism, and takes them apart, to show that they fail together, from one "
        "shared prejudice in favour of the objective world. The labs compute what those "
        "theories predict, and in the last lesson count the lesson's coding of the "
        "Introduction's cases."
    ),
    "blurb": (
        "Read the Introduction a chapter at a time. Compute how proximity groups a row of "
        "dots, what the constancy hypothesis predicts for two equal lines, how many "
        "remembered words fit a misprint, when a judgement from signs can conclude that the "
        "forms on the shore are a ship, and where the two classical accounts part."
    ),
    "key": [
        "empiricism: sensations plus association",
        "intellectualism: sensations plus judgement",
        "constancy: one stimulus, one sensation",
        "predicted = a − b",
        "recall needs a shape already there",
        "attention creates nothing, for both",
        "both assume the objective world",
    ],
    "assumes_short": "What Phenomenology Is",
    "assumes_long": (
        "what phenomenology is, from the Preface's idea of description, and nothing else; "
        "school arithmetic is enough for the labs"
    ),
    "outcomes_intro": (
        "By the end you can state each classical account of perception at its strongest, "
        "give the Introduction's reply to it, and do the lab's arithmetic for each."
    ),
    "outcomes": [
        ("Find what is in no single element",
         "Compute the groups the proximity rule gives a row of dots, and say what a "
         "pure-sensation account would have to add to obtain them."),
        ("Compute the constancy hypothesis's prediction",
         "From two measured magnitudes and a reported difference, compute the prediction and "
         "the signed gap, and state why the chapter does not call the gap a mistake."),
        ("Count the memories that fit",
         "From a list of remembered words, a pattern of seen letters and a context, count and "
         "list the words that fit, and say what selected them."),
        ("Run a judgement from signs",
         "Given interpretations and ordered cues, compute what the model keeps at each step "
         "and where it decides, and set that beside the book's description of the walk "
         "towards the ship."),
        ("Read the accounts' record",
         "From a coded table of cases, compute each account's record, the survivors and the "
         "split, and state the prejudice the Introduction says both accounts share."),
    ],
    "syllabus_intro": (
        "Five lessons in the Introduction's order: the first chapter in two, on pure "
        "sensation and on the constancy hypothesis, then association and memory, attention "
        "and judgement, and the phenomenal field."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with a short passage "
        "and then goes back through the chapter a phrase at a time, so read the whole "
        "chapter in your own copy first. Quotations are from Colin Smith's translation "
        "(Routledge Classics), short extracts quoted for commentary, and page numbers are "
        "that edition's.",
        "Watch whose voice a sentence is in. Merleau-Ponty states empiricism and "
        "intellectualism at length, often in their own words and examples, before he answers "
        "them. The cardboard tube held up to the moon is Alain's test, not his, and each "
        "lesson says whose view it is reporting.",
        "Read each figure as a prediction, and say whose. The labs compute what a theory the "
        "Introduction argues against would predict, or count the lesson's coding of the "
        "cases. None of them computes what anyone sees, and the Introduction's claim is "
        "that no such figure could.",
        "Expect the argument to be cumulative. The first two chapters are aimed at "
        "empiricism, the third at intellectualism, and the fourth gathers them; the lesson "
        "on the phenomenal field reads best after the other four.",
    ],
    "not_covered": [
        "The Introduction's long footnotes. Several carry real argument, on Jaspers, on "
        "Alain's analysis of size and on the relation of Gestalt psychology to Husserl; the "
        "lessons mention them where they bear on a passage and do not read them through.",
        "The psychology as later science judged it. The experiments the Introduction cites, "
        "Köhler's, Lewin's, Gottschaldt's and the rest, are taken as the book reports them; "
        "their later fortunes are not followed, and the lab figures are illustrative.",
        "Descartes, Kant, Bergson and the French intellectualists in their own books. Each "
        "appears where the Introduction argues with him, at his strongest, but the "
        "Meditations, the Critique and Alain's essays are not read.",
        "The transcendental question the last chapter leaves open, the relation of the "
        "phenomenal field to the transcendental one. The Introduction defers it to Part "
        "Three, and so does this Subject.",
        "Merleau-Ponty's other works. The Structure of Behaviour, which the Introduction "
        "cites throughout, is not read.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "groups from gaps between dots, a predicted difference from two lengths, the "
        "remembered words that fit a pattern, the interpretations a run of cues leaves, and "
        "a count over the lesson's coding of the Introduction's cases. The magnitudes are "
        "illustrative. None of them is a perception, which is what the Introduction argues."
    ),
    "lessons": part_a.LESSONS,
}
