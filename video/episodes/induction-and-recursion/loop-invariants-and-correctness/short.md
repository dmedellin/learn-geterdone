---
format: short
lesson: induction-and-recursion/loop-invariants-and-correctness
title: The loop invariant that proves too little
---

@art flattened-bars
Here's a sorting proof that also accepts setting every element to zero.

@words text="invariant:  A[0..j−1] is sorted"
Insertion sort, with the invariant: the first j elements are sorted. It's true at the start, every pass keeps it true, and at the end the array is sorted.

@words text="sorted  +  the same elements"
But an array of zeros is sorted too. The invariant has to say the elements are the original ones as well.

@end text="Full lesson on Learn"
The full lesson on loop invariants is on Learn.
