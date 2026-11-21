---
format: long
lesson: equilibria-stability-and-phase-lines/sketching-solutions-from-the-phase-line
title: Sketching solutions from the phase line, bends and all
thumb: The bend flips at a level
---

@chapter The question
@title text="Sketching Solutions from the Phase Line" sub="Equilibria, Stability and Phase Lines" art=thumb
Can you draw a solution's actual shape, with its bends, without a formula? The phase line gives the outline. One more derivative gives the bends.

@chapter The outline
@art outline
In the t y plane, each equilibrium is a horizontal line that no solution crosses. Between them, every solution rises or falls as the arrow says, never turning round, and levels off towards a stable equilibrium. Near an unstable one, it leaves slowly and then speeds up.

@chapter The second derivative
@math heading="Differentiate y′ = f(y)" items="y″ = f′(y)·y′@chain rule;;y″ = f′(y)·f(y)@replace y prime"
Differentiate both sides of y prime equals f of y with respect to t. On the left, that's y double prime. On the right, the chain rule gives f prime of y times y prime. Replace y prime by f of y, and y double prime equals f prime of y times f of y, a function of y alone.

@words text="same signs: concave up    different: concave down"
So where f prime and f have the same sign, y double prime is positive and the curve bends up. Where their signs differ, it bends down.

@art sign-table
So a sketch starts from a small table. In each gap, write the sign of f prime and the sign of f, and their product tells you which way the curve bends there.

@chapter A worked example
@math heading="y′ = (y − 1)·(y − 3),   f′(y) = 2y − 4" items="y < 1:   − · +  →  concave down@below one;;1 < y < 2:   − · −  →  concave up@between one and two;;2 < y < 3:   + · −  →  concave down@between two and three;;y > 3:   + · +  →  concave up@above three"
Take y minus one times y minus three, so f prime is two y minus four. y double prime is zero at one and three, the equilibria, and at two, which isn't one. Below one, the signs differ: concave down. Between one and two, both negative: concave up. Between two and three: concave down. Above three: concave up.

@math heading="From y(0) = 5/2" items="f(5/2) = −3/4:  falls@falls;;at 5/2:  y″ = 1·(−3/4) = −3/4@concave down;;at 3/2:  y″ = (−1)·(−3/4) = 3/4@concave up"
Start at five halves. f there is minus three quarters, so the solution falls. At the start, y double prime is one times minus three quarters, concave down. It crosses the level two, and at three halves, y double prime is minus one times minus three quarters, three quarters, concave up, flattening towards one.

@art inflection-level
So the inflection is at the level y equals two. And in that gap, the speed is one at two and less everywhere else, so the curve is steepest there. A curve that's steepest at a point has no change of slope there. The inflection and the fastest point are the same level.

@chapter What a sketch must show
@list heading="A sketch shows" items="Equilibria as horizontal lines, never crossed@Each equilibrium|Monotone curves in each gap@In each gap|Inflection levels, where the bend flips@Each inflection level|Any curve slid sideways is another@And any curve"
Each equilibrium as a horizontal line, never crossed. In each gap, monotone curves, rising or falling as the arrow says, levelling off towards a stable equilibrium. Each inflection level as a guide, with the bend flipping where a curve crosses it. And any curve slid left or right is another curve of the same equation.

@chapter The logistic S
@math heading="y′ = y·(1 − y/4),   f′(y) = 1 − y/2" items="f′ = 0 at y = 2@zero at two;;slopes at 1/2, 1, 2, 3, 4:   7/16, 3/4, 1, 3/4, 0@seven sixteenths"
Take the logistic equation y times one minus y over four. f prime is one minus y over two, zero at two, half the capacity. The slopes at a half, one, two, three and four are seven sixteenths, three quarters, one, three quarters, and zero.

@art logistic-sketch
From one, the curve rises, concave up until it crosses two, steepest there, then concave down, levelling off at four. From six, it falls to four, concave up all the way, with no inflection, since f prime and f are both negative above four.

@words text="cubic: inflections at (4 ± √7)/3" sub="≈ 0.451416 and ≈ 2.21525"
Not every inflection level is a fraction. The cubic from earlier lessons has f prime equal to three y squared minus eight y plus three, with roots four plus or minus root seven, over three. The lab places only rational levels, but the sketch still has two bends.

@chapter Where people slip
@list heading="Common slips" items="Drawing a straight line or a parabola@The first|Marking the equilibria as inflections@The second|Putting the inflection at a time@The third"
The first slip is sketching a straight line or a parabola between equilibria. The second is marking equilibria as inflections. There the solution is a flat line, with no bend. The third is putting the inflection at a time instead of a level.

@art straight-vs-s
A straight line has one slope throughout, and a parabola can't level off at both ends. The logistic slopes rise to one at two and fall to zero at four. The curve is an S, and each equation draws its own.

@art same-level
Two solutions of the logistic equation, starting at a half and at one, both bend at y equals two. But the first gets there later. The level is the same, the time isn't.

@chapter Try it
@words text="y′ = (y − 1)·(y − 3)" sub="sketch from 0 and from 5/2"
Your turn. Sketch the solutions of y minus one times y minus three that start at zero and at five halves. Draw the equilibrium lines first, then the inflection level, and check each bend against the sign table.

@end text="Sketch it from the line"
You can compare your sketch with the curves the lab draws, on Learn. That's learn dot get er done dot I O.
