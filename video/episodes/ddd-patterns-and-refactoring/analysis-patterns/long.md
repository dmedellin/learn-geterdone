---
format: long
lesson: ddd-patterns-and-refactoring/analysis-patterns
title: Analysis Patterns: start from a model someone already worked out
thumb: A lead, not a recipe
---

@chapter A familiar shape
@title text="Applying Analysis Patterns" sub="Domain-Driven Design, Chapter 11" art=thumb
Where does a deep model come from? Usually, Evans says, it's earned slowly, by learning, talking and trying. But now and then you meet a problem whose shape is familiar, something solved once before, and you can start from what was learned then.

@art pattern-starting-point
Some of those solutions have been written down. Martin Fowler's book Analysis Patterns, from nineteen ninety seven, calls them groups of concepts for a construction common in business modelling. Each uses a few objects to stand for one concept. They save trial and error, but they're where refactoring starts, not a finished part to install.

@quote text="Analysis patterns are not technological solutions; they are guides to help you work out a model in a particular domain." cite="Evans, Domain-Driven Design, Chapter 11"
Analysis patterns are not technological solutions; they are guides to help you work out a model in a particular domain.

@words text="Not analysis apart from design"
Evans also corrects the name. Analysis suggests modelling done apart from building, yet Fowler's patterns discuss implementation at length, code included. That experience is the most valuable thing a pattern carries. Take the model ideas without it, and you reopen the split that Model Driven Design exists to close.

@chapter Accounts and entries
@art ledger-entries
Fowler's basic model is two objects. An Account holds value. Every change to that value is an Entry, positive to add and negative to take away. Entries are kept, never edited, so the account's whole history stays.

@code block=1 lines=1-19 focus="8-10@posts an entry|12-18@balance"
In code, the account posts an entry by adding it to its list, and nothing removes or edits one. Its balance is what all its entries add up to. Whether that's added on demand or cached is hidden behind the interface.

@chapter Money only moves
@code block=2 lines=1-15 focus="6-9@adds up the entries|10-12@not zero"
The second model adds conservation. Money only moves from one account to another. So a Transaction groups entries that add up to zero. This one adds up the entries, and if the net is not zero, it refuses.

@art balance-scale
Every credit is matched by a debit. Evans, following Fowler, adds a condition: this holds only in a closed system, and many simple applications don't need the rigour.

@chapter What the team kept
@art drop-transaction
In the book's interest example, two developers sketch accounts, entries and a transaction tying each charge to its payment. The domain expert says no. Charges and payments are separate postings, days apart, and the balance is what matters. So they drop Transaction, keep accounts and entries, and learn a word from the expert: accrual.

@words text="A calculated compromise"
Coding refines it again. A fee entry and an interest entry, alike in the model, become separate classes, because the project's tables and mapping framework required it. Evans calls that a calculated compromise, to be made and moved past.

@chapter A box office week
@art ticket-till
Now the lab, on a theatre box office's week. A sale for cash, a gift voucher sold, a voucher redeemed for tickets, and a refund. A debit is positive and a credit is negative.

@math heading="week-balanced" items="cash 146.00@cash;;ticket-sales −126.00@ticket sales;;vouchers −20.00@vouchers;;total 0.00 · no unbalanced transactions@nets to zero"
Three accounts, four transactions. The balances are cash one hundred and forty six, ticket sales minus one hundred and twenty six, and vouchers minus twenty. Every transaction nets to zero, so the total is zero.

@math heading="week-two-slips" items="t3: 30.00 − 3.00 = +27.00@typed as three;;t4: −24.00, nothing to match it@cash side only;;total: +27.00 − 24.00 = +3.00@only three"
Now two mistakes. In t3, the credit side is typed as three instead of thirty, so it's off by plus twenty seven. And t4's refund is recorded on the cash side only, minus twenty four. Yet the total of all entries is only three, because the two errors partly cancel.

@art offsetting-errors
That's what the Transaction model buys. A check on each movement, where a grand total hides errors that offset. It's a reason to look at t3 and t4, nothing more. Whether a system needs that check is the question the book's own team answered no to.

@chapter Where people slip
@list heading="Common slips" items="Installing a pattern whole@The first|Double entry for everything@The second|Analysis without design@And the third"
The first slip is installing an analysis pattern whole, as a finished component. The second is assuming every money like system needs double entry. It needs a closed system. And the third is reading the word analysis as analysis without design.

@chapter Try it
@code block=3 lines=1-8 focus="1-2@b one|3-4@b two|5-6@b three|7-8@b four"
Your turn: the theatre bar's evening, as transaction, account and amount. Transactions b one, b two, b three and b four. By hand, give each account's balance and the total of all entries. Then name every transaction that doesn't add up to zero, with its net, and say what the slip probably was.

@end text="Check each movement"
Type the records into the lab to check, on Learn. That's learn dot get er done dot I O.
