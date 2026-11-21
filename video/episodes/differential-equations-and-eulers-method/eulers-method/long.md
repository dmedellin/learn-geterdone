---
format: long
lesson: differential-equations-and-eulers-method/eulers-method
title: Euler's method: value plus rate times step
thumb: Exact fractions, approximate answer
---

@chapter One sentence
@title text="Euler's Method" sub="Differential Equations and Euler's Method" art=thumb
Euler's method is one sentence: the next value is this value plus the rate times the step. Write it as a formula, repeat it, and you can follow a differential equation forward with nothing but arithmetic.

@math heading="Euler's method" items="tₙ₊₁ = tₙ + h@move t forward;;yₙ₊₁ = yₙ + h·f(tₙ, yₙ)@move y by h times"
Given y prime equals f of t and y, a start, and a step h, you move t forward by h, and move y by h times the slope at the point where you're standing. Then read a new slope, and do it again.

@art one-step
Each step walks along the slope you're standing on, for a time h.

@art euler-polygon
Join the points with straight segments, and you get Euler's polygon. Each segment has the slope the equation gives at its left end.

@chapter Four steps on y prime equals y
@math heading="y′ = y,  y(0) = 1,  h = 1/4" items="y₁ = 1 + (1/4)·1 = 5/4@five quarters;;y₂ = 5/4 + (1/4)·(5/4) = 25/16@twenty five sixteenths;;y₃ = 125/64@one hundred and twenty five;;y₄ = 625/256@six hundred and twenty five"
Take y prime equals y, from one, with a step of a quarter. The first step is one plus a quarter times one: five quarters. The second is five quarters plus a quarter of that: twenty five sixteenths. Then one hundred and twenty five sixty fourths, and then six hundred and twenty five over two hundred and fifty six.

@words text="y₄ = (5/4)⁴ = 625/256 ≈ 2.44" sub="each step multiplies by 1 + h"
Because the slope is the value itself, each step multiplies by one plus h, which is five quarters. So every row is a power of five quarters, a geometric sequence. That's a fact about the recipe.

@chapter How far off it is
@math heading="at t = 1" items="Euler:  625/256 ≈ 2.44141@Euler gives;;true:  e ≈ 2.71828@The true solution;;error ≈ 0.276876@The error"
The true solution is e to the t, so at one it's e, about two point seven one eight. Euler gives about two point four four. The error is about zero point two seven seven, rounded, because e isn't a fraction.

@art growing-shortfall
None of that error is an arithmetic slip. Every step used the slope at its left end, while the real slope kept climbing as y grew. So every step fell a little short, the shortfalls piled up, and the polygon lies below the curve.

@words text="an exact fraction ≠ the exact answer"
So six hundred and twenty five over two hundred and fifty six is the exact value of the method, and a rough value of the solution. Exact arithmetic removes arithmetic error, and leaves the method's error just where it was.

@chapter A rate in t alone
@math heading="y′ = 2t,  y(0) = 0,  h = 1/4" items="slopes:  0,  1/2,  1,  3/2@The slopes;;values:  0,  0,  1/8,  3/8,  3/4@the values;;true:  t² = 1 at t = 1,   error 1/4@The true solution"
Take y prime equals two t, from zero, with steps of a quarter. The slopes are zero, a half, one and three halves, so the values are zero, zero, an eighth, three eighths and three quarters. The true solution, t squared, is one at one, so the error is exactly a quarter.

@art left-sum-staircase
That's the left sum from the integral course: a quarter times zero plus a half plus one plus three halves. Euler's method on an equation without y in it is exactly a left sum.

@chapter A rate that falls, then rises
@math heading="y′ = t − y,  y(0) = 2,  h = 1/2" items="slope −2:   y₁ = 1@minus two;;slope −1/2:   y₂ = 3/4@minus a half;;slope 1/4:   y₃ = 7/8@Then a quarter;;y₄ = 19/16@nineteen sixteenths"
Now y prime equals t minus y, from two, with steps of a half. The first slope is minus two, so y one is one. Then minus a half, giving three quarters. Then a quarter, giving seven eighths, and the fourth step gives nineteen sixteenths.

@art dip-and-turn
The path falls and then turns upward, just as the true solution does. Its true value at two is about one point four zero six, rounded.

@chapter Smaller steps
@art finer-polygon
The tempting fix is more steps. But eight steps of a quarter end at two, a different place. What helps at one is a smaller step. Eight steps of an eighth give about two point five six six, an error of about zero point one five two. Better, and still not zero. No step makes the polygon the solution.

@chapter Where people slip
@list heading="Common slips" items="Expecting the method to give the solution@The first|Calling an exact fraction the exact answer@The second|Reading the slope at the end of the step@the third"
The first slip is expecting the method to give the solution, and more steps to make it exact. The second is calling an exact fraction the exact answer. And the third is reading the slope at the end of the step. That puts the new value on both sides, which is a different method.

@chapter Try it
@words text="y′ = 2y,  y(0) = 1,  h = 1/2" sub="each step multiplies by 1 + 2·(1/2) = 2"
Your turn. Take y prime equals two y, from one, with a step of a half. Each step multiplies by one plus two times a half, which is two. Find y one and y two, and compare with the true value at one, e squared, about seven point three nine.

@end text="Value plus rate times step"
You can step any equation forward in exact fractions, and see the polygon against the curve, on Learn. That's learn dot get er done dot I O.
