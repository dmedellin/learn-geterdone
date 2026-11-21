---
format: long
lesson: algorithms-and-complexity/complexity-classes
title: P vs NP, explained without the jargon
thumb: Easy to check, hard to find?
---

@chapter Solving and checking
@title text="P, NP and NP-Completeness" sub="Algorithms and Complexity" art=thumb
Some problems are quick to solve. Others seem slow to solve, but if someone hands you an answer, you can check it quickly. Whether those two groups are really the same is the biggest open question in computer science.

@words text="P: solvable in polynomial time" sub="time O(nᵏ) for some constant k"
P is the class of decision problems that an algorithm can solve in time big O of n to the k, for some constant k, where n is the size of the input. Informally, efficiently solvable.

@art solve-vs-check
NP is the class of decision problems where a proposed solution can be verified in polynomial time. If someone hands you an answer, you can check it quickly.

@words text="NP ≠ “not polynomial”" sub="nondeterministic polynomial"
The name trips everyone up. NP stands for nondeterministic polynomial, from an older definition with a machine that guesses. It does not mean not polynomial. The verification definition is equivalent, and far easier to think with.

@chapter P sits inside NP
@art nested-circles
Every problem in P is also in NP. If you can solve it quickly, you can check a claimed answer by solving it yourself and comparing. So P is a subset of NP. Whether the reverse is true is the open question.

@list heading="In P? · In NP?" items="Is n prime?  yes · yes@prime|Shortest path:  yes · yes@shortest path|Satisfiable formula?  unknown · yes@satisfiable|Hamilton circuit?  unknown · yes@Hamilton circuit|Does this program halt?  no · no@halt"
Is n prime? That's in P, and so in NP. Shortest path, the same. Is this formula satisfiable? In NP, and nobody knows whether it's in P. Does a Hamilton circuit exist? Also unknown, but in NP. And does this program halt? Neither. It's undecidable.

@chapter Reductions
@art reduction-funnel
Problem A reduces to problem B if every instance of A can be turned into an instance of B, in polynomial time, with the same answer. Then a fast algorithm for B gives one for A. So B is at least as hard as A.

@art many-to-one
A problem is NP complete if it's in NP, and every problem in NP reduces to it. It's NP hard if that second part holds, whether or not it's in NP itself. These are the hardest problems in NP.

@words text="Cook-Levin, 1971" sub="SAT is NP-complete"
The first one ever found was SAT, deciding whether a propositional formula can be satisfied. That's the Cook Levin theorem, from nineteen seventy one. Every NP completeness proof since then reduces from a problem already known to be complete.

@chapter All or nothing
@list heading="Some NP-complete problems" items="Hamilton circuit@Hamilton circuit|3-colouring@three colouring|Subset sum@subset sum|0/1 knapsack@knapsack|Clique@clique"
Thousands are now known, including Hamilton circuit, three colouring, subset sum, the travelling salesman decision problem, zero one knapsack, and clique.

@art dominoes
And they stand or fall together. A polynomial time algorithm for any one of them would give one for all of them, and so P would equal NP. Fifty years of effort has produced neither that algorithm nor a proof that none exists.

@chapter What it means in practice
@art three-doors
The classification tells you what to do. In P, look for a good polynomial algorithm, and expect to find one. NP complete, stop looking for a fast exact algorithm. Try approximation with proved ratios, heuristics, restricted inputs, or solvers that are fast in practice. Undecidable, stop entirely.

@words text="Millions of variables" sub="industrial SAT solvers"
And NP complete is a worst case statement. It doesn't mean your instances are hard. Industrial SAT solvers routinely handle formulas with millions of variables, because real instances have structure. Most researchers expect P is not NP. Nobody has proved it, and it's one of the Clay Millennium Problems.

@chapter Where people slip
@list heading="Common slips" items="Reading NP as “not polynomial”@The first|Treating NP-complete as unsolvable@The second|Confusing NP-complete with undecidable@The third"
The first slip is reading NP as not polynomial. The second is treating NP complete as unsolvable. It's a worst case statement, and real instances are often solved fine. And the third is confusing NP complete with undecidable. NP complete problems have algorithms that are slow. Undecidable problems have no algorithm at all.

@chapter Try it
@words text="Hamilton circuit" sub="what would you check?"
Try this. Someone hands you a graph and a proposed Hamilton circuit. List exactly what you'd check to confirm it, and convince yourself each check is quick. That's what it means for the problem to be in NP.

@end text="Quick to check isn't quick to solve"
The full lesson on P, NP and NP completeness is on Learn. That's learn dot get er done dot I O.
