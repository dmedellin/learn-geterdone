---
format: long
lesson: exponential-and-logarithmic-functions/logarithmic-functions-and-their-graphs
title: Graphing logarithms: one reflection explains everything
thumb: The exponential, in a mirror
---

@chapter The inverse of b to the x
@title text="Logarithmic Functions and Their Graphs" sub="Exponential and Logarithmic Functions" art=thumb
You don't need to memorise the graph of a logarithm. Log base b of x is the inverse of b to the x, so its graph is that exponential curve reflected in the line y equals x. Everything else follows from the reflection.

@art mirror-pair
A function has an inverse when it never repeats a value. b to the x is strictly increasing when b is above one, and strictly decreasing when it's between zero and one. So it never repeats, and it has an inverse with no restriction on its domain. That inverse is the logarithm.

@math heading="An inverse pair" items="log_b(bˣ) = x    for every real x@for every real x;;b^(log_b x) = x    for every x > 0@for every positive x"
Log base b of b to the x is x, for every real x. And b to the log base b of x is x, for every positive x.

@chapter Swap the coordinates
@math heading="y = 2ˣ    ⟷    y = log₂(x)" items="(−3, 1/8)    ⟷    (1/8, −3)@minus three;;(0, 1)    ⟷    (1, 0)@Zero, one;;(1, 2)    ⟷    (2, 1)@One, two;;(3, 8)    ⟷    (8, 3)@three, eight"
Reflecting in y equals x swaps the coordinates. Two to the x passes through minus three, one eighth, so log base two passes through one eighth, minus three. Zero, one becomes one, zero. One, two becomes two, one. And three, eight becomes eight, three. One set of pairs, read in two directions.

@art point-swap
If p, q is on the exponential, then q, p is on the logarithm. So domain and range trade places. b to the x accepts every real number and returns only positive ones. The logarithm accepts only positive numbers, and returns every real one.

@chapter What to read off
@list heading="Read off the graph" items="domain   x > 0@The domain|range:   every real number@The range|through (1, 0)@one, zero|through (b, 1)@b, one|no vertical intercept@no vertical intercept|direction from the base@the direction"
The domain is x greater than zero. The range is every real number. Every log curve passes through one, zero, since b to the zero is one. It passes through b, one, which tells bases apart. There's no vertical intercept. And the direction comes from the base: rising for b above one, falling below one.

@art vertical-asymptote
The asymptote turns through a right angle. b to the x flattens toward the horizontal line y equals zero. Reflect that line in y equals x and you get the vertical line x equals zero. The log curve plunges without bound as x comes down toward zero from the right.

@chapter Slow, but unbounded
@math heading="log₁₀(x)" items="x:    1,   10,   100,   1000,   10⁶,   10¹⁰⁰@one, ten;;log₁₀(x):    0,   1,   2,   3,   6,   100@zero, one, two"
To lift log base ten by one, you multiply x by ten. At one, ten, a hundred, a thousand, a million and ten to the hundred, the outputs are zero, one, two, three, six and a hundred.

@art slow-climb
So the output crawls while the input explodes. But there's no height it fails to reach eventually. That's why a log curve looks flat on any wide drawing. Flat isn't level, and slow isn't bounded.

@chapter Shifts move the asymptote
@math heading="y = log₃(x − 5)" items="x − 5 > 0    →    x > 5@greater than zero;;asymptote    x = 5@The asymptote;;(6, 0):    x − 5 = 1@six, zero;;(8, 1):    x − 5 = 3@eight, one"
Take log base three of x minus five. The argument must be positive, so x minus five is greater than zero, and the domain is x greater than five. The asymptote is the vertical line x equals five. The curve passes through six, zero, where x minus five is one, and through eight, one, where x minus five is three.

@art shifted-log
It's the standard shape, moved five to the right, and the asymptote went with it. This is the commonest source of a wrong domain in the course, because the shift is invisible unless you look inside the brackets. The rule is that the argument is positive, not that x is.

@chapter Where people slip
@list heading="Common slips" items="Giving log(x − 5) the domain x > 0@The first|Expecting the curve to level off@The second|Reflecting in the wrong line@The third"
The first is giving a shifted log the domain x greater than zero. Solve argument greater than zero instead. The second is expecting the curve to level off. Log base ten needs an input of ten to the hundred to reach a hundred, but it gets there. The third is reflecting in the wrong line.

@art wrong-mirrors
Reflect b to the x in the horizontal axis and you get minus b to the x. Reflect it in the vertical axis and you get b to the minus x. Neither is a logarithm, and neither has a vertical asymptote. The inverse is the reflection in y equals x.

@chapter Try it
@words text="g(x) = log₄(x + 3)" sub="first line:    x + 3 > 0"
Your turn. Sketch log base four of x plus three. The first line is given: x plus three is greater than zero. Finish the domain, draw the asymptote, move the anchor inputs one, four and one quarter through the shift, and state the direction. Check each point by turning it back into an exponential equation.

@end text="Two curves and the mirror"
You can move a point on one curve and watch its mirror move on the other, on Learn. That's learn dot get er done dot I O.
