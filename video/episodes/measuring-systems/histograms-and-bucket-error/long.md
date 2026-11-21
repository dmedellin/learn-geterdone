---
format: long
lesson: measuring-systems/histograms-and-bucket-error
title: Histogram percentiles are intervals, not numbers
thumb: Known to the bucket, no finer
---

@chapter Counts, not values
@title text="Histograms and Bucket Error" sub="Measuring Systems" art=thumb
Your dashboard says the p ninety nine is a hundred and fifty milliseconds. If it came from a histogram, it doesn't know that. It knows the answer is somewhere between a hundred and two hundred.

@art counts-not-values
A histogram keeps a count per bucket and throws the values away. Each request bumps the counter for the bucket its latency fell in. What's left is enough to say which bucket a given rank lands in, and not where inside it.

@art geometric-edges
Boundaries are chosen once, before any data, and usually geometrically, because latency spans orders of magnitude. The lab starts at twenty five milliseconds and doubles: fifty, a hundred, two hundred, four hundred, eight hundred, sixteen hundred.

@chapter Reading the p99
@math heading="n = 100 requests" items="[25, 50):  65,  cumulative 65@sixty five;;[50, 100):  25,  cumulative 90@ninety;;[100, 200):  9,  cumulative 99@ninety nine;;p99 = rank 99  →  [100, 200)@rank ninety nine"
Take a hundred requests. Sixty five land in the bottom bucket. Twenty five more in fifty to a hundred, so ninety so far. Nine in a hundred to two hundred, so ninety nine. The p ninety nine is rank ninety nine, which is first reached in the bucket from a hundred to two hundred.

@art rank-walk
So walk the cumulative counts until they reach the rank. Count every bucket, including the overflow, or n is wrong and the rank moves.

@art interval-not-point
The exact p ninety nine of this sample is a hundred and thirty seven milliseconds. The histogram can't say a hundred and thirty seven. It can say at least a hundred and less than two hundred. True, useful, and a hundred milliseconds wide.

@chapter Constant relative width
@math heading="Edges eᵢ = b · rⁱ" items="width = eᵢ(r − 1)@its width;;relative width = r − 1@r minus one;;r = 2:  100%,   r = 5/4:  25%@a hundred percent"
With geometric edges, a bucket starting at x ends at r times x. So its width, relative to where it starts, is r minus one, in every bucket. At a ratio of two, that's a hundred percent. Every answer is known to within a factor of two. At five quarters, twenty five percent.

@art finer-buckets
Refine to five quarters, from the same twenty five milliseconds, and the same rank lands between a hundred and nineteen point two one and a hundred and forty nine point oh one, about thirty milliseconds wide. Nothing new was measured. But covering the same range takes about three point one times as many buckets, and every bucket is another time series.

@chapter Traffic doesn't fix it
@art more-traffic-same-width
This error is systematic. Ten times the traffic puts ten times the counts in the same buckets, and the answer is still the same interval. Sampling noise shrinks with the square root of n. Bucket width doesn't shrink at all.

@chapter Don't interpolate
@words text="Interpolated: 200 ms.  True: 137 ms."
Most metrics systems interpolate, assuming values are spread evenly across the bucket. Here, rank ninety nine is the last of nine in its bucket, so interpolation reports two hundred, the top edge, against a true hundred and thirty seven. Inside a geometric bucket the mass sits low. Interpolation turns an honest interval into a point whose error you can't see.

@words text="137 → 195 ms: same bucket.  199 → 201: next bucket."
And watch the edges. A regression from a hundred and thirty seven to a hundred and ninety five wouldn't move the reported bucket. One from a hundred and ninety nine to two hundred and one moves a whole bucket. Choose boundaries so the values you care about aren't near an edge.

@chapter Where people slip
@list heading="Common slips" items="Reporting a bucketed percentile as a number@The first|Expecting more traffic to sharpen it@The second|Linear buckets for latency@the third"
The first slip is reporting a bucketed percentile as a number. Report the bucket, or the lower edge as a lower bound. The second is expecting more traffic to sharpen it. And the third is choosing equal width buckets for latency, which resolves the tail finely and the median terribly.

@chapter Try it
@words text="Base 25,  ratio 3/2" sub="25, 37.5, 56.25, 84.375, 126.5625, …"
Your turn. Keep the sample and the base, and set the ratio to three halves. The edges become twenty five, thirty seven point five, fifty six point two five, and so on. Predict which bucket rank ninety nine lands in and the relative width, then count how many buckets reach eight hundred.

@end text="Report the bucket"
You can change the boundaries and watch the interval narrow, on Learn. That's learn dot get er done dot I O.
