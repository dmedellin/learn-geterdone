---
format: long
lesson: quadratics-and-complex-numbers/maximum-and-minimum-problems
title: Maximum and minimum problems with quadratics
thumb: The vertex is the optimum
---

@chapter The shape of the problem
@title text="Maximum and Minimum Problems" sub="Quadratics and Complex Numbers" art=thumb
What's the biggest area a fence can enclose? How high does a thrown ball go? When a quantity depends quadratically on one variable, the answer sits at the vertex. The algebra is three lines. The real work is building the quadratic, and respecting what the variable is allowed to be.

@art up-no-max
A quadratic turns once, so the vertex is the only optimum. If a is positive, f of h is the smallest value and there's no largest, because the curve grows without bound. If a is negative, f of h is the largest and there's no smallest.

@chapter Building the quadratic
@list heading="Four steps" items="Name one variable, with its unit@name one variable|Write everything else in terms of it@the constraint|Write the quantity as ax² + bx + c@expand|State the allowed values first@state the values"
First, name one variable, with its unit. One, not two. Then use the constraint to write every other quantity in terms of it. Write the quantity you're optimising as a function, and expand it so a and b are visible. And state the values the situation allows, before you compute anything.

@chapter A fence
@math heading="Perimeter 80" items="2x + 2y = 80  →  y = 40 − x@two x plus two y;;A(x) = x(40 − x) = −x² + 40x@the area;;x = −40 / (2 · (−1)) = 20@twenty;;A(20) = 400@four hundred"
A rectangle has perimeter eighty. Let x be one side in metres. Then two x plus two y is eighty, so the other side is forty minus x. The area is x times forty minus x, minus x squared plus forty x. a is negative, so the vertex is a maximum, at twenty. And A of twenty is four hundred.

@art rectangle-family
x can be anything between zero and forty, and twenty is inside that. So the greatest area is four hundred square metres, from a twenty by twenty square. One example doesn't prove the best rectangle is always a square. Running the same lines with a letter for the perimeter does.

@chapter A thrown ball
@math heading="h(t) = −5t² + 20t + 1" items="t = −20 / (2 · (−5)) = 2@two seconds;;h(2) = −20 + 40 + 1 = 21@twenty one metres"
A ball's height after t seconds is minus five t squared plus twenty t plus one metres. a is minus five, so the vertex is a maximum, at two seconds. The greatest height is minus twenty plus forty plus one, twenty one metres.

@art ball-arc
When does it land is a different question. That needs the formula, not the vertex. The answers are two plus or minus root one hundred and five over five, and only the positive one, about four point oh five seconds, makes sense, because time after the throw can't be negative.

@chapter Where versus how much
@art where-how-much
Two different numbers are in play here. Minus b over two a says where the optimum is. f of that says how much. How many should you sell, and what's the greatest profit, have different answers, and each is wrong in the other's place.

@chapter When the vertex is out of reach
@math heading="P(x) = −3x² + 30x − 12,  0 ≤ x ≤ 4" items="vertex at x = 5  ✗  out of range@vertex is at five;;P(4) = −48 + 120 − 12 = 60@sixty"
Profit from x machines is minus three x squared plus thirty x minus twelve pounds, but only four machines exist. The vertex is at five, outside the allowed range. The profit rises all the way towards five, so the best allowed value is at the end: P of four is sixty pounds. The unreachable sixty three isn't an answer.

@art fenced-domain
So with a restricted range, check the endpoints as well as the vertex.

@math heading="f(x) = −x² + 5x,  x a whole number" items="vertex at x = 5/2@five halves;;f(2) = 6,  f(3) = 6@two and three"
Whole numbers work the same way. If the vertex of minus x squared plus five x sits at five halves, compare the whole numbers either side, two and three. Both give six.

@art whole-steps
That's what the symmetry predicts, since two and three are the same distance from the axis at five halves. But five halves itself isn't an answer when only whole numbers are allowed.

@chapter Where people slip
@list heading="Common slips" items="Reporting where, when how much was asked@The first|Ignoring the allowed values@The second|Assuming the vertex is a maximum@The third"
The first slip is reporting the location when the value was wanted. The second is ignoring the values the situation allows. The third is assuming the vertex is always a maximum. Find the maximum of x squared minus four x plus seven has no answer, unless a range is given.

@words text="20 m by 20 m, area 400 m²" sub="not  x = 20"
And always finish with a sentence and units. x equals twenty doesn't answer, what are the dimensions of the largest rectangle. Twenty metres by twenty metres, with area four hundred square metres, does.

@end text="Model it, then check the domain"
Build and solve a few optimisation models, on Learn. That's learn dot get er done dot I O.
