"""Course 13 -- Ground Rent: Volume III, Part VI, Chapters 37-47.

Eleven lessons, one per chapter: part_a is Chapters 37 to 42 (the price of
land, the waterfall, differential rent I and the first two cases of
differential rent II); part_b is Chapters 43 to 47 (the rising-price case, rent
on the worst soil, absolute rent, building and mining rent, and the history of
rent from labour rent to the capitalist tenant).
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-ground-rent",
    "title": "Ground Rent",
    "level": "Advanced",
    "summary": (
        "Volume III, Part VI, Transformation of Surplus Profit into Ground-Rent: Chapters 37 "
        "to 47. How a portion of surplus value passes to the owners of land; why the price of "
        "land is rent capitalised; how unequal soils and unequal doses of capital make "
        "differential rent, at a constant, falling or rising price of corn; how even the worst "
        "soil can pay rent; what absolute rent is; and how rent came to be a surplus over "
        "profit, from labour rent on the lord's field to the capitalist tenant's lease."
    ),
    "blurb": (
        "Do Marx's rent tables yourself, soil by soil and dose by dose. Price land from its "
        "rent, compute the waterfall's surplus profit, the rents on four soils and on one acre "
        "with four capitals, follow total rent as the price of corn falls and rises, and "
        "compute the absolute rent a low composition of capital allows."
    ),
    "key": [
        "price of land = rent / rate of interest",
        "price set by the least productive dose",
        "rent = output · price − capital − profit",
        "A–D: 1–4 quarters; rents 0–180s at 60s",
        "rent needs unequal soils, not worse ones",
        "absolute rent ≤ value − price of production",
        "labour rent: lord's days / own days",
    ],
    "assumes_short": "Volumes I and II, Volume III Parts I and II",
    "assumes_long": (
        "the courses on Volume I, above all the rate of surplus value from From Money to "
        "Surplus Value, and from Volume III Cost Price and the Rate of Profit and Average "
        "Profit and Its Fall, whose prices of production and average rate of profit every "
        "lesson here uses; Merchant's Capital and Interest supplies the rate of interest at "
        "which rent is capitalised"
    ),
    "outcomes_intro": (
        "By the end you can rebuild Marx's rent tables from the figures in his sentences, and "
        "say in his terms what each rent is a share of."
    ),
    "outcomes": [
        ("Price a piece of land",
         "Compute the price of land from its rent and the rate of interest, separate the true "
         "rent from interest on capital sunk in the land, and compute the price after a change "
         "in the rate of interest."),
        ("Compute differential rent I",
         "Given soils with equal capitals and unequal yields, compute the regulating price, "
         "each soil's rent and the total, and the waterfall's surplus profit by both of Marx's "
         "measures."),
        ("Compute differential rent II",
         "Given successive doses of capital on each soil, compute the rents at a constant "
         "price, and when the price falls because the worst soil drops out, or rises because a "
         "less productive dose or a worse soil is needed."),
        ("Find rent on the worst soil",
         "Compute the rent the worst soil pays when an additional dose on a better soil "
         "regulates the price."),
        ("Compute absolute rent",
         "Compute agriculture's value and its price of production equalised with industry, "
         "and the absolute rent the difference allows, with and without a market limit."),
        ("Compare the forms of rent",
         "Compute the rate of surplus labour in labour rent from days on the lord's land and "
         "days on one's own, and say what changes in rent in kind and money rent."),
    ],
    "syllabus_intro": (
        "Eleven lessons read the eleven chapters of Part VI in order: the preliminaries and "
        "the waterfall, the two forms of differential rent and the three cases of the second, "
        "rent on the worst soil, absolute rent, building and mining rent, and the history of "
        "rent."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and then "
        "goes back through them a phrase at a time, so the passage is worth a second reading once "
        "the lesson is done. Quotations are from the Kerr editions in the Online Library of "
        "Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of text Part VI is. Marx did not finish Volume III, and Engels assembled "
        "it from his manuscripts and published it in 1894. Chapters 39 to 44 are long runs of "
        "tables, some of them with slips in the arithmetic; Chapter 43's third case existed in "
        "the manuscript only as a title, and Engels wrote it. The lessons say where Engels' hand "
        "is, and where a figure in the text does not follow from the yields it gives.",
        "Expect the tables to be rebuilt. The Kerr edition prints Marx's tables as images, "
        "which the lessons cite by page; each &ldquo;Marx's figures&rdquo; preset is built "
        "from a printed table or from the sentences around it, and checked against both. The labs reckon in shillings throughout; Marx changes from shillings to pounds "
        "after Chapter 39, and 60s is his £3.",
        "Keep the definitions apart from the verdict. Every figure is computed on Marx's "
        "definitions, above all his claim that land adds no value and rent is a share of "
        "surplus value. Ricardo built the theory Marx is correcting, and the economists who "
        "came after Marx treat rent as the earnings of a productive factor; the lessons give "
        "both at strength and settle neither.",
    ],
    "not_covered": [
        "Location. Marx names it as the second cause of differential rent beside fertility and "
        "then sets it aside; so do the labs, which compare soils by their yields alone.",
        "The averaging of successive doses. Chapter 43 says a landlord sees only the yield of "
        "the whole acre and must average the doses before a rent can be set; Engels' "
        "correction in Chapter 44 turns on it. The labs value every dose separately at the "
        "regulating price, and the lessons say where the two rules part.",
        "The tables the labs cannot hold. Chapter 39's Table II has seven soils, one more "
        "than a lab takes; Chapter 42's Table V, Chapter 44's corrected figures and most of "
        "Engels' tables in Chapter 43 price a soil's product at its average. They are "
        "described in prose rather than computed.",
        "Monopoly price proper. Marx distinguishes rent that rests on a true monopoly price, "
        "such as a rare vineyard's, from differential and absolute rent, and leaves its "
        "analysis to a theory of competition; Building Rent, Mining Rent, the Price of Land "
        "names it and computes nothing.",
        "Whether agriculture's composition of capital is in fact lower than industry's. Marx "
        "says it is a question for statistics; this course carries none, and treats absolute "
        "rent as what follows from his assumption.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the soils, doses, prices "
        "and rates a lesson states, in exact arithmetic, on Marx's definitions. The tables are "
        "Marx's except where a preset says otherwise, and no lab can tell you whether rent is "
        "a share of surplus value or the earnings of the land."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
