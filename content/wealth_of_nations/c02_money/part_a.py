"""Money and the Measure of Value, lessons 1-4 -- Book I, Chapters 4 and 5.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition, Pennsylvania State University, 2005);
the comment beside each lesson gives its line numbers. Smith's spelling is kept
inside quotations.

Figures of Smith's own, used as preset data: the pound weight of silver, 240
pennies of a pennyweight each (l. 890-896); the mint's sixty-two shillings to the
pound weight (l. 1393-1395); the fractions to which the English, Scots and French
pounds had fallen (l. 913-916); the twenty-five and fifty shillings of a quarter
of corn (l. 1195-1197); the college rents and Blackstone's near double
(l. 1131-1148). The traders, the wage of a shilling a day and the series of corn
prices are written for the lessons and the presets say so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 756-760 (every man a merchant), l. 761-795 (the want of a
    # double coincidence, the commodities used as money), l. 796-826 (metals),
    # l. 827-875 (weighing, assaying, the public stamp), l. 876-925 (the
    # denominations and their debasement), l. 936-962 (value, the three questions).
    {
        "slug": "the-origin-and-use-of-money",
        "title": "The Origin and Use of Money",
        "module": "Book I, Chapter 4 · Of the Origin and Use of Money",
        "one_line": "When every man lives by exchanging, some one commodity that nobody will refuse becomes the instrument of exchange, and in every country it ends as a metal.",
        "summary": (
            "Smith asks how people trade once they have divided their work, and finds the "
            "butcher who has meat, the brewer who wants it, and nothing the butcher "
            "needs. Count the exchange ratios a market must quote with no common measure "
            "and with one, find who can trade directly, and follow the choice of cattle, "
            "salt and nails down to the metals, the public stamp, and the pound that "
            "began as a pound weight of silver."
        ),
        "key": [
            "ratios without a measure: n·(n − 1)/2",
            "ratios with a common measure: n − 1",
            "money serves when no pair coincides",
            "metals: lasting, and divisible without loss",
            "value in use is not value in exchange",
        ],
        "key_label": "Why money, in five lines",
        "concepts_intro": (
            "Chapter 4 is three short arguments in a row: why a common instrument of "
            "exchange arises, why it ends as a metal and then as a stamped coin, and "
            "what the word value is going to mean for the rest of the book."
        ),
        "concepts": [
            ("The want of a coincidence",
             "Once everyone lives by exchange, a trade needs two people each with what "
             "the other wants. The butcher has meat to sell, and the brewer and the baker "
             "want it, but have nothing he needs, so no exchange can be made between "
             "them. Smith does not give this a name; the phrase double coincidence of "
             "wants is W. S. Jevons's, from 1875."),
            ("A commodity few will refuse",
             "Every prudent man, Smith says, keeps by him besides his own produce some one "
             "commodity such as few people would refuse. Cattle, salt, shells, dried cod, "
             "tobacco and nails have each served, and in all countries the preference "
             "went to metals, which keep and which can be divided without loss and "
             "joined again by fusion."),
            ("Two meanings of value",
             "The word value, Smith says, sometimes expresses the usefulness of an "
             "object, its value in use, and sometimes the power of purchasing other "
             "goods that owning it conveys, its value in exchange. The things with the "
             "greatest value in use have frequently little or none in exchange: water "
             "and the diamond."),
        ],
        "read_title": "The butcher's difficulty, then the metals, then value",
        "read_intro": (
            "The chapter has the look of a history of money, and the first part is. But "
            "it ends on the question the next chapter is for: what regulates exchangeable "
            "value. Read to the end."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 4.</strong> The chapter starts where the last "
                  "one stopped. After the division of labour is established, only a very "
                  "small part of a man's wants can be supplied by his own produce: "
                  "&ldquo;Every man thus lives by exchanging, or becomes, in some measure, "
                  "a merchant, and the society itself grows to be what is properly a "
                  "commercial society.&rdquo; But at first, he says, the power of "
                  "exchanging &ldquo;must frequently have been very much clogged and "
                  "embarrassed in its operations&rdquo;."),
            ("p", "The example is the same three trades as before. &ldquo;The butcher has "
                  "more meat in his shop than he himself can consume&rdquo;, and the brewer "
                  "and the baker would each be willing to buy a part of it. &ldquo;But they "
                  "have nothing to offer in exchange, except the different productions of "
                  "their respective trades, and the butcher is already provided with all "
                  "the bread and beer which he has immediate occasion for.&rdquo; The "
                  "result: &ldquo;He cannot be their merchant, nor they his customers; and "
                  "they are all of them thus mutually less serviceable to one another.&rdquo;"),
            ("p", "The lab counts what this costs. Write the three goods meat, beer and "
                  "bread. With no common measure, each good must have a rate against each of "
                  "the others, and the number of pairs among n goods is "
                  "`n·(n − 1)/2`, so three goods need 3 ratios. If one of the goods serves "
                  "as the measure, each of the others needs only a price in it, which is "
                  "`n − 1`, so 2. In the preset <code>market-town</code>, with twelve goods "
                  "in a town's market, that is 66 ratios without a measure and 11 with "
                  "one. Its six traders, written for the lesson, show all three cases at "
                  "once: the weaver and the shepherd want each other's cloth and wool and "
                  "can trade directly; the butcher, the shoemaker and the tanner are a "
                  "ring like the one described next and can trade only through a money; and the "
                  "smith's iron is wanted by none of them, so he has no buyer here at "
                  "all. The lab counts the measure as one of the goods, as cattle were; if "
                  "money is a thirteenth thing outside the list, each of the twelve goods "
                  "has one price in it, and that is twelve."),
            ("p", "The same lab can say who can trade with whom, with traders written for "
                  "the lesson. In the preset <code>ring</code> the butcher has meat and "
                  "wants bread, the baker has bread and wants beer, and the brewer has beer "
                  "and wants meat. Take any two and one of them has what the other wants "
                  "but not the other way round, so no pair can trade directly: three "
                  "traders, three goods, and no exchange. All three can trade through a "
                  "money, because each has something that someone wants. Change one wish, as "
                  "in <code>one-match</code>, so the butcher wants bread and the baker wants "
                  "meat, and those two can trade directly, while the brewer is left out: "
                  "no one of the three wants his beer."),
            ("def", ("A common measure",
                     "A commodity in which every other good is priced, so that the rates of "
                     "exchange among many goods can be read off from a few. In this chapter "
                     "the common measure is also the thing that is handed over, the "
                     "&ldquo;instrument of commerce&rdquo;. Pricing and paying in it are "
                     "two jobs one object does.")),
            ("p", "Smith's answer to the difficulty is the prudent man who keeps by him "
                  "&ldquo;a certain quantity of some one commodity or other, such as he "
                  "imagined few people would be likely to refuse in exchange for the "
                  "produce of their industry&rdquo;. Then the examples: cattle in the rude "
                  "ages, so that Homer says the armour of Diomede cost nine oxen and that "
                  "of Glaucus a hundred; salt in Abyssinia; shells on the coast of India; "
                  "dried cod at Newfoundland; tobacco in Virginia; sugar in the West "
                  "Indies; and a village in Scotland where a workman may carry nails to the "
                  "baker's shop or the ale-house."),
            ("p", "Why metals? &ldquo;Metals can not only be kept with as little loss as any "
                  "other commodity, scarce any thing being less perishable than they are, but "
                  "they can likewise, without any loss, be divided into any number of "
                  "parts.&rdquo; The man who wants salt and has only cattle must buy a whole "
                  "ox's worth at a time, or two or three, because the ox cannot be divided "
                  "without loss. With metal he can &ldquo;proportion the quantity of the "
                  "metal to the precise quantity of the commodity which he had immediate "
                  "occasion for.&rdquo; Iron served the Spartans, copper the Romans, and "
                  "gold and silver all rich and commercial nations."),
            ("p", "Then the stamp. At first the metals were used in rude bars, with two "
                  "inconveniences, weighing and assaying. Nobody wants to weigh a "
                  "farthing's worth of goods. So it was found necessary &ldquo;to affix a "
                  "public stamp upon certain quantities of such particular metals&rdquo; as "
                  "were commonly used, hence coined money and the mints, institutions he "
                  "compares with the aulnagers and stamp-masters of cloth. The first "
                  "stamps certified fineness; the coin that covered both sides of the piece "
                  "was supposed to certify weight too, and could be taken by tale, that is "
                  "by counting, without weighing. Smith's stamp does not make the metal "
                  "money: money comes first, as a commodity chosen by custom, and the stamp "
                  "is a guarantee added to it."),
            ("p", "The denominations first named a weight, and Smith says so. The English "
                  "pound sterling in the time of Edward I &ldquo;contained a pound, Tower "
                  "weight, of silver of a known fineness&rdquo;. English, French and Scots "
                  "pennies &ldquo;contained all of them originally a real penny-weight of "
                  "silver&rdquo;, which he says was the twentieth part of an ounce and the "
                  "two hundred and fortieth part of a pound. That is why a pound was two "
                  "hundred and forty pence. The shilling, he says, was first a weight too, "
                  "but the pence in it varied, five at one time among the Saxons, until "
                  "from William the Conqueror's time the proportion of pound, shilling and "
                  "penny was the twenty and twelve it still is. Then comes the sentence that the next lessons use: "
                  "&ldquo;the avarice and injustice of princes and sovereign states, "
                  "abusing the confidence of their subjects, have by degrees diminished "
                  "the real quantity of metal, which had been originally contained in "
                  "their coins&rdquo;. The English pound and penny, he says, now contain "
                  "about a third of their original value, the Scots about a thirty-sixth "
                  "and the French about a sixty-sixth. The last lesson of this course "
                  "works it."),
            ("p", "Now the last third of the chapter. Smith tells his reader what he is "
                  "about to do, and defines the word he will use. &ldquo;The word VALUE, it "
                  "is to be observed, has two different meanings&rdquo;: value in use and "
                  "value in exchange. &ldquo;Nothing is more useful than water; but it "
                  "will purchase scarce any thing; scarce any thing can be had in exchange "
                  "for it. A diamond, on the contrary, has scarce any value in use; but a "
                  "very great quantity of other goods may frequently be had in exchange for "
                  "it.&rdquo; The economists of the 1870s, Jevons, Menger and Walras, "
                  "answered the puzzle by separating the usefulness of the whole supply of "
                  "water from the usefulness of one more glass of it; Smith, who has not "
                  "that distinction, simply sets the puzzle aside and goes on to exchange "
                  "value. Capital reads the same distinction between a thing's use and "
                  "its exchange in its lesson &lsquo;The Two Factors of a Commodity&rsquo;, "
                  "and the step from barter to a common equivalent in &lsquo;Exchange&rsquo;; "
                  "neither is repeated here."),
            ("p", "He then lays out three subjects for the next three chapters: what is "
                  "&ldquo;the real measure of this exchangeable value; or wherein consists "
                  "the real price of all commodities&rdquo;; what are the parts of which "
                  "that price is made up; and what makes the market price sometimes "
                  "differ from the natural price. This course takes the first of them, in "
                  "Chapter 5, and the next course the second and third. The story Smith "
                  "tells of money's origin is a conjecture, and the anthropologist "
                  "Caroline Humphrey wrote in 1985 that no economy run on barter alone had "
                  "ever been described, and David Graeber, in 2011, drawing on her and on "
                  "others, argued that credit and debt came before coin, which the "
                  "economists' story leaves out. The lab counts what the story implies for a market of "
                  "stated size, and takes no side on that."),
        ],
        "lab": ("wonkit", {
            "mode": "money",
            "view": "barter",
            "preset": "ring",
            "presets": [
                {"id": "ring",
                 "label": "Butcher, baker and brewer in a ring of wants, written for this lesson",
                 "goods": "meat beer bread",
                 "traders": "butcher, meat, bread; baker, bread, beer; brewer, beer, meat",
                 "expect": {
                          "wmoWithout": "3 ratios",
                          "wmoWith": "2 prices",
                          "wmoFewer": "1 quotation fewer",
                          "wmoDirect": "0: none",
                          "wmoViaMoney": "3: butcher, baker, brewer",
                          "wmoNoBuyer": "0: none",
                         }},
                {"id": "one-match",
                 "label": "The butcher and the baker want each other's goods, written for this lesson",
                 "goods": "meat beer bread",
                 "traders": "butcher, meat, bread; baker, bread, meat; brewer, beer, meat",
                 "expect": {
                          "wmoWithout": "3 ratios",
                          "wmoWith": "2 prices",
                          "wmoFewer": "1 quotation fewer",
                          "wmoDirect": "1: butcher–baker",
                          "wmoViaMoney": "0: none",
                          "wmoNoBuyer": "1: brewer",
                         }},
                {"id": "market-town",
                 "label": "Twelve goods and six traders in a town's market, written for this lesson",
                 "goods": "meat beer bread salt cloth shoes candles leather iron timber wool cheese",
                 "traders": "butcher, meat, shoes; shoemaker, shoes, leather; tanner, leather, meat; weaver, cloth, wool; shepherd, wool, cloth; smith, iron, timber",
                 "expect": {
                          "wmoWithout": "66 ratios",
                          "wmoWith": "11 prices",
                          "wmoFewer": "55 quotations fewer",
                          "wmoDirect": "1: weaver–shepherd",
                          "wmoViaMoney": "3: butcher, shoemaker, tanner",
                          "wmoNoBuyer": "1: smith",
                         }},
            ],
            "panel_title": "What exchange costs without a common measure",
            "panel_intro": (
                "A list of goods, and optionally who has what and wants what, go in. The "
                "lab counts the rates a market would have to quote with no measure and with "
                "one, and says which pairs of traders can deal directly."
            ),
        }),
        "steps_title": "Counting the rates and the trades",
        "steps_intro": "Four steps, for any list of goods and any set of traders.",
        "steps": [
            ("Count the goods",
             "Call the number n. Smith's three trades give three goods; a town's market may "
             "give a dozen or more."),
            ("Count the ratios with no measure",
             "Each pair of goods needs its own rate, and the number of pairs is "
             "`n·(n − 1)/2`. Write n times n minus one over two, and check it on three goods: "
             "three pairs."),
            ("Count them with a measure",
             "Choose one good to price all the others in. Then each other good needs one "
             "price, which is `n − 1`."),
            ("Find who can trade",
             "Two traders can deal directly only if each has what the other wants. A trader "
             "who has a good that someone wants can trade through a money, even if no one "
             "he can reach wants what he has to give."),
        ],
        "worked": {
            "title": "Twelve goods in a market-town",
            "intro": [
                "Take the third preset: meat, beer, bread, salt, cloth, shoes, candles, "
                "leather, iron, timber, wool and cheese. You want the number of rates the "
                "market would have to quote, and the number if one good is the measure.",
            ],
            "lines": [
                "n = 12",
                "pairs of goods:  12 · 11 / 2 = 66 rates",
                "one good as measure:  12 − 1 = 11 prices",
                "Smith's three trades:  3 · 2 / 2 = 3 rates, or 2",
            ],
            "after": [
                "Sixty-six rates against eleven prices, and the gap widens as the market "
                "grows: for a hundred goods it is 4,950 against 99. That is the saving a "
                "common measure makes, and it comes with the second saving that the same "
                "good is the one handed over, so no one needs the coincidence of wants.",
            ],
        },
        "quiz_title": "Exchange without and with a measure",
        "quiz": [
            {"q": "A market has six goods and no common measure. How many exchange rates "
                  "must it quote, one for each pair of goods?",
             "a": ["30", "15", "6", "5"],
             "c": 1,
             "why": "The pairs among six goods number `6·5/2 = 15`. Thirty counts each "
                    "pair twice, as if beef for beer and beer for beef were separate "
                    "rates; six is the number of goods; and five is what the market "
                    "would need with one good as the measure."},
            {"q": "The butcher has meat and wants bread, the baker has bread and wants "
                  "beer, and the brewer has beer and wants meat. How many pairs of them "
                  "can trade directly?",
             "a": ["0", "1", "2", "3"],
             "c": 0,
             "why": "In each pair one has what the other wants, but not the reverse: the "
                    "butcher's meat is wanted by the brewer, but the brewer's beer is not "
                    "wanted by the butcher. So no pair can trade, and all three need a "
                    "money. If any pair coincided, that pair could trade directly."},
            {"q": "According to Smith, why did men in all countries give the preference to "
                  "metals for the instrument of commerce?",
             "a": ["Metals were declared money by the sovereign",
                   "Metals were the most beautiful commodity",
                   "Metals keep with little loss, and can be divided without loss and joined "
                   "again by fusion",
                   "Metals were the only things everyone wanted for use"],
             "c": 2,
             "why": "Smith's reasons are durability and divisibility: nothing is less "
                    "perishable, and metal can be divided into any number of parts and "
                    "re-united by fusion. The stamp, which a public authority affixes, comes "
                    "later in his account. He does not say metals are beautiful or that "
                    "everyone wanted them for use."},
            {"q": "Which of these does Smith give as an example of a thing with great value "
                  "in use and little or none in exchange?",
             "a": ["A diamond", "Water", "Salt in Abyssinia", "A pound weight of silver"],
             "c": 1,
             "why": "&ldquo;Nothing is more useful than water; but it will purchase scarce "
                    "any thing&rdquo;. The diamond is the reverse: &ldquo;scarce any value "
                    "in use&rdquo; but great value in exchange. Salt and silver are his "
                    "examples of things that served as money, and neither is called a case "
                    "of the paradox."},
        ],
        "mistakes": [
            ("Thinking Smith says money was invented by law",
             "In his account the commodity comes first, chosen by prudent men over many "
             "ages, and the public stamp is added afterwards to save the trouble of "
             "weighing and assaying. The sovereign certifies the metal; the chapter does "
             "not have him create the money."),
            ("Reading n − 1 as a count of every price in an economy",
             "The lab counts the measure as one of the goods. If money is a further thing "
             "outside the list of goods, the goods need one price each, which is as many "
             "as there are goods. The saving comes from replacing pairs with one common "
             "term, and the exact figure depends on whether that term is counted."),
            ("Reading “little or no value in exchange” as “worth little”",
             "Smith's water has the greatest value in use. He is distinguishing two "
             "senses of value, and the puzzle he raises is why they come apart. He "
             "does not say water is unimportant, and he does not solve the puzzle here."),
        ],
        "standard": (
            "Finish when you can count the rates a market needs with and without a common "
            "measure and say who can trade directly.",
            "Given a list of goods, compute the exchange rates needed without a measure and "
            "with one; given traders' goods and wants, say which pairs coincide and which "
            "traders need a money."
        ),
        "note": (
            "The lab counts the pairs of goods and the traders who coincide, and the count "
            "is the same whether or not any society ever traded in that way. It cannot say "
            "whether money arose from barter, which is Smith's conjecture, repeated by "
            "later economists and doubted by later anthropologists, or whether a "
            "money of account came before coin. The traders' wants are written for "
            "the lesson, and in Smith's own case the butcher wants nothing the others have."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 970-1010 (rich or poor, toil and trouble, labour commanded),
    # l. 1011-1052 (the difficulty of measuring labour, why money is used),
    # l. 1053-1100 (silver varies, labour does not; the real price of labour),
    # l. 1223-1269 (Canton and London; same time and place).
    {
        "slug": "labour-the-real-measure",
        "title": "Labour, the Real Measure of Value",
        "module": "Book I, Chapter 5, first part · Of the Real and Nominal Price of Commodities",
        "one_line": "What a thing is worth is the labour it lets you command, because labour costs its owner the same toil in every age, and money is only its nominal price.",
        "summary": (
            "Smith says a man is rich or poor by the quantity of labour he can command, "
            "so labour, not money, is the real measure of exchangeable value. Compute a "
            "price in days of labour and see it move differently from the price in "
            "money: Smith's corn at twenty-five shillings and then fifty, a price that "
            "doubles while the wage doubles, and one that falls in money while it rises "
            "in labour."
        ),
        "key": [
            "real price = money price / price of a day",
            "money price: nominal; labour price: real",
            "rich = the labour you can command",
            "a day's toil costs the labourer the same",
            "same time and place: money measures exactly",
        ],
        "key_label": "Real and nominal in five lines",
        "concepts_intro": (
            "The first part of Chapter 5 states a thesis, explains why we do not "
            "actually measure by it, and argues that it is the only measure that holds "
            "still."
        ),
        "concepts": [
            ("Value is command over labour",
             "Once the work is divided, only a small part of a man's wants can be met by "
             "his own labour; he is rich or poor according to the quantity of other men's "
             "labour he can command or afford to purchase. The value of a commodity to "
             "the man who means to exchange it is the quantity of labour it enables him "
             "to command."),
            ("Real price is toil and trouble",
             "The real price of everything is the toil and trouble of acquiring it. What "
             "money or goods buy is bought by labour, as much as what we acquire by the "
             "toil of our own body. Their value to the owner is the toil they can save him "
             "and impose on others."),
            ("Labour does not vary in its own value",
             "Gold and silver vary with the fertility of the mines, so they cannot measure "
             "other things accurately. Equal quantities of labour are, to the labourer, "
             "always of equal value, because he lays down the same portion of his ease, "
             "liberty and happiness. Labour is the real price; money is the nominal."),
        ],
        "read_title": "The thesis, the difficulty and the standard",
        "read_intro": (
            "This is the chapter on which the rest of Book I leans, and also the one "
            "later economists argued with most. Read the thesis, and then read what Smith "
            "himself says about why it is hard to use."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 5.</strong> The opening: a man is rich or poor "
                  "&ldquo;according to the degree in which he can afford to enjoy the "
                  "necessaries, conveniencies, and amusements of human life&rdquo;. But once "
                  "the division of labour is complete, only a small part of these can come "
                  "from his own labour, and so he must be rich or poor &ldquo;according to "
                  "the quantity of that labour which he can command, or which he can afford "
                  "to purchase&rdquo;. From which: &ldquo;Labour therefore, is the real "
                  "measure of the exchangeable value of all commodities.&rdquo;"),
            ("p", "<em>Command</em> is the word to hold on to. The value of a thing to "
                  "its owner, if he means to exchange it, is the labour it lets him buy. "
                  "This is the thesis of the chapter, and Smith repeats it in another form: "
                  "&ldquo;The real price of every thing, what every thing really costs to "
                  "the man who wants to acquire it, is the toil and trouble of acquiring "
                  "it. What every thing is really worth to the man who has acquired it and "
                  "who wants to dispose of it, or exchange it for something else, is the "
                  "toil and trouble which it can save to himself, and which it can impose "
                  "upon other people.&rdquo; Notice that he means two things by labour "
                  "without separating them: the toil one spends to get a thing, and the "
                  "toil one can make others spend for it."),
            ("p", "Smith then says why he is not describing what we do. &ldquo;It is often "
                  "difficult to ascertain the proportion between two different quantities of "
                  "labour&rdquo;, because the time spent will not alone settle it. Hardship "
                  "and ingenuity count: there may be more labour in an hour's hard work "
                  "than in two hours' easy business. But &ldquo;it is not easy to find any "
                  "accurate measure either of hardship or ingenuity&rdquo;, and the "
                  "allowance is made &ldquo;by the higgling and bargaining of the "
                  "market&rdquo;, according to a rough equality that is good enough for "
                  "common business. And in practice a good is exchanged for money more often "
                  "than for labour, so the butcher says his meat is worth three-pence or "
                  "fourpence a pound, and not so many pounds of bread. So the nominal price "
                  "is the one we use."),
            ("p", "Why not use it as the measure? Because gold and silver &ldquo;like every "
                  "other commodity, vary in their value&rdquo;. The mines of America "
                  "&ldquo;reduced, in the sixteenth century, the value of gold and silver in "
                  "Europe to about a third of what it had been before.&rdquo; And &ldquo;a "
                  "commodity which is itself continually varying in its own value, can never "
                  "be an accurate measure of the value of other commodities&rdquo;. "
                  "Labour does not vary. &ldquo;Equal quantities of labour, at all times and "
                  "places, may be said to be of equal value to the labourer. In his "
                  "ordinary state of health, strength, and spirits; in the ordinary degree "
                  "of his skill and dexterity, he must always lay down the same portion of "
                  "his ease, his liberty, and his happiness.&rdquo; So: &ldquo;It is their "
                  "real price; money is their nominal price only.&rdquo;"),
            ("def", ("Real price and nominal price",
                     "The real price of a thing is the quantity of labour it costs or "
                     "commands, and the nominal price is the quantity of money it sells for. "
                     "In the lab the real price is the money price divided by the money "
                     "price of the measure, here a day's labour, so it is a number of days. "
                     "Smith uses the same two words of labour itself: its real price is the "
                     "necessaries and conveniencies given for it, its nominal price the "
                     "money.")),
            ("p", "The lab does the division. In the preset <code>corn-doubles</code>, a "
                  "quarter of corn is at 25 shillings in an ordinary year and 50 in a dear "
                  "one, which are Smith's figures; the price of a day's labour, held at one "
                  "shilling, is written for the lesson, and Smith's own point is that "
                  "the money price of labour does not follow the year's price of corn. The "
                  "real price of a quarter is `25/1 = 25` days, then `50/1 = 50`: the "
                  "money price and the real price both rise by a hundred per cent. In "
                  "<code>both-double</code>, written for the lesson, silver is cheapened so "
                  "that the money price of the good doubles from 10 shillings to 20 and "
                  "so does the wage, from a shilling to two: the real price stays at 10 "
                  "days, though the money price rose by a hundred per cent. And in "
                  "<code>money-falls</code>, also the lesson's, the money price falls from "
                  "10 shillings to 8 while the wage falls from one shilling to sixpence: "
                  "the real price goes from 10 days to 16, so the good has become dearer in "
                  "labour though cheaper in money. The lab prints whether the two moved the "
                  "same way."),
            ("p", "Smith adds a point that people who apply the thesis forget. To the "
                  "employer, labour appears dear in one case and cheap in the other, because "
                  "he buys it with more or fewer goods; but &ldquo;it is the goods which are "
                  "cheap in the one case, and dear in the other&rdquo;. The labourer is "
                  "rich or poor in proportion to the real, not the nominal, price of his "
                  "labour, and its real price consists in &ldquo;the quantity of the "
                  "necessaries and conveniencies of life which are given for it&rdquo;."),
            ("p", "And then a limit Smith sets on the thesis himself. In buying and "
                  "selling, the distinction is of none: &ldquo;At the same time and place "
                  "&hellip; money is the exact measure of the real exchangeable value of all "
                  "commodities. It is so, however, at the same time and place only.&rdquo; "
                  "The Canton example makes the point. Half an ounce of silver at Canton may "
                  "command more labour and necessaries than an ounce at London. A London "
                  "merchant who buys at Canton for half an ounce what he can sell at London "
                  "for an ounce gains a hundred per cent, and it is of no importance to "
                  "him that half an ounce commanded more at Canton, because an ounce at "
                  "London will give him the command of double what half an ounce could. "
                  "That is why money prices are the ones attended to."),
            ("p", "Smith's critics took the thesis seriously, and the strongest one is "
                  "Ricardo, writing in 1817. He said Smith had run together two things: "
                  "the labour a good costs to make, and the labour it commands in exchange. "
                  "The first stays the same when wages rise; the second does not, because "
                  "a good that is worth the same labour to make will command less "
                  "labour when labour is dearer. So the labour a thing commands cannot be "
                  "a fixed standard, and Ricardo took the labour spent on making it. The "
                  "difference matters in the lab: the real price here is a quantity of "
                  "labour commanded, and a rise in the wage lowers it. Where Capital takes "
                  "up what it means to speak of the price of labour at all, it is in the "
                  "lesson &lsquo;The Value of Labour-Power Becomes Wages&rsquo;, and not "
                  "repeated here."),
            ("p", "That leaves a practical problem: the price of labour at distant times "
                  "and places &ldquo;can scarce ever be known with any degree of "
                  "exactness&rdquo;, so Smith proposes to use the price of corn. The next "
                  "lesson reads what he says it can and cannot do."),
        ],
        "lab": ("wonkit", {
            "mode": "price",
            "view": "real",
            "money_unit": "s",
            "measure_unit": "days of labour",
            "preset": "corn-doubles",
            "presets": [
                {"id": "corn-doubles",
                 "label": "A quarter of corn at Smith's 25s and 50s, a day's labour at 1s (the wage is written for this lesson)",
                 "years": "ordinary-year, 25, 1; dear-year, 50, 1",
                 "expect": {
                          "wprReal": "ordinary-year 25 days of labour; dear-year 50 days of labour",
                          "wprMoneyCh": "ordinary-year → dear-year: +1 = +100%",
                          "wprRealCh": "ordinary-year → dear-year: +1 = +100%",
                          "wprWay": "the same way: both rose",
                         }},
                {"id": "both-double",
                 "label": "A good and the wage both double in money, written for this lesson",
                 "years": "before, 10, 1; after, 20, 2",
                 "expect": {
                          "wprReal": "before 10 days of labour; after 10 days of labour",
                          "wprMoneyCh": "before → after: +1 = +100%",
                          "wprRealCh": "before → after: 0 = 0%",
                          "wprWay": "not the same way: the money price rose and the real price held",
                         }},
                {"id": "money-falls",
                 "label": "The money price falls while the wage falls faster, written for this lesson",
                 "years": "before, 10, 1; after, 8, 1/2",
                 "expect": {
                          "wprReal": "before 10 days of labour; after 16 days of labour",
                          "wprMoneyCh": "before → after: −1/5 = −20%",
                          "wprRealCh": "before → after: +3/5 = +60%",
                          "wprWay": "not the same way: the money price fell and the real price rose",
                         }},
            ],
            "panel_title": "A price in money and a price in labour",
            "panel_intro": (
                "In each year the money price of a good and the money price of a day's "
                "labour go in. The lab divides to give the real price in days, and says "
                "whether the money price and the real price moved the same way."
            ),
        }),
        "steps_title": "Turning a money price into a labour price",
        "steps_intro": "Four steps, for any good and any pair of years.",
        "steps": [
            ("Take the money price",
             "The price of the good in the year, in shillings, silver or any other money, "
             "which Smith calls its nominal price."),
            ("Take the price of the measure",
             "What a day of labour was paid in the same year, in the same money. Smith "
             "notes that at distant times this is rarely known."),
            ("Divide",
             "Money price over the price of a day is the real price, in days of labour. "
             "A change in the unit of money cancels out of it."),
            ("Compare the two changes",
             "Work out the percentage change of each from the first year to the last. If "
             "the money price rose and the real price did not, the change was in the "
             "money."),
        ],
        "worked": {
            "title": "A price that doubles in money and stays still in labour",
            "intro": [
                "Take the second preset. A good costs 10 shillings and a day's labour 1 "
                "shilling; later the good costs 20 shillings and a day's labour 2. You want "
                "the real price each year and each change.",
            ],
            "lines": [
                "before:  10 / 1 = 10 days",
                "after:  20 / 2 = 10 days",
                "money price:  (20 − 10) / 10 = 100%",
                "real price:  (10 − 10) / 10 = 0%",
            ],
            "after": [
                "The money price doubled and the labour price did not move. Smith would say "
                "the shilling had become worth half as much labour, which is a change in "
                "the money. In the first preset, with the wage held and the corn price "
                "doubled, both moved: the corn really had become dearer.",
            ],
        },
        "quiz_title": "Real and nominal price",
        "quiz": [
            {"q": "A quarter of corn sells for 50 shillings and a day's labour for 1 shilling. "
                  "What is the real price of the quarter, in Smith's sense?",
             "a": ["50 days of labour", "25 days of labour", "1/50 of a day", "51 days of labour"],
             "c": 0,
             "why": "The real price is the labour the corn commands: `50/1 = 50` days. "
                    "Twenty-five is the real price in the ordinary year, when the corn was "
                    "at 25 shillings. One fiftieth inverts the division, and 51 adds "
                    "instead of dividing."},
            {"q": "Why does Smith say equal quantities of labour are always of equal value "
                  "to the labourer?",
             "a": ["Because wages never change",
                   "Because labour always produces the same quantity of goods",
                   "Because the labourer must always lay down the same portion of his ease, "
                   "liberty and happiness",
                   "Because labour is bought with gold, which does not vary"],
             "c": 2,
             "why": "The reason Smith gives is the sacrifice: in his ordinary health and "
                    "skill the labourer &ldquo;must always lay down the same portion of his "
                    "ease, his liberty, and his happiness&rdquo;. It is the goods he "
                    "receives that vary, not the labour. And gold, he says, does vary."},
            {"q": "A London merchant buys goods at Canton for half an ounce of silver and sells "
                  "them in London for an ounce. By Smith's reckoning, what does he gain?",
             "a": ["Fifty per cent", "A hundred per cent", "Two hundred per cent",
                   "Nothing, because half an ounce commands more labour at Canton"],
             "c": 1,
             "why": "He doubles his silver, &ldquo;a hundred per cent&rdquo;, and Smith says "
                    "it is of no importance to him that half an ounce commanded more labour "
                    "at Canton. The gain is in money and the merchant's concern is the money "
                    "price. Fifty per cent would be the gain if the selling price were only "
                    "three-quarters of an ounce."},
            {"q": "In the preset where a good's money price doubles from 10s to 20s while a "
                  "day's wage doubles from 1s to 2s, what happens to its real price?",
             "a": ["It doubles", "It halves", "It stays at 10 days", "It falls to 5 days"],
             "c": 2,
             "why": "`10/1 = 10` before and `20/2 = 10` after. The doubling of the money "
                    "price is matched by the doubling of the measure's money price, which is "
                    "the situation Smith describes when the value of silver has fallen."},
        ],
        "mistakes": [
            ("Thinking the real price moves whenever the money price does",
             "In the <code>both-double</code> preset the money price rises by a hundred per "
             "cent and the real price does not move at all, because the measure's own "
             "money price moved with it. A change that is in the money cancels out of the "
             "division."),
            ("Reading Smith as saying money prices do not matter",
             "He says at the same time and place money is the exact measure, and that the "
             "merchant who carries goods between places has nothing to consider but the "
             "money price. The real price is wanted when we compare across times or "
             "places, which is what the next two lessons do."),
            ("Confusing the real price of a good with the real price of labour",
             "Smith uses the words of both. The real price of a good is the labour it "
             "commands. The real price of labour is the necessaries and conveniencies "
             "given for it. The lab's measure is a day of labour, and nothing in it "
             "says what a day was worth in goods."),
        ],
        "standard": (
            "Finish when you can compute a real price in days of labour and say whether "
            "a change in money price was a change in the real price.",
            "Given a good's money price and the money price of a day's labour in two years, "
            "compute the real price in each, the percentage changes in money and in "
            "labour, and say whether they moved the same way."
        ),
        "note": (
            "The lab divides one money figure by another, and what it gives is a quantity "
            "of labour commanded. It cannot show that this is a stable measure: that is "
            "Smith's thesis, and Ricardo's objection is that the quantity commanded depends "
            "on the wage, so it is not one of labour spent. The wage per day is written "
            "for the lesson, and a day of labour is treated as one unit whatever its "
            "hardship or skill, which Smith says is the difficulty."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 1101-1127 (a perpetual rent reserved in money), l. 1128-1154
    # (the colleges' rents), l. 1155-1216 (corn and silver as measures),
    # l. 1217-1222 (the use of the distinction).
    {
        "slug": "corn-rents-and-money-rents",
        "title": "Corn Rents and Money Rents",
        "module": "Book I, Chapter 5, middle · Of the Real and Nominal Price of Commodities",
        "one_line": "Corn holds its value in labour better over centuries and silver holds it better over years, so a perpetual rent is safer reserved in corn.",
        "summary": (
            "If labour is the real measure but nobody records its price, what stands in "
            "for it? Smith argues for corn over centuries and silver over years. Compute "
            "what a fixed money rent comes to in corn as the price of corn rises, the "
            "college rents that fell to a quarter of their old value, and the corn "
            "rent that doubles its worth in a dear year."
        ),
        "key": [
            "real rent = money rent / price of a quarter",
            "money rent falls as corn gets dearer",
            "corn better by the century",
            "silver better by the year",
            "college rents: near a fourth of their value",
        ],
        "key_label": "Corn and silver in five lines",
        "concepts_intro": (
            "This stretch of Chapter 5 is Smith's practical advice. A perpetual rent "
            "should be reserved in corn, and the reason is the thesis of the last lesson "
            "put to work."
        ),
        "concepts": [
            ("Two ways a money rent can fall",
             "A rent fixed in a sum of money can lose value because the coin of the same "
             "name contains less metal, and because the same weight of metal buys less. "
             "Even a rent fixed in ounces of silver suffers from the second."),
            ("Corn as the better long measure",
             "Equal quantities of labour are bought, over long periods, more nearly by "
             "equal quantities of corn, the subsistence of the labourer, than by equal "
             "quantities of silver. Smith adds that even corn does not do it exactly."),
            ("Silver as the better short measure",
             "The money price of labour follows the average price of corn and not the "
             "price of this year's harvest, and the value of silver seldom varies much "
             "from year to year. So over a year silver is the better measure of the "
             "labour a thing commands, and corn the worse."),
        ],
        "read_title": "The perpetual rent, the colleges and the two measures",
        "read_intro": (
            "The passage runs from a rule of conveyancing to a theory of the measure of "
            "value. Read the college rents closely, since Smith does the arithmetic in a "
            "sentence."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 5.</strong> The distinction of real and nominal "
                  "price, Smith says, is &ldquo;not a matter of mere speculation, but may "
                  "sometimes be of considerable use in practice&rdquo;. His example is a "
                  "landed estate sold with a perpetual rent reserved. If the rent is to be "
                  "always of the same value, the family it was reserved for should not "
                  "take it in a particular sum of money, whose value would vary in two "
                  "ways: &ldquo;first, to those which arise from the different quantities "
                  "of gold and silver which are contained at different times in coin of the "
                  "same denomination; and, secondly, to those which arise from the "
                  "different values of equal quantities of gold and silver at different "
                  "times.&rdquo;"),
            ("p", "On the first: &ldquo;Princes and sovereign states have frequently fancied "
                  "that they had a temporary interest to diminish the quantity of pure "
                  "metal contained in their coins; but they seldom have fancied that they "
                  "had any to augment it.&rdquo; On the second, he writes that the "
                  "discovery of America diminished the value of silver, and that this "
                  "diminution is &ldquo;commonly supposed, though I apprehend without any "
                  "certain proof&rdquo;, to be still going on. A rent in ounces of silver "
                  "escapes the first and not the second."),
            ("p", "Then the case, which is a figure and not a theory. &ldquo;By the 18th of "
                  "Elizabeth, it was enacted, that a third of the rent of all college "
                  "leases should be reserved in corn, to be paid either in kind, or "
                  "according to the current prices at the nearest public market.&rdquo; "
                  "The money arising from the corn third, he says, &ldquo;though "
                  "originally but a third of the whole, is, in the present times, "
                  "according to Dr. Blackstone, commonly near double of what arises from "
                  "the other two-thirds.&rdquo; So the old money rents of the colleges "
                  "&ldquo;must, according to this account, have sunk almost to a fourth "
                  "part of their ancient value&rdquo;."),
            ("p", "Check Smith's sum with the lab's first preset, <code>college-rent</code>. "
                  "Say a college's whole rent was 60 shillings: a third, 20 shillings, in "
                  "corn, and 40 in money. At 5 shillings a quarter the corn third was 4 "
                  "quarters. In Smith's day, he says, the corn third brings near double what "
                  "the money two-thirds bring, so near 80 shillings, which for the same 4 "
                  "quarters means 20 shillings a quarter: corn four times as dear. The "
                  "money two-thirds are still 40 shillings, and the lab shows what they "
                  "buy: 8 quarters at the first price, 2 at the second, "
                  "a fall of 75 per cent, so the money rent is worth `1/4` of what it was, "
                  "Smith's fourth. The proportion between the corn third and the money "
                  "two-thirds is Blackstone's as Smith reports it, and the fourfold rise in "
                  "corn is what follows from it. The shilling figures are written for the "
                  "lesson."),
            ("p", "Why is it not the coin? Because &ldquo;since the reign of Philip and "
                  "Mary, the denomination of the English coin has undergone little or no "
                  "alteration, and the same number of pounds, shillings, and pence, have "
                  "contained very nearly the same quantity of pure silver. This degradation, "
                  "therefore, in the value of the money rents of colleges, has arisen "
                  "altogether from the degradation in the price of silver.&rdquo; In "
                  "Scotland and France, he adds, where the coin had changed more, the two "
                  "causes combined and some ancient rents were reduced almost to nothing."),
            ("p", "So the rule: &ldquo;Equal quantities of labour will, at distant times, be "
                  "purchased more nearly with equal quantities of corn, the subsistence of "
                  "the labourer, than with equal quantities of gold and silver, or, "
                  "perhaps, of any other commodity.&rdquo; The reason is that any other "
                  "commodity, at a given time, buys labour in proportion to the subsistence "
                  "it will buy; a rent in corn is liable only to the variation in the "
                  "labour a quantity of corn will buy, while a rent in anything else is liable "
                  "to that and to the variation in the corn that thing buys. Smith qualifies "
                  "it at once: &ldquo;even equal quantities of corn will not do it "
                  "exactly&rdquo;, because the subsistence of the labourer &ldquo;is very "
                  "different upon different occasions; more liberal in a society advancing "
                  "to opulence, than in one that is standing still&rdquo;."),
            ("p", "The preset <code>century</code>, written for the lesson, shows the "
                  "long run: a money rent of 100 shillings, with a quarter of corn at 20 "
                  "shillings, then 40, then 80 as each century passes. The rent is worth 5 "
                  "quarters, then `5/2`, then `5/4`. The price of corn in the three "
                  "centuries is the lesson's, not Smith's. For the short run Smith's own "
                  "figures serve: the temporary price of corn &ldquo;may frequently be "
                  "double one year of what it had been the year before, or fluctuate, for "
                  "example, from five-and-twenty to fifty shillings the quarter&rdquo;. In "
                  "the preset <code>dear-year</code> a money rent of 250 shillings buys 10 "
                  "quarters at 25 and 5 at 50, so by the corn measure it has halved in a "
                  "year. By labour it has not: the money price of labour, Smith says, "
                  "follows the average price of corn and not the year's, so with a day's "
                  "labour at a shilling (the lesson's figure) the money rent commands 250 "
                  "days in both years, while a corn rent of ten quarters, worth 250 "
                  "shillings and then 500, commands 250 days and then 500. That is why, "
                  "from year to year, the silver rent is the steadier."),
            ("def", ("The two measures, by period",
                     "Over a century, corn is the better measure of the labour a thing "
                     "commands, because the value of silver can change greatly while a "
                     "labourer's subsistence changes little. Over a year, silver is the better, "
                     "because the money price of labour follows the ordinary price of corn "
                     "and the value of silver seldom changes in a year. Smith's rule: "
                     "&ldquo;From century to century, corn is a better measure than silver "
                     "&hellip; From year to year, on the contrary, silver is a better measure than "
                     "corn.&rdquo;")),
            ("p", "Two things limit the advice. First, Smith himself says that for ordinary "
                  "buying and selling the distinction is of no use. Second, a single "
                  "commodity is only a stand-in. The other answer is a basket of goods: the "
                  "index number, which had forerunners in the eighteenth century and which "
                  "W. S. Jevons used in 1863 to measure the "
                  "fall in the value of gold after the Californian and Australian "
                  "discoveries. A basket answers some of Smith's difficulties and has its own, "
                  "since it needs a choice of what goes in it and in what proportion. "
                  "The lab holds to Smith's single measure."),
            ("p", "That leaves the measure itself. The next lesson turns to the metals and "
                  "the coin, and to what happens to every figure in this lesson when a "
                  "sovereign changes what the coin contains."),
        ],
        "lab": ("wonkit", {
            "mode": "price",
            "view": "real",
            "money_unit": "s",
            "measure_unit": "quarters of corn",
            "preset": "college-rent",
            "presets": [
                {"id": "college-rent",
                 "label": "The money two-thirds of a college rent, 40s, as corn goes from 5s to 20s a quarter (Smith's near double gives the fourfold rise; the shillings are written for this lesson)",
                 "years": "1576, 40, 5; 1776, 40, 20",
                 "expect": {
                          "wprReal": "1576 8 quarters of corn; 1776 2 quarters of corn",
                          "wprMoneyCh": "1576 → 1776: 0 = 0%",
                          "wprRealCh": "1576 → 1776: −3/4 = −75%",
                          "wprWay": "not the same way: the money price held and the real price fell",
                         }},
                {"id": "century",
                 "label": "A fixed money rent of 100s as corn goes from 20s to 80s a quarter, written for this lesson",
                 "years": "century-one, 100, 20; century-two, 100, 40; century-three, 100, 80",
                 "expect": {
                          "wprReal": "century-one 5 quarters of corn; century-two 5/2 = 2.50 quarters of corn; century-three 5/4 = 1.25 quarters of corn",
                          "wprMoneyCh": "century-one → century-three: 0 = 0%",
                          "wprRealCh": "century-one → century-three: −3/4 = −75%",
                          "wprWay": "not the same way: the money price held and the real price fell",
                         }},
                {"id": "dear-year",
                 "label": "A money rent of 250s against corn at Smith's 25s and 50s the quarter (the rent is written for this lesson)",
                 "years": "ordinary-year, 250, 25; dear-year, 250, 50",
                 "expect": {
                          "wprReal": "ordinary-year 10 quarters of corn; dear-year 5 quarters of corn",
                          "wprMoneyCh": "ordinary-year → dear-year: 0 = 0%",
                          "wprRealCh": "ordinary-year → dear-year: −1/2 = −50%",
                          "wprWay": "not the same way: the money price held and the real price fell",
                         }},
            ],
            "panel_title": "A rent in money and in corn",
            "panel_intro": (
                "In each year the money value of a rent and the money price of a quarter "
                "of corn go in. The lab divides and says how much corn the rent buys."
            ),
        }),
        "steps_title": "What a fixed rent is worth in corn",
        "steps_intro": "Four steps, for a rent and any number of dates.",
        "steps": [
            ("Fix the rent in money",
             "A rent reserved in a sum of money stays the same figure at every date, "
             "whatever happens to the value of money. That is the point of the example."),
            ("Take the price of corn at each date",
             "A quarter's money price in each year. For a rent reserved in corn, the money "
             "figure is the quarters times that price."),
            ("Divide",
             "Rent over the price of a quarter is the quarters the rent buys. This is the "
             "rent's real value in the measure of the century."),
            ("Compare dates, and compare measures",
             "Set the first date against the last. Then ask what the same rent is worth in "
             "days of labour, which is the measure for a year and not a century."),
        ],
        "worked": {
            "title": "A money rent as corn gets dearer",
            "intro": [
                "Take the second preset. A rent of 100 shillings is fixed for three centuries. "
                "A quarter of corn costs 20 shillings, then 40, then 80. You want what the "
                "rent buys in each.",
            ],
            "lines": [
                "century one:  100 / 20 = 5 quarters",
                "century two:  100 / 40 = 5/2 quarters",
                "century three:  100 / 80 = 5/4 quarters",
                "change, first to last:  (5/4 − 5) / 5 = −75%",
            ],
            "after": [
                "The money figure never changed and the rent lost three quarters of its "
                "worth in corn. Smith's colleges, whose money two-thirds sank to a fourth "
                "of their old value, are the same arithmetic with a fourfold price.",
            ],
        },
        "quiz_title": "Rents in money and in corn",
        "quiz": [
            {"q": "Smith says the corn third of a college rent now brings near double what "
                  "the money two-thirds bring. By about what factor has the price of corn "
                  "risen since the statute?",
             "a": ["2", "3", "4", "6"],
             "c": 2,
             "why": "If the whole rent was 3 units, the corn third was worth 1 and the money "
                    "two-thirds 2. Now the corn third is near double 2, which is 4, so the "
                    "corn has become four times as dear. Two would be the ratio of the two "
                    "parts, not the rise in the price."},
            {"q": "A fixed rent of 100 shillings buys 5 quarters when corn is 20 shillings. "
                  "How many does it buy when corn is 80 shillings?",
             "a": ["1/4 of a quarter", "4 quarters", "5 quarters", "5/4 quarters"],
             "c": 3,
             "why": "`100/80 = 5/4` quarters. Four quarters would be the price quadrupling in "
                    "the wrong direction, and five is the original figure."},
            {"q": "According to Smith, which is the better measure of the labour a thing "
                  "commands from year to year?",
             "a": ["Corn, because it is the subsistence of the labourer",
                   "Silver, because it seldom varies much from year to year",
                   "Gold, because it is the dearer metal",
                   "Neither, because labour cannot be measured"],
             "c": 1,
             "why": "Smith: &ldquo;From year to year, on the contrary, silver is a better "
                    "measure than corn&rdquo;. The money price of labour follows the "
                    "average price of corn, not the year's, and silver's value seldom "
                    "varies from year to year. Corn is the better measure from century to "
                    "century."},
            {"q": "Why does Smith say the fall in the value of the colleges' money rents "
                  "has arisen altogether from the degradation in the price of silver?",
             "a": ["Because the colleges lent the money at a loss",
                   "Because the English coin's denomination had been little altered since "
                   "Philip and Mary",
                   "Because the corn rents were paid in kind",
                   "Because the statute fixed the price of corn"],
             "c": 1,
             "why": "Since Philip and Mary the same number of pounds, shillings and pence had "
                    "contained very nearly the same pure silver, so the coin was not the "
                    "cause. The fall in the rents had therefore to come from the fall in "
                    "the value of silver itself, and the statute did not fix a price."},
        ],
        "mistakes": [
            ("Blaming the coin when the silver has cheapened",
             "Smith's college rents lost three-quarters of their worth with the English "
             "coin unchanged. A rent in the same name of money can lose value without any "
             "debasement, and a rent in ounces of silver cannot be protected from it."),
            ("Thinking a corn rent is fixed in value",
             "Smith says corn is better over centuries, and he adds that it is not exact, "
             "since the labourer's subsistence differs between a growing and a stagnant "
             "society. From year to year a corn rent's worth in labour can double: the "
             "<code>dear-year</code> preset shows the other side of it, a money rent "
             "that halves in corn, so ten quarters of corn rent are worth twice the "
             "money, and with the wage steady twice the labour."),
            ("Taking one measure to be the right one for all periods",
             "Corn serves for the century and silver for the year, and Smith says it in "
             "so many words. Choosing the measure is part of the problem, and the "
             "lab's measure is whichever the preset names."),
        ],
        "standard": (
            "Finish when you can compute what a fixed rent buys in corn at two prices and "
            "say which measure suits which period.",
            "Given a rent in money and the price of a quarter of corn at two dates, compute "
            "the rent in quarters and its change, and say why Smith prefers corn to silver "
            "over a century and silver to corn over a year."
        ),
        "note": (
            "The lab divides and compares. It cannot say that corn is the better "
            "long-run measure, which depends on the labourer's subsistence changing "
            "little, and Smith says it changes. Blackstone's near double is second-hand, "
            "the quarters of corn and the rents in the century preset are the lesson's "
            "figures, and what the colleges actually paid in 1576 or in 1776 is a "
            "question for the records."
        ),
    },
    # ---------------------------------------------------------------- 04
    # PSU text l. 1270-1297 (the metals as money), l. 1298-1347 (the standard and
    # the legal ratio), l. 1348-1409 (copper pence, the mint prices), l. 1410-1479
    # (bullion and coin), l. 1520-1549 (the accuracy of money). The fall of the
    # pound is from l. 876-925.
    {
        "slug": "gold-silver-and-copper-coin",
        "title": "Gold, Silver and Copper Coin",
        "module": "Book I, Chapter 5, end · Of the Real and Nominal Price of Commodities",
        "one_line": "A coin is a measure only as far as it holds the metal it names, and a prince who lessens that metal pays his debts with less than he owes.",
        "summary": (
            "The end of Chapter 5 is about the coin itself: which metal is the standard, "
            "what the law makes a guinea worth in shillings, and what the mint will give "
            "for an ounce. Compute the silver in a penny as the pound is debased, what "
            "the first period's pound comes to in later pence, and what a creditor paid "
            "the same sum in the new coin loses."
        ),
        "key": [
            "silver per penny: first coined / later coined",
            "a creditor paid in new coin gets less silver",
            "silver: 62 shillings to the pound weight",
            "gold: 21 shillings the guinea, by law",
            "worn coin: price follows what it contains",
        ],
        "key_label": "The coin in five lines",
        "concepts_intro": (
            "Three metals are coined in England and one of them is the standard. This "
            "last section of Chapter 5 is dense with figures, and what matters in them "
            "is a handful of ideas."
        ),
        "concepts": [
            ("One metal is the standard",
             "Commercial nations coin gold for large payments, silver for moderate ones "
             "and copper for small, but keep their accounts in one, usually the first they "
             "used. In England the accounts are in silver, and so the pound sterling is "
             "a sum of silver, whatever the guineas are."),
            ("The law fixes a ratio, the market tests it",
             "A public law can declare that a guinea shall be worth one-and-twenty "
             "shillings. While the ratio holds, which metal is the standard is little "
             "more than a nominal distinction; when it is changed the debts written in "
             "silver need the same silver and different amounts of gold."),
            ("A coin is a measure only if it holds its weight",
             "The money of a country is an accurate measure of value just as the coin is "
             "agreeable to its standard. Worn coin makes the measure uncertain, as "
             "uneven weights do, and the prices of goods adjust to what coin on average "
             "contains."),
        ],
        "read_title": "The standard, the ratio, the mint and the debased coin",
        "read_intro": (
            "This is the most technical part of the chapter. Read for the three "
            "arguments in the concepts above, and take the figures as the lab's data."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 5.</strong> &ldquo;In the progress of industry, "
                  "commercial nations have found it convenient to coin several different "
                  "metals into money; gold for larger payments, silver for purchases of "
                  "moderate value, and copper, or some other coarse metal, for those of "
                  "still smaller consideration.&rdquo; But they &ldquo;have always, "
                  "however, considered one of those metals as more peculiarly the measure "
                  "of value than any of the other two&rdquo;, usually the one they used "
                  "first. The Romans, who had copper for centuries, kept accounts in "
                  "copper even after they coined silver. In England &ldquo;all accounts "
                  "are kept, and the value of all goods and of all estates is generally "
                  "computed, in silver&rdquo;."),
            ("p", "When the law fixes a ratio of the metals, the standard is a matter of "
                  "accounting. A guinea, say, is declared to be worth one-and-twenty "
                  "shillings. If it were reduced to twenty or raised to two-and-twenty, "
                  "&ldquo;the greater part of payments could in either case be made with "
                  "the same quantity of silver money as before; but would require very "
                  "different quantities of gold money; a greater in the one case, and a "
                  "smaller in the other&rdquo;. Silver would then appear the more "
                  "invariable. And yet Mr Drummond's notes for five-and-twenty or fifty "
                  "guineas would still be payable with the same guineas, and, in "
                  "payment of such a note, gold would appear invariable and silver "
                  "vary. Smith says the difference is &ldquo;altogether owing to the "
                  "custom of keeping accounts&rdquo;. A debt of 42 shillings, with the "
                  "guinea at 21, is two guineas; with the guinea reduced to 20 it is "
                  "`42/20`, or two and one-tenth."),
            ("p", "The most valuable metal regulates the value of the whole coin. His "
                  "illustration is the copper penny: twelve copper pence &ldquo;contain "
                  "half a pound avoirdupois of copper, of not the best quality, which, "
                  "before it is coined, is seldom worth seven-pence in silver&rdquo;, yet "
                  "because by regulation twelve of them exchange for a shilling, "
                  "&ldquo;they are in the market considered as worth a shilling&rdquo;. "
                  "Likewise, one-and-twenty worn and defaced shillings were considered "
                  "equal to a guinea, because the gold coin, less degraded, regulated "
                  "the silver."),
            ("p", "Then the mint. &ldquo;In the English mint, a pound weight of gold is "
                  "coined into forty-four guineas and a half, which at one-and-twenty "
                  "shillings the guinea, is equal to forty-six pounds fourteen shillings "
                  "and sixpence. An ounce of such gold coin, therefore, is worth "
                  "£ 3:17:10½ in silver.&rdquo; The figures check: `44½ × 21` is 934½ "
                  "shillings, which is 46 pounds and 14½ shillings, and a twelfth of it is "
                  "77⅞ shillings, which is £3 17s 10½d. And for silver, &ldquo;a pound "
                  "weight of standard silver bullion is coined into sixty-two "
                  "shillings&rdquo;, so five shillings and twopence an ounce is, he says, "
                  "the mint price of silver: sixty-two "
                  "shillings over twelve ounces is five and one-sixth, which is 5s 2d. The "
                  "mint charges nothing for coining, so a man who brings an ounce of bullion "
                  "gets an ounce of coin back."),
            ("p", "A word on the ratio of the metals in England. Smith says that in the "
                  "market of Europe an ounce of fine gold exchanges for about fourteen "
                  "ounces of fine silver, but in the English coin for about fifteen: the "
                  "English coin rates silver somewhat below its worth and gold above it. "
                  "He draws the consequence that if the silver coin were restored to its "
                  "standard weight, &ldquo;there would in this case, be a profit in "
                  "melting it down&rdquo;, since a guinea would buy more silver in coin than "
                  "in bullion. Later economists named this kind of tendency, in which the "
                  "overrated metal drives the other out, Gresham's law, a name H. D. Macleod "
                  "gave it in the 1850s. Smith also reports that Locke blamed the high price "
                  "of silver bullion on the permission to export bullion, and replies that "
                  "gold had the same permission and its price had fallen below the mint "
                  "price. The reader can take the details as his argument that a coin's "
                  "value follows its metal and not its name."),
            ("p", "That is the idea the lab uses. &ldquo;The money of any particular "
                  "country is, at any particular time and place, more or less an accurate "
                  "measure or value, according as the current coin is more or less exactly "
                  "agreeable to its standard.&rdquo; Smith defines the money price of goods "
                  "as &ldquo;the quantity of pure gold or silver for which they are sold, "
                  "without any regard to the denomination of the coin&rdquo;, and gives the "
                  "example: six shillings and eightpence in Edward I's time, he says, is "
                  "the same money price as a pound sterling in his own, &ldquo;because it "
                  "contained, as nearly as we can judge, the same quantity of pure "
                  "silver&rdquo;. Six and eightpence is 80 pence, a third of the 240 in "
                  "the pound, which is Smith's third."),
            ("p", "The lab turns that into a table. Each period gives the pence coined from "
                  "one pound weight of silver. In the preset <code>england</code> they are "
                  "240, the pound of Edward I (a pound of silver, 240 pennies of a "
                  "pennyweight each, which Smith gives in Chapter 4), and 744, the mint's "
                  "62 shillings of Smith's day. Each penny now holds `240/744`, which is "
                  "`10/31`, or nearly a third of the silver; the old pound comes to 744 "
                  "new pence, £3 2s; and a debt of £100, 24,000 pence, paid in the new coin "
                  "is paid with `10/31` of the silver it was lent in, so the creditor loses "
                  "`21/31`, about 68 per cent. Smith's own word is &ldquo;about a "
                  "third&rdquo;, and his Tower pound was a little lighter than the Troy pound "
                  "of the mint, so the match of 240 with 744 is rough, as he says."),
            ("p", "The presets <code>scotland</code> and <code>france</code> apply his "
                  "other fractions to the same 240: a Scots pound at about a thirty-sixth of "
                  "its original silver is 240 times 36, or 8,640 pence to the pound weight, "
                  "and a French livre at about a sixty-sixth is 15,840. These are the lab's "
                  "arithmetic with Smith's &ldquo;about&rdquo;, and not recorded mint "
                  "figures. The creditor owed £100 in the old Scots money is repaid with "
                  "`1/36` of the silver, and in French money with `1/66`. Smith's verdict "
                  "is in the Chapter 4 passage the lab is built on: such operations enabled "
                  "princes to pay their debts &ldquo;in appearance only; for their "
                  "creditors were really defrauded of a part of what was due to them&rdquo;, "
                  "so they have always proved &ldquo;favourable to the debtor, and ruinous "
                  "to the creditor&rdquo;."),
            ("p", "Chapter 5 closes on that definition of the money price. In Chapter 6 Smith "
                  "turns to the second of the three questions he set in Chapter 4: what "
                  "parts make up a price? The next course reads it."),
        ],
        "lab": ("wonkit", {
            "mode": "money",
            "view": "coin",
            "preset": "england",
            "presets": [
                {"id": "england",
                 "label": "England, Edward I's 240 pennies to the pound weight and the mint's 744 in Smith's day (his about a third)",
                 "periods": "edward-i, 240; smiths-day, 744",
                 "sum": 24000,
                 "expect": {
                          "wmoSilver": "edward-i 1 = 100%; smiths-day 10/31 ≈ 32.3%",
                          "wmoPound": "edward-i 240d (£1); smiths-day 744d (£3 2s)",
                          "wmoSumSilver": "edward-i 100 lb silver; smiths-day 1,000/31 ≈ 32.26 lb silver",
                          "wmoLoss": "smiths-day 21/31 ≈ 67.7% of the silver",
                          "wmoLossSum": "smiths-day 504,000/31 ≈ 16,258.06d lost, in edward-i’s pence",
                         }},
                {"id": "scotland",
                 "label": "Scotland, Smith's about a thirty-sixth applied to 240 (the lab's arithmetic)",
                 "periods": "alexander-to-bruce, 240; smiths-day, 8640",
                 "sum": 24000,
                 "expect": {
                          "wmoSilver": "alexander-to-bruce 1 = 100%; smiths-day 1/36 ≈ 2.8%",
                          "wmoPound": "alexander-to-bruce 240d (£1); smiths-day 8,640d (£36)",
                          "wmoSumSilver": "alexander-to-bruce 100 lb silver; smiths-day 25/9 ≈ 2.78 lb silver",
                          "wmoLoss": "smiths-day 35/36 ≈ 97.2% of the silver",
                          "wmoLossSum": "smiths-day 70,000/3 ≈ 23,333.33d lost, in alexander-to-bruce’s pence",
                         }},
                {"id": "france",
                 "label": "France, Smith's about a sixty-sixth applied to 240 (the lab's arithmetic)",
                 "periods": "charlemagne, 240; smiths-day, 15840",
                 "sum": 24000,
                 "expect": {
                          "wmoSilver": "charlemagne 1 = 100%; smiths-day 1/66 ≈ 1.5%",
                          "wmoPound": "charlemagne 240d (£1); smiths-day 15,840d (£66)",
                          "wmoSumSilver": "charlemagne 100 lb silver; smiths-day 50/33 ≈ 1.52 lb silver",
                          "wmoLoss": "smiths-day 65/66 ≈ 98.5% of the silver",
                          "wmoLossSum": "smiths-day 260,000/11 ≈ 23,636.36d lost, in charlemagne’s pence",
                         }},
            ],
            "panel_title": "The silver in a penny",
            "panel_intro": (
                "For each period, the pence coined from a pound weight of silver go in, "
                "and a fixed sum of pence if you like. The lab gives the silver in a "
                "penny against the first period, the first period's pound in later "
                "pence, and what a creditor paid the same sum would lose."
            ),
        }),
        "steps_title": "What a debased coin does to a debt",
        "steps_intro": "Four steps, for any pair of periods.",
        "steps": [
            ("Write the pence from a pound weight",
             "In each period, how many pence were coined from one pound weight of silver. "
             "Smith's first figure is 240, a pennyweight to the penny."),
            ("Find the silver in a penny",
             "A penny holds the first period's coinage divided by this period's, as a "
             "fraction of what a first-period penny held. Coining more pence from the "
             "same silver means each holds less."),
            ("Convert the old pound",
             "The first period's pound is 240 pence of silver and comes to as many later "
             "pence as were coined from the pound weight. For 744 that is £3 2s."),
            ("Pay the debt in the new coin",
             "A fixed sum of pence, paid in later pence, carries the silver fraction of "
             "step two. One minus that fraction is what the creditor is defrauded of."),
        ],
        "worked": {
            "title": "The pound of Edward I, paid in the coin of Smith's day",
            "intro": [
                "Take the first preset. A pound weight of silver coins 240 pence under "
                "Edward I and 744 in Smith's day. A debt of £100 is 24,000 pence. You want "
                "the silver in a penny, the old pound in new pence and the creditor's loss.",
            ],
            "lines": [
                "silver in a penny:  240 / 744 = 10/31",
                "old pound in new pence:  744 pence = £3 2s",
                "debt in silver, old:  24000 / 240 = 100 pounds weight",
                "debt in silver, new:  24000 / 744 = 32 pounds weight, nearly",
                "creditor's loss:  1 − 10/31 = 21/31",
            ],
            "after": [
                "The same 24,000 pence that were once 100 pounds weight of silver are now "
                "about 32, so the creditor loses a little over two-thirds. Smith's "
                "&ldquo;about a third&rdquo; is `10/31`, which is `0.32`, close to a "
                "third. The Scots and French figures are the same arithmetic with larger "
                "numbers.",
            ],
        },
        "quiz_title": "Coin, mint and creditor",
        "quiz": [
            {"q": "A pound weight of silver coins 240 pence in one reign and 720 in another. "
                  "How much silver does a penny of the second reign hold, compared with a "
                  "penny of the first?",
             "a": ["One third", "Three times as much", "Two thirds", "One half"],
             "c": 0,
             "why": "`240/720 = 1/3`. Three times as much is the number of pence coined, "
                    "not the silver in each, and two thirds is what is lost, not what "
                    "remains."},
            {"q": "A debt of 24,000 pence, borrowed when 240 pence were coined from a pound "
                  "weight of silver, is repaid when 720 are coined. What does the creditor "
                  "lose?",
             "a": ["One third of the silver he lent",
                   "Two thirds of the silver he lent",
                   "Nothing, because the sum of pence is the same",
                   "Three times the silver he lent"],
             "c": 1,
             "why": "He lent 100 pounds weight and is repaid 24000/720, which is `100/3`: "
                    "a third of the silver, so he loses two thirds. Smith's complaint is that "
                    "the sum of pence is the same and the silver is not, so the "
                    "creditor is &ldquo;really defrauded&rdquo;."},
            {"q": "The mint coins a pound weight of standard silver into 62 shillings. "
                  "What is the mint price of an ounce, there being twelve ounces to the "
                  "pound?",
             "a": ["5s", "5s 4d", "5s 2d", "6s"],
             "c": 2,
             "why": "`62/12` shillings is five and one-sixth, which is 5s 2d, Smith's "
                    "figure. Five shillings would be 60 shillings to the pound."},
            {"q": "If the legal value of the guinea were reduced from 21 to 20 shillings, "
                  "how many guineas would pay a debt of 42 shillings?",
             "a": ["2", "2 and 1/10", "1 and 9/10", "42"],
             "c": 1,
             "why": "`42/20 = 2 1/10` guineas. At 21 shillings it was two, and at 22 it "
                    "would be a little under two. The silver needed is unchanged; the gold "
                    "needed is more when the guinea is reduced."},
        ],
        "mistakes": [
            ("Thinking a debased coin only changes its name",
             "The pound is a sum of silver, and when more pence are coined from a pound "
             "weight each holds less. A debt of the same number of pence is then a smaller "
             "debt in silver, and that is the creditor's loss."),
            ("Taking Smith's fractions as mint records",
             "Smith's &ldquo;about a third&rdquo;, &ldquo;about a thirty-sixth&rdquo; and "
             "&ldquo;about a sixty-sixth&rdquo; are his estimates. The English figures of "
             "240 and 744 are his weights read against one another, with a Tower pound and "
             "a Troy pound that differ; the Scots and French pence are the lab's "
             "arithmetic from his fractions."),
            ("Reading the standard metal as a matter of fact",
             "Smith says the distinction between the metal that is the standard and "
             "the one that is not becomes, while the law fixes a ratio, &ldquo;little more "
             "than a nominal distinction&rdquo;. It matters when the ratio is changed, and "
             "the lesson's guinea shows how."),
        ],
        "standard": (
            "Finish when you can compute the silver in a coin after a debasement and the "
            "loss to a creditor paid in it.",
            "Given the pence coined from a pound weight of silver in two periods and a "
            "fixed sum of pence, compute the silver in a penny, the earlier pound in "
            "later pence and the share of the silver the creditor loses."
        ),
        "note": (
            "The lab compares pennies per pound weight of silver. It cannot say whether a "
            "prince gained, since a prince also owes, or what the fall of the pound did to "
            "prices, wages or trade; Smith says only that creditors are defrauded. The "
            "figures for Scotland and France are not recorded coinage: they are his "
            "fractions multiplied out. Smith's claim that sovereigns have almost never "
            "raised the metal in a coin is a generalisation on which the record is mixed."
        ),
    },
]
