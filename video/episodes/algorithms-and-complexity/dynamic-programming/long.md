---
format: long
lesson: algorithms-and-complexity/dynamic-programming
title: Dynamic programming: solve each subproblem once
thumb: Never solve it twice
---

@chapter The waste
@title text="Dynamic Programming" sub="Algorithms and Complexity" art=thumb
Some recursive algorithms are slow for a silly reason. They solve the same small problem again and again. Dynamic programming fixes that by solving each subproblem once, and remembering the answer.

@art fib-tree
The classic case is Fibonacci. The naive recursion makes about one point six to the n calls, because it keeps recomputing the same values. F of five calls F of three twice, and F of two three times. And it only gets worse.

@list heading="Calls to compute F(n)" items="n = 10:  177 naive · 10 memoised@At ten|n = 30:  2 692 537 naive · 30 memoised@At thirty|n = 50:  about 40 000 000 000 naive · 50 memoised@at fifty"
At ten, the naive version makes a hundred and seventy seven calls. At thirty, it's over two point six million. And at fifty, about forty billion. Store each value the first time you compute it, and the count drops to n: ten, thirty, fifty.

@chapter Two conditions
@list heading="Dynamic programming needs" items="Optimal substructure@Optimal substructure|Overlapping subproblems@Overlapping subproblems"
It works when a problem has two properties. Optimal substructure: an optimal solution is built from optimal solutions to subproblems. Overlapping subproblems: the recursion visits the same subproblems many times.

@words text="Merge sort: no overlap" sub="caching would never hit"
You need both. Merge sort has optimal substructure but no overlap, so it's plain divide and conquer, and caching would never help. And without optimal substructure you can't combine sub solutions at all.

@chapter Coin change
@math heading="Fewest coins" items="best[0] = 0@best of zero;;best[v] = 1 + min{ best[v − c] : c ≤ v }@best of v"
Remember coin change with one, three and four, where greedy failed at six? Best of zero is zero. And best of v is one, plus the smallest best of v minus c, over every coin c that fits.

@art coin-table
That recurrence is the optimal substructure written down. The best way to make v uses some coin c, and the rest has to be the best way to make v minus c. So fill the table from small amounts upward.

@math heading="Coins {1, 3, 4}, target 6" items="best[1..5] = 1, 2, 1, 1, 2@one, two;;best[6] = 1 + min(best[5], best[3], best[2])@best of six;;= 1 + 1 = 2  →  3 + 3@one plus one"
Best of one up to five are one, two, one, one and two. Then best of six is one plus the smallest of best of five, best of three and best of two. That's one plus one, which is two. The two coins are three and three, the answer greedy missed. Filling the table costs Theta of v times the number of coins.

@chapter Longest common subsequence
@math heading="L[i][j]" items="0  if i = 0 or j = 0@zero if;;L[i−1][j−1] + 1  if X[i] = Y[j]@if the characters match;;max(L[i−1][j], L[i][j−1])  otherwise@Otherwise"
Here's another. L of i, j is the length of the longest common subsequence of the first i characters of X and the first j of Y. It's zero if either is empty. If the characters match, it's one more than the diagonal entry. Otherwise, it's the larger of the entry above and the entry to the left.

@art lcs-grid
That costs Theta of m times n, against exponential for the naive recursion. It's the algorithm behind diff, behind version control merges, and behind sequence alignment in biology.

@chapter Where it doesn't apply
@art path-graph
Now a warning. The longest path with no repeated vertex has no optimal substructure. The longest path from a to c needn't be the longest from a to b, then from b to c, because those two may share vertices. The problem is NP hard.

@words text="Shortest path ✓   Longest simple path ✗"
The shortest path is different. Any piece of a shortest path is itself shortest, and Dijkstra solves it in polynomial time. Two problems one word apart, on opposite sides of tractability.

@chapter Top down or bottom up
@art memo-table
You can write it two ways. Top down is recursion plus a cache, and computes only the subproblems you need. Bottom up fills a table in dependency order, with no recursion overhead. The asymptotic cost is the same.

@art two-rows
Bottom up often lets you throw old rows away. The Fibonacci table only needs its last two entries. That's why it's preferred when memory matters.

@chapter Where people slip
@list heading="Common slips" items="Not checking optimal substructure@The first|Memoising divide and conquer@The second|Defining the subproblem loosely@The third"
The first slip is not checking optimal substructure, so the recurrence gets written and is wrong. The second is memoising a divide and conquer algorithm like merge sort, where the cache never hits. The third is defining the subproblem loosely. The best solution so far isn't a subproblem. It has to be a function of explicit parameters.

@chapter Try it
@words text="Fill the table by hand" sub="L[i][j] for two short words"
Try it. Pick two short words of your own and fill in the longest common subsequence table, row by row. At each cell, ask one question: do the characters match? Then read the length off the bottom right corner.

@end text="Solve it once, then look it up"
The full lesson on dynamic programming is on Learn. That's learn dot get er done dot I O.
