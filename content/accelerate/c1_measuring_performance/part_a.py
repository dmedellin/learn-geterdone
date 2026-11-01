"""Accelerate and Measuring Performance, lessons 1-5 -- the Preface, Chapter 1
and Chapter 2.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): the Preface; Chapter 1,
Accelerate (Focus on Capabilities, Not Maturity; Evidence-Based
Transformations Focus on Key Capabilities; The Value of Adopting DevOps);
Chapter 2, Measuring Performance (The Flaws in Previous Attempts to Measure
Performance; Measuring Software Delivery Performance; The Impact of Delivery
Performance on Organizational Performance; Driving Change). Pages in the
comments are PDF pages of the operator's copy; the lessons cite by chapter and
section. Every quotation is copied from that copy and checked with quotes.py.
The samples are written for these lessons: none of the book's tables, figures
or data is reproduced. The design is docs/accelerate/PLAN.md, section C,
Course 1.
"""


def _lines(text):
    """A constant as a list of lines."""
    return text.split("\n")


_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)


# ---------------------------------------------------------------- 01 samples

# The book's 24 capabilities and five categories (Quick Reference, PDF pp.
# 20-22, and Appendix A) are facts; the teams and the ladder are invented.
_CATEGORY_CD = "continuous delivery"
_CATEGORY_AR = "architecture"
_CATEGORY_PP = "product and process"
_CATEGORY_LM = "lean management and monitoring"
_CATEGORY_CU = "cultural"

_CAPABILITIES = [
    ("version control", _CATEGORY_CD),
    ("deployment automation", _CATEGORY_CD),
    ("continuous integration", _CATEGORY_CD),
    ("trunk-based development", _CATEGORY_CD),
    ("test automation", _CATEGORY_CD),
    ("test data management", _CATEGORY_CD),
    ("shift left on security", _CATEGORY_CD),
    ("continuous delivery", _CATEGORY_CD),
    ("loosely coupled architecture", _CATEGORY_AR),
    ("empowered teams", _CATEGORY_AR),
    ("customer feedback", _CATEGORY_PP),
    ("value stream", _CATEGORY_PP),
    ("working in small batches", _CATEGORY_PP),
    ("team experimentation", _CATEGORY_PP),
    ("change approval processes", _CATEGORY_LM),
    ("monitoring", _CATEGORY_LM),
    ("proactive notification", _CATEGORY_LM),
    ("WIP limits", _CATEGORY_LM),
    ("visualizing work", _CATEGORY_LM),
    ("Westrum organizational culture", _CATEGORY_CU),
    ("supporting learning", _CATEGORY_CU),
    ("collaboration among teams", _CATEGORY_CU),
    ("job satisfaction", _CATEGORY_CU),
    ("transformational leadership", _CATEGORY_CU),
]


def _h(name):
    """A name as the lab reads it: words joined by hyphens."""
    return name.replace(" ", "-")


CAPABILITIES = "; ".join("%s, %s" % (_h(a), _h(b)) for a, b in _CAPABILITIES)

# Two invented teams. Atlas has fourteen of the twenty-four in March; Brook has
# eight, all of them in the first category.
ATLAS = [
    "version control", "deployment automation", "continuous integration",
    "test automation", "empowered teams", "customer feedback",
    "working in small batches", "monitoring", "WIP limits", "visualizing work",
    "Westrum organizational culture", "supporting learning",
    "collaboration among teams", "job satisfaction",
]
ATLAS_LATER = ATLAS + [
    "trunk-based development", "shift left on security",
    "loosely coupled architecture",
]
BROOK = [
    "version control", "deployment automation", "continuous integration",
    "trunk-based development", "test automation", "test data management",
    "shift left on security", "continuous delivery",
]


def _team(name, has):
    return "%s, %s" % (name, ", ".join(_h(c) for c in has))


# An invented three-step ladder, of the kind the lesson argues against.
LADDER = (
    "1, version-control, deployment-automation; "
    "2, continuous-integration, test-automation, trunk-based-development; "
    "3, continuous-delivery, loosely-coupled-architecture, monitoring"
)


# ---------------------------------------------------------------- 02 samples

# A review that takes two hours of hands-on work, at five utilizations.
UTIL_LADDER = "50, 80, 90, 95, 99"


# ---------------------------------------------------------------- 03 samples

# A fortnight's log for a team that ships small changes: ten changes, one of
# which failed, and two incidents. Times are day.hh:mm from the period start.
FORTNIGHT_CHANGES = (
    "c01, 1.09:00, 1.15:00, no; c02, 2.10:00, 2.14:00, no; "
    "c03, 3.09:30, 4.11:30, no; c04, 5.13:00, 5.16:00, no; "
    "c05, 8.09:00, 8.17:00, no; c06, 9.10:00, 9.12:00, yes; "
    "c07, 10.14:00, 11.10:00, no; c08, 12.09:00, 12.13:00, no; "
    "c09, 13.11:00, 13.16:00, no; c10, 14.09:00, 14.12:00, no"
)
FORTNIGHT_INCIDENTS = "i1, 6.08:00, 6.20:00; i2, 9.12:30, 9.15:30"

# Four weeks for a team that gathers its changes and ships them together:
# seven changes in three deployments, two of them failed.
BATCHED_CHANGES = (
    "d01, 2.10:00, 10.10:00, no; d02, 4.14:00, 10.10:00, no; "
    "d03, 7.09:00, 10.10:00, no; d04, 12.09:00, 19.10:00, yes; "
    "d05, 15.16:00, 19.10:00, yes; d06, 21.10:00, 28.10:00, no; "
    "d07, 26.12:00, 28.10:00, no"
)
BATCHED_INCIDENTS = "j1, 19.11:00, 21.11:00; j2, 19.14:00, 20.14:00"

# ---------------------------------------------------------------- 04 samples

# Ten invented teams, coded 1 (best) to 6 on the four measures: deployment
# frequency, lead time, time to restore, change fail rate. Written so that
# Ward's method with k = 3 finds a group of four and two of three, with whole
# medians.
TEAMS = {
    "T01": (1, 1, 2, 2),
    "T02": (2, 2, 2, 2),
    "T03": (1, 1, 2, 1),
    "T04": (1, 1, 1, 2),
    "T05": (4, 3, 3, 4),
    "T06": (3, 4, 3, 3),
    "T07": (3, 3, 4, 3),
    "T08": (6, 4, 6, 4),
    "T09": (5, 5, 4, 5),
    "T10": (4, 5, 5, 4),
}
TEN_TEAMS = "; ".join(
    "%s, %s" % (name, ", ".join(str(v) for v in codes))
    for name, codes in sorted(TEAMS.items())
)

# 04 exercise: four teams.
FOUR_TEAMS = "Quay, 1, 1, 1, 2; Ridge, 1, 2, 1, 2; Shoal, 4, 4, 3, 3; Tarn, 5, 4, 3, 4"


# ---------------------------------------------------------------- 05 samples

# Forty invented teams: twenty high performers and twenty low, and whether
# each exceeded a goal.
GOAL_HALF = "high, 20, 12; low, 20, 6"
GOAL_RARE = "high, 20, 4; low, 20, 2"
GOAL_EXERCISE = "high, 20, 18; low, 20, 9"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Preface (PDF pp. 23-33 of the operator's copy): the research (p. 24),
    # the journey and the data (pp. 25-27), the four years (pp. 28-31).
    # Chapter 1 (pp. 35-43): software at the heart (pp. 35-37), executives and
    # practitioners (pp. 37-38), Focus on Capabilities, Not Maturity (pp.
    # 38-40), Evidence-Based Transformations (pp. 41-42), The Value of
    # Adopting DevOps (pp. 42-43). Fowler's foreword, pp. 14-16.
    # Quote: PDF p. 38 of the operator's copy, 18 words, quotes.py OK.
    # Figures: over 23,000 responses and over 2,000 organizations (p. 24);
    # 2014 through 2017 (p. 27); 24 capabilities, five categories (pp. 20,
    # 42); 46, 440, 170 and 5 (p. 42), the gap narrowing for tempo and
    # widening for stability against 2016 (p. 43).
    # Lesson total: 18 words.
    {
        "slug": "capabilities-not-maturity",
        "title": "Capabilities, Not Maturity",
        "module": "Preface and Chapter 1 · Accelerate",
        "one_line": "Four years of survey research, 24 capabilities in five categories, and the authors' case for measuring what a team can do rather than which level it has reached.",
        "summary": (
            "The Preface says where the book's evidence comes from: four years of "
            "surveys, 2014 to 2017, and a method borrowed from academic research. "
            "Chapter 1 says what to do with it: measure capabilities, not maturity. "
            "Read the authors' four reasons against maturity models, the three "
            "often-cited factors that did not predict performance, and the 2017 "
            "gap between high and low performers; then see in a small profile what "
            "a single level hides."
        ),
        "key": [
            "four years of surveys, 2014 to 2017",
            "24 capabilities, in five categories",
            "a level says where you stopped",
            "capabilities are levers on outcomes",
            "a profile belongs to one team",
            "a survey finding is not a promise",
        ],
        "key_label": "Capabilities, not maturity, in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the book's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Capability",
             "Something a team or organization can do, such as keep its work in "
             "version control or release without a freeze, that the research found "
             "to drive an outcome. The book lists 24, sorted into five categories: "
             "continuous delivery, architecture, product and process, lean "
             "management and monitoring, and cultural."),
            ("Maturity model",
             "A ladder of levels, each defined by what a team has in place, that a "
             "team climbs and then has arrived. The authors' objection is to the "
             "ladder as a way of measuring, not to any one practice on it."),
            ("Profile",
             "The lab's word for which of the capabilities a team has in place, "
             "counted by category. A profile has no top; the lab sets it beside a "
             "stated ladder to show what the ladder's single level leaves out."),
        ],
        "read_title": "Where the evidence comes from, and what to measure",
        "read_intro": (
            "Read the Preface and Chapter 1 in your own copy first, and Martin "
            "Fowler's foreword if you have not. The lesson takes them in the order "
            "of the book: the research, the case for capabilities, the evidence "
            "that some often-cited factors do not matter, and the gap the authors "
            "report for 2017."
        ),
        "body": [
            ("p", "The Preface and Chapter 1 are the book's overture, and Chapter 1 "
                  "makes its first argument in one sentence about how to measure "
                  "change. Of maturity models, the authors write that "
                  "&ldquo;we cannot stress enough that maturity models are not the "
                  "appropriate tool to use or mindset to have&rdquo;. This lesson "
                  "reads that argument, and the research behind the book that the "
                  "Preface describes, then computes a small team's profile of "
                  "capabilities to show what the argument is about."),
            ("p", "The Preface first. Forsgren, Humble and Kim began working "
                  "together in late 2013, with the team at Puppet, on the 2014 State "
                  "of DevOps Report, and the book covers four years of findings: "
                  "2014 through 2017. Over those years they report more than 23,000 "
                  "survey responses from more than 2,000 organizations, from "
                  "startups to enterprises, in finance, healthcare and government as "
                  "well as internet companies. The data came from surveys sent to "
                  "mailing lists and social media, and readers were asked to pass "
                  "them on, which the authors call snowball sampling and defend in "
                  "Chapter 15. In the first year they moved from yes-or-no "
                  "questions to Likert-type ones, answers on a range from strongly "
                  "disagree to strongly agree, which let them collect shades of "
                  "gray. Each year asked a new set of questions: whether delivery "
                  "can be measured and whether it matters to the organization "
                  "(2014); technical and lean management practices, and deployment "
                  "anxiety and burnout (2015); security, trunk-based development, "
                  "lean product management and loyalty (2016); architecture, "
                  "leadership and not-for-profit outcomes (2017)."),
            ("p", "The Preface also says what kind of study this is: a "
                  "cross-sectional one, which asks many people about the present "
                  "and looks for relationships among their answers, the method of "
                  "much healthcare and workplace research. Keep that in view. "
                  "Martin Fowler's foreword, written by a reader who says he is "
                  "usually sceptical of such reports, gives the strongest reasons "
                  "to trust the book and the plainest cautions. These are surveys "
                  "that capture subjective perceptions, he notes, and he wonders "
                  "how well the sample reflects the IT world; he would feel more "
                  "confident when other teams, using other approaches, confirm the "
                  "reasoning; and the book covers the journey from commit to "
                  "production, not all of software development. Every lesson in "
                  "this course inherits those cautions."),
            ("p", "Chapter 1 begins with the claim that software is at the heart of "
                  "acceleration in every industry, and cites outside studies and "
                  "industry reports for it. The one that matters most for what "
                  "follows is a report from Forrester, which the authors read as "
                  "showing that organizations often overestimate their progress in "
                  "DevOps, and executives more than the people doing the work. If "
                  "the practitioners' estimates are the more accurate, the authors "
                  "argue, two things follow: there is more value waiting than "
                  "executives think, and progress has to be measured, and the "
                  "measurements shared with leaders."),
            ("p", "Then the section the lesson is named for, Focus on Capabilities, "
                  "Not Maturity. A maturity model sets out levels and assesses a "
                  "team against them. The authors give four reasons against the "
                  "approach. Maturity models aim at arriving, and a transformation "
                  "has no arrival. They are lock-step, as if level one and level "
                  "two looked the same in every team, where capability models are "
                  "multidimensional and let each part of an organization work on "
                  "what helps it most. They often measure the tooling a team has "
                  "installed without tying it to an outcome, which the authors call "
                  "vanity metrics. And they fix a static level, while the industry "
                  "moves: what counted as high-performing one year, the authors "
                  "found, was not enough the next."),
            ("p", "The next section, Evidence-Based Transformations Focus on Key "
                  "Capabilities, says why a particular list. Vendors and "
                  "consultants, the authors observe, favour the capabilities that "
                  "suit what they sell, and organizations design homegrown "
                  "assessments or freeze at the number of things to fix. Their "
                  "alternative is evidence: of the factors people often cite, three "
                  "did not predict performance, namely the age and technology of "
                  "the application (mainframe against greenfield), whether "
                  "operations or development staff performed deployments, and "
                  "whether a change approval board was in place. What did "
                  "predict it, they report, were 24 capabilities, which the Quick "
                  "Reference and Appendix A list with the chapter that treats each. "
                  "They are in no particular order, and the five categories are the "
                  "ones named above."),
            ("p", "The Value of Adopting DevOps ends the chapter with a number from "
                  "Chapter 2's survey. In 2017, comparing high performers with low "
                  "performers, the authors report that the first deployed code 46 times as often, got a commit to production 440 times as fast, recovered from downtime 170 times as fast and had a fifth of the failure rate. Against 2016 the gap narrowed for tempo and "
                  "widened for stability, which they suspect is because low "
                  "performers were pushing for speed without building quality in. "
                  "These are comparisons of two groups of survey respondents in one "
                  "year; the next lesson says how the groups were drawn."),
            ("p", "Now the profile. The lab takes the 24 capabilities, each with "
                  "its category, and a team's list of those it has in place, and "
                  "counts them by category. It can also take a ladder, and finds "
                  "the highest level whose requirements, and those of every level "
                  "below it, the team meets. The sample is two invented teams and "
                  "an invented three-level ladder: level 1 asks for version control "
                  "and deployment automation; level 2 adds continuous integration, "
                  "test automation and trunk-based development; level 3 adds "
                  "continuous delivery, a loosely coupled architecture and "
                  "monitoring. The ladder is the lesson's, an example of the kind "
                  "the authors argue against, and not a model from the book."),
            ("p", "On the preset <code>one-team</code> the team `Atlas` has 14 of "
                  "the 24 in place: 4 of 8 in continuous delivery, 1 of 2 in "
                  "architecture, 2 of 4 in product and process, 3 of 5 in lean "
                  "management and monitoring, and 4 of 5 in culture. It has "
                  "continuous integration and test automation but not trunk-based "
                  "development, so the ladder puts it at level 1. The lab's tile for what the level hides lists 3 capabilities it has that higher levels ask for: continuous integration, test automation and monitoring. Another 9, among them everything cultural, are on no level of the ladder at all. One missing item at level 2 hides a team that is strong in four categories and ahead on culture."),
            ("p", "The preset <code>two-teams</code> adds `Brook`, which has 8 of "
                  "the 24, every one of them in continuous delivery. Brook meets level 2 and misses level 3 on two items, so the ladder puts it above Atlas, though it has fewer capabilities and none in architecture, product and process, lean management or culture; the level hides one of Brook's, continuous delivery. The ladder "
                  "answers which team is higher and not what each should do next: "
                  "for Atlas it is one capability, trunk-based development, and "
                  "for Brook it is the other four categories. The capability that fewest teams have is the lab's last tile; with two teams it lists the 6 that neither has, from loosely coupled architecture to transformational leadership, so it is only a pointer."),
            ("p", "The preset <code>later</code> is `Atlas` in March and again in September, with three more: trunk-based development, shift left on security and a loosely coupled architecture. That is 17 of 24, and the lab lists the three it gained in its tile for the second date. Typed in as the team, the September list reaches level 2 on the ladder, missing only continuous delivery at level 3. The change in level is one step, the change in the profile is three capabilities in three categories, and neither is a measure of the outcomes the authors care about. The book would want those "
                  "measured too: the four delivery measures of the next lesson."),
            ("h3", "Exercise"),
            ("ul", [
                "A team, `Cove`, has these in place: `version control`, `deployment "
                "automation`, `continuous integration`, `test automation`, "
                "`trunk-based development`, `monitoring`.",
                "The ladder is the one above.",
            ]),
            ("p", "Count Cove's capabilities, find its level, and name the capabilities that would lift it to the next level. Then type the team into the lab to check your count and read the tile for what the level hides. Finally, say what you would want to know about Cove that the level cannot tell you."),
            ("p", "The next lesson, The Flaws in Previous Attempts to Measure "
                  "Performance, takes up the first section of Chapter 2: the "
                  "measures the authors set aside, and why."),
        ],
        "lab": ("acckit", {
            "mode": "capability",
            "view": "profile",
            "preset": "one-team",
            "presets": [
                {"id": "one-team",
                 "label": "Atlas against an invented three-level ladder",
                 "capabilities": CAPABILITIES,
                 "teams": _team("Atlas", ATLAS),
                 "levels": LADDER,
                 "expect": {
                            "acpOverall": "Atlas 14 of 24",
                            "acpCategories": "Atlas: continuous-delivery 4 of 8, architecture 1 of 2, product-and-process 2 of 4, lean-management-and-monitoring 3 of 5, cultural 4 of 5",
                            "acpLevel": "Atlas 1",
                            "acpHidden": "Atlas 3: continuous-integration, test-automation, monitoring",
                 }},
                {"id": "two-teams",
                 "label": "Atlas and Brook against the same ladder",
                 "capabilities": CAPABILITIES,
                 "teams": _team("Atlas", ATLAS) + "; " + _team("Brook", BROOK),
                 "levels": LADDER,
                 "expect": {
                            "acpOverall": "Atlas 14 of 24; Brook 8 of 24",
                            "acpLevel": "Atlas 1; Brook 2",
                            "acpHidden": "Atlas 3: continuous-integration, test-automation, monitoring; Brook 1: continuous-delivery",
                            "acpFewest": "0 of 2 teams: loosely-coupled-architecture, value-stream, team-experimentation, change-approval-processes, proactive-notification, transformational-leadership",
                 }},
                {"id": "later",
                 "label": "Atlas in March and in September",
                 "capabilities": CAPABILITIES,
                 "teams": _team("Atlas", ATLAS),
                 "teams2": _team("Atlas", ATLAS_LATER),
                 "levels": LADDER,
                 "expect": {
                            "acpOverall": "Atlas 14 of 24",
                            "acpAdded": "Atlas +3 (trunk-based-development, shift-left-on-security, loosely-coupled-architecture)",
                 }},
            ],
            "panel_title": "A team's capabilities, and the level they hide",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Reading a profile",
        "steps_intro": "Four steps, the last of them on a team you know.",
        "steps": [
            ("List what is in place",
             "Write down the capabilities the team has, one to a line, against the "
             "book's 24, and sort them by the five categories."),
            ("Count by category",
             "For each category write in place over total. A category with none in "
             "place is a place to look; it is not a score."),
            ("Set it beside a ladder, if you have one",
             "If your organization uses levels, find the level the team reaches and "
             "list the capabilities it has that the level does not ask about."),
            ("Do it for a team of your own",
             "Take your own team, and fill in the 24 honestly with one other person "
             "who works on it. Note where the two of you disagree: that is the "
             "executive-and-practitioner gap in small."),
        ],
        "worked": {
            "title": "Atlas against the ladder",
            "intro": [
                "Find `Atlas`'s level on <code>one-team</code>.",
            ],
            "lines": [
                "level 1: version control, deployment automation, both in place",
                "level 2: continuous integration yes, test automation yes",
                "level 2: trunk-based development no, so level 2 is not met",
                "the level: 1",
                "in place: 4 + 1 + 2 + 3 + 4 = 14 of 24",
                "level 1 asks for 2; higher levels ask for 3 more, the ones the level hides",
            ],
            "after": [
                "Each line asks one question and nothing more. The ladder reads the "
                "first miss and stops; the profile reads all 24.",
            ],
        },
        "quiz_title": "Capabilities, maturity and the book's evidence",
        "quiz": [
            {"q": "How many capabilities does the book say drive improvement in "
                  "software delivery performance, and how many categories does its "
                  "Quick Reference sort them into?",
             "a": ["24 capabilities in five categories",
                   "12 capabilities in five categories",
                   "24 capabilities in 12 categories",
                   "5 capabilities in 24 categories"],
             "c": 0,
             "why": "The Quick Reference and Chapter 1 give 24 key capabilities, "
                    "classified into continuous delivery, architecture, product and "
                    "process, lean management and monitoring, and cultural "
                    "capabilities. The other options reverse or change one of the "
                    "two numbers."},
            {"q": "Chapter 1 lists factors often cited as drivers of performance "
                  "that the research did not find to predict it. Which of these is "
                  "one of them?",
             "a": ["Whether operations or development staff performed deployments",
                   "Whether the team practices trunk-based development",
                   "Whether the organization has a Westrum generative culture",
                   "Whether the team keeps its work in version control"],
             "c": 0,
             "why": "The chapter names three: the age and technology of the "
                    "application, who performed deployments, and whether a change "
                    "approval board was in place. The other three options are "
                    "capabilities in the book's list of 24, which the book reports "
                    "as drivers."},
            {"q": "In the exercise, `Cove` has version control, deployment "
                  "automation, continuous integration, test automation, "
                  "trunk-based development and monitoring. On the lesson's ladder, "
                  "what level does it reach, and what does the lab list as hidden "
                  "by that level?",
             "a": ["Level 2, hiding monitoring",
                   "Level 3, because it has monitoring",
                   "Level 1, hiding continuous integration and test automation",
                   "Level 2, hiding nothing, since it has no other capability"],
             "c": 0,
             "why": "Cove meets level 1 and level 2, which asks for continuous "
                    "integration, test automation and trunk-based development. "
                    "Level 3 also needs continuous delivery and a loosely coupled "
                    "architecture, which it lacks, so the level is 2. Monitoring is "
                    "a level 3 requirement that Cove has, so the level hides it. "
                    "To reach level 3 it needs the two it lacks."},
            {"q": "In 2017, comparing high performers with low performers, how many "
                  "times more frequent were code deployments, according to Chapter 1?",
             "a": ["46 times",
                   "440 times",
                   "170 times",
                   "5 times"],
             "c": 0,
             "why": "The chapter's four comparisons are 46 for deployments, 440 for lead time, 170 for recovery and a fifth for the failure rate. Each of the other options is one of the other three."},
        ],
        "mistakes": [
            ("Thinking a level says where a team is",
             "A level is where the first unmet requirement is. On the lesson's "
             "sample, one missing item put a team with 14 of 24 capabilities below "
             "one with 8. The authors' point is that a single level hides what the "
             "team can do and what it should do next; a profile by category shows "
             "both, and a profile by outcome is what the later chapters add."),
            ("Reading the 24 as a checklist to tick in order",
             "The Quick Reference gives the 24 in no ranking, and the authors' second reason against maturity "
             "models is that teams differ in their context, systems and goals. "
             "Which capability to improve next depends on which outcome the team "
             "wants to move."),
            ("Reading a survey finding as a promise about your team",
             "The authors report predictions from many teams' answers, in 2014 to "
             "2017, and Fowler's foreword notes that surveys capture perceptions, "
             "that the sample may not mirror the industry and that confirmation "
             "would help. A finding says what tended to go together across "
             "thousands of responses; it does not say what will happen in a team "
             "that adopts a capability."),
        ],
        "standard": (
            "Finish when you can say what a single level hides.",
            "Given a team's capabilities and a stated ladder, count the capabilities in place by category, find the level the ladder gives, and name the ones in place that higher levels ask for."
        ),
        "note": (
            "The lab counts the capabilities you say a team has and compares them "
            "with a ladder you give it. It cannot tell whether a capability is "
            "really in place, how well, or whether it moves any outcome; the book's "
            "evidence for that is its survey's, and the lab's team and ladder are "
            "invented."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 2 opening and The Flaws in Previous Attempts to Measure
    # Performance (PDF pp. 44-47 of the operator's copy): outputs and local
    # measures (p. 45), lines of code (p. 45), velocity (pp. 45-46),
    # utilization (pp. 46-47).
    # Quote: PDF p. 46 of the operator's copy, 9 words, quotes.py OK.
    # Lesson total: 9 words.
    {
        "slug": "the-flaws-in-previous-measures",
        "title": "The Flaws in Previous Attempts to Measure Performance",
        "module": "Chapter 2 · Measuring Performance",
        "one_line": "Lines of code, velocity and utilization each measure an output or a local quantity, and the third has a rule that shows why: a wait grows without limit as slack runs out.",
        "summary": (
            "Chapter 2 begins by clearing the ground. The authors name two flaws in "
            "earlier measures of software productivity, outputs rather than "
            "outcomes and local rather than global measures, and test three "
            "examples against them. Read the case against lines of code and "
            "velocity, then compute the one that has arithmetic behind it: what a "
            "task's lead time does as the people doing it are kept busier."
        ),
        "key": [
            "output is not outcome",
            "a local measure can hurt the whole",
            "lines of code reward bloat",
            "velocity is relative and gameable",
            "lead = service time ÷ (1 − utilization)",
            "at 100 percent, no finite wait",
        ],
        "key_label": "The flaws in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the second "
            "the lab's, the third both."
        ),
        "concepts": [
            ("Output and outcome",
             "An output is what a team produces, lines of code or stories finished; "
             "an outcome is what the output achieves for the organization. The "
             "authors' first complaint is that earlier measures count the first "
             "and miss the second."),
            ("Utilization",
             "The share of its time that a person or team is busy. The lab gives "
             "it as a percentage from 0 to 99, and it is the one lever on this "
             "page that a manager can pull in the wrong direction."),
            ("Lead time and service time",
             "Lead time is how long a task takes from request to completion; "
             "service time is the hands-on part of it. The difference is the "
             "wait, and the lab computes it from utilization in the simplest "
             "queueing model."),
        ],
        "read_title": "Three measures, and why each fails",
        "read_intro": (
            "Read the opening of Chapter 2 and its first section, The Flaws in "
            "Previous Attempts to Measure Performance, in your own copy first. The "
            "lesson goes through the three examples in the authors' order, then "
            "computes the third."
        ),
        "body": [
            ("p", "Chapter 2 opens with a difficulty. Measuring performance in "
                  "software is hard, the authors say, because the inventory is "
                  "invisible, because the way work is broken down is relatively "
                  "arbitrary, and because design and delivery happen at the same "
                  "time. Their first section, The Flaws in Previous Attempts to "
                  "Measure Performance, names two drawbacks of the usual measures of "
                  "productivity. They focus on outputs rather than outcomes, and on what one person or one function does, rather than on what a team or the whole delivers. "
                  "Three examples follow: lines of code, velocity and utilization."),
            ("p", "Lines of code come first, and the argument is short. A company "
                  "that rewards developers for lines written gets more lines, and "
                  "the authors say it gets bloated software with higher maintenance "
                  "and change costs. They would rather have ten lines than a "
                  "thousand for the same problem, and a business process change that "
                  "removes the need for code is better still. They do not conclude "
                  "that fewer is always better: a task done in one line that nobody "
                  "else can read is worse than a few lines everybody can. A count of "
                  "lines is a count of output, and no direction of it is the goal."),
            ("p", "Velocity is the Agile way to measure the same thing. Teams "
                  "estimate stories in points, and the points signed off at the end "
                  "of an iteration are the team's velocity, which was designed to "
                  "plan capacity, to extrapolate how long the planned work will "
                  "take. The authors object when managers use it to compare teams "
                  "or to measure productivity. It is relative and team-dependent, "
                  "since teams' contexts differ, so one team's points cannot be "
                  "set against another's. And when it is a target, teams game it, "
                  "inflating estimates and pushing stories through while collaboration suffers, which spoils its use as a "
                  "planning tool and discourages teams from helping one another."),
            ("p", "Utilization is the third. Many organizations treat how busy "
                  "people are as a stand-in for productivity. The authors say that "
                  "&ldquo;high utilization is only good up to a point&rdquo;: past "
                  "it, no spare capacity, or slack, remains to absorb unplanned "
                  "work, changes of plan or improvement work, and lead times "
                  "lengthen. They cite queue theory, in which lead times approach "
                  "infinity as utilization approaches 100 percent, and say that getting anything done then takes teams far longer, in their word exponentially. Lead time is the productivity measure that avoids the faults of the other two, and the authors conclude that utilization has to be managed against it."),
            ("p", "The rule behind that sentence is a few lines of arithmetic, and "
                  "the lab does it. In the simplest queueing model, one worker "
                  "taking tasks one at a time, with tasks arriving at random, a "
                  "task waits on average `u/(1 − u)` times its service time for "
                  "its turn, where `u` is the utilization as a fraction. Its lead "
                  "time is the wait plus the service, which is the service time "
                  "divided by `1 − u`. Two cautions. The model is a simplification "
                  "of any real team, which has several people, tasks of mixed "
                  "sizes and arrivals that are not random. And in this model the "
                  "growth is a hyperbola, steeper and steeper near 100 percent, "
                  "which is not strictly the exponential of the book's wording; "
                  "the book's point, that the wait has no limit, holds. The "
                  "System Design path teaches the model in its lesson The Knee: "
                  "Response Time vs Utilisation, in Queues and Utilisation, and "
                  "this lesson does not repeat it."),
            ("p", "The preset <code>ladder</code> takes a review that needs two "
                  "hours of hands-on work, at 50, 80, 90, 95 and 99 percent "
                  "utilization. The waits are 1, 4, 9, 19 and 99 times the service "
                  "time, so the lead times are 4, 10, 20, 40 and 200 hours. Going "
                  "from 50 to 80 percent busy multiplies the lead time by two and "
                  "a half; going from 90 to 99 multiplies it by ten. The same "
                  "person, doing the same review, is the same speed at every row; "
                  "all that changes is how often a review arrives while another is "
                  "being done."),
            ("p", "The preset <code>headroom</code> asks the manager's question. "
                  "A task takes 3 hours of hands-on work, and the team is at 90 "
                  "percent. The lead time is 30 hours. Take ten points of "
                  "utilization off, to 80 percent, and it is 15 hours: half. "
                  "Nothing was sped up, and the people are no less capable; some of "
                  "the time was set aside so that work does not queue. That is the trade the authors ask managers to make, weighing utilization against lead time, and "
                  "the lab leaves the economics, what the idle time costs, to you."),
            ("p", "Read the figures as a reason to look, not as a forecast. Lead "
                  "time is where this model sends you, but the model sees one "
                  "queue and a team has many. The lab refuses 100 percent, since "
                  "the formula divides by zero there; that refusal is the book's "
                  "claim as arithmetic, and no team's true utilization is known to "
                  "the point where the model matters. What the lesson can say "
                  "is the direction: the nearer a team runs to full, the more a "
                  "small rise in demand costs."),
            ("h3", "Exercise"),
            ("ul", [
                "A task takes 6 hours of hands-on work.",
                "The team's utilization is 75 percent.",
            ]),
            ("p", "Find the wait in service times, then the lead time in hours. "
                  "Then find the utilization at which the lead time is ten times "
                  "the service time, and check both in the lab. Try 100 percent "
                  "and read what the lab says."),
            ("p", "The next lesson, Measuring Software Delivery Performance, "
                  "turns to what the authors measure instead: four measures of "
                  "delivery, each of which is a team-level outcome."),
        ],
        "lab": ("acckit", {
            "mode": "flow",
            "view": "utilization",
            "preset": "ladder",
            "presets": [
                {"id": "ladder",
                 "label": "A two-hour review at five levels of utilization",
                 "levels": UTIL_LADDER,
                 "service": "2",
                 "expect": {
                            "aflMultiples": "50%: 1; 80%: 4; 90%: 9; 95%: 19; 99%: 99",
                            "aflLeads": "50%: 4 hours; 80%: 10 hours; 90%: 20 hours; 95%: 40 hours; 99%: 200 hours",
                            "aflRatio": "50× (50% to 99%)",
                 }},
                {"id": "headroom",
                 "label": "A three-hour task at 90 and at 80 percent",
                 "levels": "90, 80",
                 "service": "3",
                 "expect": {
                            "aflLeads": "90%: 30 hours; 80%: 15 hours",
                            "aflRatio": "2× (80% to 90%)",
                 }},
            ],
            "panel_title": "How the wait grows as slack runs out",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Testing a measure",
        "steps_intro": "Four steps, the last of them on a measure in use near you.",
        "steps": [
            ("Ask what it counts",
             "Say whether the measure counts something produced (an output) or "
             "something achieved (an outcome)."),
            ("Ask who it can be compared across",
             "Say whether the figure means the same thing across teams, and whether "
             "improving it for one team can make another's worse."),
            ("Ask what happens when it is a target",
             "Imagine rewarding it. Write down one cheap way to raise it that helps "
             "nobody."),
            ("Do it on a measure of your own",
             "Take a measure your organization reports about teams. Answer the "
             "three questions and, if it is a utilization, type its value into "
             "the lab with a typical task's service time."),
        ],
        "worked": {
            "title": "A two-hour review at 80 percent",
            "intro": [
                "Find the lead time on <code>ladder</code> at 80 percent.",
            ],
            "lines": [
                "u = 80 percent = 4/5",
                "1 − u = 1/5",
                "wait = u/(1 − u) = (4/5)/(1/5) = 4 service times",
                "lead time = 2 hours × (1 + 4) = 10 hours",
                "check: 2 hours ÷ (1/5) = 10 hours",
            ],
            "after": [
                "The two ways of getting the lead time are the same line of "
                "algebra. At 99 percent the wait is 99 service times and the lead "
                "time 200 hours.",
            ],
        },
        "quiz_title": "Output, velocity and the utilization model",
        "quiz": [
            {"q": "In the exercise, a task takes 6 hours of hands-on work and the "
                  "team is 75 percent utilized. In the lab's model, what is the "
                  "task's lead time, counting the wait and the work?",
             "a": ["24 hours",
                   "18 hours",
                   "8 hours",
                   "4.5 hours"],
             "c": 0,
             "why": "At 75 percent the wait is u/(1 − u) = 3 service times, 18 "
                    "hours, and the lead time adds the 6 hours of work: 24 hours, "
                    "or 6 hours divided by 1/4. The 18 is the wait alone; 8 hours "
                    "divides by u where the model divides by 1 − u; and 4.5 hours "
                    "multiplies by it."},
            {"q": "Which of the three measures does Chapter 2 criticise as "
                  "relative and team-dependent, so that teams' figures cannot be "
                  "compared?",
             "a": ["Velocity",
                   "Lines of code",
                   "Utilization",
                   "Lead time"],
             "c": 0,
             "why": "Velocity is the points a team signs off, and the points are the "
                    "team's own estimates in its own context. Lines of code are "
                    "criticised for rewarding bloat, utilization for leaving no "
                    "slack, and lead time is the measure the authors favour."},
            {"q": "In the lab's model, at what utilization is the lead time ten "
                  "times the service time?",
             "a": ["90 percent",
                   "99 percent",
                   "80 percent",
                   "50 percent"],
             "c": 0,
             "why": "The lead time is the service time divided by 1 − u, so ten "
                    "times it needs 1 − u = 1/10, which is u = 90 percent. At 99 "
                    "percent it is 100 times, at 80 percent 5 times and at 50 "
                    "percent twice."},
            {"q": "According to the section, what does queue theory say happens to "
                  "lead times as utilization approaches 100 percent?",
             "a": ["They approach infinity",
                   "They fall, because nobody is idle",
                   "They stay level until 100 percent and then jump",
                   "They double, whatever the starting level"],
             "c": 0,
             "why": "The authors say that lead times approach infinity, so that "
                    "teams take far longer to get anything done. The lab's "
                    "arithmetic agrees: the wait is u/(1 − u) service times, "
                    "unbounded as u goes to 1, and it is not level before that."},
        ],
        "mistakes": [
            ("Thinking a busier team is a more productive one",
             "The authors' point is that high utilization is good only up to a "
             "point. On the lesson's sample, the same two-hour review takes 4 hours "
             "of lead time at 50 percent and 20 at 90. The people are no slower; "
             "the work waits."),
            ("Using velocity to compare teams",
             "Velocity was built to plan one team's capacity, and the authors say "
             "teams' points are not commensurable and, used as a target, get "
             "inflated. A change in the points a team signs off tells you little "
             "about the value delivered."),
            ("Concluding that less code is always better",
             "The authors say the same of minimising lines as of rewarding them: "
             "the aim is to solve the business problem with the least code that "
             "people can read and keep up, and the best saving is code that never "
             "has to be written. Neither more nor fewer lines is the measure."),
        ],
        "standard": (
            "Finish when you can compute what a rise in utilization costs.",
            "Given a task's service time and a utilization, work out the wait in "
            "service times and the lead time, and say why the model has no answer "
            "at 100 percent."
        ),
        "note": (
            "The lab uses the simplest queueing model, one server and random "
            "arrivals. A real team has several people, tasks of mixed sizes and "
            "demand that is not random, and the lab cannot say how close any team "
            "is to the model; it shows the direction and the steepness, not your "
            "lead time."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Measuring Software Delivery Performance (PDF pp. 47-51 of the operator's
    # copy): the two criteria (p. 47), lead time and its two parts (pp. 47-49),
    # deployment frequency and batch size (pp. 49-50), time to restore and
    # change fail rate (pp. 50-51), cluster analysis introduced (p. 51).
    # Quote: PDF p. 47 of the operator's copy, 15 words, quotes.py OK.
    # Answer options: the six lead-time options (p. 49) and the six deployment
    # frequency options (p. 50) are facts.
    # Lesson total: 15 words.
    {
        "slug": "the-four-measures",
        "title": "Measuring Software Delivery Performance",
        "module": "Chapter 2 · Measuring Performance",
        "one_line": "Lead time, deployment frequency, time to restore service and change fail rate: four team-level outcomes, each recorded as a choice among a few answers.",
        "summary": (
            "The authors want a measure that rewards a global outcome and not "
            "output, and they settle on four. Read why lead time is split in two "
            "and only the delivery half measured, why deployment frequency "
            "stands for batch size, and why restoring service replaced time "
            "between failures; then compute all four from a two-week log."
        ),
        "key": [
            "a global outcome, not output",
            "lead time: commit to running in production",
            "deployment frequency stands for batch size",
            "tempo: lead time, deployment frequency",
            "stability: time to restore, change fail rate",
            "each is a survey answer, picked from options",
        ],
        "key_label": "The four measures in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, all the chapter's."
        ),
        "concepts": [
            ("Lead time for changes",
             "The time from code committed to that code running successfully in "
             "production. The authors split a feature's whole lead time into a "
             "design part, hard to time and highly variable, and this delivery "
             "part, which is easier to measure and steadier."),
            ("Deployment frequency",
             "How often the primary service is deployed to production or to an app "
             "store. The authors use it as a proxy for batch size, since a smaller "
             "batch is deployed more often and the batch itself is hard to see."),
            ("Tempo and stability",
             "The two pairs the four measures fall into. Lead time and "
             "deployment frequency are tempo; time to restore service and change "
             "fail rate are stability. The authors test whether improving the "
             "first costs the second."),
        ],
        "read_title": "Four measures, chosen against two criteria",
        "read_intro": (
            "Read the section Measuring Software Delivery Performance in your own "
            "copy first, up to the introduction of cluster analysis. The lesson "
            "follows its order, then computes the four measures from a log."
        ),
        "body": [
            ("p", "The authors give their measure two criteria. It should be a "
                  "global outcome, because, in their words, &ldquo;it should focus "
                  "on a global outcome to ensure teams aren’t pitted against each "
                  "other&rdquo;, and their example is paying developers for "
                  "throughput and operations for stability, which builds the wall of "
                  "confusion between them. And it should be an outcome and not "
                  "output, so that it cannot be raised with busywork. They settle "
                  "on four measures: delivery lead time, deployment frequency, time "
                  "to restore service and change fail rate."),
            ("p", "Lead time is the Lean measure of how long it takes to go from a "
                  "customer's request to its satisfaction. In product development "
                  "it has two parts. Designing and validating a feature is "
                  "uncertain, it is hard to say when the clock starts, and the "
                  "variance is high, which Reinertsen, whom the authors cite, calls "
                  "the fuzzy front end. Delivering it, from implementation through "
                  "test to release, is easier to measure and steadier. The authors "
                  "measure only the second: the time from code committed to code "
                  "running in production. Their survey offered six answers: less "
                  "than one hour; less than one day; between one day and one week; "
                  "between one week and one month; between one month and six "
                  "months; more than six months."),
            ("p", "Batch size is the second measure&rsquo;s subject, and the "
                  "difficulty is that in software there is no visible inventory. "
                  "Reducing batches shortens cycle times, speeds feedback and cuts "
                  "risk, in the Lean tradition the authors cite from Toyota, so they "
                  "needed a stand-in that respondents can report: deployment "
                  "frequency, to production or an app store. The six answers were "
                  "on demand, meaning several deploys a day; between once an hour "
                  "and once a day; between once a day and once a week; between once "
                  "a week and once a month; between once a month and once every six "
                  "months; and fewer than once every six months. A release usually "
                  "contains several commits, unless each commit goes out alone."),
            ("p", "Lead time and deployment frequency are the tempo of delivery. "
                  "To see whether teams that speed up give up stability, the authors "
                  "add two measures. Traditionally reliability is the time between "
                  "failures, but in complex, quickly changing systems failure is "
                  "inevitable, so the question becomes how quickly service is "
                  "restored after an incident, answered from the same six options as "
                  "lead time. And the change fail rate: the percentage of changes to "
                  "production, including releases and configuration changes, that "
                  "lead to degraded service or need a hotfix, a rollback, a fix "
                  "forward or a patch. In Lean terms, they note, it is the percent "
                  "complete and accurate of the delivery process."),
            ("p", "Notice what kind of data these are. In the book, each measure is "
                  "a respondent's answer to a question about their primary "
                  "application or service, an option from a short list, which is "
                  "why Fowler's foreword says they capture perceptions. The lab "
                  "does something the survey did not: it computes the four from a "
                  "log of changes and incidents, and then reads each on the book's "
                  "scale, so that you can see which answer a team would give."),
            ("p", "The preset <code>fortnight</code> is a team&rsquo;s log over 14 "
                  "days: ten changes, each with the time it was committed and the "
                  "time it reached production, one of them failed, and two "
                  "incidents. The lab reports the ten deployments, 5 a week, which "
                  "is between once a day and once a week; a median lead time of 4.5 "
                  "hours, less than one day; a change fail rate of 1 in 10, 10 "
                  "percent, in the 0 to 15 percent band; and a median time to "
                  "restore of 7.5 hours, from restorations of 3 and 12 hours, less "
                  "than one day. The longest lead times are 26 and 20 hours, over "
                  "a weekend and an overnight wait, and the median hides them."),
            ("p", "The preset <code>batched</code> is a different team over 28 "
                  "days that gathers its changes and ships them together: seven "
                  "changes in three deployments, committed on days 2 to 26 and released on days 10, 19 and 28. Median lead time is 140 hours, "
                  "between one day and one week, because a change waits for the "
                  "next release. Two of the seven failed, 28.6 percent, in the 16 "
                  "to 30 percent band, and the two incidents took 48 and 24 hours "
                  "to restore, a median of 36 hours, between one day and one week. "
                  "The sample is written so that the long wait, the failures and "
                  "the slow recovery fall on the same team; a real log would not "
                  "have to, and the next lesson is about whether they do."),
            ("p", "What the lab cannot do is decide where your clock starts. The "
                  "authors choose commit to production because it can be timed, "
                  "and Fowler remarks that the book covers delivery and not the "
                  "entire development process; a team that merges once a day and "
                  "waits for review for three days has lead time that begins "
                  "earlier than the log shows. Which events a team records as "
                  "commit, deploy, failure and restoration is the "
                  "measurement, and the figures are only as good as that choice."),
            ("h3", "Exercise"),
            ("p", "A third team&rsquo;s week, a period of 7 days: four changes, w1 committed at 10:00 on day 1 and deployed at 12:00; w2 committed at 09:00 on day 2 and deployed at 15:00, and failed; w3 committed at 11:00 on day 3 and deployed at 13:00; w4 committed at 14:00 on day 5 and deployed at 15:00. One incident began at 15:30 on day 2 and ended at 18:30 the same day."),
            ("p", "Work out the lead time of each change, the median, the change "
                  "fail rate and the time to restore, and say which of the book&rsquo;s "
                  "answers each falls under. Then type the log into the lab to "
                  "check it."),
            ("p", "The next lesson, High, Medium and Low Performers, takes "
                  "the next step in the chapter: grouping teams by these four "
                  "answers, without a prior idea of which are good."),
        ],
        "lab": ("acckit", {
            "mode": "delivery",
            "view": "metrics",
            "preset": "fortnight",
            "presets": [
                {"id": "fortnight",
                 "label": "A team that ships small changes, over 14 days",
                 "days": "14",
                 "changes": FORTNIGHT_CHANGES,
                 "incidents": FORTNIGHT_INCIDENTS,
                 "expect": {
                            "adeDeploys": "10",
                            "adePerWeek": "5",
                            "adeFreq": "between once per day and once per week",
                            "adeLead": "4 h 30 min",
                            "adeLeadOpt": "less than one day",
                            "adeFail": "1/10 = 10%",
                            "adeFailBand": "0–15%",
                            "adeRestore": "7 h 30 min",
                            "adeRestoreOpt": "less than one day",
                 }},
                {"id": "batched",
                 "label": "A team that gathers changes into releases, over 28 days",
                 "days": "28",
                 "changes": BATCHED_CHANGES,
                 "incidents": BATCHED_INCIDENTS,
                 "expect": {
                            "adeDeploys": "3",
                            "adeChanges": "7 of 7",
                            "adeFreq": "between once per week and once per month",
                            "adeLead": "5 d 20 h",
                            "adeLeadOpt": "between one day and one week",
                            "adeFail": "2/7 ≈ 28.6%",
                            "adeFailBand": "16–30%",
                            "adeRestore": "1 d 12 h",
                            "adeRestoreOpt": "between one day and one week",
                 }},
            ],
            "panel_title": "Four delivery measures from a log",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Measuring delivery from a log",
        "steps_intro": "Four steps, the last of them on a service of your own.",
        "steps": [
            ("Fix the events",
             "Decide which timestamps mean committed, deployed to production, failed "
             "and restored, and write the decision down."),
            ("Compute the four",
             "For one period, count the deployments, take the median commit-to-deploy "
             "time, the share of deployments that failed, and the median time to "
             "restore."),
            ("Read each on the book's scale",
             "Find the answer each figure falls under, and note which of the four "
             "is tempo and which is stability."),
            ("Do it on a service of your own",
             "Take a fortnight from your own history, type it into the lab, and "
             "look first at the longest lead time and the slowest restoration, "
             "which the medians hide."),
        ],
        "worked": {
            "title": "Four measures from a fortnight",
            "intro": [
                "Compute the measures for <code>fortnight</code> by hand.",
            ],
            "lines": [
                "lead times in hours: 6, 4, 26, 3, 8, 2, 20, 4, 5, 3",
                "sorted: 2, 3, 3, 4, 4, 5, 6, 8, 20, 26",
                "median: (4 + 5) / 2 = 4.5 hours, less than one day",
                "deployments: 10 in 14 days = 5 a week",
                "change fail rate: 1 / 10 = 10 percent, band 0 to 15",
                "restore: 12 and 3 hours, median 7.5, less than one day",
            ],
            "after": [
                "The median of an even count is the mean of the middle two. The "
                "mean lead time would be 8.1 hours, because of the two long waits; "
                "the median is the figure the lab reads on the scale.",
            ],
        },
        "quiz_title": "The four measures, and what they are for",
        "quiz": [
            {"q": "On the preset <code>fortnight</code>, the median lead time is "
                  "4.5 hours. Which of the book&rsquo;s lead-time answers does that "
                  "fall under?",
             "a": ["Less than one day",
                   "Less than one hour",
                   "Between one day and one week",
                   "Between one week and one month"],
             "c": 0,
             "why": "4.5 hours is more than an hour and less than a day. The "
                    "median is used because the sorted lead times run from 2 to 26 "
                    "hours; the mean, 8.1 hours, falls under the same answer."},
            {"q": "Why do the authors use deployment frequency in their measure of "
                  "delivery performance?",
             "a": ["As a proxy for batch size, which is hard to see in software",
                   "As a measure of how busy developers are",
                   "As a measure of the number of features delivered",
                   "As a measure of customers' demand for new releases"],
             "c": 0,
             "why": "The authors say batch size is a central Lean idea but hard to "
                    "measure where there is no visible inventory, so they take "
                    "deployment frequency, which is easy to report and typically "
                    "steady, as its stand-in. It is not a count of effort or of "
                    "features, and it is not demand."},
            {"q": "Which two of the four measures does the chapter treat as the "
                  "stability measures?",
             "a": ["Time to restore service and change fail rate",
                   "Lead time and change fail rate",
                   "Deployment frequency and time to restore service",
                   "Lead time and deployment frequency"],
             "c": 0,
             "why": "Lead time and deployment frequency are the tempo of delivery; "
                    "time to restore service and change fail rate are about the "
                    "stability of the systems a team works on. The question the "
                    "chapter goes on to ask is whether tempo is bought with "
                    "stability."},
            {"q": "In the exercise week, the lead times are 2, 6, 2 and 1 hours and "
                  "one of the four changes failed. What are the median lead time and "
                  "the change fail rate's band?",
             "a": ["2 hours, and 25 percent, in the 16 to 30 percent band",
                   "2.75 hours, and 25 percent, in the 16 to 30 percent band",
                   "2 hours, and 25 percent, in the 31 to 45 percent band",
                   "2 hours, and 4 percent, in the 0 to 15 percent band"],
             "c": 0,
             "why": "Sorted, the lead times are 1, 2, 2 and 6, and the median of an "
                    "even count is the mean of the middle two: 2 hours. The mean, "
                    "2.75 hours, is a different figure. One failure in four is 25 "
                    "percent, above 15 and not above 30. The incident took 3 hours "
                    "to restore, under one day."},
        ],
        "mistakes": [
            ("Measuring developers on throughput and operations on stability",
             "The authors give this as the classic example of a measure that is not "
             "global: each side is rewarded for what it controls, and the wall of "
             "confusion between them follows. Their four measures are for the "
             "delivery as a whole, which no function achieves alone."),
            ("Taking lead time to start with the customer's request",
             "The book splits lead time and measures only the delivery part, from "
             "commit to production, because the design part has no clear start and "
             "is highly variable. Fowler's foreword says plainly that the book "
             "covers IT delivery, not the whole development process."),
            ("Trusting a median to describe every change",
             "On the lesson's fortnight the median is 4.5 hours, and two changes "
             "took 20 and 26. The book asks respondents for a typical answer; a "
             "log can show the spread, and the long waits are where to look."),
        ],
        "standard": (
            "Finish when you can compute the four measures from a log.",
            "Given a period's changes and incidents, compute the lead time, "
            "deployment frequency, change fail rate and time to restore, and say "
            "which of the book's answers each falls under."
        ),
        "note": (
            "The lab computes the measures from the log you type, with the events "
            "you say are commits, deployments, failures and restorations. The book's "
            "own figures were survey answers, from other respondents, in 2014 to "
            "2017; a log of one team is not a sample of them."
        ),
    },
    # ---------------------------------------------------------------- 04
    # High, Medium and Low Performers (PDF pp. 51-57 of the operator's copy):
    # cluster analysis (p. 51), the categories found each year (p. 52),
    # Tables 2.2 and 2.3 (pp. 52-53, described in prose only), no trade-off
    # (p. 53), the trends (pp. 53-54), the 2016 surprise (p. 57). Method:
    # Appendix C, Tests for Classification (p. 272); What Is Clustering? (p. 181).
    # Quote: PDF p. 53 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "high-medium-and-low-performers",
        "title": "High, Medium and Low Performers",
        "module": "Chapter 2 · Measuring Performance",
        "one_line": "Cluster analysis groups teams by their four answers with no notion of good or bad, and finds that the groups differ on all four at once.",
        "summary": (
            "How do the authors get from four measures to high, medium and low "
            "performers? By a method that does not know which answers are good. "
            "Read what cluster analysis is, which variant they chose and why, what "
            "the groups look like in words, and the 2016 result that did not fit; "
            "then cluster ten invented teams with Ward's method and read the "
            "groups' medians."
        ),
        "key": [
            "cluster analysis cannot tell good from bad",
            "Ward's method: merge the cheapest pair",
            "a fusion coefficient is the cost of a merge",
            "high performers do better on all four",
            "no tradeoff between tempo and stability",
            "groups are drawn afresh from each year",
        ],
        "key_label": "High, medium and low in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the other "
            "two are Appendix C's and the lab's."
        ),
        "concepts": [
            ("Cluster analysis",
             "A way of grouping responses so that those in a group are more like "
             "one another than like those in other groups. Each measure is a "
             "dimension, and the method sees only the distances between "
             "responses, never whether an answer is a good one."),
            ("Ward's method",
             "A hierarchical clustering: start with every team alone and merge, "
             "step by step, the two groups whose merger adds least to the spread "
             "within the groups. The authors compared it with four other methods "
             "and report that it performed best."),
            ("Fusion coefficient",
             "The cost of one merge: how much the within-group sum of squares "
             "grows when two groups join. Small early on, large when unlike "
             "groups are forced together; a jump is where to consider stopping."),
        ],
        "read_title": "Groups that the data draw, and what the authors found",
        "read_intro": (
            "Read the rest of Chapter 2 up to its Surprise! box in your own copy "
            "first, and the paragraph on cluster analysis in Appendix C, under "
            "Tests for Classification. The lesson describes the book's two tables "
            "in a few sentences and does not reproduce them."
        ),
        "body": [
            ("p", "Having chosen four measures, the authors needed a way to say who "
                  "performs well on them. They use cluster analysis, which they "
                  "describe as attempting to group responses so that those in a "
                  "group are more alike than those in different groups. Each "
                  "measurement is put on its own dimension, and the algorithm tries "
                  "to keep members of a cluster close and the clusters apart. The "
                  "feature they stress is that the technique has no understanding of "
                  "the meaning of the answers; it does not know what counts as a "
                  "good or a bad response on any measure. That, they say, lets them "
                  "see trends in the industry without deciding in advance what "
                  "good looks like."),
            ("p", "Appendix C gives the method. They tried five hierarchical "
                  "methods, Ward's among them, and compared the solutions by the "
                  "change in fusion coefficients, by the number in each cluster "
                  "(solutions with tiny clusters were set aside) and by univariate "
                  "F-statistics; Ward's gave the best solution. They chose a "
                  "hierarchical method because it shows how clusters join, because "
                  "they had no theory about how many groups to expect and wanted "
                  "the data to say, and because the dataset was not too large for "
                  "it. Chapter 12 has a short box, What Is Clustering?, on the same choice, and the chapter&rsquo;s own footnote sends the reader on to an appendix."),
            ("p", "The result, which the authors report for each of the four years: "
                  "there were significantly different categories of delivery "
                  "performance, all four measures were good classifiers, and the "
                  "high, medium and low groups differed significantly on every one. "
                  "In their account of the 2017 data, high performers deploy on "
                  "demand, have lead times and times to restore under an hour and "
                  "change fail rates of 0 to 15 percent, while the low performers "
                  "deploy between once a week and once a month and take between a "
                  "day and a week to restore, with change fail rates of 31 to 45 "
                  "percent. The book flags that the low and medium groups shared a "
                  "median on two measures, deployment frequency and lead time, and "
                  "that the low group was worse on average at a statistically "
                  "significant level. The tables are the book&rsquo;s; the "
                  "lesson&rsquo;s sample is not drawn from them."),
            ("p", "Then the authors&rsquo; headline: &ldquo;Astonishingly, these "
                  "results demonstrate that there is no tradeoff between improving "
                  "performance and achieving higher levels of stability and "
                  "quality&rdquo;. The better groups are better on tempo and on "
                  "stability together, which is what Agile and Lean predict, and "
                  "which they set against the view that moving faster means giving "
                  "up something else. Fowler&rsquo;s foreword states it as speed "
                  "depending on stability. Note what it says and no more: in their "
                  "survey, the groups that are quick are also the groups that "
                  "recover quickly and fail less. It is a description of the "
                  "groups, and the authors take up why in later chapters."),
            ("p", "They also report the trend. High performers in 2017 maintained "
                  "or improved on 2016. Low performers kept the same throughput "
                  "from 2014 to 2016 and began to speed up in 2017, but lost "
                  "ground on stability, which the authors suspect is the result "
                  "of pushing harder without tackling what is in the way: "
                  "rearchitecture, process improvement, automation. So the "
                  "groups are not fixed targets. What counted as strong "
                  "three years earlier, they write, is not good enough now, and "
                  "the clusters are redrawn from each year&rsquo;s data."),
            ("p", "One box in the chapter, headed Surprise!, is the honest part. "
                  "In 2016 the medium performers did worse than the low performers "
                  "on change fail rate, the first year of any inconsistency across "
                  "the measures. The research does not explain it conclusively. "
                  "The authors suggest that medium performers were in the middle of "
                  "large rearchitecture work, and recall that in the same year "
                  "they spent more time on unplanned rework than the low group, "
                  "because they spent more on new work, perhaps at the expense of "
                  "rework and so with technical debt and more fragile systems. "
                  "It is offered as a possible reason, and the lesson does not "
                  "claim more for it."),
            ("p", "Now the method, by hand and in the lab. Take each team as a "
                  "point whose coordinates are its four answers, coded 1 for the "
                  "best option to 6. Start with every team on its own. At each "
                  "step, merge the two groups for which the merger raises the "
                  "within-group sum of squares least: for groups of sizes `a` and "
                  "`b` that is `a·b/(a + b)` times the squared distance between "
                  "their centres, and for two single teams it is half their squared "
                  "distance. That increase is the fusion coefficient. Ties are "
                  "broken in favour of the earlier team in the list. The lab "
                  "prints the merges in order, the groups at the number you ask "
                  "for, and each group&rsquo;s median on each measure in the "
                  "book&rsquo;s own words."),
            ("p", "The preset <code>ten-teams</code> is ten invented teams, coded "
                  "on deployment frequency, lead time, time to restore and change "
                  "fail rate, with three groups asked for. The nine merges cost 1/2, "
                  "5/6, 1, 3/2, 5/3, 5/3, 23/6, 25/2 and 63; the early ones join "
                  "near neighbours and cost less than 2. "
                  "Three groups remain after the 23/6 merge, which joined <code>T08</code> to <code>T09</code> and <code>T10</code>, and the next merge, the lab shows, would cost 25/2. The total within-group sum of squares is 11. Group G1, <code>T01</code> to <code>T04</code>, has median codes 1, 1, 2 and 2: deploying on "
                  "demand, lead times under an hour, restoring within a day, "
                  "and change fail rates of 16 to 30 percent. G2, <code>T05</code> to <code>T07</code>, has 3, 3, 3 and 3, between a day and a week "
                  "on the first three and 31 to 45 percent. G3, <code>T08</code> to <code>T10</code>, has 5, 5, 5 and 4, between a month and six "
                  "months and 46 to 60 percent. Whether to call one group high "
                  "is for the reader, who reads the medians; the lab does not "
                  "know."),
            ("p", "The preset <code>two-groups</code> asks for two groups from the "
                  "same ten teams. The hierarchy is the same, carried one merge further: G2 and G3 become one group, at a cost of 25/2, which raises the total within-group sum of squares from 11 to 23.5, and its medians are all 4, between a week and a month "
                  "on the first three and 46 to 60 percent on the last. That is the "
                  "use of the fusion coefficients in Appendix C. The costs of "
                  "reaching three, two and one groups are 23/6, 25/2 and 63, "
                  "and each jump says that more unlike groups are being forced "
                  "together. The sample cannot say which cut is right, because "
                  "that is a judgement the authors also made with other "
                  "criteria. Nor was it written to show a trade-off either way: it "
                  "was written so that groups come out, and the book&rsquo;s "
                  "finding is about its own survey."),
            ("h3", "Exercise"),
            ("p", "Four teams, coded on deployment frequency, lead time, time to "
                  "restore and change fail rate: `Quay` 1, 1, 1, 2; `Ridge` 1, 2, "
                  "1, 2; `Shoal` 4, 4, 3, 3; `Tarn` 5, 4, 3, 4."),
            ("p", "Find the squared distance between each pair of teams, then the "
                  "first merge and its fusion coefficient, then the groups for two "
                  "clusters. Type the teams into the lab to check, and then change "
                  "`Tarn` to 1, 1, 1, 2 and say what happens to the merges."),
            ("p", "The next lesson, Delivery and Organizational Performance, "
                  "asks the question that gives the groups their point: whether "
                  "the high performers' organizations do better."),
        ],
        "lab": ("acckit", {
            "mode": "delivery",
            "view": "cluster",
            "preset": "ten-teams",
            "presets": [
                {"id": "ten-teams",
                 "label": "Ten invented teams, three groups",
                 "teams": TEN_TEAMS,
                 "k": "3",
                 "expect": {
                            "adeGroups": "G1: T01, T02, T03, T04; G2: T05, T06, T07; G3: T08, T09, T10",
                            "adeMedDeploy": "G1: 1, on demand (multiple deploys per day); G2: 3, between once per day and once per week; G3: 5, between once per month and once every six months",
                            "adeMedFail": "G1: 2, 16–30%; G2: 3, 31–45%; G3: 4, 46–60%",
                            "adeWithin": "11",
                            "adeLastCoef": "23/6 ≈ 3.83 ({T08} + {T09, T10})",
                            "adeNextCoef": "25/2 = 12.50 ({T05, T06, T07} + {T08, T09, T10})",
                 }},
                {"id": "two-groups",
                 "label": "The same ten teams, two groups",
                 "teams": TEN_TEAMS,
                 "k": "2",
                 "expect": {
                            "adeGroups": "G1: T01, T02, T03, T04; G2: T05, T06, T07, T08, T09, T10",
                            "adeMedLead": "G1: 1, less than one hour; G2: 4, between one week and one month",
                            "adeWithin": "47/2 = 23.50",
                            "adeLastCoef": "25/2 = 12.50 ({T05, T06, T07} + {T08, T09, T10})",
                            "adeNextCoef": "63 ({T01, T02, T03, T04} + {T05, T06, T07, T08, T09, T10})",
                 }},
            ],
            "panel_title": "Which teams the clustering groups together",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Clustering by hand",
        "steps_intro": "Four steps, the last of them on teams you know.",
        "steps": [
            ("Code every team",
             "Put each team's four answers on the 1 to 6 scales, 1 the best option "
             "on each, and write them as four numbers."),
            ("Find the cheapest merge",
             "For every pair of groups compute the cost of joining them, and merge "
             "the cheapest. Repeat until one group is left, writing down each cost."),
            ("Cut the tree",
             "Pick the number of groups, look at where the costs jump, and read "
             "each group's median on each measure in words."),
            ("Do it on teams you know",
             "Code five or six teams near you, type them in, and compare the groups "
             "with your own idea of which teams are alike."),
        ],
        "worked": {
            "title": "The first merges among the ten teams",
            "intro": [
                "Follow the first three merges of <code>ten-teams</code>, by "
                "squared distance and the cost of Ward's merge.",
            ],
            "lines": [
                "T01 (1, 1, 2, 2) to T03 (1, 1, 2, 1): 0 + 0 + 0 + 1 = 1",
                "T01 to T04 (1, 1, 1, 2): 1 as well, so the tie goes to T03",
                "two single teams merge at half: T01 + T03 cost 1/2",
                "centre of T01 and T03: (1, 1, 2, 1.5), and T04 is at (1, 1, 1, 2)",
                "squared distance: 0 + 0 + 1 + 0.25 = 1.25",
                "T04 joins at (2 · 1 / 3) · 1.25 = 5/6",
            ],
            "after": [
                "Each merge is the cheapest available, which the lab found by "
                "trying every pair. The later merges, 1, 3/2, 5/3, 5/3, 23/6, "
                "25/2 and 63, are the same arithmetic on larger groups' centres.",
            ],
        },
        "quiz_title": "Clusters, Ward's method and the book's findings",
        "quiz": [
            {"q": "In the exercise, which pair of teams merges first, and at what "
                  "fusion coefficient?",
             "a": ["Quay and Ridge, at 1/2",
                   "Quay and Ridge, at 1",
                   "Shoal and Tarn, at 1/2",
                   "Shoal and Tarn, at 1"],
             "c": 0,
             "why": "The squared distance between Quay and Ridge is 1, the smallest "
                    "of the six, and two single teams merge at half the squared "
                    "distance: 1/2. Shoal and Tarn are 2 apart and merge second, at 1, and the last merge, of the two pairs, costs 99/4, about 25. Changing Tarn to Quay's codes makes the merges 0, 2/3 and 95/6: Tarn joins Quay for nothing, Ridge joins them cheaply, and Shoal alone is far away."},
            {"q": "What does cluster analysis know about whether an answer, such as "
                  "a lead time of under an hour, is a good one?",
             "a": ["Nothing: it sees only the distances between responses",
                   "It knows the shorter option is better and groups accordingly",
                   "It is told which end of each scale is better",
                   "It learns it from the organizational performance of the teams"],
             "c": 0,
             "why": "The chapter says the technique cannot tell what a response means, so it cannot tell a good answer from a bad one, which is why the authors can read "
                    "the groups afterwards. The lab's cfg says which end of a scale "
                    "is better only to word the medians; the clustering ignores it."},
            {"q": "In Appendix C, which of the five clustering methods performed "
                  "best on the authors' criteria?",
             "a": ["Ward's",
                   "Centroid",
                   "Median",
                   "Between-groups linkage"],
             "c": 0,
             "why": "The authors compared Ward's method, between-groups linkage, "
                    "within-groups linkage, centroid and median, and report that "
                    "the solution using Ward's performed best and was selected."},
            {"q": "What did the authors report in the Surprise! box about medium and "
                  "low performers in 2016?",
             "a": ["Medium performers did worse than low performers on change fail "
                   "rate",
                   "Low performers deployed more often than high performers",
                   "Medium performers restored service faster than high performers",
                   "Low performers had a lower change fail rate than high performers"],
             "c": 0,
             "why": "In 2016 the medium group's change fail rate was worse than the low group's. The authors do not explain it conclusively "
                    "and offer large rearchitecture work and neglected rework as "
                    "possibilities. The other options describe results the box does "
                    "not report."},
        ],
        "mistakes": [
            ("Thinking the clustering tells you which group is high performing",
             "The method sees distances and nothing else. We call a group high "
             "performing because we read its medians afterwards and see that they "
             "are the best options. The lab prints the medians so that the reading "
             "is yours."),
            ("Reading no trade-off as proof that speed causes stability",
             "The authors report that the high group is better on all four measures "
             "in their survey, which is evidence against the idea that speed must "
             "be bought with quality. Why the measures go together is a question "
             "for the later chapters on practices, and the lesson's invented teams "
             "were written to cluster, and show nothing about it."),
            ("Treating the groups as fixed bands every team can be placed in",
             "The groups are drawn from each year's responses, and the authors "
             "report that the high group kept pulling away and that last year's "
             "good was not enough. A cluster is a description of one sample in one "
             "year."),
        ],
        "standard": (
            "Finish when you can say what a fusion coefficient costs.",
            "Given teams coded on the four measures, merge them by Ward's method, "
            "write the cost of each merge, and read the groups' medians in words."
        ),
        "note": (
            "The lab clusters the teams you code, exactly, and reads the groups' "
            "medians. It cannot say how many groups are right, whether the "
            "answers are honest, or whether the groups mean anything about causes; "
            "the book's groups come from its survey's responses, and the lab's "
            "ten teams are invented."
        ),
    },
    # ---------------------------------------------------------------- 05
    # The Impact of Delivery Performance on Organizational Performance, and
    # Driving Change (PDF pp. 58-62 of the operator's copy): the organizational
    # performance measure (p. 58), "twice as likely" (p. 58), the noncommercial
    # measure (pp. 58-59), reading the figures (p. 59), small batches and
    # strategic software (p. 60), driving change (pp. 60-62).
    # Quote: PDF p. 58 of the operator's copy, 15 words; PDF p. 62, 9 words
    # (Deming, in the book's quotation of Humble et al. 2014), quotes.py OK.
    # Lesson total: 24 words.
    {
        "slug": "delivery-and-organizational-performance",
        "title": "Delivery and Organizational Performance",
        "module": "Chapter 2 · Measuring Performance",
        "one_line": "High performers' organizations were twice as likely to exceed their goals, and the lab shows what a ratio like that is, and is not.",
        "summary": (
            "The last part of Chapter 2 asks whether delivery performance matters "
            "to the organization, and ends with advice on using the measures. Read "
            "how organizational performance was measured, what 'twice as likely' "
            "reports, how the authors read the arrows in their figures, and why "
            "they warn against measures used for control; then work the ratio on "
            "invented teams, beside the difference and the odds ratio it is "
            "mistaken for."
        ),
        "key": [
            "organizational performance is a self rating",
            "twice as likely: a ratio of two shares",
            "a ratio is not a difference in shares",
            "a ratio is not an odds ratio",
            "an arrow is a prediction, not a proof",
            "measure to learn, not to punish",
        ],
        "key_label": "Delivery and the organization in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's; the other "
            "two are the lab's."
        ),
        "concepts": [
            ("Organizational performance",
             "How respondents rated their organization's relative performance on profitability, market share and productivity, a scale used and validated in earlier research. It is the respondents' own rating, not a figure taken from accounts."),
            ("Times as likely",
             "The share of one group meeting a goal divided by the share of "
             "another. If 60 percent of one group and 30 percent of the other "
             "meet it, the first is twice as likely."),
            ("Difference and odds ratio",
             "Two other comparisons of the same shares. The difference is the "
             "percentage points between them; the odds ratio divides each group's "
             "odds, those who met the goal over those who did not. Neither equals "
             "the ratio of shares."),
        ],
        "read_title": "Does delivery performance matter, and how to use the measures",
        "read_intro": (
            "Read the rest of Chapter 2 in your own copy first, from The Impact of "
            "Delivery Performance on Organizational Performance to the end. The "
            "lesson takes the finding, how the authors read their figures, and "
            "the closing advice, then computes the ratio."
        ),
        "body": [
            ("p", "The question of this part is the reason for the four measures: "
                  "does delivery performance matter to the organization? To find "
                  "out, respondents rated their organization&rsquo;s relative performance on profitability, market share and productivity, a scale the authors say has been validated "
                  "several times, found to correlate with return on investment "
                  "and to hold up through economic cycles. The finding is "
                  "stated in one sentence: across several years, "
                  "&ldquo;high-performing organizations were consistently twice as "
                  "likely to exceed these goals as low performers&rdquo;. The "
                  "authors read it as showing that software delivery capability "
                  "can be a competitive advantage."),
            ("p", "Two things about the measure matter for how to hold the finding. "
                  "It is self-reported: the delivery measures and the organizational rating are both survey answers, and Fowler&rsquo;s foreword notes that a survey captures subjective perceptions. And it is relative: respondents place their organization against others, not against a number. The authors answer the first by the validation of the scale and by the longer argument in Part II; the lesson notes it and moves on."),
            ("p", "In 2017 they added a measure for noncommercial organizations, "
                  "with a scale also validated before, and found that high performers were again twice as likely to exceed their objectives, across five noncommercial goals that include customer satisfaction and the organization's mission. The chapter&rsquo;s "
                  "Figure 2.4 draws this as arrows from software delivery "
                  "performance to the two kinds of organizational performance, "
                  "and a box on reading the book&rsquo;s figures explains the "
                  "arrows: each is a predictive relationship, read as drives, "
                  "predicts, affects or impacts. The authors say that the "
                  "analyses go beyond correlation into prediction, and Chapter 12 "
                  "says in what sense, which later lessons take up."),
            ("p", "Three consequences follow in the chapter. The ability to work "
                  "in small batches lets a team collect user feedback quickly, "
                  "for example by A/B testing, and the authors add that teams able to experiment with their product tend also to be the ones with the technical practices of continuous delivery. Delivery performance is an argument against "
                  "outsourcing software that is strategic to a business, while "
                  "software such as payroll or office tools is not strategic and can "
                  "be bought as a service; telling the two apart is of enormous "
                  "importance, and they point to Simon Wardley&rsquo;s mapping "
                  "method for that."),
            ("p", "The last section, Driving Change, is about using the numbers. "
                  "With delivery performance defined, teams can be compared with "
                  "their organizations and the industry, tracked over time and "
                  "tested for what moves them. The authors give a spoiler: change "
                  "approval boards do not improve delivery performance, they are "
                  "correlated negatively with both tempo and stability. They invite "
                  "readers to place their own teams in the book&rsquo;s taxonomy "
                  "and to set targets on the four measures. Then comes the "
                  "caution that ends the chapter. Where fear rules, they say, numbers become a tool of control and information that challenges the rules is hidden, and as Deming said, "
                  "&ldquo;whenever there is fear, you get the wrong numbers&rdquo;. "
                  "Culture first, then, and Chapter 3 is where the book begins."),
            ("p", "Now the arithmetic of the headline. The lab takes groups, how "
                  "many teams each has and how many met a goal, and prints each "
                  "group&rsquo;s share, the ratio of two groups&rsquo; shares, "
                  "their difference in percentage points and, separately, the odds "
                  "ratio. The sample is forty invented teams: twenty high "
                  "performers and twenty low. On <code>half-the-teams</code>, 12 "
                  "of the high group and 6 of the low group met the goal: 60 "
                  "percent and 30 percent, a ratio of 2.00, a difference of 30 "
                  "points. The odds are 12 to 8 and 6 to 14, an odds ratio of "
                  "3.50. The sentence &lsquo;twice as likely&rsquo; is the first "
                  "figure and not the last."),
            ("p", "The preset <code>rare-goal</code> changes the goal and keeps "
                  "the ratio: 4 of the high group and 2 of the low group met it, "
                  "20 percent and 10 percent. The ratio is again 2.00, and the "
                  "difference is 10 points, not 30; the odds ratio is 2.25. "
                  "&lsquo;Twice as likely&rsquo; is compatible with a difference "
                  "that is large or small, depending on how common the outcome is, "
                  "which the book&rsquo;s sentence does not say, since it gives no underlying shares. Whether the finding is "
                  "big enough to matter is a question about the shares, and the "
                  "lab asks for them."),
            ("p", "None of these is a cause. The ratio compares two groups drawn by "
                  "the clustering in one survey; it does not show that moving a "
                  "team from the low group to the high one would change its "
                  "organization&rsquo;s results. The book&rsquo;s case that it "
                  "would rests on prediction from many years of data and on "
                  "theory, which Part II sets out, and on the survey&rsquo;s "
                  "limits that Fowler names. The lab shows what the ratio is "
                  "arithmetically."),
            ("h3", "Exercise"),
            ("p", "A goal is met by 18 of 20 high-performing teams and 9 of 20 "
                  "low-performing teams. Find each share, the ratio, the "
                  "difference in points and the odds ratio. Then type the groups "
                  "in to check, and say which of the three comparisons would make "
                  "the result look largest in a headline, and which looks "
                  "smallest."),
            ("p", "The next course, Measuring and Changing Culture, begins "
                  "with its first lesson, Modeling and Measuring Culture: the "
                  "authors&rsquo; model of the culture that, they say, makes "
                  "measurement safe."),
        ],
        "lab": ("acckit", {
            "mode": "groups",
            "view": "likely",
            "preset": "half-the-teams",
            "presets": [
                {"id": "half-the-teams",
                 "label": "Twenty high and twenty low performers, a common goal",
                 "rows": GOAL_HALF,
                 "first": "high",
                 "second": "low",
                 "expect": {
                            "agrShares": "high 12 of 20 = 60%; low 6 of 20 = 30%",
                            "agrRatio": "2×",
                            "agrDiff": "+30 points",
                            "agrOdds": "3.50",
                 }},
                {"id": "rare-goal",
                 "label": "The same groups, a goal few met",
                 "rows": GOAL_RARE,
                 "first": "high",
                 "second": "low",
                 "expect": {
                            "agrShares": "high 4 of 20 = 20%; low 2 of 20 = 10%",
                            "agrRatio": "2×",
                            "agrDiff": "+10 points",
                            "agrOdds": "2.25",
                 }},
            ],
            "panel_title": "How much likelier, and what that ratio hides",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Reading a 'times as likely'",
        "steps_intro": "Four steps, the last of them on a claim you have read.",
        "steps": [
            ("Find the two shares",
             "For each group divide those who met the goal by the group's size. "
             "Without the shares, a ratio cannot be judged."),
            ("Divide them",
             "Divide the larger share by the smaller to get times as likely, and "
             "subtract them to get the difference in points."),
            ("Add the odds ratio if the odds are quoted",
             "For each group divide those who met the goal by those who did not, "
             "then divide the two figures. It will not match the ratio of shares."),
            ("Do it on a claim of your own",
             "Take a report that says one group is some times as likely to succeed. "
             "Find the two shares in it, or note that it does not give them."),
        ],
        "worked": {
            "title": "Twice as likely, and three and a half times the odds",
            "intro": [
                "Work <code>half-the-teams</code> by hand.",
            ],
            "lines": [
                "high: 12 of 20 = 60 percent",
                "low: 6 of 20 = 30 percent",
                "ratio: 60 / 30 = 2.00",
                "difference: 60 - 30 = 30 points",
                "odds high: 12 to 8 = 3/2",
                "odds low: 6 to 14 = 3/7",
                "odds ratio: (3/2) / (3/7) = 7/2 = 3.50",
            ],
            "after": [
                "All three describe the same forty teams. Which one a sentence "
                "uses changes how large the result sounds, and none of them says "
                "why the groups differ.",
            ],
        },
        "quiz_title": "Ratio, difference and the chapter's cautions",
        "quiz": [
            {"q": "In the exercise, 18 of 20 high-performing teams and 9 of 20 "
                  "low-performing teams met a goal. How many times as likely are "
                  "the high performers to have met it?",
             "a": ["2.00 times",
                   "11 times",
                   "45 times",
                   "0.50 times"],
             "c": 0,
             "why": "The shares are 90 percent and 45 percent, and 90 divided by 45 "
                    "is 2. The odds ratio is 11, since the odds are 18 to 2 and 9 "
                    "to 11; 45 is the difference in percentage points; and 0.50 is "
                    "the low group's share relative to the high group's, the "
                    "inverse, which answers a different question."},
            {"q": "Which of these did the chapter's noncommercial measure cover?",
             "a": ["Customer satisfaction",
                   "Profitability",
                   "Market share",
                   "Productivity"],
             "c": 0,
             "why": "Customer satisfaction is one of the five noncommercial goals, with the mission among them. Profitability, market share and productivity are the commercial measure."},
            {"q": "On the presets <code>half-the-teams</code> and "
                  "<code>rare-goal</code>, what is the same and what differs?",
             "a": ["The ratio is 2.00 on both; the difference in points is 30 on "
                   "one and 10 on the other",
                   "The difference in points is 30 on both; the ratio is 2.00 on one "
                   "and 1.50 on the other",
                   "The odds ratio is 3.50 on both; the ratio is 2.00 on one and "
                   "2.25 on the other",
                   "Everything is the same, since the two groups are the same"],
             "c": 0,
             "why": "Both have a ratio of 2.00; the differences are 30 and 10 "
                    "points, and the odds ratios 3.50 and 2.25. The groups are the "
                    "same size but a different goal was met by different numbers."},
            {"q": "What does the chapter say about change approval boards, in its "
                  "Driving Change section?",
             "a": ["They are negatively correlated with tempo and stability",
                   "They improve stability at some cost to tempo",
                   "They are positively correlated with change fail rate being low",
                   "They are not mentioned in the chapter"],
             "c": 0,
             "why": "The authors answer their own question, whether change "
                    "management boards improve delivery performance, with a "
                    "spoiler: they do not, and the correlation with tempo and with stability is negative."},
        ],
        "mistakes": [
            ("Reading 'twice as likely' as twice the result",
             "It is a ratio of two shares of teams meeting a goal. On the lesson's "
             "sample it is 2.00 for shares of 60 and 30 percent and for 20 and 10 "
             "percent, with differences of 30 and 10 points. It says nothing of "
             "how far the goal was exceeded."),
            ("Using the measures to rank and reward teams",
             "The chapter ends on the warning that where people fear the "
             "measurement, they hide what challenges the rules, and the numbers "
             "are wrong. The four measures are for a team to learn from and to set "
             "its own targets against."),
            ("Treating the arrows as proof of cause",
             "The authors say their arrows are predictive relationships, going "
             "beyond correlation; they do not say each is an experiment. Fowler's "
             "foreword adds that confirmation from other approaches would give "
             "him more confidence. The finding is strong evidence of a pattern "
             "and the argument for its cause is the book's."),
        ],
        "standard": (
            "Finish when you can compare two groups three ways.",
            "Given each group's size and how many met a goal, compute the share, "
            "the ratio, the difference in points and the odds ratio, and say what "
            "each does and does not show."
        ),
        "note": (
            "The lab compares the shares you give it. It cannot tell whether the "
            "groups were drawn well, whether the goal was a fair one, or whether "
            "the difference is a cause; the book's 'twice as likely' is its "
            "survey's, from respondents' own ratings in several years."
        ),
    },
]
