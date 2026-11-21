---
format: long
lesson: graphs-and-trees/graph-colouring
title: Graph colouring: why two colours is easy and three is hard
thumb: Neighbours never match
---

@chapter The question
@title text="Graph Colouring" sub="Graphs and Trees" art=thumb
Five exams, and some pairs share a student, so they can't be at the same time. What's the fewest time slots you need? That's a colouring problem.

@chapter The definition
@art proper-colouring
A proper colouring gives each vertex a colour so that no edge joins two vertices of the same colour. The chromatic number, chi of G, is the smallest number of colours that makes a proper colouring possible.

@math heading="Some chromatic numbers" items="χ(Kₙ) = n@complete graph;;χ(Cₙ) = 2 if n even, 3 if n odd@a cycle;;χ(tree) = 2, for a tree with an edge@any tree"
A complete graph on n vertices needs n colours, because every pair is adjacent. A cycle needs two if it's even, and three if it's odd. And any tree with at least one edge needs exactly two.

@art odd-even-cycles
Two colours is a familiar question. Chi of G is at most two exactly when the graph is bipartite, which is exactly when it has no odd cycle. You can test that with one breadth first search.

@chapter Greedy colouring
@art greedy-order
Here's a fast method. Go through the vertices in any order, and give each one the smallest colour none of its already coloured neighbours has. That's greedy colouring.

@math heading="The greedy bound" items="at most Δ coloured neighbours@at most delta;;so at most Δ colours forbidden@forbidden;;so Δ + 1 colours always suffice@delta plus one"
Let delta be the largest degree. When you reach a vertex, it has at most delta neighbours, so at most delta colours are forbidden. With delta plus one colours, one is always free. Brooks's theorem sharpens it: delta colours are enough, unless the graph is complete or an odd cycle.

@words text="Greedy gives a bound, not χ"
But greedy isn't optimal, and the order is what costs it. On a bipartite graph, a bad order can use more colours than the two you need.

@chapter Scheduling exams
@math heading="Edges: A–B, A–C, B–C, B–D, C–D, D–E" items="A, B, C form a triangle → χ ≥ 3@a triangle;;A 1 · B 2 · C 3 · D 1 · E 2@Greedy in order;;3 colours used and χ ≥ 3 → χ = 3@so chi is three"
Edges join A B, A C, B C, B D, C D and D E. A, B and C are all adjacent, a triangle, so you need at least three colours. Greedy in order: A gets one, B gets two, C gets three, D gets one, and E gets two. Three colours used, and at least three needed, so chi is three.

@art exam-graph
So three time slots work: A and D together, B and E together, and C alone. The triangle gave the lower bound, greedy gave the upper bound, and they met. That's the only cheap way to be certain.

@list heading="Colouring models conflict" items="Registers: variables live at the same time@Compilers|Frequencies: transmitters that interfere@transmitters|Sudoku: 81 vertices, 9 colours@Sudoku"
The same idea models any conflict. An edge means can't share, and a colour is a resource. Compilers colour variables that are live at the same time, with registers as colours. Transmitters that would interfere get different frequencies. Even Sudoku is a nine colouring of a graph with eighty one vertices.

@art clique-inside
That lower bound is worth remembering. If a graph contains a complete graph on k vertices, it needs at least k colours. It's usually the easiest lower bound to find.

@chapter Two is easy, three is hard
@words text="χ ≤ 2: linear time" sub="χ ≤ 3: NP-complete"
Here's the surprise. Deciding whether two colours suffice takes one search. Deciding whether three suffice is NP complete, and computing chi exactly is NP hard. Even approximating it well is hard. Nothing in the statement warns you.

@chapter Four colours
@art planar-map
Now the most famous theorem in graph theory. Every planar graph can be coloured with at most four colours. It was conjectured in 1852, and proved by Appel and Haken in 1976, by reducing it to 1936 configurations and checking them by computer.

@words text="The first proof no human could check by reading"
It was the first major theorem whose proof couldn't be verified by a person reading it. The five colour theorem, by contrast, has a short proof by induction. Four really is harder than five.

@chapter Where people slip
@list heading="Common slips" items="Treating greedy's answer as χ@The first|Thinking planar graphs need four@The second|Forgetting the clique lower bound@And the third"
The first slip is treating greedy's answer as the chromatic number. It's only an upper bound. The second is thinking every planar graph needs four colours. Four suffice, and many need two or three. And the third is forgetting the clique lower bound.

@chapter Try it
@words text="χ(C₅) = ?" sub="2, 3, 4 or 5?"
Your turn. What's the chromatic number of the five cycle? Show that two colours fail, and then find a proper colouring with three.

@end text="Watch greedy, and both bounds"
You can load the exam graph and compare greedy with both bounds, on Learn. That's learn dot get er done dot I O.
