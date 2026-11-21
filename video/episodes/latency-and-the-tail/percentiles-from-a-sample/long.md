---
format: long
lesson: latency-and-the-tail/percentiles-from-a-sample
title: Percentiles from a sample: why no user saw the mean
thumb: Nobody took 53 ms
---

@chapter The question
@title text="Percentiles from a Sample" sub="Latency and the Tail" art=thumb
Twenty requests, and their average time is fifty three point two milliseconds. So the typical user sees about fifty three? In this sample, no request took anything close to that. Let's see why.

@art sorted-row
A percentile is a position in a sorted list, not an average. Sort the sample from fastest to slowest, and the percentile is the value at a particular rank. So it's always a time some request actually took.

@math heading="Nearest rank" items="r = ⌈q · n⌉@the rank r;;p_q = the r-th smallest value@the r th"
For a sample of n values and a fraction q, the rank r is the ceiling of q times n. The percentile is the r th smallest value. Other definitions interpolate and can return a number nobody measured. This course uses nearest rank throughout.

@chapter Twenty measurements
@words text="12 13 14 14 15 15 16 17 18 19 21 22 24 27 31 38 52 96 180 420" sub="milliseconds, sorted"
Here are twenty measurements in milliseconds, already sorted. Twelve, thirteen, fourteen, fourteen, and so on, up through thirty eight, fifty two, ninety six, a hundred and eighty, and four hundred and twenty.

@math heading="n = 20" items="p50: ⌈0.50 × 20⌉ = 10 → 19 ms@the p fifty;;p90: ⌈0.90 × 20⌉ = 18 → 96 ms@the p ninety;;p95: ⌈0.95 × 20⌉ = 19 → 180 ms@the p ninety five;;p99: ⌈0.99 × 20⌉ = ⌈19.8⌉ = 20 → 420 ms@the p ninety nine"
For the p fifty, the rank is ten, so it's nineteen milliseconds. For the p ninety, rank eighteen, ninety six. For the p ninety five, rank nineteen, a hundred and eighty. And for the p ninety nine, the ceiling of nineteen point eight is twenty, so it's four hundred and twenty.

@art spread-out
Four numbers for one sample: nineteen, ninety six, a hundred and eighty, four hundred and twenty. The p ninety nine is twenty two times the median. No single summary figure can carry that spread.

@chapter The mean
@math heading="The mean" items="1064 / 20 = 266/5 = 53.2 ms@ten sixty four;;17 of 20 are faster@Seventeen of the twenty;;neighbours: 52 and 96@fifty two and ninety six"
The mean is ten sixty four over twenty, fifty three point two milliseconds. Seventeen of the twenty requests were faster than that. And the values either side of it are fifty two and ninety six. The mean has landed in a gap.

@art mean-in-gap
That's not a defect of this sample. It's what happens to an average whenever a few large values are pulled far out, which is the normal shape of latency. Eighty five percent of requests were faster, fifteen percent were much slower, and the mean belongs to neither group.

@art total-work
What the mean does tell you is that twenty requests consumed ten sixty four milliseconds of service time in total. That's a fact about load. It's exactly what a capacity calculation needs, and exactly what a latency report doesn't.

@chapter Small samples
@art one-removed
Now delete the four hundred and twenty. At n equals nineteen, the rank is the ceiling of zero point nine nine times nineteen, which is nineteen. So the p ninety nine becomes a hundred and eighty, less than half what it was.

@words text="n = 20: the p99 is the maximum" sub="resolution 1/n"
With twenty values, the p ninety nine is simply the maximum: one measurement carrying the whole claim. A percentile is only as trustworthy as the number of observations beyond it. The fix is more measurements, not a different formula.

@art quickselect
Sorting is the obvious way to find the value, and seeing the sorted list is the point here. But a system with millions of measurements finds the r th smallest value without sorting the rest. The definition doesn't change. Only the work does.

@chapter Where people slip
@list heading="Common slips" items="Calling the p99 an average of the slow ones@The first|Rounding the rank down@The second|Reporting the mean as typical@The third"
The first slip is calling the p ninety nine an average of the slow requests. It's one observation, selected by position. The second is rounding the rank down. Rank nineteen gives a hundred and eighty instead of four hundred and twenty. And the third is reporting the mean as what a typical user experiences.

@chapter Try it
@words text="5 6 6 7 8 9 11 14 20 60 300" sub="n = 11"
Your turn. Take eleven measurements: five, six, six, seven, eight, nine, eleven, fourteen, twenty, sixty and three hundred. So n is eleven. Compute the ranks and values for the p fifty, p ninety and p ninety nine, then the mean, and count how many sit below it. Which single observation does the p ninety nine rest on?

@end text="Rank, don't average"
You can edit the sample and watch every percentile and the mean move, on Learn. That's learn dot get er done dot I O.
