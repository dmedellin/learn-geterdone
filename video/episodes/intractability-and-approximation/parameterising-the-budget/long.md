---
format: long
lesson: intractability-and-approximation/parameterising-the-budget
title: Vertex cover in 2ᵏ time: putting the exponential on the budget
thumb: Exponential in k, not n
---

@chapter Move the exponential
@title text="Parameterising the Budget" sub="Intractability and Approximation" art=thumb
An exponential running time doesn't have to be exponential in the size of the input. For vertex cover, you can make it exponential only in the size of the answer you're looking for.

@words text="Is there a vertex cover of size ≤ k?" sub="the parameter is k"
Here's the question. Does a graph have a vertex cover with at most k vertices? The parameter is k, chosen by whoever asks. The running time may depend on k in any way at all, as long as it's polynomial in the graph.

@chapter One end or the other
@art edge-branch
Take any edge with both ends still uncovered. Every cover must contain one of its two ends, because nothing else touches that edge. There's no third option. So branch: put u in the cover, or put v in. Each branch spends one unit of the budget.

@art bounded-tree
After k levels the budget is gone. If an uncovered edge remains, that branch fails. If none does, it has a cover. The depth of the tree is the budget, not the graph. So there are at most two to the k plus one nodes, and each one just scans for an uncovered edge.

@words text="O(2ᵏ · m)"
That's order two to the k times the number of edges. The graph's size only enters through the scan.

@chapter The six-cycle
@art six-cycle
The lab loads the cycle on six vertices, with k equals three. It finds the cover one, three, five. The exhaustive optimum is three, so the answer's right. It opened nine nodes, against a tree bound of sixteen. And two to the k times n is forty eight, against two to the n, sixty four. Parameterising wins, narrowly.

@math heading="Lowering the budget" items="k = 0:  fails in 1 node@k equals zero;;k = 1:  fails in 3@k equals one;;k = 2:  fails in 7, bound 8@k equals two;;k = 3:  succeeds in 9, bound 16@k equals three"
Move the budget down. At k equals zero, it fails in one node. At k equals one, in three. At k equals two, it fails in seven, against a bound of eight, nearly the whole tree, because with no cover the tree is explored in full. At k equals three, it succeeds in nine against sixteen, because it stops at the first cover.

@chapter Where it pays
@art star
Load the star on eight vertices with k equals one. The hub covers every edge. Three nodes, against two to the k times n equal to sixteen, and two to the n equal to two hundred and fifty six. A star with forty leaves would open the same three nodes. That's an argument, not a measurement, since the parser stops at eight.

@chapter Where it doesn't
@art two-triangles
Now two separate triangles, with k equals four. Each triangle needs two vertices, so four is the smallest budget that works, and that's large next to six vertices.

@art two-curves
So which wins, two to the k times n, or two to the n? It depends where k sits.

@math heading="Two triangles, k = 4" items="2ᵏ · n = 16 × 6 = 96@ninety six;;2ⁿ = 64@sixty four;;nodes opened: 9@nine nodes"
Two to the k times n is ninety six, and two to the n is sixty four. The parameterised bound is worse than checking every subset. The search itself still opens only nine nodes. That's the measurement. The other two are expressions evaluated at this instance, and one of them is losing.

@words text="f(k) · poly(n)" sub="fixed-parameter tractable: a shape, not a speed"
A problem is fixed parameter tractable when it runs in some function of k, times a polynomial in the input. That doesn't say fast. The function can be monstrous. It says the exponential has moved onto a quantity that may be small in practice. Shrinking the graph first, called kernelisation, is the other half, and this course names it without building it.

@chapter Where people slip
@list heading="Common slips" items="Reading fixed-parameter tractable as fast@The first|Quoting 2ᵏ · n as work done@The second|Choosing a parameter without checking it's small@And the third"
The first slip is reading fixed parameter tractable as fast. The second is quoting two to the k times n as work done. On the six cycle it's forty eight, and nine nodes were opened. And the third is choosing a parameter without checking it's small on your instances.

@end text="Exponential in k, not n"
Move the budget and watch the tree on Learn. That's learn dot get er done dot I O.
