---
format: long
lesson: simulation-and-variance-reduction/control-variates
title: Control variates: subtract what you already know
thumb: The best b is a vertex
---

@chapter A companion you understand
@title text="Control Variates" sub="Simulation and Variance Reduction" art=thumb
Your simulation records lots of things besides the answer you want. Some of them have means you know exactly. You can use that knowledge to cut the noise in your estimate.

@art companion
Take a second quantity C, measured on the same run, whose expectation you know exactly before the run. Report X minus b times C minus its mean. That's a control variate.

@words text="E[C − E[C]] = 0" sub="unbiased at every b"
The correction has expectation zero, so the estimator is unbiased for every b, good or bad. Nothing about the answer is risked. Only the variance is at stake.

@chapter The best coefficient
@math heading="A quadratic in b" items="Var = Var X − 2b·Cov(X, C) + b²·Var C@a quadratic;;b* = Cov(X, C) / Var C@the vertex;;at b*:  Var X · (1 − ρ²)@one minus rho squared"
The variance is Var X, minus two b times the covariance, plus b squared times Var C. That's a quadratic in b, opening upward. Complete the square, and the vertex is at the covariance over Var C. There, the variance is Var X times one minus rho squared.

@art variance-parabola
So the best b isn't tuned. It's a vertex, computed from quantities you already have, and it carries the right sign automatically. A negatively correlated control works just as well.

@words text="ρ² = Cov² / (Var X · Var C)" sub="exact · ρ itself is irrational"
And notice: rho has square roots in it, so it's usually irrational. Rho squared is a ratio of three exact fractions. So the reduction factor is exact, even when rho isn't.

@chapter The measurement
@words text="C = arrivals in 200 slots" sub="E[C] = 200 × 2/5 = 80, known"
Here's the lesson's example. X is the time average number in system over two hundred slots. C is the number of arrivals. Each slot has a two fifths chance, so the mean of C is exactly eighty. Known, not estimated. And arrivals plainly drive the queue.

@math heading="24 replications" items="b* ≈ 0.1123@nought point one one;;ρ² = 0.457615@rho squared;;Var: 1.530750 → 0.830256@falls"
Over twenty four replications, the best b is about nought point one one two three. Rho squared is about point four five eight. And the variance falls from about one point five three one to about point eight three oh.

@art tilt-correction
That's just over forty five percent of the variance removed, from something already being recorded. Buying the same reduction with more runs would take nearly twice the replications.

@chapter Wrong both ways
@art both-sides-wrong
The parabola rises on both sides. At b of zero, it's the uncontrolled one point five three. At twice the best b, it's one point five three again, exactly: the whole benefit thrown away. And with the right size and the wrong sign, it's three point six three, more than twice as bad.

@chapter Known mean, not correlation
@art weak-control
The panel's second companion counts how many of two hundred unrelated draws fall below a half. Its mean is exactly a hundred, just as firmly known, but it barely relates to the queue. Rho squared is only about point oh seven five, and the variance falls just to about one point four one six.

@art known-mean
And a strongly correlated quantity whose mean you don't know isn't a weaker control. It isn't a control. Estimate its mean from the same run, and the correction cancels against the error it was meant to remove, and the estimate is no longer unbiased. No variance figure on the page will show it.

@chapter Where people slip
@list heading="Common slips" items="Estimating the control's mean from the run@The first|Choosing b by hand@The second|Treating correlation as the condition@And the third"
The first slip is estimating the control's mean from the same run. The second is choosing b by hand, or forcing its sign. And the third is treating correlation as the condition. The known mean decides whether it's a control at all. Correlation decides how much it's worth.

@chapter Try it
@words text="b = b*/2" sub="Var X − 2b·Cov + b²·Var C"
Your turn. Using the lesson's own figures from the table, compute the variance at half the best b. Using the completed square, show it keeps three quarters of the benefit you'd get at b star. Then try one and a half times b star, and check you get the same variance, because the parabola is symmetric.

@end text="Subtract what you know"
You can slide b along the parabola and watch the variance rise on both sides, on Learn. That's learn dot get er done dot I O.
