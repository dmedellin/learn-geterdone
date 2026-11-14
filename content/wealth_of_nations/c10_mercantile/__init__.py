"""Course 10 -- The Mercantile System: Book IV, Chapters 1-6.

Split across two lesson modules: part_a is Chapters 1 to 3 (the principle of the
system, the restraints on importation, and the balance of trade with the Digression
on Banks of Deposit); part_b is Chapters 4 to 6 (drawbacks, bounties with the
Digression on the Corn Trade, and treaties of commerce).
"""

from . import part_a, part_b

COURSE = {
    "slug": "wealth-mercantile-system",
    "title": "The Mercantile System",
    "level": "Intermediate",
    "summary": (
        "Book IV, Chapters 1 to 6. Smith's account of the commercial or mercantile "
        "system: the belief that wealth is money, the restraints on importation that "
        "follow from it, the doctrine of the balance of trade, and the encouragements to "
        "exportation by drawback, bounty and treaty. Each is read for what it does to "
        "the annual produce of a country, and the lessons say who has argued against "
        "Smith and why."
    ),
    "blurb": (
        "Read Smith's case against the restraints of trade, and his cases for them, in "
        "his own words. Compute a balance of trade country by country and see how little "
        "it says, compare the cost of making at home with the cost of buying, work out "
        "who pays for a drawback, a corn bounty and a preference in a treaty, and meet "
        "the one use of the phrase 'invisible hand' in the book."
    ),
    "key": [
        "partner's balance = exports − imports",
        "buy abroad when it costs less than at home",
        "duty kept = duty paid − duty drawn back",
        "bounty cost = bounty × units exported",
        "home tax = price rise × units sold at home",
        "a preference lowers one seller's duty only",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no economics and no earlier course is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Book IV, Chapters 1 to 6, yourself and "
        "say what each figure is a figure of, in Smith's terms and in the terms of those "
        "who disagreed with him."
    ),
    "outcomes": [
        ("Say what the mercantile system took wealth to be",
         "State the belief that wealth is money, the two arguments Smith finds in it that "
         "are partly solid, and the replies he gives from the supply of gold, the use of "
         "money and the cost of a war."),
        ("Compare making with buying",
         "Given what a good costs to make at home and to buy abroad with its duty, say "
         "which is cheaper, what a prohibition costs a year, and what Smith's two cases "
         "for a restraint and his case against retaliation add."),
        ("Compute a balance of trade and say what it leaves out",
         "Compute the balance of trade country by country, show that a favourable balance "
         "and a gain to the country are different things, and say why Smith rejects the "
         "course of exchange and the custom-house books as measures of it."),
        ("Work out who pays for a drawback",
         "Compute the duty paid, drawn back and kept on goods exported again, and say why "
         "Smith counts a drawback among the reasonable encouragements."),
        ("Count the two taxes of a bounty",
         "Compute the cost of an export bounty to the treasury and to home buyers from "
         "its size, the quantity exported and the rise in the home price, and say what "
         "Smith adds about the corn trade."),
        ("Read a preference in a treaty",
         "Compute what a preferential duty does to the price of the favoured and the "
         "unfavoured good, say who gains and who pays, and put Smith's reading of the "
         "Methuen treaty beside Ricardo's later reading."),
    ],
    "syllabus_intro": (
        "Six lessons follow the six chapters. The first states the system and answers its "
        "central belief, the second takes up restraints on importation and Smith's one use "
        "of the invisible hand, the third the balance of trade and the banks of deposit, "
        "and the last three the encouragements to exportation: drawbacks, bounties and "
        "treaties."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Smith's words and "
        "then goes back through them a phrase at a time. This is a read-along of Adam "
        "Smith, <em>An Inquiry into the Nature and Causes of the Wealth of Nations</em> "
        "(1776), quoted from the public-domain Electronic Classics Series edition "
        "(Pennsylvania State University, 2005).",
        "Money is in pounds, shillings and pence. There are 12 pence in a shilling and 20 "
        "shillings in a pound, and a quarter of corn is eight bushels. The lessons say "
        "so again where a figure needs it.",
        "Use the labs to change one thing at a time. Each preset says whether its figures "
        "are Smith's or were written for the lesson, and the difference matters: Smith's "
        "figures are his, often second-hand, and a lab only shows what his reasoning "
        "implies for them.",
        "Keep the arithmetic apart from the verdict. A lab computes what the chapter's "
        "reasoning implies for stated quantities. Whether the reasoning describes the "
        "economy of any time is what the book argues and its critics dispute, and every "
        "lesson says where the strongest objection comes from.",
    ],
    "not_covered": [
        "The history of the corn laws. The Digression concerning the Corn Trade is read "
        "in outline: its four trades, its two figures, and its case about the inland "
        "dealer. The long account of the statutes from Edward VI to the thirteenth year "
        "of George III, and the table of duties, are in the book.",
        "The herring bounty accounts. Chapter 5 states them in part and the Appendix at "
        "the end of Book IV gives the full accounts; the Agricultural Systems lesson of "
        "the next course points to the Appendix.",
        "The Navigation Act's clauses in detail, and the French tariffs of Colbert. The "
        "lessons give the clauses Smith relies on and the dates he gives, and no more.",
        "The theory of exchange rates. Smith's account of the course of exchange, the "
        "computed and the real par, is read for what it says about the balance of trade; "
        "the lab does not compute an exchange.",
        "Whether the doctrine of a favourable balance was ever the whole of the mercantile "
        "writers' view. Smith presents a system; historians of earlier economic writing "
        "have found a good deal more variety in Mun, Misselden, Child and the others "
        "than he reports, and the lessons say so where it matters but do not survey them.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the quantities a "
        "lesson states, in exact arithmetic, on Smith's reasoning. Where a preset uses "
        "Smith's own figures it says so, and the other figures were written for the "
        "lesson. No lab can tell you whether the reasoning describes any economy, then "
        "or now."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
