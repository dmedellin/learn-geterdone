---
format: short
lesson: graphs-and-trees/tree-traversals
title: The traversal that sorts a search tree for free
---

@art bst-shape
One traversal of a search tree hands you every key in sorted order.

@words text="Inorder: left, root, right"
It's inorder. Visit the left subtree, then the root, then the right subtree. In a search tree, everything on the left is smaller and everything on the right is larger.

@math items="inorder:   2 3 5 6 7 8@two, three"
So with six at the root, inorder reads two, three, five, six, seven, eight. Sorted, with no sorting step.

@end text="Full lesson on Learn"
The full lesson on tree traversals is on Learn.
