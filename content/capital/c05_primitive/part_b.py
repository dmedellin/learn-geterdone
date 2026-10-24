"""So-Called Primitive Accumulation, lessons 5-8 -- Volume I, Chapters 30 to 33.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals are left out, a drop capital is printed as an
ordinary capital, and the translator's double quotation marks inside a
quotation are printed as single curly quotes. Nothing else is changed. The
Kerr text prints "&c." as "8c." and "E. G." as "E.g."; no quotation here
crosses either misprint.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Kerr vol. 1, l. 5418 (means of nourishment set free); l. 5420 (the
    # flax's new social soul; manufactures réunies); l. 5424 (the home market).
    {
        "slug": "the-home-market",
        "title": "The Home Market for Industrial Capital",
        "module": "Chapter 30 · Creation of the Home Market for Industrial Capital",
        "one_line": "The same separation that made wage-labourers out of peasants turned what they had made for themselves into commodities, and so made a home market for industry.",
        "summary": (
            "Chapter 30 follows the agricultural revolution into industry: the evicted "
            "peasants' food becomes variable capital, their flax becomes constant capital, "
            "and the goods their households used to make become things to buy. Compute the "
            "market created when households that supplied themselves must buy their "
            "subsistence, with the same use-values consumed before and after."
        ),
        "key": [
            "market = households × (needs − self-made)",
            "self-supplied households: no market",
            "wage-earners buy their whole subsistence",
            "the market is the wage bill, spent",
            "same use-values, newly commodities",
        ],
        "key_label": "Chapter 30 in five lines",
        "concepts_intro": (
            "Marx finds three things set free by the expropriation, beside the people "
            "themselves."
        ),
        "concepts": [
            ("Subsistence as variable capital",
             "The land yielded as much or more after the clearing. The food the evicted "
             "peasants used to grow for themselves is now sold, and they must buy back its "
             "value with wages: it has become an element of variable capital."),
            ("Materials as constant capital",
             "Flax that a peasant family grew and spun at home becomes the raw material of a "
             "spinning-mill. &ldquo;Not a fibre of it is changed&rdquo;, but it is now part "
             "of a manufacturer's constant capital."),
            ("The home market",
             "Yarn, linen and coarse woollens that households made for their own use become "
             "manufactured goods they must buy. The destruction of rural domestic industry "
             "creates the internal market capital requires."),
        ],
        "read_title": "Means of nourishment, set free",
        "read_intro": (
            "Marx's phrase &ldquo;set free&rdquo; carries the chapter, and he applies it to "
            "the people and their food in the same sentence."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 30.</strong> &ldquo;With the setting free of a "
                  "part of the agricultural population, therefore, their former means of "
                  "nourishment were also set free. They were now transformed into material "
                  "elements of variable capital. The peasant, expropriated and cast adrift, "
                  "must buy their value in the form of wages, from his new master, the "
                  "industrial capitalist.&rdquo;"),
            ("p", "The phrase &ldquo;set free&rdquo; is ironic, and Marx also means it literally. The cleared land, "
                  "Marx says, brought forth as much produce as before or more, because of "
                  "better methods, larger farms and labourers worked harder. So the food the "
                  "peasants used to grow still exists. What has changed is that it no longer "
                  "goes to the people who grew it. It is sold, and they must earn the money to "
                  "buy it. In Marx's terms the food has become variable capital: the "
                  "capitalist advances wages, and the wages buy back the food."),
            ("p", "The raw materials go the same way. Marx imagines the Westphalian peasants "
                  "of Frederick II's time, who all spun flax, driven from their land, while "
                  "great flax-spinning and weaving establishments arise and employ them. "
                  "&ldquo;The flax looks exactly as before. Not a fibre of it is changed, but a "
                  "new social soul has popped into its body.&rdquo; It is now constant capital, "
                  "and the extra labour spun into it, which once meant extra income for many "
                  "peasant families, now means profit for a few capitalists."),
            ("p", "Marx adds a piece of popular wisdom. In Mirabeau's France the great "
                  "workshops were still called &ldquo;manufactures réunies, workshops thrown "
                  "into one&rdquo;, as fields were thrown into one, and Mirabeau thought the "
                  "scattered workshops of independent producers the better source of national "
                  "prosperity. You do not see, looking at a large factory, the many small "
                  "centres of production it was built from; the name remembered it."),
            ("p", "Then the market:"),
            ("p", "<strong>Volume I, Chapter 30.</strong> &ldquo;Formerly, the peasant family "
                  "produced the means of subsistence and the raw materials, which they "
                  "themselves, for the most part, consumed. These raw materials and means of "
                  "subsistence have now become commodities; the large farmer sells them, he "
                  "finds his market in manufactures.&rdquo;"),
            ("p", "The lab makes this a sum, with illustrative figures. A household's "
                  "subsistence is worth 1s 6d a day: a shilling of food, and 3d a day each for "
                  "cloth and for fuel and candles, each bought every twelve days for 3s. "
                  "A hundred households that grow, spin and gather all of it themselves buy "
                  "nothing: the market is 0s, in the before preset. Separate the same hundred households from their "
                  "land, and each must buy the whole 1s 6d: a market of 150s a day, in the after "
                  "preset. Nobody eats "
                  "more or dresses better. The same use-values are consumed; they have become "
                  "commodities."),
            ("def", ("Home market",
                     "The internal market for the products of industrial capital. On Marx's "
                     "account it is created when households stop producing their own "
                     "subsistence and materials and must buy them, and on the lab's model it "
                     "equals the households times the part of their subsistence they no "
                     "longer make.")),
            ("p", "Read the 150s from the other side and it is the same number. If each "
                  "household supplies one wage-earner and the wage covers the value of its "
                  "subsistence, the wage bill is a hundred wages of 1s 6d, 150s a day, and it is spent on "
                  "exactly those goods. The market created and the variable capital that now "
                  "circulates are one sum seen from two sides. Leave each household its "
                  "cottage acres, as the old laws tried to, so that it still grows its own "
                  "food, and the market is 50s, the cottage preset: only the cloth and fuel are bought."),
            ("p", "The strongest rival account starts from the same households. Adam Smith "
                  "made the division of labour depend on the extent of the market, with "
                  "households buying what specialised producers make more cheaply than they "
                  "could. Jan de Vries has argued that "
                  "in the seventeenth and eighteenth centuries households chose to work more "
                  "for the market and to buy what they had made at home, because they wanted "
                  "new goods: an industrious revolution, in which the home market grew by "
                  "choice and with rising consumption. Marx's account has the change forced and "
                  "consumption flat. The lab holds consumption flat by construction, so it "
                  "shows Marx's mechanism; it cannot show that the change was forced."),
            ("p", "Marx himself says the process was slow and incomplete. Manufacture destroyed "
                  "rural domestic industry in some branches and called it up again in others. "
                  "That is one reason, though not, he says, the chief one, why the student of "
                  "English history keeps finding the peasantry complained of as vanishing and "
                  "then turning up again; the chief is that England swung between corn and "
                  "cattle, and peasant cultivation with it. Only modern industry, "
                  "with machinery, completes the separation of agriculture from domestic "
                  "spinning and weaving and conquers the whole home market for capital."),
            ("p", "That accounts for the farmer and for the market. The next lesson, “Genesis "
                  "of the Industrial Capitalist”, asks where the industrial capitalist's "
                  "capital came from, and finds it in the colonies, the national debt, taxation "
                  "and protection."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "market",
            "money_unit": "s",
            "preset": "before",
            "presets": [
                {"id": "before", "label": "100 households that make all their own subsistence",
                 "households": 100,
                 "subsistence": [{"item": "food", "hours": 1, "every_days": 1},
                                 {"item": "yarn and linen", "hours": 3, "every_days": 12},
                                 {"item": "fuel and candles", "hours": 3, "every_days": 12}],
                 "self_supplied_value": "3/2",
                 "expect": {"ciLpValue": "1s 6d", "ciMarket": "0s"}},
                {"id": "after", "label": "The same 100 households as wage-earners",
                 "households": 100,
                 "subsistence": [{"item": "food", "hours": 1, "every_days": 1},
                                 {"item": "yarn and linen", "hours": 3, "every_days": 12},
                                 {"item": "fuel and candles", "hours": 3, "every_days": 12}],
                 "self_supplied_value": 0,
                 "expect": {"ciLpValue": "1s 6d", "ciMarket": "150s"}},
                {"id": "cottage", "label": "Wage-earners who still grow their food on cottage acres",
                 "households": 100,
                 "subsistence": [{"item": "food", "hours": 1, "every_days": 1},
                                 {"item": "yarn and linen", "hours": 3, "every_days": 12},
                                 {"item": "fuel and candles", "hours": 3, "every_days": 12}],
                 "self_supplied_value": 1,
                 "expect": {"ciLpValue": "1s 6d", "ciMarket": "50s"}},
            ],
            "panel_title": "A market made by separation",
            "panel_intro": (
                "Values are in shillings and illustrative. Each item's value is spread over "
                "the days it lasts, giving a household's subsistence per day in the first "
                "tile, which is the same in every preset. The second tile is what the "
                "households must buy: their number times the part of that subsistence they "
                "no longer make."
            ),
        }),
        "steps_title": "Measuring a home market",
        "steps_intro": "Four steps, from what a household needs to what it must buy.",
        "steps": [
            ("Value a day's subsistence",
             "For each item divide its value by the days it lasts, and add: food 1s a day, "
             "cloth and fuel 3s every 12 days each, make 1s 6d."),
            ("Subtract what the household still makes",
             "Bought per household = subsistence per day − the part it still produces for "
             "itself."),
            ("Multiply by the households",
             "Market created per day = households × the part bought."),
            ("Read it as a wage bill",
             "If each household supplies one wage-earner paid the value of its "
             "subsistence, the wage bill equals the market: the variable capital that "
             "circulates comes back as purchases of the same goods."),
        ],
        "worked": {
            "title": "A hundred households, before and after",
            "intro": [
                "A hundred households each need 1s 6d of subsistence a day. You want the "
                "market they make when they produce all of it themselves, when they produce "
                "none of it, and when they still grow their food.",
            ],
            "lines": [
                "subsistence:  1s + 3s/12 + 3s/12 = 1s 6d a day",
                "self-supplied:  100 × (1s 6d − 1s 6d) = 0s",
                "wage-earners:  100 × 1s 6d = 150s a day",
                "cottage food kept:  100 × (1s 6d − 1s) = 50s",
            ],
            "after": [
                "From nothing to 150s a day, and no household consumes a penny more. The "
                "figures are illustrative; the change of form is Marx's.",
            ],
        },
        "quiz_title": "A market from separation",
        "quiz": [
            {"q": "Two hundred households each need 2s of subsistence a day and still make "
                  "6d of it themselves. What market do they create a day?",
             "a": ["300s", "400s", "100s", "1s 6d"],
             "c": 0,
             "why": "Each buys 2s − 6d = 1s 6d, and 200 × 1s 6d = 300s. Four hundred "
                    "shillings ignores what they still make; 100s counts only what they make; "
                    "1s 6d is one household's purchase."},
            {"q": "A household's subsistence is 1s of food a day and 6s of clothing every 24 "
                  "days. What is its subsistence per day?",
             "a": ["1s 3d", "7s", "1s 6d", "1/4 s"],
             "c": 0,
             "why": "Clothing is 6s / 24 = 3d a day, so the total is 1s 3d. Seven shillings "
                    "adds the clothing's full value to one day; 1s 6d divides by 12 instead of "
                    "24; 1/4 s is the clothing alone."},
            {"q": "In the lab, households go from making all their subsistence to buying all "
                  "of it. What happens to the subsistence they consume each day?",
             "a": ["It rises, because they are now richer",
                   "It is unchanged; only its form, as commodities, changes",
                   "It falls, because they must pay a profit on it",
                   "It doubles, because they now pay wages and prices"],
             "c": 1,
             "why": "The first tile, subsistence per household, is 1s 6d in every preset. The "
                    "market appears because the same use-values are now bought, not because "
                    "more is consumed. Nothing in the lab charges a profit on top of value or "
                    "counts anything twice."},
            {"q": "What does Marx mean by saying the flax has a &ldquo;new social soul&rdquo;?",
             "a": ["Its fibre has been improved by new methods",
                   "It is now spun by machines rather than by hand",
                   "It is the same flax, but now the constant capital of a manufacturer",
                   "It has become more valuable because more labour is spent on it"],
             "c": 2,
             "why": "&ldquo;Not a fibre of it is changed&rdquo;, Marx stresses: what changes "
                    "is the social relation, as the flax becomes part of a manufacturer's "
                    "constant capital. In his example it is spun in large establishments, not "
                    "yet by machines, and nothing is said of more labour."},
        ],
        "mistakes": [
            ("Thinking the home market grew because people became richer",
             "In the lab each household's subsistence is 1s 6d a day in every preset, so "
             "consumption never rises; yet the market goes from 0s to 150s a day when the "
             "households lose their land. What grew is the part of subsistence that is "
             "bought. De Vries's industrious revolution, in which households chose the "
             "market and consumed more, is a real rival account; the lab shows how a market "
             "can grow without it."),
            ("Thinking the market and the wage bill are two separate sums",
             "With one wage-earner per household paid the value of its subsistence, the "
             "wages paid out, 150s, are the purchases made. Marx's point is that variable "
             "capital, once advanced, is the home market."),
            ("Thinking the land produced less after the clearing",
             "Marx says the soil brought forth &ldquo;as much or more produce&rdquo;. The food "
             "was not destroyed but redirected: it is sold to the people who used to grow "
             "it."),
        ],
        "standard": (
            "Finish when you can compute the market a separation creates.",
            "Given the households, each item of their subsistence with its value and the "
            "days it lasts, and the part they still make themselves, compute the "
            "subsistence per household per day and the market created per day, and state "
            "it as the wage bill that circulates."
        ),
        "note": (
            "The figures are illustrative, and the lab holds each household's consumption "
            "fixed, which is Marx's assumption and the point de Vries disputes. It counts a "
            "market in value and cannot say whether the change was forced, as Marx argues, "
            "or chosen, as the industrious-revolution account argues."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 1, l. 5446 to l. 5448 (the systematical combination; force the
    # midwife); l. 5436 (the snail's-pace);
    # l. 5450 (Sweet commerce); l. 5465 (the national debt; the credo of
    # capital); l. 5467 (barren money breeds); l. 5470 (the Bank at 8%);
    # l. 5476 (over-taxation); l. 5478 (Cobbett, Doubleday); l. 5481
    # (manufacturing manufacturers); l. 5495 (veiled slavery); l. 5499
    # (blood and dirt).
    {
        "slug": "the-industrial-capitalist",
        "title": "Genesis of the Industrial Capitalist",
        "module": "Chapter 31 · Genesis of the Industrial Capitalist",
        "one_line": "The industrial capitalist was made quickly, by the colonies, the national debt, taxation and protection, all of them using the power of the state.",
        "summary": (
            "Chapter 31 names four levers that, combined in England by the end of the "
            "seventeenth century, turned merchant's and usurer's money into industrial "
            "capital: the colonial system, the national debt, modern taxation and "
            "protection. Compute one of them: the price of a claim on the state from its "
            "yearly interest and the rate of interest, and what happens to that price when "
            "the rate falls and nothing else does."
        ),
        "key": [
            "levers: colonies, debt, taxes, protection",
            "price of a claim = yearly income / rate",
            "£3 a year at 3%: a claim priced at £100",
            "the rate falls to 2%: the claim is £150",
            "the interest is paid out of taxes",
        ],
        "key_label": "Chapter 31 in five lines",
        "concepts_intro": (
            "The farmer rose slowly. Chapter 31 is about a capitalist who did not, and "
            "about the state's part in making him."
        ),
        "concepts": [
            ("Merchant's and usurer's capital",
             "The middle ages handed down two forms of money capital, from trade and from "
             "lending. Feudal law in the country and the guilds in the towns kept them from "
             "becoming industrial capital until those fetters dissolved."),
            ("The four levers",
             "The colonial system, the national debt, the modern mode of taxation and the "
             "protectionist system. Some rest on brute force, and all, Marx says, use the "
             "power of the state to hasten the passage from the feudal to the capitalist "
             "mode of production."),
            ("A debt as capital",
             "A state's debt turns money lent into negotiable bonds that function in their "
             "owners' hands &ldquo;just as so much hard cash would&rdquo;. The yearly interest, "
             "paid from taxes, is priced as a capital, though nothing was built with it."),
        ],
        "read_title": "Force as an economic power",
        "read_intro": (
            "The passage names the four levers and the one thing they share. Its last two "
            "sentences are among the most quoted in the book."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 31.</strong> &ldquo;In England at the end of the "
                  "17th century, they arrive at a systematical combination, embracing the "
                  "colonies, the national debt, the modern mode of taxation, and the "
                  "protectionist system. These methods depend in part on brute force, e.g., the "
                  "colonial system. But they all employ the power of the State, the concentrated "
                  "and organised force of society, to hasten, hothouse fashion, the process of "
                  "transformation of the feudal mode of production into the capitalist mode, "
                  "and to shorten the transition. Force is the midwife of every old society "
                  "pregnant with a new one. It is itself an economic power.&rdquo;"),
            ("p", "Marx grants the slow road first. Many small guild-masters, artisans and even "
                  "wage-labourers did turn themselves into small capitalists by gradually "
                  "extending the exploitation of wage-labour. But that &ldquo;snail's-pace&rdquo; "
                  "could not meet the world market opened by the discoveries of the late "
                  "fifteenth century. Money capital existed, from usury and trade; feudal law "
                  "and the guilds kept it out of industry, and when they dissolved, the new "
                  "manufactures settled in sea-ports and in places beyond the old towns' "
                  "control."),
            ("p", "The colonial system comes first, and the chapter gives it the most space: "
                  "the treasure of the Americas and the enslavement and destruction of their "
                  "peoples, the plunder of the East Indies, and the trade in captured Africans. "
                  "Marx's catalogue is specific. The Dutch stole men in Celebes to work as slaves "
                  "in Java; &ldquo;Sweet commerce!&rdquo;, he writes after the depopulation of "
                  "Banjuwangi. The East India Company and its servants took £6,000,000 from "
                  "Indians as gifts between 1757 and 1766. New England's assemblies paid bounties "
                  "for scalps. Liverpool's slave-ships rose from 15 in 1730 to 132 in 1792. "
                  "&ldquo;In fact, the veiled slavery of the wage-earners in Europe needed, for its "
                  "pedestal, slavery pure and simple in the new world.&rdquo;"),
            ("p", "How much colonial and slave-trade profit mattered to British industry is one "
                  "of the long arguments of economic history. Eric Williams argued in 1944, in "
                  "<em>Capitalism and Slavery</em>, that the profits of the slave trade and the "
                  "plantations helped finance the Industrial Revolution. Stanley Engerman and "
                  "Patrick O'Brien answered, in separate studies of 1972 and 1982, with estimates in which those profits were a small "
                  "share of British investment, too small to be decisive. Joseph Inikori "
                  "replied in 2002 that the Atlantic trade's demand for British manufactures, "
                  "not its profits alone, was central. None of these sides denies the "
                  "brutality Marx records; they dispute its weight in the accounts."),
            ("p", "The second lever is the national debt, and here Marx is at his most "
                  "sardonic:"),
            ("p", "<strong>Volume I, Chapter 31.</strong> &ldquo;The only part of the so-called "
                  "national wealth that actually enters into the collective possessions of "
                  "modern peoples is&mdash;their national debt.&rdquo;"),
            ("p", "His account of how the debt works is specific. It &ldquo;endows barren money "
                  "with the power of breeding&rdquo;: the state's creditors give nothing away, "
                  "since the sum lent becomes negotiable bonds that go on working in their hands "
                  "like cash. Around the debt grew joint-stock companies, dealing in securities, "
                  "and the great banks. The Bank of England, founded in 1694, &ldquo;began with "
                  "lending its money to the Government at 8%&rdquo;, and then lent its own notes "
                  "back to the public. The bank-1694 preset prices its £8 a year on each £100 at "
                  "that 8%: £100. &ldquo;Public credit becomes the credo of capital.&rdquo;"),
            ("def", ("Capitalise",
                     "To price a yearly payment as the sum that, lent at the current rate of "
                     "interest, would yield it: price = yearly income / rate of interest. A "
                     "claim to £3 a year is priced at £100 when the rate is 3%.")),
            ("p", "The lab computes that price. A government bond paying £3 a year, at a rate "
                  "of interest of 3%, is priced at £100, which is what the consols, the "
                  "consolidated three per cent stock that Britain issued from 1751, were "
                  "reckoned in. The £100 the creditor lent may have been spent on a war; nothing "
                  "need have been built with it. Yet the creditor holds £100 of capital in his "
                  "books and can sell it; that is the consols preset. Let the rate of interest fall to 2%, the cheap-money preset, and the same £3 a "
                  "year is priced at £150. The creditor is £50 richer, and nothing in the country "
                  "has changed but a rate."),
            ("p", "Interest needs revenue, so taxation is the debt's necessary complement. "
                  "Taxes fell above all on necessaries, raising their price, and each new loan "
                  "meant new taxes: &ldquo;Over-taxation is not an incident, but rather a "
                  "principle.&rdquo; Protection, the fourth lever, was &ldquo;an artificial means "
                  "of manufacturing manufacturers&rdquo;, and in dependent countries it rooted out "
                  "industry, as England did with the Irish woollen manufacture. Marx also marks "
                  "his limit: Cobbett, Doubleday and others had made the debt the fundamental "
                  "cause of the people's misery, and that, he says, was incorrect."),
            ("p", "The same history has a reading opposite to Marx's. Douglass North and Barry "
                  "Weingast argued in 1989 that after 1688 Parliament's control of the purse made "
                  "the English state's promises to pay believable, so it could borrow cheaply "
                  "and safely; on their account public credit was a foundation of secure "
                  "property and of growth, not a lever of expropriation. P. G. M. Dickson had "
                  "already called the change a financial revolution. Marx and they describe "
                  "the same institutions; they disagree on what they were for and whom they "
                  "served."),
            ("p", "Marx closes the chapter by finishing a sentence of Augier's: if money comes "
                  "into the world with a blood-stain on one cheek, &ldquo;capital comes "
                  "dripping from head to foot, from every pore, with blood and dirt&rdquo;. The "
                  "next lesson, “Historical Tendency of Capitalist Accumulation”, asks what the "
                  "whole of this history comes to, and where Marx thinks it leads."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "capitalise",
            "money_unit": "£",
            "preset": "consols",
            "presets": [
                {"id": "consols", "label": "A bond paying £3 a year, at 3%",
                 "income": 3, "interest_rate": "3/100",
                 "expect": {"inPrice": "£100"}},
                {"id": "cheap-money", "label": "The same £3 a year when the rate falls to 2%",
                 "income": 3, "interest_rate": "2/100",
                 "expect": {"inPrice": "£150"}},
                {"id": "bank-1694", "label": "Marx's rate: the Bank of England lends at 8% in 1694, £8 a year on each £100",
                 "income": 8, "interest_rate": "8/100",
                 "expect": {"inPrice": "£100"}},
            ],
            "panel_title": "Pricing a claim on the state",
            "panel_intro": (
                "A yearly payment and a rate of interest go in; the tile is the sum that, "
                "lent at that rate, would pay it. Compare the first two presets: the claim is "
                "the same £3 a year, and only the rate changed."
            ),
        }),
        "steps_title": "Capitalising a yearly payment",
        "steps_intro": "Four steps, from a bond's interest to the capital it is reckoned as.",
        "steps": [
            ("Take the yearly payment",
             "The interest the state pays each year on the claim, in money."),
            ("Take the rate of interest",
             "The rate at which money is currently lent, as a fraction: 3% is 3/100."),
            ("Divide",
             "Price of the claim = yearly payment / rate of interest. £3 / (3/100) = £100."),
            ("Trace a change to its source",
             "If the rate falls, the price rises with no change in the payment or in "
             "anything produced. Name where the payment comes from: taxes."),
        ],
        "worked": {
            "title": "Consols at 3% and at 2%",
            "intro": [
                "A creditor holds a claim on the state to £3 a year, paid out of taxes. You "
                "want its price at a rate of interest of 3%, and at 2%.",
            ],
            "lines": [
                "at 3%:  £3 / (3/100) = £100",
                "at 2%:  £3 / (2/100) = £150",
                "Bank of England, 1694:  £8 / (8/100) = £100",
            ],
            "after": [
                "Fifty pounds of new capital in the creditor's books, from a change in a rate. "
                "The 8% is Marx's figure; the £3 and the rates are illustrative.",
            ],
        },
        "quiz_title": "A debt priced as capital",
        "quiz": [
            {"q": "A claim on the state pays £5 a year, and the rate of interest is 4%. What "
                  "is the claim priced at?",
             "a": ["£125", "£20", "£500", "£105"],
             "c": 0,
             "why": "£5 / (4/100) = £125. Twenty pounds multiplies by 4 instead of dividing by "
                    "4/100; £500 divides by 1/100; £105 adds the interest to £100."},
            {"q": "The rate of interest falls from 4% to 2% and the claim still pays £5 a "
                  "year. What happens to its price?",
             "a": ["It doubles, to £250", "It halves, to £62 10s", "It is unchanged",
                   "It rises by £5"],
             "c": 0,
             "why": "The price is the payment over the rate, so halving the rate doubles it: "
                    "£5 / (2/100) = £250. It would halve if the rate doubled; it is unchanged "
                    "only if the rate is."},
            {"q": "Which four levers does Marx name as combined in England at the end of the "
                  "seventeenth century?",
             "a": ["The colonies, the national debt, modern taxation and protection",
                   "Enclosure, the poor law, the factory and the machine",
                   "Usury, trade, the guilds and the Church",
                   "Gold, silver, credit and paper money"],
             "c": 0,
             "why": "Marx's list is &ldquo;the colonies, the national debt, the modern mode of "
                    "taxation, and the protectionist system&rdquo;. Enclosure belongs to Chapter "
                    "27, and usury and trade are the older forms of capital the levers "
                    "released; the Church and the guilds were obstacles."},
            {"q": "On Marx's account, what does a state creditor give up by lending?",
             "a": ["Nothing, since the loan becomes bonds that work in his hands like cash",
                   "His capital, which the state spends and never repays",
                   "The right to sell his claim",
                   "The interest, which is paid to the taxpayers instead"],
             "c": 0,
             "why": "Marx says the creditors &ldquo;actually give nothing away&rdquo;, because "
                    "the sum lent is turned into negotiable bonds that function &ldquo;just as "
                    "so much hard cash would&rdquo;. They can sell the claim, and the interest "
                    "is paid to them out of taxes."},
        ],
        "mistakes": [
            ("Thinking the national debt is part of the nation's wealth",
             "This is Marx's own target, and he answers it with sarcasm: the only part of "
             "the national wealth the people collectively own is their debt. The tile makes "
             "the point in figures: the same £3 a year is a £100 claim at 3% and a £150 claim "
             "at 2%, though nothing was built and nothing changed but the rate. For the "
             "nation as a whole the creditor's asset is the taxpayers' liability. Whether "
             "borrowing also financed growth, as North and Weingast argue, is a separate "
             "question."),
            ("Reading the chapter as saying the debt caused capitalism",
             "Marx names the debt one lever of four and calls Cobbett and Doubleday wrong to "
             "make it the fundamental cause of the people's misery. The fundamental process, "
             "on his account, remains the separation of the producers from the means of "
             "production."),
            ("Reading the chapter as only about consols",
             "Most of the chapter is the colonial system: plunder, enslavement and the slave "
             "trade. The lab computes the debt because it is the lever with a formula; the "
             "others are matters of evidence, argued between Williams, Engerman, O'Brien and "
             "Inikori."),
        ],
        "standard": (
            "Finish when you can name the four levers and price a claim on the state.",
            "Name the four levers Marx says were combined in England by the end of the "
            "seventeenth century, and, given a yearly payment and a rate of interest, "
            "compute the price of the claim and its price again after a change in the rate."
        ),
        "note": (
            "To capitalise is to call a yearly £3 a £100 claim because £100 lent at 3% pays "
            "£3. Why that rate exists, and what sets it, is Volume III's question, taken up "
            "in Merchant's Capital and Interest; here the rate is simply given. The lab "
            "prices one lever of four, and the weight of the colonial system in Britain's "
            "industrialisation is an argument about evidence that it cannot enter."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 1, l. 5513 (the knell); l. 5507 (universal mediocrity);
    # l. 5511 (one capitalist always kills many); l. 5515 (the negation of
    # negation); l. 5517 (the two expropriations compared).
    {
        "slug": "the-historical-tendency",
        "title": "Historical Tendency of Capitalist Accumulation",
        "module": "Chapter 32 · Historical Tendency of Capitalist Accumulation",
        "one_line": "Marx's summary of Part Eight: the expropriation of the many by the few is followed, by the centralisation of capital, by the expropriation of the few.",
        "summary": (
            "In four pages Marx states where the history of the last six chapters is going: "
            "petty private property based on one's own labour is expropriated by capitalist "
            "property, and capitalist property, centralised into fewer hands, prepares its "
            "own expropriation. Compute concentration, every capital growing, against "
            "centralisation, capitals merging, and the share the largest holds after "
            "several periods of each."
        ),
        "key": [
            "concentration: every capital grows",
            "centralisation: capitals merge",
            "largest's share = largest / total",
            "one capitalist always kills many",
            "the expropriators are expropriated",
        ],
        "key_label": "Chapter 32 in five lines",
        "concepts_intro": (
            "The chapter tells two expropriations and puts them in sequence."
        ),
        "concepts": [
            ("Property from one's own labour",
             "The peasant who owns his land and the artisan his tools, the basis of petty "
             "industry. It excludes co-operation and the large-scale use of science, and "
             "Marx says it is annihilated as the conditions for capital develop."),
            ("Centralisation",
             "The merging of existing capitals into fewer hands: &ldquo;One capitalist "
             "always kills many.&rdquo; It differs from concentration, the growth of each "
             "capital by its own accumulation, defined in Chapter 25."),
            ("The negation of the negation",
             "Capitalist property negated property based on one's own labour; Marx argues "
             "that capitalist production begets its own negation, which establishes not "
             "private property for the producer but individual property based on "
             "co-operation and common possession of the means of production."),
        ],
        "read_title": "The knell",
        "read_intro": (
            "One of the best-known passages in Volume I comes at the end of a long sentence "
            "about centralisation. Its argument is about the merging of capitals."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 32.</strong> &ldquo;Centralisation of the means of "
                  "production and socialisation of labour at last reach a point where they "
                  "become incompatible with their capitalist integument. This integument is "
                  "burst asunder. The knell of capitalist private property sounds. The "
                  "expropriators are expropriated.&rdquo;"),
            ("p", "The chapter begins by asking what primitive accumulation comes to. Where "
                  "it is not simply the turning of slaves and serfs into wage-labourers, it is "
                  "the expropriation of the immediate producers, the dissolution of private "
                  "property based on the owner's own labour. Marx gives that property its due. "
                  "It is the basis of petty industry and of &ldquo;the free individuality of the "
                  "labourer himself&rdquo;, the peasant with his land and the artisan with the "
                  "tool he handles &ldquo;as a virtuoso&rdquo;. But it scatters the means of "
                  "production and excludes co-operation; to perpetuate it would be, quoting "
                  "Pecqueur, &ldquo;to decree universal mediocrity&rdquo;."),
            ("p", "So it is annihilated, and that annihilation is the history of the last five "
                  "lessons: the &ldquo;pigmy property of the many&rdquo; turned into &ldquo;the "
                  "huge property of the few&rdquo;. Then the movement continues with a new "
                  "object. &ldquo;That which is now to be expropriated is no longer the labourer "
                  "working for himself, but the capitalist exploiting many labourers.&rdquo; The "
                  "means is the action of capitalist production's own laws, the centralisation "
                  "of capital. &ldquo;One capitalist always kills many.&rdquo;"),
            ("p", "Two words from “The General Law of Capitalist Accumulation” matter here, "
                  "and they are easy to run together. Concentration is the growth of each "
                  "capital by its own accumulation. Centralisation is the merging of capitals "
                  "already formed, by competition or credit, so that one grows because others "
                  "disappear. Marx's sentence here names centralisation, and the lab shows why "
                  "the difference matters."),
            ("def", ("Centralisation",
                     "The combination of capitals already formed into fewer and larger ones. "
                     "It changes how the social capital is distributed without adding to it, "
                     "where concentration adds to each capital by accumulation.")),
            ("p", "Start with ten capitals of £100 each, the ten preset, where nothing moves and "
                  "the largest holds 1/10. In the grow preset every one grows by a tenth each "
                  "period for five periods: each becomes a little over £161, the total "
                  "rises from £1,000 to about £1,610, and the largest still holds 1/10 of it, "
                  "one of ten. That is concentration. In the merge preset nothing grows, but in each period "
                  "the largest capital absorbs the smallest. After five periods five capitals "
                  "are left, the total is still £1,000, and the largest holds £600 of it, 3/5. "
                  "That is centralisation, and it is the movement Marx's sentence is about."),
            ("p", "Around the shrinking number of magnates Marx sees two things grow: "
                  "&ldquo;the mass of misery, oppression, slavery, degradation, "
                  "exploitation&rdquo;, and the revolt of a working-class &ldquo;disciplined, "
                  "united, organised by the very mechanism of the process of capitalist "
                  "production itself&rdquo;. Then the knell. Capitalist property, he says, was "
                  "the first negation of individual property founded on one's own labour, and "
                  "&ldquo;capitalist production begets, with the inexorability of a law of "
                  "Nature, its own negation. It is the negation of negation.&rdquo;"),
            ("p", "What it establishes, Marx says, is not private property for the producer "
                  "again but &ldquo;individual property based on the acquisitions of the "
                  "capitalist era: i.e., on co-operation and the possession in common of the "
                  "land and of the means of production&rdquo;. And he compares the two "
                  "expropriations: the first was &ldquo;incomparably more protracted, violent, "
                  "and difficult&rdquo; than the second will be, because &ldquo;we had the "
                  "expropriation of the mass of the people by a few usurpers; in the latter, we "
                  "have the expropriation of a few usurpers by the mass of the people&rdquo;."),
            ("p", "Few chapters of the volume have drawn more argument. Eugen "
                  "Dühring attacked the negation of the negation as Hegelian word-play doing "
                  "the work of proof, and Engels replied in <em>Anti-Dühring</em> in 1878 that "
                  "Marx first shows the process historically and only afterwards names its "
                  "form. Eduard Bernstein argued in 1899 that the number of property-owners was "
                  "growing, not shrinking, and that small and middling firms were persisting, "
                  "so the polarisation was not happening as foretold. Karl Popper later "
                  "classed such laws of historical development as prophecy rather than "
                  "science. On the other side, Paul Baran and Paul Sweezy argued in 1966 that "
                  "the giant corporation had become the typical unit of capital, which is the "
                  "centralisation Marx foresaw, and defenders of the chapter point to the spread "
                  "of wage-labour across the world since he wrote. The lab computes a mechanism "
                  "and none of the record."),
            ("p", "There is one more chapter, and it seems to go backwards. The next lesson, "
                  "“The Modern Theory of Colonisation”, travels to the colonies, where, Marx "
                  "says, the secret of the old world was blurted out."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "centralise",
            "money_unit": "£",
            "preset": "ten",
            "presets": [
                {"id": "ten", "label": "Ten equal capitals of £100; no growth, no merging",
                 "capitals": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
                 "merge_rule": "none", "growth": 0,
                 "expect": {"acTopShare": "1/10 = 10%", "acCount": "10"}},
                {"id": "grow", "label": "Concentration: every capital grows by a tenth a period",
                 "capitals": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
                 "merge_rule": "none", "growth": "1/10",
                 "expect": {"acTopShare": "1/10 = 10%", "acCount": "10"}},
                {"id": "merge", "label": "Centralisation: the largest absorbs the smallest each period",
                 "capitals": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
                 "merge_rule": "largest-absorbs-smallest", "growth": 0,
                 "expect": {"acTopShare": "3/5 = 60%", "acCount": "5"}},
            ],
            "panel_title": "Concentration against centralisation",
            "panel_intro": (
                "The figures are illustrative. Each period every capital grows at the stated "
                "rate; then, under the merging rule, the largest absorbs the smallest. The "
                "tiles give the largest capital's share of the total and the number of "
                "capitals left after the periods chosen; the table shows the total each "
                "period."
            ),
        }),
        "steps_title": "Concentration or centralisation",
        "steps_intro": "Four steps for a set of capitals followed over several periods.",
        "steps": [
            ("Grow each capital",
             "Multiply every capital by 1 + the growth rate for each period. This is "
             "concentration; it raises the total."),
            ("Merge, if the rule says so",
             "After growth, the largest capital absorbs the smallest of the others, and the "
             "number of capitals falls by one. This is centralisation; it leaves the total "
             "as it was."),
            ("Compute the largest's share",
             "Share = largest capital / total of all capitals, after the last period."),
            ("Tell the two apart",
             "If the share and the count are unchanged while the total grows, the change was "
             "concentration. If the count falls and the share rises with no change in the "
             "total, it was centralisation."),
        ],
        "worked": {
            "title": "Ten capitals, five periods",
            "intro": [
                "Ten capitals of £100 each. You want the largest's share after five periods "
                "if all grow by a tenth each period, and if instead the largest absorbs the "
                "smallest each period.",
            ],
            "lines": [
                "growth:  10 × £161.051 = £1,610.51; share 1/10",
                "merging:  £200, £300, £400, £500, £600",
                "after five mergers:  5 capitals left",
                "share:  £600 / £1,000 = 3/5 = 60%",
            ],
            "after": [
                "Growth left the largest with a tenth; merging gave it three-fifths of a "
                "total that never grew. Both happen together in practice, which is why the "
                "lab lets you run them separately.",
            ],
        },
        "quiz_title": "Fewer and larger",
        "quiz": [
            {"q": "Eight equal capitals; each period the largest absorbs the smallest and "
                  "nothing grows. After three periods, what share does the largest hold?",
             "a": ["1/2", "3/8", "1/8", "4/5"],
             "c": 0,
             "why": "The largest absorbs one capital a period, so after three it is four of "
                    "the original eight: 4/8 = 1/2, with five capitals left. Three-eighths "
                    "counts only the absorbed ones; 1/8 is the starting share; 4/5 divides by "
                    "the capitals left."},
            {"q": "Every one of ten equal capitals doubles over a decade and none merges. What "
                  "happens to the largest's share?",
             "a": ["It stays 1/10", "It doubles to 1/5", "It halves to 1/20",
                   "It rises to 1/2"],
             "c": 0,
             "why": "Every capital and the total double together, so each still holds 1/10. "
                    "That is concentration without centralisation: everything grows and the "
                    "distribution does not change."},
            {"q": "In Chapter 32, what does Marx say is expropriated once the capitalist mode "
                  "of production stands on its own feet?",
             "a": ["The labourer working for himself",
                   "The capitalist exploiting many labourers",
                   "The landlord's rent",
                   "The state's lands"],
             "c": 1,
             "why": "&ldquo;That which is now to be expropriated is no longer the labourer "
                    "working for himself, but the capitalist exploiting many labourers.&rdquo; "
                    "The labourer working for himself was the object of the first "
                    "expropriation; rent and state lands belong to earlier chapters."},
            {"q": "What does Marx say the negation of the negation establishes?",
             "a": ["Private property for each producer, as before capitalism",
                   "Individual property based on co-operation and the possession in common of "
                   "the land and the means of production",
                   "State ownership of all property",
                   "The return of petty industry"],
             "c": 1,
             "why": "Marx says it &ldquo;does not re-establish private property for the "
                    "producer&rdquo; but gives individual property based on co-operation and "
                    "common possession. He says nothing here of state ownership, and petty "
                    "industry is what the first negation destroyed."},
        ],
        "mistakes": [
            ("Thinking concentration and centralisation are the same thing",
             "Both make capitals larger, but by different routes. In the grow preset every "
             "capital grows by a tenth a period, the total rises, and after five periods the "
             "largest still holds 1/10 of ten. In the merge preset nothing grows, yet five "
             "capitals are left and the largest holds 3/5. Marx's &ldquo;One capitalist "
             "always kills many&rdquo; is the second."),
            ("Reading the knell as a calculation the chapter performs",
             "The lab computes how merging changes shares. Marx's claim that centralisation "
             "and the socialisation of labour become incompatible with capitalist property is "
             "an argument about history, contested from Bernstein to Popper, and no tile "
             "computes it."),
            ("Thinking Marx dismisses the producer's own property as worthless",
             "He calls it the foundation of petty industry and of the labourer's free "
             "individuality. His claim is that it excludes co-operation and large-scale "
             "production, and so cannot last once those develop."),
        ],
        "standard": (
            "Finish when you can tell concentration from centralisation in figures.",
            "Given a set of capitals, a growth rate and a merging rule, compute the number "
            "of capitals left and the largest's share after several periods, and classify "
            "the change as concentration, centralisation or both."
        ),
        "note": (
            "The merging rule is mechanical, the largest absorbing the smallest, and the "
            "figures are illustrative; real centralisation goes by competition and credit "
            "in no fixed order. The lab shows what centralisation does to shares. Whether "
            "it leads where Marx says is one of the most argued questions in the book, and the "
            "record that would settle it is not computed here."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 1, l. 5529 and l. 5531 (capital a social relation; Mr. Peel);
    # l. 5525 (two kinds of private property); l. 5561 and l. 5563 (the
    # sufficient price); l. 5527 (Wakefield's merit); l. 5537 (capital
    # perished at Swan River); l. 5569 (the last sentence).
    {
        "slug": "the-modern-theory-of-colonisation",
        "title": "The Modern Theory of Colonisation",
        "module": "Chapter 33 · The Modern Theory of Colonisation",
        "one_line": "In the colonies, where land was free, a capitalist found that his money and machines employed no one, and Wakefield's remedy was to put a price on the land.",
        "summary": (
            "Volume I ends with Edward Gibbon Wakefield, who, on Marx's reading, discovered "
            "in the colonies that capital is not a thing but a relation between persons. Compute the "
            "workers left for hire to a colonist who brought £50,000 and 3,000 labourers "
            "when land is free, and the years of wage-labour Wakefield's land price "
            "imposes before a worker can leave."
        ),
        "key": [
            "capital: a social relation, not a thing",
            "free land: every worker can leave",
            "years to land = price / share saved",
            "Wakefield: a sufficient price for land",
            "the colony shows what home conceals",
        ],
        "key_label": "Chapter 33 in five lines",
        "concepts_intro": (
            "The last chapter of Volume I goes abroad to make a point about home."
        ),
        "concepts": [
            ("Two kinds of private property",
             "Political economy, Marx says, confuses property that rests on the producer's "
             "own labour with property that rests on employing the labour of others. In "
             "Europe the second has grown on the first's grave; in the colonies the two meet "
             "and fight."),
            ("Capital as a social relation",
             "Wakefield found that money, means of subsistence and machines do not make a "
             "man a capitalist without the wage-worker who must sell himself. Capital, in "
             "Marx's reading of him, is a relation between persons established through "
             "things."),
            ("Systematic colonisation",
             "Wakefield's remedy: the state sells colonial land at a price high enough that "
             "immigrants must work for wages for years before they can buy, and uses the "
             "proceeds to bring out more labourers."),
        ],
        "read_title": "Mr. Peel and his servants",
        "read_intro": (
            "Marx reports Wakefield's anecdote with relish, and the anecdote carries the "
            "whole chapter's argument."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 33.</strong> &ldquo;He discovered that capital is "
                  "not a thing, but a social relation between persons, established by the "
                  "instrumentality of things. Mr. Peel, he moans, took with him from England to "
                  "Swan River, West Australia, means of subsistence and of production to the "
                  "amount of £50,000. Mr. Peel had the foresight to bring with him, besides, "
                  "3000 persons of the working-class, men, women, and children. Once arrived at "
                  "his destination, &lsquo;Mr. Peel was left without a servant to make his bed "
                  "or fetch him water from the river.&rsquo;&rdquo;"),
            ("p", "Why end a book about capital in the colonies? Because, Marx says, political "
                  "economy &ldquo;confuses on principle two very different kinds of private "
                  "property&rdquo;: one resting on the producer's own labour, the other on the "
                  "employment of the labour of others. In Western Europe primitive "
                  "accumulation is more or less finished, and the economist can apply the "
                  "language of the first kind of property to the second. In the colonies he "
                  "cannot, because there the independent producer still exists in numbers, and "
                  "capital runs into him."),
            ("p", "Edward Gibbon Wakefield is the economist who said so. In the 1820s and 1830s "
                  "he wrote that the trouble with new colonies was not a lack of capital but a "
                  "lack of labourers for hire, and his ideas were put into practice in the "
                  "founding of South Australia in 1836 and in the New Zealand Company's "
                  "settlements. Marx gives him credit for discovering &ldquo;not anything new "
                  "about the Colonies&rdquo; but, in the colonies, the truth about the mother "
                  "country."),
            ("p", "Thomas Peel's party sailed for the Swan River in 1829 with money, tools, "
                  "seed and people. On arrival the people found land for the taking and went to "
                  "take it. &ldquo;Unhappy Mr. Peel who provided for everything except the export "
                  "of English modes of production to Swan River!&rdquo; That is Marx's joke, and "
                  "the lesson needs no other."),
            ("def", ("Capital (as a social relation)",
                     "On Marx's reading of Wakefield, means of production and subsistence are "
                     "capital only where they serve to employ and command workers who have no "
                     "means of their own. The same tools in the hands of an independent "
                     "settler are his means of production, not capital.")),
            ("p", "The lab computes Peel's position. A capital of £50,000 and 3,000 colonists "
                  "brought out as workers, the peel preset; land is free, so its price in years of wages is 0, "
                  "and every one of them can leave wage-labour at once. Workers for hire: 0. "
                  "The £50,000 is all still there, in tools and stores, and it employs no one. "
                  "Wakefield himself reported that at the Swan River a great mass of capital "
                  "&ldquo;has perished for want of labourers to use it&rdquo;."),
            ("p", "Wakefield's remedy was a price:"),
            ("p", "<strong>Volume I, Chapter 33.</strong> &ldquo;The price of the soil imposed "
                  "by the State must, of course, be a &lsquo;sufficient price&rsquo;&mdash;i.e., "
                  "so high &lsquo;as to prevent the labourers from becoming independent "
                  "landowners until others had followed to take their place.&rsquo;&rdquo;"),
            ("p", "In the wakefield preset the price is two years' wages, and a worker saves half his wage. He "
                  "needs 4 years of wage-labour to buy land, and for those 4 years the 3,000 "
                  "colonists remain for hire. The lab ships four periods; move the slider to "
                  "five and they are gone, and the price must bring others to take their place. "
                  "In the closed preset the worker can save nothing, so land at any price is out of "
                  "reach and the workers stay for hire indefinitely, which "
                  "is the condition of the old country. Marx calls the sufficient price "
                  "&ldquo;the ransom which the labourer pays to the capitalist for leave to "
                  "retire from the wage-labour market to the land&rdquo;."),
            ("p", "Wakefield had serious supporters, and their case was not only the "
                  "capitalist's. John Stuart Mill endorsed systematic colonisation as a "
                  "justified exception to leaving things to the market: settlers scattered "
                  "over cheap land, he argued, could not build roads, schools or markets, or "
                  "combine their labour, and concentrated settlement would make everyone "
                  "richer. In 1970 Evsey Domar turned Wakefield's observation into a general "
                  "hypothesis: free land, free peasants and a class of landowners who do not "
                  "work cannot all exist together, and any two exclude the third, which, he "
                  "argued, is why free land so often went with serfdom or slavery. Marx notes "
                  "that Wakefield himself called slavery the natural basis of colonial "
                  "wealth."),
            ("p", "The scheme failed, Marx says, as completely as Sir Robert Peel's Bank Act, a "
                  "different Peel's fiasco: emigrants "
                  "went to the United States instead. And then the old world caught up with "
                  "the new. Immigration outran the westward movement, the Civil War brought a "
                  "national debt and a financial aristocracy, public land went to railway "
                  "companies, and the United States ceased to be the promised land for "
                  "emigrant labourers. What the colonies had blurted out, Marx ends, is that the "
                  "capitalist mode of production and accumulation, and with them capitalist "
                  "private property, have &ldquo;for their fundamental condition the "
                  "annihilation of self-earned private property; in other words, the "
                  "expropriation of the labourer&rdquo;."),
            ("p", "That is the end of Volume I, which has studied capital in production and "
                  "asked where its first conditions came from. The next course, The Circuits of "
                  "Capital, opens Volume II and follows capital in motion, through the forms of "
                  "money, production and commodities that it must pass through again and "
                  "again."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "colony",
            "money_unit": "£",
            "periods": 4,
            "preset": "peel",
            "presets": [
                {"id": "peel", "label": "Marx's figures: Mr. Peel's £50,000 and 3,000 colonists, land free",
                 "capital": 50000, "colonists": 3000, "land_price_years": 0, "saving_share": "1/2",
                 "expect": {"acReserve": "0", "acYearsToLand": "0 years"}},
                {"id": "wakefield", "label": "Wakefield's sufficient price: land at two years' wages, half the wage saved",
                 "capital": 50000, "colonists": 3000, "land_price_years": 2, "saving_share": "1/2",
                 "expect": {"acReserve": "3,000", "acYearsToLand": "4 years"}},
                {"id": "closed", "label": "No land to be had: nothing the workers save will buy it",
                 "capital": 50000, "colonists": 3000, "land_price_years": 2, "saving_share": 0,
                 "expect": {"acReserve": "3,000", "acYearsToLand": "never"}},
            ],
            "panel_title": "Workers for hire in a colony",
            "panel_intro": (
                "The price of land is in years of a worker's full wage; a worker who saves "
                "the stated share of his wage buys land after that price divided by the "
                "share, and leaves wage-labour. The first tile counts the workers still for "
                "hire in the last period shown; the lab ships four. Move the periods to five "
                "with the Wakefield preset and watch them go."
            ),
        }),
        "steps_title": "Labour for hire in a colony",
        "steps_intro": "Four steps, from the price of land to the workers a capitalist can find.",
        "steps": [
            ("State the price of land in wages",
             "Express the land price as years of a worker's full wage. Free land has a price "
             "of 0."),
            ("Find the years to buy land",
             "Years of wage-labour = land price in years / share of the wage saved. If "
             "nothing can be saved, the worker never buys."),
            ("Count the workers for hire",
             "In each period before the years run out, every colonist is for hire; after "
             "that, none is. With free land, none is from the start."),
            ("Read what the capital commands",
             "Set the capital beside the workers it can hire. Where they are 0, the money and "
             "means of production are present and command no one."),
        ],
        "worked": {
            "title": "Peel and Wakefield",
            "intro": [
                "A colonist brings £50,000 and 3,000 workers. You want the workers for hire "
                "with free land, and with land priced at two years' wages when a worker "
                "saves half his wage.",
            ],
            "lines": [
                "free land:  0 / (1/2) = 0 years; 0 for hire",
                "Wakefield:  2 / (1/2) = 4 years of wage-labour",
                "periods 1 to 4:  3,000 for hire",
                "period 5:  0 for hire, unless others follow",
            ],
            "after": [
                "Peel's £50,000 and 3,000 people are Marx's figures as the Kerr text prints "
                "them. The land price and the saving are illustrative, chosen to give the "
                "four years in the lesson.",
            ],
        },
        "quiz_title": "Capital without wage-labour",
        "quiz": [
            {"q": "Land costs three years' wages and a worker saves a quarter of his wage. How "
                  "many years must he work for wages before he can buy land?",
             "a": ["12", "3", "3/4", "4"],
             "c": 0,
             "why": "Years = price in years / share saved = 3 / (1/4) = 12. Three is the price "
                    "itself, which he could meet only by saving the whole wage; 3/4 "
                    "multiplies instead of dividing; 4 inverts the share alone."},
            {"q": "A colonist brings £20,000 and 500 workers to a place where land is free. On "
                  "the lab's model, how many workers are for hire after the first period?",
             "a": ["0", "500", "250", "40"],
             "c": 0,
             "why": "With free land every worker can leave wage-labour at once, so none is "
                    "for hire, whatever the capital. Five hundred is the number brought; 250 "
                    "and 40 come from dividing figures the model does not divide."},
            {"q": "What did Wakefield discover in the colonies, on Marx's reading?",
             "a": ["That colonies lack capital",
                   "That capital is a social relation between persons, established through "
                   "things",
                   "That land in the colonies is worthless",
                   "That high wages make workers more productive"],
             "c": 1,
             "why": "Marx credits Wakefield with discovering that &ldquo;capital is not a "
                    "thing, but a social relation between persons&rdquo;. Peel had capital in "
                    "plenty; the land was valuable enough that everyone wanted it; and "
                    "productivity is not the chapter's subject."},
            {"q": "What is Wakefield's &ldquo;sufficient price&rdquo; for land meant to do?",
             "a": ["Raise revenue to pay the colony's national debt",
                   "Keep labourers working for wages until others arrive to take their place",
                   "Make land cheap enough for every immigrant",
                   "Pay the original inhabitants for their land"],
             "c": 1,
             "why": "The price must be high enough &ldquo;to prevent the labourers from "
                    "becoming independent landowners until others had followed to take their "
                    "place&rdquo;. The proceeds were to bring out more labourers, not to "
                    "service a debt, and the scheme made land dearer, not cheaper."},
        ],
        "mistakes": [
            ("Thinking capital is a thing, money and machines, that can be exported",
             "Peel exported £50,000 of means of subsistence and production, and with free "
             "land the tile counts 0 workers for hire: the things arrived and the capital did "
             "not. Only the Wakefield and closed presets, which keep the workers from the "
             "land, give the £50,000 anyone to employ. This is the discovery Marx credits "
             "to Wakefield, while adding that Wakefield himself went on calling the settlers' "
             "own tools capital, and their spread among many owners an equal division of "
             "capital."),
            ("Reading the land price as a market price",
             "Wakefield's price was to be set by the state, &ldquo;independent of the law of "
             "supply and demand&rdquo;, at whatever level kept workers on the labour market. "
             "In the lab it is an input chosen for that effect, not a price discovered by "
             "trade."),
            ("Thinking the colony chapter is about the colonies",
             "Marx says the condition of the colonies does not concern him. What concerns him "
             "is the secret they reveal about Europe: that capitalist property requires the "
             "expropriation of the labourer, which at home has already happened and so is "
             "out of sight."),
        ],
        "standard": (
            "Finish when you can compute what free land does to a colonist's labour supply.",
            "Given a capital, a number of colonists, a land price in years of wages and the "
            "share of the wage saved, compute the years of wage-labour before a worker can "
            "buy land and the workers left for hire in a given period."
        ),
        "note": (
            "The lab's colony is a sketch of Wakefield's argument: every worker leaves the "
            "moment he can buy land and none leaves before. The 3,000 is the Kerr text's "
            "figure; the 1887 Moore and Aveling printing reads 300, and the lesson's point "
            "does not depend on which. The land price and the saving are illustrative."
        ),
    },
]
