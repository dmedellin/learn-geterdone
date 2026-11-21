---
format: short
lesson: graph-algorithms/max-flow-and-min-cut
title: When max flow gets stuck, it hands you a proof
---

@art reachable-set
When the max flow search fails, the failure is the proof that you're done.

@words text="S = everything the source can still reach"
Take every vertex the source can still reach in the residual network. Every arc leaving that set is full, and every arc coming in is empty.

@words text="flow = cut capacity ⟹ both optimal"
So the cut's capacity equals the flow. No flow beats any cut, so nothing can beat this one.

@end text="Full lesson on Learn"
The full lesson, checked against every cut, is on Learn.
