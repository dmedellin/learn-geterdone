---
format: long
lesson: duality-and-sensitivity-analysis/shadow-prices-and-right-hand-side-ranging
title: Shadow prices only hold over a range, and here's how to find it
thumb: A price comes with a range
---

@chapter The question
@title text="Shadow Prices and Right-Hand-Side Ranging" sub="Duality and Sensitivity Analysis" art=thumb
One more hour of assembly is worth one pound to the workshop. So twenty more hours are worth twenty pounds? Not necessarily. A shadow price is true only over a range, and the range is part of the answer.

@chapter What a shadow price is
@words text="yᵢ = change in z* per unit of bᵢ" sub="while the basis stays feasible"
A shadow price is the change in the optimal value per unit of one right hand side, holding everything else fixed. It's the i th entry of y, which you've already read off the final tableau.

@math heading="Why it's the slope" items="plan = B⁻¹b@B inverse b;;value = c_BᵀB⁻¹b = yᵀb@y transpose b;;bᵢ + Δ  →  yᵀb + yᵢΔ@Add delta"
Here's why. With the basis fixed, the plan is B inverse b, and the value is y transpose b. Add delta to b i, and the value becomes y transpose b plus y i times delta. Linear, with slope y i, for as long as that basis stays optimal.

@art basis-feasible
And the only thing that can break it is feasibility. The objective row doesn't involve b at all. So the basis stays optimal exactly while the plan stays non negative.

@chapter Finding the range
@math heading="The range" items="d = B⁻¹eᵢ@column i;;need  x_B + Δd ≥ 0@at least zero;;each basic variable bounds Δ@one bound"
Let d be column i of B inverse. The basis stays optimal while x B plus delta d is at least zero. That's a ratio test. Each basic variable gives one bound on delta, and the tightest ones give the two ends. At each end, some basic variable hits exactly zero.

@art range-band
So every price comes with an interval, and the current right hand side sits somewhere inside it.

@list heading="The workshop's prices" items="Cutting: 0, for 2 ≤ b₁@Cutting is worth|Glazing: 3/2, for 6 ≤ b₂ ≤ 18@Glazing is worth|Assembly: 1, for 12 ≤ b₃ ≤ 24@Assembly is worth"
Cutting is worth zero, for b one at least two, with no upper limit. Glazing is worth three halves, from six to eighteen. Assembly is worth one, from twelve to twenty four. And notice: even the worthless cutting row has an end. Below two, it starts to bite.

@chapter The optimum as a function
@math heading="z* against assembly hours b₃" items="0 to 12:  slope 5/2@five halves;;12 to 24:  slope 1@twelve to twenty four;;24 up:  slope 0@nothing at all"
Plot the optimum against assembly hours. From zero to twelve, the slope is five halves. From twelve to twenty four, it's one. Past twenty four, it's nothing at all, because the plan has run out of cutting capacity and can't use more assembly.

@art piecewise-line
Three prices, one row, each true on its own interval. The optimum is piecewise linear, with a corner at every breakpoint.

@math heading="Predict, then check" items="z*(20) = 36 + 1(20 − 18) = 38  ✓@thirty eight;;naive z*(26) = 36 + 1(26 − 18) = 44@forty four;;true z*(26) = 42@forty two"
At eighteen hours, the price is one. Predict twenty hours: thirty six plus one times two, thirty eight. Correct. Now predict twenty six: thirty six plus eight, forty four. The truth is forty two.

@art outside-range
That isn't a small approximation error. The function is exactly linear on each piece. You used the wrong slope, because the basis it belonged to stopped being feasible at twenty four.

@chapter Worth nothing, two ways
@words text="Slack → price 0" sub="cutting has 2 spare"
A row can be worth nothing in two ways. The easy one: the cutting row has two units spare, so its price is zero. More of something you're not using can't help.

@math heading="max x + y" items="x ≤ 2,  y ≤ 2,  x + y ≤ 4@at most two;;firing: 0, for 4 ≤ b₃@firing;;kiln, wheel: 1, for 0 ≤ b ≤ 2@kiln and wheel"
The other: maximise x plus y, with x at most two, y at most two, and x plus y at most four. At two, two, all three are tight. Firing is priced at zero, for b three at least four. Tight, fully used, and worthless. And kiln and wheel are worth one, from zero to two.

@art one-sided
But two is where they already are. The range has no room above. So that price is valid for decreases only. Quoting it as the value of one more unit is wrong.

@chapter Not a derivative
@art two-slopes
At twelve hours, it's five halves arriving and one leaving. At a breakpoint, the slope arriving and the slope leaving are both correct, and different. A derivative would have to pick one. A rate with a stated interval reports both.

@chapter Where people slip
@list heading="Common slips" items="Quoting a price for any change@The first|Assuming a price must be positive@The second|Confusing this with objective ranging@The third"
The first slip is treating a shadow price as valid for any change. The second is assuming a price must be positive. On a floor in a maximisation, it's at most zero. And the third is confusing this range with the range of an objective coefficient. That's a different ratio test, and it's next.

@end text="Never quote a price without its range"
You can slide a right hand side and watch the price hold, then break, at its range, on Learn. That's learn dot get er done dot I O.
