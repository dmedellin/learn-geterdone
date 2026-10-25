"""Course 3, lessons 01-06 -- How the Eyes Read (docs/reading/PLAN.md §C, Course 3)."""

from reading.passages import PASSAGES, POOL

_POOL = {p["id"]: p for p in POOL}


def _span_preset(hits):
    """A worked flash/span instance: ten 15-letter strings, every position asked.

    hits[d] is how many of the ten letters at distance d from the centre (both
    sides) were identified. Misses are spread over the strings, and the
    strings come from a stated generator, so the preset never changes.
    """
    letters = "BCDFGHJKLMNPQRSTVWXZ"
    s = 20261025
    targets, typed = [], []
    for i in range(10):
        t = ""
        for _p in range(15):
            s = (1103515245 * s + 12345) % 2147483648
            t += letters[(s >> 16) % len(letters)]
        a = ""
        for p in range(15):
            d = abs(p - 7)
            a += t[p] if (i + p) % 10 < hits[d] else "-"
        targets.append(t)
        typed.append(a)
    return {"targets": targets, "typed": typed}


_DAILY = ("Then today's Daily Drill",
          "Open The Daily Drill from Guided Practice and do today's session: one pool passage "
          "with the pacer at your hold target, or a test at natural pace when it says one is due.")

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "fixations-and-saccades",
        "title": "Fixations and Saccades",
        "module": "Fixations and saccades",
        "one_line": "Compute the rate that the eyes' stops and jumps allow, from five stated quantities.",
        "summary": (
            "Your eyes do not glide along a line: they stop for about a quarter of a second, jump "
            "a few letters, and stop again, and the text is taken in during the stops. A stated "
            "model turns the length of a stop, the length and reach of a jump, the share of jumps "
            "that go backwards and the length of a word into fixations per word, milliseconds per "
            "word and the rate those allow."
        ),
        "key": [
            "forward fixations per word = 6 / step",
            "fixations = forward / (1 − regressions)",
            "time a word = fixations × (fixation + saccade)",
            "rate = 60,000 / time per word",
            "typical: 15/17 fixation, 225 ms a word",
        ],
        "key_label": "The budget in five lines",
        "concepts_intro": (
            "Every speed claim in this course is checked against one small model. It has five "
            "quantities, and each has a measured typical value."
        ),
        "concepts": [
            ("Stops and jumps",
             "A fixation is a stop, about 200 to 250 ms long in silent reading. A saccade is the "
             "jump between stops: about 7 to 9 letter spaces, in 20 to 35 ms. Vision is "
             "suppressed during the jump, so the reading is done in the stops (Rayner 1998)."),
            ("Some jumps go backwards",
             "About 10 to 15% of saccades in skilled readers are regressions, back to text "
             "already passed. The model counts each one as a fixation that does not advance, "
             "which understates its cost: a real regression also has to travel back."),
            ("A model returns a rate, not a reader",
             "With the typical values the model allows about 267 words a minute, close to the "
             "measured averages for silent reading in English: 238 for non-fiction and 260 for "
             "fiction (Brysbaert 2019). It says what follows from the numbers put into it, not "
             "what any one reader does."),
        ],
        "read_title": "Stops, jumps and the budget they make",
        "read_intro": (
            "First a timed reading, so that you have a minute of your own reading to set the "
            "model against. Then the model, which says how a minute like that is spent."
        ),
        "body": [
            ("p", "Start with the warm-up in the lab, Why the Tide Keeps Moving, at your usual "
                  "pace, and answer its six questions. It is logged as practice and fills none of "
                  "the model's boxes. It is 453 words long; if you read it at about 250 words a "
                  "minute, the model below says your eyes stopped about four hundred times on the "
                  "way through."),
            ("p", "It did not feel like four hundred stops. Reading feels like a smooth slide "
                  "along the line, and that is the picture most readers hold. Watch someone "
                  "else's eyes while they read, though, and you see jerks and pauses. The jumps "
                  "were described in &Eacute;mile Javal's laboratory around 1879 &mdash; the "
                  "observation was his colleague Lamare's, and Ewald Hering made it independently "
                  "&mdash; and Javal's word for them, <em>saccade</em>, is the one that stuck "
                  "(Wade and Tatler 2009)."),
            ("def", ("Fixation, saccade, regression",
                     "A <strong>fixation</strong> is a stop of the eyes, during which text is taken "
                     "in. A <strong>saccade</strong> is the jump from one fixation to the next; "
                     "vision is suppressed while it happens. A <strong>regression</strong> is a "
                     "saccade that goes back to text already passed.")),
            ("p", "Rayner's 1998 review of twenty years of eye-tracking gives the typical "
                  "values for skilled adults reading silently: fixations of about 200 to 250 ms, "
                  "with 225 a fair middle; saccades of about 7 to 9 letter spaces, taking 20 to "
                  "35 ms; and regressions making up about 10 to 15% of saccades. Add a length for "
                  "a word &mdash; six characters with the space, the convention of a "
                  "standard-length word &mdash; and you have the five quantities of the model."),
            ("math", [
                "forward fixations per word = 6 / step",
                "fixations per word = forward / (1 − regressions)",
                "time per word = fixations × (fixation + saccade)",
                "rate = 60,000 / time per word",
            ]),
            ("p", "The <strong>typical</strong> preset puts in 225 ms, 30 ms, 8 characters a "
                  "step, a regression share of 3/20 and 6 characters a word. Six over eight is "
                  "3/4 of a forward fixation per word; dividing by 17/20 gives 15/17 &asymp; 0.9 "
                  "fixations; at 255 ms each that is 225 ms per word, and 60,000 / 225 &asymp; "
                  "266.7 words a minute."),
            ("p", "Now change one thing at a time. The <strong>no-regressions</strong> preset "
                  "sets the regression share to 0: 3/4 = 0.75 fixations, 191.25 ms per word, "
                  "&asymp; 313.7 words a minute. That is everything that cutting every regression "
                  "could buy at these settings, and Looking Back is about why you would not want "
                  "to. The <strong>long-fixations</strong> preset keeps the regressions and "
                  "lengthens each stop to 300 ms: still 15/17 fixations, now &asymp; 291.2 ms per "
                  "word, &asymp; 206.1 words a minute. A stop 75 ms longer costs about sixty "
                  "words a minute; the length of a stop is where most of the budget goes."),
            ("p", "What the model leaves out, stated once. It counts a regression as one more "
                  "fixation that does not advance, but a real regression also travels back and "
                  "the eyes must then move forward again, so the model understates what looking "
                  "back costs. Skipping short words and fixating long ones twice are folded into "
                  "the average step. And six characters a word is a convention, not a "
                  "measurement of your text."),
            ("ul", [
                "One cost the model leaves out is the end of the line. The eyes make a long jump "
                "back to the start of the next line, a return sweep, and it costs about one more "
                "fixation per line.",
                "On a line of 64 characters at 8 a step, that is about 8 forward fixations and "
                "one more for the sweep, so roughly an eighth more time than the model says.",
                "Over 30 such lines, about 30 extra fixations: at 255 ms each, about 7.7 seconds a "
                "page. Shorter lines mean more sweeps for the same words.",
            ]),
            ("p", "Set the warm-up beside the model. If your warm-up came out at 240 words a "
                  "minute and the typical preset says 266.7, the gap is not a finding about your "
                  "eyes: the model's inputs are averages over many readers in a laboratory, and "
                  "your rate is one passage on one day. What the model gives you is a way to ask "
                  "where time could go, and how much each part can move the total."),
            ("p", "The model assumes that each stop takes in about eight new characters. The "
                  "next lesson, The Perceptual Span, measures how far one glance reaches."),
        ],
        "lab": ("readkit", {
            "mode": "eye",
            "view": "budget",
            "warmup": PASSAGES["P06"],
            "preset": "typical",
            "presets": [
                {"id": "typical", "label": "Typical: 225 ms, 30 ms, 8 characters, 3/20 back",
                 "fix": 225, "sac": 30, "step": 8, "reg": "3/20", "cpw": 6, "expect": {"eyFixPerWord": "15/17 ≈ 0.9 fixations", "eyMsPerWord": "225 ms",
                            "eyWpm": "≈ 266.7 wpm"}},
                {"id": "no-regressions", "label": "No regressions at all",
                 "fix": 225, "sac": 30, "step": 8, "reg": 0, "cpw": 6, "expect": {"eyFixPerWord": "3/4 = 0.75 fixations", "eyMsPerWord": "191.25 ms",
                            "eyWpm": "≈ 313.7 wpm"}},
                {"id": "long-fixations", "label": "Longer stops: 300 ms",
                 "fix": 300, "sac": 30, "step": 8, "reg": "3/20", "cpw": 6, "expect": {"eyFixPerWord": "15/17 ≈ 0.9 fixations", "eyMsPerWord": "≈ 291.2 ms",
                            "eyWpm": "≈ 206.1 wpm"}},
            ],
            "panel_intro": (
                "A stated model: forward fixations per word = characters per word / characters "
                "per saccade; fixations per word = that / (1 − regression share); time per word = "
                "fixations × (fixation + saccade); rate = 60,000 / time per word. A regression is "
                "counted as one more fixation that does not advance, which understates its cost: a "
                "real regression also travels back (Rayner 1998). A return sweep at the end of each "
                "line, about one more fixation per line, is not in the model. The warm-up above "
                "is your measurement and fills none of these boxes."
            ),
        }),
        "steps_title": "Doing it again on another day",
        "steps_intro": "Five steps, about ten minutes. The first needs a second person or a mirror.",
        "steps": [
            ("Watch eyes read",
             "Ask someone to read a few lines silently while you watch their eyes from the side, "
             "or hold a small mirror beside the page and glance at your own. Count the jumps across "
             "one line. The oldest demonstration there is still works."),
            ("Do the warm-up at your usual pace",
             "The warm-up serves the next passage you have not logged. Read once, answer the six "
             "questions, and note the rate and the effective rate."),
            ("Load the typical preset and say each line",
             "Say aloud what each tile is: fixations per word, milliseconds per word, the rate "
             "the model allows. Then do the same arithmetic on paper."),
            ("Move one quantity at a time",
             "Change the fixation, then the step, then the regression share, each by a realistic "
             "amount, and write down which moved the rate most."),
            _DAILY,
        ],
        "worked": {
            "title": "The typical reader's budget",
            "intro": [
                "Fixation 225 ms, saccade 30 ms, 8 characters a step, regressions 3/20 of "
                "fixations, 6 characters a word.",
            ],
            "lines": [
                "forward fixations = 6 / 8 = 3/4",
                "all fixations = (3/4) / (17/20) = 15/17",
                "time per word = (15/17) × 255 = 225 ms",
                "rate = 60,000 / 225 ≈ 266.7 words a minute",
            ],
            "after": [
                "Dividing by 17/20 is what the regressions cost in the model: three stops in "
                "twenty do not advance, so the forward ones must be made up by the rest. The "
                "typical preset shows the same four figures.",
            ],
        },
        "quiz_title": "The budget",
        "quiz": [
            {"q": "Fixations of 225 ms, saccades of 30 ms, 8 characters a step, no regressions, "
                  "6 characters a word. What is the time per word?",
             "a": ["225 ms", "191.25 ms", "255 ms", "168.75 ms"],
             "c": 1,
             "why": "Six over eight is 3/4 of a fixation per word, and each costs 225 + 30 = 255 "
                    "ms, so 191.25 ms. 225 ms is the figure with regressions of 3/20; 255 ms "
                    "assumes one fixation per word; 168.75 ms leaves out the saccade."},
            {"q": "Why does the model understate what a regression costs?",
             "a": ["It counts a regression as one stop that does not advance, but a real one "
                   "also travels back and then forward again",
                   "Regressions are shorter jumps than forward saccades, and the model gives "
                   "them the full forward length",
                   "The model leaves saccade time out of the time per word",
                   "The model's regression share is a share of words, not of fixations"],
             "c": 0,
             "why": "A regression in the model is only a fixation that does not advance. In real "
                    "reading the eyes also travel back and then pick up the line again. The "
                    "model does include saccade time, and its regression share is a share of "
                    "fixations; the length of a backward jump is not one of its inputs."},
            {"q": "When is the text taken in?",
             "a": ["During the saccades, while the eyes are moving",
                   "Evenly, during both stops and jumps",
                   "During the fixations, while the eyes are still",
                   "Mostly during the return sweeps at the ends of lines"],
             "c": 2,
             "why": "Vision is suppressed during a saccade, so nearly all the reading happens in "
                    "the fixations. The return sweep is itself a saccade, so nothing is taken in "
                    "during it either."},
            {"q": "The long-fixations preset changes only the fixation, from 225 ms to 300 ms. "
                  "What rate does the model allow?",
             "a": ["≈ 266.7 words a minute", "200 words a minute",
                   "≈ 313.7 words a minute", "≈ 206.1 words a minute"],
             "c": 3,
             "why": "15/17 fixations at 330 ms each is &asymp; 291.2 ms a word, and 60,000 divided "
                    "by that is &asymp; 206.1. 266.7 is the typical rate before the change; 200 is "
                    "one 300 ms fixation per word with no saccades; 313.7 is the rate with no "
                    "regressions."},
        ],
        "mistakes": [
            ("Picturing the eyes gliding along the line",
             "They jump and stop. Vision is suppressed during each jump, so nearly all the reading "
             "happens in the stops, about four of them a second. The jumps were described in "
             "Javal's laboratory around 1879, by Lamare, and by Hering independently; Javal's word "
             "&ldquo;saccade&rdquo; stuck. Any technique that promises to make the eyes "
             "&ldquo;flow&rdquo; is describing something the eyes do not do."),
            ("Reading the model's rate as your rate",
             "266.7 words a minute is what five averages imply, not a measurement of anyone. Your "
             "warm-up is one measurement of you. When they differ, neither is wrong; they answer "
             "different questions."),
            ("Treating a regression as free",
             "The model already charges a regression one stop, and a real one costs more, because "
             "the eyes must travel back and then forward again. Whether that cost is worth paying "
             "is the question of Looking Back."),
        ],
        "standard": (
            "Compute a budget by hand",
            "Given a fixation and a saccade duration, characters per saccade, a regression share "
            "and characters per word, compute fixations per word and words a minute by hand, "
            "exactly or to one decimal, and say which of the five quantities moves the rate most "
            "for a realistic change."
        ),
        "note": (
            "The model's inputs are averages from laboratory eye-tracking of skilled adult readers. "
            "The lab computes what they imply; it does not track your eyes, and your warm-up "
            "measured only your time and your answers on one passage."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-perceptual-span",
        "title": "The Perceptual Span",
        "module": "Fixations and saccades",
        "one_line": "Measure how far from the centre a 150 ms glance identifies letters, and set it against the span in reading.",
        "summary": (
            "A row of random letters is flashed for less time than the eyes need to move, and you "
            "name the letters at a few marked positions. Scored by distance from the centre, the "
            "answers show how far letter identification reaches from one fixation. The span that "
            "matters in reading is related but different: it is measured with real text, and it "
            "is lopsided."
        ),
        "key": [
            "accuracy at a position = right / asked",
            "span: farthest position, half or more right",
            "chance with four choices: 1 in 4",
            "reading span: 3 to 4 left, 14 to 15 right",
            "words identified: about 7 to 8 right",
        ],
        "key_label": "Two spans in five lines",
        "concepts_intro": (
            "One fixation takes in a window of text. How wide it is depends on what is being "
            "measured, and the drill and the reading studies measure different things."
        ),
        "concepts": [
            ("A flash too short to look at",
             "The letters are shown for 150 ms. Starting a saccade takes about 175 to 200 ms, so "
             "the flash is over before the eyes could move to it: what you report was seen from "
             "the one fixation on the centre."),
            ("Asking for a few letters after the flash",
             "Fifteen letters are too many to hold in mind, so the drill marks two or three "
             "positions only after the flash has gone. Because you cannot know in advance which "
             "will be asked, your answers sample what was available everywhere in the row."),
            ("The span in reading is lopsided",
             "Measured with real text, the perceptual span reaches about 3 to 4 letters to the "
             "left of the fixation and 14 to 15 to the right, and words are identified only within "
             "about 7 to 8 to the right. The asymmetry follows attention in the direction of "
             "reading (Rayner 1998)."),
        ],
        "read_title": "How far one glance reaches",
        "read_intro": (
            "The drill comes first in the lab and takes about five minutes. Read what it does "
            "before you start, so that the flash does not surprise you."
        ),
        "body": [
            ("p", "The drill in the lab runs twenty flashes. Each begins with a + where your eyes "
                  "should rest. Then a row of fifteen random letters appears for 150 ms, a mask "
                  "of # signs covers it, and three positions are marked one at a time; for each, "
                  "you pick the letter that was there from four, or say you did not see it. Keep "
                  "your eyes on the + and do not try to look along the row: there is no time."),
            ("p", "The flash is shorter than the time it takes to start a saccade, about 175 to "
                  "200 ms, so everything you report was seen from the fixation on the centre. The "
                  "150 ms is requested; a screen can show it a frame or two longer, and the drill "
                  "prints what it measured. The drill is logged as <em>other</em>, because it is "
                  "not a reading."),
            ("p", "The answers are scored by position, from &minus;7 on the left to +7 on the "
                  "right. Accuracy at a position is the letters you got right there over the "
                  "times it was asked, and your span is the farthest position on each side where "
                  "it was at least one half. One caution before you read your own: with four "
                  "choices a pure guess is right one time in four, and twenty flashes of three "
                  "marks ask each position only about four times, so one lucky answer can move a "
                  "position by a quarter."),
            ("p", "The <strong>typical</strong> preset writes out a reader whose every position "
                  "was asked ten times: 10/10 at the centre, 9/10 at one letter either side, 8/10 "
                  "at two, 6/10 at three, 4/10 at four, and 2/10 from five outwards. Its tiles "
                  "read 1 = 100% at the centre, 1/5 = 20% at the outermost positions (4 right of "
                  "20 asked, close to guessing), and a span of left 3, right 3. The "
                  "<strong>strong</strong> preset is the same reader with 6/10 at four letters, "
                  "and its span reads left 4, right 4."),
            ("p", "Notice that both spans are symmetric. A row of random letters has no "
                  "direction to read in and no words to recognise, so nothing pulls attention one "
                  "way. That is what makes this a different span from the one in reading."),
            ("h3", "The span in reading"),
            ("p", "The reading span was measured by McConkie and Rayner in 1975 with a moving "
                  "window: as a reader's eyes moved, a computer changed the text outside a window "
                  "around each fixation and left the window intact. When the window was wide "
                  "enough that reading went on at its normal speed, it held everything the reader "
                  "was using. The answer, gathered in Rayner's 1998 review, is about 3 to 4 "
                  "letters to the left of the fixation and 14 to 15 to the right, with words "
                  "identified only within about 7 to 8 letters to the right; beyond that, the "
                  "reader picks up mostly the lengths of words."),
            ("p", "The lopsidedness is attention, not the eye. For readers of Hebrew, which runs "
                  "right to left, the span is larger to the left (Pollatsek, Bolozky, Well and "
                  "Rayner 1981). The span is also smaller on hard text and somewhat larger in "
                  "faster, more skilled readers (Rayner, Slattery and B&eacute;langer 2010). So it "
                  "is set by acuity and by attention together, and it does move a little."),
            ("p", "What it does not do, on any evidence, is reach a whole line. Some speed-reading "
                  "courses teach readers to take in a line, or a page, at a glance. Your own "
                  "drill puts a number on why that is a large claim: past three or four letters "
                  "either side, even unrelated letters with your full attention on them were "
                  "mostly guesses. A line of 65 characters is about eight word-identification "
                  "spans long."),
            ("p", "The worked example reads one side of the typical preset: 6/10 at +3 and 4/10 "
                  "at +4. The identification of random letters ends between those two positions, "
                  "and the tile says right 3."),
            ("p", "A span limits what one fixation can take in. The next lesson, Looking Back, "
                  "asks what happens when the eyes cannot return to what they have passed."),
        ],
        "lab": ("readkit", {
            "mode": "flash",
            "view": "span",
            "len": 15,
            "ms": 150,
            "n": 20,
            "cues": 3,
            "kind": "other",
            "preset": "typical",
            "presets": [
                dict({"id": "typical", "label": "Typical: 6/10 at three letters, 4/10 at four",
                      "expect": {"flCentre": "1 = 100%", "flEdge": "1/5 = 20%", "flSpan": "left 3, right 3"}},
                     **_span_preset([10, 9, 8, 6, 4, 2, 2, 2])),
                dict({"id": "strong", "label": "Strong: 6/10 at four letters",
                      "expect": {"flCentre": "1 = 100%", "flEdge": "1/5 = 20%", "flSpan": "left 4, right 4"}},
                     **_span_preset([10, 9, 8, 6, 6, 2, 2, 2])),
            ],
        }),
        "steps_title": "Doing it again on another day",
        "steps_intro": "Five steps, about ten minutes. Sit at the same distance from the same screen each time.",
        "steps": [
            ("Settle the eyes first",
             "Sit at your usual distance in a quiet place. Before each flash, rest your eyes on "
             "the + and keep them there."),
            ("Run the twenty flashes",
             "Answer the marked positions only. When you did not see a letter, say so rather than "
             "guess: a guess among four is right one time in four and makes the edges look wider "
             "than they are."),
            ("Read the accuracies by position",
             "Find the centre, the outermost positions and the farthest position each side at "
             "half or better. Note how many times each was asked."),
            ("Set it beside the reading span",
             "Write your span next to 3 to 4 left and 14 to 15 right, and say in a sentence why "
             "yours is roughly symmetric and the reading span is not."),
            _DAILY,
        ],
        "worked": {
            "title": "Where identification ends",
            "intro": [
                "The typical preset, right of the centre: 9/10 at +1, 8/10 at +2, 6/10 at +3, 4/10 "
                "at +4, 2/10 at +5.",
            ],
            "lines": [
                "+3: 6/10 = 60%, at least 1/2",
                "+4: 4/10 = 40%, below 1/2",
                "span on the right: 3",
            ],
            "after": [
                "Identification of random letters ends between +3 and +4. The left side reads the "
                "same, so the tile prints left 3, right 3.",
            ],
        },
        "quiz_title": "Two spans",
        "quiz": [
            {"q": "In the typical preset, which tiles does the lab print for the span?",
             "a": ["left 4, right 4", "left 3, right 3", "left 3, right 15", "left 7, right 7"],
             "c": 1,
             "why": "6/10 at &plusmn;3 is at least a half and 4/10 at &plusmn;4 is not, so the "
                    "span is 3 on each side. Left 4, right 4 is the strong preset; 3 and 15 mixes "
                    "in the reading span; 7 is the end of the string."},
            {"q": "Why is the span this drill measures roughly symmetric, when the span in reading "
                  "is not?",
             "a": ["The flash is too short for the eyes to drift to the right",
                   "The drill uses capital letters, which are equally visible on both sides",
                   "Random letters have no reading direction, so attention is not pulled to the "
                   "right",
                   "The drill asks about the left positions as often as the right ones"],
             "c": 2,
             "why": "The reading span is lopsided because attention runs ahead in the direction of "
                    "reading; it reverses for readers of Hebrew. A row of random letters gives "
                    "attention no direction. Asking both sides equally is fair scoring, not the "
                    "cause: the reading span was measured with text on both sides too."},
            {"q": "Why is the flash 150 ms?",
             "a": ["It is shorter than the 175 to 200 ms needed to start a saccade, so the eyes "
                   "cannot move to the letters",
                   "It is the length of an average fixation in silent reading",
                   "It is the shortest time a screen can show anything",
                   "It is the time one saccade takes to cross seven letters"],
             "c": 0,
             "why": "The point is to measure what one fixation takes in, so the letters must be "
                    "gone before an eye movement could land. An average fixation is about 225 ms, "
                    "a saccade itself takes 20 to 35 ms, and screens can show much less than "
                    "150 ms."},
            {"q": "In reading, about how far to the right of the fixation are words identified?",
             "a": ["14 to 15 letters", "3 to 4 letters", "About a whole line",
                   "7 to 8 letters"],
             "c": 3,
             "why": "Words are identified within about 7 to 8 letters to the right. 14 to 15 is the "
                    "whole perceptual span, which includes word lengths and rough shapes beyond "
                    "identification; 3 to 4 is the span to the left."},
        ],
        "mistakes": [
            ("Believing a trained eye takes in a line at a glance",
             "In reading, the perceptual span is about 3 to 4 letters left and 14 to 15 right, and "
             "words are identified only within about 7 to 8 letters to the right. It is smaller on "
             "hard text and somewhat larger in skilled readers, but there is no evidence that "
             "training widens it to a line. Your drill measures a related but different span, "
             "letters with no context, and it ended a few letters from the centre too."),
            ("Reading the drill's span as the reading span",
             "Random letters, flashed, with no words and no direction, measure letter "
             "identification by position. The reading span is measured with real text and is "
             "lopsided. A symmetric left 3, right 3 does not contradict the reading figures; it "
             "answers a different question."),
            ("Trusting one position's score",
             "Twenty flashes of three marks ask each position about four times, and a guess "
             "among four is right one time in four. One lucky answer can lift a position over "
             "the half line. Read the pattern across positions, not one cell."),
        ],
        "standard": (
            "Read a span from accuracies",
            "Given accuracy by position, name the farthest position on each side with accuracy "
            "of at least one half, and say in two sentences why the span in reading is "
            "asymmetric while this one is not."
        ),
        "note": (
            "The drill measures letters identified by position in a 150 ms flash, on your screen, "
            "on one day, with about four answers per position. It is not the perceptual span in "
            "reading, which can only be measured by tracking the eyes over real text."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "looking-back",
        "title": "Looking Back",
        "module": "Fixations and saccades",
        "one_line": "Find out what hiding the text behind your eyes does to comprehension at a fixed rate.",
        "summary": (
            "Two readings at the same pacer rate: one with the passage left on the page, one with "
            "each line hidden once the highlight has passed it, so that looking back finds nothing. "
            "Because the rate is fixed, the comparison is a comparison of comprehension, read "
            "through the effective rate. It asks whether the regressions you make are a habit to "
            "cut or a repair you need."
        ),
        "key": [
            "same pacer rate on both readings",
            "effective rate = rate × comprehension",
            "one question = 1/6 of comprehension",
            "300 × 4/6 = 200, against 300 × 6/6 = 300",
        ],
        "key_label": "One rate, two scores",
        "concepts_intro": (
            "Speed-reading courses often treat every backward glance as a habit to break. This "
            "lesson tests that on your own reading."
        ),
        "concepts": [
            ("Regressions are ordinary",
             "About 10 to 15% of saccades in skilled readers go backwards (Rayner 1998). They are "
             "part of normal reading, not a fault peculiar to slow readers."),
            ("Masking makes looking back useless",
             "The mask display hides every line above the highlight as the pacer moves on. You can "
             "still glance back, but there is nothing there to read, so any repair a regression "
             "would have made cannot happen."),
            ("A fixed rate turns the comparison into one of comprehension",
             "Both readings run with the pacer at one rate, so their rates come out the same. "
             "Whatever differs in the effective rate comes from the questions, and one question "
             "is a sixth of the score."),
        ],
        "read_title": "What looking back is for",
        "read_intro": (
            "Set both target boxes to your hold target from Guided Practice before you start. "
            "Then do both readings, in the order the lab gives."
        ),
        "body": [
            ("p", "The lab has two readings. Reading A, The Dance in the Hive, runs with the pacer: "
                  "a highlight moving line by line at the target rate. Reading B, Hearing in the "
                  "Dark, runs with the mask: the same pacer, with each line above the highlight "
                  "hidden as it goes. Put your hold target in both target boxes, do them in the "
                  "order the lab names, and answer the six questions after each. Both are logged as "
                  "condition readings, so neither counts towards your baseline or tests."),
            ("p", "A reader who regresses a lot usually feels it as a fault: the eyes slip back, "
                  "the line is read twice, time is lost. The tradition agrees, and many "
                  "speed-reading courses teach readers to suppress it. The mask is a way of asking "
                  "what those backward glances were doing, by making them find nothing."),
            ("p", "The evidence comes from a study that did this far more precisely. Schotter, "
                  "Tran and Rayner (2014) tracked readers' eyes and replaced each word with x's "
                  "the moment the eyes left it, so that a reader could still look back but would "
                  "find only x's. Comprehension fell, for ordinary sentences as well as for "
                  "sentences built to be ambiguous. And in normal reading, sentences on which "
                  "readers had regressed were understood about as well as ones on which they had "
                  "not: the regressions came when they were needed."),
            ("p", "The kit's mask is a coarser version of their method. It hides whole lines, not "
                  "words, and only once the highlight has moved on, so you can still look back "
                  "within the line you are on. If anything, it costs less than their mask did."),
            ("p", "Because both readings ran at the pacer's rate, their rates come out the same, "
                  "and the difference lies in the questions. At 300 words a minute one question "
                  "is worth 50 words a minute of effective rate, so a difference of 50 is a "
                  "difference of one question, which is not a result."),
            ("p", "The <strong>masked-costs</strong> preset is a reader at 300 words a minute "
                  "both times: 447 words in 89.4 seconds with all six right, an effective rate of "
                  "300; then 436 words in 87.2 seconds with four right, 300 &times; 4/6 = 200. The "
                  "difference is &minus;100 words a minute, two questions. The "
                  "<strong>no-cost</strong> preset is a reader who got five of six on both, 250 "
                  "and 250, a difference of nothing at all."),
            ("p", "If your result looks like no-cost, you have not refuted the study, and the "
                  "study has not refuted you. Your two readings were of different passages, one "
                  "of them came first, and each is one reading; the study had many readers, many "
                  "sentences and a tracker that knew where every word was. What you have learned "
                  "is what the mask did to you on one day, which is worth knowing too."),
            ("p", "What the study does not support is the idea that regressions are wasted time "
                  "to be trained away. Some may be: the next lesson, Fewer Needless Regressions, "
                  "separates the ones that repair understanding from the ones that only follow a "
                  "wandering mind."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P07"], PASSAGES["P08"]],
            "a": {"display": "pacer", "target": 300, "kind": "condition",
                  "label": "Reading A, with the pacer"},
            "b": {"display": "mask", "target": 300, "kind": "condition",
                  "label": "Reading B, with the mask"},
            "preset": "masked-costs",
            "presets": [
                {"id": "masked-costs", "label": "The mask costs two questions",
                 "wordsA": 447, "secondsA": "89.4", "correctA": 6, "totalA": 6, "targetA": 300,
                 "wordsB": 436, "secondsB": "87.2", "correctB": 4, "totalB": 6, "targetB": 300,
                 "expect": {"drErrA": "300 wpm", "drErrB": "200 wpm", "drErrDiff": "−100 wpm"}},
                {"id": "no-cost", "label": "No cost: five right both times",
                 "wordsA": 447, "secondsA": "89.4", "correctA": 5, "totalA": 6, "targetA": 300,
                 "wordsB": 436, "secondsB": "87.2", "correctB": 5, "totalB": 6, "targetB": 300,
                 "expect": {"drErrA": "250 wpm", "drErrB": "250 wpm", "drErrDiff": "0 wpm"}},
            ],
        }),
        "steps_title": "Doing it again on another day",
        "steps_intro": "Five steps, about twelve minutes. Use a pair of passages you have not read.",
        "steps": [
            ("Set one rate for both",
             "Put your current hold target in both target boxes, so that the only difference "
             "between the readings is whether the text behind you stays."),
            ("Read in the order given",
             "The lab alternates which reading comes first from one comparison to the next. Do the "
             "first, answer its questions, then the second."),
            ("Compute both effective rates",
             "Multiply each rate by its comprehension, then work out what one question is worth at "
             "your rate: the rate divided by six."),
            ("Decide whether the difference is a result",
             "A difference of one question or less is not. Two or more is worth writing in your "
             "log beside the date, as one comparison."),
            _DAILY,
        ],
        "worked": {
            "title": "The masked-costs reader",
            "intro": [
                "Both readings at 300 words a minute; six of six with the pacer, four of six with "
                "the mask.",
            ],
            "lines": [
                "A: 300 × 6/6 = 300 words a minute",
                "B: 300 × 4/6 = 200 words a minute",
                "B − A = −100, and one question = 300 / 6 = 50",
            ],
            "after": [
                "The difference is two questions' worth. On one pair of passages that is worth "
                "noting; it is not yet a finding about you.",
            ],
        },
        "quiz_title": "One rate, two scores",
        "quiz": [
            {"q": "Both readings ran at 270 words a minute. With the pacer you got 5 of 6; with "
                  "the mask, 4 of 6. What are the two effective rates?",
             "a": ["270 and 180", "225 and 180", "225 and 216", "270 and 216"],
             "c": 1,
             "why": "270 &times; 5/6 = 225 and 270 &times; 4/6 = 180. The difference, 45, is one "
                    "question at this rate, so it is not a result. 270 is the rate before "
                    "comprehension; 216 is 270 &times; 4/5, as if there were five questions."},
            {"q": "What did Schotter, Tran and Rayner (2014) do?",
             "a": ["Prevented readers from moving their eyes backwards at all",
                   "Replaced each word with x's once the eyes had left it, so looking back found "
                   "nothing",
                   "Hid every line above the one being read, as the kit's mask does",
                   "Trained readers to stop regressing and measured their speed afterwards"],
             "c": 1,
             "why": "They used a trailing mask, word by word, driven by an eye tracker. Readers "
                    "could still look back; they found x's. The kit's line mask is a coarser "
                    "version of the same idea, and nobody in the study was trained."},
            {"q": "In that study, where did the mask lower comprehension?",
             "a": ["Only on sentences built to be ambiguous",
                   "Only for readers who regressed more than average",
                   "On ordinary sentences as well as ambiguous ones",
                   "Nowhere; it lowered reading speed instead"],
             "c": 2,
             "why": "The cost was not confined to the ambiguous sentences. Comprehension fell with "
                    "the mask for both kinds, which is why the study argues that regressions "
                    "support comprehension generally."},
        ],
        "mistakes": [
            ("Calling regressions a bad habit to eliminate",
             "They are about 10 to 15% of saccades in skilled readers. When Schotter, Tran and "
             "Rayner made going back useless &mdash; each word turned to x's as the eyes left it "
             "&mdash; comprehension fell, for ordinary sentences as well as ambiguous ones; in "
             "normal reading, regressions happen when they are needed. The kit's mask hides whole "
             "lines, a coarser version of their method."),
            ("Reading a one-question difference as a result",
             "At 300 words a minute one question is 50 words a minute of effective rate. A "
             "reading with the mask that comes out 50 lower has lost one answer, which happens "
             "between any two passages."),
            ("Comparing rates instead of scores",
             "Both readings ran at the pacer's rate, so their rates agree by design. The question "
             "this drill answers is in the comprehension, and so in the effective rate."),
        ],
        "standard": (
            "Compare two scores at one rate",
            "Given two readings at one rate and their scores out of six, compute both effective "
            "rates and the value of one question at that rate, and say whether the difference "
            "exceeds one question."
        ),
        "note": (
            "Two readings are two passages, and one of them came first; the lab alternates the "
            "order but cannot remove it. One comparison on one day cannot tell a cost of the mask "
            "from a harder second passage, and the kit's line mask is not the word-by-word mask "
            "of the study."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "fewer-needless-regressions",
        "title": "Fewer Needless Regressions",
        "module": "Fixations and saccades",
        "one_line": "Separate looking back to repair understanding from losing your place, and compare a paced and an unpaced reading on both.",
        "summary": (
            "Some backward glances repair understanding; others follow a mind that drifted off the "
            "line. This lesson compares a reading at your natural pace with one behind the pacer, "
            "on effective rate and on a count you keep yourself of the times you lost your place. "
            "The eye-movement budget shows what a smaller regression share could be worth."
        ),
        "key": [
            "repair: a look back that restores the sense",
            "lapse: going back after the mind drifted",
            "lapses are a self-report, not a measure",
            "budget at 3/20 back: ≈ 266.7 words a minute",
            "budget at 7/100 back: ≈ 291.8 words a minute",
        ],
        "key_label": "Two kinds of looking back",
        "concepts_intro": (
            "Looking Back showed what regressions do for comprehension. This lesson asks which of "
            "them, if any, can go."
        ),
        "concepts": [
            ("Repair and drift",
             "A repair regression goes back because the sense did not hold: a word misread, a "
             "sentence that turned. A lapse is different: the eyes kept moving while attention "
             "went elsewhere, and re-reading is how you notice. The split is a teaching device, "
             "not a distinction the studies measured."),
            ("A count you keep",
             "After each reading you write down how many times you lost your place or re-read "
             "for no reason. It is a self-report: it counts what you noticed, not what your eyes "
             "did."),
            ("What a pacer can and cannot do",
             "A pacer keeps a steady pace and gives the eyes somewhere to be, which may reduce "
             "drifting. It cannot make a repair unnecessary, and hiding the text behind it would "
             "make repairs impossible."),
        ],
        "read_title": "Repair, drift and the pacer",
        "read_intro": (
            "Keep a pencil by you: after each reading, before the questions, write down how often "
            "you lost your place."
        ),
        "body": [
            ("p", "Two readings again. Reading A, A Hand on the Wire, is at your natural pace with "
                  "no pacer, and is logged as a test. Reading B, Soup for Twenty-Six, runs behind "
                  "the pacer at your hold target, and is logged as a condition reading. Keep a "
                  "count as you read of how many times you lost your place or re-read for no "
                  "reason. After each reading, before the questions, the lab asks for that "
                  "number, puts it in the lapse boxes and logs it with the reading."),
            ("p", "Most readers who try this find the second number smaller. The pacer gives the "
                  "eyes a place to be, and a moving highlight is harder to drift away from than a "
                  "still page. That is the experience the tradition reports, and it is worth "
                  "having for yourself. It is also a self-report: you count the lapses you "
                  "noticed, and some lapses pass unnoticed."),
            ("p", "Looking Back showed that regressions which repair the sense carry "
                  "comprehension, so a course that trains readers to stop regressing altogether "
                  "trains away the repairs as well. The useful question is not how to stop "
                  "looking back, but whether the looking back that follows drifting can be made "
                  "rarer. Splitting regressions this way is a teaching device; the studies "
                  "measured regressions, not their reasons."),
            ("p", "The eye-movement budget puts a size on it, with illustrative shares. Suppose a "
                  "reader's regressions are 3/20 of fixations, and drifting accounts for some of "
                  "them; if steadier attention brought the share down to 7/100, the model says:"),
            ("math", [
                "3/20 back: (3/4) / (17/20) = 15/17 fixations",
                "15/17 × 255 = 225 ms; 60,000 / 225 ≈ 266.7",
                "7/100 back: (3/4) / (93/100) = 25/31 fixations",
                "25/31 × 255 ≈ 205.6 ms; 60,000 × 31 / 6,375 ≈ 291.8",
            ]),
            ("p", "About 25 words a minute, at the same comprehension, if the regressions cut "
                  "were all lapses. The shares are invented for the example; nobody knows yours, "
                  "and the model understates what a regression costs. Treat the figure as the "
                  "size of the prize, not a promise of it."),
            ("p", "Now the lab. The <strong>pacer-steadies</strong> preset is a reader who read A "
                  "at 240 words a minute (484 words in 121 seconds) with five of six right, an "
                  "effective rate of 200, and counted four lapses; then read B behind the pacer at "
                  "264 (457 words in 103.864 seconds, as the drill records time to the "
                  "millisecond) with five of six again, an effective rate of &asymp; 220.0, and "
                  "counted one lapse. The difference is &asymp; +20.0 words a minute, less than "
                  "one question's worth at these rates, so the effective rates do not show a "
                  "result; the lapse count, four against one, is the part worth noting, as a "
                  "self-report. The <strong>no-change</strong> preset is a reader at 250 both "
                  "times, five of six both times, an effective rate of &asymp; 208.3 each, with "
                  "two lapses both times."),
            ("p", "If your readings look like no-change, you have not refuted anyone, and nobody "
                  "has refuted you: the two passages differ, one came first, and B's rate was set "
                  "by the pacer rather than by you. Reading A is logged as a test at natural pace, "
                  "so it joins your history. B's rate was the pacer's, so the lab does not set "
                  "it against your baseline range."),
            ("p", "A pacer can do something for drift. What it cannot do is widen the window a "
                  "fixation takes in, or make a regression that repairs the sense unnecessary. "
                  "The next lesson, The Speed Ceiling, turns the window into a limit on speed."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "compare",
            "passages": [PASSAGES["P21"], PASSAGES["P22"]],
            "a": {"display": "normal", "kind": "test", "label": "Reading A, natural pace"},
            "b": {"display": "pacer", "target": 264, "kind": "condition",
                  "label": "Reading B, with the pacer"},
            "lapses": True,
            "preset": "pacer-steadies",
            "presets": [
                {"id": "pacer-steadies", "label": "Pacer: 4 lapses became 1",
                 "wordsA": 484, "secondsA": 121, "correctA": 5, "totalA": 6,
                 "wordsB": 457, "secondsB": "103.864", "correctB": 5, "totalB": 6, "targetB": 264,
                 "lapsesA": 4, "lapsesB": 1,
                 "expect": {"drErrA": "200 wpm", "drErrB": "≈ 220.0 wpm", "drErrDiff": "≈ +20.0 wpm",
                            "drWpmB": "≈ 264.0 wpm", "drLapsesA": "4", "drLapsesB": "1"}},
                {"id": "no-change", "label": "No change: 2 lapses both times",
                 "wordsA": 484, "secondsA": "116.16", "correctA": 5, "totalA": 6,
                 "wordsB": 457, "secondsB": "109.68", "correctB": 5, "totalB": 6, "targetB": 250,
                 "lapsesA": 2, "lapsesB": 2,
                 "expect": {"drErrA": "≈ 208.3 wpm", "drErrB": "≈ 208.3 wpm", "drErrDiff": "0 wpm",
                            "drLapsesA": "2", "drLapsesB": "2"}},
            ],
        }),
        "steps_title": "Doing it again on another day",
        "steps_intro": "Five steps, about twelve minutes, with a pencil.",
        "steps": [
            ("Set the pacer to your hold target",
             "Put your current hold target in B's target box. A has no pacer: read it at your "
             "natural pace."),
            ("Read, then count, then answer",
             "After each reading, before the questions, give the lab the number of times you lost "
             "your place or re-read for no reason. Count only the ones you noticed."),
            ("Compare effective rates, then lapses",
             "Compute both effective rates and what one question is worth. Then set the two "
             "lapse counts side by side, and remember which one the pacer drove."),
            ("Note it as one comparison",
             "Write the date, the two effective rates and the two lapse counts in a log note. A "
             "pattern over several weeks says more than one pair."),
            _DAILY,
        ],
        "worked": {
            "title": "What a smaller regression share is worth, in the model",
            "intro": [
                "Fixation 225 ms, saccade 30 ms, 8 characters a step, 6 a word; regressions cut "
                "from 3/20 to 7/100 of fixations (illustrative).",
            ],
            "lines": [
                "at 3/20: 15/17 fixations, 225 ms, ≈ 266.7",
                "at 7/100: (3/4) × (100/93) = 25/31 fixations",
                "(25/31) × 255 ≈ 205.6 ms per word",
                "60,000 × 31 / 6,375 ≈ 291.8 words a minute",
            ],
            "after": [
                "About 25 words a minute, if every regression cut was a lapse and none a repair. "
                "The model already understates a regression's cost, so the true figure could be "
                "a little larger; whether any of it is available to you is what the lapse count "
                "is for.",
            ],
        },
        "quiz_title": "Repair and drift",
        "quiz": [
            {"q": "Which kind of regression can a pacer plausibly reduce?",
             "a": ["Re-reading after attention drifted off the line",
                   "Going back to fix a word that was misread",
                   "Going back when a sentence turns out to mean something else",
                   "None: a pacer changes only the rate"],
             "c": 0,
             "why": "A steady moving highlight gives the eyes somewhere to be and may reduce "
                    "drifting. A misread word or a sentence that turned needs the look back to be "
                    "understood. A pacer does more than set a rate: that is the point of counting "
                    "lapses."},
            {"q": "Reading A: 240 words a minute, 5 of 6. Reading B: 264 words a minute, 5 of 6. "
                  "What are the effective rates, and is the difference a result?",
             "a": ["200 and 220; no, it is less than one question",
                   "200 and 220; yes, B is 10% better",
                   "240 and 264; no, it is less than one question",
                   "200 and 220; yes, the lapse count confirms it"],
             "c": 0,
             "why": "240 &times; 5/6 = 200 and 264 &times; 5/6 = 220. One question at these rates "
                    "is 40 to 44 words a minute, and the difference is 20. The lapse count is a "
                    "self-report about drift, not evidence about the effective rates."},
            {"q": "In the budget, cutting regressions from 3/20 to 7/100 of fixations raises the "
                  "rate from &asymp; 266.7 to &asymp; 291.8 words a minute. What does that figure "
                  "show?",
             "a": ["What a reader will gain by training regressions away",
                   "What the model allows if the regressions cut were lapses, at illustrative "
                   "shares",
                   "The average gain measured in Rayner and colleagues' 2016 review",
                   "How much comprehension a reader loses by regressing less"],
             "c": 1,
             "why": "The shares are invented for the example and the model computes what they "
                    "imply. No study measured this gain, nothing promises it, and the model says "
                    "nothing about comprehension, which is why it matters which regressions are "
                    "cut."},
        ],
        "mistakes": [
            ("Treating every look back as wasted time",
             "The ones worth cutting come from drifting attention; the repair regressions carry "
             "comprehension, as Looking Back showed. The split is a teaching device, not a "
             "distinction the studies measured, and only you can say which of yours were which."),
            ("Reading the lapse count as a measure of regressions",
             "It counts the times you noticed losing your place. Your eyes regressed many more "
             "times than that, mostly without your noticing, and some lapses pass unnoticed too."),
            ("Crediting the pacer with B's rate",
             "B's rate was set by the pacer. The comparison that means something is effective "
             "rate, and the difference has to exceed one question to be a result."),
        ],
        "standard": (
            "Weigh a paced and an unpaced reading",
            "Given two readings with their scores and lapse counts, compute both effective rates, "
            "say whether the difference exceeds one question, and say which kind of regression a "
            "pacer can reduce and which it cannot."
        ),
        "note": (
            "Two passages, and one read first; the lab alternates the order but cannot remove it. "
            "The lapse count is your own report of what you noticed, and the budget's shares are "
            "illustrative. Neither is a measurement of your regressions, which only an eye "
            "tracker could make."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-speed-ceiling",
        "title": "The Speed Ceiling",
        "module": "The limits",
        "one_line": "Compute how many characters each glance must take in for a claimed rate, and set that against the spans.",
        "summary": (
            "Any claimed reading rate can be turned into the number of new characters each "
            "fixation would have to take in, at stated settings for a fixation, a saccade and a "
            "word. Set against how far words are identified and how far a glance reaches, the "
            "figure says which claims are within ordinary reading, which need more than a "
            "fixation identifies, and which need more than it can see at all."
        ),
        "key": [
            "needed = rate × 6 × stop / 60,000",
            "stop = fixation + saccade, in ms",
            "identification span ≈ 8 characters",
            "perceptual span ≈ 15 characters",
            "1,000 × 6 × 255 / 60,000 = 25.5",
        ],
        "key_label": "One line of arithmetic",
        "concepts_intro": (
            "The budget in Fixations and Saccades turned stops and jumps into a rate. This lesson "
            "runs it backwards: from a rate to what each stop would need."
        ),
        "concepts": [
            ("From a rate to a glance",
             "A rate fixes the time per word. Divide that by the time one fixation and its saccade "
             "take, and you have fixations per word; turn it over and multiply by six characters, "
             "and you have the characters each fixation must advance."),
            ("Two thresholds",
             "Words are identified within about 8 characters of the fixation, and the perceptual "
             "span reaches about 15 to the right (Rayner 1998). Needing more than 8 means taking "
             "in words that are not identified; needing more than 15 means taking in text that is "
             "not seen."),
            ("At these settings",
             "The verdict depends on the fixation and saccade you put in. Shorter fixations "
             "lower the figure, and so does skipping short words, which skilled readers do. Every "
             "verdict holds at the settings that produced it."),
        ],
        "read_title": "What a claimed speed would need",
        "read_intro": (
            "Begin with the warm-up reading in the lab, at your usual pace. Then put your own rate "
            "into the model, and then some claims."
        ),
        "body": [
            ("p", "Do the warm-up first, The Case for Teaching Every Child to Swim, at your usual "
                  "pace. It is logged as practice. Then put your warm-up rate into the target box "
                  "and read the two tiles: the characters each fixation had to advance, and the "
                  "verdict. For most readers it will be well inside the spans, which is as it "
                  "should be."),
            ("math", [
                "time per word = 60,000 / rate",
                "fixations per word = time per word / (fixation + saccade)",
                "characters per fixation = 6 / fixations per word",
                "so: needed = rate × 6 × (fixation + saccade) / 60,000",
            ]),
            ("p", "The <strong>double</strong> preset is a claim of 500 words a minute, about "
                  "twice an ordinary rate, at the default settings of 225 ms, 30 ms, six "
                  "characters a word and no regressions: 500 &times; 6 &times; 255 / 60,000 = "
                  "12.75 characters. The verdict is beyond the word-identification span but within "
                  "the perceptual span, at these settings: more than an average fixation "
                  "identifies, though not more than it sees."),
            ("p", "The <strong>thousand</strong> preset is 1,000 words a minute: 25.5 characters "
                  "per fixation, beyond the perceptual span. The "
                  "<strong>twenty-five-thousand</strong> preset is there for the claims far larger "
                  "than that: 25,000 words a minute needs 637.5 characters per fixation, about ten "
                  "lines of 65 characters taken in at each glance."),
            ("p", "These are verdicts at stated settings, and the settings are adjustable. Skilled "
                  "readers who reach 350 to 400 words a minute do it with shorter fixations and by "
                  "skipping short words (Rayner et al. 2016). Try it: at 350 words a minute with "
                  "the default 225 ms, a fixation must advance 8.925 characters (the tile prints "
                  "&asymp; 8.9), just past the identification span; with fixations of 190 ms, 350 &times; 6 &times; 220 / "
                  "60,000 = 7.7, inside it. Skipping is not one of the model's settings, but each "
                  "skipped word adds its characters to a step without a stop, which has the same "
                  "effect as a larger step."),
            ("p", "Settings do little for 1,000. Bringing it inside the identification span needs "
                  "fixation and saccade together under 80 ms, so fixations under 50 ms, a quarter "
                  "of the average, on every word. The tradition's answer is "
                  "that trained readers stop reading word by word and take in meaning by the "
                  "line or the page; the trainees in speed-reading courses often report that it "
                  "feels that way. The test is comprehension, and when Carver (1985) tested some "
                  "of the fastest readers he could find, speed-reading graduates among them, none "
                  "showed comprehension at rates above about 600 words a minute."),
            ("p", "What happens at 1,000 words a minute is real, and it has a name: skimming. "
                  "Skimming, Scanning and Previewing teaches it as that, with its own questions and "
                  "its own costs. The mistake is to call it reading with full comprehension."),
            ("p", "Carry this line of arithmetic with you; it settles most speed claims before any "
                  "drill. The last lesson of this course, Training the Periphery, tests a different "
                  "kind of claim: that an eye exercise makes reading faster."),
        ],
        "lab": ("readkit", {
            "mode": "eye",
            "view": "required",
            "warmup": _POOL["Q19"],
            "preset": "double",
            "presets": [
                {"id": "double", "label": "500 words a minute", "target": 500, "expect": {"eyNeeded": "12.75 characters",
                            "eyVerdict": "at these settings, beyond the word-identification span but within the perceptual span"}},
                {"id": "thousand", "label": "1,000 words a minute", "target": 1000, "expect": {"eyNeeded": "25.5 characters", "eyVerdict": "at these settings, beyond the perceptual span"}},
                {"id": "twenty-five-thousand", "label": "25,000 words a minute",
                 "target": 25000, "expect": {"eyNeeded": "637.5 characters", "eyVerdict": "at these settings, beyond the perceptual span"}},
            ],
        }),
        "steps_title": "Testing a claim on another day",
        "steps_intro": "Five steps, about eight minutes, and any claim you come across.",
        "steps": [
            ("Do the warm-up and enter your rate",
             "Read the warm-up at your usual pace, put its rate in the target box, and note the "
             "characters per fixation it needed."),
            ("Enter the claim",
             "Put the claimed rate in the target box with the default settings, and read the "
             "characters and the verdict."),
            ("Give the claim its best settings",
             "Lower the fixation to the shortest you think plausible, and see whether the verdict "
             "changes. State the verdict with the settings that produced it."),
            ("Ask what was tested",
             "If the claim comes with a comprehension figure, ask how it was measured. A claim with "
             "no questions behind it has not been tested on reading."),
            _DAILY,
        ],
        "worked": {
            "title": "A thousand words a minute",
            "intro": [
                "Fixation 225 ms, saccade 30 ms, six characters a word, no regressions.",
            ],
            "lines": [
                "needed = 1,000 × 6 × 255 / 60,000",
                "= 1,530,000 / 60,000 = 25.5 characters",
                "25.5 > 15: beyond the perceptual span",
            ],
            "after": [
                "At these settings a reader at 1,000 words a minute would have to take in 25.5 new "
                "characters at every stop, ten more than a fixation sees to the right. Shortening "
                "the stops lowers it; getting it under 8 would need fixations under 50 ms.",
            ],
        },
        "quiz_title": "Testing a claim",
        "quiz": [
            {"q": "At 225 ms fixations, 30 ms saccades, six characters a word and no regressions, "
                  "how many characters must each fixation advance at 500 words a minute?",
             "a": ["8.5", "12.75", "25.5", "11.25"],
             "c": 1,
             "why": "500 &times; 6 &times; 255 / 60,000 = 12.75. 25.5 is the figure for 1,000; "
                    "11.25 leaves out the saccade; 8.5 is the figure at about 333 words a minute."},
            {"q": "A claim needs 12.75 characters per fixation. What is the verdict at these "
                  "settings?",
             "a": ["Within the word-identification span",
                   "Beyond the perceptual span",
                   "Beyond the word-identification span but within the perceptual span",
                   "Impossible at any settings"],
             "c": 2,
             "why": "12.75 is more than the 8 characters within which words are identified and "
                    "less than the 15 of the perceptual span. It is a verdict at these settings: "
                    "shorter fixations would lower the figure."},
            {"q": "How do skilled readers at 350 to 400 words a minute fit inside the spans?",
             "a": ["They widen their perceptual span to a whole line by training",
                   "They stop making saccades and read in one sweep",
                   "They read only the first sentence of each paragraph",
                   "They make shorter fixations and skip short words"],
             "c": 3,
             "why": "Shorter stops and skipped words lower the characters each fixation must take "
                    "in. There is no evidence that the span widens to a line, saccades cannot be "
                    "avoided, and reading first sentences is skimming."},
            {"q": "What did Carver (1985) find when he tested some of the fastest readers he "
                  "could find?",
             "a": ["None showed comprehension at rates above about 600 words a minute",
                   "Speed-reading graduates comprehended well at 1,000 words a minute",
                   "Most readers could double their rate without losing comprehension",
                   "None could read faster than 300 words a minute"],
             "c": 0,
             "why": "No reader he tested comprehended above about 600 words a minute. That is a "
                    "ceiling on comprehension, not on movement: anyone can turn pages faster."},
        ],
        "mistakes": [
            ("Believing 1,000 words a minute with full comprehension is a matter of technique",
             "At an average fixation it needs 25.5 characters identified per glance, beyond even "
             "the perceptual span. Skilled readers who reach 350 to 400 words a minute do it with "
             "shorter fixations and by skipping short words, which the settings let you try; what "
             "is done at 1,000 is skimming, which the Subject teaches as skimming. Carver (1985) "
             "found no tested reader comprehending above about 600 words a minute."),
            ("Stating a verdict without its settings",
             "&ldquo;Beyond identification&rdquo; at 225 ms can be &ldquo;within&rdquo; at 190 "
             "ms. A verdict is true at the settings that produced it, and those belong in the "
             "sentence."),
            ("Testing a claim by speed alone",
             "Any reader can move their eyes across a page at 1,000 words a minute. The claim "
             "worth testing is comprehension at that rate, and the arithmetic here says what "
             "that would require of each fixation."),
        ],
        "standard": (
            "Test a speed claim",
            "Given a claimed rate and settings for the fixation, saccade, word length and "
            "regressions, compute the characters each fixation must advance and state the verdict "
            "against the identification and perceptual spans, naming the settings."
        ),
        "note": (
            "The model says what a claim would need of an average fixation, not whether a reader "
            "did it, and its thresholds are averages from studies of skilled readers. Your "
            "warm-up is one measurement, of you, on one passage."
        ),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "training-the-periphery",
        "title": "Training the Periphery",
        "module": "The limits",
        "one_line": "Time a Schulte table, and ask what getting faster at it would and would not show about reading.",
        "summary": (
            "A Schulte table is a five-by-five grid of the numbers 1 to 25, found in order with "
            "the eyes held on the centre. Speed-reading courses use it to train the periphery. "
            "You time three tables, then do a test reading, and the question the lesson leaves "
            "you with is whether the two move together over weeks, and what else would explain "
            "it if they did."
        ),
        "key": [
            "time per cell = table time / 25",
            "62 / 25 = 2.48 s; 41 / 25 = 1.64 s",
            "practice improves the practised task",
            "transfer to reading is the claim to test",
        ],
        "key_label": "A table and a test",
        "concepts_intro": (
            "This is the tradition's exercise for the periphery, done the way the tradition does "
            "it, and measured."
        ),
        "concepts": [
            ("The table",
             "Twenty-five numbers in a random grid, clicked in order from 1 to 25 while you keep "
             "your eyes as near the centre as you can. The lab times it and counts wrong clicks."),
            ("Practice and transfer",
             "Doing a task again makes you faster at that task. Whether it makes you faster at a "
             "different one, here reading, is transfer, and it has to be shown, not assumed."),
            ("Two series, side by side",
             "Table times and test effective rates, session by session over weeks, are what could "
             "show transfer. Even then, both could improve for a reason other than the table."),
        ],
        "read_title": "What a faster table would show",
        "read_intro": (
            "Do three tables in the lab, then the test reading above them. The order matters: "
            "the test should be the last thing you do."
        ),
        "body": [
            ("p", "The lab's table is 25 numbers in a random five-by-five grid. Press Start, keep "
                  "your eyes on the centre as well as you can, and click 1, 2, 3 and on to 25. "
                  "Do three tables in a row; each is timed and logged as <em>other</em>, with its "
                  "time. Then do the warm-up reading, The Piano on Fenwick Road, at your natural "
                  "pace: this one is logged as a test, so it joins your baseline and tests."),
            ("p", "The table is a staple of speed-reading courses, as a way to train what the eyes "
                  "take in away from the centre, and readers who practise it do get faster at it, "
                  "often quickly. The tradition's claim is that the wider awareness carries over "
                  "into reading, so that the eyes take in more of each line."),
            ("p", "The <strong>first</strong> preset is a reader's first table: 62 seconds, "
                  "62 / 25 = 2.48 seconds per cell. The <strong>third</strong> preset is the same "
                  "reader's third: 41 seconds, 41 / 25 = 1.64 seconds per cell. A third off the "
                  "time in three tries is the kind of gain practice brings to any new task. Each "
                  "preset draws its table from a stated seed, so the grid is always the same; the "
                  "drill gives you a fresh random one."),
            ("p", "What the faster table shows is that you got faster at finding numbers in a "
                  "grid. Practice improves the practised task. Whether it improves reading is the claim to test, and "
                  "Rayner and colleagues' 2016 review found the evidence for that kind of transfer "
                  "from eye exercises weak. Reviews of brain-training games have mostly reported "
                  "the same pattern: better at the game, little change elsewhere."),
            ("p", "You can test it on yourself. Keep doing a few tables before some of your test "
                  "readings, and write each table time beside the test's effective rate in a log "
                  "note. Over several weeks, two lines will form. If the table times fall and the "
                  "test rates stay inside your baseline range, the exercise has not transferred, "
                  "for you, so far."),
            ("p", "If both improve, that is not yet transfer either. The Daily Drill has been "
                  "running the whole time, and it trains reading directly; the passages differ "
                  "from week to week; and a reader who is keeping a careful log is also paying "
                  "more attention. The comparison that would separate them is a stretch of weeks "
                  "with the tables and a stretch without, with the Daily Drill held the same."),
            ("p", "Even the table time is not simple to read. A faster table could come from "
                  "better search, quicker clicking or more seen away from the centre, and The "
                  "Perceptual Span showed how quickly letter identification falls off a few "
                  "positions out. The time alone cannot say which; your log can say whether "
                  "reading moved."),
            ("p", "That ends How the Eyes Read: what a fixation takes in, what looking back is for, "
                  "and a line of arithmetic for any speed claim. The next course, The Inner Voice "
                  "and Flashing Words, tests the tradition's other techniques the same way, against "
                  "a control."),
        ],
        "lab": ("readkit", {
            "mode": "flash",
            "view": "schulte",
            "kind": "other",
            "warmup": PASSAGES["P11"],
            "warmup_kind": "test",
            "preset": "first",
            "presets": [
                {"id": "first", "label": "A first table: 62 seconds",
                 "seconds": 62, "errors": 0, "seed": 12345, "expect": {"flTime": "62 s", "flPerCell": "2.48 s"}},
                {"id": "third", "label": "The third table: 41 seconds",
                 "seconds": 41, "errors": 0, "seed": 2718, "expect": {"flTime": "41 s", "flPerCell": "1.64 s"}},
            ],
        }),
        "steps_title": "Doing it again on another day",
        "steps_intro": "Five steps, about ten minutes. The test reading always comes last.",
        "steps": [
            ("Three tables",
             "Do three tables in a row with your eyes on the centre, and write down the three "
             "times and the best per-cell figure."),
            ("Then the test reading",
             "Do a test reading at natural pace: the warm-up here while it lasts, then the test in "
             "the Daily Drill. Note its effective rate."),
            ("Write both in one note",
             "Add a note to your log with the date, the best table time and the test's effective "
             "rate, so that the two series can be read side by side later."),
            ("Read the two series every few weeks",
             "Ask whether the table times fell, whether the test rates left your baseline range, "
             "and what else changed in those weeks."),
            _DAILY,
        ],
        "worked": {
            "title": "First table and third",
            "intro": [
                "One reader, three tables on one day: 62 seconds for the first, 41 for the third.",
            ],
            "lines": [
                "first: 62 / 25 = 2.48 s per cell",
                "third: 41 / 25 = 1.64 s per cell",
                "change: 2.48 − 1.64 = 0.84 s per cell",
            ],
            "after": [
                "The table got about a third faster in three tries. Nothing in these figures says "
                "anything about reading; that needs the test readings beside them, over weeks.",
            ],
        },
        "quiz_title": "Practice and transfer",
        "quiz": [
            {"q": "A table took 41 seconds. What is the time per cell?",
             "a": ["1.64 s", "2.48 s", "0.61 s", "1.52 s"],
             "c": 0,
             "why": "41 / 25 = 1.64. 2.48 s is 62 / 25, the first table; 0.61 is 25 / 41, the "
                    "cells per second; 1.52 s divides by 27 instead of 25."},
            {"q": "Over six weeks your table time fell from 60 to 35 seconds and your test "
                  "effective rate rose from 230 to 260. What does this show?",
             "a": ["The table transferred to reading",
                   "Both improved, which is consistent with transfer but has other explanations",
                   "The table made reading worse",
                   "Nothing, because table times cannot be compared"],
             "c": 1,
             "why": "The Daily Drill ran through those weeks and trains reading directly, the "
                    "passages differed, and the test rise must also leave your baseline range to "
                    "count. Transfer needs a comparison with weeks without the table."},
            {"q": "What did Rayner and colleagues' 2016 review conclude about eye exercises and "
                  "reading?",
             "a": ["They reliably widen the perceptual span to a line",
                   "They make reading slower",
                   "The evidence that they transfer to reading is weak",
                   "They work for readers who practise them daily"],
             "c": 2,
             "why": "Practice improves the practised task; the evidence that it carries over to "
                    "reading is weak. The review does not say the exercises harm reading, and "
                    "there is no evidence that any training widens the span to a line."},
        ],
        "mistakes": [
            ("Believing that faster eye exercises make reading faster",
             "Practice improves the practised task; transfer to reading is the claim to test, and "
             "the evidence for it is weak (Rayner et al. 2016). A falling table time shows that "
             "you got better at tables."),
            ("Reading two rising lines as cause and effect",
             "If table times fall and test rates rise over the same weeks, the Daily Drill, the "
             "passages and your attention all changed too. Only a stretch without the tables, "
             "with everything else the same, could separate them."),
            ("Treating the table time as a reading",
             "The table is logged as other, so it never enters your baseline or tests and is not "
             "drawn in your history; its time goes in a note beside the test. A table time and a "
             "reading rate are different measurements, and only the reading is a reading."),
        ],
        "standard": (
            "Judge a transfer claim from two series",
            "Given table times and test effective rates over several sessions, say whether they "
            "support transfer to reading, and name at least two other things that could explain "
            "both improving."
        ),
        "note": (
            "The table measures finding numbers in a grid, and the test measures one reading of "
            "one passage. Transfer is a claim about weeks of both, and one day of either cannot "
            "settle it; the kit draws your test readings in the log, and the table times are "
            "yours to set beside them."
        ),
    },
]
