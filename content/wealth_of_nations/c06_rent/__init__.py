"""Course 6 -- The Rent of Land: Book I, Chapter 11.

Split across two lesson modules: part_a is the chapter's introduction, Part I and
Part II; part_b is Part III with the long Digression on the value of silver, and the
chapter's conclusion on the three great orders of society.
"""

from . import part_a, part_b

COURSE = {
    "slug": "wealth-rent-of-land",
    "title": "The Rent of Land",
    "level": "Intermediate",
    "summary": (
        "Book I, Chapter 11, the longest chapter of The Wealth of Nations. What rent is "
        "and why Smith calls it a monopoly price, which produce of land always affords "
        "a rent and which only sometimes, how the price of corn in silver was read "
        "across four centuries in the Digression on the value of silver, and what the "
        "progress of improvement does to the rent of land and to the interests of "
        "landlords, labourers and dealers."
    ),
    "blurb": (
        "Read the longest chapter of the book in six lessons, with its arithmetic in "
        "front of you. Compute a farm's rent as what a price leaves after wages, "
        "stock and ordinary profit, find which of four coal mines can pay a rent, "
        "average Smith's prices of wheat into periods and read the value of silver "
        "from them, and follow a rise in the price of cattle into the rent of a "
        "Highland estate."
    ),
    "key": [
        "rent = price − outlay − ordinary profit",
        "high price: the cause of rent, not its effect",
        "the best mine's price rules the others",
        "falling price of corn: silver grown dearer",
        "outlay fixed, price up: rent up faster",
        "dealers: interest opposite to the public's",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no economics and no earlier course is assumed, and school arithmetic is "
        "enough; Smith's pounds, shillings and pence are explained in the lessons "
        "that use them"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of the chapter yourself and say, in "
        "Smith's terms, what each figure is a figure of and what it does not show."
    ),
    "outcomes": [
        ("Compute a rent",
         "Given a farm's output, wages, stock, the ordinary rate of profit and the "
         "price of its produce, compute its rent as the residual and say at what "
         "price it would afford none."),
        ("Compare lands",
         "Compute and compare the rents of lands that differ in fertility and in "
         "distance from the market, and say how a road changes them."),
        ("Tell which mines pay a rent",
         "Given several mines' outputs and outlays and the price set by the best of "
         "them, say which can be worked, which pay no rent and which pay one."),
        ("Read the value of silver from the price of corn",
         "Average prices of corn by period, compare them with the first period and say "
         "what Smith infers from a rise or a fall, and what he does not."),
        ("Test a run of averages",
         "Reduce best wheat to middle wheat and to ounces of silver, and say which "
         "period's average needs a footnote and why."),
        ("Follow a price change into rent",
         "Compute the rent of a land at two prices with the outlay held fixed, say why "
         "it changes by a larger proportion than the price, and name the order whose "
         "interest Smith calls opposite to the public's."),
    ],
    "syllabus_intro": (
        "Three lessons read the introduction and Parts I and II of Chapter 11, two "
        "follow the Digression on silver, and the last takes Part III's three sorts of "
        "produce through to the end of the chapter."
    ),
    "how_to": [
        "Read the passage before the explanation. Each lesson opens with Smith's words "
        "and goes back through them, so the passage is worth a second reading once "
        "the lesson is done. The course is a read-along of Adam Smith, <em>An Inquiry "
        "into the Nature and Causes of the Wealth of Nations</em> (1776), and "
        "quotations are from the public-domain text of the Electronic Classics Series "
        "edition (Pennsylvania State University, 2005).",
        "Expect a long chapter. The Digression on silver is the hardest stretch, with "
        "its ounces of silver, its shillings of two different dates and its tables of "
        "wheat prices. The lessons take it in two pieces, and the labs average the "
        "prices for you. Smith writes pounds, shillings and pence: twelve pence to the "
        "shilling and twenty shillings to the pound, so a pound is 240 pence, and a quarter "
        "of corn is eight bushels. The labs keep to pence where the figures need it.",
        "Use the labs to change one thing at a time. Each preset changes a single "
        "figure against the one before: a price, a wage, a mine's output. The point "
        "of the lesson is in what moves and what does not.",
        "Keep the arithmetic apart from the verdict. Every figure is computed from "
        "the definitions the chapter gives, and some of the farms and mines are written "
        "for the lessons, not taken from Smith. Whether Smith's reasoning describes any "
        "economy is what the book argues about, and each lesson says where the "
        "strongest objections come from.",
    ],
    "not_covered": [
        "The tables of Windsor prices. The chapter ends with Fleetwood's prices of wheat "
        "from 1202 to 1597 and the Eton College prices to 1764. The lessons use "
        "the averages Smith prints and a handful of years, with the line cited, and "
        "leave the rest of the table to the book.",
        "The Corn Laws. Smith's account of the bounty on the export of corn is Book "
        "IV, Chapter 5, and the Digression only refers to it. Nothing in this course "
        "models the bounty.",
        "Later theories of rent. Ricardo's differential rent, Malthus on the nature "
        "and progress of rent, and Marx's absolute rent come after Smith and appear "
        "here only where the chapter's own claims meet them, briefly and at their "
        "strongest. The Capital Subject's course Ground Rent is the place for them.",
        "The ratio of gold to silver. Smith discusses it at some length, and the "
        "fifth lesson reads it in prose; no lab computes it.",
        "The modern value of any of Smith's sums. The labs do not convert his money "
        "to present prices, and nothing here says what a pound of 1776 would buy now.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the outputs, "
        "wages, stock and prices a lesson states, in exact arithmetic, on Smith's "
        "definitions. The farms and mines are written for the lessons except where a "
        "preset says it uses Smith's figures, and no lab can tell you whether the "
        "chapter's reasoning describes an economy you could measure."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
