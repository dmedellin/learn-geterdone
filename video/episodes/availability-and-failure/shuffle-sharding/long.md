---
format: long
lesson: availability-and-failure/shuffle-sharding
title: Shuffle sharding: turn outages into degradations by counting overlaps
thumb: Overlap is not collision
---

@chapter The question
@title text="Blast Radius and Shuffle Sharding" sub="Availability and Failure" art=thumb
One tenant sends a request that poisons a node. How many other tenants go down with it? With the right placement, almost none. And you can count exactly how many.

@art fixed-shards
The obvious layout splits the fleet into fixed shards. Sixteen nodes, eight shards of two. If one tenant poisons a node, its whole shard is out, and every tenant in that shard is fully down. That's an eighth of the fleet.

@chapter Shuffle sharding
@art random-subsets
Shuffle sharding gives each tenant k of the n nodes, drawn at random, independently per tenant. There are n choose k possible assignments. At sixteen nodes and two per tenant, that's a hundred and twenty distinct shards.

@math heading="Overlap in j nodes" items="P(j) = C(k, j)·C(n − k, k − j) / C(n, k)@shares exactly j"
Fix your k nodes. Another tenant shares exactly j of them with probability k choose j, times n minus k choose k minus j, over n choose k. Choose j from yours and the rest from the nodes you don't hold. That's the hypergeometric distribution, and it's exact.

@math heading="n = 16, k = 2" items="j = 0:  91/120 = 75.8333%  untouched@zero shared;;j = 1:  28/120 = 7/30 = 23.3333%  degraded@one shared;;j = 2:  1/120 = 0.8333%  down with you@both shared;;91 + 28 + 1 = 120 ✓@sums to"
Zero shared nodes: ninety one in a hundred and twenty, about seventy six percent. One shared: twenty eight in a hundred and twenty, seven thirtieths. Both shared: one in a hundred and twenty. And ninety one plus twenty eight plus one sums to a hundred and twenty.

@chapter Overlap is not collision
@art poison-request
Suppose a tenant sends a request that makes a node unusable. A poison pill, a query that exhausts memory, a pattern that triggers a bug. Every tenant sharing that node is affected. But affected how?

@art one-left
A tenant that shares one of your two nodes still has one working node. If its client retries elsewhere, it still has a service. It's degraded, not down. Only a tenant holding your exact set has nothing left.

@words text="1/120, not 23.3%" sub="the number that matters"
So the risk to quote is one in a hundred and twenty, not the twenty three percent chance of some overlap. Those differ by a factor of twenty eight. And sharing nothing is ninety one times likelier than sharing everything.

@art blast-radius
Now one bad node. It's used by k over n of tenants, an eighth. Each of them loses one node of two and keeps the other. None is down. Same fraction as the fixed layout, entirely different consequence.

@chapter What raising k does
@math heading="n = 24, k = 4" items="C(24, 4) = 10 626 shards@ten thousand six hundred;;P(share none) = 4845/10 626 = 45.596%@share nothing;;P(identical) = 1/10 626 = 0.0094%@collide;;one bad node degrades k/n = 1/6@a sixth"
Raise k and collisions fall hard. At twenty four nodes and four per tenant, there are ten thousand six hundred and twenty six shards. Forty five point six percent share nothing, and two tenants collide with probability one in ten thousand six hundred and twenty six. But each bad node now touches a sixth of tenants.

@art two-levers
Two levers, pulling opposite ways. More nodes per tenant means fewer tenants can take you down, and more tenants feel each failure, each less severely. Quote both numbers in the same sentence.

@chapter A thousand tenants
@math heading="n = 32, k = 4, 1000 tenants" items="C(32, 4) = 35 960@thirty five thousand;;fully down:  999 × 1/35 960 = 0.0278@fully down;;degraded:  999 × 43.06% ≈ 430@degraded"
Thirty two nodes, four per tenant, a thousand tenants. There are thirty five thousand nine hundred and sixty shards. Expected tenants fully down with the poisoned one: point oh two seven eight. Expected degraded: about four hundred and thirty. Fixed shards of four would put a hundred and twenty five tenants fully out.

@chapter Where people slip
@list heading="Common slips" items="Treating any overlap as a shared outage@The first|Quoting collisions without blast radius@The second|Assuming the client uses the survivors@The third"
The first slip is treating any overlap as a shared outage. The second is quoting a collision probability without the blast radius. The third is assuming the client can use the surviving nodes. If requests are pinned to one node, or one node can't carry the load, losing one is an outage. And at k equals one, the distinction disappears.

@chapter Try it
@words text="n = 32, k = 2" sub="C(32, 2) = 496"
Your turn. The operator proposes two nodes per tenant instead of four. Thirty two choose two is four hundred and ninety six. Compute the expected fully down and degraded tenants, and say which column you'd be willing to trade.

@end text="Draw a shuffle, count the overlaps"
You can set n and k, draw an assignment from a seed, and see who shares what, on Learn. That's learn dot get er done dot I O.
