---
format: short
lesson: induction-and-recursion/structural-induction
title: How to do induction on a tree
---

@art tree-two-parts
How do you do induction on a tree? There's no n to count.

@words text="Induct on how it was built"
You follow the definition instead. A tree is either empty, or a root with two subtrees.

@art full-tree
So prove your claim for the empty tree. Then assume it for both subtrees, and prove it for the tree built from them. Both subtrees, not just one.

@end text="Full lesson on Learn"
The full lesson, with strings and formulas too, is on Learn.
