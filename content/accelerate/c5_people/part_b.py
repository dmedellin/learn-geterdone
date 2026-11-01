"""Sustainable Work, Satisfaction and Leadership, lessons 6-7 -- Chapter 11.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 11, Leaders and Managers
(Transformational Leadership; The Role of Managers; Tips to Improve Culture
and Support Your Teams). Pages in the comments are PDF pages of the
operator's copy; the lessons cite by chapter and section. Every quotation is
copied from that copy and checked with quotes.py. The leader, the ratings, the
teams and the counts are invented for these lessons: none of the book's
tables, figures, survey items or example data is reproduced. The design is
docs/accelerate/PLAN.md, section C, Course 5.
"""

_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its "
    "survey's, and a correlation is not a cause."
)


# ---------------------------------------------------------------- 06 data

# One invented leader rated by six invented reports on a 7-point scale, two
# invented items for each of Rafferty and Griffin's five dimensions.
LEADER_ITEMS = (
    "v1, vision, no; v2, vision, no; "
    "c1, communication, no; c2, communication, no; "
    "s1, stimulation, no; s2, stimulation, no; "
    "u1, support, no; u2, support, no; "
    "r1, recognition, no; r2, recognition, no"
)
LEADER_RATINGS = (
    "p1, 6, 6, 5, 6, 5, 4, 6, 5, 3, 3; "
    "p2, 7, 6, 6, 6, 5, 5, 5, 6, 2, 3; "
    "p3, 5, 5, 5, 4, 4, 4, 6, 6, 3, 4; "
    "p4, 6, 7, 6, 5, 5, 6, 5, 5, 4, 3; "
    "p5, 6, 5, 4, 5, 4, 5, 6, 6, 2, 2; "
    "p6, 7, 7, 6, 6, 5, 5, 5, 6, 3, 4"
)
# The same reports a while later; only the two recognition items differ.
LEADER_LATER = (
    "p1, 6, 6, 5, 6, 5, 4, 6, 5, 4, 4; "
    "p2, 7, 6, 6, 6, 5, 5, 5, 6, 4, 4; "
    "p3, 5, 5, 5, 4, 4, 4, 6, 6, 4, 5; "
    "p4, 6, 7, 6, 5, 5, 6, 5, 5, 5, 4; "
    "p5, 6, 5, 4, 5, 4, 5, 6, 6, 3, 3; "
    "p6, 7, 7, 6, 6, 5, 5, 5, 6, 4, 5"
)


# ---------------------------------------------------------------- 07 data

# Forty invented teams: whether the team has a learning budget, and whether
# it met its goal for the quarter ("met").
BUDGET = "Budget, 20, 13; No-budget, 20, 7"
# The same forty, split by whether the team's manager also removes obstacles.
BUDGET_SPLIT = (
    "Budget-cleared, 16, 12; Budget-not-cleared, 4, 1; "
    "No-budget-cleared, 4, 3; No-budget-not-cleared, 16, 4"
)
# 07 exercise: thirty invented teams, metrics visible or not.
METRICS = "Visible, 15, 9; Not-visible, 15, 3"


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Chapter 11, Transformational Leadership (PDF pp. 155-162 of the
    # operator's copy): the case for leadership (pp. 155-157), the five
    # dimensions after Rafferty and Griffin (pp. 157-158), the box on what
    # transformational leadership is and its difference from servant
    # leadership (p. 158), measurement (pp. 158-159, footnote p. 168),
    # findings (pp. 160-161), "leaders alone" (p. 161), summary (pp. 161-162).
    # The 2017 survey year in which leadership was studied is on p. 31.
    # Appendix A repeats the findings (pp. 261-262).
    # Quote: PDF p. 161 of the operator's copy, 11 words, quotes.py OK.
    # Lesson total: 11 words.
    {
        "slug": "transformational-leadership",
        "title": "Transformational Leadership",
        "module": "Chapter 11 · Leaders and Managers",
        "one_line": "Five dimensions of leadership, rated by the people who report to the leader, and the finding that leaders enable results but cannot deliver them alone.",
        "summary": (
            "Chapter 11 turns to the people who set the tone. The authors measure "
            "transformational leadership with five dimensions from Rafferty and "
            "Griffin, report what teams of each level of performance said, and add "
            "that the very strongest leaders did not guarantee high performance. "
            "Read the argument, then score one invented leader on ten invented "
            "items and find the dimension with the lowest mean."
        ),
        "key": [
            "vision, communication, stimulation",
            "supportive leadership, personal recognition",
            "rated by the people who report to the leader",
            "high performers rated leaders higher",
            "leaders enable; teams and practices deliver",
            "the lowest mean is a question to ask",
        ],
        "key_label": "Transformational leadership in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter&rsquo;s, "
            "the third the lab&rsquo;s."
        ),
        "concepts": [
            ("Transformational leadership",
             "Leaders who move their followers to perform better by speaking to their values and their sense of purpose. The "
             "authors measure it through five dimensions, and note that being a "
             "leader is not the same as having people report to you."),
            ("The five dimensions",
             "From Rafferty and Griffin (2004): vision, inspirational "
             "communication, intellectual stimulation, supportive leadership and "
             "personal recognition. Each is measured by several survey items and "
             "scored as the mean of the answers."),
            ("A dimension mean",
             "The lab's figure: the mean of every report&rsquo;s answers to the "
             "items of one dimension. The lowest is where this leader&rsquo;s "
             "ratings, from these reports, are lowest; it is not a grade."),
        ],
        "read_title": "The chapter's argument, then the ratings",
        "read_intro": (
            "Read the opening of Chapter 11 and the section Transformational "
            "Leadership in your own copy first. The lesson reads it as an argument "
            "about indirect effects, then scores a leader on ratings of its own."
        ),
        "body": [
            ("p", "Chapter 11 admits a gap. In the first years of the research, "
                  "the authors say, they had not studied leadership directly; the "
                  "survey of 2017, the fourth year, was where they set out to "
                  "measure what transformational leadership does to software "
                  "delivery. Their answer comes with a limit stated in its own "
                  "words: &ldquo;we found evidence that leaders alone cannot "
                  "achieve high DevOps outcomes.&rdquo; This lesson reads that "
                  "claim, the evidence for it and the model of leadership behind "
                  "it."),
            ("p", "Why look at leaders at all? The authors say that leadership is "
                  "about inspiring and motivating those around you, and is not a "
                  "matter of who has people reporting to them on an organization "
                  "chart. They argue that its effects on profitability, "
                  "productivity, market share, customer satisfaction and "
                  "noncommercial goals are all indirect: they run through the technical and Lean practices that the leaders back. They name "
                  "four things for which they hold transformational leadership "
                  "essential: generative, high-trust cultural norms; technology "
                  "that makes developers productive; support for experimentation "
                  "and innovation; and work across organizational silos. They also "
                  "own up to a fault of their own community: DevOps people have "
                  "sometimes maligned leaders, such as middle managers who stand in "
                  "the way of change, even though leaders hold the authority "
                  "and budget for large changes, can give a transformation "
                  "air cover and can change the incentives of whole groups."),
            ("p", "Measuring needs a model. The authors adopted five dimensions "
                  "from Rafferty and Griffin (2004). Vision is knowing where the organization is heading and where it ought to stand in five years. Inspirational communication speaks in a way that lifts people, including when the ground is shifting. Intellectual stimulation pushes people to look at problems afresh. Supportive leadership shows regard for people&rsquo;s personal needs and feelings. Personal recognition means praising achievement and better quality of work, in person. They contrast the model with servant leadership, which "
                  "focuses on followers&rsquo; development and performance; "
                  "transformational leaders aim at followers&rsquo; commitment to the organization&rsquo;s goals. "
                  "They chose it because, in other settings, it predicts "
                  "performance outcomes better."),
            ("p", "The measure itself is a set of questions, adapted from "
                  "Rafferty and Griffin, in which a person describes their own "
                  "leader or manager; in the chapter there are three for each "
                  "dimension. So the score is the report of the followers, not "
                  "the leader&rsquo;s own account. The authors note in a footnote "
                  "that their analysis confirmed that the questions are good "
                  "measures of the construct, and send the reader to Chapter 13 "
                  "and to Appendix C. The wording is the book's and is not "
                  "reproduced here; the lab uses two items of its own for each "
                  "dimension."),
            ("p", "The findings come in three parts. The first is a gradient. "
                  "High-performing teams reported leaders with the strongest "
                  "behaviors on all five dimensions, low-performing teams the "
                  "lowest, and the differences were statistically significant. "
                  "Teams whose leadership ratings fell in the bottom third had half the chance of being high performers. The second is "
                  "a link to loyalty: transformational leadership was highly "
                  "correlated with the employee Net Promoter Score of the last "
                  "lessons. The third is a limit on what the authors could show: "
                  "leadership and culture were never measured in one year of their research, so on culture they lean on other studies."),
            ("p", "Then comes the claim that gives the lesson its quotation. "
                  "The authors looked at teams with the top 10 percent of reported "
                  "transformational leadership. One might expect them to be better "
                  "than average. They were no more likely, and possibly less, to be high performers than teams in the survey as a whole. The authors&rsquo; reading is that a leader cannot reach goals alone: teams must do the work, on a fitting architecture, with sound technical practices and Lean principles. They report "
                  "that leadership predicts the Lean product development "
                  "capabilities and the technical practices, and that its "
                  "influence, positive or negative, flows through them to delivery "
                  "and organizational performance. "
                  "Leadership, they write, amplifies the practices studied over "
                  "the years; it is not a separate set of practices."),
            ("p", "Now score a leader. The lab takes one invented leader rated by "
                  "six invented reports on a 7-point scale, with two invented "
                  "items for each of the five dimensions, ten in all. In the "
                  "preset <code>ratings</code> the first report gives the vision "
                  "items 6 and 6 and the personal recognition items 3 and 3. "
                  "Over the six reports, the vision answers add to 73 over 12, a "
                  "mean of 6.083; communication 64 over 12, 5.333; stimulation "
                  "57 over 12, 4.75; support 67 over 12, 5.583; recognition 36 "
                  "over 12, 3. The lowest dimension is personal recognition."),
            ("p", "In <code>later</code> the same six reports answer a while "
                  "afterwards, and only the two recognition items have changed: "
                  "their answers now add to 49 over 12, a mean of 4.083. "
                  "Recognition is still the lowest, because stimulation is 4.75, "
                  "but it has moved most. These ratings are six people&rsquo;s "
                  "perceptions of one person, and the lab never grades a leader; "
                  "a low dimension is a question to take to the people who gave "
                  "the ratings, and a high mean is not evidence that the team will "
                  "perform."),
            ("h3", "Exercise"),
            ("ul", [
                "A second invented leader, rated by the same six reports on the "
                "same ten items. Each dimension&rsquo;s twelve answers add to: "
                "vision 66, communication 60, stimulation 48, support 63, "
                "recognition 51.",
            ]),
            ("p", "Divide each total by 12 to get the dimension means, name the "
                  "lowest and the highest, and find the gap between them. Say "
                  "what you would ask the six reports about the lowest, and what "
                  "you could not conclude from it."),
            ("p", "A leader rated well on all five is, on the chapter&rsquo;s "
                  "evidence, a help to the team and no guarantee of its results. "
                  "The next lesson, The Role of Managers, turns to those who hold "
                  "the budgets and the time."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "score",
            "preset": "ratings",
            "presets": [
                {"id": "ratings",
                 "label": "One invented leader, six reports, ten items in five dimensions",
                 "points": 7,
                 "items": LEADER_ITEMS,
                 "answers": LEADER_RATINGS,
                 "expect": {
                    "alkN": "6",
                    "alkConstructs": "vision 73/12 ≈ 6.083; communication 16/3 ≈ 5.333; stimulation 4.75; support 67/12 ≈ 5.583; recognition 3",
                    "alkLine": "vision: 6 above, 0 at, 0 below; communication: 6 above, 0 at, 0 below; stimulation: 5 above, 1 at, 0 below; support: 6 above, 0 at, 0 below; recognition: 0 above, 0 at, 6 below",
                 }},
                {"id": "later",
                 "label": "The same reports later: only the recognition answers differ",
                 "points": 7,
                 "items": LEADER_ITEMS,
                 "answers": LEADER_LATER,
                 "expect": {
                    "alkN": "6",
                    "alkConstructs": "vision 73/12 ≈ 6.083; communication 16/3 ≈ 5.333; stimulation 4.75; support 67/12 ≈ 5.583; recognition 49/12 ≈ 4.083",
                    "alkLine": "vision: 6 above, 0 at, 0 below; communication: 6 above, 0 at, 0 below; stimulation: 5 above, 1 at, 0 below; support: 6 above, 0 at, 0 below; recognition: 3 above, 2 at, 1 below",
                 }},
            ],
            "panel_title": "A leader's five dimension means",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Scoring a leader on five dimensions",
        "steps_intro": "Four steps, the last of them on ratings of your own.",
        "steps": [
            ("Assign every item to a dimension",
             "Write down which items belong to vision, communication, stimulation, "
             "support and recognition. Each item belongs to one dimension."),
            ("Add the answers for each dimension",
             "For each dimension add every report&rsquo;s answers to its items. "
             "The count of answers is the number of reports times the number of "
             "items."),
            ("Divide to get each mean, and compare",
             "Divide each total by the count of answers. Name the lowest and the "
             "highest, and the gap between them on the 7-point scale."),
            ("Ask about the lowest",
             "Take your own ratings, or a made-up set, enter them in the lab and "
             "write down one question for the reports about the lowest dimension. "
             "Leave the number out of any judgement of the leader."),
        ],
        "worked": {
            "title": "Five dimension means for one leader",
            "intro": [
                "Work the preset <code>ratings</code>. There are six reports and "
                "two items a dimension, so each dimension has twelve answers.",
            ],
            "lines": [
                "Vision: 12 + 13 + 10 + 13 + 11 + 14 = 73; 73/12 = 6.083",
                "Communication: 11 + 12 + 9 + 11 + 9 + 12 = 64; 64/12 = 5.333",
                "Stimulation: 9 + 10 + 8 + 11 + 9 + 10 = 57; 57/12 = 4.75",
                "Support: 11 + 11 + 12 + 10 + 12 + 11 = 67; 67/12 = 5.583",
                "Recognition: 6 + 5 + 7 + 7 + 4 + 7 = 36; 36/12 = 3",
            ],
            "after": [
                "The lowest is recognition at 3, and the highest vision at 6.083, "
                "a gap of 3.083. The lab prints each of these, and the same sums "
                "for each report.",
            ],
        },
        "quiz_title": "Dimensions, means and the chapter's limit on leaders",
        "quiz": [
            {"q": "For the exercise leader, which dimension has the lowest mean, "
                  "and what is it?",
             "a": ["Personal recognition, 4.25",
                   "Intellectual stimulation, 4.00",
                   "Intellectual stimulation, 48",
                   "Supportive leadership, 5.25"],
             "c": 1,
             "why": "Dividing each total by 12 gives vision 5.5, communication 5.0, "
                    "stimulation 4.0, support 5.25 and recognition 4.25. The "
                    "lowest is intellectual stimulation, 4.00. Personal recognition "
                    "is the second lowest. 48 is the total, not the mean."},
            {"q": "According to Chapter 11, how likely were teams whose reported "
                  "leadership was in the bottom third to be high performers?",
             "a": ["Twice as likely",
                   "Exactly as likely",
                   "Half as likely",
                   "One third as likely"],
             "c": 2,
             "why": "The chapter says teams whose leadership ratings fall in the bottom third have half the chance of being high performers. It reports the top 10 percent separately."},
            {"q": "What did the chapter find for teams with the top 10 percent of "
                  "reported transformational leadership?",
             "a": ["They were more than twice as likely to be high performers",
                   "They were always high performers",
                   "They could not be compared, because there were too few",
                   "They were no more likely, and possibly less likely, to be high performers than teams overall"],
             "c": 3,
             "why": "The authors report that the teams with the strongest leaders "
                    "were no more likely, and possibly less, to be high performers than teams in the survey as a whole, and conclude that leaders alone cannot achieve high outcomes."},
            {"q": "Which of these is NOT one of the five dimensions in the model "
                  "the authors used?",
             "a": ["Technical authority",
                   "Vision",
                   "Intellectual stimulation",
                   "Personal recognition"],
             "c": 0,
             "why": "The five are vision, inspirational communication, "
                    "intellectual stimulation, supportive leadership and personal "
                    "recognition. Technical authority is not among them."},
        ],
        "mistakes": [
            ("Concluding that the strongest leaders deliver the strongest teams",
             "The chapter reports the opposite for the top 10 percent: they were "
             "no more likely, and possibly less, to be high performers. Leaders enable the practices; the teams and their architecture deliver."),
            ("Equating leadership with a place on the organization chart",
             "The authors write that being a leader does not mean having people "
             "report to you; leadership is about inspiring and motivating those "
             "around you."),
            ("Treating the lowest dimension as a verdict on the leader",
             "On the lab&rsquo;s ratings recognition is lowest at 3, and "
             "that is six invented reports&rsquo; perception of one invented "
             "leader. It is a question to ask them, and the lab never grades a "
             "leader."),
        ],
        "standard": (
            "Finish when you can score a leader on five dimensions and say what the score leaves out.",
            "Given reports' answers by dimension, compute each dimension's mean "
            "by hand, name the lowest, and state the chapter's finding on what "
            "leaders can and cannot deliver alone."
        ),
        "note": (
            "The lab averages the ratings you enter. It cannot say whether the "
            "items form a sound scale, whether the six reports speak for the "
            "team, or whether the leader's behavior caused any result; the "
            "authors' findings rest on surveys of thousands, not six."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Chapter 11, The Role of Managers and Tips to Improve Culture and
    # Support Your Teams (PDF pp. 162-168): what managers are and can do
    # (pp. 162-163), the ways to invest in teams (pp. 163-164), the three
    # things correlated with delivery performance and culture (p. 165),
    # collaboration, the game-day box, learning, tools (pp. 165-168), the
    # close (p. 168). Appendix A (p. 259) lists organizational investment in
    # DevOps among the measures strongly correlated with culture.
    # Quote: PDF p. 163 of the operator's copy, 14 words, quotes.py OK.
    # Lesson total: 14 words.
    {
        "slug": "the-role-of-managers",
        "title": "The Role of Managers",
        "module": "Chapter 11 · Leaders and Managers",
        "one_line": "What the authors ask of the people who hold the budgets and the time, and what a ratio of two groups can and cannot show about it.",
        "summary": (
            "The last sections of Chapter 11 turn from leaders in general to "
            "managers: the people responsible for people, budgets and resources. "
            "Read what the authors say they can do, how they might invest in their "
            "teams and which three things they tie to delivery performance and "
            "culture; then compare the share of teams that met a goal among those "
            "with and without a learning budget, and see how a third factor can "
            "stand behind a ratio."
        ),
        "key": [
            "managers link strategy to the team's work",
            "make the team safe and remove obstacles",
            "invest in skills, with a budget and time",
            "collaboration, learning climate and tools",
            "a ratio of shares is not an effect",
            "split by a third factor before you believe it",
        ],
        "key_label": "The role of managers in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter&rsquo;s, the "
            "other two the lab&rsquo;s."
        ),
        "concepts": [
            ("Manager",
             "In the chapter's definition, someone with responsibility for people, "
             "and often for budgets and resources. In the best case a manager is "
             "also a leader and shows the transformational characteristics of the "
             "last lesson."),
            ("Times as likely",
             "The ratio of two groups&rsquo; shares. If 65 percent of one group "
             "and 35 percent of another meet a goal, the first is 65/35, about "
             "1.86 times as likely. The gap between the shares, 30 percentage "
             "points, is a different number, and so is the ratio of odds."),
            ("Confounder",
             "A third factor that is linked to both the group a team falls in and "
             "the outcome, and so can produce a ratio between the groups that "
             "disappears when the teams are compared within levels of the third "
             "factor."),
        ],
        "read_title": "The chapter's argument, then the ratio",
        "read_intro": (
            "Read The Role of Managers and the section after it, Tips to Improve "
            "Culture and Support Your Teams, in your own copy first. The lesson "
            "reads them as a list of what managers can do and one finding, then "
            "computes a ratio of shares on teams of its own."
        ),
        "body": [
            ("p", "&ldquo;Knowledge is power, and you should give power to those "
                  "who have the knowledge.&rdquo; The sentence closes the authors&rsquo; "
                  "list of what managers can do, in the section The Role of Managers "
                  "of Chapter 11, and it explains the whole list. Managers, in their definition, are the people answerable for staff and frequently for budgets and resources, and they have a part to play in tying the business&rsquo;s aims to what the team does. "
                  "In the best case a manager is also a leader."),
            ("p", "What can a manager do? The chapter says they can create a "
                  "working environment in which people feel safe, invest in "
                  "developing their people&rsquo;s capabilities and remove "
                  "obstacles to work. They can enable specific DevOps practices "
                  "and visibly invest in DevOps and in professional development; the authors report a high correlation between investment in DevOps and delivery performance. They can make deployments "
                  "less painful, as Chapter 9 argued; make performance metrics "
                  "visible and align them with the aims of the organization; and "
                  "delegate more authority to employees."),
            ("p", "The chapter makes the investment concrete. It suggests that "
                  "managers make existing resources available to everyone; "
                  "establish a training budget that people know about, with the "
                  "latitude to choose training and, if possible, time in the "
                  "working day to use it; encourage staff to attend a technical "
                  "conference at least once a year and to report back to the team; "
                  "set up internal hack days; encourage teams to hold &lsquo;yak "
                  "days&rsquo; to work on technical debt, which is rarely "
                  "prioritized; hold internal DevOps mini-conferences; and give staff protected time to experiment, for instance 20 percent time or a few days once a release is out. These are the authors&rsquo; "
                  "suggestions, drawn from what they have seen organizations do."),
            ("p", "The next section gathers tips for managers, team leads and "
                  "engaged practitioners around three things the authors tie closely to delivery performance and to a strong team culture: tools, a climate for learning, and collaboration across functions. For "
                  "collaboration they advise building trust with counterparts on "
                  "other teams over time, encouraging people to move between "
                  "departments, and rewarding work that makes collaboration easier. "
                  "A box describes disaster recovery exercises, or game days, "
                  "which Kripa Krishnan runs at Google: outages are simulated "
                  "according to a plan so that engineers who do not usually work "
                  "together learn to, before a real disaster. For learning they "
                  "advise a training budget, space for informal learning (they "
                  "note that 3M and Google set aside 15 and 20 percent of time), "
                  "making it safe to fail with blameless postmortems, and regular "
                  "occasions to share what has been learned. For tools they advise "
                  "letting practitioners choose their own where there is no good "
                  "reason not to, and making monitoring a priority."),
            ("p", "Two claims in these sections deserve their exact strength. "
                  "That teams choosing their tools matters is tied by the authors "
                  "to Chapters 5 and 10: tool choice was a predictor of continuous "
                  "delivery, and having the tools and resources to do the job "
                  "contributes to job satisfaction. The conference and hack-day "
                  "lists, however, are advice, with no figure from the survey "
                  "behind any one of them. The chapter ends by saying that "
                  "grassroots efforts matter and that transformations benefit from "
                  "engaged leaders who amplify the work of teams, so that "
                  "leadership development is an investment in teams, technology "
                  "and products."),
            ("p", "Now a number that sounds like a finding. The lab works on "
                  "forty invented teams. In the preset <code>budget</code> twenty "
                  "teams have a learning budget and thirteen of them met their "
                  "goal for the quarter, 65 percent; twenty do not, and seven met "
                  "it, 35 percent. The lab reports a ratio of 1.86, so teams with a "
                  "budget were 1.86 times as likely to meet the goal; a gap of 30 "
                  "percentage points; and an odds ratio, shown separately, of "
                  "3.45. The ratio of shares, 13/7, is the one that matches the "
                  "words &lsquo;times as likely&rsquo;."),
            ("p", "Now split the same forty teams by one more fact, whether the "
                  "team&rsquo;s manager also removes obstacles. In "
                  "<code>by-obstacles</code> the budget teams with obstacles "
                  "removed are 16, of which 12 met the goal; the budget teams "
                  "without are 4, of which 1 did; the teams with no budget and "
                  "obstacles removed are 4, of which 3 did; and those with neither "
                  "are 16, of which 4 did. Both groups with obstacles removed "
                  "met the goal at 75 percent, whether or not they had a budget, "
                  "and both without at 25 percent. Within each level of the third "
                  "factor the ratio is 1. The 1.86 came from the budget teams "
                  "being mostly the teams whose managers remove obstacles."),
            ("p", "That is a pattern that invented data can show; it is not a "
                  "claim about real teams, and the chapter does not say that "
                  "budgets are worthless. The authors argue from many years of "
                  "survey data and from a theory about how these things fit "
                  "together. The lesson&rsquo;s point is narrower: a ratio between "
                  "two groups tells you what happened to the teams in front of "
                  "you, and a third factor can stand behind it. The Science Behind the Book returns "
                  "to the question of when a relationship in data supports a "
                  "claim about cause."),
            ("h3", "Exercise"),
            ("ul", [
                "Thirty invented teams. Fifteen make their performance metrics "
                "visible and nine of them met their goal; fifteen do not and three "
                "met it: `Visible, 15, 9; Not-visible, 15, 3`.",
            ]),
            ("p", "Find each group&rsquo;s share, the ratio of the first to the "
                  "second and the gap in percentage points. Then find the odds "
                  "of meeting the goal in each group and their ratio, and say "
                  "why it is not the same as the first ratio. Type the rows in to "
                  "check."),
            ("p", "That ends Part I of the book&rsquo;s results for this "
                  "course: delivery, culture, work and people. The next course, "
                  "The Science Behind the Book, opens Part II and asks how the "
                  "authors knew any of it."),
        ],
        "lab": ("acckit", {
            "mode": "groups",
            "view": "likely",
            "preset": "budget",
            "presets": [
                {"id": "budget",
                 "label": "Forty invented teams: with and without a learning budget",
                 "rows": BUDGET, "first": "Budget", "second": "No-budget",
                 "expect": {
                    "agrShares": "Budget 13 of 20 = 65%; No-budget 7 of 20 = 35%",
                    "agrRatio": "≈ 1.86×",
                    "agrDiff": "+30 points",
                    "agrOdds": "≈ 3.45",
                 }},
                {"id": "by-obstacles",
                 "label": "The same forty, split by whether the manager removes obstacles",
                 "rows": BUDGET_SPLIT, "first": "Budget-cleared", "second": "No-budget-cleared",
                 "expect": {
                    "agrShares": "Budget-cleared 12 of 16 = 75%; Budget-not-cleared 1 of 4 = 25%; No-budget-cleared 3 of 4 = 75%; No-budget-not-cleared 4 of 16 = 25%",
                    "agrRatio": "1.00×",
                    "agrDiff": "0 points",
                    "agrOdds": "1.00",
                 }},
            ],
            "panel_title": "How many times as likely, and why that is not an effect",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Comparing two groups' shares",
        "steps_intro": "Four steps, the last of them on teams of your own.",
        "steps": [
            ("Count each group and its successes",
             "For each group write how many teams it has and how many met the "
             "goal. Decide before counting what &lsquo;met&rsquo; means."),
            ("Turn the counts into shares",
             "Divide the teams that met the goal by the group&rsquo;s size, as a "
             "percentage. Then divide one share by the other for the ratio, and "
             "subtract them for the gap in points."),
            ("Split by a third factor",
             "Pick one other fact that could be linked to both the grouping and "
             "the goal. Repeat the counts for each level of it and compare the "
             "ratios within the levels."),
            ("Do it on your own teams",
             "List a few teams you know, whether each has something a manager "
             "provides and whether it met a goal. Type the counts in, note the "
             "ratio, and write down one third factor you would split by."),
        ],
        "worked": {
            "title": "Times as likely, for forty invented teams",
            "intro": [
                "Work the preset <code>budget</code>: twenty teams with a budget, "
                "thirteen of which met the goal; twenty without, seven of which "
                "did.",
            ],
            "lines": [
                "With a budget: 13/20 = 65%",
                "Without: 7/20 = 35%",
                "Ratio: 65/35 = 13/7 = 1.86",
                "Gap: 65 - 35 = 30 percentage points",
                "Odds with: 13 to 7; odds without: 7 to 13; ratio (13/7)/(7/13) = 3.45",
            ],
            "after": [
                "Only the ratio of shares answers &lsquo;how many times as "
                "likely&rsquo;. In <code>by-obstacles</code> the four shares are "
                "75, 25, 75 and 25 percent, and each within-level ratio is 1.",
            ],
        },
        "quiz_title": "A ratio of shares, and the chapter's advice",
        "quiz": [
            {"q": "For the exercise, how many times as likely to meet the goal "
                  "were the teams whose metrics are visible?",
             "a": ["6",
                   "3",
                   "40",
                   "0.33"],
             "c": 1,
             "why": "Nine of 15 is 60 percent and three of 15 is 20 percent, so "
                    "the ratio is 3. 6 is the ratio of odds, 9/6 over 3/12. "
                    "40 is the gap in percentage points, and 0.33 is the ratio "
                    "the wrong way round."},
            {"q": "In <code>by-obstacles</code>, what is the ratio of budget teams "
                  "to no-budget teams within the teams whose managers remove "
                  "obstacles?",
             "a": ["1.86, as in the whole sample",
                   "3",
                   "1",
                   "0.25"],
             "c": 2,
             "why": "Twelve of 16 and three of 4 are both 75 percent, so the ratio "
                    "is 1. The 1.86 is the ratio over all forty, and it came "
                    "from the budget teams being mostly those with obstacles "
                    "removed."},
            {"q": "Under which three headings does Chapter 11 gather its tips for a strong team culture?",
             "a": ["Team size, a training budget and monitoring",
                   "Trust, a vision and a release schedule",
                   "Hack days, game days and conferences",
                   "Cross-functional collaboration, a climate for learning and tools"],
             "c": 3,
             "why": "The tips are grouped under collaboration across functions, a climate for learning and tools. Hack days, "
                    "game days and conferences are examples under them, and a "
                    "training budget belongs under learning."},
            {"q": "How does the chapter describe the relationship between "
                  "investment in DevOps and software delivery performance?",
             "a": ["The two are highly correlated",
                   "Investment in DevOps has been shown to cause higher delivery performance",
                   "Investment in DevOps has no relation to delivery performance, only to culture",
                   "Investment in DevOps predicts only burnout"],
             "c": 0,
             "why": "The authors report a high correlation. It is also one of the five factors that correlated most with burnout, and a culture correlate, so it is not unrelated to either, and the chapter "
                    "does not claim to have shown cause."},
        ],
        "mistakes": [
            ("Reading '1.86 times as likely' as the effect of the budget",
             "The ratio describes the forty teams in front of you. On the lab&rsquo;s "
             "split it falls to 1 within each level of a third factor, so a "
             "ratio between groups cannot be read as what the budget does."),
            ("Funding training and leaving no time to use it",
             "The chapter pairs the training budget with latitude to choose the "
             "training and with dedicated time during the day, and its other "
             "suggestions are about time as well: 20 percent time, days after a "
             "release, hack days."),
            ("Confusing the ratio of shares with the gap or the ratio of odds",
             "On the lab&rsquo;s first preset the ratio is 1.86, the gap 30 "
             "percentage points and the odds ratio 3.45. Only the first is "
             "&lsquo;times as likely&rsquo;."),
        ],
        "standard": (
            "Finish when you can compare two groups' shares and say what a third factor could do.",
            "Given counts for two groups, compute shares, the ratio and the gap "
            "by hand, then split by a third factor and say whether the ratio "
            "survives."
        ),
        "note": (
            "The lab compares the counts you give it. It cannot say which "
            "third factor matters, whether the teams are alike in other ways, "
            "or whether any practice caused any result; the authors argue those "
            "from many years of survey data, and The Science Behind the Book reads how."
        ),
    },
]
