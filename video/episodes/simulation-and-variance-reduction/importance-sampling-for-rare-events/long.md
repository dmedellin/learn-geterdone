---
format: long
lesson: simulation-and-variance-reduction/importance-sampling-for-rare-events
title: Importance sampling for rare events: reweight, then read the variance
thumb: Divide by 123, or multiply by 9546
---

@chapter The rare event problem
@title text="Importance Sampling for Rare Events" sub="Simulation and Variance Reduction" art=thumb
Some events are rare, and those are often the ones you care about most. Simulate them directly, and almost every draw tells you nothing.

@art ten-coins
The lesson's event: ten fair coins all landing heads. Its probability is exactly one in a thousand and twenty four. Because the answer is known, any difference between methods has to be variance.

@art wasted-draws
To see that event even ten times takes about ten thousand draws. To estimate it within ten percent takes on the order of a hundred thousand. Nine hundred ninety nine draws in a thousand return a zero.

@chapter Reweight the draws
@math heading="Importance sampling" items="E_p[h(X)] = E_q[ h(X) · p(X)/q(X) ]@the expectation;;q(x) > 0 wherever p(x)h(x) ≠ 0@as long as"
So draw from a different distribution, q, where the event is common, and weight each draw by p over q, the likelihood ratio. The expectation under p equals the expectation under q of the weighted quantity, as long as q is positive everywhere p times h is.

@words text="Σ q(x) · h(x)p(x)/q(x) = Σ h(x)p(x)"
The proof is one line: the q cancels. So the estimator is unbiased for the same number as direct simulation, for every valid q. The estimate isn't where good and bad proposals differ. The variance is.

@chapter A good proposal
@art tilted-proposal
Weight the coins toward heads, four fifths each. Now ten heads happens about one draw in nine, and its weight is about nought point oh oh nine one.

@math heading="Per-draw variance" items="direct:  1023/1048576@Directly;;P(H) = 4/5:  ≈ 0.0000079@four fifths;;divided by ≈ 123.06@divided"
Directly, the variance per draw is a thousand twenty three over about a million. With the four fifths coin, it's about seven point nine millionths. That's the original variance divided by about a hundred and twenty three. The same estimator, the same unbiasedness, and far fewer draws for the same width.

@art weights-scale
In two thousand draws, the good proposal hits the event two hundred fifteen times and estimates about point oh oh oh nine seven seven seven, against the exact point oh oh oh nine seven seven. The fair coin hits it once, and estimates one in two thousand, about half the true value.

@chapter A bad proposal
@art huge-weight
Now weight the coins the wrong way, one fifth heads. Under that coin, ten heads has a chance of about one in ten million, and its weight is about nine thousand five hundred. A draw that hits contributes its whole weight. The variance is multiplied by about nine thousand five hundred forty six.

@words text="2000 draws · 0 hits · estimate 0"
And here's the trap. Two thousand draws hit it not at all, and estimate exactly zero, with a flat, ordinary looking trace. Still unbiased. All the damage is in the spread, and none of it is in the picture. One draw in ten million would have carried the entire estimate.

@chapter The proposal that's refused
@art hole-in-support
Take the good proposal and remove its mass on ten heads. It's still a genuine distribution. But q is zero exactly where the event lives, so the weight is undefined there, and the panel refuses it.

@words text="No estimator at all"
That refusal matters. Skip the undefined outcome and you'd return zero, every time, with zero variance. A confident, reproducible, perfectly stable wrong answer. The support condition decides whether there is an estimator at all. Closeness to p only decides how good it is.

@chapter Where people slip
@list heading="Common slips" items="Oversampling and forgetting to weight@The first|Judging a proposal by its estimate@The second|Assuming it can only help@And the third"
The first slip is oversampling the event and forgetting to weight. That gives about point one oh seven instead of point oh oh oh nine eight. The second is judging a proposal by its estimate, when every valid one aims at the same number. And the third is assuming importance sampling can only help.

@chapter Try it
@words text="P(H) = 3/5" sub="q(event)? weight? better or worse?"
Your turn. Try a proposal with three fifths heads. Work out the chance of ten heads under it, the weight on that outcome, and predict whether the variance falls, and by roughly how much compared with four fifths.

@end text="Read the variance, not the estimate"
You can try your own proposal and see the variance divided or multiplied, on Learn. That's learn dot get er done dot I O.
