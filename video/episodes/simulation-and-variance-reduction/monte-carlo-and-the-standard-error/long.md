---
format: long
lesson: simulation-and-variance-reduction/monte-carlo-and-the-standard-error
title: Monte Carlo and the standard error: why four times the runs buys half
thumb: Four times the runs, half the width
---

@chapter An answer that moves
@title text="Monte Carlo and the Standard Error" sub="Simulation and Variance Reduction" art=thumb
Run a simulation, get a number. Run it again with a different seed, and you get a different number. So what exactly should you report?

@art scatter-draws
The output of a simulation is a random variable, not an answer. The Monte Carlo estimator draws X one to X n independently and reports their average, X bar.

@words text="E[X̄ₙ] = μ" sub="unbiased at every n"
That average is unbiased. Its expectation is the true mean mu, for every n, so it's aimed at the right number from the very first draw. The question is how far it wanders.

@chapter The standard error
@math heading="The spread of the average" items="Var(X̄ₙ) = σ²/n@the variance;;SE = σ/√n@standard error;;s² = Σ(Xᵢ − X̄)² / (n − 1)@sample variance"
For independent draws, the variance of the average is sigma squared over n. Its square root is the standard error, sigma over root n. When sigma squared is unknown, estimate it with the sample variance, dividing by n minus one.

@words text="Why n − 1?"
The n minus one isn't a fudge. The sample mean was fitted to the same data, so one degree of freedom is spent. Divide by n and the variance comes out systematically too small. On four draws, that's off by a quarter.

@art data-vs-mean-spread
And the standard error describes the average, not the data. At four hundred draws, the spread of a single draw is twenty times the spread of the average. Mixing those up is easy, and costly.

@chapter Four times the runs
@art four-for-half
Here's the rate. The standard error at n, over the standard error at four n, is exactly two, whatever sigma is, because squaring removes both roots. So halving the width costs four times the draws, and one more decimal digit costs a hundred times.

@math heading="One stream, three lengths" items="n = 100:  mean 21/10,  SE ≈ 0.10684 · σ/√n = 1/10@a hundred;;n = 400:  413/200,  ≈ 0.05192 · 1/20@four hundred;;n = 1600:  3231/1600,  ≈ 0.02485 · 1/40@sixteen hundred"
On the table one, four, six, four, one over sixteen, at a hundred draws the mean is twenty one tenths, and the standard error is about point one oh seven, against a true tenth. At four hundred, about point oh five two, against a twentieth. At sixteen hundred, about point oh two five, against a fortieth.

@art narrowing-band
The estimates track the theory without matching it, and that's correct. The sample variance is itself an estimate. An estimate of a standard error has a standard error.

@chapter One rounded number
@words text="SE = (1/330)√1243 ≈ 0.10684 (rounded)"
And notice: the mean and variance are exact fractions. The standard error is a square root, so it's carried as an exact surd, and printed with the word rounded. Every other decimal on these pages says exact, shown to so many places. Keeping that word honest is what lets you tell which is which.

@chapter What shrinking doesn't mean
@art many-runs
More draws don't converge to the answer. They shrink the spread. A long run can land further off than a short one. At four hundred draws, this stream is thirteen two hundredths out, while seed four is three four hundredths out, and seed zero is three fortieths out.

@art flat-trace
And a running mean that's stopped moving hasn't converged. A flat stretch is just what a small sample of a slow process looks like. The interval is the evidence. The picture is just a picture.

@words text="Change the estimator, not the budget"
That one over root n is proved, and it's slow. The only way to beat it isn't more draws. It's a better estimator, and that's what the second half of this course is about.

@chapter Where people slip
@list heading="Common slips" items="Reporting the estimate without the width@The first|Quoting the data's spread as the estimate's@The second|Believing a run that has settled@And the third"
The first slip is reporting the estimate without its standard error. That makes no claim anyone can check. The second is quoting the spread of the data as the spread of the estimate. And the third is believing a run because it looks settled.

@chapter Try it
@words text="n = 6400?" sub="σ² = 1"
Your turn. On the same table, sigma squared is one. What's the theoretical standard error at six thousand four hundred draws? And how many draws would you need to reach a two hundredth?

@end text="Print the width beside the number"
You can push the number of draws and watch the standard error halve every time you quadruple them, on Learn. That's learn dot get er done dot I O.
