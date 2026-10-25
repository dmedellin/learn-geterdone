"""Course 8 -- Your Training Plan.

The Subject's last course turns everything before it on the reader's own log:
a week of practice planned under a budget, the log read by the Subject's rule,
a first reading of a new kind of text, and a profile of four measures.
"""

from . import part_a

COURSE = {
    "slug": "reading-your-training-plan",
    "title": "Your Training Plan",
    "level": "Intermediate",
    "summary": (
        "A week of practice planned under a time budget, a log read by the "
        "Subject's rule for a real change, a first reading of a kind of text you "
        "have not practised, and a profile of four measures set beside your first "
        "ones. The last course of the Subject, worked on your own numbers."
    ),
    "blurb": (
        "Plan next week so that it measures something, read your log for a change "
        "rather than a best day, try your practised pace on a dense argument, and "
        "take the full battery to see which of your measures have moved and which "
        "have too few readings to say."
    ),
    "key": [
        "week = sessions × minutes, summed",
        "a test at least every fifth session",
        "evidence: median of last 3 tests > range",
        "a new kind of text has no baseline yet",
        "a reader is a profile, not one number",
    ],
    "assumes_short": "The first seven courses",
    "assumes_long": (
        "the earlier courses, above all Measure Your Reading and Guided Practice, "
        "and a log kept since The Daily Drill; the profile also reads the drills of "
        "Skimming, Scanning and Previewing and Remembering What You Read"
    ),
    "outcomes_intro": (
        "By the end you can plan a week of practice that measures something, give "
        "the verdict on your own log, and say which of your measures have changed "
        "and which have not yet been measured often enough to say."
    ),
    "outcomes": [
        ("Plan a practice week",
         "Write a week of sessions under a time budget that keeps the routine's "
         "rules, and name the rule an unbalanced week breaks."),
        ("Give the verdict on a log",
         "Leave out the entries that do not count, compute the baseline range and "
         "the median of the last three tests, and state the verdict in the "
         "Subject's three tiers."),
        ("Test for transfer",
         "Set a first reading of an unpractised kind of text beside your baseline "
         "range and recent tests, and say what it can and cannot show."),
        ("Read a profile",
         "Compare four measures with your first ones, and say which changed by the "
         "Subject's rule and which have too few readings to say."),
    ],
    "syllabus_intro": (
        "Two lessons on the plan, the week and the curve it produces, then two on "
        "the test: a kind of text the practice never gave you, and the full battery."
    ),
    "how_to": [
        "Do each lesson's timed reading first. The three warm-ups here are test "
        "readings at natural pace, with no pacer, and they go into your log as "
        "tests; the drill in Plateaus and Transfer is a first reading of a new kind "
        "of text. Never read a drill's passage before its drill, and never read it "
        "again afterwards for the drill: a second reading measures memory.",
        "Have your log. Every lab in this course reads it, and a log that has been "
        "kept since The Daily Drill gives each one something to say. With an empty "
        "log the boxes hold worked examples, which teach the rule but say nothing "
        "about you.",
        "Do The Full Battery fresh, in one fifteen-minute sitting, and not after "
        "another drill. A tired battery measures the tiredness.",
        "Keep the Daily Drill going. Each lesson ends with it, and the course is "
        "built so that after the last lesson the routine, the log and the rule for "
        "reading it are all you need.",
    ],
    "not_covered": [
        "A plan made for you. The lab adds up the week you write and checks it "
        "against your budget; the routine's numbers are the Subject's choices, not "
        "a prescription measured for your reading, and no lab checks whether you "
        "keep the plan.",
        "Statistics beyond the Subject's rule. The median of the last three tests "
        "against the range of three baselines is a rule of thumb for one reader's "
        "log, not a significance test, and it says nothing about readers in "
        "general.",
        "Brain-training games and eye exercises as routes to transfer. They get "
        "one sentence in Plateaus and Transfer; the transfer tested here is from "
        "the practice passages to a new kind of text.",
        "Screen against paper, fonts and layout. The evidence is large and mixed, "
        "and none of it is a drill.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from your own log, "
        "from a drill you just did, or from a plan you typed. The verdicts follow "
        "the Subject's rule, which is honest about one reader's numbers and makes "
        "no claim about anyone else's, and a plan the lab says fits is a plan, not "
        "a promise."
    ),
    "lessons": part_a.LESSONS,
}
