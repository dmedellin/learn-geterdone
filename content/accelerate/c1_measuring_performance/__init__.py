"""Course 1 -- Accelerate and Measuring Performance: the Preface, Chapters 1
and 2.

Five lessons in three modules: part_a reads the Preface and Chapter 1,
Accelerate, in one lesson, and Chapter 2, Measuring Performance, in four.
References are to Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The
Science of Lean Software and DevOps (IT Revolution, 2018), by chapter and
section; PDF pages of the operator's copy appear only in source comments. The
design is docs/accelerate/PLAN.md, section C, Course 1.
"""

from . import part_a

COURSE = {
    "slug": "accelerate-measuring-performance",
    "title": "Accelerate and Measuring Performance",
    "level": "Introductory",
    "summary": (
        "The Preface, Chapter 1 and Chapter 2 of the book: where the research "
        "comes from, why the authors measure capabilities and not maturity, and "
        "how they measure the performance of software delivery. Each lesson sets "
        "out what the researchers found and how they measured it, and recomputes "
        "one kind of figure on a small sample written for it: a team's "
        "capabilities against a ladder of levels, the wait that grows as slack "
        "runs out, the four delivery measures from a log, the groups a clustering "
        "finds among ten teams, and the ratio behind \"twice as likely\"."
    ),
    "blurb": (
        "Read the opening of the book and its chapter on measurement. See what a "
        "single maturity level hides about a team, watch a wait grow without "
        "limit as utilization nears 100 percent, compute lead time, deployment "
        "frequency, change fail rate and time to restore from a fortnight's "
        "log, cluster ten invented teams with Ward's method, and tell a ratio of "
        "shares from a difference and an odds ratio."
    ),
    "key": [
        "capabilities, not a maturity level",
        "output and local measures mislead",
        "four measures, all team-level outcomes",
        "tempo and stability, together",
        "groups drawn by data, read by people",
        "a ratio of shares is not a cause",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no earlier course; you have worked on, with or near a team that builds "
        "and runs software"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of "
        "you, the computations these chapters rest on, and say in the authors' "
        "terms what each shows and what it leaves out."
    ),
    "outcomes": [
        ("Read a profile of capabilities",
         "Count which of the 24 capabilities a team has by category, find the "
         "level a stated ladder gives it, and name what the level hides."),
        ("Compute what high utilization costs",
         "Work out the wait and the lead time at a stated utilization in the "
         "simplest queueing model, and say why it has no answer at 100 percent."),
        ("Measure delivery from a log",
         "Compute lead time, deployment frequency, change fail rate and time "
         "to restore for a period, and read each on the book's own scale."),
        ("Cluster teams by Ward's method",
         "Merge teams by the cheapest increase in spread, write the fusion "
         "coefficient of each merge, and read the groups' medians in words."),
        ("Compare two groups three ways",
         "Compute the shares, the ratio, the difference and the odds ratio of "
         "two groups meeting a goal, and say why \"twice as likely\" is not a "
         "cause."),
    ],
    "syllabus_intro": (
        "Five lessons in the book's order. The first reads the Preface and "
        "Chapter 1. The other four read Chapter 2, Measuring Performance: the "
        "flaws in earlier measures, the four measures, the three groups of "
        "performer, and the link to the organization's results."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Each lesson names its chapter and sections, "
        "opens with at most one short quotation, and sets out the argument in its "
        "own words.",
        "Read the findings as a survey's. The book reports what four years of "
        "survey answers showed, and says so; Martin Fowler's foreword names the "
        "limits, that surveys capture perceptions and that the sample may not "
        "reflect the industry. Each lesson states a finding with its year and "
        "its source, and never as a promise about your team.",
        "Treat each figure as a figure of the sample the lesson states. The labs "
        "compute what the researchers computed, a profile, a wait, a measure, a "
        "cluster, a ratio, on a small sample written for the lesson. What one "
        "measure says about that sample is not a finding about any team or "
        "organization.",
        "Bring your own team. Every lesson ends by sending you to a team you "
        "know, and the labs take whatever records you type. Nothing you type "
        "leaves your browser.",
    ],
    "not_covered": [
        "The book's tables and figures: the tables of high, medium and low "
        "performers, the year-over-year charts and the diagrams of drivers and "
        "impacts. They are described in words where the argument runs through "
        "them and are better read in the book; the labs use samples of their own.",
        "The survey questions, whose wording is the authors' and is in "
        "copyright. The lessons say what was asked and name the answer options.",
        "The capabilities in detail. This course names all 24 and counts a "
        "profile of them; each is read in the course for the chapter that treats "
        "it, from Measuring and Changing Culture onward.",
        "Queueing theory. The one rule the second lesson uses is taught in the "
        "System Design path, in Queues and Utilisation, and is not repeated.",
        "The research method in full: constructs, reliability, sampling and the "
        "kinds of analysis are the subject of the later courses on the science "
        "behind the book and on surveys, data and statistical methods.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the small "
        "sample a lesson states: capabilities counted from the list a team is "
        "given, a wait from a utilization and a service time, measures from a "
        "log of changes and incidents, groups from teams' coded answers, and a "
        "ratio from two groups' counts. The samples are written for these "
        "lessons, and none is taken from the book. A figure shows what one "
        "measure says about that sample; it is not a finding about any team or "
        "organization, and a correlation in it is not a cause."
    ),
    "lessons": part_a.LESSONS,
}
