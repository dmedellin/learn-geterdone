---
format: short
lesson: replication-and-consistency/majorities-and-fault-tolerance
title: A four node cluster is less available than three
---

@art three-specific
Adding a fourth node to your three node cluster makes it less available.

@math items="3 nodes, need 2:  99.9702%@three nodes;;4 nodes, need 3:  99.940797%@four nodes"
Three nodes need a majority of two, and tolerate one failure. Four nodes need three, and still tolerate only one. At ninety nine percent each, four nodes have about double the downtime.

@words text="3, 5, 7: n = 2f + 1"
Buy odd sizes. Two f plus one.

@end text="Full lesson on Learn"
The full lesson, with cluster sizes to try, is on Learn.
