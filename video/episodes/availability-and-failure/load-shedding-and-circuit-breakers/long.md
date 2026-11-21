---
format: long
lesson: availability-and-failure/load-shedding-and-circuit-breakers
title: Load shedding: say no to more traffic, serve more users
thumb: Refuse 55%, serve 1.8×
---

@chapter The question
@title text="Load Shedding" sub="Availability and Failure" art=thumb
Your service gets twice the traffic it can handle. Should it try to serve everyone, or turn some away? Turning people away sounds worse. It isn't. The service that says no serves almost twice as many users.

@art abandoned-work
Above capacity, a server spreads its work across more requests than it can finish before clients give up. Work spent on a request whose client has already left is work lost.

@chapter Goodput under collapse
@math heading="Capacity C, offered load L" items="L ≤ C:  goodput = L@at or below;;L > C:  only C/L complete in time@above capacity;;goodput = C × (C/L) = C²/L@goodput is"
Goodput is the rate of requests that are served and still wanted. At or below capacity, goodput equals the load. Above capacity, only C over L of the requests complete in time, so goodput is C times C over L. C squared over L. It falls as load rises.

@words text="C = 1000 rps" sub="2000 → 500/s · 4000 → 250/s"
So a thousand request a second service, offered two thousand, delivers five hundred. Offered four thousand, two hundred and fifty. More traffic, fewer users served.

@chapter Shedding
@art door-cap
A shedder with threshold T admits the smaller of L and T, and puts that through the same model. Below the threshold, nothing changes. Above it, goodput is flat at T, as long as T is at or below capacity.

@list heading="C = 1000, T = 900" items="100%:  900 vs 1000 · 0.90@a hundred percent|150%:  900 vs 666.7 · 1.35@a hundred and fifty|200%:  900 vs 500 · 1.80@twice capacity|400%:  900 vs 250 · 3.60@four times"
With a threshold of nine hundred, there's exactly one place shedding costs you. At a hundred percent load, it delivers nine hundred instead of a thousand. At a hundred and fifty percent, it wins, nine hundred against six sixty seven. At twice capacity, one point eight times. At four times, three point six.

@art two-curves
So the cost is bounded by C minus T, a hundred a second, in a band the system passes through. Everywhere above capacity, shedding wins, and the margin grows without limit.

@chapter Where to put the threshold
@math heading="T = 120% of C, L = 200%" items="admits 1200/s, more than C@admits;;goodput = 1000²/1200 = 833.3/s@eight hundred and thirty three"
Why not set the threshold above capacity? Try a hundred and twenty percent at twice capacity. The shedder admits twelve hundred, which the server can't serve, so goodput is a thousand squared over twelve hundred, eight hundred and thirty three. Better than five hundred, worse than nine hundred.

@art queue-overflow
The real product is utilisation. With the shedder it's point nine. Without it, two. A utilisation above one isn't a state, it's a queue growing without bound. So place the threshold a little under capacity, as insurance against a wrong estimate of C.

@chapter Rejection defends availability
@math heading="200% offered" items="no shedding:  500 of 2000 = 25%@unshed;;shedding:  900 of 2000 = 45%@shed;;failures:  1500 timeouts vs 1100 fast rejections@timeouts"
At twice capacity, the unshed service succeeds on five hundred of two thousand, twenty five percent. The shed service succeeds on nine hundred, forty five percent. And by the error budget, it fails fewer requests: eleven hundred immediate rejections against fifteen hundred timeouts a second.

@art circuit-breaker
A circuit breaker is the same arithmetic, with the client doing the refusing. After enough failures, the client stops calling for a while and fails fast locally. The rejected request never crosses the network. But the client is deciding on stale evidence about a service it's stopped watching.

@chapter Where people slip
@list heading="Common slips" items="Believing rejection lowers availability@The first|Setting the threshold from peak throughput@The second|Rejecting expensively or illegibly@The third"
The first slip is believing rejection lowers availability. The second is setting the threshold from the maximum throughput ever seen, which was measured inside the collapse. Measure the knee. The third is rejecting expensively, or in a way the client can't tell from a timeout, so it retries at once.

@art knee-mark
So measure where latency turns up, and set the threshold just below that. Response time is already rising steeply as utilisation nears one, so the ten percent you give up is cheap insurance, and it's paid in a region you pass through, not one you sit in.

@chapter Try it
@words text="C = 1200 · T = 1080 → 1200?" sub="what if true capacity is 1100?"
Your turn. A service with a knee at twelve hundred sheds at ten eighty. The team wants the threshold at exactly twelve hundred. Work out the goodput under both thresholds if the true capacity is really eleven hundred, and say where the ten percent was going.

@end text="Raise the load, watch the two curves part"
You can move the threshold and the offered load and compare goodput with and without shedding, on Learn. That's learn dot get er done dot I O.
