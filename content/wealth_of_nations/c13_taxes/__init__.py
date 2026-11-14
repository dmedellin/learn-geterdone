"""Course 13 -- Taxes and Public Debts: Book V, Chapters 2 and 3.

Seven lessons, the last course of the Subject; its last lesson closes the book.
part_a is Chapter 2 (the sovereign's own funds, the four maxims, and the taxes
upon rent, profit and wages); part_b is the taxes upon consumable commodities
and Chapter 3, Of Public Debts, which ends the Inquiry.
"""

from . import part_a, part_b

COURSE = {
    "slug": "wealth-taxes-and-public-debts",
    "title": "Taxes and Public Debts",
    "level": "Advanced",
    "summary": (
        "Book V, Chapters 2 and 3, the last two chapters of the Inquiry. The funds a "
        "sovereign can own, the four maxims by which Smith tests a tax, and then the "
        "taxes themselves, on rent, on profit, on wages and on commodities, each followed "
        "to the person who finally pays it; then the public debts, the sinking fund that "
        "does not sink, the pretended payment by lighter coin, and the question of "
        "what an empire costs."
    ),
    "blurb": (
        "Read the end of Smith's book with the arithmetic beside it. Price a crown estate "
        "at years' purchase, hold a land tax at its valuation while rents move, find the "
        "wage a tax on wages requires, compute what a duty yields until two and two "
        "make one, run a debt year by year through a war, and pay a debt in coin that "
        "has lost its silver."
    ),
    "key": [
        "price = yearly rent × years' purchase",
        "fixed valuation: tax stays, rent moves",
        "wage needed = old wage / (1 − rate)",
        "revenue = duty × quantity that pays it",
        "debt next year = debt + interest − payment",
        "silver paid = debt × new silver / old silver",
    ],
    "assumes_short": "The courses before it",
    "assumes_long": (
        "the twelve courses before it, and above all the account of wages in Wages and "
        "Profits, of rent in The Rent of Land, of the progress of the mercantile system "
        "in The Mercantile System and of what the sovereign must spend in The Expenses "
        "of the Sovereign; school arithmetic is enough for the figures"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of Book V's chapters on revenue and debt "
        "yourself, and say, in Smith's terms, who finally pays and what a figure is a "
        "figure of."
    ),
    "outcomes": [
        ("Price a rent",
         "Given a yearly rent and a rate of interest, compute the years' purchase and the "
         "price, and say what interest the price would redeem on a debt."),
        ("Test a tax against the maxims",
         "Given a valuation, a rate and a run of rents, compute a fixed land tax and its "
         "share of the rent each year, and say which of Smith's four maxims it passes "
         "and which it fails."),
        ("Say who finally pays",
         "For a tax on rent, on a house, on profit, on wages or on a commodity, follow the "
         "tax from the person who hands it over to the one who finally pays it, and "
         "work Smith's tithe, house and wage examples from the figures."),
        ("Find the wage a tax requires",
         "Compute the wage that leaves the labourer the same after a tax, the rise as a "
         "fraction of the old wage, and say why the rise exceeds the rate."),
        ("Compute what a duty yields",
         "Compute the revenue at each duty from the quantity that pays it, find where a "
         "higher duty brings in less, and say what Smith's necessaries and luxuries do "
         "to wages."),
        ("Follow a debt and a debasement",
         "Compute a debt year by year with a payment and new loans, and compute the "
         "metal owed and paid, and the creditor's loss, when the coin is lightened."),
    ],
    "syllabus_intro": (
        "The first four lessons read Chapter 2 from the sovereign's own funds to the taxes "
        "on rent, profit and wages; the fifth reads the taxes on commodities, and the last "
        "two read Chapter 3 on public debts and the end of the book."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Smith's words and "
        "then goes back through them. This is a read-along of Adam Smith, <em>An Inquiry "
        "into the Nature and Causes of the Wealth of Nations</em> (1776); quotations are from "
        "the public-domain Electronic Classics Series edition.",
        "Keep the money straight. Smith writes pounds, shillings and pence: twelve pence "
        "make a shilling and twenty shillings a pound, so four shillings in the pound is a "
        "fifth. Where a lab says a million it means pounds sterling, and where it says "
        "years' purchase it means years of a rent.",
        "Use the labs to move one thing at a time. A preset changes a rent, a rate or a "
        "duty against the one before, and the point is in what moves and what does not: a "
        "tax that stays fixed while rents rise, or a duty that doubles while its revenue "
        "halves.",
        "Keep the sum apart from the verdict. Smith's figures are his, of his century, "
        "and the labs show what his reasoning implies for them. Whether the reasoning "
        "describes any economy is what the book argues, and each lesson says where "
        "the strongest objections come from.",
    ],
    "not_covered": [
        "The catalogue of taxes. Smith reviews the land taxes of Prussia, Silesia, "
        "Milan and Bohemia, the French taille, and the duties of the excise and customs "
        "country by country. The lessons take the ones that carry the argument and "
        "say where the rest are skipped.",
        "The general mortgages of 1697 to 1717 and the annuities for lives. The "
        "chapter on debts lists each fund and each loan with its amount. The "
        "sinking-fund lesson uses his totals and leaves the list in the book.",
        "Modern public finance. Smith's maxims, his incidence reasoning and his argument "
        "about debt are read as he wrote them. Ricardo, Mill, George and the "
        "equivalence writers appear where they answer him, briefly and at their "
        "strongest, and a modern account of tax incidence is not attempted.",
        "The colonies in detail. The last lesson reads the plan for a union of the "
        "empire and the argument for giving it up, with his figures. The history of "
        "the American war and of what the colonies cost is for historians.",
        "Whether any figure describes an economy. The labs compute what Smith's reasoning "
        "implies for stated quantities. They do not say whether wages followed "
        "subsistence, whether funding destroyed capital, or whether a duty past its "
        "peak would have brought in more at a lower rate.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the rents, wages, "
        "duties, debts and coin weights a lesson states, in exact arithmetic, on Smith's "
        "reasoning. The figures are Smith's where a preset says so and written for the "
        "lesson where it says that, and no lab can tell you whether the reasoning "
        "describes any economy."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
