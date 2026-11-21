---
format: long
lesson: data-structures/priority-queues-and-binary-heaps
title: Binary heaps: a tree hiding in a plain array
thumb: Ordered down, not across
---

@chapter The question
@title text="Priority Queues and Binary Heaps" sub="Data Structures" art=thumb
You want the smallest item, over and over, while new items keep arriving. A binary heap does both in logarithmic time, with no pointers at all. And it does it without ever being sorted.

@chapter The heap property
@art heap-tree
A min heap is a complete binary tree with one rule. Every parent is less than or equal to both of its children. Complete means every level is full except maybe the last, which fills from the left.

@words text="parent ≤ both children" sub="so the root holds a minimum"
That rule is only about ancestry. The root is an ancestor of everything, and the inequality carries down every path, so the root holds a minimum. Siblings, though, are in no particular order. And a max heap just flips the inequality.

@chapter A tree in an array
@art array-as-tree
Because the tree is complete, you can write its levels out left to right in an array. Then the shape is just arithmetic. No node stores a link.

@math heading="Positions from 1" items="children of i:  2i  and  2i + 1@two i and two i plus one;;parent of i:  ⌊i/2⌋@the floor of i over two;;from 0:  2i + 1  and  2i + 2@counted from zero"
Counting positions from one, the children of i sit at two i and two i plus one, and the parent at the floor of i over two. Counted from zero, which is how the lab draws it, the children are at two i plus one and two i plus two. Same tree.

@math heading="Insert 1, 9, 2, 8, 3, 7, 4, 6" items="array:  1  3  2  6  8  7  4  9@the array reads;;paths:  1 3 6 9 · 1 3 8 · 1 2 7 · 1 2 4@every path"
Insert one, nine, two, eight, three, seven, four, six, and the array reads one, three, two, six, eight, seven, four, nine. Every path down increases. But three comes before two. It's a valid heap, and it isn't sorted.

@chapter Insert: sift up
@art sift-up
To insert, put the new key in the first free slot, so the tree stays complete. Then, while it's smaller than its parent, swap them. Each swap fixes one level, so it's at most the floor of log two of n comparisons.

@math heading="Insert 8 into 1, 9, 2" items="8 < 9:  swap@against its parent nine;;8 > 1:  stop@against one;;2 comparisons, 1 swap · bound ⌊log₂ 4⌋ = 2@two comparisons"
Insert eight into the heap one, nine, two. Compare eight against its parent nine, and swap. Compare against one, and stop. That's two comparisons and one swap, against a bound of two. Inserting seven a step later costs one comparison and no swap.

@chapter Extract-min: sift down
@art sift-down
The root is the answer. To remove it, move the last element into the root, then push it down. Compare the two children with each other, then compare it with the smaller one, and swap if it's bigger. Two comparisons per level.

@math heading="Extract 1 from 1 3 2 6 8 7 4 9" items="9 to root:  9 3 2 6 8 7 4@Move nine;;smaller child 2, swap:  2 3 9 6 8 7 4@smaller is two;;smaller child 4, swap:  2 3 4 6 8 7 9@smaller is four;;4 comparisons · bound 2⌊log₂ 7⌋ = 4@four comparisons"
Move nine to the root. Its children are three and two, the smaller is two, so swap. Now its children are seven and four, the smaller is four, swap again. Four comparisons, two swaps, against a bound of four. It reached a leaf, the worst case at that size.

@words text="The lab shows the walk, not the proof"
Over the lab's ten operations, every step stays under its bound. But the proof is one line. A complete tree on n nodes has height floor of log two of n, and a sift visits each level once.

@art tree-height
That height is the whole bound. Insert climbs one path, with at most one comparison per level. Extract min walks down one path, with two comparisons per level. So insert costs at most log n, and extract at most twice that.

@chapter Where people slip
@list heading="Common slips" items="Expecting the array to be in order@The first|Swapping without comparing the children@The second|Mixing the two index conventions@And the third"
The first slip is expecting the array to be in order. Only paths down are ordered. The second is sifting down without comparing the two children first, which breaks the rule on the other edge. And the third is applying the count from one formula to an array counted from zero, which sends you to a cousin.

@art wrong-child
Swap with a child that isn't the smaller one, and that child's sibling ends up below something bigger than itself. Find the smaller child first. That's where the factor of two comes from.

@chapter Try it
@words text="Extract again from 2 3 4 6 8 7 9" sub="the lab counts 4 comparisons"
Your turn. From two, three, four, six, eight, seven, nine, extract the minimum again. Move the last key up, sift it down, and count your comparisons. The lab gets four.

@end text="Sift it yourself"
You can insert and extract, and watch the array and the tree side by side, on Learn. That's learn dot get er done dot I O.
