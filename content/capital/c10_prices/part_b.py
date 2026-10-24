"""Average Profit and Its Fall, lessons 5-8 -- Volume III, Chapter 12 and Part III, Chapters 13-15, one lesson per chapter.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, and the translator's double quotation marks inside a quotation
are printed as single curly quotes. Nothing else is changed: Chapter 13's
"66 1/3%" is the Kerr text's misprint for 66 2/3%, kept inside the quotation
and pointed out in the lesson. Marx's p' (the rate of profit) is printed with
a curly apostrophe inside quotations, p&rsquo;.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Kerr vol. 3, l. 2110 (the claims for compensation: the opening
    # passage). Inline: l. 2066 (a change in other commodities), l. 2074
    # (all changes reduce to changes in value), l. 2090 (the sphere of
    # average composition), l. 2100 (everything appears upside down),
    # l. 2106 (capitals of the same magnitude), l. 2108 (turnover, shipping),
    # l. 2110 (insurance).
    {
        "slug": "supplementary-remarks-on-prices",
        "title": "Supplementary Remarks on Prices of Production",
        "module": "Chapter 12 · Some After Remarks",
        "one_line": "A capitalist who claims a higher price for risk or slow turnover is claiming a larger share of a fixed total of surplus value, and every such premium is paid out of everyone else's rate.",
        "summary": (
            "Chapter 12 gathers three remarks. A price of production changes only through a change "
            "in value, its own or other commodities'; a sphere of average composition behaves as if "
            "it sold at value; and the reasons capitalists give one another for higher prices are "
            "claims on one pool. Compute prices of production with a premium for one sphere and see "
            "the general rate fall to pay for it."
        ),
        "key": [
            "every price change goes back to value",
            "average c/v: price = value, always",
            "a premium shares out the same total s",
            "base rate = (Σ s − premiums) / Σ C",
            "competition shows prices, not values",
        ],
        "key_label": "Chapter 12 in five lines",
        "concepts_intro": (
            "The chapter has three numbered sections, and each takes one of these ideas."
        ),
        "concepts": [
            ("Two causes of a price change",
             "A price of production changes only if the general rate changes, which needs a change "
             "in value somewhere in the economy, or if the commodity's own value changes. Either "
             "way the cause is a change in labour-time."),
            ("The sphere of average composition",
             "Its profit equals its surplus value, so a change in wages moves its profit and leaves "
             "its price alone, exactly as if it sold at value."),
            ("Grounds for compensation",
             "Slow turnover, distant markets and danger are allowed for in prices. Marx's point is "
             "that each allowance divides the same total surplus value differently; none adds to it."),
        ],
        "read_title": "The passage first, then the three sections",
        "read_intro": (
            "The passage is from the chapter's third section, on what capitalists allow for. The "
            "first two sections are short and are taken in order after it."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 12, §3.</strong> &ldquo;The capitalist simply "
                  "forgets, or rather he does not see, because competition does not show it to him, "
                  "that all these claims for compensation mutually advanced by the capitalists in the "
                  "calculation of the prices of commodities of different lines of production repeat "
                  "in another way the idea that all capitalists are entitled, in proportion to the "
                  "magnitude of their respective capitals, to equal shares of the common loot, the "
                  "total surplus-value.&rdquo;"),
            ("p", "Insurance makes the idea familiar. A shipowner pays a higher premium than a baker, "
                  "and the freight he charges covers it. Marx's example is the same: capitals "
                  "&ldquo;exposed to considerable danger, for instance in shipping, should be "
                  "compensated by a raise in prices&rdquo;, and once insurance is developed the "
                  "danger is spread over everyone, while the dangerous trades pay higher premiums "
                  "and recover them in their prices. The other standard claim is turnover: a capital "
                  "turned over slowly, because production is long or markets far away, "
                  "&ldquo;should nevertheless charge the profit it loses in this way&rdquo;."),
            ("p", "Marx does not deny that these allowances are made, or that they belong in prices "
                  "of production; Chapter 9 already allotted profit &ldquo;in proportion to its "
                  "conditions of turn-over&rdquo;. What he denies is the capitalist's reading of "
                  "them. Each claim, read alone, seems to create profit: a premium added to a price. "
                  "Read together they are a rule for sharing what exists, the stock company of "
                  "Chapter 9 with some shares weighted more heavily."),
            ("p", "The lab makes that a sum. Take Marx's five spheres from Chapter 9, with 110 of "
                  "surplus value on 500 of capital. With no premiums, the <strong>none</strong> "
                  "preset gives the familiar 22% and prices of £92, £103, £113, £77 and £37. In "
                  "<strong>risk-premium</strong>, sphere V, the one with most capital per worker, is "
                  "allowed 5% on top of the general rate for danger. Its 5 has to come from "
                  "somewhere: the base rate falls to 21%, every other sphere's price falls by 1, V's "
                  "rises by 4, and the totals tile still reads values £422 = prices £422; s £110 = "
                  "profit £110."),
            ("def", ("Ground for compensation",
                     "A circumstance, such as slow turnover or danger, for which a sphere's price "
                     "allows a profit above the general rate. On the chapter's account it is paid out "
                     "of the same total surplus value, so it lowers the rate left for the others.")),
            ("p", "In <strong>turnover-premium</strong>, sphere I, a capital with a slow turnover, "
                  "is allowed 10% extra. The base rate falls to 20%, I sells at £100 instead of £92, "
                  "the others at £101, £111, £75 and £35, and the totals do not move. However the "
                  "claims are set, the base rate is the surplus value left after the premiums, "
                  "divided by the whole capital."),
            ("p", "The chapter's first section makes the same point from the other side. A price of "
                  "production can change only if the general rate changes, or if the commodity's own "
                  "value changes. If it changes through the general rate, &ldquo;its own value may "
                  "have remained unchanged, but a change must have taken place in the value of other "
                  "commodities.&rdquo; Hence &ldquo;All changes in the price of production of "
                  "commodities reduce themselves in the last analysis to changes in value.&rdquo;"),
            ("p", "The second section shows why the sphere of average composition is the anchor. "
                  "Even if its inputs are bought at prices that differ from their values, what matters "
                  "is that its v is the same share of its capital as in the whole. Then its surplus "
                  "value equals the average profit, and a rise or fall in wages changes its profit, "
                  "never its price. The previous lesson's average sphere, unchanged at 120 after the "
                  "wage rise, was this rule at work."),
            ("p", "Why does the capitalist not see the pool? Because competition shows him the "
                  "average rate, the movement of prices with wages, and market prices gathering "
                  "round prices of production, and none of these shows labour-time. "
                  "&ldquo;Everything appears upside down in competition.&rdquo; The rise of a price "
                  "with wages, which looks like a refutation of the law of value, was in the last "
                  "lesson its consequence."),
            ("p", "There is a strong objection to the whole frame, and it belongs here. A modern "
                  "economist would say that a risk premium is not a share of a pool but a price: "
                  "investors who could earn the safe rate elsewhere must be paid more to hold a risky "
                  "asset, and profit itself, as Frank Knight argued in <em>Risk, Uncertainty and "
                  "Profit</em> (1921), is the reward for bearing an uncertainty no insurance covers. "
                  "On that account the premium is earned, not redistributed. What in the chapter "
                  "bears on it is its accounting: the claims repeat the idea of equal shares in one "
                  "total, so any premium in one place is a deduction somewhere else. The lab computes inside that accounting, and cannot say whether "
                  "the total is fixed in the way the chapter assumes."),
            ("p", "That ends Part II: the general rate of profit is formed, and it moves with the "
                  "composition of the whole capital. The next lesson, “The Falling Rate of Profit: "
                  "The Law as Such”, asks what happens to that rate as the composition keeps rising."),
        ],
        "lab": ("capkit", {
            "mode": "prices",
            "view": "production",
            "money_unit": "£",
            "preset": "none",
            "presets": [
                {"id": "none", "label": "Marx's five spheres, no premiums",
                 "spheres": [{"name": "I", "c": 80, "v": 20, "c_used": 50},
                             {"name": "II", "c": 70, "v": 30, "c_used": 51},
                             {"name": "III", "c": 60, "v": 40, "c_used": 51},
                             {"name": "IV", "c": 85, "v": 15, "c_used": 40},
                             {"name": "V", "c": 95, "v": 5, "c_used": 10}],
                 "s_rate": 1, "premiums": [], "expect": {"ppAverage": "11/50 = 22%", "ppPrices": "£92, £103, £113, £77, £37", "ppTotals": "values £422 = prices £422; s £110 = profit £110"}},
                {"id": "risk-premium", "label": "The same, with 5% extra for danger in sphere V",
                 "spheres": [{"name": "I", "c": 80, "v": 20, "c_used": 50},
                             {"name": "II", "c": 70, "v": 30, "c_used": 51},
                             {"name": "III", "c": 60, "v": 40, "c_used": 51},
                             {"name": "IV", "c": 85, "v": 15, "c_used": 40},
                             {"name": "V", "c": 95, "v": 5, "c_used": 10}],
                 "s_rate": 1, "premiums": [{"sphere": "V", "rate": "1/20"}], "expect": {"ppAverage": "21/100 = 21%", "ppPrices": "£91, £102, £112, £76, £41", "ppTotals": "values £422 = prices £422; s £110 = profit £110"}},
                {"id": "turnover-premium", "label": "The same, with 10% extra for slow turnover in sphere I",
                 "spheres": [{"name": "I", "c": 80, "v": 20, "c_used": 50},
                             {"name": "II", "c": 70, "v": 30, "c_used": 51},
                             {"name": "III", "c": 60, "v": 40, "c_used": 51},
                             {"name": "IV", "c": 85, "v": 15, "c_used": 40},
                             {"name": "V", "c": 95, "v": 5, "c_used": 10}],
                 "s_rate": 1, "premiums": [{"sphere": "I", "rate": "1/10"}], "expect": {"ppAverage": "1/5 = 20%", "ppPrices": "£100, £101, £111, £75, £35", "ppTotals": "values £422 = prices £422; s £110 = profit £110"}},
            ],
            "panel_title": "Premiums paid out of one total",
            "panel_intro": (
                "The spheres are Marx's from Chapter 9. A premium is typed as sphere, extra rate. "
                "The lab pays every premium out of total surplus value first, divides what is left by "
                "the whole capital for the base rate, and prices each sphere at cost price plus its "
                "rate on its capital. Watch the totals tile as the premiums change."
            ),
        }),
        "steps_title": "Pricing with a ground for compensation",
        "steps_intro": "Four steps, with every premium paid from the same total.",
        "steps": [
            ("Total the surplus value and the capital",
             "Add every sphere's s and every sphere's whole capital, as for the general rate."),
            ("Pay the premiums first",
             "For each sphere with a premium, multiply its extra rate by its capital, and subtract "
             "the results from total surplus value."),
            ("Compute the base rate",
             "Divide what is left by the total capital. Every sphere gets the base rate, and the "
             "favoured ones get their premium on top."),
            ("Price and check",
             "Price each sphere at cost price plus its rate on its capital, and check that total "
             "profit still equals total surplus value."),
        ],
        "worked": {
            "title": "A premium for danger in sphere V",
            "intro": [
                "Marx's five spheres make 110 of surplus value on 500 of capital. Sphere V, with a "
                "capital of 100, is allowed 5% extra. You want the base rate and V's price.",
            ],
            "lines": [
                "premium:  5% · 100 = 5",
                "base rate:  (110 − 5) / 500 = 21%",
                "V's profit:  (21% + 5%) · 100 = 26",
                "V's price:  15 + 26 = 41",
                "total profit:  4 · 21 + 26 = 110",
            ],
            "after": [
                "V gains 4 over its price without the premium, and the four other spheres lose 1 "
                "each. The premium moved 4 of surplus value; it created none.",
            ],
        },
        "quiz_title": "Compensation within a fixed total",
        "quiz": [
            {"q": "Five spheres of 100 each make 110 of surplus value. One sphere is allowed a 10% "
                  "premium. What rate do the other four receive?",
             "a": ["22%",
                   "12%",
                   "20%",
                   "32%"],
             "c": 2,
             "why": "The premium takes `10% · 100 = 10`, leaving 100 on 500, 20% for everyone, with "
                    "the favoured sphere at 30%. Twenty-two per cent ignores the premium; 12% "
                    "subtracts it from the rate instead of sharing it; 32% adds it to the others."},
            {"q": "On the chapter's account, what does a risk premium in shipping do to total profit "
                  "in the economy?",
             "a": ["It raises total profit by the premium",
                   "Nothing: it changes how total surplus value is shared",
                   "It lowers total profit by the premium",
                   "It raises total profit only if insurance is developed"],
             "c": 1,
             "why": "That is the passage: the claims for compensation repeat the idea that capitals "
                    "share the total surplus value in proportion to their size. In the risk-premium "
                    "preset the totals tile is unchanged at £110."},
            {"q": "The general rate of profit falls while the value of a commodity stays the same. "
                  "According to Chapter 12, what must have happened?",
             "a": ["Nothing: the general rate moves by itself",
                   "Demand for the commodity fell",
                   "The commodity's own price of production rose",
                   "The value of other commodities changed"],
             "c": 3,
             "why": "Marx's rule: if a price of production changes through the general rate, its own "
                    "value may be unchanged, but the value of other commodities must have changed. "
                    "Demand moves market prices, not the general rate, and a rise in its own price of production reverses "
                    "the question."},
            {"q": "Wages rise generally. What happens to the price of production of a sphere of "
                  "average composition, on Chapter 12's account?",
             "a": ["It is unchanged; only its profit falls",
                   "It rises by the wage rise",
                   "It falls with the general rate",
                   "It cannot be said without knowing its inputs' prices"],
             "c": 0,
             "why": "Its surplus value equals the average profit, so a wage rise moves its profit "
                    "and not its price, as if it sold at value. Marx says this holds even when its "
                    "inputs are bought at prices that differ from their values."},
        ],
        "mistakes": [
            ("Thinking each compensation adds new profit",
             "That is the capitalist's reading, and Marx says competition hides the rest from him. "
             "In the risk-premium preset sphere V's price rises from £37 to £41, every other price "
             "falls by £1, the general rate tile drops from 22% to 21%, and the totals tile still "
             "reads s £110 = profit £110. The premium is a larger share of the same pool."),
            ("Thinking the chapter calls the allowances illegitimate",
             "Marx says turnover and danger are reckoned into prices of production, and Chapter 9 "
             "already allots profit in proportion to turnover. His objection is to the idea that "
             "the allowance is a source of profit, not to its being made."),
            ("Treating every change in a price of production as a change in its own value",
             "A price can move because the general rate moved, while the commodity's own labour-time "
             "is unchanged. Chapter 12's rule is only that some value, somewhere, has changed."),
        ],
        "standard": (
            "Finish when you can price spheres with a premium paid from total surplus value.",
            "Given the spheres of a general-rate table and a premium for one or more of them, "
            "compute the base rate after the premiums, each sphere's price of production, and "
            "check that total profit still equals total surplus value."
        ),
        "note": (
            "The lab, like the chapter, takes total profit as fixed by total surplus value, so any "
            "premium must lower someone else's rate. That is the assumption a theory of profit as a "
            "reward for bearing risk denies, and the lab cannot test it. The spheres are Marx's; "
            "the premiums are illustrative, since the chapter gives none in figures."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 3, l. 2122-2128 (Marx's table: the opening passage); l. 2135
    # (a peculiar expression of rising productivity). Inline: l. 2143 (66 2/3%
    # written correctly), l. 2167-2174 (two to three million; 4 c + 2 v + 2 s
    # against 15 c + 3 v + 3 s), l. 2208 (the capital must be doubled),
    # l. 2220 (100 at 25%, 400 at 5%), l. 2232 (within certain limits).
    {
        "slug": "the-law-as-such",
        "title": "The Falling Rate of Profit: The Law as Such",
        "module": "Chapter 13 · The Theory of the Law",
        "one_line": "At a constant rate of surplus value, a rising composition of capital lowers the rate of profit, while the mass of profit can keep growing as the capital grows.",
        "summary": (
            "Part III opens with the most debated law in Volume III. If each worker sets more means "
            "of production in motion while the rate of surplus value stays the same, surplus value "
            "falls relative to the whole capital, and the rate of profit falls. Compute Marx's "
            "table of falling rates, and his illustration in which the rate halves while the mass "
            "of profit rises by half."
        ),
        "key": [
            "p′ = s′ · v / (c + v)",
            "s′ fixed, c/v up: p′ down",
            "Marx: 66 2/3% → 20% as c: 50 → 400",
            "mass of profit = p′ · capital",
            "mass up only if capital grows faster",
        ],
        "key_label": "The law in five lines",
        "concepts_intro": (
            "The law is simple to state, and Marx says so. What is hard is what he claims it "
            "expresses, and the step critics refuse."
        ),
        "concepts": [
            ("The rising composition",
             "Accumulation brings machinery and more materials per worker, so c grows faster than "
             "v. Marx takes this from Volume I as the form that rising productivity takes under "
             "capitalism."),
            ("The rate falls",
             "With s′ constant, s grows with v and the capital grows with c + v, so s / (c + v) "
             "falls. It falls, Marx insists, because labour has become more productive, not less."),
            ("The mass can rise",
             "The rate is profit per hundred; the mass is profit in all. A capital growing fast "
             "enough can make more profit at a lower rate, and Marx calls the two movements "
             "different sides of one law."),
        ],
        "read_title": "Marx's table first, then the law it expresses",
        "read_intro": (
            "The chapter opens with five lines of arithmetic. They are quoted as the Kerr text "
            "prints them, misprint included."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 13.</strong> &ldquo;Take it that the rate of "
                  "surplus-value is 100%. Now, if c = 50, and v = 100, then p&rsquo; = 100/150, or "
                  "66 1/3%. c = 100, and v = 100, then p&rsquo; = 100/200, or 50%. c = 200, and "
                  "v = 100, then p&rsquo; = 100/300, or 33 1/3%. c = 300, and v = 100, then "
                  "p&rsquo; = 100/400, or 25%. c = 400, and v = 100, then p&rsquo; = 100/500, or "
                  "20%.&rdquo;"),
            ("p", "The first line has a misprint: 100/150 is 66 2/3%, which is how the text writes it "
                  "a few pages later (Kerr page 250, against the table's 247). Otherwise the table "
                  "is exactly what it looks like. A hundred "
                  "pounds of wages employ the same workers at the same rate of exploitation in every "
                  "line, and make 100 of surplus value. Only the means of production behind them "
                  "grow, from 50 to 400, and the rate of profit falls from two-thirds to a fifth. The "
                  "<strong>marx</strong> preset runs the table: the tiles for the last period read a "
                  "rate of 1/5 and a mass of £100."),
            ("p", "<strong>Volume III, Chapter 13.</strong> &ldquo;This progressive tendency of the "
                  "average rate of profit to fall is, therefore, but a peculiar expression of "
                  "capitalist production for the fact that the social productivity of labor is "
                  "progressively increasing.&rdquo;"),
            ("p", "That sentence carries the argument. The same number of workers, Marx says, work "
                  "up more and more raw material with more and more machinery, so each product holds "
                  "less labour and is cheaper. The capital that sets them to work grows in value, "
                  "though not as fast as in mass. If the worker's paid and unpaid hours keep their "
                  "proportion, the unpaid labour shrinks relative to everything the capital advances. "
                  "The rate falls; and Marx adds, in a parenthesis, that the fall &ldquo;does not "
                  "manifest itself in an absolute form, but rather as a tendency toward a progressive "
                  "fall&rdquo;, with the reasons it does not fall faster left for the next chapter."),
            ("def", ("The law of the falling tendency of the rate of profit",
                     "At a given rate of surplus value, a rising organic composition of the social "
                     "capital expresses itself in a falling general rate of profit. Marx states it as "
                     "a tendency, checked by influences the next chapter lists.")),
            ("p", "A falling rate does not mean falling profits, and Marx spends much of the chapter "
                  "on the difference. His illustration is a working population that grows from two "
                  "million to three, its variable capital from two million to three, while the "
                  "constant capital grows from four million to fifteen. In his notation, in "
                  "millions, I is 4c + 2v + 2s at 33 1/3% and II is &ldquo;15 c + 3 v + 3 s; C = 18, "
                  "p&rsquo; = 16 2/3%.&rdquo; Then: &ldquo;While the mass of surplus-value has "
                  "increased by one-half, the rate of profit has fallen by one-half.&rdquo; The "
                  "<strong>mass-rises</strong> preset makes the whole change in its first period, "
                  "the capital half as large again and 9 million added to c, and holds it there: the "
                  "last period reads 1/6 and £3,000,000."),
            ("p", "The rule behind it is one Marx spells out. To keep the mass of profit the same "
                  "when the rate halves, the capital must double; to raise it, the capital must grow "
                  "faster than the rate falls. And the reverse is possible: &ldquo;For 100 at 25% make "
                  "25, while 400 at 5% make only 20.&rdquo; Nothing guarantees that a growing capital "
                  "makes more profit; Marx's claim is that accumulation, which raises the composition, "
                  "also makes the capital grow fast enough, &ldquo;aside from temporary "
                  "fluctuations&rdquo;."),
            ("p", "A rising composition is not the same thing as accumulation. In the "
                  "<strong>steady</strong> preset a capital of 800c + 200v doubles four times at the "
                  "same composition: the rate stays at 1/5 and the mass of profit grows from £200 to "
                  "£3,200. Marx makes the same point in the chapter: &ldquo;The fall of the rate of "
                  "profit is not due to an absolute, but only to a relative decrease of the variable "
                  "part of the total capital&rdquo;. Accumulation lowers the rate only when it changes "
                  "the proportions of c and v."),
            ("p", "Now the step critics refuse, because the lesson takes it. Marx holds s′ at 100% "
                  "while productivity rises. But the rising productivity that raises the composition "
                  "also cheapens the workers' necessities, which on Volume I's own account raises the "
                  "rate of surplus value. Joan Robinson and Paul Sweezy both pressed this in 1942: "
                  "hold s′ fixed and real wages must be rising with productivity; let s′ rise and "
                  "nothing in the table says whether the composition or the rate of surplus value "
                  "wins. What in the chapter bears on it is this: Marx says the mass of profit in a single "
                  "commodity may grow with a rising rate of surplus value &ldquo;only within certain "
                  "limits&rdquo;, and that, with the exception of a few cases, &ldquo;the rate of profit "
                  "will fall in spite of the increased rate of surplus-value&rdquo;; the next two "
                  "chapters argue those limits. Whether they hold is argued to this day, and this "
                  "course does not decide it."),
            ("p", "Marx claims the law as his own discovery, and says that &ldquo;all of political economy has so "
                  "far tried in vain to discover it&rdquo;. Smith and Ricardo had both expected profits "
                  "to fall, Smith because competition among growing capitals would press them down, "
                  "Ricardo because feeding the workers from worse and worse land would raise wages. Marx's law needs neither "
                  "competition nor nature: on his definitions it follows from productivity itself."),
            ("p", "If the law is so simple, why does the rate not fall faster? The next lesson, "
                  "“Counteracting Influences”, takes Marx's six answers one at a time."),
        ],
        "lab": ("capkit", {
            "mode": "tendency",
            "view": "law",
            "money_unit": "£",
            "periods": 4,
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's table: v = 100 at 100%, c rising from 50 to 400",
                 "c": 50, "v": 100, "s_rate": 1, "c_step": [50, 100, 100, 100], "capital_growth": [],
                 "expect": {"teRate": "1/5 = 20%", "teMass": "£100"}},
                {"id": "mass-rises", "label": "Marx's figures: 4c + 2v to 15c + 3v, in millions, in one period",
                 "c": 4000000, "v": 2000000, "s_rate": 1, "c_step": [9000000, 0, 0, 0],
                 "capital_growth": ["1/2", 0, 0, 0], "expect": {"teRate": "1/6 = 16.67%", "teMass": "£3,000,000"}},
                {"id": "steady", "label": "800c + 200v doubling each period at the same composition",
                 "c": 800, "v": 200, "s_rate": 1, "c_step": [], "capital_growth": [1],
                 "expect": {"teRate": "1/5 = 20%", "teMass": "£3,200"}},
            ],
            "panel_title": "The rate of profit as the composition rises",
            "panel_intro": (
                "Each period the whole capital first grows by the growth figure, c and v alike, and "
                "then c rises by the step. The rate of surplus value stays fixed. The table gives "
                "every period; the tiles give the last. Compare c/v with p′ in the marx preset's "
                "table, and the rate with the mass in mass-rises."
            ),
        }),
        "steps_title": "Following the law through a table",
        "steps_intro": "Four steps for any sequence of capitals at one rate of surplus value.",
        "steps": [
            ("Write each period's capital",
             "For each period give c and v. Where the whole capital grows, scale both; where the "
             "composition rises, add to c."),
            ("Compute surplus value",
             "Multiply v by the fixed rate of surplus value."),
            ("Compute the rate",
             "Divide s by c + v. With s′ fixed, the rate falls exactly when c/v rises."),
            ("Compute the mass",
             "The mass of profit is s itself. Compare its growth with the fall in the rate: the "
             "mass rises only if the capital grows faster than the rate falls."),
        ],
        "worked": {
            "title": "Two million workers become three",
            "intro": [
                "Take Marx's illustration, in millions of pounds. You want the rate and the mass of "
                "profit before and after.",
            ],
            "lines": [
                "before:  4c + 2v + 2s",
                "p′ = 2 / 6 = 1/3",
                "after:  15c + 3v + 3s",
                "p′ = 3 / 18 = 1/6",
                "mass of profit:  2 to 3 million",
            ],
            "after": [
                "The capital has trebled, from 6 to 18 million, while the rate has halved, so the mass "
                "of profit rises by half. Had the capital only doubled, the mass would have stayed at "
                "2 million.",
            ],
        },
        "quiz_title": "The law as such",
        "quiz": [
            {"q": "At a rate of surplus value of 100%, what is the rate of profit of 300c + 100v?",
             "a": ["33 1/3%",
                   "25%",
                   "100%",
                   "20%"],
             "c": 1,
             "why": "Surplus value is 100 on a capital of 400. A third is the rate of 200c + 100v; "
                    "100% is s′; 20% belongs to 400c + 100v."},
            {"q": "A capital's rate of profit falls from 40% to 20%. By what factor must the capital "
                  "grow to make the same mass of profit as before?",
             "a": ["1/2",
                   "4",
                   "It cannot make the same mass",
                   "2"],
             "c": 3,
             "why": "Marx's rule: the multiplier of the capital must equal the divisor of the rate. "
                    "Half the rate on twice the capital gives the same mass. Four times would double "
                    "the mass."},
            {"q": "In the mass-rises preset, what happens between the first and the last period?",
             "a": ["The rate and the mass both halve",
                   "The rate halves and the mass is unchanged",
                   "The rate halves and the mass of profit rises by half",
                   "The rate rises and the mass falls"],
             "c": 2,
             "why": "The rate goes from 1/3 to 1/6, and surplus value from 2 million to 3 million, "
                    "because the capital trebles while the rate halves."},
            {"q": "What is the standard objection to the law as Chapter 13 states it?",
             "a": ["That rising productivity also cheapens wage goods and so raises s′, which the table holds fixed",
                   "That the composition of capital cannot rise",
                   "That the mass of profit cannot rise while the rate falls",
                   "That the table's arithmetic is wrong"],
             "c": 0,
             "why": "Robinson and Sweezy pressed exactly that: the table fixes s′ while productivity "
                    "rises. No one disputes the arithmetic, and the chapter itself shows the mass "
                    "rising as the rate falls. A rising composition is the premise both sides grant."},
        ],
        "mistakes": [
            ("Thinking a falling rate of profit means falling profits",
             "The rate is profit per hundred of capital, the mass is profit in all. In the "
             "mass-rises preset the rate tile falls to 1/6 = 16.67% while the mass tile rises to "
             "£3,000,000 from £2,000,000. Marx calls them two sides of one law: the same "
             "accumulation lowers the rate and raises the mass."),
            ("Thinking the law says profit falls because workers are exploited less",
             "In the marx preset s′ is 100% throughout, and Marx adds that the fall can come with "
             "&ldquo;the same, or even of a higher, rate of surplus-value&rdquo;. The rate of profit "
             "falls because each worker sets more capital in motion, not because he works fewer "
             "unpaid hours."),
            ("Thinking accumulation by itself lowers the rate",
             "In the steady preset the capital doubles four times and the rate stays at 1/5. Only a "
             "change in composition lowers the rate at a given s′."),
        ],
        "standard": (
            "Finish when you can compute the rate and the mass of profit through a rising composition.",
            "Given a capital's c and v in successive periods and a fixed rate of surplus value, "
            "compute each period's rate and mass of profit, and state how fast the capital must "
            "grow for the mass to stay the same or rise."
        ),
        "note": (
            "The lab holds s′ fixed, which is the step the standard objection disputes; the next "
            "lesson lets it move. It also measures the composition in value and takes the rise in "
            "c as given, so it cannot say whether a rising composition is how productivity actually "
            "grows, or whether the rate of profit has fallen in any economy. Marx's table and his "
            "two-million illustration are his figures; steady is illustrative."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 3, l. 2284 (why the fall is not more rapid: the opening
    # passage). Inline: l. 2288, 2312, 2316, 2324, 2330, 2353 (the six
    # headings), l. 2306 (more of a tendency), l. 2320 (mass grows while its
    # value stays the same), l. 2344 (not suspended, but weakened), l. 2351
    # (more productive, not less). Chapter 15, l. 2408 (two laborers against
    # 24) and l. 2553 (no capitalist voluntarily introduces) for Marx's
    # limit and Okishio's premise.
    {
        "slug": "counteracting-influences",
        "title": "Counteracting Influences",
        "module": "Chapter 14 · Counteracting Causes",
        "one_line": "The same development that raises the composition of capital also raises the rate of exploitation and cheapens the means of production, which slows the fall of the rate of profit and makes the law a tendency.",
        "summary": (
            "Chapter 14 asks why the rate of profit does not fall faster and lists six influences "
            "that check it. Apply the two that act on the rate directly, a rising rate of surplus "
            "value and cheaper means of production, to the law's sequence and compute how much of "
            "the fall each offsets. Then read the strongest modern objection, Okishio's theorem, "
            "which says the offset can be complete."
        ),
        "key": [
            "first check: raise s′ (a longer, harder day)",
            "third check: cheapen the elements of c",
            "offset = actual p′ − p′ without them",
            "s′ 100% → 150%, c/v 3 → 5: p′ holds 25%",
            "so the law is a tendency, not a fact",
        ],
        "key_label": "The counteracting causes",
        "concepts_intro": (
            "The chapter is a list. The lab computes two of its items, and the other four are "
            "taken in prose."
        ),
        "concepts": [
            ("A tendency",
             "A law whose effect is checked, delayed or weakened by influences that come from the "
             "same causes. Marx says the counteracting causes do not suspend the law; they explain "
             "why its effect shows only over long periods."),
            ("Raising the rate of surplus value",
             "Longer days and harder work raise s′ without adding much constant capital, and so "
             "raise the rate of profit on the same composition. Marx says the fall is checked above "
             "all by lengthening the working day."),
            ("Cheapening the elements of constant capital",
             "The productivity that multiplies the mass of means of production also cheapens them, "
             "so their value grows more slowly than their mass, and may not grow at all."),
        ],
        "read_title": "The passage first, then the list",
        "read_intro": (
            "Marx turns the problem round in the chapter's first paragraph. The six headings follow."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 14.</strong> &ldquo;How is it that this fall is not "
                  "greater and more rapid? There must be some counteracting influences at work, "
                  "which thwart and annul the effects of this general law, leaving to it merely the "
                  "character of a tendency. For this reason we have referred to the fall of the "
                  "average rate of profit as a tendency to fall.&rdquo;"),
            ("p", "Marx turns the question round. Looking at the mass of machinery industry had added in "
                  "thirty years, he says the puzzle is no longer why the rate falls but why it falls "
                  "so slowly. His answer is a list, and the Kerr headings are worth reading in order: "
                  "&ldquo;Raising the Intensity of Exploitation&rdquo;, &ldquo;Depression of Wages "
                  "Below their Value&rdquo;, &ldquo;Cheapening of the Elements of Constant "
                  "Capital&rdquo;, &ldquo;Relative Overpopulation&rdquo;, &ldquo;Foreign "
                  "Trade&rdquo; and &ldquo;The Increase of Stock Capital&rdquo;."),
            ("p", "The first is the one the lab computes. A longer or more intense working day raises "
                  "s′, and the lengthening in particular raises it without adding constant capital. "
                  "In the <strong>rising-s</strong> preset the capital starts at 300c + 100v at 100%, "
                  "c rises by 50 a period and s′ by an eighth: after four periods it is 500c + 100v at "
                  "150%, and the rate is still 25%. Without the rise in s′ it would be 1/6. The offset "
                  "tile reads 25/3 of 25/3 points: all of the fall is offset."),
            ("p", "Marx is careful about what this proves. A rise in the rate of surplus value "
                  "&ldquo;does not suspend the general law. But it causes that law to become more of "
                  "a tendency, that is, a law whose absolute enforcement is checked, retarded, "
                  "weakened, by counteracting influences.&rdquo; And he adds the limit in the next "
                  "chapter: &ldquo;Two laborers, each working 12 hours daily, cannot produce the same "
                  "mass of surplus-value as 24 laborers each working only 2 hours, even if they could "
                  "live on air&rdquo;. A rise in s′ can check the fall, he says, but cannot prevent it "
                  "entirely, because the surplus labour of fewer workers per pound of capital is "
                  "bounded by their working day."),
            ("p", "The second heading, wages pushed below the value of labour-power, Marx mentions "
                  "only empirically, as belonging to a study of competition, and calls it one of the "
                  "most important checks. The third is the lab's second case. The same productivity "
                  "that multiplies the cotton a spinner works up cheapens the cotton, and &ldquo;In "
                  "exceptional cases the mass of the elements of constant capital may even increase, "
                  "while its value remains the same or even falls.&rdquo; In <strong>cheap-c</strong> "
                  "c's value rises by 25 a period instead of 50, because its elements cheapen: it "
                  "ends at 400c + 100v and a rate of 1/5. The offset tile reads 10/3 of 25/3 points, "
                  "two-fifths of the fall."),
            ("def", ("Offset",
                     "The rate of profit with the counteracting influences minus the rate the same "
                     "sequence would reach without them, in percentage points, set beside the fall "
                     "that would otherwise have happened.")),
            ("p", "In <strong>combined</strong> both act at half strength: s′ rises by a sixteenth a "
                  "period, to 125%, and c cheapens as in cheap-c. Neither alone holds the rate, and "
                  "together they hold it at 25%, the offset tile reading 25/3 of 25/3 points again. "
                  "The other three causes are mechanisms the lab does not separate. Relative "
                  "overpopulation keeps labour cheap enough that old labour-intensive trades survive "
                  "and new ones, luxuries above all, start with a low composition, and they enter the "
                  "average. Foreign trade cheapens both necessities and materials. Stock capital, "
                  "railways for example, takes only interest or dividends and stays out of the "
                  "averaging, which keeps the measured rate higher than it would be."),
            ("p", "Several of them, Marx stresses, cut both ways. Foreign trade cheapens "
                  "inputs and also speeds accumulation and the rise in composition. Cheapening c "
                  "depreciates existing capital. &ldquo;This law is not suspended, but its effect is "
                  "weakened.&rdquo; And near the chapter's end comes a sentence that sums up Part III: "
                  "&ldquo;The rate of profit does not fall, because labor becomes less productive, "
                  "but because it becomes more productive.&rdquo;"),
            ("p", "Here the strongest modern objection belongs, and it should be heard in full. In "
                  "1961 the Japanese economist Nobuo Okishio proved a theorem about exactly the "
                  "change this chapter describes. Suppose capitalists adopt a new technique only if "
                  "it lowers their costs at current prices, and the real wage stays the same. Then, "
                  "once prices and the general rate settle again, the rate of profit cannot fall, "
                  "and it rises if the change touches goods that enter, directly or indirectly, into "
                  "every other. On those assumptions the counteracting influences always win: a "
                  "rising composition chosen by cost-cutting capitalists comes with enough "
                  "cheapening to more than offset it. If the rate falls, Okishio concluded, it is "
                  "because real wages rose, not because of the technique."),
            ("p", "There are replies, and the chapter bears on one of them. Marx's premise is close to Okishio's: in Chapter "
                  "15 he says no capitalist adopts a method that lowers the rate of profit, and that "
                  "the fall comes later, when competition generalises the method. Anwar Shaikh "
                  "argued that with fixed capital, competition pushes firms to cut unit costs even "
                  "at a lower rate of profit on their larger capital. Andrew Kliman, Alan Freeman and "
                  "others of the temporal single-system school argued that Okishio's result depends "
                  "on valuing inputs and outputs at the same prices, and does not hold when they "
                  "are valued in time. Others accept the theorem and look for the rate's movements "
                  "in wages and demand instead. The lab computes what a given offset does to a given "
                  "sequence. It cannot say which sequence an economy follows."),
            ("p", "If the law works only as a tendency, how does it show itself? The next lesson, “The "
                  "Internal Contradictions of the Law”, follows Marx from the falling rate to "
                  "over-accumulation and crisis."),
        ],
        "lab": ("capkit", {
            "mode": "tendency",
            "view": "counter",
            "money_unit": "£",
            "periods": 4,
            "preset": "rising-s",
            "presets": [
                {"id": "rising-s", "label": "300c + 100v at 100%; c up 50 and s′ up 1/8 each period",
                 "c": 300, "v": 100, "s_rate": 1, "c_step": [50], "capital_growth": [],
                 "s_rate_step": ["1/8"], "c_cheapening": [], "expect": {"teRate": "1/4 = 25%", "teMass": "£150", "teOffset": "25/3 of 25/3 points"}},
                {"id": "cheap-c", "label": "The same capital; its elements cheapen enough to halve each rise in c",
                 "c": 300, "v": 100, "s_rate": 1, "c_step": [50], "capital_growth": [],
                 "s_rate_step": [], "c_cheapening": ["1/14", "1/15", "1/16", "1/17"], "expect": {"teRate": "1/5 = 20%", "teMass": "£100", "teOffset": "10/3 of 25/3 points"}},
                {"id": "combined", "label": "Both: s′ up 1/16 a period and the same cheapening",
                 "c": 300, "v": 100, "s_rate": 1, "c_step": [50], "capital_growth": [],
                 "s_rate_step": ["1/16"], "c_cheapening": ["1/14", "1/15", "1/16", "1/17"], "expect": {"teRate": "1/4 = 25%", "teMass": "£125", "teOffset": "25/3 of 25/3 points"}},
            ],
            "panel_title": "The fall, and what offsets it",
            "panel_intro": (
                "Each period c rises by the step, then cheapens by the share given, and s′ rises by "
                "its step. The lab runs the same sequence again without the rise in s′ and the "
                "cheapening, and the offset tile compares the two. Every preset rises from c/v = 3 "
                "toward c/v = 5 in mass."
            ),
        }),
        "steps_title": "Measuring an offset",
        "steps_intro": "Four steps for any sequence and any counteracting influence.",
        "steps": [
            ("Run the law alone",
             "Raise c period by period at a fixed s′ and compute the last period's rate. The fall "
             "is the first rate minus that one."),
            ("Apply the influences",
             "Run the same sequence with s′ rising or c cheapening, and compute the last period's "
             "rate again."),
            ("Compute the offset",
             "Subtract the rate without the influences from the rate with them, in percentage "
             "points."),
            ("Compare with the fall",
             "An offset equal to the fall holds the rate; a smaller one slows the fall; a larger "
             "one reverses it."),
        ],
        "worked": {
            "title": "A rising rate of surplus value holds the rate",
            "intro": [
                "Take the rising-s preset's end point. You want the rate with and without the rise "
                "in s′, and the offset.",
            ],
            "lines": [
                "start:  100 / (300 + 100) = 1/4",
                "s′ still 100%:  100 / (500 + 100) = 1/6",
                "s′ at 150%:  150 / (500 + 100) = 1/4",
                "fall offset:  25/3 of 25/3 points",
            ],
            "after": [
                "The composition has risen from 3 to 5 and the rate has not moved. Whether the checks "
                "can hold the rate without limit is the question Marx answers no, in Chapter 15, and "
                "Okishio's theorem, on its own assumptions, answers differently.",
            ],
        },
        "quiz_title": "Counteracting influences",
        "quiz": [
            {"q": "A capital of 400c + 100v at 100% becomes 600c + 100v. What rate of surplus value "
                  "would hold its rate of profit at 20%?",
             "a": ["100%",
                   "120%",
                   "140%",
                   "200%"],
             "c": 2,
             "why": "A rate of 20% on 700 needs 140 of surplus value, which on v = 100 is 140%. At "
                    "100% the rate falls to 1/7; 120% gives 120/700; 200% gives 2/7."},
            {"q": "In the cheap-c preset, how much of the fall does the cheapening offset?",
             "a": ["All of it",
                   "10/3 of 25/3 points",
                   "None of it",
                   "25/3 of 10/3 points"],
             "c": 1,
             "why": "Without cheapening the rate falls from 1/4 to 1/6, 25/3 points. With it, c ends "
                    "at 400 and the rate at 1/5, which is 10/3 points above 1/6. Reading it as 25/3 of 10/3 "
                    "points reverses offset and fall."},
            {"q": "What does Marx say the counteracting influences do to the law?",
             "a": ["They refute it",
                   "They are exceptions that leave its effect untouched",
                   "They reverse it in the long run",
                   "They do not suspend it but weaken its effect, so it acts as a tendency"],
             "c": 3,
             "why": "&ldquo;This law is not suspended, but its effect is weakened.&rdquo; Marx "
                    "rejects both readings in the other options: the influences are neither a "
                    "refutation nor irrelevant exceptions."},
            {"q": "What does Okishio's theorem assume about technical change?",
             "a": ["That capitalists adopt a technique only if it lowers costs at current prices, with the real wage constant",
                   "That the rate of surplus value is constant",
                   "That the composition of capital never rises",
                   "That capitalists adopt every technique that raises productivity"],
             "c": 0,
             "why": "Cost-reducing choice at a constant real wage is the theorem's premise. It allows "
                    "s′ and the composition to change, and it excludes techniques that do not cut "
                    "costs, which Marx also says capitalists refuse."},
        ],
        "mistakes": [
            ("Treating the counteracting influences as either a refutation or mere exceptions",
             "Marx's claim is narrower: they make the fall a tendency. In rising-s the offset tile "
             "reads 25/3 of 25/3 points, so for those four periods the rate does not fall at all, "
             "and in cheap-c it reads 10/3 of 25/3, so it falls more slowly. Neither shows what "
             "happens over a longer run. Marx argues that a rising s′ cannot offset a rising c/v "
             "without limit; Okishio (1961) argued that under cost-cutting choice it need never "
             "fall; this course does not settle it."),
            ("Thinking the influences are separate from the causes of the fall",
             "Marx's point is that they come from the same development. The productivity that raises "
             "c/v also raises s′ and cheapens c; foreign trade cheapens inputs and speeds "
             "accumulation. In the combined preset both offsets are products of the change that "
             "raises c."),
            ("Reading a higher rate of exploitation as a lower rate of profit",
             "The rising-s preset raises s′ to 150% and the rate of profit stays at 25% instead of "
             "falling to 1/6. Exploitation rising and profit rate falling can go together, as in the "
             "previous lesson, but a rise in s′ by itself raises the rate."),
        ],
        "standard": (
            "Finish when you can apply a counteracting influence to the law's sequence and measure its offset.",
            "Given a sequence of capitals at a fixed s′ and a rise in s′ or a cheapening of c, "
            "compute the last period's rate with and without the influence, the fall that would "
            "have occurred, and the part of it offset."
        ),
        "note": (
            "The lab offsets a fall over the periods it is given and says nothing about the long "
            "run, which is where Marx and his critics disagree; nor does it model wages below value, "
            "overpopulation, foreign trade or stock capital. Okishio's theorem works in a "
            "general-equilibrium model this lab does not have. The figures are illustrative; Marx "
            "gives the causes without numbers."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 3, l. 2437 (the real barrier: the opening passage); l. 2453
    # (1,000 yielding 100 grows to 1,500). Inline: l. 2425 (crises as
    # momentary and forcible solutions), l. 2445 (over-accumulation),
    # l. 2449 (absolute overproduction), l. 2461 (hostile brothers), l. 2465
    # (equilibrium restored), l. 2489 (economists who deny overproduction of
    # commodities), l. 2501 (not too much wealth), l. 2553 (no capitalist
    # voluntarily introduces).
    {
        "slug": "internal-contradictions-of-the-law",
        "title": "The Internal Contradictions of the Law",
        "module": "Chapter 15 · Unraveling the Internal Contradictions of the Law",
        "one_line": "When added capital yields no added profit, capital is over-accumulated, and on Marx's account the rate is restored only when part of the capital is idled or destroyed in a crisis.",
        "summary": (
            "Chapter 15 follows the falling rate into crisis. Marx separates producing surplus value "
            "from realising it, defines an absolute over-accumulation of capital, and argues that "
            "the rate is restored by the devaluation and destruction of capital. Compute the rate "
            "when added capital yields no added profit, and the rate after part of the swollen "
            "capital is written off."
        ),
        "key": [
            "absolute over-accumulation: ΔC adds no s",
            "Marx: 1,000 earns 100; 1,500 earns 100",
            "p′ from 10% to 6 2/3%",
            "devalue a third: 1,000 again, 10%",
            "barrier: capital itself",
        ],
        "key_label": "Chapter 15 in five lines",
        "concepts_intro": (
            "Chapter 15 has four sections and ranges widely. The lesson follows three ideas through "
            "it."
        ),
        "concepts": [
            ("Production and realisation",
             "Exploitation is limited by the productive power of society; selling what it produces "
             "is limited by the proportions between trades and by consumption under the given "
             "distribution of income. The two sets of conditions are separate, and can come apart."),
            ("Over-accumulation of capital",
             "Capital is over-accumulated, absolutely, when added capital produces no more surplus "
             "value than the capital before it, or less. Then the same profit is reckoned on more "
             "capital, and the rate falls sharply."),
            ("Devaluation",
             "The rate is restored, on Marx's account, by idling or destroying part of the capital: "
             "plant stands still, stocks are sold off cheap, and claims on future profit lose value. "
             "The same mass of profit then stands against a smaller capital."),
        ],
        "read_title": "The passage first, then Marx's over-accumulation",
        "read_intro": (
            "The passage is the chapter's best-known sentence and what follows it. The arithmetic "
            "comes from the next section."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 15, §2.</strong> &ldquo;The real barrier of "
                  "capitalist production is capital itself. It is the fact that capital and its "
                  "self-expansion appear as the starting and closing point, as the motive and aim of "
                  "production; that production is merely production for capital, and not vice versa, "
                  "the means of production mere means for an ever expanding system of the life "
                  "process for the benefit of the society of producers.&rdquo;"),
            ("p", "The first section draws a line you can see in any recession. Producing surplus "
                  "value is the first act; selling the goods that contain it is the second. A firm "
                  "can exploit its workers fully and still fail to realise the profit, if the goods "
                  "do not sell or sell below their prices of production. The first act is limited by "
                  "productive power, the second by the proportions between trades and by "
                  "consumption, and consumption is held down by the very distribution that makes "
                  "the profit. Marx says the fall in the rate &ldquo;promotes overproduction, "
                  "speculation, crises, surplus-capital along with surplus-population&rdquo;."),
            ("p", "Read the passage line by line. Marx says that &ldquo;capital and its self-expansion&rdquo; "
                  "are the starting and closing point: production is undertaken when it promises profit "
                  "at the going rate, and halted when it does not, whatever the need for the goods. "
                  "The means, an unlimited growth of productive power, comes into conflict with the "
                  "limited end, the growth of the existing capital's value. Marx is not saying that "
                  "too much is produced for people's wants. He says the opposite later in the "
                  "chapter: &ldquo;It is not a fact that too much wealth is produced.&rdquo; What is "
                  "produced in excess is wealth in the form of capital, means of production that "
                  "cannot be employed at a sufficient rate of profit."),
            ("p", "Section 3 makes this precise with a thought experiment. Suppose capital has grown "
                  "so far relative to the working population that neither the working day nor the "
                  "rate of exploitation can be raised further. Then the increased capital, C plus ΔC in Marx's notation (the Kerr text garbles "
                  "the symbol), would produce no more profit than C did. That is absolute over-accumulation. His figures:"),
            ("p", "<strong>Volume III, Chapter 15, §3.</strong> &ldquo;If a total capital of 1,000 "
                  "yielded a profit of 100, and after its increase to 1,500 still yielded 100, then "
                  "1,000 in the second case would yield only 66 2/3.&rdquo;"),
            ("def", ("Absolute over-accumulation of capital",
                     "A state in which additional capital produces no additional surplus value, or "
                     "less, than the capital before it, so that the rate of profit on the whole "
                     "falls in proportion to the growth of capital or faster.")),
            ("p", "The <strong>marx</strong> preset sets the capital at 900c + 100v at 100%, which "
                  "yields Marx's 100 on 1,000 (the split is the lab's, since Marx gives only the "
                  "total), and adds 500 that sets no more labour to work. The rate tile reads 1/15, "
                  "6.67%, and the mass tile £100: the rate has fallen from 10% to 6 2/3% with no fall "
                  "in exploitation at all. A milder case, <strong>mild</strong>, adds 100 and the rate "
                  "falls to 1/11."),
            ("p", "How is it resolved? Not peacefully. While profits grow, competition is &ldquo;a "
                  "practical brotherhood of the capitalist class&rdquo;; when losses have to be "
                  "shared, it becomes &ldquo;a fight of hostile brothers&rdquo;, each trying to push "
                  "the idle capital onto someone else. &ldquo;But under all circumstances the "
                  "equilibrium is restored by making more or less capital unproductive or destroying "
                  "it.&rdquo; Factories close, stocks are sold at a loss, fixed capital is written "
                  "down, and the chain of payments breaks. The <strong>devalue</strong> preset writes "
                  "off a third of the swollen 1,500: the same 100 of profit on 1,000 is 10% again."),
            ("p", "Crises, then, are on this account &ldquo;momentary and forcible solutions of the "
                  "existing contradictions&rdquo;, which clear the ground for the next expansion: "
                  "unemployment pushes wages down, depreciated plant raises the rate, and the cycle "
                  "starts again on a larger scale. He turns to the economists of his day "
                  "who, following Say and Ricardo, denied that a general overproduction of commodities is "
                  "possible. He notes that &ldquo;the same economists, who deny the overproduction of "
                  "commodities, admit that of capital&rdquo;, and since capital consists of "
                  "commodities, he says, the two cannot be separated."),
            ("p", "The strongest objections come from several sides. Many Marxists themselves do not "
                  "trace crises to the falling rate: underconsumption theories, from Rosa Luxemburg to "
                  "Paul Baran and Paul Sweezy, put the weight on the realisation problem of the first "
                  "section instead. Okishio's theorem, from the previous lesson, denies that technical "
                  "change by itself lowers the rate. Keynes, writing in 1936 with no reference to "
                  "Marx's law, located slumps in a shortfall of investment demand, which the right "
                  "policy could correct. And Marx's own figures are a model: the lab holds the mass "
                  "of profit fixed as the capital grows, where Marx's text has wages rising until it "
                  "does. Whether the rate of profit has fallen in fact, and whether its movements "
                  "explain crises, are argued with data this course does not carry."),
            ("p", "Near the chapter's end Marx strikes a different note. No capitalist adopts a new method that "
                  "lowers his rate of profit; he adopts the cheaper one, sells above its price of "
                  "production while it is new, and competition then generalises it. &ldquo;Then "
                  "follows a fall in the rate of profit&rdquo;, &ldquo;wholly independent of the will "
                  "of the capitalist&rdquo;. That is the law as Marx leaves it: the result of no "
                  "capitalist's choice, and shown in the rate only over long periods."),
            ("p", "Part III ends here, and Volume III turns to the people who share the surplus value "
                  "without producing it. The next course, Merchant's Capital and Interest, begins "
                  "with the merchant, who takes part in the general rate of profit without making any "
                  "of the goods he sells."),
        ],
        "lab": ("capkit", {
            "mode": "tendency",
            "view": "overaccumulation",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 1,000 yielding 100 grows to 1,500 and still yields 100",
                 "c": 900, "v": 100, "s_rate": 1, "added_capital": 500, "devalued_share": 0, "expect": {"teRate": "1/15 = 6.67%", "teMass": "£100"}},
                {"id": "devalue", "label": "The same, then a third of the swollen capital destroyed",
                 "c": 900, "v": 100, "s_rate": 1, "added_capital": 500, "devalued_share": "1/3", "expect": {"teRate": "1/10 = 10%", "teMass": "£100"}},
                {"id": "mild", "label": "1,000 yielding 100 grows to 1,100 and still yields 100",
                 "c": 900, "v": 100, "s_rate": 1, "added_capital": 100, "devalued_share": 0, "expect": {"teRate": "1/11 = 9.09%", "teMass": "£100"}},
            ],
            "panel_title": "Over-accumulation and devaluation",
            "panel_intro": (
                "A capital is typed as c, v and s′; the added capital sets no more labour in motion, "
                "so the mass of surplus value stays where it was. A devalued share then removes part "
                "of the swollen capital. The table shows the rate at each step; the tiles show the "
                "last."
            ),
        }),
        "steps_title": "Following an over-accumulation",
        "steps_intro": "Four steps, as Marx's thought experiment runs.",
        "steps": [
            ("Find the mass of profit",
             "Compute s = s′ · v for the capital before it grows. Under absolute over-accumulation "
             "this mass does not rise."),
            ("Add the capital",
             "Add the new capital to c + v and divide the same mass by the larger total."),
            ("Devalue",
             "Multiply the swollen capital by one minus the share destroyed or idled, and divide "
             "the same mass by what is left."),
            ("Compare the rates",
             "The added capital lowers the rate in proportion to its size; devaluation restores the "
             "rate in proportion to what it removes."),
        ],
        "worked": {
            "title": "Marx's 1,000 and 1,500",
            "intro": [
                "A capital of 1,000 yields 100. It grows to 1,500 with no more profit, and a third is "
                "then written off. You want the rate at each step.",
            ],
            "lines": [
                "before:  100 / 1,000 = 10%",
                "after the addition:  100 / 1,500 = 1/15",
                "devalued:  1,500 · 2/3 = 1,000",
                "after devaluation:  100 / 1,000 = 10%",
            ],
            "after": [
                "Marx's way of saying the second line is that 1,000 now yields only 66 2/3, as if "
                "it were a capital of 666 2/3 under the old conditions.",
            ],
        },
        "quiz_title": "Over-accumulation",
        "quiz": [
            {"q": "A capital of 2,000 yields 200. It grows to 2,500 and still yields 200. What is "
                  "the new rate of profit?",
             "a": ["10%",
                   "8%",
                   "40%",
                   "2%"],
             "c": 1,
             "why": "`200 / 2,500 = 2/25`, 8%. Ten per cent is the old rate; 40% divides the profit "
                    "by the added 500 alone; 2% divides it by the old capital times five."},
            {"q": "In the same case, what share of the 2,500 must be devalued to restore the old rate?",
             "a": ["1/4",
                   "1/2",
                   "1/10",
                   "1/5"],
             "c": 3,
             "why": "The rate is back at 10% when the capital is 2,000 again, a fifth of 2,500 "
                    "removed. A quarter is 500 over the old 2,000, not over the swollen capital."},
            {"q": "What does Marx mean by an absolute overproduction of capital?",
             "a": ["More goods are produced than people could use",
                   "The rate of interest rises above the rate of profit",
                   "Added capital produces no more surplus value than the capital before it, or less",
                   "Capital is sent abroad"],
             "c": 2,
             "why": "That is his definition. He says expressly that too much wealth is not produced, "
                    "only too much in the form of capital; interest is not in the definition; and "
                    "capital sent abroad goes for a higher rate, not because there is none at home."},
            {"q": "On Marx's account, how is the rate of profit restored after over-accumulation?",
             "a": ["By idling or destroying part of the capital",
                   "By a rise in wages",
                   "By the state buying the surplus",
                   "It is never restored"],
             "c": 0,
             "why": "Marx: &ldquo;the equilibrium is restored by making more or less capital unproductive "
                    "or destroying it.&rdquo; A rise in wages is, in Marx's thought experiment, part "
                    "of what causes the over-accumulation, and the chapter describes the cycle "
                    "restarting."},
        ],
        "mistakes": [
            ("Thinking crises come from a shortage of capital",
             "In Marx's over-accumulation there is too much capital, not too little. In the marx "
             "preset the capital grows from 1,000 to 1,500 while the mass tile stays at £100, and "
             "the rate tile reads 1/15. Only the devalue preset, which destroys a third of the "
             "capital, brings the rate back to 10%."),
            ("Reading over-accumulation as too many goods for people's needs",
             "Marx denies this in so many words: &ldquo;It is not a fact that too much wealth is "
             "produced.&rdquo; The surplus is of means of production that cannot be employed at a "
             "sufficient rate of profit, while there are unemployed workers beside them."),
            ("Treating the crisis as the end of the system in Marx's chapter",
             "Chapter 15 describes crises as momentary solutions after which the cycle runs again "
             "on a larger scale. Whatever Marx expected in the long run, the mechanism he computes "
             "here restores the rate."),
        ],
        "standard": (
            "Finish when you can compute the rate under over-accumulation and after a devaluation.",
            "Given a capital's c, v and s′, an added capital that yields no added surplus value, and "
            "a share devalued, compute the rate of profit before and after the addition and after "
            "the devaluation, and state the share that restores the old rate."
        ),
        "note": (
            "The lab holds the mass of profit fixed as capital is added, which is the second of "
            "Marx's two alternatives, &ldquo;the mass of profits remaining the same&rdquo;; in his "
            "thought experiment the added capital makes no more profit because wages rise once the "
            "working population is fully employed, which the lab does not model; and it says nothing about "
            "whether real crises have this cause. The 1,000 and 1,500 are Marx's; the split into c "
            "and v, the third devalued and the mild case are illustrative."
        ),
    },
]
