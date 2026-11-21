---
format: short
lesson: networks-flows-paths-and-assignments/maximum-flow-and-minimum-cut
title: The backward arc that rescues max flow
---

@art backward-arc
Leave out one kind of arc, and your max flow algorithm stops at four instead of five.

@math items="s→b, back b→a, a→t@backward;;value 4 → 5@five"
On the lesson's network, the third augmenting path goes s to b, then backward from b to a, then a to t. There's no arc from b to a. It un-sends a unit and reroutes it, and the flow climbs from four to five.

@words text="No backward arcs: stuck at 4"
Without that move, no path remains at four, and the algorithm reports it as the answer.

@end text="Full lesson on Learn"
The full lesson, with every cut checked, is on Learn.
