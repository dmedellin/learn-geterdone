---
format: short
lesson: intro-algorithms-data-structures/red-black-trees
title: Why a red-black tree is never more than 2 times off
---

@art short-long-paths
In a red black tree, no path is over twice another. Why?

@words text="Same number of blacks on every path"
Every path from the root down to a leaf meets the same number of black nodes. And a red node can't have a red child.

@art rb-tree
So the shortest possible path is all black, and the longest alternates red and black. That's at most twice the length, and a height of at most two log of n plus one.

@end text="Full lesson on Learn"
Check trees yourself in the full lesson on Learn.
