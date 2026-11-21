---
format: long
lesson: quadratics-and-complex-numbers/solving-by-factoring
title: Solving quadratics by factoring, and checking every root
thumb: Zero first, then factor
---

@chapter The method
@title text="Solving by Factoring" sub="Quadratics and Complex Numbers" art=thumb
With a zero on one side and a factorisation on the other, the zero product property finishes the job in a line. All the real work is in the factoring, and in two things a finished answer can hide.

@math heading="x² + 3x = 10" items="x² + 3x − 10 = 0@subtract ten;;(x + 5)(x − 2) = 0@five and minus two;;x + 5 = 0  or  x − 2 = 0@set each;;x = −5  or  x = 2@minus five or two"
Start with x squared plus three x equals ten. First, subtract ten, so there's a zero on the right. Now find two numbers with product minus ten and sum three: five and minus two. Set each bracket to zero, and x is minus five or two.

@art factor-blocks
That first step isn't tidiness. x squared plus three x equals ten also factors, as x times x plus three equals ten. But that's a dead end, because the zero product property only works when the product is zero.

@chapter Constant factors
@math heading="2x² − 8x = 0" items="2x(x − 4) = 0@two x;;2 = 0  has no solution@two equals zero;;x = 0  or  x = 4@zero and four"
Now two x squared minus eight x equals zero. It factors as two x, times x minus four. That's three factors, but the two contributes nothing, because two equals zero is simply false. The answers are zero and four.

@art three-boxes
A constant factor never creates a solution, and never destroys one. So multiplying an equation through by three, or dividing by three, leaves its solutions alone. Only multiplying or dividing by something that could be zero is dangerous.

@chapter Repeated factors
@math heading="4x² − 12x + 9 = 0" items="(2x − 3)² = 0@two x minus three, squared;;x = 3/2@three halves;;4(9/4) − 12(3/2) + 9 = 9 − 18 + 9 = 0@nine minus eighteen"
Four x squared minus twelve x plus nine is two x minus three, squared. So the only equation to solve is two x minus three equals zero, and the only solution is three halves. Check it: nine minus eighteen plus nine is zero.

@art double-root
People call that a double root, or a root of multiplicity two. That's a statement about the factorisation. As a solution of the equation, it's one number. The convention pays off later, when counting roots this way keeps the statements clean.

@chapter Leading coefficient not one
@math heading="6x² + x − 12 = 0" items="ac = 6 · (−12) = −72  →  9 and −8@minus seventy two;;6x² + 9x − 8x − 12 = 0@split the middle;;3x(2x + 3) − 4(2x + 3) = 0@group in pairs;;(2x + 3)(3x − 4) = 0@two x plus three, times;;x = −3/2  or  x = 4/3@minus three halves"
When the leading number isn't one, the AC method still works. For six x squared plus x minus twelve, a times c is minus seventy two. Nine and minus eight have that product, and sum one. Split the middle term, then group in pairs. That gives two x plus three, times three x minus four. So x is minus three halves or four thirds.

@art split-middle
Both answers are exact fractions. Minus one point five happens to equal minus three halves, but four thirds has no decimal that equals it at all. That's why exact fractions are the standard here.

@chapter When it won't factor
@art no-integer-fit
Sometimes the search fails. x squared minus four x plus one has no pair of integers with product one and sum minus four. But it still has two solutions, two plus root three and two minus root three, and completing the square will produce them. It doesn't factor is a different sentence from it has no solutions. Only the first one has been shown.

@words text="a(x − r)(x − s) = 0  →  x = r or x = s" sub="and nothing else"
Here's why a factorisation tells you everything. If the quadratic equals a times x minus r, times x minus s, then r and s each make a bracket zero. Any other value makes both brackets non-zero, and a isn't zero either. So there's nothing else to find.

@chapter Running it backwards
@math heading="Roots −5 and 2" items="(x + 5)(x − 2) = 0@start from;;x² + 3x − 10 = 0@expand;;2x² + 6x − 20 = 0@multiply through"
To build an equation with solutions minus five and two, start from x plus five, times x minus two, equals zero, and expand: x squared plus three x minus ten equals zero. Multiply through by two, and two x squared plus six x minus twenty works equally well.

@art scaled-curves
So there's no single equation with a given pair of roots. Any two quadratics with the same roots differ by a constant multiple. That's the constant factor idea again, read the other way round.

@chapter Where people slip
@list heading="Common slips" items="Factoring before there's a zero@The first|Inverting a factor instead of solving it@The second|Reading no factoring as no solutions@The third"
The first slip is factoring before there's a zero on the other side. The second is inverting a factor. Three x minus four equals zero gives four thirds, not three quarters. Add four, then divide by three. The third is reporting does not factor as no solutions.

@end text="Factor, split, substitute back"
Try factoring a few yourself and check every root, on Learn. That's learn dot get er done dot I O.
