---
format: long
lesson: data-structures/union-find
title: Union-find: why linking the right way round is everything
thumb: Depth 11 or depth 1
---

@chapter The question
@title text="Union–Find" sub="Data Structures" art=thumb
You've got twelve elements and a stream of merge this set with that one, and are these two together? There's a structure for exactly that. Build it carelessly and a lookup walks eleven pointers. Build it with one small rule and it walks one.

@chapter Sets as trees
@art forest
Each set is a rooted tree. Every element has a parent pointer, and the root is the set's name. Find of x walks parent pointers up to the root. Union of x and y finds both roots, and if they differ, makes one the parent of the other.

@words text="cost of find = depth of x"
So find costs the number of pointers walked, which is the depth of x. Everything about how fast this is comes down to how deep the trees get.

@art same-set
To test whether two elements are together, find both roots. Same root, same set. That's the only question it answers. It can't even tell you what's in a set.

@chapter The naive way
@art chain
The naive version links the first root under the second. Now run union of zero and one, one and two, and so on up to ten and eleven. Each union hangs the growing tree under a fresh single node. The result is a path of twelve.

@math heading="Twelve finds on the path" items="11 + 10 + … + 0 = 66 hops@sixty six;;worst find:  11@eleven"
The twelve finds afterwards walk eleven, plus ten, down to zero. That's sixty six pointers, and the deepest find walks eleven.

@chapter Union by rank
@art link-by-rank
Here's the fix. Every root carries a rank, starting at zero. On a union, the root with smaller rank goes under the one with larger rank. If they're equal, pick either, and the new root's rank goes up by one. That's two comparisons, and it costs nothing.

@art doubling
Why does that help? Look at when rank grows. Only when two trees of equal rank merge, and then the merged tree is at least twice as big as either.

@math heading="Rank r ⟹ at least 2ʳ elements" items="rank 0:  a single element,  2⁰ = 1@rank zero;;rank r from two rank r − 1 roots:  2ʳ⁻¹ + 2ʳ⁻¹ = 2ʳ@only by merging;;2ʳ ≤ n  ⟹  r ≤ log₂ n@with n elements"
Now the induction. A rank zero root is a single element, and two to the zero is one. A root reaches rank r only by merging two roots of rank r minus one, each with at least two to the r minus one elements, so together, two to the r. And with n elements in total, r can't exceed log two of n.

@words text="The bound is a fact about the rule"
Rank bounds height, so every find walks at most log n pointers. But notice where the doubling came from. The clause only by merging two equal ranks. The naive union has no such clause, so the bound simply doesn't hold for it.

@chapter Four ways, measured
@math heading="n = 12, chain of unions, then 12 finds" items="neither:  66 hops,  worst 11,  bound needs 2048  ✗@neither rule;;union by rank:  20 hops,  worst 1  ✓@union by rank;;compression only:  21 hops,  worst 11  ✗@compression only;;both:  20 hops,  worst 1  ✓@both rules"
With neither rule, sixty six hops, worst find eleven. A tree that deep would need two thousand and forty eight elements, and there are twelve. With union by rank, twenty hops, worst find one. Compression only, twenty one, but the worst is still eleven. And both rules, twenty.

@art compress
Path compression works during find. Once you reach the root, point every node on the path straight at it. On the chain, the first find walks eleven and flattens everything, so the other eleven cost one each. But it repairs. It doesn't prevent. The first find still paid in full.

@words text="pair, then pair the pairs" sub="neither: 39 hops, depth 4 · rank: tallest rank 3, bound holds"
A gentler pattern: pair them up, then pair the pairs. With neither rule, thirty nine hops and depth four, whose bound of sixteen already exceeds twelve elements. With union by rank, the tallest rank is three, the bound is eight, and it holds. Both rules together, thirty hops.

@chapter What's proved
@words text="O(m α(n)) with both rules" sub="stated here, not proved"
With both rules, m operations cost order m times alpha of n, the inverse Ackermann function, which is at most four for any n you'll ever write down. That's stated on this course, not proved. The log n bound from union by rank is what's proved, and it's the one later courses use.

@chapter Where people slip
@list heading="Common slips" items="Linking roots without comparing ranks@The first|Expecting compression to fix a tall tree@The second|Quoting the near-constant bound as proved@And the third"
The first slip is linking roots without comparing ranks, which builds paths and loses the bound itself. The second is expecting path compression to fix a tree that's already tall. And the third is quoting the near constant bound as something proved here.

@chapter Try it
@words text="union(i, i+1) for i = 0 … 10" sub="run it under each pair of rules"
Your turn. Run the eleven chain unions under each combination of the two rules, and count the hops for twelve finds. Then write out the induction for why rank r means at least two to the r elements.

@end text="Link it both ways"
You can run union and find with each rule switched on or off, on Learn. That's learn dot get er done dot I O.
