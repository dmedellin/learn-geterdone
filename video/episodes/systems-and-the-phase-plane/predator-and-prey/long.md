---
format: long
lesson: systems-and-the-phase-plane/predator-and-prey
title: Predator and prey: why foxes and rabbits go round in loops
thumb: They never settle
---

@chapter The question
@title text="Predator and Prey" sub="Systems and the Phase Plane" art=thumb
Foxes eat rabbits. More rabbits feed more foxes, and more foxes eat more rabbits. Do the two populations settle down to a balance? There is a balance point. But they never reach it.

@chapter The model
@math heading="Lotka–Volterra" items="x′ = α·x − β·x·y@x prime equals alpha x;;y′ = −γ·y + δ·x·y@y prime equals minus gamma y"
Let x be the prey and y the predators. x prime equals alpha x minus beta x y, and y prime equals minus gamma y plus delta x y, with all four constants positive.

@art meetings
The assumptions are named, not defended. Prey have unlimited food and grow without bound alone. Predators starve alone. And meetings happen at a rate proportional to the product of the two populations, moving numbers from prey to predators.

@math heading="α = 2,   β = γ = δ = 1" items="x′ = 2x − x·y = x·(2 − y)@two x minus x y;;y′ = −y + x·y = y·(x − 1)@minus y plus x y"
Take alpha as two and the rest as one. Then x prime is two x minus x y, which factors as x times two minus y. And y prime is minus y plus x y, which is y times x minus one. Prey grow while there are fewer than two predators. Predators grow while there are more than one prey.

@chapter The equilibria
@art two-equilibria
Pair the factors, and the equilibria that matter are zero, zero and one, two. The Jacobian has rows two minus y, minus x, and y, x minus one.

@math heading="Jacobians" items="(0, 0):  rows 2 0 and 0 −1,  Δ = −2@At zero, zero;;(1, 2):  rows 0 −1 and 2 0@At one, two;;τ = 0,  Δ = 2,  λ = ±i·√2@plus or minus i"
At zero, zero, the rows are two, zero and zero, minus one. The determinant is minus two: a saddle. At one, two, the rows are zero, minus one and two, zero. The trace is zero, the determinant is two, and the roots are plus or minus i root two.

@art saddle-corner
The saddle makes sense. At the origin, prey grow out along the x axis, and predators die away down the y axis. With no foxes, the rabbits boom. With no rabbits, the foxes starve.

@words text="centre of J: inconclusive"
That's the borderline case. The Jacobian says centre, and from the last lesson you know a centre of the Jacobian settles nothing. Something else has to decide.

@chapter A quantity that's kept
@math heading="for x > 0,  y > 0" items="V = x − ln x + y − 2·ln y@V equals x;;V′ = (1 − 1/x)·x′ + (1 − 2/y)·y′@V prime;;= (x − 1)(2 − y) + (y − 2)(x − 1) = 0@cancel"
Here it is. V equals x minus the log of x, plus y minus two log y. Differentiate along a solution: V prime is one minus one over x, times x prime, plus one minus two over y, times y prime. Substitute the equations, and you get x minus one times two minus y, plus y minus two times x minus one. Those two terms cancel.

@art level-loops
So V never changes along a solution, and each solution stays on one level curve of V. V is smallest at one, two and rises on all sides, so near it those level curves are closed loops. The populations go round and come back.

@chapter Going round
@art lag-peaks
Predators only grow when prey are above one. So the predator peak comes after the prey peak, and the loop runs anticlockwise. Start exactly at one, two and nothing moves. Start anywhere else in the first quadrant, and you circle the point for ever.

@chapter Where people slip
@math heading="V at the start and at the balance" items="(1, 1):  V = 2@one, one;;(1, 2):  V = 3 − 2·ln 2 ≈ 1.61371@three minus two"
The first slip is expecting the populations to settle. At the start one, one, V is two. At the balance, V is three minus two log two, about one point six one. V never changes, so the start can never reach the balance.

@list heading="Two more slips" items="Taking the drawn loop as a proof@The second|Taking J's centre as the model's reason@And the third"
The second slip is taking the drawn loop as a proof that orbits close. It's stepped in floating point, and a very slow spiral could look the same. And the third is thinking the Jacobian's centre is why the model is a centre. The cubic example had the same linearisation and spiralled out.

@art drawing-vs-proof
The picture is evidence. The reason is the conserved quantity, V prime equals zero, together with the shape of V.

@chapter Try it
@words text="x′ = x·(2 − y),   y′ = y·(x − 1)" sub="show V′ = 0"
Your turn. Factor each rate, pair the factors to find both equilibria, and linearise at each. Then substitute the equations into V prime yourself and watch the two terms cancel.

@end text="Watch the populations cycle"
You can start the populations anywhere and watch them loop on Learn. That's learn dot get er done dot I O.
