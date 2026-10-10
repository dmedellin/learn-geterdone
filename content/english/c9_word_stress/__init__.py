# -*- coding: utf-8 -*-
"""Course eight of the English Subject: where the strong part of a word falls, and what the rest says."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "word-stress",
    "title": "Word Stress",
    "level": "Intermediate",
    "blurb": (
        "Every English word of two or more parts has one part that is said "
        "stronger than the rest. A learner who puts it in the wrong place is "
        "often not understood, even when every sound is right. This course "
        "states the rules for where it goes, runs them over the 2,800 words in "
        "your browser, and prints how often each is right and every word it "
        "misses. It ends with what the weak parts sound like."
    ),
    "summary": (
        "The strong part of a word is not random. A noun of two parts has it "
        "first and a verb of two parts has it second. Some endings pull it "
        "toward themselves and some leave it alone. The parts that are not "
        "strong are said with one short sound, the flat vowel, whatever the "
        "spelling. This course counts each rule on a printed list, shows the "
        "words it misses, and says what kind of word each miss is."
    ),
    "assumes_short": (
        "Spelling to Sound, for how the page reads a pronunciation, and Tense "
        "Tables, for the strong part."
    ),
    "assumes_long": (
        "The page reads the strong part of every word from a pronouncing "
        "dictionary, the way the course called Spelling to Sound does for "
        "letters. The course called Tense Tables met the strong part first, in "
        "the rule that doubles a letter. Nothing here goes past counting and "
        "working out a share."
    ),
    "how_to": [
        "Say each word out loud before you read what the rule says. A rule "
        "about sound is checked by your own mouth first and by the table "
        "second.",
        "Read the lists of misses. Each one is short, and each kind of miss "
        "has a reason you can use, such as a noun made from a verb.",
        "Use the setting that shows the words set aside. A score is only about "
        "the words it was tried on, and the page says which words those were "
        "and which were left out.",
    ],
    "outcomes_intro": (
        "By the end you can place the strong part in a word you have not "
        "heard, and say how much to trust the rule you used."
    ),
    "outcomes": [
        ("Place the strong part of a two-part noun or verb",
         "First for the noun, second for the verb, a rule that is right for "
         "207 of 231 nouns and 134 of 150 verbs."),
        ("Say record both ways",
         "The 49 words that are a noun and a verb, and are strong on "
         "different parts in each."),
        ("Place the strong part in a word with an ending that pulls it",
         "The part before <em>-tion</em> and <em>-ic</em>, the third from "
         "the end for <em>-ical</em>, <em>-ity</em>, <em>-ate</em> and "
         "<em>-ize</em>."),
        ("Add an ending that leaves the strong part alone",
         "<em>-ly</em>, <em>-ness</em>, <em>-ment</em>, <em>-er</em>, "
         "<em>-ful</em> and <em>-able</em>, right for 185 of 192 pairs."),
        ("Sort a rule's misses into kinds",
         "A noun made from a verb, a false pair found by spelling, a word with "
         "two strong beats, and a word that sits alone."),
        ("Say a weak part with the flat vowel",
         "The vowel of 1387 of the 2628 weak parts in the list, whatever "
         "letter it is spelled with."),
    ],
    "syllabus_intro": (
        "The class of the word first, because it is the rule you need in "
        "every sentence. Then the endings that move the strong part, then the "
        "endings that do not, and last what the weak parts sound like."
    ),
    "not_covered": [
        "Stress across a sentence. This course is about one word at a time. "
        "Which words of a sentence are strong depends on what the speaker "
        "means, and no count on a printed list can read that.",
        "Words of three parts or more that have no ending in the lessons. "
        "The rules here cover the endings that were counted. A word such as "
        "<em>important</em> has no rule in this course, and the course does "
        "not pretend it has.",
        "Accents. The sound facts are the dictionary's American readings. "
        "British speakers put the strong part in a different place in some "
        "words, and no lesson measures the difference.",
        "Compound words and the two-word names that look like them. They have "
        "patterns of their own that the list cannot sort without a person to "
        "mark each one.",
    ],
    "key": [
        "noun of two parts: first   207 of 231",
        "verb of two parts: second  134 of 150",
        "-tion, -ic: just before    151, 28",
        "-ly, -ment, -er: no move   83, 31, 48",
        "the flat vowel         1387 of 2628",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every rule on this "
        "course is run in your browser on the list of words printed there, and "
        "every hit rate is counted on the page. Word list: the New General "
        "Service List (Browne, Culligan and Phillips), CC BY-SA 4.0. Sounds "
        "and the strong part of each word are from CMUdict (Carnegie Mellon "
        "University, BSD licence). Which words are nouns, verbs or adjectives "
        "was decided at build time with the help of the Moby Part-of-Speech "
        "list (public domain) and checked against a dictionary; no page "
        "carries either list."
    ),
    "lessons": list(_A) + list(_B),
}
