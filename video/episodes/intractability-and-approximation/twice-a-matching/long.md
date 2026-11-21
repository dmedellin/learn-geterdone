---
format: long
lesson: intractability-and-approximation/twice-a-matching
title: The 2-approximation for vertex cover, proved with four numbers
thumb: Matching ≤ optimum ≤ cover
---

@chapter A guarantee without the optimum
@title text="Twice a Matching" sub="Intractability and Approximation" art=thumb
How can an algorithm promise to be within twice the optimum, when it doesn't know the optimum? Because the promise is proved against something it can see: a lower bound. A guarantee can't be a claim about the optimum directly, because computing the optimum is the whole problem.

@chapter The algorithm
@art greedy-matching
Scan the edges in order. Keep an edge whenever neither of its ends has been used yet. That's a maximal matching: edges sharing no vertex, where no further edge can be added. Then return every endpoint of every kept edge as the cover.

@art both-ends
Why is that a cover? If some edge had neither end chosen, neither end was used by a matched edge, so it could have been added. That contradicts maximality. Maximal is enough. It doesn't need to be a maximum matching.

@chapter The proof in one line
@math heading="The chain" items="matching ≤ optimum@at most the optimum;;cover = 2 × matching@exactly twice;;so cover ≤ 2 × optimum@twice the optimum"
The matched edges share no vertex, so any cover needs a different vertex for each one. So the matching is at most the optimum. And the cover is exactly twice the matching, since disjoint edges have distinct ends. So the cover is at most twice the optimum.

@words text="the optimum appears only in the middle"
Look at where the optimum appears. Only in the middle inequality, the one nobody has to evaluate. The algorithm computes the matching and the cover. That's the shape of every approximation guarantee in this course.

@chapter Three disjoint edges
@art disjoint-edges
Now put numbers on that chain. The panel draws all four of them on one axis, rather than just two.

@math heading="1–2, 3–4, 5–6" items="matching 3@matching takes all three;;optimum 3@optimum is three;;cover built 6@the cover;;ratio 6/3 = 2@exactly two"
The loaded graph is three separate edges, one two, three four, and five six. The matching takes all three. The optimum is three, one end of each edge. The cover takes all six vertices. So the ratio is exactly two, the promise attained.

@art four-number-line
This is the worst the algorithm can do, and it isn't a strange graph. Each matched edge needs one vertex in a cover, and the algorithm takes two. The optimum here came from exhaustive search. Without it, the ratio would have an invented denominator.

@chapter Every graph of a size
@art sweep-grid
One graph proves nothing about the worst case.

@words text="63 graphs on 4 vertices" sub="worst ratio 2, attained by 49"
Then the panel goes further. It enumerates all sixty three non empty graphs on four vertices, solves each exactly, runs the approximation on each, and reports the worst ratio. It's two, attained by forty nine of them, from a single edge up to one with five edges. The panel names both, so nobody concludes the bound is an artefact of one degenerate case.

@list heading="Other graphs" items="Five-cycle:  cover 4, optimum 3, ratio 4/3@five cycle|Two triangles:  ratio 1@two triangles"
On the five cycle, the matching takes two edges, the cover has four vertices, the optimum is three, so four thirds. On two triangles, the ratio is one. Neither number is the algorithm's number. The matching is greedy in edge order, so the sweep's worst is this implementation's worst. The proof never mentioned the order, so it covers them all.

@chapter Should you approximate here?
@art bipartite
Here's an irony. The default graph is bipartite. And Koenig's theorem, proved from max flow in the graph course, says a bipartite graph's minimum cover equals its maximum matching, both computable in polynomial time. So on the very instance where the guarantee is attained, an exact algorithm gives three where the approximation gives six.

@words text="bipartite · bounded degree · a tree" sub="exactly solvable special cases"
Bounded degree and tree shapes make the problem polynomial too. Knowing which special cases are exactly solvable is part of knowing when to approximate at all.

@chapter Where people slip
@list heading="Common slips" items="Reading a guarantee as about the optimum@The first|Quoting one ratio as the algorithm's@The second|Approximating where exact is cheap@And the third"
The first slip is reading a guarantee as a statement about the optimum. Ask which computable quantity it's proved against. The second is quoting one instance's ratio as the algorithm's ratio. And the third is approximating when the instance is exactly solvable: bipartite, bounded degree, or a tree.

@end text="Matching, optimum, cover"
See all four numbers on one axis, and sweep every graph of a size, on Learn. That's learn dot get er done dot I O.
