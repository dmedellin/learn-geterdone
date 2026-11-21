---
format: long
lesson: separable-equations-growth-and-decay/newtons-law-of-cooling
title: Newton's law of cooling: the gap decays, not the temperature
thumb: The gap decays, not the coffee
---

@chapter The question
@title text="Newton's Law of Cooling" sub="Separable Equations, Growth and Decay" art=thumb
A cup of coffee at a hundred degrees stands in a room at twenty. How does it cool? Not at a steady rate, as it turns out, and the reason is one subtraction.

@art hot-cup
Newton's observation was that the coffee loses heat at a rate proportional to how much hotter it is than the room. The bigger the gap, the faster it cools. Take the constant of proportionality to be one quarter per minute.

@chapter The law
@math heading="Newton's law of cooling" items="y′ = −k·(y − A),  k > 0@y prime equals minus k"
For a body at temperature y in surroundings at a constant temperature A, y prime equals minus k times y minus A. It assumes the room stays at A, and the body has one temperature throughout.

@chapter One substitution
@math heading="y′ = −(1/4)·(y − 20),  y(0) = 100" items="u = y − 20,  u(0) = 80@Put u;;u′ = −(1/4)·u@decay equation;;u = 80·e^(−t/4)@so u is;;y = 20 + 80·e^(−t/4)@add the twenty back"
Put u equal to the gap, y minus twenty, so u starts at eighty. The room temperature is constant, so u prime is y prime, and the equation becomes u prime equals minus a quarter u, the decay equation. So u is eighty times e to the minus t over four. Add the twenty back, and y is twenty plus that.

@art gap-shrinks
So it's the gap that decays, and the temperature is that decaying gap sitting on top of the room's level. In general, y equals A plus y nought minus A, times e to the minus k t.

@words text="rate: −20·e^(−t/4)" sub="= −(1/4)·80·e^(−t/4)  ✓"
Check by differentiating. The rate of twenty plus eighty e to the minus t over four is minus twenty e to the minus t over four, and that's exactly minus a quarter of the gap. Evaluating is rounded, so differentiating is the right check.

@chapter The rate isn't constant
@math heading="Euler,  h = 1 minute" items="gap 80,  rate −20  →  y₁ = 80@rate is minus twenty;;gap 60,  rate −15  →  y₂ = 65@minus fifteen;;gap 45,  rate −45/4  →  y₃ = 215/4@minus forty five quarters"
Run Euler's method with a step of one minute. The first rate is minus twenty, so the coffee drops to eighty. Now the gap is sixty, the rate is minus fifteen, and it drops to sixty five. Then the gap is forty five, the rate minus forty five quarters, and it reaches two hundred fifteen over four.

@art staircase-cooling
Every gap is the one before times three quarters, which is one minus k h. So after n steps the temperature is twenty plus eighty times three quarters to the n. The rate changes at every step because the gap does.

@math heading="At t = 4" items="y₄ = 20 + 80·81/256 = 725/16 = 45.3125@seven hundred twenty five;;closed form 20 + 80·e^(−1) ≈ 49.4304@the closed form;;error ≈ 4.11786@differ by"
At step four, that's seven hundred twenty five over sixteen, forty five point three one two five, exactly. The closed form at t equals four is about forty nine point four three. They differ by about four point one two, because a one minute step assumes the rate stays put while the true rate keeps falling.

@chapter Warming works too
@math heading="5° cup in a 20° room,  k = 1/2,  h = 1" items="gap −15,  factor 1/2@minus fifteen;;5,  25/2,  65/4,  145/8,  305/16 …@climb towards twenty"
A cup at five degrees in a room at twenty has a gap of minus fifteen, and the rate is positive. With k equals one half and a step of one, the factor is a half, so the gap halves each step. The temperatures five, twenty five halves, sixty five quarters, and so on, climb towards twenty, and none of them passes it.

@art warming-curve
The temperature approaches the room and never reaches it, because the gap is never zero. Twenty is an equilibrium. Start there, and nothing changes.

@art fridge-drink
A drink at twenty five degrees in a fridge at four works the same way. The gap is twenty one, the factor is nine tenths, and the steady state is four.

@chapter When the gap halves
@words text="ln 2/k = 4·ln 2 ≈ 2.77259 min" sub="then the coffee is at 60°"
The gap halves in ln two over k, the half life again. For a quarter, that's four ln two, about two point seven seven minutes, and the coffee is then at sixty degrees. The exact sequence first reaches sixty or below at step three, at fifty three point seven five, having been at sixty five a step earlier.

@chapter Where people slip
@list heading="Common slips" items="Cooling at a constant rate@The first|Decaying the temperature, not the gap@The second|Treating warming as a separate law@The third"
The first slip is believing the coffee cools at a constant rate. A steady twenty a minute would put it at room temperature after four minutes, and below after that, which the law forbids. The second is applying the decay factor to the temperature instead of the gap. The third is treating warming as a separate law.

@art wrong-target
A hundred times three quarters to the n heads for zero, not twenty. At step four it gives about thirty one point six, and it keeps falling past the room. Only the gap decays.

@chapter Try it
@words text="y′ = −(1/4)·(y − 20),  y(0) = 100" sub="take four steps of 1 minute"
Your turn. Take the coffee from a hundred, with a step of one minute. Multiply the gap by three quarters four times, add twenty, and check you land on seven hundred twenty five over sixteen.

@end text="Watch the gap shrink"
You can try a hot cup, a cold cup and a drink in the fridge, on Learn. That's learn dot get er done dot I O.
