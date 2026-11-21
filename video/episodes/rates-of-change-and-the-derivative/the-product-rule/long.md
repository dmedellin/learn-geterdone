---
format: long
lesson: rates-of-change-and-the-derivative/the-product-rule
title: The product rule, and why it isn't f′ times g′
thumb: A product changes twice
---

@chapter The question
@title text="The Product Rule" sub="Rates of Change and the Derivative" art=thumb
You can always multiply two polynomials out and differentiate term by term. But sometimes the factors are better left as they are. So what's the derivative of a product?

@math heading="f(t) = t²,  g(t) = t + 1" items="f·g = t³ + t²@Multiplied out;;(f·g)′ = 3t² + 2t@the power rule;;✗  f′·g′ = 2t·1 = 2t@tempting"
Take t squared times t plus one. Multiplied out, it's t cubed plus t squared, and the power rule gives three t squared plus two t. The tempting rule is to differentiate each factor and multiply. Two t times one is two t. That's wrong.

@art degree-towers
And it can't possibly be right. The true derivative has degree two, and two t has degree one. No choice of coefficients could fix that.

@chapter The idea
@art growing-rectangle
Picture a rectangle with width f and height g. Its area is f times g. If the width grows, the area gains a strip along the side, as tall as the old height. If the height grows, it gains a strip along the top, as wide as the old width.

@math heading="The product rule" items="(f·g)′ = f′·g + f·g′@f prime g"
The rate of the area is the sum of the two strips' rates. That's the product rule: f prime g, plus f g prime. Each term holds one factor still, and differentiates the other.

@chapter Why it works
@math heading="Add and subtract f(t)·g(t + h)" items="f(t + h)·g(t + h) − f(t)·g(t)@The top;;= [f(t + h) − f(t)]·g(t + h) + f(t)·[g(t + h) − g(t)]@regroup"
Here's the algebra. The top of the quotient is f of t plus h, times g of t plus h, minus f of t times g of t. Add and subtract f of t times g of t plus h, then regroup.

@art two-strips
Now divide by h. You get the quotient of f, times g of t plus h, plus f of t, times the quotient of g. Read off the parts that are free of h: f prime, g, and g prime. That's f prime g, plus f g prime.

@chapter Checking it
@math heading="t² and t + 1" items="f′·g = 2t·(t + 1) = 2t² + 2t@F prime g;;f·g′ = t²·1 = t²@f g prime;;sum:  3t² + 2t  ✓@Add them"
Check it on t squared and t plus one. F prime g is two t times t plus one, which is two t squared plus two t. And f g prime is t squared times one. Add them, and you get three t squared plus two t, the same as the expansion.

@math heading="f = t³ − t,  g = t² + 2" items="f′·g = (3t² − 1)(t² + 2) = 3t⁴ + 5t² − 2@F prime g;;f·g′ = (t³ − t)·2t = 2t⁴ − 2t²@f g prime;;sum:  5t⁴ + 3t² − 2@They add;;expanded:  t⁵ + t³ − 2t  →  5t⁴ + 3t² − 2@Expand first"
A bigger pair. F prime g is three t to the fourth, plus five t squared, minus two. And f g prime is two t to the fourth minus two t squared. They add to five t to the fourth, plus three t squared, minus two. Expand first, and you get the same.

@chapter A square
@art square-growing
Put g equal to f, and the rule says the derivative of f squared is two f f prime. For t plus one, the square is t squared plus two t plus one, with derivative two t plus two. The rule gives two times t plus one, times one. The same.

@art agree-at-points
Now square t squared. The true derivative of t to the fourth is four t cubed, and the wrong rule gives four t squared. At zero and at one they agree, so a check at either place would pass the wrong rule. But the degrees, three against two, say they're different.

@chapter Where people slip
@list heading="Common slips" items="(f·g)′ = f′·g′  ✗@the product of the derivatives|Keeping only one of the two terms@only one|(f²)′ = (f′)²  or  2f′  ✗@a square"
The first slip is the product of the derivatives. Even t times t shows it: the derivative of t squared is two t, not one times one. The second is keeping only one of the two terms. The third is getting a square wrong. The function itself stays in the answer.

@art lone-strip
For t times t, each term of the rule is t, and either one alone is half the answer. With one strip, you've counted only half of how the area grows. So when a term seems to vanish, check that its factor really is a constant.

@chapter Try it
@words text="t·(t² + 1)" sub="by the rule, then by expanding"
Your turn. Differentiate t times t squared plus one. Do it first by the rule, then by expanding, and compare.

@end text="Two strips, one sum"
You can check the product rule against the expansion for any pair of polynomials, on Learn. That's learn dot get er done dot I O.
