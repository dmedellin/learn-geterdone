"""The Capital path, as data: a read-along of Marx's *Capital*, all three volumes.

Fourteen courses in Marx's order, one lesson for every chapter and more for
the long ones. The content lives here and only here; scripts/ turns it into
pages. Each lesson quotes its passage from the public-domain Kerr editions
(see /mnt/project-files/capital-texts/ during authoring) and computes what the
chapter computes in the capkit lab. The design is docs/capital/PLAN.md.
"""

from . import (
    c01_commodities,
    c02_surplus_value,
    c03_relative,
    c04_accumulation,
    c05_primitive,
    c06_circuits,
    c07_turnover,
    c08_reproduction,
    c09_profit,
    c10_prices,
    c11_interest,
    c12_credit,
    c13_rent,
    c14_revenues,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c01_commodities.COURSE,
    c02_surplus_value.COURSE,
    c03_relative.COURSE,
    c04_accumulation.COURSE,
    c05_primitive.COURSE,
    c06_circuits.COURSE,
    c07_turnover.COURSE,
    c08_reproduction.COURSE,
    c09_profit.COURSE,
    c10_prices.COURSE,
    c11_interest.COURSE,
    c12_credit.COURSE,
    c13_rent.COURSE,
    c14_revenues.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "capital",
    "title": "Capital, Read Along",
    "level": "Beginner \u2192 Advanced",
    "level_note": "school arithmetic only; no economics is assumed",
    "tagline": (
        'Karl Marx&rsquo;s <em>Capital</em>, read chapter by chapter, all three volumes &mdash; with the arithmetic Marx does on the page done in front of you: value and money, the working day, surplus value, wages, accumulation, turnover, reproduction, profit, prices of production, interest and rent. Fourteen courses and 119 lessons are available.'
    ),
    "description": (
        "The Capital Subject: a read-along of all three volumes in Marx's own order, fourteen courses that follow his Parts, a lesson for every chapter and more for the long ones. Each lesson reads a passage first, then explains it, then computes what the chapter computes &mdash; a commodity's value, a rate of surplus value, a reproduction scheme that balances or does not, a price of production, a rent schedule &mdash; in exact arithmetic in your browser. All fourteen courses and 119 lessons are available."
    ),
    "key": ['value of product = c + v + s', 'rate of surplus value  s′ = s / v', 'day = necessary + surplus labour', 'simple reproduction: I(v + s) = II c', 'rate of profit  p′ = s / (c + v)', 'price of production = k + k · p̄′', 'price of land = rent / rate of interest'],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. From Money to Surplus Value uses the value of Commodities and Money; Relative Surplus Value uses the working day; Wages and Accumulation uses all of Volume I's arithmetic; the three Volume II courses add time and the balance of two departments; the Volume III courses re-read every one of those categories as profit, prices of production, interest and rent; Revenues and Their Sources uses all of it."
    ),
    "why_order": ["The order is Marx's, and it is the order of the argument. Volume I studies capital in production, under the simplifying assumption that everything sells at its value; Volume II studies capital in circulation, where time and balance enter; Volume III puts the two together and lets competition, credit and landed property break the simplifications one by one.", 'Commodities and money come first because every later category is built from them. Surplus value cannot be stated before value is, and capital cannot be distinguished from money before money is.', "The historical Part Eight of Volume I comes after accumulation, not before, because Marx wants the reader to see the mechanism first and then ask where the first capital came from. Read in the book's order, the history answers a question the reader already has.", "Volume III's profit, interest and rent come last because each is a share of surplus value under another name. Read without Volume I they look like three separate incomes from three separate sources, which is exactly the appearance the last course, Revenues and Their Sources, takes apart."],
    "prerequisites": ["School arithmetic: fractions, percentages and a willingness to add up a column. Marx's examples are in shillings, pounds and hours, and every one of them is a sum or a ratio. The labs do the arithmetic; what is asked of you is to say what each number means.", 'No economics. The Subject introduces every category it uses in the chapter where Marx introduces it, and it introduces the classical economists Marx is arguing with &mdash; Smith, Ricardo, Say, Senior, Mill &mdash; at the moment he argues with them. If you have studied modern economics, expect to unlearn some vocabulary: &ldquo;capital&rdquo;, &ldquo;profit&rdquo; and &ldquo;value&rdquo; do not mean here what they mean in a textbook, and the first lessons say exactly how.', "A copy of the book is welcome but not required. Every lesson quotes the passage it reads from the public-domain Kerr editions: Volume I in the Moore and Aveling translation as revised by Ernest Untermann, Volumes II and III in Untermann's translation. Chapter numbers follow the English edition of Volume I, which differs from the German from Chapter 4 on; the two places where that matters say so.", 'Patience with abstraction. Volume I assumes that commodities sell at their values; Volume III takes that assumption away. A reader who stops after Volume I has read the first half of an argument, and several lessons say so on purpose.'],
    # Each path names its own hazard. This one's is that the arithmetic is
    # exact and the definitions are the argument.
    "material": (
        'every figure on this path is computed in your browser from the quantities a lesson states and the definitions Marx gives in the chapter being read, and a figure is only as good as the definitions it was computed from &mdash; whether they describe the economy you live in is the question the book argues and the lab cannot settle.'
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what the lesson states: a value is total hours over total output, a rate of surplus value is a ratio of two sums, a scheme balances or it does not, a price of production is a cost price plus the average profit. Nothing is rounded except where a lesson says so. Quotations are from the public-domain Kerr editions, as published in the Online Library of Liberty. What the labs cannot do is tell you whether Marx's definitions are the right ones &mdash; and that is what the book is arguing about."
    ),
    "courses": COURSES,
}
