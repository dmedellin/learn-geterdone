"""Course 4 -- Wages and Accumulation: Volume I, Parts VI and VII, Chapters 19-25.

Split across two lesson modules: part_a is Part VI on wages (Chapters 19-22)
and Chapter 23; part_b is Chapter 24 and the three lessons on Chapter 25.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-wages-and-accumulation",
    "title": "Wages and Accumulation",
    "level": "Intermediate",
    "summary": (
        "Volume I, Part VI, Wages, and Part VII, The Accumulation of Capital: Chapters 19 "
        "to 25. Why the value of labour-power appears as a price paid for labour, how "
        "time-wages and piece-wages convert it, what a comparison of national wages has "
        "to measure, what the bare repetition of production does to a capital, how "
        "surplus value becomes capital, and how accumulation produces a reserve army of "
        "labour."
    ),
    "blurb": (
        "Read the chapters on wages and accumulation with Marx's own sums beside them. "
        "Compute the price of an hour and of a piece, compare two countries' wages per "
        "unit of output, count the years in which a capitalist consumes his capital, run "
        "accumulation period by period, and watch employment stand still while capital "
        "triples."
    ),
    "key": [
        "price of an hour = day's value / hours",
        "piece-rate = day's value / normal pieces",
        "years = capital / yearly surplus consumed",
        "next capital = capital + share · s",
        "v = capital / (1 + c/v)",
        "workers employed = v / wage",
        "reserve = supply − workers employed",
    ],
    "assumes_short": "Commodities and Money, From Money to Surplus Value and Relative Surplus Value",
    "assumes_long": (
        "the value of labour-power and the rate of surplus value from From Money to Surplus "
        "Value, and the working day, intensity and machinery from Relative Surplus Value"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of Parts VI and VII yourself and say, in "
        "Marx's terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Read a wage",
         "Compute the apparent price of an hour from the daily value of labour-power and "
         "the length of the day, set it beside the value the hours create, and name the "
         "unpaid part the wage form hides."),
        ("Compute time-wages and piece-wages",
         "Compute the price of an hour from the normal day and the day's wage for any hours "
         "worked; compute a piece-rate from the normal output, and recompute both when the "
         "day or the output changes."),
        ("Compare national wages",
         "Compute two countries' wages per unit of output and their rates of surplus value, "
         "and say which country's labour is cheaper per unit whatever its money wage."),
        ("Reckon simple and expanded reproduction",
         "Compute the years in which a capitalist consumes a sum equal to his capital, and "
         "run accumulation period by period to find the original capital's share of the "
         "present one."),
        ("Follow employment through accumulation",
         "Compute the workers employed, the reserve and the ratio of reserve to employed "
         "period by period, at a constant or a rising composition of capital."),
    ],
    "syllabus_intro": (
        "Four lessons read the four chapters of Part VI on wages. Two read the first two "
        "chapters of Part VII, on simple reproduction and on accumulation, and three follow "
        "Chapter 25 from a constant composition of capital to the general law."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and "
        "then goes back through them a phrase at a time. Quotations are from the Kerr "
        "editions in the Online Library of Liberty, hosted by Liberty Fund, Inc.",
        "Expect two different kinds of chapter. Part VI is short and about an appearance: "
        "the wage looks like a price paid for work. Part VII is long, and Chapter 25 is the "
        "longest in Volume I; three lessons take it, a section or two at a time, and its "
        "fifth section of English and Irish evidence is summarised rather than read.",
        "Use the labs to change one thing at a time. Most presets keep Marx's figures and "
        "change one of them, the hours of the day, the normal output, the share of surplus "
        "value capitalised, the rise in the composition of capital, and the point of the "
        "lesson is in what moves and what does not.",
        "Keep the arithmetic apart from the verdict. Every figure is computed on the "
        "chapter's definitions. Whether wages hide unpaid labour, whether capital is "
        "capitalised surplus value and whether accumulation produces a reserve army in fact "
        "are what the book argues, and each lesson names the strongest reply.",
    ],
    "not_covered": [
        "The forms of wages beyond the two fundamental ones. Marx says an exposition of all "
        "the forms of wages belongs to a special study of wage-labour and leaves it out; so "
        "does this course. Overtime paid at a separate rate is worked in prose, not in a lab.",
        "A model of the labour market. The labs raise wages by one simple rule when demand "
        "outruns the supply of workers, and never let them fall back. Marx states the "
        "direction and the limit of the movement, not a formula, and modern theories of "
        "wages and unemployment are named only where a lesson needs the contrast.",
        "Empirical tests of the reserve army and of immiseration. Data on wages, employment "
        "and poverty since 1867 is not computed here. The last lesson says how the general "
        "law has been read and disputed, and that the dispute is about evidence this course "
        "does not carry.",
        "Most of Chapter 25, Section 5. Marx's illustrations of the general law from England "
        "and Ireland, 1846 to 1866, run to many pages of tables and reports. The last lesson "
        "summarises them and quotes one exchange, with Gladstone.",
        "Where the first capital came from. Chapter 24 postpones the question, and the next "
        "course, So-Called Primitive Accumulation, answers it.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the wages, outputs, "
        "capitals and rates a lesson states, in exact arithmetic, on Marx's definitions. The "
        "figures are illustrative except where a preset says it uses Marx's, and no lab can "
        "tell you whether a wage hides unpaid labour or whether accumulation must produce a "
        "reserve army."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
