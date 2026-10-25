"""Course 3 -- How the Eyes Read.

One lesson module: part_a holds all six lessons (fixations and saccades, the
perceptual span, looking back, needless regressions, the speed ceiling,
training the periphery). The design is docs/reading/PLAN.md §C, Course 3.
"""

from . import part_a

COURSE = {
    "slug": "reading-how-the-eyes-read",
    "title": "How the Eyes Read",
    "level": "Intermediate",
    "summary": (
        "What the eyes do while you read, and the limits that follow: stops and jumps and the "
        "budget they make, how far one glance reaches, what looking back is for, and the line "
        "of arithmetic that tests any claimed reading speed against those limits."
    ),
    "blurb": (
        "Compute the rate a fixation budget allows, measure how far a 150 ms glance identifies "
        "letters, find out what hiding the lines behind your eyes does to your comprehension, "
        "and test a speed claim by the characters each glance would have to take in."
    ),
    "key": [
        "fixation ≈ 225 ms; saccade ≈ 30 ms",
        "a saccade moves about 7 to 9 letters",
        "time a word = fixations × (fixation + saccade)",
        "reading span: 3 to 4 left, 14 to 15 right",
        "needed = rate × 6 × 255 / 60,000",
        "regressions: 10 to 15% of saccades",
    ],
    "assumes_short": "Measure Your Reading, Guided Practice",
    "assumes_long": (
        "the rate, comprehension and effective rate of Measure Your Reading, and a hold target "
        "and a Daily Drill from Guided Practice"
    ),
    "outcomes_intro": (
        "By the end you can say what your eyes were doing during a drill, compute what that "
        "allows, and test a speed claim against it in a line of arithmetic."
    ),
    "outcomes": [
        ("Compute an eye-movement budget",
         "From fixation and saccade durations, characters per saccade, regression share and "
         "characters per word, compute fixations per word, time per word and the rate the "
         "model allows."),
        ("Measure a letter span",
         "Score a flash drill by distance from the centre, name the farthest position each "
         "side at which half the letters were identified, and say how this span differs from "
         "the perceptual span in reading."),
        ("Weigh what looking back is for",
         "Compare a reading with the text behind the eyes hidden against one without, on "
         "effective rate, and say whether the difference exceeds one question."),
        ("Tell repair from drift",
         "Separate regressions that repair understanding from lapses of attention, and say "
         "which kind a pacer can reduce."),
        ("Test a speed claim",
         "Compute the characters a fixation must advance for a claimed rate and classify the "
         "claim against the identification and perceptual spans, at stated settings."),
        ("Ask whether a drill transfers",
         "Read table times and test readings over weeks and say whether they support "
         "transfer to reading, and what else could explain both."),
    ],
    "syllabus_intro": (
        "The first module is what the eyes do: the stops and jumps, how far a stop reaches, and "
        "the jumps that go backwards. The second turns those figures into limits, and tests a "
        "speed claim and an eye exercise against them."
    ),
    "how_to": [
        "Keep the Daily Drill going. This course has a warm-up or a drill in every lesson, but "
        "none of them replaces the session from Guided Practice; the last step of every lesson "
        "sends you back to it.",
        "Read each passage once. Every drill here uses a passage you have not seen, and the "
        "warm-up serves the next one you have not logged. Rereading a passage measures your "
        "memory of it, not your reading.",
        "Treat the model as a model. The eye-movement budget and the speed check compute what "
        "stated averages imply, and say so. Nothing in this course tracks your eyes; your "
        "drills measure time and answers, and the model says how that time could have been "
        "spent.",
        "Read the two comparisons for what they are. Looking Back and Fewer Needless "
        "Regressions each set two readings of two passages side by side. One question is "
        "&asymp; 16.7 points of comprehension, and a difference of one question is not a result.",
    ],
    "not_covered": [
        "Eye tracking. The labs draw what a model of the eye implies; none of them measures "
        "your fixations, and nothing here claims to.",
        "Screen against paper, fonts and typography beyond line length. The evidence is large "
        "and mixed, and none of it is a drill.",
        "Reading difficulties and their treatment. A reader who finds reading effortful should "
        "see a specialist, not a drill, as Measure Your Reading says.",
        "The wider literature on brain-training games. Training the Periphery gives it one "
        "sentence; this course tests one exercise against your own log instead.",
    ],
    "footer_lead": (
        "The eye-movement figures in this course are stated averages from laboratory studies "
        "of skilled adult readers, and the labs compute what those figures imply, exactly. "
        "Your drills measure only the time you took and the questions you answered, in your "
        "browser; what your eyes did during them is not measured."
    ),
    "lessons": part_a.LESSONS,
}
