---
format: long
lesson: equilibria-stability-and-phase-lines/autonomous-equations
title: Autonomous equations: no clock on the right side
thumb: Equilibria are the roots of f
---

@chapter The question
@title text="Autonomous Equations" sub="Equilibria, Stability and Phase Lines" art=thumb
Some differential equations never mention the time on their right side. That one restriction changes a lot. It makes the slope field repeat, lets you slide solutions sideways, and turns finding constant solutions into plain algebra.

@chapter What autonomous means
@math heading="Autonomous" items="y′ = f(y)@y prime equals f of y;;f(y*) = 0  ⟹  y = y* is a solution@an equilibrium"
An equation is autonomous when it can be written y prime equals f of y, with the right side a function of y alone. An equilibrium is a number, call it y star, where f of y star is zero. Then the constant function y equals y star is a solution for every t.

@list heading="Which are autonomous?" items="y′ = k·y   ✓@Exponential growth|y′ = −k·(y − A)   ✓@Newton's law|y′ = y² − 1,  y′ = 3 − y   ✓@y squared minus one|y′ = 2t,  y′ = t·y,  y′ = y + t   ✗@not"
The test is only whether t appears. Exponential growth is autonomous, and so is Newton's law of cooling, whose only equilibrium is the room temperature. y squared minus one and three minus y are autonomous too. But y prime equals two t is not, and nor are t y and y plus t.

@chapter The field repeats
@art repeating-field
The slope at a point t, y is f of y, whatever t is. So the column of slopes above t equals one is the same as the column above t equals five. Only the height matters. Every horizontal line carries one slope from end to end.

@art single-axis
That's why the lab draws just one line, the y axis, and puts on it everything the field knows. The rest of the field is copies.

@chapter Sliding sideways
@words text="y(t) a solution  ⟹  y(t − c) a solution"
Here's a consequence. If y of t solves the equation, so does y of t minus c, for any constant c.

@math heading="Why" items="w(t) = y(t − c)@Put w of t;;w′(t) = y′(t − c)@by the chain rule;;= f(y(t − c)) = f(w(t))@because y satisfies"
Put w of t equal to y of t minus c. By the chain rule, w prime is y prime at t minus c, because t minus c has slope one. And that's f of y at t minus c, because y satisfies the equation everywhere. So w prime equals f of w.

@art sliding-solution
Slide a solution left or right, and it meets the same slopes, so it's a solution again. For y prime equals t y, that last step fails. The right side would become t minus c times y, not t times w.

@chapter Finding the equilibria
@math heading="f(y) = y³ − 4y² + 3y" items="= y·(y² − 4y + 3)@take out y;;= y·(y − 1)·(y − 3)@factor;;equilibria:  0,  1,  3@read off"
The equilibria are the roots of f, so you find them by algebra. Write f as a polynomial, take out y, factor what's left as y minus one times y minus three, and read off the roots: zero, one and three.

@art cubic-roots
On a graph of f against y, those are the three places where the curve crosses the axis. Each one is a constant solution.

@math heading="y′ = y² − y − 1" items="y* = (1 ± √5)/2@one plus or minus;;≈ 1.61803,  ≈ −0.618034@rounded"
Not every equilibrium is a fraction. For y squared minus y minus one, the equilibria are one plus or minus root five, over two. Rounded, that's about one point six one eight and minus zero point six one eight. The surd stays exact, so the check that f is zero there can be stated exactly.

@chapter Not a pause
@art equilibrium-lines
A solution that's at an equilibrium at one instant is there at every instant, before and after. Through each point there's exactly one solution, and the constant is already one, so no other curve can pass through it.

@words text="y′ = −(1/2)·(y − 20)" sub="only equilibrium: y = 20"
Cooling shows it with no lab at all. With the room at twenty, the right side is zero only when y is twenty. A cup already at room temperature stays there at every later time, and at every earlier one.

@chapter Where people slip
@list heading="Common slips" items="Treating an equilibrium as a pause@The first|Cancelling a factor and losing a root@The second|Treating the decimal as the equilibrium@The third"
The first slip is treating an equilibrium as somewhere a solution stops for a while. If y of three is one for y squared minus one, then y of zero is one as well. The second is cancelling a factor that can be zero. The third is rounding an irrational equilibrium and treating the decimal as the real thing.

@art lost-root
Divide y squared minus y by y, and you see only the root one. The factored form, y times y minus one, shows two, zero and one. And f of one point six one eight isn't zero, so that constant isn't a solution. Keep the surd, and write approximately for sizes.

@chapter Try it
@words text="y′ = y² − 1" sub="find the equilibria, then check them"
Your turn. Find the equilibria of y prime equals y squared minus one by factoring, then substitute each constant back in and check the residual is exactly zero.

@end text="Find the roots of f"
You can type any polynomial and see its equilibria found exactly, on Learn. That's learn dot get er done dot I O.
