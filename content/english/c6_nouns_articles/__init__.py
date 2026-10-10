# -*- coding: utf-8 -*-
"""Course four of the English Subject: plurals, a and an, and the before the only one."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "nouns-and-articles",
    "title": "Nouns and Articles",
    "level": "Foundational",
    "blurb": (
        "Four small questions about nouns: how to make the <dfn>plural</dfn>, "
        "the form that means more than one; which nouns have none; whether it "
        "is <em>a</em> or <em>an</em>; and when <em>the</em> goes before the "
        "only one. Each is a rule that you can score on printed words, with "
        "every miss shown."
    ),
    "summary": (
        "The plural rule is right for 1,866 of 1,887 nouns, and the 21 it "
        "misses are five short lists. Seventy-five nouns have no plural at "
        "all. <em>A</em> or <em>an</em> goes by the next sound, not the next "
        "letter, and <em>the</em> goes before the only one. This course "
        "scores each rule on the page and prints the lines that break it."
    ),
    "assumes_short": "Tense Tables, for the -s rule.",
    "assumes_long": (
        "the course called Tense Tables, because the plural rule is the "
        "-s rule again, on nouns. Nothing else is needed. The "
        "counting never goes past working out a share."
    ),
    "how_to": [
        "Make the plural or choose the small word yourself before you read "
        "the rule, then check. The lab prints the rule beside each answer, so "
        "you can see whether you had the right reason as well as the right "
        "form.",
        "Read the table of misses before the rest of the lesson. Each list is "
        "short, and each one is a group with a reason. The groups are the "
        "lesson.",
        "Change the rule in the lab and watch the score move. Two of the three "
        "improvements to the plural rule make it worse, and only the count "
        "shows that.",
    ],
    "outcomes_intro": (
        "By the end you can make a plural, choose a small word in front of a "
        "noun, and say how often each of your rules is right."
    ),
    "outcomes": [
        ("Make the plural of a noun you have not seen",
         "Add <em>-s</em>; add <em>-es</em>, as in <em>boxes</em>; change "
         "<em>-y</em> to <em>-ies</em>, as in <em>cities</em>. Right for "
         "1,866 of 1,887 nouns."),
        ("Name the 21 nouns the rule misses and the kinds they make",
         "Old plural forms, <em>f</em> words, words from Greek, and two "
         "single cases. Each group is short enough to learn."),
        ("Say why two extra rules made the score worse",
         "<em>Potato</em> gained and <em>photo</em> lost. The count found "
         "that; the feeling that the rule made sense did not."),
        ("Say which nouns have no plural, and which small words they refuse",
         "Seventy-five in the word list, sorted into the kinds a student "
         "needs, with the limits of the list stated."),
        ("Choose a or an by the next sound",
         "Right on 493 of 493 printed lines, against 486 for the letter rule."),
        ("Put the before an -est word, and say when most means very",
         "Right on 127 of 142 lines with an <em>-est</em> word, and on 40 of "
         "122 with <em>most</em>, where 45 lines have <em>a</em>."),
    ],
    "syllabus_intro": (
        "Plurals first, because the rule is the one from Tense Tables, applied "
        "to nouns. Then the small words in front of a noun, which need the "
        "sound of the next word."
    ),
    "not_covered": [
        "Choosing <em>a</em> or <em>the</em> by meaning. Whether a noun has "
        "been mentioned before, or whether you mean any one or one in "
        "particular, depends on what the writer has in mind, and no count of "
        "printed words can see that.",
        "Whether a noun counts in the sentence in front of you. "
        "<em>Time</em> counts in one sense and not in another, and the course "
        "shows that with a quoted count. It cannot tell you which sense a "
        "writer means.",
        "<em>Much</em> and <em>many</em>, <em>few</em> and <em>little</em>. "
        "The course says which goes with a noun that has no plural, as a plain "
        "statement. It does not score it.",
        "Every plural that breaks the rule. The word list holds about two "
        "thousand common nouns, so rare nouns, which more often have an old "
        "or borrowed plural, are not in the table.",
    ],
    "key": [
        "a rule, the share it gets right,",
        "and the words it misses",
        "",
        "plural: -s, -es, -ies    1866 of 1887",
        "a or an by sound         493 of 493",
        "a or an by letter        486 of 493",
        "the with an -est word    127 of 142",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every rule on this "
        "course is run in your browser on the words printed there, and every "
        "share is counted on the page. Word list: the New General Service List "
        "(Browne, Culligan and Phillips), CC BY-SA 4.0. Parts of speech were "
        "taken at build time from the Moby Part-of-Speech list (public "
        "domain) and checked against a dictionary, and neither is carried on "
        "the page. Sounds are from CMUdict (Carnegie Mellon University, BSD "
        "licence). The older passages are public domain: <em>Pride and "
        "Prejudice</em> (1813) and <em>The Importance of Being Earnest</em> "
        "(1895). The two modern documents are works of the U.S. government. "
        "Counts over the whole novel were made once, offline, and each lesson "
        "marks them as quoted."
    ),
    "lessons": list(_A) + list(_B),
}
