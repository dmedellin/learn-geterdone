---
format: long
lesson: oscillators-damping-and-resonance/critical-damping-and-design
title: Critical damping: at most one crossing, and why door closers aim for it
thumb: Shut, without the swing back
---

@chapter The question
@title text="Critical Damping and Design" sub="Oscillators, Damping and Resonance" art=thumb
Why is a door closer set to critical damping? To answer that, you need to know exactly when a critically damped motion crosses its rest position. The answer is at most once.

@art door-closer
At critical damping, c equals two root m k, and the characteristic equation has one repeated root, r equals minus c over two m. For m one, c four, k four, that root is minus two.

@chapter The solution
@math heading="x = (C₁ + C₂·t)·e^(rt)" items="x′ = (C₂ + r·C₁ + r·C₂·t)·e^(rt)@its rate;;x(0) = C₁,   x′(0) = C₂ + r·C₁@At t equals zero;;C₁ = x₀,   C₂ = v₀ − r·x₀@So C one"
The motion is C one plus C two t, times e to the r t. Take its rate by the product rule. At t equals zero, x is C one, and the rate is C two plus r C one. So C one is the start, and C two is the starting velocity minus r times the start.

@art line-times-decay
So the motion is a straight line in t times a decaying exponential. The exponential is never zero. So x is zero exactly where the line is.

@words text="zero at t = −C₁/C₂" sub="counts only if t > 0"
And a straight line meets the axis at most once, at t equals minus C one over C two. That counts only if it's positive, which happens exactly when C one and C two are both nonzero with opposite signs.

@chapter Two starts on one damper
@math heading="m = 1,  c = 4,  k = 4,  r = −2" items="(1, 1):  C₂ = 1 − (−2)·1 = 3@moving outward;;x = (1 + 3t)·e^(−2t),  zero at t = −1/3@one plus three t"
Release the mass at one, moving outward at speed one. C one is one, and C two is one minus minus two times one, three. So x is one plus three t, times e to the minus two t. Its zero, minus a third, is in the past.

@art no-crossing
The mass drifts out a little further, then decays to rest from above. It never reaches the rest position.

@math heading="start (1, −5)" items="C₂ = −5 − (−2)·1 = −3@minus five minus minus two;;x = (1 − 3t)·e^(−2t),  zero at t = 1/3@one minus three t"
Now release it at one, moving inward at speed five. C two is minus five minus minus two, minus three, the opposite sign to C one. So x is one minus three t, times e to the minus two t, and it's zero at t equals a third.

@art one-crossing
The mass passes through rest once, goes to the far side, and creeps back from below. Critical damping doesn't forbid an overshoot. It forbids a second crossing.

@chapter The door closer
@words text="v₀ = 0  ⟹  C₂ = (c/(2m))·x₀" sub="same sign as C₁ = x₀"
Model the door as a mass, the closing spring as k, and the oil damper as c, with x the angle from shut. Someone opens it and lets go, a start from rest. Then C two is c over two m times x nought, the same sign as C one. So the door never crosses shut.

@art three-door-closes
A weaker damper would swing it through the frame and back. A stronger one would close it slowly.

@math heading="m = 1,  k = 4:  long-run rate" items="c = 2:  1@a damper of two;;c = 3:  3/2@three halves;;c = 4:  2@at four;;c = 5:  1@at five"
And slowly can be measured. With m one and k four, the long-run rate is one for a damper of two, three halves at three, two at four, and back to one at five.

@art decay-rate-peak
It rises to its peak at the critical value, then falls. The two roots multiply to k over m, which is four. Past the border, raising c pushes the fast root out and the slow root toward zero.

@chapter Where people slip
@list heading="Common slips" items="Critical is quickest in every sense@The first|Critical never crosses zero@The second|C₂ is the starting velocity@The third"
The first slip is thinking critical is quickest in every sense. It wins the long-run race, but released from rest, c equals three reaches rest in finite time, then overshoots. The second is assuming it never crosses zero. It can, once. And the third is taking C two as the starting velocity. For one, minus five, that wrongly puts the crossing at a fifth.

@chapter Try it
@words text="start (1, −5)" sub="x′ = (6t − 5)·e^(−2t)"
Your turn. Check one minus three t, times e to the minus two t, by substitution. Its rate is six t minus five, times e to the minus two t. Find the second rate and show the residual is zero.

@end text="One line, one crossing at most"
You can try any start and read the crossing time exactly, on Learn. That's learn dot get er done dot I O.
