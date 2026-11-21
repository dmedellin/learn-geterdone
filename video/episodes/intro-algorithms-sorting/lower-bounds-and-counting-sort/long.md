---
format: long
lesson: intro-algorithms-sorting/lower-bounds-and-counting-sort
title: Why comparison sorts can't beat n log n, and how counting sort does
thumb: Stop comparing, start counting
---

@chapter What every sort so far shares
@title text="The Sorting Lower Bound and Counting Sort" sub="Introduction to Algorithms, Sections 8.1 and 8.2" art=thumb
Insertion sort, merge sort, heapsort and quicksort all share one property. Chapter eight proves that property sets a hard limit, and then sorts in linear time by breaking it.

@quote text="the sorted order they determine is based only on comparisons between the input elements." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 8"
The property is that the sorted order they determine is based only on comparisons between the input elements. The authors call them comparison sorts.

@chapter The decision tree
@art decision-tree
Any comparison sort on n keys can be drawn as a decision tree. The root is the first comparison. The answer sends the run left or right, to the next comparison. And each leaf records the ordering the sort has worked out. One run of the sort is one path from root to leaf.

@art leaf-count
A correct sort must be able to produce every one of the n factorial orderings, because each one is the right answer for some input. So every ordering needs a reachable leaf. And the longest path is the number of comparisons on the worst input.

@math heading="Theorem 8.1" items="2ʰ ≥ n!@two to the h;;h ≥ lg(n!)@h is at least;;= Ω(n lg n)@omega of n log n"
A binary tree of height h has at most two to the h leaves. It needs at least n factorial, so two to the h is at least n factorial. Then h is at least log of n factorial, which by Stirling's approximation is omega of n log n.

@words text="Merge sort and heapsort are optimal" sub="⌈lg n!⌉: 3, 5, 7 … 22 for ten keys"
So merge sort and heapsort are asymptotically optimal comparison sorts. And for a given n, the exact bound is the ceiling of log n factorial. That's three comparisons for three keys, five for four, seven for five, and twenty two for ten.

@words text="A bound on the worst input" sub="sorted input: insertion sort uses n − 1"
Careful though. The bound is about the worst input, the tree's longest path. Some leaves are shallow. Insertion sort uses only n minus one comparisons on sorted input. What no comparison sort can do is be fast on every input.

@chapter Counting sort
@art tally-bins
Counting sort escapes the bound by never comparing keys. It assumes each key is an integer from zero to k. First, it counts how many keys equal each value.

@art prefix-sums
Then it adds the counts up from the left. Now each count says how many keys are at most that value, which is the last output position a key of that value may take.

@art place-from-back
Finally, it walks the input from the last key to the first. Each key goes to the position its counter names, and the counter drops by one, so the next equal key lands one place to the left.

@math heading="Counting sort's cost" items="tally + place: Θ(n)@tally;;clear + sum C: Θ(k)@clearing;;total Θ(n + k)@n plus k"
The tally and the placement each take theta of n. Clearing and summing the counts take theta of k. So counting sort is theta of n plus k, which is linear when k is O of n. The lower bound doesn't apply, because it uses keys as indexes.

@chapter Stable, from the back
@art unstable-front
Walking from the back is what makes it stable. The last equal key is placed rightmost, and each earlier one just to its left, so equal keys keep their input order. That matters for satellite data, and above all for radix sort, next lesson.

@math heading="3, 0, 5, 2, 3, 5, 1, 0, 3, 4" items="work 16  vs  bound 22@sixteen;;place from the front: 5 pairs reversed@from the front;;16-bit range: work 65,546@sixteen bit"
On three, zero, five, two, three, five, one, zero, three, four, the lab's work is sixteen, against twenty two comparisons for any comparison sort's worst case. Place from the front instead, and five pairs of equal keys come out reversed. Declare a sixteen bit range, and the work jumps to sixty five thousand five hundred and forty six.

@chapter Common slips
@list heading="Common slips" items="Taking Ω(n lg n) as a bound on all sorting@The first|Reading it as a bound on every input@The second|Calling counting sort linear without asking about k@the third"
The first slip is taking omega of n log n as a bound on all sorting. It's only for comparison sorts. The second is reading it as a statement about every input. And the third is calling counting sort linear without asking about k.

@chapter Try it
@words text="[2, 4, 1, 2, 0, 4, 2, 1],  k = 4" sub="tally, prefix sums, positions"
Your turn. Sort two, four, one, two, zero, four, two, one by counting sort, with k equal to four. Write the tally, the prefix sums, and the position each key takes from the back. Then check that the three twos keep their order.

@end text="Count, then break stability"
You can count keys yourself, and break stability by placing them the wrong way, on Learn. That's learn dot get er done dot I O.
