"""Merchant's Capital and Interest, lessons 1-5 -- Volume III, Part IV, Chapters 16-20.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, and the translator's double quotation marks inside a
quotation are printed as single curly quotes. No quotation opens on one of
the text's drop capitals ("THE", "IN"), so the first word's case is always
the text's. Nothing else is changed.

Untermann calls Marx's Geldhandlungskapital "financial capital", and Chapter
19's module name keeps his title, as PLAN §E.3 requires; the lesson title and
prose say "money-dealing capital", and the lesson says why once, because
"financial capital" means something else to a reader today.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 3, l. 2596 (a changed form of the capital of circulation).
    # Inline: l. 2600 (3,000 p.st. of linen), l. 2610 (the clerk), l. 2646
    # (the persons who hold it), l. 2628 (his own or borrowed), l. 2668 (the
    # quicker the turnover),
    # l. 2681-2683 (no value, at least not directly).
    {
        "slug": "commercial-capital",
        "title": "Commercial Capital",
        "module": "Chapter 16 · Commercial Capital",
        "one_line": "A merchant's capital is the manufacturer's commodity capital in other hands: it makes the selling a separate business, and it creates no value doing so.",
        "summary": (
            "Part IV opens by asking what a merchant is in a world of industrial capital. "
            "Marx's answer is that commercial capital is a piece of the capital that every "
            "manufacturer must keep in circulation, handed over to a specialist. Compute the "
            "commodity capital a merchant takes off the manufacturers' hands in a year from "
            "the capital he advances and the times he turns it over, and see why a quicker "
            "merchant needs less capital for the same trade."
        ),
        "key": [
            "commercial capital: C–M done by another",
            "the merchant's circuit: M–C–M′",
            "the same linen is sold twice",
            "trade a year = capital × turnovers",
            "quicker turnover: less capital needed",
        ],
        "key_label": "Chapter 16 in five lines",
        "concepts_intro": (
            "Volume II followed one capital through its circuit and found a stage, selling, "
            "in which nothing is produced. Chapter 16 watches that stage become somebody "
            "else's business."
        ),
        "concepts": [
            ("Commodity capital in other hands",
             "Once the linen is made it must be sold. If a merchant buys it, the manufacturer "
             "has his money and goes on producing, but the linen is still on the market "
             "waiting for its final buyer. Nothing has changed except the person who holds "
             "it."),
            ("The merchant's advance",
             "A travelling agent who sells on commission is not a capitalist. What makes "
             "the merchant one is that he advances money capital, his own or borrowed: his business is "
             "M–C–M′, buying in order to sell, and the same commodity changes hands twice."),
            ("A smaller money reserve",
             "Without the merchant each manufacturer would keep a larger reserve to carry "
             "him while his goods sold. One merchant's capital, turned over many times, "
             "does that work for many manufacturers, so the capital tied up in circulation "
             "is smaller."),
        ],
        "read_title": "The definition, then the linen merchant",
        "read_intro": (
            "The definition comes a page into the chapter, after Marx has set aside the "
            "transport and storage that a merchant may also do. The rest of the chapter is "
            "one linen merchant with 3,000 pounds."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 16.</strong> &ldquo;Commercial capital is "
                  "nothing else but a changed form of a portion of this capital of "
                  "circulation, which exists continually on the market in the process of its "
                  "metamorphoses within the sphere of circulation.&rdquo;"),
            ("p", "Volume III has so far been about capital in production: cost price, the "
                  "rate of profit, and the averaging of profit across industries. Part IV turns "
                  "to the people who never produce anything and still own capital: the "
                  "merchant, who buys and sells goods, and the money-dealer, who handles "
                  "payments. Marx's complaint, in the chapter's first paragraph, is that "
                  "economists file trading capital under industrial capital and miss what is "
                  "peculiar to it. This lesson and the next three say what is."),
            ("p", "Take the passage a phrase at a time. The phrase &ldquo;this capital of "
                  "circulation&rdquo; means the part of the social capital that is always on the "
                  "market as goods waiting to be sold or as money waiting to buy, the stage "
                  "Volume II called commodity capital and money capital. &ldquo;A "
                  "portion&rdquo; is said with care: manufacturers also buy from and sell to "
                  "each other, and Marx sets that part aside. And &ldquo;a changed form&rdquo; "
                  "is the claim of the chapter. The merchant's capital is not a new kind of "
                  "capital beside the mill's. It is the mill's selling, done by someone "
                  "else."),
            ("p", "Marx's example is a merchant with 3,000 pounds who buys 30,000 yards of "
                  "linen at 2 shillings a yard and sells it again. The manufacturer has his "
                  "money and buys yarn, coal and labour; for him the sale is over. For the "
                  "linen it is not: it is still on the market, and nothing has happened to it "
                  "but a change in the person of its owner. If the merchant cannot sell before "
                  "the next 30,000 yards are ready, he cannot buy them, and the manufacturer's "
                  "reproduction stalls exactly as if he had kept the linen himself. Put a "
                  "salaried clerk in the merchant's place, Marx says, and &ldquo;this "
                  "connection would not be obscured for a moment.&rdquo;"),
            ("p", "So what makes the merchant a capitalist rather than a clerk? Two things, "
                  "on Marx's count. Selling becomes the exclusive business of a separate "
                  "agent, and that agent advances money capital, &ldquo;his own or "
                  "borrowed&rdquo;. A commission salesman has "
                  "the first and not the second. The merchant buys outright, and his business "
                  "is `M–C–M′`. Notice what changes hands twice here. In the manufacturer's "
                  "sale-and-purchase `C–M–C` it is the money: received for linen, spent on "
                  "yarn. In the merchant's `M–C–M′` it is the same linen, sold to him and sold "
                  "by him, and that second sale is how his money comes back."),
            ("p", "The lab computes the one quantity the chapter turns on: how much commodity "
                  "capital a merchant takes off the manufacturers' hands in a year. In the "
                  "no-merchant preset there is no merchant capital and the tile reads £0: "
                  "every manufacturer carries his own goods until they sell. In the merchant "
                  "preset Marx's 3,000 pounds are taken as turning over once, one lot of linen a "
                  "year, £3,000; the chapter gives the sum and leaves the number of turnovers "
                  "open. In the "
                  "faster-merchant preset the same £3,000 is turned over four times, because "
                  "the merchant sells each lot before its maker can finish the next and buys "
                  "from other manufacturers in between: `£3,000 × 4 = £12,000`. Marx draws the "
                  "conclusion: &ldquo;The quicker merchant's capital is turned over, the "
                  "smaller is that portion of the total money-capital, which serves as "
                  "merchant's capital&rdquo;. To move £12,000 of linen a year takes £12,000 of "
                  "merchant's capital turned once, or £3,000 turned four times."),
            ("p", "That is the case for the merchant on Marx's terms, and he makes it "
                  "himself. A capital devoted only to buying and selling is smaller than the "
                  "reserves the manufacturers would otherwise need; their goods turn into "
                  "money faster; and one merchant's capital can serve many producers, even in "
                  "different trades, when he buys linen and then silk. The other side of the "
                  "ledger is that a slice of the social capital now sits permanently in "
                  "circulation, buying and selling and doing nothing else. Marx's dry summary "
                  "of the change: &ldquo;There seems then to have been no other change but "
                  "that of the persons who hold this capital in their hands.&rdquo;"),
            ("p", "<strong>Volume III, Chapter 16.</strong> &ldquo;Merchant's capital, "
                  "therefore, does not create any value or surplus-value, at least not "
                  "directly.&rdquo;"),
            ("p", "The reason is the one Volume II gave: no value is produced in circulation, "
                  "only changes of form of the same values. The words &ldquo;at least not "
                  "directly&rdquo; are a real qualification. By shortening the time goods "
                  "spend unsold, the merchant lets more of the industrial capital stay in "
                  "production, and on Marx's account that raises the surplus value produced "
                  "and the rate of profit. It is the same with a quicker bus to work: the bus "
                  "makes nothing at the office, but you get more hours there. Adam Smith, "
                  "whom Marx does not cite here but who is the obvious other side, counted the "
                  "capital of wholesale and retail traders among the productive employments of "
                  "capital, and modern national accounts count a trade margin as value added. "
                  "Marx's line runs between the two kinds of usefulness, and this lesson "
                  "computes on his side of it."),
            ("p", "If the merchant creates no value, his profit must come from somewhere. "
                  "The next lesson, “Commercial Profit”, finds where, in Marx's own figures: "
                  "an industrial capital of 900 and a merchant's capital of 100."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "merchant",
            "money_unit": "£",
            "preset": "merchant",
            "presets": [
                {"id": "no-merchant", "label": "No merchant: each manufacturer holds his own goods",
                 "merchant_capital": 0, "merchant_turnovers": 0,
                 "expect": {"tuFreed": "£0"}},
                {"id": "merchant", "label": "Marx's £3,000 of linen, taken as one turnover a year",
                 "merchant_capital": 3000, "merchant_turnovers": 1,
                 "expect": {"tuFreed": "£3,000"}},
                {"id": "faster-merchant", "label": "The same £3,000 turned over four times a year",
                 "merchant_capital": 3000, "merchant_turnovers": 4,
                 "expect": {"tuFreed": "£12,000"}},
            ],
            "panel_title": "What a merchant takes off the manufacturers' hands",
            "panel_intro": (
                "The merchant's capital and the times he turns it over in a year go in; the "
                "tile is the commodity capital he buys from manufacturers in that year, which "
                "they would otherwise hold until it sold. The £3,000 is Marx's linen merchant; "
                "the four turnovers are illustrative."
            ),
        }),
        "steps_title": "Sizing a merchant's capital",
        "steps_intro": "Four steps for any trade a merchant takes over.",
        "steps": [
            ("Find the merchant's advance",
             "Take the money capital the merchant lays out on one purchase. Money owed on "
             "credit and repaid from the sale is not his advance."),
            ("Count the turnovers",
             "Count how many times a year the advance is laid out and comes back through a "
             "sale. It is limited by how fast the producers produce and how fast the "
             "consumers buy, not by any one producer."),
            ("Multiply",
             "The commodity capital taken off the producers' hands in a year is the advance "
             "times the turnovers."),
            ("Invert for the capital needed",
             "For a given trade a year, the merchant's capital needed is the trade divided by "
             "the turnovers: the quicker the turnover, the smaller the capital tied up in "
             "circulation."),
        ],
        "worked": {
            "title": "One linen merchant, four manufacturers",
            "intro": [
                "A merchant has £3,000 and sells each lot of linen before its maker can finish "
                "the next, so he buys from four manufacturers in turn and turns his capital "
                "over four times a year. You want the linen he takes off their hands, and the "
                "capital a merchant who turned over once would need for the same trade.",
            ],
            "lines": [
                "trade a year:  £3,000 × 4 = £12,000",
                "turned over once:  £12,000 / 1 = £12,000 needed",
                "turned over four times:  £12,000 / 4 = £3,000 needed",
            ],
            "after": [
                "The same £12,000 of linen reaches its buyers either way. The quicker merchant "
                "does it with a quarter of the capital, and on Marx's account the rest is "
                "free to stay in production.",
            ],
        },
        "quiz_title": "A changed form of the capital of circulation",
        "quiz": [
            {"q": "A merchant advances £2,000 and turns it over three times a year. How much "
                  "commodity capital does he take off the producers' hands in a year?",
             "a": ["£6,000", "£2,000", "£666⅔", "£8,000"],
             "c": 0,
             "why": "Trade a year is advance times turnovers, `£2,000 × 3 = £6,000`. £2,000 is "
                    "one turnover, £666⅔ divides where it should multiply, and £8,000 counts "
                    "a fourth turnover that does not happen."},
            {"q": "On Marx's account, what makes a merchant a capitalist rather than a "
                  "salesman for the manufacturer?",
             "a": ["He advances money capital and buys the goods outright",
                   "He moves the goods to where they are consumed",
                   "He adds value to the goods by selling them",
                   "He sells to many buyers instead of one"],
             "c": 0,
             "why": "Marx names two elements: selling becomes a separate business, and the "
                    "merchant advances money capital. A commission agent has the first only. "
                    "Transport is set aside as production continued in circulation, selling "
                    "adds no value, and selling to many buyers is something a salesman does "
                    "too."},
            {"q": "A trade of £24,000 a year is carried by merchants who turn their capital "
                  "over six times a year. How much merchant's capital does it need?",
             "a": ["£4,000", "£24,000", "£144,000", "£6,000"],
             "c": 0,
             "why": "Capital needed is trade divided by turnovers, `£24,000 / 6 = £4,000`. "
                    "£24,000 is the capital for one turnover a year, £144,000 multiplies, and "
                    "£6,000 divides by four."},
            {"q": "In `M–C–M′`, the merchant's circuit, what changes hands twice?",
             "a": ["The same commodity", "The same money", "The means of production",
                   "Labour-power"],
             "c": 0,
             "why": "The linen is sold to the merchant and sold again by him; that second "
                    "sale returns his money. In the manufacturer's `C–M–C` it is the same money "
                    "that changes hands twice. The merchant buys neither means of production "
                    "nor labour-power for production."},
        ],
        "mistakes": [
            ("Thinking merchants produce value by moving goods from hand to hand",
             "Every sale passes goods from one owner to another, and it can look as if the "
             "passing were the work that makes them worth more. Marx's linen shows otherwise: "
             "after the merchant buys it, nothing has happened to it but a change in the "
             "person of its owner. In the no-merchant preset nothing changes owner and the "
             "tile reads £0; in the merchant preset £3,000 of linen changes owner and is "
             "still worth £3,000. What the merchant can do is shorten "
             "the time goods wait, which helps the industrial capital produce more."),
            ("Confusing the merchant's selling with transport and storage",
             "A merchant may also carry and store goods, and Volume II counted those as "
             "production continued in circulation, which adds value. Marx strips them away "
             "to see the merchant's own function, buying in order to sell, which does not."),
            ("Thinking a larger merchant's capital means more trade",
             "The same trade can be carried by a large capital turned slowly or a small one "
             "turned quickly. In the faster-merchant preset £3,000 does what £12,000 would "
             "do turned once."),
        ],
        "standard": (
            "Finish when you can size a merchant's capital from its turnovers.",
            "Given a merchant's advance and turnovers a year, compute the commodity capital "
            "he takes off the producers' hands in a year, and given a year's trade and the "
            "turnovers, compute the merchant's capital it needs."
        ),
        "note": (
            "The tile multiplies the advance by the turnovers and nothing more. Whether the "
            "manufacturers' money freed by the merchant actually goes into production, and "
            "whether merchant's capital stays within what Marx calls its necessary "
            "proportions, are conditions the chapter states and the lab assumes. The four "
            "turnovers are illustrative; the 3,000 pounds of linen are Marx's."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 3, l. 2717 (900 industrial + 100 merchant: 1,062 and 1,080).
    # Inline: l. 2697 (outward semblance), l. 2707 (2 sh. 2 2/5d.), l. 2727
    # (purchase price below value), l. 2739 (commercial profit originally),
    # l. 2772 (17 1/7%, 1,130), l. 2785 (the clerks' unpaid labour).
    {
        "slug": "commercial-profit",
        "title": "Commercial Profit",
        "module": "Chapter 17 · Commercial Profit",
        "one_line": "The merchant sells at value and still makes a profit, because the manufacturer sold to him below value: the merchant's capital shares in the averaging of profit.",
        "summary": (
            "If merchants create no value, how do they profit without selling above value? "
            "Marx's answer is that the merchant's capital joins the averaging of profit, so "
            "the general rate is reckoned over industrial and merchant's capital together and "
            "the manufacturer sells to the merchant below value. Compute the general rate, "
            "the price at which the manufacturer sells and the merchant's price, in Marx's "
            "figures, with and without the merchant's own costs."
        ),
        "key": [
            "rate = s / (industrial + merchant)",
            "180 / (900 + 100) = 18%",
            "industrial price = k + rate × capital",
            "900 + 162 = 1,062; 1,062 + 18 = 1,080",
            "the merchant sells at value",
            "with £50 of costs: 17 1/7%, 1,130",
        ],
        "key_label": "Chapter 17's arithmetic",
        "concepts_intro": (
            "The chapter has a puzzle and an answer. The puzzle is how a capital that adds "
            "no value earns the average profit; the answer changes the definition of the "
            "general rate itself."
        ),
        "concepts": [
            ("The appearance of a mark-up",
             "The merchant's profit is the excess of his selling price over his purchase "
             "price, so it looks like a mark-up added to value. If the manufacturer sold to "
             "him at value, it would be one, and every commodity would sell above value."),
            ("The merchant's share in averaging",
             "Merchant's capital must earn the average rate, or capital would move into or "
             "out of trade. So the surplus value of all industry is averaged over industrial "
             "and merchant's capital together, and the general rate is lower than "
             "industry's alone."),
            ("Buying below value",
             "The manufacturer sells at his cost price plus the general rate on his own "
             "capital, which is less than value. The merchant adds the same rate on his "
             "capital and sells at exactly the value."),
        ],
        "read_title": "Marx's example first, then the puzzle it answers",
        "read_intro": (
            "The passage is the arithmetic at the centre of the chapter. Marx reaches it "
            "after showing why the obvious explanation of commercial profit cannot be "
            "right."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 17.</strong> &ldquo;In other words, the "
                  "price at which C is sold by the owners of the industrial capital of 900 to "
                  "the dealers is 720 c + 180 v + 162 s = 1,062. Now, if the dealer adds his "
                  "average profit of 18% on his capital of 100, he sells the commodities at "
                  "1,062 + 18 = 1,080, which is their price of production, or, from the point "
                  "of view of the total commodity-capital, their value&rdquo;."),
            ("p", "Think of any shop. It buys a jacket for one price and sells it for more, "
                  "and the difference pays the shop. That is the merchant's profit as everyone "
                  "sees it, and Marx grants that it is the only place the profit can come "
                  "from: the excess of the selling price over the purchase price. His sharper "
                  "question is whether that excess is a price raised above value. His "
                  "illustration of the obvious answer is a yard of linen bought at 2 shillings "
                  "and sold at 2s 2⅖d to make 10 per cent, which, he notes, comes to the same "
                  "as selling the buyer 10/11 of a yard for 2 shillings. Then: "
                  "&ldquo;It is only outward semblance that commercial profit is a mere "
                  "addition to, a nominal raise of the prices of commodities above their "
                  "value.&rdquo;"),
            ("p", "Why only a semblance? Because the mark-up story assumed that the "
                  "manufacturer sold to the merchant at the full price of production, and that "
                  "assumption came from Part II, where the general rate of profit was worked "
                  "out before merchant's capital existed in the analysis. Bring the merchant "
                  "in and the rate itself must be worked out again."),
            ("p", "So the passage. The industrial capital of society is 720c + 180v, and with "
                  "a rate of surplus value of 100 per cent its product is worth 1,080, of which "
                  "180 is surplus value. On industrial capital alone that is 20 per cent. Now "
                  "add 100 of merchant's capital. Capital moves freely into and out of trade, "
                  "so the merchant must earn the same rate as anyone, and the 180 is spread "
                  "over 1,000: 18 per cent. The manufacturers sell at their cost of 900 plus "
                  "18 per cent of 900, which is &ldquo;720 c + 180 v + 162 s = "
                  "1,062&rdquo;. The merchant adds 18 per cent of his 100 and sells at 1,080. "
                  "That is the value of the goods. Marx's formula for it: the merchant's "
                  "selling price &ldquo;stands above his purchase price, not because the former "
                  "stands above the total value, but because the purchase price stands below "
                  "this value.&rdquo;"),
            ("p", "The lab does the averaging. In the marx preset the general rate is `9/50`, "
                  "18 per cent, and the prices are £1,062 and £1,080, Marx's figures to the "
                  "pound. In the no-merchant preset the merchant's capital is zero: the rate "
                  "goes back to 20 per cent and the manufacturers sell at £1,080, the value, "
                  "with nothing left for anyone else. Compare the two and the merchant's 18 "
                  "is exactly what the manufacturers gave up, `1,080 − 1,062`. Marx's first "
                  "corollary follows: the larger the merchant's capital in proportion to the "
                  "industrial, the lower the rate of industrial profit."),
            ("p", "Then the merchant's own costs: offices, paper, postage and the clerks. Marx "
                  "adds 50 of them to the merchant's 100. The surplus value of 180 is now "
                  "spread over `900 + 150 = 1,050`, and &ldquo;The average rate of profit then "
                  "falls to 17 1/7%.&rdquo; The manufacturers sell at `900 + 154 2/7`, and the "
                  "merchant at 1,130: the value of 1,080 plus the 50 he must recover. The "
                  "with-costs preset reproduces all three figures, printing the manufacturers' "
                  "price as the exact fraction `£7,380/7`, which is Marx's 1,054 2/7. The 50 enters the price "
                  "without adding value to the goods, which is what Marx means by calling these "
                  "pure costs of circulation."),
            ("p", "Who pays for the clerks, on this account? Their work realises value and "
                  "creates none, yet the merchant profits by it, because the more buying and "
                  "selling they do the more capital he can turn over. Marx puts it exactly: "
                  "&ldquo;The unpaid labor of his clerks, while it does not create any "
                  "surplus-value, at least appropriates surplus-value for him&rdquo;. He adds, "
                  "with an eye on the commercial clerks of his day, that their wages tend to "
                  "fall as schooling spreads and more people can do the work."),
            ("p", "The standard objection is the one met in “The Costs of Circulation”, "
                  "now aimed at the merchant's profit itself. On the mainstream account a "
                  "retailer sells a service, putting goods where and when buyers want them, "
                  "and the margin is the price of that service, produced like any other. Marx's "
                  "1,062 and 1,080 also rest on the averaging of Part II, with every input "
                  "taken at value, which is where the transformation problem enters. The lab "
                  "computes his accounting and leaves both disputes where they stand."),
            ("p", "One more turn: Marx says the historical order is the reverse of the "
                  "analytical one. In the analysis industrial profit comes first and the "
                  "merchant is fitted in afterwards; in history it was trade that first brought "
                  "prices near values, and &ldquo;The commercial profit originally determines "
                  "the industrial profit.&rdquo; That history is the subject of “Historical "
                  "Facts about Merchant's Capital”."),
            ("p", "Eighteen per cent a year is the merchant's rate. The next lesson, “The "
                  "Turnover of Merchant's Capital”, asks what it means for the price of a "
                  "single article when one merchant turns his capital over once a year and "
                  "another five times."),
        ],
        "lab": ("capkit", {
            "mode": "prices",
            "view": "merchant",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 720c + 180v + 180s and a merchant's 100",
                 "spheres": [{"name": "industry", "c": 720, "v": 180}],
                 "s_rate": 1, "merchant_capital": 100,
                 "expect": {"ppAverage": "9/50 = 18%",
                            "ppMerchantPrice": "industrial £1,062; merchant £1,080"}},
                {"id": "no-merchant", "label": "No merchant's capital: industry alone",
                 "spheres": [{"name": "industry", "c": 720, "v": 180}],
                 "s_rate": 1, "merchant_capital": 0,
                 "expect": {"ppAverage": "1/5 = 20%",
                            "ppMerchantPrice": "industrial £1,080; merchant £1,080"}},
                {"id": "with-costs", "label": "Marx's figures with 50 of the merchant's own costs",
                 "spheres": [{"name": "industry", "c": 720, "v": 180}],
                 "s_rate": 1, "merchant_capital": 100, "merchant_costs": 50,
                 "expect": {"ppAverage": "6/35 = 17.14%",
                            "ppMerchantPrice": "industrial £7,380/7; merchant £1,130"}},
            ],
            "panel_title": "The general rate with the merchant in it",
            "panel_intro": (
                "The industrial capital, its rate of surplus value, the merchant's capital and "
                "his own circulation costs go in. The lab spreads the surplus value over all of "
                "it, prices the manufacturers' sale at cost plus the general rate on their "
                "capital, and prices the merchant's sale at that plus his costs and the rate on "
                "his capital and costs. Every preset uses Marx's figures."
            ),
        }),
        "steps_title": "Pricing the manufacturer's and the merchant's sale",
        "steps_intro": "Four steps, the same for any merchant's capital Marx's way.",
        "steps": [
            ("Total the surplus value and the capital",
             "Add the surplus value of all industrial capital, and add the industrial "
             "capital, the merchant's capital and any capital the merchant lays out on "
             "costs."),
            ("Divide for the general rate",
             "The general rate of profit is the total surplus value divided by the total "
             "capital, merchant's capital included."),
            ("Price the manufacturer's sale",
             "The manufacturer sells at his cost price plus the general rate on his own "
             "capital. With all capital used up in the year, that is his capital times one "
             "plus the rate."),
            ("Price the merchant's sale",
             "The merchant adds his costs, if any, and the general rate on his capital plus "
             "costs. Without costs the result is the value of the goods."),
        ],
        "worked": {
            "title": "Marx's 900 and 100",
            "intro": [
                "Industrial capital is 720c + 180v with surplus value 180, and merchants hold "
                "100. You want the general rate and the two prices.",
            ],
            "lines": [
                "rate:  180 / (900 + 100) = 9/50 = 18%",
                "manufacturer:  900 + 18% × 900 = 1,062",
                "merchant:  1,062 + 18% × 100 = 1,080",
                "value:  720 + 180 + 180 = 1,080",
            ],
            "after": [
                "The merchant's 18 is the difference between what the manufacturers would "
                "have taken at 20 per cent, 180, and what they take at 18 per cent, 162. "
                "Nothing is sold above value.",
            ],
        },
        "quiz_title": "Where the merchant's profit comes from",
        "quiz": [
            {"q": "Industrial capital of 800 produces surplus value of 200, and merchants "
                  "hold 200. What is the general rate of profit on Marx's account?",
             "a": ["20%", "25%", "100%", "40%"],
             "c": 0,
             "why": "The surplus value is spread over all the capital, `200 / (800 + 200) = "
                    "1/5`. 25 per cent leaves the merchant out, 100 per cent divides by the "
                    "merchant's capital alone, and 40 per cent adds the merchant's capital "
                    "to the surplus value."},
            {"q": "In Marx's example the manufacturers sell at 1,062 and the merchant at "
                  "1,080. Which statement is right?",
             "a": ["The merchant sells at value; the manufacturers sell below it",
                   "The merchant sells 18 above value",
                   "Both sell at value",
                   "The manufacturers sell at value and the merchant above it"],
             "c": 0,
             "why": "The goods are worth `720 + 180 + 180 = 1,080`. The merchant sells at "
                    "exactly that; the manufacturers, at 1,062, sell below it. The mark-up "
                    "readings are the semblance Marx sets out to dispel."},
            {"q": "In the with-costs preset the merchant adds 50 of costs to his 100. Why "
                  "does the general rate fall from 18% to 17 1/7%?",
             "a": ["The same 180 of surplus value is spread over 1,050 of capital",
                   "The costs reduce the surplus value produced to 170",
                   "The merchant takes a smaller share of the profit",
                   "The manufacturers' capital rises to 950"],
             "c": 0,
             "why": "The costs are capital that must earn the average rate, so `180 / 1,050 = "
                    "6/35`. Production is untouched, so surplus value stays 180, the "
                    "manufacturers' capital is still 900, and the merchant's share rises."},
            {"q": "On Marx's account, what happens to the rate of industrial profit as "
                  "merchant's capital grows relative to industrial capital, other things "
                  "equal?",
             "a": ["It falls", "It rises", "It stays the same", "It doubles"],
             "c": 0,
             "why": "The same surplus value is averaged over more capital. Marx states it "
                    "as his first corollary: the larger the merchant's capital in proportion, "
                    "the smaller the rate of industrial profit."},
        ],
        "mistakes": [
            ("Thinking the merchant's profit is a mark-up added on top of value",
             "It looks like one, because the merchant profits only by selling dearer than he "
             "bought. Marx calls this an outward semblance. In the marx preset the merchant "
             "sells at £1,080, which is the value of the goods; his £18 comes from the "
             "manufacturers' selling to him at £1,062, below value. In the no-merchant preset "
             "the manufacturers sell at £1,080 themselves and keep the 18."),
            ("Reckoning the general rate on industrial capital alone",
             "Part II's rate, 180 on 900, left trade out. Once merchant's capital earns the "
             "average, the rate is 180 on 1,000, and the price of production a manufacturer "
             "charges is lower than the one Part II computed."),
            ("Thinking the merchant's costs add value because they raise the price",
             "In the with-costs preset the merchant sells at 1,130, 50 above value, and "
             "recovers his costs. Marx calls the addition a nominal value: the price rises "
             "and the value of the goods is still 1,080."),
        ],
        "standard": (
            "Finish when you can price the manufacturer's and the merchant's sale.",
            "Given industrial capital, its surplus value, the merchant's capital and his "
            "costs, compute the general rate of profit, the price at which the manufacturer "
            "sells to the merchant and the merchant's selling price, and compare them with "
            "the value."
        ),
        "note": (
            "The lab treats the whole industrial capital as one sphere of average "
            "composition, used up in a year, as Marx's example does, so price of production "
            "and value coincide for the total. The merchant's costs are taken as Marx takes "
            "them in this example, wholly recovered in the price with profit on them. "
            "Whether a merchant's margin is the price of a service is the dispute the "
            "accounting presupposes and does not decide."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 3, l. 2930 (15% a year, once and five times). Inline:
    # l. 2883 (sugar), l. 2885 (nothing more ridiculous), l. 2869 (crisis),
    # l. 2946 (perverted conceptions), l. 2952 (small profits and quick
    # returns), l. 2956 (location and rent).
    {
        "slug": "the-turnover-of-merchants-capital",
        "title": "The Turnover of Merchant's Capital",
        "module": "Chapter 18 · The Turn-Over of Merchant's Capital. The Prices",
        "one_line": "A merchant who turns his capital over more often earns the same rate a year and adds a smaller mark-up to each sale.",
        "summary": (
            "An industrial capital that turns over faster produces more surplus value; a "
            "merchant's capital that turns over faster does not. Its rate is the general "
            "rate, given from outside, and what its turnovers change is the mark-up on each "
            "sale. Compute the mark-up per turnover from Marx's 15 per cent a year and five "
            "turnovers, and see why “small profits and quick returns” is not the merchant's "
            "choice."
        ),
        "key": [
            "the merchant's rate is the general rate",
            "addition per sale = annual rate / turnovers",
            "15% a year, 5 turnovers: 3% a sale",
            "100 sells at 103, five times: 515",
            "faster turnover, a smaller addition per sale",
        ],
        "key_label": "Chapter 18 in five lines",
        "concepts_intro": (
            "The chapter compares two kinds of turnover that look alike and work in "
            "opposite ways."
        ),
        "concepts": [
            ("Industrial turnover",
             "When an industrial capital turns over faster it sets more labour in motion in "
             "a year, so it produces more surplus value, and with it the general rate of "
             "profit rises. Its turnover helps determine the rate."),
            ("Merchant's turnover",
             "For the merchant the general rate is a given. However often he turns over his "
             "capital, he earns that rate a year on it, so a faster turnover spreads the same "
             "annual profit over more sales."),
            ("The mark-up",
             "The addition to the price of each lot is the annual rate divided by the "
             "turnovers. It varies inversely with the turnover, which is why merchants' "
             "prices look as if circulation set them."),
        ],
        "read_title": "The passage, then the sugar",
        "read_intro": (
            "Marx's arithmetic sits in the middle of the chapter. It answers a question the "
            "chapter raised earlier with a pound of sugar."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 18.</strong> &ldquo;If the yearly general rate "
                  "of profit is 15%, and the merchant advances 100 p.st., which he turns over "
                  "once a year, then he will sell his commodities at 115. If his capital is "
                  "turned over five times per year, then he will sell a commodity-capital of "
                  "100 purchase price five times per year at 103, which will amount in one "
                  "year to a commodity-capital of 500 sold 515.&rdquo;"),
            ("p", "You know two kinds of shop. One sells furniture, with a few big sales a "
                  "month and stock that waits; the other sells groceries, with stock that is "
                  "gone in days. The furniture shop's margin on each item is large and the "
                  "grocer's is thin, and it is easy to think the furniture dealer has simply "
                  "decided to charge more. Chapter 18 says neither of them decided anything."),
            ("p", "Go through the passage. The rate of 15 per cent is &ldquo;yearly&rdquo; "
                  "and &ldquo;general&rdquo;: it is the rate every capital earns a year, the "
                  "rate of “Commercial Profit” with a different figure. Turned over once, the "
                  "merchant's 100 comes back as 115. Turned over five times, it buys 100 and "
                  "sells at 103 each time, and five sales at 3 make 15: &ldquo;500 sold "
                  "515&rdquo;. The annual profit is the same 15 on the same 100. If the fast "
                  "merchant charged 15 on every sale he would make 75 a year, and capital would "
                  "rush into his line until it stopped."),
            ("p", "The lab divides. In the marx preset the rate is `3/20` a year and the "
                  "turnovers are 5, so the mark-up is `3/100`, 3 per cent, and 100 sells at "
                  "£103. In the once preset the mark-up is the whole 15 per cent and 100 sells "
                  "at £115. In the ten preset it is `3/200`, 1½ per cent, and 100 sells at "
                  "`£203/2`, which is £101½. The rate on the merchant's capital is 15 per cent a year in all "
                  "three."),
            ("p", "Marx's sugar example makes the same point from the price side. At £1 for "
                  "a pound of sugar, £100 buys 100 lb, and a merchant who turns over "
                  "once adds 3 shillings to each pound to make his £15. If productivity cuts "
                  "the price of production to 1 shilling, the same £100 buys 2,000 lb "
                  "and the addition to each is 1⅘d. The profit a year is unchanged. What "
                  "fixes the mark-up is the price of production, which the merchant does not "
                  "control, and the general rate, which he does not control either. So, Marx "
                  "says, &ldquo;there is nothing more ridiculous than the current idea that "
                  "it depends on the merchant whether he wants to sell many commodities at a "
                  "small profit or few commodities at a large profit on the individual "
                  "commodities.&rdquo; He excepts the monopolist, the Dutch East India Company "
                  "his example, and he names one economist who had not seen it: Wilhelm "
                  "Roscher of Leipzig, who could still imagine selling prices changed by "
                  "&ldquo;prudence and humanity&rdquo; rather than by a change in "
                  "production."),
            ("p", "He enjoys the shopkeeper's motto: &ldquo;Small profits and quick returns "
                  "appears particularly to the shopkeeper as a principle, which he follows on "
                  "principle.&rdquo; The motto describes the result of a fast turnover, and the "
                  "shopkeeper reads it as his policy. Marx makes a larger claim of the same "
                  "kind: because turnover visibly sets the mercantile mark-up, it looks as if "
                  "circulation fixed prices by itself, and &ldquo;The conceptions of a "
                  "merchant, a stock gambler, a banker, are necessarily quite "
                  "perverted.&rdquo;"),
            ("p", "Two qualifications keep the law honest. It holds for the average turnover "
                  "of a whole line of trade. A single merchant who turns over faster than the "
                  "average in his line makes an extra profit, as an industrialist with a "
                  "better machine does, and if the advantage comes from something that can be "
                  "bought, a good corner site, he may pay part of it away as rent. And merchants' "
                  "turnover can run ahead of consumption, one merchant selling to another on "
                  "credit, until &ldquo;The internal dependence and the external independence "
                  "drive merchant's capital to a point, where the internal connection is "
                  "violently restored by a crisis.&rdquo; That is why, Marx says, crises "
                  "break out first in wholesale trade and banking rather than in the shops."),
            ("p", "A modern reader may object that firms do choose between high margins and "
                  "high volume, and that pricing strategy is a whole field of study. What in "
                  "the chapter bears on it is Marx's list of such choices, underselling a "
                  "rival among them, which he says concern only the competition of merchants "
                  "among themselves and leave the average untouched. Whether averages discipline margins as strictly as the "
                  "chapter assumes is a question about real markets this lab does not "
                  "carry."),
            ("p", "That ends commercial capital. The next lesson, “Money-Dealing Capital”, "
                  "takes the other half of Part IV: the capital that does nothing but keep, "
                  "pay and exchange money for everyone else."),
        ],
        "lab": ("capkit", {
            "mode": "prices",
            "view": "merchant-turnover",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 15% a year, five turnovers",
                 "profit_rate": "3/20", "merchant_turnovers": 5, "merchant_capital": 100,
                 "expect": {"ppMarkup": "3/100 = 3%",
                            "ppMerchantPrice": "buys at £100, sells at £103"}},
                {"id": "once", "label": "Marx's figures: 15% a year, turned over once",
                 "profit_rate": "3/20", "merchant_turnovers": 1, "merchant_capital": 100,
                 "expect": {"ppMarkup": "3/20 = 15%",
                            "ppMerchantPrice": "buys at £100, sells at £115"}},
                {"id": "ten", "label": "15% a year, turned over ten times",
                 "profit_rate": "3/20", "merchant_turnovers": 10, "merchant_capital": 100,
                 "expect": {"ppMarkup": "3/200 = 1.5%",
                            "ppMerchantPrice": "buys at £100, sells at £203/2"}},
            ],
            "panel_title": "The mark-up on each turnover",
            "panel_intro": (
                "The general rate of profit a year, the merchant's turnovers a year and the "
                "capital laid out on each turnover go in. The tiles show the addition to the "
                "price on each sale and the price at which one turnover's goods are sold. The "
                "first two presets are Marx's figures; ten turnovers are illustrative."
            ),
        }),
        "steps_title": "Finding the mark-up per turnover",
        "steps_intro": "Four steps for any line of trade.",
        "steps": [
            ("Take the general rate as given",
             "The merchant's rate a year is the general rate of profit. Nothing in his own "
             "business changes it."),
            ("Count the turnovers",
             "Find how many times a year the merchant's capital buys and sells, on the "
             "average of his line of trade."),
            ("Divide",
             "The mark-up on each turnover is the annual rate divided by the turnovers."),
            ("Price one turnover and check the year",
             "Each lot sells at its purchase price times one plus the mark-up. The mark-ups "
             "of all the turnovers in a year add up to the annual rate on the capital."),
        ],
        "worked": {
            "title": "Marx's 100 at 15 per cent",
            "intro": [
                "A merchant advances 100 at a general rate of 15 per cent a year and turns "
                "his capital over five times. You want the mark-up on each sale and his profit "
                "for the year.",
            ],
            "lines": [
                "mark-up:  15% / 5 = 3% a turnover",
                "each sale:  100 · (1 + 3/100) = 103",
                "the year:  5 × 3 = 15 on 100 = 15%",
                "once a year:  100 · (1 + 15/100) = 115",
            ],
            "after": [
                "The fast merchant sells 500 of goods for 515, the slow one 100 for 115. Both "
                "earn 15 a year on 100, which is all the general rate allows either of them.",
            ],
        },
        "quiz_title": "Turnover and the mark-up",
        "quiz": [
            {"q": "The general rate of profit is 12% a year and a merchant turns his capital "
                  "over four times a year. What mark-up does he add to each sale?",
             "a": ["3%", "12%", "48%", "16%"],
             "c": 0,
             "why": "The mark-up is the annual rate divided by the turnovers, `12% / 4 = 3%`. "
                    "Twelve per cent is the mark-up for one turnover, 48 per cent multiplies, "
                    "and 16 per cent adds the turnovers to the rate."},
            {"q": "Two merchants each advance 100 at a general rate of 15%. One turns over "
                  "once a year, the other five times. What are their profits for the year?",
             "a": ["15 each",
                   "15 and 75",
                   "15 and 3",
                   "3 each"],
             "c": 0,
             "why": "Each earns the general rate on his capital, 15 on 100. Seventy-five "
                    "charges 15 per cent on every sale, which would draw capital into that "
                    "line until it stopped; 3 is one sale's mark-up, not the year's profit."},
            {"q": "On the chapter's account, which of these settles whether a merchant sells "
                  "“many commodities at a small profit” or few at a large one?",
             "a": ["The price of production of the goods, the general rate of profit and the "
                   "turnover of his line",
                   "The merchant's own pricing policy",
                   "The merchant's generosity to his customers",
                   "The rate of surplus value in his shop"],
             "c": 0,
             "why": "Marx says the merchant controls neither the price of production nor the "
                    "general rate, and the turnover of his line spreads the rate over his "
                    "sales. Policy and Roscher's &ldquo;prudence and humanity&rdquo; are what "
                    "he calls ridiculous, and the merchant's shop produces no surplus value."},
            {"q": "A merchant turns over faster than the average in his line of trade. What "
                  "does the chapter say he gets?",
             "a": ["An extra profit above the average",
                   "Exactly the average profit",
                   "A lower rate of profit",
                   "No profit until he slows down"],
             "c": 0,
             "why": "The law holds for the average turnover of the whole line. A merchant "
                    "above it makes an extra profit, Marx says, as an industrialist producing "
                    "under better conditions does, and may pay some of it as rent for a good "
                    "location."},
        ],
        "mistakes": [
            ("Thinking a faster-turning merchant earns a higher rate of profit",
             "For industrial capital a faster turnover means more labour exploited and more "
             "surplus value, so it is natural to expect the same of trade. But the merchant "
             "produces no surplus value, and his rate is the general rate. In the marx preset "
             "five turnovers bring 3 per cent each, 15 a year; in the once preset one turnover "
             "brings 15. The rate on the capital is 15 per cent either way."),
            ("Thinking the merchant chooses his margin",
             "A shopkeeper's “small profits and quick returns” sounds like a policy. Marx's "
             "point is that the margin follows from the price of production and the turnover "
             "of the trade, which no merchant sets; the motto describes the result."),
            ("Carrying the merchant's law over to industrial capital",
             "An industrial capital that turns over faster does produce more surplus value "
             "and raise the rate of profit. The inverse law of mark-up and turnover is "
             "particular to merchant's capital, for which the rate is given from outside."),
        ],
        "standard": (
            "Finish when you can find the mark-up per turnover.",
            "Given the general rate of profit a year and a merchant's turnovers, compute the "
            "mark-up on each sale and the price of one turnover's goods, and show that the "
            "annual rate on his capital is the general rate."
        ),
        "note": (
            "The lab leaves out the merchant's costs, as Marx does in this chapter, and "
            "applies the law to an average turnover. A single merchant's extra profit from a "
            "faster turnover than his line's, and the credit that lets merchants run ahead "
            "of consumption, are in the prose and not in the tiles."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 3, l. 2966-2968 (paying and receiving as a special department).
    # Inline: l. 2960 (purely technical movements), l. 2979 (money-exchange
    # from international commerce), l. 2983 (goldsmiths), l. 3004 (reserve
    # funds managed for the class), l. 3018 (a deduction from surplus value).
    {
        "slug": "money-dealing-capital",
        "title": "Money-Dealing Capital",
        "module": "Chapter 19 · Financial Capital",
        "one_line": "A capital that only keeps, pays and exchanges money for others adds no value and draws its profit, at the general rate, out of the same surplus value.",
        "summary": (
            "Every business pays out and takes in money, keeps a reserve and, if it trades "
            "abroad, changes coin. Chapter 19 watches those technical jobs become the "
            "business of a separate capital, the money-dealer's. Add a money-dealer's "
            "capital to the averaging of “Commercial Profit” and compute the new general "
            "rate, the dealer's share of profit and what the manufacturers give up."
        ),
        "key": [
            "money-dealing: paying, keeping, exchanging",
            "it creates no value",
            "its profit: a deduction from s",
            "rate = s / all capital, dealer's included",
            "the goods still sell at their value",
        ],
        "key_label": "Chapter 19 in five lines",
        "concepts_intro": (
            "The chapter is short and works by analogy with commercial capital. What the "
            "merchant does for commodities, the money-dealer does for money itself."
        ),
        "concepts": [
            ("Technical operations of money",
             "Receiving and paying, balancing accounts, keeping a hoard as a reserve, "
             "changing one country's coin for another's and dealing in bullion. Every capital "
             "must have them done, and none of them creates value."),
            ("Concentration",
             "Done by specialists for the whole capitalist class, the operations are "
             "cheaper and the reserves smaller, because one cashier's fund serves many "
             "businesses whose payments partly cancel."),
            ("A share of the average",
             "The money-dealer's capital earns the general rate like the merchant's. Its "
             "profit, Marx says, is a deduction from the surplus value, because it operates "
             "only with values already realised."),
        ],
        "read_title": "The cashier's work, then its profit",
        "read_intro": (
            "The passage comes early in the chapter, where Marx says what the money-dealer "
            "does and why it costs something without producing anything."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 19.</strong> &ldquo;This purely technical "
                  "labor of paying money and receiving money constitutes an employment by "
                  "itself, which necessitates the making of balances, the balancing of "
                  "accounts, so far as money serves as a means of payment. This labor belongs "
                  "to the expenses of circulation, it does not create any values. It is "
                  "abbreviated by being organised as a special department of agents, or "
                  "capitalists, who perform this work for all the rest of the capitalist "
                  "class.&rdquo;"),
            ("p", "A word on the name first. Untermann's translation calls this "
                  "&ldquo;financial capital&rdquo;, and the module keeps his chapter title. "
                  "Today &ldquo;finance&rdquo; suggests lending and investment banking, which "
                  "is exactly what Marx leaves out here: lending at interest is the next "
                  "Part's subject. So the lesson says money-dealing capital, which is what the "
                  "chapter describes, the &ldquo;purely technical movements performed by "
                  "money&rdquo;."),
            ("p", "Think of the payroll office of a large firm, or the payment processor "
                  "behind a card. Money comes in from many people and goes out to many others; "
                  "someone must count it, keep it, balance the accounts and hold enough in "
                  "reserve to meet the days when more goes out than comes in. In the passage "
                  "this is &ldquo;an employment by itself&rdquo;, a cost of circulation that "
                  "creates no value, and it is &ldquo;abbreviated&rdquo; when a special set of "
                  "agents does it for everyone. Abbreviated is the right word: the "
                  "money-dealer does not abolish the work, he makes it shorter."),
            ("p", "Where did the business start? Marx's answer is history, briefly told. "
                  "Money-changing came out of international trade, when merchants had to swap "
                  "one country's coin for another's or for bullion; out of it grew the banks "
                  "of exchange. Remittances between money-changers in different countries go "
                  "back to Greece and Rome. And &ldquo;In England, the goldsmiths still served "
                  "as bankers during the greater part of the 17th century.&rdquo; The other "
                  "root is the hoard every business keeps as a reserve. Managed for the class "
                  "as a whole, Marx notes, the reserves &ldquo;need not be so large as they "
                  "would have to be, did each capitalist manage his own.&rdquo;"),
            ("p", "Then the profit. A capital put into this business must earn the general "
                  "rate, or no one would put it there. Marx is brief: &ldquo;It is equally "
                  "evident, that the profit of the money dealers is nothing but a deduction "
                  "from the surplus-value, since they are operating merely with already "
                  "realised values&rdquo;. The lab puts the money-dealer's capital into the "
                  "averaging of “Commercial Profit”, beside the merchant's, and spreads the "
                  "same surplus value over the lot. It has one field for capital in "
                  "circulation, so the merchant's 100 and the dealer's capital are entered "
                  "together, and the lesson splits the profit between them by the common "
                  "rate."),
            ("p", "In the none preset there is no money-dealer: Marx's industrial 900 and "
                  "merchant's 100 give 18 per cent, and the manufacturers sell at £1,062. In "
                  "the cashier preset a cashier's capital of 125 joins them. The 180 of surplus "
                  "value is spread over 1,125, so the general rate is `4/25`, 16 per cent, and "
                  "the manufacturers sell at £1,044. The cashier draws `16% × 125 = 20` and "
                  "the merchant 16. In the exchange preset a money-changer's 75 joins the "
                  "cashier: 180 over 1,200 is `3/20`, 15 per cent, the manufacturers sell at "
                  "£1,035, and the two money-dealers draw `15% × 200 = 30` between them. In "
                  "every preset the goods reach their final buyers at £1,080, their value. "
                  "What moves is the split: each new capital in circulation takes its share "
                  "from what the others would otherwise have kept."),
            ("p", "That last fact is the lesson's arithmetic in one line. The money-dealer "
                  "does not raise the value of anything; the total profit is still 180, and "
                  "the manufacturers and the merchant lose between them exactly what the "
                  "dealers draw. In the "
                  "cashier preset the manufacturers take 144 and the circulation capitals 36, "
                  "against 162 and 18 in the none preset."),
            ("p", "Is there anything special about the money-dealer's circuit? Marx says "
                  "there is not. The merchant has his own form, `M–C–M′`, in which the same "
                  "commodity changes hands twice; the money-dealer has no special form of "
                  "circulation at all, only the general form of capital, money advanced and "
                  "returned with an increment. He promotes the technique of payment and does "
                  "not decide its volume: the cheques and bills that cancel in a clearing "
                  "house reflect transactions that happened anyway."),
            ("p", "The objection from modern economics is the one met in “Commercial "
                  "Profit”: payment services are services, priced like any other, and a "
                  "payments firm's fees are counted as output. Economists in Marx's own "
                  "tradition argue about whether a modern bank's revenue is a share of surplus "
                  "value, a payment for a cost of circulation or partly something else. The "
                  "lab computes the chapter's accounting and goes no further."),
            ("p", "Part IV ends with history. The next lesson, “Historical Facts about "
                  "Merchant's Capital”, asks how merchants profited before there was any "
                  "general rate of profit to share."),
        ],
        "lab": ("capkit", {
            "mode": "prices",
            "view": "merchant",
            "money_unit": "£",
            "preset": "cashier",
            "presets": [
                {"id": "none", "label": "No money-dealer: Marx's 900 and the merchant's 100",
                 "spheres": [{"name": "industry", "c": 720, "v": 180}],
                 "s_rate": 1, "merchant_capital": 100,
                 "expect": {"ppAverage": "9/50 = 18%",
                            "ppMerchantPrice": "industrial £1,062; merchant £1,080"}},
                {"id": "cashier", "label": "A cashier's 125 joins the merchant's 100",
                 "spheres": [{"name": "industry", "c": 720, "v": 180}],
                 "s_rate": 1, "merchant_capital": 225,
                 "expect": {"ppAverage": "4/25 = 16%",
                            "ppMerchantPrice": "industrial £1,044; merchant £1,080"}},
                {"id": "exchange", "label": "The cashier and a money-changer's 75",
                 "spheres": [{"name": "industry", "c": 720, "v": 180}],
                 "s_rate": 1, "merchant_capital": 300,
                 "expect": {"ppAverage": "3/20 = 15%",
                            "ppMerchantPrice": "industrial £1,035; merchant £1,080"}},
            ],
            "panel_title": "The money-dealer in the averaging",
            "panel_intro": (
                "Marx's industrial capital of 720c + 180v goes in with the capital held in "
                "circulation: the merchant's 100 plus any money-dealer's capital, entered as "
                "one figure. The tiles show the general rate and the prices at which the "
                "manufacturers and the last seller sell. The money-dealers' capitals are "
                "illustrative."
            ),
        }),
        "steps_title": "Sharing out surplus value with a money-dealer",
        "steps_intro": "Four steps, extending those of “Commercial Profit”.",
        "steps": [
            ("Add every capital in circulation",
             "Total the merchant's capital and the money-dealer's capital, and add them to "
             "the industrial capital."),
            ("Find the general rate",
             "Divide the surplus value of industry by the whole capital. The money-dealer's "
             "capital produces none of it and shares in all of it."),
            ("Give each capital its share",
             "Each capital draws the general rate on its own size: the manufacturers on "
             "theirs, the merchant on his, the money-dealer on his."),
            ("Check the totals",
             "The shares add up to the surplus value, and the goods still sell at their "
             "value. What the money-dealer draws, the manufacturers give up."),
        ],
        "worked": {
            "title": "A cashier among Marx's capitals",
            "intro": [
                "Industrial capital of 900 produces 180 of surplus value; the merchant holds "
                "100 and a cashier 125. You want the general rate and each capital's profit.",
            ],
            "lines": [
                "rate:  180 / (900 + 100 + 125) = 4/25 = 16%",
                "manufacturers:  16% × 900 = 144",
                "merchant:  16% × 100 = 16",
                "cashier:  16% × 125 = 20",
                "check:  144 + 16 + 20 = 180",
            ],
            "after": [
                "Without the cashier the manufacturers took 162 and the merchant 18. The "
                "cashier's 20 is their loss, 18 and 2, and the goods still sell at 1,080.",
            ],
        },
        "quiz_title": "The money-dealer's share",
        "quiz": [
            {"q": "Industrial capital of 900 produces 180 of surplus value. A merchant holds "
                  "100 and a money-dealer 200. What is the general rate of profit on Marx's "
                  "account?",
             "a": ["15%", "18%", "20%", "60%"],
             "c": 0,
             "why": "All three capitals share, `180 / 1,200 = 3/20`. Eighteen per cent leaves "
                    "the money-dealer out, 20 per cent leaves out all circulation capital, and "
                    "60 per cent divides by the circulation capital alone."},
            {"q": "At that rate, what profit does the money-dealer's 200 draw?",
             "a": ["30", "36", "40", "20"],
             "c": 0,
             "why": "`15% × 200 = 30`. Thirty-six uses the 18 per cent rate that held without "
                    "him, 40 the 20 per cent of industry alone, and 20 halves his capital."},
            {"q": "Which of these does Marx count among the money-dealer's operations in "
                  "Chapter 19?",
             "a": ["Keeping the reserve fund of means of payment",
                   "Lending money at interest to industrialists",
                   "Transporting goods to market",
                   "Producing gold"],
             "c": 0,
             "why": "Safekeeping the hoard, paying, receiving, balancing and exchanging coin "
                    "are his technical operations. Lending at interest is set aside for Part "
                    "V, transport is production continued in circulation, and gold is produced "
                    "by mining."},
            {"q": "In the cashier preset, at what price do the goods reach their final "
                  "buyers?",
             "a": ["£1,080, their value", "£1,205, value plus the cashier's capital",
                   "£1,100, value plus the cashier's profit", "£1,044"],
             "c": 0,
             "why": "The dealer's profit comes out of the existing surplus value, so the "
                    "final price stays at the value. £1,044 is the manufacturers' price to the "
                    "merchant, and the other two add the dealer to the value."},
        ],
        "mistakes": [
            ("Thinking money-dealing creates value because it handles value",
             "Money-dealers handle large sums, and large sums look productive. But handling "
             "realised values does not add to them. In the cashier preset the goods still "
             "sell at £1,080 and the total profit is still 180; the cashier's 20 appears "
             "only because the manufacturers now sell at £1,044 instead of £1,062."),
            ("Reading “financial capital” as lending capital",
             "Untermann's term suggests banking in the modern sense. Chapter 19 is about the "
             "technical work of payments, reserves and exchange, and keeps lending out; "
             "interest-bearing capital begins with “Interest-Bearing Capital”."),
            ("Thinking the money-dealer decides how much is paid",
             "He concentrates and shortens the work of payment and reduces the reserves "
             "needed. The volume and connections of payments are set by the trade in "
             "commodities, Marx says, not by the money trade."),
        ],
        "standard": (
            "Finish when you can share out surplus value with a money-dealer in the averaging.",
            "Given industrial capital, its surplus value, the merchant's capital and a "
            "money-dealer's capital, compute the general rate of profit, the profit each "
            "capital draws and the price at which the manufacturers sell."
        ),
        "note": (
            "Marx gives no figures in this chapter. The cashier's 125 and the "
            "money-changer's 75 are illustrative, and the lab enters them with the "
            "merchant's 100 in one field for capital in circulation; the split between "
            "merchant and dealer is computed in the prose at the common rate. The tile "
            "labelled merchant is the last seller's price, whoever holds the capital."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 3, l. 3079 (the intervening movement between extremes).
    # Inline: l. 3061 (reduced to the general average), l. 3065 (inverse
    # ratio), l. 3077 (profit upon alienation; buy cheap, sell dear), l. 3089
    # (a system of robbery), l. 3101 (industry revolutionises commerce; the
    # decline of Holland), l. 3105 (the really revolutionary way), l. 3119
    # (interest-bearing capital likewise a very old form).
    {
        "slug": "history-of-merchants-capital",
        "title": "Historical Facts about Merchant's Capital",
        "module": "Chapter 20 · Historical Data Concerning Merchants' Capital",
        "one_line": "Before capitalist production, the merchant's profit came from buying cheap in one community and selling dear in another, and no general rate limited it.",
        "summary": (
            "Merchant's capital is older than capitalist production, and for most of its "
            "history its profit was not a share of any average. Compute the gain of a "
            "carrying trader who buys in one community and sells in another, beside the "
            "share of a capitalist merchant held to a general rate, and follow Marx's "
            "argument that trade dissolved old modes of production without deciding what "
            "replaced them."
        ),
        "key": [
            "M–C–M′: the oldest free form of capital",
            "profit upon alienation: buy cheap, sell dear",
            "buy at 60, sell at 100: +40",
            "a capitalist merchant: 18 on 100",
            "commerce dissolves; it does not decide",
        ],
        "key_label": "Chapter 20 in five lines",
        "concepts_intro": (
            "Chapters 16 to 19 placed the merchant inside capitalist production. Chapter 20 "
            "steps outside it, into the long history in which the merchant came first."
        ),
        "concepts": [
            ("Profit upon alienation",
             "Where production is not yet for the market, the merchant compares prices "
             "between communities and pockets the difference. His profit is made in "
             "circulation, by buying cheap and selling dear, not shared out of a surplus "
             "value produced under his control."),
            ("The inverse ratio",
             "The more merchant's capital dominates on its own, the less developed "
             "production is. The great trading cities lived by carrying goods between "
             "producers who did not trade with each other directly."),
            ("Two roads out of feudalism",
             "Either the producer becomes a merchant and capitalist, which Marx calls the "
             "really revolutionary way, or the merchant takes over production and leaves its "
             "methods as they were."),
        ],
        "read_title": "One sentence, then a history",
        "read_intro": (
            "The sentence is short and comes after Marx has described the merchant's "
            "profit in the old trading world. The chapter around it is a survey from Carthage "
            "to Victorian London."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 20.</strong> &ldquo;The merchants' capital "
                  "is at first merely the intervening movement between extremes not "
                  "controlled by it and between premises not created by it.&rdquo;"),
            ("p", "The &ldquo;extremes&rdquo; are the producers at either end of a trade: a "
                  "village that grows grain, a city that makes cloth, a court that collects "
                  "tribute and wants silk. The merchant controls neither end and did not create "
                  "either. He only moves between them. Marx's point in the chapter is that "
                  "this is the shape merchant's capital has for most of its history, and that "
                  "it is the oldest free existence of capital: buying in order to sell, "
                  "`M–C–M′`, long before anyone bought labour-power in order to produce."),
            ("p", "How does such a merchant profit? Not by sharing an average rate, because "
                  "there is none. &ldquo;It is a profit upon alienation.&rdquo; The quantities "
                  "in which different communities' products exchange are at first arbitrary, "
                  "and the merchant, who alone sees both prices, buys where goods are cheap and "
                  "sells where they are dear: &ldquo;To buy cheap in order to sell dear is the "
                  "rule of trade.&rdquo; By doing it again and again he gradually brings prices "
                  "toward each other, and so, in Marx's phrase, by his own movements he "
                  "establishes the equivalence of commodities."),
            ("p", "The lab writes the merchant's circuit and computes what comes back. In the "
                  "venice preset a carrying trader buys a lot for £60 in one community and "
                  "sells it for £100 in another: `+£40`, two-thirds on his outlay, and nothing "
                  "pulls it towards anyone else's rate. In the dutch preset a company with a "
                  "monopoly at both ends buys for £25 and sells for £100: `+£75`. In the "
                  "capitalist preset the merchant of “Commercial Profit” lays out £100 and "
                  "gets back £118, 18 per cent, the general rate. The circuit is `M–C–M′` "
                  "every time. What changed between the first two presets and the third is "
                  "not the form but what limits the increment."),
            ("p", "Marx does not romanticise the old merchant. Between undeveloped "
                  "societies, he writes, commercial profit arises largely from out-bargaining "
                  "and cheating, and &ldquo;Merchants' capital in its supremacy everywhere "
                  "stands for a system of robbery&rdquo;, connected with piracy, the slave "
                  "trade and the conquest of colonies; Carthage, Rome, the Venetians, "
                  "Portuguese and Dutch are his list. The venice and dutch presets name the "
                  "kind of trade, not a historical price: Marx quotes none, and the figures "
                  "are illustrative."),
            ("p", "Then the rule that organises the chapter: &ldquo;The independent "
                  "development of merchants' capital stands therefore in an inverse ratio to "
                  "the general economic development of society.&rdquo; The carrying trade of "
                  "the Venetians, Genoese and Dutch flourished on the backwardness of the "
                  "peoples at either end, and declined as those peoples developed. "
                  "&ldquo;The history of the decline of Holland as the ruling commercial nation "
                  "is the history of the subordination of merchants' capital to industrial "
                  "capital.&rdquo; Within capitalist production, the merchant's rate is "
                  "reduced to the general average, which is the capitalist preset."),
            ("p", "Did trade make capitalism? The question has a famous history. The Belgian "
                  "historian Henri Pirenne argued in the 1920s that the revival of "
                  "long-distance trade rebuilt Europe's towns, and in the 1950s the American "
                  "economist Paul Sweezy, debating the British economist Maurice Dobb, made "
                  "trade the solvent of feudalism. What in the chapter bears on their debate "
                  "is that Marx grants trade a great deal: the discoveries of the sixteenth and seventeenth centuries and the sudden "
                  "world market helped destroy feudal barriers. But he denies that trade "
                  "decides what comes next. In the ancient world it led to slave economies; "
                  "in the modern world, to capitalism; and Russian commerce left Asian "
                  "production untouched. Once modern industry exists, &ldquo;it is not "
                  "commerce in this case which revolutionises industry, but industry which "
                  "continually revolutionises commerce.&rdquo; Dobb, and later Robert Brenner, "
                  "read the transition from relations inside agriculture rather than from "
                  "trade, and the dispute continues among historians."),
            ("p", "Marx ends with the two roads. The producer may become a merchant and "
                  "capitalist: &ldquo;This is the really revolutionary way.&rdquo; Or the "
                  "merchant may take over production, like the English clothier who sells "
                  "wool to weavers and buys back their cloth, leaving them to work in the old "
                  "way and squeezing them harder. His Victorian example is the London "
                  "furniture trade, where small masters sell their chairs and tables every "
                  "Saturday to the furniture-store owners with as much haggling as a pawnshop, and "
                  "the merchant is the real capitalist."),
            ("p", "That closes Part IV. Part V begins with a capital that is, as Marx says at "
                  "the chapter's end, &ldquo;likewise a very old form of capital&rdquo;, and one "
                  "even further from production. The next lesson, "
                  "“Interest-Bearing Capital”, asks what a lender sells when he lends £100."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "formula",
            "money_unit": "£",
            "preset": "venice",
            "presets": [
                {"id": "venice", "label": "A carrying trader buys at £60 and sells at £100",
                 "start": "money", "M": 60, "product": 100,
                 "expect": {"ciForm": "M–C–M′", "ciDelta": "+£40"}},
                {"id": "dutch", "label": "A monopoly company buys at £25 and sells at £100",
                 "start": "money", "M": 25, "product": 100,
                 "expect": {"ciDelta": "+£75"}},
                {"id": "capitalist", "label": "A capitalist merchant held to the 18% average",
                 "start": "money", "M": 100, "product": 118,
                 "expect": {"ciForm": "M–C–M′", "ciDelta": "+£18"}},
            ],
            "panel_title": "The merchant's circuit, before and after the average",
            "panel_intro": (
                "The money the merchant lays out and the money his goods bring back go in. "
                "The tiles show the form of the circuit and the increment. The first two "
                "presets are illustrative kinds of trade, not historical prices; the third is "
                "the 18 per cent of “Commercial Profit”."
            ),
        }),
        "steps_title": "Reading a merchant's gain",
        "steps_intro": "Four steps for any merchant, old or modern.",
        "steps": [
            ("Write the circuit",
             "Money laid out, goods bought, goods sold: `M–C–M′`. The merchant starts and "
             "ends with money."),
            ("Compute the increment",
             "The gain is the money returned less the money laid out, and the rate on the "
             "outlay is the gain divided by the outlay."),
            ("Ask where the price gap comes from",
             "Between communities that do not otherwise trade, the gap is the difference "
             "between two prices the merchant alone compares. Within capitalist production, "
             "it is the manufacturer's sale below value."),
            ("Ask what limits it",
             "With no general rate, nothing but the gap and the merchant's power limits the "
             "gain. With a general rate, competition holds the merchant to it."),
        ],
        "worked": {
            "title": "A carrying trader and a capitalist merchant",
            "intro": [
                "One merchant buys at £60 in one community and sells at £100 in another. A "
                "capitalist merchant lays out £100 at a general rate of 18 per cent. You want "
                "each one's gain and rate on outlay.",
            ],
            "lines": [
                "carrying trader:  £100 − £60 = £40",
                "his rate:  40 / 60 = 2/3",
                "capitalist merchant:  £118 − £100 = £18",
                "his rate:  18 / 100 = 9/50 = 18%",
            ],
            "after": [
                "Both circuits are `M–C–M′`. The first gain is limited only by the gap between "
                "two communities' prices; the second is the share of a surplus value that the "
                "general rate allots to £100.",
            ],
        },
        "quiz_title": "Merchants before and after the average",
        "quiz": [
            {"q": "A carrying trader buys goods for £50 and sells them for £80. What is his "
                  "rate of gain on the outlay?",
             "a": ["3/5 = 60%", "3/8 = 37.5%", "30%", "8/5 = 160%"],
             "c": 0,
             "why": "The gain is `£80 − £50 = £30`, and `30 / 50 = 3/5`. Three-eighths "
                    "divides by the sale price, 30 per cent reads the gain in pounds as a "
                    "percentage, and 160 per cent is the money returned over the money laid "
                    "out."},
            {"q": "On Marx's account, what limits the carrying trader's gain in a world "
                  "without capitalist production?",
             "a": ["Nothing but the gap between the prices and his power to exploit it",
                   "The general rate of profit",
                   "The value his transport adds to the goods",
                   "The wages he pays his crews"],
             "c": 0,
             "why": "There is no general rate yet: the profit is a profit upon alienation, "
                    "made by buying cheap and selling dear. The general rate arrives with "
                    "capitalist production, transport is set aside, and the crews' wages are "
                    "a cost, not a limit."},
            {"q": "Which statement matches Chapter 20's rule?",
             "a": ["Independent merchant's capital flourishes most where production is least "
                   "developed",
                   "Merchant's capital grows in step with the development of production",
                   "Merchant's capital caused the capitalist mode of production by itself",
                   "Merchant's capital disappears under capitalist production"],
             "c": 0,
             "why": "Marx states an inverse ratio between the independent development of "
                    "merchant's capital and general economic development. He denies that trade "
                    "by itself explains the transition, and under capitalism merchant's "
                    "capital survives as a capital with a special function."},
            {"q": "Which of Marx's two roads out of feudal production does he call “the "
                  "really revolutionary way”?",
             "a": ["The producer becomes a merchant and capitalist",
                   "The merchant takes direct possession of production",
                   "The state organises production for export",
                   "The guilds merge into companies"],
             "c": 0,
             "why": "Marx's words are &ldquo;This is the really revolutionary way&rdquo; of "
                    "the producer becoming merchant and capitalist. The merchant who takes "
                    "over production, like the English clothier, preserves the old methods. "
                    "The other two are not among his roads."},
        ],
        "mistakes": [
            ("Thinking a merchant's profit is always a share of an average rate of profit",
             "That is true inside capitalist production, as “Commercial Profit” showed, and "
             "it is easy to read it back into all history. Marx's chapter says the reverse "
             "held for most of it. In the venice preset the trader's £40 on £60 is two-thirds "
             "of his outlay and in the dutch preset £75 on £25 is three times it; no average "
             "draws either toward the capitalist preset's £18 on £100."),
            ("Thinking trade by itself produced capitalism",
             "Marx grants that the world market of the sixteenth and seventeenth centuries "
             "helped dissolve feudal production. What replaced it depended on the old mode "
             "of production, he argues: slave economies in antiquity, capitalism in modern "
             "Europe, and little change where Russian commerce met Asian production."),
            ("Reading the old merchant's profit as an exchange of equivalents",
             "Between undeveloped communities the ratios of exchange are at first "
             "arbitrary, and the merchant's profit is made from the gap, often by "
             "out-bargaining and cheating, in Marx's words. Equivalence is what his trade "
             "gradually brings about, not where it starts."),
        ],
        "standard": (
            "Finish when you can compute a merchant's gain with and without a general rate.",
            "Given a merchant's outlay and returns, compute his gain and its rate on outlay, "
            "and state whether a general rate of profit limits it."
        ),
        "note": (
            "The circuit tile sees only money out and money back. It cannot show where a "
            "price gap came from, whether a rate is a share of an average, or the history "
            "Marx tells; those are the prose's. The venice and dutch figures are "
            "illustrative kinds of trade, and the debate over trade and the transition from "
            "feudalism is a historians' dispute this lesson only names."
        ),
    },
]
