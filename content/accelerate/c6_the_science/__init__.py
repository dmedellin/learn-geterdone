"""Course 6 -- The Science Behind the Book: Chapters 12 and 13.

Seven lessons in two modules: part_a reads Chapter 12, The Science Behind This
Book, in four lessons (primary and secondary, qualitative and quantitative
research and descriptive analysis; exploratory analysis; inferential
predictive analysis and what the book leaves unclaimed; classification
analysis) and the opening of Chapter 13, Introduction to Psychometrics (latent
constructs); part_b reads the rest of Chapter 13 (several views and rogue
data; latent constructs and system data). References are to Nicole Forsgren,
Jez Humble and Gene Kim, Accelerate: The Science of Lean Software and DevOps
(IT Revolution, 2018), by chapter and section; PDF pages of the operator's
copy appear only in source comments. The design is docs/accelerate/PLAN.md,
section C, Course 6.
"""

from . import part_a, part_b

COURSE = {
    "slug": "accelerate-the-science",
    "title": "The Science Behind the Book",
    "level": "Intermediate",
    "summary": (
        "Chapters 12 and 13 of the book: how the authors went from a survey to "
        "their findings, and why they think the survey can be trusted. Each "
        "lesson sets out what the chapter says and recomputes one figure of the "
        "kind it describes on a small sample written for the lesson: the numbers "
        "that describe a set of answers, the correlation that two rising series "
        "share by themselves, the correlation left when a third variable is held "
        "fixed, the order in which Ward's method merges nine teams, the score of "
        "a construct from its items, the averages that expose an item in the "
        "wrong construct, and Cronbach's alpha for a service's signals."
    ),
    "blurb": (
        "Read the two chapters that explain the method. Describe a team's "
        "answers and see which numbers tell two teams apart, find the "
        "correlation that comes from nothing but shared growth, hold a third "
        "variable fixed, merge teams into groups by Ward's method, score a "
        "construct from its items, find the item that belongs to the wrong "
        "construct, and compute the figure that says whether signals agree."
    ),
    "key": [
        "primary research, quantitative data",
        "correlation is only the exploratory stage",
        "drive means predict, from a stated theory",
        "groups from the data, named afterwards",
        "latent constructs: several items, one idea",
        "all measures are proxies, retest them",
    ],
    "assumes_short": "Accelerate and Measuring Performance",
    "assumes_long": (
        "Accelerate and Measuring Performance, for the four delivery measures and "
        "the three groups of performer that Chapter 12's classification produced; "
        "the arithmetic is shown line by line and needs no more than adding, "
        "squaring and a square root"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of you, "
        "the computations these two chapters describe in words, and say in the "
        "authors' terms what each shows and what it leaves out."
    ),
    "outcomes": [
        ("Describe a set of answers",
         "Find the count, mean, median, mode, range and both standard "
         "deviations of a set of answers, and say why two groups with the same "
         "centre can differ."),
        ("Separate a shared trend from a relationship",
         "Compute Pearson's r for two series and for their year-on-year changes, "
         "and say what a large r of the first and a small r of the second means."),
        ("Hold a third variable fixed",
         "Compute r over all rows, within each group and pooled, and say what "
         "the fall shows and what it does not."),
        ("Read a hierarchical clustering",
         "Work Ward's merge costs by hand, read the jump that marks where to "
         "stop, and say what the method does and does not know about good and "
         "bad."),
        ("Score and test a construct",
         "Reverse-code and average items, find an item that goes with the wrong "
         "construct from a correlation matrix, and compute Cronbach's alpha with "
         "and without each item."),
    ],
    "syllabus_intro": (
        "Seven lessons in the book's order. The first four read Chapter 12, The "
        "Science Behind This Book: kinds of research and description, exploratory "
        "analysis, inferential predictive analysis, and classification. The last "
        "three read Chapter 13, Introduction to Psychometrics: latent constructs, "
        "validity and rogue data, and the use of the same ideas on system data."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Each lesson names its chapter and sections, "
        "opens with at most one short quotation, and sets out the argument in its "
        "own words.",
        "Read the method as the authors' own account of it, and with their "
        "limits. The book names them: the data are perceptions reported on a "
        "survey, the analysis is inferential prediction and not a randomised "
        "study, and Martin Fowler's foreword asks how well the sample reflects "
        "the industry. These two chapters are where those limits are explained.",
        "Treat each figure as a figure of the sample the lesson states. The labs "
        "compute a summary, a correlation, a clustering, a score and a "
        "reliability on a small sample written for the lesson. What one measure "
        "says about that sample is not a finding about any team or organization, "
        "and a correlation in it is not a cause.",
        "Bring your own data. Every lesson ends by sending you to figures you "
        "know, and the labs take whatever records you type. Nothing you type "
        "leaves your browser.",
    ],
    "not_covered": [
        "The book's survey items, tables and figures, including the items of the "
        "culture construct, the failure-notification items, Westrum's table and "
        "the chapter's chart of spurious correlation. They are described in "
        "words and are better read in the book; the labs use samples of their "
        "own.",
        "The chapter's political example of a push poll, which is a fair "
        "illustration of bad survey writing and is best read in the book.",
        "Hypothesis tests and p-values. The labs compare statistics with "
        "thresholds the lesson states and print no significance, because the "
        "small samples could not support one.",
        "The tests of the measurement model, the relationship tests and the "
        "bias tests in full. Chapter 13 and Chapter 12 name them; Appendix C "
        "defines them, and Surveys, Data and Statistical Methods computes them.",
        "Queueing and flow, which have other homes in this library; none "
        "appears in these chapters.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the small "
        "sample a lesson states: summaries from a list of answers, correlations "
        "from pairs and series, merge costs from teams' coded answers, scores "
        "from items and reverse flags, averages from a matrix, and alpha from "
        "a table of signals. The samples are written for these lessons, and "
        "none is taken from the book. A figure shows what one measure says about "
        "that sample; it is not a finding about any team or organization, and a "
        "correlation in it is not a cause."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
