---
format: long
lesson: latency-and-the-tail/percentiles-do-not-add
title: Percentiles do not add: convolve instead
thumb: 38 + 72 is not the p99
---

@chapter The question
@title text="Percentiles Do Not Add" sub="Latency and the Tail" art=thumb
Two stages run one after the other. The first has a p ninety nine of thirty eight milliseconds, the second seventy two. So the request's p ninety nine is a hundred and ten? That number appears in a great many latency budgets. It's wrong, and not even in a predictable direction.

@art two-stages
Here are the two stages, each given as a list of times and weights. Stage A is mostly fast, four milliseconds on more than half of calls, with a thin tail out to seventy. Stage B is slower and steadier, centred near seventeen, with a tail to a hundred and thirty.

@art series-pipe
They run one after the other, so each request takes the sum of the two. What's the p ninety nine of that sum?

@chapter Means add
@math heading="Means" items="E[A] = 881/125 = 7.048@seven point zero four eight;;E[B] = 2414/125 = 19.312@nineteen point three one two;;E[A + B] = 659/25 = 26.360  exactly@twenty six point three six"
Means do add. Stage A's mean is seven point zero four eight milliseconds. Stage B's is nineteen point three one two. The mean of the sum is twenty six point three six, exactly the sum of the two. That's linearity of expectation. It's a theorem, and it doesn't even need independence.

@words text="There is no such theorem for percentiles"
But there's no theorem next to it for percentiles. A percentile is a position in a sorted list, and positions don't add.

@chapter Convolution
@art convolution-grid
To get the distribution of the sum, convolve. For every pair of outcomes, a from A and b from B, the total a plus b happens with probability P of a times Q of b. Add up the probabilities that land on the same total. Seven outcomes each give forty nine pairs, and forty three distinct totals.

@art sum-histogram
The result is a new distribution, the distribution of the total, with its own shape and its own tail. Every probability in it is an exact fraction.

@math heading="Read the p99 by rank" items="cumulative at 77 ms = 24693/25000 = 0.98772@seventy seven;;cumulative at 78 ms = 3096/3125 = 0.99072@seventy eight;;p99(A + B) = 78 ms@So the p ninety nine"
Then walk the totals upward, accumulating. At seventy seven milliseconds, the cumulative probability is nought point nine eight seven seven two, still short of ninety nine percent. At seventy eight, it's nought point nine nine zero seven two. So the p ninety nine of the sum is seventy eight.

@math heading="True against naive" items="p99(A + B) = 78 ms@seventy eight;;p99(A) + p99(B) = 110 ms@a hundred and ten;;gap 32 ms, 41.0% high@thirty two"
The true p ninety nine is seventy eight. The sum of the stage p ninety nines is a hundred and ten. That overstates by thirty two milliseconds, forty one percent. If that budget sizes a timeout or a machine count, you pay for the overstatement in capacity.

@chapter Not a bound either
@math heading="Same stages, the p95" items="p95(A) + p95(B) = 14 + 34 = 48 ms@fourteen and thirty four;;p95(A + B) = 52 ms@fifty two"
So call the sum conservative? Look at the p ninety five of the same pair. The stage p ninety fives are fourteen and thirty four, which add to forty eight. The true p ninety five of the sum is fifty two. Here the naive arithmetic understates, by four milliseconds.

@art high-and-low
So the sum of percentiles is not an upper bound, not a lower bound, and not conservative. Whether it comes out high or low depends on how the mass past each stage's percentile is arranged.

@chapter How rare is the naive answer?
@math heading="Both stages at their p99" items="P(A > 37) = 1/50@one in fifty;;P(B > 71) = 7/500@seven in five hundred;;together: 7/25000 ≈ 0.0280%@seven in twenty five thousand"
For the total to reach a hundred and ten by both stages being at their p ninety nine together, A must exceed thirty seven, one in fifty, and B must exceed seventy one, seven in five hundred. Together that's seven in twenty five thousand. You asked about the worst one percent, and got the worst three in ten thousand.

@art joint-corner
Adding the p ninety nines assumes both bad days coincide. That's a far rarer event than the one you asked about.

@chapter Where people slip
@list heading="Common slips" items="Adding stage percentiles@The first|Assuming the error has a direction@The second|Budgeting a p99 in means@The third"
The first slip is adding stage percentiles to get an end to end one. The second is assuming the naive sum errs in a known direction. The p ninety five row refutes that. And the third is using the mean because it composes. Here the mean of the total is twenty six point three six, against a p ninety nine of seventy eight.

@chapter Try it
@words text="B = 10 ms ×9 in 10 · 100 ms ×1 in 10" sub="p99(B) = 100 ms · naive: 38 + 100 = 138 ms"
Your turn. Replace stage B with one that's ten milliseconds nine times in ten, and a hundred otherwise. Its p ninety nine is a hundred, so the naive sum is a hundred and thirty eight. Predict whether the true p ninety nine is above or below that, then convolve.

@end text="Convolve, then rank"
You can type in two stages and watch the convolution and its percentiles, on Learn. That's learn dot get er done dot I O.
