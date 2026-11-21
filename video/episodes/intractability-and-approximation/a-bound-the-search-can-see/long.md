---
format: long
lesson: intractability-and-approximation/a-bound-the-search-can-see
title: Branch and bound on knapsack: same answer, fewer nodes
thumb: 14 nodes, not 44
---

@chapter Solve it exactly, visit less
@title text="A Bound the Search Can See" sub="Intractability and Approximation" art=thumb
The first honest response to a hard problem is to solve it exactly anyway, and try to visit less of the search tree. Branch and bound does that, and it never changes the answer.

@art search-tree
Search over partial solutions. At each node, compute an upper bound on the best value any completion could still reach. If that bound doesn't beat the best complete answer found so far, abandon the node. The bound must never underestimate, or the search could throw away the optimum.

@chapter The fractional bound
@art fractional-fill
For knapsack, here's the bound. At a node, some items are decided, with value v taken and capacity c left. Now let the remaining items be taken fractionally. Greed solves that exactly: take items in decreasing value per unit weight, and split the one that doesn't fit.

@words text="bound = v + fractional optimum of what remains"
Why is that a bound? Any real completion picks a subset of the remaining items that fits. Taking each in full is also a fractional solution, so it can't beat the fractional optimum. Allowing fractions can only help.

@chapter Five items
@math heading="Capacity 10" items="items 3:5, 4:6, 5:8, 2:3, 6:9@three five;;optimum 16:  3:5 + 5:8 + 2:3,  weight 10@value sixteen;;exhaustive over 32 subsets:  16@thirty two subsets"
The instance is five items, written weight then value: three five, four six, five eight, two three, and six nine, with capacity ten. The answer is value sixteen, taking three five, five eight and two three, which fills the sack exactly. An exhaustive search over thirty two subsets agrees.

@math heading="The searches" items="with the bound:  14 nodes,  4 branches cut@fourteen nodes;;without:  44 nodes,  0 cut@forty four"
With the bound, the search opens fourteen nodes and cuts four branches. Without it, forty four nodes. Same answer, sixteen, both times.

@art nodes-vs-subsets
Wait, forty four nodes, but only thirty two subsets? Thirty two counts the leaves, the complete subsets. Nodes include every partial decision on the way down, so the unbounded search can open more nodes than there are subsets.

@chapter A tight root bound
@words text="root bound = 16 = the optimum"
At the root, the fractional bound is sixteen, exactly the true optimum. That's a coincidence of these numbers, and it's the best case. The bound knows the answer before the search starts, and still has to prove it, by exploring until every alternative is cut.

@art heavy-prize
Now run the same code on other instances. With one heavy prize that fills the sack, the root bound is thirty, taking the prize gives thirty, and everything else is cut at once.

@list heading="Same code, three instances" items="Five items:  14 vs 44, 4 cut@Five items|One heavy prize:  3 vs 135@One heavy prize|Equal densities:  30 vs 86, 2 cut@equal density"
Five items: fourteen against forty four. One heavy prize, nine thirty, with six copies of one two: three nodes against a hundred and thirty five. Every item at equal density: thirty against eighty six, with only two cut, even though the root bound is again exactly the optimum.

@art equal-density
The ratio moves from about three, to forty five, to under three. And the branches cut move from four to two to two, tracking neither.

@art pruning-depends
Three instances, one algorithm, and node counts of fourteen, three and thirty. A tight bound at the root doesn't mean heavy pruning. Pruning compares the bound with the best answer found so far, and early in the search that's a poor answer.

@chapter What's not established
@words text="nothing about the worst case"
Branch and bound on knapsack is still exponential in the worst case. There are instances where nothing is cut. The node counts tell you what the bound bought on this instance, and that's the only kind of fact a counter can produce. It's the strategy that gives up least: the answer is exact, at a cost you can watch.

@chapter Where people slip
@list heading="Common slips" items="Trusting a bound that isn't proved@The first|Reading a trace row as a cut@The second|Turning node counts into a claim@And the third"
The first slip is trusting a quantity that only usually exceeds the completions. If any completion beats it, the search returns a confident wrong answer. The second is reading a trace row as a pruned branch. The search prunes against the running best, so trust its own counter. And the third is turning fourteen against forty four into a claim about the algorithm.

@end text="Same answer, fewer nodes"
Run the search with the bound on and off, on Learn. That's learn dot get er done dot I O.
