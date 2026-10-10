# -*- coding: utf-8 -*-
"""Course seven of the English Subject: five rules that take a spelling to a sound."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "spelling-to-sound",
    "number": 7,
    "title": "Spelling to Sound",
    "level": "Foundational",
    "blurb": (
        "Every student is given rules for how a spelling is said, and few are "
        "told how often each rule is right. This course takes five of them, runs "
        "each on the 2,800 words of the list, checks it against a dictionary that "
        "records how the word is said, and prints the score and every word the "
        "rule gets wrong."
    ),
    "summary": (
        "A spelling does not give you a sound, but it gives you a good guess, and "
        "some guesses are far better than others. Soft <em>c</em> is right every "
        "time it can be tried. <em>I before e</em> is right about six times in "
        "ten. This course scores five rules in your browser and sorts every "
        "miss into a group you can use."
    ),
    "assumes_short": "Nothing. You need to read English and to count.",
    "assumes_long": (
        "No other course on this site is needed before this one. The only sums "
        "are counting and working out a share. The sounds are written as plain "
        "words such as “shun” and “chur”, so you do not need to "
        "read any sound symbols."
    ),
    "how_to": [
        "Say the rule out loud, then say the word, before you look at the table. "
        "If you hear that the rule is wrong, find the word in the misses.",
        "Switch the list from the misses to every word. The words the rule gets "
        "right are the evidence that it is worth learning.",
        "Read the words that were set aside. A score is honest only if you know "
        "which words it was not tried on and why.",
    ],
    "outcomes_intro": (
        "By the end you can say a new word from its spelling with a number "
        "behind each guess, and name the words that break each rule."
    ),
    "outcomes": [
        ("Say c and g from the letter after them",
         "<em>C</em> before <em>e</em>, <em>i</em> or <em>y</em> is said as "
         "<em>s</em>, and the ten common words where <em>g</em> breaks the "
         "matching rule are a list you can learn."),
        ("Use the silent e and know its nine breaks",
         "The vowel says its name, except in <em>have</em>, <em>give</em>, "
         "<em>come</em>, <em>some</em>, <em>love</em>, <em>none</em>, "
         "<em>lose</em>, <em>move</em> and <em>prove</em>."),
        ("Quote a score for i before e",
         "36 of 58 words, and the three groups that all 22 failures fall "
         "into."),
        ("Name the letters you do not say",
         "Five rules for silent letters, and the one group, <em>ough</em>, "
         "that has no rule at all."),
        ("Say four common endings from their letters",
         "<em>-tion</em>, <em>-ture</em> and <em>-cial</em> are each said "
         "one way in nearly every word that has them, and <em>-sion</em> is "
         "said one of two ways, chosen by the letter before it."),
        ("Tell a rule from a habit",
         "A rule you can score and a list of misses you can read is worth "
         "keeping. A rule with a long list of misses is a habit."),
    ],
    "syllabus_intro": (
        "Letters first, because one letter and one sound is the simplest case. "
        "Then the famous rule and its score. Then letters that are not said "
        "at all, and last the endings that are always said the same way."
    ),
    "not_covered": [
        "How a word is said in British or any other speech. The page reads the "
        "first way one American dictionary gives, and it cannot tell you how "
        "the word sounds in your country or in any other.",
        "Where the strong part of a word falls. That is the next sound course, "
        "Word Stress, and it needs what this course teaches about the sounds "
        "themselves.",
        "Every spelling rule. Five rules were chosen because each can be "
        "scored on a list of whole words. A rule that depends on meaning "
        "cannot be scored this way.",
    ],
    "key": [
        "a rule, its score, and the words it misses",
        "",
        "c before e, i, y says s    348 of 348",
        "g before e, i, y says j    177 of 187",
        "silent e, vowel says name  131 of 140",
        "i before e, except after c   36 of 58",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every score is counted "
        "on the page by the rule named beside it, against the first way the "
        "dictionary says each word. Word list: the New General Service List "
        "(Browne, Culligan and Phillips), CC BY-SA 4.0. How each word is "
        "said: CMUdict (Carnegie Mellon University), BSD licence; its notice "
        "is printed under each lab."
    ),
    "lessons": list(_A) + list(_B),
}
