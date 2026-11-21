---
format: long
lesson: replication-and-consistency/quorums-overlap
title: Quorum overlap: what R plus W greater than N really guarantees
thumb: One node, and only one
---

@chapter The question
@title text="Quorums Overlap" sub="Replication and Consistency" art=thumb
Every quorum system rests on one inequality: R plus W greater than N. It's proved in two lines. But what it guarantees is smaller than most people think, and this video says exactly how much smaller.

@art read-write-sets
A write is applied to a set of W nodes. A read consults a set of R nodes. Both are drawn from the same N. The question is whether those two sets must share a node.

@chapter Pigeonhole
@math heading="The overlap bound" items="R + W names drawn from N nodes@names;;R + W > N  ⟹  |read ∩ write| ≥ R + W − N@at least R plus W;;R + W ≤ N  ⟹  disjoint sets exist@at most N"
Together the two sets name R plus W nodes, from a pool of N. Each node can be named at most twice, once by each set. So if R plus W is more than N, at least R plus W minus N names must appear in both. And if R plus W is at most N, you can pick the read entirely outside the write.

@art pigeonholes
That's the pigeonhole principle, with machine names as the pigeonholes. Nothing about time, ordering, or protocol enters the argument.

@chapter The bound is attained
@math heading="N = 3, R = 2, W = 2" items="read sets {1,2} {1,3} {2,3}@read sets;;write sets {1,2} {1,3} {2,3}@write sets;;9 pairs · smallest intersection 1 = R + W − N@nine pairs;;6 of 9 pairs sit exactly on the bound@six of the nine"
Take three nodes, reads of two and writes of two. There are three read sets and three write sets, so nine pairs. The smallest intersection is one, exactly R plus W minus N. And six of the nine pairs sit exactly on that bound.

@art bound-attained
So the worst case is the common case. A design that assumed a comfortable margin of agreement has assumed something false most of the time. The guarantee is one node. And one node is enough, if the reader knows what to do with answers that disagree.

@chapter What overlap doesn't buy
@art unlabeled-values
The read set contains a node holding the latest acknowledged write. It also contains nodes holding older values, and the reader gets all of them, with no label saying which is which. Version numbers or timestamps turn overlap into an answer, and they bring their own problems.

@art concurrent-writes
Now two concurrent writes. Client one writes x equals one to nodes one and two. At the same moment, client two writes x equals two to nodes two and three. A reader of one and three sees both values and overlaps both writes, as promised. But neither write happened first, so the reader still can't say which is current. That's a conflict, not staleness.

@words text="No acknowledged write is missed entirely" sub="not: the read returns the current value"
So the right claim is this. No acknowledged write can be missed entirely by a later read. That's real and useful. It isn't the read returns the current value, and the gap between those is where the rest of this course lives.

@chapter Five nodes
@list heading="N = 5" items="R = 3, W = 3:  overlap 1@three and three|R = 1, W = 5 · R = 5, W = 1:  overlap 1@one and five|R = 2, W = 3:  R + W = N, no guarantee@two and three|R = 4, W = 4:  overlap 3@four and four"
With five nodes, three and three overlap by one. One and five, or five and one, also overlap by one. But they can't tolerate a node down on writes, or on reads. And four and four overlap by three. Two and three is the trap.

@art disjoint-sets
It's popular because R plus W equals N looks like a boundary you're standing on. You're outside it. A write to nodes one, two and three, and a read of four and five, are both legal under that configuration, and they share nothing.

@chapter Where people slip
@list heading="Common slips" items="Reading R + W > N as R + W ≥ N@The first|Treating R + W − N as having slack@The second|Calling a quorum configuration consistent@The third"
The first slip is reading greater than as greater than or equal. At three nodes, R plus W of three misses the write one time in three. The second is treating R plus W minus N as a bound with slack. It's attained. The third is calling a quorum configuration consistent.

@chapter Try it
@words text="N = 7, R = 3, W = 5" sub="R + W = 8 > 7"
Your turn. Seven nodes, reads of three, writes of five. Eight is more than seven, so it overlaps. Find the minimum overlap. Then cut W to four, find the smallest R that still overlaps, and say what that does to the read path.

@end text="Enumerate every pair yourself"
You can set N, R and W and see every read set and write set pair, on Learn. That's learn dot get er done dot I O.
