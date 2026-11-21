---
format: long
lesson: polynomials-and-factoring/polynomials-degree-and-standard-form
title: What makes something a polynomial, and how to read its degree
thumb: Combine first, then read
---

@chapter The question
@title text="Polynomials, Degree and Standard Form" sub="Polynomials and Factoring" art=thumb
Every technique in this course works on one kind of expression, the polynomial. So before you add, multiply or factor anything, you need to know what qualifies, and how to read the one number that describes it best.

@math heading="A polynomial in x" items="aₙxⁿ + aₙ₋₁xⁿ⁻¹ + … + a₁x + a₀@a n x to the n;;n = 0, 1, 2, 3, …@a whole number"
A polynomial in x is anything you can write as a finite sum like this: a n x to the n, plus the next term down, all the way to a zero. The power n is a whole number, and the coefficients in front are just numbers.

@art term-blocks
Each piece is a term. The number in front is that term's coefficient, and the piece with no x at all is the constant term.

@words text="x(x + 1) = x² + x" sub="it can be written as a sum"
Notice the words can be written as. x times x plus one is a polynomial, because multiplying it out gives x squared plus x.

@chapter What fails
@art rejected-tiles
Three kinds of expression fail, and they fail for the same reason: the exponent is not a whole number.

@math heading="Not polynomials" items="2/x = 2x⁻¹@two over x;;√x = x^(1/2)@the square root of x;;2ˣ@two to the x"
Two over x is two x to the minus one, and minus one isn't a whole number. The square root of x is x to the one half, a fractional exponent. And two to the x puts the variable up in the exponent, the reverse of x squared. That one is an exponential.

@words text="(1/2)x³ − 0.7x" sub="a polynomial: coefficients can be any numbers"
But a fraction in a coefficient is fine. One half x cubed minus zero point seven x is a perfectly good polynomial. The rule restricts the exponents, not the coefficients.

@chapter Degree and standard form
@art descending-steps
The degree is the largest exponent on the variable, once like terms are combined. The coefficient of that term is the leading coefficient. And a polynomial is in standard form when its terms run in descending order of degree.

@math heading="Reading one" items="−2x³ + 5x + 8@minus two x cubed;;degree 3 · leading coefficient −2@degree three;;constant term 8@constant term"
Take minus two x cubed plus five x plus eight. It's in standard form. Degree three, leading coefficient minus two, constant term eight.

@art missing-slot
And the coefficient of x squared is zero. That's worth saying out loud, because polynomial long division will make you write that zero down.

@chapter Combine before you read
@math heading="x³ + 5x − x³" items="x³ − x³ = 0@cancel;;= 5x@leaves;;degree 1@degree one"
Now the part that matters. In x cubed plus five x minus x cubed, the highest power written is three. But the x cubed terms cancel, which leaves five x, and that has degree one.

@art cancelling-bars
Degree belongs to the polynomial, not to the way it happens to be written. A seven on its own is seven x to the zero, so its degree is zero. The zero polynomial has no degree at all, since there's no highest power to point at.

@art term-chains
Short polynomials have names. One term is a monomial, two is a binomial, three is a trinomial. Beyond that, nobody bothers.

@words text="4x²y − 3xy + y³" sub="4x²y has degree 2 + 1 = 3"
A polynomial can have more than one variable too. For a term like four x squared y, add the exponents, two plus one, so its degree is three.

@chapter A worked example
@math heading="5x − 3x³ + 8 + x³" items="−3x³ + x³ = −2x³@combine;;−2x³ + 5x + 8@standard form;;degree 3 · leading coefficient −2@degree three"
Here's one that catches people. Five x minus three x cubed plus eight plus x cubed. Combine the cubes: minus three x cubed plus x cubed is minus two x cubed. In standard form that's minus two x cubed plus five x plus eight, degree three, leading coefficient minus two.

@words text="not −3x³" sub="the first term written is not the leading term"
Read it as written, and the leading coefficient looks like minus three. That reading doesn't survive combining, and combining isn't optional. It's how you find out what the polynomial actually is.

@chapter Where people slip
@list heading="Common slips" items="Reading the degree off the first term written@The first|Thinking a fractional coefficient disqualifies it@The second|Calling a factored expression not a polynomial@The third"
The first slip is reading the degree off the first term written. Only standard form makes that reliable. The second is thinking a fractional coefficient disqualifies an expression. It doesn't. The third is calling a factored expression not a polynomial. x plus one times x minus four is x squared minus three x minus four.

@chapter Try it
@words text="6 − 4x³ + 2x − x³" sub="combine, order, then name the degree"
Your turn. Six minus four x cubed plus two x minus x cubed. Every exponent is whole, so it's a polynomial. Combine and order the terms, then name the degree, the leading coefficient and the number of terms.

@math items="−5x³ + 2x + 6@minus five x cubed;;degree 3 · leading coefficient −5 · three terms@degree three"
Check yourself. You should get minus five x cubed plus two x plus six, with degree three, leading coefficient minus five, and three terms. If you wrote minus three x cubed, you treated the second cubic term as positive.

@end text="Type a polynomial, watch it sort"
You can type in a polynomial and watch it combine, sort and report its degree, on Learn. That's learn dot get er done dot I O.
