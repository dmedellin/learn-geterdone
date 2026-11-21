---
format: long
lesson: discrete-probability/random-variables
title: Random variables: neither random nor a variable
thumb: It's a function
---

@chapter The idea
@title text="Random Variables" sub="Discrete Probability" art=thumb
Roll two dice, and you usually care about one number: the sum. Flip three coins, and you care about how many heads. A random variable is that number, attached to each outcome.

@math heading="Random variable" items="X : S → ℝ@a function;;X = k  is the event  {s ∈ S : X(s) = k}@the event;;P(X = k)@its probability"
Formally, a random variable on a sample space S is a function from S to the real numbers. One value for each outcome. The event X equals k is the set of outcomes that X sends to k, and P of X equals k is its probability.

@art function-arrows
The name is doubly misleading. X is a function, and it's completely determined. Nothing about it is random. What varies is which outcome occurs. Read X as a function on outcomes, and most of the confusion goes away.

@chapter Distributions
@words text="(k, P(X = k))" sub="non-negative, summing to 1"
The distribution of X is the list of its values, each paired with its probability. Those probabilities are non-negative, and they add up to one. It's a summary: it forgets which outcomes gave each value, which is usually exactly what you want.

@art triangle-bars
Take the sum of two dice. The sample space is the thirty-six pairs, and X of a, b is a plus b. The sum two comes from one pair, three from two pairs, and so on up to seven from six pairs, then back down again.

@math heading="Sum of two dice" items="k:      2  3  4  5  6  7  8  9  10  11  12@The sums;;pairs:  1  2  3  4  5  6  5  4  3  2  1@the counts;;P(X = k) = pairs / 36@over thirty-six;;Σ pairs = 36  ⟹  Σ P = 1  ✓@a free check"
The sums run from two to twelve, and the counts make a triangle: one, two, three, four, five, six, five, four, three, two, one. Each probability is the count over thirty-six. The counts add up to thirty-six, so the probabilities add up to one. That's a free check that catches missed cases.

@chapter Indicators
@art indicator-switch
For any event A, the indicator of A is the random variable that's one when A happens and zero otherwise. So the probability it equals one is just P of A.

@words text="Any count = a sum of indicators"
Indicators look trivial. They're actually the single most useful tool in the lesson on linearity of expectation, because any count can be written as a sum of indicators.

@chapter Several at once
@art joint-table
With two variables, the joint distribution gives P of X equals a and Y equals b, for every pair of values. They're independent when every entry is the product of P of X equals a and P of Y equals b.

@words text="X = first die, Y = sum" sub="P(Y = 2 | X = 3) = 0,  P(Y = 2) = 1/36"
Variables on the same space can be dependent by construction. Let X be the first die and Y the sum. The chance Y is two, given X is three, is zero. But P of Y equals two is one over thirty-six. Knowing X restricts Y sharply.

@chapter Three coins
@art coin-row
Flip three coins. There are eight outcomes, each with probability one eighth. Let X be the number of heads, and let Y be one if the first flip is heads, and zero otherwise.

@math heading="Three coins" items="X:  P(0) = 1/8,  P(1) = 3/8,  P(2) = 3/8,  P(3) = 1/8@three eighths;;Y:  P(0) = 1/2,  P(1) = 1/2@one half each;;P(X = 3, Y = 1) = 1/8@all heads;;P(X = 3) P(Y = 1) = 1/16  ⟹  dependent@one sixteenth"
X takes zero, one, two, three with probabilities one eighth, three eighths, three eighths, one eighth. Y is zero or one, one half each. Now, X is three and Y is one only for all heads, so one eighth. But the product is one eighth times one half, one sixteenth. They're dependent.

@words text="Y is part of X"
That's no surprise. Y is part of X. In fact X is the sum of three indicators, one for each flip, and that decomposition is exactly what the next lessons use.

@chapter Where people slip
@list heading="Common slips" items="Treating X as random, not as a function@rather than as a function|Confusing the value with the event@the value with the event|Assuming variables on one space are independent@are independent"
First, treating X as random rather than as a function. Second, confusing the value with the event. X equals three is a set of outcomes, and P of X equals three is the probability of that set. Third, assuming variables on the same space are independent. Check the joint distribution.

@art same-shape
And one more thing. Different variables can share a distribution. The number of heads in three flips and the number of tails have the same distribution, yet they're different functions.

@chapter Try it
@words text="Three coins: Z = number of tails" sub="find its distribution"
Your turn. With the same three coins, let Z be the number of tails. Write its distribution, check it sums to one, and compare it with the distribution of X. Then ask: is Z the same function as X?

@end text="A random variable is a function"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
