---
format: short
lesson: graphs-and-trees/paths-and-connectivity
title: How to spot a bridge in a graph
---

@art bridge-edge
Which single edge would split this network in two? There's a one line test.

@words text="A bridge lies on no cycle"
An edge is a bridge exactly when it lies on no cycle. If it's on a cycle, the rest of the cycle is a detour, so removing it disconnects nothing.

@art three-components
In this seven vertex graph, the edges three four and five six lie on no cycle, so they're bridges. The triangle's three edges aren't.

@end text="Full lesson on Learn"
The full lesson, with bridges to find yourself, is on Learn.
