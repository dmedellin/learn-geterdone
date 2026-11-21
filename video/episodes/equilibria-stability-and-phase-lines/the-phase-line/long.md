---
format: long
lesson: equilibria-stability-and-phase-lines/the-phase-line
title: The phase line: every solution's direction, without solving
thumb: One test value per gap
---

@chapter The question
@title text="The Phase Line" sub="Equilibria, Stability and Phase Lines" art=thumb
Can you tell where every solution of an equation is heading without solving it? For y prime equals f of y, you can, with a number line, a few dots, and one test value in each gap.

@chapter One sign per gap
@art sign-gaps
Between two consecutive equilibria, f can't change sign. A polynomial changes sign only by passing through zero, and the equilibria are exactly its zeros. So on each gap, f is positive throughout or negative throughout, and one value decides which.

@words text="f > 0: up      f < 0: down"
Where f is positive, the slope is positive and solutions rise, so the arrow points to larger y. Where f is negative, the arrow points down. And a solution can't leave its gap, because leaving would mean passing through an equilibrium.

@art phase-line
Draw the y axis, mark each equilibrium with a dot, and put an arrow in every gap, including the two ends. That's the phase line, the whole qualitative story of the equation, without a formula.

@chapter A worked example
@math heading="f(y) = y·(y − 1)·(y − 3)" items="f(−1) = −8   ↓@minus one;;f(1/2) = 5/8   ↑@one half;;f(2) = −2   ↓@At two;;f(4) = 12   ↑@at four"
Take y cubed minus four y squared plus three y, which factors with roots zero, one and three. Test one number in each piece. At minus one, f is minus eight, so down. At one half, it's five eighths, up. At two, it's minus two, down. And at four, it's twelve, up.

@art cubic-phase-line
Read upwards along the axis. Below zero, solutions fall away from zero. Between zero and one, they rise towards one. Between one and three, they fall, again towards one. Above three they rise, and nothing stops them.

@words text="1 draws solutions in;  0 and 3 push them away"
So without finding a single formula, the picture says one draws in solutions from both sides, and zero and three push them away.

@chapter Direction, not speed
@math heading="Speed is |f(y)|" items="|f(1/2)| = 5/8@five eighths;;|f(2)| = 2@at two it's two;;2 ÷ 5/8 = 16/5@sixteen fifths"
The arrow is a sign, and only a sign. At one half, the speed is five eighths. At two it's two. So a solution through two is falling sixteen fifths times as fast as one through a half is rising, and the two arrows are the same size.

@art slowing-approach
One consequence is worth keeping. Close to an equilibrium, f is close to zero, so solutions slow down as they close in. The arrows look as if they run all the way to one, but they describe a limit that's never reached in finite time.

@chapter One equilibrium
@math heading="y′ = 2 − y" items="f(1) = 1 > 0   ↑@f of one;;f(3) = −1 < 0   ↓@f of three"
With a single equilibrium there are only two arrows. For y prime equals two minus y, the equilibrium is two. Test at one and three. f of one is one, positive. f of three is minus one, negative. Both arrows point at two.

@art two-gaps
So every solution heads for two. Start below it, and the solution rises towards two. Start above, and it falls towards it. Either way it slows as it closes in, and never arrives in finite time.

@chapter Where people slip
@list heading="Common slips" items="Reading arrow length as speed@The first|Putting dots at the test values@The second|Copying one gap's sign to the rest@The third"
The first slip is reading arrow length as speed. The second is using the test values in place of the equilibria. The dots are the roots, so list them first. The third is testing one gap and copying the sign. Signs alternate across a simple root, but not across a repeated one. For y squared times one minus y, the signs are plus, plus, minus.

@art wrong-arrow
Here's a drawing with two arrows that can't both be right. The cubic drawn with up on zero to one, and up again on one to three. The second is wrong. f of two is minus two. And a solution rising there would have to pass through three, an equilibrium, which can't be crossed.

@chapter Try it
@words text="y′ = y²·(1 − y)" sub="test at −1, 1/2 and 2"
Your turn. Find the equilibria of y prime equals y squared times one minus y. Test at minus one, one half and two, and draw the arrows. Check that the first two point the same way.

@end text="Draw the arrows"
You can type an equation and watch its phase line appear, on Learn. That's learn dot get er done dot I O.
