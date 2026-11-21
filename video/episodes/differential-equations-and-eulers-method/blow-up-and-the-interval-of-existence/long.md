---
format: long
lesson: differential-equations-and-eulers-method/blow-up-and-the-interval-of-existence
title: Blow-up: when a solution stops existing
thumb: Smooth isn't for ever
---

@chapter A smooth equation that ends
@title text="Blow-Up and the Interval of Existence" sub="Differential Equations and Euler's Method" art=thumb
Here's an equation with the friendliest possible right side: y prime equals y squared. Start it at y of zero equal to one. The solution exists for a while, and then, at t equals one, it simply stops existing.

@math heading="y′ = y²,  y(0) = 1" items="y = 1/(1 − t)@one over one minus t;;y′ = 1/(1 − t)² = y²@Its derivative;;residual 0@The residual"
The candidate is one over one minus t. Its derivative is one over one minus t, squared, and so is y squared. The residual is zero, and at zero the value is one, so it passes through the start.

@art vertical-asymptote
At three quarters, it's four. At nine tenths, it's ten. And as t approaches one, it grows without limit. There's no value at one at all. The solution lives on t less than one.

@chapter Starting higher ends it sooner
@math heading="y(0) = y₀" items="y = y₀/(1 − y₀·t)@y nought over;;ends at t = 1/y₀@It ends at;;y₀ = 2:   ends at t = 1/2@From two"
Start at y nought instead, and the solution is y nought over one minus y nought times t. It ends at one over y nought. From two, it ends at a half. The end time depends on the start, and nothing in the equation announces it.

@art earlier-end
Two starts, two different ends. The higher start runs out sooner.

@chapter What the theorem promises
@words text="smooth f: exactly one solution near the start" sub="on some interval, of unstated length"
Here's the theorem. If f and its derivative with respect to y are continuous near the start, there's exactly one solution through the start, on some interval around it. But it doesn't say how long that interval is.

@art local-interval
That last part isn't a technicality. Y squared is as well behaved as a function gets, and the interval is still only t less than one. The lab demonstrates this one case, and doesn't prove the theorem. That's for a course in analysis.

@chapter Euler against the solution
@math heading="h = 1/4" items="y₁ = 5/4    true 4/3@five quarters;;y₂ = 105/64    true 2@one hundred and five;;y₃ = 37905/16384 ≈ 2.31354    true 4@thirty seven thousand"
Run Euler with steps of a quarter. The first step gives five quarters, against a true four thirds. The second gives one hundred and five sixty fourths, against two. The third gives thirty seven thousand nine hundred and five over sixteen thousand three hundred and eighty four, about two point three one, against a true four.

@art euler-behind
Euler falls well behind, as it must on a rate that rises this fast. Every step reads a slope smaller than the one it's about to meet. And still the polygon looks tame.

@chapter Stepping past the end
@art step-past
Run five steps, and t reaches five quarters, past one. The lab prints a perfectly good fraction, about six point nine eight five. And the tile for the known solution reads undefined. The method never saw the end, because it never looks further than one step.

@words text="1/(1 − t) at t = 5/4 is −4" sub="a different curve, not this solution"
Don't be fooled by the formula, either. One over one minus t at five quarters gives minus four, but that's a different branch. The solution through zero, one has already ended.

@chapter The digit budget
@art doubling-lengths
Now look at the fractions. The denominators are four, sixty four, sixteen thousand three hundred and eighty four, and on. Their lengths are one, two, five, ten, nineteen, thirty eight, seventy seven digits, roughly doubling. Squaring a fraction doubles its digits, and each step squares.

@words text="stopped after step 11: digit budget"
With a step of a quarter, the lab completes eleven steps, and stops before the twelfth, which would pass its limit of two thousand digits. Nothing was rounded to carry on. A floating point program would hide this by rounding, and keep printing numbers that are no more the solution.

@chapter Where people slip
@list heading="Common slips" items="Expecting a smooth f to give a solution for all t@The first|Reading Euler past the end as the solution@The second|Taking the digit stop for the end of the solution@the third"
The first slip is expecting a smooth right side to give a solution for all t. The second is reading Euler's values past the end as values of the solution. They approximate nothing. And the third is taking the digit budget stop for where the solution ends. That stop is at eleven quarters, and the solution ended at one.

@chapter Try it
@words text="y′ = y²,  y(0) = 2" sub="y = 2/(1 − 2t)"
Your turn. Start at y of zero equal to two. The solution is two over one minus two t. Say where it ends, then take the first Euler step with h equal to a quarter, and see what it gives.

@end text="Smooth isn't for ever"
You can watch Euler step past the end, in exact fractions, on Learn. That's learn dot get er done dot I O.
