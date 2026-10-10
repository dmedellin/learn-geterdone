# -*- coding: utf-8 -*-
"""Course nine of the English Subject: listening, taught by annotation because no page can make a sound."""

from .part_a import LESSONS as _A
from .part_b import LESSONS as _B

COURSE = {
    "slug": "listening",
    "title": "Listening",
    "level": "Foundational",
    "blurb": (
        "People learning English say it is spoken too fast. Mostly it is not. "
        "Fewer than fifty small grammar words are two in every five of a page, and "
        "most of them change shape when said. Most of the rest announces where it "
        "begins. Two more lessons count how the small words are written when they "
        "are said short, and where the gaps between words go. Every count is made "
        "on a page you can read."
    ),
    "summary": (
        "Press Listen at the top of any page here and the browser reads it out. "
        "This course tells you what to listen FOR while it does. It marks, on "
        "real printed text, the things a listener uses to cut speech into words: "
        "which words get <dfn>squashed</dfn>, that is, said in a weak form; where "
        "the strong part of each other word falls; how <em>not</em> and the other "
        "small words are written when they are said short; and where one word "
        "runs into the next. Each is counted in your browser, the words counted "
        "are listed beside the count, and together they explain why a learner "
        "who knows every word on a page can still fail to hear it read aloud."
    ),
    "assumes_short": "Nothing from the other courses. It can be read first.",
    "assumes_long": (
        "No other course is needed. This one is about sound rather than form, "
        "so a reader who wants help hearing English before anything else is "
        "not held up by the rest. Word Stress helps with the second lesson, "
        "because it scores the rules for where the strong part falls."
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
         "387 of 936 words on the passage in the lab, which is 41.3%, counted in "
         "your browser."),
        ("Find where a word begins",
         "Most words that carry meaning start on their strong part &mdash; 390 "
         "of the 474 marked on the same page, which is 82.3%. The ones where "
         "that fails are a group: <em>believe</em>, <em>return</em>, "
         "<em>again</em>."),
        ("Write the full form behind a contraction",
         "<em>N't</em> is <em>not</em>, <em>'ll</em> is <em>will</em>, and "
         "<em>'s</em> and <em>'d</em> have more than one answer that you sort "
         "by the word that follows."),
        ("Say which kind of text contracts",
         "In 1,975 words of a play, 22 of 36 <em>not</em> words are written "
         "<em>n't</em>, which is 61.1%. In the novel passage it is 1 of 13, "
         "and in two modern documents 0 of 10."),
        ("Mark where words run together",
         "Where a word ends in a consonant and the next begins with a vowel, "
         "the consonant goes with the next word: 124 of 740 places on the "
         "passage, which is 16.8%."),
    ],
    "syllabus_intro": (
        "The small words first, because they are the larger share and the "
        "quicker win. Then where the other words begin, where the small words "
        "go when they are said short, and how the gaps between words fill."
    ),
    "not_covered": [
        "Teaching you to make the sounds. The pages read themselves aloud with "
        "your browser&rsquo;s voice, which is a reading voice and not a model to "
        "copy. This course tells you what to listen for; it does not correct "
        "your own speech, and nothing on a page could.",
        "Accents. The words that take a weak form are much the same everywhere "
        "English is spoken, but what they turn into is not. The shapes printed "
        "here are the ones a speaker from the south of England uses; the first "
        "lesson says what an American speaker does differently. The strong "
        "parts and the sounds at the edges of words come from an American "
        "dictionary, and nothing here measures the difference.",
        "Speech beyond what a page can show. Sounds also change where they "
        "meet in ways this course does not count, and a printed passage cannot "
        "say how often a speaker does any of it. The last lesson counts where "
        "words meet; it does not count what is said there.",
        "Which part of a word is the strong one. The second lesson counts how "
        "often it comes first. The rules that find it, by the class of the "
        "word and by its ending, are scored in Word Stress.",
    ],
    "key": [
        "speech has no gaps in it",
        "",
        "41.3% of a page is a few dozen small words",
        "and most of them get squashed",
        "",
        "82.3% of the rest start strong",
        "so a strong part means a new word",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> The reading voice is your "
        "own browser&rsquo;s. Every figure is counted in your browser over the "
        "passage printed on the same page, from <em>Pride and Prejudice</em> "
        "(Jane Austen, 1813, public domain), or over an excerpt of <em>The "
        "Importance of Being Earnest</em> (Oscar Wilde, 1895, public domain), "
        "or over the two modern documents, which are works of the U.S. "
        "government, with the words it counted listed beside it. A figure for "
        "a whole text that no page can carry is marked as quoted. Sounds and "
        "strong-part marks: CMUdict (Carnegie Mellon University, BSD licence). "
        "The squashed shapes are written as a speaker from the south of "
        "England says them."
    ),
    "lessons": list(_A) + list(_B),
}
