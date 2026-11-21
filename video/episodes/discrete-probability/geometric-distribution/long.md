---
format: long
lesson: discrete-probability/geometric-distribution
title: The geometric distribution: waiting for the first success
thumb: Average 6, most likely 1
---

@chapter The question
@title text="The Geometric Distribution" sub="Discrete Probability" art=thumb
How many rolls until your first six? On average it's six. But the single most likely answer is one. That gap is what this lesson is about.

@art wait-row
Run independent trials, each succeeding with probability p, and let X be the number of the trial where the first success happens. Unlike the binomial, the number of trials isn't fixed. You keep going until you succeed.

@math heading="Geometric distribution" items="P(X = k) = (1 − p)ᵏ⁻¹ p@to the k minus one;;k = 1, 2, 3, …@for k equal one"
A first success on trial k means k minus one failures, then a success. By independence, that's one minus p, to the k minus one, times p, for k equal one, two, three, and on forever. These add up to one by the geometric series.

@chapter The mean, by conditioning
@art restart-loop
Here's a lovely way to find the mean without summing an infinite series. Look at the first trial. With probability p it succeeds, and X is one. With probability one minus p it fails, and the remaining wait looks exactly like X again.

@math heading="Condition on the first trial" items="E[X] = p · 1 + (1 − p)(1 + E[X])@p times one;;E[X] = 1 + (1 − p) E[X]@Expanding;;p E[X] = 1@p times;;E[X] = 1/p@one over p"
So the expectation is p times one, plus one minus p times one plus the expectation. Expanding, the expectation is one plus one minus p times the expectation. Gather terms, and p times the expectation is one. So the mean is one over p.

@words text="Var(X) = (1 − p) / p²"
The variance is one minus p over p squared. And that conditioning trick is worth more than the formula. It handles many waiting time problems where no series is available.

@chapter Rolling for a six
@math heading="p = 1/6" items="E[X] = 1/p = 6@six rolls;;Var(X) = (5/6)/(1/36) = 30,  σ ≈ 5.48@thirty;;P(X = 1) = 1/6 ≈ 0.1667@the most likely;;P(X = 6) = (5/6)⁵(1/6) ≈ 0.0670@exactly six"
With p equal to one sixth, the mean is six rolls. The variance is five sixths over one thirty-sixth, which is thirty, so sigma is about five point four eight. The first roll is the most likely single value, about zero point one six six seven. Exactly six rolls is only about zero point zero six seven.

@art falling-bars
The distribution always falls. The most likely single outcome is the first trial, whatever p is. On average six describes a long tail on the right, balanced against a peak at one.

@chapter Why the mean misleads
@words text="P(X > k) = (5/6)ᵏ"
The tail has a clean form. The chance of waiting more than k rolls is five sixths to the k, since the first k rolls all failed.

@math heading="p = 1/6" items="P(X ≤ 3) ≈ 0.421@by the third;;P(X ≤ 6) = 1 − (5/6)⁶ ≈ 0.665@by the sixth;;P(X > 12) = (5/6)¹² ≈ 0.112@more than twelve;;P(X > 20) ≈ 0.026@more than twenty"
You're done by the third roll with probability about zero point four two one, and by the sixth about zero point six six five. More than twelve rolls happens about zero point one one two of the time, and more than twenty about zero point zero two six.

@art tail-bars
So two thirds of the time you finish by the mean, and one time in nine you wait more than twice as long. With sigma nearly as big as the mean, no single number summarises this.

@chapter No memory
@math heading="Memorylessness" items="P(X > m + n | X > m) = P(X > n)@has no memory;;= (1 − p)ᵐ⁺ⁿ / (1 − p)ᵐ = (1 − p)ⁿ@divide"
The geometric distribution has no memory. Given you've already waited more than m trials, the chance of waiting n more is the same as from scratch. Divide one minus p to the m plus n by one minus p to the m, and you get one minus p to the n. It's the only discrete distribution with that property.

@art roulette-streak
This is the gambler's fallacy, stated correctly. A roulette wheel that's come up red twenty times is exactly as likely to come up red next spin. The trials are independent, so past failures change nothing.

@chapter Collecting coupons
@art coupon-stages
With n equally likely coupons, split the collecting into stages. In stage i you hold i minus one coupons, and each purchase is new with probability n minus i plus one over n. So each stage is a geometric wait, with mean n over n minus i plus one.

@math heading="Coupon collector" items="E[total] = n(1 + 1/2 + ⋯ + 1/n)@adds the stages;;n = 50  ⟹  about 225 purchases@fifty;;last coupon alone: 50 on average@the last coupon"
Linearity adds the stages: n times one plus a half and so on up to one over n. For fifty coupons, that's about two hundred twenty-five purchases, and the last coupon alone takes fifty of them on average. That's why the last few of anything take so long.

@chapter Where people slip
@list heading="Common slips" items="Confusing it with the binomial@with the binomial|Believing a losing streak improves the odds@losing streak|Reporting only the mean@only the mean"
First, confusing it with the binomial. Fixed trials, count successes: binomial. Fixed target, count trials: geometric. Second, believing a losing streak improves the odds. Third, reporting only the mean, which hides both the peak at one and the long tail.

@chapter Try it
@words text="p = 0.1, failed 20 times" sub="P(next trial succeeds)?"
Your turn. Suppose p is zero point one, and you've failed twenty times in a row. What's the chance the next trial succeeds? Use memorylessness, and resist the story your intuition tells.

@end text="Report the tail, not just the mean"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
