"""Course 7 -- Stock, Money and Banks: Book II, the Introduction and Chapters 1-2.

Five lessons, all in part_a. Chapter 2 is read in three: gross and net revenue,
paper money and the Scottish banks, drawing and redrawing.
"""

from . import part_a

COURSE = {
    "slug": "wealth-stock-and-money",
    "title": "Stock, Money and Banks",
    "level": "Intermediate",
    "summary": (
        "Book II, the Introduction and Chapters 1 and 2. Why stock must be laid up before "
        "labour can be divided, how Smith sorts a stock into what is kept for consumption, "
        "fixed capital and circulating capital, why money is a wheel of circulation and "
        "no part of a nation's revenue, what paper money spares, and what it costs a bank "
        "that issues too much."
    ),
    "blurb": (
        "Read the book's turn from the division of labour to the stock that makes it "
        "possible. Sort a weaver's and a parish's stock into Smith's three portions, "
        "subtract the upkeep of machines and money from a gross revenue, work out the "
        "gold that a million of notes sets free, and price the old trick of drawing and "
        "redrawing bills."
    ),
    "key": [
        "stock first, then division of labour",
        "stock = consumption + fixed + circulating",
        "net revenue = gross − fixed − money upkeep",
        "gold spared = circulation − coin reserve",
        "notes beyond the circulation come back",
        "redraw cost = interest + commission a draw",
    ],
    "assumes_short": "Book I, in outline",
    "assumes_long": (
        "no economics beyond what Book I's courses cover, and school arithmetic is "
        "enough: the lessons say again what a pound, a shilling and a penny are when a "
        "figure needs them"
    ),
    "outcomes_intro": (
        "By the end you can do the sums that sit under Smith's account of stock and "
        "banks, and say what each figure does and does not show."
    ),
    "outcomes": [
        ("State why stock comes first",
         "Say why a weaver, or any specialist, needs a stock laid up before the web is "
         "sold, and what must grow with the division of labour: the provisions, or the "
         "materials and tools."),
        ("Sort a stock into Smith's three portions",
         "Given a list of holdings, classify each as kept for immediate consumption, fixed "
         "capital or circulating capital by Smith's test (does it yield a revenue by "
         "staying or by going?), and compute the shares."),
        ("Separate gross from net revenue",
         "Compute a society's net revenue from its gross, the upkeep of its fixed capital "
         "and the upkeep of its money, and explain why Smith says money is no part of the "
         "revenue it circulates."),
        ("Compute what paper spares",
         "From a circulation, a quantity of notes and a coin reserve, compute the gold and "
         "silver a banking system sets free, and the notes that must come back."),
        ("Price drawing and redrawing",
         "Compute what a trader paid a year to raise money by renewing bills, from the "
         "interest, the commission and the term of each bill, and compare it with the "
         "profits Smith says a merchant could expect."),
    ],
    "syllabus_intro": (
        "Five lessons follow Book II to the end of its second chapter: the stock that "
        "must come first, Smith's three portions of a stock, the revenue of a nation and "
        "what is deducted from it, the paper that replaces gold, and the dangerous trade "
        "of the bill that is drawn only to be redrawn."
    ),
    "how_to": [
        "Read the passage before the explanation. Each lesson opens on Smith's own words "
        "and then goes back through them. This course is a read-along of Adam Smith, "
        "<em>An Inquiry into the Nature and Causes of the Wealth of Nations</em> (1776); "
        "quotations are from the public-domain Electronic Classics Series edition "
        "(Pennsylvania State University, 2005), and Smith's spelling is kept inside them.",
        "Money is in pounds, shillings and pence, as Smith has it: twelve pence to the "
        "shilling and twenty shillings to the pound. Most figures in this course are in "
        "pounds, and a lesson says when a sum is Smith's own and when it is written for "
        "the lesson.",
        "Use the labs to change one thing at a time. Each preset moves a single quantity "
        "against the one before it: a bank's notes, a reserve, a month more on every bill. "
        "The point of a lesson is in what moves and what does not.",
        "Keep the arithmetic apart from the verdict. Every figure shows what Smith's "
        "reasoning implies for the quantities stated. Whether the reasoning describes any "
        "bank, in his century or ours, is what the chapter argues and its critics dispute.",
    ],
    "not_covered": [
        "The history of the Bank of England. Smith's account of its charter, its loans to "
        "government and its capital runs for a page and a half; the lessons keep what bears "
        "on circulation and leave the rest to the book.",
        "Law and the Mississippi scheme, the Bank of Amsterdam, and the colonial paper "
        "currencies of North America. Each appears in the chapter's last pages; the lessons "
        "mention what they illustrate and no lab models them.",
        "Modern money. Smith's notes are promises to pay gold and silver on demand. No lab "
        "here models a currency that is convertible into nothing, a central bank, or a "
        "deposit, and the lessons say so where it matters.",
        "Later monetary theory. Thornton, Ricardo, the Currency and Banking schools and "
        "Marx's account of credit all wrote after Smith. They appear where they bear on a "
        "step, briefly and at strength, and a history of monetary thought is not attempted.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the stocks, notes, "
        "reserves and rates a lesson states, in exact arithmetic, on Smith's definitions. "
        "Some figures are Smith's and say so; the rest are written for the lesson. No lab "
        "can tell you whether a bank behaves the way the chapter says it does."
    ),
    "lessons": part_a.LESSONS,
}
