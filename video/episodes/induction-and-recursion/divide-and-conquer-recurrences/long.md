---
format: long
lesson: induction-and-recursion/divide-and-conquer-recurrences
title: The master theorem: solving divide-and-conquer recurrences
thumb: One comparison decides it
---

@chapter One shape of recurrence
@title text="Divide-and-Conquer Recurrences" sub="Induction and Recursion" art=thumb
A divide and conquer algorithm splits a problem of size n into a pieces, each of size n over b. It solves each piece recursively, then spends f of n combining the results.

@math heading="The running time" items="T(n) = aT(n/b) + f(n)@T of n"
So its running time satisfies one shape of recurrence: T of n equals a times T of n over b, plus f of n. When f is a power of n, one comparison settles it.

@chapter The recursion tree
@art recursion-tree
Picture the calls as a tree. At the top, one problem of size n. One level down, a problems of size n over b. Then a squared problems of size n over b squared, and so on, down to size one after log base b of n levels.

@math items="level i:  aⁱ · (n/bⁱ)ᵈ = nᵈ · (a/bᵈ)ⁱ@level i;;ratio a/bᵈ vs 1  ⟺  log_b a vs d@ratio"
Let f of n be n to the d. Then the work at level i is n to the d, times a over b to the d, to the power i. That's a geometric series with ratio a over b to the d. And comparing that ratio with one is the same as comparing log base b of a with d.

@chapter The master theorem
@words text="Θ(g(n))" sub="between two constant multiples of g(n), for large n"
One piece of notation. T of n is theta of g of n when it's trapped between two positive constant multiples of g of n, for all large enough n. It names a growth rate and throws away the constants.

@list heading="T(n) = aT(n/b) + Θ(nᵈ)" items="log_b a < d:  Θ(nᵈ)@less than d|log_b a = d:  Θ(nᵈ log n)@equals d|log_b a > d:  Θ(n^(log_b a))@greater than d"
Here's the theorem. If log base b of a is less than d, T is theta of n to the d. If it equals d, you get n to the d, times log n. And if it's greater than d, T is theta of n to the log base b of a.

@art three-shapes
Read those through the tree. In case one the work shrinks down the levels, so the root dominates. In case two every level does the same work. In case three the work grows, so the leaves dominate. Some texts number the cases the other way round, so name a case by what dominates.

@chapter Merge sort and binary search
@math items="merge sort:  2T(n/2) + n,   log₂2 = 1 = d  →  Θ(n log n)@Merge sort"
Merge sort is two T of n over two, plus n. Log base two of two is one, which equals d. So it's the balanced case: n log n.

@art level-bars
Every level merges n items in total, and there are log n levels. Binary search, T of n over two plus one, is balanced too: log base two of one is zero, which equals d, so it's theta of log n.

@chapter Karatsuba
@art four-vs-three
Multiplying two n digit numbers by splitting them in halves naively takes four half size products: four T of n over two, plus n. Log base two of four is two, more than one, so that's n squared, no better than schoolbook.

@words text="3T(n/2) + n  →  Θ(n^1.585)" sub="log₂3 ≈ 1.585"
Karatsuba's identity does it with three products. Log base two of three is about one point five eight five, so you get n to the one point five eight five. One fewer multiplication changes the exponent.

@chapter Three recurrences
@math items="2T(n/2) + n:   1 = 1  →  case 2,  Θ(n log n)@The first;;8T(n/2) + n²:   3 > 2  →  case 3,  Θ(n³)@The second;;2T(n/2) + n²:   1 < 2  →  case 1,  Θ(n²)@The third"
The first, two T of n over two plus n, is merge sort: case two. The second, eight T of n over two plus n squared, has log base two of eight, three, more than two: case three, n cubed. The third, two T of n over two plus n squared, has one less than two: case one, n squared.

@art leaf-heavy
That second one is naive matrix multiplication, and the recursion is doing the damage: the n cubed comes from the leaves, not the combining.

@art block-grids
Strassen attacks exactly that, with seven products instead of eight. Log base two of seven is about two point eight zero seven, so the cost drops to n to the two point eight zero seven.

@chapter Where people slip
@list heading="Common slips" items="Mixing up a and b@Mixing up|Forcing a non-polynomial f into it@non polynomial|Reading Θ as real running time@running time"
Three slips. Mixing up a and b. In two T of n over three plus n, a is two and b is three. Forcing a non polynomial f, like n log n, into this version. And reading theta as real running time. A better exponent with a worse constant can be slower on every input you'll ever run.

@end text="The three cases, tabulated"
On Learn, you can compare log base b of a with d for a table of recurrences and read off each case. That's learn dot get er done dot I O.
