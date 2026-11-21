---
format: short
lesson: intro-algorithms-data-structures/augmenting-data-structures
title: One extra field turns a tree into a rank finder
---

@art size-tree
One number per node finds the ith smallest key in log n.

@words text="x.size = left + right + 1"
That number is the size of the node's subtree. It depends only on the node's two children.

@art select-walk
So to find rank i, compare i with the left size plus one. Equal, you're done. Smaller, go left. Larger, go right, and subtract.

@end text="Full lesson on Learn"
Walk the tree yourself in the full lesson on Learn.
