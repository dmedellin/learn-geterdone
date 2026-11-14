"""Course 8 -- Accumulation and the Employments of Capital: Book II, Chapters 3-5.

Five lessons, all in part_a: productive and unproductive labour and parsimony and the
prodigal (Chapter 3, in two), stock lent at interest (Chapter 4), and the four ways of
employing capital and the three branches of trade (Chapter 5, in two).
"""

from . import part_a

COURSE = {
    "slug": "wealth-accumulation",
    "title": "Accumulation and the Employments of Capital",
    "level": "Intermediate",
    "summary": (
        "Book II, Chapters 3 to 5. Which labour adds to a nation's stock and which "
        "only uses it up, why capital grows by saving and shrinks by prodigality, what "
        "lending at interest transfers, and how Smith ranks the four employments of a "
        "capital and the home, foreign and carrying trades by the labour each sets "
        "in motion."
    ),
    "blurb": (
        "Follow a capital year by year as it grows by what is saved and shrinks by "
        "what is spent, price land in years' purchase, and count the labour that "
        "equal capitals put in motion in the farm, the factory, the warehouse and the "
        "shop. Each step is Smith's argument worked in numbers, with the objections "
        "of the people who came after him."
    ),
    "key": [
        "capital replaces itself; revenue is spent",
        "capital next year = capital + saved revenue",
        "price of land = rent × years' purchase",
        "years' purchase = 100 / rate of interest",
        "labour set going = capital × returns / wage",
        "home trade: quick returns, two replaced",
    ],
    "assumes_short": "Course 7, in outline",
    "assumes_long": (
        "no economics beyond what the earlier courses give, and school arithmetic is "
        "enough: the lessons use compound growth for a few years and percentages, and "
        "work each figure out in the lesson"
    ),
    "outcomes_intro": (
        "By the end you can follow Smith's account of how a nation's capital grows and "
        "where it is employed, work the sums that sit under it, and say what each "
        "sum does not show."
    ),
    "outcomes": [
        ("Separate productive from unproductive labour",
         "State Smith's test, that labour is productive if it fixes and realises itself in "
         "something that lasts and can later set an equal quantity of labour to work, and "
         "say which of two stated hands it makes productive."),
        ("Compute a capital under saving and spending",
         "Compute a capital year by year from its return and the share of the return "
         "saved, for a frugal path and a prodigal one, and the labour it maintains at "
         "a stated wage."),
        ("Price land and a loan",
         "Compute the years' purchase and the price of an estate from its rent and the "
         "rate of interest, and say what a loan hands over, in Smith's terms, and why "
         "the rate falls as stock grows."),
        ("Rank employments by the labour they set going",
         "Compute the labour that equal capitals put in motion in each of Smith's four "
         "employments from stated wage shares, and say what the ranking depends on."),
        ("Compare the home, foreign and carrying trades",
         "Compute the multiple by which a home-trade capital outworks a foreign-trade "
         "capital from the returns a year and the number of home capitals replaced, and "
         "state the policy Smith draws from it."),
    ],
    "syllabus_intro": (
        "Five lessons follow Book II to its end: the labour that adds to the stock, "
        "the saving that makes it grow, the loan that hands it to another, and the "
        "two lessons on where a capital does the most good."
    ),
    "how_to": [
        "Read the passage before the explanation. Each lesson opens on Smith's own words "
        "and then goes back through them. This course is a read-along of Adam Smith, "
        "<em>An Inquiry into the Nature and Causes of the Wealth of Nations</em> (1776); "
        "quotations are from the public-domain Electronic Classics Series edition "
        "(Pennsylvania State University, 2005), and Smith's spelling is kept inside them.",
        "Money is in pounds, shillings and pence, as Smith has it: twelve pence to the "
        "shilling and twenty shillings to the pound. Most sums here are in pounds, and a "
        "lesson says when a figure is Smith's own and when it is written for the "
        "lesson.",
        "Use the labs to change one thing at a time. Each preset moves a single "
        "quantity against the one before it: the share saved, the rate of interest, the "
        "number of returns in a year. The point of a lesson is in what moves and what "
        "does not.",
        "Keep the arithmetic apart from the verdict. Every figure shows what Smith's "
        "reasoning implies for the quantities stated. Whether the reasoning describes the "
        "economy of his century or of ours is what the book argues and its critics "
        "dispute, and each lesson says who disputes it.",
    ],
    "not_covered": [
        "The war debt. Smith counts what the four French wars added to the national debt "
        "in Chapter 3, and the lessons use the sum as an example only; the debt is the "
        "subject of the last course in this Subject, <em>Taxes and Public Debts</em>.",
        "The agricultural system and the Physiocrats. Smith says in a note that some French "
        "authors use productive and unproductive in another sense, and keeps his answer for "
        "Book IV, Chapter 9. This course states the note and does not go further.",
        "Foreign trade and the balance of trade. Chapter 5 ranks the trades by the labour "
        "they employ and says the carrying trade is a symptom of wealth. The case for and "
        "against free trade is Book IV's, and the lessons here only say where Smith "
        "turns to it.",
        "Modern accounts of output and saving. Smith's productive labour is not the "
        "measure used in national accounts today, and no lab here converts between them.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the capitals, "
        "returns, rates and wages a lesson states, in exact arithmetic, on Smith's "
        "definitions. Some figures are Smith's and say so; the rest are written for the "
        "lesson. No lab can tell you whether the economy behaves the way the chapters say "
        "it does."
    ),
    "lessons": part_a.LESSONS,
}
