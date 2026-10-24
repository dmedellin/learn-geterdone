"""Course 8 -- Reproduction of the Social Capital: Volume II, Part III, Chapters 18-21.

Six lessons, all in part_a: one each for Chapters 18 and 19, two each for
Chapters 20 and 21.
"""

from . import part_a

COURSE = {
    "slug": "capital-social-reproduction",
    "title": "Reproduction of the Social Capital",
    "level": "Advanced",
    "summary": (
        "Volume II, Part III, The Reproduction and Circulation of the Aggregate Social Capital: "
        "Chapters 18 to 21. How the product of a whole society, divided into means of production "
        "and means of consumption, replaces the capital used up and feeds the people who made it; "
        "why Adam Smith's account lost part of its value; what simple reproduction requires; how "
        "fixed capital and hoarding can break the balance; and how the scheme grows when surplus "
        "value is accumulated."
    ),
    "blurb": (
        "Work through Marx's reproduction schemes with the arithmetic beside them. Sort a "
        "society's product into two departments, find the 6,000 that Smith's dogma loses, check "
        "the condition I(v + s) = IIc, price the gap between machines worn and machines renewed, "
        "and run Marx's scheme of accumulation for four years."
    ),
    "key": [
        "Department I: means of production",
        "Department II: means of consumption",
        "annual product = c + v + s, not v + s",
        "simple reproduction: I(v + s) = IIc",
        "renewals in kind = wear hoarded in money",
        "hoarders' sales = investors' purchases",
        "accumulation: I(v + s) > IIc",
    ],
    "assumes_short": "Volume I and the first two courses on Volume II",
    "assumes_long": (
        "the five courses on Volume I, above all c, v and s and the rate of surplus value from "
        "From Money to Surplus Value, and the two earlier courses on Volume II, The Circuits of "
        "Capital and The Turnover of Capital"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic of Marx's reproduction schemes yourself and say "
        "what each balance condition asks of the two departments."
    ),
    "outcomes": [
        ("Sort the social product",
         "Assign a society's products to Department I or Department II by their use, and total "
         "each department."),
        ("Find Smith's missing c",
         "Compute the value of an annual product with and without its constant capital, and say "
         "which part no income of the year accounts for."),
        ("Check simple reproduction",
         "Given both departments' c, v and s, test I(v + s) = IIc, compute the three great "
         "exchanges, and say what is left unsold when the condition fails."),
        ("Balance fixed capital",
         "Compute the gap between Department II's renewals in kind and its wear hoarded in money, "
         "and name the side left short."),
        ("Balance the hoards",
         "Compute the surplus product left unsold, or the demand left without a product, when "
         "the capitalists of Department I who hoard and those who invest do not match."),
        ("Run a scheme of accumulation",
         "Run Marx's expanded scheme period by period, compute both departments after each "
         "period and the growth of the annual product, and say when balance is impossible."),
    ],
    "syllabus_intro": (
        "Six lessons read the four chapters of Part III: one for the introduction, one for the "
        "history of the question, and two each for the long chapters on simple and on enlarged "
        "reproduction."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and then "
        "goes back through them a phrase at a time, so the passage is worth a second reading once "
        "the lesson is done. Quotations are from the Kerr editions in the Online Library of "
        "Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of text Part III is. Engels assembled it after Marx's death from Marx's "
        "manuscripts, chiefly the ones he numbered II and VIII, and his footnotes say which "
        "passage comes from which. Chapter 21 ends where the manuscript does. The arithmetic is "
        "worked out on the page, sometimes by trial, with fractions rounded off and the odd slip "
        "in a sum; the lessons follow Engels' text and say where a figure needs correcting.",
        "Keep Marx's scheme in view. I 4,000c + 1,000v + 1,000s and II 2,000c + 500v + 500s, "
        "9,000 in all, are the figures of Chapter 20, and Chapter 21 starts its growth from the "
        "same Department I. Marx says the figures may stand for millions of francs, marks, pounds "
        "or dollars; the labs print them bare, as he does, except where Smith's dogma is priced "
        "in pounds.",
        "Keep the definitions apart from the verdict. Every balance here is computed on Marx's "
        "definitions, with everything exchanged at its value. Whether an economy that nobody "
        "plans comes to meet these conditions, and by what mechanism, is a question his readers "
        "have argued over since the 1890s, and the lessons say who argued what.",
    ],
    "not_covered": [
        "The exchange within Department II between necessities and luxuries (Chapter 20, §4). "
        "Marx divides Department II in two and shows that the wages of the workers who make "
        "luxuries return to their employers only through capitalists' spending; the lessons name "
        "it and do not compute it.",
        "The reproduction of the money material (Chapter 20, §12) and Chapter 21's closing "
        "remarks on where Department II's money comes from. The gold producer appears only as "
        "the one capitalist who can buy without first having sold.",
        "Destutt de Tracy's theory of reproduction (Chapter 20, §13) beyond a sentence, and most "
        "of the argument with Smith's successors in Chapter 19.",
        "The later debate on the schemes: Tugan-Baranovsky, Luxemburg, Bauer, Bukharin and "
        "Grossman, and the two-sector growth models descended from it. The last lesson names the "
        "dispute; no lesson computes a later model.",
        "Prices that differ from values. Marx says a divergence would change who gets what, not "
        "the quantities exchanged; prices of production belong to Average Profit and Its Fall.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the departments' c, v and s "
        "and the shares a lesson states, in exact arithmetic, on Marx's definitions. The schemes "
        "are Marx's; the variations on them are illustrative. No lab can tell you whether a real "
        "economy meets these balances, or how."
    ),
    "lessons": part_a.LESSONS,
}
