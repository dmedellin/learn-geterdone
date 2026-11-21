---
format: short
lesson: dynamic-programming/dynamic-programming-on-a-tree
title: Why a tree makes an NP-hard problem easy
---

@art disjoint-subtrees
NP hard on a general graph. On a tree, it's one pass.

@words text="with(v) · without(v)"
Choose vertices, no two adjacent, with the biggest total weight. Keep two numbers per vertex: the best in its subtree with it, and without it.

@words text="subtrees share no edge"
It works because a tree's subtrees share no vertex and no edge, so each one can be solved on its own. Add a cycle, and that's gone.

@end text="Full lesson on Learn"
Try your own tree on Learn.
