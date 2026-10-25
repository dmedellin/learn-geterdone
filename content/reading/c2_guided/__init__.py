"""Course 2 -- Guided Practice.

The speed-reading tradition's own techniques -- the pacer, a target pace,
sprints above comfort, repeated reading -- done the way the tradition does
them, each measured with comprehension questions, and the Daily Drill the
rest of the Subject keeps going. One lesson module: part_a.
"""

from . import part_a

COURSE = {
    "slug": "reading-guided-practice",
    "title": "Guided Practice",
    "level": "Beginner",
    "summary": (
        "The techniques the speed-reading courses teach, done their way and "
        "measured: a pacer that moves down the page, a target pace found on a "
        "ladder of three readings, a routine of short daily sessions with a "
        "test every fifth, sprints above your usual rate, and repeated reading "
        "of one passage against a new one."
    ),
    "blurb": (
        "Read with a pacer, find the fastest pace at which you still "
        "understand, and start the Daily Drill the rest of the Subject keeps "
        "going. Every technique is scored with questions, so what it did to "
        "your understanding is measured beside what it did to your rate."
    ),
    "key": [
        "line time = words × 60,000 / target",
        "hold = fastest target scoring 4/6 or more",
        "three holds in a row: target × 21/20",
        "two misses in a row: target × 19/20",
        "every fifth session a test, no pacer",
        "repeat gain = reading 3 − reading 1",
        "transfer gain = new passage − reading 1",
    ],
    "assumes_short": "Measure Your Reading",
    "assumes_long": (
        "your baseline readings and the rule for a real change from Measure "
        "Your Reading, and a log in this browser that holds them"
    ),
    "outcomes_intro": (
        "By the end you have a practice routine running and know what each "
        "guided technique did on your own reading, in rate and in "
        "understanding."
    ),
    "outcomes": [
        ("Read with a pacer",
         "Set a pacer from a target rate, compute the time it gives a line, "
         "and compare a paced reading with an unpaced one on effective rate."),
        ("Find your hold target",
         "Run three paced readings at rising targets and name the fastest at "
         "which you still answer four questions in six, and say why it can "
         "differ from the run with the best effective rate."),
        ("Keep the Daily Drill",
         "Run a ten-to-fifteen-minute session by the routine, read your log "
         "for the next target, and know when the next session is a test."),
        ("Judge a sprint by the rule",
         "Read the reading after a sprint against your baseline range and say "
         "what further readings would make it evidence."),
        ("Tell practice on a passage from a faster reader",
         "Compute the gain on a repeated passage and on a new one, and say "
         "which of the two measures you rather than the text."),
    ],
    "syllabus_intro": (
        "The pacer comes first, then the pace to set it at, then the routine "
        "that uses both every day; the last two lessons push the pace and ask "
        "what a gain on a passage you know is worth."
    ),
    "how_to": [
        "Do each lesson's drill the first time you open it, before you read "
        "the explanation, and never practise on a passage you have already "
        "read: reading a text a second time measures your memory of it as "
        "well as your reading. The drills serve passages you have not logged "
        "and say so when there are none left.",
        "Put your own numbers into the target boxes before you start. A "
        "pacer's target is a box: “Use my baseline median” or “Use my next "
        "target” fills it from your log, or you type it, from the middle of "
        "your baseline rates in Measure Your Reading or the hold target you "
        "find in Choosing a Target Pace. The figures already in the boxes are "
        "a worked example, not a recommendation.",
        "Expect modest numbers. Rayner and colleagues' 2016 review of the "
        "research concluded that readers are unlikely to double or triple "
        "their rate while understanding as well as at their normal pace, and "
        "that the way to read faster with comprehension held is practice in "
        "reading and in language itself. The large savings of time come later, in Skimming, Scanning and Previewing and "
        "in Words, Knowledge and Difficulty. This course measures what the "
        "guided techniques do for you, whichever way it comes out.",
        "Keep the Daily Drill going. From The Daily Drill on, every lesson in "
        "the Subject ends with it, and the routine's tests are the readings "
        "Your Training Plan will read back to you.",
    ],
    "not_covered": [
        "Eye tracking. The pacer moves a highlight at a rate you set; it does "
        "not see where your eyes are, and nothing on these pages measures "
        "your fixations. How the Eyes Read models them.",
        "Reading instruction. Repeated reading comes from work on fluency "
        "with school-age readers and is described here as a method from that "
        "field, not taught as one. A reader who finds reading effortful "
        "should see a specialist, not a drill.",
        "Screen against paper, fonts and typography. The pacer groups words "
        "into lines as your screen lays them out, so a line's length depends "
        "on your device; the evidence on layout is large and mixed, and none "
        "of it is a drill.",
        "Claims that make no testable prediction. Photoreading and mental "
        "photography are named once, in Testing a Speed Claim in The Inner "
        "Voice and Flashing Words, and tested by the same arithmetic every "
        "speed claim gets.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from a "
        "reading you did or from the numbers a lesson states: a pacer's time "
        "per line is words times 60,000 over the target, a hold is the "
        "fastest target at which four questions in six were right, a gain is "
        "one rate minus another. A paced reading is paced by a highlight you "
        "set, and one comparison is one measurement; whether a technique helps "
        "you is a question your log answers over weeks."
    ),
    "lessons": part_a.LESSONS,
}
