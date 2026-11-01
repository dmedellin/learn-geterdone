"""The Science Behind the Book, lessons 6-7 -- the rest of Chapter 13.

Nicole Forsgren, Jez Humble and Gene Kim, Accelerate: The Science of Lean
Software and DevOps (IT Revolution, 2018): Chapter 13, Introduction to
Psychometrics (Latent Constructs Give Us Several Views into Our Data, Latent
Constructs Help Safeguard Against Rogue Data, How Latent Constructs Can Be
Used for System Data), with Appendix C, Tests of the Measurement Model, for
the statement of Cronbach's alpha. Pages in the comments are PDF pages of the
operator's copy; the lessons cite by chapter and section. Every quotation is
copied from that copy and checked with quotes.py. The samples are written for
these lessons: none of the book's items, tables or data is reproduced. The
design is docs/accelerate/PLAN.md, section C, Course 6.
"""


_PANEL_INTRO = (
    "A figure computed from the small sample the lesson states. It shows what "
    "one measure says about that sample; the book's findings are its survey's, "
    "and a correlation is not a cause."
)


# ---------------------------------------------------------------- 06 samples

# Six invented items in two constructs; the sixth, B3, is a stray: it is
# written for the second construct and moves with the first.
TWO_CONSTRUCTS = (
    "A1, confidence; A2, confidence; A3, confidence; "
    "B1, burden; B2, burden; B3, burden"
)
STRAY_CORR = (
    "A1, A2, 0.72; A1, A3, 0.68; A2, A3, 0.64; "
    "B1, B2, 0.70; B1, B3, 0.20; B2, B3, 0.24; "
    "A1, B1, 0.18; A1, B2, 0.22; A1, B3, 0.55; "
    "A2, B1, 0.15; A2, B2, 0.20; A2, B3, 0.50; "
    "A3, B1, 0.21; A3, B2, 0.17; A3, B3, 0.52"
)
# The same correlations with B3 reassigned to the first construct.
REASSIGNED = (
    "A1, confidence; A2, confidence; A3, confidence; "
    "B1, burden; B2, burden; B3, confidence"
)
# 06 exercise: five items in two constructs.
EX_ITEMS = "P1, p; P2, p; P3, p; Q1, q; Q2, q"
EX_CORR = (
    "P1, P2, 0.65; P1, P3, 0.60; P2, P3, 0.55; Q1, Q2, 0.60; "
    "P1, Q1, 0.15; P1, Q2, 0.10; P2, Q1, 0.20; P2, Q2, 0.15; "
    "P3, Q1, 0.60; P3, Q2, 0.65"
)

# ---------------------------------------------------------------- 07 samples

# Eight days of four signals about the strain on one invented service, each
# banded 1 to 7 by a stated rule, 7 being the most strained.
SIGNALS_AGREE = (
    "d1, 1, 1, 1, 1; d2, 4, 3, 4, 4; d3, 2, 3, 3, 4; d4, 4, 5, 4, 4; "
    "d5, 4, 3, 3, 5; d6, 5, 6, 4, 4; d7, 5, 5, 5, 4; d8, 6, 4, 5, 6"
)
# The same days after the fourth signal's collector changed on day 5.
SIGNALS_CHANGED = (
    "d1, 1, 1, 1, 1; d2, 4, 3, 4, 4; d3, 2, 3, 3, 4; d4, 4, 5, 4, 4; "
    "d5, 4, 3, 3, 7; d6, 5, 6, 4, 1; d7, 5, 5, 5, 1; d8, 6, 4, 5, 3"
)
SIGNAL_NAMES = "signal-1, signal-2, signal-3, signal-4"
# 07 exercise: five days, three signals.
SIGNALS_THREE = "d1, 7, 1, 7; d2, 4, 2, 5; d3, 6, 4, 7; d4, 5, 4, 5; d5, 4, 1, 3"


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Latent Constructs Give Us Several Views into Our Data (PDF pp. 190-192
    # of the operator's copy), with the validity and reliability tests (p.
    # 191); Latent Constructs Help Safeguard Against Rogue Data (pp.
    # 192-195), with the notification example (pp. 193-195); Appendix C, Tests
    # of the Measurement Model (pp. 268-270) for the tests named at the end.
    # Quote: PDF p. 191 of the operator's copy, 14 words, quotes.py OK.
    # Lesson total: 14 words.
    {
        "slug": "several-views-and-rogue-data",
        "title": "Several Views, and a Safeguard Against Rogue Data",
        "module": "Chapter 13 · Introduction to Psychometrics",
        "one_line": "Items that belong to one construct should go together and stay apart from the others, and a test that says so is also an alarm.",
        "summary": (
            "A score is only worth reporting if the items behave. Read what the "
            "validity and reliability tests are for, why the authors run them "
            "before any analysis and again from time to time, and how a "
            "five-item construct turned out to be two. Then read a correlation "
            "matrix for two invented constructs and find the item that belongs "
            "with the wrong one."),
        "key": [
            "convergent: items that go together do",
            "discriminant: items that should not, don't",
            "reliability: items read the same way",
            "tests come before any analysis",
            "retest: a construct can stop passing",
            "one stray item shows in the matrix",
        ],
        "key_label": "Validity, reliability and rogue data in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Convergent and discriminant validity",
             "Two tests that the items of a construct measure one thing. "
             "Convergent validity asks whether items meant to go together do "
             "correlate; discriminant validity asks whether items meant to be "
             "separate fail to. "
             "Appendix C reads them with principal components, average variance "
             "extracted and a ceiling on cross-construct correlations."),
            ("Reliability (internal consistency)",
             "Assurance that the people who answer read and interpret the items "
             "similarly. The next lesson computes one such figure, Cronbach's "
             "alpha. A construct that passes the validity and reliability tests "
             "is said to exhibit good psychometric properties."),
            ("A stray item",
             "An item written for one construct whose answers move more with "
             "another construct's items than with its own. The lab spots one "
             "by comparing each item's average correlation with its own "
             "construct's other items against its average with each other "
             "construct's items."),
        ],
        "read_title": "Several views of one idea, and what happens when one of them goes wrong",
        "read_intro": (
            "Read the two sections of Chapter 13 headed by several views and by "
            "rogue data in your own copy first. The lesson follows them and then "
            "reads a matrix of correlations the way their tests do, in outline."
        ),
        "body": [
            ("p", "&ldquo;Taken together, validity and reliability statistical tests "
                  "confirm our measures. They come before any analysis.&rdquo; Forsgren, "
                  "Humble and Kim write that in Chapter 13, in the section on how "
                  "latent constructs give several views into the data. The last "
                  "lesson scored a construct from its items. This one asks how "
                  "you would know the items belong together, and what the "
                  "authors do when they find that some do not."),
            ("p", "Once the data is in, the authors say, they run statistical tests "
                  "that check the items all measure the same underlying idea. "
                  "Discriminant validity tests make sure that items that should "
                  "not be related are unrelated; their example is items thought "
                  "not to capture culture that turn out to relate to it. "
                  "Convergent validity tests make sure that items that should be "
                  "related are, so that items meant to measure culture do measure "
                  "it. Reliability tests, also called internal consistency, give "
                  "assurance that the people taking the survey read and "
                  "interpret the items alike. The tests are an order of work, as "
                  "the opening sentence says: constructs are confirmed first, and "
                  "only constructs that pass go forward to the analyses of the "
                  "rungs above."),
            ("p", "Their model case is the culture construct. Seven items, rated "
                  "on the seven-point agreement scale, passed the "
                  "tests and are, the authors say, statistically valid and "
                  "reliable. They also note a decision made when the items were "
                  "written, a departure from Westrum's original frame: the items "
                  "ask about a team and not an organisation, because an "
                  "organisation can hold pockets of different cultures and "
                  "a person's answer about their own team is likelier to be "
                  "accurate."),
            ("p", "The third section adds a second use of the same tests. A "
                  "construct that passes today may not pass tomorrow, so the "
                  "authors recommend retesting those that have good "
                  "psychometric properties periodically, particularly if you "
                  "suspect the system or its environment has changed. A "
                  "construct that fails after passing is a rogue-data alarm: "
                  "something about the data has changed."),
            ("p", "Their example is a construct that was not so well behaved. They "
                  "wanted to measure how teams learn of failures, with five items: "
                  "two about being told by people outside the automated process "
                  "(customers and a network operations centre), and three about "
                  "alerts and monitoring from systems. In a pilot with about 20 "
                  "technical professionals the items loaded together, which "
                  "means they measured one underlying idea. In the final, larger "
                  "data collection the tests did not confirm one construct but "
                  "revealed two: notification from outside the automated "
                  "processes, and notification from systems, which the authors "
                  "call proactive failure notification. They found the second "
                  "predictive of software delivery performance. Had they asked a "
                  "single question about failure monitoring, they say, they would "
                  "not have known that where the notice comes from matters."),
            ("p", "Now read a matrix the way the first of those tests does, in "
                  "outline. The lab's sample is six invented items in two "
                  "constructs: <code>A1</code>, <code>A2</code> and "
                  "<code>A3</code> measure confidence in releasing, and "
                  "<code>B1</code>, <code>B2</code> and <code>B3</code> measure "
                  "the burden of being on call. Each cell is the correlation of "
                  "two items across the people who answered, and the matrix is "
                  "shown with only its lower triangle."),
            ("math", [
                "      A1    A2    A3    B1    B2",
                "A2    0.72",
                "A3    0.68  0.64",
                "B1    0.18  0.15  0.21",
                "B2    0.22  0.20  0.17  0.70",
                "B3    0.55  0.50  0.52  0.20  0.24",
            ]),
            ("p", "On the preset <code>one-stray-item</code>, the lab reports the "
                  "average correlation among each construct's own items: 0.68 "
                  "for the first construct, 0.38 for the second. The average "
                  "across the two constructs, over the nine cross pairs, is "
                  "0.3. The first construct's items agree strongly; the second "
                  "does not, and the item-by-item table shows why. For every "
                  "item the table gives its average correlation with its own "
                  "construct's other items and with the other construct's items. "
                  "For <code>A1</code> that is 0.7 against 19/60, about 0.317, "
                  "and the other four ordinary items show the same wide gap. "
                  "<code>B3</code> shows 0.22 with its own and 157/300, about "
                  "0.523, with the first construct, so the lab lists it as the "
                  "one item that goes with the wrong construct."),
            ("p", "Move it where it belongs. On the preset <code>reassigned</code> "
                  "the same correlations are used, with <code>B3</code> written "
                  "as part of the first construct. That construct now averages "
                  "about 0.602 over its six pairs, the second has one pair at "
                  "0.7, and the average across the two falls to 0.19625 over "
                  "eight pairs. No item is listed any longer. The cross-construct "
                  "average being lower after the move is the sign that the "
                  "items were mislabelled and not that the data improved: "
                  "nothing in the numbers was changed."),
            ("p", "The lab is a picture of the test, not the test. Appendix C "
                  "runs principal components with varimax rotation and asks for "
                  "loadings above 0.60 without cross-loading, average variance "
                  "extracted above 0.50, the square root of that above each "
                  "correlation with another construct, and correlations below "
                  "0.85, which Surveys, Data and Statistical Methods reads and computes. The averages here "
                  "show the pattern those tests look for, with six items and "
                  "no people, and a stray item can hide in an average that "
                  "looks acceptable."),
            ("h3", "Exercise"),
            ("ul", [
                "Items: `P1, p; P2, p; P3, p; Q1, q; Q2, q`.",
                "Correlations: `P1, P2, 0.65; P1, P3, 0.60; P2, P3, 0.55; Q1, Q2, "
                "0.60; P1, Q1, 0.15; P1, Q2, 0.10; P2, Q1, 0.20; P2, Q2, 0.15; "
                "P3, Q1, 0.60; P3, Q2, 0.65`.",
            ]),
            ("p", "For each item, average its correlations with its own "
                  "construct's other items and with the other construct's items. "
                  "Say which item the lab will list and by how much, then check "
                  "your table in the lab."),
            ("p", "A construct that holds together can be scored and relied on, "
                  "and the same idea reaches beyond surveys. The next lesson, "
                  "Latent Constructs and System Data, reads how."),
        ],
        "lab": ("acckit", {
            "mode": "validity",
            "view": "matrix",
            "preset": "one-stray-item",
            "presets": [
                {"id": "one-stray-item",
                 "label": "Six invented items in two constructs, one of them out of place",
                 "items": TWO_CONSTRUCTS,
                 "corr": STRAY_CORR,
                 "expect": {"avdItems": "6 items in 2 constructs", "avdWithin": "confidence 0.68; burden 0.38", "avdCross": "0.3", "avdFlagged": "1: B3 (own 0.22; with confidence 157/300 ≈ 0.523)"}},
                {"id": "reassigned",
                 "label": "The same correlations with the stray item written for the first construct",
                 "items": REASSIGNED,
                 "corr": STRAY_CORR,
                 "expect": {"avdItems": "6 items in 2 constructs", "avdWithin": "confidence 361/600 ≈ 0.602; burden 0.7", "avdCross": "0.19625", "avdFlagged": "0: none"}},
            ],
            "panel_title": "Which items go with which construct",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Reading a correlation matrix for a stray item",
        "steps_intro": "Five steps, the last of them on items of your own.",
        "steps": [
            ("Say which construct each item was written for",
             "List the items with the construct each is meant to measure. This "
             "is the design, and the matrix tests it."),
            ("Average the within-construct correlations",
             "For each construct, add the correlations among its own items and "
             "divide by the number of pairs. Do the same for all pairs that cross "
             "between constructs."),
            ("Compare each item with its own and with the others",
             "For one item, average its correlations with its own construct's "
             "other items, then with the items of each other construct."),
            ("List the items that go with the wrong group",
             "An item whose average with another construct exceeds its average "
             "with its own is a candidate stray. Look at its wording before you "
             "move it."),
            ("Do it on items of your own",
             "Take a short survey you have on file with two constructs and at "
             "least three items each, get its correlation matrix from any "
             "spreadsheet, and type the lower triangle into the lab. Write "
             "down any item the lab lists and what the item asks."),
        ],
        "worked": {
            "title": "The averages for one-stray-item by hand",
            "intro": [
                "Find the three averages and B3's two figures for "
                "<code>one-stray-item</code>.",
            ],
            "lines": [
                "first construct: (0.72 + 0.68 + 0.64) / 3 = 2.04 / 3 = 0.68",
                "second construct: (0.70 + 0.20 + 0.24) / 3 = 1.14 / 3 = 0.38",
                "cross pairs: 0.95 + 0.85 + 0.90 = 2.70, over 9 = 0.3",
                "B3 with its own: (0.20 + 0.24) / 2 = 0.22",
                "B3 with the first construct: (0.55 + 0.50 + 0.52) / 3 = 1.57 / 3 ≈ 0.523",
                "0.523 > 0.22: B3 is listed",
            ],
            "after": [
                "The nine cross pairs add as the three items of the first "
                "construct against B1, B2 and B3. Without B3's three the other "
                "six cross pairs average 0.188, so the single stray item "
                "raises the average across constructs from about 0.188 to 0.3.",
            ],
        },
        "quiz_title": "Validity, reliability and what the tests are for",
        "quiz": [
            {"q": "In Chapter 13, what does a discriminant validity test make sure "
                  "of?",
             "a": ["That items which are supposed to be related are related",
                   "That items which are not supposed to be related are unrelated",
                   "That the people who answer read and interpret the items alike",
                   "That the findings hold in a sample of a different population"],
             "c": 1,
             "why": "The chapter pairs discriminant and convergent validity. "
                    "Discriminant is the test that unrelated items are unrelated; "
                    "convergent is the test that related items are related. "
                    "Reading items alike is reliability, or internal consistency. "
                    "Holding in other populations is a question about the sample, "
                    "which neither validity test answers."},
            {"q": "In the exercise, which item does the lab list, and with which "
                  "averages?",
             "a": ["Q1: 0.6 with its own construct, 0.317 with the other",
                   "P3: 0.625 with its own construct, 0.575 with the other",
                   "P3: 0.575 with its own construct, 0.625 with the other",
                   "No item: every item correlates more with its own construct"],
             "c": 2,
             "why": "P3 averages (0.60 + 0.55)/2 = 0.575 with P1 and P2 and "
                    "(0.60 + 0.65)/2 = 0.625 with Q1 and Q2, so its cross average "
                    "is the larger and it is listed. Q1 averages 0.600 with Q2 and "
                    "(0.15 + 0.20 + 0.60)/3 = 0.317 with P1, P2, P3, which is the "
                    "ordinary pattern. P3 at 0.625 with its own construct swaps "
                    "the two figures, and no item ignores P3."},
            {"q": "On the preset reassigned, the first construct has the items A1, "
                  "A2, A3 and B3. What is the average correlation among its own "
                  "items?",
             "a": ["0.68", "0.523", "0.3", "0.602"],
             "c": 3,
             "why": "Four items give six pairs: 0.72, 0.68, 0.64, 0.55, 0.50 and "
                    "0.52, which sum to 3.61 and average 0.602. 0.68 is the "
                    "average of the three original items before the move, 0.523 is "
                    "B3's average with them, and 0.3 is the cross-construct "
                    "average before the move."},
            {"q": "What did the authors find when they ran the validity tests on "
                  "their five failure-notification items in the final, larger "
                  "data collection?",
             "a": ["The items revealed two constructs, not the single one the "
                   "pilot of about 20 people had suggested",
                   "The items loaded together as one construct, as in the pilot",
                   "The items failed reliability, so the construct was dropped",
                   "A single item explained all the others, so four were removed"],
             "c": 0,
             "why": "The chapter says the pilot items loaded together but the "
                    "final tests did not confirm one construct and revealed two, "
                    "one for notifications from outside automated processes and "
                    "one for notifications from systems. The authors report both "
                    "and found the second predictive of software delivery "
                    "performance, so the construct was split rather than dropped."},
        ],
        "mistakes": [
            ("Taking one well-worded question to be enough",
             "A single question cannot be checked against anything. The chapter's "
             "failure-notification example shows what a question would have "
             "hidden: the five items were two constructs, and where the notice "
             "comes from mattered to the outcome."),
            ("Treating a construct that passed once as settled",
             "The authors recommend retesting periodically, especially if the "
             "system or environment may have changed, because items that "
             "belonged together can stop doing so. A construct is passing, not "
             "proven."),
            ("Reading several views as immunity from a bad source",
             "The chapter says several measures make it harder for one bad "
             "source to skew results, and give a better chance of "
             "noticing it. Neither is a guarantee: in the lab a stray item "
             "raises the cross-construct average from about 0.188 to 0.3 and shows "
             "up only because the matrix is read item by item."),
        ],
        "standard": (
            "Finish when you can read a matrix for a stray item.",
            "Given two constructs' items and a lower-triangle correlation matrix, "
            "find each construct's average correlation, each item's own and "
            "cross averages, and name the item that goes with the wrong group."
        ),
        "note": (
            "The lab compares averages in a matrix you type. It is not the "
            "principal-components, variance-extracted and reliability tests the "
            "book reports in Appendix C, and it cannot tell why an item goes with "
            "the wrong group; that is a reading of what the item asks."
        ),
    },
    # ---------------------------------------------------------------- 07
    # How Latent Constructs Can Be Used for System Data (PDF pp. 195-196 of
    # the operator's copy); reliability as internal consistency (p. 191);
    # Appendix C, Cronbach's alpha and composite reliability (pp. 269-270).
    # Quote: PDF p. 196 of the operator's copy, 15 words, quotes.py OK.
    # Lesson total: 15 words.
    {
        "slug": "latent-constructs-and-system-data",
        "title": "Latent Constructs and System Data",
        "module": "Chapter 13 · Introduction to Psychometrics",
        "one_line": "The same idea works on a service's own signals: several readings of one thing, and a figure for whether they agree.",
        "summary": (
            "Chapter 13 closes by saying its ideas carry over from surveys to the "
            "data a system produces: use several measures, and remember that "
            "every measure is a proxy. Read that section, then compute "
            "Cronbach's alpha, the book's figure for internal consistency, for "
            "four invented signals about one service and watch what one signal "
            "that goes wrong does to it."),
        "key": [
            "every measure is a proxy",
            "several signals beat one",
            "alpha: how well the signals agree",
            "0.70 is the usual cutoff",
            "alpha runs low on short scales",
            "agreeing is not the same as valid",
        ],
        "key_label": "Constructs on system data in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the book's, the "
            "third the lab's."
        ),
        "concepts": [
            ("A proxy",
             "A measure that stands for an idea it is not. Chapter 13 says all "
             "measures are proxies, system data as much as survey data: response "
             "time stands in for a system's performance, as an item's answer "
             "stands in for part of a team's culture."),
            ("Cronbach's alpha",
             "A figure of at most 1, and below 0 when items move against each other, for how well a set of items measure "
             "together, which Appendix C calls a measure of internal "
             "consistency, with an acceptable cutoff of 0.70. It is high when "
             "the items vary together and low when each varies on its own."),
            ("Alpha with an item removed",
             "Alpha recomputed from the other items. The lab prints it for every "
             "item. An item whose removal lifts alpha well past the rest is the "
             "one pulling the figure down."),
        ],
        "read_title": "The same safeguards on a system's own data",
        "read_intro": (
            "Read How Latent Constructs Can Be Used for System Data at the end "
            "of Chapter 13 in your own copy first, and the paragraph on "
            "reliability in Appendix C. The lesson follows them and then "
            "computes alpha."),
        "body": [
            ("p", "&ldquo;Latent constructs give us one mechanism to protect "
                  "ourselves against bad measures or bad agents.&rdquo; That is "
                  "the last argument of Chapter 13, and it is made about "
                  "surveys and system data in the same breath. The chapter's final "
                  "section, How Latent Constructs Can Be Used for System Data, is "
                  "short, and it is written for readers who already trust what "
                  "their toolchain records."),
            ("p", "Its advice carries over in two parts. Collect several measures "
                  "and look for the same pattern across them, and think through "
                  "what you are really trying to proxy. If you want to measure "
                  "a system's performance, response time is one measure of it; "
                  "ask what other aspects of performance would show in the "
                  "system's data, and you may find that what you care about is a "
                  "concept better captured by several related measures than "
                  "by one. Then comes the sentence the chapter stresses: all "
                  "measures are proxies, true of system data as of survey "
                  "data."),
            ("p", "The risk of a single measure is concrete. A change to the "
                  "code that collects a metric can alter that one measure, and "
                  "if it is the only one you have, the chance of noticing is "
                  "low. With several, a shift in one stands out against the rest "
                  "and is likelier to be caught. The authors add the same caution as before, "
                  "that measures which pass checks today should still be "
                  "checked from time to time, because they can change."),
            ("p", "How would you know the several measures agree? Chapter 13 "
                  "calls the property reliability, or internal consistency, "
                  "assurance that items are read alike. Appendix C gives "
                  "the usual figure, Cronbach's alpha, an acceptable cutoff of "
                  "0.70, and a caution: alpha runs low on short scales, "
                  "those with few items, so the authors also ran "
                  "composite reliability, and every construct met the cutoff on "
                  "one or the other."),
            ("math", [
                "α  =  k / (k − 1)  ·  ( 1 − Σ σᵢ² / σₜ² )",
                "k = number of items, σᵢ² = variance of item i,",
                "σₜ² = variance of the total score, the sum of the items",
            ]),
            ("p", "Read the formula as a comparison. If the items moved "
                  "independently, the variance of their sum would be about the "
                  "sum of their variances, the fraction would be near 1 and "
                  "alpha near 0. If they move together, the variance of the "
                  "sum is larger, the fraction smaller and alpha closer to 1. "
                  "The factor k/(k − 1) corrects for the number of items. "
                  "Divide the squared distances by n or by n − 1 and the "
                  "variances change by the same factor, so alpha is the same "
                  "either way."),
            ("p", "The caution about small scales can be shown without any "
                  "data. When every item has the same variance and the items "
                  "correlate on average r, alpha equals k·r / (1 + (k − 1)·r), "
                  "the textbook relation for standardised items, which the "
                  "book does not print. With r = 0.5 it is 0.667 for two "
                  "items, 0.75 for three and 0.80 for four. The items agree "
                  "equally well in all three; only their number has changed."),
            ("p", "Now compute it on a sample written for the lesson: eight days "
                  "of four signals about the strain on one invented service, "
                  "each banded from 1 to 7 by a stated rule, 7 the most "
                  "strained. On the preset <code>four-signals-agree</code> the "
                  "lab reports alpha = 0.921, which meets 0.70; the signals' "
                  "variances are 2.359375, 2.1875, 1.484375 and 1.75, which "
                  "are 151, 140, 95 and 112 from the worked example divided by "
                  "64, and the variance of the daily totals is 25.1875, "
                  "1612 divided by 64. With each signal "
                  "left out in turn it gives 0.861, 0.931, 0.870 and 0.923, so "
                  "no single signal is holding the figure up; leaving out the "
                  "second or the fourth raises it slightly, to 0.931 and 0.923."),
            ("math", [
                "day      d1  d2  d3  d4  d5  d6  d7  d8",
                "signal 1  1   4   2   4   4   5   5   6",
                "signal 2  1   3   3   5   3   6   5   4",
                "signal 3  1   4   3   4   3   4   5   5",
                "signal 4  1   4   4   4   5   4   4   6",
            ]),
            ("p", "Now suppose the collector for the fourth signal was changed "
                  "after day 4, and it reads 7, 1, 1, 3 on the last four days. "
                  "On the preset <code>collector-changed</code> alpha is 0.610, "
                  "below the cutoff. Leave out signal 1, 2 or 3 and it "
                  "falls further, to 0.245, 0.448 and 0.320, because the changed "
                  "signal is still in and now has fewer partners; leave out "
                  "signal 4 and it returns to 0.923, which is the figure for the "
                  "three untouched signals. The table of figures with an item removed "
                  "points at the one that moved. That is the rogue-data "
                  "safeguard of the last lesson at work on system data."),
            ("p", "Do not read more into it than it holds. Alpha measures "
                  "consistency and not validity. Four signals that all follow "
                  "daily traffic would agree whether or not they measure strain. "
                  "It does not catch every failure either: if the fourth "
                  "collector froze at 4 from day 5 on, alpha in this sample "
                  "would be 0.924, because the frozen readings sit in the middle of the "
                  "others' range and its one low day, day 1, still agrees with them; "
                  "a stuck signal that contradicts nothing does not pull alpha down. And eight days is a very "
                  "small sample."),
            ("h3", "Exercise"),
            ("ul", [
                "Five days of three signals about another service: `d1, 7, 1, 7; "
                "d2, 4, 2, 5; d3, 6, 4, 7; d4, 5, 4, 5; d5, 4, 1, 3`.",
                "Find alpha and say whether it meets 0.70. Then find alpha with "
                "each signal left out in turn.",
            ]),
            ("p", "Use the sums of squares method of the worked example. Say "
                  "which signal you would look at first, and what you would "
                  "want to know about it before you removed it."),
            ("p", "That ends the first two chapters of Part II. Surveys, Data "
                  "and Statistical Methods begins with Chapter "
                  "14's case for surveys, in its first lesson, Surveys Allow You "
                  "to Collect and Analyze Data Quickly."),
        ],
        "lab": ("acckit", {
            "mode": "likert",
            "view": "alpha",
            "preset": "four-signals-agree",
            "presets": [
                {"id": "four-signals-agree",
                 "label": "Eight invented days of four signals that agree",
                 "items": SIGNAL_NAMES,
                 "answers": SIGNALS_AGREE,
                 "expect": {"alkK": "4", "alkN": "8", "alkVars": "signal-1 2.359375; signal-2 2.1875; signal-3 1.484375; signal-4 1.75", "alkTotal": "25.1875", "alkAlpha": "1,114/1,209 ≈ 0.921", "alkDeleted": "signal-1 0.861; signal-2 0.931; signal-3 0.870; signal-4 0.923", "alkMeets": "yes: 0.921 ≥ 0.7"}},
                {"id": "collector-changed",
                 "label": "The same days after the fourth signal's collector changed",
                 "items": SIGNAL_NAMES,
                 "answers": SIGNALS_CHANGED,
                 "expect": {"alkK": "4", "alkN": "8", "alkVars": "signal-1 2.359375; signal-2 2.1875; signal-3 1.484375; signal-4 3.859375", "alkTotal": "18.234375", "alkAlpha": "712/1,167 ≈ 0.610", "alkDeleted": "signal-1 0.245; signal-2 0.448; signal-3 0.320; signal-4 0.923", "alkMeets": "no: 0.610 < 0.7"}},
            ],
            "panel_title": "How well do the signals agree?",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Computing Cronbach's alpha",
        "steps_intro": "Five steps, the last of them on signals of your own.",
        "steps": [
            ("Put the signals in columns",
             "Write one row per day, or per person, and one column per signal, "
             "all on the same scale and pointing the same way."),
            ("Find each signal's spread",
             "For every column compute n times the sum of squares minus the "
             "square of the column sum. That is n² times the variance, in whole "
             "numbers."),
            ("Find the spread of the daily totals",
             "Add each row, and compute the same quantity for the row totals."),
            ("Put them together",
             "Subtract the signals' spreads, added up, over the totals' spread "
             "from 1, and multiply by k/(k − 1)."),
            ("Do it on signals of your own",
             "Pick three or four readings of one thing that you already record, "
             "band each for eight or more days on a 1 to 7 scale, and type them "
             "in. Note alpha, and alpha with each signal left out."),
        ],
        "worked": {
            "title": "Alpha for four-signals-agree by hand",
            "intro": [
                "Compute alpha with sums of squares, using n = 8, so that every "
                "line is a whole number.",
            ],
            "lines": [
                "signal 1: 8·139 − 31² = 1112 − 961 = 151",
                "signal 2: 8·130 − 30² = 1040 − 900 = 140",
                "signal 3: 8·117 − 29² = 936 − 841 = 95",
                "signal 4: 8·142 − 32² = 1136 − 1024 = 112",
                "sum of the four = 498",
                "day totals 4 15 12 17 15 19 19 21: Σ = 122, Σ² = 2062",
                "totals: 8·2062 − 122² = 16496 − 14884 = 1612",
                "α = (4/3)·(1 − 498/1612) = (4/3)·(1114/1612)",
                "α = 1114/1209 ≈ 0.921",
            ],
            "after": [
                "Using sample variances divides every spread by the same factor, "
                "which cancels in the fraction. For collector-changed the "
                "fourth signal's line becomes 8·109 − 25² = 247 and the totals' "
                "line 1167, so alpha = (4/3)·(1 − 633/1167) = 712/1167 ≈ 0.610.",
            ],
        },
        "quiz_title": "Alpha, proxies and the 0.70 cutoff",
        "quiz": [
            {"q": "What does Appendix C say about Cronbach's alpha?",
             "a": ["It measures validity, with a cutoff of 0.85, and is biased in "
                   "favour of small scales",
                   "It measures internal consistency, has an acceptable cutoff of "
                   "0.70, and is biased against scales with few items, so "
                   "composite reliability was run too",
                   "It measures how well the survey represents its population, "
                   "with a cutoff of 0.50",
                   "It is unbiased at any size, so no second figure is needed"],
             "c": 1,
             "why": "Appendix C calls alpha a measure of internal consistency, with "
                    "an acceptable cutoff of 0.70, and warns that it runs "
                    "unfairly low on scales with few items, so both alpha and composite "
                    "reliability were run and every construct met one or the other. "
                    "0.85 is the ceiling it sets for correlations between "
                    "constructs, and 0.50 is the floor for average variance "
                    "extracted."},
            {"q": "In the exercise, what is alpha for the three signals, and what "
                  "happens when signal 2 is left out?",
             "a": ["0.684, which meets 0.70; without signal 2 it falls to 0.478",
                   "0.916, which meets 0.70; without signal 2 it falls to 0.684",
                   "171/250 = 0.684, which misses 0.70; without signal 2 it is "
                   "76/83 ≈ 0.916",
                   "0.684, which misses 0.70; without signal 2 it is 0.140"],
             "c": 2,
             "why": "With n = 5 the signals' spreads are 5·142 − 26² = 34, "
                    "5·38 − 12² = 46 and 5·157 − 27² = 56, which sum to 136; the "
                    "daily totals 15, 11, 17, 14, 8 give 5·895 − 65² = 250. Alpha "
                    "is (3/2)·(1 − 136/250) = 171/250 = 0.684. Without signal 2 "
                    "there are two signals with totals 14, 9, 13, 10, 7 and a "
                    "spread of 5·595 − 53² = 166, so alpha is 2·(1 − 90/166) = "
                    "76/83 ≈ 0.916. The other options give the figure for "
                    "leaving out signal 1 (0.478) or signal 3 (0.140) or swap the "
                    "two."},
            {"q": "On collector-changed, alpha is 0.610. Which signal's removal "
                  "brings it back above 0.70?",
             "a": ["Signal 1, giving 0.245", "Signal 2, giving 0.448",
                   "Signal 3, giving 0.320", "Signal 4, giving 0.923"],
             "c": 3,
             "why": "Removing signal 4 leaves the three untouched signals, whose "
                    "alpha is 927/1004 ≈ 0.923. Removing any of the others leaves "
                    "the changed signal in, and alpha falls, to 0.245, 0.448 or "
                    "0.320, all below the cutoff."},
            {"q": "A change to the code that collects one metric alters that metric. "
                  "What does Chapter 13 say several metrics give you?",
             "a": ["A better chance of detecting the change",
                   "Automatic correction of the altered metric",
                   "Freedom from checking the metrics again",
                   "Measures that are no longer proxies"],
             "c": 0,
             "why": "The chapter says that with one metric the likelihood of "
                    "catching the change is low, and with several the change has "
                    "a better chance of being detected. It adds that measures "
                    "should be rechecked from time to time, and that all "
                    "measures are proxies, system data included."},
        ],
        "mistakes": [
            ("Reading a high alpha as proof that the signals measure strain",
             "Alpha measures whether the signals agree, not whether they "
             "measure what you named. Four signals that all follow traffic "
             "would score well. Chapter 13's first benefit, defining what you "
             "mean before you choose the measures, is what alpha cannot "
             "supply."),
            ("Expecting alpha to raise the alarm for every broken signal",
             "A signal whose collector changed so that its readings jump about "
             "pulls alpha down, as the second preset shows. One that freezes "
             "does not: in this sample alpha is 0.924, slightly higher. Alpha is one test "
             "among several, and the chapter's advice to check the measures "
             "periodically stands."),
            ("Judging a short scale by alpha alone",
             "Appendix C says alpha penalises scales with few items. With the "
             "same average correlation of 0.5 between items it is 0.667 for two "
             "items and 0.80 for four. That is why the authors also ran "
             "composite reliability, and every construct met the cutoff on one or the other."),
        ],
        "standard": (
            "Finish when you can compute and read Cronbach's alpha.",
            "Given a table of signals over several days, find alpha by sums of "
            "squares, say whether it meets 0.70, and find which signal's "
            "removal changes it most."
        ),
        "note": (
            "The lab computes alpha for the table you type. It cannot tell whether "
            "the signals measure what you named, whether eight days is enough, or "
            "why a signal went wrong; the book's answer to the first is a clear "
            "definition, and to the last is to check the collector."
        ),
    },
]
