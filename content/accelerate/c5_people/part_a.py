"""Sustainable Work, Satisfaction and Leadership, lessons 1-5 -- Chapter 9 and
the first half of Chapter 10.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 9, Making Work Sustainable
(Deployment Pain, Burnout, Common Problems That Can Lead to Burnout, How to
Reduce or Fight Burnout); Chapter 10, Employee Satisfaction, Identity, and
Engagement (Employee Loyalty, Changing Organizational Culture and Identity,
How Does Job Satisfaction Impact Organizational Performance, How Does DevOps
Contribute to Job Satisfaction, Diversity in Tech). Pages in the comments are
PDF pages of the operator's copy; the lessons cite by chapter and section.
Every quotation is copied from that copy and checked with quotes.py. The
teams, answers and counts are invented for these lessons: none of the book's
tables, figures, survey items or example data is reproduced. The design is
docs/accelerate/PLAN.md, section C, Course 5.
"""

_STATS_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)


# ---------------------------------------------------------------- 01 data

# Eight invented teams: the share of deployment steps done by hand (percent)
# and a pain score from 1 (easy, pain-free) to 7 (feared, disruptive).
MANUAL_PAIN = (
    "A, 10, 2; B, 20, 3; C, 30, 2; D, 40, 4; "
    "E, 50, 4; F, 60, 5; G, 70, 6; H, 80, 6"
)
# The same eight, with Team H's pain score 2 instead of 6.
MANUAL_PAIN_H = (
    "A, 10, 2; B, 20, 3; C, 30, 2; D, 40, 4; "
    "E, 50, 4; F, 60, 5; G, 70, 6; H, 80, 2"
)
# 01 exercise: five invented teams.
MANUAL_PAIN_FIVE = "P, 10, 2; Q, 30, 3; R, 50, 4; S, 70, 4; T, 90, 7"


# ---------------------------------------------------------------- 02 data

# Six invented respondents, 7-point scale, four invented burnout items:
# b1 exhaustion, b2 cynicism, b3 energy left for life outside work (reverse),
# b4 a sense of getting worthwhile things done (reverse).
BURNOUT_ITEMS = "b1, burnout, no; b2, burnout, no; b3, burnout, yes; b4, burnout, yes"
BURNOUT_NOT_FLAGGED = (
    "b1, burnout, no; b2, burnout, no; b3, burnout, no; b4, burnout, no"
)
BURNOUT_ANSWERS = (
    "r1, 6, 5, 2, 2; r2, 2, 2, 6, 6; r3, 4, 3, 4, 3; "
    "r4, 5, 6, 3, 2; r5, 3, 2, 5, 5; r6, 7, 6, 1, 2"
)
# 02 exercise: three respondents, 5-point scale, three items, the third reversed.
BURNOUT_FIVE_ITEMS = "x1, burnout, no; x2, burnout, no; x3, burnout, yes"
BURNOUT_FIVE_ANSWERS = "A, 4, 5, 2; B, 2, 1, 5; C, 3, 4, 3"


# ---------------------------------------------------------------- 03 data

# Ten invented answers to "how likely are you to recommend ... 0 to 10".
ENPS_TEAM = "10, 9, 9, 9, 8, 8, 7, 6, 5, 3"
ENPS_UP = "10, 9, 9, 9, 9, 8, 7, 6, 5, 3"      # one 8 became a 9
ENPS_INSIDE = "10, 9, 9, 9, 7, 8, 7, 6, 5, 3"  # one 8 became a 7
# 03 exercise.
ENPS_EXERCISE = "10, 9, 8, 8, 7, 7, 7, 6, 5, 4"


# ---------------------------------------------------------------- 04 data

# Two invented teams of four, 7-point scale. Items i1-i3 ask about identifying
# with the organization, s1-s3 about satisfaction with the work, its tools
# and resources, and the use it makes of one's skills.
TWO_CONSTRUCTS = (
    "i1, identity, no; i2, identity, no; i3, identity, no; "
    "s1, satisfaction, no; s2, satisfaction, no; s3, satisfaction, no"
)
ALDER_ANSWERS = (
    "a1, 6, 6, 5, 5, 6, 6; a2, 5, 4, 5, 4, 5, 4; "
    "a3, 7, 6, 6, 6, 6, 7; a4, 4, 5, 4, 3, 4, 4"
)
BIRCH_ANSWERS = (
    "b1, 3, 4, 3, 5, 5, 6; b2, 2, 3, 3, 4, 5, 4; "
    "b3, 4, 4, 5, 6, 6, 5; b4, 3, 2, 3, 5, 4, 5"
)
# 04 exercise: a third invented team, two items for each construct.
CEDAR_ITEMS = (
    "i1, identity, no; i2, identity, no; s1, satisfaction, no; "
    "s2, satisfaction, no"
)
CEDAR_ANSWERS = "c1, 6, 6, 3, 4; c2, 5, 7, 2, 3; c3, 4, 4, 5, 6"


# ---------------------------------------------------------------- 05 data

# An invented region of 1,000 engineers, 800 in group A and 200 in group B.
# "met" is "answered the survey". The first wave's invitations reach group B
# less well; the second adds invitations through a list B's members use.
SURVEY_FIRST = "Group-A, 800, 240; Group-B, 200, 30"
SURVEY_SECOND = "Group-A, 800, 240; Group-B, 200, 60"
# 05 exercise.
SURVEY_EXERCISE = "Group-P, 600, 180; Group-Q, 400, 80"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 9, Deployment Pain (PDF pp. 125-130 of the operator's copy):
    # the definition and why it matters (pp. 125-126), the Bing box (p. 126),
    # not knowing what deployments are like and how it was measured
    # (p. 127), the practices that reduce it and the correlation with
    # outcomes (pp. 127-128), the three causes (pp. 128-129), what to build
    # (pp. 129-130). The years 2015, 2016 and 2017 are on p. 127.
    # Quote: PDF p. 126 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "deployment-pain",
        "title": "Deployment Pain",
        "module": "Chapter 9 · Making Work Sustainable",
        "one_line": "The fear and anxiety of pushing code to production, asked about in three surveys, and what moves with it.",
        "summary": (
            "The authors wanted software delivery that is not bought with the mental "
            "health of the team, and Chapter 9 starts with a feeling every engineer "
            "knows: dread at deploy time. Read how they turned it into a measure, "
            "what they found it moves with, and the three causes they give; then "
            "compute a correlation between a deployment-pain score and the share of "
            "manual steps, on eight invented teams."
        ),
        "key": [
            "deployment pain is fear at deploy time",
            "asked in 2015, 2016 and 2017",
            "painful goes with poorer performance",
            "causes: design, manual steps, handoffs",
            "r says how closely two measures move",
            "one team can move r on a small sample",
        ],
        "key_label": "Deployment pain in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the other two "
            "the lab's."
        ),
        "concepts": [
            ("Deployment pain",
             "The dread that engineers and other technical staff feel when they release code to production. The authors measured it by asking respondents whether deployments were feared or disruptive in their work, or easy and free of pain."),
            ("Correlation coefficient (r)",
             "A number from minus 1 to 1 that says how closely two measures rise and "
             "fall together across the same set of teams. Plus 1 is a perfect "
             "upward line, 0 is no straight-line relation and minus 1 a perfect "
             "downward line."),
            ("r squared",
             "The correlation multiplied by itself, read as the share of the "
             "variation in one measure that a straight line on the other accounts "
             "for in this sample. It is a description of the sample, not of a "
             "cause."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read the opening of Chapter 9 and its section Deployment Pain in your "
            "own copy first. The lesson sets out what the authors found and how they "
            "measured it, then computes the kind of figure they used on a sample of "
            "its own."
        ),
        "body": [
            ("p", "&ldquo;We found that where code deployments are most painful, "
                  "you&rsquo;ll find the poorest software delivery performance, "
                  "organizational performance, and culture.&rdquo; That is the "
                  "claim at the centre of the Deployment Pain section of Chapter 9, "
                  "Making Work Sustainable, which is the first of two halves of the "
                  "chapter; the second, on burnout, is the next lesson. The chapter "
                  "opens with the reason for the pair. Forsgren, Humble and Kim want "
                  "to know whether delivery performance is being reached by brute "
                  "force, at the cost of the people doing it, so their project "
                  "asked about how painful deployment is and how burned out the "
                  "team feels."),
            ("p", "Why start with deployment? The authors say it is where "
                  "development meets IT operations, and so where two groups differ "
                  "most, in environment, in process, in mindset and even in the "
                  "words they use for their work. Years of watching teams had made "
                  "the pain of a release stand out. They add a second warning "
                  "sign that is easy to miss. If you ask a developer or tester what "
                  "deployments are like and the answer is that they have never "
                  "thought about it, the authors suspect that something is keeping the work of deployment out of their sight, and they count that, too, as a sign that delivery performance may be low."),
            ("p", "How do you measure a feeling? The authors built a measure from "
                  "their own experience and from talking to people who run "
                  "systems, and they asked about it in the surveys of 2015, 2016 "
                  "and 2017. Respondents were asked whether deployments were "
                  "feared, whether they were disruptive to their work, or whether "
                  "they were easy and pain-free. As with every measure in the "
                  "book, this is a person's report of how things feel, gathered "
                  "by survey; Chapter 14 is where the authors argue that such "
                  "reports can be trusted, and the later courses of this path read "
                  "it."),
            ("p", "What they report is two findings. The first is about practices. "
                  "The teams whose deployment pain fell were those that had put in place comprehensive test and deployment automation, continuous integration (trunk-based development included), shift left on security, effective test data management, loosely coupled architectures, the ability to work independently, and version control of everything needed to reproduce production environments. Those "
                  "are the technical practices of Chapters 4 and 5; the authors "
                  "point out that the same practices that improve speed and "
                  "stability also reduce the stress of pushing code. The second finding is a correlation: where deployments hurt more, IT performance, organizational performance and culture are all lower. The text calls it a high correlation, and the lesson keeps to that word."),
            ("p", "The chapter adds one story from industry. A box quotes Thiago Almeida, a Microsoft engineering lead, on the benefits continuous delivery brought inside his company, and reports that engineers on the Bing team scored their work/life balance satisfaction at 38 percent before the practices and 75 percent after. It is one team's account, not a figure from the authors' survey, and the lesson uses it only as an "
                  "illustration of what a lower-pain deployment means to the people "
                  "who do it."),
            ("p", "The authors name three reasons a deployment becomes complex and "
                  "brittle. The software was not written with deployability in "
                  "mind, so it needs its environment set up in one precise way and "
                  "says little when it fails. Manual changes are made to production "
                  "as part of the deployment, which raises the chance of failure "
                  "through typing slips, copy and paste, out-of-date documents and "
                  "environments that drift apart. And deployments need many "
                  "handoffs between teams in siloed organizations. Their remedies "
                  "follow: build systems that deploy easily to several "
                  "environments and tolerate failure; reproduce production state "
                  "from version control; put intelligence in the application and "
                  "platform so that the deployment itself is simple. A deployment "
                  "that must happen outside business hours, they say, is a sign of "
                  "architectural problems."),
            ("p", "Now the count. A correlation coefficient is the figure the "
                  "authors report when they say two measures move together, and the "
                  "lab computes it on eight invented teams. For each team the lab is "
                  "given the share of deployment steps done by hand and a pain score "
                  "from 1 to 7. The preset <code>manual-steps</code> has the shares "
                  "10, 20, up to 80 percent; the pain scores are 2, 3, 2, 4, 4, 5, 6, "
                  "6. The means are 45 percent and 4. The lab reports r of 0.946, "
                  "so r squared is 0.894 or 89.4 percent, and a fitted straight line "
                  "that adds about 0.062 to the pain score for each extra point of "
                  "manual share, starting from 1.214 at none. The mean pain score "
                  "and the mean manual share sit on that line."),
            ("p", "Then change one thing. The preset <code>one-team-differs</code> "
                  "is the same eight, except that the last team, which does 80 "
                  "percent of its steps by hand, scores its pain at 2 instead of 6. "
                  "The lab now reports r of 0.463 and r squared of 21.4 percent. "
                  "One team out of eight moved the figure by about half. That is "
                  "not a flaw in the formula; it is what a small sample does, and "
                  "it is why the authors collect thousands of responses before "
                  "they say a practice goes with an outcome."),
            ("h3", "Exercise"),
            ("ul", [
                "Five invented teams, written as team, manual share (percent), pain "
                "score: `P, 10, 2`; `Q, 30, 3`; `R, 50, 4`; `S, 70, 4`; `T, 90, 7`.",
            ]),
            ("p", "Find the two means, then the sum of the products of each "
                  "team's two distances from the means, and the two sums of squared "
                  "distances. The correlation is the first sum divided by the "
                  "square root of the product of the other two. Write r squared "
                  "as a fraction before you take any root, then type the five "
                  "records into the lab to check."),
            ("p", "A figure of this kind answers how closely two measures "
                  "move on the teams you give it; it does not say that manual steps "
                  "produce dread, or that dread leads teams to keep their steps "
                  "manual. The authors argue the direction from their practices and "
                  "their theory over several years of surveys, not from one "
                  "coefficient. The next lesson, Burnout, takes the chapter's second "
                  "half: how they define it, what puts it at risk and how it is "
                  "scored."),
        ],
        "lab": ("acckit", {
            "mode": "stats",
            "view": "pearson",
            "preset": "manual-steps",
            "presets": [
                {"id": "manual-steps",
                 "label": "Eight invented teams: share of manual deployment steps against pain",
                 "pairs": MANUAL_PAIN,
                 "expect": {
                    "astN": "8",
                    "astMeans": "x̄ = 45, ȳ = 4",
                    "astR": "≈ 0.946",
                    "astR2": "169/189 ≈ 89.4%",
                    "astLine": "y = 17/14 ≈ 1.214 + 13/210 ≈ 0.062·x",
                    "astWords": "positive, strong",
                 }},
                {"id": "one-team-differs",
                 "label": "The same eight, with the last team's pain score at 2",
                 "pairs": MANUAL_PAIN_H,
                 "expect": {
                    "astN": "8",
                    "astMeans": "x̄ = 45, ȳ = 3.5",
                    "astR": "≈ 0.463",
                    "astR2": "3/14 ≈ 21.4%",
                    "astLine": "y = 31/14 ≈ 2.214 + 1/35 ≈ 0.029·x",
                    "astWords": "positive, moderate",
                 }},
            ],
            "panel_title": "How closely two measures move together",
            "panel_intro": _STATS_INTRO,
        }),
        "steps_title": "Computing and reading a correlation",
        "steps_intro": "Four steps, the last of them on teams of your own.",
        "steps": [
            ("Write down two measures for each team",
             "One row for each team: its name, the share of deployment steps done "
             "by hand and a pain score. Use the same teams in both columns."),
            ("Find each mean and each distance",
             "Average each column, then subtract the mean from every value in that "
             "column. The sign of a distance says which side of the mean the team "
             "lies."),
            ("Combine the distances",
             "Add up the products of each team's two distances, and the squares of "
             "each column's distances. Divide the first by the square root of the "
             "product of the other two to get r; square r for r squared."),
            ("Do it on your own teams",
             "Take six or more teams you know and score how many of their "
             "deployment steps are manual and how painful the last release felt, "
             "from 1 to 7. Type them into the lab, note r, then remove the team "
             "that differs most and note how far r moves."),
        ],
        "worked": {
            "title": "r for eight invented teams",
            "intro": [
                "Work the preset <code>manual-steps</code> by hand. The mean share is "
                "45 and the mean pain score 4.",
            ],
            "lines": [
                "Distances in share: -35, -25, -15, -5, 5, 15, 25, 35",
                "Distances in pain: -2, -1, -2, 0, 0, 1, 2, 2",
                "Sum of products: 70 + 25 + 30 + 0 + 0 + 15 + 50 + 70 = 260",
                "Sum of squares, share: 2 times (1225 + 625 + 225 + 25) = 4200",
                "Sum of squares, pain: 4 + 1 + 4 + 0 + 0 + 1 + 4 + 4 = 18",
                "r squared = 260 times 260 over (4200 times 18) = 67600/75600 = 0.894",
                "r = 260 over the square root of 75600 = 260/274.95 = 0.946",
            ],
            "after": [
                "Each line uses only the eight rows. The lab prints the same r to "
                "three decimals, and the same r squared as an exact fraction and a "
                "percentage.",
            ],
        },
        "quiz_title": "A correlation, and what the chapter reports",
        "quiz": [
            {"q": "For the five teams of the exercise, the sum of products of "
                  "distances is 220, the sum of squared distances in the share is "
                  "4000 and in the pain score 14. What is r squared?",
             "a": ["About 0.930",
                   "About 0.055",
                   "About 0.136",
                   "About 0.864, or 121/140"],
             "c": 3,
             "why": "r squared is 220 times 220 over (4000 times 14), which is 48400/56000, "
                    "or 121/140, about 0.864. About 0.930 is r itself, the square "
                    "root of that fraction. About 0.055 is 220 over 4000, the slope "
                    "of the fitted line, not a correlation. About 0.136 is 1 minus "
                    "r squared, the part the line does not account for."},
            {"q": "In which survey years does Chapter 9 say the authors asked "
                  "respondents about deployment pain?",
             "a": ["2015, 2016 and 2017",
                   "2014, 2015, 2016 and 2017",
                   "2017 only",
                   "2016 only, when the Lean questions were added"],
             "c": 0,
             "why": "The chapter says deployment pain was included in the research "
                    "in 2015, 2016 and 2017. The 2014 survey, the first, is not "
                    "among them, and the question was not confined to one year."},
            {"q": "The lab reports r of 0.946 on <code>manual-steps</code> and "
                  "0.463 on <code>one-team-differs</code>. What does the "
                  "difference show?",
             "a": ["Manual steps do not affect pain, because r fell",
                   "With eight teams, changing one team's score can move r a long way",
                   "The first preset proves manual steps cause the pain",
                   "r depends on the order in which the teams are listed"],
             "c": 1,
             "why": "Only the last team's score changed, and r fell from 0.946 to "
                    "0.463, so a small sample is sensitive to a single team. A fall "
                    "in r does not show there is no effect, and a high r does not "
                    "show a cause; the order of the rows does not enter the "
                    "formula."},
            {"q": "A team answers, \"I don&rsquo;t know; I have never thought about "
                  "deployments.\" How does the chapter read that answer?",
             "a": ["As the best result: deployment is so smooth nobody notices it",
                   "As a sign the respondent should be left out of the survey",
                   "As a warning that barriers may be hiding the work from them",
                   "As a measure of low burnout"],
             "c": 2,
             "why": "The authors say that when developers or testers cannot say what deployments are like, something is probably keeping the work out of their sight, which is a warning that delivery performance could be low."},
        ],
        "mistakes": [
            ("Thinking deployment pain is only a feeling, so it says nothing about delivery",
             "The chapter reports that where deployments hurt more, IT performance, organizational performance and culture are lower, and that "
             "improving the technical practices reduces the pain. A feeling "
             "measured in a survey is still a measure, and this one moves with "
             "outcomes that are measured in other ways."),
            ("Reading a high r as proof that manual steps cause the pain",
             "r says how closely two columns move on the teams given. The chapter "
             "gives its reason for the direction, that brittle manual deployments "
             "hurt, from theory and from several years of surveys; the lab shows "
             "only the first step, that the columns move together."),
            ("Treating a painless deployment as one nobody thinks about",
             "The authors treat not knowing what deployments are like as a warning "
             "of its own, because it suggests barriers between developers and "
             "testers and the deployment itself."),
        ],
        "standard": (
            "Finish when you can compute r for a small sample and say what it leaves out.",
            "Given pairs of measures for a few teams, compute r and r squared by "
            "hand, say what changed when one team did, and name the direction of "
            "cause that r cannot supply."
        ),
        "note": (
            "The lab computes a correlation on the invented teams you give it. It "
            "cannot say whether the pain scores are honest, whether a third thing "
            "drives both columns, or which way any cause runs; the authors argue "
            "those from their model, and The Science Behind the Book reads how."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 9, Burnout to How to Reduce or Fight Burnout (PDF pp. 130-137):
    # what burnout is and costs (pp. 130-131), what managers should attend to
    # (pp. 131-132), Maslach's six risk factors (p. 132), how it was measured
    # and the finding on practices (p. 133), the five most highly correlated
    # factors (pp. 133-135), values alignment (pp. 135-136), summary (p. 136),
    # footnote 3 on other models of burnout (p. 137).
    # Quote: PDF p. 131 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "burnout",
        "title": "Burnout",
        "module": "Chapter 9 · Making Work Sustainable",
        "one_line": "Exhaustion and cynicism that managers try to fix in the person, when the chapter says to fix the work.",
        "summary": (
            "The authors describe burnout, give the six organizational risk factors "
            "of the psychologist Christina Maslach, say how they measured it and list "
            "what correlated most with it. Read their argument that the environment, "
            "not the person, is where to act; then score a team on four invented "
            "burnout items, one of them reverse-coded, and see what forgetting the "
            "reversal does."
        ),
        "key": [
            "burnout is more than overwork",
            "six risk factors management can change",
            "fix the work, not only the person",
            "lived values count, not the printed ones",
            "reverse items before you average",
            "a missed reversal changes the whole result",
        ],
        "key_label": "Burnout in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Burnout",
             "Exhaustion that overwork or stress brings on, and more than being busy: it shows as exhaustion, cynicism and a feeling of being ineffective."),
            ("Organizational risk factor",
             "A condition of the workplace, not of the person, that predicts burnout. "
             "The chapter takes Maslach's six: work overload, lack of control, "
             "insufficient rewards, breakdown of community, absence of fairness "
             "and value conflicts."),
            ("Reverse-coded item",
             "A survey item worded so that agreeing means less of what is being "
             "measured. Before items are averaged its answer is turned round, on a "
             "7-point scale to 8 minus the answer, so that a high score means "
             "the same thing on every item."),
        ],
        "read_title": "The chapter's argument, then the score",
        "read_intro": (
            "Read the sections from Burnout to How to Reduce or Fight Burnout in your "
            "own copy first. The lesson reads them as an argument about where to "
            "look for the cause of burnout, then scores a team's answers."
        ),
        "body": [
            ("p", "&ldquo;Technology managers, like so many other well-meaning "
                  "managers, often try to fix the person while ignoring the work "
                  "environment&rdquo;: that sentence from the Burnout section of "
                  "Chapter 9 carries its whole argument. The section is also "
                  "careful to say what burnout is. The authors insist it is more than being overworked: it can make what you once loved about work seem dull, it often shows as helplessness, and it goes with pathological cultures and wasteful "
                  "work. Its symptoms are feeling exhausted, cynical or ineffective, "
                  "little sense of accomplishment, and work that spills into the "
                  "rest of life."),
            ("p", "The chapter gives reasons to take it seriously. It cites "
                  "research comparing the health cost of stressful jobs to that of "
                  "secondhand smoke and of obesity, and a cost of 300 billion "
                  "dollars a year to the US economy in sick time, long-term "
                  "disability and turnover, attributed to Maslach in 2014. Those "
                  "are other researchers' figures, which the book reports, not "
                  "results from its own survey. From them the authors draw an "
                  "obligation: employers have a duty of care and a fiduciary obligation to prevent it."),
            ("p", "Where should a manager look? The authors rely on Christina "
                  "Maslach, a psychology professor at the University of California "
                  "at Berkeley who pioneered the study of job burnout, and on "
                  "Leiter and Maslach (2008): six organizational risk factors "
                  "that predict burnout. They are work overload, lack of control "
                  "over decisions that affect your job, insufficient rewards "
                  "(financial, institutional or social), breakdown of community, "
                  "absence of fairness, and a mismatch between your values and the "
                  "organization&rsquo;s. All six, the chapter notes, are things "
                  "that management has the power to change, yet most organizations work on the individual and leave the setting alone, though "
                  "Maslach&rsquo;s research shows that changing the setting is "
                  "likelier to work. The chapter adds, in a note, that other models "
                  "of burnout exist, such as that of Marie Asberg, and that the "
                  "authors chose Maslach&rsquo;s."),
            ("p", "To measure it the authors asked respondents three things: "
                  "whether they felt burned out or exhausted; whether they felt detached, cynical or useless in their work; and whether the job was doing their life outside it harm. They report that respondents who worked with better technical practices (those behind continuous delivery) and Lean practices (Lean management and Lean product management) felt less burned out."),
            ("p", "Which factors went with burnout most strongly? The chapter "
                  "lists five. Organizational culture comes first: strong feelings "
                  "of burnout were found in pathological, power-oriented cultures. "
                  "Then deployment pain, the last lesson&rsquo;s subject; "
                  "the effectiveness of leaders; organizational investment in "
                  "DevOps, in the skills of teams and in the time to acquire them; "
                  "and organizational performance. In most cases the authors "
                  "turn the correlation into advice for managers: build a "
                  "blame-free environment, ask teams how painful deployments are "
                  "and fix what hurts most, limit work in process and remove "
                  "roadblocks, give people time and resources to learn, and make "
                  "room for experiment in the working week rather than expecting "
                  "it after hours."),
            ("p", "The last argument is about values. When a person&rsquo;s values "
                  "and the organization&rsquo;s do not match, the authors say, "
                  "burnout is likelier; when they match, its effects can be "
                  "lessened. They are careful about which values: the ones "
                  "employees feel in everyday life at work count, not the "
                  "mission statement on the wall. This is the sixth of "
                  "Maslach&rsquo;s factors, and Chapter 10 will carry it into the "
                  "measure called identity."),
            ("p", "Now the score. A survey that asks about burnout asks several "
                  "questions, and some are worded the other way round: agreeing "
                  "with \"I have energy left for my life outside work\" means less "
                  "burnout. The lab scores the preset <code>team</code>, six "
                  "invented respondents on four invented items on a 7-point scale; "
                  "<code>b1</code> and <code>b2</code> ask about exhaustion and "
                  "cynicism, and <code>b3</code> and <code>b4</code> about energy "
                  "left and a sense of getting worthwhile things done, so those "
                  "two are reverse-coded. The first respondent answers 6, 5, 2, 2. "
                  "The reversed answers are 6 and 6, so the four scores are 6, 5, "
                  "6, 6, a mean of 5.75. The team&rsquo;s mean is 4.417. The "
                  "lesson sets its own line at 5; three of the six respondents are "
                  "above it. The book gives no such line, and a line is only a "
                  "place to start asking questions."),
            ("p", "Now see what a missed reversal costs. The preset "
                  "<code>not-reversed</code> has the same answers but no item "
                  "flagged. The first respondent&rsquo;s mean falls from 5.75 to "
                  "3.75, the team mean from 4.417 to 3.833, and no one is above the "
                  "line any more. The most worn-out respondent in the team, who "
                  "answered 7, 6, 1, 2, now looks like a 4.0, no different from a "
                  "contented colleague who answered 2, 2, 6, 6. A survey scored "
                  "with the wrong sign would send a manager the wrong message."),
            ("h3", "Exercise"),
            ("ul", [
                "A 5-point scale. Items `x1` and `x2` are not reversed; `x3` is.",
                "Answers, written as respondent, `x1`, `x2`, `x3`: `A, 4, 5, 2`; "
                "`B, 2, 1, 5`; `C, 3, 4, 3`.",
            ]),
            ("p", "Reverse the third answer for each person (on a 5-point scale a "
                  "reversed answer is 6 minus the answer), find each "
                  "person&rsquo;s mean and then the team mean. Then recompute it "
                  "with nothing reversed, and say which way the missing "
                  "reversal moved the team. Type the records in to check."),
            ("p", "A score of this kind is a place to ask what is going on, not "
                  "a verdict on anyone. The authors write that managers should ask "
                  "employees what is preventing them from reaching their objectives "
                  "and fix those things; a number cannot do that for them. The next "
                  "lesson, Employee Loyalty and the Net Promoter Score, turns to "
                  "Chapter 10 and a different measure of how people feel about the "
                  "place they work."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "score",
            "preset": "team",
            "presets": [
                {"id": "team",
                 "label": "Six respondents, four burnout items, two reverse-coded",
                 "points": 7,
                 "items": BURNOUT_ITEMS,
                 "answers": BURNOUT_ANSWERS,
                 "line": 5,
                 "expect": {
                    "alkN": "6",
                    "alkConstructs": "burnout 53/12 ≈ 4.417",
                    "alkLine": "burnout: 3 above, 0 at, 3 below",
                    "alkReversed": "2: b3, b4",
                    "alkUnreversed": "burnout 23/6 ≈ 3.833",
                 }},
                {"id": "not-reversed",
                 "label": "The same answers, with no item flagged as reversed",
                 "points": 7,
                 "items": BURNOUT_NOT_FLAGGED,
                 "answers": BURNOUT_ANSWERS,
                 "line": 5,
                 "expect": {
                    "alkN": "6",
                    "alkConstructs": "burnout 23/6 ≈ 3.833",
                    "alkLine": "burnout: 0 above, 0 at, 6 below",
                    "alkReversed": "0: none",
                    "alkUnreversed": "burnout 23/6 ≈ 3.833",
                 }},
            ],
            "panel_title": "Scoring a construct from survey items",
            "panel_intro": (
                "A figure computed from the small sample the lesson states. It "
                "shows what one measure says about that sample; the book's "
                "findings are its survey's, and a score is not a diagnosis."
            ),
        }),
        "steps_title": "Scoring burnout items",
        "steps_intro": "Four steps, the last of them on a survey of your own.",
        "steps": [
            ("Mark the reversed items",
             "Read each item and ask whether agreeing means more or less of what "
             "you measure. Mark every item where it means less."),
            ("Turn those answers round",
             "For each marked item replace the answer with the scale&rsquo;s "
             "number of points plus 1, minus the answer. On a 7-point scale a 2 "
             "becomes a 6."),
            ("Average each person, then the team",
             "A respondent&rsquo;s score is the mean of their items after "
             "reversing. The team&rsquo;s is the mean over respondents. Count the "
             "respondents above the line you chose and say why you chose it."),
            ("Check it on your own survey",
             "Take a short survey of your own with at least one reversed item, "
             "type it into the lab with and without the reversal, and note how "
             "many respondents change sides of your line."),
        ],
        "worked": {
            "title": "Two respondents of the burnout team",
            "intro": [
                "Score the first and third respondents of <code>team</code>. Items "
                "<code>b3</code> and <code>b4</code> are reversed; on 7 points a "
                "reversed answer is 8 minus the answer.",
            ],
            "lines": [
                "r1 answers 6, 5, 2, 2",
                "r1 reversed 6, 5, 8-2 = 6, 8-2 = 6; sum 23; mean 23/4 = 5.75",
                "r3 answers 4, 3, 4, 3",
                "r3 reversed 4, 3, 8-4 = 4, 8-3 = 5; sum 16; mean 16/4 = 4.00",
                "Without reversing: r1 = 15/4 = 3.75, r3 = 14/4 = 3.50",
            ],
            "after": [
                "The same four numbers for each of the six respondents give the "
                "team mean, 26.5 over 6, or 4.417. Only the reversal differs from "
                "<code>not-reversed</code>, and it moves each of the means shown.",
            ],
        },
        "quiz_title": "Reverse coding, and what the chapter says",
        "quiz": [
            {"q": "For the exercise, with the third item reversed on a 5-point "
                  "scale, what is the team mean?",
             "a": ["3.22, the mean with nothing reversed",
                   "2.78, the mean with all three items reversed",
                   "2.67, from reversing with 5 minus the answer",
                   "3"],
             "c": 3,
             "why": "The reversed third answers are 4, 1 and 3, so the totals are "
                    "13, 4 and 10 and the team total is 27 over nine answers, "
                    "which is 3. With nothing reversed the total is 29 and the "
                    "mean 3.22. Reversing all three would give 25 over 9, or 2.78. "
                    "Reversing with 5 minus the answer, which forgets that the "
                    "scale starts at 1, gives 24 over 9, or 2.67."},
            {"q": "According to Chapter 9, what do Maslach&rsquo;s six factors have in common?",
             "a": ["They are conditions that management and the organization have the power to change",
                   "They are traits of the individual employee that screening can find",
                   "They were each measured in the authors&rsquo; own survey",
                   "They apply only to technology work"],
             "c": 0,
             "why": "The chapter says all of the risk factors are things that "
                    "management and organizations can change. They are from "
                    "Leiter and Maslach (2008), not measured one by one in the "
                    "authors&rsquo; survey, and the chapter does not limit them to "
                    "technology."},
            {"q": "On the preset <code>team</code>, which respondent has the highest burnout mean?",
             "a": ["r2, whose raw answers add to 16",
                   "r6, with a mean of 6.5 after reversing",
                   "r1, with a mean of 5.75 after reversing",
                   "r3, who answered near the middle of the scale throughout"],
             "c": 1,
             "why": "After reversing, r6 answers 7, 6, 7, 6, a mean of 6.5. r1 is "
                    "5.75, r4 5.5, r3 4.0, and r2, whose raw answers add to 16 "
                    "but whose last two are reversed from 6 to 2, is 2.0."},
            {"q": "Which sentence matches the chapter&rsquo;s own advice on where to act?",
             "a": ["Concentrate on helping individuals cope; the environment changes slowly",
                   "Remove burned-out people from critical systems",
                   "Change the work environment; fixing the person alone is less likely to succeed",
                   "Wait for the survey to show a high mean before acting"],
             "c": 2,
             "why": "The authors write that managers often fix the person while "
                    "ignoring the environment, and that changing the environment "
                    "is far more important for long-term success; Maslach&rsquo;s "
                    "research shows it is likelier to work."},
        ],
        "mistakes": [
            ("Treating burnout as the result of an individual's weakness to be fixed in the person",
             "The chapter says this is exactly what managers tend to do and that it "
             "is a mistake: the six risk factors are conditions of the workplace, "
             "and fixing the environment is likelier to work."),
            ("Averaging the raw answers, reversed items included",
             "A reversed item points the other way, so averaging it raw cancels "
             "real signal: on the lab&rsquo;s team the raw mean is 3.833 and the "
             "scored one 4.417, and no respondent is above the line."),
            ("Reading the official values as the values that count",
             "The authors say that it is the real, lived values felt by employees "
             "that count. A mission statement that differs from what people live "
             "does not protect against burnout."),
        ],
        "standard": (
            "Finish when you can score a construct with reversed items.",
            "Given items, answers and which items are reversed, find each "
            "respondent&rsquo;s score and the team&rsquo;s by hand, and say what "
            "forgetting a reversal would do."
        ),
        "note": (
            "The lab averages the answers you type. It cannot say whether the "
            "items measure burnout, whether the line is meaningful (the book "
            "gives none), or why a respondent answered as they did; those are "
            "judgements a manager makes by asking."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 10, Employee Loyalty and Measuring NPS (PDF pp. 138-142): the
    # chapter's aims (p. 138); the 2.2 and 1.8 figures (pp. 139-140); the
    # NPS bands (pp. 139-140); the two questions asked (p. 140); constructs
    # eNPS was correlated with (p. 141); NPS Explained, with the subtraction
    # (pp. 141-142). The 2016 survey year in which eNPS was added is on
    # p. 30 (Preface).
    # Quote: PDF p. 142 of the operator's copy, 14 words, quotes.py OK.
    # Lesson total: 14 words.
    {
        "slug": "employee-loyalty-and-nps",
        "title": "Employee Loyalty and the Net Promoter Score",
        "module": "Chapter 10 · Employee Satisfaction, Identity, and Engagement",
        "one_line": "One question, three bands and a subtraction: how the authors measured loyalty, and why one answer can move the score by ten points.",
        "summary": (
            "Chapter 10 borrows a measure from customer loyalty and asks employees "
            "whether they would recommend their organization and their team as places "
            "to work. Read the bands, the arithmetic and the finding that people on "
            "high-performing teams were more likely to be promoters; then compute an "
            "employee Net Promoter Score from ten invented answers and see which "
            "single answers move it."
        ),
        "key": [
            "one question, answered from 0 to 10",
            "9 or 10 promote; 7 or 8 are passive",
            "0 to 6 detract",
            "promoters minus detractors, as percents",
            "passives count in the total, not the score",
            "an answer matters only if it changes band",
        ],
        "key_label": "The employee Net Promoter Score in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, the first two the chapter&rsquo;s and "
            "the third the lab&rsquo;s."
        ),
        "concepts": [
            ("Promoter, passive, detractor",
             "The three bands of a 0 to 10 answer to \"how likely are you to "
             "recommend ...\". Promoters answer 9 or 10, passives 7 or 8 and "
             "detractors anything from 0 to 6."),
            ("Employee Net Promoter Score (eNPS)",
             "The percentage of respondents who are promoters minus the percentage "
             "who are detractors. It runs from minus 100 to 100, and passives are "
             "counted in the total but not in the subtraction."),
            ("A band edge",
             "The step between two answers that fall in different bands, 6 to 7 "
             "or 8 to 9. The lab lists the answers that sit one step below an "
             "edge, because moving them changes the score."),
        ],
        "read_title": "The chapter's argument, then the score",
        "read_intro": (
            "Read Employee Loyalty and the boxes Measuring NPS and NPS Explained in "
            "your own copy first. The lesson reads them as a method and a finding, "
            "then computes the score from answers of its own."
        ),
        "body": [
            ("p", "Chapter 10 begins with people. Its opening claims that "
                  "engaged and satisfied employees are loyal and identify with the organization, are less prone to burnout and help drive profitability, productivity and market share, and promises to show how to "
                  "measure them. The first measure is loyalty, and the authors "
                  "borrow it from customers. The net promoter idea scores a company by asking one thing: would you tell a friend or colleague to use us? The chapter&rsquo;s own "
                  "summary of the arithmetic is the one this lesson opens on: "
                  "&ldquo;NPS is calculated by subtracting the percentage of "
                  "detractors from the percentage of promoters.&rdquo;"),
            ("p", "The answers run from 0 to 10, and three bands do the work. "
                  "People who answer 9 or 10 are promoters; among customers, the chapter credits promoters with spending more, costing less to win and keep, and talking the company up. "
                  "People who answer 7 or 8 are passives, satisfied but much less "
                  "enthusiastic and more likely to leave for something better. "
                  "People who answer from 0 to 6 are detractors. For employees the authors asked two versions, one about the organization as a place to work and one about the team. The authors say such a single-question measure may look "
                  "simple, and cite earlier work that found customer NPS "
                  "correlated with company growth in many industries."),
            ("p", "Their finding is a comparison of groups. The authors compared the "
                  "share of promoters among people in high-performing teams, those "
                  "the earlier chapters define, with the share among people in "
                  "low-performing teams. Promoters were 2.2 times as likely to be found among employees of high-performing teams when the question was about the organization, and 1.8 times as likely when it was about the team. Notice that the thing being "
                  "compared is the proportion of promoters, not the score itself, "
                  "and that the Preface says the employee questions were added to "
                  "the survey of 2016; the chapter does not give a year for the "
                  "comparison, so this lesson gives none."),
            ("p", "The authors add that the employee score was significantly "
                  "correlated with three things: how much the organization gathers customer feedback and lets it shape its products, how well teams can see their work travel from idea to customer, and how strongly employees identify with the organization&rsquo;s values and goals and put in effort for its success. Chapter 11 will add that "
                  "transformational leadership was highly correlated with it. "
                  "Their reading is that loyal people engage most and do their best work, and that this lifts company performance. "
                  "That is a reading of a correlation, at the strength of the "
                  "word the chapter uses."),
            ("p", "Now the arithmetic, which is short but has an edge. The lab "
                  "scores the preset <code>team</code>, ten invented answers to "
                  "one question: 10, 9, 9, 9, 8, 8, 7, 6, 5, 3. Four answers are 9 "
                  "or 10, so 40 percent are promoters; three are 7 or 8, so 30 "
                  "percent are passive; three are from 0 to 6, so 30 percent "
                  "are detractors. The score is 40 minus 30, which is 10. The "
                  "passives do not appear in the subtraction, though they are "
                  "counted in the ten."),
            ("p", "Now move a single answer. In <code>eight-to-nine</code> one "
                  "respondent who said 8 says 9 instead; the passive becomes a "
                  "promoter, five of ten are now promoters and the score is 50 "
                  "minus 30, or 20. The score rose by 10 points because one person "
                  "in ten changed from 8 to 9. In <code>eight-to-seven</code> one "
                  "respondent who said 8 says 7: both are passive, and the score "
                  "stays at 10. An answer matters to the score only when it "
                  "crosses an edge, from 8 to 9 or from 6 to 7, and the lab "
                  "lists which respondents sit just below one. The employee is "
                  "the same person in both cases."),
            ("p", "What it cannot tell you is why. A score of 10 is a number "
                  "about a team of ten; nothing in the subtraction says whether "
                  "the three detractors are unhappy with the work, the pay or a "
                  "manager. The lesson keeps to the strength the chapter gives: an "
                  "association, in the authors&rsquo; survey, between "
                  "high-performing teams and a greater likelihood of promoters."),
            ("h3", "Exercise"),
            ("ul", [
                "A team of ten answers, 0 to 10: `10, 9, 8, 8, 7, 7, 7, 6, 5, 4`.",
            ]),
            ("p", "Count the promoters, passives and detractors, find the two "
                  "percentages and subtract. Then say which answers would raise the "
                  "score if each moved up by one, and by how much each would. Type "
                  "the ten answers in to check."),
            ("p", "The score is also a number about a sample, here a team of ten, "
                  "and a team of ten has a coarse scale: every respondent is worth "
                  "10 points. The next lesson, Identity and Job Satisfaction, moves "
                  "from a single question to two measures built from several."),
        ],
        "lab": ("acckit", {
            "mode": "groups",
            "view": "enps",
            "preset": "team",
            "presets": [
                {"id": "team",
                 "label": "Ten invented answers to one recommend-it question",
                 "answers": ENPS_TEAM,
                 "expect": {
                    "agrN": "10",
                    "agrPromoters": "4 of 10 = 40%",
                    "agrPassives": "3 of 10 = 30%",
                    "agrDetractors": "3 of 10 = 30%",
                    "agrEnps": "+10",
                    "agrNear": "3: 1 at 6 (a detractor one point from passive), 2 at 8 (a passive one point from promoter); each one moved raises eNPS by 10 points",
                 }},
                {"id": "eight-to-nine",
                 "label": "One 8 becomes a 9",
                 "answers": ENPS_UP,
                 "expect": {
                    "agrN": "10",
                    "agrPromoters": "5 of 10 = 50%",
                    "agrPassives": "2 of 10 = 20%",
                    "agrDetractors": "3 of 10 = 30%",
                    "agrEnps": "+20",
                    "agrNear": "2: 1 at 6 (a detractor one point from passive), 1 at 8 (a passive one point from promoter); each one moved raises eNPS by 10 points",
                 }},
                {"id": "eight-to-seven",
                 "label": "One 8 becomes a 7",
                 "answers": ENPS_INSIDE,
                 "expect": {
                    "agrN": "10",
                    "agrPromoters": "4 of 10 = 40%",
                    "agrPassives": "3 of 10 = 30%",
                    "agrDetractors": "3 of 10 = 30%",
                    "agrEnps": "+10",
                    "agrNear": "2: 1 at 6 (a detractor one point from passive), 1 at 8 (a passive one point from promoter); each one moved raises eNPS by 10 points",
                 }},
            ],
            "panel_title": "Promoters, passives, detractors",
            "panel_intro": (
                "A figure computed from the small sample the lesson states. It "
                "shows what one measure says about that sample; the book's "
                "findings are its survey's."
            ),
        }),
        "steps_title": "Computing an employee Net Promoter Score",
        "steps_intro": "Four steps, the last of them on a team of your own.",
        "steps": [
            ("Sort every answer into a band",
             "9 and 10 are promoters, 7 and 8 passives, 0 to 6 detractors. Count "
             "each band and check the three counts add to the number of answers."),
            ("Turn the counts into percentages",
             "Divide the promoters and the detractors by the total number of "
             "answers, passives included, and multiply by 100."),
            ("Subtract",
             "Promoters&rsquo; percentage minus detractors&rsquo;. The result "
             "lies between minus 100 and 100 and is a whole number when the "
             "total divides 100 evenly."),
            ("Find the edges on a team of your own",
             "Take anonymous answers from a team you know, enter them in the "
             "lab, and list the answers that sit one step below an edge. Note by "
             "how much each of those moves would change the score."),
        ],
        "worked": {
            "title": "The score for ten invented answers",
            "intro": [
                "Score <code>team</code> and then <code>eight-to-nine</code>.",
            ],
            "lines": [
                "Answers 10, 9, 9, 9, 8, 8, 7, 6, 5, 3",
                "Promoters (9 or 10): 10, 9, 9, 9 = 4 of 10 = 40%",
                "Passives (7 or 8): 8, 8, 7 = 3 of 10 = 30%",
                "Detractors (0 to 6): 6, 5, 3 = 3 of 10 = 30%",
                "Score = 40 - 30 = 10",
                "One 8 becomes a 9: promoters 5 = 50%, detractors 30%; 50 - 30 = 20",
            ],
            "after": [
                "Only the one respondent changed band, and one in ten is worth "
                "10 points. The same respondent moving from 8 to 7 changes no "
                "band and no score.",
            ],
        },
        "quiz_title": "Bands, arithmetic and the chapter's comparison",
        "quiz": [
            {"q": "For the exercise answers, what is the employee Net Promoter Score?",
             "a": ["Plus 20, the percentage of promoters alone",
                   "Minus 20, dividing by only the promoters and detractors",
                   "Minus 30, the percentage of detractors alone",
                   "Minus 10"],
             "c": 3,
             "why": "Two answers (10 and 9) are promoters, five (8, 8, 7, 7, 7) are "
                    "passive and three (6, 5, 4) are detractors, out of ten. "
                    "20 percent minus 30 percent is minus 10. Plus 20 leaves out the "
                    "subtraction; minus 20 is 2 minus 3 over 5 answers, "
                    "which drops the passives from the total; minus 30 leaves out "
                    "the promoters."},
            {"q": "On the preset <code>team</code>, one respondent who answered 6 "
                  "changes to 7. What happens to the score?",
             "a": ["It rises to 20, because a detractor becomes a passive",
                   "It stays at 10, because 6 and 7 are neighbours",
                   "It rises to 20, because a detractor becomes a promoter",
                   "It rises to 11, in proportion to the change in the mean"],
             "c": 0,
             "why": "6 is the highest detractor answer and 7 the lowest passive "
                    "one, so the move crosses an edge: detractors fall from 3 to "
                    "2, giving 40 minus 20, which is 20. It does not reach the "
                    "promoter band, and the score depends on bands, not on the "
                    "mean answer."},
            {"q": "In Chapter 10, what was compared to give the 2.2 and the 1.8?",
             "a": ["The employee Net Promoter Scores of the high and low groups, as a ratio",
                   "The proportions of promoters in high-performing and low-performing groups",
                   "The mean answers to the two questions, in the same year",
                   "The number of detractors on teams with and without Lean practices"],
             "c": 1,
             "why": "The authors compared the proportion of promoters in the "
                    "high-performing group with that in the low-performing group, "
                    "and found promoters 2.2 times as likely in the high group for the organization question and 1.8 times as likely for the team question. A score can be negative, so a ratio of "
                    "scores would not mean anything."},
        ],
        "mistakes": [
            ("Leaving the passives out of the total",
             "Passives are counted in the total but not in the subtraction. "
             "Dividing by only the promoters and detractors overstates both "
             "percentages, and the score with them."),
            ("Reading a score as the mean answer",
             "The score counts people in bands, not points on a scale. A team whose "
             "mean answer is 7.1 can have a negative score, as the exercise does, "
             "and a respondent moving from 8 to 7 changes nothing."),
            ("Hearing \"2.2 times more likely\" as \"a score 2.2 times higher\"",
             "The authors compared the shares of promoters in two groups. That is "
             "a ratio of proportions in their survey, not a ratio of scores, and the "
             "lab&rsquo;s later lessons compute such a ratio."),
        ],
        "standard": (
            "Finish when you can score a team and say which answers matter.",
            "Given a list of 0 to 10 answers, sort them into bands, compute the "
            "score by hand, and name an answer whose move would change it and one "
            "whose move would not."
        ),
        "note": (
            "The lab counts the answers you give it. It cannot say what a "
            "respondent meant, and with ten answers one person is a tenth of the "
            "score; the authors' comparison rests on thousands of respondents."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 10, Changing Organizational Culture and Identity (PDF pp.
    # 142-145), How Does Job Satisfaction Impact Organizational Performance
    # (pp. 145-146), How Does DevOps Contribute to Job Satisfaction (pp.
    # 146-147). The identity items are listed on p. 143 (six statements; the
    # text says "the five item scores"); the lesson does not quote or list them.
    # Quote: PDF p. 145 of the operator's copy, 28 words, quotes.py OK.
    # Lesson total: 28 words.
    {
        "slug": "identity-and-job-satisfaction",
        "title": "Identity and Job Satisfaction",
        "module": "Chapter 10 · Employee Satisfaction, Identity, and Engagement",
        "one_line": "Two constructs built from several survey items each, and the chapter's case that technical practice reaches them both.",
        "summary": (
            "Chapter 10 adds two measures built from several answers: how far people "
            "identify with their organization, and how satisfied they are with their "
            "work, their tools and the use made of their skills. Read how the authors "
            "built them and what they found them to predict; then compute both from "
            "invented answers for two teams and see that one can be high while the "
            "other is not."
        ),
        "key": [
            "identity: how far you identify with the firm",
            "satisfaction: work, tools and your skills",
            "each is the mean of several items",
            "identity predicted organizational performance",
            "tools and automation go with satisfaction",
            "two constructs can come apart",
        ],
        "key_label": "Identity and job satisfaction in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter&rsquo;s, "
            "the third the lab&rsquo;s."
        ),
        "concepts": [
            ("Identity",
             "The extent to which people identify with the organization they work "
             "for: whether they are glad to work there, speak well of it, give extra "
             "effort for it and share its values and goals. The authors measure it "
             "with several agree-disagree statements."),
            ("Job satisfaction",
             "In the chapter's measure, three things: being satisfied in your work, "
             "being given the tools and resources to do it, and having a job that puts your skills to good use."),
            ("Construct",
             "A quantity, such as identity, that cannot be observed directly and "
             "is measured by several items taken together. A person&rsquo;s "
             "score is the mean of their answers to the construct&rsquo;s items."),
        ],
        "read_title": "The chapter's argument, then the two scores",
        "read_intro": (
            "Read the three sections after Employee Loyalty in your own copy first, "
            "from Changing Organizational Culture and Identity to How Does DevOps "
            "Contribute to Job Satisfaction. The lesson reads them as a chain of "
            "claims, then scores them on teams of its own."
        ),
        "body": [
            ("p", "&ldquo;[P]eople who feel supported by their employers, who have the "
                  "tools and resources to do their work, and who feel their "
                  "judgment is valued, turn out better work.&rdquo; The sentence is "
                  "from the section of Chapter 10 on how job satisfaction affects "
                  "organizational performance, and it is the chapter&rsquo;s "
                  "argument in miniature: how people feel about their work and "
                  "their organization is not a side effect of delivery; it joins a "
                  "cycle with it. The chapter reaches this through two measures, "
                  "identity and job satisfaction."),
            ("p", "The authors added identity, they say, because they expected teams that practice "
                  "continuous delivery and take an experimental approach to "
                  "product development to build better products and to feel closer to the rest of the organization. They asked respondents how far they agreed with six statements adapted from Kankanhalli and colleagues (2005), on being glad to work there, sharing the organization's values and goals, and the like. They used "
                  "Likert-type agreement scales, and the items passed the "
                  "statistical conditions for measuring a construct, so a "
                  "person&rsquo;s identity can be taken as the average of the item "
                  "scores; the chapter points to Chapter 13 for those conditions. "
                  "(The chapter lists six statements and says &lsquo;five item "
                  "scores&rsquo;, so check the count in your own copy before "
                  "borrowing the scale.)"),
            ("p", "Identity predicted both a generative culture and organizational performance (productivity, market share, profitability). The authors connect it back to burnout, since "
                  "identity includes the matching of personal and organizational "
                  "values that the last lesson saw is a risk factor, and set it "
                  "against the way many companies still work, handing requirements "
                  "to a team that then delivers large batches, which leaves "
                  "people with little control and little connection. They tell a "
                  "story: Netflix&rsquo;s cloud architect, Adrian Cockcroft, asked by "
                  "a senior leader of a large company where he found his "
                  "remarkable people, answered that he had hired them from that "
                  "very company."),
            ("p", "Job satisfaction is built differently. The authors say their "
                  "measure looks at a few key things: whether you are satisfied "
                  "with your work, whether you are given the tools and resources "
                  "you need, and whether the job puts your skills to good use. Taken together, they say, these are what make "
                  "the measure so impactful, and the second and third are how "
                  "they connect it to DevOps. "
                  "Good technical practices predicted job satisfaction. "
                  "The chapter&rsquo;s reasoning is that automation gives the rote "
                  "tasks to computers and leaves people the work of weighing evidence "
                  "and deciding; practices such as proactive monitoring and "
                  "test and deployment automation, which put people in a feedback "
                  "loop, correlated strongly with it."),
            ("p", "The chain, then, runs like this. Technical and Lean practices were found to predict identity and job satisfaction. For satisfaction the chapter argues that supported people turn out better work, which results in higher delivery performance and in turn higher organizational performance, and that faster delivery lets teams validate ideas sooner, which raises satisfaction again. The authors call it a virtuous circle. Chapter 12 will explain what "
                  "&lsquo;predict&rsquo; means in their statistics: a prediction, "
                  "not a proof of cause."),
            ("p", "Now compute both constructs. The lab takes six invented items, "
                  "<code>i1</code> to <code>i3</code> on identifying with the "
                  "organization and <code>s1</code> to <code>s3</code> on "
                  "satisfaction with the work, its tools and its use of skills. "
                  "None of them is an item from the book. The preset "
                  "<code>alder</code> has four respondents on a 7-point scale; "
                  "the first answers 6, 6, 5 on identity, a sum of 17 and a mean of "
                  "5.667, and 5, 6, 6 on satisfaction, also 17. Over all four "
                  "respondents the identity mean is 63 over 12 answers, which is "
                  "5.25, and the satisfaction mean is 60 over 12, which is 5."),
            ("p", "The preset <code>birch</code> is a second invented team of four "
                  "whose satisfaction answers also add to 60, a mean of 5; its "
                  "identity answers add to 39, a mean of 3.25. Two teams are "
                  "equally satisfied and one identifies much less. That is the "
                  "reason the chapter treats them as two constructs, each "
                  "with its own items, not as one feeling. The lab does not tell you "
                  "which team is better off; it shows two columns that "
                  "need different questions, and the lab&rsquo;s status line says "
                  "again that the figures are of these eight invented people."),
            ("h3", "Exercise"),
            ("ul", [
                "A third invented team, 7-point scale. Items `i1`, `i2` measure "
                "identity and `s1`, `s2` satisfaction.",
                "Answers, written as respondent, `i1`, `i2`, `s1`, `s2`: "
                "`c1, 6, 6, 3, 4`; `c2, 5, 7, 2, 3`; `c3, 4, 4, 5, 6`.",
            ]),
            ("p", "Score each respondent on each construct, then find the "
                  "team&rsquo;s mean for each, and the difference between them. "
                  "Say in a sentence what a manager could do with the finding "
                  "that the two differ, and what the lab cannot tell them."),
            ("p", "The chapter ends its treatment of these two measures and turns "
                  "to a harder subject, one in which numbers must be handled with "
                  "particular care. The next lesson is Diversity in Tech."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "score",
            "preset": "alder",
            "presets": [
                {"id": "alder",
                 "label": "Team Alder: four respondents, identity and satisfaction items",
                 "points": 7,
                 "items": TWO_CONSTRUCTS,
                 "answers": ALDER_ANSWERS,
                 "expect": {
                    "alkN": "4",
                    "alkConstructs": "identity 5.25; satisfaction 5",
                    "alkLine": "identity: 4 above, 0 at, 0 below; satisfaction: 3 above, 0 at, 1 below",
                 }},
                {"id": "birch",
                 "label": "Team Birch: the same satisfaction mean, a lower identity mean",
                 "points": 7,
                 "items": TWO_CONSTRUCTS,
                 "answers": BIRCH_ANSWERS,
                 "expect": {
                    "alkN": "4",
                    "alkConstructs": "identity 3.25; satisfaction 5",
                    "alkLine": "identity: 1 above, 0 at, 3 below; satisfaction: 4 above, 0 at, 0 below",
                 }},
            ],
            "panel_title": "Two constructs, two means",
            "panel_intro": (
                "A figure computed from the small sample the lesson states. It "
                "shows what one measure says about that sample; the book's "
                "findings are its survey's."
            ),
        }),
        "steps_title": "Scoring two constructs",
        "steps_intro": "Four steps, the last of them on a survey of your own.",
        "steps": [
            ("Assign each item to a construct",
             "Write down which items measure identity and which satisfaction. An "
             "item belongs to one construct only."),
            ("Average within each construct",
             "For each respondent add up their answers to the construct&rsquo;s "
             "items and divide by the number of items. Do the other construct "
             "separately."),
            ("Average across respondents",
             "A construct&rsquo;s team mean is the mean of the respondents&rsquo; "
             "scores. Compare the two constructs&rsquo; means for the same team."),
            ("Compare two groups on your own survey",
             "Score two teams of yours on both constructs, type them in, and "
             "note any construct where they are alike and any where they differ."),
        ],
        "worked": {
            "title": "Alder's two means",
            "intro": [
                "Score the preset <code>alder</code>. Each respondent has three "
                "identity answers and three satisfaction answers.",
            ],
            "lines": [
                "Identity sums: 17, 14, 19, 13; total 63; 63/12 = 5.25",
                "Satisfaction sums: 17, 13, 19, 11; total 60; 60/12 = 5",
                "Birch identity sums: 10, 8, 13, 8; total 39; 39/12 = 3.25",
                "Birch satisfaction sums: 16, 13, 17, 14; total 60; 60/12 = 5",
            ],
            "after": [
                "Every figure is a sum of the answers divided by their count. "
                "The lab prints the respondents&rsquo; means as thirds, to three "
                "decimals.",
            ],
        },
        "quiz_title": "Two constructs and the chapter's claims",
        "quiz": [
            {"q": "For the exercise team, what are the identity and satisfaction means?",
             "a": ["Identity 3.83 and satisfaction 5.33",
                   "Identity 5.33 and satisfaction 4.17",
                   "Identity 5.33 and satisfaction 3.83",
                   "Identity 4.58 and satisfaction 4.58, the grand mean of both"],
             "c": 2,
             "why": "Identity answers are 6, 6, 5, 7, 4, 4, which add to 32; over "
                    "six answers that is 5.33. Satisfaction answers are 3, 4, 2, "
                    "3, 5, 6, which add to 23, a mean of 3.83. Swapping the columns gives the other pair, and pooling both gives one mean for two constructs that the chapter treats as different."},
            {"q": "On the presets, how do Alder and Birch differ?",
             "a": ["Birch has the lower satisfaction mean",
                   "Both constructs are lower for Birch",
                   "They are the same on both",
                   "Birch has the lower identity mean, 3.25 against 5.25"],
             "c": 3,
             "why": "Both teams have satisfaction totals of 60 over 12 answers, "
                    "5, so they are alike on that; identity totals are 63 and "
                    "39, means of 5.25 and 3.25."},
            {"q": "Which three things does the chapter say its job satisfaction "
                  "measure looks at?",
             "a": ["Being satisfied in your work, having the tools and resources, and having your skills well used",
                   "Pay, title and length of service",
                   "How often you deploy, how long a change takes, and how quickly you recover",
                   "Whether you would recommend your team, your organization and your manager"],
             "c": 0,
             "why": "The chapter names satisfaction with the work, the tools and "
                    "resources to do it, and the use made of skills and abilities. "
                    "The delivery measures are the subject of Chapter 2, and the "
                    "recommendations are the employee Net Promoter Score."},
        ],
        "mistakes": [
            ("Thinking identity and job satisfaction are one measure",
             "They are built from different items and answer different questions. On "
             "the lab&rsquo;s two invented teams the satisfaction means are the "
             "same and the identity means are 5.25 and 3.25."),
            ("Reading 'predicts' as 'causes'",
             "The authors report that identity and good technical practices "
             "predicted outcomes. Their statistics are about prediction in a "
             "survey, and they call the result a virtuous circle, a reading they "
             "argue from several years of data."),
            ("Treating satisfaction as only about how much you like the work",
             "The chapter&rsquo;s measure includes the tools and resources you are "
             "given and whether your job uses your skills, which is why it can be "
             "connected to automation and monitoring."),
        ],
        "standard": (
            "Finish when you can score two constructs and say how they differ.",
            "Given items assigned to two constructs and each respondent&rsquo;s "
            "answers, compute every respondent&rsquo;s two scores and each "
            "team&rsquo;s two means by hand."
        ),
        "note": (
            "The lab averages the items you assign. It cannot say whether the "
            "items form a good construct (Surveys, Data and Statistical Methods reads the checks), whether "
            "either mean is high or low in general, or what produced it."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 10, Diversity in Tech: What Our Research Found, Women in DevOps,
    # Underrepresented Minorities in DevOps, What Other Research Tells Us
    # About Diversity, What We Can Do (PDF pp. 147-154). Figures: 5% in 2015,
    # 6% in 2016, 6.5% in 2017 and the comparison figures from SAGE and Diaz
    # and King (p. 148); 33%, 56% and 81% (pp. 148-149), no year given in the
    # passage; 91/6/3 in the 2017 study (p. 150); 77/12/11 in the 2017 study
    # (pp. 151-152); the sampling note (p. 152, and Chapter 15 p. 214 on the
    # snowball sample's invitations). Appendix A (p. 262) repeats the figures.
    # The 23,000 responses over the four years are on p. 24 (Preface).
    # Quote: PDF p. 148 of the operator's copy, 11 words, quotes.py OK.
    # Lesson total: 11 words.
    {
        "slug": "diversity-in-tech",
        "title": "Diversity in Tech",
        "module": "Chapter 10 · Employee Satisfaction, Identity, and Engagement",
        "one_line": "What the authors report about women and underrepresented minorities in their sample, what they cite from other research, and why a share of respondents is not a share of the industry.",
        "summary": (
            "Chapter 10 closes with diversity: the authors say few teams in their "
            "data are diverse, give the shares of respondents by gender and by "
            "identification as underrepresented in the years they asked, cite "
            "other research on why diversity helps and why people leave, and add "
            "that diversity is not enough without inclusion. Read what they report "
            "and how far it reaches; then see on an invented sample how the share "
            "of a group among respondents can differ from its share of the "
            "industry."
        ),
        "key": [
            "few teams in the sample are diverse",
            "the book's figures are of its respondents",
            "benefits cited from other research",
            "inclusion is needed as well as diversity",
            "respondents' share is not the field's share",
            "outreach changes who answers",
        ],
        "key_label": "Diversity in Tech in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter&rsquo;s, "
            "the third the lab&rsquo;s."
        ),
        "concepts": [
            ("Inclusion",
             "The chapter&rsquo;s word, after Smith and Lindsay, for an organization where every member is welcomed and belongs; the authors say diversity does not last without it."),
            ("Underrepresented minority",
             "In the survey, a respondent&rsquo;s own answer to whether they "
             "identify as underrepresented. The authors explain that because the "
             "data came from around the world, self-identification was as specific "
             "as they could be, since the groups that count as minorities differ "
             "by country."),
            ("Share and ratio",
             "A group&rsquo;s share is its members who meet a condition (here, "
             "answered) over its size. A ratio of two shares says how many times "
             "as likely one group is to meet it; a difference in percentage "
             "points says how far apart they are."),
        ],
        "read_title": "The chapter's argument, then the count",
        "read_intro": (
            "Read the last part of Chapter 10, from Diversity in Tech to What We "
            "Can Do, in your own copy first. The lesson sets out what the authors "
            "report, with the year and the sample for each figure, what they "
            "borrow from other research, and what can and cannot be concluded."
        ),
        "body": [
            ("p", "The authors begin the section with a position and a "
                  "limit. The position is that diversity matters: they cite "
                  "research that teams with more diversity in gender or "
                  "underrepresented minorities are smarter, achieve better team "
                  "performance and better business outcomes. The limit is on their "
                  "own data, in which few teams are diverse. They recommend that "
                  "teams who want high performance hire and keep more women and members of underrepresented groups, and work on other kinds of diversity, for example including people with disabilities. "
                  "They then add &ldquo;diversity is not enough. Teams and "
                  "organizations must also be inclusive.&rdquo;"),
            ("p", "Note whose findings these are. The benefits of diversity are "
                  "reported from other research, by Rock and Grant in 2016, "
                  "Deloitte in 2013 and Hunt and colleagues in 2015, and later "
                  "in the section the authors cite a study by Woolley and Malone "
                  "of the collective intelligence of groups. Accelerate&rsquo;s own "
                  "survey does not report a test of them. What it does contribute is a "
                  "description of who answered, and that is what the next "
                  "paragraphs set out, in the words and with the years the "
                  "chapter gives."),
            ("p", "On gender, the authors began asking in 2015. Of all respondents, "
                  "5 percent identified as female in 2015, 6 percent in 2016 and "
                  "6.5 percent in 2017. They say the figures were much lower than they expected, given outside figures of about 7 percent women in systems administration in 2011 (13 percent in 2008) and 27 percent in computer and information management, per Diaz and King in 2013. The chapter gives 6.5 percent for 2017 in one place and 6 percent in its 2017 breakdown, and does not reconcile them. Among the survey respondents, 33 percent reported a team with no women on it, 56 percent a team under 10 percent female and 81 percent a team under 25 percent female; the passage does not name a year for these three "
                  "figures. For the 2017 study alone the authors report 91 "
                  "percent male, 6 percent female and 3 percent non-binary or "
                  "other. They say they started with binary gender in order to "
                  "compare with existing research, and hope to extend their work "
                  "to non-binary gender."),
            ("p", "On underrepresented minorities, they asked respondents in "
                  "2017 whether they identify as underrepresented: 77 percent "
                  "answered no, 12 percent yes and 11 percent preferred not to "
                  "respond or answered not applicable. The authors explain that "
                  "the data came from around the world, so they could not "
                  "ask about particular groups; the United States defines several "
                  "minorities that would not make sense elsewhere. They add that "
                  "they have not yet extended the research to people with "
                  "disabilities. The sample behind all of these is the survey's: "
                  "over 23,000 responses in the research as a whole, reached by "
                  "invitation and referral, which Chapter 15 describes."),
            ("p", "What other research says, according to the authors: studies "
                  "link women in leadership with higher financial performance; "
                  "there is no significant difference between men and women in "
                  "ability or aptitude in the STEM fields; and women are "
                  "leaving tech at a 45 percent higher rate than men, a figure they "
                  "attribute to a 2017 source. Citing Leslie and colleagues (2015), they suggest that a widespread belief in some men&rsquo;s innate gift for technical work may keep women and others out; a footnote says that study covered only women and African Americans. They also cite reports of harassment, "
                  "microaggressions and unequal pay. These are the authors&rsquo; "
                  "reading of other people&rsquo;s studies. They end with "
                  "resources, among them the Anita Borg Institute, Geek Feminism "
                  "and Project Include, and with the call for all of us to "
                  "prioritize diversity and inclusive environments."),
            ("p", "Now the count, and a caution about reading a share. The authors "
                  "read the low figures as a real shortfall, and the team figures point the same way. Even so, 6.5 percent of respondents is a share of the people who answered, not a measured share of the industry, and the two can differ for reasons of how the survey was distributed. Nothing in the book says which way, if at all, its share differs from the field&rsquo;s; the field cannot be counted (Chapter 15), so the lab below assumes a known field only to show the mechanism. In Chapter 15 the "
                  "authors explain that their invitations came from several "
                  "mailing lists, referrals and reaching out to underrepresented "
                  "groups through their own lists, and they name the limits of "
                  "such a snowball sample themselves."),
            ("p", "The lab shows that effect on invented numbers. An invented "
                  "region has 1,000 engineers: 800 in Group A and 200 in Group B, "
                  "so Group B is 20 percent of the field. Group B stands for any "
                  "group that the invitations reach less well. In the preset "
                  "<code>first-wave</code> 240 of Group A answer and 30 of Group "
                  "B. The lab reports the shares that answered as 30 percent and "
                  "15 percent, a ratio of 2 (Group A is twice as likely to "
                  "answer) and a gap of 15 percentage points. Work out the "
                  "composition of the sample by hand: 30 of the 270 answers are "
                  "Group B, 11.1 percent, against 20 percent of the field."),
            ("p", "In <code>second-wave</code> an invitation is added through "
                  "a list that Group B uses, and 60 of its 200 answer. Both groups "
                  "now answer at 30 percent, the ratio is 1 and the gap is 0, "
                  "and Group B is 60 of the 300 answers, 20 percent, the "
                  "same as its share of the field. The respondent shares matched "
                  "the field, in this invented case, only because the answering "
                  "rates did. Notice also that the lab prints a ratio and an odds ratio separately. The ratio, 2 in the first wave, is what the book means by &lsquo;times as likely&rsquo;, as in Chapter 10&rsquo;s loyalty finding; "
                  "the odds ratio, 2.43, is a different number."),
            ("h3", "Exercise"),
            ("ul", [
                "An invented region of 1,000: Group P has 600 people, Group Q "
                "400. In a survey, 180 of P answered and 80 of Q: `Group-P, 600, "
                "180; Group-Q, 400, 80`.",
            ]),
            ("p", "Find each group's share that answered, the ratio of P to Q "
                  "and the gap in percentage points. Then find Q's share of the "
                  "answers and compare it with its share of the 1,000. Type the rows in to check the shares, ratio and gap; the share of the answers is by hand."),
            ("p", "These counts say something about how a sample was drawn, and "
                  "nothing about why people leave or stay, which the authors "
                  "attribute to the cultures they work in and the studies they "
                  "cite. The next lesson, Transformational Leadership, begins "
                  "Chapter 11 and the role of the people who set the tone."),
        ],
        "lab": ("acckit", {
            "mode": "groups",
            "view": "likely",
            "preset": "first-wave",
            "presets": [
                {"id": "first-wave",
                 "label": "An invented region: who answered the first invitation",
                 "rows": SURVEY_FIRST, "first": "Group-A", "second": "Group-B",
                 "expect": {
                    "agrShares": "Group-A 240 of 800 = 30%; Group-B 30 of 200 = 15%",
                    "agrRatio": "2.00×",
                    "agrDiff": "+15 points",
                    "agrOdds": "≈ 2.43",
                 }},
                {"id": "second-wave",
                 "label": "The same region, after an invitation through a list Group B uses",
                 "rows": SURVEY_SECOND, "first": "Group-A", "second": "Group-B",
                 "expect": {
                    "agrShares": "Group-A 240 of 800 = 30%; Group-B 60 of 200 = 30%",
                    "agrRatio": "1.00×",
                    "agrDiff": "0 points",
                    "agrOdds": "1.00",
                 }},
            ],
            "panel_title": "Who answered, group by group",
            "panel_intro": (
                "A figure computed from the small sample the lesson states. It "
                "shows what one measure says about that sample; the book's "
                "findings are its survey's. These groups and counts are "
                "invented to show how a sample can differ from a population."
            ),
        }),
        "steps_title": "Comparing a sample with its population",
        "steps_intro": "Four steps, the last of them on a survey of your own.",
        "steps": [
            ("Write each group's size and responses",
             "For each group, how many were invited (or exist) and how many "
             "answered. Keep invited and answered in separate columns."),
            ("Compute each group's response share",
             "Answered over invited, as a percentage. Then the ratio of one "
             "group&rsquo;s share to the other&rsquo;s, and the gap in percentage "
             "points."),
            ("Compare the sample with the population",
             "A group&rsquo;s share of the answers is its answers over all the "
             "answers; its share of the field is its size over all sizes. Put "
             "the two side by side."),
            ("Check a survey of your own",
             "Take a survey you have run or answered, and compare who was "
             "invited, who answered and who the population is. Name who an "
             "invitation might have missed and what would reach them."),
        ],
        "worked": {
            "title": "Group B in the first wave",
            "intro": [
                "Work the preset <code>first-wave</code>: Group A has 800 people "
                "and 240 answers, Group B 200 people and 30 answers.",
            ],
            "lines": [
                "Group A answered: 240/800 = 30%",
                "Group B answered: 30/200 = 15%",
                "Ratio A to B: 30/15 = 2; gap: 15 percentage points",
                "Answers in all: 240 + 30 = 270",
                "Group B in the sample: 30/270 = 11.1%",
                "Group B in the field: 200/1000 = 20%",
            ],
            "after": [
                "Group A's odds of answering are 240 to 560, Group B's 30 to 170. "
                "Their ratio, 2.43, is not the ratio of shares, 2.",
            ],
        },
        "quiz_title": "What the chapter reports, and what a share shows",
        "quiz": [
            {"q": "Which gives the chapter&rsquo;s shares of respondents who "
                  "identified as female in 2015, 2016 and 2017?",
             "a": ["6.5%, 6% and 5%",
                   "5%, 6% and 6.5%",
                   "7%, 13% and 27%",
                   "33%, 56% and 81%"],
             "c": 1,
             "why": "The chapter reports 5 percent in 2015, 6 percent in 2016 and "
                    "6.5 percent in 2017. The reversed order would mean the share "
                    "was falling. 7, 13 and 27 are figures from other sources for "
                    "systems administration in 2011 and 2008 and for computer and "
                    "information management; 33, 56 and 81 are the shares of "
                    "respondents on teams with no women, under 10 percent and "
                    "under 25 percent."},
            {"q": "For the exercise, what is Group Q&rsquo;s share of the answers?",
             "a": ["20%, which is 80 of 400",
                   "40%, which is 400 of 1000",
                   "30.8%, which is 80 of 260",
                   "50%, which is the gap in the shares"],
             "c": 2,
             "why": "Together 180 and 80 answered, 260 answers, and Q&rsquo;s 80 "
                    "are 30.8 percent of them. 20 percent is the share of Q that "
                    "answered; 40 percent is Q&rsquo;s share of the field, and "
                    "that comparison is the point."},
            {"q": "According to Chapter 10, whose research shows that diversity "
                  "improves team performance?",
             "a": ["The authors&rsquo; own survey, in each year it was run",
                   "Both the authors&rsquo; survey and other researchers, at the same strength",
                   "No one; the chapter only recommends it",
                   "Other researchers, whom the authors cite"],
             "c": 3,
             "why": "The authors cite other research on the benefits and report "
                    "that few teams in their own sample are diverse; they "
                    "recommend that teams hire and keep more women and members of underrepresented groups. They did not report testing the "
                    "benefit in their data."},
            {"q": "On <code>second-wave</code>, the lab reports a ratio of 1. "
                  "What does that mean?",
             "a": ["The two groups answered at the same share, 30%",
                   "The groups are the same size",
                   "Group B is now over-represented in the sample",
                   "The odds ratio is 2.43"],
             "c": 0,
             "why": "A ratio of shares is 1 when the shares are equal; here "
                    "both groups answered at 30 percent. The groups are still 800 "
                    "and 200, and the sample shares now match the field."},
        ],
        "mistakes": [
            ("Reading 6.5 percent of respondents as the share of women in the industry",
             "It is the share of the people who answered the 2017 survey, "
             "reached by invitation and referral. The authors themselves set it "
             "beside other figures for the field and found it lower than they "
             "expected."),
            ("Assuming the chapter shows that diverse teams perform better in its own data",
             "The benefit is reported from other studies, which the authors "
             "cite; what the chapter adds is who answered and how few teams are "
             "diverse."),
            ("Thinking diversity alone is the goal",
             "The chapter says a diverse team is only the start: it must also be inclusive, or the diversity does not last."),
        ],
        "standard": (
            "Finish when you can say what a share of respondents does and does not show.",
            "Given the counts invited and answered by two groups, compute the "
            "shares, their ratio and gap, each group's share of the answers, and "
            "say how that compares with its share of the field."
        ),
        "note": (
            "The groups and counts here are invented; they illustrate a sampling "
            "point and say nothing about any real group or the book's sample. The "
            "lab cannot say why people leave a field or stay, which the chapter "
            "attributes to its cited research."
        ),
    },
]
