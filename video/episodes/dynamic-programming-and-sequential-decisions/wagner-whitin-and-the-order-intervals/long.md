---
format: long
lesson: dynamic-programming-and-sequential-decisions/wagner-whitin-and-the-order-intervals
title: Wagner-Whitin: why an ordering plan is just a set of intervals
thumb: Never order with stock left
---

@chapter The problem
@title text="Wagner-Whitin" sub="Dynamic Programming and Sequential Decisions" art=thumb
You know demand period by period. Every order costs a fixed charge, however big it is. And every unit you carry into the next period costs something to hold. How much should you order, and when?

@art demand-bars
Here's the setup. Demands d one to d T are known in advance. An order placed in a period arrives in time for that period and costs a setup charge K. Each unit carried into the next period costs h. No shortages, no starting stock, nothing left at the end.

@words text="cost = K × orders + h × unit-periods held"
A plan's cost is K times the number of orders, plus h times the total unit periods of holding. It looks like you're choosing a quantity in every period, which is a continuum. One small theorem collapses that.

@chapter The theorem
@art sawtooth-stock
There's always an optimal plan that orders only when stock has run out. So every order covers a run of consecutive periods, and orders exactly that run's demand.

@art holding-overlap
Here's why. Suppose a period starts with stock left over and also places an order. Shift some quantity from the earlier order into this one. The number of orders doesn't go up, and those units are held for fewer periods, so holding cost falls. Repeat until no period both holds and orders.

@art order-intervals
So a plan is a partition of the periods into consecutive intervals, each covered by one order. With T periods there are two to the T minus one of them, one yes or no choice at each boundary.

@chapter The recursion
@math heading="Cover periods 1 to t" items="F(0) = 0@zero;;F(t) = min over j of  F(j−1) + K + h · Σ (i − j) dᵢ@the last order"
Let F of t be the cheapest way to cover periods one to t, with F of zero equal to zero. If the last order went in period j, F of t is F of j minus one, plus K, plus the holding on that run, minimised over j. Period i's demand sits in stock for i minus j periods.

@chapter A worked example
@words text="d = 10, 62, 12, 130, 154, 129" sub="K = 54 · h = 2"
The lesson's demands are ten, sixty two, twelve, one thirty, one fifty four and one twenty nine. The setup is fifty four and holding is two per unit per period.

@math heading="The table" items="F(1) = 54@fifty four;;F(2) = min(178, 108) = 108@one oh eight;;F(3) = min(226, 132, 162) = 132@one thirty two;;F(4) = min(1006, 652, 422, 186) = 186@one eighty six;;F(5) = 240@two forty;;F(6) = 294@two ninety four"
F of one is fifty four. F of two is the smaller of one seventy eight and one oh eight. F of three is one thirty two, ordering in period two. F of four is one eighty six, then two forty, and finally two ninety four.

@math heading="Read the argmins back" items="orders: 10 in p1 · 74 in p2 · 130 in p4 · 154 in p5 · 129 in p6@five orders;;5 × 54 = 270@two seventy;;holding: 12 × 1 × 2 = 24@twenty four;;270 + 24 = 294@two ninety four"
Following the argmins back gives five orders: ten in period one, seventy four in period two, then one thirty, one fifty four and one twenty nine. Five setups is two seventy. The only holding is period three's twelve units, carried one period at two each, twenty four. Total two ninety four.

@chapter Read the argmin column
@words text="F(4): 1006, 652, 422, 186"
Look at F of four. The last candidate wins by miles. Covering period four's one thirty from any earlier order means holding it at least a period, which is two sixty, against a setup of fifty four. The values give the answer. The argmins tell you why.

@art even-blocks
Flat demand shows the balance. Every demand forty, setup ninety, holding one, and the plan is three orders of eighty, covering two periods each, for three ninety. Raise the setup and intervals lengthen. Raise holding and they shorten.

@art giant-period
And when one period dwarfs the rest, like a demand of two hundred with a holding rate of three, carrying it even once costs six hundred. So the plan is forced to break just before it.

@chapter Where people slip
@list heading="Common slips" items="Using stock on hand as the state@The first|Holding (i − j + 1) instead of (i − j)@The second|Forgetting demand was assumed known@And the third"
The first slip is using stock on hand as the state. It's bigger and no more correct. The second is charging holding on the period the order arrives for. Every candidate inflates, the plan often looks right, and every number is wrong. And the third is quoting the plan without saying demand was assumed known.

@chapter Try it
@words text="d = 8, 6, 200, 7, 9, 5" sub="K = 60 · h = 3"
Your turn. Demands eight, six, two hundred, seven, nine and five, with setup sixty and holding three. Fill the table. You should find three orders, one of them in period three, for two thirty four.

@end text="Slide the setup, watch the breaks move"
You can change the setup charge and watch the order intervals stretch and shrink, on Learn. That's learn dot get er done dot I O.
