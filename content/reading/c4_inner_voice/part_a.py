"""Course 4, lessons 01-06 -- the inner voice, and the flashed word stream."""

from reading.passages import PASSAGES

DAILY = ("Then today's Daily Drill",
         "Open The Daily Drill and run today's session: the next pool passage with the "
         "pacer at your hold target, or a test at natural pace when the panel says one "
         "is due. A comparison like this one is a separate reading, never a "
         "replacement for that session.")

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-inner-voice",
        "title": "The Inner Voice",
        "module": "The inner voice",
        "one_line": "Read one story aloud and another silently, and compare the two rates.",
        "summary": (
            "Most readers hear the words as they read silently, and the speed-reading "
            "tradition calls that voice a brake held at speaking pace. Read one easy "
            "story aloud and another silently, compute the two rates and their ratio, "
            "and see what the ratio says about the advice to get rid of the voice."
        ),
        "key": [
            "rate = words × 60 / seconds",
            "ratio = silent rate / aloud rate",
            "aloud: about 183 words a minute",
            "silent: about 238 words a minute",
            "inner speech is not full speech",
        ],
        "key_label": "Two rates and a ratio",
        "concepts_intro": (
            "The claim to test is simple: if the inner voice held you to the pace of "
            "speech, you could not read silently faster than you read aloud."
        ),
        "concepts": [
            ("Two readings, one ratio",
             "You read one passage aloud and time it, then a second silently and time "
             "it. Dividing the silent rate by the aloud rate gives a single number: "
             "how many times faster your eyes and your inner voice go than your "
             "mouth."),
            ("The published averages",
             "Brysbaert (2019) pooled the studies of adult reading rates in English: "
             "about 238 words a minute for silent reading of non-fiction, 260 for "
             "fiction, and about 183 for reading aloud. They are averages over many "
             "readers, not targets."),
            ("Inner speech is not speaking",
             "The voice you hear when you read silently is not your mouth moving "
             "quietly. Inner speech is not full articulation, so it is not tied to "
             "the pace at which lips, tongue and breath can make the sounds (Rayner "
             "and colleagues, 2016)."),
        ],
        "read_title": "What the ratio says about the voice",
        "read_intro": (
            "One reading aloud, one silently, and a division. The argument is in what "
            "the division can come out as."
        ),
        "body": [
            ("p", "The lab below has two readings of two easy stories. Read the first, "
                  "<em>The Bell at Six</em>, aloud at a natural speaking pace &mdash; a "
                  "whisper is enough &mdash; and press Done when you finish speaking; "
                  "it has no questions. Read the second, <em>Bread in the Dark</em>, "
                  "silently at your usual pace, then answer its six questions. The lab "
                  "divides the second rate by the first."),
            ("p", "The advice you are testing is old and widely repeated in "
                  "speed-reading courses and books: the voice in your head is a habit "
                  "left over from learning to read aloud, it holds silent reading to "
                  "the pace of speech, and a fast reader must learn to stop hearing "
                  "the words. "
                  "Readers who practise this often say the voice grows fainter as they "
                  "speed up, and the experience is real enough to take seriously."),
            ("p", "The claim makes a prediction you can check in five minutes. If the "
                  "voice held you to speaking pace, your silent rate could not be much "
                  "above your aloud rate. The published averages already say "
                  "otherwise: Brysbaert's review puts silent reading of non-fiction at "
                  "about 238 words a minute and reading aloud at about 183. On average, "
                  "adults read silently about 1.3 times as fast as they speak."),
            ("def", ("The ratio",
                     "The <strong>silent-to-aloud ratio</strong> is the silent rate "
                     "divided by the aloud rate, each in words a minute. Above 1, you "
                     "read silently faster than you speak; the lab prints it as a "
                     "fraction and a percentage, so 1.3 reads as about 130%.")),
            ("p", "The preset <strong>typical</strong> is those averages as one reader: "
                  "183 words aloud in 60 seconds, which is exactly what the "
                  "&ldquo;I can&rsquo;t read aloud here&rdquo; button writes, and 476 "
                  "words silently in 120 seconds with five of six questions right. The "
                  "tiles read 183 wpm and 238 wpm, and the ratio 238/183, about "
                  "130.1%."),
            ("p", "The preset <strong>fast-silent</strong> is a reader who read the "
                  "whole of <em>The Bell at Six</em>, 477 words, aloud in 159 seconds, "
                  "which is 180 wpm, and the 453 words of <em>Bread in the Dark</em> "
                  "silently in 84.9375 seconds, which is 320 wpm. The ratio is 16/9, "
                  "about 177.8%: silent reading nearly 1.8 times the speed of speech, "
                  "by a reader who may well still hear every word."),
            ("p", "Now read your own pair. A ratio above 1 means you already read "
                  "silently faster than you can speak, and so whatever your inner "
                  "voice is doing, it is not holding you to the pace of your mouth. A "
                  "ratio near 1 or below is unusual for easy stories; check that you "
                  "read the silent passage at your usual pace and not carefully. "
                  "Either way, if your result goes the other way from Brysbaert's "
                  "averages, you have not refuted the review, and the review has not "
                  "refuted you: it describes many readers, and this is one pair of "
                  "your readings."),
            ("p", "Only the silent reading has questions, and the lab compares rates, "
                  "not effective rates. The aloud reading is there to time your "
                  "speaking pace, and a reader performing a text aloud is attending to "
                  "the performance as much as to the meaning. The silent side still "
                  "prints its comprehension and effective rate, so you can see that the "
                  "rate was a reading and not a skim."),
            ("p", "If you cannot read aloud where you are, press &ldquo;I can&rsquo;t "
                  "read aloud here&rdquo;. The lab writes Brysbaert's oral average, 183 "
                  "words in 60 seconds, into the aloud side, labels it as a published "
                  "figure, and logs nothing for that side. Your ratio is then your "
                  "silent rate against other people's speaking rate, which is a weaker "
                  "comparison; do the aloud reading on another day if you can."),
            ("p", "So the voice is not a brake set at speaking speed. Whether it does "
                  "useful work, and what happens to your reading when it is kept busy, "
                  "is a different question, and the next lesson, Silencing the Inner "
                  "Voice, tests it with a matched pair of passages."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P25"], PASSAGES["P26"]],
            "ratioOf": "wpm",
            "a": {"label": "Aloud", "display": "aloud", "questions": False, "kind": "other"},
            "b": {"label": "Silently", "kind": "test"},
            "preset": "typical",
            "presets": [
                {"id": "typical", "label": "183 aloud, 238 silently",
                 "wordsA": 183, "secondsA": 60, "correctA": 0, "totalA": 0,
                 "wordsB": 476, "secondsB": 120, "correctB": 5, "totalB": 6,
                 "expect": {"drWpmA": "183 wpm", "drWpmB": "238 wpm", "drRatio": "238/183 ≈ 130.1%"}},
                {"id": "fast-silent", "label": "180 aloud, 320 silently",
                 "wordsA": 477, "secondsA": 159, "correctA": 0, "totalA": 0,
                 "wordsB": 453, "secondsB": "84.9375", "correctB": 5, "totalB": 6,
                 "expect": {"drWpmA": "180 wpm", "drWpmB": "320 wpm", "drRatio": "16/9 ≈ 177.8%"}},
            ],
            "panel_title": "Aloud against silent",
            "panel_intro": (
                "Your measurement: two timed readings, the first aloud with no "
                "questions, the second silent with six. The ratio tile divides the "
                "silent rate by the aloud rate. Choose a preset to see a worked pair, "
                "or do the drill to fill the boxes with your own."
            ),
        }),
        "steps_title": "Measuring your speaking and silent rates",
        "steps_intro": (
            "To repeat the comparison on another day, use two fresh passages of the "
            "same difficulty, and these steps in this order."
        ),
        "steps": [
            ("Choose two fresh, easy passages",
             "Two texts you have not read, of about the same length and difficulty. "
             "Easy texts keep the aloud reading from turning into a struggle with "
             "pronunciation."),
            ("Read the first aloud at a natural pace",
             "As you would read to someone across a table, not a performance and not "
             "a race. A whisper is enough. Time it from the first word to the last."),
            ("Read the second silently at your usual pace",
             "Time it, then answer questions on it with the text out of sight, so "
             "that the silent rate is a reading and not a skim."),
            ("Divide the silent rate by the aloud rate",
             "Each rate is words × 60 / seconds. A ratio above 1 means your silent "
             "reading already outruns your speech."),
            DAILY,
        ],
        "worked": {
            "title": "The published averages as a ratio",
            "intro": [
                "Brysbaert's averages for adult readers of English: about 238 words a "
                "minute silently, for non-fiction, and about 183 aloud.",
            ],
            "lines": [
                "silent rate = 238 words a minute",
                "aloud rate = 183 words a minute",
                "ratio = 238 / 183 ≈ 1.3",
            ],
            "after": [
                "The average reader reads silently about 1.3 times as fast as they "
                "speak. The "
                "advice to eliminate the voice assumes the voice sets the speed; the "
                "ratio shows that silent reading is already past the speed of speech.",
            ],
        },
        "quiz_title": "Reading the ratio",
        "quiz": [
            {"q": "A reader reads 400 words aloud in 120 seconds and 450 words silently "
                  "in 90 seconds. What is the silent-to-aloud ratio?",
             "a": ["9/8 ≈ 1.1", "2/3 ≈ 0.7", "1.5", "2.25"],
             "c": 2,
             "why": "Aloud is 400 × 60 / 120 = 200 words a minute; silent is "
                    "450 × 60 / 90 = 300. The ratio is 300 / 200 = 1.5. Dividing the "
                    "word counts gives 9/8, and dividing aloud by silent gives 2/3."},
            {"q": "Your silent rate is well above your aloud rate. What does that imply "
                  "for the advice that the inner voice must go because it limits you to "
                  "speaking speed?",
             "a": ["Your silent reading is already faster than speech, so the voice is "
                   "not holding you to speaking speed",
                   "Reading aloud is the faster way for you to read",
                   "Your inner voice must already have gone",
                   "The aloud reading was too slow to count"],
             "c": 0,
             "why": "The advice predicts that silent reading cannot outrun speech. A "
                    "silent rate above the aloud rate contradicts the prediction. It "
                    "does not show that your voice has gone: inner speech is not full "
                    "articulation, so it need not keep to the speed of your mouth."},
            {"q": "Why does this lab compare the two rates rather than the two "
                  "effective rates?",
             "a": ["Comprehension is always complete when reading aloud",
                   "The aloud reading has no questions; it is there to time your "
                   "speaking pace",
                   "Effective rates cannot be divided",
                   "The silent reading's questions are only about gist"],
             "c": 1,
             "why": "The aloud side has no questions, so it has no effective rate. Its "
                    "job is to measure how fast you speak a text, which is the speed "
                    "the advice says your silent reading is held to."},
            {"q": "You press &ldquo;I can&rsquo;t read aloud here&rdquo;. What goes into "
                  "the aloud side?",
             "a": ["Your last aloud reading from the log",
                   "Nothing, and the ratio tile stays blank",
                   "Brysbaert's oral average, 183 words in 60 seconds, labelled and not "
                   "logged",
                   "Your silent rate divided by 1.3"],
             "c": 2,
             "why": "The fallback writes the published figure into the boxes and says "
                    "so; it logs nothing, because it is not your reading. The ratio is "
                    "then your silent rate against an average, a weaker comparison."},
        ],
        "mistakes": [
            ("The inner voice limits you to speaking speed, so it must go",
             "Silent reading is already faster than reading aloud on average: about "
             "238 words a minute against 183 in Brysbaert's review. Inner speech is "
             "not full articulation, so it is not held to the speed of the mouth. A "
             "voice that accompanies reading at 1.3 times the speed of speech is not "
             "a brake set at speaking pace."),
            ("Reading the published averages as targets",
             "238 and 183 are averages over many readers and many texts. A reader "
             "whose ratio is 1.5 or 1.1 is not ahead or behind; the ratio only has to "
             "be above 1 for the argument to go through for that reader."),
            ("Treating one pair as a fact about yourself",
             "The two readings were on different stories, in one order, on one day. "
             "Easy stories, a nervous aloud reading or a careful silent one all move "
             "the ratio. It is one measurement of each rate, and a second pair on "
             "another day will differ."),
        ],
        "standard": (
            "Finish when you can turn two rates into a ratio and say what it implies.",
            "Given an aloud rate and a silent rate, compute the ratio to one decimal, "
            "and say in a sentence what a ratio above 1 implies for the advice to "
            "eliminate the inner voice: silent reading already outruns speech, so the "
            "voice that comes with it is not holding reading to speaking pace. The "
            "ratio right and that sentence pass."
        ),
        "note": (
            "This is one pair of readings, on two different stories, in one order: "
            "which passage you read and which came first both move the ratio, and the "
            "lab alternates the order between visits for that reason. Easy stories "
            "were chosen so that the aloud reading measures speaking pace, not "
            "pronunciation; on harder text both rates fall."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "silencing-the-inner-voice",
        "title": "Silencing the Inner Voice",
        "module": "The inner voice",
        "one_line": "Read one passage normally and a matched one while counting under your breath, and compare what you understood.",
        "summary": (
            "If the inner voice were only a brake, keeping it busy should cost nothing. "
            "Read one passage normally and a matched one while counting under your "
            "breath, the method Slowiaczek and Clifton used, and compare the two "
            "effective rates."
        ),
        "key": [
            "effective rate = rate × correct / 6",
            "difference = effective B − effective A",
            "one question ≈ 16.7 points",
            "a lapse in the counting voids B",
        ],
        "key_label": "Suppression in four lines",
        "concepts_intro": (
            "You cannot switch the inner voice off at will, but you can keep the "
            "machinery of speech busy and see what happens to your reading."
        ),
        "concepts": [
            ("Articulatory suppression",
             "Saying something over and over under your breath, such as "
             "&ldquo;one-two-three&rdquo;, occupies the mouth and the speech "
             "machinery while you read. Slowiaczek and Clifton (1980) used counting "
             "this way; mouthing the numbers is enough."),
            ("The effective rate decides it",
             "A rate that goes up while comprehension goes down may be a gain or a "
             "loss. The effective rate, rate times the share of questions right, puts "
             "both into one number, and the difference between the two readings' "
             "effective rates is the result."),
            ("Two tasks at once",
             "Counting while reading is a second task. Any cost it brings may come "
             "from losing the inner voice, or simply from doing two things at once, "
             "and this drill cannot tell those apart."),
        ],
        "read_title": "What keeping the voice busy costs",
        "read_intro": (
            "Two matched passages, one read with the voice free and one with it "
            "occupied, and what the studies found when they did the same."
        ),
        "body": [
            ("p", "The usual advice for getting rid of the inner voice is to give it "
                  "something else to do: hum, count, or repeat a word under your "
                  "breath while you read, until the habit of hearing the text fades. "
                  "If the voice were only a brake, this should make reading faster and "
                  "cost nothing. The drill tests that on two matched passages, "
                  "<em>Riding on Warm Air</em> and <em>Trees That Stand in the "
                  "Sea</em>, which are of the same length and difficulty to within a "
                  "few words and a fraction of a grade."),
            ("p", "Read one normally. Read the other while counting &ldquo;one-two-three, "
                  "one-two-three&rdquo; steadily under your breath, from the first word "
                  "to the last; mouthing the numbers without sound is enough. After you "
                  "press Done on the counting reading, tick &ldquo;I kept counting the "
                  "whole way&rdquo; only if you did. Both readings have six questions, "
                  "and both are logged as condition readings, outside your baselines "
                  "and tests."),
            ("p", "The preset <strong>typical</strong> is a reader who read 392 words "
                  "normally in 96 seconds with all six questions right, which is 245 "
                  "wpm and an effective rate of 245, and 393 words while counting in 90 "
                  "seconds with four right. The counting reading was faster, 262 wpm, "
                  "and its effective rate is 262 × 4/6, about 174.7. The difference "
                  "tile reads about −70.3 wpm: the reader went 17 words a minute faster "
                  "and lost two questions, and the product says the trade was a bad "
                  "one."),
            ("p", "The preset <strong>easy-text</strong> is a reader on easier text: "
                  "403 words normally in 93 seconds, 260 wpm with six right, and 399 "
                  "words while counting in 90 seconds, 266 wpm with five right, an "
                  "effective rate of about 221.7. The difference is about −38.3 wpm, "
                  "and it rests on one question. The lab says why that matters: one "
                  "question is about 16.7 points of comprehension, and a "
                  "one-question difference is not a result."),
            ("p", "The studies point the same way, and they are few and small. "
                  "Hardyck and Petrinovich (1970) recorded the activity of the speech "
                  "muscles in the throat and fed it back to readers so that they could "
                  "learn to keep it quiet; when they did, comprehension of the "
                  "difficult text fell, while comprehension of the easy text held up. "
                  "Slowiaczek and Clifton (1980) had readers count aloud, as in this "
                  "drill, and found that it impaired their comprehension of passages "
                  "they read, though not of passages they heard."),
            ("p", "That last contrast is worth a second look. Counting did not stop "
                  "people understanding language in general; it hurt reading. The "
                  "studies do not settle why, and the second-task problem is always "
                  "there: counting takes attention, and a reader doing two things at "
                  "once may lose comprehension whatever the inner voice does. What "
                  "they do not support is the claim that occupying the voice is free."),
            ("p", "Now read your own tiles. If the counting reading's effective rate is "
                  "lower, you have seen in your own numbers the cost the studies "
                  "describe. If it is the same or higher, look at the tick first: a "
                  "reading where the counting lapsed is a normal reading of a different "
                  "passage, and the comparison is void. If you kept counting and still "
                  "did as well, you have not refuted the studies, and the studies have "
                  "not refuted you: these are two readings, and your passages were of "
                  "standard difficulty, not the difficult text on which Hardyck and "
                  "Petrinovich found the cost."),
            ("p", "Look at the rates as well as the effective rates. If your counting "
                  "reading was a little faster, that is the experience the advice is "
                  "built on, and it is real. The question the effective rate "
                  "asks is whether what you understood kept up with the speed."),
            ("p", "Next, the tradition's other way past the voice: show the words one "
                  "at a time, faster than any voice could say them. One Word at a Time "
                  "starts with the drill."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P27"], PASSAGES["P28"]],
            "a": {"label": "Reading normally"},
            "b": {"label": "Counting under your breath", "suppress": True},
            "preset": "typical",
            "presets": [
                {"id": "typical", "label": "245 normally, 262 while counting",
                 "wordsA": 392, "secondsA": 96, "correctA": 6, "totalA": 6,
                 "wordsB": 393, "secondsB": 90, "correctB": 4, "totalB": 6,
                 "expect": {"drErrA": "245 wpm", "drErrB": "≈ 174.7 wpm", "drErrDiff": "≈ −70.3 wpm"}},
                {"id": "easy-text", "label": "260 normally, 266 while counting",
                 "wordsA": 403, "secondsA": 93, "correctA": 6, "totalA": 6,
                 "wordsB": 399, "secondsB": 90, "correctB": 5, "totalB": 6,
                 "expect": {"drErrA": "260 wpm", "drErrB": "≈ 221.7 wpm", "drErrDiff": "≈ −38.3 wpm"}},
            ],
            "panel_title": "Reading with the voice busy",
            "panel_intro": (
                "Your measurement: two timed readings of a matched pair, each with six "
                "questions, the second while counting under your breath. The tiles "
                "give each reading's rate, comprehension and effective rate, and the "
                "difference between the effective rates, counting minus normal."
            ),
        }),
        "steps_title": "Testing suppression on your reading",
        "steps_intro": (
            "To run the test again, you need two fresh passages matched for length and "
            "difficulty, and the discipline to keep counting."
        ),
        "steps": [
            ("Choose a matched pair you have not read",
             "Two passages within a few dozen words and about one grade of each "
             "other, with six questions each that cannot be answered without reading."),
            ("Read the first normally",
             "At your usual pace, timed, then its questions with the text out of "
             "sight."),
            ("Read the second while counting",
             "&ldquo;One-two-three&rdquo; under your breath, steadily, from the first "
             "word to the last. If you stop counting at any point, finish the reading "
             "but mark it as lapsed."),
            ("Compare the effective rates, and void a lapse",
             "Rate × correct / 6 for each, then counting minus normal. A lapsed reading "
             "does not count, and a one-question difference is not a result."),
            DAILY,
        ],
        "worked": {
            "title": "The typical reader",
            "intro": [
                "Normally: 245 wpm with six of six right. While counting: 262 wpm with "
                "four of six.",
            ],
            "lines": [
                "A: 245 × 6/6 = 245 words a minute",
                "B: 262 × 4/6 ≈ 174.7 words a minute",
                "B − A ≈ −70.3 words a minute",
            ],
            "after": [
                "The counting reading was 17 words a minute faster and two questions "
                "worse, and its effective rate is lower by about 70. Exactly, "
                "262 × 4/6 = 524/3, and 524/3 − 245 = −211/3.",
            ],
        },
        "quiz_title": "Reading a suppression result",
        "quiz": [
            {"q": "Normally a reader reads at 250 wpm with five of six right; while "
                  "counting, at 270 wpm with four of six. What is the difference in "
                  "effective rate, counting minus normal?",
             "a": ["+20 wpm", "≈ −28.3 wpm", "≈ −16.7 wpm", "−45 wpm"],
             "c": 1,
             "why": "Normal: 250 × 5/6 ≈ 208.3. Counting: 270 × 4/6 = 180. "
                    "180 − 208.3 ≈ −28.3. +20 is the difference in rate alone, and "
                    "−16.7 is the difference in comprehension points."},
            {"q": "After the counting reading you leave &ldquo;I kept counting the whole "
                  "way&rdquo; unticked, because you stopped for most of a paragraph. "
                  "What should you do with the result?",
             "a": ["Count it, since you counted for most of the passage",
                   "Use its rate but not its comprehension",
                   "Treat the comparison as void, and repeat it on a fresh pair another "
                   "day",
                   "Subtract one question from it to allow for the lapse"],
             "c": 2,
             "why": "While you were not counting, you were reading normally, so the "
                    "second reading is partly a normal reading of a different passage. "
                    "No adjustment recovers what the suppressed part would have been."},
            {"q": "Why could counting lower comprehension even if the inner voice did "
                  "no useful work at all?",
             "a": ["Counting is a second task that takes attention",
                   "Counting makes the passage longer",
                   "The questions after a counting reading are harder",
                   "Counting slows the reading below 183 wpm"],
             "c": 0,
             "why": "Suppression always adds a second task. A cost could come from "
                    "doing two things at once rather than from losing the voice, which "
                    "is one reason the studies are read with care."},
            {"q": "What did Hardyck and Petrinovich (1970) find when readers learned to "
                  "keep their speech muscles quiet?",
             "a": ["Comprehension fell on both easy and difficult text",
                   "Reading rate doubled with no loss",
                   "Nothing changed on either text",
                   "Comprehension of the difficult text fell; the easy text held up"],
             "c": 3,
             "why": "The cost appeared on difficult text. On easy text comprehension "
                    "held up, which is why an easy pair of passages could show little "
                    "or no cost."},
        ],
        "mistakes": [
            ("Eliminating subvocalisation is the key to speed reading",
             "In the studies that suppressed inner speech, comprehension of difficult "
             "text fell while easy text held up (Hardyck and Petrinovich, by feedback "
             "from the speech muscles), and counting aloud impaired comprehension of "
             "passages (Slowiaczek and Clifton). The studies are few and small, and "
             "suppression also adds a second task, but none of them found the voice "
             "to be a cost-free brake."),
            ("Counting a reading where the counting lapsed",
             "A reading that was suppressed for half its length is half a normal "
             "reading. It cannot be compared with anything as a suppressed reading. "
             "The tick is there so that the log knows which readings to trust."),
            ("Reading the rate and not the effective rate",
             "A counting reading can be a little faster. A rate that rose by 17 "
             "words a minute while two questions were lost is a lower effective rate, "
             "and the effective rate is the one that counts what you understood."),
        ],
        "standard": (
            "Finish when you can score a suppression comparison and say when it does not count.",
            "Given two readings with their rates and questions right, compute both "
            "effective rates and the difference, counting minus normal, to one "
            "decimal; and say in a sentence why a reading in which the counting lapsed "
            "does not count. Both, right, pass."
        ),
        "note": (
            "Two readings, two passages, one order: the passages are matched but not "
            "identical, and which came first moves the result, which is why the lab "
            "alternates the order between visits. The studies cited used their own "
            "texts and small samples; the drill copies Slowiaczek and "
            "Clifton's counting, not Hardyck and Petrinovich's muscle feedback."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "one-word-at-a-time",
        "title": "One Word at a Time",
        "module": "Flashing words",
        "one_line": "Read a story flashed one word at a time at your usual rate, and compare what you understood with your baselines.",
        "summary": (
            "Speed-reading apps show one word at a time in a fixed spot, so the eyes "
            "never move. Read a story that way at your own baseline rate, compute how "
            "long each word is on screen, and compare your comprehension with your "
            "baseline readings."
        ),
        "key": [
            "time per word = 60,000 ms / rate",
            "250 words a minute: 240 ms a word",
            "500 words a minute: 120 ms a word",
            "saccades: 30 of 255 ms in the model",
        ],
        "key_label": "The stream in four lines",
        "concepts_intro": (
            "The question is what happens to your understanding when the words come "
            "to your eyes instead of your eyes going to the words."
        ),
        "concepts": [
            ("Every word gets the same time",
             "At a rate of r words a minute, each word is shown for 60,000 / r "
             "milliseconds, long or short, easy or hard. The stream ends when the "
             "last word has been shown, and the total time is fixed by the rate."),
            ("Your baselines are the control",
             "Set the stream to the median of your baseline readings, so that the rate "
             "is the one you read at anyway and only the display has changed. Then "
             "compare this reading's comprehension with theirs."),
            ("What the display removes",
             "In the stream your eyes do not move along a line, the next word is not "
             "visible before it arrives, and a word that has gone cannot be looked at "
             "again. The drill measures all three changes together."),
        ],
        "read_title": "What the stream saves and what it costs",
        "read_intro": (
            "The arithmetic of a flashed word, the share of reading time eye "
            "movements take, and what the studies of the apps found."
        ),
        "body": [
            ("p", "Do the drill before you read on. Look up the median of your baseline "
                  "readings in your log, type it into the box labelled Target rate, wpm "
                  "(250 if you have no baselines yet), and press Start. <em>The Slow Clock</em> will "
                  "appear one word at a time in the box, each for the same fraction of "
                  "a second, and the questions follow when the stream ends."),
            ("p", "Many readers find the first few lines strange and then settle into "
                  "the rhythm, and the stream can feel effortless. The questions are "
                  "where to look next: compare the share you got right with the "
                  "comprehension of your baseline readings, which were at about the "
                  "same rate with your eyes free."),
            ("p", "The time per word is a division. A minute is 60,000 milliseconds, "
                  "so at 250 words a minute each word is shown for 60,000 / 250 = 240 "
                  "milliseconds. The preset <strong>at-baseline</strong> is a reader "
                  "whose baseline median is 250: the 403 words of the story took 96.72 "
                  "seconds, the tiles read 240 ms a word and 250 wpm, and with five "
                  "questions of six right the effective rate is about 208.3 wpm."),
            ("p", "The lab prints two times per word: the one requested, from the rate "
                  "you typed, and the one measured, from how long the stream actually "
                  "took. A browser busy with something else can show a word a few "
                  "milliseconds late; when the two differ, the measured one is the "
                  "rate you actually read at."),
            ("p", "The preset <strong>at-500</strong> doubles the rate: 120 ms a word, "
                  "48.36 seconds for the story, three questions of six right. Its "
                  "effective rate is 500 × 3/6 = 250 wpm, higher than the at-baseline "
                  "reader's 208.3, because the product rewards speed; and half the "
                  "questions are gone. Whether a reading that keeps half of a story is "
                  "good enough depends on what you are reading it for, and Skimming, "
                  "Scanning and Previewing is about exactly that choice."),
            ("p", "The preset <strong>at-600</strong> is the fastest the drill will run: "
                  "100 ms a word, the story in 40.3 seconds, two questions right, an "
                  "effective rate of 200 wpm. Above 600 the drill refuses, because the "
                  "display becomes a flicker rather than something to read."),
            ("p", "Why does removing eye movements save so little? Take the eye model "
                  "from How the Eyes Read: a fixation of 225 ms and a saccade of 30 ms. "
                  "The saccades are 30 of every 255 milliseconds, about 11.8% of the "
                  "time. Nearly all reading time is spent in the fixations, identifying "
                  "words, and a stream still needs that time for every word. Removing "
                  "every saccade would save about a tenth."),
            ("p", "That is not to say the stream is unreadable. Potter (1984) showed "
                  "that single sentences can be understood in a stream at about twelve "
                  "words a second, around 720 words a minute. The costs come with "
                  "passages, with memory, and with having no way back. When Benedetto "
                  "and colleagues (2015) tested Spritz, one of the apps that made the "
                  "display famous in 2014, literal comprehension was lower and visual "
                  "fatigue higher, with readers blinking less; Acklin and Papesh (2017) "
                  "found that the apps lowered comprehension at speed compared with "
                  "normal reading."),
            ("p", "So read your result as a comparison with yourself. If your "
                  "comprehension in the stream matched your baselines, the stream at "
                  "your own rate cost you little on this story, which fits Potter's "
                  "sentences. If it fell, you have felt what the app studies measured. "
                  "Either way it is one reading of one passage, and one question is "
                  "about 16.7 points."),
            ("p", "The tradition's answer to the stream's costs is to group the words. "
                  "Reading in Phrases shows a passage one meaningful phrase at a time, "
                  "against a matched passage one word at a time, at the same rate."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "single",
            "passage": PASSAGES["P29"],
            "display": "rsvp",
            "target": 250,
            "kind": "condition",
            "preset": "at-baseline",
            "presets": [
                {"id": "at-baseline", "label": "250 wpm, 5 of 6",
                 "words": 403, "seconds": "96.72", "correct": 5, "total": 6,
                 "target": 250, "chunk": 1, "expect": {"drWordMs": "240 ms", "drWpm": "250 wpm", "drErr": "≈ 208.3 wpm"}},
                {"id": "at-500", "label": "500 wpm, 3 of 6",
                 "words": 403, "seconds": "48.36", "correct": 3, "total": 6,
                 "target": 500, "chunk": 1, "expect": {"drWordMs": "120 ms", "drWpm": "500 wpm", "drErr": "250 wpm"}},
                {"id": "at-600", "label": "600 wpm, 2 of 6",
                 "words": 403, "seconds": "40.3", "correct": 2, "total": 6,
                 "target": 600, "chunk": 1, "expect": {"drWordMs": "100 ms", "drWpm": "600 wpm", "drErr": "200 wpm"}},
            ],
            "panel_title": "One word at a time",
            "panel_intro": (
                "Your measurement: one streamed reading at the rate in the target box, "
                "then six questions. The tiles give the time each word was requested "
                "and the time it was actually shown, the rate, comprehension and "
                "effective rate. Put your baseline median in the target box before you "
                "press Start: type it, or press Use my baseline median."
            ),
        }),
        "steps_title": "Trying the stream on another day",
        "steps_intro": (
            "The stream is worth trying more than once, on fresh text and at your own "
            "rate, before you decide what it does for you."
        ),
        "steps": [
            ("Find your baseline median",
             "In your log, the middle of your baseline rates. That is the rate to "
             "stream at, so that the display is the only change."),
            ("Stream a fresh passage at that rate",
             "One you have not read, with questions written by someone else. Keep "
             "your eyes on the box and do not try to read ahead."),
            ("Answer the questions with nothing on screen",
             "Then compare the share right with your baseline readings' comprehension."),
            ("Compare the requested and measured times",
             "If the measured time per word is longer, your rate was lower than you "
             "asked for; use the measured figure."),
            DAILY,
        ],
        "worked": {
            "title": "A word at 250, and the saccades' share",
            "intro": [
                "A reader streams at their baseline median of 250 words a minute. The "
                "eye model from How the Eyes Read gives a fixation 225 ms and a saccade "
                "30 ms.",
            ],
            "lines": [
                "time per word = 60,000 / 250 = 240 ms",
                "saccade share = 30 / 255 ≈ 11.8%",
            ],
            "after": [
                "Each word is on screen for 240 ms. In ordinary reading about a "
                "tenth of the time goes to moving the eyes, so a display that removes "
                "the movements removes about that much time and no more; the rest is "
                "the time it takes to identify the words, which the stream still "
                "needs.",
            ],
        },
        "quiz_title": "Time on screen",
        "quiz": [
            {"q": "A stream runs at 400 words a minute. How long is each word shown?",
             "a": ["240 ms", "150 ms", "6.7 ms", "2.5 ms"],
             "c": 1,
             "why": "60,000 / 400 = 150 milliseconds. 240 ms is the time at 250 wpm; "
                    "6.7 is 400 / 60, words per second; 2.5 is 1,000 / 400, a second "
                    "taken for a minute."},
            {"q": "In the eye model, a fixation is 225 ms and a saccade 30 ms. Why does "
                  "a stream that removes every saccade save so little time?",
             "a": ["Saccades are about a tenth of the time; identifying the words "
                   "takes the rest, and the stream still needs it",
                   "The stream adds a pause between words",
                   "Saccades are faster in a stream",
                   "The stream shows each word twice"],
             "c": 0,
             "why": "30 / 255 ≈ 11.8% of the time is saccades. The fixations, in which "
                    "the words are identified, are the other 88%, and a word flashed in "
                    "a box still has to be identified."},
            {"q": "The tiles read 240 ms requested and 250 ms measured. What happened?",
             "a": ["You read faster than 250 wpm",
                   "The questions took longer than expected",
                   "The browser showed words a little late, so the rate you actually "
                   "read at was a little below 250 wpm",
                   "The passage had more words than the box said"],
             "c": 2,
             "why": "The measured time per word is the stream's real duration divided "
                    "by its words. 250 ms a word is 60,000 / 250 = 240 wpm, a little "
                    "below the 250 you asked for."},
            {"q": "What did Potter (1984) find about streams of single words?",
             "a": ["Nobody can read a stream faster than 300 words a minute",
                   "Streams are understood better than normal reading at any rate",
                   "Streams cause headaches above 400 words a minute",
                   "Single sentences can be understood at about twelve words a second"],
             "c": 3,
             "why": "Potter's finding was about sentences, at around 720 words a "
                    "minute. The costs found later were with passages, memory, and no "
                    "way back, which is why a stream can feel fine and still cost "
                    "comprehension."},
        ],
        "mistakes": [
            ("Removing eye movements removes their time, so a flashed stream is free speed",
             "Saccades are about a tenth of reading time: 30 of 255 ms in the model. "
             "Single sentences can be understood in a stream at about twelve words a "
             "second (Potter 1984), but the costs come with passages, with memory and "
             "with no way back: lower literal comprehension and more visual fatigue "
             "with Spritz (Benedetto and colleagues, 2015), lower comprehension at "
             "speed with the apps (Acklin and Papesh, 2017)."),
            ("Judging the stream by how it felt",
             "A stream sets the pace for you, so it rarely feels like falling behind. "
             "The questions are the measurement; a smooth-feeling reading with three "
             "questions of six right lost half the story."),
            ("Streaming at a guessed rate",
             "If the target is not your baseline median, the reading changes both the "
             "display and the pace, and a change in comprehension cannot be put down "
             "to either. Set the rate from your log."),
        ],
        "standard": (
            "Finish when you can time a flashed word and say why the saving is small.",
            "Given a rate, compute the milliseconds each word is shown; and explain in "
            "two sentences, with the model's 30 of 255 ms, why removing eye movements "
            "saves little time. Both pass."
        ),
        "note": (
            "One streamed reading of one story, compared with baselines on other "
            "passages: the passages differ, and so does the day. The app studies used "
            "their own texts, rates and questions; the drill copies the "
            "display, not their procedure."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "reading-in-phrases",
        "title": "Reading in Phrases",
        "module": "Flashing words",
        "one_line": "Stream one passage a word at a time and a matched one a phrase at a time, at the same rate, and compare comprehension.",
        "summary": (
            "Speed-reading courses teach reading in phrases. Stream one passage word "
            "by word and a matched one phrase by phrase at the same rate, compute how "
            "long a phrase is shown, and see whether grouping changes what you "
            "understood."
        ),
        "key": [
            "time per phrase = words × 60,000 / rate",
            "4 words at 250: 960 ms",
            "same rate, same stream, new grouping",
            "one question ≈ 16.7 points",
        ],
        "key_label": "Grouping in four lines",
        "concepts_intro": (
            "Reading in phrases is usually sold as seeing more words in one glance. "
            "The drill separates that claim from a smaller one: that grouping helps."
        ),
        "concepts": [
            ("A phrase is a unit of meaning",
             "&ldquo;Into the top layer&rdquo;, &ldquo;of the soil&rdquo;: a few words "
             "that belong together. The phrase passage is marked into such groups, two "
             "to five words each, and the stream shows one group at a time."),
            ("The rate is the same",
             "A phrase stays on screen for its words' time at the rate, so both "
             "streams run at the same words a minute; only the grouping differs."),
            ("Both streams forbid looking back",
             "Neither display lets you return to a word, so the pair compares grouped "
             "with ungrouped text and nothing else about the stream."),
        ],
        "read_title": "What grouping can and cannot do",
        "read_intro": (
            "The arithmetic of a phrase on screen, two presets, and why phrase "
            "reading on a page is a different thing."
        ),
        "body": [
            ("p", "The tradition's advice is to read in &ldquo;thought units&rdquo;, "
                  "three or four words at a time, with fewer stops along a line. The "
                  "drill tests a narrower version: two streams at one rate, the "
                  "first, <em>Building a Campfire</em>, one word at a time, the second, "
                  "<em>Planting a Young Tree</em>, one marked phrase at a time. Put "
                  "your baseline median into both boxes labelled Target rate, wpm, "
                  "(A) and (B), before you start: type it, or press “Use my "
                  "baseline median”."),
            ("p", "A phrase stays on screen as long as its words would at that "
                  "rate. At 250 words a minute a four-word phrase is shown for "
                  "4 × 60,000 / 250 = 960 milliseconds, and a two-word phrase for 480. "
                  "The tree passage has 438 words in 127 phrases, about 3.4 words a "
                  "phrase, and the phrase tile gives the mean: 438 × 60,000 / "
                  "(250 × 127), about 827.7 ms."),
            ("p", "The preset <strong>grouping-helps</strong> is a reader for whom it "
                  "did: 459 words word by word in 110.16 seconds, which is 250 wpm, "
                  "with three questions of six right, an effective rate of 125; then "
                  "438 words phrase by phrase in 105.12 seconds, also 250 wpm, with five "
                  "right, an effective rate of about 208.3. Same rate, two more "
                  "questions, and a difference of about +83.3 wpm."),
            ("p", "The preset <strong>no-difference</strong> is a reader for whom it "
                  "did not: four of six right in both streams, an effective rate of "
                  "about 166.7 each, and a difference of 0. One question either way, "
                  "about 16.7 points, is not a result."),
            ("p", "What the pair isolates is the grouping. Both streams run at one "
                  "rate in the same box, and neither lets you look back, so a "
                  "difference is not about speed or regressions. It can still be about "
                  "the passages, matched but not the same, and the order."),
            ("p", "What it cannot show is that phrase reading speeds up ordinary "
                  "reading. On a page, nobody marks the phrases for you, and the claim "
                  "usually made for phrase reading is about the eye: that a trained "
                  "reader sees a whole phrase in one fixation. In normal reading the "
                  "eyes still fixate most content words (Rayner and colleagues, 2016), "
                  "and How the Eyes Read showed how few letters a fixation identifies. "
                  "Chunking groups words by meaning; it does not widen the glance."),
            ("p", "So if grouping helped you, what helped may be the grouping itself, "
                  "a stream that hands you the words in meaningful pieces: a finding "
                  "about streams, not about the page. If your result went the other "
                  "way, you have not refuted the review, and it has not refuted you: "
                  "this is one pair of readings."),
            ("p", "Both streams here took away the second look. Flashing Words Without "
                  "Looking Back measures what that costs, against a pacer that lets "
                  "your eyes go back."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P19"], PASSAGES["P20"]],
            "a": {"label": "One word at a time", "display": "rsvp", "target": 250},
            "b": {"label": "One phrase at a time", "display": "phrases", "target": 250},
            "preset": "grouping-helps",
            "presets": [
                {"id": "grouping-helps", "label": "3 of 6 by word, 5 of 6 by phrase",
                 "wordsA": 459, "secondsA": "110.16", "correctA": 3, "totalA": 6,
                 "targetA": 250, "chunkA": 1,
                 "wordsB": 438, "secondsB": "105.12", "correctB": 5, "totalB": 6,
                 "targetB": 250, "phrasesB": 127,
                 "expect": {"drErrA": "125 wpm", "drErrB": "≈ 208.3 wpm", "drErrDiff": "≈ +83.3 wpm", "drPhraseMs": "≈ 827.7 ms"}},
                {"id": "no-difference", "label": "4 of 6 both ways",
                 "wordsA": 459, "secondsA": "110.16", "correctA": 4, "totalA": 6,
                 "targetA": 250, "chunkA": 1,
                 "wordsB": 438, "secondsB": "105.12", "correctB": 4, "totalB": 6,
                 "targetB": 250, "phrasesB": 127,
                 "expect": {"drErrA": "≈ 166.7 wpm", "drErrB": "≈ 166.7 wpm", "drErrDiff": "0 wpm", "drPhraseMs": "≈ 827.7 ms"}},
            ],
            "panel_title": "Words or phrases, at one rate",
            "panel_intro": (
                "Your measurement: two streamed readings of a matched pair at the same "
                "rate, each with six questions. Put your baseline median into both "
                "target boxes (Use my baseline median fills them). The tiles add the time per word of the first stream and "
                "the mean time per phrase of the second."
            ),
        }),
        "steps_title": "Comparing word and phrase streams",
        "steps_intro": (
            "To repeat the comparison, keep the rate fixed and change only the "
            "grouping."
        ),
        "steps": [
            ("Set one rate for both streams",
             "Your baseline median, typed into both target boxes, so that neither "
             "stream is faster than the other."),
            ("Stream a fresh passage one word at a time",
             "Eyes on the box, then its questions with nothing on screen."),
            ("Stream a matched passage one phrase at a time",
             "The same rate and box, the words grouped; then its questions."),
            ("Compare the effective rates",
             "Rate × correct / 6 for each. A difference of one question is not a "
             "result; a pattern over several pairs on different days is."),
            DAILY,
        ],
        "worked": {
            "title": "A phrase at 250",
            "intro": [
                "A four-word phrase, and the whole of the tree passage, streamed at 250 "
                "words a minute.",
            ],
            "lines": [
                "4 × 60,000 / 250 = 960 ms",
                "438 × 60,000 / (250 × 127) ≈ 827.7 ms",
            ],
            "after": [
                "A phrase gets exactly the time its words would get one by one, so "
                "both streams take the same time for the same number of words.",
            ],
        },
        "quiz_title": "Phrases on screen",
        "quiz": [
            {"q": "At 300 words a minute, how long is a three-word phrase shown?",
             "a": ["200 ms", "300 ms", "900 ms", "600 ms"],
             "c": 3,
             "why": "3 × 60,000 / 300 = 600 milliseconds: three words at 200 ms each. "
                    "200 ms is one word's time."},
            {"q": "Both streams run at the same rate and neither lets you look back. "
                  "What, then, does a difference between them mostly reflect?",
             "a": ["The grouping, along with the different passages and the order",
                   "The reader's speed",
                   "How often the reader looked back",
                   "The width of the reader's perceptual span"],
             "c": 0,
             "why": "Rate and regressions are the same in both, so they cannot explain "
                    "a difference. What differs is the grouping, and also the passage "
                    "and which came first, which is why one pair is not a verdict."},
            {"q": "A course says phrase reading lets a trained reader see a whole phrase "
                  "in one fixation. What does the evidence say about normal reading?",
             "a": ["Trained readers fixate once per phrase",
                   "The eyes still fixate most content words",
                   "Fixations disappear with practice",
                   "Phrases are identified before the words in them"],
             "c": 1,
             "why": "In normal reading the eyes land on most content words. Grouping "
                    "by meaning can help a stream; it does not widen the glance."},
        ],
        "mistakes": [
            ("Phrase reading means seeing several words in one fixation",
             "Chunking groups words by meaning. In normal reading the eyes still "
             "fixate most content words (Rayner and colleagues, 2016), and words are "
             "identified only about 7–8 letters to the right of a fixation (Rayner "
             "1998). What may help is the grouping, which this drill isolates."),
            ("Comparing streams at different rates",
             "If one stream ran faster, a difference in comprehension could be the "
             "rate. Type the same target into both boxes."),
            ("Carrying a stream result to the page",
             "The phrase stream did the grouping for you. On a page nobody marks the "
             "phrases, and a gain in the stream is a finding about streams."),
        ],
        "standard": (
            "Finish when you can time a phrase and say what the comparison isolates.",
            "Given a phrase's words and a rate, compute the milliseconds it is shown; "
            "and say in two sentences what the word-against-phrase comparison isolates "
            "(the grouping, with rate and regressions held the same) and what it does "
            "not (the passages, the order, and anything about reading a page). Both "
            "pass."
        ),
        "note": (
            "Two streams, two passages, one order: the campfire and tree passages are "
            "matched for length and difficulty but are different texts, and the lab "
            "alternates which you read first between visits. Another reader might "
            "mark the phrases differently."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "rsvp-without-looking-back",
        "title": "Flashing Words Without Looking Back",
        "module": "Flashing words",
        "one_line": "Read one story behind a pacer and a matched one in a stream at the same rate, and see what having no way back costs.",
        "summary": (
            "A stream never lets you go back to a word. Read one story with the pacer "
            "and a matched story in a stream at the same rate, each with one sentence "
            "that is easy to misread the first time, and compare comprehension, with "
            "an eye on the question about that sentence."
        ),
        "key": [
            "same rate: pacer against stream",
            "pacer: you can still look back",
            "stream: a word that has gone is gone",
            "300 × 4/6 = 200 against 300",
        ],
        "key_label": "The second look in four lines",
        "concepts_intro": (
            "Regressions, the looks back, are ten to fifteen per cent of the eye's "
            "movements. The stream takes them all away; this lesson measures what "
            "goes with them."
        ),
        "concepts": [
            ("The pacer keeps the page",
             "The pacer sets the pace, but the whole passage stays on screen. Your "
             "eyes can go back to a word in the line you are on, or above it, whenever "
             "they need to."),
            ("The stream keeps nothing",
             "In the stream each word replaces the last. A sentence you misread "
             "cannot be checked, and the next words arrive whether you have repaired "
             "it or not."),
            ("A sentence that needs a second look",
             "A garden-path sentence leads you to one reading and then turns out to "
             "mean another, as in &ldquo;The dog walked past the gate barked&rdquo;. "
             "Each passage has one, and one question depends on reading it right."),
        ],
        "read_title": "What going back is for",
        "read_intro": (
            "Two displays at one rate, two presets, and what Schotter, Tran and Rayner "
            "found when going back was made useless."
        ),
        "body": [
            ("p", "Both readings in the lab run at one rate: put your baseline median "
                  "into both boxes labelled Target rate, wpm (“Use my baseline "
                  "median” does it), or 300 to match the presets. "
                  "<em>The Harvest Supper</em> is read with the pacer, a highlight "
                  "moving line by line with the whole story on screen. <em>The Red "
                  "Flag</em> is read in the stream, one word at a time. Each has six "
                  "questions."),
            ("p", "Each story also contains one sentence built to be misread on the "
                  "first pass, of the kind linguists call a garden path. In &ldquo;The "
                  "dog walked past the gate barked&rdquo; you take &ldquo;walked&rdquo; "
                  "as what the dog did, until &ldquo;barked&rdquo; arrives and the "
                  "sentence only makes sense as &ldquo;the dog that was walked past the "
                  "gate barked&rdquo;. On a page, you can repair a sentence like "
                  "that with a glance back. One question on each story depends on "
                  "getting its sentence right."),
            ("p", "The preset <strong>stream-costs</strong> is a reader at 300 words a "
                  "minute both ways: 391 words with the pacer in 78.2 seconds, six of "
                  "six right, an effective rate of 300; and 403 words in the stream in "
                  "80.6 seconds, four of six right, an effective rate of 300 × 4/6 = "
                  "200. The difference is −100 wpm, two questions, at the same rate."),
            ("p", "The preset <strong>even</strong> is a reader with five of six right "
                  "both ways, effective rates of 250 and 250, and no difference. That "
                  "is a real possibility: two stories are not a laboratory, and a "
                  "reader who misreads neither garden path, or both, will see no "
                  "gap."),
            ("p", "Now look at your own answers, which the lab shows after Score, and "
                  "find the question about the misleading sentence in each story. If "
                  "you got it right with the pacer and wrong in the stream, you may "
                  "remember the moment: the sentence stopped making sense and the next "
                  "words were already coming."),
            ("p", "Schotter, Tran and Rayner (2014) tested what going back is for. As "
                  "people read sentences, each word was replaced by x's as soon as the "
                  "eyes left it, so that a reader could still look back but would find "
                  "nothing there. Comprehension was lower with the mask, and not only "
                  "for the ambiguous sentences: it was lower for ordinary sentences "
                  "too. In normal reading, by contrast, sentences read with and "
                  "without regressions were understood about equally well, which is "
                  "what you would see if readers go back when they need to."),
            ("p", "So the garden path is not where the cost is confined; it is where "
                  "you can feel it. A stream removes every chance to repair, including "
                  "the small, unnoticed ones, and Acklin and Papesh (2017) found the "
                  "apps that use it lowered comprehension at speed. The stream did "
                  "remove the look back, and the look back was doing work."),
            ("p", "If your result goes the other way, with the stream as good as the "
                  "pacer or better, you have not refuted Schotter, Tran and Rayner, and "
                  "their study has not refuted you: you read two stories once each, "
                  "and their readers read many sentences under careful control."),
            ("p", "The last lesson of the course takes the claims made for fast "
                  "reading and tests them with arithmetic you already have. Testing a "
                  "Speed Claim is next."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P30"], PASSAGES["P31"]],
            "a": {"label": "With the pacer", "display": "pacer", "target": 300},
            "b": {"label": "In the stream", "display": "rsvp", "target": 300},
            "preset": "stream-costs",
            "presets": [
                {"id": "stream-costs", "label": "6 of 6 with the pacer, 4 of 6 streamed",
                 "wordsA": 391, "secondsA": "78.2", "correctA": 6, "totalA": 6,
                 "targetA": 300,
                 "wordsB": 403, "secondsB": "80.6", "correctB": 4, "totalB": 6,
                 "targetB": 300, "chunkB": 1,
                 "expect": {"drErrA": "300 wpm", "drErrB": "200 wpm", "drErrDiff": "−100 wpm"}},
                {"id": "even", "label": "5 of 6 both ways",
                 "wordsA": 391, "secondsA": "78.2", "correctA": 5, "totalA": 6,
                 "targetA": 300,
                 "wordsB": 403, "secondsB": "80.6", "correctB": 5, "totalB": 6,
                 "targetB": 300, "chunkB": 1,
                 "expect": {"drErrA": "250 wpm", "drErrB": "250 wpm", "drErrDiff": "0 wpm"}},
            ],
            "panel_title": "The pacer against the stream",
            "panel_intro": (
                "Your measurement: two readings of a matched pair at one rate, the "
                "first behind a pacer that leaves the page on screen, the second in a "
                "stream that does not. Type the same target into both boxes, or press "
                "Use my baseline median. Each "
                "story has one sentence that is easy to misread; after Score, find its "
                "question among your answers."
            ),
        }),
        "steps_title": "Testing the second look",
        "steps_intro": (
            "To repeat the comparison, hold the rate and change only whether you can "
            "look back."
        ),
        "steps": [
            ("Set one rate for both readings",
             "Your baseline median, typed into both target boxes."),
            ("Read a fresh passage behind the pacer",
             "Keep up with the highlight, and let your eyes go back when a sentence "
             "needs it. Then its questions."),
            ("Stream a matched passage at the same rate",
             "One word at a time, eyes on the box, then its questions."),
            ("Compare the effective rates and the hard question",
             "Rate × correct / 6 for each, and whether the question about the "
             "misleading sentence went differently."),
            DAILY,
        ],
        "worked": {
            "title": "The stream-costs reader",
            "intro": [
                "Both readings at 300 words a minute: six of six with the pacer, four "
                "of six in the stream.",
            ],
            "lines": [
                "pacer: 300 × 6/6 = 300 words a minute",
                "stream: 300 × 4/6 = 200 words a minute",
                "difference = 200 − 300 = −100",
            ],
            "after": [
                "The rate was the same, so the whole difference is in what was "
                "understood: two questions, a third of the effective rate.",
            ],
        },
        "quiz_title": "What the stream takes away",
        "quiz": [
            {"q": "Both readings run at 300 wpm. With the pacer the reader gets five of "
                  "six; in the stream, three of six. What is the difference in effective "
                  "rate, stream minus pacer?",
             "a": ["−100 wpm", "−2 questions", "−50 wpm", "0 wpm, since the rates are "
                   "equal"],
             "c": 0,
             "why": "300 × 5/6 = 250 and 300 × 3/6 = 150, so 150 − 250 = −100 wpm. "
                    "The rates are equal, which is why the whole difference is in "
                    "comprehension."},
            {"q": "What did Schotter, Tran and Rayner (2014) do to make going back "
                  "useless?",
             "a": ["They told readers not to look back",
                   "They streamed the sentences one word at a time",
                   "They replaced each word with x's as soon as the eyes left it",
                   "They removed the ambiguous sentences"],
             "c": 2,
             "why": "Readers could still move their eyes back, but the words they had "
                    "read were masked. Comprehension was lower with the mask."},
            {"q": "In that study, which sentences were understood less well when going "
                  "back was made useless?",
             "a": ["Only the ambiguous ones",
                   "Ambiguous and ordinary sentences alike",
                   "Only the ordinary ones",
                   "Neither; only reading time changed"],
             "c": 1,
             "why": "The cost appeared for unambiguous sentences as well as ambiguous "
                    "ones. The garden path is where you can feel the cost, not the only "
                    "place it is."},
            {"q": "Why can the pacer reading serve as the control here?",
             "a": ["It is slower than the stream",
                   "It has easier questions",
                   "It shows one phrase at a time",
                   "It runs at the same rate but leaves the whole passage on screen"],
             "c": 3,
             "why": "Holding the rate equal and keeping the page visible means the "
                    "main difference between the readings is whether your eyes can go "
                    "back."},
        ],
        "mistakes": [
            ("RSVP is reading with the waste removed",
             "The stream removes regressions too, and the looks back are not waste. "
             "Schotter, Tran and Rayner found that making them useless lowered "
             "comprehension for ordinary sentences as well as ambiguous ones; the "
             "garden path is just where you can feel it."),
            ("Thinking every look back is a mistake",
             "In normal reading, sentences read with and without regressions were "
             "understood about equally well. Readers tend to go back when they need "
             "to, and that is the repair the stream cannot make."),
            ("Reading the garden-path question alone",
             "One question either way is about 16.7 points and not a result. The "
             "effective rates over all six questions are the comparison; the "
             "misleading sentence is where to look for the reason."),
        ],
        "standard": (
            "Finish when you can say what the garden-path question tests.",
            "Say in two sentences what the garden-path question tests (whether you "
            "repaired a sentence that misled you on first reading) and why the stream "
            "cannot let you repair it (the words have gone, and the next ones keep "
            "coming). Then, given both readings' figures, compute the two effective "
            "rates. All three pass."
        ),
        "note": (
            "Two passages, one order: the stories are matched but not identical, the "
            "two misleading sentences are not equally misleading for every reader, "
            "and which display came first matters, which is why the lab alternates the "
            "order between visits. The pacer's look back is free; Schotter, Tran and "
            "Rayner's mask left the eyes free and hid the words, a finer test than "
            "this one."
        ),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "testing-a-speed-claim",
        "title": "Testing a Speed Claim",
        "module": "Flashing words",
        "one_line": "Test a claimed reading speed with three computations, and name the test that would settle it.",
        "summary": (
            "A claim of 1,500 words a minute can be checked before anyone is timed. "
            "Compute the characters each glance would have to take in, the effective "
            "rate at a stated comprehension, and the time a book would take; then name "
            "the evidence that would settle the claim."
        ),
        "key": [
            "rate = words × 60 / seconds",
            "glance = rate × 6 × 255 / 60,000",
            "effective rate = rate × comprehension",
            "book time = words / rate, in minutes",
        ],
        "key_label": "Three computations",
        "concepts_intro": (
            "Every claim about reading speed is a number, and a number can be "
            "followed to what it would require."
        ),
        "concepts": [
            ("What each glance would need",
             "At an average fixation of 225 ms and saccade of 30 ms, six characters to "
             "a word and no looking back, a rate of r words a minute needs each "
             "fixation to advance r × 6 × 255 / 60,000 characters. Words are "
             "identified within about 8 characters of the centre, and the perceptual "
             "span reaches about 15."),
            ("What it would mean understood",
             "A rate with no comprehension attached is a page-turning speed. The "
             "effective rate multiplies the claimed rate by the share of questions "
             "answered, and a claim that will not say how much was understood has not "
             "said much."),
            ("What a test looks like",
             "A fresh passage, questions written by someone else that cannot be "
             "answered from general knowledge, and a comparison reader or condition. "
             "A testimonial has none of the three."),
        ],
        "read_title": "Three lines of arithmetic, and a test",
        "read_intro": (
            "A claim followed to the eye, to the questions and to the bookshelf, then "
            "the studies that tested the claims properly."
        ),
        "body": [
            ("p", "Start with the warm-up, <em>The Message for Coldwater</em>, at your "
                  "usual pace: it is one more reading for your log, and a reminder of "
                  "what your rate feels like. Then take a claim, and the claim panel "
                  "below follows it through three computations."),
            ("p", "The claims are made at their strongest. Speed-reading courses "
                  "have long advertised rates of a thousand "
                  "words a minute and more, with graduates who say they read a novel "
                  "in an evening; some methods go further and promise a page taken in "
                  "at a glance. Photoreading and &ldquo;mental photography&rdquo; claim "
                  "to absorb a page without reading it, and make no prediction that "
                  "ordinary comprehension questions could not test, so they are tested "
                  "here the same way as everything else."),
            ("p", "The first computation is the one from How the Eyes Read. With the "
                  "average settings, a 225 ms fixation, a 30 ms saccade, six "
                  "characters to a word and no regressions, the characters a fixation "
                  "must advance are rate × 6 × 255 / 60,000. The preset "
                  "<strong>triple-speed</strong>, a claim of three times an ordinary "
                  "250, is 750 words in 60 seconds: 750 wpm, about 19.1 characters a "
                  "glance (19.125 exactly), beyond the perceptual span at these "
                  "settings."),
            ("p", "The preset <strong>a-novel-an-hour</strong> is 90,000 words in 60 "
                  "minutes: 1,500 wpm, and 38.25 characters a glance, two and a half "
                  "times the perceptual span. The preset <strong>whole-page</strong> "
                  "takes the glance claim literally, 350 words in a 2-second look: "
                  "10,500 wpm and 267.75 characters a glance, several lines of text "
                  "in one fixation. You can change the fixation and saccade times in "
                  "the panel; shorter fixations help, but to bring 1,500 inside the "
                  "perceptual span, a fixation and its saccade together would have to "
                  "take 100 ms, well under half the average fixation alone."),
            ("p", "The second computation asks what was understood. Each preset "
                  "assumes half the questions right, and the panel prints the "
                  "effective rate: 375 for the triple-speed claim, 750 for the novel an "
                  "hour, 5,250 for the page at a glance. Change the comprehension box "
                  "to what the claimant can show. A claim that cannot say what share "
                  "of questions was answered cannot fill the box at all."),
            ("p", "The third is the bookshelf. A 90,000-word novel at Brysbaert's 238 "
                  "words a minute takes 90,000 / 238, about 378 minutes, a little over "
                  "six hours. At the triple-speed 750 it is 120 minutes, and at 1,500 "
                  "it is the hour the claim promises. Woody Allen's line puts the "
                  "result of the fastest claims best: &ldquo;I took a speed-reading "
                  "course and read <em>War and Peace</em> in twenty minutes. It "
                  "involves Russia.&rdquo;"),
            ("p", "Then ask what would settle it. Just, Carpenter and Masson (1982) set "
                  "out the model: trained speed readers, ordinary readers and people "
                  "told to skim, on the same texts, with their eye fixations recorded "
                  "and their understanding tested. Carver (1985) went looking for the "
                  "world's best readers, speed-reading graduates and claimants among "
                  "them, and found none who showed comprehension at rates beyond about "
                  "600 words a minute; the fastest comprehending readers were superior "
                  "readers, not graduates of the courses."),
            ("p", "That is the test to ask of any claim, and of your own results: a "
                  "passage the reader has not seen, questions someone else wrote that "
                  "cannot be answered from general knowledge (Rayner and colleagues "
                  "make this point about speed-reading tests), and a comparison reader "
                  "or condition. The drills in this Subject are built that way, and "
                  "your log is the comparison."),
            ("p", "If you want to feel a claimed pace, the stream will show it to you "
                  "up to its cap. Go back to One Word at a Time, type 600 into the "
                  "target box, and watch the story go by; press Reset at the questions, "
                  "since you have read that story before and the answers would measure "
                  "your memory. Beyond 600 the drill will not go: the display becomes a "
                  "flicker, and that is itself the finding."),
            ("p", "This course has tested the tradition's techniques one at a time. The "
                  "next course, Skimming, Scanning and Previewing, is about the honest "
                  "version of reading a book in an hour: deciding what not to read."),
        ],
        "lab": ("readkit", {
            "mode": "eye",
            "view": "required",
            "claim": True,
            "warmup": PASSAGES["Q20"],
            "preset": "a-novel-an-hour",
            "presets": [
                {"id": "triple-speed", "label": "750 wpm, half understood",
                 "words": 750, "seconds": 60, "comp": "1/2", "expect": {"eyClaimWpm": "750 wpm", "eyNeeded": "≈ 19.1 characters", "eyVerdict": "at these settings, beyond the perceptual span", "eyClaimErr": "375 wpm"}},
                {"id": "a-novel-an-hour", "label": "90,000 words in an hour",
                 "words": 90000, "seconds": 3600, "comp": "1/2", "expect": {"eyClaimWpm": "1,500 wpm", "eyNeeded": "38.25 characters", "eyVerdict": "at these settings, beyond the perceptual span", "eyClaimErr": "750 wpm"}},
                {"id": "whole-page", "label": "350 words in a 2-second glance",
                 "words": 350, "seconds": 2, "comp": "1/2", "expect": {"eyClaimWpm": "10,500 wpm", "eyNeeded": "267.75 characters", "eyVerdict": "at these settings, beyond the perceptual span", "eyClaimErr": "5,250 wpm"}},
            ],
            "panel_title": "A claim, followed through",
            "panel_intro": (
                "A stated model: the claim's words and seconds give its rate; the eye "
                "settings give the characters each fixation would have to advance at "
                "that rate, against the word-identification span (about 8 characters) "
                "and the perceptual span (about 15). The comprehension box gives the "
                "effective rate. Every verdict holds at these settings only."
            ),
        }),
        "steps_title": "Testing any claim",
        "steps_intro": (
            "Four questions to put to a claimed speed, in this order, and then your "
            "own practice."
        ),
        "steps": [
            ("Turn the claim into a rate",
             "Words × 60 / seconds. A novel an hour, a page a glance and triple speed "
             "all become words a minute."),
            ("Compute what each glance would need",
             "Rate × 6 × 255 / 60,000 characters at average settings, against about 8 "
             "for identifying words and 15 for the perceptual span."),
            ("Ask what was understood, and how long a book takes",
             "The effective rate at the comprehension the claimant can show, and "
             "90,000 words divided by the rate for a novel."),
            ("Name the test that would settle it",
             "A fresh passage, questions written by someone else that cannot be "
             "answered from general knowledge, and a comparison reader. If the claim "
             "has not been tested that way, it is a claim."),
            DAILY,
        ],
        "worked": {
            "title": "A novel an hour",
            "intro": [
                "The claim: a 90,000-word novel in 60 minutes, at the average eye "
                "settings, with half the questions right.",
            ],
            "lines": [
                "rate = 90,000 / 60 = 1,500 words a minute",
                "glance = 1,500 × 6 × 255 / 60,000 = 38.25",
                "effective rate = 1,500 × 1/2 = 750",
                "book at 238: 90,000 / 238 ≈ 378 minutes",
            ],
            "after": [
                "Each fixation would have to take in about 38 characters, two and a "
                "half times the perceptual span. Even granting half the questions, "
                "the claim is 750 understood words a minute, three times an average "
                "reader's whole rate. The test that would settle it is the one Carver "
                "ran: a fresh text, someone else's questions, and comparison readers.",
            ],
        },
        "quiz_title": "Following a claim",
        "quiz": [
            {"q": "A course claims its graduates read 1,000 words a minute. At 225 ms "
                  "fixations, 30 ms saccades, six characters a word and no regressions, "
                  "how many characters must each fixation advance?",
             "a": ["12.75", "38.25", "25.5", "6"],
             "c": 2,
             "why": "1,000 × 6 × 255 / 60,000 = 25.5 characters, beyond the perceptual "
                    "span of about 15. 12.75 is the figure for 500 wpm and 38.25 for "
                    "1,500."},
            {"q": "How long does a 90,000-word novel take at 750 words a minute?",
             "a": ["2 hours", "1 hour", "12.5 hours", "20 minutes"],
             "c": 0,
             "why": "90,000 / 750 = 120 minutes. One hour is the time at 1,500 wpm."},
            {"q": "Which of these would best settle a claim that someone reads at 1,500 "
                  "words a minute with full comprehension?",
             "a": ["A video of them turning pages quickly",
                   "A passage they choose, with questions they write",
                   "Their own estimate of how much they understood",
                   "A passage new to them, questions written by someone else, and a "
                   "comparison reader"],
             "c": 3,
             "why": "A fresh text and someone else's questions measure understanding "
                    "rather than familiarity, and the comparison reader shows what "
                    "ordinary reading gets on the same test."},
            {"q": "What did Carver (1985) find when he tested some of the world's best "
                  "readers?",
             "a": ["Speed-reading graduates comprehended at about 1,500 wpm",
                   "None showed comprehension at rates beyond about 600 wpm",
                   "Every reader tested was below 238 wpm",
                   "Photoreaders scored best on the questions"],
             "c": 1,
             "why": "No tested reader showed comprehension beyond about 600 words a "
                    "minute, and the fastest comprehending readers were superior "
                    "readers, not speed-reading graduates."},
        ],
        "mistakes": [
            ("A claim with a testimonial is a measured claim",
             "A testimonial says how reading felt. A measured claim has a passage the "
             "reader had not seen, questions someone else wrote, and a comparison: the "
             "design of Just, Carpenter and Masson's study of speed readers, ordinary "
             "readers and skimmers, and of Carver's search for the best readers, "
             "which found none comprehending beyond about 600 words a minute."),
            ("Quoting a rate without the comprehension",
             "1,500 words a minute with nothing understood is page-turning. Ask what "
             "share of questions was answered and multiply; if nobody can say, the "
             "claim has no effective rate at all."),
            ("Reading the eye verdict as a law",
             "The verdict holds at the stated settings. Shorter fixations and skipped "
             "words raise what a skilled reader manages, which is why the settings can "
             "be changed; but a novel an hour would need a fixation and its saccade "
             "to take 100 ms together, well under half an average fixation."),
        ],
        "standard": (
            "Finish when you can follow a claim through three computations and name its test.",
            "Given a claimed rate, or words and a time, compute the characters each "
            "fixation would need at average settings, the effective rate at a stated "
            "comprehension, and the time a 90,000-word book would take; then name the "
            "three parts of a test that would settle it. All four pass."
        ),
        "note": (
            "The eye computation is a model with average settings; it says what a "
            "claim would require, not what any one reader's eyes do. The studies "
            "cited tested particular readers on particular texts, and the lesson "
            "takes only the design of Just, Carpenter and Masson's study, not its "
            "figures."
        ),
    },
]
