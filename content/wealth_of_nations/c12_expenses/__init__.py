"""Course 12 -- The Expenses of the Sovereign: Book V, Chapter 1.

Split across two lesson modules: part_a is the three duties' first stretches (defence,
justice, roads and tolls); part_b is the companies, the education of youth, and the
instruction of people of all ages with Part IV and the Conclusion.
"""

from . import part_a, part_b

COURSE = {
    "slug": "wealth-expenses-of-the-sovereign",
    "title": "The Expenses of the Sovereign",
    "level": "Intermediate",
    "summary": (
        "Book V, Chapter 1. What a sovereign has to pay for and who should pay it: the "
        "army, which costs nothing among shepherds and the most of all in a rich nation; "
        "the courts, once a source of revenue; roads and canals that can be charged to "
        "their users; the trading companies that built forts; the schools and the "
        "clergy; and the rule of who should bear each cost."
    ),
    "blurb": (
        "Read the chapter in which Smith turns from wealth to government. Compute how many "
        "soldiers a people can feed, what a judge earns from fees and from salary, who "
        "pays a toll by the ton, what a dividend is as a rate on stock, and what a "
        "teacher or a minister depends on his pupils or hearers for."
    ),
    "key": [
        "soldiers = population × share under arms",
        "toll = rate a ton × tons × trips",
        "income = salary + (pupils × fee)",
        "dividend rate = dividend / stock",
        "average living = revenue / ministers",
        "who benefits pays; else all, by ability",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no economics and no earlier course is assumed, and school arithmetic is enough; "
        "pounds, shillings and pence are explained in the second lesson"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of the chapter yourself and say, in "
        "Smith's terms, what each expense is for and who he thinks should pay it."
    ),
    "outcomes": [
        ("Price an army",
         "Compute the soldiers a population supports at a stated share and what they "
         "cost in a year, and say why Smith holds that the share must fall as a nation "
         "grows rich."),
        ("Split a judge's pay",
         "Compute an income from salary and from fees, the share that follows the "
         "work, and state Smith's case for fees paid to the judge only after the case "
         "is decided."),
        ("Charge a toll",
         "Compute what each carriage pays by weight and trips, and state why Smith "
         "thinks the consumer who pays it still gains and why he would not make it a "
         "general revenue."),
        ("Read a company's dividend",
         "Compute a dividend as a rate on stock, state the difference between a "
         "regulated and a joint-stock company, and give Smith's reason and his four "
         "exceptions."),
        ("Split a teacher's or a clergyman's living",
         "Compute an income from salary and from fees or offerings, and state what "
         "Smith says the public should and should not pay for in schooling."),
        ("Sort the chapter's expenses",
         "State who Smith says should pay for defence, justice, roads, local works and "
         "instruction, and where he leaves the choice open."),
    ],
    "syllabus_intro": (
        "Six lessons follow the chapter's three duties of the sovereign and its "
        "Conclusion: defence, justice, the works that help commerce, the companies "
        "that built forts for particular trades, and the two kinds of instruction."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Smith's words "
        "and then goes back through them a stage at a time. This is a read-along of "
        "Adam Smith, <em>An Inquiry into the Nature and Causes of the Wealth of "
        "Nations</em> (1776), and quotations are from the public-domain Electronic "
        "Classics Series edition (Pennsylvania State University, 2005).",
        "Expect a long chapter. Book V Chapter 1 runs to about four thousand lines of "
        "the book, and the lessons read some parts in outline: the history of the "
        "militia and the standing army, the lesser trading companies and the medieval "
        "church are summarised and left to the text, and each lesson says what it skips.",
        "Use the labs to change one figure at a time. Smith's own figures are used "
        "where he gives them, such as the Toulouse salary, the East India Company's "
        "dividends and the revenue of the church of Scotland, and a preset written for the "
        "lesson says so in its label. The money is pounds, shillings and pence: twelve "
        "pence to the shilling and twenty shillings to the pound.",
        "Keep the arithmetic apart from the verdict. Every figure is computed from "
        "what the lesson states. Whether Smith's reasoning describes any economy, then "
        "or now, is what the book argues and its critics dispute, and each lesson says "
        "where the strongest objections come from.",
    ],
    "not_covered": [
        "The history of the militia and the standing army in full. Part I carries pages "
        "of Greek, Roman and Carthaginian history as evidence. The lesson gives the "
        "argument and the figures and leaves the campaigns to the book.",
        "Smith's account of the university curriculum. Article II describes how the "
        "universities came to teach logic, ontology, pneumatology and a debased moral "
        "philosophy. The lesson reads it as part of the argument about endowments and "
        "does not follow it.",
        "The history of the medieval church. Article III's long middle runs from the "
        "wealth of the clergy to the Reformation. The lesson says what it argues and "
        "does not recount it.",
        "The lesser companies. The fines, statutes and dates for the Hamburgh, Russia, "
        "Eastland and Turkey companies, and most of the East India Company's "
        "political history, are summarised in a few lines.",
        "Anything about how the revenue is raised. This chapter says who should pay "
        "for what. Taxes, the funds of the sovereign and public debts are the next "
        "course.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the quantities a "
        "lesson states, Smith's own or written for the lesson, in exact arithmetic. It "
        "shows what the reasoning of the chapter implies for those quantities, and no lab "
        "can tell you whether that reasoning describes an economy."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
