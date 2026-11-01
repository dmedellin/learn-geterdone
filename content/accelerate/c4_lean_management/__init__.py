"""Course 4 -- Security, Lean Management and Product Development: Chapters 6-8.

Five lessons in three modules, all in part_a: Chapter 6, Integrating Infosec
into the Delivery Lifecycle; Chapter 7, Management Practices for Software
(Lean Management Practices, then Implement a Lightweight Change Management
Process); Chapter 8, Product Development (Lean Product Development Practices,
then Team Experimentation and Effective Product Management Drives
Performance). References are to Nicole Forsgren, Jez Humble and Gene Kim,
Accelerate (IT Revolution, 2018), by chapter and section; PDF pages of the
operator's copy appear only in source comments. The design is
docs/accelerate/PLAN.md, section C, Course 4.
"""

from . import part_a

COURSE = {
    "slug": "accelerate-lean-management",
    "title": "Security, Lean Management and Product Development",
    "level": "Intermediate",
    "summary": (
        "Chapters 6, 7 and 8 of Accelerate, the three short chapters that take "
        "the research beyond the technical practices: security, the way work is "
        "managed, and the way products are developed. Each lesson sets out what "
        "the authors measured and found, in the book's own order, and then works "
        "one small calculation on a sample written for the lesson: the hours "
        "that security findings cost by the stage at which they are found, the "
        "lead time a work-in-progress limit buys when throughput holds, the wait "
        "each route of change approval adds, when the first customer feedback "
        "arrives from big and small batches, and the correlation between a "
        "lean-product score and a delivery score, with what it cannot say about "
        "which drives which."
    ),
    "blurb": (
        "Read the chapters on security, management and product development. "
        "Price a security finding by the stage that catches it, see what a "
        "work-in-progress limit does to lead time, compare the waits that three "
        "kinds of change approval add, count when feedback first arrives from "
        "big and small batches, and compute a correlation that cannot say which "
        "way the cause runs."
    ),
    "key": [
        "shift security left into the daily work",
        "make the secure way the easy way",
        "limit work in progress and show the work",
        "feed production data back to the team",
        "peer review and a pipeline, not a board",
        "small batches bring feedback sooner",
        "experiment freely, within the team's reach",
    ],
    "assumes_short": "Technical Practices and Architecture",
    "assumes_long": (
        "Technical Practices and Architecture, for continuous delivery and the "
        "deployment pipeline that the change-management lessons lean on, and "
        "Accelerate and Measuring Performance, for the four delivery measures "
        "that these chapters correlate their practices with"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of "
        "you, the calculations these three chapters rest on, and say what the "
        "authors found, how they measured it, and what the sample cannot show."
    ),
    "outcomes": [
        ("Price a late security finding",
         "Total the hours a set of security findings costs to remediate by the "
         "stage at which each is found, and say what the arithmetic assumes "
         "that the book does not report."),
        ("Apply Little's law to a board",
         "From a log of work items, find the average work in progress, the "
         "throughput and the average lead time, and show how a limit changes "
         "the lead time when throughput holds."),
        ("Compare routes of change approval",
         "Find the wait each route adds and the change fail rate of each, and "
         "say how few changes it takes for one failure to move a rate."),
        ("Time the first feedback",
         "Compute when the first customer feedback arrives from one big release "
         "and from several small ones, and what the extra releases cost."),
        ("Read a correlation about practices",
         "Compute Pearson's r between two scores, state what it shares, and say "
         "why it cannot tell which of the two drives the other."),
    ],
    "syllabus_intro": (
        "Five lessons in the book's order. The first reads Chapter 6, on "
        "security. The next two read Chapter 7: the Lean management practices, "
        "then the lightweight change management process. The last two read "
        "Chapter 8: Lean product development practices, then team "
        "experimentation and effective product management."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Each lesson names its chapter and sections, "
        "opens with at most one short quotation, and sets out the authors' "
        "findings in its own words.",
        "Read each finding as a survey's, of its sample. The book reports what a "
        "survey of people who work in technology found in the years it names, "
        "measured by what the respondents reported. Each lesson says so, and "
        "says where the authors state a limit.",
        "Treat each calculation as arithmetic on a sample of its own. The labs "
        "work small invented samples, a team of eight or twelve changes, and "
        "none is taken from the book. A figure shows what one measure says about "
        "that sample; it does not show what causes what, which the authors argue "
        "from theory and from years of data.",
        "Bring your own numbers. Every lesson ends by sending you to a team you "
        "know, and the labs take whatever records you type. Nothing you type "
        "leaves your browser.",
    ],
    "not_covered": [
        "The book's figures and tables, including the models of Figures 7.1, 7.2, "
        "8.1 and 8.2. The findings they draw are stated in the lessons' own words; "
        "the figures are better read in the book.",
        "The survey items behind each practice. The lessons describe what was "
        "asked at the level the chapters do, and Course 7 reads how the survey "
        "was built.",
        "The statistics behind the words &ldquo;predict&rdquo; and "
        "&ldquo;correlated&rdquo;. They are Chapter 12, read in Course 6, The "
        "Science Behind the Book; this course states the claims at the strength "
        "the chapters give them.",
        "The technical practices that the change-management chapter leans on, the "
        "deployment pipeline and continuous delivery. They are Chapters 4 and 5, "
        "read in Technical Practices and Architecture.",
        "The sections of Chapters 7 and 8 on burnout and culture, which point on "
        "to Chapter 9 and Chapter 3.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from a small "
        "sample a lesson states: hours by the stage a finding was caught, lead "
        "time as work in progress over throughput, waits and fail rates by "
        "approval route, feedback times from batch sizes, and a correlation "
        "between two scores. The samples are written for these lessons, and none "
        "is taken from the book. A figure shows what one measure says about one "
        "sample; it is not a finding about any team or organization, and the "
        "book's findings are its survey's."
    ),
    "lessons": part_a.LESSONS,
}
