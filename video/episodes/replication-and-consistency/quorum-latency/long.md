---
format: long
lesson: replication-and-consistency/quorum-latency
title: Quorum latency: why adding a replica makes writes faster
thumb: More racers, earlier second place
---

@chapter The question
@title text="Quorum Latency: the W-th Fastest" sub="Replication and Consistency" art=thumb
Your quorum write waits for two replicas out of three. Add a fourth replica, and does the write get slower? Everyone expects yes. It gets twice as fast. And it quietly breaks something on the way.

@art race
A quorum write is sent to all N replicas, and acknowledged as soon as W of them reply. It doesn't wait for everyone. It waits for the W th fastest.

@chapter A binomial tail
@math heading="Acknowledged by t" items="P(ack by t) = P(at least W of N replied by t)@at least W;;= Σ_{k ≥ W} C(N, k) F(t)ᵏ (1 − F(t))ᴺ⁻ᵏ@the sum"
If replies are independent with distribution F, the chance the write is acknowledged by t is the chance that at least W of N replied by t. That's the sum over k from W to N, of N choose k, times F to the k, times one minus F to the N minus k. The same binomial tail as k of n availability.

@art stragglers
Use the same per replica reply times as the synchronous write lesson. Sixty percent reply by two milliseconds, ninety percent by four, ninety seven by eight, ninety nine point two by sixteen, and ninety nine point eight by twenty four.

@chapter Sweeping N at W = 2
@list heading="p99 of the quorum ack" items="N = 3, W = 3:  24 ms@everybody|N = 2:  24 ms@two of two|N = 3:  8 ms@two of three|N = 4:  4 ms@two of four|N = 8:  2 ms@two of eight"
Waiting for everybody, three of three, costs twenty four milliseconds. Two of two also waits for both, twenty four. Two of three costs eight, a third as much, for a write still on two machines. Two of four costs four. And two of eight costs two.

@chapter Why bigger is faster
@math heading="At t = 4 ms, F = 9/10" items="N = 3:  3(81/100)(1/10) + 729/1000 = 972/1000@three replicas;;0.972 < 0.99@short of;;N = 4:  1 − 1/10 000 − 36/10 000 = 9963/10 000@With four;;0.9963 ≥ 0.99  →  p99 = 4 ms@clears"
At four milliseconds, each replica has replied with probability nine tenths. With three replicas, the chance at least two did is nine seven two in a thousand, short of ninety nine percent. With four, it's one minus the chance of zero or one replies, nine nine six three in ten thousand. That clears it.

@art more-racers
Nothing about the fourth replica is faster. W is a threshold, and N is the number of attempts at it. Fewer than two replies now needs three stragglers instead of two, and stragglers are rare. A race with more entrants finishes its second place earlier.

@art floor
And it doesn't go on forever. From four to eight replicas, the p ninety nine halves again to two milliseconds, the floor of this distribution. No configuration beats the fastest time any replica ever replies.

@chapter What N breaks
@math heading="R = 2, W = 2" items="N = 3:  R + W = 4 > 3  ·  overlap 1@three nodes;;N = 4:  R + W = 4 = N  ·  no overlap@Add the fourth replica;;miss = C(2, 2)/C(4, 2) = 1/6@one read in six"
But the same cluster reads with R of two. At three nodes, R plus W is four, more than three, so reads overlap writes. Add the fourth replica, and R plus W equals N. One read in six now misses the write.

@art broken-overlap
That's C of two two, over C of four two, from the sloppy quorums lesson. Nothing gets slower. Nothing logs an error. A sixth of reads just stop seeing recent writes.

@art slower-read
Restoring overlap means R of three, so every read waits for the third fastest of four, instead of the second of three. The write got faster by making the read slower, and no dashboard would show the trade.

@words text="N lowers fixed-W latency · N works against R + W > N"
So the rule isn't more replicas are slower, or faster. N moves a fixed W quorum's latency down, and moves the overlap condition against you, at the same time. Compute both whenever N changes.

@chapter Where people slip
@list heading="Common slips" items="Assuming more replicas slow a fixed-W write@The first|Raising N without re-checking R + W > N@The second|Quoting the quorum p99 as the slowest replica's@The third"
The first slip is assuming more replicas make a fixed W write slower. They're extra racers. The second is raising N without rechecking R plus W greater than N. That fails quietly. The third is quoting the quorum p ninety nine as the slowest replica's, three times too high here.

@chapter Try it
@words text="N = 4, R = W = 2" sub="R + W = 4 is not > 4"
Your turn. The team takes four replicas for the faster write, with R and W of two. R plus W is no longer more than N. Work out what R must become, compute the read's p ninety nine with the same binomial tail, and give the net change to a read then write round trip.

@end text="Sweep N, watch both effects"
You can set N and W and read the quorum's p ninety nine against the overlap condition, on Learn. That's learn dot get er done dot I O.
