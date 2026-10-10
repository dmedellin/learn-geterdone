# -*- coding: utf-8 -*-
"""Course two: the verbs that break the forming rules, and how few patterns they take."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B
from .part_c import LESSONS as _C

COURSE = {
    "slug": "irregular-verbs",
    "title": "Irregular Verbs",
    "level": "Foundational",
    "blurb": (
        "<em>Tense Tables</em> built any verb from four rules. An <dfn>irregular</dfn> verb is "
        "one those rules do not reach. This is the list of them, and it is "
        "shorter than it looks, because 132 of the "
        "133 verbs here fall into six patterns, <em>be</em> stands alone "
        "outside them, and three words carry more than half of the trouble."
    ),
    "summary": (
        "The verbs that break the rules are the ones you meet most often, which "
        "is why they feel like the whole language. This course prints all of "
        "them, sorts them into six patterns decided by the written forms alone, "
        "and then counts, in your browser, how much of a printed page they "
        "actually make up. The honest answer means pulling <em>be</em>, "
        "<em>have</em> and <em>do</em> out of the count, and the number falls "
        "by more than half when you do. Figures for the whole novel are quoted beside "
        "the page&rsquo;s own, and marked as quoted, so you can see which way "
        "a count moves when the text gets longer."
    ),
    "assumes_short": "Tense Tables, because an irregular verb is one the rules there do not reach.",
    "assumes_long": (
        "Tense Tables. An irregular verb is defined here as one whose forms the "
        "rules of Tense Tables do not produce, so those rules have to exist first. "
        "Nothing else is assumed and the number work is counting and shares."
    ),
    "how_to": [
        "Learn the pattern, not the verb. Six shapes is a smaller thing to hold "
        "than 133 separate words, and a pattern tells you how many forms to "
        "remember even when it does not tell you the letters.",
        "Start at the top of the list. These verbs are common, which "
        "is why they survived; the commonest twenty do most of the work.",
        "Watch the count when <em>be</em>, <em>have</em> and <em>do</em> leave "
        "the room. Every flattering number about irregular verbs depends on "
        "them, and the lab lets you take them out.",
    ],
    "outcomes_intro": (
        "By the end you can place an unfamiliar irregular verb in a pattern, and "
        "say how much of a page they really take up."
    ),
    "outcomes": [
        ("Say what makes a verb one of these",
         "Its forms are not the ones <em>Tense Tables</em> produces. That is a "
         "test, not a feeling, and it decides the whole list."),
        ("Sort a verb into one of six patterns",
         "Decided by the three written forms: all the same, past and the form "
         "after <em>have</em> the same, all three different, and so on."),
        ("Name the pattern worth learning first",
         "Sixty of the 133 have the same past and <dfn>participle</dfn>, so one form fewer "
         "to remember for nearly half the list."),
        ("Count how much of a real page they are",
         "About one word in six on the printed passage, counted in the browser "
         "against the printed list."),
        ("Take out the three that bend every count",
         "<em>Be</em>, <em>have</em> and <em>do</em> are about three in five of "
         "these words on the printed passage, 91 of 149. Taking them out cuts "
         "the share by more than half, 15.9% to 6.2%."),
        ("Tell a figure the page computes from one it quotes",
         "Over the whole novel, counted once and quoted, the top twenty "
         "irregular verbs cover 87.66% or 73.90% of the irregular forms depending on "
         "whether those three are counted. The page cannot recount either, "
         "but it counts the same thing on its passage, 95.3% or 93.1%, and "
         "you can say why the shorter text gives the higher share."),
    ],
    "syllabus_intro": (
        "The list first, then the patterns inside it, then the question of how "
        "much of English it really is."
    ),
    "not_covered": [
        "Every one of them in English. The list here is the 133 that appear "
        "in the 2,800 commonest words. About fifty more exist that a learner "
        "meets rarely, and they are "
        "named as left out rather than quietly dropped.",
        "Why these verbs are the way they are. The history is real and this course does "
        "not teach it, because nothing on the page could check it. What can be "
        "checked is that they are common, and the course shows that.",
        "Verbs with two pasts, such as <em>learnt</em> and <em>learned</em>, "
        "or <em>dream</em>, which takes either form. The list gives one, "
        "and no rule could be scored on a choice the dictionary allows "
        "both ways.",
    ],
    "key": [
        "133 verbs: six patterns, and be",
        "",
        "past = the have-form     60",
        "all three differ, -n     37",
        "all three the same       21",
        "all three differ, other   9",
        "",
        "be, have, do: more than half of the trouble",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> The verb list on this "
        "course is printed on the page, and every share the lab prints is "
        "counted in your browser against it, on a printed passage of "
        "<em>Pride and Prejudice</em> (1813), public domain, novel text only, "
        "936 words of it. The text is old, and the lab says so where that "
        "changes an answer. "
        "Figures for the whole novel were counted once, offline, with the "
        "same program over the novel text only, and the "
        "lesson marks each one as quoted where it appears."
    ),
    "lessons": list(_A) + list(_B) + list(_C),
}
