---
format: short
lesson: scaling-laws-and-cost/vertical-vs-horizontal
title: Why five nodes' worth needs six nodes
---

@art extra-node
You need five times one node's capacity. Five nodes won't do it.

@math items="200N / (199 + N) ≥ 5@two hundred N;;N = 5:  4.90×,   N = 6:  5.85×@five nodes"
Nodes spend some of their work coordinating. At this contention, N nodes deliver two hundred N over a hundred and ninety nine plus N. Five nodes give four point nine times. Six give five point eight five.

@words text="Solve for N. Don't divide."
The sixth node pays for the coordination of the other five.

@end text="Full lesson on Learn"
The full lesson, with the big machine priced too, is on Learn.
