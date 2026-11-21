---
format: long
lesson: intro-algorithms-data-structures/red-black-trees
title: Red-black trees: five rules that keep a tree balanced
thumb: One bit, height 2 lg(n+1)
---

@chapter Why colour a tree
@title text="Red-Black Trees and Rotations" sub="Introduction to Algorithms, Sections 13.1 and 13.2" art=thumb
In a binary search tree, every operation costs the height, and a bad insertion order makes the height n minus one. A red black tree spends one bit per node, a colour, to keep the height logarithmic whatever order the keys come in.

@quote text="no such path is more than twice as long as any other, so that the tree is approximately balanced." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 13.1"
The colours are constrained so that no such path is more than twice as long as any other, so that the tree is approximately balanced. The paths are the ones from the root down to a leaf.

@chapter Leaves and the sentinel
@art nil-sentinel
First, a convention. Wherever a node lacks a child, the missing child counts as a leaf, an external node. Every key bearing node then has exactly two children. The book uses one black sentinel, T nil, for every leaf, one extra object per tree.

@chapter Five properties
@list heading="The red-black properties" items="Every node is red or black@red or black|The root is black@The root|Every leaf is black@Every leaf|A red node has two black children@A red node|Equal black counts down every path@from any node"
Here are the five rules. Every node is red or black, the root is black, and every leaf, T nil, is black. A red node has two black children. And from any node, every path down to a leaf meets the same number of black nodes.

@art rb-tree
That last count is the black height of a node. It leaves the node itself out, and counts the leaf. In the lab's eight node example, the root twenty six has black height two.

@art black-count
Rules four and five do the work. By rule five, every path from the root has the same number of black nodes. By rule four, no two reds are adjacent.

@art short-long-paths
So reds can at most alternate with blacks. The shortest possible path is all black, and the longest alternates. That's the factor of two.

@chapter The height bound
@math heading="Lemma 13.1" items="subtree at x holds ≥ 2^bh(x) − 1 nodes@at least two to the;;bh(root) ≥ h/2@at least h over two;;n ≥ 2^(h/2) − 1@n is at least;;h ≤ 2·lg(n + 1)@two log of n plus one"
By induction, the subtree at any node x holds at least two to the black height of x, minus one, internal nodes. Since at least half of every path is black, the root's black height is at least h over two. So n is at least two to the h over two, minus one, and h is at most two log of n plus one.

@words text="Search, min, max, successor: O(lg n)" sub="Chapter 12's code, unchanged"
So searching, minimum, maximum, successor and predecessor all run in O of log n, with Chapter twelve's code unchanged. Insertion and deletion are different, because they can break the rules.

@chapter Rotations
@art rotation
The repair tool is the rotation. A left rotation at x, whose right child is y, makes y the root of the subtree, makes x y's left child, and hands y's old left subtree across to x. A right rotation is the mirror image.

@math heading="Left rotation at x" items="before: x(α, y(β, γ))@before;;after: y(x(α, β), γ)@after;;inorder: α x β y γ@both times"
Before, x has left subtree alpha and right child y, with subtrees beta and gamma. After, y has left child x and right subtree gamma, and x has alpha and beta. The inorder sequence is alpha, x, beta, y, gamma both times. It runs in constant time, and only pointers change.

@chapter Checking trees
@art bad-red-pair
The lab checks trees against all five rules. Add a red thirty below the red thirty three, and rule four fails at thirty three, while rule five still holds, since a red node adds no black. Blacken fifty two instead, and rule five fails at forty one.

@words text="Correct colours, wrong order" sub="30 sits in 26's left subtree"
And here's a tree coloured perfectly that isn't a search tree at all. Thirty sits in twenty six's left subtree. The colours constrain shape. They say nothing about key order.

@chapter Common slips
@list heading="Common slips" items="Thinking the rules mean perfect balance@The first|Counting black-height wrongly@The second|Letting colours stand in for key order@the third"
The first slip is reading the rules as perfect balance. They allow a factor of two. The second is counting black height wrongly, by counting the node itself, or leaving out the leaf. And the third is thinking the colours can stand in for the search tree property.

@chapter Try it
@words text="20 black · 10 black, 30 red · 5 red · 25, 40 black · 35, 45 red" sub="give every black-height"
Your turn. Root twenty black, with ten black and thirty red below it, five red below ten, twenty five and forty black below thirty, and thirty five and forty five red below forty. Give every black height. Then colour forty red, and thirty five and forty five black, and say which rule fails, and where.

@end text="Check a tree's colours"
You can check trees against all five properties, and find where each one fails, on Learn. That's learn dot get er done dot I O.
