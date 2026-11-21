---
format: long
lesson: discrete-probability/binomial-distribution
title: The binomial distribution: counting successes in n trials
thumb: n trials, k successes
---

@chapter The setup
@title text="Bernoulli Trials and the Binomial Distribution" sub="Discrete Probability" art=thumb
Flip a coin ten times and count heads. Guess twenty multiple choice answers and count how many are right. Each time, you're counting successes in a fixed number of independent tries.

@art coin-sequence
One try with two outcomes is a Bernoulli trial: success with probability p, failure with probability one minus p. Its indicator has mean p and variance p times one minus p.

@chapter The formula
@math heading="Binomial distribution" items="P(X = k) = C(n, k) pᵏ (1 − p)ⁿ⁻ᵏ@n choose k;;k = 0, 1, …, n@from zero up to n"
If X counts the successes in n independent trials, each with probability p, then the probability of k successes is n choose k, times p to the k, times one minus p to the n minus k, for k from zero up to n.

@art arrangements
Here's where it comes from. One particular sequence with k successes and n minus k failures has probability p to the k times one minus p to the n minus k, by independence. And the number of such sequences is the number of ways to choose which k trials succeed: n choose k.

@words text="Σ = (p + (1 − p))ⁿ = 1"
Those sequences are disjoint, so you add them. And the probabilities sum to one by the binomial theorem: p plus one minus p, all to the n, is one.

@chapter Mean and variance
@math heading="Mean and variance" items="X = I₁ + ⋯ + Iₙ@a sum of n indicators;;E[X] = np@n p;;Var(X) = np(1 − p)@one minus p"
Write X as a sum of n indicators, one per trial. By linearity, the mean is n p, with no independence needed for that step. For the variance, independence is needed. The variances add, giving n p times one minus p.

@art variance-peak
The variance is largest at p equals one half, where it's n over four. And it vanishes at p equals zero and p equals one. A trial that always succeeds or always fails has no spread.

@chapter Two examples
@math heading="Ten coin flips" items="P(X = 5) = C(10, 5) / 2¹⁰@ten choose five;;= 252 / 1024 ≈ 0.246@two hundred fifty-two"
Ten coin flips, p one half. The chance of exactly five heads is ten choose five over two to the ten. That's two hundred fifty-two over ten twenty-four, about zero point two four six. Slightly under a quarter, which surprises people who expect the most likely value to be likely.

@art defect-batch
A process makes two percent defectives. In a batch of a hundred, the expected number of defects is two. The chance of no defects is zero point nine eight to the hundredth, about zero point one three three. So about one batch in eight is clean.

@chapter Guessing a test
@art binomial-hump
Twenty questions, four options each, answered at random. That's twenty trials, each succeeding with probability one quarter. How many will you get right?

@math heading="20 questions, 4 options, at random" items="E[X] = 20 × 0.25 = 5@five;;Var(X) = 20 × 0.25 × 0.75 = 3.75,  σ ≈ 1.94@three point seven five;;P(X = 5) ≈ 0.2023@exactly five;;P(X ≥ 10) = 1 − P(X ≤ 9) ≈ 0.0139@at least ten"
The mean is twenty times a quarter, five. The variance is three point seven five, so sigma is about one point nine four. The chance of exactly five right is about zero point two zero two three. And the chance of at least ten is one minus the chance of nine or fewer, about zero point zero one three nine.

@words text="Pass by guessing: about 1 in 72" sub="Chebyshev only guarantees ≤ 15%"
So passing at fifty percent by guessing happens about once in seventy-two attempts. Ten is about two point six standard deviations above the mean, and Chebyshev would only promise at most fifteen percent. Knowing the distribution buys precision.

@chapter Where the model breaks
@list heading="Assumptions" items="Fixed n@Fixed n|Independent trials@independent trials|Constant p@constant p"
The binomial needs three things: fixed n, independent trials, and constant p.

@art urn-draws
Sampling without replacement breaks them. Draw five cards, and the chance of an ace changes with every draw. That's hypergeometric, and the binomial is only a good approximation when the sample is small next to the population. Weather on consecutive days isn't independent either.

@words text="Mean about right, variance too small"
And the failure has a typical shape. The mean stays about right, while the variance is wrong, usually too small. So the extremes are far more likely than the model predicts, exactly where a wrong model does damage.

@list heading="Common slips" items="Using it without replacement@without replacement|Forgetting the binomial coefficient@coefficient|Assuming the mean is the likely value@the likely value"
Three slips. Using it for sampling without replacement. Forgetting the binomial coefficient, which counts the arrangements. And assuming the mean is the likely value. At a hundred flips, the chance of exactly fifty heads is only about eight percent.

@chapter Try it
@words text="n = 10, p = 0.3: E[X]?" sub="then Var(X)"
Your turn. With ten trials and p equal to zero point three, find the mean using n p. Then find the variance and the standard deviation, and check whether the chance of hitting the mean exactly is large or small.

@end text="Check n, independence, p"
The full lesson, with a lab where you can move n and p, is on Learn. That's learn dot get er done dot I O.
