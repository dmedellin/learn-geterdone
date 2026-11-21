---
format: long
lesson: sorting-and-selection/partitioning
title: Partitioning: the one pass that does all of quicksort's work
thumb: One element placed for good
---

@chapter The question
@title text="Partitioning" sub="Sorting and Selection" art=thumb
Strip the recursion out of quicksort and what's left is one pass called partition. It does all the work. And after it, exactly one element is in its final place, and nothing else is sorted.

@chapter What partition means
@art pivot-split
To partition a range around a pivot p is to rearrange it so p sits at some index q, with everything left of q at most p, and everything right of q above p. The index q is returned. It isn't chosen in advance, and it usually isn't the middle.

@chapter Lomuto's scheme
@list heading="Lomuto's pass" items="Park the pivot at the end@Park the pivot|Walk j from lo to hi − 1@Walk j|If a[j] ≤ pivot: i = i + 1, swap a[i], a[j]@If a of j|Finally swap a[i+1], a[hi]@finally"
Here's the scheme this course counts. Park the pivot at the end. Walk j from lo to hi minus one, with a second index i marking the end of the small region. If a of j is at most the pivot, advance i and swap a of i with a of j. Finally, swap a of i plus one with the pivot.

@art three-regions
The invariant is three regions. From lo to i, at most the pivot. From i plus one to j minus one, above it. From j to the end, not yet looked at. The indices are the boundaries between them.

@art scan-step
Watch one step. j points at the next element. If it's bigger than the pivot, j just moves on, and the middle region grows. If it's at most the pivot, i moves up one, the element is swapped into the small region, and then j moves on.

@list heading="The invariant holds" items="Before: two regions empty@Before the loop|Each step: one case or the other@Each step|At exit: nothing unexamined@At exit"
Before the loop, i is one before the start, so two regions are empty and it holds for any array. Each step examines a of j: bigger, and the middle region grows; smaller or equal, and one element moves from the middle into the first. At exit, nothing is unexamined.

@art final-swap
So the array reads: at most, above, pivot. The final swap exchanges the pivot with the first element above it. Now the pivot sits at i plus one, with everything at most it on the left and everything above it on the right. That's its place in sorted order, and no later recursion can move it.

@chapter Twelve elements
@math heading="pivot 24" items="38 27 43 3 9 82 10 55 16 7 91 24@thirty eight;;11 comparisons,  6 swaps@eleven comparisons;;3 9 10 16 7 24 43 55 38 27 91 82@the array is"
Take thirty eight, twenty seven, forty three, three, nine, eighty two, ten, fifty five, sixteen, seven, ninety one, and the pivot, twenty four. Eleven comparisons and six swaps later, the array is three, nine, ten, sixteen, seven, twenty four, then forty three, fifty five, thirty eight, twenty seven, ninety one, eighty two.

@words text="left: 3 9 10 16 7 · right: 43 55 38 27 91 82" sub="neither side is sorted"
Twenty four is at position six. Five elements are at most it, six are above. And look at the sides. Neither is in order. Sorting them is the recursion's job, not this pass's.

@words text="comparisons = n − 1" sub="every input of length n"
Every element except the pivot is compared with it exactly once. So twelve elements always cost eleven comparisons, whatever they are. That's what makes quicksort's cost the sum of its range sizes.

@chapter Hoare's scheme
@art two-pointers
Hoare's partition walks one index up from the left and one down from the right, swapping an out of place pair whenever both stop. It does fewer swaps, four rather than six on this array. But its comparison count depends on the data, fourteen here, and it returns a boundary rather than placing the pivot.

@art equal-keys-side
Both schemes send keys equal to the pivot to one side. That sounds like a detail. On an array of all equal keys, it's a disaster, and it comes back two lessons from now.

@chapter Where people slip
@list heading="Common slips" items="Expecting the two sides to be sorted@The first|Swapping before advancing i@The second|Assuming the pivot lands in the middle@And the third"
The first slip is expecting the sides to be sorted. The second is swapping before advancing i, which overwrites the boundary. Advance i, then swap, then advance j. And the third is assuming the pivot lands near the middle. With pivot forty three on the same array, it lands at position nine.

@chapter Try it
@words text="Partition around 43" sub="state the three regions at every step"
Your turn. Partition the same twelve elements, but with forty three as the pivot. At every step, write down i, j and the three regions, and check the pivot lands at position nine.

@end text="Step through the partition"
You can step through every comparison and watch the invariant checked, on Learn. That's learn dot get er done dot I O.
