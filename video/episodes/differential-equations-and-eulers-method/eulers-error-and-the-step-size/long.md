---
format: long
lesson: differential-equations-and-eulers-method/eulers-error-and-the-step-size
title: Euler's error and the step size: why halving h halves the error
thumb: Every step's miss adds up
---

@chapter Measuring the error
@title text="Euler's Error and the Step Size" sub="Differential Equations and Euler's Method" art=thumb
Euler's method is always a little off. The question for this lesson is how the error shrinks when you shrink the step. The answer has a name: Euler's method is first order.

@art fixed-end
To compare step sizes fairly, fix an end time, say T equals one, and measure the error there. A smaller step takes more steps to arrive. The lab runs three step sizes, h, h over two and h over four, all to the same end.

@math heading="The error at T" items="E(h) = |y_N − y(T)|@The error E of h;;N = (T − t₀)/h@N steps"
The error E of h is the distance between Euler's last value and the true value at T, where it takes N steps of size h to get there.

@chapter Exactly h
@math heading="y′ = 2t,  y(0) = 0,  exact y = t²" items="h = 1/4:   y₄ = 3/4,   E = 1/4@a step of a quarter;;h = 1/8:   y₈ = 7/8,   E = 1/8@With an eighth;;h = 1/16:   y₁₆ = 15/16,   E = 1/16@With a sixteenth;;ratios:  2,  2@both ratios"
On y prime equals two t, the true value at one is one. With a step of a quarter, Euler reaches three quarters, an error of a quarter. With an eighth, seven eighths, an error of an eighth. With a sixteenth, an error of a sixteenth. So both ratios are exactly two.

@words text="E(h) = h,  exactly"
On this equation, the error is exactly h. That's not an approximation. Here's where it comes from.

@chapter One step at a time
@math heading="One step from (t, t²)" items="true rise:  (t + h)² − t² = 2th + h²@The true solution rises;;Euler's rise:  h·2t = 2th@Euler's step rises;;miss:  h²@misses by"
Look at one step. The true solution rises from t squared to t plus h, squared: two t h plus h squared. Euler's step rises by h times two t. So each step misses by h squared, whatever t is.

@art step-miss
A tiny miss on each step. With a step of a quarter, each step misses by one sixteenth.

@art pieces-add
But there are one over h steps. So the total is one over h, times h squared, which is h. At a quarter, four misses of a sixteenth add up to a quarter. The error isn't the last step's miss. It's every step's, accumulated.

@art quarter-pieces
Now halve h. Each piece shrinks to a quarter of its size, but there are twice as many of them. A quarter times two is a half, so the total halves.

@chapter First order
@words text="E(h) ≈ C·h" sub="halve h, halve the error: first order"
In general, for a right side with continuous first derivatives, Euler's error at a fixed T is about C times h. Halving h halves the error, and the ratio heads for two. That's first order. The lab demonstrates it on chosen equations, and doesn't prove it for every one.

@art ratio-two
Two errors side by side, the second half the first: a ratio of two.

@math heading="order = log₂ of the ratio" items="ratio near 2:  error ≈ C·h@near two;;ratio near 4:  error ≈ C·h²@near four"
The order is the power, the log base two of the ratio. A ratio near two means an error like h. A ratio near four would mean h squared. The lab forms two ratios from three errors, so one can check the other.

@chapter When the ratio only approaches two
@math heading="y′ = t²,  exact y = t³/3" items="errors:  11/96,  23/384,  47/1536@the errors;;ratios:  44/23 ≈ 1.91304,  92/47 ≈ 1.95745@The ratios;;error = h/2 − h²/6@h over two"
On y prime equals t squared, the errors are eleven ninety sixths, twenty three over three hundred and eighty four, and forty seven over one thousand five hundred and thirty six. The ratios are about one point nine one and one point nine six. The error is exactly h over two minus h squared over six.

@art approaching-two
The first term halves exactly. The second falls four times faster, so its effect fades, and the ratio stays below two while it climbs toward it. And on y prime equals y, the true value is e, so every error and ratio is printed rounded.

@chapter Where people slip
@list heading="Common slips" items="Taking the error to be the last step's@The first|Expecting every ratio to be exactly 2@The second|Naming the order from one error@the third"
The first slip is taking the error to be the last step's miss. On two t with a quarter, the last step misses by a sixteenth, and the error is a quarter. The second is expecting every ratio to be exactly two. And the third is naming the order from a single error. It takes at least two errors, and their ratio.

@chapter Try it
@words text="y′ = 2t,  h = 1/10"
Your turn. Run a step of a tenth through the same formula. How many steps reach one, how much does each one miss, and what's the total?

@end text="Halve the step, halve the error"
You can run three step sizes and read the exact ratios yourself, on Learn. That's learn dot get er done dot I O.
