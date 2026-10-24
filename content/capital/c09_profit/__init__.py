"""Course 9 -- Cost Price and the Rate of Profit: Volume III, Part I, Chapters 1-7.

Split across two lesson modules: part_a is Chapters 1 to 4, part_b Chapters 5
to 7, one lesson per chapter.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-cost-price-and-profit",
    "title": "Cost Price and the Rate of Profit",
    "level": "Intermediate",
    "summary": (
        "Volume III, Part I, The Conversion of Surplus-Value into Profit and of the Rate of "
        "Surplus-Value into the Rate of Profit: Chapters 1 to 7. How the capitalist's cost "
        "price hides the difference between constant and variable capital, how the same "
        "surplus value measured against the whole capital becomes the rate of profit, what "
        "moves that rate, from exploitation and composition to turnover, economies in "
        "constant capital and the price of raw materials, and why the capitalist does not see "
        "his profit as surplus value."
    ),
    "blurb": (
        "Take Volume I's c, v and s and look at them as the owner of the business does. "
        "Compute cost price and profit, the rate of profit beside the rate of surplus value, "
        "the annual rate of a capital that turns over many times, and the rate after a saving "
        "in constant capital or a rise in the price of cotton, mostly on Marx's and Engels' own "
        "figures."
    ),
    "key": [
        "cost price  k = c + v",
        "value = k + s; profit at value = s",
        "rate of profit  p′ = s / (c + v)",
        "p′ = s′ · v / C",
        "annual p′ = s′ · n · v / C",
        "s and v fixed: p′ moves against c",
    ],
    "assumes_short": "Volumes I and II",
    "assumes_long": (
        "the Volume I courses, above all the rate of surplus value from From Money to Surplus "
        "Value, and the turnover of variable capital from The Turnover of Capital"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of Part I yourself and say, for each figure, "
        "whether it is the capitalist's measure or Marx's."
    ),
    "outcomes": [
        ("Compute cost price and profit",
         "From c, v and s and a selling price, compute the cost price, the value and the "
         "profit, and state whether a sale is above or below value and above or below cost."),
        ("Compute the two rates",
         "Compute the rate of surplus value and the rate of profit for one capital, with fixed "
         "capital counted in full, and show that equal rates of profit can rest on unequal "
         "rates of surplus value."),
        ("Separate the two factors",
         "Given two states of a capital, compute s′ and v/C for each and state which factor "
         "moved the rate of profit, and whether the two offset each other."),
        ("Compute an annual rate",
         "From the rate of surplus value, the variable capital, its turnovers in a year and the "
         "capital advanced, compute the annual rate of profit."),
        ("Price a change in constant capital",
         "Compute the rate of profit after a saving in constant capital or a change in the price "
         "of raw material, passed on in the product's price in full, in part or not at all."),
        ("Read one account two ways",
         "Put a capitalist's books beside Marx's categories for the same figures, and explain "
         "why two businesses exploiting labour equally earn different rates of profit."),
    ],
    "syllabus_intro": (
        "Seven lessons read the seven chapters of Part I in order: cost price and profit, the "
        "rate of profit and its two factors, the effect of turnover, economy in constant "
        "capital, the price of raw materials, and the chapter of further remarks that closes "
        "the Part."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with the text and then "
        "goes back through it a phrase at a time, so the passage is worth a second reading "
        "once the lesson is done. Quotations are from the Kerr editions in the Online Library "
        "of Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of book Volume III is. Marx wrote its main manuscript in the 1860s and "
        "did not finish it; Engels edited it from his drafts and published it in 1894, eleven "
        "years after Marx's death. Part I gave him the most trouble: his preface says the main "
        "manuscript served it only with considerable restrictions, so Chapter 1 comes from two "
        "attempts at rewriting, Chapter 3 from a later manuscript of equations, and Chapter 4 "
        "is Engels' own text: Marx left only its title, and the lesson on it says so.",
        "Keep Volume I's letters in view. Part I takes c, v and s exactly as Volume I left them "
        "and measures them a different way. Marx's capital of 400c + 100v + 100s appears in "
        "several lessons, so that one change at a time can be seen against it.",
        "Keep the definitions apart from the verdict. Every figure is computed on Marx's "
        "definitions, and in particular on his claim that only variable capital produces "
        "surplus value. Economists who treat profit as a return to all capital compute many of "
        "the same figures and read them differently, and the lessons say where.",
    ],
    "not_covered": [
        "The general rate of profit and prices of production. Part I assumes that profit "
        "equals the surplus value of each capital and that commodities sell at their values. "
        "How capitals of different composition come to earn one rate is Part II, in Average "
        "Profit and Its Fall.",
        "The falling rate of profit. Chapter 3 supplies the arithmetic that the law of Part III "
        "uses, and the lesson on it names the dispute; the law itself and its counteracting "
        "causes belong to Average Profit and Its Fall.",
        "The longer working day as an economy in fixed capital. Chapter 5 opens with it, and "
        "the lesson describes it, but the economy view holds s and v fixed and does not compute "
        "it.",
        "Stocks, waste and the tie-up of capital. Chapter 6's second section shows how a rise "
        "in raw material revalues the stocks a capital holds; the lab changes only c and the "
        "selling price.",
        "The full history of the cotton famine. Chapter 6 ends with the factory inspectors' "
        "reports of 1845 to 1864 on prices, short time, wages and relief; the lesson takes a "
        "handful of their figures and leaves the rest to the text.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the c, v and s a lesson "
        "states, in exact arithmetic, on Marx's definitions. Most presets use Marx's or Engels' "
        "own capitals and say so; the rest are illustrative. No lab can tell you whether the "
        "profit on a capital is unpaid labour or a return the capital earns."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
