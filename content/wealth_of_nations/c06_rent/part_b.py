"""The Rent of Land, lessons 4-6 -- Book I, Chapter 11: Part 3 and the Digression
concerning the variations in the value of silver.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt;
the comment beside each lesson gives its line numbers. A quotation never runs over a
page break of the extraction (its running heads and page numbers would sit in the
middle of it), so a few of Smith's long sentences are paraphrased instead.

Money. Smith writes pounds, shillings and pence: twelve pence to the shilling, twenty
shillings to the pound, so a pound is 240 pence. The Digression's prices are for the
quarter of eight bushels (the Windsor figures are for the best wheat, in the quarter of
nine bushels, unless a line says it has been reduced). Every price in these labs is in
pounds, written as decimals or fractions of a pound (13s 4d is 2/3), so that the lab's
last tile, the corn a pound buys, is a figure a reader can read; the first preset of each
lesson is in the money of Smith's day, the "present money" of 1776.
"""

LESSONS = [
    # ---------------------------------------------------------------- 04
    # PSU text l. 5846-5866 (the three combinations); l. 5868-5899 (1350 and the
    # Statute of Labourers); l. 5910-5919 (the feast of 1309); l. 5952-5999 (the
    # silver in 6s 8d); l. 6027-6035 (the opinion Smith opposes); l. 6120-6180
    # (Fleetwood's prices); l. 6181-6211 (cattle and corn); l. 6366-6367 (corn a
    # necessary); l. 6005-6026 (demand or exhausted mines); l. 6600-6616 (silver risen
    # rather than corn fallen, said of the years after 1700); l. 8485-8632
    # (Fleetwood's table and its seven averages).
    {
        "slug": "the-value-of-silver-over-four-centuries",
        "title": "The Value of Silver over Four Centuries",
        "module": "Book I, Chapter 11, Digression · First Period, 1350 to about 1570",
        "one_line": "A falling price of corn in silver means silver grew dearer in corn, not corn cheaper, and Smith reads four centuries of wheat prices to say so.",
        "summary": (
            "In the Digression Smith turns from rent to the value of silver, which he "
            "measures in corn. Read his first period: a quarter of wheat at four ounces "
            "of silver in 1350 and two ounces by 1500. Work the Statute of Labourers "
            "and the feast of 1309 as he does, average Fleetwood's prices into seven "
            "divisions with the lab, and see why Smith, who warns the table is uncertain, "
            "still takes it to refute the opinion that silver always grew cheaper."
        ),
        "key": [
            "price of corn = silver per quarter of corn",
            "falling price: silver dearer in corn",
            "average the ordinary years, not the extremes",
            "silver in a nominal sum changes with the coin",
            "corn: a necessary; silver: a superfluity",
        ],
        "key_label": "Reading the price of corn as the value of silver",
        "concepts_intro": (
            "The Digression is the longest passage of its kind in the book, and Smith "
            "says in its title what it is for. The first period holds three ideas."
        ),
        "concepts": [
            ("Corn as the measure of silver",
             "Labour is the real measure of value, but corn, which a labourer lives on, "
             "keeps nearly the same labour cost through the stages of improvement, so "
             "&ldquo;we can judge better of the real value of silver, by comparing it "
             "with corn&rdquo;. A silver price of corn that falls means silver buys more "
             "corn, and silver has become dearer."),
            ("The ordinary price, not the remarkable one",
             "Statutes and ordinary accounts record what was thought a moderate price. "
             "Chroniclers record years of dearth and glut. Smith prefers the first, and "
             "reduces every price to the silver in it, since the coin lost silver "
             "while its name stayed."),
            ("Three ways to be misled",
             "Writers took conversion prices for market prices, copied only the first "
             "lines of old statutes, and judged ordinary prices by the lowest ever "
             "recorded. Smith corrects all three and ends by saying where his own "
             "evidence is thin."),
        ],
        "read_title": "The three combinations, then four centuries of wheat",
        "read_intro": (
            "The Digression is set up in the last page of Part III, and this lesson "
            "starts there. The tables at the end of the chapter, which Smith refers "
            "to throughout, are in the book and are used here only in part."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 11, Part 3.</strong> Smith has argued that as "
                  "improvement spreads, the produce that sometimes affords rent "
                  "should grow dearer in food. Silver is the exception, because "
                  "its market is the whole commercial world. Three things could happen "
                  "to its value, and he lists them: if demand grows faster than supply, "
                  "silver gets dearer and &ldquo;the average money price of corn would "
                  "gradually become cheaper and cheaper&rdquo;; if supply grows "
                  "faster, corn grows dearer in silver; if they keep pace, its price "
                  "stays about the same. &ldquo;These three seem to exhaust all the "
                  "possible combinations of events which can happen in the progress of "
                  "improvement; and during the course of the four centuries preceding "
                  "the present ... each of those three different combinations seems to "
                  "have taken place in the European market, and nearly in the same "
                  "order, too, in which I have here set them down.&rdquo; The Digression "
                  "that follows is his evidence, and it comes in three periods."),
            ("p", "<strong>First period.</strong> &ldquo;In 1350, and for some time "
                  "before, the average price of the quarter of wheat in England seems "
                  "not to have been estimated lower than four ounces of silver, Tower "
                  "weight, equal to about twenty shillings of our present money.&rdquo; "
                  "From that it fell by about 1500 to two ounces, about ten shillings, "
                  "and stayed there until about 1570. Everything in the section is "
                  "about how Smith knows this, and what it shows."),
            ("p", "His first witness is a statute. In 1350 Parliament, complaining "
                  "of &ldquo;the insolence of servants, who endeavoured to raise their "
                  "wages upon their masters&rdquo;, ordered that livery wheat, the corn "
                  "paid in kind as part of a wage, should be valued at no more than "
                  "tenpence a bushel. Tenpence was then about half an ounce of silver. "
                  "So the quarter of eight bushels was 80 pence, six shillings and "
                  "eightpence, containing four ounces. A statute that tries to fix a "
                  "moderate price, he says, &ldquo;is surely a better evidence of what "
                  "was reckoned, in those times, a moderate price of grain, than the "
                  "prices of some particular years&rdquo;."),
            ("p", "He adds two more. In 1309 Ralph de Born, prior of St Augustine's "
                  "at Canterbury, gave a feast on his installation day of which William "
                  "Thorn preserved the bill of fare: fifty-three quarters of wheat cost "
                  "£19, &ldquo;or seven shillings, and twopence a-quarter&rdquo;. And "
                  "the assize of bread and ale of 1262 regulated the price of bread "
                  "for wheat from one shilling to twenty shillings the quarter, whose "
                  "middle price, he argues, was not less than a third of the highest, six "
                  "shillings and eightpence again. The three come from different "
                  "sources and all point to about four ounces of silver, which is why "
                  "he trusts them."),
            ("p", "Then the surprise. For more than two hundred years afterwards "
                  "statutes still treated six shillings and eightpence as the moderate "
                  "price: a rule of 1436 let wheat be exported at that price, one of "
                  "1463 forbade its import below it. But the silver in a "
                  "six-and-eightpence had been shrinking all that time, as the coin was "
                  "altered. By 1436 it held as much silver as thirteen shillings and "
                  "fourpence of the money of Smith's day, one third less than in "
                  "Edward III's time, and by 1512 only two ounces, the ten shillings "
                  "of his day. So the same nominal price meant a smaller and smaller "
                  "amount of silver, and the legislators saw no reason to change the "
                  "figure because silver had in the meantime grown dearer. The lab's "
                  "money-and-silver preset has Smith's five prices in pounds of "
                  "the money of 1776: £1 in 1350 (twenty shillings), 2/3 of a pound in "
                  "1436 and in 1463 (thirteen and fourpence), £1/2 in 1512 and in 1562 "
                  "(ten shillings). Grouped as 1350, then 1436 to 1463, then 1512 to "
                  "1562, the ratios to the first are 2/3 and 1/2, and the last tile "
                  "turns the prices round: a pound of 1776 money buys 1 quarter of "
                  "wheat in 1350, 1.50 quarters in the middle period and 2 quarters at "
                  "the end. Silver buys twice as much corn at the end as at the start."),
            ("p", "Why corn, and not cattle or poultry? Because, Smith argues, "
                  "&ldquo;Labour, it must always be remembered, and not any particular "
                  "commodity, or set of commodities, is the real measure of the value "
                  "both of silver and of all other commodities&rdquo;, and corn is the "
                  "nearest thing to labour that a price can track: it is always the "
                  "product of human industry, its supply is fitted to the demand, "
                  "and it is what a labourer lives on. Cattle, poultry and game were "
                  "cheap in ancient times, he says, but &ldquo;this cheapness was not the "
                  "effect of the high value of silver, but of the low value of those "
                  "commodities&rdquo;. An ox at Buenos Ayres cost twenty-one pence "
                  "halfpenny, and silver is certainly not dear there. And a "
                  "reason of another kind: &ldquo;Corn is a necessary, silver is only a "
                  "superfluity.&rdquo; People give up their superfluities first when "
                  "they are poor, so the value of silver, if anything, sinks in "
                  "hard times and corn rises."),
            ("p", "He then names the opinion he is arguing against, that from the "
                  "Conquest until America's mines were found the value of silver "
                  "continually diminished. It rests, he says, on the popular notion that "
                  "&ldquo;as the quantity of silver naturally increases in every country "
                  "with the increase of wealth, so its value diminishes as its quantity "
                  "increases&rdquo;, which he finds &ldquo;altogether groundless&rdquo;, and "
                  "on three mistakes about corn prices. Scottish rents were paid in kind "
                  "with the landlord's option of money at a conversion price kept below "
                  "the market price, in places about half of it, and Bishop Fleetwood, "
                  "Smith says, copied a conversion price of eight shillings fifteen "
                  "times before admitting what it was. Copyists of the assize of "
                  "1262 stopped at twelve shillings when the table runs to twenty, "
                  "and later writers took six shillings for the middle. And the lowest "
                  "prices of very ancient times were remembered while the highest were "
                  "forgotten: in 1270 Fleetwood gives two prices of the quarter, £4 16s "
                  "and £6 8s, which Smith turns into £14 8s and £19 4s of his day."),
            ("p", "Last, the table. Smith says the reader will find at the end of the "
                  "chapter all the prices of wheat Fleetwood collected from 1202 to "
                  "1597, in the money of 1776, in seven divisions of twelve years "
                  "each, with the average of each, to which he has added the Eton "
                  "College prices of 1598 to 1601. The averages, in pounds, shillings "
                  "and pence of Smith's day: £2 19s 1&frac14;d, £1 18s 8d, "
                  "£1 5s 9&frac12;d, £1 1s 3&#8531;d, 14s 1d, 10s 0&frac12;d, and for "
                  "the last division £2 7s 5&frac12;d. The fleetwood-divisions preset "
                  "sets them out as fractions of a pound (£2 19s 1&frac14;d is "
                  "709&frac14; pence, 2837/960 of a pound), and prints the averages "
                  "as about £2.96, £1.93, £1.29, £1.06, £0.70, £0.50 and £2.37. The "
                  "fall is steady to the sixth division, which is under a fifth of "
                  "the first, and then comes the rise Smith expects. Read the other "
                  "way, a pound bought about 0.34 of a quarter in the first division "
                  "and almost 2 quarters in the sixth. But he does not claim much for it: "
                  "&ldquo;The prices, indeed, which Fleetwood has been able to collect, seem "
                  "to have been those chiefly which were remarkable for extraordinary "
                  "dearness or cheapness; and I do not pretend that any very certain "
                  "conclusion can be drawn from them.&rdquo; An average of "
                  "remarkable years is a rough guide, and he says so."),
            ("p", "Smith's reading of all this is simple. If the price of corn in "
                  "silver fell, silver became dearer in corn. After "
                  "America's mines were found, corn rose to three and four times its "
                  "money price, and everyone ascribed that to a fall in the value of "
                  "silver. Equally, he says of the smaller fall in the price of corn "
                  "after 1700, which the next lesson reads, "
                  "&ldquo;It would be more proper, perhaps, to consider this variation "
                  "in the average money price of corn as the effect rather of some "
                  "gradual rise in the real value of silver in the European market, "
                  "than of any fall in the real average value of corn.&rdquo; Why "
                  "silver rose is a separate question. Smith allows two causes: a growing "
                  "demand for it as Europe grew settled and rich, or a shrinking "
                  "supply as old mines were worked out, and thinks both natural to "
                  "suppose."),
            ("p", "Two kinds of critic, both from after his death, press on this. "
                  "Ricardo objected that corn is not a fixed measure: on his account its "
                  "cost, and so its price, rises when cultivation has to be pushed on "
                  "to worse land, so a silver price of corn can move with the cost of "
                  "growing corn and say little about silver. And historians who came "
                  "later drew much fuller price series from manorial and college "
                  "accounts, beginning with Thorold Rogers's <em>History of Agriculture "
                  "and Prices in England</em> from 1866 and continuing with Phelps Brown "
                  "and Hopkins, who in 1956 priced a basket of consumables rather than "
                  "wheat alone. Smith's reply, in his own words, is the one above: corn "
                  "is the commodity that most nearly represents equal quantities of "
                  "labour. Whether that holds is a question the lab cannot answer."),
            ("p", "The next lesson, <em>Silver from America</em>, follows the price "
                  "of corn through the rest of the Digression, when silver sank in "
                  "value, and asks what Smith can and cannot say about what came "
                  "after."),
        ],
        "lab": ("wonkit", {
            "mode": "rent",
            "view": "silver",
            "money_unit": "£",
            "preset": "money-and-silver",
            "presets": [
                {"id": "money-and-silver", "label": "Smith's wheat in the silver of 1776: 20s in 1350, 13s 4d in 1436 and 1463, 10s in 1512 and 1562",
                 "prices": "1350, 1; 1436, 2/3; 1463, 2/3; 1512, 1/2; 1562, 1/2",
                 "periods": "1350, 1350, 1350; 1436-1463, 1436, 1463; 1512-1562, 1512, 1562",
                 "expect": {"wreAverage": "1350 £1; 1436-1463 ≈ £0.67; 1512-1562 £0.50", "wreRatio": "1350 1×; 1436-1463 2/3 ≈ 0.67×; 1512-1562 1/2 = 0.50×", "wreCorn": "1350 1 quarter for £1; 1436-1463 3/2 = 1.50 quarters for £1; 1512-1562 2 quarters for £1"}},
                {"id": "fleetwood-divisions", "label": "Fleetwood's seven divisions as Smith prints their averages, in pounds of 1776",
                 "prices": "1202, 2837/960; 1287, 29/15; 1339, 619/480; 1423, 383/360; 1453, 169/240; 1499, 241/480; 1561, 1139/480",
                 "periods": "1202-1286, 1202, 1286; 1287-1338, 1287, 1338; 1339-1416, 1339, 1416; 1423-1451, 1423, 1451; 1453-1497, 1453, 1497; 1499-1560, 1499, 1560; 1561-1601, 1561, 1601",
                 "expect": {"wreAverage": "1202-1286 ≈ £2.96; 1287-1338 ≈ £1.93; 1339-1416 ≈ £1.29; 1423-1451 ≈ £1.06; 1453-1497 ≈ £0.70; 1499-1560 ≈ £0.50; 1561-1601 ≈ £2.37", "wreCorn": "1202-1286 960/2,837 ≈ 0.34 quarters for £1; 1287-1338 15/29 ≈ 0.52 quarters for £1; 1339-1416 480/619 ≈ 0.78 quarters for £1; 1423-1451 360/383 ≈ 0.94 quarters for £1; 1453-1497 240/169 ≈ 1.42 quarters for £1; 1499-1560 480/241 ≈ 1.99 quarters for £1; 1561-1601 480/1,139 ≈ 0.42 quarters for £1", "wreRatio": "1202-1286 1×; 1287-1338 1,856/2,837 ≈ 0.65×; 1339-1416 1,238/2,837 ≈ 0.44×; 1423-1451 3,064/8,511 ≈ 0.36×; 1453-1497 676/2,837 ≈ 0.24×; 1499-1560 482/2,837 ≈ 0.17×; 1561-1601 2,278/2,837 ≈ 0.80×"}},
            ],
            "panel_title": "Wheat in silver, period by period",
            "panel_intro": (
                "Each price is a quarter of wheat in pounds of the money of 1776, written "
                "as a fraction of a pound where it is less (13s 4d is 2/3), entered "
                "against a year; periods group the years. The lab averages each period, "
                "compares it with the first and prints how many quarters of wheat a "
                "pound of that money buys. In both presets each record is Smith's own "
                "figure for its period, so the average of a period is that figure."
            ),
        }),
        "steps_title": "Reading a price of corn as the value of silver",
        "steps_intro": "Four steps, as Smith does it.",
        "steps": [
            ("Reduce every price to one money",
             "A price of six shillings and eightpence is not the same price in "
             "1350 and 1512, because the coin held less silver. Convert each nominal "
             "price to its silver, or to the money of one date, before comparing."),
            ("Choose ordinary prices",
             "Use statutes and accounts of large ordinary purchases, and be wary of "
             "prices recorded for being remarkable. Smith averages Fleetwood's "
             "table in twelves, and says it is only a rough guide."),
            ("Average by period and divide",
             "Take each period's average price and divide it by the first period's. "
             "A ratio below one means corn cost less silver than before."),
            ("Invert to read silver",
             "The wheat a unit of silver buys is one divided by the average price. "
             "If it rises, silver has grown dearer in corn."),
        ],
        "worked": {
            "title": "The Statute of Labourers and the feast of 1309",
            "intro": [
                "Smith derives four ounces from a statute and checks the price of wheat "
                "against a feast. Both sums are small enough to do by hand.",
            ],
            "lines": [
                "a quarter:  8 · 10d = 80d = 6s 8d",
                "its silver:  8 · 1/2 oz = 4 oz",
                "four ounces ≈ 20s, so an ounce ≈ 5s",
                "tenpence:  1/2 oz · 5s = 2s 6d, a half-crown",
                "the feast:  £19 / 53 = 380s / 53 ≈ 7s 2d",
            ],
            "after": [
                "The half-crown agrees with what Smith says of tenpence, that it was "
                "&ldquo;nearly equal to half-a-crown of our present money&rdquo;. And "
                "380 shillings over 53 quarters is 7.17 shillings, which is seven "
                "shillings and twopence to the penny, as the prior's feast bill gives "
                "it.",
            ],
        },
        "quiz_title": "Silver in corn, century by century",
        "quiz": [
            {"q": "The Statute of Labourers of 1350 valued livery wheat at no more than "
                  "tenpence a bushel. What is that for the quarter of eight bushels?",
             "a": ["6s 8d", "10s", "8s 4d", "5s"],
             "c": 0,
             "why": "`8 · 10d = 80d`, which is six shillings and eightpence. Ten shillings "
                    "is what a bushel at 15d would give; 8s 4d is a quarter of ten bushels "
                    "at tenpence; 5s is a quarter of six."},
            {"q": "In Smith's account, the nominal price of 6s 8d was thought moderate "
                  "in 1350 and still in 1512, but the silver in it fell from four ounces "
                  "to two. What does that show about the price of wheat in silver?",
             "a": ["It rose by half",
                   "It fell by half",
                   "It stayed the same, because the nominal price did",
                   "It doubled"],
             "c": 1,
             "why": "A quarter that cost four ounces now costs two, half as much silver. "
                    "The nominal price stayed put because the coin had lost silver; Smith's "
                    "point is that the silver price, not the nominal one, is what to compare."},
            {"q": "In the lab's Fleetwood preset, which division has the lowest average "
                  "price?",
             "a": ["1202 to 1286", "1453 to 1497", "1561 to 1601", "1499 to 1560"],
             "c": 3,
             "why": "The lab prints the averages as about £2.96, £1.93, £1.29, £1.06, "
                    "£0.70, £0.50 and £2.37. The lowest, 10s 0&frac12;d, about £0.50, "
                    "belongs to 1499 to 1560, where a pound buys almost 2 quarters. "
                    "1453 to 1497 comes next, at 14s 1d, about £0.70."},
            {"q": "On Smith's account, what does a fall in the money price of corn, over a "
                  "period when it takes much the same labour to raise, most likely show?",
             "a": ["Silver has become dearer in corn",
                   "Corn has become less valuable in labour",
                   "Labourers' wages have been cut",
                   "The country has grown poorer"],
             "c": 0,
             "why": "Smith treats corn as a nearly steady measure of labour, so a falling "
                    "silver price of corn shows silver buying more corn. Corn has not become "
                    "less valuable in labour, and he denies that a low price of corn proves "
                    "poverty."},
        ],
        "mistakes": [
            ("Reading a fall in the money price of corn as corn becoming less valuable",
             "When the price of corn in silver falls, Smith says the better reading is that "
             "silver has grown dearer. After America's mines were found corn rose to "
             "three and four times its price, and nobody thought that corn had grown "
             "that much more valuable. The same logic runs in reverse in the first "
             "period."),
            ("Taking the low price of cattle and game in old times as proof silver was dear",
             "Smith answers that the cheapness of such things in a wild country was "
             "&ldquo;not the effect of the high value of silver, but of the low value of "
             "those commodities&rdquo;. They cost little labour to get, and bought "
             "little. Corn is the better yardstick because it is made by human industry."),
            ("Supposing silver must grow cheaper as a country grows rich",
             "That is the popular notion Smith calls groundless. The quantity of "
             "silver in a country may grow because its mines are richer, which does lower "
             "the metal's value, or because the people are richer and need more coin and "
             "plate, which does not. The first period shows the second happening."),
        ],
        "standard": (
            "Finish when you can read a silver price of corn as the value of silver.",
            "Given wheat prices in several periods, say in which direction silver "
            "changed in value, compute each period's average and its ratio to the first, "
            "and say what the conclusion depends on if the prices are of remarkable years.",
        ),
        "note": (
            "The lab only averages and divides. It cannot tell whether corn is a steady "
            "measure of labour, which Ricardo doubted, or whether the "
            "prices Fleetwood collected were typical, which Smith doubted himself. "
            "Smith's table is of prices he did not collect, many second-hand, "
            "and the table the lab uses is the seven averages Smith prints, not the "
            "prices behind them. The figures are Smith's and the lines are given in the "
            "preset labels."
        ),
    },
    # ---------------------------------------------------------------- 05
    # PSU text l. 6377-6426 (second and third periods); l. 6427-6455 (the civil war);
    # l. 6456-6468 (the bounty); l. 6469-6532 (clipped coin and the present century);
    # l. 6533-6535 (silver risen); l. 6617-6635 (the seasons, 1741-1750); l. 6884-6890
    # (silver to India); l. 6921-6989 (Cadiz and Lisbon, Meggens, Birmingham); l.
    # 7023-7075 (gold and silver, the ox and the lamb); l. 7181-7186 (scarce a belief);
    # l. 6274-6284 (coin "from necessity"); l. 8036-8062 (Poland, Spain and Portugal);
    # l. 8637-8827 (the Windsor table and its averages).
    {
        "slug": "silver-from-america",
        "title": "Silver from America",
        "module": "Book I, Chapter 11, Digression · Second and Third Periods, and the Proportion between Gold and Silver",
        "one_line": "American silver cut its value in corn until about 1636, and Smith argues, with great hedging, that it then slowly recovered.",
        "summary": (
            "Smith's second period runs from about 1570 to 1640, when silver sank in "
            "value and corn rose from about two ounces a quarter to six and eight; "
            "his third begins about 1636, and he argues that silver then held and "
            "began, perhaps, to rise. Work the conversion from best wheat to middle "
            "wheat and to ounces of silver, test each of the four Windsor averages "
            "against what Smith says distorted it, and read his reply to the claim "
            "that gold's value should follow the proportions imported."),
            "key": [
                "second period: silver sinks, corn rises",
                "about 1636 the effect was complete",
                "dear years and clipped coin raise a price",
                "ratio of values is not ratio of quantities",
                "his belief: silver rose a little after 1700",
            ],
        "key_label": "The second and third periods",
        "concepts_intro": (
            "These pages are a long argument about what a number does not show. They "
            "hold three ideas."
        ),
        "concepts": [
            ("The fall after 1570",
             "&ldquo;The discovery of the abundant mines of America seems to have been the "
             "sole cause&rdquo; of silver's sinking in value in proportion to corn, and "
             "Smith says nobody disputes it. The price of the quarter went from about "
             "two ounces of silver to about six and eight."),
            ("A price needs its circumstances",
             "The average at Windsor for 1637 to 1700 is higher than for 1621 to 1636, "
             "but a civil war, a bounty on export and clipped coin raised prices without "
             "silver cheapening. Smith strips them out before reading it."),
            ("Quantity is not value",
             "Silver is imported into Europe at twenty-two times the weight of gold, "
             "yet an ounce of gold is worth fourteen or fifteen of silver. The "
             "ratio of two commodities' prices is not the ratio of the amounts that "
             "come to market."),
        ],
        "read_title": "The sinking of silver, and what came after",
        "read_intro": (
            "The second period is short. The third is where Smith has to be "
            "careful, and he is. Read his hedges as part of the argument."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 11, Digression, Second Period.</strong> "
                  "&ldquo;From about 1570 to about 1640, during a period of about "
                  "seventy years, the variation in the proportion between the value of "
                  "silver and that of corn held a quite opposite course. Silver sunk in "
                  "its real value, or would exchange for a smaller quantity of labour "
                  "than before; and corn rose in its nominal price, and, instead of "
                  "being commonly sold for about two ounces of silver the quarter, or "
                  "about ten shillings of our present money, came to be sold for six and "
                  "eight ounces of silver the quarter, or about thirty and forty "
                  "shillings of our present money.&rdquo; No one disputes it, he adds, "
                  "&ldquo;either about the fact, or about the cause of it&rdquo;: the "
                  "mines of America."),
            ("p", "He gives the Windsor figures from the accounts of Eton College, and "
                  "the windsor-1595-1636 preset has every year of them for the best "
                  "wheat, in the quarter of nine bushels, from 1595 to 1636, as "
                  "fractions of a pound. The lab prints the average of the 26 prices "
                  "from 1595 to 1620 as about £2.08; worked exactly it is 25,933/52 "
                  "pence, which is 498.71 pence, or £2 1s 6.7d. Smith's text gives £2 1s 6 9/13d and "
                  "his table £2 1s 6&frac34;d, and the three agree to within a "
                  "farthing. To get the quarter of eight bushels he takes off a ninth, "
                  "and to get middle wheat, a ninth again, ending at about £1 12s "
                  "8 8/9d, &ldquo;or about six ounces and one-third of an ounce of "
                  "silver&rdquo;, at his figure of sixty-two shillings the pound troy, "
                  "which is 62 pence the ounce. The 16 prices from 1621 to 1636 average exactly "
                  "£2.50, £2 10s, which by the same two steps is £1 19s 6d, about "
                  "seven and two-thirds ounces. The lab's silver-falls preset puts in "
                  "pounds of 1776 money the ten shillings, £1/2, of the earlier period, "
                  "£1 12s 8 8/9d (221/135 of a pound, about £1.64) for 1595 to 1620 and "
                  "£1 19s 6d (£1.975, about £1.98) for 1621 to 1636. A pound that "
                  "bought 2 quarters before 1570 buys about 0.61 of a quarter, and then "
                  "about 0.51: silver buys about a third as much corn as in the first "
                  "period, and then about a quarter."),
            ("p", "The third period begins at once: &ldquo;Between 1630 and 1640, or "
                  "about 1636, the effect of the discovery of the mines of America, in "
                  "reducing the value of silver, appears to have been completed, and "
                  "the value of that metal seems never to have sunk lower in proportion "
                  "to that of corn than it was about that time.&rdquo; The evidence "
                  "needs care. The average for 1637 to 1700 is £2 11s 0&frac13;d, a "
                  "shilling above the sixteen years before, so on its face silver "
                  "had not risen. Smith lists three events. The civil war discouraged "
                  "tillage and interrupted trade, and sent the best wheat at Windsor to "
                  "£4 5s in 1648 and £4 in 1649. The bounty on export of 1688 raised "
                  "the home price. And the silver coin had been clipped and worn "
                  "to near five-and-twenty per cent below its standard by 1695, which "
                  "raised the nominal sum paid without raising the silver. "
                  "The two war years alone settle most of it. Their excess over £2 10s, "
                  "the average of the sixteen years before 1637, "
                  "is (1,020 − 600) + (960 − 600) = 780 pence, £3 5s, and 780 "
                  "pence over sixty-four years is about 12.2 pence a year, against the "
                  "12&frac13; pence by which the average exceeds the earlier one."),
            ("p", "For 1701 to 1764 the Windsor average in Smith's table is £2 0s 6&frac34;d, "
                  "&ldquo;about ten shillings and sixpence, or more than five-and-twenty "
                  "percent. cheaper&rdquo; than the last sixty-four years of the old "
                  "century. Check the percentage. The gap is 125.6 pence, which is 25.8% "
                  "of the lower price but 20.5% of the higher: so Smith's "
                  "five-and-twenty is the gap measured against the "
                  "later, lower price, or, equivalently, the earlier price is 25.8% "
                  "dearer. The lab's windsor-averages preset sets Smith's four "
                  "printed averages side by side, which it prints as about £2.08, £2.50, "
                  "£2.55 and £2.03, since the 64 years of each of the last two periods "
                  "are more than the lab takes. Silver in the third period is about "
                  "back where it was in the first of the four: the last ratio to the "
                  "first is about 0.98, and a pound buys about 0.49 of a quarter "
                  "against 0.48. From this Smith draws a belief, "
                  "or rather less: &ldquo;The value of silver, therefore, seems to have "
                  "risen somewhat in proportion to that of corn during the course of the "
                  "present century&rdquo; and he says of his own opinion that it "
                  "&ldquo;scarce, perhaps, deserves the name of belief&rdquo;. A "
                  "low decade, 1741 to 1750, at £1 13s 9 4/5d, and the dear years "
                  "after, he puts down to the seasons, since a change "
                  "&ldquo;in the value of silver, which is always slow and "
                  "gradual&rdquo; cannot be so sudden. (The two figures he gives "
                  "for the decade and the sixty-four years differ by about 6s 9d, where the "
                  "text says nearly 6s 3d: a slip somewhere on the page, and nothing "
                  "turns on it)."),
            ("p", "Why should silver have grown dearer when more was coming in? "
                  "Because the market grew faster. Smith names three. Europe, "
                  "which had grown settled and richer, needed more coin and plate. "
                  "America was a new market. And the East Indies took silver by the "
                  "ship-load, because there it bought more: in China and Indostan, he "
                  "says, an ounce of gold fetched ten or twelve of silver, against "
                  "fourteen or fifteen in Europe. Against this, the annual import into "
                  "Cadiz and Lisbon was about six millions sterling, of which the "
                  "gilding and plating of Birmingham alone, at fifty thousand pounds a "
                  "year, consumed a hundred-and-twentieth. The whole consumption of "
                  "gold and silver, he says, may perhaps be nearly equal to the whole produce, "
                  "and what remains may be no more than the growing countries need."),
            ("p", "Then the ratio of gold to silver. Before the American mines the "
                  "value of fine gold to fine silver ran between one to ten and one to "
                  "twelve; about the middle of the seventeenth century it came to be "
                  "between one to fourteen and one to fifteen. &ldquo;Both metals "
                  "sunk in their real value, or in the quantity of labour which they "
                  "could purchase; but silver sunk more than gold.&rdquo; Mr Meggens "
                  "put the yearly import into Spain and Portugal, on a six-year and a "
                  "seven-year average, at 1,101,107 pounds weight of silver and 49,940 "
                  "of gold, which is as one to twenty-two nearly, and inferred that "
                  "the values must stand in that proportion but for the silver sent to "
                  "the East. Smith's answer is an ox and a lamb: &ldquo;It would be "
                  "absurd, however, to infer from thence, that there are commonly in the "
                  "market three score lambs for one ox; and it would be just as absurd "
                  "to infer, because an ounce of gold will commonly purchase from "
                  "fourteen or fifteen ounces of silver, that there are commonly in the "
                  "market only fourteen or fifteen ounces of silver for one ounce of "
                  "gold.&rdquo; An ox at ten guineas is 210 shillings, a lamb at 3s 6d is "
                  "3.5, and the ratio is 60. A cheap commodity is sold in far greater "
                  "quantity than a dear one, and more of it in value too, because more "
                  "buyers can afford it. The lab does not model the gold ratio."),
            ("p", "This lesson is also a place to meet a critic who comes after "
                  "Smith. The quantity theory of money in its later forms, from "
                  "Irving Fisher's equation of exchange to Milton Friedman's "
                  "restatement, says the general level of prices moves with the stock of "
                  "money against the volume of goods, whatever causes the stock to grow. "
                  "Smith's text leaves room for that. His claim is narrower: where the "
                  "quantity of coin rises because the country's produce does, it rises "
                  "&ldquo;from necessity&rdquo;, to circulate more goods, and "
                  "he sees no reason for prices to rise. Later work on the "
                  "price rise of the sixteenth century, beginning with Earl "
                  "Hamilton's study of Spanish treasure in 1934, has weighed American "
                  "silver against a growing population and debased coinages; Smith had "
                  "no tables of population to weigh it with. The Digression "
                  "also ends with a warning. A high value of silver, or a low money "
                  "price of corn, in times past is no proof of poverty and "
                  "barbarism, and a low value of silver no proof of wealth: Poland, "
                  "where silver has lost value as elsewhere, and Spain and Portugal, "
                  "where it is cheapest, are on his account the most beggarly "
                  "countries in Europe."),
            ("p", "The next lesson, <em>Improvement and the Three Great Orders</em>, "
                  "goes back to the main line of the chapter, the sorts of rude "
                  "produce whose price rises as improvement spreads, and to what Smith "
                  "concludes about the landlords, the labourers and the dealers."),
        ],
        "lab": ("wonkit", {
            "mode": "rent",
            "view": "silver",
            "money_unit": "£",
            "preset": "silver-falls",
            "presets": [
                {"id": "silver-falls", "label": "Smith's wheat in the silver of 1776: 10s about 1512, then middle wheat at Windsor 1595 to 1620 and 1621 to 1636",
                 "prices": "1512, 1/2; 1595, 221/135; 1621, 1.975",
                 "periods": "to-1570, 1512, 1570; 1595-1620, 1595, 1620; 1621-1636, 1621, 1636",
                 "expect": {"wreAverage": "to-1570 £0.50; 1595-1620 ≈ £1.64; 1621-1636 ≈ £1.98", "wreRatio": "to-1570 1×; 1595-1620 442/135 ≈ 3.27×; 1621-1636 79/20 = 3.95×", "wreCorn": "to-1570 2 quarters for £1; 1595-1620 135/221 ≈ 0.61 quarters for £1; 1621-1636 40/79 ≈ 0.51 quarters for £1"}},
                {"id": "windsor-1595-1636", "label": "Windsor best wheat, the quarter of nine bushels, each year from 1595 to 1636 (Smith's table, in pounds)",
                 "prices": (
                     "1595, 2; 1596, 2.4; 1597, 3.475; 1598, 17/6; 1599, 47/24; 1600, 113/60; 1601, 209/120; 1602, 22/15; 1603, 53/30; 1604, 23/15; 1605, 43/24; 1606, 1.65; 1607, 11/6; 1608, 17/6; 1609, 2.5; 1610, 43/24; 1611, 29/15; 1612, 127/60; 1613, 73/30; 1614, 1001/480; 1615, 29/15; 1616, 121/60; 1617, 73/30; 1618, 7/3; 1619, 53/30; 1620, 91/60; 1621, 91/60; 1622, 44/15; 1623, 2.6; 1624, 2.4; 1625, 2.6; 1626, 37/15; 1627, 1.8; 1628, 1.4; 1629, 2.1; 1630, 167/60; 1631, 3.4; 1632, 8/3; 1633, 2.9; 1634, 2.8; 1635, 2.8; 1636, 17/6"
                 ),
                 "periods": "1595-1620, 1595, 1620; 1621-1636, 1621, 1636",
                 "expect": {"wreYears": "1595-1620 26 years; 1621-1636 16 years", "wreAverage": "1595-1620 ≈ £2.08; 1621-1636 £2.50", "wreRatio": "1595-1620 1×; 1621-1636 31,200/25,933 ≈ 1.20×", "wreCorn": "1595-1620 12,480/25,933 ≈ 0.48 quarters for £1; 1621-1636 2/5 = 0.40 quarters for £1"}},
                {"id": "windsor-averages", "label": "Windsor best wheat: Smith's four averages from 1595 to 1764, in pounds",
                 "prices": "1595, 133/64; 1621, 2.5; 1637, 1837/720; 1701, 649/320",
                 "periods": "1595-1620, 1595, 1620; 1621-1636, 1621, 1636; 1637-1700, 1637, 1700; 1701-1764, 1701, 1764",
                 "expect": {"wreAverage": "1595-1620 ≈ £2.08; 1621-1636 £2.50; 1637-1700 ≈ £2.55; 1701-1764 ≈ £2.03", "wreRatio": "1595-1620 1×; 1621-1636 160/133 ≈ 1.20×; 1637-1700 7,348/5,985 ≈ 1.23×; 1701-1764 649/665 ≈ 0.98×", "wreCorn": "1595-1620 64/133 ≈ 0.48 quarters for £1; 1621-1636 2/5 = 0.40 quarters for £1; 1637-1700 720/1,837 ≈ 0.39 quarters for £1; 1701-1764 320/649 ≈ 0.49 quarters for £1"}},
            ],
            "panel_title": "Wheat in silver after America",
            "panel_intro": (
                "Prices are pounds for a quarter of wheat, written as decimals or "
                "fractions of a pound, in the money of 1776 in the first preset and the "
                "nominal money of each year at Windsor in the others. The lab averages "
                "each period's years, compares each average with the first period's and "
                "prints how many quarters of wheat a pound buys."
            ),
        }),
        "steps_title": "Testing a period's average",
        "steps_intro": "Four steps for any run of averages, as Smith does.",
        "steps": [
            ("Put the prices on one footing",
             "Reduce best wheat to the quarter of eight bushels by taking off a ninth, "
             "and to middle wheat by taking off another ninth. Convert pence to "
             "silver at the mint rate Smith uses, sixty-two shillings the pound troy, "
             "which is 62 pence the ounce."),
            ("Average each period and compare",
             "Divide each period's average by the first's. A rise in the ratio is "
             "corn dearer in silver, which on Smith's reading is silver cheaper."),
            ("Ask what else raised the price",
             "A war, a bounty or a debased coin can raise a nominal price without "
             "silver cheapening. Smith subtracts what he can and says what he cannot."),
            ("Say how sure to be",
             "He calls his own opinion, that silver rose a little after 1700, something "
             "that scarcely deserves the name of belief. Copy that grade of "
             "confidence when the evidence is a few averages."),
        ],
        "worked": {
            "title": "From best wheat to ounces of silver",
            "intro": [
                "Take Smith's second period, 1621 to 1636, when the best wheat at "
                "Windsor, the quarter of nine bushels, averaged £2 10s.",
            ],
            "lines": [
                "£2 10s = 600d",
                "eight bushels:  600 · 8/9 = 1600/3 d",
                "middle wheat:  600 · (8/9)² = 38400/81 d ≈ 474.07d",
                "474.07d = £1 19s 6d",
                "ounces:  474.07 / 62 ≈ 7.65 oz",
            ],
            "after": [
                "That is £1 19s 6d, as Smith says, and about seven and two-thirds ounces of "
                "silver. The first period's two ounces for a quarter are now nearly four "
                "times that, the sinking of silver the Digression is about.",
            ],
        },
        "quiz_title": "What the averages show and what they hide",
        "quiz": [
            {"q": "The best wheat at Windsor, in the quarter of nine bushels, averaged "
                  "£2 10s from 1621 to 1636. Following Smith, take off a ninth for the "
                  "quarter of eight bushels and a ninth again for middle wheat. What is "
                  "the price?",
             "a": ["£1 19s 6d", "£2 4s 5d", "£1 13s 4d", "£2 0s 0d"],
             "c": 0,
             "why": "`600 · 8/9 · 8/9 ≈ 474.07` pence, which is £1 19s 6d. £2 4s 5d is "
                    "the quarter of eight bushels of the best wheat, with only the first "
                    "ninth taken off; the other two are not what either reduction gives."},
            {"q": "Why does Smith not read the higher Windsor average for 1637 to 1700 as "
                  "proof that silver kept on falling?",
             "a": ["Because the Windsor figures are not reliable",
                   "Because the accounts of Eton College stop in 1636",
                   "Because silver fell faster in those years",
                   "Because the civil war, the bounty on export and the clipped coin "
                   "raised the price without silver becoming cheaper"],
             "c": 3,
             "why": "Smith names three events that account for the price: the war, the "
                    "bounty on corn exports from 1688, and the clipping of the silver coin. "
                    "He does not doubt the Eton accounts or say silver fell faster. "
                    "The Windsor figures are what he uses."},
            {"q": "In the lab's Windsor preset, which period has the highest average "
                  "price of best wheat?",
             "a": ["1595 to 1620", "1621 to 1636", "1701 to 1764", "1637 to 1700"],
             "c": 3,
             "why": "The lab prints the averages as about £2.08, £2.50, £2.55 and £2.03, "
                    "so 1637 to 1700 is the highest and 1701 to 1764 the lowest."},
            {"q": "Meggens found that silver was imported into Spain and Portugal at "
                  "about 22 times the weight of gold, and reasoned that gold should be "
                  "worth about 22 ounces of silver. What is Smith's reply?",
             "a": ["The ratio of two commodities' prices is not the ratio of the "
                   "quantities in the market: oxen sell at sixty lambs, but there are "
                   "not sixty lambs to an ox",
                   "Gold is always worth exactly 15 ounces of silver",
                   "Silver imports are not recorded accurately",
                   "Gold is not used as money"],
             "c": 0,
             "why": "The ox and the lamb are his illustration: a dear commodity is "
                    "sold in smaller quantity and value than a cheap one, so the ratio of "
                    "values need not be the ratio of quantities. He does not say the "
                    "ratio is fixed, or that the imports are unreliable."},
        ],
        "mistakes": [
            ("Reading a rising price of wheat after 1636 as silver still sinking",
             "The Windsor average for 1637 to 1700 is above the one before, but Smith "
             "shows that a civil war, a bounty and clipped coin could account for it. "
             "The 1648 and 1649 prices alone add about twelve pence to the average."),
            ("Reading a change in the nominal price as a change in the silver paid",
             "The same nominal sum held less silver after the coin was clipped, and "
             "more after the recoinage. Smith calls the sum &ldquo;regulated, not so much by "
             "the quantity of silver, which, according to the standard, ought to be "
             "contained in it, as by that which, it is found by experience, actually "
             "is contained in it&rdquo;."),
            ("Inferring the ratio of values from the ratio of quantities",
             "Meggens did it with gold and silver, and Smith's ox and lamb show why it "
             "fails. A dear good sells in smaller quantity, so the pounds weight "
             "imported say little about how many ounces of silver an ounce of gold "
             "will fetch."),
        ],
        "standard": (
            "Finish when you can read a run of averages without overreading it.",
            "Given best-wheat prices for several periods, reduce them to middle wheat "
            "and to ounces of silver, say which period's price needs a footnote and why, "
            "and say how much confidence a few averages can bear.",
        ),
        "note": (
            "The lab cannot separate what Smith separates by argument: the war, the "
            "bounty and the clipped coin that distort the third period. It also cannot "
            "model the ratio of gold to silver. Smith's evidence for the rise in "
            "silver after 1700 is a handful of averages, and he knew it. Prices "
            "after 1764 are outside his table, and the long rise in British prices "
            "that followed, argued over in the Bullion Controversy, is a question "
            "about the later record, not about his arithmetic."
        ),
    },
    # ---------------------------------------------------------------- 06
    # PSU text l. 5802-5866 (Part 3's opening); l. 7241-7255 (the three sorts); l.
    # 7269-7272 (woodcocks); l. 7330-7331 (cattle cannot go higher); l. 7434-7436
    # (Scotland and the Union); l. 7505-7508 (poultry); l. 7643-7652 (the rise a
    # forerunner); l. 7400-7436 (lowland husbandry before the Union); l. 7555-7562
    # (cottagers); l. 7700-7712 (Hume's two-fifths; hides in Spanish America); l.
    # 7743-7775 (wool); l. 7855-7880 (a country of pasture); l. 7903-7940 (fish and
    # metals); l. 8193-8267 (manufactures, the watch, the scarlet cloth of 1487); l.
    # 8357-8484 (the conclusion and the three orders).
    {
        "slug": "improvement-and-the-three-orders",
        "title": "Improvement and the Three Great Orders",
        "module": "Book I, Chapter 11, Part 3 and the Conclusion of the Chapter",
        "one_line": "As improvement spreads the price of cattle, poultry and the like rises until it matches corn, the rent of land rises, and the interests of landlords, labourers and dealers are not alike.",
        "summary": (
            "Part III sorts rude produce into three kinds and says how each is priced as a "
            "country improves. Work out what a rise in the price of cattle does to a "
            "Highland estate's rent, and what the loss of a market for wool does to a "
            "sheep country's, then read Smith's closing page on the three great orders of "
            "society, each with its revenue and its interest, and what he says "
            "about each at his sharpest."),
        "key": [
            "first sort: cannot be multiplied",
            "second: rises until as good as corn land",
            "third: limited or uncertain; may even fall",
            "outlay fixed, price up: rent up faster",
            "dealers: interest opposite to the public's",
        ],
        "key_label": "Three kinds of produce, three orders",
        "concepts_intro": (
            "This is the last stretch of the longest chapter. It has a classification, "
            "a prediction and a verdict."),
        "concepts": [
            ("Three sorts of rude produce",
             "The first is what industry cannot multiply, the second what it can multiply "
             "to the demand, the third what it can only limitedly or uncertainly. "
             "Their prices behave differently as a country improves."),
            ("A rise in price as the forerunner of improvement",
             "Cattle cannot be reared on improved land until their price pays the "
             "rent and profit of corn land. That rise is, in Smith's words, "
             "&ldquo;the necessary forerunner and attendant of the greatest of all public "
             "advantages&rdquo;, not a public calamity."),
            ("Three orders, three interests",
             "Rent, wages and profit are the revenues of landlords, labourers and "
             "those who live by profit. The first two orders' interest is bound up "
             "with the public's, Smith says, while the dealers' is &ldquo;always in "
             "some respects different from, and even opposite to, that of the "
             "public&rdquo;."),
        ],
        "read_title": "Three sorts of produce, and the three orders",
        "read_intro": (
            "This is a long stretch of text, about fifteen hundred lines, and most "
            "of it is examples. Read for the classification first, and for the "
            "closing pages second."),
        "body": [
            ("p", "<strong>Book I, Chapter 11, Part 3.</strong> Part III opens from the "
                  "claim of Part II. As food grows more abundant with cultivation, the "
                  "demand rises for every part of the produce of land that is not food, so "
                  "the produce that only sometimes affords rent should keep growing "
                  "dearer in food. &ldquo;This, accordingly, has been the case with most "
                  "of these things upon most occasions&rdquo;, with the exception of "
                  "silver, which the Digression has just dealt with. Smith then divides "
                  "the rude produce whose price rises with improvement into "
                  "&ldquo;three classes. The first comprehends those which it is scarce in "
                  "the power of human industry to multiply at all. The second, those "
                  "which it can multiply in proportion to the demand. The third, those in "
                  "which the efficacy of industry is either limited or "
                  "uncertain.&rdquo;"),
            ("p", "The first sort is rare birds and fishes, game and wild fowl, "
                  "of which the supply is fixed by nature and is perishable. "
                  "&ldquo;If woodcocks should become so fashionable as to sell for "
                  "twenty guineas a-piece, no effort of human industry could increase "
                  "the number of those brought to market, much beyond what it is at "
                  "present.&rdquo; Their price, as wealth grows, has no ceiling. Smith "
                  "uses it to explain the prices the Romans paid for a white nightingale "
                  "or a surmullet: they were the high price of a rarity, not a low value "
                  "of silver, and in fact, he argues from the price of Sicilian wheat, "
                  "silver was dearer at Rome than in Europe now."),
            ("p", "The second sort is the interesting one: plants and animals which "
                  "nature produces in wild abundance and which cultivation then "
                  "crowds out, cattle first among them. Their real price rises as they "
                  "grow scarce, until it reaches a ceiling: &ldquo;When it has got so "
                  "high, it cannot well go higher. If it did, more land and more "
                  "industry would soon be employed to increase their quantity.&rdquo; "
                  "That ceiling is the price at which feeding cattle on cultivated "
                  "land pays the rent and profit that corn would. Until the price gets "
                  "there, Smith argues, the land cannot be fully improved: farms far from "
                  "any town can be manured only by their own cattle, and cattle that "
                  "are worth too little to feed on good land leave most of a farm "
                  "run out. That, he says, was the husbandry of lowland Scotland before the "
                  "Union with England, and he rates the rise in the price of cattle after "
                  "it as &ldquo;perhaps, the greatest&rdquo; of Scotland's commercial "
                  "gains from the Union."),
            ("p", "Poultry, hogs and the dairy follow the same road, each beginning as "
                  "a &ldquo;save-all&rdquo; kept on the farm's scraps and almost free. "
                  "As long as that is enough for the demand they are as cheap as any "
                  "meat, and when it is not, their price must rise until it pays "
                  "to cultivate land for them. He adds that the great rise in the price "
                  "of hogs and poultry has often been blamed on the loss of "
                  "cottagers, who raised them for nothing; that may have hastened it, "
                  "but the end would have come anyway."),
            ("p", "The lab takes the effect of such a rise on rent. A Highland "
                  "estate, in Smith's account of Part I, saw its cattle's price rise "
                  "&ldquo;about three times greater than at the beginning of the "
                  "century&rdquo; after the Union opened England's market, and the "
                  "rents of many estates were &ldquo;tripled and quadrupled&rdquo;. The "
                  "highland-cattle preset takes a pasture raising 60 beasts, with wages "
                  "of £24 and other stock of £16, so the outlay is £40 and ordinary profit "
                  "is £4. At £2 a beast the produce is worth £120 and the rent is £76. "
                  "Let the price triple to £6 and the produce is worth £360, so the "
                  "rent is £316. Rent has more than quadrupled, 4.16 times, on a "
                  "price that tripled. The preset is written for the lesson, and its "
                  "outlay is chosen so that the rent more than quadruples; what is "
                  "Smith's is the tripled price and the tripled and quadrupled rents. "
                  "This is the arithmetic of his closing remark, that when the "
                  "price of cattle rises the produce &ldquo;requires no more labour to "
                  "collect it than before&rdquo;, so a smaller part of it replaces "
                  "the stock with its ordinary profit and a greater part belongs to "
                  "the landlord. The lab holds the outlay fixed. A real estate's "
                  "outlay would move, so the multiple is what the model says, not what "
                  "any estate did."),
            ("p", "The third sort is produce whose quantity depends on something else, "
                  "or on other countries, so that industry can multiply it only "
                  "within limits, or unreliably. Wool and hides are appendages of the "
                  "cattle. Their market, unlike that of meat, is the world: wool and "
                  "raw hides can be shipped far, so when a country improves, their price "
                  "need not rise with the price of the beast. In an unimproved country "
                  "the fleece is a large part of the sheep's value. Smith says that "
                  "Hume reckoned it in Saxon times at two-fifths of the whole sheep, "
                  "and that in Spanish America cattle are killed for the hide and "
                  "tallow and the carcase left to rot. In England, though, the "
                  "price of wool has fallen since Edward III, and by his arithmetic "
                  "it fell in real terms by half: a tod of twenty-eight pounds, then "
                  "ten shillings of the money of that time, bought twelve bushels of "
                  "wheat, while one-and-twenty shillings, a good price in Smith's day, "
                  "bought six. He says this could not have happened &ldquo;in "
                  "consequence of the natural course of things&rdquo;. &ldquo;It has "
                  "accordingly been the effect of violence and artifice&rdquo;: the "
                  "prohibition of exporting English wool, free import of Spanish, and "
                  "the confining of Irish wool to England."),
            ("p", "The sheep-country preset shows why this mattered to a landlord in "
                  "a land of pasture. A hundred sheep, at £5 a head, with wages of "
                  "£180 and other stock of £120, ordinary profit 10%, give £500 of "
                  "produce against £330 of outlay and profit: rent £170. Let the "
                  "wool market close and the price of a sheep fall by a fifth, to £4, and the "
                  "rent is £400 − £330 = £70. A fifth off the price takes more "
                  "than half the rent. This is Smith's own point, that where "
                  "&ldquo;the wool and the hide made the principal part of the value "
                  "of those cattle&rdquo;, the loss of that market takes the whole price "
                  "of cattle down with it, and both the rent and the profit. "
                  "In an improved country the carcase's price rises to make up, "
                  "and the landlords lose little. The preset's prices are written for "
                  "the lesson."),
            ("p", "Fish and the metals are the other cases. Industry's power over the "
                  "fish brought to market, Smith says, is both limited, by the "
                  "country's situation and waters, and uncertain; over the metals it "
                  "is not limited but altogether uncertain, since new mines are a "
                  "matter of chance. Then he turns to manufactures. "
                  "&ldquo;It is the natural effect of improvement, however, to diminish "
                  "gradually the real price of almost all manufactures.&rdquo; A better "
                  "watch movement than £20 bought in the middle of the last century may "
                  "now, he says, perhaps be had for twenty shillings. A yard of the finest scarlet cloth was "
                  "reckoned in 1487 at sixteen shillings; at six shillings and eightpence "
                  "a quarter of wheat that is two quarters and three bushels or more, "
                  "and at twenty-eight shillings a quarter, at least £3 6s 6d of Smith's "
                  "money, against a guinea at most now. The exceptions are those whose "
                  "raw material grows dearer, as timber does, so that carpenters' and "
                  "joiners' work does not follow."),
            ("p", "<strong>Conclusion of the Chapter.</strong> From all this Smith "
                  "draws a result about landlords. &ldquo;every improvement in the "
                  "circumstances of the society tends, either directly or indirectly, to "
                  "raise the real rent of land&rdquo;: directly, by extending cultivation "
                  "and raising the price of cattle and the like; indirectly, because "
                  "whatever lowers the real price of manufactures makes the landlord's "
                  "surplus buy more of them. The wool example is the contrary case he lists, a fall "
                  "in the real price of part of the rude produce, which lowers the real rent. He then divides the whole annual produce, as the earlier "
                  "chapters did, into rent, wages and profit, the revenue of "
                  "&ldquo;three different orders of people&rdquo; from whose revenue "
                  "that of every other order is derived."),
            ("p", "He says three things about the orders and the public. Of the "
                  "landlords: their interest is &ldquo;strictly and inseparably "
                  "connected with the general interest of the society&rdquo;, so "
                  "that when the public deliberates, landlords &ldquo;never can mislead "
                  "it&rdquo;, but they are too often ignorant, the only order whose "
                  "revenue &ldquo;costs them neither labour nor care&rdquo;, and their "
                  "indolence makes them incapable of foreseeing a regulation's "
                  "consequences. Of labourers: their wages are highest when demand is "
                  "rising and they suffer cruelly in a decline, and they are "
                  "&ldquo;incapable either of comprehending that interest, or of "
                  "understanding its connexion with his own&rdquo;, and so little heard. "
                  "Of those who live by profit: the rate of profit falls with a "
                  "society's prosperity, unlike rent and wages, and is highest in the "
                  "countries going fastest to ruin. Merchants and master manufacturers "
                  "know their own interest better than country gentlemen know theirs, "
                  "but their interest is another matter."),
            ("p", "The last paragraph of the chapter is its sharpest: &ldquo;The interest "
                  "of the dealers, however, in any particular branch of trade or "
                  "manufactures, is always in some respects different from, and even "
                  "opposite to, that of the public. To widen the market, and to narrow "
                  "the competition, is always the interest of the dealers.&rdquo; The first "
                  "may suit the public, but to narrow the competition &ldquo;can only serve "
                  "to enable the dealers, by raising their profits above what they "
                  "naturally would be, to levy, for their own benefit, an absurd tax upon "
                  "the rest of their fellow-citizens&rdquo;. A proposal from this order "
                  "should be examined &ldquo;not only with the most scrupulous, but with "
                  "the most suspicious attention&rdquo;. Economists who study lobbying "
                  "often cite the passage. Smith says it of any proposal for a new law or "
                  "regulation of commerce that comes from this order, and Book IV is "
                  "where he follows such proposals one by one."),
            ("p", "Critics came at the three orders from three sides. Ricardo, who "
                  "gave a chapter of his <em>Principles</em> to Smith's doctrine of "
                  "rent, argued that rent rises as a growing population forces "
                  "cultivation onto worse land, so the landlord gains from the "
                  "dearness of food and his interest is opposed to the rest, the "
                  "reverse of Smith's &ldquo;inseparably connected&rdquo;. Marx, in "
                  "Volume III of <em>Capital</em>, argues with the division of the "
                  "whole product into rent, wages and profit as three independent "
                  "sources of revenue, which he calls the trinity formula; the "
                  "Capital lesson <em>The Trinity Formula</em> goes through what he "
                  "makes of it. And the lab's fixed outlay is Smith's own assumption "
                  "in the passage; on Ricardo's account the outlay on the margin "
                  "rises as worse land is cultivated, so the assumption is the point "
                  "in dispute."),
            ("p", "That ends <em>The Rent of Land</em>. The next course, <em>Stock, Money and Banks</em>, "
                  "turns to Book II: what a stock is, how it is divided, and why Smith "
                  "begins the book by calling the accumulation of stock a necessary "
                  "step before there is any division of labour."),
        ],
        "lab": ("wonkit", {
            "mode": "rent",
            "view": "residual",
            "money_unit": "£",
            "preset": "highland-cattle",
            "presets": [
                {"id": "highland-cattle", "label": "A Highland pasture when the price of a beast triples, from £2 to £6 (the price rise is Smith's; the outlay is written for this lesson)",
                 "lands": "highland-estate, 60, 24, 16",
                 "price": "2", "price2": "6", "rate": "10", "expect": {"wreRent": "highland-estate £76", "wreRent2": "highland-estate £316", "wreTotal2": "£316 at £6 a unit"}},
                {"id": "sheep-country", "label": "A sheep country when the price of a sheep falls from £5 to £4 with the loss of the wool market, written for this lesson",
                 "lands": "sheep-estate, 100, 180, 120",
                 "price": "5", "price2": "4", "rate": "10", "expect": {"wreRent": "sheep-estate £170", "wreRent2": "sheep-estate £70", "wreTotal2": "£70 at £4 a unit"}},
            ],
            "panel_title": "What a change in price does to rent",
            "panel_intro": (
                "One land, two prices. The lab computes the rent at each price, with "
                "the outlay and the ordinary profit held where they are, so every "
                "change in price falls on the rent."
            ),
        }),
        "steps_title": "Following a price change into rent",
        "steps_intro": "Four steps, for any land and any change in price.",
        "steps": [
            ("Fix the outlay",
             "Add the wages and stock for the year and the ordinary profit on them. "
             "Smith's closing argument assumes the produce takes no more labour to "
             "collect after its price has risen."),
            ("Compute rent at the first price",
             "Value the produce at the first price, take off the outlay and ordinary "
             "profit, and keep the remainder as the old rent."),
            ("Compute it at the second",
             "Do the same sum at the new price, with the same outlay. The rent that "
             "results is the whole of the change in price, added or taken away."),
            ("Compare the changes",
             "Divide each rent by the produce's value to get the landlord's share, "
             "and divide the new rent by the old. The rent changes by a larger "
             "proportion than the price, in either direction."),
        ],
        "worked": {
            "title": "A tod of wool, and the Highland pasture",
            "intro": [
                "Smith's wool sum and the lab's first preset use the same idea, a real "
                "price against a money one, and they are quick to check.",
            ],
            "lines": [
                "Edward III:  10s / (6s 8d / 8) = 120d / 10d = 12 bushels",
                "Smith's day:  21s / (28s / 8) = 21 / 3.5 = 6 bushels",
                "real price:  6 / 12 = 1/2",
                "money price:  21s / 30s = 7/10",
                "pasture:  60 · £2 − £44 = £76 at £2; 60 · £6 − £44 = £316 at £6",
            ],
            "after": [
                "The wool's money price fell to seven-tenths and its real price to a "
                "half, as Smith says. The pasture's rent rose 316/76, about 4.16 times, "
                "on a price that tripled.",
            ],
        },
        "quiz_title": "Improvement, rent and the orders",
        "quiz": [
            {"q": "A pasture raises 60 beasts. Wages are £24, other stock is £16, and "
                  "ordinary profit is 10% of the outlay. The price of a beast rises from "
                  "£2 to £6. What is the rent at £6?",
             "a": ["£228", "£320", "£316", "£120"],
             "c": 2,
             "why": "The produce is worth `60 · 6 = 360`. The outlay is 40 and its ordinary "
                    "profit is 4, so the rent is `360 − 44 = 316`. £228 is the old rent "
                    "of £76 tripled, which forgets that the outlay does not triple. £320 "
                    "leaves out the ordinary profit, and £120 is the old produce."},
            {"q": "Why can the price of woodcocks rise without limit as a country grows "
                  "rich, while the price of cattle cannot?",
             "a": ["Because cattle are cheaper to feed",
                   "Because woodcocks cost more to keep",
                   "Because landlords restrain the supply of woodcocks",
                   "Because industry cannot multiply woodcocks, but a high price of "
                   "cattle makes it worth turning more land to raising them"],
             "c": 3,
             "why": "The first sort of produce cannot be increased by industry, so its price "
                    "has no ceiling. The second can be, so once cattle pay as well as "
                    "corn land, more land and industry would soon be used for them. "
                    "Neither cost of keeping nor any restraint by landlords comes into it."},
            {"q": "What does Smith give as the reason the real price of English wool fell "
                  "between Edward III and his own day?",
             "a": ["Cheaper silver",
                   "Restraints: the prohibition of export, free import from Spain, and "
                   "Irish wool confined to England",
                   "A larger number of sheep",
                   "Better English manufacturing"],
             "c": 1,
             "why": "He says the fall &ldquo;has accordingly been the effect of violence and "
                    "artifice&rdquo; and lists three regulations. He argues that the "
                    "natural course of things would have raised the price, so the other "
                    "answers are not his."},
            {"q": "Which of the three orders does Smith say has an interest &ldquo;always "
                  "in some respects different from, and even opposite to, that of the "
                  "public&rdquo;?",
             "a": ["Landlords", "Labourers", "All three equally", "Dealers in particular branches of trade"],
             "c": 3,
             "why": "The landlords' and labourers' interests he calls strictly connected "
                    "with the society's, though he faults both for ignorance. Of the dealers "
                    "it is the interest in narrowing competition that he says is opposite to the "
                    "public's."},
        ],
        "mistakes": [
            ("Reading a rise in the price of cattle or poultry as proof that silver has "
             "grown cheaper",
             "A fall in the value of silver, Smith says, &ldquo;would affect all sorts of "
             "goods equally&rdquo;, a third or a fourth dearer together. Corn rose "
             "less than cattle and poultry, so the rise in those is the real rise in "
             "their price as land is improved, not a change in silver."),
            ("Taking the rise in the price of cattle for a public calamity",
             "Smith says it is a necessary forerunner of the improvement of land, "
             "since land cannot be improved to feed cattle until the price of cattle "
             "pays for it. It hurts those who buy meat, and he says so; it also marks "
             "the stage at which Scotland's lowlands could finally be cultivated."),
            ("Hearing the chapter's last pages as a verdict that landlords look after "
             "the public",
             "Smith says the landlords' interest is joined to the society's, and then "
             "says they are too often ignorant and incapable of understanding the "
             "consequence of a regulation. He says labourers cannot understand "
             "theirs, and dealers know their own interest better than the public's. All "
             "three orders are described, none is flattered."),
        ],
        "standard": (
            "Finish when you can follow a change of price into rent, and name the orders.",
            "Given a land's output, outlay, ordinary profit and two prices, compute the "
            "rent at each and the multiple, say why the multiple exceeds the price's, "
            "and say whose interest Smith calls opposite to the public's, and why.",
        ),
        "note": (
            "The lab holds the outlay fixed while the price moves, which is the "
            "assumption Smith's closing argument makes and the one a critic like "
            "Ricardo challenges: if rent rises because worse land is brought in, "
            "the outlay on the margin is not fixed. Smith's verdicts on the three "
            "orders are about interest and understanding, and no arithmetic here "
            "settles either. The highland and sheep estates are written for the "
            "lesson, and only the tripled price and the rents of tripled and "
            "quadrupled are Smith's."
        ),
    },
]
