---
format: long
lesson: separable-equations-growth-and-decay/implicit-and-explicit-solutions
title: Implicit and explicit solutions: which branch, and where it lives
thumb: Pick the branch, state the interval
---

@chapter The question
@title text="Implicit and Explicit Solutions" sub="Separable Equations, Growth and Decay" art=thumb
Separating an equation hands you a relation, like y squared equals t squared plus four. But a relation isn't a function yet. Which y do you mean, and for which t does it exist?

@art two-branches
y squared equals t squared plus four allows two values of y for each t. Solve it as a quadratic with no linear term and you get y equals plus or minus the square root of t squared plus four. Each sign gives a function, and both solve y times y prime equals t.

@chapter The initial value picks
@math heading="y² = t² + 4" items="y = √(t² + 4)  above the axis@above the axis;;y = −√(t² + 4)  below the axis@below it;;y(0) = 2 selects the positive root@y of zero equals two;;y(0) = −2 selects the negative root@minus two"
The positive root lives above the axis, and the negative root below it. So the sign of the starting value chooses. y of zero equals two selects the positive root. y of zero equals minus two selects the negative one.

@art branch-pick
The branch you didn't choose is still a solution, just not of this initial value problem. The relation names the pair. Only an initial value names one of them.

@words text="t² + 4 > 0 for every t" sub="both branches exist for all t"
Here, t squared plus four is positive for every t, so both branches exist everywhere and never reach y equals zero. That matters, because no solution of y prime equals t over y can cross the axis. At y equals zero the equation gives no slope to follow.

@chapter A domain with two ends
@math heading="y·y′ = −t,  y(0) = 1" items="y²/2 = −t²/2 + C@y squared over two;;C = 1/2@C is one half;;y² = 1 − t²@one minus t squared;;y = √(1 − t²),  −1 < t < 1@between minus one"
Change the right side to minus t, with y of zero equal to one. Then y squared over two equals minus t squared over two, plus C, and C is one half. So y squared equals one minus t squared. Its branch through zero, one, the square root of one minus t squared, exists only between minus one and one, ends excluded.

@art semicircle
Why leave out the ends? At t equals plus or minus one, y is zero, and there y prime equals minus t over y has no value. The formula survives at the ends. The equation doesn't.

@chapter A domain with one end
@math heading="(1/y²)·y′ = 1,  y(0) = 1" items="−1/y = t − 1@minus one over y;;y = 1/(1 − t)@inverting gives;;t < 1@less than one"
For one over y squared times y prime equals one, with y of zero equal to one, the relation is minus one over y equals t minus one. Inverting gives y equals one over one minus t. The solution through zero, one lives only where t is less than one.

@art blow-up
As t approaches one from below, y grows without bound. That's blow up, now with a formula attached.

@art two-pieces
The formula is also defined for t greater than one, where it's negative. That piece solves the equation, but it isn't a continuation of ours. The two are separated by the point where the formula has no value. A solution is a function on one interval, the one holding the starting t.

@chapter When it won't solve
@words text="implicit only" sub="the relation is the solution"
Sometimes the relation can't be solved for y. Then the explicit form reads implicit only, and no domain is given. That's the honest answer for cubics and beyond. The relation is the solution, and you can still differentiate it and check it.

@chapter Where people slip
@list heading="Common slips" items="Taking only the positive root@The first|Giving the formula's domain, not the solution's@The second|Switching branches where y = 0@The third"
The first slip is reading y squared equals t squared plus four as the positive root alone. The square root recovers the size of y, not its sign. The second is stating the domain of the formula instead of the solution. The third is switching branches across a point where y is zero.

@art bad-join
At such a point the two branches meet, and you could draw a curve that looks continuous from one to the other. It isn't a solution there. Each branch arrives with an infinite slope, and the equation doesn't hold at the join. A solution stays on the branch it started on.

@chapter Try it
@words text="y² = t² + 4,  y(0) = −2" sub="which branch? which interval?"
Your turn. Take y squared equals t squared plus four with y of zero equal to minus two. Pick the branch, check that its value at zero really is minus two, and state the interval where it exists.

@end text="Pick the branch, state the interval"
The lab prints the relation, the explicit solution and its domain for each example, on Learn. That's learn dot get er done dot I O.
