---
format: long
lesson: measuring-systems/percentiles-do-not-average
title: Percentiles don't average: the dashboard p99 that's below the median
thumb: Merge, then take the percentile
---

@chapter One definition
@title text="Percentiles Do Not Average" sub="Measuring Systems" art=thumb
Your dashboard shows a fleet p ninety nine. It's the average of each host's p ninety nine. That number isn't a percentile of anything, and on the example in this lesson, it's below the median.

@art merge-sample
A fleet percentile is the percentile of the merged sample. Sort every request the fleet served, and take the one at position q times n, rounded up. One definition, applied once, and every request counts once.

@chapter Three hosts
@art three-hosts
Here are three hosts. Host A served five requests, eight to twelve milliseconds. Host B, five requests, ten to fourteen. Host C carries the traffic, ninety requests, from a hundred and fifty up to four hundred milliseconds.

@math heading="Per host, nearest rank at q = 0.99" items="A:  rank 5 of 5  →  12 ms@twelve;;B:  rank 5 of 5  →  14 ms@fourteen;;C:  rank 90 of 90  →  400 ms@four hundred;;mean = (12 + 14 + 400)/3 = 142 ms@a hundred and forty two"
Per host, at ninety nine percent: A's p ninety nine is twelve. B's is fourteen. C's is four hundred. Average them, and you get a hundred and forty two milliseconds.

@math heading="Merged,  n = 100" items="fleet p99:  rank 99  →  400 ms@rank ninety nine;;fleet p50:  rank 50  →  180 ms@rank fifty"
Now merge all hundred requests. Rank ninety nine is four hundred milliseconds. That's the fleet p ninety nine. And rank fifty, the median, is a hundred and eighty.

@words text="142 < 180" sub="the average p99 is below the median"
So the number presented as the slowest one percent is smaller than the number half of all requests beat. It's not a slightly optimistic p ninety nine. It's below the middle.

@art votes-vs-requests
Here's the mechanism. The average weights hosts. The fleet percentile weights requests. Host C served ninety of the hundred, but in the average it gets one vote of three. Two hosts with a tenth of the traffic drag it down.

@chapter Why nobody notices
@art bounded-range
There's a bound. The fleet percentile always lies between the smallest and largest per host percentile. If every host reports the same p ninety nine, the fleet's is exactly that. And the average lies inside the range too. So the wrong number is never absurd, which is exactly why it survives review.

@chapter The summaries aren't enough
@words text="Host p99s 40 and 100 ms" sub="fleet p99: 50 ms in one fleet, 100 ms in another"
Worse, the per host percentiles don't decide the fleet percentile. Here are two fleets, each with two hosts of a hundred requests, and host p ninety nines of forty and a hundred in both. In one fleet, the merged p ninety nine is fifty. In the other, it's a hundred. The average, seventy, describes neither.

@art merge-histograms
So keep something mergeable. Counts and sums add. A histogram of counts per bucket adds bucket by bucket, and you read the percentile off the merged histogram. It gives an interval, not a point. An interval that contains the answer beats a point that doesn't. And if you only have per host percentiles, report the range between the smallest and the largest, as a range.

@art average-summaries
Most panels that plot one line per host and then apply an aggregation are averaging percentiles by default. Find that setting before you quote the number in an incident review, and write the answer in the panel description so nobody has to look again.

@chapter Where people slip
@list heading="Common slips" items="Averaging the per-host percentiles@The first|Taking the max of the per-host p99s as the answer@The second|Quoting a p99 from five requests@the third"
The first slip is averaging the per host percentiles, usually done by a dashboard's default aggregation. The second is taking the maximum as the fleet p ninety nine. It's an upper bound, and in the two host example it's out by a factor of two. And the third is quoting a p ninety nine from five requests.

@words text="⌈0.99 × 5⌉ = 5 of 5" sub="the maximum, relabelled"
On a five request host, rank five of five is just the maximum, relabelled. Two of the three numbers being averaged here were maxima of tiny samples.

@chapter Try it
@words text="C: 30 requests,  A and B: 35 each" sub="first move: host p99s barely change"
Your turn. Keep the three samples, but give host C thirty requests and hosts A and B thirty five each. The per host p ninety nines barely change. Predict the new fleet p ninety nine and the new average, then check, and say which moved and why.

@end text="Merge, then take the percentile"
You can move requests between hosts and watch both numbers, on Learn. That's learn dot get er done dot I O.
