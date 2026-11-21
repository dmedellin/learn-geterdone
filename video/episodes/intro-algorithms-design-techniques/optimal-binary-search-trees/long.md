---
format: long
lesson: intro-algorithms-design-techniques/optimal-binary-search-trees
title: Optimal binary search trees by dynamic programming
thumb: Likeliest key isn't the root
---

@chapter Two shortcuts that fail
@title text="Optimal Binary Search Trees" sub="Introduction to Algorithms, Section 15.5" art=thumb
If you know how often each key will be searched for, what's the best binary search tree? The obvious answers are wrong.

@quote text="This example shows that an optimal binary search tree is not necessarily a tree whose overall height is smallest." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 15.5"
The authors say it early. This example shows that an optimal binary search tree is not necessarily a tree whose overall height is smallest. And putting the most probable key at the root doesn't work either.

@chapter The model
@art word-lookup
Picture a translation program looking up every word of a text in a search tree. Frequent words should sit near the root. And some words of the text aren't in the tree at all.

@art dummy-leaves
So each key has a search probability, p i, and between and around the keys sit dummy leaves, with probabilities q i, for the unsuccessful searches. Every search ends at a key or a dummy, and all the probabilities sum to one.

@math heading="Expected search cost" items="Σ (depth(kᵢ) + 1)·pᵢ + Σ (depth(dᵢ) + 1)·qᵢ@the sum over keys"
A search costs the depth of the node it ends at, plus one. So the expected cost is the sum over keys of depth plus one times p, plus the sum over dummies of depth plus one times q. The optimal tree minimizes that.

@chapter Ranges and roots
@art range-subtree
Every subtree holds a contiguous range of keys, k i to k j, with the dummies around them as its leaves. And by cut and paste, an optimal tree's subtrees are optimal for their ranges.

@art root-choice
So try every key in the range as the root. A root at an end of the range has an empty subtree on that side, which by convention holds a single dummy.

@art push-down
When a subtree hangs under a new root, every node in it moves one level deeper. So its expected cost rises by exactly its total probability, its weight. Add the root's own probability, and the extra is the weight of the whole range.

@math heading="The recurrence" items="e[i, i − 1] = qᵢ₋₁@an empty range;;e[i, j] = min over r of e[i, r − 1] + e[r + 1, j] + w(i, j)@the minimum over r"
So e of an empty range is just its dummy's probability. And e of i j is the minimum over r of the left cost, plus the right cost, plus the weight of the range. Fill it by range length, like the matrix chain, in theta of n cubed.

@chapter A four-key example
@math heading="In fortieths" items="p = 7, 6, 5, 10@p is seven;;q = 3, 2, 2, 2, 3@q is three;;e[1, 4] = 95/40 = 19/8 = 2.375@ninety five fortieths;;root k₂@k two"
Here's an instance in fortieths. p is seven, six, five and ten, so key four is the likeliest. q is three, two, two, two, three. The table's answer is ninety five fortieths, nineteen eighths, two point three seven five. And the root is k two.

@art likely-key-root
k two sits at the root, k one to its left, and k four to its right with k three below it. The likeliest key is one level down. The best tree with k four at the root costs a hundred fortieths, two point five. Three keys and four dummies lie to its left, and a root at the end pushes them all down.

@words text="Three keys: root is the least likely" sub="the dummies carry the weight · 47/20"
In another example with three keys, the optimal root is k two, the least likely key, at cost forty seven twentieths. The dummies carry the weight there, nearly half of all searches.

@chapter Checking by brute force
@words text="7 equal keys: 1 cheapest of 429" sub="8 keys: 1,430 trees, too many to list"
The lab checks the table against every tree, up to seven keys. Seven equally likely keys give the perfectly balanced tree, the only cheapest of four hundred and twenty nine. At eight keys, the table answers, but listing one thousand four hundred and thirty trees is declined. The table is right at every n because of the cut and paste argument.

@chapter Common slips
@list heading="Common slips" items="Putting the likeliest key at the root@The first|Leaving out the unsuccessful searches@The second|Forgetting the weight term@the third"
The first slip is putting the likeliest key at the root. The second is leaving out the unsuccessful searches. Without them, the tree favours the keys wrongly. And the third is forgetting the weight term, which computes the cost of a forest, not a tree.

@chapter Try it
@words text="k₃ at the root" sub="k₁ above k₂ on the left · k₄ on the right"
Your turn. For the four key instance, compute by hand the expected cost of the tree with k three at the root, k one and k two on its left with k one above, and k four on its right. Which root beats it, and by how many fortieths?

@end text="Check against every tree"
You can fill the table on your own probabilities and check it against every tree, on Learn. That's learn dot get er done dot I O.
