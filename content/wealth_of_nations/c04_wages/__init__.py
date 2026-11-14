"""Course 4 -- Wages and Profits: Book I, Chapters 8 and 9.

One lesson module of five: Chapter 8 is three lessons (the bargain and the
floor, the funds that raise wages, and what a liberal reward does), and Chapter 9
is two (profit and interest, and the last page on prices).
"""

from . import part_a

COURSE = {
    "slug": "wealth-wages-and-profits",
    "title": "Wages and Profits",
    "level": "Beginner",
    "summary": (
        "Book I, Chapters 8 and 9. What fixes the wages of labour and the profits of "
        "stock: the bargain between masters and workmen and the floor beneath it, the "
        "funds destined for maintaining labour, the liberal reward and the numbers of the "
        "people, profit read from the rate of interest, and why a rise of profit raises a "
        "price more than a rise of wages."
    ),
    "blurb": (
        "Read Smith on wages and profit with the arithmetic beside it. Set a wage "
        "against a family's weekly needs, compute a wage from a fund and a number of "
        "workers over the years, count the doublings of a population, read profit from "
        "interest, and watch a rise of profit compound through the stages of a linen "
        "manufacture."
    ),
    "key": [
        "wages follow the contract; masters can wait",
        "the floor: the family's maintenance, plus",
        "wage rises with the increase of the fund",
        "population follows the demand for men",
        "stock grows: wages up, profit down",
        "profit compounds through the stages",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no economics and no earlier course is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Chapters 8 and 9 yourself and say, in "
        "Smith's terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Set a wage against a subsistence",
         "Given a family's weekly needs and a wage, compute the shortfall or surplus, "
         "and compare the wage with Cantillon's minimum of twice a man's own maintenance."),
        ("Follow a wage from the funds",
         "Given a fund for maintaining labour and a number of workers with their yearly "
         "growth rates, compute the wage each year and say whether it rises, holds or "
         "falls, and why Smith says increase and not size matters."),
        ("Count a population's doublings",
         "Given a doubling time and a number of years, compute the population after "
         "them, and say what in Smith's text sets the rate."),
        ("Read profit from interest",
         "Given rates of interest and a multiple, compute the implied profit and what "
         "is left after interest, and say why Smith's rule of double interest is limited."),
        ("Compare a wage rise with a profit rise",
         "Price a chain of stages with a rise of wages and with a rise of profit and say "
         "which part rises in arithmetical and which in geometrical proportion."),
    ],
    "syllabus_intro": (
        "Five lessons: three on the long Chapter 8, from the bargain over wages to what "
        "a liberal reward does to the people, and two on Chapter 9, from the rate of "
        "profit to the page on prices."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Smith's words "
        "and then goes back through them a phrase at a time. This course is a "
        "read-along of Adam Smith, <em>An Inquiry into the Nature and Causes of the "
        "Wealth of Nations</em> (1776), quoted from the public-domain Electronic "
        "Classics Series edition (Pennsylvania State University, 2005).",
        "Money is in Smith's units where a figure is his: twelve pence to a shilling "
        "and twenty shillings to a pound. The first lesson works in pence a week, the "
        "second in pounds a year, and the last in pounds.",
        "Use the labs to change one thing at a time. Each preset of a lesson varies a "
        "single figure against the others: the wage, the growth of the fund, the "
        "doubling time, the rate of interest, the rise of profit.",
        "Keep the rule apart from the verdict. Every figure is computed from the "
        "chapter's own reasoning. Whether that reasoning describes any economy is "
        "what the book argues, and each lesson says where Ricardo, Malthus, Marx "
        "and later writers parted from it.",
    ],
    "not_covered": [
        "The long evidence for British wages in Chapter 8. Smith's four proofs that "
        "wages are above the lowest rate, the comparison of the last century with the "
        "present, and the register of prices of provisions are summarised and not "
        "worked, and his pages on dear and cheap years are passed over.",
        "The comparisons among countries in Chapter 9. Scotland, France, Holland, the "
        "colonies and Bengal appear as examples of a tendency, and the history of the "
        "French rate of interest and of usury in the Roman provinces is left out.",
        "Wages in different employments and the proportion between them. Chapter 10 "
        "takes that up, and the next course reads it.",
        "The rent of land. Chapter 11 is its own course, and Chapter 7's idea that rent "
        "can be an effect of price and not a cause is used there.",
        "Any modern theory of wages, population or the rate of interest. A later writer "
        "is named where he disagreed with Smith, to say why, and no theory is taught.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states, Smith's own or written for the lesson, in exact arithmetic. The figures "
        "show what the chapters' reasoning implies for those quantities, and no lab can "
        "tell you whether wages and profit are fixed as Smith says."
    ),
    "lessons": part_a.LESSONS,
}
