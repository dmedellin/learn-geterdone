"""Course 6 -- Words, Knowledge and Difficulty.

One lesson module: part_a holds all five lessons, the Difficulty module
(your rate on hard text, readability formulas) and the Knowledge module
(vocabulary coverage, topic familiarity, reading volume).
"""

from . import part_a

COURSE = {
    "slug": "reading-words-knowledge-and-difficulty",
    "title": "Words, Knowledge and Difficulty",
    "level": "Intermediate",
    "summary": (
        "Why the same reader has different rates on different texts: what a hard "
        "passage does to your rate and your comprehension, what a readability "
        "formula counts and what it misses, how many unknown words a page can carry, "
        "how much what you already know about a topic matters, and what reading more "
        "minutes a day adds against reading faster."
    ),
    "blurb": (
        "Read an easy and a hard passage and measure the gap between them. Count a "
        "text the way a readability formula does, mark the words you do not know, "
        "time a familiar topic against an unfamiliar one, and work out what ten more "
        "minutes a day would add to a year of reading."
    ),
    "key": [
        "rate ratio = hard rate / easy rate",
        "ease = 206.835 − 1.015 × W/S − 84.6 × Y/W",
        "grade = 0.39 × W/S + 11.8 × Y/W − 15.59",
        "coverage = known tokens / all tokens",
        "one unknown in every N = tokens / unknown",
        "words a year = minutes × rate × days",
    ],
    "assumes_short": "Courses 1 to 5",
    "assumes_long": (
        "the scoring from Measure Your Reading, the Daily Drill from Guided Practice, "
        "and the gears of reading met in Skimming, Scanning and Previewing"
    ),
    "outcomes_intro": (
        "By the end you can say what kind of text a rate was measured on, and put a "
        "number on four things that change a rate more than any technique: "
        "difficulty, unknown words, what you already know, and how much you read."
    ),
    "outcomes": [
        ("Measure the cost of a hard text",
         "Read an easy and a hard passage at your own pace, compute the ratio of the "
         "two rates and both effective rates, and say what a rate measured on easy "
         "text tells you about a hard one."),
        ("Compute a readability score",
         "Compute Flesch Reading Ease and the Flesch–Kincaid grade from counts of "
         "words, sentences and syllables, to one decimal, and name what the formulas "
         "cannot see."),
        ("Measure vocabulary coverage",
         "Mark the unknown words in a passage, compute the share you know and one "
         "unknown in every so many tokens, and set it beside the published "
         "estimates at the strength they were found."),
        ("Separate knowledge from readability",
         "Time a familiar and an unfamiliar topic at about the same grade, compute "
         "both effective rates and their ratio, and say why the formula did not "
         "predict the difference."),
        ("Compare a rate gain with a time gain",
         "Compute a year of reading from minutes a day and a rate, and find the "
         "rate gain that would equal ten more minutes."),
    ],
    "syllabus_intro": (
        "The course starts with your own easy and hard readings, then measures "
        "difficulty by formula, then turns to what the formula leaves out: the "
        "words you know, the topics you know, and how much you read."
    ),
    "how_to": [
        "Do each drill before you read the lesson below it. Most of the lessons "
        "start by sending you to the drill, and the explanations are written for a "
        "reader who has just seen their own numbers.",
        "Read every passage once. A passage you have read before is a test of your "
        "memory, not your reading, and each lesson's passages are used nowhere else "
        "in the Subject except where a lesson counts a text you have already read.",
        "Keep the Daily Drill going. Every lesson ends with it, and when the pool "
        "reaches its hard passages, the hold target you find there is a second "
        "measurement of what this course is about.",
        "Read each comparison as two measurements. An easy and a hard passage, or a "
        "familiar and an unfamiliar one, differ in more than the one thing the "
        "lesson is about, and one comprehension question is about 16.7 points.",
    ],
    "not_covered": [
        "Learning vocabulary. The course measures how many words in a text you do "
        "not know and what the studies say that costs; it does not teach word lists, "
        "roots or memory techniques for new words.",
        "Reading in another language, beyond the coverage studies. Most of what is "
        "known about coverage comes from learners of English, and the course says "
        "so where it uses it; how to read in a second language is a subject of its own.",
        "Other readability formulas. Flesch's two are taught because they are "
        "simple and widely used; the others count much the same things and share "
        "the same blind spot.",
        "Developing readers and reading difficulties. A reader for whom ordinary "
        "text is effortful should see a specialist, not a drill, as Measure Your "
        "Reading says.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from a drill you "
        "did or from the counts a lesson states. A readability score is a count of "
        "sentence and word lengths, a coverage figure is a count of the words you "
        "marked, and a year of reading is a product of three numbers. None of them "
        "says how hard a text is for you; your two readings say that, for one day."
    ),
    "lessons": part_a.LESSONS,
}
