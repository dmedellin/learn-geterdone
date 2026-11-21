---
format: long
lesson: replication-and-consistency/majorities-and-fault-tolerance
title: Why consensus clusters have an odd number of nodes
thumb: Four is worse than three
---

@chapter The question
@title text="Majorities and Fault Tolerance" sub="Replication and Consistency" art=thumb
You run a three node consensus cluster and a spare machine turns up. Add it, and you'll have four. More nodes, more resilience? No. Four nodes tolerate exactly what three do, and they're less available.

@art two-majorities
A majority of n nodes is any set of size n over two, rounded down, plus one. And any two majorities of the same n must share a node. That's why consensus is built on them.

@chapter Why majorities
@words text="A node doesn't vote both ways"
That's the same pigeonhole argument as quorum overlap. A node that voted for one decision can refuse a conflicting one. So two leaders can't be elected in the same term. A majority is simply the smallest quorum that overlaps itself.

@math heading="Failures tolerated" items="majority = ⌊n/2⌋ + 1@a majority;;f = n − majority = ⌊(n − 1)/2⌋@tolerates;;n = 2f + 1@two f plus one"
The cluster keeps working while a majority is up. So it tolerates n minus the majority, which is n minus one over two, rounded down. To tolerate f failures, buy two f plus one nodes.

@chapter The table
@list heading="Each node up 99%" items="n = 3:  majority 2 · f = 1 · 99.9702%@three nodes|n = 4:  majority 3 · f = 1 · 99.940797%@four nodes|n = 5:  majority 3 · f = 2 · 99.99901494%@Five need three|n = 7:  majority 4 · f = 3@seven"
With each node up ninety nine percent of the time, three nodes need two, tolerate one failure, and are available ninety nine point nine seven oh two percent. Four nodes need three, still tolerate one, and are ninety nine point nine four oh eight. Five need three and tolerate two. Seven need four and tolerate three.

@art odd-steps
Read down the tolerance and the rule falls out. It only rises on the odd sizes: three, five, seven. The even sizes carry the cost of the next size up, and the tolerance of the one below.

@chapter Why four is worse
@math heading="n = 3, majority 2" items="C(3,2)(99/100)²(1/100) + (99/100)³@three choose two;;= 29 403/1 000 000 + 970 299/1 000 000@twenty nine thousand;;= 999 702/1 000 000 = 99.9702%@ninety nine point nine seven"
For three nodes, it's three choose two, times point nine nine squared, times point oh one, plus point nine nine cubed. That's twenty nine thousand four hundred and three, plus nine hundred and seventy thousand two hundred and ninety nine, in a million. Ninety nine point nine seven oh two percent.

@math heading="n = 4, majority 3" items="C(4,3)(99/100)³(1/100) + (99/100)⁴@four choose three;;= 99 940 797/100 000 000 = 99.940797%@ninety nine point nine four;;−0.029403 points · downtime ≈ doubled@about doubled"
For four, it's four choose three, times point nine nine cubed, times point oh one, plus point nine nine to the fourth. Ninety nine point nine four oh seven nine seven percent. That's point oh two nine four points less, with the downtime about doubled.

@art three-specific
Because now you need three specific machines up instead of two, from a pool with one more thing that can break. The even step raises the quorum and the pool by one each, and at ninety nine percent per node, the quorum wins.

@chapter The real next step
@art five-nodes
From three, the upgrade is five, not four. Five tolerates two failures, and is available ninety nine point nine nine nine oh one percent, about a thirtieth of the downtime. If you can afford one more node and not two, keep three, and spend the money making each node more available.

@art one-rack
And all of this assumes independent failures. Three nodes in one rack share a switch, a power feed and an operator. Then the real availability is closer to one node's. Spreading the nodes across failure domains is what makes the arithmetic approximately true.

@chapter Where people slip
@list heading="Common slips" items="Believing a bigger majority tolerates more@The first|Sizing a cluster on an even number@The second|Quoting the binomial for dependent nodes@The third"
The first slip is believing a bigger majority tolerates more failures. The second is sizing a cluster on an even number. Every even size is dominated by the odd one below it. The third is quoting the binomial availability for nodes that aren't independent.

@art non-voting
If you really have a spare machine, it doesn't have to vote. As a non voting replica, it can serve reads without joining the quorum, so it adds capacity without raising the majority.

@chapter Try it
@words text="each node up 95%" sub="n = 3: 3(0.95)²(0.05) + (0.95)³"
Your turn. Say each node is only ninety five percent available. Three nodes give three times point nine five squared times point oh five, plus point nine five cubed. Do the same for four and five, and say whether the even size penalty is larger or smaller than at ninety nine.

@end text="Add a node, watch the majority"
You can set the cluster size and per node availability and see each majority's tolerance, on Learn. That's learn dot get er done dot I O.
