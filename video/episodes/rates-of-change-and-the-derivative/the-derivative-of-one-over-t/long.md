---
format: long
lesson: rates-of-change-and-the-derivative/the-derivative-of-one-over-t
title: The derivative of 1/t, from two fractions
thumb: Minus one over a squared
---

@chapter Not a polynomial
@title text="The Derivative of 1/t" sub="Rates of Change and the Derivative" art=thumb
One over t isn't a polynomial, so there's nothing to expand. But its difference quotient can still be simplified exactly. The trick is to subtract the two fractions first.

@art hyperbola
Here's the graph of one over t, for positive t. It falls fast near zero and flattens out as t grows. So you'd expect its rate to be negative, and steeper where t is small.

@chapter Combine the fractions
@art common-denominator
The quotient has a fraction inside a fraction. The way through is to write one over a plus h, minus one over a, over a common denominator, a times a plus h.

@math heading="f(t) = 1/t" items="1/(a + h) − 1/a = (a − (a + h)) / (a·(a + h))@Over the common denominator;;= −h / (a·(a + h))@minus h over;;÷ h:  −1 / (a·(a + h))@Divide by h"
Over the common denominator, the top is a minus a plus h, which is minus h. So the difference is minus h over a times a plus h. Divide by h, and the quotient is minus one over a times a plus h.

@words text="h is a factor of the top" sub="so the zero leaves the denominator"
That h on top is the whole point, just as in the polynomial lesson. Once it's divided out, the quotient has no zero left in its denominator.

@chapter One step by hand
@math heading="a = 2,  h = 1/4" items="1/(9/4) = 4/9@four ninths;;4/9 − 1/2 = −1/18@minus one eighteenth;;(−1/18) ÷ (1/4) = −2/9@Divide by a quarter;;formula:  −1/(2·(9/4)) = −2/9@the formula"
Check it at two, with a step of a quarter. The long way first. One over nine quarters is four ninths. Four ninths minus a half is minus one eighteenth. Divide by a quarter, and you get minus two ninths. And the formula gives the same, minus two ninths.

@chapter The column
@math heading="a = 2:  −1/(2·(2 + h))" items="h = 1:  −1/6@minus one sixth;;h = 1/2:  −1/5@minus one fifth;;h = 1/4:  −2/9@minus two ninths;;h = 1/8:  −4/17@minus four seventeenths;;→ −1/4@heads for"
Now halve the step again and again at two. The column is minus one sixth, minus one fifth, minus two ninths, minus four seventeenths, and on. It heads for minus a quarter, though, as always, no row reaches it.

@art negative-column
Every one of those is negative, and each sits a little lower than the last, by a smaller and smaller amount. The gaps from minus a quarter shrink as the step does, just as the gaps did for t squared.

@art secants-on-hyperbola
Why minus a quarter? The denominator, two times two plus h, heads for four as the step shrinks. In general, a times a plus h is a squared plus a h, which differs from a squared by a h, and that can be made as small as you like.

@chapter The derivative
@words text="f′(a) = −1/a²" sub="for every a ≠ 0"
So for every place a other than zero, the derivative of one over t is minus one over a squared. It's negative, because one over t falls.

@math heading="Two more places" items="a = 1:  −1/2, −2/3, −4/5, −8/9 …  → −1@At one;;a = 1/2:  −4/3 …  → −4@At a half"
At one, the column is minus a half, minus two thirds, minus four fifths, minus eight ninths, heading for minus one. At a half, it starts at minus four thirds and heads for minus four. Both agree with minus one over a squared.

@art steep-near-zero
The rate is steeper where t is smaller, which fits the graph. And at one the slope is minus one, so the tangent line through one, one is y equals minus t plus two. That's the line from the last lesson, which ran below the curve, because one over t bends upward away from it.

@chapter Where people slip
@list heading="Common slips" items="Calling the derivative 1, or ln t@The first|Applying a polynomial rule to a fraction@The second|Forgetting that a can't be 0@The third"
The first slip is calling the derivative one, or the log of t. Every quotient at one is negative, so the answer can't be positive. The second is applying a polynomial rule to a fraction. Skip combining the fractions, and there's no h to cancel. The third is forgetting that a can't be zero.

@art hole-at-zero
One over t has no value at zero, so there's no quotient there and no derivative, and minus one over a squared is undefined. The lab refuses that place, rather than print something.

@chapter Try it
@words text="1/t at a = 3" sub="check: at h = 1 the quotient is −1/12"
Your turn. Find the derivative of one over t at three, from the formula. Then check that the quotient at a step of one is minus one twelfth.

@end text="Combine, cancel, approach"
You can watch the column of quotients head for minus one over a squared, on Learn. That's learn dot get er done dot I O.
