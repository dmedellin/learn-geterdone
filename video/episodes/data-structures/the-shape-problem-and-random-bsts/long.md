---
format: long
lesson: data-structures/the-shape-problem-and-random-bsts
title: Same 15 keys, height 14 or height 3: the shape problem
thumb: The order decides the shape
---

@chapter The question
@title text="The Shape Problem and Random BSTs" sub="Data Structures" art=thumb
How tall is a search tree built from these fifteen keys? It's a trick question. The keys don't decide. The order they arrive in does.

@chapter The order fixes the tree
@art insert-walk
Insertion has no choices. Each new key walks down to the one empty spot where a search for it would have failed. So the tree is a function of the sequence. Same keys, different order, different tree.

@art sorted-path
Insert ten, twenty, thirty, up to a hundred and fifty. Every key is bigger than everything already there, so each one becomes the right child of the last. A path of height fourteen, on fifteen keys. Reversed input does the same thing to the left.

@words text="Sorted is the common case" sub="dumps by primary key · logs by timestamp · incrementing IDs"
And sorted isn't rare. A database dump ordered by primary key, a log replayed by timestamp, an ID that increments. The worst case for this structure is one of the most common inputs there is.

@chapter Four orders, one key set
@math heading="n = 15,  keys 10 20 … 150" items="sorted:  height 14,  mean depth 7,  105 comparisons@sorted;;reversed:  height 14,  mean depth 7,  105@reversed;;shuffled:  height 6,  mean depth 44/15,  44@A shuffle;;bisect:  height 3,  mean depth 34/15,  34@middle first"
Here are four orders. Sorted: height fourteen, mean depth seven, a hundred and five comparisons to build. Reversed: the same. A shuffle: height six, mean depth forty four fifteenths, forty four comparisons. And middle first, then the middle of each half: height three, thirty four comparisons.

@art three-trees
Height three is the floor of log two of fifteen, the shortest a fifteen node tree can be. But it's useless as a strategy. To insert middle first, you need all the keys in order already, which means you've sorted them.

@chapter Three different numbers
@words text="2 ln 15 = 5.416" sub="asymptotic · not counted"
Now one number that wasn't counted. Two times the natural log of n is the asymptotic expected depth of a node, in a tree built from a uniformly random order. At fifteen it's five point four one six.

@list heading="Three quantities" items="Height: the longest path@Height|Mean depth: average over the nodes@mean depth|2 ln n: a limit of an average over orders@two ln n"
So there are three different quantities on screen. Height is the longest path, what a worst case search costs. Mean depth is the average over the nodes, what a search for a random key costs. And two ln n is a formula about a limit of an average over orders.

@art depth-bands
Think of the bands as levels. Height counts down to the deepest one. Mean depth averages every node's level, and in a bushy tree most nodes sit low, so the mean is well under the height. In the shuffled tree, the two differ by a factor of two.

@words text="shuffle: height 6 · mean depth ≈ 2.93" sub="2 ln 15 ≈ 85% above"
They don't agree. The shuffled tree has height six and mean depth about two point nine three. The asymptote is about eighty five percent above that, which is what an asymptotic formula does at small n.

@chapter Random order, on average
@art random-root
Here's the theorem, stated but not proved here. Insert n distinct keys in a uniformly random order, and the expected height is order log n. The recurrence behind it comes from picking a random root and recursing on both sides. It's the same recurrence randomised quicksort solves, because a random pivot and a random root are the same object.

@art online-stream
But a shuffle needs every key before you insert any of them. If keys arrive one at a time from a sorted stream, there's nothing to shuffle, and the tree degenerates as it grows. So the fix is to enforce a shape on every insert, which is where rotations come in.

@chapter Where people slip
@list heading="Common slips" items="Blaming the keys for the shape@The first|Reading 2 ln n as the height@The second|Taking one shuffle as the theorem@And the third"
The first slip is blaming the keys. The real question is whether they arrived sorted. The second is reading two ln n as the height. And the third is taking one shuffle as evidence for the theorem. A different seed gives a different height, and the theorem is about the average over all n factorial orders.

@chapter Try it
@words text="Keys 10 20 … 150" sub="one order that degenerates · one that balances"
Your turn. For the keys ten to a hundred and fifty, write one order that builds a path, and one that builds height three. Predict each height before you check it. Then work out each tree's mean depth, as a fraction over fifteen.

@end text="Shuffle the keys yourself"
You can try your own insertion orders and watch the height change, on Learn. That's learn dot get er done dot I O.
