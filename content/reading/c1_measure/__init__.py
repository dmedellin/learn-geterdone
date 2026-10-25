"""Course 1 -- Measure Your Reading.

One lesson module: rate, comprehension and the effective rate, then how much
one reading varies, the published reference figures, and the practice log.
The baselines every later course compares against are taken here.
"""

from . import part_a

COURSE = {
    "slug": "reading-measure-your-reading",
    "title": "Measure Your Reading",
    "level": "Beginner",
    "summary": (
        "Time your own reading and score it: words per minute, comprehension out of six "
        "questions, and their product, the effective reading rate. Take the baseline "
        "readings every later course is compared with, find out how much one reading "
        "varies with nothing changed, place your numbers against the published figures "
        "in the right unit, and read a practice log."
    ),
    "blurb": (
        "Find out what your numbers are before you try to change them. Time a reading, "
        "score it, see how far a second reading moves on its own, and learn the rule this "
        "Subject uses before it calls any change real."
    ),
    "key": [
        "rate = words × 60 / seconds",
        "standard words = characters / 6",
        "comprehension = right / asked",
        "effective rate = rate × comprehension",
        "baseline range = lowest to highest",
        "a change: median of 3 tests above it",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "fluent reading in English and a division; no technique is assumed, and the labs "
        "do the arithmetic"
    ),
    "outcomes_intro": (
        "By the end you have three baseline readings and a fourth to test them with, and "
        "you can say what any later number of yours does and does not show."
    ),
    "outcomes": [
        ("Compute a reading rate",
         "From a word count and a time, compute words per minute, and from the characters, "
         "the rate in standard-length words of six characters."),
        ("Score a reading",
         "Compute comprehension and the effective rate for two readings, and say which "
         "delivered more understood words per minute."),
        ("Measure the noise",
         "Compute the range of your baselines and decide whether a later reading, and the "
         "median of three later tests, is above it."),
        ("Place a rate against the references",
         "Compare a rate in words with Brysbaert's averages and a rate in standard words "
         "with Carver's five gears, naming the purpose of each gear."),
        ("Read a practice log",
         "Pick out the readings that count, find the median of the last three tests, and "
         "state the verdict by the Subject's rule."),
    ],
    "syllabus_intro": (
        "Two drills give a rate and a score; two more readings show how much the rate moves "
        "on its own; the last two lessons place the numbers against published figures and "
        "against your own log."
    ),
    "how_to": [
        "Do every drill the first time you open the lesson, before you read the "
        "explanation. The first two lessons say so in their opening line, and the others "
        "put a warm-up reading above the lab. A drill done after you have read what it is "
        "supposed to show measures what you expected as much as what you read.",
        "Never practise on a passage you have already read. A second reading of the same "
        "text measures your memory of it, which is why every passage in this course is "
        "used in one lesson only. If you come back to a lesson, read its explanation and "
        "leave its drill alone.",
        "Read the way you would read something you had chosen to read: no racing, no "
        "studying, in a quiet ten minutes. The first three natural-pace readings become "
        "your baseline, and every later course compares with them.",
        "Keep the browser you started in. Your results are kept in this browser only, "
        "under one key, and Keeping a Practice Log shows you how to export them as text.",
    ],
    "not_covered": [
        "Reading difficulties. A reader who finds reading effortful, slow in a way that "
        "gets in the way of work or study, or tiring after a page should see a specialist, "
        "not a drill. Nothing in this Subject diagnoses or treats a reading difficulty, "
        "and dyslexia is outside it.",
        "Teaching children to read, and reading in a language you are still learning. The "
        "reference figures here are for adults reading English silently, and a reader in a "
        "second language should compare only with their own earlier numbers.",
        "Statistics beyond a range and a median. The Subject's rule for a real change is a "
        "rule of thumb that a single lucky reading cannot meet; it is not a significance "
        "test, and the course says how often chance can meet it anyway.",
        "Techniques for reading faster. This course measures; the pacer and the Daily Drill "
        "start in Guided Practice.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from a drill you did or "
        "from the numbers a lesson states: a rate is words over minutes, comprehension is "
        "questions right over questions asked. One timed reading of one passage is one "
        "measurement, not your reading speed, and the course is about how much two of them "
        "can differ with nothing changed."
    ),
    "lessons": part_a.LESSONS,
}
