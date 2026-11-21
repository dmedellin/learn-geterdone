---
format: long
lesson: first-order-linear-equations/the-integrating-factor
title: The integrating factor: the product rule read backwards
thumb: Make the left side a derivative
---

@chapter The question
@title text="The Integrating Factor" sub="First-Order Linear Equations" art=thumb
The left side of y prime plus p y equals q is almost the derivative of something, and not quite. y prime alone is the derivative of y. The extra p y spoils it. Can you fix that with one multiplication?

@art product-rule
A product mu times y has the derivative mu times y prime, plus mu prime times y. That's the same two term shape. The only question is whether some mu makes the second term p times mu times y.

@chapter The condition
@math heading="If μ′ = p·μ" items="(μ·y)′ = μ·y′ + μ′·y@product rule;;= μ·y′ + p·μ·y@Replace;;= μ·(y′ + p·y)@mu times"
Suppose mu prime equals p times mu. The product rule gives mu times y prime, plus mu prime times y. Replace mu prime by p mu, and that's mu times y prime plus p y. So multiplying the left side by mu turns it into the derivative of mu y.

@words text="(μ·y)′ = μ·q"
And if y prime plus p y equals q, the whole equation becomes the derivative of mu y equals mu times q. Now you can integrate.

@chapter Finding μ
@math heading="Two easy families" items="p = a:   μ = e^(a·t)@constant;;p = a/t:   μ = tᵃ@a over t;;p = 2/t:   μ′ = 2t = (2/t)·t²  ✓@two over t"
For a constant p equals a, mu is e to the a t, since its rate is a times itself. For p equals a over t, mu is t to the a, by the power rule. For two over t, mu is t squared. Its rate is two t, and two over t times t squared is also two t.

@math heading="In general" items="μ = e^(∫p dt)@e to the integral;;μ′ = p·e^(∫p dt) = p·μ@chain rule"
In general, mu is e to the integral of p. The chain rule gives mu prime as p times mu, which is the condition. The exponent has to be an antiderivative of p.

@art wrong-exponent
Putting p itself in the exponent fails at once. For p equals three, e to the p is e cubed, a constant, so its rate is zero, not three e cubed. And which antiderivative doesn't matter. A different constant multiplies mu by a fixed factor, like five, and that cancels.

@chapter An exponential case
@math heading="y′ + 2y = e^t" items="μ = e^(2t)@mu is;;(e^(2t)·y)′ = e^(3t)@e to the three t"
Take y prime plus two y equals e to the t. Then mu is e to the two t, and the derivative of mu y is e to the two t times e to the t, which is e to the three t.

@math heading="Integrate, then divide" items="e^(2t)·y = (1/3)·e^(3t) + C@Integrate;;y = (1/3)·e^t + C·e^(−2t)@Divide by mu"
Integrate, and mu y is a third of e to the three t, plus C. Divide by mu, constant included, and y is a third of e to the t, plus C e to the minus two t. With no starting value, C stays free.

@chapter A case in fractions
@art two-cases
That one had an exponential factor. When p is a over t, the factor is a power of t, and every step stays in fractions.

@math heading="y′ + (2/t)·y = t²,  y(1) = 1" items="μ = t²@t squared;;(t²·y)′ = t⁴@t to the fourth;;t²·y = t⁵/5 + C@Integrate;;y = t³/5 + C/t²@Divide;;1/5 + C = 1,  C = 4/5@four fifths"
Here mu is t squared, and the derivative of t squared y is t to the fourth. Integrate: t to the fifth over five, plus C. Divide: t cubed over five plus C over t squared. At one, a fifth plus C is one, so C is four fifths.

@art check-substitute
Check by substituting. y prime is three t squared over five minus two C over t cubed. Two over t times y is two t squared over five plus two C over t cubed. They add to t squared, for every C.

@chapter Where people slip
@list heading="Common slips" items="Putting p in the exponent@The first|Multiplying only the left side by μ@The second|Adding C after dividing by μ@The third"
The first slip is putting p itself in the exponent instead of its antiderivative. The second is multiplying only the left side by mu. The third is adding C after dividing by mu, when the constant belongs to the integral.

@art left-only
Multiply only the left, and you get t squared y equals t cubed over three plus C, so y is t over three plus C over t squared. Substitute, and the sum is one, not t squared. The factor multiplies the right side too.

@words text="y = t³/5 + C  ✗" sub="gives t² + 2C/t"
And add C after dividing, and substituting leaves t squared plus two C over t, which works only when C is zero. The constant is divided with the integral.

@chapter The lab's limits
@art lab-limits
The lab takes a constant p, or a over t with a whole number from minus four to four. It won't integrate when a log of t would appear, and for a over t it needs a starting time other than zero. Those are limits of the lab. The integrating factor itself has no such limit.

@chapter Try it
@words text="y′ + (2/t)·y = t²,  y(1) = 1" sub="target: y = t³/5 + 4/(5t²)"
Your turn. Work through this one yourself: find mu, integrate mu times q, divide by mu with the constant included, and fit the constant at t equals one. Then substitute to check.

@end text="Multiply by μ, then integrate"
You can try constant and a over t cases, solved in exact fractions, on Learn. That's learn dot get er done dot I O.
