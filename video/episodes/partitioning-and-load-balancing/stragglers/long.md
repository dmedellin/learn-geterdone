---
format: long
lesson: partitioning-and-load-balancing/stragglers
title: Stragglers: why more partitions make the job slower
thumb: The job waits for the slowest
---

@chapter The slowest one wins
@title text="Stragglers" sub="Partitioning and Load Balancing" art=thumb
Split a job across more partitions and it should get faster, right? Each one has less work to do. But there's a second effect pulling the other way, and it's the one nobody budgets for.

@art wait-for-all
If a job has to wait for every partition, it finishes when the slowest one does. That last one is the straggler. So the job's running time isn't the mean of N partition times. It's the maximum of them.

@math heading="The maximum's distribution" items="max ≤ t  ⇔  every partition ≤ t@every one of the N;;P(max ≤ t) = P(T ≤ t)ᴺ@to the power N"
The maximum is at most t exactly when every one of the N partitions is at most t. If they're independent and drawn from the same distribution, that probability is one partition's probability, raised to the power N.

@chapter One partition
@art four-outcomes
Here's the lab's distribution for one partition, in milliseconds, with weights out of a thousand. Twenty with weight nine hundred. Forty with seventy. A hundred and twenty with twenty five. And four hundred with weight five, half a percent.

@math heading="One partition" items="mean = 18.0 + 2.8 + 3.0 + 2.0 = 25.80 ms@twenty five point eight;;P(T ≤ 40) = 0.970,  P(T ≤ 120) = 0.995@point nine seven;;p99 = 120 ms@a hundred and twenty"
The mean is eighteen plus two point eight plus three plus two, twenty five point eight milliseconds. The chance of forty or less is point nine seven, and of a hundred and twenty or less is point nine nine five. So one partition's p ninety nine is a hundred and twenty milliseconds.

@chapter Twenty four partitions
@math heading="The job over N = 24" items="P(job ≤ 120) = 0.995²⁴ = 0.8867@to the twenty fourth;;p99 = 400 ms@four hundred;;mean = 111.63 ms,  tax = 4.33×@a hundred and eleven;;P(one past 120 ms) = 11.33%@eleven point three three"
Now a job over twenty four partitions. Point nine nine five to the twenty fourth is point eight eight six seven. So the job's p ninety nine is four hundred, the worst outcome there is. The mean is a hundred and eleven point six three milliseconds, four point three three times one partition. And eleven point three three percent of jobs have one partition past a hundred and twenty.

@words text="Exact, not simulated"
Every one of those figures is exact. The lab enumerates the distribution of the maximum rather than sampling it, so you get the same numbers every time.

@chapter More partitions, slower job
@art rising-mean
Hold that distribution fixed and vary N. The job mean goes twenty five point eight at one partition, forty one point six one at four, eighty eight point seven three at sixteen, a hundred and eleven point six three at twenty four, and a hundred and thirty point six two at thirty two. It only goes up.

@math heading="Where p99 becomes 400 ms" items="N = 2:  0.995² = 0.990025 ≥ 0.99,  p99 = 120@at two;;N = 3:  0.995³ = 0.985075 < 0.99,  p99 = 400@at three"
And look at the p ninety nine. At two partitions, point nine nine five squared is still above point nine nine, so the p ninety nine is a hundred and twenty. At three, it drops below, and the p ninety nine jumps to four hundred. Nothing got slower. The job just takes enough draws that the rare outcome stops being rare.

@art tail-takeover
Read it as a failure rate. If a hundred and twenty milliseconds is a timeout, one partition misses it point five percent of the time. A hundred and twenty eight way job misses it forty seven point three six percent of the time. Every one of those is a retry.

@chapter What to do about it
@art three-levers
Three responses, cheapest first. Shrink the tail of one partition, which moves the whole table at once. Stop waiting for every partition, if the answer allows it. Or send the slow one somewhere else and take the first answer, which is hedging, and costs duplicate work. What doesn't help is adding partitions.

@art max-of-draws
And notice this needs no skew at all. Every partition draws from the same distribution, and the job is still four times slower than one partition, because the maximum of many identical things is larger than any of them.

@chapter Where people slip
@list heading="Common slips" items="Budgeting a job at its partitions' mean@The first|Expecting partitions to buy time linearly@The second|Dismissing a half-percent outcome@the third"
The first slip is budgeting a job at its partitions' mean. The second is expecting more partitions to buy time linearly. And the third is dismissing a half percent outcome as a tail, when at three partitions it's already the p ninety nine.

@chapter Try it
@words text="20:940 · 40:40 · 120:15 · 400:5" sub="first move: the new one-partition mean"
Your turn. Same outcomes, new weights: twenty at nine forty, forty at forty, a hundred and twenty at fifteen, four hundred at five. Work out the new mean for one partition, then the job's mean and p ninety nine at twenty four. Did the p ninety nine move? Then predict what halving the weight on four hundred would do instead.

@end text="The max, not the mean"
You can change the partition count and watch the job's tail, on Learn. That's learn dot get er done dot I O.
