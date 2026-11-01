"""Technical Practices and Architecture, lessons 6-7 -- the rest of Chapter 5.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 5, Architecture (Focus on
Deployability and Testability, from the 2017 analysis and Conway's law; A
Loosely Coupled Architecture Enables Scaling; Allow Teams to Choose Their Own
Tools; Architects Should Focus on Engineers and Outcomes, Not Tools or
Technologies). Pages in the comments are PDF pages of the operator's copy; the
lessons cite by chapter and section. Every quotation is copied from that copy
and checked with quotes.py. The samples are invented for these lessons: none
of the book's figures, tables, survey items or data is reproduced. The design
is docs/accelerate/PLAN.md, section C, Course 3.
"""

_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)

# ---------------------------------------------------------------- 06 samples

# Three invented organizations over twenty working days: org, developers,
# deploys. The three presets are three shapes the rate can take.
RISING_ORGS = "small, 5, 40; medium, 20, 190; large, 80, 1000"
HOLDING_ORGS = "small, 5, 50; medium, 20, 200; large, 80, 800"
FALLING_ORGS = "small, 5, 60; medium, 20, 200; large, 80, 640"
# 06 exercise: ten days.
TEN_DAY_ORGS = "a, 4, 20; b, 16, 64; c, 64, 160"

# ---------------------------------------------------------------- 07 samples

# A system of seven services owned by four teams; a shared library forces
# three of the ties.
SERVICES = "billing, invoices, signup, referrals, reports, export, gateway"
SERVICE_TEAMS = (
    "billing, payments; invoices, payments; signup, growth; "
    "referrals, growth; reports, data; export, data; gateway, platform"
)
LOCKSTEP_TIES = (
    "billing, invoices; signup, referrals; reports, export; "
    "billing, signup; signup, reports; reports, gateway"
)
PINNED_TIES = "billing, invoices; signup, referrals; reports, export"
LOCKSTEP_REMOVE = "signup, reports"


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Conway's law and the inverse Conway maneuver (PDF pp. 98-99 of the
    # operator's copy); A Loosely Coupled Architecture Enables Scaling (pp.
    # 99-102): deploys per developer per day (pp. 100-101, Figure 5.1 in
    # prose), the three trends (p. 101).
    # Quote: PDF p. 98 of the operator's copy, 19 words (Conway 1968, as
    # the authors quote him), quotes.py LOOSE only for the ellipsis the
    # authors themselves print.
    # Lesson total: 19 words.
    {
        "slug": "loosely-coupled-architecture-enables-scaling",
        "title": "A Loosely Coupled Architecture Enables Scaling",
        "module": "Chapter 5 · Architecture",
        "one_line": "Conway's law, the inverse Conway maneuver, and the one measure the authors use to ask whether a bigger team must be a slower one.",
        "summary": (
            "The two sections of Chapter 5 that connect structure to growth: "
            "how architecture and team structure copy one another, and what "
            "happens to deploys per developer per day as an organization "
            "grows. Then compute that rate for three invented organizations and "
            "say whether it rises, holds or falls."
        ),
        "key": [
            "organizations copy their communication",
            "evolve the teams to get the architecture",
            "teams that need not coordinate to ship",
            "cross-functional teams, loosely coupled",
            "deploys per developer per day",
            "high performers' rate rose with size",
            "orthodoxy says individual output falls",
        ],
        "key_label": "Scaling in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Conway's law",
             "Melvin Conway's observation of 1968 that organizations which design "
             "systems produce designs that copy the communication structures of "
             "the organizations. Seen from the other side, the structure of the "
             "teams shapes the structure of the system."),
            ("Inverse Conway maneuver",
             "The practice of evolving the team and organizational structure "
             "in order to get the architecture you want, instead of letting the "
             "existing structure dictate it."),
            ("Deploys per developer per day",
             "The authors' measure of productivity for this chapter: the number "
             "of deployments in a period, divided by the developers and by the "
             "days. The lab works it out exactly for each organization you type."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read the rest of Focus on Deployability and Testability, from the "
            "2017 findings onward, and then A Loosely Coupled Architecture "
            "Enables Scaling in your own copy first. The lesson sets out the "
            "argument and then works the one measure the chapter uses."
        ),
        "body": [
            ("p", "Melvin Conway wrote in 1968 that &ldquo;organizations which "
                  "design systems . . . are "
                  "constrained to produce designs which are copies of the "
                  "communication structures of these organizations,&rdquo; as "
                  "Forsgren, Humble and Kim "
                  "quote him in Chapter 5, and it is the bridge in their "
                  "argument from architecture to organization. They ask what "
                  "sort of architecture a team needs in order to deliver without "
                  "waiting on anyone, and they answer from their 2017 survey."),
            ("p", "In teams that scored highly on the architectural "
                  "capabilities, little communication was needed between "
                  "delivery teams to get work done, and the system let teams "
                  "test, deploy and change their parts without depending on "
                  "other teams. The authors conclude that architecture and teams "
                  "are loosely coupled, and add that delivery teams must be "
                  "cross-functional, with the skills to design, build, test, "
                  "deploy and run the system. Their research, they say, supports "
                  "the idea called the inverse Conway maneuver: evolve "
                  "the team and organization structure to achieve the "
                  "architecture you want, so that teams can get from design to "
                  "deployment without high-bandwidth communication with other "
                  "teams."),
            ("p", "Ways to do it include bounded contexts and APIs to split a "
                  "large domain into smaller, loosely coupled units, and test "
                  "doubles and virtualization to test a service on its own. The "
                  "Domain-Driven Design read-along's lesson \"Bounded Context\" "
                  "teaches the first. The authors repeat their earlier caution "
                  "that service-oriented and microservice designs must be strict "
                  "about independence to deliver it. They also say what they do "
                  "not mean: DevOps is about better collaboration, and the aim "
                  "of loose coupling is that the available communication "
                  "bandwidth is not swamped by fine-grained decisions about "
                  "implementation, so it can be spent on higher-level shared "
                  "goals."),
            ("p", "The next section says what is gained. With a loosely "
                  "coupled, well-encapsulated architecture and a matching "
                  "organization, the authors expect two things: better delivery "
                  "performance, with tempo and stability both up and burnout and "
                  "deployment pain down; and the ability to grow the engineering "
                  "organization and raise productivity linearly or better as it "
                  "grows. For the second they build a measure from their data: "
                  "the number of deploys each developer makes in a day. The "
                  "orthodox view of growing a software team is that adding people "
                  "may raise total output but lowers each person's, because of "
                  "communication and integration overheads."),
            ("p", "Figure 5.1 plots the measure against the number of "
                  "developers for the respondents who deploy at least once a day. "
                  "The authors report three trends as the number of "
                  "developers grows. Low performers deploy less often per "
                  "developer, medium performers just as often, and high "
                  "performers significantly more often. "
                  "They credit what predicts high performance: a "
                  "generative culture, a modular architecture, the engineering "
                  "practices of continuous delivery, and good "
                  "leadership. Those, they argue, let a business move faster as "
                  "it adds people instead of slower."),
            ("p", "A reader who remembers Chapter 2's objection to output "
                  "measures may pause here. A deploy is a count of something done, "
                  "not of value delivered; the chapter treats it as the productivity "
                  "metric and does not take up the question. That is a limit to "
                  "carry with the finding, along with its sample: only "
                  "respondents who deploy at least daily appear in the figure, "
                  "and the three trends are the survey's description of them."),
            ("p", "Now the count. The lab takes a number of days and, for each "
                  "organization, its developers and its deploys, and gives deploys "
                  "per developer per day exactly, ordered by size, with whether "
                  "the rate rises, holds or falls from the smallest to the largest. "
                  "The organizations are invented for this lesson, and the three "
                  "presets are three shapes, not three kinds of performer. In "
                  "<code>rising</code>, over 20 days, the small organization of "
                  "5 developers makes 40 deploys, a rate of 2/5 (0.4); the "
                  "medium one of 20 makes 190, 19/40 (0.475); the large one of 80 "
                  "makes 1,000, 5/8 (0.625). The rate rises with size."),
            ("p", "In <code>holding</code> the same three sizes make 50, 200 and "
                  "800 deploys: 1/2 a deploy per developer per day each time. In "
                  "<code>falling</code> they make 60, 200 and 640: 3/5, 1/2 and "
                  "2/5. The first echoes the chapter's report for medium "
                  "performers and the second its report for low performers. The "
                  "lab counts three organizations and says "
                  "which shape they make; it cannot say whether any real "
                  "organization of those sizes would, or why. Total deploys "
                  "rise in all three presets, so what is at stake is the share "
                  "each developer carries, not whether the organization ships "
                  "more."),
            ("h3", "Exercise"),
            ("ul", [
                "Ten days. Organizations as `name, developers, deploys`: `a, 4, "
                "20; b, 16, 64; c, 64, 160`.",
            ]),
            ("p", "Work out each organization's deploys per developer per day, "
                  "say whether the rate rises, holds or falls from the smallest to "
                  "the largest, and type the records into the lab to check "
                  "you. Then say what would have to be true of the largest "
                  "organization for the rate to hold, and what in the chapter's "
                  "account would predict it."),
            ("p", "The next lesson, Allow Teams to Choose Their Own Tools, reads "
                  "the last two sections of the chapter, on tools and on the "
                  "architects who help choose them."),
        ],
        "lab": ("acckit", {
            "mode": "release",
            "view": "scaling",
            "preset": "rising",
            "presets": [
                {"id": "rising",
                 "label": "Three sizes of organization, deploys per developer rising",
                 "days": "20",
                 "orgs": RISING_ORGS,
                 "expect": {
                     "arlRates": "small (5 developers): 2/5 = 0.400; medium (20 developers): 19/40 = 0.475; large (80 developers): 5/8 = 0.625",
                     "arlTrend": "from small to large, the rate rises at every step"
                 }},
                {"id": "holding",
                 "label": "The same sizes, deploys per developer holding",
                 "days": "20",
                 "orgs": HOLDING_ORGS,
                 "expect": {
                     "arlRates": "small (5 developers): 1/2 = 0.500; medium (20 developers): 1/2 = 0.500; large (80 developers): 1/2 = 0.500",
                     "arlTrend": "from small to large, the rate holds: the same at every size"
                 }},
                {"id": "falling",
                 "label": "The same sizes, deploys per developer falling",
                 "days": "20",
                 "orgs": FALLING_ORGS,
                 "expect": {
                     "arlRates": "small (5 developers): 3/5 = 0.600; medium (20 developers): 1/2 = 0.500; large (80 developers): 2/5 = 0.400",
                     "arlTrend": "from small to large, the rate falls at every step"
                 }},
            ],
            "panel_title": "Deploys per developer per day, by size",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Working out a rate by size",
        "steps_intro": "Four steps, the last of them on organizations you know.",
        "steps": [
            ("Fix the period",
             "Choose the number of days and use it for every organization, "
             "counting working days if that is how you deploy."),
            ("Work out each rate",
             "Divide the deploys by the developers, then by the days. Keep it "
             "as a fraction to compare exactly."),
            ("Order by size and compare",
             "Put the organizations in order of developers and see whether "
             "the rate rises, holds or falls from the smallest to the largest."),
            ("Do it on organizations you know",
             "Take the deploy counts and headcounts of two or three teams of "
             "different sizes over the same period, and type them in. Write "
             "down one thing other than size that differs between them."),
        ],
        "worked": {
            "title": "Three organizations rising",
            "intro": [
                "Work out <code>rising</code>: 20 days, three organizations.",
            ],
            "lines": [
                "small: 40 / (5 x 20) = 40/100 = 2/5",
                "medium: 190 / (20 x 20) = 190/400 = 19/40",
                "large: 1,000 / (80 x 20) = 1,000/1,600 = 5/8",
                "2/5 = 0.400, 19/40 = 0.475, 5/8 = 0.625",
                "0.400 < 0.475 < 0.625: rises with size",
            ],
            "after": [
                "Each rate is the total deploys over the developers and the days "
                "at once. Dividing by only one of them gives deploys per "
                "developer, or deploys per day, which are different numbers.",
            ],
        },
        "quiz_title": "Rates, trends and Conway",
        "quiz": [
            {"q": "In the preset <code>rising</code>, how many deploys per "
                  "developer per day does the medium organization (20 developers, "
                  "190 deploys, 20 days) make?",
             "a": ["9.5", "0.95", "4.75", "0.475"],
             "c": 3,
             "why": "190 over 20 developers over 20 days is 190/400, which is 0.475. "
                    "9.5 divides by 20 once (deploys per day for the whole "
                    "organization, or per developer for the whole period); 0.95 "
                    "divides by 20 and 10; and 4.75 divides by 40 once."},
            {"q": "In the exercise (10 days; a: 4 developers, 20 deploys; b: 16, "
                  "64; c: 64, 160), what is the largest organization's rate?",
             "a": ["1/4", "1/2", "2/5", "5/2"],
             "c": 0,
             "why": "160 over 64 developers over 10 days is 160/640, which is "
                    "1/4. 1/2 is organization a's rate and 2/5 is b's; 5/2 is "
                    "160 over 64 without the days. The rate falls from a to c."},
            {"q": "In Figure 5.1's trends, how do the authors say medium "
                  "performers' deploys per developer change as the number of "
                  "developers rises?",
             "a": ["They decrease",
                   "They stay at a constant frequency",
                   "They increase significantly",
                   "The authors give no trend for them"],
             "c": 1,
             "why": "The chapter gives all three: low performers decreasing, "
                    "medium performers constant, high performers significantly "
                    "increasing. Decreasing is the low performers' trend and "
                    "increasing significantly the high performers'."},
            {"q": "What does the chapter say the inverse Conway maneuver advises?",
             "a": ["Redesigning the architecture to copy the current org chart",
                   "Keeping teams from communicating with one another",
                   "Changing how teams and the organization are structured so "
                   "as to get the architecture wanted",
                   "Merging all teams into one so that the system is one"],
             "c": 2,
             "why": "Conway's law describes the structure shaping the design; the "
                    "inverse maneuver uses that on purpose, changing the structure "
                    "to get the design wanted. The chapter says loose coupling "
                    "does not mean teams should not work together."},
        ],
        "mistakes": [
            ("Believing that more people must mean less output per person",
             "That is the orthodox view the authors name, from communication and "
             "integration overheads. In their survey, among those who deploy at "
             "least once a day, the high performers' rate rose with the number of "
             "developers, the medium performers' held and the low performers' "
             "fell. It is a pattern in a sample, not a law."),
            ("Reading loose coupling as a ban on talking",
             "The chapter says DevOps is about collaboration and teams should work "
             "together. The aim is that the available communication bandwidth "
             "goes to higher-level shared goals and not to fine-grained "
             "implementation decisions."),
            ("Expecting growth alone to raise the rate",
             "The authors tie the high performers' rising rate to a generative "
             "culture, a modular architecture, continuous delivery practices "
             "and good leadership, not to headcount. The "
             "<code>falling</code> preset shows the pattern the orthodox view "
             "expects; the lab does not say what produces it."),
        ],
        "standard": (
            "Finish when you can say what a rate by size shows.",
            "Given organizations with developers and deploys over a period, work "
            "out deploys per developer per day exactly, say whether it rises, holds "
            "or falls with size, and say what the chapter claims explains the "
            "differences and what it does not show."
        ),
        "note": (
            "The lab works a rate for organizations you type. It cannot say what "
            "a deploy is worth, whether the organizations are alike in other "
            "ways, or why a rate rises: the figure in the book is of survey "
            "respondents who deploy at least daily, and the explanation is "
            "the authors'."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Allow Teams to Choose Their Own Tools (PDF pp. 102-103 of the
    # operator's copy); Architects Should Focus on Engineers and Outcomes,
    # Not Tools or Technologies (pp. 103-104).
    # Quote: PDF p. 104 of the operator's copy, 18 words, quotes.py LOOSE only for the comma the book prints after
    # "them", where the quotation stops.
    # Lesson total: 18 words.
    {
        "slug": "tools-and-architects",
        "title": "Allow Teams to Choose Their Own Tools",
        "module": "Chapter 5 · Architecture",
        "one_line": "Why the authors ask for tool choice to rest with the teams, where they would still standardize, and the questions architects should ask instead.",
        "summary": (
            "The last two sections of Chapter 5: the case for letting teams "
            "choose their tools, the room the authors leave for standards, and "
            "what they say architects should attend to. Then count how many "
            "teams must coordinate a release when a shared library forces its "
            "consumers to upgrade together."
        ),
        "key": [
            "approved lists have reasons and costs",
            "team tool choice predicts performance",
            "standardize the platform, not every tool",
            "usable tools get adopted by choice",
            "wrong questions: which tool, which stack",
            "enable change without depending on others",
            "architects work with engineers",
        ],
        "key_label": "Tools and architects in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Approved list",
             "A list of tools and frameworks engineers must choose from. The "
             "chapter names its purposes: a simpler environment, the skills to "
             "support it, buying power with vendors and correct licensing. It "
             "weighs them against the teams' loss of fit."),
            ("Standardized platform",
             "A common way to build, run and debug services, such as a universal "
             "way to run each in a debuggable sandbox. The authors keep a place "
             "for it, around the architecture and configuration of "
             "infrastructure."),
            ("Teams that must coordinate",
             "The teams that own the components of a release group spanning more "
             "than one team. The lab's tile counts such groups and names each "
             "group's teams; a group owned by one team is not listed. Fewer "
             "means fewer people who must agree before anything ships."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read Allow Teams to Choose Their Own Tools and Architects Should "
            "Focus on Engineers and Outcomes, Not Tools or Technologies in your "
            "own copy first. The lesson sets out the two arguments and then "
            "counts the teams a tie draws together."),
        "body": [
            ("p", "&ldquo;What tools or technologies you use is irrelevant if the "
                  "people who must use them hate using them&rdquo;, the authors write in the last section of "
                  "Chapter 5, going on to say that the tools must also achieve the "
                  "outcomes wanted. It comes at the end of a short argument about who should "
                  "choose. In many organizations engineers must use an approved "
                  "list of tools and frameworks. The authors give the usual "
                  "reasons fairly: a simpler environment, the skills to "
                  "manage the technology through its life, more buying power "
                  "with vendors, and correct licences."),
            ("p", "Their objection is the cost. A fixed list stops teams from "
                  "choosing what suits their work and from trying new "
                  "approaches. In their analysis, where teams decide for themselves which "
                  "tools to use, that contributes to software delivery "
                  "performance and through it to organizational performance. "
                  "They find it unsurprising, since the people who build and run "
                  "systems choose on what serves their work and their users, "
                  "and they note similar results in other studies of technical "
                  "professionals, suggesting the upside of delegating the choice "
                  "may outweigh the downside. This is the second of the two "
                  "capabilities the 2017 analysis added to the drivers of "
                  "continuous delivery."),
            ("p", "They do not argue against standards. Some belong, "
                  "especially in how infrastructure is architected and "
                  "configured; they cite Humble's discussion "
                  "of a standardized operational platform and Steve Yegge's "
                  "account of Amazon's move to service-oriented architecture, "
                  "which noted that debugging another team's code is nearly "
                  "impossible without one standard way to run each service in a "
                  "sandbox you can debug. They add a finding on security: teams "
                  "that build it into their work do better at continuous "
                  "delivery, and a key element is that security teams supply "
                  "libraries, packages, toolchains and processes that are "
                  "already approved and easy to use."),
            ("p", "The two fit together, the authors say. Tools that make "
                  "engineers' lives easier get adopted freely, which beats forcing "
                  "tools chosen for the convenience of other stakeholders, and "
                  "the freedom to decline keeps the internal tool-builders honest: "
                  "usability and customer satisfaction matter as much to internal "
                  "customers as to external ones. The last section turns to "
                  "architects. Discussions of architecture, they observe, "
                  "fixate on whether to adopt microservices or serverless, which "
                  "orchestrator, which CI server or language. Their research says "
                  "these are the wrong questions; what matters is enabling "
                  "teams to change their products and services without waiting "
                  "on other teams or systems, and architects should work closely "
                  "with the engineers who build and run them."),
            ("p", "Now the count, which is the previous lesson's, with teams. "
                  "The lab takes components, the team that owns each, and the "
                  "ties between components that must be released together. The "
                  "system is invented for this lesson: seven services owned by "
                  "four teams. Three of the ties are real couplings inside a "
                  "team's own area (billing and invoices; signup and referrals; "
                  "reports and export). Three more come from a shared library "
                  "whose new version must be adopted at the same time by billing, "
                  "signup, reports and the gateway. In the preset "
                  "<code>lockstep</code> those six ties make one group of 7: all "
                  "seven services, no component deployable alone, and 4 teams "
                  "that must coordinate every release."),
            ("p", "Suppose signup and reports could take the new library version at "
                  "different times, say through a compatibility shim, and remove "
                  "that one tie. The group splits in two. The larger has 4 "
                  "services owned by payments and growth, the other 3 services "
                  "owned by data and platform. The lab's after tile reads 2: two "
                  "groups that still need two teams each, so all four teams still "
                  "coordinate, but in pairs. In the preset <code>pinned</code> the "
                  "shared library is pinned by version, so each service upgrades "
                  "when its own team chooses and those three ties vanish. "
                  "There are 4 groups, the largest has 2, 1 component (the "
                  "gateway) is deployable alone, and no group spans more than "
                  "one team, so the lab lists none that must coordinate."),
            ("p", "The lab shows what the chapter argues, that team choice and "
                  "coupling meet in the release. A tool or library that forces a "
                  "lock-step upgrade makes a decision that was meant to be local "
                  "into one across teams. It does not decide the question the "
                  "chapter leaves open: a standardized platform also removes some "
                  "choices from a team, and whether a given standard serves its "
                  "users or only its owners is something to ask the "
                  "engineers who use it."),
            ("h3", "Exercise"),
            ("ul", [
                "Components and owners: `web, shop; api, shop; search, find; "
                "index, find; ads, growth`.",
                "Ties: `web, api; api, search; search, index; ads, web`. A shared "
                "library ties `api` and `search`.",
            ]),
            ("p", "Find the release groups and the teams that must coordinate "
                  "in the largest. Then remove the tie between api and search and "
                  "do it again. Say what the first count tells you about the "
                  "shared library, and what a team would give up by pinning "
                  "it."),
            ("p", "The next course, Security, Lean Management and Product "
                  "Development, reads Chapters 6 to 8, on security, lean "
                  "management and product development."),
        ],
        "lab": ("acckit", {
            "mode": "release",
            "view": "independent",
            "preset": "lockstep",
            "presets": [
                {"id": "lockstep",
                 "label": "Seven services, with a shared library forcing a lock-step upgrade",
                 "components": SERVICES,
                 "teams": SERVICE_TEAMS,
                 "ties": LOCKSTEP_TIES,
                 "remove": LOCKSTEP_REMOVE,
                 "expect": {
                     "arlGroups": "1: {billing, invoices, signup, referrals, reports, export, gateway}",
                     "arlLargest": "7: billing, invoices, signup, referrals, reports, export, gateway",
                     "arlAlone": "0: none",
                     "arlCoord": "1 group spans more than one team: payments + growth + data + platform for {billing, invoices, signup, referrals, reports, export, gateway}",
                     "arlAfterCoord": "2 groups span more than one team: payments + growth for {billing, invoices, signup, referrals}; data + platform for {reports, export, gateway}"
                 }},
                {"id": "pinned",
                 "label": "The same services, with the library pinned by version",
                 "components": SERVICES,
                 "teams": SERVICE_TEAMS,
                 "ties": PINNED_TIES,
                 "expect": {
                     "arlGroups": "4: {billing, invoices}, {signup, referrals}, {reports, export}, {gateway}",
                     "arlLargest": "2: billing, invoices",
                     "arlAlone": "1: gateway",
                     "arlCoord": "none: every release group belongs to one team"
                 }},
            ],
            "panel_title": "Which teams must coordinate a release",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Counting the teams a release draws in",
        "steps_intro": "Four steps, the last of them on a system you know.",
        "steps": [
            ("Give every component an owner",
             "Write down which team owns each service, as the team that would "
             "be called out if it broke."),
            ("List the ties, shared things included",
             "Add a tie for each pair that must go out together. A shared "
             "library, tool or platform that forces a lock-step upgrade ties "
             "all its consumers, so tie them in turn."),
            ("Find the largest group and its teams",
             "Follow the ties to the biggest set and list the distinct teams "
             "that own its components."),
            ("Do it on your own system",
             "Take a shared library or tool your teams all use, list the "
             "services that must adopt a new version together, and type them in. "
             "Write down how many teams must agree before it ships."),
        ],
        "worked": {
            "title": "Seven services, four teams",
            "intro": [
                "Find the group in <code>lockstep</code>, then split it.",
            ],
            "lines": [
                "billing ties to invoices and to signup",
                "signup ties to referrals and to reports",
                "reports ties to export and to gateway",
                "one group: all 7 services; none alone",
                "teams: payments, growth, data, platform: 4",
                "remove signup-reports",
                "billing, invoices, signup, referrals: 4 services, 2 teams",
                "reports, export, gateway: 3 services, 2 teams",
            ],
            "after": [
                "After the split the larger group has 4 services and 2 teams, and "
                "the lab's after tile reads 2 because two groups still span "
                "two teams each; the teams it names are four. Each group needs "
                "fewer people to agree than before.",
            ],
        },
        "quiz_title": "Tools, ties and architects",
        "quiz": [
            {"q": "In the preset <code>lockstep</code>, how many teams must "
                  "coordinate every release?",
             "a": ["2", "6", "7", "4"],
             "c": 3,
             "why": "All seven services are in one group, and they are owned by "
                    "payments, growth, data and platform: four teams. Seven is "
                    "the number of services and six the number of ties; two is the "
                    "number of teams in each group after the signup-reports tie is removed."},
            {"q": "On <code>lockstep</code>, once the tie between signup and "
                  "reports is removed, how many services are in the largest group?",
             "a": ["4", "3", "6", "7"],
             "c": 0,
             "why": "The group splits into billing, invoices, signup and referrals "
                    "(4) and reports, export and gateway (3). Seven is the "
                    "size before the removal; six is the number of ties; three "
                    "is the smaller group."},
            {"q": "According to the chapter, what is the effect when teams choose "
                  "their own tools?",
             "a": ["It lowers performance until a standard is chosen",
                   "It contributes to software delivery performance, and so "
                   "to organizational performance",
                   "It makes no difference to delivery, but raises morale",
                   "It matters only for security tooling"],
             "c": 1,
             "why": "The authors report a contribution to software delivery "
                    "performance and, so, to the organization's. "
                    "They also keep a place for standardization around "
                    "infrastructure, and say preapproved security tools get "
                    "used when they make engineers' lives easier."},
            {"q": "What does the chapter call the wrong questions for "
                  "architects to focus on?",
             "a": ["Whether teams can change their products without depending on "
                   "other teams",
                   "How closely architects should work with engineers",
                   "Which tools, languages, frameworks or architectural styles "
                   "the organization should adopt",
                   "Whether engineers like the tools they use"],
             "c": 2,
             "why": "The authors say the discussion should not turn on whether "
                    "to adopt microservices or serverless, or which CI server "
                    "or language. The other options are what they say matters: "
                    "enabling change without dependencies, collaborating with "
                    "engineers and whether people hate using the tools."},
        ],
        "mistakes": [
            ("Reading the chapter as saying there should be no standards",
             "The authors keep a place for standards, especially for how "
             "infrastructure is architected and configured, and cite a "
             "standardized operational platform and Yegge's account of Amazon. "
             "Their objection is to standards chosen for other stakeholders' "
             "convenience and imposed on the engineers who use them."),
            ("Thinking an architect's job is to pick the best technology",
             "The chapter calls questions such as microservices against "
             "serverless or one orchestrator against another the wrong ones. "
             "Tools are irrelevant if the people hate using them or if they do not "
             "produce the outcomes and behaviors wanted; architects should help "
             "teams change their services without depending on others."),
            ("Mandating a tool because it is good",
             "The chapter's point on security tools is that engineers adopt "
             "preapproved libraries and toolchains of their own free will when "
             "they make life easier. A tool forced on teams hides whether it is "
             "usable, which the freedom to decline keeps in view."),
        ],
        "standard": (
            "Finish when you can say what a shared tool couples.",
            "Given services, their owning teams and the ties that force them to "
            "release together, find the largest group and the teams that must "
            "coordinate, and say what the chapter claims about tool choice, "
            "standards and the questions architects should ask."
        ),
        "note": (
            "The lab counts teams from ties you type. It cannot say whether a "
            "tie is a real constraint, whether pinning a version costs more than "
            "the coordination it saves, or whether team choice caused anything: "
            "the authors report that it contributes to performance in their "
            "survey, and argue the rest."
        ),
    },
]
