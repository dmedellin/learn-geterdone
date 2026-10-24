"""Credit and Fictitious Capital, lessons 7-12 -- Volume III, Part V, Chapters 31-36.

Quoting conventions as in part_a: every quotation is copied from
/mnt/project-files/capital-texts/volume-3-kerr.txt, footnote numerals left out,
the translator's inner double quotes printed as single curly quotes, nothing
else changed. Misprints in the Kerr text are quoted as printed and pointed out.

Chapters 33 to 35 lean heavily on the parliamentary evidence, and Chapter 34
is mostly Engels: a long bracket of his own, wrapped round a quotation from
Marx's Contribution to the Critique of Political Economy (1859). The opening
passages of lessons 10 and 11 are Engels' text, and the lessons say so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    # Kerr vol. 3, l. 4316 (technical means). Inline: l. 4302-4306 (two
    # conversions), l. 4312 (two phases), l. 4322 (London stock banks,
    # Ipswich), l. 4334 (the rural depositor), l. 4346 and 4358 (the dealer's
    # £100), l. 4388-4390 (revenue as deposit), l. 4320 (credit jargon),
    # l. 4406-4408 (Chapter 32 on capital released by a fall in prices).
    {
        "slug": "money-capital-and-real-capital-ii",
        "title": "Money Capital and Real Capital II",
        "module": "Chapter 31 · Money-Capital and Actual Capital. II",
        "one_line": "Loan capital grows when banking spreads, when a business contracts and when income waits to be spent; none of it needs anyone to save.",
        "summary": (
            "Chapter 31 follows the routes by which money becomes loan capital: the spread and "
            "concentration of banking, the capital a business lets go when it contracts, and "
            "the revenue that waits in a bank until it is spent. Using Volume II's working and "
            "circulation periods, compute the circulating capital a business releases when it "
            "cuts its weekly outlay, and see that it reaches the money market though nobody "
            "saved it."
        ),
        "key": [
            "loan capital: money offered at interest",
            "advance = (weeks of both periods) · outlay",
            "released: old advance less new advance",
            "deposits grow as banking spreads",
            "waiting revenue is a deposit too",
        ],
        "key_label": "Where loan capital comes from",
        "concepts_intro": (
            "Marx starts by separating two things that both put money in a banker's hands, "
            "and says only the second can go with real accumulation."
        ),
        "concepts": [
            ("Conversion of money into loan capital",
             "Money already in existence that is placed with a bank: a reserve no longer "
             "needed, capital let go by a business that has contracted, deposits gathered by a "
             "bank that opens in a new district. Nothing new has been produced."),
            ("Conversion of capital or revenue into loan capital",
             "Profit or other income realised in money and deposited while it waits to be "
             "invested or spent. This is the route that can go with actual accumulation."),
            ("Floating capital",
             "The money market's name for the short-term loan capital that moves back and "
             "forth between banks and borrowers. Marx makes fun of the jargon: in it money, "
             "bullion and debts all become capital."),
        ],
        "read_title": "The technical routes first, then the routes through income",
        "read_intro": (
            "The passage closes the chapter's first section, on the plain conversion of "
            "money into loan capital."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 31.</strong> &ldquo;We have seen, on the other "
                  "hand, that an accumulation of loan capital may take place without any actual "
                  "accumulation, by mere technical means, such as an expansion and concentration "
                  "of the banking system, a saving in the currency reserve, or in the reserve "
                  "fund of private means of payment, which are then always converted into loan "
                  "capital for a short time.&rdquo;"),
            ("p", "When a firm scales back, its overdraft shrinks and its cash piles up in a "
                  "deposit account. Nobody in the firm has saved anything; it simply needs less "
                  "money to keep going. Chapter 31 asks where the banks' loanable money comes "
                  "from, and its first answer is cases like this, in which money that already "
                  "exists changes hands and turns into money on offer at interest."),
            ("p", "Marx divides the ground at once. There is &ldquo;The mere conversion of money "
                  "into money-capital&rdquo;, and there is &ldquo;The conversion of capital or "
                  "revenue into money, which is turned into loan capital&rdquo;. Only the second "
                  "&ldquo;can imply a positive accumulation of loan capital connected with an "
                  "actual accumulation of industrial capital&rdquo;. The passage lists the first "
                  "kind: banks spreading and concentrating, and businesses keeping smaller "
                  "reserves of cash because the banks keep it for them."),
            ("p", "He places the plain conversion in two phases of the cycle. Just after a crisis "
                  "industrial capital is contracted, and &ldquo;the money-capital, which was "
                  "formerly employed in production and commerce, appears as unemployed loan "
                  "capital&rdquo;. In the early recovery it is lent again, but cheaply, because "
                  "the industrialist &ldquo;prescribes the conditions for the money "
                  "capitalist&rdquo;. Of the first phase Marx says that &ldquo;the superfluity of "
                  "loan capital is the direct opposite of the expression of actual "
                  "accumulation&rdquo;."),
            ("p", "The lab takes Volume II's numbers, which you met in “Turnover Time and the "
                  "Capital Advanced”: a working period of 9 weeks at £100 a week and 3 weeks of "
                  "circulation. Capital I covers the working period, £900; capital II keeps work "
                  "going while the product circulates, £300; the business ties up £1,200. In the "
                  "contract preset the business halves its scale to £50 a week. Its advance falls "
                  "to £600, and the lab prints £600 released. That £600 is the money capital "
                  "&ldquo;formerly employed in production&rdquo;, now lying in a bank as a "
                  "deposit. The steady preset keeps £100 a week and releases nothing; the expand "
                  "preset raises the outlay to £150 and ties up £600 more."),
            ("p", "Course 7's version of this preset halved prices, not scale, and Chapter 32 "
                  "makes the difference count. A fall in the prices of materials sets capital "
                  "free and leaves the business able to do as much as before: it is &ldquo;an "
                  "actual release of a portion of formerly tied up capital&rdquo;. A contraction "
                  "sets the same sum free because less is being produced. Both are deposited, "
                  "and both, Marx says, &ldquo;influences equally the money-market and the rate "
                  "of interest&rdquo;. The lab's £600 is the same either way; what it means is "
                  "not."),
            ("p", "Then the spread of banking. The Bank Committee of 1858 reported that the "
                  "London stock banks had increased their deposits &ldquo;from 8,850,774 pounds "
                  "sterling in 1847 to 43,100,724 pounds sterling in 1857&rdquo;, much of it from "
                  "people who had never banked before; around Ipswich &ldquo;nearly all farmers, "
                  "even those paying only 50 pounds sterling of rent annually, now have deposits "
                  "in banks&rdquo;. Country banks sent what they could not lend to the London "
                  "bill brokers, who lent it on in the industrial districts. &ldquo;The rural "
                  "depositor imagines to deposit only with his banker, and imagines furthermore "
                  "that, when his banker lends to others, it is done to private persons whom he "
                  "knows.&rdquo;"),
            ("p", "None of this needs more money. A small dealer pays £100 into his bank every "
                  "week; the bank pays it to a manufacturer, who pays his workers, who spend it "
                  "at the dealer's shop, and the dealer banks it again. Marx's arithmetic: at the "
                  "end of twenty weeks &ldquo;he would have deposited 2,000 pounds sterling in "
                  "the bank by means of the same 100 pounds sterling&rdquo;. Hence &ldquo;the mass "
                  "of this loanable capital is different from and independent of the mass of the "
                  "circulating money&rdquo;."),
            ("p", "The second section turns to income. Profit waiting to be invested lies in a "
                  "bank, and so does the part a capitalist means to spend, a little at a time: "
                  "&ldquo;That portion, which is to be spent as revenue, is gradually consumed, "
                  "but forms in the meantime a loan capital of the banker in the form of a "
                  "deposit.&rdquo; Rents, salaries and every other income spent gradually do the "
                  "same, so that even a rise in consumption &ldquo;expresses itself as an "
                  "accumulation of loan capital&rdquo;."),
            ("p", "Between these points come the extracts, and Marx's patience runs out with the "
                  "Governor of the Bank of England, Weguelin, who calls floating capital first "
                  "the bankers' reserves and then bullion. &ldquo;It is truly wonderful, what a "
                  "different meaning and different form all economic categories receive in this "
                  "credit jargon of the money market.&rdquo; In it &ldquo;money is capital, bullion "
                  "is capital, bank notes are currency, capital is a commodity, debts are "
                  "commodities&rdquo;."),
            ("p", "The view the chapter has in its sights is the classical one, which John "
                  "Stuart Mill put in his Principles of 1848: capital is the result of "
                  "saving. On that account a loan is always some saver's abstinence lent out, and "
                  "the rate of interest is the price of waiting. Marx does not deny that saved "
                  "profit becomes loan capital; that is his second route. What the chapter adds "
                  "is the first route, in which the mass on offer grows or shrinks with no saving "
                  "at all. Later theories of the supply of loans, such as Dennis Robertson's "
                  "loanable funds in the 1930s, also count released hoards and new bank credit "
                  "beside saving; how much each source weighs in a given year is a question of "
                  "fact the chapter does not try to answer."),
            ("p", "If the mass of loan capital can grow for so many reasons, what does a crisis "
                  "take away? “Money Capital and Real Capital III” closes the three chapters "
                  "with the demand for loans in a panic."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "advance",
            "money_unit": "£",
            "preset": "contract",
            "presets": [
                {"id": "contract", "label": "Marx's 9 weeks and 3 at £100 a week, then the business halves: £50 a week",
                 "working_weeks": 9, "circulation_weeks": 3, "weekly_outlay": 100,
                 "new_outlay": 50, "year_weeks": 50,
                 "expect": {"tuAdvance": "£1,200 = I £900 + II £300", "tuFreed": "£600 released"}},
                {"id": "steady", "label": "The same business at the same scale",
                 "working_weeks": 9, "circulation_weeks": 3, "weekly_outlay": 100,
                 "new_outlay": 100, "year_weeks": 50,
                 "expect": {"tuFreed": "£0 released"}},
                {"id": "expand", "label": "The same business expands: £150 a week",
                 "working_weeks": 9, "circulation_weeks": 3, "weekly_outlay": 100,
                 "new_outlay": 150, "year_weeks": 50,
                 "expect": {"tuFreed": "£600 more tied up"}},
            ],
            "panel_title": "Capital a change of scale sets free",
            "panel_intro": (
                "The working period, the circulation period, the weekly outlay and the new weekly "
                "outlay go in, with a 50-week year. The lab computes the capital advanced before "
                "the change and the capital released, or tied up, after it. Released capital "
                "lies in the bank as a deposit: loan capital that nobody saved."
            ),
        }),
        "steps_title": "Finding the capital a contraction releases",
        "steps_intro": "Four steps for a business that changes its weekly outlay.",
        "steps": [
            ("Add the periods",
             "Add the working period and the circulation period: the weeks for which each "
             "week's outlay is tied up before it returns."),
            ("Compute the advance before",
             "Multiply the weeks by the old weekly outlay."),
            ("Compute the advance after",
             "Multiply the same weeks by the new weekly outlay."),
            ("Subtract and say where it goes",
             "The difference is capital released, if the outlay fell, or tied up, if it rose. "
             "Released capital goes to the bank and appears as loan capital."),
        ],
        "worked": {
            "title": "Marx's 9 weeks and 3, at half the scale",
            "intro": [
                "A business works 9 weeks and circulates its product for 3, at £100 a week. After "
                "a crisis it halves its scale. How much capital does it release?",
            ],
            "lines": [
                "before:  (9 + 3) · £100 = £1,200",
                "after:  (9 + 3) · £50 = £600",
                "released:  £1,200 − £600 = £600",
            ],
            "after": [
                "The £600 lies in the business's bank account and the bank lends it. Loan capital "
                "has grown by £600 while production has shrunk by half, and nobody has saved a "
                "penny.",
            ],
        },
        "quiz_title": "Loan capital without saving",
        "quiz": [
            {"q": "A business works 6 weeks and circulates for 2, spending £80 a week. It cuts the "
                  "outlay to £60 a week. How much capital is released?",
             "a": ["£160", "£120", "£40", "£480"],
             "c": 0,
             "why": "Before, `8 · 80 = 640`; after, `8 · 60 = 480`; released, `640 − 480 = 160`. "
                    "Six weeks alone gives £120, two weeks alone £40, and £480 is the new advance, "
                    "not the sum released."},
            {"q": "Just after a crisis, loan capital is superabundant. What does Chapter 31 say "
                  "this expresses?",
             "a": ["A stagnation of industrial capital",
                   "A rapid accumulation of real capital",
                   "A rise in workers' savings",
                   "An over-issue of notes by the Bank of England"],
             "c": 0,
             "why": "Marx: &ldquo;The superabundance of loan capital expresses in the first case a "
                    "stagnation of industrial capital&rdquo;. It is the money that production has "
                    "let go, not new saving or new notes."},
            {"q": "A dealer pays £100 into his bank each week, and the same £100 comes back to him "
                  "through the bank, a manufacturer and his workers. After twenty weeks he has "
                  "deposited £2,000. What does Marx take this to show?",
             "a": ["That deposits can be far larger than the money circulating",
                   "That the dealer has saved £2,000",
                   "That the bank has created £1,900 of new notes",
                   "That the money circulates at a loss"],
             "c": 0,
             "why": "Marx: &ldquo;the mass of this loanable capital is different from and independent "
                    "of the mass of the circulating money&rdquo;. The dealer spent and was paid "
                    "the same £100 twenty times; no notes were added and nothing was saved."},
            {"q": "A landowner receives £1,200 of rent on New Year's Day and spends it evenly "
                  "over the year. On Marx's account, what is the money while it waits?",
             "a": ["A loan capital of the banker, in the form of a deposit",
                   "A hoard withdrawn from circulation",
                   "Productive capital of the landowner",
                   "Nothing, since revenue is not capital"],
             "c": 0,
             "why": "Revenue spent gradually &ldquo;forms in the meantime a loan capital of the "
                    "banker in the form of a deposit&rdquo;. It is not a hoard in a strongbox, "
                    "and it never becomes the landowner's own productive capital."},
        ],
        "mistakes": [
            ("Thinking loan capital is only savings out of income",
             "In the contract preset a business halves its scale and £600 of circulating capital "
             "lands in its bank account: the lab prints £600 released. Nobody saved it. Marx's "
             "other routes, the spread of banking and the dealer's £100 that comes back every "
             "week, need no saving either. Saved profit is one source among several."),
            ("Reading a rise in deposits as proof that production is growing",
             "The London stock banks' deposits grew almost fivefold between 1847 and 1857, and "
             "the Committee found much of it came &ldquo;from sources, which were formerly not "
             "available for this purpose&rdquo;: new depositors, not new production."),
            ("Treating all released capital as a sign of health",
             "Capital released by cheaper materials leaves the business doing as much as before; "
             "capital released by a contraction is, in the phase after a crisis, &ldquo;the "
             "direct opposite of the expression of actual accumulation&rdquo;. In the bank the two "
             "look the same."),
        ],
        "standard": (
            "Finish when you can compute the capital a change of scale releases.",
            "Given the working period, the circulation period and the weekly outlay before and "
            "after a change, compute the capital advanced each time and the capital released or "
            "tied up, and say in what form the released capital reaches the money market."
        ),
        "note": (
            "The 9 weeks, 3 weeks and £100 a week are Marx's figures from Volume II, Chapter 15; "
            "Chapter 31 gives none of its own, and the halving to £50 is illustrative. The lab "
            "assumes the whole sum released is deposited at once, and it ignores the weeks a "
            "business needs to wind down."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 3, l. 4486 (stringency). Inline: l. 4462 (paying, buying),
    # l. 4488 (both sides right and wrong), l. 4472 (£150 for £100),
    # l. 4474 (Overstone's attempt), l. 4476 (supply falls), l. 4400 (revenue),
    # l. 4412 (plethora), l. 4416-4418 (last illusion), l. 4492 (few millions;
    # a bank's credit), l. 4733 (Chapter 33: only cash payment).
    {
        "slug": "money-capital-and-real-capital-iii",
        "title": "Money Capital and Real Capital III",
        "module": "Chapter 32 · Money-Capital and Actual Capital. III",
        "one_line": "In a crash firms borrow to pay debts, not to buy: what is scarce is money as means of payment, while unsold goods fill the warehouses.",
        "summary": (
            "Chapter 32 ends Marx's inquiry into money capital and real capital with the demand "
            "for loans in a crisis. Settle the same chain of bills while it holds, after one "
            "debtor fails to pay, and once credit has stopped altogether, with the goods and "
            "their prices unchanged, and see why Marx says both sides of the old debate about "
            "crises were right and wrong."
        ),
        "key": [
            "in a crash firms borrow to pay",
            "in a recovery they borrow to buy",
            "the chain holds: cash needed £0",
            "one default: cash needed £100",
            "credit stops: every sale in cash",
        ],
        "key_label": "Borrowing to pay and borrowing to buy",
        "concepts_intro": (
            "The chapter has two halves: the last word on where loan capital comes from, and "
            "then what the demand for it is in each phase of the cycle."
        ),
        "concepts": [
            ("Means of payment",
             "Money that settles a debt already contracted, as against money that buys. Volume I "
             "introduced the distinction; in a crash it decides who survives."),
            ("Plethora of money capital",
             "More loan capital than can find borrowers. Marx says it shows that capitalist "
             "production has limits, not that there is nothing left to produce."),
            ("Money crisis",
             "The moment when credit stops and money is the only thing that settles a debt, so "
             "that commodities are sold at any price to get it."),
        ],
        "read_title": "The passage first, then the two sides it judges",
        "read_intro": (
            "The passage comes near the end of the chapter. Its second clause contains what "
            "looks like a slip in the Kerr text; the lesson reads it after the passage."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 32.</strong> &ldquo;In times of stringency the "
                  "demand after loan capital is a demand for means of payment and nothing else; "
                  "it is by no means a demand for money as a means of payment. The rate of "
                  "interest may rise very high at the same time, regardless of whether real "
                  "capital, that is, productive and commodity-capital, exists in abundance or is "
                  "scarce.&rdquo;"),
            ("p", "In a financial panic the news reports that firms cannot get cash, and some "
                  "of those firms have warehouses full of goods. That is the scene Marx is "
                  "describing. The demand is for something to pay with, at any price, whatever "
                  "the state of the real capital."),
            ("p", "As printed, the passage's second clause contradicts the first. Earlier in the "
                  "chapter Marx draws the contrast it needs: in a crisis &ldquo;every one borrows "
                  "only for the purpose of paying, in order to settle previously contracted "
                  "obligations&rdquo;, while in the recovery loan capital &ldquo;is demanded for "
                  "the purpose of buying&rdquo;. Read the second clause as <em>not a demand for "
                  "money as a means of purchase</em> and the passage says what that contrast "
                  "says. This lesson reads it so, and flags the reading as its own."),
            ("p", "The lab settles one chain of bills three ways. In the prosperity preset A owes "
                  "B £100, B owes C £100 and C owes A £100, every bill for goods delivered. Set "
                  "off, they cancel: cash needed £0. In the crisis preset A cannot pay B. Nothing "
                  "about the cloth, yarn or cotton has changed, and their prices sum to £300 as "
                  "before, but B still owes C £100 with nothing coming in: cash needed £100. It "
                  "is Course 1's broken chain from “Hoards and Means of Payment”, now as a "
                  "picture of 1847. In the cash-only preset credit has stopped. As Chapter 33 "
                  "puts it, &ldquo;no man can make use of a promise to pay, since every one "
                  "wants to accept only cash payment&rdquo;; every sale is paid in money, and with "
                  "each note held rather than passed on, £300 is needed."),
            ("p", "So who was right about 1847, those who said the country lacked money or those "
                  "who said it lacked capital? &ldquo;This is the point, where both sides of the "
                  "current theory are right and wrong in their opinion about crisis.&rdquo; Those "
                  "who speak only of means of payment have in view the owners of good bills, who "
                  "lack only conversion into money; or they are &ldquo;fools who believe that it "
                  "is the duty and power of banks to transform all bankrupt swindlers into "
                  "solvent and solid capitalists by means of pieces of paper&rdquo;. Those who "
                  "speak of a lack of capital are &ldquo;harping on words, since in such times "
                  "there is a mass of inconvertible capital in consequence of over-imports and "
                  "overproduction&rdquo;, or else they mean the speculators who have lost "
                  "capital that no bank can give back."),
            ("p", "Overstone, the chapter's target again, called the demand for loans a demand "
                  "for capital. Marx says it is a demand for commodities, and a dearer one needs "
                  "more money: a merchant who now pays £150 for goods that cost £100 must borrow "
                  "£150, and at 5% &ldquo;he would now have to pay 7½ pounds sterling of interest "
                  "as against 5 pounds sterling of former times&rdquo;. The rate is the same; the "
                  "sum is larger. And if the goods are dearer because fewer are on the market, the "
                  "same sum may buy them, and the demand for loans need not rise at all. "
                  "&ldquo;The whole attempt of Mr. Overstone consists in pretending that the "
                  "interests of loan capital and of industrial capital are identical&rdquo;."),
            ("p", "The first half of the chapter finishes the account of where loan capital "
                  "comes from. Revenue meant for consumption passes through the banks first, so "
                  "that its growth &ldquo;represents itself in the first instance as an "
                  "accumulation of money-capital&rdquo;. And when profits pile up faster than they "
                  "can be invested, &ldquo;such a plethora of loanable money-capital proves merely "
                  "that capitalist production has its limits&rdquo;. Marx adds at once that a "
                  "plethora &ldquo;does not necessarily indicate an overproduction, nor even a "
                  "lack of spheres of investment for capital&rdquo;."),
            ("p", "Here too is the chapter's sharpest sentence about saving. In the division of "
                  "labour, actual saving falls to &ldquo;those who receive the smallest share of "
                  "such elements, and who frequently enough lose even their savings, as do the "
                  "laborers when banks fail&rdquo;, while the industrialist commands the savings "
                  "of others. &ldquo;The last illusion of the capitalist system, to the effect "
                  "that capital is the fruit of ones own labor and saving, is thereby "
                  "destroyed.&rdquo;"),
            ("p", "Why must a money crisis come at all? Because credit money is money only while "
                  "it can be turned into gold, and when gold leaves the country the banks defend "
                  "convertibility by raising the rate of interest. &ldquo;For the sake of a few "
                  "millions of money many millions of commodities must therefore be "
                  "sacrificed.&rdquo; Marx blames the excess on Overstone's legislation, but says "
                  "the basis &ldquo;is given with the basis of the mode of production "
                  "itself&rdquo;."),
            ("p", "Walter Bagehot drew the opposite lesson in <em>Lombard Street</em> (1873): in a "
                  "panic the Bank of England should lend freely, at a high rate, to anyone with "
                  "good security, and the panic will pass. Central banks still state their role "
                  "in roughly those terms. What in the chapter bears on it is the distinction "
                  "between holders of good securities and bankrupt swindlers, and a sentence near "
                  "the end: &ldquo;so long as the credit of a bank is not shaken, it will "
                  "alleviate the panic in such cases by increasing the credit money, and intensify "
                  "it by contracting this money&rdquo;. Whether lending that way prevents crises or "
                  "only shortens them is not something the chapter settles."),
            ("p", "If notes are what a panic wants, who decides how many there are? “The Medium "
                  "of Circulation in the Credit System” takes the notes themselves."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "payments",
            "money_unit": "£",
            "preset": "prosperity",
            "presets": [
                {"id": "prosperity", "label": "The chain holds: three bills of £100 in a circle",
                 "goods": [{"name": "cotton", "value_hours": 200},
                           {"name": "yarn", "value_hours": 200},
                           {"name": "cloth", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 300, "payments_due": 300, "cancelling": 300,
                 "bills": [{"from": "A", "to": "B", "amount": 100, "backed": True},
                           {"from": "B", "to": "C", "amount": 100, "backed": True},
                           {"from": "C", "to": "A", "amount": 100, "backed": True}],
                 "expect": {"moNeeded": "£0", "moNetted": "£0"}},
                {"id": "crisis", "label": "The same chain, and A cannot pay B",
                 "goods": [{"name": "cotton", "value_hours": 200},
                           {"name": "yarn", "value_hours": 200},
                           {"name": "cloth", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 300, "payments_due": 200, "cancelling": 100,
                 "bills": [{"from": "A", "to": "B", "amount": 100, "backed": True},
                           {"from": "B", "to": "C", "amount": 100, "backed": True},
                           {"from": "C", "to": "A", "amount": 100, "backed": True}],
                 "default": 1,
                 "expect": {"moNeeded": "£100", "moNetted": "£100"}},
                {"id": "cash-only", "label": "Credit has stopped: every sale in cash, no note passed on",
                 "goods": [{"name": "cotton", "value_hours": 200},
                           {"name": "yarn", "value_hours": 200},
                           {"name": "cloth", "value_hours": 200}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "credit_sales": 0, "payments_due": 0, "cancelling": 0,
                 "bills": [],
                 "expect": {"moNeeded": "£300", "moNetted": "£0"}},
            ],
            "panel_title": "One chain of payments, before and in a crisis",
            "panel_intro": (
                "Each bill runs from the party who pays to the party who is paid; a defaulted "
                "bill is left out of the netting. The goods and their prices stay the same in "
                "every preset. The tiles are the money needed in circulation and the cash needed "
                "to settle the bills."
            ),
        }),
        "steps_title": "Settling a chain before and after a default",
        "steps_intro": "Four steps, with the goods and prices held fixed.",
        "steps": [
            ("Write the bills",
             "List each debt as a bill from payer to payee, with its amount."),
            ("Net each party",
             "For each party, add what it is owed and subtract what it owes."),
            ("Add the positive balances",
             "The cash needed to settle is the sum of the positive balances: what the creditors "
             "must actually be paid in money."),
            ("Strike out the bill that fails",
             "Leave the defaulted bill out and net again. The difference is a new demand for "
             "means of payment, with nothing real changed."),
        ],
        "worked": {
            "title": "One chain, before and after a default",
            "intro": [
                "A owes B £100, B owes C £100 and C owes A £100, each for goods delivered. Then A "
                "cannot pay. How much cash does the chain need, before and after?",
            ],
            "lines": [
                "before:  A 0,  B 0,  C 0;  cash needed £0",
                "A fails:  A +100,  B 0,  C −100",
                "cash needed:  £100",
                "goods and prices:  unchanged, £300",
            ],
            "after": [
                "Nothing real was lost between the two lines. What appeared was a demand for £100 "
                "of means of payment, which C must find before the day the bill falls due.",
            ],
        },
        "quiz_title": "Means of payment in a crisis",
        "quiz": [
            {"q": "A owes B £200, B owes C £200 and C owes A £200. The bill from B to C is not "
                  "paid. How much cash does settlement now need?",
             "a": ["£200", "£0", "£400", "£600"],
             "c": 0,
             "why": "With that bill struck out, A owes B £200 and C owes A £200. A's balance is 0, "
                    "B is owed £200 and C owes £200, so £200 must change hands in cash. Zero is "
                    "the unbroken circle; £600 is the bills' gross."},
            {"q": "A merchant now pays £150 for goods that used to cost £100, and borrows the "
                  "whole sum at 5%. What has risen?",
             "a": ["The interest he pays, from £5 to £7½",
                   "The rate of interest, from 5% to 7½%",
                   "His profit, by £50",
                   "Nothing, since the goods are the same"],
             "c": 0,
             "why": "Marx's example: at 5% the merchant &ldquo;would now have to pay 7½ pounds "
                    "sterling of interest as against 5 pounds sterling of former times&rdquo;. "
                    "The rate is unchanged; he borrows more. Dearer goods do not raise his "
                    "profit."},
            {"q": "On the chapter's account, who is right that a crisis is only a lack of means "
                  "of payment?",
             "a": ["Those who have the owners of good securities in view",
                   "Everyone, since all capital is intact in a crisis",
                   "No one, since a crisis is a scarcity of real capital",
                   "The speculators, once a bank lends them notes"],
             "c": 0,
             "why": "Marx says those who speak of means of payment &ldquo;have either the owners "
                    "of bona fide securities alone in view&rdquo;, or are fools about swindlers. "
                    "Capital is not all intact, and real capital is not scarce: warehouses are "
                    "full."},
            {"q": "A manufacturer's household income grows, and it is paid into a bank and drawn "
                  "out week by week as it is spent. What does Chapter 32 say this growth shows "
                  "up as first?",
             "a": ["An accumulation of money capital",
                   "An accumulation of productive capital",
                   "A rise in the rate of profit",
                   "A rise in hoarding"],
             "c": 0,
             "why": "Revenue meant for consumption &ldquo;represents itself in the first instance "
                    "as an accumulation of money-capital&rdquo;. It is not productive capital, "
                    "and it is lent, not hoarded; the rate of profit does not enter."},
        ],
        "mistakes": [
            ("Thinking that in a crisis capital is scarce",
             "Between the prosperity and crisis presets nothing about the goods changes, and the "
             "cash needed goes from £0 to £100. For holders of good bills what is scarce is "
             "means of payment, while unsold goods are in excess. Marx adds that the speculator "
             "really has lost capital, and no amount of notes gives it back."),
            ("Thinking dearer commodities must raise the rate of interest",
             "Dearer goods raise the sum borrowed, not the rate, as the £150 merchant shows; and "
             "if they are dearer because fewer are offered, the same sum buys them and the demand "
             "for loans may not rise at all."),
            ("Taking a plethora of loan capital as proof of overproduction",
             "Marx says it proves &ldquo;merely that capitalist production has its limits&rdquo;, "
             "and adds that it &ldquo;does not necessarily indicate an overproduction, nor even a "
             "lack of spheres of investment for capital&rdquo;."),
        ],
        "standard": (
            "Finish when you can show what a default does to the demand for means of payment.",
            "Given a chain of bills and one that fails, net each party's balance before and "
            "after, compute the cash each settlement needs, and say what changed and what did "
            "not."
        ),
        "note": (
            "The chain and its £100 bills are illustrative; Chapter 32 gives no such example. "
            "The cash-only preset sets velocity to 1 to stand for notes held back rather than "
            "passed on; how far circulation slows in a real panic is a matter of record, not of "
            "this lab."
        ),
    },
    # ---------------------------------------------------------------- 09
    # Kerr vol. 3, l. 4579 (requirements of business). Inline: l. 4573
    # (Scotland), l. 4526 (the law), l. 4567 (Tooke 3094), l. 4569 (Wright
    # 2844), l. 4551 (1844-57), l. 4577 (Kinnear), l. 4516 (stringency, full
    # circulation), l. 4593 (Wright 2930, in Engels' bracket), l. 4595
    # (Gurney), l. 4631 and 4675-4677 (Chapman), l. 4727-4731 (bills),
    # l. 4742 (fictitious capital), l. 4754 (Glyn), l. 4559 (Engels on
    # inconvertible notes), l. 4589 (Gurney 2650-51).
    {
        "slug": "the-medium-of-circulation-in-the-credit-system",
        "title": "The Medium of Circulation in the Credit System",
        "module": "Chapter 33 · The Currency under the Credit System",
        "one_line": "How many convertible notes circulate is set by trade, not by the bank: notes beyond what payments need flow straight back, and in a panic the need doubles because notes are hoarded.",
        "summary": (
            "Chapter 33 argues that, with notes convertible into gold, the requirements of "
            "business alone decide how many notes and coins circulate. Compute the notes a "
            "given sum of prices needs at a given velocity, issue more and watch the excess "
            "flow back, and halve the velocity to see why a panic needs twice the notes while "
            "trade has not grown."
        ),
        "key": [
            "notes needed = sum of prices / velocity",
            "excess notes flow back to the bank",
            "a panic hoards notes: velocity falls",
            "credit speeds every note's turnover",
            "a bank can set the rate in a squeeze",
        ],
        "key_label": "Notes and the needs of trade",
        "concepts_intro": (
            "The chapter applies Volume I's law of circulation to bank notes, and the evidence "
            "is the reports of 1847 to 1858."
        ),
        "concepts": [
            ("The law of circulation",
             "Given the velocity of money and the economy of payments, the money in circulation "
             "is set by the prices of commodities and the mass of transactions. Marx says the "
             "same law rules notes."),
            ("Reflux",
             "The return of notes the public does not need, as deposits or as repayments of "
             "loans. It is why a bank of issue cannot keep extra notes out."),
            ("Convertibility",
             "The holder's right to change a note for gold on demand. The chapter's argument "
             "assumes it; inconvertible paper is set aside."),
        ],
        "read_title": "The rule first, then the evidence and the panic",
        "read_intro": (
            "The passage follows a run of evidence from bankers in England, Scotland and Ireland. "
            "It sums up what they said."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 33.</strong> &ldquo;Hence only the requirements of "
                  "business itself exert an influence on the quantity of circulating money—notes "
                  "and gold.&rdquo;"),
            ("p", "Try to give a shopkeeper more cash than he needs and by evening the surplus "
                  "is in the bank. A Scottish banker told the committee that this is the whole "
                  "story of note issue in Scotland: everyone banks what he does not need that "
                  "day, &ldquo;so that at the end of every business day all the money is in the "
                  "banks, except what each carries in his pockets&rdquo;. The notes in circulation "
                  "are the notes people are using; the rest are back where they came from."),
            ("p", "Go back to the passage. The &ldquo;requirements of business&rdquo; are the "
                  "law from Volume I's chapter on money: &ldquo;the mass of the actually "
                  "circulating money, assuming the velocity of currency and the economy of "
                  "payments to be given, is determined by the prices of commodities and the mass "
                  "of transactions. The same law rules the circulation of notes.&rdquo; The words "
                  "&ldquo;notes and gold&rdquo; matter: Marx means the whole of the currency, "
                  "paper and metal, and only paper convertible into gold."),
            ("p", "The witnesses say so in their own trade. Thomas Tooke: &ldquo;The Bank has no "
                  "power to expand the amount of its notes in the hands of the public at its own "
                  "arbitrary will&rdquo;. J. C. Wright, thirty years a banker in Nottingham, on "
                  "the Bank of England: &ldquo;every surplus of the circulation will pass over "
                  "into the deposits and thus assume another form&rdquo;."),
            ("p", "The lab computes the notes trade needs from a sum of prices and a velocity, "
                  "and sets an issue against it. In the needs preset the cotton, yarn and cloth "
                  "come to £600 and each note serves 4 times: £150 is needed, £150 is issued, "
                  "nothing comes back. In the over-issue preset the bank pushes out £200 against "
                  "the same £150 of needs, and the lab prints £50 of notes that flow back. They "
                  "return as deposits or as loans repaid early, and the circulation stays at "
                  "£150."),
            ("p", "The figures in the chapter point the same way. The notes of the Bank of "
                  "England in the public's hands were a little lower in 1857 than in 1844, "
                  "&ldquo;although the commercial business had more than doubled&rdquo;, because "
                  "the London Clearing House let banks settle with each other without large "
                  "notes. Between September 1846 and April 1847 the Bank's gold fell by six "
                  "millions and its notes in circulation hardly moved: &ldquo;no contraction of "
                  "the currency took place in spite of the export of 6 million pounds sterling of "
                  "precious metal&rdquo;."),
            ("p", "Credit enters through velocity. A note paid in, lent out, paid in again does "
                  "more work in a week than a coin that passes only by sales, and the banks, the "
                  "bill brokers and the Clearing House all make the same money serve more "
                  "often. That is why, in a pamphlet Marx quotes, &ldquo;a sharp stringency in the "
                  "money-market generally coincides with a full circulation&rdquo;: when credit "
                  "falters, velocity falls and more notes are needed for the same trade."),
            ("p", "Engels adds a long passage of his own on what happens next. In the crisis the "
                  "notes, &ldquo;yesterday still so plentiful, have disappeared from the "
                  "market&rdquo;, and Wright again: &ldquo;During the alarm,&rdquo; he says, "
                  "&ldquo;the country needs twice as much currency as in ordinary times, because "
                  "the medium of circulation is stored up by bankers and others.&rdquo; In the "
                  "crisis-demand preset each note serves twice instead of 4 times, and the same "
                  "£600 of goods needs £300. Samuel Gurney put the notes locked away in October "
                  "1847 at 4 to 5 million pounds."),
            ("p", "Chapman, Gurney's partner, gives the bill brokers' view of the whole system: "
                  "&ldquo;We have 300 million pounds sterling worth of obligations, the payment of "
                  "which in coin of the realm may be demanded at any moment; and this coin of the "
                  "realm, if we use all of it for this purpose, amounts to 23 million pounds "
                  "sterling, or thereabout&rdquo;. Marx's comment: &ldquo;Hence we have in times "
                  "of crisis the sudden change of the credit system into a monetary "
                  "system.&rdquo;"),
            ("p", "Bills of exchange follow the same rule in ordinary times, but nothing returns "
                  "an excess of them. The <em>Economist</em> put it plainly: &ldquo;Bank notes "
                  "payable on presentation can never stay out in excess, because the excess would "
                  "always return to the bank for exchange, while two-months drafts may be issued "
                  "in great superabundance&rdquo;. In a squeeze the bills multiply and get worse; "
                  "in the crash they stop circulating at all."),
            ("p", "None of this leaves the Bank of England powerless. Its notes without gold "
                  "behind them are, for the Bank, &ldquo;additional, even if fictitious, "
                  "capital&rdquo; that earns interest, and in a squeeze, a London banker said, "
                  "&ldquo;the Bank of England commands the rate of interest&rdquo;. It cannot "
                  "choose how many notes circulate; it can choose what they cost."),
            ("p", "The opposing view is the Currency School's, which the next lesson takes in "
                  "full. Overstone and his allies held that the quantity of notes is the lever "
                  "on prices: issue more and prices rise, gold leaves, and the country is drawn "
                  "into speculation, so the issue must be fixed by law. A later and different "
                  "theory, Milton Friedman's monetarism in the 1960s, also held that the "
                  "authorities can fix the quantity of money and that prices follow it, though "
                  "for a world without convertible notes. What in the chapter bears on both is "
                  "its limit, which Engels states in a bracket: &ldquo;Inconvertible bank notes "
                  "are not taken into consideration at all here&rdquo;. The reflux the lab shows "
                  "depends on a holder's right to gold."),
            ("p", "The Currency School got its law in 1844. “The Currency Principle and the Bank "
                  "Act of 1844” computes what the law did when the panic came."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "bank-act",
            "money_unit": "£",
            "preset": "needs",
            "presets": [
                {"id": "needs", "label": "£600 of goods, each note serving 4 times, £150 issued",
                 "goods": [{"name": "cotton", "value_hours": 400},
                           {"name": "yarn", "value_hours": 400},
                           {"name": "cloth", "value_hours": 400}],
                 "gold_hours_per_unit": 2, "velocity": 4,
                 "issue": 150, "reserve": 200, "fiduciary": 300, "demand": 150,
                 "expect": {"moNeeded": "£150", "moReturned": "£0"}},
                {"id": "over-issue", "label": "The same trade, and the bank issues £200",
                 "goods": [{"name": "cotton", "value_hours": 400},
                           {"name": "yarn", "value_hours": 400},
                           {"name": "cloth", "value_hours": 400}],
                 "gold_hours_per_unit": 2, "velocity": 4,
                 "issue": 200, "reserve": 200, "fiduciary": 300, "demand": 150,
                 "expect": {"moNeeded": "£150", "moReturned": "£50"}},
                {"id": "crisis-demand", "label": "A panic: notes are held back, each serves twice",
                 "goods": [{"name": "cotton", "value_hours": 400},
                           {"name": "yarn", "value_hours": 400},
                           {"name": "cloth", "value_hours": 400}],
                 "gold_hours_per_unit": 2, "velocity": 2,
                 "issue": 300, "reserve": 200, "fiduciary": 300, "demand": 300,
                 "expect": {"moNeeded": "£300", "moReturned": "£0"}},
            ],
            "panel_title": "The notes trade needs, and the notes that come back",
            "panel_intro": (
                "The goods and their values in hours, the hours in one pound of gold and the "
                "velocity of a note go in, with the notes the bank issues. The lab computes the "
                "notes the circulation needs and the excess that flows back. The cap and the "
                "unmet demand belong to the next lesson; here the cap is set high enough never "
                "to bind."
            ),
        }),
        "steps_title": "Finding the notes trade needs",
        "steps_intro": "Four steps for a circulation of convertible notes.",
        "steps": [
            ("Price the goods",
             "Divide each commodity's value in hours by the hours in a pound of gold, and add "
             "the prices."),
            ("Divide by the velocity",
             "Divide the sum of prices by the number of times each note serves in the period. "
             "This is the circulation's need."),
            ("Set the issue against it",
             "Any issue above the need flows back to the bank as deposits or repayments; the "
             "circulation stays at the need."),
            ("Change the velocity, not the goods",
             "In a panic notes are held back and serve fewer times. The need rises with the same "
             "goods and the same prices."),
        ],
        "worked": {
            "title": "An over-issue and a panic",
            "intro": [
                "Goods priced at £600 circulate, and each note serves 4 times. The bank issues "
                "£200. Then panic halves the velocity. How many notes stay out each time?",
            ],
            "lines": [
                "needed:  £600 / 4 = £150",
                "issued £200:  £200 − £150 = £50 flows back",
                "panic:  £600 / 2 = £300 needed",
            ],
            "after": [
                "The bank could not keep the extra £50 out in good times, and in the panic the "
                "public needs twice the notes for the same goods. Neither number was the bank's "
                "choice.",
            ],
        },
        "quiz_title": "Notes and the requirements of business",
        "quiz": [
            {"q": "Goods priced at £900 circulate and each note serves 3 times. A bank issues "
                  "£400. How many notes flow back?",
             "a": ["£100", "£0", "£400", "£300"],
             "c": 0,
             "why": "Needed: `900 / 3 = 300`. Issued: 400. Back: `400 − 300 = 100`. Three hundred "
                    "is what stays out, not what returns."},
            {"q": "In a panic prices are unchanged but each note serves 2 times instead of 4. "
                  "What happens to the notes needed for £600 of goods?",
             "a": ["They double, from £150 to £300",
                   "They halve, from £150 to £75",
                   "They stay at £150",
                   "They fall to nothing"],
             "c": 0,
             "why": "`600 / 4 = 150` and `600 / 2 = 300`. Wright's &ldquo;twice as much "
                    "currency&rdquo; is this: the notes are stored up, so the same trade needs "
                    "more of them."},
            {"q": "Between September 1846 and April 1847 the Bank's gold fell by about six "
                  "millions and its notes in circulation hardly changed. What does the chapter "
                  "take this to show?",
             "a": ["That the circulation did not depend on the gold reserve",
                   "That the Bank had over-issued its notes",
                   "That prices must have risen",
                   "That the gold went into domestic circulation"],
             "c": 0,
             "why": "Marx says the circulation of notes &ldquo;is just as independent of the state "
                    "of the gold reserve&rdquo; as of the Bank's will, adding that this holds "
                    "only so far as legislation does not decide differently. Kinnear says the "
                    "gold was exported."},
            {"q": "Chapman says £300 million of obligations rest on about £23 million of coin. "
                  "What does Marx call what happens to them in a crisis?",
             "a": ["The sudden change of the credit system into a monetary system",
                   "The automatic adjustment of the currency",
                   "The conversion of revenue into capital",
                   "The depreciation of gold"],
             "c": 0,
             "why": "&ldquo;Hence we have in times of crisis the sudden change of the credit "
                    "system into a monetary system.&rdquo; Every promise is called for in money "
                    "at once, and there is not enough."},
        ],
        "mistakes": [
            ("Thinking the bank decides how much money circulates",
             "The Currency School held that the issue of notes fixes the circulation and, through "
             "it, prices. In the over-issue preset the bank issues £200 against needs of £150, "
             "and £50 comes straight back. Tooke allowed the Bank one power: to reduce the "
             "notes, &ldquo;but only by means of a very forcible operation&rdquo;."),
            ("Reading a large note circulation as easy money",
             "Gurney said that in October 1847, with £20.8 million of notes out, notes could not "
             "be had; in March 1848, with £17.7 million, &ldquo;this is much more than is "
             "needed&rdquo;. What decides is how hard the notes are working, not how many there "
             "are."),
            ("Applying the reflux to any paper money",
             "The argument needs notes that can be turned into gold on demand. Engels sets "
             "inconvertible notes aside, as falling under Volume I's laws of paper money."),
        ],
        "standard": (
            "Finish when you can compute the notes a circulation needs and the excess that returns.",
            "Given a sum of prices, a velocity and an issue, compute the notes needed and the "
            "notes that flow back, and show what a fall in velocity does with the goods "
            "unchanged."
        ),
        "note": (
            "The £600 of goods and the velocities are illustrative. The lab treats velocity as "
            "one number for the period and ignores payments, which the chapter's law includes "
            "under the economy of payments; it also treats the reflux as immediate, where the "
            "chapter says notes return within days or weeks."
        ),
    },
    # ---------------------------------------------------------------- 10
    # Kerr vol. 3, l. 4839 (Engels: five pounds in gold). Inline: l. 4789-4801
    # (Contribution, quoted by Engels), l. 4813 (Hubbard), l. 4817 (gold and
    # interest), l. 4837 (the Act), l. 4159 (Chapter 29 figures), l. 4843
    # (hasten and intensify; 1847, 1857), l. 4904 (Brown), l. 4873 (Palmer),
    # l. 4869 (Newmarch), l. 4891 and 4897 (Twells), l. 4926-4930 (Overstone),
    # l. 4803 (Tooke and co.), l. 4936 (Chapter 35: 1857 above the maximum).
    # Hubbard's table: Kerr p. 646.
    {
        "slug": "the-currency-principle-and-the-bank-act",
        "title": "The Currency Principle and the Bank Act of 1844",
        "module": "Chapter 34 · The Currency Principle and the English Bank Laws of 1844",
        "one_line": "The 1844 Act capped notes at a fixed sum plus the gold in the Bank, so a drain of gold cut the notes just when a panic wanted more, and the Act had to be suspended at the height of two crises.",
        "summary": (
            "Chapter 34 is the Currency School's theory and its trial in practice. With Marx's "
            "figures for the Bank of England, compute the cap the 1844 Act set on notes, what a "
            "drain of gold does to it, the demand left unmet when a panic arrives, and what "
            "suspending the Act changed."
        ),
        "key": [
            "cap = fixed issue + gold in the Bank",
            "gold out: the cap falls by as much",
            "unmet = demand less the cap",
            "suspended: 25 October 1847",
            "suspended: 12 November 1857",
        ],
        "key_label": "The Act of 1844 in five lines",
        "concepts_intro": (
            "Most of Chapter 34 is in Engels' hand. He supplies the theory from Marx's earlier "
            "book and a description of the Act; Marx's own text is the evidence of the bankers "
            "who worked under it."
        ),
        "concepts": [
            ("The currency principle",
             "Overstone's rule that a currency of notes and gold should change in quantity "
             "exactly as a currency of gold alone would: a note out for every sovereign in, a "
             "note destroyed for every sovereign out."),
            ("Fiduciary issue",
             "The notes the Act allowed the Bank to issue against government securities rather "
             "than gold: 14 millions in 1844."),
            ("Issue department and banking department",
             "The two halves the Act cut the Bank into. The issue department held the gold and "
             "issued notes; the banking department held deposits, with unissued notes as its "
             "reserve."),
        ],
        "read_title": "Engels on the mechanism, then the bankers on the result",
        "read_intro": (
            "The passage is Engels', from his description of the Act inside a bracketed passage "
            "he signed. It states the mechanism in one sentence."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 34.</strong> &ldquo;For every five pounds in gold, "
                  "then, which leave the bank treasury, a five pound note returns to the issue "
                  "department and is destroyed; for every five sovereigns going into the treasury "
                  "a new five pound note passes into circulation.&rdquo;"),
            ("p", "Picture a rule that every time five pounds of gold leaves the country, a "
                  "five-pound note must be taken out of use. In quiet times you would hardly "
                  "notice. The trouble is that gold leaves in the months before a crisis, when "
                  "everyone is about to want notes. That rule was English law from 1844, and "
                  "this chapter is about what it did."),
            ("p", "A word on whose chapter this is. It opens with a bracket by Engels, most of "
                  "which quotes Marx's <em>A Contribution to the Critique of Political "
                  "Economy</em> of 1859; Engels then describes the Act and its crises in a second "
                  "bracket. Between them is Marx's manuscript: extracts from the committees of "
                  "1848 and 1857, with his comments."),
            ("p", "The theory, at its strongest. Ricardo had argued that a currency of gold alone "
                  "corrects itself: too much gold raises prices, gold flows abroad, and prices "
                  "fall again. The Currency School, Overstone, Torrens, Norman and others, "
                  "concluded that a currency of notes must be made to behave the same way, or "
                  "notes would feed speculation and the gold behind them would drain away. In "
                  "the words of Marx's 1859 summary, &ldquo;the issue of bank notes must be "
                  "regulated by the import and export of the precious metals or by the rate of "
                  "exchange&rdquo;. The Act, they said, would make crises impossible."),
            ("p", "Marx's objection in 1859 was that the theory explains a fall in prices by a "
                  "rise in the value of money, which is the same fact twice: &ldquo;Ricardo's "
                  "theory of money was exceedingly convenient, because it lends to a tautology "
                  "the semblance of a statement of casual connection.&rdquo; (Read "
                  "<em>causal</em>; the Kerr text has a misprint.) Chapter 34 adds evidence. "
                  "J. G. Hubbard, a former Governor of the Bank, gave the committee tables showing "
                  "the Bank's gold, the rate of discount and the prices of fifteen principal "
                  "articles. In the first (Kerr, p. 646) the gold stood at £10,471,000 on 1 March "
                  "1838 with discount at 2.75%, and at £2,684,000 on 1 September 1839 with "
                  "discount at 6%; the prices of eight articles rose and five fell. Hubbard's "
                  "summary: gold movements went with the rate of discount, while prices showed "
                  "&ldquo;a complete independence from the amount of the currency&rdquo;. Marx: "
                  "&ldquo;the reduction of the quantity of gold raises only the rate of "
                  "interest&rdquo;."),
            ("p", "The lab computes the Act's cap. Marx's own figures, from Chapter 29: the "
                  "fixed issue is 14 millions; with 14 millions of gold the Bank may issue 28 "
                  "millions of notes; 20 millions are in circulation, so the banking department "
                  "holds the other 8 as its reserve. That is the normal preset: cap £28 million, "
                  "demand £20 million, nothing unmet. In the drain preset 6 millions of gold are "
                  "exported. The cap falls to 22 millions, and the banking department's reserve "
                  "from 8 millions to 2. Every pound of it is a pound the Bank can no longer "
                  "lend."),
            ("p", "Now the panic. Engels writes that the Act &ldquo;directly challenges the "
                  "commercial world to think betimes of laying up a reserve fund of bank notes on "
                  "the eve of a crisis, in other words, to hasten and intensify the crisis&rdquo;. "
                  "In the panic preset the hoarding adds 4 millions to the demand for notes, "
                  "Gurney's figure for 1847, and the demand of 24 millions meets a cap of 22: the "
                  "lab prints £2 million unmet. Twice, on 25 October 1847 and 12 November 1857, "
                  "the government let the Bank exceed the cap, &ldquo;and this sufficed in both "
                  "cases to break the crisis&rdquo;."),
            ("p", "The suspension preset raises the fixed issue by 2 millions and the gap closes. "
                  "What actually happened was smaller. In 1847 the promise alone brought the "
                  "hoarded notes back out and no extra notes were issued; in 1857 the excess "
                  "&ldquo;did not quite reach one million, and this was out for a very short "
                  "time&rdquo;. The lab shows the cap that had to go; history shows that once it "
                  "went, the demand fell back."),
            ("p", "The bankers' evidence is the chapter's body. Palmer, a director since 1811, "
                  "said that in December 1825 the Bank issued 5 or 6 million notes in a week, "
                  "&ldquo;and this relieved the panic of that time considerably&rdquo;; under the "
                  "Act it would have failed. Newmarch counted some 60 changes in the rate of "
                  "discount between 1844 and 1857, against hardly a dozen before. And a "
                  "Liverpool witness said the gold locked in the issue department &ldquo;might "
                  "just as well have been thrown into the sea; for not the least bit of it could "
                  "be used, without breaking the Act of Parliament&rdquo;."),
            ("p", "Who gained? A Birmingham banker, Twells: &ldquo;Should I answer you as a "
                  "banker, I would say that it has operated splendidly&rdquo;, for lending money "
                  "had become very profitable. Asked whether dear money meant cheap capital, he "
                  "said yes, and Marx notes that he is &ldquo;by no means of Overstone's opinion "
                  "that a high rate of interest is the same as dear capital&rdquo;. Engels closes "
                  "the chapter with Overstone's evidence of July 1857, that the country's "
                  "prosperity proved the Act sound: &ldquo;Look about you; consider the present "
                  "condition of the business of this country&rdquo;. In November the Act was "
                  "suspended."),
            ("p", "Engels does not make Tooke's side the winner either: the critics of the "
                  "Currency School, he writes, saw only &ldquo;incompletely&rdquo; into the nature "
                  "of gold and the relation of money to capital. The Act was suspended a third "
                  "time in 1866, after the failure of Overend, Gurney and Co., the bill brokers "
                  "whose partners Gurney and Chapman testify in these chapters. Bagehot's "
                  "<em>Lombard Street</em>, which the last lesson met, was written in the years after it."),
            ("p", "The Act tied the notes to the Bank's gold, and the gold moved with the "
                  "foreign exchanges. “Precious Metal and the Rate of Exchange” follows it "
                  "abroad."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "bank-act",
            "money_unit": "£",
            "preset": "normal",
            "presets": [
                {"id": "normal", "label": "Marx's figures: 14 millions fixed, 14 millions of gold, 20 millions out",
                 "goods": [{"name": "the year's goods", "value_hours": 40000000}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "issue": 20000000, "fiduciary": 14000000, "reserve": 14000000, "demand": 20000000,
                 "expect": {"moCap": "£28,000,000", "moGap": "£0"}},
                {"id": "drain", "label": "6 millions of gold exported",
                 "goods": [{"name": "the year's goods", "value_hours": 40000000}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "issue": 20000000, "fiduciary": 14000000, "reserve": 8000000, "demand": 20000000,
                 "expect": {"moCap": "£22,000,000", "moGap": "£0"}},
                {"id": "panic", "label": "The drain, and 4 millions of notes hoarded in a panic",
                 "goods": [{"name": "the year's goods", "value_hours": 40000000}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "issue": 20000000, "fiduciary": 14000000, "reserve": 8000000, "demand": 24000000,
                 "expect": {"moCap": "£22,000,000", "moGap": "£2,000,000"}},
                {"id": "suspension", "label": "The Act suspended: the fixed issue raised by 2 millions",
                 "goods": [{"name": "the year's goods", "value_hours": 40000000}],
                 "gold_hours_per_unit": 2, "velocity": 1,
                 "issue": 20000000, "fiduciary": 16000000, "reserve": 8000000, "demand": 24000000,
                 "expect": {"moCap": "£24,000,000", "moGap": "£0"}},
            ],
            "panel_title": "The cap on notes under the Act of 1844",
            "panel_intro": (
                "The fixed issue, the gold in the Bank and the public's demand for notes go in. "
                "The lab computes the Act's cap, the fixed issue plus the gold, and the demand "
                "it leaves unmet. The goods and the issue are held at the 20 millions the "
                "circulation needs in ordinary times."
            ),
        }),
        "steps_title": "Computing the Act's cap and the gap",
        "steps_intro": "Four steps, in millions of pounds.",
        "steps": [
            ("Add the fixed issue and the gold",
             "The cap on notes is the fiduciary issue plus the gold in the Bank."),
            ("Subtract the notes out",
             "The cap less the notes in circulation is the banking department's reserve, what it "
             "has to lend and to meet its deposits."),
            ("Take out the gold that leaves",
             "A drain lowers the cap pound for pound, and the reserve with it."),
            ("Set the demand against the cap",
             "If the public's demand for notes exceeds the cap, the difference is unmet unless "
             "the Act is suspended."),
        ],
        "worked": {
            "title": "Marx's 14 and 14, a drain and a panic",
            "intro": [
                "The fixed issue is 14 millions and the gold 14 millions; 20 millions of notes "
                "are out. Then 6 millions of gold leave, and panic raises the demand to 24 "
                "millions. What is unmet?",
            ],
            "lines": [
                "cap:  14 + 14 = 28 million",
                "banking reserve:  28 − 20 = 8 million",
                "drain:  14 + 8 = 22 million;  reserve 2",
                "panic:  24 − 22 = 2 million unmet",
            ],
            "after": [
                "The Act took 6 millions off the cap in the same weeks that panic added 4 millions "
                "to the demand. The figures before the panic are Marx's; the 4 millions are "
                "Gurney's estimate of the notes hoarded in 1847.",
            ],
        },
        "quiz_title": "The cap and the crisis",
        "quiz": [
            {"q": "The fixed issue is 14 millions and the Bank holds 10 millions of gold. In a "
                  "panic the public wants 26 millions of notes. How much is unmet?",
             "a": ["2 millions", "0", "12 millions", "16 millions"],
             "c": 0,
             "why": "Cap: `14 + 10 = 24`. Unmet: `26 − 24 = 2`. Twelve and sixteen are "
                    "differences against the gold or the fixed issue alone."},
            {"q": "With a cap of 28 millions and 20 millions out, 6 millions of gold are "
                  "exported. What happens to the banking department's reserve?",
             "a": ["It falls from 8 millions to 2",
                   "It is untouched, since the issue department lost the gold",
                   "It falls from 28 millions to 22",
                   "It rises, since fewer notes are out"],
             "c": 0,
             "why": "These are Marx's figures from Chapter 29: the cap falls to 22, the 20 "
                    "millions stay out, and the reserve is `22 − 20 = 2`. The drain lands on the "
                    "half of the Bank that lends."},
            {"q": "What did Hubbard's tables show, on the chapter's account?",
             "a": ["The Bank's gold moved with the rate of discount, not with prices",
                   "Prices rose whenever gold came in",
                   "The rate of discount followed the prices of the fifteen articles",
                   "Gold and prices moved together, as the Currency School said"],
             "c": 0,
             "why": "Hubbard: the fluctuations of the gold went with the rate of discount, while "
                    "prices showed &ldquo;a complete independence from the amount of the "
                    "currency&rdquo;. That is the opposite of the Currency School's claim."},
            {"q": "After the government letter of 25 October 1847, how many notes did the Bank "
                  "issue above the legal limit?",
             "a": ["None: the promise brought the hoarded notes back out",
                   "About 5 or 6 millions in a week",
                   "About one million, briefly",
                   "Enough to double the circulation"],
             "c": 0,
             "why": "Engels: in 1847 the assurance sufficed &ldquo;to bring to light the 4 to 5 "
                    "millions of hoarded notes&rdquo;. The million is 1857; the 5 or 6 millions "
                    "is Palmer's 1825, before the Act."},
        ],
        "mistakes": [
            ("Thinking that tying notes to gold steadies the circulation",
             "That was the Currency School's case: a mixed currency that behaves like gold "
             "cannot be over-issued. In the drain preset the cap falls from 28 millions to 22 "
             "with the circulation's needs unchanged, and in the panic preset 2 millions of "
             "demand are left unmet. The Act had to be suspended at the height of both crises "
             "it met."),
            ("Reading the cap as the number of notes the country needed",
             "The notes out stayed near 20 millions while the cap moved with the gold. Chapter "
             "35 notes that after 1844 the circulation reached the legal maximum only once, in "
             "November 1857."),
            ("Thinking the suspension worked by flooding the country with notes",
             "In 1847 no extra notes were issued at all; the promise brought hoards back. In "
             "1857 the excess stayed under a million and lasted days. What the suspension "
             "removed was the fear that notes could not be had."),
        ],
        "standard": (
            "Finish when you can compute the Act's cap and the demand it leaves unmet.",
            "Given the fixed issue, the gold in the Bank, the notes out and the public's demand, "
            "compute the cap, the banking department's reserve and the unmet demand, before and "
            "after a drain of gold."
        ),
        "note": (
            "The 14, 14, 20 and the drain of 6 millions are Marx's figures from Chapter 29; the 4 "
            "millions hoarded is Gurney's estimate for 1847, and the suspension preset's extra 2 "
            "millions is illustrative. The lab ignores the Act's limit on silver, the private "
            "banks' fixed issues and the coin the banking department kept for daily use."
        ),
    },
    # ---------------------------------------------------------------- 11
    # Kerr vol. 3, l. 5018 (Engels: the barometer). Inline: l. 4958 (three
    # functions), l. 4964 (1825-1857), l. 4984 (symptom), l. 4996 (feather;
    # 70 millions), l. 5004 (pivot), l. 5008 (credit shaken), l. 5135 (1847
    # exports of metal), l. 5042-5044 (Newmarch 1855), l. 5068 (tribute),
    # l. 5072 (good government), l. 5036 (loanable money-capital), l. 5052
    # (investment in England), l. 5175 (Catholic, Protestant), l. 5000 (crop
    # failures).
    {
        "slug": "precious-metal-and-the-rate-of-exchange",
        "title": "Precious Metal and the Rate of Exchange",
        "module": "Chapter 35 · Precious Metals and Rates of Exchange",
        "one_line": "Gold leaves a country when its payments abroad exceed what it is owed; the sums are small beside its production, but they come out of the reserve on which its whole credit rests.",
        "summary": (
            "Chapter 35 follows the gold reserve and the foreign exchanges. Compute the bullion a "
            "country must ship when its imports exceed its exports and other receipts, and the "
            "inflow when they do not, using Newmarch's figures for England and India in 1855, and "
            "see why a drain small beside a nation's production can still decide a crisis."
        ),
        "key": [
            "shipped = imports − exports − receipts",
            "a positive balance goes out in gold",
            "a drain falls on the Bank's reserve",
            "the reserve is the pivot of credit",
            "the crash follows the drain's end",
        ],
        "key_label": "Gold and the exchanges",
        "concepts_intro": (
            "The chapter has four sections. Marx's notes on the gold reserve come first; the "
            "second opens with a paragraph of Engels' on the exchanges, then returns to the "
            "evidence."
        ),
        "concepts": [
            ("Rate of exchange",
             "The price of one country's money in another's, set day by day by the supply of and "
             "demand for bills payable abroad."),
            ("Drain",
             "A sustained export of gold that pulls the central bank's reserve down towards its "
             "minimum."),
            ("Balance of payments",
             "Everything a country must pay abroad in a period against everything it receives: "
             "trade, interest, dividends, tribute, loans. Marx distinguishes it from the balance "
             "of trade, which need not be settled at once."),
        ],
        "read_title": "The barometer first, then what it measures",
        "read_intro": (
            "The passage is Engels', from the bracketed paragraph that opens the section on the "
            "rate of exchange. It gives the mechanism the rest takes for granted."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 35.</strong> &ldquo;The barometer for the "
                  "international movement of the money metals is the rate of exchange. If England "
                  "has more payments to make to Germany than Germany to England, the price of "
                  "marks, expressed in sterling, rises in London, and the price of sterling, "
                  "expressed in marks, falls in Hamburg and Berlin.&rdquo;"),
            ("p", "When the news says the pound has fallen, it means the price of other "
                  "currencies in pounds has risen. In Marx's day that price could rise only so "
                  "far: past a point, it was cheaper to ship gold than to buy a bill on Hamburg. "
                  "That point is where Engels' barometer turns into a drain."),
            ("p", "Read the passage as a sum. If English merchants owe more in Germany than "
                  "Germans owe in England, bills on Germany are scarce in London and their price "
                  "rises. If nothing evens the balance, the price rises until &ldquo;it will pay "
                  "to send metal (gold coin or bullion) from England to Germany in payment of "
                  "obligations, instead of sending bills of exchange&rdquo;. The gold that goes is "
                  "the balance that bills could not settle."),
            ("p", "The lab computes that balance: imports less exports less other receipts from "
                  "abroad. In the balanced preset a country imports £8 million, exports £6 "
                  "million and receives £2 million in interest and dividends: nothing to ship. In "
                  "the harvest-failure preset it must buy £1 million more of corn, and £1 million "
                  "goes out in bullion. Of drains caused by crop failures Marx says only that "
                  "they need &ldquo;no further explanation&rdquo;."),
            ("p", "Where does the gold come from? From the Bank of England's reserve, which, "
                  "Marx says, does three jobs: a fund of world money for payments abroad, a fund "
                  "for the gold circulating at home, and a fund for paying deposits and changing "
                  "notes. The first job drains the third. &ldquo;The central bank is the pivot of "
                  "the credit system. And the metal reserve in its turn is the pivot of the "
                  "bank.&rdquo;"),
            ("p", "That is why small sums matter. The drain in 1847 took the reserve down by "
                  "about six millions, and England's exports of precious metals that year came to "
                  "8,602,597 pounds. Marx calls such a sum &ldquo;a vanishing magnitude in a "
                  "production of such volume as the English&rdquo;, small even beside the 70 "
                  "millions of gold circulating at home. It tells because of when it comes: it "
                  "&ldquo;works like a feather, which, added to the weight on the scales, suffice "
                  "to incline the occillating balance definitely to one side&rdquo;. (The spelling "
                  "is the Kerr text's.)"),
            ("p", "The order of events matters too. Marx notes that the crash usually came after "
                  "the drain had stopped: &ldquo;In 1847 the drain of gold ceased in April and the "
                  "crash came in October.&rdquo; Drains are &ldquo;a symptom of a change in the "
                  "condition of foreign commerce&rdquo;, and the change is a warning of the "
                  "crisis, not its cause."),
            ("p", "Behind the arithmetic is a claim about money. While credit holds, money looks "
                  "like a book-keeping device. &ldquo;But as soon as credit is shaken—and this "
                  "phase always appears of necessity in the cycles of modern industry—all the real "
                  "wealth is to be actually and suddenly transformed into money, into gold and "
                  "silver, a crazy demand, which, however, necessarily grows out of the system "
                  "itself.&rdquo; Marx puts the same point as a joke a few pages on: "
                  "&ldquo;The monetary system is essentially Catholic, the credit system "
                  "essentially Protestant.&rdquo;"),
            ("p", "The india preset uses William Newmarch's figures for 1855. England imported "
                  "£12,670,000 of goods from India and exported £10,350,000 to it, and the East "
                  "India Company drew £3,700,000 of bills on India to meet its London expenses and "
                  "dividends. Count those drafts as receipts and the lab prints £0 to ship, with "
                  "£1,380,000 owed to England, Newmarch's own balance. (The Kerr text gives other "
                  "figures for the same year a page later, 2,250,000 and 3,250,000; they do not "
                  "agree with these.) Marx's comment is that the drafts &ldquo;resolve themselves "
                  "into a tribute levied on India&rdquo;; Newmarch said Britain exported "
                  "&ldquo;good government&rdquo; for them."),
            ("p", "The section also takes up James Wilson of the <em>Economist</em>, who held that "
                  "any export of capital moves the exchanges, whether it goes as gold or as rails "
                  "for Indian railways. Marx calls Newmarch's reply &ldquo;the correct "
                  "answer&rdquo;, and Newmarch put it plainly to the next questioner: rails "
                  "bought in England are &ldquo;an investment of English capital, in England itself, for a "
                  "certain kind of commodities to be shipped to India, and that ends the "
                  "matter&rdquo;. Gold is different because &ldquo;precious metal is directly "
                  "loanable money-capital and the basis of the entire money-system&rdquo;."),
            ("p", "The oldest view of all is the mercantilist one, that a country's gold is its "
                  "wealth and an outflow makes it poorer, and it is the misconception this lesson "
                  "tests. David Hume answered it in 1752 with the price-specie flow: gold that "
                  "leaves lowers prices at home and comes back by itself. What the chapter adds "
                  "is that the outflow is small beside production and matters through the "
                  "reserve, the rate of interest and the phase of the cycle. Since the gold "
                  "standard ended, reserves of foreign currency have taken gold's place, and how "
                  "much of the chapter carries over to them is not something it can settle."),
            ("p", "Part V ends where interest-bearing capital began, before capitalism. "
                  "“Pre-Capitalist Relationships” takes the usurer."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "world",
            "money_unit": "£",
            "preset": "balanced",
            "presets": [
                {"id": "balanced", "label": "Imports £8 million, exports £6 million, £2 million of interest and dividends",
                 "imports": 8000000, "exports": 6000000, "other_receipts": 2000000,
                 "expect": {"moDrain": "£0"}},
                {"id": "harvest-failure", "label": "The same, and £1 million more of corn bought abroad",
                 "imports": 9000000, "exports": 6000000, "other_receipts": 2000000,
                 "expect": {"moDrain": "£1,000,000 out"}},
                {"id": "india", "label": "Newmarch's England and India, 1855, with the India House drafts",
                 "imports": 12670000, "exports": 10350000, "other_receipts": 3700000,
                 "expect": {"moDrain": "£0 (£1,380,000 in)"}},
            ],
            "panel_title": "The balance a country must ship in bullion",
            "panel_intro": (
                "Imports, exports and other receipts from abroad go in, for one country over one "
                "period. The lab computes the balance: if the country owes more than it is owed, "
                "the difference goes out in bullion; if less, bullion flows in."
            ),
        }),
        "steps_title": "Computing the bullion shipped",
        "steps_intro": "Four steps for one country's payments abroad.",
        "steps": [
            ("Set imports against exports",
             "Subtract the exports from the imports: the trade balance to be paid."),
            ("Subtract the other receipts",
             "Take off interest, dividends, drafts and other sums owed to the country from "
             "abroad."),
            ("Read the sign",
             "A positive remainder is shipped in bullion; a negative one is owed to the country, "
             "and bullion flows in."),
            ("Set it against the reserve",
             "The bullion comes out of the central bank's reserve. Compare the sum with the "
             "reserve, not with the nation's production, and ask what phase of the cycle it "
             "comes in."),
        ],
        "worked": {
            "title": "A bad harvest",
            "intro": [
                "A country imports £9 million, including £1 million of extra corn after a bad "
                "harvest, exports £6 million and receives £2 million in interest and dividends. "
                "What must it ship?",
            ],
            "lines": [
                "trade balance:  9 − 6 = 3 million",
                "less receipts:  3 − 2 = 1 million",
                "shipped in gold:  1 million",
            ],
            "after": [
                "The million comes out of the central bank's reserve. Whether it matters depends, "
                "on Marx's account, on how large that reserve is and on the phase of the cycle.",
            ],
        },
        "quiz_title": "Gold, the exchanges and the reserve",
        "quiz": [
            {"q": "A country imports £15 million, exports £11 million and receives £3 million of "
                  "interest from abroad. What does it ship?",
             "a": ["£1 million in gold", "£4 million in gold", "Nothing; £1 million flows in", "£7 million in gold"],
             "c": 0,
             "why": "`15 − 11 = 4`, then `4 − 3 = 1`. Four leaves out the interest; seven adds it "
                    "the wrong way."},
            {"q": "Newmarch: in 1855 England imported £12,670,000 from India and exported "
                  "£10,350,000, and the India House drew £3,700,000 on India. Which way did the "
                  "balance run?",
             "a": ["£1,380,000 in England's favour",
                   "£2,320,000 against England",
                   "£3,700,000 in England's favour",
                   "Exactly even"],
             "c": 0,
             "why": "The trade balance is 2,320,000 against England, and the drafts more than "
                    "cover it, leaving 1,380,000 owed to England: Newmarch's figure."},
            {"q": "In 1847, when did the crash come, relative to the drain of gold?",
             "a": ["In October, months after the drain ceased in April",
                   "In April, at the height of the drain",
                   "Before the drain began",
                   "There was no drain in 1847"],
             "c": 0,
             "why": "&ldquo;In 1847 the drain of gold ceased in April and the crash came in "
                    "October.&rdquo; Marx treats the drain as a symptom and a warning, not the "
                    "cause."},
            {"q": "Why, on Marx's account, can a drain of five to eight millions matter in an "
                  "economy whose production is far larger?",
             "a": ["Because it falls on the bank reserve on which credit turns, at a critical moment",
                   "Because the country is that much poorer",
                   "Because prices fall in proportion to the gold",
                   "Because the gold was needed for wages"],
             "c": 0,
             "why": "The sum is &ldquo;a vanishing magnitude&rdquo; beside production; it tells "
                    "because the metal reserve is &ldquo;the pivot of the bank&rdquo; and the "
                    "drain comes when a little decides. The chapter cites Hubbard's tables to "
                    "show that prices do not follow the gold."},
        ],
        "mistakes": [
            ("Thinking a gold outflow means the country is getting poorer",
             "In the harvest-failure preset £1 million goes out, against goods and income worth "
             "many times that. England's metal exports in 1847 were 8.6 millions, which Marx "
             "calls &ldquo;a vanishing magnitude&rdquo; beside its production. The harm, when "
             "there is harm, comes through the Bank's reserve and the rate of interest."),
            ("Thinking the crash comes while the gold is flowing out",
             "In 1825, 1847 and 1857 the crash came after the drain had stopped. The drain is a "
             "symptom that foreign trade has turned; the crash has other causes."),
            ("Thinking every export of capital moves the exchanges",
             "Rails made in England and sent to India are paid for in England, and India owes "
             "nothing for them, so the bills on India are untouched. Gold sent out is "
             "different, because it comes out of the reserve that is loan capital itself."),
        ],
        "standard": (
            "Finish when you can compute what a country ships in bullion and say why it matters.",
            "Given imports, exports and other receipts, compute the balance shipped or received "
            "in bullion, and explain with the chapter why a sum small beside production can "
            "still decide a crisis."
        ),
        "note": (
            "The balanced and harvest-failure figures are illustrative; the india preset is "
            "Newmarch's 1855 figures as the Kerr text gives them at 1786. The lab nets one "
            "period's payments and ignores the timing Marx stresses: credit given on exports and "
            "taken on imports can turn the exchanges for months with no change in the balance."
        ),
    },
    # ---------------------------------------------------------------- 12
    # Kerr vol. 3, l. 5206 (undermines and ruins). Inline: l. 5240
    # (pawnshops), l. 5193-5195 (two forms), l. 5202 (whole surplus; Carey),
    # l. 5224 (death of a cow), l. 5226 and 5220 (means of payment), l. 5208-
    # 5210 (parasite; the indebted lord), l. 5212 (Asiatic forms), l. 5309
    # (Luther), l. 5228 (reaction against usury), l. 5250 (Child), l. 5234
    # (the borrower), l. 5236 (ruling class), l. 5281 and 5285 (banking;
    # Proudhon), l. 5232 (small farmers), l. 5293 (land loaned to
    # capitalists), l. 5197 (stage of development).
    {
        "slug": "pre-capitalist-relationships",
        "title": "Pre-Capitalist Relationships",
        "module": "Chapter 36 · Precapitalist Conditions",
        "one_line": "Before capitalism the usurer lent to lords who spent and to peasants who had to pay, and could take the whole surplus; credit as we know it began as the subordination of interest to industry.",
        "summary": (
            "Chapter 36 ends Part V with usurer's capital, the form interest-bearing capital took "
            "before capitalist production. Follow a small producer's debt year by year when the "
            "usurer's interest is more than the whole surplus, find the year it passes the value "
            "of the holding, and compare an artisan whose surplus covers the interest and a "
            "landlord who borrows to spend."
        ),
        "key": [
            "usury lends to lords and small producers",
            "interest can take the whole surplus",
            "debt grows if interest beats surplus",
            "unpaid interest itself bears interest",
            "credit: interest subordinated to industry",
        ],
        "key_label": "Usurer's capital in five lines",
        "concepts_intro": (
            "Marx calls usurer's capital and merchant's capital twins, both far older than "
            "capitalist production. The chapter asks what the older one did to the societies "
            "it lived in."
        ),
        "concepts": [
            ("Usurer's capital",
             "Interest-bearing capital in its old form, lent to borrowers who do not borrow to "
             "produce surplus value: spendthrift landowners and small producers in need."),
            ("Small production",
             "Production by peasants and artisans who own their own means of production. It is "
             "usury's natural ground, and usury undermines it."),
            ("The credit system",
             "On Marx's account, a reaction against usury that subordinates interest-bearing "
             "capital to industrial and commercial capital, without ever abolishing interest."),
        ],
        "read_title": "The two victims first, then what usury does and does not change",
        "read_intro": (
            "The passage comes after Marx has named usury's two characteristic borrowers. It "
            "says what happens to each."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 36.</strong> &ldquo;On the one hand, usury thus "
                  "exerts an undermining and destructive influence on ancient and feudal wealth "
                  "and ancient and feudal property. On the other hand it undermines and ruins "
                  "small peasants' and small burghers' production, in short all forms, in which "
                  "the producer still appears as the owner of his conditions of "
                  "production.&rdquo;"),
            ("p", "Payday lenders and pawnshops still charge rates that would ruin a business, "
                  "and their customers are people who need money to pay something now. Marx "
                  "says the same of his own day: &ldquo;the English working class pays 100% to "
                  "the pawnshops&rdquo;. This chapter is about the time when that kind of lending "
                  "was the main kind."),
            ("p", "The two borrowers in the passage are the two forms Marx calls characteristic: "
                  "&ldquo;First, usury by lending money to extravagant persons of the higher "
                  "classes, particularly to land owners; secondly, usury by lending money to the "
                  "small producer who is in possession of his own means of employment, which "
                  "includes the artisan, but more particularly the peasant&rdquo;. Neither borrows "
                  "to make a profit. The lord borrows to spend; the peasant borrows because a "
                  "payment is due or a harvest has failed."),
            ("p", "So the interest is not a share of profit, as it is under capitalism. "
                  "&ldquo;Under the form of interest the whole of the surplus over the necessary "
                  "means of subsistence&rdquo; of the producer &ldquo;may here be devoured by "
                  "usury&rdquo;. That is why Marx calls it absurd to compare the usurer's rates "
                  "with modern ones, as the American economist Henry Carey did, to show how much "
                  "workers have gained: the modern worker hands over the whole surplus too, as "
                  "profit, interest and rent together."),
            ("p", "The lab follows one debt. In the peasant preset a peasant owes £50 at 30% "
                  "and his holding yields a surplus of £10 a year beyond his family's needs. The "
                  "first year's interest is £15. He pays the £10 he has, and the other £5 is "
                  "added to the debt, which then bears interest itself: £55, £61.50, £69.95, and "
                  "in year 6 the debt passes £100, the value of his holding. Marx gives the occasion in "
                  "one line: &ldquo;The mere death of a cow may render the small producer unable "
                  "to renew his reproduction on the former scale. Then he falls into the clutches "
                  "of the usurer, and once he is in the usurer's power he never extricates "
                  "himself.&rdquo;"),
            ("p", "The artisan preset shows the line that decides it. He owes £20 at 20% with a "
                  "surplus of £10: the interest of £4 leaves him £6 to pay off the debt, which is "
                  "gone in year 3. The rate is lower, but what matters is whether the interest is "
                  "more than the surplus. Once it is, the debt can only grow. Martin Luther, whom "
                  "Marx quotes, saw it at the Leipzig fair, where lenders took 30 or 40 a year on "
                  "every hundred: &ldquo;which is the same as devouring one peasant or burgher "
                  "each year&rdquo;. The leipzig preset gives the peasant Luther's 40%, and he is "
                  "lost in year 4."),
            ("p", "Why do small producers borrow at such rates? Because they need money to pay. "
                  "&ldquo;The typical great and peculiar domain of the usurer, however, is the "
                  "function of money as a means of payment.&rdquo; Rents, tithes and taxes turned "
                  "into money payments on fixed days, and the producer who had no money that day "
                  "had to borrow it. You met this function of money in “Hoards and Means of "
                  "Payment”; here it is the usurer's opening."),
            ("p", "The lord preset is the other form: a landowner who owes £1,000 at 10% and has "
                  "£50 a year to spare. The debt grows more slowly, but it grows, and in year 12 it "
                  "passes his estate of £2,000. Marx's point is that ruin does not change how the "
                  "land is worked. Usury &ldquo;does not alter the mode of production, but "
                  "attaches itself to it as a parasite and makes it miserable&rdquo;; the indebted "
                  "lord &ldquo;becomes more oppressive, because he is himself more "
                  "oppressed&rdquo;, or the usurer takes his place. Only where the other "
                  "conditions of capitalist production were present did usury help to bring it "
                  "about; under the Asiatic forms it produced nothing but &ldquo;economic "
                  "disintegration and political rottenness&rdquo;."),
            ("p", "Then the turn. &ldquo;The development of the credit system takes place as a "
                  "reaction against usury.&rdquo; Marx warns at once against reading this as the "
                  "church fathers or Luther would: &ldquo;It signifies no more and no less than "
                  "the subordination of interest-bearing capital to the conditions and "
                  "requirements of the capitalist mode of production.&rdquo; Seventeenth-century "
                  "writers such as Josiah Child demanded a lower legal rate of interest so that "
                  "trade could flourish. What changed was the borrower: credit is now given to a "
                  "man &ldquo;in his capacity as a potential capitalist&rdquo;, expected to make "
                  "a profit out of others' labour."),
            ("p", "The chapter, and Part V, ends on the banking system's double character. By "
                  "putting all society's idle capital at the disposal of industry, it &ldquo;does "
                  "away with the private character of capital and implies in itself, to that "
                  "extent, the abolition of capital&rdquo;; and it is &ldquo;one of the most potent "
                  "instruments of crises and swindle&rdquo;. Marx expects credit to serve as a "
                  "lever in a transition to associated production, &ldquo;but only as one "
                  "element&rdquo;, and dismisses Proudhon's dream of free credit, &ldquo;a "
                  "crédit gratuit, this monster which was supposed to realise the pious wish of "
                  "small capitalist production&rdquo;."),
            ("p", "A modern answer to usury is microfinance, which since the 1970s, with "
                  "Muhammad Yunus and the Grameen Bank among its best-known names, has lent small "
                  "sums to poor producers, often women, on group guarantees, with the aim of "
                  "freeing them from moneylenders. Its supporters point to repayment rates and "
                  "businesses started; its critics to high interest and over-indebtedness. What "
                  "in the chapter bears on it is the sentence that interest-bearing capital keeps "
                  "the form of usurer's capital wherever it lends to &ldquo;producers who are not "
                  "capitalist producers, such as small farmers, craftsmen, etc.&rdquo;, and the "
                  "lab's line between interest that the surplus covers and interest that it does "
                  "not. Which side of that line a given borrower stands on is not a question the "
                  "chapter can answer."),
            ("p", "That ends Part V and this course. Marx's last remark in the chapter is that "
                  "&ldquo;land, like capital, is loaned only to capitalists&rdquo;, and land is "
                  "where Volume III goes next. Ground Rent asks how a share of surplus value "
                  "reaches the owners of the soil."),
        ],
        "lab": ("capkit", {
            "mode": "interest",
            "view": "usury",
            "money_unit": "£",
            "preset": "peasant",
            "presets": [
                {"id": "peasant", "label": "A peasant after a bad year: owes £50 at 30%, surplus £10, holding £100",
                 "debt": 50, "interest_rate": "3/10", "surplus": 10, "holding_value": 100, "years": 20,
                 "expect": {"inInterest": "£15 in year 1", "inYearsToRuin": "year 6"}},
                {"id": "artisan", "label": "An artisan: owes £20 at 20%, surplus £10, workshop £60",
                 "debt": 20, "interest_rate": "1/5", "surplus": 10, "holding_value": 60, "years": 20,
                 "expect": {"inInterest": "£4 in year 1", "inYearsToRuin": "repaid in year 3"}},
                {"id": "leipzig", "label": "The peasant at Luther's Leipzig rate of 40%",
                 "debt": 50, "interest_rate": "2/5", "surplus": 10, "holding_value": 100, "years": 20,
                 "expect": {"inInterest": "£20 in year 1", "inYearsToRuin": "year 4"}},
                {"id": "lord", "label": "A spendthrift landowner: owes £1,000 at 10%, £50 to spare, estate £2,000",
                 "debt": 1000, "interest_rate": "1/10", "surplus": 50, "holding_value": 2000, "years": 30,
                 "expect": {"inInterest": "£100 in year 1", "inYearsToRuin": "year 12"}},
            ],
            "panel_title": "A debt to the usurer, year by year",
            "panel_intro": (
                "The debt, the usurer's rate, the surplus the borrower can pay each year and the "
                "value of the holding go in. Each year the borrower pays the whole surplus; "
                "interest it does not cover is added to the debt and bears interest in turn. The "
                "lab prints the first year's interest and the year the debt passes the holding, "
                "or the year it is repaid."
            ),
        }),
        "steps_title": "Following a debt to the usurer",
        "steps_intro": "Four steps, one year at a time.",
        "steps": [
            ("Compute the year's interest",
             "Multiply the debt at the start of the year by the usurer's rate."),
            ("Pay the surplus",
             "The borrower pays everything he has beyond his subsistence. If it covers the "
             "interest, the rest reduces the debt."),
            ("Add what is unpaid",
             "If the interest is more than the surplus, the difference is added to the debt, "
             "and next year it bears interest too."),
            ("Compare with the holding",
             "Repeat until the debt is paid or passes the value of the holding. From then on the "
             "holding is, in effect, the usurer's."),
        ],
        "worked": {
            "title": "The peasant after the death of a cow",
            "intro": [
                "A peasant owes £50 at 30% and can spare £10 a year. His holding is worth £100. In "
                "which year does the debt pass it?",
            ],
            "lines": [
                "year 1:  50 · 3/10 = 15;  50 + 15 − 10 = 55",
                "year 2:  55 · 3/10 = 16.5;  debt 61.5",
                "years 3 to 5:  debt 69.95, 80.94, 95.22",
                "year 6:  debt about 113.78, past 100",
            ],
            "after": [
                "The interest was never paid in full, so every year's shortfall bore interest "
                "the next year. The usurer took the whole surplus for six years and ended with a "
                "claim larger than the holding.",
            ],
        },
        "quiz_title": "Usury and small production",
        "quiz": [
            {"q": "A peasant owes £40 at 25% and can spare £10 a year. What happens to the debt?",
             "a": ["It stays at £40 for ever: the surplus just meets the interest",
                   "It is repaid in year 4",
                   "It passes £100 in year 4",
                   "It grows by £10 a year"],
             "c": 0,
             "why": "The interest is `40 · 1/4 = 10`, exactly the surplus. Nothing is added and "
                    "nothing is repaid; the usurer takes the whole surplus every year without "
                    "end."},
            {"q": "The peasant of the worked example owes £55 at the start of year 2. What is "
                  "year 2's interest?",
             "a": ["£16.50", "£15", "£5", "£21.50"],
             "c": 0,
             "why": "`55 · 3/10 = 16.5`. Fifteen is year 1's interest on 50; five is year 1's "
                    "shortfall; 21.5 adds the shortfall to the interest."},
            {"q": "Which two borrowers does Marx call the characteristic forms of usury before "
                  "capitalist production?",
             "a": ["Extravagant landowners and small producers who own their means of production",
                   "Merchants and manufacturers",
                   "The state and the church",
                   "Wage workers and pawnbrokers"],
             "c": 0,
             "why": "&ldquo;First, usury by lending money to extravagant persons of the higher "
                    "classes, particularly to land owners; secondly, usury by lending money to the "
                    "small producer&rdquo;. Merchants borrow to make a profit, as capitalists do."},
            {"q": "On the chapter's account, what distinguishes interest-bearing capital under "
                  "capitalism from usurer's capital?",
             "a": ["The changed conditions and the changed character of the borrower",
                   "A lower rate of interest, fixed by law",
                   "The nature of the capital lent",
                   "The church's approval of interest"],
             "c": 0,
             "why": "It is &ldquo;in no way the nature or the character of this capital itself. It "
                    "is merely the altered conditions, under which it operates, and consequently "
                    "the totally changed character of the borrower&rdquo;."},
        ],
        "mistakes": [
            ("Thinking usury is just high interest on loans for production",
             "Usury's characteristic borrowers do not borrow to produce a profit: the lord "
             "borrows to spend, the peasant to pay. In the peasant preset the interest of £15 is "
             "more than the whole surplus of £10, which &ldquo;may here be devoured by "
             "usury&rdquo;. Modern interest is &ldquo;normally no more than a part of the "
             "surplus-value&rdquo;."),
            ("Comparing the usurer's rates with modern ones to show the worker's gain",
             "That was Carey's comparison, and Marx calls it absurd: the usurer took the whole "
             "surplus of an owner-producer, while the modern worker yields the whole surplus "
             "value as profit, interest and rent."),
            ("Thinking usury by itself brings in capitalist production",
             "Usury ruins lords and peasants, but whether that leads to capitalism &ldquo;depends "
             "entirely upon the stage of historical development and the circumstances "
             "surrounding it&rdquo;. Under the Asiatic forms it led to nothing new."),
        ],
        "standard": (
            "Finish when you can follow a debt to the usurer year by year.",
            "Given a debt, the usurer's rate, the yearly surplus and the value of the holding, "
            "compute each year's interest and debt, say whether the debt is repaid or passes "
            "the holding, and in which year."
        ),
        "note": (
            "All the debts, surpluses and holdings are illustrative; Chapter 36 gives none. The "
            "40% is Luther's figure for the Leipzig fair. The lab assumes the borrower pays the "
            "whole surplus every year and borrows nothing more, which is kinder than the "
            "chapter's account of what usurers did."
        ),
    },
]
