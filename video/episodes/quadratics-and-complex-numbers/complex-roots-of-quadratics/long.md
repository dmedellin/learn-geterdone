---
format: long
lesson: quadratics-and-complex-numbers/complex-roots-of-quadratics
title: Complex roots of quadratics: the conjugate pair
thumb: No real roots isn't no roots
---

@chapter Unfinished business
@title text="Complex Roots of Quadratics" sub="Quadratics and Complex Numbers" art=thumb
The discriminant lesson left one case open on purpose. When b squared minus four a c is negative, the formula asks for the square root of a negative number. Complex numbers gave that a meaning, and nothing else about the method needs to change.

@math heading="D = b² − 4ac < 0" items="(i√(−D))² = i² · (−D) = D@i root minus D;;x = −b/(2a) ± (√(−D)/(2a)) i@minus b over two a"
If D is negative, then minus D is positive, so root minus D is an ordinary real number. And i root minus D, squared, is D. So it's a square root of D. Put it in the formula and divide both parts by two a: x is minus b over two a, plus or minus root minus D over two a, times i.

@art mirror-pair
Both of those pieces are real numbers. So the two solutions have the same real part and opposite imaginary parts. That makes them conjugates of each other.

@chapter A worked example
@math heading="x² − 6x + 13 = 0" items="D = 36 − 52 = −16@thirty six minus;;√(−D) = √16 = 4@root sixteen;;x = (6 ± 4i) / 2 = 3 ± 2i@six plus or minus four i"
Take x squared minus six x plus thirteen. D is thirty six minus fifty two, which is minus sixteen. So root minus D is root sixteen, four. Then x is six plus or minus four i, over two, which is three plus or minus two i.

@words text="(−6 ± 4i)/2 = −3 ± 2i" sub="not −3 ± 4i"
Divide both parts of the numerator. Minus six plus or minus four i, over two, is minus three plus or minus two i. Halving only the real part, and writing minus three plus or minus four i, is wrong.

@chapter A second route
@math heading="Complete the square" items="(x − 3)² − 9 + 13 = 0@half of minus six;;(x − 3)² = −4@minus four;;x − 3 = ±2i@plus or minus two i;;x = 3 ± 2i@three plus or minus"
Now complete the square instead. Half of minus six is minus three, and minus three squared is nine. That gives x minus three, squared, equals minus four. Two i squared is minus four, so x minus three is plus or minus two i, and x is three plus or minus two i.

@art two-routes-meet
Two methods, done separately, agreeing. And completing the square never needed the discriminant. The negative simply turned up as the number a square was being asked to equal.

@chapter Real coefficients
@art broken-pairing
The pairing depends on a, b and c being real. Without that, it fails. x squared minus i x equals zero factors as x times x minus i, so its solutions are zero and i, and those aren't conjugates.

@math heading="Factoring over the complex numbers" items="x² − 6x + 13 = (x − 3 − 2i)(x − 3 + 2i)@factors;;(x − 3)² − (2i)² = x² − 6x + 9 + 4@expanding"
With the pair in hand, the quadratic factors, just not over the reals. x squared minus six x plus thirteen factors as x minus three minus two i, times x minus three plus two i. Expanding confirms it.

@art two-capsules
So a quadratic that wouldn't factor over the reals, the kind called irreducible, factors here into two brackets, one for each root. That word always means irreducible over some system. Over the complex numbers, no quadratic is.

@art sum-product
The sum and product make a good check. For three plus or minus two i, the sum is six, which is minus b over a. The product is nine plus four, thirteen, which is c over a. Both come out real, as they must.

@chapter Keep it exact
@math heading="2x² + 3x + 5 = 0" items="D = 9 − 40 = −31@nine minus forty;;x = (−3 ± i√31) / 4@minus three plus or minus;;x = −3/4 ± (√31/4) i@minus three quarters"
Another. Two x squared plus three x plus five has D equal to nine minus forty, minus thirty one. So x is minus three plus or minus i root thirty one, over four. That's minus three quarters, plus or minus root thirty one over four, times i. Root thirty one stays as it is.

@chapter On the graph
@art floating-parabola
On the graph, nothing dramatic happens. The parabola y equals x squared minus six x plus thirteen has its lowest point at three, four. It sits entirely above the x axis, so there are no x intercepts. The conjugate pair isn't hiding anywhere in that picture. The picture only shows real numbers.

@chapter Where people slip
@list heading="Common slips" items="Answering no solution, unqualified@The first|Dividing only part of the numerator@The second|Writing √−36 as −6@The third"
The first slip is answering no solution with no qualifier. x squared plus four equals zero has no real solution, and two complex ones, two i and minus two i. The second is dividing only part of the numerator by two a. The third is writing root minus thirty six as minus six. Minus six squared is thirty six, not minus thirty six.

@end text="Same formula, two conjugate roots"
Carry a negative discriminant through the formula yourself, on Learn. That's learn dot get er done dot I O.
