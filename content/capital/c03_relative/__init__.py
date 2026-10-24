"""Course 3 -- Relative Surplus Value: Volume I, Parts IV and V, Chapters 12-18.

Split across two lesson modules: part_a is Chapters 12 to 14 and the first two
lessons on Chapter 15; part_b is the third lesson on Chapter 15 and Part V,
Chapters 16 to 18.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-relative-surplus-value",
    "title": "Relative Surplus Value",
    "level": "Intermediate",
    "summary": (
        "Volume I, Part IV, Production of Relative Surplus-Value, and Part V, The "
        "Production of Absolute and of Relative Surplus-Value: Chapters 12 to 18. How "
        "surplus labour grows in a day that cannot be lengthened, through co-operation, "
        "the division of labour in manufacture and machinery; what machinery adds to "
        "value, does to the worker and leaves of the promise of compensation; and how "
        "length, intensity and productivity together set the rate of surplus value."
    ),
    "blurb": (
        "Follow capital from the crowded workshop to the factory with the arithmetic "
        "beside it. Compute relative and extra surplus value, what shared tools save, the "
        "proportions of a manufacture, a machine's two tests for adoption, the labour in "
        "a denser hour and the capital a machine fails to set free, then run Marx's cases "
        "for the working day and his two formulae for the rate."
    ),
    "key": [
        "relative s: necessary time cut, day fixed",
        "pioneer's extra = day × (productivity − 1)",
        "detail workers ∝ 1 / rate of their step",
        "machine adopted if cost < wages displaced",
        "labour spent = hours × intensity",
        "s/v has no ceiling; s/(v + s) < 1",
    ],
    "assumes_short": "From Money to Surplus Value",
    "assumes_long": (
        "the value of Commodities and Money and the surplus value of From Money to Surplus "
        "Value, above all the rate of surplus value and the working day divided into "
        "necessary and surplus labour"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of Parts IV and V yourself and say, in "
        "Marx's terms, which part of the working day each figure moves."
    ),
    "outcomes": [
        ("Compute relative surplus value",
         "Given a working day and a rise in productivity in the industries that make the "
         "necessaries, compute the new rate of surplus value, and a pioneer's extra "
         "surplus value before competition removes it."),
        ("Count what combination saves",
         "Compute the constant capital per unit when means of production are shared, the "
         "combined working day, and the workers each step of a manufacture needs."),
        ("Test a machine",
         "Compute the value a machine adds per unit and decide whether it passes "
         "society's test and the capitalist's, and the capital it sets free when it "
         "displaces workers."),
        ("Weigh length against intensity",
         "Compute the labour in a day of given length and intensity, and the rate of "
         "surplus value when a shorter day is worked more densely."),
        ("Run the three factors",
         "Classify a change in the day as absolute or relative, and compute the value of "
         "labour-power and the rate when length, intensity and productivity vary alone or "
         "together."),
        ("Read the rate two ways",
         "Compute surplus over necessary labour and surplus over the whole day for the "
         "same day, and convert one into the other."),
    ],
    "syllabus_intro": (
        "One lesson reads each of Chapters 12, 13 and 14, three lessons read the long "
        "Chapter 15 on machinery, and three read the chapters of Part V, which look back "
        "over the whole working day."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words "
        "and then goes back through them a phrase at a time. Quotations are from the Kerr "
        "editions in the Online Library of Liberty, hosted by Liberty Fund, Inc.",
        "Expect Chapter 15 to be long and mostly history. Its figures come from factory "
        "inspectors' reports and parliamentary evidence, and the three lessons on it take "
        "one argument each: what a machine adds to value, what it does to the hours and "
        "intensity of work, and what becomes of the workers it displaces.",
        "Use the labs to change one thing at a time. Each preset changes a single figure "
        "against the one before, a necessary hour, a step's rate, a wage bill, the length "
        "of the day, and the point of the lesson is in which part of the day moves.",
        "Keep the definitions apart from the verdict. Every figure is computed from the "
        "definitions the chapter gives. Whether a machine's saving in unpaid labour, or a "
        "pioneer's extra surplus value, describes the economy you live in is what the "
        "book argues about, and each lesson says where the strongest objections come from.",
    ],
    "not_covered": [
        "The history in Chapter 15. The employment of women and children, the factory "
        "regime, the Luddites, the cotton crisis, domestic industry and the Factory Acts "
        "take most of the chapter's pages. The lessons state them briefly and compute "
        "only the mechanisms: value transferred, intensity and the capital set free.",
        "The value of labour-power spread over a family. Marx argues that machinery, by "
        "putting the whole family to work, lowers the value of each member's "
        "labour-power. The lesson on intensity states this; no lab computes it, because "
        "the chapter gives no figures for it.",
        "Prices that differ from values, and the rate of profit. Every lab here prices "
        "goods and labour-power at their values. Part V mentions the rate of profit to "
        "correct John Stuart Mill; it is computed in Cost Price and the Rate of Profit.",
        "The long-run effect of machinery on total employment. Whether mechanisation "
        "reduces employment over decades is a question about data, which this path does "
        "not carry. The lessons compute what installing a machine does to one capital's "
        "wage fund, and say that the wider question is argued elsewhere.",
        "Theories of the firm and of management. Co-operation raises the question of "
        "what a manager is paid for, which later economics answers very differently. "
        "The lesson states the opposing view in a paragraph and goes no further.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the hours, wages, "
        "rates and prices a lesson states, in exact arithmetic, on Marx's definitions. "
        "The figures are illustrative except where a preset says it uses Marx's own, and "
        "no lab can tell you whether the gap between the labour a machine saves and the "
        "wages it saves is really unpaid labour."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
