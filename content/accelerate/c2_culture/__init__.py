"""Course 2 -- Measuring and Changing Culture: Chapter 3.

Four lessons in one module. References are to Nicole Forsgren, Jez Humble and
Gene Kim, Accelerate: The Science of Lean Software and DevOps (IT Revolution,
2018), by chapter and section; PDF pages of the operator's copy appear only in
source comments. The design is docs/accelerate/PLAN.md, section C, Course 2.
"""

from . import part_a

COURSE = {
    "slug": "accelerate-culture",
    "title": "Measuring and Changing Culture",
    "level": "Introductory",
    "summary": (
        "Chapter 3, the one chapter of Accelerate that is about culture. The "
        "authors needed a model of culture they could measure and test, chose "
        "sociologist Ron Westrum's three types of organization, turned it into "
        "survey statements answered from strongly disagree to strongly agree, "
        "and found that the score predicts how well a team delivers software, "
        "how its organization performs and how satisfied its people are. Four "
        "lessons follow the chapter: the model, the measure, what the score "
        "predicts, and the claim that you act your way to a new culture. Each "
        "recomputes one step on a small sample written for the lesson: a "
        "team's mean on six aspects and where it falls among stated cut-points, "
        "a construct score with one reversed item, a correlation between a "
        "culture score and a delivery score, and the change in a team's scores "
        "between two surveys."
    ),
    "blurb": (
        "Read the chapter that makes culture something you can measure. Score "
        "seven people's answers on Westrum's six aspects, reverse a negatively "
        "worded item, correlate a culture score with a delivery score across "
        "eight teams, and compare a team's two surveys against a team that "
        "changed nothing."
    ),
    "key": [
        "culture is chosen at the level of values",
        "Westrum: three types on one scale",
        "a construct is the mean of its items",
        "reverse a negative item before you average",
        "culture predicts delivery performance",
        "behave your way to a new culture",
    ],
    "assumes_short": "Accelerate and Measuring Performance",
    "assumes_long": (
        "Accelerate and Measuring Performance, for the delivery measures that "
        "this chapter's culture score is set beside; a reader who has worked on "
        "or near a software team can follow either"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of "
        "you, the calculations Chapter 3 describes in words, and say what each "
        "one shows and what it leaves open."
    ),
    "outcomes": [
        ("Place a team on Westrum's scale",
         "Take respondents' answers on six aspects, find each person's mean and "
         "the team's, and say which type each falls nearest under a stated pair "
         "of cut-points, and why a team's mean can hide the spread."),
        ("Score a construct",
         "Reverse a negatively worded item, average the items for each "
         "respondent and for the team, and say what the score would have been "
         "had the reversal been forgotten."),
        ("Read a culture correlation",
         "Compute Pearson's r between a culture score and a delivery score "
         "across teams, read r squared as a share, and say why the chapter "
         "claims prediction and not cause."),
        ("Compare two surveys",
         "Find each respondent's change and the team's, say who moved between "
         "types, and say what a team that changed nothing shows about the size "
         "of an ordinary movement."),
    ],
    "syllabus_intro": (
        "Four lessons in the chapter's order: its model, its measure, its "
        "findings and its claim about change."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Each lesson names the chapter and sections it "
        "reads, opens with at most one short quotation, and sets out the "
        "argument in its own words.",
        "Read the findings as the authors' and the numbers as a sample's. The "
        "book reports what a survey of thousands of people found over several "
        "years. The labs work a handful of invented respondents and teams, so "
        "that you can see how each figure is made; they do not reproduce the "
        "book's data, and they do not test its claims.",
        "Treat each figure as one measure of one stated sample. A mean, a band or "
        "a correlation here says what the numbers you typed say. It is not a "
        "finding about any team, and a correlation in it is not a cause.",
        "Bring your own team. Every lesson ends by sending you to people you "
        "know, and the labs take whatever answers you type. Nothing you type "
        "leaves your browser.",
    ],
    "not_covered": [
        "The survey statements themselves and the chapter's figures and tables. "
        "The lessons name Westrum's three types and six aspects and describe "
        "them in their own words; the statements, Table 3.1 and Figures 3.1 to "
        "3.3 are better read in the book.",
        "How a construct is shown to be valid and reliable. Chapter 3 names the "
        "tests and points ahead; Cronbach's alpha, average variance extracted "
        "and composite reliability are worked in The Science Behind the Book "
        "and Surveys, Data and Statistical Methods.",
        "The technical and management practices that the chapter says move "
        "culture. They are Chapters 4, 7 and 8, read in Technical Practices and "
        "Architecture and in Security, Lean Management and Product Development.",
        "Blameless postmortems and the rest of how a team learns from "
        "failure. Chapter 3 argues that an investigation should not stop at "
        "human error; the practice is taken up in the chapters on people.",
        "Any judgement of your own organization. A score from a few answers "
        "says what those answers say, and no lab here grades a team.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the small "
        "sample a lesson states: respondents' means from the answers typed, "
        "bands from the cut-points the lesson states, construct scores from the "
        "items and the reversal given, and a correlation from the pairs listed. "
        "The samples are written for these lessons and none is taken from the "
        "book. A figure shows what one measure says about one stated sample; it "
        "is not a finding about any team or organization, and a correlation in "
        "it is not a cause."
    ),
    "lessons": part_a.LESSONS,
}
