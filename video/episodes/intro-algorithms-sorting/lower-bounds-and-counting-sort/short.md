---
format: short
lesson: intro-algorithms-sorting/lower-bounds-and-counting-sort
title: Why no comparison sort beats n log n
---

@art decision-tree
No sort that only compares keys can ever beat n log n. Here's the proof.

@art leaf-count
Draw the sort as a tree of comparisons. Every one of the n factorial orderings needs its own leaf.

@math items="2ʰ ≥ n!@two to the h;;h ≥ lg(n!) = Ω(n lg n)@log of n factorial"
A tree of height h has at most two to the h leaves. So h is at least log of n factorial, which is omega of n log n.

@end text="Full lesson on Learn"
See how counting sort escapes it in the full lesson on Learn.
