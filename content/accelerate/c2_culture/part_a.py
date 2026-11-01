"""Measuring and Changing Culture, lessons 1-4 -- Chapter 3.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 3, Measuring and Changing
Culture (Modeling and Measuring Culture, Measuring Culture, What Does Westrum
Organizational Culture Predict?, Consequences of Westrum's Theory for
Technology Organizations, How Do We Change Culture?). Pages in the comments
are PDF pages of the operator's copy; the lessons cite by chapter and section.
Every quotation is copied from that copy and checked with quotes.py. The
respondents, items, teams and scores are written for these lessons: none of the
book's survey items, tables, figures or data is reproduced. The design is
docs/accelerate/PLAN.md, section C, Course 2.
"""

_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)

# ---------------------------------------------------------------- 01 data

# Seven respondents (invented) answer six aspects on the 1-7 scale.
ASPECTS = (
    "cooperation, westrum, no; messengers, westrum, no; "
    "responsibility, westrum, no; bridging, westrum, no; "
    "failure, westrum, no; novelty, westrum, no"
)
MIXED_TEAM = (
    "r1, 6, 5, 6, 6, 5, 6; r2, 5, 4, 5, 5, 4, 5; r3, 3, 2, 3, 4, 2, 3; "
    "r4, 6, 6, 5, 6, 6, 5; r5, 4, 3, 4, 4, 3, 4; r6, 2, 2, 3, 2, 2, 3; "
    "r7, 5, 5, 4, 5, 5, 4"
)
EVEN_TEAM = (
    "u1, 4, 4, 4, 4, 4, 5; u2, 4, 4, 4, 4, 5, 4; u3, 4, 4, 4, 5, 4, 4; "
    "u4, 4, 4, 5, 4, 4, 4; u5, 4, 5, 4, 4, 4, 4; u6, 5, 4, 4, 4, 4, 5; "
    "u7, 4, 5, 4, 4, 4, 5"
)
CUTS = "3 5"

# 01 exercise: a platform team of five.
PLATFORM_TEAM = (
    "e1, 2, 3, 2, 3, 2, 2; e2, 4, 4, 5, 4, 4, 5; e3, 7, 6, 6, 7, 6, 6; "
    "e4, 3, 3, 4, 3, 3, 3; e5, 5, 5, 5, 5, 5, 4"
)

# ---------------------------------------------------------------- 02 data

# Four items, one worded negatively, six respondents (all invented).
FOUR_ITEMS_REVERSED = (
    "news, flow, no; ask, flow, no; share, flow, no; blame, flow, yes"
)
FOUR_ITEMS_FORGOTTEN = (
    "news, flow, no; ask, flow, no; share, flow, no; blame, flow, no"
)
FLOW_ANSWERS = (
    "r1, 6, 6, 5, 2; r2, 5, 4, 6, 3; r3, 3, 4, 3, 6; r4, 7, 6, 6, 1; "
    "r5, 5, 5, 6, 2; r6, 2, 3, 2, 7"
)

# 02 exercise: three more respondents on the same four items.
FLOW_EXERCISE = "q1, 7, 6, 7, 1; q2, 4, 4, 4, 4; q3, 2, 3, 2, 6"

# ---------------------------------------------------------------- 03 data

# Eight teams: a culture score (mean of 1-7 answers) and a delivery score
# (invented: the mean of three answers coded 1-7, higher is better).
EIGHT_TEAMS = (
    "a, 2.5, 2.0; b, 3.0, 3.0; c, 3.5, 2.5; d, 4.0, 4.0; "
    "e, 4.5, 3.5; f, 5.0, 5.0; g, 5.5, 4.5; h, 6.0, 6.0"
)
EIGHT_TEAMS_MOVED = (
    "a, 2.5, 2.0; b, 3.0, 3.0; c, 3.5, 2.5; d, 4.0, 4.0; "
    "e, 4.5, 3.5; f, 5.0, 5.0; g, 5.5, 4.5; h, 6.0, 2.0"
)

# 03 exercise: five teams.
FIVE_TEAMS = "v, 3.0, 3.0; w, 4.0, 2.0; x, 5.0, 4.0; y, 6.0, 5.0; z, 7.0, 6.0"

# ---------------------------------------------------------------- 04 data

# A team of six surveyed twice, six months apart (invented); the same six
# people answer both times and are matched by label.
BEFORE_TEAM = (
    "s1, 3, 3, 3, 3, 2, 3; s2, 4, 4, 4, 5, 4, 4; s3, 2, 2, 3, 2, 2, 2; "
    "s4, 5, 5, 5, 4, 5, 5; s5, 4, 3, 4, 4, 3, 4; s6, 3, 4, 3, 3, 4, 3"
)
AFTER_TEAM = (
    "s1, 4, 5, 4, 5, 4, 4; s2, 5, 5, 5, 5, 4, 5; s3, 3, 3, 3, 3, 2, 3; "
    "s4, 5, 4, 5, 5, 5, 4; s5, 5, 5, 5, 5, 5, 4; s6, 3, 4, 3, 3, 4, 3"
)
# A second team that adopted nothing new, surveyed at the same two times.
CONTROL_BEFORE = BEFORE_TEAM
CONTROL_AFTER = (
    "s1, 3, 3, 3, 3, 2, 3; s2, 4, 4, 5, 4, 4, 5; s3, 2, 3, 3, 2, 2, 3; "
    "s4, 5, 5, 5, 4, 5, 5; s5, 4, 4, 4, 4, 3, 4; s6, 3, 4, 3, 4, 4, 3"
)

# 04 exercise: three people.
EX_BEFORE = "x1, 3, 3, 4, 3, 3, 4; x2, 5, 5, 4, 5, 5, 5; x3, 2, 2, 2, 3, 2, 2"
EX_AFTER = "x1, 3, 4, 4, 4, 4, 4; x2, 5, 6, 5, 6, 5, 6; x3, 2, 2, 2, 2, 2, 2"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 3 opening (PDF p. 63 of the operator's copy); Modeling and
    # Measuring Culture (pp. 63-66): Schein's three levels (p. 64), Westrum's
    # typology (pp. 64-65), good information (p. 65), Table 3.1 (p. 66, in
    # prose only); the remarks on bureaucracy (pp. 69-70).
    # Quote: PDF p. 65 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words.
    {
        "slug": "modeling-culture",
        "title": "Modeling and Measuring Culture",
        "module": "Chapter 3 · Measuring and Changing Culture",
        "one_line": "Culture is a word with many definitions; the authors chose Westrum's three types, which sit on a scale and so can be measured.",
        "summary": (
            "Chapter 3 begins by choosing a model of culture. Read the three "
            "levels the authors distinguish, why they work at the level of "
            "values, and Westrum's pathological, bureaucratic and generative "
            "types with the information flow behind them; then score seven "
            "respondents on six aspects and see where a team falls among "
            "stated cut-points."
        ),
        "key": [
            "three levels: assumptions, values, artifacts",
            "this chapter works at the level of values",
            "pathological, bureaucratic, generative",
            "culture shapes how information flows",
            "the types sit on a scale, not in boxes",
            "a team's mean can hide its spread",
        ],
        "key_label": "Modeling culture in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Westrum's typology",
             "Ron Westrum's three kinds of organization, set out in 1988 from "
             "his work on safety in fields such as aviation and healthcare: "
             "pathological, which is power-oriented, bureaucratic, which is "
             "rule-oriented, and generative, which is performance-oriented. "
             "They differ in how cooperative people are and in what happens to "
             "messengers, responsibilities, bridging between groups, failure "
             "and new ideas."),
            ("Information flow",
             "How well what people know reaches the people who need it. "
             "Westrum counts information as good when it answers the "
             "receiver's questions, arrives in time and is presented so that "
             "the receiver can use it. The chapter's claim is that culture "
             "predicts this flow."),
            ("Respondent mean and band",
             "One person's answers on the six aspects, averaged on the 1 to 7 "
             "scale, and the name of the type nearest that mean under two "
             "cut-points. The book gives no cut-points; the lab's are the "
             "lesson's own, stated where they are used."),
        ],
        "read_title": "The chapter's choice of a model, then the count",
        "read_intro": (
            "Read the opening of Chapter 3 and its first section, Modeling and "
            "Measuring Culture, in your own copy first. The lesson reads how the "
            "authors chose a model and what it says, then scores a small team on "
            "it."
        ),
        "body": [
            ("p", "&ldquo;Westrum&rsquo;s further insight was that the "
                  "organizational culture predicts the way information flows "
                  "through an organization.&rdquo; The sentence comes from Modeling "
                  "and Measuring Culture, the first section of Chapter 3, and "
                  "it explains why a chapter in a book about software delivery "
                  "borrows a typology from the study of accidents. The authors "
                  "say what they needed: a model of culture that is defined well "
                  "in the scientific literature, can be measured, and has "
                  "predictive power in their field. This lesson reads how they "
                  "chose one."),
            ("p", "They begin by admitting that there are many ways to model "
                  "culture: by nation, by the values an organization enacts, and "
                  "more. Within organizational culture they follow Edgar Schein "
                  "(1985), who describes three levels. The first is basic "
                  "assumptions, formed over time as a group makes sense of what "
                  "happens to it; they are the least visible, the things a team "
                  "just knows and finds hard to put into words. The second is "
                  "values and norms, which a group can discuss and even argue "
                  "over, and which shape how members act. The third is "
                  "artifacts, the most visible level: mission statements, "
                  "procedures, technology, heroes and rituals. The authors work "
                  "at the second level, the one people usually mean when they "
                  "talk about the culture of a team."),
            ("p", "The model they chose is Ron Westrum&rsquo;s, a sociologist who "
                  "studied human factors in safety in fields where accidents are "
                  "costly. His typology of 1988 has three types. A pathological "
                  "organization is power-oriented, and marked by fear and threat; "
                  "people hoard information or bend it to look better. A "
                  "bureaucratic organization is rule-oriented and protects its "
                  "departments, each keeping to its own rules and turf. A "
                  "generative organization is performance-oriented and keeps its "
                  "eye on the mission, so that everything is subordinated to doing "
                  "what the organization is there to do."),
            ("p", "Westrum&rsquo;s point is about information. He names three "
                  "marks of good information: it answers the questions the "
                  "receiver has, it is timely, and it is presented so the "
                  "receiver can use it. Good flow matters most where work is fast "
                  "and mistakes are expensive, and technology organizations are "
                  "among those. Chapter 3 then lays out, in its Table 3.1, how the "
                  "three types differ on six aspects: cooperation, how "
                  "messengers are treated, responsibilities, bridging between "
                  "groups, how failure is handled, and how novelty is received. "
                  "The table is the book&rsquo;s; the lesson only names the "
                  "aspects. Read down failure and you see the sharpest contrast, "
                  "from blaming someone, through judging them by the rules, to "
                  "asking what happened."),
            ("p", "The authors are careful not to turn the bureaucratic type into "
                  "a villain. They quote Mark Schwartz, who argues that the "
                  "purpose of bureaucracy is fairness: the same rules for every "
                  "case, built from the accumulated knowledge of experts. "
                  "Westrum&rsquo;s bureaucratic culture is best read, they say, "
                  "as one where following the rules counts for more than "
                  "achieving the mission. They add that they have worked with "
                  "United States federal government teams they would call "
                  "generative and with startups that are plainly pathological, so "
                  "the type is not a matter of an organization&rsquo;s size, age "
                  "or sector."),
            ("p", "Now the count. The lab takes six aspects, a scale of 1 to 7, "
                  "and each respondent&rsquo;s six answers, written respondent "
                  "then answers. It finds each respondent&rsquo;s mean, the "
                  "team&rsquo;s mean, and a band for each. The lesson states two "
                  "cut-points of its own, 3 and 5: below 3 is nearest the "
                  "pathological type, 3 up to 5 the bureaucratic, 5 and above the "
                  "generative. They are an assumption, because the chapter "
                  "gives none and treats the types as points on a continuum. The "
                  "sample is invented: seven people on one team. On the preset "
                  "<code>mixed</code> the respondent means are 5.667, 4.667, "
                  "2.833, 5.667, 3.667, 2.333 and 4.667; two people fall in the "
                  "pathological band, three in the bureaucratic and two in the "
                  "generative. The team mean is 177 over 42, which is 4.214, "
                  "and the team falls in the bureaucratic band."),
            ("p", "The preset <code>even</code> is a second team of seven with "
                  "the same team mean, 4.214, and a different shape: everyone "
                  "answers 4 or 5 on every aspect, so every respondent mean lies "
                  "between 4.167 and 4.333 and all seven sit in the bureaucratic "
                  "band. The two teams get the same team figure, and their lives "
                  "inside the team are not the same. The first has two people "
                  "who answer as if it were a fearful place and two who answer "
                  "as if it were a good one; a single mean cannot tell you that, "
                  "and it is a reason to look at the answers person by person "
                  "before acting on a team figure."),
            ("p", "The lab shows how a score is made and nothing more. The "
                  "Martin Fowler&rsquo;s foreword adds a caution that "
                  "applies here: these are surveys of subjective perceptions, "
                  "and a sample can differ from the industry it is taken from. "
                  "The chapter also reports, in a footnote, that in 2016 31 "
                  "percent of respondents were classified as pathological, 48 "
                  "percent as bureaucratic and 21 percent as generative; it does "
                  "not say in that chapter where the dividing lines were drawn, "
                  "which is why the lab states its own."),
            ("h3", "Exercise"),
            ("ul", [
                "Aspects, in order: `cooperation`, `messengers`, `responsibility`, "
                "`bridging`, `failure`, `novelty`. Scale 1 to 7; cut-points 3 and 5.",
                "A platform team of five: `e1, 2, 3, 2, 3, 2, 2; e2, 4, 4, 5, 4, 4, "
                "5; e3, 7, 6, 6, 7, 6, 6; e4, 3, 3, 4, 3, 3, 3; e5, 5, 5, 5, 5, 5, "
                "4`.",
            ]),
            ("p", "Work out each person&rsquo;s mean by hand and place each in a "
                  "band, then the team&rsquo;s mean and band. Say how many "
                  "people sit in each band and whether the team figure describes "
                  "any one of them. Then type the records into the lab to check "
                  "your count."),
            ("p", "Averaging is only the first step; the next lesson, Measuring "
                  "Culture, reads how the chapter turns the types into survey "
                  "statements and what has to be true of the answers before the "
                  "score means anything."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "westrum",
            "preset": "mixed",
            "presets": [
                {"id": "mixed",
                 "label": "Seven people: two near pathological, two near generative",
                 "points": 7,
                 "items": ASPECTS,
                 "answers": MIXED_TEAM,
                 "cuts": CUTS,
                 "expect": {"alkN": "7", "alkTeam": "59/14 ≈ 4.214, bureaucratic", "alkBands": "pathological 2, bureaucratic 3, generative 2"}},
                {"id": "even",
                 "label": "Seven people with the same team mean, all in the middle",
                 "points": 7,
                 "items": ASPECTS,
                 "answers": EVEN_TEAM,
                 "cuts": CUTS,
                 "expect": {"alkN": "7", "alkTeam": "59/14 ≈ 4.214, bureaucratic", "alkBands": "pathological 0, bureaucratic 7, generative 0"}},
            ],
            "panel_title": "A team on Westrum's scale",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Placing a team on the scale",
        "steps_intro": "Four steps, the last of them on a team of your own.",
        "steps": [
            ("Fix the scale and the cut-points first",
             "Write down the scale (1 to 7) and your two cut-points before you "
             "look at any answers, so that the bands are not drawn to suit the "
             "results."),
            ("Average each person's answers",
             "Add one respondent's six answers and divide by six. Do this for "
             "everyone before you look at the team."),
            ("Band each person, then the team",
             "Compare each mean with the cut-points, and the team mean with "
             "them. Count the people in each band."),
            ("Try it on a team you know",
             "Ask five people you work with to rate the six aspects from 1 to 7 "
             "without names, type the answers into the lab, and write down "
             "whether the team mean describes any one of them."),
        ],
        "worked": {
            "title": "One respondent and the team, on the preset mixed",
            "intro": [
                "Take respondent <code>r1</code>, who answered 6, 5, 6, 6, 5, 6, "
                "then the whole team.",
            ],
            "lines": [
                "r1 total 6 + 5 + 6 + 6 + 5 + 6 = 34",
                "r1 mean 34 / 6 = 5.667, which is 5 or above: generative band",
                "r3 total 17, mean 17 / 6 = 2.833: below 3, pathological band",
                "all seven totals: 34, 28, 17, 34, 22, 14, 28",
                "team total 177, answers 7 x 6 = 42",
                "team mean 177 / 42 = 4.214: bureaucratic band",
            ],
            "after": [
                "The team mean is the mean of the respondent means, because "
                "every respondent answered the same six items. No single "
                "respondent is at 4.214.",
            ],
        },
        "quiz_title": "Levels, types and the count",
        "quiz": [
            {"q": "In the exercise, with cut-points 3 and 5 as the lesson states "
                  "them (below 3 pathological, 3 up to 5 bureaucratic, 5 and "
                  "above generative), how many of the five people sit in the "
                  "pathological, bureaucratic and generative bands, in that "
                  "order?",
             "a": ["1, 3 and 1",
                   "1, 2 and 2",
                   "2, 2 and 1",
                   "1, 4 and 0"],
             "c": 0,
             "why": "The means are e1 2.333, e2 4.333, e3 6.333, e4 3.167 and e5 "
                    "4.833. Only e1 is below 3 and only e3 is 5 or above. e5 is "
                    "4.833, which is under the cut-point, so it is bureaucratic, "
                    "not generative; e4 is 3.167, above the lower cut-point, so "
                    "it is bureaucratic, not pathological. That leaves e2, e4 "
                    "and e5 in the middle band. The team mean is 126 over 30, "
                    "which is 4.2, also bureaucratic, and it describes none of "
                    "the five."},
            {"q": "Which of Schein's three levels of organizational culture do "
                  "the authors say they work at in Chapter 3?",
             "a": ["Values, the second level",
                   "Basic assumptions, the first level",
                   "Artifacts, the third level",
                   "National culture, which is not one of the three levels"],
             "c": 0,
             "why": "Chapter 3 names basic assumptions, values and artifacts, and "
                    "says it chose a model with the second level, values, in "
                    "mind. National culture is mentioned as one way to model "
                    "culture in general, and is not one of Schein's levels or "
                    "the chapter's choice."},
            {"q": "On the preset <code>mixed</code>, what is the team mean to three "
                  "decimal places?",
             "a": ["4.214",
                   "4.667",
                   "4.000",
                   "3.667"],
             "c": 0,
             "why": "The team mean is the total of all 42 answers, 177, divided "
                    "by 42, which is 4.214. 4.667 is the median of the seven "
                    "respondent means; 4.000 is the middle of the 1 to 7 scale, "
                    "which is not computed from the answers at all; 3.667 is "
                    "one respondent&rsquo;s mean."},
            {"q": "What do the authors say about the bureaucratic type?",
             "a": ["It is not necessarily bad: bureaucracy aims at fairness, and "
                   "the type is one where following the rules matters more than "
                   "the mission",
                   "It is the worst of the three, because rules replace thought",
                   "It cannot occur in a team whose members cooperate",
                   "It is found only in large, old organizations"],
             "c": 0,
             "why": "The authors quote Mark Schwartz on bureaucracy as a "
                    "fairness mechanism and say that Westrum&rsquo;s "
                    "rule-oriented type is best read as rules mattering more "
                    "than the mission. They say too that they have seen "
                    "generative federal teams and pathological startups, so "
                    "neither size nor age settles the type."},
        ],
        "mistakes": [
            ("Treating Westrum's types as three boxes a team falls into",
             "The authors use the types as points on a scale, a continuum, which "
             "is what makes them measurable with a scale of 1 to 7. A team "
             "mean of 4.2 is a position between the poles. The lab's bands are "
             "a convenience with cut-points the lesson chose, and a person "
             "whose mean is 4.9 and one whose mean is 5.1 are not in different "
             "worlds."),
            ("Reading “bureaucratic” as an insult",
             "The authors take care to say bureaucracy is not necessarily bad. "
             "Its goal, in the words they quote, is to treat every case alike "
             "and to keep the best rules the organization has learned. The "
             "type describes where the rules rank against the mission, and the "
             "chapter says a team of any kind of organization can land "
             "anywhere on the scale."),
            ("Taking the team mean as a description of the people in the team",
             "A mean of 4.214 comes from seven people whose own means run from "
             "2.333 to 5.667, and it comes equally from seven people who all sit "
             "near 4.2. The mean says nothing about the spread. Look at the "
             "answers person by person before acting on a team figure."),
        ],
        "standard": (
            "Finish when you can place a team and its people on the scale.",
            "Given respondents' answers on six aspects and two cut-points, find "
            "each respondent's mean, band each, find and band the team mean, and "
            "say what the team mean hides."
        ),
        "note": (
            "The lab averages the answers you type and compares the means with "
            "cut-points you state. It cannot tell whether six aspects capture a "
            "culture, whether seven people represent a team, or whether the "
            "people answered candidly; the survey measures perceptions, and "
            "whether the construct is valid and reliable is the next lesson&rsquo;s "
            "question."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Measuring Culture (PDF pp. 66-70 of the operator's copy): the types as
    # points on a scale (p. 66), Likert-type questions and the 1-7 values
    # (pp. 66-67), the statements (p. 67, Figure 3.1 not reproduced),
    # constructs, discriminant and convergent validity and reliability (pp.
    # 67-69), the score as a mean (p. 69), footnote 1 (p. 75).
    # Quote: PDF p. 67 of the operator's copy, 19 words, quotes.py OK.
    # Lesson total: 19 words.
    {
        "slug": "likert-type-questions",
        "title": "Measuring Culture",
        "module": "Chapter 3 · Measuring and Changing Culture",
        "one_line": "Culture becomes a number when people answer several statements from strongly disagree to strongly agree and the answers are averaged.",
        "summary": (
            "Chapter 3 turns Westrum's types into a measure. Read why a scale "
            "suits them, how Likert-type answers are valued from 1 to 7, what "
            "makes a set of statements a construct, and how a response is scored; "
            "then reverse a negatively worded item, average four items for six "
            "respondents, and see what the score becomes if the reversal is "
            "forgotten."
        ),
        "key": [
            "a Likert-type answer is a number from 1 to 7",
            "several statements, not one",
            "a construct must be valid and reliable",
            "the score is the mean of the answers",
            "reverse a negative item first",
            "a score measures perception",
        ],
        "key_label": "Measuring culture in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Likert-type question",
             "A statement that a respondent rates by how strongly they agree "
             "with it, from strongly disagree to strongly agree. The authors "
             "give the answers the values 1 to 7, and the chapter says the "
             "statement must be worded strongly enough that people can "
             "strongly agree or disagree with it."),
            ("Construct",
             "A measure built from several survey statements that have been "
             "shown to be understood alike by the people answering and to "
             "measure the one thing together. The chapter's construct is "
             "Westrum organizational culture, and a response&rsquo;s score on it "
             "is the mean of its answers."),
            ("Reverse-coded item",
             "A statement worded so that agreeing means the opposite of what the "
             "construct measures. Before averaging, its answer is replaced by "
             "the scale&rsquo;s top plus 1, minus the answer: on a scale of 7, "
             "8 minus the answer. The lab shows the score both ways."),
        ],
        "read_title": "How the chapter measures culture, then the count",
        "read_intro": (
            "Read the section Measuring Culture, and the paragraphs on "
            "constructs that run into the next section, in your own copy first. "
            "The lesson reads how the measure is built and then scores a small "
            "sample, one item reversed."
        ),
        "body": [
            ("p", "&ldquo;For this approach to work, the statement must be worded "
                  "strongly, so that people can strongly agree or disagree&rdquo; "
                  "is how the authors begin the practical part of Measuring "
                  "Culture, the second section of Chapter 3. Before it they make "
                  "the step that matters: Westrum&rsquo;s types form points on a "
                  "scale, a continuum, and that makes them a good candidate for "
                  "Likert-type questions. The lesson reads the section and the "
                  "paragraphs that follow it, up to the point where the chapter "
                  "turns to what the score predicts."),
            ("p", "The Likert scale comes from psychometrics, the measurement of "
                  "people&rsquo;s perceptions: a respondent rates a statement by "
                  "how far they agree with it. The authors give the answers "
                  "values running from 1, for the strongest disagreement, to 7, "
                  "for the strongest agreement; Chapter 12, later in the book, gives neutral as 4. The "
                  "chapter's Figure 3.1 re-creates the statements they wrote from "
                  "Westrum&rsquo;s model. The lesson does not reproduce them; "
                  "they are best read in the book, and the lab's four items are "
                  "the lesson&rsquo;s own."),
            ("p", "Asking is the easy half. The chapter says that once you have "
                  "responses from several people, often dozens or hundreds, you "
                  "must show that the measure is valid and reliable. That means "
                  "finding out whether the statements are understood alike by "
                  "everyone and whether, taken together, they measure "
                  "organizational culture. If several statistical tests confirm "
                  "both, what has been measured is called a construct, here "
                  "&ldquo;Westrum organizational culture&rdquo;, and may be used "
                  "in further research. The chapter names three families of test: "
                  "discriminant validity, that items which should be unrelated "
                  "are; convergent validity, that items which should be related "
                  "are; and reliability, also called internal consistency, that "
                  "the items are read and interpreted alike. They come before any "
                  "test of correlation or prediction. Chapter 13 and Appendix C "
                  "take them up, and this course leaves them there."),
            ("p", "The authors report that their Westrum construct has "
                  "consistently been found valid and reliable, so, they say, you "
                  "can use the questions in your own surveys. To get the score for "
                  "a response, take the number from 1 to 7 for each answer and "
                  "calculate the mean across all the questions. After that, the "
                  "scores of all the responses can go into the further analysis."),
            ("p", "The reason for several statements is the lesson&rsquo;s gloss "
                  "on the chapter, not its wording. One answer carries a "
                  "person&rsquo;s mood that day and how they read one sentence; "
                  "a mean of several lets one stray answer weigh less. The chapter "
                  "does say that the questions must hang together, which is what "
                  "reliability tests."),
            ("p", "Now the count. The chapter does not discuss reversing, and the "
                  "lesson adds it because any survey that mixes statement "
                  "directions has to deal with it. The lab takes a scale of 7, "
                  "four items in one construct called <code>flow</code> and six "
                  "respondents; the item <code>blame</code> is worded so that "
                  "agreeing is bad news, and is marked reversed. On the preset "
                  "<code>reversed</code> the respondent scores are 5.75, 5.0, "
                  "3.0, 6.5, 5.5 and 2.0, the item means are 4.667, 4.667, 4.667 "
                  "and, after reversing, 4.5 for <code>blame</code>, and the "
                  "construct mean over the six is 4.625. With the line at 4, the "
                  "midpoint, four respondents sit above and two below."),
            ("p", "The preset <code>forgotten</code> uses the same answers and "
                  "leaves <code>blame</code> unreversed, as an analyst who "
                  "missed the wording would. The respondent scores become 4.75, "
                  "4.5, 4.0, 5.0, 4.5 and 3.5, and the construct mean 4.375. "
                  "Respondent <code>r6</code>, who strongly agreed that blame is "
                  "common, moves from 2.0 to 3.5; <code>r4</code>, who strongly "
                  "disagreed, drops from 6.5 to 5.0. Everyone is pulled toward "
                  "the middle, because the one wrongly coded item points the "
                  "other way from the three correct ones. An answer of 4 is "
                  "unchanged by reversing, which is why a neutral person never "
                  "shows the mistake."),
            ("p", "The same four items show why one statement is not enough. "
                  "Respondent <code>r3</code> answered 4 to <code>ask</code>, "
                  "which if it were the only item would put them exactly at the "
                  "neutral midpoint; the four items together give 3.0. "
                  "Fowler&rsquo;s foreword warns that surveys capture subjective "
                  "perceptions. A score is a summary of what people said they "
                  "perceive, with the chance of misreading that goes with any "
                  "summary."),
            ("h3", "Exercise"),
            ("ul", [
                "The same four items, `news`, `ask`, `share` and `blame`, with "
                "`blame` reversed, scale 7.",
                "Three respondents: `q1, 7, 6, 7, 1; q2, 4, 4, 4, 4; q3, 2, 3, 2, "
                "6`.",
            ]),
            ("p", "Score each respondent with `blame` reversed and then without. "
                  "Find which respondent&rsquo;s score changes the most when the "
                  "reversal is forgotten, and by how much, and explain why one "
                  "respondent&rsquo;s score does not change at all. Type the "
                  "records into the lab to check them."),
            ("p", "A score is only a measure. The next lesson, What Westrum "
                  "Culture Predicts, reads what the authors found when they set "
                  "this score beside delivery and organizational performance."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "score",
            "preset": "reversed",
            "presets": [
                {"id": "reversed",
                 "label": "Four items, blame reversed",
                 "points": 7,
                 "items": FOUR_ITEMS_REVERSED,
                 "answers": FLOW_ANSWERS,
                 "line": 4,
                 "expect": {"alkConstructs": "flow 4.625", "alkItems": "news 14/3 ≈ 4.667; ask 14/3 ≈ 4.667; share 14/3 ≈ 4.667; blame 4.5", "alkLine": "flow: 4 above, 0 at, 2 below", "alkReversed": "1: blame", "alkUnreversed": "flow 4.375"}},
                {"id": "forgotten",
                 "label": "The same answers, the reversal forgotten",
                 "points": 7,
                 "items": FOUR_ITEMS_FORGOTTEN,
                 "answers": FLOW_ANSWERS,
                 "line": 4,
                 "expect": {"alkConstructs": "flow 4.375", "alkItems": "news 14/3 ≈ 4.667; ask 14/3 ≈ 4.667; share 14/3 ≈ 4.667; blame 3.5", "alkLine": "flow: 4 above, 1 at, 1 below", "alkReversed": "0: none"}},
            ],
            "panel_title": "Scoring a construct",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Scoring a construct",
        "steps_intro": "Four steps, the last of them on answers of your own.",
        "steps": [
            ("Mark the reverse-worded items",
             "Read each statement and ask whether agreeing means more of the "
             "thing measured or less. Mark every item where it means less."),
            ("Reverse before you average",
             "For a marked item, replace the answer by 8 minus the answer on a "
             "scale of 7. Check that 1 and 7 swap and that 4 stays put."),
            ("Average per respondent, then per item",
             "A respondent&rsquo;s score is the mean of their reversed-and-"
             "unreversed answers. An item&rsquo;s mean is over respondents; the "
             "construct mean is over both."),
            ("Check it on your own survey",
             "Take a short survey you have run or could run, mark its "
             "negatively worded statements, and compute five people&rsquo;s "
             "scores with and without reversing."),
        ],
        "worked": {
            "title": "One respondent, with and without the reversal",
            "intro": [
                "Take respondent <code>r3</code> on the preset <code>reversed</code>, "
                "who answered 3, 4, 3 and 6, the last to <code>blame</code>.",
            ],
            "lines": [
                "blame is reversed: 8 - 6 = 2",
                "answers used: 3, 4, 3, 2",
                "total 12, mean 12 / 4 = 3.0",
                "forgotten: answers 3, 4, 3, 6, total 16, mean 16 / 4 = 4.0",
                "difference 16 - 12 = 4, and 4 / 4 = 1.0",
            ],
            "after": [
                "The correct score, 3.0, is below the line of 4 and the "
                "forgotten one sits exactly on it: the error moved this "
                "respondent from below the line to its edge.",
            ],
        },
        "quiz_title": "Scale, reversal and score",
        "quiz": [
            {"q": "In the exercise, whose score changes the most when the "
                  "reversal of <code>blame</code> is forgotten, and by how much?",
             "a": ["q1, by 1.5 points",
                   "q3, by 1.0 point",
                   "q2, by 1.5 points",
                   "All three change by the same amount"],
             "c": 0,
             "why": "q1 answered 1 to blame, which reverses to 7: the scores are "
                    "27 over 4, 6.75, and without reversing 21 over 4, 5.25, a "
                    "change of 1.5. q3 answered 6, which reverses to 2: 2.25 "
                    "against 3.25, a change of 1.0. q2 answered 4 on everything "
                    "and 4 reverses to 4, so q2's score is 4.0 either way. The "
                    "change is the distance between the answer and its reverse, "
                    "8 minus twice the answer, over 4."},
            {"q": "On a scale of 1 to 7, a respondent answers 2 to a reverse-coded "
                  "item. What number enters the mean?",
             "a": ["6",
                   "2",
                   "5",
                   "4"],
             "c": 0,
             "why": "Reversing swaps the ends of the scale: 1 and 7, 2 and 6, 3 "
                    "and 5, with 4 fixed, so the value is 8 minus 2, which is 6. "
                    "5 comes from subtracting from 7, which sends 1 to 6 and "
                    "leaves 7 unmatched; 2 is the answer left unreversed."},
            {"q": "According to Chapter 3, how is a response&rsquo;s score on the "
                  "Westrum construct calculated?",
             "a": ["The mean of the 1 to 7 values of its answers across all the "
                   "questions",
                   "The median of its answers across the questions",
                   "The lowest answer it gave to any question",
                   "The share of questions answered 5 or higher"],
             "c": 0,
             "why": "The chapter says to turn each answer into its number from 1 "
                    "to 7 and average those numbers over the whole set of "
                    "questions. The median, the lowest answer and the share "
                    "above a threshold are different summaries and the chapter "
                    "does not use them."},
            {"q": "On the preset <code>forgotten</code> the lab reports a construct "
                  "mean of 4.375. What is the construct mean on <code>reversed</code>?",
             "a": ["4.625",
                   "4.375",
                   "4.500",
                   "3.500"],
             "c": 0,
             "why": "The six scores with blame reversed are 5.75, 5.0, 3.0, 6.5, "
                    "5.5 and 2.0, which total 27.75, a mean of 4.625. Reversing "
                    "changes every answer to blame except a 4, and the six "
                    "answers are 2, 3, 6, 1, 2 and 7, so the total moves and the "
                    "mean cannot stay at 4.375. 3.5 is the unreversed mean of "
                    "the blame item alone."},
        ],
        "mistakes": [
            ("Averaging a negatively worded item without reversing it",
             "If agreeing with one statement means worse culture and agreeing "
             "with the other three means better, averaging the raw answers "
             "pulls everyone toward the middle and hides the people whose "
             "answers differ most. Reverse first, so that every item points the "
             "same way."),
            ("Treating one statement as the measure",
             "One answer reflects a person&rsquo;s reading of one sentence. The "
             "chapter builds a construct from several statements and requires "
             "evidence that they are understood alike and measure one thing "
             "together before the score is used."),
            ("Reading a score as a fact about the organization",
             "The score is a summary of what a handful of people said they "
             "perceive, on statements they might read differently. Martin Fowler "
             "warns in his foreword that the surveys capture perceptions, and "
             "asks how the sample reflects the industry. The score tells you "
             "what these answers say."),
        ],
        "standard": (
            "Finish when you can score a construct from raw answers.",
            "Given items, one marked reverse-coded, and respondents' answers on a "
            "scale of 7, reverse the marked item, find each respondent&rsquo;s "
            "score and the construct mean, and say what the mean would be if "
            "the reversal were forgotten."
        ),
        "note": (
            "The lab applies the reversal you declare and averages. It cannot "
            "tell you whether your statements are understood alike or measure "
            "one thing; that is what the validity and reliability tests of "
            "Chapter 13 and Appendix C are for, and four invented items prove "
            "nothing about any real survey."
        ),
    },
    # ---------------------------------------------------------------- 03
    # What Does Westrum Organizational Culture Predict? (PDF pp. 70-71 of the
    # operator's copy), Consequences of Westrum's Theory for Technology
    # Organizations (pp. 71-74), the delivery performance construct (p. 72),
    # Google's team study (p. 73), failures and accidents (pp. 73-74),
    # footnote 2 (p. 75).
    # Quote: PDF p. 73 of the operator's copy, 20 words, quotes.py OK; PDF p.
    # 73, 10 words, quotes.py OK.
    # Lesson total: 30 words.
    {
        "slug": "what-westrum-culture-predicts",
        "title": "What Westrum Culture Predicts",
        "module": "Chapter 3 · Measuring and Changing Culture",
        "one_line": "Teams with better information flow deliver and perform better, the authors found, and they read that as prediction, not proof of cause.",
        "summary": (
            "Chapter 3 tests its measure: does a team's culture score predict "
            "anything? Read what Westrum's theory says to expect, the three "
            "outcomes the authors hypothesized and found, the point about "
            "which delivery measures form a construct, Google's study of its "
            "teams and what an accident investigation should do; then compute a "
            "correlation between culture and delivery across eight invented "
            "teams."
        ),
        "key": [
            "better information flow, better function",
            "predicts delivery, results, satisfaction",
            "the delivery construct has three measures",
            "how a team interacts matters most",
            "human error starts an investigation",
            "a correlation is not a cause",
        ],
        "key_label": "What Westrum culture predicts in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Software delivery performance",
             "In Chapter 3, the construct made from lead time, release frequency "
             "and time to restore service. Change fail rate is left out because "
             "the four together did not pass all the tests of validity and "
             "reliability; it is strongly correlated with the construct, so "
             "what correlates with the construct usually correlates with it too."),
            ("Inferential predictive research",
             "Research that sets a hypothesis from earlier work and theory, and "
             "then tests whether the data show the predicted relationship. The "
             "authors' own footnote calls their culture hypotheses by this name "
             "and points ahead to Chapter 12."),
            ("Pearson's r",
             "A number from -1 to 1 for how closely two measures move on a "
             "straight line across the same cases. The lab also gives r squared, "
             "the share of the spread in one measure that the straight line "
             "through the points accounts for."),
        ],
        "read_title": "What the chapter predicts, how it tested it, then the count",
        "read_intro": (
            "Read What Does Westrum Organizational Culture Predict? and "
            "Consequences of Westrum's Theory for Technology Organizations in "
            "your own copy first. The lesson reads the prediction and the "
            "evidence offered, then computes a correlation on invented teams."
        ),
        "body": [
            ("p", "Google found, in the authors&rsquo; quotation of its research, that "
                  "&ldquo;who is on a team matters less than how the team members "
                  "interact, structure their work, and view their "
                  "contributions&rdquo;. The line comes in Consequences of "
                  "Westrum&rsquo;s Theory for Technology Organizations, near the "
                  "end of the part of Chapter 3 that asks what a culture score is "
                  "good for. This lesson reads that part and the section before "
                  "it, What Does Westrum Organizational Culture Predict?"),
            ("p", "Westrum&rsquo;s theory is that an organization whose "
                  "information flows better works better, and the authors "
                  "give three reasons a culture score should stand for more than "
                  "itself. It reflects trust and cooperation across the "
                  "organization. It can indicate better decisions, since better "
                  "information is available and a decision can be reversed more "
                  "easily in a team that is open and transparent. And teams with "
                  "these norms are likely to do better by their people, because "
                  "problems are found and fixed faster."),
            ("p", "From this they set three hypotheses: that a higher culture "
                  "score goes with better software delivery, with a better "
                  "performing organization and with more satisfied staff. The chapter says they proved true, and its Figure 3.2 shows the three paths. Their own "
                  "footnote adds that the hypotheses rest on earlier research and "
                  "theory, plus the authors&rsquo; experience, and that this is "
                  "inferential predictive research. The word predict is used "
                  "with that meaning: the data are consistent with a "
                  "relationship the theory expected. It is not an experiment that "
                  "changed culture and watched the result."),
            ("p", "One precision in this section is easy to miss. In Chapter 2 "
                  "delivery performance had four measures. When the authors tried "
                  "to build a construct from the four, it did not pass all the "
                  "statistical tests. Three of them, lead time, release frequency "
                  "and time to restore, passed together as a construct. "
                  "So when the rest of the book says software delivery "
                  "performance, it means that three-measure construct. Change "
                  "fail rate is still useful: it is strongly correlated with the "
                  "construct, and most things correlated with delivery "
                  "performance are correlated with it also."),
            ("p", "The authors also say the finding fits Google&rsquo;s study. "
                  "Google ran a two-year project to find what its best teams had "
                  "in common, with over 200 interviews and over 250 attributes "
                  "of more than 180 active teams, as the authors report it. They expected the secret to lie "
                  "in individual traits and skills; they found it in team "
                  "dynamics. Fowler&rsquo;s foreword reads that study as "
                  "evidence from other researchers for the importance of a "
                  "Westrum-generative culture."),
            ("p", "The section ends on failure, where the types differ most. "
                  "A pathological organization looks for a throat to choke, "
                  "someone responsible to punish. But in complex systems, the "
                  "authors write, accidents are almost never the fault of one "
                  "person who saw what was coming; they emerge from many "
                  "contributing factors. So &ldquo;Human error should, instead, be "
                  "the start of the investigation&rdquo;, with the question of how "
                  "information could have reached people sooner or in a better "
                  "form. The practice of blameless postmortems comes in a later "
                  "chapter; this one gives the reasoning."),
            ("p", "Now the count. The lab takes pairs of numbers, one team per "
                  "pair: a culture score on the 1 to 7 scale and a delivery "
                  "score. The delivery score is the lesson&rsquo;s invention, "
                  "the mean of a team&rsquo;s three coded answers on lead time, "
                  "release frequency and time to restore, higher being better. "
                  "The eight teams are invented. On the preset <code>eight</code> "
                  "the lab finds r = 0.929, so r squared is 0.862, or 86.2 "
                  "percent of the spread in delivery score accounted for by the "
                  "line, with the line y = -0.488 + 1.012 x: in this sample a "
                  "team one point higher in culture score is about one point "
                  "higher in delivery score."),
            ("p", "The preset <code>moved</code> changes one number. Team "
                  "<code>h</code>, the highest in culture score at 6.0, now "
                  "scores 2.0 on delivery instead of 6.0, and r falls to 0.374, "
                  "r squared to 14.0 percent. With eight teams a single team can "
                  "move the correlation a long way; the book&rsquo;s own "
                  "analyses draw on a far larger survey, over 23,000 responses "
                  "across its years, as Chapter 1 reports. Neither preset says that culture causes delivery, "
                  "or that delivery causes culture, or that a third thing, such as "
                  "the age of the system, causes both; the correlation is the "
                  "same in all three stories."),
            ("h3", "Exercise"),
            ("ul", [
                "Five teams, culture score then delivery score: `v, 3.0, 3.0; "
                "w, 4.0, 2.0; x, 5.0, 4.0; y, 6.0, 5.0; z, 7.0, 6.0`.",
            ]),
            ("p", "Find the means of the two scores, the sum of the products of "
                  "the deviations, and the sums of squared deviations, then r. "
                  "Say what share of the spread in delivery score the line "
                  "accounts for. Then raise team <code>w</code>&rsquo;s delivery "
                  "score from 2.0 to 4.0 in the lab and say whether r rises or "
                  "falls."),
            ("p", "The chapter's last section turns from prediction to action. "
                  "The next lesson, How Do We Change Culture?, reads what the "
                  "authors say you can do about a score that is not where you "
                  "want it."),
        ],
        "lab": ("acckit", {
            "mode": "stats",
            "view": "pearson",
            "preset": "eight",
            "presets": [
                {"id": "eight",
                 "label": "Eight teams: culture score against delivery score",
                 "pairs": EIGHT_TEAMS,
                 "expect": {"astN": "8", "astMeans": "x̄ = 4.25, ȳ = 3.8125", "astR": "≈ 0.929", "astR2": "7,225/8,379 ≈ 86.2%", "astLine": "y = −41/84 ≈ −0.488 + 85/84 ≈ 1.012·x", "astWords": "positive, strong"}},
                {"id": "moved",
                 "label": "The same teams, the highest-culture team delivers poorly",
                 "pairs": EIGHT_TEAMS_MOVED,
                 "expect": {"astMeans": "x̄ = 4.25, ȳ = 3.3125", "astR": "≈ 0.374", "astR2": "841/6,027 ≈ 14.0%", "astLine": "y = 155/84 ≈ 1.845 + 29/84 ≈ 0.345·x", "astWords": "positive, moderate"}},
            ],
            "panel_title": "Culture and delivery across eight teams",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Computing a correlation",
        "steps_intro": "Four steps, the last of them on teams of your own.",
        "steps": [
            ("Find the two means",
             "Add each measure over the teams and divide by the number of teams."),
            ("Find three sums over the teams",
             "For each team, take its two deviations from the means. Sum their "
             "products, sum the squares of the first, and sum the squares of "
             "the second."),
            ("Divide",
             "r is the sum of products over the square root of the product of "
             "the two sums of squares. Square r for the share of the spread "
             "the line accounts for."),
            ("Try it on teams you know",
             "Give five teams a culture score from their answers and a delivery "
             "score from a log or a survey, type them in, and write down r and "
             "which single team moves it most."),
        ],
        "worked": {
            "title": "r for the eight teams, by hand",
            "intro": [
                "On the preset <code>eight</code> the culture scores are 2.5, 3.0, "
                "3.5, 4.0, 4.5, 5.0, 5.5 and 6.0, the delivery scores 2.0, 3.0, "
                "2.5, 4.0, 3.5, 5.0, 4.5 and 6.0.",
            ],
            "lines": [
                "mean culture 34 / 8 = 4.25; mean delivery 30.5 / 8 = 3.8125",
                "sum of products of deviations = 10.625",
                "sum of squared deviations, culture = 10.5",
                "sum of squared deviations, delivery = 12.46875",
                "r = 10.625 / sqrt(10.5 x 12.46875) = 10.625 / 11.442 = 0.929",
                "r squared = 0.862, so 86.2 percent",
                "slope 10.625 / 10.5 = 1.012; intercept 3.8125 - 1.012 x 4.25 = -0.488",
            ],
            "after": [
                "The slope says how many points of delivery score go with one "
                "point of culture score in these eight teams. It does not say "
                "what would happen to a team whose culture score you raised.",
            ],
        },
        "quiz_title": "Predictions, constructs and correlation",
        "quiz": [
            {"q": "In the exercise, what are r and r squared for the five teams "
                  "(to the precision shown)?",
             "a": ["r = 0.900 and r squared = 0.810",
                   "r = 0.810 and r squared = 0.900",
                   "r = 0.900 and r squared = 0.900",
                   "r = 0.450 and r squared = 0.200"],
             "c": 0,
             "why": "The means are 5 and 4. The deviations in culture are -2, -1, "
                    "0, 1, 2 and in delivery -1, -2, 0, 1, 2. The products sum to "
                    "9, the squares of culture to 10 and of delivery to 10, so r "
                    "is 9 over the square root of 100, which is 0.900, and r "
                    "squared is 0.810, 81 percent. Raising w's delivery score to "
                    "4.0 moves that team onto the line, and r rises to about "
                    "0.97."},
            {"q": "Which measures make up the software delivery performance "
                  "construct as Chapter 3 defines it?",
             "a": ["Lead time, release frequency and time to restore service",
                   "All four of Chapter 2's measures",
                   "Lead time, release frequency and change fail rate",
                   "Release frequency and change fail rate"],
             "c": 0,
             "why": "The four measures together classified performers well, but "
                    "as a construct they did not pass all the validity and "
                    "reliability tests. Only the three, lead time, release "
                    "frequency and time to restore, did. Change fail rate is "
                    "strongly correlated with that construct, and is not part "
                    "of it."},
            {"q": "On the preset <code>eight</code> r is 0.929. Which share does r "
                  "squared give?",
             "a": ["86.2 percent of the spread in delivery score is accounted "
                   "for by the line",
                   "92.9 percent of the teams have good delivery",
                   "7.1 percent of delivery is caused by culture",
                   "92.9 percent of the spread in delivery score is accounted "
                   "for by the line"],
             "c": 0,
             "why": "r squared is 0.929 times 0.929, which is 0.862. It is a "
                    "share of the spread in one measure, not a share of teams, "
                    "and it is not a share of causation. The 92.9 percent "
                    "answer confuses r with r squared."},
            {"q": "What did Google's study of its teams find, as the authors "
                  "report it?",
             "a": ["Team dynamics, how people interact and see their work, "
                   "mattered more than which individuals were on the team",
                   "The most skilled individuals made the best teams",
                   "Team size was the strongest single factor",
                   "Teams with more experienced managers delivered more"],
             "c": 0,
             "why": "The authors quote Google&rsquo;s finding that team dynamics "
                    "mattered more than the individuals on the team, and cite it "
                    "as support for the importance of a generative culture. The "
                    "other options are not what the chapter reports."},
        ],
        "mistakes": [
            ("Reading “predicts” as “causes”",
             "The chapter hypothesized that culture would predict delivery "
             "performance, organizational performance and job satisfaction from "
             "theory and earlier research, and found data consistent with it. "
             "Its own footnote calls this inferential predictive research. A "
             "correlation fits culture driving delivery, delivery driving "
             "culture, or a third thing driving both; the argument for the first "
             "reading is the theory, not the correlation."),
            ("Taking r squared for the share of teams or the share of cause",
             "r of 0.929 gives r squared of 0.862: 86.2 percent of the spread in "
             "the delivery score is accounted for by the straight line through "
             "the points. It is not the share of teams that deliver well, and it "
             "does not say how much of delivery culture causes."),
            ("Counting change fail rate in the delivery performance construct",
             "Chapter 2 gave four measures, but in Chapter 3 the authors report "
             "that the four did not together pass the validity and reliability "
             "tests. Only lead time, release frequency and time to restore form "
             "the construct, and change fail rate is strongly correlated with "
             "it."),
        ],
        "standard": (
            "Finish when you can compute and read a correlation of this kind.",
            "Given pairs of culture and delivery scores for several teams, find r "
            "and r squared by hand, say what share of the spread r squared "
            "describes, and say why a correlation of this kind is a prediction "
            "and not a proof of cause."
        ),
        "note": (
            "The lab computes r for the pairs you type. It cannot tell you "
            "which way any cause runs, whether a third factor drives both "
            "scores, or whether eight teams are representative; the book argues "
            "the direction from theory and many years of survey data, and "
            "Chapter 12 says how."
        ),
    },
    # ---------------------------------------------------------------- 04
    # How Do We Change Culture? (PDF pp. 74-75 of the operator's copy):
    # Shook's account of the Fremont plant (p. 74), the hypothesis that Lean
    # and Agile practices affect culture (p. 74), Figure 3.3 (p. 74, in
    # prose only), "act your way" (p. 75), footnote 3 (p. 75).
    # Quote: PDF p. 74 of the operator's copy, 25 words, quotes.py OK.
    # Lesson total: 25 words.
    {
        "slug": "how-do-we-change-culture",
        "title": "How Do We Change Culture?",
        "module": "Chapter 3 · Measuring and Changing Culture",
        "one_line": "Start by changing what people do, not what they are told to think; the authors found that technical and management practices move the culture score.",
        "summary": (
            "The chapter's last section gives its answer on how culture "
            "changes. Read John Shook's account of the Fremont plant and the "
            "authors' hypothesis that Lean and continuous delivery practices "
            "change culture, and what their data say; then compare one team's "
            "two surveys and a team that changed nothing, and see what the "
            "change in scores does and does not tell you."
        ),
        "key": [
            "change how people behave first",
            "practices can change culture",
            "Lean management and continuous delivery",
            "act your way to a better culture",
            "compare each person, and the mean",
            "a change in score does not give its cause",
        ],
        "key_label": "Changing culture in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Behaviour before belief",
             "John Shook's lesson from the Fremont plant, as the authors quote "
             "it: change starts from how people behave, and "
             "not first from how they think. The authors hypothesize that "
             "adopting Lean and Agile practices therefore changes culture."),
            ("Drivers of culture",
             "The practices the authors found to influence the Westrum score: "
             "Lean management and the technical practices known as continuous "
             "delivery. The chapter shows them in its Figure 3.3 and takes them "
             "up in Chapters 4, 7 and 8."),
            ("Change in a score",
             "The difference between a respondent's mean, or a team's, on a "
             "later survey and an earlier one. The lab also shows who changes "
             "band. It says how far the numbers moved, and nothing about why."),
        ],
        "read_title": "The chapter's claim about change, then the count",
        "read_intro": (
            "Read How Do We Change Culture? in your own copy first; it is "
            "short. The lesson reads its argument and what the authors set "
            "out to test, then compares two surveys of a team."
        ),
        "body": [
            ("p", "John Shook, in the authors&rsquo; quotation, learned that &ldquo;the "
                  "way to change culture is not to first change how people "
                  "think, but instead to start by changing how people "
                  "behave&mdash;what they do&rdquo;. The words open How Do We "
                  "Change Culture?, the closing section of Chapter 3. Shook was describing his "
                  "experience helping transform the culture of the Fremont, "
                  "California, car plant that was the starting point of the Lean "
                  "manufacturing movement in the United States, and the story is "
                  "told in a radio episode the chapter cites in a footnote. This "
                  "lesson reads the section and what the authors made of it."),
            ("p", "The authors take Shook&rsquo;s idea as a hypothesis for "
                  "software: following the theory of the Lean and Agile "
                  "movements, implementing their practices can have an effect on "
                  "culture. They looked at both technical practices and "
                  "management practices and measured their impact on culture. "
                  "Their research shows, they say, that Lean management, with the "
                  "set of technical practices called continuous delivery, do "
                  "affect culture, as the chapter&rsquo;s Figure 3.3 shows. The "
                  "practices themselves are the business of Chapter 4 and "
                  "Chapters 7 and 8, which later lessons read."),
            ("p", "The conclusion the chapter draws is practical: a better "
                  "culture can be reached by acting, through implementing these "
                  "practices in technology organizations, as in "
                  "manufacturing. It does not say that culture will change by "
                  "decree, by a values statement or by a training day. It also "
                  "does not say how long a change takes. Its evidence is the "
                  "relationship between practices and culture scores in the "
                  "authors&rsquo; survey data; it does not describe following "
                  "one team through a change."),
            ("p", "That difference is what the lab explores. A before-and-after "
                  "comparison of one team is not what the book did, and it "
                  "cannot be what proves the book right; it is how you would "
                  "watch your own team. The lab uses the Westrum view with two "
                  "surveys, six months apart, of the same six invented people "
                  "matched by label, on the six aspects of the first lesson and "
                  "its cut-points of 3 and 5. The team has adopted some new "
                  "practices between the two; the lesson does not say which, "
                  "because the numbers cannot."),
            ("p", "On the preset <code>adopted</code> the respondent means go "
                  "from 2.833, 4.167, 2.167, 4.833, 3.667 and 3.333 to 4.333, "
                  "4.833, 2.833, 4.667, 4.833 and 3.333. The changes are +1.500, "
                  "+0.667, +0.667, -0.167, +1.167 and 0.000, and the team mean "
                  "rises from 3.500 to 4.139, a change of +0.639. Five people "
                  "rose or stayed level and one fell a little. One person, "
                  "<code>s1</code>, moved from the pathological band into the "
                  "bureaucratic one; nobody crossed into the generative band, "
                  "and the team stays bureaucratic. A score can rise by "
                  "two-thirds of a point and leave the team in the same band, "
                  "which is a good reason to look at both."),
            ("p", "Is +0.639 a lot? The preset <code>unchanged</code> is a second "
                  "team that began from the same answers and adopted nothing; "
                  "its people simply answered again. Its means move from 3.500 "
                  "to 3.639, a change of +0.139, and nobody changes band. People "
                  "answer a little differently on a second day, and a few "
                  "answers drift. The lab cannot say that +0.139 is the "
                  "ordinary size of a drift in general, only that one team "
                  "which changed nothing moved that much. Comparing a team "
                  "that changed practices with one that did not is a design "
                  "idea, not one the lesson can settle with twelve people."),
            ("p", "Between the two surveys the team may have also lost a person, "
                  "gained a manager, shipped a hard release or passed a "
                  "reorganization. Any of these can move a score. The change "
                  "tells you that the numbers moved. It does not tell you why, "
                  "and by itself it does not even tell you that the cause was "
                  "the practices; what the book adds is theory and a pattern "
                  "across many teams."),
            ("h3", "Exercise"),
            ("ul", [
                "Before: `x1, 3, 3, 4, 3, 3, 4; x2, 5, 5, 4, 5, 5, 5; x3, 2, 2, 2, "
                "3, 2, 2`.",
                "After: `x1, 3, 4, 4, 4, 4, 4; x2, 5, 6, 5, 6, 5, 6; x3, 2, 2, 2, "
                "2, 2, 2`.",
            ]),
            ("p", "Find each person&rsquo;s mean before and after, the change for "
                  "each, and the team&rsquo;s mean and change. With cut-points 3 "
                  "and 5, say who changes band. Then say what you would need to "
                  "know to explain the change."),
            ("p", "This closes the course. The next course, Technical Practices "
                  "and Architecture, begins with its first lesson, What Is "
                  "Continuous Delivery?, on the technical practices the chapter "
                  "has just said move culture."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "westrum",
            "preset": "adopted",
            "presets": [
                {"id": "adopted",
                 "label": "Six people surveyed twice, six months apart",
                 "points": 7,
                 "items": ASPECTS,
                 "answers": BEFORE_TEAM,
                 "answers2": AFTER_TEAM,
                 "cuts": CUTS,
                 "expect": {"alkTeam": "3.5, bureaucratic", "alkBands": "pathological 2, bureaucratic 4, generative 0", "alkTeam2": "149/36 ≈ 4.139, bureaucratic", "alkBands2": "pathological 1, bureaucratic 5, generative 0", "alkChange": "+23/36 ≈ 0.639 (bureaucratic to bureaucratic)", "alkEach": "6: s1 +1.5, s2 +2/3 ≈ 0.667, s3 +2/3 ≈ 0.667, s4 −1/6 ≈ −0.167, s5 +7/6 ≈ 1.167, s6 0"}},
                {"id": "unchanged",
                 "label": "A team that adopted nothing, answering twice",
                 "points": 7,
                 "items": ASPECTS,
                 "answers": CONTROL_BEFORE,
                 "answers2": CONTROL_AFTER,
                 "cuts": CUTS,
                 "expect": {"alkTeam2": "131/36 ≈ 3.639, bureaucratic", "alkBands2": "pathological 2, bureaucratic 4, generative 0", "alkChange": "+5/36 ≈ 0.139 (bureaucratic to bureaucratic)"}},
            ],
            "panel_title": "A team's two surveys",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Reading a change in culture scores",
        "steps_intro": "Four steps, the last of them on a team of your own.",
        "steps": [
            ("Match the respondents, if you can",
             "Pair each person's two surveys by a label. If the surveys are "
             "anonymous and cannot be matched, you can compare only the team "
             "means."),
            ("Find each person's change",
             "Subtract the earlier mean from the later for every person, and "
             "average the changes. With the same people, this equals the change "
             "in the team mean."),
            ("Look for band changes and for people who fell",
             "List who moved to another band and who went down. A rise in the "
             "mean can hide a fall."),
            ("Ask what else moved",
             "Write down what else changed on the team between the two surveys, "
             "and, if you can, run the same survey on a team that changed "
             "nothing, to see how much scores move by themselves."),
        ],
        "worked": {
            "title": "One respondent and the team, on the preset adopted",
            "intro": [
                "Take respondent <code>s1</code>, who answered 3, 3, 3, 3, 2, 3 "
                "and then 4, 5, 4, 5, 4, 4, and then the team.",
            ],
            "lines": [
                "s1 before 17 / 6 = 2.833: below 3, pathological band",
                "s1 after 26 / 6 = 4.333: bureaucratic band",
                "s1 change 4.333 - 2.833 = +1.500",
                "team before 126 / 36 = 3.500; after 149 / 36 = 4.139",
                "team change 4.139 - 3.500 = +0.639, which is 23 / 36",
            ],
            "after": [
                "The team change is also the mean of the six personal "
                "changes, 3.833 / 6, because the same six people answered both "
                "times. The mean change is positive; it does not say why.",
            ],
        },
        "quiz_title": "Behaviour, practices and change in a score",
        "quiz": [
            {"q": "In the exercise, which respondent changes band, with cut-points "
                  "3 and 5 as in the lesson?",
             "a": ["x2 only, from bureaucratic to generative",
                   "x1 only, from pathological to bureaucratic",
                   "x1 and x2",
                   "Nobody"],
             "c": 0,
             "why": "The means before are x1 3.333, x2 4.833, x3 2.167 and after "
                    "x1 3.833, x2 5.500, x3 2.000. Only x2 crosses a cut-point, "
                    "moving from under 5 to 5 or above. x1 was already above 3, "
                    "and x3 stayed below 3. The team mean goes from 3.444 to "
                    "3.778, +0.333, and stays bureaucratic."},
            {"q": "According to Shook as the authors quote him, what is the way "
                  "to change a culture?",
             "a": ["Begin with a change in behaviour, in what people do",
                   "First change how people think, then their behaviour",
                   "Write down the values and display them",
                   "Replace the people who hold the old assumptions"],
             "c": 0,
             "why": "Shook's lesson from Fremont, quoted in the chapter, is that "
                    "the way to change culture is to start by changing behaviour "
                    "and not by first changing thinking. The authors build their "
                    "hypothesis about practices on it."},
            {"q": "What change in the team mean does the lab report on the preset "
                  "<code>unchanged</code>?",
             "a": ["+0.139",
                   "+0.639",
                   "0.000",
                   "+0.333"],
             "c": 0,
             "why": "The second team's before total is 126 over 36, 3.500, and "
                    "its after total is 131 over 36, 3.639, a change of 5 over "
                    "36, +0.139. +0.639 is the team that adopted new practices; "
                    "0.000 would need no answer to differ; +0.333 is the "
                    "exercise's change."},
            {"q": "Which practices does Chapter 3 report as affecting culture?",
             "a": ["Lean management and the technical practices of continuous "
                   "delivery",
                   "Written mission statements and creeds",
                   "Hiring from outside the organization",
                   "National culture and country of origin"],
             "c": 0,
             "why": "The chapter's research found that Lean management and "
                    "continuous delivery have an impact on culture. Mission "
                    "statements are given in the chapter only as an example of "
                    "artifacts, Schein's most visible level, and national culture "
                    "only as one way of modelling culture; neither is reported "
                    "as a driver."},
        ],
        "mistakes": [
            ("Changing how people think first, and expecting behaviour to follow",
             "Shook's experience, which the authors adopt as a hypothesis, was "
             "the reverse order: start with what people do. The "
             "chapter's advice is to implement the practices, not to wait for "
             "belief."),
            ("Reading a rise in the score as proof that the practices did it",
             "The change is a difference between two sets of answers. Other "
             "things moved on the team too, and a team that changed nothing "
             "also moved on the lab's second preset. The book's case rests on "
             "theory and on a pattern across many teams, not on one team&rsquo;s "
             "before-and-after."),
            ("Reading the team mean as the change in each person",
             "A mean change of +0.639 hides a person up 1.5, a person who fell "
             "and a person who did not move. Compare each respondent, and who "
             "changes band, as well as the team mean."),
        ],
        "standard": (
            "Finish when you can read two surveys and say what they do not show.",
            "Given a team's answers at two times, find each respondent's change "
            "and the team's, say who changes band, and name two things the "
            "change cannot tell you."
        ),
        "note": (
            "The lab subtracts one set of means from another. It cannot tell you "
            "that the practices caused a change, how large a change the book "
            "would call meaningful, or whether six invented people behave "
            "like a team; the book reports its practices-and-culture finding "
            "across its survey and does not describe following one team."
        ),
    },
]
