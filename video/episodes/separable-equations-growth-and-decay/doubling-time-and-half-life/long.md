---
format: long
lesson: separable-equations-growth-and-decay/doubling-time-and-half-life
title: Doubling time and half-life: T = ln 2 over k
thumb: Same doubling time, any start
---

@chapter The question
@title text="Doubling Time and Half-Life" sub="Separable Equations, Growth and Decay" art=thumb
How long does an exponentially growing quantity take to double? The surprise is that the answer doesn't depend on how much you start with. Only the rate matters.

@chapter One equation
@math heading="y = y₀·e^(kt)" items="y = 2·y₀@doubled when;;e^(kT) = 2@e to the k T;;kT = ln 2@natural logarithm;;T = ln 2/k@T equals ln two over k"
The solution y nought times e to the k t has doubled when y is two y nought. That means e to the k T equals two. Take the natural logarithm of both sides, and k T equals ln two. So T equals ln two over k.

@art doubling-ladder
Picture the curve. It reaches double, then double again, then again, and each doubling takes the same stretch of time.

@art halving-ladder
For decay, with k negative, the quantity halves in ln two over the size of k. That's the half life. And ln two is irrational, about zero point six nine three one four seven, so these times are always rounded.

@math heading="Three rates" items="k = 1/2:   T = 2·ln 2 ≈ 1.38629@one half;;k = 1/10:   T = 10·ln 2 ≈ 6.93147@one tenth;;k = −1/2:   half-life 2·ln 2 ≈ 1.38629@minus one half"
With k equals one half, T is two ln two, about one point three eight six two nine. With k equals one tenth, T is ten ln two, about six point nine three. And with k equals minus one half, the half life is again about one point three eight six two nine.

@words text="k·T = ln 2" sub="k = 0.07 per year → about 10 years"
A bigger rate gives a shorter doubling time, and the product k T is ln two for every equation of this kind. So T is about zero point six nine three over k. A rate of seven percent a year doubles in about ten years, rounded.

@chapter The start drops out
@math heading="Why the start doesn't matter" items="y(t + T) = y₀·e^(kt)·e^(kT)@at time t plus T;;= 2·y(t)@two times y of t"
Here's why. The amount at time t plus T is y nought times e to the k t, times e to the k T. That last factor is two, so it's two times y of t. Whatever y of t is, doubling it takes T.

@art scaled-curves
A culture of a thousand and a culture of a million, with the same k, have the same doubling time. Start at one with target two, or at eight with target four and k minus one half, and you get the same one point three eight six two nine. The amount scales the curve and moves nothing along the time axis.

@chapter Where Euler crosses
@math heading="k = 1/2,  h = 1/4,  factor 9/8" items="step 5:  (9/8)⁵ = 59049/32768 ≈ 1.80203@step five;;step 6:  (9/8)⁶ = 531441/262144 ≈ 2.02729@step six;;first past 2: step 6, t = 3/2@So the exact sequence"
Now the exact Euler sequence. With k equals one half and a step of a quarter, the factor is nine eighths. At step five it's about one point eight, below two. At step six it's about two point zero two seven, above two. So the exact sequence first reaches double at step six, which is t equals three halves.

@art grid-crossing
The true curve passes two at about one point three eight six, between steps five and six. For growth, the sequence lies below the curve, so it can't cross earlier. Here it crosses at the first grid point after T. It doesn't have to.

@math heading="k = 1/10,  h = 1,  factor 11/10" items="(11/10)⁷ ≈ 1.94872@step seven;;(11/10)⁸ ≈ 2.14359@step eight;;closed form at t = 7: ≈ 2.01375@at t equals seven"
With k equals one tenth and a step of one, the factor is eleven tenths. At step seven it's about one point nine five, still below two. At step eight it's about two point one four. But at t equals seven the closed form already reads about two point zero one. The sequence is late by a whole step.

@art late-crossing
So the crossing step is an exact fact about the sequence on its grid. With a fine step it's within a step of T. With a coarse one, it can be more.

@chapter Where people slip
@list heading="Common slips" items="Thinking T depends on the start@The first|Getting T upside down@The second|Reading the crossing step as T@The third"
The first slip is believing the doubling time depends on the starting amount. The formula has no place to put the start. The second is getting T upside down, as k over ln two. A faster rate must shorten the time. The third is reading the crossing step as the doubling time. Step six is the sequence, not the equation.

@art rate-and-time
A quick check for the second slip: k times T must be ln two. So doubling k halves T. One half against one tenth gives about one point three nine against six point nine three, about five times shorter.

@chapter Try it
@words text="k = 1/2:  T = ?" sub="then start at 5, target 10"
Your turn. Work out the doubling time for k equals one half from e to the k T equals two. Then start at five with target ten, and confirm the time hasn't moved.

@end text="Change the start, keep the time"
You can change the start and the step, and watch where the sequence crosses, on Learn. That's learn dot get er done dot I O.
