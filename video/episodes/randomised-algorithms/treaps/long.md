---
format: long
lesson: randomised-algorithms/treaps
title: Treaps: a search tree whose shape the input can't control
thumb: Random priorities, one tree
---

@chapter The shape problem
@title text="Treaps" sub="Randomised Algorithms" art=thumb
A binary search tree's shape is decided by the order keys arrive in, and the tree doesn't control that. Twelve keys in sorted order give a path of height eleven. A treap takes that power away from the input.

@art sorted-path
Balanced trees fix it with a rule, enforced on every insertion. A treap fixes it differently. It makes the shape depend on coins, instead of on the arrival order.

@chapter Two orders at once
@art key-priority
Each node holds a key and a random priority. The tree is a search tree on the keys: smaller keys to the left, larger to the right. And it's a heap on the priorities: every node's priority is smaller than its children's.

@chapter Only one tree
@art unique-root
With distinct keys and distinct priorities, exactly one such tree exists. The smallest priority must be at the root, because anywhere else it would sit under a larger one. Then the search order forces every smaller key left, and every larger key right. Apply the same argument to each side, and there's nothing left to choose.

@words text="insertion order changes the rotations, not the tree"
So the insertion order can't change the tree. Only the priorities can. The lab builds it twice, from sorted and shuffled orders, and compares the two node for node. Priorities are ranked so no two can tie. A tie would leave the shape undecided, for a reason that has nothing to do with treaps.

@chapter Twelve keys
@math heading="Keys 10 … 120" items="priority 1 belongs to 30  ⟹  root 30@priority one;;sorted order: 8 rotations · shuffled: 11@eight rotations;;treap height 5, mean depth 5/2@height five;;plain tree: height 11, mean depth 11/2@plain search tree"
The keys are ten, twenty, up to a hundred and twenty. Priority one belongs to thirty, so thirty is the root. Inserting in sorted order costs eight rotations, and shuffled costs eleven. Both give the same tree, height five, mean depth five halves. A plain search tree on the sorted order has height eleven and mean depth eleven halves.

@art two-builds
Different work, identical result. And it got there with no rule about heights at all. The only thing maintained is heap order on twelve numbers the structure made up itself.

@chapter Insertion
@art rotate-up
To insert, give the key a random priority and place it as a leaf, the ordinary way. Then rotate it upward while its priority is smaller than its parent's. A rotation preserves the search order, so the loop stops exactly when heap order is restored.

@words text="no stored height · no balance factor · no cases"
That's the whole implementation. No height is stored, no balance factor, no four case analysis. Deletion is the reverse: rotate the node down until it's a leaf, then remove it.

@chapter What's guaranteed
@art unique-root
A treap has the shape of a randomly built search tree, so its expected mean depth is about two times the natural log of n, and its height is order log n.

@words text="2 ln n = 4.970" sub="counted mean depth 2.500 · height 5"
That's stated, not proved, in this library. At twelve keys, two natural log n reads four point nine seven, while the counted mean depth is two point five, and the height is five. An asymptote, an exact mean, and a count. Three numbers with three meanings. Reading them as estimates of each other is the trap here.

@art height-spread
And it's in expectation, not always. Over seeds one to twelve, the height came out five, six, four, five, five, six, six, five, five, four, six, five. Never eleven, never three. The input can be chosen by an adversary, but the coins belong to the structure. A random pivot and universal hashing make the same trade.

@chapter Where people slip
@list heading="Common slips" items="Expecting insertion order to matter@The first|Reading 2 ln n as the depth@The second|Expecting a height bound@And the third"
The first slip is expecting the insertion order to matter. It changes the rotations, and nothing else. The second is reading two natural log n as this tree's depth. And the third is expecting a height bound. There isn't one. A treap can be a path, just very unlikely. If you need a bound that always holds, use an AVL tree.

@end text="Random priorities, one tree"
Change the insertion order and the priority seed, and see which one moves the tree, on Learn. That's learn dot get er done dot I O.
