---
format: short
lesson: graph-algorithms/augmenting-paths
title: This flow is stuck, and it isn't the maximum
---

@art undo
Push flow along the first path you find, and you can get stuck at one when the answer is two.

@words text="backward arcs off: value 1"
On this little network, the path through the middle arc uses up the routes, and no forward path is left.

@words text="backward arcs on: value 2"
Allow a path to run backwards along the middle arc, and it cancels that first choice and reroutes it. Now two units get through.

@end text="Full lesson on Learn"
The full lesson, with the residual network, is on Learn.
