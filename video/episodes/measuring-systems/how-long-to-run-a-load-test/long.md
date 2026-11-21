---
format: long
lesson: measuring-systems/how-long-to-run-a-load-test
title: Your one minute load test didn't see its own p99.9
thumb: 2 995 requests, at least
---

@chapter A quick check
@title text="How Long to Run a Load Test" sub="Measuring Systems" art=thumb
A quick load test: ten requests a second for a minute, six hundred requests. The report has a p ninety nine point nine in it. More than half the time, that number came from a run that never saw the top tenth of a percent at all.

@art short-run
Each request is in the slowest t fraction with probability t, independently. For the p ninety nine point nine, t is one in a thousand.

@math heading="Meeting the tail" items="P = 1 − (1 − t)ⁿ@one minus;;n = 600:  1 − (999/1000)⁶⁰⁰ = 45.14%@six hundred;;expected in the tail:  600 × 1/1000 = 0.6@point six"
So a run of n requests meets that tail at least once with probability one minus one minus t, to the n. At six hundred, that's forty five point one four percent. Worse than a coin toss. You'd expect point six requests in the tail.

@art max-label
And the tool still reports a number. Rank point nine nine nine times six hundred, rounded up, is six hundred. That's the maximum of the run, with a label on it. Ask for the p ninety nine point nine, the p ninety nine point nine nine, and the maximum, and if they're all the same number, the run is too short.

@chapter How long is enough?
@math heading="t = 1/1000" items="even chance:  n = 693@six hundred and ninety three;;95%:  n = 2 995@two thousand nine hundred and ninety five;;n = 2 994 → 0.050012…  short,   n = 2 995 → 0.049962…@two thousand nine hundred and ninety four"
An even chance needs six hundred and ninety three requests. Ninety five percent confidence needs two thousand nine hundred and ninety five. At two thousand nine hundred and ninety four, the miss probability is still just above one twentieth. At two thousand nine hundred and ninety five, it clears.

@words text="Scan exact fractions, don't take a log"
The lab finds that by scanning exact fractions, not by taking a logarithm. Nine nine nine over a thousand to the two thousand nine hundred and ninety fifth has a numerator about nine thousand digits long. A floating point number can't hold it. A scan can, and it shows both sides of the boundary.

@art long-run
And six hundred and ninety three should look familiar. It's the same break even as tail amplification under fan out. Same equation, point nine nine nine to the n equals a half.

@chapter Meeting is not measuring
@art meet-curve
Even ninety five percent only says the tail was met once. The p ninety nine point nine is then estimated from one or two observations, and the next run will give a different value.

@art ten-in-tail
As a working rule, ask for ten samples in the tail. That's ten over t, ten thousand requests for a p ninety nine point nine, and a hundred thousand for a p ninety nine point nine nine.

@math heading="At 10 requests a second" items="693 → 69 s@sixty nine seconds;;2 995 → 5 min@five minutes;;10 000 → 17 min@seventeen minutes"
At ten requests a second, six hundred and ninety three takes sixty nine seconds. Two thousand nine hundred and ninety five takes five minutes. Ten thousand takes seventeen minutes. That's less time than people usually spend arguing about the meaningless one.

@chapter One distribution?
@art ramp-and-warm
All of this assumes every request is an independent draw from one distribution. A ramp, a cold cache, or a run that fits inside one garbage collection cycle breaks that. Discard the ramp, warm the system, and run for several of whatever cycle it has.

@chapter Where people slip
@list heading="Common slips" items="Believing a one-minute run showed the p99.9@The first|Confusing meeting a tail with measuring it@The second|Reading run-to-run noise as a change@the third"
The first slip is believing a one minute run showed you the p ninety nine point nine. The second is confusing meeting a tail with measuring it. And the third is reading run to run variation in a deep percentile as a change in the system. Check n times t for both runs first.

@chapter Try it
@words text="p99.99 at 95% confidence" sub="first move: t = 1/10000"
Your turn. Size a run that reports a p ninety nine point nine nine at ninety five percent confidence. T is one in ten thousand, so n will be about ten times the last answer. Predict it, find it by the scan, and work out how long it takes at a hundred requests a second.

@end text="Size the run before you run it"
You can move the percentile and the run length and watch the chance of meeting the tail, on Learn. That's learn dot get er done dot I O.
