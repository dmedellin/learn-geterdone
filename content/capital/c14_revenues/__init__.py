"""Course 14 -- Revenues and Their Sources: Volume III, Part VII, Chapters 48-52.

Five lessons, one per chapter, all in part_a. The last course of the Subject;
its last lesson ends where Marx's manuscript does.
"""

from . import part_a

COURSE = {
    "slug": "capital-revenues-and-their-sources",
    "title": "Revenues and Their Sources",
    "level": "Advanced",
    "summary": (
        "Volume III, Part VII, The Revenues and Their Sources: Chapters 48 to 52, the last Part "
        "of Capital. The trinity formula, in which capital yields interest, land rent and labour "
        "wages; the gap between a year's product and a year's income; why a price looks like "
        "wages, profit and rent added up; whether distribution can change while production does "
        "not; and the unfinished chapter on classes."
    ),
    "blurb": (
        "Divide one value product into wages, rent, interest and profit of enterprise, and move "
        "the shares without moving the whole. Find the part of Marx's 9,000 of annual product "
        "that is nobody's income, run his wage rise on 400c + 100v + 150s, split one product "
        "three ways under three relations of production, and count classes by source of revenue "
        "until the manuscript stops."
    ),
    "key": [
        "annual product = c + v + s",
        "value product = v + s",
        "v + s = wages + profit + rent",
        "s = rent + interest + profit of enterprise",
        "Ic is replaced within Department I",
        "a wage rise comes out of s",
        "classes by source of revenue: no limit",
    ],
    "assumes_short": "Volumes I to III",
    "assumes_long": (
        "the thirteen courses before it, and above all the reproduction schemes of Reproduction "
        "of the Social Capital, the split of profit in Merchant's Capital and Interest and the "
        "rent of Ground Rent"
    ),
    "outcomes_intro": (
        "By the end you can take any income the trinity formula names and say, in figures, which "
        "part of which value product it is."
    ),
    "outcomes": [
        ("Resolve the revenues",
         "Given a product's c, v and s and the shares of s taken by rent and interest, compute "
         "wages, rent, interest and profit of enterprise, and show that they sum to v + s."),
        ("Separate product from income",
         "Given a two-department scheme, compute the annual product, the annual revenue and the "
         "part of the product exchanged within Department I that is no one's income."),
        ("Divide a fixed value product",
         "Compute the four revenues after a change in wages or in the shares of s, and show that "
         "the product's value does not move."),
        ("Compare relations of production",
         "Divide one value product under a capitalist firm, a co-operative and an association "
         "of producers, and say what is common to all three and what belongs to one."),
        ("Test a definition of class",
         "Group a list of people by source of revenue, recount as the sources are made finer, "
         "and state the objection with which Chapter 52 ends."),
    ],
    "syllabus_intro": (
        "Five lessons read the five chapters of Part VII in Marx's order: the trinity formula, the "
        "product and the income, the appearance of price as a sum, distribution and production, "
        "and the chapter on classes that the manuscript leaves unfinished."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words and then "
        "goes back through them a phrase at a time. Quotations are from the Kerr editions in the "
        "Online Library of Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of text this is. Part VII comes from the manuscript Marx wrote in the "
        "mid-1860s and never revised; Engels published Volume III in 1894, eleven years after "
        "Marx's death. Chapter 48 is three fragments Engels found in different places, with a "
        "folio missing, and Chapter 52 stops after a page. The lessons follow Engels' text and "
        "say where it is broken.",
        "Keep the earlier courses within reach. Chapter 49 reuses the reproduction scheme of "
        "Volume II with Marx's figures, and Chapter 50 works a wage rise on 400c + 100v + 150s "
        "with his figures too. The other presets are illustrative, and each lesson says so.",
        "Keep the accounting apart from the verdict. Every figure is computed on Marx's "
        "definitions, on which the year's labour makes the value product and the revenues are "
        "its parts. The marginal-productivity account, on which each factor is paid for what it "
        "adds, reads the same figures differently, and the lessons state it at its strongest.",
    ],
    "not_covered": [
        "What a class is. The manuscript asks and breaks off; the last lesson ends there. Later "
        "answers, Lenin's and Weber's among them, are named in its note and not argued.",
        "The marginal-productivity theory of distribution and the Cambridge capital controversy. "
        "Both are stated in “The Trinity Formula”; neither is computed, because computing either "
        "would take a side.",
        "Monopoly prices and the limits they set. Chapter 50 says a monopoly price transfers "
        "surplus value from other producers without changing the total; the lab does not model "
        "it.",
        "The socialist calculation debate. Mises, Lange and Hayek are named in “Distribution "
        "Relations and Production Relations” as the standard objection to an association of "
        "producers; the debate itself is not followed.",
        "Prices under modern money. Whether a general rise in money wages raises the price level "
        "is a question about paper money, which this Subject does not model.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the value parts, shares "
        "and people a lesson states, in exact arithmetic, on Marx's definitions. The scheme of "
        "Chapter 49 and the example of Chapter 50 are Marx's; the rest are illustrative. No lab "
        "can tell you whether the year's labour alone makes the value the revenues divide."
    ),
    "lessons": part_a.LESSONS,
}
