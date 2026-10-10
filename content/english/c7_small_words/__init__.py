# -*- coding: utf-8 -*-
"""Small Words and Comparisons: in, on or at; -er or more; -ly; the pronoun and the particle.

Every figure in this course is read off a lab tile with labcheck.js --observe:
  in-on-at-for-time        109 lines, 103 right, 94.5% (novel 77 of 79, play 9 of 13,
                           modern documents 17 of 17)
  bigger-or-more-big       novel 367 forms, rule A 337 (91.8%), rule B 341 (92.9%);
                           play 44 of 49 (89.8%) and 45 of 49 (91.8%); modern 32 of 32
  happily-simply-truly     plain 98 of 126 (77.8%), with the changes 126 of 126 (100.0%),
                           27 of 153 with no adverb
  give-it-up-not-give-up-it  novel 473 lines, 34 pronouns between, 8 after, 81.0%, 347
                           preposition lines; play 149, 16, 5, 76.2%, 93
"""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "small-words-and-comparisons",
    "title": "Small Words and Comparisons",
    "level": "Intermediate",
    "blurb": (
        "<em>In</em>, <em>on</em> or <em>at</em>? <em>Bigger</em> or <em>more "
        "big</em>? <em>Happily</em> or <em>happyly</em>? <em>Give it up</em> or "
        "<em>give up it</em>? This course states the rule for each, counts how "
        "often it is right on printed lines, and shows you the lines it gets wrong."
    ),
    "summary": (
        "Four small questions that learners keep asking and books answer with "
        "a sentence and two examples. Here each answer is a rule, and each rule "
        "is run in your browser over lines from a novel, a play and two modern "
        "documents, or over a word list. You read the score, then the lines "
        "behind it, and the lines that break the rule turn out to be a few "
        "kinds, each with a reason you can use."
    ),
    "assumes_short": "Nouns and Articles, and a first look at Word Stress.",
    "assumes_long": (
        "Nouns and Articles, whose lessons count words in the same way, and Word "
        "Stress, which counts the parts of a word. The comparison lesson explains "
        "what a part is where it first needs one, so you can read this course "
        "first and come back to Word Stress later"
    ),
    "how_to": [
        "Say your own choice before you open the score. If you would say "
        "<em>in the evening</em>, say why. The lab prints the kind of time word "
        "beside every line, so you can check the reason as well as the answer.",
        "Read the lines the rule gets wrong before you read the lines it gets "
        "right. Each list of misses is short, and each one comes in a few kinds. "
        "Learning the kinds is quicker than learning the lines.",
        "Notice the age of the text. The novel is from 1813 and the play from "
        "1895, and some of what they do, such as <em>handsomer</em>, is not what "
        "a writer does now. The modern documents show the other side.",
    ],
    "outcomes_intro": (
        "By the end you can choose the <dfn>preposition</dfn>, the small word "
        "such as <em>in</em> that stands before a noun, for a time word; choose "
        "the comparison form of an <dfn>adjective</dfn> (<dfn>adjectives</dfn> "
        "are words such as <em>big</em> that say what a thing is like); make "
        "the <dfn>adverb</dfn>, the word that says how; and place the "
        "<dfn>pronoun</dfn>, a word such as <em>it</em> that stands for a "
        "noun. Each is a rule you can state, and each page says how often "
        "that rule holds."
    ),
    "outcomes": [
        ("Choose in, on or at from the time word",
         "A clock time, <em>night</em> and a festival take <em>at</em>; a day "
         "takes <em>on</em>; a month, a year, a season and a morning take "
         "<em>in</em>. The rule is right on 103 of 109 printed lines."),
        ("Choose -er or more by counting the parts",
         "One part takes <em>-er</em>; two parts ending in <em>-y</em> take "
         "<em>-ier</em>; the rest take <em>more</em>. Right on 337 of the "
         "novel's 367 forms."),
        ("Name the comparisons an old text uses and a modern one does not",
         "Of the 30 forms the rule gets wrong in the novel, 22 put "
         "<em>-er</em> or <em>-est</em> on a word of two parts, such as "
         "<em>handsomer</em> and <em>pleasanter</em>."),
        ("Make an -ly adverb from an adjective",
         "Adding <em>-ly</em> alone is right for 98 of 126 adjectives; the "
         "five spelling changes are right for all 126."),
        ("Name the adjectives that have no -ly adverb",
         "27 of the 153 adjectives in the list, among them <em>afraid</em>, "
         "<em>alive</em> and <em>sorry</em>."),
        ("Place a pronoun with a phrasal verb",
         "Between the verb and the <dfn>particle</dfn>, the small word of a "
         "<dfn>phrasal verb</dfn> such as the <em>up</em> of <em>give up</em>: "
         "<em>find it out</em>. After a preposition: <em>look at it</em>. Read "
         "off 473 novel lines."),
    ],
    "syllabus_intro": (
        "Time words first, because the rule is a table you can learn in a "
        "minute. Then the two lessons that build a new word from an old one, "
        "the comparison and the adverb. The last lesson is about a small word "
        "that moves."
    ),
    "not_covered": [
        "<em>In</em>, <em>on</em> and <em>at</em> for places. <em>At "
        "Netherfield</em> and <em>in London</em> depend on what kind of place "
        "it is, and a count cannot sort a house from a town without a person "
        "to do it. Only time words are scored here.",
        "Which of two adjectives comes first, and pairs such as <em>much</em> "
        "and <em>many</em>. The first is a matter of the ear and the second "
        "is too mixed to count well on the lines this course has.",
        "What a phrasal verb means. The lab finds the verb and the small word "
        "and says where a pronoun goes; it cannot say that <em>give up</em> "
        "means stop. That is the work of a dictionary and of reading.",
        "How a form sounds. Whether <em>handsomer</em> sounds old, or "
        "<em>more handsome</em> sounds plain, is a judgement. The lab shows "
        "what the novel did and what the modern documents did, and leaves "
        "the judgement to you.",
    ],
    "key": [
        "small words, counted on printed lines",
        "",
        "in, on or at       103 of 109 lines",
        "-er or more        337 of 367 forms",
        "-ly with changes   126 of 126 words",
        "pronoun between    34 of 42 lines",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every score on this "
        "course is counted in your browser on the lines or the word list printed "
        "on the page. Word list: the New General Service List (Browne, Culligan "
        "and Phillips), CC BY-SA 4.0. The older lines are public domain: "
        "<em>Pride and Prejudice</em> (1813) and <em>The Importance of Being "
        "Earnest</em> (1895). The number of parts in a word is from CMUdict "
        "(BSD licence), and the parts of speech were taken at build time from "
        "the Moby Part-of-Speech list (public domain) and checked against a "
        "dictionary; no page carries either list. The two modern documents are "
        "works of the U.S. government."
    ),
    "lessons": list(_A) + list(_B),
}
