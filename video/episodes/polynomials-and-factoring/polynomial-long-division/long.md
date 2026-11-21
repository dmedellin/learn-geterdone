---
format: long
lesson: polynomials-and-factoring/polynomial-long-division
title: Polynomial long division, one leading term at a time
thumb: Stop when the degree drops
---

@chapter The question
@title text="Polynomial Long Division" sub="Polynomials and Factoring" art=thumb
You already know long division with numbers. Polynomials divide the same way, by a divisor of any degree. And it always finishes with one quotient and one remainder.

@words text="17 = 5 · 3 + 2,   2 < 5"
Seventeen divided by five is three, remainder two. What that really says is seventeen equals five times three, plus two, with two less than five. Polynomial division says the same thing, with degree playing the part of size.

@chapter The division algorithm
@math heading="f(x) = d(x) · q(x) + r(x)" items="d ≠ 0@nonzero d;;r = 0  or  deg r < deg d@the degree of r"
For any polynomial f and any nonzero d, there's a unique quotient q and remainder r with f equal to d times q, plus r. And either r is zero, or the degree of r is less than the degree of d.

@art unique-answer
Uniqueness is the half people skip, and it's what lets you check. If two people divide the same f by the same d and get different quotients, one of them is wrong. There's no second right answer.

@chapter The procedure
@art leading-terms
Write both in descending order, with every power present. Divide the leading term of what's left by the leading term of the divisor. That gives the next quotient term. Multiply the whole divisor by it, subtract, and repeat.

@art stop-by-degree
Stop when the remainder's degree is less than the divisor's. Only the leading terms decide each step. Everything else waits for the multiply.

@chapter A worked example
@math heading="(2x⁴ − 3x³ + 5x − 1) ÷ (x² − x + 2)" items="2x⁴ − 3x³ + 0x² + 5x − 1@zero x squared"
Divide two x to the fourth minus three x cubed plus five x minus one, by x squared minus x plus two. There's no x squared term, so write zero x squared in its place.

@math heading="Step 1" items="2x⁴ ÷ x² = 2x²@what times x squared;;2x² · (x² − x + 2) = 2x⁴ − 2x³ + 4x²@multiply;;(2x⁴ − 3x³ + 0x²) − (2x⁴ − 2x³ + 4x²) = −x³ − 4x²@subtract"
Ask what times x squared gives two x to the fourth. It's two x squared. Multiply the divisor by it: two x to the fourth minus two x cubed plus four x squared. Now subtract. Minus three x cubed minus minus two x cubed is minus x cubed, and zero minus four x squared is minus four x squared.

@math heading="Steps 2 and 3" items="−x · (x² − x + 2) = −x³ + x² − 2x@minus x times;;−5x² + 7x − 1@leaves;;−5 · (x² − x + 2) = −5x² + 5x − 10@minus five times;;2x + 9@two x plus nine"
Bring down five x. The next term is minus x, and minus x times the divisor is minus x cubed plus x squared minus two x. Subtracting leaves minus five x squared plus seven x minus one. Then minus five times the divisor, subtracted, leaves two x plus nine.

@art remainder-left
Two x plus nine has degree one, and the divisor has degree two. So stop. The quotient is two x squared minus x minus five, and the remainder is two x plus nine.

@math heading="Check" items="(x² − x + 2)(2x² − x − 5) = 2x⁴ − 3x³ + 3x − 10@expand;;+ (2x + 9) = 2x⁴ − 3x³ + 5x − 1@add two x plus nine"
To check, expand the divisor times the quotient: two x to the fourth minus three x cubed plus three x minus ten. Add two x plus nine, and you get the original. So both are right.

@chapter What the result means
@art factor-or-not
The remainder isn't zero, so the divisor is not a factor. If it had been zero, you'd have factored a quartic into two quadratics. That's how division earns its place in a course on factoring.

@words text="r = 0 → deg f = deg d + deg q" sub="degree 4 ÷ degree 2 → degree 2"
And degrees add. If r is zero, the degree of f is the degree of d plus the degree of q. Divide degree four by degree two, and any quotient that isn't degree two is an error.

@chapter Where people slip
@list heading="Common slips" items="Subtracting only the first term@The first|Leaving out a missing power@The second|Dividing whole polynomials@The third"
The first slip is subtracting only the first term of the product. Every sign flips, and each line feeds the next. The second is leaving out a missing power, which shifts every coefficient a column. The third is dividing whole polynomials, when each quotient term comes from the leading terms alone.

@chapter Try it
@words text="(x³ + 0x² − 5x + 6) ÷ (x² + x − 2)" sub="first quotient term: x"
Your turn. Divide x cubed plus zero x squared minus five x plus six, by x squared plus x minus two. The first quotient term is x. Finish the loop, and check the identity.

@math items="q = x − 1@x minus one;;r = −2x + 4@minus two x plus four"
You should get q equals x minus one, and r equals minus two x plus four. If your remainder still has an x squared in it, you stopped too soon.

@end text="Every line of the division"
You can enter any two polynomials and see every line of the division, then the check, on Learn. That's learn dot get er done dot I O.
