---
format: long
lesson: systems-and-the-phase-plane/systems-of-two-equations
title: Systems of two equations: a plane full of arrows
thumb: A solution follows the arrows
---

@chapter Two things changing together
@title text="Systems of Two Equations" sub="Systems and the Phase Plane" art=thumb
Some quantities don't change on their own. Two of them change together, and each one's rate depends on both. A pair of equations can describe that, and it turns a whole plane into a map of arrows.

@math heading="A linear system" items="x′ = a·x + b·y@x prime equals a x;;y′ = c·x + d·y@y prime equals c x;;x′ = A·x@Written with a matrix"
Here's the shape. x prime equals a x plus b y, and y prime equals c x plus d y, where a, b, c and d are numbers. Written with a matrix, it's x prime equals A x, where A has the rows a b and c d.

@chapter Every point gets an arrow
@art arrow-field
The right-hand sides depend only on the point x, y. So at every point the system names a direction and a speed: an arrow. Put all those arrows together and you have a vector field. The system is a rule for drawing it.

@math heading="x′ = x,  y′ = −y" items="at (1, 1):  (1, −1)@At one, one;;at (2, 1):  (2, −1)@At two, one;;at (0, 3):  (0, −3)@at zero, three"
Take x prime equals x, and y prime equals minus y. At one, one the arrow is one, minus one. At two, one it's two, minus one. And at zero, three it's zero, minus three.

@chapter A solution is a curve
@art phase-curve
A solution is a pair of functions, x of t and y of t, whose velocity at every moment is the arrow at the point where it is. Plot those points as t runs, and you get a curve that's tangent to the field everywhere it goes. The plane with x and y as its axes is the phase plane.

@art time-axis-mistake
Notice what's missing. Neither axis is time. Time is how far along the curve you've gone. And because there's no t on the right-hand side, the arrow at a point is the same whenever you arrive, so two solutions that meet at a point leave it in the same direction.

@chapter Euler, both at once
@math heading="Euler step" items="new point = point + h·arrow@The new point;;(x + h·x′,  y + h·y′)@Both coordinates"
Euler's method works here too. The new point is the old point plus h times the arrow. Both coordinates move before either rate is read again.

@math heading="x′ = x,  y′ = −y  from (1, 1),  h = 1/4" items="step 1:  (5/4, 3/4)@five quarters;;step 2:  (25/16, 9/16)@twenty five sixteenths;;step 3:  (125/64, 27/64)@a hundred and twenty five"
Start at one, one with h equal to a quarter. The arrow is one, minus one, so the first step lands at five quarters, three quarters. Next comes twenty five sixteenths, nine sixteenths. Then a hundred and twenty five over sixty four, twenty seven over sixty four.

@art saddle-paths
Each step multiplies x by five quarters and y by three quarters. So the point heads away from the origin along the x direction while y dies away. Going out along one direction and in along another is the picture of a saddle.

@chapter What the solution keeps
@math heading="(x·y)′ = x′·y + x·y′" items="= x·y − x·y = 0@which is zero;;through (1, 1):  x·y = 1@the curve x y equals one;;Euler, 3 steps:  3375/4096 = (15/16)³@three thousand"
By the product rule, the derivative of x times y is x prime y plus x y prime. That's x y minus x y, which is zero. So the true solution through one, one stays on the curve x y equals one. But Euler's third point gives three thousand three hundred and seventy five over four thousand and ninety six, which is fifteen sixteenths cubed.

@art euler-polygon
Each step multiplies the product by one plus h, times one minus h, which is fifteen sixteenths. So the polygon slips inside the curve. Every step is computed exactly, and the polygon still isn't the solution.

@art euler-spiral
On a rotation, x prime equals y and y prime equals minus x, the true solutions are circles. Each Euler step moves along a tangent, and a tangent always leaves the circle. So the squared distance grows by exactly one plus h squared. With h a quarter, that's seventeen sixteenths, every step.

@chapter Where people slip
@list heading="Common slips" items="Reading an axis as time@The first|Using h × coefficient, not h × arrow@The second|Taking the polygon for the solution@And the third"
The first slip is reading the horizontal axis as time. It's x. The second is multiplying h by the coefficient but not the coordinate. From two, one with x prime equals x, the step in x is a quarter times two, a half, not a quarter. And the third is taking Euler's polygon for the solution itself.

@chapter Try it
@words text="x′ = −x,  y′ = −2y" sub="from (2, 2),  h = 1/4"
Your turn. Take x prime equals minus x and y prime equals minus two y, starting at two, two with h a quarter. Read the arrow there, scale it by h, and add it on. Where does the first step land?

@end text="Step a system through its field"
You can look at the arrows and step the polygon yourself on Learn. That's learn dot get er done dot I O.
