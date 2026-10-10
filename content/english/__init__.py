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

from .c1_tense_tables import COURSE as _C1_TENSE_TABLES
from .c2_irregular_verbs import COURSE as _C2_IRREGULAR_VERBS
from .c5_helping_verbs import COURSE as _C5_HELPING_VERBS
from .c6_nouns_articles import COURSE as _C6_NOUNS_ARTICLES
from .c3_word_order import COURSE as _C3_WORD_ORDER
from .c7_small_words import COURSE as _C7_SMALL_WORDS
from .c8_spelling_sound import COURSE as _C8_SPELLING_SOUND
from .c9_word_stress import COURSE as _C9_WORD_STRESS
from .c4_listening import COURSE as _C4_LISTENING
from .c10_vocabulary import COURSE as _C10_VOCABULARY

# Path order (docs/english-v2/PLAN.md): Helping Verbs before Word Order, which
# assumes it. A course still being authored exports COURSE = None and is
# filtered here, so it is visible in the source and cannot be forgotten.
_ORDER = [_C1_TENSE_TABLES, _C2_IRREGULAR_VERBS, _C5_HELPING_VERBS, _C6_NOUNS_ARTICLES, _C3_WORD_ORDER, _C7_SMALL_WORDS, _C8_SPELLING_SOUND, _C9_WORD_STRESS, _C4_LISTENING, _C10_VOCABULARY]

# A course's number is its position on the path, never its package prefix:
# c3_word_order is fifth and c4_listening is ninth.
COURSES = [c for c in _ORDER if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

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
        "English, with every other word explained where it first appears. "
        "Ten courses and 41 lessons."
    ),
    "key": [
        "a rule, the share it gets right,",
        "and the words it misses",
        "",
        "-s 99.92%    -ing 99.34%    -ed 99.26%",
        "",
        "a or an by sound, not letter: 493 of 493",
        "i before e, except after c: 36 of 58",
    ],
    "sequence_intro": (
        "Ten courses. The first six are grammar and are in one order: the forms "
        "of a verb, then the verbs that break the rules for them, then the "
        "helping verbs that stand in front of a verb, then nouns and the little "
        "words before them, then where everything goes in a sentence, then the "
        "small words and comparisons. The next three are about sound &mdash; "
        "how a spelling is said, where the strong part of a word falls, and "
        "what a listener actually hears &mdash; and can be read apart from the "
        "first six, Listening first if you want help hearing English before "
        "anything else. The tenth uses every rule before it. These ten are the "
        "whole Subject as published: a new course is added only when its rule "
        "can be run over printed words and scored the same way, and nothing is "
        "announced before its page exists."
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
        "Helping Verbs comes third because <em>be</em>, <em>have</em> and "
        "<em>do</em> take the forms the first two courses build, and before Word "
        "Order because the adverb and question rules move a helping verb, and a "
        "reader should have met one first.",
        "Nouns and Articles comes fourth because its plural rule is the same "
        "<em>-s</em> rule the first course scores on verbs, now run on nouns.",
        "Word Order comes fifth because it needs a verb, a helping verb and a "
        "noun before it can ask where each one goes, and because its method is "
        "borrowed from the first course: English marks who is doing the action "
        "in the little words like <em>he</em> and <em>him</em>, so the rule can "
        "be checked on printed words with nothing marked up by hand.",
        "Small Words and Comparisons comes sixth and closes the grammar: its "
        "rules are about the short words around nouns and verbs, and its "
        "comparisons lesson counts the parts of a word, which it explains where "
        "it needs them and which Word Stress takes further.",
        "Spelling to Sound comes seventh and begins the three courses about "
        "sound. It needs nothing from the grammar and can be read first: each "
        "rule takes a spelling to a sound and is scored on the 2,800 words.",
        "Word Stress comes eighth because it uses the sound marks Spelling to "
        "Sound explains, and the strong part of a verb that Tense Tables needed "
        "for its doubling rule.",
        "Listening comes ninth, and apart: it needs nothing from the other "
        "courses, Word Stress helps it, and a reader who wants help hearing "
        "English before anything else can start there.",
        "Vocabulary and Reading comes last because its lab is the other nine "
        "courses' rules run as a reading machine: it asks how much of a real "
        "page the 2,800 words cover, and a reader needs the rules that turn one "
        "listed word into its other forms first.",
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
        "every figure counted on this path is computed in your browser from the "
        "rule the lesson states, run over the words printed on the page, and the "
        "few figures taken from a whole novel are marked as quoted where they "
        "appear &mdash; so a hit rate is something you can check by hand rather "
        "than something you are told"
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure counted on "
        "this path is computed in your browser from the rule the lesson states, "
        "run over the words printed on the page; the few figures taken from a "
        "whole novel are marked as quoted where they appear. The word lists in "
        "these pages are adapted from the New General Service List (Browne, "
        "Culligan and Phillips) and, unlike the rest of this site, are shared "
        "under CC BY-SA 4.0. The older passages are public domain: <em>Pride and "
        "Prejudice</em> (1813) and <em>The Importance of Being Earnest</em> "
        "(1895). Pronunciation facts are from CMUdict (BSD licence); parts of "
        "speech were taken at build time from the Moby Part-of-Speech list "
        "(public domain) and checked against a dictionary, and no page carries "
        "either list. The two modern documents &mdash; <em>Stanley v. "
        "City of Sanford</em>, 606 U.S. 46 (2025), and the U.S. Census "
        "Bureau&rsquo;s &ldquo;U.S. Population Aging as Nation Turns 250&rdquo; "
        "(9 April 2026) &mdash; are works of the U.S. government."
    ),
    "courses": COURSES,
}
