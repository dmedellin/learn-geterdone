---
format: long
lesson: rational-and-radical-expressions/radical-functions-and-their-graphs
title: Radical functions: solve for the domain, then sketch
thumb: The domain is an inequality
---

@chapter Solved for, not read off
@title text="Radical Functions and Their Graphs" sub="Rational and Radical Expressions" art=thumb
A radical function's domain isn't read off. It's solved for. An even index turns radicand at least zero into an inequality, and the answer to that inequality is the domain. Then the graph follows from the domain, the range, and a few exact points.

@math heading="Radical function" items="f(x) = ⁿ√(g(x))@f of x;;n even:  domain { x : g(x) ≥ 0 }@for even n;;n odd:  domain of g@for odd n"
A radical function puts the variable under a radical: f of x is the nth root of g of x. For even n, the domain is every x where g of x is at least zero. For odd n, it's just the domain of g.

@art closed-ray
Compare that with rational expressions. There, the domain came from setting a denominator equal to zero, an equation, and it removed isolated points. Here it comes from requiring a radicand to be non negative, an inequality. An even radical removes whole intervals.

@chapter Three domains
@math items="√(x − 3):  x − 3 ≥ 0  →  x ≥ 3@of x minus three needs;;√(5 − x):  5 − x ≥ 0  →  x ≤ 5@five minus x;;∛(x − 3):  all real numbers@cube root"
The square root of x minus three needs x minus three at least zero, so x is at least three. The square root of five minus x needs five minus x at least zero, so x is at most five. The inequality reverses. And the cube root of x minus three needs nothing at all. Its domain is every real number.

@chapter A quadratic radicand
@math heading="h(x) = √(x² − 9)" items="x² − 9 ≥ 0@at least zero;;(x − 3)(x + 3) ≥ 0@that is;;x ≤ −3   or   x ≥ 3@for x at most"
For h of x equals the square root of x squared minus nine, you need x squared minus nine at least zero, that is, x minus three times x plus three at least zero. A product of two factors is non negative when both have the same sign. That happens for x at most minus three, and for x at least three.

@art two-rays
So the domain is two separate rays, with a gap between minus three and three where the function doesn't exist. The formula gives no warning that it's undefined on an interval six units wide. Only solving the inequality shows it.

@math heading="Two checks" items="x = 0:  √(−9), undefined  ✓  the gap is real@at zero;;x = 3:  √0 = 0, defined  ✓  endpoints included@at three"
Two checks make it solid. At zero, you get the square root of minus nine, undefined, so the gap is real. At three, you get root zero, which is zero, so the endpoints belong to the domain. The condition is at least, not greater than.

@chapter The basic curve
@art sqrt-curve
The graph of y equals root x has domain x at least zero and range y at least zero. It starts at the origin, rises, and flattens. It's the upper half of the sideways parabola x equals y squared, not all of it.

@art mirror-diagonal
It's also the reflection of y equals x squared, kept to x at least zero, in the line y equals x. That's what makes it that function's inverse, and why the restriction is needed at all.

@math heading="y = √(x − 3), exact points" items="x:  3,  4,  7,  12,  19@three, four;;y:  0,  1,  2,  3,  4@zero, one"
To sketch, choose inputs that make the radicand a perfect square. For root x minus three, take x as three, four, seven, twelve and nineteen. Then y is zero, one, two, three and four. Picking x equals five instead gives root two, about one point four one four, which you can't place accurately by hand.

@chapter Shifts and flips
@art shifted-start
The usual transformations apply. In y equals a times the square root of x minus h, plus k, the graph starts at h, k instead of the origin. h shifts the domain to x at least h, k shifts the range to y at least k, and a negative a flips it downward, so the range becomes y at most k.

@art v-shape
One last link. f of x equals the square root of x squared is defined for every real x, but its graph isn't the line y equals x. It's y equals the absolute value of x, a V with its vertex at the origin. The identity from Simplifying Radical Expressions, drawn.

@chapter Where people slip
@list heading="Common slips" items="Reading the domain off the formula@The first|Forgetting to reverse the inequality@The second|Excluding the endpoint@the third"
The first slip is reading the domain off the formula instead of solving for it. The second is forgetting to reverse the inequality: five minus x at least zero gives x at most five. And the third is excluding the endpoint. Root zero is zero, so the graph starts with a closed point.

@chapter Try it
@words text="g(x) = −√(6 − 2x) + 1" sub="start from 6 − 2x ≥ 0"
Your turn. Take g of x equals minus the square root of six minus two x, plus one. Solve six minus two x at least zero. Then use the outside minus and the shift to state the endpoint and the range, before choosing exact points.

@end text="Solve for the domain"
You can practise solving for domains and sketching radical graphs on Learn. That's learn dot get er done dot I O.
