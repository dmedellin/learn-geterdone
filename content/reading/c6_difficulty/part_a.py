"""Course 6, lessons 1-5 -- difficulty, vocabulary, knowledge and volume."""

from reading.passages import PASSAGES, POOL

_POOL = {p["id"]: p for p in POOL}

DAILY = (
    "Then today's Daily Drill",
    "Open The Daily Drill and do today's session as its routine says. When the pool "
    "reaches its hard passages, find your hold target again: it will probably be "
    "lower, and that is this course's subject measured on your own practice.",
)

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "your-rate-on-hard-text",
        "title": "Your Rate on Hard Text",
        "module": "Difficulty",
        "one_line": "Read an easy and a hard passage at your own pace and measure what changed.",
        "summary": (
            "Does your rate stay the same when the text gets harder, or does your "
            "comprehension give way instead? Read an easy passage and a hard one at "
            "your natural pace, answer six questions on each, and compute the ratio "
            "of the two rates and both effective rates."
        ),
        "key": [
            "rate ratio = hard rate / easy rate",
            "effective rate = rate × comprehension",
            "compare both, not the rate alone",
            "a rate is a rate on a kind of text",
        ],
        "key_label": "Easy against hard in four lines",
        "concepts_intro": (
            "Almost every rate in your log so far was measured on standard text. This lesson "
            "asks what one of those rates tells you about a page that is much harder."
        ),
        "concepts": [
            ("Two ways to meet a hard text",
             "A reader can keep their pace and understand less, or slow down and keep "
             "their understanding. The rate alone cannot tell the two apart; the rate "
             "beside the comprehension score can."),
            ("The ratio of two rates",
             "Divide the rate on the hard passage by the rate on the easy one. A ratio "
             "near 1 says the pace held; a ratio well below 1 says it fell. Then look "
             "at the two effective rates, which count only what was understood."),
            ("A rate belongs to a kind of text",
             "A figure measured on easy text is a measurement on easy text. Before you "
             "accept a speed claim, ask what it was read on and whether the questions "
             "were hard enough to catch a reader who kept the pace and lost the sense."),
        ],
        "read_title": "What a hard text does to a rate",
        "read_intro": (
            "Two passages of almost the same length, one written for a young reader "
            "and one in the dense style of a geology textbook."
        ),
        "body": [
            ("p", "Do the drill below before you read on. Read The Octopus at the pace "
                  "you would use if no one were timing you, answer its six questions, "
                  "then do the same with From Drifting Continents to Moving Plates. The "
                  "lab alternates which passage comes first, so follow the order it "
                  "gives you."),
            ("p", "Now put your two readings side by side and look at two things, not "
                  "one: the rates, and the scores. The passages are close in length, 395 "
                  "words and 391, and far apart in difficulty. By the formula the next "
                  "lesson teaches, The Octopus is written at about grade 6.8 and the "
                  "continents passage at about grade 17.3: long sentences, long words, "
                  "and one idea leaning on the last."),
            ("p", "Some readers slow down a long way on the hard passage and keep "
                  "their score. The preset <strong>big-drop</strong> is such a reader: "
                  "395 words in 79 seconds on the easy passage, 300 words a minute with "
                  "6 of 6 right, then 391 words in 138 seconds on the hard one, 170 words "
                  "a minute with 5 of 6. The ratio of the rates is 170/300 = 17/30, about "
                  "56.7%, and the effective rate fell from 300 to about 141.7."),
            ("math", [
                "easy:  395 × 60 / 79  = 300 words a minute, 6/6",
                "hard:  391 × 60 / 138 = 170 words a minute, 5/6",
                "rate ratio = 170 / 300 = 17/30 ≈ 56.7%",
                "hard effective rate = 170 × 5/6 ≈ 141.7",
            ]),
            ("p", "Other readers barely change pace and pay for it in the questions. "
                  "The preset <strong>held-rate</strong> read the easy passage at 250 "
                  "words a minute with 6 of 6 and the hard one at 240 with 3 of 6. The "
                  "rate ratio is 24/25 = 96%, which looks like a reader untroubled by "
                  "difficulty, until you see the effective rates: 250 on the easy "
                  "passage and 120 on the hard one. Half of the hard passage went by "
                  "without being understood, at nearly full speed."),
            ("p", "The second pattern is the one Ronald Carver described. In his 1990 "
                  "review of reading rate he found that readers tend to keep a nearly "
                  "constant rate, which he called the rauding rate, across texts within "
                  "their level, and that when the text gets harder it is their "
                  "comprehension that falls. On text well above their level, readers "
                  "drop into a slower gear, which he called learning, at about 200 "
                  "standard-length words a minute for the college students he studied. "
                  "So how far your rate drops depends on how far above your level the "
                  "hard text is."),
            ("p", "The eye-movement studies show the same difficulty from the inside. "
                  "Rayner's 1998 review reports that on difficult text fixations get "
                  "longer and regressions more frequent: each glance costs more time, "
                  "and more of them go backwards. You met both costs in How the Eyes "
                  "Read; a hard passage raises both at once."),
            ("p", "This is a comparison of two readings, and two readings differ in "
                  "more than difficulty. The passages differ in topic as well as grade, "
                  "and whichever you read second you read a few minutes more practised "
                  "or more tired. One question is about 16.7 points, so a one-question "
                  "difference in the scores is not a result. If your readings go the "
                  "other way from Carver's account, you have not refuted his review, "
                  "and his review has not refuted your readings: it describes readers "
                  "on average, and yours is one pair on one day."),
            ("p", "What this measurement settles is narrower and more useful: a rate "
                  "is a rate on a kind of text. A figure measured on easy text says "
                  "little about how fast you can read a contract, a paper or a manual "
                  "with the sense intact, and a speed claim should be measured on the "
                  "kind of text you need to read, with questions that would catch a "
                  "held rate and a lost meaning."),
            ("p", "The next lesson, Measuring Difficulty, counts the two passages you "
                  "just read the way a readability formula does, and shows what the "
                  "count can and cannot see."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P38"], PASSAGES["P39"]],
            "a": {"label": "Easy text", "kind": "test"},
            "b": {"label": "Hard text", "kind": "test"},
            "ratioOf": "wpm",
            "preset": "big-drop",
            "presets": [
                {"id": "big-drop", "label": "big drop: 300 and 170 words a minute",
                 "wordsA": 395, "secondsA": 79, "correctA": 6, "totalA": 6,
                 "wordsB": 391, "secondsB": 138, "correctB": 5, "totalB": 6,
                 "expect": {"drWpmA": "300 wpm", "drWpmB": "170 wpm", "drRatio": "17/30 ≈ 56.7%", "drErrB": "≈ 141.7 wpm"}},
                {"id": "held-rate", "label": "held rate: 250 and 240, half lost",
                 "wordsA": 395, "secondsA": "94.8", "correctA": 6, "totalA": 6,
                 "wordsB": 391, "secondsB": "97.75", "correctB": 3, "totalB": 6,
                 "expect": {"drWpmA": "250 wpm", "drWpmB": "240 wpm", "drRatio": "24/25 = 96%", "drErrB": "120 wpm"}},
            ],
            "panel_title": "Your easy and hard readings",
            "panel_intro": (
                "Your measurement: two readings at your natural pace, one easy passage "
                "and one hard, each with six questions. The ratio is the hard rate over "
                "the easy rate; read it beside the two effective rates. One question is ≈ 16.7 "
                "points; a one-question difference is not a result."
            ),
        }),
        "steps_title": "Measuring a hard text again",
        "steps_intro": (
            "On another day, with a hard text of your own choosing and an easy one, the "
            "protocol is the same. The third step is the one that is easy to skip."
        ),
        "steps": [
            ("Choose two texts of the same length",
             "One easy and one hard, both new to you, both 350 to 500 words. Count the "
             "words, or paste each into the counter in Measuring Difficulty."),
            ("Read each once at your natural pace",
             "Not as fast as you can: at the pace you would use if no one were timing "
             "you. Time each reading, and note which came first."),
            ("Test your understanding before you compute",
             "Write three sentences on each text with the page out of sight, or have "
             "someone ask you questions. Without a score, a held rate and a lost meaning "
             "look the same."),
            ("Compute the ratio and both effective rates",
             "Hard rate over easy rate, then each rate times its score. Say in a "
             "sentence which pattern you showed: slower and understood, or same pace "
             "and less understood."),
            DAILY,
        ],
        "worked": {
            "title": "The big-drop reader",
            "intro": [
                "A reader reads The Octopus, 395 words, in 79 seconds with 6 of 6 right, "
                "and From Drifting Continents to Moving Plates, 391 words, in 138 seconds "
                "with 5 of 6.",
            ],
            "lines": [
                "easy rate  = 395 × 60 / 79  = 300 words a minute",
                "hard rate  = 391 × 60 / 138 = 170 words a minute",
                "ratio      = 170 / 300 = 17/30 ≈ 56.7%",
                "effective  = 300 × 1 = 300;  170 × 5/6 ≈ 141.7",
            ],
            "after": [
                "This reader slowed to a little over half their easy rate and kept most "
                "of the meaning. The held-rate preset shows the other pattern: a ratio "
                "of 96% and an effective rate that halved.",
            ],
        },
        "quiz_title": "Reading two rates",
        "quiz": [
            {"q": "A reader reads an easy passage at 250 words a minute with 6 of 6 and a "
                  "hard one at 240 with 3 of 6. What does the pair show?",
             "a": ["The reader is untroubled by difficulty, since the rate hardly changed",
                   "The rate held and comprehension fell, so the effective rate halved",
                   "The hard passage was misjudged, since a hard text always slows a reader",
                   "The reader slowed down and kept the meaning"],
             "c": 1,
             "why": "The ratio is 240/250 = 96%, but the effective rates are 250 and 240 × 3/6 "
                    "= 120. The pace held and half the meaning went, which is the pattern "
                    "Carver described for readers who keep their rauding rate."},
            {"q": "On an easy passage of 395 words a reader takes 79 seconds; on a hard one "
                  "of 391 words, 138 seconds. What is the ratio of the hard rate to the easy rate?",
             "a": ["17/30, about 56.7%", "79/138, about 57.2%", "30/17, about 176.5%",
                   "391/395, about 99%"],
             "c": 0,
             "why": "The rates are 395 × 60 / 79 = 300 and 391 × 60 / 138 = 170, and 170/300 "
                    "= 17/30. Dividing the times instead ignores the small difference in "
                    "length, and dividing the word counts ignores the times altogether."},
            {"q": "A course advertises that its graduates read 600 words a minute, measured "
                  "on short magazine pieces with three easy questions. What does that "
                  "measurement tell you about reading a technical report?",
             "a": ["That the graduates read reports at 600 words a minute",
                   "That reports will take them exactly twice as long as the magazine pieces",
                   "Little: it is a rate on easy text, with questions too easy to catch a "
                   "held pace and a lost meaning",
                   "Nothing about rates, since rates cannot be measured on reports"],
             "c": 2,
             "why": "A rate is a rate on a kind of text. Nothing in the advertised figure "
                    "says how the graduates read hard text, and no fixed factor converts "
                    "one kind of text into another; that depends on how far above the "
                    "reader's level the report is."},
        ],
        "mistakes": [
            ("Treating your reading speed as one number",
             "A rate measured on one kind of text is a measurement on that kind of text. "
             "Carver found that readers keep a nearly constant rate across texts within "
             "their level and lose comprehension instead, and that on text well above it "
             "they drop into a slower gear; the eye-movement studies show longer "
             "fixations and more regressions on hard text. Either way, the big-drop and "
             "held-rate readers would each misreport themselves with a single figure."),
            ("Reading the rate ratio without the scores",
             "A ratio of 96% looks like a reader whom difficulty does not touch. The "
             "held-rate preset has that ratio and an effective rate that fell from 250 "
             "to 120. Compare the two effective rates before you say what the hard text "
             "cost."),
            ("Taking one pair of readings as the verdict",
             "The two passages differ in topic as well as difficulty, and one was read "
             "second. A one-question difference is about 16.7 points and is not a "
             "result; repeat the pair on other texts before you trust the pattern."),
        ],
        "standard": (
            "Finish when you can say what a rate on easy text tells you about a hard one.",
            "Given an easy and a hard reading, each with words, seconds and a score, "
            "compute both rates, their ratio and both effective rates, and say in a "
            "sentence which pattern the reader showed and what a speed claim measured "
            "on easy text would and would not tell them about the hard one."
        ),
        "note": (
            "This is one pair of readings on one day. The passages differ in topic as "
            "well as difficulty, and which came first matters too: the second reading "
            "is done a little more practised or a little more tired, which is why the "
            "lab alternates the order. The pattern is worth trusting only after it "
            "repeats on other pairs."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "measuring-difficulty",
        "title": "Measuring Difficulty",
        "module": "Difficulty",
        "one_line": "Count words, sentences and syllables, and compute two readability scores from them.",
        "summary": (
            "A readability formula turns three counts into a score: words, sentences "
            "and syllables. Compute Flesch Reading Ease and the Flesch–Kincaid grade "
            "for the passages you have read, by the kit's counting rule, and see what "
            "the formulas measure and what they cannot see."
        ),
        "key": [
            "W/S = words per sentence",
            "Y/W = syllables per word",
            "ease = 206.835 − 1.015 × W/S − 84.6 × Y/W",
            "grade = 0.39 × W/S + 11.8 × Y/W − 15.59",
            "higher ease, easier; higher grade, harder",
        ],
        "key_label": "Two formulas from three counts",
        "concepts_intro": (
            "You have felt the difference between an easy and a hard passage. A "
            "readability formula puts a number on part of that difference, and only part."
        ),
        "concepts": [
            ("Two counts stand in for difficulty",
             "Both formulas use the average sentence length in words and the average "
             "word length in syllables. Long sentences and long words make a text score "
             "harder; nothing else enters."),
            ("Two scales, one pair of inputs",
             "Flesch Reading Ease runs downward with difficulty: the higher the score, "
             "the easier the text. The Flesch–Kincaid grade runs upward and is read as "
             "a school grade. The same two averages drive both, so they almost always "
             "agree on which of two texts is harder."),
            ("A count, not a judgement",
             "The formulas cannot see whether the ideas are familiar, whether one "
             "sentence depends on the last, or whether the words are common. Short "
             "words about unfamiliar ideas score easy."),
        ],
        "read_title": "Counting a text",
        "read_intro": (
            "Start with the warm-up reading at the top of the lab; then count the "
            "passages you have already read."
        ),
        "body": [
            ("p", "Begin with the warm-up at the top of the lab, Endgame at the Rosedal, "
                  "at your usual pace. It is a practice reading from the Subject's "
                  "passage pool, logged as practice, and it keeps every lesson in this Subject a "
                  "lesson with a timed reading in it."),
            ("def", ("Flesch Reading Ease and the Flesch–Kincaid grade",
                     "With W words, S sentences and Y syllables, Rudolf Flesch's 1948 "
                     "<strong>Reading Ease</strong> is 206.835, less 1.015 times the words "
                     "per sentence, less 84.6 times the syllables per word; the "
                     "<strong>Flesch–Kincaid grade</strong>, derived by Kincaid and "
                     "colleagues in 1975 for Navy enlisted personnel, is 0.39 times the "
                     "words per sentence, plus 11.8 times the syllables per word, less "
                     "15.59. The key lines above give both in symbols.")),
            ("p", "The counts need rules, and the lab states its own. A word is a "
                  "whitespace-separated token with a letter or a digit in it. A sentence "
                  "ends at a full stop, a question mark or an exclamation mark followed "
                  "by a space. Syllables are counted by a rule: the groups of vowels in a "
                  "word, with y as a vowel, less one for a silent e at the end, and at "
                  "least one a word. The rule miscounts some words, so every syllable "
                  "figure is an approximation, and another program's counts will differ "
                  "a little."),
            ("p", "Work the example by hand first. A text of 100 words in 5 sentences "
                  "with 140 syllables has 20 words a sentence and 1.4 syllables a word. "
                  "The preset <strong>by-hand</strong> carries those counts."),
            ("math", [
                "W/S = 100 / 5 = 20      Y/W = 140 / 100 = 1.4",
                "ease  = 206.835 − 1.015 × 20 − 84.6 × 1.4",
                "      = 206.835 − 20.3 − 118.44 = 68.095",
                "grade = 0.39 × 20 + 11.8 × 1.4 − 15.59",
                "      = 7.8 + 16.52 − 15.59 = 8.73",
            ]),
            ("p", "Now the passages. The preset <strong>octopus</strong> counts The "
                  "Octopus: 395 words, 21 sentences and 504 syllables, so about 18.8 "
                  "words a sentence and 1.28 syllables a word, for a reading ease of "
                  "about 79.8 and a grade of about 6.8. The preset "
                  "<strong>continents</strong> counts From Drifting Continents to Moving "
                  "Plates: 391 words, 16 sentences, 775 syllables, about 24.4 words a "
                  "sentence and 1.98 syllables a word, for an ease of about 14.3 and a "
                  "grade of about 17.3. Between them is the preset "
                  "<strong>church-clock</strong>, The Church Clock at Wexley, the first "
                  "passage you timed in Measure Your Reading: 491 words, 21 sentences, "
                  "an ease of about 70.2 and a grade of about 9.3."),
            ("p", "Look at where the difference comes from. The sentences of the hard "
                  "passage are only about a third longer than the easy one's, but its "
                  "words carry more than half as many syllables again, and syllables a "
                  "word are multiplied by 84.6. Most of the gap between 79.8 and 14.3 is "
                  "word length."),
            ("p", "The passages you read for time in this Subject were sorted into bands by "
                  "exactly these counts: easy at grades 5 to 7, standard at 8 to 11, hard at 13 "
                  "and above. That is the honest use of a formula: to sort many texts "
                  "quickly by how long their sentences and words are."),
            ("p", "The formulas cannot see anything else. They do not know whether a "
                  "word is common or rare, so a short technical word counts as easy. "
                  "They do not know whether you know the subject, and they cannot tell "
                  "a passage of separate facts from one in which every sentence depends "
                  "on the one before. A sentence of short words about an idea you have "
                  "never met can score as easy as a nursery rhyme, and What You Already "
                  "Know puts two passages of nearly the same grade side by side to "
                  "measure exactly that."),
            ("p", "The lab also counts your own text: open Count a text of your own, "
                  "paste a few paragraphs of something you are reading this week, and "
                  "compare its grade with the three passages."),
            ("p", "The next lesson, Unknown Words and Coverage, measures one of the "
                  "things the formulas miss: the words in a text that you do not know."),
        ],
        "lab": ("readkit", {
            "mode": "text",
            "view": "readability",
            "passages": [PASSAGES["P38"], PASSAGES["P01"], PASSAGES["P39"]],
            "warmup": _POOL["Q22"],
            "preset": "octopus",
            "presets": [
                {"id": "octopus", "label": "The Octopus (easy)", "passage": "P38", "expect": {"txWords": "395", "txSentences": "21", "txFre": "≈ 79.8", "txGrade": "≈ 6.8"}},
                {"id": "church-clock", "label": "The Church Clock at Wexley (standard)",
                 "passage": "P01", "expect": {"txWords": "491", "txSentences": "21", "txFre": "≈ 70.2", "txGrade": "≈ 9.3"}},
                {"id": "continents", "label": "From Drifting Continents to Moving Plates (hard)",
                 "passage": "P39", "expect": {"txWords": "391", "txSentences": "16", "txFre": "≈ 14.3", "txGrade": "≈ 17.3"}},
                {"id": "by-hand", "label": "by hand: 100 words, 5 sentences, 140 syllables",
                 "words": 100, "sentences": 5, "syllables": 140, "expect": {"txWords": "100", "txSentences": "5", "txFre": "≈ 68.1", "txGrade": "8.73"}},
            ],
            "panel_title": "Three counts and two formulas",
            "panel_intro": (
                "A count over a text: words, sentences and syllables by the kit's stated "
                "rule (vowel groups, less a final silent e, at least one a word), which is "
                "an approximation; then Flesch's Reading Ease and the Flesch–Kincaid grade."
            ),
        }),
        "steps_title": "Scoring a text yourself",
        "steps_intro": "Four steps for any text you want to place, then the day's practice.",
        "steps": [
            ("Count the three things",
             "Words, sentences and syllables, by one rule kept the same for every text. "
             "Paste the text into the lab's counter, or count a 100-word sample by hand."),
            ("Compute the two averages",
             "Words per sentence and syllables per word. Write them down: they are the "
             "whole of what the formulas know about the text."),
            ("Compute both scores",
             "Reading Ease is 206.835, less 1.015 times the words per sentence, less 84.6 "
             "times the syllables per word; the grade is 0.39 times the words per "
             "sentence, plus 11.8 times the syllables per word, less 15.59. Keep one "
             "decimal."),
            ("Say what the score leaves out",
             "Before you trust the number, ask whether the words are common, whether you "
             "know the topic, and whether each sentence leans on the last. The formula "
             "has seen none of that."),
            DAILY,
        ],
        "worked": {
            "title": "A hundred words by hand",
            "intro": [
                "A text of 100 words, 5 sentences and 140 syllables.",
            ],
            "lines": [
                "words a sentence   = 100 / 5   = 20",
                "syllables a word   = 140 / 100 = 1.4",
                "ease  = 206.835 − 20.3 − 118.44 = 68.095",
                "grade = 7.8 + 16.52 − 15.59     = 8.73",
            ],
            "after": [
                "The lab prints the ease as about 68.1 and the grade as 8.73, exact. A "
                "grade of 8.73 sits in this Subject's standard band.",
            ],
        },
        "quiz_title": "Counting difficulty",
        "quiz": [
            {"q": "A text has 200 words, 10 sentences and 300 syllables. What is its "
                  "Flesch–Kincaid grade?",
             "a": ["9.91", "8.73", "11.21", "7.80"],
             "c": 0,
             "why": "Words a sentence = 20, syllables a word = 1.5. Grade = 0.39 × 20 + "
                    "11.8 × 1.5 − 15.59 = 7.8 + 17.7 − 15.59 = 9.91. The answer 8.73 is "
                    "the grade for 1.4 syllables a word, and 7.80 is the sentence term alone."},
            {"q": "Two texts have the same sentence length. Text A averages 1.3 syllables "
                  "a word and text B 1.6. By how much does B's Reading Ease fall below A's?",
             "a": ["About 0.3 points", "About 25.4 points", "About 3.5 points",
                   "It cannot be said without the sentence length"],
             "c": 1,
             "why": "With sentence length the same, only the last term changes: 84.6 × "
                    "(1.6 − 1.3) = 84.6 × 0.3 = 25.38. The sentence term cancels, so its "
                    "value is not needed."},
            {"q": "A passage of short, common words explains an idea from a field you have "
                  "never studied, and its grade comes out at 6. What does the grade tell you?",
             "a": ["That you will read it as easily as other grade-6 text",
                   "That its sentences and words are short; nothing about how familiar "
                   "its ideas are",
                   "That the syllable rule failed on it",
                   "That it was written for children"],
             "c": 1,
             "why": "The formulas see only sentence length and syllables a word. Whether "
                    "the ideas are familiar is invisible to them, which is the lesson's "
                    "point and the subject of What You Already Know."},
        ],
        "mistakes": [
            ("Taking a readability score for how hard a text is to understand",
             "The score measures sentence length and syllables a word, nothing more. "
             "Short words about unfamiliar ideas score easy, and a passage in which every "
             "sentence depends on the last scores the same as a list of separate facts "
             "with the same counts. The score is a count; whether you understand the "
             "text is a measurement only a reading can make."),
            ("Reading the two scales the same way round",
             "Reading Ease falls as difficulty rises; the grade rises. The octopus "
             "passage has an ease of about 79.8 and a grade of about 6.8, the continents "
             "passage about 14.3 and 17.3. A high ease is an easy text and a high grade "
             "a hard one."),
            ("Trusting the second decimal",
             "Syllables are counted by a rule that gets some words wrong, and different "
             "programs count sentences differently. A grade of 9.3 against 9.4 is no "
             "difference at all; use the formulas to sort texts into broad bands."),
        ],
        "standard": (
            "Finish when you can score a text by hand and say what the score misses.",
            "Given counts of words, sentences and syllables, compute Flesch Reading Ease "
            "and the Flesch–Kincaid grade by hand to one decimal, and name two things "
            "that make a text hard which neither formula can see."
        ),
        "note": (
            "Every syllable figure here comes from a counting rule, an approximation, "
            "and another program will give slightly different scores for the same text. "
            "The formulas were fitted to readers and texts of their time; they sort "
            "texts by sentence and word length, and that is all they can be asked to do."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "unknown-words-and-coverage",
        "title": "Unknown Words and Coverage",
        "module": "Knowledge",
        "one_line": "Mark the words you do not know and compute the share of the text you do.",
        "summary": (
            "Coverage is the share of the words in a text that a reader knows. Read a "
            "hard passage full of technical terms, mark every word you do not know, "
            "and compute your coverage and how often an unknown word turned up, then "
            "set the figure beside what the studies of coverage found."
        ),
        "key": [
            "coverage = known tokens / all tokens",
            "one in every N = tokens / unknown",
            "98% = one unknown in every 50",
            "95% = one unknown in every 20",
        ],
        "key_label": "Coverage in four lines",
        "concepts_intro": (
            "A readability formula cannot tell a common word from a rare one. Your own "
            "marks can, for you."
        ),
        "concepts": [
            ("Tokens, not dictionary words",
             "Coverage counts every running word of the text, so a word that appears "
             "five times and that you do not know counts five times. That is how often "
             "you meet the gap while reading."),
            ("Two ways to say the same share",
             "Coverage of 98% and one unknown in every 50 tokens are the same "
             "measurement. The second is easier to picture: at ordinary prose density, "
             "50 tokens is two or three sentences."),
            ("A measurement made by marking",
             "You decide which words are unknown, and a word you half know is a "
             "judgement call. Mark the words whose meaning you could not give if asked, "
             "and keep the rule the same each time you measure."),
        ],
        "read_title": "How many unknown words a page can carry",
        "read_intro": (
            "The passage is about heraldry, a subject with its own vocabulary, chosen so "
            "that most readers meet some words they do not know."
        ),
        "body": [
            ("p", "The drill gives you The Grammar of Heraldry, a hard passage of 380 "
                  "words. Press Start, read it through once at your own pace, and mark "
                  "every word you do not know as you meet it: click it, or Tab to it and "
                  "press Enter. A second click unmarks a word. Mark a word each time it "
                  "appears. When you reach the end, press Count my marks."),
            ("def", ("Coverage",
                     "The <strong>coverage</strong> of a text for a reader is the share of "
                     "its running words, its tokens, that the reader knows: known tokens / "
                     "all tokens. With U unknown tokens in T, coverage is (T − U)/T, and "
                     "an unknown word turns up once in every T/U tokens.")),
            ("p", "The presets are a 500-word page at three coverages. "
                  "<strong>ninety-eight</strong> has 10 unknown tokens: 490/500 = 49/50 = "
                  "98%, one unknown in every 50. <strong>ninety-five</strong> has 25: "
                  "19/20 = 95%, one in every 20. <strong>ninety</strong> has 50: 9/10 = "
                  "90%, one in every 10. Ninety-five per cent sounds close to "
                  "ninety-eight. On the page, it is an unknown word in nearly every "
                  "sentence instead of one in every two or three."),
            ("math", [
                "ninety-eight:  490 / 500 = 98%,  500 / 10 = one in 50",
                "ninety-five:   475 / 500 = 95%,  500 / 25 = one in 20",
                "ninety:        450 / 500 = 90%,  500 / 50 = one in 10",
            ]),
            ("p", "How much coverage does reading need? The best-known study is Hu and "
                  "Nation's of 2000. They gave learners of English in New Zealand one "
                  "story, in versions at different coverages, and tested their "
                  "comprehension. At 95% coverage some "
                  "of the readers understood the story adequately but most did not, and "
                  "Hu and Nation estimated that about 98% was needed for most such "
                  "readers to read a text of that kind unassisted."),
            ("p", "That figure has been argued over since. Laufer and "
                  "Ravenhorst-Kalovski (2010) proposed 95% as a minimum and 98% as "
                  "optimal. Schmitt, Jiang and Grabe (2011) found comprehension rising "
                  "roughly in a line with coverage and no threshold at which it jumped. "
                  "Nation (2006) used 98% to estimate how large a vocabulary reading in "
                  "English needs. All of these concern learners of English; for a fluent "
                  "native reader the figures are an extrapolation, and a reasonable one "
                  "only as a rough guide."),
            ("p", "Now read your own result against them. If your coverage of the "
                  "heraldry passage was in the low nineties, you met an unknown word in "
                  "almost every sentence, and you will probably have felt it: the "
                  "passage defines many of its terms, but each definition has to be "
                  "held while the next term arrives. If your coverage was near 98% or "
                  "above, the unknown words were probably not the main difficulty: look "
                  "instead at its long sentences and long words, which the formulas "
                  "count, and at how much each sentence asks you to hold, which they "
                  "do not."),
            ("p", "This drill is not timed, and the heraldry passage's own six "
                  "questions are not asked: the marking interrupts the reading, so a rate "
                  "taken here would measure the marking. What the drill gives you is the "
                  "count. The step that follows from it is the slow one: a reader who "
                  "regularly meets one unknown word in every 20 is likely to gain more "
                  "from learning the field's words than from a change of pace."),
            ("p", "The next lesson, What You Already Know, asks the same question about "
                  "ideas instead of words: what happens to a rate when the words are "
                  "familiar and the subject is not."),
        ],
        "lab": ("readkit", {
            "mode": "text",
            "view": "coverage",
            "passage": PASSAGES["P40"],
            "preset": "ninety-eight",
            "presets": [
                {"id": "ninety-eight", "label": "500 words, 10 unknown",
                 "tokens": 500, "unknown": 10, "expect": {"txCoverage": "49/50 = 98%", "txOneIn": "one unknown in every 50 tokens"}},
                {"id": "ninety-five", "label": "500 words, 25 unknown",
                 "tokens": 500, "unknown": 25, "expect": {"txCoverage": "19/20 = 95%", "txOneIn": "one unknown in every 20 tokens"}},
                {"id": "ninety", "label": "500 words, 50 unknown",
                 "tokens": 500, "unknown": 50, "expect": {"txCoverage": "9/10 = 90%", "txOneIn": "one unknown in every 10 tokens"}},
            ],
            "panel_title": "Your coverage of the passage",
            "panel_intro": (
                "Your measurement: the words you marked as unknown, counted against every "
                "word of the passage by the kit's word rule. The presets are a 500-word "
                "page; after the drill the boxes hold the passage's 380 words and your marks."
            ),
        }),
        "steps_title": "Measuring coverage on your own reading",
        "steps_intro": (
            "Coverage is worth measuring on the texts you actually need to read, a page "
            "at a time."
        ),
        "steps": [
            ("Choose a page you need to read",
             "A page of a report, a paper or a manual in a field you are entering, new "
             "to you. About 300 to 500 words is enough."),
            ("Read it once and mark as you go",
             "Underline or note each word whose meaning you could not give if asked, "
             "every time it appears. Keep the same rule every time you measure."),
            ("Compute coverage and one in every N",
             "Count the words and the marks. Coverage = (words − marks) / words; one "
             "unknown in every words / marks. Below about 95%, expect an unknown word in "
             "nearly every sentence."),
            ("Decide what to do before you read on",
             "If the same few terms account for most of the marks, look them up first "
             "and read the page again later; if the marks are scattered, a glossary or "
             "an introductory text in the field will save more time than reading faster."),
            DAILY,
        ],
        "worked": {
            "title": "Ten unknown words in five hundred",
            "intro": [
                "A reader marks 10 unknown tokens on a page of 500 words.",
            ],
            "lines": [
                "known tokens  = 500 − 10 = 490",
                "coverage      = 490 / 500 = 49/50 = 98%",
                "one in every  = 500 / 10 = 50 tokens",
            ],
            "after": [
                "At 25 unknown tokens the same page has 95% coverage and an unknown word "
                "every 20 tokens; at 50, 90% and one every 10.",
            ],
        },
        "quiz_title": "Counting unknown words",
        "quiz": [
            {"q": "A reader marks 19 unknown tokens in a passage of 380 words. What are "
                  "their coverage and the density of unknown words?",
             "a": ["19/20 = 95%, one unknown in every 20 tokens",
                   "361/380 = 95%, one unknown in every 19 tokens",
                   "1/20 = 5%, one unknown in every 20 tokens",
                   "19/20 = 95%, one unknown in every 361 tokens"],
             "c": 0,
             "why": "Coverage is (380 − 19)/380 = 361/380 = 19/20 = 95%, and 380/19 = 20 "
                    "tokens per unknown word. The second option has the right coverage "
                    "and divides by the wrong number; the third gives the unknown share, "
                    "not the coverage."},
            {"q": "What did Hu and Nation's 2000 study find at 95% coverage?",
             "a": ["Every reader understood the story adequately",
                   "No reader understood the story at all",
                   "Some of the learners understood the story adequately, but most did not",
                   "Fluent native readers needed exactly 95% coverage"],
             "c": 2,
             "why": "Their readers were learners of English reading one story. At 95% some "
                    "reached adequate comprehension and most did not, and they estimated "
                    "about 98% for unassisted reading. They did not study native readers."},
            {"q": "A word you do not know appears four times in a passage. How should it "
                  "be counted for coverage?",
             "a": ["Once, since it is one word",
                   "Four times, since coverage counts running words",
                   "Not at all, if you can guess it from context",
                   "Once for each paragraph it appears in"],
             "c": 1,
             "why": "Coverage is a share of tokens, the running words of the text, so each "
                    "appearance counts. That is how often the gap interrupts the reading."},
        ],
        "mistakes": [
            ("Assuming one unknown word in twenty is fine because context will supply it",
             "In Hu and Nation's study of learners of English reading a story, most did "
             "not understand it adequately at 95% coverage, which is one unknown word in "
             "every 20; they estimated about 98%, one in every 50, for unassisted "
             "reading. Others put 95% as a minimum and 98% as optimal, or find no "
             "threshold at all, and for a fluent native reader the figures are an "
             "extrapolation. None of them found that context reliably fills the gaps at "
             "95%."),
            ("Counting each unknown word once",
             "Coverage counts tokens. A term you do not know that appears six times "
             "interrupts the reading six times and counts six times."),
            ("Reading 95% and 98% as nearly the same",
             "As shares they are three points apart; as densities they are one unknown "
             "word every 20 tokens against one every 50, an unknown word in almost every "
             "sentence against one in every two or three."),
        ],
        "standard": (
            "Finish when you can turn a count of unknown words into coverage and density.",
            "Given the tokens in a text and the unknown tokens, compute the coverage as "
            "a fraction and a percentage and one unknown in every N tokens, and say what "
            "Hu and Nation found at 95% and for whom."
        ),
        "note": (
            "Your marks are a judgement, and a word you half know may go either way; "
            "keep one rule each time you measure. The published figures come from "
            "learners of English, mostly reading single texts, and they disagree about "
            "whether there is a threshold at all. One passage on one day gives you one "
            "coverage figure for one subject."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "what-you-already-know",
        "title": "What You Already Know",
        "module": "Knowledge",
        "one_line": "Time a familiar topic against an unfamiliar one at the same grade, and compare.",
        "summary": (
            "Two procedures of about the same length and readability, one everyday and "
            "one from a laboratory. Read both at your natural pace with six questions "
            "each, compute both effective rates and their ratio, and see whether the "
            "readability formula predicted the difference."
        ),
        "key": [
            "effective rate = rate × comprehension",
            "ratio = unfamiliar ÷ familiar",
            "same grade, different topic",
            "knowledge is not in the formula",
        ],
        "key_label": "Familiar against unfamiliar",
        "concepts_intro": (
            "The last two lessons measured difficulty in sentences and in words. This "
            "one holds those close and changes the topic."
        ),
        "concepts": [
            ("A matched pair",
             "The two passages are both step-by-step procedures, 385 and 375 words long, "
             "at grades of about 9.4 and 8.9 by the formula. What differs is how much a "
             "typical reader already knows about each subject."),
            ("Knowledge does work while you read",
             "What you know about a subject tells you what a sentence is likely to say "
             "before you finish it, and where each new fact fits. Without it, every "
             "step has to be held in mind on its own."),
            ("The comparison is in effective rates",
             "An unfamiliar topic can cost time, questions or both. Comparing effective "
             "rates counts both costs at once."),
        ],
        "read_title": "What the formula did not predict",
        "read_intro": (
            "Packing a suitcase and staining bacteria on a slide: two procedures that a "
            "readability formula calls equally hard."
        ),
        "body": [
            ("p", "Do the drill first. Read Packing for a Week Away and Performing a "
                  "Gram Stain, each once at your natural pace, and answer the six "
                  "questions after each. The lab alternates which comes first, so take "
                  "them in the order it shows."),
            ("p", "By the counts of Measuring Difficulty, the two passages are as close "
                  "as two texts on different subjects get. Packing for a Week Away has "
                  "385 words in 16 sentences, a grade of about 9.4; Performing a Gram "
                  "Stain has 375 words in 18 sentences, a grade of about 8.9. If the "
                  "formula measured difficulty, the Gram stain would be the slightly "
                  "easier read."),
            ("p", "Whether it read easier for you is what the drill measured. The "
                  "preset <strong>typical</strong> is a reader for whom it did not, "
                  "who read the packing passage in 96.25 seconds, 240 words a "
                  "minute, with 6 of 6 right, and the Gram stain in 100 seconds, 225 "
                  "words a minute, with 4 of 6. The effective rates are 240 and 225 × "
                  "4/6 = 150, and the ratio is 150/240 = 5/8 = 62.5%. The rate fell a "
                  "little and the questions fell more: the steps of the stain had to be "
                  "taken in one by one, and two of them did not stay."),
            ("math", [
                "familiar:    385 × 60 / 96.25 = 240,  240 × 6/6 = 240",
                "unfamiliar:  375 × 60 / 100   = 225,  225 × 4/6 = 150",
                "ratio = 150 / 240 = 5/8 = 62.5%",
            ]),
            ("p", "The preset <strong>expert</strong> is a reader who has worked in a "
                  "microbiology laboratory. The packing passage is the same, 240 words "
                  "a minute and 6 of 6; the Gram stain takes them 90 seconds, 250 words "
                  "a minute, with 6 of 6. Their effective rates are 240 and 250, a ratio "
                  "of 25/24, about 104.2%. For this reader the specialist passage is the "
                  "familiar one, and it reads a little faster than the everyday one."),
            ("p", "The best-known demonstration is Recht and Leslie's of 1988. They "
                  "gave 64 junior-high students, sorted by reading ability and by how "
                  "much they knew about baseball, a passage describing part of a "
                  "baseball game, and measured what the students recalled and could "
                  "re-enact of it. Knowledge of baseball mattered more than reading "
                  "ability for what they recalled. They measured recall, not speed, and "
                  "their readers were young; Rayner and colleagues' 2016 review counts "
                  "background knowledge among the strongest influences on comprehension "
                  "in readers generally."),
            ("p", "Two readings differ in more than topic. The passages are different "
                  "texts, with different steps and different questions, and whichever "
                  "you read second you read a little more practised or more tired. One "
                  "question is about 16.7 points, so a one-question difference is not a "
                  "result. If your result goes the other way, you have not refuted Recht "
                  "and Leslie, and they have not refuted your reading: you may know more "
                  "about laboratories than about suitcases."),
            ("p", "What follows for reading faster is the least glamorous finding in "
                  "the Subject and one of the most useful. In a field you read often, "
                  "the gain most within reach is often to know more of the field: an "
                  "introductory text first, then the hard one. That is an inference "
                  "from studies of recall, not something they timed. No change of technique "
                  "gave the expert reader their extra 100 effective words a minute on "
                  "the Gram stain; what they knew did."),
            ("p", "The next lesson, How Much You Read, turns from what you know to how "
                  "you come to know it, and puts a number on a year of reading."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P41"], PASSAGES["P42"]],
            "a": {"label": "Familiar topic", "kind": "test"},
            "b": {"label": "Unfamiliar topic", "kind": "test"},
            "ratioOf": "err",
            "preset": "typical",
            "presets": [
                {"id": "typical", "label": "typical reader: 240 and 150 effective",
                 "wordsA": 385, "secondsA": "96.25", "correctA": 6, "totalA": 6,
                 "wordsB": 375, "secondsB": 100, "correctB": 4, "totalB": 6,
                 "expect": {"drErrA": "240 wpm", "drErrB": "150 wpm", "drRatio": "5/8 = 62.5%"}},
                {"id": "expert", "label": "a reader who knows the laboratory",
                 "wordsA": 385, "secondsA": "96.25", "correctA": 6, "totalA": 6,
                 "wordsB": 375, "secondsB": 90, "correctB": 6, "totalB": 6,
                 "expect": {"drErrA": "240 wpm", "drErrB": "250 wpm", "drRatio": "25/24 ≈ 104.2%"}},
            ],
            "panel_title": "A familiar and an unfamiliar topic",
            "panel_intro": (
                "Your measurement: two readings at your natural pace on passages of about "
                "the same length and grade. The ratio is the unfamiliar topic's effective "
                "rate over the familiar one's. One question is ≈ 16.7 points; a "
                "one-question difference is not a result."
            ),
        }),
        "steps_title": "Testing what your knowledge is worth",
        "steps_intro": (
            "You can run this comparison on your own reading, with a subject you know "
            "well and one you do not."
        ),
        "steps": [
            ("Choose two texts at about the same grade",
             "One on a subject you know well and one on a subject new to you, of similar "
             "length. Check both grades with the counter in Measuring Difficulty; keep "
             "them within one grade."),
            ("Read each once at your natural pace",
             "Time each reading and note the order. If you can, read the unfamiliar one "
             "first on one occasion and second on another."),
            ("Test yourself on both",
             "Questions from someone else, or three sentences from memory on each. "
             "Score each the same way."),
            ("Compute both effective rates and the ratio",
             "Rate times score for each, then unfamiliar over familiar. Then compare the "
             "two grades and say whether the formula predicted what you found."),
            DAILY,
        ],
        "worked": {
            "title": "Suitcase and slide",
            "intro": [
                "A reader reads Packing for a Week Away, 385 words, in 96.25 seconds with "
                "6 of 6, and Performing a Gram Stain, 375 words, in 100 seconds with 4 of 6.",
            ],
            "lines": [
                "familiar rate   = 385 × 60 / 96.25 = 240",
                "unfamiliar rate = 375 × 60 / 100   = 225",
                "effective       = 240 × 1 = 240;  225 × 4/6 = 150",
                "ratio           = 150 / 240 = 5/8 = 62.5%",
            ],
            "after": [
                "The grades were about 9.4 and 8.9, so the formula called the unfamiliar "
                "passage slightly easier. The effective rate on it was five eighths of the "
                "familiar one.",
            ],
        },
        "quiz_title": "Knowledge and rate",
        "quiz": [
            {"q": "A reader reads a familiar passage at 260 words a minute with 6 of 6 and "
                  "an unfamiliar one at 225 with 4 of 6. What is the ratio of the effective "
                  "rates, unfamiliar to familiar?",
             "a": ["225/260, about 86.5%", "15/26, about 57.7%", "4/6, about 66.7%",
                   "26/15, about 173.3%"],
             "c": 1,
             "why": "The effective rates are 260 × 1 = 260 and 225 × 4/6 = 150, and 150/260 "
                    "= 15/26 ≈ 57.7%. The first option compares the rates and ignores the "
                    "scores; the third is the score alone."},
            {"q": "The Gram stain passage scores a grade of about 8.9 and the packing "
                  "passage about 9.4. Why did the formula not predict that a reader new "
                  "to microbiology finds the Gram stain harder?",
             "a": ["The syllable rule miscounted the Gram stain passage",
                   "The formula sees sentence and word length, not whether the reader "
                   "knows the subject",
                   "The packing passage has more sentences",
                   "Grades below 9 are always unreliable"],
             "c": 1,
             "why": "Both formulas are built from words per sentence and syllables per "
                    "word. How much a reader knows about the topic is not among their inputs."},
            {"q": "What did Recht and Leslie's 1988 study measure?",
             "a": ["How fast junior-high students read a baseball passage",
                   "Whether knowing baseball raised students' reading ability scores",
                   "What students recalled of a baseball passage, by reading ability and "
                   "by knowledge of baseball",
                   "Eye movements of adults reading about baseball"],
             "c": 2,
             "why": "They measured recall and re-enactment, not speed, in 64 junior-high "
                    "students, and found that knowledge of baseball mattered more than "
                    "reading ability."},
        ],
        "mistakes": [
            ("Believing speed is a skill independent of what you know",
             "Recht and Leslie found that junior-high readers' knowledge of baseball "
             "mattered more than their reading ability for what they recalled of a "
             "baseball passage, and Rayner and colleagues' 2016 review counts background "
             "knowledge among the strongest influences on comprehension. In the typical "
             "preset the same reader's effective rate is 240 on a familiar procedure and "
             "150 on an unfamiliar one at almost the same grade."),
            ("Trusting the grade to predict your reading",
             "The Gram stain passage scores slightly easier than the packing passage. "
             "The formula has no input for what you know, so two texts at the same grade "
             "can read very differently for the same reader."),
            ("Comparing the rates and not the effective rates",
             "In the typical preset the rate fell from 240 to 225, about 6%. The "
             "effective rate fell from 240 to 150, because two questions were lost. An "
             "unfamiliar topic can cost time, understanding or both, and only the "
             "effective rate counts both."),
        ],
        "standard": (
            "Finish when you can say what knowing a topic did to a reading.",
            "Given a familiar and an unfamiliar reading, each with words, seconds and a "
            "score, compute both effective rates and their ratio, and say why a "
            "readability formula with both texts at the same grade did not predict the "
            "difference."
        ),
        "note": (
            "This is one pair of readings on one day. The passages differ in more than "
            "topic, being different texts with different questions, and which came first "
            "matters: the lab alternates the order because the second reading is done "
            "more practised or more tired. Recht and Leslie measured recall in young "
            "readers; your drill measures one adult's rate and score on two texts."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "how-much-you-read",
        "title": "How Much You Read",
        "module": "Knowledge",
        "one_line": "Compute a year of reading, and compare a faster rate with more minutes a day.",
        "summary": (
            "A year of reading is minutes a day times rate times days. Compute it for "
            "your own habits, then compare what a higher rate adds with what more "
            "minutes add, and find the rate gain that would equal ten more minutes a day."
        ),
        "key": [
            "words a year = minutes × rate × 365",
            "books a year = words a year / 90,000",
            "+10 minutes on 20 = +50% volume",
            "+50% volume by rate: 250 → 375",
        ],
        "key_label": "A year of reading",
        "concepts_intro": (
            "This course has measured what knowing the words and knowing the subject do "
            "to a reading. Much of both is thought to come from reading itself."
        ),
        "concepts": [
            ("Volume is a product",
             "Words a year is minutes a day times words a minute times days. Raise "
             "either factor by half and the year's reading rises by half."),
            ("Time is the easier factor",
             "A rate gain of half is far beyond what any technique in this Subject has "
             "reliably shown. Ten minutes more on twenty is half as much time again, and "
             "it is a choice you can make tomorrow."),
            ("Reading volume and growth go together",
             "Studies of children find that those who read more also grow more in "
             "vocabulary and reading. The evidence is correlational, and it is "
             "consistent with the lessons before this one."),
        ],
        "read_title": "Minutes against words a minute",
        "read_intro": (
            "Start with the warm-up reading at the top of the lab; then compute what a "
            "year of reading at your rate comes to."
        ),
        "body": [
            ("p", "Begin with the warm-up at the top of the lab: a hard passage from the "
                  "practice pool, read at your usual pace and logged as practice. The lab "
                  "serves How a Violin Makes Its Voice, or Best Specimen for the Table if "
                  "you have read the first already."),
            ("p", "Then put your own habits into the calculator below it: the minutes a "
                  "day you actually read, not the minutes you mean to, and your rate "
                  "from your log. The model is a product, with the year at 365 days and "
                  "a book at 90,000 words."),
            ("p", "The preset <strong>twenty-minutes</strong> is a reader who reads 20 "
                  "minutes a day at 250 words a minute: 20 × 250 × 365 = 1,825,000 words "
                  "a year, about 20.3 books of 90,000 words. The preset "
                  "<strong>faster</strong> keeps the 20 minutes and raises the rate to "
                  "300: 2,190,000 words, about 24.3 books. The preset "
                  "<strong>longer</strong> keeps the rate at 250 and reads for 30 "
                  "minutes: 2,737,500 words, about 30.4 books."),
            ("math", [
                "twenty-minutes: 20 × 250 × 365 = 1,825,000 words",
                "faster:         20 × 300 × 365 = 2,190,000 words",
                "longer:         30 × 250 × 365 = 2,737,500 words",
                "rate-to-match:  20 × 375 × 365 = 2,737,500 words",
            ]),
            ("p", "Ten more minutes on twenty is 50% more time, so it adds 50% more "
                  "words. To get the same from rate alone, 250 words a minute would have "
                  "to become 250 × 3/2 = 375, which is the preset "
                  "<strong>rate-to-match</strong>. A rate gain from 250 to 300 is 20%, "
                  "and even that adds less than half of what the ten minutes add: "
                  "365,000 words against 912,500."),
            ("p", "There is a second reason the minutes matter. Anderson, Wilson and "
                  "Fielding (1988) had 155 fifth-graders keep diaries of how they spent "
                  "their time out of school, and found that time spent reading books was "
                  "the best predictor of their growth in reading. Nagy and Herman (1987) "
                  "argued, from estimates of how many words children learn each year, "
                  "that most of that vocabulary is picked up from context while reading "
                  "rather than taught. Both lines of evidence are correlational or rest "
                  "on estimates: readers who read more grow more, and the studies cannot "
                  "fully separate the reading from the readers."),
            ("p", "Put the course together. A rate "
                  "is a rate on a kind of text; it falls on hard text, on text full of "
                  "unknown words and on unfamiliar subjects; and the words and subjects "
                  "you know come, on the best estimates, largely from what you have "
                  "read. Reading faster is worth training, and this Subject trains it "
                  "every day. Reading more is the larger lever on how much you read, "
                  "and if the correlational studies point the right way, it is also "
                  "the one that makes the next text easier."),
            ("p", "The next course, Remembering What You Read, asks what is kept of all "
                  "those words, and measures it."),
        ],
        "lab": ("readkit", {
            "mode": "text",
            "view": "volume",
            "warmup": [_POOL["Q23"], _POOL["Q30"]],
            "preset": "twenty-minutes",
            "presets": [
                {"id": "twenty-minutes", "label": "20 minutes at 250",
                 "minutes": 20, "wpm": 250, "expect": {"txWordsYear": "1,825,000 words", "txBooksYear": "≈ 20.3 books"}},
                {"id": "faster", "label": "20 minutes at 300",
                 "minutes": 20, "wpm": 300, "expect": {"txWordsYear": "2,190,000 words", "txBooksYear": "≈ 24.3 books"}},
                {"id": "longer", "label": "30 minutes at 250",
                 "minutes": 30, "wpm": 250, "expect": {"txWordsYear": "2,737,500 words", "txBooksYear": "≈ 30.4 books"}},
                {"id": "rate-to-match", "label": "20 minutes at 375",
                 "minutes": 20, "wpm": 375, "expect": {"txWordsYear": "2,737,500 words", "txBooksYear": "≈ 30.4 books"}},
            ],
            "panel_title": "A year of reading",
            "panel_intro": (
                "A stated model: words a year = minutes a day × rate × days, and books = "
                "words a year / words in a book. Put in your own minutes and the rate from "
                "your log."
            ),
        }),
        "steps_title": "Working out your own year",
        "steps_intro": "Do this once now and again whenever your habits change.",
        "steps": [
            ("Measure your minutes honestly",
             "For a week, note the minutes you spend reading text of your choosing each "
             "day, and take the average. Intentions do not count."),
            ("Take your rate from your log",
             "Use the median of your baseline and test readings, not your best reading."),
            ("Compute your year, then two changes",
             "Minutes × rate × 365, then the same with ten more minutes, then the rate "
             "gain that would match it: rate × (minutes + 10) / minutes."),
            ("Choose the cheaper change",
             "Decide where the ten minutes would come from, and write it down. A rate "
             "gain is trained over months; ten minutes can be found by tomorrow."),
            DAILY,
        ],
        "worked": {
            "title": "Ten more minutes, or 125 more words a minute",
            "intro": [
                "A reader reads 20 minutes a day at 250 words a minute.",
            ],
            "lines": [
                "now:          20 × 250 × 365 = 1,825,000 words",
                "+10 minutes:  30 × 250 × 365 = 2,737,500 words",
                "faster:       20 × 300 × 365 = 2,190,000 words",
                "to match:     250 × 30 / 20  = 375 words a minute",
            ],
            "after": [
                "Ten more minutes a day adds 912,500 words a year, about 10.1 books; "
                "reading at 300 adds 365,000, about 4.1 books. Only a rate of 375 would "
                "match the ten minutes.",
            ],
        },
        "quiz_title": "A year of reading",
        "quiz": [
            {"q": "A reader reads 15 minutes a day at 240 words a minute. How many words "
                  "is that in a year of 365 days?",
             "a": ["1,314,000", "3,600", "1,095,000", "87,600"],
             "c": 0,
             "why": "15 × 240 = 3,600 words a day, and 3,600 × 365 = 1,314,000. The "
                    "second option is one day's reading and the last forgets the minutes."},
            {"q": "A reader reads 20 minutes a day at 250 words a minute. What rate would "
                  "add as many words a year as reading 10 minutes longer at 250?",
             "a": ["260 words a minute", "300 words a minute", "375 words a minute",
                   "500 words a minute"],
             "c": 2,
             "why": "Ten minutes more on twenty is half as much again, so the rate must "
                    "rise by half: 250 × 30/20 = 375. 300 adds only a fifth, and 500 "
                    "would double the volume."},
            {"q": "What kind of evidence links reading volume with vocabulary growth in "
                  "Anderson, Wilson and Fielding's 1988 study?",
             "a": ["A randomised experiment that assigned extra reading time",
                   "A correlation between diary records of reading time and reading growth",
                   "Eye-movement recordings of fifth-graders",
                   "A comparison of speed-reading graduates with untrained readers"],
             "c": 1,
             "why": "The children kept diaries of their time out of school, and time "
                    "spent reading books was the best predictor of their reading growth. "
                    "That is a correlation; no child was assigned to read more."},
        ],
        "mistakes": [
            ("Thinking the way to read more is to read faster",
             "Ten more minutes a day at 250 adds as much as a rate gain from 250 to 375, "
             "which no technique reliably delivers: in the presets, 2,737,500 words a "
             "year either way, against 2,190,000 for a gain to 300. Reading volume is "
             "also strongly associated with growth in vocabulary and knowledge, though "
             "that evidence is correlational."),
            ("Counting intended minutes",
             "The model is only as good as the minutes put into it. A week of noted "
             "minutes is a measurement; a resolution is not."),
            ("Reading the correlation as proof",
             "Children who read more grow more, but they may differ in other ways too. "
             "The case for more minutes rests on the arithmetic of this lesson and on "
             "the lessons before it, not on the correlation alone."),
        ],
        "standard": (
            "Finish when you can compare a rate gain with a time gain in numbers.",
            "Given minutes a day and two rates, compute both years of reading in words "
            "and in books, and compute the rate gain that would equal a given number of "
            "extra minutes a day."
        ),
        "note": (
            "The model multiplies three numbers and assumes every minute is read at "
            "your logged rate, on text like the text you were measured on. The studies "
            "linking volume with growth are of children and are correlational; for an "
            "adult reader they suggest a direction, not a size."
        ),
    },
]
