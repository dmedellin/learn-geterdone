"""Cost Price and the Rate of Profit, lessons 1-4 -- Volume III, Chapters 1-4, one lesson per chapter.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, and the translator's double quotation marks inside a quotation
are printed as single curly quotes. Formulas inside a quotation are printed as
the Kerr text prints them, with an apostrophe for the prime (p' = s/C); the
lessons' own prose writes p′ and s′. Nothing else is changed.

Chapter 4 is Engels' text, not Marx's: his preface says Marx left only its
title. The lesson on it says so in its first paragraph after the passage.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 3, l. 456 (the formula C = c + v + s); l. 539-541 (a profit
    # below value). Inline: l. 462 (two vastly different amounts), l. 466
    # (capitalist cost and actual cost), l. 470 (the false role), l. 502 (the
    # distinction has disappeared), l. 533 (an offspring of the total capital),
    # l. 541 (practical playroom), l. 549 (Torrens), l. 551 (something cannot
    # come out of nothing), l. 553 (phlogiston), l. 557 (Proudhon).
    {
        "slug": "cost-price-and-profit",
        "title": "Cost Price and Profit",
        "module": "Chapter 1 · Cost Price and Profit",
        "one_line": "What a commodity costs its owner is less than what it is worth, and the difference, surplus value, appears to him as a profit on everything he laid out.",
        "summary": (
            "Volume III opens by looking at Volume I's commodity from the owner's side. Of a "
            "value of c + v + s, only c + v cost the capitalist anything: that is the cost "
            "price, and the surplus over it looks like the offspring of the whole capital. "
            "Compute the cost price and the profit on Marx's commodity of £600, and sell it "
            "below its value to see that a profit can still be made."
        ),
        "key": [
            "value of a commodity = c + v + s",
            "cost price k = c + v",
            "value = k + s; on the surface, k + p",
            "profit on a sale = price − k",
            "a sale above k may still be below value",
        ],
        "key_label": "The first chapter in five lines",
        "concepts_intro": (
            "Chapter 1 adds no new quantity to Volume I. It regroups the old ones the way the "
            "owner of the business groups them, and three things follow from the regrouping."
        ),
        "concepts": [
            ("Cost price",
             "The part of a commodity's value that replaces what the capitalist spent on it: "
             "the means of production used up and the wages, `k = c + v`. It is less than the "
             "value by exactly the surplus value, which cost him nothing."),
            ("Capitalist cost and actual cost",
             "The capitalist measures cost by the capital he spent; Marx measures it by the "
             "labour spent. The two differ by the unpaid labour, and in cost price the "
             "difference between constant and variable capital disappears from view."),
            ("Profit",
             "Surplus value seen as the increase of the whole capital advanced rather than of "
             "the variable part alone. In this Part it is the same amount as the surplus "
             "value; only its form, and the way it is measured, differ."),
        ],
        "read_title": "The formula first, then the owner's view of it",
        "read_intro": (
            "The chapter states Volume I's formula in its first lines and then subtracts from "
            "it. Its sharpest claim comes near the end, about selling below value."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 1.</strong> &ldquo;The value of every commodity "
                  "produced by capitalist methods is represented by the formula: C = c + v + s. "
                  "If we subtract the surplus-value s from this value of the product, there "
                  "remains only an equivalent for the value of the capital c + v expended for the "
                  "elements used in the production of this commodity.&rdquo;"),
            ("p", "Think about how a price is usually explained to you: the maker's costs, plus "
                  "a margin on top. That is the view this chapter starts from and takes apart. "
                  "Volume I went inside production and Volume II followed capital through "
                  "circulation; Volume III, Marx says in his opening paragraph, moves step by step "
                  "towards the forms capital takes &ldquo;on the surface of society&rdquo;, where "
                  "it meets other capitals and the ordinary consciousness of the people in it. In "
                  "this chapter's formula C is the value of the commodity; from the next chapter "
                  "on the same letter means the capital."),
            ("p", "Marx's figures: a capital of £500, of which £20 is wear of the instruments, "
                  "£380 is materials and £100 buys labour-power, with a rate of surplus value of "
                  "100%. The product is `400c + 100v + 100s`, worth £600. Take away the £100 of "
                  "surplus value and £500 is left, which only replaces what was spent. That £500 "
                  "is the cost price, written k. And here the chapter makes its first distinction: "
                  "the cost to the capitalist and the actual cost are &ldquo;two vastly different "
                  "amounts&rdquo;. &ldquo;The capitalist cost of the commodity is measured by the "
                  "expenditure of capital, while the actual cost of the commodity is measured by "
                  "the expenditure of labor.&rdquo; The surplus value costs the capitalist nothing "
                  "because it costs the labourer unpaid labour."),
            ("p", "Cost price is not just a heading in the books. It has to buy back the means "
                  "of production and labour-power for the next round, so it acts on production "
                  "every day. But it says nothing about how value is formed, and Marx warns that "
                  "it will play &ldquo;the false role of a category in the actual production of "
                  "values&rdquo;. He shows why by changing its two parts in turn. Raise the price "
                  "of the means of production from £400 to £600 and both the cost price and the "
                  "value rise by £200, to £700 and £800, because constant capital passes its own "
                  "value into the product. Raise the wages from £100 to £150 and the cost price "
                  "rises to £550, but the value stays at £600: `400c + 150v + 50s`. Wages do not "
                  "pass into the product; the labour adds new value, and a dearer wage only "
                  "changes how that new value is split. In the cost price this difference is "
                  "invisible. &ldquo;The distinction between constant and variable capital has "
                  "disappeared.&rdquo;"),
            ("p", "Then the fixed capital. Suppose the instruments were worth £1,200 before "
                  "production began. Only the £20 of wear enters the cost price, so the capital "
                  "advanced is £1,680 while the cost price is £500. After the sale the capitalist "
                  "has £1,180 of machinery left and £600 of product, £1,780 in all: £100 more than "
                  "the £1,680 he started with. Seen this way the £100 is as much an increase of "
                  "the whole £1,680 as of the £500 consumed. &ldquo;In its alleged capacity of an "
                  "offspring of the advanced total capital, the surplus-value assumes the change of "
                  "form known as profit.&rdquo; Written with p for profit, the value of the "
                  "commodity is `k + p`. The word &ldquo;alleged&rdquo; is doing work: on Marx's "
                  "account only v produces the £100, and the profit form hides that."),
            ("p", "<strong>Volume III, Chapter 1.</strong> &ldquo;Hence, if a commodity is sold "
                  "at its value, a profit is realized, which is equal to the excess of its value "
                  "over its cost-price, or equal to the entire surplus-value incorporated in the "
                  "value of the commodity. But the capitalist may sell a commodity at a profit even "
                  "when selling it below its value.&rdquo;"),
            ("p", "Marx lists the sales himself: at £510, 520, 530, 560 or 590 the commodity is "
                  "sold £90 to £10 below its value and still yields a profit of £10 to £90. The "
                  "lab does the same subtraction. The marx preset sells at the value: cost price "
                  "£500, profit £100. The cheap-sale preset sells at £560: profit £60, and the "
                  "banner says the sale is £40 below value. The proudhon preset sells at the cost "
                  "price, £500: profit £0. The below-cost preset sells at £480: profit −£20, the "
                  "case Marx allows when &ldquo;peculiar market combinations&rdquo; push a price "
                  "under cost, and which, if it continues, eats the capital. Between cost price "
                  "and value there is &ldquo;practical playroom&rdquo;, and Marx says competition "
                  "and underselling live in it. The general rate of profit, which comes in Average "
                  "Profit and Its Fall, rests on that gap too."),
            ("p", "Because cost price is what the capitalist himself paid, it is easy to take it "
                  "for the commodity's real value, and then the profit seems to come from selling "
                  "above value. Robert Torrens, a Royal Marines officer turned economist who wrote "
                  "in Ricardo's circle, made the argument carefully. A farmer advances 100 "
                  "quarters of corn and gets 120 back, and &ldquo;it would be absurd to call this "
                  "surplus, or profit, a part of his expenditure&rdquo;. So profit cannot be part "
                  "of the cost of production, and must come from the buyers, who &ldquo;by a "
                  "direct or circuitous exchange yield a certain larger portion of all ingredients "
                  "of capital than it cost to produce them&rdquo;. Marx grants the first step: an "
                  "excess over a magnitude cannot be part of it. His answer is that, if nothing "
                  "but the capitalist's advance enters the value, &ldquo;something cannot come out "
                  "of nothing&rdquo;, and Torrens has only moved the creation out of production "
                  "into exchange. Marx then lets George Ramsay give the reply from the other side: "
                  "profit cannot come out of exchange unless it existed before it, because "
                  "exchange does not change the sum of the values exchanged."),
            ("p", "Marx keeps his driest line for Proudhon, who presented the idea that "
                  "commodities sold at cost price are sold at their value &ldquo;with his customary "
                  "charlatanry in the guise of science&rdquo;. His reply is an example. Twenty "
                  "pounds of yarn worth 30s contain 24s of means of production, 3s of wages and 3s "
                  "of surplus value, so the surplus value is 2 lb of the yarn. Sell at the cost "
                  "price of 27s and the buyer gets 2 lb for nothing; the spinner has done the same "
                  "surplus labour, for the buyer instead of his employer."),
            ("p", "A modern reader will have an objection ready. Alfred Marshall, whose "
                  "<em>Principles of Economics</em> appeared in 1890, counted normal profits, the "
                  "interest on the capital and the earnings of management, among the expenses of "
                  "production: the supply price of a commodity has to cover them, or the capital "
                  "and the management go elsewhere. On that definition a sale at cost already "
                  "includes a profit, and Marx's k, which leaves it out, is a cost with a piece "
                  "missing. Marx died before Marshall wrote. What in the chapter bears on the "
                  "point is its definition of k as what the capitalist spent, chosen so that the "
                  "surplus over it can be asked about; whether the return on capital is a cost of "
                  "production or an unpaid surplus is the question the whole book argues, and this "
                  "Subject leaves it open."),
            ("p", "Cost price and profit are amounts. The next lesson, “The Rate of Profit”, "
                  "turns the profit into a ratio, and asks what it is measured against."),
        ],
        "lab": ("capkit", {
            "mode": "profit",
            "view": "cost",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 400c + 100v + 100s = £600, sold at its value",
                 "c": 400, "v": 100, "s": 100, "sale_price": "", "expect": {"prCost": "£500", "prProfit": "£100"}},
                {"id": "cheap-sale", "label": "Marx's figures, sold at £560",
                 "c": 400, "v": 100, "s": 100, "sale_price": 560, "expect": {"prCost": "£500", "prProfit": "£60"}},
                {"id": "proudhon", "label": "Sold at its cost price, £500",
                 "c": 400, "v": 100, "s": 100, "sale_price": 500, "expect": {"prCost": "£500", "prProfit": "£0"}},
                {"id": "below-cost", "label": "Sold below its cost price, at £480",
                 "c": 400, "v": 100, "s": 100, "sale_price": 480, "expect": {"prCost": "£500", "prProfit": "−£20"}},
            ],
            "panel_title": "What the commodity cost its owner",
            "panel_intro": (
                "c, v and s go in, with a selling price; leave the price empty to sell at the "
                "value. The tiles give the cost price and the profit, and the banner says how "
                "far the sale is above or below value. Compare cheap-sale with marx: the profit "
                "falls, and stays positive, while the sale is below value."
            ),
        }),
        "steps_title": "Computing cost price and profit",
        "steps_intro": "Four steps for any commodity whose value is given as c + v + s.",
        "steps": [
            ("Add c and v",
             "The cost price is the constant capital used up plus the wages: `k = c + v`. Fixed "
             "capital enters only by its wear in the period."),
            ("Add s for the value",
             "The value is `k + s`. The difference between value and cost price is the surplus "
             "value, which cost the capitalist nothing."),
            ("Subtract k from the price",
             "The profit on a sale is the selling price minus the cost price. At the value it is "
             "the whole of s."),
            ("Compare the price with the value",
             "A price between k and the value yields a profit and is still below value; a price "
             "below k yields a loss. State which case the sale is."),
        ],
        "worked": {
            "title": "Marx's £600 commodity, sold at £560",
            "intro": [
                "Take Marx's figures and sell the product for £560. You want the cost price, the "
                "profit, and how far the sale is from the value.",
            ],
            "lines": [
                "value:  400c + 100v + 100s = £600",
                "cost price:  k = 400 + 100 = £500",
                "profit:  £560 − £500 = £60",
                "below value by:  £600 − £560 = £40",
            ],
            "after": [
                "A profit of £60, and a sale £40 below value. Marx's list runs from £510 to £590 "
                "on the same commodity; every one of those sales is profitable and every one is "
                "below value.",
            ],
        },
        "quiz_title": "Cost price, value and profit",
        "quiz": [
            {"q": "A commodity's value is 300c + 150v + 150s. What is its cost price?",
             "a": ["£450", "£600", "£300", "£150"],
             "c": 0,
             "why": "Cost price is `c + v = 300 + 150 = 450`. £600 is the value, £300 is c alone, "
                    "and £150 is the surplus value, which is exactly what cost price leaves out."},
            {"q": "Marx's commodity, worth £600 with a cost price of £500, sells for £530. Which "
                  "statement is right?",
             "a": ["It is sold above its value, at a profit of £30",
                   "It is sold £70 below its value, at a profit of £30",
                   "It is sold at a loss of £70",
                   "It is sold at its value, since it covers its cost"],
             "c": 1,
             "why": "The profit is `530 − 500 = 30`, and the price is `600 − 530 = 70` below the "
                    "value. Covering cost price is not selling at value; value includes the "
                    "surplus value, and the loss of £70 is only against the value, not against "
                    "what the capitalist spent."},
            {"q": "In Marx's example the wages rise from £100 to £150, with everything else "
                  "the same. What happens to the commodity's value?",
             "a": ["It rises to £650",
                   "It stays at £600, and the surplus value falls to £50",
                   "It falls to £550",
                   "It rises to £700, like a rise in c"],
             "c": 1,
             "why": "Variable capital does not pass its value into the product; the labour adds "
                    "new value of £200 whatever the wage. A dearer wage takes more of the £200, so "
                    "the value is `400c + 150v + 50s = 600`. A rise in c would raise the value, "
                    "because constant capital does pass its value on."},
            {"q": "The instruments are worth £1,200 and wear by £20 in the period; materials "
                  "cost £380 and wages £100. What is the cost price?",
             "a": ["£1,680", "£500", "£1,580", "£480"],
             "c": 1,
             "why": "Only the wear enters the cost price: `20 + 380 + 100 = 500`. £1,680 is the "
                    "capital advanced, £1,580 counts the whole machinery but not the wages, and "
                    "£480 is the circulating capital alone, without the wear."},
        ],
        "mistakes": [
            ("Thinking a sale above cost price is a sale above value",
             "It is the capitalist's own view, and Torrens wrote it up as theory: profit is the "
             "excess of the price over the cost. The cheap-sale preset refutes it. Sold at £560, "
             "Marx's commodity yields a profit of £60 over its cost price of £500 and is still "
             "£40 below its value of £600. Any price between £500 and £600 does the same: a "
             "profit, below value."),
            ("Treating the cost price as the commodity's real value",
             "Proudhon's version of the error. The proudhon preset sells at cost price, £500, "
             "for a profit of £0, and the commodity is still worth £600. In Marx's yarn example "
             "the buyer at cost price receives the surplus labour as 2 lb of yarn for nothing."),
            ("Counting the whole capital advanced in the cost price",
             "Fixed capital enters cost price only by its wear. With machinery worth £1,200 "
             "wearing £20, the capital advanced is £1,680 and the cost price £500. The whole "
             "£1,680 does count once profit is measured as a rate, which is the next lesson."),
        ],
        "standard": (
            "Finish when you can compute cost price and profit and place a sale against the value.",
            "Given c, v and s and a selling price, compute the cost price, the value and the "
            "profit, and state whether the sale is at, above or below value and whether it is "
            "above or below cost price."
        ),
        "note": (
            "Like Volume I, this chapter assumes commodities sell at their values, and the lab "
            "prices a sale away from value only when a preset says so. The figures are Marx's. "
            "The lab subtracts; it cannot say whether the £100 is unpaid labour or a return the "
            "capital earned, which is the disagreement the lesson's closing argument names."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 3, l. 575 (the two definitions); l. 613 (profit the disguise).
    # Inline: l. 569 (lumps them together; may express different rates), l. 579
    # (deduced, not vice versa; invisible essence), l. 599 (the Ricardian
    # school), l. 613 (the same thing and numerically equal).
    {
        "slug": "the-rate-of-profit",
        "title": "The Rate of Profit",
        "module": "Chapter 2 · The Rate of Profit",
        "one_line": "The same surplus value measured against the whole capital instead of the wages is the rate of profit, and it can stay the same while exploitation doubles.",
        "summary": (
            "Chapter 2 measures one quantity two ways. Surplus value over the variable capital "
            "is the rate of surplus value; over the whole capital it is the rate of profit, the "
            "rate the capitalist sees. Compute both for three capitals of £500 that each make "
            "£100, and see one rate of profit stand for three different rates of surplus value."
        ),
        "key": [
            "s′ = s / v: measured against wages",
            "p′ = s / (c + v): against the capital",
            "same s, two standards of measurement",
            "p′ is below s′ whenever c > 0",
            "equal p′ can hide unequal s′",
        ],
        "key_label": "The second chapter in five lines",
        "concepts_intro": (
            "Chapter 2 is short and argumentative. Its arithmetic is a single division; its "
            "point is what the division shows and what it hides."
        ),
        "concepts": [
            ("Rate of surplus value",
             "Surplus value over the variable capital, `s′ = s/v`. Volume I's measure of the "
             "degree of exploitation: unpaid labour against paid."),
            ("Rate of profit",
             "The same surplus value over the whole capital advanced, `p′ = s/(c + v)`. It is "
             "the measure of how far the total capital has grown, and the only rate the "
             "capitalist calculates."),
            ("Profit as a disguise",
             "Profit and surplus value are the same amount in this Part. The rate of profit "
             "relates the surplus to every part of the capital alike, so the one part that "
             "produces it, v, cannot be seen in it."),
        ],
        "read_title": "Two definitions, then what the capitalist sees",
        "read_intro": (
            "The chapter's definitions take two sentences. The rest of it explains why the "
            "second is the one that shows on the surface."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 2.</strong> &ldquo;The rate of surplus-value "
                  "measured by the variable capital is called rate of surplus-value. The rate of "
                  "surplus-value measured by the total capital is called rate of profit.&rdquo;"),
            ("p", "If you put money in a savings account you think of the interest as a "
                  "percentage of all of it. Nobody asks which pound earned it. That is how the "
                  "capitalist reckons too, and Marx thinks he has a reason. He cannot exploit "
                  "labour without advancing machines and materials, and cannot use the machines "
                  "without hiring labour, so &ldquo;he lumps them all together in his "
                  "imagination&rdquo;, the more readily because his gain is calculated against "
                  "the total capital. Marx adds at once the sentence the lab is built on: "
                  "&ldquo;the rate of profit may remain unchanged and yet may express different "
                  "rates of surplus-value&rdquo;."),
            ("p", "Read the definition slowly. It does not introduce a new quantity. Both rates "
                  "have the same numerator, s; they differ in what s is divided by. Against v, "
                  "the wages that buy the labour which produces it, s is `s′ = s/v`. Against the "
                  "whole capital it is `p′ = s/(c + v)`. In this chapter C stops meaning the "
                  "commodity's value and starts meaning the capital, `C = c + v`. Because C is "
                  "larger than v whenever any means of production are used, p′ is always smaller "
                  "than s′."),
            ("p", "The lab divides the same surplus value both ways. Marx's capital from the "
                  "last lesson, `400c + 100v + 100s`, is the marx preset: s′ = 100% and p′ = 20%. Now keep the "
                  "capital at £500 and the surplus value at £100 and move money between c and v. "
                  "The labour-heavy preset, `300c + 200v + 100s`, gives s′ = 50%; the "
                  "capital-heavy preset, `450c + 50v + 100s`, gives s′ = 200%. The rate of profit "
                  "is 20% in all three. A worker at the capital-heavy firm does four times as "
                  "much unpaid labour, for each pound of wages, as one at the labour-heavy firm, "
                  "and the rate of profit cannot tell them apart."),
            ("p", "The machinery preset adds what the first lesson set aside. Marx's instruments "
                  "were worth £1,200, not £20, and the rate of profit is calculated on the whole "
                  "capital advanced, fixed capital included. With £1,200 of machines and £380 of "
                  "materials as c, the same £100 of surplus value on £1,680 is a rate of profit of "
                  "`5/84`, under 6%, while s′ stays at 100%. Marx notes that the difference "
                  "between fixed and circulating capital is the one difference the rate of profit "
                  "does show, because the fixed capital enters the cost price only by its wear "
                  "and the denominator in full."),
            ("p", "Then the order of explanation. &ldquo;The transformation of surplus-value "
                  "into profit must be deduced from the transformation of the rate of "
                  "surplus-value into the rate of profit, not vice versa.&rdquo; Historically, "
                  "Marx says, inquiry started from the rate of profit, because that is what is "
                  "visible; surplus value and its rate are the &ldquo;invisible and unknown "
                  "essence&rdquo;. He names the Ricardian school as the example of a mistake that "
                  "runs both ways: developing the laws of one rate directly out of the other's. The "
                  "capitalist has no reason to separate them, and the market gives him reasons "
                  "not to: whether a surplus is realised, and how much, depends on competition, "
                  "and from where he stands it looks as if it comes from selling."),
            ("p", "His own illustration of why the value of c has no inner tie to s is a "
                  "spinner. If six hours pay the wage, a twelve-hour day gives six hours of "
                  "surplus labour and uses twice the cotton of a six-hour day. What matters for "
                  "the surplus is the quantity of cotton the labour needs, not its price. Make "
                  "cotton dearer and the same surplus labour sits on a larger capital: s is "
                  "unchanged and p′ falls. That case returns in “Price Fluctuations of Raw "
                  "Materials”."),
            ("p", "<strong>Volume III, Chapter 2.</strong> &ldquo;Profit is, therefore, that "
                  "disguise of surplus-value which must be removed before the real nature of "
                  "surplus-value can be discovered.&rdquo;"),
            ("p", "Not every economist accepts that profit disguises anything. In this chapter "
                  "Marx names Ramsay, Malthus, Senior and Torrens as writers who took the "
                  "phenomena of circulation as proof that capital can be a source of surplus "
                  "value &ldquo;quite as well as labor itself&rdquo;. Nassau Senior, elsewhere, "
                  "called profit the reward of abstinence: the capitalist forgoes consuming his "
                  "wealth so that it can be used in production. Later, Eugen von Böhm-Bawerk "
                  "explained interest by time preference, the lower value people set on future "
                  "goods than on present ones, so that a return on the whole capital pays for the "
                  "time all of it is tied up. On either view a rate measured on the whole capital "
                  "is the natural measure rather than a disguise. What in the chapter bears on "
                  "them is its claim that the rate of profit, taken as the starting point, gives "
                  "&ldquo;no basis&rdquo; for any conclusion about the relation of the surplus "
                  "to the wages, while &ldquo;the profit and the surplus-value are actually the "
                  "same thing and numerically equal&rdquo; in this Part. Which starting point is "
                  "the right one is the dispute; the lab computes both rates."),
            ("p", "The rate of profit has two factors hidden in it, the rate of surplus value and "
                  "the share of v in the capital. The next lesson, “The Rate of Profit and the "
                  "Rate of Surplus Value”, changes them one at a time."),
        ],
        "lab": ("capkit", {
            "mode": "profit",
            "view": "rate",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 400c + 100v + 100s",
                 "c": 400, "v": 100, "s": 100, "expect": {"prRate": "1/5 = 20%", "prSRate": "1 = 100%"}},
                {"id": "labour-heavy", "label": "£500 with more in wages: 300c + 200v + 100s",
                 "c": 300, "v": 200, "s": 100, "expect": {"prRate": "1/5 = 20%", "prSRate": "1/2 = 50%"}},
                {"id": "capital-heavy", "label": "£500 with less in wages: 450c + 50v + 100s",
                 "c": 450, "v": 50, "s": 100, "expect": {"prRate": "1/5 = 20%", "prSRate": "2 = 200%"}},
                {"id": "machinery", "label": "Marx's figures with the £1,200 of machinery advanced",
                 "c": 1580, "v": 100, "s": 100, "expect": {"prRate": "5/84 = 5.95%", "prSRate": "1 = 100%"}},
            ],
            "panel_title": "One surplus, two rates",
            "panel_intro": (
                "c, v and s go in. The first tile divides s by the whole capital, the second by "
                "v alone. Step through the first three presets: the rate of profit does not "
                "move, and the rate of surplus value goes from 50% to 200%."
            ),
        }),
        "steps_title": "Computing the two rates",
        "steps_intro": "Four steps for any capital given as c + v with its surplus value s.",
        "steps": [
            ("Add the capital",
             "The capital advanced is `C = c + v`, with all of the fixed capital in c, not only "
             "its wear."),
            ("Divide by v",
             "The rate of surplus value is `s′ = s/v`."),
            ("Divide by C",
             "The rate of profit is `p′ = s/(c + v)`. Write both as fractions before turning "
             "them into percentages."),
            ("Compare",
             "Check that `p′ = s′·v/C` and that p′ is below s′. Two capitals with equal p′ have "
             "equal s′ only if their shares of v are equal."),
        ],
        "worked": {
            "title": "Marx's capital, two ways",
            "intro": [
                "Marx's capital of £500 makes £100 of surplus value with £100 of wages. You want "
                "both rates.",
            ],
            "lines": [
                "capital:  C = 400 + 100 = £500",
                "s′ = 100 / 100 = 1 = 100%",
                "p′ = 100 / 500 = 1/5 = 20%",
                "check:  s′ · v / C = 1 · 100 / 500 = 1/5",
            ],
            "after": [
                "Move £100 from c to v and the surplus stays £100: s′ falls to 50%, p′ stays at "
                "20%. The rate of profit records the growth of the capital, not the exploitation "
                "of the labour.",
            ],
        },
        "quiz_title": "Measured against what",
        "quiz": [
            {"q": "A capital of 600c + 200v makes £100 of surplus value. What are s′ and p′?",
             "a": ["s′ = 50%, p′ = 12.5%",
                   "s′ = 12.5%, p′ = 50%",
                   "s′ = 50%, p′ = 16.67%",
                   "s′ = 100%, p′ = 12.5%"],
             "c": 0,
             "why": "`s′ = 100/200 = 1/2` and `p′ = 100/800 = 1/8`. The second option swaps "
                    "the two denominators, the third divides by c alone, and the fourth takes s′ "
                    "as 100% without computing it."},
            {"q": "Two capitals both have a rate of profit of 20%. What can be concluded about "
                  "their rates of surplus value?",
             "a": ["They are equal",
                   "Nothing, unless their shares of v in the capital are also known",
                   "The larger capital has the higher rate of surplus value",
                   "Both are 20%"],
             "c": 1,
             "why": "`p′ = s′·v/C`, so equal p′ fits any s′ with a matching share of v. The "
                    "lab's three presets all give 20% with s′ of 50%, 100% and 200%. Size alone "
                    "does not decide it, and s′ equals p′ only if there is no constant capital."},
            {"q": "In this Part of Volume III, how does the amount of profit compare with the "
                  "amount of surplus value?",
             "a": ["Profit is smaller, because it is divided by the whole capital",
                   "They are the same amount; only the rates differ",
                   "Profit is larger, because the constant capital also yields a return",
                   "Profit is surplus value minus wages"],
             "c": 1,
             "why": "Marx says the profit and the surplus value are &ldquo;the same thing and "
                    "numerically equal&rdquo; here; what differs is the denominator of the rate. "
                    "Part II lets them differ in amount. Wages are v, not part of the surplus."},
            {"q": "Machinery worth £1,200 wears by £20 a period. In the rate of profit, how much "
                  "of the machinery is counted in the capital?",
             "a": ["£20, its wear", "£1,200, all of it", "£1,180, what is left", "None of it"],
             "c": 1,
             "why": "The rate of profit is calculated on the capital advanced, and all £1,200 is "
                    "advanced. The wear is what enters the cost price; £1,180 is what remains "
                    "after the period."},
        ],
        "mistakes": [
            ("Reading the rate of profit as the degree of exploitation",
             "It is a natural reading, since both are percentages of the same surplus. The first "
             "three presets refute it: each capital is £500 and makes £100, so each has a rate "
             "of profit of 20%, while the rate of surplus value is 50%, 100% and 200%. Exploitation "
             "is measured against v, and the rate of profit dilutes v in the whole capital."),
            ("Thinking profit and surplus value differ in amount here",
             "In Part I Marx treats them as the same magnitude with a different form; only the "
             "rates differ. That they can differ in amount is Part II's subject, in Average "
             "Profit and Its Fall."),
            ("Dividing by the cost price instead of the capital advanced",
             "The cost price counts fixed capital by its wear; the rate of profit counts it in "
             "full. With Marx's £1,200 of machinery the rate is `100/1,680 = 5/84`, under 6%, "
             "not the 20% that `100/500` would give."),
        ],
        "standard": (
            "Finish when you can compute s′ and p′ for one capital and say why they differ.",
            "Given c, v and s, with fixed capital counted in full, compute the rate of surplus "
            "value and the rate of profit, and given two capitals with equal rates of profit, "
            "state what further figure decides whether their rates of surplus value are equal."
        ),
        "note": (
            "The lab treats c as the constant capital advanced, so a preset must put the whole "
            "fixed capital in it, as the machinery preset does. The labour-heavy and "
            "capital-heavy figures are illustrative; Marx gives none in this chapter. Whether "
            "the rate on the whole capital is the right measure or a disguise is argued, not "
            "computed, and the lab does not decide it."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 3, l. 627-629 (p' : s' = v : C). Inline: l. 300 (Engels'
    # preface: the manuscript in equations, Samuel Moore), l. 625 (purely on
    # the field of mathematics), l. 749-751 (capitals II and III), l. 841
    # (80c + 20v + 40s), l. 849 (Ricardo), l. 930 (90c + 10v + 15s), l. 938
    # (104c + 16v + 24s), l. 942 (different countries), l. 944 (the summary).
    {
        "slug": "rate-of-profit-and-rate-of-surplus-value",
        "title": "The Rate of Profit and the Rate of Surplus Value",
        "module": "Chapter 3 · The Relation of the Rate of Profit to the Rate of Surplus-Value",
        "one_line": "The rate of profit is the rate of surplus value times the share of wages in the capital, so either factor can move it, and they can cancel.",
        "summary": (
            "Chapter 3 is algebra: the rate of profit equals the rate of surplus value times "
            "v/C, and Marx changes the factors one at a time. Raise s′ alone, raise c alone, then "
            "raise both, and compute p′ each time on Marx's own capitals. In one of them the "
            "rate of surplus value rises by half and the rate of profit does not move."
        ),
        "key": [
            "p′ = s′ · v / C",
            "p′ : s′ = v : C",
            "s′ fixed: p′ moves with v/C",
            "v/C fixed: p′ moves with s′",
            "both move: they can offset exactly",
        ],
        "key_label": "The third chapter in five lines",
        "concepts_intro": (
            "The chapter has one equation and many cases. Three ideas organise them."
        ),
        "concepts": [
            ("Two factors",
             "Since `s = s′·v`, the rate of profit is `p′ = s′·v/C`: the rate of surplus value "
             "times the share of variable capital in the whole. Every change in p′ is a change "
             "in one factor or both."),
            ("One at a time",
             "Marx holds one factor fixed and varies the other, then lets both vary. A rising, "
             "falling or constant p′ can go with a constant s′, and with a rising or falling "
             "one."),
            ("Absolute figures",
             "Percentages make capitals easy to compare and hide how a change happened. "
             "`80c + 20v` becoming `90c + 10v` could be more c, less v, or both; the chapter's "
             "cases need the absolute amounts."),
        ],
        "read_title": "The equation first, then its cases",
        "read_intro": (
            "The equation comes at the start of the chapter, in symbols and then in words. "
            "Everything after it is a case of it."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 3.</strong> &ldquo;Accordingly, p' = s/C = "
                  "s/(c+v). &hellip; And this equation may be expressed by the proportion p' : "
                  "s' = v : C, or in words, the rate of profit is proportioned to the rate of "
                  "surplus-value as the variable capital is to the total capital.&rdquo;"),
            ("p", "This chapter has a history of its own. Engels writes in his preface that for "
                  "it he had, besides Marx's main draft, a manuscript from the 1870s working out "
                  "the relation of the two rates &ldquo;in the form of equations&rdquo;, and that "
                  "he gave it to Samuel Moore, the translator of Volume I, who was better fitted "
                  "to edit it &ldquo;since he graduated from Cambridge in mathematics&rdquo;. "
                  "Engels finished the chapter from Moore's summary. You can feel it in the "
                  "prose: &ldquo;The analysis, therefore, is first carried on purely on the field "
                  "of mathematics.&rdquo;"),
            ("p", "The equation comes from putting `s = s′·v` into `p′ = s/C`, which gives "
                  "`p′ = s′·v/C`. Read as a proportion, `p′ : s′ = v : C`. The rate of profit is "
                  "the rate of surplus value scaled down by the share of v in the capital. If a "
                  "capitalist advanced only wages, with no means of production at all, the two "
                  "rates would be equal; Marx calls that case practically impossible."),
            ("p", "First case: hold s′ and v fixed and change c. Marx's three capitals are "
                  "`80c + 20v + 20s`, `100c + 20v + 20s` and `60c + 20v + 20s`, all at s′ = 100%. "
                  "Their rates of profit are 20%, `16 2/3`% and 25%: the same surplus on a "
                  "larger or smaller capital. In the lab, the base preset is the first and the "
                  "vary-composition preset the second, `1/6` at the same s′. The mass of surplus "
                  "value does not change at all."),
            ("p", "Second case: hold the composition fixed and change s′. Marx's capital "
                  "`80c + 20v + 40s` has s′ = 200% and p′ = 40%; `80c + 20v + 10s` has 50% and "
                  "10%. With v/C fixed, p′ moves in exactly the same proportion as s′. Marx says "
                  "s′ can differ between capitals of the same composition in three ways, through "
                  "wages, the intensity of labour or the length of the day, and that the first, "
                  "with the other two held constant, is the only case in which David Ricardo was "
                  "right that &ldquo;profits would be high or low, exactly in proportion as wages "
                  "would be low or high&rdquo;. Ricardo, the stockbroker whose <em>Principles</em> of 1817 "
                  "dominated English economics for a generation, reasoned as if the composition "
                  "of capital stood still. The vary-s preset is Marx's 200% capital."),
            ("p", "Third, both at once. Marx starts from `80c + 20v + 20s` and lets wages fall "
                  "so that the same workers cost 16 instead of 20: the capital becomes "
                  "`80c + 16v + 24s`, with s′ = 150% and p′ = 25%. For p′ to stay at 20%, the "
                  "capital would have to grow to 120, with c at 104: `104c + 16v + 24s`. That is "
                  "the both-offset preset. The rate of surplus value has risen by half, c/v has "
                  "gone from 4 to `13/2`, and the rate of profit has not moved. Marx says such an "
                  "exact offset happens only by an &ldquo;accidental coincidence&rdquo; within "
                  "one country, but that between two countries the same rate of profit rests "
                  "&ldquo;as a rule&rdquo; on different rates of surplus value."),
            ("p", "And the offset can overshoot. Marx's capital `90c + 10v + 15s` has s′ = 150% "
                  "and p′ = 15%. Set beside `80c + 20v + 20s`, s′ has risen from 100% to 150% and "
                  "p′ has fallen from 20% to 15%, because the share of v halved while s′ rose by "
                  "only half. The s-up-p-down preset shows it. Marx sums up the chapter in one "
                  "sentence: &ldquo;a rising rate of profit may be the companion of a falling or "
                  "rising rate of surplus-value&rdquo;, and so on through every combination."),
            ("p", "This is where the chapter matters for what comes later. In Part III Marx "
                  "argues that the rate of profit tends to fall as c grows faster than v, even "
                  "while exploitation rises. Mikhail Tugan-Baranovsky argued in 1901 that a "
                  "rising composition need not lower the rate at all, since the productivity that "
                  "raises c also cheapens it and the workers' necessities. Nobuo Okishio proved in "
                  "1961 that a new technique a capitalist adopts because it cuts his costs at the "
                  "going prices cannot, with the real wage unchanged, lower the general rate of "
                  "profit. This chapter does not settle that argument; it supplies the arithmetic "
                  "both sides use. The both-offset preset is the case where a rise in s′ exactly "
                  "cancels a rise in c/v, and the s-up-p-down preset the case where it does not. "
                  "Which case history produces is taken up in Average Profit and Its Fall."),
            ("p", "Every case here takes a single turnover of the capital. The next lesson, "
                  "“The Effect of Turnover on the Rate of Profit”, lets the capital turn over "
                  "several times a year, and the chapter it reads is Engels', not Marx's."),
        ],
        "lab": ("capkit", {
            "mode": "profit",
            "view": "relation",
            "money_unit": "£",
            "preset": "base",
            "presets": [
                {"id": "base", "label": "Marx's figures: 80c + 20v + 20s",
                 "c": 80, "v": 20, "s": 20, "expect": {"prRate": "1/5 = 20%", "prSRate": "1 = 100%"}},
                {"id": "vary-s", "label": "Marx's figures: s′ doubled, 80c + 20v + 40s",
                 "c": 80, "v": 20, "s": 40, "expect": {"prRate": "2/5 = 40%", "prSRate": "2 = 200%"}},
                {"id": "vary-composition", "label": "Marx's figures: c raised, 100c + 20v + 20s",
                 "c": 100, "v": 20, "s": 20, "expect": {"prRate": "1/6 = 16.67%", "prSRate": "1 = 100%"}},
                {"id": "both-offset", "label": "Marx's figures: s′ up by half, c/v to 13/2, 104c + 16v + 24s",
                 "c": 104, "v": 16, "s": 24, "expect": {"prRate": "1/5 = 20%", "prSRate": "3/2 = 150%"}},
                {"id": "s-up-p-down", "label": "Marx's figures: s′ up, p′ down, 90c + 10v + 15s",
                 "c": 90, "v": 10, "s": 15, "expect": {"prRate": "3/20 = 15%", "prSRate": "3/2 = 150%"}},
            ],
            "panel_title": "Two factors of the rate of profit",
            "panel_intro": (
                "c, v and s go in; the tiles give p′ and s′, and the banner gives c/v. Start "
                "from the base preset and change one factor at a time, then compare both-offset "
                "with the base: s′ rises, and p′ does not."
            ),
        }),
        "steps_title": "Predicting a change in the rate of profit",
        "steps_intro": "Four steps for comparing two states of a capital, or two capitals.",
        "steps": [
            ("Compute s′ for each",
             "Divide s by v in both states, from the absolute figures."),
            ("Compute v/C for each",
             "Divide v by `c + v`. This is the share of the capital that buys labour-power."),
            ("Multiply",
             "The rate of profit is `s′·v/C`. Check it against `s/(c + v)` computed directly."),
            ("Name the factor",
             "Say whether the change came from s′, from v/C or from both, and whether the two "
             "moved in the same direction, against each other, or exactly offset."),
        ],
        "worked": {
            "title": "A rise in exploitation that the rate of profit does not show",
            "intro": [
                "Marx's capital `80c + 20v + 20s` becomes `104c + 16v + 24s`. You want s′, v/C "
                "and p′ before and after.",
            ],
            "lines": [
                "before:  s′ = 20/20 = 100%,  v/C = 20/100 = 1/5",
                "before:  p′ = 1 · 1/5 = 20%",
                "after:  s′ = 24/16 = 3/2 = 150%,  v/C = 16/120 = 2/15",
                "after:  p′ = 3/2 · 2/15 = 1/5 = 20%",
                "c/v:  80/20 = 4 before,  104/16 = 13/2 after",
            ],
            "after": [
                "s′ rose by half and v/C fell by a third, and `3/2 · 2/3 = 1`. The rate of "
                "profit is unchanged although the workers do half as much again of unpaid "
                "labour per pound of wages.",
            ],
        },
        "quiz_title": "Moving one factor at a time",
        "quiz": [
            {"q": "A capital of 80c + 20v has s′ = 100%. The constant capital rises to 180 with "
                  "v and s′ unchanged. What is the new rate of profit?",
             "a": ["10%", "20%", "16.67%", "100%"],
             "c": 0,
             "why": "s stays at 20 on a capital of 200, so `p′ = 20/200 = 1/10`. 20% is the old "
                    "rate, 16.67% belongs to a c of 100, and 100% is s′."},
            {"q": "Two capitals have the same composition, 80c + 20v. One has s′ = 50%, the "
                  "other s′ = 150%. How do their rates of profit compare?",
             "a": ["They are equal",
                   "The second is three times the first",
                   "The second is 100 points higher",
                   "The second is higher by one half"],
             "c": 1,
             "why": "With v/C equal, p′ is proportional to s′: 10% and 30%. Equal rates would "
                    "need different compositions; the gap is 20 points, not 100; and 150% is "
                    "three times 50%, not one and a half times."},
            {"q": "In Marx's example, 80c + 20v + 20s becomes 90c + 10v + 15s. What happens?",
             "a": ["s′ and p′ both rise",
                   "s′ rises from 100% to 150% and p′ falls from 20% to 15%",
                   "s′ falls and p′ rises",
                   "Both stay the same"],
             "c": 1,
             "why": "`15/10 = 3/2` against `20/20 = 1`, so s′ rises; `15/100` against "
                    "`20/100`, so p′ falls. The share of v halved, which outweighs a rise in s′ "
                    "by half."},
            {"q": "When is Ricardo's rule, that profits rise exactly as wages fall, correct "
                  "according to the chapter?",
             "a": ["Always",
                   "Only when the composition of capital, the working day and the intensity of labour are constant",
                   "Only when the rate of surplus value is constant",
                   "Never"],
             "c": 1,
             "why": "Marx says this case, with the composition, the working day and the "
                    "intensity fixed and only wages varying, is &ldquo;the only one&rdquo; in "
                    "which Ricardo's assumption holds. A constant s′ would leave the split between "
                    "wages and surplus unchanged, so it cannot be the case his rule describes."},
        ],
        "mistakes": [
            ("Thinking a rising rate of surplus value must raise the rate of profit",
             "It holds only if the composition stays put, and Ricardo reasoned as though it did. "
             "The s-up-p-down preset refutes it on Marx's figures: s′ rises from 100% to 150% "
             "while p′ falls from 20% to 15%, because v's share of the capital halved. The "
             "both-offset preset shows the middle case, s′ up by half and p′ unchanged at 20%."),
            ("Reading a change in percentages as a change in amounts",
             "Marx's own warning: `80c + 20v` becoming `90c + 10v` in percentages could be "
             "`27,000c + 3,000v` from `12,000c + 3,000v`, or v falling with c fixed, or both "
             "changing. Compute the cases from absolute figures."),
            ("Expecting the mass of surplus value to change with c",
             "When c alone changes, s does not: `100c + 20v + 20s` still yields 20. Only the "
             "rate falls, to `1/6`, because the same surplus is divided by more capital."),
        ],
        "standard": (
            "Finish when you can predict the direction of p′ from changes in s′ and v/C.",
            "Given two states of a capital as c, v and s, compute s′, v/C and p′ for each, and "
            "state which factor moved p′ and whether the factors reinforced, opposed or offset "
            "each other."
        ),
        "note": (
            "Every capital in the presets is Marx's. The lab treats each pair as two capitals "
            "side by side; Marx says some of his transitions could hardly happen to one "
            "capital, and counts them as illustrations of independent capitals. Every case "
            "assumes one turnover, which the next lesson relaxes."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 3, l. 1036 (the annual formula). Inline: l. 300 (Engels'
    # preface: only the title), l. 976 (twelve months to weeks), l. 980-986
    # (capitals A and B), l. 988 (inversely as the periods), l. 994-1028
    # (capitals I-III), l. 1038 (the capitalist does not know v), l. 1040-1050
    # (the Manchester mill), l. 1052-1054 (the brave soul).
    {
        "slug": "turnover-and-the-rate-of-profit",
        "title": "The Effect of Turnover on the Rate of Profit",
        "module": "Chapter 4 · The Effect of the Turn-Over on the Rate of Profit",
        "one_line": "A variable capital turned over n times a year produces n times its surplus value on the same capital advanced, so the annual rate of profit is s′·n·v/C.",
        "summary": (
            "Marx left only the title of Chapter 4, and Engels wrote it. It carries Volume II's "
            "turnover into the rate of profit: the surplus value of a year is the surplus of "
            "one turnover times the number of turnovers, measured against the capital "
            "advanced once. Compute the annual rate on Engels' three capitals and on his "
            "Manchester spinning mill."
        ),
        "key": [
            "S = s · n in a year",
            "annual p′ = s′ · n · v / C",
            "C is advanced once, turned over n times",
            "halve the turnovers, halve the rate",
            "fixed capital is still in C",
        ],
        "key_label": "The fourth chapter in five lines",
        "concepts_intro": (
            "The chapter imports one result from Volume II and does three things with it."
        ),
        "concepts": [
            ("The annual rate of profit",
             "The surplus value of a year over the capital advanced. If v turns over n times, "
             "the year's surplus is `s·n` and the annual rate is `s′·n·v/C`."),
            ("Advanced, not turned over",
             "The rate is computed on the capital advanced, not on the sum of the capital "
             "values that pass through the year. A capital turned over twice is advanced "
             "once."),
            ("What the books do not show",
             "The capitalist's accounts record the wages paid in a year, `v·n`, not the "
             "variable capital v itself. Finding v takes a calculation, which Engels does for a "
             "real mill."),
        ],
        "read_title": "Engels' formula first, then his capitals",
        "read_intro": (
            "The passage is Engels' statement of the formula, near the end of the chapter. The "
            "cases that lead to it come before it in the text and after it here."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 4.</strong> &ldquo;In order that the formula "
                  "for the annual rate of profit may be exact, we must substitute the annual rate "
                  "of surplus-value for the simple rate of surplus-value, we must substitute S' "
                  "or s'n for s'. &hellip; Thus we obtain p' = s'n v/C, which is the formula for "
                  "the calculation of the annual rate of profit.&rdquo;"),
            ("p", "These are Engels' words, not Marx's. Volume III, like Volume II, is Engels' "
                  "edition of Marx's manuscripts, and for this chapter, his preface says, "
                  "&ldquo;Nothing was available for chapter IV but the title.&rdquo; He thought "
                  "the subject too important to leave out, so &ldquo;I have elaborated it "
                  "myself&rdquo;, and the whole chapter is printed in brackets and signed F. E. "
                  "Read it as Engels applying Volume II to Volume III, in his own voice and with "
                  "his own examples."),
            ("p", "He opens with the world he was living in. Shorter production time comes from "
                  "new processes, the Bessemer and Siemens methods in steel, alizarin dye made "
                  "from coal-tar in weeks instead of madder roots grown for years. Shorter "
                  "circulation time comes from railways, steamships, the telegraph and the Suez "
                  "Canal: a shipment to Eastern Asia took &ldquo;at least twelve months as late as "
                  "1847&rdquo;, and now almost as many weeks. Either shortening means less capital "
                  "lying idle and more surplus value on the same advance."),
            ("p", "Then the pure case. Capital A is `80c + 20v`, worth 100, at s′ = 100%, turned "
                  "over twice a year: its year's product is `160c + 40v + 40s`, and the 40 of "
                  "surplus value is reckoned on the 100 advanced, not on the 200 turned over, so "
                  "the annual rate is 40%. Capital B is `160c + 40v`, worth 200, turned over once: "
                  "the same year's product, the same 40, on 200 advanced, so 20%. With the same "
                  "composition and the same s′, &ldquo;the rates of profit are proportioned "
                  "inversely as their periods of turn-over&rdquo;."),
            ("p", "Engels' second set of capitals makes the point with fixed capital in them. "
                  "Capital I has 10,000 of fixed capital wearing 1,000 a year, 500 of circulating "
                  "constant capital and 500 of variable, at s′ = 100%, with v turned over ten times. "
                  "In a year v pays 5,000 of wages and produces 5,000 of surplus value on a "
                  "capital of 11,000: an annual rate of `5/11`, which Engels writes as "
                  "`45 5/11`%. That is the ten-times preset. Capital III has no fixed capital, "
                  "6,000 of constant and 5,000 of variable capital, turned over once: the same "
                  "5,000 on the same 11,000, the once preset. Turn capital I's v over only five "
                  "times and the year's surplus halves to 2,500, so the rate falls to `5/22`, "
                  "`22 8/11`%: the halved preset. The 10,000 of machinery has not changed, and "
                  "it is in C all the time."),
            ("p", "Why does this matter in practice? Because, Engels says, &ldquo;In most cases "
                  "the capitalist himself does not know the amount of variable capital invested "
                  "in his business.&rdquo; He pays wages and cotton from the same cash-box, and "
                  "his books show the wages of the year, `v·n`, not v. So Engels does the "
                  "calculation for the Manchester mill of 10,000 mule spindles from Volume I. "
                  "Its week: £20 of wear, £358 of circulating constant capital, £52 of wages, £80 "
                  "of surplus value. The machinery is valued at £10,000, and Engels assumes "
                  "£2,500 of circulating capital, split in the week's proportion into £2,182 "
                  "constant and £318 variable. A year's wages are `52 · 52 = 2,704`, so the £318 "
                  "turns over almost exactly 8½ times; s′ is `80/52`, about 154%. With C = "
                  "£12,500 the formula gives 33.27%."),
            ("p", "The engels preset runs that calculation, with v = 318, s per turnover = "
                  "`318 · 80/52`, n = 8½ and c = 12,182, and prints 33.27%. Engels checks it the "
                  "simple way: a year's surplus is `52 · 80 = 4,160`, and `4,160/12,500` is "
                  "33.28%. The hundredth of a point between them is the rounding of `2,704/318` "
                  "to 8½. Then comes his one sardonic aside. &ldquo;A certain brave soul was "
                  "shocked to the point of speechlessness over the abnormity of an annual rate of "
                  "profit of 1,000%&rdquo; in Volume II's example; here is an annual rate of "
                  "surplus value of more than 1,300%, &ldquo;taken from the practical life of "
                  "Manchester&rdquo;."),
            ("p", "The arithmetic is not in dispute: on any account, a capital that turns over "
                  "faster ties up less money for the same output and earns more on what it "
                  "advances, and a modern accountant's return on capital employed shows the same "
                  "effect. What is Marx's and Engels' own is the reason given, that the gain comes "
                  "from v working more often. An economist who counts every part of the capital "
                  "as productive explains the same figure by the circulating constant capital "
                  "turning over too, which in Engels' examples it does, at the same speed as v. "
                  "The formula puts the whole effect on v by its definitions; the lab computes it "
                  "on them and cannot test them."),
            ("p", "Engels ends by noting that statistics are almost silent on the split between "
                  "c and v, because few capitalists ever make his calculation. The next lesson, "
                  "“Economy in the Use of Constant Capital”, turns from the speed of capital to "
                  "its size: how a capitalist raises his rate of profit by spending less on c."),
        ],
        "lab": ("capkit", {
            "mode": "profit",
            "view": "turnover",
            "money_unit": "£",
            "preset": "ten-times",
            "presets": [
                {"id": "ten-times", "label": "Engels' capital I: 10,500c + 500v, v turned over 10 times",
                 "c": 10500, "v": 500, "s": 500, "turnovers": 10, "expect": {"prAnnual": "5/11 = 45.45%"}},
                {"id": "once", "label": "Engels' capital III: 6,000c + 5,000v, turned over once",
                 "c": 6000, "v": 5000, "s": 5000, "turnovers": 1, "expect": {"prAnnual": "5/11 = 45.45%"}},
                {"id": "halved", "label": "Engels' capital I with v turned over 5 times",
                 "c": 10500, "v": 500, "s": 500, "turnovers": 5, "expect": {"prAnnual": "5/22 = 22.73%"}},
                {"id": "engels", "label": "Engels' figures: the Manchester mill, £318 of v turned over 8½ times",
                 "c": 12182, "v": 318, "s": "6360/13", "turnovers": "17/2", "expect": {"prAnnual": "2,703/8,125 = 33.27%", "prSRate": "20/13 = 153.85%"}},
            ],
            "panel_title": "The rate of profit over a year",
            "panel_intro": (
                "c is the whole constant capital advanced, fixed capital included; s is the "
                "surplus value of one turnover of v. The first tile is the annual rate of "
                "profit; the second is the rate for one turnover. Compare ten-times with once: "
                "ten turnovers against one, and the same annual rate."
            ),
        }),
        "steps_title": "Computing the annual rate of profit",
        "steps_intro": "Four steps, the same for any capital whose variable part turns over n times a year.",
        "steps": [
            ("Find the capital advanced",
             "C is the whole capital advanced, fixed capital at its full value and the "
             "circulating capital at what one turnover needs."),
            ("Find the surplus of one turnover",
             "`s = s′·v`, where v is the variable capital advanced, not the wages of the year."),
            ("Multiply by the turnovers",
             "The year's surplus value is `s·n`, and the annual rate of surplus value is `s′·n`."),
            ("Divide by C",
             "The annual rate of profit is `s′·n·v/C`. Check it by dividing the year's surplus "
             "value directly by C."),
        ],
        "worked": {
            "title": "A capital of £1,000 turned over five times",
            "intro": [
                "A capital of £900 constant and £100 variable has s′ = 100%, and its variable "
                "part turns over five times a year. You want the annual rate of profit.",
            ],
            "lines": [
                "s per turnover:  1 · 100 = £100",
                "s in a year:  100 · 5 = £500",
                "C = 900 + 100 = £1000",
                "annual p′ = 500 / 1000 = 1/2 = 50%",
                "one turnover:  100 / 1000 = 10%",
            ],
            "after": [
                "The capital advanced is still £1,000; it has been used five times. Engels' "
                "capital I does the same on a larger scale: 10 turnovers of £500 give `5/11` on "
                "11,000, and five give half of that.",
            ],
        },
        "quiz_title": "The year and the turnover",
        "quiz": [
            {"q": "A capital of 400c + 100v at s′ = 100% turns its variable capital over four "
                  "times a year. What is the annual rate of profit?",
             "a": ["80%", "20%", "100%", "400%"],
             "c": 0,
             "why": "The year's surplus is `100 · 4 = 400` on a capital of 500, so `400/500 = "
                    "4/5`. 20% is one turnover's rate, 100% is s′, and 400% is the annual rate of "
                    "surplus value."},
            {"q": "Engels' capital A, 80c + 20v, turns over twice a year at s′ = 100%. Why is "
                  "its annual rate 40% and not 20%?",
             "a": ["Because the 40 of surplus is divided by the 100 advanced, not by the 200 turned over",
                   "Because its rate of surplus value is 200%",
                   "Because its fixed capital is smaller",
                   "Because it sells above value"],
             "c": 0,
             "why": "The rate of profit is on the capital advanced. s′ is still 100% per "
                    "turnover; capital A has no separate fixed capital in the example; and the "
                    "chapter assumes sale at value."},
            {"q": "Capital I has 10,000 of fixed capital and its 500 of variable capital turns "
                  "over 10 times a year; its annual rate is 5/11. If v turns over 5 times "
                  "instead, what is the rate?",
             "a": ["5/11, since the fixed capital is unchanged",
                   "5/22",
                   "10/11",
                   "1/22"],
             "c": 1,
             "why": "The year's surplus halves from 5,000 to 2,500 on the same 11,000, so the "
                    "rate halves. The unchanged fixed capital is in the denominator either way. "
                    "`1/22` is one turnover's rate."},
            {"q": "Engels says the capitalist usually does not know his variable capital. What "
                  "do his books show instead?",
             "a": ["The wages paid in the year, v times n",
                   "The rate of surplus value",
                   "The value of his fixed capital only",
                   "The variable capital, but not the turnovers"],
             "c": 0,
             "why": "Wages and materials come from the same cash-box, and a wages account shows "
                    "the year's total `v·n`. Finding v takes a separate calculation; s′ is not in "
                    "the books at all."},
        ],
        "mistakes": [
            ("Thinking turnover affects only the circulating capital's profit",
             "It is tempting to say faster turnover earns more on the circulating capital and "
             "leaves the fixed capital's return alone. But the rate of profit is on the whole "
             "capital advanced. The halved preset keeps capital I's 10,000 of fixed capital and "
             "turns v over five times instead of ten: the annual rate on the whole 11,000 falls "
             "from `5/11` to `5/22`."),
            ("Dividing by the capital turned over",
             "Capital A's year handles 200 of capital value, but only 100 is advanced. Its 40 of "
             "surplus is 40% on the advance; dividing by the 200 gives 20%, capital B's rate, "
             "and erases the difference the chapter is about."),
            ("Expecting more turnovers always to mean a higher rate",
             "Capital I turns over ten times and capital III once, and both earn `5/11` a year, "
             "because III has ten times the variable capital. Turnover multiplies v; the "
             "composition still matters."),
        ],
        "standard": (
            "Finish when you can compute an annual rate of profit from s′, n, v and C.",
            "Given a capital's constant and variable parts, its rate of surplus value and the "
            "number of turnovers of v in a year, compute the year's surplus value and the "
            "annual rate of profit on the capital advanced."
        ),
        "note": (
            "Engels' figures throughout, except the worked example. The engels preset uses his "
            "8½ turnovers and so prints his 33.27%; the exact turnover gives his check figure, "
            "33.28%. The lab, like Engels, turns the circulating constant capital over with v "
            "and assumes no credit, so every pound of circulating capital is the capitalist's "
            "own."
        ),
    },
]
