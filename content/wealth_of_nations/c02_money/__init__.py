"""Course 2 -- Money and the Measure of Value: Book I, Chapters 4 and 5.

One lesson module: part_a is Chapter 4, and the three parts of Chapter 5.
"""

from . import part_a

COURSE = {
    "slug": "wealth-money-and-measure",
    "title": "Money and the Measure of Value",
    "level": "Beginner",
    "summary": (
        "Book I, Chapters 4 and 5. Why a common instrument of exchange arises and why it "
        "ends as a stamped metal, what the real measure of exchangeable value is and why "
        "Smith says it is labour, how corn and silver serve in its place over centuries "
        "and over years, and what a prince does to a creditor when he lessens the silver "
        "in the coin."
    ),
    "blurb": (
        "Count the exchange rates a market needs with no money and with one, turn a "
        "money price into a price in days of labour, see a fixed rent fall as corn "
        "grows dear, and work out how much silver a creditor loses when the pound is "
        "debased."
    ),
    "key": [
        "ratios without a measure: n·(n − 1)/2",
        "real price = money price / price of a day",
        "rent in corn = money rent / price of a quarter",
        "silver per penny: first coined / later coined",
        "a debased coin pays a creditor in less silver",
    ],
    "assumes_short": "The Division of Labour",
    "assumes_long": "the first course, which gives the units (pounds, shillings and pence) and the division of labour that makes exchange necessary",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Chapters 4 and 5 yourself and say, in "
        "Smith's terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Count what exchange costs without money",
         "Compute the rates a market must quote with no common measure and with one, and "
         "say which of a set of traders can deal directly."),
        ("Say why metals became money",
         "State the reasons Smith gives for the choice of metals and for the public stamp, "
         "and say what the denominations of the coins first meant."),
        ("Turn a money price into a labour price",
         "Compute the real price of a good in days of labour from its money price and the "
         "money price of a day, and say whether a change in money price was a change in "
         "the real price."),
        ("Value a rent in corn and in silver",
         "Compute what a fixed money rent buys in corn at two dates, and say which of "
         "corn and silver Smith thinks the better measure over a century and over a year."),
        ("Work out a debasement",
         "From the pence coined from a pound weight of silver in two periods, compute the "
         "silver in a penny and the share of the silver a creditor paid in the new coin "
         "loses."),
    ],
    "syllabus_intro": (
        "One lesson reads Chapter 4, and three read the three parts of Chapter 5: the "
        "thesis that labour is the real measure, the advice about corn and silver, and "
        "the long section on the coin."
    ),
    "how_to": [
        "This Subject is a read-along of Adam Smith, <em>An Inquiry into the Nature and "
        "Causes of the Wealth of Nations</em> (1776). Every lesson quotes the passage it "
        "reads from the public-domain Electronic Classics Series edition (Pennsylvania "
        "State University, 2005) and keeps Smith's spelling inside the quotations. A "
        "copy of the book is welcome but not needed.",
        "Know the units before you start. Twelve pence make a shilling and twenty "
        "shillings a pound, so a pound is 240 pence; a guinea is a gold coin that the "
        "law of Smith's day valued at 21 shillings; a quarter of corn is eight bushels. "
        "Chapter 4 says that the pound sterling was first a pound weight of silver, and "
        "the last lesson works what happened to it.",
        "Use the labs to change one thing at a time. A preset labelled with Smith's name "
        "uses figures from his pages; a preset marked <em>written for this "
        "lesson</em> uses figures invented to show the reasoning, and the lessons say "
        "which is which.",
        "Keep what Smith reasons apart from what the labs show. A figure here shows what "
        "the reasoning of a chapter implies for the quantities stated. Whether the "
        "reasoning describes any economy is what the book argues, and the lessons say "
        "where the strongest objections come from.",
    ],
    "not_covered": [
        "The history of money. Smith's conjecture that money grew out of barter is read "
        "at the strength he gives it and a sentence of the objections to it is added; "
        "no history of money or of credit is attempted.",
        "The Windsor and other tables of corn prices. Book I, Chapter 11 and the Digression "
        "on silver use a handful of years as data; this course uses only the two prices "
        "Chapter 5 gives, twenty-five and fifty shillings.",
        "The theory of a measure of value after Smith. Ricardo's objection to labour "
        "commanded is stated once, and the index number once; the dispute over whether "
        "any measure of value can be invariable is not developed.",
        "Bullion, the mint and the balance of the coinage in detail. The long discussion "
        "of the price of silver bullion and Locke's view of it is summarised in one "
        "paragraph, and the figures for gold and silver in the English mint are used "
        "only as far as they check.",
        "Value in Capital. The step from barter to a common equivalent and the "
        "distinction of use and exchange are read by Capital in other lessons, named where "
        "they arise and not repeated.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the quantities a "
        "lesson states, in exact arithmetic. Where a preset says it is Smith's, the "
        "figures are his, and the lessons give the line of the text. Every other figure "
        "is written for the lesson, and no lab can tell you whether labour is the "
        "measure of value or whether a prince gains by debasing the coin."
    ),
    "lessons": part_a.LESSONS,
}
