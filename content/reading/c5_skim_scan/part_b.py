"""Course 5, lessons 5-7 -- reading strategically: a book, a pile, a text in two gears."""

from reading.passages import PASSAGES, POOL

MODULE = "Reading strategically"

Q21 = next(p for p in POOL if p["id"] == "Q21")

# The pile for Triaging a Reading List, in the order it arrived. Purpose: tomorrow
# you help decide whether your team moves to a new building. 15,000 words; values
# sum to 36.
PILE = [
    ("Neighbourhood newsletter", 1800, 1),
    ("Minutes of last month's meeting", 1500, 3),
    ("Landlord's lease proposal", 3000, 10),
    ("Parking study", 2100, 3),
    ("Staff survey results", 2400, 6),
    ("History of the building", 2100, 1),
    ("Facilities manager's summary", 1200, 8),
    ("Removal firm's quote", 900, 4),
]


def _plan(*choices):
    return [{"title": t, "words": w, "value": v, "choice": c} for (t, w, v), c in zip(PILE, choices)]


LESSONS = [
    # ---------------------------------------------------------------- 05
    {
        "slug": "inspectional-reading",
        "title": "Inspectional Reading",
        "module": MODULE,
        "one_line": "Inspect the front and back matter of a book against a five-minute limit, and find out what it is about, how it is built and where a topic is treated.",
        "summary": (
            "Before reading a book, find out whether it needs reading and how. Inspect "
            "the title page, contents, preface and index of an imaginary book about "
            "apples for up to five minutes, find five structural answers in them, and "
            "compute the seconds per answer found."
        ),
        "key": [
            "inspect a book before you read it",
            "title, contents, preface, index",
            "per target = seconds / targets found",
            "then: read it all, in part, or not",
        ],
        "key_label": "Inspection in four lines",
        "concepts_intro": (
            "A book announces what it is in a few pages at the front and the back. "
            "Inspection is reading those pages on purpose, against a clock."
        ),
        "concepts": [
            ("Inspectional reading",
             "Adler and Van Doren (1972) made it the second of four levels of reading: "
             "a short, deliberate look at a book to find out what kind of book it is, "
             "what it is about and how it is organised, before deciding how, or "
             "whether, to read it."),
            ("Where the structure lives",
             "The title and subtitle say what the book claims to be; the contents give "
             "its plan; the preface often says who it is for and which parts to read "
             "first; the index says where a topic is treated and how many pages it "
             "gets."),
            ("A decision, not a summary",
             "What an inspection produces is a decision: read the book, read some of "
             "its chapters, or put it back. Five minutes on a book you then decide not "
             "to read is the cheapest reading you will do."),
        ],
        "read_title": "Five minutes with a book",
        "read_intro": (
            "The drill is the scanning drill with a five-minute limit and questions "
            "about a book rather than a timetable."
        ),
        "body": [
            ("p", "The drill is the front and back matter of a book that does not exist: "
                  "The Patient Orchard, a grower's history of the apple, with its title "
                  "page, contents, preface and part of its index, 586 words in all. Press "
                  "Start and a prompt asks a question about the book, such as which "
                  "chapter deals with the insects that attack apple trees. Click the word "
                  "in the document that answers it, or Tab to it and press Enter. There "
                  "are five questions, and the document disappears after five minutes, "
                  "300 seconds, whether you have finished or not; press Skip this one for "
                  "a question you cannot answer. The result is logged as an inspection, "
                  "not a reading."),
            ("p", "The questions are not about apples. They are about the book: which "
                  "edition it is, how it is divided, who it is written for, and where a "
                  "topic sits in it. Those are the questions an inspection answers, and "
                  "the answers are all in pages most readers turn past."),
            ("math", [
                "five-minutes   300 / 4 = 75 s per target found",
                "thorough       210 / 5 = 42 s per target found",
            ]),
            ("p", "The <strong>five-minutes</strong> preset is a reader who found four of "
                  "the five answers before the limit ran out: 300 / 4 = 75 seconds per "
                  "answer found. The <strong>thorough</strong> preset found all five in "
                  "210 seconds, 42 seconds an answer, which is what it can look like when "
                  "a reader goes through the whole contents and the preface at the first "
                  "prompt, and finds the later answers already known."),
            ("p", "Adler and Van Doren's How to Read a Book, in its 1972 revision, names "
                  "four levels of reading, elementary, inspectional, analytical and "
                  "syntopical, and puts inspection before any careful reading. Its first "
                  "part, which they call systematic skimming, is what this drill does: "
                  "the title page, the preface, the contents and the index, looked at on "
                  "purpose, with questions in mind."),
            ("p", "The preface of The Patient Orchard is the part a hurried reader skips, "
                  "and it answers the most. It says the book is written mainly for growers "
                  "with a small garden, that the chapter on pests was largely rewritten "
                  "for this edition, and that a reader who wants only practical advice "
                  "can begin with the fourth and fifth chapters and the calendar. That "
                  "last sentence is the best thing an inspection can find: a reason not "
                  "to start on page one."),
            ("p", "Seconds per target found, which the panel here labels seconds per right "
                  "answer, is the same arithmetic as in Scanning for a Target, and it means "
                  "something a little different here, because these targets need a "
                  "moment's thought about where a book would put a thing. "
                  "The panel also prints the words passed over per second, which is "
                  "beside the point for an inspection: it is not trying to cover the "
                  "text."),
            ("p", "The drill is a book's front and back matter without the book, so it "
                  "leaves out a step Adler and Van Doren also recommend, dipping into a "
                  "few pages and reading the last pages of the main text. On a real book, "
                  "add that, and keep the limit."),
            ("p", "An inspection decides about one book. Triaging a Reading List decides "
                  "about a pile of documents at once, against a time budget."),
        ],
        "lab": ("readkit", {
            "mode": "scan",
            "view": "inspect",
            "passage": PASSAGES["B01"],
            "limit": 300,
            "preset": "five-minutes",
            "presets": [
                {"id": "five-minutes", "label": "Four of five when the five minutes ran out",
                 "found": 4, "wrong": 0, "seconds": 300,
                 "expect": {"scFound": "4 of 5", "scPerTarget": "75 s"}},
                {"id": "thorough", "label": "Five of five in 210 seconds",
                 "found": 5, "wrong": 0, "seconds": 210,
                 "expect": {"scFound": "5 of 5", "scPerTarget": "42 s"}},
            ],
            "panel_intro": (
                "Your measurement: the boxes fill when the inspection ends, at the fifth "
                "question or at 300 seconds; before that they hold a worked example. Each "
                "target is a question about the book, answered by clicking the word in "
                "the document that answers it."
            ),
        }),
        "steps_title": "Inspecting a book of your own",
        "steps_intro": "Five steps, five minutes for the first four.",
        "steps": [
            ("Write three questions and set five minutes",
             "Before you open the book: what is it about, how is it organised, and "
             "where does it treat the topic you care about?"),
            ("Title, contents, preface",
             "Read the title and subtitle, the whole contents, and the preface or "
             "introduction for who the book is for and which parts it says to read "
             "first."),
            ("Index, and a dip",
             "Look up two topics in the index and see how many pages each gets; read a "
             "page from the middle and the last pages of the main text."),
            ("Write the decision",
             "One sentence on what the book is about, one on its plan, and the "
             "decision: read all of it, read named chapters, or put it back."),
            ("Then today's Daily Drill",
             "Finish with today's reading from The Daily Drill."),
        ],
        "worked": {
            "title": "The five-minutes preset",
            "intro": [
                "Four of the five answers found when the five-minute limit ran out.",
            ],
            "lines": [
                "targets found       4 of 5",
                "seconds             300",
                "per target found    300 / 4 = 75 s",
            ],
            "after": [
                "The fifth answer is missing, but the 300 seconds are not: each answer "
                "the reader did find cost 75 of them. The thorough preset's 42 seconds "
                "an answer is what the same document can cost a reader who reads the "
                "contents and preface through at the start.",
            ],
        },
        "quiz_title": "Check the inspection",
        "quiz": [
            {"q": "In The Patient Orchard, which part tells a reader who wants only "
                  "practical advice where to begin?",
             "a": ["The preface", "The index", "The title page", "The dedication"], "c": 0,
             "why": "The preface says to begin with the fourth and fifth chapters and the "
                    "calendar. The index locates topics; it does not say where to start."},
            {"q": "An inspection finds 3 of 5 answers in 240 seconds. What is the time per "
                  "target found?",
             "a": ["80 s", "48 s", "60 s", "120 s"], "c": 0,
             "why": "240 / 3 = 80. 48 divides by the five asked, which hides the cost of "
                    "the two not found."},
            {"q": "In Adler and Van Doren's sense, what does an inspectional reading "
                  "produce?",
             "a": ["A decision about whether and how to read the book",
                   "A summary of every chapter",
                   "A list of the book's errors",
                   "The reader's rate on the book"], "c": 0,
             "why": "Inspection comes before any careful reading and decides whether the "
                    "book needs one, and which parts."},
            {"q": "Why does the panel's words-passed-over figure matter little for an "
                  "inspection?",
             "a": ["An inspection is not trying to cover the text, so the words passed over are not its point",
                   "The document has too few words to count",
                   "The figure is wrong whenever a target is skipped",
                   "Front and back matter are not counted as words"], "c": 0,
             "why": "An inspection looks for structure in a few chosen places; how much "
                    "text went by while it did so is not what it was for."},
        ],
        "mistakes": [
            ("Taking reading a book to mean starting at page one",
             "Adler and Van Doren put an inspection first, and it decides whether the "
             "book needs a whole reading at all. The Patient Orchard's preface tells a "
             "reader who wants practical advice to begin at chapter four, on page 63; "
             "one who started at page one would reach that advice sixty-two pages later."),
            ("Skipping the preface",
             "It is the part of the front matter that most often says who a book is "
             "for and which parts matter. In the drill it answers one question outright "
             "and tells you how the book's two halves, history and practice, relate."),
            ("Inspecting without questions",
             "Five minutes of browsing leave an impression; five minutes with questions, "
             "what is it, how is it built, where is my topic, leave a decision. Write the "
             "questions before you open the book."),
        ],
        "standard": (
            "Finish when you can inspect a book and decide about it within the limit.",
            "Given a book's title page, contents, preface and index, answer five "
            "structural questions about it, such as what it is about, how it is "
            "organised, who it is for, where a topic is treated and which edition it "
            "is, within five minutes, and say whether to read it all, in part or not.",
        ),
        "note": (
            "An imaginary book, five questions and a limit: the drill measures how "
            "quickly you find structural facts in front and back matter, not how well "
            "you judge a real book, which also needs a look inside. The prompts come one "
            "at a time, so the drill is more guided than an inspection on your own."
        ),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "triaging-a-reading-list",
        "title": "Triaging a Reading List",
        "module": MODULE,
        "one_line": "Plan a session through eight documents under a 45-minute budget by choosing to read, skim or skip each one, and compute the time and the value the plan covers.",
        "summary": (
            "Reading a whole pile of eight documents at 250 words a minute takes an hour, "
            "and the budget is 45 minutes. Choose read, skim or skip for each document, "
            "and the lab computes the time the plan takes and the share of the pile's "
            "value it covers, under a stated model of what a skim keeps."
        ),
        "key": [
            "read: words / reading rate",
            "skim: words / skimming rate",
            "a skim covers 1/2 of the value",
            "skip: no time, no value",
            "decide what not to read first",
        ],
        "key_label": "The triage model",
        "concepts_intro": (
            "A reading list is a scheduling problem before it is a reading problem. The "
            "lab states a simple model of it and computes what each plan costs."
        ),
        "concepts": [
            ("Value for a purpose",
             "Each document carries a value, a judgement of how much it bears on what "
             "you are reading for. The values are stated, not computed, and choosing "
             "them is half of triage."),
            ("Three choices and their price",
             "A document read costs its words over your reading rate and yields its "
             "whole value. One skimmed costs its words over a skimming rate and yields "
             "a stated share of its value. One skipped costs and yields nothing."),
            ("Fit, then coverage",
             "A plan first has to fit the budget. Among the plans that fit, the better "
             "one covers more of the value, and reading in the order the pile arrived "
             "is a plan too, usually a poor one."),
        ],
        "read_title": "Eight documents and 45 minutes",
        "read_intro": (
            "A warm-up reading first, then a plan for the pile."
        ),
        "body": [
            ("p", "Start with the warm-up at the top of the lab: a timed reading with six "
                  "questions, logged as practice, so that this lesson, which has no drill "
                  "of its own, still has a reading in it. Then turn to the pile."),
            ("p", "The pile is for a stated purpose: tomorrow you help decide whether your "
                  "team moves to a new building. Eight documents arrived, in the order "
                  "the lab lists them, 15,000 words in all. Each has a value for that "
                  "decision, from 1 for the neighbourhood newsletter to 10 for the "
                  "landlord's lease proposal, 36 in all. The read, skim and skip buttons "
                  "beside each document rewrite the plan, and the tiles recompute."),
            ("p", "The model is plain. A document read costs its words over a reading rate "
                  "of 250 words a minute. One skimmed costs its words over a skimming rate "
                  "of 750 and is credited with half its value. One skipped costs nothing. "
                  "The half is an assumption in the spirit of What Skimming Costs, where "
                  "a skim kept the gist better than the detail, and you can change it in "
                  "its box."),
            ("math", [
                "read everything   15,000 / 250 = 60 min        budget 45",
                "in arrival order  10,800 / 250 = 43.2 min      23/36 of the value",
                "triaged           7,500 / 250 + 7,500 / 750 = 40 min   32/36",
            ]),
            ("p", "The <strong>read-everything</strong> preset is the plan most piles get: "
                  "60 minutes, 15 over the budget, so in practice the last documents are "
                  "never reached. The <strong>skip-wrong</strong> preset is what that "
                  "looks like: read in the order they came until the time runs out, "
                  "which gets through the staff survey and stops, 43.2 minutes with 1.8 "
                  "to spare, and covers 23 of the 36, about 63.9%, without ever opening "
                  "the facilities manager's summary, the second most valuable document "
                  "in the pile. The <strong>skim-the-rest</strong> preset reads the four "
                  "documents worth 4 or more, skims the other four, and takes 40 minutes "
                  "with 5 to spare, covering 32/36 = 8/9, about 88.9%."),
            ("p", "Now compare that with reading faster. To read the whole pile in 45 "
                  "minutes you would need 15,000 / 45 ≈ 333.3 words a minute, a third "
                  "faster than 250, with the same understanding, and no lesson in this "
                  "Subject promises that. The triaged plan came in under the budget with "
                  "nearly nine-tenths of the value at the rate you already have. Skip the "
                  "four low documents instead of skimming them and it takes 30 minutes "
                  "and covers 28/36 = 7/9, about 77.8%."),
            ("p", "Duggan and Payne (2009) studied readers with more text than time, "
                  "enough for half of each text: those who skimmed all of it remembered "
                  "more of its important ideas than those who read half of it, because "
                  "they chose where to look, and the advantage depended on how easily "
                  "they could move around the text. A reading list asks for the same "
                  "choice one level up, between documents instead of within one."),
            ("p", "The plan is only as good as its values. If the parking study matters "
                  "more to your team than it does here, change its value and the plan; "
                  "the lab recomputes. In this pile the time was saved by the documents "
                  "not read in full, not by the speed at which the others were read."),
            ("p", "Triage decides how much of each text to read. Shifting Gears, the last "
                  "lesson of the course, asks whether you change speed within a text when "
                  "its difficulty changes."),
        ],
        "lab": ("readkit", {
            "mode": "triage",
            "view": "plan",
            "warmup": Q21,
            "preset": "skim-the-rest",
            "presets": [
                {"id": "read-everything", "label": "Read all eight",
                 "items": _plan("read", "read", "read", "read", "read", "read", "read", "read"),
                 "budget": 45,
                 "expect": {"trMinutes": "60 min", "trCovered": "1 = 100%",
                            "trFits": "over the budget by 15 min"}},
                {"id": "skip-wrong", "label": "Read in the order they came until time runs out",
                 "items": _plan("read", "read", "read", "read", "read", "skip", "skip", "skip"),
                 "budget": 45,
                 "expect": {"trMinutes": "43.2 min", "trCovered": "23/36 ≈ 63.9%",
                            "trFits": "fits, 1.8 min to spare"}},
                {"id": "skim-the-rest", "label": "Read the four worth most, skim the rest",
                 "items": _plan("skim", "skim", "read", "skim", "read", "skim", "read", "read"),
                 "budget": 45,
                 "expect": {"trMinutes": "40 min", "trCovered": "8/9 ≈ 88.9%",
                            "trFits": "fits, 5 min to spare"}},
            ],
        }),
        "steps_title": "Triaging your own pile",
        "steps_intro": "Five steps, and the reading starts only at the fourth.",
        "steps": [
            ("Write the purpose",
             "One sentence: what the reading is for, and when it is needed."),
            ("List and value the pile",
             "Each document with its rough length and a value from 1 to 10 for that "
             "purpose. Do this before you read any of them."),
            ("Read, skim or skip",
             "Read the highest values, skim the middle and skip the lowest, and add up "
             "the time at your own rates until the plan fits the budget with a little "
             "to spare."),
            ("Read in order of value",
             "Work through the plan from the most valuable down, so that if the time "
             "runs out, it is the least valuable that goes."),
            ("Then today's Daily Drill",
             "Finish with today's reading from The Daily Drill."),
        ],
        "worked": {
            "title": "The skim-the-rest preset",
            "intro": [
                "Read the lease proposal, the staff survey, the facilities summary and "
                "the removal quote; skim the other four.",
            ],
            "lines": [
                "read   3,000 + 2,400 + 1,200 + 900 = 7,500 words",
                "       7,500 / 250 = 30 min",
                "skim   1,800 + 1,500 + 2,100 + 2,100 = 7,500 words",
                "       7,500 / 750 = 10 min",
                "value  10 + 6 + 8 + 4 + (1 + 3 + 3 + 1) / 2 = 32",
                "       32 / 36 = 8/9 ≈ 88.9%, in 40 of 45 min",
            ],
            "after": [
                "Half the words were read and half skimmed, and the skimmed half carried "
                "only 8 of the 36 points of value. That asymmetry, not a faster rate, is "
                "what got the pile under the budget.",
            ],
        },
        "quiz_title": "Check the plan",
        "quiz": [
            {"q": "A pile of 9,000 words, a reading rate of 250 words a minute and a "
                  "30-minute budget. Reading everything takes",
             "a": ["36 minutes, 6 over the budget", "30 minutes exactly",
                   "24 minutes, 6 to spare", "12 minutes"], "c": 0,
             "why": "9,000 / 250 = 36 minutes. The 12 minutes is the whole pile at the "
                    "skimming rate of 750, which is not reading it."},
            {"q": "In the lab's model, skimming a 1,500-word document worth 6, at 750 words "
                  "a minute with a skim covering half the value, costs and covers",
             "a": ["2 minutes and 3 points of value", "6 minutes and 6 points of value",
                   "2 minutes and 6 points of value", "6 minutes and 3 points of value"], "c": 0,
             "why": "1,500 / 750 = 2 minutes, and half of 6 is 3."},
            {"q": "Why did reading in the order of arrival cover only about 63.9% of the "
                  "value?",
             "a": ["It spent the budget on low-value documents before reaching high-value ones",
                   "Its reading rate was slower than the triaged plan's",
                   "It skimmed the documents it should have read",
                   "It went over the budget"], "c": 0,
             "why": "Both plans read at 250 and both fit. The order of arrival put the "
                    "newsletter first and left the facilities summary for later, and "
                    "later never came."},
            {"q": "Which saves more time on the 15,000-word pile at 250 words a minute: "
                  "reading 10% faster, or skipping the newsletter and the building history?",
             "a": ["Skipping the two, about 15.6 minutes against about 5.5",
                   "Reading faster, about 15.6 minutes against about 5.5",
                   "They save about the same time",
                   "Neither saves any time, because both plans read every document"], "c": 0,
             "why": "15,000 / 275 ≈ 54.5 minutes saves about 5.5. Skipping 1,800 + 2,100 "
                    "= 3,900 words saves 3,900 / 250 = 15.6 minutes, and loses 2 of 36 "
                    "points of value."},
        ],
        "mistakes": [
            ("Thinking the fastest way through a pile is to read faster",
             "Reading the whole pile in 45 minutes would need about 333.3 words a "
             "minute, a third faster than 250. Reading four documents and skimming four "
             "fits at 250 with 5 minutes to spare and 8/9 of the value. Choosing what "
             "not to read saved more time here than a rate gain you could count on."),
            ("Working through a pile in the order it arrived",
             "The order of arrival is nobody's judgement of value. In the skip-wrong "
             "preset it put the newsletter first and left the facilities manager's "
             "summary, worth 8, unread."),
            ("Forgetting that the values are yours",
             "The lab computes the plan from the values you state, and a wrong value "
             "produces a confident wrong plan. Value the pile for the purpose before "
             "you open any of it."),
        ],
        "standard": (
            "Finish when you can plan a pile to fit a budget and beat reading it in order.",
            "Given a stack with word counts and values, a budget, and reading and "
            "skimming rates, produce a plan that fits the budget, compute its time and "
            "the share of the value it covers, and show that it covers more than "
            "reading the stack in the order given.",
        ),
        "note": (
            "The model is stated, not measured: a skim's share of the value is set at "
            "one half, the values are judgements, and a real document's value is not "
            "spread evenly through it. The warm-up is a practice reading and fills none "
            "of the plan's boxes."
        ),
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "shifting-gears",
        "title": "Shifting Gears",
        "module": MODULE,
        "one_line": "Read a passage whose second half is far denser than its first, time each half, and see whether you changed speed by choice.",
        "summary": (
            "Read a story about a failing vegetable plot, then the soil laboratory's "
            "report on it, timed separately, with questions on both. Compute the rate "
            "of each section and say whether a slower second section was a shift of "
            "gear the reader chose or a collapse the text forced."
        ),
        "key": [
            "section rate = words × 60 / seconds",
            "a shift: slower, and the facts kept",
            "a collapse: slower, and facts lost",
            "most readers hold one rate (Carver)",
        ],
        "key_label": "Gears in four lines",
        "concepts_intro": (
            "Every reading so far has been one text at one difficulty. This one changes "
            "halfway, and the question is whether your speed changes with it."
        ),
        "concepts": [
            ("Gears",
             "Carver (1990) described five: scanning, skimming, rauding (his word for "
             "ordinary reading for understanding), learning and memorising, each slower "
             "than the last. Shifting gear means choosing one to fit the text and the "
             "purpose."),
            ("A rate per section",
             "The drill times each section, so the panel can give each its own rate. "
             "The rate for the whole passage is a blend of the two and hides the "
             "shift."),
            ("Chosen or forced",
             "A dense section slows everyone down. The slowdown was a choice if the "
             "facts of that section were kept, and a collapse if they were lost. Only "
             "the questions on each section can tell the two apart."),
        ],
        "read_title": "Two sections, two rates",
        "read_intro": (
            "One passage, a story and then a technical report, with the clock split "
            "between them."
        ),
        "body": [
            ("p", "The drill is one passage in two sections. The first is a story: a "
                  "retired woman, her grandson and a vegetable plot that will not grow. "
                  "The second is the soil laboratory's report on that plot, written the "
                  "way such reports are. Read section one, press Next section, read "
                  "section two and press Done; the lab times each. A box then asks "
                  "whether your attention left the text, and six questions follow, three "
                  "on each section. Change speed between the sections if the text asks "
                  "you to: that is the exercise. The reading is logged as a test."),
            ("p", "The panel gives a rate for each section, its words over its seconds, "
                  "and then the whole passage's rate and effective rate. The list under "
                  "the drill shows which questions you got right; the last three are on "
                  "the report."),
            ("math", [
                "flexible   292 × 60 / 60 = 292     286 × 60 / 104 = 165",
                "rigid      292 × 60 / 73 = 240     286 × 60 / 72 ≈ 238.3",
            ]),
            ("p", "The <strong>flexible</strong> preset is a reader who took the 292-word "
                  "story at 292 words a minute, slowed to 165 for the 286-word report, and "
                  "got 5 of 6: the whole passage at about 211.5 words a minute, and an "
                  "effective rate of about 176.2. The <strong>rigid</strong> preset held "
                  "one speed, 240 and about 238.3, got all three story questions and one "
                  "of the three report questions, 4 of 6: a whole rate of about 239.2 and "
                  "an effective rate of about 159.4. The rigid reader finished sooner and "
                  "understood less, and the whole loss was in the dense section."),
            ("p", "A slower second section is not by itself a shift of gear. A reader whose "
                  "rate fell to 165 and whose report questions fell too did not choose to "
                  "slow down; the text slowed them and still beat them. A shift is a "
                  "choice when the rate falls and the questions on the hard section "
                  "hold. That is why the drill asks about both sections, and why the "
                  "attention box is there: a slow section with your mind elsewhere is a "
                  "lapse, not a gear."),
            ("p", "Carver (1990) put his five gears at about 600, 450, 300, 200 and 138 "
                  "standard-length words a minute for the college students he studied, "
                  "and he found that most readers seldom use them. They hold a nearly "
                  "constant rate, their rauding rate, across ordinary texts, and when a "
                  "text is harder, their understanding tends to give way rather than "
                  "their speed. His advice (Carver 1992) was to shift deliberately: down "
                  "into the learning gear for what must be learned, up into skimming for "
                  "what need only be skimmed."),
            ("p", "So the rigid preset is not a poor reader. By Carver's account it is the "
                  "usual one. This lesson asks you to do the unusual thing on purpose, "
                  "and the drill is how you see whether you did. His figures are in "
                  "six-character words for students on his materials; the comparison "
                  "that matters here is between your own two sections."),
            ("p", "That ends the course on reading less of a text, and reading it in the "
                  "right gear. Words, Knowledge and Difficulty, the next course, asks what "
                  "makes a text hard in the first place, starting with your own rate on "
                  "an easy passage and a hard one."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "sections",
            "passage": PASSAGES["P37"],
            "kind": "test",
            "preset": "flexible",
            "presets": [
                {"id": "flexible", "label": "Story 292, report 165, 5 of 6",
                 "seconds1": 60, "seconds2": 104, "correct": 5, "total": 6,
                 "expect": {"drRateS1": "292 wpm", "drRateS2": "165 wpm",
                            "drWpm": "≈ 211.5 wpm", "drErr": "≈ 176.2 wpm"}},
                {"id": "rigid", "label": "One speed, 4 of 6",
                 "seconds1": 73, "seconds2": 72, "correct": 4, "total": 6,
                 "expect": {"drRateS1": "240 wpm", "drRateS2": "≈ 238.3 wpm",
                            "drWpm": "≈ 239.2 wpm", "drErr": "≈ 159.4 wpm"}},
            ],
        }),
        "steps_title": "Shifting gear on purpose",
        "steps_intro": "Five steps, on any text whose difficulty changes.",
        "steps": [
            ("Name the gear before you start",
             "For each part of the text, decide what it is for: to be skimmed, read, or "
             "learned."),
            ("Time the parts",
             "Mark where the hard part starts, and time each part separately."),
            ("Check the hard part",
             "With the text hidden, write down three facts from the hard part. If you "
             "cannot, you did not shift; the text carried you."),
            ("Compare the rates",
             "If the hard part was slower and you kept its facts, that was a shift. If "
             "it was slower and you lost them, slow down further next time, or reread "
             "the part on purpose."),
            ("Then today's Daily Drill",
             "Finish with today's reading from The Daily Drill."),
        ],
        "worked": {
            "title": "The flexible preset",
            "intro": [
                "Section one, 292 words in 60 seconds; section two, 286 words in 104 "
                "seconds; 5 of 6 right.",
            ],
            "lines": [
                "section 1   292 × 60 / 60 = 292 words a minute",
                "section 2   286 × 60 / 104 = 165 words a minute",
                "whole       578 × 60 / 164 ≈ 211.5 words a minute",
                "effective   578 × 60 / 164 × 5/6 ≈ 176.2",
            ],
            "after": [
                "The reader spent 104 of the 164 seconds on the report, almost two-thirds "
                "of the time on half the words, and kept most of it. The whole-passage "
                "rate alone would have hidden both the shift and what it bought.",
            ],
        },
        "quiz_title": "Check the gears",
        "quiz": [
            {"q": "A reader takes 60 seconds over a 300-word easy section and 100 seconds "
                  "over a 300-word dense one. What are the two section rates?",
             "a": ["300 and 180 words a minute", "300 and 300 words a minute",
                   "180 and 300 words a minute", "225 and 225 words a minute"], "c": 0,
             "why": "300 × 60 / 60 = 300 and 300 × 60 / 100 = 180. 225 is the whole "
                    "passage, 600 × 60 / 160, which hides the shift."},
            {"q": "What did Carver find about most readers' rates across ordinary texts?",
             "a": ["They stay nearly constant; readers seldom shift gear",
                   "They change with every change of difficulty",
                   "They rise steadily with practice in skimming",
                   "They are fastest on the hardest texts"], "c": 0,
             "why": "Most readers hold their rauding rate; Carver recommended shifting "
                    "deliberately because most do not."},
            {"q": "A reader slows from 250 to 170 words a minute on a dense section and "
                  "gets none of its three questions right. What is the best reading of "
                  "that?",
             "a": ["The text slowed them without their keeping it: not yet a chosen shift",
                   "A deliberate shift into the learning gear",
                   "Proof that the dense section was badly written",
                   "A rigid reader who held one speed"], "c": 0,
             "why": "A shift is a slowdown that keeps the facts. This one lost them, so "
                    "the reader was slowed, not shifting. They did not hold one speed "
                    "either."},
        ],
        "mistakes": [
            ("Believing a good reader holds one fast speed",
             "Carver found that most readers do hold one speed, their rauding rate, "
             "across ordinary texts, and seldom shift gear; he recommended shifting "
             "deliberately, slowing for what must be learned and speeding up for what "
             "need only be skimmed. The rigid preset held about 240 through both "
             "sections and lost two of the three report questions."),
            ("Counting any slowdown as a shift",
             "A dense section slows everyone. It was a shift if the questions on it "
             "held; in the flexible preset the reader slowed to 165 and got five of six, "
             "and that is the difference."),
            ("Judging by the whole-passage rate",
             "The rigid preset's whole rate, about 239.2, beats the flexible preset's "
             "211.5; its effective rate, about 159.4 against 176.2, does not. The rate "
             "and the questions for each section are what show a gear."),
        ],
        "standard": (
            "Finish when you can tell a chosen shift from a collapse.",
            "Given the words and seconds for each section and the questions right on "
            "each, compute both section rates, and say whether the reader shifted gear "
            "by choice, slower on the hard part with its questions kept, or was slowed "
            "by it and lost them.",
        ),
        "note": (
            "One passage in two sections, read once. The second section is harder and "
            "also second, so part of any slowdown may be the drill's length rather than "
            "the difficulty. Carver's gears are in standard-length words for college "
            "students on his materials; the comparison that matters is between your own "
            "two sections."
        ),
    },
]
