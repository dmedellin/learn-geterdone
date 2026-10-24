"""Course 12 -- Credit and Fictitious Capital: Volume III, Part V, Chapters 25-36.

Split across two lesson modules: part_a is Chapters 25-30 (credit, the rate of
interest, stock companies, currency and capital, bank capital, money capital
and real capital I); part_b is Chapters 31-36 (money capital and real capital
II and III, the currency, the Bank Act, gold and the exchanges, usury). Part V
begins in Merchant's Capital and Interest, whose last four lessons read
Chapters 21-24.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-credit-and-fictitious-capital",
    "title": "Credit and Fictitious Capital",
    "level": "Advanced",
    "summary": (
        "Volume III, Part V, Division of Profit into Interest and Profit of Enterprise, "
        "Chapters 25 to 36. How bills of exchange and banks make credit money, what sets "
        "the rate of interest in a boom and a crash, what stock companies do to the owner "
        "of capital, why a share or a bond is fictitious capital, why money capital can pile "
        "up while real accumulation stands still, how the Bank Act of 1844 sharpened two "
        "crises, how gold moves between countries, and what usury was before capitalism."
    ),
    "blurb": (
        "Settle a circle of bills with no cash, then break it. Price a bond at three rates of "
        "interest, watch a stock company turn profit into interest and its manager into a "
        "wage earner, release £600 from a business that shrinks, push notes out and see them "
        "come back, run Marx's figures for the Bank of England into a panic, and follow a "
        "peasant's debt to the usurer year by year."
    ),
    "key": [
        "cash to settle bills = positive balances",
        "enterprise = profit less interest",
        "price of a claim = income / rate",
        "loan capital grows without saving",
        "notes needed = prices / velocity",
        "the Act's cap = fixed issue + gold",
        "gold shipped = imports − exports − receipts",
    ],
    "assumes_short": "Volumes I and II, and Volume III through Part IV",
    "assumes_long": (
        "Merchant's Capital and Interest, whose lessons on interest-bearing capital and the "
        "rate of interest this course continues; the general rate of profit from Cost Price "
        "and the Rate of Profit and Average Profit and Its Fall; the circle of payments from "
        "Commodities and Money; and the working and circulation periods from The Turnover of "
        "Capital"
    ),
    "outcomes_intro": (
        "By the end you can compute what credit does to the money a circulation needs, the "
        "price of a claim and the reserve of a bank, and say, chapter by chapter, where "
        "Marx's argument is finished and where Engels had only notes to work from."
    ),
    "outcomes": [
        ("Settle a chain of credit",
         "Net a set of bills of exchange, compute the cash their settlement needs, and show "
         "what a bill with no sale behind it, or a default, adds."),
        ("Divide profit",
         "Split a profit into interest and profit of enterprise at a given rate, find where the "
         "rate of profit caps the rate of interest, and show how a stock company turns the whole "
         "profit into dividend and salary."),
        ("Price fictitious capital",
         "Capitalise a yearly income at a rate of interest, and show the price moving with the "
         "rate while nothing real changes."),
        ("Separate money capital from real capital",
         "Compute the money that piles up when hoarders outnumber investors, and the capital a "
         "contracting business releases to the money market without anyone saving."),
        ("Follow the currency",
         "Compute the notes a circulation needs, the excess that flows back, the Bank Act's cap "
         "and the demand it leaves unmet, and the gold a balance of payments sends abroad."),
        ("Follow a debt to the usurer",
         "Compute a small producer's debt year by year and the year it passes the value of the "
         "holding."),
    ],
    "syllabus_intro": (
        "Twelve lessons read the twelve chapters from 25 to 36 in order: credit and the banks, "
        "the rate of interest, stock companies, currency and capital, the bank's capital, three "
        "chapters on money capital and real capital, the currency, the Bank Act, gold and the "
        "exchanges, and usury before capitalism."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with the text and then goes "
        "back through it a phrase at a time. Quotations are from the Kerr editions in the Online "
        "Library of Liberty, hosted by Liberty Fund, Inc.",
        "Know what kind of manuscript Part V is. Engels, who edited Volume III after Marx's "
        "death, says this part gave him the most trouble: for it there was &ldquo;no finished "
        "draft, nor even an outline&rdquo;, and the draft &ldquo;more than once ended in a "
        "disarranged mass of notes, comments and extracts&rdquo;. Several chapters are mostly "
        "extracts from the parliamentary inquiries of 1847 to 1858, with Marx's comments between "
        "them, and Engels wrote some passages himself. The lessons read the argument through the "
        "extracts, say whose words a passage is, and say where the manuscript stops short.",
        "Keep the figures apart. Where Marx gives figures, as for the Bank of England's reserve or "
        "a bond capitalised at 5%, the labs use them; where he gives none, the figures are "
        "illustrative, and each lesson's note says which are which.",
        "Keep the computation apart from the verdict. Every lab computes on the chapter's own "
        "definitions. Whether Marx's account of credit and crises is right is argued to this "
        "day, and the lessons name the other side's case at its strongest without settling it.",
    ],
    "not_covered": [
        "Public credit and the national debt as a system. Marx treats government bonds only as "
        "the first example of fictitious capital.",
        "The full statistical tables and the long runs of committee evidence. The lessons quote "
        "the passages the argument turns on and leave the rest.",
        "Marx's critique of Ricardo's theory of money, which Chapter 34 only summarises from his "
        "Contribution to the Critique of Political Economy of 1859.",
        "Money and banking after the gold standard. The chapters assume notes convertible into "
        "gold; how far they carry over to central banks and inconvertible money is a question "
        "the lessons point to and do not answer.",
        "The rate of interest's own laws and the split of profit as such, which belong to "
        "Merchant's Capital and Interest.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser, in exact arithmetic, from the "
        "bills, rates, reserves and debts a lesson states. Marx's figures are used where he gives "
        "them; the rest are illustrative. No lab can tell you whether a crisis is a lack of money "
        "or a lack of capital."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
