"""Cost Price and the Rate of Profit, lessons 5-7 -- Volume III, Chapters 5-7, one lesson per chapter.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, and the translator's double quotation marks inside a quotation
are printed as single curly quotes. Formulas inside a quotation are printed as
the Kerr text prints them (s/(c+v)). A quotation that begins mid-sentence keeps
the case of the text. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Kerr vol. 3, l. 1143 (such economies are); l. 1088 (s given). Inline:
    # l. 1074 (one week into one and a half), l. 1104 (the division of social
    # labour), l. 1143 (prodigal with human life), l. 1157 (the 1829 mines
    # report), l. 1159 (15 men a week), l. 1167 (Glasgow; killing is no
    # murder), l. 1184 (263 in Manchester), l. 1246 (rags 4 p.st. 4 sh. to
    # 44 p.st.), l. 1272 (the second-hand owners).
    {
        "slug": "economy-in-constant-capital",
        "title": "Economy in the Use of Constant Capital",
        "module": "Chapter 5 · Economies in the Employment of Constant Capital",
        "one_line": "With the surplus value given, the rate of profit rises only if the constant capital is cheapened, and some of the cheapening is paid for with the workers' health.",
        "summary": (
            "Chapter 5 holds s and v fixed and asks how the rate of profit can still rise: only "
            "by spending less on c. Compute the new rate when a shared building, reused waste or "
            "a ventilation shaft never dug cuts the constant capital. The arithmetic is the "
            "same in each case, and the chapter is about why that sameness matters."
        ),
        "key": [
            "s and v fixed: p′ rises only if c falls",
            "p′ = s / (c − saving + v)",
            "c → 0 would make p′ = s′",
            "savings in scale come from social labour",
            "some savings are paid for in health",
        ],
        "key_label": "The fifth chapter in five lines",
        "concepts_intro": (
            "Chapter 5 is long and mostly evidence: factory inspectors, engineers, medical "
            "reports. The argument underneath it has three parts."
        ),
        "concepts": [
            ("Economy in c",
             "With s and v given, the rate of profit `s/(c + v)` can rise only if c falls. Every "
             "saving on buildings, power, materials or waste raises it, however the saving was "
             "made."),
            ("Savings that come from social labour",
             "Most economies arise from many workers combined on a large scale, or from "
             "cheaper machines and materials made by labour in other industries. The capitalist "
             "takes them as the fruit of his own management."),
            ("Savings at the workers' expense",
             "Crowded rooms, unguarded machinery, unventilated mines are also savings in c. They "
             "raise the rate of profit by exactly the same arithmetic, and the workers pay for "
             "them in health and lives."),
        ],
        "read_title": "The list of savings first, then the rule behind them",
        "read_intro": (
            "The passage closes the chapter's general section, just before the evidence begins. "
            "The rule that makes those savings profitable comes earlier in the chapter and "
            "second here."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 5, §1.</strong> &ldquo;Such economies are: The "
                  "overcrowding of narrow and unsanitary rooms with laborers, or, in the language "
                  "of the capitalist, a saving in buildings; a crowding of dangerous machinery "
                  "into one and the same room without means of protection against this danger; "
                  "a neglect of precautions in productive processes which are dangerous to health "
                  "or life, such as mining, etc.&rdquo;"),
            ("p", "The phrase that carries the chapter is &ldquo;in the language of the "
                  "capitalist, a saving in buildings&rdquo;. The same entry in the books, less spent on c, can "
                  "be a better engine or a room too small to breathe in. Marx's claim is that the "
                  "rate of profit cannot tell the two apart, and so the drive to raise it reaches "
                  "for both. The chapter's second section, on the coal mines and the factories, "
                  "is headed &ldquo;Economies in the conditions of labor at the expense of the "
                  "laborers&rdquo;."),
            ("p", "<strong>Volume III, Chapter 5, §1.</strong> &ldquo;If the surplus-value is "
                  "given, then the rate of profit can be increased only by a reduction of the "
                  "value of the constant capital required for the production of commodities.&rdquo;"),
            ("p", "That is the rule, and it is Chapter 3's third case put to work: s and v fixed, "
                  "c moving. The lab cuts c and recomputes. On Marx's familiar `400c + 100v + 100s` "
                  "the rate is 20%. The shared-building preset cuts c by £100, as when one engine "
                  "and one roof serve a larger workforce: the rate rises to 25% and the cost price "
                  "falls to £400. The waste-reuse preset cuts it by £40: `100/460 = 5/23`, about "
                  "21.7%. The unsafe preset cuts it by £20, the guard rails and ventilation not "
                  "bought: `100/480 = 5/24`, about 20.8%. If c could fall to nothing the rate of "
                  "profit would equal the rate of surplus value, which is why, Marx notes, it is "
                  "the upper limit."),
            ("p", "Where do the savings come from? First, from the working day. A longer day "
                  "uses the same buildings and machines for more hours: if the hands work 18 hours "
                  "instead of 12, &ldquo;one week is stretched into one and a half&rdquo;, and the "
                  "machinery's value comes back in two-thirds of the time. Second, from scale: one "
                  "central engine costs less than many small ones, a building shared costs less "
                  "per worker. Third, from other industries. When cotton, iron or machines are "
                  "made more cheaply elsewhere, the spinner's c falls and his rate rises. "
                  "&ldquo;The capitalist thus appropriates the advantages of the entire system of "
                  "the division of social labor.&rdquo;"),
            ("p", "Fourth, from what used to be thrown away. Woollen rags were worth about £4 4s "
                  "a ton some thirty years before 1863 and as much as £44 a ton a few years before "
                  "it, because the shoddy trade had learned to remake them into cloth; the "
                  "chemical industry turned gas-tar into aniline dyes. Fifth, from inventions, and "
                  "here Marx is at his driest: the first firms to use a new invention usually go "
                  "bankrupt, and the buildings and machines are bought cheaply by successors, so "
                  "that &ldquo;the most worthless and miserable sort of money-capitalists&rdquo; "
                  "draw the greatest benefit from the work of science."),
            ("p", "Then the evidence for the savings at the workers' expense. Around 1860, fatal "
                  "accidents in English collieries averaged 15 men a week; many mines had a single "
                  "shaft, so no ventilation and no escape. In the factories, manufacturers resisted "
                  "the law requiring guards on horizontal shafts, and in 1854 formed a National "
                  "Association that raised, in 1855, more than £50,000, at 2s per horse-power, to fight the "
                  "factory inspectors in court. A Glasgow firm guarded all its machinery with old "
                  "iron for £9 1s; its subscription to the Association, on 110 horse-power, would "
                  "have been £11. Marx's verdict on the Association's purpose: &ldquo;The issue was "
                  "to prove that killing is no murder when done for profit.&rdquo; The medical "
                  "reports he quotes put deaths from lung disease among men of 15 to 55 at 263 in "
                  "Manchester for every 100 in the farming districts."),
            ("p", "Marx's summary is that capitalist production, however sparing it is with "
                  "materials, &ldquo;is utterly prodigal with human life&rdquo;. A standing "
                  "objection to it is older than the chapter. Adam Smith argued that wages vary with "
                  "the hardship and danger of a trade, so that dangerous work is paid "
                  "a premium and the risk is priced, not simply imposed; later economists built "
                  "the theory of compensating wage differentials on that idea. The chapter does "
                  "not take up Smith. The evidence it sets against the idea is the 1829 report "
                  "it quotes, in which miners, &ldquo;whose numbers generally exceed the "
                  "demand&rdquo;, accept danger &ldquo;for a wage which is little above that of "
                  "the day laborers&rdquo; nearby. Whether risk is priced in a given labour "
                  "market is an empirical question the lab cannot answer."),
            ("p", "The rule assumed the prices of c's elements were given and only the quantity "
                  "used was cut. The next lesson, “Price Fluctuations of Raw Materials”, keeps "
                  "the quantities and lets the price of the raw material move."),
        ],
        "lab": ("capkit", {
            "mode": "profit",
            "view": "economy",
            "money_unit": "£",
            "preset": "shared-building",
            "presets": [
                {"id": "shared-building", "label": "400c + 100v + 100s; one engine and one building save £100 of c",
                 "c": 400, "v": 100, "s": 100, "c_change": -100, "expect": {"prRate": "1/4 = 25%", "prCost": "£400"}},
                {"id": "waste-reuse", "label": "The same capital; reused waste saves £40 of c",
                 "c": 400, "v": 100, "s": 100, "c_change": -40, "expect": {"prRate": "5/23 = 21.74%", "prCost": "£460"}},
                {"id": "unsafe", "label": "The same capital; guards and ventilation not bought, £20 of c",
                 "c": 400, "v": 100, "s": 100, "c_change": -20, "expect": {"prRate": "5/24 = 20.83%", "prCost": "£480"}},
            ],
            "panel_title": "A saving in constant capital",
            "panel_intro": (
                "c, v and s go in, with the change in c. The tiles give the rate of profit and "
                "the cost price after the change; the banner gives the rate before and after. "
                "Compare the three presets: each raises the rate, and nothing in the figures "
                "says how the saving was made."
            ),
        }),
        "steps_title": "Computing the effect of a saving in c",
        "steps_intro": "Four steps, with s and v held fixed throughout.",
        "steps": [
            ("Compute the rate before",
             "The rate of profit is `s/(c + v)` on the capital as it stands."),
            ("Apply the saving",
             "Subtract the saving from c. Leave v and s unchanged; a saving that changed the "
             "workforce or the working day is a different case."),
            ("Compute the rate after",
             "Divide the same s by the smaller capital. The rise in the rate is the whole "
             "effect; the mass of profit is unchanged."),
            ("Classify the saving",
             "Say whether it came from scale, from cheaper inputs made elsewhere, from reused "
             "waste, or from the conditions of work."),
        ],
        "worked": {
            "title": "Cutting £100 from the constant capital",
            "intro": [
                "Marx's capital `400c + 100v + 100s` saves £100 on its constant capital. You "
                "want the rate of profit before and after.",
            ],
            "lines": [
                "before:  p′ = 100 / (400 + 100) = 1/5 = 20%",
                "after:  c = 400 − 100 = 300",
                "after:  p′ = 100 / (300 + 100) = 1/4 = 25%",
                "mass of profit:  £100 before and after",
            ],
            "after": [
                "The rate rises by a quarter, from 20% to 25%, and not a penny more surplus value "
                "is produced. The same calculation would follow from a better engine or from a "
                "room without ventilation.",
            ],
        },
        "quiz_title": "Where a saving comes from",
        "quiz": [
            {"q": "A capital of 300c + 100v + 50s saves £100 on its constant capital, with v and s "
                  "unchanged. What happens to the rate of profit?",
             "a": ["It rises from 12.5% to 16.67%",
                   "It stays at 50%",
                   "It rises from 16.67% to 25%",
                   "It falls, because less is invested"],
             "c": 0,
             "why": "`50/400 = 1/8` before and `50/300 = 1/6` after. 50% is s′, which is "
                    "unchanged; the third option divides by c alone; and a smaller capital with "
                    "the same surplus earns a higher rate, not a lower one."},
            {"q": "On the chapter's account, what is the upper limit to the rate of profit as c "
                  "is cut, with s and v given?",
             "a": ["100%", "The rate of surplus value s′", "Twice the original rate", "There is none"],
             "c": 1,
             "why": "With c at zero, `p′ = s/v = s′`. 100% is s′ only when s equals v, the "
                    "doubling has no basis, and the limit exists because v and s stay fixed."},
            {"q": "Cheaper cotton raises a spinner's rate of profit. Where, on Marx's account, "
                  "did the gain originate?",
             "a": ["In the spinner's own management",
                   "In higher productivity of labour in cotton growing and transport",
                   "In a higher rate of surplus value in the spinnery",
                   "In selling the yarn above its value"],
             "c": 1,
             "why": "Marx says the rise in one line's rate of profit is here the result of higher "
                    "productivity in another, so the capitalist appropriates a gain of social "
                    "labour. The spinnery's s′ is assumed unchanged, and the yarn sells at value."},
            {"q": "In the lab, the unsafe preset and a preset that saves £20 with a better boiler "
                  "both start from 400c + 100v + 100s. How do their rates of profit compare?",
             "a": ["The unsafe one is lower, because accidents cost money",
                   "They are equal, 5/24",
                   "The boiler one is higher, because it raises productivity",
                   "They cannot be compared"],
             "c": 1,
             "why": "Both cut c by £20 with s and v fixed, so both give `100/480 = 5/24`. The "
                    "figures carry no trace of how the saving was made, which is Marx's point. A "
                    "cost of accidents to the firm, or a gain in productivity, would be further "
                    "changes in the figures, not part of these."},
        ],
        "mistakes": [
            ("Treating economy in constant capital as only good management",
             "Much of it is a real saving, and Marx describes engines, buildings and reused waste "
             "at length. But the unsafe preset cuts c by £20 by not buying guards and ventilation, "
             "and the rate rises from 20% to `5/24`, exactly as a £20 saving from a better boiler "
             "would. The rate of profit rewards both alike, which is why Marx files the crowded "
             "room under &ldquo;a saving in buildings&rdquo;."),
            ("Thinking a saving in c produces more surplus value",
             "In the shared-building preset the profit is £100 before and after. The rate rises "
             "because the same surplus is measured against a smaller capital, not because more "
             "is produced."),
            ("Crediting every economy to the individual capitalist",
             "Marx's argument is that most of them come from the combination of many workers, "
             "or from productivity in the industries that supply the capitalist, and he "
             "appropriates them. The lab cannot show where a saving came from, only what it does "
             "to the rate."),
        ],
        "standard": (
            "Finish when you can compute the rise in p′ from a saving in c and classify the saving.",
            "Given c, v and s and a reduction in c with s and v unchanged, compute the rate of "
            "profit before and after and the new cost price, and state whether the saving came "
            "from scale, cheaper inputs, reused waste or the conditions of work."
        ),
        "note": (
            "The savings in the presets are illustrative; the evidence the lesson cites is "
            "Marx's. The lab sees a smaller c and nothing else: it cannot price a lost life, "
            "and it holds s and v fixed, as the chapter does, so a saving made by lengthening "
            "the working day is described here but not computed."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 3, l. 1290-1292 (inversely as the price of raw material);
    # l. 1300-1302 (not accompanied by a corresponding rise). Inline: l. 1298
    # (Greg, the corn laws, the ten hours), l. 1310 (waste: 3½d., 7d., 2 sh.),
    # l. 1338 (stocks appreciate), l. 1372 (2,000c + 400v + 600s), l. 1424
    # (1845-46: cotton up, goods down), l. 1434 (4d. to 6d.), l. 1469 (stocks
    # held in Blackburn).
    {
        "slug": "price-fluctuations-of-raw-materials",
        "title": "Price Fluctuations of Raw Materials",
        "module": "Chapter 6 · The Effect of Fluctuations in Price",
        "one_line": "A dearer raw material lowers the rate of profit even if the product's price follows it in full, and in practice the product's price seldom follows in full.",
        "summary": (
            "Chapter 6 lets the price of the raw material move with the surplus value fixed. "
            "Compute the rate of profit when cotton doubles and the yarn's price follows in "
            "full, in part or not at all, and when cotton falls. Then read the factory "
            "inspectors' record of the cotton famine of 1861 to 1865, where the case with no "
            "profit left was the real one."
        ),
        "key": [
            "dearer raw material: c and C rise",
            "same s on a larger C: p′ falls",
            "passed on in full: still a lower p′",
            "not passed on: profit falls by the rise",
            "stocks gain when raw material rises",
        ],
        "key_label": "The sixth chapter in five lines",
        "concepts_intro": (
            "The chapter has a law, two qualifications and a long history. The lesson keeps "
            "the law and the qualifications in the foreground."
        ),
        "concepts": [
            ("The law",
             "With s and v unchanged, a rise in the price of raw material raises c and so C, and "
             "the rate of profit falls; a fall raises it. The rate moves inversely with the "
             "price of raw material."),
            ("Passed on or not",
             "Raw material passes its whole value into the product in one turnover, so its "
             "price moves the product's value strongly. Marx notes that in practice the "
             "product's price rarely follows a rise or fall in full."),
            ("Stocks and release",
             "A capital already at work holds stocks of material and goods. A rise in price "
             "raises their value too, which can offset the fall in the rate; a fall in price "
             "depreciates them."),
        ],
        "read_title": "The law first, then what happens in reality",
        "read_intro": (
            "The law takes two sentences from the first section. Its qualification comes a few "
            "paragraphs later, and the lab works between the two."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 6, §1.</strong> &ldquo;Since the rate of profit "
                  "is represented by s/C, or s/(c+v), it is evident that everything which causes a "
                  "variation of the magnitude of c, and thereby of C, must also bring about a "
                  "variation in the rate of profit, even if s and v, and their mutual proportions, "
                  "remain unaltered. &hellip; Other circumstances remaining unchanged, the rate of "
                  "profit falls and rises, therefore, inversely as the price of raw "
                  "material.&rdquo;"),
            ("p", "You have seen this happen to a café when the price of coffee beans jumps: "
                  "either the cup costs more, or the café earns less on it, or both. Marx's "
                  "point is a step further. Even if the cup's price rises by exactly the dearer "
                  "beans, the café's rate of profit falls, because the same surplus is now made "
                  "on a larger capital. The last lesson cut c by economy; this one lets the "
                  "price of c's largest element, the raw material, move by itself."),
            ("p", "Take Marx's `400c + 100v + 100s` again, and suppose £100 of the c is cotton. "
                  "Cotton doubles: c becomes 500 and the cost price 600. If the product sells at "
                  "its new value, 700, the profit is still £100, but on a capital of 600: the "
                  "passed-on preset gives `1/6`, about 16.7%, down from 20%. The value has risen by "
                  "exactly the dearer cotton, as Chapter 1 showed it must, and the rate has fallen "
                  "anyway. The cheaper preset runs it the other way: cotton falls by half, c to "
                  "350, the product to 550, and the rate rises to `2/9`, about 22.2%."),
            ("p", "<strong>Volume III, Chapter 6, §1.</strong> &ldquo;For this reason we note in "
                  "reality that a rise in the price of raw material is not accompanied by a "
                  "corresponding rise of the price of the product, nor a fall in the price of the "
                  "raw material by a corresponding fall of that of the product.&rdquo;"),
            ("p", "The reason Marx gives is the market: a dearer product sells less, so its price "
                  "is held back. The lab's share passed on is the part of the rise that "
                  "reaches the product's price. The cotton-famine preset passes none of it on: "
                  "cost price £600, sale at the old £600, profit £0 and a rate of 0. The "
                  "half-passed preset passes on half: sale at £650, profit £50, rate `1/12`. The "
                  "profit falls by exactly the part of the rise that is not passed on. Marx's "
                  "conclusion is that the rate &ldquo;falls lower in one case, and rises higher in "
                  "the other&rdquo; than it would if products sold at their value."),
            ("p", "Raw material weighs more on the product's price than machinery does, because "
                  "it passes its whole value in one turnover while machinery passes only its "
                  "wear, and the waste rises with its price. Marx quotes the inspectors: with "
                  "15% waste, cotton at 3½d a pound loses ½d a pound in waste, and at 7d it "
                  "loses 1d; in the famine, with cotton at 2s, the loss was 6d. He also tells a "
                  "story against the manufacturers. In 1837 R. H. Greg calculated what the corn "
                  "laws added to the flour used for sizing cloth, and manufacturers declared "
                  "that ten hours of labour a day would be enough if the corn laws were repealed. "
                  "The corn laws and the cotton duties went; their opposition to the Ten Hours "
                  "Bill, Marx writes, &ldquo;became more violent than ever&rdquo;."),
            ("p", "The second section adds the qualification that softens the law for a capital "
                  "already at work. When cotton rises, the cotton in stock and the yarn and cloth "
                  "already made rise in value with it, and that appreciation may make good the "
                  "fall in the rate, &ldquo;or it may even more than make good that loss&rdquo;. "
                  "The inspectors saw it in Blackburn at the start of the famine: &ldquo;The "
                  "supplies rose in value so long as they were held in stock&rdquo;. Wages work "
                  "the same way. Marx's figures: `2,000c + 400v + 600s` is a rate of profit of 25%; "
                  "if the same 500 workers now cost 500, it is `2,000c + 500v + 500s` and 20%, and "
                  "a capital already invested must tie up £100 more just to keep its machinery "
                  "running."),
            ("p", "The third section is history, most of it the inspectors' reports from 1845 to "
                  "1864. In 1845 and 1846 cotton rose while the price of cotton goods fell below "
                  "where it had been, and mills went on short time; by 1847 cotton had risen from "
                  "4d to 6d a pound while yarn stood &ldquo;only a trifle above its former "
                  "price&rdquo;. Then the American Civil War cut off the supply. American cotton "
                  "had cost 5d or 6d a pound and went to 2s. Mills ran short time or closed; in "
                  "Lancashire and Cheshire in late 1862 about half the cotton workers had no work "
                  "at all. Marx reads the cycle as built in: machinery can be multiplied in a "
                  "year, cotton only at the pace of a harvest. Economists who trust prices to "
                  "balance the two hold that the high price itself calls out new supply, and the "
                  "inspectors' figures show Indian and Egyptian cotton arriving. What the chapter "
                  "sets against that is its observation that the supply of raw materials is "
                  "extended &ldquo;only convulsively&rdquo;, suddenly enlarged and then violently "
                  "contracted when the price falls back."),
            ("p", "The two chapters on c are done. The last lesson of the course, “Supplementary "
                  "Remarks on Profit”, asks why the capitalist, looking at all this, still does "
                  "not see his profit as surplus value."),
        ],
        "lab": ("capkit", {
            "mode": "profit",
            "view": "price",
            "money_unit": "£",
            "preset": "passed-on",
            "presets": [
                {"id": "passed-on", "label": "400c + 100v + 100s with £100 of cotton; cotton doubles, sold at the new value",
                 "c": 400, "v": 100, "s": 100, "c_change": 100, "price_passed_on": 1, "expect": {"prRate": "1/6 = 16.67%", "prProfit": "£100"}},
                {"id": "half-passed", "label": "Cotton doubles; half the rise reaches the price",
                 "c": 400, "v": 100, "s": 100, "c_change": 100, "price_passed_on": "1/2", "expect": {"prRate": "1/12 = 8.33%", "prProfit": "£50"}},
                {"id": "cotton-famine", "label": "Cotton doubles; the product's price does not move",
                 "c": 400, "v": 100, "s": 100, "c_change": 100, "price_passed_on": 0, "expect": {"prRate": "0 = 0%", "prProfit": "£0"}},
                {"id": "cheaper", "label": "Cotton falls by half; sold at the new value",
                 "c": 400, "v": 100, "s": 100, "c_change": -50, "price_passed_on": 1, "expect": {"prRate": "2/9 = 22.22%", "prProfit": "£100"}},
            ],
            "panel_title": "A change in the price of the raw material",
            "panel_intro": (
                "c, v and s go in, with the change in c's price and the share of it passed on "
                "in the selling price. The tiles give the rate of profit, the profit and the "
                "cost price. Compare passed-on with cotton-famine: the same dearer cotton, and a "
                "rate of `1/6` against 0."
            ),
        }),
        "steps_title": "Computing the rate after a price change",
        "steps_intro": "Four steps, with s and v held fixed and only the price of c changing.",
        "steps": [
            ("Change c",
             "Add the rise in the raw material's price to c, or subtract the fall. The cost "
             "price is the new `c + v`."),
            ("Set the selling price",
             "Start from the old value `c + v + s` and add the share of the change that is "
             "passed on. Passed on in full, the price is the new value."),
            ("Compute the profit",
             "The profit is the selling price minus the new cost price. It falls short of s by "
             "the part of a rise that is not passed on."),
            ("Compute the rate",
             "Divide the profit by the new capital. Compare it with the old rate `s/(c + v)`."),
        ],
        "worked": {
            "title": "£100 of cotton doubles",
            "intro": [
                "Marx's `400c + 100v + 100s` holds £100 of cotton, which doubles in price. You "
                "want the rate of profit if the price of the product follows, and if it does not.",
            ],
            "lines": [
                "c:  400 + 100 = 500,  cost price 500 + 100 = 600",
                "passed on:  price 700,  profit 700 − 600 = 100",
                "passed on:  p′ = 100 / 600 = 1/6",
                "not passed on:  price 600,  profit 600 − 600 = 0",
                "not passed on:  p′ = 0",
            ],
            "after": [
                "Even at the new value the rate falls from `1/5` to `1/6`. Every share of the "
                "rise not passed on comes straight off the £100 of profit, and with none passed "
                "on there is none left.",
            ],
        },
        "quiz_title": "Dearer and cheaper materials",
        "quiz": [
            {"q": "A capital of 300c + 100v + 100s pays £100 more for its raw material, and the "
                  "product sells at its new value. What is the new rate of profit?",
             "a": ["20%", "25%", "0%", "33.33%"],
             "c": 0,
             "why": "c becomes 400, so `100/500 = 1/5`. 25% is the old rate on 400, 0% would "
                    "need none of the rise passed on, and 33.33% divides by c alone."},
            {"q": "In the same case the product's price does not move at all. What is the "
                  "profit?",
             "a": ["£100", "£0", "−£100", "£50"],
             "c": 1,
             "why": "The cost price is `400 + 100 = 500` and the price stays at the old value, "
                    "500. The £100 of surplus value has been absorbed by the dearer material; "
                    "£50 would need half the rise passed on."},
            {"q": "Why does the rate of profit fall even when a rise in raw material is passed "
                  "on in full?",
             "a": ["Because the rate of surplus value falls",
                   "Because the same surplus value is measured against a larger capital",
                   "Because the product sells below its value",
                   "Because wages rise with the raw material"],
             "c": 1,
             "why": "Passed on in full, the product sells at its new value and the profit is "
                    "still s; only C has grown. s′ and wages are held fixed in the chapter's "
                    "assumption."},
            {"q": "According to the chapter's second section, what can offset the fall in the "
                  "rate of profit for a capital already at work when raw material rises?",
             "a": ["The rise in value of the stocks of material and goods it already holds",
                   "A fall in the rate of surplus value",
                   "A longer turnover",
                   "Nothing; the law admits no exception"],
             "c": 0,
             "why": "Marx says the appreciation of stocks may make good the loss, &ldquo;or it "
                    "may even more than make good&rdquo; it. A fall in s′ would worsen the "
                    "rate, a longer turnover lowers the annual rate, and the law is stated for "
                    "&ldquo;other circumstances remaining the same&rdquo;."},
        ],
        "mistakes": [
            ("Thinking a raw material price rise is always passed on in full",
             "Then a dearer material would cost the capitalist nothing but a little of his rate. "
             "Marx says the market holds the product's price back, and the inspectors recorded "
             "cotton up and goods down in 1845 and 1846. The cotton-famine preset passes none of "
             "the rise on: the cost price is £600, the sale £600, the profit £0. The half-passed "
             "preset leaves £50."),
            ("Expecting the rate to be unchanged when the rise is passed on",
             "The passed-on preset sells at the full new value of £700 and the rate still falls, "
             "from 20% to `1/6`, because £100 of profit is now on £600 of capital."),
            ("Concluding that a rise in raw material always hurts the capitalist",
             "For a capital with stocks on hand, the rise also raises the value of its cotton, "
             "yarn and cloth. Blackburn's mills in 1861 were saved partly by that. The law holds "
             "unconditionally, Marx says, for capital being newly invested."),
        ],
        "standard": (
            "Finish when you can compute p′ after a raw material price change, passed on or not.",
            "Given c, v and s, a change in the price of the raw material and the share of it "
            "passed on in the selling price, compute the new cost price, the profit and the "
            "rate of profit, and compare the rate with the rate before the change."
        ),
        "note": (
            "The cotton presets are illustrative; the prices in the text are the inspectors'. "
            "The lab changes only c and the selling price: it does not model the stocks a "
            "capital holds, the waste that rises with the price, or the short time and closures "
            "the famine brought, all of which the chapter discusses."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 3, l. 1544-1546 (the bourgeois will not consider). Inline:
    # l. 1546 (Engels: a blank), l. 1548-1550 (businesses A and B), l. 1550
    # (his individual activity), l. 1552-1558 (Rodbertus; gold; nC and C/n).
    {
        "slug": "supplementary-remarks-on-profit",
        "title": "Supplementary Remarks on Profit",
        "module": "Chapter 7 · Additional Remarks",
        "one_line": "The capitalist will not see his profit as surplus value, because circulation and his own business skill both seem to make it, and the same books can be read either way.",
        "summary": (
            "Chapter 7 is short and partly unfinished: it gives the capitalist's reasons for not "
            "seeing profit as unpaid labour. Reconcile his books with Marx's categories on the "
            "same figures, then compute Marx's two businesses that exploit the same labour "
            "equally and earn different rates of profit."
        ),
        "key": [
            "books: profit = price − cost price",
            "analysis: the same sum is s, made by v",
            "same s on more c: a lower p′",
            "scale all of C: p′ unchanged",
            "the difference is what the sum is called",
        ],
        "key_label": "The seventh chapter in five lines",
        "concepts_intro": (
            "The chapter collects reasons, and Engels notes a gap where one of them was to be "
            "developed. Three ideas come out of it."
        ),
        "concepts": [
            ("The capitalist's view",
             "Profit is what the selling price brings in over the cost price, a return on what "
             "was laid out. In the books there is no s and no v, only sales, costs and capital."),
            ("Business ability",
             "With the same surplus value, a capitalist who manages with less constant capital "
             "earns a higher rate. That difference is real, and it persuades him that his "
             "profit comes from his own activity."),
            ("Size and rate",
             "Changing the size of a capital leaves the rate of profit alone only in two cases: "
             "a change in the money measuring it, or a change that keeps its composition. "
             "Otherwise a change in size changes the rate."),
        ],
        "read_title": "The capitalist's refusal first, then his reasons",
        "read_intro": (
            "The chapter begins by granting the whole of Part I's assumption and then saying "
            "why the capitalist still will not see it."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 7.</strong> &ldquo;Nevertheless the bourgeois "
                  "will not consider his profit as identical with the surplus-value, that is to "
                  "say, with unpaid surplus-labor. And he will do so, for the following "
                  "reasons. 1) He forgets the process of production in the process of "
                  "circulation.&rdquo;"),
            ("p", "&ldquo;And he will do so&rdquo; is the translation's slip; the sense is that "
                  "he will not. The sentence before the passage grants Part I's assumption in "
                  "full: the profit of a sphere equals the surplus value produced in it. Even "
                  "so, the person who makes the profit does not recognise it. The first reason "
                  "is the one Chapter 1 met in Torrens: the surplus is realised by selling, so it "
                  "seems to come from selling. And there the manuscript stops. Engels' note in "
                  "brackets says &ldquo;There is a blank at this place, indicating that Marx "
                  "intended to dwell in detail on this point.&rdquo; You are reading a draft."),
            ("p", "The second reason is the one the chapter develops. Given the same exploitation, "
                  "the rate of profit still depends on the price of materials, the quality of the "
                  "machinery, the management. Marx's figures: two businesses each pay £1,000 of "
                  "wages and get £1,000 of surplus value, so the same number of workers are "
                  "exploited to the same degree. Business A works with £9,000 of constant "
                  "capital, business B with £11,000. A's rate is `1,000/10,000`, 10%; B's is "
                  "`1,000/12,000`, `8 1/3`%. The business-a and business-b presets compute them."),
            ("p", "The difference may be due, Marx says, &ldquo;wholly to a difference in business "
                  "ability&rdquo;. He does not deny the ability. His point is about what the "
                  "capitalist concludes from it: &ldquo;And this fact leads the capitalist to the "
                  "conviction that his profits are due, not to the exploitation of labor, but at "
                  "least, in part, to other circumstances independent of that exploitation, "
                  "particularly to his individual activity.&rdquo; A real difference in the rate "
                  "is read as the source of the profit itself."),
            ("p", "The lab's books view sets the two readings side by side. The ledger preset is "
                  "Chapter 1's commodity sold at its value of £600: the books show a cost price "
                  "of £500, a profit of £100 and a return of 20% on cost. The banner adds the "
                  "analysis of the same figures: the £100 is surplus value produced by £100 of "
                  "variable capital. Every number agrees. What differs is what the £100 is called, "
                  "and what it is taken to be a return on."),
            ("p", "The chapter then turns on Johann Karl Rodbertus, the Prussian landowner and "
                  "economist, who had argued that a larger capital earns a proportionally larger "
                  "profit and so cannot change the rate. Marx says that is true in only two "
                  "cases. The first is a change in the value of gold: a capital of £100 earning "
                  "£20 becomes £150 earning £30, and `150 : 30 = 100 : 20`, because nothing real "
                  "has changed, only its money name. The gold preset computes it. The second is "
                  "a change of scale with the composition unchanged: capitals of 1,000, 2,000 and "
                  "500 at the same composition earn 200, 400 and 100. In every other case a "
                  "change in size comes with a change in composition, and the rate moves, as "
                  "business B's extra £2,000 of c showed."),
            ("p", "The obvious objection is that the capitalist may simply be right. If capital "
                  "is productive, and management is a skill that earns its reward, then business "
                  "A's higher rate is A's achievement and nothing is disguised. The chapter does "
                  "not argue that point; it explains why the capitalist believes it, and grants "
                  "that the gap between A and B may come wholly from business ability. Whether "
                  "his belief is an illusion rests on Volume I's account of where the £1,000 of "
                  "surplus value came from, and the lab cannot test that: it shows only that the "
                  "two readings agree on every figure."),
            ("p", "Part I has treated profit and surplus value as equal in amount. Average Profit "
                  "and Its Fall takes the next step, Volume III's Part II: capitals of different "
                  "composition must earn the same rate, so profit and surplus value part company "
                  "sphere by sphere."),
        ],
        "lab": ("capkit", {
            "mode": "profit",
            "view": "books",
            "money_unit": "£",
            "preset": "ledger",
            "presets": [
                {"id": "ledger", "label": "Marx's Chapter 1 figures: 400c + 100v + 100s, sold at £600",
                 "c": 400, "v": 100, "s": 100, "sale_price": "", "expect": {"prProfit": "£100", "prRate": "1/5 = 20%"}},
                {"id": "business-a", "label": "Marx's business A: 9,000c + 1,000v + 1,000s",
                 "c": 9000, "v": 1000, "s": 1000, "sale_price": "", "expect": {"prProfit": "£1,000", "prRate": "1/10 = 10%"}},
                {"id": "business-b", "label": "Marx's business B: 11,000c + 1,000v + 1,000s",
                 "c": 11000, "v": 1000, "s": 1000, "sale_price": "", "expect": {"prProfit": "£1,000", "prRate": "1/12 = 8.33%"}},
                {"id": "gold", "label": "Marx's £100 earning £20, re-priced as £150 when gold's value changes",
                 "c": 120, "v": 30, "s": 30, "sale_price": "", "expect": {"prProfit": "£30", "prRate": "1/5 = 20%"}},
            ],
            "panel_title": "The books and the analysis",
            "panel_intro": (
                "c, v and s go in, with a selling price; leave it empty to sell at the value. "
                "The tiles are what the books show: profit, the rate on cost, the cost price. "
                "The banner reads the same figures as surplus value. Compare business-a with "
                "business-b: the same surplus on the same wages, and two different rates."
            ),
        }),
        "steps_title": "Reading one set of figures two ways",
        "steps_intro": "Four steps that put a capitalist's account beside Marx's categories.",
        "steps": [
            ("Read the books",
             "From the selling price and the cost price, compute the profit and its rate on "
             "the capital laid out."),
            ("Split the cost price",
             "Divide the cost price into c, the means of production, and v, the wages."),
            ("Name the profit",
             "At a sale at value the profit equals s. Compute `s′ = s/v` beside the books' "
             "rate."),
            ("Compare two businesses",
             "With equal v and s, a difference in the rate of profit comes from c alone. Say "
             "whether exploitation or the constant capital differs."),
        ],
        "worked": {
            "title": "One commodity, two accounts",
            "intro": [
                "Chapter 1's commodity, `400c + 100v + 100s`, is sold at its value of £600. You "
                "want the books' figures and the analysis of the same sale.",
            ],
            "lines": [
                "books:  cost price 400 + 100 = £500",
                "books:  profit 600 − 500 = £100,  rate 1/5",
                "analysis:  s = £100, produced by v = £100",
                "analysis:  s′ = 100 / 100 = 100%,  p′ = 1/5",
            ],
            "after": [
                "The books and the analysis agree on every figure. They disagree only about what "
                "the £100 is: a return on the £500 laid out, or the unpaid labour bought with "
                "the £100 of wages.",
            ],
        },
        "quiz_title": "Profit as the capitalist sees it",
        "quiz": [
            {"q": "A commodity of 400c + 100v + 100s is sold at its value. What profit do the "
                  "capitalist's books record?",
             "a": ["£0, since it was sold at value", "£100", "£600", "£500"],
             "c": 1,
             "why": "The books record the selling price minus the cost price, `600 − 500 = 100`, "
                    "which is the whole surplus value. A sale at value is not a sale at cost "
                    "price. £600 is the price and £500 the cost price."},
            {"q": "Marx's businesses A and B each pay £1,000 in wages and produce £1,000 of "
                  "surplus value; A has £9,000 of constant capital, B £11,000. Which statement "
                  "is right?",
             "a": ["A exploits its workers more, since its rate of profit is higher",
                   "Both exploit to the same degree; A's rate of profit is 10%, B's 8 1/3%",
                   "Both have a rate of profit of 10%",
                   "B's rate of profit is higher, since it has more capital"],
             "c": 1,
             "why": "s′ is 100% in both. The rates of profit are `1,000/10,000` and "
                    "`1,000/12,000`. The difference comes from c, not from exploitation, and more "
                    "capital with the same surplus means a lower rate."},
            {"q": "In which case does a change in the size of a capital leave its rate of profit "
                  "unchanged, according to the chapter?",
             "a": ["Whenever the capital grows, since its profit grows with it",
                   "When the capital doubles by adding constant capital only",
                   "When it grows with its composition unchanged",
                   "Never"],
             "c": 2,
             "why": "Marx names two cases: a change in the value of the money and a change of "
                    "scale that keeps the proportion of v to c. Adding c alone lowers the rate. "
                    "The first option is Rodbertus' general claim, which Marx says holds only in "
                    "those two cases."},
            {"q": "Gold's value changes so that a capital of £100 earning £20 is now expressed "
                  "as £150. What is its profit and rate of profit?",
             "a": ["£20 and 13.33%", "£30 and 20%", "£30 and 30%", "£20 and 20%"],
             "c": 1,
             "why": "Everything is re-priced in the same proportion, so the profit becomes £30 "
                    "and `30/150 = 1/5`. Keeping the profit at £20 forgets that it is "
                    "re-priced too; 30% divides by the old capital."},
        ],
        "mistakes": [
            ("Thinking a capitalist who sells at value makes no profit",
             "It follows if cost price is taken for value, and Chapter 1 showed who took it so. "
             "The ledger preset sells Chapter 1's commodity at its value of £600 and the books "
             "record a profit of £100 on a cost price of £500, a rate of 20%. Sale at value "
             "realises the whole surplus value as profit."),
            ("Reading a higher rate of profit as more exploitation",
             "Businesses A and B pay the same £1,000 of wages and get the same £1,000 of surplus "
             "value. A's rate is 10% and B's `8 1/3`%, because B works with £2,000 more constant "
             "capital. The rate differs; the exploitation does not."),
            ("Assuming the size of a capital never affects its rate",
             "Rodbertus' view, which Marx limits to two cases: a change in money's value, as in "
             "the gold preset, and a change of scale at the same composition. Business B is the "
             "other case: £2,000 more of c and the same surplus, so a lower rate."),
        ],
        "standard": (
            "Finish when you can read one set of figures as the books do and as Marx does.",
            "Given c, v, s and a selling price, compute the profit, the cost price and the rate "
            "on cost as the books show them, state the same profit as surplus value with its "
            "rate s′, and for two capitals with equal v and s, compute and explain their "
            "different rates of profit."
        ),
        "note": (
            "The figures are Marx's. The books view sells at value unless a price is typed, as "
            "Part I assumes. The chapter is unfinished where Engels marks a blank, and the "
            "lesson does not fill it in. The lab shows the books and the analysis agreeing; "
            "which reading names the £100 correctly is the argument of the whole book."
        ),
    },
]
