"""Course 7 -- Surveys, Data and Statistical Methods: Chapters 14 and 15 and
Appendix C.

Six lessons in three modules: part_a reads Chapter 14, Why Use a Survey (two
lessons), Chapter 15, The Data for the Project (one lesson), and the first two
sections of Appendix C, Statistical Methods Used in Our Research (tests for
bias; tests of the measurement model); part_b reads the appendix's last
sections (tests for relationships and classification). References are to
Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018), by chapter and section; PDF pages
of the operator's copy appear only in source comments. The design is
docs/accelerate/PLAN.md, section C, Course 7.
"""

from . import part_a, part_b

COURSE = {
    "slug": "accelerate-surveys-and-data",
    "title": "Surveys, Data and Statistical Methods",
    "level": "Intermediate",
    "summary": (
        "Chapter 14, Why Use a Survey, Chapter 15, The Data for the Project, and "
        "Appendix C, Statistical Methods Used in Our Research: why the authors "
        "asked people instead of reading a toolchain, how they reached the people "
        "they asked, and the tests they ran before they believed an answer. Each "
        "lesson sets out the authors' argument, then recomputes one of their "
        "checks on a small sample written for the lesson: the deploys a log "
        "misses, the weight of one suspect respondent, the people a snowball "
        "reaches, a chi-square test of early against late respondents, the "
        "validity and reliability of two constructs, and a correlation with its "
        "fitted line."
    ),
    "blurb": (
        "Read the part of Accelerate that defends and describes its own data. "
        "Compare a log with the work it misses, weigh one suspect respondent, "
        "follow a snowball sample from its seeds, test early against late "
        "respondents, check two constructs against the appendix's thresholds, and "
        "fit a line to five teams."
    ),
    "key": [
        "a log sees only what it records",
        "one liar among thousands moves a mean little",
        "no list of the population: ask for referrals",
        "the first invitations shape the sample",
        "compare early against late respondents",
        "every measurement test must pass",
        "r measures a straight line, not a cause",
    ],
    "assumes_short": "The Science Behind the Book",
    "assumes_long": (
        "The Science Behind the Book, for latent constructs, Likert-type items and "
        "cluster analysis, which this course tests and summarises; the arithmetic "
        "is done by hand on five to twenty numbers, and no earlier statistics is "
        "needed"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of you, "
        "the checks the authors describe in words, and say what each figure shows "
        "about the sample and what it leaves open."
    ),
    "outcomes": [
        ("Compare a log with the work",
         "Compute deployments, median lead time and change fail rate from a log, "
         "then again with a path the log does not record, and say which measures "
         "moved."),
        ("Weigh one respondent",
         "Score a construct with a reverse-worded item, and compute how far one "
         "respondent who answers every item the same moves the mean for a group "
         "of six and for a group of eleven."),
        ("Follow a snowball sample",
         "Count the people each wave reaches, the share of the sample that comes "
         "from each seed, and what disappears from the sample when one seed's "
         "community is missing."),
        ("Test early against late respondents",
         "Compute expected counts and a chi-square statistic for early and late "
         "respondents, and compare it with a critical value the lesson states."),
        ("Run the measurement-model tests",
         "Compute a construct's average variance extracted, composite reliability "
         "and square root, and test each against the appendix's thresholds."),
        ("Fit a line to a correlation",
         "Compute Pearson's r, the least-squares line and r squared for five "
         "teams, and say what a straight-line measure cannot see."),
    ],
    "syllabus_intro": (
        "Six lessons in the book's order. The first two read Chapter 14, the "
        "third Chapter 15, and the last three the parts of Appendix C that "
        "describe the tests for bias, the measurement model, and relationships "
        "and classification."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Each lesson names its chapter and sections, "
        "opens with at most one short quotation, and sets out the authors' "
        "argument in its own words.",
        "Read Chapters 14 and 15 as an argument and Appendix C as a reference. "
        "The chapters defend a choice, surveys and a snowball sample, and name "
        "its costs; the appendix lists tests and thresholds without working "
        "any. The lessons work them: each recomputes one test on a sample of "
        "its own, such as a hotfix path, a team of six respondents or two "
        "constructs with seven items, and none of it is the book's data.",
        "Treat each figure as what one measure says about one sample. A chi-square "
        "statistic, an average variance extracted or a correlation computed here "
        "describes the numbers a lesson states. The authors' findings are their "
        "survey's, of its sample, in its years, and nothing computed in these "
        "labs confirms or refutes them. The labs print no p-values.",
        "Bring your own numbers. Every lesson ends by sending you to a log, a "
        "survey or a set of scores you know, and the labs take whatever records "
        "you type. Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The survey items and the book's tables, figures and example data. The "
        "authors' items are theirs; the labs use invented items, invented teams "
        "and invented respondents, and the lessons cite the book's findings in "
        "prose.",
        "The science of constructs, reliability and clustering in Chapters 12 "
        "and 13. They are read in the previous course, The Science Behind the "
        "Book; this course tests what that one builds and does not repeat its "
        "prose.",
        "Significance testing in full. The appendix names t-tests, regression, "
        "partial least squares, analysis of variance and Tukey's test; the labs "
        "compute a chi-square statistic against a stated critical value and a "
        "correlation with its line, and they print no p-values. Reading further "
        "belongs to a statistics text.",
        "Principal components analysis and confirmatory factor analysis. The "
        "lessons take loadings as given and test them against the appendix's "
        "thresholds; estimating loadings from respondents' answers is outside "
        "these labs.",
        "Part III. Chapter 16, by Steve Bell and Karen Whitley Bell, and the "
        "Conclusion and Appendices A and B are read in the next course, "
        "Transformation.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the small "
        "sample a lesson states: deploys and their lead times from the records "
        "typed, construct scores from the answers typed, waves and shares from "
        "the referrals typed, chi-square from the counts typed, validity and "
        "reliability from the loadings typed, and a correlation from the pairs "
        "typed. The samples are written for these lessons, and none is taken "
        "from the book. A figure shows what one measure says about that sample; "
        "it is not a finding about any team or organization, and a correlation "
        "is not a cause."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
