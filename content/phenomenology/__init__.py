"""The Phenomenology path, as data: a read-along of Merleau-Ponty's *Phenomenology of Perception*.

Seven courses in the book's order, from the Preface to Freedom. Each lesson
quotes a short passage from Colin Smith's translation (Routledge Classics
pagination; the book is in copyright, so quotation is kept small) and computes,
in the phenkit lab, what a theory Merleau-Ponty argues against predicts. The
design is docs/phenomenology/PLAN.md.
"""

from . import (
    c1_preface,
    c2_prejudices,
    c3_lived_body,
    c4_expressive_body,
    c5_sensing_space,
    c6_things_others,
    c7_cogito_time_freedom,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_preface.COURSE,
    c2_prejudices.COURSE,
    c3_lived_body.COURSE,
    c4_expressive_body.COURSE,
    c5_sensing_space.COURSE,
    c6_things_others.COURSE,
    c7_cogito_time_freedom.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "phenomenology",
    "title": "Phenomenology of Perception, Read Along",
    "level": "Beginner \u2192 Advanced",
    "level_note": "no philosophy is assumed; school geometry is enough for the labs",
    "tagline": (
        'Maurice Merleau-Ponty&rsquo;s <em>Phenomenology of Perception</em>, read section by section from the Preface to Freedom &mdash; with the predictions of the theories he argues against computed in front of you, so that what perception gives can be seen beside them. Seven courses and 44 lessons are available.'
    ),
    "description": (
        "The Phenomenology Subject: a read-along of Merleau-Ponty's 1945 book in its own order, seven courses that follow its Preface, Introduction and three Parts. Each lesson reads a short passage first, then explains it line by line, then computes what a classical theory of perception predicts &mdash; the length of two lines, the size of a person across a room, the colour of a spotlit disc, the motion between two lights &mdash; or finds the clinical observation on which the classical accounts part. All seven courses and 44 lessons are available."
    ),
    "key": ['angular size = size / distance', 'luminance = reflectance × illumination', "ratio = luminance / surround's luminance", 'perceived tilt = image tilt − spatial level', 'motion seen: lights alternate in the band', 'an account survives if no case refutes it', 'a ∠ sum = two right angles, by a parallel'],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. Classical Prejudices uses the Preface's idea of description; The Lived Body uses the Introduction's two opponents; The Expressive Body extends the body schema; Sensing and Space and Things, the World and Others re-read perception from the body; The Cogito, Time and Freedom uses all of it."
    ),
    "why_order": ["The order is the book's, and it is the order of an argument. The Preface says what phenomenology is; the Introduction clears away two theories of perception; Part One finds, in the lived body, what both of them missed; Part Two re-reads sensing, space, things and other people from there; Part Three asks what this makes of the thinking subject, of time and of freedom.", 'The Introduction comes before the body because the body is the answer to a question the Introduction poses: if perception is neither a sum of sensations nor a judgement, what is it? Read first, Part One looks like a collection of clinical curiosities; read second, every case is an argument.', "Part Three comes last because Merleau-Ponty wants the reader to have lived through the perceived world before being told what it implies about the cogito. The book's claims about freedom rest on its claims about the body and about time, and he says so.", 'The Preface is the hardest place to begin, and the Subject begins there only because the book does. It can be read again after the book, and Classical Prejudices does not depend on its labs.'],
    "prerequisites": ['No philosophy. The Subject introduces Descartes, Kant, Husserl, Heidegger, Scheler, Cassirer, Bergson, Sartre and the psychologists — the Gestalt school (Köhler, Koffka, Wertheimer), Gelb and Goldstein, Stratton, Binswanger, Minkowski — at the moment Merleau-Ponty argues with them or draws on them, at their strongest. Words he uses in a sense of his own (*the body proper*, *motor intentionality*, *the phenomenal field*, *being-in-the-world*, which he takes from Heidegger) are defined in the lesson that introduces them.', 'School geometry: a ratio, a right angle, the angles of a triangle, a point on a grid. The labs do the arithmetic; what is asked of you is to say what each figure is a prediction of, and whose.', "A copy of the book is strongly recommended. The book is in copyright, so a lesson quotes only a short passage and the phrases it reads closely, with page references to Colin Smith's translation (Routledge Classics, 2002, the 1962 translation repaginated), the one translation every lesson cites. The rest is paraphrase, and a paraphrase is a reading: check it against the page.", "Patience with a style. Merleau-Ponty writes long, looping paragraphs that state an opponent's view in its own words for pages before turning on it. A sentence quoted out of its paragraph can say the opposite of what he means; every lesson says whose voice a quoted sentence is in."],
    # Each path names its own hazard. This one's is that perception is not a
    # figure, and every figure here is a model's.
    "material": (
        "every figure on this path is what a stated model of perception predicts from a stated stimulus, or a count over the cases a lesson sets out, or a lesson's own illustration, computed in your browser &mdash; and what perception gives is not a figure, which is the claim the book argues and the lab cannot settle."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what the lesson states: an angular size is a size over a distance, a luminance is a reflectance times an illumination, an account's record is a count over the cases. Nothing is rounded except where a lesson says so. Quotations are short extracts from Colin Smith&rsquo;s translation, quoted for commentary. What the labs cannot do is compute an experience &mdash; and that is what the book is about."
    ),
    "courses": COURSES,
}
