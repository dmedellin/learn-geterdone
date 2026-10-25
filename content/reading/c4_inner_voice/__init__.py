"""Course 4 -- The Inner Voice and Flashing Words.

One lesson module: the inner voice (aloud against silent, then counting under
the breath), and the flashed word stream (one word at a time, phrases, no way
back, and testing a speed claim).
"""

from . import part_a

COURSE = {
    "slug": "reading-inner-voice-and-flashing-words",
    "title": "The Inner Voice and Flashing Words",
    "level": "Intermediate",
    "summary": (
        "The speed-reading tradition's other techniques, each tried against a "
        "control on your own reading: silencing the inner voice, reading one "
        "flashed word at a time, reading in phrases, and the stream that never "
        "lets you look back. The course ends by testing a speed claim with three "
        "lines of arithmetic."
    ),
    "blurb": (
        "Read aloud and silently and compare the rates, read while counting under "
        "your breath, read a story flashed one word at a time and then one phrase "
        "at a time, and find out what the stream costs when a sentence needs a "
        "second look. Then test a claimed speed the way a study would."
    ),
    "key": [
        "ratio = silent rate / aloud rate",
        "effective rate = rate × correct / 6",
        "time per word = 60,000 ms / rate",
        "time per phrase = words × 60,000 / rate",
        "glance = rate × 6 × 255 / 60,000",
        "one question ≈ 16.7 points",
    ],
    "assumes_short": "Measure Your Reading, Guided Practice, How the Eyes Read",
    "assumes_long": (
        "Measure Your Reading for the rate, the effective rate and the baseline "
        "range, Guided Practice for the pacer and the Daily Drill, and How the "
        "Eyes Read for the eye-movement budget and the characters a fixation must "
        "advance"
    ),
    "outcomes_intro": (
        "By the end you can put each of the tradition's techniques to a fair test "
        "on your own reading, and say what your result does and does not show."
    ),
    "outcomes": [
        ("Compare reading aloud with reading silently",
         "Compute both rates and their ratio, and say what a silent rate above "
         "the speaking rate implies for the advice to eliminate the inner voice."),
        ("Test silencing the voice",
         "Compute the effective rates of a normal reading and a reading under "
         "suppression, and say when a suppressed reading does not count."),
        ("Read a flashed stream",
         "Compute the time each word or phrase is shown at a rate, and compare "
         "comprehension in the stream with your baselines."),
        ("Say what a stream takes away",
         "Explain why removing eye movements saves little time and why a stream "
         "with no way back can cost comprehension."),
        ("Test a speed claim",
         "Compute the characters each glance would need, the effective rate at a "
         "stated comprehension and the time a book would take, and name the test "
         "that would settle the claim."),
    ],
    "syllabus_intro": (
        "Two lessons on the inner voice, then four on the flashed stream: one word "
        "at a time, one phrase at a time, the stream against a pacer that lets you "
        "look back, and a claim tested by arithmetic."
    ),
    "how_to": [
        "Do each drill before you read its explanation, and never on a passage you "
        "have already read: a second reading of the same text measures your memory "
        "of it. Every drill here is a comparison, and each one uses its own fresh "
        "passages.",
        "Set the rate from your log. The streamed drills ask for a target rate; type "
        "the median of your baseline readings, so that the display is the only "
        "thing that changes. If you have no baselines yet, use 250 words a minute "
        "and say so to yourself when you read the result.",
        "Read the comparison for what it is. Two readings on two passages, in one "
        "order, on one day, are one pair of measurements. One question is about "
        "16.7 points of comprehension, and a difference of one question is not a "
        "result.",
        "Keep up the Daily Drill. Every lesson's last step sends you back to it, "
        "and a technique you want to adopt belongs in your log for weeks before "
        "you decide it works for you.",
    ],
    "not_covered": [
        "Training programmes for the inner voice. The lessons test what happens when "
        "the voice is occupied for one reading; they do not teach a method for "
        "removing it, and the studies in Silencing the Inner Voice are a reason for "
        "caution.",
        "Speed-reading apps by name. The drills reproduce the display such apps use, "
        "one word or one phrase at a time in a fixed spot, at a rate you set, and "
        "measure it on your reading.",
        "Photoreading, &ldquo;mental photography&rdquo; and subliminal methods, beyond "
        "one paragraph in Testing a Speed Claim: they make no prediction that "
        "ordinary comprehension questions could not test, and that test is the "
        "lesson.",
        "Reading aloud as a skill. The aloud reading is here to time your speaking "
        "pace; fluency in oral reading, and reading instruction for developing "
        "readers, are outside this Subject.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from a drill you "
        "did or from the numbers a lesson states: a ratio of two rates, a rate "
        "times the share of questions right, the time a word is on screen. The "
        "streams run at the rate you set and print the time they actually took. "
        "None of it can say, from one pair of readings, whether a technique works "
        "for you &mdash; that is what the log is for."
    ),
    "lessons": part_a.LESSONS,
}
