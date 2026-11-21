---
format: long
lesson: discrete-probability/linearity-of-expectation
title: Linearity of expectation: add first, no independence needed
thumb: Add first, always
---

@chapter The idea
@title text="Linearity of Expectation" sub="Discrete Probability" art=thumb
Here's the most useful fact in elementary probability. The expectation of a sum is the sum of the expectations. And it holds whether or not the variables are independent.

@math heading="Linearity of expectation" items="E[aX + bY] = a E[X] + b E[Y]@a times the expectation;;no independence needed@No independence"
For random variables X and Y on the same sample space, and constants a and b, the expectation of a X plus b Y is a times the expectation of X, plus b times the expectation of Y. No independence assumption at all.

@chapter Why it's true
@math heading="Sum over outcomes" items="E[aX + bY] = Σ_s (aX(s) + bY(s)) P(s)@sum over outcomes;;= a Σ_s X(s)P(s) + b Σ_s Y(s)P(s)@split the sum;;= a E[X] + b E[Y]@which is"
Sum over outcomes. The expectation is the sum of a X of s plus b Y of s, times P of s. Split the sum into two pieces, and each piece is an expectation, which is a times the expectation of X plus b times the expectation of Y.

@art sum-stacks
Nothing about how X and Y behave together ever entered. That's exactly why independence isn't required. The proof is three lines, and the consequence is enormous.

@chapter Indicators
@math heading="Indicator" items="E[I_A] = 1 · P(A) + 0 · P(Ā) = P(A)@one times;;X = I_{A₁} + ⋯ + I_{Aₙ}  ⟹  E[X] = Σ P(Aᵢ)@counts how many"
The expectation of an indicator is one times P of A plus zero times P of not A, which is just P of A. So if X counts how many of some events happen, X is a sum of indicators, and its expectation is the sum of their probabilities.

@art indicator-lamps
The events can overlap, depend on each other, or be governed by anything at all. Take heads in n flips. Each flip's indicator has expectation p, so the expected number of heads is n p. You never need the binomial distribution.

@chapter The hat problem
@art hats-pegs
Shuffle n things into a random order, and count how many end up in their own place. Those are the fixed points of a random permutation.

@math heading="Fixed points" items="X = Σ Iᵢ,  Iᵢ = 1 if i is fixed@the indicator;;P(Iᵢ = 1) = 1/n@one over n;;E[X] = n · (1/n) = 1@exactly one"
Let I i be the indicator that element i stays in place. Each has probability one over n. So the expectation is n times one over n, which is exactly one, for every n.

@words text="5 people or 5 million: one hat back"
On average, exactly one person gets their own hat back, whether there are five people or five million. And the indicators are dependent. If n minus one elements are fixed, the last one must be too. Linearity doesn't care.

@chapter Two decks
@art two-decks
The same idea works for two shuffled decks of n cards dealt side by side. How many positions match? Let I j be one if position j matches.

@math heading="Matching pairs" items="P(Iⱼ = 1) = 1/n@one chance in n;;E[X] = Σⱼ E[Iⱼ] = n · (1/n) = 1@By linearity"
Whatever card is in the first deck at position j, the second deck has one chance in n of matching it. By linearity, the expectation is n times one over n, which is one. Doing this from the full distribution would need the derangement numbers, all for one number.

@chapter Collecting coupons
@art coupon-grid
There are n different coupons, one per box, at random. How many boxes do you need to collect them all? Break the wait into stages, one for each new coupon.

@math heading="Coupon collector" items="E[Xᵢ] = n / (n − i + 1)@n over;;E[total] = n(1 + 1/2 + ⋯ + 1/n)@add up;;n = 50  ⟹  about 225 boxes@fifty"
While you hold i minus one distinct coupons, the expected wait for a new one is n over n minus i plus one. Add up the stages, and the total is n times one plus a half plus and so on up to one over n. For fifty coupons, that's about two hundred twenty-five boxes.

@chapter Products are different
@art linked-pair
Here's the one real trap. If X and Y are independent, the expectation of X times Y is the product of their expectations. Without independence, that can fail.

@math heading="Y = X, a fair coin scored 0 or 1" items="E[X] = 1/2@one half;;E[XY] = E[X²] = 1/2@X squared;;E[X]E[Y] = 1/4  ✗@one quarter"
Let X be a fair coin scored zero or one, and let Y just be X. Then the expectation of X is one half. The expectation of X Y is the expectation of X squared, which is also one half. But the product of the expectations is one quarter.

@list heading="Common slips" items="Checking independence before adding@before adding|Applying linearity to a product@to a product|Missing the indicator decomposition@indicator decomposition"
So, three slips. Checking independence before adding is unnecessary: add first. Applying linearity to a product is wrong. And not looking for an indicator decomposition makes easy problems hard.

@chapter Try it
@words text="52-card decks: expected matches?" sub="one indicator per position"
Your turn. Two shuffled fifty-two card decks are dealt face up side by side. Write the number of matching positions as a sum of indicators, find one indicator's expectation, and add.

@end text="Expectation adds, always"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
