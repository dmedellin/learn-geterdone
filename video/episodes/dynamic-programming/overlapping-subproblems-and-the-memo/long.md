---
format: long
lesson: dynamic-programming/overlapping-subproblems-and-the-memo
title: Overlapping subproblems: why a memo turns 22,089 calls into 50
thumb: Same questions, asked once
---

@chapter The question
@title text="Overlapping Subproblems and the Memo" sub="Dynamic Programming and Optimal Substructure" art=thumb
The fewest coins recurrence is correct. But run it exactly as written on an amount of eighteen, and it makes twenty two thousand and eighty nine calls. Add a memo, and it makes fifty. Where does all that waste come from?

@art repeated-subtrees
It comes from asking the same questions over and over. F of eighteen asks for f of seventeen, f of sixteen and f of thirteen. Then f of seventeen asks for f of sixteen again. The recursion tree has thousands of nodes, but only eighteen distinct arguments.

@words text="Overlapping subproblems" sub="few distinct arguments, many calls"
That's overlapping subproblems. The set of distinct arguments is much smaller than the number of calls. Optimal substructure says the recurrence is right. Overlapping subproblems says evaluating it naively is wasteful, by an amount you can count.

@chapter Three routes
@list heading="Coins 1, 2, 5  ·  amount 18" items="No memo:  22 089 calls@memo free|Memo:  50 calls, 18 stored@with a memo|Table:  76 cells, 106 reads@The table"
The memo free recursion answers five, after twenty two thousand and eighty nine calls. The same recursion with a memo answers five after fifty calls, and stores eighteen subproblems. The table answers five after filling seventy six cells, with a hundred and six reads, and no recursion at all.

@art memo-lookup
A memo writes each answer down the first time. Every later request for the same argument becomes a lookup. It turns the tree back into the graph it always was.

@chapter Where fifty comes from
@math heading="Counting memo calls" items="amount 1: 1 coin fits@amount one;;amounts 2 to 4: 2 coins fit, three times@two to four;;amounts 5 to 18: 3 coins fit, fourteen times@five to eighteen;;1 + (1 + 6 + 42) = 50@one plus"
Fifty is worth deriving. Each computed amount makes one sub call per coin that fits. At amount one, only one coin fits. At two to four, two coins fit, three times over. At five to eighteen, three fit, fourteen times. That's forty nine edges. One plus forty nine is fifty.

@art dependency-graph
So fifty isn't a property of memoisation as a technique. It's the size of the dependency graph, the distinct amounts and the arrows between them.

@chapter Two kinds of state
@art coin-table
The memo stores eighteen entries. The table fills seventy six cells. They count different things. The memo keys on the remaining amount alone. The table's cell is a pair, the coins allowed so far and the amount, because each row makes one more coin available. Four rows by nineteen columns is seventy six.

@words text="Same function, different state" sub="memo = table's last row = f(a)"
Both compute the same function. By induction on the amount, both are right at zero, and if both are right below a, they take the minimum over the same options at a. The difference is state, not answer. Choosing the state is the design decision this course keeps returning to.

@chapter What the ratio says
@math heading="One instance" items="22089 / 50 = 441.8@over fifty;;table: Θ(nk)@Theta of n k;;no memo: exponential in k@grows exponentially"
The panel prints twenty two thousand and eighty nine over fifty, about four hundred and forty one point eight. That's a measurement on one amount. The proved statements are different. The table is Theta of n k for n coins and amount k. The memo free recursion grows exponentially in k.

@art crossing
And at small sizes they cross. With coins one, three and four, and an amount of six, the memo free recursion made twenty four calls, against the table's twenty eight cells. Neither bound changed. The input just sat on the other side of the crossing.

@chapter Where people slip
@list heading="Common slips" items="Calling the memo an optimisation and stopping there@The first|Keying the memo on too little state@The second|Reading one ratio as a property of memoisation@The third"
The first slip is calling the memo an optimisation and stopping there. Estimate what it will save first. The second is keying the memo on too little state. Add a rule like at most two of each coin, and the code returns answers to a different question. The third is reading one ratio as a property of memoisation.

@art merge-sort-tree
And remember the case where a memo saves nothing at all. Merge sort's halves are all distinct, so a cache on it stores entries that nobody ever reads.

@chapter Try it
@words text="coins 1, 2, 5 · amount 8" sub="count the memo's calls"
Your turn. With coins one, two and five and an amount of eight, count the edges leaving each amount from one to eight, and predict the memo's call count before you run it.

@end text="Count the calls yourself"
You can count the calls with and without a memo, and plot them, on Learn. That's learn dot get er done dot I O.
