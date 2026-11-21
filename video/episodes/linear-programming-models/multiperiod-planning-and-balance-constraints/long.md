---
format: long
lesson: linear-programming-models/multiperiod-planning-and-balance-constraints
title: Multiperiod planning: the balance row that ties a plan together
thumb: Cheaper, and fifty units short
---

@chapter The question
@title text="Multiperiod Planning and Balance Constraints" sub="Linear Programming Models" art=thumb
A plant makes one product over four periods. Each period has its own demand and its own cost. How do you tie the periods together so the plan makes sense from one to the next?

@art four-periods
Picture four periods in a row, with a store between each one and the next. Units made early can wait in the store, at a price.

@math heading="The data" items="demand:  20, 35, 30, 25@twenty, thirty five;;cost to make one:  9, 8, 7, 6@nine, eight;;capacity 60 a period · carry 1 a unit · opening stock 5@sixty"
Demand is twenty, thirty five, thirty and twenty five. Making a unit costs nine, eight, seven, then six. At most sixty can be made in a period. Carrying a unit forward costs one, and there are five units in the store before the first period.

@chapter The balance equation
@art store-flow
The answer is one equation per period. The stock carried out of a period is the stock carried in, plus what was made, minus what was sold.

@math heading="Balance" items="Iₜ = Iₜ₋₁ + Pₜ − Dₜ@the stock at the end;;Pₜ + Iₜ₋₁ − Iₜ = Dₜ@for a solver"
In symbols, I t, the stock at the end of period t, equals I t minus one, plus P t, minus D t. For a solver, put the data on the right: P t plus I t minus one, minus I t, equals D t.

@art inventory-chain
Here's the key point. Inventory is a decision variable, not a formula. Each I appears in exactly two rows: the period that carries it out, and the period that carries it in. That's the link.

@chapter The model
@math heading="Four balance rows" items="P₁ − I₁ = 15@fifteen;;P₂ + I₁ − I₂ = 35@P two plus I one;;P₃ + I₂ − I₃ = 30@periods three;;P₄ + I₃ − I₄ = 25@and four"
The first row is P one minus I one equals fifteen. That's twenty demanded, with five already in the store. Then P two plus I one minus I two equals thirty five, and so on for periods three and four. Every P is at most sixty, and every P and I is at least zero.

@words text="Opening stock is data" sub="no I₀ variable"
Notice the first row has no I zero variable. The opening stock is data. Make it a variable and you hand the plan a free store to draw from.

@chapter The cheapest plan
@math heading="Optimum" items="make 15, 35, 30, 25@fifteen, thirty five;;carry 0 every period@carries nothing;;cost 775@seven hundred and seventy five"
The cheapest plan makes fifteen, thirty five, thirty and twenty five, and carries nothing, at a cost of seven hundred and seventy five. Why? Making gets cheaper every period and carrying costs money. So make each unit as late as the balance rows allow, the period it's sold in.

@math heading="Capacity 30, period-two demand 40" items="make 25, 30, 30, 25@twenty five first;;I₁ = 10@carries ten;;cost 835@eight hundred and thirty five"
Now cut capacity to thirty and raise period two's demand to forty. Period two can't make what it sells. So the plan makes twenty five first, carries ten forward, then makes thirty, thirty and twenty five, for eight hundred and thirty five.

@art carry-forward
That first inventory variable, ten, is the only thing in the model that could make the second period feasible at all.

@chapter The aggregate row
@math heading="One row instead of four" items="P₁ + P₂ + P₃ + P₄ ≥ 105@a hundred and five;;make 0, 0, 45, 60@nothing at all;;cost 675@six hundred and seventy five"
The tempting shortcut is one row: total production at least total demand, a hundred and five. It solves, and it's cheaper. The plan makes nothing at all in the first two periods, then forty five and sixty. Cost: six hundred and seventy five, against seven seventy five.

@art unmet-demand
Run it through the periods. Fifteen units go unmet in period one, and thirty five in period two. Fifty units unserved, by a plan the objective calls better. Nothing is infeasible and no arithmetic is off. The row is true, just much weaker, and the cost can't show what was lost.

@chapter Where people slip
@list heading="Common slips" items="One aggregate row@The first|Copying the middle pattern into period one@The second|Letting the store go negative@The third"
The first slip is replacing the balance rows with one aggregate row. The second is copying the middle period pattern into the first period. The third is letting the store go negative. Drop I two at least zero, and I two equals minus thirty five reads as thirty five units promised and never delivered.

@art backorder
If backorders really are allowed, give them their own variable and their own cost, on purpose. If not, the sign restriction is the row that says so.

@chapter Try it
@words text="Capacity 30, demand 40 in period 2" sub="read the inventory path"
Your turn. With capacity thirty and period two demand forty, write the four balance rows. Read off the production and inventory paths, and check that each row balances.

@end text="Read the production and stock paths"
You can change the demands and capacities and read both paths off the solution, on Learn. That's learn dot get er done dot I O.
