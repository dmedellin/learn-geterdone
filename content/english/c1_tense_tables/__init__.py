# -*- coding: utf-8 -*-
"""Course one of the English Subject: the tense table, generated rather than learned."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "tense-tables",
    "number": 1,
    "title": "Tense Tables",
    "level": "Foundational",
    "blurb": (
        "A book gives you twelve boxes and asks you to learn them. This course "
        "gives you five forms and four rules that build all twelve, then runs "
        "those rules over 1,210 real verbs in your browser and prints how often "
        "they are right and every word they miss."
    ),
    "summary": (
        "The tense table is not twelve things to remember. It is five forms of a "
        "verb, four of which follow rules, placed behind <em>have</em>, "
        "<em>be</em> and <em>will</em>. This course states the rules, measures "
        "them on the page, and shows their exceptions &mdash; including the three "
        "that turned out to be mistakes in the word list rather than in English."
    ),
    "assumes_short": "Nothing. You need to read English and to count.",
    "assumes_long": (
        "No course on this site comes before this one. The arithmetic never goes "
        "past counting and working out a share, and every word list a lab uses "
        "is printed on the page you are reading."
    ),
    "how_to": [
        "Say the rule out loud before you look at the answer. The lab names the "
        "rule beside every form it makes, so you can check whether you had the "
        "right reason and not only the right word.",
        "Type verbs that are not in the list. The rules run on anything, and the "
        "ones that go wrong are more useful to you than the ones that go right.",
        "Read the misses. Each list of missed words is short enough to learn "
        "directly, and that is the whole saving: a rule plus a short list beats "
        "a long list.",
    ],
    "outcomes_intro": (
        "By the end you can build the full table for a verb you have never seen, "
        "say which rule made each form, and name the cases where the rules fail."
    ),
    "outcomes": [
        ("Build any verb's table from five forms",
         "The twelve boxes written out from the base form, with <em>have</em>, "
         "<em>be</em> and <em>will</em> doing the work that ten of them need."),
        ("Say which rule made a form, not just what the form is",
         "Each ending named as it is applied &mdash; the hiss rule, the "
         "<em>-y</em> rule, the silent <em>-e</em>, the doubling rule and the "
         "stress it depends on."),
        ("Quote a hit rate for every rule you use",
         "99.92% for <em>-s</em>, 99.34% for <em>-ing</em>, 99.26% for the past, "
         "measured on the page against 1,210 verbs and their recorded forms."),
        ("Name the words each rule misses",
         "Short lists, printed, and several of them cases where British and "
         "American spelling differ and no rule could choose."),
        ("Tell a rule that helps from one that only sounds right",
         "The <em>-f</em> to <em>-ves</em> rule, added for good reasons, made "
         "the results worse. The count found it; the ear did not."),
        ("Tell a spelling difference from a mistake",
         "<em>Travelling</em> and <em>traveling</em> are both right. Eleven of "
         "the eighteen words the doubling rule still misses are this, and three "
         "words it once seemed to miss were wrong spellings in the list itself."),
    ],
    "syllabus_intro": (
        "The forms first, because every later lesson puts them behind a small "
        "word. Then the one rule that needs the sound of the word, scored on "
        "every verb it can touch."
    ),
    "not_covered": [
        "When to choose one box over another. That is a question about meaning, "
        "and no count on this page answers it. The labs show how to build every "
        "box and how often the rules that build it are right; choosing between "
        "boxes is the work of reading and being corrected, which a page cannot "
        "do for you.",
        "Speaking and listening. This course does not teach them. The doubling rule "
        "needs to know where the stress falls, and the page reads that from a "
        "printed list rather than pretending to say the word to you.",
        "Every irregular verb in English. The second course takes the ones that "
        "appear often enough to matter and says plainly how far down the list it "
        "goes.",
        "Rare and old forms. <em>Shall</em> as a plain future and the "
        "subjunctive are named where they turn up in the printed passages and "
        "otherwise left alone.",
    ],
    "key": [
        "five forms fill twelve boxes",
        "base   he, she, it   -ing   past   after have",
        "",
        "have + past form     looks back",
        "be + -ing form       still going on",
        "will + base          later",
        "",
        "-s 99.92%   -ing 99.34%   -ed 99.26%",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every form on this course "
        "is built in your browser by the rule named beside it, and every hit rate "
        "is counted on the page against the word list printed there. Word list: "
        "the New General Service List (Browne, Culligan and Phillips), CC BY-SA 4.0."
    ),
    "lessons": list(_A) + list(_B),
}
