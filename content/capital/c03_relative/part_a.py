"""Relative Surplus Value, lessons 1-5 -- Volume I, Chapters 12 to 15.

Chapter 12, Chapter 13, Chapter 14, and the first two of the three lessons on
Chapter 15 (the value machinery transfers; the intensification of labour).

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals in the text are left out of the quotations, a
drop capital ("THAT", "CAPITALIST") is printed as an ordinary capital, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 1, l. 2609 (the definitions of absolute and relative
    # surplus-value); l. 2631 (to cheapen the labourer himself); l. 2603 (one-tenth
    # less of the necessaries; plays in actual practice); l. 2614-2616 (pro tanto;
    # by no means necessarily aims; tendencies and forms of manifestation);
    # l. 2627 (the coercive law of competition); l. 2633 (Quesnay's riddle).
    {
        "slug": "the-concept-of-relative-surplus-value",
        "title": "The Concept of Relative Surplus Value",
        "module": "Chapter 12 · The Concept of Relative Surplus-Value",
        "one_line": "With the working day fixed, surplus labour can grow only if necessary labour shrinks, and that needs cheaper necessaries, not lower wages.",
        "summary": (
            "Chapter 12 asks how surplus labour can grow when the working day cannot. Its "
            "answer is that the necessary part of the day must shrink, which on Marx's "
            "assumptions means the necessaries must get cheaper. Compute the new rate of "
            "surplus value when necessary time falls from 10 hours to 9, the extra surplus "
            "value of one capitalist who doubles productivity before anyone else, and what "
            "is left of it once everyone has caught up."
        ),
        "key": [
            "absolute: the day is lengthened",
            "relative: necessary time is cut",
            "cut it by cheapening necessaries",
            "a wage below value is excluded",
            "the pioneer gains until all catch up",
        ],
        "key_label": "Surplus value of the second kind",
        "concepts_intro": (
            "Part III held the necessary part of the day fixed and let the day grow. Part "
            "IV holds the day fixed and asks what else can move. Three ideas carry the "
            "chapter."
        ),
        "concepts": [
            ("Absolute and relative surplus value",
             "Surplus value got by lengthening the working day is absolute. Surplus value got "
             "by shortening the necessary part of a day of given length is relative. The two "
             "are told apart by which end of the surplus labour moves."),
            ("Cheapening the worker",
             "With labour-power bought at its value, necessary time falls only if the value "
             "of labour-power falls, and that falls only if the things workers live on, or "
             "the means of producing them, take less labour to make."),
            ("Extra surplus value",
             "A capitalist whose method is ahead of the rest makes his goods with less "
             "labour than their social value. Selling at or near the social value, he "
             "pockets the difference, until competition spreads the method and the "
             "difference disappears."),
        ],
        "read_title": "Two names for two ways of getting more",
        "read_intro": (
            "The definitions come a few pages into the chapter, after Marx has shown that a "
            "wage cut is not what he means. The passage is short and exact, so it is worth "
            "reading slowly."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 12.</strong> &ldquo;The surplus-value produced by "
                  "prolongation of the working day, I call absolute surplus-value. On the other "
                  "hand, the surplus-value arising from the curtailment of the necessary "
                  "labour-time, and from the corresponding alteration in the respective lengths "
                  "of the two components of the working day, I call relative "
                  "surplus-value.&rdquo;"),
            ("p", "Marx draws the day as a line from a through b to c: from a to b the worker "
                  "replaces the value of his labour-power, from b to c he works for the capitalist. In "
                  "the previous course's two lessons on Chapter 10 the point c moved, as the day was "
                  "pushed out to fourteen or fifteen hours. Here c is fixed by law or custom at "
                  "twelve, and the question is whether b can be pushed back towards a. Marx's "
                  "figures are a 12-hour day with 10 hours necessary and 2 surplus. Move b "
                  "back by an hour and the surplus labour grows by half, from 2 hours to 3, "
                  "though the day has not changed by a minute."),
            ("p", "The obvious way to move b is to pay less, and Marx raises it himself. Pay "
                  "4s 6d instead of 5s and nine hours replace the wage instead of ten. But that "
                  "is buying labour-power below its value, the worker &ldquo;commands one-tenth "
                  "less of the necessaries of life than before&rdquo;, and the book has assumed "
                  "since Chapter 1 that every commodity, labour-power included, sells at its "
                  "value. Marx grants that the method &ldquo;plays in actual practice&rdquo; an "
                  "important part and sets it aside. On his assumption the necessary time can "
                  "fall only if the value of labour-power itself falls."),
            ("p", "And that value is the value of the worker's necessaries. So the necessaries "
                  "must take less labour to make: bread, shirts, boots, and also the leather, "
                  "thread and tools that go into boots. Productivity has to rise in those "
                  "industries, and only in those. Cheaper diamonds leave the value of "
                  "labour-power where it was. And each cheapened article lowers it only "
                  "&ldquo;pro tanto&rdquo;, in proportion to its place in what the worker "
                  "buys: shirts are one item among many."),
            ("p", "Think of how this looks from inside a firm. Nobody who introduces a better "
                  "loom is thinking about the national value of labour-power. Marx agrees: the "
                  "capitalist who cheapens shirts &ldquo;by no means necessarily aims at "
                  "reducing the value of labour-power&rdquo;, and &ldquo;The general and "
                  "necessary tendencies of capital must be distinguished from their forms of "
                  "manifestation.&rdquo; So he tells the story from inside the firm too, with "
                  "numbers."),
            ("p", "An hour of labour is embodied in sixpence, so a 12-hour day adds 6s. Twelve "
                  "articles are made in it, each with 6d of means of production, so each is "
                  "worth 1s. One capitalist doubles productivity and makes 24. Each now costs "
                  "him 9d: the same 6d of materials and only 3d of new labour. But the social "
                  "value is still 1s, and if he sells at that he gains 3d an article over his "
                  "individual value, 6s in a day, which is 12 hours of social labour. To sell "
                  "twice as many he will shade the price, and Marx's example has him sell at "
                  "10d. Even then, his day's surplus value goes from 1s to 3s, and the worker "
                  "replaces his 5s wage in `7 1/2` hours instead of 10."),
            ("p", "That gain is the motive. It does not depend on whether his article is a "
                  "necessary at all; a maker of mirrors would chase it too. And it is "
                  "temporary. The same law of value that let him sell above his individual "
                  "value, &ldquo;acting as a coercive law of competition, forces his "
                  "competitors to adopt the new method&rdquo;. When they have, the social value "
                  "has fallen to 9d and the extra is gone. What remains, if the article is one "
                  "the workers live on, is a lower value of labour-power for every capitalist "
                  "at once."),
            ("p", "<strong>Volume I, Chapter 12.</strong> &ldquo;Hence there is immanent in "
                  "capital an inclination and constant tendency, to heighten the productiveness "
                  "of labour, in order to cheapen commodities, and by such cheapening to cheapen "
                  "the labourer himself.&rdquo;"),
            ("def", ("Relative surplus value",
                     "Surplus value that arises because, the working day being given, the "
                     "necessary labour-time is shortened by a fall in the value of labour-power, "
                     "which in turn follows from a rise in productivity in the industries that "
                     "make the workers' necessaries or their means of production.")),
            ("p", "The lab runs Marx's day four ways. The given preset, 10 hours necessary in "
                  "12, is a rate of `2/10`, 20%. The cheaper preset cheapens the necessaries so "
                  "that 9 hours replace the wage, and the rate is `3/9`, a third. The pioneer "
                  "preset leaves the necessaries alone and doubles one capitalist's "
                  "productivity: the general rate stays at 20% and he alone gains 12 hours a "
                  "day, Marx's 6s at the full social value. In the general preset the method "
                  "has spread to the wage-goods "
                  "industries and labour-power has fallen from 5s to 3s, Marx's own later "
                  "figure: the necessary time is 6 hours, the rate is 100%, and the pioneer's "
                  "extra is zero."),
            ("p", "Marx ends with a riddle he credits to François Quesnay, the court physician "
                  "who founded the Physiocrats: why does the capitalist, who cares only about "
                  "exchange-value, keep trying to lower the exchange-value of what he sells? "
                  "Because &ldquo;The value of a commodity is, in itself, of no interest to the "
                  "capitalist&rdquo;; only the surplus value in it is, and the process that "
                  "cheapens commodities is the one that enlarges it. Economists who think in "
                  "terms of innovation will recognise the pioneer. Joseph Schumpeter, writing "
                  "in 1911, also traced profit to the innovator's lead and its erosion by "
                  "imitators, without any theory of surplus labour behind it. The arithmetic of "
                  "the lead is the same; what it is a lead in is the dispute."),
            ("p", "Productivity, then, is how capital gets more from a day it cannot lengthen. "
                  "The next lesson, “Co-operation”, starts with the simplest way of raising it: "
                  "putting many workers in one place."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "relative",
            "money_unit": "hours",
            "preset": "given",
            "presets": [
                {"id": "given", "label": "Marx's day: 12 hours, 10 of them necessary",
                 "day": 12, "necessary": 10, "productivity": 1, "pioneer_productivity": 1,
                 "expect": {"wdRate": "1/5 = 20%", "wdExtra": "0 h"}},
                {"id": "cheaper", "label": "Necessaries cheapen: 10 necessary hours become 9",
                 "day": 12, "necessary": 10, "productivity": "10/9", "pioneer_productivity": 1,
                 "expect": {"wdRate": "1/3 = 33.33%", "wdExtra": "0 h"}},
                {"id": "pioneer", "label": "One capitalist doubles productivity (Marx's 24 articles)",
                 "day": 12, "necessary": 10, "productivity": 1, "pioneer_productivity": 2,
                 "expect": {"wdRate": "1/5 = 20%", "wdExtra": "+12 h"}},
                {"id": "general", "label": "The method spreads to wage goods: labour-power 5s to 3s",
                 "day": 12, "necessary": 10, "productivity": "5/3", "pioneer_productivity": 1,
                 "expect": {"wdRate": "1 = 100%", "wdExtra": "0 h"}},
            ],
            "panel_title": "A twelve-hour day that cannot be lengthened",
            "panel_intro": (
                "The day is fixed at 12 hours. Productivity in the wage-goods industries "
                "divides the necessary time; the pioneer's productivity is one capitalist's "
                "method against the average, and his extra surplus value is counted at the "
                "full social value of what he sells."
            ),
        }),
        "steps_title": "Finding relative surplus value in a fixed day",
        "steps_intro": "Four steps for any change that leaves the length of the day alone.",
        "steps": [
            ("Fix the day and the necessary time",
             "Write down the length of the working day and the hours that replace the value "
             "of a day's labour-power. Their difference is the surplus labour."),
            ("Find the new value of labour-power",
             "If productivity in the industries making the necessaries rises by a factor, "
             "divide the necessary time by it. A rise anywhere else leaves it unchanged."),
            ("Recompute the rate",
             "Surplus labour is the day less the new necessary time; the rate is surplus "
             "over necessary. The day has not changed, so any rise is relative."),
            ("Separate the pioneer's extra",
             "For one capitalist ahead of the rest, value his output at its social value and "
             "subtract what it cost him. The difference is extra surplus value, and it falls "
             "to zero when the method is general."),
        ],
        "worked": {
            "title": "Twenty-four articles at tenpence",
            "intro": [
                "Take Marx's pioneer. His 12-hour day makes 24 articles instead of 12, each "
                "with 6d of means of production, and he sells them at 10d to find buyers for "
                "twice the usual number. His worker's labour-power is worth 5s a day. You want "
                "his surplus value and the hours in which the wage is replaced.",
            ],
            "lines": [
                "sales:  24 · 10d = 240d = 20s",
                "means of production:  24 · 6d = 144d = 12s",
                "new value realised:  20s − 12s = 8s",
                "surplus value:  8s − 5s = 3s (was 1s)",
                "wage replaced in:  12 h · 5/8 = 7 1/2 h",
            ],
            "after": [
                "His worker's necessary labour has fallen from 10 hours to `7 1/2` without any "
                "change in what the worker is paid or can buy. The book prints `7 1/5` hours "
                "here, and a surplus labour increased by `2 4/5`, and every other figure in the "
                "same paragraph says `7 1/2`. Marx has the day's labour carried by `9 3/5` "
                "articles, 6 of them for the wage, and 6 of `9 3/5` is five-eighths, the same "
                "as 5s of the 8s; he gives the new ratio of necessary to surplus labour as 5 to "
                "3; and he has surplus value grow from 1s to 3s. Each of these makes the "
                "necessary time `7 1/2` hours and the surplus `4 1/2`, not `7 1/5` and `4 4/5`, "
                "so the slip is in the text, not in the method. Selling at the full 1s would "
                "have given 6s of extra surplus value; the lab's pioneer preset counts at that "
                "full social value.",
            ],
        },
        "quiz_title": "Absolute, relative and extra",
        "quiz": [
            {"q": "A working day of 12 hours has 10 hours of necessary labour. The necessaries "
                  "cheapen so that 9 hours replace the wage. What is the new rate of surplus "
                  "value?",
             "a": ["1/3, about 33%", "1/5, 20%", "1/4, 25%", "1/2, 50%"],
             "c": 0,
             "why": "Surplus labour is `12 − 9 = 3` hours against 9 necessary, so `3/9 = 1/3`. "
                    "One fifth is the rate before the change. One quarter divides the surplus by "
                    "the whole day, not by the necessary time, and one half matches no step of "
                    "the example."},
            {"q": "On Chapter 12's definitions, which of these produces relative surplus value?",
             "a": ["Cheaper shirts, which workers buy, lower the value of labour-power",
                   "The working day is lengthened from 12 hours to 14",
                   "Wages are cut from 5s to 4s 6d while the necessaries cost what they did",
                   "Cheaper diamonds, which workers do not buy"],
             "c": 0,
             "why": "Relative surplus value needs a fall in the value of labour-power, which "
                    "cheaper necessaries bring. A longer day is absolute surplus value. A wage "
                    "cut with prices unchanged is labour-power bought below its value, which "
                    "Marx excludes. Cheaper diamonds leave the value of labour-power where it "
                    "was."},
            {"q": "In the pioneer preset, one capitalist gains 12 hours a day of extra surplus "
                  "value. What happens to that gain once his method is in general use?",
             "a": ["It disappears, because the social value falls to his individual value",
                   "It doubles, because every capitalist now earns it",
                   "It stays at 12 hours, because his productivity is still double",
                   "It becomes part of the value of labour-power"],
             "c": 0,
             "why": "The extra exists only while his individual value is below the social "
                    "value. When everyone uses the method the two are equal and the extra is "
                    "zero. His productivity is still double the old average, but it is now the "
                    "average. It does not enter the value of labour-power, which depends on "
                    "the necessaries."},
            {"q": "Marx's pioneer sells 24 articles at 10d, with 6d of means of production in "
                  "each and a day's labour-power worth 5s. What is his surplus value for the day?",
             "a": ["3s", "1s", "8s", "6s"],
             "c": 0,
             "why": "Sales are 20s, the means of production 12s, so the new value realised is "
                    "8s, and 8s less the 5s wage is 3s. One shilling is the surplus value of an "
                    "ordinary capitalist; 8s is the new value before the wage is paid; 6s is the "
                    "extra he would gain selling at the full 1s."},
        ],
        "mistakes": [
            ("Thinking the capitalist innovates in order to lower the value of labour-power",
             "Marx says the reverse of the individual: he &ldquo;by no means necessarily "
             "aims&rdquo; at it. His motive is the extra surplus value of selling below the "
             "social value and above his own. In the pioneer preset he gains 12 hours a day "
             "while the general rate stays at 20%: the gain is there whether or not his "
             "article is a necessary. The fall in the value of labour-power is the combined "
             "result, which the general preset shows, at a rate of 100% and an extra of "
             "zero."),
            ("Counting a wage cut as relative surplus value",
             "Paying 4s 6d instead of 5s would also leave 3 hours of surplus labour in the "
             "day. Marx sets it aside because it buys labour-power below its value, which "
             "his argument has assumed away since Chapter 1. Relative surplus value is a fall "
             "in the value itself, with the worker buying exactly what he bought before."),
            ("Expecting the pioneer's advantage to last",
             "His extra depends on the gap between his individual value and the social "
             "value. Competition closes it by forcing the method on everyone. A lasting gain "
             "survives only where the cheapened article is one the workers live on, and then "
             "it is a gain for every capitalist, not for him."),
        ],
        "standard": (
            "Finish when you can compute relative and extra surplus value in a fixed day.",
            "Given a working day, the necessary time and a rise in productivity in the "
            "wage-goods industries, compute the new rate of surplus value; given one "
            "capitalist's output, costs and selling price, compute his surplus value and "
            "state when his extra disappears."
        ),
        "note": (
            "The lab treats all the necessaries as one good, cheapened by one factor; Marx "
            "says each article lowers the value of labour-power only in proportion to its "
            "share of what workers buy. Its pioneer sells at the full social value, where "
            "Marx's sells at 10d. And it counts the pioneer's extra in hours of social "
            "labour, which is the step a theory of price without labour-values would not "
            "take. The day of 12 hours and the articles are Marx's figures."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 1, l. 2683 (the combined working day; the social productive
    # power of labour); l. 2707-2709 (he pays for 100 independent
    # labour-powers; this power costs capital nothing); l. 2645 (simply
    # enlarged); l. 2650 (Burke's platoon); l. 2656 (one workshop for twenty);
    # l. 2672 (hands and eyes); l. 2697 (the violin player); l. 2705 (a leader
    # of industry because he is a capitalist).
    {
        "slug": "co-operation",
        "title": "Co-operation",
        "module": "Chapter 13 · Co-operation",
        "one_line": "Many workers in one place under one capital produce more than the same number apart, and the capitalist pays for none of the difference.",
        "summary": (
            "Capitalist production starts where one capital employs many workers at once. "
            "Marx finds in their combined working day a productive power no single worker "
            "has, and a saving in the means of production they use in common. Compute the "
            "constant capital in each unit of output when a workshop is shared, and the "
            "combined day of twelve masons or a hundred harvesters, and see what in it the "
            "wage pays for."
        ),
        "key": [
            "many workers, one place, one capital",
            "combined day = workers × hours",
            "shared means: less c per unit",
            "wages buy separate labour-powers",
            "the combined power is unpaid",
        ],
        "key_label": "The simplest relative surplus value",
        "concepts_intro": (
            "Chapter 13 is short and its machinery is nothing but numbers of people. Three "
            "things happen when they are gathered."
        ),
        "concepts": [
            ("The combined working day",
             "Twelve workers for 12 hours are a working day of 144 hours from the "
             "capitalist's side. Their individual differences cancel, so the combined day "
             "is a day of average social labour."),
            ("Means of production used in common",
             "One workshop for twenty costs less than ten for two. Buildings, stores and "
             "tools used in common give up less value to each unit of product, which "
             "cheapens it as if they had cost less."),
            ("A power that costs capital nothing",
             "Co-operation creates a productive power of its own, from many hands at a "
             "critical moment to emulation. The capitalist buys separate labour-powers and "
             "gets their combination free."),
        ],
        "read_title": "The combined working day",
        "read_intro": (
            "The passage comes after Marx has listed every way a combined day can beat the "
            "same number of separate days. He sums them up in one sentence."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 13.</strong> &ldquo;The combined working day "
                  "produces, relatively to an equal sum of isolated working-days, a greater "
                  "quantity of use-values, and, consequently, diminishes the labour-time "
                  "necessary for the production of a given useful effect. &hellip; the special "
                  "productive power of the combined working day is, under all circumstances, the "
                  "social productive power of labour, or the productive power of social labour. "
                  "This power is due to co-operation itself.&rdquo;"),
            ("p", "Marx opens the chapter by saying that at first nothing seems to change. A "
                  "workshop with many workers under one master is a medieval workshop "
                  "&ldquo;simply enlarged&rdquo;. If a day of 12 hours is embodied in 6s, 1,200 "
                  "such days are embodied in 1,200 times 6s, whether the men work together or "
                  "apart. Numbers alone do not change the rate of surplus value. Then come the "
                  "changes that make numbers matter."),
            ("p", "The first is averaging. One worker may be quick and another slow, but twelve "
                  "together, working 12 hours each, make a collective day of 144 hours, and "
                  "the individual differences cancel. Marx quotes Edmund Burke, writing as a "
                  "farmer, that &ldquo;in so small a platoon&rdquo; as five farm labourers "
                  "all individual differences vanish. Split the same twelve among six small "
                  "masters, two each, and it becomes a matter of chance whether a given master "
                  "gets average labour. The law of value holds for the individual employer, "
                  "Marx concludes, only when he employs many."),
            ("p", "The second is economy in the means of production. A room for twenty weavers "
                  "must be larger than a room for one weaver and two assistants, &ldquo;But it "
                  "costs less labour to build one workshop for twenty persons than to build ten "
                  "to accommodate two weavers each&rdquo;. The shared building gives up less "
                  "value to each yard of cloth, and the effect is the same as if it had cost "
                  "less. That is the first figure the lab computes: constant capital per unit "
                  "of output, used alone and used in common."),
            ("p", "The third is the new power itself. A squadron of cavalry is not the sum of "
                  "its riders. Twelve masons in a row passing stones up a ladder move them "
                  "faster than twelve men each climbing with his own load, and a body of men "
                  "working on a building from every side at once has &ldquo;hands and eyes both "
                  "before and behind&rdquo;. Some work must be done at a critical moment: a "
                  "flock to be shorn, a field to be harvested before the weather turns. One man "
                  "can carve 12 hours out of a natural day; a hundred men together make a day "
                  "of 1,200 hours, at the moment it is needed."),
            ("p", "Who pays for all this? Not the capitalist, and that is the chapter's turn. He "
                  "makes a separate contract with each worker for that worker's own "
                  "labour-power, which is all the worker has to sell:"),
            ("p", "<strong>Volume I, Chapter 13.</strong> &ldquo;He pays them the value of 100 "
                  "independent labour-powers, but he does not pay for the combined labour-power "
                  "of the hundred. &hellip; Because this power costs capital nothing, and "
                  "because, on the other hand, the labourer himself does not develop it before "
                  "his labour belongs to capital, it appears as a power with which capital is "
                  "endowed by Nature&mdash;a productive power that is immanent in "
                  "capital.&rdquo;"),
            ("def", ("Co-operation",
                     "Many workers working side by side, in the same process or in connected "
                     "ones, according to a plan. Under capital it is brought about by the "
                     "capital that employs them all, and its productive power appears as a "
                     "power of that capital.")),
            ("p", "The lab works the economy of shared means of production. In the one preset "
                  "a worker alone, with 10s of tools and room, makes 12 pieces in a day, so "
                  "each carries 10d of constant capital. In the masons preset twelve masons "
                  "sharing the same 10s of tackle make 144 pieces in a combined day of 144 "
                  "hours, and each piece carries `5/6` of a penny. The workshop preset builds a "
                  "room for twelve at 60s, dearer than one worker's room but far cheaper than "
                  "twelve, and puts 5d into each piece. The harvest preset is Marx's hundred "
                  "harvesters, a combined day of 1,200 hours, with each piece carrying `1 1/5` "
                  "pence together against 6d alone. In none of these is a wage an input. The "
                  "wages buy the labour-powers, and the combination comes with them."),
            ("p", "Gathering a hundred workers takes money in advance: a week's wages for all of "
                  "them in the capitalist's pocket, and the raw material for all of them. So "
                  "the scale of co-operation depends on the size of capital. And once labour is "
                  "combined, it needs direction. &ldquo;A single violin player is his own "
                  "conductor; an orchestra requires a separate one.&rdquo; Marx grants the need "
                  "and denies the inference: the work of directing becomes a function of "
                  "capital, and under capital it is also supervision of people whose interests "
                  "run against the employer's. &ldquo;It is not because he is a leader of "
                  "industry that a man is a capitalist; on the contrary, he is a leader of "
                  "industry because he is a capitalist.&rdquo;"),
            ("p", "The obvious reply comes from economists who see the organiser's work as "
                  "productive in its own right, and pay as its price. On that account the "
                  "co-operative gain is partly the return to coordination, and the firm exists "
                  "because coordination inside it is cheaper than through the market, which is "
                  "Ronald Coase's answer, in 1937, to why firms exist at all. The chapter was "
                  "written long before that, and what it says bears on the first half of the "
                  "view: once co-operation is large enough the capitalist hands supervision "
                  "&ldquo;to a special kind of wage labourer&rdquo;, managers and overlookers, "
                  "so the work of directing is paid as a wage while the capital's return "
                  "remains. Volume III takes the question up again, where profit of enterprise "
                  "is set beside the wages of superintendence."),
            ("p", "Co-operation in its simple form leaves each worker doing what he did before, "
                  "only beside others. The next lesson, “Division of Labour and Manufacture”, "
                  "takes the next step: splitting the work itself into pieces."),
        ],
        "lab": ("capkit", {
            "mode": "machine",
            "view": "cooperate",
            "money_unit": "s",
            "qty_unit": "pieces",
            "preset": "one",
            "presets": [
                {"id": "one", "label": "One worker alone, 10s of tools and room",
                 "workers": 1, "output_each": 12, "shared_c": 10, "c_each_if_alone": 10,
                 "hours": 12, "expect": {"maCPerUnit": "alone 10d, together 10d", "maCombinedDay": "12 h"}},
                {"id": "masons", "label": "Marx's 12 masons, 12 hours each, sharing 10s of tackle",
                 "workers": 12, "output_each": 12, "shared_c": 10, "c_each_if_alone": 10,
                 "hours": 12, "expect": {"maCPerUnit": "alone 10d, together 5/6 d", "maCombinedDay": "144 h"}},
                {"id": "workshop", "label": "One workshop for 12, built at 60s",
                 "workers": 12, "output_each": 12, "shared_c": 60, "c_each_if_alone": 10,
                 "hours": 12, "expect": {"maCPerUnit": "alone 10d, together 5d", "maCombinedDay": "144 h"}},
                {"id": "harvest", "label": "Marx's 100 harvesters, 12 hours each, sharing carts",
                 "workers": 100, "output_each": 10, "shared_c": 100, "c_each_if_alone": 5,
                 "hours": 12, "expect": {"maCPerUnit": "alone 6d, together 1 1/5 d", "maCombinedDay": "1,200 h"}},
            ],
            "panel_title": "What co-operation saves",
            "panel_intro": (
                "The means of production one worker needs alone go into one worker's output; "
                "the means shared by all go into everyone's. The combined day is the workers "
                "times the hours. The money figures are illustrative; the numbers of workers "
                "and hours in the masons and harvest presets are Marx's."
            ),
        }),
        "steps_title": "Counting what co-operation gives",
        "steps_intro": "Four steps for any group of workers gathered under one capital.",
        "steps": [
            ("Count the combined day",
             "Multiply the workers by the hours each works. The result is one working day "
             "from the capitalist's side, and in it individual differences average out."),
            ("Find the constant capital per unit alone",
             "Divide the means of production one worker would need working alone by that "
             "worker's daily output."),
            ("Find it in common",
             "Divide the means of production the group shares by the group's total output. "
             "The shared means may cost more in all and still less per unit."),
            ("Ask what the wage paid for",
             "The wage bill is so many separate labour-powers at their value. Any gain from "
             "combining them, in output or in shared means, is not in it."),
        ],
        "worked": {
            "title": "Twelve masons and their tackle",
            "intro": [
                "A mason working alone needs 10s of ladder, scaffold and tools, and makes 12 "
                "pieces of work in a 12-hour day. Twelve masons share one set of the same "
                "tackle. You want the constant capital in each piece both ways, and the "
                "combined working day.",
            ],
            "lines": [
                "alone:  10s / 12 pieces = 10d a piece",
                "together:  12 · 12 = 144 pieces",
                "together:  10s / 144 = 120d / 144 = 5/6 d a piece",
                "combined day:  12 · 12 h = 144 h",
            ],
            "after": [
                "The same 10s of tackle now passes a twelfth as much value into each piece. "
                "Nothing in the calculation is a wage, and nothing in the wage bill changed: "
                "twelve labour-powers were bought, at their value, either way.",
            ],
        },
        "quiz_title": "What the combination yields",
        "quiz": [
            {"q": "Twelve workers each work a 12-hour day in one workshop. From the capitalist's "
                  "side, what is the combined working day?",
             "a": ["144 hours", "12 hours", "24 hours", "156 hours"],
             "c": 0,
             "why": "Each worker's day is a twelfth of the collective day, so it is `12 · 12 = "
                    "144` hours. Twelve hours is one worker's day. The other two add the numbers "
                    "instead of multiplying them, or add the workers on top."},
            {"q": "Working alone, a weaver needs a 10s room and makes 20 yards a day. Twenty "
                  "weavers share one room worth 100s and make 400 yards between them. How much "
                  "of the room's value is in each yard, alone and together?",
             "a": ["6d alone, 3d together", "6d both ways", "3d alone, 6d together",
                   "1/2 d alone, 1/4 d together"],
             "c": 0,
             "why": "Alone, `10s / 20 = 1/2 s`, which is 6d. Together, `100s / 400 = 1/4 s`, "
                    "which is 3d. The shared room is worth more in all and gives less to each "
                    "yard. The last option reads the shillings as pence."},
            {"q": "On Marx's account, why does the extra product of co-operation cost the "
                  "capitalist nothing?",
             "a": ["He pays for each worker's labour-power separately, not for their "
                   "combination",
                   "Co-operating workers accept lower wages in return for company",
                   "The extra product is used up in supervision",
                   "Co-operation adds no use-values, only value"],
             "c": 0,
             "why": "The contract is with each worker for that worker's labour-power at its "
                    "value; the combined power arises only once they work together, under the "
                    "capitalist. Marx assumes wages at value, so no lower wage is involved. "
                    "Supervision is a cost he discusses, not where the product goes. And the "
                    "chapter's claim is that co-operation yields more use-values, which is the "
                    "reverse of the last option."},
        ],
        "mistakes": [
            ("Thinking co-operation's extra product is paid for because each worker is paid in full",
             "Each worker is paid in full for his own labour-power, and that is the point: "
             "the capitalist &ldquo;does not pay for the combined labour-power of the "
             "hundred&rdquo;. In the masons preset the wage bill is twelve separate "
             "labour-powers whether or not they pass stones to one another, while the "
             "constant capital in each piece falls from 10d to `5/6` of a penny and the "
             "combined day is 144 hours. Nothing in the wage moves with either figure."),
            ("Reading the shared means of production as worth less",
             "A workshop for twelve costs more than a workshop for one. What falls is the "
             "value it passes to each unit, because the value it gives up is spread over more "
             "product. In the workshop preset 60s is six times one worker's 10s and still "
             "halves the constant capital per piece."),
            ("Treating the direction of labour as only a technical function",
             "Marx grants that any combined labour needs direction, as an orchestra needs a "
             "conductor. His claim is that under capital the directing is also the "
             "supervision of an antagonism, and that the capitalist directs because he owns "
             "the capital, not the other way round. Those who see management as a productive "
             "service paid at its price dispute exactly this."),
        ],
        "standard": (
            "Finish when you can compute what shared means of production save.",
            "Given workers, their output, the means of production each would need alone and "
            "those they share, compute the constant capital per unit both ways and the "
            "combined working day, and state which of them the wage bill pays for."
        ),
        "note": (
            "The lab computes only the economy of means of production used in common. The "
            "larger claim, that a combined day makes more use-values than the same hours "
            "apart, is not computed: Marx gives no figure for it, and output per worker is an "
            "input here, the same alone and together. The shillings and outputs are "
            "illustrative; the twelve masons, the 144 hours and the hundred harvesters are "
            "Marx's."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 1, l. 2790-2792 (unequal periods; four founders and two
    # breakers to one rubber; a fixed mathematical ratio); l. 2841 (the detail
    # labourer produces no commodities; the iron law of proportionality);
    # l. 2742 (20 needlemakers); l. 2744 (a productive mechanism whose parts are
    # human beings); l. 2788 (a given result in a given time); l. 2798 (the
    # "hole"); l. 2843 (one immense factory); l. 2837 (Ferguson's Helots);
    # l. 2867 (a crippled monstrosity); l. 2875-2877 (Smith on the detail
    # labourer); l. 2889 (a refined and civilised method of exploitation);
    # l. 2814-2816 (a hierarchy of labour-powers; in both cases the value of
    # labour-power falls); l. 7524 (footnote 50, Babbage on purchasing the
    # precise quantity of skill).
    {
        "slug": "division-of-labour-and-manufacture",
        "title": "Division of Labour and Manufacture",
        "module": "Chapter 14 · Division of Labour and Manufacture",
        "one_line": "Manufacture splits a handicraft into detail operations and fixes how many workers each one needs, which no market does for society.",
        "summary": (
            "Manufacture is co-operation based on dividing a craft into detail operations, "
            "each done for life by one kind of worker. Because the operations run at "
            "different speeds, the workshop needs them in fixed proportions. Compute those "
            "proportions and the smallest workshop that keeps everyone busy, from Marx's "
            "type-founders, and see why he insists that this division is a different kind of "
            "thing from the division of labour in society."
        ),
        "key": [
            "a craft split into detail operations",
            "workers per step ∝ 1 / its rate",
            "type: founders 4, breakers 2, rubbers 1",
            "the workshop's plan is fixed in advance",
            "society's proportions are set by sale",
        ],
        "key_label": "The collective labourer",
        "concepts_intro": (
            "Chapter 14 runs from the middle of the sixteenth century to the eve of the factory. "
            "Three ideas carry its argument."
        ),
        "concepts": [
            ("The detail labourer",
             "A worker who performs one operation all his life becomes faster at it, and "
             "his tools are reshaped to suit it. The craft is gone; the operation remains."),
            ("The collective labourer",
             "The workshop as a whole is a mechanism whose parts are people. Because each "
             "operation yields a different quantity in an hour, the parts must stand in a "
             "fixed numerical ratio."),
            ("Two divisions of labour",
             "In society the producers are linked by buying and selling each other's "
             "products. In the workshop they are linked by selling their labour-power to "
             "one capitalist, and their product becomes a commodity only when it is "
             "finished."),
        ],
        "read_title": "A fixed mathematical ratio",
        "read_intro": (
            "The passage comes from the third section, on manufacture as a whole. It is the "
            "one place in the chapter where Marx gives the arithmetic."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 14, §3.</strong> &ldquo;Different operations "
                  "take, however, unequal periods, and yield therefore, in equal times unequal "
                  "quantities of fractional products. If, therefore, the same labourer has, day "
                  "after day, to perform the same operation, there must be a different number of "
                  "labourers for each operation; for instance, in type manufacture, there are "
                  "four founders and two breakers to one rubber: the founder casts 2,000 type an "
                  "hour, the breaker breaks up 4,000, and the rubber polishes 8,000.&rdquo;"),
            ("p", "Manufacture, Marx says, arose in two ways. A carriage used to be made by "
                  "independent wheelwrights, harness-makers, upholsterers and gilders; gathered "
                  "under one roof, each slowly loses his old craft and becomes a carriage "
                  "specialist. Or the reverse: a capitalist hires many needle-makers who each "
                  "make whole needles, until a rush order makes him split the work, and in "
                  "England twenty needlemakers came to stand side by side, &ldquo;each performing "
                  "one alone of those 20 operations&rdquo;. Either way the end is the same: "
                  "&ldquo;a productive mechanism whose parts are human beings&rdquo;."),
            ("p", "Why is the detail worker faster? He no longer changes place or tool, so the "
                  "gaps in his day close up. A lifetime on one motion teaches him the least "
                  "effort it needs, and the trade's tricks are handed down. His tools are "
                  "reshaped for his one task: Birmingham, Marx notes, made 500 kinds of hammer. "
                  "All of this is still handicraft. Each operation is done by hand and depends "
                  "on the strength and skill of the person doing it."),
            ("p", "There is a second gain, and the economists of the day saw it before Marx did. "
                  "Charles Babbage, the Cambridge mathematician who designed a calculating "
                  "engine and in 1832 wrote <em>On the Economy of Machinery and "
                  "Manufactures</em>, put it exactly: a master who divides the work into "
                  "processes needing different degrees of skill or force &ldquo;can purchase "
                  "exactly that precise quantity of both which is necessary for each "
                  "process&rdquo;, where a single craftsman must be paid at the rate of the "
                  "hardest operation for all of them. Marx quotes the passage and takes the "
                  "point whole. Manufacture &ldquo;developes a hierarchy of labour-powers, to "
                  "which there corresponds a scale of wages&rdquo;; it creates a class of "
                  "unskilled workers the crafts never had, for whom the cost of apprenticeship "
                  "vanishes, and for the skilled it shrinks. &ldquo;In both cases the value of "
                  "labour-power falls.&rdquo; That is the sense in which manufacture, like "
                  "co-operation, is a method of relative surplus value: not only more pieces "
                  "an hour, but cheaper labour-power for each piece. The lab does not compute "
                  "this; its workers all stand at one rate and one wage, and the hierarchy is "
                  "stated here only."),
            ("p", "Now read the passage again. Casting is slow, breaking twice as fast, "
                  "polishing four times as fast. If one founder fed one breaker, the breaker "
                  "would stand idle half the time. The workshop balances only when every step "
                  "turns out the same number of pieces an hour, so the number of workers at a "
                  "step must be inversely proportional to its rate. Four founders at 2,000, two "
                  "breakers at 4,000 and one rubber at 8,000 each make 8,000 an hour. That is "
                  "the &ldquo;fixed mathematical relation or ratio&rdquo; Marx means, and the "
                  "lab computes it."),
            ("p", "The ratio has a consequence for the size of the business. Seven workers are "
                  "the smallest type workshop with nobody idle; to grow, the workshop must add "
                  "whole multiples of that group. So the minimum capital a manufacturer needs "
                  "keeps rising. Marx's glass-house shows the other shape the rule can take: "
                  "at each mouth of the furnace works &ldquo;the hole&rdquo;, five men, a "
                  "bottlemaker, a blower, a gatherer, a putter-up and a taker-in, who can work "
                  "only as a group of five."),
            ("p", "Is this the same thing as the division of labour in society, only on a "
                  "smaller scale? Adam Smith thought the difference was merely in the eye of the "
                  "observer, who can see a whole workshop at a glance but not the cattle-breeder, "
                  "tanner and shoemaker spread across a country. Marx answers in the fourth "
                  "section:"),
            ("p", "<strong>Volume I, Chapter 14, §4.</strong> &ldquo;While within the workshop, "
                  "the iron law of proportionality subjects definite numbers of workmen to "
                  "definite functions, in the society outside the workshop, chance and caprice "
                  "have full play in distributing the producers and their means of production "
                  "among the various branches of industry.&rdquo;"),
            ("p", "The tanner sells leather; the shoemaker buys it. What binds them is that "
                  "their products are commodities. In the workshop the founder sells nothing: "
                  "&ldquo;the detail labourer produces no commodities&rdquo;. What binds him to "
                  "the breaker is that both sold their labour-power to the same capitalist, who "
                  "fixes their proportions in advance. Society's proportions are found only "
                  "afterwards, in the swings of market prices. Marx then turns to the people who "
                  "praise the first and denounce any attempt at the second: their "
                  "worst charge against planning society is that it would &ldquo;turn all society "
                  "into one immense factory&rdquo;."),
            ("def", ("Manufacture",
                     "Co-operation based on the division of a handicraft into detail operations, "
                     "each performed by specialised workers with specialised tools, in "
                     "proportions fixed by the rates of the operations. Marx dates its period "
                     "from the middle of the sixteenth century to the last third of the "
                     "eighteenth.")),
            ("p", "The lab takes each step's rate per worker and finds the smallest whole "
                  "numbers of workers that balance them. For Marx's type-founding the type "
                  "preset prints 4, 2 and 1, seven in all. The pins preset is three illustrative "
                  "steps, drawing at 3,000 "
                  "an hour, cutting at 2,000 and pointing at 1,200, and the smallest balanced "
                  "shop is 2, 3 and 5 workers, ten in all: Smith's famous pin workshop also had "
                  "ten men, though Smith gives no rates for its steps. The bottle preset, the "
                  "glass-house hole, is five steps at one pace, so one of each, five in all. "
                  "The better-mould preset gives the founders a mould casting 4,000 an hour, "
                  "and the type shop shrinks to 2, 2 and 1, five in all: the ratio "
                  "is a fact about the technique, not about the people."),
            ("p", "The price, Marx says, is paid by the worker. Manufacture &ldquo;converts the "
                  "labourer into a crippled monstrosity&rdquo;, and he lets the economists say "
                  "it themselves. Smith wrote that a man who spends his life on a few simple "
                  "operations &ldquo;generally becomes as stupid and ignorant as it is possible "
                  "for a human creature to become&rdquo;, and proposed schooling by the state "
                  "against it; Adam Ferguson, whom Marx calls Smith's master, exclaimed, &ldquo;We make a nation of "
                  "Helots, and have no free citizens.&rdquo; The same chapter that measures the "
                  "gain in output measures this loss, and Marx calls manufacture both a "
                  "necessary phase of development and &ldquo;a refined and civilised method of "
                  "exploitation&rdquo;."),
            ("p", "Manufacture's limit was its own basis: every operation still had to be done "
                  "by a human hand. Its most finished product was the workshop that made "
                  "machines. The next lesson, “Machinery and the Value It Transfers”, asks what "
                  "a machine adds to the value of what it makes."),
        ],
        "lab": ("capkit", {
            "mode": "machine",
            "view": "detail",
            "money_unit": "s",
            "qty_unit": "pieces",
            "preset": "type",
            "presets": [
                {"id": "type", "label": "Marx's type-founding: 2,000, 4,000 and 8,000 an hour",
                 "steps": [{"name": "founders", "rate": 2000},
                           {"name": "breakers", "rate": 4000},
                           {"name": "rubbers", "rate": 8000}],
                 "expect": {"maWorkers": "founders 4, breakers 2, rubbers 1", "maMinimum": "7"}},
                {"id": "pins", "label": "A pin workshop at illustrative rates (Smith gives none)",
                 "steps": [{"name": "drawers", "rate": 3000},
                           {"name": "cutters", "rate": 2000},
                           {"name": "pointers", "rate": 1200}],
                 "expect": {"maWorkers": "drawers 2, cutters 3, pointers 5", "maMinimum": "10"}},
                {"id": "bottle", "label": "Marx's glass-house 'hole': five steps at one pace",
                 "steps": [{"name": "gatherers", "rate": 60},
                           {"name": "blowers", "rate": 60},
                           {"name": "bottlemakers", "rate": 60},
                           {"name": "putters-up", "rate": 60},
                           {"name": "takers-in", "rate": 60}],
                 "expect": {"maWorkers": "gatherers 1, blowers 1, bottlemakers 1, putters-up 1, takers-in 1", "maMinimum": "5"}},
                {"id": "better-mould", "label": "Type-founding with founders casting 4,000 an hour",
                 "steps": [{"name": "founders", "rate": 4000},
                           {"name": "breakers", "rate": 4000},
                           {"name": "rubbers", "rate": 8000}],
                 "expect": {"maWorkers": "founders 2, breakers 2, rubbers 1", "maMinimum": "5"}},
            ],
            "panel_title": "Balancing the detail operations",
            "panel_intro": (
                "Each step is a detail operation and the pieces one worker at it turns out in "
                "an hour. The lab finds the smallest whole numbers of workers that make every "
                "step turn out the same number of pieces an hour."
            ),
        }),
        "steps_title": "Balancing a manufacture",
        "steps_intro": "Four steps for any sequence of detail operations.",
        "steps": [
            ("List the rates",
             "For each operation write the number of pieces one worker turns out in an "
             "hour."),
            ("Invert them",
             "The workers a step needs are proportional to one over its rate: a step twice "
             "as fast needs half as many."),
            ("Clear to whole numbers",
             "Multiply the inverses by the smallest number that makes them all whole, then "
             "divide by any common factor. These are the workers per step."),
            ("Add and check",
             "Their sum is the smallest workshop with nobody idle. Multiply each step's "
             "workers by its rate: every product must be the same hourly output."),
        ],
        "worked": {
            "title": "Founders, breakers and rubbers",
            "intro": [
                "Marx's figures: a founder casts 2,000 type an hour, a breaker breaks up "
                "4,000, a rubber polishes 8,000. You want the smallest workshop in which "
                "nobody waits.",
            ],
            "lines": [
                "inverses:  1/2000, 1/4000, 1/8000",
                "times 8000:  4, 2, 1",
                "workers:  4 + 2 + 1 = 7",
                "check:  4·2000 = 2·4000 = 1·8000 = 8000 an hour",
            ],
            "after": [
                "Four founders and two breakers to one rubber, exactly as Marx reports. A "
                "larger shop is 14, 21, 28 workers, never 8 or 9, which is why the minimum "
                "capital of a manufacture rises with every gain from dividing the work.",
            ],
        },
        "quiz_title": "Proportions in the workshop",
        "quiz": [
            {"q": "Three detail operations turn out 600, 300 and 200 pieces an hour per worker. "
                  "What is the smallest balanced workshop?",
             "a": ["1, 2 and 3 workers, 6 in all", "3, 2 and 1 workers, 6 in all",
                   "1, 1 and 1 workers, 3 in all", "2, 3 and 6 workers, 11 in all"],
             "c": 0,
             "why": "Workers are proportional to one over the rate: `1/600, 1/300, 1/200` times "
                    "600 is 1, 2 and 3, and each step then makes 600 an hour. Reversing the "
                    "order gives the fastest step the most workers. One of each leaves the "
                    "fast workers idle, and 2, 3, 6 does not balance."},
            {"q": "In Marx's type workshop the founders get a mould that casts 4,000 an hour; "
                  "breakers and rubbers are unchanged. How many workers does the smallest "
                  "balanced workshop need now?",
             "a": ["5", "7", "4", "3"],
             "c": 0,
             "why": "The rates are 4,000, 4,000 and 8,000, so the workers are 2, 2 and 1, five in "
                    "all. Seven was the figure before the new mould. Four and three leave some "
                    "step turning out less than the others."},
            {"q": "On Marx's account, what links the tanner to the shoemaker that does not link "
                  "the founder to the breaker in a type workshop?",
             "a": ["The tanner's product is a commodity the shoemaker buys",
                   "The tanner and the shoemaker work for the same capitalist",
                   "The tanner and the shoemaker work at fixed rates",
                   "The tanner and the shoemaker work in the same place"],
             "c": 0,
             "why": "Between independent trades the bond is the sale of products; inside the "
                    "workshop the detail worker sells no product, only his labour-power to the "
                    "one capitalist. Working for the same capitalist and in the same place "
                    "describe the workshop, not the trades. Fixed rates belong to the "
                    "workshop's plan; society's proportions are found through prices."},
        ],
        "mistakes": [
            ("Treating the workshop's division of labour as society's division in miniature",
             "Smith thought the difference was only how much an observer can see. Marx's "
             "answer is that the two are bound differently: in the workshop by one plan, so "
             "the lab can compute 4, 2 and 1 founders, breakers and rubbers from three rates; "
             "in society by the sale of commodities, where no input could compute how many "
             "tanners there will be, because the proportion is found afterwards, through "
             "prices."),
            ("Giving the fastest step the most workers",
             "Workers per step are proportional to one over its rate, so the slow step needs "
             "the most hands. In the type preset the founders, at 2,000 an hour, are four; "
             "the rubbers, at 8,000, are one."),
            ("Thinking a manufacture can grow one worker at a time",
             "Once the proportion is fixed, the workshop can grow only by whole multiples of "
             "its smallest balanced group: 7, 14, 21 for type. That is why Marx says the "
             "minimum capital in manufacture keeps rising."),
        ],
        "standard": (
            "Finish when you can balance a set of detail operations.",
            "Given the hourly rate per worker of each detail operation, compute the workers "
            "each step needs and the smallest workshop with nobody idle, and name the bond "
            "that fixes those proportions in the workshop and the one that sets them in "
            "society."
        ),
        "note": (
            "The lab assumes every worker at a step works at exactly its rate, which is "
            "manufacture's own assumption: Marx says it is &ldquo;based on the assumption "
            "that a given result will be obtained in a given time&rdquo;. The type rates and "
            "the five-man hole are Marx's; the hole's pace and the pin workshop's three rates "
            "are illustrative, and Smith's pin factory gives only a total, about 48,000 pins "
            "a day from ten men."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 1, l. 2993 (machinery creates no new value); l. 3019 (the
    # £3000 machine and the 150 men); l. 3021-3023 (the capitalist pays only
    # for labour-power; not the labour employed but the labour paid for);
    # l. 2915 (Mill's question; a means for producing surplus-value);
    # l. 2995-2997 (gratuitously, like the forces of nature); l. 3025 (the
    # "wretch" who breaks stones).
    {
        "slug": "machinery-and-the-value-it-transfers",
        "title": "Machinery and the Value It Transfers",
        "module": "Chapter 15 · Machinery and Modern Industry",
        "one_line": "A machine adds to the product only the value it loses, and a capitalist adopts it only if it costs less than the wages it saves.",
        "summary": (
            "Machinery, like every other part of constant capital, creates no new value; it "
            "passes its own value into the product bit by bit. Compute the value a machine "
            "adds to each unit, then apply two tests for adopting it: society's, which "
            "compares its cost with the labour it saves, and the capitalist's, which compares "
            "it with the wages it saves. Marx's £3,000 machine passes the first and only "
            "breaks even on the second."
        ),
        "key": [
            "a machine creates no new value",
            "per unit = machine value / lifetime output",
            "society: cost < labour saved",
            "capitalist: cost < wages saved",
            "wages are less than the labour",
        ],
        "key_label": "What a machine is worth to whom",
        "concepts_intro": (
            "Chapter 15 is the longest in Volume I, and its first two sections lay down "
            "what the rest depends on: what a machine is, and what it adds."
        ),
        "concepts": [
            ("The machine",
             "A mechanism that, once set in motion, performs with its tools the operations a "
             "worker used to perform with similar tools. What revolutionises production is "
             "the working machine, not the engine that drives it."),
            ("Value transferred",
             "A machine enters the labour process whole but the process of making value only "
             "piecemeal: it gives up, on average, what it loses by wear. The longer its life "
             "and the larger its output, the less it adds to each unit."),
            ("Two limits to its use",
             "For society, a machine is worth using if it costs less labour than it saves. "
             "For the capitalist, who pays for labour-power and not for labour, it is worth "
             "using only if it costs less than the wages it saves."),
        ],
        "read_title": "Machinery adds only what it loses",
        "read_intro": (
            "The second section opens by setting machines beside the other free gifts of "
            "production, co-operation and the forces of nature, and then marks the "
            "difference: a machine has a value."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 15, §2.</strong> &ldquo;Machinery, like every "
                  "other component of constant capital, creates no new value, but yields up its "
                  "own value to the product that it serves to beget. In so far as the machine "
                  "has value, and, in consequence, parts with value to the product, it forms an "
                  "element in the value of that product. Instead of being cheapened, the product "
                  "is made dearer in proportion to the value of the machine.&rdquo;"),
            ("p", "The chapter begins with a sentence from John Stuart Mill: &ldquo;It is "
                  "questionable if all the mechanical inventions yet made have lighted the day's "
                  "toil of any human being.&rdquo; Marx's reply is that lightening toil was never "
                  "the aim. Machinery is &ldquo;a means for producing surplus-value&rdquo;, by "
                  "cheapening commodities and so shortening the part of the day a worker works "
                  "for himself."),
            ("p", "What is a machine? Not, Marx says, a tool moved by something other than a "
                  "person: on that test an ox-plough would be a machine and a loom worked by "
                  "hand a tool. A machine is a mechanism that takes the tool out of the worker's "
                  "hand and works it itself, and so escapes the limit of the human body. A "
                  "spinner has two hands; the jenny began with 12 to 18 spindles. The steam "
                  "engine came afterwards, because the machines needed it. And at the end of "
                  "the first section Modern Industry has to make its own machines by machine, "
                  "since manufacture's hand-workers could not make them large or exact "
                  "enough."),
            ("p", "Now the passage. A machine is constant capital, and the rule of “Constant "
                  "Capital and Variable Capital” in the previous course holds for it: it passes "
                  "on the value it loses and creates none. It enters the labour process whole "
                  "but the product's value only bit by bit, and the gap between what it is worth "
                  "and what it adds in a day is far larger than for a tool, because it lasts "
                  "longer and makes so much more. Beyond the wear it passes on, it works "
                  "&ldquo;gratuitously, just like the forces furnished by nature&rdquo;."),
            ("p", "So the first figure is simple: the machine's value divided by everything it "
                  "will make in its life. Mr. Baynes of Blackburn, whom Marx quotes, reckoned "
                  "that one horse-power drove 450 self-acting mule spindles, and that two and a "
                  "half workers on them spun in a week a quantity of yarn a hand-spinner would "
                  "need 27,000 hours to spin; the machine's share in each pound of yarn was tiny. "
                  "The productiveness of a machine, Marx concludes, is measured by the human "
                  "labour-power it replaces."),
            ("p", "Then the turn that gives the section its edge. Suppose a machine costs £3,000, "
                  "as much as a year's wages of the 150 men it displaces. Does it save as much "
                  "labour as it costs? No:"),
            ("p", "<strong>Volume I, Chapter 15, §2.</strong> &ldquo;Suppose, then, a machine "
                  "cost as much as the wages for a year of the 150 men it displaces, say £3000; "
                  "this £3000 is by no means the expression in money of the labour added to the "
                  "object produced by these 150 men before the introduction of the machine, but "
                  "only of that portion of their year's labour which was expended for "
                  "themselves and represented by their wages.&rdquo;"),
            ("p", "At a rate of surplus value of 100%, the 150 men added £6,000 of value in a "
                  "year, and were paid £3,000 of it. The £3,000 machine embodies all the labour "
                  "that made it. So by society's measure it saves twice what it costs. But the "
                  "capitalist does not pay for the labour, only for the labour-power, so "
                  "&ldquo;the limit to his using a machine is fixed by the difference between "
                  "the value of the machine and the value of the labour-power replaced by "
                  "it&rdquo;. At £3,000 against £3,000 of wages, the machine saves him "
                  "nothing."),
            ("def", ("The capitalist's limit to machinery",
                     "A capitalist adopts a machine only if its value is less than the value of "
                     "the labour-power it replaces. Society's limit is wider: the machine need "
                     "only cost less labour than the labour it replaces, wages and surplus "
                     "together.")),
            ("p", "The lab computes the value per unit and both verdicts. In the marx preset the "
                  "£3,000 machine adds `£3/10` to each yard, and because the test is strict, a "
                  "machine costing exactly the wages it displaces is not adopted on the "
                  "capitalist's test: it saves him nothing. Switch the test to society's and the "
                  "same machine is adopted, because it costs £3,000 against £6,000 of labour. "
                  "The society preset is a £5,000 machine, `£1/2` a yard, that saves the same "
                  "£6,000 of labour and still loses on the capitalist's test. The cheap-labour "
                  "preset lowers the wages to £2,000, and even the £3,000 machine is not "
                  "adopted; the dear-labour preset raises them to £4,500, and it is."),
            ("p", "This, Marx says, is why machines were invented in England to be used only "
                  "in North America: the gap between a machine's value and the labour-power it "
                  "replaces differs from country to country, and the same machine can pass the "
                  "capitalist's test where labour-power is dear and fail it where it is cheap. "
                  "It is why a Yankee stone-breaking "
                  "machine went unused in England, where the &ldquo;wretch&rdquo; who broke "
                  "stones was paid for so little of his labour, and why women still sometimes "
                  "hauled canal boats instead of horses. The capitalist's profit comes, in "
                  "Marx's phrase, &ldquo;not from a diminution of the labour employed, but of the "
                  "labour paid for&rdquo;."),
            ("p", "The rule that a firm adopts a technique when it lowers costs at going wages "
                  "is common ground; any textbook says that cheap labour delays mechanisation. "
                  "What is Marx's is the second measure, the labour a machine saves, and the "
                  "claim that the gap between the two measures is unpaid labour. An economist "
                  "who prices labour by its marginal product would say the wage is the value of "
                  "what the worker adds, and that the gap is not there to find."),
            ("p", "A machine that pays for itself out of saved wages also changes who works and "
                  "how hard. The next lesson, “Machinery and the Intensity of Labour”, follows "
                  "it into the factory once the law has shortened the day."),
        ],
        "lab": ("capkit", {
            "mode": "machine",
            "view": "adopt",
            "money_unit": "£",
            "qty_unit": "yards",
            "test": "capitalist",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's £3,000 machine displacing 150 men's £3,000 of wages",
                 "machine_value": 3000, "machine_life_units": 10000, "wages_displaced": 3000,
                 "labour_saved_value": 6000, "expect": {"maPerUnit": "£3/10", "maVerdict": "not adopted (the capitalist’s test)"}},
                {"id": "society", "label": "A £5,000 machine saving the same £6,000 of labour",
                 "machine_value": 5000, "machine_life_units": 10000, "wages_displaced": 3000,
                 "labour_saved_value": 6000, "expect": {"maPerUnit": "£1/2", "maVerdict": "not adopted (the capitalist’s test)"}},
                {"id": "cheap-labour", "label": "The £3,000 machine where the 150 earn £2,000",
                 "machine_value": 3000, "machine_life_units": 10000, "wages_displaced": 2000,
                 "labour_saved_value": 6000, "expect": {"maPerUnit": "£3/10", "maVerdict": "not adopted (the capitalist’s test)"}},
                {"id": "dear-labour", "label": "The £3,000 machine where the 150 earn £4,500",
                 "machine_value": 3000, "machine_life_units": 10000, "wages_displaced": 4500,
                 "labour_saved_value": 6000, "expect": {"maPerUnit": "£3/10", "maVerdict": "adopted (the capitalist’s test)"}},
            ],
            "panel_title": "Two tests for one machine",
            "panel_intro": (
                "The machine's value over the yards it makes in its life is what it adds to "
                "each yard. The test compares its value with the wages it displaces "
                "(the capitalist's) or with the labour it saves (society's); switch between "
                "them on each preset. The 10,000 yards of life is illustrative."
            ),
        }),
        "steps_title": "Pricing a machine and testing it",
        "steps_intro": "Four steps for any machine that replaces workers.",
        "steps": [
            ("Spread its value",
             "Divide the machine's value by the units it makes in its working life. That is "
             "what it adds to each unit; it adds no more."),
            ("Value the labour it saves",
             "Take the labour the displaced workers performed, necessary and surplus "
             "together. At a rate of surplus value of 100% it is twice their wages."),
            ("Apply society's test",
             "The machine saves labour if its value is less than the labour it replaces."),
            ("Apply the capitalist's test",
             "He adopts it only if its value is less than the wages of the workers it "
             "replaces. Between the two tests lies the unpaid labour of those workers."),
        ],
        "worked": {
            "title": "Marx's £3,000 machine",
            "intro": [
                "A machine costs £3,000, a year's wages of the 150 men it displaces. Their rate "
                "of surplus value is 100%, and the machine will make 10,000 yards in its life. "
                "You want its value per yard and the verdict of each test.",
            ],
            "lines": [
                "per yard:  £3000 / 10000 = £3/10",
                "labour saved:  £3000 · (1 + 1) = £6000",
                "society:  £3000 < £6000, adopted",
                "capitalist:  £3000 < £3000 is false, no saving",
            ],
            "after": [
                "The machine saves £3,000 of labour that nobody was paid for, and that saving "
                "is invisible to the capitalist's test. Lower the wages and the gap between the "
                "two verdicts widens.",
            ],
        },
        "quiz_title": "Value transferred and the limit to machinery",
        "quiz": [
            {"q": "A machine worth £1,200 will make 6,000 units in its life. How much value "
                  "does it add to each unit?",
             "a": ["£1/5", "£5", "£1,200", "Nothing, since machines create no value"],
             "c": 0,
             "why": "It passes on its own value over its life: `£1200 / 6000 = £1/5` a unit. "
                    "Five pounds inverts the division, and £1,200 is the whole machine. It "
                    "creates no new value, but it does transfer its own."},
            {"q": "A machine costs £4,000. It replaces workers paid £3,500 a year, whose labour "
                  "at 100% surplus value amounts to £7,000. On Marx's account, what happens?",
             "a": ["It saves labour, and the capitalist does not adopt it",
                   "It saves labour, and the capitalist adopts it",
                   "It saves no labour, and the capitalist does not adopt it",
                   "It saves no labour, and the capitalist adopts it"],
             "c": 0,
             "why": "£4,000 is less than the £7,000 of labour it replaces, so it saves labour, "
                    "but more than the £3,500 of wages, so the capitalist's test fails. The "
                    "other three each get one of the two comparisons wrong."},
            {"q": "Why, on Marx's account, were some machines invented in England and used only "
                  "in North America?",
             "a": ["Wages in North America were higher, so the machines saved more in wages",
                   "The machines saved more labour in North America",
                   "Machines cost less to build in North America",
                   "Surplus value was higher in North America"],
             "c": 0,
             "why": "The capitalist's limit is the wages a machine displaces, and higher wages "
                    "widen it. The labour saved is the same machine's work in either country. "
                    "Marx does not say the machines were cheaper there, and a higher rate of "
                    "surplus value with the same labour would mean lower wages, which narrows "
                    "the limit."},
            {"q": "On Chapter 15's definitions, what does a machine add to the value of the "
                  "product?",
             "a": ["The value it loses by wear, and no new value",
                   "Its whole value at once, in the first period",
                   "New value in proportion to the labour it replaces",
                   "Nothing, because it works gratuitously"],
             "c": 0,
             "why": "It enters the value of the product only piecemeal, by its average wear. It "
                    "does not pass on its whole value at once, and it creates no new value; "
                    "only labour does. It works gratuitously beyond the value it transfers, "
                    "not instead of transferring it."},
        ],
        "mistakes": [
            ("Thinking a machine is used whenever it saves labour",
             "That is society's test. The capitalist's test is narrower, because he pays for "
             "labour-power, not labour. In the society preset a £5,000 machine saves £6,000 "
             "of labour and is not adopted on the capitalist's test, because it costs more "
             "than the £3,000 of wages it displaces. In the cheap-labour preset even Marx's "
             "£3,000 machine fails, and that is Marx's explanation of why low wages delay "
             "machinery."),
            ("Treating a machine as a source of new value",
             "A machine raises productivity, so each hour of labour makes more product. But "
             "the value it adds is its own, passed on by wear; it creates none. The marx "
             "preset's machine adds `£3/10` to each yard and nothing besides."),
            ("Equating the wages a machine displaces with the labour it saves",
             "The £3,000 of wages is only the part of the 150 men's labour that they did for "
             "themselves. At a rate of surplus value of 100% they performed £6,000 of labour. "
             "The difference is why the same machine can pass one test and fail the other."),
        ],
        "standard": (
            "Finish when you can price a machine per unit and apply both tests.",
            "Given a machine's value, its lifetime output, the wages it displaces and the "
            "labour it saves, compute the value it adds per unit and state whether it passes "
            "society's test and the capitalist's."
        ),
        "note": (
            "The lab spreads a machine's value evenly over its lifetime output; Marx notes "
            "that wear is not exactly proportional to use, and that a machine can lose value "
            "before it wears out when cheaper or better ones appear. Its capitalist's test "
            "compares a year's wages with the machine's whole value, as Marx's example does. "
            "The £3,000 and the 150 men are Marx's; the lifetime output and the other wages "
            "are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 1, l. 3104 (the denser hour; 3 1/3 and 6 2/3 hours; a measure
    # of its intensity); l. 3102 (extension and intensity exclude one another);
    # l. 3037 (spread over the whole family); l. 3068 (perpetuum mobile);
    # l. 3088 (2 against 24 labourers); l. 3110 (Gardner's experiment);
    # l. 3145 (twelve hours compressed into ten); l. 3173 (a living appendage;
    # the lightening of the labour a torture); l. 3157 (Ure, the Pindar of the
    # automatic factory); l. 3315 (Ure on the self-acting mule).
    {
        "slug": "machinery-and-the-worker",
        "title": "Machinery and the Intensity of Labour",
        "module": "Chapter 15 · Machinery and Modern Industry",
        "one_line": "When the law shortens the day, capital makes each hour denser, and a shorter day of more intense labour can yield as much surplus value as a longer one.",
        "summary": (
            "Machinery first lengthens the working day, and the reaction it provokes fixes "
            "the day by law. Capital then turns to intensity: faster machines, more of them "
            "to a worker, fewer pores in the hour. Compute the labour spent and the rate of "
            "surplus value when a 12-hour day becomes 10 hours at a fifth more intensity, as "
            "in Marx's own example, and see why the shorter day need not mean less surplus "
            "value."
        ),
        "key": [
            "labour spent = hours × intensity",
            "necessary time is in normal hours",
            "10 hours at 6/5 = 12 normal hours",
            "a shorter day, the same surplus value",
            "length and intensity exclude each other",
        ],
        "key_label": "A denser hour",
        "concepts_intro": (
            "The third section of Chapter 15 traces three effects of machinery on the "
            "worker. This lesson computes the third and states the other two."
        ),
        "concepts": [
            ("Supplementary labour-power",
             "Machinery makes muscular strength unnecessary, so capital hires women and "
             "children, and the value of labour-power, once the cost of keeping a family, is "
             "spread over the whole family."),
            ("The lengthened day",
             "A machine idle is capital idle, and a machine can be made obsolete by a better "
             "one before it wears out. Both push towards a longer day, and the reaction "
             "against it is the legal limit."),
            ("Intensity",
             "Once the day is fixed, more labour is pressed into each hour. A denser hour "
             "counts as more labour, so intensity is a measure of labour alongside its "
             "duration."),
        ],
        "read_title": "The denser hour",
        "read_intro": (
            "The passage is from section 3(c), just after the Ten Hours' Act has been "
            "mentioned. It does its own arithmetic, in hours."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 15, §3(c).</strong> &ldquo;The denser hour of the "
                  "ten hours' working-day contains more labour, i.e., expended labour-power, "
                  "than the more porous hour of the twelve hours' working-day. The product "
                  "therefore of one of the former hours has as much or more value than has the "
                  "product of 1 1/5 of the latter hours. Apart from the increased yield of "
                  "relative surplus-value through the heightened productiveness of labour, the "
                  "same mass of value is now produced for the capitalist, say, by 3 1/3 hours of "
                  "surplus labour, and 6 2/3 hours of necessary labour, as was previously "
                  "produced by four hours of surplus labour and eight hours of necessary "
                  "labour.&rdquo;"),
            ("p", "Before the passage, two other effects. Machinery needs no strength, so the "
                  "first labour capital sought for it was that of women and children, and Marx "
                  "spends pages on the child markets of Bethnal Green and the education clauses "
                  "that schooled nobody. His economic point is short. The value of labour-power "
                  "was the cost of keeping a worker and his family; once the whole family works, "
                  "that value is spread, in Marx's words, &ldquo;over his whole family&rdquo;, and four people "
                  "now give surplus labour where one did. That is stated here and not computed."),
            ("p", "The second effect is the long day. A machine is &ldquo;an industrial "
                  "perpetuum mobile&rdquo; stopped only by the bodies of the people who tend "
                  "it. The longer it runs each day, the sooner its value comes back, and the "
                  "less it risks being made obsolete by a cheaper model first. Marx quotes the "
                  "cotton master Ashworth telling Nassau Senior that a labourer who lays down "
                  "his spade idles eighteenpence of capital, but one who leaves the mill idles "
                  "£100,000. Behind this lies a contradiction: machinery raises the rate of "
                  "surplus value by cutting the number of workers, and &ldquo;It is impossible, "
                  "for instance, to squeeze as much surplus-value out of 2 as out of 24 "
                  "labourers.&rdquo; Lengthening the day is how capital tries to make up the "
                  "lost numbers."),
            ("p", "The long day provoked the reaction that “The Struggle for a Normal Working "
                  "Day” of the previous course described: a legal limit, twelve hours from 1833 "
                  "and ten from 1847. From then on, Marx says, &ldquo;a point must inevitably be "
                  "reached, where extension of the working day and intensity of the labour "
                  "mutually exclude one another&rdquo;. With the length fixed, capital turned to "
                  "the other dimension."),
            ("p", "Now the passage, line by line. A &ldquo;denser hour&rdquo; has fewer pores: "
                  "fewer moments of rest, more motions, more attention. It &ldquo;contains more "
                  "labour&rdquo;, and so counts for more value. If one hour of the ten-hour day "
                  "holds as much labour as `1 1/5` hours of the twelve-hour day, then ten such "
                  "hours hold as much as twelve. The old day was 8 hours necessary and 4 "
                  "surplus. The new one, in clock time, is `6 2/3` necessary and `3 1/3` "
                  "surplus; in normal hours of labour it is still 8 and 4. The worker's day is "
                  "two hours shorter and the capitalist loses nothing."),
            ("def", ("Intensity of labour",
                     "The quantity of labour-power spent in a given time. A more intense hour "
                     "counts as more than one hour of labour of normal intensity, and creates "
                     "correspondingly more value.")),
            ("p", "How was the hour made denser? First by the worker himself, since a shorter "
                  "day lets him exert more strength in each hour. In 1844 the masters swore that "
                  "their overlookers already saw to it that &ldquo;the hands lost no time&rdquo;. "
                  "Then Robert Gardner cut the hours at his two Preston mills from twelve to "
                  "eleven, and after a year &ldquo;the same amount of product for the same cost "
                  "was received, and the workpeople as a whole earned in eleven hours as much "
                  "wages as they did before in twelve.&rdquo; After that, by machinery: faster "
                  "spindles, and more looms to a weaver. By 1863 a Member of Parliament reported "
                  "that &ldquo;Twelve hours' work, as is evident from the facts adduced, is now "
                  "compressed into less than 10 hours.&rdquo;"),
            ("p", "The lab measures labour in normal hours: the day's length times its "
                  "intensity. Necessary labour is held at Marx's 8 normal hours. In the twelve "
                  "preset twelve hours at normal intensity give 4 hours of surplus labour, a "
                  "rate of 50%. The ten-only preset cuts the day to ten with no change in "
                  "intensity, the case the manufacturers argued from, and surplus labour falls "
                  "to 2 hours, 25%. In the ten-denser preset ten hours at `6/5` intensity spend "
                  "12 normal hours, and the rate is back at 50%. The twelve-denser preset keeps "
                  "twelve hours and raises intensity by a third: 16 normal hours "
                  "and a rate of 100%, which is exactly the combination Marx says cannot last."),
            ("p", "The rest of the chapter goes on to the factory itself, and there Marx argues "
                  "with its great admirer. Andrew Ure, a Glasgow chemist, published <em>The "
                  "Philosophy of Manufactures</em> in 1835, and his case deserves its full "
                  "weight: the automatic factory relieves the worker of the heaviest toil, "
                  "its discipline, which he credits to Arkwright, is the real invention, and "
                  "every improvement that makes a skilled hand unnecessary ends a strike before "
                  "it starts. Of the self-acting mule he wrote that it was &ldquo;A creation "
                  "destined to restore order among the industrious classes&rdquo;, and that "
                  "&ldquo;when capital enlists science into her service, the refractory hand of "
                  "labour will always be taught docility.&rdquo; Marx calls him &ldquo;the "
                  "Pindar of the automatic factory&rdquo; and answers that the lightness is the "
                  "point against him: in section 4 the worker becomes &ldquo;its mere living "
                  "appendage&rdquo;, &ldquo;The lightening of the labour, even, becomes a sort "
                  "of torture&rdquo;, and the overlooker's book of fines replaces the "
                  "slave-driver's lash. In section 5 the worker turns on the machine: the "
                  "ribbon-loom riots of the seventeenth century, the Luddites, until, Marx "
                  "says, workers learned to distinguish machinery from its employment by "
                  "capital. The inspectors who praised the shorter day also reported that the "
                  "new pace was itself injuring health, and Marx predicted it would force a "
                  "further cut in hours."),
            ("p", "Machines make the hour denser and need fewer hands for it. The next lesson, "
                  "“Machinery and the Displaced Worker”, asks what becomes of the hands no "
                  "longer needed, and of the economists' promise that capital would re-employ "
                  "them."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "intensity",
            "money_unit": "hours",
            "preset": "twelve",
            "presets": [
                {"id": "twelve", "label": "Marx's 12-hour day: 8 necessary, normal intensity",
                 "day": 12, "necessary": 8, "intensity": 1, "expect": {"wdLabour": "12 h", "wdSurplus": "4 h", "wdRate": "1/2 = 50%"}},
                {"id": "ten-only", "label": "Cut to 10 hours, intensity unchanged",
                 "day": 10, "necessary": 8, "intensity": 1, "expect": {"wdLabour": "10 h", "wdSurplus": "2 h", "wdRate": "1/4 = 25%"}},
                {"id": "ten-denser", "label": "Marx's 10-hour day at 6/5 the intensity",
                 "day": 10, "necessary": 8, "intensity": "6/5", "expect": {"wdLabour": "12 h", "wdSurplus": "4 h", "wdRate": "1/2 = 50%"}},
                {"id": "twelve-denser", "label": "12 hours at 4/3 the intensity",
                 "day": 12, "necessary": 8, "intensity": "4/3", "expect": {"wdLabour": "16 h", "wdSurplus": "8 h", "wdRate": "1 = 100%"}},
            ],
            "panel_title": "Length and intensity",
            "panel_intro": (
                "Labour spent is the length of the day times its intensity, counted in hours "
                "of normal intensity. Necessary labour is in the same normal hours: the value "
                "of a day's labour-power is held at 8 of them."
            ),
        }),
        "steps_title": "Measuring a day by duration and density",
        "steps_intro": "Four steps for any change in the length or intensity of a day.",
        "steps": [
            ("Convert the day to normal hours",
             "Multiply the length of the day by its intensity. A 10-hour day at `6/5` "
             "intensity is 12 hours of labour of normal intensity."),
            ("Keep necessary labour in the same unit",
             "The value of labour-power is so many normal hours. If intensity rises and "
             "wages do not, it stays where it was."),
            ("Subtract and divide",
             "Surplus labour is the labour spent less the necessary labour; the rate is "
             "surplus over necessary."),
            ("Compare with the old day",
             "Set the result beside the longer, more porous day. Equal labour spent means "
             "equal value and, at the same wage, equal surplus value."),
        ],
        "worked": {
            "title": "Ten denser hours for twelve",
            "intro": [
                "Marx's day: twelve hours, 8 of them necessary. The law cuts it to ten and the "
                "hour becomes a fifth denser. You want the labour spent, the surplus labour and "
                "the rate, and the necessary and surplus parts in clock time.",
            ],
            "lines": [
                "labour spent:  10 h · 6/5 = 12 h",
                "surplus:  12 h − 8 h = 4 h;  rate 4/8 = 50%",
                "necessary in clock time:  8 h / (6/5) = 6 2/3 h",
                "surplus in clock time:  4 h / (6/5) = 3 1/3 h",
            ],
            "after": [
                "These are Marx's `6 2/3` and `3 1/3` hours. The worker gains two hours of his "
                "day and spends as much labour as before in the ten that remain.",
            ],
        },
        "quiz_title": "Duration and density",
        "quiz": [
            {"q": "A 9-hour day is worked at 4/3 the normal intensity. How many hours of "
                  "labour of normal intensity does it contain?",
             "a": ["12 hours", "9 hours", "27/4 hours", "10 1/3 hours"],
             "c": 0,
             "why": "Labour spent is length times intensity, `9 · 4/3 = 12`. Nine hours ignores "
                    "the intensity, `27/4` divides by it instead of multiplying, and `10 1/3` "
                    "adds the intensity to the hours instead of multiplying."},
            {"q": "A day of 12 hours at normal intensity has 8 hours of necessary labour. The "
                  "law cuts it to 10 hours and intensity rises by a fifth; wages are unchanged. "
                  "What is the new rate of surplus value?",
             "a": ["50%", "25%", "20%", "100%"],
             "c": 0,
             "why": "Ten hours at `6/5` are 12 normal hours, of which 8 are necessary, so 4 "
                    "surplus on 8 is 50%, as before the cut. Twenty-five per cent is the shorter "
                    "day with no rise in intensity. Twenty per cent divides 2 by 10, and 100% "
                    "matches no case here."},
            {"q": "What did Robert Gardner's experiment at Preston show, as Marx reports it?",
             "a": ["Eleven hours produced as much as twelve, at the same wages",
                   "Eleven hours produced eleven-twelfths as much as twelve",
                   "Output rose only because the machines were sped up",
                   "Wages fell by a twelfth when the hours were cut"],
             "c": 0,
             "why": "The same product for the same cost came out of eleven hours, and the "
                    "workers earned as much as in twelve. Marx sets aside the departments where "
                    "machine speed rose 2% and reports the weaving department, where nothing in "
                    "the conditions changed, so the gain came from steadier work."},
        ],
        "mistakes": [
            ("Thinking a shorter working day always means less surplus value",
             "It does only if nothing else changes, which is the case the manufacturers "
             "argued from: the ten-only preset gives 2 hours of surplus labour and 25%. Marx's "
             "point is that the shortening itself sets off a rise in intensity. In the "
             "ten-denser preset the same ten hours at `6/5` intensity spend 12 normal hours "
             "and the rate is back at 50%, with 4 hours of surplus labour, exactly as in the "
             "twelve-hour day."),
            ("Measuring labour by the clock alone",
             "Once intensity varies, an hour is not a fixed quantity of labour. Marx adds "
             "&ldquo;a measure of its intensity or of the degree of its condensation&rdquo; "
             "to the measure of its duration, and the lab counts labour in hours of normal "
             "intensity for that reason."),
            ("Assuming any day can be both long and intense",
             "The twelve-denser preset computes 16 normal hours in a twelve-hour day, and the "
             "arithmetic does not object. Marx does: beyond a point length and intensity "
             "&ldquo;mutually exclude one another&rdquo;, and the intensity reached under the "
             "shorter day could not be sustained over a longer one."),
        ],
        "standard": (
            "Finish when you can compute the labour in a day of given length and intensity.",
            "Given the length of a working day, its intensity and the necessary labour in "
            "normal hours, compute the labour spent, the surplus labour and the rate of "
            "surplus value, and compare them with a longer day at normal intensity."
        ),
        "note": (
            "The lab holds the value of labour-power fixed when intensity rises. Marx says a "
            "more intense day wears labour-power out faster, so its value may rise, and a "
            "wage that does not rise with it falls below value. The lab also accepts any "
            "intensity on any length of day, which Marx says is impossible beyond a point. "
            "The 12-hour day, the 8 necessary hours and the `6/5` are Marx's."
        ),
    },
]
