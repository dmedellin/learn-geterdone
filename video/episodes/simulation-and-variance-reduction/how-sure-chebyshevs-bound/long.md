---
format: long
lesson: simulation-and-variance-reduction/how-sure-chebyshevs-bound
title: How sure are you? Chebyshev's bound for simulation intervals
thumb: Plus or minus 2 is not 95%
---

@chapter What an interval guarantees
@title text="How Sure? Chebyshev's Bound" sub="Simulation and Variance Reduction" art=thumb
You've got an estimate and its standard error. Now you want an interval. Everybody reaches for plus or minus two standard errors, and calls it ninety five percent. Without an extra assumption, that's not what it guarantees.

@math heading="Chebyshev's inequality" items="P(|X − μ| ≥ kσ) ≤ 1/k²@at most;;X̄ ± k·SE covers μ with probability ≥ 1 − 1/k²@applied to"
Chebyshev's inequality says the chance a random variable lands k standard deviations or more from its mean is at most one over k squared. Applied to the sample mean, whose standard deviation is the standard error, the interval X bar plus or minus k standard errors covers mu with probability at least one minus one over k squared.

@art tail-mass
Picture it as tails. However the distribution is shaped, at most one over k squared of its mass can sit beyond k standard deviations either side.

@art any-shape
And it holds for every distribution with a finite variance. Skewed, bimodal, discrete, anything. There's no assumption in it that can turn out false about the model you actually simulated.

@chapter The numbers
@math heading="Guaranteed coverage" items="k = 5:  1 − 1/25 = 24/25 = 96%@k of five;;k = 2:  1 − 1/4 = 3/4@k of two;;k = 1:  0@k of one"
At k of five, that's twenty four twenty fifths, ninety six percent. At k of two, the guarantee is just three quarters. And at k of one, it's zero: Chebyshev promises nothing about plus or minus one standard error.

@words text="95% for ±2 SE is an assumption"
So where does the ninety five come from? The normal approximation, which this path hasn't built and doesn't assume. And it fits worst exactly where the later estimators live: averages of a few strongly dependent replications.

@chapter Counting coverage
@words text="(X̄ − μ)² ≥ k²σ²/n" sub="no square root needed"
To count coverage exactly, square both sides. The distance being at least k standard errors is the same as the squared distance being at least k squared sigma squared over n. No root, so each check compares two exact fractions.

@art replication-bars
Here are forty replications of a hundred draws, on a table with variance exactly one. At k of five, the guarantee is ninety six percent, and all forty cover the truth: a hundred percent. That gap isn't luck. It's the slack in a bound that has to hold for every distribution at once.

@art narrow-misses
Drag k down to one. The guarantee is zero, and the observed coverage is twenty five of forty, sixty two point five percent. Both are correct. They answer different questions.

@chapter What the guarantee costs
@math heading="σ² = 1 · n = 100 · SE = 1/10" items="k = 5:  half-width 1/2@a half;;k = 2:  half-width 1/5@a fifth;;ratio (1/2)/(1/5) = 5/2@five halves"
With a standard error of a tenth, the half width at k of five is a half. At k of two, a fifth. The ratio is five halves.

@art width-ratio
So avoid saying five times wider. The five in k of five isn't a width ratio. Two and a half is the honest price of the guarantee, and a reader who wants a real ninety six percent might well pay it.

@art runs-price
Or pay with runs. Keep k at five and shrink the standard error until the band is as narrow as plus or minus two. Width falls like one over root n, so that takes five halves squared, twenty five quarters, six and a quarter times the draws.

@words text="Half-width (1/32)√367 ≈ 0.59866" sub="skewed table, σ² = 367/256"
On the skewed table, with variance three sixty seven over two fifty six, the half width becomes a surd, a thirty second of root three sixty seven, about point six. The guarantee, the width ratio and the run cost don't move, because none of them has a root in it.

@chapter Where people slip
@list heading="Common slips" items="Calling ±2 SE a 95% interval@The first|Reading the bound as the error@The second|Choosing k after seeing the results@And the third"
The first slip is calling plus or minus two standard errors a ninety five percent interval. The second is reading the bound as an estimate of the error. It's a worst case. And the third is choosing k after seeing where the replications fell. That turns a guarantee into a description.

@chapter Try it
@words text="k = 3 · k = 4" sub="guarantee? half-width at SE = 1/10?"
Your turn. Work out the guaranteed coverage and the half width at k of three and k of four, with a standard error of a tenth. Then say how many times the draws you'd need for k of four to match the width of k of two.

@end text="Pay for the guarantee, knowingly"
You can drag k and watch the guarantee and the observed coverage side by side, on Learn. That's learn dot get er done dot I O.
