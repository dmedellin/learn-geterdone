---
format: short
lesson: data-structures/avl-insertion
title: Why one rotation can't fix this AVL tree
---

@art single-fails
Insert thirty, ten, twenty, and one rotation just tips the tree the other way.

@words text="LR: the key went inside"
Thirty leans left, but the new key went into the right side of its left child. Rotate thirty right, and twenty comes along, landing on the wrong side again.

@art double-rotation
So rotate ten left first, then thirty right. Twenty, the inner grandchild, rises to the root.

@end text="Full lesson on Learn"
The full lesson, with all four cases animated, is on Learn.
