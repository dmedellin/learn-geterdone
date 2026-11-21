---
format: long
lesson: networks-flows-paths-and-assignments/potentials-and-the-stepping-stone-cycle
title: Potentials and the stepping-stone cycle: improving a transportation plan
thumb: Price it, then cycle it
---

@chapter The question
@title text="Potentials and the Stepping-Stone Cycle" sub="Networks, Flows, Paths and Assignments" art=thumb
You've got a starting plan for a transportation table. Is it the cheapest? And if it isn't, which empty cell should you start using, and how much should move?

@chapter Potentials
@math heading="On every occupied cell" items="uᵢ + vⱼ = cᵢⱼ@u i plus v j;;c̄ᵢⱼ = cᵢⱼ − uᵢ − vⱼ@reduced cost"
Give each row a potential u, and each column a potential v. On every occupied cell, u i plus v j must equal that cell's cost. Then every cell gets a reduced cost: its cost, minus u i, minus v j. Occupied cells come out at zero by construction.

@art potential-tree
There are m plus n potentials but one equation fewer, so you fix one potential, any one, and walk the tree of occupied cells. Each cell hands a known value across to an unknown one. That's why the basis had to be a spanning tree.

@math heading="North-west start, three-plant table" items="u = (0, 5, 3)@u equals;;v = (10, 2, 4, 15)@v equals;;0 + 10 = 10 = c(A, D1)  ✓@check"
On the north west start of the three plant table, fixing u A at zero gives u equals zero, five, three, and v equals ten, two, four, fifteen. As a check, zero plus ten is ten, which is the cost in cell A, D one.

@chapter Reading the reduced costs
@art reduced-cost-grid
If every empty cell has a reduced cost of zero or more, the plan is optimal. A negative one means that route is cheaper than the current plan, by that much per unit. Here, two cells stand out.

@math heading="Which cell enters?" items="most negative: (C, D1) at −9 · Dantzig@most negative;;first negative: (A, D4) at −4 · Bland@first negative"
The most negative is C, D one, at minus nine. That's Dantzig's rule. The first negative is A, D four, at minus four. That's Bland's rule. The rule changes the path, not where you end up.

@art shift-potentials
Fix a different potential, v D one at zero, and all seven potentials move by ten. But not one of the twelve reduced costs changes, because the shift cancels. So u A equals zero is a choice, not a fact.

@chapter The cycle
@art staircase-cycle
Adding one cell to a spanning tree makes exactly one cycle. Put a plus on the entering cell, then alternate minus and plus round the cycle. Row and column sums stay the same for any amount you move. For C, D one, the cycle has six corners, a staircase.

@art false-rectangle
The rectangle you might guess, along row C and up column D one, would have to turn at B, D one. That cell is empty. A cycle may cross an empty cell, but it can only turn at an occupied one.

@math heading="First pivot" items="minus cells carry 10, 5, 5  →  θ = 5@theta is five;;(B, D2) leaves@leaves;;cost 520 → 475 = 520 − 9 × 5@nine times five"
How much moves? The smallest amount on a minus cell. Those carry ten, five and five, so theta is five, and B, D two leaves the basis. The cost falls from five hundred and twenty to four hundred and seventy five, which is nine times five less.

@chapter Degeneracy
@art flat-step
On the second pivot, A, D four enters, but the smallest minus cell carries a zero. So theta is zero. The basis changes and the cost stands still at four hundred and seventy five. The run goes five twenty, four seventy five, four seventy five, four thirty five. Non increasing is the claim, not strictly decreasing.

@words text="Dummy priced at 160, not 0" sub="real bill 605 either way · +1600 on every plan"
And that dummy question gets a number. Price the surplus table's dummy at one hundred and sixty instead of zero. Every plan sends ten units there, so every plan gets sixteen hundred added, and the real bill stays at six hundred and five.

@chapter Where people slip
@list heading="Common slips" items="Believing u₁ = 0 is part of the method@The first|Drawing a rectangle instead of tracing the cycle@The second|Removing two cells when both hit zero@And the third"
The first slip is believing u one equals zero is part of the method. The second is drawing a rectangle instead of tracing the cycle. And the third is removing two cells when two minus corners hit zero together. Only one leaves. The other stays, carrying zero.

@chapter Try it
@words text="Enter (A, D4) instead" sub="trace its cycle, find θ"
Your turn. From the north west start, suppose Bland's rule picks A, D four first. Trace the cycle it closes, turning only at occupied cells, mark the plus and minus corners, and find the smallest allocation on a minus corner.

@end text="Price every cell, trace every cycle"
You can fix any potential and watch the cycle each entering cell closes, on Learn. That's learn dot get er done dot I O.
