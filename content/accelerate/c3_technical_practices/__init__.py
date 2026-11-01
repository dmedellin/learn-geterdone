"""Course 3 -- Technical Practices and Architecture: Chapters 4 and 5.

Seven lessons in two modules: part_a reads Chapter 4, Technical Practices
(continuous delivery, its impact, version control and tests, trunk-based
development), and the first part of Chapter 5, Architecture (types of systems,
deployability and testability); part_b reads the rest of Chapter 5 (loosely
coupled architecture and scaling, tools and architects). References are to
Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018), by chapter and section; PDF pages
of the operator's copy appear only in source comments. The design is
docs/accelerate/PLAN.md, section C, Course 3.
"""

from . import part_a, part_b

COURSE = {
    "slug": "accelerate-technical-practices",
    "title": "Technical Practices and Architecture",
    "level": "Introductory",
    "summary": (
        "Chapter 4, Technical Practices, and Chapter 5, Architecture: the part "
        "of Accelerate that asks what a team does with its code and its systems "
        "to deliver well. The authors define continuous delivery and report what "
        "it went with in their survey, from delivery performance to burnout; "
        "they say which practices around version control, tests and branches "
        "worked and which did not; and they ask what kind of architecture, and "
        "what kind of tool choice, lets a team ship without waiting for anyone. "
        "Each lesson sets out the argument and counts one thing on a small "
        "sample written for it: the wait a smaller batch removes, the share of a "
        "month spent on unplanned work, the ratio between two groups of teams, "
        "the branches over a day, the components that must go out together, the "
        "deploys per developer as an organization grows, and the teams a shared "
        "library draws into a release."
    ),
    "blurb": (
        "Read the chapters on technical practice and architecture. Compare "
        "batch sizes, split a month by kind of work, work out how many times "
        "as likely one group of teams is to meet a goal, read a month of "
        "branches against the trunk-based thresholds, find the services that "
        "must be released together and the teams a shared library pulls in."
    ),
    "key": [
        "continuous delivery is a set of capabilities",
        "small batches need cheap releases",
        "less unplanned work, less burnout",
        "developers own the acceptance tests",
        "short branches, no freezes",
        "test and deploy a part alone",
        "teams that need not coordinate to ship",
    ],
    "assumes_short": "Measuring and Changing Culture",
    "assumes_long": (
        "Measuring and Changing Culture, for the survey constructs and the "
        "performer classes that these chapters report their findings in; no "
        "programming is needed, though the practices are easier to picture if "
        "you have worked in a version-controlled codebase"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of "
        "you, the counts these chapters rest on, and say in the authors' terms "
        "what each count shows and what it leaves to the survey."
    ),
    "outcomes": [
        ("Compare batch sizes",
         "Work out the first release, the last release and the average wait for "
         "two batch sizes, and say what a cheaper release does to the trade."),
        ("Split time by kind of work",
         "Work out the share of new work, unplanned work and rework, and the hours "
         "freed when one kind is scaled, and say why the share of unplanned work "
         "is a proxy for quality and not a measure of it."),
        ("Compare groups of teams",
         "Work out how many times as likely one group is to meet a goal, the "
         "difference in points and the odds ratio, and keep the three apart."),
        ("Read a branch log",
         "Count active branches by day, lifetimes and freeze days, and say which "
         "of the chapter's three trunk-based conditions a log meets."),
        ("Find what must ship together",
         "Group components by their release ties, count the teams a group draws "
         "in, and compute deploys per developer per day as an organization "
         "grows."),
    ],
    "syllabus_intro": (
        "Seven lessons in the book's order. The first four read Chapter 4: "
        "continuous delivery, its impact, version control and tests, and trunk-"
        "based development. The last three read Chapter 5: types of systems and "
        "deployability, loosely coupled architecture and scaling, and tools and "
        "architects."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Each lesson names its chapter and sections, "
        "opens with at most one short quotation, and sets out the argument in its "
        "own words.",
        "Read each finding as a result of a survey. The authors measured "
        "practices as constructs from survey answers and report what went with "
        "what in their sample, in their years; the book names its limits, and "
        "so do these lessons. Where a lesson gives a figure from the book it says "
        "whose figure it is.",
        "Treat each count as a reason to look. The labs compute one measure on "
        "the small invented sample a lesson states: a wait, a share, a ratio, a "
        "branch count, a group, a rate. They show what that measure says about "
        "that sample; the book's findings are its survey's, and a correlation is "
        "not a cause.",
        "Bring your own team. Every lesson ends by sending you to a team or a "
        "system you know, and the labs take whatever records you type. Nothing "
        "you type leaves your browser.",
    ],
    "not_covered": [
        "The book's figures and tables: Figures 4.1 to 4.4 and 5.1 are described "
        "in the lessons in words and are better read in the book, and the lab "
        "samples are invented for these lessons.",
        "The survey items behind each capability. The book gives some of them, "
        "and these lessons paraphrase what the capabilities ask about and do not "
        "reproduce the wording.",
        "Security as a practice. Chapter 4's short section is read in the "
        "trunk-based development lesson; the next course reads Chapter 6.",
        "How to build a deployment pipeline, or to adopt any practice in a "
        "particular organization. The chapters report what went with performance, "
        "and the labs count; neither is a method for your team.",
        "Running code. The labs count records you type and never run them, so "
        "they cannot tell you whether a practice works for a team.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the "
        "small sample a lesson states: waits from the batch size and the "
        "hours, shares from the hours or the teams counted, branch counts from "
        "the days each branch was open, release groups from the ties typed in, "
        "and rates from the deploys, developers and days. The samples are "
        "written for these lessons, and none is taken from the book. A figure "
        "shows what one measure says about one sample; it is not a finding "
        "about any team, and a correlation is not a cause."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
