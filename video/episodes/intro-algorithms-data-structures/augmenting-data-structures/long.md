---
format: long
lesson: intro-algorithms-data-structures/augmenting-data-structures
title: Augmenting data structures: order statistics in log n
thumb: Add one field, get rank
---

@chapter Adapt, don't invent
@title text="Augmenting Data Structures" sub="Introduction to Algorithms, Chapter 14" art=thumb
Most new data structures aren't new at all. They're old ones with an extra field. Chapter fourteen shows how to add information to a red black tree, and which information comes free.

@chapter Order statistics, dynamically
@art size-tree
Chapter nine selected the ith smallest key in linear time, on a set that didn't change. On a dynamic set, the authors want O of log n. The device is to store in each node the size of its subtree. A node's size is its left child's size, plus its right child's size, plus one.

@art select-walk
To select the key of rank i, start at the root and compute r, the left child's size plus one. If i equals r, you've found it. If i is smaller, go left with the same i. If it's larger, go right, looking for rank i minus r, since r keys have been passed. Each step drops a level, so it's O of log n.

@art rank-climb
Rank goes the other way. Start at the node, with r equal to its left size plus one, and climb to the root. Each time you climb from a right child, add the left sibling's size plus one. At the root, r is the rank.

@math heading="44 21 70 9 33 58 86 27 39 64" items="select i = 4  →  33@select the fourth;;3 of 10 nodes visited@three of the ten"
In the lab, build a tree from forty four, twenty one, seventy, nine, thirty three, fifty eight, eighty six, twenty seven, thirty nine and sixty four. Select the fourth smallest, and you get thirty three, after visiting three of the ten nodes. A scan would read up to ten. The walk reads one path.

@chapter Keeping sizes right
@art rotation-sizes
The sizes must stay correct. On insertion, add one to each node passed on the way down. The fix up only recolours and rotates. Recolouring leaves sizes alone, and a rotation spoils exactly two, the two nodes it moves. Recompute them in constant time, the lower one first.

@words text="At most 2 rotations → O(1) extra" sub="deletion: subtract one along the path"
At most two rotations means constant extra work. Deletion subtracts one along the path to the root, and patches its rotations the same way.

@chapter The four steps
@art four-steps
The book gives a method in four steps. Pick the structure to build on. Decide what extra information it carries. Make sure its modifying operations can keep that information correct. And write the new operations that use it.

@quote text="As with any prescriptive design method, you should not blindly follow the steps in the order given." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 14.2"
But the authors add a warning. As with any prescriptive design method, you should not blindly follow the steps in the order given. Steps two and four are worthless if step three fails.

@chapter Which fields come free
@math heading="Theorem 14.1" items="f(x) computable from x and its two children@from the node itself;;→ insert and delete still O(lg n)@still run in O of log n"
Theorem fourteen point one says which fields come free. If a node's field can be computed from the node itself and its two children, insertion and deletion can maintain it and still run in O of log n.

@words text="Subtree size: yes · Global rank: no · Depth: no" sub="a change reaches only the ancestors"
The proof: a change to one node's field affects only its ancestors, and there are O of log n of them. Subtree size passes. But a node's rank in the whole tree doesn't. Insert a new smallest key, and every rank changes. Depth fails too, since a rotation changes the depth of a whole subtree.

@art interval-tree
Section fourteen point three is a second example. An interval tree stores intervals keyed on their low endpoints, and each node also keeps the largest high endpoint in its subtree. That's computable from the node and its children, so the theorem applies, and searching for an overlap walks one path.

@chapter Common slips
@list heading="Common slips" items="Storing global rank instead of subtree size@The first|Forgetting rotations change sizes@The second|Following the four steps strictly in order@the third"
The first slip is storing each node's rank in the whole tree instead of its subtree size. The second is forgetting that rotations change sizes. And the third is following the four steps strictly in order.

@chapter Try it
@words text="44 21 70 9 33 58 86 27 39 64" sub="sizes, then OS-RANK on 39"
Your turn. In the tree built from those ten keys, write every node's size. Then find the rank of thirty nine by climbing, writing r after each step. Check it in the lab, where the downward walk makes the same additions your climb made.

@end text="Walk a size-annotated tree"
You can walk a size annotated tree and count the nodes each query visits, on Learn. That's learn dot get er done dot I O.
