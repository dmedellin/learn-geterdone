---
format: long
lesson: systems-and-the-phase-plane/linearisation-and-the-jacobian
title: Linearisation and the Jacobian: zooming in on an equilibrium
thumb: Zoom in, it looks linear
---

@chapter The question
@title text="Linearisation and the Jacobian" sub="Systems and the Phase Plane" art=thumb
You've found the equilibria of a nonlinear system. Now, what does each one do? Is it a saddle, a node, a spiral? The trick is to zoom in until the system looks linear.

@art zoom-in
Close to an equilibrium, the curved terms are small. So the system behaves like a linear system, u prime equals J u, where u is the displacement from the point. And J is a matrix you can build from derivatives.

@chapter The Jacobian
@math heading="Jacobian" items="J = rows  f_x  f_y   and   g_x  g_y@has rows;;at the equilibrium@evaluated there"
The Jacobian has rows f x, f y and g x, g y. Those are partial derivatives, each one evaluated there, at the equilibrium.

@art hold-one-fixed
A partial derivative is the ordinary derivative in one unknown, with the other held still. For f x, treat y as a number and differentiate in x. For f y, do the reverse. It's the tangent-line estimate, made once in each direction.

@math heading="x′ = y − x²,   y′ = x − y" items="f_x = −2x,   f_y = 1@f x is minus two x;;g_x = 1,   g_y = −1@g x is one"
Take last lesson's system, x prime equals y minus x squared, and y prime equals x minus y. f x is minus two x and f y is one. g x is one and g y is minus one.

@chapter Two equilibria, two pictures
@math heading="at (1, 1)" items="J = rows −2 1 and 1 −1@the rows are;;τ = −3,   Δ = 2 − 1 = 1@trace is minus three;;τ² − 4Δ = 9 − 4 = 5 > 0@nine minus four;;λ = (−3 ± √5)/2@root five"
At one, one, the rows are minus two, one and one, minus one. The trace is minus three, and the determinant is two minus one, which is one. The discriminant is nine minus four, five, positive. So the roots are minus three plus or minus root five, over two, and both are negative.

@art node-and-saddle
So one, one is a stable node. At the origin the rows are zero, one and one, minus one, with trace minus one and determinant minus one. A negative determinant: a saddle. One system with a sink at one equilibrium and a saddle at the other. A linear system can never do that.

@chapter When it transfers
@art tangent-plane
Why does that work? The rates are zero at the equilibrium, and to first order they change by the partial derivatives times the displacement. The terms you throw away are smaller than the ones you keep.

@words text="no eigenvalue with real part 0" sub="saddle, node, spiral: the system agrees"
Here's the rule. If no eigenvalue of J has real part zero, the nonlinear system shares the linear picture. Saddle stays saddle, and stable or unstable stays the same. The lesson states that theorem and doesn't prove it. The lab only demonstrates it.

@chapter When it doesn't
@math heading="x′ = −y + x³,   y′ = x + y³" items="J at (0, 0) = rows 0 −1 and 1 0@zero, minus one;;τ = 0,   Δ = 1,   λ = ±i@a centre"
Now take x prime equals minus y plus x cubed, and y prime equals x plus y cubed. The cubic terms have zero derivative at the origin, so J has rows zero, minus one and one, zero. Trace zero, determinant one, roots plus or minus i. The Jacobian says a centre.

@math heading="D = x² + y²" items="D′ = 2x·x′ + 2y·y′@two x times x prime;;= 2x(−y + x³) + 2y(x + y³)@substitute;;= 2x⁴ + 2y⁴ > 0@two x to the fourth"
But look at the squared distance, D equals x squared plus y squared. D prime is two x times x prime, plus two y times y prime. Substitute, and the cross terms cancel, leaving two x to the fourth plus two y to the fourth. That's positive everywhere except the origin.

@art cubic-escape
So every solution moves away. The origin is really an unstable spiral. The Jacobian wasn't wrong. A centre has real part zero, so there's nothing left for the thrown-away terms to be smaller than, and the curved terms decide.

@chapter Where people slip
@list heading="Common slips" items="Trusting J at a centre@The first|Evaluating J at the wrong point@The second|Letting y vary in f_x@And the third"
The first slip is trusting the Jacobian at a centre, or when the determinant is zero. Say it's inconclusive. The second is evaluating J at the wrong point. Using the origin's matrix at one, one gives a saddle, where the truth is a stable node. And the third is letting y vary in f x. Substitute y equals x first, and you get one minus two x, which is a different derivative.

@art wrong-point
So the order is fixed. Differentiate first, holding the other unknown still. Only then substitute the point you're standing on.

@chapter Try it
@words text="x′ = y − x²,   y′ = x − y" sub="linearise at (0, 0)"
Your turn. Build the Jacobian of this system at the origin from the four partial derivatives. Compute its trace and determinant, classify it, and say whether the verdict carries over to the nonlinear system.

@end text="Linearise at every equilibrium"
You can linearise a system at each of its equilibria and read the type on Learn. That's learn dot get er done dot I O.
