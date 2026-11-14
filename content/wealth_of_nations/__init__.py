"""The Wealth of Nations path, as data: a read-along of Adam Smith's *An Inquiry
into the Nature and Causes of the Wealth of Nations* (1776), all five Books.

Thirteen courses in Smith's order, a lesson for a chapter or for a Part of a
long one. The content lives here and only here; scripts/ turns it into pages.
Each lesson quotes its passage from the public-domain Electronic Classics
Series edition (see /mnt/project-files/wealth-texts/ during authoring) and
works the arithmetic of the chapter in the wonkit lab. The design is
docs/wealth-of-nations/PLAN.md.
"""

from . import (
    c01_division,
    c02_money,
    c03_price,
    c04_wages,
    c05_employments,
    c06_rent,
    c07_stock,
    c08_accumulation,
    c09_opulence,
    c10_mercantile,
    c11_colonies,
    c12_expenses,
    c13_taxes,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c01_division.COURSE,
    c02_money.COURSE,
    c03_price.COURSE,
    c04_wages.COURSE,
    c05_employments.COURSE,
    c06_rent.COURSE,
    c07_stock.COURSE,
    c08_accumulation.COURSE,
    c09_opulence.COURSE,
    c10_mercantile.COURSE,
    c11_colonies.COURSE,
    c12_expenses.COURSE,
    c13_taxes.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "wealth-of-nations",
    "title": "The Wealth of Nations, Read Along",
    "level": "Beginner → Advanced",
    "level_note": "school arithmetic only; no economics is assumed",
    "tagline": (
        'Adam Smith&rsquo;s <em>The Wealth of Nations</em>, read chapter by chapter, all five Books in his order &mdash; with the arithmetic on his pages worked in front of you: the division of labour, money and the measure of value, price and its parts, wages, profit and rent, stock and banks, trade policy, and the revenue and debts of the sovereign. Thirteen courses and 65 lessons are available.'
    ),
    "description": (
        "The Wealth of Nations Subject: a read-along of all five Books in Smith's own order, thirteen courses that follow his Books and chapters, a lesson for a chapter or for a Part of a long one. Each lesson reads a passage first, then explains it, then works what the chapter works &mdash; the pin factory's output, a price resolved into wages, profit and rent, a wage from the funds for maintaining labour, a rent as what is left after wages and ordinary profit, a capital grown by parsimony, the cost of a bounty, a tax on wages and who pays it &mdash; in exact arithmetic in your browser. All thirteen courses and 65 lessons are available."
    ),
    "key": [
        "produce per head = share at work × output",
        "price = wages + profit + rent",
        "market price vs natural price",
        "wage = funds for labour / workers",
        "rent = price − wages − ordinary profit",
        "capital × returns a year = labour employed",
        "price of land = rent × years' purchase",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. Book I's six courses build price from labour, money, wages, profit and rent; the two Book II courses add stock, banks and accumulation; Book III reads the history of Europe with all of it; the two Book IV courses use every category to examine the mercantile and agricultural systems; and the two Book V courses ask what a sovereign must spend and how it should raise the money."
    ),
    "why_order": [
        "The order is Smith's, and it is the order of the argument. Book I explains what makes labour productive and how its produce is divided into wages, profit and rent; Book II explains the stock that sets labour to work; Book III tells how Europe's actual history departed from what Books I and II call the natural course; Book IV examines the two systems of policy that grew out of that history; Book V asks what a government must do and how to pay for it.",
        "The division of labour comes first because everything later depends on it. Smith begins the book with the pin factory, not with money or trade, and money, exchange and the extent of the market follow as consequences of dividing work.",
        "Price, wages, profit and rent come before stock because Book II assumes them. A capital that returns four times a year is a capital whose profits Book I has already explained.",
        "The critique of the mercantile system comes late on purpose. Book IV is the part of the book most often quoted, and its arguments use the categories of every earlier Book; read first, the invisible hand is a slogan, read fourth, it is a conclusion about where capital goes.",
    ],
    "prerequisites": [
        "School arithmetic: fractions, percentages and a willingness to add up a column. Smith's figures are in pounds, shillings and pence, ounces of silver and quarters of corn; the first course explains each unit once (twelve pence to the shilling, twenty shillings to the pound, eight bushels to the quarter), and the labs do the arithmetic.",
        "No economics. The Subject introduces each category in the chapter where Smith introduces it, and introduces the writers he argues with &mdash; Mun, Mandeville, Cantillon, Hume, Quesnay &mdash; at the moment he argues with them. If you have studied modern economics, expect familiar words to carry older meanings: &ldquo;stock&rdquo;, &ldquo;natural price&rdquo; and &ldquo;productive labour&rdquo; are Smith's terms and the lessons say what each means.",
        "A copy of the book is welcome but not required. Every lesson quotes the passage it reads from the public-domain Electronic Classics Series edition, which prints the text of the later editions; Smith's spelling is kept inside quotations.",
        "Patience with Smith's examples. The book argues by long examples &mdash; a pin factory, a Highland village, the corn trade, the Bank of Amsterdam &mdash; and the examples are the argument. The lessons read them in outline and say what they skip.",
    ],
    # Each path names its own hazard. This one's is that the arithmetic follows
    # the chapter's reasoning, and the reasoning is what is disputed.
    "material": (
        "every figure on this path is computed in your browser from the quantities a lesson states, Smith&rsquo;s own or written for the lesson, and shows what the reasoning of the chapter implies for those quantities; whether that reasoning describes any economy, then or now, is what the book argues and its critics dispute, and no lab can settle it."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what the lesson states: a produce per head, a price resolved into its parts, a wage from a fund and a number of workers, a rent as what is left after wages and ordinary profit, a capital after years of saving, a tax and who pays it. Nothing is rounded except where a lesson says so. Quotations are from the public-domain text of the Electronic Classics Series edition (Pennsylvania State University, 2005). What the labs cannot do is tell you whether Smith's reasoning describes the economy you live in &mdash; and that is what the book is arguing about."
    ),
    "courses": COURSES,
}
