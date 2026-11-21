---
format: short
lesson: intractability-and-approximation/a-reduction-is-a-construction
title: Turn a logic formula into a graph
---

@art clause-triangles
Here's how to turn a logic formula into a graph problem.

@list items="A triangle on each clause@triangle|An edge between x and ¬x@an edge|Ask for an independent set of size m@independent set"
Give each clause a triangle of literal vertices. Put an edge between every x and every not x. Then ask for an independent set as big as the number of clauses.

@words text="satisfiable ⟺ set of size m"
The triangles force one literal per clause, and the extra edges forbid contradictions. So the set exists exactly when the formula is satisfiable.

@end text="Full lesson on Learn"
The full lesson is on Learn.
