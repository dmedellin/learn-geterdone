"""Course 3 -- The Component Parts of Price: Book I, Chapters 6 and 7.

One lesson module: Chapter 6 is one lesson, and Chapter 7 is two (its
definitions and mechanism, then the causes that keep a price above the natural
price).
"""

from . import part_a

COURSE = {
    "slug": "wealth-component-parts-of-price",
    "title": "The Component Parts of Price",
    "level": "Beginner",
    "summary": (
        "Book I, Chapters 6 and 7. What a price is made of once stock and land are "
        "owned, how a price resolves into wages, profit and rent, and how the price "
        "actually paid moves around the natural price that pays each part at its "
        "ordinary rate: effectual demand, the quantity brought to market, and the "
        "secrets, scarcities and monopolies that hold a price up."
    ),
    "blurb": (
        "Read Smith's rule that every price resolves into wages, profit and rent, with "
        "the arithmetic beside it. Follow a batch of bread from the farmer to the "
        "baker, run his two manufactories to see why profit is not wages, and work a "
        "market short of goods, glutted with them and held short by a monopolist."
    ),
    "key": [
        "price = wages + profit + rent, in the end",
        "profit is a share of the stock advanced",
        "natural price: every part at its natural rate",
        "short supply: market price above natural",
        "glut: market price below natural",
        "monopoly price: the highest which can be got",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no economics and no earlier course is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Chapters 6 and 7 yourself and say, in "
        "Smith's terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Resolve a price",
         "Given each stage's wages, rent and rate of profit, compute the price after "
         "every stage and the wages, rent and profit it resolves into."),
        ("Say why profit is not wages of inspection",
         "Compute the profit on two stocks that employ the same labour at the same "
         "rate, and say what Smith concludes from the difference."),
        ("Place a market price against the natural price",
         "Given the natural price, the effectual demand and the quantity brought, say "
         "whether the market price is above, at or below the natural price, and why."),
        ("Read a monopolist's price",
         "Given a buyers' schedule, compute the price and the excess over the natural "
         "price at several quantities, and say what Smith's sentence does and does not "
         "claim."),
    ],
    "syllabus_intro": (
        "Three lessons: one on Chapter 6, which states the rule, and two on Chapter 7, "
        "which says how the price paid keeps returning to the price the rule gives, "
        "and what can stop it."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Smith's words "
        "and then goes back through them a phrase at a time. This course is a "
        "read-along of Adam Smith, <em>An Inquiry into the Nature and Causes of the "
        "Wealth of Nations</em> (1776), quoted from the public-domain Electronic "
        "Classics Series edition (Pennsylvania State University, 2005).",
        "Money is in Smith's units where a figure is his: twelve pence to a shilling "
        "and twenty shillings to a pound. The first lesson works in pounds, and the "
        "second and third in shillings a yard of cloth, with figures written for the "
        "lessons.",
        "Use the labs to change one thing at a time. The presets of one lesson vary "
        "a single figure against the one before: the number of stages, the quantity "
        "brought to market, the quantity a monopolist keeps back.",
        "Keep the rule apart from the verdict. Every figure is computed from the "
        "chapter's own definitions. Whether prices are made as Smith says is the "
        "argument of the book, and each lesson says where later economists disagreed.",
    ],
    "not_covered": [
        "What fixes the rates of wages, profit and rent. Chapter 7 calls them natural "
        "and says they vary with the state of the society; the four chapters after it "
        "give the account, and the next course takes the first two.",
        "The long run of the price of corn and silver. Chapter 7 gives the idea of a "
        "natural price in the abstract, and the Digression on the Value of Silver, "
        "which belongs to the course on rent, puts figures to it.",
        "The Capital argument with Smith's resolution of price. Smith's rule is here "
        "stated as he stated it; the lesson on Chapter 6 names the Capital lesson that "
        "argues with it and does not repeat it.",
        "Any modern theory of price or monopoly. Where a lesson mentions a later "
        "writer, it is to say who disagreed with Smith and why, not to teach their "
        "theory.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states, Smith's own or written for the lesson, in exact arithmetic. The "
        "figures show what the chapters' reasoning implies for those quantities, and "
        "no lab can tell you whether prices are made as Smith says."
    ),
    "lessons": part_a.LESSONS,
}
