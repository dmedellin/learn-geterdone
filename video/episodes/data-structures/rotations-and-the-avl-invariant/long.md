---
format: long
lesson: data-structures/rotations-and-the-avl-invariant
title: Tree rotations and the AVL rule, with the exact height table
thumb: Move pointers, not keys
---

@chapter The question
@title text="Rotations and the AVL Invariant" sub="Data Structures" art=thumb
A search tree can degenerate into a path. To stop that, you need a way to reshape a tree without breaking it, and a rule that says when the shape is good enough. That's a rotation, and the AVL condition.

@chapter The rotation
@art rotate-right
Take a node x with a left child y. A right rotation lifts y into x's place. x becomes y's right child. And y's old right subtree becomes x's new left subtree. A left rotation is the mirror image. Either way, it's a fixed number of pointer writes.

@math heading="Right rotation at x" items="before, in order:  A, y, B, x, C@before;;after, in order:  A, y, B, x, C@after"
Why is it safe? Call the subtrees A and B under y, and C under x. In order, before, you read A, y, B, x, C. After the rotation, you read A, y, B, x, C. Identical, symbol by symbol.

@words text="No key moves in the sorted order" sub="only pointers change"
So no key changes its position in the sorted order, and the search tree invariant survives automatically. What does change is the heights, by at most one at each of the two nodes. That's the whole point.

@art rotate-example
Here's one. Keys fifty, thirty, seventy, twenty, forty, ten. Rotate right at fifty, and thirty becomes the root. The in order sequence is ten, twenty, thirty, forty, fifty, seventy, before and after. The height drops from three to two.

@art rotation-impossible
Two cautions. A rotation needs the child it lifts. There's no right rotation at a node without a left child, and the lab says not possible, rather than quietly returning the same tree. From outside, nothing changed and order preserved look identical.

@words text="Not every rotation shortens a tree" sub="50 30 70 20 40 35 45: rotate left at 30 → height still 3"
And not every rotation shortens a tree. Rotate left at thirty in the tree from fifty, thirty, seventy, twenty, forty, thirty five, forty five, and the height stays at three. A rotation is a tool, not a repair.

@chapter The AVL condition
@math heading="AVL tree" items="|h_L − h_R| ≤ 1  at every node@differ by at most one;;balance factor ∈ {−1, 0, 1}@minus one, zero or one;;empty: −1 · leaf: 0@an empty subtree"
An AVL tree is a search tree where, at every node, the heights of the two subtrees differ by at most one. That difference is the balance factor, and it must be minus one, zero or one. An empty subtree has height minus one, and a leaf has height zero. Each node stores its height.

@chapter How tall can it get
@art sparse-avl
To bound the height, ask the opposite question. What's the fewest nodes an AVL tree of height h can have? Call it N of h. One subtree must have height h minus one. The other has height at least h minus two, since a difference of two isn't allowed.

@math heading="Fewest nodes at height h" items="N(0) = 1,  N(1) = 2@N of zero;;N(h) = N(h−1) + N(h−2) + 1@plus one;;1, 2, 4, 7, 12, 20, 33, 54, 88@one, two, four"
So N of zero is one, N of one is two, and N of h is N of h minus one, plus N of h minus two, plus one, for the root. That gives one, two, four, seven, twelve, twenty, thirty three, fifty four, eighty eight.

@art fib-growth
Add one to each and you get Fibonacci numbers: two, three, five, eight, thirteen. So the node count grows exponentially with height, which means the height grows only logarithmically with the nodes.

@chapter Reading the table
@math heading="Largest h with N(h) ≤ n" items="n = 6:  N(2) = 4 ≤ 6,  N(3) = 7 > 6  ⟹  h ≤ 2@six nodes;;n = 1000:  N(13) = 986,  N(14) = 1596  ⟹  h ≤ 13@a thousand nodes"
To bound a tree on n nodes, find the largest h whose N is at most n. Six nodes: N of two is four, N of three is seven, so the height is at most two. A thousand nodes: N of thirteen is nine eighty six, N of fourteen is fifteen ninety six, so at most thirteen.

@art table-vs-formula
The usual formula, one point four four log two n, gives fourteen point three five, so it permits fourteen. Both are correct bounds, but the table is tighter. It's integer arithmetic with nothing to round, while one point four four is itself a rounded constant. Use the formula for the shape, and the table for the number.

@chapter Where people slip
@list heading="Common slips" items="Thinking a rotation rearranges keys@The first|Expecting every rotation to shorten the tree@The second|Quoting 1.44 log₂ n when the table is there@And the third"
The first slip is thinking a rotation rearranges keys. Write both in order sequences out and compare them. That also catches the real error, dropping the inner subtree. The second is expecting every rotation to shorten the tree. And the third is quoting one point four four log n when the exact table is right there.

@chapter Try it
@words text="Rotate right at 50" sub="keys 50 30 70 20 40 10"
Your turn. Build the tree from fifty, thirty, seventy, twenty, forty, ten, rotate right at fifty, and write both in order sequences. Then use the table to bound the height of an AVL tree on a hundred nodes.

@end text="Rotate a tree yourself"
You can rotate at any node and compare the in order sequences, on Learn. That's learn dot get er done dot I O.
