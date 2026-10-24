"""The Turnover of Capital, lessons 7-11 -- Volume II, Chapters 13 to 17.

Every quotation is copied from /mnt/project-files/capital-texts/volume-2-kerr.txt
(the Kerr edition of Volume II); the comment beside each lesson gives its line
numbers. Footnote numerals are left out, the edition's interleaved page
markers are dropped, and the translator's double quotation marks inside a
quotation are printed as single curly quotes. The translator's spellings and
abbreviations ("labor", "turn-over", "p. st.") stand inside quotation marks.
Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    # Kerr vol. 2, l. 2154 and l. 2158 (the passage: working time and
    # production time; grain and timber); l. 2164 (tanning); l. 2166
    # (Bessemer, more fixed capital); l. 2168 (shoe-lasts); l. 2174 (Russia;
    # compensated for capital, not the labourer); l. 2181 (Hodgskin); l. 2191
    # (forestry); l. 2210 (MacCulloch and James Mill).
    {
        "slug": "the-time-of-production",
        "title": "The Time of Production",
        "module": "Chapter 13 · The Time of Production",
        "one_line": "Production time includes stretches in which nature works and nobody does, so the working time can be a small part of it, and shortening the one is not shortening the other.",
        "summary": (
            "Grain ripens, wine ferments and pots dry while the labour process stands still, "
            "and the capital waits through all of it. Compute the share of a production "
            "period that is working time and its effect on the turnovers a year, and see "
            "that cutting the production time of tanning from a year to two months speeds the "
            "turnover without saving an hour of labour."
        ),
        "key": [
            "production time ≥ working time",
            "the rest: nature works, capital waits",
            "turnover = production + circulation",
            "working share = working / production",
            "a faster process need not save labour",
        ],
        "key_label": "When nobody is working",
        "concepts_intro": (
            "The last chapter was about products that take a long time to make. This one is "
            "about products that take a long time while hardly being made at all."
        ),
        "concepts": [
            ("Production time",
             "The whole time capital is held in the sphere of production, from the first "
             "outlay until the product is ripe for sale. It includes the working time and "
             "every pause the product's own nature imposes."),
            ("Working time",
             "The part of the production time in which labour is actually applied. In "
             "industry the two often coincide; in agriculture the working time is a few "
             "months out of the year."),
            ("Natural processes",
             "Fermenting, drying, bleaching in the sun, ripening, growing: physical, "
             "chemical and physiological changes during which the labour process is "
             "suspended wholly or in part, while the capital stays tied up."),
        ],
        "read_title": "Working time inside production time, then the chapter line by line",
        "read_intro": (
            "The chapter's first two sentences state the whole distinction. Its examples "
            "come a paragraph later."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 13.</strong> &ldquo;The working time is always the "
                  "time of production, that is to say, the time during which capital is held in "
                  "the sphere of production. But vice versa, not all time during which capital "
                  "is engaged in the process of production is necessarily a working time. "
                  "&hellip; Winter grain needs about nine months to mature. Between the time of "
                  "sowing and harvesting the labor-process is almost entirely suspended. In "
                  "timber raising, after the sowing and the incidental preliminary work are "
                  "completed, the seed may require 100 years in order to be transformed into a "
                  "finished product, and during all this time it requires very insignificant "
                  "contributions of labor.&rdquo;"),
            ("p", "Read the first sentence carefully: every working hour is production time, and "
                  "not the other way round. Marx is not talking about nights and Sundays, the "
                  "pauses labour-power itself needs. He means pauses that belong to the "
                  "product: grape juice that must ferment and rest, pottery that must dry, "
                  "linen bleached on the grass. During them the object of labour is "
                  "&ldquo;subjected to lasting natural processes&rdquo; and the capital "
                  "advanced simply waits."),
            ("p", "So production time splits in two, a working period and a period when the "
                  "product is left to nature, and the turnover is lengthened by the second as "
                  "much as by the first. Where the pause is not fixed by a law of nature it can "
                  "be shortened. Chemical bleaching replaced the bleaching green; drying "
                  "apparatus replaced the open shed. Marx's sharpest example is leather:"),
            ("p", "<strong>Volume II, Chapter 13.</strong> &ldquo;Or, in tanning, where the "
                  "penetration of the tannic acid into the skins, by the old method, required "
                  "from six to eighteen months, while the new method, by means of the "
                  "air-pump, does it in one and a half to two months.&rdquo;"),
            ("p", "Nothing in that change saves the tanners an hour. The acid soaks in faster, "
                  "the capital comes back sooner, and the work is what it was. The same story "
                  "runs through the making of steel from the puddling process to Bessemer's, "
                  "with a sting in the tail: &ldquo;The time of production has been enormously "
                  "abbreviated, but the investment of fixed capital has increased "
                  "accordingly.&rdquo; American makers of shoe-lasts show the pause can come "
                  "first, too: the wood sat drying for eighteen months before anyone worked "
                  "on it."),
            ("p", "Agriculture is where the gap is widest. A German farm manual Marx quotes "
                  "counts roughly 170 to 215 working days spread over spring, summer and "
                  "autumn, and little but chores in winter; in northern Russia field work is "
                  "possible on 130 to 150 days a year. The peasants filled the winter with "
                  "weaving, tanning and smithing at home, which merchants soon organised. "
                  "Marx's verdict is short: &ldquo;For the capital, all the differences are "
                  "compensated in the turn-over. Not so for the laborer.&rdquo;"),
            ("p", "Thomas Hodgskin, the radical journalist who wrote <em>Labour Defended "
                  "against the Claims of Capital</em>, had already seen the consequence for "
                  "farmers: they cannot bring their goods to market in less than a year, and "
                  "must buy on credit all year from the shoemaker, tailor and smith whose goods "
                  "are made in days. And at the far end lies the forest, whose capital turns "
                  "over once in as much as 150 years, which in Marx's judgement makes forestry "
                  "&ldquo;little adapted for private, and therefore, capitalist "
                  "enterprise&rdquo;."),
            ("p", "The chapter names, in a single sentence, the people who got this wrong: the "
                  "&ldquo;senseless theories&rdquo; of MacCulloch, James Mill and others, an "
                  "attempt at &ldquo;identifying the diverging time of production with the "
                  "working time&rdquo;. Marx says no more here, and promises to return to them "
                  "in Volume III; the volume Engels published does not take them up by name. "
                  "The case they argued over is not in this chapter either. It comes from their "
                  "own books: wine that is worth more after years in a cellar, with no more "
                  "work done on it. Their case at its strongest: if value is labour and the "
                  "wine's value rose, something must have laboured. James Mill reckoned the "
                  "year in the cellar as so much more labour spent on the wine; John Ramsay "
                  "McCulloch let the operations of nature count as labour. On Marx's "
                  "definitions the waiting adds no value, and why capital that waits longer "
                  "still earns the going rate is left to Volume III's equalisation of profit "
                  "rates."),
            ("p", "The lab adds a working time inside the production period. Marx's winter grain "
                  "is nine months, 39 weeks, of which say 13 are worked; with 13 weeks to sell "
                  "it, the capital turns over once a year and a third of the production time "
                  "is work. Timber at a hundred years, with six months of work in it, turns "
                  "over once a century, and only `1/200` of its production time is work. Then the "
                  "tannery, with four weeks of work and four of selling: under the old method, "
                  "a year in the pits, it turns over `13/14` times a year; with the air-pump, "
                  "eight weeks, `13/3` times. The working time is four weeks in both."),
            ("p", "Production time is only half of a turnover. The next lesson, “The Time of "
                  "Circulation in the Turnover”, takes the other half: the weeks a product "
                  "spends on its way to a market and back as money."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "time",
            "money_unit": "£",
            "preset": "wheat",
            "presets": [
                {"id": "wheat", "label": "Marx's winter grain: 9 months to ripen, 3 of them worked",
                 "production_weeks": 39, "working_weeks": 13, "circulation_weeks": 13,
                 "year_weeks": 52, "expect": {"tuTurnover": "52 weeks", "tuTurnovers": "1 a year (a 52-week year)", "tuWorkingShare": "1/3 = 33.33%", "tuCirculationShare": "1/4 = 25%"}},
                {"id": "timber", "label": "Marx's timber: 100 years from seed, six months of work",
                 "production_weeks": 5200, "working_weeks": 26, "circulation_weeks": 0,
                 "year_weeks": 52, "expect": {"tuTurnover": "5,200 weeks", "tuTurnovers": "1/100 a year (a 52-week year)", "tuWorkingShare": "1/200 = 0.5%", "tuCirculationShare": "0 = 0%"}},
                {"id": "tanning-old", "label": "Tanning by the old method: a year in the pits, 4 weeks of work",
                 "production_weeks": 52, "working_weeks": 4, "circulation_weeks": 4,
                 "year_weeks": 52, "expect": {"tuTurnover": "56 weeks", "tuTurnovers": "13/14 a year (a 52-week year)", "tuWorkingShare": "1/13 = 7.69%", "tuCirculationShare": "1/14 = 7.14%"}},
                {"id": "tanning-air-pump", "label": "Tanning with the air-pump: 8 weeks, the same 4 weeks of work",
                 "production_weeks": 8, "working_weeks": 4, "circulation_weeks": 4,
                 "year_weeks": 52, "expect": {"tuTurnover": "12 weeks", "tuTurnovers": "13/3 a year (a 52-week year)", "tuWorkingShare": "1/2 = 50%", "tuCirculationShare": "1/3 = 33.33%"}},
            ],
            "panel_title": "Working time inside production time",
            "panel_intro": (
                "The production period, the working time within it and the circulation "
                "period go in, in weeks. The lab computes the turnover and the share of the "
                "production period that is work. Compare the two tanning presets: one tile "
                "moves a great deal, and the working time does not move at all."
            ),
        }),
        "steps_title": "Timing a production period with pauses in it",
        "steps_intro": "Four steps for any product that spends time unworked.",
        "steps": [
            ("Measure the whole production period",
             "From the first outlay to the moment the product is ready for sale, pauses "
             "included: nine months for winter grain, not the weeks of ploughing and reaping."),
            ("Mark the working time inside it",
             "Count only the weeks in which labour is applied. It cannot be longer than the "
             "production period it lies in."),
            ("Add circulation for the turnover",
             "The turnover is the whole production period plus the circulation period, and "
             "the turnovers a year follow by division."),
            ("Read the working share",
             "Divide the working time by the production period. A change that shortens the "
             "production period and leaves the working time alone raises this share and the "
             "turnovers together."),
        ],
        "worked": {
            "title": "Nine months of grain, three of work",
            "intro": [
                "Winter grain takes 39 weeks from sowing to harvest, of which 13 are worked, "
                "and 13 weeks to sell. You want the turnover, the turnovers a year and the "
                "share of production time that is work.",
            ],
            "lines": [
                "turnover = 39 + 13 = 52 weeks",
                "turnovers = 52 / 52 = 1 a year",
                "working share = 13 / 39 = 1/3",
            ],
            "after": [
                "Two-thirds of the production time no one is working on the crop, and the "
                "capital is tied up all the same. However hard the farm works in its thirteen "
                "weeks, it cannot turn over more than once a year.",
            ],
        },
        "quiz_title": "Production time and working time",
        "quiz": [
            {"q": "A crop needs 26 weeks from sowing to harvest, 13 of them worked, and 26 weeks "
                  "to sell, in a 52-week year. How many times does the capital turn over?",
             "a": ["2", "4", "1", "4/3"],
             "c": 2,
             "why": "The turnover is `26 + 26 = 52` weeks, so once a year. Two divides by the "
                    "production period alone, 4 by the working time alone, and `4/3` by the "
                    "working time plus circulation, leaving out the weeks the crop grows "
                    "unworked."},
            {"q": "Which change shortens production time without shortening working time?",
             "a": ["Tanning with the air-pump in place of the old pits",
                   "Paying the tanners for fewer hours",
                   "Selling the leather to a nearer market",
                   "Hiring more tanners to finish the work sooner"],
             "c": 0,
             "why": "The air-pump cuts the months the acid needs to soak in and leaves the work "
                    "as it was. Fewer paid hours or more hands change the labour; a nearer "
                    "market shortens circulation time, not production time."},
            {"q": "Grain takes 39 weeks to ripen, of which 13 are worked. What share of its "
                  "production time is working time?",
             "a": ["1/3", "1/4", "3", "1/2"],
             "c": 0,
             "why": "`13/39 = 1/3`. A quarter is 13 weeks out of a 52-week year, not out of "
                    "the production period; 3 divides the wrong way; a half has no basis in "
                    "the figures."},
            {"q": "Whose error does Marx mean when he speaks of identifying the time of "
                  "production with the working time?",
             "a": ["Quesnay's, who thought only agriculture productive",
                   "That of MacCulloch, James Mill and others, who let natural processes count as labour",
                   "Adam Smith's, who called the merchant's capital circulating",
                   "Hodgskin's, who described the farmers' dependence"],
             "c": 1,
             "why": "The chapter names MacCulloch and James Mill for the theories that "
                    "identify the two times; the wine in the cellar, their standard case, "
                    "comes from their own writings, not from this chapter. "
                    "Quesnay and Smith appear in Chapter 10 for other mistakes, and Marx cites "
                    "Hodgskin with approval."},
        ],
        "mistakes": [
            ("Thinking that shortening production time always shortens labour time",
             "In the two tanning presets the work is four weeks both times. The production "
             "period falls from 52 weeks to 8, and the turnovers rise from `13/14` to `13/3` "
             "a year. Not an hour of labour was saved; the capital simply waited less."),
            ("Treating the unworked months as idle capital that costs nothing",
             "The capital is advanced for the whole production period, worked or not. Winter "
             "grain ties up its outlay for nine months though only three are worked, and the "
             "wheat preset turns over once a year for that reason."),
            ("Counting natural processes as labour",
             "That was MacCulloch's way out of the wine-cellar puzzle, one of the theories "
             "Marx calls senseless. On "
             "Marx's definitions value is created only by labour, so the months in which the "
             "grain ripens or the wine matures add time to the turnover and no value to the "
             "product."),
        ],
        "standard": (
            "Finish when you can separate working time from production time and time a turnover.",
            "Given a production period, the working time within it and a circulation period, "
            "compute the turnover, the turnovers a year and the working share of production "
            "time, and say whether a stated change shortens production time, working time or "
            "both."
        ),
        "note": (
            "The lab treats the working time as a single figure inside the production period; "
            "it does not schedule the work, and it ignores that advances in agriculture fall "
            "unevenly through the year, which Marx stresses. The grain's nine months and the "
            "tanning ranges are Marx's; the weeks of work and of selling are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 2, l. 2228 and l. 2244 (the passage: the time of selling;
    # India, four months each way); l. 2232 (distance; a railway alters
    # relative distance); l. 2234 (frequency of sailings); l. 2240-2242 (the
    # world market); l. 2244 (terms of credit); l. 2264 (wool auctions);
    # l. 2274 (money capital forgotten).
    {
        "slug": "the-time-of-circulation-in-turnover",
        "title": "The Time of Circulation in the Turnover",
        "module": "Chapter 14 · The Time of Circulation",
        "one_line": "The time a product spends travelling to market and coming back as money is part of the producer's turnover, so a distant market slows the producer's capital as surely as a slow machine.",
        "summary": (
            "Circulation time is the time of selling and the time of buying, and its largest "
            "part is often distance. Compute how a market four months away and four months "
            "back lengthens a turnover, Marx's goods shipped to India, and how a faster "
            "passage or a nearer market restores the turnovers a year."
        ),
        "key": [
            "circulation = selling time + buying time",
            "distance fetters capital as commodities",
            "turnover = production + circulation",
            "India: 4 months out + 4 back = 8",
            "transport cuts absolute, not relative, time",
        ],
        "key_label": "Time spent away from the workshop",
        "concepts_intro": (
            "Chapter 14 is about the half of a turnover that happens outside production. "
            "Three ideas carry it."
        ),
        "concepts": [
            ("Selling time",
             "The time capital spends as commodity capital: travelling to its market and "
             "waiting there to be sold. Marx calls it relatively the most decisive part of "
             "circulation time."),
            ("Buying time",
             "The time capital spends as money capital before it is turned back into means "
             "of production and labour-power. It requires that part of every capital be held "
             "in the form of money."),
            ("Distance in time",
             "Better transport shortens every journey, but not equally: a railway can bring a "
             "far market nearer in time than a closer one it does not reach. What matters to "
             "turnover is distance measured in weeks."),
        ],
        "read_title": "The time of selling, and Marx's goods for India",
        "read_intro": (
            "The passage joins the chapter's definition of the most decisive part of "
            "circulation time to its one worked example."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 14.</strong> &ldquo;One of the sections of the "
                  "time of circulation&mdash;relatively the most decisive&mdash;consists of the "
                  "time of selling, the period during which capital has the form of "
                  "commodity-capital. &hellip; For instance, some commodities are shipped to "
                  "India. This requires, say, four months. Let us assume that the selling time "
                  "is equal to zero, that is to say, the commodities are made to order and are "
                  "paid for on delivery to the agent of the producer. The return of the money "
                  "(no matter what may be its form) requires again four months. Thus it takes "
                  "eight months, before the same capital can again serve as productive capital "
                  "and renew the same operations.&rdquo;"),
            ("p", "Notice how much Marx gives away in the example. The goods are made to order; "
                  "they are paid for on arrival; there is no waiting in a warehouse at all. "
                  "And still the capital is gone for eight months, four as cloth on a ship and "
                  "four as money or bills coming home. During the voyage, as he says earlier "
                  "in the chapter, &ldquo;capital finds itself fettered in the form of "
                  "commodity-capital&rdquo;."),
            ("p", "Selling time varies between capitalists in one branch and between good years "
                  "and bad, and Marx does not linger on that. Distance he treats as the steady "
                  "cause. Better ships and railways shorten journeys absolutely, but they "
                  "change relative distances unevenly: &ldquo;a railroad, which leads from a "
                  "place of production to an inland center of population, may relatively or "
                  "absolutely prolong the distance to a nearer point inland not connected with "
                  "a railroad&rdquo;. Towns on the new lines grew; towns left on a branch with "
                  "few trains declined."),
            ("p", "Frequency matters as well as speed. When ships clear for New York from "
                  "Liverpool on successive days, and goods trains leave Manchester for London "
                  "several times a day, goods need not pile up waiting for the one sailing, "
                  "and money flows back in a steady stream rather than in lumps. The same "
                  "progress pushes the other way, though: the cheaper it is to reach distant "
                  "markets, the more production is for the world market, and the more of "
                  "society's capital is at any moment on its way somewhere."),
            ("p", "Marx's India example was not idle. Trade with the East ran on bills of "
                  "exchange of six or ten months, and turnover was part of the reason: "
                  "&ldquo;The differences in the turn-over thus caused are one of the material "
                  "bases of the various terms of credit.&rdquo; The banks tried in 1866 to cut "
                  "the Indian usance to four months and had to give up; a bracketed sentence "
                  "adds that the Suez canal has since revolutionised all of it."),
            ("p", "Buying time is the other half. A wool spinner in London had to buy at the "
                  "great auctions held every three months, and so had to keep money for three "
                  "months' wool; a cotton spinner could buy more evenly. Either way part of the "
                  "capital always waits as money. Marx closes the chapter on the point he will "
                  "build on next: &ldquo;It is especially the portion always available as "
                  "money-capital which is forgotten by economists&rdquo;."),
            ("p", "The lab takes a production period of four months, `52/3` weeks, and varies "
                  "only the circulation. A market a month away, two months there and back, gives a turnover "
                  "of 26 weeks, twice a year. Marx's India, eight months there and back, gives "
                  "52 weeks: once a year, with two-thirds of the turnover in circulation. Halve "
                  "each leg of the voyage and the turnover falls to `104/3` weeks, `3/2` a "
                  "year. Nothing in the factory changed in any of the three."),
            ("p", "Distance and selling time lengthen the turnover; Marx now has every part of "
                  "it. The next lesson, “Turnover Time and the Capital Advanced”, asks what a "
                  "business must advance to keep working while its last product is still on "
                  "the road."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "time",
            "money_unit": "£",
            "preset": "india",
            "presets": [
                {"id": "near", "label": "A nearer market: four months' production, two months out and back",
                 "production_weeks": "52/3", "circulation_weeks": "26/3", "year_weeks": 52,
                 "expect": {"tuTurnover": "26 weeks", "tuTurnovers": "2 a year (a 52-week year)", "tuWorkingShare": "1 = 100%", "tuCirculationShare": "1/3 = 33.33%"}},
                {"id": "india", "label": "Marx's India: four months out, four months back",
                 "production_weeks": "52/3", "circulation_weeks": "104/3", "year_weeks": 52,
                 "expect": {"tuTurnover": "52 weeks", "tuTurnovers": "1 a year (a 52-week year)", "tuWorkingShare": "1 = 100%", "tuCirculationShare": "2/3 = 66.67%"}},
                {"id": "faster-passage", "label": "India with a passage twice as fast: two months each way",
                 "production_weeks": "52/3", "circulation_weeks": "52/3", "year_weeks": 52,
                 "expect": {"tuTurnover": "104/3 weeks", "tuTurnovers": "3/2 a year (a 52-week year)", "tuWorkingShare": "1 = 100%", "tuCirculationShare": "1/2 = 50%"}},
            ],
            "panel_title": "The same factory, three markets",
            "panel_intro": (
                "The production period is four months, written as 52/3 weeks, in every "
                "preset; only the circulation period changes. The lab adds the two and "
                "divides the year by the sum. Watch the last-but-one tile: the share of the "
                "turnover spent in circulation."
            ),
        }),
        "steps_title": "Adding circulation to a turnover",
        "steps_intro": "Four steps for any product that must travel to be sold.",
        "steps": [
            ("Time the journey out",
             "Count the time the product spends as commodity capital: carriage to the market "
             "and any waiting there before sale."),
            ("Time the journey back",
             "Count the time until the money, or a bill for it, is home and can be laid out "
             "again. Marx's India example takes four months each way."),
            ("Add both to the production period",
             "The turnover is production time plus the whole circulation time; the turnovers "
             "a year follow by dividing the year by it."),
            ("Compare markets at the same production time",
             "Hold the factory fixed and change only the circulation. Every change in the "
             "turnovers is then due to the market's distance alone."),
        ],
        "worked": {
            "title": "Four months to India and four back",
            "intro": [
                "A factory's production period is four months, `52/3` weeks. Its goods go to "
                "India, four months out and four months back as money, with no waiting to be "
                "sold. You want the turnover and the turnovers a year.",
            ],
            "lines": [
                "circulation = 52/3 + 52/3 = 104/3 weeks",
                "turnover = 52/3 + 104/3 = 52 weeks",
                "turnovers = 52 / 52 = 1 a year",
                "circulation share = (104/3) / 52 = 2/3",
            ],
            "after": [
                "Sold nearer home, a month each way, the same factory turns over twice a "
                "year. Distance alone halved its turnovers.",
            ],
        },
        "quiz_title": "Circulation time",
        "quiz": [
            {"q": "Production takes 8 weeks. The goods take 6 weeks to reach their market and "
                  "the money 6 weeks to return. How many times a year does the capital turn "
                  "over, in a 52-week year?",
             "a": ["13/2", "13/5", "26/7", "52/6"],
             "c": 1,
             "why": "The turnover is `8 + 6 + 6 = 20` weeks and `52/20 = 13/5`. `13/2` divides "
                    "by production alone, `26/7` leaves out the journey back, and `52/6` "
                    "divides by one leg of the journey."},
            {"q": "In Marx's India example the goods are made to order and paid for on "
                  "delivery. Why is the capital still away for eight months?",
             "a": ["Because the goods wait in an Indian warehouse",
                   "Because the voyage out and the return of the money each take four months",
                   "Because the working period is eight months",
                   "Because the merchant holds the goods for speculation"],
             "c": 1,
             "why": "Marx sets the selling time to zero precisely to isolate distance: four "
                    "months out, four back. No warehouse, no long working period and no "
                    "speculation enter the example."},
            {"q": "On Marx's account, why must part of every capital be held as money?",
             "a": ["Because the law requires a reserve",
                   "Because buying time means money waits to be laid out on materials and wages",
                   "Because money earns interest while it waits",
                   "Because fixed capital must be paid in cash"],
             "c": 1,
             "why": "The buying half of circulation time keeps part of the capital in money "
                    "form: wages are paid weekly and materials bought when markets allow. "
                    "Part II assumes no credit, so no interest; no law or rule about fixed "
                    "capital is involved."},
        ],
        "mistakes": [
            ("Thinking circulation time is wasted only for the merchant",
             "It is the producer's own capital that is fettered. In the India preset nothing "
             "in the factory changes and its capital turns over once a year instead of twice, "
             "with two-thirds of the turnover spent in circulation. If a merchant buys the "
             "goods, Marx notes in Chapter 16, he simply advances that additional capital in the "
             "manufacturer's place."),
            ("Measuring distance in miles",
             "What lengthens a turnover is time. A railway can make a distant town nearer in "
             "weeks than a closer one it bypasses, and frequent sailings shorten the wait "
             "before departure without changing the voyage."),
            ("Forgetting the journey back",
             "Selling is not the end of circulation. The money must come home before it can "
             "buy labour-power again; in Marx's example that is another four months."),
        ],
        "standard": (
            "Finish when you can compute what distance does to a turnover.",
            "Given a production period and the times out to a market and back, compute the "
            "turnover, the turnovers a year and the share of the turnover spent in "
            "circulation, and compare two markets at the same production period."
        ),
        "note": (
            "The lab treats circulation as a fixed number of weeks; it does not model a "
            "market's uncertainty, the price risk Marx says grows with the time abroad, or the "
            "credit that bridged the gap in practice. Marx's four months each way are his; the "
            "four months of production and the nearer market are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 09
    # Kerr vol. 2, l. 2284 (the passage: nine weeks at £100, three of
    # circulation); l. 2288 (reduce the scale to £75); l. 2298 (capital II
    # of £300); l. 2312 (£300 set free); l. 2372-2374 (hollow skulls; one
    # part in production, another in circulation); l. 2853 (the rule);
    # l. 2881 (900 to 800); l. 2887 (2/9 more); l. 2889 (Engels' note);
    # l. 2912 (prices halve: £450).
    {
        "slug": "turnover-time-and-capital-advanced",
        "title": "Turnover Time and the Capital Advanced",
        "module": "Chapter 15 · Influence of the Time of Circulation on the Magnitude of an Advance of Capital",
        "one_line": "To keep working while its last product is being sold, a business must advance a second capital for the circulation period, and the two capitals together are what the turnover costs.",
        "summary": (
            "Nine weeks of work at £100 a week make £900 of product, which then takes three "
            "weeks to sell. Compute capital I for the working period and the additional "
            "capital II that keeps production going through the circulation period, the "
            "capital set free at the close of each working period, and what a faster sale "
            "or a fall in prices releases."
        ),
        "key": [
            "capital I = working weeks · weekly outlay",
            "capital II = circulation weeks · outlay",
            "advanced = I + II",
            "II / (I + II) = circulation / turnover",
            "set free: II, when working > circulation",
        ],
        "key_label": "Two capitals for one business",
        "concepts_intro": (
            "This is the longest and most arithmetical chapter of Part II, and Engels says "
            "preparing it gave him no small trouble. Three ideas are enough to follow it."
        ),
        "concepts": [
            ("Capital I",
             "The circulating capital advanced for one working period: the weekly outlay "
             "times the weeks of work. When the period ends it becomes commodity capital and "
             "is useless for production until it is sold."),
            ("Capital II",
             "The additional capital that keeps production going while capital I circulates: "
             "the weekly outlay times the weeks of circulation. Without it the business "
             "either stands idle or shrinks its scale."),
            ("Capital set free",
             "From the second turnover on, money returns in lumps the size of capital I while "
             "the current working period needs only part of it. The rest lies free until the "
             "next period. Marx's rule says when this happens and how much."),
        ],
        "read_title": "Nine weeks of work and three of selling",
        "read_intro": (
            "The chapter opens with its main example. Everything after it varies the two "
            "periods."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 15.</strong> &ldquo;Take the commodity-capital "
                  "which is the product of a certain working period, for instance, of nine "
                  "weeks. &hellip; Let this value be 900 pounds sterling, so that the weekly "
                  "outlay is 100 pounds sterling. &hellip; Let the time of circulation be three "
                  "weeks. Then the entire time of turn-over is twelve weeks. At the end of nine "
                  "weeks, the advanced productive capital is converted into a commodity-capital, "
                  "but now it exists for three weeks in the period of circulation. The new time "
                  "of production, therefore, cannot commence until the beginning of the "
                  "thirteenth week&rdquo;."),
            ("p", "So the factory would stand still three weeks in every twelve, a quarter of "
                  "the year. Marx sees two ways out. The first is to shrink: spread the £900 "
                  "over twelve weeks at £75 a week, so that work never stops. That means a "
                  "smaller business in every respect, fixed capital included, and in most "
                  "branches competition sets a minimum scale below which no one survives."),
            ("p", "The second way is more capital. While the first £900 is out being sold, "
                  "a further £300 keeps the work going, and Marx puts the proportion in one "
                  "line: &ldquo;During the period of turn-over of twelve weeks, 1,200 pounds "
                  "sterling are successively invested in twelve weeks, and 300 is one quarter "
                  "of this sum as three weeks is of twelve.&rdquo; Capital II stands to the "
                  "whole as circulation time stands to the turnover."),
            ("p", "Then the two capitals begin to cross. In the thirteenth week the first £900 "
                  "returns, but the second working period, opened by the £300 in week ten, "
                  "already has three of its nine weeks done. It needs only £600 more, and "
                  "&ldquo;Thus 300 pounds of the original 900 are set free&rdquo; to play the "
                  "part capital II played before. From then on, at the close of each working "
                  "period, £300 lies free."),
            ("p", "Marx works through case after case and draws a rule. When the working and "
                  "circulation periods are equal, the two capitals relieve each other without "
                  "crossing, and nothing is set free; likewise when the circulation period is a "
                  "whole multiple of the working period. Otherwise capital is set free at the "
                  "close of every working period: the whole of capital II if the working period "
                  "is the longer, and if it is the shorter, the capital that covers the excess "
                  "of circulation over the largest multiple of working periods. With four weeks "
                  "of work and five of circulation, £100 is set free each time."),
            ("p", "Behind the tables is a point Marx thinks the economists always miss: "
                  "&ldquo;While one part is busy in the process of production, another must "
                  "always be engaged in the process of circulation.&rdquo; Say that £1,000 has "
                  "turned over five times, he writes, and &ldquo;the recollection of the time "
                  "of circulation disappears in the hollow skulls of the capitalists&rdquo;, "
                  "as if the whole £1,000 had been at work all year."),
            ("p", "The chapter's last section changes one thing at a time. If the circulation "
                  "time shrinks from three weeks to two, a business with six weeks of work "
                  "needs £800 instead of £900, and £100 is thrown on the money market though "
                  "nobody saved it. If circulation stretches to five weeks, it needs `2/9` "
                  "more, £200, which can only be borrowed. If the prices of materials and "
                  "labour-power halve, the nine-week turnover needs £450 instead of £900. Marx "
                  "uses these to show how a glut or a scarcity of loanable money can arise with "
                  "no change at all in the quantity of money."),
            ("p", "Then, in the middle of the section, the editor speaks:"),
            ("p", "<strong>Volume II, Chapter 15, Engels' note.</strong> &ldquo;Consequently "
                  "Marx entangled himself to such an extent in his computation of turn-overs, "
                  "that the result, so far as he completed his work, contained various errors "
                  "and contradictions. In the diagrams given above, I have preserved only the "
                  "simplest and arithmetically correct data&rdquo;."),
            ("p", "Engels goes further and doubts the importance of the release Marx found: "
                  "money equal to capital I comes back at the end of every working period "
                  "whatever the proportions, he says, so a release of money happens "
                  "&ldquo;under all circumstances&rdquo;. Both men agree on what matters, that "
                  "a considerable part of industrial capital must always be held as money. The "
                  "lab follows the rule Marx states in the chapter's conclusions and leaves "
                  "their disagreement where it is."),
            ("p", "On Marx's figures the lab gives £1,200, capital I £900 and capital II £300, "
                  "with £300 set free each working period and `25/6` turnovers in a 50-week "
                  "year. Five weeks against five gives £500 and £500 and nothing set free. Four "
                  "weeks against five gives £400 and £500, and £100 set free. Six weeks with "
                  "two of circulation needs only £800; and halving prices on six weeks and "
                  "three releases £450."),
            ("p", "All of this concerned circulating capital as a whole. The next lesson, “The "
                  "Turnover of Variable Capital”, takes the part of it paid in wages, and asks "
                  "what turnover does to the rate of surplus value."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "advance",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 9 weeks' work at £100, 3 of circulation",
                 "working_weeks": 9, "circulation_weeks": 3, "weekly_outlay": 100,
                 "year_weeks": 50, "expect": {"tuAdvance": "£1,200 = I £900 + II £300", "tuFreed": "£300 each working period", "tuTurnovers": "25/6 a year (a 50-week year)"}},
                {"id": "equal", "label": "Marx's equal periods: 5 weeks' work, 5 of circulation",
                 "working_weeks": 5, "circulation_weeks": 5, "weekly_outlay": 100,
                 "year_weeks": 50, "expect": {"tuAdvance": "£1,000 = I £500 + II £500", "tuFreed": "£0 each working period", "tuTurnovers": "5 a year (a 50-week year)"}},
                {"id": "longer-circulation", "label": "Marx's 4 weeks' work against 5 of circulation",
                 "working_weeks": 4, "circulation_weeks": 5, "weekly_outlay": 100,
                 "year_weeks": 50, "expect": {"tuAdvance": "£900 = I £400 + II £500", "tuFreed": "£100 each working period", "tuTurnovers": "50/9 a year (a 50-week year)"}},
                {"id": "faster-sale", "label": "Marx's 6 weeks' work, circulation cut from 3 weeks to 2",
                 "working_weeks": 6, "circulation_weeks": 2, "weekly_outlay": 100,
                 "year_weeks": 50, "expect": {"tuAdvance": "£800 = I £600 + II £200", "tuFreed": "£200 each working period", "tuTurnovers": "25/4 a year (a 50-week year)"}},
                {"id": "prices-halve", "label": "Marx's 6 weeks and 3, then prices halve: £50 a week",
                 "working_weeks": 6, "circulation_weeks": 3, "weekly_outlay": 100,
                 "new_outlay": 50, "year_weeks": 50, "expect": {"tuAdvance": "£900 = I £600 + II £300", "tuFreed": "£450 released", "tuTurnovers": "50/9 a year (a 50-week year)"}},
            ],
            "panel_title": "What a continuous business must advance",
            "panel_intro": (
                "The working period, the circulation period and the weekly outlay go in, with "
                "a 50-week year as in the chapter. The lab computes capital I for the working "
                "period, capital II for the circulation period, and the capital set free at "
                "the close of each working period; with a new weekly outlay it computes the "
                "capital released instead."
            ),
        }),
        "steps_title": "Computing the capital a continuous business needs",
        "steps_intro": "Four steps, with the weekly outlay held constant.",
        "steps": [
            ("Compute capital I",
             "Multiply the weekly outlay by the weeks of the working period. This is what the "
             "first product absorbs before it can be sold."),
            ("Compute capital II",
             "Multiply the weekly outlay by the weeks of the circulation period. This keeps "
             "work going while capital I is being sold."),
            ("Add, and check the proportion",
             "The capital advanced is I plus II. Capital II is to the whole as the circulation "
             "period is to the turnover."),
            ("Apply the rule for capital set free",
             "Equal periods, or circulation a whole multiple of the working period: nothing. "
             "Working period longer: capital II. Circulation longer otherwise: the outlay for "
             "the excess of circulation over the largest multiple of working periods."),
        ],
        "worked": {
            "title": "Marx's nine weeks and three",
            "intro": [
                "A business lays out £100 a week. Its working period is nine weeks and its "
                "circulation period three, in a 50-week year. You want the capital advanced, "
                "its two parts, and the capital set free.",
            ],
            "lines": [
                "capital I = 9 · £100 = £900",
                "capital II = 3 · £100 = £300",
                "advanced = £900 + £300 = £1,200",
                "II share = 300 / 1,200 = 3 / 12 = 1/4",
                "working 9 > circulation 3: £300 set free",
            ],
            "after": [
                "From the thirteenth week on, £900 returns while the current working period "
                "needs only £600 more, so £300 lies free at the close of each working period.",
            ],
        },
        "quiz_title": "The capital advanced",
        "quiz": [
            {"q": "A business lays out £200 a week, works 8 weeks and needs 4 weeks to sell. "
                  "What capital must it advance to work without a break?",
             "a": ["£1,600", "£800", "£2,400", "£2,000"],
             "c": 2,
             "why": "Capital I is `8 · 200 = 1,600` and capital II `4 · 200 = 800`, so £2,400. "
                    "£1,600 is capital I alone, £800 capital II alone, and £2,000 adds only two "
                    "weeks of circulation."},
            {"q": "In the same business, how much capital is set free at the close of each "
                  "working period, on Marx's rule?",
             "a": ["Nothing", "£800", "£1,600", "£400"],
             "c": 1,
             "why": "The working period is longer than the circulation period, so the whole of "
                    "capital II, £800, is set free. Nothing is set free only when the periods "
                    "are equal or circulation is a whole multiple of work; £1,600 is capital I, "
                    "and £400 is half of capital II."},
            {"q": "Working period 4 weeks, circulation 8 weeks, £100 a week. How much is set "
                  "free at the close of each working period?",
             "a": ["£400", "£800", "Nothing", "£1,200"],
             "c": 2,
             "why": "Eight weeks is exactly twice four, so the capitals relieve one another "
                    "without crossing and nothing is set free. £400 and £800 are capital I and "
                    "capital II, and £1,200 the whole capital advanced."},
            {"q": "Circulation time shrinks from 3 weeks to 2 for a business with 6 weeks of work "
                  "at £100 a week. What happens to the capital it needs?",
             "a": ["It falls from £900 to £800, and £100 becomes money capital seeking use",
                   "It is unchanged, because production is on the same scale",
                   "It rises, because the business now turns over faster",
                   "It falls from £900 to £600, because circulation needs no capital"],
             "c": 0,
             "why": "Capital II falls from £300 to £200, so the business needs £800, and the "
                    "£100 is thrown on the money market. The scale is the same, but the capital "
                    "advanced is not; it cannot rise; and two weeks of circulation still need "
                    "£200."},
        ],
        "mistakes": [
            ("Thinking a capital needs only enough to cover one working period",
             "Then it stops whenever its product is being sold. On Marx's figures £900 covers "
             "the nine weeks of work, and the three weeks of circulation need £300 more; the "
             "first tile reads £1,200, not £900. The only alternative is to shrink to £75 a "
             "week."),
            ("Thinking capital II is needed only once",
             "Capital II is part of the capital advanced for as long as the business runs. "
             "What changes after the first turnover is that the two capitals cross, and part "
             "of the money returning lies free between working periods."),
            ("Expecting capital to be set free in every case",
             "With equal periods, or circulation a whole multiple of work, the capitals "
             "relieve one another exactly. The equal preset shows £500 and £500 and £0 set "
             "free."),
        ],
        "standard": (
            "Finish when you can compute the capital a business must advance to work without a break.",
            "Given a working period, a circulation period and a weekly outlay, compute capital "
            "I, capital II, the capital advanced and the capital set free at the close of each "
            "working period, and the capital released by a shorter circulation period or "
            "lower prices."
        ),
        "note": (
            "Engels edited this chapter heavily, says Marx's own computations contained "
            "errors, and doubts that the release of capital matters as much as Marx thought; "
            "the lab applies the rule of the chapter's conclusions and does not settle that "
            "disagreement. It also assumes, with Marx, no credit and identical turnovers all "
            "year. The figures are Marx's own examples."
        ),
    },
    # ---------------------------------------------------------------- 10
    # Kerr vol. 2, l. 3032 and l. 3034 (the passage: the annual rate of
    # surplus value, 1000%); l. 3016 (2,500 circulating; 5-week turnover);
    # l. 3044 (capital B); l. 3050 (a difference of 900%); l. 3052 (the
    # Ricardian school); l. 3058 (B on A's footing: 50,000); l. 3153 (S' =
    # s'n); l. 3167-3173 (capital C, 90 10/11%); l. 3256 (social
    # intelligence after the fact).
    {
        "slug": "the-turnover-of-variable-capital",
        "title": "The Turnover of Variable Capital",
        "module": "Chapter 16 · The Turn-Over of the Variable Capital",
        "one_line": "The annual rate of surplus value is the real rate times the turnovers of the variable capital, so two capitals that exploit their workers equally can show annual rates of 1,000% and 100%.",
        "summary": (
            "Chapter 16 sets two capitals side by side that employ the same workers at the "
            "same rate of exploitation, one turning its variable capital over ten times a "
            "year and one once. Compute the annual rate of surplus value as the real rate "
            "times the number of turnovers, and the mass of surplus value, which is the same "
            "for both."
        ),
        "key": [
            "annual rate S′ = s / v advanced",
            "S′ = s′ · n",
            "s′: the real rate, per turnover",
            "A: 100% · 10 = 1,000%",
            "B: 100% · 1 = 100%, same mass",
        ],
        "key_label": "Two rates of surplus value",
        "concepts_intro": (
            "Volume I's rate of surplus value compared the surplus value a capital produces "
            "with the variable capital that produced it. This chapter asks what happens when "
            "the comparison is made per year."
        ),
        "concepts": [
            ("Annual rate of surplus value",
             "The surplus value produced in a year divided by the variable capital "
             "advanced. Marx writes it S′, against the real rate s′."),
            ("Variable capital advanced and employed",
             "The variable capital advanced is the sum the capitalist must have in hand; the "
             "variable capital employed in a year is what is actually paid out for "
             "labour-power over the year. The first times the turnovers is the second."),
            ("S′ = s′n",
             "The annual rate equals the real rate times the turnovers of the variable "
             "capital. It equals the real rate only when the variable capital turns over "
             "exactly once a year."),
        ],
        "read_title": "Capital A, then capital B",
        "read_intro": (
            "The passage defines the annual rate on capital A. Capital B arrives a page "
            "later, and the chapter is the comparison between them."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 16, §1.</strong> &ldquo;If 500 p. st. of "
                  "variable capital produce a surplus-value of 500 p. st., then 5000 p. st. "
                  "produce ten times 500, or 5000 p. st. of surplus-value. The proportion of "
                  "the total quantity of surplus-value produced during one year to the value of "
                  "the advanced variable capital is what we call the annual rate of "
                  "surplus-value. In the present case, this is as 5000 to 500, or "
                  "1000%.&rdquo;"),
            ("p", "Set up capital A as Marx does. A circulating capital of £2,500, a fifth of it, "
                  "£500, variable. A turnover of five weeks, four of work and one of "
                  "circulation, in a 50-week year: ten turnovers. Each week £100 of wages sets "
                  "labour in motion and, at a rate of surplus value of 100%, yields £100 of "
                  "surplus value. Over the year £5,000 of wages is paid, from the same £500 "
                  "coming back ten times, and £5,000 of surplus value is produced. On £500 "
                  "advanced, that is 1,000%."),
            ("p", "Marx then writes the general formula, `S′ = s′·n`: the annual rate is the real "
                  "rate, 100%, times the turnovers, 10. In the Kerr text it is &ldquo;S' is "
                  "equal to s'vn/v, or s'n.&rdquo; Only when n is 1 is the annual rate the real "
                  "one."),
            ("p", "Now capital B. It advances £5,000 for a whole 50-week year and turns it over "
                  "once. It too pays £100 a week, employs the same number of workers for the "
                  "same day at the same rate, and produces £5,000 of surplus value. Its annual "
                  "rate is `5,000/5,000`, 100%. &ldquo;Nevertheless, there is a difference of "
                  "900% in the annual rate of surplus-value of the two capitals A and "
                  "B.&rdquo;"),
            ("p", "This is the puzzle, and Marx says it had a history. The appearance that "
                  "surplus value depends on circulation as well as on exploitation &ldquo;has "
                  "completely routed the Ricardian school since the beginning of the twenties "
                  "of the 19th century&rdquo;, in its disguised form as the annual rate of "
                  "profit. Ricardo's followers could not explain, from labour alone, why "
                  "capitals that turn over at different speeds earned what looked like the same "
                  "annual return. Marx names no one here; histories of the school usually "
                  "count Samuel Bailey and Robert Torrens among the critics who pressed that "
                  "kind of point. Marx's answer is to separate the variable capital "
                  "advanced from the variable capital employed."),
            ("p", "Put B on A's footing to see it. Let B spend its £5,000 every five weeks, "
                  "£1,000 a week: then it too turns over ten times, its annual rate is 1,000%, "
                  "and it produces £50,000, ten times A's, because it employs ten times the "
                  "labour. The real rate of surplus value never moved. What moved was how much "
                  "money had to be advanced to keep a given amount of labour at work."),
            ("p", "The rule also runs below one turnover. Marx's capital C needs 55 weeks to turn "
                  "over £5,500 at £100 a week. In a 50-week year it employs £5,000 and produces "
                  "£5,000 of surplus value on £5,500 advanced: `10/11` turnovers, an annual "
                  "rate of `10/11`, which Marx prints as &ldquo;90 10-11%&rdquo;."),
            ("p", "The last two sections turn to who pays whom with what. A's workers, from the "
                  "second turnover on, are paid with the money form of what they made in the "
                  "first; B's are paid out of money that will not be replaced by their product "
                  "until next year. Scale that up to a railway, which takes labour and means of "
                  "production out of the market for years and puts nothing back, and you get "
                  "pressure on prices and on the money market. A communist society, Marx "
                  "says, would reckon in advance how much it could spare; in capitalist "
                  "society, &ldquo;where social intelligence does not act until after the "
                  "fact, great disturbances will and must occur&rdquo;."),
            ("p", "The lab computes the turnover from the working and circulation periods and "
                  "multiplies. Capital A: 1,000% and £5,000 a year. Capital B: 100% and the same "
                  "£5,000. Capital C: `10/11` and £5,000 again. And B on A's footing: 1,000% "
                  "and £50,000. The rate of surplus value typed in is 100% in every preset."),
            ("p", "A turns its surplus value into money ten times a year, B once. The next "
                  "lesson, “The Circulation of Surplus Value”, asks where the money comes from "
                  "to turn surplus value into money at all."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "annual",
            "money_unit": "£",
            "preset": "marx-a",
            "presets": [
                {"id": "marx-a", "label": "Marx's capital A: £500 variable, a 5-week turnover, 100%",
                 "variable": 500, "s_rate": 1, "working_weeks": 4, "circulation_weeks": 1,
                 "year_weeks": 50, "expect": {"tuTurnover": "5 weeks", "tuTurnovers": "10 a year (a 50-week year)", "tuAnnualRate": "10 = 1,000%", "tuMassS": "£5,000 a year"}},
                {"id": "marx-b", "label": "Marx's capital B: £5,000 advanced for the 50-week year, 100%",
                 "variable": 5000, "s_rate": 1, "working_weeks": 50, "circulation_weeks": 0,
                 "year_weeks": 50, "expect": {"tuTurnover": "50 weeks", "tuTurnovers": "1 a year (a 50-week year)", "tuAnnualRate": "1 = 100%", "tuMassS": "£5,000 a year"}},
                {"id": "marx-c", "label": "Marx's capital C: £5,500 over a 55-week turnover, 100%",
                 "variable": 5500, "s_rate": 1, "working_weeks": 55, "circulation_weeks": 0,
                 "year_weeks": 50, "expect": {"tuTurnover": "55 weeks", "tuTurnovers": "10/11 a year (a 50-week year)", "tuAnnualRate": "10/11 = 90.91%", "tuMassS": "£5,000 a year"}},
                {"id": "b-at-a-pace", "label": "Capital B spent every 5 weeks: £1,000 a week",
                 "variable": 5000, "s_rate": 1, "working_weeks": 4, "circulation_weeks": 1,
                 "year_weeks": 50, "expect": {"tuTurnover": "5 weeks", "tuTurnovers": "10 a year (a 50-week year)", "tuAnnualRate": "10 = 1,000%", "tuMassS": "£50,000 a year"}},
            ],
            "panel_title": "The annual rate of surplus value",
            "panel_intro": (
                "The variable capital advanced, the rate of surplus value and the two periods "
                "go in. The lab computes the turnovers, the annual rate and the surplus value "
                "produced in the year. Compare capitals A and B: the third tile differs "
                "tenfold, the fourth not at all."
            ),
        }),
        "steps_title": "Computing the annual rate of surplus value",
        "steps_intro": "Four steps for any variable capital.",
        "steps": [
            ("Time the turnover",
             "Add the working and circulation periods for the turnover of the variable "
             "capital, and divide the year by it for n."),
            ("Compute the surplus value of the year",
             "Multiply the variable capital advanced by the real rate of surplus value and by "
             "n. This is the surplus value the year's labour produces."),
            ("Divide by the variable capital advanced",
             "The annual rate is the year's surplus value over the variable capital advanced, "
             "which is the real rate times n."),
            ("Compare with the real rate",
             "The annual rate exceeds the real rate when n is above 1, equals it at 1, and "
             "falls below it when the turnover is longer than a year."),
        ],
        "worked": {
            "title": "Capitals A and B",
            "intro": [
                "Both capitals pay £100 a week in wages at a rate of surplus value of 100% "
                "over a 50-week year. A advances £500 for a five-week turnover; B advances "
                "£5,000 for the whole year.",
            ],
            "lines": [
                "A: n = 50 / 5 = 10",
                "A: s = 100% · £500 · 10 = £5,000",
                "A: S′ = 5,000 / 500 = 1,000%",
                "B: n = 50 / 50 = 1",
                "B: s = 100% · £5,000 · 1 = £5,000",
                "B: S′ = 5,000 / 5,000 = 100%",
            ],
            "after": [
                "Same workers, same day, same real rate, same surplus value. The annual rates "
                "differ tenfold because B must advance ten times the money to keep the same "
                "labour employed.",
            ],
        },
        "quiz_title": "The annual rate of surplus value",
        "quiz": [
            {"q": "A variable capital of £400 turns over 5 times a year at a rate of surplus "
                  "value of 100%. What is the annual rate of surplus value?",
             "a": ["100%", "500%", "20%", "2,000%"],
             "c": 1,
             "why": "`S′ = s′·n = 100% · 5 = 500%`: £2,000 of surplus value on £400 advanced. "
                    "100% is the real rate, 20% divides by n, and 2,000% confuses the mass "
                    "£2,000 with a percentage."},
            {"q": "In the same case, what mass of surplus value is produced in the year?",
             "a": ["£400", "£2,000", "£500", "£80"],
             "c": 1,
             "why": "`100% · 400 · 5 = 2,000`. £400 is one turnover's surplus value, £500 is "
                    "the annual rate read as pounds, and £80 divides by the turnovers."},
            {"q": "Capital A has an annual rate of 1,000% and capital B of 100%, each with a "
                  "real rate of 100% and £100 of wages a week. Which statement is right on "
                  "Marx's account?",
             "a": ["A's workers are exploited ten times as hard",
                   "A and B produce the same surplus value; B must advance ten times the variable capital",
                   "B produces ten times A's surplus value",
                   "A's surplus value comes from circulation"],
             "c": 1,
             "why": "Both employ the same labour at the same real rate and produce £5,000; the "
                    "annual rates differ because B's £5,000 is advanced for a year and A's "
                    "£500 for five weeks. No one is exploited harder, and circulation creates "
                    "no surplus value."},
            {"q": "A variable capital of £2,000 has a turnover of 100 weeks in a 50-week year, at "
                  "a real rate of 100%. What is its annual rate?",
             "a": ["200%", "100%", "50%", "1/100"],
             "c": 2,
             "why": "`n = 50/100 = 1/2`, so `S′ = 100% · 1/2 = 50%`. 200% multiplies by the "
                    "turnover time in years; 100% is the real rate; `1/100` divides the year "
                    "into nothing meaningful."},
        ],
        "mistakes": [
            ("Thinking a capital that turns over faster exploits its workers harder",
             "Capital A shows 1,000% and capital B 100%, and in both the real rate typed into "
             "the lab is 100%: the same working day, half of it unpaid, and £5,000 of surplus "
             "value in each. The annual rate measures how little money had to be advanced, "
             "not how hard anyone worked."),
            ("Dividing the year's surplus value by the variable capital employed",
             "Over the year A employs £5,000 of variable capital, the same as B. Divided by "
             "that, both give 100%, the real rate. The annual rate divides by the capital "
             "advanced, £500 for A, which is what makes it `s′·n`."),
            ("Expecting the annual rate never to fall below the real rate",
             "Marx's capital C turns over in 55 weeks, so `n = 10/11` and its annual rate is "
             "`10/11`, below 100%. Any turnover longer than a year does this."),
        ],
        "standard": (
            "Finish when you can compute an annual rate of surplus value and tell it from the real rate.",
            "Given a variable capital, a rate of surplus value and working and circulation "
            "periods, compute the turnovers a year, the annual rate of surplus value and the "
            "mass of surplus value produced in the year, and compare two capitals with the "
            "same real rate."
        ),
        "note": (
            "The annual rate is a ratio to the money advanced, and the lab computes it at a "
            "real rate it is given; whether the real rate is a measure of anything is Volume "
            "I's question, not this chapter's. The same distinction returns, between the "
            "annual rate of profit and the rate per turnover, in Volume III. The figures for "
            "capitals A, B and C are Marx's."
        ),
    },
    # ---------------------------------------------------------------- 11
    # Kerr vol. 2, l. 3385 and l. 3395 (the passage: whence the money; 500
    # in, 600 out); l. 3290 (A pays its consumption from s, B in advance);
    # l. 3381 and l. 3393 (Tooke); l. 3418 (the problem itself does not
    # exist); l. 3426 (from nothing comes nothing); l. 3430 (the capitalist
    # class throws in the money); l. 3432-3434 (the farmer); l. 3350 (gold
    # producers); l. 3526 (accumulation: no new problem).
    {
        "slug": "the-circulation-of-surplus-value",
        "title": "The Circulation of Surplus Value",
        "module": "Chapter 17 · The Circulation of Surplus-Value",
        "one_line": "The money that turns the capitalists' surplus value into cash is money the capitalists themselves spend on their own consumption, thrown into circulation not as capital but as revenue.",
        "summary": (
            "If the capitalist class throws £500 into circulation as capital and takes £600 "
            "out, where did the other £100 come from? Compute the money a capitalist class "
            "must spend on its own consumption, ahead of its sales, for the surplus value in "
            "its product to return as money, and see what happens when it spends less."
        ),
        "key": [
            "capital thrown in: M",
            "commodities thrown in: M + s",
            "money for s: what the capitalists spend",
            "returned = M + consumption, up to M + s",
            "spent, not advanced",
        ],
        "key_label": "Where the money comes from",
        "concepts_intro": (
            "The chapter asks a question about money, not about value, and Marx is careful "
            "to keep the two apart."
        ),
        "concepts": [
            ("Realising surplus value",
             "Turning the surplus value contained in commodities into money by selling them. "
             "Surplus value is produced in production; it still has to be sold, and selling "
             "needs money in the buyers' hands."),
            ("Money spent and money advanced",
             "Money advanced as capital returns to its owner by the turnover. Money spent on "
             "consumption is gone, exchanged for goods that are eaten or worn. The money that "
             "realises surplus value is of the second kind."),
            ("The source of money itself",
             "In Marx's simplest case gold is produced at home, and the gold producers throw "
             "their wages, costs and surplus value into circulation directly as money. That "
             "is where new money enters; the capitalists' spending is how it reaches the "
             "surplus value."),
        ],
        "read_title": "Not where surplus value comes from, but its money",
        "read_intro": (
            "The passage states the question in Marx's own careful words, then in figures. "
            "The answer comes several pages later, after the wrong answers."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 17, §1.</strong> &ldquo;The question, then, is "
                  "not&mdash;where does the surplus-value come from? It is rather: Whence comes "
                  "the money for which it is exchanged? &hellip; The circulating capital of 500 "
                  "p. st. advanced in the form of money-capital, whatever may be its period of "
                  "turn-over, may now stand for the total capital of society, that is to say, of "
                  "the capitalist class. Let the surplus-value be 100 p. st. How can the entire "
                  "capitalist class manage to draw continually 600 p. st. out of the "
                  "circulation, when they continually throw only 500 p. st. into it?&rdquo;"),
            ("p", "The chapter begins from the last lesson. Capital A sells every five weeks and "
                  "can pay for its owner's household out of surplus value as it comes in. "
                  "Capital B sells once a year, so its owner must live for a year out of funds "
                  "advanced in some other way. Either way, before any surplus value can be "
                  "spent, it has to become money, and that raises the question in the "
                  "passage."),
            ("p", "Marx found it put to Thomas Tooke, the historian of prices and the leading "
                  "critic of the Currency School, by an opponent who asked how the capitalist "
                  "manages always to withdraw more money from circulation than he put in. Marx "
                  "thinks the question fair, and that it had not been answered: &ldquo;neither "
                  "Tooke nor any one else has answered it so far&rdquo;. Notice what is not in "
                  "question. Surplus value is produced in the workshop; the puzzle is only its "
                  "money."),
            ("p", "He disposes of four evasions first. That the same coins serve many "
                  "purchases one after another, which &ldquo;assumes that money as existing "
                  "whose existence it is called upon to explain&rdquo;; that one capitalist's "
                  "spending turns another's product into money, which only asks where the "
                  "spender got his; that wages flow back and can be used meanwhile; that money "
                  "spent on fixed capital stays out for years. None supplies the money it "
                  "presumes. Then he says the problem, as a special problem, does not "
                  "exist: the money needed to circulate commodities worth so much is the same "
                  "whether or not part of their value is surplus value. And yet in capitalist "
                  "society the capitalist is the starting point of the money in circulation, "
                  "wages included, so the question has a real form: &ldquo;From nothing comes "
                  "nothing. The capitalist class as a whole cannot draw out of circulation what "
                  "was not previously in it.&rdquo;"),
            ("p", "The answer:"),
            ("p", "<strong>Volume II, Chapter 17, §1.</strong> &ldquo;Indeed, paradoxical as it "
                  "may appear at first sight, it is the capitalist class itself that throws the "
                  "money into circulation which serves for the realization of the "
                  "surplus-value incorporated in the commodities. But, mark well, it is not "
                  "thrown into circulation as advanced money, not as capital. The capitalist "
                  "class spends it for their individual consumption.&rdquo;"),
            ("p", "Marx's farmer makes it concrete. In his first year he advances £5,000, £4,000 "
                  "for means of production and £1,000 for labour-power, and at a rate of 100% "
                  "the harvest is worth £6,000. He gets nothing back until the end of the year, "
                  "so he spends £1,000 from his own pocket on living. At the year's end he sells "
                  "for £6,000: £5,000 replaces his capital and £1,000 is his surplus value in "
                  "money, &ldquo;monetized with the money which he had himself thrown into "
                  "circulation, not as a capitalist, but as a consumer&rdquo;. From the second "
                  "year on, what he spends is last year's surplus value."),
            ("p", "And where did the money come from in the first place? Marx's simplest "
                  "assumption is a country that mines its own gold. Its gold producers throw "
                  "their wages, their costs and their surplus value into circulation directly "
                  "as money, newly made, replacing the coin worn out each year. Surplus value "
                  "elsewhere is &ldquo;thrown into circulation without the money required for "
                  "its monetization&rdquo;, and on the other side the gold producers' surplus "
                  "value arrives already as gold, without first being a product that has to "
                  "be sold."),
            ("p", "That covers simple reproduction, where the surplus value is all consumed. "
                  "For accumulation the second section says &ldquo;it does not offer any new "
                  "problem in matters of the circulation of money&rdquo;: the money is already "
                  "in the capitalists' hands as realised surplus value, and is thrown in as "
                  "capital instead of being spent as revenue; hoards and new gold do the rest. "
                  "Rosa Luxemburg, in "
                  "<em>The Accumulation of Capital</em> of 1913, thought this was exactly where "
                  "the problem was. If capitalists invest their surplus value instead of "
                  "consuming it, who buys the growing product, and with whose money? Her "
                  "answer was buyers outside capitalist production, peasants and colonies. Her "
                  "critics, Nikolai Bukharin among them, replied that the capitalists buy the "
                  "additional means of production from one another, as the reproduction schemes "
                  "of Part III show."),
            ("p", "The lab follows the money. The capitalist class throws in £500 as capital and "
                  "£100 as spending; its product is worth £600; all £600 returns and £100 of "
                  "surplus value is realised. Marx's farmer, at ten times the scale, gets back "
                  "£6,000 and realises £1,000. Then let the class spend only £50: only £550 of "
                  "money exists to buy a product worth £600, and only £50 of the surplus value "
                  "returns as money."),
            ("p", "Part II ends with the individual capital and its money. The next course, "
                  "Reproduction of the Social Capital, takes up the whole social capital at "
                  "once, and asks whether its two great departments can buy each other's "
                  "products year after year."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "realise",
            "money_unit": "£",
            "preset": "class",
            "presets": [
                {"id": "class", "label": "Marx's capitalist class: £500 as capital, £100 of surplus value",
                 "M": 500, "product": 600, "consumption_advance": 100, "expect": {"ciReturned": "£600", "ciS": "£100"}},
                {"id": "farmer", "label": "Marx's farmer: £5,000 advanced, £1,000 spent on living",
                 "M": 5000, "product": 6000, "consumption_advance": 1000, "expect": {"ciReturned": "£6,000", "ciS": "£1,000"}},
                {"id": "half-spent", "label": "The class spends only £50 ahead of its sales",
                 "M": 500, "product": 600, "consumption_advance": 50, "expect": {"ciReturned": "£550", "ciS": "£50"}},
            ],
            "panel_title": "The money that realises surplus value",
            "panel_intro": (
                "The money the capitalist class advances as capital, the value of its product "
                "and the money it spends on its own consumption go in. The lab counts all the "
                "money there is to buy the product and how much of the surplus value comes "
                "back as money. Try a smaller consumption and watch the second tile."
            ),
        }),
        "steps_title": "Following the money for surplus value",
        "steps_intro": "Four steps for a capitalist class, or one capitalist starting out.",
        "steps": [
            ("Count the money advanced as capital",
             "This returns by the turnover, and on its own it can buy back only commodities "
             "of the same value."),
            ("Count the value of the product",
             "The product is worth the capital plus the surplus value. The difference is what "
             "still needs money to be sold."),
            ("Add the money spent on consumption",
             "The capitalists' own spending, before or during the sale, is the additional "
             "money in circulation. It is spent, not advanced."),
            ("Compute what returns",
             "The money that returns is the capital plus the consumption spending, but never "
             "more than the product is worth. What returns beyond the capital is surplus "
             "value realised."),
        ],
        "worked": {
            "title": "Marx's farmer in his first year",
            "intro": [
                "A farmer advances £5,000 and, at a rate of surplus value of 100%, harvests a "
                "product worth £6,000. He receives nothing until the year's end and spends "
                "£1,000 on his household meanwhile.",
            ],
            "lines": [
                "thrown in as capital: £5,000",
                "thrown in as spending: £1,000",
                "product: £5,000 + £1,000 = £6,000",
                "returned: £6,000",
                "s realised: £6,000 − £5,000 = £1,000",
            ],
            "after": [
                "The £1,000 that realises his surplus value is the £1,000 he spent. From the "
                "second year on he spends last year's surplus value, and it flows back again "
                "at the end of each year.",
            ],
        },
        "quiz_title": "The circulation of surplus value",
        "quiz": [
            {"q": "A capitalist class advances £800 as capital, produces commodities worth "
                  "£1,000, and spends £200 on its own consumption. How much surplus value is "
                  "realised in money?",
             "a": ["£200", "£1,000", "£0", "£800"],
             "c": 0,
             "why": "£1,000 of money exists to buy the product, £800 replaces the capital and "
                    "£200 is surplus value realised. £1,000 is the product, £0 forgets the "
                    "spending, and £800 is the capital."},
            {"q": "The same class spends only £120 on consumption. How much surplus value is "
                  "realised in money?",
             "a": ["£200", "£120", "£80", "£920"],
             "c": 1,
             "why": "Only `800 + 120 = 920` of money is there to buy a £1,000 product, so £120 "
                    "of the surplus value returns as money. £200 is the surplus value produced, "
                    "£80 is what stays unsold, and £920 is the whole money returned."},
            {"q": "In what capacity does the capitalist class throw into circulation the money "
                  "that realises its surplus value, according to Marx?",
             "a": ["As capital advanced",
                   "As consumers spending revenue",
                   "As lenders at interest",
                   "As buyers of labour-power"],
             "c": 1,
             "why": "Marx's words: not as advanced money, not as capital, but spent for their "
                    "individual consumption. Money for labour-power is variable capital, and "
                    "the chapter assumes no credit."},
            {"q": "Whose objection holds that Marx's answer covers capitalists' consumption but "
                  "not accumulation?",
             "a": ["Thomas Tooke's", "Rosa Luxemburg's", "Adam Smith's", "David Ricardo's"],
             "c": 1,
             "why": "Luxemburg argued in 1913 that when capitalists invest rather than consume, "
                    "someone outside capitalist production must buy the growing product. Tooke "
                    "was the one the original question was put to; Smith and Ricardo wrote long "
                    "before the chapter."},
        ],
        "mistakes": [
            ("Thinking surplus value cannot be realised unless someone outside the capitalist class supplies the money",
             "The lab's class preset has no outsider at all: £500 thrown in as capital and "
             "£100 spent on consumption buy back a product worth £600, and £100 of surplus "
             "value returns as money. The money comes from the capitalists themselves, as "
             "spenders. Luxemburg's version of the objection, about accumulation, is a "
             "different question and is stated in the lesson."),
            ("Confusing the source of surplus value with the source of its money",
             "Marx says the question is not where surplus value comes from; that was "
             "settled in production. The question is only where the money to exchange it "
             "comes from."),
            ("Calling the consumption money an advance of capital",
             "The farmer's £1,000 does not come back as capital; it is spent and the goods "
             "it buys are consumed. What comes back at the year's end is the money form of "
             "his surplus value, which happens to be the same amount."),
        ],
        "standard": (
            "Finish when you can say where the money for surplus value comes from, with figures.",
            "Given the capital a capitalist class advances, the value of its product and its "
            "spending on its own consumption, compute the money returned and the surplus "
            "value realised in money, and say in what capacity that money was thrown into "
            "circulation."
        ),
        "note": (
            "The lab caps the money returned at the product's value and treats one round of "
            "spending and sale; it has no credit, no hoards and no gold mine. Its answer is "
            "Marx's for simple reproduction. Whether the same answer covers accumulation is "
            "the question Rosa Luxemburg reopened, and the lab cannot settle it. The £500, "
            "£100 and the farmer's figures are Marx's; the £50 is illustrative."
        ),
    },
]
