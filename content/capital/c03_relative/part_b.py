"""Relative Surplus Value, lessons 6-9 -- Volume I, Chapters 15 to 18.

The third lesson on Chapter 15 (the compensation theory and what follows it),
then Part V: Chapter 16, Chapter 17 and Chapter 18.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals are left out, a drop capital is printed as an
ordinary capital, and the translator's double quotation marks inside a
quotation are printed as single curly quotes. Nothing else is changed. The
formulae of Chapter 18 are printed as displays in the book and are missing
from the plain-text edition; the lesson states them in its own words and
quotes only Marx's prose about them.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    # Kerr vol. 1, l. 3321 (the compensation theorists); l. 3323 (the carpet
    # factory; variable changed into constant capital); l. 3325 (£1000 of
    # machinery, less than 16 men); l. 3327 (at the best); l. 3329 (the
    # liberated workpeople); l. 3335 (not capital, but commodities); l. 3347
    # (Bill Sykes); l. 3407 (£500 capital, 300 men); l. 3426 (repelled and
    # attracted); l. 3715 (the soil and the labourer).
    {
        "slug": "machinery-and-the-displaced-worker",
        "title": "Machinery and the Displaced Worker",
        "module": "Chapter 15 · Machinery and Modern Industry",
        "one_line": "A machine that displaces workers does not set free a fund to employ them; it turns money that paid wages into constant capital.",
        "summary": (
            "The leading economists of Marx's day held that machinery which displaces "
            "workers necessarily sets free capital enough to employ them again. Marx answers "
            "with a carpet factory. Compute the variable capital before and after a machine "
            "is installed, the capital actually set free, and the most jobs the machine's "
            "price could create in machine-building, and see why the compensation is not "
            "automatic."
        ),
        "key": [
            "before: £3000 of wages pays 100 men",
            "after: £1500 pays 50, £1500 is machinery",
            "set free = wages saved − machine cost",
            "machine-building jobs: fewer, and once",
            "variable has become constant capital",
        ],
        "key_label": "Capital locked up, not set free",
        "concepts_intro": (
            "Section 6 of Chapter 15 is an argument with the economists, and the rest of "
            "the chapter follows its consequences. Three ideas carry it."
        ),
        "concepts": [
            ("The compensation theory",
             "Machinery that displaces workers sets free, at the same moment, a capital "
             "adequate to employ the same workers elsewhere, so their hardship is "
             "temporary."),
            ("Variable into constant capital",
             "Money that paid wages, once spent on a machine, no longer buys labour-power. "
             "Unless the machine cost less than the wages it replaced, nothing is set free "
             "at all."),
            ("Repulsion and attraction",
             "Factories throw workers out when their technique changes and draw them in when "
             "they expand on the old technique. The number employed can rise while falling "
             "relative to the capital."),
        ],
        "read_title": "The economists' claim, and a carpet factory",
        "read_intro": (
            "Marx states the claim in one sentence and then tests it with an example in "
            "round numbers."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 15, §6.</strong> &ldquo;James Mill, MacCulloch, "
                  "Torrens, Senior, John Stuart Mill, and a whole series besides, of bourgeois "
                  "political economists, insist that all machinery that displaces workmen, "
                  "simultaneously and necessarily sets free an amount of capital adequate to "
                  "employ the same identical workmen.&rdquo;"),
            ("p", "This is a serious argument, and it deserves its best form first. A machine is "
                  "adopted because it makes the product cheaper. The buyers of the cheaper "
                  "product have money left over, which they spend on other things, and the "
                  "makers of those things hire more hands. Meanwhile the capitalist who "
                  "installed the machine earns more and invests it. Nothing in the economy's "
                  "purchasing power has been destroyed; it has been moved, and the jobs follow "
                  "it. The displaced suffer in the passage, but the passage ends. David Ricardo "
                  "accepted this for years and then, in the third edition of his "
                  "<em>Principles</em> in 1821, added a chapter saying he had been wrong: "
                  "machinery could be injurious to the labouring class. Marx's opponents in "
                  "this section are the ones who did not follow him."),
            ("p", "Marx tests the narrowest form of the claim, that capital is &ldquo;set "
                  "free&rdquo;. A carpet manufacturer employs 100 men at £30 a year, so his "
                  "variable capital is £3,000. He also spends £3,000 a year on raw material. He "
                  "discharges 50 men and employs the other 50 with machinery that costs £1,500. "
                  "Before, his £6,000 was half constant and half variable. After, it is £4,500 "
                  "constant and £1,500 variable:"),
            ("p", "<strong>Volume I, Chapter 15, §6.</strong> &ldquo;Instead of being set free, "
                  "a part of the capital is here locked up in such a way as to cease to be "
                  "exchanged against labour-power: variable has been changed into constant "
                  "capital.&rdquo;"),
            ("p", "The capital of £6,000 can now employ only 50 men. If the machine had cost "
                  "£1,000 instead, £500 would have been set free, enough at £30 a head for "
                  "about 16 of the 50, &ldquo;nay, less than 16&rdquo;, Marx adds, because "
                  "some of that £500 must itself become constant capital if it is to employ "
                  "anyone. What about the men who build the machine? The £1,500 pays them, but "
                  "it also pays for their materials and their master's surplus value, so "
                  "&ldquo;At the best, its construction employs fewer men than its employment "
                  "displaces&rdquo;; and it employs them once, since the machine need not be "
                  "replaced until it wears out."),
            ("def", ("Capital set free",
                     "The wages a machine saves less what the machine costs. Only this "
                     "difference, if it is positive, is a fund that can employ anyone; the rest "
                     "of the old wage fund now exists as machinery.")),
            ("p", "The lab works all three cases. In the marx preset 50 men are displaced and "
                  "nothing is set free; the £1,500, spent in a machine-building trade where "
                  "materials are four times wages, pays 10 men for the time it takes to build "
                  "the machine. The cheaper-machine preset is Marx's £1,000 machine: `50/3`, "
                  "about 16, could be re-employed from the £500, and a further `20/3` in "
                  "machine-building, `70/3` in all. The "
                  "compensation preset is the most favourable case there could be: every penny "
                  "of the £1,500 paid out as wages to machine-builders, with no materials and "
                  "no profit, so all 50 are re-employed in machine-building. Then, and only "
                  "then, the number re-employed equals the number "
                  "displaced, and only while the machine is being built."),
            ("p", "But the apologists, Marx says, do not mean that sort of setting free. They "
                  "mean that the £1,500 of food and clothing the 50 men used to buy is now "
                  "&ldquo;liberated&rdquo; to employ them again. To the workers, though, those "
                  "necessaries were never capital: &ldquo;These means, therefore, were to them, "
                  "not capital, but commodities, and they, as regards these commodities, were "
                  "not wage-labourers, but buyers.&rdquo; Thrown out of work, they stop buying, "
                  "and the producers of their necessaries sell less, which can throw others out "
                  "of work too. The discharged men find work again only through some new "
                  "capital looking for workers, often in worse trades, since the division of "
                  "labour has fitted them for one operation."),
            ("p", "Marx's light moment is his parody of the apologists' last line of defence, "
                  "that the harm comes from the capitalist use of machinery and not from "
                  "machinery itself, so whoever attacks the one attacks the other. It is, he "
                  "says, the reasoning of Bill Sikes before the jury: &ldquo;Gentlemen of the "
                  "jury, no doubt the throat of this commercial traveller has been cut. But that "
                  "is not my fault, it is the fault of the knife!&rdquo;"),
            ("p", "Section 7 then grants what is true in the economists' case. Factories can end "
                  "by employing more people than the crafts they ruined. Marx's example: a "
                  "capital of £500 a week, two-fifths constant, pays 300 men at £1. Machinery "
                  "makes it four-fifths constant, and 100 men remain. Let the capital grow to "
                  "£1,500 and 300 are employed again; at £2,000, 400. The number has risen by "
                  "100, but the £2,000 would have employed 1,200 under the old technique. The "
                  "workers are &ldquo;continually both repelled and attracted&rdquo; as the "
                  "trade cycle and the technique change, and Marx follows the English cotton "
                  "trade through its crises to the cotton famine of 1862."),
            ("p", "The last sections widen the view. Machinery overturns manufacture and "
                  "domestic industry, from the needle machine that does the work of Smith's "
                  "ten men many times over to the sewing machine. The Factory Acts, extended "
                  "trade by trade, speed that conversion; their education clauses, paltry as "
                  "they were, show to Marx the germ of an education that would combine "
                  "productive work with schooling. And in agriculture the same process works by "
                  "&ldquo;sapping the original sources of all wealth&mdash;the soil and the "
                  "labourer&rdquo;."),
            ("p", "Whether machinery lowers employment over decades is a question about data, "
                  "and economists have mostly answered that it has not: employment has grown "
                  "with mechanisation, while particular trades and places have been ruined by "
                  "it. Marx's claim is narrower and about mechanism. Nothing in the act of "
                  "installing a machine re-employs the people it displaces; anything that does "
                  "comes from new capital, later, elsewhere. The lab computes that mechanism and "
                  "nothing about the decades."),
            ("p", "That closes Part IV's three methods: co-operation, manufacture and "
                  "machinery. The next lesson, “Absolute and Relative Surplus Value”, steps back "
                  "and asks whether the two kinds of surplus value were ever really two."),
        ],
        "lab": ("capkit", {
            "mode": "machine",
            "view": "displace",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's carpet factory: 50 of 100 men replaced by £1,500 of machinery",
                 "variable": 3000, "wage_each": 30, "discharged": 50, "machine_spend": 1500,
                 "mb_composition": 4, "expect": {"maDisplaced": "50", "maReemployed": "10 = 0 set free + 10 in machine-building"}},
                {"id": "cheaper-machine", "label": "Marx's variant: the machinery costs £1,000",
                 "variable": 3000, "wage_each": 30, "discharged": 50, "machine_spend": 1000,
                 "mb_composition": 4, "expect": {"maDisplaced": "50", "maReemployed": "70/3 = 50/3 set free + 20/3 in machine-building"}},
                {"id": "compensation", "label": "Most favourable case: all £1,500 paid as machine-builders' wages",
                 "variable": 3000, "wage_each": 30, "discharged": 50, "machine_spend": 1500,
                 "mb_composition": 0, "expect": {"maDisplaced": "50", "maReemployed": "50 = 0 set free + 50 in machine-building"}},
            ],
            "panel_title": "Where the wage fund went",
            "panel_intro": (
                "The machine displaces workers and their wages; what it costs is subtracted "
                "from those wages to find the capital set free. The machine's price also pays "
                "wages in machine-building, at that trade's c/v and the same wage. The "
                "carpet factory is Marx's; the c/v of 4 in machine-building is "
                "illustrative."
            ),
        }),
        "steps_title": "Testing a claim of compensation",
        "steps_intro": "Four steps for any machine said to set capital free.",
        "steps": [
            ("Count the wages saved",
             "Multiply the workers discharged by the wage of each. That is the variable "
             "capital the machine replaces."),
            ("Subtract the machine",
             "Take the machine's cost from the wages saved. Only a positive remainder is set "
             "free, and only it can employ anyone at once."),
            ("Find the machine-building jobs",
             "Divide the machine's price by one plus the composition c/v of machine-building "
             "to get its wage bill, and that by the wage. These jobs last while the machine is "
             "built."),
            ("Compare with the displaced",
             "Set the total beside the workers discharged. Anything short of them must be "
             "made up by new capital, which the machine did not supply."),
        ],
        "worked": {
            "title": "The carpet factory",
            "intro": [
                "A carpet manufacturer pays 100 men £30 a year each. He discharges 50 and "
                "spends £1,500 on machinery for the rest. Machine-building, in this "
                "illustration, spends £4 on materials for every £1 of wages. You want the "
                "capital set free and the most men the change can employ.",
            ],
            "lines": [
                "variable before:  100 · £30 = £3000",
                "wages saved:  50 · £30 = £1500",
                "set free:  £1500 − £1500 = £0",
                "machine-building wages:  £1500 / (1 + 4) = £300",
                "machine-building jobs:  £300 / £30 = 10, once",
            ],
            "after": [
                "Fifty men are displaced and ten are employed for as long as it takes to build "
                "the machine. The variable capital has fallen from £3,000 to £1,500, and the "
                "capital of £6,000 now employs 50 men instead of 100.",
            ],
        },
        "quiz_title": "Set free or locked up",
        "quiz": [
            {"q": "A manufacturer pays 60 workers £40 a year each, discharges 20 of them, and "
                  "spends £600 on machinery. How much capital does the change set free?",
             "a": ["£200", "£800", "£2,400", "Nothing"],
             "c": 0,
             "why": "The wages saved are `20 · £40 = £800`, and the machinery costs £600, so "
                    "£200 is set free. Eight hundred pounds ignores the machine's cost, £2,400 "
                    "is the whole wage bill before the change, and nothing would be right only "
                    "if the machine had cost £800 or more."},
            {"q": "In Marx's carpet factory, what has become of the £1,500 that used to pay "
                  "the 50 discharged men?",
             "a": ["It exists as machinery, constant capital that buys no labour-power",
                   "It is set free to employ the 50 men in another trade",
                   "It has been paid out as profit",
                   "It is held as a reserve to pay them when trade recovers"],
             "c": 0,
             "why": "The £1,500 was spent on the machine, so variable capital became constant "
                    "capital. That is exactly why nothing is set free to employ the 50. Marx's "
                    "example has no profit taken out of it, and no reserve is held."},
            {"q": "Which version of the compensation argument does Marx's carpet factory answer "
                  "directly?",
             "a": ["That installing the machine sets free capital to employ the same workers",
                   "That machinery never raises total employment over the long run",
                   "That cheaper products release spending that creates jobs elsewhere",
                   "That machinery raises the value of labour-power"],
             "c": 0,
             "why": "The example tests the claim that capital is set free by the change itself. "
                    "The wider claim, about spending released by cheaper products, he answers "
                    "separately, saying the jobs it creates come from new capital and not from "
                    "the capital that bought the machine. He does not deny that employment can "
                    "rise in the long run, and the last option is no one's argument."},
            {"q": "A capital of £2,000 a week is four-fifths constant and pays its workers £1 "
                  "each a week. How many does it employ, and how many would it have employed "
                  "at two-fifths constant?",
             "a": ["400, against 1,200", "1,600, against 800", "400, against 800",
                   "300, against 1,200"],
             "c": 0,
             "why": "One-fifth of £2,000 is £400 of wages, 400 workers; three-fifths would have "
                    "been £1,200, 1,200 workers. These are Marx's figures in section 7. The "
                    "second option uses the constant part as wages, and the others mix the two "
                    "cases."},
        ],
        "mistakes": [
            ("Thinking the capital freed by a machine re-employs the workers it displaced",
             "The compensation theorists' strongest case is that spending released by cheaper "
             "products creates jobs elsewhere, and Marx answers that those jobs need new "
             "capital. His carpet factory answers the narrower claim that capital is set "
             "free. In the marx preset 50 men are displaced and the lab prints 0 set free: "
             "the £1,500 that paid them is now machinery. Even the compensation preset, with "
             "every penny of the machine paid as wages, re-employs 50 only while the machine "
             "is built."),
            ("Counting the workers' necessaries as capital set free",
             "The £1,500 of food and clothing the discharged men used to buy was never "
             "capital to them; it was commodities they bought with their wages. Machinery "
             "turns them from buyers into non-buyers, which lowers demand for those "
             "commodities rather than creating a fund to employ them."),
            ("Concluding that machinery must reduce total employment",
             "Marx does not say so. Section 7 shows factory employment rising absolutely, "
             "from 100 to 400 men in his example, while falling relative to the capital, and "
             "new trades growing out of machinery itself. His claim is about what the "
             "machine does, not about the total, which depends on how fast capital "
             "accumulates."),
        ],
        "standard": (
            "Finish when you can compute what a machine sets free.",
            "Given the variable capital, the wage, the workers discharged, the cost of the "
            "machinery and the composition of machine-building, compute the capital set "
            "free, the workers it and the machine's construction could employ, and compare "
            "them with the workers displaced."
        ),
        "note": (
            "The lab counts the machine's price as constant and variable capital in "
            "machine-building and leaves out the machine-builders' surplus value, so its "
            "re-employment figure is an upper bound, as Marx's &ldquo;at the best&rdquo; "
            "says. It does not model the wider effects of cheaper products, which are the "
            "strongest form of the compensation argument. The carpet factory and the £1,000 "
            "variant are Marx's; the composition of machine-building is illustrative."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 1, l. 3745 (any distinction appears illusory); l. 3747 (the
    # alternative, once capitalist production is general); l. 3731 (no longer
    # necessary to do manual work yourself); l. 3733 (the productive labourer;
    # luck and misfortune); l. 3765 (only the possibility); l. 3767 (the
    # sago-cutter; historical events); l. 3774 (Mill and the bird's nest);
    # l. 3780 (20% and 4%).
    {
        "slug": "absolute-and-relative-surplus-value",
        "title": "Absolute and Relative Surplus Value",
        "module": "Chapter 16 · Absolute and Relative Surplus-Value",
        "one_line": "Each kind of surplus value presupposes the other, but once capital is established a rise in the rate comes either from a longer day or from a shorter necessary time.",
        "summary": (
            "Chapter 16 asks whether the distinction of the last two Parts was ever real. "
            "From one side each kind of surplus value is also the other; from the side of a "
            "change in the rate they come apart again. Classify changes in the working day "
            "as absolute, relative or both, compute the new rate, and see why a fertile soil "
            "makes surplus labour possible but does not explain it."
        ),
        "key": [
            "longer day: absolute",
            "shorter necessary time: relative",
            "both at once: both",
            "nature fixes the necessary time",
            "not the surplus that is extracted",
        ],
        "key_label": "Two kinds, told apart by the change",
        "concepts_intro": (
            "Part V is short: three chapters that review Parts III and IV together. The "
            "first sets out three ideas."
        ),
        "concepts": [
            ("Productive labour",
             "For capital, the productive labourer is the one who produces surplus value. A "
             "schoolmaster employed by a school proprietor is productive in this sense; the "
             "same teaching done for oneself is not."),
            ("Formal and real subjection",
             "Absolute surplus value needs only that workers work for a capitalist. Relative "
             "surplus value needs the methods of production themselves to be remade."),
            ("A natural basis, and its limit",
             "Some productivity is needed before anyone can work for others, and a kind "
             "climate lowers the necessary time. Nature fixes where surplus labour could "
             "begin, never that it does."),
        ],
        "read_title": "A distinction that appears illusory",
        "read_intro": (
            "The passage comes halfway through the chapter. Marx states the objection to his "
            "own distinction and then says when it stops holding."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 16.</strong> &ldquo;From one standpoint, any "
                  "distinction between absolute and relative surplus-value appears illusory. "
                  "Relative surplus-value is absolute, since it compels the absolute "
                  "prolongation of the working day beyond the labour-time necessary to the "
                  "existence of the labourer himself. Absolute surplus-value is relative, since "
                  "it makes necessary such a development of the productiveness of labour, as "
                  "will allow of the necessary labour-time being confined to a portion of the "
                  "working day. But if we keep in mind the behaviour of surplus-value, this "
                  "appearance of identity vanishes.&rdquo;"),
            ("p", "The chapter opens with a definition that widens and narrows at once. Since the "
                  "work is now done by a collective labourer, &ldquo;it is no longer necessary "
                  "for you to do manual work yourself&rdquo; to labour productively; an organ "
                  "of the collective labourer is enough. But for capital only labour that "
                  "produces surplus value counts as productive. A schoolmaster who &ldquo;works "
                  "like a horse to enrich the school proprietor&rdquo; is productive, and it "
                  "makes no difference that the proprietor chose a teaching factory instead of "
                  "a sausage factory. Marx's verdict is dry: &ldquo;To be a productive labourer "
                  "is, therefore, not a piece of luck, but a misfortune.&rdquo;"),
            ("p", "Now the passage. Relative surplus value is &ldquo;absolute&rdquo; because "
                  "any surplus at all requires a day longer than the necessary time; absolute "
                  "surplus value is &ldquo;relative&rdquo; because the necessary time must "
                  "already be short enough to leave room. Read that way, every surplus value is "
                  "both. The appearance vanishes once you ask how the rate is raised. With "
                  "labour-power paid at its value, Marx says, there are only two ways: lengthen "
                  "the day with productivity and intensity given, or, with the day given, "
                  "change the proportion between its parts through productivity or "
                  "intensity."),
            ("def", ("Absolute or relative, by the change",
                     "A rise in the rate of surplus value is absolute when it comes from a "
                     "longer working day, relative when it comes from a shorter necessary "
                     "labour-time in a day of given length, and both when both change at "
                     "once.")),
            ("p", "That is the lab's rule. Begin with a 12-hour day of 6 necessary hours, a rate "
                  "of 100%. The lengthen preset takes it to 14 and the rate is `8/6`, 133.33%: "
                  "absolute. The cheapen preset keeps 12 and cuts the necessary time to 5, and "
                  "the rate is `7/5`, 140%: relative. The both preset does both, and the rate is "
                  "`9/5`, 180%: of the 3 extra hours of surplus labour, 2 are absolute and 1 is "
                  "relative."),
            ("p", "The second half of the chapter takes up a tempting explanation of surplus "
                  "value: that some labour simply produces more than it needs, because nature "
                  "is generous. Marx grants the premise and denies the conclusion. Without a "
                  "certain productivity there is no time to work for others, and where the soil "
                  "is fertile and wants are few, the necessary time is short. But "
                  "&ldquo;Favourable natural conditions alone, gave us only the possibility, "
                  "never the reality, of surplus-labour&rdquo;. His example is a sago-cutter in "
                  "the eastern islands of the Asiatic Archipelago, who fells a tree and has his bread for "
                  "the week from it:"),
            ("p", "<strong>Volume I, Chapter 16.</strong> &ldquo;The bounty of Nature does "
                  "not explain why he would then have to work 6 days a week, or why he must "
                  "furnish 5 days of surplus-labour. It explains only why his necessary "
                  "labour-time would be limited to one day a week.&rdquo;"),
            ("p", "Marx supposes the sago-cutter meets all his wants in 12 hours a week. The "
                  "sago preset puts that as 2 hours on each of six days, all of it necessary, a "
                  "rate of zero. Make him a wage labourer on a 12-hour day and the necessary "
                  "time is "
                  "still 2 hours, but the day is 12: a rate of 500%, Marx's five days of surplus "
                  "labour to one of necessary. The change is absolute. Nature set the 2 hours. "
                  "The other 10 needed, in Marx's words, &ldquo;a whole series of historical "
                  "events&rdquo; and compulsion."),
            ("p", "The chapter ends with John Stuart Mill, who said that capital yields a profit "
                  "because food, clothing and tools &ldquo;last longer than the time which was "
                  "required to produce them&rdquo;. Marx's reply is the lesson's one joke, and "
                  "it is his: on that view a baker could never make the profit a machine-maker "
                  "makes, and &ldquo;if a bird's nest did not last longer than the time it takes "
                  "in building, birds would have to do without nests.&rdquo; He also corrects "
                  "Mill's arithmetic. If workers produce 20% more than their wages, profit is "
                  "not 20%, because profit is reckoned on the whole capital: with £400 of means "
                  "of production and £100 of wages, it is 20 on 500, which is 4%."),
            ("p", "Those who explain profit by the productivity of capital, or by the reward for "
                  "waiting, would reply that Mill's durability point is a crude form of a sound "
                  "idea: that goods available sooner are worth more than goods available later, "
                  "and interest pays for the difference. Marx's answer is that this explains "
                  "nothing about where the surplus comes from, and Volume III returns to the "
                  "question when it divides surplus value into profit and interest."),
            ("p", "If the rate can move in these two ways, how do its parts move together? The "
                  "next lesson, “Changes in the Price of Labour-Power and in Surplus Value”, "
                  "varies length, intensity and productivity one at a time."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "classify",
            "money_unit": "hours",
            "preset": "lengthen",
            "presets": [
                {"id": "lengthen", "label": "12 hours, 6 necessary, lengthened to 14",
                 "day": 12, "necessary": 6, "new_day": 14, "new_necessary": 6, "expect": {"wdKind": "absolute", "wdRate": "4/3 = 133.33%"}},
                {"id": "cheapen", "label": "12 hours, 6 necessary, necessary cut to 5",
                 "day": 12, "necessary": 6, "new_day": 12, "new_necessary": 5, "expect": {"wdKind": "relative", "wdRate": "7/5 = 140%"}},
                {"id": "both", "label": "12 hours, 6 necessary, to 14 hours with 5 necessary",
                 "day": 12, "necessary": 6, "new_day": 14, "new_necessary": 5, "expect": {"wdKind": "both", "wdRate": "9/5 = 180%"}},
                {"id": "sago", "label": "Marx's sago-cutter: 2 hours a day for himself, then a 12-hour day",
                 "day": 2, "necessary": 2, "new_day": 12, "new_necessary": 2, "expect": {"wdKind": "absolute", "wdRate": "5 = 500%"}},
            ],
            "panel_title": "Which kind of change is this?",
            "panel_intro": (
                "A day before and after. A longer day is absolute surplus value, a shorter "
                "necessary time is relative, and both together are both. The rate shown is "
                "the one after the change."
            ),
        }),
        "steps_title": "Classifying a change in the rate",
        "steps_intro": "Four steps for any before and after of a working day.",
        "steps": [
            ("Write both days",
             "Record the length of the day and the necessary time, before and after."),
            ("Compare the lengths",
             "If the day is longer, the change has an absolute part: the added hours are "
             "surplus labour."),
            ("Compare the necessary times",
             "If the necessary time is shorter in the day, the change has a relative part: "
             "the hours it lost became surplus labour."),
            ("Compute the new rate",
             "Surplus labour is the new day less the new necessary time; divide it by the new "
             "necessary time."),
        ],
        "worked": {
            "title": "Twelve and six to fourteen and five",
            "intro": [
                "A 12-hour day has 6 hours of necessary labour. The day is lengthened to 14 "
                "hours, and cheaper necessaries cut the necessary time to 5. You want the "
                "kind of change and the new rate.",
            ],
            "lines": [
                "before:  (12 − 6) / 6 = 1 = 100%",
                "after:   (14 − 5) / 5 = 9/5 = 180%",
                "absolute part:  14 − 12 = 2 h",
                "relative part:  6 − 5 = 1 h",
            ],
            "after": [
                "Surplus labour has grown from 6 hours to 9: two of the extra hours came from "
                "the end of the day and one from its necessary part. The lab calls the change "
                "both.",
            ],
        },
        "quiz_title": "Absolute, relative or both",
        "quiz": [
            {"q": "A day of 10 hours with 5 necessary becomes a day of 10 hours with 4 "
                  "necessary. What kind of change is it, and what is the new rate?",
             "a": ["Relative, 150%", "Absolute, 150%", "Relative, 100%", "Both, 150%"],
             "c": 0,
             "why": "The day has not changed and the necessary time has fallen, so the change "
                    "is relative; `(10 − 4) / 4 = 3/2`, 150%. It is not absolute or both, "
                    "because the length is the same, and 100% is the rate before."},
            {"q": "Marx's sago-cutter meets his wants in one day a week and, under capital, "
                  "works six. What does nature explain about this, on Marx's account?",
             "a": ["Why his necessary labour is only one day",
                   "Why he must give five days of surplus labour",
                   "Why his surplus labour is 500% of his necessary labour",
                   "Nothing at all"],
             "c": 0,
             "why": "Marx says the bounty of nature &ldquo;explains only why his necessary "
                    "labour-time would be limited to one day a week&rdquo;. The five days of "
                    "surplus labour, and so the 500%, need historical events and compulsion. "
                    "Nature is not irrelevant either: it fixes the necessary time."},
            {"q": "Mill says that if workers produce 20% more than their wages, profits will be "
                  "20%. With £400 of means of production and £100 of wages, what does Marx say "
                  "the rate of profit is?",
             "a": ["4%", "20%", "25%", "5%"],
             "c": 0,
             "why": "The surplus value is 20% of £100, which is £20, and profit is reckoned on "
                    "the whole capital of £500, so `20/500` is 4%. Twenty per cent is the rate of "
                    "surplus value, 5% divides the £20 by the £400 of means of production alone, and 25% "
                    "is the wages over the means of production, which is not a rate of profit."},
            {"q": "On Chapter 16's definition, which of these is a productive labourer for "
                  "capital?",
             "a": ["A teacher employed by a school run for profit",
                   "A teacher who tutors her own children",
                   "A cook employed in a private household",
                   "A farmer who grows food for his own family"],
             "c": 0,
             "why": "Only labour that produces surplus value for a capitalist counts, whatever it "
                    "makes, and Marx's own example is the schoolmaster in a teaching factory. "
                    "The other three may be useful and hard work, but none produces surplus "
                    "value for a capital."},
        ],
        "mistakes": [
            ("Thinking surplus value needs a natural surplus of the soil",
             "Nature can shorten the necessary time; it cannot make anyone work past it. In "
             "the sago preset the necessary time is 2 hours before and after, set by the "
             "sago palm, and the rate goes from zero to 500% only because the day goes from 2 "
             "hours to 12. The change is absolute, and the lab says so. Favourable conditions "
             "give &ldquo;only the possibility, never the reality&rdquo;."),
            ("Calling every rise in the rate relative because productivity is involved",
             "Marx grants that any surplus presupposes some productivity, which is why the "
             "distinction can look illusory. A change is classified by what moved: a longer "
             "day is absolute even in a highly productive industry. The lengthen preset "
             "changes only the day and is absolute."),
            ("Equating the rate of surplus value with the rate of profit",
             "Mill made this slip and Marx corrects it in the chapter: the rate of surplus "
             "value divides surplus value by wages, the rate of profit divides it by the whole "
             "capital. With £100 of wages, £400 of means of production and £20 of surplus value "
             "they are 20% and 4%."),
        ],
        "standard": (
            "Finish when you can classify a change in the working day.",
            "Given the length of a working day and its necessary time before and after a "
            "change, classify the change as absolute, relative or both, compute the new rate "
            "of surplus value, and separate the surplus labour gained in each way."
        ),
        "note": (
            "The lab classifies by what changed in the day; it cannot tell whether a shorter "
            "necessary time came from higher productivity or from a wage below value, which "
            "Marx's definition excludes. The sago-cutter's 12 hours a week and his five days "
            "of surplus labour are Marx's; spreading them as 2 hours on each of six days, and "
            "the other days, are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 1, l. 3798 (the three circumstances); l. 3804-3806 (a day of
    # given length always creates the same value); l. 3818 (Ricardo; 4s to 3s,
    # 2s to 3s); l. 3840 (an increased value; 6s to 8s); l. 3866 (12 to 14
    # hours); l. 3872 (no longer commensurable); l. 3882 (dearer necessaries,
    # 12 to 14 and 16 hours); l. 3896 (spare time for one class).
    {
        "slug": "price-of-labour-power-and-surplus-value",
        "title": "Changes in the Price of Labour-Power and in Surplus Value",
        "module": "Chapter 17 · Changes of Magnitude in the Price of Labour-Power and in Surplus-Value",
        "one_line": "Vary one of the day's length, the intensity of labour or its productivity and the split between labour-power and surplus value moves in a way Marx's laws predict.",
        "summary": (
            "Three things decide how a day's value divides between labour-power and surplus "
            "value: the length of the day, the intensity of labour and its productivity. "
            "Run Marx's cases one factor at a time and then together, and compute the value of "
            "labour-power and the rate of surplus value in each. Productivity moves the split "
            "without changing the value a day creates; length and intensity change that "
            "value itself."
        ),
        "key": [
            "length, intensity, productivity",
            "productivity: same value, new split",
            "intensity: more value in the same day",
            "length: more value in a longer day",
            "s and v trade off only if productivity moves",
        ],
        "key_label": "Three factors, one at a time",
        "concepts_intro": (
            "Chapter 17 is the arithmetic of Parts III to V in one place. It rests on two "
            "assumptions, stated at the start: commodities sell at their values, and the price "
            "of labour-power may rise above its value but never falls below it."
        ),
        "concepts": [
            ("Productivity varies",
             "A day of given length always creates the same value. Higher productivity in "
             "the necessaries lowers the value of labour-power, and surplus value rises by "
             "exactly as much."),
            ("Intensity varies",
             "A more intense day creates more value. Labour-power and surplus value can then "
             "both rise at once, and productivity elsewhere has nothing to do with it."),
            ("Length varies",
             "A longer day creates more value. With the value of labour-power fixed, all the "
             "extra goes to surplus value, until the extra wear on the worker forces the "
             "value of labour-power up."),
        ],
        "read_title": "The three circumstances",
        "read_intro": (
            "The passage opens the chapter's argument. Everything after it is a case of one, "
            "two or three of these circumstances varying."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 17.</strong> &ldquo;On this assumption we have "
                  "seen that the relative magnitudes of surplus-value and of price of "
                  "labour-power are determined by three circumstances; (1) the length of the "
                  "working day, or the extensive magnitude of labour; (2) the normal intensity of "
                  "labour, its intensive magnitude, whereby a given quantity of labour is "
                  "expended in a given time; (3) the productiveness of labour, whereby the same "
                  "quantum of labour yields, in a given time, a greater or less quantum of "
                  "product, dependent on the degree of development in the conditions of "
                  "production.&rdquo;"),
            ("p", "Think of a pay rise in a year when prices also rose, and the question of "
                  "whether you are better off. Chapter 17 asks the same kind of question at the "
                  "level of the day. A day's labour creates a value; the worker's labour-power "
                  "takes part of it and the capitalist the rest. Three things can change, and "
                  "Marx changes them one at a time, holding the other two."),
            ("p", "First, productivity, with length and intensity fixed. Marx states three laws, "
                  "and the first carries the others:"),
            ("p", "<strong>Volume I, Chapter 17.</strong> &ldquo;(1.) A working day of given "
                  "length always creates the same amount of value, no matter how the "
                  "productiveness of labour, and, with it, the mass of the product, and the price "
                  "of each single commodity produced, may vary.&rdquo;"),
            ("p", "If a 12-hour day creates 6s, the 6s is all there is to divide. So the value of "
                  "labour-power and surplus value move in opposite directions, by the same "
                  "amount; and the movement starts with the value of labour-power, which falls "
                  "only when the necessaries cheapen. Marx's figures: labour-power worth 4s, 8 "
                  "hours, surplus value 2s, 4 hours. Productivity rises and labour-power falls "
                  "to 3s, 6 hours; surplus value rises to 3s, 6 hours. The same shilling moved "
                  "each way, but labour-power fell by a quarter and surplus value rose by half. "
                  "Ricardo, who first stated these laws, missed that the proportions differ, and "
                  "made a larger mistake: he knew no change in length or intensity, so he took "
                  "this one case for the whole."),
            ("p", "Second, intensity, with length and productivity fixed. A more intense day "
                  "&ldquo;will be incorporated in an increased value&rdquo;: the 12 hours that "
                  "created 6s may create 8s. Now both parts can grow at once, from 3s each to "
                  "4s each, and a rise in wages need not mean the worker is paid above the value "
                  "of his labour-power, since he is also wearing it out faster. The lab holds "
                  "the value of labour-power at 6 hours and gives all of the extra to surplus "
                  "value."),
            ("p", "Third, length, with intensity and productivity fixed. A longer day creates "
                  "more value, and with labour-power still worth 3s, the extra is all surplus "
                  "value: 12 hours become 14, and surplus labour goes from 6 hours to 8. The "
                  "value of labour-power has not changed, but it is now a smaller share of the "
                  "day. Past a point, Marx adds, the extra wear grows geometrically, and the "
                  "price of labour-power and the degree of its exploitation &ldquo;cease to be "
                  "commensurable quantities&rdquo;."),
            ("def", ("The three factors",
                     "The length of the working day, the intensity of labour and the "
                     "productiveness of labour. Productivity changes how the value a day creates "
                     "is divided; length and intensity change how much value the day creates.")),
            ("p", "Last, Marx combines them. Suppose the soil grows less fertile, food grows "
                  "dearer, and labour-power rises from 3s to 4s, 6 hours to 8. On a 12-hour day "
                  "surplus labour falls to 4 hours. Lengthen the day to 14 and it is back at 6 "
                  "hours but a smaller share. Lengthen it to 16 and the proportion is restored, "
                  "8 hours against 8, while the surplus value has grown by a third. Marx uses "
                  "this to correct West and Ricardo, who read the dear bread of 1799 to 1815 as "
                  "proof that the rate of surplus value fell; in fact, he says, the day was "
                  "lengthened and intensified in those years and the rate rose."),
            ("p", "The lab ships with all three factors switched on, so each preset shows its own "
                  "case; the menu “which factor varies” lets you switch off all but one. The "
                  "productivity preset is Marx's 8 hours falling to 6 on a 12-hour day: the rate "
                  "goes from 50% to 100%. The intensity preset is his 6s becoming 8s: 16 normal "
                  "hours on 6 necessary. The length preset is 12 hours becoming 14. The combined "
                  "preset is dearer food on a 16-hour day: 8 necessary hours and a rate of "
                  "100%. The dearer-food preset shows the same dearer food on an unchanged day "
                  "of 12: 8 necessary hours and a rate of 50%."),
            ("p", "The chapter ends with the case that runs the other way: higher productivity "
                  "and intensity with a shorter day. The necessary time sets the lower limit of "
                  "the day, and only the end of capitalist production, Marx says, would let the "
                  "day shrink towards it. His last sentence is the chapter's sharpest: "
                  "&ldquo;In capitalist society spare time is acquired for one class by "
                  "converting the whole life-time of the masses into labour-time.&rdquo;"),
            ("p", "All of this has used one measure of exploitation, the rate of surplus value. "
                  "The next lesson, “Formulae for the Rate of Surplus Value”, looks at the "
                  "measures the economists used instead, and why one of them can never reach "
                  "100%."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "three",
            "money_unit": "hours",
            "hold": "combined",
            "preset": "productivity",
            "presets": [
                {"id": "productivity", "label": "Marx's case I: labour-power falls from 8 hours to 6",
                 "day": 12, "necessary": 8, "productivity": "4/3", "intensity": 1, "new_day": 12,
                 "expect": {"wdLpValue": "6 h", "wdRate": "1 = 100%"}},
                {"id": "intensity", "label": "Marx's case II: a day that created 6s creates 8s",
                 "day": 12, "necessary": 6, "productivity": 1, "intensity": "4/3", "new_day": 12,
                 "expect": {"wdLpValue": "6 h", "wdRate": "5/3 = 166.67%"}},
                {"id": "length", "label": "Marx's case III: 12 hours become 14",
                 "day": 12, "necessary": 6, "productivity": 1, "intensity": 1, "new_day": 14,
                 "expect": {"wdLpValue": "6 h", "wdRate": "4/3 = 133.33%"}},
                {"id": "combined", "label": "Marx's case IV: dearer food, the day lengthened to 16",
                 "day": 12, "necessary": 6, "productivity": "3/4", "intensity": 1, "new_day": 16,
                 "expect": {"wdLpValue": "8 h", "wdRate": "1 = 100%"}},
                {"id": "dearer-food", "label": "Dearer food, the day left at 12",
                 "day": 12, "necessary": 6, "productivity": "3/4", "intensity": 1, "new_day": 12,
                 "expect": {"wdLpValue": "8 h", "wdRate": "1/2 = 50%"}},
            ],
            "panel_title": "Length, intensity and productivity",
            "panel_intro": (
                "Productivity in the wage-goods industries divides the necessary time; "
                "intensity multiplies the labour in the day; the new length replaces the old. "
                "“Which factor varies” is set to all three; choose one to hold the other two "
                "at their starting values."
            ),
        }),
        "steps_title": "Running one of Marx's cases",
        "steps_intro": "Four steps, whichever factor varies.",
        "steps": [
            ("Start from the given day",
             "Write the length of the day and the necessary time. Their difference is surplus "
             "labour, and the day's length is the value it creates, in hours."),
            ("Apply productivity to the necessary time",
             "Divide the necessary time by the change in productivity in the industries that "
             "make the necessaries. That is the new value of labour-power."),
            ("Apply length and intensity to the day",
             "Multiply the new length of the day by its intensity. That is the value the day "
             "now creates, in hours of normal labour."),
            ("Divide the day again",
             "Surplus labour is the value created less the value of labour-power; the rate is "
             "one over the other. Compare with the start."),
        ],
        "worked": {
            "title": "Dearer bread and a longer day",
            "intro": [
                "Marx's case IV: a 12-hour day, 6 hours necessary. The soil grows less fertile "
                "and labour-power rises from 3s to 4s. You want the rate on the old day and on "
                "days lengthened to 14 and 16 hours.",
            ],
            "lines": [
                "new necessary time:  6 h / (3/4) = 8 h",
                "12-hour day:  4 h surplus, 4/8 = 50%",
                "14-hour day:  6 h surplus, 6/8 = 75%",
                "16-hour day:  8 h surplus, 8/8 = 100%",
            ],
            "after": [
                "At 14 hours the surplus labour is back at its old 6 hours but the rate has "
                "fallen; at 16 the rate is back at 100% and the surplus labour has grown by a "
                "third, from 6 hours to 8. These are Marx's figures.",
            ],
        },
        "quiz_title": "One factor at a time",
        "quiz": [
            {"q": "A 12-hour day creates a value of 6s. Productivity doubles in every industry, "
                  "with the length and intensity of the day unchanged. What value does the day "
                  "create now?",
             "a": ["6s", "12s", "3s", "It depends on the new price of labour-power"],
             "c": 0,
             "why": "Marx's first law: a day of given length always creates the same value, "
                    "however productive the labour. Twice as many articles share the 6s. Twelve "
                    "shillings and 3s each treat productivity as changing value; the price of "
                    "labour-power changes how the 6s is divided, not its total."},
            {"q": "On a 12-hour day the value of labour-power falls from 8 hours to 6. By what "
                  "proportion does surplus labour rise?",
             "a": ["By a half, from 4 hours to 6", "By a quarter, from 4 hours to 5",
                   "By a quarter, from 8 hours to 6", "It does not change"],
             "c": 0,
             "why": "Surplus labour goes from `12 − 8 = 4` to `12 − 6 = 6` hours, a rise of a "
                    "half, while labour-power falls by a quarter. The same two hours move each "
                    "way, which is the point Marx says Ricardo missed. The other answers mistake "
                    "the fall in labour-power for the rise in surplus labour."},
            {"q": "Which change can raise the value of labour-power and surplus value at the "
                  "same time, on Chapter 17's assumptions?",
             "a": ["A rise in the intensity of labour",
                   "A rise in productivity in the industries making necessaries",
                   "A fall in productivity in the industries making necessaries",
                   "No change can raise both at once"],
             "c": 0,
             "why": "A more intense day creates more value, so both parts can grow, as from 3s "
                    "each to 4s each. A change in productivity leaves the value created fixed, "
                    "so one part can grow only at the other's expense. A longer day can also "
                    "raise both, which is why the last option is wrong."},
            {"q": "Food grows dearer and the value of labour-power rises from 6 hours to 8. How "
                  "long must the day become for the rate of surplus value to stay at 100%?",
             "a": ["16 hours", "14 hours", "12 hours", "18 hours"],
             "c": 0,
             "why": "A rate of 100% needs as many surplus hours as necessary ones: 8 and 8, a "
                    "day of 16. At 14 hours the rate is `6/8`, 75%, and at 12 it is 50%. "
                    "Eighteen hours would raise the rate to 125%."},
        ],
        "mistakes": [
            ("Thinking higher productivity raises the value a worker produces each day",
             "It raises the number of things produced, not their value. A day of given length "
             "creates the same value whatever its productivity. In the productivity preset the "
             "day is still 12 hours of value, and what moves is its split: labour-power falls "
             "from 8 hours to 6, and the rate rises from 50% to 100%."),
            ("Expecting wages and surplus value always to move in opposite directions",
             "That holds when only productivity varies, because the value to be divided is "
             "fixed. When the day is longer or more intense, there is more value and both "
             "parts can rise; Marx's example takes each from 3s to 4s. Ricardo's error, as "
             "Marx tells it, was to treat the first case as the only one."),
            ("Reading a rise in wages as a rise above the value of labour-power",
             "In a more intense or longer day the worker's labour-power wears out faster, so "
             "its value can rise. A wage that rises less than that wear is a wage below value, "
             "however much larger it looks."),
        ],
        "standard": (
            "Finish when you can run Marx's cases for a change in the working day.",
            "Given a working day, its necessary time and a change in productivity, intensity "
            "or length, alone or together, compute the new value of labour-power and the new "
            "rate of surplus value, and state the direction each moved."
        ),
        "note": (
            "The lab holds the value of labour-power fixed when only the length or intensity "
            "of the day changes, which is Marx's starting case; he says the extra wear on the "
            "worker would raise it. Prices of labour-power above value, which Marx allows, "
            "are not computed. All the presets use Marx's figures, read in hours at his 6d an "
            "hour."
        ),
    },
    # ---------------------------------------------------------------- 09
    # Kerr vol. 1, l. 3912-3914 (the derivative formulae; can never reach
    # 100%); l. 3904 (substantially, but not consciously); l. 3914-3916
    # (Lavergne: a quarter and three-quarters, 300%); l. 3920 (the false
    # semblance of an association); l. 3930 (gratis); l. 3932 (command over
    # unpaid labour).
    {
        "slug": "formulae-for-the-rate-of-surplus-value",
        "title": "Formulae for the Rate of Surplus Value",
        "module": "Chapter 18 · Various Formulæ for the Rate of Surplus-Value",
        "one_line": "Surplus labour over the whole day measures how the day is shared, not the rate of exploitation, and it can never reach 100%.",
        "summary": (
            "The rate of surplus value compares surplus labour with necessary labour. The "
            "classical economists compared it with the whole working day instead. Compute "
            "both for the same day, see why the second can approach 100% but never reach it, "
            "and convert either one into the other."
        ),
        "key": [
            "rate: s/v = surplus / necessary",
            "derivative: s/(v + s) = surplus / whole day",
            "the derivative stays below 100%",
            "s/v = d / (1 − d), with d = s/(v + s)",
            "unpaid / paid = surplus / necessary",
        ],
        "key_label": "One day, two ratios",
        "concepts_intro": (
            "Chapter 18 is the shortest in Volume I. In the book its formulae are printed as "
            "fractions in displays; here they are written out."
        ),
        "concepts": [
            ("The rate of surplus value",
             "Surplus value over variable capital, or surplus labour over necessary labour: "
             "the same ratio in values and in times. Marx calls these formulae rigorously "
             "definite and correct."),
            ("The derivative formulae",
             "Surplus labour over the working day, surplus value over the value of the "
             "product, surplus product over total product. They describe how the day or its "
             "product is shared."),
            ("Unpaid over paid labour",
             "A popular form of the first ratio. It is accurate only if read as surplus over "
             "necessary labour, since the capitalist pays for labour-power, not labour."),
        ],
        "read_title": "A law that would hold, if the formulae were right",
        "read_intro": (
            "The passage follows the formulae, which the plain-text edition has lost. The "
            "words that matter survive."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 18.</strong> &ldquo;These derivative formulæ "
                  "express, in reality, only the proportion in which the working-day, or the "
                  "value produced by it, is divided between capitalist and labourer. If they are "
                  "to be treated as direct expressions of the degree of self-expansion of "
                  "capital, the following erroneous law would hold good: Surplus-labour or "
                  "surplus-value can never reach 100%.&rdquo;"),
            ("p", "Suppose you are told that a company's workers receive a quarter of what they "
                  "produce and its owners three-quarters. That sounds like 75%. Expressed "
                  "Marx's way, it is 300%. Both describe the same day, and the chapter is about "
                  "why the first figure hides what the second shows."),
            ("p", "Marx first lists his own formulae: surplus value over variable capital, "
                  "surplus value over the value of labour-power, surplus labour over necessary "
                  "labour. They are the same ratio stated three ways, and the classical "
                  "economists worked with them &ldquo;substantially, but not "
                  "consciously&rdquo;. What the economists wrote down instead were the "
                  "derivative formulae: surplus labour over the working day, surplus value over "
                  "the value of the product, surplus product over the whole product. The value of "
                  "the product here means only the value newly created, without the constant "
                  "capital."),
            ("p", "Read the passage now. A derivative formula divides a part of the day by the "
                  "whole. Since the surplus labour is always a part, the ratio is always below "
                  "1. To reach 100% the surplus labour would have to be the whole day, and then "
                  "the necessary labour would be zero, and with it the worker, and with him the "
                  "surplus labour. So the ratio can approach 100% and never get there. The "
                  "rate of surplus value has no such ceiling: it divides surplus by necessary, "
                  "and as necessary labour shrinks the rate grows without bound."),
            ("def", ("The derivative formula",
                     "Surplus labour divided by the whole working day, or surplus value divided "
                     "by the new value created, `s/(v + s)`. It measures the share of the day or "
                     "its product that goes to the capitalist, not the rate of surplus value, "
                     "`s/v`.")),
            ("p", "Marx's example is the French economist Léonce de Lavergne's estimate that the "
                  "English agricultural labourer gets a quarter of the product and the farmer "
                  "three-quarters. By the derivative formula that is 75%. By the rate of surplus "
                  "value it is three to one, &ldquo;which gives a rate of exploitation of "
                  "300%.&rdquo; The two numbers are tied together: if `d` is the share taken as "
                  "surplus, the rate is `d/(1 − d)`, so three-quarters over one-quarter is 3, and "
                  "the rate can be recovered from the share at any time, as Marx shows with "
                  "6 hours over 12 becoming 6 over 6."),
            ("p", "The lab computes both for a 12-hour day. In the half preset, with 6 hours "
                  "necessary, they are 100% and 50%. In the two-thirds preset, with 4 hours "
                  "necessary, 200% and two-thirds. The lavergne preset is Lavergne's quarter, "
                  "3 hours in 12: 300% and three-quarters. And in the extreme preset, with a "
                  "single necessary hour, the rate of surplus value is 1,100% while the share "
                  "is eleven-twelfths, still "
                  "short of 100%. Every step that doubles or triples the first barely moves the "
                  "second."),
            ("p", "Why should the choice matter? Because, Marx says, representing surplus value "
                  "and wages as fractions of the value created hides the transaction that "
                  "creates them:"),
            ("p", "<strong>Volume I, Chapter 18.</strong> &ldquo;Instead of the real fact, we "
                  "have the false semblance of an association, in which labourer and capitalist "
                  "divide the product in proportion to the different elements which they "
                  "respectively contribute towards its formation.&rdquo;"),
            ("p", "A share looks like a partnership; a ratio of unpaid to paid labour looks like "
                  "what Marx thinks it is. The economists who accept the share as the natural "
                  "measure would answer that it is a partnership: labour and capital each "
                  "contribute, and each is paid its contribution. That is the dispute the whole "
                  "book has been about, and the choice of formula does not settle it; it only "
                  "decides which side's language the number is written in."),
            ("p", "The last pages restate the point as a formula of their own, unpaid labour "
                  "over paid labour, and warn against reading it as payment for labour: the "
                  "capitalist pays for labour-power, and its use during the surplus hours "
                  "&ldquo;comes to him gratis&rdquo;. Marx ends Part V with a correction to "
                  "Adam Smith: &ldquo;Capital, therefore, is not only, as Adam Smith says, the "
                  "command over labour. It is essentially the command over unpaid "
                  "labour.&rdquo;"),
            ("p", "That warning is where the next course begins. Wages and Accumulation opens "
                  "with “The Value of Labour-Power Becomes Wages”, on why a wage looks like the "
                  "price of all the labour done when it is the price of the labour-power."),
        ],
        "lab": ("capkit", {
            "mode": "surplus",
            "view": "formulae",
            "money_unit": "s",
            "preset": "half",
            "presets": [
                {"id": "half", "label": "A 12-hour day, 6 hours necessary",
                 "hours": 12, "necessary_hours": 6, "expect": {"suRate": "1 = 100%", "suFalse": "1/2 = 50%"}},
                {"id": "two-thirds", "label": "A 12-hour day, 4 hours necessary",
                 "hours": 12, "necessary_hours": 4, "expect": {"suRate": "2 = 200%", "suFalse": "2/3 = 66.67%"}},
                {"id": "lavergne", "label": "Lavergne's labourer: a quarter of the day necessary",
                 "hours": 12, "necessary_hours": 3, "expect": {"suRate": "3 = 300%", "suFalse": "3/4 = 75%"}},
                {"id": "extreme", "label": "A 12-hour day, 1 hour necessary",
                 "hours": 12, "necessary_hours": 1, "expect": {"suRate": "11 = 1,100%", "suFalse": "11/12 = 91.67%"}},
            ],
            "panel_title": "The same day, two ratios",
            "panel_intro": (
                "The hours worked and the necessary hours go in. The lab divides the surplus "
                "labour by the necessary labour, which is the rate of surplus value, and by "
                "the whole day, which is the derivative formula."
            ),
        }),
        "steps_title": "Converting between the two ratios",
        "steps_intro": "Four steps for any working day, or any division of its product.",
        "steps": [
            ("Split the day",
             "Write the working day and its necessary part. Surplus labour is the day less "
             "the necessary labour."),
            ("Compute the rate",
             "Divide surplus labour by necessary labour. This is `s/v`, the rate of surplus "
             "value."),
            ("Compute the share",
             "Divide surplus labour by the whole day. This is `s/(v + s)`, which is below 1 "
             "whenever any labour is necessary."),
            ("Convert",
             "From a share `d`, the rate is `d/(1 − d)`; from a rate `r`, the share is "
             "`r/(1 + r)`."),
        ],
        "worked": {
            "title": "Eight hours of surplus in twelve",
            "intro": [
                "A 12-hour day has 4 hours of necessary labour and 8 of surplus labour. You want "
                "the rate of surplus value and the derivative share, and to recover one from "
                "the other.",
            ],
            "lines": [
                "rate:  8 / 4 = 2 = 200%",
                "share:  8 / 12 = 2/3",
                "from share to rate:  (2/3) / (1/3) = 2",
                "from rate to share:  2 / (1 + 2) = 2/3",
            ],
            "after": [
                "Two-thirds sounds moderate and 200% does not, and they are the same day. The "
                "share can never reach 1; the rate has no ceiling.",
            ],
        },
        "quiz_title": "Rates and shares",
        "quiz": [
            {"q": "A 10-hour day has 2 hours of necessary labour. What are the rate of surplus "
                  "value and the derivative share?",
             "a": ["400% and 4/5", "80% and 4/5", "400% and 1/4", "500% and 4/5"],
             "c": 0,
             "why": "Surplus labour is 8 hours: `8/2 = 4`, 400%, and `8/10 = 4/5`. Eighty per "
                    "cent is the share written as a rate, a quarter is necessary over surplus, "
                    "and 500% divides the whole day by the necessary hours."},
            {"q": "Workers receive a fifth of the new value their day creates. What is the rate "
                  "of surplus value?",
             "a": ["400%", "80%", "20%", "500%"],
             "c": 0,
             "why": "The capitalist takes four-fifths, so surplus over necessary is `4/1`, 400%. "
                    "Eighty per cent is the derivative share; 20% is the workers' share; 500% "
                    "divides the whole by the workers' part."},
            {"q": "Why, on Marx's account, can surplus labour over the working day never reach "
                  "100%?",
             "a": ["Surplus labour is only part of the day, and without necessary labour there "
                   "is no surplus labour either",
                   "The law limits the working day",
                   "Wages can never fall to zero by statute",
                   "Constant capital always takes part of the product"],
             "c": 0,
             "why": "The ratio divides a part by the whole, and to equal the whole the "
                    "necessary labour would have to vanish, taking surplus labour with it. Legal "
                    "limits and statutes play no part in the argument, and the value of the "
                    "product in these formulae excludes constant capital."},
        ],
        "mistakes": [
            ("Treating s/(v + s) as the measure of exploitation",
             "It measures the share of the day the capitalist receives, and it can never reach "
             "100%. In the extreme preset the rate of surplus value is 1,100% while the share "
             "is `11/12`, 91.67%; in Lavergne's case they are 300% and 75%. Marx's measure is "
             "surplus over necessary labour, which has no ceiling."),
            ("Thinking the two formulae describe different days",
             "They are two divisions of the same day and convert exactly: a share `d` is a "
             "rate `d/(1 − d)`. Marx's own conversion takes 6 surplus hours over a 12-hour day "
             "to 6 over 6, which is 100%."),
            ("Reading unpaid over paid labour as payment for labour",
             "The formula is a popular form of surplus over necessary labour. The capitalist "
             "pays the value of labour-power; he does not pay for some hours and not others. "
             "Chapter 18 warns against the slip, and the next course takes it up."),
        ],
        "standard": (
            "Finish when you can compute and convert both ratios for a working day.",
            "Given a working day and its necessary labour, or the shares of the new value "
            "going to wages and surplus value, compute the rate of surplus value and the "
            "derivative share and convert each into the other."
        ),
        "note": (
            "The book prints the formulae of Chapter 18 as fractions in displays, which the "
            "plain-text Kerr edition lost; the lesson states them from the prose around them. "
            "The lab's derivative formula is surplus over the whole day, which equals surplus "
            "value over new value only if every hour adds the same value. The days are "
            "illustrative except Lavergne's quarter, which Marx quotes."
        ),
    },
]
