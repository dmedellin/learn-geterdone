---
format: long
lesson: intro-algorithms-advanced-structures/decrease-key-and-the-degree-bound
title: Cascading cuts, and where the Fibonacci in Fibonacci heaps comes from
thumb: Lose two children, get cut
---

@chapter The open question
@title text="Decreasing a Key and Bounding the Degree" sub="Introduction to Algorithms, Sections 19.3–19.4" art=thumb
The last lesson left two loose ends. Why does the potential count each marked node twice? And why should any node's degree be small?

@chapter Decreasing a key
@art cut-to-root
Lower a node's key. If it's a root, or the new key is still at least its parent's, nothing is broken and nothing moves. Otherwise, the node is cut. It leaves its parent's child list, with its whole subtree, and joins the root list as a new, unmarked tree.

@words text="70 → 65: nothing moves · 70 → 5: cut" sub="70's parent is 60"
On the lab's tree, decreasing seventy to sixty five moves nothing, since sixty five is still above its parent, sixty. Decreasing it to five cuts it.

@chapter Marks and cascading cuts
@art mark-flag
After the cut, the parent may be in trouble. A mark records that a node has lost one child since it was last made a child. If the parent was unmarked, it's marked now. If it was already marked, this is its second loss, and it's cut too.

@art cascade-chain
Then the same test runs on its parent, and so on up. The chain of cascading cuts climbs until it reaches a root, or an unmarked node.

@math heading="two-cascades" items="mark 160, 140, 100@marks one sixty;;decrease 160: cut 160, then 140, then 100@then decreases one sixty;;stops at root 20 · 6 cuts, 2 cascading@stopping at the root"
In the lab's two cascades example, it first marks one sixty, one forty and one hundred, by cutting one child from each. It then decreases one sixty itself. One sixty is cut, then its marked parent one forty, then one hundred, stopping at the root, twenty. Six cuts in all, two cascading.

@chapter Why it's still cheap
@quote text="One unit of potential pays for the cut and the clearing of the mark bit, and the other unit compensates for the unit increase in potential due to node y becoming a root." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 19.3"
Here's why marks count double. In the authors' words: one unit of potential pays for the cut and the clearing of the mark bit, and the other unit compensates for the unit increase in potential due to node y becoming a root.

@math heading="One call with c cascading-cut calls" items="actual cost: 1 + c@costs one plus c;;ΔΦ ≤ c + 2·(2 − c) = 4 − c@the potential rises;;amortized ≤ 5@at most five"
In the lab's units, a call with c cascading cut calls costs one plus c. The potential rises by at most c plus two times two minus c, which is four minus c. So any decrease key costs at most five amortized, however long its cascade.

@words text="Delete = decrease to −∞, then extract-min" sub="O(1) + O(D(n)) amortized"
Delete is then easy. Decrease the key to minus infinity, and extract the minimum. That's O of one plus O of D of n.

@chapter The degree bound
@art children-in-order
Now the bound. List a node's children in the order they were linked. When the i th child was linked, the node already had i minus one children, and consolidate links only equal degrees. Since then that child can have lost at most one child. So its degree is at least i minus two.

@math heading="Lemma 19.4 and Corollary 19.5" items="size(x) ≥ F(k + 2) ≥ φᵏ@at least F of k plus two;;φ = (1 + √5)/2 ≈ 1.618@phi is;;degree ≤ ⌊log_φ n⌋@so every degree"
Add up the smallest possible subtrees, and a node of degree k has at least F of k plus two nodes, a Fibonacci number, which is at least phi to the k. Phi is one plus the square root of five, over two, about one point six one eight. So every degree is at most the floor of log base phi of n.

@art degree-bound-curve
Since n is at least phi to the k, a degree can only grow like a logarithm of n. So D of n is O of log n, the bound the last lesson's analysis assumed.

@art fibonacci-vs-binomial
Consolidation alone builds binomial trees, with two to the k nodes at degree k. Cuts let a node fall below that, and the marks stop the fall at the Fibonacci row: one, two, three, five, eight, thirteen. That row gives the structure its name.

@chapter Where people slip
@list heading="Common slips" items="Cutting on every decrease@The first|Fearing long cascades@The second|Assuming binomial trees@the third"
The first slip is cutting every node whose key is decreased. Only a broken heap order causes a cut. The second is fearing long cascades. Every node they cut was marked and prepaid. And the third is assuming every tree is binomial. Cuts break that shape.

@chapter Try it
@words text="decrease 130 9 · 150 8 · 160 7" sub="what is cut? what is marked?"
Your turn. Start from the lab's sixteen node tree and run decrease one thirty to nine, one fifty to eight, and one sixty to seven. Say what's cut and marked each time, and find a node whose size equals F of k plus two exactly.

@end text="Watch the cascade"
You can count cuts, marks, and the lemma at every node, on Learn. That's learn dot get er done dot I O.
