---
format: long
lesson: duality-and-sensitivity-analysis/the-dual-problem
title: The dual problem, derived rather than memorised
thumb: The cheapest certificate
---

@chapter The question
@title text="The Dual Problem" sub="Duality and Sensitivity Analysis" art=thumb
Every linear programme carries a second one hidden inside it, with a variable for each constraint and a constraint for each variable. You don't need to memorise its rules. Each one is forced.

@math heading="The workshop" items="max 3x₁ + 5x₂@maximise;;x₁ ≤ 4@cutting;;2x₂ ≤ 12@glazing;;3x₁ + 2x₂ ≤ 18@assembly"
Take the workshop. Maximise three x one plus five x two, with x one at most four for cutting, two x two at most twelve for glazing, and three x one plus two x two at most eighteen for assembly.

@chapter Building a bound
@art weighted-rows
Choose a price for each row, y one, y two, y three, all at least zero. Multiply each row by its price, and add them up. The left side becomes y one plus three y three times x one, plus two y two plus two y three times x two. The right side is four y one plus twelve y two plus eighteen y three.

@math heading="When the sum bounds the objective" items="y₁ + 3y₃ ≥ 3@at least three;;2y₂ + 2y₃ ≥ 5@at least five;;3x₁ + 5x₂ ≤ 4y₁ + 12y₂ + 18y₃@for every feasible"
That left side is at least three x one plus five x two whenever y one plus three y three is at least three, and two y two plus two y three is at least five. Then, for every feasible x, the objective is at most four y one plus twelve y two plus eighteen y three.

@math heading="The dual" items="min 4y₁ + 12y₂ + 18y₃@the smallest;;y₁ + 3y₃ ≥ 3,  2y₂ + 2y₃ ≥ 5,  y ≥ 0@those two rows"
So the best bound you can build is the smallest such sum. Minimise four y one plus twelve y two plus eighteen y three, subject to those two rows, with y at least zero. That's the dual.

@art bound-ceiling
Picture it as a lid. Every choice of prices puts a ceiling over the whole feasible region. The dual pushes that ceiling down until it rests on the best corner.

@chapter Every line is forced
@list heading="Why each piece" items="y ≥ 0: keeps each ≤ pointing the same way@a negative multiplier|x ≥ 0: lets the combination dominate c@x one not to be negative|minimise: a bound is best when smallest@as small as"
Every line was forced. You need y at least zero, because a negative multiplier would flip a row and the sum would bound nothing. You need x at least zero, so that a bigger coefficient means a bigger term, which requires x one not to be negative. And the dual minimises because a bound is only worth having as small as it can be made.

@art transpose-trap
So the dual isn't the transpose of the primal. It's the cheapest certificate the primal admits. The transpose is just what that turns out to look like.

@words text="Cutting + assembly per x₁ ≥ £3"
Read the first dual row aloud. The cutting and assembly capacity that one unit of x one uses must be worth at least the three that unit earns.

@chapter The rules
@list heading="In a maximisation" items="≤ row → y ≥ 0@at most row|≥ row → y ≤ 0@at least row|= row → y free@equals row|x free → dual row is =@free variable"
Run the same argument on other shapes, and you get the rules. In a maximisation, an at most row gives a non negative price. An at least row is a floor, and relaxing a floor can't improve a maximum, so its price is at most zero. An equals row binds both ways, so its price is free. And a free variable makes its dual row an equation.

@art mirror-pair
If the primal is a minimisation, every one of those turns over. The requirement rows get non negative prices, the caps get non positive ones, and the dual maximises. Same derivation, different shape.

@chapter The mixed case
@math heading="Cap, floor, quota, free v" items="max 4u + 3v@four u plus three v;;2u + v ≤ 10,  u − v ≥ 1,  u + v = 4@capacity;;u ≥ 0,  v free@v is free"
Here's a case that uses them all. Maximise four u plus three v, with two u plus v at most ten for capacity, u minus v at least one for balance, and u plus v equals four, a quota. u is at least zero, and v is free.

@math heading="Its dual" items="min 10y₁ + y₂ + 4y₃@ten y one;;2y₁ + y₂ + y₃ ≥ 4@the u column;;y₁ − y₂ + y₃ = 3@the v column;;y₁ ≥ 0,  y₂ ≤ 0,  y₃ free@y two at most zero"
The dual minimises ten y one plus y two plus four y three. The u column gives two y one plus y two plus y three at least four. The v column, because v is free, gives an equation: y one minus y two plus y three equals three. And y one is at least zero, y two at most zero, y three free.

@art dual-of-dual
The primal solves to eighteen, at u equals six, v equals minus two. A negative variable at the optimum, which is what declaring it free was for. And take the dual of the dual, and the original comes back, sign for sign.

@chapter Where people slip
@list heading="Common slips" items="Transposing and copying the rest@The first|Pairing a price with a variable@The second|A non-negative price on an = row@The third"
The first slip is transposing the matrix and copying everything else across. The result bounds nothing. The second is pairing a price with a variable instead of a row. Count first. The third is giving an equals row a non negative price.

@art price-units
And here's a ten second check. A price's units are the objective's units over its row's units, like pounds per hour. If you can't say a price's units out loud, you've paired it with the wrong row.

@end text="Derive the dual, then dualise it again"
You can build the dual of a mixed programme, see the reason for every sign, and take it back again, on Learn. That's learn dot get er done dot I O.
