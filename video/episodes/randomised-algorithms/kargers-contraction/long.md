---
format: long
lesson: randomised-algorithms/kargers-contraction
title: Karger's algorithm: finding a minimum cut by random contraction
thumb: Contract until two remain
---

@chapter The algorithm
@title text="Karger's Contraction" sub="Randomised Algorithms" art=thumb
Here's a minimum cut algorithm you can explain in one breath. Pick a random edge, merge its ends, repeat. It's sometimes wrong, and you can say exactly how often.

@art contract-edge
To contract an edge, merge its two endpoints into one supernode. Every other edge at either end now points at the supernode. Edges that became loops are deleted. Parallel edges are kept.

@art shrinking-graph
Karger's algorithm contracts a uniformly random edge, again and again, until two supernodes remain. Then it returns the edges between them.

@art two-supernodes
Those two supernodes split the vertices in two, so that's always a cut. It just isn't always a minimum cut. The running time is fixed, and the answer is sometimes wrong. That's a Monte Carlo algorithm.

@chapter Why small cuts survive
@words text="min cut k  ⟹  every degree ≥ k  ⟹  |E| ≥ nk/2"
Say the minimum cut has k edges. Then every vertex has degree at least k, or its own edges would be a smaller cut. So there are at least n k over two edges.

@math heading="One contraction" items="P(hit the cut) ≤ k / (nk/2) = 2/n@two over n;;P(miss) ≥ 1 − 2/n@one minus"
A random edge lands in the cut with probability at most k over n k over two, which is two over n. So the first contraction misses the cut with probability at least one minus two over n.

@art parallel-edges
And contraction can't create a smaller cut. It only loses sight of one. If the cut is missed, it's still a minimum cut of the smaller graph. Parallel edges are counted separately, and that's the point. A pair joined by many edges is likely to be merged, and merging them is harmless.

@chapter The guarantee
@math heading="All the way down" items="∏ (1 − 2/i),  i = n … 3@the product;;= 2 / (n(n − 1))@telescopes;;n = 6:  1/15@one fifteenth"
Repeat that for every step, and the chance of missing the cut every time is the product of one minus two over i, for i from n down to three. That telescopes to two over n times n minus one. At six vertices, one fifteenth, about point zero six seven.

@art two-supernodes
And if no edge of the cut is ever contracted, each supernode sits wholly on one side, so the last two supernodes are exactly the two sides. That's a guarantee for every six vertex graph, and it's very far from what happens on any particular one.

@chapter The exact answer
@art two-triangles
The lab doesn't sample. Its opening graph is two triangles joined by two edges. Six vertices, eight edges. It computes the exact probability by recursion over contraction states, memoised, so it's a few dozen states instead of every edge order.

@math heading="Three minimum cuts of size 2" items="isolate vertex 3:  13/70@vertex three;;isolate vertex 6:  13/70@vertex six;;split the triangles:  6/35@splitting the triangles;;any of them:  19/35 ≈ 0.543@any of them"
Searching all thirty one bipartitions finds a minimum cut of two edges, and three cuts achieve it. Isolating vertex three, thirteen seventieths. Isolating vertex six, the same. Splitting the triangles, six thirty fifths. Returning any of them: nineteen thirty fifths, about point five four three. Every one clears the bound of one fifteenth.

@words text="one cut ≠ any cut"
Notice the cut the graph was built to show, the two joining edges, is the least likely of the three. And the bound is about one named cut. Success is about any of them, so you add them up.

@chapter The seeds that missed
@words text="67 of 120 seeds succeeded" sub="53 failed · seed 5 returned a cut of 3"
Over a hundred and twenty seeds, it found a minimum cut sixty seven times, against an exact probability of nineteen thirty fifths. Fifty three seeds failed, and the panel names them. Seed five is the first: it returned a cut of three edges, not two. That's what with high probability looks like.

@art four-cycle
For contrast, a four cycle has six minimum cuts, each with probability exactly one sixth, which matches the bound at n equals four. They add up to one, so the algorithm never fails there.

@chapter Where people slip
@list heading="Common slips" items="Quoting one cut's survival as success@The first|Folding parallel edges into one@The second|Reading a probable bound as always@And the third"
The first slip is quoting one cut's survival as the success probability. Six thirty fifths against nineteen thirty fifths. The second is folding parallel edges into one, which changes the probabilities. And the third is reading a with high probability bound as always. The fix is repetition, and the next lesson prices it.

@end text="Contract until two remain"
Step through a contraction and see which seeds missed, on Learn. That's learn dot get er done dot I O.
