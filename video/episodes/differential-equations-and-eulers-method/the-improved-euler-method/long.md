---
format: long
lesson: differential-equations-and-eulers-method/the-improved-euler-method
title: The improved Euler method: average the slopes at both ends
thumb: Halve the step, quarter the error
---

@chapter A second look at the slope
@title text="The Improved Euler Method" sub="Differential Equations and Euler's Method" art=thumb
Euler's method uses the slope at the start of a step, and nothing else. The improved method also asks what the slope would be at the end. That costs one more slope reading per step, and it changes how fast the error falls.

@math heading="The improved Euler method" items="k₁ = f(tₙ, yₙ)@k one;;k₂ = f(tₙ + h, yₙ + h·k₁)@k two;;yₙ₊₁ = yₙ + h·(k₁ + k₂)/2@the average"
First read the start slope, k one. Then take an ordinary Euler step to a trial point, and read the slope there, k two. Finally, move from the start along the average of the two. It's also called Heun's method.

@art trial-step
The trial point is only a guess at where the step would end. It's used for nothing except reading that second slope.

@art average-slope
Why average? The true slope changes through a step. Where the rate rises, the start slope is too low, and the end slope is too high. Their average is a better stand in for the whole step.

@chapter One step by hand
@math heading="y′ = y,  y(0) = 1,  h = 1/4" items="k₁ = 1@start slope;;trial:  1 + (1/4)·1 = 5/4,   k₂ = 5/4@trial value;;average:  (1 + 5/4)/2 = 9/8@average slope;;y₁ = 1 + (1/4)·(9/8) = 41/32@y one"
Take y prime equals y from one, with a step of a quarter. The start slope is one. The trial value is five quarters, so the trial slope is five quarters. The average slope is nine eighths, and y one is one plus a quarter of nine eighths: forty one thirty seconds.

@art heun-step
Plain Euler gave five quarters, which is forty thirty seconds. The true value, e to the quarter, is about one point two eight four, and forty one thirty seconds, about one point two eight one, is nearer.

@chapter The trapezoid rule, again
@art trapezoid-step
Now take y prime equals t squared. The right side doesn't mention y, so the trial value never matters. K one is t squared, k two is t plus h, squared, and the step adds h times their average. That's the trapezoid rule on one piece.

@math heading="y′ = t²,  T = 1" items="h = 1/4:   E = 1/96@one ninety sixth;;h = 1/8:   E = 1/384@three hundred and eighty four;;h = 1/16:   E = 1/1536@one thousand five hundred;;ratios:  4,  4@exactly four"
So the error is the trapezoid rule's, exactly h squared over six. At a quarter, that's one ninety sixth. At an eighth, one over three hundred and eighty four. At a sixteenth, one over one thousand five hundred and thirty six. Both ratios are exactly four.

@art four-vs-two
Halving h now divides the error by four, not two. That makes the improved method second order, with an error about C times h squared. As before, the lab demonstrates this on chosen equations, and doesn't prove it in general.

@chapter Near four, not four
@math heading="y′ = t⁴" items="ratios:  848/213 ≈ 3.98122,   3408/853 ≈ 3.99531@The ratios"
Change the equation to y prime equals t to the fourth. The ratios are about three point nine eight and three point nine nine five. They climb toward four and aren't four, because the trapezoid error has a smaller term in h to the fourth as well.

@art close-not-equal
On a cubic, the exactness comes back. For y prime equals t cubed, the errors are one sixty fourth, one over two hundred and fifty six, and one over one thousand and twenty four, a ratio of four twice. And on y prime equals y, everything is rounded.

@chapter Second order isn't half the error
@math heading="y′ = t²" items="h = 1/4:   Euler 11/96,   improved 1/96@eleven ninety sixths;;8 slope readings:   Euler 23/384,   improved 4/384@eight slope readings"
At a quarter, Euler's error is eleven ninety sixths, and the improved method's is one ninety sixth: eleven times smaller, not half. For the same work, eight slope readings each, Euler has twenty three over three hundred and eighty four, and the improved method four. Nearly six times smaller, and the gap grows as the step shrinks.

@chapter Where people slip
@list heading="Common slips" items="Thinking second order means half the error@The first|Keeping the trial value as the answer@The second|Expecting the ratio to be 4 on every equation@the third"
The first slip is thinking second order means half the error. Order is about how the error changes with h. The second is keeping the trial value as the answer. On y prime equals y, the trial value is five quarters, and the kept value is forty one thirty seconds. And the third is expecting a ratio of exactly four on every equation.

@chapter Try it
@words text="y′ = t²:  improved, then Euler" sub="switch the Method menu"
Your turn. In the lab, run the improved method on y prime equals t squared, then switch the method menu to Euler. Watch one ninety sixth become eleven ninety sixths, and compare how each column falls as the step halves.

@end text="Two slopes, a quarter of the error"
You can run both methods side by side and read the exact ratios, on Learn. That's learn dot get er done dot I O.
