---
format: short
lesson: replication-and-consistency/sloppy-quorums
title: R plus W equals N misses one read in three
---

@art edge-not-safe
Three replicas. Reads of two, writes of one. Sounds like the edge of safe. It misses one read in three.

@math items="C(2, 2) / C(3, 2) = 1/3@two choose two"
The write reached one node. The read misses if both its nodes are the other two. Two choose two over three choose two. A third.

@words text="R + W must be greater than N"
Equal isn't nearly greater. One more node on either side takes it to zero.

@end text="Full lesson on Learn"
The full lesson, with every configuration counted, is on Learn.
