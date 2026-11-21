---
format: long
lesson: intractability-and-approximation/circuits-tours-and-the-chain
title: Hamilton circuit to travelling salesman, and why TSP can't be approximated
thumb: Distance one or two
---

@chapter The cleanest reduction
@title text="Circuits, Tours and the Chain" sub="Intractability and Approximation" art=thumb
Here's the cleanest reduction in this course. Every pair of cities gets distance one or two, the budget is the number of cities, and the solutions on both sides are literally the same list.

@list heading="Two problems" items="Hamilton circuit: a cycle visiting every vertex once@A Hamilton circuit|Travelling salesman: a tour within a budget@the travelling salesman"
A Hamilton circuit is a cycle visiting every vertex of a graph exactly once. The travelling salesman decision problem gives a distance for every pair of cities and a budget, and asks whether some tour, visiting every city once and returning, costs at most the budget.

@chapter The construction
@math heading="From G to distances" items="D[u][v] = 1  if uv is an edge@one;;D[u][v] = 2  if it isn't@two;;budget B = n@the budget"
Put distance one where the graph has an edge, and two where it doesn't. Set the budget to n, the number of vertices.

@art tour-steps
A tour visits n cities and returns, so it takes exactly n steps, each costing one or two. So it costs at least n, and exactly n only when every step is an edge. And a tour where every step is an edge is a Hamilton circuit.

@words text="tours within budget = Hamilton circuits" sub="the same cyclic sequences"
So the tours within budget and the Hamilton circuits are the same sequences. The map on solutions is the identity. That's stronger than a reduction needs.

@chapter The five-cycle
@art five-cycle-tour
The lab loads the five cycle. Five vertices, five edges, budget five. It considers twelve tours. One is within budget, and it's the one Hamilton circuit, the cycle itself. The panel confirms the two lists are the same list.

@math heading="Counting tours" items="(5 − 1)! / 2 = 12@four factorial;;tour lengths: 5, 7, 8, 10@five, seven;;no tour of 6@no tour costs six"
Twelve is four factorial over two. Start from city one, and count a tour and its reverse once. The tour lengths are five, seven, eight and ten. No tour costs six. Dropping one edge of the cycle leaves a path whose ends are joined only by that same edge, so one non edge forces a second.

@art tour-lengths
The budget separates the one from the eleven, and it's the only thing doing the separating.

@art reverse-tour
That counting convention matters. Count a cycle and its reverse separately on one side, and a perfect identity looks like a two to one map. Canonicalise both sides the same way before comparing.

@chapter The chain
@art reduction-chain
Nobody reduces satisfiability to the travelling salesman in one step. The route runs through a chain of problems, and reductions compose. Two polynomial maps make a polynomial map. This page builds the last link.

@list heading="Built here, and quoted" items="Built: search from decision, SAT to independent set, cover and clique, subset sum, Hamilton to TSP@Built on this course|Quoted: Cook–Levin, and independent set to Hamilton circuit@quoted"
Built on this course: search from decision, satisfiability to independent set, the identity to cover and clique, satisfiability to subset sum, and Hamilton circuit to the travelling salesman. Quoted, not built: Cook Levin, that satisfiability is NP complete at all, and the link from independent set into Hamilton circuits.

@chapter No constant factor
@math heading="Inapproximability" items="off-edge distance ρ·n + 1@rho times n;;Hamilton circuit  ⟹  optimum = n@optimum is exactly n;;no circuit  ⟹  every tour > ρ·n@more than rho"
Now raise the off edge distance to rho times n, plus one. If there's a Hamilton circuit, the optimum is exactly n, so a rho approximation must return a tour costing at most rho times n. If there isn't, every tour uses a non edge and costs more than rho times n. So the returned cost decides Hamilton circuit.

@art huge-penalty
The distances are still polynomial to write down. And the whole procedure runs in polynomial time.

@words text="ρ-approximation for general TSP  ⟹  P = NP"
So no constant factor approximation exists for the general travelling salesman unless P equals N P. That's why approximating a tour later needs a hypothesis, the triangle inequality. The lab itself uses two, not rho times n plus one, because its distances come from the graph. A later lesson turns that number into a slider.

@chapter Where people slip
@list heading="Common slips" items="Counting a tour and its reverse twice@The first|Reading this as an approximation result@The second|Thinking every link was built here@And the third"
The first slip is counting a tour and its reverse as two solutions. The second is reading the one or two construction as an approximation result. With distances one and two, a factor of two is free. And the third is treating the chain as though every link were built here.

@end text="Distance one or two"
Enumerate the tours of the five cycle yourself, on Learn. That's learn dot get er done dot I O.
