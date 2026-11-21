---
format: long
lesson: integer-programming/fixed-charges-facility-location-and-big-m
title: Big M: why "a million to be safe" quietly ruins your bound
thumb: The smallest valid M
---

@chapter The problem
@title text="Fixed Charges, Facility Location and Big-M" sub="Integer Programming" art=thumb
Some costs are paid only if an activity happens at all. Open a warehouse and you pay to open it, whether you ship one unit or a thousand. A linear cost can't say that. You need a binary.

@art fixed-switch
Let y be one if the facility opens and zero if not. Put the fixed charge times y in the objective, and link y to the amount shipped with x at most M times y. At y equals zero that forces x to zero. At y equals one, it's slack, as long as M is big enough.

@words text="y = 1 never forces x > 0"
Note what it doesn't do. Opening never forces shipping. Paying a fixed cost for nothing stays feasible. It's just never optimal.

@chapter Two facilities
@art two-facilities
The lesson's instance: facility one costs two hundred to open and two a unit. Facility two costs sixty to open and six a unit. Each can handle forty units, and demand is thirty.

@math heading="Open one or the other" items="facility 1:  200 + 2 × 30 = 260@facility one;;facility 2:  60 + 6 × 30 = 240@facility two;;answer: 240@the answer"
Open facility one and you pay two hundred plus sixty, two sixty. Open facility two and you pay sixty plus a hundred and eighty, two forty. So the answer is two forty. The question is how well the relaxation knows it.

@chapter Size M from a reason
@words text="M = 30" sub="no facility ships more than total demand"
M must allow every amount the rest of the model allows. No facility can ship more than total demand, which is thirty. So thirty is valid, and nothing smaller is. A million isn't a reason. Total demand being thirty is a reason.

@words text="M = 30 → bound 240, 1 node"
At M equals thirty, the relaxation sets y two to one, whole. The bound is two forty, which is the answer, and the search tree closes in a single node.

@chapter What a loose M buys the relaxation
@art fraction-open
Now set M to six hundred. Nothing about feasibility changes. But the relaxation ships all thirty from facility one, and sets y one to thirty over six hundred, one twentieth. It pays a twentieth of the opening cost: ten plus sixty, seventy.

@math heading="Same answer, weaker proof" items="M = 30:  bound 240,  1 node@thirty;;M = 60:  bound 160,  5 nodes@sixty;;M = 150:  bound 100,  5 nodes@a hundred and fifty;;M = 600:  bound 70,  5 nodes@six hundred;;M = 1200:  bound 65,  5 nodes@twelve hundred"
At thirty, the bound is two forty in one node. At sixty, a hundred and sixty. At a hundred and fifty, a hundred. At six hundred, seventy. At twelve hundred, sixty five, and each of those needs five nodes. Every one returns the same answer, two forty.

@art bound-decay
Here's why. With y equal to x over M, each unit costs its shipping cost plus the fixed cost over M. As M grows, the opening cost is spread thinner and thinner, and the relaxation drifts toward a model where opening is free.

@math heading="Where the preference flips" items="2 + 200/M = 6 + 60/M@two plus;;140/M = 4  →  M = 35@thirty five"
That also explains the bend. The two effective costs are equal where two plus two hundred over M equals six plus sixty over M. That's at M equals thirty five. Above it, the relaxation half opens the expensive to build, cheap to run facility.

@art crossing-lines
And from there the bound decays and never comes back. A loose M doesn't make the model wrong. It costs the bound, and so the proof and the work.

@chapter Too small is worse
@art tree-nodes
An M that's too small is a different failure. It forbids plans the situation allows, and returns a confident answer to a problem nobody asked. It's silent, because the model still solves. That's why the reason matters more than the number.

@chapter Where people slip
@list heading="Common slips" items="A million, to be safe@The first|Choosing M by feel@The second|Rounding the fractional y up@And the third"
The first slip is setting M to a million to be safe. It's safe for feasibility and ruinous for the bound. The second is choosing M by feel instead of from a stated bound. And the third is rounding the fractional y up and calling it a solution.

@chapter Try it
@words text="M = 60 → y₁ = ?" sub="effective unit cost 2 + 200/M"
Your turn. At M equals sixty, work out each facility's effective unit cost. Decide which one the relaxation prefers, find its y, and confirm the bound is a hundred and sixty.

@end text="Size M and watch the bound"
You can change M and watch the bound and the tree respond, on Learn. That's learn dot get er done dot I O.
