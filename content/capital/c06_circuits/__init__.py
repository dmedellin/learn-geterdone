"""Course 6 -- The Circuits of Capital: Volume II, Part I, Chapters 1-6.

Six lessons, one per chapter, all in part_a.
"""

from . import part_a

COURSE = {
    "slug": "capital-circuits-of-capital",
    "title": "The Circuits of Capital",
    "level": "Intermediate",
    "summary": (
        "Volume II, Part I, The Metamorphoses of Capital and Their Circuits: Chapters 1 to 6. "
        "How one capital passes through the forms of money, means of production and product "
        "and back; what each of the three circuits it describes shows and hides; how a "
        "continuous business holds all three forms at once; and what the time and the costs "
        "of buying and selling add to value, which on Marx's account is nothing, with two "
        "exceptions."
    ),
    "blurb": (
        "Follow Marx's spinner and his £422 round the whole circuit, from money to yarn to "
        "more money. Compute the surplus value produced and the surplus value realised, "
        "restart production simply or on a larger scale, split the yarn into the parts that "
        "are and are not anyone's income, and price the weeks and the clerks that circulation "
        "costs."
    ),
    "key": [
        "I. M–C…P…C′–M′: money to more money",
        "II. P…C′–M′–C…P: production renewed",
        "III. C′–M′–C…P…C′: the whole product",
        "C′ = c + v + s; only v + s is income",
        "share in a form = its weeks / all weeks",
        "turnover = production + circulation",
        "s after costs = s − pure costs",
    ],
    "assumes_short": "Volume I",
    "assumes_long": (
        "the five courses on Volume I, from Commodities and Money to So-Called Primitive "
        "Accumulation, and above all the spinning mill and the rate of surplus value from From "
        "Money to Surplus Value"
    ),
    "outcomes_intro": (
        "By the end you can follow a capital through every form it takes and say, with Marx's "
        "figures, where its value grows and where it only changes shape."
    ),
    "outcomes": [
        ("Trace a circuit",
         "Given the money advanced, its split, the product's value and the share sold, give a "
         "capital's value as money, productive and commodity capital, and compute the surplus "
         "value produced and the surplus value realised."),
        ("Restart production",
         "Compute the productive capital that re-enters production under simple and enlarged "
         "reproduction, and the hoard held while surplus value is below the least sum that can "
         "be invested."),
        ("Split the product",
         "Divide a product, or any lot of it, into the units that replace constant capital, "
         "pay wages and carry surplus value, and say which of them is anyone's income."),
        ("Divide a continuous capital",
         "From the weeks spent in each stage, compute the share of a continuous capital held as "
         "money, productive and commodity capital at any moment."),
        ("Measure a turnover",
         "Compute the turnover time, the turnovers in a year and the share of the turnover spent "
         "in circulation, in which no value is produced."),
        ("Sort the costs of circulation",
         "Classify a cost as a pure cost of circulation or as a cost that adds value, and compute "
         "the surplus value left after the pure costs."),
    ],
    "syllabus_intro": (
        "Six lessons read the six chapters of Part I in order: the three circuits one at a time, "
        "the three together, and then the time and the costs of the circulation that joins them."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and then "
        "goes back through them a phrase at a time, so the passage is worth a second reading once "
        "the lesson is done. Quotations are from the Kerr editions in the Online Library of "
        "Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of book Volume II is. Marx did not finish it. He died in 1883, and "
        "Friedrich Engels assembled the volume from his manuscripts and published it in 1885; "
        "Marx had left the material, Engels wrote, for him &ldquo;to make something&rdquo; of. "
        "Part I draws on the last drafts Marx wrote, in 1877 and 1878, and on an earlier, more "
        "finished manuscript, and in places it reads like notes, repeated and unpolished. The "
        "lessons follow Engels' text and do not try to separate the two hands.",
        "Keep the spinner in view. Chapter 1 sets up £422 of capital, £372 of means of "
        "production and £50 of labour-power, making 10,000 lb of yarn worth £500, and the first "
        "three lessons use Marx's figures throughout. The last three need weeks and costs the "
        "chapters do not give; there the figures are illustrative, and each lesson says so.",
        "Keep the definitions apart from the verdict. Every figure is computed on Marx's "
        "definitions, and in particular on his claim that buying and selling add no value. "
        "Whether that line is drawn in the right place is argued over to this day, and the "
        "lessons say who argues the other side.",
    ],
    "not_covered": [
        "The difference between working time and production time, and the turnover of fixed and "
        "circulating capital. Chapter 5 introduces production time as longer than labour time; "
        "the arithmetic of both belongs to The Turnover of Capital, which reads Part II.",
        "Merchant's capital and the profit on it. Chapter 6 sets the merchant aside as a buying "
        "and selling agent; how merchants share in surplus value is Volume III's subject, in "
        "Merchant's Capital and Interest.",
        "Credit and credit money. Marx says Volume II reckons with metallic money and leaves "
        "credit aside, and these lessons do the same. Credit and Fictitious Capital takes it up.",
        "The equalisation of profits. Chapter 5 mentions that capitals with longer circulation "
        "times receive higher prices once profits are equalised. That needs prices of production, "
        "which come in Average Profit and Its Fall.",
        "The modern debate over productive and unproductive labour. Lesson 6 names where the "
        "dispute lies and who has argued it; it does not attempt to measure an economy on Marx's "
        "categories.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the sums, weeks and costs "
        "a lesson states, in exact arithmetic, on Marx's definitions. The spinner's figures are "
        "Marx's; the weeks and the costs are illustrative. No lab can tell you whether buying and "
        "selling really add nothing to value."
    ),
    "lessons": part_a.LESSONS,
}
