"""Course 7 -- The Turnover of Capital: Volume II, Part II, Chapters 7-17.

Split across two lesson modules: part_a is Chapters 7 to 12 (turnover, fixed
and circulating capital, the economists' theories of them, the working
period); part_b is Chapters 13 to 17 (the time of production and of
circulation, the capital advanced, the variable capital's turnover and the
circulation of surplus value).
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-turnover-of-capital",
    "title": "The Turnover of Capital",
    "level": "Intermediate",
    "summary": (
        "Volume II, Part II, The Turnover of Capital: Chapters 7 to 17. How often a "
        "capital goes round its circuit and why that matters: the year as the unit of "
        "turnover, fixed and circulating capital and the confusion of that distinction "
        "with constant and variable capital, the working period, the time of production "
        "and of circulation, the extra capital a continuous business must advance, the "
        "annual rate of surplus value, and where the money comes from to realise surplus "
        "value at all."
    ),
    "blurb": (
        "Follow a capital round its circuit with a stopwatch. Count turnovers a year, "
        "compute what a machine passes on by wear, total the turnover of a capital with "
        "fixed and circulating parts, sort the same capital two ways, and compute the "
        "additional capital, the annual rate of surplus value and the money that realises "
        "it."
    ),
    "key": [
        "turnover = production + circulation",
        "turnovers a year  n = T / t",
        "wear a year = fixed value / life",
        "turned over = wear + circulating · n",
        "fixed and circulating ≠ constant and variable",
        "capital II = circulation · weekly outlay",
        "annual rate  S′ = s′ · n",
        "s realised by what capitalists spend to live",
    ],
    "assumes_short": "The Circuits of Capital",
    "assumes_long": (
        "the three circuits of capital from The Circuits of Capital, and constant and "
        "variable capital and the rate of surplus value from From Money to Surplus Value"
    ),
    "outcomes_intro": (
        "By the end you can time a capital's circuit, say which of its parts return "
        "quickly and which slowly, and compute what that does to the capital a business "
        "must advance and to the surplus value it shows for a year."
    ),
    "outcomes": [
        ("Count turnovers",
         "Compute the turnover time from the times of production and circulation, the "
         "number of turnovers a year, and the value turned over on a given capital "
         "advanced, including the case where a working period is only part of the "
         "production time."),
        ("Compute what fixed capital transfers",
         "Compute the value a fixed capital passes to the product each year, the value "
         "still locked in it after so many years, and the effect of repairs and of a "
         "cheaper machine of the same kind."),
        ("Total the turnover of a whole capital",
         "Combine the wear of fixed capital with the turnovers of circulating capital to "
         "compute the value turned over in a year and the turnovers of the whole capital "
         "advanced."),
        ("Classify a capital twice",
         "Sort the same items as fixed or circulating and as constant or variable, and "
         "compute which of the two classifications fixes the surplus value produced."),
        ("Compute the capital advanced",
         "Compute the capital a continuous business needs when its working period and "
         "circulation period differ, the capital set free at the close of each working "
         "period, and the annual rate and mass of surplus value."),
        ("Account for the money that realises surplus value",
         "Compute the money a capitalist class must spend on its own consumption for the "
         "surplus value in its product to come back to it as money."),
    ],
    "syllabus_intro": (
        "One lesson for each of the eleven chapters of Part II, in Marx's order: the "
        "measure of turnover, the two kinds of productive capital and the theories of "
        "them, the three times that make up a turnover, and then what turnover does to "
        "the capital advanced and to surplus value."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with the chapter's "
        "own words and then goes back through them a phrase at a time. Quotations are "
        "from the Kerr editions in the Online Library of Liberty, hosted by Liberty Fund, "
        "Inc.",
        "Remember whose book this is. Volume II was put together by Engels from Marx's "
        "manuscripts after Marx died, and Part II shows it more than most: Chapter 15 "
        "carries a note in which Engels says he kept only the figures that were "
        "arithmetically correct. Where a lesson leans on a passage Engels shaped, it says "
        "so.",
        "Keep a clock beside the ledger. Volume I counted value in hours and shillings; "
        "this course adds weeks and years. Every lab here asks how long a sum of money is "
        "away from its owner before it comes back, and the arithmetic is mostly division "
        "by time.",
        "Keep the definitions apart from the verdict. Every figure is computed from the "
        "chapter's definitions. Whether the turnover of capital explains the trade cycle, "
        "or whether the classical economists were as confused as Marx says, is argued "
        "elsewhere, and each lesson says where the strongest objection comes from.",
    ],
    "not_covered": [
        "Credit. Part II assumes, again and again, that the capitalist works with his own "
        "money, and so do the labs. How credit shortens or replaces the advances computed "
        "here is Volume III's subject, in Credit and Fictitious Capital.",
        "The rate of profit. Chapter 16's annual rate of surplus value is the step before "
        "the annual rate of profit, and Ricardo's fixed and circulating capital matter "
        "most where profits are equalised. Both are Volume III's business, in Cost Price "
        "and the Rate of Profit and Average Profit and Its Fall.",
        "Turnover from the point of view of the whole society. Chapter 16's third section "
        "and Chapter 17's second turn towards the social capital and its reproduction. "
        "The balance between departments that this requires is the next course, "
        "Reproduction of the Social Capital.",
        "The business-cycle literature. Marx suggests that the ten-year life of fixed "
        "capital gives the trade cycle a material basis. Whether it does is argued with "
        "data on investment and crises that this path does not carry.",
        "Engels' reconstruction of Chapter 15. The lab computes the capital set free by "
        "the rule Marx states in the chapter's conclusions; it does not reproduce Marx's "
        "abandoned tables, and it takes no side on Engels' view that the release of money "
        "capital matters less than Marx thought.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the weeks, years "
        "and sums a lesson states, in exact arithmetic, on the definitions of Part II. "
        "Marx's own figures are labelled as his; the rest are illustrative, and no lab "
        "can tell you whether turnover explains anything in an actual economy."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
