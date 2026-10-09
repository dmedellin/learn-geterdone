# -*- coding: utf-8 -*-
"""Course three: where the words go, and how that can be checked without tags."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B
from .part_c import LESSONS as _C

COURSE = {
    "slug": "word-order",
    "number": 3,
    "title": "Word Order",
    "level": "Foundational",
    "blurb": (
        "English does not mark who does what with word endings. It marks it with "
        "position, and with the shape of the <dfn>pronoun</dfn> &mdash; <em>he</em> "
        "against <em>him</em>. That makes the order rules checkable on ordinary "
        "printed text, with nothing marked up by hand, and this course checks "
        "them."
    ),
    "summary": (
        "If your first language can move words about freely because the endings "
        "say who did what, English will feel rigid. It is rigid, and this course "
        "measures how rigid. Three rules are stated and scored on printed text: "
        "where a pronoun sits beside its verb, where an <dfn>adverb</dfn> sits, and how a "
        "question opens. Two of the three hold. The third covers only half of "
        "the questions people actually ask, and the course prints the other "
        "half rather than quietly dropping the rule."
    ),
    "assumes_short": "Tense Tables and Irregular Verbs, because a verb has to exist before you can ask where it goes.",
    "assumes_long": (
        "The two courses before this one. The scans here look for a verb next to "
        "a pronoun, so they need the forms Tense Tables builds and the broken ones "
        "Irregular Verbs lists. Nothing else is assumed, and the number work is still "
        "counting and working out a share."
    ),
    "how_to": [
        "Read the printed text before you read the number. Every figure in a lab "
        "here is counted from words printed on the same page, and the point is "
        "that you can check a row and disagree with it. Where a lesson quotes a "
        "count made over the whole novel, which no page can carry, it says so "
        "beside the figure.",
        "Treat what is left over as the lesson. A rule that holds nine times in ten "
        "is only useful if you know what the tenth looks like, and each lesson "
        "names what is left rather than rounding it away.",
        "Remember the book is old. The text these rules are scored on was "
        "written in 1813, and where that changes an answer the lesson says so.",
    ],
    "outcomes_intro": (
        "By the end you can state three rules about English order, say how often "
        "each holds on real text, and describe what the leftovers are made of."
    ),
    "outcomes": [
        ("Say why English can afford a fixed order",
         "Because the pronoun itself carries the job: <em>he</em> and "
         "<em>him</em> are not the same word, so position and shape agree."),
        ("Score the order rule without marking anything up",
         "A subject pronoun followed by its verb, counted over printed text, with "
         "nothing marked, no trees, nothing decided by hand."),
        ("Read what is left over and say which kind it is",
         "A missing word, a word that comes between, or the one real turn-around "
         "English keeps &mdash; and they are not the same thing."),
        ("Put a frequency adverb where it belongs",
         "In the middle: before the main verb, after the first helping verb, after "
         "<em>be</em>, scored on 120 printed lines."),
        ("Say what a question actually looks like",
         "Starting with a helping verb covers about half of them. The lesson gives "
         "the rule, shows it failing, and shows what the other half do."),
        ("Know why a course book leaves you unready to talk",
         "Modern formal writing barely contains these shapes. That gap is "
         "measured, not simply claimed."),
    ],
    "syllabus_intro": (
        "Pronouns first, because they are what makes the order checkable at all. "
        "Then adverbs, where the rule is weaker. Then questions, where it breaks."
    ),
    "not_covered": [
        "Sentences with more than one clause. Everything scored here is a "
        "pronoun and the word beside it. Where two clauses join, the scan stops, "
        "and the lesson says how often that happens rather than guessing at it.",
        "Which order sounds better. Several orders are allowed and one is "
        "normal; that difference is a matter of what writers do, and nothing on "
        "this page measures it.",
        "Spoken English. Every figure is from printed text. Speech moves words "
        "about far more freely, and a course that measured writing and talked "
        "about speech would be claiming something it had not checked.",
        "Modern usage, mostly. The text is from 1813. Two modern public-domain "
        "passages are measured for comparison and they turn out to contain "
        "almost none of these shapes, which is itself one of the findings.",
    ],
    "key": [
        "he or him     she or her     they or them",
        "the word changes with the job",
        "",
        "subject pronoun then its verb   90.0%",
        "adverb in the middle            70.8%",
        "question opens with a helper    53.3%",
        "",
        "what is left is words, not order",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure in a lab on "
        "this course is counted in your browser over text printed on the same "
        "page; where a lesson quotes a count made over the whole novel, which no "
        "page can carry, it says so beside the figure. The text is <em>Pride and "
        "Prejudice</em> (1813), public domain, novel text only, and two modern "
        "public-domain documents, named where they are counted."
    ),
    "lessons": list(_A) + list(_B) + list(_C),
}
