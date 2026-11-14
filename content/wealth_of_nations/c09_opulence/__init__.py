"""Course 9 -- The Progress of Opulence: Book III, Chapters 1 to 4.

One book, four lessons, one chapter each; part_a holds all four. Book III is a
history, and each lesson reads its chapter in outline where the narrative runs
long, saying what it leaves out.
"""

from . import part_a

COURSE = {
    "slug": "wealth-progress-of-opulence",
    "title": "The Progress of Opulence",
    "level": "Beginner",
    "summary": (
        "Book III, Of the Different Progress of Opulence in Different Nations: Chapters 1 "
        "to 4. The natural order in which a society's capital goes to agriculture, "
        "manufactures and foreign commerce; why the great estates of post-Roman Europe "
        "and the tenures of those who worked them discouraged improvement; how the towns "
        "got liberty and good government first; and how the commerce of towns, "
        "unintended, loosened the great lords' hold on the country."
    ),
    "blurb": (
        "Read Smith's history of how Europe got its economy, with the arithmetic beside "
        "it. Work what a farmer and a weaver gain by trading, whether an improvement pays "
        "the slave, the metayer or the farmer who must make it, what a fixed farm of a "
        "town's dues gives up as the town grows, and how a lord's spending turns "
        "retainers into customers."
    ),
    "key": [
        "alone: hours / (a + b) of each good",
        "keep to the good that costs you less",
        "gain = share × added × years − cost borne",
        "farm / dues falls as the dues grow",
        "a share of 1 is wholly the lord's man",
        "capital goes land, then works, then trade",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no economics and no earlier course is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Book III yourself and say, in Smith's "
        "terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Work the gain from an exchange",
         "Compute what two producers make alone and after each keeps to the good that "
         "costs him less, and the gain in each good."),
        ("State the natural order of capital",
         "Say in what order Smith says a growing society's capital goes to agriculture, "
         "manufactures and foreign commerce, why, and in what sense Europe inverted it."),
        ("Test whether an occupier would improve",
         "Given an improvement's cost and yearly return, the term, and an occupier's shares "
         "of the produce and the cost, compute his gain and the term that just repays him."),
        ("Price a rent certain",
         "Compute a fixed yearly sum as a share of a yield that grows or falls, and what "
         "the party who let it gives up or bears."),
        ("Measure a dependence",
         "Compute what a spender's purchases pay each maker as a share of a year's "
         "maintenance, and say whether anyone is wholly dependent on him."),
        ("Place Book III in its argument",
         "Say how Book III's history sets up the two systems of political economy of "
         "Book IV, and where Smith says Europe departed from the natural order."),
    ],
    "syllabus_intro": (
        "Four lessons, one for each chapter of the book: the natural order, the "
        "great estates and their tenants, the rise of the towns, and what the towns "
        "did for the country."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson goes through Smith's words a "
        "phrase at a time, so the passage is worth a second reading once the lesson is done. "
        "This is a read-along of Adam Smith, <em>An Inquiry into the Nature and Causes of "
        "the Wealth of Nations</em> (1776); quotations are from the public-domain Electronic "
        "Classics Series edition.",
        "Book III is history, and the lessons read it in outline. Chapters 2 and 3 tell "
        "long stories of conquest, law, church and city that the lessons leave out; each "
        "says what it skips, and the whole text is worth a slow reading on its own.",
        "Money is in pounds, shillings and pence, as Smith writes it: twelve pence to the "
        "shilling and twenty shillings to the pound. Notice whose figures a preset uses. One "
        "labelled with Smith's name uses a figure he states in the chapter; one labelled as "
        "written for the lesson is an invention to show a method, and Smith never says it.",
        "Keep the definitions apart from the verdict. Every figure is computed from the "
        "reasoning the chapter gives. Whether it describes how any economy worked, then or "
        "now, is what the book and its critics argue about, and each lesson says where the "
        "standard objection comes from.",
    ],
    "not_covered": [
        "The history of the conquest of the Roman provinces, of the feudal law and of the "
        "church's part in ending slavery. Smith's narrative is long and learned; the "
        "lessons read the economics inside it and leave the rest for the text.",
        "The cities of Italy, Germany and the Hanse in detail. Chapter 3 tells how each "
        "won its liberty; the lesson follows one thread, the farm of the town, and the "
        "rest is in the chapter.",
        "Whether Smith's natural order is history. Economic historians since have "
        "disputed how far long-distance trade and towns came before the cultivation of "
        "the land, and the lessons say so where the dispute bears; no lab decides it.",
        "The Book IV account of the restraints on corn and on commerce that Smith says "
        "have worked against the natural order. They are the next course's subject.",
        "Slavery. Smith's arguments about its cost and about where it can pay appear in "
        "Chapter 2 in a few pages; the lessons report them and the later debate in a "
        "sentence, and they are not a history of slavery.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the hours, costs "
        "and revenues a lesson states, in exact arithmetic, on Smith's reasoning. The "
        "figures are illustrative except where a preset says it uses Smith's, and no lab "
        "can tell you whether Europe's order of growth was the one he describes."
    ),
    "lessons": part_a.LESSONS,
}
