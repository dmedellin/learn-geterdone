---
format: short
lesson: replication-and-consistency/quorums-overlap
title: R plus W greater than N guarantees one node, not consistency
---

@art read-write-sets
Reads of two, writes of two, three nodes. How many nodes must they share?

@math items="R + W − N = 2 + 2 − 3 = 1@two plus two"
Two plus two minus three. Exactly one. And six of the nine possible pairs share only that one node.

@words text="One node saw it" sub="not: the read knows which value is current"
So a read can't miss an acknowledged write entirely. But it can't tell which answer is current without versions.

@end text="Full lesson on Learn"
The full lesson, with every pair enumerated, is on Learn.
