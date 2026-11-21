---
format: short
lesson: combinatorics-and-counting/combinatorial-proof
title: Why a graph's degrees always add up to an even number
---

@art incidence-grid
Add up every degree in any graph, and the total is always even. Why?

@math items="vertex by vertex: Σ deg(v)@Vertex by vertex;;edge by edge: 2 · |E|@Edge by edge;;Σ deg(v) = 2|E|@Same set"
Count the pairs of a vertex and an edge touching it. Vertex by vertex, you get the sum of the degrees. Edge by edge, each edge has two ends, so you get twice the number of edges. Same set, so the two counts are equal.

@words text="one set, counted twice"
That's double counting: one set, two counts, and so one answer.

@end text="Full lesson on Learn"
The full lesson, with bijections too, is on Learn.
