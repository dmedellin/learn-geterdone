"""Course 2 -- From Money to Surplus Value: Volume I, Parts II and III, Chapters 4-11.

Split across two lesson modules: part_a is Chapters 4 to 8, from the general
formula for capital to constant and variable capital; part_b is Chapters 9
to 11, the rate of surplus value, Senior's last hour, the two lessons on the
working day, and the rate and mass of surplus value.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-money-into-surplus-value",
    "title": "From Money to Surplus Value",
    "level": "Beginner",
    "summary": (
        "Volume I, Parts II and III, The Transformation of Money into Capital and The "
        "Production of Absolute Surplus-Value: Chapters 4 to 11. How money becomes capital, "
        "why buying and selling cannot explain the increment, what labour-power is and what "
        "it is worth, how a day's work yields more value than a day's labour-power costs, "
        "and how the rate, the length of the working day and the number of workers fix the "
        "surplus."
    ),
    "blurb": (
        "Follow Moneybags from the market into the spinning mill. Compute what a mark-up "
        "adds to the sum of values, value a day's labour-power, do Marx's yarn arithmetic "
        "for six hours and for twelve, measure the surplus against the variable capital, "
        "recompute Senior's last hour, and see what a legal limit on the day does to the "
        "rate."
    ),
    "key": [
        "C–M–C: sell to buy; M–C–M′: buy to sell",
        "ΔM = M′ − M is surplus value",
        "value of product = c + v + s",
        "rate of surplus value = s / v",
        "s / v = surplus labour / necessary labour",
        "mass of s = variable capital × s / v",
    ],
    "assumes_short": "Commodities and Money",
    "assumes_long": (
        "the value, the forms of value and the money of Commodities and Money, especially "
        "value as socially necessary labour-time and the circuit C–M–C"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of Parts II and III yourself and say, in "
        "Marx's terms, where the surplus comes from and what limits it."
    ),
    "outcomes": [
        ("Read a circuit",
         "Name a sequence of sale and purchase as C–M–C or M–C–M′ from what stands at its "
         "ends, and compute the increment ΔM."),
        ("Show what circulation cannot do",
         "Compute the values held before and after a round of mark-ups or a single cheat, "
         "and identify whose gain is whose loss."),
        ("Value labour-power",
         "Compute the daily value of labour-power from a bundle of necessities bought on "
         "different schedules, with children's upkeep and training."),
        ("Find the surplus in a product",
         "Compute the value of a product from materials, wear and hours, the surplus over "
         "the capital advanced, and what an instrument transfers per day."),
        ("Measure and divide the surplus",
         "Compute s/v, divide a product into the parts that carry c, v and s, and recompute "
         "Senior's claim about the last hour."),
        ("Work with the working day",
         "Compute the rate for any length of day, the effect of a legal limit, and the mass "
         "of surplus value from the number of workers and the rate, with its limit."),
    ],
    "syllabus_intro": (
        "Three lessons read Part II, one chapter each. Seven read Part III: one each for "
        "Chapters 7, 8 and 11, two for Chapter 9 (the rate, and Senior's last hour) and two "
        "for Chapter 10 (the limits of the day, and the struggle over them)."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and "
        "then goes back through them a phrase at a time. Quotations are from the Kerr "
        "editions in the Online Library of Liberty, hosted by Liberty Fund, Inc.",
        "Keep the spinning mill in your head. From Chapter 7 on, Marx reuses one example: "
        "cotton at a shilling a pound, 2s of wear for every 10 lb, a day's labour-power "
        "worth 3s, the value of 6 hours. “The Labour Process and the Production of Surplus "
        "Value” sets it up, and the next five lessons all return to it.",
        "Use the labs to change one thing at a time. Each preset moves a single figure, a "
        "mark-up, the hours, the price of cotton, a legal limit, and the point of the lesson "
        "is in what moves and what does not.",
        "Keep the definitions apart from the verdict. Every figure is computed from the "
        "definitions the chapter gives, and the word exploitation in Chapter 9 is one of "
        "them. Whether those definitions describe the economy you live in is what the book "
        "argues about, and each lesson says where the strongest objections come from.",
    ],
    "not_covered": [
        "Prices that differ from values. This course follows Volume I in assuming that "
        "commodities sell at their values, and the surplus is computed on that assumption. "
        "How prices of production depart from values, and whether that undoes Volume I, is "
        "the subject of Average Profit and Its Fall.",
        "Relative surplus value. Every lesson here holds the value of labour-power fixed and "
        "moves the length of the day. Shortening the necessary part of the day by making "
        "wage goods cheaper is the next course, Relative Surplus Value.",
        "Wages as a price of labour. The lessons speak of the value of labour-power and "
        "compute it from a bundle of necessities. How that value appears as a price per hour "
        "or per piece is Volume I's Part VI, in Wages and Accumulation.",
        "The full historical record of Chapter 10. The factory inspectors' reports Marx "
        "quotes run to dozens of pages; the lessons give the dates and the cases that carry "
        "the argument, and no lab models the history beyond the length of the day.",
        "Theories of profit as a reward for waiting or risk. The abstinence argument, "
        "Böhm-Bawerk's theory of interest and the marginal productivity theory of wages "
        "are stated at their strongest where Marx argues with them. They are not developed "
        "or computed.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the sums, hours and "
        "workers a lesson states, in exact arithmetic, on Marx's definitions. The figures are "
        "Marx's where a preset says so and illustrative otherwise, and no lab can tell you "
        "whether the surplus is unpaid labour or a return to capital."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
