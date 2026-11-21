---
format: long
lesson: differential-equations-and-eulers-method/checking-a-proposed-solution
title: Checking a proposed solution, on harder equations
thumb: Same test, more to do
---

@chapter Harder equations, same test
@title text="Checking a Proposed Solution" sub="Differential Equations and Euler's Method" art=thumb
The residual test works the same on every equation: substitute, subtract, simplify. But harder equations give it more to do, and one kind of equation behaves differently from the rest.

@math heading="y″ − y′ − 2y = 0" items="second order:  needs y′ and y″@two derivatives;;linear:  y″, y′ and y each once, times a number@linear"
Start with y double prime minus y prime minus two y equals zero. It's second order, so a candidate needs two derivatives. And it's linear: y double prime, y prime and y each appear once, with a number in front.

@chapter Two exponentials
@math heading="y = e^(2t)" items="y′ = 2e^(2t)@y prime is two;;y″ = 4e^(2t)@y double prime is four;;4e^(2t) − 2e^(2t) − 2e^(2t) = 0@So the residual"
Try e to the two t. The derivative of e to the k t is k times e to the k t, so y prime is two e to the two t, and y double prime is four e to the two t. So the residual is four minus two minus two, times e to the two t. Zero. A solution.

@art cancel-to-zero
Four, minus two, minus two. Everything cancels, but only with the four. Use two for the second derivative by mistake, and the check falls apart.

@math heading="y = eᵗ" items="y′ = eᵗ,   y″ = eᵗ@y prime and y double prime;;eᵗ − eᵗ − 2eᵗ = −2eᵗ@the residual"
Now try e to the t. Here y prime and y double prime are both e to the t, and the residual is e to the t, minus e to the t, minus two e to the t: minus two e to the t. And e to the t is never zero, so this candidate fails everywhere.

@art two-exponentials
The two exponentials differ only in the number in the exponent, and the equation accepts one and rejects the other. In a later course, the right numbers turn out to be the roots of a quadratic.

@chapter A coefficient that depends on t
@math heading="t·y′ = 2y" items="y = 5t²:   t·10t = 10t² = 2·5t²,   residual 0@five t squared;;y = 5t:   t·5 = 5t,   2y = 10t,   residual −5t@For five t"
In t times y prime equals two y, the t has to be carried through. For five t squared, the derivative is ten t, so the left side is ten t squared, and so is the right. Residual zero. For five t, the left side is five t and the right is ten t, so the residual is minus five t.

@words text="residual −5t:  zero at t = 0, nowhere else"
At zero, both sides are zero. So a check at that one point would pass it. The whole simplified residual says otherwise.

@art multiples-of-parabola
And five t squared isn't alone. T squared and minus three t squared work too. Each is a constant multiple of t squared, and in a linear equation with zero on the right, that's allowed.

@chapter A nonlinear equation
@art blow-up-curve
Now y prime equals y squared. Take y equals one over one minus t. By the chain rule, its derivative is one over one minus t, squared, and y squared is the same. Residual zero. The lab labels this equation nonlinear, because y is squared.

@words text="linear, with 0 on the right:" sub="multiples and sums of solutions are solutions"
Here's what linear buys you. In a linear equation with zero on the right, a constant multiple of a solution is a solution, and so is the sum of two. The lab demonstrates this, and doesn't prove it. For a nonlinear equation, neither is guaranteed.

@art doubled-curve
Watch it fail. Double the solution, to two over one minus t. Its derivative is two over one minus t, squared, but its square is four over one minus t, squared. The residual is minus two over one minus t, squared, and that's never zero.

@chapter What the lab decides exactly
@art five-points
One limit is worth knowing. Ratios of polynomials, and exponential or sine and cosine candidates in a linear equation, are decided exactly. An exponential in a nonlinear equation isn't. The lab then checks the residual at five values of t, and says so. That's a spot check, labelled as one.

@chapter Where people slip
@list heading="Common slips" items="Accepting a pass at one value of t@The first|Forgetting a derivative or its coefficient@The second|Assuming a multiple of a solution always works@the third"
The first slip is accepting a candidate because it passes at one value of t. The second is forgetting a derivative, or its coefficient, in a second order check. Write y prime and y double prime on their own lines first. And the third is assuming a multiple of a solution always works. Classify the equation first.

@chapter Try it
@words text="y″ − y′ − 2y = 0" sub="test y = e^(−t)"
Your turn. Test e to the minus t in the same equation. Its derivatives are minus e to the minus t, then e to the minus t. Substitute, simplify, and see whether this equation has a second exponential that works.

@end text="Every derivative, every t"
You can test candidates against harder equations, with the exact residual, on Learn. That's learn dot get er done dot I O.
