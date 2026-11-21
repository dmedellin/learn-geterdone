---
format: long
lesson: duality-and-sensitivity-analysis/strong-duality-from-the-final-tableau
title: Strong duality: the prices were in the final tableau all along
thumb: Read the prices, check them
---

@chapter The question
@title text="Strong Duality from the Final Tableau" sub="Duality and Sensitivity Analysis" art=thumb
Weak duality says matching values prove optimality. But where do prices that match come from? They aren't guessed. They're already printed in the final tableau of the primal solve.

@chapter Where the prices sit
@art identity-columns
In standard form, each row has some original column equal to a unit vector. Call those the initial identity columns. Since the tableau is B inverse times the data, the tableau column over each of them is a column of B inverse.

@words text="y = c_BᵀB⁻¹" sub="objective row, under the initial identity columns"
So the objective row entries under those columns are c B transpose B inverse. That's the price vector y, already sitting in a row most readers walk past.

@math heading="Workshop final z-row" items="x₁  x₂  s₁  s₂  s₃  |  rhs@final tableau;;0   0   0   3/2   1  |  36@zero, three halves, one;;y = (0, 3/2, 1),  z* = 36@thirty six"
In the workshop's final tableau, the identity columns are the three slacks. The objective row over them reads zero, three halves, one. So cutting is worth nothing, an hour of glazing is worth three halves, and an hour of assembly is worth one. And z star is thirty six.

@chapter Checking it
@math heading="Dual feasibility, column by column" items="x₁:  0·1 + (3/2)·0 + 1·3 = 3 ≥ 3@x one gives;;x₂:  0·0 + (3/2)·2 + 1·2 = 5 ≥ 5@x two gives;;slacks:  0, 3/2, 1 ≥ 0@slack columns"
Now check it. Column x one gives three, at least its cost of three, a gap of zero. Column x two gives five, at least five, gap zero. The slack columns give zero, three halves and one, against a cost of zero. Every gap is non negative, so y is dual feasible.

@math heading="Equal values" items="bᵀy = 4·0 + 12·(3/2) + 18·1@four times zero;;= 36 = z*@That's thirty six"
And b y is four times zero, plus twelve times three halves, plus eighteen times one. That's thirty six, which is z star.

@art closed-chain
Two checks, and weak duality does the rest. Dual feasibility is just the optimality test, which the method stopped on. And b y equals z star because B inverse b is the plan. That's strong duality, proved on this instance, in exact fractions.

@chapter Not the right-hand column
@art rhs-plan
Don't read the prices from the right hand column. That's B inverse b, the plan: x one two, s one two, x two six. It has one entry per row, like y, so it survives a glance. But it fails b y equals z star immediately.

@chapter A floor
@art bakery-loaves
Every example so far had only at most rows. That's the case where the identity columns and the slack columns are the same list, so the difference is invisible. A floor or a quota pulls them apart.

@math heading="Bakery:  max 5x + 4y" items="flour 6x + 4y ≤ 24,  sugar x + 2y ≤ 6@flour;;contract x + y ≥ 2@contract;;columns:  x, y, s₁, s₂, e₃, a₃@surplus and an artificial"
Now a programme with a floor. A bakery maximises five x plus four y, with flour and sugar limits, and a contract, x plus y at least two. The floor gets a surplus and an artificial, so the columns are x, y, s one, s two, e three, a three.

@math heading="Prices" items="y = (3/4, 1/2, 0)@three quarters;;bᵀy = 18 + 3 + 0 = 21 = z*@twenty one"
Read the identity columns: slack, slack, and the artificial. The prices are three quarters, a half and zero. And b y is twenty one, which is z star, at the plan three, three halves.

@art surplus-mirror
Read the third price from the surplus column instead, and you get its negative. That column of the original data is minus the unit vector.

@chapter A quota
@math heading="Contract becomes x + y = 3" items="columns:  x, y, s₁, s₂, a₃@no third slack;;y = (0, 0, 5)@zero, zero, five;;bᵀy = 3·5 = 15 = z*@fifteen"
Replace the floor with a quota: x plus y equals three. Now there's no third slack at all. The identity column is the artificial. The prices are zero, zero, five, and b y is fifteen, which is z star at three, zero.

@art quota-value
Both at most rows have slack, so they're priced at nothing. The whole value of the programme is attributed to the quota. And the y column's dual gap is five minus four, one. The second product is worth one less than the quota room it would use.

@chapter Where people slip
@list heading="Common slips" items="Reading prices from the right-hand column@The first|Assuming identity columns are slack columns@The second|Assuming dual feasibility@The third"
The first slip is reading prices from the right hand column. The second is assuming the identity columns are the slack columns. And the third is assuming dual feasibility instead of checking it. On a tableau you've modified by hand, it may not hold. It's one dot product per column.

@end text="Read the prices, then check them"
You can read the prices off a final tableau and check them column by column, on Learn. That's learn dot get er done dot I O.
