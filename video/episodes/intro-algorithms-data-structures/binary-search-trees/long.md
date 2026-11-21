---
format: long
lesson: intro-algorithms-data-structures/binary-search-trees
title: Binary search trees: every operation costs the height
thumb: Height is the cost
---

@chapter Height is the cost
@title text="Binary Search Trees" sub="Introduction to Algorithms, Chapter 12" art=thumb
Hash tables are fast on average and slow in the worst case, and they forget the order of the keys. A binary search tree keeps the order, and makes one number decide the cost of everything.

@quote text="Basic operations on a binary search tree take time proportional to the height of the tree." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 12"
The chapter's second paragraph says it outright. Basic operations on a binary search tree take time proportional to the height of the tree.

@chapter The property
@art bst-property
Each node has a key, and pointers to its left child, its right child and its parent. The rule is about whole subtrees. Every key in a node's left subtree is at most its key, and every key in its right subtree is at least its key.

@words text="Inorder walk → sorted keys" sub="left subtree, node, right subtree · Θ(n)"
Different trees can hold the same keys. What they share is this. Walk the tree inorder, left subtree, then the node, then the right subtree, and the keys come out sorted, in theta of n time.

@chapter Queries
@art search-path
Search compares the key it wants with the node's key, and goes left if smaller, right if larger, until it finds a match or runs out of tree. Minimum just follows left pointers to the end. Maximum follows right pointers. Each follows one path down, so each is O of h.

@art successor-climb
The successor has two cases. If the node has a right subtree, it's the leftmost node there. If not, climb up until you arrive at a node from its left child. That node is the successor. It never compares a key, because the shape of the tree already encodes the order.

@chapter Insert and delete
@words text="Insert: walk down, hang a new leaf" sub="O(h)"
Insert walks down as a search would, keeping a trailing pointer to the last node passed, and hangs the new node from it as a leaf.

@art delete-cases
Deleting a node z has three cases. With no left child, z is replaced by its right subtree. With no right child, by its left. And with two children, z's successor takes its place.

@art successor-lift
The successor sits in z's right subtree, and it has no left child, which makes it easy to lift out. If it's z's right child, it moves straight up. If it's deeper, first hand its right subtree to its parent, then lift it into z's place. Subtrees are moved whole, by transplant.

@math heading="41 20 65 11 29 50 91 32 72 99, then −65" items="successor 72 moves up@seventy two;;9 keys, height 3, 23 comparisons@nine keys"
In the lab, insert forty one, twenty, sixty five, eleven, twenty nine, fifty, ninety one, thirty two, seventy two, ninety nine, then delete sixty five. Its successor, seventy two, moves up from below ninety one. That leaves nine keys, height three, and twenty three comparisons in all.

@chapter The shape problem
@art chain-vs-bushy
The height depends on the order of insertion. Insert keys in increasing order, and you get a chain of height n minus one, just a linked list. The best any tree can do is the floor of log n.

@words text="Same 10 keys: height 3 or 9" sub="19 comparisons or 45"
Those same ten keys in the order above give height three and nineteen comparisons. In increasing order, height nine and forty five comparisons. One set of keys, two costs, decided by the order alone.

@math heading="Theorem 12.4" items="random insertion order  →  expected height O(lg n)@random order"
Section twelve point four proves that if keys are inserted in a random order, the expected height is O of log n. But deletions are excluded, and the randomness is in the order of the keys, which a program usually doesn't choose.

@chapter Common slips
@list heading="Common slips" items="Checking the property only parent to child@The first|Assuming the successor is the right child@The second|Treating O(lg n) as every tree's cost@the third"
The first slip is checking the property only between parents and children. A key can be wrong two levels up. The second is assuming the successor is always the deleted node's right child. And the third is treating O of log n as the cost of every search tree operation. It's O of h.

@chapter Try it
@words text="41 20 65 11 29 50 91 32 72 99" sub="delete 20 · successor of 32"
Your turn. Build the tree from those ten keys by hand. Delete twenty, say which case applies, and give the height and inorder sequence. Then find the successor of thirty two by the climbing rule, without comparing keys.

@end text="Build and prune a tree"
You can build and prune a tree with every comparison counted, on Learn. That's learn dot get er done dot I O.
