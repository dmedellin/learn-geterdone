---
format: long
lesson: caching-and-hit-rates/cache-stampedes
title: Cache stampedes: the moment your cache isn't there
thumb: 500 requests, one key
---

@chapter The question
@title text="Cache Stampedes" sub="Caching and Hit Rates" art=thumb
Your cache has a ninety nine point nine percent hit rate. Your backend falls over anyway. Here's how that happens, and the one number that predicts it.

@art expiry-gap
A hot key expires. The next request misses and starts a refill. Until that refill lands, every request for the key also finds nothing, also misses, and is also sent to the backend. For those few milliseconds, there is no cache.

@chapter The miss window
@words text="miss window d" sub="backend call + write back"
Call that gap the miss window, d. It's the time from detecting a miss to having the refilled value ready to serve, so the backend call plus the write back.

@math heading="The stampede" items="stampede = λ_key · d@a rate times a time;;λ_key = the one key's read rate@the one key;;50 000 rps · 10% hottest  →  λ_key = 5 000@fifty thousand"
How many requests pile in? It's a rate times a time, which is Little's Law. Lambda key times d. And lambda key is the read rate of the one key, not the service. A service at fifty thousand requests a second whose hottest key takes ten percent has lambda key of five thousand.

@art same-burst
Here's the uncomfortable part. That formula doesn't mention the hit rate, the cache size, or the policy. Those describe steady state. This is a transient. A ninety nine point nine percent cache has exactly the same stampede as a fifty percent one, for the same key.

@chapter A hot key
@math heading="λ_key = 5 000/s, d = 100 ms" items="5 000 × 0.1 = 500 requests@five thousand times;;backend holds 200 concurrent fills@two hundred;;500/200 = 5/2 = 2.50×@two and a half"
Take five thousand reads a second and a hundred millisecond fill. Five thousand times point one is five hundred requests. Against a backend that holds two hundred concurrent fills, that's five halves, two and a half times its capacity. What it can't take either queues or fails.

@list heading="The same key, other fills" items="1 ms  →  5@one millisecond|500 ms  →  2 500@five hundred milliseconds|2 s  →  10 000@two seconds"
It scales linearly. A one millisecond fill sends five requests through. Five hundred milliseconds sends two thousand five hundred. Two seconds, ten thousand. And a slow fill is exactly what happens when the backend is already struggling. That's a feedback loop.

@chapter Fixes that aren't
@list heading="Not fixes" items="A bigger cache@A bigger cache|A longer TTL@A longer TTL|A higher hit rate@a higher hit rate"
A bigger cache doesn't help. The key was in the cache, and the problem is the moment it left. A longer TTL makes the expiry rarer, not smaller. And a higher hit rate is an average over a window that contains this one, and the average is fine.

@chapter Fixes that are
@art single-flight
Coalescing, also called single flight, makes one request per key reach the backend, and parks the rest on its result. Without it, lambda key times d requests go through. With it, exactly one. So the reduction factor is lambda key times d itself, five hundred here.

@art early-refresh
Early refresh goes further. A request arriving near the end of a TTL refreshes the entry while the old value keeps being served. That removes the window altogether, at the cost of a little more staleness.

@chapter Many keys at once
@art synced-expiry
The version that takes systems down is many keys at once. A fleet that sets the same TTL on everything at deploy time expires everything together. K hot keys each send their burst in the same window. Coalescing still cuts it to k, one per key. And jittering the TTLs spreads them out. That's the cheapest fix of all.

@art capacity-line
One limit. Lambda times d assumes the backend keeps accepting arrivals. A backend that starts queueing makes d longer, which lets more requests in, which makes d longer still. The formula gives the first step of that loop, and the first step is already enough to size the problem.

@chapter Where people slip
@list heading="Common slips" items="Believing a cache always protects the backend@The first|Using the service's rate instead of the key's@The second|Reaching for a longer TTL@The third"
The first slip is believing a cache always protects the backend. It does in steady state, not in the miss window. The second is using the service's rate instead of the key's. The third is reaching for a longer TTL, which doesn't make the burst any smaller.

@chapter Try it
@words text="20 000 rps · hottest key 10% · d = 50 ms" sub="capacity 200 · λ_key = 2 000"
Your turn. Twenty thousand requests a second, the hottest key is ten percent, so lambda key is two thousand. The fill takes fifty milliseconds and the backend holds two hundred. Find the burst and its ratio to capacity, then the ratio if twelve hot keys expire together. Which fix would you reach for first?

@end text="Expire more keys, watch the burst"
You can raise the number of keys expiring together and watch the burst outgrow the backend, on Learn. That's learn dot get er done dot I O.
