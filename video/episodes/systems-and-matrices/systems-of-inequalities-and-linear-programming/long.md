---
format: long
lesson: systems-and-matrices/systems-of-inequalities-and-linear-programming
title: Linear programming: why the best point is a corner
thumb: Check the corners
---

@chapter The question
@title text="Inequalities and Linear Programming" sub="Systems and Matrices" art=thumb
Infinitely many points can satisfy a system of inequalities. Linear programming asks which one of them is best. The surprising part is that you only need to check a handful.

@art half-plane
A linear inequality in two variables is satisfied by a half-plane: everything on one side of the line a x plus b y equals c. The line is included for less than or equal, or greater than or equal, and left out for strict inequalities.

@math heading="One test point" items="x + y ≤ 8:    0 ≤ 8    true  →  shade the origin side@For x plus y;;2x + y ≤ 10:    0 ≤ 10    true  →  shade the origin side@two x plus y;;2x − 3y ≥ 6:    0 ≥ 6    false  →  shade the other side@two x minus three y"
To shade, substitute a test point off the line, usually the origin. For x plus y at most eight, zero is at most eight. True, so shade the origin side. The same goes for two x plus y at most ten. But two x minus three y at least six gives zero at least six, false, so shade the other side.

@chapter The feasible region
@art feasible-polygon
The feasible region is where every inequality holds at once, the intersection of the half-planes. Take x and y at least zero, x plus y at most eight, and two x plus y at most ten. The first two keep you in the first quadrant, and the other two cut it down to four sides.

@math heading="Maximise P = 5x + 4y" items="x = 0,    y = 0,    x + y = 8,    2x + y = 10@four boundary lines;;six crossings to check@six places"
Now ask a question: maximise P equals five x plus four y on that region. Four constraints give four boundary lines, and four lines cross in six places.

@chapter The corner point theorem
@art sliding-line
Why corners? The points where five x plus four y equals some value k form a line. Raise k, and the line slides across the plane. The largest k that still touches the region is where the line is about to leave, and a straight line leaves a polygon through a corner.

@words text="the optimum is at a corner" sub="nonempty, closed, bounded region · linear objective"
That's the corner point theorem. On a nonempty, closed, bounded region, a linear objective reaches its maximum and its minimum at corners. If two corners tie, the whole edge between them is optimal too.

@chapter Finding the corners
@math heading="Solve boundaries in pairs" items="(2x + y = 10)  −  (x + y = 8)   →   x = 2@two x plus y equals ten;;2 + y = 8   →   y = 6        (2, 6)@two plus y"
Each corner is two boundary lines solved together. For the slanted pair, subtract: two x plus y equals ten, minus x plus y equals eight, leaves x equals two. Then two plus y equals eight, so y is six.

@math heading="Test every crossing" items="(0, 0),   (5, 0),   (2, 6),   (0, 8)    feasible@are feasible;;(8, 0):    2x + y = 16 > 10    out@eight, zero;;(0, 10):    x + y = 10 > 8    out@zero, ten"
Then test each crossing against every other constraint. Zero, zero; five, zero; two, six; and zero, eight are feasible. But eight, zero gives two x plus y equals sixteen, more than ten. And zero, ten gives x plus y equals ten, more than eight. Both are out.

@art fake-corner
Those two are crossings of boundary lines, but not corners of the region. A crossing has to survive every other constraint as well.

@chapter Evaluate
@math heading="P = 5x + 4y at each corner" items="(0, 0):    P = 0@P is zero;;(5, 0):    P = 25@twenty five;;(2, 6):    P = 10 + 24 = 34    maximum@thirty four;;(0, 8):    P = 32@thirty two"
At zero, zero, P is zero. At five, zero, it's twenty five. At two, six, ten plus twenty four, thirty four. At zero, eight, thirty two. The maximum is thirty four, at x equals two and y equals six. Report the point as well as the value.

@words text="P = 40 at (8, 0) and (0, 10)" sub="larger, and not allowed"
Here's why the test mattered. Both rejected crossings give P equals forty, bigger than the true maximum. Leave one in and it doesn't sit there harmlessly. It wins, and your answer breaks a constraint.

@chapter Where it breaks
@art curved-objective
The method needs a linear objective. On the same region, P equals x times y is largest at two and a half, five, which isn't a corner of anything.

@art unbounded-region
And the theorem needs a bounded region. With x and y at least zero and x plus y at least four, C equals two x plus three y has a minimum of eight, at four, zero. But there's no maximum: along four plus t, zero, C is eight plus two t, growing without bound.

@list heading="Common slips" items="Treating every crossing as a corner@The first|Losing the inequality's direction@The second|Looking for the optimum inside@The third"
The first slip is treating every crossing as a corner. The second is losing the inequality's direction while solving for y: dividing by minus one reverses it, so it's safer to draw the boundary and test a point. The third is looking for the optimum inside the region.

@chapter Try it
@words text="Minimise C = 2x + 7y" sub="same four constraints"
Your turn. Keep the same four constraints, but minimise C equals two x plus seven y. The corners are already known, so build a fresh table of values. Name the winning point and value, and explain why the corner comparison is conclusive here.

@end text="Slide the objective line"
You can test the corners and slide the objective line yourself, on Learn. That's learn dot get er done dot I O.
