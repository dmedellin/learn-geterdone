"""Course 11 -- Merchant's Capital and Interest: Volume III, Parts IV-V, Chapters 16-24.

Split across two lesson modules: part_a is Part IV, Chapters 16-20 (merchant's
capital); part_b is the first four chapters of Part V, Chapters 21-24
(interest-bearing capital). Part V continues in Credit and Fictitious Capital.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-merchants-and-interest",
    "title": "Merchant's Capital and Interest",
    "level": "Advanced",
    "summary": (
        "Volume III, Part IV, the Transformation of Commodity-Capital and Money-Capital into "
        "Commercial Capital and Financial Capital, Chapters 16 to 20, and the first four "
        "chapters of Part V, Division of Profit into Interest and Profit of Enterprise, "
        "Chapters 21 to 24. How merchants and money-dealers share in surplus value without "
        "producing any, how merchants profited before there was an average to share, what a "
        "lender sells, why the rate of interest has bounds and no law, and why money at "
        "interest looks as if it grew by itself."
    ),
    "blurb": (
        "Follow surplus value out of the factory to the people who never produce it. Compute "
        "Marx's general rate with a merchant's capital in it, the mark-up a fast-turning "
        "merchant adds, a money-dealer's share, the interest on a borrowed £100 and what is "
        "left after a manager's salary, and Richard Price's penny at compound interest beside "
        "what a real product could pay."
    ),
    "key": [
        "rate = s / (industrial + merchant capital)",
        "mark-up = annual rate / turnovers",
        "interest = sum lent × rate of interest",
        "enterprise = profit − interest − salary",
        "normal bounds: 0 < i < p′",
        "compound sum = c · (1 + i)ⁿ",
    ],
    "assumes_short": "Volume III, Parts I–III",
    "assumes_long": (
        "the earlier courses, and above all Cost Price and the Rate of Profit and Average "
        "Profit and Its Fall, whose general rate of profit this course divides further, and "
        "the costs of circulation from The Circuits of Capital"
    ),
    "outcomes_intro": (
        "By the end you can follow surplus value from the industrial capital that produces it "
        "to the merchant, the money-dealer and the lender who share it, and say on Marx's "
        "accounting where each share comes from."
    ),
    "outcomes": [
        ("Size a merchant's capital",
         "Compute the commodity capital a merchant takes off the producers' hands from his "
         "advance and turnovers, and the merchant's capital a year's trade needs."),
        ("Price the merchant's sale",
         "Compute the general rate of profit with merchant's and money-dealing capital in it, "
         "the manufacturer's price to the merchant and the merchant's selling price, with and "
         "without the merchant's costs."),
        ("Find the mark-up per turnover",
         "From the general rate and a merchant's turnovers, compute the addition to the price "
         "of each sale and show the annual rate is unchanged."),
        ("Split profit into interest and enterprise",
         "Given capital, the sum borrowed, the rates of profit and interest and a manager's "
         "salary, compute interest, profit of enterprise and what is left after the salary, "
         "and test whether the rate of interest lies within its bounds."),
        ("Weigh a compound claim",
         "Compute a sum at compound interest beside the same sum grown with a real product, "
         "and state from what the interest would have to be paid."),
    ],
    "syllabus_intro": (
        "Five lessons read Part IV, one chapter each: commercial capital, commercial profit, "
        "the merchant's turnover, money-dealing capital and the history of merchant's capital. "
        "Four read the opening chapters of Part V on interest-bearing capital, the rate of "
        "interest, profit of enterprise and the fetish of money that breeds money."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and then "
        "goes back through them a phrase at a time, so the passage is worth a second reading once "
        "the lesson is done. Quotations are from the Kerr editions in the Online Library of "
        "Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of book Volume III is. Marx drafted it in the 1860s and never finished "
        "it; Friedrich Engels edited the manuscripts and published the volume in 1894. Part V "
        "in particular, he wrote in his preface, more than once ended in &ldquo;a disarranged "
        "mass of notes, comments and extracts&rdquo;, and Chapter 23 still has a numbered point marked as a blank in the manuscript. The "
        "lessons follow Engels' text.",
        "Keep Marx's 900 and 100 in view. “Commercial Profit” sets up 720c + 180v of industrial "
        "capital with 180 of surplus value and a merchant's capital of 100, and three lessons "
        "use those figures. Where a chapter gives no figures, as Chapter 19 does not, the "
        "lesson's figures are illustrative and it says so.",
        "Keep the definitions apart from the verdict. Every figure is computed on Marx's "
        "definitions: that trade and money-dealing add no value, and that interest is a share "
        "of profit. Both are disputed, and each lesson names who disputes them and on what "
        "ground.",
    ],
    "not_covered": [
        "Credit, banks and fictitious capital. Part V goes on from Chapter 25 into the credit "
        "system, bank capital and the money market; those chapters are the next course, Credit "
        "and Fictitious Capital.",
        "The merchant's labour and the law of necessary labour in circulation. Marx lists "
        "questions in Chapter 17, how the merchant's labour preserves the value of his constant "
        "capital among them, that the chapter leaves open; the lessons do not try to answer "
        "them.",
        "The trade cycle and the market rate of interest. Chapter 22 sets the cycle aside and "
        "reports a few rates from the 1840s; no lab models the cycle or the supply of loanable "
        "money.",
        "Modern finance and money. The chapters describe merchants, cashiers and lenders of "
        "Marx's century and money based on gold. A lesson says in a sentence where a modern "
        "institution differs, and no lab models central banking or fiat money.",
        "The historians' debate over trade and the transition to capitalism. Historical Facts "
        "about Merchant's Capital names Pirenne, Sweezy, Dobb and Brenner and does not try to "
        "settle the dispute.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the capitals, rates and "
        "turnovers a lesson states, in exact arithmetic, on Marx's definitions. The 900 and 100, "
        "the 15 per cent and five turnovers, the £100 at 20 per cent and Price's penny are "
        "Marx's or his sources'; the rest are illustrative. No lab can tell you whether trade "
        "adds value or whether interest is only a share of profit."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
