---
format: short
lesson: graph-algorithms/the-cut-property
title: The minimum spanning tree swap in one picture
---

@art exchange
Why is the lightest edge across a cut always safe to take? One swap proves it.

@words text="add e, remove g"
Take a minimum tree without that edge. Add it, and you get one cycle, which must cross the cut a second time. Remove that other crossing edge.

@words text="w(e) ≤ w(g)"
You still have a spanning tree, and it's no heavier. So some minimum tree contains the lightest edge.

@end text="Full lesson on Learn"
The full lesson, with every spanning tree listed, is on Learn.
