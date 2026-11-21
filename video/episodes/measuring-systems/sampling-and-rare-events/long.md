---
format: long
lesson: measuring-systems/sampling-and-rare-events
title: One percent sampling misses rare problems nine times in ten
thumb: 1% sampling, 9.56% caught
---

@chapter One percent of what?
@title text="Sampling and Rare Events" sub="Measuring Systems" art=thumb
You sample one request in a hundred. A customer reports ten slow requests. What are the chances any of them is in your store? About one in ten.

@art sparse-sample
Under uniform sampling at rate s, each request is kept independently with probability s. A problem that produces k requests is captured if at least one is kept.

@math heading="Capture" items="P(caught) = 1 − (1 − s)ᵏ@one minus;;s = 1/100,  k = 10:  (99/100)¹⁰ = 0.9044@ninety nine hundredths;;caught 9.56%,  missed 90.44%@nine point five six"
The chance of missing all k is one minus s, to the k. The chance of catching at least one is one minus that. At one percent and ten requests, ninety nine hundredths to the tenth is point nine oh four four. So it's caught nine point five six percent of the time, and missed ninety point four four.

@art miss-probability
One percent sampling sees one percent of the totals over millions of requests. For one incident, it gives a tenth of an expected capture, which means, almost always, none at all.

@words text="1 − e^(−sk) = 9.516%" sub="a rule of thumb, not the exact 9.562%"
There's a rule of thumb, one minus e to the minus s k, nine point five one six percent. It's an approximation, out by point oh four five percentage points. That's a different kind of wrong from rounding, and computing harder won't shrink it.

@chapter The rate confidence needs
@art capture-curve
Turn it round. For ninety five percent confidence on a ten request problem, find the smallest s where one minus one minus s to the tenth clears ninety five percent. The lab scans the thousandths.

@math heading="k = 10" items="s = 5%:  40.13%@five percent;;s = 10%:  65.13%@ten percent;;s = 25%:  94.37%@twenty five percent;;s = 25.9%:  95.01%  first to clear@twenty five point nine"
Five percent sampling gives forty point one three. Ten percent, sixty five point one three, better than a coin toss and not a guarantee. Twenty five percent, ninety four point three seven, still short. Twenty five point nine is the first to clear it.

@words text="26× the rate for 10× the confidence"
So going from nine point five six to ninety five percent takes twenty six times the rate, not ten. What scales cleanly is the miss probability, and you have to halve it four times over.

@chapter Sample the tail instead
@art tail-keep
If a problem must be visible whenever it happens, uniform sampling is the wrong tool. Keep every request slower than a threshold, and sample the rest. Now every slow request survives.

@math heading="900 × 5 ms,  60 × 8,  30 × 12,  10 × 400" items="true mean = 9 340 / 1 000 = 9.34 ms@nine point three four;;keep all ≥ 100 ms, 1% of the rest@keep all;;naive mean = 4 053.4 / 19.9 = 203.69 ms@two hundred and three"
But that breaks the average. Take a thousand requests with a true mean of nine point three four milliseconds. Keep all ten slow ones, and one percent of the fast ones. The naive mean of what's kept is two hundred and three point six nine milliseconds, twenty one point eight times the truth.

@art skewed-average
The kept set over represents the tail by a factor of one over s. Any plain statistic on it describes a population that was never served.

@words text="One pipeline, two failures"
That's the same decision seen from both ends. Sample uniformly, and nobody finds the customer's ten slow requests. Keep the tail, and a week later a dashboard on the same store reports a mean of two hundred and three milliseconds, and someone declares an incident about a healthy service.

@chapter Reweighting
@art reweight
The repair is to count each kept request one over its own keep probability. Slow ones count once, fast ones a hundred times. Nine thousand three hundred and forty over a thousand, nine point three four, exactly. Not an approximation. That only works if the rate travels with the data.

@chapter Where people slip
@list heading="Common slips" items="Reading the rate as the share of a problem you'll see@The first|Scaling the rate linearly with confidence@The second|Averaging a deliberately biased sample@the third"
The first slip is reading the sampling rate as the share of a problem you'll see. The second is scaling the rate linearly with the confidence you want. And the third is averaging a deliberately biased sample without reweighting.

@chapter Try it
@words text="k = 40,  s = 1%" sub="first move: (99/100)⁴⁰"
Your turn. Take a problem of forty requests at one percent. Start from ninety nine hundredths to the fortieth. Work out the capture probability, then the rate that reaches ninety five percent, and say why it's so much smaller than twenty five point nine.

@end text="Carry the rate with the data"
You can move the rate and the problem size and watch the capture probability, on Learn. That's learn dot get er done dot I O.
