"""Course 5 -- Sustainable Work, Satisfaction and Leadership: Chapters 9-11.

Seven lessons in three modules: part_a reads Chapter 9, Making Work
Sustainable (deployment pain, burnout), and the first four sections of
Chapter 10, Employee Satisfaction, Identity, and Engagement (loyalty and the
employee Net Promoter Score, identity and job satisfaction, diversity in
tech); part_b reads Chapter 11, Leaders and Managers (transformational
leadership, the role of managers). References are to Nicole Forsgren, Jez
Humble and Gene Kim, Accelerate: The Science of Lean Software and DevOps (IT
Revolution, 2018), by chapter and section; PDF pages of the operator's copy
appear only in source comments. The design is docs/accelerate/PLAN.md,
section C, Course 5.
"""

from . import part_a, part_b

COURSE = {
    "slug": "accelerate-people",
    "title": "Sustainable Work, Satisfaction and Leadership",
    "level": "Intermediate",
    "summary": (
        "Chapters 9, 10 and 11 of Accelerate, the part of Part I about the "
        "people who do the work. The authors asked whether software delivery is "
        "being achieved at the cost of the team, and measured the fear of "
        "deploying and burnout; they measured loyalty, identification with the "
        "organization and job satisfaction; they reported who answered their "
        "survey, by gender and by identification as underrepresented, and what "
        "other research says about diversity; and they measured leadership and "
        "described what managers can do. Each lesson sets out the chapter's "
        "argument and what the authors found, with the year and the sample, and "
        "then computes the same kind of figure on a small sample written for the "
        "lesson: a correlation, a score from survey items with a reversed item, "
        "an employee Net Promoter Score, two constructs side by side, a share "
        "and a ratio of shares, a leader's five dimension means, and a ratio "
        "that a third factor can explain away."
    ),
    "blurb": (
        "Read the chapters on the people. Correlate the fear of deploying with "
        "manual steps, score a team for burnout with a reversed item, work out an "
        "employee Net Promoter Score and see which answers move it, compare "
        "identity with satisfaction, see how a share of respondents differs from a "
        "share of an industry, score a leader on five dimensions, and find out "
        "what a ratio of two teams' shares can hide."
    ),
    "key": [
        "deployment pain goes with poorer outcomes",
        "fix the work, not only the person",
        "loyalty is promoters minus detractors",
        "identity and satisfaction are two scores",
        "diversity needs inclusion as well",
        "leaders enable; they do not deliver alone",
        "managers can invest in skills and time",
    ],
    "assumes_short": "Measuring and Changing Culture",
    "assumes_long": (
        "Measuring and Changing Culture, for the Westrum culture measure that "
        "deployment pain, burnout and identity are set beside, and the first "
        "course for how the authors' survey and its high, medium and low "
        "performers work; the arithmetic is averages, shares and one "
        "correlation, and a reader who can use a calculator can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of you, "
        "the computations these chapters rest on, and say what each figure shows "
        "about the sample and what it leaves to the authors' argument."
    ),
    "outcomes": [
        ("Correlate two measures",
         "Compute r and r squared for a few teams by hand, and say what one team "
         "can do to r when the sample is small."),
        ("Score a construct",
         "Reverse the reversed items, average a respondent's items and a team's "
         "respondents, and compare two constructs for the same team."),
        ("Compute an employee Net Promoter Score",
         "Sort answers into promoters, passives and detractors, subtract the "
         "percentages, and say which single answers could move the score."),
        ("Compare a sample with a population",
         "Compute each group's share, the ratio and the gap, and say when a share "
         "of respondents differs from a share of the field."),
        ("Read a ratio with care",
         "Say how many times as likely one group is, separate it from the gap and "
         "the odds ratio, and split by a third factor to see whether it holds."),
    ],
    "syllabus_intro": (
        "Seven lessons in the book's order. The first two read Chapter 9, Making "
        "Work Sustainable. The next three read Chapter 10: loyalty, then identity "
        "and job satisfaction, then diversity. The last two read Chapter 11, "
        "Leaders and Managers."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Each lesson names its chapter and sections, "
        "opens with at most one short quotation, and sets out the argument in its "
        "own words.",
        "Read each finding as a survey's, of a sample, in a year. The authors "
        "report what they found in their surveys of 2014 to 2017, and the lessons "
        "give the year and the sample wherever the book does. Where a figure is "
        "borrowed from other research, the lesson says whose it is.",
        "Treat each computed figure as a figure of the sample stated. The labs "
        "compute a correlation, a mean, a score or a ratio from a few invented "
        "teams or people. They show what one measure says about those few and "
        "never grade a team, an organization or a leader; a correlation is not "
        "a cause.",
        "Bring your own data. Every lesson ends by sending you to teams or "
        "survey answers you know, and the labs take whatever records you type. "
        "Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The book's figures, tables and survey items. The lessons describe the "
        "findings in their own words and write their own items; the book's "
        "wording is better read in the book.",
        "The measures of Chapters 3 and 4 to 8: the Westrum culture score, the "
        "technical practices, the Lean practices. They are read in earlier "
        "courses of this path.",
        "How the authors made sure their measures are sound, and why a survey of "
        "perceptions can be trusted. Part II does that, and the later courses "
        "read it: Chapter 13 for constructs, Chapters 14 and 15 and Appendix C "
        "for the survey, the sample and the statistics.",
        "The statistical tests behind the statements that a difference is "
        "significant. The labs compute descriptive figures and print no "
        "significance.",
        "Running anything. The labs count records you type; they cannot tell you "
        "whether a team is well led or well.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the small "
        "sample a lesson states: a correlation from the pairs of measures typed, "
        "a score from the items and answers typed with the reversed items turned "
        "round, an employee Net Promoter Score from the 0 to 10 answers, and "
        "shares and ratios from the counts of each group. The teams, answers and "
        "counts are written for these lessons, and none is taken from the book. "
        "The book's own findings are those of its survey, of its sample, in its "
        "years; a figure here shows what one measure says about the sample "
        "stated, and a correlation is not a cause."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
