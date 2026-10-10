# -*- coding: utf-8 -*-
"""Word Order, the fifth course on the path: where the words go, and how that
can be checked without tags. The package keeps its old name, c3_word_order;
the path puts it fifth and sets its number."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B
from .part_c import LESSONS as _C

COURSE = {
    "slug": "word-order",
    "title": "Word Order",
    "level": "Foundational",
    "blurb": (
        "English does not mark who does what with word endings. It marks it with "
        "position, and with the shape of the <dfn>pronoun</dfn> &mdash; <em>he</em> "
        "against <em>him</em>. That makes the order rules checkable on ordinary "
        "printed text, with nothing marked up by hand, and this course checks "
        "them, on a novel and on a play."
    ),
    "summary": (
        "If your first language can move words about freely because the endings "
        "say who did what, English will feel rigid. It is rigid, and this course "
        "measures how rigid. Three rules are stated and scored on printed text: "
        "where a pronoun sits beside its verb, where an <dfn>adverb</dfn> sits, "
        "and how a question opens. The first two hold. The third covers a little "
        "over half of the questions in a novel and about a third of the questions "
        "in a play, and the course prints the rest, sorted into kinds, rather "
        "than quietly dropping the rule."
    ),
    "assumes_short": "Tense Tables, Irregular Verbs and Helping Verbs, because a verb has to exist, and a helping verb has to be known, before you can ask where either goes.",
    "assumes_long": (
        "The three courses before this one. The scans here look for a verb next to "
        "a pronoun, so they need the forms Tense Tables builds and the broken ones "
        "Irregular Verbs lists. The adverb rule puts a word after a helping verb, "
        "and the question rule moves one; Helping Verbs introduces them. Nothing "
        "else is assumed, and the number work is still counting and working out a "
        "share."
    ),
    "how_to": [
        "Read the printed text before you read the number. Every figure in a lab "
        "here is counted from words printed on the same page, and the point is "
        "that you can check a row and disagree with it. Where a lesson quotes a "
        "count made over a whole text, which no page can carry, it says so "
        "beside the figure.",
        "Treat what is left over as the lesson. A rule that holds nine times in ten "
        "is only useful if you know what the tenth looks like, and each lesson "
        "names what is left rather than rounding it away.",
        "Remember the texts are old. The novel was written in 1813 and the play "
        "in 1895, and where that changes an answer the lesson says so.",
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
        ("Build a question, and say how often real ones follow the rule",
         "A helping verb in front of the subject, or <em>do</em> added. It "
         "covers 57.8% of 90 questions from a novel and 34.8% of 256 from a play."),
        ("Name the kinds of question the rule leaves out",
         "A joining word first, a name first, a pronoun first, a question word "
         "with no helping verb after it, and a few words with no verb."),
    ],
    "syllabus_intro": (
        "Pronouns first, because they are what makes the order checkable at all. "
        "Then adverbs, where the rule is weaker. Then questions, scored twice: on "
        "a novel, where the rule covers over half, and on a play, where it covers "
        "a third."
    ),
    "not_covered": [
        "Sentences with more than one clause. Everything scored here is a "
        "pronoun and the word beside it, or the first words of a question. "
        "Where two clauses join, the scan stops, and the lesson says how often "
        "that happens rather than guessing at it.",
        "Question tags, such as <em>isn&rsquo;t it?</em> at the end of a "
        "statement. The novel has 7 and the play 19, quoted, so few that a count "
        "over them would be a list and not a measure. Where a printed question "
        "carries one, the lab sorts the line by its first words like any other, "
        "and How People Really Ask names the kind; no lesson scores the tag "
        "itself.",
        "Which order sounds better. Several orders are allowed and one is "
        "normal; that difference is a matter of what writers do, and nothing on "
        "this page measures it.",
        "Recorded speech. A play is written to be said, but every line in it was "
        "made up by a writer, and every figure is from printed text. A course "
        "that measured a script and talked about speech would be claiming "
        "something it had not checked.",
    ],
    "key": [
        "he or him     she or her     they or them",
        "the word changes with the job",
        "",
        "subject pronoun then its verb   90.0%",
        "adverb in the middle            70.8%",
        "question opens with a helper:",
        "  in a novel, 90 questions      57.8%",
        "  in a play, 256 questions      34.8%",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure in a lab on "
        "this course is counted in your browser over text printed on the same "
        "page; where a lesson quotes a count made over a whole text, which no "
        "page can carry, it says so beside the figure. The texts are <em>Pride "
        "and Prejudice</em> (1813) and <em>The Importance of Being Earnest</em> "
        "(1895), both public domain, from Project Gutenberg, and two modern "
        "public-domain documents, named where they are counted. The verb lists "
        "are adapted from the New General Service List (Browne, Culligan and "
        "Phillips) and are shared under CC BY-SA 4.0."
    ),
    "lessons": list(_A) + list(_B) + list(_C),
}
