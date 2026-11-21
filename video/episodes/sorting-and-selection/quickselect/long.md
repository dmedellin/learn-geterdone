---
format: long
lesson: sorting-and-selection/quickselect
title: Quickselect: find the median without sorting
thumb: One side, never both
---

@chapter The question
@title text="Quickselect" sub="Sorting and Selection" art=thumb
You want the median of a list. The obvious move is to sort it and look in the middle. That's n log n work for a question that only needs linear time. Here's how.

@chapter Order statistics
@words text="k-th order statistic = k-th smallest" sub="median: the ⌈n/2⌉-th"
The k th order statistic is the k th smallest value. The first is the minimum, the n th is the maximum, and the median is the ceiling of n over two. Finding one is called selection.

@art discard-side
Quickselect partitions, then looks at where the pivot landed. If its rank is the one you want, you're done. If not, the answer is on one known side, and the other side is thrown away, unexamined.

@list heading="Quickselect" items="r = k:  return the pivot@r equals k|k < r:  recurse left, same k@less than r|k > r:  recurse right, for k − r@Otherwise"
Let r be the pivot's rank in the range. If r equals k, return the pivot. If k is less than r, recurse on the left with the same k. Otherwise, recurse on the right, looking for k minus r.

@chapter One term, not two
@math heading="The recurrences" items="quicksort:  T(n) = T(k) + T(n − k − 1) + (n − 1)@Quicksort's recurrence;;quickselect:  T(n) = T(one side) + (n − 1)@Quickselect's has one"
Quicksort's recurrence has two recursive terms, because both sides still need sorting. Quickselect's has one. That single change is the whole difference.

@art one-vs-two
Quicksort's calls branch into a tree, with about n work on every level and log n levels. Quickselect's calls form a single chain that keeps shrinking. Sum a chain like that, and you get a geometric series.

@math heading="Two extremes" items="median pivot:  n + n/2 + n/4 + … < 2n@exactly the median;;worst pivot:  n(n − 1)/2@worst"
If every pivot were exactly the median, the work would be n plus n over two plus n over four, and so on, which is under two n. If every pivot were the worst, it would be n times n minus one, over two, just as for quicksort.

@chapter Why random is linear
@art middle-half
So pick the pivot at random. Call a pivot good if its rank lies in the middle half. A random pivot is good with probability at least one half. And a good pivot leaves at most three quarters of the range.

@math heading="Expected comparisons" items="≤ 2 calls per size class@two calls;;2n(1 + 3/4 + 9/16 + …) = 8n@eight n;;sharper:  < 4n@four n"
So you expect at most two calls before the range shrinks to three quarters. Each costs under n. Adding up the size classes gives two n times one plus three quarters plus nine sixteenths and so on, which is eight n. Already linear. Solving the recurrence properly sharpens it to under four n, for every input and every k.

@chapter Twenty four keys
@math heading="12th smallest of 24, seed 5" items="1–24 → 12–24 → one element@shrinks;;35 comparisons@thirty five;;sort then index:  83@against merge sort's"
A seeded shuffle of one to twenty four, looking for the twelfth smallest. Three partitions find it, as the range shrinks from one to twenty four, to twelve to twenty four, to a single element. Thirty five comparisons, against merge sort's eighty three for sorting and indexing.

@art shrinking-ranges
Each partition threw away a side and never looked at it again. Twenty four elements, then thirteen, then one. That's the chain, shrinking.

@art seed-scatter
Change the seed, and the count moves. A hundred and eight at seed one, fifty seven at seed two, eighty six at seed three. Over two hundred seeds, the mean is fifty nine point six, ranging from twenty three to a hundred and eighteen.

@words text="4n = 96 bounds the mean, not each run"
So seed one, at a hundred and eight, is above the four n line of ninety six. That's allowed. The bound is on the expectation, not on each run. Take a single count as the bound and you'll see it broken.

@chapter A fixed rule fails again
@art sorted-trap
Use the first element as the pivot, and ask for the median of an already sorted array of twenty four. The pivot is the smallest every time, so each call discards one element. Two hundred and ten comparisons, against fifty two for merge sort. Same reason as quicksort.

@chapter Where people slip
@list heading="Common slips" items="Sorting to get one value@The first|Reading expected linear as per-run@The second|Forgetting to shift k when going right@And the third"
The first slip is sorting to get one value. A median, a percentile or a top k threshold don't need the whole order. The second is reading expected linear as a promise about each run. And the third is forgetting to shift k when recursing right, which returns a plausible wrong answer.

@chapter Try it
@words text="Find the 5th smallest of 9 values" sub="partition by hand, discard a side each time"
Your turn. Write down nine numbers and find the fifth smallest by partitioning by hand. At each step, say which side you discard and what k becomes.

@end text="Select without sorting"
You can run quickselect on seeded arrays and watch the counts scatter around four n, on Learn. That's learn dot get er done dot I O.
