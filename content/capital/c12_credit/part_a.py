"""Credit and Fictitious Capital, lessons 1-6 -- Volume III, Part V, Chapters 25-30.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, a drop capital ("AN", "IN", "THE") is printed as an ordinary
capital, and the translator's double quotation marks inside a quotation are
printed as single curly quotes. The Kerr text prints page markers in the
middle of sentences; a quotation that runs across one is printed whole.
Nothing else is changed.

Part V is the roughest manuscript in the book. Engels says in his preface
that it gave him the most trouble, and much of Chapters 25, 26 and 30 is
extracts from the parliamentary reports of 1847-48 and 1857, with Marx's
comments between them. Passages Engels wrote himself are marked [... F. E.]
in the text; a lesson that quotes one says so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 3, l. 3600-3602 (bills as commercial money). Inline: l. 3612
    # (Coquelin), l. 3602 (bank notes rest on bills), l. 3616 (the bank's
    # profit), l. 3621 (discounting), l. 3810 (Engels: a sale), l. 3604
    # (Leatham), l. 3697 (products or wind), l. 3639 (Gilbart); preface
    # l. 304 and l. 308.
    {
        "slug": "credit-and-fictitious-capital",
        "title": "Credit and Fictitious Capital",
        "module": "Chapter 25 · Credit and Fictitious Capital",
        "one_line": "A bill of exchange is a promise to pay for goods already sold; bills that cancel do the work of money without any money, and a bill with no sale behind it is a claim against nothing.",
        "summary": (
            "Chapter 25 opens Marx's account of credit with the bill of exchange, the written "
            "promise to pay on which merchants and manufacturers sell to one another. Compute the "
            "cash a circle of bills needs when it is settled, see what changes when a bank buys "
            "one of the bills before it falls due, and add a bill drawn with no sale behind it to "
            "find the claims that stand against nothing."
        ),
        "key": [
            "bill: a promise to pay on a set day",
            "bills that cancel need no cash",
            "cash = the positive net balances",
            "discount: a bank buys a bill early",
            "accommodation bill: no sale behind it",
        ],
        "key_label": "Commercial credit in five lines",
        "concepts_intro": (
            "Marx says at once that a full analysis of credit is beyond his plan. What he wants "
            "are the few points that show what credit does to capitalist production, and the "
            "first is the oldest and plainest form of it."
        ),
        "concepts": [
            ("Commercial credit",
             "The credit producers and merchants give one another: goods now, payment on a "
             "stated day. The bill of exchange records it, and passes from hand to hand by "
             "endorsement until it falls due."),
            ("Bank credit",
             "The other side of the system. Banks gather the idle money of the whole business "
             "world and lend it, and they turn bills into money before they fall due by "
             "discounting them."),
            ("A bill against nothing",
             "A bill drawn to raise money rather than to pay for goods, or drawn to pay off an "
             "earlier bill. It looks exactly like the others, and a banker cannot tell it from "
             "them by looking."),
        ],
        "read_title": "The bill first, then the bank, then the bills that represent nothing",
        "read_intro": (
            "The chapter's argument is in its first pages, before the extracts begin. The "
            "passage is Marx's definition of the bill as money."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 25.</strong> &ldquo;Such bills of exchange in "
                  "their turn circulate as means of payment until the day on which they fall due; "
                  "and they form commercial money in the strict meaning of the term. To the extent "
                  "that they ultimately balance one another by the compensation of credits and "
                  "debts, they serve absolutely as money, since no transformation into actual "
                  "money takes place.&rdquo;"),
            ("p", "If you have ever sent or received an invoice marked <em>payment due in "
                  "thirty days</em>, you have used the thing Marx starts from. The supplier "
                  "hands over the goods and becomes a creditor; the buyer takes them and becomes "
                  "a debtor. In the 1840s the debt was written as a bill of exchange, and the "
                  "French economist Charles Coquelin, whom Marx quotes, described the chain it "
                  "made, from the producer of raw material down to the shopkeeper: &ldquo;All "
                  "borrow with one hand and lend with the other, sometimes money, but more "
                  "frequently products.&rdquo;"),
            ("p", "A word about the kind of chapter this is. Volume III was put together by "
                  "Engels after Marx's death, and Engels says Part V gave him the most trouble "
                  "of all: for these chapters there was &ldquo;no finished draft, nor even an "
                  "outline&rdquo;, but a draft that &ldquo;more than once ended in a disarranged "
                  "mass of notes, comments and extracts&rdquo;. Chapter 25 is two pages of "
                  "argument followed by long extracts from bankers' books and from the "
                  "parliamentary inquiries into the crises of 1847 and 1857, several of them "
                  "added by Engels from elsewhere in the manuscript. The lessons on Part V read "
                  "the argument through the extracts and say where the manuscript stops short."),
            ("p", "Go back through the passage. The bills &ldquo;circulate as means of "
                  "payment&rdquo;: a manufacturer who holds a bill on his customer can endorse it "
                  "over to his own supplier, who can pass it on again. While they do that they "
                  "are &ldquo;commercial money in the strict meaning of the term&rdquo;, money "
                  "made by merchants out of their own promises. And when they &ldquo;balance one "
                  "another&rdquo;, they &ldquo;serve absolutely as money&rdquo;, because the debt "
                  "is settled and no coin or note ever appears. Marx adds that bank notes grow out "
                  "of this, not the other way round: credit money &ldquo;proper&rdquo; does not "
                  "rest on the circulation of money &ldquo;but upon the circulation of bills of "
                  "exchange&rdquo;."),
            ("p", "The lab writes the bills down and sets each party's bills against one "
                  "another. In the bills preset, A owes B £100 for cotton, B owes C £100 for yarn "
                  "and C owes A £100 for cloth, all due on the same day. Each party pays £100 and "
                  "receives £100, so every balance is zero: £300 of goods have changed hands and "
                  "the settlement needs £0 of cash. This is the circle of debts from Volume I's "
                  "chapter on money, which you met in “Hoards and Means of Payment”. What is new "
                  "is Marx's claim that the bills are themselves a kind of money, and that a whole "
                  "credit system stands on them."),
            ("p", "Then the other side, the banks. A bank gathers the reserves every business "
                  "must keep, the deposits of the rich and the small savings of everyone else, "
                  "and lends them; its profit &ldquo;is generally made by borrowing at a lower "
                  "rate of interest than it loans&rdquo;. One of the ways it lends is by "
                  "discounting bills, &ldquo;that is, by converting them into money before they "
                  "come due&rdquo;. In the discounted preset B does not wait for A to pay: B sells "
                  "his bill on A to a bank, takes the money now, less a deduction for the weeks "
                  "the bill has still to run, and on the due day A pays the bank. The circle no "
                  "longer closes among the three merchants. Set the bills off again and B owes C "
                  "£100 with nothing coming in, and the bank is owed £100: the settlement needs "
                  "£100 of cash. It is the bank's own £100, which B received when the bill was "
                  "sold, paid on to C, from C to A, and from A back to the bank."),
            ("p", "Was that a loan of money to B? Engels, in a passage he added to the next "
                  "chapter, says it was not. When a bill is discounted, &ldquo;even the form of an "
                  "advance disappears. The transaction is then purely one of buying and "
                  "selling.&rdquo; B sold a claim to money for money, as he might sell cotton; the "
                  "goods behind the bill had been delivered long before. The bankers of the day "
                  "saw it the other way. To them every note they paid out was an advance of "
                  "capital to a customer who lacked it, and the next lesson hears them say so "
                  "before a committee of Parliament."),
            ("p", "Now the bills that represent nothing. The Yorkshire banker William Leatham, "
                  "writing in 1840, said it was impossible to tell how many of the bills in "
                  "circulation were &ldquo;due to actual business&rdquo; and how many were "
                  "&ldquo;fictitious and consists only of prolonged bills, that is, when a bill "
                  "of exchange is drawn for the purpose of taking up a current one before it "
                  "becomes due, and thus of creating fictitious capital by the manufacture of mere "
                  "means of circulation&rdquo;. In the accommodation preset A, on top of the "
                  "circle, accepts a second bill for £100 payable to B with no sale behind it, so "
                  "that B can have it discounted and raise money. The lab counts £100 of bills "
                  "with no sale behind them, and the settlement now needs £100 of cash where the "
                  "circle needed none: A owes B twice, once for cotton and once for nothing."),
            ("p", "Engels, in a long bracketed passage, tells what this came to in 1845 to 1847. "
                  "Goods were shipped to India and China not to be sold but so that bills could be "
                  "drawn against them and discounted; firms put their capital into railway shares "
                  "and then borrowed to carry on their own trade. The extracts Marx gathered after "
                  "the bracket fill in the detail: a Manchester newspaper of 1848 reports that the "
                  "drafts were commonly renewed when they fell due, and a Liverpool banker told the Lords' committee that he could "
                  "not tell by looking at a bill &ldquo;whether it represents products or "
                  "wind&rdquo;. Marx's dry contribution is a line from the banker James Gilbart, "
                  "who had written in 1834 that &ldquo;The cheapness of capital promotes "
                  "speculation, just as the cheapness of beer and meat promotes gluttony and "
                  "drunkenness&rdquo;."),
            ("p", "The distinction the chapter leans on, between bills that represent sales and "
                  "bills that represent nothing, was the core of the <em>real bills</em> "
                  "doctrine many bankers held: lend only against genuine trade and credit can "
                  "never be excessive. Henry Thornton objected to it in "
                  "1802, arguing that the rule limits nothing, because when prices rise every genuine sale "
                  "is a larger bill, and genuine bills can multiply with the boom they finance. "
                  "Several of Marx's extracts describe firms whose bills were all for real goods "
                  "bought too dear. The lab can count a bill as backed or unbacked; it "
                  "cannot say whether a backed bill will be paid."),
            ("p", "The chapter's title names fictitious capital, but Chapter 25 only shows it "
                  "being made. Marx explains what it is four chapters on. First, “Accumulation of "
                  "Money Capital and the Rate of Interest” asks what sets the price at which "
                  "these bills are bought and these loans are made."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "payments",
            "money_unit": "£",
            "preset": "bills",
            "presets": [
                {"id": "bills", "label": "Three bills of £100 in a circle, each for goods sold",
                 "goods": [{"name": "cotton", "value_hours": 200},
                           {"name": "yarn", "value_hours": 200},
                           {"name": "cloth", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 300, "payments_due": 300, "cancelling": 300,
                 "bills": [{"from": "A", "to": "B", "amount": 100, "backed": True},
                           {"from": "B", "to": "C", "amount": 100, "backed": True},
                           {"from": "C", "to": "A", "amount": 100, "backed": True}],
                 "expect": {"moNeeded": "£0", "moNetted": "£0", "moUnbacked": "£0"}},
                {"id": "discounted", "label": "B sells his bill on A to a bank before it falls due",
                 "goods": [{"name": "cotton", "value_hours": 200},
                           {"name": "yarn", "value_hours": 200},
                           {"name": "cloth", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 300, "payments_due": 300, "cancelling": 200,
                 "bills": [{"from": "A", "to": "bank", "amount": 100, "backed": True},
                           {"from": "B", "to": "C", "amount": 100, "backed": True},
                           {"from": "C", "to": "A", "amount": 100, "backed": True}],
                 "expect": {"moNeeded": "£100", "moNetted": "£100", "moUnbacked": "£0"}},
                {"id": "accommodation", "label": "The circle, plus a £100 bill A accepts for B with no sale behind it",
                 "goods": [{"name": "cotton", "value_hours": 200},
                           {"name": "yarn", "value_hours": 200},
                           {"name": "cloth", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 300, "payments_due": 400, "cancelling": 300,
                 "bills": [{"from": "A", "to": "B", "amount": 100, "backed": True},
                           {"from": "B", "to": "C", "amount": 100, "backed": True},
                           {"from": "C", "to": "A", "amount": 100, "backed": True},
                           {"from": "A", "to": "B", "amount": 100, "backed": False}],
                 "expect": {"moNeeded": "£100", "moNetted": "£100", "moUnbacked": "£100"}},
            ],
            "panel_title": "A circle of bills, settled",
            "panel_intro": (
                "Each bill runs from the party who pays to the party who is paid, and says whether a "
                "sale stands behind it. The goods are valued at 2 hours to the pound, so each lot is "
                "£100. The lab sets every party's bills against one another and adds the positive "
                "balances for the cash the settlement needs; the money-needed tile is Volume I's "
                "formula for the same day. Compare the discounted preset's table with the bills "
                "preset's: only the name on one bill has changed."
            ),
        }),
        "steps_title": "Settling a set of bills",
        "steps_intro": "Four steps for any set of bills falling due on one day.",
        "steps": [
            ("List the bills",
             "Write each bill as payer, payee and amount, and mark whether a sale of goods stands "
             "behind it."),
            ("Net each party",
             "For each party add what it receives and subtract what it pays. Bills that run in a "
             "circle cancel."),
            ("Add the positive balances",
             "The cash the settlement needs is the sum of the positive balances, which equals the "
             "sum of the negative ones."),
            ("Count the bills against nothing",
             "Add the bills with no sale behind them. They need settling like the others, but no "
             "goods were delivered for them."),
        ],
        "worked": {
            "title": "Three bills, then a bank, then a bill for nothing",
            "intro": [
                "A, B and C each sell £100 of goods on bills due the same day: A owes B, B owes C, "
                "C owes A. You want the cash the settlement needs, then the cash once B has sold "
                "his bill to a bank, then the cash once A has also accepted a bill for B with "
                "nothing sold.",
            ],
            "lines": [
                "circle:  A 0,  B 0,  C 0;  cash £0",
                "discounted:  A pays the bank instead of B",
                "nets:  A 0,  B −100,  C 0,  bank +100",
                "cash:  £100, the bank's money coming home",
                "accommodation:  A −100,  B +100,  C 0",
                "cash £100;  bills against nothing £100",
            ],
            "after": [
                "Three hundred pounds of goods changed hands and needed no cash at all while the "
                "bills cancelled. A bank's purchase of one bill brings £100 of real money into the "
                "settlement, and one bill drawn for nothing brings £100 of debt with no goods "
                "behind it.",
            ],
        },
        "quiz_title": "Bills, discounts and bills against nothing",
        "quiz": [
            {"q": "Four firms owe one another £50 each in a circle: A to B, B to C, C to D and D to "
                  "A, all due today. How much cash does the settlement need?",
             "a": ["£200", "£50", "£0", "£150"],
             "c": 2,
             "why": "Each firm receives £50 and pays £50, so every net balance is zero. Two hundred "
                    "pounds is the gross sum of the bills, which would be needed only if each were "
                    "paid separately in cash with nothing passed on."},
            {"q": "In the same circle, A sells its bill on D to a bank before it falls due, so D "
                  "pays the bank. How much cash does the settlement need?",
             "a": ["£0", "£50", "£100", "£200"],
             "c": 1,
             "why": "A now pays B £50 with nothing coming in, and the bank receives £50 from D: "
                    "the positive balances come to £50. The circle no longer closes among the "
                    "firms, so it cannot be £0; £100 counts both the bank's receipt and A's "
                    "payment as cash needed."},
            {"q": "On the account Engels gives in Part V, what happens when a bank discounts a "
                  "bill for a merchant?",
             "a": ["The bank lends the merchant additional capital",
                   "The bank buys the bill, and the merchant receives money for goods already sold",
                   "The bank creates new commodities",
                   "The merchant's debt to his supplier is cancelled"],
             "c": 1,
             "why": "Engels calls discounting &ldquo;purely one of buying and selling&rdquo;: the "
                    "bill passes to the bank and the money to the customer. The goods behind it "
                    "were delivered already; the merchant's own debts are untouched, and no "
                    "commodity is made."},
            {"q": "Why can a banker not keep accommodation bills out of his bill case, on the "
                  "evidence Marx quotes?",
             "a": ["Because they carry a lower rate of interest",
                   "Because a bill does not show whether goods stand behind it",
                   "Because the law obliged banks to discount every bill",
                   "Because accommodation bills were always paid on time"],
             "c": 1,
             "why": "The Liverpool banker said he could not tell by looking at a bill whether it "
                    "represented &ldquo;products or wind&rdquo;. Nothing in the extracts says such "
                    "bills were cheaper, legally compulsory or reliably paid; Leatham feared the "
                    "opposite."},
        ],
        "mistakes": [
            ("Thinking a bill of exchange is a loan of money",
             "A bill records goods already delivered and the day they are to be paid for; no money "
             "was lent when it was drawn. In the bills preset £300 of goods change hands on three "
             "bills and the settlement needs £0, which a set of money loans could not do. Even "
             "the discount is, in Engels' words, &ldquo;purely one of buying and selling&rdquo;: "
             "B sells his claim to the bank, and the £100 the settlement then needs is the bank's "
             "purchase money coming home."),
            ("Treating every bill as backed by goods",
             "The accommodation preset adds a bill that looks like the others and has no sale "
             "behind it. It adds £100 to the bills against nothing and turns a settlement that "
             "needed nothing into one that needs £100. Leatham's prolonged bills, drawn to pay "
             "earlier bills, are of this kind."),
            ("Reading the title as Marx's theory of fictitious capital",
             "Chapter 25 shows fictitious capital being made, by bills drawn for nothing; what it "
             "is, and how its price is set, is Chapter 29's subject. Much of this chapter is "
             "extracts and an editor's narrative, not argument."),
        ],
        "standard": (
            "Finish when you can settle a set of bills and count the bills against nothing.",
            "Given bills between named parties, each marked as backed by a sale or not, compute "
            "each party's net balance, the cash the settlement needs and the sum of bills with no "
            "sale behind them, and again when one bill has been sold to a bank."
        ),
        "note": (
            "The lab sets bills off as if all fell due on one day and were cleared together, "
            "which is the most money credit can save; in fact bills fall due on different days "
            "and a merchant must hold a reserve against the gap, which Chapter 30 discusses. "
            "Whether a bill is backed is entered by hand: the lab cannot tell a sound bill from a "
            "bill for goods that will never sell. The bills and their amounts are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 3, l. 3759 (Overstone, 3722); l. 3759 (Marx's reply).
    # Inline: l. 3753 (the 1847 bank rates), l. 3775 (question 3729),
    # l. 3727 (Tooke, 5451), l. 3717 (Gurney, 1763), l. 3751 (one form
    # rose), l. 3733 and l. 3737 (Norman), l. 3721 (the dividend).
    {
        "slug": "accumulation-of-money-capital",
        "title": "Accumulation of Money Capital and the Rate of Interest",
        "module": "Chapter 26 · Accumulation of Money-Capital. Its Influence on the Rate of Interest",
        "one_line": "A rise in the rate of interest comes out of the same profit, so it cuts profit of enterprise point for point, and it can rise while real capital lies unsold.",
        "summary": (
            "Chapter 26 is mostly the cross-examination of two bankers before Parliament, Norman "
            "and Lord Overstone, who held that the rate of interest measures the scarcity of "
            "capital in general. Compute what a rise in the rate of interest does to the profit "
            "left to a borrowing industrialist at a fixed rate of profit, from the Bank's 3% of "
            "January 1847 to its 10% of November."
        ),
        "key": [
            "profit = capital × rate of profit",
            "interest = capital borrowed × rate",
            "enterprise = profit − interest",
            "normally 0 < interest < profit",
            "dear money is not scarce capital",
        ],
        "key_label": "Interest against profit",
        "concepts_intro": (
            "The chapter's title promises an analysis of how money capital accumulates. What it "
            "contains is an argument with the most powerful banker of the day about what the rate "
            "of interest is the price of."
        ),
        "concepts": [
            ("Money capital and real capital",
             "Money capital is capital held as money, to be lent. Real capital is the means of "
             "production and the commodities that money can buy. Overstone treated a demand for "
             "the first as a demand for the second."),
            ("Interest out of profit",
             "Interest is paid out of the profit made with borrowed capital. With the rate of "
             "profit fixed, every point added to the rate of interest is a point taken from the "
             "borrower's profit of enterprise."),
            ("The value of capital",
             "Overstone's phrase for what the rate of interest measures. Marx's complaint is that "
             "it means the rate of interest itself in one answer and the rate of profit in the "
             "next."),
        ],
        "read_title": "Overstone's evidence first, then Marx's reply",
        "read_intro": (
            "The passage is Overstone's own answer to the Bank Committee of 1857, as the Kerr "
            "text gives it in translation from the German edition. Marx's comment follows it in "
            "the same paragraph."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 26.</strong> &ldquo;The conception that the "
                  "business profit is destroyed by raising the rate of interest is highly "
                  "erroneous. In the first place, a rise in the rate of interest is rarely of long "
                  "duration; in the second place, if it is of long duration and considerable, it "
                  "is in the nature of things a rise in the value of capital, and why does the "
                  "value of capital rise? Because the rate of profit has risen.&rdquo;"),
            ("p", "You know this argument in its modern form: when a central bank raises its rate, "
                  "someone always says that rates are high because the economy is strong. The man "
                  "saying it here is Samuel Jones Loyd, Lord Overstone, banker, chief theorist of "
                  "the Bank Act of 1844, and one of the richest men in England. His position "
                  "deserves to be put at its strongest. Interest is the price of capital. Capital "
                  "is the stock of things used in production. When trade expands, as English commerce "
                  "had, Overstone told the committee, from 45 to 120 million pounds in the thirteen "
                  "years of the Act, more of those things are "
                  "wanted, their &ldquo;value&rdquo; rises, and the rate of interest records it. A "
                  "high rate is then a sign of prosperity, not a burden on it."),
            ("p", "Marx's reply is in the next sentence: &ldquo;the rate of profit may hold itself "
                  "at a high level for a long time, and yet the industrial capitalist's profit may "
                  "fall and the rate of interest rise to a point where it swallows the greater "
                  "portion of the profit.&rdquo; Interest and profit of enterprise are two shares "
                  "of one profit, as Merchant's Capital and Interest showed, and nothing about a "
                  "high rate of profit stops the first share from growing at the expense of the "
                  "second."),
            ("p", "The lab does that division. A manufacturer works £100 of borrowed capital at "
                  "an average rate of profit of 10%; the committee's examiner put the average rate at "
                  "&ldquo;from 7 to 10%&rdquo;, and the figure is illustrative. In the low preset "
                  "interest is 3%, where the Bank's rate began in January 1847: £3 goes to the lender "
                  "and £7 stays as profit of enterprise. In the high preset interest is 8%, near the "
                  "top of the examiner's question, &ldquo;from 2% to 7 or 8%&rdquo;: £8 to the lender, "
                  "£2 left. In the crisis preset it is 10%, where the Bank's rate peaked in November "
                  "1847, and profit of enterprise is £0. The rate of profit never moved."),
            ("p", "This is not hypothetical. Tooke told a committee of Parliament that in the "
                  "Warwickshire and Staffordshire metal trades &ldquo;very many orders were rejected "
                  "in 1847, because the rate of interest, which the manufacturer had to pay for "
                  "discounting his bills of exchange, would have more than swallowed his entire "
                  "profit&rdquo;. Overstone's answer to the examiner was that businessmen &ldquo;will "
                  "not pay a rate of discount, which takes away most of their profits "
                  "beforehand&rdquo;. Marx's bracketed retort: they pay it when profit is large "
                  "&ldquo;because they are willing, and when profit is low, they pay the discount "
                  "because they must&rdquo;."),
            ("p", "What then did the rate of interest measure in 1847? The rate rose through the "
                  "year to 10%, and by October, a Liverpool banker testified, goods were "
                  "&ldquo;almost unsaleable&rdquo;. The warehouses were full; what firms lacked was "
                  "the means to pay bills falling due. Samuel Gurney, the Quaker bill broker, "
                  "said as much: &ldquo;I do not believe that it was a lack of capital, which "
                  "drove the rate of interest so high; it was the alarm, the difficulty of "
                  "obtaining bank notes.&rdquo; Marx puts it as a change of form: &ldquo;The "
                  "value of capital in one form rose, because the value of capital in the other "
                  "forms fell.&rdquo; Money capital grew dear because commodity capital could not "
                  "be turned into money."),
            ("p", "The other banker, George Warde Norman, a director of the Bank of England, "
                  "offers the chapter's most quoted exchange. The rate of interest, he argued, is "
                  "set by the supply of and demand for capital, and capital is &ldquo;All "
                  "commodities used in production.&rdquo; So &ldquo;There would be interest even "
                  "if no money existed.&rdquo; Marx answers him flatly: &ldquo;If there were no "
                  "money at all, there would certainly be no general rate of interest.&rdquo; A "
                  "single rate of interest for borrowers in every trade, whatever the state of "
                  "the cotton or the iron market, is a price of money capital, set by the supply of and "
                  "demand for money capital, which need not follow the market for cotton or iron."),
            ("p", "Marx is at his most sarcastic in this chapter, and he lets the committee's examiners make "
                  "his jokes. Disraeli asks a director of the Bank what its dividend was in 1844: "
                  "7%. And in 1847, the year of the crisis? &ldquo;Nine per cent.&rdquo; Overstone, "
                  "pressed on what exactly he means by capital, finally declines to answer, "
                  "saying the question is better suited &ldquo;for the study room of a "
                  "scientist than for this committee room&rdquo;."),
            ("p", "In the middle of the chapter Engels breaks in with a passage of his own, "
                  "marked with his initials, on the confusion underneath the whole argument. A "
                  "banker, he says, comes to think every payment he makes is a loan of capital. "
                  "But a customer who borrows against good securities receives money and no "
                  "capital, since he has deposited more value than he receives, and a customer "
                  "who discounts a bill has sold it. Only an unsecured advance gives a customer "
                  "capital he did not have. Engels adds that Overstone, who had been his own "
                  "firm's banker in Manchester, &ldquo;very rarely advanced any funds without "
                  "collateral&rdquo;."),
            ("p", "Whether Marx or Overstone was right about 1847 is still argued in the language "
                  "of the time's two schools. Overstone's descendants say a high rate rations "
                  "scarce real resources; the other side, Marx's included, says it often prices "
                  "nothing but the scramble for means of payment. The lab settles neither. It "
                  "shows only that, with the rate of profit fixed, a rise in the rate of interest "
                  "comes out of profit of enterprise pound for pound."),
            ("p", "Chapter 26 asked what interest does to the industrialist. “The Role of Credit "
                  "in Capitalist Production” asks what credit does to the industrialist himself, "
                  "once his business is owned by shareholders."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "bounds",
            "money_unit": "£",
            "preset": "low",
            "presets": [
                {"id": "low", "label": "£100 borrowed at 10% profit; interest at January 1847's 3%",
                 "capital": 100, "profit_rate": "1/10", "interest_rate": "3/100",
                 "expect": {"inInterest": "£3", "inEnterprise": "£7", "inBound": "0 < 3% < 10%"}},
                {"id": "high", "label": "The same £100; interest at 8%",
                 "capital": 100, "profit_rate": "1/10", "interest_rate": "8/100",
                 "expect": {"inInterest": "£8", "inEnterprise": "£2", "inBound": "0 < 8% < 10%"}},
                {"id": "crisis", "label": "The same £100; interest at November 1847's 10%",
                 "capital": 100, "profit_rate": "1/10", "interest_rate": "1/10",
                 "expect": {"inInterest": "£10", "inEnterprise": "£0", "inBound": "breached: 10% ≥ 10%"}},
            ],
            "panel_title": "Interest out of a fixed profit",
            "panel_intro": (
                "The capital, all of it borrowed, the average rate of profit and the rate of interest "
                "go in. The lab computes the profit, the interest and what is left as profit of "
                "enterprise, and checks the rate of interest against the bounds 0 and the rate of "
                "profit. Move only the rate of interest and watch which tile moves with it."
            ),
        }),
        "steps_title": "Dividing a profit between lender and borrower",
        "steps_intro": "Four steps for a capital worked with borrowed money.",
        "steps": [
            ("Compute the profit",
             "Multiply the capital employed by the average rate of profit."),
            ("Compute the interest",
             "Multiply the capital borrowed by the rate of interest. Here all of it is borrowed."),
            ("Subtract",
             "Profit of enterprise is the profit less the interest. It falls by exactly what the "
             "interest rises."),
            ("Check the bounds",
             "Normally the rate of interest lies above 0 and below the rate of profit. At or above "
             "the rate of profit the interest is no longer paid out of this profit."),
        ],
        "worked": {
            "title": "January to November 1847, at a fixed rate of profit",
            "intro": [
                "A manufacturer borrows all of a £100 capital and makes the average 10% on it. You "
                "want his profit of enterprise as the Bank's rate goes from 3% to 8% and then 10%.",
            ],
            "lines": [
                "profit:  £100 · 1/10 = £10",
                "at 3%:  interest £3,  enterprise £10 − £3 = £7",
                "at 8%:  interest £8,  enterprise £2",
                "at 10%:  interest £10,  enterprise £0",
            ],
            "after": [
                "Profit stayed at £10 throughout. Overstone's &ldquo;value of capital&rdquo; rose "
                "from 3 to 10, and everything it gained came out of the share that was left to the "
                "man who employed the capital.",
            ],
        },
        "quiz_title": "Interest, profit and the value of capital",
        "quiz": [
            {"q": "A firm borrows £200 at 4% and makes 12% on it. How much profit of enterprise is "
                  "left?",
             "a": ["£24", "£8", "£16", "£32"],
             "c": 2,
             "why": "Profit is `200 · 12/100 = 24` and interest `200 · 4/100 = 8`, so `24 − 8 = 16`. "
                    "Twenty-four is the whole profit, eight the interest, and thirty-two adds them."},
            {"q": "With the rate of profit fixed at 10%, the rate of interest rises from 3% to 8%. "
                  "What happens to profit of enterprise per £100?",
             "a": ["It falls from £7 to £2",
                   "It rises, because a higher rate shows a higher rate of profit",
                   "It stays at £7",
                   "It falls from £10 to £8"],
             "c": 0,
             "why": "The profit stays £10 and interest takes £3 and then £8, leaving £7 and then £2. "
                    "That a high rate shows a high rate of profit is Overstone's claim, and the "
                    "question fixes the rate of profit. £10 and £8 are the profit and the new "
                    "interest."},
            {"q": "On the evidence Marx quotes, what was scarce in October 1847?",
             "a": ["Commodities, which were unobtainable at any price",
                   "Means of payment, while goods lay almost unsaleable",
                   "Labour-power, because of the railway works",
                   "Nothing; the high rate reflected a high rate of profit"],
             "c": 1,
             "why": "The witnesses describe goods &ldquo;almost unsaleable&rdquo; and, in Gurney's "
                    "words, &ldquo;the difficulty of obtaining bank notes&rdquo;. Nothing in the "
                    "chapter says goods or labour were scarce, and the last option is Overstone's "
                    "view, which the chapter rejects."},
            {"q": "Norman said there would be interest even if no money existed. What is Marx's "
                  "reply?",
             "a": ["That interest is a sin and should be abolished",
                   "That without money there would be no general rate of interest",
                   "That interest is the wage of the banker's labour",
                   "That Norman was right about commodities but wrong about gold"],
             "c": 1,
             "why": "Marx writes that if there were no money at all &ldquo;there would certainly be "
                    "no general rate of interest&rdquo;. He makes no moral argument here, does not "
                    "call interest a wage, and does not concede Norman's point."},
        ],
        "mistakes": [
            ("Thinking a high rate of interest shows a scarcity of capital in general",
             "It is Overstone's view: interest is the price of capital, so dear money means scarce "
             "capital. In 1847 the rate rose to 10% while goods were &ldquo;almost "
             "unsaleable&rdquo; and warehouses full; Gurney put it down to &ldquo;the alarm, the "
             "difficulty of obtaining bank notes&rdquo;. In the crisis preset the rate of profit "
             "is still 10% and the capital is the same £100; what moved is the price of money "
             "capital, which took all £10 of the profit."),
            ("Treating a high rate of interest as a sign of high profits for the borrower",
             "The rate of profit may stay high while profit of enterprise vanishes. In the high "
             "preset the rate of profit is 10% and the borrower keeps £2 of every £10."),
            ("Reading every bank payment as a loan of capital",
             "Engels' interpolation separates the cases: an advance against securities gives money "
             "but no new capital, a discount is a sale, and only an unsecured advance adds to the "
             "borrower's capital."),
        ],
        "standard": (
            "Finish when you can compute profit of enterprise as the rate of interest moves.",
            "Given a capital, the share of it borrowed, the average rate of profit and a rate of "
            "interest, compute the interest and the profit of enterprise, state whether the rate "
            "lies between 0 and the rate of profit, and compute both again at a new rate of "
            "interest."
        ),
        "note": (
            "The lab holds the rate of profit fixed so that only the division moves. In 1847 the "
            "rate of profit fell as well: the interest rose, Marx writes, &ldquo;because the "
            "profits decreased and the money-values of commodities fell enormously&rdquo;. The "
            "lab does not model a falling profit. The 10% rate of profit is "
            "illustrative; the 3% and 10% are the two ends of the Bank of England's rate as the "
            "chapter lists it month by month for 1847, 3 to 3½% in January and 7 to 10% in "
            "November."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 3, l. 3899-3901 (manager and money-capitalist); l. 3913
    # (abolition within capitalist production). Inline: l. 3901 (the
    # dividend as interest), l. 3905-3907 (enterprises that yield only
    # interest), l. 3909 (Engels: the Alkali Trust), l. 3917 (others save
    # for him), l. 3921 (co-operative factories), l. 3931 (swindlers and
    # prophets).
    {
        "slug": "the-role-of-credit",
        "title": "The Role of Credit in Capitalist Production",
        "module": "Chapter 27 · The Role of Credit in Capitalist Production",
        "one_line": "In a stock company the owners receive the whole profit as if it were interest on their shares, and the man who runs the business is paid a wage.",
        "summary": (
            "Chapter 27 lists what credit does: it equalises profits, cheapens circulation, forms "
            "stock companies and puts other people's capital at the disposal of a few. Compute a "
            "stock company's profit paid out as dividend and its manager's salary, set beside an "
            "owner who runs his own capital and a dealer who works mostly with borrowed money."
        ),
        "key": [
            "dividend = profit − manager's salary",
            "a dividend looks like interest on shares",
            "a manager's salary looks like a wage",
            "borrowed capital, the borrower's profit",
            "credit commands others' capital",
        ],
        "key_label": "The stock company in five lines",
        "concepts_intro": (
            "Engels says this chapter came almost whole from Marx's manuscript. It is short, a "
            "numbered list, and it contains some of the most quoted sentences in Volume III."
        ),
        "concepts": [
            ("The stock company",
             "A business whose capital is put up by shareholders who do not run it. It can be far "
             "larger than any one fortune, as railways and canals had to be."),
            ("Owner and manager",
             "The two sides of the old capitalist, split between two people: the owner of capital, "
             "who receives a dividend, and the functioning manager, who is paid a salary."),
            ("Command of others' capital",
             "Credit lets a dealer work with capital that is mostly borrowed, so that the risk he "
             "runs is, in Marx's phrase, social property and not his own."),
        ],
        "read_title": "The split in the capitalist, then Marx's verdict on it",
        "read_intro": (
            "The passage comes from the chapter's third point, on stock companies. The verdict "
            "comes a page later, after a bracketed insertion by Engels."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 27.</strong> &ldquo;Transformation of the actually "
                  "functioning capitalist into a mere manager, an administrator of other people's "
                  "capital, and of the owners of capital into mere owners, mere "
                  "money-capitalists.&rdquo;"),
            ("p", "If you have a pension or a fund that holds shares, you are one of these "
                  "&ldquo;mere owners&rdquo;. You will never meet the people who run the firms "
                  "whose dividends you receive, and they are paid salaries, like you. In Marx's "
                  "day the stock company was new outside railways, canals, banks and insurance, "
                  "and he saw in it the figure of Volume I's capitalist splitting in two."),
            ("p", "Read the rest of the point. The manager's salary &ldquo;is, or is supposed to "
                  "be, a mere wage of a certain kind of skilled labor, the price of which is "
                  "regulated in the labormarket&rdquo;. The shareholders' dividend may contain both "
                  "interest and profit of enterprise, the whole profit, but it is received "
                  "&ldquo;only in the form of interest, that is, in the form of a mere compensation "
                  "of the ownership of capital&rdquo;. In Merchant's Capital and Interest the profit "
                  "of a borrowed capital split into interest for the owner and profit of enterprise "
                  "for the man who ran it. Here the man who runs it is an employee, and nothing is "
                  "left that could be called profit of enterprise."),
            ("p", "The lab makes that a sum. In the stock-company preset £1,000 of shares earn "
                  "£220 at a rate of profit of 22%; the manager is paid a salary of £20, and the "
                  "lab counts the remaining £200 as a dividend at 20% on the shares, the "
                  "&ldquo;interest&rdquo; on them. Profit of enterprise is £0. In the owner-managed "
                  "preset an owner works his own £1,000 at 20%: reckoned the way Chapter 23 reckons "
                  "it, £50 is interest on his capital at 5% and £150 is profit of enterprise, but "
                  "both are his. In the leveraged preset a dealer works £1,000 of which £800 is "
                  "borrowed at 5%: the lenders get £40, he keeps £160, and on his own £200 that is "
                  "80%. The figures are illustrative."),
            ("p", "That last preset is the chapter's fourth point. Credit gives the individual "
                  "&ldquo;absolute command of the capital of others&rdquo;, and with it of the "
                  "labour of others, &ldquo;within certain limits&rdquo;. Two of the old defences of "
                  "profit go with it. The capitalist who saved his capital? &ldquo;Equally stale "
                  "becomes the phrase concerning the origin of capital from saving, for what he "
                  "demands is precisely that others shall save for him.&rdquo; And the "
                  "speculating merchant's risk: &ldquo;What the speculating wholesale merchant risks "
                  "is social property, not his own.&rdquo;"),
            ("p", "<strong>Volume III, Chapter 27.</strong> &ldquo;This is the abolition of the "
                  "capitalist mode of production within capitalist production itself, a "
                  "self-destructive contradiction, which represents on its face a mere phase of "
                  "transition to a new form of production.&rdquo;"),
            ("p", "This is the sentence the chapter is remembered for, and it is worth reading "
                  "slowly. The &ldquo;abolition&rdquo; is of capital as private property run by its "
                  "owner: the means of production are already held in common, by thousands of "
                  "shareholders, and run by hired staff. But the same paragraph says what it "
                  "brings with it: &ldquo;a new aristocracy of finance, a new sort of parasites in "
                  "the shape of promoters, speculators and merely nominal directors&rdquo;. Marx "
                  "calls the stock company &ldquo;private production without the control of private "
                  "property&rdquo;, and sets beside it the workers' co-operative factories, where "
                  "the opposition of capital and labour is overcome &ldquo;only in the form of "
                  "making the associated laborers their own capitalists&rdquo;."),
            ("p", "Engels added a bracketed paragraph thirty years later, on what had happened "
                  "since: cartels fixing output, and then trusts. His example is the United Alkali "
                  "Trust, which brought more than thirty works under one management, with shares of "
                  "about £5 million given to the former owners and £1 million of working capital "
                  "raised from the public. Marx also notes, in passing, that a company that pays only "
                  "interest can go on operating, so such firms &ldquo;do not necessarily come under the regulation of "
                  "the average rate of profit&rdquo;, and he says outright that this &ldquo;is one of "
                  "the causes, which stem the fall of the rate of profit&rdquo;."),
            ("p", "The standard objection came in 1932, when Adolf Berle and Gardiner Means "
                  "showed how widely ownership and control had separated in American corporations "
                  "and argued the opposite moral: that managers, unchecked by scattered owners, "
                  "could run firms in their own interest. Later economists made this the "
                  "principal-agent problem, and executive pay tied to profits is the attempt to "
                  "solve it. On that account the manager is not simply a wage earner. Marx's "
                  "chapter takes the salary at its face, a wage set in the labour market, and the "
                  "lab does the same."),
            ("p", "Marx ends with credit's double character. It drives production to its limits "
                  "and speeds the crises, and it is also &ldquo;a transition to a new mode of "
                  "production&rdquo;. That is why, he says, its great promoters &ldquo;from Law to "
                  "Isaac Pereire&rdquo; have the &ldquo;pleasant character of swindlers and "
                  "prophets&rdquo;."),
            ("p", "So far credit has been about who owns and who runs. “Medium of Circulation and "
                  "Capital” asks how much money a business economy needs, and whether it matters "
                  "that some of it is capital."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "split",
            "money_unit": "£",
            "preset": "stock-company",
            "presets": [
                {"id": "stock-company", "label": "£1,000 of shares earning 22%, a hired manager at £20, a 20% dividend",
                 "capital": 1000, "profit_rate": "11/50", "interest_rate": "1/5",
                 "principal": 1000, "manager_salary": 20,
                 "expect": {"inInterest": "£200", "inEnterprise": "£0"}},
                {"id": "owner-managed", "label": "An owner works his own £1,000 at 20%, with interest reckoned at 5%",
                 "capital": 1000, "profit_rate": "1/5", "interest_rate": "1/20",
                 "principal": 1000, "manager_salary": 0,
                 "expect": {"inInterest": "£50", "inEnterprise": "£150"}},
                {"id": "leveraged", "label": "A dealer works £1,000 at 20%, £800 of it borrowed at 5%",
                 "capital": 1000, "profit_rate": "1/5", "interest_rate": "1/20",
                 "principal": 800, "manager_salary": 0,
                 "expect": {"inInterest": "£40", "inEnterprise": "£160"}},
            ],
            "panel_title": "Who receives the profit",
            "panel_intro": (
                "The capital employed, the rate of profit, the capital that is lent or held as shares, "
                "the rate paid on it and any manager's salary go in. The lab pays the salary and the "
                "interest out of the profit and prints what is left as profit of enterprise. In the "
                "stock-company preset the &ldquo;interest&rdquo; is the dividend on the shares."
            ),
        }),
        "steps_title": "Dividing a company's profit",
        "steps_intro": "Four steps for a capital that is owned by one party and run by another.",
        "steps": [
            ("Compute the profit",
             "Multiply the capital employed by the rate of profit."),
            ("Pay the manager",
             "Take out the manager's salary, counted as the wage of a kind of skilled labour."),
            ("Pay the owners",
             "Multiply the capital the owners or lenders put up by the rate they are paid. In a "
             "stock company that rate is the dividend on the shares."),
            ("See what is left",
             "Profit of enterprise is whatever remains. When the dividend takes all of it, the "
             "whole profit has taken the form of interest."),
        ],
        "worked": {
            "title": "A stock company, an owner and a borrower",
            "intro": [
                "Take the three presets. You want, in each, what goes to the owners of the capital "
                "and what is left as profit of enterprise.",
            ],
            "lines": [
                "company:  £1000 · 22% = £220;  salary £20",
                "dividend:  £1000 · 20% = £200;  enterprise £0",
                "owner:  £200 profit = £50 interest + £150",
                "dealer:  £200 profit;  interest £800 · 5% = £40",
                "dealer keeps £160 on £200 of his own",
            ],
            "after": [
                "In the company the whole profit leaves as dividend and the man who runs it earns a "
                "salary; in the dealer's business most of the capital is other people's and most of "
                "the profit is his.",
            ],
        },
        "quiz_title": "Owners, managers and borrowed capital",
        "quiz": [
            {"q": "A company's £5,000 of shares earn a profit of £600. Its manager is paid £100 "
                  "and the rest is paid out. What is the dividend, as a rate on the shares?",
             "a": ["12%", "10%", "2%", "14%"],
             "c": 1,
             "why": "The dividend is `600 − 100 = 500`, and `500/5000 = 1/10`. Twelve per cent is "
                    "the profit before the salary, 2% is the salary as a share of the capital, and "
                    "14% adds the two."},
            {"q": "On the chapter's account, what form does a shareholder's dividend take, even "
                  "when it contains the whole profit?",
             "a": ["The form of a wage",
                   "The form of interest, a compensation for owning capital",
                   "The form of ground rent",
                   "The form of profit of enterprise, earned by supervising"],
             "c": 1,
             "why": "Marx writes that the total profit is received &ldquo;only in the form of "
                    "interest&rdquo;. The wage is the manager's, the shareholder supervises nothing, "
                    "and rent does not enter the chapter's account of the company."},
            {"q": "A dealer works £1,000 at 15%, of which £900 is borrowed at 5%. What does he make "
                  "on his own £100?",
             "a": ["15%", "105%", "45%", "150%"],
             "c": 1,
             "why": "Profit is £150 and interest `900 · 5/100 = 45`, so he keeps £105 on £100 of his "
                    "own. Fifteen per cent is the rate on the whole capital; 150% forgets the "
                    "interest, and 45% is the interest alone, reckoned on his own £100."},
            {"q": "What does Marx mean by calling the stock company &ldquo;the abolition of the "
                  "capitalist mode of production within capitalist production itself&rdquo;?",
             "a": ["That stock companies pay no profit",
                   "That capital is no longer owned and run by one private capitalist, though it is still capital",
                   "That workers own the shares",
                   "That the state has taken over production"],
             "c": 1,
             "why": "The means of production are held by many owners and run by hired managers, "
                    "&ldquo;private production without the control of private property&rdquo;, and "
                    "the profit is still paid out as dividends. Workers owning the means of "
                    "production is the co-operative factory, which Marx treats separately; the "
                    "state is mentioned only as challenged to interfere."},
        ],
        "mistakes": [
            ("Thinking that in a stock company the profit of enterprise stays with the people who run it",
             "In the stock-company preset the profit is £220, the manager is paid a £20 salary, and "
             "the remaining £200 goes to the shareholders as a 20% dividend: profit of enterprise "
             "is £0. Marx's point is that the whole profit takes &ldquo;the form of "
             "interest&rdquo;, and the function of the old capitalist is paid as &ldquo;a mere wage "
             "of a certain kind of skilled labor&rdquo;. Whether managers in fact take more, as "
             "Berle and Means argued, is a question about real firms the lab does not settle."),
            ("Reading the &ldquo;abolition&rdquo; as the end of capitalism",
             "Marx calls it a &ldquo;transition&rdquo; that stays &ldquo;ensnared in the boundaries "
             "of capitalism&rdquo;. Profit is still paid out, now to shareholders, and the same "
             "page describes a &ldquo;new aristocracy of finance&rdquo;."),
            ("Treating borrowed capital as the borrower's risk alone",
             "In the leveraged preset £800 of the £1,000 is other people's. If the business fails, "
             "it is chiefly their capital that is lost; the dealer has £200 at stake and keeps "
             "£160 of the profit when it succeeds."),
        ],
        "standard": (
            "Finish when you can divide a company's profit into salary, dividend and what is left.",
            "Given a capital, its rate of profit, the capital put up by owners or lenders, the "
            "rate paid on it and a manager's salary, compute the dividend or interest and the "
            "profit of enterprise, and the borrower's return on his own capital."
        ),
        "note": (
            "The lab counts the manager's salary out of profit and treats it as a wage, as the "
            "chapter does; it cannot see bonuses, share options or any other route by which a "
            "manager might share the profit. The company, the owner and the dealer are "
            "illustrative; the Alkali Trust's £5 million and £1 million are Engels' figures."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 3, l. 3941 (money-form of revenue and of capital); l. 3966
    # (the mass of currency). Inline: l. 3937 (the distinction), l. 3953
    # (the five pound note), l. 3958 (the banker issuing notes), l. 3976,
    # l. 3982 (prosperity), l. 3992 (Fullarton), l. 4029 (the loan
    # remains), l. 4058 (titles that are no capital).
    {
        "slug": "medium-of-circulation-and-capital",
        "title": "Medium of Circulation and Capital: Tooke and Fullarton",
        "module": "Chapter 28 · The Medium of Circulation (Currency) and Capital. Tooke's and Fullarton's Conception",
        "one_line": "Money spent from wages and money paid between capitalists are the same notes and obey the same law; how many are needed depends on prices and velocity, not on whether they are capital.",
        "summary": (
            "Thomas Tooke and John Fullarton, the leading critics of the Bank Act, drew a line "
            "between currency, the notes in the public's pockets, and capital, the funds bankers "
            "lend. Marx says the line is drawn in the wrong place. Sort payments into the "
            "circulation of revenue and the transfer of capital, compute the notes each needs at "
            "a given velocity, and see that the answer does not depend on the label."
        ),
        "key": [
            "revenue: wages and income spent in shops",
            "capital: payments between capitalists",
            "notes needed = sum of prices / velocity",
            "the same law for both kinds",
            "a loan is not an issue of notes",
        ],
        "key_label": "Currency and capital",
        "concepts_intro": (
            "Engels says this chapter had to be rearranged in places; apart from a bracketed "
            "passage of his on the forms a bank loan can take and a one-line gloss on a drain "
            "of gold, the text is Marx's. It "
            "is an argument with allies: Tooke and Fullarton were right against the Currency "
            "School, and Marx thinks they were right for a confused reason."
        ),
        "concepts": [
            ("Circulation of revenue",
             "Money spent by consumers, mostly wages, at the shops. It circulates as coin and "
             "small notes, and its quantity grows in good times as employment and prices rise."),
            ("Transfer of capital",
             "Money paid between capitalists: the manufacturer to the merchant, the merchant to "
             "the importer. It is mostly means of payment, and credit lets much of it be settled "
             "without money at all."),
            ("Currency and capital",
             "Tooke's pair of terms. Marx's objection is that the same note serves in both "
             "circulations, and what distinguishes them is the money-form of revenue against the "
             "money-form of capital."),
        ],
        "read_title": "Marx's distinction first, then the law that governs both sides",
        "read_intro": (
            "The passage comes from the chapter's first page, where Marx restates Tooke's "
            "distinction in his own terms. The law comes from the second section."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 28.</strong> &ldquo;The difference, then, is in fact "
                  "that between the money-form of revenue and the money-form of capital, but not "
                  "that between currency and capital, for a certain quantity of money circulates in "
                  "the transactions between dealers as well as those between consumers and "
                  "dealers.&rdquo;"),
            ("p", "Think of a five-pound note in your wallet. You were paid it as wages, you spend "
                  "it at a shop, the shopkeeper banks it, and next week the bank pays it out to a "
                  "manufacturer to meet his wage bill. For you it was income, for the shopkeeper a "
                  "return of his capital, for the manufacturer capital advanced. Marx's example is the "
                  "same note: &ldquo;the same price of money, for instance a five pound note, "
                  "passes from one sphere to the other and performs alternately both "
                  "functions&rdquo;. (The word &ldquo;price&rdquo; makes no sense there: what passes "
                  "from one sphere to the other is a single note, and earlier in the same "
                  "chapter Marx speaks of &ldquo;pieces of individual coin&rdquo;. It reads as a slip, "
                  "most likely for &ldquo;piece&rdquo;.)"),
            ("p", "Who were Tooke and Fullarton? Thomas Tooke, a Russia merchant turned historian "
                  "of prices, and John Fullarton, a banker who had worked in India, led the "
                  "<em>Banking School</em> against Overstone's Currency School in the 1840s. "
                  "They argued, from the record, that a bank cannot force notes into circulation: "
                  "the public holds what trade needs and returns the rest. Marx agrees, and “The "
                  "Medium of Circulation in the Credit System” is his version of it. But Tooke also "
                  "divided money into "
                  "&ldquo;currency&rdquo;, the notes in the public's pockets, and &ldquo;capital&rdquo;, "
                  "the funds bankers lend, and that, Marx says, &ldquo;indiscriminately confounds&rdquo; "
                  "three different things."),
            ("p", "Read the passage again. Marx keeps a real distinction, between money that "
                  "realises revenue, wages and incomes spent on consumption, and money that "
                  "transfers capital between capitalists. What he denies is that the distinction "
                  "makes one kind of money &ldquo;currency&rdquo; and the other &ldquo;capital&rdquo;, "
                  "since both are money circulating. Tooke's terms come, he says, from the "
                  "standpoint of a banker who issues notes: the notes in the public's hands cost him "
                  "only &ldquo;paper and printing&rdquo;, while what he lends out of his own funds "
                  "is his capital."),
            ("p", "<strong>Volume III, Chapter 28.</strong> &ldquo;Whether the money so serving "
                  "represents capital or revenue for the paying or receiving party, is immaterial, "
                  "and does not alter the matter in any way. Its mass is simply determined by its "
                  "function as a medium of purchase and payment.&rdquo;"),
            ("p", "That is the law of Volume I, Chapter 3, and the lab computes it: the money "
                  "needed is the sum of prices divided by the number of times each note changes "
                  "hands. In the revenue preset a week's wages of £1,000 are spent in shops and "
                  "each note serves 10 times: £100 of notes. In the capital preset £1,000 of "
                  "payments pass between manufacturers and merchants, also at 10 turns: £100. "
                  "The label changed and the notes did not. In the mixed preset both go on at "
                  "once, £2,000 of payments at 10 turns, and need £200. In the credit preset the "
                  "£1,000 between capitalists moves at 25 turns, because, as Marx says, between "
                  "capitalist and capitalist the velocity &ldquo;is regulated directly by "
                  "credit&rdquo;: it needs £40. The quantities are illustrative."),
            ("p", "The two circulations do move differently over the cycle, and that is the grain "
                  "of truth Marx finds in Tooke. In prosperity the circulation of revenue "
                  "&ldquo;increases decidedly&rdquo;, with fuller employment and higher prices, "
                  "while credit lets the payments between capitalists grow with relatively less "
                  "money. In a crisis it is the other way round: the shops' circulation shrinks and "
                  "the demand for means of payment between capitalists grows, &ldquo;in proportion "
                  "as credit decreases&rdquo;."),
            ("p", "Fullarton held that &ldquo;A demand for capital on loan and a demand for "
                  "additional circulation are quite distinct things, and not often found "
                  "associated.&rdquo; He had the Bank of England's own figures on his side: when "
                  "its loans rose its notes in circulation often fell. Marx accepts the figures and "
                  "explains them. The notes a bank lends come back as deposits or as payments of "
                  "bills: &ldquo;The loan remains, and the currency, if not wanted, finds its way "
                  "back to the issuer&rdquo;, in Fullarton's own phrase. The loan and the notes are "
                  "different magnitudes, so a bank can lend more with no more notes outstanding."),
            ("p", "Where Fullarton went wrong, on Marx's account, is in what he called the thing "
                  "demanded. In a crisis firms borrow &ldquo;for the purpose of paying, not of "
                  "buying&rdquo;; the notes go out and return at once, and so the circulation does "
                  "not swell. That is money as means of payment, not a demand for capital as "
                  "opposed to currency. And the securities a bank holds against its loans are not "
                  "capital either: shares are &ldquo;mere titles of ownership&rdquo;, government "
                  "bonds &ldquo;merely claims on loans&rdquo;. That last thought is the next "
                  "chapter's."),
            ("p", "Economists today keep something like Tooke's line: they distinguish the money "
                  "supply from credit, and a central bank's balance sheet from the loans the "
                  "banking system makes. Marx's point in this chapter is narrower: the quantity "
                  "of notes in circulation tells you how many purchases and payments money has to "
                  "perform, not how much capital there is."),
            ("p", "If notes are not capital, what is in a bank's strongroom? “The Component Parts "
                  "of Bank Capital” takes the bank's balance sheet apart."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "circulate",
            "money_unit": "£",
            "preset": "revenue",
            "presets": [
                {"id": "revenue", "label": "A week's wages of £1,000 spent in shops; each note serves 10 times",
                 "goods": [{"name": "food and rent", "value_hours": 1400},
                           {"name": "clothing", "value_hours": 400},
                           {"name": "fuel", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 10,
                 "expect": {"moPriceSum": "£1,000", "moNeeded": "£100"}},
                {"id": "capital", "label": "£1,000 paid between capitalists; each note serves 10 times",
                 "goods": [{"name": "cotton to the spinner", "value_hours": 1200},
                           {"name": "yarn to the weaver", "value_hours": 800}],
                 "gold_hours_per_unit": 2, "velocity": 10,
                 "expect": {"moPriceSum": "£1,000", "moNeeded": "£100"}},
                {"id": "mixed", "label": "Both at once: £2,000 of payments at 10 turns",
                 "goods": [{"name": "food and rent", "value_hours": 1400},
                           {"name": "clothing", "value_hours": 400},
                           {"name": "fuel", "value_hours": 200},
                           {"name": "cotton to the spinner", "value_hours": 1200},
                           {"name": "yarn to the weaver", "value_hours": 800}],
                 "gold_hours_per_unit": 2, "velocity": 10,
                 "expect": {"moPriceSum": "£2,000", "moNeeded": "£200"}},
                {"id": "credit", "label": "The £1,000 between capitalists, speeded by credit to 25 turns",
                 "goods": [{"name": "cotton to the spinner", "value_hours": 1200},
                           {"name": "yarn to the weaver", "value_hours": 800}],
                 "gold_hours_per_unit": 2, "velocity": 25,
                 "expect": {"moPriceSum": "£1,000", "moNeeded": "£40"}},
            ],
            "panel_title": "Notes for revenue and for capital",
            "panel_intro": (
                "The payments of a period and the velocity go in; values are in hours at 2 hours to "
                "the pound, so the prices are in pounds. The lab sums the prices and divides by the "
                "velocity. Nothing in the computation asks whether a payment is revenue or capital: "
                "compare the revenue and capital presets."
            ),
        }),
        "steps_title": "Computing the notes a circulation needs",
        "steps_intro": "Four steps for any mix of revenue and capital.",
        "steps": [
            ("Sort the payments",
             "Mark each payment as revenue spent on consumption or as a transfer of capital between "
             "capitalists. The sorting says what the money does, not how much is needed."),
            ("Sum the prices",
             "Add the payments to be made in the period, of both kinds."),
            ("Find the velocity",
             "Take the number of times each note serves in the period. Credit raises it between "
             "capitalists, and settles some payments with no notes at all."),
            ("Divide",
             "The notes needed are the sum of prices divided by the velocity, whatever the payments "
             "are labelled."),
        ],
        "worked": {
            "title": "The same notes for wages and for cotton",
            "intro": [
                "A week's wages of £1,000 are spent in shops and £1,000 of cotton and yarn are paid "
                "for between capitalists, each note serving 10 times. You want the notes each "
                "needs, and the notes the second needs once credit speeds it to 25 turns.",
            ],
            "lines": [
                "revenue:  £1000 / 10 = £100",
                "capital:  £1000 / 10 = £100",
                "both:  £2000 / 10 = £200",
                "capital with credit:  £1000 / 25 = £40",
            ],
            "after": [
                "Calling the second £1,000 capital changed nothing in the notes it needs. What "
                "changed them was the velocity, which credit raised.",
            ],
        },
        "quiz_title": "Currency, capital and the notes needed",
        "quiz": [
            {"q": "In a week, £600 of wages are spent in shops and £900 is paid between merchants; "
                  "every note serves 5 times. How many pounds of notes are needed?",
             "a": ["£300", "£120", "£180", "£1,500"],
             "c": 0,
             "why": "`(600 + 900) / 5 = 300`. One hundred and twenty counts only the wages and "
                    "180 only the merchants' payments; £1,500 forgets to divide by the velocity."},
            {"q": "On Marx's account, what really distinguishes the two circulations Tooke called "
                  "currency and capital?",
             "a": ["One uses gold and the other paper",
                   "One realises revenue and the other transfers capital",
                   "One obeys the law of circulation and the other does not",
                   "One is issued by the Bank of England and the other by private banks"],
             "c": 1,
             "why": "Marx calls the difference &ldquo;that between the money-form of revenue and the "
                    "money-form of capital&rdquo;. Both obey the same law, the same note serves in "
                    "both, and the metals and issuers differ only by custom."},
            {"q": "A bank lends a manufacturer £1,000 in notes; he pays a supplier, who deposits "
                  "them back in the bank the same day. What has happened to the notes in "
                  "circulation and to the loan?",
             "a": ["Both have risen by £1,000",
                   "The notes are back with the bank and the loan remains",
                   "The loan has been repaid",
                   "The notes have become capital"],
             "c": 1,
             "why": "In Fullarton's words, &ldquo;The loan remains, and the currency, if not wanted, "
                    "finds its way back to the issuer.&rdquo; The manufacturer still owes the bank, "
                    "so the loan is not repaid; the notes did one payment and returned."},
            {"q": "Between capitalists, credit raises the velocity of a £2,000 circulation from 10 "
                  "to 40. By how much does the need for notes fall?",
             "a": ["£150", "£50", "£200", "£1,500"],
             "c": 0,
             "why": "From `2000/10 = 200` to `2000/40 = 50`, a fall of 150. Fifty is the new need, "
                    "200 the old one, and 1,500 applies the fall to the £2,000 of payments "
                    "instead of to the notes."},
        ],
        "mistakes": [
            ("Thinking the quantity of notes measures the quantity of capital",
             "The revenue and capital presets need the same £100 of notes, though one is wages and "
             "the other cotton. The credit preset moves the same £1,000 of capital with £40. The "
             "notes measure the purchases and payments money has to perform at a given velocity, "
             "and Marx says whether they represent &ldquo;capital or revenue&rdquo; is "
             "&ldquo;immaterial&rdquo;."),
            ("Equating a bank's loans with its notes in circulation",
             "Notes lent come back as deposits and repayments while the loan remains. Fullarton saw "
             "the Bank's loans rise as its notes fell; Marx agrees on the fact and explains it by "
             "the reflux, not by a difference between currency and capital."),
            ("Taking Marx to dismiss Tooke and Fullarton",
             "They were his allies against the Currency School on the main point, that a bank "
             "cannot force notes into circulation. His quarrel is with their terms, and with the "
             "&ldquo;narrow minded banker's conception of circulation&rdquo; behind them."),
        ],
        "standard": (
            "Finish when you can compute the notes a mixed circulation needs.",
            "Given payments sorted into revenue and transfers of capital, and the velocity of each, "
            "compute the notes each circulation needs and the total, and compute the change when "
            "credit alters a velocity."
        ),
        "note": (
            "The lab divides a period's payments by one velocity. Marx's law also subtracts "
            "payments that cancel, which the lessons on Chapters 25 and 32 return to; and in "
            "fact the two circulations have different velocities, which the lab shows only by "
            "running them as separate presets. The wages and payments are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 3, l. 4108-4110 (capitalising). Inline: l. 4096 (the
    # simple matter), l. 4100 (the state debt), l. 4102-4104 (wages
    # capitalised), l. 4112 (shares), l. 4116 (the share and the rate),
    # l. 4120 (Morris and the bubble), l. 4130 (banking capital fictitious),
    # l. 4136 (capital doubles).
    {
        "slug": "component-parts-of-bank-capital",
        "title": "The Component Parts of Bank Capital",
        "module": "Chapter 29 · The Composition of Banking Capital",
        "one_line": "A claim to a yearly income is priced by dividing the income by the rate of interest, so its price moves with the rate while nothing real changes.",
        "summary": (
            "A bank's capital is cash, bills and securities: government bonds, shares, mortgages. "
            "Marx calls the price of these claims fictitious capital and shows how it is formed. "
            "Compute the price of a claim to a yearly income at a rate of interest, Marx's £100 a "
            "year at 5%, and what a change in the rate does to it with no change in anything the "
            "claim is a claim on."
        ),
        "key": [
            "price = yearly income / rate of interest",
            "£100 a year at 5% = £2,000",
            "the rate doubles, the price halves",
            "a state bond: capital already spent",
            "a share: a title, not a second capital",
        ],
        "key_label": "Capitalisation in five lines",
        "concepts_intro": (
            "Engels says this chapter came almost whole from Marx's manuscript. It is where the "
            "phrase in Part V's title finally gets its meaning."
        ),
        "concepts": [
            ("Capitalising",
             "Treating any regular income as interest on a capital, and computing that capital by "
             "dividing the income by the going rate of interest."),
            ("Fictitious capital",
             "The capital-value so computed, where no capital of that amount exists: a state debt "
             "whose principal was spent long ago, or a share, whose paper price is a second "
             "capital-value beside the real capital the company works. Even where the paper stands "
             "for real capital, Marx says its capital-value is &ldquo;wholly illusory&rdquo;."),
            ("A bank's capital",
             "Cash, bills of exchange and interest-bearing papers, most of it other people's "
             "deposits. Marx calls the greater part of it &ldquo;purely fictitious&rdquo;."),
        ],
        "read_title": "The definition first, then the bond, the share and the crash",
        "read_intro": (
            "The passage is Marx's definition, with his own figures. It comes after two examples, "
            "a state debt and a wage, which the lesson returns to."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 29.</strong> &ldquo;The forming of a fictitious "
                  "capital is called capitalising. Every periodically repeated income is "
                  "capitalised by calculating it on the average rate of interest, as an income which "
                  "would be realised by a capital at this rate of interest. For instance, if the "
                  "annual income is 100 pounds sterling and the rate of interest 5%, then these 100 "
                  "pounds sterling would represent the annual interest on 2,000 pounds "
                  "sterling&rdquo;."),
            ("p", "You have met this sum whenever you have heard that bond prices fall when "
                  "interest rates rise, or that a house is <em>worth twenty years' rent</em>. "
                  "Marx's sentence is the rule behind both. A claim to £100 a year is worth whatever "
                  "sum would earn £100 a year if it were lent at the going rate: at 5%, £2,000. The "
                  "lab divides the income by the rate. The marx preset is his own example, £100 a "
                  "year at 5%, and prints £2,000."),
            ("p", "Now change only the rate. Marx does it in the same chapter: &ldquo;If the rate of "
                  "interest rises from 5% to 10%, then a security guaranteeing an income of 5 pounds "
                  "sterling will represent only a capital of 50 pounds sterling.&rdquo; In the "
                  "rate-up preset the same £100 a year at 10% is priced at £1,000; in the rate-down "
                  "preset, at 2½%, at £4,000. The income is unchanged in all three. Nothing that "
                  "pays it has grown or shrunk, and the &ldquo;capital&rdquo; has doubled and "
                  "halved."),
            ("p", "Marx's first example is a government bond. The state borrowed £100 and spent it, "
                  "on a war perhaps, and pays the lender £5 a year out of taxes. The lender cannot "
                  "ask for the £100 back; he can sell his claim, and at 5% a buyer will pay £100 "
                  "for it. To both of them it looks like a capital of £100. But &ldquo;Not only does "
                  "the amount loaned to the state exist no longer, but it was never intended at all "
                  "to be invested as capital&rdquo;. That is fictitious capital in its plainest "
                  "form: &ldquo;from the moment that the certificates would become unsalable, the "
                  "fiction of this capital would disappear.&rdquo;"),
            ("p", "His second example shows how far the habit of capitalising goes. If a worker "
                  "earns £50 a year and the rate of interest is 5%, his labour-power can be called a "
                  "capital of £1,000, and statisticians did so. &ldquo;The insanity of the capitalist "
                  "mode of conception reaches its climax here.&rdquo; Two facts spoil the sum, Marx "
                  "says dryly: the worker has to work to get this &ldquo;interest&rdquo;, and he "
                  "cannot sell the &ldquo;capital&rdquo;."),
            ("p", "Shares are different, and Marx is careful about the difference. A railway share "
                  "is a title to real capital, the rails and engines the shareholders paid for. But "
                  "&ldquo;this capital does not exist twofold&rdquo;: once as rails and again as "
                  "the price of the paper. The paper's price is fixed by capitalising its dividend. "
                  "Marx's figures: a share issued at £100 whose company pays 10% is worth £200 while "
                  "the rate of interest is 5%. The share preset computes it, £10 a year at 5%: £200. "
                  "The company's rails are the same rails at either price."),
            ("p", "This is why a crash can destroy so much &ldquo;wealth&rdquo; and so little "
                  "capital. The Governor of the Bank of England told the committee that on 23 "
                  "October 1847 the public funds and canal and railway stocks had lost "
                  "£114,752,225 of value. Marx's comment: unless the fall stopped trains and canal "
                  "boats or ended works under way, &ldquo;the nation did not grow poorer by one cent "
                  "through the bursting of this bubble of fictitious capital.&rdquo; Who grew poorer "
                  "were the holders who had to sell, and who grew richer were the buyers, since the "
                  "fall &ldquo;serves as a potent means of centralising money&rdquo;."),
            ("p", "Then the bank itself. Its capital is cash, bills of exchange and securities, and "
                  "most of it is not its own but its depositors'. The bills are promises to pay; "
                  "the bonds represent &ldquo;spent capital&rdquo;; the shares are &ldquo;claims on "
                  "future yields of production&rdquo;. Even the deposits are mostly lent out again, "
                  "so the same sum appears as a deposit in one book and a loan in another. "
                  "&ldquo;With the development of the credit system and of interest-bearing capital "
                  "all capital seems to double, or even treble, itself&rdquo;."),
            ("p", "The rule itself is now the first lesson of finance: a security's price is the "
                  "present value of its expected income, and it moves inversely with the rate. "
                  "Irving Fisher built a theory of capital on it in 1906. What a modern economist "
                  "would dispute is the word &ldquo;fictitious&rdquo;. On the standard view a share's "
                  "price is the market's best estimate of what the real capital will earn, so a "
                  "rise above the money invested is information, not fiction. What in the chapter "
                  "bears on that is the government bond, where the capital lent was spent long "
                  "ago and the bond is a claim on future taxes, and the remark that the price of a "
                  "share is a claim on future yields, not the capital that was paid in. The "
                  "presets show one more thing both sides accept: the price moves with the rate "
                  "of interest even when nothing about the earnings has changed."),
            ("p", "If so much of the money capital in the banks is fictitious, does a pile of it "
                  "tell you that real capital is piling up? “Money Capital and Real Capital I” "
                  "asks exactly that."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "capitalise",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: £100 a year at 5%",
                 "income": 100, "interest_rate": "1/20",
                 "expect": {"inPrice": "£2,000"}},
                {"id": "rate-up", "label": "The same £100 a year at 10%",
                 "income": 100, "interest_rate": "1/10",
                 "expect": {"inPrice": "£1,000"}},
                {"id": "rate-down", "label": "The same £100 a year at 2½%",
                 "income": 100, "interest_rate": "1/40",
                 "expect": {"inPrice": "£4,000"}},
                {"id": "share", "label": "Marx's share: £100 paid in, a 10% dividend, capitalised at 5%",
                 "income": 10, "interest_rate": "1/20",
                 "expect": {"inPrice": "£200"}},
            ],
            "panel_title": "The price of a claim to an income",
            "panel_intro": (
                "A yearly income and the rate of interest go in; the lab divides one by the other. "
                "Nothing about what pays the income is an input, because nothing about it enters the "
                "price. Run the first three presets in turn: only the rate changes."
            ),
        }),
        "steps_title": "Capitalising an income",
        "steps_intro": "Four steps for any regular income that can be sold.",
        "steps": [
            ("Find the yearly income",
             "Take the income the claim pays each year: a bond's interest, a share's dividend, a "
             "rent."),
            ("Find the rate of interest",
             "Take the going rate at which money can be lent with similar security."),
            ("Divide",
             "The claim's price is the income divided by the rate: the sum that would earn the same "
             "income if lent at that rate."),
            ("Compare with what was invested",
             "Set the price beside the money actually put in, if any was. The difference, or the "
             "whole price for a spent state loan, is fictitious capital."),
        ],
        "worked": {
            "title": "Marx's £100 a year at three rates",
            "intro": [
                "A claim pays £100 a year, and nothing about it changes. You want its price at 5%, "
                "at 10% and at 2½%, and the price of Marx's share.",
            ],
            "lines": [
                "at 5%:  £100 / (1/20) = £2000",
                "at 10%:  £100 / (1/10) = £1000",
                "at 2½%:  £100 / (1/40) = £4000",
                "share:  £10 / (1/20) = £200 on £100 paid in",
            ],
            "after": [
                "The same income is £1,000, £2,000 or £4,000 of capital depending on a rate set in "
                "the money market. The share's extra £100 is a price for paper; the company has the "
                "same £100 of real capital either way.",
            ],
        },
        "quiz_title": "Capitalisation and fictitious capital",
        "quiz": [
            {"q": "A bond pays £30 a year and the rate of interest is 6%. What is its price on the "
                  "chapter's rule?",
             "a": ["£180", "£500", "£300", "£1,800"],
             "c": 1,
             "why": "`30 / (6/100) = 500`. One hundred and eighty multiplies instead of dividing; "
                    "£300 is ten years' income and £1,800 sixty years'."},
            {"q": "The rate of interest falls from 5% to 4% and the bond's income does not change. "
                  "What happens to the price of a bond paying £20 a year?",
             "a": ["It falls from £400 to £320",
                   "It rises from £400 to £500",
                   "It stays at £400, since nothing real has changed",
                   "It rises from £100 to £125"],
             "c": 1,
             "why": "`20 / (5/100) = 400` and `20 / (4/100) = 500`. The price moves inversely with "
                    "the rate, which is the point; it does not stay put, and £100 and £125 confuse "
                    "the income with the principal."},
            {"q": "Why does Marx call the capital of a national debt purely fictitious?",
             "a": ["Because the state never pays the interest",
                   "Because the sum lent was spent and exists no longer, while the claim to interest is sold as capital",
                   "Because bonds are printed on paper",
                   "Because the rate of interest on bonds is fixed by law"],
             "c": 1,
             "why": "Marx writes that the amount loaned to the state does &ldquo;exist no longer&rdquo; and was "
                    "never invested as capital. The state does pay the interest, out of taxes; "
                    "paper and a legal rate are not his reasons."},
            {"q": "Railway shares lose a third of their market price in a panic, and the trains run "
                  "as before. On the chapter's account, how much poorer is the nation?",
             "a": ["By the whole fall in the share price",
                   "Not at all, though the sellers are poorer and the buyers richer",
                   "By a third of the railway's capital",
                   "By the interest the shares would have earned"],
             "c": 1,
             "why": "Marx says that unless production is stopped &ldquo;the nation did not grow "
                    "poorer by one cent&rdquo;, while the fall centralises money in the buyers' "
                    "hands. The railway's real capital is untouched, so the other options count a "
                    "price change as a loss of capital."},
        ],
        "mistakes": [
            ("Thinking the price of a security measures real capital invested",
             "In the marx, rate-up and rate-down presets the same £100 a year is £2,000, £1,000 and "
             "£4,000, and nothing that pays it has changed. In the share preset a share with £100 "
             "of real capital behind it is priced at £200. The price is the income divided by the "
             "rate of interest; the capital invested is not an input to the sum at all."),
            ("Counting a share's price as a second capital beside the company's",
             "Marx: &ldquo;this capital does not exist twofold&rdquo;. The rails exist once; the "
             "share is a title to part of what they earn, and its price can move while they stand "
             "still."),
            ("Believing a fall in security prices destroys national wealth",
             "Unless production stops, a crash moves wealth from sellers to buyers. The £114 "
             "million of 1847 was a fall in the price of claims, and Marx says the nation did not "
             "grow poorer by it."),
        ],
        "standard": (
            "Finish when you can price a claim to an income and say what a change in the rate does.",
            "Given a yearly income and a rate of interest, compute the claim's price; compute it "
            "again at a new rate; and state how much of the price, if any, corresponds to capital "
            "actually invested."
        ),
        "note": (
            "The lab capitalises a perpetual income at one rate and ignores risk, the expected "
            "growth of a dividend and the term of a bond, all of which a market price includes; "
            "Marx mentions the expected income and the security of the yield and does not compute "
            "them. The £100 at 5% and the share at £200 are Marx's figures; the 2½% and the "
            "10% applied to the £100 follow his own changes of rate."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 3, l. 4238 (not every augmentation). Inline: l. 4175 (the
    # questions), l. 4226 (nothing more erroneous), l. 4242 (Hodgson),
    # l. 4234 (business always sound), l. 4259 (opposite directions),
    # l. 4228 (the last cause), l. 4266 (no bank legislation); preface
    # l. 308.
    {
        "slug": "money-capital-and-real-capital-i",
        "title": "Money Capital and Real Capital I",
        "module": "Chapter 30 · Money-Capital and Actual Capital, I",
        "one_line": "Loanable money piles up in the banks fastest just after a crisis, when real accumulation has stopped, because the money set free by the producers who cannot invest is deposited, not spent.",
        "summary": (
            "Chapter 30 asks whether a growing mass of loanable money capital shows that real "
            "capital is being accumulated, and answers that it often shows the reverse. Using "
            "Volume II's scheme of expanded reproduction, compute the surplus product left unsold "
            "when more of the capitalists who accumulate hoard money than spend it, and see why "
            "the money that would have bought it lies in the banks while production stands still."
        ),
        "key": [
            "real capital: means of production, goods",
            "money capital: money held to lend",
            "hoarders sell and do not buy",
            "unsold = hoarders' sales − purchases",
            "after a crisis: cheap money, idle plant",
        ],
        "key_label": "Money capital against real capital",
        "concepts_intro": (
            "Engels says the real difficulty of Part V began here: this chapter was assembled by "
            "&ldquo;transpositions and eliminations&rdquo; from a manuscript that kept breaking "
            "off. Its questions are clear, and so is its answer to the first of them."
        ),
        "concepts": [
            ("Actual accumulation",
             "The growth of real capital: more means of production, more labour employed, "
             "production on a larger scale."),
            ("Accumulation of money capital",
             "The growth of the money held in banks to be lent. It can grow for reasons that have "
             "nothing to do with actual accumulation."),
            ("The cycle",
             "Marx follows the rate of interest through the trade cycle: low after a crisis, "
             "rising through recovery and prosperity, highest in the crash. Loan capital and "
             "industrial capital move in opposite directions over most of it."),
        ],
        "read_title": "The answer first, then the cycle it comes from",
        "read_intro": (
            "The chapter opens with two questions. The passage is Marx's answer to the first, "
            "given after a long digression on commercial credit."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 30.</strong> &ldquo;Not every augmentation of "
                  "loanable capital indicates a real accumulation of capital or expansion of the "
                  "process of reproduction. This becomes most evident in the phase of the industrial "
                  "cycle following immediately after a crisis, when loanable capital lies fallow in "
                  "masses.&rdquo;"),
            ("p", "You may have noticed that interest rates are often lowest just when the news is "
                  "worst: after a recession, deposits pile up in banks and nobody wants to borrow. "
                  "That is the season Marx describes. His two questions at the start of the chapter "
                  "are whether the accumulation of money capital is a sign of real accumulation, "
                  "and whether a scarcity of loan capital in a crisis is a scarcity of real capital. "
                  "This lesson takes the first; the next two take the rest."),
            ("p", "Go through the passage. The &ldquo;loanable capital&rdquo; is money in the hands of "
                  "banks and lenders, offered at interest. A &ldquo;real accumulation of "
                  "capital&rdquo; is more spindles, more cotton, more workers employed. After the "
                  "crisis of 1847, Marx notes, production in the English industrial districts fell "
                  "by a third, and yet the banks reported &ldquo;a reduction of transactions and a "
                  "great super-abundance of money&rdquo;. The rate of interest was low, a banker "
                  "said, because of the &ldquo;almost complete annihilation of commerce and nearly "
                  "utter absence of a possibility of investing money&rdquo;. Loanable capital was "
                  "plentiful precisely because industrial capital had been laid lame."),
            ("p", "The lab borrows the scheme from Volume II, Chapter 21, which you met in "
                  "Reproduction of the Social Capital: Department I, making means of production, "
                  "with 4,000c + 1,000v + 1,000s, and half the surplus value, 500, set aside for "
                  "accumulation. Accumulation needs two groups. Some capitalists have just sold their "
                  "surplus product and hold the money, adding to a hoard until it is large enough to "
                  "invest; others spend hoards built up before. The surplus product sells only if "
                  "the second group's purchases match the first group's sales."),
            ("p", "In the balanced preset half the accumulating capitalists hoard and half invest: "
                  "250 of surplus product sold, 250 bought, gap 0. In the stagnant preset all of "
                  "them hoard and none invests, the state just after a crisis: they sell 500 and buy "
                  "nothing, and the lab prints +500, 500 of surplus product unsold. That 500 is "
                  "commodity capital that cannot complete its round: the sellers do not have the "
                  "money for it, because nobody bought it. The money that would have bought it, "
                  "the hoards the investors built up in earlier years, is not spent either. In a "
                  "developed credit system it sits in the banks as deposits, loanable capital "
                  "lying fallow while not one spindle is added. In the boom preset only a quarter hoard, and investors want "
                  "250 more than is offered: the lab prints −250, demand without a product."),
            ("p", "So a pile of deposits can mean two opposite things. Marx's reading of the cycle "
                  "is that the movements of loan capital &ldquo;tend in a direction opposite to that "
                  "of industrial capital&rdquo;. A low rate of interest coincides with contraction "
                  "at the start of the cycle and a high rate with a glut of industrial capital at "
                  "the end. Only in the recovery and the middle of prosperity are abundant loan capital "
                  "and expanding production found together."),
            ("p", "The second question gets an answer in the same chapter, though the next lessons "
                  "work it out. In the crash, when credit stops, commodities are unsold and "
                  "factories closed. &ldquo;Nothing is more erroneous, therefore, than to blame a "
                  "scarcity of productive capital for such a condition.&rdquo; What is scarce is "
                  "credit; the real capital is in excess, unable to complete its round."),
            ("p", "Marx has his usual fun with the witnesses. Every expert before the Bank "
                  "Committees of 1857 and 1858, Overstone at their head, congratulated the others on "
                  "the soundness of business a month before the crisis, and Tooke's history of "
                  "prices records the same illusion every time: &ldquo;Business is always thoroughly "
                  "sound and the campaign in full swing, until the collapse suddenly overtakes "
                  "them.&rdquo;"),
            ("p", "In the middle of all this is one of the most argued-over sentences in "
                  "<em>Capital</em>: &ldquo;The last cause of all real crises always remains the "
                  "poverty and restricted consumption of the masses as compared to the tendency of "
                  "capitalist production to develop the productive forces&rdquo;. Readers who hold "
                  "an underconsumption theory of crisis take it as Marx's verdict. Others point out "
                  "that Volume II argues against explaining crises by workers' lack of purchasing "
                  "power, and that Volume III's own Part III puts the falling rate of profit at "
                  "the centre; they read this sentence as one consideration among several in an "
                  "unfinished manuscript. The lesson takes no side, and neither does the lab, "
                  "which computes only the gap between hoarders and investors."),
            ("p", "Marx's chapter is also clear that bank legislation is not the cause: &ldquo;An "
                  "ignorant and mistaken legislation, such as that of 1844-45, may intensify a money "
                  "crisis. But no manner of bank legislation can abolish a crisis.&rdquo; The Bank "
                  "Act lesson later in this course computes how it intensified one."),
            ("p", "If money capital can pile up while nothing real accumulates, where does it come "
                  "from? “Money Capital and Real Capital II” follows the routes by which money "
                  "becomes loan capital without anyone saving."),
        ],
        "lab": ("capkit", {
            "mode": "schemes",
            "view": "hoard",
            "preset": "balanced",
            "presets": [
                {"id": "balanced", "label": "Volume II's Department I: half the accumulators hoard, half invest",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "I_accumulate_share": "1/2", "hoarders_share": "1/2",
                 "expect": {"scHoardGap": "0: hoarders' sales = investors' purchases"}},
                {"id": "stagnant", "label": "After a crisis: every accumulator hoards, none invests",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "I_accumulate_share": "1/2", "hoarders_share": "1",
                 "expect": {"scHoardGap": "+500: 500 of surplus product unsold"}},
                {"id": "boom", "label": "A boom: a quarter hoard, three quarters invest",
                 "I": {"c": 4000, "v": 1000, "s": 1000}, "I_accumulate_share": "1/2", "hoarders_share": "1/4",
                 "expect": {"scHoardGap": "−250: 250 of demand without a product"}},
            ],
            "panel_title": "Hoarders, investors and the surplus product",
            "panel_intro": (
                "Department I's c, v and s, the share of s it accumulates and the share of the "
                "accumulators who hoard this year go in. Hoarders sell their surplus product and buy "
                "nothing; investors buy with money hoarded before. The tile is hoarders' sales less "
                "investors' purchases; a positive gap is surplus product unsold, and a negative one "
                "is investors' money with no product to buy."
            ),
        }),
        "steps_title": "Finding the unsold surplus product",
        "steps_intro": "Four steps for Department I in a year of accumulation.",
        "steps": [
            ("Find the surplus to be accumulated",
             "Multiply Department I's surplus value by the share it accumulates."),
            ("Split the accumulators",
             "Those who hoard this year sell their share of that surplus product for money and buy "
             "nothing; the rest buy means of production with money hoarded earlier."),
            ("Subtract",
             "The gap is the hoarders' sales less the investors' purchases. Positive, product is "
             "unsold; negative, investors want more than is offered."),
            ("Read the gap both ways",
             "A positive gap is commodity capital that cannot be turned into money. The hoards "
             "that would have bought it stay in the banks as loanable capital, while real "
             "accumulation stands still."),
        ],
        "worked": {
            "title": "Department I, before and after a crisis",
            "intro": [
                "Department I produces 4,000c + 1,000v + 1,000s and accumulates half its surplus "
                "value. You want the gap when half the accumulators hoard, and when all of them do.",
            ],
            "lines": [
                "to accumulate:  1000 · 1/2 = 500",
                "half hoard:  sales 250,  purchases 250,  gap 0",
                "all hoard:  sales 500,  purchases 0",
                "gap:  +500 unsold;  the investors' hoards unspent",
            ],
            "after": [
                "In the second year 500 of product lies unsold, and the money that would have "
                "bought it stays in the banks. Measured by the money offered for loan, capital "
                "looks plentiful; measured by means of production put to work, nothing has been "
                "added.",
            ],
        },
        "quiz_title": "Loanable capital and actual accumulation",
        "quiz": [
            {"q": "Department I accumulates 800 of its surplus value. Three quarters of the "
                  "accumulators hoard this year. What gap does the lab print?",
             "a": ["+400: 400 unsold", "+600: 600 unsold", "−400: 400 of demand without a product", "+200: 200 unsold"],
             "c": 0,
             "why": "Hoarders sell `800 · 3/4 = 600` and investors buy `800 · 1/4 = 200`, so the gap "
                    "is `600 − 200 = +400`. Six hundred is the hoarders' sales alone, 200 the "
                    "investors' purchases, and the sign is positive because sales exceed purchases."},
            {"q": "On the chapter's account, when is loanable capital most abundant while industrial "
                  "capital is contracted?",
             "a": ["At the height of prosperity",
                   "In the phase just after a crisis",
                   "In the middle of the crash",
                   "Never; the two always move together"],
             "c": 1,
             "why": "Marx's passage names &ldquo;the phase of the industrial cycle following "
                    "immediately after a crisis, when loanable capital lies fallow in masses&rdquo;. "
                    "In the crash loan capital is scarcest, and his point is that the two move in "
                    "opposite directions over most of the cycle."},
            {"q": "Bank deposits rise by £5 million in a year in which no factory is built or "
                  "enlarged. What does Marx's chapter allow you to conclude?",
             "a": ["That real capital rose by £5 million",
                   "That loanable capital rose with no actual accumulation",
                   "That the rate of interest must rise",
                   "That the deposits are fictitious and will vanish"],
             "c": 1,
             "why": "&ldquo;Not every augmentation of loanable capital indicates a real "
                    "accumulation&rdquo;. With nothing built the rise cannot be real capital; more "
                    "money offered for loan tends to lower the rate, not raise it; and although "
                    "Chapter 29 calls most deposits fictitious, nothing in the chapter says these "
                    "will vanish."},
            {"q": "Why, after the crisis of 1847, was the rate of interest low, according to the "
                  "banker Marx quotes?",
             "a": ["Because the Bank of England printed more notes",
                   "Because commerce had nearly stopped and there was no way to invest money",
                   "Because profits were unusually high",
                   "Because gold flowed out of the country"],
             "c": 1,
             "why": "Hodgson gives the &ldquo;almost complete annihilation of commerce and nearly "
                    "utter absence of a possibility of investing money&rdquo;. High profits would "
                    "raise demand for loans, and a gold drain raises the rate; note issue is not his "
                    "explanation."},
        ],
        "mistakes": [
            ("Thinking a pile of bank deposits means plenty of real capital",
             "In the stagnant preset Department I offers 500 of surplus product and buys none: +500 "
             "of product is unsold, and the hoards that would have bought it sit in the banks. "
             "Loanable capital lies fallow while real accumulation is nothing. Marx's evidence is 1847: production "
             "down a third and &ldquo;a great super-abundance of money&rdquo;."),
            ("Reading a low rate of interest as a sign of good times",
             "A low rate comes both in the slump after a crisis and in the early recovery. Marx "
             "says only the recovery and mid-prosperity combine abundant loan capital with expanding "
             "production; just after a crisis the low rate shows industrial capital &ldquo;laid "
             "lame&rdquo;."),
            ("Taking the sentence on the masses' consumption as the chapter's settled theory of crisis",
             "It is one sentence in a chapter Engels assembled from fragments, and readers dispute "
             "its weight against Volume II's objections to underconsumption and Part III's falling "
             "rate of profit. The lab computes a gap between hoarders and investors, nothing more."),
        ],
        "standard": (
            "Finish when you can compute the surplus product left unsold by hoarding.",
            "Given Department I's surplus value, the share accumulated and the share of "
            "accumulators who hoard, compute the hoarders' sales, the investors' purchases and the "
            "gap, and state what the gap adds to money capital and to real capital."
        ),
        "note": (
            "The lab reuses Volume II's scheme, whose 4,000c + 1,000v + 1,000s are Marx's figures "
            "there; Chapter 30 gives no scheme, and the shares of hoarders are illustrative. It "
            "computes the unsold product only; it does not track the deposits, or the money "
            "that stays in pockets as a hoard, and it follows one department for one year."
        ),
    },
]
