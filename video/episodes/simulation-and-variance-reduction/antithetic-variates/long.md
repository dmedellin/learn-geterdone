---
format: long
lesson: simulation-and-variance-reduction/antithetic-variates
title: Antithetic variates: pair U with 1 minus U, and check the sign
thumb: Zero variance, or double
---

@chapter Pair each draw with its opposite
@title text="Antithetic Variates" sub="Simulation and Variance Reduction" art=thumb
Here's a variance reduction trick that takes one line of code. Sometimes it makes the variance exactly zero. Sometimes it exactly doubles the work. The difference is one sign.

@art mirror-pair
Take a uniform draw U, and pair it with one minus U. If U is uniform, so is one minus U. So each half is a legitimate draw, and averaging the pair still gives an unbiased estimator.

@chapter The variance of a pair
@math heading="Pair mean" items="Var((A + B)/2) = (Var A + Var B + 2·Cov(A, B)) / 4@the variance;;= (Var A + Cov(A, B)) / 2@same distribution;;independent pair:  Var A / 2@independent"
The variance of the pair mean is the variance of A, plus the variance of B, plus twice their covariance, all over four. A and B have the same distribution, so that's Var A plus the covariance, over two. An independent pair would give Var A over two.

@words text="Better exactly when Cov < 0"
So compare against an independent pair, which also costs two draws. The antithetic pair is better exactly when the covariance is negative, and worse exactly when it's positive. No tuning, no magic. Just the sign of one number.

@chapter The best case
@art step-monotone
Take a monotone quantity: g of U is one when U is at least a half, and zero otherwise. Whenever U is at least a half, one minus U is below it. So one of each pair is always one, and the other always zero.

@art constant-means
Every pair mean is exactly a half. The variance of the pair means is exactly zero, and the correlation is exactly minus one.

@math heading="64 pairs" items="ordinary:  38 of 64 → 19/32 = 0.59375@ordinary;;antithetic:  1/2, exactly@antithetic;;true value:  1/2@true"
Look at what that does. The sixty four single draws came out one, thirty eight times, so an ordinary estimate on the same draws is nineteen thirty seconds. The antithetic estimate is a half, exactly the true value. The variance isn't just small here. It's zero, and the arithmetic says so, not the picture.

@chapter The worst case
@art v-symmetric
Now a symmetric quantity: the distance from U to a half. One minus U is exactly as far from a half as U is. So the two halves of the pair are the same number, and the correlation is plus one.

@math heading="Symmetric g" items="Var of one draw:  0.022439@a single draw;;independent pair:  0.011219@independent pair;;antithetic pair:  0.022439  (× 2)@twice as bad"
The pair mean has exactly the variance of a single draw, about point oh two two four. An independent pair would have half that. So it's exactly twice as bad: two draws, for an observation no better than one.

@art opposite-signs
Here's the sharp point. The squared correlation is one in both cases. Squared correlation says the two halves determine each other. The sign of the covariance says whether that's worth everything or nothing.

@chapter Why it's available here
@art monotone-sampler
Inverse transform sampling returns the first value whose cumulative probability reaches U, so a larger U never gives a smaller value. Any non decreasing function of the sampled value is then monotone in U, and the covariance is guaranteed negative. That's built into the sampler from the start of the course.

@words text="Many draws, not monotone: measure it"
But that guarantee stops once a run uses many draws in ways that aren't monotone, like a queue. Then the covariance has no guaranteed sign, and you have to measure it on the model in hand.

@chapter Where people slip
@list heading="Common slips" items="Counting a pair as two observations@The first|Assuming it helps because of its name@The second|Pairing a non-monotone run@And the third"
The first slip is counting a pair as two independent observations. In the symmetric case, that hides a doubling and makes it look like a halving. The second is assuming it helps because it's called variance reduction. And the third is pairing a whole run that isn't monotone in its draws.

@chapter Try it
@words text="g(U) = U" sub="is Cov(U, 1 − U) negative?"
Your turn. Take the simplest case of all, g of U equals U. Is it monotone? Work out the pair mean of U and one minus U, and say what its variance is. Then try g of U equals U times one minus U, and predict which way the pairing goes.

@end text="Read the sign of the covariance"
You can switch between monotone and symmetric quantities and watch the pairing pay or cost, on Learn. That's learn dot get er done dot I O.
