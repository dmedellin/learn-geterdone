"""Course 5, lessons 01-07 - the fraction, the three compositions, the assumption, the budget."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "nines-and-downtime",
        "title": "Nines and Downtime",
        "module": "The fraction",
        "one_line": "Convert a target availability into minutes of downtime and back, over a period you have stated.",
        "summary": (
            "Availability is a fraction of a period, and the downtime it permits is "
            "`(1 − A) × period`. Each further nine divides that downtime by ten while "
            "moving the percentage by less than a tenth of a point, which is why the "
            "two ways of quoting the same target sound so unlike each other. The period "
            "is part of the number: a downtime figure without one says nothing at all."
        ),
        "key": [
            "downtime = (1 − A) × period          A is a fraction, never a percentage",
            "99.9%   →  43 min 48 s a month,  8 h 45 min 36 s a year",
            "99.99%  →  4 min 22.8 s a month, 52 min 33.6 s a year",
            "k nines ⟺ 1 − A ≤ 10⁻ᵏ              a month here is 2 628 000 s",
        ],
        "key_label": "One subtraction, one multiplication, one stated period",
        "concepts_intro": (
            "One equation read in both directions, and the convention that makes its answer "
            "reproducible from one page to the next."
        ),
        "concepts": [
            ("Availability is a share of a period",
             "`A` is the fraction of a period during which the service does its job, so "
             "`1 − A` is the fraction during which it does not, and multiplying that by "
             "the length of the period gives the downtime the target permits. Nothing "
             "else is happening: `downtime = (1 − A) × period` is the whole of this "
             "lesson, and every other lesson on this course is what happens to `A` when "
             "several of them are put together."),
            ("A nine is a factor of ten in the downtime",
             "Going from 99.9% to 99.99% moves the percentage by `0.09` points, which "
             "sounds like a rounding. It divides `1 − A` by ten, and `1 − A` is what you "
             "actually buy: 43 minutes and 48 seconds a month become 4 minutes and "
             "22.8 seconds. The percentage is a bad scale for this quantity and the "
             "downtime is a good one, which is why the lab draws the ladder in minutes."),
            ("The period is part of the number",
             "&ldquo;Fifty-two minutes of downtime&rdquo; is four nines over a year and "
             "barely three nines over a month; the same duration is a different promise "
             "on a different clock. This course fixes one table of periods, and a month "
             "in it is a twelfth of a 365-day year &mdash; `2 628 000` seconds &mdash; "
             "so every monthly figure on every page can be reconciled with every other."),
        ],
        "read_title": "Nines, minutes, and the period they are measured over",
        "read_intro": (
            "What an availability is, what a nine is worth, and why the period has to be "
            "written down before the arithmetic starts."
        ),
        "body": [
            ("def", ("Availability",
                     "The <strong>availability</strong> `A` of a service over a period is "
                     "the fraction of that period during which it is serving. It is a "
                     "number in `[0, 1]`; the percentage is a presentation of it and "
                     "never enters a calculation. The complementary fraction `1 − A` is "
                     "the <strong>unavailability</strong>, and the "
                     "<strong>downtime</strong> permitted by `A` over a period of length "
                     "`T` is `(1 − A) × T`.")),
            ("p", "Both directions of that equation are used constantly. A target hands "
                  "you `A` and you want the minutes; a downtime budget hands you the "
                  "minutes and you want the `A` it corresponds to. They are the same "
                  "equation rearranged, and the lab does both."),
            ("math", [
                "given A:        downtime = (1 − A) × T",
                "given downtime: A = 1 − downtime/T",
                "",
                "A = 999/1000, T = 2 628 000 s",
                "downtime = (1/1000) × 2 628 000 = 2628 s = 43 min 48 s",
            ]),
            ("p", "Keep `A` as a fraction throughout. `999/1000` is exactly three nines "
                  "and `0.999` is a double that is very slightly not; the differences "
                  "this course cares about live in the fourth decimal place and further "
                  "down, and a percentage rounded for display hides all of them. Every "
                  "figure the lab prints is an exact fraction until the last digit."),
            ("example", ("The same service, one nine apart",
                         "At 99.9% you may be down `43 min 48 s` a month and "
                         "`8 h 45 min 36 s` a year. At 99.99% those become "
                         "`4 min 22.8 s` and `52 min 33.6 s`. The percentages differ by "
                         "`0.09000%`; the minutes differ by a factor of ten, and it is "
                         "the minutes that get paid for &mdash; in redundancy, in "
                         "deployment discipline and in how fast someone has to be woken "
                         "up.")),
            ("def", ("Nines",
                     "An availability has <strong>k nines</strong> when "
                     "`1 − A ≤ 10⁻ᵏ`, taking the largest such `k`. This is a statement "
                     "about the unavailability and not about how many `9` characters "
                     "appear in the printed percentage.")),
            ("p", "The two readings come apart immediately. 99.95% shows two nines in "
                  "its digits, but `1 − A = 0.0005`, which is smaller than `10⁻³` and "
                  "larger than `10⁻⁴`, so it has three nines &mdash; and it permits "
                  "`21 min 54 s` a month, half of what 99.9% permits. Nines are a "
                  "logarithmic scale, so &ldquo;three and a half nines&rdquo; is not a "
                  "category the definition contains."),
            ("h3", "The period is not optional"),
            ("p", "A downtime is a duration and a duration only means something against "
                  "a period. This course fixes one table and states it on every page: an "
                  "hour is `3600` s, a day `86 400` s, a week `604 800` s, a month "
                  "`2 628 000` s, a quarter `7 884 000` s and a year `31 536 000` s. The "
                  "month is a twelfth of a 365-day year, which is the convention under "
                  "which three nines is the 43.8 minutes quoted everywhere above."),
            ("p", "Another convention is in circulation and it is also defensible: a "
                  "30-day month is `2 592 000` seconds, and three nines over that is "
                  "`2592` s, or 43.2 minutes. Neither figure is wrong. What is wrong is "
                  "quoting one of them beside an annual figure computed from the other, "
                  "and that is why the period is written down first rather than assumed."),
            ("h3", "The other direction: a budget is an availability"),
            ("p", "Start from what you are willing to be down and the same equation hands "
                  "back the target. This is usually the more honest order, because a "
                  "team can say how long an outage may last long before it can say which "
                  "nine it wants, and the arithmetic converts one into the other without "
                  "any negotiation."),
            ("example", ("A budget that does not quite buy a nine",
                         "Someone rounds 43.8 minutes up and writes &ldquo;44 minutes a "
                         "month&rdquo; into a document. That budget is "
                         "`1 − 2640/2 628 000 = 10939/10950`, or `99.89954%`, and by the "
                         "definition above it has <strong>two</strong> nines rather than "
                         "three. The rounding went the wrong way across a boundary. Set "
                         "the lab to work from a budget and move the slider between 43 "
                         "and 44 minutes to watch the count change.")),
        ],
        "lab": ("avail", {
            "mode": "nines",
            "direction": "target",
            "target": "999/1000",
            "budget_minutes": 44,
            "period": "month",
            "panel_title": "Pick a target, or pick a budget",
            "panel_intro": "Start from a target availability and read the minutes off, "
                           "then switch the selector and start from the minutes instead. "
                           "The ladder beside it draws one rung per nine, and each rung "
                           "is a tenth of the one above it rather than a hundredth of a "
                           "per cent below it.",
        }),
        "steps_title": "Turning a target into minutes",
        "steps_intro": (
            "Four lines, and the third one is the only arithmetic. The other three are "
            "what stop the arithmetic being done on the wrong number."
        ),
        "steps": [
            ("Write the availability as an exact fraction",
             "99.9% is `999/1000`. Do not carry it as `0.999`, and do not carry the "
             "percentage into the multiplication: the factor you need is `1 − A`, and "
             "here that is exactly `1/1000`."),
            ("Name the period and put it in seconds",
             "Write down which period you are quoting and its length before anything "
             "else. A month on this course is `2 628 000` s. If a different convention "
             "is in use, say so in the same sentence as the answer."),
            ("Multiply, then read the product as a duration",
             "`(1/1000) × 2 628 000 = 2628` s. Convert once, at the end: 43 minutes and "
             "48 seconds. Converting earlier introduces a rounding into a quantity whose "
             "interesting digits are at the far right."),
            ("Check the answer against the ladder",
             "One more nine must give a tenth of the downtime and one fewer must give ten "
             "times as much. If your answer does not sit on that ladder, the error is "
             "almost always a period mismatch &mdash; a monthly figure compared with an "
             "annual one."),
        ],
        "worked": {
            "title": "99.95% into minutes, and 21 minutes 54 seconds back into a fraction",
            "intro": [
                "A target that is not a round nine, so the fraction has to be carried "
                "rather than recognised.",
            ],
            "lines": [
                "A = 99.95% = 9995/10000 = 1999/2000",
                "1 − A = 1/2000",
                "",
                "a month, 2 628 000 s",
                "downtime = (1/2000) × 2 628 000 = 1314 s = 21 min 54 s",
                "",
                "a year, 31 536 000 s",
                "downtime = (1/2000) × 31 536 000 = 15 768 s = 4 h 22 min 48 s",
                "",
                "and back again",
                "A = 1 − 1314/2 628 000 = 1 − 1/2000 = 1999/2000 = 99.95%",
                "",
                "how many nines",
                "1 − A = 0.0005 ≤ 10⁻³        so k is at least 3",
                "0.0005 > 10⁻⁴                 so k is not 4",
                "99.95% is three nines, and it permits half the downtime of 99.9%",
            ],
            "after": [
                "The check at the end is the part worth keeping. Two digits of the "
                "percentage moved and the count of nines did not; the downtime halved. "
                "Anyone reading &ldquo;99.95&rdquo; as &ldquo;two nines and a bit&rdquo; "
                "has compared the printed characters instead of the unavailability.",
                "For a faded rehearsal, take 99.5%. The supplied first move is "
                "`1 − A = 1/200`. Produce the downtime per week and per quarter, say how "
                "many nines it has by the definition rather than by looking, and then "
                "state the monthly budget in minutes that would buy exactly one more "
                "nine. Check all three against the lab before opening the quiz, and say "
                "which period each of your figures belongs to.",
            ],
        },
        "quiz_title": "Nines, minutes and periods",
        "quiz": [
            {"q": "A service is offered at 99.99%. How much downtime does that permit a month, with a month taken as `2 628 000` seconds?",
             "a": ["`4 min 22.8 s`", "`43 min 48 s`", "`26.28 s`", "`52 min 33.6 s`"],
             "c": 0,
             "why": "`(1 − 9999/10000) × 2 628 000 = 262.8` s. `43 min 48 s` is 99.9%, "
                    "one nine less. `26.28 s` is 99.999%, one nine more. "
                    "`52 min 33.6 s` is the right availability over the wrong period "
                    "&mdash; it is 99.99% for a year."},
            {"q": "Someone objects that moving from 99.9% to 99.99% is &ldquo;only 0.09% better&rdquo;. What is wrong with that?",
             "a": ["The percentages differ by 0.9 points, not 0.09",
                   "Nothing is wrong with the subtraction; it is the wrong quantity, because the downtime falls by a factor of ten",
                   "Availability figures can never be compared to one another",
                   "99.99% is two nines above 99.9%, not one"],
             "c": 1,
             "why": "The subtraction is correct: the lab prints the gap as `0.09000%`. "
                    "It is simply not what anyone is buying. What is bought is "
                    "`1 − A`, which goes from `1/1000` to `1/10000` &mdash; from "
                    "43 minutes and 48 seconds a month to 4 minutes and 22.8 seconds. "
                    "Availabilities compare perfectly well, by the ratio of their "
                    "unavailabilities rather than by the difference of their percentages."},
            {"q": "By the rule that `k` nines means `1 − A ≤ 10⁻ᵏ`, how many nines does 99.95% have?",
             "a": ["Two", "Three", "Four", "Three and a half"],
             "c": 1,
             "why": "`1 − A = 0.0005`, which is at most `10⁻³` and more than `10⁻⁴`, so "
                    "`k = 3`. &ldquo;Two&rdquo; comes from counting the `9` characters "
                    "in the printed number. &ldquo;Four&rdquo; would need "
                    "`1 − A ≤ 0.0001`. &ldquo;Three and a half&rdquo; is not a value the "
                    "definition can return: `k` is a whole number of decades."},
        ],
        "mistakes": [
            ("Comparing two targets by subtracting their percentages",
             "`99.99 − 99.9 = 0.09` is arithmetic about the wrong quantity. The thing "
             "that changed is `1 − A`, and it changed by a factor of ten. Any argument "
             "of the form &ldquo;that is a tiny improvement&rdquo; based on the "
             "percentage gap has measured the availability where it should have measured "
             "the outage."),
            ("Quoting a downtime with no period attached",
             "&ldquo;We were down 52 minutes&rdquo; is four nines against a year and "
             "worse than three against a month. A duration is half a number; the period "
             "is the other half. Write both, every time, and prefer to write the period "
             "in seconds so that nobody has to guess whether your month has 30 days or "
             "30.4167 of them."),
            ("Counting the nines that are printed rather than the ones that are bought",
             "99.95% displays two nines and has three. 99.5% displays two and has two. "
             "The definition looks at `1 − A` and asks which power of ten it fits under, "
             "which is a question about the size of the outage rather than about the "
             "spelling of the target."),
        ],
        "standard": ("Finish when a target availability and a downtime budget feel like one number written two ways.",
                     "You should be able to convert either into the other over any of "
                     "the six periods without looking anything up, say how many nines an "
                     "availability has by the definition rather than by eye, and state "
                     "the period alongside every duration you quote."),
        "note": 'This lesson takes the availability as given. Where it comes from is the next question, and it has an answer with two levers in it: a machine is available in proportion to how long it runs between failures and how fast it is repaired. &ldquo;MTBF and MTTR&rdquo; shows that those two levers are worth exactly the same amount, and that one of them is usually far cheaper to pull.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "mtbf-and-mttr",
        "title": "MTBF and MTTR",
        "module": "The fraction",
        "one_line": "Compute availability from the two lifetimes, and the repair time a target actually demands.",
        "summary": (
            "A machine's life is a cycle: it runs for `MTBF`, it is repaired for `MTTR`, "
            "and its availability is the running share of that cycle, `MTBF/(MTBF + MTTR)`. "
            "The formula is symmetric in a way that is worth a lesson on its own &mdash; "
            "halving the repair time and doubling the time between failures produce the "
            "identical fraction &mdash; and one of the two is usually much cheaper to buy."
        ),
        "key": [
            "A = MTBF/(MTBF + MTTR)              one cycle is MTBF + MTTR",
            "A(M, R/2) = A(2M, R)                the two levers are worth the same",
            "MTTR = M(1 − A)/A                   the repair time a target allows",
            "1000 h between failures, 1 h to fix  →  1000/1001 = 99.90010%",
        ],
        "key_label": "Availability as the running share of a cycle",
        "concepts_intro": (
            "Availability has a mechanism underneath it, and the mechanism has exactly two "
            "parameters. Confusing either of them with the availability is the standard error."
        ),
        "concepts": [
            ("One cycle is a run and a repair",
             "`MTBF` is the mean time between failures and `MTTR` the mean time to "
             "repair, so one full cycle lasts `MTBF + MTTR` and the service is up for "
             "`MTBF` of it. The availability is that share: "
             "`A = MTBF/(MTBF + MTTR)`. A machine that runs `1000` hours and is repaired "
             "in one is available `1000/1001` of the time, which is `99.90010%`."),
            ("The two levers are the same lever",
             "`A(2M, R) = 2M/(2M + R) = M/(M + R/2) = A(M, R/2)`. That is an identity, "
             "not an approximation: halving the repair time buys exactly as much "
             "availability as doubling the time between failures. The lab draws both as "
             "bars and they are the same length. Which one to pull is then a question "
             "about cost, and repairing faster is usually the cheaper of the two."),
            ("Reliability is not availability",
             "Reliability is how rarely it breaks; availability is how much of the time "
             "it works. A machine that fails once a year and takes a day to fix is "
             "`365/366 = 99.72678%` &mdash; two nines. A machine that fails every "
             "`100` hours, eighty-seven times a year, but is back in six minutes is "
             "`1000/1001 = 99.90010%` &mdash; three nines. The unreliable machine is "
             "the more available one, and the user experiences availability."),
        ],
        "read_title": "The cycle, the identity, and the lever you can actually move",
        "read_intro": (
            "Where an availability comes from, why its two inputs trade off exactly, and "
            "what a target availability demands of a repair process."
        ),
        "body": [
            ("def", ("MTBF, MTTR and steady-state availability",
                     "For a component that alternates between working and being "
                     "repaired, <strong>MTBF</strong> is the mean length of a working "
                     "interval and <strong>MTTR</strong> the mean length of a repair. "
                     "Over many cycles the fraction of time spent working tends to "
                     "`A = MTBF/(MTBF + MTTR)`, which is the "
                     "<strong>steady-state availability</strong>.")),
            ("p", "This course takes the failure rate as constant: a component that has "
                  "run for a year is no likelier to fail in the next hour than one "
                  "installed this morning. That is a modelling assumption and it is "
                  "wrong for anything with a wear-out mode, but it is the assumption "
                  "under which `MTBF` is a single number rather than a curve."),
            ("thm", ("The two levers are worth exactly the same",
                     "For any `M > 0` and `R > 0`, `A(2M, R) = A(M, R/2)`.")),
            ("proof", [
                "`A(2M, R) = 2M/(2M + R)`. Divide numerator and denominator by `2`: "
                "`= M/(M + R/2) = A(M, R/2)`.",
                "Nothing about the sizes of `M` and `R` was used, so the equality holds "
                "everywhere, not merely for small `R`. The lab computes both fractions "
                "and compares them exactly; if they ever failed to agree the page would "
                "say so on its face.",
            ]),
            ("example", ("One thousand hours and one hour",
                         "`M = 1000` h, `R = 60` min gives "
                         "`A = 3 600 000/3 603 600 = 1000/1001 = 99.90010%`, which is "
                         "three nines and `8 h 45 min 4.50 s` of downtime a year across "
                         "`8.75` cycles. Halve the repair to 30 minutes and `A` becomes "
                         "`2000/2001 = 99.95002%`, cutting the annual downtime to "
                         "`4 h 22 min 40.12 s`. Double the time between failures instead "
                         "and `A` is `2000/2001` again, to the digit.")),
            ("h3", "What a target demands of the repair process"),
            ("p", "Rearranging gives the two questions a target actually asks. "
                  "`MTTR = M(1 − A)/A` is the repair time a target allows at the current "
                  "reliability, and `MTBF = R·A/(1 − A)` is the reliability it would "
                  "demand at the current repair time. Both are printed by the lab, and "
                  "they are usually the moment a target stops being an aspiration."),
            ("math", [
                "target A = 99.99%,  M = 1000 h",
                "MTTR = M(1 − A)/A = 3 600 000 × (1/10000) / (9999/10000)",
                "     = 3 600 000/9999 = 360.036 s = 6 min 0.04 s",
                "",
                "the same target at the current one-hour repair",
                "MTBF = R·A/(1 − A) = 3600 × 9999 = 35 996 400 s = 9999 h",
            ]),
            ("p", "Four nines on a component that fails every thousand hours means "
                  "detecting, diagnosing and fixing inside six minutes, every time. "
                  "Stated that way the target is a claim about paging, automation and "
                  "rollback rather than about hardware, which is the useful form of it. "
                  "The alternative is running `9999` hours between failures, which is a "
                  "different and generally slower project."),
            ("h3", "Why the unreliable machine wins"),
            ("p", "The misconception this lesson exists to break is that a machine which "
                  "rarely fails is the available one. Availability does not count "
                  "failures, it counts seconds, and a rare failure that lasts a day costs "
                  "more seconds than eighty-seven failures that last six minutes each. "
                  "Both machines are in the lab's reach: set `8760` hours against a "
                  "1440-minute repair and then `100` hours against a six-minute one."),
            ("example", ("Two machines, one preference",
                         "Machine A fails once a year and is repaired in a day: "
                         "`A = 365/366 = 99.72678%`, `23 h 56 min 3.93 s` down a year, "
                         "two nines. Machine B fails every `100` hours &mdash; "
                         "`87.51` times a year &mdash; and is repaired in six minutes: "
                         "`A = 1000/1001 = 99.90010%`, `8 h 45 min 4.50 s` down a year, "
                         "three nines. Machine B breaks eighty-seven times as often and "
                         "is down for a third as long.")),
        ],
        "lab": ("avail", {
            "mode": "mtbf",
            "mtbf_hours": 1000,
            "mttr_minutes": 60,
            "target": "9999/10000",
            "panel_title": "Move the two levers independently",
            "panel_intro": "Set the time between failures and the repair time, and watch "
                           "the two comparison bars. They are the same length whenever "
                           "one lever is doubled and the other halved, which is the "
                           "identity this lesson turns on. The last row of the table is "
                           "the repair time your target actually demands.",
        }),
        "steps_title": "Sizing a repair process against a target",
        "steps_intro": (
            "The target is given and the reliability is usually a fact about hardware you "
            "did not choose. That leaves one unknown, and it is the interesting one."
        ),
        "steps": [
            ("Put both lifetimes in the same unit",
             "Seconds, for preference. `MTBF` quoted in hours against an `MTTR` quoted "
             "in minutes is the most common way to produce an availability that is wrong "
             "by a factor of sixty, and the error looks entirely plausible."),
            ("Compute the cycle, then the share",
             "`A = MTBF/(MTBF + MTTR)`. Leave it as a fraction: `1000/1001` is exact and "
             "carries its own sanity check, because the denominator is visibly one repair "
             "longer than the numerator."),
            ("Rearrange for the lever you can move",
             "`MTTR = M(1 − A)/A` for the repair time a target allows; "
             "`MTBF = R·A/(1 − A)` for the reliability it would otherwise demand. Compute "
             "both and compare them with what your organisation can actually do."),
            ("State the answer as an operational claim",
             "&ldquo;Four nines&rdquo; is not actionable; &ldquo;detected, diagnosed and "
             "repaired within six minutes, every time, on a component that fails every "
             "thousand hours&rdquo; is. If that sentence is not true of your team, the "
             "target is not either."),
        ],
        "worked": {
            "title": "A database that fails monthly: what repair time buys three nines",
            "intro": [
                "The reliability is given and cannot be changed this quarter. The target "
                "is three nines. The only unknown is how fast a failure has to be dealt "
                "with, and the answer is the specification for the on-call process.",
            ],
            "lines": [
                "MTBF = 730 h = 2 628 000 s          (one failure a month)",
                "target A = 999/1000",
                "",
                "MTTR = M(1 − A)/A",
                "     = 2 628 000 × (1/1000) / (999/1000)",
                "     = 2 628 000/999",
                "     = 2630.63 s = 43 min 50.63 s",
                "",
                "check by substitution",
                "A = 2 628 000 / (2 628 000 + 2 628 000/999)",
                "  = 999/1000        ✓",
                "",
                "and what the current 3-hour repair actually gives",
                "A = 2 628 000/(2 628 000 + 10 800) = 730/733 = 99.59072%",
                "  two nines, and 1 d 11 h 51 min 9.58 s of downtime a year",
            ],
            "after": [
                "The 43 minutes and 50 seconds is the whole answer: one failure a month "
                "and three nines means every failure is closed inside three quarters of "
                "an hour, including the part where somebody notices. The current "
                "three-hour repair is not close &mdash; it is two nines, and 4.09 times "
                "the annual downtime.",
                "Note the coincidence and do not read anything into it: `43 min 50 s` "
                "here and the `43 min 48 s` of three nines a month are nearly the same "
                "duration for an unrelated reason, which is that this machine's `MTBF` "
                "happens to be one month. Change the `MTBF` and the two part company.",
                "For a faded rehearsal, keep the monthly failure and ask for four nines. "
                "The supplied first move is that `1 − A` falls by a factor of ten while "
                "`M` does not move at all. Produce the required `MTTR`, then answer the "
                "harder question: at a repair time your team could actually hold, what "
                "`MTBF` would four nines demand, and is that a hardware project or a "
                "redundancy one?",
            ],
        },
        "quiz_title": "Cycles, levers and targets",
        "quiz": [
            {"q": "A service has `MTBF = 200` h and `MTTR = 2` h. What is its availability?",
             "a": ["`200/202 = 99.0099%`", "`200/198 = 101.01%`", "`2/202 = 0.9901%`", "`198/200 = 99.0000%`"],
             "c": 0,
             "why": "The cycle is `200 + 2 = 202` hours and the service is up for `200` "
                    "of them, so `A = 200/202`. The second choice divides by the run "
                    "time less the repair and returns a number above one, which no "
                    "availability can be. The third is the unavailability. The fourth "
                    "subtracts the repair from the run time instead of adding it to the "
                    "cycle."},
            {"q": "You can either halve the repair time or double the time between failures, at the same cost. Which buys more availability?",
             "a": ["Doubling the time between failures, because fewer failures is always better",
                   "Halving the repair time, because downtime is what is being measured",
                   "They give exactly the same availability",
                   "It depends on whether `MTTR` is larger or smaller than `MTBF`"],
             "c": 2,
             "why": "`A(2M, R) = 2M/(2M + R) = M/(M + R/2) = A(M, R/2)`, identically, for "
                    "every `M` and `R`. The first two options each name a real effect "
                    "and then claim it dominates; neither does. The fourth suggests the "
                    "identity holds only in some regime, and the proof uses no assumption "
                    "about the relative sizes at all. Since they are equal, choose on "
                    "cost &mdash; and repairing faster is usually cheaper."},
            {"q": "Machine A fails once a year and takes a day to repair. Machine B fails every `100` hours and is back in six minutes. Which is more available?",
             "a": ["A, because it fails 87 times less often",
                   "B, at `99.90010%` against A's `99.72678%`",
                   "They are equally available, since A's rarity offsets B's speed",
                   "A, because availability is determined by the failure rate"],
             "c": 1,
             "why": "`A = 365/366 = 99.72678%`, two nines, `23 h 56 min` down a year. "
                    "`B = 1000/1001 = 99.90010%`, three nines, `8 h 45 min` down a year. "
                    "Availability counts seconds of outage, not incidents: B has "
                    "eighty-seven times as many incidents and a third as much downtime. "
                    "That is the difference between reliability and availability, and it "
                    "is why the repair lever exists."},
        ],
        "mistakes": [
            ("Reading an MTBF as a prediction of one outage",
             "&ldquo;Our MTBF is a year, so we get one outage a year&rdquo; is two "
             "errors in one clause. A mean is not a schedule &mdash; with a constant "
             "failure rate the time to the next failure is memoryless, and two failures "
             "in a month is an ordinary outcome. And a yearly failure says nothing at "
             "all about availability until the repair time is named: a day of repair is "
             "two nines, six minutes is more than four."),
            ("Mixing the units of the two lifetimes",
             "Hours against minutes is the usual version, and it is invisible in the "
             "answer: `1000` and `60` with no units gives `1000/1060 = 94.3%`, which "
             "looks like a plausible availability for a plausible machine and is wrong "
             "by more than a factor of fifty in the downtime. Convert both to seconds "
             "before the division, every time."),
            ("Treating reliability as the thing being bought",
             "A component that fails rarely is not thereby available, and a component "
             "that fails constantly is not thereby unavailable. The user notices the "
             "seconds they could not use the service, which is `1 − A`, and that number "
             "is as sensitive to the repair as to the failure. Buying only reliability "
             "leaves the cheaper half of the equation untouched."),
        ],
        "standard": ("Finish when a target availability reads as a statement about how fast a failure must be closed.",
                     "You should be able to compute `A` from the two lifetimes in "
                     "consistent units, derive the `MTTR` a target allows, show that the "
                     "two levers are identical rather than approximately so, and say why "
                     "the machine that fails more often can be the one that is up more."),
        "note": 'Both lessons so far concern one component. Real systems are many components arranged in two ways: those a request needs all of, and those it needs any of. Those two arrangements have different formulas and they point in opposite directions &mdash; &ldquo;Series: Availability Multiplies&rdquo; takes the first, and it is the one that surprises people, because a chain is worse than every part of it.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "chains-multiply",
        "title": "Series: Availability Multiplies",
        "module": "Composing availability",
        "one_line": "Compute the availability of a chain of dependencies and show it falls below the weakest of them.",
        "summary": (
            "A request that needs every one of its dependencies succeeds only if all of "
            "them do, so under independence the availabilities multiply: `A = ∏Aᵢ`. Ten "
            "dependencies at 99.9% each give `99.00449%`, which is two nines rather than "
            "three and nearly ten times the downtime of any single link. The phrase "
            "&ldquo;as available as the weakest link&rdquo; describes the wrong shape entirely."
        ),
        "key": [
            "A = ∏Aᵢ            given independence, and a request that needs them all",
            "ten links at 99.9%  →  99.00449%,  7 h 16 min 2.05 s a month",
            "that is 9.96 × the downtime of the weakest link alone",
            "adding a 99.99% service to that chain lowers it to 98.99459%",
        ],
        "key_label": "A chain, and what it costs to make it longer",
        "concepts_intro": (
            "One multiplication, one assumption, and one conclusion that sounds wrong until "
            "the numbers are in front of you."
        ),
        "concepts": [
            ("A serial dependency is an AND",
             "If a request needs the auth service and the database and the cache and the "
             "network between them, it succeeds only when every one of them is up. The "
             "probability of an AND of independent events is the product of their "
             "probabilities, so `A = A₁A₂…Aₙ`. Nothing in that argument is about "
             "software; it is the definition of independence applied to the list of "
             "things a request cannot do without."),
            ("The product is below every factor",
             "Each `Aᵢ` is at most `1`, so multiplying by it cannot raise the running "
             "total. The chain is therefore worse than its weakest link, not equal to "
             "it: ten links at 99.9% give `99.00449%`, whose downtime is `9.96` times "
             "the `43 min 48 s` a single link permits. The unavailabilities add, near "
             "enough, and that is the useful way to hold it."),
            ("Independence is an assumption, and it is stated here",
             "`A = ∏Aᵢ` is exactly right when the components fail independently and "
             "merely plausible otherwise. Two services in the same rack, behind the same "
             "certificate or shipped by the same deploy are not independent, and the "
             "product will read optimistically for one shape of correlation and "
             "pessimistically for another. &ldquo;Correlated Failure&rdquo; measures the gap."),
        ],
        "read_title": "The product, and why it is worse than the worst component",
        "read_intro": (
            "What multiplies, what it multiplies to, and what happens when a very good "
            "service is added to a chain that is already mediocre."
        ),
        "body": [
            ("def", ("Series availability",
                     "Components are <strong>in series</strong> for a request when the "
                     "request needs all of them. If they fail independently, the "
                     "availability of the whole is the product of the parts: "
                     "`A = ∏ᵢ Aᵢ`. The unavailability is `1 − ∏ᵢ Aᵢ`, which for small "
                     "unavailabilities is close to `Σᵢ (1 − Aᵢ)` &mdash; the outages add up.")),
            ("p", "The approximation is worth carrying separately from the formula, "
                  "because it is how the number is estimated in a meeting. Ten "
                  "dependencies each down one part in a thousand are down roughly ten "
                  "parts in a thousand altogether, so the chain is about 99%. The exact "
                  "answer is `99.00449%`, and the estimate was reached without a "
                  "calculator."),
            ("math", [
                "ten links, each 999/1000",
                "",
                "A = (999/1000)¹⁰",
                "  = 990 044 880 209 748 209 880 044 990 001 / 10³⁰",
                "  = 0.9900449 = 99.00449%          two nines, not three",
                "",
                "downtime a month = (1 − A) × 2 628 000 s = 7 h 16 min 2.05 s",
                "the weakest link alone                   =      43 min 48 s",
                "ratio                                    = 9.96 ×",
            ]),
            ("p", "The product is exact. Ten fractions of `999/1000` multiply to "
                  "`999¹⁰` over `1000¹⁰`, a thirty-digit rational, and the lab carries it "
                  "as one rather than as a double that has already lost the digits the "
                  "lesson is about. The percentage appears once, at the end."),
            ("h3", "Adding a better service still makes it worse"),
            ("p", "This is the consequence people resist. A chain at `99.00449%` gains a "
                  "new dependency at 99.99% &mdash; a service ten times better than any "
                  "link already in it. The chain becomes `98.99459%`, which is one nine. "
                  "Multiplying by `0.9999` is still multiplying by something less than "
                  "one, and there is no availability, short of exactly `1`, that a chain "
                  "can absorb for free."),
            ("example", ("Eleven links, ten of them the same",
                         "`(999/1000)¹⁰ × (9999/10000) = 98.99459%`, "
                         "`7 h 20 min 22.24 s` a month against the "
                         "`7 h 16 min 2.05 s` before it, and the nines count drops from "
                         "two to one. Type the eleventh dependency into the lab's chain "
                         "and watch the running product step down rather than hold "
                         "still. Every architecture review that adds &ldquo;just one "
                         "more service, and it's a very reliable one&rdquo; is this "
                         "calculation.")),
            ("h3", "Which way to read the number"),
            ("p", "Two readings of the same fact are useful in different rooms. The "
                  "first: a chain is a budget and each dependency spends part of it, so "
                  "a three-nines promise cannot be built from three-nines parts. The "
                  "second: the cheapest way to raise a chain is usually to shorten it, "
                  "because removing a link multiplies the product by more than any "
                  "plausible improvement to a link that stays."),
            ("example", ("What three nines costs in a chain of ten",
                         "For the whole chain to reach `999/1000`, ten equal links must "
                         "each satisfy `A¹⁰ = 0.999`, which is `A ≈ 0.9998999` &mdash; "
                         "about four nines each. Set the lab's chain to ten entries of "
                         "`99.99` and the product is `99.90004%`: ten four-nines "
                         "services, assembled in series, are worth three nines. That is "
                         "the arithmetic behind every complaint that the platform team's "
                         "SLOs are stricter than the product's.")),
            ("p", "One caution before the lab. Everything above assumes each dependency "
                  "is genuinely required. A service called on a cache miss, or only for "
                  "one endpoint, is not in series with every request and does not belong "
                  "in the product at its full weight; putting it there produces a "
                  "pessimistic number that the next argument will rightly dismiss."),
        ],
        "lab": ("avail", {
            "mode": "series",
            "chain": "99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9",
            "extra": 0,
            "extra_avail": "9999/10000",
            "panel_title": "Build the chain",
            "panel_intro": "Ten dependencies at 99.9% are loaded. Read the running "
                           "product down the table, then bolt on extras at 99.99% and "
                           "watch the line fall below the dashed one that marks the "
                           "weakest link. Every entry is an exact fraction and the "
                           "product is taken as one.",
        }),
        "steps_title": "Computing a chain, and reporting it honestly",
        "steps_intro": (
            "The multiplication is trivial. Deciding what belongs in the list, and saying "
            "what you assumed about it, is the work."
        ),
        "steps": [
            ("List what the request genuinely cannot do without",
             "Walk one request end to end and write down every component whose failure "
             "fails it. Anything consulted optionally, behind a cache or on one endpoint "
             "only, is not in series at full weight and should be left out or weighted "
             "down."),
            ("Multiply the availabilities, not the percentages",
             "Carry each as a fraction and take the product. Ten links at `999/1000` are "
             "`999¹⁰/1000¹⁰`; convert to a percentage once, at the end, and keep enough "
             "digits that the nines are still visible."),
            ("Convert to downtime and compare with the weakest link",
             "Turn `1 − A` into minutes over a stated period and put it beside the "
             "downtime of the worst single component. The ratio should be close to the "
             "number of links; if it is not, either a link is dominating or something is "
             "in the list that does not belong."),
            ("Say out loud that you assumed independence",
             "The product is exactly right under independence and optimistic under a "
             "shared cause. Name what the components share &mdash; rack, power feed, "
             "deploy pipeline, certificate authority &mdash; and record the product as "
             "an upper bound where they share something that matters."),
        ],
        "worked": {
            "title": "A checkout path, five dependencies, unequal",
            "intro": [
                "A real chain is not ten identical links. The arithmetic is the same and "
                "the reading changes: one component turns out to be spending most of the "
                "budget, and that is the finding.",
            ],
            "lines": [
                "edge / TLS        99.99%   = 9999/10000",
                "auth              99.9%    =  999/1000",
                "catalogue         99.95%   = 1999/2000",
                "payments          99.9%    =  999/1000",
                "ledger write      99.99%   = 9999/10000",
                "",
                "A = 0.9999 × 0.999 × 0.9995 × 0.999 × 0.9999",
                "  = 99.73025%          two nines",
                "",
                "downtime a month = (1 − A) × 2 628 000 = 1 h 58 min 9.01 s",
                "weakest link alone                     =      43 min 48 s",
                "ratio                                  = 2.70 ×",
                "",
                "where the budget went, as unavailabilities",
                "auth      0.0010      payments  0.0010      catalogue 0.0005",
                "edge      0.0001      ledger    0.0001",
                "sum       0.0027      and 1 − A = 0.0026975        ✓",
            ],
            "after": [
                "The last block is the one to keep. The unavailabilities sum to `0.0027` "
                "and the exact `1 − A` is `0.0026975`; the sum is a good estimate and a "
                "better explanation, because it says immediately that auth and payments "
                "are three quarters of the outage and that improving the edge cannot "
                "matter. Two nines, and the ratio of `2.70` against the weakest link "
                "says the chain behaves like about three equal links.",
                "For a faded rehearsal, the team proposes adding a fraud-check service "
                "at 99.995% to this path. The supplied first move is that its "
                "unavailability, `0.00005`, joins the sum above. Predict the new chain "
                "availability and its monthly downtime before computing them, then type "
                "the six values into the lab and check. Then answer the question the "
                "number raises: is the new chain still inside a two-nines promise, and "
                "what would have to be removed to keep it inside a three-nines one?",
            ],
        },
        "quiz_title": "Chains and products",
        "quiz": [
            {"q": "Three services, each 99.9%, are all required by a request. What is the availability of the path, assuming independence?",
             "a": ["`99.9%`, the same as the weakest link",
                   "`99.70030%`",
                   "`99.96667%`, the average",
                   "`99.99%`, because the three back each other up"],
             "c": 1,
             "why": "`(999/1000)³ = 0.9970030`. The first option is the "
                    "weakest-link misconception: a chain is worse than its worst part, "
                    "not equal to it. The third averages the availabilities, which is not "
                    "an operation this model contains. The fourth is the parallel formula "
                    "applied to components that are in series &mdash; these three do not "
                    "back each other up, the request needs all of them."},
            {"q": "A path made of ten 99.9% dependencies sits at `99.00449%`. A new dependency at 99.99%, ten times more available than any existing link, is added. What happens to the path?",
             "a": ["It rises, because the new service is better than the average",
                   "It stays the same, because 99.99% is close enough to 1",
                   "It falls to `98.99459%`",
                   "It falls, but only if the new service is less available than the path"],
             "c": 2,
             "why": "`0.9900449 × 0.9999 = 0.9899459`. Multiplying by anything below `1` "
                    "lowers the product, whatever it is compared with. The last option "
                    "sounds like a sensible rule and is exactly the error: the "
                    "comparison that matters is with `1`, not with the path. The only "
                    "free dependency is one that never fails."},
            {"q": "Ten equal services are wired in series and the path must reach three nines. What availability must each service have?",
             "a": ["Three nines each, since ten of them make the path",
                   "About four nines each, because `A¹⁰ = 0.999` needs `A ≈ 0.9998999`",
                   "99.99% each, exactly",
                   "It is impossible; a ten-link chain cannot reach three nines"],
             "c": 1,
             "why": "Ten links at three nines give `99.00449%`, an order of magnitude "
                    "short. Solving `A¹⁰ = 0.999` gives `A ≈ 0.9998999`, a shade under "
                    "four nines. The third choice is close and not exact: ten links at "
                    "`99.99%` give `99.90004%`, which does clear three nines but is not "
                    "the minimum. The fourth is simply false, and the lab will build the "
                    "chain that disproves it."},
        ],
        "mistakes": [
            ("Reporting a chain as being as good as its weakest link",
             "It is worse, and by roughly the number of links: ten at 99.9% give "
             "`99.00449%`, whose downtime is `9.96` times the weakest link's own. The "
             "phrase is borrowed from load-bearing metaphors where the chain breaks at "
             "one point; here every link has its own outages and they accumulate."),
            ("Adding a very available service and expecting the path to improve",
             "Attaching a 99.99% dependency to a 99.00449% path gives `98.99459%`. The "
             "new service is not helping the others &mdash; it is another thing that can "
             "fail. Redundancy improves a path; a dependency, however good, only ever "
             "costs it something."),
            ("Multiplying without saying that independence was assumed",
             "`A = ∏Aᵢ` is a theorem about independent events. Components in one rack, "
             "behind one certificate or shipped by one pipeline are not independent, and "
             "the product then reports a confident number about a system it does not "
             "describe. The multiplication is not wrong; the silence about its premise is."),
        ],
        "standard": ("Finish when “we added a dependency” reads as “we lowered the availability”.",
                     "You should be able to multiply a chain exactly, estimate it by "
                     "summing unavailabilities, say how far under the weakest link it "
                     "lands and why, work out what per-component availability a target "
                     "demands, and name the independence assumption unprompted."),
        "note": 'A chain multiplies availability down, which raises the obvious question of what multiplies it up. The answer is the same probability read through its complement: if a request needs any one of several paths, it fails only when all of them do. &ldquo;Parallel: Redundancy&rdquo; does that arithmetic, and then charges for the thing the formula quietly leaves out.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "redundancy-and-parallel-paths",
        "title": "Parallel: Redundancy",
        "module": "Composing availability",
        "one_line": "Compute a redundant set's availability, then subtract the time spent switching between paths.",
        "summary": (
            "If a request needs any one of several independent paths, it fails only when "
            "all of them fail, so `A = 1 − ∏(1 − Aᵢ)`: two 99% paths give 99.99%. That "
            "formula assumes the switch between paths is instantaneous, which it never "
            "is. Charging the failover time against the result is usually a larger "
            "correction than anything a further replica would buy."
        ),
        "key": [
            "A = 1 − ∏(1 − Aᵢ)       any one path serves; all must fail to fail",
            "two paths at 99%   →  P(both down) = 1/10 000  →  99.99%",
            "three paths at 99% →  P(all down)  = 1/10⁶     →  99.9999%",
            "12 failovers a year at 30 s = 6 min a year, which the formula omits",
        ],
        "key_label": "Redundancy, and the bill the formula does not print",
        "concepts_intro": (
            "The complement turns an AND into an OR, and then reality adds a term that no "
            "amount of redundancy removes."
        ),
        "concepts": [
            ("Redundancy is an AND of failures",
             "A set of paths serving the same request is up unless every one of them is "
             "down. Under independence `P(all down) = ∏(1 − Aᵢ)`, so "
             "`A = 1 − ∏(1 − Aᵢ)`. Two paths at 99% fail together with probability "
             "`1/10 000` and the pair is `99.99%`; a third path makes it `1/10⁶` and "
             "`99.9999%`. Each replica multiplies the unavailability by the next one's."),
            ("Every replica is a decade, while independence holds",
             "In series, each component divides the availability; in parallel, each "
             "replica multiplies the unavailability by a number well below one. That is "
             "why redundancy looks like such a good deal on paper &mdash; four paths at "
             "99% are eight nines &mdash; and why the paper number is almost never the "
             "one a system achieves."),
            ("The switch is not free, and it does not get cheaper",
             "Detecting the failure, agreeing on it and cutting over takes seconds, and "
             "those seconds are downtime the formula never mentions. Twelve failovers a "
             "year at thirty seconds is six minutes a year, flat. At two paths that is a "
             "tenth of the ideal outage; at four paths it is essentially all of it, and "
             "the fifth replica buys nothing measurable."),
        ],
        "read_title": "The parallel formula, and the term it leaves out",
        "read_intro": (
            "Why the complement is the right way to compute an OR, what each replica is "
            "worth, and where the returns actually stop."
        ),
        "body": [
            ("def", ("Parallel availability",
                     "Components are <strong>in parallel</strong> for a request when any "
                     "one of them can serve it. If they fail independently, the whole is "
                     "unavailable only when all are, so `1 − A = ∏ᵢ (1 − Aᵢ)` and "
                     "`A = 1 − ∏ᵢ (1 − Aᵢ)`. Computing the complement is not a trick: it "
                     "converts an OR over many events, which has inclusion-exclusion "
                     "terms, into an AND, which does not.")),
            ("math", [
                "each path 99/100,  so 1 − Aᵢ = 1/100",
                "",
                "n = 1     P(all down) = 1/100        A = 99%",
                "n = 2     P(all down) = 1/10 000     A = 99.99%",
                "n = 3     P(all down) = 1/10⁶        A = 99.9999%",
                "n = 4     P(all down) = 1/10⁸        A = 99.999999%",
                "",
                "ideal downtime a year",
                "n = 2   52 min 33.60 s        n = 3   31.54 s        n = 4   0.32 s",
            ]),
            ("p", "Two nines plus two nines is four nines, in parallel &mdash; and it is "
                  "worth being precise about why, because the same reader who adds nines "
                  "here will add them in series, where the claim is false in the other "
                  "direction. In parallel the unavailabilities multiply, and "
                  "`10⁻² × 10⁻²` is `10⁻⁴`. In series the unavailabilities add."),
            ("h3", "Charging for the failover"),
            ("p", "The formula describes a system that notices a failure instantly and "
                  "switches with no loss. Real cutovers take a health check, a timeout, "
                  "a decision and a reconnection, and every second of that is a second "
                  "the request did not get served. The correction is arithmetic: "
                  "`failover seconds × events per period ÷ period`, subtracted."),
            ("math", [
                "charge = (failover × events) / period",
                "       = (30 s × 12) / 31 536 000 s = 360/31 536 000 = 1/87 600",
                "",
                "n = 2   ideal 99.990000%   charged 1/87 600   real 99.988858%",
                "        ideal 52 min 33.60 s a year      real 58 min 33.60 s a year",
            ]),
            ("p", "Six minutes a year, and it does not shrink when a replica is added, "
                  "because it is not a property of the replicas &mdash; it is a property "
                  "of the switching. That is what makes it dominate so quickly."),
            ("example", ("Where the replicas stop paying",
                         "With a thirty-second failover happening twelve times a year: "
                         "two paths at 99% give a real `99.988858%`, three give "
                         "`99.998758%`, four give `99.998857%`. The ideal figures over "
                         "the same range go from four nines to eight; the real ones have "
                         "essentially stopped by three, because the ideal outage has fallen "
                         "below the six minutes of switching and the fourth replica is "
                         "improving a term that is no longer the largest one.")),
            ("h3", "What else the formula is quietly assuming"),
            ("p", "Three things, and each is a separate way to be disappointed. That the "
                  "paths fail independently, which is the next lesson and the largest of "
                  "the three. That any single path can carry the whole load &mdash; if "
                  "two paths each run at 60% of capacity, losing one does not leave a "
                  "working system, it leaves an overloaded one. And that the redundancy "
                  "is exercised: a standby that has never served a request is a component "
                  "with an unmeasured availability, and it is not `0.99`."),
            ("example", ("A replica that is in series, not in parallel",
                         "A cache is added in front of a database to make reads faster, "
                         "and the client is written so that a cache error fails the "
                         "request. The reader calls it redundancy because there are now "
                         "two data stores. The request needs both, so it is a series "
                         "chain: `0.999 × 0.999 = 99.80010%`, below the database alone. "
                         "Adding a component raises availability only when the request "
                         "can succeed without it, and that is a property of the client's "
                         "error handling rather than of the topology drawing.")),
        ],
        "lab": ("avail", {
            "mode": "parallel",
            "paths": 2,
            "each": "99/100",
            "failover_seconds": 30,
            "events_per_year": 12,
            "panel_title": "Add paths, then charge for the switch",
            "panel_intro": "Two 99% paths are loaded with a thirty-second failover "
                           "happening twelve times a year. The table prints the ideal "
                           "availability and the charged one side by side for one to six "
                           "paths; find the replica count at which the amber column "
                           "stops improving.",
        }),
        "steps_title": "Sizing redundancy",
        "steps_intro": (
            "Compute the ideal, then subtract what the mechanism costs, then check the three "
            "assumptions. The subtraction is usually the biggest number on the page."
        ),
        "steps": [
            ("Confirm the paths are genuinely alternatives",
             "A request must be able to succeed using any one of them alone. If the "
             "client fails the request when one errors, or if one path holds data the "
             "other does not, they are in series and the formula for this lesson is the "
             "wrong one."),
            ("Multiply the unavailabilities, then complement",
             "`P(all down) = ∏(1 − Aᵢ)` and `A = 1 − P(all down)`. Two paths at `1/100` "
             "give `1/10 000`. Working in unavailabilities keeps the exact digits: "
             "`1/10 000` is legible where `0.9999` is nearly `1`."),
            ("Charge the failover time against the result",
             "`failover seconds × events per period ÷ period`, subtracted from the ideal. "
             "Estimate the event rate from how often the paths actually fail rather than "
             "from how often you plan to test, and include every cutover, including the "
             "ones that turned out to be unnecessary."),
            ("Compare the two terms and stop where they cross",
             "If the failover charge already exceeds the ideal unavailability, another "
             "replica cannot help: it shrinks a term that is no longer the largest. Spend "
             "the effort on detecting failures faster or switching more cleanly instead."),
        ],
        "worked": {
            "title": "Two regions at 99.9%, with a ninety-second regional failover",
            "intro": [
                "Regional redundancy with a slow cutover, which is the common case: the "
                "paths are very good and the switching is not.",
            ],
            "lines": [
                "each region A = 999/1000,  so 1 − Aᵢ = 1/1000",
                "",
                "ideal",
                "P(both down) = (1/1000)² = 1/1 000 000",
                "A = 999 999/1 000 000 = 99.9999%            six nines",
                "ideal downtime a year = 31.54 s",
                "",
                "the switching",
                "4 failovers a year × 90 s = 360 s = 6 min a year",
                "charge = 360/31 536 000 = 1/87 600 = 0.0000114",
                "",
                "real",
                "A = 0.999999 − 0.0000114 = 0.9999876 = 99.998758%     four nines",
                "real downtime a year = 31.54 s + 6 min = 6 min 31.54 s",
                "",
                "the failover is 92% of the total outage",
            ],
            "after": [
                "Six nines on the slide, four in the year, and twelve times as many "
                "seconds of outage as the formula promised &mdash; all of it spent "
                "switching. The direction this points is clear: cutting the cutover from "
                "ninety seconds to ten is worth far more here than a third region, which "
                "would improve the `31.54` seconds and leave the six minutes alone.",
                "For a faded rehearsal, keep two regions and suppose the team can either "
                "add a third region or halve the failover to `45` seconds. The supplied "
                "first move is to write the two terms separately &mdash; the ideal "
                "unavailability and the charge &mdash; and see which one each option "
                "touches. Compute both resulting availabilities in the lab, then say "
                "which you would buy and what you assumed about the regions failing "
                "independently.",
            ],
        },
        "quiz_title": "Parallel paths and their costs",
        "quiz": [
            {"q": "Two independent paths, each 99%, can each serve the request alone. What is the availability of the pair, ignoring failover time?",
             "a": ["`99%`, the same as one path", "`99.99%`", "`198%`", "`99.5%`, the average"],
             "c": 1,
             "why": "`P(both down) = (1/100)² = 1/10 000`, so `A = 9999/10 000`. Two "
                    "nines and two nines make four nines in parallel, because the "
                    "unavailabilities multiply. Note that the same addition of nines "
                    "would be badly wrong for components in series, where the "
                    "unavailabilities add instead."},
            {"q": "A system has two 99% paths and a thirty-second failover that happens twelve times a year. Which change improves the real availability more: a third path, or halving the failover time?",
             "a": ["The third path, because it adds two more nines",
                   "Halving the failover, because the six minutes a year already exceeds the ideal outage at three paths",
                   "They are equivalent, by the same identity as MTBF and MTTR",
                   "Neither; failover time cannot be charged against availability"],
             "c": 1,
             "why": "The ideal outage at three paths is `31.54` s a year; the failover "
                    "charge is `6` minutes and does not shrink when replicas are added. "
                    "Halving it returns three minutes a year, which is an order of "
                    "magnitude more than the third replica returns. The identity of "
                    "&ldquo;MTBF and MTTR&rdquo; is about one component's two lifetimes "
                    "and does not apply here."},
            {"q": "A cache is put in front of a database, and the client returns an error if the cache call fails. Availability of each is 99.9%. What is the availability of a read?",
             "a": ["`99.9999%`, because there are now two stores",
                   "`99.9%`, because the database is authoritative",
                   "`99.80010%`, because the read needs both",
                   "`99.95%`, the average of the two"],
             "c": 2,
             "why": "The client cannot succeed without the cache, so the two are in "
                    "series and the availabilities multiply: `0.999 × 0.999`. This is the "
                    "shape of the mistake worth remembering &mdash; a component is "
                    "redundant only if the request can succeed without it, which is a "
                    "fact about the error handling and not about the diagram. Change the "
                    "client to fall through on a cache error and the same two components "
                    "become parallel for reads."},
        ],
        "mistakes": [
            ("Taking the ideal figure into a plan",
             "`1 − ∏(1 − Aᵢ)` describes instantaneous, lossless switching. Four paths at "
             "99% compute to eight nines and deliver, with a thirty-second failover "
             "twelve times a year, about four. Quote the charged figure, and quote the "
             "charge separately so that everyone can see which term is which."),
            ("Calling a required component redundant",
             "Two data stores are only redundancy if a read succeeds when either one "
             "fails. If the client errors on a cache miss-with-error, the cache is a new "
             "serial dependency and it has lowered availability: `0.999 × 0.999 = "
             "99.80010%`. Whether a component is in series or in parallel is decided by "
             "the error handling, not by the topology."),
            ("Adding replicas past the point where the switching dominates",
             "Once the failover charge is larger than the ideal unavailability, the next "
             "replica improves a term that no longer matters. At two paths of 99% with "
             "six minutes of annual switching the ideal outage is `52` minutes and the "
             "replica is worth having; at four paths the ideal outage is under a second "
             "and the same replica is worth nothing at all."),
        ],
        "standard": ("Finish when you quote the charged availability by default and treat the ideal one as an upper bound.",
                     "You should be able to compute `1 − ∏(1 − Aᵢ)` exactly, convert a "
                     "failover policy into seconds a year, subtract it, identify the "
                     "replica count at which the switching dominates, and say which "
                     "components in a drawing are genuinely parallel for a given request."),
        "note": 'Full redundancy is one end of a spectrum. Most real systems do not need every replica and do not need only one &mdash; they need a quorum, some `k` out of `n`, and both the series and the parallel formulas turn out to be special cases of the same binomial sum. &ldquo;k-of-n&rdquo; computes it, and closes on the case where adding replicas makes a system less available rather than more.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "k-of-n-and-quorums",
        "title": "k-of-n",
        "module": "Composing availability",
        "one_line": "Compute the availability of a k-of-n quorum and say when another replica helps.",
        "summary": (
            "A system that needs `k` of its `n` replicas is available with probability "
            "`Σ_{j≥k} C(n,j)Aʲ(1 − A)ⁿ⁻ʲ`, the upper tail of a binomial. Series and "
            "parallel are the two ends of it: `k = n` is the product and `k = 1` is "
            "`1 − ∏(1 − Aᵢ)`. Whether another replica helps depends entirely on whether "
            "`k` rises with `n`, and if it does the answer is no."
        ),
        "key": [
            "A = Σ_{j≥k} C(n,j) Aʲ (1 − A)ⁿ⁻ʲ        the upper tail of a binomial",
            "k = n  →  the series product            k = 1  →  1 − ∏(1 − Aᵢ)",
            "at A = 99%:  3-of-5 = 99.9990149%,  5-of-5 = 95.0990%,  1-of-1 = 99%",
            "so 5-of-5 is worse than one machine, by a factor of 49 in downtime",
        ],
        "key_label": "One binomial tail, with the two earlier formulas inside it",
        "concepts_intro": (
            "A quorum is a counting question about how many replicas are up, and the answer "
            "contains both of the previous lessons as special cases."
        ),
        "concepts": [
            ("How many are up is a binomial",
             "With `n` replicas that are independently up with probability `A`, the "
             "number up is `Binomial(n, A)`, so `P(exactly j up) = C(n,j)Aʲ(1 − A)ⁿ⁻ʲ`. "
             "A `k`-of-`n` system is available when at least `k` are up, which is the sum "
             "of those terms from `j = k` to `j = n` &mdash; the upper tail. The lab "
             "lists every term and sums them exactly, and the whole row sums to `1`."),
            ("Series and parallel are its two ends",
             "Setting `k = n` demands every replica and the tail collapses to the single "
             "term `Aⁿ`, which is the series product. Setting `k = 1` demands any one "
             "and the tail is everything except `j = 0`, which is `1 − (1 − A)ⁿ` &mdash; "
             "the parallel formula. These are identities, and the lab checks both on "
             "screen rather than asserting them."),
            ("More replicas help only when k stays put",
             "At `A = 99%`, 3-of-5 is `99.9990149%` and 5-of-5 is `95.0990%`, which is "
             "worse than a single machine's `99%`. Going from `n = 1` to `n = 5` helped "
             "or hurt entirely according to what happened to `k`. A quorum that grows "
             "with the fleet, like `k = n`, is a chain wearing a redundancy costume."),
        ],
        "read_title": "The binomial tail, its two special cases, and when a replica hurts",
        "read_intro": (
            "Where the coefficients come from, how the formula contains the previous two "
            "lessons, and the configuration in which redundancy runs backwards."
        ),
        "body": [
            ("def", ("k-of-n availability",
                     "A system is <strong>`k`-of-`n`</strong> when it serves as long as "
                     "at least `k` of its `n` components are up. If the components are "
                     "independent and each is up with probability `A`, then "
                     "`A(k, n) = Σ_{j=k}^{n} C(n,j) Aʲ (1 − A)ⁿ⁻ʲ`. The term at `j` is "
                     "the probability that exactly `j` are up: `C(n,j)` ways to choose "
                     "which, `Aʲ` for those being up and `(1 − A)ⁿ⁻ʲ` for the rest "
                     "being down.")),
            ("math", [
                "n = 5, A = 99/100, listed term by term",
                "",
                "j   C(5,j)   term                       value",
                "0     1      (1/100)⁵                   0.0000000001",
                "1     5      5(99/100)(1/100)⁴          0.0000000495",
                "2    10      10(99/100)²(1/100)³        0.0000098010",
                "3    10      10(99/100)³(1/100)²        0.0009702990",
                "4     5      5(99/100)⁴(1/100)          0.0480298005",
                "5     1      (99/100)⁵                  0.9509900499",
                "                                        ───────────",
                "                                        1.0000000000",
                "",
                "3-of-5 = j ≥ 3 = 0.999990149 = 99.9990149%        five nines",
            ]),
            ("p", "The column sums to exactly `1`, which is the cheapest available check "
                  "on a binomial: a set of terms that does not sum to one has a wrong "
                  "coefficient somewhere in it. The lab prints that sum for whatever `n` "
                  "you set, and the coefficients are exact integers, so the twelfth row "
                  "of Pascal's triangle is right rather than nearly right."),
            ("h3", "The two ends are the two previous lessons"),
            ("p", "At `k = n` only the `j = n` term survives, so `A(n, n) = Aⁿ`, which is "
                  "the series product of `n` identical components. At `k = 1` every term "
                  "except `j = 0` survives, so `A(1, n) = 1 − (1 − A)ⁿ`, which is the "
                  "parallel formula. Three formulas, one of them; the lab computes all "
                  "three and prints their agreement."),
            ("example", ("Five replicas, three quorums",
                         "Each replica 99%. 1-of-5 is `99.999999990000%` &mdash; ten "
                         "nines, and the parallel formula to the digit. 3-of-5 is "
                         "`99.9990149%` &mdash; five nines, `5 min 10.65 s` a year. "
                         "5-of-5 is `95.0990%` &mdash; one nine, `17 d 21 h` a year, and "
                         "identical to `(99/100)⁵`. The same five machines span nine "
                         "orders of magnitude in downtime depending only on how many of "
                         "them have to agree.")),
            ("h3", "When another replica lowers availability"),
            ("p", "Compare 5-of-5 at `95.0990%` with a single machine at `99%`. Four "
                  "replicas were added and the availability fell by a factor of about "
                  "fifty in downtime, because each new replica was also a new thing that "
                  "had to be up. This is the honest answer to &ldquo;should we add "
                  "another node&rdquo;: it depends on whether the quorum rule holds `k` "
                  "fixed as `n` grows."),
            ("p", "Majority quorums, `k = ⌈(n+1)/2⌉`, sit between the two extremes and "
                  "do improve with `n`, because `k` grows at half the rate `n` does: "
                  "2-of-3 is `99.97020%` and 3-of-5 is `99.9990149%` at the same "
                  "per-node 99%. That is the arithmetic behind five-node clusters, and "
                  "it is also why going from five to seven buys much less than going "
                  "from three to five."),
            ("example", ("The write quorum that made things worse",
                         "A team runs three replicas and, worried about durability, "
                         "changes writes to require acknowledgement from all three "
                         "rather than two. Write availability moves from 2-of-3, "
                         "`99.97020%`, to 3-of-3, `97.0299%` &mdash; from three nines to "
                         "one, and from `2 h 36 min` to `10 d 20 h` a year. Nothing about "
                         "the hardware changed. The lab reproduces this in two slider "
                         "moves: set `n = 3`, then `k = 2` and `k = 3`.")),
            ("p", "One boundary to keep in view: this lesson counts replicas that are up "
                  "and says nothing about whether they agree on the data. A quorum that "
                  "is available can still return a stale read, and the rule that "
                  "prevents that &mdash; read and write sets overlapping &mdash; is a "
                  "different condition on `k` that belongs to the replication course."),
        ],
        "lab": ("avail", {
            "mode": "kofn",
            "n": 5,
            "k": 3,
            "each": "99/100",
            "panel_title": "Set the quorum",
            "panel_intro": "Five replicas at 99% with a quorum of three are loaded. Every "
                           "binomial term is listed and the tail from `k` is highlighted; "
                           "the last three readouts check that `k = n` is the series "
                           "product, that `k = 1` is the parallel form, and that the "
                           "whole row sums to one. Take `k` up to `n` and watch "
                           "availability fall below a single machine.",
        }),
        "steps_title": "Computing and choosing a quorum",
        "steps_intro": (
            "Two of these steps are arithmetic and two are about what the number means once "
            "you have it. The second pair is where quorum decisions are actually made."
        ),
        "steps": [
            ("Write down k and n, and say which operation they govern",
             "Reads and writes often have different quorums, and the availability of a "
             "write is not the availability of a read. Compute them separately; a system "
             "quoted as one number is usually quoting whichever is better."),
            ("Sum the tail, term by term",
             "`Σ_{j≥k} C(n,j)Aʲ(1 − A)ⁿ⁻ʲ`. Write the terms out rather than reaching for "
             "a closed form &mdash; there is not one &mdash; and check that all `n + 1` "
             "terms sum to one before trusting the part you kept."),
            ("Check the two ends you already know",
             "Evaluate the same `n` at `k = n` and at `k = 1`. The first must equal the "
             "series product `Aⁿ` and the second the parallel `1 − (1 − A)ⁿ`. If either "
             "disagrees, a coefficient or an exponent is wrong."),
            ("Ask what happens to k when n grows",
             "Fixed `k` means more replicas help. `k = n` means they hurt. A majority "
             "rule means they help with diminishing returns. That single question decides "
             "whether adding a node is an improvement, and it is answered by the quorum "
             "rule rather than by the node count."),
        ],
        "worked": {
            "title": "Three nodes, and the cost of requiring all three",
            "intro": [
                "The smallest quorum question that comes up in practice, and the one "
                "where the intuition that more agreement is safer does the most damage.",
            ],
            "lines": [
                "n = 3, each node A = 99/100,  1 − A = 1/100",
                "",
                "all four terms",
                "j = 0   C(3,0)(1/100)³            = 0.000001",
                "j = 1   C(3,1)(99/100)(1/100)²    = 0.000297",
                "j = 2   C(3,2)(99/100)²(1/100)    = 0.029403",
                "j = 3   C(3,3)(99/100)³           = 0.970299",
                "                                    ────────",
                "                                    1.000000     ✓",
                "",
                "2-of-3  = 0.029403 + 0.970299 = 0.999702 = 99.97020%",
                "3-of-3  =                       0.970299 = 97.0299%",
                "1-of-1  =                                  99%",
                "",
                "downtime a year",
                "2-of-3   2 h 36 min 37.73 s",
                "3-of-3  10 d 20 h 10 min 50.74 s",
                "1-of-1   3 d 15 h 36 min",
            ],
            "after": [
                "Three nodes requiring two are a hundred times better than one node. The "
                "same three nodes requiring three are three times worse than one node, "
                "and the only thing that changed was a constant in a configuration file. "
                "The `j = 2` term, `0.029403`, is where all of the difference lives: it "
                "is the probability that exactly one node is down, which 2-of-3 survives "
                "and 3-of-3 does not.",
                "For a faded rehearsal, take `n = 5` at the same per-node 99% and work "
                "out 4-of-5. The supplied first move is that you need the terms at "
                "`j = 4` and `j = 5`, which are already listed in the material above. "
                "Produce the availability and its annual downtime, place it between the "
                "3-of-5 and 5-of-5 figures, and then answer the design question: going "
                "from three nodes to five, what must happen to `k` for the change to be "
                "an improvement at all?",
            ],
        },
        "quiz_title": "Quorums and tails",
        "quiz": [
            {"q": "Five replicas, each up with probability 99%, and the system needs all five. What is its availability?",
             "a": ["`99.999999990000%`", "`99.9990149%`", "`95.0990%`", "`99%`"],
             "c": 2,
             "why": "`k = n` collapses the tail to the single term `(99/100)⁵ = "
                    "0.9509900499`, which is the series product of five components. The "
                    "first choice is 1-of-5, the parallel form; the second is 3-of-5. "
                    "The fourth is one machine, which at `99%` is better than this "
                    "five-machine system by a factor of about fifty in downtime."},
            {"q": "Which statement about `k`-of-`n` availability is correct?",
             "a": ["Raising `n` always raises availability",
                   "Raising `n` raises availability when `k` is held fixed, and can lower it when `k` rises with `n`",
                   "Raising `n` always lowers availability, since each replica can fail",
                   "Availability depends on `k/n` only, so 2-of-4 and 3-of-6 are the same"],
             "c": 1,
             "why": "1-of-1 is `99%`, 1-of-5 is ten nines, and 5-of-5 is `95.0990%` "
                    "&mdash; all at the same per-node availability, so neither "
                    "&ldquo;always raises&rdquo; nor &ldquo;always lowers&rdquo; "
                    "survives. The last option is tempting and false: at `A = 99%`, "
                    "2-of-4 is `99.9996030%` and 3-of-6 is `99.99998524%`. The ratio is not "
                    "the variable; `k` and `n` enter separately."},
            {"q": "A three-node cluster changes its write quorum from two nodes to three. Per-node availability is 99%. What happens to write availability?",
             "a": ["It rises, because more nodes confirm each write",
                   "It is unchanged, because the same three nodes are involved",
                   "It falls from `99.97020%` to `97.0299%`",
                   "It falls, but only during a failure"],
             "c": 2,
             "why": "2-of-3 sums the `j = 2` and `j = 3` terms; 3-of-3 keeps only "
                    "`j = 3`, discarding the `0.029403` probability that exactly one node "
                    "is down. Three nines become one, and the annual write downtime goes "
                    "from about two and a half hours to nearly eleven days. More "
                    "confirmation is more durable and less available, and the two are "
                    "being traded rather than both improved."},
        ],
        "mistakes": [
            ("Assuming more replicas is more availability",
             "It depends on the quorum. Five replicas requiring five are less available "
             "than one replica requiring one &mdash; `95.0990%` against `99%` &mdash; "
             "because each addition was both a new way to survive and a new thing that "
               "had to be up. Ask what `k` does as `n` grows before claiming the node "
             "count is the improvement."),
            ("Quoting one availability for a system with two quorums",
             "Reads at 1-of-3 and writes at 3-of-3 are ten nines and one nine on the same "
             "hardware. A single headline figure for such a system is the read path's "
             "number wearing the whole system's name. Compute each operation's quorum "
             "separately and report both."),
            ("Reading the majority rule as a rule about safety only",
             "A majority quorum is chosen so that read and write sets must intersect, "
             "which is a consistency property. It also has an availability consequence, "
             "and the two can point different ways: raising `k` makes stale reads less "
             "likely and the system less available. Treating the quorum as purely a "
             "correctness knob hides the second half of the trade."),
        ],
        "standard": ("Finish when the question “should we add a node” reads as a question about k.",
                     "You should be able to sum a binomial tail exactly, recover the "
                     "series and parallel formulas from it by setting `k = n` and "
                     "`k = 1`, check the terms against a sum of one, and explain a "
                     "configuration in which five replicas are less available than one."),
        "note": 'Every formula on this course so far &mdash; the product, the parallel complement, the binomial tail &mdash; has the same premise written above it, and it has been taken on trust three times. &ldquo;Correlated Failure&rdquo; is where it is paid for: a lab cannot check an assumption, so the model reports a confident number for a system whose components share a rack, a power feed or a deploy, and the only honest thing to do is compute both figures and look at the gap.',
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "correlated-failure",
        "title": "Correlated Failure",
        "module": "Composing availability",
        "one_line": "Compute pair availability with a common-cause term and find the c at which redundancy stops paying.",
        "summary": (
            "Every formula on this course so far assumed independence. Add a shared cause "
            "that takes both machines at once with probability `c` and the pair is down "
            "with probability `c + (1 − c)p²`, not `p²`. A common cause of one part in a "
            "thousand makes a pair whose independent product is `10⁻⁴` eleven times worse, "
            "and at `c = p/(1 + p)` the second machine is buying nothing at all."
        ),
        "key": [
            "P(both down) = c + (1 − c)p²        c is a probability, never a count",
            "p = 1/100, c = 1/1000  →  0.0010999 against the promised 0.0001",
            "that is 11.00 × worse: 99.89001% rather than 99.99000%",
            "break-even   c = p/(1 + p) = 1/101 ≈ 0.009901     pair = one machine",
        ],
        "key_label": "The term the independent model leaves out",
        "concepts_intro": (
            "A lab cannot check an assumption. What it can do is compute the answer under "
            "two models and put them on the same axes, which is what this one does."
        ),
        "concepts": [
            ("A common cause is added whole and only p² is discounted",
             "Split the ways a pair goes down: a shared event takes both, with "
             "probability `c`; otherwise, with probability `1 − c`, they fail "
             "independently and both happen to be down, with probability `p²`. So "
             "`P(both down) = c + (1 − c)p²`. The first term enters at full size while "
             "the second is shrunk, which is why the curve leaves the independent line "
             "the moment `c` does."),
            ("c only has to beat p², and p² is tiny",
             "For `p = 1/100` the independent pair is `10⁻⁴`. A common cause at `10⁻³` "
               "&mdash; one chance in a thousand of an event that takes both &mdash; is "
             "ten times larger than that, and it raises `P(both down)` to `0.0010999`, "
             "eleven times what independence promised. The pair falls from four nines to "
             "two. Correlation does not need to be likely to dominate; it needs only to "
             "be likelier than a product of two small numbers."),
            ("There is a c at which the second machine is worthless",
             "Solving `c + (1 − c)p² = p` gives `c = p/(1 + p)`, exactly. Above it the "
             "pair is less available than a single machine. At `p = 1/100` that is "
             "`1/101`, about one per cent &mdash; so if a single shared event has a one "
             "per cent chance of taking both machines, the whole argument for the second "
             "machine has gone."),
        ],
        "read_title": "The common cause, the gap it opens, and where redundancy stops paying",
        "read_intro": (
            "How to write down a correlation you cannot measure precisely, what it does to "
            "the numbers from the last three lessons, and how to report a figure honestly "
            "when the assumption under it is doubtful."
        ),
        "body": [
            ("def", ("Common-cause failure",
                     "A <strong>common cause</strong> is an event that takes more than "
                     "one component at once: a power feed, a rack, a network partition, "
                     "an expired certificate, a configuration push, a deploy. Writing `c` "
                     "for the probability that such an event occurs in the period and `p` "
                     "for each component's own independent failure probability, a pair is "
                     "down together with probability `c + (1 − c)p²`. `c` is a "
                     "probability in `[0, 1]` and never a count of machines.")),
            ("p", "At `c = 0` this is exactly independence and the pair is `p²`, which is "
                  "the parallel formula of two lessons ago. The model does not replace "
                  "the earlier one; it contains it, and the earlier one is the special "
                  "case where a claim that was never checked happens to be true."),
            ("math", [
                "p = 1/100,  p² = 1/10 000 = 0.0001",
                "",
                "c = 0          P(both down) = 0.00010000     pair 99.99000%   4 nines",
                "c = 1/100 000  P(both down) = 0.00011000     pair 99.98900%   3 nines",
                "c = 1/10 000   P(both down) = 0.00019999     pair 99.98000%   3 nines",
                "c = 1/1000     P(both down) = 0.00109990     pair 99.89001%   2 nines",
                "c = 1/100      P(both down) = 0.01009900     pair 98.99010%   1 nine",
                "",
                "at c = p² exactly, P(both down) is 2.00 × the independent value",
            ]),
            ("p", "Read the middle row first. When `c` equals `p²` the correlated answer "
                  "is exactly twice the independent one, which gives a usable rule of "
                  "thumb: the independent model is trustworthy only while the shared "
                  "causes are much rarer than the product of the individual failures. "
                  "For a pair of four-nines machines that product is `10⁻⁸`, and very "
                  "little in a data centre is rarer than that."),
            ("h3", "Where the second machine stops earning its place"),
            ("thm", ("The break-even common cause",
                     "A pair is exactly as available as one machine when "
                     "`c = p/(1 + p)`.")),
            ("proof", [
                "The pair is no better than a single machine when "
                "`c + (1 − c)p² = p`.",
                "Rearranging: `c − cp² = p − p²`, so `c(1 − p²) = p(1 − p)`.",
                "Factor `1 − p² = (1 − p)(1 + p)` and divide by `1 − p`, which is "
                "positive for `p < 1`: `c(1 + p) = p`, hence `c = p/(1 + p)`.",
                "At `p = 1/100` this is `1/101 ≈ 0.009901`. Above that value the second "
                "machine is worse than useless: it adds cost, complexity and a failover "
                "path while lowering availability.",
            ]),
            ("h3", "How to report a number whose assumption you doubt"),
            ("p", "You will rarely know `c`. What you can do is bracket it: compute the "
                  "independent figure, compute the figure at a `c` you would not be "
                  "surprised by, and report both with the gap between them named. A "
                  "single number computed under an unstated assumption is the failure "
                  "mode this lesson exists to prevent, and it is not fixed by choosing a "
                  "more conservative single number."),
            ("example", ("The same pair, reported two ways",
                         "&ldquo;Two 99% machines give 99.99%&rdquo; is the independent "
                         "answer. &ldquo;Two 99% machines give 99.99% if they fail "
                         "independently, and 99.89% if one event in a thousand takes both "
                         "&mdash; they are in the same rack, so the second figure is the "
                         "one to plan against&rdquo; is the same arithmetic and a "
                         "different claim. The second sentence is what the lab is for: "
                         "move `c` up from zero and the red curve leaves the dashed "
                         "line immediately.")),
            ("p", "The practical follow-up is that `c` is the quantity to attack. "
                  "Splitting replicas across racks, power feeds, availability zones, "
                  "deploy waves and certificate authorities are all attempts to lower "
                  "`c`, and each of them is worth more than another replica once `c` is "
                  "above `p²`. The lab makes that comparison directly: a replica "
                  "multiplies `p²` by `p`, and it does not touch `c` at all."),
            ("example", ("Where correlation actually comes from",
                         "The shared deploy is the one that catches teams with "
                         "genuinely independent hardware: five replicas in five racks "
                         "across three zones, all receiving the same bad configuration "
                         "within ninety seconds. For that failure the fleet is one "
                         "machine, `c` is the probability of shipping a bad change, and "
                         "no amount of `n` in the previous lesson's binomial changes the "
                         "answer. Staged rollouts are an attempt to make `c` smaller by "
                         "making the deploy not simultaneous.")),
        ],
        "lab": ("avail", {
            "mode": "correlated",
            "p_per_10000": 100,
            "c_per_100000": 100,
            "axis_per_100000": 2000,
            "panel_title": "Move the common cause up from zero",
            "panel_intro": "The dashed line is what independence promises and the curve "
                           "is what a shared cause delivers; they part company at once, "
                           "because `c` is added whole while only `p²` is discounted. The "
                           "purple marker is the break-even `c = p/(1 + p)`, where the "
                           "pair is exactly as available as one machine.",
        }),
        "steps_title": "Auditing an availability claim for correlation",
        "steps_intro": (
            "Three of these steps happen before any arithmetic. The assumption is the thing "
            "being checked, and it is not visible in the number."
        ),
        "steps": [
            ("List what the components share",
             "Rack, power feed, network path, availability zone, deploy pipeline, "
             "configuration source, certificate authority, DNS zone, the same library "
             "version, the same on-call engineer. Anything on that list is a candidate "
             "common cause, and the deploy pipeline is the one most often forgotten "
             "because it does not appear on a topology diagram."),
            ("Put a number on c, however rough",
             "An order of magnitude is enough to decide the question. Ask how often a "
             "single event has taken the whole set out in the last two years, divide by "
             "the number of periods, and use that. A `c` you can defend to one "
             "significant figure beats an independence assumption you cannot defend at "
             "all."),
            ("Compute both figures and compare c with p²",
             "`p²` for independence, `c + (1 − c)p²` for the pair. If `c` exceeds `p²` "
             "the correlated term dominates and the independent figure is not an estimate "
             "of anything. Report the pair of numbers, not the better one."),
            ("Spend on c before spending on n",
             "Another replica multiplies the independent term by `p` and leaves `c` "
             "untouched. Separating the failure domains lowers `c` itself. Once `c` is "
             "above `p²` the second of those is the only one that moves the answer, and "
             "the break-even `c = p/(1 + p)` says where the replica has stopped being "
             "worth anything at all."),
        ],
        "worked": {
            "title": "Two database replicas in one rack",
            "intro": [
                "The independent figure is on the design document. The operations record "
                "says the rack has lost power twice in three years, which is the number "
                "the design document does not contain.",
            ],
            "lines": [
                "each replica p = 1/100 of being down in a given month",
                "",
                "what the design document says",
                "P(both down) = p² = 1/10 000 = 0.0001",
                "A = 99.99000%,  four nines,  4 min 22.80 s a month",
                "",
                "what the rack contributes",
                "2 power events in 36 months  →  c ≈ 2/36 ≈ 1/18",
                "but only some of those exceed the batteries; say one in three",
                "c ≈ 1/54 ≈ 0.01852",
                "",
                "the break-even",
                "c* = p/(1 + p) = (1/100)/(101/100) = 1/101 ≈ 0.009901",
                "c ≈ 0.01852  >  c* ≈ 0.009901",
                "",
                "so the pair is WORSE than one replica",
                "P(both down) = 0.01852 + (0.98148)(0.0001) = 0.018617",
                "A = 98.1383%  against a single replica's 99%",
            ],
            "after": [
                "The conclusion is not &ldquo;the estimate was a bit optimistic&rdquo;. "
                "The second replica, in this rack, makes the service less available than "
                "one replica would be, while doubling the cost and adding a failover "
                "path that can itself fail. Everything about the arrangement is justified "
                "by a product of two small numbers that is swamped by a term nobody wrote "
                "down.",
                "Note what fixes it and what does not. A third replica in the same rack "
                "changes `p³` and leaves `c` alone: still `0.0186`, still worse than one "
                "machine. Moving the second replica to another rack attacks `c` directly, "
                "and that is the whole of the improvement.",
                "For a faded rehearsal, keep `p = 1/100` and suppose the second replica "
                "moves to a different rack on the same power feed, which you estimate cuts "
                "`c` to `1/500`. The supplied first move is to compare that `c` with "
                "`p² = 0.0001` before computing anything. Work out `P(both down)`, the "
                "pair availability, and the factor by which it still exceeds the "
                "independent promise; then say what the next `c` to attack is.",
            ],
        },
        "quiz_title": "Common causes",
        "quiz": [
            {"q": "Two machines each fail with probability `p = 1/100`. A single event takes both with probability `c = 1/1000`. What is `P(both down)`?",
             "a": ["`0.0001`, since the common cause is smaller than `p`",
                   "`0.0010999`",
                   "`0.0011`, the sum of `c` and `p²`",
                   "`0.001`, since the common cause dominates and `p²` can be dropped"],
             "c": 1,
             "why": "`c + (1 − c)p² = 0.001 + 0.999 × 0.0001 = 0.0010999`. The third "
                    "choice adds the two terms without discounting the second, which is "
                    "close but not what the model says; the fourth drops `p²` entirely. "
                    "The first ignores `c` altogether and is what the independent formula "
                    "returns &mdash; eleven times too optimistic."},
            {"q": "At `p = 1/100`, above what common-cause probability is a pair of machines less available than a single machine?",
             "a": ["`c > 1/100`, when the common cause is as likely as an individual failure",
                   "`c > 1/101`",
                   "`c > 1/10 000`, when the common cause exceeds `p²`",
                   "There is no such point; two machines are always at least as good as one"],
             "c": 1,
             "why": "Setting `c + (1 − c)p² = p` and solving gives `c = p/(1 + p)`, which "
                    "is `1/101` here. The third option names a different and also "
                    "important threshold &mdash; above `c = p²` the correlated term "
                    "dominates the independent one &mdash; but at that point the pair is "
                    "still better than one machine, just not by what was promised. The "
                    "last option is the assumption this lesson exists to remove."},
            {"q": "Five replicas sit in five racks across three availability zones, and all five receive the same configuration push. For a bad configuration, what does the binomial tail of the previous lesson say about the fleet?",
             "a": ["Nothing useful: for that failure mode the five replicas are one machine",
                   "That the fleet survives, since a majority of racks are unaffected",
                   "That availability improves with the number of zones",
                   "That the probability of all five failing is `p⁵`, which is negligible"],
             "c": 0,
             "why": "The binomial assumes the five failures are independent. A shared "
                    "configuration push is a single event with a single probability, so "
                    "the fleet has one failure mode and `n` does not appear in it at all. "
                    "This is why staged rollouts exist: they do not make the change safer, "
                    "they make the failure non-simultaneous, which is an attack on `c`."},
        ],
        "mistakes": [
            ("Assuming independence by default, and silently",
             "The product, the parallel complement and the binomial tail are all "
             "theorems about independent events, and none of them announces its premise "
             "in the answer. Same rack, same deploy, same certificate, same zone: each "
             "of those makes the computed figure a number about a system that does not "
             "exist. The fix is to say the word &ldquo;independent&rdquo; out loud every "
             "time you multiply."),
            ("Treating c as a count of machines or of incidents",
             "`c` is the probability that one event takes the whole set in the period "
             "under discussion. &ldquo;`c = 2` because we lost two machines&rdquo; and "
             "&ldquo;`c = 3` because three racks share the feed&rdquo; both produce "
             "nonsense, and the nonsense is not obvious because the formula returns a "
             "number. Convert incidents to a rate, then to a probability per period, "
             "before it enters the formula."),
            ("Answering a correlation problem with another replica",
             "Adding a replica multiplies the independent term by `p` and does not touch "
             "`c` at all. Once `c` exceeds `p²` the extra replica is improving the "
             "smaller of the two terms, and once `c` exceeds `p/(1 + p)` the replicas are "
             "actively making things worse. Separating the failure domains is the move "
             "that changes the number."),
        ],
        "standard": ("Finish when you cannot multiply two availabilities without naming what the components share.",
                     "You should be able to compute `c + (1 − c)p²`, compare `c` with "
                     "`p²` to decide whether the independent figure means anything, "
                     "derive and use the break-even `c = p/(1 + p)`, and report a "
                     "correlated pair as two figures with the gap between them named."),
        "note": 'The five lessons so far turn a system into one fraction. What an organisation does with that fraction is a separate question, and it has an arithmetic of its own that is often mistaken for policy: a target implies a quantity of failure that may be spent, an incident spends a computable share of it, and the two are counted in failed requests rather than in minutes. &ldquo;Error Budgets&rdquo; is that arithmetic.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "error-budgets",
        "title": "Error Budgets",
        "module": "Budgets and retries",
        "one_line": "Compute a period's error budget in failed requests and the share one incident burns.",
        "summary": (
            "An objective of `99.9%` successful requests over a month permits "
            "`(1 − SLO) × requests` failures, and at a thousand requests a second that is "
            "`2 628 000` of them &mdash; the same budget as `43 min 48 s` of complete "
            "outage. An incident spends `duration × failed fraction` of it, so a "
            "half-broken hour costs half of what a dead hour costs. That last sentence is "
            "the whole difference between an objective measured on requests and one "
            "measured on the clock."
        ),
        "key": [
            "budget = (1 − SLO) × requests in the period          a count of failures",
            "burn   = rate × duration × failed fraction           what one incident spends",
            "99.9% at 1000 rps over a month: 2 628 000 failures allowed",
            "the same budget as time = (1 − SLO) × period = 43 min 48 s",
        ],
        "key_label": "A budget in failed requests, and the outage it buys",
        "concepts_intro": (
            "Three quantities and one conversion. The conversion is where an objective "
            "stops being a slogan and starts constraining what may be done this month."
        ),
        "concepts": [
            ("The budget is a count of failures",
             "An objective of `99.9%` successful requests does not forbid failure; it "
             "permits one request in a thousand to fail. Over a month at `1000` requests "
             "a second that is `2 628 000 000` requests and a budget of `2 628 000` "
             "failures. The budget is a quantity that can be spent, measured, and "
             "reported as a fraction consumed, which is what makes it useful."),
            ("An incident spends duration times severity",
             "`burn = rate × duration × failed fraction`. A thirty-minute total outage at "
             "`1000` rps burns `1 800 000` failed requests, which is `68.49%` of the "
             "month's budget. The same thirty minutes with only a tenth of requests "
             "failing burns `180 000`, or `6.85%`. Two incidents of identical length can "
             "differ tenfold in what they cost."),
            ("The same budget as time is a different number",
             "`(1 − SLO) × period` converts the budget into the length of a complete "
             "outage that would spend all of it: `43 min 48 s` a month at three nines. "
             "That figure is useful for intuition and dangerous as a measurement, because "
             "it is only the right cost when every single request is failing. Measure on "
             "requests; quote the minutes as an illustration."),
        ],
        "read_title": "Budgets, burn, and the difference between uptime and success",
        "read_intro": (
            "What the budget is, how an incident spends it, and why the same outage costs "
            "different amounts depending on a number that uptime monitoring cannot see."
        ),
        "body": [
            ("def", ("Service level objective and error budget",
                     "A <strong>service level objective</strong> fixes a target value for "
                     "an indicator over a period &mdash; here, the fraction of requests "
                     "that succeed. The <strong>error budget</strong> is the failure the "
                     "objective permits: `(1 − SLO) × N`, where `N` is the number of "
                     "requests in the period. It is a count, it is fixed when the period "
                     "begins, and it is spent by incidents until it is gone.")),
            ("math", [
                "SLO = 999/1000,  rate = 1000 rps,  month = 2 628 000 s",
                "",
                "N      = 1000 × 2 628 000      = 2 628 000 000 requests",
                "budget = (1/1000) × N          =     2 628 000 failures",
                "",
                "the same budget expressed as a complete outage",
                "(1 − SLO) × period = (1/1000) × 2 628 000 s = 2628 s = 43 min 48 s",
            ]),
            ("p", "Both lines describe the same permission and the second is the one "
                  "everybody quotes. Note the period it belongs to: a month here is "
                  "`2 628 000` seconds, a twelfth of a 365-day year. Under a 30-day "
                  "convention the same three nines would be `2592` seconds, or 43.2 "
                  "minutes. Neither is wrong and mixing them is."),
            ("h3", "What an incident actually spends"),
            ("p", "The burn is `rate × duration × failed fraction`, and the third factor "
                  "is the one that uptime monitoring does not have. A service returning "
                  "errors to one request in ten is not down by any binary measure, and it "
                  "is spending budget the whole time. Conversely a two-minute total "
                  "outage at three in the morning, at a tenth of the daytime rate, costs "
                  "a tenth of what the same two minutes would cost at noon."),
            ("math", [
                "a 30-minute incident at 1000 rps, against a 2 628 000 budget",
                "",
                "severity   failed requests   share of budget   minutes that spend it all",
                " 10%           180 000            6.85%              438.0",
                " 25%           450 000           17.12%              175.2",
                " 50%           900 000           34.25%               87.6",
                "100%         1 800 000           68.49%               43.8",
            ]),
            ("p", "The last column is the budget in minutes at each severity, and the "
                  "bottom row is the familiar `43.8` &mdash; which is the point. The "
                  "&ldquo;43.8 minutes a month&rdquo; figure is the special case of a "
                  "full outage, and quoting it as though it were the budget itself "
                  "understates by a factor of ten what a long partial degradation is "
                  "allowed to cost."),
            ("h3", "Where the arithmetic stops"),
            ("p", "Everything above is computation. What to do when the budget is spent "
                  "&mdash; freeze releases, divert the team to reliability work, revise "
                  "the objective, accept the overrun &mdash; is a policy decision that "
                  "the arithmetic informs and does not make. The value of separating them "
                  "is that the argument about policy then happens over an agreed number "
                  "rather than over whose impression of last month is right."),
            ("example", ("One incident, and what is left",
                         "A thirty-minute total outage at `1000` rps against a three-nines "
                         "monthly objective burns `1 800 000` of `2 628 000` failures: "
                         "`68.49%` of the month, gone, on day three. `828 000` failures "
                         "remain, which is another `13.8` minutes of full outage or "
                         "`138` minutes at ten per cent severity. That is a concrete "
                         "statement about what the rest of the month can afford, and it "
                         "is available within minutes of the incident ending.")),
            ("example", ("The objective that was already impossible",
                         "Set the lab's objective to four nines and leave the incident "
                         "at thirty minutes: the budget is `262 800` failures and the "
                         "single incident burns `684.93%` of it. A month's budget at "
                         "four nines is `4 min 22.8 s` of full outage, so one "
                         "half-hour incident overruns the whole month&rsquo;s budget nearly "
                         "seven times over. An objective that a single "
                         "ordinary incident cannot fit inside is not a target, and the "
                         "arithmetic says so before anyone has to argue about it.")),
            ("p", "One measurement caution. The budget is defined against the requests in "
                  "the period, so a traffic-weighted objective forgives failures during "
                  "quiet hours and punishes them at peak, which may or may not match what "
                  "users experience. If ten customers each send a thousand requests and "
                  "one sends a million, a request-weighted objective is mostly about that "
                  "one customer. The arithmetic here is exact; what it is exact about is "
                  "a choice that has to be made deliberately."),
        ],
        "lab": ("avail", {
            "mode": "budget",
            "slo": "999/1000",
            "rps": 1000,
            "incident_minutes": 30,
            "severity_pct": 100,
            "incidents": 1,
            "panel_title": "Set the SLO and the incident",
            "panel_intro": "Three nines at a thousand requests a second, with one "
                           "thirty-minute total outage. The budget prints in failed "
                           "requests and in the minutes of complete outage it buys; the "
                           "severity column shows the same incident costing ten different "
                           "amounts. Move the severity slider before you move anything else.",
        }),
        "steps_title": "Computing and spending a budget",
        "steps_intro": (
            "The first step is the one that gets skipped, and skipping it is what turns an "
            "objective into an argument."
        ),
        "steps": [
            ("Say what the indicator counts, and over what period",
             "Successful requests out of total requests, over a calendar month, measured "
             "at a named place. Each of those choices changes the number: measured at the "
             "load balancer or in the client, counting all endpoints or the ones users "
             "care about, a rolling window or a calendar one."),
            ("Multiply to get the budget as a count",
             "`budget = (1 − SLO) × N`, where `N` is the requests in the period. At "
             "`1000` rps over a month that is `(1/1000) × 2 628 000 000 = 2 628 000` "
             "failures. Keep it as a count; converting to minutes too early is what "
             "loses the severity."),
            ("Price each incident as duration times severity",
             "`burn = rate × duration × failed fraction`. Use the rate that actually "
             "applied during the incident rather than the monthly average, and use the "
             "measured failed fraction rather than the fact that an alert fired."),
            ("Report the share spent and what remains",
             "A percentage of the budget consumed, and the remainder expressed both as "
             "failures and as the minutes of outage it would buy. Then, separately, the "
             "policy question &mdash; the arithmetic has nothing to say about that and "
             "should not pretend to."),
        ],
        "worked": {
            "title": "Two incidents in one month, one of them not an outage at all",
            "intro": [
                "A month with one short total outage and one long partial degradation. "
                "Uptime monitoring saw one of them. The budget sees both, and prices "
                "the invisible one higher.",
            ],
            "lines": [
                "SLO = 99.9% of requests,  rate = 2000 rps,  month = 2 628 000 s",
                "",
                "N      = 2000 × 2 628 000 = 5 256 000 000 requests",
                "budget = (1/1000) × N     =     5 256 000 failures",
                "       = (1/1000) × 2 628 000 s = 43 min 48 s of complete outage",
                "",
                "incident A   8 minutes, 100% of requests failing",
                "burn = 2000 × 480 × 1.00 =   960 000      18.26% of the budget",
                "",
                "incident B   6 hours, 15% of requests failing",
                "burn = 2000 × 21 600 × 0.15 = 6 480 000   123.29% of the budget",
                "",
                "total spent = 7 440 000 = 141.55% of the month",
                "remaining   = −2 184 000        the budget is gone",
                "",
                "what an uptime measure would have recorded",
                "downtime = 8 min against a 43 min 48 s allowance = 18.26%",
                "verdict: comfortably inside the objective",
            ],
            "after": [
                "The two verdicts disagree completely, and the second one is wrong. "
                "Incident B failed one request in seven for six hours and never took the "
                "service down, so every binary uptime check passed throughout; it spent "
                "more than the entire month's budget on its own. The request-weighted "
                "measure sees it because severity is one of its factors and is not one "
                "of uptime's.",
                "Notice also that `43 min 48 s` appears here as an illustration and is "
                "not what was measured. The measurement is `7 440 000` failed requests "
                "against `5 256 000` allowed. The minutes are useful for explaining the "
                "size of the budget to someone and are the wrong instrument for spending "
                "it.",
                "For a faded rehearsal, keep the same objective and rate and suppose the "
                "team wants to know how long a `5%`-severity degradation may run before "
                "it exhausts the month. The supplied first move is that severity enters "
                "the burn as a multiplier, so the answer is the budget divided by "
                "`rate × severity`. Compute the minutes, check them against the lab's "
                "severity table, and then state what that duration implies about how "
                "quickly a partial degradation has to be detected.",
            ],
        },
        "quiz_title": "Budgets and burn",
        "quiz": [
            {"q": "An objective of `99.9%` successful requests, at `1000` rps over a month of `2 628 000` seconds. How many failed requests does the budget permit?",
             "a": ["`2 628 000`", "`2 628 000 000`", "`2628`", "`43.8`"],
             "c": 0,
             "why": "`N = 1000 × 2 628 000 = 2 628 000 000` requests, and the budget is "
                    "one thousandth of that. The second choice is the total request "
                    "count, not the budget. `2628` is the budget in seconds of complete "
                    "outage and `43.8` is the same figure in minutes &mdash; both are "
                    "the budget expressed as time, which is a different unit from a "
                    "count of failures."},
            {"q": "Two incidents, each thirty minutes at `1000` rps. One fails every request; the other fails one request in ten. How do their costs compare?",
             "a": ["They cost the same, since they lasted the same time",
                   "The total outage costs ten times as much: `1 800 000` failures against `180 000`",
                   "The total outage costs twice as much, since severity is capped",
                   "The partial one costs more, because it lasted undetected"],
             "c": 1,
             "why": "`burn = rate × duration × severity`, so severity scales the cost "
                    "linearly: `68.49%` of the month's budget against `6.85%`. The first "
                    "option is exactly the error that measuring on uptime produces "
                    "&mdash; a binary up-or-down measure has no severity factor, so the "
                    "two incidents are indistinguishable to it."},
            {"q": "A team measures its `99.9%` objective as uptime: minutes when the service answered at all, out of minutes in the month. What does that measurement systematically miss?",
             "a": ["Nothing; uptime and success ratio agree when the period is long enough",
                   "Partial failure, which costs `duration × failed fraction` and registers as full uptime",
                   "Only incidents shorter than one minute",
                   "The difference between a 30-day month and `2 628 000` seconds"],
             "c": 1,
             "why": "A service failing `15%` of requests for six hours is up the whole "
                    "time by a binary measure and, at `2000` rps against a three-nines "
                    "budget, has spent `123%` of the month. The period convention in the "
                    "last option is a real bookkeeping hazard and a much smaller one "
                    "&mdash; about `1.4%` &mdash; than the factor of ten that severity "
                    "can hide."},
        ],
        "mistakes": [
            ("Measuring the objective on uptime when it is a success ratio",
             "Uptime has no severity factor, so a long partial degradation registers as a "
             "perfect month. Six hours at `15%` failure can spend more than the whole "
               "budget while every availability check stays green. If the objective is "
             "about requests, the measurement has to count requests."),
            ("Quoting the budget only as minutes",
             "&ldquo;43.8 minutes a month&rdquo; is the budget on the assumption that "
             "every request fails throughout, which is the least likely incident shape "
             "there is. Used as the measurement it understates a partial outage by the "
             "reciprocal of its severity &mdash; a factor of ten at `10%`. Quote the "
             "count; keep the minutes as an illustration of its size."),
            ("Confusing the arithmetic with the policy",
             "&ldquo;We have spent 68% of the budget&rdquo; is a computation and is not "
             "in dispute. &ldquo;Therefore we freeze releases&rdquo; is a decision that "
             "reasonable people can disagree about. Presenting the second as though it "
             "followed from the first makes the arithmetic contentious, which is the one "
             "thing it should never be."),
        ],
        "standard": ("Finish when you would price an incident by its severity before asking how long it lasted.",
                     "You should be able to compute a budget as a count of failures, "
                     "convert it to an equivalent full outage and say why that conversion "
                     "is an illustration rather than a measurement, price an incident as "
                     "`rate × duration × severity`, and report the share spent without "
                     "attaching a policy to it."),
        "note": 'Every lesson so far has treated the load on a system as given from outside. It is not: a failing service produces load of its own, because a client that does not get an answer asks again. &ldquo;Retries and Request Amplification&rdquo; puts a number on that extra load, and the number has an unpleasant property &mdash; it is largest exactly when the service is least able to carry it.',
    },
]
