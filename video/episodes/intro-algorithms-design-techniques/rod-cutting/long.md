---
format: long
lesson: intro-algorithms-design-techniques/rod-cutting
title: Rod cutting: dynamic programming from 2 to the n down to n squared
thumb: Solve each length once
---

@chapter The method in a sentence
@title text="Rod Cutting and Dynamic Programming" sub="Introduction to Algorithms, Section 15.1" art=thumb
Chapter fifteen opens with one sentence that is the whole method.

@quote text="A dynamic-programming algorithm solves each subsubproblem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time it solves each subsubproblem." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 15"
A dynamic programming algorithm solves each subsubproblem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time it solves each subsubproblem. And programming here means a tabular method, not writing code.

@words text="Overlapping subproblems" sub="divide-and-conquer splits into disjoint pieces"
Like divide and conquer, it combines solutions to subproblems. The difference is that here the subproblems overlap. They share smaller subproblems, and the table makes sure none is solved twice.

@chapter The rod-cutting problem
@art rod-pieces
You have a rod n inches long, and a price for a piece of each whole inch length. Cut it into pieces to earn the most. Cuts are free, and selling it whole is allowed.

@art cut-fan
How many ways are there? At each of the n minus one inch marks, you cut or you don't. So there are two to the n minus one cuttings, and trying them all is hopeless.

@art first-piece
The trick is to see every cutting as a first piece from the left, sold as it is, plus a remainder, which may be cut further. The best revenue is the best first piece plus the best revenue for what's left.

@math heading="The recurrence" items="rₙ = max over 1 ≤ i ≤ n of (pᵢ + rₙ₋ᵢ)@r n is the largest;;r₀ = 0@r nought"
So r n is the largest of p i plus r n minus i, over every first piece i, with r nought equal to zero. The best solution is built from the best solution to a smaller rod. That's optimal substructure.

@chapter The plain recursion
@art recursion-explosion
Compute that recurrence directly, and something goes badly wrong. A call on length j calls every shorter length. The recursion makes two to the n calls in all. At forty inches it runs for minutes, likely more than an hour, and each extra inch roughly doubles the time.

@words text="2ⁿ calls · n + 1 subproblems" sub="the lengths 0 to n"
Yet there are only n plus one distinct subproblems, the lengths zero to n. So trade memory for time. Solve each length once, store it, and look it up.

@chapter Memoized and bottom-up
@art table-fill
There are two ways. Memoized cut rod keeps the recursion, but checks a table of answers first and records each new one. Bottom up cut rod fills the table in order of length, so every answer it needs is already there. Both do one plus two up to n steps, n times n plus one over two, which is theta of n squared.

@art subproblem-graph
The subproblem graph shows why. One vertex for each length, and an arc from each length to every shorter one. Bottom up visits the vertices in reverse topological order. Memoized is a depth first search.

@chapter Recovering the cuts
@math heading="Prices 1 4 8 9 14 15 19 21" items="r: 1 4 8 9 14 16 19 22@r runs one;;s: 1 2 3 1 5 3 7 3@the first piece;;cut 8: s(8) = 3, then s(5) = 5 → 8 + 14 = 22@twenty two"
Store beside each answer the first piece that achieved it. For these eight prices, r runs one, four, eight, nine, fourteen, sixteen, nineteen, twenty two. And s, the first piece, is one, two, three, one, five, three, seven, three. For eight inches, cut three, then the remainder's entry says five. Eight plus fourteen is twenty two.

@words text="j = 6: 3 + 3 earns 16 > 15" sub="j = 7: whole rod at 19 wins"
Look at six. Two three inch pieces earn sixteen, against fifteen for the whole rod. And at seven, the whole rod at nineteen beats every split.

@math heading="Calls counted" items="8 inches: 256 vs 37@two hundred and fifty six;;20 inches: 1,048,576 vs 211@twenty inch"
On eight inches, the plain recursion makes two hundred and fifty six calls, the memoized version thirty seven. On a twenty inch price list, it's over a million calls against two hundred and eleven. The revenue is the same by every route.

@chapter Common slips
@list heading="Common slips" items="Thinking the table changes the recurrence@The first|Counting calls when you mean subproblems@The second|Reading s(n) as the whole answer@the third"
The first slip is thinking the table changes the recurrence. It only changes how often each piece is solved. The second is counting calls when you mean subproblems. And the third is reading s of n as the whole answer. It's only the first piece.

@chapter Try it
@words text="add p(9) = 24" sub="find r(9) from the table"
Your turn. Add a price of twenty four for a nine inch piece. Compute r of nine by hand from the table, list every first piece that achieves it, and say which cutting the lab will print.

@end text="Count the three routes"
You can count the plain, memoized and bottom up routes on your own prices, on Learn. That's learn dot get er done dot I O.
