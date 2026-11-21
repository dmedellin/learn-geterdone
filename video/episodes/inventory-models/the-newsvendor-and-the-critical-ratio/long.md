---
format: long
lesson: inventory-models/the-newsvendor-and-the-critical-ratio
title: The newsvendor problem and the critical ratio
thumb: The ratio is a probability
---

@chapter One order, one season
@title text="The Newsvendor and the Critical Ratio" sub="Inventory Models" art=thumb
You get one order for the whole season. Demand is uncertain, there's no reordering, and whatever's left at the end is wasted. How many do you buy?

@art one-season
That's the newsvendor problem. Demand D for the season is random, with a known distribution. You choose Q before the season starts, and you can't change it. There's no cycle, so there's no ordering cost to trade off.

@art two-errors
Instead, you trade two errors. Each unit short costs c u, the underage cost. Each unit left over costs c o, the overage cost. Buy for three and sell for ten, and a leftover costs the three you spent, while a shortage costs the seven of margin you didn't earn.

@chapter The rule
@math heading="Expected cost" items="C(Q) = cₒ·E[(Q − D)⁺] + cᵤ·E[(D − Q)⁺]@the expected cost"
So the expected cost is c o times the expected leftover, plus c u times the expected shortage.

@math heading="One more unit" items="saves cᵤ with probability 1 − P(D ≤ Q)@saves;;costs cₒ with probability P(D ≤ Q)@costs;;worth it while P(D ≤ Q) < cᵤ/(cᵤ + cₒ)@worth it"
Now raise the order by one. It saves c u if demand turns out bigger than Q. It costs c o otherwise. So it's worth it while the chance that demand is at most Q is below c u over c u plus c o. That's the critical ratio.

@words text="Order the smallest Q with P(D ≤ Q) ≥ cᵤ/(cᵤ + cₒ)"
So order the smallest quantity whose cumulative probability reaches the ratio. And notice: the ratio is a probability, not a quantity. That's the most useful thing to know about it.

@chapter A worked stall
@art demand-bars
Here's the lesson's stall. Demand is zero to four, with probabilities one, two, three, three and one tenths. Underage is seven, and overage is three. So the ratio is seven over seven plus three: seven tenths.

@art cdf-staircase
Add up the probabilities. One tenth, three tenths, three fifths, nine tenths. The first time the cumulative probability reaches seven tenths is at three. So order three.

@math heading="Expected cost" items="Q = 2:  47/10@two;;Q = 3:  37/10@three;;Q = 4:  57/10@four;;Q = 0: 147/10 · Q = 6: 117/10@nothing"
Check it against the whole curve. At two, forty seven tenths. At three, thirty seven tenths. At four, fifty seven tenths. Ordering nothing costs a hundred forty seven tenths, and ordering six costs a hundred seventeen tenths. Three is the cheapest row.

@art cost-curve
Every figure there is exact. The probabilities are fractions, so the expectations are too, and there's no square root anywhere in this model.

@chapter The mean is not the answer
@words text="Bakery: cᵤ 2, cₒ 5 · ratio 2/7" sub="mean 10 · order 9"
Now a bakery. Demand eight to twelve, mean exactly ten. Underage two, overage five, so the ratio is two sevenths. The order is nine, below the mean. When leftovers cost more, you plan to be short some of the time.

@words text="Spare part: cᵤ 20, cₒ 1 · ratio 20/21" sub="mean 15/16 · order 4"
And a spare part. Mean demand is fifteen sixteenths, less than one unit. But a stockout costs twenty times a leftover, so the ratio is twenty twenty firsts, and the order is four, the very top of the distribution.

@art below-and-above-mean
Above the mean, below it, and far above it. Nothing about the distributions explains that pattern. Everything about the two unit costs does.

@chapter Check, don't just apply
@words text="Rule and table, side by side"
So the lab computes the answer twice. Once by walking the cumulative distribution to the ratio, and once by pricing every whole quantity and taking the cheapest. They agree on all three instances. A rule argued one step at a time is easy to mis-state, with greater than for greater than or equal, and a table is the cheapest refutation.

@chapter Where people slip
@list heading="Common slips" items="Ordering the mean@The first|Swapping the two costs@The second|Rescaling probabilities that don't sum to one@And the third"
The first slip is ordering the mean. The second is swapping the two costs, which replaces the ratio by its complement and gives a plausible wrong answer. Price one quantity either side to catch it. And the third is quietly rescaling probabilities that don't sum to one. That's a typo, so stop and fix it.

@chapter Try it
@words text="Bakery: demand 8–12" sub="probabilities 1/8, 1/4, 1/4, 1/4, 1/8"
Your turn. For the bakery, the probabilities are an eighth, then a quarter three times, then an eighth. Find the cumulative probabilities, find where they reach two sevenths, and price the expected cost there. You should get twenty three eighths.

@end text="Find where the CDF reaches the ratio"
You can change the costs and the demand and check the rule against the whole cost curve, on Learn. That's learn dot get er done dot I O.
