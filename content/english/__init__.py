# -*- coding: utf-8 -*-
"""English for speakers of other languages.

WHAT THIS SUBJECT CLAIMS, and the test every lesson has to pass. Elsewhere on
this site a lab computes a number from a definition the lesson states. Here the
definition is a RULE OF ENGLISH and the number is the share of real words the
rule gets right, with the words it misses printed beside it. Every lesson is
"state a rule, measure it on printed text, show what is left over", and a
lesson that cannot be written that way does not ship.

WHAT THAT LEAVES OUT, said here rather than discovered later. Knowing when to
use the present perfect, what an idiom means, or how polite to be is
explanation, and explanation does not compute. Those are named in each course's
`not_covered` rather than given a lab that only looks like one.

THE BAND. Every page of this Subject is written inside the 2,809 headwords of
the New General Service List plus a short glossary defined where it first
appears, and `scripts/bandcheck.py` refuses the build below 98%. The first
course teaches that 98% is the coverage a reader needs; a page that teaches it
and misses it has failed its own lesson.

DATA AND LICENCE. Word lists are the NGSL 1.2 (Browne, Culligan and Phillips),
CC BY-SA 4.0. Pronunciations are CMUdict, BSD-2. Passages are public domain.
Published research figures -- Nation's coverage thresholds, Biber's frequency
counts -- are QUOTED in the prose and never embedded as data, which keeps every
shipped byte permissively licensed.
"""

from .c1_tense_tables import COURSE as _C1
from .c2_irregular_verbs import COURSE as _C2
from .c3_word_order import COURSE as _C3

PATH = {
    "slug": "english",
    "title": "English",
    "level": "Foundational",
    "level_note": "no earlier course on this site is assumed; the number work never goes past counting",
    "tagline": (
        "Every rule you have been given about English, with the one thing no "
        "book prints beside it &mdash; how often it is actually right, and the "
        "words it gets wrong."
    ),
    "description": (
        "English for speakers of other languages, built the way the rest of this "
        "site is built: a rule is stated, run over real printed words in your "
        "browser, and scored. Written inside the 2,800 most common words of "
        "English, with every other word explained where it first appears."
    ),
    "key": [
        "a rule, the share it gets right,",
        "and the words it misses",
        "",
        "-s 99.85%    -ing 98.97%    -ed 98.67%",
        "",
        "four of the twelve tense boxes",
        "carry most of real writing",
    ],
    "sequence_intro": (
        "Three courses, in one order, and each one needs the last. The first builds any "
        "verb's forms from rules. The second takes the verbs that break those "
        "rules. The third puts the verb in a sentence and asks where everything "
        "else goes."
    ),
    "why_order": [
        "Tense Tables comes first because every later lesson needs the forms it "
        "builds, and because it is the lesson that shows what this Subject does "
        "differently: a rule arrives with a hit rate and a list of exceptions "
        "rather than on its own.",
        "Irregular Verbs comes second because it is the exception list the first "
        "course keeps pointing at, and because it is short &mdash; the verbs that "
        "break the rules are few, and a small number of them carry most of the "
        "trouble.",
        "Word Order comes last because it needs a verb before it can ask where "
        "the verb goes, and because its method is borrowed from the first "
        "course: English marks who is doing the action in the little words like "
        "<em>he</em> and <em>him</em>, so the rule can be checked on printed "
        "words with nothing marked up by hand.",
    ],
    "prerequisites": [
        "The ability to read this page. The writing is kept inside the 2,800 "
        "most frequent words of English and every other word is defined where it "
        "first appears, but it is still English, and a reader at the very "
        "beginning will want a teacher as well as a page.",
        "Counting, and working out a share. Nothing here needs more number work "
        "than that, and no earlier course on this site is assumed.",
    ],
    "material": (
        "every figure on this path is computed in your browser from the rule the "
        "lesson states, run over the words printed on the page, so a hit rate is "
        "something you can check by hand rather than something you are told"
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path "
        "is computed in your browser from the rule the lesson states, run over "
        "the words printed on the page. Word lists are the New General Service "
        "List (Browne, Culligan and Phillips), CC BY-SA 4.0; pronunciations are "
        "CMUdict; passages are public domain."
    ),
    "courses": [_C1, _C2, _C3],
}
