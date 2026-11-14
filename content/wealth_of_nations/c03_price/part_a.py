"""The Component Parts of Price, lessons 1-3 -- Book I, Chapters 6 and 7.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition); the comment beside each lesson gives
its line numbers. A drop capital in the text ("IN THAT", "THERE IS") is not
quoted. Smith's spelling is kept inside quotations.

Money: Smith reckons in pounds, shillings and pence, twelve pence to the
shilling and twenty shillings to the pound. The figures in the presets are
either Smith's, and the preset's label says so, or written for the lesson, and
the label says that.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 1556-1580 (the early and rude state); l. 1581-1598 (profit
    # of the undertaker); l. 1599-1622 (the two manufactories, l. 1601-1611);
    # l. 1631-1638 (rent); l. 1639-1661 (price resolves into three parts);
    # l. 1675-1682 (each profit greater than the foregoing); l. 1683-1697
    # (sea-fish, salmon, Scotch pebbles); l. 1711-1715 (the three original
    # sources); l. 1741-1766 (the confusions).
    {
        "slug": "wages-profit-and-rent",
        "title": "Wages, Profit and Rent",
        "module": "Book I, Chapter 6 · Of the Component Part of the Price of Commodities",
        "one_line": "Once stock is accumulated and land is owned, a price is no longer only the labour that made the thing: it resolves into wages, profit and rent.",
        "summary": (
            "Smith starts with hunters, where labour alone sets the rate of exchange, and "
            "adds the two things that change it: a master who advances stock and wants a "
            "profit in proportion to it, and a landlord who wants rent. Resolve the price "
            "of a batch of bread into wages, profit and rent stage by stage, and work "
            "Smith's two manufactories to see why profit is not the wages of "
            "superintendence."
        ),
        "key": [
            "price = wages + profit + rent, in the end",
            "profit follows the stock, not the toil",
            "each stage's profit is on all it advanced",
            "three original sources of all revenue",
        ],
        "key_label": "The chapter in four lines",
        "concepts_intro": (
            "Chapter 6 tells a short history, in three states of society, and then draws "
            "from it a rule about what any price is made of."
        ),
        "concepts": [
            ("Labour alone, in the early state",
             "Before stock is accumulated and land is appropriated, the whole produce of "
             "labour belongs to the labourer, and the quantity of labour a thing costs is "
             "&ldquo;the only circumstance&rdquo; that regulates what it exchanges for. "
             "A beaver that costs twice the labour of a deer is worth two deer, with "
             "some allowance for harder work or rarer skill."),
            ("Profit and rent enter the price",
             "Once a master supplies materials and subsistence to workmen, he must be "
             "repaid more than he advanced, and the more he advanced the more he expects. "
             "Once land is private property, the landlord charges for what had cost "
             "nothing but the gathering. So the price of the greater part of commodities "
             "has three parts, not one."),
            ("Resolving a price",
             "Whatever is paid for materials was itself made by labour, stock and land, so "
             "a price can be followed back through its stages until all of it has been "
             "assigned to wages, profit or rent. Smith adds that these are also the "
             "&ldquo;three original sources of all revenue&rdquo;: whoever has an income "
             "draws it from labour, from stock or from land."),
        ],
        "read_title": "Three states of society, then the rule",
        "read_intro": (
            "The chapter is short and its order matters: Smith lets each new party into "
            "the price one at a time, and only then states the general rule."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 6.</strong> &ldquo;If among a nation of hunters, "
                  "for example, it usually costs twice the labour to kill a beaver which it "
                  "does to kill a deer, one beaver should naturally exchange for or be worth "
                  "two deer.&rdquo;"),
            ("p", "This is the early and rude state of society that comes before stock and "
                  "before private land, and it is the nearest Smith comes to the case the "
                  "course on money and the measure of value was about: labour as the "
                  "measure of what a thing is worth. Smith allows two refinements even here. If one kind of labour is "
                  "more severe, some allowance is made for the hardship; if it needs "
                  "uncommon dexterity, the produce is worth more than the time spent on it, "
                  "which &ldquo;may frequently be no more than a reasonable compensation for "
                  "the time and labour which must be spent in acquiring&rdquo; the skill. "
                  "Then he closes the state off: the whole produce belongs to the labourer, "
                  "and the quantity of labour a thing costs is the only thing that governs "
                  "how much labour it ought to command."),
            ("p", "The second state begins when stock has accumulated in particular hands. "
                  "A man who owns stock sets industrious people to work, supplies them with "
                  "materials and subsistence, and sells what they make. In the price, Smith "
                  "says, &ldquo;something must be given for the profits of the undertaker of "
                  "the work&rdquo;. He puts it as a split of what the workmen add: &ldquo;The "
                  "value which the workmen add to the materials, therefore, resolves itself "
                  "in this case into two parts, of which the one pays their wages, the other "
                  "the profits of their employer upon the whole stock of materials and wages "
                  "which he advanced.&rdquo; The last words carry the point. The profit is "
                  "reckoned on everything the employer put up, the materials as well as the "
                  "wages."),
            ("def", ("Profit of stock",
                     "The part of a price that repays an employer for the stock he advanced "
                     "in materials and wages and pays him for hazarding it, in proportion "
                     "to the size of that stock. It is a revenue of the stock's owner, not "
                     "a payment for any labour he does.")),
            ("p", "An objection suggests itself, and Smith states it: profits may be only "
                  "&ldquo;a different name for the wages of a particular sort of "
                  "labour, the labour of inspection and direction&rdquo;. He answers with "
                  "a case. In a place where the common annual profit on manufacturing stock "
                  "is ten per cent, take two manufactories with twenty workmen each at "
                  "£15 a year, so £300 a year in wages in each. In one the materials cost "
                  "£700 a year and in the other £7,000, so the capitals are £1,000 and "
                  "£7,300. At ten per cent the first owner expects about £100 and the second "
                  "about £730, though &ldquo;their labour of inspection and direction may be "
                  "either altogether or very nearly the same&rdquo;. The clerk who does the "
                  "overseeing is paid by wages that bear no regular proportion to the "
                  "capital he oversees, while the owner, &ldquo;though he is thus discharged "
                  "of almost all labour, still expects that his profit should bear a regular "
                  "proportion to his capital&rdquo;. The lab's two Smith presets, "
                  "<code>coarse</code> and <code>fine</code>, run his figures: wages of "
                  "£300 and the same labour in both, profits of £100 and £730, and a price of "
                  "£1,100 against £8,030. The lab has no column for materials, so each "
                  "preset enters them as a first stage, the earlier hands who made them, "
                  "and counts their £700 or £7,000 as those hands' wages with no rent or "
                  "profit. That is the lab's assumption, not Smith's, and it is why the wage "
                  "tile reads £1,000 and £7,300: the owner's £300 and the earlier hands' "
                  "materials together. The whole profit is the owner's, so the profit tile "
                  "is Smith's comparison exactly."),
            ("p", "The third state brings in the landlord. &ldquo;As soon as the land of "
                  "any country has all become private property, the landlords, like all "
                  "other men, love to reap where they never sowed, and demand a rent even "
                  "for its natural produce.&rdquo; What had cost the labourer only the "
                  "trouble of gathering must now be paid for, and that portion, or its "
                  "price, &ldquo;constitutes the rent of land, and in the price of the "
                  "greater part of commodities, makes a third component part&rdquo;. Smith "
                  "says in the next paragraph how each part is to be valued: &ldquo;Labour "
                  "measures the value, not only of that part of price which resolves itself "
                  "into labour, but of that which resolves itself into rent, and of that "
                  "which resolves itself into profit.&rdquo; Each part is measured by the "
                  "labour it can buy, which is the measure the last course gave."),
            ("p", "Then comes the rule, and it is stated with care: &ldquo;In every "
                  "society, the price of every commodity finally resolves itself into some "
                  "one or other, or all of those three parts.&rdquo; Take corn. One part "
                  "pays the landlord's rent, one pays the wages of the labourers and "
                  "labouring cattle, one pays the farmer's profit. A fourth part to replace "
                  "the farmer's stock, a plough horse worn out, might seem needed. Smith "
                  "says it is not, because the horse's price is itself made of the same "
                  "parts, the rent of the land he was reared on, the labour of rearing him "
                  "and the profit of the farmer who advanced both, so that &ldquo;the whole "
                  "price still resolves itself, either immediately or ultimately, into the "
                  "same three parts of rent, labour, and profit.&rdquo; Capital argues with "
                  "this step, and its lesson <em>Former Discussions: Quesnay and "
                  "Smith</em> takes it up; this lesson only states what Smith says."),
            ("p", "The lab follows the chain in the text: corn, then the flour of the "
                  "miller, then the bread of the baker. Each stage adds its wages and "
                  "profit to the price it bought, and the profits grow as they go, because, "
                  "in Smith's words, &ldquo;every subsequent profit is greater than the "
                  "foregoing; because the capital from which it is derived must always be "
                  "greater.&rdquo; The bread preset is written for this "
                  "lesson, not Smith's. A farmer pays £40 in wages and £30 in rent, and the "
                  "ordinary profit is ten per cent. His advance is £70 and the price he "
                  "asks is £77. The miller buys that, adds £5 of wages, advances £82 and asks "
                  "£90.20. The baker adds £10 of wages, advances £100.20 and asks "
                  "£110.22. Add up what went to wages (£55), to rent (£30) and to profit "
                  "(£7, £8.20 and £10.02, which make £25.22) and you have the whole price, "
                  "with nothing over. A price with fewer parts is possible too. In the "
                  "fish preset a sea-fish pays wages and profit and no rent, and "
                  "in the pebbles preset the price paid to the poor people who "
                  "gather Scotch pebbles on the shore is &ldquo;altogether the wages of their "
                  "labour&rdquo;. Both are written for the lesson, after Smith's examples."),
            ("p", "Smith finishes with revenue. Wages, profit and rent &ldquo;are the three "
                  "original sources of all revenue, as well as of all exchangeable "
                  "value&rdquo;. Interest is a derivative revenue, a share of the "
                  "borrower's profit; taxes, salaries and pensions are paid from one of the "
                  "three. When the three belong to one person they are mixed up in common "
                  "language: the planter who farms his own estate calls his whole gain "
                  "profit, which confounds rent with profit; the independent manufacturer "
                  "calls his gain profit when part of it is wages; and the gardener who "
                  "works his own garden gets the rent of the landlord, the profit of the "
                  "farmer and the wages of the labourer, and calls it all the earnings of "
                  "his labour."),
            ("p", "Two things this chapter does not do. It does not say what fixes the "
                  "size of each part, only what a price is made of: the next lesson, and "
                  "four chapters after it, are about the rates. And later economists read it "
                  "differently. Ricardo, in 1817, held that labour still regulates "
                  "exchange after stock and land arrive, with profit and wage changes "
                  "modifying the ratios, and that rent is not a part of the price of "
                  "corn at all, since that price is set on land that pays none. Marx "
                  "argued that the resolution loses the part of the price that replaces "
                  "the means of production used up, the very fourth part that Smith's "
                  "horse was meant to dispose of. Smith died in 1790 and said nothing to either. "
                  "A fair complaint from any side is that a price made of three components "
                  "is not yet an explanation of the price, because each component is itself "
                  "a price."),
            ("p", "The next lesson, <em>Natural and Market Price</em>, takes the "
                  "ordinary rates of wages, profit and rent that this one assumed and asks "
                  "what happens when the market pays more or less than they come to."),
        ],
        "lab": ("wonkit", {
            "mode": "price",
            "view": "parts",
            "money_unit": "£",
            "preset": "bread",
            "presets": [
                {"id": "bread", "label": "Corn, flour and bread, written for this lesson",
                 "stages": [["farmer", 40, 30, 10],
                            ["miller", 5, 0, 10],
                            ["baker", 10, 0, 10]],
                 "expect": {
                    "wprFinal": "£110.22",
                    "wprResolved": "wages £55, rent £30, profit £25.22",
                    "wprStages": "farmer £77; miller £90.20; baker £110.22",
                 }},
                {"id": "fish", "label": "Sea-fish: wages and profit only, written for this lesson",
                 "stages": [["fishery", 60, 0, 10]],
                 "expect": {
                    "wprFinal": "£66",
                    "wprResolved": "wages £60, rent £0, profit £6",
                 }},
                {"id": "pebbles", "label": "Scotch pebbles: wages alone, written for this lesson",
                 "stages": [["gatherers", 20, 0, 0]],
                 "expect": {
                    "wprFinal": "£20",
                    "wprResolved": "wages £20, rent £0, profit £0",
                 }},
                {"id": "coarse", "label": "Smith's manufactory on £700 of materials (the materials counted as earlier wages, the lab's assumption)",
                 "stages": [["earlier-hands", 700, 0, 0],
                            ["twenty-workmen", 300, 0, 10]],
                 "expect": {
                    "wprStages": "earlier-hands £700; twenty-workmen £1,100",
                    "wprFinal": "£1,100",
                    "wprResolved": "wages £1,000, rent £0, profit £100",
                 }},
                {"id": "fine", "label": "Smith's manufactory on £7,000 of materials (the materials counted as earlier wages, the lab's assumption)",
                 "stages": [["earlier-hands", 7000, 0, 0],
                            ["twenty-workmen", 300, 0, 10]],
                 "expect": {
                    "wprStages": "earlier-hands £7,000; twenty-workmen £8,030",
                    "wprFinal": "£8,030",
                    "wprResolved": "wages £7,300, rent £0, profit £730",
                 }},
            ],
            "panel_title": "What a price is made of",
            "panel_intro": (
                "Each stage's wages, rent and rate of profit go in. The lab adds each "
                "stage's wages and rent to the price it bought, adds the stage's profit "
                "on all of that, and reports the final price and how it divides. The "
                "coarse and fine presets compare Smith's two manufactories."
            ),
        }),
        "steps_title": "Resolving a price stage by stage",
        "steps_intro": "Four steps, the same for corn, linen or anything made in stages.",
        "steps": [
            ("List the stages",
             "Write the producers in order from the land to the shop: farmer, miller, "
             "baker. A stage that uses no land has no rent, and a stage with no master has "
             "no profit."),
            ("Enter each stage's wages and rent",
             "These are the payments made at that stage, not earlier ones. The price "
             "bought from the stage before is carried forward on its own."),
            ("Add the profit on everything advanced",
             "Stage price = (price bought + wages + rent) · (1 + rate). The profit is "
             "the rate times the whole advance, the materials included."),
            ("Add up the parts",
             "Total the wages, the rents and the profits over all the stages. They sum to "
             "the final price. If they do not, a payment was counted twice or left out."),
        ],
        "worked": {
            "title": "A batch of bread, in three stages",
            "intro": [
                "Take the first preset: ordinary profit is ten per cent at every stage, and "
                "only the farmer pays rent.",
            ],
            "lines": [
                "farmer:  (0 + 40 + 30) · 1.1 = 77",
                "miller:  (77 + 5) · 1.1 = 90.2",
                "baker:  (90.2 + 10) · 1.1 = 110.22",
                "profits:  7 + 8.2 + 10.02 = 25.22",
                "wages 55 + rent 30 + profit 25.22 = 110.22",
            ],
            "after": [
                "The three parts return the price exactly. The baker's profit of £10.02 is "
                "larger than the farmer's £7, though he spent less on labour, because he "
                "advanced £100.20 against the farmer's £70.",
            ],
        },
        "quiz_title": "What a price is made of",
        "quiz": [
            {"q": "Smith's two manufactories each employ twenty workmen at £15 a year. One works "
                  "£700 of materials and the other £7,000, and ordinary profit is ten per cent. "
                  "About what profit does each owner expect?",
             "a": ["About £100 and £730",
                   "£30 each, because the labour of direction is the same",
                   "£70 and £700, a tenth of the materials alone",
                   "£300 each, the wages of the workmen"],
             "c": 0,
             "why": "Profit is a tenth of the whole stock advanced: £1,000 in the first and "
                    "£7,300 in the second. The same labour of direction gives the same wages "
                    "to a clerk, which is Smith's reason for saying profit is something else. "
                    "A tenth of the materials alone leaves out the £300 of wages advanced, and "
                    "£300 is the wage bill, not a profit."},
            {"q": "Following Smith's chapter, what are the parts of the price of sea-fish in "
                  "the ordinary case?",
             "a": ["Wages alone",
                   "Wages, profit and rent, always",
                   "Wages and profit, because rent seldom enters it",
                   "Profit alone, because the sea is free"],
             "c": 2,
             "why": "In the price of sea-fish, &ldquo;one part pays the labour of the fisherman, and the other the "
                    "profits of the capital employed in the fishery&rdquo;. Rent &ldquo;very "
                    "seldom makes any part of it&rdquo;. Wages alone is Smith's case of the "
                    "Scotch pebbles, and the salmon fishery is his example where a rent does "
                    "enter."},
            {"q": "On the first preset, the miller buys at £77, pays £5 in wages and takes "
                  "ten per cent profit. What is his profit?",
             "a": ["£7.70", "£8.20", "£0.50", "£9.02"],
             "c": 1,
             "why": "The advance is £77 + £5 = £82, and a tenth of it is £8.20. £7.70 is a "
                    "tenth of the price he bought alone, which leaves out the wages he "
                    "advanced; £0.50 is a tenth of the wages alone; £9.02 is a tenth of the "
                    "price he sells at."},
            {"q": "What does Smith say a gardener who cultivates his own garden with his own "
                  "hands receives, whatever he calls it?",
             "a": ["Only the wages of his labour",
                   "Profit and wages, because no one pays himself rent",
                   "Rent only, because he owns the ground",
                   "The rent of a landlord, the profit of a farmer and the wages of a labourer"],
             "c": 3,
             "why": "He &ldquo;unites in his own person the three different characters, of "
                    "landlord, farmer, and labourer&rdquo;, so his produce should pay him all "
                    "three revenues, though it &ldquo;is commonly considered as the earnings "
                    "of his labour&rdquo;. Wages alone is the common way of speaking that "
                    "Smith is correcting."},
        ],
        "mistakes": [
            ("Taking profit for the owner's wages of management",
             "Smith raises this himself and answers it with the two manufactories: the "
             "labour of oversight is the same, the profits are £100 and £730, and the owner "
             "still expects his profit in proportion to his capital. The clerk's wages are "
             "the pay for the oversight."),
            ("Adding a fourth part to replace the stock",
             "A horse or a plough wears out, and the price of the corn pays for it. Smith's "
             "answer is that the horse's own price is rent, labour and profit of earlier "
             "hands, so nothing is added to the three. Whether that answer is enough is the "
             "point Capital disputes."),
            ("Reading the rule as a theory of how large each part is",
             "The chapter says what a price is made of and where revenue comes from. "
             "It does not say why wages are £55 in the lab or profit ten per cent: those "
             "are inputs, and the next chapters give Smith's account of them."),
        ],
        "standard": (
            "Finish when you can resolve a price into wages, profit and rent through its stages.",
            "Given each stage's wages, rent and rate of profit, compute the price after each "
            "stage and the total wages, rent and profit it resolves into, and say why a "
            "stage's profit is reckoned on everything advanced."
        ),
        "note": (
            "The lab adds up a price built by the rule of the chapter, so the three parts "
            "always return the price: that is how it is made, not a finding. What it cannot "
            "show is whether prices are built that way, or what fixes the wages, the "
            "rents and the ten per cent, which are entered. The two manufactories are "
            "Smith's; the bread, the fish and the pebbles are written for the lesson. "
            "Ricardo and Marx each objected to the rule, and the lab takes no side."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 1788-1799 (natural rates); l. 1800-1820 (natural price);
    # l. 1821-1864 (market price and effectual demand); l. 1865-1893 (the
    # quantity suits itself; gravitation); l. 1894-1957 (corn and linen,
    # fluctuations in parts of price, the public mourning).
    {
        "slug": "natural-and-market-price",
        "title": "Natural and Market Price",
        "module": "Book I, Chapter 7 · Of the Natural and Market Price of Commodities",
        "one_line": "A price that pays every part at its ordinary rate is natural; the market price sits above or below it as the quantity brought falls short of or exceeds the effectual demand.",
        "summary": (
            "Smith calls the ordinary rates of wages, profit and rent natural, and the price "
            "that pays exactly those the natural price. The price actually paid, the market "
            "price, is set by how much is brought against how much buyers will take at the "
            "natural price, and the interests of landlords, labourers and employers push "
            "it back. Work a short supply and a glut against a buyers' schedule written "
            "for the lesson."
        ),
        "key": [
            "natural price = parts at their natural rates",
            "effectual demand: buyers at the natural price",
            "short supply: market price above natural",
            "glut: market price below natural",
        ],
        "key_label": "Natural and market price in four lines",
        "concepts_intro": (
            "Three ideas carry the chapter, and the second is the one the word demand "
            "usually hides."
        ),
        "concepts": [
            ("The natural price",
             "In every neighbourhood there is an ordinary rate of wages, of profit and of "
             "rent. A commodity whose price pays all three at those rates is sold at its "
             "natural price. <em>Natural</em> here means usual and sufficient, not "
             "fair: below it, the dealer would lose by the trade."),
            ("Effectual demand",
             "Only those willing to pay the natural price count as the effectual "
             "demand, because only they can bring the commodity to market at all. A wish "
             "for a thing that nobody will pay the cost of making is a demand in a looser "
             "sense, but it does not make anyone produce."),
            ("Gravitation",
             "When less than the effectual demand is brought, competition among buyers lifts "
             "the market price above the natural price. When more is brought, competition "
             "among sellers pulls it below. Whoever is paid above or below the natural rate "
             "moves land, labour or stock in or out, and the price returns."),
        ],
        "read_title": "The natural price first, then what disturbs it",
        "read_intro": (
            "The chapter has an even order: a definition, the two ways a market can miss "
            "it, the mechanism that corrects the miss, and then the exceptions, which are "
            "the next lesson."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 7.</strong> &ldquo;When the price of any "
                  "commodity is neither more nor less than what is sufficient to pay the rent "
                  "of the land, the wages of the labour, and the profits of the stock employed "
                  "in raising, preparing, and bringing it to market, according to their "
                  "natural rates, the commodity is then sold for what may be called its "
                  "natural price.&rdquo;"),
            ("p", "Read <em>natural</em> as ordinary. Smith has just said that in "
                  "every society there is an ordinary or average rate of wages and profit in "
                  "each employment, and of rent in each place, and &ldquo;These ordinary or "
                  "average rates may be called the natural rates of wages, profit and rent, "
                  "at the time and place in which they commonly prevail.&rdquo; Nothing "
                  "about justice is claimed. The word does a job in his argument: the natural "
                  "price is the one a dealer can go on selling at. If it does not leave "
                  "him the ordinary profit of his neighbourhood he is losing by the trade, "
                  "because he could have made that profit by employing his stock another way. "
                  "That is why the natural price, while not always the lowest a dealer may "
                  "sometimes sell at, is &ldquo;the lowest at which he is likely to sell them "
                  "for any considerable time&rdquo;, where he can change his trade as often as "
                  "he pleases."),
            ("def", ("Effectual demand",
                     "The demand of those who are willing to pay the natural price of a "
                     "commodity, the whole of its rent, wages and profit. Smith contrasts it "
                     "with absolute demand, a mere wish.")),
            ("p", "The market price is simply the price at which the commodity is "
                  "actually sold, and it may be above, below or exactly the same as "
                  "its natural price. What decides it is a proportion: "
                  "the quantity brought to market against the effectual demand. Smith "
                  "marks the distinction with a coach: &ldquo;A very poor man may be said, "
                  "in some sense, to have a demand for a coach and six; he might like to have "
                  "it; but his demand is not an effectual demand, as the commodity can never "
                  "be brought to market in order to satisfy it.&rdquo;"),
            ("p", "If less is brought than the effectual demand, some who would pay the "
                  "natural price cannot be supplied. &ldquo;Rather than want it altogether, "
                  "some of them will be willing to give more. A competition will immediately "
                  "begin among them&rdquo;, and the price rises more or less according to the "
                  "size of the shortage and to the wealth and eagerness of the buyers, which "
                  "is why the necessaries of life are so dear in a blockade or a famine. If "
                  "more is brought than the effectual demand, &ldquo;Some part must be sold "
                  "to those who are willing to pay less, and the low price which they give "
                  "for it must reduce the price of the whole.&rdquo; How far it falls depends "
                  "on the sellers' hurry. A glut of oranges is a worse glut than the same "
                  "weight of old iron, because oranges perish."),
            ("p", "The lab puts a schedule behind this, and the schedule is the lab's, not "
                  "Smith's: he gives no table of what buyers would take at each price. In "
                  "all three presets the natural price is 10 shillings a yard of cloth, the "
                  "effectual demand 1,000 yards, and buyers would take 1,300 yards at 8 "
                  "shillings, 1,000 at 10, 900 at 12, 800 at 14, 700 at 16 and 600 at 18. The "
                  "lab's rule, which is its own and not Smith's, is that the market price is "
                  "the highest listed price at which buyers take at least the quantity "
                  "brought. In the short preset, 800 yards come to market and "
                  "buyers take that many at 14 shillings, four above the natural price, and "
                  "the sellers receive 3,200 shillings more than the natural price would "
                  "have brought for those 800 yards. In the glut preset 1,300 "
                  "are brought, the only listed price at which buyers take them all is 8, and "
                  "the market price falls two shillings below the natural price on all 1,300, "
                  "2,600 shillings in all. "
                  "In the match preset 1,000 are brought and the price is 10: "
                  "&ldquo;The competition of the different dealers obliges them all to accept "
                  "of this price, but does not oblige them to accept of less.&rdquo;"),
            ("p", "Then the mechanism. &ldquo;If at any time it exceeds the effectual "
                  "demand, some of the component parts of its price must be paid below "
                  "their natural rate.&rdquo; Which part, depends on whose they are. If it "
                  "is rent, landlords withdraw land; if wages, labourers withdraw labour; if "
                  "profit, employers withdraw stock, and the quantity falls until the price "
                  "comes back. A shortfall works the other way, and others bring in more. "
                  "&ldquo;The natural price, therefore, is, as it were, the central price, "
                  "to which the prices of all commodities are continually gravitating.&rdquo; "
                  "Accidents may hold prices above or push them below, but they are always "
                  "&ldquo;constantly tending towards it&rdquo;."),
            ("p", "Smith adds that industries differ in how steadily they can aim at the "
                  "effectual demand. The same labourers in husbandry, in different years, "
                  "produce very different quantities of corn, wine or hops, while the same "
                  "spinners and weavers make nearly the same cloth each year. Corn's market "
                  "price therefore swings with the harvest as well as with demand, and linen's "
                  "only with demand. The swings fall mostly on the parts of price that are "
                  "wages and profit, much less on rent, because a landlord and a farmer "
                  "fix the rent by the average price and not the year's."),
            ("p", "His example is a public mourning. &ldquo;A public mourning raises the "
                  "price of black cloth&rdquo;, which the market is understocked with, and "
                  "so raises the profits of the merchants who hold it; it does not touch the "
                  "wages of the weavers, because the market is understocked with commodities "
                  "and not with labour. But it does raise the wages of journeymen tailors, "
                  "for &ldquo;The market is here understocked with labour.&rdquo; The same "
                  "event pushes different parts of different prices up and down."),
            ("p", "Later writers took the idea and changed it. Ricardo adopted a "
                  "natural price and a market price, with the natural price set by cost of "
                  "production. Alfred Marshall, in 1890, compared demand and supply to the "
                  "two blades of a pair of scissors, so that neither alone cuts the price. "
                  "Marx's counterpart to Smith's natural price, the price of production, "
                  "is the subject of the Capital lesson <em>The General Rate of Profit and "
                  "Prices of Production</em>. Objection to Smith's version comes from "
                  "two quarters: that it says nothing about how long the return takes, and "
                  "that it assumes land, labour and stock can move freely and quickly, "
                  "which Smith himself qualifies with &ldquo;where there is perfect "
                  "liberty&rdquo;."),
            ("p", "The next lesson, <em>Monopoly and the Natural Price</em>, reads the "
                  "end of the chapter: the cases where the market price stays above the "
                  "natural price for years, for centuries, or for as long as a law says."),
        ],
        "lab": ("wonkit", {
            "mode": "price",
            "view": "market",
            "money_unit": "s",
            "qty_unit": "yards",
            "preset": "short",
            "presets": [
                {"id": "short", "label": "800 yards brought, a shortage, schedule written for the lesson",
                 "natural": 10, "effectual": 1000, "brought": 800,
                 "buyers": [[8, 1300], [10, 1000],
                            [12, 900], [14, 800],
                            [16, 700], [18, 600]],
                 "expect": {
                    "wprPosition": "above the natural price: less is brought (800) than the effectual demand (1,000)",
                    "wprGap": "shortfall of 200 yards",
                    "wprMarketPrice": "14s a unit",
                    "wprUnitGap": "+4s a unit above the natural price",
                    "wprAllGap": "+3,200s over the 800 yards brought",
                 }},
                {"id": "match", "label": "1,000 yards brought, the effectual demand, schedule written for the lesson",
                 "natural": 10, "effectual": 1000, "brought": 1000,
                 "buyers": [[8, 1300], [10, 1000],
                            [12, 900], [14, 800],
                            [16, 700], [18, 600]],
                 "expect": {
                    "wprPosition": "at the natural price: the quantity brought equals the effectual demand (1,000)",
                    "wprGap": "none",
                    "wprMarketPrice": "10s a unit",
                    "wprUnitGap": "0s a unit at the natural price",
                    "wprAllGap": "0s over the 1,000 yards brought",
                 }},
                {"id": "glut", "label": "1,300 yards brought, a glut, schedule written for the lesson",
                 "natural": 10, "effectual": 1000, "brought": 1300,
                 "buyers": [[8, 1300], [10, 1000],
                            [12, 900], [14, 800],
                            [16, 700], [18, 600]],
                 "expect": {
                    "wprPosition": "below the natural price: more is brought (1,300) than the effectual demand (1,000)",
                    "wprGap": "excess of 300 yards",
                    "wprMarketPrice": "8s a unit",
                    "wprUnitGap": "−2s a unit below the natural price",
                    "wprAllGap": "−2,600s over the 1,300 yards brought",
                 }},
            ],
            "panel_title": "Where the market price lands",
            "panel_intro": (
                "The natural price, the effectual demand and the quantity brought go in, "
                "with a schedule of what buyers would take at each price. The lab compares "
                "the quantity brought with the effectual demand and finds the price at which "
                "buyers take all of it."
            ),
        }),
        "steps_title": "Placing a market price against the natural price",
        "steps_intro": "Four steps, for any commodity whose parts are known.",
        "steps": [
            ("Find the natural price",
             "Add the rent, wages and profit at their ordinary rates for one unit. That is "
             "the price that leaves everyone their natural rate and no more."),
            ("Find the effectual demand",
             "Count the units buyers would take at the natural price. This is the quantity "
             "that the natural price can call forth."),
            ("Compare the quantity brought",
             "More than the effectual demand means a market price below natural; less means "
             "above; equal means at it."),
            ("Read the price from the buyers' schedule",
             "Smith gives no schedule. On a schedule you supply, take the highest listed "
             "price at which buyers take at least the quantity brought, and multiply its "
             "gap to the natural price by the quantity."),
        ],
        "worked": {
            "title": "A shortage of 200 yards",
            "intro": [
                "Take the short preset: the natural price is 10 shillings and "
                "the effectual demand is 1,000 yards. Only 800 are brought.",
            ],
            "lines": [
                "brought against demand:  800 < 1000",
                "shortfall:  1000 − 800 = 200 yards",
                "highest price taking 800:  14 s",
                "gap to the natural price:  14 − 10 = 4 s",
                "over the quantity brought:  4 · 800 = 3200 s",
            ],
            "after": [
                "Sellers of those 800 yards receive 3,200 shillings more than the natural "
                "price pays. On Smith's account that excess is paid to one or more of the "
                "parts of price: to the profits of those who hold the cloth, or the wages "
                "of those who work it up, until others bring more.",
            ],
        },
        "quiz_title": "Natural price and market price",
        "quiz": [
            {"q": "On the lesson's schedule, buyers take 1,300 yards at 8 s, 1,000 at 10 s, "
                  "900 at 12 s and 800 at 14 s. The natural price is 10 s. With 1,300 yards "
                  "brought, what is the market price on the lab's rule?",
             "a": ["8 s, two shillings below the natural price",
                   "10 s, the natural price",
                   "12 s, two shillings above it",
                   "14 s, four shillings above it"],
             "c": 0,
             "why": "1,300 yards exceed the effectual demand of 1,000, and the only listed "
                    "price at which buyers take 1,300 is 8 s. At 10 s they take only 1,000, "
                    "so some yards would go unsold. A glut brings the price below the natural "
                    "price, never above it."},
            {"q": "Which commodity's market price does Smith say varies more from year to "
                  "year with the quantity brought, linen or corn?",
             "a": ["Linen, because weaving is steadier than farming",
                   "Corn, because the same labour yields very different harvests",
                   "Both equally, because demand is the same for each",
                   "Neither, because both are necessaries"],
             "c": 1,
             "why": "The same number of labourers in husbandry will, in different years, "
                    "&ldquo;produce very different quantities of corn&rdquo;, while the same "
                    "spinners and weavers make nearly the same linen. So corn's price varies "
                    "with the harvest as well as with demand, linen's with demand only."},
            {"q": "Smith says a very poor man has a demand for a coach and six. In his terms "
                  "that demand is:",
             "a": ["an effectual demand, because he would like to have it",
                   "no demand at all, because he cannot pay",
                   "a demand in some sense, but not an effectual demand",
                   "an effectual demand once the market price falls"],
             "c": 2,
             "why": "&ldquo;he might like to have it; but his demand is not an effectual "
                    "demand, as the commodity can never be brought to market in order to "
                    "satisfy it.&rdquo; Smith grants the wish a place &ldquo;in some "
                    "sense&rdquo;, so saying it is no demand at all overstates him, and the "
                    "wish alone is not what makes anyone produce."},
            {"q": "More is brought to market than the effectual demand. What does Smith say "
                  "brings the quantity back?",
             "a": ["Buyers' wishes grow until they take it all",
                   "Sellers agree among themselves to hold the price at its natural level",
                   "The natural price falls to meet the market price",
                   "Landlords, labourers or employers who are paid below the natural rate "
                   "withdraw land, labour or stock"],
             "c": 3,
             "why": "&ldquo;If it is rent, the interest of the landlords will immediately "
                    "prompt them to withdraw a part of their land; and if it is wages or "
                    "profit, the interest of the labourers in the one case, and of their "
                    "employers in the other, will prompt them to withdraw a part of their "
                    "labour or stock.&rdquo; The other answers describe things Smith does "
                    "not say here."},
        ],
        "mistakes": [
            ("Taking natural to mean fair or just",
             "Smith's natural rates are the ordinary or average rates of a time and place. A "
             "natural price may sit on low wages if those are the going wages, and "
             "he says nothing in this chapter to praise it."),
            ("Taking every want for demand",
             "Effectual demand is the demand of those willing to pay the whole natural price, "
             "which is what can bring a commodity to market at all. In the lab, the effectual "
             "demand is entered and the schedule of buyers is separate; a wish with no "
             "money behind it appears in neither."),
            ("Expecting the market price to be the natural price",
             "The natural price is the centre the market price keeps coming back to, "
             "not the price on any given day. In the lab the three presets sit at, below "
             "and above it, and each of the three is an ordinary state of a market."),
        ],
        "standard": (
            "Finish when you can say whether a market price is above, at or below the natural price.",
            "Given the natural price, the effectual demand and the quantity brought, say "
            "whether the market price is above, at or below the natural price, and which "
            "way the quantity is pushed to move."
        ),
        "note": (
            "The lab's schedule of buyers and its rule for the market price are written for "
            "the lesson; Smith gives neither. It also cannot say how fast the return to "
            "the natural price happens, or whether land, labour and stock move as freely "
            "as Smith assumes, and it does not say which of the three parts of price "
            "absorbs the excess. The figures are in shillings of the lesson, not Smith's "
            "prices."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 1958-1986 (secrets in trade and manufactures; the dyer);
    # l. 1987-2009 (natural scarcity, the French vineyards); l. 2010-2034
    # (monopoly and corporations); l. 2035-2062 (below the natural price);
    # l. 2063-2092 (the plan of the next chapters).
    {
        "slug": "monopoly-and-the-natural-price",
        "title": "Monopoly and the Natural Price",
        "module": "Book I, Chapter 7 · Of the Natural and Market Price of Commodities",
        "one_line": "A secret, a scarce soil or a privilege can keep the market under-stocked, and the price of monopoly is the highest which can be got.",
        "summary": (
            "The end of Chapter 7 asks what can hold a market price above the natural price "
            "for years: a trade or manufacturing secret, a natural scarcity such as a "
            "particular vineyard, and a monopoly or a corporation's privilege. Run a "
            "monopolist's choice of quantity against a buyers' schedule written for the "
            "lesson and see the price and the excess over the natural price at each."
        ),
        "key": [
            "monopoly keeps the market under-stocked",
            "monopoly price: the highest which can be got",
            "natural price: the lowest for long",
            "a scarce vineyard raises rent, not wages",
        ],
        "key_label": "Monopoly and the natural price",
        "concepts_intro": (
            "Smith's list of what keeps a market price up has three kinds of entry, and "
            "they differ in how long they last."
        ),
        "concepts": [
            ("Secrets",
             "A trader who learns that demand has risen conceals it, so that rivals do not "
             "crowd in; a manufacturer with a secret process can hold it for life. The "
             "extra gains last as long as the secret."),
            ("Natural scarcity",
             "Some goods, a wine from one slope for instance, can be grown on so little "
             "land that no one can ever supply the whole effectual demand. The excess price "
             "is paid to the land, as rent, and the high price may last for centuries."),
            ("Monopoly and privilege",
             "A monopoly keeps the market understocked by never fully supplying the demand. "
             "Corporations and statutes of apprenticeship are &ldquo;a sort of enlarged "
             "monopolies&rdquo;. Their effect lasts as long as the law that gives them."),
        ],
        "read_title": "What keeps a price up, and for how long",
        "read_intro": (
            "These pages are the end of Chapter 7. They answer a question the "
            "chapter's rule leaves open: if a price always gravitates to the natural "
            "price, how can it stay above?"
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 7.</strong> &ldquo;The price of monopoly is upon "
                  "every occasion the highest which can be got. The natural price, or the "
                  "price of free competition, on the contrary, is the lowest which can be "
                  "taken, not upon every occasion indeed, but for any considerable time "
                  "together.&rdquo;"),
            ("p", "Smith comes to this sentence last, after three kinds of case. The first "
                  "is the secret. When a rise in the effectual demand lifts the market price "
                  "well above the natural price, &ldquo;those who employ their stocks in "
                  "supplying that market, are generally careful to conceal this "
                  "change&rdquo;, because if it were known, so many rivals would come in "
                  "that the price would fall again, perhaps below the natural price for a "
                  "while. If the market is far away, the secret may be kept for years, but "
                  "&ldquo;Secrets of this kind, however, it must be acknowledged, can seldom "
                  "be long kept&rdquo;. Secrets in manufactures last longer. His example "
                  "is a dyer who finds a way of producing a colour with materials that cost "
                  "half as much, and may enjoy the advantage as long as he lives and leave it "
                  "to his heirs."),
            ("p", "Smith says exactly what these gains are, and that deserves a second "
                  "look. The dyer's extraordinary gains &ldquo;arise from the high price which "
                  "is paid for his private labour. They properly consist in the high wages "
                  "of that labour.&rdquo; But the advantage repeats on every part of his stock, "
                  "so the whole amount is in proportion to his stock, &ldquo;they are "
                  "commonly considered as extraordinary profits of stock&rdquo;. That is "
                  "the sort of mix-up the last lesson ended on: a revenue of one name "
                  "that belongs to another. Later writers made more of this kind of gain. "
                  "Schumpeter argued in 1942 that the prospect of a temporary advantage of "
                  "this kind is what drives invention and that a market with no such "
                  "prize would have less of it; Smith does not take that step, and treats "
                  "the gain as a departure from the natural price."),
            ("p", "The second kind is the natural scarcity. Some natural productions need "
                  "&ldquo;such a singularity of soil and situation&rdquo; that all the land "
                  "fit to produce them may not supply the effectual demand, and then the "
                  "whole quantity is sold to those willing to pay more than the natural "
                  "price. &ldquo;Such commodities may continue for whole centuries together "
                  "to be sold at this high price; and that part of it which resolves itself "
                  "into the rent of land, is in this case the part which is generally paid "
                  "above its natural rate.&rdquo; The French vineyards of a peculiarly "
                  "happy soil pay a rent that &ldquo;bears no regular proportion to the rent "
                  "of other equally fertile and equally well cultivated land in its "
                  "neighbourhood&rdquo;, while the wages and the profits employed there are "
                  "&ldquo;seldom out of their natural proportion&rdquo;. This is the first "
                  "appearance of an idea that Chapter 11, in the course on rent, builds on: that "
                  "rent can be a consequence of price and not its cause."),
            ("p", "The third kind is monopoly itself. &ldquo;The monopolists, by keeping the "
                  "market constantly understocked by never fully supplying the effectual "
                  "demand, sell their commodities much above the natural price, and raise "
                  "their emoluments, whether they consist in wages or profit, greatly above "
                  "their natural rate.&rdquo; Corporations and the statutes of apprenticeship "
                  "&ldquo;are a sort of enlarged monopolies&rdquo; and may keep wages and "
                  "profits above their natural rate for ages together. The course after "
                  "next, in its lesson <em>Apprenticeship and Corporations</em>, takes "
                  "these up with their own figures."),
            ("p", "The lab can show the shape of this, with a schedule that is the "
                  "lab's and not Smith's. The natural price is 10 shillings a yard and the "
                  "effectual demand 1,000 yards, and buyers would take 1,300 yards at 8 "
                  "shillings, 1,000 at 10, 900 at 12, 800 at 14, 700 at 16, 600 at 18, 500 at "
                  "20 and 400 at 22. Bring the effectual demand to market, in the free "
                  "preset, and the price is the natural 10 and there is nothing over. Keep "
                  "800 back in the m800 preset and the price rises to 14; keep 500 back in "
                  "the m500 preset and it is 20; in the m400 preset it is 22. The excess "
                  "over the natural price, taken over the quantity brought, is 3,200, "
                  "5,000 and 4,800 shillings."),
            ("p", "Notice that the highest price is not the largest gain. Smith's sentence "
                  "says the price of monopoly is &ldquo;upon every occasion the highest which "
                  "can be got&rdquo;, and it is, for the quantity actually brought. Keep "
                  "back more and the price per yard is higher still, in this schedule. "
                  "But fewer yards are sold, and the total excess over the natural price "
                  "rises to 5,000 shillings at 500 yards and then falls to 4,800 at 400. "
                  "Taking the natural price as the cost of a yard at every quantity, which "
                  "is a simplification of the lab and not Smith's, the monopolist who "
                  "wants the most would stop at 500. Augustin Cournot, in 1838, "
                  "worked this out as a problem of choosing a quantity; Smith's chapter "
                  "states the result in its plainest form and does not set the problem."),
            ("p", "The last pages are about the other side. &ldquo;The market price of any "
                  "particular commodity, though it may continue long above, can seldom "
                  "continue long below, its natural price&rdquo;: whoever is paid below the "
                  "natural rate withdraws land, labour or stock at once. The statutes of "
                  "apprenticeship that raise a workman's wages in a prosperous trade may "
                  "hold them down when it decays, but with less force, for their effect "
                  "&ldquo;is not near so durable in sinking the workman's wages below, as in "
                  "raising them above their natural rate&rdquo;. Only a policy as violent as "
                  "the castes of Indostan or ancient Egypt could keep wages or profit below "
                  "the natural rate for generations."),
            ("p", "Smith closes the chapter by saying that the natural price itself "
                  "&ldquo;varies with the natural rate of each of its component parts&rdquo; "
                  "and listing four tasks for the four chapters that follow: the rate of "
                  "wages, the rate of profit, the proportions between wages and profits "
                  "in different employments, and the rent of land. There is a question "
                  "his chapter leaves open that critics have kept asking: in which case "
                  "is a price above the natural price a monopoly, and in which a reward? "
                  "The chapter marks it out, but does not draw the line."),
            ("p", "The next course, <em>Wages and Profits</em>, begins with the first of "
                  "those tasks: what determines the wages of labour."),
        ],
        "lab": ("wonkit", {
            "mode": "price",
            "view": "market",
            "money_unit": "s",
            "qty_unit": "yards",
            "preset": "m500",
            "presets": [
                {"id": "free", "label": "1,000 yards brought, free competition, schedule written for the lesson",
                 "natural": 10, "effectual": 1000, "brought": 1000,
                 "buyers": [[8, 1300], [10, 1000],
                            [12, 900], [14, 800],
                            [16, 700], [18, 600],
                            [20, 500], [22, 400]],
                 "expect": {
                    "wprMarketPrice": "10s a unit",
                    "wprUnitGap": "0s a unit at the natural price",
                    "wprAllGap": "0s over the 1,000 yards brought",
                 }},
                {"id": "m800", "label": "A monopolist brings 800, schedule written for the lesson",
                 "natural": 10, "effectual": 1000, "brought": 800,
                 "buyers": [[8, 1300], [10, 1000],
                            [12, 900], [14, 800],
                            [16, 700], [18, 600],
                            [20, 500], [22, 400]],
                 "expect": {
                    "wprMarketPrice": "14s a unit",
                    "wprUnitGap": "+4s a unit above the natural price",
                    "wprAllGap": "+3,200s over the 800 yards brought",
                 }},
                {"id": "m500", "label": "A monopolist brings 500, schedule written for the lesson",
                 "natural": 10, "effectual": 1000, "brought": 500,
                 "buyers": [[8, 1300], [10, 1000],
                            [12, 900], [14, 800],
                            [16, 700], [18, 600],
                            [20, 500], [22, 400]],
                 "expect": {
                    "wprMarketPrice": "20s a unit",
                    "wprUnitGap": "+10s a unit above the natural price",
                    "wprAllGap": "+5,000s over the 500 yards brought",
                 }},
                {"id": "m400", "label": "A monopolist brings 400, schedule written for the lesson",
                 "natural": 10, "effectual": 1000, "brought": 400,
                 "buyers": [[8, 1300], [10, 1000],
                            [12, 900], [14, 800],
                            [16, 700], [18, 600],
                            [20, 500], [22, 400]],
                 "expect": {
                    "wprMarketPrice": "22s a unit",
                    "wprUnitGap": "+12s a unit above the natural price",
                    "wprAllGap": "+4,800s over the 400 yards brought",
                 }},
            ],
            "panel_title": "What keeping the market short is worth",
            "panel_intro": (
                "The same schedule as before, with two more rows at the top. Choose the "
                "quantity the seller brings and read the price at which buyers take all of "
                "it, and the gap to the natural price over that quantity."
            ),
        }),
        "steps_title": "Reading a monopolist's choice",
        "steps_intro": "Four steps, on a buyers' schedule you are given.",
        "steps": [
            ("Fix the natural price and the schedule",
             "The natural price pays every part of one unit at its natural rate, so for the "
             "lab it is also what a unit costs the seller."),
            ("Pick a quantity to bring",
             "Under free competition it is the effectual demand. A monopolist may bring "
             "less."),
            ("Read the price the schedule gives for it",
             "The highest listed price at which buyers take at least that quantity."),
            ("Multiply the gap by the quantity",
             "(price − natural price) · quantity is the excess over what the natural price "
             "would have paid. Compare it across quantities, not just the prices."),
        ],
        "worked": {
            "title": "Three quantities, one schedule",
            "intro": [
                "Use the schedule above with the natural price 10 shillings a yard, and "
                "compare 800, 500 and 400 yards.",
            ],
            "lines": [
                "800 yards:  (14 − 10) · 800 = 3200 s",
                "500 yards:  (20 − 10) · 500 = 5000 s",
                "400 yards:  (22 − 10) · 400 = 4800 s",
                "1000 yards:  (10 − 10) · 1000 = 0 s",
            ],
            "after": [
                "The price rises with each step of withholding, but the excess peaks at 500 "
                "yards on this schedule. The highest price, 22 shillings at 400 yards, is "
                "not the largest gain.",
            ],
        },
        "quiz_title": "Monopoly and the natural price",
        "quiz": [
            {"q": "Buyers take 1,000 yards at 10 s, 600 at 18 s, 500 at 20 s and 400 at 22 s. "
                  "The natural price is 10 s. A seller brings 500 yards. What price clears "
                  "them on the lab's rule?",
             "a": ["10 s", "18 s", "22 s", "20 s"],
             "c": 3,
             "why": "The highest listed price at which buyers take at least 500 yards is "
                    "20 s. At 22 s they take only 400, so 100 of the 500 would be unsold. "
                    "18 s is a price at which they would take more than 500, so a seller "
                    "need not accept so little, and 10 s is the natural price, which clears "
                    "1,000."},
            {"q": "In Smith's account of the French vineyards of peculiar soil, which part of "
                  "the price is paid above its natural rate?",
             "a": ["The wages of the vine-dressers", "The profits of the growers",
                   "The rent of the land", "All three, in equal degree"],
             "c": 2,
             "why": "&ldquo;that part of it which resolves itself into the rent of land, is in "
                    "this case the part which is generally paid above its natural "
                    "rate.&rdquo; The wages and profits there are &ldquo;seldom out of their "
                    "natural proportion&rdquo; to those of other employments nearby."},
            {"q": "What does Smith say the dyer's extraordinary gains from a cheap secret "
                  "process properly consist in?",
             "a": ["Interest on the money he lent",
                   "The high wages of his private labour",
                   "The rent of his dye-works",
                   "A monopoly granted by the crown"],
             "c": 1,
             "why": "&ldquo;They properly consist in the high wages of that labour.&rdquo; "
                    "Because they are repeated on every part of his stock, he adds, they are "
                    "&ldquo;commonly considered as extraordinary profits of stock&rdquo;. "
                    "Smith's dyer has no privilege; his secret is his own."},
            {"q": "On the lesson's schedule and with the natural price as the cost of a yard, "
                  "which of these quantities brings the seller the largest excess over the "
                  "natural price?",
             "a": ["500 yards", "800 yards", "1,000 yards", "400 yards"],
             "c": 0,
             "why": "The excess is (price − 10) · quantity: 0 at 1,000 yards, 3,200 at 800, "
                    "5,000 at 500 and 4,800 at 400. The price is highest at 400, but fewer "
                    "yards are sold."},
        ],
        "mistakes": [
            ("Reading &ldquo;the highest which can be got&rdquo; as the monopolist's best choice",
             "&ldquo;the highest which can be got&rdquo; is the highest for the quantity "
             "brought. The lab shows that a still smaller quantity gets a higher price and "
             "can bring a smaller total excess. Smith's sentence is about what a "
             "monopoly's price is, not about how it picks a quantity."),
            ("Treating every price above the natural price as a monopoly",
             "Smith lists three causes of different lengths: a secret, a natural scarcity "
             "and a legal privilege. The dyer has no privilege; the vineyard has no "
             "seller's design. Each keeps the market under-supplied, for different "
             "reasons."),
            ("Expecting the same force below the natural price",
             "The market price can stay above the natural price for centuries, and "
             "can only briefly stay below it, because those who are paid less withdraw "
             "land, labour or stock. Smith makes an exception only for a policy as "
             "violent as caste."),
        ],
        "standard": (
            "Finish when you can find a monopolist's price and its excess over the natural price.",
            "Given the natural price and a buyers' schedule, compute the price and the "
            "excess over the natural price for several quantities, and say which "
            "quantity gives the largest excess on that schedule."
        ),
        "note": (
            "The schedule is written for the lesson, and the idea that the natural "
            "price is the monopolist's cost at every quantity is the lab's, not Smith's. The "
            "lab cannot say whether a given price above the natural price is a monopoly, a "
            "reward for a secret or a scarcity; it does not know why the market is "
            "under-supplied. Cournot's quantity rule is a later one, and Smith "
            "stated none."
        ),
    },
]
