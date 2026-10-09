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
        "Fewer than fifty small grammar words are two in every five of a page, most of "
        "them change shape when said &mdash; and most of the rest "
        "announces where it begins. Both are counted here, on a page you can "
        "read."
    ),
    "summary": (
        "Press Listen at the top of any page here and the browser reads it out. "
        "This course tells you what to listen FOR while it does: it marks, on "
        "real printed text, the two things a listener uses to "
        "cut speech into words: which words get <dfn>squashed</dfn>, that is, "
        "said in a weak form, and where the strong part of each other word "
        "falls. Both are counted in your browser, the words counted are listed "
        "beside the count, and together they explain why a learner who knows "
        "every word on a page can still fail to hear it read aloud."
    ),
    "assumes_short": "Nothing from the other courses. It can be read first.",
    "assumes_long": (
        "No other course is needed. This one is about sound rather than form, "
        "so a reader who wants help hearing English before anything else is "
        "not held up by the rest."
    ),
    "how_to": [
        "Take the printed list away with you. The small words on it are the "
        "same in a news report, a film and a conversation, and the list is the "
        "part of this course that does work outside it.",
        "Use it on something you are already listening to. The voice that reads "
        "these pages is a reading voice, so the course is only useful when you "
        "carry it to a person talking.",
        "Do not try to catch every word. The course is partly an argument that "
        "trying to is the wrong method, and that listening for the strong parts "
        "is what a native listener actually does.",
    ],
    "outcomes_intro": (
        "By the end you can look at a written sentence and say which parts of it "
        "will be hard to hear, and why."
    ),
    "outcomes": [
        ("Name the words that can take a weak form",
         "Fewer than fifty of them. The 43 that appear on the passage in the lab are "
         "printed with the shape each one takes in an ordinary sentence, and "
         "the common small words that keep their shape are named."),
        ("Say what share of a page they are",
         "388 of 949 words on the passage in the lab, which is 40.9%, counted in "
         "your browser."),
        ("Explain why they blur together",
         "They are short and most of them use the same flat <dfn>vowel</dfn>, so "
         "they sound the same as well as being short."),
        ("Find where a word begins",
         "Most words that carry meaning start on their strong part &mdash; 399 "
         "of the 485 marked on the same page, which is 82.3%."),
        ("Name the words where that guess fails",
         "The ones with a small piece on the front: <em>believe</em>, "
         "<em>return</em>, <em>again</em>. A group, not a scatter."),
        ("Stop blaming your ears",
         "Two words in five of what reaches you come from one short list, in a shape nobody "
         "showed you. That is a gap in teaching, and it closes quickly."),
    ],
    "syllabus_intro": (
        "The small words first, because they are the larger share and the "
        "quicker win. Then where the other words begin."
    ),
    "not_covered": [
        "Teaching you to make the sounds. The pages read themselves aloud with "
        "your browser&rsquo;s voice, which is a reading voice and not a model to "
        "copy. This course tells you what to listen for; it does not correct "
        "your own speech, and nothing on a page could.",
        "Accents. The words that take a weak form are much the same everywhere "
        "English is spoken, but what they turn into is not. The shapes printed "
        "here are the ones a speaker from the south of England uses; the first "
        "lesson says what an American speaker does differently, and nothing "
        "here measures the rest.",
        "Quick speech beyond word shapes. Sounds also run into one another and "
        "change where they meet. That is real and it is not counted here, "
        "because nothing on a page could check it.",
        "Which part of a word is the strong one, as a rule. There is no reliable "
        "rule from the spelling. The lab prints it for every word on its page and "
        "names that as a thing to learn with the word.",
    ],
    "key": [
        "speech has no gaps in it",
        "",
        "40.9% of a page is a few dozen small words",
        "and most of them get squashed",
        "",
        "82.3% of the rest start strong",
        "so a strong part means a new word",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> The reading voice is your "
        "own browser&rsquo;s. Every figure is counted in your browser over the "
        "passage printed on the same page, from <em>Pride and Prejudice</em> "
        "(Jane Austen, 1813, public domain), with the words it counted listed "
        "beside it. Strong-part marks: CMUdict, BSD licence. The squashed shapes "
        "are written as a speaker from the south of England says them."
    ),
    "lessons": list(_A) + list(_B),
}
