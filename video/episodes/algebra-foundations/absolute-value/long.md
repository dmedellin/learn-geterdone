---
format: long
lesson: algebra-foundations/absolute-value
title: Absolute value: distance from zero, and why it needs two cases
thumb: Distance has no sign
---

@chapter The question
@title text="Absolute Value" sub="Algebra Foundations" art=thumb
How far is minus seven from zero? Seven. Distance doesn't carry a sign. Absolute value is the operation that measures it, and it needs a definition that works even for a letter whose sign you can't see.

@art distance-zero
The absolute value of a number is its distance from zero, and a distance is never negative. Minus seven and seven are both seven away. But getting that from a formula takes two cases.

@chapter The definition
@math heading="Absolute value" items="|x| = x     when x ≥ 0@at least zero;;|x| = −x     when x < 0@less than zero"
Here it is. The absolute value of x is x, when x is at least zero. And it's minus x, when x is less than zero. At zero, both lines give zero, so it doesn't matter which line zero belongs to.

@math heading="Run it three times" items="|5| = 5@five is at least zero;;|−5| = −(−5) = 5@minus five is less than zero;;|0| = 0@zero uses the first"
Five is at least zero, so the first line applies, and the answer is five. Minus five is less than zero, so the second line applies: minus, minus five, which is five. And zero uses the first line, giving zero.

@art flip-arrow
That middle case is the whole lesson. The second line doesn't say the answer is negative. Minus x means the inverse of x, and when x is negative, its inverse is positive. So an absolute value is never negative, and it's zero only when x is zero.

@chapter Distance between two numbers
@art distance-between
The distance between a and b is the absolute value of a minus b. It doesn't matter which end you subtract from, because b minus a is the inverse of a minus b, and the two have the same absolute value.

@math items="|3 − 10| = |−7| = 7@three minus ten;;|10 − 3| = |7| = 7@ten minus three;;|−2 − 5| = |−7| = 7@minus two and five"
Three minus ten is minus seven, so the distance is seven. Ten minus three is seven, so it's seven. And minus two and five are seven apart too.

@chapter Equations
@art two-points
Now read an equation. The absolute value of x minus a equals c means x is at distance c from a. On a line, that's two points when c is positive, one when c is zero, and none when c is negative.

@math items="|x| = 3   →   x = 3 or x = −3@two solutions;;|x| = 0   →   x = 0@one solution;;|x| = −1   →   no solution@no solution"
So the absolute value of x equals three has two solutions, three and minus three. Equals zero has one solution. And equals minus one has no solution, because an absolute value is never negative. No solution is a complete answer.

@chapter Solving it two ways
@math heading="|x − 4| = 3, by distance" items="3 to the left:   4 − 3 = 1@to the left;;3 to the right:   4 + 3 = 7@to the right"
Here's the worked example: the absolute value of x minus four equals three. Read as a distance, it asks for the points three away from four. Three to the left is one. Three to the right is seven.

@math heading="|x − 4| = 3, by the definition" items="x − 4 ≥ 0:   x − 4 = 3   →   x = 7@if x minus four;;x − 4 < 0:   −(x − 4) = 3   →   x = 1@if it's negative;;check:   |7 − 4| = 3,   |1 − 4| = 3@check both"
Through the definition, split into two cases. If x minus four is at least zero, then x minus four is three, and x is seven. If it's negative, then minus, x minus four, is three, and x is one. Check both, and both give three.

@art case-fork
The checks confirm that one and seven work. But the split is what says there's nothing else. Every real number makes x minus four either negative or not, so the two cases cover all of them.

@words text="|x + 4| = 3   →   x = −7 or −1" sub="the centre is −4"
Now try the absolute value of x plus four equals three. That's x minus, minus four, so the centre is minus four, and the points are minus seven and minus one. The sign inside flips the centre, not the distance.

@chapter Where people slip
@list heading="Common slips" items="Reading −x as a negative answer@reading minus x|Keeping only the positive solution@keeping only|Splitting the bars over a sum@splitting the bars"
Three slips. Reading minus x in the definition as a negative answer. Keeping only the positive solution, which loses half the answer every time. And splitting the bars over a sum.

@art triangle-sum
That last one looks plausible because products do split. The absolute value of a b is the absolute value of a times that of b. But sums don't. At three and minus five, the absolute value of the sum is two, while the sum of the absolute values is eight.

@chapter Try it
@words text="a = −6,   b = 1" sub="|a|, and the distance from a to b"
Try it with a equals minus six and b equals one. Which line of the definition fires for a? And how far apart are a and b? You should get six, and seven. If you got five, you subtracted sizes instead of measuring between the points.

@end text="Both cases, and the equation"
You can set the numbers, watch which case fires, and solve the equation, on Learn. That's learn dot get er done dot I O.
