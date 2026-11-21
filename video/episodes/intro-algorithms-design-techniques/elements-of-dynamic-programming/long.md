---
format: long
lesson: intro-algorithms-design-techniques/elements-of-dynamic-programming
title: The two ingredients of dynamic programming
thumb: Substructure plus overlap
---

@chapter A clue, not a guarantee
@title text="Elements of Dynamic Programming" sub="Introduction to Algorithms, Section 15.3" art=thumb
Two examples in, section fifteen point three steps back and asks: when does dynamic programming actually apply?

@quote text="Whenever a problem exhibits optimal substructure, we have a good clue that dynamic programming might apply." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 15.3"
The authors choose their words carefully. Whenever a problem exhibits optimal substructure, we have a good clue that dynamic programming might apply. A clue, and might.

@chapter Optimal substructure
@art cut-paste
Here's the pattern for finding it. Show that a solution makes a choice, like a first piece or a split, that leaves subproblems. Suppose you're handed an optimal solution's choice. Then prove that its parts must be optimal for their subproblems. If one weren't, cut it out, paste in a better one, and you'd beat the optimum.

@art subproblem-space
Keep the space of subproblems as simple as you can. For rod cutting, one length was enough. For the matrix chain, a split leaves a suffix that doesn't start at one, so both ends must vary.

@math heading="Running time, roughly" items="subproblems × choices each@times the choices;;rod cutting: Θ(n) × n@rod cutting;;matrix chain: Θ(n²) × (n − 1)@matrix chain"
Informally, the running time is the number of subproblems times the choices for each. Rod cutting has theta of n subproblems with n choices. The matrix chain has theta of n squared, with n minus one choices.

@chapter A problem that fails
@art shortest-split
Shortest paths have optimal substructure. If a shortest path from u to v passes through w, its two parts are shortest paths too. Otherwise you could swap in a shorter one. The longest simple path, with the most arcs and no repeated vertex, looks just as decomposable. It isn't.

@math heading="Arcs: u→v u→w v→w w→x x→u x→v" items="longest u to v: u → w → x → v@three arcs;;longest u to w: u → v → w@longest from u to w;;longest w to v: w → x → u → v@longest from w to v;;spliced: u → v → w → x → u → v  ✗@splice"
In this small graph, the longest simple path from u to v is u, w, x, v, three arcs. But the longest from u to w is u, v, w. And the longest from w to v is w, x, u, v. Splice those two together, and the path repeats u and v. It isn't even simple.

@art path-clash
The subproblems aren't independent. The longest path to w spends the vertex v, which the second part must end at. For shortest paths, the two parts can never share a vertex. The longest simple path has no known efficient dynamic program. It's NP complete.

@chapter Overlapping subproblems
@art recursion-repeats
The second ingredient is overlap. A plain recursion on the matrix chain, with no table, takes at least two to the n minus one time, even though there are only theta of n squared distinct subproblems. It keeps meeting the same ones. Divide and conquer, by contrast, usually makes new subproblems every level.

@art memo-table
Two practical points. Store the choice as well as the value, so rebuilding the answer is a lookup. And memoize when you prefer the recursion's shape. If every subproblem must be solved, bottom up usually wins by a constant. If some are never needed, memoization skips them.

@chapter Counting the memo
@math heading="Coins 1 4 6, amount 20" items="fewest: 6 + 6 + 4 + 4, four coins@four coins;;largest first: 6 + 6 + 6 + 1 + 1, five@largest coin first;;plain 3,053 calls  vs  memo 53@three thousand"
The lab makes change with the fewest coins. With coins one, four and six, and an amount of twenty, the best is six, six, four, four, four coins. Taking the largest coin first gives five, a hint of why greedy needs proofs. The plain recursion makes three thousand and fifty three calls. The memoized one makes fifty three.

@words text="Amount 24: 14,085 vs 65" sub="the memo holds amounts 1 to 20"
The memo holds only twenty subproblems, the amounts one to twenty. Raise the amount to twenty four, and the plain count jumps to fourteen thousand and eighty five, while the memoized one adds twelve calls, to sixty five.

@chapter Common slips
@list heading="Common slips" items="Assuming substructure because it looks decomposable@The first|Confusing independent with non-overlapping@The second|Believing memoization is slower than a table@the third"
The first slip is assuming optimal substructure because a problem looks decomposable. The second is confusing independent with non overlapping. They describe different things. And the third is believing memoization makes a recursion slower than a table. Asymptotically, it's the same.

@chapter Try it
@words text="add the arc w→u" sub="longest simple path from u to v?"
Your turn. Add the arc w to u to the graph. Find the longest simple path from u to v now, check whether its two parts at w are longest for their own endpoints, and say whether the new arc repaired optimal substructure, or only changed the instance.

@end text="Count plain and memoized"
You can count a plain and a memoized recursion side by side, on Learn. That's learn dot get er done dot I O.
