"""From Money to Surplus Value, lessons 1-5 -- Volume I, Chapters 4 to 8.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals in the text are left out of the quotations, a
drop capital ("THE", "IT") is printed as an ordinary capital, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 1, l. 1477-1479 (the two circulations; "no limits"); l. 1441
    # (2000 lbs. of cotton for £100, resold for £110); l. 1463 (corn and
    # clothes); l. 1455, 1469, 1481, 1485, 1495 (phrases).
    {
        "slug": "the-general-formula-for-capital",
        "title": "The General Formula for Capital",
        "module": "Chapter 4 · The General Formula for Capital",
        "one_line": "Selling in order to buy ends in a use-value; buying in order to sell starts and ends with money, and makes sense only if more money comes back.",
        "summary": (
            "Chapter 4 sets two circuits side by side: C–M–C, selling in order to buy, and "
            "M–C–M, buying in order to sell. Tell them apart by what stands at either end, "
            "and compute the increment ΔM that is the only reason to run the second one at "
            "all: Marx's £100 of cotton that sells for £110."
        ),
        "key": [
            "C–M–C: sell in order to buy",
            "M–C–M′: buy in order to sell dearer",
            "ΔM = money at the end − money at the start",
            "M′ = M + ΔM; Marx calls ΔM surplus value",
            "C–M–C ends in use; M–C–M′ has no end",
        ],
        "key_label": "Two circuits in five lines",
        "concepts_intro": (
            "Part II is called “The Transformation of Money into Capital”, and Chapter 4 "
            "does the first half of that job: it says what form money must move in before "
            "it can be called capital at all."
        ),
        "concepts": [
            ("Two circuits",
             "C–M–C is a sale followed by a purchase: a commodity becomes money and the "
             "money becomes another commodity. M–C–M is a purchase followed by a sale. The "
             "same two acts, in the opposite order."),
            ("The increment",
             "Both ends of M–C–M are money, and one sum of money differs from another only "
             "in amount. So the circuit has a point only if the money at the end exceeds the "
             "money at the start. Marx writes it M–C–M′ and calls the excess surplus value."),
            ("Value in process",
             "In M–C–M′ value keeps changing form, money then commodity then money, and "
             "grows as it goes. Money that moves this way is capital, and its owner, so far "
             "as he follows it, is a capitalist."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "The passage comes from the middle of the chapter, where Marx sums up the "
            "difference between the two circuits. The rest of the lesson goes back to how "
            "he gets there."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 4.</strong> &ldquo;The simple circulation of "
                  "commodities&mdash;selling in order to buy&mdash;is a means for carrying out "
                  "a purpose unconnected with circulation, namely, the appropriation of "
                  "use-values, the satisfaction of wants. The circulation of money as capital "
                  "is, on the contrary, an end in itself, for the expansion of value takes "
                  "place only within this constantly renewed movement. The circulation of "
                  "capital has therefore no limits.&rdquo;"),
            ("p", "You know the first circuit from your own life. You sell something you no "
                  "longer need, an old bicycle say, and spend the money on something you do. "
                  "Thing, money, thing. Marx's version is a peasant: &ldquo;If I sell a "
                  "quarter of corn for £3, and with this £3 buy clothes, the money, so far as "
                  "I am concerned, is spent and done with.&rdquo; The money was only a "
                  "go-between. What you wanted was the clothes, and once you have them the "
                  "circuit is over."),
            ("p", "Now turn it round. Marx's merchant begins with money:"),
            ("p", "<strong>Volume I, Chapter 4.</strong> &ldquo;If I purchase 2000 lbs. of "
                  "cotton for £100, and resell the 2000 lbs. of cotton for £110, I have, in "
                  "fact, exchanged £100 for £110, money for money.&rdquo;"),
            ("p", "Look first at what the two circuits share. Each is made of the same two "
                  "acts, a sale and a purchase, and each needs three people: one who only "
                  "sells, one who only buys, and one who does both. Nothing new has been added "
                  "to the market. What differs is the order. C–M–C begins with a sale and ends "
                  "with a purchase; M–C–M begins with a purchase and ends with a sale."),
            ("p", "That inversion changes what moves. In C–M–C the same coin changes hands "
                  "twice, from the corn-buyer to the peasant and from the peasant to the "
                  "clothes-dealer, and it does not come back. In M–C–M it is the cotton that "
                  "changes hands twice, and the money flows back to where it started. The "
                  "merchant &ldquo;lets the money go, but only with the sly intention of "
                  "getting it back again&rdquo;. It is not spent; it is advanced."),
            ("p", "Then the decisive step. The two ends of C–M–C are different use-values, "
                  "corn and clothes, and that difference is the whole point of the exchange. "
                  "The two ends of M–C–M are money, and money in one hand is the same as money "
                  "in another. To exchange £100 for cotton and the cotton for £100 is, Marx "
                  "says, &ldquo;merely a roundabout way of exchanging money for money, the same "
                  "for the same&rdquo;. So the circuit can only be about quantity. Its full "
                  "form is M–C–M′, where M′ is M plus an increment, and the increment Marx "
                  "names surplus value. Here the name is all there is; where the £10 comes "
                  "from is the question of the next six chapters."),
            ("def", ("Surplus value",
                     "The excess of the money withdrawn from circulation at the end of M–C–M′ "
                     "over the money thrown into it at the start: ΔM = M′ − M. In Marx's "
                     "example, £10 on £100.")),
            ("p", "Because it is about quantity, the second circuit has no natural end. The "
                  "peasant stops when he has his clothes. The £110 that comes back to the "
                  "merchant is a sum of money just as the £100 was, and has exactly the same "
                  "reason to go out again. Marx draws the comparison with the hoarder of "
                  "Chapter 3: both chase exchange value without limit, &ldquo;but while the "
                  "miser is merely a capitalist gone mad, the capitalist is a rational "
                  "miser&rdquo;. One keeps the money out of circulation to save it; the other "
                  "keeps throwing it back in."),
            ("p", "Seen this way, the subject of the movement is not the man but the value. It "
                  "is money, then cotton, then money, and through all the changes it keeps "
                  "itself and grows. Marx lets himself enjoy the image: value has acquired "
                  "&ldquo;the occult quality of being able to add value to itself. It brings "
                  "forth living offspring, or, at the least, lays golden eggs.&rdquo; The "
                  "capitalist is the person through whose pocket this movement runs, "
                  "&ldquo;capital personified and endowed with consciousness and a will&rdquo;."),
            ("p", "The formula covers more than merchants. Industrial capital also turns money "
                  "into commodities and sells the result for more money; what happens in the "
                  "factory between the purchase and the sale does not change the form. "
                  "Interest-bearing capital shortens it to M–M′, money that is worth more "
                  "money, &ldquo;en style lapidaire&rdquo;. That is why Marx calls M–C–M′ the "
                  "general formula, adding carefully that it is capital &ldquo;as it appears "
                  "prima facie within the sphere of circulation&rdquo;."),
            ("p", "A reader trained in economics will want to object here, and the objection "
                  "is a good one. A merchant who buys cotton in Liverpool and sells it in "
                  "Manchester has moved it, stored it and borne the risk that the price would "
                  "fall; on the ordinary account his £10 is the price of those services and "
                  "of waiting, and there is nothing mysterious in it. Marx does not answer "
                  "that in Chapter 4. He only fixes the form and insists that the increment be "
                  "explained, not assumed. The next chapter tests whether buying and selling "
                  "can explain it."),
            ("p", "The lab computes the one quantity the chapter defines. Choose the corn and "
                  "the circuit reads C–M–C with no difference in money, and nothing is wrong: "
                  "the peasant has his clothes. Choose the cotton and it reads M–C–M′ with "
                  "+£10. Let the cotton go for £90 and the same form shows −£10: the circuit "
                  "still has its shape, and it has failed."),
            ("p", "So capital is money that comes back as more money. The next lesson, "
                  "“Contradictions in the General Formula”, asks whether the extra can come "
                  "from buying and selling itself."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "formula",
            "money_unit": "£",
            "preset": "cmc",
            "presets": [
                {"id": "cmc", "label": "Marx's peasant: corn sold for £3, clothes bought for £3",
                 "start": "commodity", "M": 3, "product": 3, "expect": {"ciForm": "C–M–C", "ciDelta": "£0"}},
                {"id": "mcm", "label": "Marx's merchant: £100 of cotton resold for £110",
                 "start": "money", "M": 100, "product": 110, "expect": {"ciForm": "M–C–M′", "ciDelta": "+£10"}},
                {"id": "mcm-loss", "label": "The same cotton let go for £90",
                 "start": "money", "M": 100, "product": 90, "expect": {"ciForm": "M–C–M′", "ciDelta": "−£10"}},
            ],
            "panel_title": "Which circuit, and what comes back",
            "panel_intro": (
                "Say where the circuit starts, the money laid out and the money received. For "
                "C–M–C the money received is the price of what was sold and the money laid out "
                "is the price of what was bought. The lab names the circuit and subtracts."
            ),
        }),
        "steps_title": "Reading a circuit",
        "steps_intro": "Four steps for any sequence of a sale and a purchase.",
        "steps": [
            ("Find the two ends",
             "Write the sequence in order and look at its first and last terms. Commodities at "
             "both ends is C–M–C; money at both ends is M–C–M."),
            ("Name the aim",
             "In C–M–C the aim is the use-value bought at the end. In M–C–M the ends are the "
             "same kind of thing, so the aim can only be a larger sum."),
            ("Compute the increment",
             "ΔM is the money at the end less the money at the start. In C–M–C it is a matter "
             "of accident; in M–C–M it is the whole point."),
            ("Check the outcome",
             "A positive ΔM is the circuit succeeding; zero or a negative figure is M–C–M "
             "completed and failed. The form is the same either way."),
        ],
        "worked": {
            "title": "Corn and clothes, cotton and cash",
            "intro": [
                "Take Marx's two examples. A peasant sells a quarter of corn for £3 and buys "
                "clothes with it. A merchant buys 2000 lb of cotton for £100 and sells it for "
                "£110. You want each circuit's name and its increment.",
            ],
            "lines": [
                "peasant:  corn → £3 → clothes",
                "ends: two commodities, so C–M–C",
                "merchant:  £100 → cotton → £110",
                "ends: two sums of money, so M–C–M′",
                "ΔM = £110 − £100 = +£10",
            ],
            "after": [
                "The peasant's circuit is complete and successful with no money left over. "
                "The merchant's would be pointless at £100 and a failure at £90; it is a "
                "success only because of the £10, which the chapter names and does not yet "
                "explain.",
            ],
        },
        "quiz_title": "Selling to buy and buying to sell",
        "quiz": [
            {"q": "A household sells its old car for £3,000 and spends the £3,000 on a new "
                  "kitchen. On the chapter's terms, which circuit is this?",
             "a": ["M–C–M′, because money stands in the middle",
                   "C–M–C: it starts and ends with commodities, and its aim is a use-value",
                   "M–C–M′ with an increment of £0",
                   "Neither, because no money is left over at the end"],
             "c": 1,
             "why": "The sequence is car, money, kitchen: a sale and then a purchase, with "
                    "commodities at both ends. Money in the middle is what every C–M–C has. It "
                    "is not M–C–M at all, with or without an increment, and money left over is "
                    "not what defines either circuit."},
            {"q": "A dealer buys cloth for £200 and sells it for £230. What is ΔM?",
             "a": ["£230", "+£15", "£200", "+£30"],
             "c": 3,
             "why": "ΔM is the money at the end less the money at the start, `£230 − £200 = "
                    "£30`. The other figures are one end of the circuit or half the increment."},
            {"q": "Why does Marx say that M–C–M would be &ldquo;absurd and without "
                  "meaning&rdquo; if £100 came back as £100?",
             "a": ["Both ends are money, so only a difference in amount can give the circuit "
                   "a point",
                   "Money cannot buy cotton at its value",
                   "The merchant would have lost the £100",
                   "Circulation always adds a tenth to every sum"],
             "c": 0,
             "why": "Corn and clothes differ as use-values, so C–M–C has a point at equal "
                    "values. Money and money differ only in amount. The merchant at £100 has "
                    "lost nothing, which is why the circuit is pointless rather than ruinous, "
                    "and nothing in the chapter says circulation adds anything."},
            {"q": "In C–M–C the same piece of money changes hands twice. What changes hands "
                  "twice in M–C–M?",
             "a": ["The same piece of money", "The commodity", "Labour-power", "Nothing does"],
             "c": 1,
             "why": "The merchant takes the cotton from one seller and passes it to another "
                    "buyer, and that double move brings his money back. The money he pays out "
                    "and the money he receives are different coins from different people. "
                    "Labour-power has not appeared yet; it is the subject of Chapter 6."},
        ],
        "mistakes": [
            ("Treating selling to buy and buying to sell as one circulation",
             "The two are made of the same acts, so it is easy to think they are the same "
             "circuit entered at different points. The lab separates them by what counts as "
             "success. The corn preset shows a difference in money of £0, and the circuit has "
             "done all it was for. Set the cotton to £100 in and £100 out and the same "
             "difference of £0 makes the merchant's circuit pointless; at £90 it shows −£10 "
             "and has failed. One circuit aims at a use-value, the other at a larger sum."),
            ("Reading the £110 as two sums",
             "Once the cotton is sold, the merchant does not hold £100 of capital and £10 of "
             "surplus value side by side. He holds £110, which is ready to go out again exactly "
             "as the £100 was. That is why Marx says the movement has no limits."),
            ("Taking the formula for an explanation",
             "M–C–M′ says what capital looks like in circulation. It does not say where ΔM "
             "comes from, and Marx says plainly that the form is how capital appears "
             "&ldquo;prima facie&rdquo;. The explanation takes the next six chapters."),
        ],
        "standard": (
            "Finish when you can classify a circuit and compute its increment.",
            "Given a sale and a purchase in sequence, name the circuit as C–M–C or M–C–M′ "
            "from what stands at its two ends, and compute ΔM as the money at the end less "
            "the money at the start."
        ),
        "note": (
            "The lab subtracts one sum of money from another. It cannot say where the £10 "
            "came from, and Chapter 4 does not either: on the ordinary account it pays for "
            "carriage, storage, risk and waiting. Marx's general answer begins once labour-power "
            "is on the market; his account of the merchant's own share waits for Volume III. The corn and the cotton are Marx's figures; the £90 is his "
            "&ldquo;or lets it go for £100, or even £50&rdquo; made specific."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 1, l. 1564 (in circulation and not in circulation); l. 1544
    # (wine at £40, corn at £50); l. 1529 (10% dear); l. 1511, 1519-1521
    # (Condillac); l. 1540, 1552, 1562, 1570 (phrases).
    {
        "slug": "contradictions-in-the-general-formula",
        "title": "Contradictions in the General Formula",
        "module": "Chapter 5 · Contradictions in the General Formula of Capital",
        "one_line": "If everyone sells dear, everyone also buys dear, and one trader's gain from a cheat is another's loss: circulation moves value about without adding any.",
        "summary": (
            "Marx tests every way buying and selling might create surplus value and finds "
            "that none does. Compute the values held before and after when every seller "
            "marks up 10%, when one trader cheats another, and when three dealers who mark "
            "up trade with a producer who does not: the total never changes, only who holds it."
        ),
        "key": [
            "equivalents exchanged: no gain in value",
            "if all sell 10% dear, all buy 10% dear",
            "A cheats B: what A gains, B loses",
            "total held: the same before and after",
            "s arises in and not in circulation",
        ],
        "key_label": "Why circulation adds nothing",
        "concepts_intro": (
            "The chapter is a process of elimination. Each case is a way someone has "
            "thought profit could arise in trade, and each is answered with a sum."
        ),
        "concepts": [
            ("Gain in use-value",
             "Two traders can both be better off after an exchange, because each gets "
             "something more useful to him than what he gave up. That is a gain in use-value, "
             "and Marx grants it at once."),
            ("No gain in value",
             "If equal values are exchanged, nobody ends with more value than he began with. "
             "If unequal values are exchanged, one gains exactly what the other loses. Either "
             "way the sum of values in circulation is unchanged."),
            ("The double condition",
             "So surplus value cannot arise in circulation, and a producer alone with his "
             "goods cannot make value expand either. It must arise in circulation and not in "
             "circulation: that is the riddle the next chapter solves."),
        ],
        "read_title": "The conclusion first, then the cases that lead to it",
        "read_intro": (
            "The passage is the chapter's verdict, from its closing paragraphs. The lesson "
            "then works back through the cases Marx eliminates on the way."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 5.</strong> &ldquo;It is therefore impossible "
                  "for capital to be produced by circulation, and it is equally impossible for "
                  "it to originate apart from circulation. It must have its origin both in "
                  "circulation and yet not in circulation.&rdquo;"),
            ("p", "The explanation of profit that comes first to most people is the one Marx "
                  "takes first: the seller charges more than the thing is worth. Shops mark "
                  "goods up; a merchant buys cheap and sells dear. If that were the source, "
                  "the £10 of the last lesson would need no further explanation. The chapter "
                  "is an argument that it cannot be the source, for the capitalist class as a "
                  "whole."),
            ("p", "Marx starts by granting what is true in the idea. In an exchange both "
                  "parties can gain in use-value. A wine-grower who trades with a farmer may "
                  "get more corn than he could have grown with the same labour, and the farmer "
                  "more wine. Étienne Bonnot de Condillac, the eighteenth-century French "
                  "philosopher, built a theory of trade on this: value lies in a thing's "
                  "relation to our wants, so each side gives less for more, and both gain. "
                  "Marx's reply is that Condillac has run use-value and exchange value together, "
                  "and, to the later economists who used the argument to show that commerce adds "
                  "value, that &ldquo;commodities are not paid for twice over, once on account of "
                  "their use-value, and again on account of their value.&rdquo;"),
            ("p", "So suppose instead that sellers can sell above value. Every seller marks "
                  "up 10%, so what is worth 100 sells for 110. But every seller is also a "
                  "buyer, and pays 10% too much in turn: &ldquo;Our friend gained 10 as a "
                  "seller only to lose it again as a buyer.&rdquo; A general rise of prices "
                  "changes nothing real, Marx says, any more than pricing everything in silver "
                  "instead of gold would. The opposite assumption, that buyers can buy below "
                  "value, fails the same way, because every buyer was first a seller."),
            ("p", "Colonel Robert Torrens, the economist and soldier, put the claim in a form "
                  "that seems to escape: consumers pay more than goods cost to produce. Marx "
                  "answers that the consumer's money was itself the price of something he "
                  "sold. To make the claim work you need a class that only buys and never "
                  "sells, and such a class gets its money from somewhere. His example is the "
                  "towns of Asia Minor, which paid a yearly tribute to Rome and then sold the "
                  "Romans goods too dear: &ldquo;Their goods were still paid for with their own "
                  "money.&rdquo;"),
            ("p", "That leaves cheating, which certainly happens. Marx takes it seriously:"),
            ("p", "<strong>Volume I, Chapter 5.</strong> &ldquo;Before the exchange we had "
                  "£40 worth of wine in the hands of A, and £50 worth of corn in those of B, a "
                  "total value of £90. After the exchange we have still the same total value "
                  "of £90. The value in circulation has not increased by one iota, it is only "
                  "distributed differently between A and B.&rdquo;"),
            ("p", "A has made £10, and B has lost it; the same would have happened &ldquo;if A, "
                  "without the formality of an exchange, had directly stolen the £10 from "
                  "B&rdquo;. A single capitalist can grow rich this way. The class cannot, "
                  "because the sum it is dividing does not grow: &ldquo;The capitalist class, "
                  "as a whole, in any country, cannot over-reach themselves.&rdquo;"),
            ("p", "This is why Marx sets merchants' capital and money-lenders' capital aside "
                  "for now, though they are the oldest forms of capital. Explained by "
                  "circulation alone, merchants' capital would be cheating on both sides, "
                  "which is Benjamin Franklin's &ldquo;war is robbery, commerce is generally "
                  "cheating&rdquo;, and usury would be what Aristotle called it, the most "
                  "unnatural way of getting a living. Marx promises a better account of both "
                  "once the basic form is explained."),
            ("p", "Could value expand outside circulation, then? A producer alone with his "
                  "goods can add value by adding labour, turning leather into boots. But the "
                  "leather's value has not expanded itself; new labour has been added to it. "
                  "Nothing in the producer's relation to his own commodity makes a value "
                  "&ldquo;greater than itself&rdquo;."),
            ("p", "Hence the double condition. Our friend Moneybags, &ldquo;who as yet is only "
                  "an embryo capitalist&rdquo;, must buy at value, sell at value, and still "
                  "draw out more than he put in. Marx closes with the line from Aesop's fable, "
                  "said to a boaster who claimed he had once made a great leap on Rhodes: "
                  "&ldquo;Hic Rhodus, hic salta!&rdquo; Here is Rhodes; jump here."),
            ("p", "The objection at full strength runs the other way. Since David Ricardo, "
                  "economists have shown that trade between parties with different costs "
                  "raises total output, and the marginal-utility economists would add that "
                  "both sides of a voluntary exchange gain in the only sense of value they "
                  "recognise, what goods are worth to the people holding them. Marx accepts "
                  "the first point as a gain in use-value, as his wine-grower shows. The "
                  "second is a different definition of value. On the chapter's definition, "
                  "value as labour-time already spent, no exchange can change the total, and "
                  "the argument is only as strong as that definition."),
            ("p", "The lab arranges traders in a ring, each selling to the next at a mark-up, "
                  "so everyone is a buyer and a seller. Ten per cent all round leaves each "
                  "trader where he began. Marx's wine-and-corn cheat moves £10 from B to A and "
                  "leaves the £90 alone. Put a producer who sells at value into a ring with three "
                  "dealers who each add 10%, and £10 moves from him to the dealer he sells to; "
                  "the total is still what it was."),
            ("p", "So the surplus must come from a purchase made at its value. The next lesson, "
                  "“The Buying and Selling of Labour-Power”, finds the one commodity whose use "
                  "can supply it."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "markup",
            "money_unit": "£",
            "preset": "ten",
            "presets": [
                {"id": "ten", "label": "Three traders, each sells 10% above value",
                 "sellers": [{"name": "A", "value": 100, "markup": "1/10"},
                             {"name": "B", "value": 100, "markup": "1/10"},
                             {"name": "C", "value": 100, "markup": "1/10"}],
                 "expect": {"ciTotalBefore": "£300", "ciTotalAfter": "£300"}},
                {"id": "one-cheat", "label": "Marx's cheat: A's £40 of wine for B's £50 of corn",
                 "sellers": [{"name": "A (wine)", "value": 40, "markup": "1/4"},
                             {"name": "B (corn)", "value": 50, "markup": 0}],
                 "expect": {"ciTotalBefore": "£90", "ciTotalAfter": "£90"}},
                {"id": "merchants", "label": "Three dealers add 10%; the producer adds nothing",
                 "sellers": [{"name": "producer", "value": 100, "markup": 0},
                             {"name": "dealer 1", "value": 100, "markup": "1/10"},
                             {"name": "dealer 2", "value": 100, "markup": "1/10"},
                             {"name": "dealer 3", "value": 100, "markup": "1/10"}],
                 "expect": {"ciTotalBefore": "£400", "ciTotalAfter": "£400"}},
            ],
            "panel_title": "Mark-ups in a ring",
            "panel_intro": (
                "Each trader sells to the next in the list, and the last sells to the first, at "
                "the value of his goods times one plus his mark-up. A mark-up of 1/10 is 10%. "
                "The table shows what each holds after; the tiles add them up."
            ),
        }),
        "steps_title": "Following value through a round of sales",
        "steps_intro": "Four steps for any set of trades among people who both buy and sell.",
        "steps": [
            ("Total the values before",
             "Add the values of the goods each trader holds before any sale. This is the sum "
             "of values in circulation."),
            ("Price each sale",
             "Each sale is at the seller's value times one plus his mark-up. A mark-up of 0 is "
             "a sale at value."),
            ("Settle each trader",
             "What a trader holds after is the value of the goods he received plus what he was "
             "paid less what he paid. The difference from before is his gain or loss."),
            ("Total the values after",
             "Add what everyone holds after. It equals the total before; if one trader gained, "
             "find the trader who lost the same amount."),
        ],
        "worked": {
            "title": "Wine for corn",
            "intro": [
                "Take Marx's case. A holds wine worth £40 and B holds corn worth £50. A is "
                "clever enough to get the corn for his wine. You want each party's gain and the "
                "total before and after.",
            ],
            "lines": [
                "before:  A £40 + B £50 = £90",
                "A gives wine worth £40, gets corn worth £50",
                "B gives corn worth £50, gets wine worth £40",
                "after:  A £50 + B £40 = £90",
                "A +£10, B −£10, total +£0",
            ],
            "after": [
                "A has turned £40 into £50, and for A the exchange has worked like capital. For "
                "the two of them together nothing has been made, and the class that A and B "
                "stand for cannot live by cheating itself.",
            ],
        },
        "quiz_title": "What a mark-up can and cannot do",
        "quiz": [
            {"q": "Four traders each hold goods worth £100, and each sells to the next at 10% "
                  "above value. What is the total value they hold after the round?",
             "a": ["£440", "£400", "£360", "£410"],
             "c": 1,
             "why": "Each receives goods worth £100 and pays £110 for them while being paid £110 "
                    "for his own, so each still holds £100 of value and the total is `4 · £100 = "
                    "£400`. £440 counts the mark-ups received and forgets the mark-ups paid."},
            {"q": "In Marx's example A sells wine worth £40 to B and gets corn worth £50. What "
                  "is the total value held by A and B after the exchange?",
             "a": ["£100", "£80", "£90", "£50"],
             "c": 2,
             "why": "The goods change hands and the sum does not: £40 and £50 before, £50 and "
                    "£40 after, £90 both times. £100 adds A's £10 without taking it from B."},
            {"q": "Which of these can a single exchange of unequal values do, on the chapter's "
                  "argument?",
             "a": ["Raise the total value held when every trader does it",
                   "Add value to the sum in circulation",
                   "Create surplus value for the capitalist class as a whole",
                   "Move value from one trader to another"],
             "c": 3,
             "why": "A cheat transfers value: A's gain is B's loss. It adds nothing to the sum, "
                    "for one trader or for all, and a class whose members cheat one another is "
                    "only redistributing what it already has."},
            {"q": "Why does Marx agree that both parties to an exchange can gain?",
             "a": ["Each receives more labour-time than he gave",
                   "Each gets a use-value more useful to him than the one he gave up",
                   "Money adds a little value each time it changes hands",
                   "Prices always rise between a sale and the next purchase"],
             "c": 1,
             "why": "The gain Marx grants is in use-value: the wine-grower wants corn more than "
                    "his surplus wine. In value, equal exchanges give nobody more labour-time, "
                    "and money in circulation adds none."},
        ],
        "mistakes": [
            ("Thinking profit comes from selling above value",
             "It is the first explanation anyone reaches for, and the ring refutes it in one "
             "line. With every trader marking up 10%, the values held are £300 before and £300 "
             "after: each gains £10 as a seller and loses £10 as a buyer. A surplus that every "
             "seller pockets is a surplus every buyer pays, and every seller is a buyer."),
            ("Counting one trader's gain as a gain for all",
             "A who cheats B really is £10 richer, and a merchant who buys cheap and sells "
             "dear really does profit. The one-cheat preset shows the other side: B is £10 "
             "poorer and the total is still £90. Redistribution can enrich a capitalist; it "
             "cannot enrich capital as a whole."),
            ("Confusing a gain in use-value with a gain in value",
             "Both traders may be glad of the exchange, because each now has what he wants. "
             "That is a gain in use-value, and Condillac built a theory of profit on it. Marx's "
             "point is that the same exchange leaves the quantity of value held exactly where "
             "it was."),
        ],
        "standard": (
            "Finish when you can show that a mark-up adds nothing to the total.",
            "Given traders' values and mark-ups, compute what each holds before and after a "
            "round of sales, compute both totals, and identify whose gain is whose loss."
        ),
        "note": (
            "The ring is the lab's model of Marx's assumption that every seller is also a "
            "buyer; it is why he must set aside a class that only buys. The argument also "
            "leans on value as labour-time already spent, which is a definition the "
            "marginal-utility tradition rejects. The 10% and the wine and corn are Marx's "
            "figures; the three dealers are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 1, l. 1590-1592 (free in the double sense); l. 1632 (a very
    # Eden of the innate rights of man); l. 1578, 1580, 1588, 1598, 1604,
    # 1610, 1614-1616, 1620-1622 (phrases).
    {
        "slug": "buying-and-selling-labour-power",
        "title": "The Buying and Selling of Labour-Power",
        "module": "Chapter 6 · The Buying and Selling of Labour-Power",
        "one_line": "The one commodity whose use creates value is labour-power, and it is worth what the worker's means of subsistence are worth, averaged over a day.",
        "summary": (
            "Moneybags finds his commodity: labour-power, sold by a worker who is free in two "
            "senses. Compute its daily value from the values of things bought every day, every "
            "week and every year, then add a family and a trade's training, and see why Marx "
            "insists the worker sells a capacity and not labour."
        ),
        "key": [
            "labour-power: the capacity to work",
            "free twice: to sell it, and of all else",
            "value of labour-power = value of necessities",
            "daily value = sum of value / days it lasts",
            "plus children's upkeep and training",
        ],
        "key_label": "The special commodity",
        "concepts_intro": (
            "The riddle of the last chapter was a purchase at value that yields more value. "
            "Chapter 6 names the commodity and says what it is worth."
        ),
        "concepts": [
            ("Labour-power",
             "The sum of the mental and physical capabilities a person exercises in producing "
             "anything useful. It is a capacity. Labour is its use, as digestion is the use of "
             "a stomach."),
            ("Free in the double sense",
             "The seller owns his own person and can sell his capacity for a definite period. "
             "And he owns nothing else he could live by: no tools, no materials, no land. Both "
             "conditions are needed, and neither is natural."),
            ("The value of labour-power",
             "Like any commodity's, the labour-time needed to produce it: here, to produce the "
             "means of subsistence that keep the worker, and his replacements, able to work. "
             "What counts as necessary depends on the country and the period."),
        ],
        "read_title": "The free labourer, then what his commodity is worth",
        "read_intro": (
            "The passage is the chapter's central condition. A second, at the end of the "
            "lesson, is the paragraph in which Marx leaves the market behind."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 6.</strong> &ldquo;For the conversion of his "
                  "money into capital, therefore, the owner of money must meet in the market "
                  "with the free labourer, free in the double sense, that as a free man he can "
                  "dispose of his labour-power as his own commodity, and that on the other hand "
                  "he has no other commodity for sale, is short of everything necessary for the "
                  "realisation of his labour-power.&rdquo;"),
            ("p", "Go back to where the last chapter left things. The change in value cannot "
                  "happen in the money, which only realises prices, nor in the resale, which "
                  "only turns a commodity back into money. So it must happen in the commodity "
                  "bought first, and not in its value, since it was bought at its value. It "
                  "must happen in its use. Moneybags needs a commodity &ldquo;whose use-value "
                  "possesses the peculiar property of being a source of value&rdquo;, and he "
                  "finds one."),
            ("def", ("Labour-power",
                     "In Marx's words, &ldquo;the aggregate of these mental and physical "
                     "capabilities existing in a human being, which he exercises whenever he "
                     "produces a use-value of any description&rdquo;. It is sold for a period, "
                     "and its use is labour.")),
            ("p", "Now read the passage clause by clause. First, &ldquo;as a free man he can "
                  "dispose of his labour-power&rdquo;: the seller must own himself, and he must "
                  "sell for a definite time only. Sell it &ldquo;rump and stump, once for "
                  "all&rdquo;, and he would be selling himself, a slave rather than a seller. "
                  "Then, &ldquo;he has no other commodity for sale&rdquo;: if he had leather and "
                  "tools he would sell "
                  "boots instead, and &ldquo;No boots can be made without leather.&rdquo; Free "
                  "of masters, then, and free of property."),
            ("p", "Marx then adds a point that does not interest Moneybags at all. Nature "
                  "does not produce owners of money on one side and people with nothing but "
                  "their capacity to work on the other. That relation is the result of a long "
                  "history, &ldquo;the extinction of a whole series of older forms of social "
                  "production&rdquo;, and &ldquo;this one historical condition comprises a "
                  "world's history.&rdquo; He takes the fact as given for now, as Moneybags "
                  "does. The history is told at the end of the volume, in the course So-Called "
                  "Primitive Accumulation."),
            ("p", "What is the commodity worth? The rule of Chapter 1 applies: the labour-time "
                  "needed to produce it. Labour-power exists only in a living person, so "
                  "producing it means maintaining that person, and its value is the value of the "
                  "means of subsistence that maintain him in his normal state as a worker. "
                  "Here Marx adds a qualification that no other commodity needs. What counts as "
                  "necessary, how people eat, dress and are housed, depends on the climate and "
                  "on the habits of the class, so &ldquo;there enters into the determination "
                  "of the value of labour-power a historical and moral element.&rdquo; In a "
                  "given country at a given time, he says, the average is &ldquo;practically "
                  "known&rdquo;."),
            ("p", "Things are bought on different schedules. Food and fuel are bought every "
                  "day, clothes every so often, furniture rarely. Marx averages them over the "
                  "year: 365 times what is needed daily, plus 52 times what is needed weekly, "
                  "plus 4 times what is needed quarterly, all over 365. Suppose the result "
                  "contains 6 hours of social labour. Then half a day's labour goes into "
                  "producing a day's labour-power, and if half a day's labour is embodied in "
                  "three shillings, three shillings is the value of a day's labour-power. "
                  "Those are the figures the next five lessons use."),
            ("p", "Two more items enter. The worker is mortal, so the sum must include the "
                  "upkeep of his replacements, his children. And a trade that needs training "
                  "costs something to learn, a cost spread over the working life and, for "
                  "ordinary labour, &ldquo;excessively small&rdquo;. The physical minimum, below "
                  "which labour-power can be maintained only &ldquo;in a crippled state&rdquo;, "
                  "is a floor. A price at that floor is below the value."),
            ("p", "Pellegrino Rossi, the Italian economist who taught at the Collège de France, "
                  "objected that to speak of labour-power apart from the worker's subsistence "
                  "is to speak of a phantom. Marx answers first with a joke: &ldquo;When we speak "
                  "of capacity for labour, we do not speak of labour, any more than when we speak "
                  "of capacity for digestion, we speak of digestion.&rdquo; Then he turns the point "
                  "round: nobody is abstracting from the subsistence, because its value is exactly "
                  "what the capacity is worth."),
            ("p", "One detail matters later. Labour-power is usually paid for after it has been "
                  "used, at the end of the week, so the worker &ldquo;gives credit to the "
                  "capitalist&rdquo;. Marx sets this aside and assumes payment on the spot, "
                  "since it does not change what is exchanged for what."),
            ("p", "The standard objection is strong. In the theory of wages most economists use, "
                  "a wage is set by what an extra worker adds to output and by the supply of "
                  "workers, not by a cost of production, and Marx's &ldquo;historical and moral "
                  "element&rdquo; has been read as conceding that the value of labour-power is "
                  "whatever custom makes it. The chapter's claim is narrower than either reading: "
                  "at a given time and place there is a customary bundle of necessities, and "
                  "its value is what a day's labour-power is worth."),
            ("p", "The lab sums a bundle. Each item has a value in hours and lasts so many "
                  "days; its value spread over those days is what it costs per day, and the "
                  "daily value of labour-power is the total. The first preset makes Marx's 6 "
                  "hours from 4 hours of daily needs, clothes worth 7 hours lasting a week and "
                  "furniture worth 365 hours lasting a year. The second adds the children; the "
                  "third adds a year of training spread over a thirty-year working life."),
            ("p", "With the price settled, Marx follows the buyer and the seller out of the "
                  "market, and the passage is one of the most quoted in the book:"),
            ("p", "<strong>Volume I, Chapter 6.</strong> &ldquo;This sphere that we are "
                  "deserting, within whose boundaries the sale and purchase of labour-power "
                  "goes, is in fact a very Eden of the innate rights of man. There alone rule "
                  "Freedom, Equality, Property and Bentham.&rdquo;"),
            ("p", "Freedom, because both contract as they choose; equality, because equivalent "
                  "is exchanged for equivalent; property, because each disposes of his own; and "
                  "Bentham, because each looks only to himself. Behind the factory door, with "
                  "its sign &ldquo;No admittance except on business&rdquo;, the next lesson, "
                  "“The Labour Process and the Production of Surplus Value”, sees what the "
                  "buyer does with what he has bought."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "labour-power",
            "money_unit": "hours",
            "preset": "daily",
            "presets": [
                {"id": "daily", "label": "Daily, weekly and yearly needs: Marx's 6 hours",
                 "subsistence": [{"item": "food and fuel", "hours": 4, "every_days": 1},
                                 {"item": "clothes", "hours": 7, "every_days": 7},
                                 {"item": "furniture", "hours": 365, "every_days": 365}],
                 "expect": {"ciLpValue": "6 h"}},
                {"id": "family", "label": "Add the children's upkeep, 2 hours a day",
                 "subsistence": [{"item": "food and fuel", "hours": 4, "every_days": 1},
                                 {"item": "clothes", "hours": 7, "every_days": 7},
                                 {"item": "furniture", "hours": 365, "every_days": 365},
                                 {"item": "children", "hours": 2, "every_days": 1}],
                 "expect": {"ciLpValue": "8 h"}},
                {"id": "training", "label": "Add a year of training spread over 30 years",
                 "subsistence": [{"item": "food and fuel", "hours": 4, "every_days": 1},
                                 {"item": "clothes", "hours": 7, "every_days": 7},
                                 {"item": "furniture", "hours": 365, "every_days": 365},
                                 {"item": "training", "hours": 2190, "every_days": 10950}],
                 "expect": {"ciLpValue": "31/5 h"}},
            ],
            "panel_title": "What a day's labour-power is worth",
            "panel_intro": (
                "Each item of the worker's subsistence has a value in hours and is renewed "
                "every so many days. The lab spreads each value over its days and adds. Try "
                "leaving out the clothes and the furniture and see how much the daily figure "
                "falls."
            ),
        }),
        "steps_title": "Valuing a day's labour-power",
        "steps_intro": "Four steps from a list of necessities to a daily value.",
        "steps": [
            ("List the bundle",
             "Write down the means of subsistence a worker of this place and time needs, "
             "with the value of each in hours and how many days it lasts."),
            ("Spread each item over its life",
             "Divide each value by the days the item lasts. Food bought daily counts whole; "
             "a coat that lasts a year counts one 365th a day."),
            ("Add the replacements and the training",
             "Include the upkeep of the worker's children, and any training cost spread over "
             "the working life."),
            ("Total and price",
             "The sum is the value of a day's labour-power in hours. Its price is that many "
             "hours expressed in money, 3s for Marx's 6 hours."),
        ],
        "worked": {
            "title": "Six hours from three schedules",
            "intro": [
                "A worker needs food and fuel worth 4 hours every day, clothes worth 7 hours "
                "that last a week, and furniture worth 365 hours that lasts a year. You want "
                "the daily value of his labour-power and its price at Marx's rate.",
            ],
            "lines": [
                "food and fuel:  4 / 1 = 4 h a day",
                "clothes:  7 / 7 = 1 h a day",
                "furniture:  365 / 365 = 1 h a day",
                "daily value:  4 + 1 + 1 = 6 h",
                "price:  6 h at 1/2 s an hour = 3s",
            ],
            "after": [
                "Six hours is Marx's figure; the split among the three items is illustrative. "
                "Add children's upkeep of 2 hours a day and the figure is 8 hours. Leave out "
                "the clothes and the furniture and it is 4, a third too low.",
            ],
        },
        "quiz_title": "A capacity, and its price",
        "quiz": [
            {"q": "A worker's food and fuel take 4 hours a day to produce, clothes worth 14 "
                  "hours last 14 days, and furniture worth 730 hours lasts 730 days. What is "
                  "the daily value of labour-power?",
             "a": ["748 hours", "19 hours", "6 hours", "4 hours"],
             "c": 2,
             "why": "Spread each item over its life: `4 + 14/14 + 730/730 = 6` hours. 748 adds "
                    "the totals without spreading them, 19 spreads only the furniture and "
                    "counts the clothes whole, and 4 leaves out everything not bought daily."},
            {"q": "On the chapter's account, what does the worker sell to the capitalist?",
             "a": ["Labour, so many hours of work already done",
                   "Labour-power, for a definite period",
                   "Himself, once for all",
                   "The product he will make"],
             "c": 1,
             "why": "He sells his capacity to work for a period. Labour is the use of that "
                    "capacity, which happens after the sale; selling himself once for all would "
                    "make him a slave, not a seller; and the product belongs to the buyer."},
            {"q": "Which two conditions does Marx say must hold before money can find "
                  "labour-power for sale?",
             "a": ["The worker owns his own person, and has no means of production of his own",
                   "The worker owns tools, and cannot find buyers for his products",
                   "The worker is bound to one employer, and owns a little land",
                   "Wages are paid in advance, and trade is free"],
             "c": 0,
             "why": "Free in the double sense: free to sell his capacity as its owner, and free "
                    "of anything else to sell. A worker with tools sells products; a bound "
                    "worker cannot sell at all; when wages are paid is a detail Marx sets aside."},
            {"q": "Why is the value of labour-power more than the value of what keeps a worker "
                  "physically alive?",
             "a": ["Because it equals the value the worker creates in a day",
                   "Because it is whatever wage the employer chooses to pay",
                   "Because training is always the largest part of it",
                   "Because it includes a historical and moral element: the customary needs of "
                   "a given country and period"],
             "c": 3,
             "why": "Necessary wants are themselves a product of history, so the bundle is more "
                    "than the physical minimum, which Marx calls a floor below the value. The "
                    "value created in a day is a different quantity, the subject of the next "
                    "lesson; the employer does not set the value; and training for ordinary "
                    "labour is small."},
        ],
        "mistakes": [
            ("Thinking the worker sells labour, so many hours of work done",
             "Wages are paid by the hour or the day, so it looks as if labour itself is bought. "
             "The lab's figure says otherwise: the daily value of labour-power is 6 hours "
             "whatever length of day follows, because it is fixed by the bundle before any work "
             "is done. What is sold is the capacity; how long it is used is settled afterwards, "
             "and the difference between the two is the next lesson."),
            ("Reading the value of labour-power as a bare physical minimum",
             "Marx says the opposite. The minimum is what the worker cannot live without from "
             "day to day, and a price that falls to it is below the value. The value includes "
             "customary needs, the children and the training."),
            ("Leaving out the things bought rarely",
             "A daily figure built only from daily purchases is too low. In the first preset "
             "the clothes and the furniture add 2 hours to the 4 of food and fuel, a third of "
             "the whole."),
        ],
        "standard": (
            "Finish when you can compute the daily value of labour-power from a bundle of "
            "necessities.",
            "Given the value of each item of subsistence and the days it lasts, with any "
            "upkeep of children and training cost, compute the daily value of labour-power "
            "in hours, and state what the worker sells."
        ),
        "note": (
            "The bundle is the lab's input, not its output: which necessities count, and how "
            "the historical and moral element is fixed, is exactly where Marx's account is "
            "most contested, and no lab can settle it. The lab's weekly item lasts 7 days where "
            "Marx divides 52 weeks by 365 days. Marx's figures are 6 hours and 3s; the items "
            "that make them up are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 1, l. 1764 (Our capitalist stares in astonishment); l. 1782
    # (the trick has at last succeeded); l. 1653 (architect and bee); l. 1719,
    # 1728, 1762, 1772-1774, 1778, 1793 (phrases).
    {
        "slug": "the-labour-process-and-surplus-value",
        "title": "The Labour Process and the Production of Surplus Value",
        "module": "Chapter 7 · The Labour-Process and the Process of Producing Surplus-Value",
        "one_line": "Six hours of spinning give yarn worth exactly what was advanced; twelve give yarn worth 30s against 27s advanced, with every input bought at its value.",
        "summary": (
            "Section 1 describes the labour process every society has; section 2 puts "
            "Moneybags in charge of it. Compute the value of the yarn from cotton, spindle "
            "wear and labour for a six-hour day and then a twelve-hour one, and find the 3s "
            "left over between what a day's labour-power costs and what a day's labour adds."
        ),
        "key": [
            "labour process: work, object, instrument",
            "yarn = cotton + wear + new value",
            "6 h: 10 + 2 + 3 = 15s against 15s",
            "12 h: 20 + 4 + 6 = 30s against 27s",
            "s = value of product − capital advanced",
        ],
        "key_label": "The spinning mill",
        "concepts_intro": (
            "The chapter has two sections, and they look at the same work twice: once as "
            "the making of a useful thing, once as the making of value."
        ),
        "concepts": [
            ("The labour process",
             "Purposeful activity, the object it works on and the instruments it works with. "
             "It is common to every form of society, and the taste of the porridge, Marx "
             "says, does not tell you who grew the oats."),
            ("The value of the product",
             "The value of the means of production used up, carried over into the product, "
             "plus the new value the labour adds. Only socially necessary time counts, for "
             "the labour and for the materials."),
            ("Two magnitudes",
             "The value of a day's labour-power is what keeps the worker for a day. The value "
             "a day's labour adds depends on how long he works. Nothing makes them equal."),
        ],
        "read_title": "The capitalist's surprise, then how it is resolved",
        "read_intro": (
            "The passage comes at the moment the six-hour sum comes out even. The lesson "
            "reads the labour process first, then follows Marx's arithmetic to the point "
            "where it does not."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 7, §2.</strong> &ldquo;Our capitalist stares in "
                  "astonishment. The value of the product is exactly equal to the value of the "
                  "capital advanced. The value so advanced has not expanded, no surplus-value "
                  "has been created, and consequently money has not been converted into "
                  "capital.&rdquo;"),
            ("p", "Think about the last thing you bought that was made in a factory. Its price "
                  "had to cover the materials, the wear on the machines and the wages, and you "
                  "would expect it to cover them exactly if nobody cheated. That is the puzzle "
                  "Marx sets up with his spinner. Ten pounds of cotton at 10s, 2s of wear on "
                  "the spindle, six hours of spinning: the yarn is worth 15s, and the capitalist "
                  "who paid 3s for a day's labour-power and 12s for the rest has made nothing. "
                  "He &ldquo;stares in astonishment&rdquo;. Before the arithmetic, though, the "
                  "chapter steps back."),
            ("p", "Section 1 is about labour in any society. It is a process between people and "
                  "nature, and what makes it human is purpose: &ldquo;what distinguishes the "
                  "worst architect from the best of bees is this, that the architect raises his "
                  "structure in imagination before he erects it in reality.&rdquo; Its elements "
                  "are the work itself, the object worked on and the instruments. Fish in the "
                  "sea is an object of labour supplied by nature; cotton already grown is raw "
                  "material; the spindle is an instrument. At the end, &ldquo;The process "
                  "disappears in the product&rdquo;."),
            ("p", "When the capitalist runs the process, two things change and nothing else "
                  "yet does. The worker works under the capitalist's control, and the product "
                  "belongs to the capitalist, &ldquo;just as much as does the wine which is the "
                  "product of a process of fermentation completed in his cellar&rdquo;. The "
                  "methods are those he found on the market. Changing them is the subject of "
                  "Relative Surplus Value."),
            ("p", "Section 2 turns to value. The capitalist wants a use-value that will sell, "
                  "and more: a commodity worth more than the means of production and "
                  "labour-power he bought for it. So Marx counts. Ten pounds of cotton bought "
                  "at its value, 10s. Spindle wear worth 2s. If twenty-four hours of labour are "
                  "embodied in 12s, two days' labour are already in the yarn before spinning "
                  "starts. Spinning is simple average labour, and in six hours the spinner turns "
                  "the 10 lb of cotton into 10 lb of yarn, adding six hours, which is 3s. "
                  "Total: 15s, eighteenpence a pound."),
            ("p", "Then comes one of the book's comic scenes. The capitalist protests that he "
                  "advanced his money to make more money. He appeals to his abstinence: "
                  "&ldquo;Consider my abstinence; I might have played ducks and drakes with the "
                  "15 shillings&rdquo;. He claims he supplied the cotton and the spindle as a "
                  "service. He claims his own labour of superintendence, at which "
                  "&ldquo;His overlooker and his manager try to hide their smiles.&rdquo; Then "
                  "he laughs, drops the whole creed, and leaves it &ldquo;to the professors of "
                  "political economy, who are paid for it&rdquo;. He has known the answer all "
                  "along."),
            ("p", "The answer is the difference between the two magnitudes. A day's "
                  "labour-power is worth 3s because half a day's labour keeps the worker for a "
                  "day. Nothing stops him working a whole day. The value of labour-power and "
                  "the value it creates in use &ldquo;are two entirely different "
                  "magnitudes&rdquo;, and the gap is &ldquo;a piece of good luck for the buyer, "
                  "but by no means an injury to the seller.&rdquo; So the capitalist has bought "
                  "materials for twelve hours."),
            ("p", "<strong>Volume I, Chapter 7, §2.</strong> &ldquo;Therefore the value of the "
                  "product is 1/9 greater than the value advanced for its production; 27 "
                  "shillings have been transformed into 30 shillings; a surplus-value of 3 "
                  "shillings has been created. The trick has at last succeeded; money has been "
                  "converted into capital.&rdquo;"),
            ("p", "Read the twelve-hour sum line by line. Twenty pounds of cotton, 20s. Wear, "
                  "4s. Twelve hours of spinning add 6s. The yarn is worth 30s, still eighteenpence "
                  "a pound. The capitalist advanced 20 + 4 + 3 = 27s. Every commodity was bought "
                  "at its value and the yarn is sold at its value. Here the chapter's accounting "
                  "assumes that commodities sell at their values, and it needs that assumption: "
                  "the surplus is not a cheat in the market. The conditions of the riddle of "
                  "Chapter 5 are met, in circulation, where labour-power is bought, and not in "
                  "circulation, where it is used."),
            ("p", "Only socially necessary time counts, and this is why the capitalist watches "
                  "the work so closely. A spinner given a distaff where the self-acting mule is "
                  "normal, or cotton so poor that it wastes, spends time that creates no value. "
                  "If the capitalist uses a gold spindle where a steel one would do, only the "
                  "steel one's labour counts. Waste, Marx says, is forbidden by the capitalist's "
                  "&ldquo;penal code of his own&rdquo;, because wasted material carries no "
                  "value into the product."),
            ("p", "On Marx's definitions the 3s is the difference between what a day of "
                  "labour-power costs and what a day of labour adds. That is exactly the step "
                  "an economist who prices labour by its marginal product would refuse: on that "
                  "account the capital goods are productive too, and part of the product is "
                  "theirs. Eugen von Böhm-Bawerk, in the 1880s, put the return on capital down "
                  "to time instead: present goods are worth more than future ones, and the "
                  "capitalist who advances them is paid for the wait. The capitalist's appeal to "
                  "abstinence is a cruder version of that argument. Marx's answers in this "
                  "chapter are that in the six-hour case there is nothing to reward abstinence "
                  "with, since the product is worth exactly what went in, and that the "
                  "&ldquo;service&rdquo; of the cotton and the spindle is a matter of use-value, "
                  "while the question is one of value. Whether the 3s of the twelve-hour day "
                  "rewards waiting is the question the next lessons keep in view."),
            ("p", "The lab does the mill's sum. The first preset is Marx's six hours, product "
                  "15s and nothing left over. The second is his twelve hours: 27s goes in, yarn "
                  "worth 30s comes out. The third keeps the twelve hours but uses 2s more cotton "
                  "than is socially necessary: the yarn is still worth 30s, and the surplus "
                  "falls to 1s."),
            ("p", "The spindle and the cotton have passed their value into the yarn without "
                  "adding to it. The next lesson, “Constant Capital and Variable Capital”, asks "
                  "how they do that, and names the two parts of capital accordingly."),
        ],
        "lab": ("capkit", {
            "mode": "surplus",
            "view": "mill",
            "money_unit": "s",
            "preset": "six",
            "presets": [
                {"id": "six", "label": "Marx's six hours: 10 lb of cotton at 10s, 2s of wear",
                 "materials": 10, "wear": 2, "wage": 3, "hours": 6, "necessary_hours": 6,
                 "waste": 0, "expect": {"suProduct": "15s", "suS": "0s"}},
                {"id": "twelve", "label": "Marx's twelve hours: 20 lb of cotton at 20s, 4s of wear",
                 "materials": 20, "wear": 4, "wage": 3, "hours": 12, "necessary_hours": 6,
                 "waste": 0, "expect": {"suProduct": "30s", "suS": "3s"}},
                {"id": "waste", "label": "Twelve hours with 2s of cotton wasted beyond the norm",
                 "materials": 22, "wear": 4, "wage": 3, "hours": 12, "necessary_hours": 6,
                 "waste": 2, "expect": {"suProduct": "30s", "suS": "1s"}},
            ],
            "panel_title": "The value of a day's yarn",
            "panel_intro": (
                "Materials and wear are carried over at their value; each hour of spinning adds "
                "the wage divided by the necessary hours, half a shilling on Marx's figures. "
                "The second tile is the product's value less everything advanced."
            ),
        }),
        "steps_title": "Valuing a product and finding the surplus",
        "steps_intro": "Four steps, the same for the yarn and for any product.",
        "steps": [
            ("Carry over the means of production",
             "Add the value of the materials used up, counting only what is socially "
             "necessary, and the wear on the instruments."),
            ("Add the new value",
             "Each hour of average labour adds the same value. On Marx's figures six hours add "
             "3s, so an hour adds sixpence."),
            ("Total the capital advanced",
             "Add what was paid for materials, wear and a day's labour-power. Every item is "
             "bought at its value."),
            ("Subtract",
             "The value of the product less the capital advanced is the surplus value. It is "
             "zero when the hours worked equal the hours that reproduce the wage."),
        ],
        "worked": {
            "title": "Twelve hours of spinning",
            "intro": [
                "Take Marx's second case. In a twelve-hour day the spinner works 20 lb of "
                "cotton worth 20s and wears 4s off the spindle. A day's labour-power costs 3s, "
                "the value of six hours. You want the yarn's value and the surplus.",
            ],
            "lines": [
                "carried over:  20 + 4 = 24s",
                "new value:  12 h at 1/2 s an hour = 6s",
                "yarn:  24 + 6 = 30s",
                "advanced:  20 + 4 + 3 = 27s",
                "surplus value:  30 − 27 = 3s",
            ],
            "after": [
                "At six hours the same sums give 12 + 3 = 15s against 15s advanced. The "
                "difference between the two days is six hours of labour that add 3s and cost "
                "nothing extra, because the 3s for labour-power was paid already.",
            ],
        },
        "quiz_title": "Where the 3s comes from",
        "quiz": [
            {"q": "On Marx's figures a twelve-hour day spins 20 lb of cotton worth 20s, with 4s "
                  "of spindle wear, and labour-power costs 3s a day, the value of six hours. "
                  "What is the yarn worth?",
             "a": ["27s", "33s", "30s", "24s"],
             "c": 2,
             "why": "`20 + 4 = 24s` carried over plus `12 · 1/2 = 6s` added is 30s. 27s is "
                    "the capital advanced, which counts the 3s wage instead of the 6s of new "
                    "value; 24s leaves the new value out; 33s adds both."},
            {"q": "Why is there no surplus value in Marx's six-hour case?",
             "a": ["The cotton was bought below its value",
                   "Six hours of labour add 3s, exactly the value of the day's labour-power",
                   "The spindle passes no value into the yarn",
                   "The yarn is sold below its value"],
             "c": 1,
             "why": "Six hours add the same 3s that was paid for the labour-power, so the product "
                    "equals the capital advanced. Everything in the case is bought and sold at "
                    "value, and the spindle does pass its 2s of wear into the yarn."},
            {"q": "In the twelve-hour day the capitalist uses 22s of cotton where 20s is "
                  "socially necessary. On the chapter's accounting, what happens?",
             "a": ["The yarn is worth 32s, because the extra cotton is in it",
                   "The surplus rises, because more material was worked up",
                   "The yarn is still worth 30s, and the surplus falls from 3s to 1s",
                   "The extra 2s passes into the next day's yarn"],
             "c": 2,
             "why": "Only socially necessary material counts, so the yarn carries 20s of cotton "
                    "and is worth 30s; the capitalist advanced `22 + 4 + 3 = 29s` and keeps "
                    "1s. The wasted cotton passes no value anywhere."},
            {"q": "In Marx's phrase, what distinguishes the worst architect from the best of "
                  "bees?",
             "a": ["The architect raises the structure in imagination before building it",
                   "The architect is paid a wage for the work",
                   "The architect works for a capitalist",
                   "The architect's buildings last longer"],
             "c": 0,
             "why": "Purpose is what makes the labour process human: the result exists in the "
                    "worker's imagination at the start. Wages and capitalists belong to the "
                    "capitalist form of the process, which section 1 deliberately sets aside."},
        ],
        "mistakes": [
            ("Thinking the surplus is the machine's contribution",
             "The spindle and the cotton are in the six-hour preset too, and the surplus there "
             "is 0s. In the twelve-hour preset they pass over 24s, exactly what they cost, and "
             "the 3s comes from six hours of labour beyond the six that reproduce the wage. On "
             "the chapter's accounting the means of production carry value over and add none; "
             "the next lesson shows how."),
            ("Thinking the capitalist must have underpaid the worker",
             "He paid 3s, the full value of a day's labour-power, and the chapter insists on "
             "it. The surplus arises with every commodity bought and sold at its value. What "
             "the worker sold was a day's use of his capacity, and that use is worth more than "
             "its cost."),
            ("Counting every hour and every pound of cotton the mill uses",
             "Only socially necessary time and material count. In the waste preset 2s of "
             "cotton beyond the norm adds nothing to the yarn's value, so it comes straight "
             "out of the surplus."),
        ],
        "standard": (
            "Finish when you can value a product and find its surplus value.",
            "Given materials, wear, the value of a day's labour-power and the hours worked, "
            "compute the value of the product and the surplus value over the capital "
            "advanced, and compute the difference between a day's labour-power and the value "
            "a day's labour adds."
        ),
        "note": (
            "The chapter's accounting assumes commodities sell at their values, and this "
            "lesson leans on it: at other prices the 3s would be shared differently between "
            "buyer and seller. It also assumes an hour of spinning adds the same value as an "
            "hour of the labour embodied in the gold, which is the labour theory of value the "
            "marginal tradition rejects. The figures are Marx's except the waste preset."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 1, l. 1871 (constant capital); l. 1873-1875 (variable
    # capital); l. 1848 (a machine worth £1000); l. 1818, 1830, 1844, 1852,
    # 1856, 1859, 1877, 1883 (phrases).
    {
        "slug": "constant-capital-and-variable-capital",
        "title": "Constant Capital and Variable Capital",
        "module": "Chapter 8 · Constant Capital and Variable Capital",
        "one_line": "Means of production pass their value into the product unchanged; labour-power reproduces its own value and adds more, and the names constant and variable say exactly that.",
        "summary": (
            "One act of spinning does two things at once: as spinning it carries the cotton's "
            "and the machine's value into the yarn, and as labour in the abstract it adds new "
            "value. Compute the value a £1,000 machine with a 1,000-day life passes into each "
            "day's product, see what moves when productivity rises sixfold and when cotton "
            "doubles in price, and classify the parts of a capital as c or v."
        ),
        "key": [
            "c: means of production, value carried over",
            "v: labour-power, value reproduced and more",
            "daily wear = machine value / days of life",
            "c passes on no more value than it loses",
            "constant capital is not fixed capital",
        ],
        "key_label": "Two parts of capital",
        "concepts_intro": (
            "Chapter 7 assumed that the cotton and the spindle carry their value into the "
            "yarn. Chapter 8 asks how, and draws the distinction the rest of the book is "
            "built on."
        ),
        "concepts": [
            ("Preserving and adding",
             "By spinning, the worker keeps the cotton's value alive in the yarn. By working "
             "for so many hours, he adds new value. The first is a property of the concrete "
             "kind of labour, the second of its quantity."),
            ("Transfer by wear",
             "An instrument takes part whole in the labour process but passes its value into "
             "the product bit by bit, as it wears out. It can never pass on more value than it "
             "had."),
            ("Constant and variable",
             "The capital laid out on means of production does not change its value in "
             "production: constant capital, c. The capital laid out on labour-power reproduces "
             "its value and produces a surplus: variable capital, v."),
        ],
        "read_title": "The two definitions, and the arithmetic of wear",
        "read_intro": (
            "The definitions come at the end of the chapter. The passage gives the first; the "
            "second follows in the body, after the reasoning that leads to both."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 8.</strong> &ldquo;That part of capital then, "
                  "which is represented by the means of production, by the raw material, "
                  "auxiliary material and the instruments of labour, does not, in the process of "
                  "production, undergo any quantitative alteration of value. I therefore call it "
                  "the constant part of capital, or, more shortly, constant capital.&rdquo;"),
            ("p", "Here is the puzzle the chapter begins with. The spinner does not do two jobs, "
                  "one to add value and another to keep the cotton's value in the yarn. He "
                  "spins. Yet two results come out: new value added, old value preserved. "
                  "Marx's explanation is the distinction from “The Twofold Character of Labour”. "
                  "As concrete spinning, the work turns this cotton into this yarn, and so the "
                  "cotton's value goes with it. As labour in the abstract, so many hours of it, "
                  "the work adds new value. If the same man became a joiner, he would still add "
                  "value by working, but he could no longer carry the cotton's value into "
                  "anything."),
            ("p", "Marx tests the distinction by changing one thing at a time. Suppose an "
                  "invention lets the spinner spin as much in 6 hours as he did in 36. Six "
                  "hours now turn 36 lb of cotton into yarn instead of 6. The new value added in "
                  "the 6 hours is the same, spread over six times as many pounds, so each pound "
                  "gets a sixth as much. But the value carried over from the cotton is six times "
                  "as great, because six times as much cotton was spun. Productivity moves the "
                  "value preserved and leaves the value added alone."),
            ("p", "Suppose instead the cotton's value rises sixfold, or falls to a sixth, while "
                  "the spinning stays the same. Then the value transferred from each pound "
                  "changes in the same proportion, and the value added does not change at all. "
                  "Two causes, two separate effects: the two properties of labour are "
                  "&ldquo;essentially different&rdquo;."),
            ("p", "Instruments behave differently from materials. Cotton disappears into the "
                  "yarn; a spindle or a machine keeps its shape, day after day, until it is worn "
                  "out, and then its corpse is left behind, separate from everything it made. "
                  "Over its life it passes its whole value into the products of that life, a "
                  "fraction each day. How do you know the fraction? The way a life-insurance "
                  "office knows how long you will live: by averages."),
            ("p", "<strong>Volume I, Chapter 8.</strong> &ldquo;Suppose a machine to be worth "
                  "£1000, and to wear out in 1000 days. Then one thousandth part of the value of "
                  "the machine is daily transferred to the day's product.&rdquo;"),
            ("p", "So the machine enters the labour process whole every day and the formation "
                  "of value by a thousandth. Waste shows the reverse case. If 15 lb of every 115 "
                  "lb of cotton is lost as &ldquo;devil's dust&rdquo;, and that loss is normal "
                  "for the trade, the 15 lb never becomes yarn, yet its value passes into the "
                  "yarn along with the other 100. It is a necessary condition of the product, "
                  "and only for that reason it counts."),
            ("p", "One rule holds throughout: means of production never transfer more value "
                  "than they lose. A machine that cost £150 cannot add more than £150 to the "
                  "products of its life, however useful it is. Land, wind and water, which no "
                  "labour made, help produce use-values and transfer no value at all. Marx calls "
                  "the power of living labour to preserve old value while adding new &ldquo;a "
                  "gift of Nature which costs the labourer nothing&rdquo;, and notes that the "
                  "capitalist notices it mainly when a crisis stops the machines and their value "
                  "starts to rot."),
            ("p", "The other half of the definition:"),
            ("p", "<strong>Volume I, Chapter 8.</strong> &ldquo;On the other hand, that part of "
                  "capital, represented by labour-power, does, in the process of production, "
                  "undergo an alteration of value. It both reproduces the equivalent of its own "
                  "value, and also produces an excess, a surplus-value, which may itself vary, "
                  "may be more or less according to circumstances.&rdquo;"),
            ("p", "Two cautions follow. If cotton bought at sixpence a pound rises to a shilling "
                  "after a bad harvest, each pound now passes a shilling into the yarn. That "
                  "does not make cotton variable capital: the change comes from the cotton "
                  "fields, not from the spinning, and Marx notes that speculators bet on the "
                  "least-worked material for that reason. And if ten men with ten cheap tools "
                  "are replaced by one man with an expensive machine, the proportion of c to v "
                  "changes enormously while their functions stay what they were. That proportion "
                  "returns, as the composition of capital, in Wages and Accumulation."),
            ("p", "The objection at its strongest is that machines are productive, and that "
                  "their owners are paid for that productivity. Marx grants half of it: an "
                  "instrument helps make use-values, and an invention like the one in the "
                  "sixfold case multiplies the yarn. What he denies is that "
                  "it adds value, which on his definition only living labour does. The dispute "
                  "is over what value is, and the arithmetic below follows the chapter's "
                  "answer."),
            ("p", "The lab values one day in a mill. A £1,000 machine with a life of 1,000 days "
                  "passes £1 a day; £10 of cotton passes £10; the day's wages are £6 and the "
                  "twelve hours add £12. Spin six times the cotton in the same day and the value "
                  "carried over jumps while the £12 does not move. Let cotton bought at £10 be "
                  "worth £20 by the time it is spun and the value transferred rises by £10, with "
                  "the new value again unchanged."),
            ("p", "With c and v named, the surplus can be measured against the part of capital "
                  "that produced it. The next lesson, “The Rate of Surplus Value”, does that."),
        ],
        "lab": ("capkit", {
            "mode": "surplus",
            "view": "transfer",
            "money_unit": "£",
            "preset": "machine",
            "presets": [
                {"id": "machine", "label": "Marx's £1,000 machine, 1,000 days, with £10 of cotton",
                 "machine_value": 1000, "machine_days": 1000, "materials": 10, "wage": 6,
                 "hours": 12, "necessary_hours": 6, "expect": {"suTransfer": "£11", "suProduct": "£23"}},
                {"id": "sixfold", "label": "Six times the cotton spun in the same day",
                 "machine_value": 1000, "machine_days": 1000, "materials": 60, "wage": 6,
                 "hours": 12, "necessary_hours": 6, "expect": {"suTransfer": "£61", "suProduct": "£73"}},
                {"id": "price-rise", "label": "Cotton bought at £10 is worth £20 when spun",
                 "machine_value": 1000, "machine_days": 1000, "materials": 20, "wage": 6,
                 "hours": 12, "necessary_hours": 6, "expect": {"suTransfer": "£21", "suProduct": "£33"}},
            ],
            "panel_title": "What the means of production pass on",
            "panel_intro": (
                "The machine passes its value divided by its life each day, and the cotton "
                "passes its value at the time it is spun. The wage is the day's wage bill and "
                "the hours are the mill's working day. Watch which tile moves in each preset."
            ),
        }),
        "steps_title": "Sorting a capital into c and v",
        "steps_intro": "Four steps for the outlays of any capital.",
        "steps": [
            ("Classify each outlay",
             "Raw material, auxiliary material and instruments are constant capital. What is "
             "paid for labour-power is variable capital. Nothing else enters."),
            ("Compute the daily wear",
             "For an instrument, divide its value by its life in days. That is what it passes "
             "into each day's product."),
            ("Value materials when used",
             "Materials pass over their value at the time they are used up, including any "
             "normal waste, whatever was paid for them."),
            ("Add the new value separately",
             "The value labour adds depends only on the hours worked. Add it to the value "
             "transferred to get the product's value."),
        ],
        "worked": {
            "title": "A day in the mill",
            "intro": [
                "A machine worth £1,000 lasts 1,000 days. In a twelve-hour day the mill spins "
                "£10 of cotton and pays £6 in wages, the value of six hours. You want the value "
                "transferred and the value of the day's product.",
            ],
            "lines": [
                "machine:  £1,000 / 1,000 days = £1 a day",
                "transferred:  £1 + £10 = £11",
                "new value:  12 h at £1 an hour = £12",
                "product:  £11 + £12 = £23",
            ],
            "after": [
                "The £11 is constant capital reappearing; the £12 replaces the £6 of variable "
                "capital and adds £6 more. With six times the cotton the transfer is £61 and the "
                "new value still £12.",
            ],
        },
        "quiz_title": "Constant and variable",
        "quiz": [
            {"q": "A loom worth £600 lasts 1,200 days. What value does it pass into each day's "
                  "product?",
             "a": ["£2", "£600", "£1/2", "£1,200"],
             "c": 2,
             "why": "Its value spread over its life is `600/1,200 = 1/2` of a pound a day. £2 "
                    "divides the wrong way; £600 and £1,200 are the whole value and the life."},
            {"q": "Which of these is variable capital?",
             "a": ["The cotton spun in the day",
                   "The wages paid for labour-power",
                   "The spinning machine",
                   "The coal burnt under the boiler"],
             "c": 1,
             "why": "Only the capital laid out on labour-power changes its value in production. "
                    "Cotton, machine and coal are means of production, raw, instrumental and "
                    "auxiliary, and all three are constant capital."},
            {"q": "Cotton bought at sixpence a pound rises to a shilling before it is spun. "
                  "What does each pound now pass into the yarn?",
             "a": ["Sixpence, what was paid for it",
                   "Nothing, since constant capital adds no value",
                   "Sixpence, plus the spinner's new value",
                   "A shilling, its value when it is used"],
             "c": 3,
             "why": "Value is fixed by the labour socially necessary now, so every pound of that "
                    "cotton is worth a shilling and passes a shilling over. Constant capital "
                    "adds no new value but does transfer its own; the spinner's new value is a "
                    "separate quantity."},
            {"q": "Which of these is constant capital but not fixed capital?",
             "a": ["The spinning machine",
                   "The cotton spun in the day",
                   "The spinners' wages",
                   "The factory building"],
             "c": 1,
             "why": "Cotton is constant because its value passes over unchanged, and it is used "
                    "up in a single day, so in Volume II's terms it is circulating capital. The "
                    "machine and the building are constant and fixed; wages are variable."},
        ],
        "mistakes": [
            ("Taking constant capital for fixed capital",
             "The pairs answer different questions. Constant and variable sort capital by "
             "whether it creates value; fixed and circulating, which Volume II introduces, sort "
             "it by how fast its value comes back. In the machine preset the cotton passes its "
             "whole £10 in one day and the machine passes £1: both are constant capital, and "
             "only the machine is fixed."),
            ("Thinking a productive machine passes on more value than it cost",
             "A machine can make the product far larger, as the sixfold preset shows. But over "
             "its whole life the £1,000 machine passes £1,000 into the products and not a "
             "penny more, because it can only give up the value it loses."),
            ("Calling v constant because the wage is a fixed sum",
             "The £6 paid in wages is a fixed sum when it is paid, a difficulty Marx raises "
             "against his own term in the next chapter. What varies is what replaces it in production: £12 of new "
             "value in a twelve-hour day."),
        ],
        "standard": (
            "Finish when you can classify the parts of a capital and compute what they "
            "transfer.",
            "Given a capital's outlays, classify each as constant or variable, compute the "
            "value an instrument transfers per day from its value and life, and compute the "
            "value of a day's product as value transferred plus new value."
        ),
        "note": (
            "The lab's machine wears out evenly, a thousandth a day, which is Marx's average "
            "and not a fact about machines; uneven wear and obsolescence change the daily "
            "figure and are left out. Whether machines add value or only use-value is the "
            "question the labour theory of value and its critics answer differently. The "
            "machine is Marx's; the cotton and wages beside it are illustrative."
        ),
    },
]
