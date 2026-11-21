---
format: long
lesson: quadratics-and-complex-numbers/quadratic-inequalities
title: Quadratic inequalities: roots, intervals and one test value
thumb: Signs change only at roots
---

@chapter The question
@title text="Quadratic Inequalities" sub="Quadratics and Complex Numbers" art=thumb
To solve a quadratic inequality, you first solve the equation. The roots are the only places the sign can change, so one test value in each piece settles the whole number line.

@words text="ax² + bx + c > 0" sub="or <, ≥, ≤ · a ≠ 0"
A quadratic inequality can be written a x squared plus b x plus c, greater than zero, or with less than, or the or equal versions. Solving it means describing every real number that makes it true. The answer is a set.

@math heading="Zero on one side" items="(x − 1)(x + 4) > 5  ✗@greater than five;;x² + 3x − 9 > 0@rewrite"
Getting zero on one side isn't cosmetic. Greater than zero is a question about a sign, and factors report signs. Greater than five isn't. Knowing x minus one and x plus four are both positive doesn't tell you whether their product beats five. So rewrite it as x squared plus three x minus nine, greater than zero, first.

@chapter Why one test is enough
@art sign-bands
If the roots are r and s, the expression is a times x minus r, times x minus s. Each bracket changes sign only at its own root. A product changes sign only when a factor does, so between the roots, and outside them, the sign stays fixed.

@chapter Method one: a sign table
@math heading="(x + 2)(x − 3)" items="x < −2:   (−)(−) = +@left of minus two;;−2 < x < 3:   (+)(−) = −@between;;x > 3:   (+)(+) = +@right of three"
Take x plus two, times x minus three. Left of minus two, both brackets are negative, so the product is positive. Between minus two and three, one is positive and one negative, so the product is negative. Right of three, both are positive.

@words text="≤ 0:  −2 ≤ x ≤ 3        > 0:  x < −2 or x > 3"
So the product is less than or equal to zero from minus two to three, endpoints included. And it's greater than zero when x is less than minus two, or greater than three.

@chapter Method two: the parabola
@art above-below
The graph says the same thing in one picture. Greater than zero means the curve is above the x axis. An upward parabola with two roots dips below the axis exactly between them. So greater than zero gives the two outer pieces, and less than zero gives the middle.

@art arch-swap
A downward parabola swaps those two answers. That's why you check the sign of a before writing anything down.

@math heading="2x² + 5x > 3" items="2x² + 5x − 3 > 0@move everything over;;(2x − 1)(x + 3) > 0  →  roots 1/2, −3@factor;;x < −3  or  x > 1/2@outside the roots;;test x = 0:  −3 > 0  false  ✓@test zero"
Two x squared plus five x is greater than three. Move everything over, and factor: two x minus one, times x plus three. The roots are one half and minus three. a is positive, so it's positive outside the roots: x less than minus three, or greater than one half. Test zero: you get minus three, so the middle is rightly excluded.

@math heading="x² − 4x + 1 < 0" items="D = 12  →  roots 2 ± √3@twelve;;2 − √3 < x < 2 + √3@between them;;x = 2:  4 − 8 + 1 = −3  ✓@check"
This one doesn't factor, and it doesn't need to. D is twelve, so the roots are two plus or minus root three. a is positive, so the expression is negative between them. Check with x equals two: four minus eight plus one is minus three. The method only needs the roots.

@chapter Fewer than two roots
@art touch-not-cross
If D is negative, the expression never reaches zero, so it keeps the sign of a everywhere. x squared plus x plus one, greater than zero, is true for every x. If D is zero, the curve touches the axis without crossing. x minus three, squared, greater than zero, holds for every x except three.

@art open-closed
And the endpoints? The roots make the expression zero. With greater than or equal, or less than or equal, they belong. With strict greater than or less than, they don't.

@chapter Where people slip
@math heading="x² > 3x" items="x² − 3x > 0@move everything;;x(x − 3) > 0  →  x < 0 or x > 3@x times x minus three"
The first slip is dividing by x. For x squared greater than three x, cancelling gives x greater than three alone. Move everything over instead. x times x minus three, greater than zero, gives x less than zero, or greater than three. Try minus one: one is greater than minus three.

@art two-separate
The second slip is writing a two piece answer as one chain. Three less than x less than minus two says x is above three and below minus two at once. Nothing is. Use the word or. The third is assuming the sign flips at every root. At a repeated root, it doesn't.

@end text="Roots, intervals, one test each"
Solve a few inequalities and test every interval, on Learn. That's learn dot get er done dot I O.
