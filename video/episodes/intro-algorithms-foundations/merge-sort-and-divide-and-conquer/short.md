---
format: short
lesson: intro-algorithms-foundations/merge-sort-and-divide-and-conquer
title: Why merge sort is n log n
---

@art recursion-tree
Why is merge sort n log n? Draw the tree and add each row.

@art level-sums
Each level of the recursion tree has twice as many pieces, each half the size. So every level costs the same, c times n.

@math items="lg n + 1 levels × c·n@log n plus one levels;;= Θ(n lg n)@theta of n log n"
There are log n plus one levels. Multiply, and you get theta of n log n.

@end text="Full lesson on Learn"
Count the merges yourself in the full lesson on Learn.
