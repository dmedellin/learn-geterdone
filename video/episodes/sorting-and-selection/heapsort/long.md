---
format: long
lesson: sorting-and-selection/heapsort
title: Heapsort: n log n on every input, and the two promises it breaks
thumb: In place, no bad input
---

@chapter The question
@title text="Heapsort" sub="Sorting and Selection" art=thumb
What if you need a sort that never goes quadratic, and you can't spare a second array? Heapsort gives you both. Here's how it works, and the two things it quietly gives up.

@chapter Two phases
@art max-heap
First, build a max heap in the array itself, bottom up. The largest key is now at the root. A max heap is what makes the result ascending.

@list heading="Teardown, for m = n down to 2" items="Swap a[1] with a[m]: it's final@Swap|Shrink the heap to m − 1@Shrink|Sift the new root down@Sift"
Then tear it down. Swap the root with the last slot the heap still owns. That key is now final. Shrink the heap by one, so it no longer owns that slot. And sift the new root down, swapping with the larger child while that child is bigger.

@art swap-down
Each sift goes one level at a time. Compare the two children, pick the larger, and swap if it's bigger than the key coming down. That's at most two comparisons per level.

@art heap-and-suffix
So the array holds two things at once. A shrinking heap on the left, and a growing sorted suffix on the right. The boundary between them is a single index, and nothing extra is allocated.

@chapter Eight keys, counted
@math heading="8 1 3 6 5 2 7 4" items="build:  8 comparisons  →  8 6 7 4 5 2 3 1@the build;;teardown:  18 more@seven rounds;;total:  26 comparisons,  20 swaps@twenty six"
On eight, one, three, six, five, two, seven, four, the build costs eight comparisons and gives the heap eight, six, seven, four, five, two, three, one. The seven rounds of teardown cost eighteen more. That's twenty six comparisons and twenty swaps.

@words text="merge sort: 17 · ⌈log₂ 8!⌉ = 16"
For comparison, merge sort on the same keys spends seventeen. And the ceiling of log two of eight factorial is sixteen. No comparison sort can do better on every array of eight.

@art build-vs-teardown
The surprise is which phase is cheap. At sixteen keys, the build costs twenty two comparisons and the teardown fifty eight. Most nodes sit near the bottom and barely move during the build. But every teardown round starts at the root and usually travels most of the way down.

@chapter Not adaptive
@math heading="16 keys" items="increasing:  85@increasing;;shuffled:  80@a shuffle;;decreasing:  72@decreasing"
Heapsort isn't adaptive. At sixteen keys: increasing input costs eighty five, a shuffle eighty, decreasing input seventy two. Already sorted input is the most expensive of the three, because ascending order is the worst starting shape for a max heap.

@chapter Not stable
@math heading="Eight records, four keys" items="in:  1#1 2#2 3#3 4#4 1#5 2#6 3#7 4#8@eight records;;out:  1#5 1#1 2#6 2#2 3#3 3#7 4#8 4#4@heapsort returns"
And it isn't stable. Take eight records with four distinct keys, tagged by position. Heapsort returns the ones as five then one, the twos as six then two, and the fours as eight then four.

@art equal-flip
That's three pairs of equal keys reversed. One would have been enough, because a single reversed pair refutes stability.

@art long-moves
The build moves keys across the whole array. The last slot can end up at the root. So equal keys get swapped past each other before the sort proper even starts.

@chapter What it does promise
@words text="Θ(1) extra memory · Θ(n log n) worst case" sub="no bad input, no randomness"
What it does promise is why people use it. Constant extra memory, and an n log n worst case, with no bad input and no randomness. Quicksort can't offer that, and merge sort needs a second array to. When memory is the binding constraint and you want a guarantee, this is the sort.

@math heading="16 keys, same array" items="⌈log₂ 16!⌉ = 45@forty five;;merge sort:  48@forty eight;;heapsort:  80@eighty"
The price is a constant factor. At sixteen keys, the lower bound is forty five. Merge sort spends forty eight, heapsort eighty. Both are n log n. Heapsort's constant is bigger, mainly because each sift compares against both children at every level. The gap between forty five and eighty isn't slack in the bound. It's the price of those promises.

@chapter Where people slip
@list heading="Common slips" items="Inferring stability from Θ(n log n)@The first|Expecting the build to be the costly phase@The second|Reading in place as no movement@And the third"
The first slip is inferring stability or adaptivity from n log n. The second is expecting the build to dominate. It's the cheap half. And the third is reading in place as no movement. Twenty swaps on eight keys is plenty of movement, and that movement is what costs it stability.

@chapter Try it
@words text="Heapsort 8 1 3 6 5 2 7 4 by hand" sub="count every sift-down comparison"
Your turn. Run heapsort by hand on these eight keys, counting every comparison, and check you get twenty six. Then name the two promises it breaks.

@end text="Count the sifts"
You can step through heapsort's build and teardown and count each comparison, on Learn. That's learn dot get er done dot I O.
