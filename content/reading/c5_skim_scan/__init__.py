"""Course 5 -- Skimming, Scanning and Previewing.

Split across two lesson modules: part_a is scanning, skimming and previewing
(lessons 1-4, module "Scanning and skimming"), part_b is reading strategically
(lessons 5-7: inspecting a book, triaging a pile, shifting gears).
"""

from . import part_a, part_b

COURSE = {
    "slug": "reading-skim-scan-and-preview",
    "title": "Skimming, Scanning and Previewing",
    "level": "Intermediate",
    "summary": (
        "Reading less of a text on purpose, and measuring what it costs: scanning for "
        "a named target, skimming for the gist, previewing before a reading, "
        "inspecting a book before deciding to read it, triaging a pile against a "
        "time budget, and changing speed when the text changes."
    ),
    "blurb": (
        "Time a search through a timetable, skim a passage by its first sentences, "
        "score a skim on gist and detail separately, find out whether a preview pays "
        "for its own time, inspect a book in five minutes, plan a reading list that "
        "fits a 45-minute budget, and see whether you slow down where a text gets hard."
    ),
    "key": [
        "per target = seconds / targets found",
        "gist rate = gist right × 60 / seconds",
        "skim: gist suffers less than detail",
        "count a preview's time in the reading",
        "time saved by what you do not read",
        "shift gear by choice, not collapse",
    ],
    "assumes_short": "Measure Your Reading",
    "assumes_long": (
        "the rate, comprehension and effective rate from Measure Your Reading, and the "
        "Daily Drill from Guided Practice, kept going alongside this course"
    ),
    "outcomes_intro": (
        "By the end you can choose how much of a text to read for a purpose, and say "
        "from your own numbers what the choice cost you."
    ),
    "outcomes": [
        ("Time a scan",
         "Compute the seconds per target found and the words passed over per second "
         "from a timed search, and say why neither is a reading rate."),
        ("Score a skim",
         "Compute the share of a passage a skim shows and the gist questions right "
         "per minute, and point to a paragraph whose first sentence misleads."),
        ("Choose between a skim and a reading",
         "Score gist and detail separately for a skim and a full reading, and choose "
         "between them for a stated purpose."),
        ("Price a preview",
         "Compute the effective rate of a reading with its preview counted in the "
         "time, and decide whether the preview paid for itself."),
        ("Inspect and triage",
         "Answer structural questions about a book from its front and back matter "
         "within five minutes, and plan a pile of documents that fits a time budget "
         "and covers more value than reading them in order."),
        ("Shift gear deliberately",
         "Compute the rate of each section of a mixed text, and tell a chosen "
         "slowdown on the hard part from a collapse."),
    ],
    "syllabus_intro": (
        "The first module times the three ways of reading less of a text: a scan, a "
        "skim and a preview. The second moves up a level, to a whole book, a pile of "
        "documents and a text whose difficulty changes halfway through."
    ),
    "how_to": [
        "Do each drill before the explanation if you can, and do it once. Every "
        "drill passage here is used in one lesson only, and rereading a passage you "
        "have seen measures your memory of it, not your skim or your search.",
        "Score by purpose. A skim is scored on its gist, a scan on its search, a "
        "preview on the effective rate with its own time counted. A rate in words a "
        "minute is the right number only for a full reading.",
        "Keep the Daily Drill going. None of this course's drills replaces it, "
        "and the last step of every lesson is today's Daily Drill, so that your log "
        "of test readings keeps filling while you learn to read less of a text.",
        "Read a comparison as one measurement. What Skimming Costs and Previewing "
        "Before Reading each compare two different passages once; a result that "
        "goes against the studies is a reason to run the drill again on another "
        "pair, not a verdict.",
    ],
    "not_covered": [
        "Speed reading as a single skill. Skimming and scanning are taught here as "
        "ways of reading less of a text for a purpose, not as fast reading, and "
        "none of their figures is a reading rate.",
        "Reading on screens against paper, and how typography or layout changes "
        "a skim. The evidence is large and mixed, and none of it is a drill.",
        "Note-taking and study systems in full. Robinson's SQ3R is named for its "
        "survey step only; what you keep from a reading is Remembering What You "
        "Read.",
        "Choosing what is worth reading at all. The triage lesson takes the values "
        "of the documents as given; deciding them is your judgement for your "
        "purpose, and no lab checks it.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what you did "
        "in a drill or from what a lesson states: seconds per target found, the "
        "share of a passage a skim shows, gist questions right per minute, an "
        "effective rate with a preview's time counted, the minutes a reading plan "
        "takes. A skim or a scan is scored on what it was for, never as a reading "
        "rate, and one drill on one passage is one measurement."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
