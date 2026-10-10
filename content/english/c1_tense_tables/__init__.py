# -*- coding: utf-8 -*-
"""Course one of the English Subject: the tense table, generated rather than learned."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "tense-tables",
    "title": "Tense Tables",
    "level": "Foundational",
    "blurb": (
        "A book gives you twelve boxes and asks you to learn them. This course "
        "gives you five forms and four rules that build all twelve, then runs "
        "those rules over 1,210 real verbs in your browser and prints how often "
        "they are right and every word they miss. It ends with the sound of the "
        "two endings, which the spelling hides."
    ),
    "summary": (
        "The tense table is not twelve things to remember. It is five forms of a "
        "verb, four of which follow rules, placed behind <em>have</em>, "
        "<em>be</em> and <em>will</em>. This course states the rules, measures "
        "them on the page, and shows their exceptions &mdash; including the three "
        "that turned out to be mistakes in the word list rather than in English "
        "&mdash; and then says how <em>-ed</em> and <em>-s</em> are said."
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
         "strong part it depends on."),
        ("Quote a hit rate, and the misses, for every rule you use",
         "99.92% for <em>-s</em>, 99.34% for <em>-ing</em>, 99.26% for the past, "
         "measured on the page against 1,210 verbs, with each word the rule "
         "misses printed beside it."),
        ("Tell a rule that helps from one that only sounds right",
         "The <em>-f</em> to <em>-ves</em> rule, added for good reasons, made "
         "the results worse. The count found it; the ear did not."),
        ("Tell a spelling difference from a mistake",
         "<em>Travelling</em> and <em>traveling</em> are both right. Eleven of "
         "the eighteen words the doubling rule still misses are this, and three "
         "words it once seemed to miss were mistakes in the list itself."),
        ("Say how -ed and -s are said",
         "From the last sound of the verb: <em>t</em>, <em>d</em> or <em>id</em> "
         "for the past, <em>s</em>, <em>z</em> or <em>iz</em> for the other. The "
         "rule is right for 1111 of 1118 past forms and 1187 of 1189 forms with "
         "<em>-s</em>."),
    ],
    "syllabus_intro": (
        "The forms first, because every later lesson puts them behind a small "
        "word. Then the rules scored on every verb they can touch, the one rule "
        "that needs the strong part of the word, and last the sounds of the two "
        "endings."
    ),
    "not_covered": [
        "When to choose one box over another. That is a question about meaning, "
        "and no count on this page answers it. The labs show how to build every "
        "box and how often the rules that build it are right; choosing between "
        "boxes is the work of reading and being corrected, which a page cannot "
        "do for you.",
        "Sound beyond the two endings. This course says how <em>-ed</em> and "
        "<em>-s</em> are said and where the doubling rule needs the strong "
        "part. How spellings turn into sounds, where the strong part falls and "
        "how fast speech squashes words are the courses called Spelling to "
        "Sound, Word Stress and Listening.",
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
        "the New General Service List (Browne, Culligan and Phillips), CC BY-SA 4.0. "
        "Sounds are from CMUdict (Carnegie Mellon University, BSD licence). The "
        "list of nouns was cut at build time with the help of the Moby "
        "Part-of-Speech list (public domain) and checked against a dictionary; "
        "no page carries either list."
    ),
    "lessons": list(_A) + list(_B),
}
