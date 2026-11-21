---
format: long
lesson: first-order-linear-equations/homogeneous-plus-particular
title: Homogeneous plus particular: build the solution in two parts
thumb: Add the parts, then fit C
---

@chapter The question
@title text="Homogeneous Plus Particular" sub="First-Order Linear Equations" art=thumb
Every solution of a linear equation splits into two pieces. One piece answers the forcing. The other carries the constant. Knowing why that split is allowed tells you exactly when to fit the starting value.

@chapter Two parts
@math heading="y′ + p·y = q" items="y_p:  any one solution of y′ + p·y = q@a particular solution;;y_h:  y′ + p·y = 0,   y_h = C/μ@a homogeneous solution;;y = y_p + y_h@general solution"
A particular solution y p is any one function that satisfies the forced equation. A homogeneous solution y h satisfies the equation with the forcing removed, and it's C over mu, carrying the one constant. The general solution is their sum.

@chapter Why adding is allowed
@math heading="Superposition" items="(y_p + y_h)′ + p·(y_p + y_h)@substitute the sum;;= (y_p′ + p·y_p) + (y_h′ + p·y_h)@regroup;;= q + 0 = q@q plus zero"
Substitute the sum. The derivative of a sum is the sum of derivatives, so you can regroup into the particular part's left side plus the homogeneous part's left side. That's q plus zero, which is q. It works for any p and q, because y and y prime appear only to the first power.

@art two-parts-sum
And nothing is missed. If y is any solution at all, then y minus y p solves the homogeneous equation, because q minus q is zero. So every solution is y p plus C over mu. For y prime equals y squared, the sum of two solutions isn't a solution.

@chapter Finding y_p by a guess
@math heading="y′ + 3y = 2t" items="y_h = C·e^(−3t)@homogeneous part;;try y_p = A·t + B@try;;A + 3(A·t + B) = 2t@Substitute"
Take y prime plus three y equals two t. With mu equals e to the three t, the homogeneous part is C e to the minus three t. For the particular part, borrow the form of the forcing. Two t is degree one, so try A t plus B. Substitute: A plus three times A t plus B equals two t.

@math heading="Match coefficients" items="t:   3A = 2,   A = 2/3@coefficients of t;;1:   A + 3B = 0,   B = −2/9@constant terms;;y_p = (2/3)·t − 2/9@So y p"
Match the coefficients of t: three A equals two, so A is two thirds. Match the constant terms: A plus three B equals zero, so B is minus two ninths. So y p is two thirds t minus two ninths. Check: its derivative two thirds, plus three times it, is exactly two t.

@art need-constant
Why carry B, when the forcing has no constant? With A t alone, you'd need three A equals two and A equals zero, which no A satisfies. The derivative of A t is a constant, and something has to cancel it.

@chapter The steady state was this
@art steady-split
For y prime plus two y equals six, try a constant A. Then two A equals six, so A is three, the steady state from earlier. The gap found there is exactly the homogeneous part, with C equal to y nought minus three.

@chapter Fit the constant last
@math heading="y(0) = 1" items="y = (2/3)·t − 2/9 + C·e^(−3t)@Add the two parts;;−2/9 + C = 1@put in;;C = 11/9@eleven ninths"
Add the two parts first: two thirds t minus two ninths plus C e to the minus three t. Only then put in the starting value, because it's a statement about the whole solution. At zero, minus two ninths plus C equals one, so C is eleven ninths.

@math heading="y′ + 2y = e^t,  y(0) = 0" items="y_p = (1/3)·e^t@a third;;1/3 + C = 0,   C = −1/3@C is minus a third"
One more. For y prime plus two y equals e to the t, try A e to the t. Then three A equals one, so y p is a third of e to the t. Add C e to the minus two t, and at zero a third plus C is zero, so C is minus a third.

@art parts-view
The lab draws the parts separately. The homogeneous curve decays on its own. The particular curve is the forced response the starting value can't change. And the solution is their sum.

@chapter Where people slip
@list heading="Common slips" items="Fitting C before adding y_p@The first|Guessing A·t with no constant@The second|Believing y_p is unique@The third"
The first slip is fitting the constant to y h before y p is added. The second is guessing A t with no constant term. The third is believing the particular solution is unique.

@art early-fit
Fitting first gives C equals one, and a solution that starts at one minus two ninths, seven ninths, not one. The particular part is minus two ninths at zero, so the constant has to supply eleven ninths.

@art different-split
Add e to the minus three t to y p, and it still solves the equation, because the extra term is homogeneous. Then the constant is two ninths, not eleven ninths, and the final y is the same, since two ninths plus one is eleven ninths. A different split, the same sum.

@chapter Try it
@words text="y′ + 3y = 2t,  y(0) = 1" sub="target C = 11/9"
Your turn. Write y p and y h for y prime plus three y equals two t, add them, then fit the constant at zero. Check you get eleven ninths, then substitute to confirm.

@end text="Add the parts, then fit C"
You can see the homogeneous part, the particular part and their sum drawn side by side, on Learn. That's learn dot get er done dot I O.
