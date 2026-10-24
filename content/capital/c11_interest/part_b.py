"""Merchant's Capital and Interest, lessons 6-9 -- Volume III, Part V, Chapters 21-24.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals are left out, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Marx's formulas inside a quotation are printed as the Kerr text
prints them, with its dashes and its apostrophe for the prime (M—M'); the
lessons' own prose writes them M–M′. No quotation opens on a drop capital.
Nothing else is changed.

Chapter 24's opening passage is Richard Price's, quoted by Marx; the lesson
says so, and footnote 81 (l. 7579) gives Price's book and its date, 1772.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    # Kerr vol. 3, l. 3133 (a man having 100 p.st.; 5 p.st.; interest).
    # Inline: l. 3131 (capital as capital becomes a commodity), l. 3150
    # (M—M—C—M'—M'), l. 3198 (Proudhon), l. 3204 (the hatter), l. 3271
    # (the profit doubled), l. 3279 (an irrational expression; an absurd
    # contradiction).
    {
        "slug": "interest-bearing-capital",
        "title": "Interest-Bearing Capital",
        "module": "Chapter 21 · The Interest-Bearing Capital",
        "one_line": "A lender sells the use of money as capital, its power to produce the average profit, and interest is the part of that profit the borrower hands back.",
        "summary": (
            "Part V opens with the lender. What he hands over is not money as money but money "
            "as capital, a sum that can make the average profit in the borrower's hands, and "
            "interest is the share of that profit he takes back. Compute what Marx's £100 "
            "makes at 20 per cent, the interest paid out of it and the profit left to the "
            "borrower, at three rates of interest."
        ),
        "key": [
            "lent: money's use-value as capital",
            "profit = capital × average rate",
            "interest = a part of that profit",
            "£100 at 20%: £20; £5 interest, £15 kept",
            "M–M–C–M′–M′: lent, used, returned",
        ],
        "key_label": "Chapter 21 in five lines",
        "concepts_intro": (
            "The chapter asks what kind of commodity a loan is. Its answer depends on "
            "everything the course has built: a capital that yields the average profit."
        ),
        "concepts": [
            ("Capital as a commodity",
             "In capitalist production a sum of money can be turned into capital and yield "
             "the average profit. That power is a use-value of its own, and the lender sells "
             "it for a time."),
            ("Lending, not selling",
             "The lender gives up the money without receiving an equivalent and remains its "
             "owner. It comes back to him at the stated date, with an addition, because in "
             "the borrower's hands it really did function as capital."),
            ("Interest as a share of profit",
             "The borrower pays interest out of the profit the money made. It can only be a "
             "part of that profit: all of it, and the borrower gains nothing; none, and the "
             "lender has sold nothing."),
        ],
        "read_title": "Marx's £100, then the loan line by line",
        "read_intro": (
            "The example comes on the chapter's first page. Everything after it unpacks "
            "what was sold, and for what."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 21.</strong> &ldquo;In other words, a man "
                  "having 100 p.st. at his disposal, holds in his hand a power by which 100 "
                  "p.st. may be turned into 120 p.st., or by which a profit of 20% may be "
                  "produced. &hellip; If this man should pay, say 5 p.st. at the close of the "
                  "year to the owner of the 100 p.st., out of the produced profit, he would be "
                  "paying for the use-value of the 100 p.st., the use-value of its function as "
                  "capital, the function of producing 20 p.st. of profit. That part of the "
                  "profit, which he pays to the owner, is called interest.&rdquo;"),
            ("p", "You have met interest from both sides: on a savings account, where it is "
                  "paid to you, and on a loan or a mortgage, where you pay it. Newspapers call "
                  "the rate &ldquo;the price of money&rdquo;. Marx's chapter is an argument "
                  "that this everyday phrase hides what is being bought."),
            ("p", "Go through the passage. The man holds &ldquo;a power&rdquo;: in a society where "
                  "labour-power and means of production can be bought, £100 can be turned into "
                  "capital, and capital makes the average profit. That power is what makes the "
                  "sum worth borrowing. So, in Marx's phrase a page earlier, &ldquo;capital as "
                  "capital becomes a commodity.&rdquo; The man who lends the £100 for a year "
                  "&ldquo;gives him the power to produce a profit of 20%&rdquo;. And the £5 is "
                  "paid &ldquo;out of the produced profit&rdquo;: interest is not a second "
                  "source of income beside profit, it is a slice of the £20."),
            ("p", "The lab does the split. In the marx preset £100 at an average rate of 20 "
                  "per cent makes £20; at a rate of interest of 5 per cent, £5 goes to the "
                  "lender and £15 stays with the borrower. In the high-rate preset interest is "
                  "10 per cent and the £20 splits £10 and £10. In the low-rate preset it is 2 "
                  "per cent and the split is £2 and £18. The £20 does not move in any of them. "
                  "What the rate of interest decides is only who gets how much of it."),
            ("p", "Marx follows the money. The lender A hands it to the borrower B; B buys "
                  "means of production and labour-power, sells the product and gets back more; "
                  "then B hands the sum back to A with the interest. &ldquo;The movement, "
                  "then, is M—M—C—M'—M'.&rdquo; The doubled letters at each end are the "
                  "point. The first change of hands, A to B, is not a purchase or a sale. No "
                  "equivalent comes back, and A remains the owner. The last change of hands, B "
                  "to A, is a repayment. Between them the ordinary circuit of capital, "
                  "`M–C–M′`, runs in B's business, and from where A stands it is invisible."),
            ("p", "This is where Marx argues with Pierre-Joseph Proudhon, the French "
                  "socialist, whose 1850 debate with the economist Frédéric Bastiat he cites. "
                  "Proudhon thought lending at interest an injustice because it is not "
                  "selling: the lender has &ldquo;the faculty of always selling the same "
                  "article over and over, and of receiving its price again and again, without "
                  "ever relinquishing the ownership of the things one is selling&rdquo;. The "
                  "hatter who sells hats gets their value and no more, Proudhon said; the "
                  "lender gets more than he put in. Marx's reply is that the hatter gets more "
                  "too. Hats that cost 100 to make sell at their value of 115, and if the "
                  "capital was borrowed he may give up 5 of the 15 as interest. &ldquo;This "
                  "does not alter anything in the value of the hats, but only in the "
                  "distribution of the surplus-value already contained in this value between "
                  "different persons.&rdquo;"),
            ("p", "Why can the profit be divided at all? Because the same £100 is capital "
                  "twice, once in the lender's hands as a sum lent and once in the borrower's "
                  "as a sum at work, and it produces profit only once. &ldquo;The profit is "
                  "doubled by the double existence of the same sum of money as a capital for "
                  "two persons. It can serve as a capital for both of them only by dividing the "
                  "profit.&rdquo;"),
            ("p", "So is interest the price of money? Marx says the phrase is &ldquo;an "
                  "irrational expression&rdquo;. A price is the value of a thing expressed in "
                  "money. The £100 lent comes back as the same £100; it has a value, and the "
                  "interest is a second figure beside it that measures not its value but how "
                  "much profit it will yield. &ldquo;A price which is different in quality "
                  "from value is an absurd contradiction.&rdquo;"),
            ("p", "An opposing account came after Marx. Eugen von Böhm-Bawerk in "
                  "the 1880s and Irving Fisher in his 1930 <em>Theory of Interest</em> "
                  "explained interest as a genuine price: people value goods now more than the "
                  "same goods later, and time spent in roundabout production yields more, so "
                  "borrowers pay and lenders demand a premium for present over future money, "
                  "whatever the social system. On that account interest would exist even "
                  "without capitalists and profits. What in the chapter bears on it is the "
                  "claim that interest is a share of a profit produced by labour; the lab "
                  "computes the share and cannot decide between the two accounts."),
            ("p", "If interest is a share of profit, what sets the share? The next lesson, "
                  "“The Rate of Interest”, finds a ceiling and no floor."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "split",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: £100 at 20% profit, £5 interest",
                 "capital": 100, "profit_rate": "1/5", "interest_rate": "1/20",
                 "expect": {"inInterest": "£5", "inEnterprise": "£15"}},
                {"id": "high-rate", "label": "The same £100 with interest at 10%",
                 "capital": 100, "profit_rate": "1/5", "interest_rate": "1/10",
                 "expect": {"inInterest": "£10", "inEnterprise": "£10"}},
                {"id": "low-rate", "label": "The same £100 with interest at 2%",
                 "capital": 100, "profit_rate": "1/5", "interest_rate": "1/50",
                 "expect": {"inInterest": "£2", "inEnterprise": "£18"}},
            ],
            "panel_title": "Dividing the profit on a borrowed £100",
            "panel_intro": (
                "The capital employed, the average rate of profit and the rate of interest go "
                "in; all of the capital is borrowed. The lab computes the profit, the interest "
                "paid to the lender and what the borrower keeps. The first preset is Marx's; "
                "the two other rates of interest are illustrative."
            ),
        }),
        "steps_title": "Splitting the profit on borrowed capital",
        "steps_intro": "Four steps for any loan used as capital.",
        "steps": [
            ("Compute the profit",
             "Multiply the capital employed by the average rate of profit. This is what the "
             "money makes as capital, whoever owns it."),
            ("Compute the interest",
             "Multiply the sum borrowed by the rate of interest. It is paid out of the "
             "profit."),
            ("Subtract",
             "The borrower keeps the profit less the interest."),
            ("Check the share",
             "The interest should be a part of the profit, more than nothing and less than "
             "all of it. The sum lent comes back unchanged."),
        ],
        "worked": {
            "title": "Marx's lender and borrower",
            "intro": [
                "A lends B £100 for a year. The average rate of profit is 20 per cent and B "
                "pays £5 of interest. You want B's profit, the interest as a share of it and "
                "what B keeps.",
            ],
            "lines": [
                "profit:  £100 × 1/5 = £20",
                "interest:  £100 × 1/20 = £5",
                "kept by B:  £20 − £5 = £15",
                "interest's share:  5 / 20 = 1/4 of the profit",
                "returned to A:  £100 + £5 = £105",
            ],
            "after": [
                "A gets back his £100 and a quarter of what it made in B's hands. B keeps "
                "three-quarters. Nothing was bought or sold between them, and the £20 was made "
                "in B's business.",
            ],
        },
        "quiz_title": "What a lender sells",
        "quiz": [
            {"q": "A borrows £200 at 4% interest and uses it as capital at an average rate of "
                  "profit of 15%. What does the borrower keep after paying interest?",
             "a": ["£22", "£30", "£8", "£38"],
             "c": 0,
             "why": "Profit is `£200 × 15% = £30`, interest `£200 × 4% = £8`, and `£30 − "
                    "£8 = £22`. Thirty is the whole profit, 8 the interest, and 38 adds the "
                    "interest instead of subtracting it."},
            {"q": "On Marx's account, what does the lender give the borrower?",
             "a": ["The use of money as capital: its power to produce the average profit",
                   "Money in exchange for goods of equal value",
                   "A share of his labour-power",
                   "Ownership of the sum lent"],
             "c": 0,
             "why": "The lender sells the use-value of money as capital. No equivalent is "
                    "exchanged, so it is not a sale of money for goods; he supplies no labour; "
                    "and he remains the owner throughout."},
            {"q": "In Marx's reply to Proudhon, a hatter makes hats for 100 and sells them at "
                  "their value, 115, with borrowed capital, paying 5 of interest. What does "
                  "the interest change?",
             "a": ["Only the division of the 15 of surplus value",
                   "The value of the hats, which rises to 120",
                   "The hatter's cost, which rises to 105 and so raises the price",
                   "Nothing, because interest is paid from wages"],
             "c": 0,
             "why": "Marx says the interest &ldquo;does not alter anything in the value of the "
                    "hats&rdquo;, only the distribution of the surplus value in it. Proudhon "
                    "thought interest was added to the price; that is the view Marx is "
                    "rejecting, and it is paid from profit, not wages."},
            {"q": "Why, on Marx's account, can interest be neither zero nor the whole profit?",
             "a": ["Zero, the lender has sold nothing; the whole, the borrower gains nothing",
                   "The law fixes it between those limits",
                   "Zero would make money worthless; the whole would ruin the lender",
                   "Competition always sets it at half the profit"],
             "c": 0,
             "why": "If interest were the whole profit the borrower would have no reason to "
                    "borrow; if nothing, the lender would hand over the use of capital for "
                    "nothing. The text names no legal limit here, and no fixed half; the next "
                    "lesson finds no law at all for where it falls."},
        ],
        "mistakes": [
            ("Thinking interest is the price of money",
             "Everyday speech calls it that, and the money market reports it like a price. "
             "But the £100 lent comes back as the same £100, so its value has not been paid "
             "for; what is paid is a part of what it made. In the high-rate preset interest "
             "doubles to £10 and the £100 is still £100; only the split of the £20 changes, "
             "from £5 and £15 to £10 and £10. Marx calls the phrase &ldquo;an irrational "
             "expression&rdquo;."),
            ("Thinking the lender's money produces the interest",
             "It is the money's use in the borrower's business that produces profit. Kept as "
             "a hoard or spent on consumption, the £100 would make nothing; it is capital for "
             "the lender only because it is capital in the borrower's hands."),
            ("Thinking interest raises the value of what the borrower sells",
             "Proudhon thought interest was added to prices, so that workers could never "
             "buy back their product. In Marx's hatter example the hats are worth 115 whether "
             "the 15 stays with the hatter or 5 of it goes to a lender."),
        ],
        "standard": (
            "Finish when you can split the profit on borrowed capital.",
            "Given the capital employed, the sum borrowed, the average rate of profit and "
            "the rate of interest, compute the profit, the interest and the profit the "
            "borrower keeps, and state which of them the rate of interest changes."
        ),
        "note": (
            "The lab assumes the borrowed money is used as capital and makes exactly the "
            "average profit. Money borrowed for consumption, a loan that fails, or a profit "
            "above or below the average are outside it; Marx sets them aside too. Whether "
            "interest is a share of profit or the price of time is the question the split "
            "presupposes and cannot answer."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 3, l. 3349 (no "natural" rate of interest). Inline: l. 3305
    # (maximum and minimum), l. 3311 (Marx's 20%, 16%, 8% and 12%), l. 3323
    # (1842-1847), l. 3343 (Massie), l. 3345 (custom, legal tradition),
    # l. 3370 (the barometer), l. 3376 (a vanishing shape of mist).
    {
        "slug": "the-rate-of-interest",
        "title": "The Rate of Interest",
        "module": "Chapter 22 · Division of Profit. Rate of Interest. Natural Rate of Interest",
        "one_line": "The rate of interest normally lies between nothing and the rate of profit, and no law fixes where: there is no natural rate of interest.",
        "summary": (
            "Interest is a share of profit, so the rate of profit is its normal ceiling; it "
            "has no floor. Within those bounds Marx finds no law, only competition, custom "
            "and the state of trade. Compute interest and the profit left after it at "
            "several rates, check whether the rate lies inside its bounds, and see a crisis "
            "in which it does not."
        ),
        "key": [
            "normal bounds: 0 < i < p′",
            "ceiling: the rate of profit",
            "floor: none; it may fall to any depth",
            "enterprise = profit − interest",
            "crisis: interest can exceed profit",
        ],
        "key_label": "Chapter 22 in five lines",
        "concepts_intro": (
            "The chapter has a ceiling, a missing floor and a long argument that nothing "
            "between them is fixed by a law."
        ),
        "concepts": [
            ("The maximum",
             "Interest is paid out of profit, so its normal maximum is the whole profit, "
             "less what Marx reserves for wages of superintendence. Exceptionally it can be "
             "higher, and then it is not paid out of profit."),
            ("No minimum",
             "Nothing stops interest falling as far as the supply of loanable money and the "
             "demand for it take it. Counteracting circumstances lift it again, but no "
             "lower limit is defined."),
            ("No natural rate",
             "Where prices and wages have a level that supply and demand fluctuate around, "
             "the division of profit between lender and borrower has none. Competition and "
             "custom decide it; no deeper law does."),
        ],
        "read_title": "The conclusion first, then the bounds",
        "read_intro": (
            "The sentence comes halfway through the chapter, after Marx has set out the "
            "bounds of interest and the evidence of the money market. It gives the chapter "
            "its title."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 22.</strong> &ldquo;From what has gone before "
                  "it follows that there is no such thing as a &lsquo;natural&rsquo; rate of "
                  "interest.&rdquo;"),
            ("p", "Interest rates are news. A central bank raises or cuts its rate, mortgage "
                  "payments follow, and economists argue over where the rate ought to "
                  "be. Behind the argument is an idea Marx rejects: that there is a right level "
                  "the market rate tends toward, as the price of bread tends toward its cost of "
                  "production. The inner quotation marks around &lsquo;natural&rsquo; are the "
                  "translator's, and they are the whole point."),
            ("p", "Start with what can be said. Interest is a part of profit, so the profit "
                  "is its ceiling; at the ceiling the borrower keeps nothing. Marx adds an "
                  "exception at once: there are &ldquo;exceptional cases, in which interest "
                  "might be actually larger than profit and could not be paid out of "
                  "profit&rdquo;. The floor is another matter. &ldquo;The minimum limit of "
                  "interest is wholly undefinable. It may fall to any depth.&rdquo;"),
            ("p", "Marx's own figures show how the share and the rate move. If the rate of "
                  "profit is 20 per cent and interest a quarter of it, interest is 5 per cent; "
                  "at 16 per cent profit the same quarter is 4 per cent. But the quarter need "
                  "not hold: at 20 per cent profit interest might rise to 8 per cent and the "
                  "borrower would still keep 12, exactly what he kept at 16 and 4. The "
                  "borrower's profit after interest depends on two things that vary "
                  "separately."),
            ("p", "The lab computes the split and tests the bounds. In the normal preset, "
                  "Marx's 16 per cent profit and 4 per cent interest on £100, interest is £4, "
                  "£12 is left, and the bounds tile reads `0 < 4% < 16%`. In the plenty preset "
                  "profit is 20 per cent and interest only 1½ per cent, the rate Marx reports "
                  "for September 1843; the tile prints `£37/2`, which is £18½, as what is left, "
                  "the bounds tile writes the rate as `3/2%`, and the rate sits just above its missing "
                  "floor. In the crisis preset profit has fallen to 5 per cent and interest is "
                  "8 per cent, the level Marx says it passed in 1847: the borrower makes £5 "
                  "and owes £8, the tile shows profit of enterprise at minus £3, and the bounds "
                  "tile prints that the ceiling is breached. It is not an error. It is the "
                  "exceptional case, interest that &ldquo;could not be paid out of "
                  "profit&rdquo;."),
            ("p", "Those dates come from Marx's account of the trade cycle. Low interest "
                  "goes with prosperity, a rise with the turn, and a maximum &ldquo;up to a "
                  "point of extreme usury&rdquo; with the crisis, when money must be borrowed "
                  "to meet payments at any cost. The rate, which had been 4½ per cent in the "
                  "spring of 1842, &ldquo;fell to 2% in the spring and summer of 1843&rdquo;, "
                  "and then &ldquo;in September it fell even to 1½%&rdquo;, before rising to "
                  "8 per cent and more in 1847."),
            ("p", "Why no law within the bounds? For prices Marx has one: when supply and "
                  "demand balance, a commodity sells at its price of production, and the "
                  "balance reveals a level set by production itself. For interest a balance "
                  "between lenders and borrowers reveals nothing, because both sides are "
                  "dividing a single profit that the same capital produced once. The "
                  "eighteenth-century writer Joseph Massie, whom Marx credits with first seeing "
                  "that interest is part of profit, had said it: the division is settled by the "
                  "opinions of borrowers and lenders, for right and wrong in it &ldquo;are only "
                  "what common consent makes so.&rdquo; Marx adds: &ldquo;Custom, legal "
                  "tradition, etc., have as much to do with the determination of the average "
                  "rate of interest as competition itself&rdquo;."),
            ("p", "And yet the rate of interest looks far more solid than the rate of profit. "
                  "It is quoted daily, uniform for every borrower of the same standing, while "
                  "the general rate of profit is an average nobody sees. Marx's image: "
                  "&ldquo;Meteorological reports do not register the stand of the barometer "
                  "and thermometer more accurately than the reports of the Bourse do the stand "
                  "of the rate of interest&rdquo;. Beside it the general rate of profit "
                  "&ldquo;appears as a vanishing shape of mist&rdquo;. The thing without a "
                  "law looks fixed; the thing with one looks vague."),
            ("p", "The opposing view has a name and a date. The Swedish economist Knut "
                  "Wicksell, in <em>Interest and Prices</em> (1898), defined a natural rate "
                  "of interest: the rate at which the demand for loans matches the supply of "
                  "savings, close to the expected yield on new capital, with prices rising when "
                  "banks lend below it and falling when they lend above. Central banks today "
                  "estimate a neutral rate in the same spirit. What in the chapter bears on "
                  "it is the argument that nothing in the division of profit fixes such a "
                  "level; Wicksell's followers would answer that the level is fixed by saving "
                  "and investment, not by the division. The lab shows the bounds and cannot "
                  "settle that."),
            ("p", "Interest has bounds and no law. The next lesson, “Interest and Profit of "
                  "Enterprise”, asks why the part of profit left after interest comes to look "
                  "like a wage."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "bounds",
            "money_unit": "£",
            "preset": "normal",
            "presets": [
                {"id": "normal", "label": "Marx's figures: profit 16%, interest a quarter of it",
                 "capital": 100, "profit_rate": "4/25", "interest_rate": "1/25",
                 "expect": {"inEnterprise": "£12", "inBound": "0 < 4% < 16%"}},
                {"id": "plenty", "label": "Profit 20%, interest at 1½%",
                 "capital": 100, "profit_rate": "1/5", "interest_rate": "3/200",
                 "expect": {"inEnterprise": "£37/2", "inBound": "0 < 3/2% < 20%"}},
                {"id": "crisis", "label": "A crisis: profit falls to 5%, interest is 8%",
                 "capital": 100, "profit_rate": "1/20", "interest_rate": "2/25",
                 "expect": {"inInterest": "£8", "inEnterprise": "−£3",
                            "inBound": "breached: 8% ≥ 5%"}},
            ],
            "panel_title": "Interest between its bounds",
            "panel_intro": (
                "A borrowed capital of £100, the average rate of profit and the rate of "
                "interest go in. The tiles show the interest, the profit left after it and "
                "whether the rate of interest lies between nothing and the rate of profit. "
                "The 16 and 4 per cent are Marx's; the other presets pair rates he reports "
                "with illustrative rates of profit."
            ),
        }),
        "steps_title": "Placing a rate of interest",
        "steps_intro": "Four steps for any rate of interest and rate of profit.",
        "steps": [
            ("Compute the profit and the interest",
             "Multiply the capital by the rate of profit, and the sum borrowed by the rate of "
             "interest."),
            ("Subtract",
             "The profit left to the borrower is the profit less the interest. It may be "
             "negative."),
            ("Test the bounds",
             "Check that the rate of interest is above zero and below the rate of profit. "
             "Above the rate of profit, the interest is not paid out of this profit."),
            ("Name what decides the rest",
             "Within the bounds, the chapter offers no law for where the rate falls: "
             "competition between lenders and borrowers, custom and the phase of the trade "
             "cycle decide it."),
        ],
        "worked": {
            "title": "Marx's 20 and 8, beside 16 and 4",
            "intro": [
                "Marx compares a borrower at 20 per cent profit paying 8 per cent interest "
                "with one at 16 per cent profit paying 4 per cent. You want what each keeps "
                "on £100.",
            ],
            "lines": [
                "first:  £20 − £8 = £12",
                "second:  £16 − £4 = £12",
                "bounds, first:  0 < 8% < 20%",
                "bounds, second:  0 < 4% < 16%",
            ],
            "after": [
                "Both keep £12. The share of profit paid as interest is two-fifths in the "
                "first case and a quarter in the second, and nothing in the chapter says "
                "which a given year will bring.",
            ],
        },
        "quiz_title": "Bounds without a law",
        "quiz": [
            {"q": "The rate of profit is 18% and the rate of interest 6%. On a borrowed £100, "
                  "how much profit is left to the borrower?",
             "a": ["£12", "£18", "£6", "£24"],
             "c": 0,
             "why": "`£18 − £6 = £12`. Eighteen is the whole profit, 6 the interest, and 24 "
                    "adds them."},
            {"q": "Which rate of interest lies outside the normal bounds when the rate of "
                  "profit is 10%?",
             "a": ["12%", "9%", "1/2%", "5%"],
             "c": 0,
             "why": "The bounds are `0 < i < 10%`, and 12 per cent is above the rate of "
                    "profit, so the interest cannot be paid out of it. Nine, a half and five "
                    "per cent all lie between nothing and the rate of profit."},
            {"q": "What does Chapter 22 say about the minimum rate of interest?",
             "a": ["It is wholly undefinable and may fall to any depth",
                   "It is set by the wages of superintendence",
                   "It is a quarter of the rate of profit",
                   "It is the natural rate fixed by saving"],
             "c": 0,
             "why": "Those are Marx's words. The wages of superintendence enter his maximum, "
                    "not the minimum; the quarter is an assumption he uses for illustration "
                    "and then drops; and he denies any natural rate."},
            {"q": "On Marx's account, why does the rate of interest have no natural level "
                  "when prices of production do?",
             "a": ["Lenders and borrowers divide one profit, and their balance reveals no "
                   "level set by production",
                   "Interest is fixed by law in every country",
                   "Lenders always have more market power than borrowers",
                   "Money has no value, so it can have no natural price"],
             "c": 0,
             "why": "For commodities a balance of supply and demand reveals the price of "
                    "production; for interest it reveals nothing, because the same capital "
                    "produced the profit once and two parties divide it. Marx names custom and "
                    "legal tradition beside competition, but not law alone or one side's power, "
                    "and money in his account has a value."},
        ],
        "mistakes": [
            ("Thinking there is a natural rate of interest set by productivity",
             "Prices and wages have levels that supply and demand fluctuate around, so it is "
             "natural to expect interest to have one too, perhaps the yield of capital "
             "itself. Marx's answer is that the yield fixes only the ceiling. In the normal "
             "preset 4 per cent of a 16 per cent profit leaves £12, and Marx's 8 per cent of "
             "a 20 per cent profit leaves the same £12: the same borrower's result from two "
             "different divisions, and nothing in the chapter picks between them."),
            ("Treating a breach of the ceiling as impossible",
             "In the crisis preset interest of 8 per cent meets a profit of 5 per cent and the "
             "borrower ends £3 down. Marx expects exactly this at the height of a crisis, when "
             "money is borrowed to meet payments at any cost; the interest is then not paid "
             "out of profit."),
            ("Thinking the rate of profit is the more visible of the two",
             "The rate of interest is quoted daily and is the same for every borrower of "
             "the same standing; the general rate of profit is an average that no one "
             "observes. Marx's point is that the one without a law looks fixed."),
        ],
        "standard": (
            "Finish when you can place a rate of interest within its bounds.",
            "Given the rate of profit and the rate of interest on a borrowed capital, compute "
            "the interest and the profit left after it, and state whether the rate lies "
            "between zero and the rate of profit."
        ),
        "note": (
            "The bounds tile tests a rate against one rate of profit. It cannot show the "
            "trade cycle, the supply of loanable money or the customs Marx says fix the "
            "average; the 1843 and 1847 rates are the ones he reports, paired with "
            "illustrative rates of profit. Whether a natural rate in Wicksell's sense exists "
            "is the dispute this lesson names and does not decide."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 3, l. 3454 (wages of superintendence). Inline: l. 3411 (the
    # owner lends to himself), l. 3413 (quantitative into qualitative),
    # l. 3484 (the director of an orchestra), l. 3511 (walks the streets),
    # l. 3513 (ex-manufacturers), l. 3519 (co-operative factories), l. 3529
    # (nominal directors).
    {
        "slug": "interest-and-profit-of-enterprise",
        "title": "Interest and Profit of Enterprise",
        "module": "Chapter 23 · Interest and Profit of Enterprise",
        "one_line": "Once interest is a category, the rest of profit looks like a reward for work, but a hired manager's salary can be paid out of it and profit of enterprise is still left.",
        "summary": (
            "Every capitalist, borrowing or not, comes to split his profit into interest, the "
            "fruit of owning capital, and profit of enterprise, the fruit of using it, and the "
            "second looks like a wage for managing. Split £20 of profit into interest and "
            "profit of enterprise for an owner and a borrower, then pay a hired manager out "
            "of it, and see what is left that no work explains."
        ),
        "key": [
            "gross profit = interest + enterprise",
            "interest: the fruit of ownership",
            "enterprise: the fruit of function",
            "£20 − £5 interest = £15 enterprise",
            "a £6 manager leaves £9",
        ],
        "key_label": "Chapter 23 in five lines",
        "concepts_intro": (
            "The chapter explains how a division made for convenience between two people "
            "becomes two kinds of income that seem to have two sources."
        ),
        "concepts": [
            ("From quantity to quality",
             "When a borrower pays interest, the profit is split between two people. The "
             "split hardens into categories: interest belongs to capital as property, profit "
             "of enterprise to capital at work, and even an owner reckons both to himself."),
            ("Wages of superintendence",
             "Profit of enterprise is set against interest, not against wages, so the active "
             "capitalist comes to see it as the reward of his own labour of managing, a "
             "higher wage."),
            ("The manager's salary",
             "Managing has two sides: the coordination any combined labour needs, and the "
             "supervision that comes from the antagonism of owner and worker. Both can be "
             "hired, and once they are, the salary is visibly separate from profit."),
        ],
        "read_title": "The capitalist's idea, then where it comes from",
        "read_intro": (
            "The passage comes well into the chapter, once Marx has shown how interest "
            "became a category of its own. It describes what the active capitalist then "
            "believes about the rest of his profit."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 23.</strong> &ldquo;Under these circumstances "
                  "his brain necessarily conceives the idea, that his profit of enterprise, "
                  "far from being in opposition to wage-labor and representing only the unpaid "
                  "labor of others, is rather itself wages of labor, wages of superintendence "
                  "of labor.&rdquo;"),
            ("p", "Think of someone who owns and runs a small business. Her accountant tells "
                  "her to count a return on the money she has put in, what it would earn "
                  "lent out, and to count the rest as the reward for running the firm. It "
                  "seems the most natural division in the world. Chapter 23 asks where it "
                  "came from."),
            ("p", "It begins with borrowing. A capitalist who works with borrowed money must "
                  "pay interest, and what is left he regards as the product of his own "
                  "activity. Interest goes to a lender who does nothing in production; the "
                  "rest goes to the man who does. The quantitative split between two people "
                  "becomes a split between two sources, ownership and function. Then the "
                  "split spreads to everyone. &ldquo;The capitalist working with his own "
                  "capital divides the gross profit into interest due to himself as its owner "
                  "lending it to himself, and into profit of enterprise due to himself as an "
                  "active capitalist performing his function&rdquo;. In Marx's summary: "
                  "&ldquo;Thus a merely quantitative division turns into a qualitative "
                  "one.&rdquo;"),
            ("p", "Now the passage. Profit of enterprise is defined against interest, not "
                  "against wages, so the active capitalist sees it as the fruit of his work. "
                  "His &ldquo;brain necessarily conceives the idea&rdquo; that it is a wage, "
                  "higher than a labourer's, Marx goes on, because the labour is more "
                  "complicated and because he pays it to himself. What is forgotten, on "
                  "Marx's account, is that interest and profit of enterprise are both parts "
                  "of one surplus value, produced before any division."),
            ("p", "The lab splits £20 of profit on £100 at Marx's rates, 20 per cent profit "
                  "and 5 per cent interest. In the borrower preset all £100 is borrowed: £5 "
                  "interest, £15 profit of enterprise. In the owner preset nothing is borrowed, "
                  "so the lab, which books only interest actually paid, shows £0 of interest "
                  "and £20 of profit of enterprise. Marx's point is that the owner does not see "
                  "it that way: he reckons the £5 to himself as owner and the £15 to himself as "
                  "manager, just as the borrower's books show. The difference between the "
                  "presets is who receives the £5, not what it is."),
            ("p", "Is profit of enterprise a wage, then? Marx's test is to hire the work. "
                  "Coordinating a combined labour is a real function, like that of &ldquo;a "
                  "director of an orchestra&rdquo;, and any large business needs it. With "
                  "capitalist production, he writes, &ldquo;the labor of superintendence, "
                  "entirely separated from the ownership of capital, walks the streets&rdquo;: "
                  "it can be bought, like any skilled labour. In the manager preset the "
                  "borrower hires a manager for £6. Interest is still £5, and profit of "
                  "enterprise falls to £9. The work of management is now paid for, and £9 is "
                  "left that is paid for no work at all."),
            ("p", "Marx's evidence is from his own day. After every crisis, he notes, "
                  "&ldquo;one may see plenty of ex-manufacturers in the English factory "
                  "districts, who for low wages superintend their own former factories as "
                  "managers of the new owners, who are frequently their creditors.&rdquo; The "
                  "co-operative factories' accounts showed a profit after the manager's wages "
                  "were paid, and the joint-stock companies separated management from "
                  "ownership altogether. He allows himself one sharp remark about the boards of "
                  "directors who were paid by the meeting: such wages of superintendence, the "
                  "bankruptcy court showed, were inversely proportioned to the actual "
                  "superintendence performed."),
            ("p", "The superintendence also has a second side, and here Marx is "
                  "pointed. Where production rests on the antagonism of owner and "
                  "worker, supervision is needed to make people work, and it reaches its "
                  "maximum under slavery. He quotes Aristotle, who thought the master's "
                  "knowledge of commanding slaves nothing great and best left to an "
                  "overseer, and a New York lawyer of 1859 who justified slavery as "
                  "&ldquo;a just compensation for his master in return for the labor and "
                  "talents devoted to ruling him&rdquo;, words Marx then applies to the wage "
                  "of superintendence."),
            ("p", "Two later accounts of profit did not claim it was a manager's wage. Joseph Schumpeter in 1911 explained profit as the temporary reward of "
                  "the entrepreneur who innovates, and Frank Knight in 1921 as the return for "
                  "bearing uncertainty that cannot be insured. Both accept that a hired "
                  "manager's salary is not profit. What in the chapter bears on them is "
                  "limited: it does not discuss risk or innovation as sources of profit, and "
                  "argues that the residue after interest "
                  "and salary is part of surplus value. The lab computes the residue and cannot "
                  "say what it rewards."),
            ("p", "Interest now looks like the natural fruit of capital and profit of "
                  "enterprise like a wage. The next lesson, “Interest-Bearing Capital as a "
                  "Thing”, follows the first appearance to its extreme: money that seems to "
                  "grow by itself."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "split",
            "money_unit": "£",
            "preset": "borrower",
            "presets": [
                {"id": "owner", "label": "An owner who borrows nothing: no interest is paid out",
                 "capital": 100, "profit_rate": "1/5", "interest_rate": "1/20", "principal": 0,
                 "expect": {"inInterest": "£0", "inEnterprise": "£20"}},
                {"id": "borrower", "label": "Marx's figures: all £100 borrowed at 5%",
                 "capital": 100, "profit_rate": "1/5", "interest_rate": "1/20",
                 "expect": {"inInterest": "£5", "inEnterprise": "£15"}},
                {"id": "manager", "label": "The borrower hires a manager for £6",
                 "capital": 100, "profit_rate": "1/5", "interest_rate": "1/20", "manager_salary": 6,
                 "expect": {"inInterest": "£5", "inEnterprise": "£9"}},
            ],
            "panel_title": "Interest, profit of enterprise and a manager's salary",
            "panel_intro": (
                "The capital employed, the average rate of profit, the rate of interest, the "
                "sum borrowed and any hired manager's salary go in. The tiles show the "
                "interest paid out and the profit of enterprise left after interest and "
                "salary. The rates are Marx's; the £6 salary is illustrative."
            ),
        }),
        "steps_title": "Dividing gross profit",
        "steps_intro": "Four steps for any capital, borrowed or owned.",
        "steps": [
            ("Compute gross profit",
             "Multiply the capital employed by the average rate of profit."),
            ("Take out interest",
             "Multiply the sum borrowed by the rate of interest. For an owner, the same "
             "calculation on his own capital gives the interest he reckons to himself."),
            ("Take out any manager's salary",
             "A hired manager is paid out of what is left; his salary is a wage for "
             "skilled labour."),
            ("Name the residue",
             "What remains is profit of enterprise after the salary. On Marx's account it is "
             "paid for no labour, and is part of the surplus value like the interest."),
        ],
        "worked": {
            "title": "A borrower and his manager",
            "intro": [
                "A capitalist borrows £100 at 5 per cent and makes the average 20 per cent. "
                "He hires a manager for £6. You want the interest, the profit of enterprise "
                "before and after the salary.",
            ],
            "lines": [
                "gross profit:  £100 × 1/5 = £20",
                "interest:  £100 × 1/20 = £5",
                "before the salary:  £20 − £5 = £15",
                "after the salary:  £15 − £6 = £9",
            ],
            "after": [
                "If profit of enterprise were the wage of managing, the £6 would use it up. "
                "It leaves £9, which on Marx's account is surplus value, unpaid labour, and "
                "not the price of any work of superintendence.",
            ],
        },
        "quiz_title": "Ownership, function and wages",
        "quiz": [
            {"q": "Gross profit on £200 is 15% and the whole sum is borrowed at 5%. A manager "
                  "is paid £8. What profit of enterprise is left?",
             "a": ["£12", "£20", "£22", "£10"],
             "c": 0,
             "why": "Profit `£200 × 15% = £30`, interest `£200 × 5% = £10`, and `£30 − £10 − "
                    "£8 = £12`. Twenty forgets the manager, 22 forgets the interest, and 10 "
                    "is the interest itself."},
            {"q": "On Marx's account, how does a capitalist who uses only his own capital "
                  "treat his profit?",
             "a": ["He splits it into interest due to himself as owner and profit of "
                   "enterprise due to himself as active capitalist",
                   "He counts all of it as profit of enterprise",
                   "He counts all of it as interest",
                   "He counts all of it as wages of superintendence"],
             "c": 0,
             "why": "Marx says the owner lends his capital to himself, in effect, and divides "
                    "the profit just as a borrower does. The lab's owner preset books £0 of "
                    "interest because none is paid out; the qualitative split is in the "
                    "capitalist's reckoning."},
            {"q": "What does Marx take the existence of hired managers to show?",
             "a": ["That the labour of superintendence can be paid as a wage separate from "
                   "profit of enterprise",
                   "That managers produce the profit of enterprise",
                   "That interest is a wage for the lender",
                   "That co-operative factories cannot make a profit"],
             "c": 0,
             "why": "The labour of superintendence &ldquo;walks the streets&rdquo;: it is "
                    "bought like skilled labour, and profit is left after its salary. Marx "
                    "cites co-operative factories whose profit after the manager's wages was "
                    "above the average."},
            {"q": "Which of these does Chapter 23 describe as the first source of the "
                  "split into interest and profit of enterprise?",
             "a": ["Capitalists who work with borrowed capital and pay interest to lenders",
                   "Laws that set a maximum rate of interest",
                   "The wage bargain between capitalist and worker",
                   "The general rate of profit falling"],
             "c": 0,
             "why": "The division starts as a quantitative split between a lender and a "
                    "borrower and hardens into categories that every capitalist applies. Usury "
                    "laws, the wage bargain and the fall of the rate of profit are not what "
                    "the chapter traces it to."},
        ],
        "mistakes": [
            ("Thinking profit of enterprise is the capitalist's wage for managing",
             "Running a business is work, and the active capitalist sees profit of "
             "enterprise as its reward, which Marx says his brain &ldquo;necessarily "
             "conceives&rdquo;. Hire the work and the claim can be checked. In the manager "
             "preset a £6 salary pays for the managing, interest is still £5, and £9 of "
             "profit of enterprise is left over that pays for no work."),
            ("Thinking interest is earned only when money is actually lent",
             "In the owner preset no interest is paid out and the lab books £0. Marx's "
             "point is that the owner reckons the same £5 to himself as owner of capital; "
             "the borrower preset shows the division he has in mind."),
            ("Treating all supervision as productive coordination",
             "Marx grants that combined labour needs a conductor. He adds that supervision "
             "also arises from the antagonism of owner and worker, reaching its maximum "
             "under slavery, and that both sides are paid in the same salary."),
        ],
        "standard": (
            "Finish when you can split gross profit with a manager's salary.",
            "Given the capital, the sum borrowed, the average rate of profit, the rate of "
            "interest and a manager's salary, compute the interest, the profit of enterprise "
            "before and after the salary, and state which part pays for labour."
        ),
        "note": (
            "The lab books interest only on money actually borrowed, so its owner preset "
            "shows none; the owner's reckoning of interest to himself is in the prose. It "
            "treats the manager's salary as a fixed sum out of profit. Whether the residue "
            "rewards risk, innovation or ownership is the question the lesson names and the "
            "arithmetic cannot answer."
        ),
    },
    # ---------------------------------------------------------------- 09
    # Kerr vol. 3, l. 3561 (Price's penny, quoted by Marx; source in fn. 81,
    # l. 7579). Inline: l. 3533 (most fetish-like form), l. 3537 (the pear
    # tree), l. 3565 (the national debt), l. 3567 (dazzled), l. 3573 (Child),
    # l. 3590 (a qualitative limit).
    {
        "slug": "interest-bearing-capital-as-a-thing",
        "title": "Interest-Bearing Capital as a Thing",
        "module": "Chapter 24 · Externalisation of the Relations of Capital in the Form of Interest-Bearing Capital",
        "one_line": "Money at interest looks as if it grew by itself, and Price's penny shows where that leads: a sum no product of labour could ever pay.",
        "summary": (
            "In interest-bearing capital, money seems to make more money with nothing in "
            "between, as a pear tree bears pears. Compute Richard Price's penny at compound "
            "interest beside a capital that grows only as fast as the product, and Josiah "
            "Child's £100 beside it, and see why Marx calls the compound sum a fantasy: "
            "interest can only be a share of a surplus that labour produces."
        ),
        "key": [
            "M–M′: money making money",
            "compound sum = c · (1 + i)ⁿ",
            "a penny at 5% for 1,772 years: 37 digits",
            "grown with the product at 1%: 7 digits",
            "interest is a share of surplus value",
        ],
        "key_label": "Chapter 24 in five lines",
        "concepts_intro": (
            "The last chapter of the course is about an appearance, and about a man who "
            "took the appearance at its word."
        ),
        "concepts": [
            ("The fetish of M–M′",
             "In the merchant's `M–C–M′` there is at least a purchase and a sale between the "
             "two sums. In interest-bearing capital there is nothing: money returns as more "
             "money, and the growth seems a property of the money itself."),
            ("Price's compound interest",
             "Richard Price, an eighteenth-century minister and actuary, argued that a sum at "
             "compound interest grows beyond all imagination, and that a state could pay off "
             "any debt by letting a small fund accumulate. William Pitt built his sinking "
             "fund on the idea."),
            ("The limit",
             "Interest is a part of surplus value, and surplus value is limited by the "
             "working day, the productivity of labour and the number of workers. A sum "
             "that outgrows all of them cannot be paid."),
        ],
        "read_title": "Price's penny, then Marx's answer",
        "read_intro": (
            "The passage is not Marx's own. It is Richard Price, quoted by Marx from a "
            "pamphlet of 1772, and the chapter then explains why Price was wrong."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 24.</strong> &ldquo;A penny, loaned at the "
                  "birth of our Savior at compound interest at 5%, would already have grown "
                  "into a larger amount than would be contained in 150 million globes, all of "
                  "solid gold. But loaned at simple interest, it would have grown only to 7 "
                  "sh. 4½ d. in the same time.&rdquo;"),
            ("p", "These are Richard Price's words, from <em>An Appeal to the Public on the "
                  "Subject of the National Debt</em>, whose second edition Marx dates to 1772. "
                  "You have probably seen their descendants: the savings advertisement with a "
                  "curve that bends upward forever, the calculator that shows what a small sum "
                  "becomes if you start young. Compound interest is real arithmetic. Marx's "
                  "chapter asks what has to be true outside the arithmetic for it to be "
                  "paid."),
            ("p", "First, the appearance. In interest-bearing capital, Marx writes, "
                  "&ldquo;the relations of capital assume their most externalised and most "
                  "fetish-like form&rdquo;. Money is lent and money returns, more of it, and "
                  "nothing visible happens in between. The merchant at least bought and sold; "
                  "the lender just waits. So the increase looks like a property of the money: "
                  "&ldquo;It becomes a faculty of money to generate value and yield interest, "
                  "just as it is a faculty of a pear tree to bear pears.&rdquo; Everything this "
                  "course has computed, the industrial profit, the merchant's share, the "
                  "interest carved out of the average, has disappeared from view."),
            ("p", "Then Price, who took the pear tree literally. Marx says he &ldquo;was "
                  "simply dazzled by the enormousness of the figures arising from geometrical "
                  "progression&rdquo;, and that he treated capital as a number increasing "
                  "itself, by the formula `s = c·(1 + i)ⁿ`. Pitt believed him, and his "
                  "sinking-fund Act set aside £250,000 a year to accumulate at compound "
                  "interest until the fund should reach £4,000,000 a year and pay off the "
                  "national debt. Price went further in a later book: a "
                  "shilling at 6 per cent from the same date would fill a globe the size of "
                  "Saturn's orbit, and a state with the smallest savings could pay the largest "
                  "debt. Marx's comment is one line: &ldquo;What a pretty theoretical "
                  "introduction to the national debt of England!&rdquo;"),
            ("p", "The lab computes Price's sum exactly. In the price preset a penny is put "
                  "out at 5 per cent for 1,772 years, from the year Price counts from to the "
                  "year of his pamphlet. The exact sum is too long to print, so the tile gives "
                  "its form and its size: 37 digits before the point, in shillings. Beside it, "
                  "the same penny grown at 1 per cent a year, a rate an economy can sustain "
                  "for a long time, has 7 digits. The first figure is what the claim would "
                  "be; the second is a generous guess at what a product growing for 1,772 "
                  "years might be able to pay. The gap is thirty orders of magnitude."),
            ("p", "Marx also cites Josiah Child, the seventeenth-century merchant and writer "
                  "on trade, who said that &ldquo;100 pounds sterling at 10% will produce in 70 "
                  "years by compound interest 102,400 pounds sterling&rdquo;. The child preset "
                  "runs it, in shillings: 2,000s, which is £100, at 10 per cent for 70 years "
                  "has 7 digits before the point, about £78,975 compounded yearly. Child's "
                  "102,400 is £100 doubled ten times, as if it doubled every seven years; "
                  "the exact yearly figure is smaller. A product growing at 2 per cent turns "
                  "the same £100 into about £400, 4 digits in shillings. In the ten-years preset the horizon is "
                  "ordinary: £100 at 5 per cent for ten years against a capital that also "
                  "grows 5 per cent a year. The two tiles print the same exact sum, about "
                  "£162 17s 9½d. A loan at 5 per cent compound can be paid in full as long as "
                  "the capital it is lent to grows at 5 per cent. Marx's footnote on Price "
                  "puts the condition from the profit side: in his example an industrial "
                  "capitalist who pays 5 per cent interest, spends 5 and capitalises 5 needs "
                  "a profit of 15 per cent, and Price forgets that the 5 presupposes the "
                  "15."),
            ("p", "<strong>Volume III, Chapter 24.</strong> &ldquo;By the identity of "
                  "surplus-value with surplus-labor a qualitative limit is imposed upon the "
                  "accumulation of capital.&rdquo;"),
            ("p", "That is Marx's answer. Accumulation can be described as compound "
                  "interest, he grants, if the profit reinvested is called interest. But two "
                  "things stop it compounding forever. Existing capital is continually "
                  "devalued, because commodities are worth the time needed to reproduce them "
                  "and that time keeps falling. And the rate of profit falls as accumulation "
                  "raises the composition of capital, the law of Average Profit and Its Fall. "
                  "Behind both is the limit in the passage: surplus value is surplus labour, "
                  "and the working day, the productivity of labour and the number of workers "
                  "bound it. Treated as mere interest, surplus value has only a quantitative "
                  "limit, and that one &ldquo;defies all fantasy&rdquo;."),
            ("p", "The modern version of the argument is about shares rather than "
                  "impossibilities. Thomas Piketty's <em>Capital in the Twenty-First "
                  "Century</em> (2013) argued that when the return on wealth exceeds the "
                  "growth of output for long periods, the share of income going to wealth "
                  "rises, and that wars, inflation and taxes have repeatedly cut accumulated "
                  "fortunes down. It is a claim about shares, not Price's claim, and what in the chapter "
                  "bears on it is the limit in the passage: a share of a product can grow "
                  "only toward the whole product. Critics of "
                  "Piketty, Marxist and mainstream, dispute how long the return can stay "
                  "above growth. The lab's two tiles show the size of the gap and nothing "
                  "about how long it can last."),
            ("p", "Interest has turned out to be a share of profit with no natural rate, and "
                  "capital lent at interest looks like a thing that grows by itself. The next "
                  "course, Credit and Fictitious Capital, follows interest-bearing capital "
                  "into the banks and the credit system, where claims on future income are "
                  "bought and sold as if they were capital themselves."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "compound",
            "money_unit": "s",
            "preset": "price",
            "presets": [
                {"id": "price", "label": "Price's penny at 5% for 1,772 years, beside growth at 1%",
                 "principal": "1/12", "interest_rate": "1/20", "years": 1772, "real_growth": "1/100",
                 "expect": {"inCompound": "1d × (21/20)^1772: 37 digits before the point, in shillings",
                            "inReal": "1d × (101/100)^1772: 7 digits before the point, in shillings"}},
                {"id": "child", "label": "Child's £100 (2,000s) at 10% for 70 years, beside growth at 2%",
                 "principal": 2000, "interest_rate": "1/10", "years": 70, "real_growth": "1/50",
                 "expect": {"inCompound": "2,000s × (11/10)^70: 7 digits before the point, in shillings",
                            "inReal": "2,000s × (51/50)^70: 4 digits before the point, in shillings"}},
                {"id": "ten-years", "label": "£100 (2,000s) at 5% for ten years, with the capital growing 5%",
                 "principal": 2000, "interest_rate": "1/20", "years": 10, "real_growth": "1/20",
                 "expect": {"inCompound": "2,000s × (21/20)^10 = 3,257s 9 602934603/1280000000 d",
                            "inReal": "2,000s × (21/20)^10 = 3,257s 9 602934603/1280000000 d"}},
            ],
            "panel_title": "Compound interest against a growing product",
            "panel_intro": (
                "A sum in shillings, a rate of interest, a number of years and a rate at which "
                "a real product grows go in. The first tile compounds the sum at the rate of "
                "interest, the second at the rate of real growth; each prints the exact sum "
                "when it is short, and otherwise the number of digits before the point. The "
                "rates of real growth are illustrative."
            ),
        }),
        "steps_title": "Testing a compound claim",
        "steps_intro": "Four steps for any sum left at compound interest.",
        "steps": [
            ("Compound the claim",
             "Multiply the sum by one plus the rate of interest, raised to the number of "
             "years: `c·(1 + i)ⁿ`."),
            ("Compound the product",
             "Do the same at the rate at which the real product, from which interest must be "
             "paid, can grow."),
            ("Compare the sizes",
             "Where the sums are too large to print, compare their numbers of digits. Each "
             "digit is a factor of ten."),
            ("Name the source",
             "Interest is paid out of profit, profit out of surplus value, and surplus value "
             "out of surplus labour. A claim that outgrows the product cannot be paid in "
             "full."),
        ],
        "worked": {
            "title": "Child's £100 at 10 per cent",
            "intro": [
                "Josiah Child said £100 at 10 per cent would become 102,400 pounds in 70 years. "
                "You want the exact yearly compound sum and the same £100 grown at 2 per cent.",
            ],
            "lines": [
                "claim:  £100 · (11/10)^70 ≈ £78,975",
                "Child's figure:  £100 · 2^10 = £102,400",
                "product at 2%:  £100 · (51/50)^70 ≈ £400",
                "ratio:  78,975 / 400 ≈ 197",
            ],
            "after": [
                "Over seventy years the claim is about two hundred times what a product growing "
                "at 2 per cent could become. Over Price's 1,772 years the ratio has thirty "
                "digits.",
            ],
        },
        "quiz_title": "Money that seems to grow by itself",
        "quiz": [
            {"q": "£100 is left at 10% compound interest for 2 years. What does it become?",
             "a": ["£121", "£120", "£110", "£200"],
             "c": 0,
             "why": "`£100 · (11/10)² = £121`. £120 is simple interest, £110 is one year, and "
                    "£200 doubles it."},
            {"q": "On Marx's account, what puts a qualitative limit on the accumulation of "
                  "capital?",
             "a": ["The identity of surplus value with surplus labour, bounded by the working "
                   "day and the number of workers",
                   "The rate of interest set by the Bank",
                   "The size of the national debt",
                   "The amount of gold in the world"],
             "c": 0,
             "why": "Marx's sentence names the identity of surplus value with surplus labour, "
                    "and he adds the working day, productivity and population. The other "
                    "three are not his limit; gold, in particular, is what Price's globes are "
                    "made of, not what bounds accumulation."},
            {"q": "What does Marx's image of the pear tree describe?",
             "a": ["The appearance that money yields interest by its own nature",
                   "The real growth of capital through production",
                   "The merchant's profit from buying and selling",
                   "The growth of the working population"],
             "c": 0,
             "why": "In `M–M′` the yield seems &ldquo;a faculty of money&rdquo;, as bearing "
                    "pears is of a pear tree. Marx calls this the most fetish-like form; the "
                    "real growth comes from production, which the image hides."},
            {"q": "In the ten-years preset, £100 at 5% compound and a capital growing at 5% "
                  "give the same sum. What does that show on the chapter's account?",
             "a": ["Compound interest can be paid while the capital it is lent to grows as "
                   "fast",
                   "Money grows at 5% by itself",
                   "Price's penny could also be paid",
                   "Interest and profit are always equal"],
             "c": 0,
             "why": "The claim is paid out of a growth that matches it. Nothing grows by "
                    "itself, Price's penny outgrows any such growth, and Marx's footnote has "
                    "5 per cent interest presupposing a 15 per cent profit, not an equal one."},
        ],
        "mistakes": [
            ("Thinking money left at interest grows by itself",
             "Interest is paid regularly, and on a statement it looks like the money's own "
             "growth. Marx's chapter says that appearance is the fetish. In the price preset "
             "the penny at 5 per cent for 1,772 years has 37 digits in shillings, while the "
             "same penny grown with a product at 1 per cent has 7. The first could be paid "
             "only out of a surplus that no working day could produce."),
            ("Thinking compound interest arithmetic is wrong",
             "Price's arithmetic is right, and the lab computes it exactly. What Marx denies "
             "is that the sum describes anything that could be paid, because interest is a "
             "share of surplus value."),
            ("Reading Price's sinking fund as a way to abolish debt",
             "Pitt's fund set aside taxes to accumulate at compound interest, and the "
             "interest it earned was paid by the state on its own debt. Marx calls Price's "
             "promise a pretty introduction to the national debt."),
        ],
        "standard": (
            "Finish when you can compare a compound claim with the growth of a product.",
            "Given a sum, a rate of interest, a number of years and a rate of real growth, "
            "compute the compound sum and the sum grown with the product, compare their "
            "sizes, and state from what the interest would have to be paid."
        ),
        "note": (
            "“Compound Interest and Continuous Growth” on the Algebra path computes the same "
            "sum; what is new here is the second tile, the product it must be paid from. The "
            "rates of real growth are illustrative, and 1,772 years is the span from the date "
            "Price counts from to his pamphlet. How long a return on wealth can outrun growth "
            "is an empirical question the lab does not carry."
        ),
    },
]
