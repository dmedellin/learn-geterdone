---
format: short
lesson: intro-algorithms-graphs/maximum-flow
title: To push more flow, sometimes you send it back
---

@art stuck
The first path you find can block the maximum flow.

@math items="first path: 2 · max: 3@stops at two"
On the lesson's network, the first path pushes two units through the arc from two to three, and then the search stops at two. The maximum is three.

@art residual
The fix is a backward arc. Sending against that flow cancels one unit and reroutes it, and the third unit gets through.

@end text="Full lesson on Learn"
Push flow both ways in the full lesson on Learn.
