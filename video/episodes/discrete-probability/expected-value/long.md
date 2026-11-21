---
format: long
lesson: discrete-probability/expected-value
title: Expected value: the long-run average, and what it is not
thumb: No die shows 3.5
---

@chapter The idea
@title text="Expected Value" sub="Discrete Probability" art=thumb
If you played a game over and over, what would you win on average? That long-run average is the expected value. It's the most used number in probability, and also one of the most misread.

@math heading="Expected value" items="E[X] = Σ_k k · P(X = k)@each value;;E[X] = Σ_{s ∈ S} X(s) P(s)@over outcomes"
Take each value X can take, multiply it by its probability, and add them up. Equivalently, sum over outcomes instead: the value of X at each outcome, times that outcome's probability. That second form is often the more useful one.

@art balance-point
It's a weighted average. Each value is weighted by its probability. When the outcomes are equally likely, it's just the ordinary mean.

@chapter A fair die
@art die-bars
Roll a fair die. Each face from one to six has probability one sixth.

@math heading="A fair die" items="E[X] = (1 + 2 + 3 + 4 + 5 + 6) / 6@one plus two;;= 3.5@three point five"
So the expected value is one plus two plus three plus four plus five plus six, over six, which is three point five.

@words text="3.5 is not a face" sub="it's the long-run average of many rolls"
No die shows three point five, and that's not a defect. The expectation summarises the distribution, not any single roll. It's the long-run average of many rolls.

@chapter Shifting and scaling
@math heading="Linear transformation" items="E[aX + b] = a E[X] + b@a times;;E[aX + b] = a Σ X(s)P(s) + b Σ P(s)@split the sum"
For constants a and b, the expectation of a times X plus b is a times the expectation of X, plus b. To see why, split the sum into a times the sum of X of s P of s, plus b times the sum of the probabilities, which is one.

@art square-gap
But a function that isn't linear doesn't pass through like that. For a fair die, the expectation of X squared is ninety-one sixths, about fifteen point one seven. The square of the expectation is twelve point two five. They differ.

@words text="E[g(X)] ≠ g(E[X])" sub="E[X²] = 91/6 ≈ 15.17 · (E[X])² = 12.25"
In general, the expectation of g of X isn't g of the expectation. That gap is the reason variance is defined the way it is.

@chapter Fair games
@math heading="Pay £2, win £X" items="E[winnings] = 3.5 − 2 = £1.50@one pound fifty"
Here's a carnival game. Pay two pounds to roll a die, and win the face shown in pounds. Your expected winnings are three point five minus two, so one pound fifty per play in your favour. Nobody would offer that game.

@art roulette-wheel
European roulette has thirty-seven pockets. A one pound bet on a single number pays thirty-five to one.

@math heading="Roulette, £1 on one number" items="E[profit] = 35 · (1/37) − 1 · (36/37)@thirty-five times;;= −1/37 ≈ −£0.027@minus one over thirty-seven"
So the expected profit is thirty-five times one over thirty-seven, minus one times thirty-six over thirty-seven. That's minus one over thirty-seven, about minus two point seven pence per pound staked. A game is fair when the expected net gain is zero. Casinos are unfair by a small margin, on purpose.

@chapter Insurance
@art insurance-shield
A policy pays ten thousand pounds on an event with probability zero point zero zero two, and the premium is thirty pounds. Let X be the insurer's net gain on one policy.

@math heading="Insurer's gain" items="no claim: +30,  P = 0.998@no claim;;claim: 30 − 10000 = −9970,  P = 0.002@a claim;;E[X] = 29.94 − 19.94 = £10.00@ten pounds"
With no claim, the insurer gains thirty, with probability zero point nine nine eight. With a claim, it's thirty minus ten thousand, minus nine nine seven zero, with probability zero point zero zero two. So the expectation is twenty-nine ninety-four minus nineteen ninety-four, ten pounds per policy.

@words text="Customer: −£10 · both can be sensible"
The customer's expectation is exactly minus ten. Yet both can be acting sensibly. The customer removes a downside they couldn't absorb, and the insurer sells many policies, where the average approaches the expectation.

@chapter What it doesn't tell you
@list heading="Expectation is not" items="The most likely outcome@most likely|A guarantee@a guarantee|Enough to compare two options@compare two options"
Expectation is not the most likely outcome. The expected number of heads in three flips is one point five, which can't happen. It's not a guarantee: a game with positive expectation can lose for a long time. And it's not enough to compare two options, since equal expectations can hide very different risks.

@art skewed-bars
For skewed distributions, the mean can sit far from anything likely. The geometric distribution, later in this course, is the standard example.

@chapter Try it
@words text="Roulette: is every bet −1/37?" sub="try a bet that pays 1 to 1 on 18 pockets"
Your turn. The lesson says every bet on the wheel has the same expectation. Test it on a bet that pays one to one and covers eighteen of the thirty-seven pockets. Do you get minus one over thirty-seven again?

@end text="Expectation: the long-run average"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
