---
format: long
lesson: scaling-laws-and-cost/vertical-vs-horizontal
title: Many small nodes or one big box? It crosses twice
thumb: Two crossings, not one
---

@chapter Two plans
@title text="Vertical vs Horizontal" sub="Scaling Laws and Cost" art=thumb
You need five times the capacity of one node. Buy five more small nodes, or one bigger machine? Neither is always cheaper, and the place where they swap isn't where you'd think.

@art small-fleet
Horizontal means N small nodes at a price u each. But N nodes deliver less than N nodes' worth, because they coordinate. With a contention coefficient alpha, they deliver N over one plus alpha times N minus one.

@art size-ladder
Vertical means one machine from a ladder of sizes. Each doubling of size multiplies the price by more than two, here two point two. And you can only buy the rungs that exist.

@chapter Six nodes for five
@math heading="α = 1/200,  target 5×" items="200N / (199 + N) ≥ 5@two hundred N;;195N ≥ 995  ⟹  N ≥ 5.102…@five point one oh two;;N = 6@six nodes"
So don't divide. Solve. With alpha one two hundredth, N nodes deliver two hundred N over a hundred and ninety nine plus N. For five times, that gives N at least five point one oh two. So six nodes. Five would deliver only four point nine.

@art extra-node
The sixth node is bought entirely to pay for the coordination of the first five. At a target of sixty four times, you'd need ninety four nodes, thirty of them just carrying overhead. And the fleet tops out at one over alpha, two hundred times, however many you buy. A target of two hundred and fifty times can't be met horizontally at all.

@chapter The ladder
@math heading="Node $100.00,  ×2 size = ×2.2 price" items="1×:  $100.00@a hundred dollars;;2×:  $220.00@two hundred and twenty;;4×:  $484.00@four hundred and eighty four;;8×:  $1 064.80@one thousand and sixty four"
The ladder starts at a hundred dollars a month. Twice the size is two hundred and twenty. Four times is four hundred and eighty four. Eight times is one thousand and sixty four dollars eighty.

@art idle-rung
A target of five times needs the eight times rung, a thousand and sixty four eighty, with three nodes' worth sitting idle. Six small nodes cost six hundred. Horizontal wins by four hundred and sixty four dollars eighty a month. At eight times, that same rung is full and costs the same, while horizontal needs nine nodes at nine hundred.

@chapter Two crossings
@math heading="Cheaper side by target" items="2×:  3 nodes $300  vs  $220  →  vertical@at two;;3×:  4 nodes $400  vs  $484  →  horizontal@at three;;4×:  5 nodes $500  vs  $484  →  vertical@at four;;5×:  6 nodes $600  vs  $1 064.80  →  horizontal@From five times on"
Walk the targets. At two times, vertical. At three, four nodes at four hundred beat the four times rung, so horizontal. At four, the same rung now serves the bigger target at the same price, while horizontal has bought a fifth node. Vertical again. From five times on, horizontal never loses.

@art sawtooth
That's because a rung is cheap per unit until it's full, and gets cheaper as the target rises toward its top. Every rung repeats that, so vertical is a sawtooth against a straight line. One break even hides this. Report two numbers: where horizontal first wins, and where it stops losing.

@words text="64×:  94 nodes $9 400  vs  $11 337.99"
And the premium pulls away with size. At sixty four times, ninety four nodes cost nine thousand four hundred dollars, against eleven thousand three hundred and thirty seven ninety nine for the box. That's why large systems end up horizontal.

@chapter What the prices leave out
@art failure-domain
One machine is one failure domain. The fleet has parallel paths through it and the box doesn't. That's a probability, not a price, and it belongs in the recommendation. A cost comparison that leaves it out will pick the single box every time it's close.

@chapter Where people slip
@list heading="Common slips" items="Dividing the target by one node's capacity@The first|Reporting one break-even, not two@The second|Comparing nameplate with node count@the third"
The first slip is dividing the target by one node's capacity. The second is reporting one break even when the curve crosses twice. And the third is comparing a box's nameplate against a fleet's node count, when both need converting to delivered capacity.

@chapter Try it
@words text="×2 size = ×1.6 price" sub="same α, same node price"
Your turn. Change the ladder so doubling the size costs one point six times, not two point two. Keep alpha and the node price. Predict whether the two crossings move up or down, then find them in the lab, and say which targets changed verdict.

@end text="Solve, don't divide"
You can move the ladder and alpha and watch both crossings, on Learn. That's learn dot get er done dot I O.
