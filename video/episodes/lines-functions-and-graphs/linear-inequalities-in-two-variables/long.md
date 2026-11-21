---
format: long
lesson: lines-functions-and-graphs/linear-inequalities-in-two-variables
title: Linear inequalities in two variables: which side do you shade?
thumb: One test point decides
---

@chapter The idea
@title text="Linear Inequalities in Two Variables" sub="Lines, Functions and Graphs" art=thumb
Swap the equals sign in a linear equation for a less than, and something odd happens. The answer stops being a line. It becomes half of the whole plane.

@art half-plane
A linear inequality in two variables looks like A x plus B y is less than C, or less than or equal, or greater, or greater than or equal. Its solutions are still ordered pairs that make it true. There are just so many of them that they fill a region, called a half plane.

@words text="Ax + By = C splits the plane" sub="one side > C · the other side < C"
Here's why that works. The line A x plus B y equals C splits the plane into two regions. Every point on one side makes the left side bigger than C, and every point on the other side makes it smaller. To switch sides, you'd have to cross the line.

@chapter Drawing the region
@list heading="Four steps" items="Graph the boundary: replace the sign with =@graph that line|Solid for ≤ ≥, dashed for < >@solid or dashed|Test one point off the line@Test one point|Shade the side that won@shade that side"
So drawing it takes four steps. Swap the inequality sign for an equals sign, and graph that line. Make it solid or dashed. Test one point off the line, ideally zero, zero. If the test is true, shade that side. If it's false, shade the other.

@art solid-vs-dashed
The line style isn't decoration. Less than or equal and greater than or equal include the line, so it's solid. Strictly less than and strictly greater than leave it out, so it's dashed.

@math heading="2x + 3y ≤ 12" items="boundary through (6, 0) and (0, 4), solid@six, zero;;test (0, 0):  0 ≤ 12  true@zero is less than;;shade the side with the origin@origin"
Take two x plus three y is less than or equal to twelve. The boundary meets the axes at six, zero and zero, four, and it's solid. Testing zero, zero gives zero is less than or equal to twelve. True. So shade the side containing the origin, below and to the left.

@art test-point
One test point settles the whole region, because nothing on that side can switch without crossing the line.

@chapter The symbol doesn't tell you the side
@math heading="4x − 2y > 8" items="−2y > −4x + 8@subtract four x;;y < 2x − 4@divide by minus two;;test (0, 0):  0 > 8  false@Test zero, zero;;test (3, 1):  10 > 8  true@three, one"
It's tempting to read greater than as above. Watch this. Four x minus two y is greater than eight. Subtract four x, then divide by minus two, which flips the sign: y is less than two x minus four. Test zero, zero: is zero greater than eight? False. Test three, one: ten is greater than eight. True.

@art below-line
So the symbol says greater than, and the region is below the line. There's no contradiction. Dividing by a negative reverses an inequality, and that's the one rule from one variable that carries over. A test point gets the right side without any rearranging.

@chapter Two awkward cases
@art origin-on-line
What if the boundary goes through the origin? Take y is less than three x. Zero, zero is on the line, so it can't be your test point. Use any other point. One, zero gives zero is less than three, true, so shade the side containing one, zero, below and to the right.

@math heading="4x − 2y > 8" items="(0, −4):  8 > 8  false@zero, minus four"
And look at zero, minus four in four x minus two y is greater than eight. It gives eight is greater than eight, which is false.

@art edge-point
That point sits exactly on the dashed boundary. It isn't a solution. But change the symbol to greater than or equal, and it would be. One symbol changes the status of every point on the line, and no other point in the plane.

@chapter Where people slip
@list heading="Common slips" items="Forgetting to flip when dividing by a negative@The first|Reading the side off the symbol@The second|A solid line for a strict inequality@the third"
The first slip is forgetting to flip when you divide by a negative. The line still looks right, but the shading is on the wrong side. The second is reading the side off the symbol. And the third is drawing a solid line for a strict inequality.

@chapter Try it
@words text="3x − 2y ≤ 6" sub="boundary given: 3x − 2y = 6"
Try three x minus two y is less than or equal to six. The boundary is given. Decide its line style, find two points on it, test the origin, shade, and confirm with a second point. Then solve for y and use the reversed sign as a second check.

@end text="Shade it yourself"
The full lesson is on Learn. That's learn dot get er done dot I O.
