---
format: long
lesson: dynamic-programming-and-sequential-decisions/silver-meal-and-least-unit-cost
title: Silver-Meal vs least unit cost: two shortcuts that both lose
thumb: Neither one dominates
---

@chapter Two shortcuts
@title text="Silver-Meal and Least Unit Cost" sub="Dynamic Programming and Sequential Decisions" art=thumb
The exact lot sizing plan needs a recursion over the whole horizon. Two rules of thumb promise to get close by looking only a few periods ahead. Let's see how close.

@art extend-interval
Both rules build the plan from left to right. Start an interval at the first uncovered period, and try covering one more period, then another. The interval's cost is the setup K plus h times its holding.

@art average-turns
Each rule watches a running average. While it strictly falls, keep extending. At the first value that doesn't fall, close the interval and start again at the next uncovered period.

@chapter Per period or per unit
@math heading="Which average?" items="Silver-Meal:  (K + h × holding) / periods covered@Silver Meal;;Least unit cost:  (K + h × holding) / units covered@least unit cost"
The only difference is the average. Silver Meal divides the interval's cost by the number of periods it covers. Least unit cost divides it by the quantity ordered.

@art two-averages
That matters when demand rises sharply. Adding a period adds a lot of quantity, so the per unit average keeps falling long after the per period one has turned up. So least unit cost places fewer, longer orders. They're answering different questions.

@chapter Where both miss
@words text="d = 17, 25, 73, 113, 89" sub="K = 116 · h = 1 · exact: 462"
Here's the lesson's instance. Demands seventeen, twenty five, seventy three, one thirteen and eighty nine, with setup one sixteen and holding one. The exact plan orders in periods one, three and four, for four sixty two.

@math heading="Silver-Meal, from period 1" items="116 / 1 = 116@one sixteen;;141 / 2 = 70.5@seventy point five;;287 / 3 = 95.67  ↑ stop, span 2@ninety five"
Silver Meal from period one. One sixteen over one is one sixteen. Cover two periods: one forty one over two, seventy point five. Cover three: two eighty seven over three, about ninety five point seven. It turned up, so stop at two periods.

@math heading="The three plans" items="Exact:  1–2, 3, 4–5 = 462@exact;;Silver-Meal:  1–2, 3–4, 5 = 486  (+24)@Silver Meal;;Least unit cost:  1–3, 4–5 = 492  (+30)@least unit cost"
Carry on, and here are the plans. The exact one costs four sixty two. Silver Meal covers one and two, three and four, then five, for four eighty six, twenty four over. And least unit cost covers one to three, then four and five, for four ninety two, thirty over, with only two orders.

@chapter Where one is exact
@words text="d = 10, 62, 12, 130, 154, 129" sub="K = 54 · h = 2 · exact: 294"
Now the six period instance from the Wagner Whitin lesson. Silver Meal produces exactly the optimal plan, at two ninety four. Least unit cost places four orders and costs six hundred, more than twice the optimum.

@art ratio-swamp
Why so bad? From period three it covers three and four together, carrying one thirty units a period at two each. That's two sixty in holding to save a setup of fifty four. But the per unit average keeps falling, because the one thirty units in the bottom swamp the two sixty on top. It's watching the ratio, not the money.

@art three-plans
So on one instance Silver Meal is exact and least unit cost more than doubles. On the other, they're twenty four and thirty over. Two instances isn't a study. But it's enough to show neither rule dominates.

@chapter Where people slip
@list heading="Common slips" items="Treating the gap as an error that shrinks@The first|Picking one rule in advance@The second|Comparing order counts, not cost@And the third"
The first slip is treating the gap as an approximation error that shrinks with care. It's a different search, and nothing to tune. The second is picking one rule in advance. And the third is comparing the number of orders instead of the cost.

@art cost-vs-orders
On the five period instance, the exact plan and Silver Meal both place three orders and still differ by twenty four. And a flat demand instance, where everything agrees, is exactly where a heuristic looks best. That's why it isn't the test.

@chapter So why use them?
@words text="Exact needs the whole horizon" sub="the rules need the next few periods"
So why are both rules still in use? The recursion needs the whole horizon in advance. The rules need only the next few periods. On a rolling forecast, you aren't comparing four sixty two with four eighty six at all. You're comparing two different problems. The honest habit: whenever you can afford it, price the rule's plan against the recursion.

@chapter Try it
@words text="Flat demand: 30 × 6" sub="K = 80 · h = 1"
Your turn. Take six periods of thirty, setup eighty, holding one. Run both rules by hand, then the recursion. You should find all three agree on the same three order plan, costing three thirty.

@end text="Price every plan with one ruler"
You can run both rules against the exact plan, on your own demand, on Learn. That's learn dot get er done dot I O.
