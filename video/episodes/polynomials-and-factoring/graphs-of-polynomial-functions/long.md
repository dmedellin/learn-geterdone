---
format: long
lesson: polynomials-and-factoring/graphs-of-polynomial-functions
title: Sketching polynomial graphs from the factored form
thumb: Cross or touch?
---

@chapter The question
@title text="Graphs of Polynomial Functions" sub="Polynomials and Factoring" art=thumb
Give me a polynomial in factored form, and without plotting a single table of values, you can sketch its graph. The degree and the leading coefficient fix the ends. Each factor fixes where the curve meets the axis.

@art smooth-curve
Polynomial graphs are continuous and smooth. No jumps, no corners, no asymptotes. What you'll draw is a qualitative sketch, not an exact plot, because these facts don't locate every turning point.

@chapter End behaviour
@art four-ends
The leading term decides both ends. If the degree is even, the two ends go the same way: both up when the leading coefficient is positive, both down when it's negative. If the degree is odd, they go opposite ways.

@math heading="Why" items="f(x) = xⁿ(aₙ + aₙ₋₁/x + … + a₀/xⁿ)@factor out;;→ aₙxⁿ  as |x| grows@every term after"
The reason is division, not intuition. Factor out x to the n. Every term after a n in the bracket tends to zero as x grows, so the sign of f follows a n x to the n.

@art far-ends
So the constant term and the number of roots tell you nothing about the ends. x cubed minus a hundred and x cubed plus a hundred behave identically far out, however different they look near the origin.

@chapter Cross or touch
@math heading="Multiplicity" items="(x − c)ᵏ divides f, (x − c)ᵏ⁺¹ does not@divides f;;odd k: crosses · even k: touches@odd multiplicity"
If x minus c to the k divides f, but x minus c to the k plus one does not, c is a root of multiplicity k. At a root of odd multiplicity, the graph crosses the axis. At even multiplicity, it touches and goes back.

@art cross-and-touch
Why? Passing c from left to right, x minus c changes sign. So x minus c to the k changes sign exactly when k is odd. The other factors aren't zero near c, so they keep their signs.

@chapter A worked sketch
@math heading="f(x) = (x + 2)(x − 1)²(x − 3)" items="degree 4 · leading coefficient 1 → both ends rise@degree four;;−2: multiplicity 1, crosses@minus two;;1: multiplicity 2, touches@one has multiplicity two;;3: multiplicity 1, crosses@three has"
f of x equals x plus two, times x minus one squared, times x minus three. Degree four, leading coefficient one, so both ends rise. The roots: minus two with multiplicity one, so it crosses. One has multiplicity two, so it touches. And three has multiplicity one, so it crosses.

@math items="f(0) = (2)(1)(−3) = −6@f of zero"
The y-intercept is f of zero, which is two times one times minus three, minus six. In factored form, it's the product of the constants.

@art the-sketch
That's enough for a sketch. Coming down from the upper left, the curve crosses at minus two into negative values. It rises to touch the axis at one without crossing, falls back below, and crosses at three on its way up.

@math heading="Sample values" items="f(−3) = 96@minus three;;f(0) = −6@zero;;f(2) = −4@two;;f(4) = 54@four"
Sample values confirm it. f of minus three is ninety-six. f of zero is minus six. f of two is minus four. And f of four is fifty-four. Negative on both sides of one, as an even multiplicity predicts.

@words text="1 + 2 + 1 = 4" sub="four roots with multiplicity · three points on the axis"
The multiplicities add to four, exactly the degree. A degree n polynomial has at most n roots, counted with multiplicity. Here that's four roots, at three distinct points on the axis.

@art unforced-turn
A touch forces a turn at that root. But nothing here tells you where the other turning points are exactly. That takes calculus, so draw a qualitative sketch and let an evaluated plot check it.

@chapter Where people slip
@list heading="Common slips" items="Deciding the ends from the constant or the roots@The first|Drawing every root as a crossing@The second|Pretending the sketch locates every turn@The third"
The first slip is deciding the ends from the constant term or the number of roots. The second is drawing every root as a crossing. Treat x minus one squared as a crossing, and the curve is on the wrong side for a whole interval. The third is pretending the sketch locates every turn.

@chapter Try it
@words text="g(x) = −(x + 1)²(x − 2)" sub="degree 3, negative: left end rises, right end falls"
Your turn. g of x equals minus, x plus one squared, times x minus two. Degree three with a negative leading coefficient, so the left end rises and the right end falls. Mark the roots and multiplicities, find g of zero, and sketch.

@math items="touches at −1 · crosses at 2@touches at minus one;;g(0) = 2@g of zero is two"
It touches at minus one, crosses at two, and g of zero is two. If you crossed at minus one, you treated an even multiplicity as odd.

@end text="Change a factor, watch the axis"
You can change a factor's power and watch the curve switch between crossing and touching, on Learn. That's learn dot get er done dot I O.
