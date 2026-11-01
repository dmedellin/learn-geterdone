"""Technical Practices and Architecture, lessons 1-5 -- Chapter 4 and the
first part of Chapter 5.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 4, Technical Practices
(What Is Continuous Delivery?, The Impact of Continuous Delivery, The Impact
of Continuous Delivery on Quality, Continuous Delivery Practices: What Works
and What Doesn't, Adopting Continuous Delivery); Chapter 5, Architecture
(Types of Systems and Delivery Performance, Focus on Deployability and
Testability). Pages in the comments are PDF pages of the operator's copy; the
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

# ---------------------------------------------------------------- 01 samples

# A team with twenty-four changes ready to go out, written for the lesson.
# Hours: each change takes 1 hour to prepare and check; each release costs a
# fixed 2 hours however many changes it carries.
BATCH_WORK = "24"
BATCH_PER_ITEM = "1"
BATCH_COST = "2"

# ---------------------------------------------------------------- 02 samples

# A team's month, in hours, by kind of work, written for the lesson.
MONTH_ENTRIES = "new, 440; unplanned, 190; rework, 130; other, 240"
MONTH_SCALE = "rework, 1/2"

# ---------------------------------------------------------------- 03 samples

# Invented teams, counted by whether they met a goal of their own for failed
# changes in a quarter.
TESTS_ROWS = "developers-own, 40, 28; separate-qa, 50, 20"
CONFIG_ROWS = "config-in-version-control, 60, 45; config-elsewhere, 40, 20"
# 03 exercise: tests run on every commit, or not.
COMMIT_ROWS = "run-every-commit, 25, 20; run-now-and-then, 25, 10"

# ---------------------------------------------------------------- 04 samples

# A team's twenty working days, as branches written for the lesson:
# branch, day created, day merged ("-" is still open at the end).
SHORT_BRANCHES = (
    "b1, 1.09:00, 1.15:00; b2, 1.10:00, 2.09:00; b3, 2.10:00, 2.14:00; "
    "b4, 4.09:00, 4.17:00; b5, 5.09:00, 5.12:00; b6, 8.09:00, 8.16:00; "
    "b7, 9.13:00, 10.10:00; b8, 12.09:00, 12.11:00; b9, 15.14:00, 16.09:00; "
    "b10, 18.10:00, 18.15:00"
)
LONG_BRANCHES = (
    "f1, 1.09:00, 9.12:00; f2, 2.09:00, 14.10:00; f3, 3.09:00, 12.15:00; "
    "f4, 6.09:00, -; f5, 8.09:00, 17.16:00; s1, 10.09:00, 10.14:00; "
    "s2, 11.09:00, 12.08:00; s3, 15.10:00, 15.12:00"
)
LONG_FREEZES = "18, 19, 20"
# 04 exercise: a ten-day sprint.
SPRINT_BRANCHES = (
    "a, 1.09:00, 3.12:00; b, 1.10:00, 1.15:00; c, 2.09:00, 6.11:00; "
    "d, 4.09:00, 4.12:00; e, 5.09:00, -"
)

# ---------------------------------------------------------------- 05 samples

# A shop's services and the ties that force them to be released together.
SHOP_COMPONENTS = "cart, catalog, checkout, email, payments, pricing, reviews, search"
SHOP_TIES = (
    "cart, checkout; checkout, payments; pricing, catalog; catalog, search; "
    "cart, pricing"
)
SHOP_REMOVE = "cart, pricing"
# A bank's mainframe ledger behind a service interface.
LEDGER_COMPONENTS = "ledger, fx, portal, postings, statements"
LEDGER_TIES = "postings, statements; statements, portal"
# 05 exercise: a clinic.
CLINIC_COMPONENTS = "booking, notes, billing, reminders, labs"
CLINIC_TIES = "booking, reminders; reminders, notes; billing, labs"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 4, Technical Practices: the opening (PDF p. 76 of the
    # operator's copy); What Is Continuous Delivery? (pp. 77-80): the
    # definition and the five principles (pp. 77-78), the foundations (pp.
    # 79-80), the feedback loops and on-demand release (p. 80).
    # Quote: PDF p. 77 of the operator's copy, 34 words, quotes.py OK.
    # Lesson total: 34 words.
    {
        "slug": "what-is-continuous-delivery",
        "title": "What Is Continuous Delivery?",
        "module": "Chapter 4 · Technical Practices",
        "one_line": "Five principles and three foundations, and one reason small batches pay: the cost of putting out a change has to fall first.",
        "summary": (
            "Chapter 4 turns from culture to technical practice. Read how the "
            "authors define continuous delivery, the five principles at its "
            "heart and the foundations it rests on; then work out on a team's "
            "twenty-four waiting changes what a smaller batch does to the wait "
            "for the first feedback, and what it costs."
        ),
        "key": [
            "build quality in, do not inspect it in",
            "work in small batches",
            "computers repeat, people solve problems",
            "never be satisfied, always improve",
            "everyone owns the system-level outcomes",
            "a release is routine and on demand",
            "cheaper releases make small batches pay",
        ],
        "key_label": "Continuous delivery in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the other "
            "two are what the lab measures."
        ),
        "concepts": [
            ("Continuous delivery",
             "A set of capabilities that let a team get changes of every kind into "
             "production, or into users' hands, safely, quickly and sustainably. "
             "It is a way of working, kept going by tools, and not one tool."),
            ("Batch",
             "The changes released together. A batch of twenty-four waits until "
             "all twenty-four are ready; a batch of six waits for six. Chapter 4 "
             "argues for small ones, because feedback arrives sooner and less "
             "work is built on a wrong guess."),
            ("Release cost",
             "The fixed time to put out one batch, whatever its size: the "
             "build, the checks, the approvals, the deploy. Small batches "
             "multiply it, which is why the chapter pairs them with automation."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read the opening of Chapter 4 and its first section, What Is "
            "Continuous Delivery?, in your own copy first. The lesson sets out "
            "the definition and the principles in order, then counts one of them "
            "on a small sample."
        ),
        "body": [
            ("p", "&ldquo;Continuous delivery is a set of capabilities that enable us "
                  "to get changes of all kinds&mdash;features, configuration changes, "
                  "bug fixes, experiments&mdash;into production or into the hands of "
                  "users safely, quickly, and sustainably.&rdquo; That is the "
                  "definition Forsgren, Humble and Kim give in Chapter 4, Technical "
                  "Practices, and the chapter asks a plain question of it: do the "
                  "technical practices behind such a definition measurably change how "
                  "a team performs? Their reason for asking is that many Agile "
                  "adoptions treated technical practice as secondary to the "
                  "management and team practices some Agile frameworks stress, "
                  "though Extreme Programming, among the most popular frameworks "
                  "when the Agile Manifesto appeared in 2001, had put practices "
                  "like test-driven development and continuous integration at "
                  "its centre."),
            ("p", "Five principles sit at the heart of it. The first is to build "
                  "quality in. The authors quote Deming's third point, that you "
                  "should stop relying on inspection at scale and design quality "
                  "in from the start, and read it as a call to find "
                  "problems quickly, while they are cheap to fix. The second is to "
                  "work in small batches: plan in chunks that deliver a measurable "
                  "outcome to a small part of the market, get feedback, and "
                  "correct course. They admit that small chunks add overhead and "
                  "argue that the overhead buys the chance to avoid work of no "
                  "value or negative value; the goal, they say, is to change the "
                  "economics of delivery so that pushing out a single change costs "
                  "very little."),
            ("p", "The third principle divides the labour. Repetitive, slow work "
                  "such as regression testing and deployment should be automated, "
                  "so that people are free for the work that needs judgement: "
                  "improving the design of systems and processes in response to "
                  "feedback. The fourth is relentless improvement, which the "
                  "authors name as the defining trait of high-"
                  "performing teams: they are never satisfied, and improvement is "
                  "part of everybody's daily work. The fifth is that everyone is "
                  "responsible. Drawing on Westrum, whom Measuring and Changing Culture read, they note "
                  "that in a bureaucratic organization development watches "
                  "throughput, testing quality and operations stability, though all "
                  "three are outcomes of the whole system. Management's job is to "
                  "make those outcomes visible and to set goals for them that are "
                  "measurable and time-bound."),
            ("p", "Three foundations make the principles practical. "
                  "Comprehensive configuration management means environments and "
                  "software can be built, tested and deployed in a fully automated "
                  "way from what is stored in version control; manual approvals "
                  "may remain, but once given, everything after them is automatic. "
                  "Continuous integration (CI) means short-lived branches, under a "
                  "day's work, merged into trunk often, with each change triggering "
                  "a build and unit tests and any failure fixed at once. "
                  "Continuous testing means tests run against every commit, "
                  "developers able to run them all on their own machines, testers "
                  "doing exploratory work on the latest builds, and no one calling "
                  "work done until its automated tests exist and pass. The "
                  "section closes on the picture: several feedback loops, and a "
                  "release that is a routine activity available on demand. The "
                  "pipeline that joins the loops is named in a footnote; the "
                  "chapter does not describe one."),
            ("p", "Now the count. Think of a team with twenty-four changes ready "
                  "to ship, each taking an hour to prepare and check, and a release "
                  "that costs two hours however many changes it carries. These "
                  "numbers are invented for this lesson. The lab takes the number "
                  "of changes, the batch size, the hours per change and the hours "
                  "per release, and reports how many batches there are, when the "
                  "first batch is out (the earliest feedback anyone can have), when "
                  "the last is out, the average wait of a change from the start "
                  "until its batch is released, and the total hours spent on "
                  "releases. The preset <code>whole</code> sends all twenty-four "
                  "as one batch: 1 release, out at hour 26, an average wait of 26 "
                  "hours, 2 hours of release overhead."),
            ("p", "The preset <code>halved</code> splits them into batches of "
                  "twelve. Each batch takes 12 hours of work and 2 of release, so "
                  "the first is out at hour 14 and the second at hour 28; the "
                  "average wait is 21 hours and the overhead is 4. The first "
                  "feedback arrives 12 hours sooner and the last change leaves 2 "
                  "hours later. The preset <code>quarter</code> goes to batches "
                  "of six: 4 releases, the first at hour 8, the last at hour 32, an "
                  "average wait of 20 hours and 8 hours of overhead. The first "
                  "feedback now arrives in a third of the time, and the last "
                  "change is 6 hours later than in <code>whole</code>."),
            ("p", "That is the trade the authors name when they say small "
                  "batches add overhead, and it is why the principle is paired "
                  "with the third one. The preset <code>automated</code> keeps "
                  "batches of six but cuts the release to a quarter of an hour, as "
                  "a team might by automating the build and the deploy. The first "
                  "feedback arrives at hour 6.25, the last change at hour 25, the "
                  "average wait falls to about 15.63 hours, and the overhead is 1 hour "
                  "in all. Nothing in the changes got smaller; the cost of "
                  "releasing one did, which is the \"changing the economics\" "
                  "of the chapter in a number."),
            ("p", "A word on flow, which this lesson adds and the chapter does "
                  "not mention. Work in process, the number of changes started and "
                  "not yet finished, is tied to lead time by Little's law: the "
                  "average work in process equals the average rate at which work "
                  "finishes times the average time it spends in the system. A team "
                  "with 18 items in process that finishes 3 a day has an average "
                  "lead time of 6 days. The System Design lesson \"Little's Law "
                  "from a Trace\" proves and counts it. Here it is only a reason "
                  "to want fewer changes waiting at once, which is what a smaller "
                  "batch gives."),
            ("h3", "Exercise"),
            ("ul", [
                "A team has 30 changes ready, an hour to prepare each, and a "
                "release cost of 3 hours.",
                "Compare batches of 15 and of 5.",
            ]),
            ("p", "Work out, for each batch size, the hour of the first release, "
                  "the hour of the last and the average wait, then type the "
                  "numbers into the lab to check you. Say which size gives the "
                  "earliest feedback, which gives the earliest finish and what "
                  "the answer says about the cost of a release."),
            ("p", "The next lesson, The Impact of Continuous Delivery, reads the "
                  "research that connects these practices to delivery "
                  "performance, to deployment pain and to the share of time "
                  "spent on unplanned work."),
        ],
        "lab": ("acckit", {
            "mode": "flow",
            "view": "batch",
            "preset": "whole",
            "presets": [
                {"id": "whole",
                 "label": "Twenty-four changes in one batch",
                 "work": BATCH_WORK, "batch": "24", "per_item": BATCH_PER_ITEM,
                 "release_cost": BATCH_COST, "unit": "hours",
                 "expect": {
                     "aflBatches": "1 of 24",
                     "aflFirst": "26 hours",
                     "aflLast": "26 hours",
                     "aflWait": "26 hours",
                     "aflOverhead": "2 hours"
                 }},
                {"id": "halved",
                 "label": "Two batches of twelve",
                 "work": BATCH_WORK, "batch": "12", "per_item": BATCH_PER_ITEM,
                 "release_cost": BATCH_COST, "unit": "hours",
                 "expect": {
                     "aflBatches": "2 of 12",
                     "aflFirst": "14 hours",
                     "aflLast": "28 hours",
                     "aflWait": "21 hours",
                     "aflOverhead": "4 hours"
                 }},
                {"id": "quarter",
                 "label": "Four batches of six",
                 "work": BATCH_WORK, "batch": "6", "per_item": BATCH_PER_ITEM,
                 "release_cost": BATCH_COST, "unit": "hours",
                 "expect": {
                     "aflBatches": "4 of 6",
                     "aflFirst": "8 hours",
                     "aflLast": "32 hours",
                     "aflWait": "20 hours",
                     "aflOverhead": "8 hours"
                 }},
                {"id": "automated",
                 "label": "Four batches of six, with a release that costs a quarter of an hour",
                 "work": BATCH_WORK, "batch": "6", "per_item": BATCH_PER_ITEM,
                 "release_cost": "1/4", "unit": "hours",
                 "expect": {
                     "aflBatches": "4 of 6",
                     "aflFirst": "25/4 = 6.25 hours",
                     "aflLast": "25 hours",
                     "aflWait": "125/8 ≈ 15.63 hours",
                     "aflOverhead": "1 hours"
                 }},
            ],
            "panel_title": "What a smaller batch does to the wait",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Comparing batch sizes",
        "steps_intro": "Four steps, the last of them on a team of your own.",
        "steps": [
            ("Write down the three quantities",
             "Count the changes waiting, the hours one takes to prepare and "
             "check, and the fixed hours a release costs whatever it carries."),
            ("Work out one batch",
             "A batch of b changes is out after b times the hours per change, "
             "plus the release hours. Its changes all wait until then."),
            ("Compare two sizes",
             "Find the hour of the first release, the hour of the last, and the "
             "average wait for each size. Note which measure improves and "
             "which gets worse."),
            ("Do it on your own team",
             "Take the changes your team has ready now, estimate an honest "
             "release cost from your last release, and type both into the "
             "lab with two batch sizes. Write down what the release cost "
             "would have to be for the smaller batch to finish first."),
        ],
        "worked": {
            "title": "Two batches of twelve",
            "intro": [
                "Work out <code>halved</code>: 24 changes, 12 to a batch, 1 hour "
                "per change, 2 hours per release.",
            ],
            "lines": [
                "24 changes in batches of 12: 2 batches",
                "one batch: 12 x 1 hour + 2 hours = 14 hours",
                "first release: hour 14",
                "second release: 14 + 14 = hour 28",
                "average wait: (14 + 28) / 2 = 21 hours",
                "release overhead: 2 releases x 2 hours = 4 hours",
            ],
            "after": [
                "The average is of the two release hours because each batch holds "
                "the same number of changes, so each release counts equally.",
            ],
        },
        "quiz_title": "Principles, batches and releases",
        "quiz": [
            {"q": "In the exercise (30 changes, 1 hour each, a 3-hour release), "
                  "at what hour does the first release go out in batches of 5?",
             "a": ["Hour 8", "Hour 5", "Hour 18", "Hour 48"],
             "c": 0,
             "why": "A batch of 5 is 5 hours of work plus 3 of release, so the "
                    "first is out at hour 8. Hour 5 forgets the release cost; hour "
                    "18 is the first release in batches of 15 (15 + 3); hour 48 is "
                    "the sixth and last release in batches of 5. The batches of 5 "
                    "also finish later than the batches of 15, which finish at "
                    "hour 36, because the release cost is paid six times and not "
                    "twice."},
            {"q": "In the preset <code>quarter</code>, what is the last change's "
                  "hour of release, and how does it compare with "
                  "<code>whole</code>?",
             "a": ["Hour 32, later than 26", "Hour 32, earlier than 26",
                   "Hour 26, the same", "Hour 24, earlier than 26"],
             "c": 0,
             "why": "Four batches of 8 hours each finish at hour 32, six hours "
                    "after the single batch of <code>whole</code>. The overhead of "
                    "four releases (8 hours) against one (2 hours) is exactly "
                    "that six. Small batches bring feedback sooner and the last "
                    "change later, until the release itself gets cheaper."},
            {"q": "Which of the chapter's five principles says that people should "
                  "be freed for work that needs problem-solving, by automating "
                  "regression testing and deployment?",
             "a": ["Computers perform repetitive tasks; people solve problems",
                   "Build quality in",
                   "Work in small batches",
                   "Everyone is responsible"],
             "c": 0,
             "why": "That is the third principle as the chapter names it. Building "
                    "quality in is about finding problems quickly; small batches "
                    "are about feedback and the economics of releasing; everyone "
                    "being responsible is about system-level outcomes. Automation "
                    "serves the second principle by making each release cheap, but "
                    "the chapter gives it a principle of its own."},
            {"q": "On the preset <code>automated</code>, the release costs a "
                  "quarter of an hour. What do the 4 releases cost in total?",
             "a": ["1 hour", "8 hours", "6 hours", "A quarter of an hour"],
             "c": 0,
             "why": "Four releases at a quarter of an hour each is 1 hour. Eight "
                    "hours is the overhead of <code>quarter</code> at 2 hours a "
                    "release; a quarter of an hour is the cost of one release; "
                    "6 hours is the gap between the last change in "
                    "<code>quarter</code> and in <code>whole</code>."},
        ],
        "mistakes": [
            ("Taking continuous delivery to be a pipeline you buy",
             "The chapter defines it as a set of capabilities and builds the "
             "definition from principles that are about people as much as tools: "
             "building quality in, everyone being responsible, improving always. "
             "The deployment pipeline is mentioned only in a footnote, as the "
             "pattern that joins the feedback loops."),
            ("Reading small batches as always faster",
             "The authors say outright that working in small chunks adds overhead. "
             "The lab shows it: on the invented sample the last change leaves "
             "later with batches of six than with one batch of twenty-four, and "
             "only a cheaper release reverses that. What small batches buy is "
             "earlier feedback and less work built on a wrong guess."),
            ("Leaving testing and quality to the end of the work",
             "Continuous testing and building quality in say the opposite: tests "
             "run against every commit, developers can run them all locally, and "
             "no one calls work done until its automated tests pass. Waiting "
             "for a feature to be complete before testing is the dependence on "
             "inspection that Deming's point warns against."),
        ],
        "standard": (
            "Finish when you can say what a smaller batch changes.",
            "Given a number of changes, a time per change and a cost per release, "
            "work out the first release, the last release and the average wait "
            "for two batch sizes, and say what each result shows about the "
            "authors' case for small batches."
        ),
        "note": (
            "The lab models a team that prepares changes one after another and "
            "releases each batch when it is ready. It cannot say whether your "
            "team's changes are independent, what a wrong guess costs, or how "
            "the principles work together; and the authors' case for small "
            "batches is argued from theory and experience in this section, not "
            "from a figure."
        ),
    },
    # ---------------------------------------------------------------- 02
    # The Impact of Continuous Delivery (PDF pp. 80-85 of the operator's
    # copy): the 2014-2016 capabilities (pp. 80-81), the Likert measures (p.
    # 81), pain, burnout, identification and culture (p. 82), the 2017
    # first-order construct and the two new capabilities (pp. 82-83), the
    # drivers and impacts (pp. 83-85, Figures 4.1-4.3 in prose); The Impact
    # of Continuous Delivery on Quality (pp. 85-88): proxies for quality (p.
    # 86), new and unplanned work (pp. 86-87, Figure 4.4 in prose), the fuel
    # light and failure demand (pp. 87-88).
    # Quote: PDF p. 87 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "the-impact-of-continuous-delivery",
        "title": "The Impact of Continuous Delivery",
        "module": "Chapter 4 · Technical Practices",
        "one_line": "What the survey found continuous delivery goes with, from delivery performance to burnout, and the proxy it used for quality.",
        "summary": (
            "The chapter's two impact sections: what the authors measured, what "
            "they found continuous delivery predicts, and why they use the "
            "share of time spent on unplanned work and rework as a stand-in for "
            "quality. Then split a team's month by kind of work and see what "
            "halving the rework would free."
        ),
        "key": [
            "capabilities measured as survey constructs",
            "CD predicts delivery performance",
            "and less deployment pain and burnout",
            "and a more generative culture",
            "quality is value to some person",
            "unplanned work and rework as a proxy",
            "high performers spend less on it",
        ],
        "key_label": "The impact of continuous delivery in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Construct",
             "A quantity the survey cannot ask about directly and so measures "
             "from several statements, each rated on a scale. Most of the "
             "capabilities in this chapter are constructs; deployment "
             "automation is the exception the chapter notes."),
            ("Unplanned work and rework",
             "Time spent on break and fix work, emergency deployments and "
             "patches, urgent audit requests and the like, rather than on new "
             "work. The chapter treats the share of time it takes as a stand-in "
             "for quality, because it is work caused by something not built right "
             "the first time."),
            ("Share of time",
             "A kind of work's hours divided by all the hours counted, as a "
             "percentage. The lab gives each kind's share, and what new work's "
             "share would be if some hours were freed."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read The Impact of Continuous Delivery and The Impact of Continuous "
            "Delivery on Quality in your own copy first. The lesson sets out "
            "what the authors measured and found, and then works one of their "
            "measures on a team of its own."
        ),
        "body": [
            ("p", "&ldquo;Unplanned work and rework are useful proxies for quality "
                  "because they represent a failure to build quality into our "
                  "products.&rdquo; The authors say this in the second of the "
                  "chapter's impact sections, and it answers a problem the first "
                  "leaves open: what does continuous delivery do for a team, and "
                  "how do you measure that without a number for quality itself? "
                  "Read the first section for the research, the second for the "
                  "proxy."),
            ("p", "The research starts with the first iterations, from 2014 to "
                  "2016, which modelled a list of capabilities: version control for "
                  "code, system configuration and build scripts; test automation "
                  "that is reliable and runs regularly; deployment automation; "
                  "continuous integration; shifting security left; trunk-based "
                  "development; and test data management. Most were measured as "
                  "constructs from several statements on an agree-disagree scale, "
                  "the method Measuring and Changing Culture read, with deployment automation the "
                  "exception. Taken together they predicted delivery performance "
                  "strongly, and also how work felt: less "
                  "deployment pain and less team burnout. The authors reason that "
                  "when delivery is routine, deploying is no big-bang event but "
                  "something done in office hours as part of the day. Teams that "
                  "did well also identified more strongly with their "
                  "organization, which Chapter 10 treats as a predictor of "
                  "organizational performance, and the authors found that "
                  "continuous delivery predicts the more generative culture that "
                  "Chapter 3 measured."),
            ("p", "In 2017 the authors measured continuous delivery directly, "
                  "as a construct of its own: can a team deploy to production, or "
                  "to users, on demand through the life of a project, and does "
                  "everyone get fast feedback on quality and deployability that "
                  "they treat as their top priority? The capabilities of 2014 to "
                  "2016 were strongly and significantly associated with that "
                  "construct, and so were two new ones: a loosely coupled, "
                  "well-encapsulated architecture and teams that can choose their "
                  "own tools. Both are Chapter 5's, and this course's lessons on "
                  "architecture read them. Figures 4.1 to 4.3 draw these as arrows: the "
                  "drivers into continuous delivery, and from it to identification "
                  "with the organization, higher delivery performance, lower change "
                  "fail rates, a generative culture, less deployment pain and "
                  "less burnout. The book draws them as findings of a survey, "
                  "from analysis that tests whether the answers move together as "
                  "the theory says."),
            ("p", "Then the chapter asks whether continuous delivery improves "
                  "quality. The authors first concede that quality is contextual "
                  "and subjective, and quote Jerry Weinberg: quality is value to "
                  "some person. They already had one proxy, the change fail rate "
                  "that Chapter 2 introduced. They tried three more: how well the "
                  "application performs and how good it is, as its own team sees "
                  "it; how much of the working week goes on rework or unplanned work; and the "
                  "share spent on defects found by end users. All three correlated "
                  "with delivery performance. The strongest was the share of time "
                  "on rework and unplanned work, and continuous delivery predicted "
                  "less of it, in a statistically significant way."),
            ("p", "Figure 4.4 compares the survey's high and low performers, the "
                  "groups Chapter 2 formed. The high performers reported 49 percent "
                  "new work and 21 percent unplanned work or "
                  "rework; the low performers 38 and 27 percent. These are the "
                  "survey's figures for its respondents, and the page does not "
                  "give a year at that point. The authors explain the proxy "
                  "with an image from The Visible Ops Handbook, that unplanned work "
                  "is the difference between heeding a low-fuel warning light and "
                  "running dry on the highway, where six engineers drop everything "
                  "to carry fuel to a truck. They add John Seddon's idea of failure "
                  "demand, the work created by failing to do the right thing "
                  "first time."),
            ("p", "Now the count. The lab takes a list of kinds of work with the "
                  "hours spent on each, and optionally a kind to scale. The team "
                  "here is invented for this lesson: in one month it spent 440 "
                  "hours on new work, 190 on unplanned work, 130 on rework and "
                  "240 on everything else. The preset <code>month</code> reports "
                  "1,000 hours in all and the shares 44 percent new, 19 percent "
                  "unplanned, 13 percent rework and 24 percent other, so unplanned "
                  "work and rework together take 32 percent. The preset "
                  "<code>half-rework</code> halves the rework. That frees 65 "
                  "hours, and if all of them went to new work its share would "
                  "rise from 44 to 50.5 percent."),
            ("p", "Read those figures as the authors read theirs, as a proxy and "
                  "not a verdict. The 65 hours assume the team spends everything "
                  "it saves on new work, which a real team might not; the lab "
                  "says what the arithmetic gives and not what would happen. "
                  "Nor does halving rework say how to halve it. The chapter's "
                  "answer is the practices it has just listed: tests that catch "
                  "a fault before release, small batches that expose it sooner, "
                  "and configuration that can be rebuilt."),
            ("h3", "Exercise"),
            ("ul", [
                "A team's month, in hours: `new, 320; unplanned, 200; rework, 160; "
                "other, 120`.",
                "Scale `rework, 1/2`.",
            ]),
            ("p", "Work out the total and each kind's share, then the hours "
                  "freed when rework is halved, and the new share if they all go "
                  "to new work. Type the records into the lab to check them. "
                  "Then say which would please the authors more, that team's "
                  "shares or <code>month</code>'s, and why neither tells you "
                  "whether the team is a high performer."),
            ("p", "The next lesson, Version Control, Test Automation and Test "
                  "Data, reads the part of the chapter that says which "
                  "practices work and which do not, and counts a share of "
                  "teams against a ratio."),
        ],
        "lab": ("acckit", {
            "mode": "work",
            "view": "split",
            "kinds": "new unplanned rework other",
            "preset": "month",
            "presets": [
                {"id": "month",
                 "label": "A team's month: 1,000 hours by kind of work",
                 "entries": MONTH_ENTRIES,
                 "expect": {
                     "awkTotal": "1,000 hours",
                     "awkShares": "new 11/25 = 44%; unplanned 19/100 = 19%; rework 13/100 = 13%; other 6/25 = 24%",
                     "awkNew": "11/25 = 44%",
                     "awkFreed": "no scaling given",
                     "awkNewAfter": "no scaling given"
                 }},
                {"id": "half-rework",
                 "label": "The same month with the rework halved",
                 "entries": MONTH_ENTRIES,
                 "scale": MONTH_SCALE,
                 "expect": {
                     "awkTotal": "1,000 hours",
                     "awkShares": "new 11/25 = 44%; unplanned 19/100 = 19%; rework 13/100 = 13%; other 6/25 = 24%",
                     "awkNew": "11/25 = 44%",
                     "awkFreed": "65 hours (rework 130 → 65), to new",
                     "awkNewAfter": "101/200 = 50.5%"
                 }},
            ],
            "panel_title": "Where the month's hours went",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Splitting a month by kind of work",
        "steps_intro": "Four steps, the last of them on your own team's month.",
        "steps": [
            ("Name the kinds of work",
             "Choose a few kinds and decide in advance where a piece of work "
             "goes. New work, unplanned work, rework and other is the lesson's "
             "split; the chapter does not give a rule for edge cases."),
            ("Total the hours",
             "Add the hours in each kind, then add the kinds. Every share is "
             "the kind's hours divided by that total."),
            ("Scale one kind",
             "Halve the rework and work out the hours freed. Decide where "
             "the freed hours would actually go before adding them to new work."),
            ("Do it on your own team",
             "Take last month's tickets or time records, sort each into a kind "
             "and type the totals into the lab. Write down which kind was hardest "
             "to sort and why."),
        ],
        "worked": {
            "title": "A month of 1,000 hours",
            "intro": [
                "Work out <code>month</code> and then <code>half-rework</code>.",
            ],
            "lines": [
                "total: 440 + 190 + 130 + 240 = 1,000",
                "new: 440 / 1,000 = 44 percent",
                "unplanned: 190 / 1,000 = 19 percent",
                "rework: 130 / 1,000 = 13 percent",
                "halve the rework: 130 / 2 = 65 hours, so 65 freed",
                "new if all 65 go to it: 440 + 65 = 505",
                "505 / 1,000 = 50.5 percent",
            ],
            "after": [
                "The total stays 1,000 because the freed hours are spent, not "
                "lost. If they were not spent on new work, the share of new work "
                "would stay at 44 percent and the total would fall to 935.",
            ],
        },
        "quiz_title": "Measures, proxies and shares",
        "quiz": [
            {"q": "In the preset <code>month</code> (new 440, unplanned 190, "
                  "rework 130, other 240), what share of the hours is new work?",
             "a": ["44 percent", "56 percent", "32 percent", "19 percent"],
             "c": 0,
             "why": "440 of 1,000 hours is 44 percent. Fifty-six percent is everything "
                    "that is not new work; 32 percent is unplanned work and rework "
                    "together, the share the chapter's proxy looks at; 19 percent is "
                    "the unplanned work alone."},
            {"q": "Besides the change fail rate, the authors tested three proxies "
                  "for quality. Which correlated most strongly with delivery "
                  "performance?",
             "a": ["The share of time on rework or unplanned work",
                   "How good the application is, as its own team saw it",
                   "The share of time on defects found by end users",
                   "Deployment pain"],
             "c": 0,
             "why": "The chapter says all of the proxies correlated with delivery "
                    "performance and that the strongest was the percentage of time "
                    "on rework or unplanned work. Deployment pain is one of the "
                    "things continuous delivery predicts less of, not one of the "
                    "quality proxies."},
            {"q": "On the preset <code>half-rework</code>, how many hours does "
                  "halving the rework free?",
             "a": ["65", "130", "95", "32.5"],
             "c": 0,
             "why": "Half of the 130 rework hours is 65. A figure of 130 would "
                    "remove the rework altogether; 95 is half the unplanned hours "
                    "(190), which the scaling does not touch; 32.5 halves it twice."},
            {"q": "The chapter reports the time that low performers spend on new "
                  "work and on unplanned work or rework. Which pair is theirs?",
             "a": ["38 percent new, 27 percent unplanned or rework",
                   "49 percent new, 21 percent unplanned or rework",
                   "27 percent new, 38 percent unplanned or rework",
                   "38 percent new, 21 percent unplanned or rework"],
             "c": 0,
             "why": "Figure 4.4's text gives the high performers 49 and 21 percent "
                    "and the low performers 38 and 27 percent: the survey's "
                    "figures for its respondents. The third option swaps the "
                    "low performers' own two figures, and the fourth mixes one "
                    "from each group."},
        ],
        "mistakes": [
            ("Thinking the benefit of continuous delivery is only speed",
             "The chapter's findings go further than delivery performance. In the "
             "survey, teams that did well at continuous delivery also reported "
             "less deployment pain, less burnout, a stronger identification with "
             "the organization and a more generative culture. The authors argue "
             "that investment in technology is investment in people."),
            ("Treating a proxy as the quantity itself",
             "The authors open the quality section by saying quality is "
             "contextual and subjective. The share of time on unplanned work and "
             "rework is a stand-in, chosen because it correlated most strongly "
             "with delivery performance and because the work it measures is "
             "caused by something not built right the first time. A team with "
             "little of it might still be building the wrong thing."),
            ("Concluding that the goal is zero unplanned work",
             "The chapter reports that even the high performers spent about a "
             "fifth of their time on unplanned work or rework, and does not set "
             "zero as the goal. A team that allowed itself no slack for urgent work "
             "would only be hiding it."),
        ],
        "standard": (
            "Finish when you can say what a share of time shows.",
            "Given a team's hours by kind of work, work out each kind's share and "
            "the hours freed by scaling one kind, and say why the authors read "
            "the share of unplanned work and rework as a proxy for quality and "
            "not a measure of it."
        ),
        "note": (
            "The lab turns hours into shares. It cannot say how a team should "
            "classify its work, whether freed time goes where the arithmetic "
            "puts it, or whether the survey's percentages are typical of a team "
            "like yours: they are self-reported, from a sample the book describes "
            "elsewhere, and the chapter's own claim is about prediction, not proof."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Continuous Delivery Practices: What Works and What Doesn't (PDF pp.
    # 88-91 of the operator's copy): the nine capabilities (p. 88), Version
    # Control (pp. 88-89), Test Automation (pp. 89-91), Test Data Management
    # (p. 91).
    # Quote: PDF p. 89 of the operator's copy, 23 words, quotes.py OK.
    # Lesson total: 23 words.
    {
        "slug": "version-control-and-test-automation",
        "title": "Version Control, Test Automation and Test Data",
        "module": "Chapter 4 · Technical Practices",
        "one_line": "What the survey found about version control, tests and test data, including the finding that tests written by a separate QA team do not go with performance.",
        "summary": (
            "The first half of the chapter's practices section: what to keep in "
            "version control, what makes automated tests worth having, who "
            "should write them, and what a test needs from its data. Then count "
            "the share of invented teams that meet a goal with and without a "
            "practice, and the ratio between them."
        ),
        "key": [
            "version control for configuration too",
            "configuration correlated more than code",
            "automated tests that are reliable",
            "quarantine or delete the flaky ones",
            "developers write and own acceptance tests",
            "testers still test, by hand and alongside",
            "test data on demand, never the limit",
        ],
        "key_label": "Version control and tests in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Reliable automated tests",
             "A suite whose passing tells a team it can release, and whose "
             "failures mean a real defect. A flaky suite gives false alarms and "
             "false comfort. The chapter suggests moving unreliable tests to a "
             "separate quarantine suite, or deleting them."),
            ("Share and ratio",
             "A group's share is the part that met a goal over the whole group. "
             "The ratio of two groups' shares is how many times as likely one "
             "group was to meet it. A ratio of 2 is a share twice the other's."),
            ("Odds ratio",
             "A different ratio, between the odds of meeting the goal in each "
             "group (met over not met). The lab shows it separately, because a "
             "ratio of shares of 1.75 and an odds ratio of 3.5 are different "
             "numbers about the same teams."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read Continuous Delivery Practices: What Works and What Doesn't, "
            "down to Test Data Management, in your own copy first. The lesson "
            "goes through the three practices and then counts shares and ratios "
            "on a sample of its own."
        ),
        "body": [
            ("p", "The survey found, Forsgren, Humble and Kim write, that "
                  "&ldquo;keeping system and application configuration in version "
                  "control was more highly correlated with software delivery "
                  "performance than keeping application code in version "
                  "control.&rdquo; It is one of the nuances they promise in the "
                  "section What Works and What Doesn't, and the "
                  "chapter has just counted nine capabilities that drive continuous "
                  "delivery; two of them, architecture and tool choice, get Chapter "
                  "5. This lesson reads the first three practices after them: "
                  "version control, test automation and test data management."),
            ("p", "On version control, the survey asked whether application code, "
                  "system configuration, application configuration and the scripts "
                  "that automate build and configuration were all in it. Together "
                  "those predict performance and form a key part of continuous "
                  "delivery. The surprise is the one in the quotation: configuration "
                  "is usually treated as secondary to code, and the authors say the "
                  "data shows that to be a misconception. It also fits the "
                  "foundation of the first lesson, that environments and releases "
                  "can be rebuilt from what version control holds."),
            ("p", "Test automation gets the longest treatment. Tests help only "
                  "if they are reliable: a pass should give confidence that the "
                  "software is releasable and a failure should mean a real defect. "
                  "Many suites are flaky, and the authors advise putting the "
                  "unreliable ones in a separate quarantine suite run on its own, "
                  "or even deleting them, since version control keeps them. The "
                  "second finding concerns authorship. Teams where developers "
                  "chiefly create and maintain the acceptance tests, and can "
                  "reproduce and fix them on their own machines, did well; where "
                  "tests were chiefly made and kept by a QA team or an outsourcing "
                  "partner, the practice was not correlated with performance. The "
                  "theory offered is that developers who write tests write "
                  "code that is easier to test, which is why test-driven "
                  "development matters, and that developers who own the tests "
                  "care about maintaining them."),
            ("p", "The authors take care to say what this does not mean. It is "
                  "not an argument for dismissing testers, who do the manual work "
                  "of exploratory, usability and acceptance testing and who help "
                  "write and grow the automated suites alongside developers. "
                  "Once the tests exist, the chapter's advice is to run them "
                  "often: every commit should trigger a build and some quick "
                  "automated tests, developers should see the results of a fuller "
                  "acceptance and performance suite every day, and the current "
                  "builds should be available to testers. Test data management "
                  "is the last of the three. Successful teams had enough test "
                  "data to run their fully automated suites, could get it when "
                  "they needed it, and found that it did not limit which "
                  "automated tests they could run."),
            ("p", "Now the count, which is a comparison the survey makes in "
                  "another form. The lab takes groups of teams, how many teams "
                  "each holds and how many met a goal, and reports each group's "
                  "share, the ratio of two shares, the difference in percentage "
                  "points and the odds ratio. The teams are invented for this "
                  "lesson, and the goal is whatever failed-change goal each team "
                  "set for itself over a quarter. In the preset <code>tests</code>, "
                  "40 teams whose developers own the acceptance tests include 28 "
                  "that met the goal (70 percent); of 50 teams with a separate QA "
                  "team writing them, 20 did (40 percent). The first group was "
                  "1.75 times as likely to meet the goal, 30 percentage points "
                  "ahead. The odds ratio is 3.5."),
            ("p", "Why show the odds ratio at all? Because it is the number a "
                  "statistical model often reports and the number people often "
                  "mistake for the ratio of shares. Here the odds are 28 to 12 "
                  "(2.33) against 20 to 30 (0.67); their ratio is 3.5, twice the "
                  "1.75 that answers the question &ldquo;how many times as "
                  "likely?&rdquo; The preset <code>config</code> gives the same "
                  "arithmetic on the finding about configuration: 60 teams that "
                  "keep configuration in version control, 45 of which met the "
                  "goal (75 percent), against 40 that do not, 20 of which did (50 "
                  "percent). The ratio is 1.5, the difference 25 points, and the "
                  "odds ratio 3."),
            ("p", "These are counts of invented teams, and they show only that "
                  "the shares differ in that sample. The survey's finding is "
                  "also a correlation of survey answers, and the chapter does not "
                  "claim that moving tests from QA to developers causes a "
                  "result; it gives a theory and reports the correlation. The lab "
                  "cannot say whether the teams with developer-owned tests differ "
                  "in other ways, such as being smaller or newer, which would "
                  "also make the shares differ."),
            ("h3", "Exercise"),
            ("ul", [
                "25 teams that run their tests on every commit, 20 of which met "
                "the goal.",
                "25 teams that run them now and then, 10 of which did.",
            ]),
            ("p", "Work out each group's share, the ratio of the first to the "
                  "second, the difference in points and both groups' odds, then "
                  "the odds ratio. Type the two groups in to check. Say which of "
                  "the numbers answers &ldquo;how many times as likely?&rdquo; and "
                  "which would mislead someone who read it that way."),
            ("p", "The next lesson, Trunk-Based Development, reads the chapter's "
                  "finding on branches, counting a month of them against the "
                  "thresholds the authors name."),
        ],
        "lab": ("acckit", {
            "mode": "groups",
            "view": "likely",
            "preset": "tests",
            "presets": [
                {"id": "tests",
                 "label": "Developer-written acceptance tests against a separate QA team",
                 "rows": TESTS_ROWS, "first": "developers-own", "second": "separate-qa",
                 "expect": {
                     "agrShares": "developers-own 28 of 40 = 70%; separate-qa 20 of 50 = 40%",
                     "agrRatio": "1.75×",
                     "agrDiff": "+30 points",
                     "agrOdds": "3.50"
                 }},
                {"id": "config",
                 "label": "Configuration in version control against elsewhere",
                 "rows": CONFIG_ROWS, "first": "config-in-version-control",
                 "second": "config-elsewhere",
                 "expect": {
                     "agrShares": "config-in-version-control 45 of 60 = 75%; config-elsewhere 20 of 40 = 50%",
                     "agrRatio": "1.50×",
                     "agrDiff": "+25 points",
                     "agrOdds": "3"
                 }},
            ],
            "panel_title": "How many times as likely",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Comparing two groups of teams",
        "steps_intro": "Four steps, the last of them on teams of your own.",
        "steps": [
            ("Fix the goal first",
             "Decide what counts as meeting the goal before you look at the "
             "groups, and count each team once."),
            ("Work out each share",
             "Divide the teams that met the goal by the teams in the group. "
             "Keep it as a fraction until the end."),
            ("Take the ratio, not the odds",
             "Divide one share by the other for how many times as likely. "
             "Work out the odds ratio separately and do not use it for that."),
            ("Do it on your own teams",
             "Split the teams you know by one practice from this lesson, count "
             "how many in each met a goal, and type the counts in. Write down "
             "one other difference between the two groups that could explain "
             "the gap."),
        ],
        "worked": {
            "title": "Forty teams against fifty",
            "intro": [
                "Work out <code>tests</code> from its three numbers per group.",
            ],
            "lines": [
                "developers own: 28 / 40 = 70 percent",
                "separate QA: 20 / 50 = 40 percent",
                "ratio: 70 / 40 = 1.75",
                "difference: 70 - 40 = 30 percentage points",
                "odds: 28 / 12 = 7/3 against 20 / 30 = 2/3",
                "odds ratio: (7/3) / (2/3) = 3.5",
            ],
            "after": [
                "Both ratios are exact. 1.75 and 3.5 describe the same teams; "
                "they answer different questions, and only the first one is "
                "&ldquo;times as likely&rdquo;.",
            ],
        },
        "quiz_title": "What works, and the ratio",
        "quiz": [
            {"q": "In the preset <code>tests</code>, by what ratio were the teams "
                  "whose developers own the acceptance tests more likely than the "
                  "teams with a separate QA team to meet the goal?",
             "a": ["1.75", "3.5", "30", "0.57"],
             "c": 0,
             "why": "The shares are 70 and 40 percent, and 70 over 40 is 1.75. 3.5 "
                    "is the odds ratio, which the lab shows separately; 30 is the "
                    "difference in percentage points; 0.57 is the ratio the "
                    "other way round, QA over developers."},
            {"q": "According to the chapter, which went with delivery performance "
                  "more closely?",
             "a": ["Keeping system and application configuration in version "
                   "control, more than keeping application code",
                   "Keeping application code in version control, more than "
                   "configuration",
                   "The two were equally correlated",
                   "Neither: version control was uncontroversial and so not tested"],
             "c": 0,
             "why": "The chapter calls the comprehensive use of version control "
                    "relatively uncontroversial, but it tested it, and found "
                    "configuration the more highly correlated, a result it calls "
                    "a corrective to the idea that configuration is secondary."},
            {"q": "What does the chapter say about automated tests created and "
                  "maintained primarily by a QA team or an outsourced party?",
             "a": ["That practice was not correlated with IT performance",
                   "It was negatively correlated with IT performance",
                   "It was positively correlated, but less than developer tests",
                   "It was correlated only when the tests ran every day"],
             "c": 0,
             "why": "The authors report no correlation, not a negative one, and "
                    "they add that testers still have an essential role in manual "
                    "and exploratory work. Reading the finding as harm to "
                    "performance adds to what the page says."},
            {"q": "On the preset <code>config</code> (45 of 60 against 20 of "
                  "40), how many times as likely were teams that keep "
                  "configuration in version control to meet the goal?",
             "a": ["1.5", "3", "25", "0.75"],
             "c": 0,
             "why": "75 percent over 50 percent is 1.5. Three is the odds ratio "
                    "(3 to 1 against 1 to 1); 25 is the difference in points; "
                    "0.75 is the first group's share as a fraction, not a ratio."},
        ],
        "mistakes": [
            ("Concluding that the book wants testers gone",
             "The chapter says the opposite: testers do manual, exploratory, "
             "usability and acceptance testing, and help create and evolve the "
             "automated suites alongside developers. Its point is about who "
             "primarily writes and maintains the automated acceptance tests."),
            ("Treating configuration as a lesser concern than code",
             "This is the misconception the chapter names and answers. In the "
             "survey, the answers about configuration kept under version "
             "control went with delivery performance more closely than the "
             "answers about the application code kept there."),
            ("Reading a ratio of shares as the effect of the practice",
             "The ratio counts how much more often one group of teams met a goal. "
             "It does not say the practice made them. The teams may differ in age, "
             "size or domain, and the chapter itself offers a theory and "
             "reports a correlation, not an experiment."),
        ],
        "standard": (
            "Finish when you can compare two groups of teams.",
            "Given groups of teams and how many in each met a goal, work out the "
            "shares, the ratio, the difference in points and the odds ratio, "
            "say which answers \"how many times as likely\", and say what the "
            "chapter claims about each practice and what it does not."
        ),
        "note": (
            "The lab compares shares in the groups you type. It cannot say how "
            "teams were chosen into the groups, whether the practice or something "
            "else produced the gap, or whether a goal the teams set themselves "
            "is comparable across them; the survey's findings rest on its own "
            "sample and on answers about perception."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Trunk-Based Development (PDF pp. 91-92 of the operator's copy): fewer
    # than three active branches, lifetimes under a day, no freezes (p. 91);
    # GitHub Flow (pp. 91-92); Information Security (p. 92); Adopting
    # Continuous Delivery (p. 93).
    # Quote: PDF p. 91 of the operator's copy, 36 words, quotes.py OK.
    # Lesson total: 36 words.
    {
        "slug": "trunk-based-development",
        "title": "Trunk-Based Development",
        "module": "Chapter 4 · Technical Practices",
        "one_line": "Fewer than three active branches, each living under a day, and no freeze periods: the finding, the objection and the limit of each.",
        "summary": (
            "The chapter's findings on branching, the objection from teams used "
            "to GitHub Flow, and what the authors say about building security "
            "into the work and about the obstacles to adopting continuous "
            "delivery. Then read a month of branches against the three "
            "thresholds."
        ),
        "key": [
            "develop off trunk, not long-lived branches",
            "fewer than three active branches",
            "branches live under a day",
            "no code freeze or stabilization",
            "short branches are consistent with CI",
            "security built into the daily work",
            "architecture is the obstacle",
        ],
        "key_label": "Trunk-based development in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the other "
            "two are what the lab counts."
        ),
        "concepts": [
            ("Trunk-based development",
             "Working from the shared main line, trunk or master, with short-lived "
             "branches merged into it often, in place of long-lived feature "
             "branches merged now and then."),
            ("Active branch",
             "A branch that has been created and not yet merged. The lab "
             "counts a branch as open from the moment it is created until the "
             "moment it is merged, and one never merged as open to the end."),
            ("Freeze day",
             "A day on which the team stops adding to the release while it "
             "stabilizes. The chapter's strongest teams never needed one. The "
             "lab takes a list of such days."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read Trunk-Based Development, Information Security and Adopting "
            "Continuous Delivery in your own copy first. The lesson sets out "
            "the finding and its caveats, then reads a month of branches."
        ),
        "body": [
            ("p", "&ldquo;Teams that did well had fewer than three active "
                  "branches at any time, their branches had very short lifetimes "
                  "(less than a day) before being merged into trunk and never had "
                  "&ldquo;code freeze&rdquo; or stabilization periods.&rdquo; "
                  "That is Chapter 4's description of trunk-based development, "
                  "and the authors stress "
                  "that the result holds regardless of team size, organization "
                  "size or industry. What they compare it with is developing "
                  "on long-lived feature branches."),
            ("p", "The finding is a correlation with delivery performance, "
                  "and the authors take the strongest objection seriously. Some "
                  "developers who use GitHub Flow, which relies on branches and "
                  "merges to trunk only now and then, stay unconvinced. The "
                  "authors answer in two parts. First, they agree that short-lived "
                  "branches merged into trunk at least daily are consistent with "
                  "continuous integration. Second, in further research, teams "
                  "with short branch lifetimes and short merging and integration "
                  "periods, under a day for each, did better on delivery "
                  "performance than teams with longer ones. They hypothesise, "
                  "from experience and anecdote, that several long-lived "
                  "branches discourage refactoring and communication within a "
                  "team. They also say GitHub Flow suits open source projects "
                  "whose contributors are not full time, where it makes sense for "
                  "a part-time contributor's branch to live longer without being "
                  "merged."),
            ("p", "Two short sections follow. The first, Information Security, "
                  "reports that high-performing teams were more likely to build "
                  "security into the delivery process: their security people "
                  "gave feedback at every stage, from design to demos to help "
                  "with test automation, in a way that did not slow development, "
                  "and doing so contributed to delivery performance. Chapter 6 "
                  "returns to it. The second, Adopting Continuous Delivery, "
                  "sums up the chapter. The practices improve delivery "
                  "performance and quality and help culture, burnout and "
                  "deployment pain, but they often mean rethinking how teams work "
                  "and interact, and they cost substantial investment in "
                  "test and deployment automation. The authors name architecture "
                  "as a critical obstacle, because work to keep the automation "
                  "affordable depends on simple systems, and send the reader to "
                  "Chapter 5."),
            ("p", "Now the count. The lab takes the number of days, a list of "
                  "branches with the day and time each was created and merged "
                  "(a dash if still open), a list of freeze days, and three "
                  "thresholds. The book says fewer than three active "
                  "branches, so the limit is at most two; the lab also tests "
                  "that every lifetime is less than a day (24 hours) and that "
                  "there are no freeze days. The sample is invented: twenty "
                  "days of a team, with times written like 3.14:30 for day 3 "
                  "at half past two. A lifetime of exactly a day fails the "
                  "test, as the book's &ldquo;less than a day&rdquo; implies."),
            ("p", "In the preset <code>short</code> the team opens ten branches "
                  "in the twenty days and merges every one in under a day. No "
                  "more than 2 are ever open at once, the mean lifetime of the "
                  "merged branches is 9 hours 48 minutes, none reaches the "
                  "limit, none is open at the end and there are no freeze "
                  "days, so the sample meets all three thresholds. In the "
                  "preset <code>long</code> the team has eight branches, four "
                  "of which lived for 8, 12, 9 and 9 days, and one of which, "
                  "f4, is still open after at least 14 days. The most open at "
                  "once is 5, the mean lifetime of the 7 merged branches is "
                  "5 days 17 hours, 5 branches (those four and f4) have lived a "
                  "day or longer, 1 is open and 3 days were frozen, so it meets "
                  "none of the thresholds."),
            ("p", "Each tile is a count of what the log says, and the "
                  "thresholds are the book's survey-based description of "
                  "teams that did well, not a rule that guarantees anything. "
                  "The lab says nothing about why a branch lived long. A "
                  "branch may sit open for a good reason, such as waiting on a "
                  "decision, and the authors' hypothesis about refactoring "
                  "and communication is their own reading and not a "
                  "measurement of this sample."),
            ("h3", "Exercise"),
            ("ul", [
                "Ten days. Branches as `name, created, merged`, times as day.hh:mm: "
                "`a, 1.09:00, 3.12:00; b, 1.10:00, 1.15:00; c, 2.09:00, "
                "6.11:00; d, 4.09:00, 4.12:00; e, 5.09:00, -`.",
                "No freeze days.",
            ]),
            ("p", "Work out the most branches open at once, the "
                  "mean lifetime of the merged branches, which "
                  "branches have lived a day or longer and which are open, then type the "
                  "records in to check. Say which thresholds the sprint meets "
                  "and which single branch changes the answer."),
            ("p", "The next lesson, Types of Systems and Deployability, begins "
                  "Chapter 5 and asks what the chapter says about the "
                  "architecture that makes all of these practices possible."),
        ],
        "lab": ("acckit", {
            "mode": "branches",
            "view": "trunk",
            "preset": "short",
            "presets": [
                {"id": "short",
                 "label": "Twenty days, ten branches, none past a day",
                 "days": "20",
                 "branches": SHORT_BRANCHES,
                 "freezes": "",
                 "expect": {
                     "atbMaxActive": "2, first at 1.10:00",
                     "atbMeanLife": "9 h 48 min",
                     "atbOver": "0: none",
                     "atbOpen": "0: none",
                     "atbFreeze": "0: none",
                     "atbMetActive": "yes: at most 2 at once, and the threshold is at most 2 (fewer than three)",
                     "atbMetLife": "yes: every branch merged in less than 1 d",
                     "atbMetFreeze": "yes: 0 freeze days, and the threshold is at most 0"
                 }},
                {"id": "long",
                 "label": "Twenty days, long-lived branches, one still open and a freeze",
                 "days": "20",
                 "branches": LONG_BRANCHES,
                 "freezes": LONG_FREEZES,
                 "expect": {
                     "atbMaxActive": "5, first at 8.09:00",
                     "atbMeanLife": "5 d 17 h",
                     "atbOver": "5: f1 (8 d 3 h); f2 (12 d 1 h); f3 (9 d 6 h); f4 (open, at least 14 d 15 h); f5 (9 d 7 h)",
                     "atbOpen": "1: f4",
                     "atbFreeze": "3: day 18, day 19, day 20",
                     "atbMetActive": "no: 5 at once, and the threshold is at most 2 (fewer than three)",
                     "atbMetLife": "no: 5 branches lived 1 d or longer",
                     "atbMetFreeze": "no: 3 freeze days, and the threshold is at most 0"
                 }},
            ],
            "panel_title": "A month of branches against the thresholds",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Reading a branch log",
        "steps_intro": "Four steps, the last of them on your own repository.",
        "steps": [
            ("List each branch's times",
             "Write the day and time created and merged, or a dash if still "
             "open. The lifetime of a merged branch is merged minus created."),
            ("Count the branches open at once",
             "At each creation, count the branches created so far and not yet "
             "merged. The maximum is the largest of these."),
            ("Check the three thresholds",
             "Fewer than three active at once, every merged branch within "
             "a day, and no freeze day. A branch still open is a "
             "question, not a pass."),
            ("Do it on your own repository",
             "Take a month of your own branch history, list each branch with "
             "the days it lived, and type them into the lab. Write down the "
             "longest-lived branch and what kept it open."),
        ],
        "worked": {
            "title": "The long month",
            "intro": [
                "Work out the mean lifetime and the count over a day in "
                "<code>long</code>.",
            ],
            "lines": [
                "f1: 1.09:00 to 9.12:00 = 8 d 3 h = 195 hours",
                "f2: 289 hours; f3: 222 hours; f5: 223 hours",
                "s1: 5 hours; s2: 23 hours; s3: 2 hours",
                "f4 is open: not counted in the mean",
                "sum of the 7 merged: 195 + 289 + 222 + 223 + 5 + 23 + 2 = 959",
                "mean: 959 / 7 = 137 hours = 5 d 17 h",
                "a day or longer: f1, f2, f3, f5 and open f4: 5 branches",
            ],
            "after": [
                "The open branch is left out of the mean because it has no "
                "merge time yet. Counting it as living to the end of the period "
                "would raise the mean, and the lab lists it separately instead.",
            ],
        },
        "quiz_title": "Branches, thresholds and the chapter's claims",
        "quiz": [
            {"q": "In the preset <code>long</code>, what is the most branches "
                  "open at the same moment?",
             "a": ["5", "4", "8", "3"],
             "c": 0,
             "why": "From 8.09:00, when f5 is created, until f1 is merged at "
                    "9.12:00, the branches f1, f2, f3, f4 and f5 are all open: "
                    "5 at once. Eight is every branch in the log, never all open "
                    "together; 4 is the number of merged branches that lived "
                    "a day or longer; 3 is the number of freeze days."},
            {"q": "What is the mean lifetime of the merged branches in the "
                  "preset <code>long</code>?",
             "a": ["5 days 17 hours", "4 days 23 hours",
                   "8 days 3 hours", "5 days"],
             "c": 0,
             "why": "Seven branches were merged and their lifetimes add to 959 "
                    "hours; 959 over 7 is 137 hours. Dividing by 8 counts the "
                    "open branch f4 as having lifetime 0 and gives about 4 days "
                    "23 hours; 8 days 3 hours is only f1's lifetime; 5 is the "
                    "number of branches that have lived a day or longer."},
            {"q": "How does Chapter 4 treat the GitHub Flow workflow?",
             "a": ["Short-lived branches merged at least daily are consistent "
                   "with continuous integration, and GitHub Flow suits open "
                   "source projects with part-time contributors",
                   "As wrong in every setting, because any branching hurts "
                   "performance",
                   "As equivalent to trunk-based development whatever the "
                   "branch lifetime",
                   "As suitable for any team, provided it uses a pull request"],
             "c": 0,
             "why": "The authors accept short-lived branches merged at least daily, "
                    "found that teams whose branches and integration periods "
                    "last under a day did better than teams with longer ones, "
                    "and add that part-time contributors to open source can "
                    "reasonably keep branches longer."},
        ],
        "mistakes": [
            ("Thinking trunk-based development means no branches at all",
             "The chapter's description allows branches: fewer than three active, "
             "each short-lived and merged into trunk within a day. What it "
             "contrasts is long-lived feature branches and freeze periods."),
            ("Assuming the result is for small or modern teams only",
             "The authors point out that the result is independent of team "
             "size, organization size and industry. As with every finding "
             "in the book it is a correlation in their sample; it shows no "
             "exception, and it does not show one cannot exist."),
            ("Treating GitHub Flow as simply wrong",
             "The chapter agrees that short-lived branches merged daily are "
             "consistent with continuous integration, and says the workflow "
             "suits open source with part-time contributors. Its objection is "
             "to branches that live long."),
        ],
        "standard": (
            "Finish when you can read a branch log against the thresholds.",
            "Given a team's branches and freeze days, work out the active "
            "branches per day, the maximum, the mean lifetime of merged "
            "branches and which ran over a day, and say which of the chapter's "
            "three conditions the log meets."
        ),
        "note": (
            "The lab counts branches from a log you type, by whole days. It "
            "cannot say why a branch lived, whether trunk is kept releasable, "
            "or whether short branches are the cause of anything: the authors "
            "report a correlation with delivery performance and offer a "
            "hypothesis about why."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 5, Architecture: the opening (PDF p. 94 of the operator's
    # copy); Types of Systems and Delivery Performance (pp. 95-96); Focus on
    # Deployability and Testability (pp. 97-99, to the lead-in to the
    # Conway discussion).
    # Quote: PDF p. 94 of the operator's copy, 26 words, quotes.py OK.
    # Lesson total: 26 words.
    {
        "slug": "deployability-and-testability",
        "title": "Types of Systems and Deployability",
        "module": "Chapter 5 · Architecture",
        "one_line": "The kind of system a team builds does not predict its performance; whether it can test and deploy a part alone does.",
        "summary": (
            "Chapter 5 asks whether continuous delivery can work on mainframes, "
            "embedded systems and big balls of mud. Read what the survey found "
            "about system types and about the two architectural properties that "
            "did predict performance; then find the release groups in a shop's "
            "services and see what removing one tie does."
        ),
        "key": [
            "system type did not predict performance",
            "low performers: outsourced custom, mainframe",
            "testability and deployability did",
            "test without an integrated environment",
            "deploy independently of the services you use",
            "loose coupling, not the latest technology",
            "services that must release together are one",
        ],
        "key_label": "Types of systems in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Testability",
             "Being able to do most of a system's testing without an integrated "
             "environment, which the authors define as one where many separate "
             "services run side by side, a staging environment for example."),
            ("Deployability",
             "Being able to deploy or release an application independently of the "
             "other applications and services it depends on."),
            ("Release group",
             "A set of components joined by ties that say they must be released "
             "together, directly or through others. The lab finds the groups, "
             "the largest, and the components that belong to none."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read the opening of Chapter 5 and its next two sections, Types of "
            "Systems and Delivery Performance and Focus on Deployability and "
            "Testability, in your own copy first. The lesson sets out the "
            "finding and then finds the groups in a small system."
        ),
        "body": [
            ("p", "&ldquo;We found that high performance is possible with all "
                  "kinds of systems, provided that systems&mdash;and the teams "
                  "that build and maintain them&mdash;are loosely "
                  "coupled.&rdquo; That is the answer Forsgren, Humble and Kim "
                  "give at the start of Chapter 5, Architecture, to a question "
                  "that sits under the whole book: continuous delivery began in "
                  "web systems, so can it be applied to mainframes, firmware and "
                  "the tangle of thousands of tightly coupled systems found in "
                  "many enterprises?"),
            ("p", "The first section reports a search for a pattern. The survey "
                  "asked about eleven kinds of system, from new systems not yet "
                  "released to systems of record, packaged software, embedded "
                  "software and mainframes, both as the main system under "
                  "development and as a service that team's system integrates "
                  "against. Low performers were more likely to say their software "
                  "was custom software written by another company, such as an "
                  "outsourcing partner, and more likely to work on mainframe "
                  "systems, though integrating against a mainframe was not "
                  "significantly correlated with performance. For all the "
                  "other kinds there was no significant correlation. The authors "
                  "found that surprising, since they had expected packaged "
                  "software, systems of record and embedded systems to do worse, "
                  "and engagement systems and new systems to do better."),
            ("p", "Their conclusion is that it is the architecture's "
                  "characteristics that count and not the implementation: "
                  "achievable on packaged software and old mainframes, and "
                  "no guarantee on the latest services in containers if the "
                  "characteristics are ignored. They draw one more lesson "
                  "from the outsourcing finding: since delivery performance "
                  "affects organizational performance, as Chapter 2 argued, "
                  "the capability to build the core, strategic products should "
                  "be brought in-house."),
            ("p", "The next section names the characteristics. Two ideas were "
                  "more common among the high performers: that most testing can "
                  "be done without an integrated environment, and that the team "
                  "deploys or releases independently of the services it "
                  "depends on. The authors call them testability and "
                  "deployability and say they follow from systems that are "
                  "loosely coupled, meaning they can be changed and validated "
                  "independently. The 2017 survey tested a loosely coupled, "
                  "well-encapsulated architecture directly, and it turned out to "
                  "be the biggest contributor to continuous delivery in "
                  "that analysis, bigger than test and deployment automation. It "
                  "was gauged by whether a team can make large changes to its "
                  "design, and complete its work, without outside permission or "
                  "coordination; deploy on demand whatever it depends on; test on "
                  "demand without an integrated environment; and deploy in normal "
                  "business hours with negligible downtime."),
            ("p", "The authors add that service-oriented architecture and "
                  "microservices are supposed to deliver these properties, but "
                  "in practice many so-called service-oriented architectures do "
                  "not allow services to be tested and deployed independently, "
                  "and will not lift performance. Now the count. The lab takes "
                  "a list of components and a list of ties, each a pair that "
                  "must be released together, and finds the release groups. "
                  "The shop in the preset <code>shop</code> is invented: eight "
                  "services and five ties. It has 3 groups: one of six "
                  "services (cart, checkout, payments, pricing, catalog, "
                  "search) and two of one, email and reviews. So 2 components can "
                  "be released alone, and the largest group has 6."),
            ("p", "Take away one tie and see what it buys. The preset "
                  "<code>shop</code> carries the removal of the tie between "
                  "cart and pricing. After it there are 4 groups: cart, checkout "
                  "and payments; pricing, catalog and search; and the same two "
                  "single services. The largest group has 3, and the number "
                  "deployable alone is still 2. Removing one tie halved the "
                  "biggest group but freed nobody to ship alone, which is a "
                  "reminder that independence is a property of the whole set of "
                  "ties. The preset <code>ledger</code> is a bank's "
                  "mainframe ledger and four other services; the ledger has no "
                  "tie, and neither has the currency service. It has 3 groups, "
                  "2 components deployable alone and a largest group of 3."),
            ("p", "The lab is not a test of whether a tie is real. A pair "
                  "joined by a tie might share a database, a library or a "
                  "release calendar, and the lab sees only the list. The "
                  "preset <code>ledger</code> shows only what the chapter "
                  "says, that a mainframe component can be released alone "
                  "when nothing ties it to the rest."),
            ("h3", "Exercise"),
            ("ul", [
                "A clinic's components: `booking, notes, billing, reminders, "
                "labs`.",
                "Its ties: `booking, reminders; reminders, notes; billing, labs`.",
            ]),
            ("p", "Find the release groups by hand, say how many components can "
                  "be released alone and how large the largest group is, then "
                  "type them in. Then choose the one tie whose removal would "
                  "make the largest group smaller and say what the clinic would "
                  "need to change for it to go."),
            ("p", "The next lesson, A Loosely Coupled Architecture Enables "
                  "Scaling, reads what the authors found about how loosely "
                  "coupled teams grow."),
        ],
        "lab": ("acckit", {
            "mode": "release",
            "view": "independent",
            "preset": "shop",
            "presets": [
                {"id": "shop",
                 "label": "A shop's eight services, with the tie between cart and pricing removed",
                 "components": SHOP_COMPONENTS.replace(",", ""),
                 "ties": SHOP_TIES,
                 "remove": SHOP_REMOVE,
                 "expect": {
                     "arlGroups": "3: {cart, catalog, checkout, payments, pricing, search}, {email}, {reviews}",
                     "arlLargest": "6: cart, catalog, checkout, payments, pricing, search",
                     "arlAlone": "2: email, reviews",
                     "arlRemoved": "removing cart–pricing splits a group: 3 → 4 release groups",
                     "arlAfterGroups": "4: {cart, checkout, payments}, {catalog, pricing, search}, {email}, {reviews}",
                     "arlAfterAlone": "2: email, reviews"
                 }},
                {"id": "ledger",
                 "label": "A bank's mainframe ledger with no tie to the rest",
                 "components": LEDGER_COMPONENTS.replace(",", ""),
                 "ties": LEDGER_TIES,
                 "expect": {
                     "arlGroups": "3: {ledger}, {fx}, {portal, postings, statements}",
                     "arlLargest": "3: portal, postings, statements",
                     "arlAlone": "2: ledger, fx"
                 }},
            ],
            "panel_title": "Which components must go out together",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Finding the release groups",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the components",
             "Name each part that could be deployed. Include the ones with no "
             "ties, since they are the parts that can be released alone."),
            ("List the ties",
             "For each pair that must go out together, write the pair. A "
             "shared database, a shared library and a shared release "
             "calendar each count."),
            ("Group by following ties",
             "Start from one component and add everything tied to it, then "
             "everything tied to those. When no tie leaves the set, it is one "
             "group."),
            ("Do it on your own system",
             "List the services of a system you work on, and for each pair ask "
             "whether one can go out without the other. Type the ties in. "
             "Write down the largest group."),
        ],
        "worked": {
            "title": "Eight services and five ties",
            "intro": [
                "Find the groups in <code>shop</code>, then remove the tie "
                "between cart and pricing.",
            ],
            "lines": [
                "cart ties to checkout and to pricing",
                "checkout ties to payments; pricing to catalog; catalog to search",
                "group: cart, checkout, payments, pricing, catalog, search: 6",
                "email and reviews have no ties: two groups of one",
                "3 groups, largest 6, deployable alone 2",
                "remove cart-pricing: cart, checkout, payments: 3; pricing, catalog, search: 3",
                "4 groups, largest 3, deployable alone 2",
            ],
            "after": [
                "A group is a set in which you can walk from any component to any "
                "other along ties. Removing a tie can split a group in two, as "
                "here, or leave it whole if another path joins the same "
                "components.",
            ],
        },
        "quiz_title": "Groups, ties and the chapter's findings",
        "quiz": [
            {"q": "In the preset <code>shop</code> before the removal, how many "
                  "components can be released alone?",
             "a": ["2", "3", "6", "8"],
             "c": 0,
             "why": "Email and reviews have no ties. Three is the number of "
                    "groups, which counts the group of six as well; six is the "
                    "size of the largest group; eight is every component."},
            {"q": "In <code>shop</code>, after the tie between cart and pricing "
                  "is removed, what is the largest group?",
             "a": ["3", "5", "6", "4"],
             "c": 0,
             "why": "The six-service group splits into cart, checkout and payments "
                    "(3) and pricing, catalog and search (3). Five assumes the "
                    "removal takes away only one service; six is the largest "
                    "group before the removal."},
            {"q": "Which two kinds of system did the chapter find low performers "
                  "more likely to report?",
             "a": ["Custom software developed by another company, and mainframe "
                   "systems",
                   "Embedded software, and packaged commercial software",
                   "Systems of record, and systems of engagement",
                   "Software that integrates against a mainframe, and new "
                   "systems not yet released"],
             "c": 0,
             "why": "The authors found those two, outsourced custom software and "
                    "mainframe systems, and no significant correlation for most "
                    "other kinds, including embedded and packaged software, which "
                    "they had expected to do worse. Integrating against a "
                    "mainframe was not significantly correlated."},
            {"q": "Which statement does the chapter make about microservices and "
                  "service-oriented architecture?",
             "a": ["They are supposed to give testability and deployability, but "
                   "many service-oriented architectures do not let services be "
                   "tested and deployed independently",
                   "They guarantee higher performance on any platform",
                   "They are required for continuous delivery",
                   "They matter only on systems of engagement"],
             "c": 0,
             "why": "The chapter says the latest architecture is no guarantee of "
                    "higher performance if the characteristics are ignored, and "
                    "that many so-called service-oriented architectures will not "
                    "enable better performance."},
        ],
        "mistakes": [
            ("Expecting the kind of system to predict performance",
             "The authors expected packaged software, systems of record and "
             "embedded systems to do worse, and new and customer-facing systems "
             "to do better, and found otherwise for most kinds. Low performers "
             "were more likely to report outsourced custom software and "
             "mainframes; the rest showed no significant correlation."),
            ("Treating microservices as the same thing as loose coupling",
             "The chapter says a team can get the characteristics on packaged "
             "software and mainframes, and can miss them on the newest services "
             "in containers. It asks that services be tested and deployed "
             "independently, whatever they are called."),
            ("Concluding that legacy systems cannot perform",
             "The chapter says the characteristics are achievable even with "
             "packaged software and mainframes. The lab's <code>ledger</code> "
             "preset is a small illustration, not evidence: a mainframe "
             "component with no ties can be released alone."),
        ],
        "standard": (
            "Finish when you can find what must be released together.",
            "Given components and the ties that bind them, find the release "
            "groups, the largest group and the components deployable alone, "
            "and say what the chapter claims about system type and about "
            "testability and deployability."
        ),
        "note": (
            "The lab groups components from ties you type. It cannot find a "
            "hidden dependency, say whether a tie is worth removing, or show "
            "that a loosely coupled system performs better: the authors' "
            "finding is a correlation in their survey, built from answers about "
            "how a team works."
        ),
    },
]
