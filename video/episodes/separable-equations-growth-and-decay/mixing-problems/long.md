---
format: long
lesson: separable-equations-growth-and-decay/mixing-problems
title: Mixing problems: rate in minus rate out
thumb: Rate in minus rate out
---

@chapter The question
@title text="Mixing Problems" sub="Separable Equations, Growth and Decay" art=thumb
A tank holds a hundred litres of water. Salt water at two grams per litre runs in at five litres a minute, and well stirred solution runs out at the same five litres a minute. How much salt is in the tank, and does it ever reach the inflow's saltiness?

@art tank
Let y be the grams of salt in the tank. The volume stays at a hundred, because the flows match. And well stirred means the concentration inside is y over the volume, everywhere at once.

@chapter Rate in, rate out
@math heading="The balance" items="in:  r·c = 5 × 2 = 10 g/min@what the inflow brings;;out:  r·y/V = 5 × y/100 = y/20 g/min@the outflow carries;;y′ = 10 − y/20@grams in per minute"
The salt changes by what the inflow brings minus what the outflow carries away. In comes the flow times the concentration, five times two, ten grams a minute. Out goes the same flow times the tank's own concentration, five times y over a hundred, y over twenty. So y prime equals ten minus y over twenty, grams in per minute, minus grams out.

@words text="What leaves depends on what's there"
That's the key. A tank with no salt loses none. A tank that holds two hundred grams loses ten a minute, exactly what comes in.

@chapter It's Newton's law again
@math heading="Take out −1/20" items="y′ = 10 − y/20@ten minus y over twenty;;= −(1/20)·(y − 200)@minus one twentieth"
Take out minus one twentieth, and ten minus y over twenty becomes minus one twentieth times y minus two hundred. That's Newton's law of cooling, with k equals one twentieth and a steady amount of two hundred grams.

@art balance
The steady amount is where the rates balance. Ten equals y over twenty at y equals two hundred, which is the inflow concentration times the volume, two times a hundred.

@chapter Solving and stepping
@math heading="y(0) = 0,  pure water" items="y = 200·(1 − e^(−t/20))@the solution is;;factor 1 − 1/20 = 19/20@The factor;;y₁ = 10,  y₂ = 39/2,  y₃ = 1141/40@the first steps"
Start with pure water, so y of zero is zero. The solution is two hundred times one minus e to the minus t over twenty. Step it with one minute. The factor is nineteen twentieths, and the first steps are ten, thirty nine halves, and eleven hundred forty one fortieths.

@art salt-curve
After ten steps the exact value is a fraction with a long denominator. The closed form at t equals ten is two hundred times one minus e to the minus a half, about seventy eight point seven.

@chapter Never quite there
@words text="gap 200·e^(−t/20) > 0" sub="halves every ≈ 13.8629 min"
Does the tank ever get to two grams per litre? The gap, two hundred times e to the minus t over twenty, is positive at every time. The exact sequence agrees, because nineteen twentieths to any power is positive. The gap halves about every thirteen point eight six minutes, which is quick, and it's never zero.

@art flush
Run it the other way. Fill the tank with fifty grams and flush it with pure water at ten litres a minute. Then y prime equals minus y over ten, and the steady amount is zero. The factor is nine tenths, so the amounts go fifty, forty five, eighty one halves, and fall towards zero without ever reaching it.

@art two-tanks
Or top one up. Two hundred fifty litres holding a hundred grams, fed five litres a minute at one point two grams per litre, gives y prime equals six minus y over fifty. Its steady amount is three hundred, and it rises towards it and stays under.

@chapter What it assumes
@list heading="Assumptions" items="The volume doesn't change@The volume|The tank is perfectly mixed@perfectly mixed|The inflow concentration is constant@the inflow"
What the equation assumes is part of the problem. The volume doesn't change. The tank is perfectly mixed. And the inflow concentration is constant. If the outflow differed from the inflow, the volume would change with time, and that's a different problem.

@chapter Where people slip
@list heading="Common slips" items="Expecting the tank to reach 2 g/L@The first|Leaving y/V out of the outflow@The second|Reading the steady amount as a rate@The third"
The first slip is expecting the tank to reach the inflow concentration in finite time, like a glass filling up. The second is leaving the tank's own concentration out of the outflow. The third is reading the steady amount as a rate.

@art straight-line
Write the outflow as a constant five, and y prime is a constant five, so y equals five t, which passes two hundred at forty minutes and keeps going. And the steady amount is two hundred grams, not ten. Ten is grams per minute. The units are the check.

@chapter Try it
@words text="y′ = 10 − y/20,  y(0) = 0" sub="take three steps of 1 minute"
Your turn. Starting from pure water, take three Euler steps of one minute, using the gap and the factor nineteen twentieths. Check you reach eleven hundred forty one fortieths, and that every value stays under two hundred.

@end text="In minus out"
You can flush a tank or top one up, and watch it approach the steady amount, on Learn. That's learn dot get er done dot I O.
