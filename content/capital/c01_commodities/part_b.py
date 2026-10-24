"""Commodities and Money, lessons 5-8 -- Volume I, Chapters 2 and 3.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals are left out, a drop capital is printed as an
ordinary capital, and the translator's double quotation marks inside a
quotation are printed as single curly quotes. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Kerr vol. 1, l. 1034 (commodities cannot go to market); l. 1046 (Faust,
    # and the social act).
    {
        "slug": "exchange",
        "title": "Exchange",
        "module": "Chapter 2 · Exchange",
        "one_line": "Commodities need owners to take them to market, and the owners' own exchanges set one commodity apart as money.",
        "summary": (
            "Chapter 2 brings in the people the first chapter left out: the owners, who "
            "must recognise each other as private proprietors before their goods can meet. "
            "Count the exchange ratios a market of owners needs when everyone trades with "
            "everyone and when one commodity is everyone's equivalent, and see why Marx "
            "says that commodity becomes money by a social act, not by a convention."
        ),
        "key": [
            "owners, not things, make exchanges",
            "barter: n·(n − 1)/2 ratios",
            "one equivalent: n − 1 ratios",
            "money: set apart by a social act",
            "money is a commodity with a value",
        ],
        "key_label": "Chapter 2 in five lines",
        "concepts_intro": (
            "Chapter 2 is short, and it does two things: it puts people into the analysis, "
            "and it explains how one commodity comes to stand apart from the rest."
        ),
        "concepts": [
            ("Owners as personifications",
             "To exchange, owners must treat each other as private proprietors who part "
             "with goods only by consent. The contract between them reflects the economic "
             "relation, and the people on the economic stage are its personifications."),
            ("The owners' dilemma",
             "Each owner wants to treat his own commodity as the equivalent of all the "
             "others. Since every owner does, no commodity is, and their goods cannot be "
             "compared as values at all."),
            ("Money by a social act",
             "The dilemma is solved in practice, not by agreement: the owners &ldquo;acted "
             "and transacted before they thought&rdquo;, and their exchanges set one "
             "commodity apart as the universal equivalent. That commodity is money."),
        ],
        "read_title": "Commodities need guardians",
        "read_intro": (
            "After a chapter in which commodities expressed their values and even spoke, "
            "Chapter 2 opens by pointing out that they cannot walk."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 2.</strong> &ldquo;It is plain that commodities "
                  "cannot go to market and make exchanges of their own account. We must, "
                  "therefore, have recourse to their guardians, who are also their owners. "
                  "Commodities are things, and therefore without power of resistance against "
                  "man.&rdquo;"),
            ("p", "There is a dry joke in the first sentence. Chapter 1 had linen expressing "
                  "its value, coats acting as mirrors and commodities talking about "
                  "themselves. Now Marx admits that none of them can get to market. Someone "
                  "has to carry them, and that someone has a will of his own. So the owners "
                  "must &ldquo;mutually recognise in each other the right of private "
                  "proprietors&rdquo;, and their contract, &ldquo;whether such contract be "
                  "part of a developed legal system or not&rdquo;, only reflects the "
                  "economic relation underneath. One sentence here governs the rest of the "
                  "book: the characters on the economic stage &ldquo;are but the "
                  "personifications of the economical relations that exist between "
                  "them&rdquo;. When the capitalist appears later, he will be read the same "
                  "way."),
            ("p", "What separates a commodity from its owner? The commodity is &ldquo;a born "
                  "leveller and a cynic&rdquo;, ready to exchange with any other at all. The "
                  "owner is particular: his own commodity is no use to him, which is why he "
                  "brings it, and he wants something definite in return. &ldquo;All "
                  "commodities are non-use-values for their owners, and use-values for their "
                  "non-owners.&rdquo; So they must change hands, and they face a double test. "
                  "They must be realised as values before they can be used, and they must "
                  "prove useful to someone else before their value counts."),
            ("p", "Then the dilemma. To each owner, every other commodity is a particular "
                  "equivalent of his own, and his own is the universal equivalent of all the "
                  "rest. Every owner thinks this, so in fact no commodity is the universal "
                  "equivalent, and the goods cannot be compared as values at all. Marx's "
                  "answer comes from Goethe:"),
            ("p", "<strong>Volume I, Chapter 2.</strong> &ldquo;In their difficulties our "
                  "commodity-owners think like Faust: &lsquo;Im Anfang war die That.&rsquo; "
                  "They therefore acted and transacted before they thought. &hellip; But a "
                  "particular commodity cannot become the universal equivalent except by a "
                  "social act.&rdquo;"),
            ("p", "Goethe's line means <em>in the beginning was the deed</em>. Nobody sat "
                  "down and chose money. Exchange began at the edges of communities, between strangers, and "
                  "the proportions were &ldquo;at first quite a matter of chance&rdquo;. As "
                  "exchange became regular, the role of equivalent attached itself to "
                  "whatever was traded most: the main goods coming from outside, or the "
                  "community's chief movable wealth, like cattle. Nomads developed the money "
                  "form first, Marx says, because all their wealth could be moved. Over time "
                  "the role settled on the precious metals, whose every sample is alike and "
                  "which can be divided and recombined at will."),
            ("p", "The lab counts what a single equivalent saves. If every owner trades "
                  "directly with every other, each pair needs its own ratio: with `n` "
                  "commodities that is `n·(n − 1)/2`. Four commodities need 6 ratios, six "
                  "need 15. Once one commodity is everyone's equivalent, `n − 1` ratios say "
                  "the same thing: 3 and 5. Notice what the count does not care about. Make "
                  "cattle the equivalent or make gold the equivalent, and the answer is 5 "
                  "either way. The arithmetic shows why one equivalent is convenient. It "
                  "cannot show how one arises or why it ended up as gold, which is the part "
                  "of the chapter Marx cares about."),
            ("p", "That is where the chapter's argument with its predecessors lies. John "
                  "Locke wrote that the &ldquo;universal consent of mankind&rdquo; gave silver "
                  "an imaginary value as money, and Montesquieu called money a sign that "
                  "represents things. The strong form of their view is a fact Marx accepts: "
                  "coins wear thin and keep circulating, and in Chapter 3 he grants that "
                  "paper tokens can stand in for gold. If a token works, why not call money a "
                  "symbol? Marx's reply is that the token works only because it stands for "
                  "a commodity that has value, and that calling money conventional was the "
                  "eighteenth century's way of explaining away forms it could not account "
                  "for, &ldquo;by ascribing to them a conventional origin&rdquo;."),
            ("p", "Money is a commodity, then, and its value is fixed like any other's, by "
                  "the labour-time needed to produce it, at the source, by barter. Exchange "
                  "gives gold &ldquo;not its value, but its specific value-form&rdquo;. Marx "
                  "says the hard part was never seeing that money is a commodity. &ldquo;The "
                  "difficulty lies &hellip; in discovering how, why and by what means a "
                  "commodity becomes money.&rdquo;"),
            ("p", "And once it has become money, the steps vanish. It looks as if every "
                  "commodity expresses its value in gold because gold is money, when gold is "
                  "money because every commodity expresses its value in it. &ldquo;Hence the "
                  "magic of money.&rdquo; The riddle of money, Marx ends, is the riddle of the "
                  "commodity, &ldquo;only it now strikes us in its most glaring form&rdquo;."),
            ("p", "Money exists now. The next lesson, “Money as Measure and Means of "
                  "Circulation”, asks what it does: first how it measures values as prices, "
                  "then how much of it a day's trade needs."),
        ],
        "lab": ("capkit", {
            "mode": "form",
            "view": "count",
            "money_unit": "hours",
            "preset": "four",
            "presets": [
                {"id": "four", "label": "Four commodities, linen as equivalent",
                 "goods": [{"name": "linen", "qty": 20, "unit": "yards", "hours": 20},
                           {"name": "coat", "qty": 1, "unit": "", "hours": 20},
                           {"name": "tea", "qty": 10, "unit": "lb", "hours": 20},
                           {"name": "corn", "qty": 1, "unit": "quarter", "hours": 20}],
                 "equivalent": "linen", "expect": {"foPairs": "6", "foWithEquivalent": "3"}},
                {"id": "six", "label": "Six commodities, cattle as equivalent",
                 "goods": [{"name": "linen", "qty": 20, "unit": "yards", "hours": 20},
                           {"name": "coat", "qty": 1, "unit": "", "hours": 20},
                           {"name": "tea", "qty": 10, "unit": "lb", "hours": 20},
                           {"name": "coffee", "qty": 40, "unit": "lb", "hours": 20},
                           {"name": "corn", "qty": 1, "unit": "quarter", "hours": 20},
                           {"name": "cattle", "qty": 1, "unit": "head of", "hours": 20}],
                 "equivalent": "cattle", "expect": {"foPairs": "15", "foWithEquivalent": "5"}},
                {"id": "six-gold", "label": "Six commodities, gold as equivalent",
                 "goods": [{"name": "linen", "qty": 20, "unit": "yards", "hours": 20},
                           {"name": "coat", "qty": 1, "unit": "", "hours": 20},
                           {"name": "tea", "qty": 10, "unit": "lb", "hours": 20},
                           {"name": "coffee", "qty": 40, "unit": "lb", "hours": 20},
                           {"name": "corn", "qty": 1, "unit": "quarter", "hours": 20},
                           {"name": "gold", "qty": 2, "unit": "ounces", "hours": 20}],
                 "equivalent": "gold", "expect": {"foPairs": "15", "foWithEquivalent": "5"}},
            ],
            "panel_title": "How many ratios a market needs",
            "panel_intro": (
                "Each commodity has one owner. The first tile counts the ratios needed when "
                "every owner trades directly with every other; the second, when one "
                "commodity is everyone's equivalent. Compare the last two presets, which "
                "differ only in which commodity is the equivalent."
            ),
        }),
        "steps_title": "Counting exchange ratios",
        "steps_intro": "Four steps for a market of n commodities, each with one owner.",
        "steps": [
            ("Count the commodities",
             "Let n be the number of different commodities brought to market, one owner "
             "each."),
            ("Count the pairs for barter",
             "Each pair of commodities needs its own ratio: `n·(n − 1)/2`. The product "
             "`n·(n − 1)` counts every pair twice, once from each end, so it is halved."),
            ("Count the ratios with one equivalent",
             "Every commodity but the equivalent needs one ratio, its price in the "
             "equivalent: `n − 1`. Any ratio between two other commodities follows from "
             "theirs."),
            ("Name what the count leaves out",
             "The count is the same whichever commodity is the equivalent. Which one it is, "
             "and how it came to be, is settled by the owners' exchanges, not by the "
             "arithmetic."),
        ],
        "worked": {
            "title": "Six owners at market",
            "intro": [
                "Six owners bring linen, coats, tea, coffee, corn and gold. You want the "
                "number of ratios they need, trading each with each, and with gold as every "
                "owner's equivalent.",
            ],
            "lines": [
                "barter:  6 · 5 / 2 = 15 ratios",
                "with gold as equivalent:  6 − 1 = 5 ratios",
                "with cattle as equivalent:  6 − 1 = 5 ratios",
            ],
            "after": [
                "Fifteen ratios fall to five whichever commodity is the equivalent. Marx's "
                "point lies outside the count: one commodity becomes the equivalent by "
                "&ldquo;a social act&rdquo; of all the owners, who &ldquo;acted and "
                "transacted before they thought&rdquo;.",
            ],
        },
        "quiz_title": "Owners, ratios and money",
        "quiz": [
            {"q": "Five owners each bring a different commodity and trade each with each. "
                  "How many exchange ratios are needed?",
             "a": ["10", "20", "5", "25"],
             "c": 0,
             "why": "Each pair needs one ratio, and five commodities make `5 · 4 / 2 = 10` "
                    "pairs. Twenty counts each pair twice; 5 is the number of commodities; "
                    "25 pairs each commodity with itself as well."},
            {"q": "Seven commodities are traded, and one of them serves as every owner's "
                  "equivalent. How many ratios are needed?",
             "a": ["21", "6", "7", "42"],
             "c": 1,
             "why": "Every commodity except the equivalent needs one price in it: "
                    "`7 − 1 = 6`. Twenty-one is the barter count, 7 gives the equivalent a "
                    "price in itself, and 42 is every ordered pair."},
            {"q": "On Marx's account in Chapter 2, how does one commodity become the "
                  "universal equivalent?",
             "a": ["By a social act of the owners, in their exchanges",
                   "By a law that names it legal tender",
                   "By an agreement the owners reach after comparing the alternatives",
                   "By a natural property that makes it valuable in itself"],
             "c": 0,
             "why": "Marx says the owners &ldquo;acted and transacted before they "
                    "thought&rdquo;, and that a commodity becomes the equivalent only "
                    "&ldquo;by a social act&rdquo;. A deliberate agreement is exactly what "
                    "he denies; the state enters with coinage in Chapter 3; and no property "
                    "of gold makes it money by nature."},
            {"q": "In the lab, which change leaves both tiles unchanged?",
             "a": ["Adding a seventh commodity",
                   "Choosing gold instead of cattle as the equivalent",
                   "Removing two commodities",
                   "Taking the cattle out of the market altogether"],
             "c": 1,
             "why": "Both counts depend only on how many commodities there are, so swapping "
                    "one equivalent for another changes neither. Adding or removing "
                    "commodities changes both, and the equivalent is a commodity like the "
                    "rest: take the cattle away and five remain, needing 10 ratios by barter "
                    "and 4 with whichever commodity now serves as the equivalent."},
        ],
        "mistakes": [
            ("Thinking money is a mere symbol fixed by convention",
             "Locke and Montesquieu held versions of this, and it has a fact behind it: "
             "worn coins and paper tokens do circulate. Marx's answer is that a token works "
             "because it stands for a commodity with value, and that the commodity was set "
             "apart by the owners' exchanges, not chosen. The lab's count makes the point "
             "from the other side: it is the same 5 ratios for cattle or gold, so nothing "
             "in the convenience of an equivalent decides which commodity it is."),
            ("Reading the count as Marx's explanation of money",
             "Fifteen ratios against five shows why one equivalent is useful. Marx's "
             "argument is that the owners never made that calculation; the equivalent "
             "arose in exchange and was fixed by habit. The note says the lab cannot show "
             "that."),
            ("Thinking exchange gives gold its value",
             "Gold's value is fixed like any commodity's, by the labour needed to produce "
             "it, and is already given when it enters circulation. Exchange gives it "
             "&ldquo;not its value, but its specific value-form&rdquo;."),
        ],
        "standard": (
            "Finish when you can count a market's ratios and say how money arises.",
            "Given the number of commodities, compute the ratios barter needs and the "
            "ratios one equivalent needs, and state, in Marx's terms, what sets one "
            "commodity apart as money."
        ),
        "note": (
            "The count shows why one equivalent is needed, and nothing more. Marx's "
            "point is how it arises, by &ldquo;a social act&rdquo; of owners who "
            "&ldquo;acted and transacted before they thought&rdquo;, and no figure in the "
            "lab can show that. Money today is not a commodity like gold; this course reads "
            "Volume I for the gold-based money Marx describes and does not model the "
            "money we use."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 1, l. 1093 and l. 1136 (money as measure; price as money-name);
    # l. 1269 (the law of the quantity of the circulating medium).
    {
        "slug": "money-as-measure-and-means-of-circulation",
        "title": "Money as Measure and Means of Circulation",
        "module": "Chapter 3 · Money, or the Circulation of Commodities",
        "one_line": "Gold turns values into prices, and the money a day's trade needs is the sum of its prices divided by how often each coin changes hands.",
        "summary": (
            "Money's first two functions: it measures values as prices, ideally, without a "
            "grain of real gold, and it circulates commodities, selling in order to buy. "
            "Compute prices from values and gold's value, compute the money a day's sales "
            "need at a given velocity, and compute both again when gold's value changes "
            "and no commodity's does."
        ),
        "key": [
            "price = value in hours / hours in £1",
            "C–M–C: selling in order to buy",
            "money needed = sum of prices / velocity",
            "gold cheapens: prices and money needed rise",
            "measure of value ≠ standard of price",
        ],
        "key_label": "Measure and circulation",
        "concepts_intro": (
            "Chapter 3 is long, and its first two sections take money in the order it "
            "works: first as a measure, then as the go-between in exchange."
        ),
        "concepts": [
            ("Measure of value",
             "Gold expresses every commodity's value as a quantity of gold, which is its "
             "price. It does this in the imagination: a price tag needs no gold. Gold can "
             "measure value only because it has value itself."),
            ("Standard of price",
             "A fixed weight of gold, named a pound and divided into shillings and pence, "
             "measures quantities of gold. A change in gold's value leaves the standard "
             "untouched and changes every price."),
            ("Means of circulation",
             "In C–M–C a commodity is sold for money and the money buys another. The "
             "quantity of money circulation needs is fixed by the sum of prices and by how "
             "many moves each coin makes."),
        ],
        "read_title": "Price, and how much money",
        "read_intro": (
            "Two passages, one from each section: what a price is, and the law Marx draws "
            "from a chain of four sales."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 3, §1.</strong> &ldquo;It is not money that "
                  "renders commodities commensurable. Just the contrary. It is because all "
                  "commodities, as values, are realised human labour, and therefore "
                  "commensurable, that their values can be measured by one and the same "
                  "special commodity, and the latter be converted into the common measure of "
                  "their values, i.e., into money. &hellip; Price is the money-name of the "
                  "labour realised in a commodity.&rdquo;"),
            ("p", "Every price you have ever read is this function at work. The shopkeeper "
                  "who writes a price on a ticket uses no gold to do it; Marx says the owner "
                  "must &ldquo;lend them his tongue, or hang a ticket on them&rdquo;. Money "
                  "as a measure is &ldquo;imaginary or ideal money&rdquo;, and &ldquo;it does "
                  "not require the least bit of real gold, to estimate in that metal millions "
                  "of pounds' worth of goods&rdquo;. Yet the price depends entirely on what "
                  "money is made of. Measure a ton of iron in gold and in silver and you get "
                  "two very different prices for one value. (Marx assumes gold throughout, "
                  "&ldquo;for the sake of simplicity&rdquo;.)"),
            ("p", "Marx then separates two jobs the word money does. As the <strong>measure "
                  "of value</strong>, gold is the incarnation of human labour, and it turns "
                  "values into prices. As the <strong>standard of price</strong>, it is a "
                  "fixed weight of metal, divided and named. The pound began as a pound "
                  "weight of silver, and centuries of kings and princes debasing the coin "
                  "left, as Marx puts it, nothing of the original weights &ldquo;but the "
                  "names&rdquo;. A change in gold's value leaves the standard alone, since 12 "
                  "ounces are still 12 times one ounce. It changes every price."),
            ("p", "A price can also part company with value. A quarter of wheat whose value "
                  "is expressed by £2 may sell for £3 or £1, and these are still its prices. "
                  "Marx calls this &ldquo;no defect&rdquo;: in this mode of production the "
                  "laws assert themselves only as the average of irregularities that cancel "
                  "out. Things with no value can have a price too, such as &ldquo;conscience, "
                  "honour&rdquo;, or uncultivated land."),
            ("p", "Section 2 follows the weaver to market. He sells 20 yards of linen for £2 "
                  "and spends the £2 on a family Bible: C–M–C, selling in order to buy. The "
                  "first leap, from commodity to money, Marx calls the &ldquo;salto "
                  "mortale&rdquo; of the commodity, because it may fall short: the market "
                  "may already have all the linen it wants. And once the two halves are "
                  "separate, they can come apart. &ldquo;No one can sell unless some one else "
                  "purchases. But no one is forthwith bound to purchase, because he has just "
                  "sold.&rdquo; The economists who followed Jean-Baptiste Say argued that "
                  "since every sale is a purchase, supply creates its own demand and a "
                  "general glut is impossible. Marx answers that the separation gives "
                  "&ldquo;the possibility, and no more than the possibility, of "
                  "crisis&rdquo;. The next lesson takes that possibility further."),
            ("p", "Then the question of quantity. Marx chains four sales: a quarter of wheat "
                  "for £2, the £2 for 20 yards of linen, then for a Bible, then for 4 gallons "
                  "of brandy. Sold side by side in four places, they need £8. Sold one after "
                  "another, the same £2 makes four moves and realises all £8 of prices. "
                  "From this he draws a law:"),
            ("p", "<strong>Volume I, Chapter 3, §2.</strong> &ldquo;Hence, for a given "
                  "interval of time during the process of circulation, we have the following "
                  "relation: the quantity of money functioning as the circulating medium is "
                  "equal to the sum of the prices of the commodities divided by the number of "
                  "moves made by coins of the same denomination. This law holds "
                  "generally.&rdquo;"),
            ("p", "The lab sets each of Marx's four commodities at 20 hours of value and £1 of "
                  "gold at 10 hours, so each is priced at £2 as Marx has it; the hours are "
                  "illustrative, the prices are his. At a velocity of 4 the day needs £2; side "
                  "by side, at velocity 1, it needs £8. Halve the value of gold, so that £1 "
                  "holds 5 hours, and every price doubles to £4, the sum to £16, and the money "
                  "needed to £4, though nothing about wheat or linen changed. Double the "
                  "velocity instead and £1 does the work of £2."),
            ("p", "That gold-falls case is where Marx parts from David Hume. In his 1752 essay "
                  "on money Hume argued that money is not one of the wheels of trade but what "
                  "makes them turn more smoothly, and that if the money in a country were "
                  "multiplied, prices would rise in the same proportion. It is a powerful "
                  "argument, and it fits what people saw after the American silver and gold "
                  "flowed into Europe: more metal, higher prices. Marx argues that for gold "
                  "coin the causation runs the other way: given the sum of values and the "
                  "velocity, &ldquo;the quantity of precious metal current as money depends on "
                  "the value of that precious metal&rdquo;. Cheaper gold raised prices, and "
                  "higher prices drew more gold into circulation. The opposite opinion, he "
                  "says, rested on &ldquo;the absurd hypothesis that commodities are without a "
                  "price, and money without a value, when they first enter into "
                  "circulation&rdquo;; the footnote that names Hume names Jacob Vanderlint and "
                  "Nicholas Barbon before him. Any gold that circulation does not need is "
                  "withdrawn into hoards."),
            ("p", "For paper, Marx agrees with a version of the quantity rule. Paper issued by "
                  "the state stands for gold, and if twice as much is issued as the gold it "
                  "replaces would amount to, &ldquo;£1 would be the money-name not of ¼ of an "
                  "ounce, but of 1/8 of an ounce of gold&rdquo;, and every price in pounds "
                  "doubles. The difference is that paper has no value of its own to be "
                  "withdrawn."),
            ("p", "So far money has changed hands at the moment the goods did. The next "
                  "lesson, “Hoards and Means of Payment”, asks what happens when "
                  "money stops moving, and when it arrives long after the goods."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "circulate",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: four commodities at £2, sold one after another",
                 "goods": [{"name": "quarter of wheat", "value_hours": 20},
                           {"name": "20 yards of linen", "value_hours": 20},
                           {"name": "Bible", "value_hours": 20},
                           {"name": "4 gallons of brandy", "value_hours": 20}],
                 "gold_hours_per_unit": 10, "velocity": 4, "expect": {"moPriceSum": "£8", "moNeeded": "£2"}},
                {"id": "side-by-side", "label": "Marx's figures: the same four sold side by side",
                 "goods": [{"name": "quarter of wheat", "value_hours": 20},
                           {"name": "20 yards of linen", "value_hours": 20},
                           {"name": "Bible", "value_hours": 20},
                           {"name": "4 gallons of brandy", "value_hours": 20}],
                 "gold_hours_per_unit": 10, "velocity": 1, "expect": {"moPriceSum": "£8", "moNeeded": "£8"}},
                {"id": "gold-falls", "label": "Gold's value halves; the commodities' do not",
                 "goods": [{"name": "quarter of wheat", "value_hours": 20},
                           {"name": "20 yards of linen", "value_hours": 20},
                           {"name": "Bible", "value_hours": 20},
                           {"name": "4 gallons of brandy", "value_hours": 20}],
                 "gold_hours_per_unit": 5, "velocity": 4, "expect": {"moPriceSum": "£16", "moNeeded": "£4"}},
                {"id": "faster", "label": "Each coin makes 8 moves instead of 4",
                 "goods": [{"name": "quarter of wheat", "value_hours": 20},
                           {"name": "20 yards of linen", "value_hours": 20},
                           {"name": "Bible", "value_hours": 20},
                           {"name": "4 gallons of brandy", "value_hours": 20}],
                 "gold_hours_per_unit": 10, "velocity": 8, "expect": {"moPriceSum": "£8", "moNeeded": "£1"}},
            ],
            "panel_title": "From values to prices to money in circulation",
            "panel_intro": (
                "Each commodity's value in hours, divided by the hours in £1 of gold, gives "
                "its price. The sum of prices divided by the velocity gives the money the "
                "day's circulation needs. Compare the gold-falls preset with Marx's: only "
                "gold's value changed."
            ),
        }),
        "steps_title": "From values to the money needed",
        "steps_intro": "Four steps, in the order Marx takes them.",
        "steps": [
            ("Price each commodity",
             "Divide its value in hours by the hours of labour in one unit of money. "
             "Twenty hours at 10 hours to £1 is £2."),
            ("Sum the prices",
             "Add the prices of everything to be sold in the period. This is the sum of "
             "gold that circulation must realise."),
            ("Divide by the velocity",
             "Velocity is the number of moves each piece of money makes in the period. "
             "Money needed is the sum of prices divided by the velocity."),
            ("Trace a change to its source",
             "If gold's value changes, every price changes inversely and the money needed "
             "follows the prices. If the velocity changes, prices stay and only the money "
             "needed moves."),
        ],
        "worked": {
            "title": "Wheat, linen, a Bible and brandy",
            "intro": [
                "Marx's four commodities are each worth £2, and the same coins buy them one "
                "after another in a day. You want the money circulation needs, and what "
                "happens when gold's value halves.",
            ],
            "lines": [
                "prices:  4 · £2 = £8",
                "velocity:  the £2 makes 4 moves",
                "money needed:  £8 / 4 = £2",
                "gold halves:  4 · £4 = £16;  £16 / 4 = £4",
            ],
            "after": [
                "The money needed doubled because gold's value fell, through prices. On "
                "Marx's account the quantity of coin followed the prices; it did not set "
                "them.",
            ],
        },
        "quiz_title": "Prices and the money they need",
        "quiz": [
            {"q": "Five commodities are each priced at £3, and the same coins buy them one "
                  "after another, each coin making 5 moves in the day. How much money does "
                  "circulation need?",
             "a": ["£3", "£15", "£75", "£5"],
             "c": 0,
             "why": "The sum of prices is `5 · £3 = £15`, divided by 5 moves gives £3. "
                    "Fifteen pounds would be needed if all five sold at once; £75 multiplies "
                    "instead of dividing; £5 confuses the number of moves with money."},
            {"q": "The value of gold doubles and no commodity's value changes. With the "
                  "velocity fixed, what happens on Marx's account?",
             "a": ["Prices double and the money needed doubles",
                   "Prices halve and the money needed halves",
                   "Prices stay the same and the money needed halves",
                   "Prices halve and the money needed stays the same"],
             "c": 1,
             "why": "Each £1 now holds twice the labour, so each price, value divided by "
                    "the hours in £1, halves. The money needed is the sum of prices divided "
                    "by the velocity, so it halves too. Prices cannot stay the same, since "
                    "the measure changed."},
            {"q": "Which describes gold as the standard of price rather than the measure of "
                  "value?",
             "a": ["The incarnation of human labour in which values are expressed",
                   "A fixed weight of metal, divided and named, used to measure quantities "
                   "of gold",
                   "The commodity whose value determines what prices are",
                   "The money that must be present in coin at every sale"],
             "c": 1,
             "why": "Marx defines the standard of price as a fixed weight of metal that "
                    "measures quantities of gold. The first and third describe the measure of "
                    "value, and the fourth confuses both with the means of circulation."},
            {"q": "The state issues twice as much paper money as the gold coin it replaces "
                  "would amount to. On Marx's account, what follows?",
             "a": ["Half the notes flow back to the state unused",
                   "The value of gold halves",
                   "£1 names half the gold it did, and prices in pounds double",
                   "Nothing, because paper is only a symbol"],
             "c": 2,
             "why": "Marx says the excess paper still represents only the gold circulation "
                    "needs, so £1 comes to name 1/8 of an ounce instead of ¼ and prices "
                    "double. Gold's value is unaffected, and inconvertible paper with "
                    "compulsory circulation cannot simply flow back."},
        ],
        "mistakes": [
            ("Thinking that, with gold coin, prices are set by the quantity of money",
             "This is Hume's view, and Ricardo's after him, and it fits the observation "
             "that more gold went with higher prices. Marx argues that for metal the "
             "causation runs the other way. In the gold-falls preset gold's value halves "
             "and nothing else changes: prices double to £4 and the money needed doubles to "
             "£4 because the prices did. Gold beyond what circulation needs goes into "
             "hoards. For paper issued beyond the gold it stands for, Marx agrees that "
             "prices rise."),
            ("Confusing the measure of value with the standard of price",
             "The measure turns values into prices and works only because gold has value. "
             "The standard is a fixed weight of gold named a pound, and it is unaffected by "
             "gold's value. A fall in gold's value changes every price and leaves the "
             "standard exactly as it was."),
            ("Taking a price to be the value",
             "A price is the value's expression in money, and it may be above or below "
             "it: the quarter of wheat at £3 or £1. Things with no value, like uncultivated "
             "land, can have a price. Marx calls the possible gap &ldquo;no defect&rdquo; of "
             "the price-form."),
        ],
        "standard": (
            "Finish when you can compute prices and the money a day's sales need.",
            "Given values in hours, the hours in a unit of money and the velocity, compute "
            "each price, the sum of prices and the money needed in circulation, and compute "
            "them again after a change in gold's value or in the velocity."
        ),
        "note": (
            "The lab prices each commodity at its value, as Marx does in this section, and "
            "computes his law in one direction: from values and gold's value to prices to "
            "money. It cannot decide between that direction and Hume's, because both read "
            "the same correlation between gold and prices. The hours are illustrative; the "
            "£2 prices and the velocity of 4 are Marx's."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 1, l. 1383 (money current with payments); l. 1375 (the
    # virements at Lyons).
    {
        "slug": "hoards-and-means-of-payment",
        "title": "Hoards and Means of Payment",
        "module": "Chapter 3 · Money, or the Circulation of Commodities",
        "one_line": "Money that stops moving becomes a hoard, money that arrives after the goods settles a debt, and a chain of debts can cancel or break.",
        "summary": (
            "Money as money: held back from circulation as a hoard, or paid at a later "
            "date to close a sale already made. Compute the money a day needs once credit "
            "sales and payments falling due are counted, net a chain of debts that cancel, "
            "and see what one unpaid bill does to the cash the others need."
        ),
        "key": [
            "hoard: money withdrawn from circulation",
            "credit sale: goods now, money later",
            "need = prices − credit + payable − cancelled",
            "then divide by the velocity",
            "a broken chain needs hard cash",
        ],
        "key_label": "Money as money",
        "concepts_intro": (
            "Section 3 is about money no longer as a go-between but as the thing itself: "
            "kept, owed and finally paid."
        ),
        "concepts": [
            ("The hoard",
             "When a sale is not followed by a purchase, money stops circulating and "
             "becomes a hoard. Hoards are also a reservoir: they absorb coin that "
             "circulation does not need and release it when it needs more."),
            ("Means of payment",
             "When goods are sold now and paid for later, money measures the debt at the "
             "sale, and comes into circulation only on the due date, to close a "
             "transaction the goods finished long before."),
            ("Netting and its breakdown",
             "Debts that run in a circle can be set against each other and leave little or "
             "nothing to pay. When one link fails, the others suddenly need money in its "
             "hardest form."),
        ],
        "read_title": "The law, once payments fall due",
        "read_intro": (
            "Marx restates the law of the last lesson, now with credit in it, in one long "
            "sentence. A passage from earlier in the section shows how payments cancel."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 3, §3.</strong> &ldquo;If we now consider the "
                  "sum total of the money current during a given period, we shall find that, "
                  "given the rapidity of currency of the circulating medium and of the means "
                  "of payment, it is equal to the sum of the prices to be realised, plus the "
                  "sum of the payments falling due, minus the payments that balance each "
                  "other, minus finally the number of circuits in which the same piece of "
                  "coin serves in turn as means of circulation and of payment.&rdquo;"),
            ("p", "You live with this function of money all the time. Rent is paid at the end "
                  "of the month for a flat you have already lived in; a supplier delivers now "
                  "and sends an invoice due in thirty days. Marx uses the same case, a house "
                  "let for a term: the tenant &ldquo;buys it before he pays for it&rdquo;. "
                  "The seller becomes a creditor and the buyer a debtor, and money takes on "
                  "a new job."),
            ("p", "First, though, the money that stops. When a sale is not followed by a "
                  "purchase, money is changed, in Boisguillebert's words, &ldquo;from "
                  "&lsquo;meuble&rsquo; into &lsquo;immeuble&rsquo;&rdquo;, from movable "
                  "into immovable: it becomes a hoard. Marx is at his most sardonic about the "
                  "hoarder, who &ldquo;makes a sacrifice of the lusts of the flesh to his gold "
                  "fetish&rdquo;, whose cardinal virtues are &ldquo;Hard work, saving and "
                  "avarice&rdquo;, and whose labour is Sisyphus's, since any sum of money is "
                  "limited and money's power is not. But hoards also do a job. They are the "
                  "reservoir from which circulation draws coin and into which surplus coin "
                  "drains, so that it &ldquo;never overflows its banks&rdquo;. That is where, "
                  "in the last lesson, the gold that circulation did not need went."),
            ("p", "Now the debt. When the goods change hands before the money does, money "
                  "works three times over. It measures the debt in the contract. It acts as "
                  "an ideal means of purchase, moving the goods on a promise. And on the due "
                  "date it comes in as the <strong>means of payment</strong>, not to start a "
                  "transaction but to end one, &ldquo;as the absolute form of existence of "
                  "exchange value&rdquo;. The debtor sold his goods in order to pay; &ldquo;if "
                  "he do not pay, his goods will be sold by the sheriff&rdquo;."),
            ("p", "Read the opening passage with that in mind. The money a period needs is the "
                  "sum of prices, plus the payments falling due, minus those that balance "
                  "each other, and less again for coins that do several jobs in turn. The lab "
                  "writes this as one formula: take the prices, subtract the sales made on "
                  "credit (they need no money today), add the payments falling due, subtract "
                  "the payments that cancel, and divide by the velocity. That is the lab's "
                  "formalisation of Marx's sentence, not a formula he writes. How payments "
                  "cancel, he shows earlier in the section:"),
            ("p", "<strong>Volume I, Chapter 3, §3.</strong> &ldquo;The debts due to A from "
                  "B, to B from C, to C from A, and so on, have only to be confronted with "
                  "each other, in order to annul each other to a certain extent like positive "
                  "and negative quantities. There thus remains only a single balance to "
                  "pay.&rdquo;"),
            ("p", "Medieval merchants did exactly this at the fairs of Lyons, Marx notes, "
                  "settling a fair's debts by setting them against each other. In the lab "
                  "three dealers, A, B and C, each sell £100 of goods. Sold for cash at the "
                  "same moment, the three sales need £300. Sold on credit, with A owing B, B "
                  "owing C and C owing A £100 each on the same day, the debts cancel and no "
                  "money at all is needed. Then let A fail to pay. B still owes C £100 and now "
                  "has nothing coming in: £100 must be found in hard cash."),
            ("p", "That is a crisis in miniature, and Marx describes the large one in one of "
                  "the section's best passages. In good times money is only money of account; "
                  "&ldquo;On the eve of crisis, the bourgeois &hellip; declares money to be a "
                  "vain imagination. Commodities alone are money. But now the cry is "
                  "everywhere: money alone is a commodity!&rdquo; When the chain of payments "
                  "breaks, money is &ldquo;suddenly and immediately transformed, from its "
                  "merely ideal shape of money of account, into hard cash&rdquo;. That is why "
                  "the possibility of crisis from the last lesson takes the form of a money "
                  "crisis: everyone needs the means of payment at once."),
            ("p", "Credit-money, Marx adds, grows directly out of this function: bills that "
                  "record debts circulate to transfer them. And as production for sale "
                  "spreads, rents and taxes turn from payments in kind into payments in "
                  "money, which is why every country has its settling days, and why reserves "
                  "of means of payment grow even as the old hoarder disappears."),
            ("p", "All of this has stayed inside one country. The next lesson, “World "
                  "Money”, follows money across the border, where its local names stop "
                  "counting."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "payments",
            "money_unit": "£",
            "preset": "cash",
            "presets": [
                {"id": "cash", "label": "Three sales of £100 for cash, all at once",
                 "goods": [{"name": "cloth", "value_hours": 200},
                           {"name": "iron", "value_hours": 200},
                           {"name": "corn", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 0, "payments_due": 0, "cancelling": 0,
                 "bills": [], "expect": {"moNeeded": "£300", "moNetted": "£0"}},
                {"id": "chain", "label": "Sold on credit: A owes B, B owes C, C owes A",
                 "goods": [{"name": "cloth", "value_hours": 200},
                           {"name": "iron", "value_hours": 200},
                           {"name": "corn", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 300, "payments_due": 300, "cancelling": 300,
                 "bills": [{"from": "A", "to": "B", "amount": 100, "backed": True},
                           {"from": "B", "to": "C", "amount": 100, "backed": True},
                           {"from": "C", "to": "A", "amount": 100, "backed": True}],
                 "expect": {"moNeeded": "£0", "moNetted": "£0"}},
                {"id": "broken", "label": "The same chain, and A cannot pay B",
                 "goods": [{"name": "cloth", "value_hours": 200},
                           {"name": "iron", "value_hours": 200},
                           {"name": "corn", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 300, "payments_due": 200, "cancelling": 100,
                 "bills": [{"from": "A", "to": "B", "amount": 100, "backed": True},
                           {"from": "B", "to": "C", "amount": 100, "backed": True},
                           {"from": "C", "to": "A", "amount": 100, "backed": True}],
                 "default": 1, "expect": {"moNeeded": "£100", "moNetted": "£100"}},
            ],
            "panel_title": "Credit, payments and the cash they need",
            "panel_intro": (
                "Each bill runs from the party who pays to the party who is paid. The money "
                "needed is the lab's formula for Marx's sentence; the cash to settle the "
                "bills is computed by setting each party's bills against each other. In the "
                "broken preset bill 1 is unpaid, so B pays C with nothing coming in, and C's "
                "receipt and payment of £100 are the only ones that still cancel."
            ),
        }),
        "steps_title": "Computing money with payments",
        "steps_intro": "Four steps for a period in which some sales are on credit.",
        "steps": [
            ("Start from the prices",
             "Sum the prices of the commodities sold in the period, as for circulation."),
            ("Take out the credit sales",
             "Sales made on credit need no money in this period. Subtract them."),
            ("Add what falls due, less what cancels",
             "Add the payments falling due in the period for earlier sales, and subtract "
             "those that balance each other, party by party."),
            ("Divide, and test a default",
             "Divide by the velocity for the money needed. Then strike out one payment that "
             "is not made and recompute: the cancelling shrinks and the cash needed grows."),
        ],
        "worked": {
            "title": "A circle of debts, and one that breaks",
            "intro": [
                "Three dealers sell each other £100 of goods on credit. A owes B, B owes C "
                "and C owes A, all due today. You want the cash needed, and the cash needed "
                "if A cannot pay.",
            ],
            "lines": [
                "A: −100 + 100 = 0;  B: 0;  C: 0",
                "cash to settle:  £0",
                "A defaults:  A +100,  B −100,  C 0",
                "cash to settle:  £100, all of it B's",
            ],
            "after": [
                "Three hundred pounds of debts needed nothing while they cancelled. One "
                "failure turned £100 of them into a demand for coin, which is the money "
                "crisis in its smallest form.",
            ],
        },
        "quiz_title": "Payments, netting and hoards",
        "quiz": [
            {"q": "In a day, prices total £500, of which £200 are credit sales; £150 of "
                  "payments fall due, and £50 of them cancel; each coin makes 2 moves. On "
                  "the lab's formula, how much money is needed?",
             "a": ["£200", "£400", "£300", "£150"],
             "c": 0,
             "why": "`(500 − 200 + 150 − 50) / 2 = 400 / 2 = 200`. Four hundred forgets to "
                    "divide by the velocity; 300 forgets to subtract the credit sales; 150 "
                    "leaves out both the payments falling due and those that cancel."},
            {"q": "A owes B £50, B owes C £50 and C owes A £50, all due today and settled "
                  "by setting the debts against each other. How much cash is needed?",
             "a": ["£150", "£50", "£0", "£100"],
             "c": 2,
             "why": "Each dealer receives £50 and pays £50, so every balance is zero and the "
                    "debts annul each other. One hundred and fifty pounds would be needed "
                    "only if each debt were paid separately in coin with no coin passed on."},
            {"q": "In the same circle, B does not pay C. Set against each other, how much "
                  "cash do the two remaining debts need?",
             "a": ["£0", "£50", "£100", "£150"],
             "c": 1,
             "why": "A pays B £50 and receives £50 from C, so A balances; B receives £50; C "
                    "pays £50 with nothing coming in. C needs £50 in cash. The circle no "
                    "longer closes, so the answer cannot be £0."},
            {"q": "In a metallic circulation, what function does Marx give to hoards?",
             "a": ["A reservoir that absorbs coin circulation does not need and releases "
                   "it when it needs more",
                   "A way to raise prices by holding money back",
                   "The source of gold's value as money",
                   "A replacement for credit between merchants"],
             "c": 0,
             "why": "Hoards are the &ldquo;conduits for the supply or withdrawal of "
                    "money&rdquo; that keep circulation from overflowing. On Marx's account "
                    "prices are not set by the quantity held back, gold's value comes from "
                    "its production, and credit grows alongside hoards rather than being "
                    "replaced by them."},
        ],
        "mistakes": [
            ("Thinking money only matters as a medium of exchange",
             "In the broken preset no commodity changes hands at all, and yet £100 of hard "
             "cash is needed. Money there is the means of payment, closing a sale made "
             "earlier, and in a crisis it is wanted for that alone: &ldquo;money alone is a "
             "commodity!&rdquo;. A model with money only as a medium of exchange cannot "
             "see that demand."),
            ("Adding up debts as if each needed its own coin",
             "The chain preset has £300 of payments falling due and needs £0, because the "
             "payments balance party by party. The money needed depends on the net "
             "balances, not on the gross sum of the debts."),
            ("Treating the hoarder as outside the system",
             "Marx mocks the hoarder, but hoards are also the reservoir that lets the mass "
             "of coin in circulation expand and contract. As credit develops the miser "
             "fades, and reserves of means of payment grow in his place."),
        ],
        "standard": (
            "Finish when you can compute the money a period needs with credit in it.",
            "Given prices, credit sales, payments falling due, the payments that cancel and "
            "the velocity, compute the money needed; given a chain of bills, compute the "
            "cash that settles them, and again when one is not paid."
        ),
        "note": (
            "The money-needed formula is the lab's formalisation of Marx's sentence, which "
            "speaks of subtracting the circuits a coin makes rather than dividing by a "
            "velocity; the two agree when each coin does the same number of jobs. In the "
            "broken preset the unpaid bill is counted as no longer falling due, so that the "
            "formula and the netting of the bills return the same £100. The dealers and "
            "their £100 bills are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 1, l. 1402 (the local garbs); l. 1407 (money of the world).
    {
        "slug": "world-money",
        "title": "World Money",
        "module": "Chapter 3 · Money, or the Circulation of Commodities",
        "one_line": "Abroad, money drops its local names and returns to bullion, and a country's balance of payments is settled by shipping it.",
        "summary": (
            "Outside the country that coins it, money is gold or silver by weight, and its "
            "chief work is to settle international balances. Compute the bullion a country "
            "must ship when its imports exceed its exports, and again when it also owes a "
            "payment abroad."
        ),
        "key": [
            "abroad, money returns to bullion",
            "chief use: settling balances",
            "bullion out = imports − exports − receipts",
            "a payment owed abroad deepens the drain",
        ],
        "key_label": "Money of the world",
        "concepts_intro": (
            "The last few pages of Part I take money out of the country. Everything local "
            "about it stays behind."
        ),
        "concepts": [
            ("Bullion",
             "Coin, tokens, paper and the names of a standard of price are national. In "
             "trade between countries, money is the metal itself, counted by weight."),
            ("Three functions abroad",
             "World money is a universal means of payment, a universal means of purchase, "
             "and the recognised form of wealth when wealth is moved from one country to "
             "another. Settling balances is its chief use."),
            ("Two currents of gold",
             "Gold flows from the mines into every national circulation, and it flows back "
             "and forth between countries as their balances move."),
        ],
        "read_title": "Money strips off its local garbs",
        "read_intro": (
            "Marx's subsection on world money is only a few paragraphs long. Its first "
            "sentence carries the idea."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 3, §3.</strong> &ldquo;When money leaves the "
                  "home sphere of circulation, it strips off the local garbs which it there "
                  "assumes, of a standard of prices, of coin, of tokens, and of a symbol of "
                  "value, and returns to its original form of bullion. In the trade between "
                  "the markets of the world, the value of commodities is expressed so as to "
                  "be universally recognised.&rdquo;"),
            ("p", "Every local garb in that list is something earlier lessons built. The "
                  "standard of price was a weight of gold given a national name. Coin was "
                  "that weight stamped by the state. Tokens and paper stood in for it, and "
                  "held their place by &ldquo;forced currency&rdquo; within the state's own "
                  "territory. None of that crosses a border. A pound note means nothing to "
                  "a merchant in Hamburg except as a claim on gold, and so in the markets of "
                  "the world money is the metal, by weight. Only there, Marx says, does money "
                  "fully become what its concept says it is."),
            ("p", "At home there can be only one measure of value. In the world market, in "
                  "Marx's day, there were two, gold and silver, because different countries "
                  "used different metals. The double standard he called inconsistent at home "
                  "is simply a fact abroad."),
            ("p", "<strong>Volume I, Chapter 3, §3.</strong> &ldquo;Money of the world serves "
                  "as the universal medium of payment, as the universal means of purchasing, "
                  "and as the universally recognised embodiment of all wealth. Its function as "
                  "a means of payment in the settling of international balances is its chief "
                  "one. Hence the watchword of the mercantilists, balance of trade.&rdquo;"),
            ("p", "The three functions are the home functions at a larger scale. As a means "
                  "of payment, gold settles what one country owes another once their trade is "
                  "set off. As a means of purchase, it is shipped when the usual exchange of "
                  "goods is suddenly disturbed, after a failed harvest, say. And as wealth "
                  "itself, it moves when wealth must be transferred and goods will not serve: "
                  "a loan, a subsidy, a war indemnity."),
            ("p", "The mercantilists deserve their full hearing here. Writers such as Thomas "
                  "Mun, whose <em>England's Treasure by Forraign Trade</em> appeared in 1664, "
                  "argued that a country grows rich by selling abroad more than it buys and "
                  "taking the difference in gold and silver. In a world where only bullion "
                  "settled accounts, that was not foolish: the balance of trade decided "
                  "whether metal came in or went out. Smith attacked it as confusing money "
                  "with wealth. Marx's verdict is narrower: the mercantilists took the chief "
                  "function of world money for the whole of what money is."),
            ("p", "The lab does the settling. Imports of £1,000 against exports of £1,000 "
                  "balance, and no bullion moves. Let exports fall to £800 and £200 must be "
                  "shipped abroad in gold. Add a payment of £100 owed abroad, interest on a "
                  "debt, say, entered as negative other receipts, and the drain is £300. "
                  "Everything here is in pounds only for convenience: what crosses the "
                  "border is the gold those pounds name."),
            ("p", "The gold moves in two currents. One runs outward from the mines into every "
                  "national circulation, to fill its channels, replace worn coin, make "
                  "luxuries and lie in hoards. The other flows back and forth between "
                  "countries as their balances change. So every country needs a reserve for "
                  "world payments as well as for home ones, and Marx adds a sign worth "
                  "remembering: bank reserves far above their usual level are, with some "
                  "exceptions, a sign of stagnation, of commodities that are not moving."),
            ("p", "This is the gold-standard world Marx was describing. Today currencies are "
                  "not convertible into gold and international balances are settled in other "
                  "ways, and this course does not model them."),
            ("p", "That ends Part I. Money has measured values, circulated commodities, "
                  "gathered in hoards, settled debts and crossed borders, and in every case "
                  "it has been the middle of C–M–C, selling in order to buy. The next course, "
                  "From Money to Surplus Value, begins with money at the start of the "
                  "circuit instead, M–C–M′, and asks how money laid out can come back as "
                  "more money."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "world",
            "money_unit": "£",
            "preset": "balanced",
            "presets": [
                {"id": "balanced", "label": "Imports and exports of £1,000 each",
                 "imports": 1000, "exports": 1000, "other_receipts": 0, "expect": {"moDrain": "£0"}},
                {"id": "deficit", "label": "Imports £1,000, exports £800",
                 "imports": 1000, "exports": 800, "other_receipts": 0, "expect": {"moDrain": "£200 out"}},
                {"id": "drain", "label": "The same deficit and £100 owed abroad",
                 "imports": 1000, "exports": 800, "other_receipts": -100, "expect": {"moDrain": "£300 out"}},
            ],
            "panel_title": "The balance a country settles in bullion",
            "panel_intro": (
                "Imports less exports, less any other receipts from abroad, is what must be "
                "shipped in gold. A payment owed abroad goes in as negative other receipts. "
                "Try a surplus too: the tile then reports bullion flowing in."
            ),
        }),
        "steps_title": "Settling a balance in bullion",
        "steps_intro": "Four steps for one country over one period.",
        "steps": [
            ("Set imports against exports",
             "Subtract the value of exports from the value of imports. A positive "
             "difference is owed abroad; a negative one is owed to this country."),
            ("Add the other payments",
             "Subtract other receipts from abroad, and add payments owed abroad that are "
             "not for goods, such as interest on a debt."),
            ("Read the direction",
             "A positive total is shipped out in bullion. A negative total is bullion "
             "flowing in. Zero means nothing moves."),
            ("Name the function",
             "Gold settling a balance is the means of payment; gold shipped to buy grain "
             "after a failed harvest is the means of purchase; gold sent as a loan or "
             "indemnity is wealth transferred."),
        ],
        "worked": {
            "title": "A deficit and a debt",
            "intro": [
                "A country imports £1,000 of goods, exports £800, and owes £100 of interest "
                "abroad. You want the bullion it must ship.",
            ],
            "lines": [
                "trade:  1,000 − 800 = £200 owed abroad",
                "interest owed:  + £100",
                "bullion out:  200 + 100 = £300",
            ],
            "after": [
                "The £300 leaves as gold by weight. The names pound and shilling stay at "
                "home.",
            ],
        },
        "quiz_title": "Balances and bullion",
        "quiz": [
            {"q": "A country imports £500 of goods and exports £650, with no other payments. "
                  "How much bullion must it ship abroad?",
             "a": ["None: £150 flows in", "£150 out", "£1,150 out", "£500 out"],
             "c": 0,
             "why": "Imports less exports is `500 − 650 = −150`, so the balance is owed to "
                    "this country and gold flows in. One hundred and fifty out has the "
                    "direction reversed; £1,150 adds the two; £500 counts imports alone."},
            {"q": "A country imports £900, exports £700 and owes £50 of interest abroad. "
                  "How much bullion must it ship?",
             "a": ["£200", "£250", "£150", "£1,650"],
             "c": 1,
             "why": "The trade deficit is £200 and the interest owed adds £50, so £250 "
                    "goes out. Two hundred ignores the interest; 150 subtracts it; 1,650 adds "
                    "imports and exports."},
            {"q": "In settling international balances, in what form does money serve, on "
                  "Marx's account?",
             "a": ["Coin stamped by the paying country",
                   "Inconvertible paper with compulsory circulation",
                   "Bullion, gold or silver by weight",
                   "Copper and silver tokens"],
             "c": 2,
             "why": "Money leaving the home sphere strips off its local garbs and returns to "
                    "bullion. Coin, paper and tokens are exactly those local garbs, and paper "
                    "holds its place only by the state's compulsion within its own "
                    "territory."},
            {"q": "Which function of world money does Marx call its chief one?",
             "a": ["Means of payment in settling international balances",
                   "Means of purchase after a failed harvest",
                   "Measure of value in a single standard",
                   "Transfer of wealth as a war indemnity"],
             "c": 0,
             "why": "Marx says the settling of international balances is the chief function, "
                    "hence the mercantilists' watchword. Emergency purchases and transfers of "
                    "wealth are its other two functions, and in the world market there is a "
                    "double measure, gold and silver, not a single one."},
        ],
        "mistakes": [
            ("Thinking world money is just a currency exchanged at a rate",
             "In the deficit preset the £200 does not cross the border as pounds. It "
             "crosses as gold by weight, and the pound, a national name for a weight of "
             "gold, stays behind with the coin and the paper. An exchange rate between two "
             "national moneys rests on the metal each one names."),
            ("Taking the balance of trade for a measure of wealth",
             "That is the mercantilist reading. A surplus brings in gold, and gold is "
             "wealth in its universally recognised form, but Marx treats settling balances "
             "as one function of money, not as the source of a nation's wealth."),
            ("Leaving out payments that are not for goods",
             "Interest owed abroad, a loan or an indemnity moves bullion as surely as "
             "trade does. In the drain preset the same trade deficit ships £300, not £200, "
             "because £100 is owed abroad."),
        ],
        "standard": (
            "Finish when you can compute the bullion a country ships and say why it is bullion.",
            "Given imports, exports and other payments to and from abroad, compute the "
            "bullion shipped or received, state its direction, and name the function of "
            "world money it performs."
        ),
        "note": (
            "The lab nets one country's payments for one period and reports the "
            "difference; it knows nothing of exchange rates, of how fast a drain corrects "
            "itself, or of any money not backed by metal. The figures are illustrative, "
            "and the world they describe is the gold and silver one of Marx's day."
        ),
    },
]
