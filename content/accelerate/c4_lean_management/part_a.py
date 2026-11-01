"""Security, Lean Management and Product Development, lessons 1-5 -- Chapters
6, 7 and 8.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 6, Integrating Infosec into
the Delivery Lifecycle (Shifting Left on Security, Compliance in the Federal
Government, The Rugged Movement); Chapter 7, Management Practices for Software
(Lean Management Practices, Implement a Lightweight Change Management Process,
What About Segregation of Duties?); Chapter 8, Product Development (Lean
Product Development Practices, Working in Small Batches, Team Experimentation,
Effective Product Management Drives Performance). Pages in the comments are
PDF pages of the operator's copy; the lessons cite by chapter and section.
Every quotation is copied from that copy and checked with quotes.py. The
samples are written for these lessons: none of the book's figures, tables or
data is reproduced. The design is docs/accelerate/PLAN.md, section C,
Course 4.
"""

_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)

# ---------------------------------------------------------------- 01 samples

# A team's year of work, in hours, written for the lesson: 800 on new work,
# 100 unplanned, 140 rework, and security findings fixed at the stated costs.
# Costs per finding by stage (the lesson's own): design 2 h, build 4 h,
# test 12 h, after release 40 h. Twelve findings.
SEC_KINDS = "new unplanned rework security"
SEC_OTHER = "new, 800; unplanned, 100; rework, 140"
# Late: 1 at build, 3 at test, 8 after release = 4 + 36 + 320 = 360 hours.
SEC_LATE = SEC_OTHER + (
    "; security, 4, build; security, 36, test; security, 320, release"
)
# Early: 5 at design, 4 at build, 2 at test, 1 after release
# = 10 + 16 + 24 + 40 = 90 hours.
SEC_EARLY = SEC_OTHER + (
    "; security, 10, design; security, 16, build; security, 24, test; "
    "security, 40, release"
)

# 01 exercise: ten findings, costs design 3, build 6, test 15, release 45.
# Late: 2 build, 3 test, 5 release = 12 + 45 + 225 = 282 hours.
# Early: 4 design, 3 build, 2 test, 1 release = 12 + 18 + 30 + 45 = 105.
SEC_EX_KINDS = "new unplanned rework security"
SEC_EX_OTHER = "new, 600; unplanned, 60; rework, 90"
SEC_EX_LATE = SEC_EX_OTHER + (
    "; security, 12, build; security, 45, test; security, 225, release"
)
SEC_EX_EARLY = SEC_EX_OTHER + (
    "; security, 12, design; security, 18, build; security, 30, test; "
    "security, 45, release"
)

# ---------------------------------------------------------------- 02 samples

# Little's law with a limit: throughput held at 2 items a day.
WIP_THROUGHPUT = "2"
WIP_LEVELS = "18, 6"
# A board over days 0 to 8, six items, start and done days.
# Lead times 2, 4, 2, 4, 2, 4 = 18 item-days; average WIP 18/8 = 9/4;
# throughput 6/8 = 3/4; average lead time 18/6 = 3 = (9/4)/(3/4).
BOARD_LOG = (
    "A, 0, 2; B, 0, 4; C, 1, 3; D, 2, 6; E, 3, 5; F, 4, 8"
)
# 02 exercise: days 0 to 6, six items. Lead times 3, 1, 4, 2, 3, 1 = 14
# item-days; average WIP 14/6 = 7/3; throughput 6/6 = 1; lead 14/6 = 7/3.
BOARD_EX = "P, 0, 3; Q, 0, 1; R, 1, 5; S, 2, 4; T, 3, 6; U, 5, 6"

# ---------------------------------------------------------------- 03 samples

# Twelve invented changes, six by peer review and six by a change advisory
# board. Peer waits 1, 2, 1, 3, 2, 1 hours: sum 10, mean 5/3, median 3/2.
# CAB waits 48, 72, 96, 24, 72, 120 hours: sum 432, mean 72, median 72.
# One failure in each route: 1/6 = 16.7 percent each.
CHANGES_ONE = (
    "c1, peer, 1, no; c2, peer, 2, no; c3, peer, 1, yes; c4, peer, 3, no; "
    "c5, peer, 2, no; c6, peer, 1, no; "
    "c7, cab, 48, no; c8, cab, 72, no; c9, cab, 96, yes; c10, cab, 24, no; "
    "c11, cab, 72, no; c12, cab, 120, no"
)
# The same twelve with one more CAB change failing: 2/6 = 33.3 percent.
CHANGES_TWO = CHANGES_ONE.replace("c11, cab, 72, no", "c11, cab, 72, yes")

# 03 exercise: twelve changes by three routes.
# none: waits 0; 1 failure in 4 = 25 percent.
# peer: waits 2, 1, 3, 1: sum 7, mean 7/4, median 3/2; 1 in 4 = 25 percent.
# cab: waits 24, 48, 72, 96: sum 240, mean 60, median 60; 1 in 4 = 25 percent.
# The CAB's mean wait over the peer route's: 60 - 7/4 = 233/4 = 58.25 hours.
CHANGES_EX = (
    "x1, none, 0, no; x2, none, 0, yes; x3, none, 0, no; x4, none, 0, no; "
    "y1, peer, 2, no; y2, peer, 1, no; y3, peer, 3, yes; y4, peer, 1, no; "
    "z1, cab, 24, no; z2, cab, 48, no; z3, cab, 72, yes; z4, cab, 96, no"
)

# ---------------------------------------------------------------- 04 samples

# Twelve items, one day each, a release costing two days.
# One batch of 12: first feedback day 14.  Four batches of 3: first feedback
# day 3 + 2 = 5, last day 4 * 5 = 20, overhead 4 * 2 = 8 days against 2.
# With an automated release costing half a day: 3.5, 14, overhead 2 against 1/2.
# 04 exercise: ten items, one day each, a release costing three days.
# Five batches of 2: first feedback 2 + 3 = 5; last 5 * 5 = 25; overhead 15.

# ---------------------------------------------------------------- 05 samples

# Eight invented teams, each with a lean-product score and a delivery score
# on a 1-to-7 scale. Means 4 and 4. Sxy = 7, Sxx = 12, Syy = 8,
# r = 7 / sqrt(96) = 0.714, r squared = 49/96 = 51.0 percent.
# y on x: slope 7/12, intercept 5/3.  x on y: slope 7/8, intercept 1/2.
TEAMS_LEAN_FIRST = (
    "t1, 2, 3; t2, 3, 2; t3, 4, 5; t4, 4, 4; t5, 5, 5; t6, 6, 5; t7, 3, 4; "
    "t8, 5, 4"
)
TEAMS_DELIVERY_FIRST = (
    "t1, 3, 2; t2, 2, 3; t3, 5, 4; t4, 4, 4; t5, 5, 5; t6, 5, 6; t7, 4, 3; "
    "t8, 4, 5"
)
# 05 exercise: five invented teams. Means 3 and 3; Sxy = 8, Sxx = 10,
# Syy = 10, r = 8/10 = 0.8, r squared = 64 percent.
TEAMS_EX = "u1, 1, 2; u2, 2, 1; u3, 3, 3; u4, 4, 5; u5, 5, 4"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 6 (PDF pp. 105-110 of the operator's copy): the opening and the
    # staffing ratio (pp. 105-106), Shifting Left on Security (pp. 106-109),
    # Compliance in the Federal Government (pp. 107-108), the finding on
    # remediation (pp. 108-109), The Rugged Movement (pp. 109-110).
    # Do not quote the chapter's first sentence (drop capital).
    # Quote: PDF p. 106 of the operator's copy, 19 words, quotes.py OK.
    # Lesson total: 19 words.
    # F1 (p. 105): Wickett's ratio, one infosec person to 10 infrastructure
    # people to 100 developers in large companies (Wickett 2014).
    # F2 (p. 108): high performers spent 50% less time remediating security
    # issues than low performers.
    {
        "slug": "shifting-left-on-security",
        "title": "Integrating Infosec into the Delivery Lifecycle",
        "module": "Chapter 6 · Integrating Infosec into the Delivery Lifecycle",
        "one_line": "Move security from a review at the end into the daily work of the team, and the same findings cost fewer hours to fix.",
        "summary": (
            "Chapter 6 asks whether security slows delivery down or helps it. Read "
            "what the authors mean by shifting left, why they say the work has to "
            "move from security teams to the developers, and what they found about "
            "the time spent fixing security issues; then price one team's "
            "findings by the stage at which they were caught."
        ),
        "key": [
            "shift left: security inside the process",
            "review every major feature, without delay",
            "infosec joins design, demos and tests",
            "preapproved, easy-to-use libraries and tools",
            "high performers fixed less, in less time",
            "rugged: everybody's responsibility",
        ],
        "key_label": "Shifting left on security in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Shifting left",
             "Bringing information security into the work of delivery itself, "
             "rather than leaving it as a stage after development is over. "
             "The picture is a timeline running left to right from design to "
             "release: the work moves toward the left."),
            ("Preapproved tools",
             "Libraries, packages, toolchains and processes that the security "
             "team has already approved and that developers and operations can "
             "pick up without asking. The authors present them as the way to "
             "make the secure choice the simple one."),
            ("Remediation hours",
             "The hours a team spends fixing a security finding after it has been "
             "found. The lab adds them up by the stage at which each finding was "
             "caught and sets them beside the team's other work."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read Chapter 6 in your own copy first; it is short. The lesson sets "
            "out its argument in order, then prices a small team's security "
            "findings by the stage at which they were found."
        ),
        "body": [
            ("p", "&ldquo;Our research shows that building security into software "
                  "development not only improves delivery performance but also "
                  "improves security quality.&rdquo; That is the claim of Chapter 6, "
                  "Integrating Infosec into the Delivery Lifecycle, and it answers a "
                  "research question the preface lists for the 2016 survey year: "
                  "does bringing security into the work speed the process up or "
                  "hold it back? The chapter has three parts, a section on shifting left, a "
                  "box on compliance in the federal government of the United States, "
                  "and a short section on the Rugged movement. This lesson reads "
                  "all three."),
            ("p", "The problem comes first. The authors start from the DevOps "
                  "movement's own aim, which was to stop developers and operations "
                  "throwing work over a wall at each other, and note that the same "
                  "habit appears wherever functions in the delivery chain fail to "
                  "work together. Security is their example. Infosec teams are "
                  "often thinly staffed: they quote James Wickett's ratio, from "
                  "2014, of about one infosec person to ten infrastructure people "
                  "to a hundred developers in large companies. The team is usually "
                  "brought in at the end of the lifecycle, when a change is painful "
                  "and expensive to make, and many developers do not know the "
                  "common risks, such as those on the OWASP Top 10."),
            ("p", "Their answer is to shift left. The chapter lists three parts to "
                  "it. Every major feature gets a security review, arranged so "
                  "that development does not slow down. Security takes part in "
                  "the whole lifecycle, from design through operations: the "
                  "infosec experts help design applications, come to "
                  "demonstrations and comment, and see that security features "
                  "are covered by the automated tests. And the secure route is "
                  "made the easy one for developers, by supplying libraries, "
                  "packages, toolchains and processes that security has "
                  "already approved and that are simple to adopt. The authors "
                  "report that teams that do this are better at continuous "
                  "delivery, which in turn helps delivery performance."),
            ("p", "The authors give two reasons for the shift in who does the work. "
                  "It is easier to equip the builders to get it right than to "
                  "inspect nearly finished systems for large architectural "
                  "defects that mean substantial rework. "
                  "And infosec teams do not have the capacity to review every "
                  "deployment once deployments are frequent; in many organizations, "
                  "they say, security and compliance is a major bottleneck on "
                  "the way from finished code to live. The chapter adds a side "
                  "benefit, better communication between the teams. The box on "
                  "federal systems makes the same point at the scale of a "
                  "government: a platform built by a small team of civil servants, "
                  "cloud.gov, takes care of most of the required controls at the "
                  "platform level, so that systems on it reach production in "
                  "weeks and not months."),
            ("p", "Then the finding the lab is built around. The authors report that "
                  "high performers spent 50 percent less time than low performers "
                  "on fixing security problems. Read it as the book's "
                  "figure: it is a comparison between the groups of teams the "
                  "survey found in the years it covers, and the measure is what "
                  "respondents reported. It does not say that every team will halve "
                  "its time, and the chapter does not give a cost for fixing a "
                  "finding at any stage."),
            ("p", "The chapter ends with the Rugged movement and two "
                  "more names for DevOps with security in it. DevSecOps is credited "
                  "to several people, among them Topo Pal of Capital One and "
                  "Shannon Lietz of Intuit; Rugged DevOps, from Josh Corman and "
                  "James Wickett, joins DevOps to the Rugged Manifesto, "
                  "whose first claim is that the developer's code is rugged, built "
                  "to face attack and carry on. The authors take one point from it, "
                  "in line with DevOps: being rugged is everybody's responsibility."),
            ("p", "Now the count. The lab takes a team's year of work as records of a "
                  "kind of work and its hours, with a stage on the security "
                  "records, and splits the total by kind. The team is invented: "
                  "800 hours of new work, 100 unplanned and 140 rework. It found "
                  "twelve security issues, and the lesson states what it cost to fix "
                  "one at each stage: 2 hours at design, 4 at build, 12 at test "
                  "and 40 after release. Those costs are the lesson's own, to make "
                  "the arithmetic visible; the book gives none. On the preset "
                  "<code>late</code> the team found 1 issue at build, 3 at test and "
                  "8 after release, which is 4, 36 and 320 hours: 360 hours of "
                  "security remediation in a total of 1,400, about 25.7 percent, "
                  "and new work is 800 of the 1,400."),
            ("p", "The preset <code>early</code> is the same twelve issues found "
                  "earlier, as a team that had shifted left might find them: 5 at "
                  "design, 4 at build, 2 at test and 1 after release. That is "
                  "10, 16, 24 and 40 hours, 90 in all. The total falls to "
                  "1,130 hours, security is about 8 percent of it, and new work's "
                  "share rises from about 57.1 percent to about 70.8. The 270 hours "
                  "that are freed are the arithmetic of the costs the lesson "
                  "chose; the lab cannot say what finding issues earlier takes, "
                  "which is the training, the tools and the time of the "
                  "infosec experts at design. The tile for hours by stage shows the "
                  "split: build 4, test 36 and release 320 on <code>late</code>, "
                  "design 10, build 16, test 24 and release 40 on "
                  "<code>early</code>. The preset <code>quarter</code> reaches "
                  "the same place another way: it keeps the late records and "
                  "scales security to a quarter, which frees 270 hours that go to "
                  "new work, so new work is 1,070 of 1,400 hours, 107/140, about "
                  "76.4 percent. The tiles for hours freed and for the shares "
                  "after the scaling are the ones that preset fills in."),
            ("h3", "Exercise"),
            ("ul", [
                "A team's year: `new, 600; unplanned, 60; rework, 90`, and ten "
                "security issues.",
                "Costs per issue: design 3 hours, build 6, test 15, after release 45.",
                "Found late: 2 at build, 3 at test, 5 after release. Found early: "
                "4 at design, 3 at build, 2 at test, 1 after release.",
            ]),
            ("p", "Work out the hours of security remediation for the late team and "
                  "for the early team, and the hours freed. Then type the records "
                  "into the lab, one record for each stage with its hours, to check "
                  "your count."),
            ("p", "Whether your own team would find its issues earlier, and at what "
                  "price, is yours to answer. The next lesson, Lean Management "
                  "Practices, moves from security to the way work is managed, and "
                  "starts with limiting work in progress."),
        ],
        "lab": ("acckit", {
            "mode": "work",
            "view": "split",
            "preset": "late",
            "presets": [
                {"id": "late",
                 "label": "A team that finds twelve security issues late",
                 "kinds": SEC_KINDS,
                 "entries": SEC_LATE,
                 "expect": {"awkTotal": "1,400 hours", "awkHours": "new 800; unplanned 100; rework 140; security 360", "awkNew": "4/7 ≈ 57.1%", "awkStages": "build 4; test 36; release 320"}},
                {"id": "early",
                 "label": "The same twelve found at earlier stages",
                 "kinds": SEC_KINDS,
                 "entries": SEC_EARLY,
                 "expect": {"awkTotal": "1,130 hours", "awkHours": "new 800; unplanned 100; rework 140; security 90", "awkNew": "80/113 ≈ 70.8%", "awkStages": "design 10; build 16; test 24; release 40"}},
                {"id": "quarter",
                 "label": "The late team, with security remediation cut to a quarter",
                 "kinds": SEC_KINDS,
                 "entries": SEC_LATE,
                 "scale": "security, 1/4",
                 "expect": {"awkTotal": "1,400 hours", "awkHours": "new 800; unplanned 100; rework 140; security 360", "awkNew": "4/7 ≈ 57.1%", "awkStages": "build 4; test 36; release 320", "awkFreed": "270 hours (security 360 → 90), to new", "awkNewAfter": "107/140 ≈ 76.4%"}},
            ],
            "panel_title": "Hours of security remediation",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Pricing security findings by stage",
        "steps_intro": "Four steps, the last of them on a team of your own.",
        "steps": [
            ("List the findings with their stages",
             "Write down each security issue the team fixed in a period, and the "
             "stage at which it was found: design, build, test or after release."),
            ("Put an hour cost on each fix",
             "Take the hours from your own records where you have them. Where you "
             "do not, state a cost per stage as an assumption, as the lesson does, "
             "and keep it separate from anything the book reports."),
            ("Total by stage and by kind of work",
             "Add the hours of each stage, then set the total beside the team's "
             "other work. The share that security takes is the figure to watch."),
            ("Move the findings and recount",
             "On your own team, type the real records into the lab, then move "
             "some findings one stage earlier and recount. The difference is "
             "what the stated costs make of the move, not a forecast."),
        ],
        "worked": {
            "title": "Three hundred and sixty hours, late",
            "intro": [
                "Total the preset <code>late</code> by hand: twelve issues, costs "
                "of 4, 12 and 40 hours for build, test and after release.",
            ],
            "lines": [
                "Build: 1 issue at 4 hours = 4",
                "Test: 3 issues at 12 hours = 36",
                "After release: 8 issues at 40 hours = 320",
                "Security: 4 + 36 + 320 = 360 hours",
                "Total: 800 + 100 + 140 + 360 = 1,400 hours",
                "Security's share: 360 / 1,400 = 9/35, about 25.7 percent",
            ],
            "after": [
                "Each line is a product or a sum of the numbers the lesson states. "
                "The early team's 90 hours is the same sum with the findings "
                "caught sooner, and the whole difference between the two presets "
                "comes from the costs chosen for each stage.",
            ],
        },
        "quiz_title": "Security, shifting left and the chapter's figures",
        "quiz": [
            {"q": "In the exercise, how many hours do the ten findings cost the late "
                  "team and the early team, and how many hours are freed?",
             "a": ["282 and 105, freeing 177",
                   "282 and 105, freeing 387",
                   "225 and 45, freeing 180",
                   "387 and 282, freeing 105"],
             "c": 0,
             "why": "Late: 2 at build is 12 hours, 3 at test is 45, 5 after release "
                    "is 225: 282. Early: 4 at design is 12, 3 at build is 18, 2 at "
                    "test is 30, 1 after release is 45: 105. The difference is "
                    "177. The second option adds the other work's 150 hours to "
                    "the late total before subtracting; the third compares only "
                    "the after-release rows; the fourth adds the two totals."},
            {"q": "In Chapter 6, how does the time that high performers spent "
                  "remediating security issues compare with low performers'?",
             "a": ["High performers spent 50 percent less time",
                   "High performers spent 50 percent more time, because they "
                   "find more issues",
                   "The two groups spent about the same time",
                   "Low performers spent 50 percent less time, because they "
                   "review less"],
             "c": 0,
             "why": "The authors report that high performers spent 50 "
                    "percent less time than low performers fixing security "
                    "problems, and read it as a result of building security "
                    "into daily work in place of retrofitting it at the end. It "
                    "is a comparison of groups of teams in a survey, not a "
                    "promise for any one team."},
            {"q": "Which of these is the chapter's description of what shifting "
                  "left on security involves?",
             "a": ["The infosec team runs every security review itself before "
                   "each release, with more staff",
                   "A review of each major feature, infosec involved throughout the "
                   "lifecycle, and approved tools that are simple to adopt",
                   "Developers take over security entirely and the infosec team "
                   "stops attending design and demonstrations",
                   "A single penetration test is moved from the end of the year "
                   "to its start"],
             "c": 1,
             "why": "The chapter names three parts: a review of each major feature "
                    "that does not slow development, infosec involved across the "
                    "lifecycle, and approved tools that are simple to adopt. The first "
                    "option is the arrangement it argues against; the third is "
                    "contradicted by the infosec experts contributing to design "
                    "and demonstrations; the fourth is not in the chapter."},
            {"q": "In the chapter, what ratio of infosec people to infrastructure "
                  "people to developers does James Wickett cite for large "
                  "companies?",
             "a": ["1 to 10 to 100",
                   "1 to 100 to 10",
                   "10 to 100 to 1",
                   "1 to 10 to 10"],
             "c": 0,
             "why": "The chapter cites one infosec person for every ten "
                    "infrastructure people and every hundred developers, from "
                    "Wickett in 2014, as a sign of how thinly security teams are "
                    "staffed. It is one author's figure for large companies, not "
                    "a measure from the authors' survey."},
        ],
        "mistakes": [
            ("Thinking shifting left means security is the developers' job alone",
             "The chapter moves who does the reviewing, not whether infosec takes "
             "part. Infosec experts still contribute to designing applications, "
             "attend demonstrations and give feedback, and they supply the "
             "preapproved tools. What changes is that the people building the "
             "software are given the means to build security in."),
            ("Reading the 50 percent as the saving your team will see",
             "The figure compares high and low performers across the survey, in "
             "the years it covers. It is not a price list: the chapter gives no "
             "cost for fixing an issue at any stage, and the lab's costs are the "
             "lesson's own assumptions, chosen to show the arithmetic."),
            ("Treating the review at the end as the safe place for it",
             "The authors give two reasons against it: it is hard to inspect "
             "nearly finished systems for large architectural defects without "
             "substantial rework, and infosec teams cannot review every release "
             "once deployments are frequent. They describe security and "
             "compliance as a bottleneck in many organizations."),
        ],
        "standard": (
            "Finish when you can price security findings by the stage that "
            "caught them.",
            "Given findings with the stage each was found and a stated cost per "
            "stage, total the remediation hours, set them beside the other work, "
            "and say which part of the result comes from your assumed costs."
        ),
        "note": (
            "The lab adds the hours you give it. It cannot tell you what a stage's "
            "fix costs on your team, whether the findings would really be caught "
            "earlier, or what the earlier catching costs; the book reports a "
            "comparison of groups of teams, not a cost per stage."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 7, Lean Management Practices (PDF pp. 111-114 of the operator's
    # copy): the opening history (pp. 111-112), the three components
    # (p. 112), WIP limits and visual displays and what is measured
    # (p. 113), the effects on burnout and culture (p. 114).
    # Quote: PDF p. 113 of the operator's copy, 11 words, quotes.py OK.
    # Lesson total: 11 words. Cross-reference: System Design, Queues and
    # Utilisation, "Little's Law from a Trace".
    {
        "slug": "lean-management-practices",
        "title": "Lean Management Practices",
        "module": "Chapter 7 · Management Practices for Software",
        "one_line": "Limit work in progress, show the work, and feed what production tells you back to the team: the three together predict delivery performance, and the first alone does not.",
        "summary": (
            "Chapter 7 models Lean management with three components. Read what "
            "each one asks, why the authors find a bare WIP limit a weak "
            "predictor of delivery performance, and what the three "
            "together are linked to; then use Little's law to see what a limit "
            "does to lead time when throughput holds."
        ),
        "key": [
            "limit work in progress",
            "show the work and the quality, to all",
            "use production data to decide daily",
            "limits alone do not predict much",
            "together: a much stronger effect",
            "lead time is WIP over throughput",
        ],
        "key_label": "Lean management in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Work in progress (WIP)",
             "The number of items started and not yet done. A WIP limit is a "
             "cap on it. The authors measure more than whether a limit exists: "
             "whether it makes obstacles to flow visible, and whether the team "
             "removes them."),
            ("Visual display",
             "A board, storyboard or dashboard that shows the current status of "
             "the work and key quality and productivity measures, including "
             "defects, to engineers and leaders. The authors look at what is "
             "shown, how broadly it is shared, and how easy it is to reach."),
            ("Little's law",
             "For a steady flow, the average number of items in the system equals "
             "the throughput times the average time an item spends in it. So "
             "lead time is work in progress divided by throughput. The lab "
             "applies it to the numbers you give it."),
        ],
        "read_title": "The chapter's opening, its three components, then the count",
        "read_intro": (
            "Read the opening of Chapter 7 and its first section in your own copy "
            "first. The lesson reads them as an account of what the authors "
            "measured, and then works Little's law on a small board."
        ),
        "body": [
            ("p", "Chapter 7, Management Practices for Software, opens with a "
                  "short history of ways of managing software work: the project "
                  "and program management paradigm of the Project Management "
                  "Institute and PRINCE2, the Agile methods that followed the "
                  "Agile Manifesto in 2001, and the Lean movement, which comes "
                  "from Toyota and was adapted for software by Mary and Tom "
                  "Poppendieck. The chapter then takes two of the Lean-derived "
                  "practices and asks how they drive software delivery "
                  "performance. This lesson reads the first, in the section Lean "
                  "Management Practices; the next reads the second."),
            ("p", "The authors modeled Lean management with three components. The "
                  "first is capping work in progress and letting the cap drive "
                  "improvement of the process and more throughput. The second "
                  "is keeping visual displays of the work's status and of key "
                  "quality and productivity measures, defects included, open to "
                  "engineers and leaders alike and tied to operational goals. The "
                  "third is deciding by the day with data that application and "
                  "infrastructure monitoring tools supply."),
            ("p", "The finding the lesson turns on is about the first component. "
                  "The authors report that &ldquo;WIP limits on their own do not "
                  "strongly predict delivery performance.&rdquo; Only when they "
                  "are combined with visual displays and a feedback loop from "
                  "production monitoring back to the delivery teams or the "
                  "business do the authors see a strong effect, and with the "
                  "three together the positive effect on software delivery "
                  "performance is much stronger. The practices are well known in "
                  "the Lean community, they write: they keep teams from being "
                  "overburdened, which can lengthen lead times, and they expose "
                  "obstacles to flow."),
            ("p", "How the authors measured it explains the result. For WIP, the "
                  "survey did not only ask whether a team is good at limiting WIP "
                  "and has processes for it; it asked whether the limits bring "
                  "the obstacles to flow into view, and whether the team clears "
                  "them by improving the process, so that throughput rises. A limit that nobody acts on is not what they "
                  "measured. For visual displays it asked whether dashboards share "
                  "information, whether teams use kanban or storyboards, whether "
                  "quality and productivity information is readily available, and "
                  "whether failures and defect rates are shown publicly. Visibility "
                  "and the communication it enables are, they say, key."),
            ("p", "The chapter adds what the practices go with. The authors "
                  "hypothesized that in combination they raise delivery "
                  "performance, and report that they do; they also report positive "
                  "effects on team culture and performance, in that Lean "
                  "management goes with less burnout (the subject of Chapter 9) "
                  "and a more generative culture, in the sense of Westrum's model "
                  "from Chapter 3. The word the authors use throughout is "
                  "predict: a statistical relationship found in their survey, "
                  "with the limits the survey has."),
            ("p", "Now the count. System Design's lesson Little's Law from a "
                  "Trace teaches the law itself; this lab only uses it. On the "
                  "preset <code>limit</code> an invented team finishes 2 items a "
                  "day. With 18 items in progress, Little's law gives a lead time "
                  "of 18 over 2, which is 9 days; with a limit of 6, it gives 6 "
                  "over 2, 3 days. The lab holds throughput at 2 in both cases, "
                  "and that is an assumption, not a finding: a team that cuts its "
                  "work in progress might finish more, or fewer, items in a "
                  "day, and the book's point is that the limit helps when it "
                  "exposes obstacles that the team then removes."),
            ("p", "The preset <code>board</code> reads the law from a log instead. "
                  "Six items were started and done over eight days, on days 0 to 2, "
                  "0 to 4, 1 to 3, 2 to 6, 3 to 5 and 4 to 8. Their lead times "
                  "are 2, 4, 2, 4, 2 and 4 days, 18 item-days in all. Over the 8 "
                  "days the average work in progress is 18 over 8, 2.25 items; the "
                  "throughput is 6 over 8, 0.75 items a day; and the average lead "
                  "time is 18 over 6, 3 days. Check the law: 2.25 divided by 0.75 "
                  "is 3, and the tile for Little's law on the log says that it "
                  "holds. It would say that it differs if an item were still "
                  "open at the end of the window, since an unfinished item "
                  "counts toward work in progress and not toward lead time. The "
                  "last tile on <code>limit</code> gives the second lead time "
                  "over the first, 3 over 9, a third."),
            ("h3", "Exercise"),
            ("ul", [
                "A board watched from day 0 to day 6, items as name, start, done.",
                "`P, 0, 3; Q, 0, 1; R, 1, 5; S, 2, 4; T, 3, 6; U, 5, 6`.",
            ]),
            ("p", "Work out each item's lead time, the average work in progress, the "
                  "throughput and the average lead time, and check that the law "
                  "holds. Then enter the six items in the lab, and say what you "
                  "would change about the board to make an obstacle to flow "
                  "visible."),
            ("p", "Limits and displays are half of Chapter 7. The next lesson, A "
                  "Lightweight Change Management Process, reads the other half: how "
                  "changes reach production, and the review that the authors found "
                  "to work."),
        ],
        "lab": ("acckit", {
            "mode": "flow",
            "view": "wip",
            "preset": "limit",
            "presets": [
                {"id": "limit",
                 "label": "Two items a day, with 18 in progress and then 6",
                 "throughput": WIP_THROUGHPUT,
                 "wip": WIP_LEVELS,
                 "expect": {"aflThru": "2 items a day", "aflLeadAt": "WIP 18: 9 days; WIP 6: 3 days", "aflChange": "1/3 ≈ 0.3× the lead time (9 → 3 days)"}},
                {"id": "board",
                 "label": "A board of six items over eight days",
                 "throughput": "-",
                 "days": "8",
                 "items": BOARD_LOG,
                 "expect": {"aflThru": "3/4 = 0.75 items a day", "aflAvgWip": "9/4 = 2.25 items", "aflAvgLead": "3 days", "aflLittle": "holds: average WIP 9/4 = 2.25 = throughput × average lead time"}},
            ],
            "panel_title": "Work in progress, throughput and lead time",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Applying Little's law to a board",
        "steps_intro": "Four steps, the last of them on a board of your own.",
        "steps": [
            ("Log the items",
             "For each item on the board, write the day it was started and the day "
             "it was done. Watch long enough that the board neither starts nor "
             "ends empty by luck, and say how long."),
            ("Add the item-days",
             "An item's lead time is done minus started. Add them all: this is "
             "the item-days the board held."),
            ("Divide three ways",
             "Average work in progress is the item-days over the days watched; "
             "throughput is the items over the days; average lead time is the "
             "item-days over the items."),
            ("Check the law, then try a limit",
             "Confirm that WIP over throughput gives the average lead time. Then "
             "take a lower limit and hold the throughput, as the lab does, and "
             "write down what you would need to be true for throughput to hold."),
        ],
        "worked": {
            "title": "A board of six items",
            "intro": [
                "Work the preset <code>board</code> by hand, over days 0 to 8.",
            ],
            "lines": [
                "Lead times: 2, 4, 2, 4, 2, 4 days",
                "Item-days: 2 + 4 + 2 + 4 + 2 + 4 = 18",
                "Average WIP: 18 / 8 = 2.25 items",
                "Throughput: 6 items / 8 days = 0.75 a day",
                "Average lead time: 18 / 6 = 3 days",
                "Little's law: 2.25 / 0.75 = 3 days",
            ],
            "after": [
                "The two ways of reaching 3 days agree because both come from the "
                "same 18 item-days. That is why the law holds on a log: it is "
                "arithmetic, not a finding about the team.",
            ],
        },
        "quiz_title": "Limits, displays and Little's law",
        "quiz": [
            {"q": "In the exercise's board, watched from day 0 to day 6, what is the "
                  "average lead time of the six items?",
             "a": ["7/3 of a day, about 2.33 days",
                   "14 days",
                   "1 day",
                   "3 days"],
             "c": 0,
             "why": "The lead times are 3, 1, 4, 2, 3 and 1 days, 14 item-days. "
                    "Divided by the 6 items that is 7/3. The average work in "
                    "progress is 14 over 6, also 7/3, and the throughput is 1 a "
                    "day, so the law gives 7/3 over 1. Fourteen is the item-days, "
                    "1 is the throughput, and 3 is the lead time of the first item."},
            {"q": "On the preset <code>limit</code>, throughput is held at 2 items "
                  "a day. What does Little's law give for the lead time when the "
                  "work in progress is limited to 6?",
             "a": ["3 days",
                   "12 days",
                   "9 days",
                   "6 days"],
             "c": 0,
             "why": "Lead time is work in progress over throughput: 6 over 2, 3 "
                    "days. Twelve is 6 times 2; 9 is the lead time with 18 in "
                    "progress; 6 is the work in progress itself. The result "
                    "depends on throughput holding, which the lab assumes."},
            {"q": "What does Chapter 7 report about WIP limits on their own?",
             "a": ["They do not strongly predict delivery performance; with visual "
                   "displays and a feedback loop from production monitoring the "
                   "effect is strong",
                   "They strongly predict delivery performance whatever else the "
                   "team does",
                   "They predict delivery performance only for teams above a "
                   "certain size",
                   "They lower delivery performance, because they slow the team "
                   "down"],
             "c": 0,
             "why": "The authors say the effect is strong only when limits are "
                    "combined with visual displays and a feedback loop from "
                    "production monitoring back to the teams or the business. "
                    "They report no size threshold, and no negative effect."},
            {"q": "Besides whether a team limits its WIP, what does the survey "
                  "behind Chapter 7 ask about WIP?",
             "a": ["Whether the limits make obstacles to flow visible, and whether "
                   "the team removes them through process improvement",
                   "Whether managers, not the team, set the limit",
                   "Whether work is measured in story points",
                   "Whether the limit is equal to the number of people on the "
                   "team"],
             "c": 0,
             "why": "The chapter says that WIP limits are no good if they do not "
                    "lead to improvements that increase flow, so the survey asked "
                    "about obstacles made visible and removed. It does not say "
                    "who sets the limit, how work is sized, or how the limit "
                    "relates to headcount."},
        ],
        "mistakes": [
            ("Thinking a WIP limit alone makes a team faster",
             "The authors say the opposite of what the practice's fame suggests: "
             "alone, they are a weak predictor of delivery performance. The "
             "strong effect comes with visual displays and a feedback loop from "
             "production monitoring, and with limits that expose obstacles the team "
             "then removes."),
            ("Reading the lab's drop in lead time as a promise",
             "The lab holds throughput fixed to show how Little's law divides, and "
             "on the lesson's invented team that gives 3 days instead of 9. A real "
             "team that cuts its work in progress may finish more or fewer items "
             "in a day; the figure is arithmetic on the sample stated."),
            ("Treating a board as visual management whatever is on it",
             "The authors look at what is shown, how broadly it is shared and how "
             "easy it is to reach: quality and productivity measures and defect "
             "rates, available to engineers and leaders alike. A board that "
             "shows status to one manager does not meet that description."),
        ],
        "standard": (
            "Finish when you can apply Little's law to a board.",
            "Given a log of items with start and done days, compute the average "
            "work in progress, the throughput and the average lead time, show "
            "that the law holds, and say what a limit assumes about throughput."
        ),
        "note": (
            "The lab applies a law of arithmetic to the numbers you give it. It "
            "cannot say whether your limit exposes an obstacle, whether anyone "
            "removes it, or whether throughput holds; those are what the authors "
            "measured, and the book reports them from its survey."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 7, Implement a Lightweight Change Management Process (PDF pp.
    # 114-117 of the operator's copy): the four scenarios (p. 115), the
    # results (p. 115), the recommendation (pp. 115-116), What About
    # Segregation of Duties? (pp. 116-117), why external approval is
    # problematic (p. 117).
    # Quotes: PDF p. 115 of the operator's copy, 21 words, quotes.py OK;
    # PDF p. 117, 3 words, quotes.py OK. Lesson total: 24 words.
    {
        "slug": "lightweight-change-management",
        "title": "A Lightweight Change Management Process",
        "module": "Chapter 7 · Management Practices for Software",
        "one_line": "Approval by an external body slowed teams down and did not make production more stable; the authors recommend peer review and a deployment pipeline.",
        "summary": (
            "The second half of Chapter 7 asks what change approval does. Read the "
            "four approval scenarios the authors asked about, what they found, "
            "their recommendation and their answer to regulated industries; then "
            "compute the wait and the change fail rate of each route in an "
            "invented sample, and see how little it takes to move a rate."
        ),
        "key": [
            "four approval scenarios, one question",
            "external approval: slower, not safer",
            "approval only for high-risk changes: no link",
            "peer review plus a deployment pipeline",
            "segregation of duties without a CAB",
            "outside teams govern, they do not inspect",
        ],
        "key_label": "Lightweight change management in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Change advisory board (CAB)",
             "A body outside the team that reviews each change to production "
             "before it goes live. The authors describe processes of this kind "
             "that take days or weeks, on top of the team's own reviews."),
            ("Peer review",
             "Review of a change by someone on the team who did not write it, "
             "such as through pair programming or an intrateam code review, "
             "paired in the authors' recommendation with a deployment pipeline "
             "that detects and rejects bad changes."),
            ("Change fail rate",
             "The share of changes that fail: that lead to degraded service or "
             "need remediation after release. It is one of the four delivery "
             "measures of Chapter 2, and the lab counts it for each route."),
        ],
        "read_title": "The chapter's question, its results, then the count",
        "read_intro": (
            "Read the section Implement a Lightweight Change Management Process, "
            "and the box on segregation of duties, in your own copy first. The "
            "lesson sets out the question and the findings, and then counts a "
            "sample of invented changes by approval route."),
        "body": [
            ("p", "Every organization has some process for changing production. In "
                  "a startup it may be calling another developer over to look at "
                  "your code before it goes live; in a large organization the "
                  "authors often see processes that take days or weeks and send "
                  "each change to a change advisory board, a CAB outside the team, "
                  "as well as the team's own reviews. The section asks what that "
                  "outside approval does to delivery performance."),
            ("p", "They put four scenarios to respondents and asked which fits: an "
                  "outside body such as a manager or CAB signs off every "
                  "production change; sign-off is needed only for risky changes "
                  "such as database ones; the team leans on peer review; or "
                  "nothing needs approval. The results, they say, were "
                  "surprising. Asking for approval of risky changes alone showed no "
                  "correlation with delivery performance. Teams with peer "
                  "review, or with no approval step, did better on it. And "
                  "teams that sent every change to an outside body did worse."),
            ("p", "They then asked whether external approval at least buys "
                  "stability. &ldquo;Approval by an external body (such as a "
                  "manager or CAB) simply doesn&rsquo;t work to increase the "
                  "stability of production systems,&rdquo; they conclude: it "
                  "did not help time to restore service, it showed no "
                  "correlation with change fail rate, and it slowed delivery down. "
                  "In the authors' view it is worse than having no approval "
                  "process at all. Note the strength of the claim: these are "
                  "correlations in a survey of perception, and the book's wording "
                  "is that outside approval is &ldquo;negatively correlated&rdquo; "
                  "with lead time, how often teams deploy, and restore time."),
            ("p", "Their recommendation is a light process built on review by "
                  "peers, as in pair programming or a code review inside the "
                  "team, with a deployment pipeline that catches and turns away "
                  "faulty changes. They apply it to every kind of change: "
                  "code, infrastructure and database. Chapters 4 and 5 describe "
                  "the pipeline."),
            ("p", "The box What About Segregation of Duties? answers the "
                  "objection from regulated industries. Segregation of duties is "
                  "required in some regulations, and by some auditors, and the "
                  "authors say it does not require a CAB or a separate operations "
                  "team. Two mechanisms satisfy both the letter and the spirit: "
                  "somebody who did not write the change reviews it, before or "
                  "just after commit, and logs the sign-off in a tool that keeps "
                  "the record, a pull request for instance; and changes reach production "
                  "only through a fully automated deployment pipeline, so that "
                  "nothing is applied that was not committed, validated by the "
                  "standard build and test, and deployed by the pipeline. The "
                  "pipeline leaves auditors a complete record of what was applied "
                  "where, from where, with which tests, and approved by whom."),
            ("p", "The section closes with the authors' reasoning, which they offer "
                  "as logic and not as a result. Software systems are complex, and "
                  "an external body unfamiliar with the internals cannot accurately "
                  "judge tens of thousands of changed lines from hundreds of "
                  "engineers; they call the practice &ldquo;risk management "
                  "theater&rdquo;, checking boxes so that one can say the process "
                  "was followed. They see a place for people outside teams, in a "
                  "governance role: monitoring delivery performance and helping "
                  "teams adopt practices known to improve stability, quality and "
                  "speed, not inspecting changes."),
            ("p", "Now the count, on twelve invented changes, six by peer review "
                  "and six by a CAB. A change is a name, a route, the hours it "
                  "waited for approval and whether it failed. The peer-reviewed "
                  "waits are 1, 2, 1, 3, 2 and 1 hours: 10 in all, a mean of "
                  "1.67 and a median of 1.5. The CAB waits are 48, 72, 96, 24, "
                  "72 and 120: 432 in all, a mean of 72 hours and a median of 72. "
                  "One change in each route failed, so each route's change fail "
                  "rate on the preset <code>one-failure</code> is 1 in 6, 16.7 "
                  "percent, and the difference between them is 0. That matches what the "
                  "authors report about external approval and change fail rate, "
                  "on a sample built to match it."),
            ("p", "The preset <code>two-failures</code> changes one record: a second "
                  "CAB change failed. The CAB's rate becomes 2 in 6, 33.3 percent, "
                  "and the difference 16.7 percentage points. One change moved the "
                  "rate by a sixth, and that is the lesson's second point: on a "
                  "route with six changes a rate is too coarse to separate the "
                  "routes, and a real comparison needs many changes. The authors' "
                  "figure comes from a survey of many teams, not from a count of "
                  "one team's changes."),
            ("h3", "Exercise"),
            ("ul", [
                "Twelve changes as name, route, wait in hours, failed: "
                "`x1, none, 0, no; x2, none, 0, yes; x3, none, 0, no; x4, none, 0, no`.",
                "`y1, peer, 2, no; y2, peer, 1, no; y3, peer, 3, yes; y4, peer, 1, no`.",
                "`z1, cab, 24, no; z2, cab, 48, no; z3, cab, 72, yes; z4, cab, 96, no`.",
            ]),
            ("p", "Find each route's change fail rate and the mean wait of the CAB "
                  "route and of the peer route, and then the extra hours a CAB "
                  "change waits on average over a peer-reviewed one. Enter the "
                  "twelve to check. Then say what the sample does not show."),
            ("p", "The authors' recommendation depends on the deployment pipeline "
                  "that Chapters 4 and 5 describe. The next lesson, Lean Product "
                  "Development Practices, turns from how changes are approved to "
                  "how the work is cut up and what it is for."),
        ],
        "lab": ("acckit", {
            "mode": "change",
            "view": "approval",
            "compare": "cab peer",
            "preset": "one-failure",
            "presets": [
                {"id": "one-failure",
                 "label": "Six peer-reviewed and six CAB changes, one failure each",
                 "changes": CHANGES_ONE,
                 "expect": {"acmRoutes": "2: peer (6), cab (6)", "acmMeanWait": "peer 1 h 40 min; cab 3 d", "acmMedianWait": "peer 1 h 30 min; cab 3 d", "acmFail": "peer 1/6 ≈ 16.7%; cab 1/6 ≈ 16.7%", "acmOverall": "1/6 ≈ 16.7%", "acmDiff": "cab 1/6 ≈ 16.7% against peer 1/6 ≈ 16.7%: 0 points"}},
                {"id": "two-failures",
                 "label": "The same twelve with a second CAB change failing",
                 "changes": CHANGES_TWO,
                 "expect": {"acmRoutes": "2: peer (6), cab (6)", "acmMeanWait": "peer 1 h 40 min; cab 3 d", "acmMedianWait": "peer 1 h 30 min; cab 3 d", "acmFail": "peer 1/6 ≈ 16.7%; cab 1/3 ≈ 33.3%", "acmOverall": "1/4 = 25%", "acmDiff": "cab 1/3 ≈ 33.3% against peer 1/6 ≈ 16.7%: ≈ +16.7 points"}},
            ],
            "panel_title": "Wait and change fail rate by approval route",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Comparing approval routes",
        "steps_intro": "Four steps, the last of them on changes of your own.",
        "steps": [
            ("Label each change with its route",
             "For each change in a period, write its name, the route it took "
             "(none, peer or CAB), the hours between asking for approval and "
             "getting it, and whether it failed."),
            ("Count and average by route",
             "For each route, count the changes, then compute the mean and median "
             "wait. The median is less moved by one very long wait."),
            ("Compute each route's fail rate",
             "Divide each route's failed changes by its changes. Write down how "
             "many changes it is, because a rate on a handful of changes moves a "
             "long way when one more fails."),
            ("Compare, and say what the sample cannot show",
             "Take the difference in wait and in fail rate between two routes on "
             "your own changes. Then list what else differs between them: the "
             "kind of change, the risk, the team."),
        ],
        "worked": {
            "title": "One failure in six",
            "intro": [
                "Compare the two routes of the preset <code>one-failure</code> by "
                "hand.",
            ],
            "lines": [
                "Peer waits: 1, 2, 1, 3, 2, 1 = 10 hours; mean 10/6 = 1.67",
                "Peer sorted: 1, 1, 1, 2, 2, 3; median (1 + 2)/2 = 1.5",
                "CAB waits: 48, 72, 96, 24, 72, 120 = 432 hours; mean 72",
                "CAB sorted: 24, 48, 72, 72, 96, 120; median (72 + 72)/2 = 72",
                "Peer fail rate: 1/6 = 16.7 percent",
                "CAB fail rate: 1/6 = 16.7 percent, a difference of 0",
            ],
            "after": [
                "Each route adds a wait and none of them shows a lower fail rate, "
                "which is the shape of the authors' finding on this sample. With "
                "a second CAB failure the rate would be 2/6, which is why six "
                "changes cannot carry a conclusion.",
            ],
        },
        "quiz_title": "Approval routes and the chapter's claims",
        "quiz": [
            {"q": "In the exercise, what is the mean wait of the CAB changes minus "
                  "the mean wait of the peer-reviewed ones?",
             "a": ["58.25 hours",
                   "60 hours",
                   "233 hours",
                   "58.5 hours"],
             "c": 0,
             "why": "The CAB waits are 24, 48, 72 and 96: 240 over 4, a mean of 60. "
                    "The peer waits are 2, 1, 3 and 1: 7 over 4, 1.75. The "
                    "difference is 58.25 hours. Sixty ignores the peer wait; 233 "
                    "is the numerator of the difference as a fraction, 233/4; and "
                    "58.5 subtracts the medians, 60 and 1.5."},
            {"q": "On the preset <code>two-failures</code>, what is the CAB route's "
                  "change fail rate?",
             "a": ["2 in 6, 33.3 percent",
                   "2 in 12, 16.7 percent",
                   "1 in 6, 16.7 percent",
                   "2 in 6, 16.7 percent"],
             "c": 0,
             "why": "Two of the six CAB changes failed. The second option divides by "
                    "all twelve changes, which is the overall rate and not the "
                    "route's; the third is the preset before the second failure; "
                    "the fourth is the right count with the wrong percentage."},
            {"q": "Which approval scenario did the authors find was not correlated "
                  "with software delivery performance?",
             "a": ["Approval only for high-risk changes, such as database "
                   "changes",
                   "Approval of every change by an external body",
                   "Reliance on peer review",
                   "No change approval process"],
             "c": 0,
             "why": "The authors report that approval limited to risky changes "
                    "showed no correlation with delivery performance. Teams with no "
                    "approval process or with peer review did better, and teams "
                    "requiring approval by an external body did worse."},
            {"q": "According to the chapter's box on segregation of duties, how can "
                  "the requirement be met without a CAB?",
             "a": ["Someone who did not write the change reviews and approves it in "
                   "a system of record, and changes reach production only through "
                   "an automated pipeline",
                   "The author of the change signs it off in the pipeline tool",
                   "A separate operations team applies each change by hand",
                   "The requirement cannot be met without external approval"],
             "c": 0,
             "why": "The authors name two mechanisms: review by somebody not "
                    "involved in authoring the change, recorded in a system such "
                    "as a pull request, and a fully automated deployment pipeline "
                    "as the only route to production. The other options keep the "
                    "author's own approval, a separate manual team, or the CAB."},
        ],
        "mistakes": [
            ("Concluding that the book says to have no review at all",
             "Teams with no approval process did well in the survey, but the "
             "authors' recommendation is a lightweight process: peer review, such "
             "as pair programming or code review inside the team, with a "
             "pipeline that catches faulty changes."),
            ("Believing a regulated industry has to keep its CAB",
             "The box on segregation of duties says the control can be met "
             "without a CAB or a separate operations team: by review from "
             "someone who did not write the change, recorded in a system of "
             "record, and by applying changes only through an automated "
             "pipeline that leaves a full record."),
            ("Reading the lab's sample as evidence about CABs",
             "The twelve changes are invented, and the equal fail rates were "
             "chosen to match what the authors report. With six changes a route, "
             "one failure moves a rate by about 17 points. The book's finding "
             "is a correlation across many teams in a survey, not a count of "
             "one team's changes."),
        ],
        "standard": (
            "Finish when you can compare approval routes by wait and fail rate.",
            "Given changes with route, wait and outcome, compute each route's mean "
            "and median wait and change fail rate, and say how few changes it "
            "takes for one failure to move a rate."
        ),
        "note": (
            "The lab counts changes you give it by route. It cannot tell whether "
            "the routes were given comparable changes, whether a long wait was "
            "the approval or the queue, or whether the CAB was the cause; the "
            "book reports a correlation in its survey and reasons about the rest."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 8 opening and Lean Product Development Practices (PDF pp.
    # 118-121 of the operator's copy): the opening on faux Agile and Lean
    # startup (p. 118-119), the four capabilities (p. 119), the findings
    # (pp. 119-120), the box Working in Small Batches (pp. 120-121), customer
    # feedback (p. 121). Do not quote the chapter's first sentence.
    # Quote: PDF p. 120 of the operator's copy, 12 words, quotes.py OK.
    # Lesson total: 12 words.
    {
        "slug": "lean-product-development",
        "title": "Lean Product Development Practices",
        "module": "Chapter 8 · Product Development",
        "one_line": "Cut the work into batches that finish in under a week, show the flow, ask customers, and the first feedback arrives sooner.",
        "summary": (
            "Chapter 8 turns from delivery to what is delivered. Read the four "
            "capabilities the authors call Lean product development, what they "
            "found about them, and what working in small batches is for; then "
            "compare when the first customer feedback arrives from one big "
            "release and from four small ones."
        ),
        "key": [
            "faux Agile: big projects, late feedback",
            "small batches, done in under a week",
            "see the flow of work to the customer",
            "seek customer feedback and use it",
            "teams change specifications themselves",
            "short lead times, faster feedback loops",
        ],
        "key_label": "Lean product development in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Small batch",
             "A slice of a product or feature that a team can finish inside a "
             "week and ship often. The authors set it against large features "
             "built on branches and shipped rarely."),
            ("Minimum viable product (MVP)",
             "A first version with only the features needed to learn, by testing "
             "it, whether the product and its business model are sound. It applies the idea of a "
             "small batch at the level of the whole product."),
            ("Time to first feedback",
             "In the lab, the time from the start until the first batch is done "
             "and released. It is the earliest moment a customer can answer "
             "anything, so it is what a batch size changes first."),
        ],
        "read_title": "The chapter's four capabilities, then the count",
        "read_intro": (
            "Read the opening of Chapter 8 and the section Lean Product "
            "Development Practices in your own copy first. The lesson sets out "
            "the four capabilities and then compares one release with four."
        ),
        "body": [
            ("p", "Chapter 8, Product Development, begins with a complaint. The "
                  "authors say Agile has largely won the argument over methods, "
                  "but a good deal of what organizations have adopted is faux "
                  "Agile: some of the practices without the culture and processes "
                  "around them. They give three signs: months spent on "
                  "budgets, analysis and requirements before work begins; work "
                  "gathered into large projects that ship rarely; and "
                  "customer feedback treated as an afterthought. Against that they "
                  "set the Lean approach to product development and the Lean startup "
                  "movement "
                  "of Eric Ries, which test a product's design and business "
                  "model from the start with frequent user research, drawing on "
                  "Steve Blank's work and on design thinking."),
            ("p", "The chapter then states a hypothesis. Practices such as "
                  "building and validating prototypes from the beginning, working "
                  "in small batches, and changing course, or pivoting, early and "
                  "often might affect organizational performance, which the "
                  "authors measure as productivity, market share and profitability. "
                  "They examined four capabilities that make up their model of a "
                  "Lean approach."),
            ("p", "The four are these. Teams cut products and features into "
                  "small batches, each finishable within a week and shipped "
                  "often, with MVPs among the means. Teams understand how work "
                  "flows from the business to customers and can see it, "
                  "including where each product and feature stands. The "
                  "organization asks customers for feedback, regularly, and "
                  "builds it into design. And teams can write and change "
                  "specifications as they go, on their own authority. The "
                  "last gets a lesson of its own."),
            ("p", "What they found: the factors were statistically significant "
                  "predictors of higher software delivery performance and of "
                  "organizational performance, and also of a better "
                  "organizational culture and less burnout. Because they ran the "
                  "research over several years, they also found that the "
                  "prediction runs the other way, from delivery performance to "
                  "Lean product management practices, a reciprocal relationship that they call a virtuous "
                  "cycle. The next lesson reads that finding with care."),
            ("p", "The box Working in Small Batches gives the reason for the first "
                  "capability. &ldquo;Working in small batches enables short lead "
                  "times and faster feedback loops,&rdquo; the authors write, and "
                  "the key is to break work into features that can be built "
                  "quickly, in place of elaborate ones grown on branches and "
                  "shipped seldom. It applies at the feature level and "
                  "the product level, where it is the MVP. The authors add that "
                  "software makes small batches especially valuable, because "
                  "users can answer quickly, through techniques such as A/B "
                  "testing, and that an experimental style of product work goes "
                  "closely with the technical practices behind continuous "
                  "delivery. Customer feedback, as they use the term, covers "
                  "collecting satisfaction metrics, asking customers how good the "
                  "products and features are, and using the answers in "
                  "design; whether teams have the authority to respond turns "
                  "out to matter too."),
            ("p", "Now the count. The lab takes a number of work items, the "
                  "size of a batch, the time each item takes and the fixed time "
                  "each release costs, and says when the first batch is out, when "
                  "the last is, and how much of the time went to releasing. The "
                  "team is invented: twelve items of one day each, and a release "
                  "that costs 2 days, by hand. On the preset <code>by-hand</code> "
                  "one batch of 12 means one release: the first and last feedback "
                  "both arrive on day 14, and 2 days went to releasing. Four "
                  "batches of 3 mean the first feedback on day 5, 3 days of work "
                  "and the 2 of the release, the last on day 20, and 8 days of "
                  "release time in all. Two more tiles compare the plans. "
                  "The average wait per item, from the start to its release, "
                  "is 14 days for the one batch and 12.5 for the four (the "
                  "batches wait 5, 10, 15 and 20 days, which averages to "
                  "that), and the first feedback comes 14/5, about 2.8 times "
                  "sooner."),
            ("p", "The numbers show a cost as well as a gain, and the chapter does "
                  "not hide it: small batches finish later in total when each "
                  "release is costly. The preset <code>automated</code> makes the "
                  "release cost half a day, as a deployment pipeline would. One "
                  "batch of 12 now arrives on day 12.5. Four batches of 3 bring the "
                  "first feedback on day 3.5, the last on day 14, with 2 days of "
                  "release time. This is why the authors link small batches to the "
                  "technical practices of Chapters 4 and 5: they cut the price of "
                  "a release, which makes small batches affordable."),
            ("h3", "Exercise"),
            ("ul", [
                "Ten items of one day each; a release costs 3 days.",
                "Compare one batch of 10 with five batches of 2.",
            ]),
            ("p", "Find the day the first feedback arrives, the day the last does and "
                  "the days spent releasing, for both. Then say which of the two "
                  "plans a cheaper release would help more, and what that tells "
                  "you about the practices behind a cheap release. Enter the "
                  "records to check."),
            ("p", "The first three capabilities are about the work; the fourth is "
                  "about who may change it. The next lesson, Team Experimentation "
                  "and Effective Product Management, reads it, and the finding "
                  "that delivery and product practices drive each other."),
        ],
        "lab": ("acckit", {
            "mode": "flow",
            "view": "batch",
            "preset": "by-hand",
            "presets": [
                {"id": "by-hand",
                 "label": "Twelve items, a release costing two days, one batch or four",
                 "work": "12",
                 "batch": "12, 3",
                 "per_item": "1",
                 "release_cost": "2",
                 "expect": {"aflBatches": "1 of 12 → 4 of 3", "aflFirst": "14 days → 5 days", "aflLast": "14 days → 20 days", "aflWait": "14 days → 25/2 = 12.50 days", "aflOverhead": "2 days → 8 days", "aflRatio": "14/5 ≈ 2.8×"}},
                {"id": "automated",
                 "label": "The same work, with a release costing half a day",
                 "work": "12",
                 "batch": "12, 3",
                 "per_item": "1",
                 "release_cost": "1/2",
                 "expect": {"aflBatches": "1 of 12 → 4 of 3", "aflFirst": "25/2 = 12.50 days → 7/2 = 3.50 days", "aflLast": "25/2 = 12.50 days → 14 days", "aflWait": "25/2 = 12.50 days → 35/4 = 8.75 days", "aflOverhead": "1/2 = 0.50 days → 2 days", "aflRatio": "25/7 ≈ 3.6×"}},
            ],
            "panel_title": "When the first feedback arrives",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Timing the first feedback",
        "steps_intro": "Four steps, the last of them on work of your own.",
        "steps": [
            ("State the work and the costs",
             "Count the items, the time each takes and the fixed time one release "
             "costs, all in the same unit. Say where each came from."),
            ("Cut it into batches",
             "Divide the items by the batch size to get the number of batches, "
             "which is the number of releases."),
            ("Time the feedback",
             "The first feedback arrives after one batch's work plus one release. "
             "The last arrives after every batch's work and every release."),
            ("Change the release cost",
             "Recompute with a cheaper release, then on your own project with the "
             "real figures. Write down which practices would make the release "
             "cheap enough."),
        ],
        "worked": {
            "title": "One batch of twelve against four of three",
            "intro": [
                "Work the preset <code>by-hand</code>: twelve items, a day each, "
                "and a release costing 2 days.",
            ],
            "lines": [
                "One batch of 12: work 12 + release 2 = day 14, first and last",
                "Release time: 1 release x 2 = 2 days",
                "Four batches of 3: one batch = 3 + 2 = 5 days",
                "First feedback: day 5",
                "Last feedback: 4 x 5 = day 20",
                "Release time: 4 releases x 2 = 8 days",
            ],
            "after": [
                "Small batches bring the first feedback 9 days sooner and the last "
                "6 days later, at four times the release time. With the "
                "half-day release the last arrives on day 14, only 1.5 days "
                "after the single batch.",
            ],
        },
        "quiz_title": "Batches, feedback and the chapter's four capabilities",
        "quiz": [
            {"q": "In the exercise, ten items of one day each and a release "
                  "costing 3 days, on which day does the first feedback arrive "
                  "from five batches of 2?",
             "a": ["Day 5",
                   "Day 2",
                   "Day 13",
                   "Day 25"],
             "c": 0,
             "why": "One batch is 2 days of work plus a release of 3: day 5. Day 2 "
                    "forgets the release, day 13 is the single batch of 10, and "
                    "day 25 is when the last of the five batches arrives, 5 x 5."},
            {"q": "On the preset <code>by-hand</code>, how many days of release time "
                  "do four batches of 3 spend?",
             "a": ["8 days",
                   "2 days",
                   "5 days",
                   "20 days"],
             "c": 0,
             "why": "Four releases at 2 days each is 8. Two days is the single "
                    "batch's release; 5 is the time to the first feedback; 20 is "
                    "the day the last batch arrives."},
            {"q": "In Chapter 8, how long should a small batch take to complete?",
             "a": ["Less than a week",
                   "Less than a day",
                   "Less than a month",
                   "Whatever the team estimates"],
             "c": 0,
             "why": "The first capability is about cutting products and features "
                    "into batches small enough to finish within a week and ship "
                    "often, with MVPs among the means."},
            {"q": "How does the chapter define a minimum viable product?",
             "a": ["A prototype with just enough features to allow validated "
                   "learning about the product and its business model",
                   "The first release of a finished product",
                   "A feature released behind a switch",
                   "The smallest team that can ship a product"],
             "c": 0,
             "why": "In the box on small batches the authors describe an MVP as a "
                    "prototype built to test the product and its business model, "
                    "with only the features that takes."},
        ],
        "mistakes": [
            ("Thinking Agile ceremonies make a team Lean in its product work",
             "The chapter opens by calling much of what has been implemented faux "
             "Agile: following some common practices without addressing the wider "
             "culture and processes. Months of requirements before work starts, "
             "big projects with infrequent releases and feedback as an afterthought "
             "are the signs it names."),
            ("Expecting smaller batches to finish the whole job sooner",
             "The lab's four batches bring the first feedback earlier and the "
             "last later, because each batch carries a release. The gain is in "
             "feedback, not in the total, and it depends on the release being "
             "cheap, which is why the authors tie the practice to the technical "
             "practices of continuous delivery."),
            ("Reading a lab figure as the authors' finding about batch size",
             "The days are arithmetic on invented work, with release costs the "
             "lesson chose. The authors report that the capabilities predict "
             "delivery and organizational performance in their survey; they do not "
             "give a time to feedback for any batch size."),
        ],
        "standard": (
            "Finish when you can time the first feedback from different batch sizes.",
            "Given a number of items, the time per item, a batch size and a release "
            "cost, compute when the first and the last feedback arrive and how "
            "much time went to releasing."
        ),
        "note": (
            "The lab times batches from the numbers you give it. It cannot tell you "
            "whether customers will answer, whether the feedback will be used, or "
            "whether the work divides into batches of that size; the authors "
            "measured those by survey."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 8, Team Experimentation (PDF pp. 121-122 of the operator's
    # copy) and Effective Product Management Drives Performance (pp.
    # 122-124): the quotation, the caution about experimentation,
    # the 2016-2017 analysis (p. 122), the flipped model the following year
    # and the reciprocal model (p. 123), the closing (pp. 123-124).
    # Quote: PDF p. 122 of the operator's copy, 27 words, quotes.py OK.
    # Lesson total: 27 words.
    # F3 (p. 122): the analysis covered two years, 2016-2017; the first model
    # had Lean product management predict delivery performance, the second,
    # the following year, had delivery performance predict it.
    {
        "slug": "team-experimentation-and-product-management",
        "title": "Team Experimentation and Effective Product Management",
        "module": "Chapter 8 · Product Development",
        "one_line": "Teams free to change specifications without outside approval, and a reciprocal model in which product and delivery practices each predict the other.",
        "summary": (
            "The close of Chapter 8 makes two claims. Read what the authors say "
            "about letting teams experiment, why they hedge it, and how two years "
            "of analysis led them to a reciprocal model; then compute a "
            "correlation between a lean-product score and a delivery score, and "
            "see why it cannot say which drives which."
        ),
        "key": [
            "teams may change the specification",
            "experiment with small batches and feedback",
            "predicts profit, productivity, market share",
            "2016: product practice predicts delivery",
            "2017: delivery predicts product practice",
            "r is symmetric: it names no direction",
        ],
        "key_label": "Team experimentation in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Team experimentation",
             "Teams being free to test new ideas and to write and revise "
             "specifications as they build, without sign-off from outside. "
             "The authors say it works together with small "
             "batches, visible flow and customer feedback."),
            ("Reciprocal model",
             "The authors' name for the combination of two models run in "
             "successive years: Lean product management practices predicting "
             "software delivery performance, and delivery performance predicting "
             "those practices, which they also call a virtuous cycle."),
            ("Pearson's r",
             "A number from -1 to 1 for how closely two scores move together in a "
             "sample: the sum of the products of the two deviations from the "
             "means, over the square root of the product of the two sums of "
             "squares. Its square is the share of the variation the two scores "
             "share."),
        ],
        "read_title": "The chapter's last two sections, then the count",
        "read_intro": (
            "Read the sections Team Experimentation and Effective Product "
            "Management Drives Performance in your own copy first. The lesson sets "
            "out the claims and then computes a correlation on a sample of "
            "invented teams."),
        "body": [
            ("p", "The first of the chapter's last two sections is about "
                  "autonomy. Many teams in organizations that call themselves Agile "
                  "still have to follow requirements created by other teams, the "
                  "authors write, which can produce products that do not delight "
                  "customers or deliver the expected results. Agile means seeking "
                  "input from customers throughout, early included; if a team "
                  "cannot alter what it is building as it learns, without a nod "
                  "from outside, its capacity to innovate is sharply reduced."),
            ("p", "Their finding: &ldquo;the ability of teams to try out new ideas "
                  "and create and update specifications during the development "
                  "process, without requiring the approval of people outside the "
                  "team&rdquo;, they write, matters for organizational "
                  "performance, measured by profitability, productivity and "
                  "market share. The authors say at once what they do not "
                  "propose: letting developers chase any idea they fancy. "
                  "Experimentation has to go with the other capabilities, small "
                  "batches, making the flow of work visible to "
                  "everyone and building customer feedback into the design, so that "
                  "choices are informed and the decisions are shared across the "
                  "organization."),
            ("p", "The second section is about the order of cause. The authors "
                  "analysed Lean product management over two years, 2016 and "
                  "2017. In the first model Lean product management practices "
                  "positively impacted software delivery performance, stimulated a "
                  "generative culture and decreased burnout. In the following year "
                  "they turned the model round and confirmed that delivery "
                  "performance, in its turn, predicts those practices. Combined "
                  "across years it is a reciprocal model, a virtuous cycle, and "
                  "the practices predict organizational performance too."),
            ("p", "Read that as the authors do and with care. The word is "
                  "predict, which in a survey is a statistical relationship "
                  "tested in a model, once in each direction, with a year between; "
                  "and the measures are perceptions. It supports the "
                  "claim that each goes with the other. The authors say the "
                  "reciprocal relationship is suggested by the literature; what "
                  "carries the claim is two years of analysis, which the number "
                  "from a single correlation cannot. "
                  "Chapter 12 and The Science Behind the Book take up what the book argues about "
                  "cause."),
            ("p", "Now the count. The lab takes a name and two scores for each "
                  "team and computes Pearson's r. The sample is eight invented "
                  "teams, each scored from 1 to 7 on lean product practice and on "
                  "delivery, as in the preset <code>lean-first</code> with lean "
                  "as x and delivery as y: 2 and 3, 3 and 2, 4 and 5, 4 and 4, "
                  "5 and 5, 6 and 5, 3 and 4, 5 and 4. Both means are 4. The "
                  "products of the deviations sum to 7, the lean scores' squared "
                  "deviations to 12 and the delivery scores' to 8, so r is "
                  "7 over the square root of 96, about 0.714, and r squared is "
                  "49 over 96, about 51.0 percent."),
            ("p", "The preset <code>delivery-first</code> puts the same eight "
                  "teams' scores in the other order, delivery as x and lean as "
                  "y. The r is the same, 0.714: it is symmetric, and so cannot "
                  "tell which drives which. What changes is the least-squares "
                  "line the lab also prints. With lean as x it has a slope of "
                  "7 over 12, about 0.583, and an intercept of 5 over 3, about "
                  "1.667; with delivery as x, a slope of 7 over 8, 0.875, and an "
                  "intercept of 0.5. The tile for sign and strength reads "
                  "positive and strong, by cut-offs the lab states (0.3 and 0.7) "
                  "and the book does not: they are a convention, and 0.714 is "
                  "just over the second. Each line predicts one score from the "
                  "other, and neither says one score moves the other. To split the "
                  "directions the authors needed other designs: theory, and two "
                  "years of data."),
            ("h3", "Exercise"),
            ("ul", [
                "Five invented teams as name, lean score, delivery score:",
                "`u1, 1, 2; u2, 2, 1; u3, 3, 3; u4, 4, 5; u5, 5, 4`.",
            ]),
            ("p", "Find both means, the three sums that Pearson's r needs, r, and "
                  "r squared as a percentage. Then swap the two columns and say "
                  "what changes. Enter the records into the lab to check."),
            ("p", "This course ends here. The next course, Sustainable Work, "
                  "Satisfaction and Leadership, begins with Chapter 9 and the "
                  "authors' measures of burnout and work, which this one has met "
                  "only as an effect."),
        ],
        "lab": ("acckit", {
            "mode": "stats",
            "view": "pearson",
            "preset": "lean-first",
            "presets": [
                {"id": "lean-first",
                 "label": "Eight teams: lean-product score, then delivery score",
                 "pairs": TEAMS_LEAN_FIRST,
                 "expect": {"astN": "8", "astMeans": "x̄ = 4, ȳ = 4", "astR": "≈ 0.714", "astR2": "49/96 ≈ 51.0%", "astLine": "y = 5/3 ≈ 1.667 + 7/12 ≈ 0.583·x", "astWords": "positive, strong"}},
                {"id": "delivery-first",
                 "label": "The same eight teams, delivery score first",
                 "pairs": TEAMS_DELIVERY_FIRST,
                 "expect": {"astN": "8", "astMeans": "x̄ = 4, ȳ = 4", "astR": "≈ 0.714", "astR2": "49/96 ≈ 51.0%", "astLine": "y = 0.5 + 0.875·x", "astWords": "positive, strong"}},
            ],
            "panel_title": "Pearson's r between two scores",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Computing a correlation, and reading it",
        "steps_intro": "Four steps, the last of them on scores of your own.",
        "steps": [
            ("Pair the scores",
             "For each team, write the two scores side by side on the same scale. "
             "Say how each was measured and by whom."),
            ("Find the means and deviations",
             "Compute each score's mean, then each team's deviation from it. "
             "Check that each column of deviations sums to zero."),
            ("Compute the three sums, then r",
             "Sum the products of the deviations, and each score's squared "
             "deviations. Divide the first by the square root of the product of "
             "the other two. Square it for the share of variation shared."),
            ("Swap the columns and ask what is left",
             "Swap x and y and recompute. r is unchanged. Write down what you "
             "would need beyond this number, such as an order in time or an "
             "intervention, to say which score drives which."),
        ],
        "worked": {
            "title": "A correlation of 0.714",
            "intro": [
                "Compute r for the preset <code>lean-first</code>: eight teams, "
                "means of 4 and 4.",
            ],
            "lines": [
                "Lean deviations: -2, -1, 0, 0, 1, 2, -1, 1",
                "Delivery deviations: -1, -2, 1, 0, 1, 1, 0, 0",
                "Sum of products: 2 + 2 + 0 + 0 + 1 + 2 + 0 + 0 = 7",
                "Lean squares: 4 + 1 + 0 + 0 + 1 + 4 + 1 + 1 = 12",
                "Delivery squares: 1 + 4 + 1 + 0 + 1 + 1 + 0 + 0 = 8",
                "r = 7 / the square root of 12 x 8 = 7 / 9.798 = 0.714",
                "r squared = 49 / 96 = 51.0 percent",
            ],
            "after": [
                "Nothing in these sums knows which column is the cause: swap them "
                "and the sum of products and the two sums of squares are the "
                "same three numbers.",
            ],
        },
        "quiz_title": "Experimentation, the reciprocal model and r",
        "quiz": [
            {"q": "In the exercise, what is Pearson's r for the five teams, and "
                  "what share of the variation do the scores share?",
             "a": ["0.8, and 64 percent",
                   "0.8, and 80 percent",
                   "0.64, and 64 percent",
                   "0.5, and 25 percent"],
             "c": 0,
             "why": "Both means are 3. The sum of products is 8 and each sum of "
                    "squares is 10, so r is 8 over 10, 0.8, and r squared is "
                    "0.64: 64 percent. Eighty percent mistakes r for the share; "
                    "0.64 is the share used as r; the last is not the data."},
            {"q": "On the preset <code>delivery-first</code>, r is computed with "
                  "delivery as x and lean as y. What happens to r compared with "
                  "<code>lean-first</code>?",
             "a": ["It is the same, about 0.714",
                   "It falls, because delivery is the effect",
                   "It rises, because delivery is the cause",
                   "It changes sign"],
             "c": 0,
             "why": "The sum of products and the two sums of squares are the same "
                    "three numbers whichever column is x, so r is symmetric. The "
                    "least-squares line changes; r does not."},
            {"q": "How did the authors arrive at the reciprocal model of Lean "
                  "product management and delivery performance?",
             "a": ["One year's model had product practices predict delivery; the "
                   "following year's flipped model had delivery predict the "
                   "practices; combined, they are reciprocal",
                   "A single correlation, which they read in both directions",
                   "An experiment that assigned teams to practices at random",
                   "Interviews with teams that had adopted both"],
             "c": 0,
             "why": "The chapter says the analysis ran over two years, 2016 to 2017: "
                    "a first model, then the following year the flipped model, "
                    "and the two combined give the reciprocal model. A single "
                    "correlation cannot show direction; the chapter describes "
                    "neither an experiment nor interviews as its basis."},
            {"q": "According to the section on team experimentation, what does "
                  "the ability of teams to change specifications without outside "
                  "approval predict?",
             "a": ["Organizational performance, measured by profitability, "
                   "productivity and market share",
                   "Only a team's own satisfaction",
                   "Change fail rate, and nothing else",
                   "Nothing, unless a CAB reviews the result"],
             "c": 0,
             "why": "The authors say it matters for organizational performance, "
                    "which they measure by profitability, productivity and market "
                    "share, when combined with the other capabilities. They do not tie it to change fail rate."},
        ],
        "mistakes": [
            ("Reading the reciprocal model as proof that each practice causes the other",
             "The authors' words are predicts and drives, from models run on two "
             "years of survey data and argued from theory. It is the design, not a "
             "single correlation, that supports the virtuous cycle, and the "
             "measures are perceptions."),
            ("Believing teams should be free to try anything",
             "The authors say they do not propose letting developers chase any "
             "idea they fancy. Experimentation is combined with "
             "small batches, visible flow and customer feedback, so that choices "
             "are informed and shared."),
            ("Treating a high r as a statement about direction",
             "r is symmetric: the sample's 0.714 is the same whichever score is "
             "called x. It says the scores move together in the eight teams; "
             "that a third thing drives both, or that the order runs the other "
             "way, would give the same number."),
        ],
        "standard": (
            "Finish when you can compute a correlation and say what it leaves out.",
            "Given pairs of scores, compute Pearson's r and r squared, show that "
            "swapping the scores leaves r unchanged, and say what the authors "
            "used beyond a correlation to argue for a reciprocal relationship."
        ),
        "note": (
            "The lab computes r on the pairs you give it. It cannot tell whether "
            "the scores measure what their names say, whether the teams are "
            "typical, or which way the effect runs; the authors argue those from "
            "their design, and the book states the limits of a survey."
        ),
    },
]
