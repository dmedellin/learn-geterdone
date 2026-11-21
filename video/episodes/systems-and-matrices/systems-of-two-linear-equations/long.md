---
format: long
lesson: systems-and-matrices/systems-of-two-linear-equations
title: Two lines, three possible answers
thumb: Once, never, or everywhere
---

@chapter The question
@title text="Systems of Two Linear Equations" sub="Systems and Matrices" art=thumb
Two equations, two unknowns. Before you solve anything, there's a question worth asking: how many answers could there be? It turns out there are only three possibilities.

@words text="2x + y = 4" sub="on its own: infinitely many solutions"
On its own, two x plus y equals four has infinitely many solutions, one for every value of x. A system puts two equations together and asks for the pairs they have in common.

@math heading="A solution" items="ax + by = c@a x plus b y;;(x, y) satisfies every equation@satisfies every"
A linear equation can be written a x plus b y equals c, with a and b not both zero. A solution of the system is an ordered pair that satisfies every equation in it. Satisfying one of them isn't partial credit. It isn't a solution at all.

@art one-crossing
Each equation's graph is a line. So the solution set is the set of points lying on both lines: the intersection, never the union. And how many solutions becomes a picture question. How do two lines meet?

@chapter Three cases
@art three-cases
Two lines in the plane share exactly one point, no point, or every point. There's no other count. In particular, no system of two linear equations has exactly two solutions.

@art two-points
Here's why. Suppose two lines share two different points. There's exactly one line through two points, so the two lines are the same line, and they share everything. More than one shared point means all of them.

@list heading="The names" items="One solution: consistent, independent@exactly one|No solution: inconsistent@has none|Infinitely many: consistent, dependent@the same line"
The cases have names. A system with at least one solution is consistent, and with exactly one it's also independent. A system that has none is inconsistent. And a consistent system whose equations describe the same line is dependent.

@chapter Telling them apart
@math heading="Compare the slopes" items="2x − y = 1  →  y = 2x − 1@two x minus y;;x + y = 5  →  y = −x + 5@x plus y equals five;;slopes 2 and −1 differ  →  one solution@the slopes differ"
You don't need to draw. Put both equations in slope intercept form. Two x minus y equals one becomes y equals two x minus one, slope two. And x plus y equals five becomes y equals minus x plus five, slope minus one. The slopes differ, so the lines cross once.

@math heading="Find it, then check it" items="2x − 1 = −x + 5@set them equal;;3x = 6  →  x = 2,  y = 3@three x equals six;;4 − 3 = 1 ✓    2 + 3 = 5 ✓@check it in both"
To find the crossing, set them equal: two x minus one equals minus x plus five. Three x equals six, so x is two and y is three. Then check it in both: four minus three is one, and two plus three is five.

@art parallel
Equal slopes mean you're in one of the other two cases, and the intercepts decide which.

@math heading="Same slope, different intercept" items="2x + 3y = 6  →  y = −(2/3)x + 2@two x plus three y equals six;;4x + 6y = 7  →  y = −(2/3)x + 7/6@four x plus six y;;parallel and distinct  →  no solution@no solution"
Two x plus three y equals six gives slope minus two thirds and intercept two. Four x plus six y equals seven gives the same slope, with intercept seven sixths. Parallel and distinct, so no solution, and that's a complete answer.

@words text="x = 3" sub="vertical: no slope to compare"
One warning. A vertical line like x equals three has no slope. In standard form, ask instead whether one equation's two coefficients are a common multiple of the other's.

@chapter The same line, twice
@math heading="Dependent" items="x − 2y = 4@x minus two y equals four;;−3x + 6y = −12   (−3 × the first)@minus three times;;{(x, y) : x − 2y = 4}@the whole line"
Now take x minus two y equals four, with minus three x plus six y equals minus twelve. The second is minus three times the first, so every pair that fits one fits the other. The solution set is the whole line.

@art same-line
But infinitely many is not the same as all pairs. Zero, zero fails both equations, and so does most of the plane. The answer is a line, and you describe it: as x minus two y equals four, or in parameter form, two t plus four, t.

@chapter Check both
@art near-miss
A graph names the case. It doesn't give the answer. Two x plus y equals four and x minus y equals one cross at five thirds, two thirds. A careful drawing puts that near one point seven, zero point seven, and no drawing tells five thirds from one point seven.

@list heading="Common slips" items="Reporting x and stopping@The first|Checking in one equation only@The second|Calling a dependent solution set everything@the third"
The first slip is reporting x and stopping. A solution is a pair. The second is checking in one equation only: the one you used last will check out however badly things went. And the third is calling a dependent system's solution set everything.

@chapter Try it
@words text="x = 3  and  2x + y = 7" sub="then change the second to 2x = 8"
Your turn. Classify x equals three with two x plus y equals seven. Don't force a slope comparison. Substitute the fixed x into the other equation, finish the pair, and check it in both. Then change the second equation to two x equals eight, and explain the new classification before solving.

@end text="Move the coefficients, watch the lines"
You can move the coefficients and watch the crossing point leave the plane, on Learn. That's learn dot get er done dot I O.
