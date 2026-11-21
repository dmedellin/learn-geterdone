---
format: long
lesson: sorting-and-selection/k-way-merge-and-external-sorting
title: k-way merging: more comparisons, far fewer passes
thumb: Count passes, not comparisons
---

@chapter The question
@title text="k-Way Merging and Sorting in Practice" sub="Sorting and Selection" art=thumb
You have eight sorted runs to merge. Put their heads in a heap, and you'll make more comparisons than merging them two at a time. So why does every disk sort use the heap? Because on disk, comparisons aren't what you pay for.

@chapter The heap merge
@art run-heads
Put the first item of each of the k runs into a min heap, tagged with its run. Repeatedly pull the smallest, write it out, and push the next item from the same run. Every item goes in once and comes out once.

@words text="heap size k, not n" sub="each extract: sift-down of depth ⌊log₂ k⌋"
The heap only ever holds k items, so the extra memory is the fan in, not the data. Each extract is a sift down through log k levels, so the order is n log k. But the constant is worth measuring, not assuming.

@chapter Eight runs of eight
@math heading="64 items, 8 runs" items="one heap:  302 comparisons,  1 pass@one heap;;two at a time:  180 comparisons,  7 passes@two at a time"
Sixty four items. Through one heap: three hundred and two comparisons, and one pass over the data. Merging two at a time: a hundred and eighty comparisons, but seven passes, because each of the k minus one rounds rereads the whole merged prefix. Both give the same output, and the lab checks they agree.

@math heading="Why the heap loses comparisons" items="n log₂ k = 192@a hundred and ninety two;;2n log₂ k = 384@twice that;;measured:  302@spends three hundred and two"
So in comparisons, the heap loses. n log two k is a hundred and ninety two, and the heap spends three hundred and two, between that and twice that. The extra is the comparison between the two children at every level of a sift down. Heapsort paid exactly the same factor.

@art pass-sweep
What the heap buys is passes. It turns k runs into one, in a single sweep. And when the data lives on disk, a pass over the data is the cost.

@chapter Sorting on disk
@art disk-blocks
On disk, data moves in blocks, and reading everything once is a pass. So count passes.

@art memory-runs
Say N records don't fit in M of memory. First, run formation: read M records at a time, sort them, write them back as a run. That's N over M runs. Then merge them, F at a time, where the fan in F is M over B, since each open run needs one block of size B.

@math heading="passes = 1 + ⌈log_F(N/M)⌉" items="N = 10⁹, M = 10⁶, B = 4:  F = 250 000 → 2 passes@a million in memory;;M = 10³, B = 4:  F = 250 → 4 passes@a thousand;;M = 10³, B = 500:  F = 2 → 21 passes@blocks of five hundred"
The number of passes is one, plus the ceiling of log base F of the number of runs. A billion records with a million in memory, blocks of four: fan in two hundred and fifty thousand, two passes. With a thousand in memory: fan in two fifty, four passes. And with blocks of five hundred: fan in two, twenty one passes.

@art fan-in
Same data, same algorithm, and passes went from four to twenty one, because the fan in, the base of the logarithm, fell from two fifty to two. A pass over a billion records is the expensive thing, and comparisons don't appear in the formula at all.

@chapter The cutoff
@art cutoff-curve
Real library sorts add one more idea. Merging tiny runs is wasteful, so insertion sort blocks below a cutoff, then merge. On sixty four shuffled keys, the lab measures five ninety four comparisons at a cutoff of one, five hundred at four, four forty eight at eleven, and five twenty seven at twenty.

@words text="cheapest cutoff: 11, on one array" sub="the shape is Timsort's"
The cheapest cutoff is strictly inside the range. That's a crossover. Eleven is a measurement on one array, not a constant of nature. What generalises is the shape: form runs, insertion sort below a cutoff, merge. That's Timsort's shape, the sort in several standard libraries.

@chapter Three kinds of number
@list heading="On this page" items="302 and 180: measured comparisons@measured|1 + ⌈log_F(N/M)⌉: computed passes@computed|11: the low point of a sampled curve@low point"
Three figures here are three different kinds of number. Three oh two and a hundred and eighty are measured comparisons. The pass formula is arithmetic, a count of passes computed rather than measured. And eleven is the low point of a curve sampled at twenty cutoffs, on one array.

@chapter Where people slip
@list heading="Common slips" items="Expecting the heap to make fewer comparisons@The first|Quoting n log k as a count@The second|Treating the pass formula as comparisons@And the third"
The first slip is expecting the heap merge to make fewer comparisons. It makes more. The second is quoting n log k as a count, when the constant is about two. And the third is treating the pass formula as a comparison count. The cost model changed, and the algorithm that loses under the old unit wins under the new.

@chapter Try it
@words text="N = 10⁹, M = 10⁴, B = 100" sub="fan-in, runs, passes"
Your turn. Work out the fan in, the number of runs, and the passes for a billion records, ten thousand in memory, and blocks of a hundred. Then say what happens to the passes if the block size doubles.

@end text="Count the passes"
You can merge runs both ways and price a disk sort by its passes, on Learn. That's learn dot get er done dot I O.
