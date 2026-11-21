---
format: long
lesson: systems-and-the-phase-plane/nonlinear-systems-and-equilibria
title: Equilibria of a nonlinear system: where both rates are zero
thumb: Both rates zero, at once
---

@chapter The question
@title text="Nonlinear Systems and Their Equilibria" sub="Systems and the Phase Plane" art=thumb
A linear system with a non-zero determinant has exactly one resting point, the origin. Put a square or a product into the equations, and that's gone. Now the first question is how many places there are to rest, and where.

@chapter What an equilibrium is
@math heading="x′ = f(x, y),   y′ = g(x, y)" items="f(x, y) = 0@f of x, y;;g(x, y) = 0@and g of x, y"
An equilibrium is a point where f of x, y is zero and g of x, y is zero, both at once. The arrow there is zero, zero, so a solution that starts on it never leaves.

@art still-point
Both conditions matter. At a point where f is zero but g isn't, x is still for an instant, but y keeps moving, and the solution leaves at once.

@art nullclines-cross
The curve where f is zero is the x nullcline. The curve where g is zero is the y nullcline. The equilibria are exactly where those two curves cross. And bent curves can cross wherever they like, so there can be none, one, or several.

@chapter Solving them together
@math heading="x′ = y − x²,   y′ = x − y" items="g = 0:  y = x@gives y equals x;;f = 0:  x − x² = 0@x minus x squared;;x·(1 − x) = 0@factors;;x = 0  or  x = 1@x is zero or one"
Here's an example. x prime equals y minus x squared, and y prime equals x minus y. Setting g to zero gives y equals x. Put that into f equals zero, and you get x minus x squared equals zero. That factors as x times one minus x, so x is zero or one.

@art parabola-and-line
Go back to y equals x, and the two equilibria are zero, zero and one, one. Geometrically, the x nullcline is the parabola y equals x squared, and the y nullcline is the line y equals x. They cross at exactly those two points.

@chapter Check both, every time
@math heading="substitute into f and g" items="(0, 0):  f = 0,  g = 0  ✓@At zero, zero;;(1, 1):  f = 1 − 1 = 0,  g = 1 − 1 = 0  ✓@At one, one;;(2, 4):  f = 4 − 4 = 0,  g = 2 − 4 = −2  ✗@two, four"
Now check each point in both equations. At zero, zero, f and g are both zero. At one, one, f is one minus one, and g is one minus one. Both equilibria. Now try two, four, which lies on the parabola. f is four minus four, zero. But g is two minus four, minus two.

@art near-miss
So two, four isn't an equilibrium. The solution through it has x still for an instant, while y falls at a rate of two, and it moves on.

@chapter What a search can miss
@words text="x′ = y − 5x²,   y′ = x − y" sub="(0, 0)  and  (1/5, 1/5)"
The lab can test a grid of fractions exactly, with denominators one to four. But take x prime equals y minus five x squared, and y prime equals x minus y. Here x equals five x squared gives x is zero or a fifth. So the equilibria are zero, zero and a fifth, a fifth.

@art grid-search
The denominator five is outside the grid, so the search reports only the origin. A search that finds one point has told you what the grid holds, not how many there are. The algebra is the method. The search just checks it.

@chapter Where people slip
@list heading="Common slips" items="Assuming one equilibrium, at the origin@The first|Checking only one equation@The second|Dividing out a factor@And the third"
The first slip is assuming a nonlinear system has one equilibrium, at the origin, a habit carried over from linear systems. The second is checking only one of the two equations, like two, four. And the third is dividing out a common factor. Divide x times one minus x by x, and you lose zero, zero. Factor, and set each factor to zero in turn.

@art several-equilibria
That matters more as systems grow. Later in this course you'll meet rates like x times three minus x minus two y, where each factor gives its own family of points. So solve the simpler equation for one unknown, substitute, keep every root, and then check every point you found in both equations.

@chapter Try it
@words text="x′ = y − 5x²,   y′ = x − y" sub="check (1/5, 1/5) in both"
Your turn. For x prime equals y minus five x squared, and y prime equals x minus y, solve the two equations together yourself, keeping every factor. Then substitute a fifth, a fifth into both f and g, and confirm both come out zero.

@end text="Find where both rates vanish"
You can type points and check them in both equations on Learn. That's learn dot get er done dot I O.
