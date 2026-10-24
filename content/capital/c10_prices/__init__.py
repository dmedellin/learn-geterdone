"""Course 10 -- Average Profit and Its Fall: Volume III, Parts II-III, Chapters 8-15.

Split across two lesson modules: part_a is Part II's Chapters 8 to 11;
part_b is Chapter 12 and the three chapters of Part III.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-prices-of-production",
    "title": "Average Profit and Its Fall",
    "level": "Advanced",
    "summary": (
        "Volume III, Part II, Conversion of Profit into Average Profit, and Part III, The Law of "
        "the Falling Tendency of the Rate of Profit: Chapters 8 to 15. Why capitals of different "
        "composition would earn different rates at value, how competition turns values into "
        "prices of production at one general rate, what market value and surplus profit are, how "
        "wages move prices, and why, on Marx's account, the general rate tends to fall as "
        "productivity rises, what checks the fall, and how it ends in over-accumulation."
    ),
    "blurb": (
        "Read the two most disputed results in Capital with Marx's own tables beside them. "
        "Transform his five spheres into prices of production and check his totals, form a market "
        "value, reprice after a wage rise, run the law of the falling rate and its counteracting "
        "causes, and compute what over-accumulation and devaluation do to the rate."
    ),
    "key": [
        "p′ = s / (c + v), at value, by sphere",
        "general rate = total s / total capital",
        "price of production = k + p′ · capital",
        "Σ prices = Σ values; Σ profit = Σ s",
        "market value = average over every unit",
        "s′ fixed, c/v up: p′ down",
        "offset = p′ with checks − p′ without",
    ],
    "assumes_short": "Volumes I and II, and Cost Price and the Rate of Profit",
    "assumes_long": (
        "Cost Price and the Rate of Profit, whose cost price and rate of profit every lesson here "
        "uses, and from Volume I the rate of surplus value of From Money to Surplus Value and the "
        "rising composition of capital of Wages and Accumulation"
    ),
    "outcomes_intro": (
        "By the end you can do every table in Parts II and III yourself and say which of Marx's "
        "claims each one supports, and which it leaves open."
    ),
    "outcomes": [
        ("Compute rates at value",
         "Given capitals' c, v and rates of surplus value, compute each rate of profit if goods "
         "sold at their values, and state what composition does to the ranking."),
        ("Transform values into prices",
         "Compute a general rate of profit, every sphere's price of production and its deviation "
         "from value, and check the two totals, with inputs at value as Chapter 9 takes them."),
        ("Form a market value",
         "Compute a market value from groups producing under different conditions, and each "
         "group's surplus profit or loss per unit."),
        ("Reprice after a change",
         "Compute the new general rate and prices of production after a general change in wages, "
         "or with a premium for one sphere paid from the same total."),
        ("Run the law and its checks",
         "Compute the rate and mass of profit through a rising composition, the part of the fall "
         "a rising s′ or cheaper c offsets, and the rate under over-accumulation and after "
         "devaluation."),
    ],
    "syllabus_intro": (
        "Five lessons read the five chapters of Part II, from unequal rates at value to the "
        "general rate and its supplements, and three read the three chapters of Part III, the law, "
        "its counteracting causes and its contradictions."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and then "
        "goes back through them a phrase at a time, so the passage is worth a second reading once "
        "the lesson is done. Quotations are from the Kerr editions in the Online Library of "
        "Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of book Volume III is. Marx wrote its main draft in 1864 and 1865, before "
        "Volume I was published, and never finished it. Friedrich Engels edited the manuscript and "
        "published it in 1894, eleven years after Marx's death, and a few passages, marked in the "
        "Kerr text with his initials, are Engels' own. Marx's tables of Chapter 9 are printed in "
        "the book as tables; the lessons use their figures and check them against the totals the "
        "text prints.",
        "Expect argument. The transformation of values into prices and the falling rate of profit "
        "are the two results of Volume III most disputed since it appeared. Each lesson does "
        "Marx's arithmetic exactly as he gives it, states the standard objection where the step is "
        "taken, and says who makes it. No lab here takes a side, and none computes more than "
        "Marx's tables do.",
        "Watch the totals and the offsets. In Part II the tile to keep an eye on is the one that "
        "compares total price with total value; in Part III it is the one that compares the rate "
        "with and without the counteracting causes. Most of what is claimed and disputed is in "
        "those two figures.",
    ],
    "not_covered": [
        "Solutions to the transformation problem. Chapter 9 prices inputs at their values, and Marx "
        "notes that this may be an error. Bortkiewicz's solution, Sraffa's prices, the New "
        "Interpretation and the temporal single-system reading are named in “The General Rate of "
        "Profit and Prices of Production”; none is computed, because computing one would take a "
        "side in a live dispute.",
        "Empirical tests of the falling rate of profit. Whether the rate has fallen in any economy, "
        "and whether its movements explain crises, is argued with national accounts this course "
        "does not carry. The lessons say the law is stated as a tendency and leave it there.",
        "Okishio's theorem as a model. “Counteracting Influences” states the theorem and the main "
        "replies to it; the lab does not build the general-equilibrium model the theorem needs.",
        "Merchant's capital and the division of profit. The general rate here is shared among "
        "industrial capitals only; merchants, interest and rent take their shares in Merchant's "
        "Capital and Interest and the courses after it.",
        "Market prices out of line with market values. Chapter 10's lab computes market value "
        "from the mix of producers; the cases in which an excess or shortage of supply lets the "
        "best or the worst producers set the price outright are described, not computed.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the capitals, rates and "
        "periods a lesson states, in exact arithmetic, on Marx's definitions and with inputs "
        "valued as he values them. Marx's tables are his; other figures are illustrative and say "
        "so. No lab can tell you whether prices of production really rest on values, or whether "
        "the rate of profit really tends to fall."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
