---
format: short
lesson: intro-algorithms-advanced-structures/b-trees
title: The search tree that grows at the top
---

@art split-on-the-way-down
A binary search tree grows down at its leaves. A B-tree never does.

@art split-median
New keys go into existing leaves. A full node splits sideways, and its median key moves up into the parent.

@quote text="Unlike a binary search tree, a B-tree increases in height at the top instead of at the bottom." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 18.2"
The only new level is a new root above a split one. So every leaf stays at the same depth, with no rotations at all.

@end text="Full lesson on Learn"
Grow one and count its disk pages in the full lesson on Learn.
