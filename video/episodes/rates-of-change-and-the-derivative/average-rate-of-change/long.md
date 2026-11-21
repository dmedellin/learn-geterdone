---
format: long
lesson: rates-of-change-and-the-derivative/average-rate-of-change
title: Average rate of change: a difference over a step
thumb: The slope of a secant
---

@chapter The question
@title text="Average Rate of Change" sub="Rates of Change and the Derivative" art=thumb
How fast did something change between two moments? It sounds like a job for a speedometer. In fact it's a subtraction, followed by a division.

@art difference-and-step
Take a function f, a starting input a, and a step h. Over that step, the input changes by h. The output changes by f of a plus h, minus f of a. The average rate is the second, divided by the first.

@math heading="Average rate of change" items="(f(a + h) − f(a)) / h@f of a plus h;;h ≠ 0@as long as"
In symbols, it's f of a plus h, minus f of a, all over h, as long as h isn't zero. It has another name too, the difference quotient: a difference on top, divided by the step.

@chapter It's a slope
@art secant-line
Plot the two points, a, f of a, and a plus h, f of a plus h. The straight line through them is called a secant. Its slope is rise over run, and that's exactly the quotient. So an average rate is a slope you could draw, and everything you know about slopes applies to it.

@chapter Three steps on t squared
@math heading="f(t) = t²,  a = 1" items="h = 1:  (4 − 1)/1 = 3@a step of one;;h = 1/2:  (9/4 − 1)/(1/2) = 5/2@Halve the step;;h = 1/4:  (25/16 − 1)/(1/4) = 9/4@Halve it again"
Take t squared, starting at one, so the starting output is one. With a step of one, the output goes from one to four, so the rate is three. Halve the step. The output at three halves is nine quarters, the change is five quarters, and dividing by a half gives five halves. Halve it again, and you get nine quarters.

@art shrinking-secants
Three, then five halves, then nine quarters. The rates aren't the same. The function didn't change. The step did. Each number is the slope of a different secant, all through the same point, one, one.

@chapter The pattern
@words text="3 = 2 + 1   5/2 = 2 + 1/2   9/4 = 2 + 1/4" sub="each rate is 2 plus the step"
Now write those rates as two plus one, two plus a half, and two plus a quarter. Each one is two plus the step. And that's not a coincidence of three numbers.

@math heading="Why" items="(1 + h)² = 1 + 2h + h²@one plus h, squared;;change = 2h + h²@the change;;rate = 2 + h@Dividing by h"
Here's why. One plus h, squared, is one plus two h plus h squared. Take away the starting value of one, and the change is two h plus h squared. Dividing by h gives two plus h. For t squared at one, the secant slope is two plus h, for every step that isn't zero.

@chapter A cubic
@math heading="f(t) = t³ − t,  a = 2" items="f(2) = 6@f of two is six;;h = 1:  (24 − 6)/1 = 18@a step of one;;h = 1/2:  (105/8 − 6)/(1/2) = 57/4 = 14.25@a step of a half"
It happens on a cubic too. Take t cubed minus t, starting at two, where f of two is six. A step of one gives twenty four minus six, so eighteen. A step of a half gives one hundred and five eighths, a change of fifty seven eighths, and a rate of fifty seven quarters, or fourteen point two five.

@chapter When the step doesn't matter
@art straight-line-secants
Now try three t plus one, at five. The output at five is sixteen, and at five plus h it's sixteen plus three h. So the change is three h, and the quotient is three. It's three for a step of one, for a step of a half, for every step at all.

@art steep-and-flat
A function whose average rate doesn't depend on the step is exactly a line, and the rate is its slope. A curve is the opposite case. Change the step, and you get a different secant, with a different slope.

@chapter Where people slip
@list heading="Two ways to lose the rate" items="No subtraction:  (9/4)/(1/2) = 9/2@leaving out the subtraction|No division:  9/4 − 1 = 5/4@leaving out the division|The rate:  5/2@The real rate"
The first slip is leaving out the subtraction. For t squared at one, with a step of a half, nine quarters over a half gives nine halves. The second is leaving out the division, which gives five quarters. The real rate is five halves.

@art falling-secant
And always say which interval a rate belongs to, because a curve has no single one. If a rate comes out negative, that's not a mistake either. It means the output fell, just as a falling line has a negative slope.

@chapter Try it
@words text="f(t) = t²,  a = 2" sub="((2 + h)² − 4) / h"
Your turn. Take t squared again, but start at two. Work out the rate for a step of one by hand. Then simplify the general quotient, two plus h, squared, minus four, all over h, and compare it with what the lab prints.

@end text="Halve the step, watch the rate"
You can type a function, halve the step, and see every rate as an exact fraction, on Learn. That's learn dot get er done dot I O.
