---
format: long
lesson: market-structure/invalidation-stops-risk-reward
title: Where your stop goes, and how many units that allows
thumb: The stop sets the size
---

@chapter The question
@title text="Invalidation, Stops & Reward-to-Risk" sub="Market Structure" art=thumb
Where should a stop go? A lot of people put it where the loss starts to feel uncomfortable. This lesson argues for a different place: where the trade idea is wrong.

@words text="The stop expresses the thesis" sub="size adapts to the stop, not the other way round"
And then the rest follows. Position size adapts to the structural stop. You don't squeeze the stop tighter just to justify a bigger position.

@chapter The risk chain
@art risk-chain
Every number should come from the thesis, not from the profit you hope to make. There are three links in the chain: invalidation, position size, and the R multiple.

@list heading="The risk chain" items="Invalidation@Invalidation|Position size@Position size|R multiple@the R multiple"
Invalidation is the price event that disproves the setup: a protected swing breaks, a breakout fails, or acceptance returns inside a range. Position size is the risk budget divided by the risk per unit. And the R multiple is the potential reward divided by the planned risk.

@art r-ladder
One warning about R. It compares geometry, not the probability that the target will be reached. A three R target is not automatically better than a one and a half R target. Setup quality, target realism, liquidity, gaps, and execution still matter.

@chapter Three kinds of stop
@art stop-noise
There are three different stop problems. The first is a stop inside noise. It can be hit while the original structure is still perfectly valid. The position looks bigger, but the stop doesn't express the thesis.

@art stop-structural
The second sits beyond invalidation. It's past the protected swing, with a deliberate buffer for ordinary noise. This is the one the position should be sized around, because it's the real distance.

@art stop-far
And the third is arbitrarily far. A stop can be structurally unnecessary as well as too tight. The extra distance shrinks your size without adding any defined reason.

@chapter Pick the stop
@words text="Thesis: invalid only when the protected low breaks" sub="with room for ordinary noise"
Now the lesson's drill. Price pulled back, stopped at ninety eight forty five, and then carried through one hundred and four. The rule: the long thesis is invalid only when the protected low breaks, with enough room for ordinary noise.

@list heading="Which stop?" items="A  102.80 — inside recent candle noise@A, at one hundred two|B  97.80 — below the protected low@B, at ninety seven|C  91.00 — far below, no stated reason@C, at ninety one|No stop; wait for recovery@no stop at all"
You get four choices. A, at one hundred two eighty, is inside recent candle noise. B, at ninety seven eighty, is below the protected low. C, at ninety one, is far below with no stated reason. Or no stop at all. Only B says what the rule says, so B is the stop.

@chapter Now size it
@words text="Entry 105.00 · stop B 97.80" sub="$25,000 account · 0.50% risk · $1 per 1.00 move per unit"
Now size it. Entry is one hundred five, and the stop is B. The account is twenty five thousand dollars, risking half a percent per trade, at one dollar per point per unit, whole units only.

@math heading="Entry 105.00 · stop 97.80" items="Budget = 0.50% × $25,000 = $125@budget first;;Risk per unit = 105.00 − 97.80 = 7.20@one hundred five minus;;125 ÷ 7.20 = 17.36…@divided by seven twenty;;Whole units, round down → 17 units@round down"
The budget first: one hundred twenty five dollars. Then one hundred five minus ninety seven eighty is seven twenty per unit. One twenty five divided by seven twenty is about seventeen point three six. Whole units only, so round down: seventeen units.

@words text="17 × 7.20 = $122.40 ≤ $125"
Check it. Seventeen units times seven twenty is one hundred twenty two dollars forty, inside the budget. Eighteen would go over.

@art size-scale
And notice what the stop did. If the structure had demanded a wider stop, the same budget would buy fewer units. A tighter valid stop allows more. The size moves. The budget and the thesis stay put.

@chapter A word on options
@words text="Linear exposure only" sub="options: plan with the premium"
The lesson's calculator assumes linear price exposure. Options are nonlinear. So for an option, plan with the premium or an option price exit, rather than treating the underlying's price distance as the exact contract risk.

@chapter Where people slip
@list heading="Common slips" items="Stopping where it feels comfortable@The first|Shrinking the stop to size up@The second|Treating 3R as better than 1.5R@The third"
Three slips to watch. The first is placing the stop where the loss feels comfortable instead of where the idea is wrong. The second is squeezing the stop to justify a bigger size. And the third is treating a bigger R as a better trade, when R is geometry, not probability.

@end text="Plan a trade in R"
You can move the entry, stop and target, and watch the size and R update, on Learn. That's learn dot get er done dot I O.
