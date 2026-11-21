---
format: long
lesson: rates-of-change-and-the-derivative/the-chain-rule
title: The chain rule: outer rate, times inner rate
thumb: Don't forget the inside
---

@chapter The question
@title text="The Chain Rule" sub="Rates of Change and the Derivative" art=thumb
What happens when one function is fed into another? Take three t plus one, and square it. Multiplied out, that's nine t squared plus six t plus one, so its derivative is eighteen t plus six. But can you get there without expanding?

@art two-machines
Think of it as two machines. The inner one, g, turns t into three t plus one. The outer one, f, squares whatever it's given. The whole thing is f of g of t. And which one is inside matters. G of f of t would be three t squared plus one, a different function.

@chapter A missing factor
@math heading="f(t) = t²,  g(t) = 3t + 1" items="f′(t) = 2t@the outer function;;f′(g(t)) = 2(3t + 1) = 6t + 2@at the inner value;;✗  6t + 2 ≠ 18t + 6@off by"
The derivative of the outer function is two t. Read at the inner value, that's two times three t plus one, which is six t plus two. But that isn't eighteen t plus six. It's off by a factor of three.

@art missing-factor
And three is the derivative of the inner function, three t plus one. Multiply six t plus two by three, and you get eighteen t plus six.

@chapter The chain rule
@math heading="The chain rule" items="(f(g(t)))′ = f′(g(t))·g′(t)@f of g of t"
So here's the rule. The derivative of f of g of t is f prime of g of t, times g prime of t. The outer rate, read at the inner value, times the inner rate.

@art gears
Why multiply? If t moves by a small step, the inner function moves by g prime times that step. Then the outer function moves by f prime times what its input moved. The rates multiply along the chain. It's the outer rate, taken where the outer function is standing, times the rate the inner function carries it.

@chapter Why it's true
@math heading="u = g(t)" items="n = 1:  u′ = u′@n equals one;;(uⁿ⁺¹)′ = (uⁿ·u)′@The product rule;;= n·uⁿ⁻¹·u′·u + uⁿ·u′@gives;;= (n + 1)·uⁿ·u′@times u to the n, times u prime"
For polynomials, it comes from the product rule. Write u for g of t. For n equals one, the claim just says u prime equals u prime. If it holds for n, write u to the n plus one as u to the n times u. The product rule gives n plus one, times u to the n, times u prime.

@art staircase
So the claim passes from each power to the next, from one to two, from two to three, and on to every power. A polynomial is a sum of constants times powers, so the rule holds for every polynomial.

@chapter A power of a function
@math heading="f(t) = t³,  g(t) = t² + 1" items="f′(g(t)) = 3(t² + 1)²@three times t squared plus one;;g′(t) = 2t@The inner derivative;;6t·(t² + 1)² = 6t⁵ + 12t³ + 6t@product;;check:  (t² + 1)³ = t⁶ + 3t⁴ + 3t² + 1  →  6t⁵ + 12t³ + 6t@Expanding first"
Now t squared plus one, cubed. The outer derivative read at the inner value is three times t squared plus one, squared. The inner derivative is two t. Their product expands to six t to the fifth, plus twelve t cubed, plus six t. Expanding first agrees.

@chapter Shifts and stretches
@art shift-same-slope
With t minus four, squared, the rule gives two times t minus four, times one. The inner derivative is one, so the chain factor is invisible. A shift moves the graph without changing how steep it is.

@art stretch-steeper
A stretch is different. A stretch by three makes every slope three times as large. So for f of k t plus c, the derivative is k times f prime of k t plus c. The constant c never shows up in the multiplier, and k always does.

@chapter Where people slip
@list heading="Common slips" items="Forgetting the inner derivative@forgetting|Writing f′(t) instead of f′(g(t))@instead of|Multiplying by g instead of g′@by the inner function"
The first slip is forgetting the inner derivative, which leaves you off by exactly that factor. The second is reading the outer derivative at t instead of at g of t. For t squared plus one, cubed, at one, the true slope is twenty four, and that slip gives six. The third is multiplying by the inner function instead of its derivative.

@chapter Try it
@words text="(2t + 5)³" sub="outer: 3(2t + 5)²    inner: 2"
Your turn. Differentiate two t plus five, cubed, by the rule. The outer derivative read at the inner value is three times two t plus five, squared. The inner derivative is two. Multiply them, then check by expanding.

@end text="Outer rate, times inner rate"
You can check the chain rule against the expansion, for any pair of polynomials, on Learn. That's learn dot get er done dot I O.
