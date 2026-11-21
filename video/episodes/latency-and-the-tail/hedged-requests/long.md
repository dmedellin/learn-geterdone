---
format: long
lesson: latency-and-the-tail/hedged-requests
title: Hedged requests: cut the p99 for five percent more load
thumb: Square the tail
---

@chapter The question
@title text="Hedged Requests" sub="Latency and the Tail" art=thumb
Your service has a median of twelve milliseconds and a p ninety nine of a hundred and twenty. Nothing is broken. That's an ordinary shape. Can you cut the tail without making the service itself any faster?

@art hedge-timeline
You can, by hedging. Send the request. If it hasn't answered by some delay d, send a second copy and take whichever returns first. The request is slow only if both copies are slow.

@words text="finish = min(X, d + Y)" sub="X and Y independent draws"
The hedged request finishes at the smaller of X, and d plus Y, where X and Y are independent draws from the same latency distribution.

@chapter The service
@list heading="A hundred measured calls" items="40 at 10 ms · 25 at 12 ms · 15 at 15 ms@forty at ten|10 at 20 ms · 5 at 30 ms@ten at twenty|3 at 50 ms · 1 at 120 ms · 1 at 300 ms@three at fifty"
Here's the lab's service: a hundred calls. Forty at ten milliseconds, twenty five at twelve, fifteen at fifteen. Ten at twenty, five at thirty. Three at fifty, one at a hundred and twenty, and one at three hundred. Its median is twelve, its p ninety five is thirty, and its p ninety nine is a hundred and twenty.

@chapter The tail factorises
@math heading="Hedge at d" items="P(hedged > t) = P(X > t) · P(X > t − d)@the first copy;;extra load = P(X > d)@the extra load"
The hedged request exceeds t only if the first copy is still running at t, and the second copy, which started at d, is still running too. They're independent, so the probabilities multiply. And the extra load is the chance a request lives past d, because only those trigger a copy.

@math heading="d = 30 ms, the p95" items="extra load = 5/100 = 5.0%@five percent;;t = 42:  (1/20)(7/20) = 7/400@forty two;;t = 45:  (1/20)(1/5) = 1/100@forty five;;hedged p99 = 45 ms, was 120 ms@a hundred and twenty"
Hedge at thirty milliseconds, the p ninety five. The extra load is five percent. At forty two milliseconds, the tail is one twentieth times seven twentieths, seven over four hundred. At forty five, it's one twentieth times one fifth, exactly one in a hundred. So the hedged p ninety nine is forty five, down from a hundred and twenty.

@art tail-squared
That's a sixty two percent cut in the p ninety nine for five percent more traffic. Just past the delay, the tail is roughly squared: one in twenty becomes one in four hundred. It's the same multiplication rule that made fan out hurt, working for you this time.

@words text="p50: 12 ms → 12 ms"
And the median doesn't move at all. Ninety five percent of requests never reach the delay. A hedge doesn't make a service faster. It makes it less occasionally awful.

@chapter Choosing the delay
@art delay-dial
The delay is the one knob you choose. Move it earlier and more requests trigger a copy. Move it later and fewer do, but each copy has less time to help.

@math heading="Delay against cost" items="d = 12 ms (median):  +35.0% load,  p99 30 ms@the median;;d = 20 ms:  +10.0%,  p99 35 ms@twenty;;d = 30 ms (p95):  +5.0%,  p99 45 ms@thirty;;d = 50 ms:  +2.0%,  p99 62 ms@fifty;;d = 120 ms (p99):  +1.0%,  p99 120 ms@the p ninety nine"
At the median, the load goes up thirty five percent and the p ninety nine is thirty. At twenty, ten percent and thirty five. At thirty, five percent and forty five. At fifty, two percent and sixty two. And hedging at the p ninety nine costs one percent and achieves nothing.

@art load-spike
Hedging at the median buys fifteen more milliseconds and costs seven times the traffic. Around the p ninety five is where the curve bends. And the load isn't free. At forty thousand requests a second, five percent is two thousand extra calls a second, arriving exactly when the service is struggling.

@chapter When it buys nothing
@art same-replica
Every number here assumes the second copy is independent. If the call is slow because the request is expensive, a large query or a cold cache entry, the second copy is just as slow. And sending it to the same replica makes the two copies the same draw. Hedge to a different replica, or the arithmetic means nothing.

@art different-replica
Independence is plausible when the slowness belongs to the server: a garbage collection pause, a scheduling delay, a disk that's briefly busy. It's implausible when the slowness belongs to the request.

@chapter Where people slip
@list heading="Common slips" items="Hedging near the median@The first|Assuming independence@The second|Treating the load as free@The third"
The first slip is hedging near the median, reading only the number that improved. The second is assuming independence when the request carries the slowness. And the third is treating the extra load as free because it's small.

@chapter Try it
@words text="d = 20 ms" sub="extra load: (5 + 3 + 1 + 1)/100 = 10.0%"
Your turn. Same service, delay twenty milliseconds. The extra load is ten percent. Find the hedged p ninety nine by walking upward from twenty, and say whether doubling the load from the p ninety five choice was worth it.

@end text="Read both numbers before you hedge"
You can slide the hedge delay and watch the load and the p ninety nine trade off, on Learn. That's learn dot get er done dot I O.
