---
format: long
lesson: duality-and-sensitivity-analysis/pricing-a-new-activity-and-adding-a-constraint
title: Should you make the new product? Price it against what it displaces
thumb: Profitable isn't enough
---

@chapter The question
@title text="Pricing a New Activity, Adding a Constraint" sub="Duality and Sensitivity Analysis" art=thumb
Someone proposes a new product. Someone else proposes a new rule. Do you have to solve the whole model again? No. The tableau you already have answers both.

@chapter Pricing a column
@art new-column
Start with a product nobody has made yet. A machine nobody has bought, or a contract nobody has signed, works the same way. In the tableau it's just one more column, and you can value it before anything is committed.

@math heading="Reduced cost of a new column" items="c_new − yᵀa_new@c new minus;;> 0  ⟹  it enters@positive"
A new product with column a new and earnings c new has reduced cost c new minus y transpose a new, using the prices already in the final tableau. For a maximisation, it's worth introducing exactly when that's positive.

@art displaced-work
In words: what it earns, minus what its ingredients are already worth in the plan you have. Nothing requires the column to have been in the model when you solved it. The prices belong to the basis, and any column can be valued against them.

@math heading="Workshop prices y = (0, 3/2, 1)" items="new product (1, 1, 1),  earns 4@one hour of each;;uses 0·1 + (3/2)·1 + 1·1 = 5/2@five halves;;4 − 5/2 = 3/2 > 0  →  enters,  36 → 39@thirty nine"
The workshop's prices are zero for cutting, three halves for glazing, and one for assembly. Propose a product using one hour of each, earning four. It consumes five halves worth of what the plan is short of. Its reduced cost is four minus five halves, three halves per unit. It enters, and a single pivot takes the total from thirty six to thirty nine.

@chapter Profitable, and still wrong
@math heading="A heavier column" items="new product (1, 2, 3),  earns 4@two of glazing;;uses 0 + 3 + 3 = 6@six;;4 − 6 = −2  →  leave it out@minus two"
Now propose a product taking one hour of cutting, two of glazing and three of assembly, also earning four. It consumes six worth. Its reduced cost is four minus six, minus two. Every unit would displace work worth six to make four.

@art profit-trap
That's the misconception. The product makes money, so make it? It does make money. It makes less money than what it would have to stop making. Profit isn't the test. Profit beyond what the ingredients are already worth is the test.

@words text="Break-even at 5/2" sub="for the (1, 1, 1) product"
For the lighter product, the break even is earnings of exactly five halves. There, the reduced cost is zero, and the lab reports that it doesn't enter.

@chapter Testing a row
@art substitute-plan
A proposed constraint is a statement about plans, so evaluate it at the plan you have. If it holds, nothing follows. The plan is still feasible, and still optimal, because adding a rule can't create a better plan. If it fails, the plan is broken, and you'll need to restore feasibility.

@math heading="Plan (2, 6)" items="x₁ + x₂ ≤ 5:  reads 8, short by 3@at most five;;→ two pivots, lands at 25@twenty five;;x₁ + x₂ ≤ 10:  reads 8, 2 spare@at most ten;;→ nothing changes, 36@thirty six"
At the workshop's plan, two, six, the rule x one plus x two at most five reads eight. Broken by three. Restoring feasibility takes two pivots and lands at twenty five. The rule x one plus x two at most ten also reads eight, with two spare. It changes nothing at all. Same plan, same thirty six.

@art harmless-rule
That second answer is a real answer to a real question, reached by one substitution. No pivot, no re solve. A satisfied rule is genuinely free.

@chapter Which way it moves
@art up-and-down
A new rule can only cost. It removes points and never adds any. A new column can only help. If a proposed constraint seems to raise the objective, the arithmetic is wrong.

@words text="Short by 3, falls by 11"
And a broken rule doesn't tell you how much it costs. The rule is short by three, but the objective falls by eleven. The shortfall is about feasibility. The fall comes from re optimising, and that's the next lesson.

@chapter Where people slip
@list heading="Common slips" items="Making a product because it's profitable@The first|Reading the shortfall as the damage@The second|Testing a column as a row@The third"
The first slip is believing a product with positive profit is worth making. The second is reading a broken row's shortfall as the damage to the objective. It's wrong by a factor of nearly four here. And the third is testing a proposed column as though it were a row, or the reverse. Say which shape the proposal is before any arithmetic.

@end text="Price a product, test a rule"
You can propose products and rules and get each answer from the final tableau, on Learn. That's learn dot get er done dot I O.
