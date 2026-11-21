---
format: long
lesson: separable-equations-growth-and-decay/logistic-growth
title: Logistic growth: exponential growth with a ceiling
thumb: Fastest at half the capacity
---

@chapter The question
@title text="Logistic Growth" sub="Separable Equations, Growth and Decay" art=thumb
A population can't grow exponentially for ever. Exponential growth is right for a small population with room and food, and wrong for a large one, because it has no limit. Something has to slow it down as it fills its surroundings.

@chapter The logistic equation
@math heading="Logistic equation" items="y′ = r·y·(1 − y/K)@r times y"
The simplest fix multiplies the exponential rate by a factor that drops to zero at a ceiling. y prime equals r times y, times one minus y over K. Here r is the growth rate and K is the carrying capacity, the level where growth stops. K is a number the model is given, not one it derives.

@art bounding-factor
For a small population, one minus y over K is close to one, and the equation is nearly exponential growth. As y approaches K, the factor falls to zero, and so does the rate.

@chapter The rate at each size
@math heading="r = 1,  K = 4:  f(y) = y·(1 − y/4)" items="f(1) = 3/4@At one;;f(2) = 1@At two;;f(3) = 3/4@at three;;f(4) = 0@at four;;f(5) = −5/4@at five"
Take r equals one and K equals four. At one, the rate is three quarters. At two, it's one. Then at three, back to three quarters, and at four, zero. And at five, it's minus five quarters, negative.

@art rate-hump
So the rate rises from zero, peaks at two, and falls to zero at four. An exponential at three would grow at three. The logistic grows at three quarters, a quarter of the rate.

@chapter Which way it moves
@art phase-arrows
An equilibrium is a value where the rate is zero, so a population placed there stays put. Here those are zero and four. Between them the rate is positive, and above four it's negative. So every start above zero heads for four.

@words text="0 unstable;  4 stable"
Nearby starts move away from zero and towards four. So zero repels and four attracts. The next course defines those words carefully.

@chapter Fastest at half
@math heading="Steepest point" items="f′(y) = 1 − y/2@f prime of y;;f′(2) = 0  at y = 2 = K/2@zero at y equals two;;y″ = f′(y)·y′@y double prime"
The rate is largest where its own rate of change is zero. Here f prime of y is one minus y over two, which is zero at y equals two, half the capacity. And by the chain rule, y double prime is f prime of y times y prime. So that's also where the curve switches from bending up to bending down.

@art s-curve
That gives the familiar S shape. In general, the peak is at half of K, where the rate is r K over four. With K equals ten, the steepest point is at five.

@chapter Exact steps
@math heading="y(0) = 1,  h = 1/2" items="y₁ = 1 + (1/2)·(3/4) = 11/8@The first step;;y₂ = 11/8 + (1/2)·(231/256) = 935/512 ≈ 1.82617@The second"
Start at one with a step of one half. The first step is one plus a half of three quarters, eleven eighths, a little under the three halves that exponential growth would give. The second is nine hundred thirty five over five hundred twelve, about one point eight two six.

@art digit-growth
The right side is quadratic, so the digits in the fractions roughly double at every step. The lab prints exact steps until a number has more than two thousand digits. From this start that's eleven steps, and then it says so. It doesn't round to carry on.

@math heading="Start above K: y(0) = 6" items="f(6) = 6·(1 − 3/2) = −3@minus three;;6 + (1/2)·(−3) = 9/2@nine halves"
Start above the capacity, at six. The rate is six times one minus three halves, minus three. So the first step is six plus a half of minus three, nine halves.

@art above-capacity
The population falls back towards four, and the lab gives its limit as four. Above the capacity, the same factor turns the growth into a decline.

@chapter Where people slip
@list heading="Common slips" items="Exponential growth switched off at K@The first|Putting the steepest point at K@The second|Reading the lab's stop as the population's@The third"
The first slip is picturing an exponential that runs until it hits K, then switches off. There's no switch. The factor trims the rate at every size, and a switch couldn't bring a population above K back down. The second is putting the steepest point at K, where the rate is zero, the flattest. The third is reading the lab's stop as the population's.

@chapter Try it
@words text="y′ = y·(1 − y/4),  y(0) = 6,  h = 1/2" sub="first step: 9/2"
Your turn. Start above the capacity at six, with a step of one half. Work out the rate at six, take the first step to nine halves, then take one more and check it's still heading for four.

@end text="Grow to the capacity"
You can try starts below and above the capacity, and see the exact steps, on Learn. That's learn dot get er done dot I O.
