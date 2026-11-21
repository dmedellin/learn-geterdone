---
format: long
lesson: discrete-probability/variance
title: Variance and standard deviation: measuring the spread
thumb: Same mean, different risk
---

@chapter The question
@title text="Variance and Standard Deviation" sub="Discrete Probability" art=thumb
Two bets can have the same expected value and feel completely different.

@art two-bets
Win or lose a pound on a coin flip, or win or lose a thousand. Expectation can't tell them apart. Variance can.

@art deviation-arrows
Variance measures spread: how far X tends to land from its mean. You can't just average the deviations, because the expected deviation from the mean is always zero. They cancel. So you square them first.

@math heading="Variance" items="Var(X) = E[(X − μ)²],  μ = E[X]@squared deviation;;σ(X) = √Var(X)@the square root"
Variance is the expected squared deviation from the mean, mu. The standard deviation, sigma, is the square root of the variance, and it's in the same units as X.

@chapter A faster formula
@math heading="Computational formula" items="E[(X − μ)²] = E[X² − 2μX + μ²]@expand the square;;= E[X²] − 2μE[X] + μ²@linearity;;= E[X²] − μ²@two mu squared"
Expand the square, and use linearity. You get the expectation of X squared, minus two mu times the expectation of X, plus mu squared. Since the expectation of X is mu, that's minus two mu squared plus mu squared. What's left is the expectation of X squared minus mu squared.

@words text="Var(X) = E[X²] − (E[X])²" sub="so E[X²] ≥ (E[X])² always"
So variance is the expectation of X squared minus the square of the expectation. Two things drop out. Variance is never negative, so the first is always at least the second. And variance is zero exactly when X is constant.

@chapter A fair die
@math heading="A fair die" items="E[X] = 3.5@three point five;;E[X²] = (1 + 4 + 9 + 16 + 25 + 36)/6 = 91/6 ≈ 15.167@ninety-one sixths;;Var(X) = 91/6 − 49/4 = 35/12 ≈ 2.917@thirty-five twelfths;;σ ≈ 1.708@one point seven zero eight"
For a fair die, the expectation is three point five. The expectation of X squared is one plus four plus nine plus sixteen plus twenty-five plus thirty-six, over six, which is ninety-one sixths. Subtract forty-nine quarters, and the variance is thirty-five twelfths, about two point nine one seven. The standard deviation is about one point seven zero eight.

@chapter Shifts, scales and sums
@art shift-scale
Adding a constant slides the distribution without changing its spread. Scaling by a scales the spread by the size of a, and the variance by a squared. So the variance of a X plus b is a squared times the variance of X.

@math heading="Sums" items="independent: Var(X + Y) = Var(X) + Var(Y)@independent;;in general: + 2 Cov(X, Y)@covariance;;Cov(X, Y) = E[XY] − E[X]E[Y]@the amount"
If X and Y are independent, their variances add. In general, you add two times the covariance, which is the expectation of X Y minus the product of the expectations. That's the amount by which the product rule fails, and it's zero for independent variables.

@words text="Expectations add always · variances need independence"
That's the big contrast with expectation. Sums of expectations never need independence. Sums of variances always do.

@chapter Two dice, two ways
@art two-dice-sums
Take two fair dice, each with variance thirty-five twelfths. First, two separate independent dice. Then the same die counted twice.

@math heading="Var of a sum" items="independent: 35/12 + 35/12 = 35/6 ≈ 5.833@add the variances;;σ ≈ 2.415@two point four one five;;same die twice: Var(2X) = 4 · 35/12 = 35/3 ≈ 11.667@the same die counted twice;;σ ≈ 3.416@three point four one six"
For independent dice, add the variances: thirty-five sixths, about five point eight three three, with standard deviation about two point four one five. For the same die counted twice, the sum is two X, so the variance is four times thirty-five twelfths, about eleven point six six seven, with standard deviation about three point four one six.

@words text="Both have mean 7"
Both sums have expectation seven. But two independent dice can offset each other, a high one with a low one. A doubled die can't, so its spread is larger.

@chapter Averaging shrinks it
@art average-narrow
Average n independent variables, each with variance sigma squared. The sum has variance n sigma squared, and dividing by n scales the variance by one over n squared. So the average has variance sigma squared over n, and standard deviation sigma over root n.

@words text="σ / √n" sub="halve the uncertainty: four times the data"
That root n is why an insurer sells many policies. It also explains why halving the uncertainty of an estimate takes four times the data.

@art chebyshev-tails
And Chebyshev's inequality holds for every distribution with a finite variance. At most a quarter of it lies more than two standard deviations from the mean, and at most a ninth beyond three. It's weak, but it needs no shape assumption at all.

@chapter Where people slip
@list heading="Common slips" items="Squaring the mean instead of the values@instead of|Adding variances of dependent variables@dependent variables|Quoting variance for standard deviation@squared units"
First, squaring the mean instead of averaging the squares. Second, adding variances of dependent variables without the covariance term. Third, quoting the variance where you mean the standard deviation. Variance is in squared units. Sigma is what to report.

@chapter Try it
@words text="Bet A: ±£1 · Bet B: ±£1000" sub="fair coin: find E and Var for each"
Your turn. Bet A wins or loses one pound on a fair coin. Bet B wins or loses a thousand. Find the expectation and the variance of each, and see which number tells them apart.

@end text="Variance measures the risk"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
