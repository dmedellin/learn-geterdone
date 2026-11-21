---
format: long
lesson: duality-and-sensitivity-analysis/objective-coefficient-ranging-and-reduced-costs
title: Objective ranging: when a profit change moves the plan
thumb: The plan sits still, then jumps
---

@chapter The question
@title text="Objective Coefficient Ranging" sub="Duality and Sensitivity Analysis" art=thumb
A product gets more profitable. Does your plan change? Usually not. The total changes, the plan sits still, and then at one exact value, it jumps.

@art rotating-line
Changing a profit tilts the objective line. Tilt it a little, and it still touches the same corner. The corner only changes when the line tilts far enough to lie flat along an edge.

@words text="Is the activity in the basis?"
The first question to ask about any coefficient is whether the plan currently makes any of that product. The answer picks which of two calculations applies.

@chapter Reduced cost
@math heading="Reduced cost" items="rⱼ = yᵀaⱼ − cⱼ@y transpose a j;;basic:  rⱼ = 0@basic;;nonbasic:  rⱼ ≥ 0@every other one"
The reduced cost of column j is y transpose a j, minus c j. In words: what one unit would consume, valued at today's prices, minus what it earns. It's zero on every basic column, and non negative on every other one. A product isn't made because that number is positive.

@art row-vs-column
Right hand side ranging asked how far data could move while the basis stayed feasible. This asks how far it can move while the basis stays optimal. That's a ratio test along the objective row, not down a column.

@chapter The example
@math heading="max 8x₁ + 5x₂ + 3x₃" items="machine:  2x₁ + x₂ + x₃ ≤ 10@machine;;labour:  x₁ + x₂ + 2x₃ ≤ 8@labour;;contract:  x₁ ≤ 4@contract"
Take maximise eight x one plus five x two plus three x three. Machine: two x one plus x two plus x three at most ten. Labour: x one plus x two plus two x three at most eight. Contract: x one at most four.

@math heading="The optimum" items="x = (2, 6, 0),  z* = 46@forty six;;y = (3, 2, 0)@three, two, zero;;r₃ = 3 + 4 − 3 = 4@four"
The optimum is two, six, zero, worth forty six, with prices three, two, zero. x one and x two are basic, so their reduced costs are zero. For x three, it's three plus four minus three, which is four.

@chapter A coefficient being made
@math heading="c₁ = 8,  range 5 ≤ c₁ ≤ 10" items="c₁ = 9:  still (2, 6, 0),  z* = 46 + 1·2 = 48@nine;;c₁ = 10:  (2, 6, 0) and (4, 2, 0) both earn 50@ten;;c₁ > 10:  plan becomes (4, 2, 0)@past ten"
x one is basic, and its range is five to ten. Raise it to nine, and the plan doesn't move at all. Still two, six, zero. The total goes up by one times two, to forty eight. At ten, a reduced cost hits exactly zero, and four, two, zero also earns fifty. Two corners tie. Past ten, the plan has changed.

@art jump-corner
Past that value, the best corner is the neighbour along that edge, and one pivot gets you there.

@art corner-tie
That's the inside of a basic range: a different number, the same decision. The plan changes once, at a value you can compute in advance.

@chapter A coefficient not being made
@math heading="c₃ = 3,  reduced cost 4,  range c₃ ≤ 7" items="c₃ = 6:  still (2, 6, 0),  z* = 46@six;;c₃ = 7:  (4, 0, 2) ties at 46@seven;;c₃ = 8:  plan (4, 0, 2),  z* = 48@eight"
x three isn't made, and its reduced cost is four, so its range is up to seven. Raise it from three to six, and nothing happens. Same plan, same forty six. Twice as profitable, still not worth making. At seven, four, zero, two ties. At eight, the plan moves to four, zero, two, worth forty eight.

@art catch-up
So the improvement needed before anything happens is exactly the reduced cost. The range is one sided, because making a product less profitable can't make it worth starting. Unbounded below is a complete answer.

@chapter Plan or value?
@list heading="Which one changes" items="Inside a basic range: value only@basic range|Inside a nonbasic range: neither@nonbasic range|At an end: two plans tie@At the end|Past an end: the plan changes@Past the end"
So every answer has two parts. Inside a basic range, the value changes and the plan doesn't. Inside a nonbasic range, neither changes. At the end of either, two plans tie, one pivot apart. Past the end, the plan has changed, and the old range describes nothing.

@art minimise-negate
On a minimisation, the same ranging works. The solver negates a minimisation on the way in, so a coefficient handed to it must be negated too. Skip that, and the intervals look fine but the endpoints are wrong.

@chapter Where people slip
@list heading="Common slips" items="Expecting every change to move the plan@The first|Using the wrong computation@The second|Reading the wrong column@The third"
The first slip is expecting any change to the objective to change the answer. The second is running the basic computation on a nonbasic coefficient, or the reverse. And the third is reading the reduced cost off the wrong column. Here, the true column is one, two, zero, giving four. Read one, one, zero by mistake and you get two, and an interval that looks perfectly reasonable.

@end text="Slide a coefficient, watch the plan"
You can slide each coefficient and see exactly where the plan jumps, on Learn. That's learn dot get er done dot I O.
