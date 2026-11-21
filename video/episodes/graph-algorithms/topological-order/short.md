---
format: short
lesson: graph-algorithms/topological-order
title: There's no such thing as the topological order
---

@art four-orders
Two correct topological sorts, two different answers. So which one is right?

@math items="Kahn:  1 2 3 4 5 6@Kahn's method;;DFS:  2 1 3 5 4 6@the depth first walk"
On one task graph, Kahn's method gives one, two, three, four, five, six. The depth first walk gives two, one, three, five, four, six.

@words text="4 valid orders"
Both. This graph has four valid orders, and uniqueness is a count, not a feeling.

@end text="Full lesson on Learn"
The full lesson, with every order counted, is on Learn.
