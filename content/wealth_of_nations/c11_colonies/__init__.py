"""Course 11 -- Colonies and the Agricultural Systems: Book IV, Chapters 7 to 9 and the Appendix.

One module of five lessons: part_a is Chapter 7 in its three Parts, Chapter 8,
and Chapter 9 with the Appendix.
"""

from . import part_a

COURSE = {
    "slug": "wealth-colonies-and-agricultural-systems",
    "title": "Colonies and the Agricultural Systems",
    "level": "Intermediate",
    "summary": (
        "Book IV, Chapters 7 to 9 and the Appendix. Why Europeans settled America and "
        "what Smith thinks of the search for gold, why new colonies grew so fast, what "
        "the monopoly of the colony trade cost the country that held it, how the "
        "mercantile system ends in the sacrifice of the consumer, and the French "
        "economists' rival system with its net product, answered and set aside for the "
        "simple system of natural liberty."
    ),
    "blurb": (
        "Read the longest chapter of the book, on colonies, in its three Parts, then its "
        "conclusion and the system that set land against trade. Work out whether a "
        "mining lottery repays its tickets, what a doubling every twenty-five years "
        "comes to, how much labour a thousand pounds keeps at work when it comes home "
        "once in five years, what a bounty costs the treasury and the buyers, and which "
        "class shows a net product."
    ),
    "key": [
        "chance of a prize = winners / entrants",
        "population after = start × 2ⁿ doublings",
        "work kept up = capital × returns a year",
        "bounty cost = treasury + home buyers",
        "net product = produce − consumption − advances",
        "consumption is the sole end of production",
    ],
    "assumes_short": "Courses 1 to 10",
    "assumes_long": (
        "school arithmetic and the earlier courses help: the lessons on wages and "
        "profit, on a capital's returns in Book II, and on bounties and the mercantile "
        "system in Book IV, Chapters 1 to 6, are all used here"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic on Smith's pages in these chapters and say, "
        "in his terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Judge a lottery",
         "Given entrants, winners, a prize, years and the cost of a ticket, compute "
         "whether the prizes repay the tickets and the prize that would, and say why "
         "Smith calls the search for mines the most disadvantageous lottery in the world."),
        ("Compute a doubling",
         "Compute the doublings and the population after a stated time at Smith's "
         "twenty or twenty-five years, and say what land and liberty did in his account "
         "of the colonies."),
        ("Compare trades by their returns",
         "Compute the labour a capital keeps at work from how often it returns, rank "
         "trades with different returns, and say why a merchant's profit is not the "
         "country's gain."),
        ("Cost a bounty",
         "Compute what a bounty costs the treasury and the home buyers and say who "
         "pays, using Smith's maxim that consumption is the sole end of production."),
        ("Find a net product",
         "Compute a class's net product from its produce, consumption and advances and "
         "say why the economists called a class barren and why Smith refused the word."),
        ("State the system of natural liberty",
         "Give the sovereign's three duties as Smith lists them at the end of Chapter 9 "
         "and say what he thinks the sovereign is relieved of."),
    ],
    "syllabus_intro": (
        "Three lessons read the three Parts of Chapter 7, one reads Chapter 8, and one "
        "reads Chapter 9 with the Appendix."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Smith's words "
        "and then goes back through them a phrase at a time. This course is a "
        "read-along of Adam Smith, <em>An Inquiry into the Nature and Causes of the "
        "Wealth of Nations</em> (1776); quotations are from the public-domain "
        "Electronic Classics Series edition (Pennsylvania State University, 2005).",
        "Expect Chapter 7 to be long. It runs to about three thousand lines, and the "
        "lessons read each Part whole and say at the start what they read only in "
        "outline. Smith writes in these chapters about slavery and about the people "
        "of the Americas and the East Indies, and the lessons report what he says in "
        "his words, without softening it and without adding to it.",
        "Use the labs to change one figure at a time. Money is in pounds, shillings and "
        "pence, at twelve pence to the shilling and twenty shillings to the pound. "
        "Smith's own figures are labelled as his, and figures written for the lesson "
        "are labelled as that.",
        "Keep the arithmetic apart from the verdict. Every figure shows what the "
        "reasoning of the chapter implies for the quantities stated. Whether the "
        "reasoning describes any economy, then or now, is what the book argues and "
        "what its critics dispute, and each lesson says where they stand.",
    ],
    "not_covered": [
        "The colony-by-colony histories of Chapter 7. Smith's accounts of the Dutch, "
        "Danish, Swedish, French, Portuguese and Spanish colonies, and his lists of "
        "enumerated commodities and duties, are read in outline.",
        "The East India companies. The last pages of Chapter 7 describe the Dutch and "
        "English companies and their servants in Bengal and the Moluccas; they are "
        "reported in a paragraph, and no lab computes them.",
        "Taxing the colonies and the proposal of a union. Smith's pages on requisition, "
        "representation and the quarrel of 1775 are summarised, because the course "
        "cannot follow what happened after his book was printed.",
        "The detailed statutes of Chapter 8: the seven bounties on imported materials, "
        "the dyeing drugs, gum senega and beaver skins. The wool laws are read in full.",
        "The Economical Table. The edition used here does not print Quesnay's table, "
        "and the course does not supply one: the figures in the net-product lab are "
        "written for the lesson.",
        "The herring bounty accounts of the Appendix. They belong to Chapter 5 and are "
        "pointed to, with a note that their printed totals do not agree with the rows.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the quantities a "
        "lesson states, Smith's own or written for the lesson, in exact arithmetic. "
        "They show what the reasoning of the chapter implies for those quantities; "
        "whether it describes any economy, then or now, is what the book argues and "
        "its critics dispute, and no lab can settle it."
    ),
    "lessons": part_a.LESSONS,
}
