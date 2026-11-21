---
format: long
lesson: partitioning-and-load-balancing/scatter-gather-cost
title: Scatter-gather: the query that asks every shard
thumb: Times N requests, max of N waits
---

@chapter The unroutable query
@title text="Scatter-Gather Cost" sub="Partitioning and Load Balancing" art=thumb
Some queries name the partition key and go straight to one shard. Others can't, so they ask every shard and wait for the last answer. That second kind costs you twice.

@art routed-one
A routed query names the partition key and goes to one shard.

@art scatter-fan
A scatter gather query has a predicate that doesn't decide the shard, so the router sends it to all N shards, the scatter, and combines the partial results, the gather.

@art key-choice
Which queries can be routed depends only on the partitioning function. Partition by user, and everything for user ninety one is routed, while everything created yesterday is a scatter. Partition by day, and they swap. So the choice belongs with the access patterns.

@chapter Cost one: requests
@math heading="N = 24,  400 queries /s" items="shard requests = 24 × 400 = 9 600 /s@nine thousand six hundred;;routed instead = 400 /s@four hundred;;amplification = 24×@twenty four times"
Take twenty four shards and four hundred client queries a second. The shards receive twenty four times four hundred, nine thousand six hundred requests a second. Routed, it'd be four hundred. The amplification is twenty four times.

@art request-multiplier
That's the figure that surprises people. Each node does less work per query, true. But each node receives N times as many queries. So everything priced per request, a connection, a lock, a log line, a tracing span, is multiplied by twenty four.

@chapter Cost two: the tail
@math heading="Per-shard latency, weights of 100" items="10:80   25:15   90:4   250:1@ten milliseconds;;mean = 8 + 3.75 + 3.6 + 2.5 = 17.85 ms@seventeen point eight five;;P(shard ≤ 90) = 0.99,  so p99 = 90 ms@ninety milliseconds"
Now latency. Each shard answers in ten milliseconds eighty times in a hundred, twenty five, fifteen times, ninety, four times, and two hundred and fifty, once. The mean is seventeen point eight five milliseconds, and one shard's p ninety nine is ninety milliseconds.

@art slowest-answer
But the query waits for the slowest shard. It's fast only if all twenty four were fast.

@math heading="The query over 24 shards" items="P(query ≤ 90) = 0.99²⁴ = 0.7857@to the twenty fourth;;p99 = 250 ms@two hundred and fifty;;N = 2:  0.99² = 0.9801 < 0.99@just two shards"
Point nine nine to the twenty fourth is point seven eight five seven, well below point nine nine. So the query's p ninety nine is two hundred and fifty, the worst outcome a shard has. And it gets there at just two shards, because point nine nine squared is point nine eight oh one.

@words text="The tail cost starts at the second shard"
So this isn't a big cluster problem. The per shard distribution never changed. The query is just asking more shards to all be fast at once. A seeded run of four hundred queries reports two hundred and fifty as well.

@chapter Cost three: consumers
@art consumer-ceiling
There's a third effect. A partition is also the unit of parallel consumption. A downstream reader can't use more than N workers, because worker N plus one has no partition to read. At twenty four, the ceiling is twenty four, however much hardware you have. So a count chosen for storage and load has also capped a pipeline nobody in that conversation was thinking about. And raising it later means a rehash, which moves nearly every key.

@chapter What to do instead
@list heading="Better than raising N" items="Make the query routable@make the query routable|Narrow the per-shard tail@narrow the per shard tail|Accept a partial result, or hedge@accept a partial"
The direct fix is to make the query routable, usually with another copy of the data partitioned on the attribute it filters by. Otherwise, narrow the per shard tail, accept a partial result, or hedge. What doesn't help is raising N, which makes both costs worse.

@chapter Where people slip
@list heading="Common slips" items="Costing capacity but not latency, or the reverse@The first|Expecting the tail only at large fleets@The second|Raising N to speed up a scatter@the third"
The first slip is costing the fan out for capacity and not for latency, or the reverse. Nine thousand six hundred a second and two hundred and fifty milliseconds come from the same N. The second is expecting the tail cost only at large fleets. And the third is raising the shard count to speed up a scatter gather.

@chapter Try it
@words text="24 shards,  10:80 · 25:16 · 90:4" sub="first move: per-shard p99 is still 90 ms"
Your turn. Keep twenty four shards and remove the two hundred and fifty millisecond outcome: ten at eighty, twenty five at sixteen, ninety at four. One shard's p ninety nine is still ninety. Work out the query's p ninety nine, say how much the request rate changed, and which of the two costs that fix addressed.

@end text="Two costs, one dial"
You can move the shard count and watch both costs, on Learn. That's learn dot get er done dot I O.
