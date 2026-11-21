---
format: long
lesson: latency-and-the-tail/tail-amplification-under-fan-out
title: Tail amplification: when your p99 becomes the median
thumb: 69 calls, half are slow
---

@chapter The question
@title text="Tail Amplification under Fan-out" sub="Latency and the Tail" art=thumb
Every backend meets its latency objective. Every dashboard is green. Nobody gets paged. And still, most of your requests are slow. Nothing is broken. It's arithmetic.

@art fan-out
A search page assembles itself from many services: results, advertisements, spelling, personalisation signals, and a shard of the index for each partition. They run in parallel, which is the right design, so the group costs what the slowest member costs. The question is what the slowest member costs.

@chapter All of them must be fast
@art waiting-for-all
A request that waits for all n calls is fast only if every one of them is fast. That's a conjunction of n separate statements. And if the calls are independent, the probabilities multiply.

@math heading="Fan-out amplification" items="P(all n within their p99) = 0.99ⁿ@nought point nine nine to the n;;P(at least one slow) = 1 − 0.99ⁿ@one minus"
If each call is inside its p ninety nine with probability nought point nine nine, then all n are inside with probability nought point nine nine to the n. And the chance at least one is slow is one minus that.

@art multiplying-chance
Each call on its own looks fine. Nought point nine nine is very close to one. But multiply it by itself enough times, and it sinks.

@chapter The numbers
@math heading="p = 0.99" items="n = 1:  1.00% slow@n equals one;;n = 10:  9.56% slow@n equals ten;;n = 50:  39.50% slow@fifty;;n = 69:  0.99⁶⁹ = 0.499837,  50.02% slow@sixty nine;;n = 100:  63.40% slow@a hundred;;n = 200:  86.60% slow@two hundred"
At n equals one, one percent of requests contain a slow call. At n equals ten, nine point five six percent. At fifty, thirty nine point five. At sixty nine, nought point nine nine to the sixty nine is nought point four nine nine eight three seven, so just over half are slow. At a hundred, sixty three point four. At two hundred, eighty six point six.

@art green-dashboards
At a fan out of sixty nine, the per call p ninety nine has become the whole request's median. Read the hundred row slowly. Every backend is meeting its objective, and sixty three point four percent of requests are waiting on a call outside it. There's no failure to find, because there is no failure.

@chapter What moves the number
@list heading="Break-even fan-out" items="per-call p90 → n = 7@p ninety|per-call p95 → n = 14@p ninety five|per-call p99 → n = 69@p ninety nine|per-call p99.9 → n = 693@p ninety nine point nine"
Where does the break even sit? A per call p ninety breaks even at a fan out of seven. A p ninety five at fourteen. A p ninety nine at sixty nine. And a p ninety nine point nine at six hundred and ninety three. Each factor of ten in the per call tail buys roughly a factor of ten in fan out.

@art fewer-calls
So the strategy space is small. Reduce the fan out. Push the per call tail down by a factor of ten. Or stop requiring every answer: a request that can return with nine of ten results is no longer in this arithmetic at all. Hedged requests are another option, covered in the next lesson.

@math heading="200 shards at a p99.9" items="0.999²⁰⁰ ≈ 0.819@nought point nine nine nine;;18% still slow@eighteen percent;;vs 86.60% at a p99@eighty six point six"
Push every call to a p ninety nine point nine, a real engineering achievement. At a fan out of two hundred, nought point nine nine nine to the two hundred is about nought point eight one nine, so eighteen percent of requests still contain a slow call. Far better than eighty six point six. Not zero, and it never will be.

@chapter Independence
@art clustered-slowness
All of this assumes independence, and reality departs from it in a known direction. Slowness has shared causes: a garbage collection pause on a shared host, a saturated switch, a hot shard. Slow calls arrive together, so fewer requests contain one than the formula says, and those that do contain several.

@chapter Where people slip
@list heading="Common slips" items="Reasoning from one call to the request@The first|Adding the tail probabilities@The second|Forgetting independence is an assumption@The third"
The first slip is reasoning from one call to the request. The second is adding the per call tail probabilities. Ten calls at one percent gives ten percent against the true nine point five six, and at two hundred it gives two hundred percent. And the third is forgetting that independence is an assumption.

@chapter Try it
@words text="fan-out of 40 · per-call p95" sub="a p95 breaks even at n = 14"
Your turn. Take a fan out of forty with a per call p ninety five. A p ninety five breaks even at fourteen, so forty is well past it. Compute nought point nine five to the fortieth and the slow request probability. Then say which per call percentile brings that under ten percent.

@end text="Multiply before you trust a p99"
You can change the fan out and the per call percentile and watch the slow fraction climb, on Learn. That's learn dot get er done dot I O.
