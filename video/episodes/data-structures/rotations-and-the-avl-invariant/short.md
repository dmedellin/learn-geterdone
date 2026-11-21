---
format: short
lesson: data-structures/rotations-and-the-avl-invariant
title: A rotation reshapes a tree and moves no keys
---

@art rotate-right
A rotation reshapes a search tree completely, and every key keeps its place in sorted order.

@math items="before:  A, y, B, x, C@before;;after:  A, y, B, x, C@after"
Rotate right at x. The left child y rises, and y's right subtree moves under x. Read the tree in order, before and after. A, y, B, x, C, both times.

@words text="Only pointers move"
Only pointers changed. That's why a rotation can't break the search tree, and why every balanced tree uses them.

@end text="Full lesson on Learn"
The full lesson, with the exact height table, is on Learn.
