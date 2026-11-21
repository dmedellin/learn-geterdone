---
format: long
lesson: queues-and-utilisation/token-buckets-and-rate-limiting
title: Token buckets and rate limiting: a promise about every window
thumb: Advertised 5, delivered 9
---

@chapter The question
@title text="Token Buckets and Rate Limiting" sub="Queues and Utilisation" art=thumb
Your rate limiter says five requests a second. On one trace, it let nine through in a single second. Nothing was misconfigured. It was the kind of limiter that only keeps its promise on some windows.

@art bucket-refill
A token bucket has a capacity b and refills at r tokens per unit time. Between two arrivals, the level rises by r times the gap, and is then capped at b. An arrival is admitted if at least one whole token is present, and spends it. Otherwise it's rejected, and the level is unchanged.

@chapter The guarantee
@math heading="Over any window of length t" items="admitted ≤ b + r·t@at most b plus;;r = 5/s,  b = 3  →  at most 8 in any second@five a second"
Over any window of length t, admissions are at most b plus r times t: the tokens in the bucket at the start, plus the tokens that arrived during the window. With five a second and b of three, no second anywhere in any trace carries more than eight.

@art rejected-arrivals
That bound holds for every window. Not just aligned ones, and not on average. Every admission consumed a token, and the starting level was capped at b. That's the whole reason a bucket is used.

@chapter Twenty arrivals
@words text="20 arrivals over 2.2 s · bunched at 900 ms and 1000 ms"
Here's the lesson's trace: twenty arrivals over two point two seconds, bunched up at nine hundred and a thousand milliseconds. Run it through a bucket, and then through a fixed window with the same limit.

@math heading="Same trace, two limiters" items="bucket: admitted 13, rejected 7,  worst second 7  (bound 8)@the bucket;;fixed window: admitted 12, rejected 8,  worst second 9  (advertised 5)@the fixed window"
The bucket admits thirteen and rejects seven, and its worst second is seven, under its own bound of eight. The fixed window admits twelve and rejects eight. But its worst second is nine, while advertising five.

@art window-boundary
How? The fixed window counts to its limit and resets at each boundary. It admitted four late in the first window, then five more the instant the counter reset. A client straddling the boundary gets up to twice the advertised rate in one window's width.

@chapter What downstream sees
@art downstream-burst
The number that matters to whatever sits behind the limiter is the worst second, not the total. That's what sets the queue of the earlier lessons. A limiter advertising five that delivers nine has sized the downstream headroom wrong by nearly two times. A bucket's worst case is b plus r t, a number you chose.

@chapter The cap is the point
@art capped-level
With one token a second and b of three, a bucket left alone for twenty seconds holds three tokens, not twenty. So seven arrivals at once see three admitted and four refused. The cap makes b a burst allowance, not a savings account. Without it, a quiet night would pay for an unbounded morning.

@list heading="Two separate choices" items="r: the sustained rate downstream can carry@the sustained rate|b: how much bunching you'll pass through@how much bunching"
So choosing the parameters is two separate questions. r is the sustained rate the downstream system can carry, a capacity question. b is how much bunching you're willing to pass through at once, and its cost is paid by the queue behind it.

@art shaper
Rate limiting is loss, not delay. A rejected request is refused immediately, which is an honest failure a client can retry, with jitter. Or run the bucket as a shaper, holding arrivals until a token appears, which turns the same bound back into waiting.

@chapter Where people slip
@list heading="Common slips" items="A fixed window as a per-second promise@The first|Letting tokens exceed b@The second|Sizing downstream for r, not b + r@The third"
The first slip is reading a hundred per second on a fixed window as at most a hundred in any second. The second is letting the token level exceed b. And the third is sizing the downstream system for r rather than b plus r, leaving it exposed to exactly the bursts you permitted.

@chapter Try it
@words text="same trace · b = 1" sub="bound: 1 + 5 = 6 per second"
Your turn. Keep the trace, and set b to one. The bound becomes one plus five, six per second. Predict whether the total admitted goes up or down, and what happens to the largest second.

@end text="Choose r, choose b, keep the promise"
You can run the trace through a bucket and a fixed window side by side, on Learn. That's learn dot get er done dot I O.
