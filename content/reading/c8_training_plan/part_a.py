"""Course 8, lessons 1-4 -- the plan (a practice week, reading your curve) and
the test (plateaus and transfer, the full battery)."""

from reading.passages import PASSAGES, POOL

_POOL = {p["id"]: p for p in POOL}

DAILY = (
    "Then today's Daily Drill",
    "Do today's session on The Daily Drill page: the next pool passage with the "
    "pacer at your hold target, or a test at natural pace if one is due.",
)

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "a-practice-week",
        "title": "A Practice Week",
        "module": "The plan",
        "one_line": "Plan next week's practice under a time budget so that it keeps the routine and contains a test.",
        "summary": (
            "Since The Daily Drill you have kept a routine; this lesson reviews it "
            "and plans the next week. The lab adds up a week of sessions, the share "
            "of it that is a test, and whether it fits the time you have. The rules "
            "that make a week worth doing are yours to check: short sessions, most "
            "days, and a test at least every fifth session."
        ),
        "key": [
            "week = sessions × minutes, summed",
            "test share = test minutes / week",
            "a session: 10 to 15 minutes",
            "at most two timed readings a sitting",
            "a test at least every fifth session",
            "no test in the week: nothing measured",
        ],
        "key_label": "A week in six lines",
        "concepts_intro": (
            "A practice week is a budget with rules. The lab checks the budget; "
            "the rules are what this lesson is about."
        ),
        "concepts": [
            ("Practice and test are different jobs",
             "A practice reading with the pacer at your hold target trains. A test "
             "reading at natural pace, with no pacer, measures. Only tests go into "
             "the verdict, so a week of practice alone, however long, ends with "
             "nothing new known about your reading."),
            ("A session is limited by attention",
             "The routine's ten to fifteen minutes is not a minimum to beat. Past "
             "the point where attention holds, a reading practises drifting, and "
             "the attention tick after each practice reading is how you find that "
             "point for yourself."),
            ("Most days, not one day",
             "Readings taken in one sitting share that sitting's conditions: the "
             "same tiredness, the same hour, the same mood. Five short sessions "
             "give the log five days and five chances to adjust the target; one "
             "long Saturday gives it one day, measured five times."),
        ],
        "read_title": "Reviewing the routine, then planning the week",
        "read_intro": (
            "Start from what you did, then write down what you will do, and check "
            "the plan against the rules before you check it against the clock."
        ),
        "body": [
            ("p", "Begin with the warm-up above the lab: a test reading of a passage "
                  "about salt, at natural pace with no pacer, then its six questions. "
                  "It goes into your log as a test, so this week begins with a "
                  "measurement, and the next lesson reads it beside your earlier ones."),
            ("p", "Then look back. Since The Daily Drill the routine has been: ten to "
                  "fifteen minutes a day; one pool passage with the pacer at your "
                  "hold target; every fifth session a test at natural pace; the target "
                  "raised by about 5% after three holds in a row and lowered by the "
                  "same after two misses; at most two timed readings in a sitting; "
                  "and, when your attention left the text, a shorter session rather "
                  "than a slower pacer. Open your log and count last week's days with "
                  "a session, and the sessions that were tests."),
            ("p", "A week worth doing meets four rules. The first three are the "
                  "routine's; the fourth is the clock's."),
            ("ul", [
                "Sessions of ten to fifteen minutes, with at most two timed readings in each.",
                "A session on most days: five or more in the week.",
                "A test reading at least every fifth session, at natural pace with no pacer.",
                "A total inside the time you actually have.",
            ]),
            ("p", "The lab takes the week as rows, each a kind of session with how "
                  "many and how long, and adds them up: the minutes in the week, the "
                  "share of those minutes that is the test session, and whether the "
                  "total fits your budget. It checks the arithmetic and the fourth "
                  "rule only. The other three are yours to check, and the presets are "
                  "chosen so that the tiles look fine on weeks that break them."),
            ("p", "The preset fifteen-a-day keeps all four: five fifteen-minute "
                  "sessions of pacer practice and two fifteen-minute sessions that are "
                  "tests. That is 5 × 15 + 2 × 15 = 105 minutes against a budget of "
                  "120, so it fits with 15 to spare. The test sessions are 30 of the "
                  "105 minutes, and because every session is the same length the "
                  "share of minutes is the share of sessions: 2/7, about 28.6%."),
            ("p", "The preset weekend-only spends more: two sixty-minute sittings, "
                  "one of them opening with a test, 2 × 60 = 120 minutes, exactly the "
                  "budget, and half of it the test session. Every tile looks generous. "
                  "It breaks two rules all the same. An hour is four to six times the "
                  "routine's session, so most of each sitting comes after attention "
                  "has started to leave the text; and five days of the seven are "
                  "empty, so every reading of the week shares one day's conditions."),
            ("p", "The preset all-sprints is seven fifteen-minute sessions of sprints "
                  "above comfort: 7 × 15 = 105 minutes, the same total as "
                  "fifteen-a-day, and the test-share tile reads no test in the week. "
                  "At the end of it you will know how the sprints felt and nothing "
                  "about whether your reading changed, because the verdict uses test "
                  "readings and there are none. Sprints Above Comfort showed that a "
                  "sprint's after-effect is one reading in any case."),
            ("p", "The idea under the routine has a name. Ericsson, Krampe and "
                  "Tesch-Römer (1993), in a study of musicians, called it deliberate "
                  "practice: practice designed to improve one thing, at the edge of "
                  "what you can do, with knowledge of the result after each attempt. "
                  "The pacer at your hold target is the edge and the six questions are "
                  "the result. How much of expert performance such practice explains "
                  "is contested, and their study was of music, not reading; the "
                  "routine borrows its shape, not a promise."),
            ("p", "What a week of practice can be expected to give is modest. The "
                  "research finds modest rate gains with comprehension held; the large "
                  "savings are in Skimming, Scanning and Previewing and in Words, "
                  "Knowledge and Difficulty. A good week can therefore include a "
                  "deliberate skim of something you would otherwise have read through, "
                  "written as its own row."),
            ("p", "When your week is written, the button under the lab saves it to "
                  "your log as an entry of its own, so that next week's review starts "
                  "from what you planned as well as what you did. The next lesson, "
                  "Reading Your Curve, takes the tests that week produces and asks the "
                  "question the plan exists for: has anything changed?"),
        ],
        "lab": ("readkit", {
            "mode": "log",
            "view": "plan",
            "warmup": PASSAGES["P49"],
            "warmup_kind": "test",
            "preset": "fifteen-a-day",
            "presets": [
                {"id": "fifteen-a-day", "label": "Fifteen a day, two tests",
                 "rows": [{"drill": "pacer practice", "sessions": 5, "minutes": 15},
                          {"drill": "test session", "sessions": 2, "minutes": 15}],
                 "test": "test session", "budget": 120,
                 "expect": {"lgWeekMinutes": "105 min", "lgTestShare": "2/7 ≈ 28.6%", "lgFits": "fits, 15 min to spare"}},
                {"id": "weekend-only", "label": "Two hours at the weekend",
                 "rows": [{"drill": "test session", "sessions": 1, "minutes": 60},
                          {"drill": "long practice", "sessions": 1, "minutes": 60}],
                 "test": "test session", "budget": 120,
                 "expect": {"lgWeekMinutes": "120 min", "lgTestShare": "1/2 = 50%", "lgFits": "fits, 0 min to spare"}},
                {"id": "all-sprints", "label": "Sprints every day, no test",
                 "rows": [{"drill": "sprints", "sessions": 7, "minutes": 15}],
                 "test": "test session", "budget": 120,
                 "expect": {"lgWeekMinutes": "105 min", "lgTestShare": "no test in the week", "lgFits": "fits, 15 min to spare"}},
            ],
            "panel_title": "A week of practice, added up",
            "panel_intro": (
                "A stated plan: the week as you type it, one row per kind of session. "
                "The tiles add up its minutes, the share that is the test session, "
                "and whether it fits your budget. Session length, spacing and what a "
                "session holds are for you to check against the routine's rules."
            ),
        }),
        "steps_title": "Planning a week",
        "steps_intro": "Do this at the start of each week, in this order.",
        "steps": [
            ("Begin with a test reading",
             "Take a test at natural pace with no pacer, from the Daily Drill's test "
             "box, so that the week starts from a measurement."),
            ("Review last week against the rules",
             "From your log, count the days with a session, the sessions that were "
             "tests, and the practice readings where your attention left the text."),
            ("Write the week as rows",
             "One row per kind of session: what it is, how many, how many minutes "
             "each. Type as the budget the minutes you truly have, not the minutes "
             "you would like to have."),
            ("Check the three rules the lab cannot",
             "Sessions of ten to fifteen minutes with at most two timed readings; "
             "five or more days; a test at least every fifth session. Then save the "
             "plan to your log."),
            DAILY,
        ],
        "worked": {
            "title": "The fifteen-a-day week",
            "intro": [
                "Five sessions of pacer practice and two test sessions, every one "
                "fifteen minutes, against a budget of 120 minutes.",
            ],
            "lines": [
                "pacer practice   5 × 15 =  75 min",
                "test session     2 × 15 =  30 min",
                "week                       105 min",
                "test share   30 / 105 = 2/7, about 28.6%",
                "budget       120 − 105 = 15 min to spare",
            ],
            "after": [
                "The arithmetic says the week fits. The rules say more: every session "
                "is within the routine's ten to fifteen minutes, there are seven days "
                "with a session, and two of the seven are tests, more often than the "
                "routine's one in five, which costs nothing but a little practice.",
            ],
        },
        "quiz_title": "Check a week",
        "quiz": [
            {"q": "A week is seven fifteen-minute sessions, all pacer practice at the "
                  "hold target. What has it told you about whether your reading has "
                  "changed?",
             "a": ["Nothing: the verdict uses test readings, and the week has none",
                   "Seven readings' worth, enough for a median of three",
                   "Enough, because the hold target is the same thing as a change",
                   "Half a verdict, which a second such week completes"],
             "c": 0,
             "why": "Practice readings are paced, so their rate is the pacer's "
                    "setting; the verdict uses tests only. The hold target tracks the "
                    "practice, not your unpaced reading, and no number of practice "
                    "weeks adds up to a test."},
            {"q": "Rows: pacer practice 4 × 12, test session 1 × 12, own text 2 × 15. "
                  "What does the lab print for the week and the test share?",
             "a": ["90 min; 1/7, about 14.3%",
                   "90 min; 2/15, about 13.3%",
                   "87 min; 2/15, about 13.8%",
                   "90 min; 1/5 = 20%"],
             "c": 1,
             "why": "48 + 12 + 30 = 90 minutes, and the test is 12 of them: "
                    "12 / 90 = 2/15. One session in seven would be the share of "
                    "sessions, but the sessions are not all the same length, and the "
                    "lab counts minutes."},
            {"q": "The weekend-only week fits its budget exactly and half of its "
                  "minutes are a test session. Which rule does it break?",
             "a": ["None: the tiles show it fits",
                   "The budget rule, because it uses all 120 minutes",
                   "Session length and spacing: two hour-long sittings and five empty days",
                   "The test rule, because no more than a fifth may be testing"],
             "c": 2,
             "why": "A week that uses the whole budget still fits it. The test rule "
                    "asks for a test at least every fifth session, so more testing "
                    "breaks nothing. What the tiles cannot see is that each sitting is "
                    "four to six times the routine's length and that five days have "
                    "no session."},
            {"q": "Your attention tick said yes after three of last week's five practice "
                  "readings. What does the routine say to change?",
             "a": ["Lower the pacer target by 5%",
                   "Add a sixth session to make up for it",
                   "Make every session a test until it stops",
                   "Shorten the sessions and keep the pacer where it is"],
             "c": 3,
             "why": "The routine lowers the target after two misses on the questions, "
                    "not after lapses of attention; a lapse is answered by a shorter "
                    "session. More sessions or more tests leave the long, drifting "
                    "sessions as they were."},
        ],
        "mistakes": [
            ("More drills means more progress",
             "A week of seven sprint sessions has the same 105 minutes as "
             "fifteen-a-day and no test in it, so at its end nothing has been "
             "measured; a week of two hour-long sittings has more minutes and spends "
             "most of them after attention has gone, practising drifting. Progress "
             "is what the tests show, and they can show it only when there are tests "
             "and the practice between them is at a pace you understand."),
            ("Treating the budget as a target",
             "The budget is the most time you have, not the amount to use. "
             "Weekend-only fills its 120 minutes exactly and breaks the session rule; "
             "fifteen-a-day leaves 15 minutes spare and breaks nothing. Spare minutes "
             "are not a failure of the plan."),
            ("Taking a test with the pacer on",
             "A test is a reading at natural pace with no pacer. With the pacer on, "
             "the rate is the pacer's setting, and the reading measures how well you "
             "followed it rather than how you read, which is why the Daily Drill's "
             "test box turns the pacer off."),
        ],
        "standard": (
            "Finish when you can plan a week and find the rule a bad one breaks.",
            "Given a budget, write a week of rows that meets the four rules: sessions "
            "of ten to fifteen minutes with at most two timed readings, five or more "
            "days, a test at least every fifth session, and a total inside the "
            "budget. Given an unbalanced week, name the rule it breaks and the figure "
            "that shows it."
        ),
        "note": (
            "The lab adds up a plan. It cannot tell whether you will keep it, and it "
            "cannot see how long a session really is, how the days are spread, or "
            "what a row holds beyond its name. The routine's numbers are the "
            "Subject's choices, borrowed in shape from the research on deliberate "
            "practice, not measured for reading."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "reading-your-curve",
        "title": "Reading Your Curve",
        "module": "The plan",
        "one_line": "Decide from a log whether your effective rate has changed, by the median of your last three tests against your baseline range.",
        "summary": (
            "A log of readings draws a curve, and a curve invites you to look at its "
            "highest point. The Subject's rule looks elsewhere: the median of the last "
            "three tests against the range of the baselines. The lab applies the rule "
            "to your own log or to three example logs, and leaves practice readings "
            "out of the verdict."
        ),
        "key": [
            "range: lowest to highest baseline",
            "evidence: median of last 3 tests > range",
            "one test above: about 1 time in 4",
            "practice readings are not counted",
            "every figure is an effective rate",
        ],
        "key_label": "The rule in five lines",
        "concepts_intro": (
            "Your log already holds the answer to whether anything has changed. The "
            "rule says which entries to read, and which one to stop looking at."
        ),
        "concepts": [
            ("The best session is selected",
             "Among a dozen readings the highest is high partly because it was picked "
             "for being high. Some of its height is that day's luck, and the next "
             "reading will most likely fall back toward the rest."),
            ("A median of three resists one day",
             "The median of three readings is the middle one, so a single unusually "
             "good or bad day cannot move it past the other two. A change that lifts "
             "the median has shown up on at least two days."),
            ("Only like is compared with like",
             "Baselines and tests are readings at natural pace, with questions, and "
             "their effective rates are the curve. Practice is paced, a condition is "
             "a technique on trial, and a skim measures something else; the verdict "
             "leaves all of them out."),
        ],
        "read_title": "What the curve says, and what it does not",
        "read_intro": (
            "Three example logs, each with the same baselines, show the three things "
            "a curve can be: a change, a lucky day, and a faster page-turner."
        ),
        "body": [
            ("p", "The warm-up above the lab is a test reading of a passage about "
                  "rainbows, at natural pace, with six questions. Do it first, so that "
                  "your own curve ends with today. The passage comes from the standard "
                  "band of the practice pool, the band of your baselines, so it can "
                  "stand beside them on the chart."),
            ("p", "The lab reads your log and keeps only the baseline and test "
                  "readings that had questions. It puts every baseline first and the "
                  "tests after them, sets the box for the number of baselines, and "
                  "prints the median of the baselines, the median of the last three "
                  "readings, the latest effective rate and the verdict. Measure Your "
                  "Reading took three baselines; if you added a fourth, the range is "
                  "built from all four. Practice readings are drawn "
                  "as a lighter dashed line and enter no tile; notes and every other "
                  "entry are listed, greyed, under the chart. With an empty log, the "
                  "boxes hold one of three example logs."),
            ("p", "The rule is the one from One Reading Is One Measurement. The "
                  "baselines give a range: how far apart your readings fall with "
                  "nothing changed. A single test above the top of that range happens "
                  "about one time in four by chance, because a fourth reading from "
                  "the same reader is the highest of the four about one time in four. "
                  "A change is evidence when the median of the last three tests is "
                  "above the range."),
            ("p", "Take real-gain. Its baselines are 238, 245 and 251 effective words "
                  "a minute: a median of 245, and a range from 238 to 251, 13 wide "
                  "with nothing changed. Its tests are 262, 270 and 281. Each is above "
                  "251, but the verdict does not rest on the 281: the median of the "
                  "three is 270, which is 19 above the top of the range, and the lab "
                  "prints above the baseline range on the median of the last three "
                  "tests. That is the Subject's evidence of a change. The log also "
                  "holds four practice readings at the pacer, drawn lighter, with "
                  "effective rates from 240 to 290; they count for nothing here, "
                  "because the pacer set their rate."),
            ("p", "Now noise: the same baselines, and tests of 244, 262 and 239. The "
                  "262 is the best session in the log, 11 above the top of the range, "
                  "and a reader who stopped there would announce a new level. The "
                  "median of the three is 244, inside the range, and the latest, 239, "
                  "is inside too, so the lab prints inside the baseline range. The "
                  "262 is the one-in-four day."),
            ("p", "Then rate-only. Its tests were read at 354, 360 and 357 words a "
                  "minute, against baselines read at 251 to 294, with four questions "
                  "right each time instead of five or six. The rate rose by sixty words "
                  "a minute or more; the effective rates are 236, 240 and 238, with a "
                  "median of 238, the bottom of the range, and the verdict is inside. "
                  "A curve of rate would have called this a gain. It is a reader "
                  "turning pages faster and understanding less, which is why every "
                  "figure on this curve is an effective rate."),
            ("p", "Which entries does the verdict leave out? Practice at the pacer, "
                  "because its rate was set for you. The conditions of the compare "
                  "drills in earlier courses, because each was a technique on trial. "
                  "Skims, scans and recall, because they measure something else. And "
                  "any reading without questions, because a rate with no "
                  "comprehension has no effective rate. What is left should be a short "
                  "list: with a test every fifth session, about one a week."),
            ("p", "One thing the rule cannot see is the passage. A test on a harder "
                  "passage reads lower for that reason alone, and the practice pool "
                  "grows harder toward its end. If your recent tests fall just as the "
                  "pool reaches its hard passages, read the fall as the passages until "
                  "tests on standard ones say otherwise; today's warm-up was a "
                  "standard one for that reason."),
            ("p", "When you have read your verdict, write it in the note box under the "
                  "lab with the date, so that the log carries what you concluded as "
                  "well as what you measured. The next lesson, Plateaus and Transfer, "
                  "asks what a curve that has stopped rising means, and tries your "
                  "practice on a kind of text it never gave you."),
        ],
        "lab": ("readkit", {
            "mode": "log",
            "view": "history",
            "warmup": _POOL["Q16"],
            "warmup_kind": "test",
            "preset": "real-gain",
            "presets": [
                {"id": "real-gain", "label": "Tests 262, 270, 281",
                 "entries": [("285.6", 5, 6), (294, 5, 6), (251, 6, 6),
                             ("314.4", 5, 6), (324, 5, 6), (281, 6, 6)],
                 "practice": [(330, 5, 6), (336, 5, 6), (348, 5, 6), (360, 4, 6)],
                 "expect": {"lgSessions": "6", "lgBaseMedian": "245 wpm", "lgRecentMedian": "270 wpm", "lgLatestErr": "281 wpm",
                            "lgVerdict": "above the baseline range on the median of the last three tests"}},
                {"id": "noise", "label": "Tests 244, 262, 239",
                 "entries": [("285.6", 5, 6), (294, 5, 6), (251, 6, 6),
                             ("292.8", 5, 6), ("314.4", 5, 6), ("286.8", 5, 6)],
                 "expect": {"lgBaseMedian": "245 wpm", "lgRecentMedian": "244 wpm", "lgLatestErr": "239 wpm",
                            "lgVerdict": "inside the baseline range"}},
                {"id": "rate-only", "label": "Faster, fewer right",
                 "entries": [("285.6", 5, 6), (294, 5, 6), (251, 6, 6),
                             (354, 4, 6), (360, 4, 6), (357, 4, 6)],
                 "expect": {"lgBaseMedian": "245 wpm", "lgRecentMedian": "238 wpm", "lgLatestErr": "238 wpm",
                            "lgVerdict": "inside the baseline range"}},
            ],
            "panel_title": "Your curve, by the Subject's rule",
            "panel_intro": (
                "Your measurement, from your log: baseline and test readings with "
                "questions only, as effective rates, every baseline in the range. "
                "Until your log has some, the boxes hold an example log. "
                "Nothing leaves your browser."
            ),
        }),
        "steps_title": "Reading your curve",
        "steps_intro": "Do this once a week, after the week's test.",
        "steps": [
            ("Take the week's test",
             "A reading at natural pace with no pacer, with its questions, from the "
             "Daily Drill's test box or a lesson's warm-up."),
            ("Open your log and strike what does not count",
             "On this page, check that the counted sessions are your baselines and "
             "tests; practice, conditions, skims and readings without questions are "
             "greyed, and stay out."),
            ("Read the median, not the peak",
             "Find the median of the last three tests and set it against the "
             "baseline range. Then give the verdict in the Subject's three tiers: "
             "inside, above once, or above on the median of three."),
            ("Write the verdict down",
             "Add a note with the date, the median and the verdict, and whether the "
             "recent tests were on harder passages."),
            DAILY,
        ],
        "worked": {
            "title": "The real-gain log",
            "intro": [
                "Three baselines and three tests, as effective rates in words a "
                "minute.",
            ],
            "lines": [
                "baselines   238   245   251    range 238 to 251",
                "tests       262   270   281",
                "median of the last three tests = 270",
                "270 − 251 = 19 above the top of the range",
                "verdict: above, on the median of three",
            ],
            "after": [
                "Had the tests been 244, 262 and 239, the median would be 244 and the "
                "verdict inside, whatever the 262 felt like on the day.",
            ],
        },
        "quiz_title": "Give the verdict",
        "quiz": [
            {"q": "Baselines 240, 246 and 252; then tests 250, 249 and 258, the 258 "
                  "the latest. What is the verdict by the Subject's rule?",
             "a": ["A change, because the latest test is above the range",
                   "No evidence of a change: the median, 250, is inside the range, and the 258 is above it once",
                   "A change, because two of the three tests are above the baseline median",
                   "A fall, because 249 is below the latest test"],
             "c": 1,
             "why": "The median of 250, 249 and 258 is 250, inside 240 to 252. The 258 "
                    "is above the top once, which happens about one time in four with "
                    "nothing changed. The baseline median and the order of the tests "
                    "are not what the rule compares."},
            {"q": "Which of these entries does the verdict count?",
             "a": ["A pacer practice reading at the hold target, five of six right",
                   "A skim of a passage for its gist",
                   "A natural-pace test reading with six questions",
                   "A pasted text of your own, timed, with no questions"],
             "c": 2,
             "why": "Only baseline and test readings with questions count. The pacer "
                    "set the practice reading's rate, a skim measures something else, "
                    "and a reading with no questions has no effective rate."},
            {"q": "In the rate-only log, test rates rose from about 290 to about 357 words a minute, "
                  "and your score fell from five or six right to four. What does the "
                  "curve of effective rate show?",
             "a": ["A gain of about 67 words a minute",
                   "A fall, because comprehension fell",
                   "Nothing, because rate and comprehension must be judged separately",
                   "No change: 357 × 4/6 = 238, inside a range of 238 to 251"],
             "c": 3,
             "why": "The effective rate is rate times comprehension, and 238 sits in "
                    "the range. The rate alone shows a gain that the questions take "
                    "back; it is not a fall either, because 238 is not below 238."},
            {"q": "Why does the rule use the median of the last three tests rather "
                  "than the best test?",
             "a": ["The best is picked for being high, and one lucky day cannot move a median of three",
                   "The median is always lower than the best, so the rule is cautious",
                   "The best test is usually a practice reading",
                   "The lab cannot find the best test in a log"],
             "c": 0,
             "why": "Selecting the highest reading selects that day's luck along with "
                    "it. The median can equal the best when the tests agree, so it is "
                    "not always lower, and a practice reading is never a test."},
        ],
        "mistakes": [
            ("My best session is my new level",
             "The best session in a log is picked for being high, so part of its "
             "height is that day's luck. In the noise log the best test is 262, 11 "
             "above the range, and the median of the three tests is 244, inside it: "
             "one test above the range happens about one time in four with nothing "
             "changed. The honest comparison is the median of the last three tests "
             "against the baseline range."),
            ("Counting practice readings in the curve",
             "A practice reading's rate is close to the pacer's setting, so a curve "
             "that includes practice shows how fast the pacer was set. In real-gain "
             "the practice readings are read at 330 to 360 words a minute, faster "
             "than every test; the lab draws them lighter and leaves them out of "
             "every tile."),
            ("Reading a curve of rate",
             "In rate-only the rate went up by sixty words a minute or more and the "
             "effective rate stayed at 236 to 240, inside the range. A curve of rate "
             "cannot tell a faster reader from a faster page-turner, which is why the "
             "lab's curve is of effective rate."),
        ],
        "standard": (
            "Finish when you can read a log and give its verdict.",
            "Given a log of baselines, tests and other entries, strike the entries "
            "that do not count and say why, compute the baseline range and the median "
            "of the last three tests, and state the verdict in the Subject's three "
            "tiers."
        ),
        "note": (
            "The rule is a rule of thumb for one reader's log, not a statistical "
            "test: three baselines give a rough range, and a median of three is still "
            "a small sample. It cannot see the passages, so a run of tests on harder "
            "texts reads lower for that reason alone. What it does well is refuse to "
            "be impressed by one day."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "plateaus-and-transfer",
        "title": "Plateaus and Transfer",
        "module": "The test",
        "one_line": "Read a dense argument, a kind of text you have not practised, and set its effective rate beside your baseline range and your recent tests.",
        "summary": (
            "Gains made on the practice passages may or may not carry to other kinds "
            "of text. The drill is one timed reading of a hard argument with six "
            "questions; you then set its effective rate beside the baseline range and "
            "the median of your recent tests. A first reading of a new kind has no "
            "baseline of its own, so the comparison tells you what to measure next, "
            "not what you have become."
        ),
        "key": [
            "transfer: a gain that shows on new text",
            "a new kind of text has no baseline yet",
            "plateau: the practice stopped asking",
            "compare effective rate, not rate",
        ],
        "key_label": "Transfer in four lines",
        "concepts_intro": (
            "Practice improves what it practises. The open question is how far beyond "
            "that it reaches, and a first reading of a new kind of text is where you "
            "start to find out."
        ),
        "concepts": [
            ("Transfer",
             "A gain transfers when it shows on material you did not practise on. "
             "Your tests were already on fresh pool passages, which is a short step; "
             "this lesson takes a longer one, to a kind of text the pool did not "
             "contain."),
            ("A plateau has more than one cause",
             "Weeks of tests at the same level can mean the practice has stopped "
             "asking for more, or that the gains belonged to the practice material. "
             "They call for different answers, and a reading on a new kind of text "
             "helps tell them apart."),
            ("One reading, no baseline",
             "Your baselines were on standard narrative and expository passages. A "
             "hard argument has never been measured for you before today, so today's "
             "reading is the first of its kind, not a test against a baseline of its "
             "kind."),
        ],
        "read_title": "A new kind of text, read cold",
        "read_intro": (
            "One reading of an argument, then three figures side by side: today's, "
            "your baseline range, and your recent tests."
        ),
        "body": [
            ("p", "The drill is one reading of In Praise of Maintenance, an argument "
                  "of 389 words written at the hard band, the kind of prose the "
                  "practice pool did not give you: long sentences, an objection "
                  "answered, a claim built across paragraphs. Read it at your natural "
                  "pace with no pacer, then answer the six questions. It is logged as "
                  "other, not as a test, for the reason this lesson is about: it "
                  "belongs to no series yet, and as a test it would pull down the "
                  "median of your tests on standard passages."),
            ("p", "Then set three figures side by side: the effective rate you just "
                  "measured, your baseline range, and the median of your last three "
                  "tests. The drill's tiles give all three: when you score the reading, "
                  "the lab fills the baseline range and the recent test median from "
                  "your log, the same figures as on the Reading Your Curve page, and "
                  "sets today's effective rate against each before you decide "
                  "anything."),
            ("p", "Suppose your recent test median is 270 effective words a minute "
                  "against a baseline range of 238 to 251, a change by the Subject's "
                  "rule, and suppose the tests have stayed near 270 for some weeks. "
                  "That is a plateau, and the natural reading of it, that this is your "
                  "limit, is the least informative one. A plateau often means the "
                  "practice has stopped asking for more: the same target, the same "
                  "kind of passage, comfortably held. It can also mean that what "
                  "improved was reading the practice material, and an unpractised kind "
                  "of text is how you tell those apart."),
            ("p", "The preset transfers is that reader on the argument: 389 words in "
                  "97.25 seconds, 240 words a minute, all six questions right, an "
                  "effective rate of 240. That is inside the old baseline range and 30 "
                  "below the recent median of 270. It is slower than the practised "
                  "kind, as harder text is for everyone, and comprehension held. It is "
                  "consistent with some of the gain carrying over, and also with none: "
                  "without a reading of this kind from before the practice, one "
                  "reading cannot say which."),
            ("p", "The preset does-not is the other common result: the same passage in "
                  "77.8 seconds, 300 words a minute, the practised pace kept up, with "
                  "four questions right and an effective rate of 200, 38 below the "
                  "bottom of the baseline range. The rate carried over; the "
                  "understanding did not. On effective rate, the figure to compare, "
                  "this reading is the rate-only log of Reading Your Curve in a single "
                  "session."),
            ("p", "Two things this comparison cannot separate. The argument is harder "
                  "than the passages of your baselines, and it is a different kind of "
                  "text. Both lower a first reading, and one passage cannot tell you "
                  "how much of the gap is each. What it can tell you is whether the "
                  "practised pace survived contact with a text that asked more of you."),
            ("p", "The wider evidence points the same way. Practice generally "
                  "improves the practised task more than tasks that only resemble it; "
                  "Rayner and colleagues (2016) found the evidence weak that eye "
                  "exercises carry over to reading, and the brain-training games have "
                  "met the same difficulty in general. The research on reading "
                  "practice itself finds modest rate gains with comprehension held. "
                  "Ericsson, Krampe and Tesch-Römer (1993) described deliberate "
                  "practice as practice at the edge of what you can do, which is the "
                  "first thing to check when a curve goes flat."),
            ("p", "So the reading tells you where to look. If it went like does-not, "
                  "practise on that kind of text: paste arguments you have not read "
                  "into the Daily Drill's own-text box and read them with the pacer "
                  "below your hold target, raising it once you can state each one's "
                  "claim and its answer to an objection afterwards. If it went like "
                  "transfers, the plateau is more likely the practice: check it against "
                  "the routine. Has the target been raised after three holds, or has it "
                  "sat where it was comfortable for weeks? If the routine has quietly "
                  "stopped asking for more, restart it."),
            ("p", "The next lesson, The Full Battery, sets your effective rate beside "
                  "the other three things the Subject has measured, and asks which of "
                  "them have moved."),
        ],
        "lab": ("readkit", {
            "mode": "drill",
            "view": "single",
            "passage": PASSAGES["P47"],
            "display": "normal",
            "kind": "other",
            "vsLog": True,
            "preset": "transfers",
            "presets": [
                {"id": "transfers", "label": "240 words a minute, 6 of 6",
                 "seconds": "97.25", "correct": 6, "total": 6,
                 "baseLo": 238, "baseHi": 251, "recent": 270,
                 "expect": {"drWpm": "240 wpm", "drComp": "1 = 100%", "drErr": "240 wpm",
                            "drVsBase": "inside the baseline range", "drVsRecent": "−30 wpm"}},
                {"id": "does-not", "label": "300 words a minute, 4 of 6",
                 "seconds": "77.8", "correct": 4, "total": 6,
                 "baseLo": 238, "baseHi": 251, "recent": 270,
                 "expect": {"drWpm": "300 wpm", "drComp": "2/3 ≈ 66.7%", "drErr": "200 wpm",
                            "drVsBase": "below the baseline range", "drVsRecent": "−70 wpm"}},
            ],
            "panel_title": "A first reading of an argument",
            "panel_intro": (
                "Your measurement: one timed reading at natural pace, scored by its six "
                "questions; one question is about 16.7 points. Scoring it fills your "
                "baseline range and recent test median from your log, as on Reading "
                "Your Curve. Before you read, the boxes hold a worked example: a range "
                "of 238 to 251 and a recent median of 270."
            ),
        }),
        "steps_title": "Testing for transfer",
        "steps_intro": "Use this whenever your tests have stayed level for some weeks.",
        "steps": [
            ("Choose a kind you have not practised",
             "An argument, a contract, the discussion section of a paper: a text you "
             "have never read, of a kind the practice did not give you."),
            ("Read it once, at natural pace",
             "No pacer, and no going back to it afterwards; a second reading measures "
             "memory. Answer the questions, or with your own text write down its "
             "three main points and then check them."),
            ("Set three figures side by side",
             "Today's effective rate, your baseline range and the median of your last "
             "three tests; the lab fills the last two from your log."),
            ("Decide what to measure next",
             "If the rate held and the understanding did not, practise on that kind; "
             "if both held, look at the practice itself and find the hold target "
             "again. Write which in a note."),
            DAILY,
        ],
        "worked": {
            "title": "Two readings of the argument",
            "intro": [
                "389 words, against baselines of 238 to 251 and a recent test median "
                "of 270.",
            ],
            "lines": [
                "transfers: 389 × 60 / 97.25 = 240 a minute",
                "           240 × 6/6 = 240 effective",
                "does-not:  389 × 60 / 77.8 = 300 a minute",
                "           300 × 4/6 = 200 effective",
                "240: inside the range, 30 below recent",
                "200: 238 − 200 = 38 below the range",
            ],
            "after": [
                "The faster reading is the worse one. Rate carried over in does-not; "
                "understanding did not, and effective rate is the figure that shows it.",
            ],
        },
        "quiz_title": "What one reading can show",
        "quiz": [
            {"q": "Your recent test median is 270 and your baseline range 238 to 251. "
                  "On a dense argument you have never practised, your effective rate "
                  "is 245. What can you conclude?",
             "a": ["The practice transferred fully, since 245 is inside the baseline range",
                   "The practice did not transfer, since 245 is below 270",
                   "That this kind of text now has a first reading; whether the gain carried needs more readings of the kind",
                   "Your reading has fallen by 25 words a minute"],
             "c": 2,
             "why": "The argument is harder than the baseline passages and of a "
                    "different kind, and there is no reading of it from before the "
                    "practice. Being below 270 or inside 238 to 251 compares it with "
                    "readings of other texts, so neither settles transfer."},
            {"q": "389 words in 97.25 seconds with 5 of 6 right. What is the effective "
                  "rate?",
             "a": ["240 words a minute",
                   "200 words a minute",
                   "288 words a minute",
                   "about 233.4 words a minute"],
             "c": 1,
             "why": "389 × 60 / 97.25 = 240 words a minute, and 240 × 5/6 = 200. "
                    "240 is the rate before the questions, and 288 multiplies by 6/5 "
                    "instead of 5/6."},
            {"q": "Why is the argument logged as other rather than as a test?",
             "a": ["It is a first reading of a kind with no baseline, and as a test it would pull down the median of tests on standard passages",
                   "Arguments cannot be scored with questions",
                   "Readings logged as other count double in the verdict",
                   "Tests must be read with the pacer"],
             "c": 0,
             "why": "The verdict compares tests with baselines on the same kind of "
                    "passage. The argument has six questions like any other passage, "
                    "other entries do not count at all, and a test is read without "
                    "the pacer."},
            {"q": "In does-not the rate is 300 words a minute and the score 4 of 6. "
                  "What carried over from the practice?",
             "a": ["Both rate and understanding",
                   "Neither, because 300 is below nothing in the log",
                   "Understanding, but not rate",
                   "The rate, but not the understanding: an effective rate of 200 is below the range"],
             "c": 3,
             "why": "300 is the practised pace, so the rate carried; 300 × 4/6 = 200 is "
                    "below the bottom of the baseline range, 238, so the understanding "
                    "did not come with it."},
        ],
        "mistakes": [
            ("A plateau means I have reached my limit",
             "A plateau often means the practice has stopped asking for more, or that "
             "the gains were specific to the practice material. A new kind of text "
             "tells which: the reader in does-not kept the practised rate of 300 on "
             "the argument and lost two questions, a gain tied to the practice "
             "material, and the reader in transfers held comprehension at a slower "
             "rate, which points back at the practice."),
            ("Treating a first reading as a failed test",
             "An effective rate of 240 on a hard argument against a recent median of "
             "270 on standard passages is not a fall. It is the first reading of a "
             "kind that has no baseline, on a harder text, and it starts a series "
             "rather than ending one."),
            ("Comparing a rate with an effective rate",
             "300 words a minute on the argument looks like a gain over a recent "
             "median of 270, but 270 is an effective rate. Multiplied by 4/6, the 300 "
             "is 200, which is below the range."),
        ],
        "standard": (
            "Finish when you can say whether practice transferred, and why one reading cannot settle it.",
            "Given an effective rate on a new kind of text, a baseline range and a "
            "recent test median, say whether the reading is consistent with the "
            "practice carrying over, name the two things the comparison cannot "
            "separate, the kind of text and its difficulty, and say what further "
            "readings would settle it."
        ),
        "note": (
            "One passage, one day, and a passage harder than your baselines: this "
            "drill cannot separate the kind of text from its difficulty. The lab's "
            "comparison with your log is only as good as the log: with fewer than "
            "three baselines it gives no verdict. What the reading starts is a "
            "series on a new kind of text."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-full-battery",
        "title": "The Full Battery",
        "module": "The test",
        "one_line": "Take the battery fresh, and set four measures, effective rate, skim gist, scan time and recall, beside your first ones.",
        "summary": (
            "A reader is more than a rate. The battery takes one test reading here and "
            "reads your log for your first and latest skim, scan and free recall, then "
            "sets each beside your first measurement of it. Only the effective rate has "
            "a baseline range and a series of tests; for the other three the profile "
            "shows a before and an after, and says less than it seems to."
        ),
        "key": [
            "effective rate: median of last 3 tests",
            "gist: gist questions right on a skim",
            "scan: seconds per target found",
            "recall: idea units recalled / units",
            "one before, one after: too few to say",
        ],
        "key_label": "Four measures in five lines",
        "concepts_intro": (
            "Every course of the Subject measured something. The battery puts four of "
            "those measures side by side, now and at the start."
        ),
        "concepts": [
            ("A profile, not a score",
             "Four measures answer four questions: how much you understand per minute "
             "of ordinary text, how much a skim tells you, how fast you find a fact, "
             "and how much stays. They move separately, and a reader can improve on "
             "one and not the others."),
            ("Only one measure has a range",
             "Effective rate has three baselines and a run of tests, so the "
             "Subject's rule applies to it. Gist, scan and recall each have a first "
             "reading and a latest, and a change between two readings is one "
             "measurement against one."),
            ("Fresh, in one sitting",
             "Fifteen minutes, before rather than after another drill. A tired "
             "battery measures the tiredness, and a battery spread over several days "
             "measures the days."),
        ],
        "read_title": "Four measures, then and now",
        "read_intro": (
            "Take the test reading, fill the profile from your log, then judge each "
            "row by how many readings stand behind it."
        ),
        "body": [
            ("p", "Do the battery fresh, at a time you would otherwise do the Daily "
                  "Drill, and not after another drill. Start with the warm-up above the "
                  "lab: a test reading of a passage about how the Dutch kept low land "
                  "dry, at natural pace with no pacer, then six questions. That is "
                  "your newest test."),
            ("p", "Then press Fill from my log. The effective rate then is the median "
                  "of all your baselines, with their range; the effective rate now is "
                  "the latest test the log holds, today's warm-up included, and the "
                  "fill lists your recent tests so that the verdict is on the median "
                  "of the last three, by the Subject's rule. The "
                  "gist, scan and recall rows take the first and the latest of the "
                  "skims, scans and free recalls your log holds as baseline or test "
                  "readings, from Skimming, Scanning and Previewing and from "
                  "Remembering What You Read. A row your log cannot fill keeps the "
                  "example: type your own figures there if you have them, and "
                  "otherwise read that row as an example."),
            ("ul", [
                "Effective rate: tests at natural pace with questions, here and in the Daily Drill.",
                "Skim gist: the gist questions answered after a timed skim, as in Skimming for Gist.",
                "Scan time: seconds per target found, as in Scanning for a Target.",
                "Recall: idea units recalled out of the passage's units, as in Free Recall.",
            ]),
            ("p", "The preset after-practice is a reader some weeks on. The effective "
                  "rate then is 245, the median of baselines of 238, 245 and 251. The "
                  "last three tests are 262, 270 and 266, and the latest, 266, is the "
                  "rate now. The profile's verdict tile judges the latest test alone, "
                  "so it prints above the baseline range once, with its warning about "
                  "one time in four. The Subject's rule asks for the median of the "
                  "last three, and that is also 266, 15 above the top of the range: "
                  "by the rule, a change."),
            ("p", "The same reader's other rows: gist after a skim from 2 of 3 to all "
                  "3, scan time from 12 seconds a target to 8, and free recall from 5 "
                  "of 12 idea units to 7. What can be said of these? Each is one "
                  "reading before and one after, on a different text each time. The "
                  "gist score moved by one question, the smallest step the measure can "
                  "take. Scan time fell by a third, and recall rose by two idea units "
                  "of twelve. Each is promising and none has a range, so by the "
                  "Subject's rule each has too few readings to say."),
            ("p", "The preset rate-flat is the reader the one-number view forgets. "
                  "Effective rate then 245 and now 244, inside the range; gist 2 of 3 "
                  "both times; recall 5 of 12 both times; and scan time from 12 "
                  "seconds a target to 7. On the one-number view nothing happened. On "
                  "the profile, this reader finds a fact in a document in a little over "
                  "half the time, one reading each, so not yet a result, but the row "
                  "that says where to measure next."),
            ("p", "The rows are there because time spent reading is saved in four "
                  "places, not one: understanding more per minute, knowing when a "
                  "skim is enough, finding a fact without reading for it, and keeping "
                  "what was read so that it need not be read again. Skimming, "
                  "Scanning and Previewing and Words, Knowledge and Difficulty argued "
                  "that the large savings are in the second and third, not the first."),
            ("p", "To make a row say something, measure it the way the effective rate "
                  "was measured: three readings to give a range, then tests. A row "
                  "that matters to you can become a row of your plan: a skim or a scan "
                  "on a fresh text every week or two, logged, as in A Practice Week. "
                  "Take the battery again in a month or so; the profile will then have "
                  "more than one reading behind some of its rows."),
            ("p", "This is the last lesson of the Subject. What it leaves you with is "
                  "not a speed but a method: a log, a rule for reading it, a routine "
                  "that keeps it filling, and four measures for what reading faster "
                  "can mean. Tomorrow, go back to The Daily Drill."),
        ],
        "lab": ("readkit", {
            "mode": "log",
            "view": "profile",
            "warmup": PASSAGES["P48"],
            "warmup_kind": "test",
            "preset": "after-practice",
            "presets": [
                {"id": "after-practice", "label": "Some weeks on",
                 "errThen": 245, "errNow": 266, "baseLo": 238, "baseHi": 251,
                 "gistThen": "2/3", "gistNow": 1, "scanThen": 12, "scanNow": 8,
                 "recallThen": "5/12", "recallNow": "7/12",
                 "expect": {"lgErrThen": "245 wpm", "lgErrNow": "266 wpm",
                            "lgVerdict": "above the baseline range once — a fourth reading does this about one time in four",
                            "lgGist": "2/3 ≈ 66.7% → 1 = 100%", "lgScan": "12 s → 8 s",
                            "lgRecall": "5/12 ≈ 41.7% → 7/12 ≈ 58.3%"}},
                {"id": "rate-flat", "label": "Rate flat, scan faster",
                 "errThen": 245, "errNow": 244, "baseLo": 238, "baseHi": 251,
                 "gistThen": "2/3", "gistNow": "2/3", "scanThen": 12, "scanNow": 7,
                 "recallThen": "5/12", "recallNow": "5/12",
                 "expect": {"lgErrNow": "244 wpm", "lgVerdict": "inside the baseline range",
                            "lgGist": "2/3 ≈ 66.7% → 2/3 ≈ 66.7%", "lgScan": "12 s → 7 s",
                            "lgRecall": "5/12 ≈ 41.7% → 5/12 ≈ 41.7%"}},
            ],
            "panel_title": "Your profile, then and now",
            "panel_intro": (
                "Your measurement, from your log: baseline and test readings only. The "
                "effective rate is judged against your baseline range; the other three "
                "rows are a first reading and a latest, with no range. Until you fill "
                "it, the profile holds a worked example."
            ),
        }),
        "steps_title": "Taking the battery",
        "steps_intro": "About once a month, in one sitting of fifteen minutes.",
        "steps": [
            ("Sit down fresh",
             "At the time you would do the Daily Drill, with no other drill before "
             "it and nothing to interrupt you."),
            ("Take the test reading",
             "The warm-up here the first time; after that, a test at natural pace "
             "from the Daily Drill's test box."),
            ("Fill the profile",
             "Press Fill from my log, type today's effective rate into the box for "
             "now, and type any figures your log cannot supply from the latest skim, "
             "scan and recall you have done."),
            ("Judge each row by its readings",
             "Effective rate by the median of the last three tests against the range; "
             "the other rows as one reading against one, too few to say. Write down "
             "which row to give readings to next."),
            DAILY,
        ],
        "worked": {
            "title": "The after-practice profile",
            "intro": [
                "Effective rates in words a minute; the other rows as first and latest.",
            ],
            "lines": [
                "baselines 238, 245, 251: median 245, top 251",
                "tests 262, 270, 266: median 266",
                "266 − 251 = 15 above the top: a change",
                "gist 2/3 to 3/3: one question",
                "scan 12 s to 8 s: one reading each",
                "recall 5/12 to 7/12: one reading each",
            ],
            "after": [
                "One row has a range and three tests behind it; three rows have one "
                "reading each side. Only the first can be called a change.",
            ],
        },
        "quiz_title": "Read a profile",
        "quiz": [
            {"q": "Baseline range 238 to 251; latest tests 250, 262 and 247; scan time "
                  "12 seconds a target at first and 7 now. Which measure has changed by "
                  "the Subject's rule?",
             "a": ["Both",
                   "Scan time, because it nearly halved",
                   "Effective rate, because 262 is above 251",
                   "Neither: the test median, 250, is inside the range, and scan time is one reading against one"],
             "c": 3,
             "why": "The median of 250, 262 and 247 is 250, inside the range; the 262 "
                    "is above once. Scan time has no range, so its fall, however large, "
                    "is one reading against one."},
            {"q": "Why does the profile's verdict tile print above the baseline range "
                  "once for after-practice?",
             "a": ["It judges only the latest test, 266, against the range; the median of three needs the last three tests",
                   "Because 266 is less than one range above the top",
                   "Because the other three measures have too few readings",
                   "Because a profile verdict always says once"],
             "c": 0,
             "why": "The tile compares one number, the effective rate now, with the "
                    "range. The median of 262, 270 and 266 is also 266, so by the "
                    "Subject's rule the change stands; the tile does not look at the "
                    "other rows, and it can say inside as well as once."},
            {"q": "Gist after a skim went from 2 of 3 to 3 of 3. What is that?",
             "a": ["A 50% gain in skimming",
                   "One question: the smallest step the measure can take, one reading each side",
                   "Proof that the skimming practice worked",
                   "A fall, because no rate is shown"],
             "c": 1,
             "why": "Three gist questions make each one a third of the score, so one "
                    "more right answer is the smallest possible move, and two readings "
                    "make no range. A skim reports gist answers, not an effective rate."},
            {"q": "Why take the battery fresh and in one sitting?",
             "a": ["The drills stop working after fifteen minutes",
                   "The log keeps only one sitting a day",
                   "A tired battery measures tiredness, and one spread over days measures the days",
                   "The profile needs all four measures in one log entry"],
             "c": 2,
             "why": "The battery compares you with yourself, so its conditions should "
                    "be the same each time. The drills, the log and the profile have no "
                    "such limits: each measure is its own entry, and nothing times out."},
        ],
        "mistakes": [
            ("One number sums up a reader",
             "A reader is a profile: rate on a kind of text, comprehension, the "
             "choice of when not to read everything, and what is kept. In rate-flat "
             "the effective rate went from 245 to 244 and scan time from 12 seconds a "
             "target to 7; on the one-number view nothing happened, and the profile "
             "shows where to measure next."),
            ("Reading a before and an after as a change",
             "Gist 2 of 3 to 3 of 3 and recall 5 of 12 to 7 of 12 are each two "
             "readings on two different texts. Without a range there is no telling "
             "them from the variation of an ordinary week, and the effective rate's "
             "range of 13 with nothing changed is a reminder of how large that is."),
            ("Taking the verdict tile as the Subject's rule",
             "The tile sets the latest test against the range, which is the one-in-four "
             "comparison. The rule is the median of the last three tests: work it from "
             "Reading Your Curve, and use the tile as the latest reading's place."),
        ],
        "standard": (
            "Finish when you can say which measures of a profile have changed.",
            "Given two profiles, say which measures changed by the Subject's rule, "
            "which only a measure with a baseline range and three tests can do, and "
            "which have too few readings to say, giving the figures that show each."
        ),
        "note": (
            "The battery's effective rate is the only row with a range; the other "
            "three are one reading against one, each on a different text, so the "
            "profile shows where to look rather than what has changed. The page's "
            "warm-up asks no free recall and the profile's fill does not read it, so "
            "today's rate is typed by hand and the recall row comes from Remembering "
            "What You Read; the verdict tile judges one effective rate alone."
        ),
    },
]
