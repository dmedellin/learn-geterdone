"""Course 1 -- Commodities and Money: Volume I, Part I, Chapters 1-3.

Split across two lesson modules: part_a is Chapter 1, one lesson per section;
part_b is Chapter 2 and the three lessons on Chapter 3.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-commodities-and-money",
    "title": "Commodities and Money",
    "level": "Beginner",
    "summary": (
        "Volume I, Part I, Commodities and Money: Chapters 1 to 3. What a commodity is "
        "and why its value is labour-time, how that value is expressed until it becomes "
        "money, why the relation looks like a property of things, how money arises from "
        "exchange, and what it does as measure, means of circulation, hoard, means of "
        "payment and world money."
    ),
    "blurb": (
        "Read the hardest chapter of Capital slowly, with the arithmetic beside it. "
        "Compute a commodity's value from producers' hours, read the elementary form of "
        "value and watch it grow into money, count what a single equivalent saves, and "
        "compute the money a day's sales and a chain of debts need."
    ),
    "key": [
        "value per unit = total hours / total output",
        "x of A = y of B: A relative, B equivalent",
        "barter n·(n − 1)/2 ratios; money n − 1",
        "price = value in hours / hours in £1",
        "money needed = sum of prices / velocity",
        "bullion out = imports − exports − receipts",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no economics and no earlier course is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Part I yourself and say, in Marx's "
        "terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Compute a value",
         "Compute socially necessary labour-time per unit from producers' hours and "
         "outputs, value a lot at it, and say how much of a slow producer's time the "
         "product does not carry."),
        ("Separate the two sides of labour",
         "Given a change in productivity, compute the value per unit and of a period's "
         "output, and state which moved: the use-values or the value."),
        ("Read the form of value",
         "Name the relative and equivalent forms in an equation of value, compute how a "
         "lot's expression moves when either commodity's hours change, and write the "
         "expanded, general and money forms."),
        ("State what fetishism names",
         "Compute hours per unit from a ledger and say whether, in a given setting, the "
         "producers see the hours or only the ratio of their products."),
        ("Compute money in circulation",
         "Compute prices from values and gold's value, and the money a period needs from "
         "the sum of prices, the velocity, credit sales and payments that fall due or "
         "cancel."),
        ("Settle a balance in bullion",
         "Compute the bullion a country ships or receives from its imports, exports and "
         "other payments, and name the function of world money it performs."),
    ],
    "syllabus_intro": (
        "Four lessons read the four sections of Chapter 1, one lesson reads Chapter 2, "
        "and three follow Chapter 3 from money as a measure to money crossing a border."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words "
        "and then goes back through them a phrase at a time, so the passage is worth a "
        "second reading once the lesson is done. Quotations are from the Kerr editions "
        "in the Online Library of Liberty, hosted by Liberty Fund, Inc.",
        "Expect Chapter 1 to be slow. Marx said himself that “every beginning is "
        "difficult”, and the four lessons on it take one section each for that reason. “The Form of "
        "Value” is the hardest; if it does not land the first time, read “The Fetishism "
        "of Commodities” and come back to it.",
        "Use the labs to change one thing at a time. Each preset changes a single figure "
        "against the one before, a weaver's hours, a coat's value, gold's value, one "
        "unpaid bill, and the point of the lesson is in what moves and what does not.",
        "Keep the definitions apart from the verdict. Every figure is computed from the "
        "definitions the chapter gives. Whether those definitions describe the economy "
        "you live in is what the book argues about, and each lesson says where the "
        "strongest objections come from.",
    ],
    "not_covered": [
        "The reduction of skilled to simple labour. Marx says an hour of skilled labour "
        "counts as several hours of simple labour and then assumes every hour is simple. "
        "No lab here computes that multiplier, because the chapter gives no way to.",
        "Prices that differ systematically from values. Chapter 1's labs value commodities "
        "at socially necessary labour-time, and Chapter 3's price them at their values. "
        "How prices of production depart from values is Volume III's subject, in Average "
        "Profit and Its Fall.",
        "The debates over the value-form and the opening of the book. Readers have argued "
        "for more than a century about how to read Chapter 1, its relation to Hegel and "
        "whether its first section is an argument or a starting assumption. The lessons "
        "state the strongest objection where there is a standard one, and go no further.",
        "Modern money. Part I is read as an account of money based on gold. Currencies "
        "today are not convertible into any commodity, and the lessons say so in a "
        "sentence where it matters; no lab models fiat money.",
        "Marx's footnotes and the history of monetary theory. Locke, Montesquieu, Hume, "
        "Bailey and the mercantilists appear where the chapter argues with them, briefly "
        "and at their strongest. A history of the theory of money is not attempted.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the hours, prices "
        "and payments a lesson states, in exact arithmetic, on Marx's definitions. The "
        "hours are illustrative except where a preset says it uses Marx's figures, and no "
        "lab can tell you whether labour-time is what value really is."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
