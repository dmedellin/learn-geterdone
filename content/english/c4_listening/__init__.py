# -*- coding: utf-8 -*-
"""Course four: listening, taught by annotation because no page can make a sound."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "listening",
    "number": 4,
    "title": "Listening",
    "level": "Foundational",
    "blurb": (
        "People learning English say it is spoken too fast. Mostly it is not. "
        "About fifty very common words change shape when said, and they are "
        "nearly half of every sentence &mdash; and most of the other half "
        "announces where it begins. Both are counted here, on a page you can "
        "read."
    ),
    "summary": (
        "This course cannot play you a sound, and says so on every page. What it "
        "can do is mark, on real printed text, the two things a listener uses to "
        "cut speech into words: which words get squashed, and where the strong "
        "part of each other word falls. Both are counted in your browser, both "
        "lists are printed, and together they explain why a learner who knows "
        "every word on a page can still fail to hear it read aloud."
    ),
    "assumes_short": "Nothing from the other courses. It can be read first.",
    "assumes_long": (
        "No other course is needed. This one is about sound rather than form, "
        "so a reader who wants help hearing English before anything else is "
        "not held up by the rest."
    ),
    "how_to": [
        "Take the printed list away with you. The fifty squashed words are the "
        "same in a news report, a film and a conversation, and the list is the "
        "part of this course that does work outside it.",
        "Use it on something you are already listening to. Nothing here makes a "
        "sound, so the course is only useful when you carry it to something that "
        "does.",
        "Do not try to catch every word. The course is partly an argument that "
        "trying to is the wrong method, and that listening for the strong parts "
        "is what a native listener actually does.",
    ],
    "outcomes_intro": (
        "By the end you can look at a written sentence and say which parts of it "
        "will be hard to hear, and why."
    ),
    "outcomes": [
        ("Name the words that get squashed",
         "About fifty of them, printed in full, with the shape each one takes in "
         "an ordinary sentence."),
        ("Say what share of a page they are",
         "452 of 949 words on the passage in the lab, which is 47.6%, counted in "
         "your browser."),
        ("Explain why they blur together",
         "They are short and they nearly all use the same flat vowel, so they "
         "sound alike as well as brief."),
        ("Find where a word begins",
         "Most words that carry meaning start on their strong part &mdash; 399 "
         "of 485 on the same page, which is 82.3%."),
        ("Name the words where that guess fails",
         "The ones with a small piece on the front: <em>believe</em>, "
         "<em>return</em>, <em>again</em>. A group, not a scatter."),
        ("Stop blaming your ears",
         "Nearly half of what reaches you is fifty words in a shape nobody "
         "showed you. That is a gap in teaching, and it closes quickly."),
    ],
    "syllabus_intro": (
        "The squashed words first, because they are the larger share and the "
        "quicker win. Then where the other words begin."
    ),
    "not_covered": [
        "The sounds themselves. No page on this site makes a noise, and this "
        "course does not pretend otherwise. It tells you what to listen for and "
        "where it will be; you need something that speaks to practise on.",
        "Accents. The words that get squashed are much the same everywhere "
        "English is spoken, but what they are squashed into is not, and nothing "
        "here measures that.",
        "Fast speech beyond word shapes. Sounds also run into one another and "
        "change at the join. That is real and it is not counted here, because "
        "nothing on a page could check it.",
        "Which part of a word is the strong one, as a rule. There is no reliable "
        "rule from the spelling. The lab prints it for every word on its page and "
        "names that as a thing to learn with the word.",
    ],
    "key": [
        "speech has no gaps in it",
        "",
        "47.6% of a page gets squashed",
        "and only 51 words do it",
        "",
        "82.3% of the rest start strong",
        "so a strong part means a new word",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> No sound is played on "
        "this course. Every figure is counted in your browser over text printed "
        "on the same page, with the word list printed beside it. Pronunciation "
        "data: CMUdict, BSD licence."
    ),
    "lessons": list(_A) + list(_B),
}
