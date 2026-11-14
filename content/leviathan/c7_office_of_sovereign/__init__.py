"""Course 7 -- Wealth, Counsel, Law and the Office of the Sovereign: Chapters 24-31.

Split across two lesson modules: part_a is Chapters 24-27 (nutrition, counsel,
civil laws, crimes); part_b is Chapters 28-31 (punishments, dissolution, the
office of the sovereign, the kingdom of God by nature).
"""

from . import part_a, part_b

COURSE = {
    "slug": "leviathan-office-of-sovereign",
    "title": "Wealth, Counsel, Law and the Office of the Sovereign",
    "level": "Intermediate",
    "summary": (
        "Part II, Chapters 24 to 31: what a commonwealth does once it is made. How it is "
        "fed and how property comes to be, who should advise the sovereign and how, what "
        "a civil law is, what makes an act a crime and what a punishment, what kills a "
        "commonwealth, what the sovereign owes the people, and by what right God rules, "
        "which closes Part II."
    ),
    "blurb": (
        "Follow the artificial man through its digestion, its counsel, its laws and its "
        "diseases. Divide a harvest by stated shares, compute when a majority of "
        "counsellors is right, test Hobbes's argument that the sovereign is above the "
        "civil laws, find when a crime pays and when a harm is a price or hostility, play "
        "out a divided sovereignty as a game, raise a revenue on riches and on "
        "consumption, and test the argument from power to right."
    ),
    "key": [
        "share = (total - set apart) · weight / weights",
        "majority right = sum over k > n/2",
        "who can repeal a law is free of it",
        "a crime pays if chance · penalty < gain",
        "harm below the gain: a price",
        "two powers, one subject: chicken",
        "tax = rate · what each consumes",
        "valid: no row, true premises, false end",
    ],
    "assumes_short": "The first six courses",
    "assumes_long": (
        "the earlier courses are assumed, above all the definitions of sovereign, "
        "covenant and the laws of nature in Courses 4 to 6, and school arithmetic is "
        "enough for the labs"
    ),
    "outcomes_intro": (
        "By the end you can do the sums these chapters invite and say, in Hobbes's "
        "terms, what each figure is a figure of."
    ),
    "outcomes": [
        ("Divide a distribution exactly",
         "Divide a total by stated shares after a set-aside part, as Canaan was divided, "
         "and say whom Hobbes makes the author of the division."),
        ("Compute a majority of counsellors",
         "Compute the chance that a majority of independent counsellors is right, and "
         "say which of Hobbes's reasons for hearing them apart denies the independence "
         "the figure needs."),
        ("Test an argument from a definition",
         "Set out Hobbes's argument that the sovereign is not subject to the civil laws, "
         "or that God's right comes from his power, as premises, check its form and name "
         "the premise a critic would deny."),
        ("Weigh a punishment",
         "Compute the expected penalty of a crime and say whether it deters, and sort a "
         "harm into punishment, price or hostility by Hobbes's seventh and eighth "
         "inferences."),
        ("Read a divided sovereignty as a game",
         "Find the equilibria of two powers that may each yield or insist, and say what "
         "a sword behind one claim changes."),
        ("Raise a revenue two ways",
         "Compute each person's tax under a rate on riches and a rate on consumption and "
         "say who pays more under the one Hobbes recommends."),
    ],
    "syllabus_intro": (
        "Four lessons take Chapters 24 to 27, from the nutrition of a commonwealth to "
        "crime, and four take Chapters 28 to 31, from punishment to the kingdom of God "
        "by nature."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Hobbes's words "
        "and then goes back through them, so the passage is worth a second reading once "
        "the lesson is done. Quotations are from Hobbes's text of 1651, in its original "
        "spelling.",
        "Use the labs to change one thing at a time. Each preset changes a single figure "
        "against the one before, a chance, a penalty, a payoff, a rate, and the point of "
        "the lesson is in what moves and what does not.",
        "Expect the argument lessons to be short on numbers. <em>Of Civil Laws</em> and <em>The "
        "Kingdom of God by Nature</em> test an argument's form, which tells you what "
        "follows if the premises are granted and nothing about whether they are.",
        "Keep the definitions apart from the verdict. Every figure is computed from "
        "the definitions the chapter gives and from examples written for these "
        "lessons. Whether those definitions describe men and commonwealths is what the "
        "book argues about, and each lesson says where the strongest objections come from.",
    ],
    "not_covered": [
        "The rest of Chapters 24 to 31 that has no lab. Hobbes's account of colonies, "
        "the kinds of law in Justinian, divine positive law and the lawyers' "
        "doctrines are read in the lessons and not computed.",
        "Later theories of counsel, tax and punishment. Condorcet's theorem, "
        "ability-to-pay taxation and Kant's retributivism appear where they bear on a "
        "chapter, and are not worked beyond that.",
        "The Latin Leviathan and Tuck's apparatus. The course reads the English text of "
        "1651 only.",
        "Part III and Part IV. Scripture, the Christian commonwealth and the kingdom of "
        "darkness are the last two courses.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the numbers and "
        "payoffs a lesson states, in exact arithmetic, and shows what follows from them "
        "on Hobbes's definitions. The examples are written for the lessons, and no lab "
        "can tell you whether men and commonwealths are as Hobbes says."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
