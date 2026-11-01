"""Transformation, lessons 1-5 -- Chapter 16, the Conclusion, and Appendices A
and B.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018). Chapter 16, High-Performance
Leadership and Management, is by Steve Bell and Karen Whitley Bell (Lean IT
Strategies) and the lessons credit it to them. Pages in the comments are PDF
pages of the operator's copy; the lessons cite by chapter and section. Every
quotation is copied from that copy and checked with quotes.py. The samples are
written for these lessons: none of the book's tables, figures, survey items
or example data is used, and ING's structure and Obeya appear in prose only.
The design is docs/accelerate/PLAN.md, section C, Course 8.

The lab cfg keys follow docs/accelerate/kit-report.md; every preset's expect
was observed with labcheck.js --observe and checked by hand.
"""


_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)


# ---------------------------------------------------------------- 01 models

# A squad's board over ten days, written for the lesson: item, start day,
# done day. Item-days 6+4+6+3+7+5+5+4 = 40 over 10 days.
BOARD_LOG = (
    "A, 0, 6; B, 0, 4; C, 1, 7; D, 2, 5; E, 3, 10; F, 4, 9; G, 5, 10; H, 6, 10"
)

# 01 exercise: a squad finishing three items every two days.
EXERCISE_THROUGHPUT = "3/2"


# ---------------------------------------------------------------- 02 models

# A team's two fortnights of changes and incidents, written for the lesson.
# Times are hours from the start of the fortnight; failed is yes or no.
CURRENT_CHANGES = (
    "c1, 8, 62, no; c2, 20, 70, no; c3, 30, 98, yes; c4, 50, 74, no; "
    "c5, 100, 150, no; c6, 120, 200, yes; c7, 200, 290, no; c8, 250, 322, no"
)
CURRENT_INCIDENTS = "i1, 98, 107; i2, 200, 215"
NEXT_CHANGES = (
    "d1, 10, 20, no; d2, 30, 44, no; d3, 60, 80, no; d4, 90, 112, no; "
    "d5, 120, 138, no; d6, 150, 180, no; d7, 180, 192, yes; d8, 210, 236, no; "
    "d9, 250, 266, no; d10, 290, 310, no"
)
NEXT_INCIDENTS = "j1, 192, 195"

# 02 exercise: five changes over a five-day period.
EXERCISE_CHANGES = (
    "x1, 0, 30, no; x2, 10, 34, no; x3, 20, 100, yes; x4, 50, 58, no; "
    "x5, 60, 90, no"
)


# ---------------------------------------------------------------- 03 models

# The 24 capabilities of Appendix A, each under a short label of our own and
# the book's five categories. The names are facts; the wording is not the book's.
_CATEGORIES = {
    "CD": "continuous-delivery",
    "AR": "architecture",
    "PP": "product-and-process",
    "LM": "lean-management-and-monitoring",
    "CU": "cultural",
}


def _token(name):
    """The kit's names are single tokens: lower case, hyphens for spaces."""
    return name.lower().replace(" ", "-")

_CAPABILITIES = [
    ("Version control", "CD"), ("Deployment automation", "CD"),
    ("Continuous integration", "CD"), ("Trunk-based development", "CD"),
    ("Test automation", "CD"), ("Test data management", "CD"),
    ("Shift left on security", "CD"), ("Continuous delivery", "CD"),
    ("Loosely coupled architecture", "AR"), ("Empowered teams", "AR"),
    ("Customer feedback", "PP"), ("Visible flow of work", "PP"),
    ("Small batches", "PP"), ("Team experimentation", "PP"),
    ("Lightweight change approval", "LM"), ("Monitoring for decisions", "LM"),
    ("Proactive health checks", "LM"), ("WIP limits", "LM"),
    ("Visual displays", "LM"),
    ("Generative culture", "CU"), ("Learning culture", "CU"),
    ("Team collaboration", "CU"), ("Meaningful work", "CU"),
    ("Transformational leadership", "CU"),
]
CAPABILITIES = "; ".join(
    "%s, %s" % (_token(name), _CATEGORIES[code]) for name, code in _CAPABILITIES
)


def _has(*names):
    """A team's capabilities in place, as the cells after the team's name."""
    known = {name for name, _ in _CAPABILITIES}
    for name in names:
        assert name in known, name
    return ", ".join(_token(name) for name in names)


def _teams(**by_team):
    return "; ".join("%s, %s" % (team, has) for team, has in by_team.items())


# Orchid, a team of nine, at the start of a quarter and at its end.
ORCHID_START = _has(
    "Version control", "Deployment automation", "Continuous integration",
    "Test automation", "Loosely coupled architecture", "Customer feedback",
    "Lightweight change approval", "Generative culture", "Team collaboration",
)
ORCHID_END = _has(
    "Version control", "Deployment automation", "Continuous integration",
    "Test automation", "Loosely coupled architecture", "Customer feedback",
    "Lightweight change approval", "Generative culture", "Team collaboration",
    "Visible flow of work", "WIP limits", "Visual displays", "Learning culture",
)

# 03 exercise: Pine, at the start and the end of its quarter.
PINE_START = _has(
    "Version control", "Continuous integration", "Test automation",
    "Customer feedback", "Visual displays", "Meaningful work",
)
PINE_END = _has(
    "Version control", "Continuous integration", "Test automation",
    "Customer feedback", "Visual displays", "Meaningful work",
    "Deployment automation", "Small batches", "Team experimentation",
    "Proactive health checks",
)


# ---------------------------------------------------------------- 04 models

# Twenty-seven invented teams in three groups, and the number in each that met
# their organization's goals; then an uneven pair.
LIKELY_TWICE = "high, 9, 6; medium, 9, 4; low, 9, 3"
LIKELY_UNEVEN = "high, 8, 6; low, 10, 5"

# 04 exercise: a department's thirty teams.
LIKELY_EXERCISE = "high, 10, 8; low, 20, 8"


# ---------------------------------------------------------------- 05 models

# Six invented teams of one organization.
SIX_TEAMS = _teams(
    alder=_has(
        "Version control", "Deployment automation", "Continuous integration",
        "Trunk-based development", "Test automation", "Continuous delivery",
        "Loosely coupled architecture", "Empowered teams", "Customer feedback",
        "Visible flow of work", "Small batches", "Lightweight change approval",
        "Monitoring for decisions", "Visual displays", "Generative culture",
        "Learning culture", "Team collaboration", "Meaningful work",
    ),
    birch=_has(
        "Version control", "Deployment automation", "Continuous integration",
        "Test automation", "Test data management", "Loosely coupled architecture",
        "Customer feedback", "Visible flow of work", "Visual displays",
        "WIP limits", "Generative culture", "Team collaboration",
        "Meaningful work", "Transformational leadership",
    ),
    cedar=_has(
        "Version control", "Continuous integration", "Test automation",
        "Customer feedback", "Lightweight change approval", "Visual displays",
        "Learning culture", "Meaningful work",
    ),
    elm=_has(
        "Version control", "Deployment automation", "Continuous integration",
        "Trunk-based development", "Shift left on security",
        "Continuous delivery", "Empowered teams", "Small batches",
        "Proactive health checks", "Generative culture", "Learning culture",
        "Team collaboration", "Transformational leadership",
    ),
    fir=_has(
        "Version control", "Continuous integration", "Test automation",
        "Visible flow of work", "Visual displays", "Generative culture",
        "Meaningful work",
    ),
    hazel=_has(
        "Version control", "Deployment automation", "Test automation",
        "Loosely coupled architecture", "Customer feedback", "Small batches",
        "Monitoring for decisions", "Visual displays", "Learning culture",
        "Team collaboration", "Transformational leadership",
    ),
)
# Two teams with the same total and different shapes: Orchid at the end of its
# quarter (13) and Elm (13).
SAME_TOTAL = _teams(
    orchid=ORCHID_END,
    elm=_has(
        "Version control", "Deployment automation", "Continuous integration",
        "Trunk-based development", "Shift left on security",
        "Continuous delivery", "Empowered teams", "Small batches",
        "Proactive health checks", "Generative culture", "Learning culture",
        "Team collaboration", "Transformational leadership",
    ),
)

# 05 exercise: Willow, ten capabilities in place.
WILLOW = _teams(
    willow=_has(
        "Version control", "Deployment automation", "Continuous integration",
        "Test automation", "Loosely coupled architecture", "Empowered teams",
        "Customer feedback", "Small batches", "Generative culture",
        "Meaningful work",
    ),
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 16, High-Performance Leadership and Management, by Steve Bell
    # and Karen Whitley Bell: the opening (PDF pp. 219-221 of the operator's
    # copy) and A High-Performing Management Framework in Practice (pp.
    # 221-234): the Obeya (p. 222), tribes, squads, chapters (pp. 223-224),
    # the squad's visuals (p. 226). Part III introduction, p. 217; authorship
    # and notes, pp. 8, 240.
    # Quote: PDF p. 220 of the operator's copy, 24 words, quotes.py OK.
    # Lesson total: 24 words.
    {
        "slug": "a-high-performing-management-framework",
        "title": "A High-Performing Management Framework in Practice",
        "module": "Chapter 16 · High-Performance Leadership and Management",
        "one_line": "A bank's IT department as the Bells saw it: a room of visible goals, small teams, a daily board, and a limit on work in progress.",
        "summary": (
            "Part III is written by guests. Steve Bell and Karen Whitley Bell open "
            "Chapter 16 by asking what a lightweight management framework looks "
            "like in practice, and answer with a visit to ING Netherlands. Read the "
            "visit as a case, not a finding; then compute what a limit on work in "
            "process does to lead time on a squad's board."
        ),
        "key": [
            "a framework linking strategy to action",
            "the Obeya makes goals and problems visible",
            "tribes, squads and chapters; no fixed shape",
            "a board of demand and work in process",
            "lead time is work in process over throughput",
            "understand why; do not copy the behaviors",
        ],
        "key_label": "A management framework in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the Bells' own, the "
            "third the lab's."
        ),
        "concepts": [
            ("Obeya",
             "A room whose walls show a team's or a leader's goals, present "
             "performance, problems and work, so that anyone who steps in can see "
             "the state of things at a glance. ING's leadership room and each "
             "squad's workspace have one, and the Bells describe the squads' as "
             "alike enough to be read by colleagues from outside."),
            ("Tribe, squad and chapter",
             "ING's names for its structure. A tribe is a line of business, a "
             "squad is a self-steering team inside it with one customer mission, "
             "and a chapter gathers people of one discipline across squads to "
             "help them learn. The Bells present the shape as one that keeps "
             "changing."),
            ("Work in process (WIP)",
             "The items a team has started and not finished. For a steady flow, "
             "average lead time is average work in process divided by average "
             "throughput, a result known as Little's law. It is the lab's "
             "arithmetic, not the chapter's."),
        ],
        "read_title": "The chapter's question, the visit, and the board",
        "read_intro": (
            "Read the opening of Chapter 16 and its first section in your own copy "
            "first, with the introduction to Part III just before it. The lesson "
            "reads them as a case study and then puts numbers on one object in it, "
            "the squad's board."
        ),
        "body": [
            ("p", "Chapter 16 asks for &ldquo;a lightweight, high-performance "
                  "management framework that connects enterprise strategy with "
                  "action, streamlines the flow of ideas to value, facilitates rapid "
                  "feedback and learning&rdquo; and then puts the question this "
                  "lesson follows: what would one look like in practice rather than "
                  "in theory? The chapter is by Steve Bell and Karen Whitley Bell "
                  "of Lean IT Strategies, guests whom Forsgren, Humble and Kim "
                  "introduce at the head of Part III as people who coach leaders "
                  "through exactly this kind of change. Their opening argument is "
                  "that peak technical performance is necessary and not sufficient: "
                  "a team that ships quickly still has to know which experiences "
                  "customers value and how its work advances the enterprise's "
                  "strategy."),
            ("p", "Read the chapter for what it is. Parts I and II report what a "
                  "survey found. Chapter 16 is the Bells' account of what they saw "
                  "over repeated visits to ING Netherlands, a global bank, and the "
                  "words of ING's staff in it are, as its fourth note says, personal "
                  "communications with the Bells. It is a story told by people who "
                  "coached there, which is good evidence of what one organization "
                  "does and says it learned, and no evidence of how often it works "
                  "elsewhere. The chapter is open about that: its last section says "
                  "there is no checklist, and the next two lessons come back to it."),
            ("p", "The visit begins with Jannes Smit, an IT manager at ING who, seven "
                  "years before the chapter was written, began to experiment with "
                  "ways to make his teams learn as a body. His warning, which the Bells "
                  "keep for the start of their section, is that you have to "
                  "understand why and not just copy the behaviors. Their "
                  "guided tour takes in his leadership Obeya, a glass-walled room "
                  "where his work, priorities and actions are shown to his teams "
                  "and to anyone passing. It has four zones: strategic "
                  "improvement, performance monitoring, the portfolio roadmap and "
                  "leadership actions. Red and green make problems plain, and each "
                  "IT objective is tied in measurable terms to the enterprise's "
                  "strategy."),
            ("p", "Around the room is an organization of a particular kind. ING had "
                  "moved, two years before the chapter, to a matrix organized by "
                  "lines of business, which Lean practitioners would call value "
                  "streams. Each line is a tribe; a tribe holds squads, small "
                  "self-steering teams, each with a product owner, for IT an IT-area lead, "
                  "and a customer mission, and kept small by the two-pizza rule. "
                  "Most squads mix engineers and marketers, which ING calls "
                  "BizDevOps. "
                  "Chapters group people of one discipline across the squads to "
                  "spread knowledge, and centers of expertise gather specialists "
                  "such as enterprise architects. The Bells add that ING had "
                  "seen the need for a new bridging role, which it plans to call "
                  "the product area lead, and that it emerged from experience; "
                  "the caption of their Figure 16.2 says the "
                  "model has no fixed structure and keeps evolving."),
            ("p", "The squad's workspace is the part of the visit that a team of "
                  "your own could borrow most readily. Its walls hold the squad's "
                  "own Obeya, built to a few shared guidelines so that a colleague "
                  "from another squad can read it at a glance. They show what the "
                  "squad is aiming at and how far it is from that, the problems "
                  "that are new or have been passed up, the demand on the squad, "
                  "and the work in process and the work done. The Bells say that showing demand "
                  "helps the squad prioritize and keeps the amount of work in "
                  "process small. Each squad otherwise decides what to show and "
                  "how, being the best judge of what serves its own work."),
            ("p", "The research behind the book has something to say about two of "
                  "these walls. Appendix A lists using limits on work in process "
                  "and visual displays that monitor quality and work in process as "
                  "capabilities, in the lean management and monitoring category, "
                  "and making the flow of work visible as a product and process "
                  "capability. Chapters 7 and 8, read in Security, Lean Management "
                  "and Product Development, report them. Chapter 16 does not "
                  "claim a measurement of its own for ING; it shows what such "
                  "capabilities look like when a management team lives with them."),
            ("p", "Now put numbers on a board. The lab takes either a log of items "
                  "with the day each started and the day each finished, or a "
                  "throughput and one or two levels of work in process, and "
                  "returns average work in process, throughput and lead time. The "
                  "squad is invented, and the log covers ten days. On the preset "
                  "<code>board</code> eight items add up to 40 item-days, so the "
                  "average work in process is 4, the squad finishes 4/5 of an item "
                  "a day, and the average lead time is 5 days. Multiply the second "
                  "by the third and you get the first back: 4/5 times 5 is 4. That "
                  "identity is Little's law, proved from a trace in the System "
                  "Design lesson &ldquo;Little's Law from a Trace&rdquo;; "
                  "Chapter 16 neither states nor needs it."),
            ("p", "The preset <code>limit</code> asks the question the squad's "
                  "board invites. Keep the throughput at 4/5 of an item a day and "
                  "compare the usual work in process of 4 with a stated limit of "
                  "2. The lead time falls from 5 days to 2.5. Notice what was "
                  "assumed to get there: that throughput holds when the limit is "
                  "set. That is the whole bet of a limit and not a result of it, "
                  "and Appendix A says only that, used well, limits tend to drive "
                  "improvement, raise throughput and show where work is stuck. A "
                  "squad that cuts work in process and finds throughput falling in "
                  "step has learned something different, and its board will say "
                  "so."),
            ("h3", "Exercise"),
            ("ul", [
                "A squad finishes 3 items every 2 days, so its throughput is "
                "`3/2` an item a day.",
                "It usually has 9 items in process, and is considering a limit of 6.",
            ]),
            ("p", "Choose the preset <code>limit</code>, then type the throughput "
                  "and the two levels of work in process into the lab. Find the lead time at each, and then work out by hand "
                  "what level of work in process would give a lead time of 2 days "
                  "at this throughput."),
            ("p", "The Bells' squads meet at the board every morning. The next "
                  "lesson, Stand-ups, Catchball and Improvement Kata, reads how that "
                  "meeting works, how a problem travels from it up the "
                  "organization, and how a team states where it is and where it "
                  "means to be."),
        ],
        "lab": ("acckit", {
            "mode": "flow",
            "view": "wip",
            "preset": "board",
            "presets": [
                {"id": "board",
                 "label": "An invented squad's board: eight items over ten days",
                 "items": BOARD_LOG,
                 "days": 10,
                 "throughput": "-",
                 "expect": {"aflThru": "4/5 = 0.80 items a day", "aflAvgWip": "4 items", "aflAvgLead": "5 days", "aflLittle": "holds: average WIP 4 = throughput × average lead time"}},
                {"id": "limit",
                 "label": "The same throughput, with usual work in process of 4 and a limit of 2",
                 "throughput": "4/5",
                 "wip": "4 2",
                 "expect": {"aflThru": "4/5 = 0.80 items a day", "aflLeadAt": "WIP 4: 5 days; WIP 2: 5/2 = 2.50 days", "aflChange": "0.50× the lead time (5 → 5/2 = 2.50 days)"}},
            ],
            "panel_title": "A squad's board: work in process, throughput and lead time",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Reading a board with arithmetic",
        "steps_intro": "Five steps, the last of them on a board of your own.",
        "steps": [
            ("List the items",
             "Write each item with the day it was started and the day it was "
             "finished, over a window you choose, such as ten working days."),
            ("Add the item-days",
             "For each item subtract its start from its finish, and add them up. "
             "Divide by the length of the window: that is the average work in "
             "process."),
            ("Find throughput and lead time",
             "Divide the items finished by the length of the window for the "
             "throughput. Divide the item-days of the items done by their number "
             "for the average lead time."),
            ("Check the identity",
             "Multiply throughput by lead time. On a log where every item is "
             "done you get the average work in process back exactly; if an item "
             "is still open at the end of the window, the two differ, and the "
             "lab says which item."),
            ("Do it on a board of your own",
             "List the items your team finished in the last two weeks with the "
             "day each started and finished, and type them in. Compare the lead "
             "time the lab prints with what the team would have guessed."),
        ],
        "worked": {
            "title": "Eight items over ten days, then a limit of two",
            "intro": [
                "Work the preset <code>board</code> by hand, then set the limit of "
                "the preset <code>limit</code>.",
            ],
            "lines": [
                "item days: 6 + 4 + 6 + 3 + 7 + 5 + 5 + 4 = 40",
                "average work in process: 40 / 10 = 4",
                "throughput: 8 items / 10 days = 4/5 a day",
                "average lead time: 40 / 8 = 5 days",
                "check: (4/5) · 5 = 4",
                "with a limit of 2: 2 / (4/5) = 5/2 = 2.5 days",
            ],
            "after": [
                "Every line is a division. The last one holds throughput at 4/5, "
                "which nothing in the log promises; it is the assumption a limit "
                "asks you to test.",
            ],
        },
        "quiz_title": "The Bells' chapter and the board",
        "quiz": [
            {"q": "Who wrote Chapter 16, High-Performance Leadership and "
                  "Management?",
             "a": ["Nicole Forsgren, Jez Humble and Gene Kim, as the survey's "
                   "authors",
                   "Steve Bell and Karen Whitley Bell, guests whom the book's "
                   "authors invited to write Part III",
                   "Jannes Smit, the ING manager at the centre of the visit",
                   "Martin Fowler, who also wrote the first foreword"],
             "c": 1,
             "why": "The book's front matter credits Chapter 16 to Karen Whitley "
                    "Bell and Steve Bell of Lean IT Strategies, and the "
                    "introduction to Part III says the main authors asked them to "
                    "write it. Jannes Smit is the manager they visited and quote."},
            {"q": "In ING's structure as the chapter describes it, what is a "
                  "<em>chapter</em>?",
             "a": ["A self-steering team with one customer mission",
                   "A line of business delivering a portfolio of related products",
                   "People of one discipline, matrixed across squads, who help "
                   "squad members learn",
                   "A group of specialists such as enterprise architects, gathered "
                   "as a center of expertise"],
             "c": 2,
             "why": "A chapter, such as the Data Analytics Chapter, is a "
                    "discipline spread across squads. The self-steering team with "
                    "a mission is the squad, the line of business is the tribe, "
                    "and the group of specialists is a center of expertise."},
            {"q": "A squad finishes 3 items every 2 days, usually has 9 in "
                  "process, and considers a limit of 6. If throughput holds, what "
                  "are the lead times without and with the limit?",
             "a": ["13.5 days, then 9 days",
                   "6 days, then 6 days",
                   "1/6 of a day, then 1/4 of a day",
                   "6 days, then 4 days"],
             "c": 3,
             "why": "Lead time is work in process divided by throughput: 9 / (3/2) "
                    "is 6 days and 6 / (3/2) is 4. Multiplying instead of "
                    "dividing gives 13.5 and 9; keeping the lead time "
                    "at 6 forgets that the limit lowers the numerator; dividing "
                    "throughput by work in process turns the ratio upside down. "
                    "For a lead time of 2 days at that throughput the work in "
                    "process would be 2 · (3/2), which is 3 items."},
            {"q": "On the preset <code>limit</code> the lab shows the lead time "
                  "falling from 5 days to 2.5 with a limit of 2. What does that "
                  "result assume?",
             "a": ["That throughput stays at 4/5 of an item a day",
                   "That throughput falls to 2/5 of an item a day, in step with "
                   "the limit",
                   "That every item takes exactly 2.5 days",
                   "That the chapter has shown a limit halves lead time"],
             "c": 0,
             "why": "The lab holds the throughput you give it. If throughput fell "
                    "to 2/5 in step with the limit, the lead time would be 2 "
                    "divided by 2/5, which is still 5 days. Lead time here is an "
                    "average and no item is assumed to take exactly 2.5 days, and "
                    "Chapter 16 reports no such halving."},
        ],
        "mistakes": [
            ("Reading the visit to ING as a research finding",
             "Parts I and II report survey results with their samples and methods. "
             "Chapter 16 is the Bells' narrative of what they saw and were told, "
             "with quotations from ING staff that its notes call personal "
             "communications. It shows one organization's practices and what it "
             "says it learned; it does not show how often they work, and the "
             "chapter's own table marks which of its practices the survey research "
             "has tied to high performance."),
            ("Copying ING's structure",
             "Jannes Smit's own advice, which the Bells quote, is to understand "
             "why and not to copy the behaviors. The chapter's Figure 16.2 says "
             "the model has no fixed structure, and a bridging role arrived "
             "unplanned. Tribes and squads are a record of what ING's learning "
             "produced, not a design the chapter asks you to adopt."),
            ("Thinking a limit on work in process shortens lead time by itself",
             "Lead time is work in process divided by throughput, so a limit "
             "shortens it only if throughput holds. Appendix A says that used "
             "effectively a limit drives improvement and makes constraints "
             "visible; whether a particular team's throughput holds is what its "
             "board will show."),
        ],
        "standard": (
            "Finish when you can compute a board's lead time.",
            "Given a board's items with their start and finish days, or its "
            "throughput and work in process, compute average lead time, and say "
            "what the lab assumes about throughput when you set a limit."
        ),
        "note": (
            "The lab does arithmetic on a board you type. It cannot tell whether a "
            "board is kept up, whether a team trusts it, or whether a limit would "
            "leave throughput alone; the chapter gives no figure for any of those, "
            "and the squad here is invented."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 16, A High-Performing Management Framework in Practice,
    # continued (PDF pp. 226-234): the stand-up (p. 226), escalation and
    # catchball (p. 227, Figure 16.3), strategy deployment and PDCA (p. 228),
    # leaders as coaches (pp. 228-229), standard work (pp. 232-233), the
    # problem-solving approach (pp. 231-232). The four measures: Chapter 2,
    # pp. 49-51.
    # Quote: PDF p. 228 of the operator's copy, 11 words; PDF p. 228, 5 words
    # (the traditional question), quotes.py OK. Lesson total: 16 words.
    {
        "slug": "stand-ups-catchball-and-kata",
        "title": "Stand-ups, Catchball and Improvement Kata",
        "module": "Chapter 16 · High-Performance Leadership and Management",
        "one_line": "A fifteen-minute stand-up at a board, a route for problems to travel, and a way of stating where a team is and where it means to be.",
        "summary": (
            "The Bells walk past a squad's daily stand-up and follow what happens "
            "to a problem raised there. Read the rhythm they call catchball, the "
            "strategy deployment and cycle of learning it supports, and the problem "
            "solving ING settled on; then state a team's current condition and a "
            "target on the book's four delivery measures, and see which targets "
            "the next fortnight met."
        ),
        "key": [
            "stand at the board; note problems, not solve",
            "escalate up, share across: catchball",
            "strategy deployment is learning both ways",
            "do the work, improve it, develop people",
            "state the current condition, then a target",
            "a target met once is not yet a trend",
        ],
        "key_label": "Stand-ups and catchball in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Chapter 16's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Catchball",
             "The Bells' name for the vertical and horizontal passing of problems "
             "and learning that starts at the stand-up. A problem is noted, goes "
             "to a colleague, an area lead or a chapter or center of expertise as "
             "it needs, and the answer is relayed back along the same route."),
            ("Strategy deployment",
             "The Lean practice, called Hoshin Kanri, in which frontline teams "
             "learn the strategic priorities and the leaders learn about customers "
             "from the frontline. The Bells tie it to the cycle they also call "
             "PDCA, in which a team tries something, checks it and adjusts."),
            ("Current condition and target",
             "A team's measures as they stand, and the measures it means to reach "
             "next. The chapter names Kata among the methods ING tried and blended "
             "but does not set out its steps; the pair of words is borrowed here "
             "to state a starting point and an aim, in the lab, on the book's "
             "four delivery measures."),
        ],
        "read_title": "The stand-up, the route a problem takes, and the cycle",
        "read_intro": (
            "Read the rest of the chapter's first section, from the squad's "
            "stand-up to the end of the Jannes Smit interview, in your own copy "
            "first. The lesson reads it as a description of rhythm and routine, "
            "and then borrows the chapter's own call for measurement."
        ),
        "body": [
            ("p", "The Bells' tour of a squad reaches its daily stand-up. Standing "
                  "in front of a board of demand and work in process, each member "
                  "says in a few words what she or he is working on, what is in "
                  "the way, and what has been finished, and the board is updated "
                  "as they speak. It runs about fifteen minutes, and the Bells "
                  "report that it has cut the time people used to spend in "
                  "meetings; they give no measurement, and this is the "
                  "observation of coaches who were there. What the chapter says "
                  "next is about what the meeting is not for: problems are not "
                  "solved at the stand-up."),
            ("p", "The Bells describe a routine instead: a problem goes to "
                  "whoever can help, climbs a level when it must, and stays on the "
                  "board until the answer comes back down. The Bells call this pattern of vertical and "
                  "horizontal communication catchball, a leadership standard-work "
                  "practice, and their Figure 16.3 draws the rhythm; it is worth "
                  "reading in your copy, and this lesson does not reproduce it."),
            ("p", "The same channels carry learning among squads, chapters and "
                  "tribes, so that squads can decide for themselves how to shape "
                  "their work to the enterprise's strategy. The tribe lead, Jannes "
                  "Smit, learns from them too, including what squad members hear "
                  "from customers, and adapts his goals. The Bells describe the "
                  "whole exchange as &ldquo;a continuous, rapid feedback cycle of "
                  "learning, testing, validating, and adjusting&rdquo;, a form of "
                  "strategy deployment that Lean practitioners call Hoshin Kanri, "
                  "and which is also known as PDCA. Plan, do, check, act is older "
                  "than this book, and the chapter uses it as a name for a "
                  "habit."),
            ("p", "The chapter is as interested in the leader's part. Smit visits "
                  "the squads and asks questions in place of the old "
                  "&ldquo;Why isn&rsquo;t this getting done?&rdquo;, such as what the "
                  "squad is learning and how he can support it. The Bells say this "
                  "does not come easily, and that it takes coaching, mentoring and "
                  "modeling to move from command-and-control to leaders as coaches, "
                  "whose job and everyone's is threefold: do the work, improve "
                  "the work and develop the people. The third matters most, they "
                  "argue, where automation is changing technology jobs, because "
                  "people need to believe their leaders value them for the "
                  "ability to improve and not only for the present task."),
            ("p", "Improvement is given time. A fixed share of each squad's and "
                  "chapter's time is set aside for it, and Jordi de Vos, a chapter "
                  "lead the Bells meet, says squads treat it as regular work; the "
                  "chapter does not say what the share is. He is also "
                  "studying team security, the psychological safety to raise "
                  "problems without fear. His story about the leader's part "
                  "is concrete: asked to be twice as effective, the squads were told "
                  "by Smit that if quality was not there they should not release. "
                  "He would cover for them. The Bells call this slowing down to "
                  "speed up."),
            ("p", "How ING solves a problem is the nearest the chapter comes to "
                  "the kata of this lesson's title. The Bells report that the chapter "
                  "of Jan Rijkhoff tried A3, Kata, Lean startup and others before "
                  "settling on a blend of its own. The Bells describe ING's way as a loop: study the "
                  "present situation, test an idea against a measure, and make "
                  "what works the standard, at every level of the organization."),
            ("p", "The chapter says that one part of that approach is to decide how "
                  "and what to measure, and it does not say what ING measured. The "
                  "lab borrows the book's own four measures from Chapter 2: how "
                  "often you deploy, the lead time from commit to production, the "
                  "time to restore service, and the share of changes that fail. "
                  "They are the survey's measures of software delivery "
                  "performance, here taken from a log. The log is an invented "
                  "team's, over a fortnight. On the preset <code>current</code> "
                  "the lab counts 8 deployments, 4 a week, with a median lead "
                  "time of 61 hours, which the lab prints as 2 d 13 h and which falls in the option between one day "
                  "and one week. Two of the 8 changes failed, 25 percent, and the "
                  "two incidents were restored in 9 and 15 hours, a median of 12."),
            ("p", "That is a current condition. Suppose the team then states four "
                  "targets of its own, which are invented: a median lead time under "
                  "one day, a change fail rate of 15 percent or less, at least 7 "
                  "deployments a week, and a median time to restore under an hour. "
                  "The preset <code>next</code> adds the following fortnight: 10 "
                  "deployments, 5 a week, a median lead time of 19 hours, 1 failed "
                  "change out of 10, which is 10 percent, and one incident restored "
                  "in 3 hours. Two targets are met, lead time and change fail "
                  "rate; the deployment count and the restore time are not. "
                  "Each of the four moved the right way, as the log shows, and "
                  "only two crossed their line. Note too that the lab places the "
                  "deployment frequency in the same option, between once per day "
                  "and once per week, in both fortnights, though the weekly count "
                  "rose from 4 to 5: the book's six options are coarse, and a "
                  "target on the count sees what the option cannot."),
            ("p", "Read it the way the chapter reads its own results, which is "
                  "as something to learn from. The fortnight has ten changes, so "
                  "one more failure would have made the rate 20 percent and lost "
                  "a target, and one incident is a single event to take a median "
                  "of. The lab says "
                  "what the log says. It cannot say whether the stand-up caused "
                  "the better fortnight, which the Bells do not claim either: their "
                  "claim is that the rhythm is how a team notices and acts."),
            ("h3", "Exercise"),
            ("ul", [
                "A five-day period, with each change as `change, committed, "
                "deployed, failed` and times in hours from the start of the period.",
                "`x1, 0, 30, no; x2, 10, 34, no; x3, 20, 100, yes; x4, 50, 58, no; "
                "x5, 60, 90, no`",
            ]),
            ("p", "Type the changes into the lab. Find the median lead time and "
                  "the change fail rate, and say whether each meets the "
                  "lesson's targets. Then take out the slowest change and see how "
                  "far the median moves."),
            ("p", "The stand-up is one habit among several that the Bells ask "
                  "managers to build. The next lesson, Transforming Your "
                  "Leadership, Management, and Team Practices, reads how ING's "
                  "managers began, and why the chapter insists that you cannot "
                  "implement a culture."),
        ],
        "lab": ("acckit", {
            "mode": "delivery",
            "view": "metrics",
            "preset": "current",
            "presets": [
                {"id": "current",
                 "label": "An invented team's current condition: one fortnight",
                 "days": 14,
                 "changes": CURRENT_CHANGES,
                 "incidents": CURRENT_INCIDENTS,
                 "expect": {"adeDeploys": "8", "adePerDay": "4/7 ≈ 0.57", "adePerWeek": "4", "adeLead": "2 d 13 h", "adeLeadOpt": "between one day and one week", "adeFail": "1/4 = 25%", "adeFailBand": "16–30%", "adeRestore": "12 h", "adeRestoreOpt": "less than one day"}},
                {"id": "next",
                 "label": "The same team's next fortnight, beside the first",
                 "days": 14,
                 "changes": CURRENT_CHANGES,
                 "incidents": CURRENT_INCIDENTS,
                 "changes2": NEXT_CHANGES,
                 "incidents2": NEXT_INCIDENTS,
                 "expect": {"adeDeploys": "8 → 10", "adePerWeek": "4 → 5", "adeFreq": "between once per day and once per week → between once per day and once per week", "adeLead": "2 d 13 h → 19 h", "adeLeadOpt": "between one day and one week → less than one day", "adeFail": "1/4 = 25% → 1/10 = 10%", "adeFailBand": "16–30% → 0–15%", "adeRestore": "12 h → 3 h"}},
            ],
            "panel_title": "Current condition and next period on four measures",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Stating a condition and a target",
        "steps_intro": "Five steps, the last of them on a log of your own.",
        "steps": [
            ("Take a period and a log",
             "Pick a period such as a fortnight. List each change with the time "
             "it was committed and the time it reached production, and mark the "
             "ones that failed. List each incident with its start and its restore."),
            ("Read the four measures",
             "From the lab note the deployments, the median lead time, the "
             "failed share, and the median time to restore. That is the current "
             "condition, in numbers a team can see."),
            ("State targets",
             "Write a target for each measure that you could check from the same "
             "log, with a number and a direction. Say that they are yours."),
            ("Add the next period",
             "After the next fortnight, enter its log beside the first and mark "
             "which targets were met, which moved without crossing, and which "
             "went the wrong way."),
            ("Do it on a log of your own",
             "Take a fortnight of your team's changes and incidents from its "
             "tracker and type them in. Write one sentence on the first change "
             "you would make, as a hypothesis with the measure that would test "
             "it."),
        ],
        "worked": {
            "title": "Eight changes in a fortnight",
            "intro": [
                "Work the lead time and change fail rate of the preset "
                "<code>current</code> by hand. Lead time is the deployed hour less "
                "the committed hour.",
            ],
            "lines": [
                "lead times in hours: 54, 50, 68, 24, 50, 80, 90, 72",
                "sorted: 24, 50, 50, 54, 68, 72, 80, 90",
                "median: (54 + 68) / 2 = 61 hours, about 2.5 days",
                "change fail rate: 2 / 8 = 25 percent",
                "restore times in hours: 9, 15; median (9 + 15) / 2 = 12",
            ],
            "after": [
                "With an even number of values the median is the mean of the "
                "middle two. Against the target of one day, 61 hours is about two and a "
                "half times the target; against 15 percent, 25 is 10 points "
                "too high.",
            ],
        },
        "quiz_title": "The stand-up, the route and the targets",
        "quiz": [
            {"q": "In the stand-up as Chapter 16 describes it, what happens to a "
                  "problem a squad member raises?",
             "a": ["The whole squad solves it on the spot before the meeting ends",
                   "It is noted and kept visible; collaborators discuss it later, "
                   "and one needing the area lead is escalated",
                   "The product owner ranks it and puts it in the next quarter's "
                   "plan",
                   "It is held until the management team's next boot camp"],
             "c": 1,
             "why": "The Bells say problems are not solved at the stand-up; there is "
                    "a routine that makes sure they are resolved quickly, "
                    "with escalation where needed and the problem visible until "
                    "it is resolved. Nothing in the chapter waits for a boot camp "
                    "or a quarterly plan."},
            {"q": "How, according to the chapter, did ING settle on a way of "
                  "solving problems?",
             "a": ["By adopting Kata exactly as taught, in all its steps",
                   "By adopting A3 reports alone, written by each squad",
                   "By blending elements of methods such as A3, Kata and Lean "
                   "startup into an approach of their own",
                   "By having an outside consultancy prescribe a method"],
             "c": 2,
             "why": "The Bells report that a chapter experimented with several "
                    "methods and created its own blend. The chapter also says that ING does "
                    "not imitate a way of working prescribed in a book, and warns "
                    "against having consultants do the change for you."},
            {"q": "In the exercise, what are the median lead time and the change "
                  "fail rate of the five changes?",
             "a": ["34.4 hours and 20 percent",
                   "80 hours and 20 percent",
                   "30 hours and 25 percent",
                   "30 hours and 20 percent"],
             "c": 3,
             "why": "The lead times are 30, 24, 80, 8 and 30 hours, which sorted "
                    "are 8, 24, 30, 30, 80, so the median is 30. The mean, 34.4, "
                    "is the first wrong answer; 80 is just the middle record in "
                    "the order typed. One of 5 failed, which is 20 percent; "
                    "dividing by the 4 that did not fail gives 25. Taking out "
                    "the 80-hour change leaves a median of 27, which still misses "
                    "a one-day target."},
            {"q": "The lesson's four invented targets are a median lead time "
                  "under one day, a fail rate of 15 percent or less, at least 7 "
                  "deployments a week, and a median restore under an hour. How "
                  "many does the next fortnight in the preset <code>next</code> "
                  "meet?",
             "a": ["Two: lead time and change fail rate",
                   "Three: all but the restore time",
                   "One: change fail rate only",
                   "Four: every measure improved"],
             "c": 0,
             "why": "Next fortnight has a median lead time of 19 hours and a fail "
                    "rate of 10 percent, so those two targets are met. It has 5 "
                    "deployments a week against 7, and a restore of 3 hours "
                    "against under 1, so those are not, though every measure "
                    "moved the right way."},
        ],
        "mistakes": [
            ("Using the stand-up to solve problems",
             "The Bells say the opposite: during the stand-up problems are not "
             "solved, and a routine exists so that they are resolved rapidly. "
             "A problem goes to the people who can help, escalates when it needs "
             "to, and stays on the board until it is done. A meeting that tries "
             "to solve everything in the circle stops being fifteen minutes."),
            ("Taking the four measures to be ING's measures",
             "Forsgren, Humble and Kim chose deployment frequency, lead time, "
             "time to restore and change fail rate for their survey, in Chapter "
             "2. Chapter 16 does not tell us what ING measured; it says only "
             "that a hypothesis should include how and what to measure. The lab "
             "uses the four as a way to state a condition."),
            ("Reading one fortnight as a trend",
             "Ten changes and one incident are a small log. One more failed "
             "change would double the failed share. A target met in one period "
             "is a reason to look at the next, not a result; the Bells' own cycle "
             "is to keep monitoring to make sure an improvement is sustained."),
        ],
        "standard": (
            "Finish when you can state a condition and test a target.",
            "From a log of changes and incidents, state the four measures for a "
            "period, set a target for each, and say from the next period's log "
            "which targets were met."
        ),
        "note": (
            "The lab computes four measures from a log you type, for one or two "
            "periods. It does not know the targets; you compare them by eye. It "
            "cannot say whether a stand-up or any other practice caused a change, "
            "and a fortnight of ten changes is a small sample."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 16, Transforming Your Leadership, Management, and Team Practices
    # (PDF pp. 234-239): the question (p. 234), the quarterly cycle (p. 234),
    # leader standard work and the ten percent (p. 235), no checklist (p.
    # 235), Figure 16.4 (pp. 235-237), the mindset suggestions (pp. 238-239).
    # Chapter 11 on leaders alone, p. 161; Appendix B, p. 261; Appendix A,
    # pp. 244-251.
    # Quotes: PDF p. 235 of the operator's copy, 11 words; PDF p. 233, 16
    # words, quotes.py OK. Lesson total: 27 words.
    {
        "slug": "transforming-leadership-and-team-practices",
        "title": "Transforming Your Leadership, Management, and Team Practices",
        "module": "Chapter 16 · High-Performance Leadership and Management",
        "one_line": "How ING's managers began: a leader who learned first, a quarter of practice, and a warning that a culture cannot be implemented.",
        "summary": (
            "The second half of the Bells' chapter turns from what ING's days look "
            "like to how the change began. Read the question they prefer to "
            "'how do we change our culture', the first exercise of the "
            "management team, the table of practices they refuse to call a "
            "checklist, and their advice on mindset; then count the capabilities "
            "a team added in a quarter, by category."
        ),
        "key": [
            "ask how to learn, not how to change culture",
            "a leader starts, and learns first",
            "record how you spend your time",
            "a table of practices is not a checklist",
            "make it your own; grow your own coaches",
            "a count of capabilities is not a culture",
        ],
        "key_label": "Transforming practices in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the Bells', the others "
            "the book's and the lab's."
        ),
        "concepts": [
            ("Leader standard work",
             "The routines the Bells ask managers to develop: showing work "
             "visually, meeting briefly at a board, and coaching their people "
             "steadily, in place of long meetings and fire-fighting. ING's "
             "managers began by logging where their own days went."),
            ("Implementation thinking",
             "Trying to copy another company's specific behaviors and practices. "
             "The Bells call it, by its nature, contrary to the essence of a "
             "generative culture, and say that a culture cannot be implemented."),
            ("Capability profile",
             "For a team, the capabilities of Appendix A that are in place, "
             "counted in each of the book's five categories. The lab compares two "
             "dates; it counts what a team says it has, and does not score "
             "behavior."),
        ],
        "read_title": "The question, the first exercise, and the warning",
        "read_intro": (
            "Read the section Transforming Your Leadership, Management, and Team "
            "Practices in your own copy first, including the table that closes the "
            "chapter. The lesson reads it as advice from people who coach, and "
            "sets it beside what the research behind the book says about leaders."
        ),
        "body": [
            ("p", "The Bells put the point of their section in two sentences: "
                  "&ldquo;there is no checklist or playbook. You can&rsquo;t "
                  "&ldquo;implement&rdquo; culture change.&rdquo; Transforming "
                  "Your Leadership, Management, and Team Practices is built to "
                  "arrive there. They begin with a question "
                  "leaders put to them often, how do we change our culture, and "
                  "set it aside for better ones: how do we learn to learn, how can "
                  "learning be made safe for others, and how do new behaviors "
                  "turn into habits. At ING, they say, it began with "
                  "one leader asking himself those questions."),
            ("p", "That leader hired coaches to challenge everyone, himself "
                  "first, and his managers met each quarter to learn and spent the "
                  "months between making it habit. The Bells' picture is of "
                  "stretching, and stretching again, just as the team felt "
                  "comfortable."),
            ("p", "The first exercise was concrete. In an early boot camp the Bells "
                  "challenged the managers to develop leader standard work, "
                  "meaning work shown visually, short meetings at a board and steady "
                  "coaching of their people, in place of long meetings and "
                  "firefighting. To do it they first had to find out where their "
                  "days went, and for several weeks each logged the time and "
                  "measured it, shared what they found, and designed new ways "
                  "to work. Three months later one of "
                  "them said he would never go back. The managers also reached a "
                  "goal they had set, making a tenth of their time available for "
                  "what they chose. It is one management team's report in the "
                  "Bells' account, and a useful one: the first step was a "
                  "measurement of themselves."),
            ("p", "Then the warning. In the Bells' words, trying to imitate "
                  "another company's specific practices is contrary to the "
                  "essence of a generative culture, and a tribe lead whom they "
                  "quote says &ldquo;when you change the way you work, you change "
                  "the routines, you create a different culture&rdquo;. Westrum's "
                  "generative culture is Chapter 3's, read in Measuring and "
                  "Changing Culture, and Appendix A counts supporting one among "
                  "the cultural capabilities. Notice the order Smit "
                  "describes: routines first, culture after. The Bells say it "
                  "from experience of coaching; the survey of Chapter 3 measures "
                  "culture and relates it to performance, which is a different "
                  "kind of evidence."),
            ("p", "The chapter ends its argument with a table, Figure 16.4, of "
                  "team, management and leadership behaviors and practices drawn "
                  "from the visit. The Bells mark with an asterisk the ones that "
                  "research has found to go with high performance, and hope "
                  "that future research will explore the rest. They say it is "
                  "not a checklist but a distillation, general guidelines for "
                  "developing your own. The lesson does not reproduce it. The "
                  "useful thing it tells you is how much of the chapter is the "
                  "Bells' view and how much the book's data: the unstarred "
                  "practices are not ones the research has shown to go with high "
                  "performance."),
            ("p", "Their closing advice comes as a set of suggestions from their own "
                  "experience, and it is worth reading as such. Keep the right "
                  "mindset: learning, not the practices and certainly not the "
                  "tools. Make it your own, which they spell out as three "
                  "instructions: learn from other enterprises without copying "
                  "them; do not contract the change out to a large consulting "
                  "firm, because teams then feel it is done to them, though outside "
                  "coaching may be needed at first; and grow your own coaches. "
                  "Lead by example: a new culture is shown, not delegated. "
                  "Practice discipline, "
                  "patience and practice."),
            ("p", "The research behind the book supports part of this and "
                  "qualifies another. Appendix A lists supporting or embodying "
                  "transformational leadership as a capability, from Chapter 11, "
                  "and Appendix B reports high-performing teams with the strongest "
                  "leader behaviors. Chapter 11 and Appendix B also report that "
                  "teams with the top tenth of reported transformational "
                  "leadership were no more likely, and perhaps less, to be high "
                  "performers than the whole sample, and the chapter reads that "
                  "as leaders alone not being able to achieve high outcomes. The "
                  "Bells' own account has a leader who starts the change, and "
                  "then a management team, coaches and squads who carry it."),
            ("p", "The lab counts the capabilities of Appendix A that a team has in "
                  "place, by the book's five categories, on two dates. The team, "
                  "Orchid, is invented. On the preset <code>start</code> it has 9 "
                  "of the 24: 4 of 8 continuous delivery, 1 of 2 architecture, 1 of "
                  "4 product and process, 1 of 5 lean management and monitoring, "
                  "and 2 of 5 cultural. The preset <code>quarter</code> adds its "
                  "quarter: visible flow of work, limits on work in process, "
                  "visual displays and a learning culture, and lists them as added. "
                  "The preset <code>end</code> enters the end list alone, and "
                  "the lab prints 13 of 24 for Orchid. Comparing the two, three "
                  "categories changed: product and process to 2 of 4, lean "
                  "management and monitoring to 3 of 5, cultural to 3 of 5. "
                  "Continuous delivery and architecture did not."),
            ("p", "Read that count as the Bells would read a wall of problems: as a "
                  "place to ask a question. Why those four, and how did the team "
                  "come to them? They are, as it happens, the sort of practices "
                  "the visit to ING shows. But the count is of capabilities a team "
                  "reports it has. It does not show that the team changed its "
                  "routines, let alone its culture, and 13 is not a better team "
                  "than 9 in another place with other work. Treating the list as "
                  "a score to raise is exactly the checklist thinking the "
                  "chapter warns against."),
            ("h3", "Exercise"),
            ("ul", [
                "Pine, an invented team, starts a quarter with these in place: "
                "`version-control, continuous-integration, test-automation, "
                "customer-feedback, visual-displays, meaningful-work`.",
                "By the end it has added `deployment-automation, small-batches, "
                "team-experimentation, proactive-health-checks`.",
            ]),
            ("p", "Sort the capabilities into the five categories, using the "
                  "preset's list for each name. Find the category that gained "
                  "most, and how many of its capabilities Pine has at the end. "
                  "Then type the first list into the teams box as a record starting "
                  "<code>pine</code> and the ten at the end into the second-date "
                  "box to see what was added; the lab prints the category counts "
                  "of the first date only, so type the ten into the teams box "
                  "alone to read them for the end."),
            ("p", "The Bells finish by wishing the reader well on a journey of "
                  "learning, and the book's authors do the same. The next lesson, "
                  "Conclusion, reads their last three pages."),
        ],
        "lab": ("acckit", {
            "mode": "capability",
            "view": "profile",
            "preset": "quarter",
            "presets": [
                {"id": "start",
                 "label": "Orchid, an invented team, at the start of a quarter",
                 "capabilities": CAPABILITIES,
                 "teams": _teams(orchid=ORCHID_START),
                 "expect": {"acpOverall": "orchid 9 of 24", "acpCategories": "orchid: continuous-delivery 4 of 8, architecture 1 of 2, product-and-process 1 of 4, lean-management-and-monitoring 1 of 5, cultural 2 of 5", "acpAdded": "no second date given"}},
                {"id": "quarter",
                 "label": "Orchid at the start and at the end of the quarter",
                 "capabilities": CAPABILITIES,
                 "teams": _teams(orchid=ORCHID_START),
                 "teams2": _teams(orchid=ORCHID_END),
                 "expect": {"acpOverall": "orchid 9 of 24", "acpAdded": "orchid +4 (visible-flow-of-work, wip-limits, visual-displays, learning-culture)"}},
                {"id": "end",
                 "label": "Orchid at the end of the quarter, alone",
                 "capabilities": CAPABILITIES,
                 "teams": _teams(orchid=ORCHID_END),
                 "expect": {"acpOverall": "orchid 13 of 24", "acpCategories": "orchid: continuous-delivery 4 of 8, architecture 1 of 2, product-and-process 2 of 4, lean-management-and-monitoring 3 of 5, cultural 3 of 5", "acpAdded": "no second date given"}},
            ],
            "panel_title": "The capabilities a team added in a quarter",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Reading a quarter of change",
        "steps_intro": "Four steps, the last of them on a team of your own.",
        "steps": [
            ("List what is in place",
             "For a team, write which of Appendix A's 24 capabilities it has, by "
             "the team's own account, at the start of a period."),
            ("Count by category",
             "Count those in place in each of the five categories, against the "
             "category's size: 8, 2, 4, 5 and 5."),
            ("Repeat at the end",
             "List them again at the end of the period and name the capabilities "
             "added, and the categories that changed."),
            ("Do it on a team of your own",
             "Take a team you know and list its capabilities now. Ask the team "
             "which one it would most like to add next, and what routine it "
             "would change first to do so."),
        ],
        "worked": {
            "title": "Orchid's quarter, by category",
            "intro": [
                "Count the preset <code>quarter</code> by hand, with each "
                "category's size in brackets.",
            ],
            "lines": [
                "start: 4 (of 8) + 1 (of 2) + 1 (of 4) + 1 (of 5) + 2 (of 5) = 9",
                "added: visible flow of work, WIP limits, visual displays, learning culture",
                "end: 4 + 1 + 2 + 3 + 3 = 13",
                "categories changed: product and process, lean management, cultural",
            ],
            "after": [
                "The added capabilities fall one in product and process, two in "
                "lean management and monitoring and one in cultural, so three "
                "categories changed and the continuous delivery and architecture "
                "counts stayed at 4 and 1.",
            ],
        },
        "quiz_title": "The warning, the table and the quarter",
        "quiz": [
            {"q": "According to the Bells, what did ING's managers do first, before "
                  "developing new routines?",
             "a": ["They hired a large consulting firm to implement a new "
                   "methodology",
                   "They logged their own time use, day by day, for several "
                   "weeks",
                   "They copied the routines of another company's leaders",
                   "They surveyed their teams with the items for Westrum's "
                   "culture"],
             "c": 1,
             "why": "The first exercise was to find out where their days went, "
                    "which they found uncomfortable; they then shared "
                    "what they learned and developed new ways of working. The "
                    "Bells advise against contracting the change out and against "
                    "copying another company."},
            {"q": "What does the chapter say about Figure 16.4, its table of "
                  "behaviors and practices?",
             "a": ["It is a checklist of the 24 capabilities, to be adopted in order",
                   "Every practice in it is shown to cause high performance",
                   "It is a distillation or general guidelines, not a checklist; an "
                   "asterisk marks the practices that research has linked to high "
                   "performance",
                   "It reports the statistical results of the survey"],
             "c": 2,
             "why": "The Bells say the table is not a checklist, and that the "
                    "starred practices are those research shows to correlate with "
                    "high performance, in the hope that research will explore the "
                    "rest. The 24 capabilities are Appendix A's list; the table "
                    "reports no statistics."},
            {"q": "In the exercise, which category did Pine gain most in, and "
                  "how many of its capabilities does Pine have there at the "
                  "end?",
             "a": ["Continuous delivery, 4 of 8",
                   "Lean management and monitoring, 2 of 5",
                   "Product and process, 2 of 4",
                   "Product and process, 3 of 4"],
             "c": 3,
             "why": "Pine added one continuous delivery capability, two product and "
                    "process ones (small batches and team experimentation) and one "
                    "lean management and monitoring one. Product and process went "
                    "from 1 to 3 of 4. Continuous delivery has the most in place "
                    "(4 of 8) but gained only one; 2 of 4 would be its count if "
                    "only one had been added."},
            {"q": "On the preset <code>quarter</code> the team adds four "
                  "capabilities. In how many of the five categories does the "
                  "count change?",
             "a": ["Three", "Four", "Five", "Two"],
             "c": 0,
             "why": "The four additions are one product and process, two lean "
                    "management and monitoring, and one cultural, so three "
                    "categories change. Continuous delivery stays at 4 of 8 and "
                    "architecture at 1 of 2."},
        ],
        "mistakes": [
            ("Treating the table of practices as a checklist",
             "The Bells say plainly that Figure 16.4 is not a checklist and that "
             "there is no playbook. Some of its practices are starred as "
             "correlating with high performance in the research; the rest are "
             "not ones the research has shown to go with it. It is a distillation to develop your own behaviors "
             "from."),
            ("Hiring a firm to implement the new way of working",
             "The Bells' advice is not to contract out the change, because teams "
             "then feel it is being done to them and do not build the ability to "
             "sustain it. They allow that you may need outside coaching to "
             "establish a foundation at the start, and say that you must in the "
             "end be the agent of your own change and grow your own coaches."),
            ("Reading a quarter's capability count as a change of culture",
             "The count shows what a team reports it has in place. The Bells "
             "describe culture as what follows when people change their "
             "routines, and the research shows culture as measured by a survey. "
             "Neither is read off a tally of capabilities, and a team with 13 is "
             "not shown to be better than one with 9."),
        ],
        "standard": (
            "Finish when you can profile a team by category.",
            "Given a team's capabilities on two dates, count them in the five "
            "categories, name the ones added, and say what the count does not "
            "show."
        ),
        "note": (
            "The lab counts capabilities a team lists, by the categories of "
            "Appendix A, on two dates. It cannot tell whether a capability is "
            "really in place, whether routines or culture changed, or whether the "
            "additions caused any change in performance; the team is invented."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Conclusion (PDF pp. 241-243 of the operator's copy). The twice-as-likely
    # finding: Chapter 2, p. 58, and Appendix B, p. 253. The limits: Fowler's
    # foreword, pp. 15-16; Chapter 12, pp. 178-179; Chapter 15, pp. 213-214.
    # Quotes: PDF p. 242, 7 words; PDF p. 243, 4 words, quotes.py OK.
    # Lesson total: 11 words.
    {
        "slug": "conclusion",
        "title": "Conclusion",
        "module": "Conclusion",
        "one_line": "Three pages from the three authors: what the research found, what it asks of leaders, and what 'unequivocal' can honestly mean.",
        "summary": (
            "The book ends with a short look back and one instruction: develop your "
            "own capabilities. Read what the authors say they found, and read it "
            "against the limits the book itself states; then compare two groups on "
            "an invented sample, and see what 'twice as likely' does and does not "
            "carry."
        ),
        "key": [
            "delivery performance matters to every firm",
            "leadership, tools and culture all affect it",
            "you cannot buy or copy high performance",
            "develop capabilities that fit your context",
            "twice as likely is a ratio of shares",
            "a ratio in a sample is not a cause",
        ],
        "key_label": "The Conclusion in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the Conclusion's, the "
            "others the lab's."
        ),
        "concepts": [
            ("Software delivery performance",
             "The book's measure of how well a team delivers software, built from "
             "its lead time, deployment frequency and time to restore, with the "
             "change fail rate closely related. The Conclusion calls it critical "
             "to any organization doing business today, since nearly every "
             "company relies on software."),
            ("Ratio of shares",
             "The share of one group that met an outcome divided by the share of "
             "another. 'Twice as likely' is a ratio of shares of 2. It is not "
             "the ratio of the groups' counts unless the groups are the same "
             "size."),
            ("Odds ratio",
             "The odds in one group, met to not met, divided by the odds in "
             "another. It is a different number from the ratio of shares, and the "
             "lab shows both so as not to confuse them."),
        ],
        "read_title": "What the authors say, and what the book says about it",
        "read_intro": (
            "Read the Conclusion, three pages, in your own copy first. The lesson "
            "reads it as a summing-up and sets beside it the book's own account "
            "of how far its findings reach."
        ),
        "body": [
            ("p", "The Conclusion's last advice is short: &ldquo;you can&rsquo;t "
                  "buy or copy high performance&rdquo;, and a team has to develop "
                  "its own capabilities along a path that fits its context. "
                  "Forsgren, Humble and Kim write it at the end of three pages "
                  "looking back on their years of surveying people who work in "
                  "technology and publishing the State of DevOps Reports with "
                  "Puppet. The one point they say held every time is that "
                  "delivery performance matters to nearly any business, since "
                  "nearly any business runs on software. Many things affect it, "
                  "they add: leadership, tooling, automation and a culture that "
                  "keeps learning."),
            ("p", "They walk through the book's parts. Part I set out what they "
                  "found, starting from the case that delivery performance feeds "
                  "organizational performance, the commercial kind (profitability, "
                  "productivity, market share) and the noncommercial (efficiency, "
                  "effectiveness, customer satisfaction, mission goals). Part II "
                  "summarized the science: the design decisions and the analysis "
                  "methods. The capabilities that the authors say contribute to "
                  "delivery performance, in ways that are significant "
                  "statistically and in practice, are the book's core, and Part III is the Bells' chapter, one view "
                  "of what following the capabilities looks like for innovative "
                  "organizations."),
            ("p", "The ask is to leaders and teams alike. The authors hope the "
                  "book has shown the reader where to improve: in technology and "
                  "in business process, in how work feels, and in how "
                  "improvement is run. They add that it will take lasting effort and "
                  "investment over time. This is the same message, from the other "
                  "end, as the Bells' warning that a culture cannot be implemented: "
                  "what the research gives you is a list of capabilities worth "
                  "developing, not a method of installing them."),
            ("p", "Then comes the sentence a reader may want to look at twice: "
                  "&ldquo;our research is unequivocal&rdquo;, and the results are "
                  "worth it. Read it fairly, which means reading it with the book. "
                  "Martin Fowler's foreword, which recommends the book, adds "
                  "notes of caution: the data are surveys that capture "
                  "subjective perceptions, the sample may not reflect the "
                  "whole IT world, and he would be more confident when other "
                  "teams using different approaches confirmed the reasoning. "
                  "Chapter 12 says that wherever the book speaks of impact it "
                  "used inferential prediction, a theory-led design for settings "
                  "where experiments cannot be run, and that causal analysis, "
                  "which generally needs randomized studies, was not done because "
                  "the data for it were not there. Chapter 15 names the "
                  "limits of a snowball sample, whose data are strongly "
                  "influenced by the first invitations."),
            ("p", "The fairest reading of 'unequivocal' is that the survey's "
                  "results were consistent over its years, on the "
                  "relationships it tested. It is not a claim of proven cause, "
                  "and the book does not make one: an endorsement printed before the "
                  "title page speaks of a causal link, and the authors' own account "
                  "of their method does not. A reader who holds both, the strength of "
                  "the consistent findings and the stated limits of the design, "
                  "has read the book as its authors wrote it."),
            ("p", "One finding that the Conclusion's summary rests on is worth "
                  "recomputing, because it is easy to misread. Chapter 2 "
                  "reports that across several years the survey's high "
                  "performers were consistently twice as likely as low "
                  "performers to exceed their organizations' goals "
                  "of profitability, productivity and market share, as the "
                  "respondents rated them, and that in 2017 they were also "
                  "twice as likely to exceed noncommercial goals; Appendix B "
                  "repeats both. The groups come from the cluster analysis of "
                  "the four delivery measures. 'Twice as likely' compares two "
                  "shares: the share of high performers who exceeded their goals "
                  "over the share of low performers who did."),
            ("p", "The lab does that on an invented sample. Twenty-seven teams are "
                  "sorted into three groups of nine by delivery performance. On "
                  "the preset <code>twice</code>, 6 of the high group met their "
                  "organization's goals, which is 66.7 percent, 4 of the medium "
                  "group, 44.4, and 3 of the low group, 33.3. High over low is "
                  "a ratio of shares of 2, a gap of 33.3 percentage points. "
                  "The lab also prints the odds ratio, which is 4: the high "
                  "group's odds are 6 to 3 and the low group's 3 to 6. 'Twice as "
                  "likely' is the 2 and not the 4."),
            ("p", "The preset <code>uneven</code> uses two groups of different "
                  "sizes. Of 8 high-group teams, 6 met their goals, 75 percent; "
                  "of 10 low-group teams, 5 did, 50. The ratio of shares is 1.50, "
                  "the gap 25 points and the odds ratio 3. The direction is "
                  "the same as before and the size is not, which is the point "
                  "about any such figure: 'twice as likely' is a number about "
                  "the sample that produced it, in its years, and a different "
                  "sample may give 1.5 or 2.5."),
            ("p", "What the comparison cannot carry is the list that matters most "
                  "when a leader reads it. It does not say which way the "
                  "relationship runs, or that raising delivery performance "
                  "would lift the share meeting goals, which is the book's "
                  "theory-led prediction and not something a two-row table can "
                  "settle. It rests on a rating that a respondent gave of their "
                  "own organization against others, and on groups that were "
                  "clustered from the same survey. And it says nothing about "
                  "your team: your own log will give your own figures."),
            ("h3", "Exercise"),
            ("ul", [
                "A department sorts its 30 teams by delivery performance. Of 10 "
                "high-group teams, 8 met their goals; of 20 low-group teams, 8 "
                "did.",
                "As rows: `high, 10, 8; low, 20, 8`.",
            ]),
            ("p", "Find each group's share, the ratio of shares, the gap in "
                  "percentage points and the odds ratio. Then write one sentence "
                  "that the department could honestly say about the comparison, "
                  "and one thing it could not."),
            ("p", "The Conclusion points back at the capabilities. The last lesson, "
                  "Capabilities to Drive Improvement, and the Stats, reads the "
                  "two appendices that list them and the findings."),
        ],
        "lab": ("acckit", {
            "mode": "groups",
            "view": "likely",
            "preset": "twice",
            "presets": [
                {"id": "twice",
                 "label": "Twenty-seven invented teams, three groups of nine",
                 "rows": LIKELY_TWICE,
                 "first": "high",
                 "second": "low",
                 "expect": {"agrShares": "high 6 of 9 ≈ 66.7%; medium 4 of 9 ≈ 44.4%; low 3 of 9 ≈ 33.3%", "agrRatio": "2.00×", "agrDiff": "≈ +33.3 points", "agrOdds": "4.00"}},
                {"id": "uneven",
                 "label": "Two groups of different sizes: 8 high and 10 low",
                 "rows": LIKELY_UNEVEN,
                 "first": "high",
                 "second": "low",
                 "expect": {"agrShares": "high 6 of 8 = 75%; low 5 of 10 = 50%", "agrRatio": "1.50×", "agrDiff": "+25 points", "agrOdds": "3.00"}},
            ],
            "panel_title": "Who met their goals, by group",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Comparing two groups",
        "steps_intro": "Four steps, the last of them on your own teams.",
        "steps": [
            ("Count each group",
             "For each group write how many teams or people there are and how many "
             "met the outcome."),
            ("Turn counts into shares",
             "Divide met by the group's size. Do not compare the raw counts unless "
             "the groups are the same size."),
            ("Take the ratio and the gap",
             "Divide one share by the other for the ratio, and subtract for the "
             "gap in percentage points. Say which group is on top."),
            ("Do it on groups of your own",
             "Take two groups in your organization and an outcome you can count, "
             "such as teams that shipped on time, and type the counts in. Write "
             "what the ratio would and would not let you say."),
        ],
        "worked": {
            "title": "Two groups of different sizes",
            "intro": [
                "Work the preset <code>uneven</code> by hand: 8 high-group teams, "
                "6 met; 10 low-group teams, 5 met.",
            ],
            "lines": [
                "high share: 6 / 8 = 75 percent",
                "low share: 5 / 10 = 50 percent",
                "ratio of shares: 75 / 50 = 1.50",
                "gap: 75 - 50 = 25 percentage points",
                "odds: high 6 / 2 = 3, low 5 / 5 = 1; odds ratio 3 / 1 = 3",
            ],
            "after": [
                "Odds divide met by not met; shares divide met by all. The two "
                "ratios come close only when the outcome is rare, and here it is "
                "not.",
            ],
        },
        "quiz_title": "The Conclusion and the comparison",
        "quiz": [
            {"q": "What does the Conclusion say about a team's route to high "
                  "performance?",
             "a": ["You can buy it with the tools that the capabilities name",
                   "You cannot buy or copy it; you must develop your own "
                   "capabilities in a way that fits your context",
                   "You can copy it from the high performers by adopting their "
                   "practices exactly",
                   "You can reach it in a quarter if leadership is strong enough"],
             "c": 1,
             "why": "The authors say high performance cannot be bought or copied, "
                    "and that the path takes lasting effort and investment "
                    "over time. Nothing in the Conclusion promises a quarter."},
            {"q": "What does Chapter 12 say about causal analysis in the research?",
             "a": ["It was done by A/B testing every capability",
                   "It was done with partial least squares regression",
                   "It was not done, because the data it needs, generally from "
                   "randomized studies, were not available",
                   "It was done on the 2014 follow-up of publicly traded firms"],
             "c": 2,
             "why": "The chapter says the final levels of analysis (predictive, "
                    "causal and mechanistic) were not included for lack of the "
                    "data, and that causal analysis generally requires "
                    "randomized studies. The book's impact claims use inferential "
                    "prediction, and regression is how they were tested."},
            {"q": "In the exercise, 8 of 10 high-group teams and 8 of 20 low-group "
                  "teams met their goals. What are the ratio of shares and the "
                  "odds ratio?",
             "a": ["1.00 and 1.00",
                   "2 and 2",
                   "6 and 2",
                   "2 and 6"],
             "c": 3,
             "why": "The shares are 80 and 40 percent, a ratio of 2 and a gap "
                    "of 40 points. The odds are 8 to 2, which is 4, and 8 to 12, "
                    "which is 2/3; 4 divided by 2/3 is 6. Equal counts of 8 "
                    "tempt the answer 1.00, which ignores the group sizes; 6 and "
                    "2 swaps the two."},
            {"q": "On the preset <code>twice</code> the lab prints a ratio of "
                  "shares and an odds ratio for the high group over the low. "
                  "Which pair is right?",
             "a": ["2 and 4",
                   "4 and 2",
                   "2 and 2",
                   "1.50 and 3"],
             "c": 0,
             "why": "The shares are 6/9 and 3/9, whose ratio is 2. The odds are "
                    "6 to 3 and 3 to 6, that is 2 and 1/2, whose ratio is 4. "
                    "1.50 and 3 are the figures of the preset "
                    "<code>uneven</code>."},
        ],
        "mistakes": [
            ("Reading 'our research is unequivocal' as proof of cause",
             "Read fairly, the word is about how consistent the survey's "
             "results were. The book itself says its impact claims use inferential "
             "prediction, that causal analysis was not done for want of data, "
             "and Fowler's foreword asks for confirmation by other teams using "
             "other methods. Strong and consistent is not the same as proved."),
            ("Taking 'twice as likely' for twice the odds",
             "It is a ratio of two shares. The odds ratio on the same data is a "
             "different, larger number when the outcome is common, and the "
             "lab prints both so that you do not pass one off as the other."),
            ("Reading the Conclusion as 'copy the high performers'",
             "The authors say the opposite: you can't buy or copy high "
             "performance, and the path has to fit your context. The "
             "capabilities are things to develop; what the survey's high "
             "performers do is a reason to look at your own practice."),
        ],
        "standard": (
            "Finish when you can say what 'twice as likely' compares.",
            "Given two groups' sizes and the number in each that met an outcome, "
            "compute the shares, their ratio, the gap and the odds ratio, and say "
            "what the comparison cannot show."
        ),
        "note": (
            "The lab divides counts you give it. It cannot tell how the groups "
            "were formed or what 'met' meant, whether the outcome was a rating "
            "or a measurement, or which way any relationship runs; the teams are "
            "invented and the figure is of this sample."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Appendix A, Capabilities to Drive Improvement (PDF pp. 244-251) and
    # Appendix B, The Stats (pp. 252-265). The Quick Reference, p. 20. Chapter
    # 4's J-curve and the 2016 figures are not used.
    # Quote: PDF p. 252 of the operator's copy, 28 words, quotes.py OK.
    # Lesson total: 28 words.
    {
        "slug": "capabilities-and-the-stats",
        "title": "Capabilities to Drive Improvement, and the Stats",
        "module": "Appendices A and B · Capabilities to Drive Improvement and The Stats",
        "one_line": "Twenty-four capabilities in five categories, then a reference to what the research found about each, in the authors' own careful verbs.",
        "summary": (
            "Appendix A lists the 24 capabilities and says where each is read; "
            "Appendix B lists the statistical findings by category. Read them as "
            "references, with attention to the verbs, and then profile an "
            "invented organization's six teams by category to find where a "
            "capability is least often in place."
        ),
        "key": [
            "24 capabilities in five categories",
            "each points to the chapter that reads it",
            "correlation is not prediction or cause",
            "a prediction rests on theory and data",
            "a total hides the shape of a profile",
            "a figure belongs to its year and sample",
        ],
        "key_label": "The appendices in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is Appendix A's, the second "
            "Appendix B's, the third the lab's."
        ),
        "concepts": [
            ("Capability",
             "A practice or condition that the survey analysis tied to better "
             "software delivery, at a level of statistical significance. "
             "Appendix A counts 24, in five categories: "
             "continuous delivery, architecture, product and process, lean "
             "management and monitoring, and cultural."),
            ("Correlation and prediction",
             "Appendix B's two terms for how the findings are stated. A "
             "correlation says two variables move together; a prediction, which "
             "the authors call inferential, says one construct affects another "
             "on a theory tested against the data. Neither is a proof of cause."),
            ("Category profile",
             "For a team or an organization, how many of each category's "
             "capabilities are in place. It carries information that the single "
             "total hides."),
        ],
        "read_title": "A list, a reference, and the verbs in it",
        "read_intro": (
            "Skim Appendix A and Appendix B in your own copy first; they are "
            "references, not arguments. The lesson reads them for how the claims "
            "are worded, and then uses Appendix A's list as the lab's frame."
        ),
        "body": [
            ("p", "&ldquo;Correlation looks at how closely two variables move "
                  "together (or don&rsquo;t) but it doesn&rsquo;t tell us if one "
                  "variable&rsquo;s movement predicts or causes the movement in "
                  "another variable.&rdquo; Appendix B begins by saying this to "
                  "the reader, as a reminder, and then lists what the research "
                  "found, organized by category. This lesson takes the two "
                  "appendices that end the book. Appendix A is the list of "
                  "capabilities, each followed by the chapter that treats it. Appendix B is the statistical summary. Appendix C, on the "
                  "methods, is read in Surveys, Data and Statistical Methods."),
            ("p", "Appendix A lists 24 capabilities that the analysis tied to "
                  "better delivery performance, and sorts them into five "
                  "categories, in no particular order within each. "
                  "Continuous delivery has eight, all read in Chapter 4: version "
                  "control, deployment automation, continuous integration, "
                  "trunk-based development, test automation, test data "
                  "management, shifting security left and continuous delivery "
                  "itself. Architecture has two, from Chapter 5: a loosely "
                  "coupled architecture and empowered teams. Product and process "
                  "has four, from Chapter 8. Lean management and monitoring has "
                  "five, four from Chapter 7 and one from Chapter 13. Cultural "
                  "has five, from Chapters 3, 5, 10 and 11."),
            ("p", "The Quick Reference at the front of the book is the short form of "
                  "the same list, and says that Appendix A is the detailed guide; "
                  "the appendix is best used the way its authors call it, as a "
                  "handy list. A few of the entries "
                  "carry qualifications that are easy to lose, such as that "
                  "peer review does better than external change approval "
                  "boards, and that a team should keep its test data to the "
                  "least it needs. The lesson does not reproduce the "
                  "paragraphs. The lab's names for the capabilities are short "
                  "labels of its own for the book's 24, each written as one "
                  "hyphenated word because the kit takes names without spaces."),
            ("p", "Appendix B states the same findings the earlier chapters "
                  "reported, by category: organizational performance, software "
                  "delivery performance, quality, burnout and deployment pain, "
                  "technical capabilities, architecture, lean management, lean "
                  "product management, culture, identity, employee Net Promoter "
                  "Score and job satisfaction, leadership, diversity, and a "
                  "miscellany. It opens by defining "
                  "its verbs. A correlation is two things moving together. A "
                  "prediction, which the authors say is inferential prediction, "
                  "is a stronger statement, that one construct affects "
                  "another, used when an experiment cannot be run and tested "
                  "with regression. Read each line by its "
                  "verb: 'is correlated with' is one claim and 'predicts' "
                  "another, and Chapter 2 tells the reader that 'drives', "
                  "'affects' and 'impacts' are other words for the second, which "
                  "is still not a randomized test."),
            ("p", "Three kinds of line are worth reading with care. Some state a "
                  "result across years: the survey's high performers were twice "
                  "as likely as low performers to exceed organizational "
                  "performance goals, which the previous lesson recomputed. Some "
                  "state a result for one year and sample, and say so. A "
                  "follow-up to the 2014 data used respondents who named their "
                  "employer, just over a thousand of them in 355 companies. For "
                  "those at publicly traded companies the high performers' market "
                  "capitalization had grown 50 percent more over three years; the "
                  "appendix adds that later years could not repeat the analysis, "
                  "the data being too few. And some describe who answered: women "
                  "were 5 percent of respondents in 2015, then 6 percent, then "
                  "6.5 percent in 2017, which is the kind of fact "
                  "to weigh when Fowler's foreword wonders how the sample reflects "
                  "the IT world."),
            ("p", "The appendix is also candid in a way that a list of results "
                  "rarely is. It reports that teams with the strongest "
                  "transformational leaders were no more likely, and perhaps less, "
                  "to be high performers than the survey's teams as a whole, and, for "
                  "software delivery performance, that "
                  "the construct is made from three of the four measures, with "
                  "change fail rate highly correlated with it and left out. Those "
                  "are reasons not to read the capabilities as a recipe, or "
                  "the groups as a ladder."),
            ("p", "Now the lab, which uses Appendix A as its frame. Six teams of "
                  "one invented organization each list the capabilities they have "
                  "in place. On the preset <code>six-teams</code> the teams have "
                  "18, 14, 8, 13, 7 and 11 of the 24, and prints each team's "
                  "count in each category. Add a category's six counts by hand "
                  "and divide by its size times six, and the organization has 26 "
                  "of 48 continuous delivery capabilities in place, 5 of 12 in "
                  "architecture, 10 of 24 in product and process, 11 of 30 in "
                  "lean management and monitoring and 19 of 30 in cultural ones; "
                  "71 of the 144 possible in all. Three categories are below half, "
                  "lean management and monitoring lowest at 36.7 percent. These "
                  "organization-wide figures are summed by hand from the lab's "
                  "table, not printed by it. The lab's last tile shows team "
                  "experimentation in place in none of the six teams."),
            ("p", "The lab's other view is a team. On the preset "
                  "<code>same-total</code> two teams have 13 capabilities each: "
                  "Orchid, from the previous lesson, and Elm. Orchid is spread: "
                  "4 of 8 continuous delivery, 1 of 2 architecture, 2 of 4 "
                  "product and process, 3 of 5 lean management and 3 of 5 "
                  "cultural. Elm is lopsided, with 6 of 8 and 4 of 5 in "
                  "continuous delivery and culture but 1 of 4 and 1 of 5 in "
                  "product and process and lean management. The same total gives "
                  "two different pictures, which is why Appendix A sorts the "
                  "capabilities and does not rank them."),
            ("h3", "Exercise"),
            ("ul", [
                "Willow, an invented team, has these ten in place: "
                "`version-control, deployment-automation, continuous-integration, "
                "test-automation, loosely-coupled-architecture, empowered-teams, "
                "customer-feedback, small-batches, generative-culture, "
                "meaningful-work`.",
            ]),
            ("p", "Count Willow's capabilities in each of the five categories, "
                  "against the category's size. Find the category with none in "
                  "place and the one with every capability in place. Then type "
                  "the team into the lab as a record starting <code>willow</code> to "
                  "check."),
            ("p", "That is the last lesson of the read-along. The appendices point "
                  "back to the chapters, and the chapters to the surveys; from "
                  "here the book's practice is your own team's, as its "
                  "authors say, to be developed and measured on its own log."),
        ],
        "lab": ("acckit", {
            "mode": "capability",
            "view": "profile",
            "preset": "six-teams",
            "presets": [
                {"id": "six-teams",
                 "label": "An invented organization: six teams, by category",
                 "capabilities": CAPABILITIES,
                 "teams": SIX_TEAMS,
                 "expect": {"acpOverall": "alder 18 of 24; birch 14 of 24; cedar 8 of 24; elm 13 of 24; fir 7 of 24; hazel 11 of 24", "acpFewest": "0 of 6 teams: team-experimentation"}},
                {"id": "same-total",
                 "label": "Two invented teams with 13 capabilities each",
                 "capabilities": CAPABILITIES,
                 "teams": SAME_TOTAL,
                 "expect": {"acpOverall": "orchid 13 of 24; elm 13 of 24", "acpCategories": "orchid: continuous-delivery 4 of 8, architecture 1 of 2, product-and-process 2 of 4, lean-management-and-monitoring 3 of 5, cultural 3 of 5; elm: continuous-delivery 6 of 8, architecture 1 of 2, product-and-process 1 of 4, lean-management-and-monitoring 1 of 5, cultural 4 of 5"}},
            ],
            "panel_title": "Six teams' capabilities, by category",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Profiling an organization",
        "steps_intro": "Five steps, the last of them on teams of your own.",
        "steps": [
            ("Fix the frame",
             "Take Appendix A's 24 capabilities in their five categories, of "
             "sizes 8, 2, 4, 5 and 5."),
            ("List each team's capabilities",
             "For each team write the capabilities it has in place, by its own "
             "account, as a short list."),
            ("Count by category",
             "For each category add the teams' capabilities in place, and divide "
             "by the category's size times the number of teams."),
            ("Find the thin spots",
             "Note the categories with the smallest shares and the capabilities "
             "the fewest teams have. They are places to ask why."),
            ("Do it on teams of your own",
             "List three teams you know and type them in. Write one sentence on "
             "a capability none has, and what routine might bring it."),
        ],
        "worked": {
            "title": "Six teams, by category",
            "intro": [
                "Work two of the categories of the preset <code>six-teams</code> "
                "by hand: architecture has 2 capabilities and lean management and "
                "monitoring has 5, across 6 teams.",
            ],
            "lines": [
                "architecture in place, by team: 2, 1, 0, 1, 0, 1 = 5",
                "architecture possible: 2 · 6 = 12; share 5 / 12 = 41.7 percent",
                "lean management in place, by team: 3, 2, 2, 1, 1, 2 = 11",
                "lean management possible: 5 · 6 = 30; share 11 / 30 = 36.7 percent",
            ],
            "after": [
                "Dividing by the number possible keeps a category of two "
                "capabilities from looking small beside one of five. The lowest "
                "share says where to look first, not where the organization has "
                "gone wrong.",
            ],
        },
        "quiz_title": "The appendices and the profile",
        "quiz": [
            {"q": "How many capabilities does Appendix A list, and in how many "
                  "categories?",
             "a": ["24, in four categories",
                   "24, in five categories",
                   "20, in five categories",
                   "25, in six categories"],
             "c": 1,
             "why": "Appendix A lists 24 key capabilities in five categories: "
                    "continuous delivery, architecture, product and process, "
                    "lean management and monitoring, and cultural."},
            {"q": "What does Appendix B say a correlation does not tell us?",
             "a": ["Whether two variables move together at all",
                   "Whether the two variables were measured by survey",
                   "Whether either variable predicts or causes the other",
                   "How large the sample was"],
             "c": 2,
             "why": "Correlation shows how closely two variables move together; "
                    "it does not tell us whether one predicts or causes the other, "
                    "since a third variable or chance can produce the same "
                    "movement. Whether they move together is what it does tell us."},
            {"q": "In the exercise, which category of Willow's has none in place "
                  "and which has every capability in place?",
             "a": ["None in architecture; all in lean management and monitoring",
                   "None in cultural; all in continuous delivery",
                   "None in product and process; all in cultural",
                   "None in lean management and monitoring; all in architecture"],
             "c": 3,
             "why": "Willow has 4 of 8 in continuous delivery, 2 of 2 in "
                    "architecture, 2 of 4 in product and process, 0 of 5 in "
                    "lean management and monitoring and 2 of 5 in cultural. "
                    "Architecture is the only category with every capability, "
                    "and lean management and monitoring the only one with none."},
            {"q": "On the preset <code>six-teams</code>, which category has the "
                  "smallest share of its capabilities in place across the six "
                  "teams?",
             "a": ["Lean management and monitoring, 11 of 30",
                   "Architecture, 5 of 12",
                   "Product and process, 10 of 24",
                   "Continuous delivery, 26 of 48"],
             "c": 0,
             "why": "The shares are 36.7 percent for lean management and "
                    "monitoring, 41.7 for both architecture and product and "
                    "process, and 54.2 for continuous delivery. Architecture has "
                    "the fewest in place in number (5), which is why the shares, "
                    "not the counts, are compared."},
        ],
        "mistakes": [
            ("Reading every line of Appendix B as a cause",
             "The appendix defines its own verbs. A correlation is two variables "
             "moving together, and may be due to a third variable or to chance; "
             "a prediction is an inference from a theory tested on survey data; "
             "neither is a randomized test of cause. Read the verb on each line."),
            ("Reading a capability total as a maturity score",
             "Two teams can have 13 of 24 and very different profiles. Appendix "
             "A groups capabilities by kind and presents them in no particular "
             "order; it does not rank them or give a level. A total can hide the "
             "category where a team is thin."),
            ("Carrying a figure out of its year and sample",
             "The 50 percent higher market capitalization growth comes from a "
             "follow-up to the 2014 data, among just over a thousand respondents "
             "in 355 companies, publicly traded ones among them, and the appendix "
             "says it could not be repeated. A figure belongs to the sample and the year "
             "that produced it."),
        ],
        "standard": (
            "Finish when you can profile teams by category.",
            "Given teams' capabilities in place, count them in the five "
            "categories, divide by the number possible, and name the thinnest "
            "category and the capability the fewest teams have."
        ),
        "note": (
            "The lab counts capabilities that teams list, in Appendix A's "
            "categories. It cannot tell whether a capability is truly in place, "
            "how well, or what any of them does for performance; the findings in "
            "Appendix B are the survey's, and the organization here is invented."
        ),
    },
]
