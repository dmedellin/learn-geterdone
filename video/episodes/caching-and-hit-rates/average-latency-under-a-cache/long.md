---
format: long
lesson: caching-and-hit-rates/average-latency-under-a-cache
title: Average latency under a cache: the mean slides, the p99 jumps
thumb: No request takes the mean
---

@chapter The question
@title text="Average Latency under a Cache" sub="Caching and Hit Rates" art=thumb
Put a cache in front of a slow backend, and what's the latency? The honest answer is two numbers, and a third one that no request ever takes.

@art two-clusters
Under a cache, a request has two possible latencies and nothing in between. It's a hit, and fast, or it's a miss, and slow. Everything in this lesson follows from that.

@chapter The weighted mean
@math heading="Two outcomes" items="P(hit) = h  →  t_hit@probability h;;P(miss) = 1 − h  →  t_miss@one minus h;;E[latency] = h·t_hit + (1 − h)·t_miss@the mean"
A request is served in t hit with probability h, and in t miss with probability one minus h. So the mean is h times t hit, plus one minus h times t miss. A weighted average, with the hit rate as the weight.

@art slow-path
One detail. T miss is the whole miss path. The lookup that failed, the backend call, and the write back into the cache. It isn't the backend's service time alone.

@chapter A worked example
@math heading="h = 95%, t_hit = 1 ms, t_miss = 40 ms" items="(19/20)(1) + (1/20)(40)@nineteen twentieths;;= 19/20 + 40/20@which is;;= 59/20 = 2.95 ms@two point nine five"
Take a ninety five percent cache, one millisecond hits, forty millisecond misses. The mean is nineteen twentieths times one, plus one twentieth times forty, which is nineteen twentieths plus forty twentieths. That's fifty nine twentieths, two point nine five milliseconds.

@art balance-beam
Notice where it sits. Close to the hit, because hits are common, and the weighted average is dragged toward whichever outcome happens most. The plain average of one and forty is twenty point five, seven times too large.

@words text="No request takes 2.95 ms"
And here's the odd part. No request takes two point nine five milliseconds. Every one takes one or forty. The mean is a property of the stream, not of any request in it.

@chapter The percentile steps
@art staircase
A percentile asks a different question. It wants a value: the smallest t where the chance of being at most t reaches q. Under a cache, that chance is a staircase with two steps. Zero below the hit latency, h until the miss latency, then one.

@math heading="Ranks at h = 95%" items="q ≤ h  →  t_hit · q > h  →  t_miss@the rule;;p50:  19/20 ≥ 1/2  →  1 ms@the median;;p95:  19/20 ≥ 19/20  →  1 ms@the p ninety five;;p99:  19/20 < 99/100  →  40 ms@the p ninety nine;;p99.9:  19/20 < 999/1000  →  40 ms@and the p ninety nine point nine"
The rule is simple. If q is at most h, the percentile is the hit latency. Otherwise it's the miss. So the median is one millisecond, and so is the p ninety five, because the boundary belongs to the hit. But the p ninety nine is forty, and the p ninety nine point nine is forty.

@chapter Where each percentile flips
@art flip-point
Each percentile flips at exactly h equals q. Improve the cache from ninety five to ninety eight point nine percent, and the p ninety nine doesn't move at all. Then one more tenth of a point moves it by thirty nine milliseconds.

@math heading="Three hit rates" items="h = 95%:  mean 2.95 ms · p99 = 40 ms@ninety five percent;;h = 99%:  mean 139/100 = 1.39 ms · p99 = 1 ms · p99.9 = 40 ms@ninety nine percent;;h = 99.9%:  mean 1039/1000 = 1.039 ms · p99.9 = 1 ms@ninety nine point nine"
At ninety five percent, the mean is two point nine five and the p ninety nine is forty. At ninety nine percent, the mean is one point three nine, the p ninety nine has just become one, but the p ninety nine point nine is still forty. At ninety nine point nine, the mean is one point oh three nine and that tail flips too.

@art tail-unchanged
So a cache is a good answer to a throughput problem and a poor one for the tail. The slow requests it leaves behind are exactly as slow as they were. To move the tail, you move t miss, or push h past the percentile you care about.

@chapter Where people slip
@list heading="Common slips" items="Averaging the two latencies@The first|Assuming a 99% cache fixes every tail@The second|Expecting the tail to improve gradually@The third"
The first slip is averaging the two latencies instead of weighting them. The second is thinking a ninety nine percent hit rate fixes the tail. It fixes the p ninety nine, but the p ninety nine point nine stays at the miss latency. The third is expecting the tail to improve gradually. A flat p ninety nine graph isn't broken. That's the shape.

@chapter Try it
@words text="t_hit = 2 ms · t_miss = 120 ms · h = 99%" sub="mean = (99/100)(2) + (1/100)(120)"
Your turn. Two millisecond hits, a hundred and twenty millisecond misses, a ninety nine percent hit rate. Finish the mean. Then find the smallest hit rate, in tenths of a percent, where the p ninety nine point nine becomes the hit latency, and say which percentile you haven't moved.

@end text="Slide the hit rate, watch the tail jump"
You can drag the hit rate across the staircase and watch the mean slide while the p ninety nine sits still, on Learn. That's learn dot get er done dot I O.
