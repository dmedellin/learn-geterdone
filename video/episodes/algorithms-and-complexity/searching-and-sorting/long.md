---
format: long
lesson: algorithms-and-complexity/searching-and-sorting
title: Why no comparison sort can beat n log n
thumb: The limit nobody can beat
---

@chapter Searching
@title text="Searching and Sorting" sub="Algorithms and Complexity" art=thumb
Searching and sorting are the most studied problems in computing. This one ends with something unusual: a proof that no comparison sort, however clever, can ever beat n log n.

@words text="Linear search: Θ(n)" sub="works on any array"
Start with searching. Linear search checks each element in turn. In the worst case that's Theta of n, and it works on any array at all.

@chapter Binary search
@art halving-range
Binary search is much faster, but it needs a sorted array. It compares with the middle, then throws away the half that can't contain the target. Each comparison at least halves the range, so on n elements it needs at most the floor of log two of n, plus one comparisons. That's Theta of log n.

@art unsorted-trap
That sorted requirement is what licenses throwing half away. Run binary search on unsorted data and it still stops, but it returns confident wrong answers. That's the most dangerous kind of failure.

@words text="Sort once: Θ(n log n)" sub="pays off after about log n searches"
And sorting first costs Theta of n log n. So binary search only pays for itself across many searches on the same data, roughly once the number of searches is more than log n.

@chapter Four sorts
@list heading="Sorting" items="Bubble: Θ(n²) always@Bubble sort|Selection: Θ(n²) always@Selection sort|Insertion: Θ(n²) worst, Θ(n) best@Insertion sort|Merge: Θ(n log n) always@merge sort"
Now sorting. Bubble sort swaps adjacent pairs and repeats, Theta of n squared, always. Selection sort finds the minimum and places it, also n squared, always. Insertion sort inserts each element into a sorted prefix: n squared at worst, but n at best. And merge sort is n log n, always.

@art insertion-slide
Insertion sort is the interesting quadratic one. Its inner loop stops as soon as it finds a smaller element, so on nearly sorted data it does almost no work. That's why real implementations switch to it below a certain size.

@art merge-zip
Merge sort splits the list, sorts each half, and merges them. Its cost satisfies T of n equals two T of n over two, plus n, which is Theta of n log n. It doesn't depend on the data at all. Its one drawback is that it needs Theta of n extra space.

@chapter The lower bound
@art decision-tree
So can anyone do better than n log n? Picture any comparison sort as a decision tree. Each internal node is one comparison, with two outcomes. Each leaf is one possible final ordering. The height of the tree is the worst case number of comparisons.

@math heading="Height h of the tree" items="leaves ≥ n!@n factorial;;leaves ≤ 2ʰ@two to the h;;so  h ≥ log₂(n!)@log two of n factorial"
To sort correctly, the tree needs at least n factorial leaves, one for every ordering of the input. A binary tree of height h has at most two to the h leaves. So the height is at least log two of n factorial.

@math heading="Bounding log₂(n!)" items="the largest n/2 factors are each ≥ n/2@the largest;;n! ≥ (n/2)^(n/2)@so n factorial;;log₂(n!) ≥ (n/2) log₂(n/2) = Ω(n log n)@Omega of n log n"
Now bound n factorial from below. The largest n over two factors are each at least n over two, so n factorial is at least n over two, to the power n over two. Take logs, and you get at least n over two times log two of n over two. That's Omega of n log n.

@words text="Every comparison sort: Ω(n log n)" sub="merge sort is optimal"
That's a genuine impossibility result, a statement about the problem, not a failure of ingenuity. No comparison sort will ever beat n log n, which means merge sort already achieves the optimum.

@chapter Outside the theorem
@art counting-buckets
But counting sort and radix sort run in Theta of n, under assumptions about the range of the keys. They don't contradict the theorem. They never compare elements, so they fall outside its hypothesis.

@chapter Where people slip
@list heading="Common slips" items="Binary searching unsorted data@The first|Applying the lower bound to all sorting@The second|Ignoring adaptivity@The third"
The first slip is binary searching unsorted data. The second is believing the lower bound applies to all sorting, when it only covers comparison sorts. And the third is ignoring adaptivity. On partially ordered input, insertion sort being linear can be worth more than a better asymptotic class.

@chapter Try it
@words text="Sort three items" sub="how many leaves? how tall at least?"
Here's a small one to try. Draw a decision tree that sorts three elements. How many leaves does it need? And what's the least height it could have?

@end text="n log n is a floor, not a target"
The full lesson on searching and sorting is on Learn. That's learn dot get er done dot I O.
