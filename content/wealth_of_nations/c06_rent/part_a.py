"""The Rent of Land, lessons 1-3 -- Book I, Chapter 11: the introduction, Part I and Part II.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition); the comment beside each lesson gives its
line numbers. The extraction's headings and running heads are left out of the
quotations, a word the line break split is joined as the printed book has it, and
nothing else is changed.

Money. The preset figures are written for the lessons unless a label says they are
Smith's. Smith's own sums are in pounds, shillings and pence (twelve pence to the
shilling, twenty shillings to the pound); the labs here take decimals and fractions.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 4730-4744 (the definition of rent); l. 4755-4767 (kelp);
    # l. 4768-4775 (Shetland); l. 4776-4778 (a monopoly price); l. 4779-4786 (what
    # can afford a rent); l. 4793-4800 (cause and effect).
    {
        "slug": "rent-as-a-monopoly-price",
        "title": "Rent as a Monopoly Price",
        "module": "Book I, Chapter 11 · Of the Rent of Land",
        "one_line": "Rent is what is left of a price after the tenant's outlay and ordinary profit, and it is the effect of a high price, never its cause.",
        "summary": (
            "Smith opens the longest chapter of the book by fixing what rent is: the "
            "most the tenant can afford to pay, which is the price of the produce less "
            "the stock he must replace and the ordinary profit he must keep. Work it "
            "out for three farms at one price, watch the poorest farm drop out of "
            "rent when the price falls, and see why Smith puts rent on the other side "
            "of the equation from wages and profit."
        ),
        "key": [
            "rent = price − outlay − ordinary profit",
            "outlay: wages plus the stock replaced",
            "the most the tenant can afford to pay",
            "no rent where price only repays outlay",
            "price high or low: rent is the effect",
        ],
        "key_label": "What rent is, in five lines",
        "concepts_intro": (
            "The chapter's first page is a definition, an objection answered and a "
            "single sentence of consequence. Each of the three ideas is short, and "
            "the rest of the chapter leans on all of them."
        ),
        "concepts": [
            ("Rent as the residual",
             "The landlord leaves the tenant only what keeps up his stock and pays the "
             "ordinary profit of farming in the neighbourhood. Everything above that in "
             "the price of the produce goes to rent. It is a remainder, not a charge "
             "built up from the landlord's costs."),
            ("A monopoly price",
             "Rent is &ldquo;naturally a monopoly price&rdquo;: it is fixed by what the "
             "farmer can afford to give, not by what the landlord laid out or could "
             "afford to take. The word is Smith's, and it is the first thing later "
             "economists argued about."),
            ("Cause and effect in price",
             "High or low wages and profit are why a price is high or low. High or low "
             "rent is a result of a price that is already high or low. A price that "
             "barely repays wages and profit affords no rent at all."),
        ],
        "read_title": "The definition first, then the objection it answers",
        "read_intro": (
            "The chapter begins without preamble. Read the first sentence slowly, "
            "because everything in the next fifty pages is an application of it."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 11.</strong> Rent, Smith begins, considered as "
                  "the price paid for the use of land, &ldquo;is naturally the highest "
                  "which the tenant can afford to pay in the actual circumstances of the "
                  "land&rdquo;. In fixing the terms of the lease the landlord "
                  "&ldquo;endeavours to leave him no greater share of the produce than "
                  "what is sufficient to keep up the stock from which he furnishes the "
                  "seed, pays the labour, and purchases and maintains the cattle and "
                  "other instruments of husbandry, together with the ordinary profits of "
                  "farming stock in the neighbourhood.&rdquo;"),
            ("p", "Picture the two of them across a table at the renewal of a lease. The "
                  "farmer knows what a year costs him: seed, wages, the upkeep of the "
                  "horses and ploughs. He also knows what he could earn by putting the "
                  "same stock into any other farm nearby, which is what Smith calls "
                  "ordinary profit. Below that he walks away. The landlord knows the "
                  "farmer knows it. So the figure they settle on is whatever the harvest "
                  "is worth beyond those two things, and Smith says this is "
                  "&ldquo;evidently the smallest share with which the tenant can content "
                  "himself, without being a loser, and the landlord seldom means to leave "
                  "him any more&rdquo;. He allows for exceptions in both directions, the "
                  "landlord's liberality or, more often, his ignorance, and then moves on "
                  "to call the figure the natural rent."),
            ("def", ("Ordinary profit, outlay and rent",
                     "The outlay is the wages paid and the other stock advanced in a year. "
                     "Ordinary profit is what that outlay would earn on any other farm in "
                     "the neighbourhood. Rent is whatever the produce sells for beyond "
                     "outlay plus ordinary profit.")),
            ("p", "Smith then turns aside to an objection he expects from the reader. "
                  "Surely the landlord's rent is only a fair return on the money he has "
                  "put into draining, fencing and building? He grants it &ldquo;may be "
                  "partly the case upon some occasions&rdquo;, and answers that it can "
                  "scarce be more, since the landlord demands a rent even for unimproved "
                  "land, and when a lease is renewed he asks the same increase whether "
                  "he or the tenant paid for the improvement. Then he gives his two "
                  "odd examples. Kelp is a seaweed, burnt to make an alkali for glass "
                  "and soap, and it grows on rocks the tide covers twice a day. Smith "
                  "remarks that it was &ldquo;never augmented by human industry&rdquo;, "
                  "and yet a landlord whose estate is bounded by a kelp shore demands a "
                  "rent for it &ldquo;as much as for his corn-fields&rdquo;. The sea "
                  "round Shetland is rich in fish, but to profit by it the fishers need "
                  "a house on the land, and the rent is in proportion to what the farmer "
                  "can make from the land and the water together."),
            ("p", "From these cases Smith draws his conclusion: &ldquo;The rent of land, "
                  "therefore, considered as the price paid for the use of the land, is "
                  "naturally a monopoly price. It is not at all proportioned to what the "
                  "landlord may have laid out upon the improvement of the land, or to "
                  "what he can afford to take, but to what the farmer can afford to "
                  "give.&rdquo; The phrase has had a long career. David Ricardo, "
                  "writing in 1817, held that it misdescribes what happens: on his "
                  "account rent is the surplus that better land yields over the poorest "
                  "land in use, and since that poorest land pays no rent, no combination "
                  "of landlords could raise the price of corn by asking more. Smith "
                  "cannot answer him, having died in 1790, but the chapter does say, "
                  "a page on, that a produce affords rent only if its price rises above "
                  "its outlay and ordinary profit, and that whether it does so "
                  "&ldquo;depends upon the demand&rdquo;. Whether that is a monopoly or "
                  "only a scarcity is a dispute about a word. Marx, for his part, "
                  "brought the monopoly back in at another point, which "
                  "<em>Absolute Ground Rent</em> in the Capital Subject takes up."),
            ("p", "The paragraph that follows is the one to keep: &ldquo;Such parts only "
                  "of the produce of land can commonly be brought to market, of which the "
                  "ordinary price is sufficient to replace the stock which must be "
                  "employed in bringing them thither, together with its ordinary "
                  "profits.&rdquo; If the price is more, &ldquo;the surplus part of it "
                  "will naturally go to the rent of the land&rdquo;. If not, the "
                  "commodity may still come to market, but it &ldquo;can afford no rent "
                  "to the landlord&rdquo;."),
            ("p", "And then the sentence that separates rent from everything in the "
                  "previous chapters: &ldquo;High or low wages and profit are the causes "
                  "of high or low price; high or low rent is the effect of it.&rdquo; "
                  "Smith spells it out. Wages and profit have to be paid to bring a "
                  "particular commodity to market, and that is why its price is high or "
                  "low. But &ldquo;it is because its price is high or low, a great deal "
                  "more, or very little more, or no more, than what is sufficient to pay "
                  "those wages and profit, that it affords a high rent, or a low rent, or "
                  "no rent at all&rdquo;."),
            ("p", "The lab shows the arithmetic with three farms written for this "
                  "lesson, since Smith gives no farm-by-farm figures here. Each pays "
                  "£60 in wages and lays out £40 in other stock, so the outlay is £100, "
                  "and ordinary profit is 10% of that, £10. The north farm yields 100 "
                  "quarters, the middle farm 80 and the poor farm 55. In the "
                  "three-farms preset corn sells at £2 a quarter. The north "
                  "farm's produce is worth £200 and its rent is £200 − £100 − £10 = £90, "
                  "the middle farm's is £160 − £110 = £50, and the poor farm's £110 − "
                  "£110 = £0. It is brought to market and pays its workers and its "
                  "profit, and affords the landlord nothing. Total rent is £140."),
            ("p", "Now let the price fall to £3/2 a quarter, one pound ten shillings, in "
                  "the price-falls preset. The "
                  "north farm's rent drops from £90 to £40, the middle farm's from £50 "
                  "to £10, and the poor farm's produce is worth only £82.50 against a "
                  "£110 that has to be covered, so it pays no rent and would not be "
                  "farmed at all if the tenant had any choice. Total rent falls from "
                  "£140 to £50. A quarter off the price took away more than "
                  "two-thirds of the rent, which is what it means for rent to be the "
                  "remainder: the whole change in price lands on it, because the "
                  "outlay does not move."),
            ("p", "Last, hold the price at £2 and raise every farm's wages from £60 to "
                  "£66, in the wages-rise preset. Outlay becomes £106 and "
                  "ordinary profit £10.60, so the north farm's rent is £200 − £116.60 = "
                  "£83.40 and the poor farm's is now a loss of £6.60. Smith's order "
                  "of cause is the same: in this preset it is the price of corn, "
                  "fixed by demand, that is held where it is, and the dearer labour is "
                  "paid out of rent. Whether in the long run a rise in wages would also "
                  "raise the price is the question of Chapters 6 to 9, which this lab "
                  "does not decide."),
            ("p", "The next lesson, <em>Produce Which Always Affords Rent</em>, asks "
                  "which parts of the produce of land are sure to pass the test of "
                  "this one, and why Smith says it is food."),
        ],
        "lab": ("wonkit", {
            "mode": "rent",
            "view": "residual",
            "money_unit": "£",
            "preset": "three-farms",
            "presets": [
                {"id": "three-farms", "label": "Three farms at £2 a quarter, written for this lesson",
                 "lands": "north, 100, 60, 40; middle, 80, 60, 40; poor, 55, 60, 40",
                 "price": "2", "rate": "10", "expect": {"wreRent": "north £90; middle £50; poor no rent (nothing left)", "wreTotal": "£140"}},
                {"id": "price-falls", "label": "The same farms when corn falls to £3/2 a quarter",
                 "lands": "north, 100, 60, 40; middle, 80, 60, 40; poor, 55, 60, 40",
                 "price": "3/2", "rate": "10", "expect": {"wreRent": "north £40; middle £10; poor no rent (a loss of £27.50)", "wreTotal": "£50"}},
                {"id": "wages-rise", "label": "Wages up from £60 to £66 on every farm, price held at £2",
                 "lands": "north, 100, 66, 40; middle, 80, 66, 40; poor, 55, 66, 40",
                 "price": "2", "rate": "10", "expect": {"wreRent": "north £83.40; middle £43.40; poor no rent (a loss of £6.60)", "wreTotal": "£126.80"}},
            ],
            "panel_title": "What is left for the landlord",
            "panel_intro": (
                "Each farm's output, wages and other stock go in, with the price of a "
                "quarter and the ordinary rate of profit. The lab values the produce, takes "
                "off the outlay and its ordinary profit, and prints what remains as rent. "
                "Try the second preset and watch the poor farm."
            ),
        }),
        "steps_title": "Finding the rent of a farm",
        "steps_intro": "Four steps, the same for any farm or any produce.",
        "steps": [
            ("Value the produce",
             "Multiply the quantity the farm yields in a year by the price at which it "
             "sells. This is the gross produce in money."),
            ("Add up the outlay",
             "Take the wages paid and the other stock advanced in the year: seed, the "
             "upkeep of horses and tools. Smith's list includes the labour, the seed "
             "and the cattle and instruments of husbandry."),
            ("Add the ordinary profit",
             "Multiply the outlay by the ordinary rate of profit of farming stock in "
             "the neighbourhood. The sum of outlay and profit is the least the tenant "
             "will accept."),
            ("Subtract",
             "Rent is the produce's value less that sum. If the result is zero or "
             "negative, the farm affords no rent at this price, whatever it grows."),
        ],
        "worked": {
            "title": "The north farm, then the poor farm",
            "intro": [
                "Take the first preset. The north farm yields 100 quarters, pays £60 in "
                "wages and lays out £40 more. Ordinary profit is 10%, corn is £2 a "
                "quarter.",
            ],
            "lines": [
                "produce:  100 · £2 = £200",
                "outlay:  £60 + £40 = £100",
                "ordinary profit:  10% of £100 = £10",
                "rent:  £200 − £100 − £10 = £90",
                "poor farm:  55 · £2 − £110 = £0",
            ],
            "after": [
                "Run the poor farm's line on its own: 55 quarters at £2 are £110, exactly "
                "what the outlay and ordinary profit come to. It pays its way and no more, "
                "and the landlord has nothing to take. Lower the price to £3/2 and the same "
                "line gives £82.50 − £110, a loss of £27.50.",
            ],
        },
        "quiz_title": "Rent as what is left over",
        "quiz": [
            {"q": "A farm yields 120 quarters of corn, which sell at £2 a quarter. Wages "
                  "are £80, other stock is £60, and ordinary profit is 10% of the outlay. "
                  "What is the rent?",
             "a": ["£100", "£86", "£154", "£160"],
             "c": 1,
             "why": "The produce is worth `120 · 2 = 240`. The outlay is `80 + 60 = 140` and "
                    "its ordinary profit is 14, so the tenant must keep 154, and the rent is "
                    "`240 − 154 = 86`. £100 forgets the ordinary profit, £154 is what the "
                    "tenant keeps, and £160 takes off the wages alone."},
            {"q": "On Smith's account, which way does the causation run between the price "
                  "of a commodity and the rent of the land that produces it?",
             "a": ["A high price makes the rent high",
                   "A high rent makes the price high",
                   "Rent and price are fixed one independently of the other",
                   "Rent is the landlord's costs, and is added to the price"],
             "c": 0,
             "why": "The chapter says high or low rent is &ldquo;the effect&rdquo; of a high or "
                    "low price, where wages and profit are the causes. The second answer "
                    "reverses it. The third and fourth are not Smith's: rent is neither "
                    "independent of price nor a cost added on to it."},
            {"q": "Why does Smith bring in kelp, a seaweed that grows on tidal rocks?",
             "a": ["To show that rent is always paid in kind",
                   "To show that landlords never improve their land",
                   "To show that rent is demanded even for what no improvement made, so it "
                   "is not simply a return on the landlord's outlay",
                   "To show that fishing is more profitable than farming"],
             "c": 2,
             "why": "Kelp rocks are &ldquo;incapable of human improvements&rdquo;, so a rent "
                    "paid for them cannot be interest on improving expense. The first two "
                    "are not claims the passage makes, and the fish belong to the Shetland "
                    "example, not to kelp."},
            {"q": "In the lab's first preset corn falls from £2 to £3/2 a quarter. What is "
                  "the middle farm's rent at the lower price?",
             "a": ["£50", "£40", "£0", "£10"],
             "c": 3,
             "why": "The middle farm yields 80 quarters, worth `80 · 3/2 = 120`, and it "
                    "must keep £110 for outlay and ordinary profit, so the rent is £10. "
                    "£50 was its rent at £2, £40 is the north farm's rent at the lower "
                    "price, and £0 is the poor farm's, which at the lower price "
                    "cannot cover its outlay at all."},
        ],
        "mistakes": [
            ("Thinking rent is a cost that raises the price of corn",
             "Wages and profit are costs that must be paid to bring corn to market, and "
             "Smith lets them fix a lowest price. Rent works the other way round. In the "
             "second preset the price falls by a quarter and the total rent falls from £140 "
             "to £50, while the outlay is unchanged. The landlord's share is what the "
             "price leaves, not a charge the price must cover."),
            ("Reading rent as interest on the landlord's improvements",
             "Smith grants that some rent may be that. He answers that it cannot be "
             "more than partly, because the landlord asks a rent for unimproved land, "
             "and for kelp shores that no one improved. The rent is fixed by what the "
             "tenant can afford, whatever the landlord spent."),
            ("Taking a monopoly price to mean the tenant is squeezed below ordinary "
             "profit",
             "In Smith's account the tenant keeps his ordinary profit; the landlord "
             "seldom means to leave him more, and the tenant will not accept less. The "
             "&ldquo;monopoly&rdquo; is the landlord's control of the land, which makes "
             "the whole surplus above that profit his. It does not push the tenant "
             "into a loss."),
        ],
        "standard": (
            "Finish when you can find a farm's rent and say what moves it.",
            "Given a farm's output, wages, stock, the ordinary rate of profit and the "
            "price of the produce, compute its rent, say at what price it would afford "
            "none, and say whether a rise in wages or a fall in price is the cause "
            "of the change in rent.",
        ),
        "note": (
            "The lab is Smith's definition and nothing else: it cannot say whether the "
            "price of corn is set by the landlords, by demand or by the poorest land in "
            "use, which is exactly what Smith and Ricardo disagree about. It also takes "
            "the ordinary rate of profit as given, though Smith's own account of how it "
            "is set is in Chapters 6 to 9. The three farms are written for the lesson, "
            "not taken from any estate."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 4813-4829 (food always affords rent); l. 4840-4855 (fertility and
    # situation); l. 4856-4870 (roads); l. 4917-4920 (bread and butcher's meat);
    # l. 4914-4916 (Highland cattle); l. 5271-5283 (rice and potatoes); l. 5296-5316
    # (potatoes); l. 5221 (Cochin China sugar).
    {
        "slug": "produce-which-always-affords-rent",
        "title": "Produce Which Always Affords Rent",
        "module": "Book I, Chapter 11, Part 1 · Of the Produce of Land which always affords Rent",
        "one_line": "Food always leaves a surplus over the labour that raises it, so it always affords rent, and the rent of food land sets the rent of most other land.",
        "summary": (
            "Smith's first class of rude produce is food, and the reason he gives is "
            "about people: where there is food, there is somebody to work for it. Work "
            "out how fertility and distance from the town change a farm's rent, how a "
            "road puts a distant farm nearer the market, and what an acre of potatoes "
            "would do to rent if potatoes were the staple, then follow the rent of "
            "corn land into pasture, gardens, vineyards, sugar and tobacco."
        ),
        "key": [
            "food: always a surplus over its own labour",
            "rent rises with fertility and nearness",
            "a road: carriage falls, remote rent rises",
            "common food land sets the rent of the rest",
            "scarce land for a crop can earn far more",
        ],
        "key_label": "Why food always affords rent",
        "concepts_intro": (
            "Part I is a long walk through a dozen crops, and a first reading can "
            "lose the thread. There are three ideas holding it together."
        ),
        "concepts": [
            ("Food always affords rent",
             "Men multiply in proportion to their means of subsistence, so food is always "
             "in demand and can always command labour. Land in almost any situation "
             "yields more food than the labour that raises it eats, so something "
             "always remains for the landlord."),
            ("Fertility and situation",
             "Rent rises with the goodness of the land, and falls with the cost of "
             "carrying the produce to market. Smith says good roads, canals and "
             "navigable rivers are therefore &ldquo;the greatest of all "
             "improvements&rdquo;."),
            ("The rent of food land regulates the rest",
             "Pasture, kitchen gardens, vineyards, sugar, rice and tobacco earn "
             "rents that cluster around the rent of corn, because land would be turned "
             "from one to another until they did. The exception is a crop whose land is "
             "so scarce that buyers outbid one another for it."),
        ],
        "read_title": "Food, then fertility and distance, then the other crops",
        "read_intro": (
            "Part I opens quickly and slows down. Read the first four pages for the "
            "argument, then treat the rest as examples of it."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 11, Part 1.</strong> &ldquo;As men, like all "
                  "other animals, naturally multiply in proportion to the means of their "
                  "subsistence, food is always more or less in demand. It can always "
                  "purchase or command a greater or smaller quantity of labour, and "
                  "somebody can always be found who is willing to do something in order "
                  "to obtain it.&rdquo; Land, Smith goes on, &ldquo;in almost any "
                  "situation, produces a greater quantity of food than what is "
                  "sufficient to maintain all the labour necessary for bringing it to "
                  "market, in the most liberal way in which that labour is ever "
                  "maintained&rdquo;. So something always remains for the landlord."),
            ("p", "The reasoning has two halves, and Malthus, who published his "
                  "<em>Essay on the Principle of Population</em> in 1798, after Smith's "
                  "death, took the first half and built a book on it. The second half "
                  "is the claim to test. A farm that feeds the people who work it, "
                  "and has enough left over to replace the seed and give the farmer "
                  "his ordinary profit, has a surplus beyond that, and Smith expects "
                  "that surplus to be positive on any soil that anyone troubles to "
                  "farm. Even the &ldquo;most desert moors in Norway and "
                  "Scotland&rdquo;, with pasture for cattle, pay the owner some small "
                  "rent."),
            ("p", "Then two things that make the rent larger or smaller. The first is "
                  "fertility: &ldquo;The rent increases in proportion to the goodness "
                  "of the pasture&rdquo;. The second is situation, &ldquo;whatever be its "
                  "fertility&rdquo;. Land beside a town rents higher than equally "
                  "fertile land far away, because the distant produce costs more to "
                  "carry to market, so more labour has to be maintained out of it and "
                  "the surplus is smaller. Smith adds a refinement: in remote parts "
                  "the rate of profit is higher, so a smaller share of that "
                  "diminished surplus can belong to the landlord."),
            ("p", "The lab shows the first effect with two farms of the same "
                  "fertility, each yielding 100 quarters, written for this lesson. "
                  "The nearer pays £50 in wages and £30 in other stock; the distant "
                  "one pays £70 in wages, the extra £20 being the carriers, and £30 in "
                  "stock. At £2 a quarter and 10% ordinary profit, in the "
                  "town-and-distant preset, the near farm's rent is £200 − "
                  "£88 = £112 and the distant one's is £200 − £110 = £90. The lab "
                  "uses one rate of profit for every farm, so it leaves out Smith's "
                  "refinement and the gap it shows is, on his account, the smaller of "
                  "the two possible."),
            ("p", "Good roads change that. Smith's praise of them is strong: they "
                  "&ldquo;put the remote parts of the country more nearly upon a level "
                  "with those in the neighbourhood of the town. They are upon that "
                  "account the greatest of all improvements.&rdquo; They help the town "
                  "by breaking the monopoly of the neighbouring country, and they help "
                  "even that country, which loses a market but gains many new ones. "
                  "Smith adds a small piece of history. Not fifty years earlier, some "
                  "counties near London had petitioned Parliament against extending the "
                  "turnpike roads, fearing that cheap labour in the remoter counties "
                  "would undersell them; their rents, he says, had risen since. In the "
                  "after-the-road preset the carriers' wages fall from £20 "
                  "to £5, the distant farm's wages go from £70 to £55 and its rent "
                  "rises from £90 to £106.50. The lab holds the price of corn fixed, "
                  "which Smith would not: a road also lets distant corn into the old "
                  "market, and the lab cannot show the rent that costs the farms "
                  "near the town."),
            ("p", "Now compare crops. A corn field of moderate fertility, Smith says, "
                  "&ldquo;produces a much greater quantity of food for man, than the "
                  "best pasture of equal extent&rdquo;, and the surplus after seed "
                  "and labour is greater too. In the rude beginnings of agriculture "
                  "that made corn land the better rent. But &ldquo;the relative values "
                  "of those two different species of food, bread and butcher's meat, "
                  "are very different in the different periods of agriculture&rdquo;: "
                  "where wild land abounds there is more meat than bread, and bread "
                  "dearer. As tillage spreads the competition changes direction. In "
                  "most of Britain, he reports, a pound of the best butcher's meat is "
                  "worth more than two pounds of the best white bread, and sometimes "
                  "three or four. The two rents are then kept level by the movement "
                  "of land between them: &ldquo;If it was more than compensated, more "
                  "corn-land would be turned into pasture; and if it was not "
                  "compensated, part of what was in pasture would be brought back into "
                  "corn.&rdquo;"),
            ("p", "The same test is put to hop gardens, fruit and kitchen gardens and "
                  "vineyards, which need more expense at the start or each year and so "
                  "pay a greater rent and a greater profit, but &ldquo;seldom&rdquo; "
                  "more than &ldquo;a reasonable interest or compensation for this "
                  "superior expense&rdquo;. Smith spends several pages on the ancient "
                  "writers, Columella, Democritus, Cato and Varro, to show that the "
                  "arguments about whether to plant a vineyard are old, and that "
                  "comparisons between the profit and expense of new projects are, in his "
                  "words, &ldquo;commonly very fallacious&rdquo;."),
            ("p", "The exception is a crop whose land is too small for the demand. "
                  "Then the whole produce can be sold to buyers willing to give more "
                  "than the ordinary price, and the surplus &ldquo;may exceed it in "
                  "almost any degree&rdquo;, most of it going to the landlord. His "
                  "examples are the few vineyards whose wine has a flavour found "
                  "nowhere else, and the sugar islands. In Cochin China, he reports "
                  "from Poivre, the finest white sugar sells for about eight shillings "
                  "the hundredweight, &ldquo;not a fourth part of what is commonly paid "
                  "for the brown or muscovada sugars imported from our colonies&rdquo;. "
                  "Tobacco he treats as the smaller case of the same thing. He is "
                  "not praising the arrangement: he calls the prohibition of tobacco "
                  "growing in most of Europe &ldquo;most absurdly&rdquo; made, and, of the "
                  "report that planters burn tobacco to hold the price, which he "
                  "doubts, he says that if &ldquo;such violent methods are necessary&rdquo; the "
                  "advantage will not last."),
            ("p", "Last come rice and potatoes, and here Smith asks what would happen "
                  "to rent if the common food of a country were a plant that yielded far "
                  "more food from an acre. His answer, in effect, is that the surplus "
                  "after feeding the labourers would be much greater, and with it, as Smith puts it, &ldquo;The real value of his rent, his real "
                  "power and authority&rdquo;. "
                  "Rice gives two crops a year of thirty to sixty bushels each, he says. "
                  "On potatoes, &ldquo;Twelve thousand weight of potatoes from an acre "
                  "of land is not a greater produce than two thousand weight of "
                  "wheat&rdquo;, but allowing half the weight of the root for water, the "
                  "acre of potatoes still gives six thousand weight of solid "
                  "nourishment, &ldquo;three times the quantity produced by the acre of "
                  "wheat&rdquo;. In the wheat-and-potatoes preset the "
                  "outputs are Smith's, and everything else is written for the lesson. "
                  "A pound of solid food is valued at a penny, or £1/100 for the "
                  "lab. The wheat acre yields 2,000 lb, worth £20, with £7 in wages and "
                  "£5 in stock; the potato acre yields 6,000 lb, worth £60, with £6 in "
                  "wages and £4 in stock. At 10% ordinary profit the wheat acre's rent "
                  "is £20 − £13.20 = £6.80 and the potato acre's is £60 − £11 = £49. "
                  "That is the sense of Smith's remark that under potatoes &ldquo;rents "
                  "would rise much beyond what they are at present&rdquo;."),
            ("p", "The passage is also candid about the obstacle: &ldquo;It is difficult to preserve potatoes through the year, and "
                  "impossible to store them like corn, for two or three years "
                  "together&rdquo;. A reader "
                  "who knows that Ireland, which Smith mentions as a potato country, "
                  "suffered the famine of the 1840s knows what a country puts at "
                  "stake when its cheapest food cannot be kept. Smith did not "
                  "foresee that, and nothing in the lab can."),
            ("p", "The next lesson, <em>Produce Which Sometimes Affords Rent</em>, "
                  "turns from the food that always affords rent to the materials of "
                  "clothing and lodging and the mines, where the answer is "
                  "&ldquo;sometimes&rdquo;."),
        ],
        "lab": ("wonkit", {
            "mode": "rent",
            "view": "residual",
            "money_unit": "£",
            "preset": "town-and-distant",
            "presets": [
                {"id": "town-and-distant", "label": "Two equally fertile farms, one near the town and one far, written for this lesson",
                 "lands": "near-town, 100, 50, 30; distant, 100, 70, 30",
                 "price": "2", "rate": "10", "expect": {"wreRent": "near-town £112; distant £90", "wreTotal": "£202"}},
                {"id": "after-the-road", "label": "The same farms once the road has cut the carriers' wages",
                 "lands": "near-town, 100, 50, 30; distant, 100, 55, 30",
                 "price": "2", "rate": "10", "expect": {"wreRent": "near-town £112; distant £106.50", "wreTotal": "£218.50"}},
                {"id": "wheat-and-potatoes", "label": "An acre of wheat and an acre of potatoes, outputs in pounds of solid food from Smith, the costs written for this lesson",
                 "lands": "wheat-acre, 2000, 7, 5; potato-acre, 6000, 6, 4",
                 "price": "1/100", "rate": "10", "expect": {"wreRent": "wheat-acre £6.80; potato-acre £49", "wreTotal": "£55.80"}},
            ],
            "panel_title": "Fertility, distance and the staple",
            "panel_intro": (
                "The same lab as before, with different farms. In the first two presets "
                "carriage shows up as wages; in the third each land's output is a year's "
                "solid food in pounds weight, and the price is a penny a pound, which "
                "the lab writes as £1/100."
            ),
        }),
        "steps_title": "Comparing two lands",
        "steps_intro": "Four steps for any pair of fields, farms or crops.",
        "steps": [
            ("Put both on one price",
             "Value each land's output at the same price per unit, so that the "
             "comparison is about the land and not about a market."),
            ("Put carriage into the outlay",
             "A distant farm's produce costs more to bring to market. Count that as "
             "extra wages or stock on the distant farm, as Smith does when he speaks "
             "of the labour that must be maintained out of the produce."),
            ("Take off outlay and ordinary profit",
             "Each land's rent is its produce's value less its outlay and the "
             "ordinary profit on it. Lands where this is zero or negative afford no "
             "rent."),
            ("Compare and ask what moved",
             "Set the rents side by side and ask whether fertility, situation or the "
             "price moved them. A road changes situation; a new staple changes "
             "fertility, in the sense of food per acre."),
        ],
        "worked": {
            "title": "Why the road helps the distant farm",
            "intro": [
                "Take the first preset. Both farms yield 100 quarters at £2 a quarter "
                "and ordinary profit is 10%. The near farm pays £50 in wages and £30 in "
                "stock; the distant one pays £70 and £30, the extra £20 being carriage.",
            ],
            "lines": [
                "near:  200 − 1.1 · (50 + 30) = £112",
                "distant:  200 − 1.1 · (70 + 30) = £90",
                "after the road:  200 − 1.1 · (55 + 30) = £106.50",
            ],
            "after": [
                "The road saves £15 of carriage and the distant farm's rent rises by "
                "£16.50, a little more than the saving, because ordinary profit is "
                "charged on the outlay and the outlay is smaller. That is the "
                "arithmetic of Smith's remark that roads &ldquo;encourage the cultivation "
                "of the remote&rdquo;.",
            ],
        },
        "quiz_title": "Fertility, distance and food",
        "quiz": [
            {"q": "In the lab's first preset the distant farm's wages are £20 higher than "
                  "the near farm's, because of carriage. With corn at £2, ordinary profit "
                  "10% and both farms yielding 100 quarters, how much less rent does the "
                  "distant farm pay?",
             "a": ["£20", "£22", "£12", "£2"],
             "c": 1,
             "why": "The extra £20 of wages carries 10% ordinary profit, so the outlay "
                    "plus profit is £22 higher and the rent is £22 lower: £112 against £90. "
                    "£20 forgets the profit on the extra outlay."},
            {"q": "Why, on Smith's account, does food always afford some rent?",
             "a": ["Because landlords can always demand it by law",
                   "Because food is a scarce crop whose land is limited",
                   "Because a rise in wages always raises the price of food",
                   "Because land yields more food than the labour that raises it needs, "
                   "and food always finds people willing to work to get it"],
             "c": 3,
             "why": "The argument is that men multiply with their food, so food always "
                    "commands labour, and that land in almost any situation yields a surplus "
                    "over the labour's keep. The scarcity answer is Smith's account of the "
                    "crops that earn more than the common rent, not of food in general."},
            {"q": "A vineyard has a flavour that no other land can match, and the whole "
                  "crop sells above the ordinary price of wine. Where does Smith say "
                  "most of the extra goes?",
             "a": ["To the farmer, who works harder",
                   "To the wine merchants",
                   "To the landlord, as rent",
                   "To the labourers, as higher wages"],
             "c": 2,
             "why": "Smith says the greater part of the excess &ldquo;naturally goes to the "
                    "rent of the landlord&rdquo;. The high price causes the careful "
                    "cultivation, not the other way round, so only a small part is needed to "
                    "pay for the extra labour and stock."},
            {"q": "What obstacle does Smith name to potatoes ever becoming a country's "
                  "principal food, as bread is?",
             "a": ["They are difficult to keep through the year and cannot be stored for "
                   "years, as corn can",
                   "Potatoes need more labour than wheat",
                   "Potatoes are not nourishing",
                   "They cost more than rice"],
             "c": 0,
             "why": "Smith says the fear of not being able to sell potatoes before they "
                    "rot discourages their cultivation. He says an acre of potatoes needs "
                    "less expense than an acre of wheat and that the food is nourishing, so "
                    "the other three answers are wrong."},
        ],
        "mistakes": [
            ("Thinking all produce affords rent, because food does",
             "Smith claims it for food alone: human food &ldquo;always and necessarily "
             "affords some rent&rdquo;, and other produce only sometimes. The next lesson is "
             "about the rest. A produce affords rent only while its price is above its "
             "outlay and ordinary profit."),
            ("Treating a distant farm's lower rent as lower fertility",
             "In the first preset both farms yield 100 quarters, so the land is "
             "equally fertile, yet the distant farm pays £22 less. Situation alone "
             "changes the rent, through the cost of carrying the produce to market."),
            ("Supposing a rare crop's rent is set by its own costs",
             "Where the land fit for a crop is too small for the demand, the produce "
             "sells above the price that would repay outlay and ordinary profit, and "
             "most of the excess goes to the landlord. The rent is then fixed by how "
             "eagerly buyers compete, not by what the crop costs to grow."),
        ],
        "standard": (
            "Finish when you can say why one land pays more rent than another.",
            "Given two lands' outputs, outlays and the price of the produce, compute "
            "each rent and say whether fertility or situation explains the difference, "
            "and say why the rent of corn land governs the rent of most other crops.",
        ),
        "note": (
            "The lab uses one price and one rate of profit for every land, so it shows "
            "the effect of carriage on a single market's rent but not the changes in "
            "price that a road brings, or Smith's remark that profit is higher in remote "
            "parts. Smith's figures on the yield of rice and potatoes are reports and "
            "estimates, and his comparison of oatmeal and wheat-bread diets is "
            "about a rank of people, not a measured trial. The farms and costs here are "
            "written for the lesson."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 5336-5342 (the second class); l. 5400-5420 (coal mines that pay no
    # rent); l. 5440-5465 (the most fertile coal mine regulates the price); l. 5466-5475
    # (a fifth, a tenth, years' purchase); l. 5505-5530 (Cornwall and Peru, thirteen to
    # twelve); l. 5594-5602 (price of the precious metals).
    {
        "slug": "produce-which-sometimes-affords-rent",
        "title": "Produce Which Sometimes Affords Rent",
        "module": "Book I, Chapter 11, Part 2 · Of the Produce of Land which sometimes does, and sometimes does not, afford Rent",
        "one_line": "Clothing, lodging and the minerals afford a rent only where demand is strong and the mine or quarry is good, and the most fertile mine sets the price for the rest.",
        "summary": (
            "Smith's second class is the produce of land that is not food: skins and "
            "wool, timber and stone, coal, metals and precious stones. They pay rent only "
            "when the demand is rich enough. Work out which of four coal mines can pay "
            "any rent at one price and which at a lower one, and then follow Smith's "
            "own shares of the gross produce, a tenth of a coal mine, a sixth of a tin "
            "mine, a fifth of a Peruvian silver mine, through the thirteen to twelve "
            "he finds between Cornwall and Peru."
        ),
        "key": [
            "food is first: other produce follows it",
            "a mine's rent depends on fertility and site",
            "the best mine near sets the price of coals",
            "metals sell far off: one price at all mines",
            "rent: a tenth of coal, a sixth of tin",
        ],
        "key_label": "When land that is not food pays rent",
        "concepts_intro": (
            "Part II is shorter than Part I and more tightly argued. It has one claim "
            "about why the second class exists at all, one about coal, and one about "
            "metals."
        ),
        "concepts": [
            ("Clothing and lodging come after food",
             "Land in its rude state yields materials for clothing and lodging for "
             "many more people than it can feed, so they are often worth only the "
             "labour of fitting them for use. Once cultivation lets half of a society "
             "work at something other than food, there is a demand for them and "
             "they may afford a rent."),
            ("The best mine regulates the price",
             "A coal mine's rent depends on its fertility and its situation. Where "
             "many mines sell in one market, Smith says &ldquo;The most fertile coal mine, too, "
             "regulates the price of coals at all the other mines&rdquo; near it, and the rest "
             "may fall to no rent or be abandoned."),
            ("Metals are priced by the world's best mine",
             "Metals bear carriage so well that mines on different continents compete. "
             "The price at the most fertile mine in the world therefore affects every "
             "other, and rent is a small share of the price of the precious metals and "
             "of stones."),
        ],
        "read_title": "Clothing and lodging, then coal, then the metals",
        "read_intro": (
            "Part II opens with a short argument about why the second class of produce "
            "exists, and then spends most of its length on mines. Smith's own "
            "figures turn up in the last third."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 11, Part 2.</strong> &ldquo;Human food seems to "
                  "be the only produce of land, which always and necessarily affords "
                  "some rent to the landlord. Other sorts of produce sometimes may, and "
                  "sometimes may not, according to different circumstances.&rdquo; "
                  "The first of the other sorts is the materials of clothing and "
                  "lodging, and Smith's argument about them is a story about stages of "
                  "society."),
            ("p", "In its rude state, land can supply materials for clothing and "
                  "lodging &ldquo;to a much greater number of people than it can "
                  "feed&rdquo;. The skins of the larger animals were the original "
                  "clothing, and the hunter who provides himself with food provides "
                  "himself with &ldquo;the materials of more clothing than he can "
                  "wear&rdquo;. A great part is thrown away. They are worth, at the "
                  "most, the labour of fitting them for use, and afford no rent. It "
                  "takes foreign commerce to give them a price above that: the "
                  "Highlanders' hides, Flemish buyers for English wool, the "
                  "paving of London's streets which enabled owners of barren rocks "
                  "on the coast of Scotland to draw a rent from what never afforded "
                  "any before."),
            ("p", "Then comes an argument that Smith evidently likes. Populous "
                  "countries are such &ldquo;not in proportion to the number of people "
                  "whom their produce can clothe and lodge, but in proportion to that of "
                  "those whom it can feed&rdquo;. Among savage nations, he says, a "
                  "hundredth part of the year's labour provides clothing and lodging, "
                  "and ninety-nine parts are needed for food. Once cultivation lets "
                  "the labour of one family feed two, half of society is free to make "
                  "other things. The rich man consumes no more food than his poor "
                  "neighbour, but compare &ldquo;the spacious palace and great "
                  "wardrobe of the one&rdquo; with the hovel and rags of the other. "
                  "&ldquo;The desire of food is limited in every man by the narrow "
                  "capacity of the human stomach&rdquo;, and the desire for conveniences "
                  "and ornaments of building, dress and furniture &ldquo;seems to have "
                  "no limit or certain boundary&rdquo;. So from the improvement of land "
                  "in producing food comes a demand for every material that human "
                  "invention can use, &ldquo;for the fossils and minerals contained in "
                  "the bowels of the earth, the precious metals, and the precious "
                  "stones&rdquo;."),
            ("p", "That is a claim about why the second class exists, and it is worth "
                  "pausing on, because it makes every rent in this part a rent that "
                  "food has made possible. But the demand does not always come, and "
                  "Smith takes coal as his case. A mine, he says, is fertile or barren "
                  "according to whether a given quantity of labour brings out more or "
                  "less mineral than from most mines of the same kind. Some coal "
                  "mines cannot be worked because they are barren, &ldquo;They can "
                  "afford neither profit nor rent&rdquo;. Some produce just enough to "
                  "pay the labour and replace the stock with ordinary profits, and "
                  "&ldquo;They afford some profit to the undertaker of the work, but "
                  "no rent to the landlord&rdquo;, so the landlord works them himself or "
                  "leaves them. Others are fertile but badly placed, in a thinly "
                  "inhabited inland country without roads or water-carriage, and "
                  "the coal could not be sold."),
            ("p", "The most important sentence of the part follows: &ldquo;The most "
                  "fertile coal mine, too, regulates the price of coals at all the other "
                  "mines in its neighbourhood. Both the proprietor and the undertaker of "
                  "the work find, the one that he can get a greater rent, the other that "
                  "he can get a greater profit, by somewhat underselling all their "
                  "neighbours. Their neighbours are soon obliged to sell at the same "
                  "price, though they cannot so well afford it, and though it always "
                  "diminishes, and sometimes takes away altogether, both their rent and "
                  "their profit.&rdquo; Note the order of cause again: the price is set "
                  "where the best mine can profit by setting it, and the lesser mines "
                  "take it. A reader who knows Ricardo will recognise something in "
                  "this, since his rent is the surplus of better land over the poorest "
                  "in use. Smith states it here for coal; for corn land, in the previous "
                  "part, he reasons from the demand for food and does not name the "
                  "poorest land as the regulator. Capital's "
                  "<em>Differential Rent I</em> gives the later arithmetic of rent "
                  "by grade of land."),
            ("p", "The lab has four coal mines, written for the lesson, with every mine "
                  "paying £60 in wages and £40 in stock except the barren one, which "
                  "pays £70 and £50. Ordinary profit is 10%, so the outlay and profit "
                  "come to £110 at three mines and £132 at the barren one. At £1 a "
                  "ton, in the four-coal-mines preset, the barren mine "
                  "(100 tons) is worth £100 and makes a loss of £32. A second mine "
                  "(110 tons) is worth exactly £110, so it pays its way and no more, "
                  "and only its owner can profitably work it. The middling mine (150 "
                  "tons) pays a rent of £40, and the fertile mine (200 tons) pays "
                  "£90. Total rent is £130. Now let the fertile mine undersell, "
                  "bringing the price to £3/4 a ton, in the fertile-undersells "
                  "preset. The middling mine's rent shrinks to £2.50 and the fertile "
                  "mine's to £40; the second mine now loses £27.50 and the barren "
                  "mine £57. Rent has dropped from £130 to £42.50, and two mines are "
                  "worked at a loss."),
            ("p", "Smith gives a rule of thumb for how large a share rent is. &ldquo;The "
                  "rent of an estate above ground, commonly amounts to what is supposed "
                  "to be a third of the gross produce&rdquo;, and is generally certain. "
                  "&ldquo;In coal mines, a fifth of the gross produce is a very great "
                  "rent, a tenth the common rent&rdquo;, and it is seldom certain. The "
                  "consequence shows in the price of the property: in a country where "
                  "thirty years' purchase is a moderate price for an estate, ten years' "
                  "purchase is a good price for a coal mine."),
            ("p", "Metals differ in a way that matters. The coarse and still more the "
                  "precious metals &ldquo;are so valuable, that they can generally bear "
                  "the expense of a very long land, and of the most distant sea "
                  "carriage&rdquo;. So mines far apart compete: &ldquo;The price of "
                  "silver in Peru ... must have some influence on its price, not only "
                  "at the silver mines of Europe, but at those of China.&rdquo; After "
                  "the Peruvian mines were found, most of Europe's own silver mines were "
                  "abandoned. Rent at most mines can therefore be only a small share of "
                  "the price, and &ldquo;Labour and profit make up the greater part of "
                  "both&rdquo;."),
            ("p", "Here Smith's own figures come in, and the lab's third preset puts "
                  "them in a table. He is told that &ldquo;A sixth part of the gross "
                  "produce may be reckoned the average rent of the tin mines of "
                  "Cornwall&rdquo;, and that the rent of several fertile lead mines in "
                  "Scotland is the same. Until 1736 the Spanish crown's tax on Peruvian "
                  "silver was a fifth, &ldquo;which till then might be considered as the "
                  "real rent of the greater part of the silver mines of Peru&rdquo;, and "
                  "the Duke of Cornwall's tax on tin is about a twentieth. Add the "
                  "twentieth to the sixth and the Cornwall rent is 13/60 of the "
                  "produce against 12/60 for Peru: &ldquo;as thirteen to twelve&rdquo;. "
                  "The smith-shares preset builds each of his shares into a "
                  "land of 660 pounds' worth of produce at £1 for each pound's worth, "
                  "at 10% ordinary profit. The estate's share of a third is rent of "
                  "£220, the coal mine's tenth is £66, the tin mine's sixth is £110 and "
                  "the silver mine's fifth is £132. The shares are Smith's. The "
                  "outlays that give them are written for the lesson."),
            ("p", "Of the precious stones Smith says that wages and profit make up "
                  "almost the whole of the high price, and rent comes in for a very "
                  "small share, &ldquo;frequently for no share; and the most fertile "
                  "mines only afford any considerable rent&rdquo;. He quotes Tavernier "
                  "on the sovereign of Golconda, who ordered all but the mines yielding "
                  "the finest stones shut, the other mines being &ldquo;to the "
                  "proprietor not worth the working&rdquo;. And a point with a modern "
                  "ring: rent depends on a mine's superiority over others, not on its "
                  "absolute fertility. If new mines far more fertile than Potosi were "
                  "found, even Potosi might not be worth working. Estates above "
                  "ground are different, since the value of the most barren land "
                  "&ldquo;is not diminished by the neighbourhood of the most "
                  "fertile&rdquo;; the people the fertile land maintains give it "
                  "a market."),
            ("p", "The part ends with the poor inhabitants of Cuba and Santo Domingo, who wore "
                  "bits of gold in their hair like pebbles worth picking up, and were "
                  "astonished at the Spaniards' rage for them, having &ldquo;no "
                  "notion that there could anywhere be a country in which many people "
                  "had the disposal of so great a superfluity of food&rdquo;. The next "
                  "lesson, <em>The Value of Silver over Four Centuries</em>, takes up "
                  "silver itself, and asks what its price in corn says about it."),
        ],
        "lab": ("wonkit", {
            "mode": "rent",
            "view": "residual",
            "money_unit": "£",
            "preset": "four-coal-mines",
            "presets": [
                {"id": "four-coal-mines", "label": "Four coal mines at £1 a ton, written for this lesson",
                 "lands": "barren-mine, 100, 70, 50; own-work-mine, 110, 60, 40; middling-mine, 150, 60, 40; fertile-mine, 200, 60, 40",
                 "price": "1", "rate": "10", "expect": {"wreRent": "barren-mine no rent (a loss of £32); own-work-mine no rent (nothing left); middling-mine £40; fertile-mine £90", "wreTotal": "£130"}},
                {"id": "fertile-undersells", "label": "The fertile mine undersells and the price falls to £3/4 a ton",
                 "lands": "barren-mine, 100, 70, 50; own-work-mine, 110, 60, 40; middling-mine, 150, 60, 40; fertile-mine, 200, 60, 40",
                 "price": "3/4", "rate": "10", "expect": {"wreRent": "barren-mine no rent (a loss of £57); own-work-mine no rent (a loss of £27.50); middling-mine £2.50; fertile-mine £40", "wreTotal": "£42.50"}},
                {"id": "smith-shares", "label": "Smith's shares of the gross produce: a third, a tenth, a sixth and a fifth (the outlays are written for this lesson)",
                 "lands": "estate-above-ground, 660, 240, 160; coal-mine, 660, 360, 180; cornwall-tin-mine, 660, 300, 200; peru-silver-mine, 660, 300, 180",
                 "price": "1", "rate": "10", "expect": {"wreRent": "estate-above-ground £220; coal-mine £66; cornwall-tin-mine £110; peru-silver-mine £132", "wreTotal": "£528"}},
            ],
            "panel_title": "Which mines pay a rent",
            "panel_intro": (
                "Four mines, one market. In the third preset every land's output is a "
                "year's produce counted in pounds' worth, so the price of a pound's "
                "worth is £1, and each outlay is chosen so that the rent comes out at "
                "the share Smith names."
            ),
        }),
        "steps_title": "Telling whether a mine can pay a rent",
        "steps_intro": "Four steps, taken mine by mine.",
        "steps": [
            ("Find each mine's lowest price",
             "Divide outlay plus ordinary profit by the year's output. This is the "
             "lowest price at which the mine just pays its way, the one Smith "
             "describes as barely enough to replace the stock employed together with "
             "its ordinary profits."),
            ("Compare it with the market price",
             "A mine whose lowest price is above the market price loses money and "
             "cannot be worked. One whose lowest price equals it pays no rent. Only "
             "a mine whose lowest price is below it can afford a rent."),
            ("Take the best mine's price",
             "If one mine can sell below the rest and still profit, the others must "
             "follow. Set the market price at what the best mine will take and "
             "repeat the comparison."),
            ("Compute the rents",
             "For each mine still working, the rent is output times price less outlay "
             "and ordinary profit. Add them for the total, and divide by the gross "
             "produce for the share."),
        ],
        "worked": {
            "title": "Thirteen to twelve",
            "intro": [
                "Smith's comparison of Cornwall tin and Peruvian silver needs only "
                "fractions. A sixth of the gross produce is the tin mines' rent, a "
                "twentieth is the Duke of Cornwall's tax, which would belong to the "
                "owner but for the duty, and a fifth was the Spanish tax on silver.",
            ],
            "lines": [
                "tin:  1/6 + 1/20 = 10/60 + 3/60 = 13/60",
                "silver:  1/5 = 12/60",
                "13/60 : 12/60 = 13 : 12",
            ],
            "after": [
                "So the whole average rent of the Cornish tin mines was to that of the "
                "Peruvian silver mines as thirteen to twelve, and Smith adds that this "
                "makes rent a greater part of the price of tin than of silver, since "
                "once the stock and its ordinary profits are replaced the residue is "
                "greater in the coarse metal. The Peruvian mines, "
                "he says, can no longer pay even a fifth, and the tax was cut to a tenth "
                "in 1736.",
            ],
        },
        "quiz_title": "Mines and the price of coal",
        "quiz": [
            {"q": "In the lab's first preset, which mine can be worked only by its "
                  "landlord, who gets ordinary profit and no rent?",
             "a": ["The barren mine", "The own-work mine", "The middling mine", "The fertile mine"],
             "c": 1,
             "why": "At £1 a ton the own-work mine's 110 tons are worth £110, exactly the "
                    "outlay and ordinary profit, so there is nothing for a landlord who "
                    "lets it. The barren mine loses £32, and the other two pay £40 and "
                    "£90 in rent."},
            {"q": "What does Smith say happens to the price of coal when the most "
                  "fertile mine in a neighbourhood undersells the others?",
             "a": ["The other mines hold their price and lose their customers",
                   "The landlords of the other mines raise their rents",
                   "The price of coal rises to the price of wood",
                   "The other mines are soon obliged to sell at the same price, which "
                   "diminishes and sometimes takes away their rent and profit"],
             "c": 3,
             "why": "The passage says &ldquo;Their neighbours are soon obliged to sell at the same "
                    "price&rdquo;. It does not say they hold their price, and the "
                    "price of wood is the ceiling, not what the undercutting does."},
            {"q": "Smith says the tin mines' rent is a sixth of the gross produce plus "
                  "a twentieth that goes to the Duke of Cornwall, and the Peruvian "
                  "silver mines' rent is a fifth. What is the ratio of the first to the "
                  "second?",
             "a": ["13 to 12", "5 to 6", "31 to 30", "7 to 6"],
             "c": 0,
             "why": "`1/6 + 1/20 = 13/60` and `1/5 = 12/60`, so 13 to 12. 5 to 6 is the "
                    "sixth against the fifth, leaving out the Duke's twentieth, and the "
                    "other two are not ratios the sums give."},
            {"q": "On Smith's account, why is rent a small part of the price of "
                  "precious metals?",
             "a": ["Because they cost nothing to mine",
                   "Because their mines are all owned by sovereigns",
                   "Because the price is set by the world's most fertile mine, and "
                   "labour and profit make up most of it at the rest",
                   "Because gold and silver are used only as money"],
             "c": 2,
             "why": "Metals bear carriage so well that mines everywhere compete, so the "
                    "price at the most fertile mines in the world fixes the price at the "
                    "rest, and at the greater part of mines it does little more than pay "
                    "working expense. The other answers are not Smith's reasons."},
        ],
        "mistakes": [
            ("Expecting every mine, like every farm, to pay a rent",
             "Smith says mines pay rent only if they are fertile enough, or well enough "
             "placed, for the price to leave something above outlay and ordinary "
             "profit. In the first preset three mines are worked and only two pay a "
             "rent; in the second only two can pay anything."),
            ("Taking a mine's rent to measure its absolute fertility",
             "A mine's rent depends on its superiority over other mines of the "
             "same kind. If much richer mines were found, Smith says, the value of "
             "silver might fall so far that even Potosi was not worth the working, "
             "though its output was unchanged."),
            ("Reading &ldquo;thirteen to twelve&rdquo; as a comparison of the rents' "
             "sizes in money",
             "It is a comparison of shares of each mine's gross produce, not of "
             "amounts. A mine with a large produce and a small share can pay a greater "
             "sum, and Smith's comparison says nothing about which it is."),
        ],
        "standard": (
            "Finish when you can say which mines pay a rent at a given price.",
            "Given several mines' outputs and outlays and a price, say which can be "
            "worked, which pay no rent, what the rents total, and what the rents "
            "become when the best mine's price is the market price.",
        ),
        "note": (
            "The lab sets one price for every mine, which suits coal sold in one "
            "neighbourhood and not metals sold across the world, where Smith's "
            "point is that the price at the best mine governs the rest. The mines "
            "in the first two presets are written for the lesson, and so are the "
            "outlays in the third; only the shares and the thirteen to twelve are "
            "Smith's, and he reports them on the authority of Borlace, Frezier and "
            "Ulloa. Whether the best mine really sets the price, or the "
            "marginal mine does, is the dispute Ricardo opened and the Capital "
            "Subject's <em>Building Rent, Mining Rent, the Price of Land</em> takes "
            "further."
        ),
    },
]
