---
format: short
lesson: data-structures/binary-search-trees
title: Every parent is in order, and it's still not a BST
---

@art bad-tree
Every parent here is in order with its children. It's still not a search tree.

@words text="20 → left 10 → right 25"
Twenty five is the right child of ten, which is the left child of twenty. So twenty five sits in twenty's left subtree, and it's bigger than twenty. A search for it turns left and never finds it.

@words text="Walk it in order: 10, 25, 20, 30"
The cheap test is an in order walk. If it isn't sorted, the tree is broken.

@end text="Full lesson on Learn"
The full lesson, with both checks running, is on Learn.
