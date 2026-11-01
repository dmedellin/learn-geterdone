"""The Science Behind the Book, lessons 1-5 -- Chapters 12 and 13.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 12, The Science Behind This
Book (Primary and Secondary Research, Qualitative and Quantitative Research,
Types of Analysis, Descriptive Analysis, Exploratory Analysis, Inferential
Predictive Analysis, Predictive, Causal, and Mechanistic Analysis,
Classification Analysis, The Research in This Book); Chapter 13, Introduction
to Psychometrics (the opening, Trusting Data with Latent Constructs, and the
first of the three ways latent constructs help). Pages in the comments are PDF
pages of the operator's copy; the lessons cite by chapter and section. Every
quotation is copied from that copy and checked with quotes.py. The samples are
written for these lessons: none of the book's tables, figures, survey items or
data is reproduced. The design is docs/accelerate/PLAN.md, section C, Course 6.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)


# ---------------------------------------------------------------- 01 samples

# Ten people's answers to one statement on a seven-point scale, invented.
TEAM_A = "1, 3, 4, 5, 5, 6, 6, 6, 7, 7"
# A second invented team with the same mean, median and mode.
TEAM_B = "3, 4, 4, 4, 5, 6, 6, 6, 6, 6"
# 01 exercise: eight answers, one of them a 1.
EX_ONE = "1, 5, 5, 5, 6, 6, 6, 6"

# ---------------------------------------------------------------- 02 samples

# Eight invented years at a growing company: deploys per week, and cups of
# coffee sold per day at the office cafe. Both climb with the headcount.
GROWTH = (
    "1, 13, 60; 2, 19, 65; 3, 25, 68; 4, 28, 71; "
    "5, 33, 73; 6, 37, 79; 7, 43, 83; 8, 48, 86"
)
# The same deploys beside merged pull requests per week, whose yearly changes
# also keep step.
TOGETHER = (
    "1, 13, 30; 2, 19, 33; 3, 25, 36; 4, 28, 37; "
    "5, 33, 39; 6, 37, 41; 7, 43, 44; 8, 48, 46"
)
# 02 exercise: five years of a test suite's size (hundreds) and meeting-room
# bookings per week.
SUITE = "1, 10, 4; 2, 14, 7; 3, 17, 11; 4, 21, 14; 5, 24, 18"

# ---------------------------------------------------------------- 03 samples

# Twelve changes: review comments, days to merge, and the change's size.
SIZES = (
    "c1, 1, 1, small; c2, 2, 3, small; c3, 2, 2, small; c4, 3, 2, small; "
    "c5, 5, 4, medium; c6, 6, 6, medium; c7, 6, 5, medium; c8, 7, 5, medium; "
    "c9, 10, 11, large; c10, 11, 9, large; c11, 11, 10, large; "
    "c12, 12, 10, large"
)
# Twelve changes from three repositories, each holding a mix of sizes.
REPOS = (
    "c1, 1, 2, repo-a; c2, 5, 4, repo-a; c3, 10, 9, repo-a; c4, 12, 11, repo-a; "
    "c5, 2, 1, repo-b; c6, 6, 5, repo-b; c7, 9, 8, repo-b; c8, 11, 12, repo-b; "
    "c9, 3, 3, repo-c; c10, 4, 3, repo-c; c11, 8, 9, repo-c; c12, 12, 10, repo-c"
)
# 03 exercise: six changes in two repositories.
TWO_REPOS = (
    "e1, 1, 3, north; e2, 2, 2, north; e3, 3, 1, north; "
    "e4, 7, 9, south; e5, 8, 8, south; e6, 9, 7, south"
)

# ---------------------------------------------------------------- 04 samples

# Nine invented teams, each coded 1-6 on deploy frequency, lead time, time to
# restore and change fail rate, 6 being the best option on each scale.
NINE_TEAMS = (
    "T1, 6, 6, 6, 6; T2, 2, 1, 1, 1; T3, 5, 3, 5, 3; T4, 4, 4, 4, 4; "
    "T5, 6, 6, 5, 6; T6, 5, 6, 5, 5; T7, 1, 3, 2, 1; T8, 2, 1, 3, 1; "
    "T9, 3, 3, 4, 4"
)
# 04 exercise: four teams.
FOUR_TEAMS = "A, 1, 1, 1, 1; B, 2, 1, 1, 1; C, 5, 5, 5, 4; D, 6, 6, 5, 6"

# ---------------------------------------------------------------- 05 samples

# A four-item construct invented for the lesson; the third item is worded the
# opposite way round and is reverse-coded.
RELEASE_ITEMS = (
    "routine, release-confidence, no; unaided, release-confidence, no; "
    "dread, release-confidence, yes; clarity, release-confidence, no"
)
RELEASE_ANSWERS = (
    "R1, 5, 4, 1, 5; R2, 5, 6, 3, 4; R3, 3, 4, 4, 6; "
    "R4, 3, 2, 6, 3; R5, 7, 6, 1, 6; R6, 2, 3, 5, 5"
)
RELEASE_ITEMS_THREE = (
    "routine, release-confidence, no; unaided, release-confidence, no; "
    "dread, release-confidence, yes"
)
RELEASE_ANSWERS_THREE = (
    "R1, 5, 4, 1; R2, 5, 6, 3; R3, 3, 4, 4; "
    "R4, 3, 2, 6; R5, 7, 6, 1; R6, 2, 3, 5"
)
# 05 exercise: three items, the second reverse-coded, four people.
CALM_ITEMS = (
    "steady, calm, no; anxious, calm, yes; routine, calm, no"
)
CALM_ANSWERS = "A, 6, 2, 5; B, 3, 3, 3; C, 5, 1, 5; D, 2, 6, 3"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 12 opening (PDF p. 170 of the operator's copy); Primary and
    # Secondary Research (pp. 170-171); Qualitative and Quantitative Research
    # (pp. 171-172) with the Likert-type box (p. 172); Types of Analysis (p.
    # 173); Descriptive Analysis (pp. 173-175) with the population and sample
    # box (p. 174).
    # Quote: PDF p. 170 of the operator's copy, 22 words, quotes.py OK.
    # Lesson total: 22 words.
    {
        "slug": "primary-secondary-qualitative-quantitative",
        "title": "Primary and Secondary, Qualitative and Quantitative Research",
        "module": "Chapter 12 · The Science Behind This Book",
        "one_line": "Who collected the data, what form it takes, and what a handful of summary numbers can and cannot tell you.",
        "summary": (
            "Chapter 12 opens Part II by asking how the authors know that what they "
            "report is more than a coincidence. Read its two ways of sorting "
            "research, who collects the data and what form the data takes; its "
            "ladder of six kinds of analysis; and the first rung, description. Then "
            "describe two invented teams' answers to one survey statement and see "
            "which numbers tell them apart."
        ),
        "key": [
            "primary: the team collects new data",
            "secondary: someone else collected it",
            "qualitative: data not in numbers",
            "quantitative: data that includes numbers",
            "describe first: centre, spread, range",
            "a summary says what, never why",
        ],
        "key_label": "Chapter 12's first sections in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Chapter 12's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Primary and secondary research",
             "The difference is who collects the data. Secondary research works "
             "from data someone else collected, which is quicker and cheaper but "
             "bound by what already exists; primary research collects new data, "
             "which gives the researchers control over the questions and costs "
             "more. The authors place their own work in this class."),
            ("Quantitative data and the Likert-type scale",
             "Quantitative research uses data that includes numbers, whether from "
             "a system or from a survey that asks for answers on a scale. A "
             "Likert-type scale gives each answer a number: on the seven-point "
             "version the authors describe, strongly disagree is 1, neutral is 4 "
             "and strongly agree is 7."),
            ("Descriptive summary",
             "A handful of numbers that summarise a set of values: how many, where "
             "the middle is (mean, median, mode) and how far the values spread "
             "(range, standard deviation). The lab prints all of them for the "
             "values you type."),
        ],
        "read_title": "Two ways of sorting research, and the first rung of the ladder",
        "read_intro": (
            "Read the opening of Chapter 12 through Descriptive Analysis in your "
            "own copy first. The lesson follows the chapter, then describes two "
            "invented sets of answers."
        ),
        "body": [
            ("p", "&ldquo;Research falls into two broad classes: primary and secondary "
                  "research. The key difference between these two types is who "
                  "collects the data.&rdquo; That is Forsgren, Humble and Kim at the "
                  "start of Chapter 12, The Science Behind This Book. The chapter "
                  "answers a question that follows any claim about what makes teams "
                  "perform: how do you tell the actions that merely coincide with a "
                  "change from the ones that bring it about? Part II of the book is "
                  "their account of how they went about it, and this course reads "
                  "its first two chapters."),
            ("p", "The first sorting is by who gathered the data. Secondary research "
                  "summarises what someone else collected, as a school report or a "
                  "market study does; it is generally faster and cheaper, and the "
                  "authors add its limit, that the researcher is bound by whatever "
                  "data exists. Primary research collects new data; their example "
                  "is the national census taken every ten years. It can report what "
                  "is not already known and lets the team choose its questions, at "
                  "greater cost in money and time. They place their own work here, the "
                  "book and the State of DevOps Reports alike."),
            ("p", "The second sorting is by the form of the data. Qualitative "
                  "research is any whose data is not in numerical form, such as "
                  "interviews, blog posts, long-form log data and an ethnographer's "
                  "observations. It is rich and can reveal behaviour the researcher "
                  "did not expect, but it is harder and dearer to analyse, and "
                  "automated analysis usually turns it into numbers, which makes it "
                  "quantitative. Quantitative research is any with numbers in its "
                  "data, whether system data such as logs in numerical form or "
                  "survey data that asks for answers on a scale. Because a survey "
                  "need not be qualitative, the authors point out, what matters is "
                  "what the questions ask. Their own research is quantitative, since "
                  "it was collected with a Likert-type instrument."),
            ("p", "Quantitative research allows statistical analysis, and here the "
                  "chapter borrows a framework from Jeffrey Leek, a biostatistician "
                  "at Johns Hopkins: six types of analysis in order of increasing "
                  "complexity, where complexity means the knowledge the analyst "
                  "needs, the cost and the time. They are descriptive, exploratory, "
                  "inferential predictive, predictive, causal and mechanistic. The "
                  "authors say the analyses in their book fall into the first "
                  "three, and they add one more kind that does not fit the ladder "
                  "cleanly, classification. The next three lessons read those "
                  "rungs in turn, and the fourth reads classification."),
            ("p", "Descriptive analysis is the first rung. The data is summarised "
                  "and reported, as in a census, and the work takes the least effort. "
                  "It is often the first step of a longer analysis, to help a team "
                  "understand the data in hand and the sample behind it; a report "
                  "may also stop there. Two words matter before you read any "
                  "summary. The population is the whole group you want to learn "
                  "about, and the sample is the carefully defined portion of it "
                  "whose data you actually have. The authors' warning is that "
                  "a description is worth no more than the research design and "
                  "the way the sample was drawn behind it. Their own descriptive analysis in "
                  "the book is the profile of who answered, taken up in Chapter 10."),
            ("p", "Now describe a sample. The lab takes a list of values and prints "
                  "the count, the mean, the median, the mode or modes, the smallest "
                  "and largest value, the range, and the standard deviation twice. "
                  "The first sample is invented: ten people on a team answered one "
                  "statement on the seven-point scale. On the preset "
                  "<code>team-a</code>, with answers 1, 3, 4, 5, 5, 6, 6, 6, 7, 7, "
                  "it reports 10 answers, a mean of 5, a median of 5.5, a mode of 6, "
                  "a range of 6 and standard deviations of 1.789 and 1.886."),
            ("math", [
                "mean  =  (sum of the values) / n",
                "median  =  the middle value, or the mean of the two middle values",
                "mode  =  the value that appears most often",
                "range  =  largest value − smallest value",
                "population standard deviation  =  √( Σ(x − mean)² / n )",
                "sample standard deviation  =  √( Σ(x − mean)² / (n − 1) )",
            ]),
            ("p", "The two standard deviations answer slightly different questions. "
                  "Divide the sum of squared distances from the mean by n and you "
                  "have described the ten people as they are, a population of ten. "
                  "Divide by n − 1 and you have estimated the spread of a larger "
                  "group these ten were drawn from, which is the sample reading and "
                  "comes out a little larger. Chapter 12 does not print either "
                  "formula; they are standard statistics, and the lab shows both so "
                  "that neither is a surprise."),
            ("p", "Compare a second invented team. On <code>team-b</code>, with "
                  "answers 3, 4, 4, 4, 5, 6, 6, 6, 6, 6, the mean is again 5, the "
                  "median is again 5.5 and the mode is again 6. The range is 3 "
                  "instead of 6, and the standard deviations fall to 1.095 and "
                  "1.155. Three summaries are identical and two are not. The "
                  "first team contains a 1 and two 7s; the second is gathered "
                  "between 3 and 6. One mean cannot tell you which team you are "
                  "looking at, and neither can any number the lab prints say why "
                  "the first team is more spread out: a disagreement about the "
                  "statement, a reorganisation, a misread scale. That is a limit "
                  "of the first rung, and the reason the chapter has five more."),
            ("p", "One caution is the lesson's own, not the chapter's. A mean treats "
                  "the steps between 1 and 2, and between 6 and 7, as the same size, "
                  "which a Likert-type scale only assumes. The median and the mode "
                  "ask less of the numbers, so a summary that shows all three is "
                  "harder to over-read than a mean alone."),
            ("h3", "Exercise"),
            ("ul", [
                "Eight answers on the seven-point scale: `1, 5, 5, 5, 6, 6, 6, 6`.",
                "Type them into the lab and note the mean, median, mode, range and "
                "both standard deviations.",
                "Then change the 1 to a 5 and type them in again.",
            ]),
            ("p", "Say which summaries moved and which stayed put, and why the "
                  "median is the steadier of the two centres here. Work the first "
                  "set by hand before you type it, then check the lab."),
            ("p", "The first rung describes a sample and stops. The next lesson, "
                  "Descriptive and Exploratory Analysis, goes up to the second rung, "
                  "where the question becomes whether two things move together."),
        ],
        "lab": ("acckit", {
            "mode": "stats",
            "view": "describe",
            "preset": "team-a",
            "presets": [
                {"id": "team-a",
                 "label": "Ten invented answers on a seven-point scale",
                 "values": TEAM_A,
                 "expect": {"astN": "10", "astMean": "5", "astMedian": "5.5", "astMode": "6 (3 times)", "astMin": "1", "astMax": "7", "astRange": "6", "astPopSd": "≈ 1.789 (variance 3.2)", "astSampleSd": "≈ 1.886 (variance 32/9 ≈ 3.556)"}},
                {"id": "team-b",
                 "label": "A second team with the same mean, median and mode",
                 "values": TEAM_B,
                 "expect": {"astN": "10", "astMean": "5", "astMedian": "5.5", "astMode": "6 (5 times)", "astMin": "3", "astMax": "6", "astRange": "3", "astPopSd": "≈ 1.095 (variance 1.2)", "astSampleSd": "≈ 1.155 (variance 4/3 ≈ 1.333)"}},
            ],
            "panel_title": "Describing a set of answers",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Describing a set of values",
        "steps_intro": "Five steps, the last of them on answers of your own.",
        "steps": [
            ("List the values and count them",
             "Write the values in order from smallest to largest and count them. "
             "That count is n, and the order is what the median and the range "
             "read from."),
            ("Find the three centres",
             "Add the values and divide by n for the mean; take the middle value, "
             "or the mean of the middle two, for the median; find the value that "
             "appears most often for the mode, and write down every value that "
             "ties."),
            ("Find the spread",
             "Subtract the smallest from the largest for the range. Then square "
             "each value's distance from the mean, add the squares, divide by n "
             "for the population figure or n − 1 for the sample figure, and take "
             "the square root."),
            ("Say what the numbers leave out",
             "Write one question the summary cannot answer about the group, such "
             "as why the answers spread as they do or whether the people who "
             "answered stand for everyone."),
            ("Do it on answers of your own",
             "Take ten answers to one rating question from a survey you can see, "
             "type them into the lab, and compare the mean with the median. Write "
             "down which of the two you would trust more for that group."),
        ],
        "worked": {
            "title": "Ten answers described by hand",
            "intro": [
                "Describe the answers of <code>team-a</code>: 1, 3, 4, 5, 5, 6, 6, "
                "6, 7, 7.",
            ],
            "lines": [
                "sum = 1+3+4+5+5+6+6+6+7+7 = 50, n = 10",
                "mean = 50 / 10 = 5",
                "5th and 6th values are 5 and 6: median = 5.5",
                "6 appears three times: mode = 6",
                "range = 7 − 1 = 6",
                "distances from 5: −4 −2 −1 0 0 1 1 1 2 2",
                "squares: 16 4 1 0 0 1 1 1 4 4, sum = 32",
                "population: 32 / 10 = 3.2, root ≈ 1.789",
                "sample: 32 / 9 ≈ 3.556, root ≈ 1.886",
            ],
            "after": [
                "Every line uses the line before it, and nothing in them asks who "
                "the ten people are. That is why the same arithmetic is as easy to "
                "do on a poor sample as on a good one.",
            ],
        },
        "quiz_title": "Research types and summaries",
        "quiz": [
            {"q": "How does Chapter 12 classify the authors' own research?",
             "a": ["Secondary and quantitative: the survey answers were summaries "
                   "of existing reports",
                   "Primary and quantitative: the authors collected new data, using "
                   "a Likert-type survey",
                   "Primary and qualitative: surveys are always qualitative because "
                   "they do not come from computer systems",
                   "Secondary and qualitative: the authors interpreted other "
                   "people's interviews"],
             "c": 1,
             "why": "The chapter puts the book and the State of DevOps reports in "
                    "the primary class, because the team collected the data, and "
                    "quantitative, because the survey asked for answers on a "
                    "numerical scale. It also says outright that a survey is not "
                    "qualitative merely for failing to come from a machine; it "
                    "depends on what the questions ask."},
            {"q": "In the exercise, you change the 1 in 1, 5, 5, 5, 6, 6, 6, 6 to a "
                  "5. What happens to the summaries?",
             "a": ["The mean stays at 5, the median stays at 5.5 and only the range "
                   "falls",
                   "The mean and the median both rise by half a point and the "
                   "range falls from 5 to 1",
                   "The mean rises from 5 to 5.5, the median stays at 5.5 and the "
                   "range falls from 5 to 1",
                   "The mean rises from 5 to 5.5, the median falls to 5 and the "
                   "range falls from 5 to 1"],
             "c": 2,
             "why": "The first set sums to 40, so its mean is 5; its fourth and fifth "
                    "values are 5 and 6, so its median is 5.5. After the change the "
                    "sum is 44, so the mean is 5.5, the values 5, 5, 5, 5, 6, 6, 6, "
                    "6 still have 5 and 6 in the middle so the median is still 5.5, "
                    "and the range is 6 − 5 = 1. The one low answer pulled the mean "
                    "down and left the median alone, which is the point of the "
                    "exercise. The mode also changes: 6 appears four times in the "
                    "first set; in the second, 5 and 6 each appear four times, which "
                    "the lab reports as no mode, since every value occurs equally often."},
            {"q": "Both invented teams have a mean of 5, a median of 5.5 and a mode of "
                  "6. Which of these four summaries differs between them?",
             "a": ["The mean", "The median", "The mode", "The range"],
             "c": 3,
             "why": "The range is 7 − 1 = 6 for team-a and 6 − 3 = 3 for team-b. The "
                    "other three are equal by construction, so a reader who looked "
                    "only at the centre would take the teams to be alike."},
            {"q": "According to Chapter 12, where does descriptive analysis sit among "
                  "the types of analysis?",
             "a": ["First and simplest, often the first step and sometimes the "
                   "whole report, as with a census",
                   "Last and most complex, because it needs the most data",
                   "Second, after correlation has shown which variables to describe",
                   "Outside the ladder, with classification, because it makes no "
                   "use of numbers"],
             "c": 0,
             "why": "Leek's six types are listed in order of increasing complexity "
                    "and descriptive comes first. The chapter says it takes the "
                    "least effort, is often done first to understand the dataset, "
                    "and in some reports, a population census among them, is all "
                    "that is done. Classification is the one analysis the chapter "
                    "says does not fit cleanly into the ladder; description does."},
        ],
        "mistakes": [
            ("Calling a survey qualitative because it does not come from a machine",
             "Chapter 12 says this assumption is common and untrue. A survey is "
             "qualitative or quantitative according to the questions it asks. A "
             "survey whose answers are recorded on a numerical scale, as the "
             "authors' is, produces quantitative data, which is why the statistical "
             "analyses of the next lessons can be run on it."),
            ("Reading a mean as what the group thinks",
             "A mean is one number made from many. Two teams can share a mean, a "
             "median and a mode, as the two presets do, and still differ by a "
             "factor of two in range. Look at the spread, and at the values, "
             "before you say anything about the group."),
            ("Expecting a description to explain",
             "A summary says what the values are, never why. Chapter 12 puts "
             "description at the foot of its ladder because it asks the least; "
             "the questions of why two things go together, and whether one moves "
             "the other, belong to the rungs above it."),
        ],
        "standard": (
            "Finish when you can describe a set of answers.",
            "Given ten answers on the seven-point scale, find the mean, median, "
            "mode, range and both standard deviations, and name one question those "
            "numbers cannot answer."
        ),
        "note": (
            "The lab computes six summaries of the numbers you type. It cannot tell "
            "whether those numbers are a fair sample of any population, which the "
            "chapter says every descriptive claim depends on, or whether a "
            "one-to-seven code may be averaged at all."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Exploratory Analysis (PDF pp. 175-177 of the operator's copy), with the
    # Pearson footnote (p. 182, note 2) and the spurious-correlation example
    # (p. 176, Figure 12.1 on p. 177, named and never used as data).
    # Quote: PDF p. 176 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words.
    {
        "slug": "descriptive-and-exploratory-analysis",
        "title": "Descriptive and Exploratory Analysis",
        "module": "Chapter 12 · The Science Behind This Book",
        "one_line": "Correlation says how closely two measures move together, and two measures can do that for no reason that connects them.",
        "summary": (
            "The second rung of Chapter 12's ladder looks for relationships in the "
            "data, and its main tool is correlation. Read what exploratory "
            "analysis is for, what Pearson's r measures, and why the authors "
            "insist that it is only the exploratory stage; then compute r for two "
            "invented series that both climb with time, and again for their "
            "year-on-year changes."
        ),
        "key": [
            "exploratory: look for relationships",
            "correlation: how two variables move together",
            "r runs from −1 to 1; 0 is none",
            "a third variable or chance can do it",
            "shared growth gives r by itself",
            "correlation is the exploratory stage only",
        ],
        "key_label": "Exploratory analysis in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Exploratory analysis",
             "The second type of analysis in Leek's ladder. It looks for "
             "relationships among the variables, often with charts, and may find "
             "outliers, though the researcher must check that an outlier is not a "
             "legitimate member of the group. The authors call it where new "
             "hypotheses come from, and say that anyone who wants to speak of "
             "prediction or causation has to go further."),
            ("Pearson's r",
             "The correlation the authors report throughout. It rates how "
             "strongly two variables follow a straight line together, on a "
             "scale from −1 to 1: 1 when they move together exactly, −1 when they "
             "move in exactly opposite directions, 0 when they are not correlated "
             "at all."),
            ("Spurious correlation",
             "A strong correlation with nothing connecting the two measures but "
             "chance or a third variable. In the lab the third variable is time: "
             "two series that both grow every year correlate strongly whether or "
             "not either has anything to do with the other."),
        ],
        "read_title": "Looking for relationships, and why that is not the end",
        "read_intro": (
            "Read Exploratory Analysis in Chapter 12, with its footnote on Pearson "
            "correlations, in your own copy first. The lesson follows it, then "
            "computes r on two invented series."
        ),
        "body": [
            ("p", "&ldquo;Two variables moving together can always be due to a third "
                  "variable or, sometimes, just chance.&rdquo; That is the second "
                  "rung of Chapter 12's ladder in a sentence. Exploratory Analysis, "
                  "the section it comes from, follows Descriptive Analysis and "
                  "precedes the inferential rung, and it is where a team first "
                  "asks whether anything in its data goes with anything else."),
            ("p", "The authors call it a broad category: looking for relationships "
                  "among the data, perhaps with visualisations to show patterns, "
                  "and spotting outliers. They add a caution about the last of "
                  "those; a researcher has to be careful that an outlier really is "
                  "one, and not a legitimate member of the group. They also say "
                  "this is the enjoyable stage, where divergent thinkers generate "
                  "new ideas, new hypotheses and new projects, and in the next "
                  "breath that a team which wants to say anything about prediction "
                  "or causation has to go further."),
            ("p", "The tool of the stage is correlation. The chapter "
                  "says correlation shows how closely two variables rise and fall "
                  "together, or against each other, and not why. The measure the "
                  "authors report everywhere in the book is Pearson's r, which "
                  "their footnote describes as the strength of a linear "
                  "relationship, running from −1 through 0 to 1. The value is not "
                  "a percentage of anything, although the book itself writes the 0.9471 below as 94.71 percent. A scatter of points close to a rising "
                  "line gives r near 1, close to a falling line gives r near −1, "
                  "and a shapeless cloud gives r near 0."),
            ("math", [
                "r  =  Σ(x − mean of x)·(y − mean of y)",
                "      ÷ √( Σ(x − mean of x)²  ·  Σ(y − mean of y)² )",
            ]),
            ("p", "The chapter prints no formula, so the one above is standard "
                  "statistics. Read it as three sums over the pairs: how the two "
                  "measures vary together on top, and how each varies on its own "
                  "underneath, so that the result is the same whatever units each "
                  "is measured in. If both measures are above their means together "
                  "and below together, the top sum is large and positive."),
            ("p", "The chapter then makes its point with a joke that is also "
                  "serious. Tyler Vigen's website of spurious correlations, the "
                  "authors say, lists pairs of measures that correlate highly and "
                  "that common sense tells us are neither predictive nor causal. "
                  "Their Figure 12.1 shows per capita cheese consumption against "
                  "deaths by tangling in bedsheets, with r = 0.9471. Nobody "
                  "believes the one drives the other. Yet the authors warn that a "
                  "reader who goes looking through data for patterns will "
                  "find a story to tell about whatever turns up. Hence the "
                  "chapter's conclusion for this rung: report the correlations, "
                  "then go on to analyses that ask more."),
            ("p", "You can see one way such a correlation arises on a sample "
                  "written for this lesson. Eight years of an invented company, "
                  "a growing one: the number of deploys it makes per week, and "
                  "the cups of coffee its office café sells per day. Both rise "
                  "with the head count, and neither is connected to the other in "
                  "any way you would defend."),
            ("math", [
                "year             1    2    3    4    5    6    7    8",
                "deploys/week     13   19   25   28   33   37   43   48",
                "coffees/day      60   65   68   71   73   79   83   86",
                "change in deploys     6    6    3    5    4    6    5",
                "change in coffees     5    3    3    2    6    4    3",
            ]),
            ("p", "On the preset <code>shared-growth</code> the lab reports r = "
                  "0.994 for the levels, the figures as they stand. Nearly a "
                  "perfect line, and no reason to think the coffee has anything to "
                  "do with the deploys. The lab then differences the series: each "
                  "year's figure minus the year before, so that the steady climb "
                  "drops out and only the year-to-year movement is left. The "
                  "changes in the table are 6, 6, 3, 5, 4, 6, 5 against 5, 3, 3, "
                  "2, 6, 4, 3, and their r is exactly 0. Once the shared climb is "
                  "taken away, nothing is left that moves together. Differencing "
                  "is a standard device for series that trend with time; the book "
                  "does not use it, and it is here only to show where the 0.994 "
                  "came from. The lab's last tile does the comparing for you: the "
                  "changes' r is smaller in size than the levels', and one of the "
                  "two is 0."),
            ("p", "The device does not always empty a correlation, and it should "
                  "not be read as a test of cause. On the preset "
                  "<code>moving-together</code> the deploys are the same but the "
                  "second series is merged pull requests per week, 30, 33, 36, 37, "
                  "39, 41, 44, 46. The levels give r = 0.999, and the changes, 6, "
                  "6, 3, 5, 4, 6, 5 against 3, 3, 1, 2, 2, 3, 2, still give r = "
                  "0.955. The two really do rise and fall together year to year. "
                  "That is a stronger sort of correlation, and it is still only "
                  "one: a larger team may well produce both, which is the third "
                  "variable of the chapter's sentence, and the lab cannot show "
                  "whether it does."),
            ("h3", "Exercise"),
            ("ul", [
                "Five years of an invented company's test suite, in hundreds of "
                "tests, and its meeting-room bookings per week: `1, 10, 4; 2, 14, "
                "7; 3, 17, 11; 4, 21, 14; 5, 24, 18`.",
                "Find r for the levels. Then write the four year-on-year changes "
                "of each and find r for those.",
            ]),
            ("p", "Use the lab to check your arithmetic after you have done it by "
                  "hand. Say what the two answers tell you about the climb and "
                  "about the year-to-year movement, and what neither can tell you "
                  "about why the bookings follow the tests."),
            ("p", "Exploration finds the pattern; it cannot say what lies behind "
                  "it. The next lesson, Inferential Predictive Analysis, reads how "
                  "the authors go further without leaving the survey, by deciding "
                  "what they expect before they look."),
        ],
        "lab": ("acckit", {
            "mode": "stats",
            "view": "spurious",
            "preset": "shared-growth",
            "presets": [
                {"id": "shared-growth",
                 "label": "Eight invented years: deploys per week and café coffees per day",
                 "series": GROWTH,
                 "expect": {"astN": "8", "astRLevels": "≈ 0.994", "astRDiffs": "0", "astCompare": "smaller in size, no sign to compare, since one r is 0"}},
                {"id": "moving-together",
                 "label": "Deploys beside merged pull requests, whose changes also keep step",
                 "series": TOGETHER,
                 "expect": {"astN": "8", "astRLevels": "≈ 0.999", "astRDiffs": "≈ 0.955", "astCompare": "smaller in size, the same sign"}},
            ],
            "panel_title": "Correlation of the levels and of the changes",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Checking a correlation for a shared trend",
        "steps_intro": "Five steps, the last of them on two series of your own.",
        "steps": [
            ("Line the pairs up",
             "Write the two measures side by side, one pair per row, in time "
             "order. Check that every row is the same period for both."),
            ("Find r for the levels",
             "Find each mean, each distance from its mean, and the three sums. "
             "Divide the cross sum by the square root of the product of the other "
             "two."),
            ("Find r for the changes",
             "Subtract each figure from the next one, in both series, and find r "
             "again for the two lists of changes."),
            ("Compare the two, and name what is missing",
             "A large r of the levels and a small r of the changes means the "
             "series shared a trend. A large r of both means they also move "
             "together from year to year. Either way, write one candidate third "
             "variable."),
            ("Do it on series of your own",
             "Take two monthly counts from systems you know, such as deploys and "
             "tickets, type eight or more months into the lab, and read the two "
             "figures."),
        ],
        "worked": {
            "title": "The correlation of the levels by hand",
            "intro": [
                "Find r for <code>shared-growth</code>, using sums so that no "
                "fraction appears. Here n = 8, x is deploys and y is coffees.",
            ],
            "lines": [
                "Σx = 246, Σx² = 8550",
                "Σy = 585, Σy² = 43345",
                "Σxy = 18732",
                "top = 8·18732 − 246·585 = 149856 − 143910 = 5946",
                "x part = 8·8550 − 246² = 68400 − 60516 = 7884",
                "y part = 8·43345 − 585² = 346760 − 342225 = 4535",
                "r = 5946 / √(7884·4535) = 5946 / √35753940",
                "√35753940 ≈ 5979.5, so r ≈ 0.994",
            ],
            "after": [
                "The same three sums on the changes, with n = 7, give a top of "
                "7·130 − 35·26 = 0, so r is exactly 0 and the square root never "
                "matters. A top of zero is what the table of changes looks like "
                "when they have nothing in common.",
            ],
        },
        "quiz_title": "Correlation and its limits",
        "quiz": [
            {"q": "What does Pearson's r measure, as the chapter's footnote has it?",
             "a": ["The percentage of one variable's movement that the other causes",
                   "The strength of a linear relationship, from −1 to 1, with 0 "
                   "meaning not correlated at all",
                   "The strength of any relationship, linear or not, from 0 to 1",
                   "The probability that the relationship arose by chance"],
             "c": 1,
             "why": "The footnote describes it as the strength of a linear "
                    "relationship taking a value between −1 and 1, with 1 for "
                    "variables that move together exactly, −1 for exactly "
                    "opposite and 0 for none. It says nothing about cause, about "
                    "percentages of anything, or about chance."},
            {"q": "In the exercise, the levels of the test suite and the bookings "
                  "give r = 611/614 ≈ 0.995, and their year-on-year changes give "
                  "r = −1. What do the two figures show?",
             "a": ["The bookings are caused by the tests, and the changes only "
                   "confirm it",
                   "The correlation of the levels is wrong, because the changes "
                   "disagree with it",
                   "The series share a steady climb, and their yearly changes "
                   "move in exactly opposite directions",
                   "The changes cannot be correlated, because there are only four"],
             "c": 2,
             "why": "The changes in tests are 4, 3, 4, 3 and the changes in "
                    "bookings are 3, 4, 3, 4: when one is above its mean the "
                    "other is below, so the changes are perfectly negatively "
                    "correlated. Both series climb, which is what the near-perfect "
                    "r of the levels records. Neither is wrong; they measure "
                    "different things. Four changes are enough to compute r, "
                    "though too few to say much."},
            {"q": "On shared-growth the lab reports r = 0.994 for the levels and "
                  "r = 0 for the changes. What is the most the authors' "
                  "argument lets you conclude?",
             "a": ["The deploys drive the coffee sales, because r is close to 1",
                   "The coffee sales drive the deploys, because the changes are "
                   "not correlated",
                   "Neither series means anything, because r of the changes is 0",
                   "The two series share a trend; nothing in the correlation says "
                   "that either drives the other"],
             "c": 3,
             "why": "The chapter's position is that correlation says how closely "
                    "two variables move together and nothing about why. A shared "
                    "trend explains this pair's 0.994 without any link between "
                    "them. The zero for the changes does not make the series "
                    "meaningless; it shows that the correlation of the levels "
                    "came from the climb."},
            {"q": "What does Chapter 12 say an exploratory analysis should lead to?",
             "a": ["New hypotheses and more complex analyses, since it is not the "
                   "end for anyone who wants to speak of prediction or causation",
                   "A claim of causation, once r is above 0.9",
                   "A report that stops at the correlation, as with a census",
                   "The discarding of any outlier, because outliers distort r"],
             "c": 0,
             "why": "The authors call exploratory analysis the stage where "
                    "hypotheses and projects are generated, and say we report "
                    "correlations and then move on to more complex analyses. The "
                    "report that stops at the figures is the descriptive one. "
                    "Outliers are to be checked, not discarded, because one may "
                    "be a legitimate member of the group."},
        ],
        "mistakes": [
            ("Reading a high correlation as a connection",
             "Chapter 12 says a third variable, or sometimes plain chance, can "
             "always lie behind a pair that moves together, and illustrates it "
             "with a pair of measures nobody connects. The lab shows one route: two "
             "series that both climb with time correlate at 0.994 with nothing "
             "between them."),
            ("Treating r as a percentage",
             "Pearson's r is a coefficient between −1 and 1, not a share of "
             "anything. An r of 0.5 is not half of a perfect relationship in any "
             "sense you can act on. Squaring it gives the share of variance a "
             "straight line accounts for, which the last lesson of Surveys, Data and Statistical Methods "
             "takes up."),
            ("Taking a zero correlation to mean nothing is going on",
             "Pearson's r measures a linear relationship only. A pair that moves "
             "in a curve can have r near 0, and a zero r of the changes, as on "
             "the first preset, shows only that no common movement is left once "
             "the climb is removed from this sample."),
        ],
        "standard": (
            "Finish when you can say what a correlation does and does not show.",
            "Given two series, find r for the levels and for the year-on-year "
            "changes, say whether they share a trend, and name one third variable "
            "that could account for the match."
        ),
        "note": (
            "The lab computes r of the levels and of the changes for the series you "
            "type. It cannot tell you whether a third variable exists, whether the "
            "relationship is a straight line, or whether eight years is enough to "
            "say anything about the next eight."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Inferential Predictive Analysis (PDF pp. 177-179 of the operator's copy);
    # Predictive, Causal, and Mechanistic Analysis (pp. 179-180); Appendix C,
    # Tests for Relationships (pp. 270-271) for the statement that unsupported
    # relationships are reported as correlations only; Fowler's foreword
    # (pp. 15-16) for the caution about perception and sample.
    # Quote: PDF p. 178 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "inferential-predictive-analysis",
        "title": "Inferential Predictive Analysis",
        "module": "Chapter 12 · The Science Behind This Book",
        "one_line": "State what you expect from a theory first, then test it: how the book's word drive is meant, and what it does not claim.",
        "summary": (
            "The third rung is where the book's headline claims live. Read how the "
            "authors choose hypotheses from theory to avoid fishing for "
            "correlations, which methods they use to test them, and which three "
            "rungs of the ladder they did not climb and why. Then hold a third "
            "variable fixed in an invented sample of twelve changes and watch a "
            "strong correlation shrink."
        ),
        "key": [
            "hypotheses come from theory, then data",
            "drives = predicts, in the book's design",
            "regression tests the hypotheses",
            "causal analysis needs randomised study",
            "the book did not do causal analysis",
            "hold a third variable fixed and recompute",
        ],
        "key_label": "Inferential predictive analysis in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Inferential predictive analysis",
             "The third rung, very common in business and technology research, "
             "used where a purely experimental design is not possible. A "
             "hypothesis is stated beforehand and has to rest on a "
             "well-developed theory; data is then collected to test it. The "
             "authors say every place in the book that talks of impacting or "
             "driving a result used this design."),
            ("Causal analysis",
             "The rung the authors call the gold standard and did not climb. It "
             "generally requires randomised studies, as in an A/B test of a "
             "website, and it is the hardest analysis to carry out in most "
             "business and technology settings."),
            ("Holding a third variable fixed",
             "Looking at the relationship between two measures within each group "
             "of a third variable, so that differences between groups cannot "
             "drive the result. The lab reports r over all rows, r in each group, "
             "and a pooled within-group r that combines the groups."),
        ],
        "read_title": "Hypothesis first, data second, and what is left unclaimed",
        "read_intro": (
            "Read Inferential Predictive Analysis and Predictive, Causal, and "
            "Mechanistic Analysis in Chapter 12 in your own copy first. The lesson "
            "reads them as the book's account of what its findings are, then "
            "works a third-variable example."),
        "body": [
            ("p", "&ldquo;Science is done by stating hypotheses, designing research to "
                  "test those hypotheses, collecting data, and then testing the "
                  "stated hypotheses.&rdquo; Forsgren, Humble and Kim write that in "
                  "Inferential Predictive Analysis, the section of Chapter 12 that "
                  "tells you what kind of finding most of the book is. It is the "
                  "section to hold in mind when a later chapter says that a "
                  "practice drives performance."),
            ("p", "The authors say inferential design is one of the most common in "
                  "business and technology research. It is used to understand "
                  "things like the effects of HR policies, motivation, and how "
                  "technology affects satisfaction, efficiency and organisational "
                  "performance, in settings where a purely experimental design is "
                  "not possible. A company will not sacrifice earnings so that a researcher "
                  "can have a tidy control group, and the data comes from "
                  "working organisations, not from a laboratory."),
            ("p", "Their safeguard against hunting for patterns, the habit that "
                  "produced the spurious pair of the last lesson, is that "
                  "theory comes first and drives the hypotheses. A hypothesis has to rest on a "
                  "theory that is mature and has good support before the data is "
                  "touched. The authors anticipate the objection that this invites "
                  "confirmation bias, and answer that it is how science is done, "
                  "with a qualification: science is not simply confirming what the "
                  "team hoped to find, but stating hypotheses, designing the "
                  "research to test them, collecting the data and testing. Each "
                  "further piece of supporting evidence earns the hypothesis a "
                  "little more trust."),
            ("p", "Their examples are the book's main claims: that continuous "
                  "delivery and architecture practices drive software delivery "
                  "performance, that software delivery performance positively "
                  "affects organisational performance, and that organisational "
                  "culture positively affects both. The statistical methods were "
                  "multiple linear regression or partial least squares, which Appendix C describes and Surveys, Data and Statistical Methods reads. "
                  "Appendix C adds the matching rule: where no supporting theory "
                  "suggests a predictive relationship, the authors report only the "
                  "correlation."),
            ("p", "Read &ldquo;drive&rdquo; with that in mind. The chapter says that "
                  "whenever the book speaks of impacting or driving results, the "
                  "design was this third type: a theory-based hypothesis tested "
                  "on survey data to see whether one measure predicts another. "
                  "The last three rungs were not part of the research, because "
                  "the authors did not have the data they need. Predictive "
                  "analysis forecasts future events from past ones and, they "
                  "note, gets harder the further ahead it looks. Causal analysis "
                  "they call the gold standard; it generally calls for "
                  "randomised studies, such as the A/B tests companies run on "
                  "websites and prototypes. Mechanistic analysis works out the "
                  "exact change to make to cause an exact behaviour, is rare in "
                  "business, and is not suited to complex systems."),
            ("p", "Be fair to both sides of that. The authors are plain that they "
                  "did not run the randomised studies that causal analysis "
                  "needs, and the book is not best read as proof of cause. They "
                  "argue instead that a hypothesis chosen from theory and tested "
                  "against several years of data earns confidence. Martin "
                  "Fowler's foreword adds a reader's cautions: the data are "
                  "surveys of perception, he wonders how the sample reflects the "
                  "wider world of IT, and he asks for confirmation by other teams "
                  "using other approaches, admitting that the conclusions confirm "
                  "much of his own advocacy and that confirmation bias is a strong "
                  "force. Both the claim and the caution belong in your "
                  "reading."),
            ("p", "The lab shows one thing a theory-driven analysis has to guard "
                  "against. Twelve invented changes to a codebase each have a "
                  "number of review comments, the days they took to merge, and a "
                  "size: small, medium or large. On the preset "
                  "<code>size-explains</code> the lab reports r over all twelve "
                  "rows of 0.964, a very strong positive correlation. Then it "
                  "looks inside each size. Within small changes r is 0.5, "
                  "within medium 0.5, within large −0.5. Combining the three "
                  "groups' sums of squares and products into one pooled "
                  "within-group r gives 0.167. The lab's last tile compares the two "
                  "figures: the pooled one is smaller in size and has the same "
                  "sign, and a tile above lists the three groups it found, "
                  "small, medium and large."),
            ("math", [
                "r (all rows)       =  Sxy / √(Sxx · Syy)",
                "r (within group g) =  Sxy(g) / √(Sxx(g) · Syy(g))",
                "r (pooled within)  =  Σg Sxy(g) / √( Σg Sxx(g) · Σg Syy(g) )",
                "where Sxx = Σ(x − mean of x)², Syy = Σ(y − mean of y)²,",
                "and Sxy = Σ(x − mean of x)·(y − mean of y)",
            ]),
            ("p", "What the drop shows is that most of the correlation between "
                  "comments and days comes from the differences between the sizes. "
                  "Large changes have more comments and also take longer, and the difference between the "
                  "three sizes carries almost all of the 0.964. That is what a "
                  "third variable doing the work looks like. It is not a "
                  "finding that size causes either; it is a reason to ask what "
                  "else is not held fixed, and a reason the authors begin from "
                  "theory."),
            ("p", "The second preset is the contrast. On <code>size-explains-"
                  "nothing</code> the lab takes twelve changes from three "
                  "repositories, each with a mix of small and large ones. All "
                  "the rows give r = 0.967 and the pooled within-repository r is "
                  "also 0.967. Holding the repository fixed barely changes it (the "
                  "last tile still calls it smaller, in the fourth decimal), so "
                  "whatever ties comments to days here, the repository is not "
                  "it. That does not make the association causal; it says only "
                  "that this third variable is not the explanation."),
            ("h3", "Exercise"),
            ("ul", [
                "Six invented changes in two repositories, as records of name, "
                "comments, days and repository: `e1, 1, 3, north; e2, 2, 2, "
                "north; e3, 3, 1, north; e4, 7, 9, south; e5, 8, 8, south; e6, "
                "9, 7, south`.",
                "Find r over all six rows, r in each repository, and the pooled "
                "within-repository r.",
            ]),
            ("p", "Do the arithmetic by hand first, then check it in the lab. Say "
                  "what the sign does between the first answer and the other two, "
                  "and what a manager reading only the first would be tempted to "
                  "ask for."),
            ("p", "Not every analysis in the book starts from a hypothesis. The next lesson, "
                  "Classification Analysis, reads how the authors sorted teams into "
                  "high, medium and low performers."),
        ],
        "lab": ("acckit", {
            "mode": "stats",
            "view": "confound",
            "preset": "size-explains",
            "presets": [
                {"id": "size-explains",
                 "label": "Twelve invented changes grouped by size",
                 "rows": SIZES,
                 "expect": {"astN": "12", "astGroups": "3: small, medium, large", "astR": "≈ 0.964", "astWithin": "small 0.5 (n = 4); medium 0.5 (n = 4); large −0.5 (n = 4)", "astPooled": "≈ 0.167", "astCompare": "smaller in size, the same sign"}},
                {"id": "size-explains-nothing",
                 "label": "Twelve changes from three repositories, each with a mix of sizes",
                 "rows": REPOS,
                 "expect": {"astN": "12", "astGroups": "3: repo-a, repo-b, repo-c", "astR": "≈ 0.967", "astWithin": "repo-a ≈ 0.990 (n = 4); repo-b ≈ 0.988 (n = 4); repo-c ≈ 0.950 (n = 4)", "astPooled": "≈ 0.967", "astCompare": "smaller in size, the same sign"}},
            ],
            "panel_title": "The correlation before and after holding a third variable fixed",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Holding a third variable fixed",
        "steps_intro": "Five steps, the last of them on a table of your own.",
        "steps": [
            ("Choose the measures and the grouping before you look",
             "Write down the two measures, and a third variable you suspect, "
             "and say why. The book's rule is that the reason comes from theory "
             "first and the data second."),
            ("Find r over all rows",
             "Compute r for the two measures across every row, ignoring the "
             "groups. This is the figure a report would quote."),
            ("Find r inside each group",
             "Compute r again within each group of the third variable, using only "
             "that group's rows. A group needs at least three rows, and some "
             "variation in both measures."),
            ("Pool the groups",
             "Add the groups' sums of squares and products and form r from the "
             "totals. This is the relationship with the groups' differences "
             "removed."),
            ("Do it on a table of your own",
             "Take two measures from a system you know, such as review comments "
             "and days to merge, add a grouping such as repository or team, and "
             "type at least nine rows into the lab. Write down the three figures."),
        ],
        "worked": {
            "title": "The pooled within-group r by hand",
            "intro": [
                "Find the pooled r for <code>size-explains</code>. Each size has "
                "four changes.",
            ],
            "lines": [
                "small: x = 1,2,2,3  y = 1,3,2,2  Sxx = 2  Syy = 2  Sxy = 1",
                "medium: x = 5,6,6,7  y = 4,6,5,5  Sxx = 2  Syy = 2  Sxy = 1",
                "large: x = 10,11,11,12  y = 11,9,10,10  Sxx = 2  Syy = 2  Sxy = −1",
                "totals: Sxx = 6, Syy = 6, Sxy = 1",
                "pooled r = 1 / √(6·6) = 1/6 ≈ 0.167",
            ],
            "after": [
                "Each group's sums are measured about that group's own means, so "
                "the large gaps between the three sizes never enter. Over all "
                "twelve rows the sums are Sxx = 506/3, Syy = 410/3 and Sxy = "
                "439/3, which gives 439 / √(506·410) ≈ 0.964. The two figures "
                "come from the same twelve rows.",
            ],
        },
        "quiz_title": "Hypotheses, rungs and third variables",
        "quiz": [
            {"q": "Which type of analysis does Chapter 12 say lies behind the "
                  "book's statements that practices drive or impact performance?",
             "a": ["Causal analysis, with randomised studies of teams",
                   "Inferential predictive analysis, with theory-driven "
                   "hypotheses tested on survey data",
                   "Mechanistic analysis, with exact changes to variables",
                   "Descriptive analysis, since the book reports summaries"],
             "c": 1,
             "why": "The chapter says that whenever the book talks about impacting "
                    "or driving results, the design was this third type. It names "
                    "causal analysis as the gold standard that generally needs "
                    "randomised studies and says that predictive, causal and "
                    "mechanistic analysis were left out because the authors did "
                    "not have the data."},
            {"q": "In the exercise, which result do you get for the six changes in "
                  "two repositories?",
             "a": ["r over all rows is 25/29 ≈ 0.862; within each repository "
                   "r = 1; pooled within r = 1",
                   "r over all rows is −1; within each repository r is 0.862; "
                   "pooled within r is 0.862",
                   "r over all rows is 25/29 ≈ 0.862; within each repository "
                   "r = −1; pooled within r = −1",
                   "r over all rows is 0; within each repository r = −1; "
                   "pooled within r = 0"],
             "c": 2,
             "why": "Over all six rows the means are both 5, Sxx = Syy = 58 and "
                    "Sxy = 50, so r = 50/58 = 25/29 ≈ 0.862. Within north the "
                    "comments rise 1, 2, 3 while the days fall 3, 2, 1, and within "
                    "south 7, 8, 9 against 9, 8, 7, so each r is −1 and, with the "
                    "sums Sxx = Syy = 4 and Sxy = −4 in total, the pooled r is "
                    "−4/√(4·4) = −1. A strong positive figure over everything can "
                    "hide a negative relationship inside every group; a manager "
                    "reading the first number would be tempted to ask for fewer "
                    "comments to speed merges."},
            {"q": "On size-explains the lab reports r = 0.964 over all rows and a "
                  "pooled within-size r of 0.167. Which statement do the two "
                  "figures support?",
             "a": ["Size causes both the comments and the days",
                   "Comments have no effect on days to merge",
                   "The pooled figure is wrong, because the groups have different "
                   "means",
                   "Most of the correlation over all rows comes from the "
                   "differences between the three sizes' averages"],
             "c": 3,
             "why": "Holding size fixed removes the differences between the "
                    "groups' means, and the correlation falls from 0.964 to "
                    "0.167, so most of the first figure came from those "
                    "differences. The numbers do not show that size causes "
                    "anything, nor that comments have no effect; they say nothing "
                    "about cause either way. Different group means are exactly "
                    "what the pooled figure is built to set aside, so they are not "
                    "an error."},
            {"q": "Why, according to the chapter, did the authors leave out "
                  "predictive, causal and mechanistic analysis?",
             "a": ["They did not have the data needed for those analyses",
                   "Those analyses are less rigorous than inferential ones",
                   "Surveys cannot be analysed with them under any circumstances",
                   "They were done in an earlier report and not repeated"],
             "c": 0,
             "why": "The chapter says the final levels were not included because "
                    "the authors did not have the necessary data, and summarises "
                    "them for completeness. It ranks causal analysis as the gold "
                    "standard, so it is not less rigorous; it says nothing about "
                    "an earlier report; and it names A/B testing as a business "
                    "use of causal analysis where randomised data can be had."},
        ],
        "mistakes": [
            ("Reading “drives” as proof of cause",
             "In Chapter 12 the word has a stated meaning: a theory-based "
             "hypothesis tested on survey data under inferential predictive "
             "design. The authors call causal analysis the gold standard and "
             "say they did not carry it out. A reader can still find the "
             "evidence strong, as Fowler does, without reading it as a "
             "randomised experiment."),
            ("Fishing in the data and then writing the theory",
             "The authors' safeguard is the order: theory, then hypothesis, then "
             "data. A correlation noticed first and explained afterwards belongs "
             "to the exploratory rung, where it is easy to invent a story for "
             "any pair that happens to move together."),
            ("Thinking that holding one variable fixed settles the question",
             "The lab's fall from 0.964 to 0.167 shows that size carried most of "
             "that association in those twelve changes. It does not show that "
             "size is the only third variable, or that what remains is causal; "
             "a variable nobody measured cannot be held fixed."),
        ],
        "standard": (
            "Finish when you can say what a driving claim in the book means.",
            "Given a table with a third variable, find r over all rows, inside "
            "each group and pooled, say what the change shows, and state which "
            "rung of Leek's ladder a theory-based survey study climbs."
        ),
        "note": (
            "The lab holds one stated variable fixed in a table of twelve rows. It "
            "cannot choose the right variable, find a variable nobody recorded, or "
            "turn a correlation into a cause; the book's own answer to that is a "
            "theory stated first and many years of data."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Classification Analysis (PDF pp. 180-181 of the operator's copy) with the
    # clustering box (p. 181); The Research in This Book (pp. 181-182);
    # Chapter 2 on cluster analysis (pp. 51-52) and Appendix C, Tests for
    # Classification (pp. 272-273) for Ward's method and the fusion
    # coefficients.
    # Quote: PDF p. 180 of the operator's copy, 13 words, quotes.py OK.
    # Lesson total: 13 words.
    {
        "slug": "classification-analysis",
        "title": "Classification Analysis",
        "module": "Chapter 12 · The Science Behind This Book",
        "one_line": "Sorting teams into groups without telling the method what counts as good, and how to choose how many groups there are.",
        "summary": (
            "Classification is the one analysis the chapter says does not fit the "
            "ladder. Read how the authors fed their four delivery measures to a "
            "clustering algorithm to get high, medium and low performers, why they "
            "chose hierarchical clustering, and what Appendix C says they compared. "
            "Then cluster nine invented teams into two, three and four groups and "
            "read the merge costs that tell you where to stop."),
        "key": [
            "classification: grouping by similarity",
            "four measures in, groups out",
            "the method does not know good from bad",
            "hierarchical: no group count chosen first",
            "Ward's merge cost: the rise in spread",
            "a jump in merge cost marks where to stop",
        ],
        "key_label": "Classification analysis in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the book's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Classification (clustering) analysis",
             "A method that puts the cases into groups so that those in a group "
             "are more alike than those in different groups. The authors fed in "
             "four measures, deployment frequency, lead time for changes, time "
             "to restore service and change fail rate, and looked at which groups "
             "emerged. Depending on design and context, they say, it can count "
             "as exploratory, predictive or even causal analysis."),
            ("Hierarchical clustering",
             "Clustering that starts with every case alone and repeatedly merges "
             "the two closest groups, so that the merges form a tree. The authors "
             "chose it over k-means because they had no prior idea how many "
             "groups to expect, because it shows parent and child groups, and "
             "because their dataset was not huge."),
            ("Fusion coefficient",
             "The cost of one merge. Under Ward's method, the one the authors "
             "kept, it is the increase in the groups' within-group sum of "
             "squared distances that the merge causes. Appendix C says solutions "
             "were compared on the change in fusion coefficients, among other "
             "things."),
        ],
        "read_title": "Groups from the data, and where to stop merging",
        "read_intro": (
            "Read Classification Analysis and The Research in This Book in "
            "Chapter 12 in your own copy first, then the cluster paragraph of "
            "Chapter 2 and Appendix C's Tests for Classification. The lesson "
            "reads them together and then runs the merges on invented teams."
        ),
        "body": [
            ("p", "&ldquo;classification variables are entered into the clustering "
                  "algorithm and significant groups are identified.&rdquo; That is "
                  "how Chapter 12, in its section on Classification Analysis, "
                  "describes the process in one line. The book's most quoted "
                  "result, that there are high, medium and low performers, comes "
                  "from it. Chapter 2 reports the groups, and the lesson High, "
                  "Medium and Low Performers reads them; this lesson reads "
                  "the method."),
            ("p", "Classification is not one of Leek's six, and the authors say "
                  "so: depending on the context, design and methods, it may count "
                  "as exploratory, predictive or even causal analysis. They used "
                  "it for one purpose, to see whether teams differed in how they "
                  "built and delivered software. They put their four technology "
                  "performance variables into the algorithm and looked at the "
                  "groups that emerged. The groups, they report, differ "
                  "distinctly and with statistical significance: the high group is "
                  "better than the others on every one of the four measures, the "
                  "low group worse on every one, and the medium group between "
                  "the two. Chapter 2 gives the numbers and the years."),
            ("p", "What the algorithm does is easy to say. Each measure is a "
                  "dimension, so each team is a point in four-dimensional space, "
                  "and the algorithm looks for groups of points near one another "
                  "and far from the rest. Chapter 2 adds the important point: it "
                  "has no understanding of what a good or bad answer is. The "
                  "names high, medium and low are the researchers' reading of the "
                  "groups afterwards."),
            ("p", "The chapter's box explains why the authors chose hierarchical "
                  "clustering over k-means. K-means needs the number of groups "
                  "chosen first, and they had no theory or prior idea of it; "
                  "hierarchical clustering lets the data say, and also lets them "
                  "look at parent and child relationships in the groups, which "
                  "makes the result easier to interpret; and their dataset was "
                  "not so large that the computing cost mattered. Appendix C, "
                  "Tests for Classification, adds that they ran five methods, "
                  "Ward's among them, and compared the solutions on the change in "
                  "fusion coefficients, on the number of individuals in each "
                  "cluster (solutions with very small clusters were excluded), "
                  "and on univariate F-statistics. Ward's performed best and was "
                  "chosen."),
            ("p", "Ward's method has a definition the book does not print, so the "
                  "lab states it. Start with every team alone. Merge the two "
                  "groups whose joining raises the total within-group sum of "
                  "squared distances the least; that rise is the fusion "
                  "coefficient. Repeat until one group remains. For groups A and "
                  "B, with n teams and average codes a and b on each measure:"),
            ("math", [
                "merge cost(A, B)  =  (nA · nB) / (nA + nB)  ·  Σ over measures of (a − b)²",
                "where a and b are the two groups' average codes on each measure",
            ]),
            ("p", "The cost never decreases, which is why the merges can be "
                  "read as a list: cheap merges join teams that are already alike, "
                  "and a sudden expensive one joins groups that are not. The "
                  "lab uses nine invented teams, each coded 1 to 6 on the four "
                  "measures. In these presets the best answer on each scale (on "
                  "demand, less than one hour, and the lowest fail-rate band, "
                  "0&ndash;15 percent) is coded 6, so a high code is the better answer; the clustering "
                  "never looks at which end is better."),
            ("math", [
                "team  deploy  lead  restore  fail",
                "T1    6       6     6        6",
                "T2    2       1     1        1",
                "T3    5       3     5        3",
                "T4    4       4     4        4",
                "T5    6       6     5        6",
                "T6    5       6     5        5",
                "T7    1       3     2        1",
                "T8    2       1     3        1",
                "T9    3       3     4        4",
            ]),
            ("p", "On the preset <code>three-groups</code>, which asks for three "
                  "groups, the lab lists the eight merges and their costs. They "
                  "are 1/2, 1, 3/2, 2, 3, 10/3, 67/3 and 81. The first six "
                  "merges, which leave three groups, cost 10/3 at most, about "
                  "3.33; the seventh, which would join two of those three, "
                  "costs 67/3, about 22.33. A jump from about 3 to about 22 says "
                  "that going from three groups to two forces together teams that "
                  "are not alike. That is what the authors mean by looking at the "
                  "change in fusion coefficients, one of their three criteria. "
                  "Three tiles keep the score: the last merge made, 10/3 here, "
                  "the next merge to be made, 67/3, and the total within-group "
                  "sum of squares at this k, 34/3 or about 11.33, which is the "
                  "first six costs added up."),
            ("p", "The three groups are T1, T5 and T6; T2, T7 and T8; and T3, T4 "
                  "and T9. By median code on deploy, lead, restore and fail the "
                  "first is 6, 6, 5, 6, which the lab reads as "
                  "on demand, less than one hour, less than one day and 0&ndash;15 "
                  "percent; the second is 2, 1, 2, 1, which reads as between once a "
                  "month and once every six months, more than six months, "
                  "between one month and six months and 76&ndash;100 percent, the "
                  "last a band the lab adds beyond the ranges the book reports; and "
                  "the third is 4, 3, 4, 4, in between. A researcher would now "
                  "call the three groups high, low and medium, and would be doing "
                  "the naming, not the algorithm. The presets "
                  "<code>two-groups</code> and <code>four-groups</code> are the "
                  "same merges cut later or earlier. Two groups put T1, T3, T4, "
                  "T5, T6 and T9 together against T2, T7 and T8, and a group of "
                  "six has medians that are means of two middle codes: the fail "
                  "median, 4.5, prints both neighbours, and the lead median, 5, is "
                  "an answer no team in the group gave; four groups "
                  "split T7 off from T2 and T8, leaving a group of one. The "
                  "authors excluded solutions with few individuals in a cluster, "
                  "and the group of one is why."),
            ("p", "Two reservations belong to the lesson, not the chapter. The "
                  "distance used treats the codes as numbers with equal steps, "
                  "which the six answer options only suggest. And a tree of "
                  "merges always ends in one group; the merge costs help you "
                  "choose where to cut, and no cut is the true one."),
            ("h3", "Exercise"),
            ("ul", [
                "Four invented teams, coded on the four measures as before: `A, "
                "1, 1, 1, 1; B, 2, 1, 1, 1; C, 5, 5, 5, 4; D, 6, 6, 5, 6`.",
                "Work out the three merges by hand with the cost formula, then ask "
                "the lab for two groups.",
            ]),
            ("p", "Say which teams join first, what each merge costs, and what "
                  "the last merge's cost tells you about two groups against one."),
            ("p", "Classification sorts teams by what they report. The next "
                  "lesson, Latent Constructs, opens Chapter 13 and asks how one "
                  "trusts what a survey measures."),
        ],
        "lab": ("acckit", {
            "mode": "delivery",
            "view": "cluster",
            "preset": "three-groups",
            "presets": [
                {"id": "three-groups",
                 "label": "Nine invented teams, grouped into three",
                 "teams": NINE_TEAMS,
                 "better": "6",
                 "k": 3,
                 "expect": {"adeTeams": "9", "adeGroups": "G1: T1, T5, T6; G2: T2, T7, T8; G3: T3, T4, T9", "adeMedDeploy": "G1: 6, on demand (multiple deploys per day); G2: 2, between once per month and once every six months; G3: 4, between once per day and once per week", "adeMedLead": "G1: 6, less than one hour; G2: 1, more than six months; G3: 3, between one week and one month", "adeMedRestore": "G1: 5, less than one day; G2: 2, between one month and six months; G3: 4, between one day and one week", "adeMedFail": "G1: 6, 0–15%; G2: 1, 76–100%; G3: 4, 31–45%", "adeWithin": "34/3 ≈ 11.33", "adeLastCoef": "10/3 ≈ 3.33 ({T2, T8} + {T7})", "adeNextCoef": "67/3 ≈ 22.33 ({T1, T5, T6} + {T3, T4, T9})"}},
                {"id": "two-groups",
                 "label": "The same teams, cut at two groups",
                 "teams": NINE_TEAMS,
                 "better": "6",
                 "k": 2,
                 "expect": {"adeTeams": "9", "adeGroups": "G1: T1, T3, T4, T5, T6, T9; G2: T2, T7, T8", "adeMedDeploy": "G1: 5, between once per hour and once per day; G2: 2, between once per month and once every six months", "adeMedLead": "G1: 5, less than one day; G2: 1, more than six months", "adeMedRestore": "G1: 5, less than one day; G2: 2, between one month and six months", "adeMedFail": "G1: 4.5, 31–45% / 16–30%; G2: 1, 76–100%", "adeWithin": "101/3 ≈ 33.67", "adeLastCoef": "67/3 ≈ 22.33 ({T1, T5, T6} + {T3, T4, T9})", "adeNextCoef": "81 ({T1, T3, T4, T5, T6, T9} + {T2, T7, T8})"}},
                {"id": "four-groups",
                 "label": "The same teams, cut at four groups",
                 "teams": NINE_TEAMS,
                 "better": "6",
                 "k": 4,
                 "expect": {"adeTeams": "9", "adeGroups": "G1: T1, T5, T6; G2: T2, T8; G3: T3, T4, T9; G4: T7", "adeMedDeploy": "G1: 6, on demand (multiple deploys per day); G2: 2, between once per month and once every six months; G3: 4, between once per day and once per week; G4: 1, fewer than once every six months", "adeMedLead": "G1: 6, less than one hour; G2: 1, more than six months; G3: 3, between one week and one month; G4: 3, between one week and one month", "adeMedRestore": "G1: 5, less than one day; G2: 2, between one month and six months; G3: 4, between one day and one week; G4: 2, between one month and six months", "adeMedFail": "G1: 6, 0–15%; G2: 1, 76–100%; G3: 4, 31–45%; G4: 1, 76–100%", "adeWithin": "8", "adeLastCoef": "3 ({T3} + {T4, T9})", "adeNextCoef": "10/3 ≈ 3.33 ({T2, T8} + {T7})"}},
            ],
            "panel_title": "Merging teams by Ward's method",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Clustering by hand with Ward's method",
        "steps_intro": "Five steps, the last of them on teams of your own.",
        "steps": [
            ("Code each team on each measure",
             "Write each team's answer to the four questions as a number from 1 "
             "to 6, using the book's six options in their listed order."),
            ("Find the cheapest merge",
             "For every pair of groups, compute n·n/(n+n) times the sum of "
             "squared differences between their averages. Merge the pair with "
             "the lowest cost and record the cost."),
            ("Repeat with the new average",
             "Replace the two merged groups by one, whose average is the "
             "size-weighted average of the two, and find the cheapest merge "
             "again. Stop when one group is left."),
            ("Look for the jump",
             "Read the costs in order. A cost that is far larger than the one "
             "before it marks the point at which you would be forcing unlike "
             "groups together."),
            ("Do it on teams of your own",
             "Pick six teams you know, answer the four questions for each, code "
             "the answers and type them in. Ask for two, three and four groups "
             "and note which cut the costs favour."),
        ],
        "worked": {
            "title": "Three merges of Ward's method",
            "intro": [
                "Work the first, third and seventh merges of "
                "<code>three-groups</code>.",
            ],
            "lines": [
                "T1 = (6,6,6,6), T5 = (6,6,5,6): squared distance 1",
                "cost = (1·1/2)·1 = 1/2",
                "T6 = (5,6,5,5) against the average of T1, T5 = (6,6,5.5,6)",
                "squared distance 1+0+0.25+1 = 2.25; cost = (1·2/3)·2.25 = 3/2",
                "{T1,T5,T6} average (17/3, 6, 16/3, 17/3); {T3,T4,T9} (4, 10/3, 13/3, 11/3)",
                "squared distance 25/9+64/9+1+4 = 134/9",
                "cost = (3·3/6)·(134/9) = 67/3",
            ],
            "after": [
                "The eight costs add to 344/3, which is also the total of every "
                "team's squared distance from the average of all nine. The "
                "merges spend that total in order, from the cheap pairs to the "
                "expensive last.",
            ],
        },
        "quiz_title": "Groups, merges and the book's choices",
        "quiz": [
            {"q": "Under Ward's method as the lab defines it, merging T2 = (2,1,1,1) "
                  "and T8 = (2,1,3,1), two single-team groups, costs what?",
             "a": ["4", "2", "1", "1/2"],
             "c": 1,
             "why": "The two teams differ only on restore, by 2, so the squared "
                    "distance is 4. The cost multiplies it by n·n/(n+n) = "
                    "1·1/2, which is 2. A cost of 4 is the squared distance "
                    "without the size factor; 1 would apply the factor 1/2 "
                    "twice; and 1/2 is the cost of the first merge, T1 with T5."},
            {"q": "In the exercise, what are the three merge costs, in order, and "
                  "which teams make up the two-group solution?",
             "a": ["1/2, 3 and 273/4; the groups are A, B, C and D alone",
                   "1, 6 and 273/2; the groups are A, B and C, D",
                   "1/2, 3 and 273/4; the groups are A, B and C, D",
                   "1/2, 3 and 68; the groups are A, B, C and D alone"],
             "c": 2,
             "why": "A and B differ by 1 on one measure, so the cost is 1/2. C and "
                    "D differ by 1, 1, 0 and 2, a squared distance of 6, so the "
                    "cost is 6/2 = 3. The averages (1.5,1,1,1) and (5.5,5.5,5,5) "
                    "differ by 4, 4.5, 4 and 4, a squared distance of "
                    "16+20.25+16+16 = 68.25 = 273/4, times 2·2/4 = 1. Two groups "
                    "are what is left before that last merge: A, B and C, D."},
            {"q": "Why did the authors prefer hierarchical clustering to k-means, "
                  "according to Chapter 12?",
             "a": ["K-means cannot be run on survey data at all",
                   "Hierarchical clustering gives p-values for every merge",
                   "They wanted exactly three groups, high, medium and low, and "
                   "hierarchical clustering guarantees three",
                   "They had no prior idea how many groups to expect, wanted to "
                   "see parent and child groups, and their dataset was not huge"],
             "c": 3,
             "why": "The chapter's box gives three reasons: no theoretical idea of "
                    "the number of groups, parent and child relationships for "
                    "interpretation, and a dataset small enough for the cost not "
                    "to matter. Three groups were what the data gave each year, "
                    "not a requirement; the chapter does not say k-means is "
                    "impossible; and a merge cost is not a p-value."},
            {"q": "In Appendix C, which of these did the authors use to compare "
                  "the solutions from five clustering methods?",
             "a": ["The change in fusion coefficients, the number of individuals in "
                   "each cluster, and univariate F-statistics",
                   "Only the number of groups each method produced",
                   "Only whether the groups were named high, medium and low",
                   "The variance explained by the first principal component"],
             "c": 0,
             "why": "Appendix C lists three criteria: the change in fusion "
                    "coefficients, the group sizes (solutions with few individuals "
                    "were excluded) and univariate F-statistics. Ward's method "
                    "performed best on them. Principal components belong to the "
                    "measurement tests, not to the classification."},
        ],
        "mistakes": [
            ("Thinking the algorithm knows which teams are good",
             "Chapter 2 says the technique does not grasp what the responses "
             "mean; it has no idea what counts as good or bad. The "
             "labels high, medium and low come after, from reading the groups. In "
             "the lab, flip every code to the other end of the scale and the "
             "groups are the same."),
            ("Choosing the number of groups before looking",
             "That is what the authors avoided by choosing hierarchical "
             "clustering. The merge costs are the evidence for where to cut, and "
             "a jump is a prompt for judgement, with group sizes and the "
             "subject matter, not a rule."),
            ("Treating the lab's three groups as the book's finding",
             "The groups, the codes and the costs belong to nine invented teams. "
             "The book's finding is that its survey's respondents formed high, "
             "medium and low groups that differed significantly on all four "
             "measures, in each year it checked (Appendix C notes one exception, 2016, which Chapter 2 discusses), as Chapter 2 reports."),
        ],
        "standard": (
            "Finish when you can follow a hierarchical clustering.",
            "Given a small table of teams coded on four measures, find the order "
            "of merges and their costs, and say where the costs suggest stopping."
        ),
        "note": (
            "The lab clusters the codes you type with Ward's cost, exactly. It "
            "cannot tell whether the codes are a fair sample of teams, whether "
            "equal steps between the answer options is a fair assumption, or "
            "whether the groups mean anything beyond the sample."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 13 opening (PDF pp. 183-186 of the operator's copy); Trusting
    # Data with Latent Constructs (pp. 186-189) with Westrum's typology (p.
    # 187; the table's six aspect names only); Latent Constructs Help Us Think
    # Carefully (pp. 189-190); the seven culture items are not reproduced
    # (p. 192) and the footnote on items (p. 196) is paraphrased.
    # Quote: PDF p. 186 of the operator's copy, 13 words, quotes.py OK.
    # Lesson total: 13 words.
    {
        "slug": "latent-constructs",
        "title": "Latent Constructs",
        "module": "Chapter 13 · Introduction to Psychometrics",
        "one_line": "A way to measure what cannot be read off a dial: several survey items, one definition, and an average.",
        "summary": (
            "Chapter 13 answers the doubt every reader of survey research has: "
            "how far can you trust what people say? Read what makes a bad survey, "
            "what a latent construct and a manifest variable are, why the "
            "authors began with Westrum's definition of culture, and how a "
            "construct is scored. Then score a four-item construct for six "
            "invented people, reverse-coding the item worded the other way."),
        "key": [
            "a latent construct: not measured directly",
            "manifest variables: the items that are",
            "define the construct before the items",
            "one question per aspect, then average",
            "reverse-code items worded the other way",
            "a score is a mean of scored items",
        ],
        "key_label": "Latent constructs in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Latent construct",
             "Something that cannot be measured directly, such as the culture of "
             "a team. It is measured through several manifest variables, the "
             "survey items that can be answered, and the answers are combined "
             "into a single number. The authors' items are statements rather "
             "than questions."),
            ("Operationalizing a construct",
             "Deciding exactly what you mean, then writing one item for each "
             "aspect of it. Chapter 13 starts from a clear definition: for "
             "culture, Westrum's typology of pathological, bureaucratic and "
             "generative organisations, which the authors apply to the team "
             "rather than the whole organisation."),
            ("Reverse-coding",
             "An item worded the opposite way round to the others is turned "
             "round before averaging. On a seven-point scale the scored value "
             "is 8 minus the answer, so that a high score always means more of "
             "what the construct names. The lab prints the score with and "
             "without it."),
        ],
        "read_title": "Why a survey can be trusted, and how a construct is built",
        "read_intro": (
            "Read the opening of Chapter 13 through Latent Constructs Help Us "
            "Think Carefully About What We're Measuring in your own copy first. "
            "The lesson follows it, then scores a construct of its own."
        ),
        "body": [
            ("p", "&ldquo;A latent construct is a way of measuring something that "
                  "can&rsquo;t be measured directly.&rdquo; That is the sentence "
                  "Chapter 13, Introduction to Psychometrics, turns on. The chapter "
                  "opens with the two questions the authors are asked most: why "
                  "use surveys, which Chapter 14 answers, and whether data "
                  "collected with them can be trusted at all, which this "
                  "chapter does."),
            ("p", "It starts by agreeing that the scepticism is fair. Much of it "
                  "comes from the surveys most of us meet: push polls, built to "
                  "make the respondent agree with the pollster, of which they "
                  "give a political example; quick surveys; and surveys written "
                  "by people without training. The usual faults are four. Leading "
                  "questions steer the respondent. Loaded questions force an "
                  "answer that may not be true for them. Multiple questions in one "
                  "leave you not knowing which part was answered. Unclear language "
                  "uses words the respondent may not share. A related weakness is "
                  "to rest everything on one question. The authors do not "
                  "dismiss single-question surveys; the Net Promoter Score, they "
                  "say, is a careful and well-documented one and is easy to "
                  "compare, though only narrow conclusions should be drawn from "
                  "it."),
            ("p", "Their own answer to the doubt is the latent construct. The "
                  "room's temperature and a website's response time can be read "
                  "from a dial. Organisational culture cannot; it has no "
                  "temperature. It is measured through its component parts, the "
                  "manifest variables, each of which is an item answered by a "
                  "person. The items together stand for the construct. The "
                  "authors write that this is appropriate because culture is the "
                  "lived experience of the people on the team. It also means "
                  "they must say what they mean."),
            ("p", "That is the first benefit the chapter names. Before writing an "
                  "item, define the construct. A question like &ldquo;is your culture "
                  "good?&rdquo; leaves the team or organisation unclear, leaves "
                  "culture undefined and leaves good undefined, so that no answer "
                  "tells you anything. The culture the authors cared about "
                  "optimised trust and the flow of information, and they took "
                  "Ron Westrum's typology of 2004 as the definition: "
                  "pathological, bureaucratic and generative organisations, "
                  "told apart by six aspects, cooperation, how messengers are "
                  "treated, who is responsible, bridging between teams, how "
                  "failure is handled and how novelty is received. From those "
                  "aspects they wrote several items, seven in the end, and asked "
                  "them about a team, not the organisation, since people answer "
                  "more accurately about their team and large organisations hold "
                  "different cultures in different corners."),
            ("p", "The score then is the average. Respondents rate each item from "
                  "1 for strongly disagree to 7 for strongly agree, and the "
                  "average over the items is, in the authors' phrase, an "
                  "organisational culture temperature of sorts. Chapter 13 "
                  "says that statistical tests can then confirm that the items "
                  "do measure the same underlying idea; the next lesson reads "
                  "those tests, and Measuring and Changing Culture's lesson Measuring Culture scores "
                  "the authors' own culture construct."),
            ("p", "Now score a construct. The lab's sample is invented for the "
                  "lesson: confidence in releasing, measured by four items. Three "
                  "are worded so that agreeing means more confidence, "
                  "<code>routine</code>, <code>unaided</code> and "
                  "<code>clarity</code>. The third, <code>dread</code>, says how "
                  "much releasing worries the person, so agreeing means less, "
                  "and it is marked as reverse-coded. Six invented people, R1 "
                  "to R6, answer on the seven-point scale. On the preset "
                  "<code>four-items</code> the lab scores each person by "
                  "turning round the dread answer, 8 minus the answer, and "
                  "averaging the four. R1's answers 5, 4, 1, 5 become 5, 4, 7, "
                  "5 and a score of 5.25."),
            ("math", [
                "person  routine  unaided  dread  clarity",
                "R1      5        4        1      5",
                "R2      5        6        3      4",
                "R3      3        4        4      6",
                "R4      3        2        6      3",
                "R5      7        6        1      6",
                "R6      2        3        5      5",
            ]),
            ("p", "The six scores are 5.25, 5, 4.25, 2.5, 6.5 and 3.25, and the "
                  "construct mean over the six, 107/24, is 4.458 to three "
                  "places. With a line drawn at the scale's neutral point, 4, "
                  "four people score above it and two below. The item means "
                  "are printed too, as scored: the dread item averages 14/3, "
                  "4.667, after reversing, where its raw answers average 3.333. "
                  "A last tile shows what happens when the reversal is "
                  "forgotten: the construct mean falls to 4.125, and counted by "
                  "hand three people would be above the line instead of four, "
                  "because R1 drops below it."),
            ("p", "The second preset drops one item. On "
                  "<code>without-clarity</code> the lab scores the same six "
                  "people from three items. The construct mean becomes 13/3, "
                  "4.333, and R3, who scored 4.25 on four items, scores 3.667 "
                  "on three, so now three are above the line and three below. "
                  "One item moved one person across it. This is the sense in "
                  "which the chapter says to use several: a single item can "
                  "carry a lot of a person's score, and more than one lets you "
                  "see when it does."),
            ("h3", "Exercise"),
            ("ul", [
                "Three items on the seven-point scale, the second reverse-coded: "
                "`steady, calm, no; anxious, calm, yes; routine, calm, no`.",
                "Four people's answers: `A, 6, 2, 5; B, 3, 3, 3; C, 5, 1, 5; D, 2, "
                "6, 3`.",
                "Score each person, then the construct mean, with and without "
                "reversing the second item. Count the people above a line at 4 "
                "both ways.",
            ]),
            ("p", "Do it by hand and then in the lab. Say what the two construct "
                  "means are, and which person is above the line only when the "
                  "item is reversed."),
            ("p", "A score is only worth reporting if the items behave. The next "
                  "lesson, Several Views, and a Safeguard Against Rogue Data, "
                  "reads the tests that check it."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "score",
            "points": 7,
            "line": 4,
            "preset": "four-items",
            "presets": [
                {"id": "four-items",
                 "label": "Six invented people, four items, one reverse-coded",
                 "items": RELEASE_ITEMS,
                 "answers": RELEASE_ANSWERS,
                 "expect": {"alkN": "6", "alkConstructs": "release-confidence 107/24 ≈ 4.458", "alkItems": "routine 25/6 ≈ 4.167; unaided 25/6 ≈ 4.167; dread 14/3 ≈ 4.667; clarity 29/6 ≈ 4.833", "alkLine": "release-confidence: 4 above, 0 at, 2 below", "alkReversed": "1: dread", "alkUnreversed": "release-confidence 4.125"}},
                {"id": "without-clarity",
                 "label": "The same people scored on three of the items",
                 "items": RELEASE_ITEMS_THREE,
                 "answers": RELEASE_ANSWERS_THREE,
                 "expect": {"alkN": "6", "alkConstructs": "release-confidence 13/3 ≈ 4.333", "alkItems": "routine 25/6 ≈ 4.167; unaided 25/6 ≈ 4.167; dread 14/3 ≈ 4.667", "alkLine": "release-confidence: 3 above, 0 at, 3 below", "alkReversed": "1: dread", "alkUnreversed": "release-confidence 35/9 ≈ 3.889"}},
            ],
            "panel_title": "Scoring a construct from its items",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Scoring a latent construct",
        "steps_intro": "Five steps, the last of them on a short survey of your own.",
        "steps": [
            ("Define the construct in a sentence",
             "Write what you mean and for whom, such as a team's confidence in "
             "releasing. If the sentence leaves out an aspect you care about, add "
             "it before you write items."),
            ("Write one item per aspect",
             "Each item is a statement about one thing. Note any item worded the "
             "opposite way round to the rest."),
            ("Reverse the opposite items",
             "For an item marked reverse, replace each answer by 8 minus the "
             "answer on a seven-point scale."),
            ("Average each person's items",
             "Add a person's scored answers and divide by the number of items, "
             "then average the people for the construct mean."),
            ("Do it on a short survey of your own",
             "Write four statements about one thing in your team's work, one of "
             "them reversed, get six people to rate them from 1 to 7, and type "
             "the answers into the lab. Note the construct mean with and "
             "without the reversal."),
        ],
        "worked": {
            "title": "Scoring R1 and the team",
            "intro": [
                "Score R1 and the construct mean of <code>four-items</code>. The "
                "third item is reverse-coded, the scale has seven points.",
            ],
            "lines": [
                "R1 answers 5, 4, 1, 5",
                "reverse the third: 8 − 1 = 7",
                "R1 scored 5, 4, 7, 5: sum 21, mean 21/4 = 5.25",
                "R2 20/4, R3 17/4, R4 10/4, R5 26/4, R6 13/4",
                "sum of the six quarters: 21+20+17+10+26+13 = 107",
                "construct mean = 107/24 ≈ 4.458",
            ],
            "after": [
                "Without reversing the third item, R1's mean is 15/4 = 3.75, "
                "which is below the line, and the construct mean is 33/8 = "
                "4.125. The scale's arithmetic, not the respondents, moved the "
                "answer.",
            ],
        },
        "quiz_title": "Constructs, items and scores",
        "quiz": [
            {"q": "A person answers 2 on a seven-point scale to an item marked "
                  "reverse-coded. What value goes into their average?",
             "a": ["5", "6", "2", "4"],
             "c": 1,
             "why": "On a seven-point scale the reversed value is 8 minus the "
                    "answer, so 8 − 2 = 6; a 1 becomes 7 and a 7 becomes 1. 5 is "
                    "7 − 2, an off-by-one answer that would map 1 to 6 and 7 to "
                    "0, outside the scale. 2 is the answer left as it was, and 4 "
                    "is the neutral point."},
            {"q": "In the exercise, what are the construct mean with the second "
                  "item reversed and without, and how many people are above 4 each "
                  "way?",
             "a": ["11/3 ≈ 3.667 and 13/3 ≈ 4.333; one person and two",
                   "13/3 ≈ 4.333 and 13/3 ≈ 4.333; two people and two",
                   "13/3 ≈ 4.333 and 11/3 ≈ 3.667; two people and one",
                   "5 and 4; three people and two"],
             "c": 2,
             "why": "Reversed, A scores (6,6,5) = 17/3, B (3,5,3) = 11/3, C "
                    "(5,7,5) = 17/3 and D (2,2,3) = 7/3, which sum to 52/3 and "
                    "average 13/3; A and C are above 4. Unreversed, A is "
                    "(6,2,5) = 13/3, B 3, C (5,1,5) = 11/3 and D (2,6,3) = 11/3, "
                    "which sum to 44/3 and average 11/3; only A is above 4. "
                    "Forgetting the reversal here lowers the mean by two thirds "
                    "of a point and moves C below the line."},
            {"q": "Which survey weakness does &ldquo;Are releases quick and safe?&rdquo; "
                  "show?",
             "a": ["A leading question",
                   "A loaded question",
                   "A rating scale with too few points",
                   "Multiple questions in one"],
             "c": 3,
             "why": "It asks about two things at once, speed and safety, so the "
                    "reader cannot tell which half a yes or a no was about. A "
                    "loaded question presumes something about the respondent that "
                    "may be false, as the chapter's example of asking where someone "
                    "took an exam does; this one presumes nothing. It does not steer "
                    "toward an answer, and it is not trying to persuade."},
            {"q": "On the preset four-items the construct mean is 107/24 ≈ 4.458 and "
                  "on without-clarity it is 13/3 ≈ 4.333. What else changes?",
             "a": ["R3 moves from above the line at 4 to below it, so the split "
                   "goes from four and two to three and three",
                   "R1 moves from above the line to below it",
                   "The construct mean rises, because fewer items are averaged",
                   "Nothing: dropping an item cannot change anyone's side of "
                   "the line"],
             "c": 0,
             "why": "R3's four-item score is 17/4 = 4.25 and drops to 11/3 ≈ 3.667 "
                    "without clarity, because R3's clarity answer of 6 was "
                    "carrying the score over the line. R1 scores 5.25 on four "
                    "items and 16/3 on three, above the line both times. The "
                    "construct mean falls from 4.458 to 4.333, not rises."},
        ],
        "mistakes": [
            ("Asking one broad question and calling it a measure",
             "The chapter's example is asking whether a culture is good, which "
             "leaves unclear whose culture, what culture means and what good "
             "means. A construct is built from a definition and one item for "
             "each aspect, so that each answer means something."),
            ("Averaging items without turning the reversed ones round",
             "A reverse-worded item answered consistently with the others will "
             "pull the average toward the middle. In the lab, forgetting the "
             "reversal changes the construct mean from 4.458 to 4.125 and moves "
             "R1 across the line. A score is only the mean of items that all "
             "point the same way."),
            ("Taking a construct's score for a fact about the team",
             "The score is a mean of perceptions the people reported on a scale. "
             "Chapter 13 itself says all measures are proxies and that the "
             "constructs still have to pass tests, which the next lesson reads. "
             "The lab's mean describes six invented people and nothing else."),
        ],
        "standard": (
            "Finish when you can score a construct.",
            "Given items, a reverse flag and answers on the seven-point scale, "
            "score each person and the construct, and show what forgetting the "
            "reversal does."
        ),
        "note": (
            "The lab averages the items it is given. It cannot tell whether those "
            "items define the construct well, whether they measure one idea or "
            "two, or whether the six people answered honestly; the next lesson "
            "reads the tests the authors use for the first two."
        ),
    },
]
