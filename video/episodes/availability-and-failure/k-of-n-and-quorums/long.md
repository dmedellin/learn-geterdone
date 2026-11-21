---
format: long
lesson: availability-and-failure/k-of-n-and-quorums
title: k-of-n quorums: when another replica makes things worse
thumb: It depends what k does
---

@chapter The question
@title text="k-of-n" sub="Availability and Failure" art=thumb
Should you add another node? Most people say yes, more replicas, more availability. The honest answer is it depends, and it depends on one number: how many of them have to be up.

@art quorum-dots
A system is k of n when it serves as long as at least k of its n components are up. Five replicas needing three. Three replicas needing two. Five needing all five.

@chapter A binomial tail
@math heading="k-of-n availability" items="P(exactly j up) = C(n, j) Aʲ (1 − A)ⁿ⁻ʲ@exactly j;;A(k, n) = Σ_{j ≥ k} C(n, j) Aʲ (1 − A)ⁿ⁻ʲ@sums those terms"
If each component is up independently with probability A, the number up is binomial. The chance that exactly j are up is n choose j, times A to the j, times one minus A to the n minus j. A k of n system sums those terms from j equals k up to n. The upper tail.

@math heading="n = 5, A = 99/100" items="j = 5:  0.9509900499@all five;;j = 4:  0.0480298005@four;;j = 3:  0.0009702990@three;;j = 0, 1, 2:  0.0000098506@the rest;;sum = 1 ✓ · 3-of-5 = 99.9990149%@sums to exactly one"
With five replicas at ninety nine percent, all five are up with probability point nine five one. Exactly four, point oh four eight. Exactly three, about a thousandth. The rest are tiny. The column sums to exactly one, the cheapest check on a binomial. And three of five is ninety nine point nine nine nine oh one four nine percent, five nines.

@art binomial-bars
Picture those terms as bars. The quorum rule draws a line, and the availability is everything on the right of it. Move k, and you move the line.

@chapter The two ends
@art two-ends
At k equals n, only the top term survives, A to the n. That's the series product. At k equals one, everything but j equals zero survives, one minus one minus A to the n. That's the parallel formula. Three formulas, and they're one.

@math heading="Five replicas at 99%" items="1-of-5:  99.999999990000%  ·  ten nines@one of five;;3-of-5:  99.9990149%  ·  5 min 10.65 s a year@three of five;;5-of-5:  95.0990%  ·  17 d 21 h a year@five of five"
Same five machines. One of five is ten nines. Three of five is five nines, five minutes ten seconds a year. Five of five is ninety five point oh nine nine percent. One nine, nearly eighteen days a year, exactly ninety nine hundredths to the fifth.

@chapter When a replica hurts
@art costume
Five of five is worse than a single machine at ninety nine percent. Each new replica was also a new thing that had to be up. A quorum that grows with the fleet is a chain wearing a redundancy costume.

@words text="2-of-3 = 99.97020% · 3-of-5 = 99.9990149%" sub="majority: k = ⌈(n+1)/2⌉"
Majority quorums sit between the extremes, and they do improve with n, because k grows half as fast. Two of three is ninety nine point nine seven oh two. Three of five is five nines. That's why clusters have five nodes, and why seven buys much less.

@chapter The write quorum that made it worse
@math heading="n = 3, A = 99/100" items="j = 2:  C(3,2)(99/100)²(1/100) = 0.029403@exactly one;;2-of-3 = 0.029403 + 0.970299 = 99.97020%@two of three;;3-of-3 = 0.970299 = 97.0299%@three of three"
A team runs three replicas, and, worried about durability, requires writes to reach all three instead of two. The term at j equals two, point oh two nine four, is exactly one node down. Two of three survives that, ninety nine point nine seven. Three of three doesn't, ninety seven point oh three.

@art config-constant
Write availability went from three nines to one. From two hours thirty six minutes a year, to ten days twenty hours. Nothing about the hardware changed. Only a constant in a configuration file.

@art stale-read
One boundary. This counts replicas that are up, not whether they agree on the data. An available quorum can still return a stale read. Preventing that is a different condition on k, in the replication course.

@chapter Where people slip
@list heading="Common slips" items="Assuming more replicas is more availability@The first|Quoting one figure for two quorums@The second|Treating the quorum as a safety knob only@The third"
The first slip is assuming more replicas means more availability. Ask what k does as n grows. The second is quoting one figure for a system with two quorums. Reads at one of three and writes at three of three are ten nines and one nine on the same hardware. The third is treating the quorum as only a correctness knob.

@chapter Try it
@words text="4-of-5 at 99%" sub="you need the j = 4 and j = 5 terms"
Your turn. Five nodes at ninety nine percent, needing four. You'll need the terms at j equals four and five, which you've seen. Find the availability and annual downtime, place it between three of five and five of five, and say what must happen to k for three nodes to five to help.

@end text="Move n and k, watch the tail"
You can set n and k and see every term of the binomial, summed exactly, on Learn. That's learn dot get er done dot I O.
