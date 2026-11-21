---
format: long
lesson: intro-algorithms-sorting/medians-and-order-statistics
title: Finding the median in linear time, without sorting
thumb: Keep one side
---

@chapter Better than sorting
@title text="Medians and Order Statistics" sub="Introduction to Algorithms, Chapter 9" art=thumb
To find the median, you could sort and then look in the middle. That costs n log n. Chapter nine does better.

@quote text="The ith order statistic of a set of n elements is the ith smallest element." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 9"
It starts with a definition. The ith order statistic of a set of n elements is the ith smallest element. The minimum is the first, the maximum is the nth, and the median is halfway.

@chapter Minimum and maximum
@art tournament
Finding the minimum takes n minus one comparisons, and nothing can do better. Think of a tournament. Every key except the winner has to lose at least once, and each comparison has only one loser.

@art pairs-minmax
Minimum and maximum separately would take two n minus two. But do them together. Take the keys in pairs, and compare each pair with each other. Then test only the smaller against the minimum so far, and only the larger against the maximum.

@math items="3 comparisons per 2 keys@three comparisons;;at most 3⌊n/2⌋  vs  2n − 2@at most three times"
That's three comparisons for every two keys, at most three times the floor of n over two in all.

@chapter Randomized select
@art keep-one-side
Randomized select is randomized quicksort with one recursive call removed. Partition around a random pivot, and look at the pivot's rank, k. If i equals k, that's the answer. Otherwise, recurse into the one side that holds it.

@words text="Quicksort: both sides. Select: one side." sub="levels shrink geometrically"
Why is that linear, when quicksort is n log n? Quicksort recurses into both sides, so every level costs about n. Select keeps one side, so the levels shrink. A pivot from the middle half, which happens half the time, leaves at most three quarters of the keys. And a falling geometric series is a constant times its first term.

@math heading="Median of 21 keys, seed 9" items="ranges 21, 15, 12, 9, 8, 4, 3, 1@twenty one to fifteen;;20 + 14 + 11 + 8 + 7 + 3 + 2 = 65@m minus one;;merge sort first: 70@seventy"
In the lab, the median of twenty one keys takes eight steps. The ranges shrink from twenty one to fifteen, twelve, nine, eight, four, three and one. Each partition of m keys costs m minus one, so that's sixty five comparisons. Sorting first with merge sort takes seventy.

@art scattered-runs
But the expectation is an average over pivots. Move the seed and the count moves, from thirty three at seed eight to seventy seven at seeds seven and ten. And with the last element as pivot on sorted input, it's a hundred and sixty five, the quadratic worst case.

@chapter Worst-case linear select
@art groups-of-five
Section nine point three removes the luck. Split the keys into groups of five. Find each group's median by insertion sort. Then recursively find the median x of those medians, partition around x, and recurse into one side.

@art guarantee-block
x isn't the true median, but it can't be far off. At least half the group medians are at least x, and each of their groups gives three keys greater than x. So at least three n over ten minus six keys are greater than x, and as many are less.

@math heading="SELECT's recurrence" items="T(n) ≤ T(⌈n/5⌉) + T(7n/10 + 6) + O(n)@two calls;;1/5 + 7/10 = 9/10 < 1@one fifth plus seven tenths;;cn + (9/10)cn + (81/100)cn + … ≈ 10·cn@about ten c n"
That gives a recurrence with two calls, on a fifth of the keys and on at most seven tenths plus six. One fifth plus seven tenths is nine tenths, less than one. So each level costs about nine tenths of the one above, and the whole tree totals about ten c n. Linear.

@words text="No contradiction with Ω(n lg n)" sub="selection compares, but doesn't sort"
That doesn't contradict chapter eight. Select compares keys, but it doesn't sort them, and the lower bound is about producing the whole order.

@chapter Common slips
@list heading="Common slips" items="Believing a median needs a sort@The first|Assuming min and max cost 2n − 2@The second|Expecting every run to beat sorting@the third"
The first slip is believing a median needs a sort, and so n log n. The second is assuming minimum and maximum together cost two n minus two. And the third is expecting every run of an expected linear algorithm to beat sorting.

@chapter Try it
@words text="17, 4, 29, 11, 2, 23, 8, 30, 15" sub="then: groups of five at n = 60"
Your turn. Use the pairing method on seventeen, four, twenty nine, eleven, two, twenty three, eight, thirty, fifteen, counting comparisons. Then at n equals sixty, work out how many keys must be greater than the median of medians.

@end text="Select without sorting"
You can find a median and set it beside the cost of sorting first, on Learn. That's learn dot get er done dot I O.
