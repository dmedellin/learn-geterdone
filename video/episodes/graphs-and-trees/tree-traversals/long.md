---
format: long
lesson: graphs-and-trees/tree-traversals
title: Preorder, inorder, postorder: it's all about when you visit the root
thumb: Before, between, or after?
---

@chapter The question
@title text="Rooted Trees and Traversals" sub="Graphs and Trees" art=thumb
You need to visit every node of a tree exactly once. To copy it, to print it in order, or to evaluate it. There are three standard ways, and the only difference between them is one decision: when do you visit the root?

@chapter Three orders
@list heading="Three traversals" items="Preorder: root, left, right@Preorder|Inorder: left, root, right@Inorder|Postorder: left, right, root@Postorder"
Preorder visits the root, then traverses the left subtree, then the right. Inorder does the left subtree, then the root, then the right. Postorder does the left, then the right, and the root last.

@art tree-contour
The name tells you when the root is handled: before the subtrees, between them, or after both. Everything else is the same recursion. Each one is a structural induction, every node is visited exactly once, and the cost is linear in the number of nodes.

@chapter Expression trees
@art expression-tree
An arithmetic expression is a binary tree. The operators are internal nodes and the operands are leaves. Take three times four, plus five. The root is plus. Its left child is times, with leaves three and four. Its right child is five.

@math heading="(3 × 4) + 5" items="preorder:   + × 3 4 5   prefix@Preorder gives;;inorder:   3 × 4 + 5   infix@Inorder gives;;postorder:   3 4 × 5 +   postfix@postorder gives"
Preorder gives plus, times, three, four, five. That's prefix, or Polish notation. Inorder gives three times four plus five, the infix you normally read. And postorder gives three, four, times, five, plus. That's postfix, reverse Polish.

@art stack-evaluator
Postfix is what stack machines eat. Read left to right. Push each number. On an operator, pop two, and push the result. You never need parentheses or precedence rules, because the tree's structure is already in the order. Infix is the only one of the three that's ambiguous without them.

@chapter Binary search trees
@words text="Left subtree < node < right subtree"
A binary search tree is a binary tree where every node's key is bigger than everything in its left subtree, and smaller than everything in its right subtree.

@art bst-shape
And here's the payoff. An inorder traversal of a binary search tree visits the keys in increasing order. The left subtree comes out sorted and all smaller, then the root, then the right subtree, sorted and all larger. Put them together, and the whole thing is sorted.

@chapter All three on one tree
@math heading="Root 6 · 3 (2, 5) · 8 (7)" items="preorder:   6 3 2 5 8 7@Preorder is;;inorder:   2 3 5 6 7 8  sorted@Inorder is;;postorder:   2 5 3 7 8 6@Postorder is;;level order:   6 3 8 2 5 7@level order"
Here's a search tree with six at the root. Its left child is three, with children two and five. Its right child is eight, with a left child seven. Preorder is six, three, two, five, eight, seven. Inorder is two, three, five, six, seven, eight, sorted. Postorder is two, five, three, seven, eight, six. And level order is six, three, eight, two, five, seven.

@art level-order-rows
That last one, level order, visits by depth, row by row. It's exactly breadth first search from the root, using a queue instead of recursion, and it's the traversal that shows you the tree's shape.

@chapter Which one when
@list heading="Pick by the job" items="Preorder: copy or serialise@to copy|Inorder: sorted keys from a search tree@sorted keys|Postorder: evaluate or delete@evaluate|Level order: see the shape@shape"
Use preorder to copy or serialise a tree, because the root comes out first, so you can rebuild as you read. Use inorder to get sorted keys from a search tree. Use postorder to evaluate or delete, because children finish before their parent. And use level order to see the shape.

@art balanced-vs-path
Searching a balanced search tree costs log n, one comparison per level. But if the tree is lopsided, just a path, it degenerates to linear time. That's why balancing schemes exist.

@chapter Where people slip
@list heading="Common slips" items="Expecting preorder to be sorted@The first|Defining inorder with three or more children@The second|Thinking one traversal fixes the shape@And the third"
The first slip is expecting preorder to be sorted. Only inorder is. The second is defining inorder for a general tree. With three or more children, there's no single place for the root. And the third is thinking one sequence determines a binary tree. In general, you need preorder and inorder together.

@chapter Try it
@words text="Postfix: which traversal?" sub="and what does 3 4 × 5 + evaluate to?"
Your turn. Postfix notation comes from which traversal? Then run three, four, times, five, plus through a stack by hand, and check that you get the same answer as the infix version.

@end text="Read all four orders yourself"
You can load a tree and read all four orders off it, on Learn. That's learn dot get er done dot I O.
