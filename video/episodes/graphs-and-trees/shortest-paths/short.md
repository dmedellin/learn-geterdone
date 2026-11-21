---
format: short
lesson: graphs-and-trees/shortest-paths
title: The shortest route isn't the cheapest
---

@art worked-route
The route with the fewest roads can cost twice as much as the cheapest one.

@math items="s → a → t:  10 + 1 = 11@ten plus one;;s → b → t:  3 + 9 = 12@three plus nine;;s → b → a → t:  3 + 2 + 1 = 6@three plus two plus one"
Two edge routes: ten plus one is eleven, and three plus nine is twelve. But the three edge route is three plus two plus one, just six.

@words text="Fewest edges ≠ least weight"
Breadth first search finds the fewest edges. For the least total weight, you need Dijkstra.

@end text="Full lesson on Learn"
The full lesson on Dijkstra's algorithm is on Learn.
