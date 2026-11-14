"""Course 1 -- The Division of Labour: the Introduction and Book I, Chapters 1-3.

One lesson module: part_a is the Introduction and the three chapters, one lesson each.
"""

from . import part_a

COURSE = {
    "slug": "wealth-division-of-labour",
    "title": "The Division of Labour",
    "level": "Beginner",
    "summary": (
        "The Introduction and Book I, Chapters 1 to 3. What makes a nation well "
        "supplied, why dividing the work multiplies what each worker makes, what makes "
        "people divide it, and what limits how far it can go: the pin factory, the "
        "butcher, the brewer and the baker, the Highland nailer and the ship against the "
        "waggon."
    ),
    "blurb": (
        "Start where Smith starts. Compute a nation's produce per head from its "
        "workers and their skill, work the pin factory's multiple from his own "
        "figures, count what two producers gain by keeping to one trade, and count "
        "how many specialists a market can keep."
    ),
    "key": [
        "produce per head = share at work × output",
        "multiple = divided output / output alone",
        "specialised total − self-sufficient total",
        "specialists = whole units of demand/output",
        "division limited by the extent of the market",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no economics and no earlier course is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Smith's first three chapters yourself "
        "and say what each figure is a figure of."
    ),
    "outcomes": [
        ("Compute a nation's supply per head",
         "From a population, the number at useful labour and the output of each, compute "
         "the produce and the produce per head, and say which of Smith's two "
         "circumstances accounts for a difference between two nations."),
        ("Work the pin factory",
         "Compute each worker's share of a team's output and the multiple over what he "
         "could make alone, on Smith's bounds, and name the three causes he gives."),
        ("Say what the division rests on",
         "State, in Smith's terms, why people divide their work, and compute what two "
         "producers gain by each keeping to the good in which his relative cost is lower."),
        ("Count the specialists a market can keep",
         "From a place's yearly demand and one specialist's yearly output, compute the "
         "share of a year a trade would have there and the number of whole specialists."),
        ("Read a limit as Smith states it",
         "Say why Smith thinks the division of labour is limited by the extent of the "
         "market, and use his wagon and ship figures to say what water carriage does to "
         "that limit."),
    ],
    "syllabus_intro": (
        "One lesson reads the Introduction, and one reads each of the first three "
        "chapters of Book I: the division itself, its source in exchange, and its limit."
    ),
    "how_to": [
        "This Subject is a read-along of Adam Smith, <em>An Inquiry into the Nature and "
        "Causes of the Wealth of Nations</em> (1776). Every lesson quotes the passage it "
        "reads from the public-domain Electronic Classics Series edition (Pennsylvania "
        "State University, 2005), which prints the text of the later editions, and "
        "keeps Smith's spelling inside the quotations. A copy of the book is welcome but "
        "not needed.",
        "Read the passage before the explanation. Each lesson quotes Smith first and then "
        "goes back through him a phrase at a time, so the passage is worth a second "
        "reading once the lesson is done.",
        "Use the labs to change one thing at a time. Each preset changes a single figure "
        "against the one before, the output of a worker, the hours of a hunter, the "
        "demand of a place, and the point of the lesson is in what moves and what does "
        "not. A preset labelled with Smith's name uses his figures; a preset marked "
        "<em>written for this lesson</em> uses figures invented to show the "
        "reasoning.",
        "Keep what the chapter reasons apart from what it describes. Every figure is "
        "computed from the quantities a lesson states, and shows what Smith's reasoning "
        "implies for them. Whether it describes any economy is what the book argues, "
        "and each lesson says where the strongest objections come from.",
    ],
    "not_covered": [
        "The history of the idea. Others wrote about the division of labour before Smith, "
        "and the lessons mention them only where they bear on a chapter, as the "
        "Encyclopédie's article on pins does. No history of the idea is attempted.",
        "What the division does to the worker. Smith raises it only in Book V, and "
        "Marx makes it central to Volume I of Capital. This course says where and "
        "does not argue it.",
        "Modern accounts of specialisation. Ricardo's rule of comparative cost appears "
        "once, where it is the lab's rule, and Allyn Young's point that the division "
        "also enlarges the market appears once, in the last lesson. Neither is "
        "developed.",
        "The long geography of Chapter 3. Egypt, Bengal, China, Africa and the Danube "
        "are read in outline, because the argument they illustrate is the one the "
        "Highland nailer and the ship already make.",
        "The survey of agriculture and of the corn trade at the end of Chapter 1, beyond "
        "what the second lesson needs. The prices of corn in Poland, France and England "
        "are not worked.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the quantities a "
        "lesson states, in exact arithmetic. Where a preset says it is Smith's, the "
        "figures are his, and the lessons give the line of the text. Every other figure "
        "is written for the lesson, and no lab can tell you whether the division of "
        "labour explains the wealth of any actual nation."
    ),
    "lessons": part_a.LESSONS,
}
