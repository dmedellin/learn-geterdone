"""The Reading Faster path, as data: practice in reading faster, with the evidence.

Eight courses, each lesson built around a drill the reader does in the browser
-- a timed reading, a pacer, a flashed word stream, a skim, a scan, a recall --
scored there and kept in the reader's own log. The content lives here and only
here; scripts/ turns it into pages. The design is docs/reading/PLAN.md.
"""

from . import (
    c1_measure,
    c2_eyes,
    c3_guided,
    c4_inner_voice,
    c5_skim_scan,
    c6_difficulty,
    c7_remembering,
    c8_training_plan,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_measure.COURSE,
    c2_eyes.COURSE,
    c3_guided.COURSE,
    c4_inner_voice.COURSE,
    c5_skim_scan.COURSE,
    c6_difficulty.COURSE,
    c7_remembering.COURSE,
    c8_training_plan.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "reading-faster",
    "title": "Reading Faster",
    "level": "Beginner → Intermediate",
    "level_note": "any fluent adult reader; the arithmetic is a division",
    "tagline": (
        "Read faster in the ways that work, and find out for yourself which ones do &mdash; timed drills with comprehension checks in every lesson, a log of your own numbers, and the research on eye movements, the inner voice, skimming and memory. Eight courses and 42 lessons are available."
    ),
    "description": (
        "The Reading Faster Subject: eight courses of practice. Each lesson gives you a drill &mdash; a timed reading, a pacer, a flashed word stream, a skim, a scan, a recall test &mdash; scores it in your browser, and logs the result, so that what you learn about reading speed is measured on your own reading. The lessons explain what the eye can and cannot do, what the speed-reading courses promise and what the studies found, and how to choose a speed for a purpose. All eight courses and 42 lessons are available."
    ),
    "key": [
        "rate = words × 60 / seconds",
        "comprehension = correct / questions",
        "effective rate = rate × comprehension",
        "time per word = fixations × (fix + saccade)",
        "coverage = known tokens / all tokens",
        "one reading is one measurement",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. Measure Your Reading gives every later drill its scoring; How the Eyes Read gives the limits every technique is tested against; Guided Practice and The Inner Voice and Flashing Words try the classic techniques against a control; Skimming, Scanning and Previewing and Words, Knowledge and Difficulty are where most of the time is saved; Remembering What You Read measures what is kept; Your Training Plan uses all of it on your own log."
    ),
    "why_order": [
        "Measurement comes first because every later claim &mdash; that a pacer helps, that a flashed stream is faster, that skimming loses detail &mdash; is a comparison of two measurements, and a comparison means nothing until you know how much one measurement varies on its own.",
        "The eye comes second because it sets the limits. Once you have computed what a fixation costs and how far a glance reaches, you can test any speed claim in a line of arithmetic, and the rest of the Subject does.",
        "Guided practice and the inner voice come next: the techniques the speed-reading tradition teaches, each tried as a drill with a control condition, so you see what it does to your rate and to your comprehension.",
        "Skimming, difficulty and memory come after because they are where the real time is saved or lost: by not reading what you do not need, by knowing more words and more about the subject, and by remembering what you read the first time. The training plan comes last and uses all of it.",
    ],
    "prerequisites": [
        "Fluent reading in English. This is a Subject for an adult who already reads well and wants to read more in less time; it does not teach reading. If English is not your first language, your rates will be lower than the reference figures, and the comparisons that matter are with yourself.",
        "A quiet ten to twenty minutes per lesson, and a keyboard or a touchscreen. Every drill is timed; a drill run while you are interrupted measures the interruption.",
        "The arithmetic is a division and a product. The labs do it; what is asked of you is to read each number for what it is a measurement of.",
        "A willingness to be measured honestly. The comprehension questions are there so that a fast time with nothing understood shows up as what it is.",
    ],
    # Each path names its own hazard. This one's is that a single drill is
    # one measurement.
    "material": (
        "every figure on this path is computed in your browser from what you did in a drill or from the quantities a lesson states, and a rate measured on one passage on one day is one measurement, not your reading speed &mdash; whether a technique helps you is a question your log can answer and a single drill cannot."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what you did in a drill or from what the lesson states: a rate is words over minutes, comprehension is questions right over questions asked, an eye-movement budget is fixations times their cost. Passages are written for this course. Your drill results stay in your browser and are never sent anywhere. What the labs cannot do is tell you what one reading means on its own &mdash; that takes a log."
    ),
    "courses": COURSES,
}
