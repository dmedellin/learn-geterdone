# -*- coding: utf-8 -*-
"""Course three of the English Subject: the small words that stand in front of a verb."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "helping-verbs",
    "number": 3,
    "title": "Helping Verbs",
    "level": "Foundational",
    "blurb": (
        "Most mistakes with English verbs are mistakes with the small word in "
        "front of the verb. This course takes those words one rule at a time, "
        "runs each rule over one printed chapter of a novel and two modern "
        "documents in your browser, and prints every line the rule gets "
        "wrong beside the line it gets right."
    ),
    "summary": (
        "<em>Be</em>, <em>have</em>, <em>do</em> and the nine modal verbs stand in "
        "front of a verb and carry the work the verb cannot. This course "
        "states six rules about them: which form agrees with the subject, why "
        "the verb after <em>can</em> or <em>will</em> takes no ending, what "
        "<em>have</em> and <em>be</em> are when they are not helping, where <em>not</em> goes and when <em>do</em> "
        "arrives, and which of the twelve boxes a writer actually uses. Each "
        "rule is scored on printed text, and the lines it misses are sorted "
        "and explained."
    ),
    "assumes_short": "Tense Tables and Irregular Verbs, for the forms a helping verb sits in front of.",
    "assumes_long": (
        "Tense Tables and Irregular Verbs. A helping verb is only useful if you "
        "can name the form that comes after it: the base, the -ing form, "
        "the form after have; and those two "
        "courses build and list every one. The number work is counting and "
        "working out a share."
    ),
    "how_to": [
        "Read the printed chapter before you trust a number. Every figure on "
        "these pages is counted on a text you can read under the table, and "
        "each row the scan looked at is printed with the reason it was "
        "sorted where it was.",
        "Switch the lab to the two modern documents. The chapter is from 1813. "
        "A rule that holds in both has no age; a rule that changes between "
        "them tells you something about how English moved.",
        "Open the rows the rule does not cover first. They are fewer than the "
        "rows it covers, and they are where the lesson is: a rule and its "
        "short list of misses beats a long list of cases.",
    ],
    "outcomes_intro": (
        "By the end you can say what a helping verb does in front of any verb "
        "you meet, check a sentence of your own against six rules, and give "
        "the share of real text each rule covers."
    ),
    "outcomes": [
        ("Choose the verb form that agrees with its subject",
         "<em>Is</em>, <em>has</em>, <em>does</em>, <em>was</em> and the "
         "<em>-s</em> form for <em>he</em>, <em>she</em> and <em>it</em>; "
         "<em>are</em>, <em>were</em>, <em>have</em> and <em>do</em> for the "
         "rest; <em>am</em> for <em>I</em>."),
        ("Name the nine modal verbs and the form that follows each",
         "<em>Can</em>, <em>could</em>, <em>may</em>, <em>might</em>, "
         "<em>must</em>, <em>shall</em>, <em>should</em>, <em>will</em> and "
         "<em>would</em>, each followed by a verb with no ending."),
        ("Tell have the helping verb from have the main verb",
         "A form such as <em>seen</em> after it makes it a helping verb; a noun phrase after it "
         "makes it a main verb. The scan sorts the chapter's 37 forms of "
         "<em>have</em> 17 helping and 10 main, and misses seven helping "
         "verbs; read by hand, 24 are helping verbs."),
        ("Say what follows be on a real page",
         "The scan finds an <em>-ing</em> form after it 6 times in 137 in the "
         "chapter, and a reader finds one more. Most of the time <em>be</em> "
         "is the main verb, with a noun phrase, a word for what the subject "
         "is like, or a place after it."),
        ("Put not where the rule puts it, and add do when "
         "there is nothing to put it after",
         "After the first helping verb, or after a new <em>do</em>. The "
         "chapter shows 29 of 39 where the rule says, and sorts the other ten."),
        ("Read off which of the twelve boxes writers use",
         "Sorted from the words after each pronoun, the chapter's simple boxes "
         "and the phrases with a modal in front carry just over half of what "
         "is written. The lab files 3 phrases in 216 as progressive."),
    ],
    "syllabus_intro": (
        "Agreement and the form with no ending come first, because they are "
        "the rules with the highest scores. Then the two words that help "
        "another verb only some of the time. The last two put the helping "
        "verbs together: where <em>not</em> sits, and which of the twelve "
        "boxes get used."
    ),
    "not_covered": [
        "Choosing a box. This course shows which boxes writers use and how "
        "often. It never says which one to use, because that depends on what "
        "you mean, and no count of printed words can see what you mean.",
        "Short questions added at the end of a sentence, such as <em>is it not?</em> There are too few in the "
        "texts to measure: seven in the novel and nineteen in the play, which "
        "makes a list and not a rate.",
        "Sentences with <em>if</em>, and reported speech. Each one pairs a verb in "
        "one clause with a verb in another, and the scan reads only a few "
        "words at a time. The old wish form (<em>if I were</em>) is named "
        "where the chapter prints it and left there.",
        "How the helping verbs sound. They are said quickly and lightly, and that is "
        "Listening, not this course.",
    ],
    "key": [
        "he, she, it   is  has  does  was",
        "I             am",
        "you, we, they are  have  do   were",
        "",
        "modal + bare verb       can go",
        "not after the first helping verb",
        "no helping verb? add do",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every share on this "
        "course is counted in your browser on Chapter XXVI of <em>Pride and "
        "Prejudice</em> (1813, public domain) or on two modern documents that "
        "are works of the U.S. government: the Supreme Court opinion "
        "<em>Stanley v. City of Sanford</em>, 606 U.S. 46 (2025), and the "
        "Census Bureau story &ldquo;U.S. Population Aging as Nation Turns "
        "250&rdquo; (9 April 2026). Figures for the whole novel were counted "
        "once, offline, and each is marked as quoted where it appears. "
        "Parts of speech were taken at build time from the Moby Part-of-Speech "
        "list (public domain) and no page carries the list. Word list: the "
        "New General Service List (Browne, Culligan and Phillips), CC BY-SA 4.0."
    ),
    "lessons": list(_A) + list(_B),
}
