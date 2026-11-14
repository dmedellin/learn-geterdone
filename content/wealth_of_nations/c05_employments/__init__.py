"""Course 5 -- Wages and Profit in Different Employments: Book I, Chapter 10.

One chapter, five lessons: part_a holds all five. Part I of the chapter (the
inequalities that arise from the nature of the employments) is the first three
lessons; Part II (the inequalities the policy of Europe occasions) is the last
two.
"""

from . import part_a

COURSE = {
    "slug": "wealth-different-employments",
    "title": "Wages and Profit in Different Employments",
    "level": "Beginner",
    "summary": (
        "Book I, Chapter 10, Wages and Profit in the Different Employments of Labour and "
        "Stock. Why money wages differ from trade to trade while the whole of the "
        "advantages of the trades tends to equality: Smith's five circumstances, the "
        "lottery of the professions, the apothecary's wages in the garb of profit, and "
        "what apprenticeship, corporations and the law of settlements do to the equality."
    ),
    "blurb": (
        "Read one of the longest chapters of Book I with the arithmetic beside it. Net a trade's "
        "pay against what it costs to learn and what it makes you put up with, test "
        "whether a profession's prizes repay its tickets, take a trader's wages out of his "
        "profit, and price what a long apprenticeship adds to a wage."
    ),
    "key": [
        "whole advantage = wage − learning + other",
        "learning a year = cost/years + profit",
        "fair prize = tickets / (winners × years)",
        "true profit = apparent profit − wages",
        "a cap on entry lifts pay above the rest",
        "a spread that lasts needs a barrier",
    ],
    "assumes_short": "Nothing",
    "assumes_long": "no economics and no earlier course is assumed, and school arithmetic is enough",
    "outcomes_intro": (
        "By the end you can do the arithmetic of Chapter 10 yourself and say, in Smith's "
        "terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Net a trade's advantages",
         "Compute a trade's yearly money wage, charge it with each year's share of what "
         "learning cost and the ordinary profit on that sum, add a stated value for its "
         "other circumstances, and say whether the whole of its advantages is level with "
         "another trade's."),
        ("Read the five circumstances",
         "Name the five circumstances, say which of them also affect the profits of stock, "
         "and say why a mason's high day wage is no sign of his skill."),
        ("Test a profession as a lottery",
         "Compute the chance of success, the total prizes and tickets, and the yearly prize "
         "that would make a profession a fair lottery."),
        ("Separate wages from profit",
         "Take the wages of a trader's own labour out of his apparent profit, and compute "
         "the profit and rate that remain."),
        ("Price a restraint on entry",
         "Compute what a long apprenticeship or a cap on apprentices adds to the wage a "
         "trade must be paid, and say who pays it in Smith's account."),
        ("Read a wage gap as a barrier",
         "Compute the spread in the year's pay between two places and say what Smith's "
         "mechanism predicts if labour could move, and what else could keep the gap open."),
    ],
    "syllabus_intro": (
        "Three lessons read Part I of the chapter, the inequalities that arise from the "
        "nature of the employments themselves. Two read Part II, the inequalities the "
        "policy of Europe occasions."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson goes through Smith's words a "
        "phrase at a time, so the passage is worth a second reading once the lesson is done. "
        "This is a read-along of Adam Smith, <em>An Inquiry into the Nature and Causes of "
        "the Wealth of Nations</em> (1776); quotations are from the public-domain Electronic "
        "Classics Series edition.",
        "Money is in pounds, shillings and pence, as Smith writes it: twelve pence to the "
        "shilling and twenty shillings to the pound. A guinea is twenty-one shillings. The "
        "labs take their money in one unit the preset names, shillings or pounds, and "
        "never both at once.",
        "Notice whose figures a preset uses. A preset labelled with Smith's name uses a figure "
        "he states in the chapter; one labelled as written for this lesson is an invention "
        "to show a method, and Smith never says it. Run the arithmetic on both, and keep the "
        "two apart in your head.",
        "Keep the definitions apart from the verdict. Every figure is computed from the "
        "reasoning the chapter gives. Whether the reasoning describes how any economy "
        "works, then or now, is what the book and its critics argue about, and each lesson "
        "says where the standard objection comes from.",
    ],
    "not_covered": [
        "Smith's figures for wages and prices in different places and times. Chapter 10 "
        "gives dozens, from London coal-heavers to Shetland stockings and Athenian "
        "teachers. The lessons use a handful as preset data and cite the rest in prose; "
        "none of them is a measurement of the whole economy.",
        "The long history of the English poor laws. Smith's account of the settlement "
        "statutes is read in outline, as far as it explains the obstruction to movement, "
        "and the later history of poor relief is not told.",
        "Modern accounts of wage differences. Compensating differentials, human capital, "
        "segmented labour markets and the economics of discrimination all descend from "
        "or argue with this chapter. The lessons name a few critics who wrote after "
        "Smith and go no further.",
        "The rest of the dispute over guilds. Historians have argued for generations about "
        "what apprenticeship and corporations did. The fourth lesson gives Smith's case "
        "and says where it is contested; it does not settle it.",
        "Rent, which the next course takes up, and the Book III account of how the town "
        "outgrew the country, to which Smith points forward at the end of Part II.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the wages, costs and "
        "chances a lesson states, in exact arithmetic, on Smith's reasoning. The figures "
        "are illustrative except where a preset says it uses Smith's, and no lab can tell "
        "you whether the whole of the advantages of the trades does tend to equality."
    ),
    "lessons": part_a.LESSONS,
}
