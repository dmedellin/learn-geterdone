"""Course 1, lessons 1-5 -- rate, comprehension, noise, reference figures, the log."""

from reading.passages import PASSAGES

ONCE = "above the baseline range once — a fourth reading does this about one time in four"
MEDIAN = "above the baseline range on the median of the last three tests"

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "words-per-minute",
        "title": "Words per Minute",
        "module": "Rate and comprehension",
        "one_line": "Time one reading of a story at your natural pace, and turn the time into a rate in two units.",
        "summary": (
            "How fast do you read a story you have chosen to read? Time one reading of a "
            "491-word passage, divide words by minutes, and divide characters by six to get "
            "the same rate in standard-length words. Then place the number against the "
            "published averages, in the unit they use."
        ),
        "key": [
            "rate = words × 60 / seconds",
            "standard words = characters / 6",
            "standard rate = (chars / 6) × 60 / seconds",
            "Brysbaert: about 238 nonfiction, 260 fiction",
            "Carver's figures: standard-length words",
        ],
        "key_label": "A rate in five lines",
        "concepts_intro": (
            "The question is simple and the method is a stopwatch and a division. What "
            "takes care is the unit, and what a single number is a measurement of."
        ),
        "concepts": [
            ("A rate is words over minutes",
             "Words read, divided by the time in minutes. The drill counts the words, "
             "times you from Start to Done, and does the division, so the only thing you "
             "supply is the reading."),
            ("A standard word is six characters",
             "Words differ in length, so a rate in words depends on the text. Carver "
             "counts a text's characters, spaces and punctuation included, and divides by "
             "six: a standard-length word. The same reading has a rate in each unit."),
            ("An average has readers on both sides",
             "The published averages are estimates over many adult readers. They tell you "
             "where the middle is, not where you ought to be, and every average has many "
             "readers below it."),
        ],
        "read_title": "What the clock measured",
        "read_intro": (
            "One reading, two numbers from it, and the published figures they can be "
            "compared with."
        ),
        "body": [
            ("p", "Before you read on, do the drill below. Press Start, read “The Church "
                  "Clock at Wexley” at the pace you would read a story you had chosen, press "
                  "Done the moment you reach the last word, and answer the six questions. "
                  "Do it once, now: the rest of this page is better read with your own "
                  "number beside it."),
            ("p", "The drill counted the passage, 491 words, and timed you from Start to Done "
                  "to the millisecond. Your rate is the words multiplied by sixty and divided "
                  "by your seconds. If you took exactly two minutes, that is 491 × 60 / 120 "
                  "= 245.5 words a minute, and the tile prints it beside your time. The "
                  "questions were scored too; the next lesson is about them, so for now look "
                  "only at the rate."),
            ("math", [
                "rate = words × 60 / seconds",
                "491 × 60 / 120 = 245.5",
            ]),
            ("p", "Where does your number sit? Brysbaert (2019) pooled the studies of adult "
                  "silent reading in English and estimated about 238 words a minute for "
                  "nonfiction and about 260 for fiction; reading aloud averages about 183. "
                  "“The Church Clock at Wexley” is a story, so 260 is the nearer comparison. "
                  "The figure most people have heard, around 300, is in Brysbaert's "
                  "analysis an overestimate. These are averages, with many readers on each "
                  "side of them, and a first reading below one is a starting point, not a "
                  "verdict."),
            ("def", ("Standard-length word",
                     "A <strong>standard-length word</strong> is six character spaces of "
                     "text, letters, spaces and punctuation counted together. A text's "
                     "standard words are its characters divided by six. Carver (1990) used "
                     "this unit so that rates on texts of long words and of short words "
                     "could be compared.")),
            ("p", "Why a second unit? A rate in words depends on the words. Take a passage "
                  "of 400 words with 2,640 characters, 6.6 to a word with its space, which "
                  "is a text of long words. The steady preset is a reader who took 96 "
                  "seconds over it: 400 × 60 / 96 = 250 words a minute, and 2,640 / 6 = 440 "
                  "standard words, so 440 × 60 / 96 = 275 standard words a minute. The slow "
                  "preset is the same passage in 160 seconds: 150 words a minute and 165 "
                  "standard. On long words the standard rate is the higher of the two."),
            ("p", "Your passage goes the other way. It has 2,652 characters, about 5.4 to a "
                  "word with its space, so its 442 standard words are fewer than its 491 "
                  "words, and your standard rate is lower than your rate in words. At two "
                  "minutes it would be 442 × 60 / 120 = 221. Same reading, two numbers. "
                  "Which one to use depends on what you compare it with: Brysbaert's "
                  "averages are in words, and Carver's figures, which Typical Rates and "
                  "Reading Gears uses, are in standard-length words."),
            ("p", "The reading you just did is logged as a baseline, the first of the "
                  "readings at your natural pace that the later courses compare with. It is "
                  "one measurement of one passage on one day, not your reading speed, and "
                  "One Reading Is One Measurement shows how far the next one can move with "
                  "nothing changed."),
            ("p", "Next, Comprehension and the Effective Rate: a second natural-pace reading, "
                  "a reading as fast as you can make yourself go, and what the questions "
                  "say about the difference."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "single",
            "passage": PASSAGES["P01"],
            "display": "normal",
            "kind": "baseline",
            "preset": "steady",
            "presets": [
                {"id": "steady", "label": "400 words in 96 s", "words": 400, "chars": 2640,
                 "seconds": 96, "correct": 5, "total": 6,
                 "expect": {"drWpm": "250 wpm", "drStdWpm": "275 standard wpm"}},
                {"id": "slow", "label": "400 words in 160 s", "words": 400, "chars": 2640,
                 "seconds": 160, "correct": 6, "total": 6,
                 "expect": {"drWpm": "150 wpm", "drStdWpm": "165 standard wpm"}},
            ],
        }),
        "steps_title": "Timing a reading on another day",
        "steps_intro": (
            "The protocol, for any timed reading you do later. The second step is the one "
            "people get wrong."
        ),
        "steps": [
            ("Choose a text you have not read",
             "Prose of an ordinary kind, a few hundred words long, that you have never seen. "
             "A text you have read before measures your memory of it."),
            ("Read as you would by choice",
             "Not racing, because the clock is running, and not studying, because questions "
             "follow. The number is meant to describe your ordinary reading."),
            ("Stop the clock at the last word",
             "Start as your eyes reach the first word and stop as they leave the last one. "
             "Time spent deciding whether you have finished belongs to the reading; time "
             "spent on the questions does not."),
            ("Compute both rates",
             "Words × 60 / seconds, and characters / 6 × 60 / seconds. Write both down with "
             "the date and the text, and say which one you compare with which figure."),
        ],
        "worked": {
            "title": "The steady preset by hand",
            "intro": [
                "A reader took 96 seconds over a passage of 400 words and 2,640 characters, "
                "spaces included.",
            ],
            "lines": [
                "rate            = 400 × 60 / 96  = 250",
                "standard words  = 2,640 / 6      = 440",
                "standard rate   = 440 × 60 / 96  = 275",
            ],
            "after": [
                "250 words a minute and 275 standard words a minute are the same reading. "
                "The standard rate is higher because this text's words average 6.6 "
                "characters with their space, longer than Carver's six; on “The Church "
                "Clock at Wexley”, at 5.4, it comes out lower.",
            ],
        },
        "quiz_title": "Rates and units",
        "quiz": [
            {"q": "A reader takes 150 seconds over a 600-word passage. What is the rate?",
             "a": ["240 words a minute", "250 words a minute", "4 words a minute",
                   "400 words a minute"],
             "c": 0,
             "why": "600 × 60 / 150 = 240. Four is words per second, and 400 comes from "
                    "reading 150 seconds as 1.5 minutes."},
            {"q": "The same passage has 3,300 characters, spaces included. What is the rate "
                  "in standard-length words?",
             "a": ["200 standard words a minute", "240 standard words a minute",
                   "220 standard words a minute", "264 standard words a minute"],
             "c": 2,
             "why": "3,300 / 6 = 550 standard words, and 550 × 60 / 150 = 220. The words "
                    "average 5.5 characters with their space, so the standard rate is lower "
                    "than the rate in words."},
            {"q": "Which of these figures is given in standard-length words?",
             "a": ["Brysbaert's 238 for silent reading of nonfiction",
                   "Brysbaert's 183 for reading aloud",
                   "The rate in the drill's first rate tile",
                   "Carver's figures for college students"],
             "c": 3,
             "why": "Brysbaert's estimates are in words, and so is the drill's words-a-minute "
                    "tile; the standard rate has its own tile. Carver's figures use six-"
                    "character standard-length words."},
            {"q": "A reader's first drill gives 225 words a minute on a story. Which "
                  "statement does the lesson support?",
             "a": ["The reader is slow, since adults read about 300 words a minute",
                   "It is one measurement, somewhat below Brysbaert's 260 for fiction",
                   "The reader's reading speed is 225 words a minute",
                   "The rate must be raised to 260 before anything else is practised"],
             "c": 1,
             "why": "Brysbaert estimates about 260 for fiction and argues the familiar 300 is "
                    "too high. One timed reading is one measurement, and an average has many "
                    "readers below it."},
        ],
        "mistakes": [
            ("“Most adults read about 300 words a minute, so I am slow”",
             "The figure is familiar and too high. Brysbaert's (2019) estimate for silent "
             "reading of English nonfiction is about 238 words a minute, and about 260 for "
             "fiction, and he argues that 300 overstates it. An average also has readers on "
             "both sides: a first reading below it describes a starting point."),
            ("Comparing rates in words across different texts",
             "A text of long words takes longer per word. The steady preset's 250 words a "
             "minute is 275 standard words a minute on its long-word passage; the same 250 on "
             "text like “The Church Clock at Wexley” would be about 225. Carver counts "
             "six-character standard words so that texts can be compared."),
            ("Reading for the clock",
             "A running clock makes many readers hurry. A reading done as fast as you can go "
             "measures a different thing, which is the second reading in the next lesson. "
             "The baseline is meant to describe how you read when nobody is timing you."),
        ],
        "standard": (
            "Finish when you can compute both rates from three numbers.",
            "Given a reading of 520 words and 2,880 characters, spaces included, in 130 "
            "seconds, compute the rate in words and in standard-length words to the nearest "
            "whole number without the lab (240 and 222), and say that Carver's figures use "
            "the second unit and Brysbaert's the first.",
        ),
        "note": (
            "One passage, one sitting. The rate depends on the passage and on the day as well "
            "as on you, and the drill cannot separate them; that is what the baselines in "
            "this course are for. The time runs from Start to Done, so a pause in the middle "
            "is counted as reading."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "comprehension-and-effective-rate",
        "title": "Comprehension and the Effective Rate",
        "module": "Rate and comprehension",
        "one_line": "Read once at your natural pace and once as fast as you can, score both, and find which delivered more understood words per minute.",
        "summary": (
            "Does reading faster get more read? Do two timed readings, one at your natural "
            "pace and one as fast as you can go, answer six questions after each, and "
            "multiply each rate by its share of questions right. The product, the effective "
            "reading rate, is what this Subject reports beside every rate."
        ),
        "key": [
            "comprehension = right / asked",
            "effective rate = rate × comprehension",
            "one question in six ≈ 16.7 points",
            "480 × 2/6 = 160 < 240 × 6/6 = 240",
        ],
        "key_label": "The effective rate in four lines",
        "concepts_intro": (
            "A rate on its own cannot tell a careful reader from a fast page-turner. The "
            "questions can, once they are multiplied in."
        ),
        "concepts": [
            ("Comprehension is a share",
             "Questions right over questions asked. With six questions a passage, each one "
             "is about 16.7 points, which is why a one-question difference is not a result."),
            ("The effective rate is a product",
             "Rate times comprehension: understood words per minute. Jackson and McClelland "
             "(1979) called it the effective reading speed. A rate that doubles while the "
             "score falls by more than half has gone down."),
            ("Two readings, two passages",
             "A passage cannot be read for the first time twice, so a comparison uses two "
             "different texts, and one of them comes first. Both facts can move the result, "
             "and the lab records which came first."),
        ],
        "read_title": "Two readings side by side",
        "read_intro": (
            "What changed between them, what the questions add, and why the product decides."
        ),
        "body": [
            ("p", "Do the drill below before reading on. It has two timed readings: one at your "
                  "natural pace, as in Words per Minute, and one, in the box labelled “As fast "
                  "as you can”, as fast as you can make yourself go. The page chooses which comes first, and each passage is "
                  "followed by its six questions, with the text hidden."),
            ("p", "Look at your two readings side by side. If the second was faster — and for "
                  "most people told to go as fast as they can, it is, often by a lot — look "
                  "next at the questions. The usual result is a rate that went up and a score "
                  "that went down, and the question that matters is what happened to their "
                  "product. Four hundred words at 480 words a minute with two questions in "
                  "six right is, in understood words per minute, worse than the same length "
                  "at 240 with all six: 160 against 240. That product is the effective reading "
                  "rate, and it is the number every drill in this Subject reports beside your "
                  "rate, because a rate on its own cannot tell a fast reader from a fast "
                  "page-turner."),
            ("def", ("Effective reading rate",
                     "<strong>Comprehension</strong> is questions right divided by "
                     "questions asked. The <strong>effective reading rate</strong> is the "
                     "rate multiplied by comprehension, in words a minute. Jackson and "
                     "McClelland (1979) used this product, which they called effective "
                     "reading speed, to compare readers who traded speed against "
                     "understanding in different amounts.")),
            ("math", [
                "comprehension  = right / asked",
                "effective rate = rate × comprehension",
                "480 × 2/6 = 160",
                "240 × 6/6 = 240",
            ]),
            ("p", "The pushed-too-far preset is that pair. Reading A is 400 words in 100 "
                  "seconds with all six right: 240 words a minute, effective 240. Reading B "
                  "is the same length in 50 seconds with two right: 480 words a minute, "
                  "effective 160. The rate doubled and the effective rate fell by 80, to "
                  "two-thirds of A's."),
            ("p", "The worth-it preset changes only B: 400 words in 75 seconds with five "
                  "right, so 320 words a minute and an effective rate of 320 × 5/6 ≈ 266.7, "
                  "about 26.7 more than A's 240. Here the faster reading delivered more. The "
                  "lesson is not that slow is good; it is that the product decides, and a "
                  "faster reading that keeps most of its score can win."),
            ("p", "Read the scores with their size in mind. One question is about 16.7 "
                  "points of comprehension, so five right against six is a single question, "
                  "and a single question can turn on a lapse of attention or on a guess. A "
                  "one-question difference is not a result; the lab prints that sentence "
                  "above the tiles."),
            ("p", "Two readings differ in more than their pace. They are different passages, "
                  "“How Bread Rises” and “Fog on the Crossing”, an explanation and a story, "
                  "and one came first, so the second may be helped by warming up or hurt by "
                  "fatigue; the page sets the order from your log, alternating, and records "
                  "it. If your fast reading came out ahead, you have not refuted the usual "
                  "result, and the usual result has not refuted you: it is one pair of "
                  "readings on two passages."),
            ("p", "The questions were written so that a guess from general knowledge fails. "
                  "Rayner and his colleagues' 2016 review of speed reading, published after "
                  "Rayner's death in 2015, makes the point that a comprehension test which "
                  "can be passed without reading the text says nothing about the reading."),
            ("p", "Your natural-pace reading is logged as your second baseline. The fast one "
                  "is logged as a condition: it stays in your log, and no verdict counts it. "
                  "The last tile sets rate B against your baseline range, and with one "
                  "baseline so far that range is a single reading: leave the tile until One "
                  "Reading Is One Measurement has given you three."),
            ("p", "Next, One Reading Is One Measurement: two more natural-pace readings, and "
                  "how far your rate moves between them with nothing changed."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P02"], PASSAGES["P03"]],
            "a": {"label": "Your natural pace", "kind": "baseline"},
            "b": {"label": "As fast as you can", "kind": "condition",
                  "intro": "Read this one as fast as you can make yourself go, then answer its "
                           "questions as well as you can."},
            "ratioOf": "err",
            "order": "alternate",
            "panel_intro": (
                "Your measurement. Reading A is at your natural pace. Reading B is the other "
                "condition: as fast as you can make yourself go, as its box says. Press Start, "
                "read, press Done, answer, press Score, and the boxes fill with what you did; "
                "before that they hold a worked example."
            ),
            "preset": "pushed-too-far",
            "presets": [
                {"id": "pushed-too-far", "label": "Twice as fast, two right",
                 "wordsA": 400, "secondsA": 100, "correctA": 6, "totalA": 6,
                 "wordsB": 400, "secondsB": 50, "correctB": 2, "totalB": 6,
                 "expect": {"drWpmA": "240 wpm", "drWpmB": "480 wpm", "drErrA": "240 wpm",
                            "drErrB": "160 wpm", "drErrDiff": "−80 wpm",
                            "drRatio": "2/3 ≈ 66.7%"}},
                {"id": "worth-it", "label": "A third faster, five right",
                 "wordsA": 400, "secondsA": 100, "correctA": 6, "totalA": 6,
                 "wordsB": 400, "secondsB": 75, "correctB": 5, "totalB": 6,
                 "expect": {"drWpmA": "240 wpm", "drWpmB": "320 wpm", "drErrA": "240 wpm",
                            "drErrB": "≈ 266.7 wpm", "drErrDiff": "≈ +26.7 wpm",
                            "drRatio": "10/9 ≈ 111.1%"}},
            ],
        }),
        "steps_title": "Comparing two readings on another day",
        "steps_intro": (
            "The protocol for any two-reading comparison in this Subject. The last step is "
            "the one that keeps you honest."
        ),
        "steps": [
            ("Use two fresh passages of one kind",
             "Two texts you have not read, as alike in length and difficulty as you can find. "
             "The more they differ, the more of the result is the passages."),
            ("Answer the questions without looking back",
             "The text is hidden for a reason: a question answered by rereading measures the "
             "rereading."),
            ("Multiply before you compare",
             "Rate × right / asked for each reading, then compare the two products, not the "
             "two rates."),
            ("Discount one question",
             "If the scores differ by one question, or the effective rates by less than one "
             "question's worth, call it a tie and repeat the comparison another day, in the "
             "other order."),
        ],
        "worked": {
            "title": "The pushed-too-far preset",
            "intro": [
                "Reading A: 400 words in 100 seconds, six of six right. Reading B: 400 "
                "words in 50 seconds, two of six right.",
            ],
            "lines": [
                "rate A = 400 × 60 / 100 = 240",
                "rate B = 400 × 60 / 50  = 480",
                "effective A = 240 × 6/6 = 240",
                "effective B = 480 × 2/6 = 160",
                "B − A = 160 − 240 = −80",
            ],
            "after": [
                "Twice the rate, a third of the score, two-thirds of the understood words "
                "per minute. Had B kept four questions instead of two, its effective rate "
                "would have been 480 × 4/6 = 320, and the faster reading would have won.",
            ],
        },
        "quiz_title": "Which reading delivered more",
        "quiz": [
            {"q": "Reading A: 300 words a minute with 4 of 6 right. Reading B: 250 words a "
                  "minute with 6 of 6 right. Which has the higher effective rate?",
             "a": ["A, at 300 against 250", "B, at 250 against 200",
                   "They are equal", "A, at 200 against 166.7"],
             "c": 1,
             "why": "A: 300 × 4/6 = 200. B: 250 × 6/6 = 250. The slower reading delivered "
                    "more understood words per minute."},
            {"q": "In the pushed-too-far preset, reading B runs at 480 words a minute with "
                  "2 of 6 right. What is its effective rate?",
             "a": ["80 words a minute", "240 words a minute", "160 words a minute",
                   "320 words a minute"],
             "c": 2,
             "why": "480 × 2/6 = 160. Eighty is one question's worth, and 320 would need four "
                    "questions right."},
            {"q": "Two natural-pace readings score 5 of 6 and 4 of 6. What does the lesson "
                  "let you conclude about comprehension?",
             "a": ["It fell by about 16.7 points, one question, which is not a result",
                   "It fell by a third, which is a clear decline",
                   "It fell, so the second reading was less careful",
                   "The second passage was harder"],
             "c": 0,
             "why": "One question in six is about 16.7 points, and a one-question difference "
                    "can be a lapse or a guess. Nothing here says which passage was harder."},
            {"q": "A reader's fast reading came out ahead of the natural one on effective "
                  "rate. What follows?",
             "a": ["The usual result is wrong for every reader",
                   "One pair of readings on two passages went this way, nothing more",
                   "The reader should always read as fast as possible",
                   "The questions on the fast passage must have been easier"],
             "c": 1,
             "why": "Two readings differ in passage and in order as well as pace. The pair "
                    "neither refutes the usual result nor is refuted by it, and nothing in "
                    "the drill shows that one passage's questions were easier."},
        ],
        "mistakes": [
            ("“The faster reading is the better reading”",
             "Only if it keeps enough of its score. In the pushed-too-far preset the rate "
             "doubles, from 240 to 480 words a minute, and the effective rate falls from 240 "
             "to 160, because two questions in six survived. The effective rate makes the "
             "trade visible."),
            ("Judging comprehension by how the reading felt",
             "A fast reading can feel fluent and leave little behind, and a slow one can feel "
             "laboured and score six of six. The questions are there because the feeling is "
             "not a measurement."),
            ("Treating a one-question difference as a change",
             "With six questions, one is about 16.7 points. Five against six, or an effective "
             "rate that moves by less than one question's worth, is within what a lapse or a "
             "lucky guess produces."),
        ],
        "standard": (
            "Finish when you can say which of two readings delivered more.",
            "Given two readings, 450 words in 90 seconds with 5 of 6 right and 450 words in "
            "135 seconds with 6 of 6 right, compute both rates and both effective rates "
            "without the lab (rates 300 and 200 words a minute, effective rates 250 and "
            "200) and name the larger effective rate, the first reading's 250.",
        ),
        "note": (
            "Two readings, two passages, one order. The passages differ in kind as well as "
            "content, and whichever reading came first may have helped or tired the second; "
            "the lab alternates the order from one log to the next and records it, but one pair of "
            "readings cannot separate pace from passage or from order."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "one-reading-is-one-measurement",
        "title": "One Reading Is One Measurement",
        "module": "Reading your numbers",
        "one_line": "Take two more natural-pace readings, find the range of your baselines, and see where a fourth reading lands with nothing changed.",
        "summary": (
            "Two more readings at your natural pace complete your baselines. The lab takes "
            "the range of the first three and asks where a later reading falls against it. "
            "With nothing changed, a fourth reading lands above the range about one time in "
            "four, which is why this Subject waits for the median of three tests."
        ),
        "key": [
            "range = lowest to highest baseline",
            "4 readings: each the top 1 time in 4",
            "above once: what chance does 1 in 4",
            "change: median of last 3 tests above",
        ],
        "key_label": "The noise in four lines",
        "concepts_intro": (
            "Every number in this Subject is compared with something. This lesson is about "
            "how much it moves when nothing is changed at all."
        ),
        "concepts": [
            ("The baseline range",
             "The lowest and highest of your first three natural-pace rates. Its width is "
             "how far your rate moves between passages and sittings when you are not trying "
             "to change anything."),
            ("A fourth reading is the top one time in four",
             "If nothing has changed, each of four readings is equally likely to be the "
             "fastest. So a later reading lands above the range of three earlier ones about "
             "one time in four, below it one time in four, and inside only half the time."),
            ("The rule: a median of three",
             "This Subject calls a change real when the median of your last three tests is "
             "above the baseline range. One lucky reading cannot move a median; it takes at "
             "least two."),
        ],
        "read_title": "How far a rate moves on its own",
        "read_intro": (
            "Your range, what chance does to a later reading, and the rule the rest of the "
            "Subject uses."
        ),
        "body": [
            ("p", "Start with the two warm-up readings above the lab: “The Seed Tin”, then "
                  "“Lights on the Coast”, each at your natural pace with its six questions, "
                  "a minute or two apart. The first is logged as a baseline and the second "
                  "as a test. Then press “Use my baselines”."),
            ("p", "The button fills the first box with the rates of your three baselines: "
                  "“The Church Clock at Wexley”, your natural-pace reading in Comprehension "
                  "and the Effective Rate, and “The Seed Tin”. It puts your fourth reading, "
                  "“Lights on the Coast”, in the test box, and that one is the experiment. "
                  "Nothing changed between it and the others, so see what the lab makes of "
                  "a reading with no reason to differ."),
            ("def", ("Baseline range",
                     "Your <strong>baseline range</strong> runs from the lowest to the "
                     "highest of your first three natural-pace rates, in words a minute. A "
                     "later reading is <strong>inside</strong> it, "
                     "<strong>above</strong> it or <strong>below</strong> it.")),
            ("p", "The tight preset is a reader whose baselines were 238, 251 and 245: a "
                  "mean of about 244.7 and a range from 238 to 251, 13 wide. A later test "
                  "at 247 is inside. The wide preset is a reader at 212, 268 and 240, a "
                  "range 56 wide, and there a later 262 is inside too. Readers differ in how "
                  "much they vary, and so do passages: a rate depends on the passage as well "
                  "as on the reader (Carver 1990)."),
            ("p", "Now the arithmetic of chance. Take four readings of passages of one kind "
                  "with nothing changed between them. Each is as likely as any other to be "
                  "the fastest of the four, so the fourth is the fastest one time in four, "
                  "and then it is above the range of the first three. It is the slowest one "
                  "time in four as well. A reading with no reason to differ lands outside "
                  "the range half the time."),
            ("p", "The one-high preset is the tight reader with a later test at 262: 11 "
                  "above the top of the range. The lab's verdict is “above the baseline "
                  "range once — a fourth reading does this about one time in four”, and "
                  "that is all one reading can say. It is the result you were hoping for, "
                  "and it is also what chance alone produces one time in four."),
            ("p", "So the Subject asks for more. A change counts as evidence when the median "
                  "of your last three tests is above the baseline range. The three-high "
                  "preset is the tight reader with tests at 262, 270 and 258: their median "
                  "is 262, above 251, and the verdict reads “above the baseline range on "
                  "the median of the last three tests”. A median moves only when at least "
                  "two of the three move."),
            ("math", [
                "range       = 238 to 251",
                "one test    = 262          above once",
                "three tests = 262, 270, 258",
                "median      = 262 > 251    above on the median",
            ]),
            ("p", "So when you see your own fourth reading, read it as what it is. If it "
                  "landed inside, your range already covers ordinary variation. If it landed "
                  "above or below, you have seen at first hand what one reading can do on "
                  "its own, before any technique has been tried. The lab compares rates in "
                  "words a minute here; Keeping a Practice Log applies the same rule to "
                  "effective rates."),
            ("p", "Next, Typical Rates and Reading Gears: your baseline median against the "
                  "published figures, each in its own unit."),
        ],
        "lab": ("readkit", {
            "mode": "log",
            "view": "noise",
            "warmup": [PASSAGES["P04"], PASSAGES["P05"]],
            "warmup_kind": ["baseline", "test"],
            "preset": "tight",
            "presets": [
                {"id": "tight", "label": "Baselines 238, 251, 245; test 247",
                 "base": [238, 251, 245], "tests": [247],
                 "expect": {"lgMean": "≈ 244.7 wpm", "lgRange": "13 wpm",
                            "lgTestMedian": "247 wpm (of 1)",
                            "lgVerdict": "inside the baseline range"}},
                {"id": "wide", "label": "Baselines 212, 268, 240; test 262",
                 "base": [212, 268, 240], "tests": [262],
                 "expect": {"lgRange": "56 wpm", "lgTestMedian": "262 wpm (of 1)",
                            "lgVerdict": "inside the baseline range"}},
                {"id": "one-high", "label": "Tight baselines; one test at 262",
                 "base": [238, 251, 245], "tests": [262],
                 "expect": {"lgRange": "13 wpm", "lgTestMedian": "262 wpm (of 1)",
                            "lgVerdict": ONCE}},
                {"id": "three-high", "label": "Tight baselines; tests 262, 270, 258",
                 "base": [238, 251, 245], "tests": [262, 270, 258],
                 "expect": {"lgRange": "13 wpm", "lgTestMedian": "262 wpm",
                            "lgVerdict": MEDIAN}},
            ],
        }),
        "steps_title": "Checking a reading against your range",
        "steps_intro": (
            "What to do each time a test reading comes in, from now to the end of the Subject."
        ),
        "steps": [
            ("Keep the baseline fixed",
             "Your range is the lowest and highest of your first three natural-pace readings. "
             "Do not recompute it from later readings: a range that moves with the tests "
             "cannot measure them."),
            ("Place the latest test",
             "Inside, above or below. Above once is what chance does one time in four; write "
             "it down and do not act on it."),
            ("Wait for three tests",
             "Take the median of the last three. Above the range is the Subject's evidence of "
             "a change; inside is no change yet."),
            ("Test on fresh passages at natural pace",
             "A test is a reading like the baselines: a passage you have not read, no pacer, "
             "six questions. Anything else is practice and is logged as such."),
        ],
        "worked": {
            "title": "The wide reader",
            "intro": [
                "Baselines at 212, 268 and 240 words a minute; one later test at 262.",
            ],
            "lines": [
                "lowest = 212, highest = 268",
                "range  = 268 − 212 = 56 wide",
                "test   = 262, and 212 ≤ 262 ≤ 268",
                "verdict: inside the baseline range",
            ],
            "after": [
                "The same 262 is above the tight reader's range of 238 to 251. A test means "
                "something only against the range of the reader who took it.",
            ],
        },
        "quiz_title": "Inside, above, or a change",
        "quiz": [
            {"q": "A reader's baselines are 230, 252 and 241 words a minute. What is the "
                  "baseline range?",
             "a": ["241 to 252", "230 to 252, 22 wide", "About 241, the mean",
                   "230 to 241, 11 wide"],
             "c": 1,
             "why": "The range runs from the lowest baseline to the highest: 230 to 252, "
                    "which is 22 wide."},
            {"q": "The same reader's first test is 255. What is the verdict?",
             "a": ["A real improvement of 3 words a minute",
                   "Inside the baseline range",
                   "Above the range once, which chance does about one time in four",
                   "Above the range on the median of three tests"],
             "c": 2,
             "why": "255 is above 252, but it is one reading. A fourth reading with nothing "
                    "changed is the fastest of four one time in four."},
            {"q": "Later tests are 249, 258 and 262. What is the verdict now?",
             "a": ["Above the range on the median of the last three tests",
                   "Inside the range, because 249 is inside",
                   "Above the range once",
                   "No verdict until a fourth test"],
             "c": 0,
             "why": "The median of 249, 258 and 262 is 258, which is above 252. One test "
                    "inside the range does not pull the median down."},
            {"q": "Why does a fourth reading, with nothing changed, land above the range of "
                  "the first three about one time in four?",
             "a": ["Readers improve a little with every reading",
                   "One question is worth about 16.7 points",
                   "Carver found that rates vary by about a quarter",
                   "Each of the four is equally likely to be the fastest"],
             "c": 3,
             "why": "With nothing changed the four readings are interchangeable, so the "
                    "fourth is the fastest one time in four. Improvement would make it "
                    "more often, not explain the one in four."},
        ],
        "mistakes": [
            ("“My rate on one test is my reading speed”",
             "One test is one passage on one day. The wide preset's reader read at 212 and "
             "at 268 with nothing changed, 56 words a minute apart; the tight reader's 13 "
             "is still more than many claimed gains. A rate describes a reading, not a "
             "reader."),
            ("“A reading above my range means I improved”",
             "With nothing changed, a fourth reading is above the range of three about one "
             "time in four. The one-high preset's 262 is a hopeful sign and nothing more "
             "until two more tests agree."),
            ("Comparing a test with the average of the baselines",
             "Half of all readings with nothing changed are above the middle. A test beside "
             "the mean of 244.7 says even less than a test beside the range, which is why the "
             "verdict uses the range."),
        ],
        "standard": (
            "Finish when you can give the verdict without the lab.",
            "Given baselines of 236, 249 and 243 and later tests of 251, 254 and 247, compute "
            "the range (236 to 249) and the median of the tests (251), and say that the change "
            "counts as evidence by the Subject's rule because 251 is above 249, while 247 on "
            "its own would have been inside.",
        ),
        "note": (
            "The rule is a rule of thumb, not a guarantee: with nothing changed, the median of "
            "three tests still clears a range of three baselines about one time in five, "
            "because that happens whenever the two fastest of six readings are both tests. "
            "That is why the verdict is read again each week, never once. This lab uses all "
            "your baselines for the range, and compares rates in words."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "typical-rates-and-reading-gears",
        "title": "Typical Rates and Reading Gears",
        "module": "Reading your numbers",
        "one_line": "Place your baseline against Brysbaert's averages in words and Carver's five gears in standard-length words, and name what each gear is for.",
        "summary": (
            "Your baseline median is compared twice: in words with Brysbaert's average for "
            "silent reading, and in standard-length words with Carver's five gears, from "
            "scanning to memorising. The gears are purposes with typical rates, measured on "
            "college students, and the unit decides which one a number lands nearest."
        ),
        "key": [
            "standard rate = rate × (chars/word) / 6",
            "scanning 600, skimming 450",
            "rauding 300, learning 200",
            "memorising 138 (standard words)",
            "Brysbaert: about 238 words, nonfiction",
        ],
        "key_label": "Two references, two units",
        "concepts_intro": (
            "A rate means something beside a reference, and each reference has a unit and a "
            "population. Use the wrong unit and the comparison says something false."
        ),
        "concepts": [
            ("Two references in two units",
             "Brysbaert's average of about 238 is in words, for adults reading English "
             "nonfiction silently. Carver's gears are in six-character standard words, for "
             "college students on his materials. A rate is compared with each in that one's "
             "own unit."),
            ("A gear is a purpose",
             "Carver's five gears are five ways of reading with five goals: finding a word, "
             "getting the drift, understanding each sentence, learning, and memorising. The "
             "rate goes with the goal."),
            ("Most readers stay in one gear",
             "Carver (1992) found that most readers hold a fairly constant rate, their "
             "rauding rate, whatever they read, and seldom shift gear. He recommended "
             "shifting deliberately."),
        ],
        "read_title": "Your rate against the published figures",
        "read_intro": (
            "The gears, what each is for, and what happens to a comparison when the unit is "
            "wrong."
        ),
        "body": [
            ("p", "Begin with the warm-up above the lab, “The Night Train”, at your natural "
                  "pace. It is logged as practice and does not change your baselines. Then "
                  "press “Use my baseline median”: the lab takes the median of your three "
                  "baselines, in words a minute and, from the characters you read, in "
                  "standard-length words."),
            ("p", "Carver (1990) described reading as five processes, each with its own "
                  "typical rate for college students, measured in standard-length words a "
                  "minute:"),
            ("ul", [
                "<strong>Scanning</strong>, about 600: looking for a particular word or "
                "number, without reading the rest.",
                "<strong>Skimming</strong>, about 450: getting the drift of a text without "
                "understanding every sentence.",
                "<strong>Rauding</strong>, about 300: ordinary reading, understanding each "
                "sentence as you go. The word is Carver's, from reading and auding.",
                "<strong>Learning</strong>, about 200: reading to take in and keep what a "
                "text says, slowing and going back where needed.",
                "<strong>Memorising</strong>, about 138: reading until you could recall the "
                "text, with rehearsal.",
            ]),
            ("p", "The average preset is a reader at Brysbaert's 238 words a minute on text "
                  "whose words average 6.6 characters with their space. In standard words "
                  "that is 238 × 6.6 / 6 = 261.8, which is 38.2 from rauding's 300 and 61.8 "
                  "from learning's 200, so the nearest gear is rauding; against the average "
                  "of 238 it is 100%."),
            ("p", "The short-words preset is the same 238 words a minute on text like this "
                  "course's passages, about 5.4 characters a word with the space: 238 × 5.4 / "
                  "6 = 214.2 standard words a minute, and the nearest gear becomes "
                  "learning. Nothing about the reading changed. The unit did, and Carver's "
                  "figures are for college students, while Brysbaert argues that the "
                  "familiar 300 overstates ordinary silent reading. So read the nearest gear "
                  "as a comparison of numbers, not as a description of what you were doing: "
                  "if you were reading each sentence for its sense, you were rauding, at your "
                  "own rate."),
            ("p", "The slower preset is 190 words a minute on the long-word text, 209 "
                  "standard: nearest gear learning, and 95/119, about 79.8% of the average. "
                  "The claim preset is 1,000 words a minute, 1,100 standard: above every "
                  "gear, and about 420.2% of the average. No gear in Carver's table runs "
                  "that fast, and Testing a Speed Claim shows how to check a figure like "
                  "that with the questions it needs."),
            ("p", "If there are five gears, the natural thought is that a good reader moves "
                  "between them. Carver (1992) found that most readers do not: they hold a "
                  "relatively constant rauding rate across what they read and seldom shift "
                  "gear, and he recommended shifting deliberately, by purpose. Shifting "
                  "Gears, in Skimming, Scanning and Previewing, practises it."),
            ("p", "Your own number may well land nearer learning than rauding on these "
                  "passages, because their words are short: below about 278 words a minute, "
                  "5.4 characters a word puts you under 250 standard words, the halfway "
                  "point. That is the unit at work. The "
                  "comparison that will matter from here on is with your own baselines."),
            ("p", "Next, Keeping a Practice Log: which readings count, and how the log turns "
                  "them into a verdict."),
        ],
        "lab": ("readkit", {
            "mode": "log",
            "view": "gears",
            "warmup": PASSAGES["P09"],
            "warmup_kind": "practice",
            "preset": "average",
            "presets": [
                {"id": "average", "label": "238 words a minute, long words",
                 "wpm": 238, "stdwpm": "261.8",
                 "expect": {"lgNearest": "rauding, 300 standard wpm", "lgVsAverage": "1 = 100%"}},
                {"id": "short-words", "label": "238 words a minute, short words",
                 "wpm": 238, "stdwpm": "214.2",
                 "expect": {"lgNearest": "learning, 200 standard wpm", "lgVsAverage": "1 = 100%"}},
                {"id": "slower", "label": "190 words a minute",
                 "wpm": 190, "stdwpm": 209,
                 "expect": {"lgNearest": "learning, 200 standard wpm",
                            "lgVsAverage": "95/119 ≈ 79.8%"}},
                {"id": "claim", "label": "A claimed 1,000 words a minute",
                 "wpm": 1000, "stdwpm": 1100,
                 "expect": {"lgNearest": "above every gear",
                            "lgVsAverage": "500/119 ≈ 420.2%"}},
            ],
        }),
        "steps_title": "Placing a rate against the references",
        "steps_intro": "Four moves, the first two of which are about the unit.",
        "steps": [
            ("Count the characters",
             "Note the characters, spaces included, as well as the words. Without them a rate "
             "in words cannot be put into Carver's unit."),
            ("Convert before you compare with a gear",
             "Standard rate = characters / 6 × 60 / seconds. Compare that, not the rate in "
             "words, with Carver's figures."),
            ("Compare words with words",
             "Set the rate in words beside Brysbaert's 238 for nonfiction or 260 for fiction, "
             "whichever the text was."),
            ("Name the purpose",
             "Say what you were reading for. The gear is the purpose; the nearest number is "
             "a comparison with college students' figures."),
        ],
        "worked": {
            "title": "Brysbaert's average in Carver's unit",
            "intro": [
                "238 words a minute on text averaging 6.6 characters a word, space included.",
            ],
            "lines": [
                "standard rate = 238 × 6.6 / 6 = 261.8",
                "distance to rauding  = 300 − 261.8 = 38.2",
                "distance to learning = 261.8 − 200 = 61.8",
                "nearest gear: rauding",
            ],
            "after": [
                "On text averaging 5.4 characters a word the same 238 is 214.2 standard "
                "words a minute, 14.2 from learning and 85.8 from rauding. The gear a number "
                "lands nearest depends on the text's word length as well as on the reader.",
            ],
        },
        "quiz_title": "Gears and units",
        "quiz": [
            {"q": "A reader reads 250 words a minute on text averaging 5.4 characters a word, "
                  "space included. What is the rate in standard-length words?",
             "a": ["250", "278", "270", "225"],
             "c": 3,
             "why": "250 × 5.4 / 6 = 225. Short words make the standard rate lower than the "
                    "rate in words; 278 comes from multiplying by 6 and dividing by 5.4."},
            {"q": "Which of Carver's gears is ordinary reading, understanding each sentence "
                  "as you go?",
             "a": ["Skimming", "Rauding", "Learning", "Scanning"],
             "c": 1,
             "why": "Rauding, at about 300 standard words a minute for college students. "
                    "Learning is slower and aims to keep what is read; skimming does not try "
                    "to understand every sentence."},
            {"q": "Why does the lab use standard words for the gear and words for the "
                  "average?",
             "a": ["Carver's gears are in standard words and Brysbaert's average is in words",
                   "Standard words are more accurate for every comparison",
                   "Brysbaert converted Carver's figures into words",
                   "The average is for fiction and the gears for nonfiction"],
             "c": 0,
             "why": "Each reference is compared in its own unit. Neither unit is more "
                    "accurate; they answer different questions."},
            {"q": "What did Carver find about most readers and the gears?",
             "a": ["They move between gears as the text demands",
                   "They read fastest in the learning gear",
                   "They hold a fairly constant rauding rate and seldom shift gear",
                   "They read every text in the skimming gear"],
             "c": 2,
             "why": "Carver (1992) found most readers keep a relatively constant rauding "
                    "rate, and recommended shifting gear deliberately."},
        ],
        "mistakes": [
            ("“There is one right speed, and faster is always better”",
             "Carver's gears are five processes with different goals, and the slowest, "
             "memorising, is the right one when you need to recall a text. Carver also found "
             "that most readers seldom shift gear at all; his advice was to shift on purpose, "
             "which Shifting Gears practises."),
            ("Putting a rate in words beside Carver's gears",
             "His figures are in six-character standard words. Brysbaert's 238 words a "
             "minute, set against them unconverted, lands nearest learning, which would call "
             "ordinary reading studying. Convert first, as the average preset does."),
            ("Reading the nearest gear as a diagnosis",
             "Carver's figures are typical rates for college students on his materials. A "
             "natural reading nearest learning, as in the short-words preset, is a "
             "comparison of numbers; what you were doing is what you were reading for."),
        ],
        "standard": (
            "Finish when you can place a rate in the right unit.",
            "Given 260 words a minute on a passage of 500 words and 3,300 characters, "
            "convert to standard-length words without the lab (3,300 / 500 = 6.6 characters "
            "a word, so 286), name the nearest gear (rauding, 14 away) and its purpose, and "
            "compare the rate in words with Brysbaert's 238 for nonfiction.",
        ),
        "note": (
            "The gears are typical rates for college students on Carver's materials, and the "
            "average is an estimate over many studies; neither is a target. The lab finds the "
            "nearest number, with ties going to the slower gear, and cannot know what you "
            "were reading for."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "keeping-a-practice-log",
        "title": "Keeping a Practice Log",
        "module": "Reading your numbers",
        "one_line": "Read your own log: which entries count, the baseline median, the median of the last three tests, and the verdict.",
        "summary": (
            "Every drill in this Subject writes an entry to a log kept in your browser, with "
            "a kind: baseline, test, practice, condition or other. Only baselines and tests "
            "count toward a verdict, scored by effective rate. Read your log, read three "
            "example logs, and export yours as text."
        ),
        "key": [
            "counted: baseline and test readings",
            "effective rate = rate × right / asked",
            "baseline sessions: the range",
            "verdict: median of last three tests",
        ],
        "key_label": "A log in four lines",
        "concepts_intro": (
            "A log is the only place a change can show, and only if it keeps the readings "
            "that measure apart from the ones that train."
        ),
        "concepts": [
            ("Every entry has a kind",
             "Baseline and test readings are natural-pace readings of fresh passages with "
             "questions, and they are what verdicts use. Practice, condition and other "
             "entries are kept and listed, and never counted."),
            ("The log scores effective rates",
             "Each counted session is scored as rate × comprehension, so a reading that got "
             "faster by understanding less does not look like progress."),
            ("The verdict uses the rule",
             "The baseline sessions set the baseline range; the median of the last three "
             "tests is compared with it, and a single test only says “once”."),
        ],
        "read_title": "What the log keeps, and what it counts",
        "read_intro": (
            "The kinds, the three example logs, and what to do with your own."
        ),
        "body": [
            ("p", "Start with the warm-up above the lab, “The Market Before Dawn”, logged as "
                  "practice. The lab then shows your own log: every entry you have made in "
                  "this Subject, the counted ones in full and the rest greyed, with the tiles "
                  "computed from the counted ones."),
            ("p", "Each entry carries one of five kinds, set by the drill that wrote it:"),
            ("ul", [
                "<strong>baseline</strong>: a natural-pace reading of a fresh passage, with "
                "questions, before any technique. This course took three.",
                "<strong>test</strong>: a reading made like a baseline, later, to see whether "
                "anything has changed.",
                "<strong>practice</strong>: a reading done to train, with a pacer or on the "
                "Daily Drill; drawn as a lighter series on the chart.",
                "<strong>condition</strong>: one side of a comparison, such as your "
                "as-fast-as-you-can reading.",
                "<strong>other</strong>: notes, plans and drills that are not readings.",
            ]),
            ("p", "The lab scores each counted session by its effective rate, puts your "
                  "baselines first and treats them as the baseline. After this course your "
                  "log should hold four sessions: three baselines and “Lights on the Coast”, "
                  "your first test, which One Reading Is One Measurement set against the "
                  "range by its rate."),
            ("p", "The starting preset is a log with three baselines, at effective rates of "
                  "238, 251 and 245: a baseline median of 245 and the verdict “needs a "
                  "reading after the three baselines”. Three readings make a range; they "
                  "cannot test it."),
            ("p", "The six-weeks preset adds four tests, at effective rates of 255, 262, 270 "
                  "and 266, among practice readings that are drawn but not counted. Seven "
                  "sessions; the last three tests have a median of 266, above the top of the "
                  "range at 251, so the verdict is “above the baseline range on the median of "
                  "the last three tests”."),
            ("p", "The speed-only preset is the warning. Its three tests ran at 288, 354 and "
                  "488 words a minute, each faster than the last, with five, four and three "
                  "questions right. Their effective rates are 240, 236 and 244, a median of "
                  "240, and the verdict is “inside the baseline range”. Those readings felt "
                  "faster and were faster in words; in understood words they did not move."),
            ("p", "The log lives in this browser only. “Export as text” writes it out as "
                  "comma-separated lines you can keep in a file, “Add note” records "
                  "something the numbers cannot, such as a bad night's sleep, and “Clear my "
                  "log” asks for a second press before it deletes anything."),
            ("p", "That is the measuring done. The next course, Guided Practice, starts the "
                  "practice the log is for: a pacer, a target pace, and the Daily Drill."),
        ],
        "lab": ("readkit", {
            "mode": "log",
            "view": "history",
            "warmup": PASSAGES["P10"],
            "warmup_kind": "practice",
            "preset": "six-weeks",
            "presets": [
                {"id": "starting", "label": "Example: three baselines",
                 "entries": [(238, 6, 6), ("301.2", 5, 6), (294, 5, 6)],
                 "expect": {"lgSessions": "3", "lgBaseMedian": "245 wpm",
                            "lgRecentMedian": "after 6 sessions",
                            "lgVerdict": "needs a reading after the three baselines"}},
                {"id": "six-weeks", "label": "Example: six weeks of tests",
                 "entries": [(238, 6, 6), ("301.2", 5, 6), (294, 5, 6),
                             (306, 5, 6), (262, 6, 6), (324, 5, 6), ("319.2", 5, 6)],
                 "practice": [(270, 5, 6), (282, 4, 6), (300, 5, 6), (288, 5, 6),
                              (315, 4, 6), (312, 5, 6), (330, 5, 6), (324, 5, 6)],
                 "expect": {"lgSessions": "7", "lgBaseMedian": "245 wpm",
                            "lgRecentMedian": "266 wpm", "lgLatestErr": "266 wpm",
                            "lgVerdict": MEDIAN}},
                {"id": "speed-only", "label": "Example: faster, not better",
                 "entries": [(238, 6, 6), ("301.2", 5, 6), (294, 5, 6),
                             (288, 5, 6), (354, 4, 6), (488, 3, 6)],
                 "expect": {"lgSessions": "6", "lgBaseMedian": "245 wpm",
                            "lgRecentMedian": "240 wpm", "lgLatestErr": "244 wpm",
                            "lgVerdict": "inside the baseline range"}},
            ],
        }),
        "steps_title": "Keeping the log honest",
        "steps_intro": (
            "Four habits for the rest of the Subject. The log can only count what you let it."
        ),
        "steps": [
            ("Let every drill log its kind",
             "Do not repeat a drill to replace a bad reading. A low reading is part of your "
             "range, and deleting it makes every later verdict too generous."),
            ("Make tests like the baselines",
             "Natural pace, a fresh passage, no pacer, six questions. A test done any other "
             "way is a different measurement and is not comparable."),
            ("Read the verdict, not the latest rate",
             "After each test, look at the verdict tile. “Once” is a hopeful sign; the "
             "median of three is the Subject's evidence."),
            ("Export it now and then",
             "Press “Export as text” and keep the lines in a file. A cleared browser clears "
             "the log, and the export is the only copy."),
        ],
        "worked": {
            "title": "The six-weeks verdict",
            "intro": [
                "Baselines at effective rates 238, 251 and 245; tests at 255, 262, 270 and 266.",
            ],
            "lines": [
                "baseline range = 238 to 251",
                "last three tests = 262, 270, 266",
                "median = 266",
                "266 > 251: above on the median of three",
            ],
            "after": [
                "The first test, 255, drops out of the median once three later tests arrive. "
                "The practice readings in between, however fast, are not part of it.",
            ],
        },
        "quiz_title": "Reading a log",
        "quiz": [
            {"q": "Which entries does the lab use for the verdict?",
             "a": ["Every reading in the log",
                   "Practice and test readings",
                   "Baseline and test readings with questions",
                   "Only the test readings"],
             "c": 2,
             "why": "Baselines set the range and tests are compared with it; practice, "
                    "condition and other entries are listed and not counted."},
            {"q": "Three tests ran at 288, 354 and 488 words a minute, with 5, 4 and 3 of 6 "
                  "right. What are their effective rates?",
             "a": ["288, 354 and 488", "240, 236 and 244", "240, 295 and 407",
                   "48, 118 and 244"],
             "c": 1,
             "why": "288 × 5/6 = 240, 354 × 4/6 = 236 and 488 × 3/6 = 244. The rate rose "
                    "by 200 words a minute; the effective rate did not move."},
            {"q": "A pacer reading at 320 words a minute scores 6 of 6, logged as practice. "
                  "What does it do to the verdict?",
             "a": ["Nothing: practice readings are not counted",
                   "It counts as a test above the range",
                   "It replaces the lowest baseline",
                   "It raises the median of the last three tests"],
             "c": 0,
             "why": "A pacer reading is a different condition, and the log keeps it apart. "
                    "It appears as the lighter series on the chart."},
            {"q": "Baselines are 238, 251 and 245; tests are 255, 262, 270 and 266, all "
                  "effective rates. What is the verdict?",
             "a": ["Inside the baseline range",
                   "Above the range once",
                   "Needs a reading after the three baselines",
                   "Above the range on the median of the last three tests"],
             "c": 3,
             "why": "The last three tests, 262, 270 and 266, have a median of 266, above 251."},
        ],
        "mistakes": [
            ("“Practice that feels faster is faster”",
             "Felt speed and effective rate come apart. In the speed-only preset the tests "
             "rose from 288 to 488 words a minute and their effective rates stayed at 240, "
             "236 and 244, inside the range. Only the tests in the log can say."),
            ("Counting every reading",
             "A reading with a pacer, or one done as fast as you can, measures that "
             "condition. Mixed into the tests, it would make a technique look like a change "
             "in you."),
            ("Testing on a passage you have already read",
             "A second reading of a text measures memory as well as reading. A test belongs "
             "on a passage you have never seen, as the baselines were."),
        ],
        "standard": (
            "Finish when you can give a log's verdict by hand.",
            "Given a log of baselines at effective rates 240, 236 and 247, practice readings "
            "at 260 and 280, and tests at 250, 245 and 252, pick out the entries that count, "
            "compute the range (236 to 247) and the median of the last three tests (250), "
            "and state the verdict: above the baseline range on the median of the last three "
            "tests.",
        ),
        "note": (
            "The log is kept in this browser and nowhere else: another device or a cleared "
            "browser starts empty, and only the export keeps a copy. The lab treats every "
            "reading logged as a baseline as the baseline and every test as a test; a "
            "verdict waits for three baselines."
        ),
    },
]
