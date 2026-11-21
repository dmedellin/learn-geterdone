---
format: short
lesson: networks-flows-paths-and-assignments/the-minimum-cost-flow-programme
title: How a minimum cost turns into a maximum flow
---

@art return-arc
Want the biggest flow through a network? Minimise a cost instead.

@words text="Return arc t→s, cost −1, no bound"
Price every arc at zero. Add one arc from the sink back to the source, with no upper bound and a cost of minus one. Supply nothing anywhere.

@words text="Optimum −5  →  maximum flow 5"
Now the only way to save money is to run flow round the loop. On the lesson's network the optimum is minus five, so the maximum flow is five.

@end text="Full lesson on Learn"
The full lesson, with all four problems in one programme, is on Learn.
