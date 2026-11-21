---
format: short
lesson: intractability-and-approximation/circuits-tours-and-the-chain
title: Turn a graph into a travelling salesman problem
---

@art tour-steps
Edges cost one, non edges cost two. Now finding a cheap tour is hard.

@words text="budget B = n"
Set the budget to n, the number of cities.

@words text="n steps, each 1 or 2"
A tour takes exactly n steps. So it costs n only if every step is an edge, which makes it a Hamilton circuit.

@art five-cycle-tour
On the five cycle, twelve tours are possible, and exactly one is within budget: the cycle itself.

@end text="Full lesson on Learn"
The full lesson is on Learn.
