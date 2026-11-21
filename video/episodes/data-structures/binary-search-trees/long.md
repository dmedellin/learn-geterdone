---
format: long
lesson: data-structures/binary-search-trees
title: Binary search trees: the check that passes on a broken tree
thumb: Subtrees, not children
---

@chapter The question
@title text="Binary Search Trees" sub="Data Structures" art=thumb
Here's a tree where every parent is bigger than its left child and smaller than its right one. It still isn't a binary search tree. Seeing why is the whole lesson.

@chapter The invariant
@art subtree-rule
At every node x, every key in the left subtree is less than x, and every key in the right subtree is greater. That's about whole subtrees, not just the two children. Duplicates are left out here.

@art search-path
That's what makes search a single path. Compare with the root. If the target is smaller, it can only be on the left, because nothing on the right is smaller. Repeat. So the comparisons are at most the height plus one. Insert is the same walk, ending where the search failed.

@chapter The local check fails
@art bad-tree
Here's the trap. Root twenty, left child ten, right child thirty, and twenty five as the right child of ten. Ten is less than twenty, thirty is more than twenty, twenty five is more than ten. Every local check passes.

@math heading="In-order walk" items="10, 25, 20, 30@ten, twenty five;;not sorted ⟹ not a search tree@isn't sorted"
But walk it in order: left subtree, then the node, then the right. You get ten, twenty five, twenty, thirty. That isn't sorted, and the walk names the offender. Twenty five sits in twenty's left subtree, so a search for twenty five turns left at the root and never finds it.

@words text="in-order walk is sorted ⟺ search tree"
That's also the right test. An in order walk comes out sorted if and only if the tree is a binary search tree. So a sorted walk certifies the invariant everywhere, including the subtree conditions the local check never looks at.

@art inorder-walk
Picture the walk weaving round the tree from left to right. Everything in a left subtree comes out before its node, and everything in the right subtree comes out after. That's just the invariant, unrolled.

@chapter Deleting a node
@list heading="Three cases" items="No children: unlink it@No children|One child: splice the child up@One child|Two children: use the in-order successor@Two children"
Deletion has three cases. No children: unlink it. One child: splice the child into its place, and the whole subtree moves up unchanged. Two children: neither child can just take over, because the other subtree would have nowhere correct to go.

@art successor
So replace the key, not the node. The in order successor is the smallest key in the right subtree. Go right once, then left as far as you can. Everything left is smaller than it, everything still on the right is bigger. And it has no left child, so removing it is an easy case.

@math heading="Insert 50 30 70 20 40 60 80, delete 30" items="30 has two children, 20 and 40@two children;;successor of 30 = 40@successor;;in-order:  20 40 50 60 70 80@still sorted"
Insert fifty, thirty, seventy, twenty, forty, sixty, eighty. Now delete thirty. It has two children, twenty and forty. Its successor is forty, which has no children. Forty takes thirty's place, twenty stays put, and the in order walk is still sorted. The lab counts thirteen comparisons and a height of two.

@words text="delete 50 → successor 60 becomes the root"
Delete the root instead, and it's the same rule with a longer reach. The successor of fifty is sixty, in the other subtree. Sixty becomes the root, and seventy keeps eighty as its right child.

@chapter Shape decides cost
@math heading="Same 8 operations" items="keys 50 30 70 20 40 60 80:  13 comparisons@thirteen;;keys 20 30 40 … 80:  height 6,  23 comparisons@twenty three"
Search for forty, and the path is fifty, thirty, forty: three comparisons. Now run the same eight operations with the keys arriving in sorted order. The inserts build a path of height six, and the whole thing costs twenty three comparisons rather than thirteen.

@art path-tree
Same keys, same algorithm. Only the order changed. The invariant is about correctness, and says nothing about shape. A search tree is log n per operation exactly when it's short, and nothing so far makes it short.

@chapter Where people slip
@list heading="Common slips" items="Checking each node against its children only@The first|Promoting one child of a two-child node@The second|Expecting the invariant to give log n@And the third"
The first slip is checking a node against its children only. The second is promoting one child when deleting a node with two, which leaves the other subtree with nowhere to go. And the third is expecting the invariant to promise a logarithmic cost.

@chapter Try it
@words text="Delete 50 from 50 30 70 20 40 60 80"
Your turn. Build the seven key tree, delete fifty, and draw the result. Then walk it in order and check it's still sorted.

@end text="Break the invariant yourself"
You can build the tree that fools the local check and watch both checks run, on Learn. That's learn dot get er done dot I O.
