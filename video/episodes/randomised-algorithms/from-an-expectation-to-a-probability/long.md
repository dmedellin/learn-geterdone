---
format: long
lesson: randomised-algorithms/from-an-expectation-to-a-probability
title: Markov and Chebyshev: turning an average into a guarantee
thumb: A bound above one says nothing
---

@chapter An average promises nothing
@title text="From an Expectation to a Probability" sub="Randomised Algorithms" art=thumb
An expected cost, on its own, promises nothing about any particular run. Two short inequalities turn it into a real probability bound. They hold for every distribution, and you pay for that in slack.

@chapter Markov's inequality
@math heading="Markov" items="X ≥ 0,  a > 0  ⟹  P(X ≥ a) ≤ E[X]/a@X is never negative"
If X is never negative, and a is positive, then the probability that X is at least a is at most the expectation of X over a.

@art mass-far-out
Here's why. Write the expectation as a sum of each value times its probability. Every term is non negative. Throw away the terms below a, and the sum can only shrink. In what's left, every value is at least a, so replace each by a. You're left with a times the probability that X is at least a. Divide by a.

@art lever-mass
Think of it as a balance. Probability sitting far out is expensive. Every bit of it at or above a contributes at least a to the mean, so there can't be much of it.

@words text="tight: X = a with probability E[X]/a, else 0"
That bound is attained. A variable that equals a with probability E of X over a, and zero otherwise, meets it exactly. So you can't improve it without adding a hypothesis.

@chapter Chebyshev's inequality
@math heading="Chebyshev" items="Y = (X − μ)² ≥ 0,  E[Y] = Var(X)@Let Y be;;|X − μ| ≥ t  ⟺  Y ≥ t²@the same event;;P(|X − μ| ≥ t) ≤ Var(X)/t²@at most the variance;;t = kσ  ⟹  ≤ 1/k²@k sigma"
That extra hypothesis is a variance. Let Y be X minus mu, squared. It's never negative, and its expectation is the variance. Being t away from the mean is the same event as Y being at least t squared. So Markov gives a probability at most the variance over t squared. With t equal to k sigma, that's one over k squared.

@art two-tails
It's two lines, because Markov did the work. Nothing assumed the distribution was symmetric or had one peak. That's why it's valid for a simulation whose output distribution nobody has written down.

@chapter Measuring the slack
@art jagged-tail
And neither inequality needs a smooth shape. They hold for the jagged comparison count distribution just as readily.

@words text="n = 10:  E[C] = 30791/1260 ≈ 24.44" sub="Var(C) = 4913659/317520 ≈ 15.48"
Quicksort on ten keys is the perfect test, because the lab knows the whole distribution exactly. The expected count is about twenty four point four four, and the variance about fifteen point four eight.

@math heading="Markov on ten keys" items="a = 24:  truth 0.492,  bound 1.018@twenty four;;a = 36:  truth 0.0138,  bound 0.679@thirty six;;a = 45:  truth 0.00014,  bound 0.543@forty five"
At twenty four comparisons, the true tail is about point four nine two, and Markov allows one point zero one eight. Above one. True, and useless. At thirty six, the truth is point zero one three eight and the bound is point six seven nine. At forty five, the bound overstates the truth by a factor near three thousand eight hundred and forty nine.

@art bound-vs-truth
Markov decays like one over a. Chebyshev decays like one over t squared, so it's sharper further out. At t equals fifteen it allows point zero six nine, against a truth of point zero zero two, a factor of thirty four. At t equals three it's vacuous too, because three is less than one standard deviation.

@chapter Three ways to ask
@art three-routes
Why not just measure the tail instead? You can, and the lab does, beside the bounds. Over a hundred and twenty seeds, sixty runs reached twenty four comparisons, a half, against a true tail of about point four nine two. Close, and it's a measurement.

@list heading="How likely is a bad run?" items="Enumerate: exact, when you can compute it@Enumeration|Measure: always available, proves nothing unseen@measurement|Bound: two numbers, every distribution, loose@bound"
So there are three ways to ask how likely a bad run is. Enumeration is exact, but only when the distribution can be computed. A measurement is always available, and says nothing about outcomes no seed reached. A bound needs two numbers, holds for every distribution with those numbers, and is loose by a factor this page prints.

@chapter Where people slip
@list heading="Common slips" items="Quoting a bound greater than one@The first|Applying Markov to a negative variable@The second|Reading Chebyshev as one-sided@And the third"
The first slip is quoting a bound above one. Compare every bound with one before using it. The second is applying Markov to something that can be negative, like a deviation. Square it first. And the third is reading Chebyshev's two sided bound as an equality for one tail, or halving it. The two tails here are nowhere near equal.

@end text="Measure the slack"
Slide the threshold and watch both bounds against the truth, on Learn. That's learn dot get er done dot I O.
