---
format: long
lesson: rates-of-change-and-the-derivative/the-derivative-at-a-point
title: The derivative at a point, and the tangent line it gives you
thumb: The best straight-line estimate
---

@chapter The number at the point
@title text="The Derivative at a Point" sub="Rates of Change and the Derivative" art=thumb
Last lesson, the quotients for t squared at one headed for one number. That number has a name. It's the derivative at a point, and it comes with a line you can actually use.

@math heading="The derivative at a" items="f′(a):  what (f(a + h) − f(a))/h approaches as h → 0@f prime of a"
The derivative of f at a is the number the difference quotients approach as h goes to zero. You write it f prime of a. It's one number for each place, not a family of them.

@chapter The tangent line
@art secants-become-tangent
As the step shrinks, the secant lines through the point settle onto one line. That line goes through a, f of a, with slope f prime of a. It's the tangent line.

@math heading="Tangent line at a" items="y = f(a) + f′(a)·(t − a)@y equals"
Its equation is y equals f of a, plus f prime of a times t minus a. The height gives the starting point, and the slope gives the rate.

@chapter t squared at two
@math heading="f(t) = t²,  a = 2" items="((2 + h)² − 4)/h = 4 + h@four plus h;;f′(2) = 4@the constant term;;y = 4 + 4·(t − 2) = 4t − 4@the tangent line"
Take t squared at two. The quotient is four plus h, so the derivative is the constant term, four. The point is two, four, and the tangent line is y equals four plus four times t minus two, which simplifies to y equals four t minus four.

@chapter Using the line
@math heading="A tenth to the right" items="line at 21/10:  4·(21/10) − 4 = 22/5 = 440/100@The line gives;;function at 21/10:  (21/10)² = 441/100@The function gives;;error:  1/100@short by"
Now move a tenth to the right, to twenty one tenths. The line gives twenty two fifths, which is four hundred and forty hundredths. The function gives four hundred and forty one hundredths. So the estimate is short by one hundredth.

@art estimate-gap
That error is exactly h squared, and that's no accident. The function at two plus h is four plus four h plus h squared. The line is four plus four h. The difference is the h squared term that the line leaves out.

@art error-shrinks
Halve the step to one twentieth, and the error is one four hundredth. That's a quarter of it, not a half. The estimate gets better faster than the step gets smaller, and that's the whole reason a derivative is useful.

@chapter Two more functions
@math heading="f(t) = t³,  a = 1" items="f′(1) = 3,  y = 3t − 2@three t minus two;;h = 1/10:  line 13/10,  function 1331/1000@At a tenth;;error:  31/1000 = 3h² + h³@The error"
For t cubed at one, the slope is three, and the tangent is y equals three t minus two. At a tenth, the line gives thirteen tenths, and the function gives one thousand three hundred and thirty one thousandths. The error, thirty one thousandths, is three h squared plus h cubed.

@art curve-above-tangent
For one over t at one, the lab reports a slope of minus one, and the next lesson derives it. The tangent is y equals minus t plus two. Half a unit along, the line gives a half, and the function gives two thirds. The line is too low, because one over t bends upward, away from it.

@chapter Touching is the wrong picture
@art tangent-line
You've probably heard a tangent described as a line that touches the graph at one point. That's true for a circle, and misleading here. The tangent to t squared at two does meet the parabola only once, but that isn't what defines it. The slope does.

@chapter Where people slip
@list heading="Common slips" items="“It only touches, so it says nothing nearby”@The first|Using the tangent far from its point@The second|Mixing up the slope and the height@The third"
Three slips. The first is thinking a line that touches once says nothing about nearby values. The second is using the tangent far from its point. The third is mixing up the slope with the height.

@art far-from-point
The error grows as you move away. For t squared at two, it's one at a step of one, and a hundred at a step of ten. And f prime of two and f of two are both four only by coincidence. For t cubed at one, the slope is three and the height is one.

@chapter Try it
@words text="t² at 3,  used at t = 31/10" sub="slope 6 · estimate 9 + 6/10 = 48/5"
Your turn. Find the tangent to t squared at three, and use it at thirty one tenths. The slope is six, and the estimate is nine plus six tenths, forty eight fifths. Work out the error, and check that it's h squared again.

@end text="Watch the tangent's error"
You can move along the tangent and see its error printed as an exact fraction, on Learn. That's learn dot get er done dot I O.
