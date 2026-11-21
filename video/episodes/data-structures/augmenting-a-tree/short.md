---
format: short
lesson: data-structures/augmenting-a-tree
title: Why nobody stores a median in a tree
---

@art size-tree
You can store a subtree's size at every node. So why not its median?

@words text="size = 1 + left + right"
A field can ride along only if a node can rebuild it from its own key and its two children's values. Size can. So can sum and min.

@words text="median ✗"
A median can't. One key and the medians of two halves don't give you the median of the whole.

@end text="Full lesson on Learn"
The full lesson, with rank and select walks, is on Learn.
