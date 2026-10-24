"""Reproduction of the Social Capital, lessons 1-6 -- Volume II, Part III, Chapters 18-21.

Every quotation is copied from /mnt/project-files/capital-texts/volume-2-kerr.txt
(Untermann's translation of Volume II, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, and the translator's double quotation marks inside a quotation
are printed as single curly quotes. Marx's schemes inside a quotation are
printed as the Kerr text prints them, with its spacing ("4000 c+1000 v");
the lessons' own prose writes them 4,000c + 1,000v, and math runs leave the
thousands ungrouped (4000c), as Kerr does, so that the read-out does not split
them at the comma. Nothing else is changed.

Chapter 20 is two lessons (the three exchanges; fixed capital and money) and
Chapter 21 is two (the hoard; the expanded scheme), as PLAN §B says. Module
names keep Kerr's chapter titles: Chapter 19 is "Former Discussions of the
Subject" and Chapter 21 "Accumulation and Reproduction on an Enlarged Scale".
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 2, l. 3609 (the passage). Inline: l. 3607 (an individual
    # fraction), l. 3609 (purchase by the working class), l. 3627 (commodities
    # which do not represent any capital), l. 3639 (prime promoter), l. 3676
    # (checks are not money), l. 3993-3995 (the two departments, Ch. 20 §2),
    # l. 4419 (Proudhon; the stock company), l. 4150 (homogeneous for both).
    {
        "slug": "the-object-of-the-inquiry",
        "title": "The Object of the Inquiry",
        "module": "Chapter 18 · Introduction",
        "one_line": "Every capital is a fraction of society's capital, and the question of Part III is how a whole year's product replaces the means of production used up and feeds the people who made it.",
        "summary": (
            "Chapter 18 turns from the single capital of Parts I and II to the capital of a whole "
            "society, whose movement includes what workers and capitalists buy to live on. Sort a "
            "society's product by its use into means of production and means of consumption, the "
            "two departments of Chapter 20, and see why a question one firm can leave to the "
            "market is the question this Part has to answer."
        ),
        "key": [
            "social capital = the sum of all capitals",
            "its movement includes wages and s spent",
            "Department I: means of production",
            "Department II: means of consumption",
            "sort by use, not by what the thing is",
        ],
        "key_label": "The question of Part III in five lines",
        "concepts_intro": (
            "Chapter 18 is short and is mostly a statement of the problem. It changes the scale of "
            "the question, and three ideas come with the change."
        ),
        "concepts": [
            ("The individual capital as a fraction",
             "Each capital has a life of its own, but it is a fraction of the aggregate social "
             "capital, as each capitalist is a member of a class. Its turnover is one link in the "
             "movement of the whole."),
            ("Consumption comes into the circuit",
             "A single capital's circuit can stop at the sale: what the buyer does with the yarn is "
             "the buyer's business. The movement of society's capital cannot, because what workers "
             "and capitalists buy to live on is part of what keeps the whole going."),
            ("Two kinds of product",
             "Society's product divides by use: means of production, which enter production again, "
             "and means of consumption, which go into someone's household. Chapter 20 calls them "
             "Department I and Department II, and the lab sorts by that rule."),
        ],
        "read_title": "The passage first, then the change of scale",
        "read_intro": (
            "The passage comes from the chapter's first section, just after Marx has said what the "
            "single capital belongs to. It lists what the new object includes."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 18, §1.</strong> &ldquo;This total process comprises "
                  "both the productive consumption (the immediate process of production) together "
                  "with the metamorphoses (materially considered, exchanges) which promote it, and "
                  "the individual consumption together with its corresponding metamorphoses, or "
                  "exchanges.&rdquo;"),
            ("p", "Up to here the book has followed one capital at a time. Volume I took it into "
                  "the factory and assumed that the capitalist found cotton and labour-power for "
                  "sale and sold his yarn at its value. Parts I and II of this volume followed the "
                  "same single capital through its circuits and its turnovers. Chapter 18 now puts "
                  "it in its place. Every individual capital, Marx writes, &ldquo;forms but an "
                  "individual fraction, endowed with individual life, as it were, of the aggregate "
                  "social capital, just as every individual capitalist is but an individual element "
                  "of the capitalist class&rdquo;. The spinner's circuit is one thread in a cloth."),
            ("p", "Now read the passage phrase by phrase. First, &ldquo;the productive consumption&rdquo; "
                  "is production itself: cotton and spindles used up in making yarn. The "
                  "metamorphoses &ldquo;which promote it&rdquo; are the purchases and sales that "
                  "bring the means of production in and take the product out. Then comes the new "
                  "item, &ldquo;the individual consumption together with its corresponding "
                  "metamorphoses&rdquo;: what a worker does with wages and a capitalist with surplus "
                  "value, the bread, the coat, the coal for the grate. In the single circuit that "
                  "spending happened offstage. In society's movement it is on stage, because, as the "
                  "paragraph goes on, &ldquo;the sale of the commodities implies their purchase by "
                  "the working class&rdquo;."),
            ("p", "This is why the single capital cannot answer the new question. For one firm it "
                  "was enough to assume that its product found a buyer and that what it needed was "
                  "on sale somewhere. For society as a whole those assumptions are the question. "
                  "There is no market outside society to send the problem to: whoever buys the "
                  "product, and whoever sells the means of production that replace what was used "
                  "up, is part of the same whole. And the movement now includes, Marx says, "
                  "&ldquo;the circulation of commodities which do not represent any capital&rdquo;: "
                  "wages being spent on bread, surplus value being spent on a carriage."),
            ("p", "Chapter 20 gives the rule this lesson's lab uses. Society's product falls into "
                  "two great sections. Means of production are &ldquo;commodities having a form in "
                  "which they must, or at least may, pass over into productive consumption&rdquo;; "
                  "means of consumption are commodities that pass &ldquo;into the individual "
                  "consumption of the capitalist and working classes&rdquo;. The rule is by use, not "
                  "by what the thing is. Coal burned under a mill's boiler belongs to Department I. "
                  "The same coal in a kitchen grate belongs to Department II."),
            ("def", ("Department I and Department II",
                     "Department I is the whole of the branches that produce means of production, "
                     "products that will be used up in producing something else. Department II is "
                     "the whole of the branches that produce means of consumption, products that "
                     "pass into the households of workers and capitalists.")),
            ("p", "The lab sorts a product list by that rule. In the two-dept preset a small society "
                  "makes machines worth 300 and coal worth 150 and bakes bread worth 150; of the "
                  "coal, 100 goes to a mill and 50 to kitchens. Sorted by use, Department I holds "
                  "400, the machines and the mill's coal, and Department II holds 200, the bread and "
                  "the kitchens' coal. The misclassified preset files the kitchen coal with the "
                  "rest of the coal, because it is coal: Department I rises to 450 and Department II "
                  "falls to 150, and 50 of supposed means of production now stand where no "
                  "capitalist will buy them to produce with. The marx-totals preset enters Marx's "
                  "own totals from Chapter 20, 6,000 of means of production and 3,000 of means of "
                  "consumption, the figures the rest of this course takes apart."),
            ("p", "One tempting shortcut is to treat society as a single firm, with all the inputs on "
                  "one side and all the output on the other. Marx names Proudhon as one who did, "
                  "looking at society &ldquo;as though a society with a capitalist mode of "
                  "production would lose its specific historical and economic characteristics by "
                  "being taken as a unit&rdquo;. If society is to be treated as one capitalist, he "
                  "says, then it is a stock company, and it &ldquo;shares with many other stock "
                  "companies the peculiarity that every one knows what he puts in, but not what he "
                  "will get out of it&rdquo;."),
            ("p", "The chapter's second section, which Engels' note says belongs later but is placed "
                  "here, is about money. Money capital is the form in which every capital enters the "
                  "scene, &ldquo;the prime promoter, giving the first impetus to the entire "
                  "process&rdquo;. But the money advanced does not fix how much is produced: the same "
                  "workers can be worked longer or harder, and a shorter turnover sets the same "
                  "productive capital going with less money. Long projects, a railway or a canal, "
                  "withdraw labour and means of production for years with nothing in return, and in "
                  "a society that planned its production, Marx adds, workers might receive paper "
                  "checks for their share of consumption: &ldquo;These checks are not money. They do "
                  "not circulate.&rdquo;"),
            ("p", "The two departments are a large simplification, and the standard objection is "
                  "that real products will not stay in one column. Coal, electricity and a lorry "
                  "serve both factories and households, and the input–output tables that Wassily "
                  "Leontief built from the 1930s, which he traced back to Quesnay's Tableau "
                  "Économique, divide an economy into dozens of industries instead of two. Marx "
                  "grants the mixed cases: a considerable part of the instruments and materials of "
                  "labour, he writes in Chapter 20, &ldquo;is homogeneous for both "
                  "departments&rdquo;. The course keeps two departments because the question of "
                  "Part III needs only the one line the lab draws, between what is used up in production and what is used "
                  "up in a household."),
            ("p", "Before Marx, economists had asked this question and, on his account, lost part of "
                  "the answer. The next lesson, “Former Discussions: Quesnay and Smith”, reads "
                  "Chapter 19 and finds where."),
        ],
        "lab": ("capkit", {
            "mode": "schemes",
            "view": "sort",
            "preset": "two-dept",
            "presets": [
                {"id": "two-dept", "label": "Machines, coal for a mill and for kitchens, bread",
                 "products": [{"name": "machines", "use": "production", "value": 300},
                              {"name": "coal for a mill", "use": "production", "value": 100},
                              {"name": "bread", "use": "consumption", "value": 150},
                              {"name": "coal for kitchens", "use": "consumption", "value": 50}],
                 "expect": {"scDeptI": "400: machines, coal for a mill", "scDeptII": "200: bread, coal for kitchens"}},
                {"id": "misclassified", "label": "The kitchens' coal filed as coal, not by its use",
                 "products": [{"name": "machines", "use": "production", "value": 300},
                              {"name": "coal for a mill", "use": "production", "value": 100},
                              {"name": "bread", "use": "consumption", "value": 150},
                              {"name": "coal for kitchens", "use": "production", "value": 50}],
                 "expect": {"scDeptI": "450: machines, coal for a mill, coal for kitchens", "scDeptII": "150: bread"}},
                {"id": "marx-totals", "label": "Marx's totals from Chapter 20: 6,000 and 3,000",
                 "products": [{"name": "means of production", "use": "production", "value": 6000},
                              {"name": "articles of consumption", "use": "consumption", "value": 3000}],
                 "expect": {"scDeptI": "6,000: means of production", "scDeptII": "3,000: articles of consumption"}},
            ],
            "panel_title": "One product list, sorted by use",
            "panel_intro": (
                "Each product is typed with its use, production or consumption, and its value. The "
                "tiles total each department. Compare the two-dept and misclassified presets: one "
                "line changes, and only its use."
            ),
        }),
        "steps_title": "Sorting a product list",
        "steps_intro": "Four steps, the same for any list of products.",
        "steps": [
            ("Ask who uses it up",
             "For each product, ask whether it will be used up in producing something else or in "
             "someone's household. The answer, not the product's name, decides its department."),
            ("Split a product that goes both ways",
             "Coal, cloth and grain go both ways. Divide the quantity by its buyers and enter each "
             "part as a separate line."),
            ("Total each department",
             "Add the values of the means of production for Department I and of the means of "
             "consumption for Department II."),
            ("Check against the whole",
             "The two totals must add up to the value of the whole product. A product left out or "
             "counted twice shows here."),
        ],
        "worked": {
            "title": "The same coal, two departments",
            "intro": [
                "A colliery sells 150 of coal: 100 to a cotton mill and 50 to households. Machines "
                "worth 300 and bread worth 150 are also made. You want each department's total.",
            ],
            "lines": [
                "coal to the mill:  100, Department I",
                "coal to kitchens:  50, Department II",
                "Department I:  300 + 100 = 400",
                "Department II:  150 + 50 = 200",
                "whole product:  400 + 200 = 600",
            ],
            "after": [
                "The colliery is one business, but its product is split between the departments by "
                "who uses it. Filed by what it is, all 150 of coal would go to Department I, and the "
                "households' 50 would be counted as means of production that nobody will produce "
                "with.",
            ],
        },
        "quiz_title": "Sorting by use",
        "quiz": [
            {"q": "A maltster sells malt to a brewery, and the brewery sells beer that households "
                  "drink. On the chapter's rule, which department does each product belong to?",
             "a": ["Malt in Department I, beer in Department II",
                   "Both in Department I, because both were made in factories",
                   "Both in Department II, because both end up in a drink",
                   "Malt in Department II, beer in Department I"],
             "c": 0,
             "why": "The malt is used up in producing beer, so it is a means of production; the beer "
                    "passes into households, so it is a means of consumption. Where a product was "
                    "made does not decide its department, and the malt is not consumed by anyone "
                    "as malt. The last option has the two reversed."},
            {"q": "Why can a single firm's circuit leave out what its workers buy with their wages, "
                  "while the movement of society's capital cannot?",
             "a": ["Because the workers' purchases are part of the circulation by which the whole product is sold and replaced",
                   "Because wages are higher for society than for a single firm",
                   "Because a single firm pays its wages in kind, not in money",
                   "Because society's capital produces no surplus value"],
             "c": 0,
             "why": "For one firm, its buyers are outside it; for society, the workers' spending is "
                    "one of the exchanges that must happen for the product to be disposed of. Wages "
                    "are not higher for society, nothing in the chapter says firms pay in kind, and "
                    "the social capital produces all the surplus value there is."},
            {"q": "In Marx's totals, means of production are worth 6,000 and means of consumption "
                  "3,000. What is the most that workers and capitalists together can buy for their "
                  "households in the year?",
             "a": ["3,000", "6,000", "9,000", "4,500"],
             "c": 0,
             "why": "Only the means of consumption can go into a household, and there are 3,000 of "
                    "them. The 6,000 are means of production, 9,000 is the whole product, and 4,500 "
                    "is half of it, which corresponds to nothing in the scheme."},
            {"q": "In the misclassified preset, coal burned in kitchens is filed with the colliery's "
                  "other coal. What does the sort then get wrong?",
             "a": ["It counts 50 of means of consumption as means of production",
                   "It changes the value of the coal",
                   "It loses 50 from the value of the whole product",
                   "Nothing, because coal is a raw material whatever its use"],
             "c": 0,
             "why": "The whole product is still 600 and the coal is still worth 150; what changes is "
                    "the department 50 of it is counted in. The last option is the mistake itself: "
                    "the departments are defined by use, not by the kind of thing."},
        ],
        "mistakes": [
            ("Thinking of the economy as one big firm",
             "It is tempting to add up society the way a firm adds up its books: inputs on one "
             "side, output on the other, nothing to explain in between. Marx finds this in "
             "Proudhon, who treats society as if it lost its capitalist character by being taken "
             "as a unit. A firm sells its product to others; society has nobody outside to sell to, "
             "and its product comes in two kinds. The marx-totals preset shows the consequence: of "
             "9,000 of product, only 3,000 can go into any household, so all the wages and surplus "
             "value of the year, whatever they add up to, can be spent on that 3,000 alone."),
            ("Sorting by what a thing is rather than by its use",
             "Coal, grain and cloth are not means of production or of consumption by nature. The "
             "misclassified preset files kitchen coal as means of production and moves 50 from "
             "Department II to Department I. The departments are defined by the consumption a "
             "product passes into, productive or individual."),
            ("Taking the money advanced as the limit of production",
             "Chapter 18's second section warns against this. The same workers can be worked "
             "longer or harder, natural forces cost the capitalist nothing, and a shorter turnover "
             "sets the same productive capital going with less money. The money advanced fixes the "
             "value of the capital, not how much it produces."),
        ],
        "standard": (
            "Finish when you can sort a product list into the two departments by use.",
            "Given a list of products with their values and their buyers, assign each part to "
            "Department I or Department II by whether it is used up in production or in a "
            "household, total each department, and state why a single firm's circuit can leave "
            "this question to the market and society's capital cannot."
        ),
        "note": (
            "The two departments are Marx's, from Chapter 20, borrowed here so that Chapter 18's "
            "question has something to compute. Real products are often split between uses, and "
            "the lab sorts only what you tell it: it cannot know who will buy the coal. The "
            "figures in two-dept and misclassified are illustrative; those in marx-totals are "
            "Marx's."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 2, l. 3787 (the dogma). Inline: l. 3690 (Quesnay: broad
    # outlines, simple reproduction, does not circulate), l. 3709-3711 (finally
    # dissolves), l. 3818 (a fourth portion), l. 3820 (one line of production to
    # another), l. 3838 (the first mistake; merely re-appears), l. 3771 (lacked
    # but little), l. 3939 (the Says and Mac-Cullochs), l. 3941 (Say), l. 3945
    # (Storch), l. 3842 (did not create all the value).
    {
        "slug": "former-presentations",
        "title": "Former Discussions: Quesnay and Smith",
        "module": "Chapter 19 · Former Discussions of the Subject",
        "one_line": "Adam Smith resolved the price of every commodity into wages, profit and rent, and so lost the part of the annual product's value that replaces the means of production used up.",
        "summary": (
            "Chapter 19 reads the economists who tried the question before Marx. Quesnay's Tableau "
            "Économique saw that part of the harvest is old capital reappearing; Adam Smith, by "
            "resolving every price into wages, profit and rent, lost it. Compute the annual "
            "product's value with and without its constant capital and find where Smith's account "
            "drops it."
        ),
        "key": [
            "value of annual product = c + v + s",
            "Smith: price = wages + profit + rent",
            "wages = v; profit + rent = s",
            "the dogma's total: v + s",
            "missing: c, the means of production used up",
        ],
        "key_label": "Smith's dogma in five lines",
        "concepts_intro": (
            "The chapter is the history of an idea, told as a mistake handed down. Three things "
            "are needed to follow it."
        ),
        "concepts": [
            ("Quesnay's Tableau",
             "François Quesnay, physician at the court of Louis XV, drew in 1758 a table of how a "
             "nation's harvest circulates between farmers, landowners and artisans so that the next "
             "year can begin. Marx credits him with seeing that part of the product is old "
             "capital-value reappearing, and is no one's income."),
            ("Smith's dogma",
             "Adam Smith held that the price of every commodity resolves into wages, profit and "
             "rent, and so does the price of the whole annual product. Marx calls this the dogma "
             "and restates it in his own letters: the value of a commodity is v + s."),
            ("Value of the product, product in values",
             "The value of the annual product includes the means of production used up, made in "
             "earlier years. The product in values is only what this year's labour added, v + s. "
             "Marx says Smith's first mistake is to treat the two as one."),
        ],
        "read_title": "The dogma first, then where it loses c",
        "read_intro": (
            "Marx states Smith's doctrine in his own terms before he takes it apart. The passage is "
            "that restatement, from the section on Smith."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 19, §2.</strong> &ldquo;The dogma of Adam Smith, to "
                  "the effect that exchangeable value, or the price of any commodity&mdash;and "
                  "therefore of all commodities constituting the annual product of society (since "
                  "he justly assumes everywhere the existence of capitalist production)&mdash;is "
                  "made up of three component parts, or resolves itself into wages, profit, and "
                  "rent, may be reduced to the fact that the value of a commodity is equal to v plus "
                  "s, that is to say, equal to the value of the advanced variable capital plus the "
                  "surplus-value.&rdquo;"),
            ("p", "Start with the man Marx admires. François Quesnay was a court physician who "
                  "turned to economics in his sixties, and his Tableau Économique shows &ldquo;in a "
                  "few broad outlines&rdquo; how a year's national product is distributed by "
                  "circulation so that &ldquo;simple reproduction can take place&rdquo;. It starts "
                  "from last year's harvest and notices something easy to miss: part of the harvest "
                  "is seed. That part &ldquo;does not circulate, but remains in the hands of its "
                  "producers&rdquo;, to serve as capital again. Quesnay counted some things in that "
                  "portion that do not belong there, but Marx says he saw the main thing thanks to "
                  "the limits of his horizon: for him farming was the only sphere where labour "
                  "yields a surplus, and in farming the natural cycle from seed to harvest keeps "
                  "the reproduction of capital in plain view."),
            ("p", "Then Adam Smith, in <em>The Wealth of Nations</em> of 1776. On most things Marx "
                  "builds on Smith; here he says Smith went backwards. In every society, Smith "
                  "writes, the price of every commodity &ldquo;finally dissolves into one or the "
                  "other of these three parts&rdquo;, wages, profit and rent, and so does the price "
                  "of the whole annual product. Rent and profit are both parts of surplus value, so "
                  "in Marx's letters the dogma reads: the value of a commodity is v + s. The c is "
                  "gone."),
            ("p", "Smith saw the objection and answered it. &ldquo;A fourth portion may seem "
                  "necessary in order to reproduce the capital of the farmer, or the wear of his "
                  "laboring cattle and of his other implements.&rdquo; But the horse's price, he "
                  "goes on, is itself rent, wages and profit, so the corn's price still resolves "
                  "into the three. Marx's reply is that the horse's price also contains the means "
                  "of production used up in breeding it, and Smith never says so: &ldquo;He refers us "
                  "from one line of production to another, and from that to a third.&rdquo;"),
            ("p", "The lab does the sum the dogma skips. The marx-scheme preset enters the totals of "
                  "Marx's simple reproduction scheme from Chapter 20, c = 6,000, v = 1,500, s = "
                  "1,500, priced in pounds as Marx later prices them: the annual product is £9,000, "
                  "and the dogma's total is v + s = £3,000, with £6,000 of c missing. The one-firm "
                  "preset takes a single business, Marx's spinner from The Circuits of Capital, £372 "
                  "of means of production, £50 of wages and £78 of surplus value: £500 of yarn, of "
                  "which £128 is anyone's income and £372 is not. The tableau preset puts Quesnay's "
                  "point in illustrative figures, a harvest worth £500 of which £200 is seed and "
                  "advances kept back: the dogma counts £300 and loses the seed."),
            ("p", "<strong>Volume II, Chapter 19, §2.</strong> &ldquo;The first mistake of Adam "
                  "Smith consists in identifying the value of the annual product with the annual "
                  "product in values.&rdquo;"),
            ("p", "Read it slowly, because the two phrases sound alike. The annual product in "
                  "values is what this year's labour created: v + s, £3,000 in the scheme. The value "
                  "of the annual product also includes means of production made in earlier years, "
                  "whose value &ldquo;merely re-appears&rdquo; in this year's goods. The year's "
                  "labour, Marx writes, &ldquo;did not create all the value of the products finished "
                  "by it&rdquo;. Underneath, he says, is the distinction from “The Twofold Character "
                  "of Labour”: Smith does not separate labour that makes useful things, which made "
                  "every one of the year's products, from labour that creates value, which created "
                  "only a third of their value."),
            ("p", "Smith came close. He noticed that the workers who make machines are paid wages "
                  "that are their income, though nothing they make can be eaten, and that a "
                  "shopkeeper's stock is his capital and other people's consumption. Had he summed "
                  "up those observations, Marx says, &ldquo;he would have lacked but little for the "
                  "complete solution of the problem&rdquo;. His successors went the other way. Say "
                  "concluded that &ldquo;the total value of all products in a society is divided as "
                  "revenue&rdquo;, and Marx has a dry line for it: &ldquo;It is never the original "
                  "thinkers that draw the absurd conclusions. They leave that to the Says and "
                  "Mac-Cullochs.&rdquo; Storch saw the absurdity: if revenue equals the gross "
                  "product, a nation could consume its whole annual product &ldquo;without in the "
                  "least reducing its future revenue&rdquo;."),
            ("p", "Smith's defenders have a stronger reply than Smith gave. Follow the horse back: "
                  "its price is wages, profit, rent and some fodder; the fodder's price is wages, "
                  "profit, rent and some seed; each step back leaves a smaller remainder of means "
                  "of production. Piero Sraffa made this exact in 1960 as the reduction of a price "
                  "to dated quantities of labour, in which the remainder can be made as small as "
                  "you like by going back far enough. Marx wrote against Smith, not Sraffa. What in "
                  "the chapter bears on the regress is the period it asks about: one year's "
                  "product, out of which the £6,000 of means of production used up that year must "
                  "be replaced, however the regress into earlier years comes out. National accounts today draw a similar line: the year's wages, "
                  "profits, interest and rents add up to less than gross output, by the "
                  "intermediate goods and the depreciation used up."),
            ("p", "Smith's mistake had a reason: for a consumer, every price does seem to dissolve "
                  "into somebody's income. The next lesson, “Simple Reproduction: The Three Great "
                  "Exchanges”, shows where that appearance comes from, in the exchange between the "
                  "two departments."),
        ],
        "lab": ("capkit", {
            "mode": "revenue",
            "view": "dogma",
            "money_unit": "£",
            "preset": "marx-scheme",
            "presets": [
                {"id": "marx-scheme", "label": "Marx's simple scheme: 6,000c + 1,500v + 1,500s",
                 "c": 6000, "v": 1500, "s": 1500, "expect": {"rvTotal": "£9,000", "rvSmith": "v + s = £3,000; c = £6,000 missing"}},
                {"id": "one-firm", "label": "One firm: Marx's spinner, £372 + £50 + £78",
                 "c": 372, "v": 50, "s": 78, "expect": {"rvTotal": "£500", "rvSmith": "v + s = £128; c = £372 missing"}},
                {"id": "tableau", "label": "Quesnay's seed in outline, illustrative: £200 kept back",
                 "c": 200, "v": 100, "s": 200, "expect": {"rvTotal": "£500", "rvSmith": "v + s = £300; c = £200 missing"}},
            ],
            "panel_title": "The annual product, with and without c",
            "panel_intro": (
                "The product's c, v and s go in. One tile gives its value, c + v + s; the other gives "
                "the dogma's total, v + s, and the c it leaves out."
            ),
        }),
        "steps_title": "Finding the missing c",
        "steps_intro": "Four steps, for one firm's product or a whole year's.",
        "steps": [
            ("Write the product as c + v + s",
             "Give the value of the product in its three parts: means of production used up, "
             "wages, and surplus value."),
            ("Add up the incomes",
             "Wages are v. Profit, interest and rent are all parts of s. Their sum, v + s, is the "
             "year's income."),
            ("Subtract",
             "Take v + s from c + v + s. The difference is c, the value that no income of the year "
             "accounts for."),
            ("Say what the difference is",
             "The difference is not lost or double-counted. It is the value of means of production "
             "made in earlier periods, which reappears in this product and must be replaced out "
             "of it."),
        ],
        "worked": {
            "title": "Marx's 9,000 and Smith's 3,000",
            "intro": [
                "Take the totals of Marx's simple reproduction scheme in Chapter 20. You want the "
                "value of the annual product and the part of it that Smith's account leaves out.",
            ],
            "lines": [
                "c:  4000 (I) + 2000 (II) = 6000",
                "v:  1000 (I) + 500 (II) = 1500",
                "s:  1000 (I) + 500 (II) = 1500",
                "annual product:  6000 + 1500 + 1500 = 9000",
                "Smith's total:  v + s = 3000",
                "missing:  9000 − 3000 = 6000 = c",
            ],
            "after": [
                "Two thirds of the annual product's value is means of production used up. All the "
                "incomes of the year together can buy only the other third.",
            ],
        },
        "quiz_title": "What the dogma leaves out",
        "quiz": [
            {"q": "Marx's simple scheme has c = 6,000, v = 1,500 and s = 1,500 in all. What total "
                  "does Smith's dogma give for the price of the whole annual product?",
             "a": ["3,000", "9,000", "6,000", "1,500"],
             "c": 0,
             "why": "The dogma resolves every price into wages, profit and rent, which is v + s = "
                    "3,000. 9,000 is the actual value, which is Marx's answer, not Smith's; 6,000 is "
                    "the c the dogma loses; 1,500 is v or s alone."},
            {"q": "What does Marx call Smith's first mistake?",
             "a": ["Identifying the value of the annual product with the annual product in values",
                   "Counting rent as part of surplus value",
                   "Thinking that only agriculture produces a surplus",
                   "Measuring value by the labour expended"],
             "c": 0,
             "why": "That is the sentence in the text. Marx counts rent as part of surplus value "
                    "himself, the agriculture-only view is Quesnay's limit, and measuring value by "
                    "labour is common ground between Smith and Marx."},
            {"q": "Smith grants that a fourth portion of the price of corn replaces the farmer's "
                  "horse, then says the horse's price is itself wages, profit and rent. What does "
                  "Marx say this argument forgets?",
             "a": ["That the horse's price also contains the means of production used up in rearing it",
                   "That horses are not commodities",
                   "That no rent is paid on pasture",
                   "That the farmer makes no profit on corn"],
             "c": 0,
             "why": "Marx's objection is that Smith passes the price back from one line of production "
                    "to another without adding that each also contains means of production used up. "
                    "Horses are bought and sold, and nothing in the chapter denies rent on pasture or "
                    "the farmer's profit."},
            {"q": "In the one-firm preset, Marx's spinner has £372 of means of production, £50 of "
                  "wages and £78 of surplus value. How much of the yarn's value is no one's income?",
             "a": ["£372", "£128", "£50", "£0"],
             "c": 0,
             "why": "The £372 replaces the cotton and the wear of the spindles. £128 is v + s, the "
                    "part that is income; £50 is the wages alone; and £0 is the dogma's answer, "
                    "which this lesson exists to correct."},
        ],
        "mistakes": [
            ("Resolving the whole price of the annual product into incomes",
             "This is Smith's dogma, and it is plausible: every price you pay seems to go to "
             "someone as wages, profit or rent. Say drew the conclusion that &ldquo;the total value "
             "of all products in a society is divided as revenue&rdquo;. The marx-scheme preset "
             "refutes it with Marx's figures: the annual product is worth £9,000, while v + s, every "
             "wage, profit and rent of the year, is £3,000. The other £6,000 is means of production "
             "used up, which must be replaced out of the product before anyone's income is "
             "counted."),
            ("Treating Smith's regress as a proof",
             "Smith passes the horse's price back to its breeder and stops at wages, profit and "
             "rent. Each earlier product also contains means of production, which is what Marx "
             "says Smith forgets to add. Even where such a regress can be made to converge, as "
             "Sraffa later argued it can, it is an account of past years; the question here is how this "
             "year's product replaces what this year used up."),
            ("Confusing what is revenue for one person with revenue for society",
             "Smith saw that a shopkeeper's stock is his capital and other people's consumption. "
             "The next chapter calls the phrase &ldquo;capital for one and revenue for "
             "another&rdquo; only partially true: the wages and surplus value of Department I are "
             "income to its workers and capitalists, but the product in which they are embodied is "
             "machines and materials, which nobody can live on."),
        ],
        "standard": (
            "Finish when you can compute an annual product with and without c and name what Smith loses.",
            "Given c, v and s for a product, compute its value, the total the dogma gives as the "
            "sum of incomes, and the difference, and state that the difference is the constant "
            "capital used up, which no income of the period accounts for."
        ),
        "note": (
            "Smith is quoted here as Kerr prints him: Untermann's English of Marx's German of "
            "Smith, which is not word for word what Smith wrote in 1776. The lab subtracts one sum "
            "from another; it cannot settle whether Marx's division of value into c, v and s is the "
            "right one, which is the dispute behind Sraffa's reading and every later one. The "
            "tableau figures are illustrative; Marx gives none for the Tableau in this chapter."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 2, l. 4031-4037 (the recapitulation); l. 4076 (I(v+s) = IIc).
    # Inline: l. 4013 (millions of francs), l. 4039 (points of vantage),
    # l. 4047 (used up only in department I), l. 4228 (1500 circulates 5000),
    # l. 3979 (divergence of prices), l. 4155 (smaller or greater), l. 3985
    # (an abstraction), l. 4924 (Destutt: recover only their 100), l. 5160
    # (diagram b), l. 4350 (two thirds of the social working day).
    {
        "slug": "simple-reproduction-the-three-exchanges",
        "title": "Simple Reproduction: The Three Great Exchanges",
        "module": "Chapter 20 · Simple Reproduction",
        "one_line": "With every surplus value spent, Marx's two-department economy reproduces itself only if Department I's wages and surplus value equal Department II's constant capital.",
        "summary": (
            "Chapter 20 sets out Marx's scheme of a whole economy in two departments, 9,000 of "
            "annual product, and follows it through three exchanges: within Department II, between "
            "the departments, and within Department I. Check whether a scheme reproduces itself, "
            "I(v + s) = IIc, compute each exchange, and see what is left without a buyer when the "
            "condition fails."
        ),
        "key": [
            "I: 4000c + 1000v + 1000s = 6000",
            "II: 2000c + 500v + 500s = 3000",
            "within II: IIv + IIs = 1000",
            "between: I(v + s) = 2000 = IIc",
            "within I: Ic = 4000",
            "simple reproduction: I(v + s) = IIc",
        ],
        "key_label": "The scheme and its three exchanges",
        "concepts_intro": (
            "Three assumptions make the scheme work, and the chapter keeps all of them."
        ),
        "concepts": [
            ("Simple reproduction",
             "Every year's surplus value is spent on consumption, so the economy starts each year at "
             "the same size. Marx calls this an abstraction, but one that is always a part of "
             "accumulation and can be studied by itself."),
            ("Exchange at value",
             "Products exchange at their values, and no values change during the year. Marx adds "
             "that prices diverging from values would change the shares individual capitalists "
             "get, not the quantities exchanged."),
            ("Balance in kind as well as in value",
             "Department I makes nothing anyone can eat, and Department II makes nothing a factory "
             "can use. Each part of the product has to reach the department that can use it in its "
             "natural form, so the scheme must balance in use as well as in value."),
        ],
        "read_title": "The scheme first, then the three exchanges",
        "read_intro": (
            "Marx sets out his figures in the chapter's second section and sums them up in two "
            "lines. Everything in the chapter is computed from them."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 20, §2.</strong> &ldquo;Recapitulation: Total annual "
                  "product in commodities: I. 4000 c+1000 v+1000 s=6000 means of production. II. "
                  "2000 c+ 500 v+ 500 s=3000 articles of consumption. Total value 9000, exclusive "
                  "of the fixed capital persisting in its natural form, according to our "
                  "assumption.&rdquo;"),
            ("p", "These are the best-known figures in Volume II. Department I makes means of "
                  "production and Department II means of consumption, as in “The Object of the "
                  "Inquiry”. Each department's product is c + v + s, with the rate of surplus value "
                  "at 100 per cent in both, and the figures, Marx says, &ldquo;may indicate millions "
                  "of francs, marks, pounds sterling, or dollars&rdquo;. The question is whether this "
                  "9,000 can be disposed of so that next year starts exactly where this one did. "
                  "Leaving money aside at first, Marx finds &ldquo;three great points of "
                  "vantage&rdquo;, three exchanges that clear the whole product."),
            ("p", "The first exchange is inside Department II. Its workers' 500 of wages and its "
                  "capitalists' 500 of surplus value must be spent on means of consumption, and "
                  "Department II's own product contains 1,000 of exactly that. Its workers buy back "
                  "part of what they made, its capitalists buy from one another, and `500v + 500s` "
                  "of Department II's product disappears into households."),
            ("p", "The second is between the departments. Department I's 1,000 of wages and 1,000 "
                  "of surplus value must also be spent on means of consumption, but Department I's "
                  "product is machines and materials. Department II still holds 2,000 of means of "
                  "consumption whose value is its constant capital, and it needs means of "
                  "production to replace what it used up. The two meet: Department I's `v + s` in "
                  "the form of means of production goes to Department II, and Department II's `c` in "
                  "the form of means of consumption goes to Department I. Marx draws the "
                  "condition:"),
            ("p", "<strong>Volume II, Chapter 20, §3.</strong> &ldquo;It follows that, on the "
                  "basis of simple reproduction, the sum of the values of v plus s of the "
                  "commodity-capital of I (and therefore a corresponding proportional part of the "
                  "total product in commodities of I) must be equal to the constant capital c of "
                  "department II, which is likewise disposed of as a proportional part of the "
                  "entire product in commodities of department II; or I (v + s) = II c.&rdquo;"),
            ("p", "The third exchange is inside Department I. What is left is its 4,000 of constant "
                  "capital, means of production that &ldquo;can be used up only in department "
                  "I&rdquo;: coal goes to the ironworks, iron to the colliery, machines to the "
                  "machine-builder. It is exchanged among Department I's capitalists, and none of it "
                  "is ever anyone's revenue. Then Marx puts the money back in. Department I pays "
                  "£1,000 in wages; its workers buy means of consumption from Department II; "
                  "Department II spends the same £1,000 on means of production from Department I, "
                  "whose wage fund comes home. Department II advances £500 more, which goes round "
                  "twice and returns to it. &ldquo;By means of 1500 pounds sterling, a quantity of "
                  "commodities valued at 5000 pounds sterling has been circulated.&rdquo;"),
            ("p", "The lab checks the condition and computes the three exchanges. The marx preset "
                  "enters the scheme as printed: I(v + s) = 2,000 = IIc, 2,000 exchanged each way, "
                  "and 4,000 exchanged within Department I. The too-much-in-i preset raises Department "
                  "I's surplus value to 1,100, and the balance tile reads I(v + s) = 2,100, IIc = "
                  "2,000: gap +100, with 2,000 exchanged each way and 100 of Department I's product "
                  "unsold. The too-little-in-i preset lowers it to 900, and 100 of Department II's "
                  "product is unsold. Marx states both cases: if `I(v + s)` were smaller than `IIc`, "
                  "&ldquo;it would be impossible for II to reproduce its entire constant "
                  "capital; if it were greater, a surplus would remain unused&rdquo;. The diagram-b "
                  "preset is a smaller scheme Marx gives in Chapter 21, I 4,000c + 875v + 875s and II "
                  "1,750c + 376v + 376s, 8,252 in all: 1,750 against 1,750, and it closes too. The "
                  "condition is a proportion, not a size."),
            ("p", "The condition also explains Smith's mistake from the last lesson. Department "
                  "II's product, 3,000, has the same value as the whole year's `v + s` in both "
                  "departments, because its 2,000 of constant capital is exchanged against "
                  "Department I's `v + s`. Seen from the consumer's side, every price really does "
                  "resolve into incomes, but only for the means of consumption. Two thirds of the "
                  "year's social labour, Marx says, went into producing means of production, and "
                  "none of that product can be bought with wages."),
            ("p", "Marx says that prices diverging from values &ldquo;would not exert any influence "
                  "on the movements of social capital&rdquo;: the same products would be exchanged, "
                  "only in different shares. The standard objection is to what the condition can "
                  "show. It is an accounting identity at given values: if the scheme is to repeat "
                  "itself, `I(v + s) = IIc`. It says nothing about how an economy that nobody plans "
                  "comes to meet it, and an economist who expects prices and quantities to adjust "
                  "until markets clear will point out that the scheme, holding every price at value, "
                  "has left out exactly the mechanism that would do the adjusting. Leontief's "
                  "input–output analysis and the later two-sector models take the condition as one "
                  "line of a larger system. Marx's own view, stated in the next chapter, is that in "
                  "this mode of production such a balance comes about only by accident."),
            ("p", "Department II's own exchange hides a subdivision, between necessities and the "
                  "luxuries only capitalists buy, which this course leaves aside. The scheme so far "
                  "also treats all constant capital as used up within the year. The next lesson, "
                  "“Simple Reproduction: Fixed Capital and Money”, lets the machines last, and shows "
                  "that this alone can break the balance."),
        ],
        "lab": ("capkit", {
            "mode": "schemes",
            "view": "simple",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's scheme: I 4,000c + 1,000v + 1,000s; II 2,000c + 500v + 500s",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 2000, "v": 500, "s": 500},
                 "expect": {"scBalance": "I(v + s) = 2,000 = IIc", "scIExchange": "2,000 each way"}},
                {"id": "too-much-in-i", "label": "Department I's s raised to 1,100",
                 "I": {"c": 4000, "v": 1000, "s": 1100}, "II": {"c": 2000, "v": 500, "s": 500},
                 "expect": {"scBalance": "I(v + s) = 2,100, IIc = 2,000: gap +100", "scIExchange": "2,000 each way; 100 of Department I's product unsold"}},
                {"id": "too-little-in-i", "label": "Department I's s lowered to 900",
                 "I": {"c": 4000, "v": 1000, "s": 900}, "II": {"c": 2000, "v": 500, "s": 500},
                 "expect": {"scBalance": "I(v + s) = 1,900, IIc = 2,000: gap −100", "scIExchange": "1,900 each way; 100 of Department II's product unsold"}},
                {"id": "diagram-b", "label": "Marx's diagram b from Chapter 21: 8,252 in all",
                 "I": {"c": 4000, "v": 875, "s": 875}, "II": {"c": 1750, "v": 376, "s": 376},
                 "expect": {"scBalance": "I(v + s) = 1,750 = IIc", "scIExchange": "1,750 each way"}},
            ],
            "panel_title": "Does the scheme reproduce itself?",
            "panel_intro": (
                "Each department's c, v and s go in. The tiles test I(v + s) against IIc and give the "
                "exchange between the departments and within Department I; the table lists all "
                "three exchanges."
            ),
        }),
        "steps_title": "Checking a scheme for simple reproduction",
        "steps_intro": "Four steps, for any two-department scheme with all surplus value spent.",
        "steps": [
            ("Clear Department II internally",
             "IIv + IIs is spent on means of consumption, which Department II's own product "
             "supplies. That much of its product goes to its own workers and capitalists."),
            ("Compare I(v + s) with IIc",
             "Department I's wages and surplus value must be spent on means of consumption, and "
             "Department II's constant capital must be turned back into means of production. "
             "Simple reproduction needs the two equal."),
            ("Clear Department I internally",
             "Ic is means of production that only Department I can use. It is exchanged among "
             "Department I's capitalists and is no one's revenue."),
            ("Name the remainder",
             "If I(v + s) exceeds IIc, the excess of Department I's product has no buyer; if it falls "
             "short, the shortfall of Department II's product has none."),
        ],
        "worked": {
            "title": "Marx's 9,000, cleared in three exchanges",
            "intro": [
                "Take Marx's scheme as printed. You want each exchange and the test of the "
                "condition.",
            ],
            "lines": [
                "within II:  500v + 500s = 1000",
                "I(v + s):  1000 + 1000 = 2000",
                "IIc:  2000, so I(v + s) = IIc",
                "between:  2000 each way",
                "within I:  Ic = 4000",
                "check:  1000 + 2·2000 + 4000 = 9000",
            ],
            "after": [
                "Every part of the 9,000 is accounted for once. Raise Department I's surplus value "
                "to 1,100 and the second line becomes 2,100 against 2,000: 100 of means of "
                "production have no buyer.",
            ],
        },
        "quiz_title": "Balancing the two departments",
        "quiz": [
            {"q": "A scheme has I: 4000c + 1000v + 1000s and II: 2000c + 500v + 500s. Under simple "
                  "reproduction, how much value passes between the two departments in each "
                  "direction?",
             "a": ["2,000", "1,000", "4,000", "3,000"],
             "c": 0,
             "why": "I(v + s) = 2,000 goes to Department II as means of production and IIc = 2,000 "
                    "comes back as means of consumption. 1,000 is the exchange within Department II, "
                    "4,000 the exchange within Department I, and 3,000 Department II's whole "
                    "product."},
            {"q": "Department I's surplus value rises from 1,000 to 1,100, everything else as in "
                  "Marx's scheme. Under simple reproduction, what happens to the extra 100?",
             "a": ["It is means of production that find no buyer",
                   "Department II buys it and expands its constant capital",
                   "Department I's capitalists consume it as revenue",
                   "It is absorbed in the exchange within Department I"],
             "c": 0,
             "why": "Department II needs exactly 2,000 to replace its constant capital, and under "
                    "simple reproduction it does not expand. Department I's capitalists cannot live "
                    "on means of production, and the exchange within Department I covers only Ic, "
                    "which is already replaced."},
            {"q": "Of Marx's 9,000, which part is exchanged only within Department I and is never "
                  "anyone's revenue?",
             "a": ["Ic, 4,000", "IIc, 2,000", "I(v + s), 2,000", "II(v + s), 1,000"],
             "c": 0,
             "why": "Ic is means of production replaced among Department I's capitalists. IIc is "
                    "exchanged with Department I, I(v + s) is the revenue of Department I's workers "
                    "and capitalists, and II(v + s) is the revenue of Department II's."},
            {"q": "Department I pays £1,000 in wages. On Marx's account, by what route does that money "
                  "return to Department I's capitalists?",
             "a": ["Its workers buy means of consumption from II, and II spends the money on means of production from I",
                   "Its workers buy back the means of production they made",
                   "It returns to I directly as profit",
                   "It is paid out again as wages in Department II"],
             "c": 0,
             "why": "Department I's workers cannot use machines, so they spend in Department II, and "
                    "Department II spends the money on replacing its constant capital from Department "
                    "I. Nothing returns as profit, and Department II's wages are paid from its own "
                    "variable capital."},
        ],
        "mistakes": [
            ("Thinking each department's product only needs a buyer somewhere",
             "On this view a market is a market: make anything and someone will buy it. The "
             "too-much-in-i preset refutes it. Raise Department I's surplus value by 100 and the extra "
             "100 is means of production, which neither Department I's workers nor its capitalists "
             "can live on; its only possible buyer is Department II, which needs exactly 2,000 to "
             "replace its constant capital. The tile shows 2,000 exchanged each way and 100 of "
             "Department I's product unsold. The buyer has to be in the other department, and in "
             "the right amount."),
            ("Reading Ic as somebody's income",
             "The 4,000 of Department I's constant capital is coal, iron and machines sold among "
             "Department I's capitalists. They do not consume it, and the workers who made it were "
             "paid out of v. It is more than two fifths of the annual product, and none of it is "
             "revenue."),
            ("Supposing that the return of wages enriches the capitalist",
             "Department II's workers spend their wages on Department II's goods and the money "
             "comes back. Destutt de Tracy, whom Marx reads in the chapter's last section, took that "
             "return as a source of profit. Marx's reply is that it explains at best why the "
             "capitalists do not get any poorer: they recover only the money they paid out, "
             "against goods of the same value."),
        ],
        "standard": (
            "Finish when you can check a two-department scheme for simple reproduction and compute its exchanges.",
            "Given c, v and s for Departments I and II, compute I(v + s) and IIc and state whether "
            "the scheme reproduces itself; compute the exchange within Department II, the exchange "
            "between the departments and the exchange within Department I; and where the condition "
            "fails, state which department's product is left unsold and how much."
        ),
        "note": (
            "The scheme assumes that everything exchanges at its value, that the rate of surplus "
            "value is 100 per cent in both departments and that every surplus value is spent; it "
            "leaves out fixed capital, luxuries and foreign trade. I(v + s) = IIc says what balance "
            "requires; the lab cannot show how, or whether, an unplanned economy comes to meet it. "
            "The marx and diagram-b figures are Marx's; the other two presets each change one "
            "figure."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 2, l. 4567 (the passage); l. 4780 (a crisis). Inline: l. 4655
    # (Mr. X's spinning machine), l. 4610 (1800; would not return), l. 4631
    # (fall from the clouds), l. 4723 (would seem to be a law), l. 4733 and
    # l. 4753 (220 and 180; commodities valued at 40), l. 4796 (new to them),
    # l. 4794 (continuous relative overproduction; anarchy), l. 4790 (not an
    # evil in itself), l. 4792 (wider sphere), l. 4565 (suspended), l. 4831
    # (simple reproduction includes hoarding).
    {
        "slug": "simple-reproduction-fixed-capital-and-money",
        "title": "Simple Reproduction: Fixed Capital and Money",
        "module": "Chapter 20 · Simple Reproduction",
        "one_line": "Department II hoards its machines' wear in money and renews worn-out machines in kind; unless the two are equal, part of the product finds no buyer even on an unchanging scale.",
        "summary": (
            "Section 11 of Chapter 20 adds the wear of fixed capital to the scheme. Part of IIc is "
            "sold for money that is kept as a hoard until machines wear out; part is spent at once on "
            "new machines. Compute the signed gap between the renewals bought in kind and the wear "
            "hoarded in money, and say which side is left short."
        ),
        "key": [
            "IIc includes wear, hoarded in money",
            "some capitals renew machines in kind",
            "renewals − wear hoarded: the gap",
            "a negative gap: Department I's product unsold",
            "a positive gap: Department I short",
            "balance needs renewals = wear hoarded",
        ],
        "key_label": "Fixed capital in the scheme",
        "concepts_intro": (
            "The last lesson's scheme treated constant capital as if it were all used up within the "
            "year. This one lets the machines last."
        ),
        "concepts": [
            ("Wear in money",
             "A machine passes its value to the product bit by bit. When the product is sold, that "
             "part of the price is not spent on a new machine; it is set aside as a hoard until the "
             "machine is worn out."),
            ("Renewal in kind",
             "Every year some machines in Department II reach the end of their lives, and their "
             "owners spend a whole accumulated hoard on new ones at once. That is a purchase from "
             "Department I with no sale against it."),
            ("The condition",
             "For the scheme to close, the money hoarded by one group of Department II's "
             "capitalists must equal the money another group spends on renewals. Marx says such a "
             "balance would seem to be a law of reproduction on the same scale, and then shows "
             "what happens when it fails."),
        ],
        "read_title": "The hoard first, then the case where it fails",
        "read_intro": (
            "Section 11 is long and works through several attempted solutions. The passage that "
            "opens it says where the difficulty comes from."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 20, §11.</strong> &ldquo;But the money received "
                  "through the sale of commodities, so far as it represents the value of the wear "
                  "and tear of fixed capital, is not reconverted into that component part of "
                  "productive capital whose loss in value it makes good. It settles down beside the "
                  "productive capital and retains the form of money.&rdquo;"),
            ("p", "Marx's own example is a spinner he calls Mr. X. What his spinning machine loses in "
                  "wear reappears in the value of his yarn. When the yarn is sold, that part of the "
                  "price is put by, year after year, and spent only when the machine has to be "
                  "replaced, all at once. For one capitalist this is ordinary prudence. The question "
                  "is what it does to the scheme of the last lesson, where Department I's `v + s` had "
                  "to be exchanged in full against Department II's `c`."),
            ("p", "Here is the difficulty. Department II's 2,000 of constant capital includes wear, "
                  "say 200, that it wants to keep as money this year rather than turn into means of "
                  "production. Then Department II sells 2,000 to Department I but buys only 1,800 "
                  "back, and the 200 it keeps must come from Department I, which &ldquo;would have to "
                  "make good the balance of 200 in money, which would not return to it&rdquo;. "
                  "Department I would be left with 200 of its own surplus product unsold. Assuming "
                  "that Department I simply supplies the money, Marx says, is as legitimate as "
                  "assuming &ldquo;that 200 p. st. fall every year from the clouds&rdquo;."),
            ("p", "His solution is that Department II is not one capitalist. Its fixed capitals are of "
                  "different ages. One group, section 1, has machines that expire this year and "
                  "spends its hoard on new ones, buying from Department I and selling nothing back. "
                  "Another, section 2, sells the part of its product that carries wear and keeps the "
                  "money. Section 1's money goes to Department I, Department I spends it on section "
                  "2's goods, and it ends as section 2's hoard. The two one-sided acts cancel, if "
                  "they are equal. &ldquo;Such a balance of value would seem to be a law of "
                  "reproduction on the same scale.&rdquo;"),
            ("p", "Then Marx takes the cases where they are not. With section 1 spending 220 and "
                  "section 2 holding 200, 20 of section 1's money can buy no fixed capital. With "
                  "section 1 spending 180, &ldquo;There remain 20 I s unsaleable on one side, and 20 "
                  "II c of section 2 on the other. In other words, commodities valued at 40 remain "
                  "unsaleable.&rdquo;"),
            ("p", "The lab computes the gap as renewals less wear hoarded, with the departments as "
                  "in Marx's scheme. The balanced preset hoards 200 and renews 200: 0, renewals = "
                  "wear hoarded. The short-renewals preset renews only 100 against 200 hoarded: "
                  "−100, 100 of Department I's product unsold. The bunched preset, a year in which "
                  "many machines expire together, renews 300: +100, Department I 100 short of the "
                  "means of production demanded. The marx-180 preset takes Marx's second case, 180 "
                  "against 200: −20. The tile counts Department I's side; Marx counts Department "
                  "II's unsold 20 as well, 40 in all. In every preset the balance tile still reads "
                  "I(v + s) = 2,000 = IIc. The scheme balances in value and the product still does "
                  "not clear."),
            ("p", "<strong>Volume II, Chapter 20, §11.</strong> &ldquo;The result would be a "
                  "crisis&mdash;a crisis in production&mdash;in spite of the fact that reproduction "
                  "had taken place on the same scale.&rdquo;"),
            ("p", "Marx is pleased with this. A disproportion between fixed and circulating capital "
                  "was a favourite explanation of crises among economists, but always as a "
                  "disturbance of growth. &ldquo;That such a disproportion can and must arise even "
                  "when the fixed capital is merely preserved by renewal is new to them.&rdquo; In a "
                  "society that planned its production, he says, the remedy would be a "
                  "&ldquo;continuous relative overproduction&rdquo;, a reserve of fixed capital and "
                  "materials kept beyond the year's needs. &ldquo;Such a surplus is not an evil in "
                  "itself, but it is an evil under the capitalist system of production.&rdquo; "
                  "Foreign trade can relieve the pressure, but only by moving the contradiction to a "
                  "wider sphere."),
            ("p", "The standard objection is that the conditions are set to make the mismatch "
                  "show. Marx leaves out credit and stocks of goods, and with thousands of firms "
                  "whose machines are of every age, the machines expiring in a year and the wear set "
                  "aside will usually be close, while banks lend one firm's depreciation fund to "
                  "another firm that is renewing. On that view the gap is a ripple, absorbed by "
                  "credit and inventories. Marx's claim is narrower: that the balance is not "
                  "guaranteed even under the strictest assumptions, and that an industry equipped all "
                  "at once will renew all at once. Section 12 adds a related point about money: "
                  "with gold mined at home, even simple reproduction, Marx concludes, "
                  "&ldquo;inevitably includes the accumulation, or hoarding, of money&rdquo;."),
            ("p", "So far the hoards have been funds for replacement. The next lesson, “Accumulation "
                  "in Department I and the Money It Needs”, turns to the hoard that waits to become "
                  "new capital, and asks who buys while it grows."),
        ],
        "lab": ("capkit", {
            "mode": "schemes",
            "view": "fixed",
            "preset": "balanced",
            "presets": [
                {"id": "balanced", "label": "Marx's scheme: 200 of wear hoarded, 200 renewed in kind",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 2000, "v": 500, "s": 500},
                 "wear_set_aside": 200, "renewals": 200, "expect": {"scFixedGap": "0: renewals = wear hoarded"}},
                {"id": "short-renewals", "label": "Renewals of 100 against 200 hoarded",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 2000, "v": 500, "s": 500},
                 "wear_set_aside": 200, "renewals": 100, "expect": {"scFixedGap": "−100: 100 of Department I's product unsold"}},
                {"id": "bunched", "label": "Machines expire together: renewals of 300",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 2000, "v": 500, "s": 500},
                 "wear_set_aside": 200, "renewals": 300, "expect": {"scFixedGap": "+100: Department I 100 short"}},
                {"id": "marx-180", "label": "Marx's second case: 180 renewed against 200",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 2000, "v": 500, "s": 500},
                 "wear_set_aside": 200, "renewals": 180, "expect": {"scFixedGap": "−20: 20 of Department I's product unsold"}},
            ],
            "panel_title": "Wear hoarded against machines renewed",
            "panel_intro": (
                "The departments are Marx's scheme. Set the wear Department II keeps in money and the "
                "fixed capital it renews in kind; the gap tile is renewals less wear, signed. Watch "
                "the balance tile stay where it is."
            ),
        }),
        "steps_title": "Balancing wear against renewals",
        "steps_intro": "Four steps for any year of simple reproduction with fixed capital.",
        "steps": [
            ("Find the wear hoarded",
             "Take the part of Department II's constant capital that is wear on machines still in "
             "use. It is sold for money and kept: a sale with no purchase."),
            ("Find the renewals",
             "Take the machines in Department II that expire this year and are replaced in kind out "
             "of earlier hoards: a purchase with no sale."),
            ("Subtract",
             "Renewals less wear hoarded. Zero means the one-sided purchases and sales cancel."),
            ("Name the short side",
             "Below zero, that much of Department I's product has no buyer. Above zero, Department "
             "I is that much short of the means of production demanded."),
        ],
        "worked": {
            "title": "Too few machines wear out",
            "intro": [
                "In Marx's scheme Department II hoards 200 of wear this year, and the capitalists "
                "whose machines expire spend 100 on new ones. You want the gap and its side.",
            ],
            "lines": [
                "balance in value:  I(v + s) = 2000 = IIc",
                "wear hoarded:  200 (sold, not spent)",
                "renewals:  100 (bought, nothing sold)",
                "gap:  100 − 200 = −100",
                "unsold:  100 of Department I's product",
            ],
            "after": [
                "The value scheme balances, and still 100 of means of production has no buyer, "
                "because 100 of the money Department II received is lying in a hoard. Renew 300 "
                "instead and the gap is +100: Department I cannot supply the machines demanded.",
            ],
        },
        "quiz_title": "Wear, renewals and the short side",
        "quiz": [
            {"q": "Department II hoards 200 of wear this year, and the capitalists whose machines "
                  "expire spend 100 on renewals. On the chapter's account, what is left over?",
             "a": ["100 of Department I's product without a buyer",
                   "Department I 100 short of means of production",
                   "Nothing, because the scheme still balances in value",
                   "100 of Department II's hoard spent on consumption"],
             "c": 0,
             "why": "Department II sells 200 and keeps the money, but buys only 100 with old hoards, "
                    "so 100 of Department I's product finds no buyer. Department I would be short "
                    "only if renewals exceeded the hoard. The value balance does not prevent it, and "
                    "the hoard is not spent on consumption."},
            {"q": "Renewals are 300 against 200 hoarded. What does the gap tile report?",
             "a": ["Department I 100 short",
                   "100 of Department I's product unsold",
                   "Department II's hoard grows by 100",
                   "The scheme no longer satisfies I(v + s) = IIc"],
             "c": 0,
             "why": "More is bought in kind than was set aside, so Department I cannot supply 100 of "
                    "the means of production demanded. Unsold product is the opposite case, the hoard "
                    "shrinks rather than grows, and the balance tile is unchanged at 2,000."},
            {"q": "Why does Marx reject the idea that Department I advances the money that Department "
                  "II keeps for wear?",
             "a": ["Department I would pay out money that never returns to it, and 200 of its own product would stay unsold",
                   "Department I has no money at all",
                   "Wear is not part of Department II's constant capital",
                   "Department I's capitalists hoard all their money"],
             "c": 0,
             "why": "Money advanced to circulation returns only against a sale, and here Department I "
                    "would sell nothing for it; Marx compares the assumption to money falling from the "
                    "clouds. Department I does hold money, wear is part of IIc, and nothing in the "
                    "section says Department I hoards everything."},
            {"q": "In Marx's second case, section 1 of Department II renews 180 while section 2 holds "
                  "200 of wear. How much remains unsaleable in all, by Marx's count?",
             "a": ["40", "20", "180", "0"],
             "c": 0,
             "why": "20 of Department I's surplus product and 20 of section 2's goods are left unsold, "
                    "40 in all. 20 is one side only, which is what the lab's tile counts; 180 is what "
                    "section 1 spends; 0 would need renewals equal to the hoard."},
        ],
        "mistakes": [
            ("Thinking depreciation balances itself automatically every year",
             "An accountant charges depreciation every year, and on the books it always balances: "
             "so much wear, so much set aside. That is true of one firm, and it is the picture the "
             "short-renewals preset breaks. The balance tile still reads I(v + s) = 2,000 = IIc, yet "
             "with 200 hoarded and only 100 renewed the gap tile reads −100: 100 of Department I's "
             "product has no buyer. For society, depreciation balances only if the money some "
             "capitalists set aside equals the money others spend on renewals, and nothing makes "
             "the two equal."),
            ("Supposing the gap can run only one way",
             "The bunched preset is the opposite case: more machines expire than are wearing, "
             "renewals of 300 against 200 hoarded, and Department I is 100 short. A year with too "
             "many renewals is followed by one with too few, unless Department I's output swings "
             "with them."),
            ("Taking the hoard of wear as revenue",
             "The money set aside for wear is no one's income. It is constant capital waiting to be "
             "spent, what Marx calls, of money set aside to buy means of production, &ldquo;productive "
             "capital suspended in the form of money&rdquo;. Spent on consumption, it would eat the "
             "machine."),
        ],
        "standard": (
            "Finish when you can compute the gap between renewals and wear hoarded and name the short side.",
            "Given the wear Department II hoards in money and the fixed capital it renews in kind, "
            "compute renewals less wear hoarded and state whether Department I's product is left "
            "unsold or Department I is left short, and by how much, while the value scheme still "
            "balances."
        ),
        "note": (
            "The lab takes Department II's wear and renewals as given; it does not model machines "
            "of different ages, credit or stocks, which Marx also leaves out on purpose. Its gap "
            "tile counts Department I's side of a shortfall; in Marx's own case the same shortfall "
            "leaves as much of Department II's product unsold. The 200, 100 and 300 are "
            "illustrative; the 180 is Marx's."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 2, l. 4998 (the passage). Inline: l. 4998 (simple hoard),
    # l. 5002 (not an addition to the social wealth), l. 5004 (where the buyers
    # are to come from), l. 5018 (each exclusively in one role), l. 5038 (an
    # accident), l. 5126 (overproduction in II), l. 5024 (loanable capital),
    # l. 5070 (dead weight), l. 5496 (Engels' note: latent and potential).
    {
        "slug": "accumulation-and-money",
        "title": "Accumulation in Department I and the Money It Needs",
        "module": "Chapter 21 · Accumulation and Reproduction on an Enlarged Scale",
        "one_line": "Before surplus value can become new capital it is hoarded as money, and the sales of those who hoard balance only if others are buying with money hoarded before.",
        "summary": (
            "Chapter 21 begins with the money that accumulation needs. A capitalist who means to "
            "expand sells his surplus product and keeps the money until it is large enough to "
            "invest, and while he hoards he buys nothing. Compute the surplus product left unsold, "
            "or the demand left without a product, when the capitalists of Department I who hoard "
            "and those who invest do not balance."
        ),
        "key": [
            "accumulate: sell s, hold the money",
            "the hoard: potential money-capital",
            "hoarders sell and do not buy",
            "investors buy with money hoarded before",
            "hoarders' sales − investors' buys",
        ],
        "key_label": "The hoard in five lines",
        "concepts_intro": (
            "Volume I followed accumulation in one business. Here the same act is followed through "
            "the money of a whole department, and Volume I's argument with Say's law returns."
        ),
        "concepts": [
            ("Potential money-capital",
             "Surplus value sold and laid aside to be invested is, in Kerr's translation, potential "
             "money-capital: capital by its destination, a hoard in fact. It produces nothing while "
             "it waits."),
            ("Sellers who do not buy",
             "A capitalist who is building a hoard sells his surplus product and makes no purchase "
             "against it. If every capitalist did so at once, Marx says, it would be inexplicable "
             "where the buyers were to come from."),
            ("Buyers who do not sell",
             "Another group, whose hoards are now large enough, buys means of production with money "
             "saved earlier and sells nothing against it. Balance requires the two one-sided acts "
             "to be equal in value."),
        ],
        "read_title": "The hoard first, then the buyers it needs",
        "read_intro": (
            "The chapter's first section starts with one capitalist, called A, saving up to expand. "
            "The passage follows his money."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 21, §1.</strong> &ldquo;For instance, capitalist A, "
                  "who sells during one year, or during a number of successive years, certain "
                  "quantities of commodities produced by him, thereby converts that portion of the "
                  "commodities, which bears surplus-value, the surplus-product, or, in other words, "
                  "the surplus-value produced by himself, successively into money, accumulates it "
                  "gradually, and thus makes for himself a new potential money-capital.&rdquo;"),
            ("p", "Why save up at all? Because a new machine or a new mill comes in lumps, and a "
                  "year's surplus value may not buy one. So A sells his surplus product and keeps "
                  "the money. It is potential money-capital, Marx says, because of its "
                  "&ldquo;capacity and destination&rdquo; of being converted into productive "
                  "capital, &ldquo;But practically he merely accumulates a simple hoard&rdquo;. The "
                  "word has a history: Engels notes that Marx first called such money "
                  "&ldquo;latent&rdquo;, after latent heat, and in this later manuscript borrowed "
                  "&ldquo;potential&rdquo; from potential energy. Either way the money is not new "
                  "wealth. Surplus value hoarded in money &ldquo;is not an addition to the social "
                  "wealth&rdquo;; it is money that was circulating and has stopped."),
            ("p", "The difficulty follows at once. &ldquo;Money is withdrawn from circulation and "
                  "accumulated as a hoard by the sale of commodities without a subsequent purchase. "
                  "If this operation is conceived as one taking place universally, then it seems "
                  "inexplicable where the buyers are to come from&rdquo;. And it must be conceived "
                  "so, Marx adds, since every capital may be accumulating."),
            ("p", "This is where Say's law comes in, and it deserves its full strength. Jean-Baptiste "
                  "Say argued in his <em>Treatise on Political Economy</em> of 1803 that products are "
                  "paid for with products: money is only the medium, nobody sells except in order to "
                  "buy, and so the sum of sales is the sum of purchases and a general glut is "
                  "impossible. Ricardo accepted it, and James Mill defended it. In its modern form it "
                  "says that saving is not a leak, because what one person saves another borrows and "
                  "spends on investment. If Say is right, A's hoard is a passing moment of no "
                  "consequence."),
            ("p", "The section does not name Say, but it bears on his law. Department I's capitalists are at different "
                  "stages. While A, A′ and A″ are building hoards, others, B, B′ and B″, have hoards "
                  "big enough to invest, and they buy A's surplus product with money saved earlier: "
                  "the two groups &ldquo;meet as buyers and sellers, each one of them exclusively in "
                  "one of these roles&rdquo;. The one-sided sales and the one-sided purchases cancel, "
                  "if they are equal, and nothing makes them equal. These conditions, Marx writes, "
                  "become &ldquo;so many causes of abnormal movements, implying the possibility of "
                  "crises, since a balance is an accident under the crude conditions of this "
                  "production&rdquo;."),
            ("p", "The lab takes Department I from Marx's scheme, 4,000c + 1,000v + 1,000s, and lets "
                  "it accumulate half its surplus value, 500. A share you choose of that 500 belongs "
                  "to capitalists still building hoards this year; the rest is bought by capitalists "
                  "investing older hoards. The balanced preset splits it evenly: hoarders sell 250, "
                  "investors buy 250, and the tile reads 0: hoarders' sales = investors' purchases. "
                  "The all-hoard preset has every accumulating capitalist still hoarding: +500, 500 "
                  "of surplus product unsold. The all-invest preset has every one of them spending an "
                  "old hoard and none adding to a new one: −500, 500 of demand without a product."),
            ("p", "Department II meets the same problem from the other side. If Department I keeps "
                  "500 of its surplus product to accumulate at home, only 1,500 of its `v + s` is "
                  "left to exchange against Department II's 2,000 of constant capital, and Marx "
                  "concludes: &ldquo;Hence there would be an overproduction in department II, equal "
                  "in volume to the expansion of production in department I.&rdquo; Starting to "
                  "accumulate from Marx's simple scheme is not possible without rearranging it, which "
                  "is what the next lesson's scheme does."),
            ("p", "There is an obvious way out, and Marx mentions it with an edge. Banks gather these "
                  "hoards and lend them, and &ldquo;One can understand the pleasure felt by some men "
                  "when all these potential capitals, by their concentration in the hands of "
                  "bankers, etc., by means of the credit system, become disposable, &lsquo;loanable "
                  "capital,&rsquo;&rdquo;. The standard objection to the section builds on exactly "
                  "this: in the loanable-funds view of later economics, the rate of interest moves "
                  "until what savers lay aside equals what investors borrow, and Say's law is "
                  "restored through the bank. The text here does not answer that view; it sets credit "
                  "aside and assumes metallic money. In 1936 John Maynard Keynes argued against the "
                  "loanable-funds view that saving and investment are decided by different people for "
                  "different reasons and are brought into line by changes in income and output. The "
                  "lab has no interest rate and no banks; it shows only what follows when the two "
                  "one-sided acts are unequal."),
            ("p", "While it waits, Marx says, the hoard &ldquo;is quite unproductive in its chrysalis "
                  "stage of money&rdquo;; &ldquo;It is a dead weight of capitalist "
                  "production.&rdquo; The next lesson, “Reproduction on an Enlarged Scale”, "
                  "rearranges the scheme itself so that the surplus product can be accumulated, and "
                  "runs it for four years."),
        ],
        "lab": ("capkit", {
            "mode": "schemes",
            "view": "hoard",
            "preset": "balanced",
            "presets": [
                {"id": "balanced", "label": "Marx's Department I, half of s accumulated: half hoard, half invest",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "I_accumulate_share": "1/2",
                 "hoarders_share": "1/2", "expect": {"scHoardGap": "0: hoarders' sales = investors' purchases"}},
                {"id": "all-hoard", "label": "Every accumulating capitalist still hoarding",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "I_accumulate_share": "1/2",
                 "hoarders_share": 1, "expect": {"scHoardGap": "+500: 500 of surplus product unsold"}},
                {"id": "all-invest", "label": "Every accumulating capitalist spending an old hoard",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "I_accumulate_share": "1/2",
                 "hoarders_share": 0, "expect": {"scHoardGap": "−500: 500 of demand without a product"}},
            ],
            "panel_title": "Hoarders and investors in Department I",
            "panel_intro": (
                "Department I's c, v and s, the share of s it accumulates, and the share of that "
                "belonging to capitalists still hoarding go in. The tile is the hoarders' one-sided "
                "sales less the investors' one-sided purchases."
            ),
        }),
        "steps_title": "Balancing the hoards",
        "steps_intro": "Four steps for any department in which some capitalists save up while others invest.",
        "steps": [
            ("Find the surplus product accumulated",
             "Multiply Department I's surplus value by the share accumulated. That is the surplus "
             "product that is to become new capital rather than revenue."),
            ("Split it by stage",
             "The capitalists still building hoards sell their share and buy nothing. The "
             "capitalists ready to invest buy the rest with money hoarded earlier."),
            ("Subtract",
             "Hoarders' sales less investors' purchases. Zero means the two one-sided acts cancel."),
            ("Read the sign",
             "Above zero, that much surplus product is unsold. Below zero, that much money is "
             "looking for means of production that nobody is offering."),
        ],
        "worked": {
            "title": "Everyone saves at once",
            "intro": [
                "Department I has 1,000 of surplus value and accumulates half of it. This year every "
                "accumulating capitalist is still building a hoard. You want what is left unsold.",
            ],
            "lines": [
                "accumulated:  1/2 · 1000 = 500",
                "hoarders sell:  1 · 500 = 500",
                "investors buy:  0 · 500 = 0",
                "gap:  500 − 0 = +500",
            ],
            "after": [
                "All 500 of the accumulated surplus product is offered and none of it is bought: "
                "every seller is keeping the money. With half hoarding and half investing, the same "
                "lines give 250 against 250 and nothing is left over.",
            ],
        },
        "quiz_title": "Who buys while the hoard grows",
        "quiz": [
            {"q": "Department I has s = 1,000 and accumulates half of it. This year every "
                  "accumulating capitalist is still building a hoard. What does the lab report?",
             "a": ["500 of surplus product unsold",
                   "0: sales and purchases balance",
                   "500 of demand without a product",
                   "1,000 of surplus product unsold"],
             "c": 0,
             "why": "500 is accumulated, all of it is sold by hoarders and none is bought by "
                    "investors. A balance needs investors too; demand without a product is the "
                    "all-invest case; and the 500 that is spent as revenue is not part of the "
                    "hoard."},
            {"q": "Which statement is Say's law, as this lesson states it?",
             "a": ["Every sale is a purchase, so a general glut is impossible",
                   "Every hoard is spent on consumption within the year",
                   "Surplus value is created in circulation",
                   "Saving always exceeds investment"],
             "c": 0,
             "why": "Say held that products are paid for with products and that nobody sells except "
                    "to buy. The other three are not his claims: he did not say hoards are consumed, "
                    "that surplus value arises in circulation, or that saving exceeds investment, "
                    "which would contradict his law."},
            {"q": "Half the accumulating capitalists of Department I hoard this year and half invest "
                  "money hoarded before. If the accumulated surplus product is 500, how much do the "
                  "investors buy?",
             "a": ["250", "500", "0", "125"],
             "c": 0,
             "why": "Half of 500 is 250, and they buy it with old hoards, which balances the "
                    "hoarders' 250 of sales. 500 is the whole accumulated product, 0 the all-hoard "
                    "case, and 125 a quarter."},
            {"q": "On Marx's account, is a growing hoard of potential money-capital an addition to "
                  "society's wealth?",
             "a": ["No: it is money withdrawn from circulation, the money form of a surplus product already made",
                   "Yes: every pound hoarded is new value",
                   "Yes, but only when it is held in Department II",
                   "No, because hoarding cannot occur under capitalist production"],
             "c": 0,
             "why": "Marx says surplus value hoarded in money is not an addition to the social wealth, "
                    "though it is an addition to potential money-capital. Only newly mined gold adds to "
                    "the money material; the department makes no difference; and the whole section is "
                    "about hoarding under capitalist production."},
        ],
        "mistakes": [
            ("Taking it for granted that every sale is a purchase",
             "This is Say's law, and at its strongest it is a serious argument: people sell in order "
             "to buy, money is only the medium, and what one saves another spends. The all-hoard "
             "preset shows what Marx's section turns on. When every accumulating capitalist in "
             "Department I is still building a hoard, each sells his share of the 500 of "
             "accumulated surplus product and none buys: the tile reads +500, 500 of surplus "
             "product unsold. Saving becomes investment here only when someone else is spending an "
             "older hoard at the same moment, and in the same amount."),
            ("Thinking the hoard is new wealth",
             "The money in A's hoard was circulating before, as someone's wages or someone's price. "
             "Withdrawn, it changes its function, not its quantity. Only gold newly mined adds to "
             "the money material, which is why Marx treats the gold producer as a special case."),
            ("Assuming the balance between hoarders and investors is the normal case",
             "It is the case the balanced preset is set up to show, with exactly half on each side. "
             "Nothing in the economy fixes that half. Marx calls such a balance &ldquo;an accident "
             "under the crude conditions of this production&rdquo;."),
        ],
        "standard": (
            "Finish when you can compute what is left unsold when hoarders and investors do not balance.",
            "Given Department I's surplus value, the share of it accumulated and the share of that "
            "whose owners are still hoarding, compute the hoarders' one-sided sales, the investors' "
            "one-sided purchases and the difference, and state whether surplus product is left "
            "unsold or demand is left without a product."
        ),
        "note": (
            "The lab splits Department I's accumulating capitalists into two groups by a share you "
            "choose, and assumes the investors' money was hoarded earlier; it has no credit, no "
            "interest rate and no Department II. It shows what follows when the two one-sided acts "
            "are unequal, not how often they are. Department I is Marx's; the shares are "
            "illustrative."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 2, l. 5286 (the passage). Inline: l. 5208-5214 (initial
    # diagram), l. 5147-5149 (the destination, not the quantity), l. 5218-5228
    # (year one), l. 5257-5259 (9800), l. 5290-5340 (later years; 13,033 and
    # II = 4249), l. 5348-5352 and l. 5404-5408 (second illustration), l. 5460
    # (irreconcilable; a great crash).
    {
        "slug": "extended-reproduction",
        "title": "Reproduction on an Enlarged Scale",
        "module": "Chapter 21 · Accumulation and Reproduction on an Enlarged Scale",
        "one_line": "Arrange the scheme so that Department I's wages and surplus value exceed Department II's constant capital, let Department I accumulate half its surplus value, and the economy grows only if Department II accumulates exactly what balance requires.",
        "summary": (
            "Section 3 of Chapter 21 runs Marx's schemes of accumulation year by year. Start from I "
            "4,000c + 1,000v + 1,000s and II 1,500c + 750v + 750s, let Department I accumulate half "
            "its surplus value at its own composition and Department II accumulate whatever balance "
            "requires, and compute the growth path; then give Department II too little surplus "
            "value and watch the first period refused."
        ),
        "key": [
            "I 4000c + 1000v + 1000s = 6000",
            "II 1500c + 750v + 750s = 3000",
            "I(v + s) = 2000 > IIc = 1500",
            "I accumulates half of s: 400c + 100v",
            "II adds c until it absorbs I's demand",
            "year 2: I 4400c + 1100v; II 1600c + 800v",
        ],
        "key_label": "Marx's first example in six lines",
        "concepts_intro": (
            "Accumulation needs a different arrangement of the same kind of product, and Marx finds "
            "it by working the numbers through."
        ),
        "concepts": [
            ("A different arrangement, not a bigger product",
             "Marx's first diagram of accumulation has a smaller annual product, 8,252, than his "
             "simple scheme. Enlarged reproduction does not need more value to start; it needs "
             "Department I to make more means of production for itself and fewer for Department "
             "II."),
            ("I(v + s) greater than IIc",
             "If Department I is to accumulate, part of its surplus product must stay in Department "
             "I as new constant capital, so I(v + s) must exceed IIc. Marx calls their equality "
             "irreconcilable with capitalist production."),
            ("Department II follows",
             "In Marx's examples Department I accumulates half its surplus value, and Department II "
             "accumulates whatever is needed to absorb what Department I sells it. Department II's "
             "accumulation is computed, not chosen."),
        ],
        "read_title": "The rule first, then four years of it",
        "read_intro": (
            "Marx's schemes run for pages of arithmetic. The passage is the rule he draws after the "
            "second year of it."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 21, §3.</strong> &ldquo;If things are to proceed "
                  "normally, accumulation in II must take place more rapidly than in I, because that "
                  "portion of I (v + s) which must be converted into commodities of II c, would "
                  "otherwise grow more rapidly than II c, for which it can alone be exchanged.&rdquo;"),
            ("p", "Marx starts from what he calls the initial diagram for accumulation on an "
                  "expanded scale:"),
            ("math", "I.  4000c + 1000v + 1000s = 6000"),
            ("math", "II.  1500c + 750v + 750s = 3000"),
            ("p", "The total is the same 9,000 as the simple scheme, and Department I is the same. "
                  "What has changed is Department II, and with it the balance: `I(v + s) = 2000` "
                  "against `IIc = 1500`, a gap of 500, exactly the half of Department I's surplus "
                  "value that it will keep. Marx's smaller diagram of 8,252 makes the point that "
                  "size has nothing to do with it: &ldquo;It is not the quantity, but the "
                  "destination of the given elements of simple reproduction which is changed&rdquo;."),
            ("p", "Now the first year, as Marx works it. Department I accumulates 500 of its surplus "
                  "value: 400 as new constant capital and 100 as new variable capital, keeping its "
                  "proportion of four to one. Its capitalists consume the other 500. Department I's "
                  "demand on Department II is then its 1,000 of wages, the 100 of new wages and the "
                  "500 consumed, 1,600 in all, against Department II's 1,500 of constant capital. So "
                  "Department II must add 100 to its constant capital out of its own surplus value, "
                  "and at its own proportion of two to one add 50 to its variable capital; its "
                  "capitalists consume 600 of their 750. The capitals become I 4,400c + 1,100v and II "
                  "1,600c + 800v, and at the same rate of surplus value the next year's product is I "
                  "6,600 and II 3,200: 9,800."),
            ("p", "The lab runs that rule period by period. The marx preset, with four periods, gives "
                  "I 4,400c + 1,100v; II 1,600c + 800v after the first, and the annual product grows "
                  "from 9,000 to 65,219/5, that is 13,043⅘, a growth of 20,219/45,000 or 44.93%. "
                  "Marx's own products are 9,800, 10,780, 11,858 and then 13,033: for the fourth year "
                  "he rounds off fractions, and the Kerr text's total for Department II in that year, "
                  "4,249, is ten short of its own parts, 2,129 + 1,065 + 1,065 = 4,259. After the "
                  "first year both departments grow by a tenth a year; in the first, Department II "
                  "grows by a fifteenth and Department I by a tenth."),
            ("p", "The marx-second preset is Marx's second illustration, with a higher composition, "
                  "five to one: I 5,000c + 1,000v + 1,000s and II 1,430c + 285v + 285s. Marx rounds "
                  "to whole numbers and gets I 5,417c + 1,083v and II 1,583c + 316v after the first "
                  "year; the lab keeps the fractions, and its tile reads I 16,250/3c + 3,250/3v; II "
                  "4,750/3c + 947/3v, that is 5,416⅔ and 1,083⅓, 1,583⅓ and 315⅔. The ii-short preset gives Department II a surplus value of only 100 "
                  "against Marx's 750. Balance needs Department II to accumulate 150, 100 of constant "
                  "and 50 of variable capital, and it has only 100 to accumulate from: the tiles read "
                  "refused in period 1."),
            ("p", "Marx draws two conclusions in the section's last part. Equality of `I(v + s)` and "
                  "`IIc`, the condition of simple reproduction, &ldquo;is irreconcilable with "
                  "capitalist production&rdquo;. And if the accumulation of earlier periods ever left "
                  "`IIc` greater than `I(v + s)`, the result would be an overproduction in Department "
                  "II that &ldquo;could not be compensated in any other way than by a great "
                  "crash&rdquo;."),
            ("p", "No part of Volume II has been argued over more. Mikhail Tugan-Baranovsky read these "
                  "schemes in 1894 as proof that capitalism can expand without limit whatever happens "
                  "to consumption, provided the proportions are kept: crises come from disproportion "
                  "alone. Rosa Luxemburg objected in <em>The Accumulation of Capital</em> of 1913 "
                  "that Marx makes Department II accumulate passively whatever Department I requires, "
                  "and asked who buys the growing product. Workers can buy only what their wages "
                  "pay for, and capitalists who accumulate are by definition not consuming the "
                  "surplus value they accumulate; so, she argued, the part of the surplus product "
                  "that is to become new capital can be sold only to buyers outside capitalist "
                  "production. Otto Bauer answered her with a scheme of his own "
                  "the same year, and Nikolai Bukharin in 1924. All of them wrote after Marx's death "
                  "in 1883. What in the chapter bears on their dispute is the rule this lesson "
                  "opened with: Marx states what accumulation in Department II must do &ldquo;If "
                  "things are to proceed normally&rdquo;, and his figures show that it can, but the "
                  "chapter does not show what makes it do so. The lab takes the rule as given, "
                  "Department II following Department I, which is exactly the step Luxemburg "
                  "disputed."),
            ("p", "Volume II ends a few pages later, where the manuscript does, on where Department "
                  "II's money comes from. The next course, Cost Price and the Rate of Profit, opens "
                  "Volume III, where the c, v and s of these schemes are measured against the whole "
                  "capital advanced, and surplus value appears as profit."),
        ],
        "lab": ("capkit", {
            "mode": "schemes",
            "view": "expanded",
            "periods": 4,
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's first illustration: I 4,000c + 1,000v + 1,000s; II 1,500c + 750v + 750s",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 1500, "v": 750, "s": 750},
                 "I_accumulate_share": "1/2", "expect": {"scBalance": "I(v + s) = 2,000, IIc = 1,500: gap +500", "scYear2": "I 4,400c + 1,100v; II 1,600c + 800v", "scGrowth": "9,000 to 65,219/5: 20,219/45,000 = 44.93%"}},
                {"id": "marx-second", "label": "Marx's second illustration: composition 5 to 1",
                 "I": {"c": 5000, "v": 1000, "s": 1000}, "II": {"c": 1430, "v": 285, "s": 285},
                 "I_accumulate_share": "1/2", "composition_I": 5, "composition_II": 5, "expect": {"scBalance": "I(v + s) = 2,000, IIc = 1,430: gap +570", "scYear2": "I 16,250/3c + 3,250/3v; II 4,750/3c + 947/3v", "scGrowth": "9,000 to 2,690,893/216: 746,893/1,944,000 = 38.42%"}},
                {"id": "ii-short", "label": "Department II's s cut to 100",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 1500, "v": 750, "s": 100},
                 "I_accumulate_share": "1/2", "expect": {"scBalance": "I(v + s) = 2,000, IIc = 1,500: gap +500", "scYear2": "refused in period 1", "scGrowth": "refused in period 1"}},
            ],
            "panel_title": "The enlarged scheme, period by period",
            "panel_intro": (
                "Both departments' c, v and s and the share of s Department I accumulates go in. "
                "Department II's accumulation is computed to balance the exchange. The table gives "
                "every period; the tiles give the first period and the growth over all four."
            ),
        }),
        "steps_title": "Running one period of accumulation",
        "steps_intro": "Four steps, Marx's rule for his first example.",
        "steps": [
            ("Split Department I's accumulation",
             "Take the share of Department I's surplus value it accumulates and divide it between "
             "constant and variable capital at Department I's composition."),
            ("Find Department I's demand on Department II",
             "Add Department I's variable capital, its new variable capital and the surplus value its "
             "capitalists consume. All of it must be spent on means of consumption."),
            ("Balance Department II",
             "Department II's constant capital must rise to that demand. Add the difference to IIc "
             "and add variable capital at Department II's composition. Both come out of IIs."),
            ("Check and roll forward",
             "If Department II's accumulation exceeds its surplus value, the period is impossible. "
             "Otherwise the new capitals, at the same rates of surplus value, give next year's "
             "product."),
        ],
        "worked": {
            "title": "Marx's first year of accumulation",
            "intro": [
                "Start from Marx's initial diagram. You want both departments' capital after one "
                "year and the next year's product.",
            ],
            "lines": [
                "I accumulates:  1/2 · 1000 = 500 = 400c + 100v",
                "I's demand on II:  1000 + 100 + 500 = 1600",
                "II adds:  1600 − 1500 = 100c, and 50v",
                "capitals:  I 4400c + 1100v; II 1600c + 800v",
                "next product:  6600 + 3200 = 9800",
            ],
            "after": [
                "Department II accumulates 150 of its 750, a fifth; Department I accumulates half. "
                "Give Department II a surplus value below 150 and this year cannot balance.",
            ],
        },
        "quiz_title": "How the departments must grow",
        "quiz": [
            {"q": "Starting from I 4000c + 1000v + 1000s and II 1500c + 750v + 750s, Department I "
                  "accumulates half its s at four to one. How much must Department II add to its "
                  "constant capital for the first year to balance?",
             "a": ["100", "500", "50", "150"],
             "c": 0,
             "why": "Department I's demand on Department II is 1,000 + 100 + 500 = 1,600 against IIc of "
                    "1,500, so Department II adds 100. 500 is Department I's accumulation, 50 is "
                    "Department II's added variable capital, and 150 is its whole accumulation."},
            {"q": "What is the annual product at the end of Marx's first year of accumulation?",
             "a": ["9,800", "9,000", "8,252", "10,780"],
             "c": 0,
             "why": "I 4,400c + 1,100v + 1,100s = 6,600 and II 1,600c + 800v + 800s = 3,200 make "
                    "9,800. 9,000 is the starting product, 8,252 Marx's smaller diagram, and 10,780 "
                    "the product a year later."},
            {"q": "Why must I(v + s) exceed IIc if Department I is to accumulate?",
             "a": ["Part of Department I's surplus product must stay in Department I as additional constant capital",
                   "Department I's workers must consume more than Department II's",
                   "Department II must shrink for Department I to grow",
                   "Department I's rate of surplus value must be higher than Department II's"],
             "c": 0,
             "why": "What Department I accumulates as constant capital cannot also be exchanged for "
                    "means of consumption, so I(v + s) must exceed what goes to Department II. The "
                    "scheme needs no difference in consumption or in rates of surplus value, and "
                    "Department II grows too."},
            {"q": "In the ii-short preset Department II's surplus value is 100. Why is the first "
                  "period refused?",
             "a": ["Balance needs Department II to accumulate 150, more than its whole surplus value",
                   "Department I cannot accumulate at four to one",
                   "Department II's composition is too high",
                   "The scheme already balances without accumulation"],
             "c": 0,
             "why": "Department II must add 100 of constant and 50 of variable capital to absorb "
                    "Department I's demand, and 150 exceeds its 100 of surplus value. Department I's "
                    "accumulation is unaffected, Department II's composition is Marx's two to one, "
                    "and I(v + s) = 2,000 against IIc = 1,500 does not balance by itself."},
        ],
        "mistakes": [
            ("Thinking the two departments can grow at any rates they like",
             "Each department's capitalists decide their own investment, so it seems the rates could "
             "be anything. Marx's arithmetic says otherwise. Once Department I accumulates half its "
             "surplus value, Department II's accumulation is fixed by the balance, 100 of constant "
             "and 50 of variable capital in the first year. The ii-short preset gives Department II "
             "a surplus value of 100; balance needs 150, and the tiles read refused in period 1. "
             "After the first year, in Marx's example, both departments must grow at the same "
             "rate, a tenth a year."),
            ("Expecting enlarged reproduction to need a larger product",
             "Marx's diagram of accumulation has a smaller product, 8,252, than his simple scheme. "
             "What makes a scheme one of accumulation is that I(v + s) exceeds IIc; in the initial "
             "diagram the 500 of surplus means of production is the material of next year's "
             "growth."),
            ("Reading Marx's rounded figures as exact",
             "Marx rounds off fractions in the fourth year, and one printed sum carries a slip. "
             "The lab keeps every fraction, so its fourth-year product, 13,043⅘, differs from the "
             "13,033 Kerr prints; the exact figure is the one that follows from the rule."),
        ],
        "standard": (
            "Finish when you can run a two-department scheme of accumulation and compute its growth.",
            "Given c, v and s for both departments and the share of surplus value Department I "
            "accumulates, compute Department I's additions at its composition, the additions to "
            "Department II's capital that balance the exchange, both departments after the first "
            "period and the growth of the annual product over the periods, and state when "
            "Department II's surplus value is too small for balance."
        ),
        "note": (
            "The lab follows Marx's first example: Department I accumulates a fixed share at its own "
            "composition, and Department II accumulates whatever balances the exchange, with rates "
            "of surplus value unchanged. That rule is Marx's assumption, and whether Department II "
            "can be relied on to follow is what Luxemburg and others disputed. The marx and "
            "marx-second figures are Marx's; ii-short changes one figure."
        ),
    },
]
