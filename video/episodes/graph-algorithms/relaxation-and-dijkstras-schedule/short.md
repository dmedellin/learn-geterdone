---
format: short
lesson: graph-algorithms/relaxation-and-dijkstras-schedule
title: Dijkstra's algorithm is just a schedule
---

@art relax-step
Dijkstra's algorithm is one line of arithmetic, done in a clever order.

@words text="if d[u] + w < d[v], lower d[v]"
If going to u and then along an edge beats the best route to v, write the better number down. That's relaxation, and it never undershoots.

@math items="heap:  18 relaxations@a heap;;arc order:  36@arc order"
Relax nearest first from a heap, and the lab's graph takes eighteen relaxations. Sweep in arc order, and it takes thirty six. Same distances.

@end text="Full lesson on Learn"
The full lesson, with three schedules side by side, is on Learn.
