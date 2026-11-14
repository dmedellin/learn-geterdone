"""The Mercantile System, lessons 1-3 -- Book IV, Chapters 1 to 3.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition, Pennsylvania State University, 2005); the
comment beside each lesson gives its line numbers. A drop capital ("THAT WEALTH") is
printed here as ordinary text where the quotation starts after it, and a quotation
that would cross a page break in the extraction stops before the break. Nothing
else is changed. Smith's own figures are marked as his in each lab preset; the rest
were written for the lesson.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 13592-14356 (Book IV, Chapter 1). Opening l. 13594-13607; the
    # Spaniards and the Tartars l. 13611-13624; the wine and the gold l. 13791-13804;
    # the packet-boat l. 13814-13822; the utensils l. 13978-13979; the war l. 14030-14061
    # and l. 14102-14104; the benefits of foreign trade l. 14185-14201; America l. 14213-14218.
    {
        "slug": "wealth-does-not-consist-in-money",
        "title": "Wealth Does Not Consist in Money",
        "module": "Book IV, Chapter 1 · Of the Principle of the Commercial or Mercantile System",
        "one_line": "The popular belief that wealth is gold and silver explains the whole mercantile system, and Smith answers it with what gold is for.",
        "summary": (
            "Smith opens Book IV with the belief that a rich country is one with a great deal "
            "of money, and he states the case its defenders made at its best before he "
            "answers it. Compute the balance of trade country by country, the figure the "
            "system watched, and see what it can and cannot say about a country's gain."
        ),
        "key": [
            "wealth: what money buys, not money itself",
            "balance = exports − imports",
            "money runs after goods, not goods after it",
            "gold goes where it is wanted, laws or none",
            "balance with each country, then the total",
        ],
        "key_label": "The first chapter in five lines",
        "concepts_intro": (
            "The chapter has an argument and a design. The argument is about what money is "
            "for; the design is the list of six means at its end, which gives Book IV its "
            "plan."
        ),
        "concepts": [
            ("Money's two jobs",
             "Money is the instrument of commerce, so with money you can get whatever else "
             "you want more easily than by any other good. It is also the measure of value, "
             "so a rich man is said to be worth so many pounds. Smith says the belief that "
             "wealth is money arises naturally from these two jobs, and this is why it is "
             "so hard to drop."),
            ("Wealth is what money buys",
             "A country's wealth, for Smith, is what money purchases, and money is valuable "
             "only for purchasing. A nation that keeps more gold than its trade needs has "
             "not grown richer, and cannot keep it by law. Gold is a utensil of the "
             "nation, like the furniture of a kitchen."),
            ("The balance of trade",
             "The doctrine that follows from the belief. A country with no mines gets gold "
             "only by selling to foreigners more than it buys from them, so the surplus of "
             "exports over imports, taken partner by partner, is the system's measure of "
             "success, and its two engines are restraints on imports and encouragements to "
             "exports."),
        ],
        "read_title": "The passage first, then the chapter in its order",
        "read_intro": (
            "Smith starts from the popular notion and ends with a list of the six means by "
            "which the system pursues it, which the next five chapters take one at a time."
        ),
        "body": [
            ("p", "<strong>Book IV, Chapter 1.</strong> Smith opens by saying that the "
                  "belief that wealth &ldquo;consists in money, or in gold and silver, is a "
                  "popular notion which naturally arises from the double function of money, "
                  "as the instrument of commerce, and as the measure of value&rdquo;."),
            ("p", "Think of the way you talk about a rich neighbour. You say she is worth a "
                  "great deal, and you mean money. Smith's observation is that this is not a "
                  "mistake anyone made on purpose: you can get what you want with money, "
                  "and you count what you have in it, so for any one person wealth and "
                  "money do run together. The belief is a generalisation of that fact from "
                  "one person to a country, and the chapter is about whether it holds."),
            ("p", "Smith gives two examples of the belief at work. &ldquo;the first inquiry "
                  "of the Spaniards, when they arrived upon any unknown coast, used to be, if "
                  "there was any gold or silver to be found in the neighbourhood&rdquo;. "
                  "And he reports of Plano Carpino, a monk sent as ambassador to a son of "
                  "Genghis Khan, that the Tartars used to ask him whether there were plenty of "
                  "sheep and oxen in France. Among shepherds cattle are the instruments of "
                  "commerce and the measures of value, so the Tartars' question had the same "
                  "object as the Spaniards'. Smith adds a dry remark: &ldquo;Of the two, the "
                  "Tartar notion, perhaps, was the nearest to the truth.&rdquo; Cattle at "
                  "least feed and work. Gold does neither."),
            ("p", "The notion had defenders of weight. Locke, Smith says, held that "
                  "other movable goods are consumed and wasted, so that a nation abounding in "
                  "them one year may be in want the next, whereas money &ldquo;is a steady "
                  "friend&rdquo;. Others allowed that a country shut off from the world would "
                  "have no use for more money, but said that one which must fight wars abroad "
                  "must send money to pay for them, and so must save it in time of peace. "
                  "Spain and Portugal, which owned the mines, forbade or taxed its export, and "
                  "so, once, did France, England and Scotland."),
            ("p", "Then the merchants complained. Smith's account of what happened next is "
                  "the history of an idea with people in it. When those countries became "
                  "commercial, the merchants found the prohibition inconvenient, since gold "
                  "and silver were often the best thing to buy foreign goods with. They told "
                  "parliaments and princes two things. First, that sending out gold need not "
                  "reduce it: Thomas Mun, whose <em>England's Treasure by Forraign Trade</em> "
                  "was published after his death in 1664, compared foreign trade to "
                  "agriculture, where &ldquo;the actions of the husbandman in the seed time, "
                  "when he casteth away much good corn into the ground&rdquo; look madness "
                  "until the harvest. Second, that the prohibition could not work, since "
                  "gold is small and easily smuggled, and that the only remedy was to watch "
                  "what they called the balance of trade."),
            ("def", ("The balance of trade",
                     "The difference between the value of a country's exports and the value "
                     "of its imports. When exports are the larger, a balance is due to the "
                     "country from foreigners and, on the mercantile doctrine, is paid in gold "
                     "and silver; when imports are the larger, the contrary. The system "
                     "called the first favourable and the second unfavourable.")),
            ("p", "Smith's verdict on these two arguments is balanced: &ldquo;Those arguments "
                  "were partly solid and partly sophistical.&rdquo; Solid, because sending out "
                  "gold in trade may help the country and no law can stop it when private "
                  "people find it worth their while. Sophistical, because there is no reason "
                  "that gold needs the government's attention more than wine does. Smith adds "
                  "that these arguments won because of who heard them: the merchants spoke "
                  "to nobles and country gentlemen &ldquo;who were conscious to themselves "
                  "that they knew nothing about the matter&rdquo;. The effect was to turn "
                  "the care of government, in his words, &ldquo;From one fruitless care&rdquo; "
                  "(guarding gold) &ldquo;to another care much more intricate, much more "
                  "embarrassing, and just equally fruitless&rdquo; (watching the balance)."),
            ("p", "His own answer begins with what gold is. &ldquo;A country that has "
                  "wherewithal to buy wine, will always get the wine which it has occasion "
                  "for; and a country that has wherewithal to buy gold and silver, will "
                  "never be in want of those metals.&rdquo; Gold is bought, like everything "
                  "else, with whatever the country has to sell. It moves more readily than "
                  "almost anything, and Smith's picture of this is the packet-boat. If "
                  "England wanted more gold, one packet-boat from Lisbon could bring "
                  "&ldquo;fifty tons of gold, which could be coined into more than five "
                  "millions of guineas&rdquo;, whereas an equal value of grain at five guineas a "
                  "ton would need &ldquo;a million of tons of shipping, or a thousand ships "
                  "of a thousand tons each&rdquo;. A country that wants gold and can pay for "
                  "it will get it without help, and one that has too much cannot keep it."),
            ("p", "The second reply is about use. The kitchen is Smith's example: nobody "
                  "supposes a family dines better for being forced to keep more pots and "
                  "pans than its cooking needs. &ldquo;Gold and silver, whether in the shape "
                  "of coin or of plate, are utensils, it must be remembered, as much as the "
                  "furniture of the kitchen.&rdquo; The quantity of coin is set by the value "
                  "of the goods it circulates, and the quantity of plate by the number and "
                  "wealth of the families who like it. He adds the reason money behaves "
                  "differently from goods in a merchant's mind: &ldquo;Money, therefore, "
                  "necessarily runs after goods, but goods do not always or necessarily run "
                  "after money&rdquo;, for &ldquo;It is not for its own sake that men desire "
                  "money, but for the sake of what they can purchase with it.&rdquo;"),
            ("p", "The third is about war, where Smith uses figures. The last French war "
                  "cost Great Britain upwards of £90,000,000, and more than two-thirds of "
                  "that was laid out in distant countries, so about `90,000,000 × 2/3 = "
                  "60,000,000`. The country's circulating gold and silver had been supposed "
                  "to be £18,000,000, and on the most exaggerated computation he had seen "
                  "£30,000,000. Had the war been paid in coin, the whole money of the country "
                  "would have gone abroad and come back twice over in six or seven years, "
                  "yet &ldquo;The channel of circulation, however, never appeared more empty "
                  "than usual.&rdquo; The war was paid, he argues, with goods, since "
                  "&ldquo;Fleets and armies are maintained, not with gold and silver, but "
                  "with consumable goods.&rdquo; Spain and Portugal took in from their mines "
                  "no more than about £6,000,000 a year, which against the £19,000,000 spent "
                  "in 1761 gives `12 × 6/19 = 72/19`, a little under four months. Smith says "
                  "&ldquo;would scarce have paid four months expense of the late war&rdquo;."),
            ("p", "The lab computes the figure the system watched. It takes a country's "
                  "exports to and imports from each partner and prints the balance, "
                  "exports minus imports, partner by partner and in total. The first preset, "
                  "<em>three-partners</em>, was written for this lesson: Holland takes "
                  "£400,000 of goods and sends £300,000, France takes £100,000 and sends "
                  "£250,000, Portugal takes £300,000 and sends £120,000. The total balance "
                  "is favourable by £130,000, yet it is unfavourable with France by "
                  "£150,000, and on the system's own view the French trade is the one to "
                  "restrain. The second, <em>france-shut</em>, shuts that trade almost "
                  "entirely, with the French shutting ours in return, and the balance rises "
                  "to £300,000 on a total two-way trade that has fallen from £1,470,000 to "
                  "£1,140,000. The third, <em>even</em>, has the same trade as the "
                  "first and a balance of nothing with everyone. The system would score "
                  "the second highest and the third lowest. Smith's chapter is about "
                  "whether that score tells you anything."),
            ("p", "What does foreign trade do, then? Smith's answer is the one that every "
                  "later Book depends on: it &ldquo;carries out that surplus part of the "
                  "produce of their land and labour for which there is no demand among them, "
                  "and brings back in return for it something else for which there is a "
                  "demand&rdquo;, and by widening the market it lets the division of labour "
                  "go further. So &ldquo;The importation of gold and silver is not the "
                  "principal, much less the sole benefit, which a nation derives from its "
                  "foreign trade.&rdquo; The discovery of America is his example. The "
                  "American mines made silver cheaper, so that a service of plate cost about "
                  "a third of the corn or labour it had in the fifteenth century, which is "
                  "`1 ÷ 1/3 = 3` times the plate for the same expense, and Smith calls this "
                  "a very trifling convenience. What enriched Europe, he says, was the new "
                  "market. He adds, in the same passage, that &ldquo;The savage injustice of "
                  "the Europeans rendered an event, which ought to have been beneficial to "
                  "all, ruinous and destructive to several of those unfortunate "
                  "countries.&rdquo;"),
            ("p", "Objections come from two directions. Hume had argued in 1752 that a "
                  "country cannot keep gold it does not need, since the gold raises its prices "
                  "until its exports fall and the gold flows out again, and Smith's reply "
                  "has the same shape. The most serious later defence of the mercantile "
                  "writers is Keynes's, in 1936: he argued that a country which cannot "
                  "lower its interest rate except by gaining gold has a real reason to want "
                  "a favourable balance, since more gold means lower interest and more "
                  "investment, and he thought the mercantilists had hold of that. "
                  "This is an argument about unemployment, which Smith's Book IV does not "
                  "take up, and the lesson leaves it as it stands. How a country settles "
                  "payments across a border in gold is a point Capital takes up in "
                  "<em>World Money</em>. The next lesson takes the first of the six means "
                  "Smith lists, restraints on importation, and the passage in which an "
                  "invisible hand appears."),
        ],
        "lab": ("wonkit", {
            "mode": "trade",
            "view": "balance",
            "money_unit": "£",
            "preset": "three-partners",
            "presets": [
                {"id": "three-partners",
                 "label": "Three partners, written for this lesson",
                 "countries": [{"country": "holland", "exports": 400000, "imports": 300000},
                               {"country": "france", "exports": 100000, "imports": 250000},
                               {"country": "portugal", "exports": 300000, "imports": 120000}],
                 "expect": {
                    "wtrBalances": "holland +£100,000; france −£150,000; portugal +£180,000",
                    "wtrTotal": "+£130,000",
                    "wtrUnfavourable": "1: france",
                    "wtrTwoWay": "£1,470,000",
                 }},
                {"id": "france-shut",
                 "label": "The French trade shut, written for this lesson",
                 "countries": [{"country": "holland", "exports": 400000, "imports": 300000},
                               {"country": "france", "exports": 20000, "imports": 0},
                               {"country": "portugal", "exports": 300000, "imports": 120000}],
                 "expect": {
                    "wtrBalances": "holland +£100,000; france +£20,000; portugal +£180,000",
                    "wtrTotal": "+£300,000",
                    "wtrUnfavourable": "0: none",
                    "wtrTwoWay": "£1,140,000",
                 }},
                {"id": "even",
                 "label": "Even with everyone, written for this lesson",
                 "countries": [{"country": "holland", "exports": 350000, "imports": 350000},
                               {"country": "france", "exports": 175000, "imports": 175000},
                               {"country": "portugal", "exports": 210000, "imports": 210000}],
                 "expect": {
                    "wtrBalances": "holland £0; france £0; portugal £0",
                    "wtrTotal": "£0",
                    "wtrUnfavourable": "0: none",
                    "wtrTwoWay": "£1,470,000",
                 }},
            ],
            "panel_title": "The balance of trade, partner by partner",
            "panel_intro": (
                "Each partner's exports and imports go in; the lab prints the balance with "
                "each, the total and the two-way trade. The balance is the mercantile "
                "measure Smith rejects, computed here so that you can read it. Switch "
                "between the presets and watch the total balance and the two-way trade "
                "move independently."
            ),
        }),
        "steps_title": "Reading a balance of trade",
        "steps_intro": "Four steps, the same for any list of partners.",
        "steps": [
            ("Take each partner's balance",
             "Subtract what the country buys from the partner from what it sells to the "
             "partner, and keep the sign. A positive balance is what the system called "
             "favourable and a negative one unfavourable."),
            ("Add them for the whole country",
             "The total balance is the sum of the partners' balances. It is also total "
             "exports minus total imports, and the two calculations must agree."),
            ("List the unfavourable partners",
             "The system would have the country restrain trade with each partner whose "
             "balance is negative. Note which they are and how large."),
            ("Set the balance beside the trade",
             "Add exports and imports for each partner and in total. A large balance on a "
             "small trade and a zero balance on a large one are different situations, and "
             "the balance cannot tell them apart."),
        ],
        "worked": {
            "title": "Three partners, one balance",
            "intro": [
                "Take the first preset. Holland, France and Portugal take £400,000, "
                "£100,000 and £300,000 of the country's goods and send £300,000, "
                "£250,000 and £120,000.",
            ],
            "lines": [
                "Holland:  400,000 − 300,000 = +100,000",
                "France:  100,000 − 250,000 = −150,000",
                "Portugal:  300,000 − 120,000 = +180,000",
                "whole country:  100,000 − 150,000 + 180,000 = +130,000",
                "two-way trade:  700,000 + 350,000 + 420,000 = 1,470,000",
            ],
            "after": [
                "The country is £130,000 ahead and £150,000 behind with France. On the "
                "system's view it should restrain the French trade. In the second preset it "
                "does, and the balance rises by £170,000 while the trade falls by "
                "£330,000. Whether that is a gain is the question Smith keeps asking, and "
                "the balance alone cannot answer it.",
            ],
        },
        "quiz_title": "Money, wine and war",
        "quiz": [
            {"q": "Smith says of the Spaniards' notion that wealth is gold and the Tartars' "
                  "notion that it is cattle that one was nearer the truth. Which?",
             "a": ["The Spaniards', because gold can buy cattle and anything else",
                   "Neither, since he says both are equally far from the truth",
                   "The Tartars', which at least counts a thing that feeds and works",
                   "Both, since he says the two notions amount to the same thing"],
             "c": 2,
             "why": "&ldquo;Of the two, the Tartar notion, perhaps, was the nearest to the "
                    "truth.&rdquo; He gives no reason in that sentence; the reading offered "
                    "here, that cattle feed and work where gold does not, is the lesson's "
                    "gloss. The other three each contradict his sentence."},
            {"q": "In the preset <em>three-partners</em>, which statement is true?",
             "a": ["The country is £150,000 behind with France although £130,000 ahead overall",
                   "The country is £150,000 ahead with France and £130,000 behind overall",
                   "France and Portugal balance each other exactly, so the total is £100,000",
                   "The country is behind with Holland and ahead with France"],
             "c": 0,
             "why": "France's balance is `100,000 − 250,000 = −150,000`, and the total is "
                    "`100,000 − 150,000 + 180,000 = +130,000`. Holland is ahead by "
                    "£100,000 and Portugal by £180,000, so the last two answers get the "
                    "signs wrong and France and Portugal do not cancel."},
            {"q": "Why does Smith bring in the packet-boat and the thousand ships?",
             "a": ["To show that grain is worth more a ton than gold",
                   "To show that a government should guard its gold as it guards ships",
                   "To show that Britain imports more grain than gold",
                   "To show that gold moves to where it is wanted so easily that a "
                   "country able to pay for it never lacks it"],
             "c": 3,
             "why": "Fifty tons of gold make more than five million guineas, while the same "
                    "value of grain at five guineas a ton takes a million tons of shipping. "
                    "The comparison is about how easily the two move. It says nothing "
                    "about which is worth more a ton in general, and nothing about guarding."},
            {"q": "Smith gives Spain and Portugal's yearly gold and silver as about "
                  "£6,000,000 and the cost of the war in 1761 as over £19,000,000. How "
                  "long would the metal have paid for the war?",
             "a": ["About eleven months", "A little under four months",
                   "A little over seven months", "About two years"],
             "c": 1,
             "why": "`12 × 6/19 = 72/19`, which is `3 15/19` months. Smith says it &ldquo;would "
                    "scarce have paid four months expense&rdquo;. Eleven months and "
                    "seven months do not follow from the two figures, and two years is "
                    "the wrong way round."},
        ],
        "mistakes": [
            ("Thinking Smith says money does not matter",
             "He says that wealth is not money, which is a different claim. Money is part "
             "of a nation's capital, though he says it is a small part and &ldquo;always "
             "the most unprofitable part of it&rdquo;, and he says elsewhere in the chapter "
             "that a shortage of money can always be made up by barter, credit or paper. "
             "His point is that the quantity of money follows the trade it circulates "
             "and does not need government attention."),
            ("Reading a favourable balance as a gain",
             "A favourable balance is exports above imports. A gain, in Smith's sense, is an "
             "increase in the exchangeable value of the annual produce of the land and "
             "labour. The first preset shows the balance and the trade moving separately, "
             "and the third shows a country with trade and no balance at all."),
            ("Hearing Smith say the merchants were simply wrong",
             "He says their two arguments were &ldquo;partly solid and partly "
             "sophistical&rdquo;. Sending gold out may be advantageous, and no prohibition "
             "can stop it. What he denies is that the quantity of gold needs special "
             "watching, and that the balance is the way to watch it."),
        ],
        "standard": (
            "Finish when you can compute a balance of trade and say what it leaves out.",
            "Given a country's exports and imports with each partner, compute the balance "
            "with each and in total, list the unfavourable partners, and say in one sentence "
            "why Smith treats the figure as no measure of the country's gain."
        ),
        "note": (
            "The lab shows a balance of trade from stated figures. It cannot say whether a "
            "favourable balance brings gold, whether gold matters when it comes, or "
            "whether a country gains. Smith's argument is that the quantity of money follows "
            "the trade it circulates, and Hume's earlier argument runs on the same lines. "
            "Keynes's reading of the mercantilists, which concerns interest rates and "
            "employment, is not an argument the chapter takes up. The first preset's partners "
            "and sums were written for the lesson, and Smith gives none of them. The £90,000,000, "
            "the £30,000,000, the £6,000,000 and the £19,000,000 are Smith's, in the prose."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 14357-15037 (Book IV, Chapter 2). The monopoly of the home market
    # l. 14362-14399; the home trade l. 14404-14456; the invisible hand l. 14457-14481;
    # the household maxim l. 14491-14511; the grapes l. 14558-14566; the Navigation Act
    # l. 14702-14768; the equal tax l. 14769-14783; retaliation l. 14851-14907;
    # restoring freedom l. 14908-15028.
    {
        "slug": "the-invisible-hand",
        "title": "Restraints on Importation and the Invisible Hand",
        "module": "Book IV, Chapter 2 · Of Restraints upon the Importation of Goods that can be Produced at Home",
        "one_line": "Smith's one use of the words 'invisible hand' sits in an argument about where merchants put their capital, and the chapter's work is done by the household maxim beside it.",
        "summary": (
            "Chapter 2 asks what a monopoly of the home market does to a country. Smith "
            "answers that it cannot increase the industry a capital can maintain, only "
            "direct it, and he lists the cases where a burden on foreign goods may be "
            "right. Compare the cost of making with the cost of buying, and read the one "
            "sentence in the book that uses the words 'invisible hand'."
        ),
        "key": [
            "buy abroad when it costs less than at home",
            "year's cost = units × (home − abroad)",
            "a duty adds to the cost of buying abroad",
            "equal tax at home and duty abroad: same order",
            "capital sets industry; laws only divert it",
        ],
        "key_label": "The second chapter in five lines",
        "concepts_intro": (
            "The chapter has one main argument and a short list of exceptions. The main "
            "argument is about capital, and the exceptions are the part to read twice."
        ),
        "concepts": [
            ("The monopoly of the home market",
             "A high duty or a prohibition on goods that can be made at home secures the "
             "home market to domestic makers. Smith grants that this encourages the trade "
             "that gets it and turns more of the country's labour and stock to it. What he "
             "denies is that it adds to the country's industry as a whole."),
            ("Capital sets the limit",
             "&ldquo;No regulation of commerce can increase the quantity of industry in "
             "any society beyond what its capital can maintain.&rdquo; A law can only "
             "divert industry to a different use, and whether the new use is better is the "
             "question. Smith's test is the household's: never make at home what it costs "
             "more to make than to buy."),
            ("The four cases",
             "Two cases where a burden on foreign goods may be right: defence, as in the "
             "Navigation Act, and an equal tax laid on the foreign goods when a tax has "
             "been laid on the home goods. Two where the question is open: whether to "
             "retaliate against a neighbour's restraint, and how fast to remove a "
             "restraint that has grown up."),
        ],
        "read_title": "The passage first, then the argument and its exceptions",
        "read_intro": (
            "Smith's claim about capital comes first, then the sentence with the hand, "
            "then the maxim that carries the weight of the chapter."
        ),
        "body": [
            ("p", "<strong>Book IV, Chapter 2.</strong> The chapter begins with what a "
                  "restraint does. High duties or absolute prohibitions on goods that can be "
                  "made at home mean that &ldquo;the monopoly of the home market is more or "
                  "less secured to the domestic industry employed in producing them&rdquo;. "
                  "Smith's examples are the graziers, with the ban on live cattle and "
                  "salt provisions, the corn growers, the woollen makers, the silk makers "
                  "and others, and he says the variety of goods whose import is barred "
                  "&ldquo;greatly exceeds what can easily be suspected by those who are not "
                  "well acquainted with the laws of the customs&rdquo;."),
            ("p", "Then he states what he will argue. That a monopoly of the home market "
                  "&ldquo;frequently gives great encouragement to that particular species of "
                  "industry which enjoys it&rdquo; cannot be doubted. But &ldquo;No "
                  "regulation of commerce can increase the quantity of industry in any "
                  "society beyond what its capital can maintain. It can only divert a part of "
                  "it into a direction into which it might not otherwise have gone&rdquo;. "
                  "Think of a country as a household with a fixed sum to employ people. A law "
                  "that moves some of the sum from one work to another changes what the "
                  "household makes. It does not enlarge the sum."),
            ("p", "Why should the diverted use be worse? Here Smith turns to the people "
                  "whose decisions the law overrides. &ldquo;Every individual is continually "
                  "exerting himself to find out the most advantageous employment for "
                  "whatever capital he can command. It is his own advantage, indeed, and not "
                  "that of the society, which he has in view.&rdquo; And a merchant who is "
                  "choosing among uses for his capital, at equal or nearly equal profits, "
                  "&ldquo;naturally prefers the home trade to the foreign trade of "
                  "consumption, and the foreign trade of consumption to the carrying "
                  "trade&rdquo;. The reason is the one a shopkeeper would give: at home he "
                  "knows the people he trusts and the laws that would help him. An "
                  "Amsterdam merchant who carries corn from Königsberg to Lisbon has half his "
                  "capital in one place and half in the other, and for the sake of having "
                  "some of it under his eye he brings part of both cargoes to Amsterdam "
                  "and pays to unload and reload them. &ldquo;Home is in this manner the "
                  "centre, if I may say so, round which the capitals of the inhabitants of "
                  "every country are continually circulating&rdquo;."),
            ("p", "That is the preparation for the sentence. A merchant also directs his "
                  "industry so that its produce is of the greatest value, because his "
                  "profit depends on it, and the revenue of a society is the exchangeable "
                  "value of its produce, so each merchant labours to make the revenue as "
                  "great as he can. Smith continues: &ldquo;He generally, indeed, neither "
                  "intends to promote the public interest, nor knows how much he is "
                  "promoting it.&rdquo; Preferring home industry, he intends only his own "
                  "security, and directing it to the greatest value, only his own gain, and "
                  "so, in Smith's words, &ldquo;he is in this, as in many other cases, led "
                  "by an invisible hand to promote an end which was no part of his "
                  "intention.&rdquo;"),
            ("p", "The next lines are as often skipped: &ldquo;Nor is it always the worse "
                  "for the society that it was no part of it. By pursuing his own interest, "
                  "he frequently promotes that of the society more effectually than when he "
                  "really intends to promote it.&rdquo; And then &ldquo;I have never known "
                  "much good done by those who affected to trade for the public good.&rdquo; "
                  "He adds that this affectation is not very common among merchants."),
            ("def", ("The invisible hand",
                     "Smith's phrase, used once in the Wealth of Nations, in Book IV, "
                     "Chapter 2, and once in the Theory of Moral Sentiments (1759), for what "
                     "leads an individual to promote an end that was no part of his "
                     "intention. In this chapter it is used of a merchant who prefers to "
                     "employ his capital at home.")),
            ("p", "Say plainly what the book does with it. The words appear once in the "
                  "Wealth of Nations, in this paragraph, and once in the Theory of Moral "
                  "Sentiments, where the rich, who think only of their own "
                  "convenience, are led by an invisible hand to divide the necessaries of "
                  "life nearly as they would have been divided had the earth been shared "
                  "equally among its inhabitants. Here they come in an argument about the home trade: a "
                  "merchant who prefers to keep his capital where he can watch it supports "
                  "domestic industry without intending to. The passage does not use the "
                  "words to describe the market as a whole, and Smith does not return to "
                  "them. It is a plain fact about the book, and the lesson does not say how "
                  "much weight a phrase used once ought to carry."),
            ("p", "That is the point on which later readers divide, and each reading is "
                  "worth stating at its strongest. For much of the twentieth century "
                  "the phrase stood for the central idea of the book: that competition among "
                  "self-interested people produces results good for all, which Kenneth "
                  "Arrow and Gérard Debreu, among others, stated in the 1950s as a theorem, "
                  "with conditions, that a competitive economy reaches an efficient "
                  "allocation. Critics of that reading say that the conditions fail "
                  "whenever markets are incomplete or information is imperfect, and Bruce "
                  "Greenwald and Joseph Stiglitz argued in 1986 that in such an economy the "
                  "competitive outcome can generally be improved upon. Historians say "
                  "something different. Jacob Viner, in his 1927 essay on Smith and "
                  "laissez-faire, set the harmony of interests in Smith beside his belief "
                  "in a beneficent order of nature, and stressed how many exceptions to it "
                  "the Wealth of Nations makes. Emma Rothschild, in <em>Economic "
                  "Sentiments</em> (2001), argued that Smith used the phrase lightly, "
                  "perhaps ironically, and that its later fame tells us more about later "
                  "readers than about him. Smith had also written of the invisible hand of "
                  "Jupiter, in an essay on the history of astronomy, "
                  "published after his death, and some take that as a sign that the words "
                  "were a figure of speech to him. This lesson does not choose among "
                  "them."),
            ("p", "What does the chapter itself rely on? The maxim: &ldquo;It is the maxim of "
                  "every prudent master of a family, never to attempt to make at home what "
                  "it will cost him more to make than to buy.&rdquo; Smith's illustration is "
                  "the tailor, who buys shoes from the shoemaker, and the shoemaker, who "
                  "employs a tailor. &ldquo;What is prudence in the conduct of every private "
                  "family, can scarce be folly&rdquo; in a great kingdom, and so &ldquo;If a "
                  "foreign country can supply us with a commodity cheaper than we ourselves "
                  "can make it, better buy it of them with some part of the produce of our "
                  "own industry, employed in a way in which we have some advantage.&rdquo; "
                  "The preset <em>tailor-and-shoemaker</em> works it for a "
                  "household written for this lesson: a year's four pairs of shoes cost £3 to "
                  "make and £2 to buy, two coats cost £5 to make and £4 to buy, and forcing "
                  "the household to make both costs `4 × 1 + 2 × 1 = 6` pounds a year."),
            ("p", "He then lets the maxim bite. &ldquo;By means of glasses, hot-beds, and "
                  "hot-walls, very good grapes can be raised in Scotland, and very good wine, "
                  "too, can be made of them, at about thirty times the expense for which at "
                  "least equally good can be brought from foreign countries.&rdquo; Nobody "
                  "would pass a law against foreign wines to encourage claret in Scotland. "
                  "The preset <em>scottish-claret</em> sets a tun at £30 abroad "
                  "and £900 at home. Only the ratio is Smith's, and the pounds are written "
                  "for the lesson. For 100 tuns, forcing home production costs `100 × (900 "
                  "− 30) = 87,000` a year. Smith's point is that the absurdity is of the same "
                  "kind at any size: &ldquo;in turning towards any such employment a "
                  "thirtieth, or even a three hundredth part more&rdquo; of the capital. "
                  "The preset <em>a-thirtieth-more</em> makes the home cost £31 "
                  "against £30, and the year's cost is `100 × 1 = 100`."),
            ("p", "Smith allows two cases. The first is defence: &ldquo;The first is, when "
                  "some particular sort of industry is necessary for the defence of the "
                  "country.&rdquo; The defence of Great Britain depends on its sailors and "
                  "shipping, and the act of navigation, first framed by the Long "
                  "Parliament, shut foreign ships out of the trade with the colonies and "
                  "out of the coasting trade. Smith thinks some of its rules may have come "
                  "from animosity against the Dutch, and says that the animosity aimed at "
                  "what wisdom would have recommended, the weakening of &ldquo;the naval "
                  "power of Holland, the only naval power which could endanger the security "
                  "of England&rdquo;. He admits it was bad "
                  "for foreign commerce and for the wealth that comes from it, and concludes: "
                  "&ldquo;As defence, however, is of much more importance than opulence, the "
                  "act of navigation is, perhaps, the wisest of all the commercial "
                  "regulations of England.&rdquo;"),
            ("p", "The second case is the equal tax. When a tax is laid on a home product, "
                  "&ldquo;it seems reasonable that an equal tax should be imposed upon the "
                  "like produce of the former&rdquo;. The reason is that it leaves the "
                  "competition between the two as before. Take the last two "
                  "presets, written for the lesson. A home good costs £10 to make and a "
                  "foreign one £11. A tax of £2 on the home good makes it £12, and with no "
                  "duty on the foreign good (the preset <em>tax-no-duty</em>) the "
                  "foreign good is cheaper by £1, and the tax has driven the trade out of "
                  "the country. With an equal duty of £2 on the foreign good "
                  "(<em>tax-equal-duty</em>) it costs £13, the home good is again the "
                  "cheaper by £1, as before the tax. Read the other tiles with care, since "
                  "the lab takes the home cost as the £12 a buyer faces and does not know "
                  "that £2 of it is a tax. Its prohibition tile reads £1,000 a year in both, "
                  "`1,000 × (12 − 11)`, which is the cost to buyers of the taxed home good "
                  "over the foreign; to the country the home good's real cost, £10, is the "
                  "lower. In <em>tax-equal-duty</em> its tiles for what buyers pay above "
                  "the cheaper price, and for what is paid and not collected as duty, both "
                  "read £1,000: that is £1 a unit of the home tax, which the treasury does "
                  "collect, though not as a duty. Smith refuses to carry the argument "
                  "further, as some did, to a duty on all foreign goods because a tax on "
                  "necessaries raises wages, since no one can know by how much, and since a "
                  "tax on necessaries acts like a poor soil and a bad climate, which no one "
                  "would answer with a further burden."),
            ("p", "On retaliation, Smith gives both sides. &ldquo;There may be good policy in "
                  "retaliations of this kind, when there is a probability that they will "
                  "procure the repeal of the high duties or prohibitions complained of.&rdquo; "
                  "When there is no such probability he is against it, since &ldquo;Every such "
                  "law, therefore, imposes a real tax upon the whole country, not in favour "
                  "of that particular class of workmen who were injured by our neighbours "
                  "prohibitions, but of some other class.&rdquo; And on restoring free trade "
                  "after a long restraint, &ldquo;Humanity may in this case require that the "
                  "freedom of trade should be restored only by slow gradations, and with a "
                  "good deal of reserve and circumspection.&rdquo; He then argues that the "
                  "disorder would be less than commonly imagined, since more than 100,000 "
                  "soldiers and seamen were discharged at the end of the last war without "
                  "disaster, and he says that the same natural liberty should be given to "
                  "other workers, by repealing the apprenticeship statute and the law of "
                  "settlement. He does not expect it: &ldquo;To expect, indeed, that the "
                  "freedom of trade should ever be entirely restored in Great Britain, is as "
                  "absurd as to expect that an Oceana or Utopia should ever be established in "
                  "it.&rdquo;"),
            ("p", "Smith's critics here are strong. Ricardo argued in 1817 that "
                  "Smith's rule, buy it if it is cheaper abroad, is a special case: two "
                  "countries gain from trade even when one makes everything cheaper, "
                  "provided their relative costs differ, and that an absolute advantage "
                  "is not what matters. Smith's wording, a commodity cheaper abroad than "
                  "we can make it, reads most naturally as a comparison of absolute costs, "
                  "and Ricardo's reasoning does not need one. List argued in 1841 that Smith counts only "
                  "present exchange value, while a nation that wants manufactures may need a "
                  "period of protection to acquire the skill, and Smith himself concedes that "
                  "&ldquo;a particular manufacture may sometimes be acquired sooner than it "
                  "could have been otherwise&rdquo;, though he denies that the sum of "
                  "industry or revenue is increased. Smith denies the gain; List says it "
                  "comes later. The lesson leaves them there. The next lesson takes the "
                  "second restraint, aimed at one country rather than at one good, and the "
                  "balance of trade it rests on."),
        ],
        "lab": ("wonkit", {
            "mode": "trade",
            "view": "make",
            "money_unit": "£",
            "preset": "tailor-and-shoemaker",
            "presets": [
                {"id": "tailor-and-shoemaker",
                 "label": "A household's year, written for this lesson",
                 "goods": [{"good": "shoes", "quantity": 4, "home": 3, "foreign": 2, "duty": 0},
                           {"good": "coat", "quantity": 2, "home": 5, "foreign": 4, "duty": 0}],
                 "expect": {
                    "wtrAbroad": "shoes £2; coat £4",
                    "wtrCheaper": "shoes abroad; coat abroad",
                    "wtrProhibit": "£6 a year",
                    "wtrDuty": "£0 a year",
                    "wtrBuyers": "£0 a year",
                    "wtrLoss": "£0 a year",
                 }},
                {"id": "scottish-claret",
                 "label": "Scottish claret at thirty times the cost (the ratio is Smith's)",
                 "goods": [{"good": "claret", "quantity": 100, "home": 900, "foreign": 30, "duty": 0}],
                 "expect": {
                    "wtrAbroad": "claret £30",
                    "wtrCheaper": "claret abroad",
                    "wtrProhibit": "£87,000 a year",
                    "wtrDuty": "£0 a year",
                    "wtrBuyers": "£0 a year",
                    "wtrLoss": "£0 a year",
                 }},
                {"id": "a-thirtieth-more",
                 "label": "A thirtieth part more, written for this lesson",
                 "goods": [{"good": "claret", "quantity": 100, "home": 31, "foreign": 30, "duty": 0}],
                 "expect": {
                    "wtrAbroad": "claret £30",
                    "wtrCheaper": "claret abroad",
                    "wtrProhibit": "£100 a year",
                    "wtrDuty": "£0 a year",
                    "wtrBuyers": "£0 a year",
                    "wtrLoss": "£0 a year",
                 }},
                {"id": "tax-no-duty",
                 "label": "A £2 tax at home and no duty abroad, written for this lesson",
                 "goods": [{"good": "linen", "quantity": 1000, "home": 12, "foreign": 11, "duty": 0}],
                 "expect": {
                    "wtrAbroad": "linen £11",
                    "wtrCheaper": "linen abroad",
                    "wtrProhibit": "£1,000 a year",
                    "wtrDuty": "£0 a year",
                    "wtrBuyers": "£0 a year",
                    "wtrLoss": "£0 a year",
                 }},
                {"id": "tax-equal-duty",
                 "label": "The same tax with an equal duty abroad, written for this lesson",
                 "goods": [{"good": "linen", "quantity": 1000, "home": 12, "foreign": 11, "duty": 2}],
                 "expect": {
                    "wtrAbroad": "linen £13",
                    "wtrCheaper": "linen home",
                    "wtrProhibit": "£1,000 a year",
                    "wtrDuty": "£0 a year",
                    "wtrBuyers": "£1,000 a year",
                    "wtrLoss": "£1,000 a year",
                 }},
            ],
            "panel_title": "Make it or buy it",
            "panel_intro": (
                "For each good the lab prints what it costs to buy abroad, with any duty, "
                "against what it costs to make at home, which is cheaper, and what forcing "
                "the home work costs for the year. Smith's maxim is the comparison of the "
                "two costs. Try the presets in order and watch what the duty does to the "
                "comparison."
            ),
        }),
        "steps_title": "Make it or buy it",
        "steps_intro": "Four steps, the same for any good and any duty.",
        "steps": [
            ("Cost it at home",
             "What it costs to make a unit in the country, including any tax the home maker "
             "pays. The lab takes this as given."),
            ("Cost it abroad",
             "The price delivered, plus the duty a unit if there is one. A duty is part of "
             "the cost of buying abroad and is paid to the treasury."),
            ("Compare",
             "The cheaper way is the one with the smaller cost a unit. Smith's maxim says "
             "to take it, and the lab says which it is."),
            ("Price the restraint",
             "Multiply the gap by the quantity to get what forcing the dearer way costs "
             "for the year, then ask whether defence or an equal tax is the reason for "
             "the restraint, since those are Smith's exceptions."),
        ],
        "worked": {
            "title": "Scottish claret",
            "intro": [
                "Take the preset <em>scottish-claret</em>. A tun of claret costs £30 delivered from abroad "
                "and £900 to make in Scotland, and the country wants 100 tuns a year. The "
                "ratio of thirty is Smith's; the pounds are written for the lesson.",
            ],
            "lines": [
                "abroad:  30 a tun",
                "at home:  900 a tun",
                "ratio:  900 / 30 = 30",
                "forced to make at home:  100 · (900 − 30) = 87,000 a year",
            ],
            "after": [
                "The gap of £87,000 a year is what the prohibition costs, and Smith's own "
                "figure for it is the thirtyfold ratio. At a thirtieth part more, the "
                "preset <em>a-thirtieth-more</em>, the gap is `100 × (31 − 30) = 100` a year: much smaller, "
                "and in Smith's words of the same kind.",
            ],
        },
        "quiz_title": "Home trade, hands and maxims",
        "quiz": [
            {"q": "Smith names two cases in which a burden on foreign goods will generally be "
                  "advantageous. Which are they?",
             "a": ["Industry needed for defence, and an equal tax where a tax is laid "
                   "at home on the like produce",
                   "A shortage of gold, and a favourable balance with the country concerned",
                   "A new manufacture that cannot yet compete, and a petition from the "
                   "merchants",
                   "A foreign monopoly, and a high price of corn at home"],
             "c": 0,
             "why": "&ldquo;The first is, when some particular sort of industry is necessary "
                    "for the defence of the country&rdquo; and the second is the equal tax. "
                    "He grants that a manufacture may be acquired sooner by a restraint, "
                    "but does not list it as a case where the burden is advantageous."},
            {"q": "How many times do the words &ldquo;invisible hand&rdquo; appear in the "
                  "Wealth of Nations?",
             "a": ["Three times, one in each of the first three Books",
                   "Once, in Book IV, Chapter 2, in an argument about the home trade",
                   "In every chapter of Book IV",
                   "Never, since Smith uses the phrase only in the Theory of Moral Sentiments"],
             "c": 1,
             "why": "The phrase appears once in the Wealth of Nations, in the passage "
                    "about a merchant preferring to employ his capital at home, and once "
                    "in the Theory of Moral Sentiments. A search of the text finds no "
                    "other use."},
            {"q": "In the preset <em>tax-equal-duty</em> the home good costs £12 and the "
                  "foreign good £11 with a £2 duty. By how much is the home good cheaper?",
             "a": ["£2", "£0", "£1", "£3"],
             "c": 2,
             "why": "The foreign good costs `11 + 2 = 13`, so the home good at 12 is "
                    "cheaper by £1, the same margin as before the tax when the home good "
                    "cost 10 and the foreign 11. £2 is the tax itself, and £0 would be the "
                    "tie that the duty is not set to produce."},
            {"q": "On the grapes of Scotland, which does Smith say about a home cost of a "
                  "thirtieth part more than the foreign?",
             "a": ["It is no absurdity, since it is so small",
                   "It is an absurdity of exactly the same kind, though not so glaring",
                   "It is justified when the cost is thirty times as great",
                   "It is justified by the defence of the country"],
             "c": 1,
             "why": "Smith says that if turning thirty times the capital to such an "
                    "employment is absurd, then a thirtieth or a three hundredth part more is "
                    "&ldquo;an absurdity, though not altogether so glaring, yet exactly of "
                    "the same kind&rdquo;. He gives no size below which the absurdity "
                    "vanishes, and he gives no case for defence of grapes."},
        ],
        "mistakes": [
            ("Reading the invisible hand as Smith's whole doctrine of markets",
             "It is a phrase used once, in a passage about a merchant's preference for "
             "the home trade. The chapter's argument runs on capital, the household "
             "maxim and a list of exceptions, and the later theorem that is often "
             "called by the name is a different piece of work, with conditions Smith "
             "does not state."),
            ("Taking Smith to say that every restraint is folly",
             "He lists the cases in which a burden is right, calls the Navigation Act "
             "&ldquo;perhaps, the wisest of all the commercial regulations of England&rdquo;, "
             "allows retaliation when it is likely to succeed, and wants a restraint "
             "that has grown up to be taken off slowly."),
            ("Thinking a restraint cannot help the trade it protects",
             "Smith grants that it &ldquo;frequently gives great encouragement&rdquo; to "
             "that trade and draws labour and stock to it. His denial is that it increases "
             "the whole industry of the country, since that depends on capital, and that "
             "the direction it gives is likely to be the better one."),
        ],
        "standard": (
            "Finish when you can compare making with buying and name Smith's exceptions.",
            "Given the cost of a good at home and abroad with any duty, say which is "
            "cheaper and what forcing the dearer way costs in a year, and name two cases "
            "in which Smith says a burden on foreign goods may be advantageous."
        ),
        "note": (
            "The lab compares two costs and prints the gap. It cannot say whether the "
            "costs are what they would be in a free market, whether a protected industry "
            "will learn to compete, or whether a country's defence needs what a restraint "
            "preserves. Smith grants that the second may happen and List builds on that; "
            "Ricardo's reasoning shows that the comparison of costs is not by itself the "
            "right comparison. The Scottish claret's thirtyfold ratio is Smith's, and every "
            "pound and quantity in the presets was written for the lesson. The invisible "
            "hand is a phrase this lesson reports and does not weigh."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 15038-15945 (Book IV, Chapter 3, Parts I and II, with the Digression
    # concerning Banks of Deposit, particularly concerning that of Amsterdam).
    # The restraints on France l. 15045-15077; no certain criterion l. 15112-15123;
    # England and Holland l. 15141-15157; computed and real exchange l. 15158-15246;
    # the Digression l. 15247-15596; Part II l. 15597-15945; tobacco and wine l. 15691-15696;
    # the balance of produce and consumption l. 15913-15945.
    {
        "slug": "the-balance-of-trade-and-banks-of-deposit",
        "title": "The Balance of Trade and Banks of Deposit",
        "module": "Book IV, Chapter 3 · Of the Extraordinary Restraints upon the Importation of Goods from Countries with which the Balance is Supposed to be Disadvantageous",
        "one_line": "Smith takes the balance of trade apart on its own terms and then on his, and in between explains the bank of Amsterdam and why exchange is no guide to it.",
        "summary": (
            "Chapter 3 is the longest of the six. Part I argues that restraints on a "
            "partner with an adverse balance are unreasonable even on the system's own "
            "principles, and the Digression on the Bank of Amsterdam explains why the "
            "course of exchange cannot measure the balance. Part II denies the doctrine "
            "and names the balance that matters. Compute the balance on Smith's tobacco and "
            "wine, and on a payment settled through a third country."
        ),
        "key": [
            "partner's balance = exports − imports",
            "gain = home value of returns − value sent",
            "bank money = coin of full weight, plus agio",
            "a debt may be paid through a third country",
            "produce above consumption: capital grows",
        ],
        "key_label": "The third chapter in five lines",
        "concepts_intro": (
            "Three ideas carry the chapter. The first two are why the balance and the "
            "exchange mislead, and the third is the one Smith puts in their place."
        ),
        "concepts": [
            ("Computed exchange and real exchange",
             "The course of exchange is quoted from the standards of the mints, not from "
             "the metal the coin actually holds. Worn coin, the cost of coinage and the use "
             "of bank money all push the computed exchange away from the real one, so a "
             "premium on a bill does not show who owes what."),
            ("Bank money and the agio",
             "At Amsterdam a bill of 600 guilders or more had to be paid in bank money, a "
             "credit in the books of the bank for coin of full weight. Bank money is worth "
             "more than the same nominal sum of common currency, and the difference is "
             "its agio. Smith calls the whole account a digression."),
            ("The balance of produce and consumption",
             "If the annual produce is worth more than the annual consumption, the "
             "society saves and its capital grows, and if less, the capital decays. "
             "This balance is, in Smith's words, entirely different from the balance of "
             "trade, and it is the one that decides whether a country is getting richer."),
        ],
        "read_title": "The passage first, then the chapter in its three parts",
        "read_intro": (
            "Smith starts with the restraints themselves, argues first on the system's "
            "own ground and then on his, and puts the digression between the two."
        ),
        "body": [
            ("p", "<strong>Book IV, Chapter 3, Part I.</strong> The second means of the "
                  "system is to lay extraordinary restraints on goods from countries with "
                  "which the balance is thought to be against us. Smith's example is "
                  "France. Silesia lawns could be imported on paying duty, but French "
                  "cambrics and lawns were barred. The impost of 1692 laid twenty-five per "
                  "cent on French goods, and a second twenty-five per cent in 1696, with "
                  "the general subsidies, so that, he says, seventy-five per cent was the "
                  "lowest duty on the greater part of them, which he calls equivalent to a "
                  "prohibition. The French did the same in return, and as a result "
                  "&ldquo;smugglers are now the principal importers&rdquo;. These "
                  "restraints, he says, come from &ldquo;national prejudice and "
                  "animosity&rdquo;, where the monopoly of the home market came from "
                  "private interest, and they are &ldquo;still more unreasonable&rdquo;."),
            ("p", "Part I's argument is on the system's own ground. First, even if a free "
                  "trade with France would leave the balance with France against us, the "
                  "general balance of the whole trade might not be, since French wine and "
                  "linen, if better and cheaper than Portuguese and German, would make the "
                  "total of our imports smaller. Second, French goods might be sold on to "
                  "other countries at a profit and bring back as much as they cost. Third, "
                  "and here Smith spends most of his time, there is &ldquo;no certain "
                  "criterion&rdquo; for saying on which side the balance between two "
                  "countries lies. Two tests were used, "
                  "the custom-house books and the course of exchange. Of the first: &ldquo;The "
                  "custom-house books, I think, it is now generally acknowledged, are a very "
                  "uncertain criterion, on account of the inaccuracy of the valuation at which "
                  "the greater part of goods are rated in them.&rdquo; Of the second he has a "
                  "good deal to say."),
            ("p", "The reasoning behind the exchange test is this. When exchange between "
                  "London and Paris is at par, debts each way cancel; when London pays a "
                  "premium for a bill on Paris, money must be sent from London. The ordinary "
                  "state of debt and credit comes from the ordinary course of dealings, so "
                  "the exchange shows the balance. Smith's reply is that the debts between two "
                  "places are also set by their dealings with others. &ldquo;England may be "
                  "obliged to send out every year money to Holland, though its annual "
                  "exports to that country may exceed very much the annual value of its "
                  "imports from thence, and though what is called the balance of trade may be "
                  "very much in favour of England.&rdquo; The reason is that English "
                  "merchants pay for what they buy at Hamburg, Dantzic and Riga with bills on "
                  "Holland."),
            ("p", "The lab shows this with figures written for the lesson. In "
                  "<em>england-holland</em> the country sells Holland £900,000 and "
                  "buys £600,000, a balance of `900,000 − 600,000 = +300,000`. It sells the "
                  "Baltic ports, taken as one partner, £200,000 and buys £700,000, a balance "
                  "of `200,000 − 700,000 = −500,000`. Paying the Baltic ports with bills on "
                  "Holland uses up Holland's £300,000 of debt and leaves £200,000 "
                  "to be sent to Holland, though England's balance with Holland is "
                  "favourable. The total balance is `300,000 − 500,000 = −200,000`, which "
                  "is the sum that must be sent in all."),
            ("p", "The computed exchange has three further sources of error, and Smith "
                  "gives each a paragraph. The first is the wear of the coin. Before the "
                  "reform of the silver coin in King William's time, exchange with Holland, "
                  "computed from the mint standards, was twenty-five per cent against "
                  "England, but the English coin was &ldquo;rather more than five-and-twenty "
                  "per cent. below its standard value&rdquo;, so the real exchange may have "
                  "favoured England. The second is the cost of coinage: in England it was "
                  "paid by the government, so that &ldquo;if you carry a pound weight of "
                  "standard silver to the mint, you get back sixty-two shillings, containing "
                  "a pound weight of the like standard silver&rdquo;, while in France a duty of "
                  "eight per cent was deducted. The third is bank money, and it needs the "
                  "digression."),
            ("p", "The Digression concerning Banks of Deposit, particularly concerning "
                  "that of Amsterdam, describes one bank at length. A large trading city receives coin of all countries, "
                  "much of it clipped and worn. Before 1609 the currency of Amsterdam was "
                  "worth about nine per cent less than good money fresh from the mint, and "
                  "bills of exchange were of uncertain value. So &ldquo;a bank was "
                  "established in 1609, under the guarantee of the city&rdquo;, which took "
                  "coin at its intrinsic value and gave credit in its books, and "
                  "&ldquo;all bills drawn upon or negotiated at Amsterdam, of the value of "
                  "600 guilders and upwards, should be paid in bank money&rdquo;. Every "
                  "merchant had to keep an account, so there was a steady demand for it."),
            ("def", ("Agio",
                     "The premium of bank money over common currency of the same nominal "
                     "sum. At Amsterdam it was generally about five per cent, and the bank "
                     "kept it between four and five by selling bank money for currency at "
                     "five per cent agio and buying it in at four.")),
            ("p", "Smith explains it plainly: &ldquo;What is called bank money, is always of "
                  "more value than the same nominal sum of common currency.&rdquo; The bank "
                  "sold bank money for currency at five per cent agio and bought it back at "
                  "four, so that for 100 guilders of bank money, `100 × 105/100 = 105` guilders "
                  "of currency was paid and `100 × 104/100 = 104` was given back, and the "
                  "difference of one guilder in a hundred was the bank's profit on the "
                  "dealing. How much treasure the bank held, he says, is a matter of "
                  "conjecture: some 2,000 people were reckoned to keep accounts, and allowing each £1,500, which he calls a very large allowance, "
                  "the whole is `2,000 × 1,500 = 3,000,000` pounds, or at eleven guilders to "
                  "the pound `3,000,000 × 11 = 33,000,000` guilders. The bank, he says, "
                  "professes to lend none of what is deposited, and its original object was "
                  "&ldquo;to relieve the merchants from the inconvenience of a "
                  "disadvantageous exchange&rdquo;. And it is why, Smith says, the computed "
                  "exchange may favour a place that pays its bills in bank money even "
                  "when the real exchange favours the place that pays in common currency: "
                  "a sum in bank money is worth more than the same sum in currency."),
            ("p", "Part II says what Smith thinks is wrong with the whole doctrine, and the "
                  "argument turns on what gain is. &ldquo;By advantage or gain, I understand, "
                  "not the increase of the quantity of gold and silver, but that of the "
                  "exchangeable value of the annual produce of the land and labour of the "
                  "country, or the increase of the annual revenue of its inhabitants.&rdquo; "
                  "A trade carried on freely &ldquo;is always advantageous, though not always "
                  "equally so, to both&rdquo;. His example carries the point with figures: "
                  "&ldquo;If the tobacco which in England is worth only £100,000, when sent "
                  "to France, will purchase wine which is in England worth £110,000, the "
                  "exchange will augment the capital of England by £10,000.&rdquo; And the "
                  "same if the £100,000 had been gold: &ldquo;this exchange will equally "
                  "augment the capital of England by £10,000.&rdquo;"),
            ("p", "The first preset in the lab, <em>tobacco-and-wine</em>, uses these "
                  "figures, which are Smith's. Counted as the system counts, the country "
                  "exports £100,000 and imports £110,000, a balance of "
                  "`100,000 − 110,000 = −10,000`, which the system calls unfavourable. Counted "
                  "as Smith counts, what came back is worth `110,000 − 100,000 = 10,000` more "
                  "at home than what went out, and the country is that much richer. The same "
                  "trade is a loss on one measure and a gain on the other, which is his "
                  "complaint against the balance in one line."),
            ("p", "Smith adds that a direct trade is better than a round-about one, that a "
                  "nearby customer is better than a distant one (France, with returns "
                  "four, five or six times a year, against the North American colonies, "
                  "with returns every three, four or five years), and that rich neighbours are good customers: "
                  "&ldquo;The wealth of neighbouring nations, however, though dangerous in "
                  "war and politics, is certainly advantageous in trade.&rdquo; He is "
                  "sharpest about the system's authors: &ldquo;By such maxims as these, "
                  "however, nations have been taught that their interest consisted in "
                  "beggaring all their neighbours.&rdquo; It is in the same passage that he "
                  "writes that it &ldquo;always is, and must be, the interest of the great "
                  "body of the people, to buy whatever they want of those who sell it "
                  "cheapest&rdquo;, and names the merchants and manufacturers as the "
                  "people whose interest is the opposite."),
            ("p", "The chapter ends on the balance that does matter. &ldquo;This balance of "
                  "produce and consumption is entirely different from what is called the "
                  "balance of trade.&rdquo; If the produce exceeds the consumption, the "
                  "society &ldquo;lives within its revenue; and what is annually saved out of "
                  "its revenue, is naturally added to its capital&rdquo;, and if not, "
                  "&ldquo;the capital of the society must annually decay in proportion to "
                  "this deficiency&rdquo;. Such a balance can go with an adverse balance of "
                  "trade for a long time: &ldquo;A nation may import to a greater value than it "
                  "exports for half a century, perhaps, together&rdquo;. He says the state of "
                  "the North American colonies and their trade with Britain, before the "
                  "disturbances, &ldquo;may serve as a proof that this is by no means an "
                  "impossible supposition&rdquo;."),
            ("p", "Later readers have pressed three points. A country with a persistent "
                  "deficit is not obviously a country in a happy case, and economists since "
                  "have asked what the deficit is financed by and whether the borrowing "
                  "goes into investment; Smith's balance of produce and consumption is where "
                  "those questions start, though he gives no rule for deciding them. Hume's "
                  "earlier price-specie argument and Smith's both treat the money flow as "
                  "self-correcting, and Keynes's 1936 defence of the mercantilists is a "
                  "dissent from that. And Capital's lesson <em>World Money</em> follows "
                  "what bullion does when a balance is settled across a border. The next "
                  "lesson takes up drawbacks, the first of the four encouragements to "
                  "exportation."),
        ],
        "lab": ("wonkit", {
            "mode": "trade",
            "view": "balance",
            "money_unit": "£",
            "preset": "tobacco-and-wine",
            "presets": [
                {"id": "tobacco-and-wine",
                 "label": "Smith's tobacco and wine: £100,000 sent, £110,000 back",
                 "countries": [{"country": "france", "exports": 100000, "imports": 110000}],
                 "expect": {
                    "wtrBalances": "france −£10,000",
                    "wtrTotal": "−£10,000",
                    "wtrUnfavourable": "1: france",
                    "wtrTwoWay": "£210,000",
                 }},
                {"id": "england-holland",
                 "label": "Holland and the Baltic ports, written for this lesson",
                 "countries": [{"country": "holland", "exports": 900000, "imports": 600000},
                               {"country": "baltic-ports", "exports": 200000, "imports": 700000}],
                 "expect": {
                    "wtrBalances": "holland +£300,000; baltic-ports −£500,000",
                    "wtrTotal": "−£200,000",
                    "wtrUnfavourable": "1: baltic-ports",
                    "wtrTwoWay": "£2,400,000",
                 }},
            ],
            "panel_title": "A balance, and what it hides",
            "panel_intro": (
                "The lab prints the balance as the system counts it. In the first preset "
                "the trade has a balance of −£10,000 and Smith's own count gives a gain "
                "of £10,000, so the lesson's worked example sets the two side by side. "
                "In the second, a favourable balance with Holland sits beside an "
                "obligation to send money to Holland, because the Baltic debts are paid "
                "by bills on Holland."
            ),
        }),
        "steps_title": "From a balance to a gain",
        "steps_intro": "Four steps. The first two are the system's and the last two are Smith's.",
        "steps": [
            ("Take the balance with each partner",
             "Exports minus imports, with the sign, at the same valuation on both sides."),
            ("Add the balances",
             "The total is what the system would expect to be paid in money, in all, "
             "whichever partner it is paid to."),
            ("Ask where the bills are drawn",
             "A debt to one country may be paid by a bill on another, as English "
             "payments to the Baltic were drawn on Holland, so the bilateral balances do "
             "not each have to be settled with the partner."),
            ("Value what came back at home",
             "Smith's count of gain is the home value of what returns less the value of "
             "what went out. The balance does not compute it, and so you do it from the "
             "two home values."),
        ],
        "worked": {
            "title": "Tobacco and wine",
            "intro": [
                "Take Smith's own figures. England sends tobacco worth £100,000 to France and "
                "gets back wine worth £110,000 in England.",
            ],
            "lines": [
                "balance, as the system counts:  100,000 − 110,000 = −10,000",
                "home value of the wine:  110,000",
                "home value of the tobacco sent:  100,000",
                "gain to the capital, as Smith counts:  110,000 − 100,000 = 10,000",
            ],
            "after": [
                "The system's balance is −£10,000 and Smith's gain is +£10,000 on the same "
                "trade. Smith says the same of £100,000 sent in gold: what matters is what "
                "it brings back, and it brings back wine worth £110,000.",
            ],
        },
        "quiz_title": "Balance, exchange and gain",
        "quiz": [
            {"q": "In the preset <em>tobacco-and-wine</em>, the lab gives a balance of "
                  "−£10,000. What does Smith say happens to England's capital?",
             "a": ["It rises by £10,000, because the wine is worth £110,000 in England",
                   "It falls by £10,000, as the balance says",
                   "It does not change, since the goods exchanged are equal in kind",
                   "It rises by £110,000"],
             "c": 0,
             "why": "He says &ldquo;the exchange will augment the capital of England by "
                    "£10,000.&rdquo; The system counts the trade as `100,000 − 110,000 = "
                    "−10,000`. Smith compares the home value of what returns, 110,000, "
                    "with the home value of what went out, 100,000."},
            {"q": "What is the agio of the bank of Amsterdam?",
             "a": ["A tax the city laid on foreign bills of exchange",
                   "The fee for opening an account with the bank",
                   "The premium of bank money over the same nominal sum of common currency",
                   "The share of its deposits the bank kept in reserve"],
             "c": 2,
             "why": "&ldquo;What is called bank money, is always of more value than the same "
                    "nominal sum of common currency&rdquo;, and the difference is the agio, "
                    "generally about five per cent. The account-opening fee was ten "
                    "guilders, and the bank professed to keep a guilder of coin or bullion "
                    "for every guilder it credited."},
            {"q": "In the preset <em>england-holland</em> the country's balance with "
                  "Holland is +£300,000 and the total is −£200,000. How can the country "
                  "have to send money to Holland?",
             "a": ["Because Holland charges seignorage on English coin",
                   "Because bills on Holland pay the Baltic ports, so Holland's debt is used "
                   "up and £200,000 is left to send",
                   "Because the English coin is above its standard weight",
                   "Because Smith holds that a favourable balance always loses money"],
             "c": 1,
             "why": "The Baltic balance is `200,000 − 700,000 = −500,000`. Holland's credit "
                    "of 300,000 is used up in paying it, and `500,000 − 300,000 = 200,000` "
                    "remains. Smith's sentence: England may be obliged to send money to "
                    "Holland &ldquo;though what is called the balance of trade may be very "
                    "much in favour of England&rdquo;."},
            {"q": "Which balance does Smith say decides whether a country's capital grows "
                  "or decays?",
             "a": ["The balance of the course of exchange with its chief partner",
                   "The balance of the custom-house books, once they are corrected",
                   "The balance of trade with the country that has the highest agio",
                   "The balance of annual produce and consumption"],
             "c": 3,
             "why": "&ldquo;This balance of produce and consumption is entirely different "
                    "from what is called the balance of trade.&rdquo; If produce exceeds "
                    "consumption the capital grows, and if it falls short the capital "
                    "decays. He calls the books and the exchange uncertain criteria."},
        ],
        "mistakes": [
            ("Reading the course of exchange as the balance of trade",
             "Smith gives three reasons the computed exchange differs from the real one: "
             "worn coin, the cost of coinage, and bank money. A premium on a bill shows "
             "that debts are not cancelling, and not why, and he adds that it is "
             "influenced by dealings with other places."),
            ("Thinking each pair of countries has to balance",
             "Debts are paid across partners, as in the Baltic case. A deficit with one "
             "partner and a surplus with another is an ordinary state, and Smith says in "
             "Chapter 6 that the more a balance appears to be in our favour with some "
             "countries, the more it must appear against us with many others."),
            ("Taking bank money for a lending machine",
             "The bank of Amsterdam professed to lend none of what was deposited, and "
             "bank money was worth more because it stood for coin of full weight. Smith "
             "allows that this may seem uncertain for deposits whose receipts expired "
             "long ago, then gives the burgomasters' oaths as reason to believe it, and "
             "the agio is explained by quality and convenience, and not by credit."),
        ],
        "standard": (
            "Finish when you can set a balance beside a gain and say what the exchange shows.",
            "Given the home value of what a country sends and of what comes back, compute "
            "the balance as the system counts it and the gain as Smith counts it, and say "
            "why the course of exchange does not decide the balance."
        ),
        "note": (
            "The lab prints the balance as stated figures give it, and has no way to check "
            "that a valuation is right, which was Smith's first complaint about the "
            "custom-house books. Tobacco and wine are Smith's figures, and every other figure "
            "in the lesson's presets was written for it. Whether a persistent deficit is "
            "harmless, as his half-century example says, is a question about what the "
            "deficit is spent on, and nothing here computes that. Capital's account "
            "of money crossing a border is a different one from Smith's and is not argued "
            "with here."
        ),
    },
]
