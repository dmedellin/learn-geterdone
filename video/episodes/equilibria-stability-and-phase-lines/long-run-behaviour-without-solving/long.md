---
format: long
lesson: equilibria-stability-and-phase-lines/long-run-behaviour-without-solving
title: Long-run behaviour without solving: follow the arrow
thumb: Follow the arrow to the limit
---

@chapter The question
@title text="Long-Run Behaviour Without Solving" sub="Equilibria, Stability and Phase Lines" art=thumb
Where does a solution end up as time goes on? For y prime equals f of y, you can answer that for every starting point at once, without a formula, using the phase line.

@words text="y → 1     y → +∞"
A limit is a statement about what a solution does as t grows. y tends to one means y gets and stays as close to one as you like. y tends to infinity means it rises past every height. Neither says the solution ever arrives.

@chapter Three facts
@art stays-in-gap
First, a solution stays in the gap it starts in. Every equilibrium is a constant solution, and only one solution passes through each point. To leave its gap a solution would have to touch an equilibrium, putting two solutions through one point.

@art monotone
Second, inside a gap f has one sign, so the solution always rises or always falls. It never turns round. The arrow in that gap is the direction for every solution living there.

@words text="limit = the equilibrium the arrow points to" sub="or ±∞ if that end is open"
Third, a solution that keeps rising either runs into the equilibrium above it, never reaching it, or rises past every height if there's none. It can't stop short, because there the slope would still be bounded away from zero and it would carry on. That last step is stated, not proved here.

@chapter One equation, three starts
@math heading="y′ = (y − 1)·(y − 3)" items="f′(1) = −2 stable,  f′(3) = 2 unstable@f prime of one;;signs at 0, 2, 4:  + − +@test values"
Take y prime equals y minus one times y minus three. Its equilibria are one and three. f prime of one is minus two, so one is stable, and f prime of three is two, so three is unstable. The signs at the test values zero, two and four are plus, minus, plus.

@list heading="Three starts" items="start 0:  ↑  → 1@zero|start 2:  ↓  → 1@two|start 4:  ↑  → +∞@four"
So a start at zero rises to one. A start at two falls to one. And a start at four, above the unstable equilibrium with nothing above it, rises without limit.

@art three-starts
Starts zero and two are on opposite sides of one, and end at the same place, because both arrows point at it. From four, the Euler steps with a step of a quarter go nineteen quarters, then four hundred nine over sixty four, and climb. This climb even ends at a finite time, so tends to infinity is the right statement.

@chapter Steps are evidence, not proof
@math heading="From 2,  h = 1/4" items="2,  7/4,  97/64,  …@seven quarters"
With a step of a quarter, the steps from two run two, seven quarters, ninety seven over sixty four, and so on, falling and staying above one, as the arrow says.

@art column-of-steps
But a column of steps is evidence, not proof. Twelve steps that fall are twelve numbers, and no finite column reaches one. The arrow, which comes from the sign of f, is the reason.

@math heading="From 5/2,  h = 1" items="5/2,  7/4,  13/16,  313/256@thirteen sixteenths"
A step that's too large can disagree. From five halves with a step of one, the steps are five halves, seven quarters, thirteen sixteenths, and three hundred thirteen over two hundred fifty six. The third is below one and the fourth above it again.

@art overshoot
The column rocks about the equilibrium. No solution does that. The polygon stepped over one, which a solution can't do, so the error is the step size, not the equation. A smaller step doesn't do it.

@chapter Starting on the unstable point
@art split-at-three
Start exactly at three. Every Euler step is three, since f of three adds nothing, and the lab says at equilibrium. But a start just below three is in the gap from one to three, and goes down to one. A start just above goes to infinity. Unstable means nearby starts leave. It doesn't mean they all leave the same way.

@chapter Where people slip
@list heading="Common slips" items="Oscillating between two equilibria@The first|Unstable sends everything to infinity@The second|Reading a limit from steps alone@The third"
The first slip is thinking a solution between two equilibria might oscillate. It can't cross them, and it only rises or only falls. The second is saying an unstable equilibrium sends everything to infinity. Read the arrow in the start's own gap. The third is reading a limit from a column of steps alone.

@chapter Try it
@words text="y′ = (y − 1)·(y − 3)" sub="limits from −1, 3/2 and 7/2?"
Your turn. Using the phase line of y minus one times y minus three, state the limit for starts at minus one, three halves, and seven halves. Name the gap each start is in before you answer.

@end text="Follow the arrow"
You can type any start and see the predicted limit beside the exact steps, on Learn. That's learn dot get er done dot I O.
