"""Commodities and Money, lessons 1-4 -- Volume I, Chapter 1, one lesson per section.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals in the text are left out of the quotations, a
drop capital ("THE", "IT") is printed as an ordinary capital, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 1, l. 562 (opening sentence); l. 596 and l. 598 (the idle
    # labourer and the definition of socially necessary labour-time).
    {
        "slug": "the-two-factors-of-a-commodity",
        "title": "The Two Factors of a Commodity",
        "module": "Chapter 1 · Commodities",
        "one_line": "A commodity is a useful thing and a value, and its value is the labour-time society needs to make it, not the time its maker took.",
        "summary": (
            "Marx opens with the single commodity and finds two things in it: a use-value, "
            "which is a matter of the thing's body, and a value, which is a quantity of "
            "human labour in the abstract. Compute the socially necessary labour-time of "
            "a yard of linen from three weavers' hours and outputs, value a lot at it, and "
            "see what a slow weaver's extra hours are worth: much less than he spent."
        ),
        "key": [
            "a use-value: a useful thing, by its body",
            "value: abstract labour, counted in time",
            "time per unit = total hours / total output",
            "value of a lot = units × time per unit",
            "slow work is not more valuable work",
        ],
        "key_label": "The first section in five lines",
        "concepts_intro": (
            "Section 1 is short and very dense. It moves from what everyone can see, a "
            "useful thing with a price, to something nobody can see, and it does so in "
            "three steps."
        ),
        "concepts": [
            ("Use-value",
             "A commodity is first a thing that satisfies a want, whether such wants "
             "&ldquo;spring from the stomach or from fancy&rdquo;. Its usefulness belongs "
             "to its body: iron is useful as iron, linen as linen. Use-values are the "
             "material of all wealth, in any society."),
            ("Exchange value and value",
             "A quarter of wheat exchanges for so much silk, so much gold, so much iron. "
             "Because all of those are worth the same quarter of wheat, they must be equal "
             "to one another in something. Marx calls that something value, and exchange "
             "value is only the form in which it shows."),
            ("Socially necessary labour-time",
             "The magnitude of value is measured by labour-time, but not by the hours this "
             "producer happened to take. What counts is the time the article needs "
             "&ldquo;under the normal conditions of production&rdquo;, with average skill "
             "and intensity."),
        ],
        "read_title": "The passage first, then the section line by line",
        "read_intro": (
            "The chapter's first sentence comes first. The definition that does the "
            "section's real work comes in the middle, where Marx raises the obvious "
            "objection to his own argument."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 1, §1.</strong> &ldquo;The wealth of those "
                  "societies in which the capitalist mode of production prevails, presents "
                  "itself as &lsquo;an immense accumulation of commodities,&rsquo; its unit "
                  "being a single commodity. Our investigation must therefore begin with the "
                  "analysis of a commodity.&rdquo;"),
            ("p", "Look around the room you are in. Nearly everything in it was bought: made "
                  "by people you will never meet, for sale to whoever would pay. That is the "
                  "&ldquo;immense accumulation&rdquo; Marx means, and the phrase in his "
                  "quotation marks is his own, from his 1859 <em>Contribution to the "
                  "Critique of Political Economy</em>. He starts with one item from the pile "
                  "because in a society where almost everything is made for sale, the single "
                  "commodity is the unit from which the rest can be read. Nothing about money, "
                  "wages or profit is assumed yet."),
            ("p", "The first factor is the easy one. A commodity is &ldquo;an object outside "
                  "us, a thing that by its properties satisfies human wants&rdquo;. That "
                  "usefulness is its use-value, and it is a matter of the thing's body: a "
                  "diamond is useful as a diamond, and would be in any society. Use-values "
                  "&ldquo;constitute the substance of all wealth, whatever may be the social "
                  "form of that wealth&rdquo;. In this society they are also something else, "
                  "&ldquo;the material depositories of exchange value&rdquo;."),
            ("p", "Then the turn. A quarter of wheat exchanges for so much blacking, so much "
                  "silk, so much gold. Each of those is worth one quarter of wheat, so they "
                  "must be worth the same as one another, and Marx concludes that exchange "
                  "value is &ldquo;the phenomenal form, of something contained in it, yet "
                  "distinguishable from it&rdquo;. Write any exchange as `1 quarter corn = x "
                  "hundredweight iron` and the equation says that two different things are equal in "
                  "some third respect. It cannot be weight or colour or usefulness, because "
                  "exchange ignores exactly those. Take them away and one property is left: "
                  "each is a product of labour. Not of weaving or mining in particular, but "
                  "of &ldquo;human labour in the abstract&rdquo;. Crystals of that, Marx says, "
                  "are values."),
            ("p", "This step is where the book is most often challenged, and the challenge "
                  "deserves its full strength. Eugen von Böhm-Bawerk, the Austrian economist, "
                  "argued in 1896 that Marx's process of elimination is rigged: commodities "
                  "share other properties besides being products of labour, such as being "
                  "useful in general and being scarce, and Marx strikes those out without an "
                  "argument. The marginal-utility economists who wrote in the 1870s, Jevons, "
                  "Menger and Walras, explained exchange ratios from what an extra unit is "
                  "worth to the people trading, with no labour content behind them at all. "
                  "This Subject does not settle that dispute. It reads Marx's definitions and "
                  "computes what follows from them."),
            ("p", "Once value is labour, its magnitude is measured by labour's duration, in "
                  "hours and days. And Marx at once raises the objection you are probably "
                  "already forming:"),
            ("p", "<strong>Volume I, Chapter 1, §1.</strong> &ldquo;Some people might think "
                  "that if the value of a commodity is determined by the quantity of labour "
                  "spent on it, the more idle and unskilful the labourer, the more valuable "
                  "would his commodity be, because more time would be required in its "
                  "production. &hellip; The labour-time socially necessary is that required "
                  "to produce an article under the normal conditions of production, and with "
                  "the average degree of skill and intensity prevalent at the time.&rdquo;"),
            ("def", ("Socially necessary labour-time",
                     "The labour-time an article requires under the normal conditions of "
                     "production of its time, with average skill and intensity. A producer "
                     "who takes longer has spent more hours, but the article is worth only "
                     "the socially necessary ones.")),
            ("p", "Read the answer phrase by phrase. &ldquo;Normal conditions of "
                  "production&rdquo; means the looms and materials in general use, not the "
                  "ones in this workshop. &ldquo;The average degree of skill and "
                  "intensity&rdquo; rules out the idle labourer of the objection. And "
                  "&ldquo;prevalent at the time&rdquo; means the standard moves. Marx's "
                  "example is the power-loom: once it came into England, a hand-loom weaver "
                  "working exactly as before found that one hour of his labour represented "
                  "&ldquo;only half an hour's social labor&rdquo;. Nothing in his work "
                  "changed. The society around it did."),
            ("p", "The lab makes this a sum, with one model built in: it takes the average "
                  "over every producer as its stand-in for normal conditions. Three weavers "
                  "work at 1, 2 and 3 hours a yard and make 40, 40 and 20 yards. That is 180 "
                  "hours for 100 yards, so `9/5` of an hour a yard, and weaver C, who needs 3 "
                  "hours, sells each yard as `9/5` of an hour of value like everyone else. "
                  "Slow C down to 5 hours a yard and the average rises to `11/5`, by exactly "
                  "his share: 40 extra hours spread over 100 yards. His own yards are worth "
                  "`11/5` hours each, not 5. Of his 40 extra hours, his twenty yards carry 8; "
                  "the other 32 are spread over yards that other weavers made. The power-loom "
                  "preset runs Marx's example on the same three weavers: A and B halve their "
                  "hours, C works exactly as before, and the yard falls to `6/5` of an hour. "
                  "C's 3 hours a yard now count as `6/5`, so each hour he works represents "
                  "`2/5` of an hour of social labour where it represented `3/5`. In Marx's own "
                  "case the whole trade halves its time, and the hour falls to exactly half."),
            ("p", "The rest of the section follows from the definition. The more productive "
                  "labour is, the less time an article needs and the less it is worth: "
                  "Marx imagines carbon turned cheaply into diamonds, whose value &ldquo;might "
                  "fall below that of bricks&rdquo;. A thing can be useful without being a "
                  "value, like air or virgin soil, because no labour went into it. It can be "
                  "a useful product of labour without being a commodity, if you make it for "
                  "yourself. And nothing useless has value, because labour spent on a useless "
                  "thing does not count as labour."),
            ("p", "Value, then, is labour counted in hours, whatever the labour made. The "
                  "next lesson, “The Twofold Character of Labour”, asks how one and the same "
                  "work can be weaving and also simply hours of human labour."),
        ],
        "lab": ("capkit", {
            "mode": "value",
            "view": "snlt",
            "money_unit": "hours",
            "qty_unit": "yards",
            "preset": "linen",
            "presets": [
                {"id": "linen", "label": "Three weavers at 1, 2 and 3 hours a yard",
                 "producers": [{"name": "weaver A", "hours": 1, "output": 40},
                               {"name": "weaver B", "hours": 2, "output": 40},
                               {"name": "weaver C", "hours": 3, "output": 20}],
                 "basis": "per-unit", "lot": 20, "expect": {"vaSnlt": "9/5 h", "vaLotValue": "36 h"}},
                {"id": "slow", "label": "Weaver C slows to 5 hours a yard",
                 "producers": [{"name": "weaver A", "hours": 1, "output": 40},
                               {"name": "weaver B", "hours": 2, "output": 40},
                               {"name": "weaver C", "hours": 5, "output": 20}],
                 "basis": "per-unit", "lot": 20, "expect": {"vaSnlt": "11/5 h", "vaLotValue": "44 h"}},
                {"id": "power-loom", "label": "Power-looms: weavers A and B at half their hours",
                 "producers": [{"name": "weaver A", "hours": "1/2", "output": 40},
                               {"name": "weaver B", "hours": 1, "output": 40},
                               {"name": "weaver C", "hours": 3, "output": 20}],
                 "basis": "per-unit", "lot": 20, "expect": {"vaSnlt": "6/5 h", "vaLotValue": "24 h"}},
            ],
            "panel_title": "What a yard of linen is worth",
            "panel_intro": (
                "Each weaver's hours per yard and output go in; the lab adds the hours, "
                "divides by the yards and values a lot of 20 yards at the result. Choose the "
                "slow preset and compare weaver C's own hours per yard in the table with the "
                "socially necessary time in the tile."
            ),
        }),
        "steps_title": "Computing the value of a lot",
        "steps_intro": "Four steps, the same for any product made by several producers.",
        "steps": [
            ("Total the hours",
             "For each producer multiply hours per unit by units made, and add the "
             "products. If the hours are already totals, add them as they are."),
            ("Total the output",
             "Add the units every producer made. The lot being valued is a sample of "
             "this whole output, whoever made it."),
            ("Divide",
             "Socially necessary time per unit is total hours divided by total output. "
             "On this lab's model it is an average weighted by output, so a large producer "
             "moves it more than a small one."),
            ("Value the lot and compare",
             "Multiply the units in the lot by the time per unit. Then set each "
             "producer's own hours per unit beside it: the difference is time spent that "
             "the product does not carry, or time saved that it does."),
        ],
        "worked": {
            "title": "Three weavers, one price per yard",
            "intro": [
                "Take the first preset. Weavers A, B and C need 1, 2 and 3 hours a yard and "
                "make 40, 40 and 20 yards. You want the value of 20 yards, and what weaver C "
                "loses on each of his.",
            ],
            "lines": [
                "hours:  40·1 + 40·2 + 20·3 = 180 h",
                "yards:  40 + 40 + 20 = 100",
                "per yard:  180 / 100 = 9/5 h",
                "lot of 20 yards:  20 · 9/5 = 36 h",
                "weaver C:  3 − 9/5 = 6/5 h a yard not counted",
            ],
            "after": [
                "Weaver C's twenty yards are worth 36 hours, though he spent 60 on them. "
                "In the slow preset he spends 100, the yard rises to `11/5` and his twenty "
                "yards are worth 44 hours: of his 40 extra hours, 8 show up in his own yards "
                "and the other 32 are spread over the 80 yards the others made.",
            ],
        },
        "quiz_title": "Value by the hours society needs",
        "quiz": [
            {"q": "Two weavers make linen. One works at 2 hours a yard and makes 30 yards; "
                  "the other works at 4 hours a yard and makes 10. On the lab's model, what "
                  "is the socially necessary time per yard?",
             "a": ["5/2 hours", "3 hours", "2 hours", "4 hours"],
             "c": 0,
             "why": "Total hours are `30 · 2 + 10 · 4 = 100` for 40 yards, so `100/40 = 5/2`. "
                    "Three hours is the plain average of 2 and 4, which ignores that the "
                    "faster weaver makes three times as much. Two and four are one weaver's "
                    "own time each, not the social time."},
            {"q": "In the slow preset weaver C needs 5 hours for a yard. What is one of his "
                  "yards worth?",
             "a": ["5 hours", "11/5 hours", "9/5 hours", "3 hours"],
             "c": 1,
             "why": "Every yard is worth the socially necessary time, which is now "
                    "`220/100 = 11/5` hours. Five hours is what C spent, which the definition "
                    "excludes. `9/5` was the figure before he slowed down, and 3 hours was his "
                    "own time then."},
            {"q": "After the power-loom, a hand-loom weaver works exactly as before. On "
                  "Marx's account, what does one hour of his labour now represent?",
             "a": ["One hour, because he still works for an hour",
                   "Half an hour of social labour",
                   "Two hours, because his work is now harder to find",
                   "No value at all, because his loom is obsolete"],
             "c": 1,
             "why": "The power-loom halved the labour needed for a given quantity of cloth, "
                    "so the hand-loom weaver's hour counts as &ldquo;only half an hour's "
                    "social labor&rdquo;. His own hour is not the measure. His product still "
                    "has value, only less of it, and scarcity of his kind of work plays no "
                    "part in the definition."},
            {"q": "Which of these is a use-value without being a value, on the chapter's "
                  "definitions?",
             "a": ["Linen woven slowly by hand for sale",
                   "Air",
                   "A coat a tailor makes for sale",
                   "A machine-made yard of linen"],
             "c": 1,
             "why": "Air is useful, but no labour was spent producing it, so it has no "
                    "value. The other three are useful products of labour made for sale, "
                    "so each is a use-value and a value, the slow linen included."},
        ],
        "mistakes": [
            ("Thinking a commodity made more slowly is worth more",
             "Marx raises this objection himself: &ldquo;the more idle and unskilful the "
             "labourer, the more valuable would his commodity be&rdquo;. It confuses the "
             "hours one producer spent with the hours society needs. In the slow preset "
             "weaver C takes 5 hours a yard, yet his yard is worth `11/5` hours, the same "
             "as everyone's. His slowness raised the social figure only by his share of the "
             "output, and of his 40 extra hours his own yards carry 8."),
            ("Reading exchange value as value itself",
             "A quarter of wheat has as many exchange values as there are things to trade "
             "it for, and they change with time and place. Marx's claim is that all of them "
             "express one thing that is not itself a ratio: the labour the wheat contains. "
             "The ratios are how value shows, and the next lessons are about how."),
            ("Treating anything useful as having value",
             "Air, virgin soil and natural meadows are useful and have no value, because no "
             "labour made them. Usefulness is required, since useless labour creates no "
             "value, but it is not what value measures."),
        ],
        "standard": (
            "Finish when you can value a lot from several producers' hours and outputs.",
            "Given producers' hours per unit and outputs, compute the socially necessary "
            "time per unit and the value of a stated lot, and state how much of one "
            "producer's own time per unit the product does not carry."
        ),
        "note": (
            "The lab's average over every producer is a model of Marx's &ldquo;normal "
            "conditions&rdquo;, not his definition. A market in which one technique "
            "dominates may be regulated by that technique rather than by the mean, and "
            "Volume III, Chapter 10 shows the regulating value need not be the average. "
            "On the average, a slow weaver's extra hours raise every yard's value a little; "
            "a market regulated by the normal technique would not register them at all. "
            "The weavers' figures are illustrative; Marx gives none."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 1, l. 611 (the pivot); l. 651 (two coats, one coat).
    {
        "slug": "the-twofold-character-of-labour",
        "title": "The Twofold Character of Labour",
        "module": "Chapter 1 · Commodities",
        "one_line": "The same work is tailoring, which makes coats, and human labour, which makes value; productivity changes the first and not the second.",
        "summary": (
            "Labour has two sides, as the commodity does: concrete useful labour, which "
            "makes a coat, and abstract human labour, which makes the coat's value. Run a "
            "day of tailoring at three levels of productivity and compute the value of a "
            "coat and of the day's output: the coats change, the hours do not."
        ),
        "key": [
            "concrete labour makes use-values",
            "abstract labour makes value",
            "productivity: more use-values per hour",
            "same hours: same value, any productivity",
            "value per unit = hours / units made",
        ],
        "key_label": "Two sides of one labour",
        "concepts_intro": (
            "Marx calls this distinction &ldquo;the pivot on which a clear comprehension "
            "of political economy turns&rdquo;. It is short to state and easy to lose "
            "hold of."
        ),
        "concepts": [
            ("Useful labour",
             "Tailoring and weaving differ in aim, tools, materials and result. As "
             "useful labour each is counted by what it makes: so many coats, so many "
             "yards. Coats are not exchanged for coats, so commodities need different "
             "kinds of useful labour behind them."),
            ("Abstract human labour",
             "Set aside what the labour makes and each is an expenditure of human "
             "&ldquo;brains, nerves, and muscles&rdquo;. As value, labour counts only by "
             "how much of it there is, measured in time."),
            ("Productivity belongs to useful labour",
             "A better method lets tailoring make more coats an hour. It does not make an "
             "hour longer. So the same hours give the same value whatever the "
             "productivity, spread over more coats or fewer."),
        ],
        "read_title": "The pivot, and then two coats",
        "read_intro": (
            "Section 2 opens with Marx's claim to priority. The passage on two coats near "
            "its end is the arithmetic the claim leads to."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 1, §2.</strong> &ldquo;At first sight a "
                  "commodity presented itself to us as a complex of two things&mdash;use-value "
                  "and exchange-value. Later on, we saw also that labour, too, possesses the "
                  "same two-fold nature; for, so far as it finds expression in value, it does "
                  "not possess the same characteristics that belong to it as a creator of "
                  "use-values. I was the first to point out and to examine critically this "
                  "two fold nature of the labour contained in commodities. As this point is "
                  "the pivot on which a clear comprehension of political economy turns, we "
                  "must go more into detail.&rdquo;"),
            ("p", "That is a large claim, and it is fair to ask what it is a claim against. "
                  "Adam Smith and David Ricardo, the two great British economists before "
                  "Marx, had already said that labour is the measure of value. Smith even "
                  "wrote that equal quantities of labour have equal value for the worker, "
                  "whatever the labour. What Marx says they missed is not that labour counts "
                  "but that it counts twice over, in two different ways, and that the two "
                  "ways can move in opposite directions."),
            ("p", "Take the first way. The coat is made by tailoring, &ldquo;a special sort "
                  "of productive activity, the nature of which is determined by its aim, mode "
                  "of operation, subject, means, and result&rdquo;. As useful labour, "
                  "tailoring is counted by what it makes. And it must differ from weaving, "
                  "because &ldquo;Coats are not exchanged for coats&rdquo;: commodities only "
                  "meet each other because a social division of labour lies behind them. "
                  "That division does not require commodities, though. A factory divides its "
                  "work by plan, and an old Indian village community did so without anyone "
                  "selling anything to anyone."),
            ("p", "Useful labour is also not the only source of the coat. Take the labour "
                  "away and a material substratum is left, &ldquo;furnished by Nature without "
                  "the help of man&rdquo;. Marx borrows a line from William Petty, the "
                  "seventeenth-century physician who surveyed Ireland and wrote some of the "
                  "first English economics: labour is the father of material wealth &ldquo;and "
                  "the earth its mother&rdquo;. Wealth in the sense of useful things has two "
                  "parents. Value, Marx will insist, has only one."),
            ("p", "Now the second way. Set aside what tailoring and weaving make and each is "
                  "&ldquo;a productive expenditure of human brains, nerves, and "
                  "muscles&rdquo;. That is the labour that forms value, and as such it is "
                  "counted only in time: &ldquo;How much? How long a time?&rdquo; rather than "
                  "&ldquo;How and What&rdquo;. Marx adds that skilled labour counts as "
                  "&ldquo;multiplied simple labour&rdquo;, an hour of it equal to several "
                  "hours of the simple kind, and then, for simplicity, treats every hour as "
                  "simple from here on. The book never computes that multiplier from "
                  "anything, and neither does this lesson. Böhm-Bawerk pressed on exactly this "
                  "point: if the only evidence for how many simple hours a skilled hour counts "
                  "as is the ratio at which the two kinds of product exchange, then the "
                  "reduction uses the exchange ratios it was meant to explain. The chapter's "
                  "answer is only that the proportions &ldquo;are established by a social "
                  "process that goes on behind the backs of the producers&rdquo;."),
            ("p", "The two sides part company the moment productivity changes, and that is "
                  "the passage the whole distinction exists for:"),
            ("p", "<strong>Volume I, Chapter 1, §2.</strong> &ldquo;An increase in the "
                  "quantity of use-values is an increase of material wealth. With two coats "
                  "two men can be clothed, with one coat only one man. Nevertheless, an "
                  "increased quantity of material wealth may correspond to a simultaneous "
                  "fall in the magnitude of its value.&rdquo;"),
            ("p", "Think of any product that got cheaper as it got easier to make. There is "
                  "more of it, which is a real gain, and each unit is worth less. Marx's "
                  "explanation is that productivity &ldquo;has reference, of course, only to "
                  "labour of some useful concrete form&rdquo;. It changes how many coats an "
                  "hour of tailoring yields. It cannot change the hour, so &ldquo;the same "
                  "labour, exercised during equal periods of time, always yields equal amounts "
                  "of value&rdquo;."),
            ("p", "The lab runs one tailor's ten-hour day three ways. At first ten hours "
                  "make one coat, worth 10 hours. Double the productivity and ten hours make "
                  "two coats, each worth 5 hours, the pair still worth 10. Halve it and ten "
                  "hours make half a coat, so a whole coat is worth 20 hours. Marx puts the "
                  "doubled case the other way round, as the labour a coat needs being halved: "
                  "two coats are then &ldquo;only worth as much as one was before&rdquo;. The skill multiplier is fixed at 1 "
                  "throughout, which is the assumption Marx says he is making."),
            ("p", "Weaving runs alongside. On Marx's figures 20 yards of linen are worth one "
                  "coat. When tailoring doubles its productivity and weaving does not, a coat "
                  "is worth 5 hours and so only 10 yards: the linen is unchanged, and what it "
                  "will fetch in coats has doubled. How the linen &ldquo;says&rdquo; that is "
                  "the subject of the next section."),
            ("p", "Two sides of one labour, then, and only one of them makes value. The next "
                  "lesson, “The Form of Value”, asks how that value, which no one can see or "
                  "touch, comes to be expressed at all."),
        ],
        "lab": ("capkit", {
            "mode": "value",
            "view": "skill",
            "money_unit": "hours",
            "qty_unit": "coats",
            "preset": "coat",
            "presets": [
                {"id": "coat", "label": "A ten-hour day of tailoring makes 1 coat",
                 "producers": [{"name": "tailor", "hours": 10, "output": 1}],
                 "basis": "total", "skill": 1, "lot": 1, "expect": {"vaPerUnit": "10 h", "vaLotValue": "10 h"}},
                {"id": "doubled", "label": "Productivity doubles: 2 coats in ten hours",
                 "producers": [{"name": "tailor", "hours": 10, "output": 2}],
                 "basis": "total", "skill": 1, "lot": 2, "expect": {"vaPerUnit": "5 h", "vaLotValue": "10 h"}},
                {"id": "halved", "label": "Productivity halves: half a coat in ten hours",
                 "producers": [{"name": "tailor", "hours": 10, "output": "1/2"}],
                 "basis": "total", "skill": 1, "lot": "1/2", "expect": {"vaPerUnit": "20 h", "vaLotValue": "10 h"}},
            ],
            "panel_title": "One day of tailoring, three productivities",
            "panel_intro": (
                "The tailor's hours are a ten-hour day in total, and the lot is the day's "
                "output. Step through the three presets and watch the two tiles: one moves "
                "with productivity, the other does not. Skill stays at 1, as Marx assumes."
            ),
        }),
        "steps_title": "Separating the two sides",
        "steps_intro": "Four steps for any change in how productive a kind of labour is.",
        "steps": [
            ("Fix the hours",
             "Hold the labour-time constant, a day or a week. That is the abstract side, "
             "and it fixes how much value the period produces."),
            ("Count the use-values",
             "Write down how many units the hours make before and after the change. That "
             "is the useful side, and productivity acts on it alone."),
            ("Divide for the value per unit",
             "Value per unit is the hours divided by the units made. More units in the same "
             "hours means less value in each."),
            ("Check the total",
             "Multiply back: units times value per unit must return the hours. If the "
             "total moved, either the hours changed or a multiplier for skill was "
             "applied."),
        ],
        "worked": {
            "title": "Two coats where there was one",
            "intro": [
                "A tailor's ten-hour day makes one coat. A better method lets the same day "
                "make two. You want the value of a coat and of the day's output, before and "
                "after.",
            ],
            "lines": [
                "before:  10 h / 1 coat = 10 h a coat",
                "after:   10 h / 2 coats = 5 h a coat",
                "day's output before:  1 · 10 = 10 h",
                "day's output after:   2 · 5 = 10 h",
            ],
            "after": [
                "The use-values doubled and the value did not. Against linen, which is still "
                "20 yards for 10 hours, a coat now fetches 10 yards instead of 20.",
            ],
        },
        "quiz_title": "Useful labour and value-creating labour",
        "quiz": [
            {"q": "A tailor's ten-hour day used to make 1 coat and now makes 2. On the "
                  "chapter's definitions, what is the day's output worth?",
             "a": ["10 hours", "20 hours", "5 hours", "It cannot be said without a price"],
             "c": 0,
             "why": "The same hours yield the same value whatever the productivity, so the "
                    "two coats together carry 10 hours, 5 each. Twenty hours would count each "
                    "coat at the old value; 5 hours is one coat's value, not the day's. No "
                    "price is needed, because the value is measured in hours."},
            {"q": "Tailoring's productivity halves, so a ten-hour day makes half a coat. What "
                  "is one coat now worth?",
             "a": ["5 hours", "10 hours", "20 hours", "15 hours"],
             "c": 2,
             "why": "A whole coat now needs two days of ten hours, so it is worth 20 hours. "
                    "Ten hours is the old figure, and 5 hours is the doubled case. Fifteen "
                    "hours matches no change in the lesson."},
            {"q": "Which change alters the value created in a ten-hour day of tailoring, on "
                  "the chapter's assumptions?",
             "a": ["A new method that doubles the coats made",
                   "A method that halves the coats made",
                   "Working twelve hours instead of ten",
                   "Making waistcoats instead of coats"],
             "c": 2,
             "why": "Value is measured by the labour-time spent, so only a change in the "
                    "hours changes it. Doubling or halving productivity changes how many "
                    "coats carry the same ten hours, and switching product changes the "
                    "useful labour, not its quantity."},
            {"q": "Marx says skilled labour counts as &ldquo;multiplied simple "
                  "labour&rdquo;. What does Chapter 1 do with that multiplier?",
             "a": ["Computes it from the cost of training",
                   "Assumes every hour is simple labour from then on",
                   "Sets it equal to the ratio of wages",
                   "Shows that it is always 2"],
             "c": 1,
             "why": "He says the reduction is made by a social process behind the producers' "
                    "backs, and that &ldquo;for simplicity's sake&rdquo; he will treat all "
                    "labour as simple. He computes it from nothing, so it is not derived from "
                    "training costs or wages here, and no value is given for it."},
        ],
        "mistakes": [
            ("Thinking more useful things always means more value",
             "The doubled preset refutes it in one line: the day's output goes from 1 coat "
             "to 2 and stays worth 10 hours. More use-values is more material wealth, which "
             "Marx grants, and it may come with a fall in value per unit, which is the "
             "&ldquo;antagonistic movement&rdquo; this section explains."),
            ("Treating productivity as a property of the hour",
             "Productivity is an attribute of concrete labour: how much of a definite "
             "useful thing an hour makes. Once the concrete form is set aside, as it is in "
             "counting value, productivity has nothing to act on, and an hour is an hour."),
            ("Taking the skill multiplier as computed",
             "The skill field exists, and the lab will multiply by whatever you type. Marx "
             "gives no way to derive the number, and says he will ignore it. A lesson that "
             "sets it to 3 has assumed 3, not found it."),
        ],
        "standard": (
            "Finish when you can separate the two sides of a change in productivity.",
            "Given hours and units before and after a change in productivity, compute the "
            "value per unit and of the period's output, and state which of the two moved "
            "and which did not."
        ),
        "note": (
            "Every hour here is counted as simple labour, as Marx assumes. The reduction of "
            "skilled to simple labour is stated in the chapter and never computed; a lab "
            "that multiplied by a skill factor would be assuming the number it printed. "
            "The tailor's figures are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 1, l. 677-685 (the elementary form; the two poles);
    # l. 739 and l. 749 (the coat's value halves; relative value can vary).
    {
        "slug": "the-form-of-value",
        "title": "The Form of Value",
        "module": "Chapter 1 · Commodities",
        "one_line": "In 20 yards of linen = 1 coat the linen's value is expressed and the coat is the material it is expressed in; four forms lead from that equation to money.",
        "summary": (
            "Value cannot be seen in a commodity alone; it shows only when one commodity is "
            "set equal to another. Read the elementary form, name its relative and "
            "equivalent poles, follow it through the expanded and general forms to the "
            "money form, and compute how the linen's expression in coats moves when only "
            "the coat's value changes."
        ),
        "key": [
            "x of A = y of B: A relative, B equivalent",
            "expanded: A = B, or = C, or = D …",
            "general: B, C, D … each = A",
            "money: the equivalent is gold",
            "linen in coats = linen hours / coat hours",
        ],
        "key_label": "Four forms of one value",
        "concepts_intro": (
            "Section 3 is the longest and hardest part of the chapter. Its subject is one "
            "equation, read slowly, and then three ways of extending it."
        ),
        "concepts": [
            ("Relative form and equivalent form",
             "In 20 yards of linen = 1 coat the linen is the commodity whose value is "
             "being expressed: it is in the relative form. The coat is the material the "
             "value is expressed in: it is in the equivalent form. The same commodity "
             "cannot be both in one expression."),
            ("The equivalent shows value in its body",
             "As equivalent, the coat counts as value made visible, as if being worth 20 "
             "yards were a natural property of coats, like weight. It is not; it holds only "
             "within the relation."),
            ("From the elementary form to money",
             "The expanded form sets one commodity against every other. Reverse it and "
             "every commodity expresses its value in one, the general equivalent. When "
             "custom fixes that role on gold, the general form becomes the money form."),
        ],
        "read_title": "The equation, and who is speaking in it",
        "read_intro": (
            "Marx sets the equation down twice, once in letters and once in linen and "
            "coats, and then says that the whole mystery is in it."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 1, §3.</strong> &ldquo;20 yards of linen=1 "
                  "coat, or 20 yards of linen are worth 1 coat. &hellip; The whole mystery of "
                  "the form of value lies hidden in this elementary form. Its analysis, "
                  "therefore, is our real difficulty. &hellip; The linen expresses its value "
                  "in the coat; the coat serves as the material in which that value is "
                  "expressed. The former plays an active, the latter a passive, part.&rdquo;"),
            ("p", "This is the part of Chapter 1 that readers most often give up on, so it is "
                  "worth saying plainly what it is for. Sections 1 and 2 found value behind "
                  "exchange. But &ldquo;not an atom of matter enters into its "
                  "composition&rdquo;: turn a coat over as long as you like and you will not "
                  "find its value. Value can only appear in a relation between commodities. "
                  "Section 3 asks what that relation looks like at its simplest, and follows "
                  "it until it becomes money."),
            ("p", "Take the equation as a sentence. Its subject is the linen. &ldquo;The "
                  "linen expresses its value in the coat&rdquo;: the linen is in the "
                  "<strong>relative form</strong>, the coat in the <strong>equivalent "
                  "form</strong>. The two are &ldquo;poles of the same expression&rdquo;. Read "
                  "it backwards, 1 coat = 20 yards of linen, and the roles change: now the "
                  "coat's value is being expressed, in linen. Which commodity plays which part "
                  "depends only on its position. And `20 yards of linen = 20 yards of linen` "
                  "expresses nothing at all."),
            ("p", "The equivalent is the strange one. In the equation the coat counts as "
                  "value embodied, &ldquo;just as many a man strutting about in a gorgeous "
                  "uniform counts for more than when in mufti&rdquo;. Marx compares it with "
                  "weighing a sugar-loaf against iron: the iron stands for weight alone. Then "
                  "he stops the analogy. Weight is a natural property of both bodies; value "
                  "is &ldquo;something purely social&rdquo;. Yet because it is the coat's own "
                  "body that does the expressing, being exchangeable looks like a property of "
                  "the coat. That appearance is the seed of the next lesson."),
            ("p", "Then the arithmetic. Marx takes four cases: the linen's value changes, the "
                  "coat's changes, both change in the same proportion, both change by "
                  "different amounts. If the linen's value doubles and the coat's does not, 20 "
                  "yards fetch 2 coats. If the coat's value doubles and the linen's does not, "
                  "20 yards fetch half a coat. If both change in the same proportion, nothing "
                  "in the equation moves. Inside the second case is the one the lab is built "
                  "around:"),
            ("p", "<strong>Volume I, Chapter 1, §3.</strong> &ldquo;If, on the other hand, the "
                  "value of the coat sinks by one half, then 20 yards of linen=2 coats. "
                  "&hellip; The relative value of a commodity may vary, although its value "
                  "remains constant.&rdquo;"),
            ("p", "The linen's relative value, its value expressed in coats, has doubled, and "
                  "nothing about linen changed. That is why the equivalent never expresses its "
                  "own value. When 40 yards of linen are worth 2 coats, the coats "
                  "appear only as a quantity of an article; they &ldquo;can never express the "
                  "quantity of their own value&rdquo;. Marx names Samuel Bailey, whose 1825 "
                  "<em>Critical Dissertation</em> argued that value is nothing but the ratio "
                  "in which things exchange, with no absolute quantity behind it. That is a "
                  "serious position, and close to how most economists still talk about "
                  "relative prices. Marx's reply is the case just computed: the same change in "
                  "the ratio can come from a change in either commodity, so the ratio alone "
                  "cannot tell you which one changed."),
            ("p", "Aristotle got remarkably far with this. He saw that 5 beds = 1 house is no "
                  "different from 5 beds = so much money, and that exchange needs equality and "
                  "equality needs commensurability. Then he stopped: it is &ldquo;in reality, "
                  "impossible&rdquo; for such unlike things to be commensurable. Marx's "
                  "explanation of where Aristotle stopped is historical. Greek society rested "
                  "on slave labour, so the idea that all human labour is equal, which the "
                  "equation silently asserts, could not yet have the &ldquo;fixity of a "
                  "popular prejudice&rdquo;."),
            ("p", "The rest of the section builds out from the one equation. In the "
                  "<strong>expanded form</strong> the linen is set against everything: 20 "
                  "yards of linen = 1 coat, or 10 lb tea, or 40 lb coffee, or 1 quarter corn, "
                  "or 2 ounces gold, or ½ ton iron. Its defect is that it never ends and no two "
                  "commodities share one. Reverse it, and every commodity expresses its value "
                  "in linen: the <strong>general form</strong>, with linen as the general "
                  "equivalent. Put gold where linen stood and nothing changes in the equations, "
                  "only in which commodity custom has fixed on. That is the "
                  "<strong>money form</strong>, and 20 yards of linen = 2 ounces of gold is "
                  "the linen's price."),
            ("p", "In the lab, Marx's seven commodities are given 20 hours a lot, so that every "
                  "equation in his list balances; the hours are illustrative, the equations are "
                  "his. Switch the form of value between the four stages and the equations "
                  "rewrite themselves from the hours. Then choose the preset where the coat "
                  "cheapens, and watch the linen fetch twice as many coats."),
            ("p", "The equivalent form made exchangeability look like a property of a coat, "
                  "and then of gold. The next lesson, “The Fetishism of Commodities”, asks why "
                  "a relation between people's labour should look like a property of things "
                  "at all."),
        ],
        "lab": ("capkit", {
            "mode": "form",
            "view": "stage",
            "stage": "elementary",
            "money_unit": "hours",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: linen, coat, tea, coffee, corn, gold, iron",
                 "goods": [{"name": "linen", "qty": 20, "unit": "yards", "hours": 20},
                           {"name": "coat", "qty": 1, "unit": "", "hours": 20},
                           {"name": "tea", "qty": 10, "unit": "lb", "hours": 20},
                           {"name": "coffee", "qty": 40, "unit": "lb", "hours": 20},
                           {"name": "corn", "qty": 1, "unit": "quarter", "hours": 20},
                           {"name": "gold", "qty": 2, "unit": "ounces", "hours": 20},
                           {"name": "iron", "qty": "1/2", "unit": "ton", "hours": 20}],
                 "equivalent": "linen",
                 "marx": ["20 linen = 1 coat", "20 linen = 10 tea", "20 linen = 40 coffee",
                          "20 linen = 1 corn", "20 linen = 2 gold", "20 linen = 1/2 iron"],
                 "expect": {"foEquation": "20 yards linen = 1 coat", "foRelative": "1 coat"}},
                {"id": "coat-cheapens", "label": "The coat's hours halve; the linen's do not",
                 "goods": [{"name": "linen", "qty": 20, "unit": "yards", "hours": 20},
                           {"name": "coat", "qty": 1, "unit": "", "hours": 10},
                           {"name": "tea", "qty": 10, "unit": "lb", "hours": 20},
                           {"name": "coffee", "qty": 40, "unit": "lb", "hours": 20},
                           {"name": "corn", "qty": 1, "unit": "quarter", "hours": 20},
                           {"name": "gold", "qty": 2, "unit": "ounces", "hours": 20},
                           {"name": "iron", "qty": "1/2", "unit": "ton", "hours": 20}],
                 "equivalent": "linen", "expect": {"foEquation": "20 yards linen = 2 coat", "foRelative": "2 coat"}},
                {"id": "gold", "label": "Gold as the equivalent: the price form",
                 "goods": [{"name": "linen", "qty": 20, "unit": "yards", "hours": 20},
                           {"name": "gold", "qty": 2, "unit": "ounces", "hours": 20},
                           {"name": "coat", "qty": 1, "unit": "", "hours": 20},
                           {"name": "tea", "qty": 10, "unit": "lb", "hours": 20},
                           {"name": "coffee", "qty": 40, "unit": "lb", "hours": 20},
                           {"name": "corn", "qty": 1, "unit": "quarter", "hours": 20},
                           {"name": "iron", "qty": "1/2", "unit": "ton", "hours": 20}],
                 "equivalent": "gold",
                 "marx": ["20 linen = 2 gold"],
                 "expect": {"foEquation": "20 yards linen = 2 ounces gold", "foRelative": "2 ounces gold"}},
            ],
            "panel_title": "One set of values, written four ways",
            "panel_intro": (
                "The first commodity listed is the one whose value the elementary and "
                "expanded forms express; the general and money forms use the equivalent the "
                "preset names. Step the form of value from elementary to general with Marx's "
                "figures, choose the gold preset for the money form, and then choose the "
                "preset where the coat cheapens."
            ),
        }),
        "steps_title": "Reading an expression of value",
        "steps_intro": "Four steps for any equation of the form x of A = y of B.",
        "steps": [
            ("Find the subject",
             "The commodity on the left is the one whose value is expressed. It is in the "
             "relative form. The commodity on the right is the material of the expression, "
             "in the equivalent form."),
            ("Compute the quantity",
             "The lot of A fetches as much of B as holds the same hours: hours in the lot "
             "of A divided by hours per unit of B."),
            ("Change one value at a time",
             "Change A's hours with B's fixed and A's relative value moves directly with "
             "them. Change B's with A's fixed and it moves inversely. Change both in "
             "proportion and it does not move."),
            ("Name the form",
             "One equation is the elementary form; one commodity against many is the "
             "expanded form; many against one is the general form; the general form with "
             "gold as the one is the money form."),
        ],
        "worked": {
            "title": "The coat cheapens",
            "intro": [
                "Twenty yards of linen and one coat each take 20 hours. A new method halves "
                "the hours in a coat. You want what 20 yards of linen now fetch.",
            ],
            "lines": [
                "before:  20 yards linen (20 h) = 1 coat (20 h)",
                "after:   a coat takes 10 h",
                "coats fetched:  20 h / 10 h = 2",
                "so:  20 yards linen = 2 coats",
            ],
            "after": [
                "The linen's relative value doubled, measured in coats, while its own value "
                "stayed at 20 hours. Measured against tea or gold, which did not change, the "
                "linen fetches exactly what it did.",
            ],
        },
        "quiz_title": "Relative and equivalent",
        "quiz": [
            {"q": "In &ldquo;10 lb of tea = 40 lb of coffee&rdquo;, which commodity's value "
                  "is being expressed?",
             "a": ["The tea's", "The coffee's", "Both equally", "Neither; it is only a ratio"],
             "c": 0,
             "why": "The commodity on the left is in the relative form, and its value is "
                    "expressed in the body of the one on the right. The coffee is the "
                    "equivalent, and Marx says the equivalent's own value gets no "
                    "expression. The equation is more than a ratio, because it asserts that "
                    "the two are equal as values."},
            {"q": "Twenty yards of linen and one coat each take 20 hours. Then the hours in a "
                  "coat double and the linen's stay the same. What do 20 yards of linen "
                  "fetch?",
             "a": ["2 coats", "1 coat", "Half a coat", "4 coats"],
             "c": 2,
             "why": "A coat now holds 40 hours, so 20 hours of linen fetch "
                    "`20/40 = 1/2` coat. Two coats is the case where the coat's value halves; "
                    "one coat would need both values to change in proportion."},
            {"q": "The hours needed for linen and for coats both fall by half. What happens "
                  "to 20 yards of linen = 1 coat?",
             "a": ["It becomes 20 yards of linen = 2 coats",
                   "It becomes 20 yards of linen = ½ coat",
                   "It is unchanged",
                   "It can no longer be written"],
             "c": 2,
             "why": "Both lots now hold 10 hours, so they are still equal. Marx's third case: "
                    "the change in value shows only against a third commodity whose value "
                    "stayed the same."},
            {"q": "What distinguishes the money form from the general form?",
             "a": ["Every equation balances only in the money form",
                   "Gold has replaced linen as the general equivalent",
                   "The commodities now have values, not only prices",
                   "Each commodity is expressed in every other one"],
             "c": 1,
             "why": "Marx says there is no difference between the general and money forms "
                    "except that gold has taken the equivalent's place. The equations balance "
                    "in every form, values exist before any of them, and one commodity "
                    "expressed in every other is the expanded form."},
        ],
        "mistakes": [
            ("Thinking the coat's value is what “20 yards of linen = 1 coat” expresses",
             "The equation expresses the linen's value, in coats. The coat-cheapens preset "
             "shows it: the coat's value halves and the equation becomes 20 yards of "
             "linen = 2 coats, a change in what the linen fetches, while the coat's new "
             "value of 10 hours appears nowhere in it. To express the coat's value the "
             "equation must be read the other way round."),
            ("Reading a change in a ratio as a change in the commodity on the left",
             "When 20 yards of linen go from 1 coat to 2, the cause may be that linen "
             "doubled in value or that the coat halved. The ratio alone cannot say which. "
             "Compare the linen with a third commodity whose value has not changed."),
            ("Taking the general equivalent's power as natural",
             "Linen is exchangeable for everything in the general form only because every "
             "other commodity expresses its value in it, &ldquo;and that by their own "
             "act&rdquo;. Gold's place in the money form is the same role fixed by "
             "custom on one commodity, not a property of the metal."),
        ],
        "standard": (
            "Finish when you can read an expression of value and compute its movement.",
            "Given an equation x of A = y of B, name the relative and the equivalent form, "
            "compute what the lot of A fetches after a change in either commodity's hours, "
            "and write the same values in the expanded, general and money forms."
        ),
        "note": (
            "Marx gives no hours for his seven commodities; the lab gives each lot 20 hours "
            "so that his equations balance, and every quantity is computed from those "
            "hours. The lab can show that the forms balance and how the quantities move. "
            "It cannot show the qualitative point of the section, that the equivalent's "
            "body comes to count as value itself; that is in the prose."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 1, l. 962 and l. 972 (the trivial thing; a social relation
    # between men); l. 995 (Robinson's stock-book).
    {
        "slug": "the-fetishism-of-commodities",
        "title": "The Fetishism of Commodities",
        "module": "Chapter 1 · Commodities",
        "one_line": "Among commodity producers the social relation between their labours appears as a relation between things, and the same hours read openly elsewhere.",
        "summary": (
            "Marx's word for how value looks is fetishism: a relation between people's "
            "labours takes the form of a relation between products. Compute the hours "
            "behind each product in Robinson Crusoe's ledger, in a village that trades the "
            "same goods, and in an association that shares its product by hours, and "
            "compare: the ratios agree, and only some of the settings show whose hours "
            "they are."
        ),
        "key": [
            "value: a relation between labours",
            "it appears as a property of products",
            "Robinson: hours read off his ledger",
            "market: the same ratios, hours unseen",
            "hours per unit = hours / units made",
        ],
        "key_label": "Fetishism in five lines",
        "concepts_intro": (
            "Section 4 is the most quoted part of the chapter and the one least like the "
            "others. It does no new arithmetic. It explains why the arithmetic of the first "
            "three sections is hidden from the people who live by it."
        ),
        "concepts": [
            ("The fetish",
             "Where producers work privately and meet only by exchanging products, the "
             "social character of their labour shows only in the products' values. A "
             "relation between people appears as a relation between things."),
            ("Not an error of perception",
             "The appearance is not a mistake that knowledge removes. Even after the "
             "scientific discovery that values are congealed labour, Marx says, the "
             "appearance stays as real as the air did after its gases were named."),
            ("Other forms of production",
             "Robinson on his island, the medieval manor, the peasant family and an "
             "association of free producers all reckon labour-time, and in none of them is "
             "it disguised as a property of things."),
        ],
        "read_title": "A trivial thing, and Robinson's ledger",
        "read_intro": (
            "The section opens with the commodity's oddity and closes the argument with a "
            "man alone on an island keeping accounts."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 1, §4.</strong> &ldquo;A commodity appears, at "
                  "first sight, a very trivial thing, and easily understood. Its analysis "
                  "shows that it is, in reality, a very queer thing, abounding in metaphysical "
                  "subtleties and theological niceties. &hellip; There it is a definite social "
                  "relation between men, that assumes, in their eyes, the fantastic form of a "
                  "relation between things.&rdquo;"),
            ("p", "You know the feeling this section describes even if you have never named "
                  "it. A price seems to belong to the thing. A coffee costs what it costs, the "
                  "way it weighs what it weighs, and the people who grew, shipped and roasted "
                  "it are nowhere in the number. Marx's claim is that the number is in fact a "
                  "relation between all of those people's labour, and that in a society of "
                  "commodity producers it can only appear as a fact about coffee."),
            ("p", "Go through the passage. A table made of wood is &ldquo;that common, "
                  "every-day thing, wood&rdquo;, until it is sold, and then it &ldquo;stands "
                  "on its head&rdquo; and evolves notions &ldquo;far more wonderful than "
                  "&lsquo;table-turning&rsquo; ever was&rdquo;. That is a joke at the expense "
                  "of the séances fashionable when Marx wrote, and it is also the argument. "
                  "The mystery does not come from use-value, or from the plain facts that "
                  "labour is the use of brain and muscle and takes time. It comes from the "
                  "form: the equality of labours shows as the equality of products' values, "
                  "and &ldquo;the mutual relations of the producers&rdquo; show as &ldquo;a "
                  "social relation between the products&rdquo;."),
            ("p", "Why should that be? Because the producers work &ldquo;independently of "
                  "each other&rdquo; and &ldquo;do not come into social contact with each "
                  "other until they exchange their products&rdquo;. Nobody decides how much "
                  "weaving society needs. Weavers find out from prices. So the proportions of "
                  "social labour are set behind everyone's back, and to each producer they "
                  "arrive as the movement of things, &ldquo;which rule the producers instead of "
                  "being ruled by them&rdquo;. Marx calls this the fetishism of commodities, "
                  "after the religious objects to which people ascribe powers that are really "
                  "their own."),
            ("p", "To show that the hours are there all along, Marx goes somewhere they are "
                  "not hidden, to Robinson Crusoe, a favourite of the economists of his day:"),
            ("p", "<strong>Volume I, Chapter 1, §4.</strong> &ldquo;His stock-book contains a "
                  "list of the objects of utility that belong to him, of the operations "
                  "necessary for their production; and lastly; of the labour time that "
                  "definite quantities of those objects have, on an average, cost him. All "
                  "the relations between Robinson and the objects that form this wealth of his "
                  "own creation, are here so simple and clear as to be intelligible without "
                  "exertion, even to Mr. Sedley Taylor.&rdquo;"),
            ("p", "Sedley Taylor was the Cambridge fellow who, months after Marx's death, "
                  "accused him in print of falsifying a quotation from Gladstone; Engels tells "
                  "the story in his preface. The jibe is the closest the section comes to a "
                  "smile. "
                  "The point is serious. Robinson tames goats, fishes, makes furniture and "
                  "tools, and knows that all of it is his own labour in different modes. His "
                  "ledger states the hours outright. Those relations, Marx says, &ldquo;contain "
                  "all that is essential to the determination of value&rdquo;, and none of it "
                  "is mysterious."),
            ("p", "The lab gives Robinson a week of 40 hours, with illustrative figures since "
                  "Marx gives none. Ten hours tame 2 goats, 15 hours catch 30 fish, 12 hours "
                  "make 2 pieces of furniture and 3 hours make a tool: 5, ½, 6 and 3 hours a "
                  "unit. The village preset gives each product to a different household, 30 "
                  "hours each, trading with one another. The hours per unit are identical, so "
                  "the exchange ratios are too: a goat for 10 fish. But in the village nobody "
                  "reads the hours. They see that a goat fetches 10 fish, and the ratio looks "
                  "like a fact about goats."),
            ("p", "Marx's other settings all reckon labour-time openly. On the medieval manor "
                  "&ldquo;every serf knows&rdquo; what he spends in his lord's service. A "
                  "peasant family divides its work by age, sex and season. And in an "
                  "association of free individuals working with common means of production, "
                  "Marx supposes &ldquo;merely for the sake of a parallel&rdquo; that each "
                  "member's share of the means of consumption is fixed by labour-time. The "
                  "association preset is that community's whole output, 160 hours. The lab "
                  "can show its hours per unit; it cannot show the shares, which the prose has "
                  "to carry."),
            ("p", "A marginal-utility economist would reject the frame, and at full strength. "
                  "For Jevons or Menger the goat-for-ten-fish ratio is not a disguise for "
                  "hours; it reflects what one more goat and one more fish are worth to the "
                  "people trading, and nothing lies behind it to be uncovered. Others take "
                  "Marx's idea and widen it: Georg Lukács made it the centre of his reading in "
                  "1923. This Subject computes the hours and leaves you to judge whether they "
                  "are what the ratio is hiding."),
            ("p", "So far commodities have done everything: expressed values, chosen an "
                  "equivalent, ruled their producers. The next lesson, “Exchange”, starts from "
                  "the fact that they cannot walk to market by themselves."),
        ],
        "lab": ("capkit", {
            "mode": "value",
            "view": "ledger",
            "money_unit": "hours",
            "preset": "robinson",
            "presets": [
                {"id": "robinson", "label": "Robinson's week (illustrative hours)",
                 "items": [{"name": "goats", "hours": 10, "output": 2},
                           {"name": "fish", "hours": 15, "output": 30},
                           {"name": "furniture", "hours": 12, "output": 2},
                           {"name": "tools", "hours": 3, "output": 1}],
                 "expect": {"vaTotalHours": "40 h", "vaPerUnit": "goats 5 h, fish 1/2 h, furniture 6 h, tools 3 h"}},
                {"id": "village", "label": "A village: four households, 30 hours each",
                 "items": [{"name": "goats", "hours": 30, "output": 6},
                           {"name": "fish", "hours": 30, "output": 60},
                           {"name": "furniture", "hours": 30, "output": 5},
                           {"name": "tools", "hours": 30, "output": 10}],
                 "expect": {"vaTotalHours": "120 h", "vaPerUnit": "goats 5 h, fish 1/2 h, furniture 6 h, tools 3 h"}},
                {"id": "association", "label": "An association's output, 160 hours",
                 "items": [{"name": "goats", "hours": 45, "output": 9},
                           {"name": "fish", "hours": 40, "output": 80},
                           {"name": "furniture", "hours": 42, "output": 7},
                           {"name": "tools", "hours": 33, "output": 11}],
                 "expect": {"vaTotalHours": "160 h", "vaPerUnit": "goats 5 h, fish 1/2 h, furniture 6 h, tools 3 h"}},
            ],
            "panel_title": "The hours behind each product",
            "panel_intro": (
                "Each line is a product, the hours spent on it and the units made. The table's "
                "last column is how many goats each product's unit equals. Step through the "
                "three presets: the totals differ and the hours per unit do not."
            ),
        }),
        "steps_title": "Reading a ledger of hours",
        "steps_intro": "Four steps, whether the ledger is one person's or a community's.",
        "steps": [
            ("List the products",
             "Write each product with the hours spent on it and the units it yielded in "
             "the period."),
            ("Divide",
             "Hours per unit is hours spent divided by units made. This is the figure "
             "Robinson's stock-book records."),
            ("Compare two products",
             "The ratio of their hours per unit is how many of one equal one of the other "
             "in labour-time. A goat at 5 hours equals 10 fish at ½ hour."),
            ("Ask who can read it",
             "State whether, in the setting described, the producers see the hours or only "
             "the ratio. That is the difference the section is about, and no figure in the "
             "table shows it."),
        ],
        "worked": {
            "title": "Robinson's stock-book",
            "intro": [
                "Robinson spends 10 hours taming 2 goats, 15 hours catching 30 fish, 12 hours "
                "making 2 pieces of furniture and 3 hours making a tool. You want his hours "
                "per unit, and what a goat is worth in fish.",
            ],
            "lines": [
                "total:  10 + 15 + 12 + 3 = 40 h",
                "goats 10/2 = 5 h,  fish 15/30 = 1/2 h",
                "furniture 12/2 = 6 h,  tools 3/1 = 3 h",
                "one goat:  5 / (1/2) = 10 fish",
            ],
            "after": [
                "A village of four households, each spending 30 hours on one product, arrives "
                "at the same ratio, a goat for 10 fish. Robinson can say why. The villagers "
                "can only say what a goat fetches.",
            ],
        },
        "quiz_title": "Hours, and who sees them",
        "quiz": [
            {"q": "Robinson spends 12 hours making 2 pieces of furniture and 15 hours catching "
                  "30 fish. In labour-time, how many fish equal one piece of furniture?",
             "a": ["12", "6", "4/5", "2"],
             "c": 0,
             "why": "Furniture is `12/2 = 6` hours a piece and fish `15/30 = 1/2` hour each, "
                    "so a piece equals `6 / (1/2) = 12` fish. Six is the furniture's hours, "
                    "not a number of fish; `4/5` compares the totals, 12 hours against 15; "
                    "and 2 is the number of pieces."},
            {"q": "On Marx's account, what is the fetishism of commodities?",
             "a": ["A belief that some commodities have magical powers",
                   "The appearance of a social relation between producers' labours as a "
                   "relation between their products",
                   "The habit of buying more than one needs",
                   "An error that disappears once value is explained"],
             "c": 1,
             "why": "Marx's definition is that the social character of labour appears as "
                    "an objective character of its products. It is not literal magic or "
                    "overconsumption, and he says the scientific discovery of value "
                    "&ldquo;by no means, dissipates the mist&rdquo;."},
            {"q": "Which of these settings is a society of commodity producers?",
             "a": ["Robinson Crusoe on his island",
                   "A medieval manor of lords and serfs",
                   "A village of households each making one product for sale",
                   "A peasant family producing for its own use"],
             "c": 2,
             "why": "Only the village produces separately for exchange. Robinson works for "
                    "himself, the serf's labour is owed in kind and known as such, and the "
                    "peasant family's products are not commodities to one another."},
            {"q": "In the lab, the village and Robinson's ledger give the same hours per "
                  "unit. What can the lab not show?",
             "a": ["The total hours worked",
                   "How many fish equal a goat",
                   "That the villagers see only the ratio, not the hours",
                   "The hours per unit of furniture"],
             "c": 2,
             "why": "Totals, ratios and hours per unit are all tiles or table cells. Whether "
                    "the people involved can read the hours is the section's claim, and a "
                    "quantity cannot display it."},
        ],
        "mistakes": [
            ("Thinking value is a physical property of the thing, like weight",
             "Marx's own test: &ldquo;So far no chemist has ever discovered exchange value "
             "either in a pearl or a diamond.&rdquo; In the lab nothing about a goat differs "
             "between Robinson's island and the village, and the goat is worth 10 fish in "
             "both, because that figure is a ratio of hours of labour. Weight would stay "
             "with the goat if every person vanished; its value would not."),
            ("Reading fetishism as simple deception",
             "Nobody is fooling the villagers. The appearance arises from how they "
             "produce, independently and for exchange, and it stays after it is explained, "
             "as the air stayed the same after its gases were discovered."),
            ("Taking the association as a description of a real society",
             "Marx assumes labour-time shares &ldquo;merely for the sake of a "
             "parallel&rdquo; with commodity production, and says the mode of distribution "
             "would vary with the community's development. It is a contrast case, not a "
             "programme computed here."),
        ],
        "standard": (
            "Finish when you can compute a ledger of hours and say what fetishism names.",
            "Given hours spent and units made for several products, compute the hours per "
            "unit and an exchange ratio between two of them, and state for a given setting "
            "whether the producers see the hours or only the ratio."
        ),
        "note": (
            "The lab sees quantities and not appearances. It can show that Robinson's "
            "ledger and the village's ratios agree; it cannot show the difference the "
            "section is about, which is who can read them. All the hours are illustrative."
        ),
    },
]
