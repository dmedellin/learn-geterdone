---
format: long
lesson: linear-programming-models/blending-and-ratio-constraints
title: Percentages in a linear programme, and when clearing is legal
thumb: Clear the total, check the sign
---

@chapter The question
@title text="Blending and Ratio Constraints" sub="Linear Programming Models" art=thumb
At least thirty percent of the blend must be naphtha. That sentence has a decision hiding in its denominator. It looks non linear. It isn't, but only for a reason you should check.

@art blend-tanks
A refinery blends naphtha, reformate and butane into a hundred litre batch. Naphtha costs five a litre, reformate three, and butane two. At least thirty percent must be naphtha, and at most twenty five percent may be butane. Minimise the cost.

@chapter Shares of a total
@math heading="At least 30% naphtha" items="N ≥ 3/10 (N + R + B)@three tenths of;;(7/10)N − (3/10)R − (3/10)B ≥ 0@seven tenths N"
The batch is N plus R plus B litres. So the requirement is N at least three tenths of N plus R plus B. Multiply out and collect terms, and you get seven tenths N, minus three tenths R, minus three tenths B, at least zero.

@art share-pie
That's the pattern. One minus t goes on the component you named, and minus t goes on every other. Every variable appears, even the ones the sentence never mentioned. That's the visible sign that a share is about the whole batch.

@math heading="At most 25% butane" items="B ≤ 1/4 (N + R + B)@a quarter of;;−(1/4)N − (1/4)R + (3/4)B ≤ 0@three quarters B"
The butane ceiling works the same way. B at most a quarter of the total clears to minus a quarter N, minus a quarter R, plus three quarters B, at most zero.

@words text="Right-hand side: 0, always"
And notice the right hand side is zero. A share carries no constant. Scale the whole batch up or down and it still holds or fails just the same.

@chapter The cheapest batch
@art mixing-tank
Put the model together. Minimise five N plus three R plus two B. The batch row says N plus R plus B equals a hundred litres. Add the two cleared share rows, and keep all three amounts at least zero.

@math heading="Optimum" items="N = 30,  R = 45,  B = 25@thirty litres;;cost 335@three hundred and thirty five;;shares 3/10,  9/20,  1/4@three tenths"
The cheapest batch is thirty litres of naphtha, forty five of reformate and twenty five of butane, costing three hundred and thirty five. The shares are three tenths, nine twentieths and a quarter, exact fractions.

@art floor-ceiling
It takes as much cheap butane as the ceiling allows, and as little expensive naphtha as the floor allows. That's exactly what the two bounds were written to control.

@chapter A quantity for a proportion
@math heading="N ≥ 3/10 by mistake" items="N = 3/10 litre@three tenths of a litre;;cost 1378/5@thirteen seventy eight;;naphtha share 0.3%@point three percent"
Now write N at least three tenths, without the total. The model still solves, but answers a different question. The cheapest batch has three tenths of a litre of naphtha, costs thirteen seventy eight over five, and the naphtha share is point three percent.

@art unit-mismatch
N is in litres. A proportion is measured in nothing. The two sides don't carry the same unit, and no arithmetic will complain.

@words text="N ≥ 3/10 (R + B)" sub="naphtha share 3/13, about 23.08%"
A subtler slip takes the share of the wrong total: thirty percent of the others, not of the batch. It's a legal row, and a weaker one. It's satisfied at a naphtha share of three thirteenths, about twenty three point oh eight percent.

@chapter The ratio to decline
@math heading="N ÷ B ≥ 2" items="N − 2B ≥ 0  ?@N minus two B;;(30, 70, 0) is feasible@thirty, seventy, zero;;N ÷ B undefined,  30 ≥ 0 holds@not a number"
Clear N over B at least two and you'd get N minus two B at least zero. But that's only legal if B stays strictly positive. The batch thirty, seventy, zero is feasible, with no butane. There, N over B is not a number, while the cleared row reads thirty at least zero and holds.

@art zero-denominator
The cleared row admits points the original never spoke about. So the lab declines the move, and names the blend that refutes it. Whether B can vanish is itself a linear programme: add B at most zero and see if anything's left.

@chapter Where people slip
@list heading="Common slips" items="A quantity where a proportion was meant@The first|Clearing a denominator that can be zero@The second|The share of the wrong total@The third"
Three slips. The first is writing a quantity where a proportion was meant. The second is clearing a ratio whose denominator can be driven to zero. And the third is taking the share of the wrong total. The safeguard is simple: compute the achieved share at the optimum, and compare it with what the specification asked for.

@chapter Try it
@words text="At most 25% butane" sub="clear it yourself, then check the shares"
Your turn. Clear the butane ceiling by hand. Then check that at the optimum, butane's share is exactly one quarter.

@end text="Clear a share, check the total"
You can clear share rows and test ratio rows against a feasible blend, on Learn. That's learn dot get er done dot I O.
