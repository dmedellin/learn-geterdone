---
format: long
lesson: differential-equations-and-eulers-method/initial-value-problems
title: Initial value problems: one curve from a family
thumb: One value per constant
---

@chapter Pinning the constant
@title text="Initial Value Problems" sub="Differential Equations and Euler's Method" art=thumb
A differential equation like y prime equals two t has a whole family of solutions, t squared plus C. To get a single curve, you have to pin the constant. One starting value does it.

@art curve-through-point
An initial value says the solution passes through a given point. Of all the curves in the family, it leaves exactly one. The equation together with the value is an initial value problem, and it's the pair that has an answer, not the equation alone.

@math heading="y′ = 2t,  y(1) = 5" items="y = t² + C@The family;;1² + C = 5@At one;;C = 4@So C;;y = t² + 4@the solution"
Take y prime equals two t, with y of one equal to five. The family is t squared plus C. At one, that's one plus C, which must be five. So C is four, and the solution is t squared plus four.

@chapter Two checks
@math heading="Check both" items="equation:  y′ = 2t,  residual 2t − 2t = 0@The equation;;value:  y(1) = 1 + 4 = 5@The value"
Then check it twice. The equation: y prime is two t, and the residual is zero. The value: at one, it's one plus four, five. Both checks matter.

@art two-failures
A function can pass either test and fail the other. T squared solves the equation, but misses the point. The constant five hits the point, and solves nothing.

@chapter How many values
@words text="order 1: one constant, one value" sub="order 2: two constants, two values"
How many values do you need? Undoing one derivative brings one constant, so a first order equation needs one value. A second order equation undoes two derivatives, carries two constants, and needs two values: y and y prime, at the same t.

@art exponential-family
The same procedure works for y prime equals three y, whose family is C times e to the three t. With y of zero equal to two, C times e to the zero is two, so C is two. The lab fits at zero, because there, e to the zero is exactly one.

@chapter Two constants
@math heading="y″ − y′ − 2y = 0" items="y = C·e^(2t) + D·e^(−t)@the family;;y(0) = C + D = 1@C plus D;;y′(0) = 2C − D = −2@two C minus D;;3C = −1:   C = −1/3,   D = 4/3@Adding them"
For the second order equation from last time, the family is C e to the two t, plus D e to the minus t. At zero, the two values give C plus D equals one, and two C minus D equals minus two. Adding them, three C is minus one, so C is minus a third and D is four thirds.

@art two-lines-meet
Two values, two equations, one small system. Where the two lines meet is the pair of constants.

@chapter One value is not enough
@art slopes-through-point
For y double prime plus y equals zero, the family is C cos t plus D sin t. At zero, y of zero is C, and y prime of zero is D. Give the lab only y of zero equal to one, and it declines to fit. C is one, but D is free.

@words text="cos t − 2·sin t" sub="from y(0) = 1 and y′(0) = −2"
Every curve cos t plus D sin t passes through zero, one, each at a different slope. The rate at the start is the missing piece. With y prime of zero equal to minus two, the solution is cos t minus two sin t.

@chapter The value doesn't start the solution
@art both-directions
It's tempting to read y of one equal to five as saying the solution begins at one. It doesn't. T squared plus four is defined on both sides of one. The starting point is just where the information is given, and the solution runs both ways from it.

@chapter Where people slip
@list heading="Common slips" items="Treating t₀ as where the solution starts@The first|Setting C equal to the given value@The second|One value for a second order equation@the third"
The first slip is treating the starting point as where the solution begins. The second is setting the constant equal to the given value. With y of one equal to five, C is four, because one squared already contributes. And the third is giving a second order equation only one value.

@chapter Try it
@words text="y′ = 2t,  y(2) = 1"
Your turn. Take the same equation, y prime equals two t, but with y of two equal to one. Substitute, solve for C, and check both the equation and the value. The lab will tell you if you're right.

@end text="One value per constant"
You can fit the constants of a family from its starting values, on Learn. That's learn dot get er done dot I O.
