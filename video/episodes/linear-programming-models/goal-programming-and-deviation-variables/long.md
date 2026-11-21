---
format: long
lesson: linear-programming-models/goal-programming-and-deviation-variables
title: Goal programming: when your targets can't all be met
thumb: The order is the answer
---

@chapter The question
@title text="Goal Programming and Deviation Variables" sub="Linear Programming Models" art=thumb
What do you do when you want three things and can't have all of them? Make them hard constraints and the model just says infeasible. That tells you nothing about which target to give up.

@art cabinet-shop
A cabinet shop builds standard and deluxe units, S and D, in units a week. Its one hard limit is sixty machine hours: two S plus three D at most sixty.

@list heading="Three wishes" items="£60 profit, at 3 and 4 a unit@sixty pounds|At most 30 hours overtime, at 3 and 6 a unit@no more than thirty|12 deluxe units@twelve deluxe"
It would also like three things. Sixty pounds of profit, at three and four a unit. No more than thirty hours of overtime, at three and six a unit. And twelve deluxe units built. Together, as constraints, they're infeasible.

@art infeasible-targets
And infeasible is a much worse answer than missed by twelve units, when the numbers were only aspirations in the first place. A goal programme keeps the model answerable, and makes the compromise visible.

@chapter Deviation variables
@math heading="A target with two deviations" items="a·x + u − o = b@two extra variables;;u ≥ 0,  o ≥ 0@at least zero"
So write each target as an equation with two extra variables. u is how far the plan falls short. o is how far it overshoots. Both are at least zero.

@art two-deviations
Then penalise only the one you mind. For profit you mind falling short. For overtime you mind going over. At an optimum, at most one of the pair is positive, because the penalised one gets pushed to zero whenever it can be.

@math heading="The cabinet goals" items="3S + 4D + u₁ − o₁ = 60@profit;;3S + 6D + u₂ − o₂ = 30@overtime;;D + u₃ − o₃ = 12@deluxe"
So the profit row is three S plus four D plus u one minus o one equals sixty, and u one is minded. The overtime row has o two minded. The deluxe row has u three minded.

@chapter One programme per level
@math heading="Profit, then overtime, then deluxe" items="level 1:  minimise u₁ → 0@level one;;level 2:  u₁ = 0,  minimise o₂ → 30@level two;;level 3:  o₂ = 30,  minimise u₃ → 12@level three"
Take the goals in order: profit, overtime, deluxe. Level one minimises u one and gets zero. Fifteen deluxe units and no standard ones hit the profit target exactly. Level two freezes u one equals zero, and minimises o two. That comes out at thirty hours. Level three freezes that, and minimises u three, which comes out at twelve. The deluxe run is what pays.

@art frozen-level
That frozen row is what makes it a sequence. Without it, level two would simply abandon the profit target and undo level one. With it, each level searches only among plans that keep what the level above achieved.

@chapter Reorder it
@list heading="Three orderings" items="Profit first: overtime 30 over, deluxe short 12@profit first|Overtime first: profit short 30, deluxe short 12@Overtime first|Deluxe first: profit met, overtime 54 over@Deluxe first"
Change the order and everything moves. Profit first, as you've seen: thirty hours over on overtime and twelve deluxe units short. Overtime first: overtime is met, profit misses by thirty, and deluxe still misses by twelve. Deluxe first: it's met, profit's met too, and overtime is fifty four hours over.

@art three-orderings
Three orderings, three different sacrifices, each optimal for its own priorities. Choosing between them isn't a mathematical act.

@chapter The silent failure
@math heading="One weighted objective" items="minimise u₁ + o₂ + u₃@u one plus o two;;total 42@forty two;;S = 10,  D = 0@ten standard"
The tempting alternative is one objective: minimise u one plus o two plus u three. It reports a total of forty two, with ten standard units and no deluxe. But it just added pounds to hours to units. And that plan is the overtime first answer, chosen without anyone choosing that order.

@art mixed-units
A weighted objective always gives a number, and it encodes an exchange rate nobody wrote down. Raise the weight on a pound of profit to four, and it switches to the profit first plan. Weights can work, but only scaled into a common currency on purpose.

@chapter Still linear
@words text="Every level is an ordinary LP"
And none of this leaves the linear class. Every row is linear, the deviations are ordinary non negative variables, and each level is an ordinary linear programme. What's new is that the answer is a sequence of solves, plus a sentence.

@chapter Where people slip
@list heading="Common slips" items="Making a target a hard constraint@The first|Adding deviations in different units@The second|Penalising both deviations@The third"
The first slip is making a target a hard constraint. The second is adding deviations in different units. And the third is penalising both deviations, which turns an aspiration into a demand for exactly sixty.

@chapter Try it
@words text="Reorder the three goals" sub="which goal pays, and by how much?"
Your turn. Pick an ordering of the three goals, solve level by level, and write the sentence: which goal was sacrificed, at which level, and by how much, in its own unit.

@end text="Reorder the goals yourself"
You can reorder the goals and watch each level freeze the one above it, on Learn. That's learn dot get er done dot I O.
