"""Surveys, Data and Statistical Methods, lesson 6 -- the last two sections of
Appendix C.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Appendix C, Statistical Methods
Used in Our Research (Tests for Relationships (Correlation and Prediction) and
Classification; Tests for Classification). Pages in the comments are PDF pages
of the operator's copy; the lesson cites by chapter and section. The quotation
is copied from that copy and checked with quotes.py. The sample is written for
this lesson: none of the book's tables, figures, survey items or example data
is reproduced. The design is docs/accelerate/PLAN.md, section C, Course 7.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what one "
    "measure says about that sample; the book's findings are its survey's, and a "
    "correlation is not a cause."
)


# ---------------------------------------------------------------- 06 models

# Five invented teams: a practice score (x, 1 to 5) and a delivery score (y).
# name, x, y
FIVE_TEAMS = "t1, 1, 2; t2, 2, 4; t3, 3, 3; t4, 4, 6; t5, 5, 5"
RESHUFFLED = "t1, 1, 6; t2, 2, 4; t3, 3, 3; t4, 4, 2; t5, 5, 5"
A_CURVE = "t1, 1, 5; t2, 2, 2; t3, 3, 1; t4, 4, 2; t5, 5, 5"

# 06 exercise.
EXERCISE_PAIRS = "n1, 2, 3; n2, 4, 1; n3, 6, 4; n4, 8, 2; n5, 10, 5"


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Appendix C, Tests for Relationships (Correlation and Prediction) and
    # Classification, and Tests for Classification (PDF pp. 270-273 of the
    # operator's copy): inferential prediction and the rule on reporting only
    # correlations (p. 270); Pearson's r (pp. 270-271); partial least squares
    # for 2015 through 2017 and its three reasons, linear regression for 2014
    # (p. 271); cluster analysis, five methods, three criteria, Ward's chosen,
    # three reasons for the hierarchical method (pp. 272-273); ANOVA with
    # Tukey's test and Duncan's, p < 0.10, all years except 2016 (p. 273).
    # Quote: PDF p. 271 of the operator's copy, 12 words, quotes.py OK.
    # Lesson total: 12 words.
    {
        "slug": "tests-for-relationships-and-classification",
        "title": "Tests for Relationships and Classification",
        "module": "Appendix C · Statistical Methods Used in Our Research",
        "one_line": "Once the constructs pass, the authors test the relationships they predicted with correlation and regression, and sort teams into groups by cluster analysis; the lab computes the simplest of these, a correlation and its line.",
        "summary": (
            "The last sections of Appendix C list the tests of the second stage: "
            "Pearson's r, two kinds of regression, cluster analysis with Ward's "
            "method and an analysis of variance with Tukey's test. Read what each is "
            "for and why the authors chose it, then compute r, the least-squares "
            "line and r squared for five invented teams by hand and in the lab."
        ),
        "key": [
            "predict from theory, else report correlation",
            "r runs from minus one to one",
            "r measures a straight line only",
            "the line: slope is Sxy over Sxx",
            "r squared is the share the line accounts for",
            "cluster, then compare group means",
        ],
        "key_label": "Relationships and classification in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the appendix's, the other two "
            "the lab's."
        ),
        "concepts": [
            ("Pearson's r",
             "The appendix's measure of how closely two variables follow a straight-line "
             "pattern, from −1 for exact opposite movement through 0 for none "
             "to 1 for exact movement together."),
            ("Least-squares line",
             "The straight line y = a + b·x that makes the squared vertical gaps "
             "between the points and the line as small as they can be. Its slope b "
             "is Sxy over Sxx, and it passes through the point of the two means."),
            ("R squared",
             "The square of r. For one predictor it is the share of the spread of y "
             "that the line accounts for, spread meaning the sum of squared gaps from "
             "the mean of y. It describes the sample and does not say x causes y."),
        ],
        "read_title": "The second stage, then the count",
        "read_intro": (
            "Read the last two sections of Appendix C in your own copy first; they "
            "are three pages. The lesson sets out what each test is for, then "
            "computes a correlation and its line, the part that can be done on five "
            "numbers."),
        "body": [
            ("p", "&ldquo;Pearson correlation measures the strength of a linear relationship "
                  "between two variables&rdquo;, write Forsgren, Humble and Kim in "
                  "Appendix C, Statistical Methods Used in Our Research. The lesson "
                  "reads the appendix's last sections: Tests for Relationships "
                  "(Correlation and Prediction) and Classification, and Tests for "
                  "Classification. They are the second stage, which only constructs "
                  "that passed the measurement tests of the last lesson enter."),
            ("p", "The stage opens with a rule that governs everything after it. As "
                  "Chapter 12 outlines, the research design tests for inferential "
                  "prediction, which means every hypothesis tested is supported by "
                  "theory and literature. Where no theory suggests that one "
                  "construct predicts another, the authors report correlations only. "
                  "So a regression in the book is a test of a predicted relationship, "
                  "and neither a discovery of cause nor a fishing trip; Inferential "
                  "Predictive Analysis explains the distinction."),
            ("p", "Correlation is a mutual relationship or connection between "
                  "constructs, and the authors use Pearson's, the kind most used in "
                  "business. It is a value between −1 and 1: 1 if the variables move "
                  "together exactly, −1 if in exactly opposite directions, 0 if not "
                  "correlated at all. The word to hold on to is linear. Computed from "
                  "the deviations of each variable from its mean, with Sxy the sum of "
                  "the products of the two deviations and Sxx and Syy the sums of "
                  "their squares, it is a short formula."),
            ("math", [
                "r = Sxy / √(Sxx · Syy)",
                "Sxy = sum of (x − mean x) · (y − mean y)",
                "Sxx = sum of (x − mean x)², Syy = sum of (y − mean y)²",
            ]),
            ("p", "A regression adds a line, and the line adds r squared. The "
                  "least-squares slope is Sxy over Sxx, the intercept is the mean of "
                  "y less the slope times the mean of x, and r squared is r times r. "
                  "The authors used two kinds. Linear regression tested the "
                  "predictive relationships of their 2014 research. Partial least "
                  "squares regression, a correlation-based method, tested them for "
                  "2015 through 2017, chosen for three reasons they give: it "
                  "optimizes for predicting the outcome, which served readers in "
                  "industry; it does not require normally distributed data; and it "
                  "suits exploratory research. A regression with several predictors "
                  "is more than the lab's one-predictor line, and the lab "
                  "does not compute it."),
            ("p", "The classification tests need no constructs. Cluster analysis built "
                  "the data-driven groups of high, medium and low performers: each "
                  "measure is a dimension, and the algorithm tries to keep members of a "
                  "cluster close and clusters apart. The authors ran five "
                  "methods, Ward's, between-groups linkage, within-groups linkage, "
                  "centroid and median, and compared their solutions on the change in "
                  "the fusion coefficients, the number of individuals in each cluster, "
                  "with solutions containing small clusters excluded, and univariate "
                  "F-statistics. Ward's method did best and was chosen. They preferred "
                  "a hierarchical method for three reasons: it shows parent and "
                  "child relationships among the clusters, they had no reason from "
                  "industry or theory to fix the number of clusters in advance, and "
                  "their data set was not too big, since hierarchical clustering "
                  "does not suit extremely large ones. The lessons High, Medium and "
                  "Low Performers and Classification Analysis work the merges."),
            ("p", "To interpret the clusters the authors ran an analysis of variance "
                  "and compared the group means of the four delivery measures after "
                  "the fact with Tukey's test, adding Duncan's multiple range test, "
                  "which gave the same results. Differences were counted as "
                  "significant at p below 0.10. In every year but 2016, which "
                  "Chapter 2 discusses, high performers were best on all four "
                  "measures, low performers worst and medium performers in the "
                  "middle, all at significant levels. The appendix gives its reason "
                  "for Tukey's test as not requiring normality; many statistics "
                  "texts list it among the tests that assume roughly normal data, "
                  "and the lesson reports the authors' reason without settling "
                  "it. The lab prints no p-values."),
            ("p", "Now the count, on five invented teams. Each has a practice score "
                  "x from 1 to 5 and a delivery score y. The lab's correlation view "
                  "takes the pairs. On the preset <code>five-teams</code> the x values "
                  "are 1 to 5 and the y values 2, 4, 3, 6 and 5. The means are 3 and "
                  "4, Sxx is 10, Syy is 10 and Sxy is 8, so r is 8 / 10, which is "
                  "0.8. The line is y = 1.6 + 0.8·x, and r squared is 0.64: the "
                  "line accounts for 64 percent of the spread of y in this sample, "
                  "6.4 of its 10. The lab's words tile reads positive, strong; its "
                  "cut-offs, 0.3 and 0.7 by default, are a convention the lab states "
                  "and not the book's."),
            ("p", "The preset <code>reshuffled</code> keeps the same five y values and "
                  "matches them to the x values in another order: 6, 4, 3, 2 and 5. The "
                  "means, Sxx and Syy are unchanged, and Sxy becomes −4, so r is "
                  "−0.4, the tile reads negative, moderate, the line is y = 5.2 − 0.4·x and r squared is 0.16, 16 percent. "
                  "A correlation depends on which values are paired and not only on "
                  "the values."),
            ("p", "The preset <code>a-curve</code> uses y values of 5, 2, 1, 2 and 5 "
                  "against the same x values. Each y is exactly the square of x less "
                  "3, plus 1, so x determines y completely, yet Sxy is 0, r is "
                  "0, the line is flat at y = 3 and r squared is 0. Pearson's r "
                  "sees straight-line association and nothing else. Read r of zero "
                  "as no linear association and not as no relationship."),
            ("p", "Read each figure as the appendix does, as a statement about "
                  "prediction under a theory, in a sample. Five teams make a toy: "
                  "the lab shows how r and r squared are computed and what they "
                  "report, and it cannot say whether practice predicts delivery for "
                  "anyone. Nor does a high r say which way influence runs, or whether a "
                  "third thing drives both."),
            ("h3", "Exercise"),
            ("ul", [
                "Five teams, as `name, x, y`: `n1, 2, 3; n2, 4, 1; n3, 6, 4; n4, 8, 2; "
                "n5, 10, 5`.",
            ]),
            ("p", "By hand, find the two means, Sxx, Syy and Sxy, then r, r squared "
                  "and the least-squares line, and use the line to predict y at x of "
                  "8. Type the pairs into the lab to check. Say how the predicted "
                  "value at 8 compares with the team's own y at 8."),
            ("p", "That ends the survey, the sample and the tests that stand behind the "
                  "findings. The next course, Transformation, reads Part III: Chapter "
                  "16, by Steve Bell and Karen Whitley Bell, and the book's close."),
        ],
        "lab": ("acckit", {
            "mode": "stats",
            "view": "pearson",
            "preset": "five-teams",
            "presets": [
                {"id": "five-teams",
                 "label": "Five teams: practice score against delivery score",
                 "pairs": FIVE_TEAMS,
                 "expect": {"astR": "0.8", "astR2": "16/25 = 64%", "astLine": "y = 1.6 + 0.8·x"}},
                {"id": "reshuffled",
                 "label": "The same five delivery scores paired in another order",
                 "pairs": RESHUFFLED,
                 "expect": {"astR": "−0.4", "astR2": "4/25 = 16%", "astLine": "y = 5.2 − 0.4·x"}},
                {"id": "a-curve",
                 "label": "Delivery score is exactly a curve of the practice score",
                 "pairs": A_CURVE,
                 "expect": {"astR": "0", "astR2": "0 = 0%", "astLine": "y = 3 + 0·x"}},
            ],
            "panel_title": "A correlation and its least-squares line",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Computing a correlation and its line",
        "steps_intro": "Five steps, the last of them on numbers of your own.",
        "steps": [
            ("Find the two means",
             "Add the x values and divide by the number of pairs; do the same for y."),
            ("Find the deviations and their sums",
             "For each pair subtract the means, then total the squares of the x "
             "deviations (Sxx), the squares of the y deviations (Syy) and the "
             "products of the two (Sxy)."),
            ("Compute r and r squared",
             "Divide Sxy by the square root of Sxx times Syy. Square it for the "
             "share of the spread of y that the line accounts for."),
            ("Write the line",
             "The slope is Sxy over Sxx and the intercept is the mean of y less the "
             "slope times the mean of x. Check that it passes through the point of "
             "the two means."),
            ("Try it on your own pairs",
             "Take two scores for five or more teams, such as a count of "
             "automated checks and deploys a week. Compute r and the line, then "
             "swap two y values and recompute. Write down how far r moved."),
        ],
        "worked": {
            "title": "r, the line and r squared for five-teams",
            "intro": [
                "Take x of 1 to 5 and y of 2, 4, 3, 6 and 5 from <code>five-teams</code>.",
            ],
            "lines": [
                "means: x = 15 / 5 = 3, y = 20 / 5 = 4",
                "x deviations: −2 −1 0 1 2; y deviations: −2 0 −1 2 1",
                "Sxx = 4 + 1 + 0 + 1 + 4 = 10",
                "Syy = 4 + 0 + 1 + 4 + 1 = 10",
                "Sxy = 4 + 0 + 0 + 2 + 2 = 8",
                "r = 8 / √(10 · 10) = 8 / 10 = 0.8",
                "slope = 8 / 10 = 0.8; intercept = 4 − 0.8 · 3 = 1.6",
                "r squared = 0.64; line accounts for 0.8 · 8 = 6.4 of 10",
            ],
            "after": [
                "The square root is easy here because Sxx and Syy are both 10; in "
                "general it is not a whole number and the lab prints r to three "
                "decimals. The line passes through (3, 4): 1.6 + 0.8 · 3 = 4.",
            ],
        },
        "quiz_title": "Correlation, the line and the appendix",
        "quiz": [
            {"q": "In the exercise, what is Pearson's r?",
             "a": ["0.25", "1.00", "0.025", "0.50"],
             "c": 3,
             "why": "The means are 6 and 3, Sxx is 40, Syy is 10 and Sxy is 10, so r = "
                    "10 / √400 = 0.5. The 0.25 is r squared, and also the slope, "
                    "Sxy / Sxx. The 1.00 divides Sxy by Syy. The 0.025 forgets the "
                    "square root: 10 / 400."},
            {"q": "In the exercise, what y does the least-squares line predict at "
                  "x of 8?",
             "a": ["2.0, the team's own y at 8",
                   "3.0, the mean of y",
                   "3.5",
                   "4.0"],
             "c": 2,
             "why": "The slope is 10 / 40 = 0.25 and the intercept 3 − 0.25 · 6 = 1.5, so "
                    "the line is y = 1.5 + 0.25·x and at 8 it gives 3.5. The 2.0 is "
                    "the team's observed y, which the line misses by 1.5. The mean "
                    "of y is what the line predicts at the mean of x, 6."},
            {"q": "At what level do the authors say differences between clusters were "
                  "counted as significant when they compared group means with "
                  "Tukey's test?",
             "a": ["p below 0.10",
                   "p below 0.05",
                   "p below 0.01",
                   "p below 0.001"],
             "c": 0,
             "why": "Appendix C gives p below 0.10 for their research. The other three "
                    "are common conventions in other work, and none is the appendix's "
                    "figure."},
            {"q": "On the preset a-curve, r is 0. What does that show?",
             "a": ["x and y are unrelated",
                   "Pearson's r sees straight-line association only, and these "
                   "points follow a curve",
                   "The data must contain an error",
                   "x has no effect on y, a causal statement"],
             "c": 1,
             "why": "Every y is determined by its x, as the curve 1 plus the square "
                    "of x less 3. Pearson's r measures a linear relationship, and "
                    "the points fall as high, low, low, low, high around a flat "
                    "line. Zero rules out a straight-line pattern, not a "
                    "relationship."},
        ],
        "mistakes": [
            ("Reading r as the share explained",
             "A correlation of 0.8 does not mean 80 percent. The share of the spread "
             "of y that the line accounts for is r squared, 0.64 for "
             "<code>five-teams</code>. The same five delivery scores with another "
             "pairing, <code>reshuffled</code>, give r of −0.4 and 16 percent."),
            ("Reading a correlation of zero as no relationship",
             "The appendix defines Pearson's r as a measure of a linear "
             "relationship. In <code>a-curve</code> every y follows from its x and r "
             "is 0. A scatter of the points, or a different measure, shows what r "
             "cannot."),
            ("Treating a predictive test as a finding of cause",
             "The appendix says the regressions test predictive relationships, each "
             "supported by theory and literature, and that correlations are reported "
             "alone where no theory exists. It makes no claim of cause, and Chapter "
             "12 explains why a survey of this kind supports prediction. The lab's "
             "r and r squared are sample statistics of that kind."),
        ],
        "standard": (
            "Finish when you can compute a correlation and its line.",
            "Given five or more pairs, compute the means, Sxx, Syy and Sxy, then r, "
            "r squared and the least-squares line, and say what a straight-line "
            "measure cannot show."
        ),
        "note": (
            "The lab computes one predictor's r and line for the pairs you give it. "
            "It prints no p-values, does not fit the several-predictor regressions or "
            "the clusters the appendix describes, and cannot say whether a "
            "relationship is causal; the appendix's own rule is that prediction "
            "rests on theory."
        ),
    },
]
