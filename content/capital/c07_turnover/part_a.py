"""The Turnover of Capital, lessons 1-6 -- Volume II, Chapters 7 to 12.

Every quotation is copied from /mnt/project-files/capital-texts/volume-2-kerr.txt
(the Kerr edition of Volume II); the comment beside each lesson gives its line
numbers. Footnote numerals in the text are left out of the quotations, the
page markers the edition interleaves ("Edition: current; Page: [...]") are
dropped where a quotation runs across one, and the translator's double
quotation marks inside a quotation are printed as single curly quotes. The
translator's spellings ("labor", "turn-over") stand inside quotation marks.
Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 2, l. 1453 and l. 1455 (the year as the unit; n = T/t);
    # l. 1432 (turnover time); l. 1446 (Newman); l. 1449 (turnover as a
    # periodical process); l. 1457 (eighteen months); l. 1459 (the time for
    # which capital is advanced).
    {
        "slug": "turnover-time-and-number-of-turnovers",
        "title": "Turnover Time and the Number of Turnovers",
        "module": "Chapter 7 · The Period and Number of Turn-Overs",
        "one_line": "A capital's turnover is its circuit taken as a period that repeats, and the turnovers in a year are the year divided by that period.",
        "summary": (
            "Chapter 7 takes the circuit of Part I and treats it as a period that repeats: "
            "its length is the production time plus the circulation time, and the year is "
            "the unit it is measured against. Compute the turnover time, the number of "
            "turnovers a year as `n = T/t`, and the value turned over in a year against "
            "the capital advanced, which does not grow with the number of turnovers."
        ),
        "key": [
            "turnover time t = production + circulation",
            "the unit of measure is the year, T",
            "turnovers a year  n = T / t",
            "value turned over = capital · n",
            "the capital advanced does not grow",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "The chapter is four pages long. It takes the circuit of Part I and asks a new "
            "question of it: how often?"
        ),
        "concepts": [
            ("Turnover",
             "The circuit of a capital taken as a process that repeats, not as a single "
             "event. It runs from the advance of capital-value in one form to its return in "
             "that same form, ready to go round again."),
            ("Turnover time",
             "The production time plus the circulation time: how long the capital-value is "
             "away before it is back in the form it was advanced in. For the capitalist it "
             "is the time for which he must advance the capital."),
            ("Number of turnovers",
             "The year divided by the turnover time, `n = T/t`. A turnover time of three "
             "months gives 4; eighteen months gives `2/3`, a capital that completes only "
             "two-thirds of a turnover within the year."),
        ],
        "read_title": "The year as the unit, then the chapter line by line",
        "read_intro": (
            "Volume II is Engels' edition of the manuscripts Marx left, and this is one of "
            "its shortest chapters. Its central passage gives the unit and the notation "
            "together."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 7.</strong> &ldquo;Just as the working day is "
                  "the natural unit for the function of labor-power, so the year is the "
                  "natural unit for the periods of turn-over of rotating capital. The "
                  "natural basis of this unit is found in the fact that the most important "
                  "crops of the temperate zone, which is the mother country of capitalist "
                  "production, are annual products. &hellip; If we designate the year as the "
                  "unit of the time of turn-over by T, the time of turn-over of a given "
                  "capital by t, and the number of its turn-overs by n, then n = T/t.&rdquo;"),
            ("p", "You know the working day from Volume I: labour-power is bought by the day, "
                  "and the day is cut into necessary and surplus labour. Marx now wants the "
                  "matching unit for capital, and he chooses the year. His reason is "
                  "agricultural: the main crops of the temperate zone, "
                  "where capitalist production grew up, come once a year. Nothing in the "
                  "arithmetic depends on the reason. The year is a yardstick, and the rest of "
                  "Part II measures everything against it."),
            ("p", "Go back to how the chapter opens. It recalls Part I: the whole time of "
                  "rotation of a capital &ldquo;is equal to the sum of its time of circulation "
                  "plus its time of production&rdquo;. Production time is the stretch in which "
                  "the capital is in the workshop as means of production and labour-power; "
                  "circulation time is the stretch in which it is a commodity waiting to be "
                  "sold or money waiting to be laid out. Both count. A capital whose goods sit "
                  "in a warehouse is away from its owner just as surely as one whose goods are "
                  "still on the loom."),
            ("p", "Then Marx asks which of the three circuits of Part I to measure. "
                  "M&hellip;M′ shows best what turnover does to surplus value, and P&hellip;P "
                  "what it does to the product. C′&hellip;C′ will not do, because it starts "
                  "from the whole product, surplus value included, and not from the value "
                  "advanced. The economists, he says, never separated these. S. P. Newman, an "
                  "American textbook writer, measured &ldquo;the whole course of production, "
                  "from the time that outlays are made till returns are received&rdquo;; "
                  "Thomas Chalmers, the Scottish preacher and economist, began the cycle at "
                  "the moment the receipts come in. Each took one circuit for the whole "
                  "thing."),
            ("p", "Marx's own definition comes in one sentence: &ldquo;The rotation of capital, "
                  "considered as a periodical process, not as an individual event, constitutes "
                  "its turn-over.&rdquo; The single circuit is &ldquo;but a fragment in the "
                  "life of capital&rdquo;. What matters about a turnover is that it happens "
                  "again, and so it can be counted."),
            ("p", "Now read the notation as Marx uses it. T is the year, t the turnover time of "
                  "one capital, n the turnovers it makes in the year. A turnover time of three "
                  "months gives `n = 12/3 = 4`. Eighteen months gives `n = 12/18 = 2/3`: the "
                  "capital &ldquo;completes only two-thirds of its turn-over in one "
                  "year&rdquo;. A number of turnovers below 1 is not a mistake; it is a "
                  "capital that is away for longer than a year."),
            ("p", "The chapter's last definition is the one the rest of Part II builds on:"),
            ("p", "<strong>Volume II, Chapter 7.</strong> &ldquo;From the point of view of the "
                  "capitalist, the time of turn-over is the time for which he must advance his "
                  "capital in order to create value with it and have it returned in its "
                  "original form.&rdquo;"),
            ("p", "That sentence is why the count matters. The lab measures in weeks, with a "
                  "52-week year. Marx's three months is 13 weeks; split it, for the sake of "
                  "the example, into 9 weeks of production and 4 of circulation, and £400 "
                  "advanced turns over 4 times: £1,600 of value passes through the capital in "
                  "the year. The capital advanced is still £400, because the same £400 goes "
                  "round four times. At five weeks the same arithmetic gives `52/5` turnovers, "
                  "and at Marx's eighteen months, 78 weeks, £600 advanced turns over only £400 "
                  "of value within the year."),
            ("p", "So a turnover is a period that repeats, and its count is a division. Before "
                  "a whole capital's turnover can be counted, though, Marx has to deal with the "
                  "parts of it that do not go round at the same pace. The next lesson, “Fixed "
                  "Capital and Circulating Capital”, asks what it means for a machine to "
                  "return its value a little at a time."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "time",
            "money_unit": "£",
            "preset": "three-months",
            "presets": [
                {"id": "three-months", "label": "Marx's t of three months: 13 weeks, £400 advanced",
                 "production_weeks": 9, "circulation_weeks": 4, "year_weeks": 52, "capital": 400,
                 "expect": {"tuTurnover": "13 weeks", "tuTurnovers": "4 a year (a 52-week year)", "tuWorkingShare": "1 = 100%", "tuCirculationShare": "4/13 = 30.77%", "tuAggregate": "£1,600 turned over on £400 advanced"}},
                {"id": "five-weeks", "label": "A five-week turnover, £500 advanced",
                 "production_weeks": 4, "circulation_weeks": 1, "year_weeks": 52, "capital": 500,
                 "expect": {"tuTurnover": "5 weeks", "tuTurnovers": "52/5 a year (a 52-week year)", "tuWorkingShare": "1 = 100%", "tuCirculationShare": "1/5 = 20%", "tuAggregate": "£5,200 turned over on £500 advanced"}},
                {"id": "eighteen-months", "label": "Marx's t of eighteen months: 78 weeks, £600 advanced",
                 "production_weeks": 65, "circulation_weeks": 13, "year_weeks": 52, "capital": 600,
                 "expect": {"tuTurnover": "78 weeks", "tuTurnovers": "2/3 a year (a 52-week year)", "tuWorkingShare": "1 = 100%", "tuCirculationShare": "1/6 = 16.67%", "tuAggregate": "£400 turned over on £600 advanced"}},
            ],
            "panel_title": "How often a capital goes round",
            "panel_intro": (
                "The production and circulation times go in, in weeks, with a 52-week year. "
                "The lab adds them for the turnover time, divides the year by it, and "
                "multiplies the capital advanced by the turnovers. Compare the last tile "
                "with the capital you typed: one moves, the other does not."
            ),
        }),
        "steps_title": "Counting turnovers",
        "steps_intro": "Four steps for any capital whose times are known.",
        "steps": [
            ("Add the two times",
             "The turnover time is the production time plus the circulation time. Leave "
             "neither out: time spent waiting to be sold is part of the turnover."),
            ("Use the year's unit",
             "Express the turnover time in the same unit as the year, weeks against a "
             "52-week year or months against twelve."),
            ("Divide",
             "The number of turnovers is the year divided by the turnover time. A turnover "
             "longer than the year gives a number below 1."),
            ("Separate value turned over from capital advanced",
             "Multiply the capital advanced by the number of turnovers for the value turned "
             "over in the year. The capital advanced is the sum that goes round, and it "
             "stays as it was."),
        ],
        "worked": {
            "title": "Three months, four turnovers",
            "intro": [
                "Take Marx's turnover time of three months, as 9 weeks of production and 4 of "
                "circulation in a 52-week year, with £400 advanced. You want the turnovers, "
                "the value turned over and the capital advanced.",
            ],
            "lines": [
                "t = 9 + 4 = 13 weeks",
                "n = T / t = 52 / 13 = 4",
                "value turned over = 4 · £400 = £1,600",
                "capital advanced = £400",
            ],
            "after": [
                "Stretch the turnover to 78 weeks, Marx's eighteen months, and "
                "`n = 52/78 = 2/3`: £600 advanced turns over £400 of value in the year, and "
                "the capital advanced is still £600.",
            ],
        },
        "quiz_title": "Turnover time and turnovers",
        "quiz": [
            {"q": "A capital's turnover time is four months. How many turnovers does it make "
                  "in a year?",
             "a": ["3", "4", "1/3", "8"],
             "c": 0,
             "why": "`n = T/t = 12/4 = 3`. Four is the turnover time, not the count; `1/3` "
                    "divides the wrong way round, giving the fraction of a year one turnover "
                    "takes; 8 is the months left over."},
            {"q": "Production takes 10 weeks and circulation 3 in a 52-week year. How many "
                  "turnovers does the capital make?",
             "a": ["26/5", "4", "52/3", "13"],
             "c": 1,
             "why": "The turnover time is `10 + 3 = 13` weeks and `52/13 = 4`. `26/5` divides "
                    "by the production time alone and `52/3` by the circulation time alone; 13 "
                    "is the turnover time in weeks."},
            {"q": "A capital of £300 turns over 6 times a year. On the chapter's definitions, "
                  "what is the capital advanced?",
             "a": ["£1,800", "£50", "£300", "£2,100"],
             "c": 2,
             "why": "The same £300 goes round six times, so £300 is advanced and £1,800 of "
                    "value is turned over in the year. £1,800 is the value turned over, £50 "
                    "divides instead of multiplying, and £2,100 adds the two."},
            {"q": "Which of the three circuits does Marx say cannot serve for the study of "
                  "turnover?",
             "a": ["M…M′, because it shows only money",
                   "P…P, because it shows only the product",
                   "C′…C′, because it starts from an expanded value, not from the value advanced",
                   "None of them; turnover needs a fourth circuit"],
             "c": 2,
             "why": "Turnover begins with the advance of capital-value and ends with its "
                    "return in the same form. C′…C′ begins with the whole product, surplus "
                    "value included. Marx uses M…M′ for turnover's effect on surplus value and "
                    "P…P for its effect on the product, and he needs no fourth circuit."},
        ],
        "mistakes": [
            ("Thinking a capital that turns over twice a year is twice the capital",
             "Turnovers multiply the value that passes through a capital, not the capital. In "
             "the first preset £400 turns over 4 times: the tile reads £1,600 turned over on "
             "£400 advanced. At no moment does the capitalist hold more than £400 of capital "
             "in this business; the same sum is advanced, returns and is advanced again."),
            ("Timing the turnover by production alone",
             "Turnover time is production time plus circulation time. Goods waiting in a "
             "warehouse or money waiting to be laid out are capital away from its owner. In "
             "the first preset dropping the 4 weeks of circulation would give `52/9` "
             "turnovers instead of 4."),
            ("Treating fewer than one turnover a year as an error",
             "Marx's own example of eighteen months gives `2/3`. A capital tied up for longer "
             "than a year completes only part of a turnover within it, and the eighteen-month "
             "preset turns over £400 of value on £600 advanced."),
        ],
        "standard": (
            "Finish when you can count a capital's turnovers in a year.",
            "Given a production time and a circulation time, compute the turnover time, the "
            "number of turnovers in a year, and the value turned over in the year on a "
            "stated capital advanced."
        ),
        "note": (
            "The lab counts turnovers as if every one were identical and the year began with "
            "the first; Marx's own tables in Chapter 15 show the last turnover of a year "
            "running on into the next. The splits of Marx's three months into 9 weeks of "
            "production and 4 of circulation, and of his eighteen months into 65 and 13, "
            "are illustrative; the chapter gives only the totals."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 2, l. 1479 (the passage: fixed capital circulates piecemeal);
    # l. 1487 (the ox); l. 1489 (the manner of circulation decides); l. 1499
    # (the fundamental mistake); l. 1514 (a ten-year machine, the reserve
    # fund); l. 1525 (circulating capital); l. 1541 (circulation capital);
    # l. 1557 and l. 1564 (railway lifetimes, Lardner's virtual wear); l. 1568
    # (competition); l. 1598 (the £10,000 machine and its repairs); l. 1614
    # (fifteen years booked as ten); l. 1630 (railway dividends).
    {
        "slug": "fixed-and-circulating-capital",
        "title": "Fixed Capital and Circulating Capital",
        "module": "Chapter 8 · Fixed Capital and Circulating Capital",
        "one_line": "A machine passes its value to the product piecemeal while its body stays in the workshop, and that manner of circulating, not its durability or its immobility, is what makes it fixed capital.",
        "summary": (
            "Part of productive capital returns its value at once, with every product sold; "
            "part returns it a little at a time while its body stays in production. Compute "
            "the value a fixed capital transfers each year from its value and life, the value "
            "still locked in it after so many years, and what repairs and a cheaper machine "
            "of the same kind do to both."
        ),
        "key": [
            "fixed: value circulates piecemeal",
            "circulating: value returns whole each time",
            "wear a year = value / life",
            "left = value · (life − years used)/life",
            "not the same cut as constant and variable",
        ],
        "key_label": "Two ways of returning value",
        "concepts_intro": (
            "Every part of a productive capital sends its value round the circuit. The "
            "chapter is about the two different paces at which it does so."
        ),
        "concepts": [
            ("Fixed capital",
             "The part of productive capital whose value passes into the product only "
             "gradually, by wear, while its body stays in the process of production: "
             "machines, buildings, working animals, soil improvements. What fixes it is the "
             "manner in which its value circulates."),
            ("Circulating capital",
             "Every other part of productive capital: raw and auxiliary materials and the "
             "capital paid for labour-power. Its whole value passes into each product and "
             "must be replaced in full from each sale."),
            ("Wear and repair",
             "Wear is the value fixed capital transfers on average as its use-value is used "
             "up, reckoned over its average life. Repairs are a separate, additional outlay "
             "that keeps it alive for that life; Marx says they fit neither category "
             "cleanly, but belong with more justification to circulating capital."),
        ],
        "read_title": "Value that circulates piecemeal, then the chapter line by line",
        "read_intro": (
            "Section 1 builds the distinction from what a machine does in the workshop. The "
            "passage below is where it gets its name."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 8, §1.</strong> &ldquo;In the first place, it does "
                  "not circulate in its use-form, but it is merely its exchange-value which "
                  "circulates, and this takes place gradually and piecemeal, in proportion as "
                  "it is transferred to the product which circulates as a commodity. During "
                  "the entire period of its service, a portion of its value always remains "
                  "fixed in it, independent of the commodities which it helps to produce. It "
                  "is this peculiarity which gives to this portion of capital the character "
                  "of fixed capital.&rdquo;"),
            ("p", "Think of a spinning machine. Every week yarn leaves the mill and is sold, "
                  "and a little of the machine's value goes with it, as wear. The machine "
                  "itself never leaves. Its value is now in two places: one part still in the "
                  "machine, the other already turned back into money with the yarn. Marx's "
                  "example is a machine that lasts ten years: its value comes back piecemeal "
                  "over the ten, &ldquo;Until this time arrives, its value is meanwhile "
                  "accumulated in the form of a reserve fund of money&rdquo;, and only then is "
                  "the money turned back into a machine. That is a turnover of ten years."),
            ("p", "What makes a thing fixed capital is &ldquo;exclusively the peculiar manner "
                  "in which this value circulates&rdquo;, and that follows from what the thing "
                  "does in the labour process. The same object can be either. &ldquo;An ox is "
                  "fixed capital, so long as it is a beast of toil. If it is eaten, it does not "
                  "perform the functions of an instrument of production, and is, therefore, "
                  "not fixed capital.&rdquo; Immobility does not decide it either: a factory "
                  "building and a locomotive are both fixed capital, and a machine sitting in "
                  "its maker's warehouse is not fixed capital at all, only a commodity for "
                  "sale."),
            ("p", "Everything else in productive capital is circulating capital: the cotton, "
                  "the coal and the wages. Here Marx sets two things side by side that Volume I "
                  "kept apart. As constant capital the cotton only transfers its value, while "
                  "labour-power creates new value; but in the way their value comes back, "
                  "wholly and with each sale, the two are alike. &ldquo;It is these elements of "
                  "productive capital&mdash;the values invested in labor-power and in means of "
                  "production which are not fixed capital&mdash;that by their common "
                  "characteristics of turn-over constitute the circulating capital as opposed "
                  "to the fixed capital.&rdquo;"),
            ("p", "So the same capital can be cut two ways, and Marx says plainly which mistake "
                  "he is watching for: &ldquo;the confounding of the categories &lsquo;fixed "
                  "capital and circulating capital&rsquo; with the categories &lsquo;constant "
                  "capital and variable capital&rsquo;&rdquo;. Fixed against circulating is a "
                  "difference in how value returns. Constant against variable is a difference "
                  "in whether new value is created. Cotton is circulating and constant; wages "
                  "are circulating and variable; a machine is fixed and constant. Nothing is "
                  "fixed and variable. The next three lessons follow this mistake through "
                  "Smith and Ricardo."),
            ("p", "One more limit: only productive capital divides this way. Money capital and "
                  "commodity capital spend their lives in circulation, but they are &ldquo;not "
                  "circulating capital as opposed to fixed capital&rdquo;. Yarn in a "
                  "warehouse carries the value of both the cotton and the machine's wear."),
            ("p", "Section 2 turns to the railways, which were the great fixed capital of "
                  "Marx's day. The engineers had expected rails to last a century; they lasted "
                  "about twenty years, ties twelve to fifteen, a locomotive ten to twelve. And "
                  "there is a second kind of wear that has nothing to do with use. Dionysius "
                  "Lardner, the Irish writer on science and railway economy, reported that "
                  "cars and locomotives that cost £40,000 could be bought ten years later for "
                  "£30,000. Marx calls this virtual wear here; in Volume I, Chapter 15 he "
                  "called it moral depreciation. He adds that &ldquo;competition enforces the introduction "
                  "of new machinery before the old is worn out&rdquo;."),
            ("p", "Repairs are a separate account:"),
            ("p", "<strong>Volume II, Chapter 8, §2.</strong> &ldquo;For instance, if the value "
                  "of the fixed capital is 10,000 pounds sterling, and its total life-time 10 "
                  "years, then these 10,000 pounds, having been entirely converted into money "
                  "after the lapse of ten years, will replace only the value of the capital "
                  "originally invested, but they do not replace the value of the capital, or "
                  "labor, added in the meantime for repairs.&rdquo;"),
            ("p", "Repairs are advanced as they come, irregularly, and charged to the product "
                  "on the average of the branch. Many businesses, Marx notes, fold them into "
                  "the wear: a fixed capital of £10,000 that lasts 15 years wears `2,000/3` a "
                  "year, but is booked as if it lasted 10, at £1,000 a year, and the extra "
                  "`1,000/3` pays for the repairs that let it last the fifteen. He notes how "
                  "elastic the boundary between repair and renewal could be: moving repairs to the capital account &ldquo;is the "
                  "familiar method by which railway managements artificially inflate their "
                  "dividends&rdquo;."),
            ("p", "The lab computes three cases. Marx's £10,000 machine on a ten-year life "
                  "transfers £1,000 a year, and after four years £6,000 is still locked in it. "
                  "His fifteen-year machine booked at ten transfers the same £1,000 a year, "
                  "repairs included, and after three years £8,000 is still in it. Then a "
                  "machine of the same kind appears at half the price in the fourth year: the "
                  "old one is now worth what the new one would be, worn to the same age: it "
                  "passes on £500 a year instead of £1,000, £3,000 is left in it, and another "
                  "£3,000 has gone without any wear at all."),
            ("p", "Fixed capital comes back slowly and circulating capital quickly. The next "
                  "lesson, “The Aggregate Turnover of Advanced Capital”, asks how the two can "
                  "be added into one turnover for the whole capital."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "fixed",
            "money_unit": "£",
            "preset": "ten-years",
            "presets": [
                {"id": "ten-years", "label": "Marx's £10,000 machine, a 10-year life, after 4 years",
                 "fixed": [{"name": "machine", "value": 10000, "life_years": 10}],
                 "age_years": 4, "expect": {"tuWear": "£1,000 a year", "tuRemaining": "£6,000 after 4 years"}},
                {"id": "repairs", "label": "Marx's 15-year machine booked at 10: repairs in the wear, after 3 years",
                 "fixed": [{"name": "machine", "value": 10000, "life_years": 15,
                            "repairs_per_year": "1000/3"}],
                 "age_years": 3, "expect": {"tuWear": "£1,000 a year", "tuRemaining": "£8,000 after 3 years"}},
                {"id": "moral", "label": "A machine of the same kind at half the price appears in year 4",
                 "fixed": [{"name": "machine", "value": 10000, "life_years": 10,
                            "replacement_value": 5000, "appears_year": 4}],
                 "age_years": 4, "expect": {"tuWear": "£500 a year", "tuRemaining": "£3,000 after 4 years"}},
            ],
            "panel_title": "What a machine passes on, and what it keeps",
            "panel_intro": (
                "Each item of fixed capital goes in with its value and life, and optionally "
                "its yearly repairs and a cheaper replacement and the year it appears. The "
                "lab computes the value transferred a year and the value still locked in "
                "after the years in use. Step through the presets and watch the second tile."
            ),
        }),
        "steps_title": "Computing what fixed capital transfers",
        "steps_intro": "Four steps for any item of fixed capital.",
        "steps": [
            ("Divide value by life",
             "The yearly wear is the value of the item divided by its average life in years. "
             "This is the value it passes to the year's product."),
            ("Add the average repairs",
             "Repairs are an additional outlay. Where they are charged on the yearly "
             "average, add them to the wear for the yearly charge to the product."),
            ("Compute what is left",
             "After so many years the value still locked in is the value times the years "
             "remaining over the life. The rest has gone into products, and back into money."),
            ("Revalue for a cheaper replacement",
             "If an identical machine can now be had for less, the old one is worth what the "
             "new one would be at the same age. Use the replacement value from that year on; "
             "the difference is lost without any wear."),
        ],
        "worked": {
            "title": "A £10,000 machine after four years",
            "intro": [
                "Take Marx's machine: £10,000, an average life of ten years. You want the "
                "value it transfers each year and the value still in it after four years.",
            ],
            "lines": [
                "wear a year = £10,000 / 10 = £1,000",
                "transferred in 4 years = 4 · £1,000 = £4,000",
                "left = £10,000 · 6/10 = £6,000",
            ],
            "after": [
                "If an identical machine costing £5,000 appears in the fourth year, the old one "
                "is revalued at £5,000 worn for four years: £3,000 is left, and the other "
                "£3,000 of the £6,000 has gone without the machine being used any harder.",
            ],
        },
        "quiz_title": "Fixed and circulating capital",
        "quiz": [
            {"q": "A machine worth £6,000 has an average life of 12 years. What value does it "
                  "pass to the product each year, on the chapter's averages?",
             "a": ["£500", "£6,000", "£72,000", "£12"],
             "c": 0,
             "why": "`6,000/12 = 500`. £6,000 would be the whole value in one year, £72,000 "
                    "multiplies instead of dividing, and £12 is the life in years with a pound "
                    "sign."},
            {"q": "On the chapter's definitions, which of these is circulating capital?",
             "a": ["A factory building",
                   "A locomotive in use on a railway",
                   "An ox used for ploughing",
                   "The coal burned under a steam engine"],
             "c": 3,
             "why": "The coal is wholly consumed in each round of production and its whole "
                    "value passes into the product. The building, the locomotive and the "
                    "ploughing ox each pass on their value piecemeal while staying in "
                    "production, which makes all three fixed capital, mobile or not."},
            {"q": "A finished machine stands in its maker's warehouse waiting for a buyer. "
                  "What is it, for the machine-maker?",
             "a": ["Fixed capital, because it is a machine",
                   "Circulating capital, because it will be sold",
                   "Commodity capital, neither fixed nor circulating",
                   "Variable capital, because labour made it"],
             "c": 2,
             "why": "Fixed and circulating divide only productive capital. The machine is the "
                    "maker's product awaiting sale, so it is commodity capital. It becomes "
                    "fixed capital only in its buyer's workshop. Being made by labour does not "
                    "make anything variable capital."},
            {"q": "A £12,000 machine on a 12-year life is booked as if it lasted 8, to cover "
                  "repairs on the average. How much is charged to the product each year for "
                  "repairs?",
             "a": ["£1,000", "£1,500", "£500", "£12,000"],
             "c": 2,
             "why": "Booked at 8 years the charge is £1,500 a year; the true wear is "
                    "`12,000/12 = 1,000`, so £500 is the repair allowance. £1,000 is the wear "
                    "and £1,500 the whole charge; £12,000 is the machine itself."},
        ],
        "mistakes": [
            ("Thinking fixed and circulating are the same distinction as constant and variable",
             "Marx calls this the fundamental mistake. The mill in the next lessons sorts "
             "the same items twice: cotton is circulating and constant, wages circulating and "
             "variable, the machine fixed and constant. Fixed against circulating is about how "
             "value returns; constant against variable is about whether value is created. In "
             "this lesson's ten-year preset the machine transfers £1,000 a year and adds "
             "nothing new."),
            ("Making durability or immobility the test",
             "Seed stays in the ground for a year and is circulating capital; a locomotive "
             "moves all day and is fixed capital. What decides is the manner in which the "
             "value passes to the product: whole each time, or piecemeal while the body stays "
             "in production."),
            ("Counting repairs as part of the original advance",
             "The £10,000 that flows back over ten years replaces only the machine. Repairs "
             "are additional capital, advanced irregularly and charged on the average. In the "
             "repairs preset they are `1,000/3` a year on top of `2,000/3` of wear."),
        ],
        "standard": (
            "Finish when you can compute what a fixed capital transfers and keeps.",
            "Given the value and life of fixed capital, any average repairs and any cheaper "
            "replacement, compute the value transferred each year and the value still locked "
            "in after a stated number of years, and classify an item as fixed or circulating."
        ),
        "note": (
            "The lab spreads wear evenly over the average life, as Marx does, and revalues "
            "the whole machine the moment a cheaper one appears; in practice neither wear nor "
            "devaluation is that tidy, and Marx says the boundary between repair and renewal "
            "shifts. The £10,000 machine and the fifteen years booked as ten are his figures "
            "(the 10 and the 15, he says, are chosen at random); the halving price is "
            "illustrative, and revaluing the old machine at what a new one costs follows "
            "Volume I's account of moral depreciation."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 2, l. 1710 (the passage: Marx's figures); l. 1705 (the mold of
    # money); l. 1712 (£4,000 five times); l. 1714 (£72,000, nine years
    # more); l. 1718 (the material basis of crises; ten years on average);
    # l. 1720-1744 (Scrope).
    {
        "slug": "aggregate-turnover",
        "title": "The Aggregate Turnover of Advanced Capital",
        "module": "Chapter 9 · The Total Turn-Over of Advanced Capital",
        "one_line": "A capital with fixed and circulating parts turns over as fast as its year's wear plus its circulating capital's turnovers, divided by the whole capital advanced.",
        "summary": (
            "The parts of a capital turn over at different speeds, and Marx adds them by "
            "putting them all in money. Compute the value turned over in a year by a capital "
            "with fixed and circulating parts, and the turnovers of the whole capital: on "
            "Marx's figures £108,000 on £100,000 advanced, a little more than one turnover a "
            "year, although the circulating part turns over five times."
        ),
        "key": [
            "turned over = wear + circulating · n",
            "whole turnovers = turned over / advanced",
            "Marx: 8,000 + 5 · 20,000 = 108,000",
            "on 100,000 advanced: 27/25 a year",
            "the cycle is set by the fixed capital",
        ],
        "key_label": "Adding unequal turnovers",
        "concepts_intro": (
            "A machine that lasts ten years and cotton that comes back five times a year "
            "cannot be compared until they are in the same form. The chapter puts them in "
            "money."
        ),
        "concepts": [
            ("Value turned over",
             "Everything that returns to the money form in the year: the year's wear of the "
             "fixed capital plus the circulating capital times its turnovers. It can exceed "
             "the capital advanced."),
            ("Turnovers of the whole capital",
             "The value turned over divided by the capital advanced: an average over parts "
             "that move at different speeds, which can be computed only once every part is "
             "counted in money."),
            ("Cycle of turnovers",
             "The span set by the life of the fixed capital, ten years on Marx's figures, "
             "over which the whole capital-value has to pass before the fixed part is "
             "replaced."),
        ],
        "read_title": "Marx's figures, then the chapter line by line",
        "read_intro": (
            "The chapter numbers its points. The third gives the figures, and the rest of "
            "the chapter returns to them."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 9.</strong> &ldquo;Take it that the fixed "
                  "capital is 80,000 pounds sterling, its period of reproduction 10 years, so "
                  "that 8,000 pounds of this capital annually return to their money-form, or "
                  "complete one-tenth of its turn-over. Let the circulating capital be 20,000 "
                  "pounds sterling, and its period of turn-over be five times per year. The "
                  "total capital would then be 100,000 pounds sterling. &hellip; Then the "
                  "capital turned over during one year is 108,000 pounds sterling, or 8,000 "
                  "pounds more than the advanced capital.&rdquo;"),
            ("p", "Before these figures, Marx has a problem to solve. The circulating capital "
                  "is renewed in its natural form every turnover: new cotton, new labour-power. "
                  "The machine is not; it goes on working for years. Seen as P&hellip;P, "
                  "the two simply do not move alike. Seen as M&hellip;M′, they do, because "
                  "each year £8,000 of the machine's value comes back as money just as the "
                  "cotton's value does. So &ldquo;we, therefore, fix all its elements in the "
                  "mold of money, so that the return to the money-form concludes the "
                  "turn-over&rdquo;. Once everything is money, an average is a sum and a "
                  "division."),
            ("p", "Now the figures. The fixed capital returns £8,000 a year by wear. The "
                  "circulating capital of £20,000 turns over five times, which is £100,000. "
                  "Together, `8,000 + 100,000 = 108,000` is turned over on £100,000 advanced, "
                  "so the whole capital turns over `108,000/100,000 = 27/25` times a year, "
                  "once in about eleven months. The Kerr text prints the result as "
                  "&ldquo;1+2.25&rdquo;, a typesetting slip for one and two twenty-fifths."),
            ("p", "Notice what happened to the speed. The circulating part goes round five "
                  "times, and the whole capital not much more than once, because four-fifths "
                  "of it is in a machine that returns a tenth of its value a year. Point 4 "
                  "then repeats the rule of “Turnover Time and the Number of Turnovers” with "
                  "new numbers: £4,000 turned "
                  "over five times is £20,000 of value, but what returns and is advanced anew "
                  "is the original £4,000, and &ldquo;Its magnitude is not changed by the "
                  "number of its periods of turn-over&rdquo;."),
            ("p", "At the end of Marx's first year the capitalist has back £20,000 for the "
                  "circulating capital and £8,000 set free from the machine, which is still at "
                  "work but now worth £72,000. Nine more years, and the machine is used up and "
                  "replaced. That ten-year span is a cycle of turnovers, and Marx makes a large "
                  "claim for it:"),
            ("p", "<strong>Volume II, Chapter 9.</strong> &ldquo;So much at least is evident "
                  "that this cycle comprising a number of years, through which capital is "
                  "compelled to pass by its fixed part, furnishes a material basis for the "
                  "periodical commercial crises in which business goes through successive "
                  "periods of lassitude, average activity, overspeeding, and crisis.&rdquo;"),
            ("p", "He hedges it in the same paragraph: &ldquo;it is not a question of any one "
                  "definite number here&rdquo;. Moral depreciation shortens the life of fixed "
                  "capital even as engineering lengthens it, and a crisis is the moment a "
                  "great deal of new fixed capital is bought at once, so the next cycle starts "
                  "together. Whether replacement investment actually paces the trade cycle is "
                  "a question for the data. Economists after Marx built cycle theories on "
                  "investment, on credit, on harvests and on money, and this path computes "
                  "none of them."),
            ("p", "Marx ends with a writer who did this arithmetic before him: Scrope, in an "
                  "American edition of his political economy edited by Alonzo Potter. Scrope's "
                  "second case is a capital of $50,000, a quarter of it renewed every ten "
                  "years, a quarter every year and half twice a year, so that `1,250 + 12,500 "
                  "+ 50,000 = 63,750` is turned over. That is Marx's method exactly. Marx's "
                  "quarrel with Scrope is elsewhere: Scrope says wages turn over weekly because "
                  "sales come in weekly, and Marx answers that the terms of payment and credit "
                  "are one thing and the turnover that follows from the nature of capital "
                  "another."),
            ("p", "The lab adds the parts for you. On Marx's figures the tiles read £108,000 on "
                  "£100,000 and `27/25` turnovers. Put nearly all the capital in fixed form, "
                  "£95,000 of it, and the whole turns over about a third of a time a year even "
                  "though the small circulating part still goes round five times. Put most of "
                  "it in circulating form and the whole capital turns over about four times."),
            ("p", "Marx has now said what fixed and circulating capital are and how to add "
                  "them. The next lesson, “The Physiocrats and Adam Smith on Fixed Capital”, "
                  "goes back to where the two terms came from, and to what went wrong when "
                  "they were borrowed."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "aggregate",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: £80,000 fixed on 10 years, £20,000 circulating 5 times",
                 "fixed": [{"name": "fixed capital", "value": 80000, "life_years": 10}],
                 "circulating": 20000, "circ_turnovers": 5, "expect": {"tuAggregate": "£108,000 a year on £100,000 advanced", "tuAverage": "27/25 turnovers a year", "tuWear": "£8,000 a year"}},
                {"id": "heavy-fixed", "label": "Heavy fixed capital: £95,000 fixed, £5,000 circulating",
                 "fixed": [{"name": "fixed capital", "value": 95000, "life_years": 10}],
                 "circulating": 5000, "circ_turnovers": 5, "expect": {"tuAggregate": "£34,500 a year on £100,000 advanced", "tuAverage": "69/200 turnovers a year", "tuWear": "£9,500 a year"}},
                {"id": "light-fixed", "label": "Light fixed capital: £20,000 fixed, £80,000 circulating",
                 "fixed": [{"name": "fixed capital", "value": 20000, "life_years": 10}],
                 "circulating": 80000, "circ_turnovers": 5, "expect": {"tuAggregate": "£402,000 a year on £100,000 advanced", "tuAverage": "201/50 turnovers a year", "tuWear": "£2,000 a year"}},
            ],
            "panel_title": "The turnover of a whole capital",
            "panel_intro": (
                "Fixed capital goes in as items with a value and a life, circulating capital "
                "as one sum with its turnovers a year. The lab adds the year's wear to the "
                "circulating capital turned over and divides by everything advanced. Compare "
                "the second tile with the 5 you typed."
            ),
        }),
        "steps_title": "Totalling the turnover",
        "steps_intro": "Four steps, the same for any capital with fixed and circulating parts.",
        "steps": [
            ("Put the fixed capital in money",
             "For each item, the value that returns to money in a year is its value divided "
             "by its life. Add the items for the year's wear."),
            ("Turn the circulating capital over",
             "Multiply the circulating capital by its turnovers a year for the value it "
             "returns in the year."),
            ("Add, then divide by the capital advanced",
             "The value turned over is the wear plus the circulating capital turned over. "
             "Divide by the whole capital advanced, fixed and circulating, for the turnovers "
             "of the whole capital."),
            ("Read the cycle off the fixed capital",
             "The whole capital-value is replaced only when the longest-lived fixed capital "
             "is. Its life sets the cycle of turnovers, however fast the circulating part "
             "goes round."),
        ],
        "worked": {
            "title": "Marx's £100,000",
            "intro": [
                "Take Marx's figures: £80,000 of fixed capital on a ten-year life, £20,000 of "
                "circulating capital turned over five times a year. You want the value turned "
                "over and the turnovers of the whole capital.",
            ],
            "lines": [
                "wear = £80,000 / 10 = £8,000",
                "circulating turned over = 5 · £20,000 = £100,000",
                "turned over = £8,000 + £100,000 = £108,000",
                "advanced = £80,000 + £20,000 = £100,000",
                "turnovers of the whole = 108,000 / 100,000 = 27/25",
            ],
            "after": [
                "The circulating capital turns over five times and the whole capital `27/25` "
                "times. After the year the machine is worth £72,000, and nine more years will "
                "pass before it has to be replaced.",
            ],
        },
        "quiz_title": "The turnover of a whole capital",
        "quiz": [
            {"q": "A business has £30,000 of fixed capital on a 10-year life and £10,000 of "
                  "circulating capital turned over 4 times a year. What value is turned over in "
                  "the year?",
             "a": ["£40,000", "£43,000", "£160,000", "£70,000"],
             "c": 1,
             "why": "Wear is `30,000/10 = 3,000` and the circulating capital turns over "
                    "`4 · 10,000 = 40,000`, so £43,000. £40,000 leaves out the wear, £160,000 "
                    "turns the whole capital over four times, and £70,000 adds the whole fixed "
                    "capital instead of its wear."},
            {"q": "In the same business, how many times does the whole capital turn over in a "
                  "year?",
             "a": ["4", "43/40", "1/10", "43/10"],
             "c": 1,
             "why": "£43,000 turned over on `30,000 + 10,000 = 40,000` advanced is `43/40`. "
                    "Four is the circulating part alone, `1/10` the fixed part alone, and "
                    "`43/10` divides by the circulating capital only."},
            {"q": "Why does Marx put every part of the capital in money before averaging?",
             "a": ["Because only money produces surplus value",
                   "Because the fixed capital is not renewed in its natural form each turnover, "
                   "but part of its value does return as money each year",
                   "Because the capitalist always pays cash",
                   "Because money turns over faster than commodities"],
             "c": 1,
             "why": "In P…P the machine is not replaced each turnover, so the parts cannot be "
                    "compared; in M…M′ the year's wear returns as money alongside the "
                    "circulating capital. Money produces no surplus value, payment in cash is "
                    "an assumption elsewhere, and money is not said to turn over faster."},
            {"q": "What sets the length of a capital's cycle of turnovers?",
             "a": ["The turnover time of its circulating capital",
                   "The life of its fixed capital",
                   "The length of the working day",
                   "The number of workers employed"],
             "c": 1,
             "why": "The whole capital-value is replaced only when the fixed capital is worn "
                    "out, ten years on Marx's figures. The circulating capital turns over many "
                    "times within that cycle; the working day and the number of workers do not "
                    "enter."},
        ],
        "mistakes": [
            ("Taking the turnover of the circulating part for the turnover of the capital",
             "On Marx's figures the circulating £20,000 turns over five times a year, but the "
             "whole £100,000 turns over `27/25` times, because £80,000 of it returns only a "
             "tenth of its value a year. The heavy-fixed preset makes the gap wider: five "
             "turnovers for the circulating part, about a third of one for the whole."),
            ("Adding the whole fixed capital to the year's turnover",
             "Only the year's wear returns to money in the year. Adding the £80,000 machine "
             "would give £180,000, as if the machine were replaced every year."),
            ("Reading value turned over as capital",
             "The £108,000 turned over is value passing through a £100,000 capital. The "
             "capital advanced is £100,000 throughout the year, and at the end of it £72,000 "
             "is still in the machine."),
        ],
        "standard": (
            "Finish when you can total the turnover of a capital with fixed and circulating parts.",
            "Given the fixed capital's values and lives and the circulating capital's size and "
            "turnovers, compute the value turned over in a year and the turnovers of the whole "
            "capital advanced, and name what sets its cycle of turnovers."
        ),
        "note": (
            "The average here is the capitalist's reckoning, and Marx adopts it for "
            "comparison only: it counts the machine's wear as a turnover although the machine "
            "is not renewed. Marx's claim that the ten-year cycle of fixed capital underlies "
            "the trade cycle is his own hedged suggestion, not something the arithmetic shows. "
            "The heavy-fixed and light-fixed figures are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 2, l. 1800 (the passage: Smith on fixed capital, as Marx
    # quotes him); l. 1764 (Quesnay's avances); l. 1770 (Smith generalises);
    # l. 1786 (Smith's merchant); l. 1788 (capital of circulation); l. 1814
    # (mining); l. 1825 (what fixes capital); l. 1952 and l. 1954 (wages
    # with materials; the labour fund).
    {
        "slug": "physiocrats-and-adam-smith",
        "title": "The Physiocrats and Adam Smith on Fixed Capital",
        "module": "Chapter 10 · Theories of Fixed and Circulating Capital, the Physiocrats and Adam Smith",
        "one_line": "Quesnay drew the line between annual and lasting advances correctly; Smith generalised it, mixed it up with buying and selling, and put wages beside raw materials, where the difference that creates surplus value cannot be seen.",
        "summary": (
            "Chapter 10 traces fixed and circulating capital back to Quesnay's avances and "
            "follows what Adam Smith did with them. Sort the same productive capital as "
            "fixed or circulating and as constant or variable capital, and compute which "
            "sort fixes the surplus value: two capitals split identically into fixed and "
            "circulating can produce different surplus value."
        ),
        "key": [
            "Quesnay: annual and primitive advances",
            "Smith: circulating = changes masters",
            "Marx: fixed = value returns piecemeal",
            "wages and cotton: both circulating",
            "only wages: variable, create value",
        ],
        "key_label": "Where the terms came from",
        "concepts_intro": (
            "The chapter is a history of two words, told as an argument. Three pieces of "
            "vocabulary carry it."
        ),
        "concepts": [
            ("Annual and primitive advances",
             "Quesnay's division of the farmer's capital: the avances annuelles, renewed "
             "every year from the harvest, and the avances primitives, implements and cattle "
             "renewed only over many years. Marx credits him with drawing the line inside "
             "productive capital, where it belongs."),
            ("Capital of circulation",
             "Marx's name for commodity capital and money capital, the forms a capital takes "
             "while it is being sold or spent. They circulate, but they are not "
             "circulating capital as opposed to fixed: that division applies only to "
             "productive capital."),
            ("Two classifications",
             "Fixed against circulating sorts productive capital by how its value returns. "
             "Constant against variable sorts it by whether it creates new value. Wages and "
             "raw materials fall together under the first and apart under the second."),
        ],
        "read_title": "Smith's definition first, then Marx's reading of it",
        "read_intro": (
            "The passage is Adam Smith's, from Book II of The Wealth of Nations, as Marx "
            "quotes it. Most of the chapter is Marx going back over it."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 10.</strong> &ldquo;Secondly, it (capital) may be "
                  "employed in the improvement of land, in the purchase of useful machines and "
                  "instruments of trade, or in such like things as yield a revenue or profit "
                  "without changing masters, or circulating any further. Such capitals, "
                  "therefore, may very properly be called fixed capitals.&rdquo;"),
            ("p", "Begin with the people. François Quesnay was physician to the court of Louis "
                  "XV and the leader of the Physiocrats, who held that only agriculture yields "
                  "a surplus. In his <em>Tableau économique</em> of 1758 he divided the "
                  "farmer's capital into annual advances, seed, wages and the like, which the "
                  "year's harvest must replace in full, and primitive advances, implements and "
                  "cattle, which wear out over ten years or so. Marx thinks this was right. The "
                  "line runs through productive capital, and it is drawn by how each part "
                  "enters the value of the product."),
            ("p", "Adam Smith, the Scottish moral philosopher, took the distinction over in "
                  "1776 and made it general, for every capital and not only the farmer's. "
                  "&ldquo;Thus Adam Smith transforms the annual advances into circulating "
                  "capital, and the primitive advances into fixed capital. But his progress is "
                  "confined to this generalization of the categories. His analyses are far "
                  "inferior to those of Quesnay.&rdquo;"),
            ("p", "Read Smith's definition phrase by phrase and the trouble shows. Fixed capital "
                  "yields a profit &ldquo;without changing masters&rdquo;. Circulating capital, "
                  "then, is capital that does change masters, and Smith's example of it is the "
                  "merchant, whose capital &ldquo;is continually going from him in one shape, "
                  "and returning to him in another&rdquo;. That, Marx says, is not circulating "
                  "capital but capital of circulation: goods being sold and money being spent, "
                  "the forms every capital passes through on its way round, machine-value "
                  "included."),
            ("p", "Two tests show the confusion. A machine in its maker's warehouse changes "
                  "masters when it is sold, so by Smith's words it is circulating capital, "
                  "though it is the very type of a fixed one. And a copper mine uses no raw "
                  "material at all, only labour, coal and machinery, none of which ever "
                  "changes masters, so &ldquo;According to Adam Smith's own definition, the "
                  "entire capital employed in mining would consist only of fixed "
                  "capital.&rdquo;"),
            ("p", "Marx's own criterion is the one from Chapter 8, and he states it against "
                  "Smith's:"),
            ("p", "<strong>Volume II, Chapter 10.</strong> &ldquo;Hence capital is not fixed "
                  "capital, because it is fixed in the means of production, but because a part "
                  "of the value invested in means of production remains fixed in them, while "
                  "another part circulates as a part of the value of the product.&rdquo;"),
            ("p", "The damage Marx cares most about comes next. Smith lists wages with "
                  "materials as circulating capital, and lists them as the workers' "
                  "&ldquo;maintenance&rdquo;, their food and clothing, as if wages were fodder. "
                  "Sorted that way, the capital laid out on labour-power sits beside the "
                  "cotton, and its one peculiarity, that it buys something which creates more "
                  "value than it costs, disappears from view. Marx says the circulating "
                  "character of wages &ldquo;has nothing whatever to do with the role played "
                  "by this variable part of capital in the process of self-expansion&rdquo;."),
            ("p", "He follows the mistake one step further. If wages are a stock of provisions, "
                  "there is a fixed fund of them to divide among the workers, and from this "
                  "came &ldquo;the doctrine of a labor fund of definite magnitude&rdquo;, the "
                  "wage-fund doctrine that John Stuart Mill taught for twenty years and gave up "
                  "in 1869. Smith's case deserves its strength, though. For the manager "
                  "reading the books, wages and cotton really do come back together, with each "
                  "sale, and the machine really does not. Marx grants all of that. His "
                  "complaint is that a classification good for timing returns was then used to "
                  "explain profit."),
            ("p", "The lab sorts one capital both ways. In a mill with a £500 machine, £100 of "
                  "cotton and £100 of wages, Smith's split is £500 fixed and £200 circulating; "
                  "Marx's is £600 constant and £100 variable, and at 100% only the £100 of "
                  "wages yields surplus value. Then compare Smith's farmer with a copper mine, "
                  "both sorted by how their value returns, which is Marx's test and not "
                  "Smith's. Smith himself called the seed fixed, because it &ldquo;never "
                  "changes masters&rdquo;, and on his test the whole mine would be fixed; "
                  "Marx puts the seed, the coal and the wages on the circulating side. So "
                  "sorted, both split £600 fixed and £400 circulating. The farm's circulating "
                  "capital is £200 of fodder and seed and £200 of wages; the mine's is £150 of "
                  "coal and £250 of wages. Same fixed and circulating, different variable "
                  "capital, different surplus value: £200 against £250."),
            ("p", "Smith set the terms, and his successors kept them. The next lesson, “Ricardo "
                  "on Fixed and Circulating Capital”, follows them into the most careful "
                  "economist of the next generation."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "classify",
            "money_unit": "£",
            "preset": "mill",
            "presets": [
                {"id": "mill", "label": "A mill: £500 machine, £100 cotton, £100 wages, at 100%",
                 "items": [{"name": "machine", "value": 500, "fixed": True, "variable": False},
                           {"name": "cotton", "value": 100, "fixed": False, "variable": False},
                           {"name": "wages", "value": 100, "fixed": False, "variable": True}],
                 "s_rate": 1, "expect": {"tuFixed": "fixed £500, circulating £200", "tuVariable": "constant £600, variable £100", "tuS": "£100"}},
                {"id": "farm", "label": "Smith's farmer, sorted by Marx's test: implements and cattle fixed, fodder, seed and wages circulating",
                 "items": [{"name": "implements", "value": 400, "fixed": True, "variable": False},
                           {"name": "labouring cattle", "value": 200, "fixed": True, "variable": False},
                           {"name": "fodder", "value": 100, "fixed": False, "variable": False},
                           {"name": "seed", "value": 100, "fixed": False, "variable": False},
                           {"name": "wages", "value": 200, "fixed": False, "variable": True}],
                 "s_rate": 1, "expect": {"tuFixed": "fixed £600, circulating £400", "tuVariable": "constant £800, variable £200", "tuS": "£200"}},
                {"id": "mine", "label": "Marx's copper mine: no raw material, only coal, wages and machinery",
                 "items": [{"name": "machinery", "value": 600, "fixed": True, "variable": False},
                           {"name": "coal", "value": 150, "fixed": False, "variable": False},
                           {"name": "wages", "value": 250, "fixed": False, "variable": True}],
                 "s_rate": 1, "expect": {"tuFixed": "fixed £600, circulating £400", "tuVariable": "constant £750, variable £250", "tuS": "£250"}},
            ],
            "panel_title": "One capital, sorted twice",
            "panel_intro": (
                "Each item goes in with its value and two answers: is it fixed, and is it "
                "variable? The lab totals the capital both ways and computes surplus value at "
                "the rate of surplus value on the variable items only. Compare the farm and "
                "the mine: the first tile is the same, the third is not."
            ),
        }),
        "steps_title": "Sorting a capital twice",
        "steps_intro": "Four steps for any list of the items of a productive capital.",
        "steps": [
            ("Ask how each item's value returns",
             "If its value passes into the product piecemeal while it stays in production, "
             "it is fixed. If its whole value passes into each product, it is circulating."),
            ("Ask whether each item creates value",
             "Only the capital paid for labour-power is variable. Materials, coal and "
             "machines transfer their value and are constant, fixed or not."),
            ("Total each classification",
             "Add the fixed and the circulating items, then the constant and the variable. "
             "Every item appears once in each pair of totals."),
            ("Compute surplus value from the variable total",
             "Multiply the variable capital by the rate of surplus value. The fixed and "
             "circulating totals play no part in this step."),
        ],
        "worked": {
            "title": "Cotton and wages, both circulating",
            "intro": [
                "A mill has a £500 machine, £100 of cotton and £100 of wages, and the rate of "
                "surplus value is 100%. You want both classifications and the surplus value.",
            ],
            "lines": [
                "fixed: machine £500",
                "circulating: cotton £100 + wages £100 = £200",
                "constant: £500 + £100 = £600",
                "variable: wages £100",
                "s = 100% · £100 = £100",
            ],
            "after": [
                "Cotton and wages are both circulating, and only the wages create new value. "
                "Move £100 from cotton to wages and the circulating total is still £200, but "
                "the surplus value doubles.",
            ],
        },
        "quiz_title": "Smith's categories and Marx's",
        "quiz": [
            {"q": "A workshop has £300 of tools, £200 of materials and £100 of wages, at a "
                  "rate of surplus value of 100%. What is its circulating capital?",
             "a": ["£100", "£300", "£500", "£600"],
             "c": 1,
             "why": "Materials and wages are both circulating: `200 + 100 = 300`. £100 is the "
                    "variable capital only, £500 is the constant capital, and £600 is the "
                    "whole capital."},
            {"q": "In the same workshop, what surplus value is produced?",
             "a": ["£300", "£100", "£600", "£200"],
             "c": 1,
             "why": "Surplus value is the rate times the variable capital, `100% · 100 = 100`. "
                    "Applying the rate to the circulating capital gives £300, to the whole "
                    "capital £600, and to the materials £200; none of those buys labour-power."},
            {"q": "By Smith's own definition, how would the capital of a copper mine be "
                  "classed, according to Marx?",
             "a": ["Entirely as circulating capital",
                   "Entirely as fixed capital",
                   "Half fixed and half circulating",
                   "As commodity capital"],
             "c": 1,
             "why": "A mine uses no raw material that changes masters; its labour, coal and "
                    "machinery all stay with the owner, so on Smith's test everything is fixed. "
                    "Marx uses the case to show the test is wrong: the coal and wages are "
                    "circulating by how their value returns. Commodity capital is the copper "
                    "once mined."},
            {"q": "What does Marx credit Quesnay with that Smith lost?",
             "a": ["Discovering surplus value in industry",
                   "Drawing the line between annual and lasting advances inside productive capital",
                   "Treating labour-power as variable capital",
                   "Measuring turnover in weeks"],
             "c": 1,
             "why": "Quesnay's avances are both elements of productive capital, sorted by how "
                    "they enter the product's value. He found surplus value only in agriculture, "
                    "as a gift of nature, did not distinguish variable capital, and reckoned "
                    "in years."},
        ],
        "mistakes": [
            ("Thinking wages and raw materials are the same kind of capital because both circulate",
             "They return their value the same way, and that is all they share. In the mill "
             "preset £100 of cotton and £100 of wages are both circulating, and at 100% only "
             "the wages yield surplus value, £100. The farm and mine presets split identically "
             "into £600 fixed and £400 circulating and produce £200 and £250."),
            ("Defining circulating capital as capital that changes hands",
             "That is Smith's test, and it describes commodity and money capital, the forms in "
             "which every capital is sold and spent. It makes a machine in its maker's "
             "warehouse circulating and a whole mine fixed."),
            ("Counting the workers' provisions as the capital",
             "The capitalist buys labour-power, not the bread the worker later buys with the "
             "wage. Counting the bread puts wages beside fodder and hides the one difference "
             "that creates surplus value."),
        ],
        "standard": (
            "Finish when you can sort a capital both ways and say which sort fixes surplus value.",
            "Given the items of a productive capital, classify each as fixed or circulating "
            "and as constant or variable, total both classifications, and compute the surplus "
            "value from the variable capital at a stated rate."
        ),
        "note": (
            "The lab takes the rate of surplus value as given and applies it to the variable "
            "items; that is Marx's definition, and it is exactly what an economist who "
            "explains profit by the productivity of all capital would reject. The mill, farm "
            "and mine are illustrative capitals built on Smith's and Marx's examples; the "
            "chapter gives no figures for them."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 2, l. 1962 (the passage: Ricardo's purpose); l. 1966 (the
    # capital that supports labour); l. 1968 and l. 1970 (two differences;
    # both count in equalising profit); l. 1975 (raw material disappears);
    # l. 2023 and l. 2025 (Ricardo's definition); l. 2054 (the farmer's and
    # the baker's wheat); l. 2056 (the manner of transfer).
    {
        "slug": "ricardo-on-fixed-and-circulating-capital",
        "title": "Ricardo on Fixed and Circulating Capital",
        "module": "Chapter 11 · Theories of Fixed and Circulating Capital. Ricardo",
        "one_line": "Ricardo used durability to explain why prices depart from labour values, and in doing so took the fixed and circulating split for the split between machines and labour, which it is not.",
        "summary": (
            "Ricardo divided capital into what lasts and what perishes, and set that beside "
            "the capital that supports labour. Compute two capitals with the same fixed share "
            "and different wage bills, and two with different fixed shares and the same wage "
            "bill, and the surplus value each produces at the same rate: the fixed share "
            "cannot tell the first pair apart, and separates the second pair for nothing."
        ),
        "key": [
            "Ricardo: fixed = durable, slow to perish",
            "his circulating capital supports labour",
            "raw material drops out of both",
            "same fixed share, different s possible",
            "s follows the variable capital only",
        ],
        "key_label": "Durability against variable capital",
        "concepts_intro": (
            "Ricardo cared about fixed and circulating capital for one reason, and Marx's "
            "chapter is about what that reason did to the categories."
        ),
        "concepts": [
            ("Ricardo's exception",
             "In Ricardo's theory relative prices follow relative labour, except where "
             "capitals differ in durability or in their mix of fixed and circulating capital; "
             "then a change in wages moves prices. He drew the distinction only to explain "
             "that exception."),
            ("Two differences run together",
             "The durability of fixed capital governs how fast its value returns. The "
             "proportion of constant to variable capital governs how much surplus value is "
             "produced. Ricardo treats the two as one."),
            ("The vanishing raw material",
             "If circulating capital is the capital that supports labour, raw materials "
             "belong nowhere: they are not durable instruments, and they do not support "
             "labour. Marx notes that they simply disappear from Ricardo's scheme."),
        ],
        "read_title": "Ricardo's purpose, then his definition, then Marx's reply",
        "read_intro": (
            "The chapter opens by saying why Ricardo needed the distinction at all. His own "
            "definition comes later, in his own words."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 11.</strong> &ldquo;Ricardo mentions the "
                  "distinction between fixed and circulating capital merely for the purpose of "
                  "illustrating the exceptions to the law of value, namely, in cases where the "
                  "rate of wages affects the prices. The discussion of this point is reserved "
                  "for volume III.&rdquo;"),
            ("p", "David Ricardo was a stockbroker who made a fortune in government loans, "
                  "retired to the country, and wrote the most rigorous economics of his day, "
                  "<em>On the Principles of Political Economy and Taxation</em>, in 1817. His "
                  "first chapter argues that commodities exchange in proportion to the labour "
                  "they contain, and then lists the exceptions. Two goods made with "
                  "the same labour can have different prices if one is made with long-lasting "
                  "machines and the other mostly with wages, because when wages rise the second "
                  "costs more to produce and the first hardly changes. Fixed and circulating "
                  "capital enter his book to explain that."),
            ("p", "Ricardo's two sorts of capital are &ldquo;the capital that is to support "
                  "labor, and the capital that is invested in tools, machinery, and "
                  "buildings&rdquo;. Marx's first objection is that this puts two different "
                  "differences side by side as if they were one. Durability decides how fast "
                  "a machine returns its value. The proportion of constant to variable capital "
                  "decides something else entirely: &ldquo;the last-named difference "
                  "determines the difference in the production of surplus-value&rdquo;."),
            ("p", "His second objection is where the cotton went. Raw material is not a durable "
                  "instrument, so it cannot be fixed capital; and if circulating capital means "
                  "the capital that supports labour, it cannot be circulating either. Marx's "
                  "comment is dry: &ldquo;Ricardo has too much logical instinct not to feel "
                  "this, and for this reason that part of capital disappears entirely for "
                  "him.&rdquo;"),
            ("p", "Then Ricardo's own definition, as Marx quotes it:"),
            ("p", "<strong>Volume II, Chapter 11.</strong> &ldquo;According as capital is "
                  "rapidly perishable and requires to be frequently reproduced or is of slow "
                  "consumption, it is classed under the heads of circulating or fixed "
                  "capital.&rdquo;"),
            ("p", "Ricardo himself calls this &ldquo;A division not essential, and in which the "
                  "line of demarcation cannot be accurately drawn.&rdquo; Marx agrees, for "
                  "Ricardo's version. On Ricardo's test a steam engine, a ship, the worker's "
                  "clothes and the worker's food lie on one scale of durability, and the "
                  "difference between buying a machine and buying labour-power becomes a "
                  "difference of degree. Marx's test is the manner in which value passes to "
                  "the product, a test of the part a thing plays in production and not of how "
                  "long it lasts."),
            ("p", "Ricardo's example makes the point for Marx. &ldquo;The wheat bought by a "
                  "farmer to sow is comparatively a fixed capital to the wheat purchased by a "
                  "baker to make into loaves.&rdquo; The farmer waits a year for his return, "
                  "the baker a week. But the seed passes its whole value into the harvest, "
                  "exactly as the baker's wheat passes its whole value into the bread. Both "
                  "are circulating capital. Speed of return is a matter of turnover time, "
                  "which the next lessons measure directly."),
            ("p", "Ricardo's position has a strong modern form, and it is worth stating. In a "
                  "theory of prices, how long capital is tied up and how it is split really "
                  "do decide how prices respond to wages; Piero Sraffa's edition of Ricardo "
                  "and his own 1960 book rebuilt exactly that argument. Marx does not deny it. "
                  "He says that in the formation of prices of production durability and "
                  "composition &ldquo;contribute equally toward an equalization of the general "
                  "rate of profit&rdquo;, and leaves that for Volume III. His claim is "
                  "narrower: for the production of surplus value, only the variable capital "
                  "counts."),
            ("p", "The lab sets two capitals side by side. Both are £1,000 and both a quarter "
                  "fixed. A spends £500 on materials and £250 on wages; B spends £250 on "
                  "materials and £500 on wages. The fixed and circulating tile is identical, "
                  "and at 100% A produces £250 of surplus value and B £500. Reverse the test: "
                  "a capital that is mostly machine and one that is mostly material, with the "
                  "same £250 of wages, split very differently and produce the same £250. "
                  "Ricardo's farmer and baker, finally, each with £500 fixed, £400 of wheat and £100 of "
                  "wages, come out the same on both tiles: £500 circulating each, and £100 of surplus "
                  "value each, though one waits a year for his wheat and the other a week."),
            ("p", "The two chapters on the economists end here. The next lesson, “The Working "
                  "Period”, returns to time, and asks what a product that takes three months "
                  "to make does to the capital a business must have."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "classify",
            "money_unit": "£",
            "preset": "same-fixed",
            "presets": [
                {"id": "same-fixed", "label": "Two £1,000 capitals, both a quarter fixed, wages £250 and £500",
                 "items": [{"name": "A machine", "value": 250, "fixed": True, "variable": False, "capital": "A"},
                           {"name": "A materials", "value": 500, "fixed": False, "variable": False, "capital": "A"},
                           {"name": "A wages", "value": 250, "fixed": False, "variable": True, "capital": "A"},
                           {"name": "B machine", "value": 250, "fixed": True, "variable": False, "capital": "B"},
                           {"name": "B materials", "value": 250, "fixed": False, "variable": False, "capital": "B"},
                           {"name": "B wages", "value": 500, "fixed": False, "variable": True, "capital": "B"}],
                 "s_rate": 1, "expect": {"tuFixed": "A: fixed £250, circulating £750; B: fixed £250, circulating £750", "tuVariable": "A: constant £750, variable £250; B: constant £500, variable £500", "tuS": "A £250, B £500"}},
                {"id": "different-fixed", "label": "Mostly machine against mostly material, the same £250 of wages",
                 "items": [{"name": "A machine", "value": 600, "fixed": True, "variable": False, "capital": "A"},
                           {"name": "A materials", "value": 150, "fixed": False, "variable": False, "capital": "A"},
                           {"name": "A wages", "value": 250, "fixed": False, "variable": True, "capital": "A"},
                           {"name": "B machine", "value": 100, "fixed": True, "variable": False, "capital": "B"},
                           {"name": "B materials", "value": 650, "fixed": False, "variable": False, "capital": "B"},
                           {"name": "B wages", "value": 250, "fixed": False, "variable": True, "capital": "B"}],
                 "s_rate": 1, "expect": {"tuFixed": "A: fixed £600, circulating £400; B: fixed £100, circulating £900", "tuVariable": "A: constant £750, variable £250; B: constant £750, variable £250", "tuS": "A £250, B £250"}},
                {"id": "farmer-and-baker", "label": "Ricardo's farmer and baker: seed wheat and bread wheat",
                 "items": [{"name": "implements", "value": 500, "fixed": True, "variable": False, "capital": "farmer"},
                           {"name": "seed wheat", "value": 400, "fixed": False, "variable": False, "capital": "farmer"},
                           {"name": "farm wages", "value": 100, "fixed": False, "variable": True, "capital": "farmer"},
                           {"name": "oven", "value": 500, "fixed": True, "variable": False, "capital": "baker"},
                           {"name": "flour wheat", "value": 400, "fixed": False, "variable": False, "capital": "baker"},
                           {"name": "bakery wages", "value": 100, "fixed": False, "variable": True, "capital": "baker"}],
                 "s_rate": 1, "expect": {"tuFixed": "farmer: fixed £500, circulating £500; baker: fixed £500, circulating £500", "tuVariable": "farmer: constant £900, variable £100; baker: constant £900, variable £100", "tuS": "farmer £100, baker £100"}},
            ],
            "panel_title": "Two capitals, sorted twice",
            "panel_intro": (
                "Each item names the capital it belongs to. The lab sorts both capitals by "
                "fixed and circulating and by constant and variable, and computes surplus value "
                "at the stated rate on the variable items. In each preset, ask which tile "
                "tells the two capitals apart."
            ),
        }),
        "steps_title": "Testing what the fixed share can tell you",
        "steps_intro": "Four steps for comparing two capitals.",
        "steps": [
            ("Sort both capitals by how value returns",
             "Total each capital's fixed and circulating items. This is Ricardo's split, with "
             "raw material put back where its turnover places it."),
            ("Sort both by whether value is created",
             "Total each capital's constant and variable items. Wages alone are variable."),
            ("Compute each surplus value",
             "Multiply each variable capital by the common rate of surplus value."),
            ("Compare the tiles",
             "If the fixed and circulating totals agree and the surplus values differ, or the "
             "other way round, the fixed share does not explain the surplus value."),
        ],
        "worked": {
            "title": "The same fixed share, twice the surplus value",
            "intro": [
                "Capitals A and B are £1,000 each with a £250 machine. A spends £500 on "
                "materials and £250 on wages; B £250 on materials and £500 on wages. The rate "
                "of surplus value is 100%.",
            ],
            "lines": [
                "A: fixed £250, circulating £750",
                "B: fixed £250, circulating £750",
                "A: constant £750, variable £250, s = £250",
                "B: constant £500, variable £500, s = £500",
            ],
            "after": [
                "Ricardo's split cannot tell A from B. The split between constant and variable "
                "capital can, and it is the one that predicts the surplus value.",
            ],
        },
        "quiz_title": "Durability and surplus value",
        "quiz": [
            {"q": "Two £2,000 capitals each have £500 of fixed capital. C pays £300 in wages and "
                  "D £900. At a rate of surplus value of 100%, what surplus value does D produce?",
             "a": ["£300", "£900", "£1,500", "£500"],
             "c": 1,
             "why": "Surplus value is the rate times the variable capital, `100% · 900 = 900`. "
                    "£300 is C's, £1,500 is D's circulating capital, and £500 its fixed capital; "
                    "neither of those last two produces surplus value."},
            {"q": "Why does raw material disappear from Ricardo's two sorts of capital, on "
                  "Marx's account?",
             "a": ["Ricardo thought raw material had no value",
                   "It is neither a durable instrument nor capital that supports labour",
                   "Ricardo counted it as fixed capital",
                   "Raw material is commodity capital, not productive capital"],
             "c": 1,
             "why": "Ricardo's circulating capital is the capital that supports labour, and his "
                    "fixed capital is tools, machinery and buildings. Raw material fits neither. "
                    "He did not deny it value or call it fixed, and in production it is "
                    "productive capital."},
            {"q": "Ricardo calls a farmer's seed wheat comparatively fixed beside a baker's "
                  "wheat. What is it on Marx's definitions?",
             "a": ["Fixed capital, because it returns slowly",
                   "Circulating capital, because its whole value passes into the harvest",
                   "Variable capital, because it grows",
                   "Neither, because seed is not bought"],
             "c": 1,
             "why": "What decides is the manner in which value passes to the product, and the "
                    "seed passes all of it into one harvest. Slowness is turnover time, not "
                    "fixity; growth is a natural process, not labour-power; and seed taken from "
                    "the farmer's own crop is still part of his productive capital."},
            {"q": "Where does Marx agree that durability and composition both matter?",
             "a": ["In the production of surplus value",
                   "In the equalisation of the rate of profit and prices of production",
                   "In the value of labour-power",
                   "Nowhere; he rejects Ricardo entirely"],
             "c": 1,
             "why": "He says both contribute equally toward equalising the general rate of "
                    "profit, and leaves that to Volume III. For the production of surplus value "
                    "only the variable capital counts, and durability has nothing to do with "
                    "the value of labour-power."},
        ],
        "mistakes": [
            ("Thinking the fixed and circulating split explains where profit comes from",
             "In the same-fixed preset both capitals are £250 fixed and £750 circulating, and "
             "they produce £250 and £500 of surplus value. In the different-fixed preset they "
             "split £600 and £100 fixed and produce the same £250. The variable capital "
             "predicts the surplus value every time; the fixed share never does."),
            ("Taking speed of return for fixity",
             "Ricardo's farmer waits a year and his baker a week, but seed and flour both pass "
             "their whole value into one product. They are circulating capital with different "
             "turnover times, and the farmer-and-baker preset classes them identically."),
            ("Concluding that durability does not matter at all",
             "Marx says the opposite for prices: in Volume III durability and composition "
             "both enter the equalisation of profit. His claim is only that the production of "
             "surplus value depends on the variable capital."),
        ],
        "standard": (
            "Finish when you can show that the fixed share does not fix the surplus value.",
            "Given two capitals' items, compute each one's fixed and circulating totals, "
            "constant and variable totals and surplus value at a stated rate, and state which "
            "classification predicts the surplus value."
        ),
        "note": (
            "The lab computes surplus value at a rate it is given, so it cannot weigh "
            "Ricardo's actual question, how prices respond to a rise in wages; that needs "
            "prices of production and comes in Average Profit and Its Fall. The capitals are "
            "illustrative; Ricardo's farmer and baker are his, the figures are not."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 2, l. 2090 (the passage: 100 working days, the working
    # period); l. 2076 (spinnery and locomotive); l. 2078-2080 (durations);
    # l. 2082 (twelve times more circulating capital); l. 2092-2094
    # (interruption); l. 2116-2118 (the London builder); l. 2124 (railway
    # armies); l. 2142 (Bakewell).
    {
        "slug": "the-working-period",
        "title": "The Working Period",
        "module": "Chapter 12 · The Working Period",
        "one_line": "A product that takes many connected working days to finish ties up a week's outlay for every week of its making, so a long working period needs more capital, not only more patience.",
        "summary": (
            "Some products are finished every day; a locomotive needs three months of "
            "connected work before it can be sold. Compute the circulating capital a long "
            "working period ties up before anything can be sold, from the weekly outlay and "
            "the weeks, and compare a cotton mill's week with a locomotive's twelve and an "
            "ironclad's year."
        ),
        "key": [
            "working period: days joined into one act",
            "tied up = weekly outlay · weeks",
            "fixed capital: no new outlay",
            "circulating: added every week",
            "one week × 12 = twelve times the capital",
        ],
        "key_label": "The working period in five lines",
        "concepts_intro": (
            "The working day of Volume I is the same in a spinning mill and a locomotive "
            "works. The chapter is about a length that is not."
        ),
        "concepts": [
            ("Working period",
             "The number of connected working days a branch needs to finish its product. A "
             "spinner's product is done each day or week; a locomotive's takes about three "
             "months; timber can take a century."),
            ("Capital tied up",
             "Every week of a working period needs new wages and materials, and none of them "
             "returns until the product is finished and sold. The circulating capital needed "
             "grows with the length of the period."),
            ("Shortening it",
             "Machines, co-operation on a large scale and the concentration of capital can "
             "shorten a working period, usually by advancing more capital for a shorter "
             "time. Where nature sets the period, as for cattle, they can do little."),
        ],
        "read_title": "A working day of a thousand hours, then the chapter line by line",
        "read_intro": (
            "The chapter opens with a cotton mill and a locomotive works. The passage gives "
            "the name Marx coins for what separates them."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 12.</strong> &ldquo;Take it that the manufacture "
                  "of a locomotive, or of any other machine, requires 100 working days. &hellip; "
                  "But with reference to the product&mdash;the machine&mdash;these 100 working "
                  "days are a continuous magnitude, a working day of 1,000 working hours, one "
                  "single connected act of production. I call such a working day, which is "
                  "formed by the succession of more or less numerous connected working days, a "
                  "working period.&rdquo;"),
            ("p", "Take Marx's two branches, a cotton spinnery and a locomotive factory, with "
                  "equal ten-hour days. The spinner's yarn is finished every day and can be "
                  "sold every week. The locomotive is not finished until three months of days "
                  "have been joined together. For the workers each day is a separate day; for "
                  "the product they are one long act. Marx notes that the difference has "
                  "nothing to do with fixed and circulating capital: it would be there if both "
                  "factories had exactly the same proportions of each."),
            ("p", "The variety is enormous, and Marx lists it: a house in less time "
                  "than a factory, a locomotive in three months and an ironclad in a year or "
                  "more, grain in nearly a year, cattle in several, timber in twelve to a "
                  "hundred years, an ordinary carpet in a week and a Gobelins tapestry in "
                  "years."),
            ("p", "Now the arithmetic. Let the two factories lay out the same sum every week "
                  "and be paid on delivery. At the end of the week the spinner sells and starts "
                  "again with the same money. The locomotive builder must find new wages and "
                  "materials every week for twelve weeks before anything comes back:"),
            ("p", "<strong>Volume II, Chapter 12.</strong> &ldquo;The investment of the one is "
                  "made for one week, that of the other is the investment of one week "
                  "multiplied by twelve. All other circumstances being assumed as equal, the "
                  "one must have twelve times more circulating capital at his disposal than "
                  "the other.&rdquo;"),
            ("p", "Fixed capital behaves differently, and that is where its difference from "
                  "circulating capital first does practical work. The steam engine passes its "
                  "wear to the yarn weekly or to the locomotive quarterly, but it is the same "
                  "engine either way and need not be replaced for twenty years. Circulating "
                  "capital is the problem: the labour-power bought this week is used up this "
                  "week, must be paid this week, and sits in an unfinished product that cannot "
                  "circulate. A crisis that halts a ship or a house half-built wastes all of "
                  "it."),
            ("p", "This is why long working periods came late to capitalist hands. Roads and "
                  "canals were built by states and towns, often with forced labour; houses were "
                  "paid for in instalments by the people who ordered them. In 1857 a "
                  "London contractor told the parliamentary committee on the Bank Acts that he now bought land, "
                  "built 100 to 200 houses on speculation, and so took on &ldquo;an enterprise "
                  "which exceeds from twenty to fifty times his resources&rdquo;, the rest "
                  "borrowed on mortgage. If a crisis stopped the instalments, the whole thing "
                  "collapsed. Much of Belgravia was built that way."),
            ("p", "What shortens a working period? Machinery, co-operation and the concentration "
                  "of capital, almost always by advancing more capital for a shorter time: a "
                  "railway is finished sooner by &ldquo;the employment of huge armies of "
                  "laborers and the carrying on of the work in many places at once&rdquo;. "
                  "Where nature sets the period it is harder. Robert Bakewell, a farmer at "
                  "Dishley Grange, bred his New Leicester sheep to be ready in two years "
                  "instead of four or five; Marx reports that he &ldquo;reduced the skeleton of "
                  "sheep to the minimum required for their existence&rdquo;, and his source "
                  "admired the result."),
            ("p", "The lab computes the capital tied up before the first sale, at £100 a week. "
                  "The spinner's week ties up £100. The locomotive's twelve weeks tie up "
                  "£1,200, twelve times as much on the same weekly outlay. An ironclad's year "
                  "of 52 weeks ties up £5,200. The weekly outlay, the working day and the rate "
                  "of exploitation are the same in all three; only the length of the "
                  "connected act differs."),
            ("p", "A working period is all work. The next lesson, “The Time of Production”, "
                  "turns to products that spend part of their making with no work done on them "
                  "at all, while the capital waits."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "working",
            "money_unit": "£",
            "preset": "cotton",
            "presets": [
                {"id": "cotton", "label": "Cotton yarn: a working period of one week at £100",
                 "working_weeks": 1, "weekly_outlay": 100, "expect": {"tuAdvance": "£100"}},
                {"id": "locomotive", "label": "Marx's locomotive: three months, 12 weeks at £100",
                 "working_weeks": 12, "weekly_outlay": 100, "expect": {"tuAdvance": "£1,200"}},
                {"id": "ironclad", "label": "Marx's ironclad: a year or more, 52 weeks at £100",
                 "working_weeks": 52, "weekly_outlay": 100, "expect": {"tuAdvance": "£5,200"}},
            ],
            "panel_title": "What a long product ties up",
            "panel_intro": (
                "The working period in weeks and the outlay a week go in. The lab multiplies "
                "them for the circulating capital tied up before the product can be sold. The "
                "weekly outlay is the same in every preset; watch what the weeks do."
            ),
        }),
        "steps_title": "Computing the capital a working period ties up",
        "steps_intro": "Four steps for any product made over connected working days.",
        "steps": [
            ("Find the working period",
             "Count the connected working weeks the product needs before it is a finished "
             "commodity: a week for yarn, about twelve for a locomotive."),
            ("Find the weekly outlay",
             "Take the circulating capital laid out each week, wages and materials. Leave "
             "the fixed capital out: it needs no new outlay during the period."),
            ("Multiply",
             "The capital tied up before the first sale is the weekly outlay times the weeks "
             "of the working period."),
            ("Compare at the same weekly outlay",
             "Two branches with the same weekly outlay need circulating capital in "
             "proportion to their working periods, whatever else they share."),
        ],
        "worked": {
            "title": "A locomotive at £100 a week",
            "intro": [
                "A spinnery and a locomotive works each lay out £100 a week in wages and "
                "materials. Yarn is finished weekly; a locomotive takes twelve weeks. You want "
                "the circulating capital each must have before its first sale.",
            ],
            "lines": [
                "spinnery: £100 · 1 week = £100",
                "locomotive: £100 · 12 weeks = £1,200",
                "ratio: 1,200 / 100 = 12",
            ],
            "after": [
                "Twelve times the circulating capital, as Marx says, on the same weekly outlay, "
                "the same working day and the same rate of surplus value.",
            ],
        },
        "quiz_title": "The working period",
        "quiz": [
            {"q": "A ship takes 40 weeks to build at a weekly outlay of £250 in wages and "
                  "materials. How much circulating capital is tied up before it can be "
                  "delivered?",
             "a": ["£250", "£10,000", "£6,250", "£40"],
             "c": 1,
             "why": "`250 · 40 = 10,000`. £250 is one week's outlay; £6,250 multiplies by 25 "
                    "weeks instead of 40; and £40 is the weeks with a pound sign."},
            {"q": "What happens to the fixed capital during a long working period, on Marx's "
                  "account?",
             "a": ["It must be advanced again every week",
                   "It keeps working and passes on wear, without any new outlay until it is worn out",
                   "It becomes circulating capital",
                   "It stops passing on any value until the product is sold"],
             "c": 1,
             "why": "The steam engine works on whether its wear goes into yarn weekly or into a "
                    "locomotive quarterly, and is replaced only after its life. It needs no new "
                    "outlay, does not change category, and passes wear into the unfinished "
                    "product all along; what is delayed is only the return of that wear as money."},
            {"q": "Which of these is a working period in Marx's sense?",
             "a": ["The ten hours of a spinner's day",
                   "The nine months winter grain takes to ripen",
                   "The connected working days needed to finish a locomotive",
                   "The weeks a finished locomotive waits for a buyer"],
             "c": 2,
             "why": "A working period is the succession of connected working days a product "
                    "needs. The spinner's day is a working day; the grain's ripening is "
                    "production time with little work in it, the next lesson's subject; and "
                    "waiting for a buyer is circulation time."},
        ],
        "mistakes": [
            ("Thinking a long working period is only a question of patience",
             "It is a question of capital. In the locomotive preset twelve weeks at £100 tie "
             "up £1,200 before anything is sold, against £100 for the spinner: twelve times "
             "the circulating capital for the same weekly business."),
            ("Adding the fixed capital to the weekly outlay",
             "The engine is bought once and works through every working period of its life. "
             "Only wages and materials have to be found anew each week, which is why the "
             "lab's outlay is circulating capital only."),
            ("Confusing the working period with the working day",
             "The working day is the same ten hours in both factories. The working period is "
             "how many of those days are joined into one product, and it is what differs."),
        ],
        "standard": (
            "Finish when you can compute the capital a working period ties up.",
            "Given a weekly outlay of circulating capital and a working period in weeks, "
            "compute the capital tied up before the product can be sold, and compare two "
            "branches with the same weekly outlay."
        ),
        "note": (
            "The lab assumes the product is made to order and paid for on delivery, as Marx "
            "does, so no circulation time is added; the next lessons add it. Marx's locomotive "
            "and ironclad durations are his; the £100 a week is illustrative."
        ),
    },
]
