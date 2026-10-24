"""Average Profit and Its Fall, lessons 1-4 -- Volume III, Part II, Chapters 8-11, one lesson per chapter.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, and the translator's double quotation marks inside a quotation
are printed as single curly quotes. Nothing else is changed: where the Kerr
text has a misprint or a rounded figure (Chapter 9's "8 + 18 + 26", Chapter
11's "16 1/12", "128 7/12" and "100 10/19"), the quotation keeps it and the
lesson says so, and the lab prints the exact figure.

Chapter 9's three tables are printed in the book as tables and are absent
from the plain text; the Kerr pages are in the project's shared folder as
images (capital-texts/tables/volume-3/lf0445-03-0183-t0001.png, the five
spheres at value, Kerr p. 183; lf0445-03-0185-t0001.png and -t0002.png, the
same spheres with used-up c, cost prices and values, and their prices of
production and deviations, Kerr p. 185). Every figure in the Chapter 9 lesson
was read from those images and agrees with every total and deviation the text
does print (l. 1681, 1683, 1691, 1693); the lesson quotes only the text around
them and cites the pages.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 3, l. 1633-1635 (90 c + 10 v against 10 c + 90 v: the opening
    # passage). Inline: l. 1620 (A and B at 700), l. 1625 (copper and iron:
    # 200 c and 400 c), l. 1641 (sold at their values), l. 1643-1651 (the
    # European and the Asiatic country; Carey and Bastiat), l. 1665
    # (irreconcilable with the actual process).
    {
        "slug": "different-compositions-different-rates",
        "title": "Different Compositions, Different Rates of Profit",
        "module": "Chapter 8 · Different Composition of Capitals in Different Lines of Production and Resulting Differences in the Rates of Profit",
        "one_line": "Capitals of equal size that employ different amounts of labour produce different masses of surplus value, so if goods sold at their values the rates of profit would differ from trade to trade.",
        "summary": (
            "Volume III's second Part opens with a problem the theory has made for itself. At one "
            "rate of surplus value, a capital that spends most of itself on means of production "
            "sets less labour in motion than one that spends most on wages, and so yields less "
            "surplus value per hundred. Compute the rates of profit of capitals of different "
            "composition at value, and see why selling at value would leave them unequal."
        ),
        "key": [
            "same s′, different c/v",
            "s = s′ · v; v indexes the labour employed",
            "p′ = s / (c + v), sphere by sphere",
            "90c + 10v: 10%; 10c + 90v: 90%",
            "at value, equal capitals earn unequally",
        ],
        "key_label": "Chapter 8 in five lines",
        "concepts_intro": (
            "Chapter 8 is short and does one thing: it compares capitals side by side that Part I "
            "compared one after another. Three ideas carry it."
        ),
        "concepts": [
            ("Organic composition",
             "The ratio of constant to variable capital, measured in value, as it reflects the "
             "technical ratio of means of production to workers. Marx counts it per hundred of "
             "capital: 90c + 10v, 10c + 90v. Two trades with the same machines per worker can still "
             "differ in it if their materials cost different amounts."),
            ("Variable capital as an index",
             "With the wage and the working day given, each pound of variable capital stands for "
             "a definite number of workers and so for a definite amount of living labour, paid and "
             "unpaid. Only that labour produces surplus value on the book's account, so v measures "
             "how much a capital can produce."),
            ("Rates of profit at value",
             "If goods sold at their values, each capital's profit would be its own surplus value, "
             "and its rate of profit s / (c + v) would follow its composition. Equal capitals would "
             "earn unequal profits."),
        ],
        "read_title": "The passage first, then the chapter's comparisons",
        "read_intro": (
            "Marx states the difficulty in one sentence: if two such capitals made the same "
            "profit, it would be as plain as daylight that value had some other source than "
            "labour. The sentence comes first."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 8.</strong> &ldquo;If a capital, consisting of "
                  "percentages of 90 c + 10 v, produced as much surplus-value, or profit, with the "
                  "same degree of exploitation, as a capital consisting of percentages of 10 c + 90 v, "
                  "then it would be as plain as daylight that the surplus-value, and value in general, "
                  "must have an entirely different source than labor, and that political economy "
                  "would then be without a rational basis.&rdquo;"),
            ("p", "Think of two businesses you could put £100 into. One is a power station, almost "
                  "all plant and fuel, with a handful of staff. The other is a cleaning company, "
                  "almost all wages, with some mops and vans. You would expect either to pay you "
                  "about the going return, and Marx agrees that, passing differences aside, "
                  "that is how it works. Chapter 8 explains why, on the theory of the first two "
                  "volumes, that expectation is a puzzle."),
            ("p", "The chapter holds the rate of surplus value the same everywhere. Workers move "
                  "between trades, and Marx takes differences in exploitation as frictions that a "
                  "general analysis sets aside. With the wage and the working day fixed, &ldquo;one "
                  "pound sterling stands for one laborer per week&rdquo;, and at 100% each worker "
                  "paid £1 adds £2 of new value. So the variable capital is an index of the living "
                  "labour a capital sets in motion, and of the surplus labour in it."),
            ("p", "Now read the sentence again. In 90c + 10v, ten pounds of wages employ ten "
                  "workers; their week adds £20, of which £10 is surplus value. In 10c + 90v the "
                  "ninety workers add £180, of which £90 is surplus value. Marx's verdict on the "
                  "alternative is the sentence itself: if both produced the same, value would have a "
                  "source other than labour. The lab's first preset, <strong>marx</strong>, does "
                  "this sum: rates of profit of 10% and 90% on the same £100."),
            ("p", "Marx gives a second kind of case. In Chapter 8's sphere A, a capital of 700 spends "
                  "600 on means of production and 100 on wages; in B the split is reversed, so B "
                  "earns six times A's profit, 85 5/7% against 14 2/7%. But the technique need not "
                  "differ at all. Let both trades employ the same hundred workers on the same "
                  "machines and materials, and let the materials be dearer in B, as copper is dearer "
                  "than iron in another of the chapter's examples. Then A works with 200c + 100v and B with 400c + 100v, both make £100 of "
                  "surplus value, and the rates are 33 1/3% and 20%. The <strong>copper</strong> "
                  "preset shows those two rates: here a difference in what the means of production "
                  "cost, not in how many workers use them, separates the rates."),
            ("def", ("Rate of profit at value",
                     "A sphere's surplus value divided by its whole capital, s / (c + v), when its "
                     "commodities sell at their values. At a given s′ it is higher where v is a "
                     "larger share of the capital.")),
            ("p", "Then comes the comparison of countries, which carries the chapter's one surprise. "
                  "Marx's European capital is 84c + 16v at a rate of surplus value of 100%; his "
                  "Asiatic capital is 16c + 84v, with the worker labouring four-fifths of the day for "
                  "himself and one-fifth for the employer, which is a rate of surplus value of 25%. "
                  "(The Kerr text calls that 25% a &ldquo;rate of profit&rdquo;, but the clause that "
                  "follows, four-fifths for himself and one-fifth for the employer, is a rate of "
                  "surplus value, and the sum below uses it as one.) The text gives the result: "
                  "&ldquo;In the European country: Value of product 84 c + 16 v + 16 s, or 116; rate "
                  "of profit 16/100, or 16%.&rdquo; In Asia, 84 × 25% = 21, and the rate is 21%."),
            ("p", "So the capital with a quarter of the rate of exploitation earns the higher rate of "
                  "profit. The <strong>europe-asia</strong> preset gives 16% and 21%. Marx adds that "
                  "&ldquo;Men like Carey, Bastiat, and others, would come to the opposite "
                  "conclusion.&rdquo; Henry Carey in Philadelphia and Frédéric Bastiat in Paris were "
                  "the leading economists of harmony around 1850; both held that as capital grows, "
                  "labour's share of the product rises and capital's falls. Marx does not spell "
                  "out their reasoning, but on such a view a high return to capital is a sign of a "
                  "large share for capital and a small one for labour. On Marx's accounting the "
                  "comparison runs the other way: the European worker is exploited four times as "
                  "intensely, and the low rate of profit comes from the mass of means of production "
                  "each worker sets in motion."),
            ("p", "The fourth preset, <strong>equal-composition</strong>, is the one case where "
                  "nothing is puzzling. A capital of £100 at 80c + 20v and one of £1,000 at 800c + 200v "
                  "both earn 20%. Only where compositions are equal, Marx says, do profits stand in "
                  "proportion to the capitals that make them."),
            ("p", "Chapter 8 also takes up turnover: a capital turned over more often makes more "
                  "surplus value a year from the same variable capital, so turnover is a second source "
                  "of unequal rates. The proportion of fixed to circulating capital, by contrast, "
                  "affects the rate only through composition or turnover, never by itself. This lesson "
                  "computes composition; turnover's effect was computed in Cost Price and the Rate of "
                  "Profit."),
            ("p", "Everything so far assumes, as Marx says twice, that &ldquo;the commodities are "
                  "sold at their values&rdquo;. And here the trouble is plain: in reality, setting "
                  "aside passing differences, rates of profit do not differ by trade, and could not "
                  "for long without capital leaving the low ones. Marx states the problem without "
                  "softening it: &ldquo;It would seem, then, as though the theory of value were "
                  "irreconcilable at this point with the actual process&rdquo;. This is the point at "
                  "which most critics of the book have chosen to stand, and the next lesson shows why."),
            ("p", "The chapter's last paragraph gives the clue: cost prices are the same for equal "
                  "capitals, whatever their composition, and the capitalist sees only those. The next "
                  "lesson, “The General Rate of Profit and Prices of Production”, asks what prices "
                  "would let every capital earn the same rate, and what happens to the values when "
                  "they do."),
        ],
        "lab": ("capkit", {
            "mode": "prices",
            "view": "rates",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 90c + 10v against 10c + 90v, both at 100%",
                 "spheres": [{"name": "A", "c": 90, "v": 10}, {"name": "B", "c": 10, "v": 90}],
                 "s_rate": 1, "expect": {"ppRates": "1/10 = 10%, 9/10 = 90%"}},
                {"id": "copper", "label": "Marx's figures: the same 100 workers on £200 and on £400 of means of production",
                 "spheres": [{"name": "A", "c": 200, "v": 100}, {"name": "B", "c": 400, "v": 100}],
                 "s_rate": 1, "expect": {"ppRates": "1/3 = 33.33%, 1/5 = 20%"}},
                {"id": "europe-asia", "label": "Marx's figures: Europe 84c + 16v at 100%, Asia 16c + 84v at 25%",
                 "spheres": [{"name": "Europe", "c": 84, "v": 16, "s_rate": 1},
                             {"name": "Asia", "c": 16, "v": 84, "s_rate": "1/4"}],
                 "s_rate": "", "expect": {"ppRates": "4/25 = 16%, 21/100 = 21%"}},
                {"id": "equal-composition", "label": "£100 and £1,000, both at 80c + 20v",
                 "spheres": [{"name": "small", "c": 80, "v": 20}, {"name": "large", "c": 800, "v": 200}],
                 "s_rate": 1, "expect": {"ppRates": "1/5 = 20%, 1/5 = 20%"}},
            ],
            "panel_title": "Rates of profit if goods sold at their values",
            "panel_intro": (
                "Each sphere is typed as name, c, v and, if it differs from the common one, its own "
                "s/v. The lab computes s = s′ · v and the rate of profit s / (c + v) for each. "
                "Compare the europe-asia preset's rates of surplus value with its rates of profit."
            ),
        }),
        "steps_title": "Comparing rates of profit at value",
        "steps_intro": "Four steps for any set of capitals.",
        "steps": [
            ("Write each capital as c + v",
             "Put each capital in the form c + v. Per hundred is convenient but not necessary; "
             "the rate does not depend on the capital's size."),
            ("Compute surplus value",
             "Multiply each capital's v by its rate of surplus value. With one s′ for all, surplus "
             "value is proportional to v."),
            ("Divide by the whole capital",
             "The rate of profit at value is s / (c + v). Compare it with s′, which is s / v: the "
             "two differ by the share of v in the capital."),
            ("Compare the spheres",
             "Rank the rates. At one s′ the lowest composition earns the highest rate; across "
             "different s′, composition can outweigh exploitation."),
        ],
        "worked": {
            "title": "Europe against Asia",
            "intro": [
                "Take Marx's two national capitals of £100. You want each rate of profit and how it "
                "compares with each rate of surplus value.",
            ],
            "lines": [
                "Europe:  s = 100% · 16 = 16",
                "Europe:  p′ = 16 / (84 + 16) = 16%",
                "Asia:  s = 25% · 84 = 21",
                "Asia:  p′ = 21 / (16 + 84) = 21%",
                "s′: Europe four times Asia",
            ],
            "after": [
                "The rate of profit is higher in Asia by more than a quarter, as Marx says (5 on 16), "
                "on a quarter of the rate of surplus value. Composition decides the comparison, "
                "because the Asian capital sets more than five times as much labour in motion.",
            ],
        },
        "quiz_title": "Composition and the rate of profit",
        "quiz": [
            {"q": "At a rate of surplus value of 100%, what is the rate of profit of a capital of "
                  "70c + 30v if its goods sell at their value?",
             "a": ["100%",
                   "70%",
                   "30%",
                   "43%"],
             "c": 2,
             "why": "Surplus value is `100% · 30 = 30` on a capital of 100, so 30%. A hundred per "
                    "cent is the rate of surplus value; 70% confuses c with s; 43% is `30/70`, s "
                    "over c, which leaves v out of the capital."},
            {"q": "Two capitals employ the same number of workers on the same machines and "
                  "materials, but the materials cost more in the second. At one rate of surplus "
                  "value and selling at value, how do their rates of profit compare?",
             "a": ["They are equal, because the technique is the same",
                   "The second is lower, because the same surplus value is spread over a larger capital",
                   "The second is higher, because dearer materials add more value",
                   "It cannot be said without the length of the working day"],
             "c": 1,
             "why": "This is Marx's case of dearer means of production: 200c + 100v and 400c + 100v each make "
                    "£100 of surplus value, at 33 1/3% and 20%. Dearer materials pass on their value "
                    "but add no surplus value. The working day is given by the chapter's assumptions."},
            {"q": "In the europe-asia preset, which capital has the higher rate of profit, and "
                  "which the higher rate of surplus value?",
             "a": ["Europe both",
                   "Asia both",
                   "They are equal in both",
                   "Asia the higher rate of profit, Europe the higher rate of surplus value"],
             "c": 3,
             "why": "Europe: 100% s′, 16% p′. Asia: 25% s′, 21% p′. The Asian capital's low "
                    "composition, 16c + 84v, more than makes up for its lower rate of exploitation."},
            {"q": "On the chapter's account, when do profits stand in proportion to the capitals "
                  "that produce them, with goods selling at value?",
             "a": ["Only when the capitals have the same composition, rate of surplus value and turnover",
                   "Always, because competition equalises them",
                   "Only when the capitals are of the same size",
                   "Never"],
             "c": 0,
             "why": "Marx says the law that equal capitals yield equal profits holds, at value, only "
                    "for capitals of the same composition, rate of surplus value and turnover. Size "
                    "is irrelevant to the rate. Competition's equalising is the next chapter, and "
                    "works by departing from value."},
        ],
        "mistakes": [
            ("Thinking a higher rate of surplus value always means a higher rate of profit",
             "The rate of profit is s / (c + v), and s′ fixes only s / v. In the europe-asia "
             "preset Europe's s′ is 100% and Asia's 25%, yet the tile reads 16% for Europe and 21% "
             "for Asia: four times the exploitation, a lower rate of profit. That is the reading "
             "Marx says Carey and Bastiat would get backwards."),
            ("Reading a difference in composition as a difference in technique",
             "Organic composition is measured in value. In the copper preset both trades use the "
             "same workers, machines and materials; only the price of the materials differs, and the "
             "rates are 33 1/3% and 20%. A change in the price of c alone moves the composition."),
            ("Treating the rate of profit as depending on a capital's size",
             "In the equal-composition preset £100 and £1,000 at the same composition both earn "
             "20%. Size changes the mass of profit, not the rate; Marx's capital of 7,000 in A earns "
             "the same 14 2/7% as his capital of 700."),
        ],
        "standard": (
            "Finish when you can compute rates of profit at value for capitals of different composition.",
            "Given each capital's c, v and rate of surplus value, compute its surplus value and its "
            "rate of profit at value, and state which differences in composition or in s′ account "
            "for the ranking."
        ),
        "note": (
            "Everything in this lesson assumes, with the chapter, that commodities sell at their "
            "values; the next chapter drops that assumption. The lab also assumes that variable "
            "capital measures the labour set in motion, which holds only with one wage and one "
            "working day everywhere. The marx, copper and europe-asia figures are Marx's; the "
            "equal-composition capitals are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 3, l. 1707 (the aggregate price equals the aggregate value:
    # the opening passage); l. 1697 (the definition of price of production).
    # Inline: l. 1681-1683 (500, 110, 22%, 122), l. 1691-1693 (2 + 7 + 17
    # above), l. 1701 (stockholders), l. 1719 (never ascertainable average),
    # l. 1745 (k + 20), l. 1751-1755 (I, II, III at 20%), l. 1759 (a
    # modification of our original assumption; the possibility of an error).
    {
        "slug": "the-general-rate-of-profit",
        "title": "The General Rate of Profit and Prices of Production",
        "module": "Chapter 9 · Formation of a General Rate of Profit (Average Rate of Profit) and Transformation of the Values of Commodities into Prices of Production",
        "one_line": "Competition gives every capital the average rate of profit on its size, so commodities sell at cost price plus average profit, above or below their values, while total price equals total value and total profit equals total surplus value.",
        "summary": (
            "Chapter 9 is where Marx turns values into prices of production, and where the book's "
            "most argued-over step is taken. Compute the general rate of profit from Marx's five "
            "spheres, each sphere's price of production, and the totals that Marx says are kept. "
            "Then read the paragraph in which he notes what his procedure leaves out, because that "
            "is where the century-long dispute begins."
        ),
        "key": [
            "general rate = total s / total capital",
            "price of production = k + p′ · capital",
            "k = used-up c + v (cost price)",
            "Σ prices = Σ values; Σ profit = Σ s",
            "inputs at value, as Chapter 9 does it",
        ],
        "key_label": "The transformation in five lines",
        "concepts_intro": (
            "The chapter has a procedure, a result and a caveat. The lab computes the first two. "
            "The third is the subject of the paragraph on the transformation problem below."
        ),
        "concepts": [
            ("The general rate of profit",
             "Total surplus value over total capital: 110 on 500 in Marx's table, 22%. It is the "
             "average of the spheres' own rates weighted by the size of each capital, which is why "
             "the allotment of capital between spheres moves it."),
            ("Price of production",
             "A commodity's cost price plus the general rate of profit on the whole capital that "
             "produced it, consumed or not. In a sphere of average composition it equals the value; "
             "above average composition it is higher than the value, below it lower."),
            ("The two totals",
             "Summed over every sphere, prices of production equal values and profits equal surplus "
             "values. Marx reads this as the law of value holding for the whole, while each "
             "commodity's price departs from its value."),
        ],
        "read_title": "The passage first, then the table",
        "read_intro": (
            "The passage is Marx's claim about the totals. The definition of price of production "
            "comes second, and the table it summarises is computed in the lab."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 9.</strong> &ldquo;The aggregate price of the "
                  "commodities of I to V would be equal to their aggregate value, that is to say, it "
                  "would be equal to the sum of the cost-prices of I to V plus the sum of the "
                  "surplus-values, or profits, produced in I to V. It would actually be the "
                  "money-expression of the total quantity of past and present labor incorporated in "
                  "the commodities of I to V.&rdquo;"),
            ("p", "The previous lesson ended with capitals of equal size earning unequal rates at "
                  "value, which no real economy shows. Marx's answer is to treat the whole social "
                  "capital as one capital and its parts as shares. &ldquo;The various capitalists, "
                  "so far as profits are concerned, are so many stockholders in a stock "
                  "company&rdquo;, each drawing a profit in proportion to the shares held. The total "
                  "dividend is the total surplus value; what changes is who receives it."),
            ("p", "His table has five spheres of £100 each: I is 80c + 20v, II 70c + 30v, III 60c + "
                  "40v, IV 85c + 15v and V 95c + 5v, all at 100%. Together that is 390c + 110v, "
                  "110 of surplus value on 500, so the general rate is 22%. In a first version, the "
                  "table on page 183 of the Kerr edition, every sphere transfers all of its c to the "
                  "product, the values are 120, 130, 140, 115 and 105, and every product sells at 122. "
                  "The <strong>all-used-up</strong> preset gives that: five prices of £122, and values "
                  "and prices both summing to £610."),
            ("p", "Marx then warns that &ldquo;not all cost-prices are equal to 100&rdquo;: fixed "
                  "capital wears out over years, and only the worn part enters this year's product. "
                  "In the second table the spheres use up 50, 51, 51, 40 and 10 of their c, so cost "
                  "prices are 70, 81, 91, 55 and 15 and values 90, 111, 131, 70 and 20. Each sphere "
                  "then sells at its cost price plus 22. That is the <strong>marx</strong> preset: "
                  "prices of £92, £103, £113, £77 and £37. The Kerr edition prints both tables on "
                  "page 185, the second with a last column of deviations, and the text sums them: "
                  "sales &ldquo;2 + 7 + 17 = 26 above&rdquo; value and 8 + 18 = 26 below (the Kerr "
                  "text misprints the second sum as &ldquo;8 + 18 + 26&rdquo;). The lab's last column "
                  "reproduces that column of the table."),
            ("p", "<strong>Volume III, Chapter 9.</strong> &ldquo;That price of any commodity which "
                  "is equal to its cost-price plus that share of average profit on the total capital "
                  "invested (not merely consumed) in its production which is allotted to it in "
                  "proportion to its conditions of turn-over, is called its price of "
                  "production.&rdquo;"),
            ("def", ("Price of production",
                     "Cost price plus the general rate of profit on the whole capital advanced, "
                     "consumed or not. In symbols, k + p′ · C, where k is used-up c plus v.")),
            ("p", "Notice &ldquo;not merely consumed&rdquo;. The profit is on the capital "
                  "advanced, which is why sphere V, with a large capital and a small cost price, gains "
                  "most: £37 against a value of £20. Marx's smaller table makes the pattern plain. "
                  "With an average composition of 80c + 20v and a rate of 20%, 80c + 20v sells at its "
                  "value of 120, 90c + 10v at 120 against a value of 110, and 70c + 30v at 120 against "
                  "a value of 130. The <strong>three</strong> preset computes it: three prices of "
                  "£120, values and prices both £360. Capital of higher composition sells above value, "
                  "lower below, average at value."),
            ("p", "So does the law of value still hold? Marx's claim is that it holds for the whole "
                  "and through the whole. The lab's totals tile reads values £422 = prices £422 and "
                  "s £110 = profit £110 for the marx preset, and the sum of the deviations is nought. "
                  "Each capitalist gets back what his own cost price was, plus a share of a total he "
                  "did not produce alone. Under capitalism, Marx writes, the law of value enforces "
                  "itself &ldquo;as a never ascertainable average of ceaseless fluctuations&rdquo;."),
            ("p", "There is one sentence every reader should find before going further. Marx notes "
                  "that a price of production becomes the cost price of the buyer, so the inputs of "
                  "each sphere should themselves be at prices of production, not values: &ldquo;The "
                  "foregoing statements are indeed a modification of our original assumption "
                  "concerning the determination of the cost-price of commodities.&rdquo; He grants "
                  "&ldquo;the possibility of an error&rdquo; if cost price is taken as the value of "
                  "the inputs, and says that his &ldquo;present analysis does not necessitate a "
                  "closer examination of this point&rdquo;. He had met the same objection a few pages "
                  "earlier and answered it for the totals: the inputs' prices carry other spheres' "
                  "profits, but summed over the whole country &ldquo;it is evident that the "
                  "calculation must come out right&rdquo;, and the deviations &ldquo;mutually "
                  "compensate one another&rdquo;. He asserts this for the whole; he does not redo the "
                  "table with its inputs at prices of production. The table, and this lab, value the "
                  "inputs at value."),
            ("p", "That is the transformation problem, and it deserves its full strength. Eugen von "
                  "Böhm-Bawerk, in <em>Karl Marx and the Close of His System</em> (1896), argued that "
                  "Volume III contradicts Volume I: if no commodity exchanges at its value, then value "
                  "explains no actual price, and the equality of the totals is an empty statement "
                  "about a sum nobody trades. Ladislaus von Bortkiewicz (1906–07) took the procedure "
                  "on its own terms and transformed the inputs too; in his solution the rate of "
                  "profit can be found, though in general it differs from the rate computed in "
                  "values, and Marx's two totals cannot in general both hold. Later "
                  "work went in opposite directions. Paul Samuelson (1971) and Ian Steedman (1977), "
                  "after Piero Sraffa, argued that prices and the rate of profit can be computed "
                  "from technique and the real wage without values at all, so values are a detour. "
                  "Others redefined the terms. The New Interpretation of Gérard Duménil and Duncan "
                  "Foley (around 1980) takes the value of money and of labour-power from observed "
                  "prices and wages, so that total profit equals total surplus value and the year's "
                  "new value equals its price, though not gross price and gross value. The temporal "
                  "single-system reading of Andrew Kliman, Alan Freeman and others values inputs at "
                  "the prices actually paid for them, and on that reading both of Marx's totals "
                  "hold. This Subject does not "
                  "take a side, and the lab does only what Chapter 9 does."),
            ("p", "What the capitalist sees is the price of production and nothing behind it. Profit "
                  "now differs from surplus value in mass, not only in rate, and Marx says this "
                  "removes the determination of value &ldquo;from direct observation&rdquo;. A "
                  "capitalist who saves on labour sees his profit hold steady, and concludes that "
                  "labour cannot be its source."),
            ("p", "Chapter 9 takes the general rate as already formed. The next lesson, “Market Value "
                  "and Surplus Profit”, asks how competition forms it, first among producers of one "
                  "commodity and then between spheres."),
        ],
        "lab": ("capkit", {
            "mode": "prices",
            "view": "production",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's five spheres, with used-up c of 50, 51, 51, 40 and 10",
                 "spheres": [{"name": "I", "c": 80, "v": 20, "c_used": 50},
                             {"name": "II", "c": 70, "v": 30, "c_used": 51},
                             {"name": "III", "c": 60, "v": 40, "c_used": 51},
                             {"name": "IV", "c": 85, "v": 15, "c_used": 40},
                             {"name": "V", "c": 95, "v": 5, "c_used": 10}],
                 "s_rate": 1, "premiums": [], "expect": {"ppAverage": "11/50 = 22%", "ppPrices": "£92, £103, £113, £77, £37", "ppTotals": "values £422 = prices £422; s £110 = profit £110"}},
                {"id": "all-used-up", "label": "Marx's five spheres, all c used up in the year",
                 "spheres": [{"name": "I", "c": 80, "v": 20}, {"name": "II", "c": 70, "v": 30},
                             {"name": "III", "c": 60, "v": 40}, {"name": "IV", "c": 85, "v": 15},
                             {"name": "V", "c": 95, "v": 5}],
                 "s_rate": 1, "premiums": [], "expect": {"ppAverage": "11/50 = 22%", "ppPrices": "£122, £122, £122, £122, £122", "ppTotals": "values £610 = prices £610; s £110 = profit £110"}},
                {"id": "three", "label": "Marx's figures: average, higher and lower composition at 20%",
                 "spheres": [{"name": "I", "c": 80, "v": 20}, {"name": "II", "c": 90, "v": 10},
                             {"name": "III", "c": 70, "v": 30}],
                 "s_rate": 1, "premiums": [], "expect": {"ppAverage": "1/5 = 20%", "ppPrices": "£120, £120, £120", "ppTotals": "values £360 = prices £360; s £60 = profit £60"}},
            ],
            "panel_title": "From values to prices of production",
            "panel_intro": (
                "Each sphere is typed as name, c, v and used-up c (empty: all of c). The lab "
                "computes total s over total capital, adds that rate on each whole capital to each "
                "cost price, and checks the totals. Inputs are valued at value, as in Chapter 9. "
                "Compare each sphere's composition with the sign of its price − value."
            ),
        }),
        "steps_title": "Transforming values into prices of production",
        "steps_intro": "Five steps, as Chapter 9 takes them.",
        "steps": [
            ("Value each sphere's product",
             "Value is used-up c + v + s, with s = s′ · v. Cost price is used-up c + v."),
            ("Form the general rate",
             "Add every sphere's surplus value and divide by the sum of every sphere's whole "
             "capital, c + v. The result is the general rate of profit."),
            ("Price each product",
             "Add to each cost price the general rate times the sphere's whole capital. That sum "
             "is the price of production."),
            ("Compare price with value",
             "Price minus value is positive above average composition, negative below and nought "
             "at the average."),
            ("Check the totals",
             "Sum prices and values, profits and surplus values. With inputs at value, as in the "
             "chapter, each pair is equal."),
        ],
        "worked": {
            "title": "Sphere V in Marx's table",
            "intro": [
                "Take sphere V, 95c + 5v, of which 10 of c is used up, with the general rate at 22%. "
                "You want its value, its price of production and the gap between them.",
            ],
            "lines": [
                "value:  10 + 5 + 5 = 20",
                "cost price:  10 + 5 = 15",
                "profit:  22% · (95 + 5) = 22",
                "price of production:  15 + 22 = 37",
                "price − value:  37 − 20 = +17",
            ],
            "after": [
                "Sphere V produced 5 of surplus value and receives 22 of profit. The other 17 comes "
                "from spheres II and III, which sell 8 and 18 below value, net of the 2 and 7 that "
                "I and IV gain.",
            ],
        },
        "quiz_title": "Prices of production",
        "quiz": [
            {"q": "Three spheres of 100 each, 80c + 20v, 90c + 10v and 70c + 30v, have all their c "
                  "used up and a rate of surplus value of 100%. What is the general rate of profit?",
             "a": ["10%",
                   "20%",
                   "30%",
                   "60%"],
             "c": 1,
             "why": "Total surplus value is `20 + 10 + 30 = 60` on a total capital of 300, so 20%. "
                    "Ten and thirty per cent are two spheres' own rates at value; 60 is the mass of "
                    "surplus value, not a rate."},
            {"q": "In the same three spheres, at what price does 90c + 10v sell, and how does it "
                  "compare with its value?",
             "a": ["110, at its value",
                   "120, below its value of 130",
                   "100, its cost price",
                   "120, above its value of 110"],
             "c": 3,
             "why": "Cost price 100 plus 20% on a capital of 100 is 120; its value is `90 + 10 + 10 "
                    "= 110`. A capital above average composition sells above value. The value of 130 "
                    "belongs to 70c + 30v."},
            {"q": "A sphere of 60c + 40v uses up 51 of its c, and the general rate is 22%. What is "
                  "its price of production?",
             "a": ["£122",
                   "£131",
                   "£113",
                   "£91"],
             "c": 2,
             "why": "Cost price is `51 + 40 = 91`; profit is 22% on the whole 100, so 22; the price "
                    "is 113. £122 assumes all of c is used up; £131 is its value at 100%; £91 is the "
                    "cost price alone."},
            {"q": "Which statement does Chapter 9 itself make about the cost prices in its table?",
             "a": ["That taking them at the value of the inputs may be an error, since inputs are bought at prices of production",
                   "That they are exact, because inputs are bought at value",
                   "That they are irrelevant to the price of production",
                   "That they must equal 100 in every sphere"],
             "c": 0,
             "why": "Marx calls this &ldquo;a modification of our original assumption&rdquo; and "
                    "grants &ldquo;the possibility of an error&rdquo;, then says his analysis does not "
                    "need to go further. That admission is where the transformation problem starts. "
                    "He explicitly warns that not all cost prices equal 100."},
        ],
        "mistakes": [
            ("Thinking prices of production abolish the law of value because no commodity sells at its value",
             "Only the average-composition sphere sells at value, and in the marx preset none does. "
             "Marx's claim is about the whole: the totals tile reads values £422 = prices £422; s £110 "
             "= profit £110, and the deviations, +2, −8, −18, +7 and +17, sum to nought. Whether a "
             "law that holds only in the aggregate is still a law of price is exactly what "
             "Böhm-Bawerk denied; the lab shows what Marx asserted, not that he was right."),
            ("Computing profit on the cost price instead of the capital advanced",
             "Profit is the general rate on the whole capital, consumed or not. Sphere V's cost price "
             "is 15, and 22% of it would be 3.3; its profit is 22, on its capital of 100. In the "
             "marx preset that difference is what lifts V to £37."),
            ("Believing the lab has solved the transformation problem",
             "The lab transforms outputs and leaves inputs at value, exactly as Chapter 9 does. "
             "Transforming the inputs too is what Bortkiewicz did, and in general it breaks at least "
             "one of the two equalities in the totals tile. The lab does not attempt it."),
        ],
        "standard": (
            "Finish when you can compute a general rate of profit and every sphere's price of production.",
            "Given each sphere's c, v, used-up c and rate of surplus value, compute the general rate "
            "of profit, each price of production and its deviation from value, and check that total "
            "price equals total value and total profit equals total surplus value."
        ),
        "note": (
            "This lesson, like its chapter, assumes that commodities sold at their values before "
            "the equalisation and takes every input at its value. That is the step the "
            "transformation problem disputes: with inputs also at prices of production, the two "
            "totals cannot in general both hold, and which (if either) should be kept is argued to "
            "this day. The lab computes no solution. The figures are Marx's, read from the tables "
            "on pages 183 and 185 of the Kerr edition."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 3, l. 1861 (market value: the opening passage); l. 1898 (the
    # mass produced under the least favorable conditions). Inline: l. 1894
    # (the bulk under normal conditions), l. 1906 (strictly speaking; demand
    # exceeding supply slightly), l. 1908 (supply far exceeding demand),
    # l. 1942 (cease to explain anything), l. 1955 (the Observations), l. 1981
    # (capital withdraws and invades), l. 2002 (surplus-profit).
    {
        "slug": "market-value-and-surplus-profit",
        "title": "Market Value and Surplus Profit",
        "module": "Chapter 10 · Compensation of the Average Rate of Profit by Competition. Market Prices and Market Values. Surplus-Profit",
        "one_line": "Within one trade, producers working under different conditions sell at one market value, so the better placed earn a surplus profit and the worse lose part of theirs.",
        "summary": (
            "Chapter 10 asks how competition does what Chapter 9 assumed. Within a trade it forms one "
            "market value from many individual values; between trades it moves capital until rates "
            "of profit equalise. Compute a market value as the average over every unit produced, and "
            "each group's gain or loss per unit against it, as the mix of conditions changes."
        ),
        "key": [
            "market value = total hours / total units",
            "gain per unit = market value − own value",
            "bulk at average: market value = average",
            "bulk at worst: market value rises",
            "supply and demand move price round value",
        ],
        "key_label": "Market value in five lines",
        "concepts_intro": (
            "This is the longest chapter in the Part, and it moves from one trade to the economy and "
            "back. Three ideas hold it together."
        ),
        "concepts": [
            ("Individual and market value",
             "Each producer's goods have an individual value set by the conditions under which they "
             "were made. On the market, goods of one kind sell at one market value: the average value "
             "of the trade's output, or the value of goods made under the conditions of its bulk."),
            ("Surplus profit",
             "A producer whose individual value is below the market value realises more than his own "
             "surplus value; one above it realises less. The difference is surplus profit, and Marx "
             "says that, crises and general overproduction aside, every market price carries one for "
             "those who produce under the most favourable conditions."),
            ("Supply, demand and value",
             "Supply and demand move market prices above and below market values. When they balance "
             "they explain nothing, Marx argues, so the level they balance at must be set by "
             "something else."),
        ],
        "read_title": "The passage first, then Marx's three cases",
        "read_intro": (
            "The definition comes first. Marx then runs it through three cases, depending on which "
            "group produces most of the trade's output."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 10.</strong> &ldquo;We shall have to regard the "
                  "market-value on one side as the average value of the commodities produced in a "
                  "certain sphere, and on the other side as the individual value of commodities "
                  "produced under the average conditions of their respective sphere of production "
                  "and constituting the bulk of the products of that sphere.&rdquo;"),
            ("p", "You know this from any market stall. Two growers sell the same apples at the same "
                  "price, though one grows them on better land with newer equipment. The price does "
                  "not ask how each was grown. Chapter 10 asks what fixes that one price, and the "
                  "sentence above gives two answers that coincide in the ordinary case: the average "
                  "value of all the trade's goods, and the value of the goods made under the "
                  "conditions most of them are made under."),
            ("p", "Marx's first case has the bulk produced under average conditions, with small and "
                  "balancing groups above and below. Then market value is the value of the average "
                  "bulk, and it equals the average over everything. The <strong>average-dominates"
                  "</strong> preset has 1,000 pieces at 3 hours, 8,000 at 4 and 1,000 at 5: the market "
                  "value is 4 hours, the best group gains an hour a piece, the worst loses one."),
            ("p", "<strong>Volume III, Chapter 10.</strong> &ldquo;In that case the mass produced "
                  "under the least favorable conditions determines the market-value, or social "
                  "value.&rdquo;"),
            ("p", "That is the second case: the worst-placed group makes a relatively large share of "
                  "the output, and &ldquo;The lot produced under the worst conditions decides the "
                  "question.&rdquo; &ldquo;Strictly speaking&rdquo;, Marx goes on, the market value "
                  "is then the total value of the mass divided by its quantity, which lies above the "
                  "average group's value and below the worst group's, closer to the worst the "
                  "larger its share. The <strong>worst-dominates</strong> preset has 1,000 pieces at "
                  "3 hours, 3,000 at 4 and 6,000 at 5: the market value is 9/2 hours, and even the "
                  "average group now gains half an hour a piece. The third case reverses it. In "
                  "<strong>best-dominates</strong>, 6,000 at 3 hours, 3,000 at 4 and 1,000 at 5, the "
                  "market value falls to 7/2 hours, below the middle group's own."),
            ("def", ("Surplus profit",
                     "The excess a producer realises because the individual value of his goods is "
                     "below the market value at which they sell. Per unit it is market value minus "
                     "individual value; negative, it is surplus value produced and not realised.")),
            ("p", "Where does demand come in? Marx gives it a definite role. In all three cases the "
                  "quantity on the market is the ordinary one and is sold at market value. If supply "
                  "falls short, the worst conditions regulate; &ldquo;If the demand exceeds the "
                  "supply but slightly, then the individual value of the unfavorably produced "
                  "commodities regulates the market-price.&rdquo; If supply far exceeds demand, the "
                  "best conditions do. So demand decides which group sets the price, and how far "
                  "market price departs from market value. What it does not decide, on his account, "
                  "is the value those prices move around."),
            ("p", "His argument for that is short. When supply and demand balance, &ldquo;they cease "
                  "to explain anything&rdquo;: two equal forces pulling opposite ways leave the "
                  "result to be explained by something else. He quotes an anonymous English writer "
                  "of 1821 who admits that the same commodity can have two different natural prices "
                  "at two times while supply and demand stand in the same proportion of equality, "
                  "and Marx draws the conclusion that the price is fixed independently of them."),
            ("p", "The opposing view should be heard at full strength. Alfred Marshall, whose "
                  "<em>Principles of Economics</em> appeared in 1890, before Engels published this "
                  "volume, said that asking whether value is governed by utility or by cost of "
                  "production is like asking which blade of a pair of scissors cuts; demand and "
                  "supply are the two blades. In his account the supply side carries "
                  "costs, and in the long run normal price tends to cost of production, much as "
                  "Marx's market value does; but the curves are drawn at every price, not only at "
                  "balance, and demand helps fix the quantity at which cost is measured. Marx's "
                  "tautology argument works against a theory that explains price by supply and "
                  "demand at balance only. Whether it reaches Marshall's is disputed."),
            ("p", "The chapter's second half returns to the whole economy. Capital "
                  "&ldquo;withdraws from spheres with low rates of profit and invades others which "
                  "yield a higher rate&rdquo;, and the movement changes supply in each until rates "
                  "equalise and values become prices of production. Everything said of market value, "
                  "Marx adds, applies to the price of production where it takes its place. And Marx "
                  "draws a sharp conclusion from the shared rate: every capitalist has a direct "
                  "interest in the exploitation of the whole working class, because his average "
                  "profit depends on it."),
            ("p", "The surplus profit of the better placed is the seed of a later Part. Where better "
                  "conditions cannot spread, because they rest on a waterfall or a fertile field, "
                  "surplus profit becomes rent. The next lesson, “Wage Changes and Prices of "
                  "Production”, takes the general rate as formed and asks what a general rise in "
                  "wages does to prices."),
        ],
        "lab": ("capkit", {
            "mode": "value",
            "view": "market",
            "money_unit": "hours",
            "qty_unit": "pieces",
            "preset": "average-dominates",
            "presets": [
                {"id": "average-dominates", "label": "The bulk at average conditions: 1,000 at 3 h, 8,000 at 4 h, 1,000 at 5 h",
                 "groups": [{"units": 1000, "hours": 3}, {"units": 8000, "hours": 4}, {"units": 1000, "hours": 5}],
                 "expect": {"vaMarketValue": "4 h", "vaSurplus": "+1 h, 0 h, −1 h"}},
                {"id": "worst-dominates", "label": "A large share at the worst: 1,000 at 3 h, 3,000 at 4 h, 6,000 at 5 h",
                 "groups": [{"units": 1000, "hours": 3}, {"units": 3000, "hours": 4}, {"units": 6000, "hours": 5}],
                 "expect": {"vaMarketValue": "9/2 h", "vaSurplus": "+3/2 h, +1/2 h, −1/2 h"}},
                {"id": "best-dominates", "label": "A large share at the best: 6,000 at 3 h, 3,000 at 4 h, 1,000 at 5 h",
                 "groups": [{"units": 6000, "hours": 3}, {"units": 3000, "hours": 4}, {"units": 1000, "hours": 5}],
                 "expect": {"vaMarketValue": "7/2 h", "vaSurplus": "+1/2 h, −1/2 h, −3/2 h"}},
            ],
            "panel_title": "One market value from many individual values",
            "panel_intro": (
                "Each group is typed as units sold and its own hours per unit. The lab takes the "
                "market value as the average over every unit, the reading Marx calls strict, "
                "and gives each group's gain or loss per unit. The total sold is the same "
                "10,000 in every preset: only the mix of conditions changes."
            ),
        }),
        "steps_title": "Computing a market value",
        "steps_intro": "Four steps for one trade selling its ordinary quantity.",
        "steps": [
            ("Total the hours",
             "For each group multiply units by hours per unit, and add the results."),
            ("Divide by the units",
             "The market value per unit is total hours divided by total units sold."),
            ("Compare each group",
             "Market value minus a group's own hours per unit is its surplus profit per unit; a "
             "negative figure is surplus value it produced and does not realise."),
            ("Say what demand would change",
             "If demand outruns the ordinary supply, the worst group's value tends to regulate the "
             "price; if supply far outruns demand, the best group's. The lab computes the ordinary "
             "case only."),
        ],
        "worked": {
            "title": "When the worst group is large",
            "intro": [
                "Take the worst-dominates preset. You want the market value and what each group "
                "gains or loses on a piece.",
            ],
            "lines": [
                "hours:  1,000·3 + 3,000·4 + 6,000·5 = 45,000",
                "pieces:  1,000 + 3,000 + 6,000 = 10,000",
                "market value:  45,000 / 10,000 = 9/2 h",
                "gains:  +3/2 h, +1/2 h, −1/2 h",
            ],
            "after": [
                "The market value is above the middle group's 4 hours and below the worst group's 5, "
                "as Marx says it must be in his second case. Nothing about demand changed between "
                "this preset and the first; only the mix of conditions did.",
            ],
        },
        "quiz_title": "Market value",
        "quiz": [
            {"q": "A trade sells 2,000 pieces made at 2 hours each and 2,000 made at 4 hours each. "
                  "On the lab's average, what is the market value of a piece?",
             "a": ["2 hours",
                   "4 hours",
                   "3 hours",
                   "6 hours"],
             "c": 2,
             "why": "Total hours are `2,000 · 2 + 2,000 · 4 = 12,000` for 4,000 pieces, so 3 hours. "
                    "Two and four hours are each group's own value; six adds the two."},
            {"q": "In the average-dominates preset, what does the group working at 3 hours a piece "
                  "realise beyond its own value on each piece?",
             "a": ["Nothing, because it sells at value",
                   "1 hour of surplus profit",
                   "3 hours",
                   "It loses 1 hour"],
             "c": 1,
             "why": "It sells at the market value of 4 hours what cost it 3, so it gains an hour a "
                    "piece. The 5-hour group is the one that loses an hour."},
            {"q": "On Marx's account in Chapter 10, what does a slight excess of demand over the "
                  "ordinary supply do?",
             "a": ["It raises the labour-time needed to make each piece",
                   "It has no effect on any price",
                   "It makes the best producers' value regulate the price",
                   "It makes the value of the goods made under the worst conditions regulate the market price"],
             "c": 3,
             "why": "Marx says that if demand exceeds supply slightly, the individual value of the "
                    "unfavourably produced goods regulates the market price. Nobody's hours change, "
                    "and the best producers regulate only when supply far exceeds demand."},
            {"q": "Why, according to Marx, can supply and demand not explain the level of market "
                  "value?",
             "a": ["Because when they balance they cancel and explain nothing, so the level they balance at needs another cause",
                   "Because demand does not exist under capitalism",
                   "Because supply is always fixed",
                   "Because Marshall had shown it"],
             "c": 0,
             "why": "That is the chapter's argument: balanced forces have no effect, so the price at "
                    "balance must be set by something else. Marx grants demand a real role in market "
                    "prices; supply is not fixed; and Marshall wrote later and argued the other way."},
        ],
        "mistakes": [
            ("Thinking supply and demand determine value",
             "In all three presets 10,000 pieces are sold and nothing about demand changes, yet the "
             "market value tile moves from 4 hours to 9/2 and to 7/2 as the mix of conditions "
             "changes. On Marx's account supply and demand move the market price around that figure "
             "and, when they are badly out of line, decide which group sets it; the figure itself "
             "comes from the hours. Marshall's scissors are the strongest reply, and the lesson "
             "states it."),
            ("Reading surplus profit as cheating or as a mark-up",
             "The 3-hour group in average-dominates sells at the same price as everyone. It gains "
             "an hour a piece because its own value is below the market value, not because it "
             "charges more."),
            ("Assuming the market value is always the middle group's value",
             "Only when the bulk is produced under average conditions. In best-dominates the "
             "middle group makes 4-hour pieces that sell at 7/2 hours, and it loses half an hour on "
             "each."),
        ],
        "standard": (
            "Finish when you can compute a market value and each group's surplus profit or loss.",
            "Given each group's units and hours per unit, compute the market value as the average "
            "over every unit, each group's gain or loss per unit, and state which group's share "
            "pulls the market value toward its own value."
        ),
        "note": (
            "The lab takes the market value as the average over every unit sold, which Marx calls "
            "the strict reading of his cases; it does not model his further point that a slight "
            "excess of demand lets the worst group's value regulate the price outright, or that a "
            "glut lets the best group's do so. The groups and hours are illustrative; Marx gives "
            "the three cases without figures."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 3, l. 2010 (wages rise 25%: the opening passage). Inline:
    # l. 2014-2016 (50 c + 62½ v, 16 1/12, 128 7/12), l. 2020 (116 4/7),
    # l. 2024-2028 (the three results), l. 2030 (the sum is unchanged),
    # l. 2038-2044 (wages fall by a quarter: 26 6/19%, "100 10/19" (a misprint for 110 10/19), 123 15/19),
    # l. 2052 (the only relevant question treated by Ricardo).
    {
        "slug": "wages-and-prices-of-production",
        "title": "Wage Changes and Prices of Production",
        "module": "Chapter 11 · Effects of General Fluctuations of Wages on Prices of Production",
        "one_line": "A general rise in wages lowers the general rate of profit; it leaves the price of the average sphere where it was, raises prices where wages are a large share of capital and lowers them where they are small.",
        "summary": (
            "Chapter 11 is short and is mostly arithmetic. Marx raises all wages by a quarter and "
            "recomputes the general rate of profit and three prices of production: the average "
            "sphere's, a low composition's and a high composition's. Compute the new rate over the "
            "enlarged capital, the new prices, and the direction each one moves."
        ),
        "key": [
            "a wage rise comes out of surplus value",
            "after a rise: p′ = profit left / new capital",
            "Marx: 15 on 105 = 14 2/7%",
            "average sphere: price unchanged",
            "lower c/v: price rises; higher: falls",
        ],
        "key_label": "A wage rise in five lines",
        "concepts_intro": (
            "The chapter answers one question. Marx calls it secondary, and also the only relevant "
            "question Ricardo treated."
        ),
        "concepts": [
            ("A wage rise is a fall in s′",
             "With the working day and the labour performed unchanged, the same workers still add "
             "the same new value. If more of it goes to wages, less is left as surplus value, so a "
             "general wage rise lowers the rate of surplus value and the general rate of profit."),
            ("The new general rate",
             "Marx reckons it on the average capital after the rise: 80c + 20v becomes 80c + 25v, "
             "whose 40 of new value now leaves 15 of profit on 105 of capital, 14 2/7%."),
            ("Three directions",
             "The average sphere's price stays at its value. A sphere of lower composition, more "
             "wages per hundred, sees its cost rise more than its profit falls; one of higher "
             "composition sees the reverse."),
        ],
        "read_title": "The passage first, then the three spheres",
        "read_intro": (
            "The passage is Marx's whole procedure for the average capital. He then repeats it for "
            "a capital below and one above the average."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 11.</strong> &ldquo;Let wages rise by 25%. Then the "
                  "same quantity of labor, which was formerly set in motion with 20, costs 25. "
                  "Instead of 80 c + 20 v + 20 p, we have then for the value of one turn-over "
                  "80 c + 25 v + 15 p. The labor set in motion by the variable capital still produces "
                  "a value of 40, the same as before. If v rises from 20 to 25, then the surplus p, or "
                  "s, amounts only to 15. The profit of 15 on a capital of 105 is 14 2/7%, and this "
                  "would be the new average rate of profit.&rdquo;"),
            ("p", "When wages rise across an economy, a common first thought is that every price "
                  "must rise with them. It has a distinguished source. Adam Smith wrote in 1776 that "
                  "wages, profit and rent are the three component parts of price, so that raising "
                  "one raises the whole, and on that view higher wages are passed on as higher prices "
                  "everywhere. David Ricardo disagreed in his <em>Principles</em> of 1817: a rise in "
                  "wages lowers profits, and it changes relative prices, lowering those of goods made "
                  "with much fixed capital. Chapter 11 is Marx's version of Ricardo's point, with "
                  "prices of production in place of Ricardo's values."),
            ("p", "Read the passage line by line. The labour bought is the same, so it still adds 40 "
                  "of new value. Wages take 25 of it instead of 20, and 15 is left. The average "
                  "sphere's price is still 80 + 25 + 15 = 120, its value: Marx says the rise "
                  "&ldquo;would have brought about a reduction of profits, but no change in the value "
                  "and price of the commodities&rdquo;. The new rate is reckoned on the capital as "
                  "it now stands, 105, so it is `15/105 = 1/7`, or 14 2/7%."),
            ("p", "Now a sphere below the average, 50c + 50v, which sold at 120 before. Its wages "
                  "rise to 62½, its cost price to 112½, and it must now earn 14 2/7% on 112½. Exactly, "
                  "that is 16 1/14, and the price is 128 4/7. The Kerr text prints &ldquo;16 "
                  "1/12&rdquo; and &ldquo;128 7/12&rdquo;; Marx called it &ldquo;a round "
                  "profit&rdquo;, and the lab prints the exact figure, 900/7. A sphere above the "
                  "average, 92c + 8v, has wages rise from 8 to 10 and a cost price of 102, and at the "
                  "new rate sells at 116 4/7, or 816/7."),
            ("p", "The <strong>marx</strong> preset computes all three: a new general rate of 1/7 and "
                  "prices of £120, £900/7 and £816/7, with the table marking them unchanged, rising "
                  "and falling. The text's own summary is that the low composition's price "
                  "&ldquo;rises, but not in the same proportion in which the profit falls&rdquo;, and "
                  "the high composition's &ldquo;falls, but not as much as the profit&rdquo;."),
            ("def", ("General rate after a wage rise",
                     "The average capital's profit after the extra wages are paid, divided by that "
                     "capital as enlarged by them: (p′ · (c + v) − w · v) / (c + v + w · v), where w "
                     "is the rise in money wages.")),
            ("p", "Why do the prices move at all? Because the rate must be equal everywhere. If the "
                  "low-composition sphere kept its price of 120, its profit would be 7½ on 112½, 6 2/3%, "
                  "far below the new average; if the high-composition sphere kept its price, it would "
                  "earn more than the average. Prices move until each earns 14 2/7% again. "
                  "No sphere is compensated for the wage rise: the price rise in one and the fall "
                  "in the other leave both at the same reduced average profit."),
            ("p", "And the totals still hold. Since the average sphere's price is unchanged and "
                  "equal to its value, Marx says, the sum of all prices of production stays equal to "
                  "the sum of values. The <strong>two-spheres</strong> preset shows it with two "
                  "illustrative capitals that together have the average composition, 70c + 30v and "
                  "90c + 10v, with all of the economy as the average capital. After a 25% rise the "
                  "rate is again 1/7, and the prices, £860/7 and £820/7, rise and fall by exactly "
                  "the same amount: they still sum to £240."),
            ("p", "Marx then reverses the case, which he notes Ricardo did not analyse. Let wages "
                  "fall by a quarter. The average capital becomes 80c + 15v + 25 of profit, still 120, "
                  "and the rate rises to 25 on 95, 26 6/19%. The <strong>fall</strong> preset runs "
                  "it: prices of £120 for the average sphere, £2,100/19 for 50c + 50v (now 50c + 37½v), "
                  "and £2,352/19, or 123 15/19, for 92c + 8v, a rise. The first of those is 87½ + 23 "
                  "1/38 = 110 10/19; the Kerr text adds the same two figures and prints 100 10/19, a "
                  "slip the lab does not repeat. Every direction is reversed."),
            ("p", "The chapter's lesson for a reader of the news is narrow but sharp: on this "
                  "accounting, a general wage rise is paid out of profits, and it shifts relative "
                  "prices without raising the price level. The lab knows nothing of money or of "
                  "monetary policy, which is where most modern arguments about wages and prices "
                  "live, and it assumes the working day and the labour performed stay fixed."),
            ("p", "Chapters 8 to 11 have shown how the general rate is formed and how it "
                  "moves. The next lesson, “Supplementary Remarks on Prices of Production”, asks what "
                  "the capitalist's own reasons for a higher price, risk and slow turnover, amount "
                  "to inside a fixed total."),
        ],
        "lab": ("capkit", {
            "mode": "prices",
            "view": "wage-rise",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 80c + 20v, 50c + 50v and 92c + 8v at 20%; wages rise 25%",
                 "spheres": [{"name": "average", "c": 80, "v": 20}, {"name": "lower", "c": 50, "v": 50},
                             {"name": "higher", "c": 92, "v": 8}],
                 "profit_rate": "1/5", "wage_rise": "1/4", "average": "average", "expect": {"ppAverage": "1/7 = 14.29%", "ppPrices": "£120, £900/7, £816/7"}},
                {"id": "two-spheres", "label": "70c + 30v and 90c + 10v at 20%, the whole as the average; wages rise 25%",
                 "spheres": [{"name": "lower", "c": 70, "v": 30}, {"name": "higher", "c": 90, "v": 10}],
                 "profit_rate": "1/5", "wage_rise": "1/4", "average": "", "expect": {"ppAverage": "1/7 = 14.29%", "ppPrices": "£860/7, £820/7"}},
                {"id": "fall", "label": "Marx's figures: the same three spheres; wages fall by a quarter",
                 "spheres": [{"name": "average", "c": 80, "v": 20}, {"name": "lower", "c": 50, "v": 50},
                             {"name": "higher", "c": 92, "v": 8}],
                 "profit_rate": "1/5", "wage_rise": "-1/4", "average": "average", "expect": {"ppAverage": "5/19 = 26.32%", "ppPrices": "£120, £2,100/19, £2,352/19"}},
            ],
            "panel_title": "Prices of production after a change in wages",
            "panel_intro": (
                "Each sphere is typed as name, c, v, all of c used up and one turnover a year. The "
                "extra wages come out of surplus value; the new general rate is the average "
                "capital's remaining profit over that capital as enlarged. Every price is then cost "
                "price plus the new rate on the new capital. A fall in wages is a negative rise."
            ),
        }),
        "steps_title": "Repricing after a general wage rise",
        "steps_intro": "Four steps, in Marx's order.",
        "steps": [
            ("Take the average capital",
             "Raise its v by the wage rise. Its new value added is unchanged, so its profit falls "
             "by exactly the extra wages."),
            ("Compute the new general rate",
             "Divide the average capital's remaining profit by its capital after the rise, c plus "
             "the new v."),
            ("Reprice each sphere",
             "Raise each sphere's v by the same share; its new price is its new cost price plus the "
             "new rate on its new capital."),
            ("Classify the change",
             "Compare each new price with the old: unchanged at average composition, higher below "
             "it, lower above it."),
        ],
        "worked": {
            "title": "Marx's three spheres after a 25% rise",
            "intro": [
                "Start from a general rate of 20% and the average 80c + 20v. You want the new rate "
                "and the new prices of 50c + 50v and 92c + 8v.",
            ],
            "lines": [
                "average:  15 / (80 + 25) = 1/7",
                "lower:  (50 + 62½) · 8/7 = 900/7",
                "900/7 = 128 4/7, up from 120",
                "higher:  (92 + 10) · 8/7 = 816/7",
                "816/7 = 116 4/7, down from 120",
            ],
            "after": [
                "Adding the rate of 1/7 to a cost price is multiplying it by 8/7. The average sphere "
                "stays at `105 · 8/7 = 120`, its value.",
            ],
        },
        "quiz_title": "Wages and prices of production",
        "quiz": [
            {"q": "The average capital is 80c + 20v at a general rate of 20%. Wages rise by 50%. "
                  "What is the new general rate, reckoned as Marx reckons it?",
             "a": ["1/10",
                   "1/11",
                   "1/5",
                   "1/6"],
             "c": 1,
             "why": "Wages become 30, so profit falls from 20 to 10, and the capital is now 110: "
                    "`10/110 = 1/11`. One tenth reckons the profit on the old capital of 100; 1/5 "
                    "ignores the rise; 1/6 is not any of the quantities."},
            {"q": "After a general rise in wages, what happens to the price of production of a "
                  "sphere of average composition?",
             "a": ["It rises by the wage rise",
                   "It falls by the fall in profit",
                   "It rises by half the wage rise",
                   "It stays the same"],
             "c": 3,
             "why": "Its wages rise by exactly what its profit loses, so cost price plus profit is "
                    "unchanged, and it still sells at its value. Marx's 80c + 25v + 15p is still 120."},
            {"q": "In the fall preset, wages fall by a quarter. Which sphere's price rises?",
             "a": ["50c + 50v, the lower composition",
                   "80c + 20v, the average",
                   "92c + 8v, the higher composition",
                   "None of them"],
             "c": 2,
             "why": "The general rate rises to 26 6/19%, and the higher composition, whose cost "
                    "falls only from 100 to 98, gains more from the higher rate than it saves on "
                    "wages: 123 15/19. The lower composition falls to 110 10/19 and the average stays "
                    "at 120."},
            {"q": "Why must the low-composition sphere's price rise after a wage rise?",
             "a": ["Because at the old price it would earn far less than the new general rate",
                   "Because its workers produce more value than before",
                   "Because its capitalists pass the whole wage rise on",
                   "Because its surplus value rises"],
             "c": 0,
             "why": "At 120 it would earn 7½ on 112½, 6 2/3%, against a general rate of 14 2/7%, and "
                    "capital would leave it. Its workers produce the same value; the price rises by "
                    "less than the wage rise; and its surplus value falls."},
        ],
        "mistakes": [
            ("Thinking a general wage rise raises all prices",
             "That is the reading of Smith's component parts of price. In the marx preset the "
             "prices tile reads £120, £900/7, £816/7: the average sphere unchanged, the low "
             "composition up to 128 4/7 and the high composition down to 116 4/7. A general rise "
             "comes out of profit and only rearranges relative prices; in the two-spheres preset "
             "the two prices still sum to £240."),
            ("Reckoning the new rate on the old capital",
             "Marx divides the remaining profit by the capital after the rise: 15 on 105, not 15 on "
             "100. The difference is between 1/7 and 3/20, and the lab's general rate tile reads 1/7."),
            ("Taking the printed 128 7/12 as exact",
             "The text's &ldquo;16 1/12&rdquo; and &ldquo;128 7/12&rdquo; are rounded: 14 2/7% of "
             "112½ is 16 1/14, and the price is 128 4/7. The lab prints £900/7. Nothing in the "
             "argument depends on the difference, but a quotation is not a calculation."),
        ],
        "standard": (
            "Finish when you can reprice spheres after a general change in wages.",
            "Given the average capital, the old general rate, the spheres' c and v and a change in "
            "money wages, compute the new general rate over the capital after the change, each "
            "sphere's new price of production, and classify each as rising, falling or unchanged."
        ),
        "note": (
            "The lab, like the chapter, holds the working day, the labour performed and the value of "
            "the inputs fixed, and assumes one turnover a year with all of c used up. A wage change "
            "that came from a change in the value of the workers' necessities would also change "
            "some inputs, which Marx sets aside. The marx and fall figures are Marx's; two-spheres "
            "is illustrative."
        ),
    },
]
