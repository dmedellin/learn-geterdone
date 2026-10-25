"""Course 7 -- Remembering What You Read.

Four lessons in one module: free recall scored against a passage's idea units,
rereading against retrieval on a test two days later, a review schedule, and a
summary written from memory. The design is docs/reading/PLAN.md §C, Course 7.
"""

from . import part_a

COURSE = {
    "slug": "reading-remembering-what-you-read",
    "title": "Remembering What You Read",
    "level": "Intermediate",
    "summary": (
        "What a reading leaves behind, measured: a free recall scored against a "
        "passage's idea units, a reread set against a recall on a test two days "
        "later, a review schedule and its minutes, and a summary written from memory."
    ),
    "blurb": (
        "Find out how much of a passage you can write down with the page hidden, test "
        "whether a second reading or a recall keeps more after two days, plan reviews "
        "with gaps between them, and write notes from memory that hold the most for "
        "their length."
    ),
    "key": [
        "recall = units recalled / units",
        "recalled rate = rate × recall",
        "difference = recalled − read twice",
        "review day = the sum of the gaps so far",
        "words per unit = words written / units",
        "recognising is not recalling",
    ],
    "assumes_short": "Measure Your Reading",
    "assumes_long": (
        "the timed drill and the effective rate from Measure Your Reading, and the "
        "Daily Drill kept since Guided Practice"
    ),
    "outcomes_intro": (
        "By the end you can measure what a reading of yours keeps, and choose how to "
        "study a text you need to remember by what was measured rather than by what "
        "feels thorough."
    ),
    "outcomes": [
        ("Score a free recall",
         "Write down what a passage said with the page hidden, tick its idea units "
         "honestly, and compute the share recalled and your rate times that share."),
        ("Test rereading against retrieval",
         "Read one passage twice and recall another once, answer both passages' "
         "questions two or more days later, and compute the difference in points."),
        ("Plan a review schedule",
         "From a first gap, a multiplier and a number of reviews, list the review days "
         "and the minutes, and set spaced reviews against a massed session."),
        ("Write notes from memory",
         "Write a three-sentence summary with the text hidden, count the idea units it "
         "holds and the words it spends on each, and say what a good summary leaves out."),
    ],
    "syllabus_intro": (
        "The first two lessons measure what a reading keeps, at once and after two "
        "days; the last two turn the measurement into habits: when to come back to a "
        "text, and how to write it down."
    ),
    "how_to": [
        "Be an honest judge. In the recall drills the kit shows you the passage's idea "
        "units and you tick the ones your writing contains; it never reads the writing "
        "itself. Tick a unit when your writing has its substance, whatever the words, "
        "and leave it unticked when you remember only that the passage said something "
        "about it.",
        "Start Retrieval Beats Rereading early. Its comparison finishes two or more "
        "days later, when this Subject's pages offer you the delayed test. Do its two "
        "readings on your first day with this course and take the next lesson two or "
        "more days on, and the test will be waiting when you reach Spacing Your Reviews.",
        "Do not look at a passage before its drill. Each passage is used by one lesson "
        "only, and a passage you have seen before measures your memory of it rather "
        "than a first reading. If you are interrupted during a drill, Reset it and do "
        "it on another day.",
        "Keep the Daily Drill going. The recall drills sit beside the practice, not in "
        "place of it, and every lesson's last step is today's Daily Drill.",
    ],
    "not_covered": [
        "Memory techniques. Mnemonic systems, memory palaces and the like are a craft "
        "for remembering lists and sequences, and nothing here tests them.",
        "Flashcard software. Scheduling programs are where spacing is put to work at "
        "scale; this course computes a schedule by hand and leaves the choice of tool "
        "to you.",
        "Retention over months. The longest wait a drill here measures is the delayed "
        "test of Retrieval Beats Rereading, a few days; what you keep after a year is "
        "beyond a lab that lives in one browser.",
        "Studying for an examination. The techniques are the ones the research on "
        "learning rates highly, but a course of study has its own aims, and this "
        "Subject is about reading.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from your own ticks "
        "and answers, or from a schedule you state. A recall share is exactly as "
        "honest as your ticking, and one passage on one day is one measurement: a "
        "single pair of passages cannot say much about which way of studying suits you."
    ),
    "lessons": part_a.LESSONS,
}
