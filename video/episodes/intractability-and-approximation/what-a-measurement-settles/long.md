---
format: long
lesson: intractability-and-approximation/what-a-measurement-settles
title: One graph, every graph of a size, every graph: what each number proves
thumb: A count is not a bound
---

@chapter Three numbers, one algorithm
@title text="What a Measurement Settles" sub="Intractability and Approximation" art=thumb
One algorithm, three numbers: four thirds, two, and two. Only one of them is a theorem. Telling them apart is the skill this whole course has been training, and here it's met one last time, where it matters most.

@art five-cycle-cover
Start on the five cycle. The 2 approximation for vertex cover takes a maximal matching of two edges and covers with their four endpoints. The optimum is three. So the realised ratio is four thirds, against a promise of two. Everything in that sentence is measured, except the promise.

@chapter Three rungs
@list heading="Three claims" items="On this graph:  ratio 4/3@On this graph|Every graph on 4 vertices:  63, each solved, worst 2@every graph with four|Every graph, every size:  proved, at most 2@every size"
On this graph, four thirds. On every graph with four vertices, sixty three of them, each solved exactly, the worst is two. And on every graph of every size, the proof gives at most two.

@art edge-subsets
The middle claim isn't a sample. Four vertices have six possible edges, so there are two to the six minus one, sixty three non empty graphs. Every one is solved exactly. That's a genuine universal statement over a finite set, and forty nine of the sixty three hit the worst ratio of two.

@chapter Still not the theorem
@art growing-sizes
So sweep more sizes. The panel caps the size, and the next one up is already refused.

@math heading="Exhaustive sweeps" items="3 vertices:  7 graphs, worst 2@three vertices;;4 vertices:  63 graphs, worst 2@four vertices;;5 vertices:  1023 graphs, worst 2@five vertices"
Three vertices, seven graphs, worst two. Four vertices, sixty three graphs, worst two. Five vertices, a thousand and twenty three graphs, worst two. Three exhaustive answers, all equal to the bound.

@art ladder
And still not the theorem. There are infinitely many sizes. The first gap, from one graph to all graphs of a size, closes by computing more. The second can't be closed by computing at all. The bound holds because matched edges are disjoint, so any cover needs one vertex per edge, and the algorithm takes exactly two.

@words text="the sweep measured one implementation"
There's a subtler gap too. The matching is greedy in edge order, so the sweep found the worst case of this routine. A different order is a different matching. The proof never mentioned the order, so it covers every implementation at once, including ones nobody has written.

@chapter Tight, with two witnesses
@art two-witnesses
A bound is tight when some instance attains it. The sweep shows that by producing the instances: the first in edge order, a single edge, and the densest, with five edges on four vertices. Show only the single edge, and a reader decides two is a fluke.

@words text="densest witnesses: 5 edges on 4 vertices · 7 on 5"
The dense witness says the worst case lives among dense graphs too. At five vertices, there's a seven edge witness. Reporting both isn't fussiness.

@chapter Six responses
@art six-roads
Every page here put a measured number beside a claim the measurement can't establish, and said which was which.

@list heading="Six responses to a hard problem" items="Prune an exact search@Prune|Parameterise the exponential@parameterise|Approximate with a guarantee@guarantee|Approximate under a hypothesis@hypothesis|Buy accuracy by the epsilon@epsilon|Restrict to a tractable special case@special case"
Here's what this course built. Prune an exact search. Parameterise the exponential. Approximate with a guarantee. Approximate under a hypothesis. Buy accuracy by the epsilon. Or restrict to a tractable special case. Each gives something up, and each is defended the same way: a computable quantity, beside a claim over all inputs.

@words text="measured: what happened · proved: what can happen"
The measurement says what happened. The proof says what can happen. Neither substitutes for the other.

@words text="a count on one input is not a bound" sub="a count on every input of one size is not a bound either"
A count on one input is not a bound. And a count on every input of one size isn't a bound either. It's the strongest thing a computer can hand you. The last step, to every size, is the one you take with a proof.

@chapter Where people slip
@list heading="Common slips" items="Treating a full sweep as the theorem@The first|Forgetting it measured one implementation@The second|Reading a good ratio as a better guarantee@And the third"
The first slip is treating an exhaustive sweep of one size as the theorem. The second is forgetting the sweep measured one implementation. And the third is reading a comfortable ratio as a better guarantee. Four thirds, ten sevenths, three halves: all well inside their promises, and not one improves a promise.

@end text="Measure, then prove"
Sweep every graph of a size yourself, on Learn. That's learn dot get er done dot I O.
