"""Course 2, lessons 01-05 -- the pacer, a target pace, the Daily Drill,
sprints above comfort, and repeated reading against a new passage."""

from reading.passages import PASSAGES

ONE_Q = "One question is ≈ 16.7 points; a one-question difference is not a result."

# The Daily Drill's pool, served in order. PLAN §C 2.3 names Q01-Q18 and
# Q26-Q28 (21 passages); with this lesson's text the page is 69.9 KB gzipped
# at 21, against the library's 67 KB ceiling, and 66.2 KB at 18. So the page
# carries Q01-Q15 and Q26-Q28: easy, then standard, then hard. Q16-Q18 are
# left for the orchestrator to place (see the author's report).
DAILY_POOL = [PASSAGES["Q%02d" % n] for n in list(range(1, 16)) + [26, 27, 28]]

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "reading-with-a-pacer",
        "title": "Reading with a Pacer",
        "module": "The pacer",
        "one_line": "Read one passage at your own pace and a matched one behind a moving highlight, and compare the understood words per minute of each.",
        "summary": (
            "A pacer is a highlight that moves down the passage line by line at a "
            "rate you set, the screen's version of the hand the speed-reading "
            "courses taught readers to sweep down the page. The drill times a "
            "passage at your natural pace and a matched one with the pacer at the "
            "middle of your baselines, scores both, and compares their effective "
            "rates. The lab computes the time the pacer gives a line, and how much "
            "of a difference one question is worth."
        ),
        "key": [
            "line time (ms) = words × 60,000 / target",
            "12 words at 250: 2,880 ms a line",
            "effective rate = rate × comprehension",
            "one question in six ≈ 16.7 points",
            "compare effective rates, not rates",
        ],
        "key_label": "The pacer in five lines",
        "concepts_intro": (
            "Three ideas the drill rests on. None of them says what you will find; "
            "that is what the drill is for."
        ),
        "concepts": [
            ("A pacer sets the pace, line by line",
             "The highlight moves to the next line after that line's words × "
             "60,000 / target milliseconds, so a line of twelve words at 250 words "
             "a minute is lit for 2,880 ms. Your eyes still do the reading; the "
             "highlight only says when to move on."),
            ("The question is the effective rate",
             "A pacer holds a rate up whether or not you understand, because the "
             "highlight moves either way. So the comparison is of understood words "
             "per minute, the rate times the share of questions right, on two "
             "passages of the same length and difficulty."),
            ("One comparison, two confounds",
             "The two readings are of different passages, and one of them came "
             "first. Either can move a result as much as a technique does, which "
             "is why the lab alternates the order from one comparison to the next "
             "and why the result is read as one measurement."),
        ],
        "read_title": "What the two readings measured",
        "read_intro": (
            "Do the two readings first. What follows starts from what most readers "
            "find, and then shows how much of a difference one question can make."
        ),
        "body": [
            ("p", "Before you read on, do the drill below: two timed readings, one at "
                  "your usual pace and one with the pacer, each followed by six "
                  "questions. Before you start the paced reading, type into its "
                  "target box the middle of your baseline rates from Measure Your "
                  "Reading (240 if you have none), and read the two in the order the "
                  "lab gives."),
            ("p", "Now look at your two readings side by side. The paced rate probably "
                  "came out close to the target, because the highlight set it: if you "
                  "kept to the lit line, the reading ended when the highlight left the "
                  "last line. So the rate says little on its own, and the drill's real "
                  "question is the other one: with the pace fixed, did you understand "
                  "as much? Some readers find the highlight steadies them and their "
                  "score holds; others find it hurries them past a sentence they "
                  "wanted to read again, and the score drops. Your two effective rates "
                  "say which happened today."),
            ("h3", "Where the pacer comes from"),
            ("p", "The pacer is the oldest technique in the speed-reading tradition. "
                  "The Evelyn Wood courses, from 1959, taught readers to sweep a hand "
                  "down the page and let the eyes follow it, on the claim that the "
                  "hand keeps a reader moving, keeps the mind from drifting and "
                  "stops the eyes going back over lines already read. The "
                  "review of the research that Keith Rayner wrote with four "
                  "colleagues, published in 2016 after his death, describes the "
                  "method and explains why no guide can widen what the eye takes in "
                  "at each stop. What a guide can do is set a steady pace and "
                  "discourage drifting and needless going back. How the Eyes Read "
                  "shows why the stops set the limit."),
            ("p", "On this page the pacer is a highlight with an underline. When you "
                  "press Start, the lab groups the passage's words into lines as your "
                  "screen has laid them out, and lights each line for its words × "
                  "60,000 / target milliseconds. A long line stays lit longer than a "
                  "short one, so the pace in words a minute is the same whatever the "
                  "layout. The tile for the pacer's time per line is computed for a "
                  "stated line of twelve words: at a target of 250, 12 × 60,000 / 250 "
                  "= 2,880 ms."),
            ("p", "The preset <strong>steadier</strong> is one plausible pair of "
                  "readings. Reading A, unpaced: 442 words in 110.5 seconds, 240 words "
                  "a minute, with 4 of 6 right, so an effective rate of 240 × 4/6 = "
                  "160. Reading B, with the pacer at 250: 418 words in 100.32 seconds, "
                  "250 words a minute, 5 of 6 right, an effective rate of ≈ 208.3. B "
                  "is ahead by ≈ 48.3 understood words a minute, and it is tempting to "
                  "stop there."),
            ("p", "Look at where the 48.3 comes from. B's rate is only 10 words a "
                  "minute higher; nearly all the difference is one more question "
                  "right. One question in six is ≈ 16.7 points of comprehension, and "
                  "at 250 words a minute it is worth 250/6 ≈ 41.7 understood words a "
                  "minute. Give B four right instead of five and its effective rate is "
                  "250 × 4/6 ≈ 166.7, only ≈ 6.7 above A. A one-question difference "
                  "is not a result: a slightly easier question or a moment's "
                  "inattention moves it."),
            ("p", "The preset <strong>no-difference</strong> keeps both rates and "
                  "gives both readings 5 of 6. A is 240 × 5/6 = 200, B is ≈ 208.3, a "
                  "difference of ≈ 8.3, made only of the 10 words a minute the target "
                  "was set above A's rate. That is the highlight doing what it was "
                  "told, with understanding unchanged. Both presets look like most "
                  "first comparisons: a small difference, inside what one question or "
                  "one passage can produce."),
            ("ul", [
                "Did you finish each line before the highlight moved, or keep up by "
                "letting words go?",
                "Did you want to look back at a line and find it had gone dark?",
                "Was your attention on the text or on the highlight?",
            ]),
            ("p", "Those three questions are worth answering in a sentence in your "
                  "log, because the numbers cannot. Whichever way your comparison "
                  "went, it is one comparison. If the pacer cost you comprehension, "
                  "you have not refuted the readers who say it steadies them, and "
                  "they have not refuted you; if it helped, the same holds the other "
                  "way. The pacer stays in this course as a practice tool: a way of "
                  "holding a pace you choose for a whole passage."),
            ("p", "The next lesson, Choosing a Target Pace, sets the pacer above your "
                  "natural rate in three steps and finds the fastest of them at which "
                  "you still understand."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P12"], PASSAGES["P13"]],
            "a": {"label": "Reading A, your usual pace", "kind": "test"},
            "b": {"label": "Reading B, with the pacer", "display": "pacer", "target": 250,
                  "kind": "condition"},
            "lineWords": 12,
            "ratioOf": "err",
            "order": "alternate",
            "preset": "steadier",
            "presets": [
                {"id": "steadier", "label": "steadier: B one question better",
                 "wordsA": 442, "secondsA": "110.5", "correctA": 4, "totalA": 6,
                 "wordsB": 418, "secondsB": "100.32", "correctB": 5, "totalB": 6, "targetB": 250,
                 "expect": {"drErrA": "160 wpm", "drErrB": "≈ 208.3 wpm", "drErrDiff": "≈ +48.3 wpm", "drPacerLineMs": "2,880 ms"}},
                {"id": "no-difference", "label": "no-difference: the same score",
                 "wordsA": 442, "secondsA": "110.5", "correctA": 5, "totalA": 6,
                 "wordsB": 418, "secondsB": "100.32", "correctB": 5, "totalB": 6, "targetB": 250,
                 "expect": {"drErrA": "200 wpm", "drErrB": "≈ 208.3 wpm", "drErrDiff": "≈ +8.3 wpm", "drPacerLineMs": "2,880 ms"}},
            ],
            "panel_title": "Your two readings, in numbers",
            "panel_intro": (
                "Your measurement: before you start Reading B, type the middle of "
                "your baseline rates into its target box (240 if you have none). "
                "Press Start, read, press Done, answer the questions and press Score "
                "for each reading, in the order shown; the boxes fill with what you "
                "did. Until then they hold a worked example. " + ONE_Q
            ),
        }),
        "steps_title": "Comparing paced and unpaced reading on another day",
        "steps_intro": (
            "The same comparison, on fresh passages, whenever you want a second "
            "measurement. Two readings are enough for one sitting."
        ),
        "steps": [
            ("Set the target from your log",
             "Take the middle of your baseline rates, or of your last three tests "
             "if you have them, and type it as the pacer's target. A target far "
             "above your rate turns the comparison into a sprint."),
            ("Read in the order you are given",
             "Read the unpaced passage and the paced one in whichever order the "
             "lab sets, at the same time of day, without a break long enough to "
             "change how alert you are."),
            ("Answer every question without looking back",
             "The passage is hidden while you answer. Guess when you must; an "
             "unanswered question counts as wrong, and a guess at least has a "
             "chance."),
            ("Read the effective rates, then the questions",
             "Compare the two effective rates, then ask how much of the difference "
             "is one question. If it is all one question, write down that it is "
             "not a result, and note in a sentence how the pacer felt."),
        ],
        "worked": {
            "title": "How long the highlight stays on a line",
            "intro": [
                "A pacer set at 250 words a minute, on a line of twelve words, as the "
                "lab's tile states it.",
            ],
            "lines": [
                "one word = 60,000 / 250 = 240 ms",
                "12 words × 240 ms = 2,880 ms",
                "12 × 60,000 / 250 = 2,880 ms a line",
            ],
            "after": [
                "On a narrow phone screen a line may hold eight words and stay lit for "
                "8 × 240 = 1,920 ms; on a wide one, fifteen words for 3,600 ms. The "
                "time per word, and so the rate, is the same.",
            ],
        },
        "quiz_title": "The pacer's arithmetic",
        "quiz": [
            {"q": "A pacer is set at 300 words a minute. How long does it light a line "
                  "of ten words?",
             "a": ["3,000 ms", "2,000 ms", "200 ms", "1,800 ms"],
             "c": 1,
             "why": "10 × 60,000 / 300 = 2,000 ms. One word gets 60,000 / 300 = 200 "
                    "ms, which is the per-word figure, not the line's."},
            {"q": "In the steadier preset, reading B's effective rate is ≈ 208.3 and "
                  "A's is 160. What would B's effective rate be with one question "
                  "fewer right?",
             "a": ["≈ 166.7", "≈ 191.7", "160", "200"],
             "c": 0,
             "why": "B read at 250 words a minute; with 4 of 6 right its effective rate "
                    "is 250 × 4/6 ≈ 166.7. Nearly all of the 48.3 was one question."},
            {"q": "A reader's paced reading scored one question more than the unpaced "
                  "one, and its effective rate was higher. What can they conclude?",
             "a": ["The pacer improves their comprehension",
                   "The pacer works for them but not for most readers",
                   "Nothing yet: one question, on a different passage, is not a result",
                   "The pacer should now be used for all their reading"],
             "c": 2,
             "why": "One question is ≈ 16.7 points, and the two readings differ in "
                    "passage and in order as well as in the pacer. It takes more "
                    "comparisons, or the log's tests, to say more."},
            {"q": "What does a pacer do, on the account this lesson gives?",
             "a": ["It widens the stretch of text each stop of the eyes takes in",
                   "It sets a steady pace and discourages drifting and needless going back",
                   "It stops the inner voice from sounding the words",
                   "It makes the eyes move between stops faster than they otherwise can"],
             "c": 1,
             "why": "The highlight says when to move on. What each stop of the eyes "
                    "takes in is not changed by it; How the Eyes Read shows why."},
        ],
        "mistakes": [
            ("Thinking the pacer makes the eyes work faster than they can",
             "The highlight cannot reach the eyes' machinery. Reading happens at "
             "the stops the eyes make, and what each stop takes in is set by the "
             "eye, not by a moving line. A pacer sets a steady pace and discourages "
             "drifting and needless going back; if it is set faster than you can "
             "take in the words, it does not speed the stops up, it makes you leave "
             "words behind, and the questions show it."),
            ("Reading the rates instead of the effective rates",
             "The paced reading's rate is close to the target almost by "
             "definition, because the highlight set it. The comparison that says "
             "something is of rate times the share of questions right, and then of "
             "how much of any difference is one question."),
            ("Expecting every line to take the tile's time",
             "The tile states the time for a line of twelve words. Your screen's "
             "lines may hold eight or fifteen, and each is lit for its own words × "
             "60,000 / target. The rate is the same; only the time per line "
             "differs."),
        ],
        "standard": (
            "Finish when you can set a pacer and judge a comparison by hand.",
            "Given a target rate and the words in a line, compute the milliseconds "
            "the line is lit; given two readings' words, seconds and scores, compute "
            "both effective rates and say whether the difference is more than one "
            "question's worth. A verdict on the pacer from one comparison is not "
            "the standard."
        ),
        "note": (
            "The comparison has two confounds the lab cannot remove: the readings "
            "are of different passages, matched in length and difficulty but not "
            "identical, and one came first, so practice or tiredness favours one "
            "side. The lab alternates the order between comparisons, so over "
            "several the order evens out; one comparison is one measurement."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "choosing-a-target-pace",
        "title": "Choosing a Target Pace",
        "module": "The pacer",
        "one_line": "Three paced readings at rising targets find the fastest pace at which you still answer four questions in six.",
        "summary": (
            "Practice with a pacer needs a target, and the useful one is not the "
            "fastest you can follow. Run three paced readings at your baseline rate, "
            "a fifth above it and a half above it, score each, and find your hold "
            "target: the fastest at which comprehension stays at four questions in "
            "six or better. The lab also names the run with the highest effective "
            "rate, which can be a different one."
        ),
        "key": [
            "targets: base × 1, × 6/5, × 3/2",
            "hold = fastest target scoring 4/6 or more",
            "effective rate = rate × comprehension",
            "the hold and the best run can differ",
            "find the hold again on harder text",
        ],
        "key_label": "The ladder in five lines",
        "concepts_intro": (
            "A target pace is a training setting, chosen from your own scores. "
            "Three ideas make the choice."
        ),
        "concepts": [
            ("A ladder of three",
             "Three paced readings of matched passages at your baseline rate, at "
             "six-fifths of it and at three-halves. From a baseline of 240 the "
             "rungs are 240, 288 and 360 words a minute."),
            ("The hold target",
             "The fastest rung at which you answered at least four questions in "
             "six. It is the pace you still understand at, and the pace the Daily "
             "Drill trains at."),
            ("The best run is a different question",
             "The run with the highest effective rate delivered the most "
             "understood words per minute today. It is often a slower rung than "
             "the hold, because a lower score at a higher rate can still be the "
             "smaller product."),
        ],
        "read_title": "Reading the ladder",
        "read_intro": (
            "The ladder is three readings in one sitting, which the Daily Drill "
            "will not ask of you again. It is a measurement taken once, to set a "
            "starting point."
        ),
        "body": [
            ("p", "The drill below is a ladder: three passages, each read with the "
                  "pacer, each at a faster target than the last. Before you start, "
                  "type your own rungs into the three target boxes: your baseline "
                  "rate, that rate × 6/5, and that rate × 3/2. From a baseline of "
                  "240 they are 240, 288 and 360; from 200, they are 200, 240 and "
                  "300. Keep your eyes on the lit line and let each reading end when "
                  "the highlight does."),
            ("p", "The speed-reading tradition's advice is to push: set the guide "
                  "faster than is comfortable and keep raising it, on the view that "
                  "understanding catches up with the pace. The ladder puts that to a "
                  "test you can score. At each rung your rate "
                  "is close to the target, because the highlight set it, and the "
                  "questions say what came with it."),
            ("p", "Two figures come out of three rungs. The <strong>hold "
                  "target</strong> is the fastest rung at which you answered at "
                  "least four of six: the edge of the pace you still understand at. "
                  "The <strong>best run</strong> is the rung with the highest "
                  "effective rate, rate times the share right. They answer different "
                  "questions, and they can name different rungs."),
            ("p", "The preset <strong>holds-at-288</strong> is a reader whose "
                  "comprehension gives way as the pace rises: 6 of 6 at 240, 4 of 6 "
                  "at 288, 2 of 6 at 360. The effective rates are 240 × 6/6 = 240, "
                  "288 × 4/6 = 192 and 360 × 2/6 = 120. The hold target is 288, the "
                  "fastest rung with four right. The best run is 240, the slowest. At "
                  "360 this reader moved through the words half again as fast as at "
                  "240 and took away half as many understood words a minute."),
            ("p", "The preset <strong>holds-at-360</strong> is a reader for whom "
                  "the pace costs little: 5 of 6 at 240, 5 of 6 at 288, 4 of 6 at "
                  "360. The effective rates are 200, 240 and 240. The hold target is "
                  "360. The best effective rate, 240, is a tie between 288 and 360, "
                  "and the lab gives a tie to the slower rung, so it reports 240 at "
                  "288: the same understood words a minute for less effort is the "
                  "better run."),
            ("h3", "Why practise at the hold"),
            ("p", "If the best run is the most understood words a minute, why train "
                  "at the hold instead? Because the two serve different purposes. "
                  "For a reading you need to understand today, the best run's pace "
                  "is the one to read at. For practice, the idea is to work at the "
                  "edge of what you can do while still understanding, which is the "
                  "hold: faster than comfortable, not so fast that the words go by "
                  "unread. Whether practice at that edge raises your natural rate is "
                  "a question your log will answer; this course does not promise "
                  "that it will."),
            ("p", "Read your own ladder the same way. If you answered four or more "
                  "on every rung, your hold is the top rung and the ladder did not "
                  "find your edge: next time, start it at your top rung. If you "
                  "answered fewer than four even at your baseline, the passages may "
                  "have been harder for you than your baseline passages, or the "
                  "pacer itself unsettled you; take the hold as your baseline rate "
                  "for now."),
            ("p", "Every rung is one reading of one passage, and the three passages "
                  "are matched, not identical. One question is ≈ 16.7 points, so a "
                  "rung that scored three instead of four may have been one hard "
                  "question away from holding. If your ladder looks unlike either "
                  "preset, you have not refuted the tradition's advice to push the "
                  "pace, and it has not refuted you. The hold is a starting point the "
                  "Daily Drill adjusts session by session."),
            ("p", "The hold also depends on the text. On easy passages it will be "
                  "higher, on hard ones lower, and the Daily Drill's pool rises from "
                  "easy to hard. When the pool reaches the hard passages, find the "
                  "hold again."),
            ("p", "The next lesson, The Daily Drill, takes your hold target and "
                  "turns it into a routine of ten to fifteen minutes a day."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "ladder",
            "passages": [PASSAGES["P14"], PASSAGES["P15"], PASSAGES["P16"]],
            "targets": [240, 288, 360],
            "display": "pacer",
            "hold": "2/3",
            "kind": "practice",
            "preset": "holds-at-288",
            "presets": [
                {"id": "holds-at-288", "label": "holds-at-288: 6, 4 and 2 right",
                 "t1": 240, "words1": 450, "seconds1": "112.5", "correct1": 6, "total1": 6,
                 "t2": 288, "words2": 450, "seconds2": "93.75", "correct2": 4, "total2": 6,
                 "t3": 360, "words3": 450, "seconds3": 75, "correct3": 2, "total3": 6,
                 "expect": {"drBestTarget": "288 wpm", "drBestErr": "192 wpm", "drTopErr": "240 wpm (target 240 wpm)"}},
                {"id": "holds-at-360", "label": "holds-at-360: 5, 5 and 4 right",
                 "t1": 240, "words1": 450, "seconds1": "112.5", "correct1": 5, "total1": 6,
                 "t2": 288, "words2": 450, "seconds2": "93.75", "correct2": 5, "total2": 6,
                 "t3": 360, "words3": 450, "seconds3": 75, "correct3": 4, "total3": 6,
                 "expect": {"drBestTarget": "360 wpm", "drBestErr": "240 wpm", "drTopErr": "240 wpm (target 288 wpm)"}},
            ],
            "panel_title": "Your ladder, in numbers",
            "panel_intro": (
                "Your measurement: type your three targets into the target boxes "
                "first (your baseline rate, × 6/5 and × 3/2), then run the three "
                "readings in order. Each one fills its own boxes when you press "
                "Score; until then they hold a worked example. Comprehension holds "
                "at 2/3, four questions in six. " + ONE_Q
            ),
        }),
        "steps_title": "Finding your hold target again",
        "steps_intro": (
            "Run the ladder again when the Daily Drill's pool reaches harder "
            "passages, or when your target has drifted far from where it started."
        ),
        "steps": [
            ("Choose three rungs",
             "Take your current rate, from the middle of your last three tests, and "
             "multiply it by 1, 6/5 and 3/2. Type the three into the target boxes "
             "before you start."),
            ("Read each rung with the pacer",
             "Keep your eyes on the lit line and let the highlight end the reading. "
             "Pressing Done early makes the rate yours rather than the target's and "
             "spoils the rung."),
            ("Score each rung honestly",
             "Answer all six questions without looking back. A guess is fine; a "
             "skipped question is a wrong one."),
            ("Read the hold, then the best run",
             "The hold target is the fastest rung with four or more right. Note it "
             "beside the best run's pace in your log, and use the hold in the Daily "
             "Drill."),
        ],
        "worked": {
            "title": "The holds-at-288 ladder",
            "intro": [
                "Three rungs from a baseline of 240, with 6, 4 and 2 questions right "
                "of six.",
            ],
            "lines": [
                "rung 1: 240 × 6/6 = 240",
                "rung 2: 288 × 4/6 = 192",
                "rung 3: 360 × 2/6 = 120",
                "hold: 288 (fastest with 4/6 or more)",
                "best run: 240 (highest effective rate)",
            ],
            "after": [
                "360 × 2/6 = 120 is less than 288 × 4/6 = 192: beyond the hold, the "
                "effective rate falls. The reader practises at 288 and, for a reading "
                "that matters today, reads at 240.",
            ],
        },
        "quiz_title": "Reading a ladder",
        "quiz": [
            {"q": "A reader's baseline rate is 200. What are their three rungs?",
             "a": ["200, 220 and 250", "200, 240 and 300", "200, 250 and 300",
                   "200, 240 and 400"],
             "c": 1,
             "why": "200 × 1 = 200, 200 × 6/5 = 240, 200 × 3/2 = 300."},
            {"q": "A ladder at 250, 300 and 375 scores 5, 4 and 3 questions right of "
                  "six. What is the hold target?",
             "a": ["250", "375", "300", "There is none"],
             "c": 2,
             "why": "The hold is the fastest rung with at least 4 of 6. 375 had 3 of "
                    "6; 300 had 4 of 6, so the hold is 300."},
            {"q": "In that same ladder, which rung has the highest effective rate?",
             "a": ["250, at ≈ 208.3", "300, at 200", "375, at 187.5",
                   "All three are equal"],
             "c": 0,
             "why": "250 × 5/6 ≈ 208.3, 300 × 4/6 = 200, 375 × 3/6 = 187.5. The best "
                    "run is the slowest rung, which is not the hold."},
            {"q": "Why does the Daily Drill practise at the hold target rather than at "
                  "the best run's pace?",
             "a": ["Because the hold always has the higher effective rate",
                   "Because practice works at the edge of the pace you still understand at",
                   "Because the best run's pace is too slow to count as practice",
                   "Because the hold is proven to raise a reader's natural rate"],
             "c": 1,
             "why": "The hold is the fastest pace with comprehension still at four in "
                    "six. It often has the lower effective rate, and no lesson here "
                    "claims that practice at it is proven to raise your rate; your "
                    "log is where that is tested."},
        ],
        "mistakes": [
            ("Setting the pacer as fast as you can follow it",
             "Following a highlight is not the same as reading behind it. Beyond "
             "the hold, the words go by faster than you take them in, and the "
             "effective rate falls: in the holds-at-288 preset, 360 words a minute "
             "with 2 right gives 120 understood words a minute against 192 at 288. "
             "Practise at the fastest pace at which you still understand."),
            ("Taking the best run as the training target",
             "The best run is the most understood words a minute today, often at "
             "the slowest rung. It is the pace to read at when the reading matters. "
             "The hold is the pace to practise at, and the two are often different "
             "rungs."),
            ("Treating the hold as fixed",
             "The hold was found on three standard passages on one day. On easy "
             "text it is higher and on hard text lower, and the Daily Drill moves "
             "it by a twentieth at a time. Find it again when the pool reaches the "
             "hard passages."),
        ],
        "standard": (
            "Finish when you can read a ladder without the lab.",
            "Given three targets and the questions right on each, name the hold "
            "target and the run with the highest effective rate, compute both "
            "effective rates, and explain in a sentence why the two can be "
            "different rungs."
        ),
        "note": (
            "A ladder is three readings of three different passages in a fixed "
            "order, so the fastest rung always comes last, when you are most "
            "practised and perhaps most tired; and one question is ≈ 16.7 points. "
            "The hold it finds is a starting point for practice, not a measurement "
            "of what you can do."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "the-daily-drill",
        "title": "The Daily Drill",
        "module": "The pacer",
        "one_line": "A routine of ten to fifteen minutes a day: one fresh passage behind the pacer at your hold target, and every fifth session a test.",
        "summary": (
            "The Daily Drill is the routine the rest of the Subject keeps going: "
            "one unread passage from the practice pool, read with the pacer at your "
            "hold target and scored, ten to fifteen minutes a day. Every fifth "
            "session is a test at natural pace with no pacer. The target rises by a "
            "twentieth after three holds in a row and falls by a twentieth after "
            "two misses, and the lab reads the next target and the next test from "
            "your log."
        ),
        "key": [
            "one pool passage a day, pacer at the hold",
            "every fifth session: a test, no pacer",
            "three holds in a row: target × 21/20",
            "two misses in a row: target × 19/20",
            "at most two timed readings a sitting",
            "attention gone: shorten, don't slow",
        ],
        "key_label": "The routine in six lines",
        "concepts_intro": (
            "A routine has to be short enough to keep and exact enough to read "
            "back. Three ideas make this one both."
        ),
        "concepts": [
            ("A session is one passage",
             "The pool holds 18 passages, rising from easy to hard, served in order "
             "and never repeated. One passage behind the pacer and its six "
             "questions is a session, and ten to fifteen minutes a day is the "
             "routine."),
            ("The target moves by a twentieth",
             "Three holds in a row at a target, four or more right each time, "
             "raise it by a twentieth: 288 becomes 302.4. Two misses in a row "
             "lower it by a twentieth: 288 becomes 273.6. Anything else keeps it "
             "where it is."),
            ("Tests are the readings that count",
             "Every fifth session is a test: a pool passage at natural pace, with "
             "no pacer. Paced readings are practice. Only tests and baselines go "
             "into the verdicts, because only they measure your own pace."),
        ],
        "read_title": "The routine",
        "read_intro": (
            "The numbers are the Subject's, chosen to be easy to keep; the reasons "
            "for them follow the list."
        ),
        "body": [
            ("p", "Today's session is in the lab below. Type your hold target from "
                  "Choosing a Target Pace into the target box, tick the pacer box, "
                  "and press Start: the lab serves the next pool passage you have not "
                  "read. After Done it asks whether your attention left the text, "
                  "then the six questions."),
            ("ol", [
                "Ten to fifteen minutes a day: one pool passage, read with the "
                "pacer at your hold target, then its questions. At most two timed "
                "readings in a sitting.",
                "Every fifth session, a test: tick the test box and read the next "
                "pool passage at your natural pace, with no pacer. The lab says when "
                "a test is due.",
                "Three holds in a row at a target, four or more right each time, "
                "raise the target by about 5%, a twentieth. Two misses in a row "
                "lower it by the same.",
                "If your attention left the text, make the next session shorter, "
                "not the pacer slower. When the pool reaches the hard passages, find "
                "your hold again; it will be lower.",
            ]),
            ("p", "Each rule is there for a reason you have already met. A "
                  "session is short because a timed reading done while tired or "
                  "interrupted measures the tiredness. The test has no pacer because "
                  "a paced rate is the target's, not yours; only an unpaced reading "
                  "can show whether your own pace has moved, and the rule from One "
                  "Reading Is One Measurement reads the median of the last three "
                  "tests. The target moves by a twentieth so that one good day or one "
                  "bad one cannot move it, and three holds against two misses makes "
                  "it a little harder to go up than to come down."),
            ("p", "The lab reads three figures from your log. The <strong>hold "
                  "target</strong> is the fastest target at which your last three "
                  "paced practice readings at that target all scored four or more; until you have "
                  "three at one target it says &ldquo;not yet&rdquo;. The "
                  "<strong>next target</strong> applies the rule to your last "
                  "readings at your latest target. The <strong>next test</strong> "
                  "counts the practice sessions since your last test; four of them "
                  "make the fifth a test."),
            ("p", "The preset <strong>three-holds</strong> is a reader with three "
                  "paced readings at 288 that scored 5, 4 and 5 of six. All three "
                  "held, so the hold target is 288 and the next target is 288 × "
                  "21/20 = 302.4. They have had three practice sessions since their "
                  "last test, so the test is one session away."),
            ("p", "The preset <strong>two-misses</strong> is a reader whose last two "
                  "paced readings at 288 scored 3 of six each. There is no hold yet "
                  "at 288, and two misses in a row bring the target down to 288 × "
                  "19/20 = 273.6. Two practice sessions since the last test leave "
                  "two more before the next."),
            ("p", "The preset <strong>test-due</strong> is a reader with four paced "
                  "readings at 288 scoring 4, 3, 5 and 4. The last three are not all "
                  "holds and the last two are not both misses, so the target stays at "
                  "288 and there is no hold yet. Four practice sessions since the "
                  "last test make today's session a test: no pacer, natural pace."),
            ("h3", "What the research supports, and what it does not"),
            ("p", "Ericsson, Krampe and Tesch-Römer (1993) gave the name deliberate "
                  "practice to work of this kind: effortful, aimed at the edge of what "
                  "you can do, with immediate feedback. Their study was of musicians, "
                  "and how much of expert performance such practice explains is "
                  "disputed. The routine borrows the shape, not a promise. On reading "
                  "itself, Rayner and colleagues' 2016 review finds that the gains "
                  "from training without loss of comprehension are modest. What the "
                  "routine guarantees is a log in which your tests can show what "
                  "happened, whichever way it goes."),
            ("p", "If the pool runs out, the lab says so; keep going with your own "
                  "text: open &ldquo;Or paste a text of your own&rdquo; above the "
                  "Start button and paste it there. Your own text "
                  "has no questions, so it is logged as practice and its "
                  "comprehension is not scored: it keeps the habit going, and the "
                  "tests keep the measurement going."),
            ("p", "From here on, every lesson in the Subject ends with this session. "
                  "The next lesson, Sprints Above Comfort, tries one of the "
                  "tradition's ways of pushing the pace, and judges it by the same "
                  "rule."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "practice",
            "pool": DAILY_POOL,
            "target": 288,
            "hold": "2/3",
            "preset": "three-holds",
            "presets": [
                {"id": "three-holds", "label": "three-holds: 5, 4 and 5 right at 288",
                 "words": 432, "seconds": 90, "correct": 5, "total": 6, "target": 288,
                 "pacerLog": [(288, 5, 6), (288, 4, 6), (288, 5, 6)], "sinceTest": 3,
                 "expect": {"drHold": "288 wpm", "drNextTarget": "302.4 wpm", "drTestDue": "after 1 more practice session"}},
                {"id": "two-misses", "label": "two-misses: 3 and 3 right at 288",
                 "words": 432, "seconds": 90, "correct": 3, "total": 6, "target": 288,
                 "pacerLog": [(288, 3, 6), (288, 3, 6)], "sinceTest": 2,
                 "expect": {"drHold": "not yet", "drNextTarget": "273.6 wpm", "drTestDue": "after 2 more practice sessions"}},
                {"id": "test-due", "label": "test-due: four sessions since the last test",
                 "words": 432, "seconds": 90, "correct": 4, "total": 6, "target": 288,
                 "pacerLog": [(288, 4, 6), (288, 3, 6), (288, 5, 6), (288, 4, 6)], "sinceTest": 4,
                 "expect": {"drHold": "not yet", "drNextTarget": "288 wpm", "drTestDue": "due now: make the next reading a test"}},
            ],
            "panel_title": "Today's session, in numbers",
            "panel_intro": (
                "Your measurement: type your hold target into the target box, tick "
                "the pacer box (or the test box, when a test is due) and press "
                "Start. When you press Score, the boxes fill with what you did and "
                "the pacer log and sessions since your last test are read from your "
                "log; until then they hold a worked example. " + ONE_Q
            ),
        }),
        "steps_title": "Each day's session",
        "steps_intro": (
            "Ten to fifteen minutes, in this order. The lab keeps the count; you "
            "keep the habit."
        ),
        "steps": [
            ("Open this page and read the two tiles",
             "The next pacer target and the next test come from your log. If a test "
             "is due, tick the test box and leave the pacer off."),
            ("Type the target and start",
             "Type the next target into the target box, tick the pacer box, and "
             "press Start. Keep your eyes on the lit line until it ends."),
            ("Tick the attention box honestly, then answer",
             "If your attention left the text, say so. It goes into your log, and "
             "it means tomorrow's session should be shorter, not the pacer slower."),
            ("Stop after two timed readings",
             "One passage is a session. If you have time for a second, read it; "
             "after two, stop. A third measures your tiredness."),
            ("Then today's Daily Drill, every day",
             "Come back to this lesson, The Daily Drill, tomorrow, and on every "
             "day you can. Every later lesson ends by sending you here."),
        ],
        "worked": {
            "title": "Three holds, then a raise",
            "intro": [
                "The three-holds preset: three paced readings at 288, with 5, 4 and 5 "
                "questions right of six.",
            ],
            "lines": [
                "5/6, 4/6, 5/6: each at least 4/6, three holds",
                "next target = 288 × 21/20 = 302.4",
                "two misses instead: 288 × 19/20 = 273.6",
            ],
            "after": [
                "Three more holds at 302.4 would raise it to 302.4 × 21/20 = 317.52. A "
                "twentieth at a time, the target moves slowly, which is the point: one "
                "day's reading cannot move it far.",
            ],
        },
        "quiz_title": "Applying the routine",
        "quiz": [
            {"q": "A reader's last three paced readings at 300 scored 4, 5 and 4 of "
                  "six. What is their next target?",
             "a": ["300", "285", "330", "315"],
             "c": 3,
             "why": "Three holds in a row at 300 raise it by a twentieth: 300 × 21/20 "
                    "= 315."},
            {"q": "Their last two paced readings at 260 scored 3 of six each. What is "
                  "the next target?",
             "a": ["247", "260", "273", "234"],
             "c": 0,
             "why": "Two misses in a row lower the target by a twentieth: 260 × 19/20 "
                    "= 247."},
            {"q": "A reader has done four practice sessions since their last test. "
                  "What should today's session be?",
             "a": ["Another paced session at the hold target",
                   "A test: the next pool passage at natural pace, with no pacer",
                   "A ladder, to find the hold again",
                   "A reread of the last passage, to check the score"],
             "c": 1,
             "why": "Every fifth session is a test, read at natural pace with no "
                    "pacer, because only an unpaced reading measures the reader's own "
                    "pace."},
            {"q": "Halfway through a session a reader notices their attention has "
                  "drifted off the text. What does the routine say?",
             "a": ["Lower the pacer target by a twentieth for the next session",
                   "Read the passage again from the start",
                   "Make the next session shorter, and keep the target",
                   "Add a third reading to make up for it"],
             "c": 2,
             "why": "A lapse of attention is a reason to shorten the session, not to "
                    "slow the pacer; the target moves only by holds and misses."},
        ],
        "mistakes": [
            ("Reading as much as possible, as fast as possible",
             "More is not better when the reading is past the point where you "
             "understand it or after your attention has gone. Short, regular "
             "sessions at a pace you still understand, with regular tests, are the "
             "routine; a session's length is set by your attention, not by "
             "ambition."),
            ("Counting paced readings as progress",
             "A paced rate is the target's. It goes up when you raise the target, "
             "whether or not your own pace has moved. Only the tests, read without "
             "the pacer, can show that, and only the median of the last three can "
             "show it reliably."),
            ("Raising the target after one good day",
             "One reading with six right is one reading. The target rises after "
             "three holds in a row, so that the pace moves up only when it has "
             "been held more than once."),
        ],
        "standard": (
            "Finish when you can run the routine from your log alone.",
            "State the routine's four rules, and given a log excerpt of targets and "
            "scores since the last test, say what the next target is and whether "
            "today is a test, with the arithmetic."
        ),
        "note": (
            "The routine is the Subject's, not a finding: the twentieth, the three "
            "and the two, and the test every fifth session were chosen to be easy "
            "to keep and hard to fool. What it measures is your log over weeks, on "
            "passages written for this course, in a browser; whether it changes "
            "your reading elsewhere is something the tests can suggest and only you "
            "can check."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "sprints-above-comfort",
        "title": "Sprints Above Comfort",
        "module": "Pushing the pace",
        "one_line": "A minute behind the pacer at twice your rate, then a natural-pace test, judged against your baseline range.",
        "summary": (
            "A sprint is a short reading behind the pacer at about twice your "
            "baseline rate, with no questions: the tradition's way of making your "
            "ordinary pace feel slow. This lesson's drill runs a sprint and then a "
            "natural-pace test on a new passage, and the lab judges the test "
            "against your baseline range by the Subject's rule."
        ),
        "key": [
            "sprint: pacer at baseline × 2, no questions",
            "then: a test at natural pace, scored",
            "one reading above the range: one in four",
            "evidence: median of three tests above",
        ],
        "key_label": "The sprint in four lines",
        "concepts_intro": (
            "A sprint is a treatment and the reading after it is the measurement. "
            "Three ideas keep the two apart."
        ),
        "concepts": [
            ("The sprint is not a reading",
             "At twice your rate you will not take in every word, and the sprint "
             "has no questions. Its rate is the pacer's; the lab does not score it "
             "and nothing it shows is a measurement of you."),
            ("The test after it is",
             "The natural-pace reading that follows, with six questions, is "
             "logged as a test. Its rate is yours, and the question is whether it "
             "is above your baseline range."),
            ("Once is not a change",
             "A reading above the baseline range happens by chance about one time "
             "in four. A change is evidence when the median of the last three tests "
             "is above the range, which no single sprint can show."),
        ],
        "read_title": "What a sprint can and cannot show",
        "read_intro": (
            "The drill's order is fixed: the sprint first, because it is the "
            "treatment, then the test."
        ),
        "body": [
            ("p", "The drill below runs in a fixed order. First the sprint: type "
                  "twice your baseline rate into the target box (480 from a baseline "
                  "of 240), press Start, and keep up with the highlight for the whole "
                  "passage, about a minute, taking in what you can. There are no "
                  "questions. Then, straight after, the test: a new passage at your "
                  "natural pace, with six questions."),
            ("p", "The tradition's claim for the sprint is that it resets what "
                  "feels normal: after a minute at a pace you cannot follow, your "
                  "ordinary pace feels slow, and you read faster without trying. If you "
                  "felt it, the drill takes the feeling seriously enough to measure "
                  "it. The feeling is one thing; the rate and the "
                  "score of the test after it are another."),
            ("p", "Before you read the verdict, press &ldquo;Use my baseline "
                  "range&rdquo; under the drill, so that the lab compares your test "
                  "with the range of your own baseline rates rather than the worked "
                  "example's. The verdict reads your test's rate, not its effective "
                  "rate, because the range is made of rates."),
            ("p", "The preset <strong>after-sprint</strong> is a reader with a "
                  "baseline range of 238 to 251. After the sprint, their test reads "
                  "at 268 words a minute with 5 of 6 right, an effective rate of 268 "
                  "× 5/6 ≈ 223.3. 268 is 268 − 251 = 17 above the top of the range: "
                  "the lab says &ldquo;above the baseline range once &mdash; a fourth "
                  "reading does this about one time in four&rdquo;."),
            ("p", "That verdict is exactly as strong as it sounds. With nothing "
                  "changed at all, a fourth reading is the highest of four about one "
                  "time in four, so a single test above a range of three baselines is "
                  "what chance alone produces often. It is worth writing down, and it "
                  "is not yet a change."),
            ("p", "The preset <strong>no-effect</strong> is the same reader on "
                  "another day: a test at 247 words a minute with 5 of 6 right, "
                  "effective ≈ 205.8, inside the range. The sprint felt the same, and "
                  "the test shows nothing a reading without one would not have "
                  "shown."),
            ("h3", "What would make it evidence"),
            ("p", "To find out whether sprints move your pace, you need tests after "
                  "sprints across several days, and then the median of the last three "
                  "of them above your baseline range. Even then you would want to "
                  "know whether the sprint did it or the reading practice around it "
                  "did, and that takes tests without sprints as well, for comparison. "
                  "The Daily Drill's tests are the readings that build that record."),
            ("p", "Whatever your test showed today, it is one reading. If yours was "
                  "inside your range, you have not refuted the readers who say a "
                  "sprint helps them, and they have not refuted you; if yours was "
                  "above, the same holds the other way."),
            ("p", "Then today's Daily Drill. The next lesson, Repeated Reading and "
                  "Transfer, asks a sharper question about a gain: whether it belongs "
                  "to you or to the passage."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P17"], PASSAGES["P18"]],
            "a": {"label": "The sprint", "display": "pacer", "target": 480, "questions": False,
                  "kind": "condition"},
            "b": {"label": "The test after it", "kind": "test"},
            "lineWords": 12,
            "ratioOf": "wpm",
            "order": "AB",
            "preset": "after-sprint",
            "presets": [
                {"id": "after-sprint", "label": "after-sprint: a test at 268",
                 "wordsA": 484, "secondsA": "60.5", "targetA": 480,
                 "wordsB": 469, "secondsB": 105, "correctB": 5, "totalB": 6,
                 "baseLo": 238, "baseHi": 251,
                 "expect": {"drWpmB": "268 wpm", "drErrB": "≈ 223.3 wpm", "drVerdictB": "above the baseline range once — a fourth reading does this about one time in four"}},
                {"id": "no-effect", "label": "no-effect: a test at 247",
                 "wordsA": 484, "secondsA": "60.5", "targetA": 480,
                 "wordsB": 494, "secondsB": 120, "correctB": 5, "totalB": 6,
                 "baseLo": 238, "baseHi": 251,
                 "expect": {"drWpmB": "247 wpm", "drErrB": "≈ 205.8 wpm", "drVerdictB": "inside the baseline range"}},
            ],
            "panel_title": "The sprint and the test, in numbers",
            "panel_intro": (
                "Your measurement: type twice your baseline rate into the sprint's "
                "target box, run the sprint, then the test, and press Use my "
                "baseline range before you read the verdict. The sprint has no "
                "questions, so only the test has an effective rate; the verdict "
                "compares the test's rate with your baseline range. The B / A tile "
                "compares the test with the sprint's pace and means nothing here. " + ONE_Q
            ),
        }),
        "steps_title": "Trying a sprint on another day",
        "steps_intro": (
            "If you want to test sprints properly, do this on several days, and "
            "keep some tests without a sprint to compare."
        ),
        "steps": [
            ("Sprint for about a minute",
             "Set the pacer at twice your baseline rate on a passage you will not be "
             "tested on, and keep up with the highlight to the end."),
            ("Read the next passage at your natural pace",
             "Straight after, with no break, read a fresh passage without the "
             "pacer and answer its questions. Log it as a test."),
            ("Judge it by the rule",
             "Compare the test's rate with your baseline range. Once above is "
             "worth noting; the median of three tests above is evidence."),
            ("Keep a comparison",
             "On other days, take tests without a sprint before them. Only the two "
             "kinds of test side by side can say whether the sprint is what moved "
             "anything."),
            ("Then today's Daily Drill",
             "Open The Daily Drill and run today's session. Count the sprint and its "
             "test as your two timed readings if you did them today."),
        ],
        "worked": {
            "title": "The after-sprint test against the range",
            "intro": [
                "Baselines from 238 to 251 words a minute; a test after a sprint at 268, "
                "with 5 of 6 right.",
            ],
            "lines": [
                "268 − 251 = 17 above the top of the range",
                "verdict: above the range once",
                "effective rate: 268 × 5/6 ≈ 223.3",
            ],
            "after": [
                "Once above the range is what a fourth reading does about one time in "
                "four. Three tests whose median is above 251 would be evidence; this "
                "one is a reading to log.",
            ],
        },
        "quiz_title": "Judging the reading after a sprint",
        "quiz": [
            {"q": "A reader's baseline range is 220 to 236. After a sprint, their test "
                  "reads at 241. What is the verdict?",
             "a": ["Above the range once", "Inside the range",
                   "Above the range on the median of three tests",
                   "Below the range"],
             "c": 0,
             "why": "241 is 5 above the top, 236. One reading above the range happens "
                    "by chance about one time in four, so it is above once, not yet "
                    "a change."},
            {"q": "What would make sprints evidence of a change in that reader's pace?",
             "a": ["One more test above the range",
                   "A sprint at a higher target",
                   "The median of their last three tests above the range",
                   "A test that feels faster than before"],
             "c": 2,
             "why": "By the Subject's rule, a change is evidence when the median of "
                    "the last three tests is above the baseline range."},
            {"q": "Why does the sprint have no questions?",
             "a": ["Because questions would slow the pacer down",
                   "Because the sprint is the treatment, not a measurement of the reader",
                   "Because comprehension does not matter at high speed",
                   "Because the passage is too short for six questions"],
             "c": 1,
             "why": "At twice the reader's rate the sprint's rate is the pacer's, and "
                    "the reading that measures the reader is the test after it."},
        ],
        "mistakes": [
            ("Believing that after a sprint you read faster for good",
             "Any after-effect shows up in one reading, and one reading above the "
             "range happens by chance about one time in four. Only the median of "
             "later tests can say whether your base rate moved, and only tests "
             "without sprints beside them can say the sprint did it."),
            ("Taking the felt speed for the measured one",
             "After a sprint your natural pace feels slow, which is the point of it, "
             "but the feeling is not the rate. The test's words and seconds are, and "
             "they often say less than the feeling does."),
            ("Reading the sprint's rate as your own",
             "The sprint's rate is the target you typed. It has no questions and "
             "no effective rate, and it says nothing about how fast you read; it "
             "is logged as a condition, not a test."),
        ],
        "standard": (
            "Finish when you can judge a reading after a sprint without the lab.",
            "Given a baseline range and the rate of a reading after a sprint, give "
            "the verdict by the Subject's rule, with the arithmetic, and say what "
            "further readings would be needed to call it a change."
        ),
        "note": (
            "The comparison is between two different passages, and the order is "
            "fixed: the test always follows a sprint, so whatever the sprint does "
            "and whatever a minute's warm-up of any reading does are not separated "
            "here. Tests on other days without a sprint are the comparison this "
            "drill cannot give in one sitting."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "repeated-reading-and-transfer",
        "title": "Repeated Reading and Transfer",
        "module": "Pushing the pace",
        "one_line": "Read one passage three times and a new one once, and see which gain belongs to the passage and which to you.",
        "summary": (
            "Read a passage three times, then a matched passage you have never "
            "seen. The rate on the repeated passage rises because you know it; the "
            "rate on the new one is the only one that measures you. The lab "
            "computes both gains against the first reading."
        ),
        "key": [
            "repeat gain = reading 3 − reading 1",
            "transfer gain = new passage − reading 1",
            "the repeat gain measures the passage",
            "the transfer gain measures the reader",
        ],
        "key_label": "Two gains in four lines",
        "concepts_intro": (
            "Two gains, one of them easy to mistake for the other."
        ),
        "concepts": [
            ("The repeat gain",
             "The third reading of a passage minus the first. It is large for "
             "almost everyone, because by the third time you know the words, the "
             "order of the ideas and where the passage is going."),
            ("The transfer gain",
             "The rate on a new, matched passage minus the first reading of the "
             "repeated one. It is the part of any gain that went with you to a "
             "text you had not seen."),
            ("A method from another field",
             "Repeated reading is a fluency method from work with school-age "
             "readers. It is here because its evidence asks the right question: "
             "whether practice on one text helps on the next."),
        ],
        "read_title": "Whose gain is it?",
        "read_intro": (
            "Four readings, two of them scored. The lab compares the third and the "
            "fourth with the first."
        ),
        "body": [
            ("p", "The drill below asks for four readings. Read the first passage "
                  "three times at your natural pace, pressing Start for each; the "
                  "third reading has six questions. Then read the new passage once, "
                  "with its six questions. Do all four in one sitting, with a short "
                  "pause between: this drill is the one exception to the Daily "
                  "Drill's limit of two timed readings a sitting."),
            ("p", "S. Jay Samuels described the method of repeated readings in "
                  "1979, for children learning to read fluently: read a short "
                  "passage again and again until it goes smoothly, then move to the "
                  "next. Therrien's 2004 meta-analysis of studies with school-age "
                  "students, with and without learning disabilities, found that it "
                  "improved their reading of the practised passages and also of new "
                  "ones, though less on the new ones."),
            ("p", "For a skilled adult reader that finding is a question, not an "
                  "answer: the studies were not of readers like you. This drill's "
                  "new-passage reading is the test. The gain on the repeated passage "
                  "will almost certainly be large, and it is a gain in knowing that "
                  "passage."),
            ("p", "The preset <strong>practice-effect</strong> is a reader whose "
                  "three readings of the repeated passage ran at 240, 300 and 340 "
                  "words a minute, and whose new passage ran at 248. The repeat gain "
                  "is 340 − 240 = +100 words a minute; the transfer gain is 248 − 240 "
                  "= +8. A hundred words a minute came from knowing the text; eight "
                  "went with the reader to a new one, and eight is well inside the "
                  "difference two passages make on their own."),
            ("p", "The preset <strong>transfer</strong> keeps the three readings "
                  "and puts the new passage at 275: a transfer gain of 275 − 240 = "
                  "+35. That is a bigger number, and still one reading of one new "
                  "passage, compared with the first reading of a different one. "
                  "Measured against this reader's baseline range, it would be at "
                  "best above the range once."),
            ("p", "The first reading is the baseline the two gains share, and it is "
                  "itself one reading of one passage. A slow first reading inflates "
                  "both gains; a fast one shrinks both. That is a reason to compare "
                  "the new passage with your baseline range as well as with reading "
                  "one, which the tile does not do and your log can."),
            ("h3", "Why the method can still be useful"),
            ("p", "None of this makes repeated reading worthless. Reading a passage "
                  "you need to know well several times does help you know it, and "
                  "for school-age readers the gains reached new passages too. What "
                  "the drill rules out is reading the third reading's rate as a new "
                  "speed. If your new passage gained nothing, you have not refuted "
                  "Therrien, whose readers were children, and the meta-analysis has "
                  "not refuted you."),
            ("p", "One limit of the lab: every reading in this drill is logged as a "
                  "condition, so even the new passage does not enter the verdicts. "
                  "The Daily Drill's tests are the readings that do."),
            ("p", "Then today's Daily Drill. The next course, How the Eyes Read, "
                  "computes the limits every technique here is read against: what a "
                  "stop of the eyes costs, and how far one glance can reach."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "repeat",
            "passages": [PASSAGES["P23"], PASSAGES["P24"]],
            "questions": [False, False, True, True],
            "kind": "condition",
            "preset": "practice-effect",
            "presets": [
                {"id": "practice-effect", "label": "practice-effect: new passage at 248",
                 "words1": 442, "seconds1": "110.5",
                 "words2": 442, "seconds2": "88.4",
                 "words3": 442, "seconds3": 78, "correct3": 6, "total3": 6,
                 "words4": 465, "seconds4": "112.5", "correct4": 5, "total4": 6,
                 "expect": {"drWpm4": "248 wpm", "drRepeatGain": "+100 wpm", "drTransferGain": "+8 wpm"}},
                {"id": "transfer", "label": "transfer: new passage at 275",
                 "words1": 442, "seconds1": "110.5",
                 "words2": 442, "seconds2": "88.4",
                 "words3": 442, "seconds3": 78, "correct3": 6, "total3": 6,
                 "words4": 451, "seconds4": "98.4", "correct4": 5, "total4": 6,
                 "expect": {"drWpm4": "275 wpm", "drRepeatGain": "+100 wpm", "drTransferGain": "+35 wpm"}},
            ],
            "panel_title": "Four readings, in numbers",
            "panel_intro": (
                "Your measurement: read the first passage three times, then the new "
                "one, pressing Start, Done and Score for each. Each reading fills its "
                "own boxes; until then they hold a worked example. Only readings 3 "
                "and 4 have questions. " + ONE_Q
            ),
        }),
        "steps_title": "Testing transfer on another day",
        "steps_intro": (
            "The same question on your own texts: does practice on one help on the "
            "next?"
        ),
        "steps": [
            ("Choose two matched texts",
             "Two passages of about the same length, kind and difficulty, neither "
             "of which you have read."),
            ("Read the first three times",
             "Time each reading at your natural pace. Answer questions, or write a "
             "two-sentence summary, after the third."),
            ("Read the second once",
             "Time it at your natural pace and check your understanding the same "
             "way."),
            ("Compute both gains, and judge the second",
             "Subtract reading one from reading three, and from the new reading. "
             "Judge the new reading against your baseline range, by the Subject's "
             "rule."),
            ("Then today's Daily Drill",
             "Open The Daily Drill for today's session. Four readings are more "
             "than a sitting should hold, so if this drill was today's sitting, the "
             "session waits until tomorrow."),
        ],
        "worked": {
            "title": "The practice-effect preset",
            "intro": [
                "Three readings of one passage, then a new one.",
            ],
            "lines": [
                "readings 1, 2, 3: 240, 300, 340",
                "new passage: 248",
                "repeat gain = 340 − 240 = +100",
                "transfer gain = 248 − 240 = +8",
            ],
            "after": [
                "The hundred belongs to the passage. The eight is the only part that "
                "could belong to the reader, and one question or one passage can "
                "make more difference than that.",
            ],
        },
        "quiz_title": "Repeat and transfer",
        "quiz": [
            {"q": "Readings of one passage at 220, 270 and 310, then a new passage at "
                  "232. What are the repeat and transfer gains?",
             "a": ["+90 and +12", "+50 and +12", "+90 and −78", "+40 and +22"],
             "c": 0,
             "why": "Repeat gain: 310 − 220 = +90. Transfer gain: 232 − 220 = +12."},
            {"q": "Which of the two gains measures a change in the reader?",
             "a": ["The repeat gain, because it is larger",
                   "Both equally",
                   "The transfer gain, because the new passage was not practised",
                   "Neither, because the first reading is unreliable"],
             "c": 2,
             "why": "The repeated passage is known by the third reading, so its gain "
                    "is in the text. Only the new passage's gain could be a change in "
                    "the reader, and it is still one reading."},
            {"q": "What did Therrien's 2004 meta-analysis find, as this lesson states "
                  "it?",
             "a": ["Repeated reading raised adult readers' speed on new texts",
                   "With school-age readers, gains on new passages too, smaller than on practised ones",
                   "Repeated reading helped only on the practised passages",
                   "Repeated reading helped only readers with learning disabilities"],
             "c": 1,
             "why": "The studies were of school-age students, with and without "
                    "learning disabilities; the gains reached new passages, less than "
                    "the practised ones. Adults were not the population."},
        ],
        "mistakes": [
            ("Believing the third reading shows your new speed",
             "It shows that you know the passage. By the third reading the words, "
             "the order of the ideas and the ending are familiar, and the rate "
             "rises for that reason. Repeated reading is a fluency method from work "
             "with school-age readers, where it also improved new passages, less "
             "than the practised one (Therrien 2004); for a skilled adult, this "
             "drill's new-passage reading is the test."),
            ("Measuring the transfer gain against a slow first reading",
             "Both gains are measured from reading one. If that reading was slow "
             "for reasons of its own, both gains look larger. Check the new "
             "passage's rate against your baseline range too."),
            ("Taking a school-age finding as an adult one",
             "Therrien's meta-analysis was of school-age students. That it found "
             "transfer there is a reason to test it on yourself, not a result about "
             "you."),
        ],
        "standard": (
            "Finish when you can tell the two gains apart without the lab.",
            "Given four rates, three on one passage and one on a new passage, "
            "compute the repeat gain and the transfer gain, name the one that "
            "measures the reader, and say what else you would need to call it a "
            "change."
        ),
        "note": (
            "The two passages are matched, not identical, and the new one always "
            "comes last, after three readings' practice and some tiredness: the "
            "two confounds of any two-reading comparison, here in a fixed order. "
            "The transfer gain is one reading against one other reading, which is "
            "why it is read against your baseline range as well."
        ),
    },
]
