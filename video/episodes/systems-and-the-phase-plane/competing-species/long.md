---
format: long
lesson: systems-and-the-phase-plane/competing-species
title: Competing species: when do both survive?
thumb: Coexist, or one wins?
---

@chapter The question
@title text="Competing Species" sub="Systems and the Phase Plane" art=thumb
Two species eat the same food. Does one of them always win? Or can they share? The answer lives in one number: the determinant of the Jacobian at the point where both are present.

@chapter The model
@math heading="competition" items="x′ = x·(3 − x − 2y)@x prime equals x;;y′ = y·(2 − x − y)@y prime equals y"
Here's the model this lesson uses. x prime equals x times three minus x minus two y. And y prime equals y times two minus x minus y.

@art crowding
The assumptions are named. Each species grows logistically alone, and crowds both its own kind and the other kind. Here, with no y, x grows towards three, and each unit of y costs it twice as much as a unit of itself.

@chapter Four equilibria
@art four-points
Each rate is zero when its species is zero, or when its bracket is zero. Pair the factors, and you get four equilibria. The origin. Zero, two, where x is extinct. Three, zero, where y is extinct. And the mixed point, where the two bracket lines cross.

@math heading="both brackets zero" items="x + 2y = 3,   x + y = 2@x plus two y;;y = 1,   x = 1@y is one"
For the mixed point, solve x plus two y equals three and x plus y equals two together. Subtracting gives y is one, so x is one. The mixed point is one, one.

@chapter One Jacobian, four readings
@math heading="J rows:  3 − 2x − 2y, −2x  and  −y, 2 − x − 2y" items="(0, 0):  rows 3 0 and 0 2  →  unstable node@At the origin;;(3, 0):  rows −3 −6 and 0 −1  →  stable node@At three, zero;;(0, 2):  rows −1 0 and −2 −2  →  stable node@at zero, two;;(1, 1):  rows −1 −2 and −1 −1  →  saddle@at one, one"
You write the Jacobian once, then put in each point. At the origin the rows are three, zero and zero, two: an unstable node. At three, zero, it's minus three, minus six and zero, minus one: a stable node. And at zero, two, minus one, zero and minus two, minus two: another stable node. Then at one, one, it's minus one, minus two and minus one, minus one.

@words text="τ = −2,   Δ = 1 − 2 = −1" sub="saddle"
At the mixed point, the trace is minus two, and the determinant is one minus two, minus one. Negative. So the mixed point is a saddle.

@art saddle-divide
A saddle has one curve coming in, and everything else goes out. A start exactly on that curve settles at one, one. Every other start nearby leaves, and ends at one of the two stable nodes. Which one depends on which side of the incoming curve you start.

@art two-outcomes
So the long run is one species or the other. On one side, x ends alone at three, zero. On the other, y ends alone at zero, two. That claim comes from the saddle and the two nodes. The lab's drawing just shows one example of it.

@words text="exists, but doesn't last"
So in this model coexistence is an equilibrium that exists and doesn't last. Both populations are positive there, but any disturbance knocks them off.

@chapter Weaker competition
@math heading="halve the cross terms" items="x′ = x·(2 − x − y/2),   y′ = y·(2 − y − x/2)@halve the cost;;mixed point (4/3, 4/3)@four thirds;;τ = −8/3,   Δ = 4/3@minus eight thirds;;λ = −2/3  and  −2@minus two thirds"
Now halve the cost of the other species. x prime is x times two minus x minus y over two, and y prime is y times two minus y minus x over two. The mixed point is four thirds, four thirds. There the trace is minus eight thirds and the determinant is four thirds, positive. The roots are minus two thirds and minus two.

@art coexist-node
That's a stable node. Both species survive from every nearby start. Competition is the same in kind in both models. The strength of the cross terms decided whether the mixed point is a saddle or a sink.

@chapter Where people slip
@list heading="Common slips" items="Competition always means extinction@The first|An equilibrium with both present means coexistence@The second|Dividing by x and losing the axis points@And the third"
The first slip is thinking two competitors always drive one to extinction. It depends on the numbers. The second is taking an equilibrium with both species present as coexistence. It has to be stable. And the third is dividing x prime equals zero by x, which loses zero, zero and zero, two, and with them both outcomes where x dies out.

@art lose-axis
So keep the factors. Set each one to zero in turn, and pair them up.

@chapter Try it
@words text="x′ = x·(2 − x − y/2),   y′ = y·(2 − y − x/2)" sub="check (4/3, 4/3)"
Your turn. For the weaker model, find all four equilibria by pairing factors. Then build the Jacobian at four thirds, four thirds and confirm the trace, determinant and roots.

@end text="Compete the species yourself"
You can classify every equilibrium and watch who wins on Learn. That's learn dot get er done dot I O.
