---
format: long
lesson: intro-algorithms-sorting/quicksort
title: Quicksort and partitioning, step by step
thumb: One pivot, two sides
---

@chapter A paradox
@title text="Quicksort and Partitioning" sub="Introduction to Algorithms, Sections 7.1 and 7.2" art=thumb
Quicksort's worst case is theta of n squared, no better than insertion sort. And yet the book recommends it.

@quote text="quicksort is often the best practical choice for sorting because it is remarkably efficient on the average" cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 7"
In the authors' words, quicksort is often the best practical choice for sorting because it is remarkably efficient on the average. Its expected time is n log n with small constants, and it sorts in place.

@chapter Work moved to the divide
@words text="Merge sort combines. Quicksort divides." sub="nothing left to combine"
Quicksort is divide and conquer, with the work moved. Merge sort divides trivially and does its work combining. Quicksort does its work dividing, and has nothing left to combine.

@art pivot-regions
Partition picks a pivot, and rearranges the subarray so that everything left of the pivot is at most the pivot, and everything right of it is greater. The pivot is now in its final place. Then quicksort sorts the two sides recursively.

@chapter Partition
@art partition-step
The book's partition takes the last element as the pivot, x. An index i marks the end of the small region. A second index, j, walks from left to right, comparing each key with x once. If the key is greater, j just moves on, and the greater region grows. If it's at most x, i advances, and A of i and A of j swap.

@list heading="Four regions" items="p..i: at most x@at most x|i+1..j−1: greater than x@greater than x|j..r−1: not yet examined@not yet examined|r: the pivot x@the pivot itself"
That's the loop invariant. Before each iteration, the subarray is in four regions. Keys known to be at most x, keys known to be greater than x, keys not yet examined, and the pivot itself in the last position. At the end, one last swap puts the pivot between the two regions.

@math heading="21, 7, 30, 12, 4, 26, 15, 9, 33, 18" items="pivot 18: 9 comparisons, 6 exchanges@pivot eighteen;;7, 12, 4, 15, 9  |  18  |  21, 30, 33, 26@seven, twelve"
On twenty one, seven, thirty, twelve, four, twenty six, fifteen, nine, thirty three, eighteen, with pivot eighteen, partition makes nine comparisons and six exchanges. Eighteen ends at position six, with seven, twelve, four, fifteen, nine before it, and twenty one, thirty, thirty three, twenty six after.

@words text="Partition doesn't sort the sides" sub="7, 12, 4, 15, 9 is not in order"
Notice the left side isn't sorted. Partition guarantees one thing: the pivot is in its final place. Sorting the sides is the recursion's job. And n keys always cost exactly n minus one comparisons.

@chapter What the splits cost
@art worst-split
In the worst case, every partition puts n minus one keys on one side and none on the other. The recurrence is T of n equals T of n minus one plus theta of n, which sums to theta of n squared.

@art sorted-input-trap
And when does that happen? When the input is already sorted, the very case where insertion sort is fastest. Sorted data is common in practice. Seven sorted keys cost twenty one comparisons, the most any arrangement can.

@art even-split
In the best case, every split is as even as possible. That's T of n equals two T of n over two plus theta of n, and the master theorem gives theta of n log n.

@chapter The surprise in between
@art lopsided-split
Now suppose every split is nine to one, which looks terrible. Every level of the tree still costs at most c n. And the deepest path, the one that keeps the nine tenths side, ends after log base ten ninths of n levels. That's still theta of log n.

@math items="depth = log₁₀/₉ n = Θ(lg n)@log base ten ninths;;total = O(n lg n)@O of n log n"
So the depth is log base ten ninths of n, which is theta of log n, and the total is O of n log n. Any split of constant proportion gives the same. Only the constant changes.

@words text="Bad then good ≈ one good split" sub="random input absorbs bad splits"
On random input, good and bad splits mix. A bad split followed by a good one costs theta of n, and leaves pieces no worse than one good split would. The bad split is absorbed.

@chapter Common slips
@list heading="Common slips" items="Thinking partition sorts the sides@The first|Treating the worst case as rare@The second|Believing only an even split gives n lg n@the third"
The first slip is thinking partition sorts the two sides. The second is treating the worst case as a rare accident, when sorted input triggers it. And the third is believing only an even split gives n log n.

@chapter Try it
@words text="[14, 3, 27, 8, 19, 5, 11]" sub="pivot 11"
Your turn. Partition fourteen, three, twenty seven, eight, nineteen, five, eleven, with pivot eleven. Write the array after each comparison, mark the four regions, and say where the pivot ends.

@end text="Step through a partition"
You can step through partition with the invariant checked after every comparison, on Learn. That's learn dot get er done dot I O.
