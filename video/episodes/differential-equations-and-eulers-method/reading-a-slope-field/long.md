---
format: long
lesson: differential-equations-and-eulers-method/reading-a-slope-field
title: Reading a slope field: what it settles and what it suggests
thumb: Settled, or only suggested?
---

@chapter Three levels of confidence
@title text="Reading a Slope Field" sub="Differential Equations and Euler's Method" art=thumb
A slope field can tell you a lot about solutions you never write down. But not everything it shows is equally certain. Some things the arithmetic settles. Some things the picture only suggests. Reading well means keeping them apart.

@art logistic-field
Take y prime equals y times one minus y. The right side is a product, and a product is zero when either factor is. So the slope is zero exactly where y is zero or one, at every t.

@chapter Horizontal solutions
@words text="y = 0  and  y = 1" sub="horizontal solutions"
That makes both lines horizontal solutions. A constant function has derivative zero, and the equation says its slope should be zero there, so it fits. The lab lists them in the tile named horizontal solutions.

@list heading="The sign of y·(1 − y)" items="y < 0:   falling@Below zero|0 < y < 1:   rising@Between zero and one|y > 1:   falling@Above one"
Between and outside the lines, the sign of the slope is fixed. Below zero, y is negative and one minus y is positive, so the slope is negative. Between zero and one, both factors are positive, so the curve rises. Above one, one minus y is negative, and it falls again. All of that is arithmetic, so it's settled.

@chapter Curves don't cross
@art no-crossing
Now start a solution at a half. The slope there is a half times a half, a quarter, so it rises. Could it cross the line y equals one? Not at an angle. The field gives one slope at each point, so two solutions can't pass through one point with two slopes.

@art walls
But a curve that reached one would arrive flat, with the same slope, zero. Ruling that out takes one more fact: through each point there's exactly one solution, and the horizontal line is already it. So a curve that starts below one stays below it for ever, and by the same argument, above zero.

@words text="uniqueness: stated, used, not proved"
That uniqueness claim holds for every polynomial right side. This course states it and uses it, but doesn't prove it. It's what turns a horizontal solution into a wall, not just a line of flat segments.

@chapter What the picture only suggests
@art solid-then-dashed
The curve from a half seems to level off at one. The field supports that, but it doesn't prove a limit. Rising and bounded above doesn't, by itself, fix where it ends. Say that the far future is suggested, and keep what's settled separate. And remember the drawn curve is a floating point drawing. The legend says so.

@art approach-line
In y prime equals t minus y, the line y equals t minus one is itself a solution. Its derivative is one, and t minus t minus one is one, so the residual is zero. The curve from zero, two bends toward that line. That's suggested here, and established in a later course.

@art leaves-window
Now y prime equals y squared, through zero, one. The curve climbs, steeper and steeper, and leaves the window before t equals one. The slope y squared is never negative, so it never falls. But is it just large at the edge, or has it stopped existing there? The field can't tell, and the lesson on blow up answers it.

@chapter Where people slip
@list heading="Common slips" items="Letting solution curves cross@The first|Stating a limit the picture only suggested@The second|Treating leaving the window as blowing up@the third"
The first slip is letting solution curves cross. A sketch with a crossing has an error in it. The second is stating a limit as something the picture proved. And the third is treating a curve that leaves the window as one that blows up. A later lesson shows how to tell.

@chapter Try it
@words text="y′ = y·(1 − y),  start at y = 2" sub="slope 2·(1 − 2) = −2"
Your turn. Start a solution at y equals two. The slope there is two times one minus two, minus two, so the curve falls. Say which line it can never cross, and why. Then say what the picture suggests about where it heads.

@end text="Settled, or only suggested?"
You can read the horizontal solutions and signs of any field, on Learn. That's learn dot get er done dot I O.
