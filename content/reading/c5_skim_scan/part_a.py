"""Course 5, lessons 1-4 -- scanning, skimming and previewing (module "Scanning and skimming")."""

from reading.passages import PASSAGES

MODULE = "Scanning and skimming"

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "scanning-for-a-target",
        "title": "Scanning for a Target",
        "module": MODULE,
        "one_line": "Find five named things in a ferry timetable against the clock, and work out what the search cost per target.",
        "summary": (
            "Scanning is a search for something whose form you already know: a time, a "
            "price, a name. Time yourself finding five targets in a 613-word timetable, "
            "then compute the seconds per target found and the words passed over per "
            "second, and see why neither figure is a reading rate."
        ),
        "key": [
            "per target = seconds / targets found",
            "passed over = words / seconds",
            "scanning: a search for a known form",
            "its speed is not a reading rate",
        ],
        "key_label": "Scanning in four lines",
        "concepts_intro": (
            "You already scan every day, in a timetable, a menu, a contract. The drill "
            "times it, so that you can see what kind of speed it is."
        ),
        "concepts": [
            ("A known form",
             "You scan when you know what the answer will look like before you see it: "
             "a time with a colon in it, a price after a pound sign, a name with a "
             "capital. The eye matches shapes, and it can pass over everything that "
             "does not have that shape."),
            ("Two figures, two questions",
             "Seconds per target found says what each answer cost you. Words passed "
             "over per second says how much text went by while you looked. Neither "
             "says how much of the text you understood, because you were not trying "
             "to understand it."),
            ("Layout does half the work",
             "A timetable with a heading for each route and the times in a row is "
             "built to be scanned. The same facts buried in prose take longer to find, "
             "and the headings are the first thing a good scan uses."),
        ],
        "read_title": "What a scan measures",
        "read_intro": (
            "The drill comes first in the lab below; this is what its two figures "
            "mean, and what they do not."
        ),
        "body": [
            ("p", "The drill is the summer timetable of a ferry company: 613 words of "
                  "sailing times, fares, check-in rules and exceptions, with prose "
                  "between the tables. Press Start and a prompt asks for one thing, such "
                  "as the first Sunday sailing. Click the word that answers it, or Tab "
                  "to it and press Enter; a wrong click is counted and you keep looking. "
                  "If you cannot find a target, press Skip this one. Five prompts, one "
                  "clock, and the result is logged as a scan, not as a reading. On a "
                  "phone, scrolling the page is part of the search, and the clock "
                  "includes it."),
            ("p", "When the fifth prompt is answered or skipped, the panel fills with two "
                  "figures. Seconds per target found is the time divided by the targets "
                  "you found, not by the targets you were asked for: the time you spent "
                  "hunting for a target you never found was still spent, and it belongs "
                  "to the answers you did get. Words passed over per second is the "
                  "length of the text divided by the time."),
            ("math", [
                "seconds per target  = 40 / 5 = 8 s",
                "words passed over   = 613 / 40 ≈ 15.3 a second",
                "in a minute         = 613 × 60 / 40 = 919.5 words",
            ]),
            ("p", "Those are the figures of the <strong>quick</strong> preset, a reader "
                  "who found all five in 40 seconds: 8 seconds a target, and about 15.3 "
                  "words a second passed over, which is 919.5 words a minute. The "
                  "<strong>slow</strong> preset found four in 95 seconds, with one wrong "
                  "click and one target skipped: 95 / 4 = 23.75 seconds per target "
                  "found, and about 6.5 words a second."),
            ("p", "Nine hundred and twenty words a minute is nearly four times "
                  "Brysbaert's (2019) estimate of 238 words a minute for silent reading "
                  "of non-fiction, and it is not a reading rate at all. Nobody who "
                  "scanned that timetable for five targets could tell you what the other "
                  "six hundred words said. Carver (1990) counted scanning as the fastest "
                  "of five gears, at about 600 standard-length words a minute for the "
                  "college students he tested, against about 300 for ordinary reading; "
                  "what sets it apart is its goal, finding a target rather than "
                  "understanding the passage. A scan can go that fast because it is not "
                  "reading for meaning."),
            ("p", "What makes one search faster than another is mostly where you look. "
                  "Read the headings first and decide which section a target lives in. "
                  "Hold the form of the answer in mind, a colon for a time and a pound "
                  "sign for a fare, and let the eyes jump from block to block instead of "
                  "travelling along the lines. When a target sits inside a paragraph, as "
                  "the vessel out of service for inspection does, look for its shape "
                  "first and read only the sentence around it."),
            ("p", "The figures belong to this text and these five targets. A search of a "
                  "page you have just searched is quicker because you remember where "
                  "things are, so only your first run is a measurement of scanning; a "
                  "second run on the same timetable measures your memory of it. Compare "
                  "a scan with a scan of a similar document, never with a reading."),
            ("p", "Scanning finds a thing you can name. When you cannot name it, when you "
                  "want to know what a text is about, you skim, and Skimming for Gist "
                  "times that next."),
        ],
        "lab": ("readkit", {
            "mode": "scan",
            "view": "find",
            "passage": PASSAGES["S01"],
            "preset": "quick",
            "presets": [
                {"id": "quick", "label": "Five found in 40 seconds",
                 "found": 5, "wrong": 0, "seconds": 40,
                 "expect": {"scFound": "5 of 5", "scPerTarget": "8 s",
                            "scWordsPerSec": "≈ 15.3 words a second"}},
                {"id": "slow", "label": "Four found in 95 seconds, one wrong click",
                 "found": 4, "wrong": 1, "seconds": 95,
                 "expect": {"scFound": "4 of 5", "scPerTarget": "23.75 s",
                            "scWordsPerSec": "≈ 6.5 words a second", "scWrong": "1"}},
            ],
            "panel_intro": (
                "Your measurement: the boxes fill when the search ends; before that they "
                "hold a worked example. On a phone, scrolling the page is part of the "
                "search, and the clock includes it."
            ),
        }),
        "steps_title": "Timing a scan of your own",
        "steps_intro": "Five steps, on a document you need something from.",
        "steps": [
            ("Name five targets first",
             "On a document of your own, such as a timetable, a manual or a contract, "
             "write down five things to find, and next to each the form its answer "
             "will take: a time, a sum, a name, a date."),
            ("Survey the layout",
             "Before the clock starts, look at the headings only and guess which "
             "section holds each target."),
            ("Time the search",
             "Start a clock, find all five, and stop it. A target you gave up on counts "
             "as not found, and its time stays in."),
            ("Compute both figures",
             "Seconds over targets found; words in the document over seconds. Compare "
             "them with your last scan of a similar document, not with a reading."),
            ("Then today's Daily Drill",
             "Scanning is not on the practice pool. Do today's reading from The Daily "
             "Drill, at your hold target, as usual."),
        ],
        "worked": {
            "title": "The quick preset, by hand",
            "intro": [
                "A reader found all five targets in the 613-word timetable in 40 seconds, "
                "with no wrong clicks.",
            ],
            "lines": [
                "targets found        5 of 5",
                "per target found     40 / 5 = 8 s",
                "passed over          613 / 40 ≈ 15.3 words a second",
                "in a minute          613 × 60 / 40 = 919.5 words",
            ],
            "after": [
                "Over nine hundred words a minute went past the reader's eyes, and they "
                "took in five times and prices from them, because nothing else was "
                "asked. That is what the figure measures: the speed of a search.",
            ],
        },
        "quiz_title": "Check the search",
        "quiz": [
            {"q": "A reader finds 3 of 5 targets in a 600-word notice in 60 seconds and "
                  "skips the other two. What is the time per target found?",
             "a": ["12 s", "20 s", "10 s", "30 s"], "c": 1,
             "why": "60 / 3 = 20 seconds per target found. 12 s divides by the five "
                    "targets asked, which hides what the two misses cost; 10 is the "
                    "words passed over per second, 600 / 60."},
            {"q": "A scan passes over 900 words a minute. What does that say about the "
                  "reader's reading rate?",
             "a": ["Nothing: a scan does not try to understand the text it passes over",
                   "Their reading rate is about 900 words a minute",
                   "Their reading rate is at least 600 words a minute, Carver's scanning gear",
                   "Their reading rate is about a third of it, 300 words a minute"],
             "c": 0,
             "why": "A scan is a search for a known form. Its speed comes from not "
                    "reading the words between targets, so it says nothing about how "
                    "fast the same reader reads for meaning."},
            {"q": "Which of these is a scan suited to?",
             "a": ["Finding the time of the last Saturday sailing",
                   "Judging whether the ferry company is well run",
                   "Saying what the timetable's exceptions have in common",
                   "Deciding which route a visitor would enjoy most"],
             "c": 0,
             "why": "A scan needs a target whose form you know in advance, and a "
                    "departure time has one. The others need the text read and "
                    "thought about."},
            {"q": "Why does only your first search of the timetable count as a "
                  "measurement of scanning?",
             "a": ["On a second search you remember where things are, so it measures memory too",
                   "The clock runs more slowly on a second visit",
                   "The kit chooses different targets on a second visit",
                   "A second search is always slower because of fatigue"],
             "c": 0,
             "why": "The targets and the text are the same on a second run, and knowing "
                    "where the fares are is memory, not search."},
        ],
        "mistakes": [
            ("Taking scanning for fast reading",
             "In the quick preset 919.5 words a minute went past, and nothing in them "
             "was understood except five times and prices. Scanning is a search for a "
             "known form, a number or a name, and not reading for meaning; Carver "
             "(1990) counted it a gear of its own, whose goal is finding rather than "
             "understanding. Its speed says nothing about how fast you read."),
            ("Dividing by the targets asked",
             "Seconds per target is the time over the targets found. In the slow "
             "preset, 95 / 5 = 19 seconds would understate what each answer cost; "
             "95 / 4 = 23.75 seconds is the true figure, because the hunt for the "
             "missing target was part of the time."),
            ("Reading line by line to find a target in prose",
             "When a target sits inside a paragraph, it is tempting to start reading "
             "every line. The form of the answer is still the guide: look for its "
             "shape, then read only the sentence that holds it."),
        ],
        "standard": (
            "Finish when you can price a search from its time and count.",
            "Given the targets found, the targets asked, the words in the text and the "
            "seconds taken, compute the seconds per target found and the words passed "
            "over per second, and say in a sentence why neither is a reading rate. All "
            "three, without the lab.",
        ),
        "note": (
            "One timetable, five targets, one sitting: a scan's figures depend heavily "
            "on the layout and on how well the targets match the headings, so compare a "
            "scan only with a scan of a similar document. A second search of the same "
            "page measures your memory of it."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "skimming-for-gist",
        "title": "Skimming for Gist",
        "module": MODULE,
        "one_line": "Skim a passage by its headings and first sentences under a time limit, then work out how much of it you saw and how many gist questions you got right a minute.",
        "summary": (
            "How much of a passage does a skim show you, and how much of its point does "
            "that carry? Skim a passage on glaciers by its headings and first sentences "
            "for 40 seconds, answer four questions about its gist, and compute the share "
            "of its words you saw and the gist questions right per minute."
        ),
        "key": [
            "shown = words shown / words in all",
            "gist rate = gist right × 60 / seconds",
            "the skim: headings, first sentences",
            "no effective rate for a skim",
            "a skim is a bet on the structure",
        ],
        "key_label": "A skim in five lines",
        "concepts_intro": (
            "The question is how much of a text's point you can get from a small, "
            "chosen part of it. The method is to show only that part, for a fixed time, "
            "and ask about the point."
        ),
        "concepts": [
            ("What the skim shows",
             "The drill shows every heading and the first sentence of every paragraph, "
             "and nothing else, and takes them away when the limit runs out. The share "
             "it shows is the words in those sentences over the words in the passage, "
             "counted by the kit's rule."),
            ("Gist questions only",
             "The questions after a skim ask what the passage is about and what its "
             "sections say, never a figure or a name from the middle of a paragraph, "
             "because the skim never showed you one."),
            ("Gist answers per minute",
             "A skim is scored as gist questions right, times sixty, over the seconds. "
             "It is not an effective reading rate: the words you never saw were not "
             "read, and dividing the passage's length by the time would credit you "
             "with them."),
        ],
        "read_title": "What a quarter of a passage carries",
        "read_intro": (
            "Do the drill first: the explanation below starts from your score."
        ),
        "body": [
            ("p", "Do the drill before you read on. Press Start below: for 40 seconds you "
                  "see only the headings and the first sentence of each paragraph of a "
                  "passage about glaciers, then four questions about its gist. Take in "
                  "what you are shown as quickly as you like; the display ends by "
                  "itself, and the result is logged as a condition, not a test."),
            ("p", "Look at your score before anything else, because whatever it was, it "
                  "came from under a quarter of the text. The skim showed 141 of the "
                  "passage's 594 words; the rest was never on the screen. A reader who "
                  "got three of the four right has a gist rate of 3 × 60 / 40 = 4.5 gist "
                  "answers a minute, and that is the <strong>first-sentences</strong> "
                  "preset."),
            ("math", [
                "shown       141 / 594 = 47/198 ≈ 23.7%",
                "gist rate   3 × 60 / 40 = 4.5 a minute",
                "slower      4 × 60 / 80 = 3 a minute",
            ]),
            ("p", "The <strong>slower-skim</strong> preset is a reader allowed twice as "
                  "long, 80 seconds, who got all four: 4 × 60 / 80 = 3 gist answers a "
                  "minute. More right, fewer per minute. Which is better depends on what "
                  "the skim was for. If you only need to know whether the passage is "
                  "worth reading, the 40-second skim told you nearly as much in half the "
                  "time; if one wrong idea about it would mislead you, the extra 40 "
                  "seconds bought the fourth answer."),
            ("p", "Notice what the panel does not print. The line under the drill reports "
                  "the passage's 594 words over your 40 seconds, 891 words a minute, "
                  "because it reports every drill that way; the panel does not go on to "
                  "multiply that by your score. Three in four would make an effective "
                  "rate of about 668, nearly three times an ordinary reading, earned on "
                  "words that were never shown. A skim covers a passage the way a map "
                  "covers a country, and it is scored on what it was for: the gist, per "
                  "minute spent."),
            ("p", "A skim is a bet that the writer put the point of each paragraph first. "
                  "Exposition written to a plan usually does, and this passage mostly "
                  "obliges: “A glacier begins wherever more snow falls in winter than "
                  "melts in summer” is its first section in a sentence. Look again at the "
                  "section headed Stones far from home. Its first sentence sets a scene, "
                  "a boulder the size of a small car on a beach in New England, and its "
                  "point, that the ice carried the boulder there and the land keeps a "
                  "record of where the ice reached, comes at the end. A skimmer who "
                  "trusted that first sentence learned about a boulder and not why it "
                  "matters; the heading is what rescues the question about it."),
            ("p", "The studies of skimming say the same from the other side. Masson "
                  "(1982), with readers skimming stories, found that skimming lowered "
                  "their understanding of the important points as well as the "
                  "unimportant ones, but lowered it less. Duggan and Payne (2009) found "
                  "that readers skimming under time pressure did better on the important "
                  "points than readers made to go through the whole text at the same "
                  "speed, because they chose where to look, and still worse than a full "
                  "reading. A skim keeps more of the gist than of the detail. It does not "
                  "keep all of it."),
            ("p", "The 40-second limit is under a third of the time a full reading of this "
                  "passage takes for anyone reading below about 300 words a minute: at "
                  "240, the 594 words take 594 × 60 / 240 = 148.5 seconds. Set your own "
                  "skims the same way, from your baseline, and you will know what share "
                  "of a reading's time a skim is costing you."),
            ("p", "A skim costs something, and the next lesson, What Skimming Costs, "
                  "measures what: a skim against a full reading of a matched passage, "
                  "with the questions split into gist and detail."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "single",
            "passage": PASSAGES["P32"],
            "display": "gist",
            "limit": 40,
            "kind": "condition",
            "preset": "first-sentences",
            "presets": [
                {"id": "first-sentences", "label": "Three of four in 40 seconds",
                 "seconds": 40, "correct": 3, "total": 4,
                 "expect": {"drShown": "47/198 ≈ 23.7%", "drComp": "3/4 = 75%",
                            "drGistPerMin": "4.5 gist answers a minute"}},
                {"id": "slower-skim", "label": "Four of four in 80 seconds",
                 "seconds": 80, "correct": 4, "total": 4,
                 "expect": {"drShown": "47/198 ≈ 23.7%", "drComp": "1 = 100%",
                            "drGistPerMin": "3 gist answers a minute"}},
            ],
        }),
        "steps_title": "Skimming a text of your own",
        "steps_intro": "Five steps; the second is the skim itself.",
        "steps": [
            ("Set a limit from your baseline",
             "Work out how long a full reading of the text would take at your baseline "
             "rate, and give the skim under a third of that."),
            ("Headings, then first sentences",
             "Go through the headings first to see the plan, then the first sentence of "
             "each paragraph, in order. Do not stop to reread, and stop when the time "
             "is up."),
            ("Write the gist with the text hidden",
             "One sentence on what the text is about, and a phrase on what each section "
             "says."),
            ("Score it as a skim",
             "Check what you wrote against the text. Gist points right, times sixty, "
             "over the seconds; and note any section whose first sentence misled you."),
            ("Then today's Daily Drill",
             "Finish with today's reading from The Daily Drill, at your usual pace or "
             "your hold target."),
        ],
        "worked": {
            "title": "The first-sentences preset",
            "intro": [
                "A reader skimmed the 594-word glacier passage for 40 seconds. The "
                "display showed 141 words, and they answered 3 of the 4 gist questions.",
            ],
            "lines": [
                "shown        141 / 594 = 47/198 ≈ 23.7%",
                "gist right   3 of 4",
                "gist rate    3 × 60 / 40 = 4.5 a minute",
                "full reading at 240 a minute: 148.5 s",
            ],
            "after": [
                "The skim took under a third of the time a reading at 240 words a minute "
                "would, and showed under a quarter of the words. It bought three "
                "answers about the point of the passage and nothing about its details, "
                "which it never showed.",
            ],
        },
        "quiz_title": "Check the skim",
        "quiz": [
            {"q": "A skim shows 120 of a passage's 600 words for 30 seconds, and the "
                  "reader gets 2 of 4 gist questions right. What is the gist rate?",
             "a": ["4 gist answers a minute", "2 gist answers a minute",
                   "1,200 words a minute", "1/5 of the passage"], "c": 0,
             "why": "2 × 60 / 30 = 4. The 1,200 is the passage's length over the time, "
                    "a rate on words never shown; 1/5 is the share the skim showed."},
            {"q": "Why does the lab print no effective rate for a skim?",
             "a": ["It would count the words the skim never showed as read",
                   "A skim has no questions to score",
                   "The time limit makes a rate impossible to compute",
                   "Effective rates are only for passages without headings"], "c": 0,
             "why": "An effective rate is the passage's words over the time, times "
                    "comprehension. For a skim most of those words were never on the "
                    "screen, so the figure would credit reading that did not happen."},
            {"q": "On which text is a first-sentence skim most likely to mislead?",
             "a": ["An essay whose paragraphs open with an anecdote and state their point at the end",
                   "A report written to a plan, each paragraph opening with its claim",
                   "A textbook section whose headings name what each part explains",
                   "An encyclopaedia entry that opens with a definition"], "c": 0,
             "why": "A skim bets that the point comes first. The essay puts it last, so "
                    "the first sentences show the anecdotes and not the point."},
            {"q": "Reader A gets 3 of 4 gist questions in 40 seconds; reader B gets 4 of 4 "
                  "in 80 seconds. Which is right?",
             "a": ["A answered more per minute; B answered more in all",
                   "B answered more per minute and more in all",
                   "A and B have the same gist rate",
                   "A skimmed better, because A was faster"], "c": 0,
             "why": "A: 3 × 60 / 40 = 4.5 a minute. B: 4 × 60 / 80 = 3 a minute, with "
                    "one more answer. Which is better depends on the purpose, not on the "
                    "speed."},
        ],
        "mistakes": [
            ("Trusting first sentences always to carry the point",
             "They often do in exposition written to a plan, and the glacier passage "
             "mostly obliges. Its section Stones far from home does not: its first "
             "sentence is a boulder on a beach, and its point comes at the end. A skim "
             "is a bet on the text's structure, and a text built another way loses it."),
            ("Scoring a skim as a fast reading",
             "594 words in 40 seconds is 891 words a minute, and three in four right "
             "would make an effective rate of about 668 for words that were never shown. "
             "Score a skim on gist answers per minute."),
            ("Taking a good gist score for understanding the text",
             "Four gist answers right says you know what the passage is about. It says "
             "nothing about its details, and What Skimming Costs measures how many of "
             "those a skim loses."),
        ],
        "standard": (
            "Finish when you can score a skim and say where it fails.",
            "Given the words shown, the words in the passage, the gist questions right "
            "and the seconds, compute the share shown and the gist answers per minute; "
            "then point to a paragraph, here or in a text of your own, whose first "
            "sentence does not carry its point.",
        ),
        "note": (
            "One passage, one limit and four questions, so a single question is a "
            "quarter of the score. The passage has headings and mostly point-first "
            "paragraphs, the kind of text a skim suits; the same skim of a story or an "
            "argument would show you less."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "what-skimming-costs",
        "title": "What Skimming Costs",
        "module": MODULE,
        "one_line": "Skim one passage and read a matched one in full, then compare the gist and the detail you kept and choose between them for a purpose.",
        "summary": (
            "A skim is often treated as a fast reading with a little less understanding. "
            "Skim a passage on coral reefs under a 40-second limit, read a matched "
            "passage on volcanoes in full, and score each on three gist and three detail "
            "questions. Then decide, for a stated purpose, which of the two the purpose "
            "needs."
        ),
        "key": [
            "gist = gist right / gist asked",
            "detail = detail right / detail asked",
            "a skim: gist suffers less than detail",
            "choose by the purpose, not the rate",
        ],
        "key_label": "Two scores, not one",
        "concepts_intro": (
            "The effective rate from Measure Your Reading counts every question the "
            "same. This lesson splits the questions, because a skim does not lose them "
            "evenly."
        ),
        "concepts": [
            ("Two kinds of question",
             "Each passage carries three gist questions, on what it is about and what "
             "follows from it, and three detail questions, on a fact stated once. "
             "Scored apart, they show what a skim keeps and what it drops."),
            ("Matched, not identical",
             "The reef and volcano passages are the same kind of text, with headings, "
             "and within 23 words of each other in length. They are still different "
             "passages, and whichever you do second has the first behind it, so the "
             "lab alternates the order from one comparison to the next."),
            ("The purpose decides",
             "If you need to know what a text argues, a skim that keeps the gist did "
             "its job. If you need a figure from it, a skim that lost the detail "
             "failed, however fast it was."),
        ],
        "read_title": "Gist and detail, scored apart",
        "read_intro": (
            "Two readings, six questions each, and four scores instead of two."
        ),
        "body": [
            ("p", "The drill has two readings; do them in the order the lab gives above "
                  "them. The one labelled Skim is the reef passage, shown whole for 40 "
                  "seconds and then taken away. The prompt under it says to read at your usual pace; "
                  "for this one, skim instead, however you skim, because the passage "
                  "disappears when the 40 seconds run out. It is logged as a condition. "
                  "The other is the volcano passage, read in full at your usual pace and "
                  "logged as a test. Each is followed by six questions, three on the gist "
                  "and three on details, and the panel scores the two kinds separately."),
            ("p", "The <strong>typical</strong> preset is a reader who skimmed the reef "
                  "passage's 410 words in the 40 seconds, 615 words a minute, and got 2 of "
                  "3 gist and 1 of 3 detail questions; then read the volcano passage's 387 "
                  "words in 90 seconds, 258 words a minute, and got all six. The skim "
                  "lost one gist question and two details."),
            ("math", [
                "skim:  gist 2/3   detail 1/3   410 words in 40 s",
                "read:  gist 3/3   detail 3/3   387 words in 90 s",
                "skim effective rate   615 × 3/6 = 307.5",
                "read effective rate   258 × 6/6 = 258",
            ]),
            ("p", "Now look at the effective rates. The skim's is 307.5 words a minute and "
                  "the reading's 258, so by the single number Measure Your Reading taught "
                  "you to report, the skim won. That is why this lesson splits the score. "
                  "The effective rate counts a gist question and a detail question as "
                  "equal, and a purpose seldom does: if you needed the reef passage's "
                  "facts, a skim that kept one detail in three was not a faster way to "
                  "them."),
            ("p", "The <strong>good-skimmer</strong> preset kept all three gist answers "
                  "and two of the three details from the same 40-second skim, an "
                  "effective rate of 615 × 5/6 = 512.5. Some readers skim well, and this "
                  "drill is how you find out whether you are one of them; one pair of "
                  "passages is not enough to tell."),
            ("p", "The typical preset is the pattern the studies report. Masson (1982), "
                  "with readers skimming stories, found that skimming lowered their "
                  "understanding of the important points as well as the unimportant "
                  "ones, but lowered it less. Duggan and Payne (2009) found that readers "
                  "skimming under time pressure did better on the important points than "
                  "readers made to go through the whole text at the same speed, and still "
                  "worse than readers who read it all. In a phrase: gist suffers less "
                  "than detail. Both studies were laboratory tasks, and your two "
                  "passages are not theirs."),
            ("p", "If your skim kept the details as well as your reading did, you have not "
                  "refuted the studies, and they have not refuted you. One pair of "
                  "passages on one day is one measurement, and the studies report "
                  "averages over many readers. The question for your log is whether it "
                  "happens again on another pair."),
            ("p", "One question here is about 16.7 points of comprehension, and one gist "
                  "or detail question is a third of its kind's score. A difference of one "
                  "question between the two readings is not a result; the two details "
                  "the typical preset lost are the beginning of one."),
            ("p", "A skim can come before a reading as well as instead of it, and "
                  "Previewing Before Reading asks whether thirty seconds of it pays for "
                  "itself."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P33"], PASSAGES["P34"]],
            "kinds": True,
            "a": {"display": "normal", "limit": 40, "kind": "condition",
                  "label": "Skim (the passage disappears at 40 seconds)"},
            "b": {"display": "normal", "kind": "test", "label": "Full reading"},
            "preset": "typical",
            "presets": [
                {"id": "typical", "label": "Skim 2/3 gist, 1/3 detail; reading 3/3, 3/3",
                 "secondsA": 40, "gistA": 2, "gistTotalA": 3, "detailA": 1, "detailTotalA": 3,
                 "secondsB": 90, "gistB": 3, "gistTotalB": 3, "detailB": 3, "detailTotalB": 3,
                 "expect": {"drGistA": "2/3 ≈ 66.7%", "drDetailA": "1/3 ≈ 33.3%",
                            "drGistB": "1 = 100%", "drDetailB": "1 = 100%",
                            "drWpmA": "615 wpm", "drWpmB": "258 wpm",
                            "drErrA": "307.5 wpm", "drErrB": "258 wpm"}},
                {"id": "good-skimmer", "label": "Skim 3/3 gist, 2/3 detail; reading 3/3, 3/3",
                 "secondsA": 40, "gistA": 3, "gistTotalA": 3, "detailA": 2, "detailTotalA": 3,
                 "secondsB": 90, "gistB": 3, "gistTotalB": 3, "detailB": 3, "detailTotalB": 3,
                 "expect": {"drGistA": "1 = 100%", "drDetailA": "2/3 ≈ 66.7%",
                            "drGistB": "1 = 100%", "drDetailB": "1 = 100%",
                            "drErrA": "512.5 wpm"}},
            ],
        }),
        "steps_title": "Testing your own skims",
        "steps_intro": "Five steps. The first is the one that decides the rest.",
        "steps": [
            ("State the purpose first",
             "Write down what you need from the text: its point, or particular facts. "
             "The choice between a skim and a reading follows from that, not from the "
             "time you have."),
            ("Skim one, read one",
             "Take two texts of the same kind and length. Skim one under a limit of "
             "less than half its reading time, and read the other in full."),
            ("Score gist and detail apart",
             "For each, with the text hidden, write down its point and three facts from "
             "it, then check them. Count the two kinds separately."),
            ("Choose for the next text",
             "If your skims keep the detail on several pairs, a skim may do for texts "
             "like these; if the detail falls, read whatever you need facts from."),
            ("Then today's Daily Drill",
             "Finish with today's reading from The Daily Drill."),
        ],
        "worked": {
            "title": "The typical preset",
            "intro": [
                "Skim: 410 words in 40 seconds, gist 2 of 3, detail 1 of 3. Reading: 387 "
                "words in 90 seconds, gist 3 of 3, detail 3 of 3.",
            ],
            "lines": [
                "skim rate    410 × 60 / 40 = 615 words a minute",
                "read rate    387 × 60 / 90 = 258 words a minute",
                "gist         2/3 against 3/3",
                "detail       1/3 against 3/3",
            ],
            "after": [
                "The skim lost one gist question and two detail questions. For a "
                "purpose that needs the point, it did the job in under half the time; "
                "for one that needs the facts, it did not, and its higher effective "
                "rate hides that.",
            ],
        },
        "quiz_title": "Check the choice",
        "quiz": [
            {"q": "A skim scores gist 3/3 and detail 1/3; a full reading of a matched "
                  "passage scores 3/3 and 3/3. You must quote figures from the text at a "
                  "meeting. Which do you use on texts like these?",
             "a": ["The full reading: the purpose needs detail, which the skim lost",
                   "The skim: its gist was as good as the reading's",
                   "The skim: its effective rate is probably higher",
                   "Either: the totals differ by only two questions"], "c": 0,
             "why": "Quoting figures is a purpose that needs detail, and detail is what "
                    "the skim lost. Gist and the effective rate answer other questions."},
            {"q": "What did Masson (1982) find about skimming?",
             "a": ["It lowered understanding of important and unimportant points, less for important ones",
                   "It left understanding of the important points unchanged",
                   "It lowered understanding of important points more than unimportant ones",
                   "It made no difference to understanding at all"], "c": 0,
             "why": "Skimming cost understanding of both, but cost less on the important "
                    "points: gist suffers less than detail, not nothing."},
            {"q": "Why can the effective rate make a skim look better than a full "
                  "reading?",
             "a": ["It counts gist and detail questions alike and rewards the skim's speed",
                   "It leaves out the time the skim took",
                   "It counts only the gist questions",
                   "It divides by the questions asked instead of the questions right"], "c": 0,
             "why": "The skim's rate is high, and the product with comprehension does not "
                    "care which questions were lost. A purpose often does."},
            {"q": "Your skim kept every detail. What follows?",
             "a": ["Nothing yet: one pair of passages is one measurement",
                   "The studies of skimming are wrong",
                   "You should skim everything from now on",
                   "Your reading rate is now the skim's rate"], "c": 0,
             "why": "Two different passages, compared once, in one order. Run it again "
                    "on another pair before you change how you read."},
        ],
        "mistakes": [
            ("Treating a skim as a fast reading with a little less understanding",
             "A skim does not lose evenly. Gist suffers less than detail (Masson 1982), "
             "and skimmers who choose where to look keep more of the important points "
             "than readers pushed through the whole text at the same speed, still below "
             "a full reading (Duggan and Payne 2009). In the typical preset the skim "
             "lost one gist question and two of three details."),
            ("Choosing by the effective rate",
             "In the typical preset the skim's 307.5 beat the reading's 258, and the "
             "skim kept one detail in three. One number cannot say which kind of "
             "understanding a purpose needs."),
            ("Reading a one-question difference as a result",
             "One question is about 16.7 points of comprehension, and a third of a "
             "kind's score. Gist scores of 2/3 and 3/3 differ by a single answer."),
        ],
        "standard": (
            "Finish when you can choose between a skim and a reading and say why.",
            "Given gist and detail scores for a skim and a full reading and a stated "
            "purpose, say which the purpose needs, and justify it from the score of the "
            "kind the purpose needs, not from the total or the effective rate.",
        ),
        "note": (
            "Two passages compared once. They are matched in kind and length but are "
            "different texts, and whichever you did second had the first behind it, "
            "which is why the order alternates. Masson's and Duggan and Payne's findings "
            "come from laboratory tasks; only your log, over several pairs, can say how "
            "your own skims behave."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "previewing-before-reading",
        "title": "Previewing Before Reading",
        "module": MODULE,
        "one_line": "Preview a passage for thirty seconds before reading it, count the preview in the time, and see whether it paid.",
        "summary": (
            "A preview of the headings, the first paragraph and the last costs time "
            "before the reading starts. Read a passage on bridges cold, preview a "
            "matched passage on refrigerators for 30 seconds before reading it, with the "
            "preview counted in the time, and compare the two effective rates."
        ),
        "key": [
            "time = preview + reading",
            "effective rate = rate × comprehension",
            "pays if comprehension rises enough",
            "or if it lets you skip a part",
            "always count the preview's time",
        ],
        "key_label": "Previewing in five lines",
        "concepts_intro": (
            "Study manuals have advised a look at a text's structure before reading it "
            "for a long time. The drill puts a price on the look."
        ),
        "concepts": [
            ("What a preview shows",
             "Headings, the first paragraph and the last: in a text written to a plan, "
             "the question it starts from, its parts and where it ends up. The drill "
             "shows them for 30 seconds, then the whole passage, and the clock runs "
             "through both."),
            ("The preview is in the time",
             "A preview's cost is easy to forget, because it does not feel like "
             "reading. Counting it is the only fair comparison: 30 seconds before a "
             "120-second reading make a 150-second reading."),
            ("Two ways to pay",
             "A preview earns its time back in one of two ways: you understand more of "
             "what you then read, or you learn that a part does not need reading and "
             "skip it. If neither happens, it was a cost."),
        ],
        "read_title": "Putting a price on the look",
        "read_intro": (
            "A cold reading and a previewed one, with the preview's seconds counted."
        ),
        "body": [
            ("p", "The drill has two readings, in the order the lab says above them. In one "
                  "you read a passage about bridges cold, at your usual pace, logged as a "
                  "test. In the other a passage about refrigerators shows its headings and "
                  "its first and last paragraphs for 30 seconds, then the whole passage; "
                  "read it at your usual pace and press Done. The clock starts at the "
                  "preview, so the 30 seconds are in your time, and the reading is logged "
                  "as a condition. Both have six questions."),
            ("p", "The advice is older than any test of it. Robinson's SQ3R (1946) begins "
                  "with a survey of a chapter's headings before the reading, and Adler "
                  "and Van Doren (1972) advise looking a text over before deciding how to "
                  "read it. Both are advice, and the drill is a way to test it on your "
                  "own reading."),
            ("math", [
                "cold:      451 × 60 / 110 = 246;    246 × 4/6 = 164",
                "previewed: 433 × 60 / (30 + 120) = 173.2;  × 6/6 = 173.2",
                "difference 173.2 − 164 = +9.2",
            ]),
            ("p", "Those are the <strong>pays</strong> preset. The reader read the 451-word "
                  "bridge passage cold in 110 seconds, 246 words a minute, and got 4 of 6: "
                  "an effective rate of 164. They previewed the 433-word refrigerator "
                  "passage for 30 seconds and read it in 120, 150 seconds in all, which "
                  "is 173.2 words a minute counted from the start of the preview, and got "
                  "all six: an effective rate of 173.2, which is 9.2 above. The preview "
                  "cost 30 seconds and came with two more questions right."),
            ("p", "The <strong>does-not</strong> preset has the same times with five right "
                  "on both: 246 × 5/6 = 205 for the cold reading, 173.2 × 5/6 ≈ 144.3 for "
                  "the previewed one, about 60.7 below. The preview bought nothing the "
                  "reader did not get anyway, and its 30 seconds were a fifth of the "
                  "time."),
            ("p", "Leave the 30 seconds out of the pays preset and the previewed reading "
                  "becomes 433 × 60 / 120 = 216.5 words a minute, faster than the cold "
                  "one, and for the wrong reason. A comparison that starts the clock "
                  "after the preview has made the preview free, and the lab refuses to "
                  "make it."),
            ("p", "Where a preview pays most is the second way, which this drill cannot "
                  "show. On a long report the headings and the last paragraph can tell "
                  "you that two sections do not concern you, and skipping them saves "
                  "minutes, not seconds. The passages here are short and every part is "
                  "asked about, so a preview can only pay through comprehension."),
            ("p", "If your preview cost more than it paid, or paid far more than either "
                  "preset, you have not refuted Robinson's advice, and it has not refuted "
                  "you: two different passages, read once each, in an order that "
                  "alternates, are one comparison. Run it again on another pair before "
                  "you change how you read."),
            ("p", "A preview of a passage takes thirty seconds; a preview of a whole book "
                  "takes a few minutes, and Inspectional Reading, which opens the next "
                  "module, times one."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P35"], PASSAGES["P36"]],
            "a": {"display": "normal", "kind": "test", "label": "Read cold"},
            "b": {"display": "preview", "limit": 30, "kind": "condition",
                  "label": "Preview for 30 seconds, then read"},
            "preset": "pays",
            "presets": [
                {"id": "pays", "label": "Cold 4 of 6; previewed 6 of 6",
                 "secondsA": 110, "correctA": 4, "totalA": 6,
                 "secondsB": 150, "correctB": 6, "totalB": 6,
                 "expect": {"drWpmA": "246 wpm", "drWpmB": "173.2 wpm",
                            "drErrA": "164 wpm", "drErrB": "173.2 wpm",
                            "drErrDiff": "+9.2 wpm"}},
                {"id": "does-not", "label": "Cold 5 of 6; previewed 5 of 6",
                 "secondsA": 110, "correctA": 5, "totalA": 6,
                 "secondsB": 150, "correctB": 5, "totalB": 6,
                 "expect": {"drErrA": "205 wpm", "drErrB": "≈ 144.3 wpm",
                            "drErrDiff": "≈ −60.7 wpm"}},
            ],
        }),
        "steps_title": "Testing a preview on your own reading",
        "steps_intro": "Five steps; the clock runs through the second.",
        "steps": [
            ("Read one text cold",
             "Pick two texts of the same kind and length. Time a reading of the first "
             "at your usual pace, and check what you kept."),
            ("Preview the other, clock running",
             "Start the clock, look at the headings and the first and last paragraphs "
             "for about 30 seconds, then read the whole text, and stop the clock at the "
             "end."),
            ("Score both with the preview counted",
             "Words × 60 over all the seconds, times the share of questions right, for "
             "each reading."),
            ("Note any part you could have skipped",
             "On a long text, mark what the preview told you to skip. That is where a "
             "preview earns most, and the short passages here cannot show it."),
            ("Then today's Daily Drill",
             "Finish with today's reading from The Daily Drill."),
        ],
        "worked": {
            "title": "The pays preset",
            "intro": [
                "Cold: 451 words in 110 seconds, 4 of 6. Previewed: 433 words, a "
                "30-second preview and 120 seconds of reading, 6 of 6.",
            ],
            "lines": [
                "cold rate          451 × 60 / 110 = 246",
                "cold effective     246 × 4/6 = 164",
                "previewed rate     433 × 60 / 150 = 173.2",
                "previewed effect.  173.2 × 6/6 = 173.2",
                "difference         173.2 − 164 = +9.2",
            ],
            "after": [
                "Without the preview's 30 seconds the previewed rate would have been "
                "216.5, and the difference 52.5 instead of 9.2. Counting the preview is "
                "the whole of the method.",
            ],
        },
        "quiz_title": "Check the price",
        "quiz": [
            {"q": "A reader previews a 450-word passage for 30 seconds, then reads it in "
                  "90 seconds and gets 6 of 6. What is the effective rate with the "
                  "preview counted?",
             "a": ["225 words a minute", "300 words a minute", "200 words a minute",
                   "250 words a minute"], "c": 0,
             "why": "450 × 60 / (30 + 90) = 225, times 6/6. 300 leaves the preview out."},
            {"q": "With a preview, a reader's score rose from 4 of 6 to 5 of 6 and their "
                  "effective rate fell. What follows?",
             "a": ["On this pair the preview cost more time than its extra question was worth",
                   "Previewing never pays",
                   "The preview's time should have been left out",
                   "The effective rate is wrong whenever comprehension rises"], "c": 0,
             "why": "The effective rate already weighs the extra question against the "
                    "extra time. One pair, though, is one comparison, and a "
                    "one-question difference is not a result."},
            {"q": "When can a preview pay without raising comprehension at all?",
             "a": ["When it shows that a section is not needed, and you skip it",
                   "When the passage has no headings",
                   "When the preview lasts less than ten seconds",
                   "When you read the same passage twice"], "c": 0,
             "why": "Skipping a section saves its reading time outright, which can be "
                    "far more than the preview cost."},
        ],
        "mistakes": [
            ("Treating a preview as free",
             "It costs time, and the time has to be counted. In the pays preset 30 "
             "seconds came with two more questions right and the effective rate rose "
             "by 9.2; in the does-not preset the same 30 seconds bought nothing and the "
             "effective rate fell by about 60.7. A preview pays when it raises "
             "comprehension or lets you skip a section."),
            ("Starting the clock after the preview",
             "Leaving the 30 seconds out turns 173.2 into 216.5 in the pays preset, and "
             "makes any preview look like a gain in speed."),
            ("Previewing a text that has no plan",
             "Headings and first and last paragraphs are a bet that the text was built "
             "to a plan. A story or a letter without headings shows you little in "
             "thirty seconds."),
        ],
        "standard": (
            "Finish when you can say whether a preview paid, with its time counted.",
            "Given the words, times and scores of a cold reading and a previewed one, "
            "compute both effective rates with the preview in the time, give the "
            "difference, and say whether the preview paid and by which of the two ways.",
        ),
        "note": (
            "Two different passages, one reading each: the bridge and refrigerator "
            "passages are matched in kind and length but not in subject, and the second "
            "reading has the first behind it, which is why the order alternates. The "
            "drill can show a preview paying only through comprehension; skipping a "
            "section, the larger saving, needs a longer text than these."
        ),
    },
]
