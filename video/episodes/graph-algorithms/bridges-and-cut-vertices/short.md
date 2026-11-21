---
format: short
lesson: graph-algorithms/bridges-and-cut-vertices
title: A cut vertex with no bridge anywhere
---

@art shared-vertex
Two triangles share a single vertex. Remove it, and the graph falls apart. But there's no bridge.

@words text="every edge is on a triangle"
Every edge here lies on a cycle, so deleting any one edge leaves everything connected. But the shared vertex is the only way between the two triangles.

@words text="low[v] > d[u] · low[v] ≥ d[u]"
The two tests differ by one comparison, and neither property implies the other.

@end text="Full lesson on Learn"
The full lesson, with the low link walk, is on Learn.
