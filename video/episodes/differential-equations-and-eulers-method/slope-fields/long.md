---
format: long
lesson: differential-equations-and-eulers-method/slope-fields
title: Slope fields: draw a differential equation before you solve it
thumb: A slope at every point
---

@chapter A slope everywhere
@title text="Slope Fields" sub="Differential Equations and Euler's Method" art=thumb
An equation like y prime equals t minus y gives you a slope at every point of the plane. That's all the information it has. Draw it, and the equation becomes a picture, before you've solved anything.

@art slope-field-grid
At each point of a grid, draw a short segment with the slope the equation gives there. The collection of segments is called a slope field. A solution is a curve whose slope, at each of its points, matches the field. So the equation is a statement about slopes, before it's a statement about functions.

@chapter Computing a slope
@math heading="y′ = t − y" items="(2, 0):   2 − 0 = 2    rising@two, zero;;(1, 1):   1 − 1 = 0    flat@one, one;;(0, 2):   0 − 2 = −2    falling@zero, two"
Take y prime equals t minus y. At two, zero, the slope is two minus zero, two, so the segment rises two for every one across. At one, one, it's zero: flat. At zero, two, it's minus two, falling steeply.

@art three-segments
Three substitutions, three segments. There's no limit and no approximation. A grid of fifteen by fifteen is just that arithmetic, repeated, and the lab prints each slope exactly.

@chapter The nullcline
@math heading="where the slope is 0" items="t − y = 0@t minus y equals zero;;y = t@so y equals t"
Now ask where the slope is zero. Set t minus y equals zero, so y equals t. That line is called the nullcline. Every point on it, like one, one, or minus two, minus two, has a flat segment. The lab prints it in the tile named slope zero.

@art nullcline-line
Above the line, y is bigger than t, so the slope is negative. Below it, the slope is positive. The three points from before straddle it: two, zero is below with a positive slope, zero, two is above with a negative one, and one, one sits on it.

@words text="every solution crosses y = t horizontally"
So every solution crosses that line horizontally. That's a fact about the whole family, read from one equation.

@chapter Fields of one variable
@art rows-parallel
Two special cases have very regular pictures. For y prime equals y, the slope depends on y alone. At zero, one, it's one, and it's one at every point at height one. So each row is parallel copies, steeper the further the row is from the axis. The nullcline is the line y equals zero.

@art columns-parallel
For y prime equals two t, the slope depends on t alone, so every column is identical. The solutions, t squared plus C, are vertical shifts of one another. The nullcline is the line t equals zero, and the lab prints none in y, because no height makes the slope zero for every t.

@chapter Reading a segment
@art tangent-not-path
At two, zero, the segment has slope two. That says a solution through two, zero is rising there at a rate of two. It doesn't say the solution goes on to three, two. By then it's at a different point, with a different slope, and the curve has bent.

@words text="a segment is a tangent" sub="the direction of travel at that instant"
A segment is a tangent: the direction of travel at that instant, not a path. Joining segments end to end is Euler's method, and that's only approximate. Later lessons measure exactly how far off it gets.

@words text="the slope tile is exact" sub="the drawing is floating point"
One more thing about the drawing. The segments and any curve are plotted with floating point numbers. The slope tile is computed exactly. If a number matters, read it from the tile.

@chapter Where people slip
@list heading="Common slips" items="Reading a segment as where the solution goes@The first|Confusing the slope with the value of y@The second|Expecting the nullcline to be a solution@the third"
The first slip is reading a segment as where the solution goes next. The second is confusing the slope with the value of y. At one, one, the slope is zero and the height is one. And the third is expecting the nullcline to be a solution. A curve that touches y equals t carries on and leaves it.

@chapter Try it
@words text="y′ = t − y  at  (3, 1)"
Your turn. Work out the slope at three, one yourself. Then check it against the preset, and say whether that point is above or below the nullcline.

@end text="Draw the equation before you solve it"
You can draw the slope field of any equation and read each slope exactly, on Learn. That's learn dot get er done dot I O.
