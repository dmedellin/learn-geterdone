---
format: long
lesson: algorithms-and-complexity/divide-and-conquer
title: The master theorem, and where faster algorithms come from
thumb: Fewer pieces, not faster gluing
---

@chapter Split, solve, combine
@title text="Divide and Conquer" sub="Algorithms and Complexity" art=thumb
Merge sort, binary search, fast multiplication. They all work the same way, and one theorem tells you what each of them costs.

@art split-combine
A divide and conquer algorithm splits an input of size n into a subproblems, each of size n over b. It solves each one recursively, and spends f of n dividing and combining.

@math heading="The recurrence" items="T(n) = a·T(n/b) + f(n)@T of n equals"
So the running time satisfies T of n equals a times T of n over b, plus f of n. Every algorithm in this lesson has that shape.

@chapter The master theorem
@math heading="T(n) = a·T(n/b) + Θ(nᵈ)" items="log_b a < d  ⟹  Θ(nᵈ)@less than d;;log_b a = d  ⟹  Θ(nᵈ log n)@equals d;;log_b a > d  ⟹  Θ(n^(log_b a))@greater than d"
With combining cost Theta of n to the d, compare log base b of a with d. If it's less than d, T is Theta of n to the d. If it equals d, it's n to the d, times log n. If it's greater than d, it's n to the power log base b of a.

@art recursion-levels
Where do the three cases come from? Level i of the recursion has a to the i subproblems, each of size n over b to the i. Together they do n to the d times a over b to the d, to the power i, units of work.

@art three-trees
That's a geometric series with ratio a over b to the d. If the ratio is below one, the root dominates. If it's exactly one, every level is equal. If it's above one, the leaves dominate. And the ratio is below, equal to, or above one exactly when log base b of a is below, equal to, or above d.

@list heading="Examples" items="Binary search: a=1, b=2, d=0 → Θ(log n)@Binary search|Merge sort: a=2, b=2, d=1 → Θ(n log n)@Merge sort|Karatsuba: a=3, b=2, d=1 → Θ(n^1.585)@Karatsuba|Strassen: a=7, b=2, d=2 → Θ(n^2.807)@Strassen"
Binary search has one subproblem of half size and constant work, so it's Theta of log n. Merge sort has two halves and linear merging, so it's n log n. Karatsuba has three halves and linear work, n to the one point five eight five. And Strassen has seven, with quadratic work, n to the two point eight zero seven.

@chapter Karatsuba
@art four-to-three
To multiply two n digit numbers, split each in half. The obvious way needs four half size products. That's T of n equals four T of n over two, plus n, which is Theta of n squared. No better than schoolbook multiplication.

@math heading="(a·10ᵐ + b)(c·10ᵐ + d)" items="= ac·10²ᵐ + (ad + bc)·10ᵐ + bd@a c times;;ad + bc = (a + b)(c + d) − ac − bd@the middle;;3 products:  ac,  bd,  (a + b)(c + d)@three products"
Written out, it's a c times ten to the two m, plus a d plus b c times ten to the m, plus b d. But the middle part equals a plus b times c plus d, minus a c, minus b d. So three products are enough: a c, b d, and a plus b times c plus d.

@words text="log₂ 3 ≈ 1.585 < 2"
And log two of three is about one point five eight five, which is less than two. The exponent dropped.

@chapter Reducing a
@art matrix-blocks
Strassen does the same for matrices, seven half size products instead of eight, giving n to the two point eight zero seven. In both cases the gain came from reducing a. No amount of faster combining could have done it, because d only matters when it's bigger than log base b of a.

@chapter Uneven splits
@art lopsided-split
Quicksort splits around a pivot, so the split depends on the data. A perfect pivot gives two T of n over two plus n, which is n log n. The worst pivot gives T of n minus one, plus n, which is n squared. The master theorem doesn't apply there, because there's no fixed b.

@words text="T(n) = T(n/10) + T(9n/10) + n" sub="still Θ(n log n)"
Remarkably, even a lopsided but constant split is fine. T of n over ten plus T of nine n over ten, plus n, is still n log n, because the recursion still has logarithmic depth.

@chapter Where people slip
@list heading="Common slips" items="Swapping a and b@The first|Optimising the combining step in case three@The second|Applying the theorem to an uneven split@The third"
The first slip is swapping a and b. a counts the subproblems and b is how much each one shrinks. The second is optimising the combining step when the leaves dominate. The third is applying the theorem to an uneven split, which needs unrolling or a recursion tree.

@chapter Try it
@words text="T(n) = 4T(n/2) + n" sub="a = ?  b = ?  d = ?"
Try the naive multiplication recurrence. T of n equals four T of n over two, plus n. Read off a, b and d, compare log base b of a with d, and check you get Theta of n squared.

@end text="Reduce a, change the exponent"
The full lesson on divide and conquer is on Learn. That's learn dot get er done dot I O.
