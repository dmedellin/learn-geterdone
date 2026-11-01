"""Surveys, Data and Statistical Methods, lessons 1-5 -- Chapters 14 and 15 and
the first two sections of Appendix C.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 14, Why Use a Survey;
Chapter 15, The Data for the Project; Appendix C, Statistical Methods Used in
Our Research (Survey Preparation, Data Collection, Tests for Bias, Testing for
Relationships, Tests of the Measurement Model). Pages in the comments are PDF
pages of the operator's copy; the lessons cite by chapter and section. Every
quotation is copied from that copy and checked with quotes.py. The samples are
written for these lessons: none of the book's tables, figures, survey items or
example data is reproduced. The design is docs/accelerate/PLAN.md, section C,
Course 7.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what one "
    "measure says about that sample; the book's findings are its survey's, and a "
    "correlation is not a cause."
)


# ---------------------------------------------------------------- 01 models

# A team's fourteen days, written for the lesson. Times are decimal hours from
# the start of the period (hour 0 is the start of day 1; 14 days = 336 hours).
# change, committed, deployed, failed
PIPELINE_ONLY = (
    "c1, 9, 34, no; c2, 35, 87, no; c3, 82, 108, no; c4, 129, 177, no; "
    "c5, 181, 206, no; c6, 226, 275, no; c7, 278, 304, no; c8, 285, 334, no"
)
WITH_HOTFIXES = (
    "c1, 9, 34, no; c2, 35, 87, yes; c3, 82, 108, no; c4, 129, 177, no; "
    "c5, 181, 206, no; c6, 226, 275, yes; c7, 278, 304, no; c8, 285, 334, no; "
    "h1, 88.5, 90.5, no; h2, 276, 277.5, no"
)
# incident, started, restored: from the on-call tracker, a separate system
TEAM_INCIDENTS = "i1, 87.5, 90.5; i2, 275.5, 277.5"

# 01 exercise: seven days, 168 hours.
SEVEN_DAY_LOG = (
    "e1, 10, 30, no; e2, 40, 70, no; e3, 80, 120, no; e4, 100, 150, no"
)
SEVEN_DAY_ALL = (
    "e1, 10, 30, yes; m1, 31, 34, no; e2, 40, 70, no; e3, 80, 120, no; "
    "e4, 100, 150, no; m2, 125, 130, no"
)


# ---------------------------------------------------------------- 02 models

# Four items on a seven-point scale; item 4 is worded in reverse.
FOUR_ITEMS = (
    "q1, ownership, no; q2, ownership, no; q3, ownership, no; q4, ownership, yes"
)
FIVE_HONEST = (
    "r1, 6, 5, 6, 2; r2, 5, 5, 6, 3; r3, 4, 5, 4, 4; r4, 6, 6, 5, 2; "
    "r5, 3, 4, 3, 5"
)
SIX_WITH_STRAIGHT = FIVE_HONEST + "; r6, 7, 7, 7, 7"
ELEVEN_WITH_STRAIGHT = (
    "r1, 6, 5, 6, 2; r2, 5, 5, 6, 3; r3, 4, 5, 4, 4; r4, 6, 6, 5, 2; "
    "r5, 3, 4, 3, 5; r7, 6, 5, 6, 2; r8, 5, 5, 6, 3; r9, 4, 5, 4, 4; "
    "r10, 6, 6, 5, 2; r11, 3, 4, 3, 5; r6, 7, 7, 7, 7"
)

# 02 exercise.
EXERCISE_ANSWERS = (
    "s1, 6, 6, 5, 2; s2, 5, 5, 5, 3; s3, 7, 6, 6, 1; s4, 4, 4, 5, 4; "
    "s5, 1, 1, 1, 1"
)


# ---------------------------------------------------------------- 03 models

# Twenty people reached by invitation, written for the lesson. person,
# referred_by ("-" for a seed), group (where they work).
THREE_SEEDS = (
    "ana, -, retail; bo, -, bank; cy, -, health; "
    "dee, ana, retail; eli, ana, retail; fay, ana, startup; "
    "gus, bo, bank; hal, bo, bank; ida, cy, health; "
    "jon, dee, retail; kim, dee, retail; lee, eli, startup; "
    "max, gus, bank; ned, gus, bank; oli, gus, bank; pam, hal, bank; "
    "quin, ida, health; ray, jon, retail; sue, max, bank; tom, max, bank"
)
SIX_SEEDS = (
    "uma, -, retail; vic, -, bank; wes, -, health; xia, -, startup; "
    "yan, -, retail; zoe, -, health; "
    "abe, uma, retail; bea, vic, bank; cal, vic, bank; dot, wes, health; "
    "eve, xia, startup; fox, xia, startup; gil, yan, retail; hue, zoe, health; "
    "ivy, bea, bank; jay, dot, health; kai, eve, startup; lou, gil, retail; "
    "mae, hue, health; ned, ivy, bank"
)

# 03 exercise: eight people, two seeds.
EIGHT_PEOPLE = (
    "a, -, east; b, -, west; c, a, east; d, a, east; e, b, west; f, c, east; "
    "g, c, east; h, e, west"
)


# ---------------------------------------------------------------- 04 models

# Early and late respondents by the size of their organization (a categorical
# answer): category, early, late. Written for the lesson.
SIZE_NO_DIFFERENCE = "small, 19, 11; medium, 29, 21; large, 12, 8"
SIZE_DIFFERENCE = "small, 12, 18; medium, 30, 20; large, 18, 2"
HOTFIX_SMALL = "yes, 9, 1; no, 21, 9"

# 04 exercise.
PIPELINE_ANSWER = "yes, 30, 10; no, 20, 20"


# ---------------------------------------------------------------- 05 models

# Loadings of invented items on invented constructs; item, construct, loading.
SOUND_LOADINGS = (
    "rc1, release-confidence, 0.85; rc2, release-confidence, 0.80; "
    "rc3, release-confidence, 0.75; rc4, release-confidence, 0.70; "
    "tt1, team-trust, 0.90; tt2, team-trust, 0.85; tt3, team-trust, 0.80"
)
SOUND_BETWEEN = "release-confidence, team-trust, 0.45"
WEAK_LOADINGS = (
    "rc1, release-confidence, 0.85; rc2, release-confidence, 0.80; "
    "rc3, release-confidence, 0.75; rc4, release-confidence, 0.70; "
    "tf1, tool-fit, 0.70; tf2, tool-fit, 0.60; tf3, tool-fit, 0.55"
)
WEAK_BETWEEN = "release-confidence, tool-fit, 0.30"
CLOSE_LOADINGS = (
    "rc1, release-confidence, 0.85; rc2, release-confidence, 0.80; "
    "rc3, release-confidence, 0.75; rc4, release-confidence, 0.70; "
    "rr1, release-readiness, 0.85; rr2, release-readiness, 0.80; "
    "rr3, release-readiness, 0.80; rr4, release-readiness, 0.75"
)
CLOSE_BETWEEN = "release-confidence, release-readiness, 0.80"

# 05 exercise.
EXERCISE_LOADINGS = (
    "c1, scope, 0.80; c2, scope, 0.70; c3, scope, 0.65; "
    "d1, pace, 0.90; d2, pace, 0.85; d3, pace, 0.80"
)
EXERCISE_BETWEEN = "scope, pace, 0.75"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 14 opening and the first two reasons (PDF pp. 197-201 of the
    # operator's copy): the five reasons (p. 197); speed and ease, four
    # collections of four to six weeks, analysis in three to four weeks (p.
    # 198); lead time against cycle time, vetted items (p. 199); early and late
    # responders named (p. 200); measuring the full stack, the disk-storage
    # example (pp. 200-201). Preface p. 24: over 23,000 responses, over 2,000
    # organizations; p. 27: 2014 through 2017. Fowler's foreword, PDF p. 15-16.
    # Quote: PDF p. 198 of the operator's copy, 14 words, quotes.py OK.
    # Lesson total: 14 words.
    {
        "slug": "surveys-collect-data-quickly",
        "title": "Surveys Allow You to Collect and Analyze Data Quickly",
        "module": "Chapter 14 · Why Use a Survey",
        "one_line": "A team can read its delivery performance from a log or ask the people who do the work; the chapter's first two reasons for asking are speed and what a log never sees.",
        "summary": (
            "Chapter 14 asks why the authors used a survey when tools can already "
            "report lead time. Read its first two reasons, speed and the full stack, "
            "and the story of a storage team whose logs said everything was fine; "
            "then compute one team's four delivery measures from a log, and again "
            "with the hotfix path the log does not record."
        ),
        "key": [
            "system data is what your tools record",
            "a survey is fast across organizations",
            "the same word can mean two measures",
            "a log sees only what it is wired to",
            "ask people what the log cannot see",
        ],
        "key_label": "Surveys and system data in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the authors', the second the "
            "lab's, and the third the chapter's point about wording."
        ),
        "concepts": [
            ("System data",
             "The authors' name for data gathered by instrumenting the delivery "
             "process and the toolchain: commit times, deploy times, incident "
             "records. The chapter asks why anyone would collect survey data when "
             "system data of this kind is available."),
            ("Coverage",
             "The part of the work a source can see. A pipeline log covers every "
             "deploy that goes through the pipeline; a deploy made by hand to "
             "production happens in the world and is not in the log. A log with "
             "gaps still reports exact numbers, about the part it covers."),
            ("A shared definition",
             "Words and definitions that every respondent reads the same way. The "
             "authors' point is that two teams can use one name for two measures, "
             "or two names for one, and a survey item removes the doubt by asking "
             "everyone the same thing."),
        ],
        "read_title": "The chapter's first two reasons, then the count",
        "read_intro": (
            "Read the opening of Chapter 14 and the sections on speed and on the "
            "full stack in your own copy first. The lesson sets out the authors' "
            "case, then computes what a log with a gap reports."
        ),
        "body": [
            ("p", "&ldquo;Often, the strongest reason to use surveys is speed and ease "
                  "of data collection.&rdquo; That is Forsgren, Humble and Kim "
                  "starting the first of five reasons that Chapter 14, Why Use a "
                  "Survey, gives for asking people. This lesson reads the opening of "
                  "the chapter and its first two reasons, speed and the full stack. "
                  "The remaining three, completeness, trust and the things only a "
                  "survey can measure, are the next lesson's."),
            ("p", "The chapter begins from a fair question. Teams that want to "
                  "know how well their software delivery performs often start "
                  "by instrumenting the delivery process and the toolchain, and the "
                  "authors call what that yields system data. Several tools on the "
                  "market now report measures such as lead time. So why would anyone "
                  "also collect survey data? The authors list five reasons: a survey "
                  "is quick, the full stack is hard to measure from system data, so is "
                  "completeness, survey data can be trusted, and some things can "
                  "only be measured by asking."),
            ("p", "The first reason is the speed of a whole research program. The "
                  "authors say the data in the book was collected four times, each time "
                  "over four to six weeks, from thousands of respondents around the "
                  "world representing thousands of organizations; the Preface counts "
                  "over 23,000 survey responses and over 2,000 organizations across "
                  "the four years of research, 2014 through 2017. They ask the reader "
                  "to imagine the legal clearances, the data specifications and the "
                  "transfers that would be needed to gather system data from so many "
                  "teams within the same weeks. Then comes the cleaning and analysis, which for "
                  "the State of DevOps Reports generally took three to four weeks."),
            ("p", "The deeper obstacle, the authors argue, is what the data means. Teams "
                  "use the same name for different measures. The chapter's example is "
                  "the pair lead time and cycle time, which it says are often used "
                  "interchangeably and often confused; if one team calls a measure "
                  "cycle time, another calls the same thing lead time, and a third "
                  "calls something different lead time, the analyst does not know which "
                  "variable is which. A reader can see the difficulty in the book "
                  "itself: Chapter 2 measures lead time from a commit to code running "
                  "in production, while this chapter, glossing the term in passing, "
                  "ends the clock at code in a deployable state. A vetted survey item "
                  "fixes the words for everyone, so it matters what respondents were "
                  "asked and not what their organization calls it. Rigorous research "
                  "adds checks that the survey itself did not bias the answers, among "
                  "them a comparison of early and late responders, which Appendix C "
                  "describes and the lesson Tests for Bias works."),
            ("p", "The second reason is that system data is rarely exhaustive, even "
                  "when it is good. The authors tell of one of them, earlier a "
                  "performance engineer on enterprise disk storage systems. Her team "
                  "had instrumented every level of the machine and had the numbers "
                  "to show it performed well, yet customers kept reporting that it was "
                  "slow, and for the first reports the logs were taken as the answer. "
                  "The reports formed a pattern. The machine was fast. What the team "
                  "had not measured was the interface, the way customers used the box, "
                  "which introduced the slowness. People's reports were less precise "
                  "than the logs, minutes against milliseconds, yet they showed the "
                  "team where to look. The authors draw the lesson for any team: ask "
                  "the people who build and run the system, everyone and not a few, so "
                  "that a couple of very positive or very negative voices do not "
                  "decide the picture. A footnote adds the condition that the "
                  "request must be honest, with no instruction to answer well, and "
                  "that anonymity helps."),
            ("p", "Now the count, on a team of the lesson's own. Fourteen days of a "
                  "pipeline log hold eight deploys, each with the hour its change was "
                  "committed and the hour it was deployed. The team also pushes "
                  "emergency fixes to production by hand, outside the pipeline, and "
                  "the log knows nothing of them. The lab's delivery view takes the "
                  "records and computes the four measures of Chapter 2: deployments, "
                  "with their rate per day and per week, the median lead time from "
                  "commit to deploy with its answer option on the book's six-option "
                  "scale, the change fail rate with its band, and the median time to "
                  "restore. On the preset <code>pipeline-log</code> it counts 8 "
                  "deployments, 4 a week, a median lead time of 37 hours, which is "
                  "between one day and one week, and a change fail rate of 0 percent, in the "
                  "book's lowest band, 0 to 15 percent, "
                  "because the pipeline marks a deploy failed only when the pipeline "
                  "itself fails. Two incidents, from the on-call tracker, lasted 3 and "
                  "2 hours, a median time to restore of 2.5 hours."),
            ("p", "The preset <code>with-hotfixes</code> adds the two emergency "
                  "deploys the log missed, made 2 and 1.5 hours after their commits, "
                  "and records the truth the pipeline did not: the two deploys that "
                  "caused those incidents had failed. The lab now counts 10 "
                  "deployments, 5 a week, a median lead time of 26 hours, still "
                  "between one day and one week, and a change fail rate of 20 "
                  "percent, two failed of ten, which falls in the 16 to 30 percent band. The median time to restore is "
                  "unchanged at 2.5 hours, since the incidents came from a separate "
                  "record. The log was exact about what it covered. It missed a fifth "
                  "of the deploys, gave a lead time 11 hours too long, and showed no "
                  "failures where the team had two."),
            ("p", "Read the figures as the authors would, as a reason to look "
                  "elsewhere too. Neither list is the verdict on the team, and the "
                  "lab cannot say which of your own sources is the one with the gap. "
                  "A survey is not the cure for it: the authors add that people "
                  "will not have perfect knowledge or visibility either, so the "
                  "claim is that the two views together show more than one. Martin "
                  "Fowler's foreword makes the matching caution about the book, "
                  "that its surveys capture subjective perceptions and that he "
                  "wonders how the sample reflects the wider IT world. The next "
                  "lesson turns to that doubt."),
            ("h3", "Exercise"),
            ("ul", [
                "A team's seven days (168 hours). Logged deploys, as "
                "`change, committed, deployed`: `e1, 10, 30; e2, 40, 70; e3, 80, 120; "
                "e4, 100, 150`. The log marks none of them failed.",
                "Two deploys made by hand, not logged: `m1, 31, 34` and "
                "`m2, 125, 130`. The first repaired `e1`, which had in fact failed; "
                "the second shipped an urgent change.",
            ]),
            ("p", "By hand, compute the deployments, the deployments per week, the "
                  "median lead time and the change fail rate from the log alone, and "
                  "again with the two hand deploys and the failure of <code>e1</code>. "
                  "Then type both versions into the lab to check your count. Find the "
                  "measure the log gets right and the measure it gets most wrong."),
            ("p", "Surveys are quick and see across the boundary of any one system. "
                  "The authors also claim that survey data can be trusted, a claim "
                  "many engineers resist. The next lesson, You Can Trust Survey Data, "
                  "reads that argument."),
        ],
        "lab": ("acckit", {
            "mode": "delivery",
            "view": "metrics",
            "preset": "pipeline-log",
            "presets": [
                {"id": "pipeline-log",
                 "label": "Fourteen days as the pipeline log records them: eight deploys",
                 "days": "14",
                 "changes": PIPELINE_ONLY,
                 "incidents": TEAM_INCIDENTS,
                 "expect": {"adeDeploys": "8", "adePerWeek": "4", "adeLead": "1 d 13 h", "adeLeadOpt": "between one day and one week", "adeFail": "0 = 0%", "adeFailBand": "0–15%", "adeRestore": "2 h 30 min"}},
                {"id": "with-hotfixes",
                 "label": "The same fourteen days with the two emergency deploys and their failures",
                 "days": "14",
                 "changes": WITH_HOTFIXES,
                 "incidents": TEAM_INCIDENTS,
                 "expect": {"adeDeploys": "10", "adePerWeek": "5", "adeLead": "1 d 2 h", "adeLeadOpt": "between one day and one week", "adeFail": "1/5 = 20%", "adeFailBand": "16–30%", "adeRestore": "2 h 30 min"}},
            ],
            "panel_title": "The four measures from a log, with and without a gap",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Comparing a log with the work",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List every path to production",
             "Write down each way a change reaches users: the pipeline, a hand deploy, "
             "a configuration push, a vendor update. Mark the ones that write to the "
             "log you would measure from."),
            ("Compute the four measures from the log",
             "Count the deploys and the deploys per week, take the median of the "
             "lead times, and divide the failed deploys by all deploys, as the log "
             "records them."),
            ("Add the paths the log misses and recompute",
             "Type the unlogged deploys and any failures the log did not mark, run "
             "the lab again, and write down each measure that moved and by how much."),
            ("Do it on a service you run",
             "Pick one service and one week. Count its deploys from the tool, then "
             "ask three people on the team how many they made. Write down whether "
             "the counts agree and which path explains the difference."),
        ],
        "worked": {
            "title": "Median lead time, with and without the hand deploys",
            "intro": [
                "Take the lead times in hours from <code>pipeline-log</code>, then "
                "from <code>with-hotfixes</code>.",
            ],
            "lines": [
                "logged leads: 25 52 26 48 25 49 26 49 (hours)",
                "sorted: 25 25 26 26 48 49 49 52",
                "eight values: the middle two are 26 and 48",
                "median = (26 + 48) / 2 = 37",
                "add the hand deploys: 2 and 1.5 hours, ten values",
                "sorted: 1.5 2 25 25 26 26 48 49 49 52",
                "the middle two are 26 and 26, so the median is 26",
                "change fail rate: 0 of 8 logged, 2 of 10 in fact",
                "2 / 10 = 20 percent",
            ],
            "after": [
                "A median of an even number of values is the mean of the middle two. "
                "Adding two fast deploys pulled the middle down from between 26 and "
                "48 to between 26 and 26, which is why the median moved by 11 hours "
                "although eight of the ten deploys are the same.",
            ],
        },
        "quiz_title": "Logs, surveys and what the chapter claims",
        "quiz": [
            {"q": "In the exercise, what is the median lead time with the two hand "
                  "deploys included?",
             "a": ["35 hours, the median of the logged deploys",
                   "25 hours",
                   "24.7 hours",
                   "20 hours"],
             "c": 1,
             "why": "The six lead times are 20, 30, 40, 50, 3 and 5 hours, which sort to "
                    "3, 5, 20, 30, 40, 50. The middle two are 20 and 30, so the median "
                    "is 25. The 35 hours is the log's median, (30 + 40) / 2. The "
                    "24.7 hours is the mean, 148 / 6, which is a different statistic "
                    "and not the one the book's lead-time question asks for."},
            {"q": "In the exercise, what is the change fail rate once the hand deploys "
                  "and the failure of e1 are counted?",
             "a": ["0 percent, as the log says",
                   "25 percent, one failure in the four logged deploys",
                   "About 17 percent, one failure in six deploys",
                   "33 percent, two of six, counting the repair as a failure"],
             "c": 2,
             "why": "Six deploys now happened and one of them failed, so 1 / 6, about "
                    "16.7 percent. The log's 0 percent is the gap itself. One in four "
                    "keeps the old denominator. The repair deploy was a success, so "
                    "it does not add a failure."},
            {"q": "In the chapter's disk-storage story, why did the logs say the "
                  "machine was fast while customers reported it slow?",
             "a": ["The logs had been altered by someone with root access",
                   "Customers hoped for discounts under their service agreements",
                   "The logs recorded everything inside the box, but not the way "
                   "customers used its interface",
                   "The logs were too coarse to show slow responses"],
             "c": 2,
             "why": "The logs were accurate about the box. The slowness came from the "
                    "interface, which nothing had instrumented. The authors do note that "
                    "customers could have had an incentive to exaggerate, but the "
                    "reports formed a pattern. They also say the people's data was "
                    "less precise than the logs and still pointed to where to look."},
            {"q": "How does the chapter describe the collection of the data in the "
                  "book?",
             "a": ["Once, over a full year",
                   "Four times, each over four to six weeks, from around the world",
                   "Every month for four years, from one company's teams",
                   "Four times, each over a single weekend"],
             "c": 1,
             "why": "The chapter says the data was gathered in four separate rounds, each "
                    "lasting four to six weeks, drawing thousands of respondents who "
                    "worked at thousands of organizations around the world. That "
                    "speed is the first reason it gives."},
        ],
        "mistakes": [
            ("Trusting a measure because it is precise",
             "A log's numbers are exact about what the log covers, and the storage "
             "team's logs were exact to the millisecond. The lab shows the same on a "
             "small scale: 8 deploys, 37 hours and 0 percent failures are exact for the "
             "pipeline, and the team made 10 deploys, with 2 failures. Precision "
             "answers how closely a number reports what it measured, and says "
             "nothing about what it left out."),
            ("Reading the chapter as telling teams to drop their logs",
             "The authors ask why a team would collect survey data and not just "
             "toolchain data, and their reasons are about what a survey adds. They "
             "also say that people lack perfect knowledge, and they grant that tools "
             "can now report measures such as lead time. The lesson's two presets are "
             "one team seen through two sources, not a contest."),
            ("Taking a quick survey to be a short one",
             "Speed here is the speed of collecting and cleaning data from many "
             "teams once vetted items exist. Chapter 13 is wary of quick surveys that "
             "rest on a single question: it allows that a carefully developed one, "
             "its example being the Net Promoter Score, is useful, and draws only "
             "narrow conclusions from it. The authors measure their constructs "
             "with several items. A survey is fast to run because a great deal of "
             "work went into its wording first."),
        ],
        "standard": (
            "Finish when you can say what a log leaves out.",
            "Given a log and the paths it does not record, compute the deployments, "
            "median lead time and change fail rate with and without them, and name "
            "the measure the log alone gets most wrong."
        ),
        "note": (
            "The lab computes from the records you type, and it takes your word that "
            "they are complete. It cannot tell whether a log is missing deploys or "
            "whether a respondent's memory of them is better; that is a comparison of "
            "two sources, and you make it."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 14, Measuring completely with system data is difficult (PDF pp.
    # 201-202, the version-control example), You can trust survey data (pp.
    # 203-205, including the sidebar on bad actors and system data and the
    # figure of over 23,000 respondents, p. 205), Some things can only be
    # measured through surveys (pp. 206-208, turnover and retention as proxies
    # for culture, the footnotes on p. 208). Fowler's foreword, PDF p. 15-16.
    # Quote: PDF p. 205 of the operator's copy, 14 words, quotes.py OK.
    # Lesson total: 14 words.
    {
        "slug": "you-can-trust-survey-data",
        "title": "You Can Trust Survey Data",
        "module": "Chapter 14 · Why Use a Survey",
        "one_line": "Engineers who trust a log and doubt a survey have met bad data in both; the chapter argues that the survey is harder to move, and that some things only a survey measures.",
        "summary": (
            "The rest of Chapter 14 answers the doubt every survey meets: people may "
            "lie. Read the authors' comparison of one bad actor in a log with a few "
            "in a pool of thousands, and their case that culture cannot be read from "
            "turnover; then score a construct with one respondent who answers "
            "everything the same, and see how far that one respondent moves the "
            "mean."
        ),
        "key": [
            "a system sees only what is inside it",
            "logs go wrong too, with few data points",
            "pooled answers dilute one bad respondent",
            "turnover is not a measure of culture",
            "feelings and reasons need a question",
        ],
        "key_label": "Trusting survey data in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the other two "
            "the lab's."
        ),
        "concepts": [
            ("Proxy",
             "A measure used in place of one that is hard to collect. Turnover from an "
             "HR system is the chapter's proxy for organizational culture. The authors "
             "argue that a proxy can move for reasons unrelated to the thing it "
             "stands for, and can be gamed."),
            ("Reverse-coded item",
             "An item worded so that agreeing with it means the opposite of the "
             "construct. On a seven-point scale its answer is turned round before "
             "scoring: the score is 8 minus the answer, so a 7 counts as a 1. The "
             "book's chapters do not discuss the device; the lesson uses it to show "
             "what a pattern of identical answers looks like."),
            ("Straight-lining",
             "Giving the same answer to every item. The lab uses it as a stand-in for "
             "a respondent whose answers a reader would doubt, without claiming that "
             "any such respondent is lying; the person may simply have hurried."),
        ],
        "read_title": "Three more reasons, then the count",
        "read_intro": (
            "Read the sections from Measuring Completely with System Data to the end "
            "of Chapter 14 in your own copy first. The lesson sets out the authors' "
            "argument, then scores a construct with and without one suspect "
            "respondent."
        ),
        "body": [
            ("p", "&ldquo;In this case, the use of a survey actually protects us against "
                  "bad actors.&rdquo; Forsgren, Humble and Kim write that in the "
                  "section of Chapter 14 headed You Can Trust Survey Data. This "
                  "lesson reads that section and the two around it: Measuring "
                  "Completely with System Data Is Difficult, before it, and Some "
                  "Things Can Only Be Measured Through Surveys, after."),
            ("p", "The third reason continues the last lesson's. A system knows only what "
                  "happens inside its boundaries, and people can see around it. The "
                  "authors take version control. A team can say whether every "
                  "production artifact is under it, because the team sees all of its "
                  "work. A system can count the files that were checked in, but it "
                  "does not know how many files were not, so it cannot give the "
                  "percentage that matters. People lack perfect knowledge too, the "
                  "authors add, but ignoring what the professionals perceive loses an "
                  "important view."),
            ("p", "The fourth reason answers the question the authors say they are asked "
                  "most. They use a thought exercise with audiences of technologists. "
                  "Few trust survey data. More trust their system or log data, because "
                  "it feels untampered with. Then almost everyone admits having seen "
                  "bad data come out of a system, since people build systems and make "
                  "mistakes, and since it takes only one bad actor to write code that "
                  "gives erroneous data. Engineers trust logs because they understand "
                  "how systems work and expect to spot the errors; survey methods feel "
                  "foreign. The authors point to Part II for the steps that make survey "
                  "data reliable: carefully identified measures, latent constructs, "
                  "and statistical tests of validity and reliability."),
            ("p", "Then the comparison on which the lesson turns. In a log, one "
                  "or a few people can change what is reported, a highly motivated "
                  "bad actor with high access or a developer whose mistake no review "
                  "caught, and the business probably watches only one or a few data "
                  "points, so the damage is large and may go unnoticed for months or "
                  "years. In survey data, a few motivated respondents can lie, but "
                  "their effect depends on the size of the group. The authors report "
                  "over 23,000 pooled respondents and say it would take several "
                  "hundred of them lying in a coordinated way, on every item of a "
                  "construct, to the same degree and in the same direction, to make a "
                  "noticeable difference. That is their estimate and not a "
                  "computation they show. They add that responses are anonymous, "
                  "items avoid propaganda, constructs pass tests of validity and "
                  "reliability, and the data come from around the world."),
            ("p", "Now the count, on a team of six. The lab's score view takes a "
                  "construct called <code>ownership</code> with four items on a seven-point "
                  "scale, the fourth worded in reverse, and each respondent's answers. "
                  "A respondent's score is the mean of their four item scores after "
                  "the reverse-coded answer is turned round, as 8 minus the answer. "
                  "On the preset <code>five-respondents</code> the scores are 5.75, "
                  "5.25, 4.25, 5.75 and 3.25, and the construct's mean is 4.85. The "
                  "preset <code>six-respondents</code> adds <code>r6</code>, who answered 7 to "
                  "all four items. Turned round, those are 7, 7, 7 and 1, a score of "
                  "5.5, and the mean over six is 119 / 24, about 4.96. One respondent "
                  "moved the mean by 0.108. The lab's last tile gives the means if "
                  "nothing were reversed, the error to avoid: 4.45 for the five and "
                  "4.875 for the six. Its line tile counts respondents above, at and "
                  "below a line, here the scale's middle, 4: 4 above and 1 below for "
                  "the five, 5 above and 1 below for the six."),
            ("p", "That shift is a formula, and it is the whole of the authors' "
                  "argument in miniature. Adding one respondent with score s to "
                  "a group whose mean is m, for a group of n including the new "
                  "one, moves the mean by (s − m) / n. Here that is (5.5 − 4.85) / 6, "
                  "which is 0.108. The preset <code>eleven-respondents</code> repeats "
                  "the five answer patterns twice, ten honest respondents, and adds "
                  "<code>r6</code>: the mean is 54 / 11, about 4.91, and the shift is "
                  "(5.5 − 4.85) / 11, about 0.059. The repeated patterns are "
                  "invented to show dilution and say nothing about real surveys. A "
                  "log with one number that the business reads has n equal to 1, and "
                  "the one entry decides."),
            ("p", "The lab also shows why a reverse-coded item raises the bar a "
                  "little. A respondent who agrees with all three positive items "
                  "should disagree with the fourth, and the five others do: their "
                  "fourth answers are 2, 3, 4, 2 and 5 against high and low answers "
                  "elsewhere. <code>r6</code> gives 7 to the reverse-worded item too, "
                  "so the score tops out at 5.5, not 7. Read that as a prompt to look "
                  "at the answers, not as proof of anything: a hurried respondent "
                  "straight-lines honestly, and a deliberate liar who reads every "
                  "item can answer 7, 7, 7 and 1. The authors do not rely on this "
                  "device. They rely on numbers, anonymity and many items, and "
                  "the pooled estimate does not reach a bias shared by many "
                  "respondents, such as being told to answer well. Appendix C's "
                  "tests for bias, read in Tests for Bias, address that."),
            ("p", "The fifth reason is that some things can only be measured by asking. "
                  "Culture is the authors' example. Teams want a faster measure than a "
                  "survey, from HR systems, and turnover is the usual stand-in: low "
                  "turnover for a good culture, high for a bad one. The authors give "
                  "reasons it fails. A leaver may have taken a much better-paid offer; "
                  "followed a partner who relocated; or left for a different career or "
                  "for study. One of the authors knows a person who left a supportive "
                  "team because that team's encouragement gave him the confidence to "
                  "change career, so strong culture produced turnover. And the "
                  "measure can be gamed: a manager who learns an employee is looking "
                  "may lay them off to keep them out of the turnover figure, and a "
                  "manager rewarded for retention may block transfers."),
            ("p", "Turnover, the authors grant, can be useful if one is careful about "
                  "what it measures. Other proxies exist, such as network traffic "
                  "to see who talks to whom, or semantic analysis of email and "
                  "chat. But to learn how people feel about taking risks, about sharing "
                  "information and about working across boundaries, and why they "
                  "behave as they do, you have to ask, and a survey is the way to ask "
                  "systematically, reliably and comparably over time. The chapter "
                  "closes by noting that it is worth asking: it cites research that "
                  "organizational culture predicts technology and organizational "
                  "performance, and credits Google's 2015 study with finding team "
                  "dynamics and psychological safety to matter most for how a team "
                  "performs."),
            ("h3", "Exercise"),
            ("ul", [
                "Four items on a seven-point scale; the fourth is reverse-coded.",
                "Five respondents' answers, `respondent, a1, a2, a3, a4`: `s1, 6, 6, 5, 2; "
                "s2, 5, 5, 5, 3; s3, 7, 6, 6, 1; s4, 4, 4, 5, 4; s5, 1, 1, 1, 1`.",
            ]),
            ("p", "Score each respondent by hand, turning the fourth answer round, and "
                  "take the construct's mean over all five. Then take it over "
                  "<code>s1</code> to <code>s4</code> alone, and use (s − m) / n to "
                  "check the difference. Type the records into the lab to confirm. "
                  "Say what <code>s5</code>'s raw answers would have scored if the "
                  "fourth item had not been reverse-coded."),
            ("p", "The authors' case for asking is made. The next question is whom they "
                  "asked, and the next lesson, The Data for the Project, reads "
                  "Chapter 15 on how the sample was reached."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "score",
            "preset": "five-respondents",
            "presets": [
                {"id": "five-respondents",
                 "label": "Five consistent respondents on one four-item construct",
                 "points": "7",
                 "items": FOUR_ITEMS,
                 "answers": FIVE_HONEST,
                 "expect": {"alkN": "5", "alkConstructs": "ownership 4.85", "alkUnreversed": "ownership 4.45"}},
                {"id": "six-respondents",
                 "label": "The same five and one respondent who answers 7 to every item",
                 "points": "7",
                 "items": FOUR_ITEMS,
                 "answers": SIX_WITH_STRAIGHT,
                 "expect": {"alkN": "6", "alkConstructs": "ownership 119/24 ≈ 4.958", "alkUnreversed": "ownership 4.875"}},
                {"id": "eleven-respondents",
                 "label": "The five patterns twice, and the same straight-lining respondent",
                 "points": "7",
                 "items": FOUR_ITEMS,
                 "answers": ELEVEN_WITH_STRAIGHT,
                 "expect": {"alkN": "11", "alkConstructs": "ownership 54/11 ≈ 4.909", "alkUnreversed": "ownership 103/22 ≈ 4.682"}},
            ],
            "panel_title": "A construct's mean with and without one suspect respondent",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Weighing one respondent",
        "steps_intro": "Five steps, the last of them on a survey of your own.",
        "steps": [
            ("Turn the reverse-coded items round",
             "For each reverse-worded item, replace the answer with the scale's top "
             "plus one, minus the answer: on a seven-point scale, 8 minus the answer."),
            ("Score each respondent",
             "Take the mean of a respondent's item scores. The construct's mean is "
             "the mean of the respondents' scores."),
            ("Recompute without the respondent you doubt",
             "Remove their row, rerun, and subtract: the difference is their weight "
             "in the mean."),
            ("Check the difference with (s − m) / n",
             "Their score minus the others' mean, over the group size n including "
             "them. The two answers should agree to the digits shown."),
            ("Look at your own responses",
             "Take a short survey your team ran. Count the respondents who gave one "
             "answer to every item, and recompute the mean without them. Write "
             "down the difference and the group size."),
        ],
        "worked": {
            "title": "The weight of r6, by hand",
            "intro": [
                "Score the six respondents of <code>six-respondents</code>, item four "
                "turned round.",
            ],
            "lines": [
                "r1: 6 5 6 and 8 − 2 = 6, sum 23, mean 5.75",
                "r2: 5 5 6 and 8 − 3 = 5, sum 21, mean 5.25",
                "r3: 4 5 4 and 8 − 4 = 4, sum 17, mean 4.25",
                "r4: 6 6 5 and 8 − 2 = 6, sum 23, mean 5.75",
                "r5: 3 4 3 and 8 − 5 = 3, sum 13, mean 3.25",
                "r6: 7 7 7 and 8 − 7 = 1, sum 22, mean 5.5",
                "five without r6: 24.25 / 5 = 4.85",
                "six with r6: 29.75 / 6 = 4.958",
                "shift: (5.5 − 4.85) / 6 = 0.108",
            ],
            "after": [
                "Every figure is a sum or a mean of numbers on the page. The lab's "
                "tiles agree with them; the small difference between 4.958 and the "
                "4.96 in the prose is rounding.",
            ],
        },
        "quiz_title": "Trust, weight and proxies",
        "quiz": [
            {"q": "In the exercise, what is the construct's mean over all five "
                  "respondents, with the fourth item turned round?",
             "a": ["5.375, over s1 to s4 alone",
                   "3.9, leaving the fourth item as it was typed",
                   "2.5, the score of s5",
                   "4.8"],
             "c": 3,
             "why": "The scores are 5.75, 5, 6.5, 4.25 and 2.5, which sum to 24, and "
                    "24 / 5 = 4.8. The 5.375 is the mean without s5. The 3.9 comes from "
                    "using the raw answers, which treats the reverse-worded item as if "
                    "it pointed the same way. The 2.5 is one respondent's own score."},
            {"q": "What do the authors say it would take for lying respondents to make "
                  "a noticeable difference to their pooled data of over 23,000?",
             "a": ["Several hundred lying in a coordinated way, on every item of a "
                   "construct, to the same degree and in the same direction",
                   "One respondent lying on a single item",
                   "More than half of all respondents lying on any one item",
                   "No number: pooled survey data cannot be moved by lying"],
             "c": 0,
             "why": "That is the chapter's estimate. One respondent does move a mean, as "
                    "the lab shows, by (s − m) / n, which is tiny for a big n. The "
                    "authors do not say half are needed, and they do not say lying "
                    "is impossible; they say the effort required is large."},
            {"q": "On a seven-point scale, a respondent answers 7 to a reverse-coded "
                  "item. What does that answer count as when the construct is scored?",
             "a": ["7", "6", "1", "0"],
             "c": 2,
             "why": "The turned-round score is 8 minus the answer, so 8 − 7 = 1. Using 0 "
                    "or 6 are off-by-one errors, from taking 7 minus the answer; "
                    "that rule sends the scale's top to 0 and the bottom to 6, which "
                    "is not a seven-point scale. Leaving 7 as typed is the error the "
                    "lab's un-reversed score shows."},
            {"q": "Which is one of the authors' reasons that turnover is a poor "
                  "stand-in for culture?",
             "a": ["HR systems do not record who leaves",
                   "A strong team culture can itself lead someone to leave, for a "
                   "different career",
                   "Turnover is always caused by pay, never by culture",
                   "Turnover cannot be gamed by managers"],
             "c": 1,
             "why": "The authors know a case of an employee who left a supportive team "
                    "because it encouraged him to change career, so strong culture "
                    "produced turnover. They do not say HR systems lack the data, "
                    "they say pay is one reason among several, and they describe two "
                    "ways managers can game it."},
        ],
        "mistakes": [
            ("Thinking logs cannot lie and surveys can",
             "The authors ask which is more exposed. A log is shaped by people, so "
             "one bad actor or one uncaught mistake can distort the few numbers the "
             "business reads, for a long time. A survey's pooled answers are moved "
             "by a liar in proportion to one over n; the lab's 0.108 for six "
             "respondents and 0.059 for eleven fall as the group grows. Neither "
             "source is immune, and the claim is about how much each can be moved."),
            ("Believing a large pool cancels every bias",
             "The pooled estimate is about coordinated lying by a few hundred. It "
             "does not address an error that many respondents share, such as being "
             "told to answer positively, which the chapter's footnote warns "
             "against. That is why Appendix C runs tests for bias between early and "
             "late responders and for common method bias, and why the authors "
             "describe the survey as giving a reasonable assurance, not proof."),
            ("Using turnover as an objective measure of culture",
             "Turnover is easy to collect and feels free of opinion, which makes it "
             "attractive. The chapter shows it can fall or rise for reasons that have "
             "nothing to do with culture, and for a reason that runs the other "
             "way, and that it is open to being gamed. What people feel about risk, "
             "information and the work environment has to be asked."),
        ],
        "standard": (
            "Finish when you can weigh one respondent.",
            "Given a construct with a reverse-coded item and a set of answers, score "
            "each respondent, compute the construct's mean with and without a "
            "respondent you doubt, and check the difference with (s − m) / n."
        ),
        "note": (
            "The lab compares two means. It cannot tell whether a respondent lied, "
            "hurried or meant it; the pattern is a reason to look, not a finding. And "
            "the dilution it shows is for one respondent, not for a bias many "
            "respondents share."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 15 all (PDF pp. 209-216), and the Part III introduction on pp.
    # 217-218: target population and cross-sectional design, 2014 for four years
    # (p. 209); two reasons for the target and the trade-off (pp. 209-211);
    # probability and nonprobability sampling, mailing lists and social media
    # (pp. 211-213); why snowball sampling suits (pp. 213-214); three
    # limitations and countermeasures (pp. 214-215); footnotes on cross-
    # sectional design and probability sampling (pp. 215-216).
    # Quote: PDF p. 214 of the operator's copy, 17 words, quotes.py OK.
    # Lesson total: 17 words.
    {
        "slug": "the-data-for-the-project",
        "title": "The Data for the Project",
        "module": "Chapter 15 · The Data for the Project",
        "one_line": "With no list of the people who build and run software, the authors invited the people they could reach and asked each to refer others; the chapter says what that buys and what it costs.",
        "summary": (
            "Chapter 15 describes the target population, why random sampling was "
            "impossible, why snowball sampling fitted, and the three limitations "
            "the authors name with their remedies. Read it as the answer to who was "
            "asked, then follow twenty invented people from their seeds, and see "
            "what a missing seed would have left out."
        ),
        "key": [
            "target the people who know the terms",
            "no list means no random sample",
            "snowball: invite, then ask for referrals",
            "the first invitations shape the sample",
            "many diverse seeds, not just a large sample",
            "a share of the sample is not a share of all",
        ],
        "key_label": "The data for the project in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Snowball sampling",
             "Also called referral sampling: a method in which the first people "
             "invited are asked to pass the invitation on, so that the sample grows "
             "as it spreads. It is a nonprobability method, because not everyone in "
             "the population has a known chance of being asked."),
            ("Probability sampling",
             "Any method of drawing a sample by random selection, so that every member "
             "of the population has an equal chance of being chosen. The authors say "
             "it is generally preferred and was impossible here, because it needs "
             "a list of the whole population and there is no list."),
            ("Seed and wave",
             "A seed is a person invited directly. Wave 0 is the seeds; wave 1 is "
             "those a seed referred, wave 2 those a wave-1 person referred, and so "
             "on. The lab counts a person's tree as the seed they descend from."),
        ],
        "read_title": "Who was asked, then the count",
        "read_intro": (
            "Read Chapter 15 in your own copy first; it is short. The lesson sets out "
            "the research design and the case for snowball sampling, then follows an "
            "invented sample through its waves."
        ),
        "body": [
            ("p", "&ldquo;Snowball sampling is a method well suited for studying specific "
                  "groups whose populations cannot be easily identified.&rdquo; "
                  "Forsgren, Humble and Kim write that in Chapter 15, The Data for "
                  "the Project, which answers the question Chapter 14 left open: "
                  "whom the survey asked. This lesson reads the whole chapter, and "
                  "points at the two pages of Part III's introduction that follow it."),
            ("p", "The research began in 2014 and collected data in a cross-sectional "
                  "design, a single point in time each year, for four years. The "
                  "target population was people and organizations that knew the "
                  "word DevOps, or would at least open an invitation that "
                  "used it. The authors give two reasons: it let them focus on people in "
                  "the business of developing and delivering software, in any industry "
                  "that is driven by technology, and on people who already knew "
                  "terms such as continuous integration, so that a survey did not "
                  "spend its length on definitions that could make a respondent "
                  "give up."),
            ("p", "The chapter states the trade-off. The group not surveyed, people "
                  "unfamiliar with these practices, probably performs worse than the "
                  "authors' lowest performers, so their comparisons are limited and "
                  "do not show how large a change could be. In return they gain "
                  "explanatory power by defining the population tightly. The "
                  "familiarity also called for care in wording: they never asked "
                  "whether a team practiced continuous integration, a claim "
                  "respondents might make to look good, but asked about the "
                  "practices at its core, such as whether automated tests run when "
                  "code is checked in. The authors believe many findings apply "
                  "beyond this population, on prior research and experience; that is "
                  "their belief, and the sample cannot test it."),
            ("p", "Next, the sampling method. Probability sampling needs every member of "
                  "the population to be known and to have an equal chance of "
                  "being asked, and no exhaustive list of the world's DevOps "
                  "professionals exists. So the authors invited by email, to their "
                  "own mailing lists, which included past respondents and people from "
                  "the marketing databases of Puppet and of two of the authors, and "
                  "to the mailing lists of professional groups, with particular care "
                  "to reach groups of underrepresented people in technology. They "
                  "also posted on social media. Then they asked recipients to "
                  "refer others."),
            ("p", "That last step is snowball sampling, and the chapter gives two "
                  "reasons it fitted. First, the population is hard or impossible to "
                  "identify: unlike accountancy or civil engineering, software work "
                  "has no certifying body with a list, job titles vary or are too "
                  "generic to select on, and early on many held nontraditional titles. "
                  "Second, the population is often averse to being studied, after a "
                  "history of studies of technical workers that led to cuts in the "
                  "workforce, so a referral lets a colleague vouch for the questions "
                  "and the researchers."),
            ("p", "The chapter then names three limitations and what the authors did. "
                  "The first is that the people invited first may not represent their "
                  "communities, and the remedy was an initial set as large and "
                  "diverse as possible, combining several lists. The second is that "
                  "the sample is strongly influenced by the initial invitations, a "
                  "concern if a small group is targeted and the sample grows from "
                  "it, and the remedy was again a very large and diverse set. The "
                  "third is that findings may not represent the industry, and the "
                  "remedies were to engage the community and compare notes, to have "
                  "outside experts review the hypotheses each year, to read the "
                  "literature, and to ask for input. A footnote adds a limit of "
                  "the design: because responses are not linked from year to year, "
                  "the data cannot be analysed longitudinally, and the authors say "
                  "they are pursuing that. The lesson Inferential Predictive "
                  "Analysis returns to what this means for claims of cause."),
            ("p", "Now the count, on twenty invented people. The lab's snowball view "
                  "takes a list of people, who referred each, and the community each "
                  "belongs to, here where they work. A person with no referrer is a "
                  "seed. The preset <code>three-seeds</code> has three seeds: "
                  "<code>ana</code> from retail, <code>bo</code> from a bank and "
                  "<code>cy</code> from health. The lab counts 3, 6, 8 and 3 people in "
                  "waves 0 to 3, 20 in all. Ana's tree holds 8 of the 20, 40 percent; "
                  "Bo's holds 9, 45 percent; Cy's holds 3, 15 percent. By community the "
                  "sample is 6 retail, 2 startup, 9 bank and 3 health, which is 30, 10, "
                  "45 and 15 percent."),
            ("p", "The preset <code>six-seeds</code> invites six people across the same "
                  "four communities, again 20 people in all. The waves count 6, 8, 5 "
                  "and 1; no seed's tree holds more than 5, a quarter; and the "
                  "community shares are 5 retail, 5 bank, 6 health and 4 startup, "
                  "which is 25, 25, 30 and 20 percent. The sample sizes are equal "
                  "and the pictures are not. This is the second limitation made "
                  "visible, and the authors' remedy, more and more varied "
                  "invitations, is what changed it, not the size of the sample."),
            ("p", "The preset <code>without-cy</code> is <code>three-seeds</code> with "
                  "the seed <code>cy</code> dropped, as if the health community's "
                  "mailing list had never been used. The lab counts the people lost, "
                  "<code>cy</code>, <code>ida</code> and <code>quin</code>, leaving 17, "
                  "and the community with no one left, health. The shares change "
                  "because the denominator does: bank rises from 45 to 52.9 "
                  "percent, retail from 30 to 35.3 percent and startup from 10 to 11.8 "
                  "percent, although no bank, retail or startup person was added."),
            ("p", "Read the counts as the authors would, as a reason for caution. The "
                  "shares are shares of the sample. The population has no list, so "
                  "nobody can say what the shares of the whole would be, and the lab "
                  "cannot either; it also records only those who were reached and "
                  "answered, not those who were asked and did not. Whether a "
                  "sample resembles a population is something the design argues for, as "
                  "the chapter does, and does not prove."),
            ("h3", "Exercise"),
            ("ul", [
                "Eight people, as `person, referred_by, group` with `-` for a seed: "
                "`a, -, east; b, -, west; c, a, east; d, a, east; e, b, west; f, c, east; "
                "g, c, east; h, e, west`.",
            ]),
            ("p", "By hand, count the people in each wave, the share of the sample "
                  "in each seed's tree and the share in each group. Then drop seed "
                  "<code>b</code> and recount the sample and the group shares. Type the "
                  "records into the lab to check. Say what happened to the west group."),
            ("p", "The authors name their sample's limits and their remedies. Before "
                  "any analysis they also test for bias in what they collected, the "
                  "subject of the next lesson, Tests for Bias. Chapter 16, which follows "
                  "this chapter's Part III introduction, is by Steve Bell and Karen "
                  "Whitley Bell, and is read in the next course."),
        ],
        "lab": ("acckit", {
            "mode": "sample",
            "view": "snowball",
            "preset": "three-seeds",
            "presets": [
                {"id": "three-seeds",
                 "label": "Twenty people reached from three seeds",
                 "people": THREE_SEEDS,
                 "expect": {"asnSeeds": "3: ana, bo, cy", "asnWaves": "wave 0: 3; wave 1: 6; wave 2: 8; wave 3: 3", "asnSize": "20", "asnTrees": "ana 8 of 20 = 40%; bo 9 of 20 = 45%; cy 3 of 20 = 15%", "asnGroups": "retail 6 of 20 = 30%; bank 9 of 20 = 45%; health 3 of 20 = 15%; startup 2 of 20 = 10%", "asnLost": "no seed dropped", "asnAfter": "no seed dropped"}},
                {"id": "six-seeds",
                 "label": "Twenty people reached from six seeds across the same communities",
                 "people": SIX_SEEDS,
                 "expect": {"asnSeeds": "6: uma, vic, wes, xia, yan, zoe", "asnWaves": "wave 0: 6; wave 1: 8; wave 2: 5; wave 3: 1", "asnSize": "20", "asnTrees": "uma 2 of 20 = 10%; vic 5 of 20 = 25%; wes 3 of 20 = 15%; xia 4 of 20 = 20%; yan 3 of 20 = 15%; zoe 3 of 20 = 15%", "asnGroups": "retail 5 of 20 = 25%; bank 5 of 20 = 25%; health 6 of 20 = 30%; startup 4 of 20 = 20%", "asnLost": "no seed dropped", "asnAfter": "no seed dropped"}},
                {"id": "without-cy",
                 "label": "The first sample with the health seed never invited",
                 "people": THREE_SEEDS,
                 "drop": "cy",
                 "expect": {"asnSeeds": "3: ana, bo, cy", "asnWaves": "wave 0: 3; wave 1: 6; wave 2: 8; wave 3: 3", "asnSize": "20", "asnTrees": "ana 8 of 20 = 40%; bo 9 of 20 = 45%; cy 3 of 20 = 15%", "asnGroups": "retail 6 of 20 = 30%; bank 9 of 20 = 45%; health 3 of 20 = 15%; startup 2 of 20 = 10%", "asnLost": "3: cy, ida, quin", "asnAfter": "retail 6 of 17 ≈ 35.3%; bank 9 of 17 ≈ 52.9%; health 0 of 17 = 0%; startup 2 of 17 ≈ 11.8%"}},
            ],
            "panel_title": "Who a snowball reaches from its seeds",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Following a snowball sample",
        "steps_intro": "Four steps, the last of them on a sample of your own.",
        "steps": [
            ("Mark the seeds",
             "Find everyone with no referrer. They are wave 0; each later wave is the "
             "people referred by the wave before."),
            ("Count each seed's tree",
             "Follow referrals down from each seed and count the people, the seed "
             "included. Divide by the sample size for the seed's share."),
            ("Count the communities",
             "Tally the group of each person and divide by the sample size. Compare "
             "the tallies with the seeds' shares."),
            ("Drop a seed and recount",
             "Remove one seed and everyone it reached, then recount the sample "
             "and the communities. List the communities that vanish and the ones "
             "whose shares rise."),
        ],
        "worked": {
            "title": "The trees and shares of three-seeds",
            "intro": [
                "Follow the referrals in <code>three-seeds</code>.",
            ],
            "lines": [
                "ana: dee eli fay, then jon kim lee, then ray",
                "ana's tree: 1 + 3 + 3 + 1 = 8, 8 / 20 = 40 percent",
                "bo: gus hal, then max ned oli pam, then sue tom",
                "bo's tree: 1 + 2 + 4 + 2 = 9, 9 / 20 = 45 percent",
                "cy: ida, then quin; tree 1 + 1 + 1 = 3, 15 percent",
                "waves: 3 seeds, 6, 8, 3: total 20",
                "drop cy: 20 − 3 = 17; bank 9 / 17 = 52.9 percent",
            ],
            "after": [
                "The three trees partition the sample: 8 + 9 + 3 = 20, so the shares add "
                "to 100 percent. Dropping a seed removes its whole tree, including "
                "people who might have been reached another way; the lab counts "
                "only the referrals it is given.",
            ],
        },
        "quiz_title": "Who was asked, and how",
        "quiz": [
            {"q": "In the exercise, what share of the eight-person sample is reached "
                  "through seed a?",
             "a": ["50 percent, since a is one of two seeds",
                   "37.5 percent",
                   "62.5 percent",
                   "25 percent"],
             "c": 2,
             "why": "Seed a's tree is a, c, d, f and g, five of the eight, 62.5 percent. "
                    "The 37.5 percent is seed b's tree, b, e and h. Seeds are counted "
                    "as people, and a's tree is larger, so splitting 50 and 50 "
                    "by seed does not match the sample. The 25 percent is the share "
                    "of the sample who are seeds, two of eight."},
            {"q": "In the exercise, e and h are reached only through seed b. If b is "
                  "never invited, what share of the remaining sample is in the west "
                  "group?",
             "a": ["37.5 percent, as before",
                   "0 percent",
                   "12.5 percent",
                   "100 percent"],
             "c": 1,
             "why": "Dropping b removes b, e and h, the whole west group, leaving a, c, "
                    "d, f and g, all east: the west is 0 percent and the east 100 "
                    "percent of five. A group with no seed in it can vanish from the "
                    "sample, which is the chapter's second limitation."},
            {"q": "Which is one of the chapter's reasons that snowball sampling "
                  "suited its study?",
             "a": ["It gives every professional an equal chance of being chosen",
                   "It lets the researchers state a margin of error for the whole "
                   "industry",
                   "It guarantees that the first invitations do not affect "
                   "the sample",
                   "The population is hard to identify, since there is no list or "
                   "certifying body"],
             "c": 3,
             "why": "The authors say the population cannot easily be identified. Equal "
                    "chance for every professional defines probability sampling, "
                    "which they could not use. A margin of error for the whole "
                    "industry needs a probability sample. And they say the data "
                    "are strongly influenced by the first invitations, so no "
                    "guarantee is claimed."},
            {"q": "How did the authors say they countered the risk that the people "
                  "invited first were not representative of their communities?",
             "a": ["With an initial set of invitations as large and diverse as "
                   "possible, from several lists",
                   "By inviting only the most senior people, who could vouch for "
                   "others",
                   "By stopping each chain after the first referral",
                   "By discarding respondents who were referred by someone else"],
             "c": 0,
             "why": "The chapter says they combined several mailing lists, including their "
                    "own survey list, and reached out to underrepresented groups. "
                    "Chains were allowed to grow, referred respondents were kept, "
                    "and no seniority rule is mentioned."},
        ],
        "mistakes": [
            ("Treating a large snowball sample as a random sample of the industry",
             "Random selection needs a list of everyone, and the chapter says none "
             "exists. The more than 23,000 responses are a large nonprobability sample. "
             "Its size makes its means precise about the people reached and says "
             "nothing about the people never reached. The authors argue "
             "for the sample's reach, and the foreword says Fowler would have more "
             "confidence once other teams, using different approaches, confirm "
             "the reasoning."),
            ("Believing a big sample makes the first invitations irrelevant",
             "The authors name this limitation: the data are strongly influenced by "
             "the initial invitations. The lab's two presets have the same size and "
             "different pictures, with one seed's tree holding 45 percent in one "
             "and no more than 25 percent in the other. The remedy the chapter gives "
             "is a very large and diverse set of first invitations."),
            ("Reading the targeted population as something the authors hid",
             "The chapter states it openly as a design decision, with its cost: the "
             "sample omits people likely to perform worse than the low performers, "
             "which limits the comparisons. The authors call it a strength for "
             "explanatory power and also say they believe many findings apply more "
             "widely. A reader may weigh the two differently; the lesson does not "
             "settle it."),
        ],
        "standard": (
            "Finish when you can follow a snowball sample from its seeds.",
            "Given a list of people and who referred each, count the people in each "
            "wave, the share of the sample in each seed's tree and in each group, "
            "and say what a missing seed leaves out."
        ),
        "note": (
            "The lab counts the sample you give it. It cannot tell who was asked and "
            "did not answer, or what the population's shares are; with no list, "
            "nobody can. The chapter's remedies are arguments about reach, not "
            "calculations."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Appendix C, Survey Preparation, Data Collection, Tests for Bias (PDF pp.
    # 266-268): previously validated items and Dillman 1978 (p. 266), snowball
    # sampling (p. 267), chi-square tests, t-tests, common method bias with
    # Harman's single-factor test and the marker variable test (pp. 267-268),
    # no bias seen (p. 268). Chapter 14, PDF p. 199-200: early and late
    # responders.
    # Quote: PDF p. 268 of the operator's copy, 10 words, quotes.py OK.
    # Lesson total: 10 words.
    {
        "slug": "tests-for-bias",
        "title": "Tests for Bias",
        "module": "Appendix C · Statistical Methods Used in Our Research",
        "one_line": "Before the authors analyse the data they test it for bias, comparing people who answered early with people who answered late, and checking that the survey's method is not producing the pattern.",
        "summary": (
            "Appendix C is a reference, and it opens its tests with bias. Read its "
            "survey preparation, its data collection and its three families of bias "
            "tests, then compute a chi-square statistic for early and late "
            "respondents by hand and in the lab, and compare it with a critical "
            "value the lesson states."
        ),
        "key": [
            "test for bias before any analysis",
            "chi square for categories, t test for scales",
            "expected count: row times column over total",
            "chi square: sum of gap squared over expected",
            "compare with a critical value, not a verdict",
        ],
        "key_label": "Tests for bias in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the appendix's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Early and late responders",
             "The people who answered soon after the invitation and those who "
             "answered after a reminder or later. The authors compare the two on "
             "what they can measure, to see whether the order of answering goes with "
             "a difference in the answers."),
            ("Common method bias",
             "A pattern in the data that comes from the way the data were collected, "
             "such as everything being asked in one survey, and not from the things "
             "asked about. The appendix names two tests for it, Harman's "
             "single-factor test and the marker variable test."),
            ("Critical value",
             "The size the chi-square statistic must exceed, for a table of a given "
             "shape and a chosen level of chance, before the lab says the groups "
             "differ by more than chance usually produces. The lesson states its "
             "own; the book gives none for these tests."),
        ],
        "read_title": "The appendix's order of work, then the count",
        "read_intro": (
            "Read Appendix C from its opening to the end of Tests for Bias in your "
            "own copy first; it is two pages. The lesson sets out what each test "
            "asks and works one by hand."
        ),
        "body": [
            ("p", "&ldquo;We did not see bias between early and late responders.&rdquo; That is "
                  "the result Forsgren, Humble and Kim report in Appendix C, "
                  "Statistical Methods Used in Our Research, and the lesson reads the "
                  "sections that lead to it: Survey Preparation, Data Collection and "
                  "Tests for Bias. The appendix describes itself as a brief reference "
                  "to the methods, not a statistics text, and follows the authors' "
                  "path from research design to analysis."),
            ("p", "Survey preparation comes first. Each year the authors fix the "
                  "constructs and hypotheses they will test, from the literature, their "
                  "own earlier findings and debate, and then design the survey. Where "
                  "they can, they use items that other researchers have already "
                  "validated, for example for organizational performance and for "
                  "noncommercial performance; items of their own follow commonly "
                  "accepted procedures from Dillman's 1978 work. Data collection is "
                  "snowball sampling, which Chapter 15 defends and the last lesson "
                  "read."),
            ("p", "The first analysis, once there are data, is a test for bias, and the "
                  "appendix names three families. Chi-square tests check for "
                  "differences in variables that take only categorical values, such as "
                  "gender. T-tests check for differences in variables that take scale "
                  "values, such as Likert answers, and the authors used them to "
                  "compare early and late responders. Common method bias is checked "
                  "with two tests. Harman's single-factor test looks to see whether one "
                  "factor loads significantly on all the items, which would suggest "
                  "the method and not the constructs is behind the pattern. The "
                  "marker variable test adjusts the correlations between constructs "
                  "by the second-lowest positive correlation among them, and asks "
                  "whether the correlations that were significant before still "
                  "are. The result was no bias between early and late responders and "
                  "no sign that common method bias is a problem in these samples."),
            ("p", "The reasoning behind the early and late comparison is the usual one "
                  "in survey methods and the appendix does not spell it out. People "
                  "who answer late are, a little, more like the people who never "
                  "answered. If early and late respondents give the same picture, the "
                  "missing respondents are less likely to change it. The check "
                  "has limits, since it cannot see the people who were never reached "
                  "or never answered, and a snowball sample is not drawn at random "
                  "to begin with."),
            ("p", "The chi-square test is arithmetic you can do. Take a table of counts, "
                  "with a row for each category of an answer and a column each for "
                  "early and late respondents. If the order of answering had nothing "
                  "to do with the category, each cell's expected count would be its "
                  "row's total times its column's total, over the grand total N. The "
                  "statistic adds up, over every cell, the squared gap between the "
                  "observed count O and the expected count E, divided by E. The "
                  "degrees of freedom of a table are its rows minus one, times its "
                  "columns minus one."),
            ("math", [
                "E = (row total · column total) / N",
                "χ² = sum over the cells of (O − E)² / E",
                "degrees of freedom = (rows − 1) · (columns − 1)",
            ]),
            ("p", "A statistic is read against a critical value for its degrees of "
                  "freedom. The lesson states a level of 0.05, which is its own choice "
                  "and not the book's, and the values for it: 3.841 for 1 degree of "
                  "freedom and 5.991 for 2. A statistic above the critical value means "
                  "that if early and late respondents had come from one population "
                  "with the same mix, a statistic that large would arise in fewer than "
                  "5 samples in 100. It is a yardstick for a gap, not a cause for "
                  "it, and it assumes the groups behave like random draws. The lab "
                  "prints no p-value."),
            ("p", "Now the count, on invented respondents. The lab's bias view takes "
                  "a table of counts by category, early and late, and the critical "
                  "value. The answer is the size of the respondent's organization, a "
                  "categorical answer. On the preset <code>no-difference</code> there "
                  "are 60 early and 40 late respondents, 30 small, 50 medium and 20 "
                  "large organizations. The expected counts are 18 and 12 for small, "
                  "30 and 20 for medium, 12 and 8 for large. The statistic is "
                  "1/18 + 1/12 + 1/30 + 1/20 + 0 + 0, which is 2/9, about 0.222, with "
                  "2 degrees of freedom; it is not above 5.991."),
            ("p", "The preset <code>difference</code> keeps the same totals and the same "
                  "expected counts and moves the observed counts: small 12 early and "
                  "18 late, medium 30 and 20, large 18 and 2. The terms are 2, 3, 0, "
                  "0, 3 and 4.5, which sum to 12.5, above 5.991. The cell that "
                  "contributes most is large, late: 2 observed against 8 expected. "
                  "That is a reason to ask whether late respondents come from "
                  "smaller organizations. It does not say why, and it does not say "
                  "that either group is wrong."),
            ("p", "The preset <code>small-late-group</code> is a two-by-two table of "
                  "40 respondents who do or do not use a hotfix path: 9 early and 1 "
                  "late for yes, 21 and 9 for no. The expected counts are 7.5, 2.5, "
                  "22.5 and 7.5, the statistic is 0.3 + 0.9 + 0.1 + 0.3, or 1.6, with "
                  "1 degree of freedom, below 3.841. One expected count, 2.5, is under "
                  "5, and the lab flags it. Statistics texts give a rule of thumb, "
                  "not the book's, that the chi-square approximation is unreliable "
                  "when expected counts are that small, so the lab does not treat 1.6 "
                  "as a verdict."),
            ("p", "Read the figures the way the authors do, as a screen before the "
                  "analysis. A statistic below the critical value is the absence of "
                  "a detected difference on that variable in that sample, and not proof "
                  "that there is no bias. The appendix reports what the authors saw, "
                  "and a reader can weigh it with the foreword's caution about "
                  "the sample."),
            ("h3", "Exercise"),
            ("ul", [
                "A table of 80 respondents, `category, early, late`: `yes, 30, 10; "
                "no, 20, 20`. The answer is whether the team deploys from a pipeline.",
                "The critical value for this table, at the lesson's 0.05, is 3.841.",
            ]),
            ("p", "By hand, find the four expected counts, the statistic and the "
                  "degrees of freedom, and say whether the statistic is above 3.841. "
                  "Then type the table into the lab and compare. Say which cell "
                  "contributes least to the statistic."),
            ("p", "Bias is only the first screen. Once it is passed, the authors test "
                  "whether their measures are valid and reliable, and the next lesson, "
                  "Tests of the Measurement Model, computes those."),
        ],
        "lab": ("acckit", {
            "mode": "groups",
            "view": "bias",
            "preset": "no-difference",
            "presets": [
                {"id": "no-difference",
                 "label": "Early and late respondents with nearly the same mix of sizes",
                 "table": SIZE_NO_DIFFERENCE,
                 "critical": "5.991",
                 "expect": {"agrChi": "2/9 ≈ 0.222", "agrDf": "2", "agrExceeds": "no: 0.222 is not above 5.991, the critical value stated", "agrSmall": "0: none"}},
                {"id": "difference",
                 "label": "The same totals with late respondents from smaller organizations",
                 "table": SIZE_DIFFERENCE,
                 "critical": "5.991",
                 "expect": {"agrChi": "25/2 = 12.500", "agrDf": "2", "agrExceeds": "yes: 12.500 is above 5.991, the critical value stated", "agrSmall": "0: none"}},
                {"id": "small-late-group",
                 "label": "A two-by-two table with one small expected count",
                 "table": HOTFIX_SMALL,
                 "critical": "3.841",
                 "expect": {"agrChi": "8/5 = 1.600", "agrDf": "1", "agrExceeds": "no: 1.600 is not above 3.841, the critical value stated", "agrSmall": "1: yes late (expected 2.5)"}},
            ],
            "panel_title": "Early against late respondents: a chi-square statistic",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Testing early against late",
        "steps_intro": "Five steps, the last of them on a survey of your own.",
        "steps": [
            ("Tabulate the answer",
             "Count the respondents in each category of one categorical answer, "
             "separately for those who answered early and those who answered late."),
            ("Find the expected counts",
             "For each cell, multiply its row total by its column total and divide by "
             "the grand total."),
            ("Sum the gaps",
             "For each cell take observed minus expected, square it, divide by the "
             "expected count, and add up all the cells."),
            ("Compare with the critical value",
             "Take the degrees of freedom as rows minus one times columns minus one, "
             "and compare the sum with the critical value for it. Flag any expected "
             "count under 5."),
            ("Do it on a survey you ran",
             "Split a survey's respondents at the median time of answering, pick one "
             "categorical answer, and compute the statistic. Write down the cell "
             "that contributes most and what it would mean."),
        ],
        "worked": {
            "title": "The statistic for difference, cell by cell",
            "intro": [
                "Take <code>difference</code>, with 60 early and 40 late respondents.",
            ],
            "lines": [
                "row totals: small 30, medium 50, large 20; N = 100",
                "expected small: 30 · 60 / 100 = 18 early, 12 late",
                "expected medium: 30 early, 20 late",
                "expected large: 12 early, 8 late",
                "small early: gap 6, 6 squared = 36, 36 / 18 = 2",
                "small late: gap 6, 36 / 12 = 3",
                "medium: both gaps 0, terms 0 and 0",
                "large early: gap 6, 36 / 12 = 3",
                "large late: gap 6, 36 / 8 = 4.5",
                "sum 2 + 3 + 0 + 0 + 3 + 4.5 = 12.5; 12.5 > 5.991",
            ],
            "after": [
                "Each term is a gap squared over what was expected. Large organizations "
                "among late respondents give the largest term, 4.5. Degrees of "
                "freedom are (3 − 1) · (2 − 1) = 2.",
            ],
        },
        "quiz_title": "Expected counts, statistics and the appendix",
        "quiz": [
            {"q": "In the exercise, what is the chi-square statistic, and is it above "
                  "the critical value of 3.841 for 1 degree of freedom?",
             "a": ["2.0, which is below it",
                   "5.333, which is above it",
                   "5.333, which is below the critical value 5.991",
                   "2.667, which is below it"],
             "c": 1,
             "why": "The expected counts are 25, 15, 25 and 15, so the terms are 25/25 = 1, "
                    "25/15, 1 and 25/15; the sum is 2 + 10/3 = 16/3, about 5.333, above "
                    "3.841. The 2.0 leaves out the two late cells. The 5.991 is the "
                    "value for 2 degrees of freedom; a two-by-two table has (2 − 1) · "
                    "(2 − 1) = 1."},
            {"q": "According to Appendix C, which test checks early against late "
                  "responders on a variable that takes scale values, such as Likert "
                  "answers?",
             "a": ["Chi-square tests",
                   "Harman's single-factor test",
                   "T-tests",
                   "Tukey's test"],
             "c": 2,
             "why": "The appendix assigns t-tests to variables with scale values and uses "
                    "them for early against late responders. Chi-square is for "
                    "categorical values, Harman's test is one of the two checks for "
                    "common method bias, and Tukey's test belongs to the analysis of "
                    "variance used on clusters, later in the appendix."},
            {"q": "In the preset difference, what is the expected count for large "
                  "organizations among late respondents?",
             "a": ["2, the observed count",
                   "8",
                   "10, half of 20",
                   "12"],
             "c": 1,
             "why": "The row total for large is 20, the late total is 40 and N is 100, so "
                    "E = 20 · 40 / 100 = 8. The 2 is what was observed. Half of 20 "
                    "ignores that late respondents are 40 percent of the sample, "
                    "and the 12 is the expected count for early respondents, 20 · 60 / "
                    "100."},
            {"q": "On the preset difference the statistic is 12.5, above 5.991. Which "
                  "conclusion does that support?",
             "a": ["Early and late respondents differ in their mix of organization "
                   "sizes by more than chance would usually produce at the 0.05 level",
                   "Late respondents are less honest than early ones",
                   "The survey's results are invalid",
                   "The sample misrepresents the whole industry"],
             "c": 0,
             "why": "The test compares the two groups' mixes with what chance would "
                    "produce. It says nothing about honesty, and a difference on one "
                    "variable does not make a survey invalid; it is a reason to look. "
                    "Nor can it say how the whole industry compares, since it only "
                    "sees the people who answered."},
        ],
        "mistakes": [
            ("Reading a statistic below the critical value as proof of no bias",
             "The authors report that they did not see bias, which is what the tests "
             "showed on the variables they tested. The lab's <code>no-difference</code> "
             "preset gives about 0.222 against 5.991, and the preset "
             "<code>small-late-group</code> gives 1.6 against 3.841, with an expected "
             "count of 2.5 that makes the statistic unreliable. A test can fail to detect a "
             "difference that is there, particularly in small tables, and cannot see "
             "people who never answered."),
            ("Treating the early and late comparison as a test of honesty",
             "It compares the mix of two groups of respondents. A difference, as in "
             "<code>difference</code>, says that late respondents come from smaller "
             "organizations in this sample; it does not say that anyone misreported. "
             "The reason to look is that the people who answer late may resemble "
             "those who never answered."),
            ("Confusing the chi-square test with the t-test",
             "The appendix gives each a kind of variable: chi-square for categories "
             "such as gender or the size band of an organization, t-tests for scale "
             "values such as Likert answers. Both are tests for differences. Which "
             "one fits depends on what kind of answer was collected, not on the "
             "topic."),
        ],
        "standard": (
            "Finish when you can compute a chi-square statistic for early against late.",
            "Given a table of counts by category for early and late respondents, "
            "compute the expected counts, the statistic and the degrees of freedom, "
            "compare the statistic with a stated critical value, and flag small "
            "expected counts."
        ),
        "note": (
            "The lab compares a statistic with a critical value the lesson states, "
            "and prints no p-value. It treats the early and late groups as if they "
            "were random draws, which a snowball sample is not, and it cannot see "
            "the people who never answered."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Appendix C, Testing for Relationships and Tests of the Measurement Model
    # (PDF pp. 268-270): two stages (p. 268); principal components analysis
    # with varimax, EFA and CFA, loadings above 0.60 and no cross-loading (pp.
    # 268-269); AVE above 0.50 and its square root above the cross-diagonal
    # correlations (p. 269); correlations below 0.85 (p. 269); Cronbach's alpha
    # cutoff 0.70, biased against small scales (pp. 269-270); composite
    # reliability cutoff 0.70 (p. 270); all tests must pass (p. 270).
    # Quote: PDF p. 270 of the operator's copy, 19 words, quotes.py OK.
    # Lesson total: 19 words.
    {
        "slug": "tests-of-the-measurement-model",
        "title": "Tests of the Measurement Model",
        "module": "Appendix C · Statistical Methods Used in Our Research",
        "one_line": "A construct is used in the analysis only if its items load on it, it captures more of their variance than error does, it stays distinct from the others, and it is reliable; every test must pass.",
        "summary": (
            "The appendix lists the tests a construct must pass before the authors "
            "use it: loadings above 0.60, average variance extracted above 0.50, its "
            "square root above the construct's correlations, correlations below 0.85, "
            "and reliability above 0.70. Compute the average variance extracted and "
            "composite reliability of invented constructs from their loadings, and "
            "see which tests each passes."
        ),
        "key": [
            "validate the measures, then test the claims",
            "item loadings above 0.60, no cross loading",
            "variance extracted above one half",
            "its root must beat its correlations",
            "correlations between constructs below 0.85",
            "reliability above 0.70; all tests pass",
        ],
        "key_label": "The measurement model in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the appendix's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Loading",
             "How strongly an item is tied to the construct it is meant to measure; "
             "in the lab, a number from 0 to 1 for each item. The appendix asks that "
             "items load on their own construct above 0.60 and should not cross-load, "
             "that is, load strongly on another construct as well."),
            ("Average variance extracted",
             "The appendix describes it as the variance a construct captures against "
             "the variance due to measurement error, to be greater than 0.50. From "
             "standardized loadings it is the mean of their squares. The lab shortens "
             "it to AVE."),
            ("Composite reliability",
             "A measure of a construct's internal consistency computed from the "
             "loadings, with 0.70 as the acceptable cutoff. Cronbach's alpha is its "
             "counterpart, computed from the answers; the appendix asks for either "
             "to pass. The lab abbreviates composite reliability to CR."),
        ],
        "read_title": "The tests in the appendix's order, then the count",
        "read_intro": (
            "Read the appendix's Testing for Relationships and Tests of the "
            "Measurement Model in your own copy first. The lesson takes each test, "
            "gives the arithmetic the appendix leaves out, and computes it."
        ),
        "body": [
            ("p", "&ldquo;All of the above tests must pass for a construct to be "
                  "considered suitable for use in further analysis.&rdquo; Forsgren, "
                  "Humble and Kim write that in Appendix C, in the section Tests of "
                  "the Measurement Model. The lesson reads that section and the "
                  "short section Testing for Relationships that introduces it. The "
                  "authors work in two stages, following Gefen and Straub (2005): "
                  "first validate the measures and form the latent constructs of "
                  "Chapter 13, then, with only the constructs that pass, test the "
                  "hypotheses."),
            ("p", "The first test looks at the items. Principal components analysis "
                  "with varimax rotation, run separately for the independent and the "
                  "dependent variables, helps confirm convergent validity, the "
                  "property that items meant to measure one construct do. The authors "
                  "almost always used the exploratory kind, which finds the structure "
                  "without imposing one in advance; the confirmatory kind was used "
                  "once, for transformational leadership, whose items are well "
                  "established. Items should load on their construct above 0.60 and "
                  "not cross-load. The appendix names no threshold for cross-loading."),
            ("p", "The second is the average variance extracted. The appendix does not "
                  "give a formula; the standard one, for standardized loadings, is "
                  "the mean of the squared loadings, and the lab uses it. A loading "
                  "of 0.71 squares to about one half, so an AVE above 0.50 means "
                  "the construct accounts, on average, for more than half of the "
                  "variance of its items. The appendix requires it above 0.50 for "
                  "convergent validity. It also asks that the square root of the AVE, "
                  "set along the diagonal of a table of correlations, exceed "
                  "the correlations in its row and column, which supports "
                  "discriminant validity, the appendix's divergent validity: a "
                  "construct should share more with its own items than with another "
                  "construct. The lab tests it as AVE greater than r squared, "
                  "which is the same test and avoids a square root."),
            ("math", [
                "AVE = (λ₁² + λ₂² + … + λₖ²) / k",
                "root test: √AVE must exceed the absolute value of r",
            ]),
            ("p", "The third is the correlation between constructs, which the appendix "
                  "wants below 0.85 to help confirm discriminant validity. Two "
                  "constructs correlated at 0.90 are hard to call two things. This "
                  "test and the root test are separate: a pair can pass one and fail "
                  "the other."),
            ("p", "The fourth is reliability, internal consistency. Cronbach's alpha "
                  "has a cutoff of 0.70 (the appendix's sentence names composite "
                  "reliability where it plainly means alpha). The authors add "
                  "a caution about alpha: it is biased against short scales, those with "
                  "few items, so they ran both alpha and composite reliability, and "
                  "every construct met one of the two cutoffs; composite reliability "
                  "also has a cutoff of 0.70. The lesson Latent Constructs and System "
                  "Data computes alpha; this lab computes composite reliability, which "
                  "from standardized loadings is the squared sum of the loadings over "
                  "that squared sum plus the error left by each item."),
            ("math", [
                "CR = (Σλ)² / ((Σλ)² + Σ(1 − λ²))",
            ]),
            ("p", "All of these tests must pass, and the authors report that every "
                  "construct used in the research did, so each exhibits what they "
                  "call good psychometric properties. Now the count. The lab's "
                  "<code>ave</code> view takes each item's construct and loading, and the "
                  "correlation between constructs. On the preset "
                  "<code>two-sound-constructs</code>, <code>release-confidence</code> has loadings "
                  "0.85, 0.80, 0.75 and 0.70: AVE 0.604, CR 0.858 and a root of 0.777. "
                  "<code>team-trust</code> has 0.90, 0.85 and 0.80: AVE 0.724, CR 0.887, root "
                  "0.851. Their correlation is 0.45, so both roots exceed it and every test "
                  "passes; the lab's last tile counts 14 of 14 tests passed, an AVE and a "
                  "CR for each construct, a test for each item's loading, and three "
                  "for the pair."),
            ("p", "The preset <code>weak-construct</code> swaps in <code>tool-fit</code>, "
                  "with loadings 0.70, 0.60 and 0.55, correlated 0.30 with "
                  "<code>release-confidence</code>. Its AVE is 0.384, below 0.50; its CR "
                  "is 0.649, below 0.70; and two loadings, 0.60 and 0.55, are not above "
                  "0.60. Its root is 0.620, above 0.30, and 0.30 is below 0.85, so "
                  "the root test and the correlation test pass for a construct "
                  "that fails three others, and the tests tile reads 10 of 14, naming them. "
                  "That is the point of the appendix's rule that all must pass."),
            ("p", "The preset <code>too-close</code> pairs <code>release-confidence</code> "
                  "with <code>release-readiness</code>, loadings 0.85, 0.80, 0.80 and "
                  "0.75: AVE 0.641, CR 0.877, root 0.801. Each construct passes "
                  "the loading, AVE and reliability tests. They are correlated at 0.80. "
                  "That is below 0.85, but 0.80 squared is 0.64, which is above "
                  "the 0.604 AVE of <code>release-confidence</code>, so its root, 0.777, is "
                  "below 0.80 and the root test fails. The pair is a case where a "
                  "construct shares as much with another as with its own items. The tests "
                  "tile reads 14 of 15 and names the one that failed."),
            ("p", "The lab takes the loadings you type. The authors estimated theirs "
                  "from thousands of answers, and so can you only from your own. "
                  "Passing these tests shows that, in one sample, the items hang "
                  "together and stay apart; it does not show that the name given to "
                  "a construct describes what it measures, and the foreword's "
                  "caution that these are perceptions still applies. The lesson "
                  "Several Views, and a Safeguard Against Rogue Data works the "
                  "same questions from an item correlation matrix."),
            ("h3", "Exercise"),
            ("ul", [
                "Two constructs, `scope` with loadings `0.80, 0.70, 0.65` and `pace` "
                "with `0.90, 0.85, 0.80`, correlated `0.75`.",
                "As records: `c1, scope, 0.80; c2, scope, 0.70; c3, scope, 0.65; "
                "d1, pace, 0.90; d2, pace, 0.85; d3, pace, 0.80`, and between: "
                "`scope, pace, 0.75`.",
            ]),
            ("p", "By hand, compute the AVE and CR of <code>scope</code> and test each "
                  "of the appendix's thresholds: loadings, AVE, CR, the roots against "
                  "0.75, and 0.75 against 0.85. Then type the records into the lab. "
                  "Find the one test that fails and the pair it concerns."),
            ("p", "Constructs that pass go on to the second stage: relationships and "
                  "classification. The next lesson, Tests for Relationships and "
                  "Classification, computes a correlation and its line."),
        ],
        "lab": ("acckit", {
            "mode": "validity",
            "view": "ave",
            "preset": "two-sound-constructs",
            "presets": [
                {"id": "two-sound-constructs",
                 "label": "Two constructs that pass every test",
                 "loadings": SOUND_LOADINGS,
                 "between": SOUND_BETWEEN,
                 "expect": {"avdAve": "release-confidence 0.60375; team-trust 869/1,200 ≈ 0.724", "avdCr": "release-confidence 1,922/2,239 ≈ 0.858; team-trust 2,601/2,932 ≈ 0.887", "avdRoot": "release-confidence ≈ 0.777; team-trust ≈ 0.851", "avdLow": "0: none", "avdTests": "14 of 14 pass"}},
                {"id": "weak-construct",
                 "label": "A construct with low loadings that still beats its correlation",
                 "loadings": WEAK_LOADINGS,
                 "between": WEAK_BETWEEN,
                 "expect": {"avdAve": "release-confidence 0.60375; tool-fit 461/1,200 ≈ 0.384", "avdCr": "release-confidence 1,922/2,239 ≈ 0.858; tool-fit 1,369/2,108 ≈ 0.649", "avdRoot": "release-confidence ≈ 0.777; tool-fit ≈ 0.620", "avdLow": "2: tf2 0.6, tf3 0.55", "avdTests": "10 of 14 pass; not passed: tool-fit AVE, tool-fit CR, tf2 loading, tf3 loading"}},
                {"id": "too-close",
                 "label": "Two sound constructs correlated at 0.80",
                 "loadings": CLOSE_LOADINGS,
                 "between": CLOSE_BETWEEN,
                 "expect": {"avdAve": "release-confidence 0.60375; release-readiness 0.64125", "avdCr": "release-confidence 1,922/2,239 ≈ 0.858; release-readiness 2,048/2,335 ≈ 0.877", "avdRoot": "release-confidence ≈ 0.777; release-readiness ≈ 0.801", "avdLow": "0: none", "avdTests": "14 of 15 pass; not passed: √AVE of release-confidence against release-readiness"}},
            ],
            "panel_title": "Variance extracted, reliability and the root test",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Testing a measurement model",
        "steps_intro": "Five steps, the last of them on constructs of your own.",
        "steps": [
            ("Check the loadings",
             "List every item's loading on its own construct. Flag any that is 0.60 "
             "or lower, since the appendix asks for loadings higher than 0.60."),
            ("Compute AVE and CR for each construct",
             "AVE is the mean of the squared loadings. For CR, square the sum of "
             "the loadings and divide by that plus the sum of one minus each squared "
             "loading."),
            ("Test each construct against the thresholds",
             "AVE above 0.50, CR above 0.70. A construct that fails either is not "
             "used, whatever else it passes."),
            ("Test each pair",
             "Check that AVE is above r squared for both constructs, which is the "
             "root test, and that r is below 0.85. Write down which of the pair "
             "fails."),
            ("Try it on constructs you use",
             "Take a short scale your team scores with its loadings, from a "
             "factor analysis or a vendor report. List which of the appendix's "
             "tests it passes and which it cannot be tested on from what you "
             "have."),
        ],
        "worked": {
            "title": "AVE and CR for release-confidence",
            "intro": [
                "Take the loadings 0.85, 0.80, 0.75 and 0.70 of <code>release-confidence</code>.",
            ],
            "lines": [
                "squares: 0.7225, 0.64, 0.5625, 0.49",
                "sum of squares 2.415",
                "AVE = 2.415 / 4 = 0.60375",
                "root: 0.777 · 0.777 = 0.6037, so root = 0.777",
                "sum of loadings 3.10; squared 9.61",
                "errors: 4 − 2.415 = 1.585",
                "CR = 9.61 / (9.61 + 1.585) = 9.61 / 11.195 = 0.858",
                "0.60375 > 0.50 and 0.858 > 0.70: both pass",
            ],
            "after": [
                "The error sum is the sum of one minus each squared loading, which "
                "is four items less their squares: 4 − 2.415. The lab prints AVE to "
                "three decimals, 0.604; the exact value is 483 / 800.",
            ],
        },
        "quiz_title": "Thresholds and what each test asks",
        "quiz": [
            {"q": "In the exercise, which of the appendix's tests does the pair fail?",
             "a": ["The AVE test, for scope",
                   "The root test, for scope against 0.75",
                   "The correlation test, since 0.75 is high",
                   "None: both constructs pass everything"],
             "c": 1,
             "why": "The loadings of scope are 0.80, 0.70 and 0.65, all above 0.60. Its AVE "
                    "is (0.64 + 0.49 + 0.4225) / 3 = 0.5175, above 0.50, and its CR is "
                    "0.762, above 0.70. The correlation 0.75 is below 0.85. But the "
                    "root, about 0.719, is below 0.75, since 0.75 squared is 0.5625, "
                    "above 0.5175. The root test fails for scope; pace passes, with "
                    "a root of about 0.851."},
            {"q": "A construct has AVE 0.55, composite reliability 0.82, every "
                  "loading above 0.60, and its square root is above each of its "
                  "correlations with the others, which are all below 0.85. What does "
                  "the appendix say about it?",
             "a": ["It passes every test listed and may go on to the analysis",
                   "It fails, because AVE is below 0.60",
                   "It fails, because alpha has not been computed",
                   "It must be rerun with confirmatory factor analysis"],
             "c": 0,
             "why": "The thresholds are loadings above 0.60, AVE above 0.50, the root above "
                    "the correlations, correlations below 0.85, and reliability above "
                    "0.70, by alpha or composite reliability. Nothing in the appendix "
                    "calls for 0.60 AVE, for both alpha and composite reliability, or for "
                    "the confirmatory kind of analysis, which it used once."},
            {"q": "What does the appendix say about Cronbach's alpha for a construct "
                  "with few items?",
             "a": ["It is biased against small scales, so composite reliability is "
                   "run too",
                   "It is biased in favor of small scales, so the cutoff is raised",
                   "It cannot be computed for fewer than five items",
                   "It must be at least 0.85 for small scales"],
             "c": 0,
             "why": "The authors say alpha is known to be biased against constructs "
                    "with a low number of items, which is why they ran both measures. "
                    "They say nothing of a different cutoff for small scales, and "
                    "0.85 is the correlation limit between constructs."},
            {"q": "On the preset weak-construct, tool-fit passes the root test. What "
                  "follows?",
             "a": ["It is suitable for the analysis, since it passes a test of "
                   "validity",
                   "Nothing for suitability, since it fails AVE, CR and the loading "
                   "test and all must pass",
                   "The loadings must have been mistyped",
                   "Its root is above 0.30, so its AVE must be above 0.50"],
             "c": 1,
             "why": "The root test compares a construct with its correlations, and 0.30 "
                    "is a low bar; tool-fit's AVE is 0.384, below 0.50, which a root of "
                    "0.620 does not contradict. Because all the tests must pass for "
                    "use in the analysis, passing one says little."},
        ],
        "mistakes": [
            ("Passing one test and calling the construct valid",
             "The appendix says all of the tests must pass. On "
             "<code>weak-construct</code> the root test and the correlation test pass "
             "for a construct whose AVE is 0.384, whose CR is 0.649 and with two "
             "loadings not above 0.60. A single passed test answers a single "
             "question."),
            ("Treating the correlation limit of 0.85 and the root test as one test",
             "On <code>too-close</code> the correlation, 0.80, is below 0.85 and "
             "passes, while the root test fails for <code>release-confidence</code> "
             "because 0.80 squared, 0.64, exceeds its AVE of 0.604. The appendix lists "
             "them separately, and each can fail without the other."),
            ("Reading AVE as a score of how good a construct is",
             "AVE is the share of its items' variance that the construct accounts "
             "for, on average, from standardized loadings, so 0.604 means about 60 "
             "percent, in this sample. Whether the items measure what the construct's "
             "name says is a question the tests cannot answer."),
        ],
        "standard": (
            "Finish when you can test a construct against the appendix.",
            "Given the loadings of two constructs and their correlation, compute each "
            "construct's AVE, CR and root, and say which of the appendix's tests the "
            "pair passes and fails."
        ),
        "note": (
            "The lab takes the loadings you type as given and treats them as "
            "standardized. It does not estimate them from answers, and it cannot say "
            "whether a name describes what its items measure; the tests show a "
            "pattern in a sample."
        ),
    },
]
