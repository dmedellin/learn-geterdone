"""Revenues and Their Sources, lessons 1-5 -- Volume III, Part VII, Chapters 48-52, one lesson per chapter.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, a drop capital ("CAPITAL") is printed as an ordinary capital,
and the translator's double quotation marks inside a quotation are printed as
single curly quotes. Marx's dashes in the trinity formula are printed as
em dashes. Nothing else is changed.

The module names keep Untermann's chapter titles, as PLAN §E.3 requires ("The
Trinitarian Formula", "The Semblance of Competition"); the lesson titles are
the ones PLAN §C gives.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 3, l. 6924 and l. 6926 (the formula and its reduction);
    # l. 7028 (Mister Capital and Mistress Land). Inline: l. 6926 (profit of
    # enterprise as wages), l. 6930 (lawyer's fees), l. 6932 and l. 6936-6938
    # (capital, land, labour), l. 6978-6980 (three trees; the substance),
    # l. 7008 (Roscher), l. 7030 (classical economy), l. 7737 (footnote 144,
    # three fragments), l. 6984 (missing folio), l. 6952 (stops short),
    # l. 7741 (footnote 146, Smith).
    {
        "slug": "the-trinity-formula",
        "title": "The Trinity Formula",
        "module": "Chapter 48 · The Trinitarian Formula",
        "one_line": "Capital earns interest, land earns rent, labour earns wages: Marx takes the formula apart and finds three shares of one value product.",
        "summary": (
            "Chapter 48 sets out the formula in which every income seems to grow from its own "
            "source, and argues that wages, interest, profit of enterprise and rent are parts of "
            "one value product made by the year's labour. Decompose a value product of £200 into "
            "its four revenues, take the landlord away or make the capitalist borrow every pound, "
            "and see the parts move while the whole stays put."
        ),
        "key": [
            "capital–interest, land–rent, labour–wages",
            "value product = v + s",
            "wages = v",
            "s = rent + interest + profit of enterprise",
            "the parts move; v + s does not",
        ],
        "key_label": "The trinity in five lines",
        "concepts_intro": (
            "The chapter is three fragments that Engels found in different places of the "
            "manuscript, and it reads like it. Three ideas hold the fragments together."
        ),
        "concepts": [
            ("The trinity formula",
             "Capital yields interest, land yields rent, labour yields wages. Each income appears "
             "as the fruit of its own source, as regularly as a tree bears fruit, and so it can be "
             "consumed every year without using the source up."),
            ("Three sources from three worlds",
             "Capital is a social relation that shows itself in things; land is a piece of nature; "
             "labour, taken by itself, is an abstraction. Their supposed products, the three "
             "revenues, are all one kind of thing: quantities of value."),
            ("One value product, divided",
             "On the chapter's accounting the year's new labour makes a value product, v + s. "
             "Wages are v; rent, interest and profit of enterprise are parts of s. Ownership "
             "decides who receives each part. It does not create the part."),
        ],
        "read_title": "The formula, then the fragments one by one",
        "read_intro": (
            "The chapter opens by stating the formula and at once rewriting it in the form its "
            "defenders prefer. The rest of it is Marx explaining why that form is the one that "
            "hides the most."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 48.</strong> &ldquo;Capital&mdash;Profit (Profit of "
                  "Enterprise plus Interest), Land&mdash;Ground-Rent, Labor&mdash;Wages, this is the "
                  "trinitarian formula which comprises all the secrets of the social process of "
                  "production. &hellip; the above trinitarian formula reduces itself more "
                  "specifically to the following: Capital&mdash;Interest, Land&mdash;Ground-Rent, "
                  "Labor&mdash;Wages. Here profit, the specific mark characterizing the form of "
                  "surplus-value belonging to the capitalist mode of production, is happily "
                  "eliminated.&rdquo;"),
            ("p", "Think about the incomes you know. A wage is paid for work. Money in a savings "
                  "account earns interest, and the more money, the more interest. A flat let to a "
                  "tenant earns rent, and a bigger flat earns more. Each income seems to come from "
                  "its own source and to be in proportion to it, and you can spend it every year "
                  "without touching the source. Marx's phrase for that is that the revenues are "
                  "&ldquo;like the annually consumable fruits of a perennial tree, or rather of "
                  "three trees&rdquo;. The trinity formula is that picture, written as economics."),
            ("p", "This is the last Part of the last volume, and the text is rough. Engels notes "
                  "that the chapter is made of three fragments found in different places of the "
                  "manuscript, and the Kerr text marks one gap, where &ldquo;one folio sheet of the "
                  "manuscript is missing&rdquo;, and one place where the manuscript &ldquo;stops "
                  "short&rdquo; in mid-argument. What survives is an argument with a clear shape, "
                  "and the lessons in this course read it as Engels printed it."),
            ("p", "Go back to the passage. In the first version capital yields profit, made of "
                  "profit of enterprise plus interest. Then the formula shrinks: interest stands "
                  "for capital's fruit, because profit of enterprise now &ldquo;distinguishes "
                  "itself from interest by appearing as wages independent of capital&rdquo;, a "
                  "reward for the capitalist's work of managing. That is the point of "
                  "&ldquo;happily eliminated&rdquo;. Profit is the category that still points back "
                  "to the factory where surplus labour is done. Interest points to nothing but the "
                  "sum lent, which is why the formula's defenders like it best."),
            ("p", "Then Marx looks at the three sources and finds that they have nothing in "
                  "common: &ldquo;They have about the same relation to each other as lawyer's fees, "
                  "carrots, and music.&rdquo; Capital, he says, is not a set of tools, because "
                  "&ldquo;capital is not a thing&rdquo;: a spindle is capital only where it is owned "
                  "by one class and worked by another. Land is a piece of nature, and "
                  "&ldquo;Value is labor. Therefore surplus-value cannot be land.&rdquo; Labour taken "
                  "by itself, outside any society, is &ldquo;a mere ghost, &lsquo;Labor,&rsquo; a "
                  "mere abstraction&rdquo;. Yet the three supposed fruits, interest, rent and "
                  "wages, are all quantities of the same thing, value, and can be added together. "
                  "Three incomparable sources, one comparable product: that mismatch is the clue."),
            ("p", "The formula has a long history. Adam "
                  "Smith wrote, in a sentence Marx quotes, that &ldquo;Wages, profit, and rent are "
                  "the three original sources of all revenue, as well as of all exchangeable "
                  "value&rdquo;. Jean-Baptiste Say, the French economist whose <em>Treatise</em> of "
                  "1803 made Smith's ideas a system, went further: labour, capital and land each "
                  "render a productive service, and each income is the price of a service. The "
                  "German historical economist Wilhelm Roscher, whom Marx names, held that profit "
                  "comes from the means of production and &ldquo;rent from the earth, or nature, "
                  "represented by the landlord&rdquo;."),
            ("p", "The modern version is the one most economists hold. John "
                  "Bates Clark, in <em>The Distribution of Wealth</em> of 1899, argued that under "
                  "competition each factor is paid its marginal product: what the last worker, the "
                  "last machine or the last acre adds to output. Philip Wicksteed had shown in 1894 "
                  "that, where doubling every input doubles output, paying each factor its marginal "
                  "product uses up the whole product exactly, with nothing left over. On that "
                  "account the trinity is no illusion at all: land and capital really are "
                  "productive, and their owners are paid for what they contribute. Most economists "
                  "teach some form of it today. In the 1950s and 1960s Joan Robinson and Piero "
                  "Sraffa at Cambridge argued that capital cannot be measured as a quantity apart "
                  "from the rate of profit, so its marginal product for a whole economy is not well "
                  "defined, and Paul Samuelson conceded their technical point in 1966. Most "
                  "economists still use the marginal theory, and this Subject does not settle it."),
            ("p", "Marx died long before Clark wrote, and the chapter does not reply to him. What "
                  "bears on Clark's account is how narrow the chapter's own claim is. Marx does not deny that land and "
                  "machines are needed to make wheat and yarn. He claims that they help to make "
                  "the use-value and not the value, and that ownership fixes a portion of the "
                  "value product as rent or interest &ldquo;without, however, creating the "
                  "substance itself, which is transformed into these different categories&rdquo;."),
            ("p", "The lab takes that account and computes with it. In the english preset, an "
                  "illustrative capital of £100 of means of production and £100 of wages makes a "
                  "product worth `£100 + £100 + £100 = £300`, so the value product is "
                  "`v + s = £200`. Wages are £100. Of the £100 of surplus value, rent takes 3/10, "
                  "£30; interest takes 1/5, £20, because the capitalist borrowed half his capital; "
                  "profit of enterprise is the remaining £50. In the no-landlord preset the farmer "
                  "owns his land: rent is £0 and profit of enterprise £80, and the land is exactly "
                  "as fertile as before. In the all-borrowed preset every pound of the capital is "
                  "borrowed on the same terms, interest doubles to £40 and profit of enterprise "
                  "falls to £30, though no machine or worker does anything different. In all three "
                  "the four tiles add up to £200."),
            ("p", "That is the chapter's arithmetic in one line: the shares follow titles of "
                  "ownership, and the sum does not move. A marginal-productivity economist would "
                  "read the same tiles differently, as the land's product passing to its new owner "
                  "in the no-landlord preset. The tiles cannot choose between the readings; they "
                  "can only show that on Marx's definitions the four revenues are one £200 "
                  "divided, not three products added."),
            ("p", "<strong>Volume III, Chapter 48.</strong> &ldquo;It is an enchanted, perverted, "
                  "topsy-turvy world, in which Mister Capital and Mistress Land carry on their "
                  "goblin tricks as social characters and at the same time as mere things.&rdquo;"),
            ("p", "Marx is enjoying himself, and he means it. In the German edition the pair are "
                  "Monsieur le Capital and Madame la Terre, in French, a couple out of a fairy tale, and the joke carries the "
                  "argument: a social relation has been given the body of a thing, and a thing has "
                  "been given the manners of a person. He credits the classical economists, Smith "
                  "and above all Ricardo, with having seen through this, &ldquo;by reducing "
                  "interest to a portion of profit, and rent to the surplus above the average "
                  "profit, so that both of them meet in surplus-value&rdquo;, and he adds that even "
                  "they stayed partly inside the illusion they had taken apart."),
            ("p", "The revenues are spent, every year, on a product worth more than the revenues "
                  "add up to: £300 of product against £200 of income. The next lesson, "
                  "“Concerning the Analysis of the Process of Production”, asks how that can be."),
        ],
        "lab": ("capkit", {
            "mode": "revenue",
            "view": "trinity",
            "money_unit": "£",
            "preset": "english",
            "presets": [
                {"id": "english", "label": "Illustrative: £100c + £100v + £100s, half the capital borrowed",
                 "c": 100, "v": 100, "s": 100, "split": {"interest": "1/5", "rent": "3/10"},
                 "expect": {"rvTotal": "£300", "rvWages": "£100", "rvRent": "£30", "rvInterest": "£20", "rvProfitShare": "£50"}},
                {"id": "no-landlord", "label": "The farmer owns his land: no rent",
                 "c": 100, "v": 100, "s": 100, "split": {"interest": "1/5", "rent": 0},
                 "expect": {"rvWages": "£100", "rvRent": "£0", "rvInterest": "£20", "rvProfitShare": "£80"}},
                {"id": "all-borrowed", "label": "Every pound of the capital borrowed",
                 "c": 100, "v": 100, "s": 100, "split": {"interest": "2/5", "rent": "3/10"},
                 "expect": {"rvWages": "£100", "rvRent": "£30", "rvInterest": "£40", "rvProfitShare": "£30"}},
            ],
            "panel_title": "One value product, four revenues",
            "panel_intro": (
                "The value parts of a year's product go in, with the shares of surplus value that "
                "go as interest and as rent. The lab gives the product's value and the four "
                "revenues. Step through the presets and add the four revenue tiles each time."
            ),
        }),
        "steps_title": "Resolving the value product into revenues",
        "steps_intro": "Four steps, the same for any product whose value parts are given.",
        "steps": [
            ("Find the value product",
             "The product's value is c + v + s. Set c aside: it replaces means of production used "
             "up. The value product the year's labour added is v + s."),
            ("Pay the wages",
             "Wages are the variable capital, v. They are a revenue for the worker and a part of "
             "the value product, not an addition to it."),
            ("Divide the surplus value",
             "Rent and interest are each a share of s, fixed by the landlord's and the lender's "
             "titles. Multiply s by each share."),
            ("Take the remainder and check",
             "Profit of enterprise is s minus rent minus interest. Add the four revenues: they "
             "must return v + s exactly."),
        ],
        "worked": {
            "title": "Two hundred pounds in four parts",
            "intro": [
                "Take the english preset. The product is £100 of means of production, £100 of "
                "wages and £100 of surplus value; rent takes 3/10 of s and interest 1/5. You want "
                "the four revenues and their sum.",
            ],
            "lines": [
                "value product:  v + s = 100 + 100 = £200",
                "wages:  v = £100",
                "rent:  3/10 · 100 = £30",
                "interest:  1/5 · 100 = £20",
                "profit of enterprise:  100 − 30 − 20 = £50",
                "sum:  100 + 30 + 20 + 50 = £200",
            ],
            "after": [
                "The £100 of c is in the product's value, £300, and in nobody's revenue. In the "
                "no-landlord preset rent is £0 and profit of enterprise £80; in all-borrowed "
                "interest is £40 and profit of enterprise £30. The sum is £200 every time.",
            ],
        },
        "quiz_title": "Three revenues, one value product",
        "quiz": [
            {"q": "A value product of £200 is made of £100 of wages and £100 of surplus value. "
                  "Rent takes 3/10 of s and interest 1/5. What is the profit of enterprise?",
             "a": ["£50", "£70", "£100", "£30"],
             "c": 0,
             "why": "`100 − 30 − 20 = 50`. £70 is interest and profit of enterprise together, s "
                    "after rent. £100 is the whole of s, and £30 is the rent."},
            {"q": "In the no-landlord preset the farmer owns his land and pays no rent. What "
                  "happens to the £30 that was rent?",
             "a": ["It disappears, and the value product falls to £170",
                   "It goes to the workers as higher wages",
                   "It stays in the value product of £200 and lands in profit of enterprise",
                   "It is added on top, and the value product rises to £230"],
             "c": 2,
             "why": "The land and the labour are unchanged, so the value product is still £200; "
                    "profit of enterprise rises from £50 to £80. Wages are fixed at v, £100, by "
                    "the value of labour-power, not by who owns the land."},
            {"q": "In the reduced formula Capital–Interest, Land–Ground-Rent, Labour–Wages, which "
                  "category does Marx say is &ldquo;happily eliminated&rdquo;?",
             "a": ["Ground-rent", "Profit", "Wages", "Interest"],
             "c": 1,
             "why": "Interest takes profit's place as capital's fruit, and profit of enterprise "
                    "is reinterpreted as the capitalist's wages. Profit is the category that "
                    "still points back to surplus labour, which is why its disappearance is the "
                    "point of the remark. Rent, wages and interest all stay in the formula."},
            {"q": "On J. B. Clark's marginal-productivity theory, what is each factor of "
                  "production paid, under competition?",
             "a": ["A share of a value produced by labour alone",
                   "What the last unit of it adds to output",
                   "Its average product: output divided by the quantity of the factor",
                   "Whatever its owner's bargaining power secures, with no tie to output"],
             "c": 1,
             "why": "Clark's claim is that each factor earns its marginal product. The first "
                    "option is Marx's account, not Clark's. The average product is not the "
                    "marginal one, and Clark's theory ties pay to output rather than to "
                    "bargaining."},
        ],
        "mistakes": [
            ("Thinking each factor of production creates its own income",
             "This is Say's three productive services and, in its modern form, Clark's marginal "
             "productivity, and on those accounts it is no mistake. On the chapter's definitions "
             "it is: the four revenues are parts of one value product, v + s, and do not add "
             "independent amounts to it. The presets show it. With the landlord gone, rent falls "
             "from £30 to £0 and profit of enterprise rises from £50 to £80; with all the capital "
             "borrowed, interest rises to £40. The sum stays at £200 in every case."),
            ("Taking interest as capital's fruit and profit of enterprise as the capitalist's wage",
             "The formula's tidiest version makes interest the product of capital and profit of "
             "enterprise the pay for managing it. In the all-borrowed preset nobody manages "
             "anything differently, yet interest goes from £20 to £40 and profit of enterprise "
             "from £50 to £30. On Marx's reading both are shares of one surplus value, and the "
             "split between them follows who owns the money."),
            ("Confusing what land helps make with what rent is",
             "Land helps to grow wheat, a use-value. Rent is a quantity of exchange value, a "
             "share of s. Marx's point is that the two cannot be measured against each other: a "
             "more fertile acre yields more bushels for the same labour, but not more value for "
             "that labour."),
        ],
        "standard": (
            "Finish when you can resolve a value product into the four revenues.",
            "Given the value parts c, v and s of a product and the shares of s that go as rent "
            "and interest, compute wages, rent, interest and profit of enterprise, and show that "
            "they sum to v + s whatever the shares."
        ),
        "note": (
            "The lab assumes the chapter's accounting, on which the value product v + s is made "
            "by the year's labour and the revenues are its parts. On the marginal-productivity "
            "account the same four figures are payments for four productive contributions, and "
            "nothing in the arithmetic decides between the two readings; that is the oldest "
            "dispute about this book. The figures are illustrative; the chapter gives none."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 3, l. 7060-7062 (the question). Inline: l. 7092-7094 (the
    # scheme), l. 7096 (chosen at random), l. 7108-7110 (gross and net income),
    # l. 7114 (Say), l. 7743 (footnote 147, Ricardo on Say), l. 7745
    # (footnote 148, Smith's horse), l. 7117 (revenue for one, capital for
    # another), l. 7127 (four with three), l. 7154 (productively consumed).
    # Vol. 2, l. 5210-5214 (the initial diagram for accumulation).
    {
        "slug": "analysis-of-the-process-of-production",
        "title": "Concerning the Analysis of the Process of Production",
        "module": "Chapter 49 · A Contribution to the Analysis of the Process of Production",
        "one_line": "A year's revenues add up to v + s, yet they buy a product worth c + v + s; Volume II's scheme shows where the c comes from.",
        "summary": (
            "If wages, profit and rent are the whole of the value a year's labour adds, how can "
            "they buy a year's product, which also contains the value of the means of production "
            "used up? Marx answers with the reproduction scheme of Volume II. Compute, on his "
            "figures, the 4,000 of means of production that are replaced inside Department I and "
            "are never anyone's revenue."
        ),
        "key": [
            "annual product = c + v + s",
            "annual revenue = v + s",
            "I(v + s) buys IIc",
            "Ic is replaced within Department I",
            "income is a third of Marx's product",
        ],
        "key_label": "The product and the income",
        "concepts_intro": (
            "Chapter 49 returns to a problem Volume II solved, because the revenues now have "
            "their names. Three ideas carry it."
        ),
        "concepts": [
            ("Product and revenue",
             "The year's product is worth c + v + s. The year's labour added only v + s, and that "
             "is all that becomes wages, profit and rent. The c was transferred from means of "
             "production used up, and must be replaced."),
            ("The two departments",
             "Department I makes means of production, Department II means of consumption. "
             "Department I's revenues buy Department II's constant capital in kind, and "
             "Department I's own constant capital is replaced inside Department I."),
            ("Gross and net",
             "Gross output is the whole product. Gross income is wages plus profit plus rent; net "
             "income is profit plus rent. A nation's income is its gross income, not its gross "
             "output."),
        ],
        "read_title": "The question, then Volume II's answer",
        "read_intro": (
            "Marx states the difficulty in two questions near the start of the chapter. The "
            "answer is a scheme the reader has met before, now read for what it says about "
            "income."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 49.</strong> &ldquo;Its value is therefore equal "
                  "to wages plus profit plus rent plus C (its constant portion of value). How can "
                  "an annually produced value, which equals only wages plus profit plus rent, buy "
                  "a product which has a value of wages plus profit plus rent plus C? How can the "
                  "annually produced value buy a product, which has a higher value than its "
                  "own?&rdquo;"),
            ("p", "Every year a government announces a figure for national income, and every "
                  "year the shops, farms and factories turn out a product. It seems obvious that "
                  "the two should match: what everyone earns is what everyone can buy. Marx's "
                  "two questions say they cannot. The year's labour adds v + s, and that is all "
                  "that becomes wages, profit and rent. The year's product also carries C, the "
                  "value of the cotton, coal and wear it used up. Income is smaller than product, "
                  "and the gap has to be made up from somewhere."),
            ("p", "He sets the problem up with care. Prices of production can be ignored here, "
                  "because for the whole social product they add up to its value. Profit and "
                  "rent together are the surplus value, and wages are the variable capital. So "
                  "the year's new value is v + s and nothing more. There are two difficulties, "
                  "he says: who pays for C, out of what, and who does the labour that replaces "
                  "it? He answers that Volume II, Part III has already solved them, and that he "
                  "returns to the problem now for two reasons. Surplus value has since been split "
                  "into profit, interest and rent, and the formula of the three revenues is tied "
                  "to an error that has run through political economy since Adam Smith."),
            ("p", "The answer is the scheme of simple reproduction from Volume II, Chapter 20, "
                  "which Marx copies out:"),
            ("math", "I:  4000c + 1000v + 1000s = 6000"),
            ("math", "II:  2000c + 500v + 500s = 3000"),
            ("p", "Read it the way the chapter does. Department II's workers, capitalists and "
                  "landlords spend their `500v + 500s` on Department II's own consumer goods. "
                  "Department I's revenue, `1000v + 1000s`, cannot be eaten in its own form, "
                  "which is machines and iron, so it buys the other `2000c` of consumer goods, and "
                  "Department II takes the machines and iron in return as the replacement of its "
                  "constant capital. That leaves Department I's own `4000c`, which is replaced out "
                  "of its own product, by capitalists of Department I selling to one another or "
                  "using their own product again. "
                  "Marx adds that &ldquo;It should be noted that these numbers have been chosen at "
                  "random&rdquo;; what is not random is that I(v + s) must equal IIc."),
            ("p", "The lab runs that scheme in its marx preset. Of 9,000 of annual product, the "
                  "tile says 4,000 is exchanged within Department I, and the balance tile prints "
                  "`I(v + s) = 2,000 = IIc`. The revenue of the whole society is "
                  "`2,000 + 1,000 = 3,000`, a third of the product. The other two thirds are "
                  "constant capital, and 4,000 of them never pass through anyone's hands as "
                  "income at all."),
            ("p", "The growing preset uses Marx's starting point for accumulation in Volume II, "
                  "Chapter 21: Department I unchanged, Department II at `1500c + 750v + 750s`. Now "
                  "I(v + s) is 2,000 and IIc only 1,500, and the lab reports 500 of Department "
                  "I's product unsold to Department II. In Volume II that 500 is Department I's "
                  "accumulation: surplus value, a revenue in form, existing as means of "
                  "production. Chapter 49 makes the same point: of the newly created value, "
                  "&ldquo;some of it must be productively consumed&rdquo;. The one-sector preset "
                  "removes Department I altogether, which is the world the error assumes, and the "
                  "balance fails at once: Department II's 2,000 of constant capital has nothing to "
                  "be replaced with."),
            ("p", "Marx then separates gross from net. Gross "
                  "output is the whole product. Gross income is wages plus profit plus rent. Net "
                  "income is profit plus rent. An individual capitalist counts wages as a cost and "
                  "calls only his profit income; the nation's income is its gross income, all three "
                  "revenues, but not its gross output."),
            ("p", "Here is the error. Adam Smith argued that the price of every commodity "
                  "resolves, in the end, into wages, profit and rent. Smith's reasoning runs like this: the "
                  "farmer's horse looks like a fourth part of the price of corn, but Smith replies "
                  "that &ldquo;the price of any instrument of husbandry, such as a labouring horse, "
                  "is itself made up of the same three parts&rdquo;, and so on back. Say concluded "
                  "that a nation's gross product and its net income are the same thing, which Marx "
                  "calls &ldquo;the dream of men like Say&rdquo;. Ricardo had already answered "
                  "Say in one line: &ldquo;Take a whole from a whole and nothing remains.&rdquo;"),
            ("p", "Marx's own diagnosis is that the error is made by looking at one capital at a "
                  "time. The weaver's yarn is the spinner's revenue, so it seems that constant "
                  "capital is only revenue looked at from another side. &ldquo;The phrase that a "
                  "thing is revenue for one man and capital for another saves all further "
                  "thought.&rdquo; Added up over the whole society, though, the riddle comes back: "
                  "&ldquo;How can they buy a value of four with a value of three?&rdquo; The scheme "
                  "answers it. They do not buy it all; 4,000 is bought and sold among the "
                  "capitalists of Department I and never meets a consumer."),
            ("p", "Modern national accounts draw the same line between product and income. "
                  "They subtract intermediate consumption from gross output to reach "
                  "value added, and subtract the wear of fixed capital to reach net product. "
                  "Wassily Leontief, whose input–output tables of 1941 trace each industry's "
                  "purchases from every other, named Quesnay's <em>Tableau</em> as their ancestor. "
                  "What remains in dispute is the previous lesson's question, whether value added "
                  "is made by labour alone, not whether income and product differ."),
            ("p", "Income, then, is a part of the product. Yet a price still looks like wages, "
                  "profit and rent added together. The next lesson, “Illusions Created by "
                  "Competition”, asks why it looks that way."),
        ],
        "lab": ("capkit", {
            "mode": "schemes",
            "view": "simple",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: I 4,000c + 1,000v + 1,000s; II 2,000c + 500v + 500s",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 2000, "v": 500, "s": 500},
                 "expect": {"scWithinI": "4,000", "scBalance": "I(v + s) = 2,000 = IIc"}},
                {"id": "growing", "label": "Marx's start for accumulation: II 1,500c + 750v + 750s",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "II": {"c": 1500, "v": 750, "s": 750},
                 "expect": {"scWithinI": "4,000", "scBalance": "I(v + s) = 2,000, IIc = 1,500: gap +500", "scIExchange": "1,500 each way; 500 of Department I's product unsold"}},
                {"id": "one-sector", "label": "No Department I: consumer goods only",
                 "I": {"c": 0, "v": 0, "s": 0}, "II": {"c": 2000, "v": 500, "s": 500},
                 "expect": {"scWithinI": "0", "scBalance": "I(v + s) = 0, IIc = 2,000: gap −2,000"}},
            ],
            "panel_title": "The annual product and the annual revenue",
            "panel_intro": (
                "Each department's constant capital, variable capital and surplus value go in. The "
                "lab balances the exchange between the departments and gives the part of "
                "Department I's product that is exchanged within Department I. Compare that tile "
                "with the whole product in the status line."
            ),
        }),
        "steps_title": "Separating the product from the income",
        "steps_intro": "Four steps for any two-department scheme of simple reproduction.",
        "steps": [
            ("Total the product",
             "Add c + v + s in each department and add the two departments. That is the annual "
             "product, gross output."),
            ("Total the revenue",
             "Add v + s in each department. That is wages plus profit plus rent, the gross income, "
             "and it is spent on Department II's product."),
            ("Balance the exchange",
             "Department I's v + s buys Department II's c. Compare I(v + s) with IIc: equal, the "
             "scheme reproduces itself; unequal, part of one department's product finds no buyer."),
            ("Find what no one receives",
             "Department I's c is replaced within Department I. It is part of the product and of "
             "no one's revenue."),
        ],
        "worked": {
            "title": "Nine thousand of product, three thousand of income",
            "intro": [
                "Take Marx's scheme. You want the annual product, the annual revenue, and the part "
                "of the product that is never anyone's revenue.",
            ],
            "lines": [
                "product:  6000 + 3000 = 9000",
                "revenue:  I(1000 + 1000) + II(500 + 500) = 3000",
                "exchange:  I(v + s) = 2000 = IIc",
                "within Department I:  Ic = 4000",
                "constant capital:  4000 + 2000 = 6000",
            ],
            "after": [
                "Income is 3,000 of 9,000. Department II's 2,000 of constant capital is replaced by "
                "Department I's revenue, and Department I's 4,000 is replaced inside Department I, "
                "where no consumer buys it.",
            ],
        },
        "quiz_title": "Product, revenue and the part between",
        "quiz": [
            {"q": "In Marx's scheme, I 4,000c + 1,000v + 1,000s and II 2,000c + 500v + 500s, how "
                  "much of the annual product is exchanged within Department I and is never "
                  "anyone's revenue?",
             "a": ["2,000", "4,000", "3,000", "6,000"],
             "c": 1,
             "why": "Department I's own constant capital, 4,000, is replaced out of its own "
                    "product. 2,000 is Department I's revenue, which buys IIc; 3,000 is society's "
                    "revenue; 6,000 is all constant capital, of which IIc's 2,000 is replaced by "
                    "Department I's revenue."},
            {"q": "In the same scheme, what is the annual revenue, wages plus profit plus rent, "
                  "of the whole society?",
             "a": ["9,000", "6,000", "3,000", "2,000"],
             "c": 2,
             "why": "`2,000 + 1,000 = 3,000`, the v + s of both departments. 9,000 is gross "
                    "output, Say's figure for income. 6,000 is Department I's product, and 2,000 "
                    "is Department I's revenue alone."},
            {"q": "With Department II at 1,500c + 750v + 750s and Department I unchanged, "
                  "I(v + s) is 2,000 and IIc 1,500. In Marx's Volume II treatment, what becomes "
                  "of Department I's other 500?",
             "a": ["Department I's workers eat it as extra wages",
                   "Department II buys it as consumer goods",
                   "Department I accumulates it as additional means of production",
                   "It is destroyed, since nobody buys it"],
             "c": 2,
             "why": "It is surplus value in the form of means of production, and Department I "
                    "keeps it to expand. It cannot be eaten, being machines and iron; Department "
                    "II makes consumer goods and needs only 1,500 of means of production; and in "
                    "the expanded scheme it is used, not lost."},
            {"q": "Which of these is Marx's gross income?",
             "a": ["c + v + s, the whole product",
                   "Wages plus profit plus rent",
                   "Profit plus rent",
                   "Wages alone"],
             "c": 1,
             "why": "Gross income is the product minus the constant capital it replaces: wages, "
                    "profit and rent. The whole product is gross output. Profit plus rent is net "
                    "income, and wages alone are only the workers' part of gross income."},
        ],
        "mistakes": [
            ("Thinking annual income equals the annual product",
             "Smith's argument, that every price resolves into wages, profit and rent, makes it "
             "seem so, and Say drew the conclusion. The marx preset refutes it on the chapter's "
             "figures: the product is 9,000, the revenues 3,000, and the tile shows 4,000 "
             "exchanged within Department I that no wage, profit or rent ever buys."),
            ("Treating constant capital as revenue seen from another side",
             "The yarn is the spinner's profit and the weaver's constant capital, so it is "
             "tempting to say that capital and revenue are only points of view. For one capital "
             "that is true. For the whole society the 6,000 of constant capital must be replaced "
             "in kind every year, and the one-sector preset shows what happens without the "
             "department that replaces it: the balance fails."),
            ("Thinking the balance requires Marx's numbers",
             "Marx says his figures were chosen at random. What the scheme requires is the "
             "proportion, I(v + s) = IIc, and the growing preset shows what an imbalance means: "
             "500 of Department I's product that Department II does not buy and Department I "
             "must accumulate."),
        ],
        "standard": (
            "Finish when you can separate a year's product from a year's income.",
            "Given a two-department scheme, compute the annual product, the annual revenue and "
            "the part of the product exchanged within Department I, and state whether "
            "I(v + s) = IIc."
        ),
        "note": (
            "The scheme leaves out fixed capital that lasts beyond the year, money, and "
            "accumulation, as Marx's simple scheme does; Volume II adds each in turn. The figures "
            "are Marx's and, as he says, arbitrary. The one-sector preset is an illustration of "
            "the error, not a case the chapter computes."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 3, l. 7248 (the value exists first); l. 7232 (a given figure
    # of 100). Inline: l. 7198-7214 (650 and the wage rise), l. 7216-7218
    # (effect, not cause), l. 7224-7226 (dearer food), l. 7246 (prix
    # nécessaire), l. 7263 (price of labour), l. 7272 (competition),
    # l. 7274 (circulation), l. 7276-7280 (the 125), l. 7302 (contract),
    # l. 7330 (the small farmer). Table: Kerr p. 996 (tables/volume-3/
    # lf0445-03-0996-t0001.png, after l. 7207), the two cases side by side.
    {
        "slug": "illusions-created-by-competition",
        "title": "Illusions Created by Competition",
        "module": "Chapter 50 · The Semblance of Competition",
        "one_line": "A price looks like wages, profit and rent added up; Marx argues the value comes first and the three are its parts, so a wage rise comes out of the others.",
        "summary": (
            "To a business, wages, interest and rent are costs fixed in advance, and the price "
            "must cover them. Marx argues that this is the real movement seen upside down. Run "
            "his own example, 400c + 100v + 150s with wages raised by 50, and see the value stay "
            "at 650 while profit and rent shrink; then try a rent rise and a smaller wage rise."
        ),
        "key": [
            "value first: c + v + s",
            "v + s is fixed by the labour done",
            "wages up 50, surplus value down 50",
            "the price does not move",
            "adding up parts is circular",
        ],
        "key_label": "The value and its parts",
        "concepts_intro": (
            "Chapter 50 is about an appearance, and Marx argues that the appearance is not "
            "a mistake anyone makes by carelessness. Three ideas."
        ),
        "concepts": [
            ("The value exists first",
             "The labour added in a year fixes the value product. Wages, profit and rent divide "
             "it; their sizes are set by different laws, but always inside that limit."),
            ("Price added up",
             "The other view, Smith's natural price, treats wages, profit and rent as separate "
             "magnitudes that are added to make the price. Marx argues it explains each part by "
             "prices that contain the others, and so goes round in a circle."),
            ("Why it looks that way",
             "Wages are agreed before the work is done, interest and rent by contract before the "
             "sale. To every capitalist they are costs given in advance, and so they appear to "
             "make the price rather than to divide it."),
        ],
        "read_title": "The passage, then Marx's example and his reasons",
        "read_intro": (
            "The passage is Marx's summary of the chapter's argument, from its middle. His "
            "worked example comes earlier, and the reasons the illusion is necessary come after."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 50.</strong> &ldquo;In reality the value of "
                  "commodities is the magnitude which exists first, and it comprises the sum of "
                  "the total values of wages, profit and rent, whatever may be their relative "
                  "magnitudes. In the wrong conception, wages, profit and rent are three "
                  "independent magnitudes of value, whose total magnitude is supposed to produce "
                  "the magnitude of the value of a commodity, to limit and to determine it.&rdquo;"),
            ("p", "You know the wrong conception, because it is how prices are usually explained. "
                  "Wages go up, so the firm's costs go up, so prices go up. Adam Smith put it "
                  "carefully: a commodity's natural price is the sum of the natural rates of "
                  "wages, profit and rent needed to bring it to market, and the market price "
                  "gravitates towards it. Marx gives it its French name too, the <em>prix nécessaire</em>. It "
                  "is the view of every business that has ever priced a job, and Marx's claim is "
                  "that it reverses the order of things."),
            ("p", "His example is a capital of 500 producing `400c + 100v + 150s = 650`, with the "
                  "150 of surplus value divided into 75 of profit and 75 of rent. The labour paid "
                  "with £100 has made a new value of £250. In a ten-hour day the worker works four "
                  "hours for himself and six for the capitalist. Then wages rise to 150 for the "
                  "same labour. The new value is still 250, because the same labour has been done, "
                  "so the product is still worth 650: `400c + 150v + 100s`. Marx divides the "
                  "smaller surplus value, &ldquo;say&rdquo;, into 45 of profit and 55 of rent. The "
                  "worker now works six hours for himself and four for the capitalist."),
            ("p", "He then works out the rates, and the reader who checks finds one slip. On a "
                  "capital advanced of 550, profit of 45 is `8 2/11` per cent, rent of 55 is 10 "
                  "per cent, and the whole surplus value `18 2/11` per cent, as he says. Wages of "
                  "150 are `150/550 = 3/11` of the capital, `27 3/11` per cent; the Kerr text "
                  "prints `27 8/11`. The rate of surplus value falls from 150 to `66 2/3` per cent "
                  "and the rate of profit from 30 to `18 2/11` per cent, so the rate of profit "
                  "falls more than the mass of surplus value and less than its rate. Marx sets "
                  "the two cases side by side in a small table on page 996 of the Kerr edition: "
                  "product 650 and new value 250 in both. None of this moves the 650."),
            ("p", "The lab's wage-rise preset is Marx's example. Wages go from £100 to £150 and "
                  "the profit of enterprise tile from £75 to £50. The lab keeps rent at half of s, "
                  "so rent falls to £50 too, where Marx's text splits the 100 as 45 and 55; the "
                  "pair sums to £100 either way. Marx does not divide profit into interest here, "
                  "so the preset gives interest no share and the profit of enterprise tile carries "
                  "the whole profit."),
            ("p", "Marx then says when a wage rise does go with a dearer product. If labour "
                  "becomes less productive, each piece contains more labour and costs more, and "
                  "wages may rise with it; but then the rise in wages &ldquo;is not the cause, but "
                  "rather a result of a change in the value of the commodities&rdquo;. And if the "
                  "fall in productivity is in agriculture, so that only the worker's food gets "
                  "dearer, the yarn's value does not change at all; the cotton spinner pays more "
                  "wages out of the same 650. He grants, too, the case taken up in “Wage "
                  "Changes and Prices of Production”: a general rise in wages lowers the rate of "
                  "profit and so raises some prices of production and lowers others."),
            ("p", "Next he takes the adding-up view at its word and shows it going round in "
                  "circles. Wages are the price of the necessaries the worker needs; the price of "
                  "those necessaries is made of wages, profit and rent; so &ldquo;The price of labor "
                  "is determined by itself.&rdquo; Profit fares no better. Competition can equalise "
                  "rates of profit, but it cannot say why the equal rate is 10 per cent rather "
                  "than 100. Marx's verdict, at his most sardonic, is that &ldquo;competition has "
                  "to shoulder the duty of explaining all inexplicable ideas of the economists, "
                  "whereas the economists should rather explain competition.&rdquo;"),
            ("p", "He adds a small sum to show where the additions really come from. Let wages "
                  "be 100, profit 10 per cent of wages and rent 15 per cent, so the price is "
                  "`100 + 10 + 15 = 125`. If everyone sells at 125 what cost 100 in wages, every "
                  "buyer pays the mark-up that every seller gains, &ldquo;for circulation can never "
                  "give what it did not first receive&rdquo;. The 25 has to come out of the "
                  "product: the worker gets `4/5` of it, the capitalist `2/25` and the landlord "
                  "`3/25`. Raise wages to 110 and the same percentages make `137 1/2`, which is "
                  "the adding-up theory's prediction that every price rises with wages."),
            ("p", "<strong>Volume III, Chapter 50.</strong> &ldquo;A given figure of 100 always "
                  "remains the same, whether it is divided into 50 + 50, or into 20 + 70 + 10, or "
                  "into 40 + 30 + 30.&rdquo;"),
            ("p", "That is the lab's other two presets. In rent-rise, an illustrative value "
                  "product of £200 has its rent raised from 3/10 to 1/2 of the surplus value: rent "
                  "goes to £50, interest stays at £20, profit of enterprise falls to £30, and the "
                  "price has no reason to move. In fixed-value, wages on the same £200 rise by £20 "
                  "to £120; rent, interest and profit of enterprise keep their shares of a smaller "
                  "s and become £24, £16 and £40. Together they lost £20, exactly what wages "
                  "gained."),
            ("p", "Why, then, does everyone see it the other way round? Marx's answer takes up "
                  "the rest of the chapter. Even with competition removed, he argues, the "
                  "illusion would remain, because &ldquo;the wages are stipulated by contract, "
                  "before the value equivalent to them has been produced&rdquo;. Interest is fixed "
                  "when the loan is made and rent when the lease is signed. To the capitalist "
                  "each is a cost given in advance, and the price must cover them all; his own "
                  "profit of enterprise is whatever is left. He sees the parts first, so they look "
                  "like the makers of the whole."),
            ("p", "It goes so far that people who are not capitalists are counted in the same "
                  "terms. A small farmer who works his own land is treated as three people: "
                  "&ldquo;To himself as a wage worker he pays his wages, to himself as a capitalist "
                  "he turns over his profit, and to himself as a landlord he pays his rent.&rdquo; "
                  "Marx says this is not wholly wrong, in a society where capital is the general "
                  "form, and that it strengthens the illusion that these forms are natural to "
                  "every kind of production."),
            ("p", "A later result bears on this from another direction. Piero Sraffa, in "
                  "<em>Production of Commodities by Means of Commodities</em> of 1960, derived the "
                  "same inverse movement of wages and the rate of profit from the physical inputs "
                  "and outputs of production, with no labour values at all, so the result Marx "
                  "relies on here does not need his theory of value. And in an economy with paper "
                  "money, a general rise in money wages can raise the price level, which is a "
                  "question about money that the lab, reckoning in value, does not model."),
            ("p", "If the division into wages, profit and rent is a division of something given, "
                  "it is fair to ask whether the division itself is natural. The next lesson, "
                  "“Distribution Relations and Production Relations”, asks what changes if the "
                  "relations of production change."),
        ],
        "lab": ("capkit", {
            "mode": "revenue",
            "view": "added-up",
            "money_unit": "£",
            "preset": "wage-rise",
            "presets": [
                {"id": "wage-rise", "label": "Marx's figures: 400c + 100v + 150s, wages up by 50",
                 "c": 400, "v": 100, "s": 150, "split": {"interest": 0, "rent": "1/2"},
                 "wage_change": 50, "expect": {"rvWages": "£150", "rvRent": "£50", "rvProfitShare": "£50"}},
                {"id": "rent-rise", "label": "Illustrative: £200 value product, rent from 3/10 to 1/2 of s",
                 "c": 100, "v": 100, "s": 100, "split": {"interest": "1/5", "rent": "1/2"},
                 "wage_change": 0, "expect": {"rvWages": "£100", "rvRent": "£50", "rvInterest": "£20", "rvProfitShare": "£30"}},
                {"id": "fixed-value", "label": "Illustrative: £200 value product, wages up by £20",
                 "c": 100, "v": 100, "s": 100, "split": {"interest": "1/5", "rent": "3/10"},
                 "wage_change": 20, "expect": {"rvWages": "£120", "rvRent": "£24", "rvInterest": "£16", "rvProfitShare": "£40"}},
            ],
            "panel_title": "A wage change inside a fixed value product",
            "panel_intro": (
                "The value parts before the change go in, with the shares of s that go as interest "
                "and rent and the change in wages. The lab holds the value product fixed and gives "
                "the four revenues after the change; the status line says what they were before, "
                "and what adding them up would wrongly give."
            ),
        }),
        "steps_title": "Dividing a fixed value product",
        "steps_intro": "Four steps for any change in wages or in the shares of surplus value.",
        "steps": [
            ("Fix the value product",
             "With the same labour done, v + s does not change. Write it down before anything "
             "moves."),
            ("Move wages",
             "Add the change to v. Surplus value is the value product minus the new wages, so s "
             "moves by the same amount the other way."),
            ("Divide the new surplus value",
             "Apply the shares of rent and interest to the new s; profit of enterprise is the "
             "remainder."),
            ("Check the sum and the price",
             "The four revenues still add to the value product, and c + v + s, the product's "
             "value, is unchanged. Adding the new wages to the old profit and rent gives a figure "
             "the labour never produced."),
        ],
        "worked": {
            "title": "A wage rise of twenty pounds",
            "intro": [
                "Take the fixed-value preset. The value product is £200: £100 of wages and £100 of "
                "surplus value, with rent 3/10 of s and interest 1/5. Wages rise by £20 for the "
                "same work. You want the four revenues after the rise.",
            ],
            "lines": [
                "value product:  100 + 100 = £200, unchanged",
                "wages:  100 + 20 = £120",
                "surplus value:  200 − 120 = £80",
                "rent:  3/10 · 80 = £24",
                "interest:  1/5 · 80 = £16",
                "profit of enterprise:  80 − 24 − 16 = £40",
            ],
            "after": [
                "Rent, interest and profit of enterprise were £30, £20 and £50; they are now £24, "
                "£16 and £40, £20 less in all. Added up as independent parts, £120 of wages and the "
                "old £100 of surplus value would make £220, a value nobody's labour produced.",
            ],
        },
        "quiz_title": "Value first, parts after",
        "quiz": [
            {"q": "Marx's capital produces 400c + 100v + 150s = 650. Wages rise to 150 for the "
                  "same labour. What is the product now worth?",
             "a": ["700", "650", "600", "675"],
             "c": 1,
             "why": "The same labour adds the same 250, so the product is `400 + 250 = 650`, now "
                    "divided as 150v + 100s. 700 adds the wage rise on top. 600 is Marx's case of "
                    "cheaper means of production, 350c, and 675 matches nothing in the chapter."},
            {"q": "In the same example, what is the rate of surplus value after the wage rise, "
                  "as a fraction?",
             "a": ["3/2", "2/11", "2/3", "1"],
             "c": 2,
             "why": "`s/v = 100/150 = 2/3`. 3/2 is the rate before the rise, 150/100. 2/11 is the "
                    "rate of profit, 100/550, and 1 would need s and v equal."},
            {"q": "In Marx's adding-up example wages are 100, profit 10 per cent of wages and "
                  "rent 15 per cent, and the commodity sells at 125. What share of the product "
                  "does the worker receive?",
             "a": ["All of it, since the price is set by wages", "4/5", "2/25", "3/25"],
             "c": 1,
             "why": "`100/125 = 4/5`. The capitalist's 10 is 2/25 and the landlord's 15 is 3/25. "
                    "Selling at 125 to buyers who also sell at 125 adds nothing, so the extra 25 "
                    "comes out of the product, not on top of it."},
            {"q": "On the chapter's account, which change goes with a rise in the value of a "
                  "yard of the spinner's yarn?",
             "a": ["A wage rise in spinning won by the spinners, with productivity unchanged",
                   "A wage rise in spinning caused by dearer bread after a bad harvest",
                   "A fall in the productivity of spinning, with wages rising as a result",
                   "A higher rent for the mill, with productivity unchanged"],
             "c": 2,
             "why": "Less productive spinning puts more labour into each yard, so its value "
                    "rises; any wage rise is then an effect. A wage rise with productivity "
                    "unchanged comes out of s. Dearer bread raises wages but, Marx says, leaves "
                    "the yarn's value unchanged. A rent rise also comes out of s."},
        ],
        "mistakes": [
            ("Thinking a wage rise raises prices because wages are a component added to them",
             "It is Smith's natural price and every business's costing, and for one firm facing "
             "given wages it describes what it sees. On the chapter's accounting the wage-rise "
             "preset refutes it: wages go from £100 to £150, profit and rent together from £150 "
             "to £100, and the product stays at 650, because the same labour was done."),
            ("Explaining the price of labour by the price of necessaries",
             "If wages are the price of the worker's necessaries, and those are priced at wages "
             "plus profit plus rent, the price of labour has been explained by itself. Marx "
             "accepts that the value of labour-power is set by the necessaries; what he denies is "
             "that wages can then be a separate element added to make every price."),
            ("Thinking the illusion is just a mistake of the careless",
             "Marx argues it would appear even without competition, because wages, interest and "
             "rent are fixed by contract before the value is produced. The appearance is real; "
             "what he disputes is the explanation built on it."),
        ],
        "standard": (
            "Finish when you can divide a fixed value product after a change in one of its parts.",
            "Given c, v, s, the shares of s taken by rent and interest and a change in wages, "
            "compute the four revenues after the change, show that the value product and the "
            "product's value are unchanged, and state what adding up the parts would wrongly give."
        ),
        "note": (
            "The lab holds the value product fixed because the chapter's case holds the labour "
            "done fixed; if productivity changes, the value changes and the lab does not see it. "
            "It reckons in value, with gold as money, so it cannot say what a general rise in "
            "money wages does to prices under paper money. The 650 is Marx's; the £200 presets "
            "are illustrative, and the lab's equal split of the reduced s between profit and rent "
            "is a simplification of his 45 and 55."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 3, l. 7354 and l. 7358 (reverse side; if one portion were
    # not capital). Inline: l. 7350 (the more critical mind), l. 7755
    # (footnote 153, Mill), l. 7356 (wages first face the worker as capital),
    # l. 7366 and l. 7376 (two traits), l. 7394 (profit and production),
    # l. 7396 (the landlord), l. 7348 (Indian communes, Peruvians), l. 7336
    # (foundations), l. 6968 (realm of freedom), l. 7180 (accounts), l. 7402
    # (the conflict).
    {
        "slug": "distribution-and-production-relations",
        "title": "Distribution Relations and Production Relations",
        "module": "Chapter 51 · Conditions of Distribution and Production",
        "one_line": "Wages, profit and rent are not a natural way of sharing out a product; Marx argues they are the reverse side of capitalist production and change only with it.",
        "summary": (
            "John Stuart Mill held that production obeys laws like physics while distribution is "
            "a matter of human institutions. Marx argues that the forms of distribution are the "
            "other face of the forms of production. Divide the same £200 value product under a "
            "capitalist firm, a workers' co-operative and an association of producers, and see "
            "what changes and what does not."
        ),
        "key": [
            "distribution: the reverse side of production",
            "wages are capital before they are revenue",
            "every society: c replaced, a surplus fund",
            "who takes the surplus, and who decides",
            "the tile names belong to one society",
        ],
        "key_label": "Distribution and production",
        "concepts_intro": (
            "Chapter 51 is short and is a reply to one view in particular. Three ideas."
        ),
        "concepts": [
            ("Forms of distribution",
             "Wages, profit and rent say who receives which part of the value product: the owner "
             "of labour-power, of capital, of land. They are titles to shares."),
            ("The reverse side",
             "Those titles presuppose the relations of production: means of production that face "
             "the worker as capital, land held as private property. Change one and the other "
             "changes with it."),
            ("What every society keeps",
             "Any society that produces must replace its means of production and set aside a "
             "surplus for insurance, expansion and those who cannot work. What differs is who "
             "takes the surplus and who decides."),
        ],
        "read_title": "The thesis, then the argument for it",
        "read_intro": (
            "The passage comes from the chapter's first page, where Marx states the thesis and "
            "the reason for it in two sentences a paragraph apart."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 51.</strong> &ldquo;The conditions of distribution "
                  "are essentially identical with these conditions of production, being their "
                  "reverse side, so that both conditions share the same historical and passing "
                  "character. &hellip; If one portion of the product were not transformed into "
                  "capital, the other would not assume the form of wages, profit and rent.&rdquo;"),
            ("p", "Arguments about fairness in your own society are mostly arguments about "
                  "distribution: the minimum wage, taxes on income and inheritance, rent "
                  "controls. They take for granted that the product could be shared out "
                  "differently while it is produced as it is now. Marx's chapter is about that "
                  "assumption."),
            ("p", "He describes two views of it. The ordinary one treats wages, profit and rent "
                  "as natural, the way any society must share its product, with earlier "
                  "societies as rough drafts of it. The other is more careful. &ldquo;A more "
                  "advanced, more critical mind, however, admits the historically developed "
                  "character of the condition of distribution&rdquo;, but holds on all the more "
                  "firmly to production as fixed by human nature. Marx's footnote names John "
                  "Stuart Mill, and Mill's <em>Principles of Political Economy</em> of 1848 "
                  "states the view plainly: the laws of production have the character of physical "
                  "truths, while the distribution of wealth is a matter of human institution, "
                  "which society can change. Mill drew from it a programme of "
                  "reform, taxes on inheritance and on the unearned rise in land values, and the "
                  "tax-and-transfer states of the twentieth century were built on the same "
                  "distinction."),
            ("p", "Marx's reply goes through the passage. The usual starting point is that the "
                  "annual product is divided among wages, profit and rent, and he calls this a "
                  "misstatement: the product is divided first between capital and revenue. "
                  "&ldquo;One of these revenues, wages, never assumes the form of a revenue, a "
                  "revenue of the laborer, until it has first faced this laborer in the form of "
                  "capital.&rdquo; Wages exist only because the means of production belong to "
                  "someone else and labour-power is bought with capital. That is a relation of "
                  "production, and the form of distribution is its other face."),
            ("p", "&ldquo;Capitalist production is marked from the outset by two peculiar "
                  "traits.&rdquo; It produces its products as commodities, and the labourer "
                  "himself sells a commodity, labour-power. And it has &ldquo;the production of "
                  "surplus-value as the direct aim and determining incentive of production&rdquo;. "
                  "Later in the chapter Marx makes the point that matters here: profit is not "
                  "only a share of the product. It decides where capital goes and what is "
                  "produced. &ldquo;Profit, then, appears here as the main factor, not of the "
                  "distribution of products, but of their production itself&rdquo;. The split of "
                  "profit into interest and profit of enterprise develops credit, and credit shapes "
                  "production in turn. Even rent, which looks "
                  "like pure distribution, presupposes a landlord reduced to &ldquo;a usurer in "
                  "land and collector of rent&rdquo;, a figure only this mode of production makes."),
            ("p", "What, then, is common to every society? Marx's answer runs through the last "
                  "chapters. In any society that produces, part of the labour supplies the "
                  "producers' own consumption and part makes a surplus for social needs, whether "
                  "in the Indian village commune or in what he calls the communism of the Peruvians. The surplus has "
                  "work to do: an insurance fund against accidents, a fund for expansion, and the "
                  "keep of those too young, too old or too ill to work. Strip wages and surplus "
                  "value of their capitalist character, he writes at the end of Chapter 50, and "
                  "&ldquo;we have not these forms, but merely their foundations, which are common "
                  "to all social modes of production&rdquo;."),
            ("p", "The lab divides one value product three ways, with £100 of constant capital "
                  "replaced in every case. In the capitalist preset, £200 of value product gives "
                  "wages of £100, rent £30, interest £20 and profit of enterprise £50, as in "
                  "“The Trinity Formula”. In the cooperative preset the workers own the "
                  "enterprise but rent its land and borrow its capital, so rent and interest stay "
                  "at £30 and £20, and the members take the remaining £150 as pay: the profit of "
                  "enterprise tile reads £0. In the association preset the producers hold the "
                  "means of production in common: no rent, no interest, £150 for the producers' "
                  "consumption and £50 set aside for insurance, expansion and those who cannot "
                  "work."),
            ("p", "Look at the association's tiles. The kit still calls the £150 wages and the "
                  "£50 profit of enterprise, because those are the names the lab has. They are "
                  "the wrong names, and that is the chapter's point: the £100 of c, the £200 of "
                  "value product and a fund above consumption appear in all three presets, while "
                  "the forms of wages, profit and rent belong to the first."),
            ("p", "The cooperative preset shows the other half of the argument. Its distribution, "
                  "£150 to the workers and nothing to profit of enterprise, would leave a "
                  "capitalist owner with nothing for his trouble, and on Marx's account a "
                  "capitalist enterprise is carried on for exactly that surplus. The split is "
                  "sustainable where the workers own the firm, which is a change in the relations "
                  "of production. Rent and interest stay at £30 and £20 because private land and "
                  "lending at interest have not changed."),
            ("p", "The standard objection to the association preset is about knowledge, not "
                  "fairness. Ludwig von Mises argued in 1920 that without markets in the means "
                  "of production there are no prices for them, and without prices an "
                  "association cannot calculate which use of its resources is economical. Oskar "
                  "Lange replied in 1936 that a planning board could find such prices by trial "
                  "and error; Friedrich Hayek answered that the knowledge needed is dispersed "
                  "and is gathered only by markets. Marx's own remark, at the end of Chapter 49, "
                  "is that after capitalism &ldquo;the regulation of the labor time and the "
                  "distribution of the social labor among the various groups of production, also "
                  "the keeping of accounts in connection with this, become more essential than "
                  "ever&rdquo;. How that would be done is the question Mises asked, and Volume III "
                  "does not answer it."),
            ("p", "Earlier, in Chapter 48, Marx had said what the surplus is ultimately for. "
                  "Beyond the realm of necessity, where producers regulate their exchange with "
                  "nature in common, lies &ldquo;the true realm of freedom&rdquo;, and &ldquo;The "
                  "shortening of the working day is its fundamental premise.&rdquo; The chapter "
                  "ends on the conflict he expects between the two sides: &ldquo;A conflict then "
                  "arises between the material development of production and its social "
                  "form.&rdquo;"),
            ("p", "Three revenues, three titles, three kinds of owner. The next lesson, "
                  "“Classes”, asks whether those owners are what makes a class."),
        ],
        "lab": ("capkit", {
            "mode": "revenue",
            "view": "trinity",
            "money_unit": "£",
            "preset": "capitalist",
            "presets": [
                {"id": "capitalist", "label": "Capitalist firm: wages £100, rent 3/10 and interest 1/5 of s",
                 "c": 100, "v": 100, "s": 100, "split": {"interest": "1/5", "rent": "3/10"},
                 "expect": {"rvWages": "£100", "rvRent": "£30", "rvInterest": "£20", "rvProfitShare": "£50"}},
                {"id": "cooperative", "label": "Workers' co-operative: rents its land, borrows its capital",
                 "c": 100, "v": 150, "s": 50, "split": {"interest": "2/5", "rent": "3/5"},
                 "expect": {"rvWages": "£150", "rvRent": "£30", "rvInterest": "£20", "rvProfitShare": "£0"}},
                {"id": "association", "label": "Association of producers: £150 consumed, £50 common fund",
                 "c": 100, "v": 150, "s": 50, "split": {"interest": 0, "rent": 0},
                 "expect": {"rvWages": "£150", "rvRent": "£0", "rvInterest": "£0", "rvProfitShare": "£50"}},
            ],
            "panel_title": "One value product under three relations of production",
            "panel_intro": (
                "The same £100 of means of production and £200 of value product in every preset. "
                "What changes is how the £200 is split and who takes each part. The tile names "
                "are those of a capitalist economy; in the association preset read the wages "
                "tile as the producers' consumption and the profit of enterprise tile as the "
                "common fund."
            ),
        }),
        "steps_title": "Comparing one product under different relations",
        "steps_intro": "Four steps for setting two forms of production side by side.",
        "steps": [
            ("Hold the material side fixed",
             "Keep c and the value product v + s the same in every case. The means of production "
             "still have to be replaced, and the same labour has been done."),
            ("List the titles",
             "Write down who has a claim on the value product in each case: worker, capitalist, "
             "lender, landlord, or the producers in common."),
            ("Divide the value product",
             "Compute each claimant's part. Rent and interest are shares of whatever surplus is "
             "left after the producers' own consumption."),
            ("Separate form from foundation",
             "State what appears in every case, the replacement of c and a fund above "
             "consumption, and what appears in only one, the forms of wages, profit and rent."),
        ],
        "worked": {
            "title": "The same two hundred pounds, three ways",
            "intro": [
                "Take the three presets. Each has £100 of means of production to replace and a "
                "value product of £200. You want each division and what they share.",
            ],
            "lines": [
                "capitalist:  100 + 30 + 20 + 50 = £200",
                "cooperative:  150 + 30 + 20 + 0 = £200",
                "association:  150 consumed + 50 common fund = £200",
                "every case:  c = £100 replaced",
            ],
            "after": [
                "The co-operative's members take £150 and owe the same rent and interest as the "
                "capitalist firm. The association pays neither, and its £50 is a fund the "
                "producers decide on together, not anyone's profit.",
            ],
        },
        "quiz_title": "Forms and their foundations",
        "quiz": [
            {"q": "In the cooperative preset, the members rent their land and borrow their "
                  "capital, and the value product is £200 with rent £30 and interest £20. What "
                  "do the members take as pay?",
             "a": ["£200", "£100", "£150", "£50"],
             "c": 2,
             "why": "`200 − 30 − 20 = 150`. £200 ignores the landlord and the lender. £100 is the "
                    "capitalist firm's wage bill, and £50 is that firm's profit of enterprise."},
            {"q": "Which of these appears in all three presets, capitalist, cooperative and "
                  "association?",
             "a": ["Rent paid to a landlord",
                   "Profit of enterprise",
                   "The replacement of £100 of means of production",
                   "Interest paid to a lender"],
             "c": 2,
             "why": "Every form of production must replace the means of production it uses up. "
                    "The association pays no rent or interest, and the cooperative has no profit "
                    "of enterprise left over."},
            {"q": "Marx's footnote points to John Stuart Mill as holding which view?",
             "a": ["That distribution is historical while production follows fixed laws",
                   "That production and distribution are both historical",
                   "That distribution follows fixed natural laws, like production",
                   "That the trinity formula is an illusion"],
             "c": 0,
             "why": "Mill held that production has the character of physical truths and "
                    "distribution is a matter of human institution. The second option is Marx's "
                    "own view, the third is the ordinary view the chapter starts from, and Mill "
                    "did not hold the fourth."},
            {"q": "Why does Marx say the usual statement, that the annual product is distributed "
                  "among wages, profit and rent, is a misstatement?",
             "a": ["Because rent is not part of the product",
                   "Because the product is first divided between capital and revenue, and wages "
                   "face the worker as capital first",
                   "Because profit is all interest",
                   "Because wages are paid in kind, not money"],
             "c": 1,
             "why": "That is his argument in the chapter. Rent is part of the value product; "
                    "profit includes profit of enterprise as well as interest; and the chapter "
                    "says nothing about wages being paid in kind."},
        ],
        "mistakes": [
            ("Thinking distribution can be changed without changing production relations",
             "This is Mill's position, and reforms of distribution are real. Marx's claim is that "
             "the forms themselves rest on relations of production, and the cooperative preset "
             "shows the arithmetic: pay the workers £150 out of £200 while rent and interest stay "
             "at £30 and £20, and profit of enterprise is £0. A capitalist firm exists for that "
             "surplus. The split lasts where the workers own the firm, and rent and interest "
             "remain because land and lending have not changed."),
            ("Thinking an association has no surplus",
             "Marx's association still sets aside more than the producers consume: an insurance "
             "fund, a fund for expansion, and the keep of those who cannot work. The association "
             "preset's £50 is that fund. What disappears is profit, rent and interest as titles, "
             "not the surplus."),
            ("Reading the tile names as names for every society",
             "The kit labels the £150 wages and the £50 profit of enterprise in the association "
             "preset because those are the only names it has. On the chapter's argument they are "
             "the names of one society's forms, and using them elsewhere is the habit Marx "
             "describes in the small farmer who pays himself wages, profit and rent."),
        ],
        "standard": (
            "Finish when you can divide one value product under different relations of production.",
            "Given a value product, the means of production to replace and the claims on the "
            "product under a capitalist firm, a co-operative and an association of producers, "
            "compute each division, and state which features appear in all three and which in "
            "only one."
        ),
        "note": (
            "The co-operative's and the association's figures are illustrative; Marx gives none, "
            "and the split of £150 and £50 is an assumption. The lab sees quantities: it can "
            "show that a co-operative and a capitalist firm with the same tiles differ only in "
            "who receives them, but it cannot show who decides, which is the difference the "
            "chapter cares about. Whether an association could calculate without market prices "
            "is the socialist calculation debate, named here and not settled."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 3, l. 7412 and l. 7415 (what constitutes a class); l. 7417
    # (physicians and officials; the landlords; the last words). Inline:
    # l. 7408 (three great classes), l. 7410 (England; middle and transition
    # stages; the separation of the means of production from labour).
    {
        "slug": "classes",
        "title": "Classes",
        "module": "Chapter 52 · The Classes",
        "one_line": "Marx asks what makes wage labourers, capitalists and landlords three classes, tries the obvious answer, finds it multiplies classes without end, and the manuscript stops.",
        "summary": (
            "The last chapter of Capital is a page long. Marx names the three great classes of "
            "modern society, asks what makes them classes, and tests the answer the whole of "
            "Part VII suggests: their sources of revenue. Group a small society by source of "
            "revenue, make the sources finer, and watch the count grow, as the chapter does "
            "before it breaks off."
        ),
        "key": [
            "three revenues: wages, profit, rent",
            "group by source of revenue",
            "add physicians and officials: 5 groups",
            "split the landlords: more groups",
            "the manuscript stops here",
        ],
        "key_label": "The last page",
        "concepts_intro": (
            "There is very little text, and three things to see in it."
        ),
        "concepts": [
            ("The three great classes",
             "Wage labourers, capitalists and landlords, living on wages, profit and ground-rent. "
             "Marx says that even in England, where the economic structure is most developed, the "
             "boundaries are blurred by middle and transitional layers."),
            ("The question",
             "What makes them classes? The first answer is the one the whole of Part VII invites: "
             "the identity of their revenues and the sources of those revenues."),
            ("The objection",
             "By that test physicians and officials would be classes too, and landlords would "
             "split into owners of vineyards, farms, forests, mines and fisheries. The test does "
             "not stop at three."),
        ],
        "read_title": "The question, and the page that ends the book",
        "read_intro": (
            "The chapter is so short that the passage is most of it. The rest is read at the end, "
            "where the manuscript ends."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 52.</strong> &ldquo;The first question to be "
                  "answered is this: What constitutes a class? And this follows naturally from "
                  "another question, namely: What constitutes wage laborers, capitalists and "
                  "landlords into three great social classes? At first glance it might seem that "
                  "the identity of their revenues and their sources of revenue does that.&rdquo;"),
            ("p", "Marx wrote this in the manuscript of the mid-1860s from which Engels, eleven "
                  "years after Marx's death, published Volume III in 1894. The chapter is a page "
                  "long. It begins by naming its subject: the owners of labour-power, of capital "
                  "and of land, whose revenues are wages, profit and ground-rent, "
                  "&ldquo;form the three great classes of modern society resting upon the "
                  "capitalist mode of production&rdquo;."),
            ("p", "He qualifies that at once. England is where modern society is most developed, "
                  "and even there the classes do not appear in a pure form: &ldquo;Middle and "
                  "transition stages obliterate even here all definite boundaries&rdquo;, less in "
                  "the country than in the towns. That, he says, does not matter for the analysis, "
                  "because the tendency of capitalist production is to separate the means of "
                  "production more and more from labour, turning labour into wage labour and the "
                  "means of production into capital, while landed property separates from both."),
            ("p", "Then the question, and the first answer. The answer is natural after the last "
                  "four chapters. The trinity formula paired each class with a source: labour "
                  "with wages, capital with profit, land with rent. So perhaps a class is the "
                  "group of people who live on the same kind of revenue from the same kind of "
                  "source."),
            ("p", "The lab applies that test. In the three-classes preset five people, two "
                  "spinners, a mill owner, a manufacturer and a landlord, give the tile "
                  "`3 groups: wages, profit, rent`. In the doctor-and-official preset a physician "
                  "living on medical fees and an official living on a salary join them, and the "
                  "same test now finds 5 groups. In the landowners-split preset the landlords "
                  "are told apart by what their land is, vineyards, farms, forests, mines and "
                  "fisheries, and the count is 7. The status line says what the chapter is about "
                  "to say: split the sources more finely and the count grows with them."),
            ("p", "Those are Marx's own examples, and the reader who has followed the book can "
                  "see why they trouble him. The test counts kinds of income, and there are as "
                  "many kinds as the division of labour cares to make. It cannot by itself "
                  "produce three great classes, or explain why those three should matter more "
                  "than physicians and fishery owners. Whatever answer Marx had in mind, it had to "
                  "be something other than the source of revenue alone."),
            ("p", "Step back and see where the book has brought you. Volume I took a single "
                  "commodity and found in it the labour-time that makes it a value, then found "
                  "in the working day the surplus labour that makes surplus value: c + v + s in "
                  "a spinning mill. Volume II followed that value through the circuits of capital "
                  "and the turnover of its parts, and showed that two departments can reproduce "
                  "each other only in proportion. Volume III let the surplus value appear as it "
                  "does on the surface: as profit on the whole capital, averaged across "
                  "industries into prices of production, shared with merchants, split into "
                  "interest and profit of enterprise, and claimed by landlords as rent. Part VII "
                  "puts the pieces back on the surface, where each looks like the fruit of its "
                  "own source, and asks who lives on them."),
            ("p", "Every step of that argument is contested, and the lessons have tried to say "
                  "so where it is taken. The labour theory of value faces the marginal-utility "
                  "theory that replaced it in economics; the passage from values to prices of "
                  "production is the transformation problem, argued over since Bortkiewicz; the "
                  "falling rate of profit is a tendency whose record is a matter of data. What "
                  "the lab has done throughout is narrower and firmer: it has computed, from the "
                  "same c, v and s, what follows on Marx's definitions."),
            ("p", "Here the manuscript ends. These are its last words:"),
            ("p", "<strong>Volume III, Chapter 52.</strong> &ldquo;However, from this point of "
                  "view physicians and officials would also form two classes, for they belong to "
                  "the two distinct social groups, and the revenues of their members flow from the "
                  "same common source. The same would also be true of the infinite dissipation of "
                  "interests and positions created by the social division of labor among "
                  "laborers, capitalists and landlords. For instance, the landlords are divided "
                  "into owners of vineyards, farms, forests, mines, fisheries.&rdquo;"),
        ],
        "lab": ("capkit", {
            "mode": "revenue",
            "view": "classes",
            "preset": "three-classes",
            "presets": [
                {"id": "three-classes", "label": "Five people living on wages, profit and rent",
                 "people": [{"name": "a spinner", "source": "wages"},
                            {"name": "a second spinner", "source": "wages"},
                            {"name": "a mill owner", "source": "profit"},
                            {"name": "a manufacturer", "source": "profit"},
                            {"name": "a landlord", "source": "rent"}],
                 "expect": {"rvClassCount": "3 groups: wages, profit, rent"}},
                {"id": "doctor-and-official", "label": "Marx's objection: a physician and an official join them",
                 "people": [{"name": "a spinner", "source": "wages"},
                            {"name": "a second spinner", "source": "wages"},
                            {"name": "a mill owner", "source": "profit"},
                            {"name": "a manufacturer", "source": "profit"},
                            {"name": "a landlord", "source": "rent"},
                            {"name": "a physician", "source": "medical fees"},
                            {"name": "an official", "source": "salary"}],
                 "expect": {"rvClassCount": "5 groups: wages, profit, rent, medical fees, salary"}},
                {"id": "landowners-split", "label": "Marx's landlords: vineyards, farms, forests, mines, fisheries",
                 "people": [{"name": "a spinner", "source": "wages"},
                            {"name": "a mill owner", "source": "profit"},
                            {"name": "a vineyard owner", "source": "vineyard rent"},
                            {"name": "a farm owner", "source": "farm rent"},
                            {"name": "a forest owner", "source": "forest rent"},
                            {"name": "a mine owner", "source": "mining rent"},
                            {"name": "a fishery owner", "source": "fishery rent"}],
                 "expect": {"rvClassCount": "7 groups: wages, profit, vineyard rent, farm rent, forest rent, mining rent, fishery rent"}},
            ],
            "panel_title": "Grouping people by source of revenue",
            "panel_intro": (
                "Each person and the source of his revenue go in. The lab groups the people by "
                "source and counts the groups. Make a source finer, or add a person with a new "
                "one, and the count follows."
            ),
        }),
        "steps_title": "Counting groups by source of revenue",
        "steps_intro": "Four steps, the test the chapter tries and then doubts.",
        "steps": [
            ("List the people",
             "Write down each person in the society, or each kind of person."),
            ("Name each source",
             "Beside each, name the source of the revenue: wages for labour-power, profit for "
             "capital, rent for land, and any other source that appears."),
            ("Group and count",
             "Put people with the same source in one group and count the groups."),
            ("Refine and recount",
             "Make the sources finer, by kind of land or kind of service, and count again. "
             "Compare the new count with the three great classes."),
        ],
        "worked": {
            "title": "From three groups to seven",
            "intro": [
                "Take the three presets in turn. You want the number of groups the "
                "source-of-revenue test gives each time.",
            ],
            "lines": [
                "wages, profit, rent:  3 groups",
                "add medical fees and salary:  3 + 2 = 5 groups",
                "rent split five ways:  wages, profit + 5 = 7 groups",
            ],
            "after": [
                "The test gives three groups only while the sources are kept coarse. Made finer, "
                "in the ways Marx names, it gives five and then seven, and nothing in the test "
                "says where to stop.",
            ],
        },
        "quiz_title": "What makes a class",
        "quiz": [
            {"q": "Two spinners live on wages, a mill owner and a manufacturer on profit, and a "
                  "landlord on rent. How many groups does the source-of-revenue test give?",
             "a": ["5", "2", "3", "4"],
             "c": 2,
             "why": "Three sources, so three groups: wages, profit, rent. Five is the number of "
                    "people, and the test groups people with the same source together."},
            {"q": "A physician living on medical fees and an official living on a salary join "
                  "the same five people. How many groups now?",
             "a": ["3", "5", "7", "4"],
             "c": 1,
             "why": "Two new sources make `3 + 2 = 5`. Three would put the newcomers into the "
                    "old groups, which the test does not do; seven is the landowners-split "
                    "count."},
            {"q": "Marx's objection is that the test would split the landlords. Into owners of "
                  "what, in his list?",
             "a": ["Houses, shops and factories",
                   "Vineyards, farms, forests, mines and fisheries",
                   "Arable land and pasture only",
                   "Large and small estates"],
             "c": 1,
             "why": "That is the list on which the manuscript ends. The other options are "
                    "divisions the chapter does not make."},
            {"q": "What does Chapter 52 conclude about what constitutes a class?",
             "a": ["That a class is defined by its source of revenue",
                   "That a class is defined by its relation to the means of production",
                   "Nothing: the manuscript breaks off after the objection",
                   "That England has exactly three classes"],
             "c": 2,
             "why": "The chapter raises the question, tries the source-of-revenue answer, objects "
                    "to it, and stops. The relation to the means of production is a later "
                    "reader's answer, not the chapter's, and the chapter says England's classes "
                    "are blurred by middle and transitional layers."},
        ],
        "mistakes": [
            ("Thinking a class is defined by its source of income alone",
             "It is the answer Marx tries first, because the trinity formula suggests it. The "
             "presets show what goes wrong: the same test gives 3 groups, then 5 with a "
             "physician and an official, then 7 with the landlords told apart. Marx raises "
             "exactly this objection, so the chapter does not endorse the answer it tests."),
            ("Reading the three great classes as pure and exhaustive",
             "Marx says that even in England middle and transitional layers blur every boundary. "
             "The three classes are the structure he takes the tendency of capitalist production "
             "to be moving towards, not a census of any country."),
            ("Supplying the chapter's answer",
             "Later readers have answered the question, by a class's place in production or by "
             "its position in the market. Those answers are theirs. The chapter asks the "
             "question, tests one answer, finds it wanting, and breaks off."),
        ],
        "standard": (
            "Finish when you can apply the source-of-revenue test and state what the chapter says about it.",
            "Given a list of people and the sources of their revenue, count the groups the "
            "source-of-revenue test gives, recount when the sources are made finer, and state "
            "the objection Chapter 52 raises before the manuscript ends."
        ),
        "note": (
            "The lab counts distinct sources of revenue; it cannot say what makes a class, which "
            "is the question the manuscript leaves open. Answers have been given since, by "
            "Lenin in 1919, by a group's place in a system of production and its relation to "
            "the means of production, and by Max Weber, by a group's situation in the market. "
            "Neither is in the text, and this lesson does not choose between them. The people "
            "are illustrative; the physician, the official and the five kinds of landlord are "
            "Marx's."
        ),
    },
]
