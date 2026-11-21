---
format: long
lesson: rates-of-change-and-the-derivative/the-quotient-as-a-polynomial-in-h
title: The difference quotient as a polynomial in h
thumb: Cancel first, then set h = 0
---

@chapter Every place at once
@title text="The Quotient as a Polynomial in h" sub="Rates of Change and the Derivative" art=thumb
Last time, the rate of t squared at one, over a step h, came out as two plus h. That was one place. Do the same algebra at a general t, and one calculation covers every place at once.

@math heading="p(t) = t²" items="p(t + h) = t² + 2th + h²@t plus h, squared;;p(t + h) − p(t) = 2th + h²@Subtract;;(p(t + h) − p(t))/h = 2t + h@divide by h"
Expand t plus h, squared: t squared, plus two t h, plus h squared. Subtract t squared, and you're left with two t h plus h squared. Now divide by h, and the quotient is two t plus h.

@art two-places
At t equals one, that's two plus h, the last lesson's answer. At t equals two, it's four plus h. One expansion has done every place.

@chapter Why it always divides
@art square-split
Here's a picture of what happened. A square of side t plus h splits into a t by t square, two strips that are t by h, and a little h by h corner.

@art strips-left
Subtracting t squared takes away the big square. Every piece that's left has an h in it, so dividing by h comes out even. That's true for any polynomial: the terms with no h add up to exactly p of t, and the subtraction removes them.

@words text="a polynomial in h" sub="with coefficients that are polynomials in t"
What's left is a polynomial in h, whose coefficients depend on t. Its constant term, the part with no h at all, is the number the next lessons call the rate at t.

@chapter The cube
@math heading="p(t) = t³" items="(t + h)³ = t³ + 3t²h + 3th² + h³@t plus h, cubed;;p(t + h) − p(t) = 3t²h + 3th² + h³@Take away t cubed;;÷ h:  3t² + 3th + h²@Divide by h;;the part without h:  3t²@the constant term"
For t cubed, t plus h, cubed, is t cubed, plus three t squared h, plus three t h squared, plus h cubed. Take away t cubed, and every term has an h. Divide by h, and you get three t squared plus three t h plus h squared. So the constant term is three t squared.

@math heading="Check at t = 1, h = 1/4" items="3 + 3/4 + 1/16 = 61/16@three plus three quarters;;(125/64 − 1) / (1/4) = 61/16@the long way"
Check it with numbers. At t equals one, with a step of a quarter, the formula gives three plus three quarters plus one sixteenth, which is sixty one sixteenths. Now the long way. The output at five quarters is one hundred and twenty five sixty fourths. Subtract one, divide by a quarter, and it's sixty one sixteenths again.

@chapter Two terms
@math heading="p(t) = t⁴ − 2t²" items="4t³ + 6t²h + 4th² + h³ − 4t − 2h@dividing by h;;constant term:  4t³ − 4t@the constant term"
Two terms work the same way. For t to the fourth minus two t squared, expanding, subtracting and dividing by h gives four t cubed, plus six t squared h, plus four t h squared, plus h cubed, minus four t, minus two h. Group it by powers of h, and the constant term is four t cubed minus four t.

@chapter Why the order matters
@art empty-fraction
Here's the tempting shortcut. Why not put h equals zero into the quotient straight away? Because the top becomes p of t minus p of t, which is zero, and the bottom is zero too. Zero over zero has no value.

@words text="cancel first, then set h = 0" sub="t²:  2t + h  →  2t"
The simplified form is different. Once the h has been cancelled, two t plus h is a perfectly good polynomial, and it has a value at h equals zero: two t. No limit is taken. The constant term is just a coefficient, found by expanding and collecting.

@chapter Where people slip
@list heading="Common slips" items="Setting h = 0 before dividing@The first|Dropping terms because h is small@The second|Forgetting the middle of an expansion@the third"
The first slip is setting h to zero before dividing, which gives zero over zero. The second is dropping terms because h is small. Three t h and h squared are part of the exact quotient, they just aren't the constant term. And the third is forgetting the middle of an expansion.

@art missing-middle
Writing t plus h, cubed, as t cubed plus h cubed loses the middle terms, and they're what make the answer three t squared and not zero. Check with numbers. One plus one, cubed, is eight, not one plus one.

@chapter Try it
@art binomial-bars
Your turn. Repeat all this for t to the fourth, whose expansion has the coefficients one, four, six, four, one. The constant term should come out as four t cubed.

@words text="t² → 2t    t³ → 3t²    t⁴ → 4t³" sub="the exponent times the power one lower"
Then look at the pattern across t squared, t cubed and t to the fourth. The constant term is the exponent, times the power one lower. Hold on to that. It comes back when the derivative becomes a function.

@end text="Expand, subtract, divide"
You can watch the lab expand a polynomial and group its quotient by powers of h, on Learn. That's learn dot get er done dot I O.
