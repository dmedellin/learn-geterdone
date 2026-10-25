"""Course 7, lessons 1-4 -- free recall, retrieval against rereading, spacing, summaries."""

from reading.passages import PASSAGES

LESSONS = [
    # ---------------------------------------------------------------- 1
    {
        "slug": "free-recall",
        "title": "Free Recall",
        "module": "Recall",
        "one_line": "Write down what a passage said with the page hidden, and count how much of it you kept.",
        "summary": (
            "Read a passage at your usual pace, then write everything you remember with "
            "the page hidden, and tick the passage's twelve idea units that your writing "
            "contains. The share you tick is your recall, and your rate times that share "
            "is a recall-adjusted rate. Free recall asks more of memory than picking the "
            "right answer from four does."
        ),
        "key": [
            "recall = units ticked / units",
            "recalled rate = rate × recall",
            "7 of 12 units ≈ 58.3%",
            "240 × 7/12 = 140 words a minute",
            "recall is harder than recognition",
        ],
        "key_label": "Free recall in five lines",
        "concepts_intro": (
            "Every drill so far has asked questions with four answers to choose from. "
            "This one asks you to produce the answers yourself, which is a different "
            "test and a harder one."
        ),
        "concepts": [
            ("An idea unit is one thing the passage said",
             "The passage comes with a list of twelve short statements, each one claim "
             "the text makes: the hump stores fat, not water; the droppings are dry "
             "enough to burn. Your writing is scored by how many of them it holds in "
             "substance, whatever words you used."),
            ("Recall and recognition",
             "Choosing the right option from four is recognition: the answer is on the "
             "screen and you only have to know it when you see it. Writing down what "
             "you remember is recall: nothing on the screen helps. Recall scores lower "
             "for the same reading, and is closer to what you can use once the text "
             "is gone."),
            ("A recall-adjusted rate",
             "The effective rate multiplies your rate by the share of questions you got "
             "right. This drill multiplies it by the share of idea units you recalled "
             "instead: the words a minute of reading that you could still give back in "
             "your own words."),
        ],
        "read_title": "What the drill measures",
        "read_intro": (
            "Recall is the strictest test of a reading this Subject uses, and you score "
            "it yourself, so the rules for scoring matter as much as the reading."
        ),
        "body": [
            ("p", "The drill below times one reading of How a Camel Saves Water, a "
                  "passage of 383 words, at your usual pace. When you press Done the "
                  "passage disappears and a box opens: write down everything you "
                  "remember, in any order, in notes or in sentences. Press Finished "
                  "writing, and the passage's twelve idea units appear under what you "
                  "wrote. Tick each one your writing contains, then press Score."),
            ("p", "Tick a unit when your writing has its substance. &ldquo;The hump is "
                  "fat&rdquo; earns the first unit; &ldquo;something about the "
                  "hump&rdquo; does not. A unit you could have written but did not "
                  "stays unticked: the drill measures what came back without help, and "
                  "seeing the list is help. The kit never reads your writing, so the "
                  "count is exactly as honest as you are."),
            ("def", ("Recall share",
                     "The <strong>recall share</strong> is the number of idea units "
                     "ticked over the number in the passage. Your rate times the recall "
                     "share is the <strong>recalled rate</strong>, in words a minute: "
                     "the part of your reading you could give back.")),
            ("p", "The typical preset is a reader who took 95.75 seconds over the 383 "
                  "words, a rate of 240 words a minute, wrote 84 words, and ticked 7 of "
                  "the 12 units, 12 words written for each unit recalled. The recall share is 7/12 &asymp; 58.3%, and the "
                  "recalled rate is 240 &times; 7/12 = 140 words a minute. The strong "
                  "preset is the same reading with 10 of the 12 units ticked: "
                  "5/6 &asymp; 83.3%, and 240 &times; 10/12 = 200 words a minute."),
            ("math", [
                "383 × 60 / 95.75 = 240 words a minute",
                "typical:  240 × 7/12 = 140",
                "strong:   240 × 10/12 = 200",
            ]),
            ("p", "After your ticks the drill asks the passage's six multiple-choice "
                  "questions, and the lab prints your score beside the recall share. "
                  "Expect the recall share to be the lower of the two: the typical preset "
                  "pairs 7 of 12 units with 5 of 6 questions. That gap is not a "
                  "contradiction. The two tests ask different things of memory:"),
            ("ul", [
                "a multiple-choice question puts the right answer on the screen, and it "
                "only has to look familiar;",
                "free recall gives you nothing to look at, so a fact you would know if "
                "you saw it does not count;",
                "and recall asks for the passage's own ideas, not for the four options a "
                "question-setter chose.",
            ]),
            ("p", "Roediger and Karpicke (2006) measured what students kept from prose "
                  "passages by free recall, the method this drill uses, and the next "
                  "lesson rests on their result. Recall is the harsher number, and the "
                  "more useful one for a reading you need later: what you can tell "
                  "someone, or act on, when the page is closed."),
            ("p", "There is no published norm for these twelve units, and the units are "
                  "not equal in weight: the hump storing fat is the passage's opening "
                  "claim, while the eyelashes are one item in a list. So the comparison "
                  "that matters is with your own recall on the next passage, scored by "
                  "the same rules. The drill logs this reading as a test, so that Your "
                  "Training Plan can set your first recall beside your last."),
            ("p", "Next, Retrieval Beats Rereading uses this same write-and-tick drill as "
                  "one of two ways to study a passage, and asks which of the two is "
                  "still working two days later."),
        ],
        "lab": ("readkit", {
            "mode": "recall",
            "view": "free",
            "passage": PASSAGES["P43"],
            "kind": "test",
            "questions": True,
            "preset": "typical",
            "presets": [
                {"id": "typical", "label": "Typical: 7 of 12 units",
                 "recalled": 7, "seconds": "95.75", "summaryWords": 84, "correct": 5,
                 "expect": {"reRecall": "7/12 ≈ 58.3%", "reRate": "140 wpm",
                            "reComp": "5/6 ≈ 83.3%"}},
                {"id": "strong", "label": "Strong: 10 of 12 units",
                 "recalled": 10, "seconds": "95.75", "summaryWords": 120, "correct": 6,
                 "expect": {"reRecall": "5/6 ≈ 83.3%", "reRate": "200 wpm",
                            "reComp": "1 = 100%"}},
            ],
            "panel_title": "What one reading kept",
            "panel_intro": (
                "Your measurement, scored by your own ticks. Before you do the drill, "
                "the boxes hold the typical preset: 383 words in 95.75 seconds, 7 of "
                "12 idea units recalled and 5 of 6 questions right afterwards."
            ),
        }),
        "steps_title": "A free recall on another day",
        "steps_intro": "Five steps. The third is the one that keeps the number honest.",
        "steps": [
            ("Read once at your usual pace",
             "Pick a passage of three or four hundred words that you have not read, and "
             "time one reading. Do not slow down to memorise; the point is what an "
             "ordinary reading keeps."),
            ("Write with the page hidden",
             "Close or cover the text and write down everything you remember, in any "
             "order, until nothing more comes. Notes are fine."),
            ("Tick the idea units strictly",
             "Against the drill's list, or a list of the passage's main claims that you "
             "make afterwards, tick each unit your writing has in substance. Something "
             "you only recognise on the list stays unticked."),
            ("Compute the share and the recalled rate",
             "Units ticked over units, then your rate times that share. Compare the "
             "share with your next recall, not with anyone else's."),
            ("Then today's Daily Drill",
             "Run The Daily Drill as usual. A recall drill is slow and sits beside the "
             "practice; it does not replace it."),
        ],
        "worked": {
            "title": "Seven of twelve",
            "intro": [
                "The typical preset: 383 words in 95.75 seconds, and 7 of the passage's "
                "12 idea units ticked.",
            ],
            "lines": [
                "rate = 383 × 60 / 95.75 = 240",
                "recall = 7/12 ≈ 58.3%",
                "recalled rate = 240 × 7/12 = 140",
            ],
            "after": [
                "The reader read at 240 words a minute and could give back 140 words a "
                "minute's worth of the passage in their own words. The strong preset "
                "ticks 10 units: 240 &times; 10/12 = 200.",
            ],
        },
        "quiz_title": "Scoring a recall",
        "quiz": [
            {"q": "A reader takes 120 seconds over a passage of 400 words and ticks 9 of "
                  "its 12 idea units. What is the recalled rate?",
             "a": ["200 words a minute", "150 words a minute",
                   "180 words a minute", "300 words a minute"],
             "c": 1,
             "why": "The rate is 400 &times; 60 / 120 = 200 words a minute, and "
                    "200 &times; 9/12 = 150. 200 is the rate before recall is counted; "
                    "180 would need 9 of 10 units; 300 is 400 &times; 9/12, the words "
                    "rather than the rate."},
            {"q": "Which of these is recognition rather than recall?",
             "a": ["Writing down what a passage said with the page hidden",
                   "Explaining a passage to a friend from memory",
                   "Choosing the right answer from four options",
                   "Listing a passage's main claims before checking them"],
             "c": 2,
             "why": "Only the multiple-choice question puts the answer on the screen; "
                    "the other three ask you to produce it with nothing to look at."},
            {"q": "Your writing says &ldquo;the camel's blood has something special "
                  "about it&rdquo;. The idea unit reads &ldquo;Its oval red blood cells "
                  "keep flowing when the blood thickens.&rdquo; Do you tick it?",
             "a": ["Yes: you remember now, seeing the unit, that the cells are oval",
                   "Yes: your writing is about the same part of the passage",
                   "Yes, if you would have answered a question on blood cells correctly",
                   "No: your writing does not have the unit's substance"],
             "c": 3,
             "why": "The unit's substance is the oval cells and why they matter, and "
                    "the writing has neither. Remembering it on seeing the list, or "
                    "being able to pick it from options, is recognition, which is what "
                    "this drill leaves out."},
            {"q": "A reader answers 6 of 6 questions on a passage and recalls 5 of its 12 "
                  "idea units. Which reading of the two figures is right?",
             "a": ["Recognition and recall measure different things, and recall is "
                   "usually the lower",
                   "The multiple-choice score is wrong and should be ignored",
                   "The reader must have ticked the units wrongly",
                   "The reader has kept the whole passage"],
             "c": 0,
             "why": "Both figures can be true at once: knowing the answers when you see "
                    "them is easier than producing them. Neither score refutes the "
                    "other, and 5 of 12 says the reader could not give back most of the "
                    "passage unaided."},
        ],
        "mistakes": [
            ("Recognising the right answer is remembering it",
             "Multiple choice measures recognition: the answer is on the screen, and "
             "you need only know it when you see it. Free recall is harder, and closer "
             "to what you can use later. A reader who picks four of six right options "
             "may, asked to write the passage down, give back only about half of its "
             "ideas: the typical preset recalls 7 of 12."),
            ("Ticking what the list reminds you of",
             "Once the idea units are on the screen, half-remembered facts feel "
             "familiar, and familiarity is recognition again. Tick only what your "
             "writing contains; a unit you know now but did not write stays unticked, "
             "or the drill has turned back into multiple choice."),
            ("Slowing down to memorise the passage",
             "Knowing a recall test is coming, it is tempting to read at a crawl and "
             "rehearse. That measures a different kind of reading. Read at your usual "
             "pace, so that the share describes what your ordinary reading keeps; the "
             "recalled rate already charges a fast, forgetful reading for what it lost."),
        ],
        "standard": (
            "Finish when you can score a recall and say what it measures.",
            "Given the idea units recalled, the passage's units, its words and the "
            "seconds, compute the recall share and the recalled rate, and say in a "
            "sentence why the same reader scores lower on free recall than on multiple "
            "choice. Both figures right and the reason given is the pass."
        ),
        "note": (
            "One passage on one day: the share depends on the passage's units and on how "
            "strictly you tick, so compare it with your own next recall, not with a "
            "norm. The questions come after the recall, so they cannot prompt it, but "
            "six questions on one passage are a small sample of recognition."
        ),
    },
    # ---------------------------------------------------------------- 2
    {
        "slug": "retrieval-beats-rereading",
        "title": "Retrieval Beats Rereading",
        "module": "Recall",
        "one_line": "Study one passage by reading it twice and another by recalling it once, and test both two days later.",
        "summary": (
            "Read one passage twice through, and another once followed by writing down "
            "what you remember. Two or more days later the Subject offers both passages' "
            "questions with neither passage shown, and the lab computes the difference "
            "between the two delayed scores in points. The question is which way of "
            "studying keeps more once the feeling of fluency has faded."
        ),
        "key": [
            "delayed score = right / 6",
            "difference = recalled − read twice",
            "4/6 − 2/6 = 1/3 ≈ 33.3 points",
            "one question ≈ 16.7 points",
            "the immediate test favours rereading",
        ],
        "key_label": "Rereading against retrieval",
        "concepts_intro": (
            "Rereading is the commonest way to study, and the one that feels most like "
            "learning. This lesson sets it against a recall, on a test taken after the "
            "feeling has gone."
        ),
        "concepts": [
            ("Retrieval practice",
             "Pulling something out of memory with nothing to look at is a way of "
             "studying it, not only a way of testing it. The free recall from the last "
             "lesson, done in place of a second reading, is retrieval practice."),
            ("Immediate and delayed tests disagree",
             "Just after studying, rereading tends to come out ahead: the text is fresh "
             "and it has been met twice. Days later the order tends to reverse. Which "
             "test you take decides which method looks better."),
            ("A comparison of two conditions",
             "Two passages, two ways of studying, one delayed test. The difference "
             "between the two scores is the result, and like every comparison in this "
             "Subject it carries two confounds: the passages differ, and one was read "
             "first."),
        ],
        "read_title": "What the study found, and what your drill can find",
        "read_intro": (
            "This lesson's result arrives in two days. The first day is the study; the "
            "test comes to you."
        ),
        "body": [
            ("p", "The drill has two parts, and both happen today. Condition 1 is The "
                  "Mould on the Plate: read it at your usual pace and press Done, then "
                  "read it again and press Done. There is no test. Condition 2 is The "
                  "Tower That Was Meant to Come Down: read it once, then write what you "
                  "remember with the page hidden and tick its idea units, as in Free "
                  "Recall. When both are logged, the page gives the date the test is "
                  "due, two days on."),
            ("p", "From that date, every page of this Subject shows a banner with a link "
                  "back here, and this page offers the delayed test: both passages' six "
                  "questions, twelve in all, with neither passage shown. It is offered "
                  "once, and it writes your two delayed scores into the boxes. Until "
                  "then the boxes hold the presets, and you can finish the lesson today "
                  "on them and come back for your own figures. The last box, the recall "
                  "at the time, keeps the preset's count after the test: note the "
                  "number of units you ticked when you score the recall today, and type "
                  "it in on the day."),
            ("p", "The design follows Roediger and Karpicke (2006). In their first "
                  "experiment students studied short prose passages either by reading "
                  "them twice, or by reading once and then taking a free-recall test "
                  "with no feedback, and were tested by free recall five minutes, two "
                  "days or a week later. At five minutes the rereaders recalled more, "
                  "about 81% against 75%. At two days the order had reversed, about 54% "
                  "against 68%, and at a week the group that had been tested was still "
                  "ahead."),
            ("p", "The published-shape preset puts those two-day figures in the boxes as "
                  "scores out of 100, rounded and labelled as the study's: 54 for the "
                  "passage read twice, 68 for the passage recalled, a difference of +14 "
                  "points. Its last box holds 75 of 100, the tested group's score on the "
                  "five-minute test, the nearest thing in these figures to a recall at "
                  "the time."),
            ("math", [
                "              5 minutes   2 days",
                "read twice    ≈ 81%       ≈ 54%",
                "recalled      ≈ 75%       ≈ 68%",
                "difference    ≈ −6        ≈ +14 points",
            ]),
            ("p", "The reader-example preset is an illustration, not a study: a reader "
                  "who, two days later, got 2 of 6 right on the passage read twice and 4 "
                  "of 6 on the passage recalled. The difference is "
                  "4/6 &minus; 2/6 = 1/3, about +33.3 points, which is two questions. "
                  "On six questions one question is &asymp; 16.7 points, so a "
                  "one-question difference is not a result, and two questions on one "
                  "pair of passages is still a single measurement."),
            ("p", "Why would rereading win at five minutes? A second reading comes just "
                  "after the first, so every idea has been met twice and the text is "
                  "fresh; the recall group met their passage once and wrote down only "
                  "what they could find, with no feedback on what they missed. One "
                  "reading of the reversal is that what was only fluent fades over two "
                  "days, while what was once retrieved is easier to retrieve again."),
            ("p", "Your drill is a gentler test than theirs. Their final test was free "
                  "recall; yours is multiple choice, a recognition test, which tends to "
                  "show a smaller testing effect, so a small difference on your drill, "
                  "or none, is not a contradiction. And it has the two confounds of every "
                  "comparison here: the two passages differ in content and difficulty, "
                  "and which one you read first may matter."),
            ("p", "So a reader whose result goes the other way has not refuted the "
                  "study, and the study has not refuted them. What the study does settle "
                  "is narrower and still useful: for its students and its passages, the "
                  "way of studying that did better at five minutes did worse at two "
                  "days."),
            ("p", "Rereading also feels better. The second pass is smooth and every "
                  "sentence is familiar, and that fluency is easy to take for knowing. "
                  "That feeling is why the next lesson, Spacing Your Reviews, asks when "
                  "to come back to a text rather than how many times to read it."),
        ],
        "lab": ("readkit", {
            "mode": "recall",
            "view": "delayed",
            "passages": [PASSAGES["P44"], PASSAGES["P45"]],
            "days": 2,
            "kind": "condition",
            "preset": "reader-example",
            "presets": [
                {"id": "reader-example", "label": "Reader example (illustrative): 2 of 6 against 4 of 6",
                 "delA": 2, "delB": 4, "total": 6, "recalled": 7,
                 "expect": {"reDelayedA": "1/3 ≈ 33.3%", "reDelayedB": "2/3 ≈ 66.7%",
                            "reDelayedDiff": "≈ +33.3 points", "reRecallB": "7/11 ≈ 63.6%"}},
                {"id": "published-shape", "label": "Published shape (Roediger and Karpicke 2006, rounded)",
                 "delA": 54, "delB": 68, "total": 100, "units": 100, "recalled": 75,
                 "expect": {"reDelayedA": "27/50 = 54%", "reDelayedB": "17/25 = 68%",
                            "reDelayedDiff": "+14 points", "reRecallB": "3/4 = 75%"}},
            ],
            "panel_title": "Two ways of studying, tested two days later",
            "panel_intro": (
                "Your measurement once the delayed test is done; until then the boxes "
                "hold a preset. The published-shape preset carries the study's rounded "
                "percentages as scores out of 100. On your own test one question is "
                "≈ 16.7 points, and a one-question difference is not a result."
            ),
        }),
        "steps_title": "The comparison on your own texts",
        "steps_intro": "Five steps over two or more days. The third is the hardest to keep.",
        "steps": [
            ("Choose two texts of the same kind",
             "Two articles of similar length and difficulty that you have not read, or "
             "two sections of one long piece. Decide in advance which one you will "
             "reread."),
            ("Reread one, recall the other",
             "Read the first twice through with no test. Read the second once, then "
             "write what you remember with it hidden, and only then look back at it."),
            ("Put the test in the calendar",
             "Two or more days ahead. Until then, do not look at either text."),
            ("Test both cold",
             "On the day, write what you remember of each, or answer questions someone "
             "else has set, and compute the difference in points. Next time, swap which "
             "kind of text gets which method, and which comes first."),
            ("Then today's Daily Drill",
             "Run The Daily Drill as usual; the two readings here do not replace it."),
        ],
        "worked": {
            "title": "Two of six against four of six",
            "intro": [
                "The reader-example preset: two days after studying, 2 of 6 right on the "
                "passage read twice and 4 of 6 on the passage recalled.",
            ],
            "lines": [
                "read twice:  2/6 ≈ 33.3%",
                "recalled:    4/6 ≈ 66.7%",
                "4/6 − 2/6 = 1/3 ≈ 33.3 points",
            ],
            "after": [
                "Two questions' difference, on one pair of passages. The published-shape "
                "preset puts the study's two-day figures in the same boxes: "
                "68 &minus; 54 = 14 points.",
            ],
        },
        "quiz_title": "Reading the delayed test",
        "quiz": [
            {"q": "Two days after studying, a reader scores 3 of 6 on the passage read "
                  "twice and 5 of 6 on the passage recalled. What does the lab print for "
                  "the difference?",
             "a": ["+2 points", "≈ −33.3 points", "≈ +33.3 points", "≈ +66.7 points"],
             "c": 2,
             "why": "5/6 &minus; 3/6 = 2/6 = 1/3, which is &asymp; +33.3 points: the "
                    "recalled passage minus the passage read twice. +2 is the difference "
                    "in questions, not in points, and +66.7 would be four questions."},
            {"q": "In Roediger and Karpicke's first experiment, which group did better "
                  "on the test five minutes after studying?",
             "a": ["The group that had taken a recall test",
                   "The group that had read the passage twice",
                   "Neither; the two scores were equal",
                   "There was no five-minute test, only later ones"],
             "c": 1,
             "why": "At five minutes the rereaders were ahead, about 81% against 75%. "
                    "The order reversed at two days, about 54% against 68%."},
            {"q": "On your own delayed test the passage you read twice scores one "
                  "question more than the passage you recalled. What follows?",
             "a": ["One question is ≈ 16.7 points, so the difference is not a result, "
                   "and the study is not refuted",
                   "Retrieval practice does not work for you",
                   "The study was wrong about delayed tests",
                   "You should reread every text twice from now on"],
             "c": 0,
             "why": "A one-question difference on one pair of passages is inside what "
                    "the passages and the order alone could produce. It neither refutes "
                    "the study nor shows that the method fails for you."},
            {"q": "Why might your drill show a smaller difference than the study did?",
             "a": ["Its test comes sooner than the study's two days",
                   "It lets you see the passages during the test",
                   "It gives the recalled passage no idea units to tick",
                   "Its delayed test is multiple choice, where testing effects tend to "
                   "be smaller"],
             "c": 3,
             "why": "The study's final test was free recall; the drill's is recognition, "
                    "which tends to show a smaller effect. The drill waits at least two "
                    "days, hides both passages and has idea units on the recalled side, "
                    "so the other three are false."},
        ],
        "mistakes": [
            ("Reading it again is the best way to remember it",
             "Rereading wins on an immediate test and loses on a delayed one. In "
             "Roediger and Karpicke's first experiment the rereaders recalled about 81% "
             "at five minutes against 75% for the group that had been tested, and about "
             "54% against 68% two days later. Their test was free recall without "
             "feedback; this drill's delayed test is multiple choice, which tends to "
             "show a smaller effect."),
            ("Judging a way of studying by how it feels",
             "The second reading is smooth and familiar, and that fluency feels like "
             "knowing; the recall is effortful and shows you the gaps. The five-minute "
             "test agrees with the feeling and the two-day test does not, which is why "
             "the drill waits two days before it asks."),
            ("Taking one pair of passages as your result",
             "The two passages differ, and you read one before the other. One question "
             "is &asymp; 16.7 points, so a one-question difference is not a result; a "
             "difference that holds on other pairs, with the order swapped, is "
             "evidence about you."),
        ],
        "standard": (
            "Finish when you can compute the delayed difference and explain the reversal.",
            "Given the delayed scores of a passage read twice and a passage recalled, "
            "compute both shares and the difference in points, say whether one question "
            "could account for it, and explain why an immediate test would have favoured "
            "rereading. The figures right, with the reason, is the pass."
        ),
        "note": (
            "Two passages and one delayed test: the passages differ in content and "
            "difficulty, and which you read first may matter, so one result in either "
            "direction is one measurement. The study was a laboratory task with students "
            "and short prose passages; your drill's delayed test is a recognition test, "
            "which tends to show a smaller effect."
        ),
    },
    # ---------------------------------------------------------------- 3
    {
        "slug": "spacing-your-reviews",
        "title": "Spacing Your Reviews",
        "module": "Keeping it",
        "one_line": "Lay out review days from a first gap and a multiplier, and set spaced reviews against one massed session.",
        "summary": (
            "A review schedule is a first gap, a rule for the next gap, a number of "
            "reviews and their length. Compute the days the reviews fall on and the "
            "minutes they cost, for gaps that double, gaps that stay equal and reviews "
            "crammed into one day. Spaced review keeps more at a delay than massed "
            "review; whether the gaps should grow is less settled."
        ),
        "key": [
            "review day = the sum of the gaps so far",
            "gaps 1, 2, 4, 8, 16 → days 1, 3, 7, 15, 31",
            "minutes = reviews × minutes each",
            "5 × 10 = 50 minutes",
            "spaced keeps more than massed",
        ],
        "key_label": "A schedule in five lines",
        "concepts_intro": (
            "What you read fades, and a review slows the fading. The question here is "
            "when to review, not how often."
        ),
        "concepts": [
            ("Spaced and massed",
             "Massed review is all of it in one sitting; spaced review divides the same "
             "minutes among sessions with gaps between them. The total can be the same; "
             "what changes is when."),
            ("A schedule is arithmetic",
             "Take a first gap and multiply each gap by the same number to get the next. "
             "The review days are the running totals of the gaps: gaps of 1, 2, 4, 8 and "
             "16 days put reviews on days 1, 3, 7, 15 and 31."),
            ("Expanding or equal",
             "Gaps that grow are one reasonable choice, and gaps that stay the same "
             "are another. The evidence that spacing helps is strong; the evidence that "
             "the gaps should grow is mixed."),
        ],
        "read_title": "When to come back to a text",
        "read_intro": (
            "A schedule is a handful of additions. The research says which kind of "
            "schedule to choose, and how firmly."
        ),
        "body": [
            ("p", "If the delayed test from Retrieval Beats Rereading is due, this page "
                  "shows its banner in place of the warm-up: take the test first, from "
                  "the link, and come back. Otherwise the warm-up reading above the "
                  "panel is today's timed reading, a hard passage with six questions, "
                  "logged as practice; another visit serves a second one."),
            ("p", "The first measurements of forgetting were Hermann Ebbinghaus's, "
                  "published in 1885. Testing his own memory for lists of nonsense "
                  "syllables, he measured how quickly it faded, and he reported that "
                  "learning spread over several days held better than the same learning "
                  "massed together."),
            ("p", "Cepeda and colleagues (2006) gathered the later studies of verbal "
                  "recall into one review. Spaced practice beat massed practice, and the "
                  "best gap grew with how long the material had to be remembered: the "
                  "longer you need a text, the longer the gaps between reviews can be."),
            ("p", "The expanding preset is the schedule the lab opens with: a first gap "
                  "of 1 day, each gap twice the last, five reviews of 10 minutes. The "
                  "gaps are 1, 2, 4, 8 and 16 days, so the reviews fall on days 1, 3, 7, "
                  "15 and 31, and they cost 5 &times; 10 = 50 minutes."),
            ("math", [
                "gaps:   1   2   4   8   16",
                "days:   1   3   7   15  31",
                "5 × 10 = 50 minutes",
            ]),
            ("p", "The equal preset spends the same 50 minutes with a first gap of 6 days "
                  "and a multiplier of 1, so every gap is 6 days: reviews on days 6, 12, "
                  "18, 24 and 30. It ends near the same day as the expanding schedule, "
                  "with its gaps all the same size."),
            ("p", "The massed preset spends the 50 minutes the other way: a first gap of "
                  "1 day and a multiplier of 0, so every later gap is 0 and all five "
                  "reviews fall on day 1, one after another. (The lab takes no first gap "
                  "of 0, so day 1 stands for the day of the cramming; what matters is "
                  "that the five reviews share one day.)"),
            ("p", "Massed review is the one that feels best. By the fifth pass in a row "
                  "the text is fluent, a self-test during the session scores high, and "
                  "each review is easier than the last. Spaced reviews feel worse, "
                  "because each one starts with something forgotten. The spaced schedule "
                  "is the one retained better at a delay (Cepeda et al. 2006)."),
            ("p", "Should the gaps grow? Expanding gaps are one reasonable schedule, but "
                  "they are not what the review found. On expanding against equal gaps "
                  "the evidence is mixed: Karpicke and Roediger (2007) found that "
                  "expanding retrieval helped retention in the short term, and that "
                  "equally spaced retrieval did as well or better over the longer term."),
            ("p", "A review of a reading is best done as the last lesson suggests: a "
                  "free recall with the text closed, then a look back at what you "
                  "missed, rather than a reread. Ten minutes covers an article."),
            ("p", "Next, Notes in Your Own Words turns the recall into something you "
                  "keep: a short summary written from memory, counted by the idea units "
                  "it holds."),
        ],
        "lab": ("readkit", {
            "mode": "recall",
            "view": "schedule",
            "warmup": [PASSAGES["Q24"], PASSAGES["Q29"]],
            "warmup_kind": "practice",
            "preset": "expanding",
            "presets": [
                {"id": "expanding", "label": "Expanding: gaps doubling from 1 day",
                 "first": 1, "mult": 2, "reviews": 5, "minutes": 10,
                 "expect": {"reDays": "1, 3, 7, 15, 31", "reLastDay": "day 31",
                            "reMinutes": "50 min"}},
                {"id": "equal", "label": "Equal: a gap of 6 days each time",
                 "first": 6, "mult": 1, "reviews": 5, "minutes": 10,
                 "expect": {"reDays": "6, 12, 18, 24, 30", "reLastDay": "day 30",
                            "reMinutes": "50 min"}},
                {"id": "massed", "label": "Massed: all five reviews on day 1",
                 "first": 1, "mult": 0, "reviews": 5, "minutes": 10,
                 "expect": {"reDays": "1, 1, 1, 1, 1", "reLastDay": "day 1",
                            "reMinutes": "50 min"}},
            ],
            "panel_title": "When the reviews fall, and what they cost",
            "panel_intro": (
                "A stated schedule, computed: the days are the running totals of the "
                "gaps, and each gap is the last one times the multiplier. The lab says "
                "when the reviews fall, not what they will keep."
            ),
        }),
        "steps_title": "Planning reviews for a text you need",
        "steps_intro": "Five steps. The second is a choice, not a formula.",
        "steps": [
            ("Decide how long you need it",
             "A text you need next week and a text you need in a year want different "
             "gaps; the longer you need it, the longer the gaps can be."),
            ("Choose a first gap and a rule",
             "A day, then doubling, is one reasonable start; equal gaps of a few days "
             "are another. Put the review days in your calendar."),
            ("Review by recalling",
             "At each review, write what you remember with the text closed, then check "
             "it against the text and note what you missed."),
            ("Count the minutes",
             "Reviews times minutes each. If the total is more than the text is worth "
             "to you, drop a review rather than closing the gaps."),
            ("Then today's Daily Drill",
             "Run The Daily Drill as usual; the warm-up here does not replace it."),
        ],
        "worked": {
            "title": "Doubling gaps",
            "intro": [
                "First gap 1 day, each gap twice the last, five reviews of 10 minutes.",
            ],
            "lines": [
                "gaps:  1, 2, 4, 8, 16",
                "days:  1, 1 + 2 = 3, 3 + 4 = 7, 7 + 8 = 15, 15 + 16 = 31",
                "minutes:  5 × 10 = 50",
            ],
            "after": [
                "The equal preset reaches day 30 with gaps of 6 days for the same 50 "
                "minutes, and the massed preset spends all 50 on day 1.",
            ],
        },
        "quiz_title": "Laying out a schedule",
        "quiz": [
            {"q": "The first gap is 2 days and each gap is three times the last. On "
                  "which days do four reviews fall?",
             "a": ["2, 6, 18, 54", "2, 8, 26, 80", "2, 5, 8, 11", "3, 9, 27, 81"],
             "c": 1,
             "why": "The gaps are 2, 6, 18 and 54; the days are their running totals: 2, "
                    "2 + 6 = 8, 8 + 18 = 26, 26 + 54 = 80. The first option lists the "
                    "gaps, not the days."},
            {"q": "Four reviews of 15 minutes all on one evening, against the same four "
                  "spread over a month. What does the research the lesson cites predict "
                  "for a test a month later?",
             "a": ["The massed reviews do better, because they felt more fluent",
                   "No difference, because the minutes are the same",
                   "The massed reviews do better if the test is multiple choice",
                   "The spread reviews are retained better"],
             "c": 3,
             "why": "Spaced practice beats massed practice at a delay (Cepeda et al. "
                    "2006), for the same total time. Fluency during the session is the "
                    "feeling the misconception mistakes for retention."},
            {"q": "What did Karpicke and Roediger (2007) find about expanding and "
                  "equal gaps?",
             "a": ["Equally spaced retrieval did as well or better over the longer term",
                   "Expanding gaps beat every other schedule at every delay",
                   "Spacing made no difference to long-term retention",
                   "Massed retrieval beat both spaced schedules"],
             "c": 0,
             "why": "Expanding retrieval helped in the short term; equally spaced "
                    "retrieval did as well or better over the longer term. Both are "
                    "spaced, and neither finding favours massing."},
        ],
        "mistakes": [
            ("Massed review works better, because it feels better",
             "Review crammed into one sitting feels fluent and produces high scores "
             "during the session; spaced review is retained better at a delay (Cepeda "
             "et al. 2006). The massed and the expanding presets both cost 50 minutes; "
             "only the second spreads them to day 31."),
            ("Taking the expanding schedule to be the proven one",
             "Doubling gaps are one reasonable schedule, not a finding. The evidence for "
             "spacing is strong; on expanding against equal gaps it is mixed, and "
             "Karpicke and Roediger (2007) found equal gaps as good or better over the "
             "longer term."),
            ("Reviewing by rereading",
             "A review that rereads the text is a second reading, with the fluency "
             "problem of Retrieval Beats Rereading. Recall first with the text closed, "
             "then check: the review is then a retrieval, spaced."),
        ],
        "standard": (
            "Finish when you can lay out a schedule and its cost.",
            "Given a first gap, a multiplier and a number of reviews, list the review "
            "days as running totals of the gaps and compute the minutes, and say which "
            "of a spaced and a massed plan of the same minutes is retained better at a "
            "delay. The days, the minutes and the comparison right is the pass."
        ),
        "note": (
            "The schedule is arithmetic, not a measurement: the lab computes when the "
            "reviews fall, not what they will keep. The spacing studies used word lists, "
            "facts and short texts under laboratory conditions; which gaps suit your "
            "reading only a delayed test of your own can show."
        ),
    },
    # ---------------------------------------------------------------- 4
    {
        "slug": "notes-in-your-own-words",
        "title": "Notes in Your Own Words",
        "module": "Keeping it",
        "one_line": "Write a three-sentence summary from memory, and count how many of the passage's ideas it holds for its length.",
        "summary": (
            "Read a passage once, then write a summary of three sentences with the page "
            "hidden and tick the idea units it contains. The units over the passage's "
            "ten give its coverage, and the words written over the units give its cost. "
            "A summary written from memory is a retrieval, and the question is what a "
            "good one leaves out."
        ),
        "key": [
            "coverage = units in summary / units",
            "words per unit = words / units",
            "40 / 6 ≈ 6.7 words per unit",
            "90 / 4 = 22.5 words per unit",
            "write it from memory, then check",
        ],
        "key_label": "A summary in five lines",
        "concepts_intro": (
            "A summary is the notes most readers would take if they took any. This "
            "lesson measures one, and asks when writing it is studying."
        ),
        "concepts": [
            ("Coverage",
             "How many of the passage's idea units the summary holds, over how many the "
             "passage has. Three sentences cannot hold ten units in full, and should "
             "not try."),
            ("Cost",
             "Words written per unit recalled. A summary that spends many words on each "
             "idea has kept the passage's sentences rather than compressing them."),
            ("Written from memory",
             "A summary written with the text open is copying. Written with the text "
             "hidden, it is a recall, and recalling is the kind of study the research "
             "rates highly."),
        ],
        "read_title": "What a summary is for",
        "read_intro": (
            "Three sentences force a choice. The drill counts what you chose to keep "
            "and what it cost."
        ),
        "body": [
            ("p", "The drill times one reading of Where Autumn Colours Come From, 377 "
                  "words, at your usual pace. When you press Done the passage disappears "
                  "and the box asks for a summary of three sentences in your own words. "
                  "Write it, press Finished writing, and tick the passage's ten idea "
                  "units that your summary holds. The kit counts the words you wrote."),
            ("p", "The tight preset is a summary of 40 words that holds 6 of the 10 "
                  "units: coverage 6/10 = 60% (the lab prints it reduced, 3/5), and "
                  "40 / 6 &asymp; 6.7 words per unit. "
                  "The copied preset is a summary of 90 words that holds 4 units: 40%, "
                  "and 90 / 4 = 22.5 words per unit. Both readers took 94.25 seconds "
                  "over the 377 words, 240 words a minute, so their recalled rates are "
                  "144 and 96 words a minute."),
            ("math", [
                "tight:   40 / 6 ≈ 6.7 words per unit,  6/10 = 60%",
                "copied:  90 / 4 = 22.5 words per unit,  4/10 = 40%",
            ]),
            ("p", "The copied summary is more than twice as long and holds fewer ideas. "
                  "Picture it as the passage's opening, nearly word for word: the "
                  "chlorophyll, the sunlight, the sugar, the summer's repairs, and the "
                  "three sentences have run out before the reds and the falling leaves. "
                  "The tight summary names the cause and the colours and stops."),
            ("p", "So what does a good summary leave out? Roughly, anything whose loss "
                  "leaves the passage's claims standing:"),
            ("ul", [
                "examples, once the claim they illustrate is kept: the maple and the "
                "birch can go once the green is explained;",
                "the members of a list, when what they are a list of will do: that "
                "brown is what is left when the other pigments break down can stay, "
                "and the word tannins can go;",
                "detail of a mechanism that the main claim does not need: the layer "
                "of cells at the base of the leaf stalk;",
                "and the passage's own phrasing.",
            ]),
            ("p", "Dunlosky and colleagues (2013) rated common learning techniques by "
                  "how well the evidence supports them. They rated highlighting, "
                  "rereading and summarisation all of low utility, and practice testing "
                  "and distributed practice high. Summarisation helped learners who "
                  "had been trained to do it well, and untrained summaries helped little."),
            ("p", "That answers the misconception. Highlighting marks a text while you "
                  "look at it, and a summary copied from the open page is little more. "
                  "A summary written from memory, with the passage hidden, is a "
                  "different act: it turns the summary into retrieval practice, the kind "
                  "of study the review rated high, and that is what this drill makes it."),
            ("p", "The drill logs your reading as other, apart from the free recall "
                  "from Free Recall, so a summary does not enter your recall tests. The "
                  "two shares are not the same measure: a three-sentence "
                  "summary is not asked to hold every unit, so expect a lower share "
                  "here, and compare a summary with your next summary."),
            ("p", "That ends Remembering What You Read. The next course, Your Training "
                  "Plan, puts your log to work, beginning with A Practice Week, which "
                  "reviews the routine you have kept since The Daily Drill and plans the "
                  "week ahead."),
        ],
        "lab": ("readkit", {
            "mode": "recall",
            "view": "free",
            "passage": PASSAGES["P46"],
            "summary": True,
            "kind": "other",
            "preset": "tight",
            "presets": [
                {"id": "tight", "label": "Tight: 40 words, 6 units",
                 "recalled": 6, "seconds": "94.25", "summaryWords": 40,
                 "expect": {"reRecall": "3/5 = 60%", "reWordsPerUnit": "≈ 6.7 words",
                            "reRate": "144 wpm"}},
                {"id": "copied", "label": "Copied: 90 words, 4 units",
                 "recalled": 4, "seconds": "94.25", "summaryWords": 90,
                 "expect": {"reRecall": "2/5 = 40%", "reWordsPerUnit": "22.5 words",
                            "reRate": "96 wpm"}},
            ],
            "panel_title": "What three sentences kept",
            "panel_intro": (
                "Your measurement, scored by your own ticks; the kit counts the words "
                "you wrote. Before you do the drill, the boxes hold the tight preset: 40 "
                "words holding 6 of the 10 idea units."
            ),
        }),
        "steps_title": "Notes on a text you need",
        "steps_intro": "Five steps. The first and the third are what make it retrieval.",
        "steps": [
            ("Read once, then close the text",
             "Read at your usual pace, to the end, and put the text out of sight before "
             "you write anything."),
            ("Write three sentences from memory",
             "The main claim, the most important reason or mechanism, and what follows "
             "from it, in your own words, without looking back."),
            ("Check against the text",
             "Open it and mark what your summary got wrong or left out that matters. "
             "Add the correction where you can see it later."),
            ("Count units and words",
             "The units the summary holds, and its words per unit. A cost far above the "
             "tight preset's is a sign of sentences kept rather than compressed."),
            ("Then today's Daily Drill",
             "Run The Daily Drill as usual; a summary drill sits beside it."),
        ],
        "worked": {
            "title": "Tight against copied",
            "intro": [
                "Two summaries of the same reading: 40 words holding 6 of 10 units, and "
                "90 words holding 4.",
            ],
            "lines": [
                "tight:   40 / 6 ≈ 6.7 words per unit",
                "copied:  90 / 4 = 22.5 words per unit",
                "coverage:  6/10 = 60% against 4/10 = 40%",
            ],
            "after": [
                "The tight summary spends less than a third as many words on each idea "
                "and holds half as many ideas again.",
            ],
        },
        "quiz_title": "Measuring a summary",
        "quiz": [
            {"q": "A summary of 60 words holds 5 of a passage's 10 idea units. What does "
                  "it cost per unit?",
             "a": ["6 words per unit", "300 words per unit",
                   "12 words per unit", "2 words per unit"],
             "c": 2,
             "why": "60 / 5 = 12 words per unit recalled. 6 divides by all ten units "
                    "rather than the five recalled; 300 multiplies; 2 is 10 / 5."},
            {"q": "How did Dunlosky and colleagues (2013) rate highlighting and "
                  "summarisation?",
             "a": ["Both of low utility",
                   "Highlighting low, summarisation moderate",
                   "Both of moderate utility",
                   "Highlighting moderate, summarisation high"],
             "c": 0,
             "why": "Both were rated low, with rereading; practice testing and "
                    "distributed practice were rated high. A summary written from memory "
                    "is a form of retrieval practice, which is why the drill hides the "
                    "passage."},
            {"q": "Which of these turns writing a summary into retrieval practice?",
             "a": ["Writing it with the passage open beside you",
                   "Writing it with the passage hidden",
                   "Highlighting the key sentences first, then copying them",
                   "Making it as long as the passage's first paragraph"],
             "c": 1,
             "why": "Retrieval means producing the ideas with nothing to look at. With "
                    "the passage open, or copied from highlights, the summary is "
                    "copying, however good it is."},
            {"q": "Summary A has 45 words and holds 5 units; summary B has 30 words and "
                  "holds the same 5. Which is the better trade by this lesson's measure?",
             "a": ["A: it is longer, so it says more",
                   "Neither: they hold the same units, so they are equal",
                   "A: 9 words per unit against 6",
                   "B: 6 words per unit against 9"],
             "c": 3,
             "why": "Same coverage, so the cost decides: 30 / 5 = 6 against "
                    "45 / 5 = 9. A's extra words hold no extra idea, and lower cost is "
                    "the better trade, not the worse."},
        ],
        "mistakes": [
            ("Highlighting is studying",
             "Dunlosky and colleagues (2013) rated highlighting, rereading and "
             "summarisation all of low utility, and practice testing high. Highlighting "
             "marks a text while you look at it. A summary written from memory, with the "
             "passage hidden, is retrieval practice, which is what this drill makes it."),
            ("A longer summary is a better one",
             "The copied preset is more than twice as long as the tight one and holds "
             "fewer units, 4 against 6. Length is cost; a summary is judged by the ideas "
             "it holds for its words, and three sentences force the choice."),
            ("Writing the summary with the text open",
             "With the page in front of you a summary is copying, the low-utility "
             "version. Close the text first, write, and check against it afterwards."),
        ],
        "standard": (
            "Finish when you can compare two summaries and choose.",
            "Given two summaries' word counts and the idea units each holds, compute "
            "each one's coverage and words per unit, choose the better, and name one "
            "kind of thing a good summary leaves out. Both figures right for both "
            "summaries and a reasoned choice is the pass."
        ),
        "note": (
            "One summary of one passage: how many units three sentences can hold depends "
            "on the passage and on how strictly you tick. The drill cannot say whether "
            "your summary will help you on a test next month; Retrieval Beats Rereading "
            "and Spacing Your Reviews say what the research found about that."
        ),
    },
]
