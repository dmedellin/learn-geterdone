---
format: long
lesson: randomised-algorithms/balls-in-bins-and-the-birthday-bound
title: Balls in bins: why hash collisions start at the square root
thumb: Collisions start near √m
---

@chapter The model
@title text="Balls in Bins and the Birthday Bound" sub="Randomised Algorithms" art=thumb
Throw keys into slots at random. How many collide? How many slots stay empty? And when does a collision become more likely than not? Two of those have clean answers. One is a question this library won't pretend to answer.

@art balls-bins
Here's the model. n keys go into m slots. Each key lands in a uniformly random slot, independently of the others. That's the idealised hash function. A collision is a pair of keys in the same slot.

@chapter Colliding pairs
@math heading="Linearity over pairs" items="X_ij = 1 if keys i and j share a slot@for each pair;;E[X_ij] = 1/m@one over m;;E[X] = C(n, 2)/m = n(n − 1)/2m@n times n minus one"
For each pair of keys, let an indicator be one if they share a slot. Wherever key i lands, key j lands there with probability one over m. Add up over all the pairs, and the expected number of colliding pairs is n times n minus one, over two m.

@art transitive
Notice those indicators aren't independent. If one and two collide, and two and three collide, then one and three certainly do. Linearity of expectation doesn't care. That's the step most people think needs independence. It doesn't.

@words text="23 keys, 365 slots:  253/365 ≈ 0.693"
At twenty three keys in three hundred and sixty five slots, that's two hundred and fifty three over three sixty five, about point six nine three. The seeded throw had exactly one colliding pair. Change the seed and the count moves. The expectation doesn't.

@chapter Empty slots
@math heading="Linearity over slots" items="P(slot j empty) = (1 − 1/m)ⁿ@all n miss;;E[empty] = m(1 − 1/m)ⁿ@m times;;23 keys, 365 slots:  ≈ 342.68@three hundred and forty two"
A key misses a given slot with probability one minus one over m. The keys are independent, so all n miss it with that, to the n. Sum over slots: m times one minus one over m, to the n. At twenty three keys that's about three hundred and forty two point six eight, and the throw left three hundred and forty three empty.

@art empty-slots
Those slot indicators are dependent too. If all but one slot is empty, the last one isn't.

@words text="independent throws, dependent slots"
Keep two things apart. The throws are independent, and that's a real hypothesis. The slot indicators aren't, and nothing needs them to be.

@chapter Even odds
@math heading="P(all apart), exactly" items="(m/m)·((m − 1)/m)·…·((m − n + 1)/m)@the product;;m = 365,  n = 23:  0.492703…@twenty three"
The chance all n keys land apart is the product of m over m, m minus one over m, and so on. The lab multiplies it out exactly. At three hundred and sixty five slots, it first drops below a half at twenty three keys, point four nine two seven. So twenty three makes a collision more likely than not, and twenty two doesn't.

@art sqrt-curve
The familiar estimate, root two m log two, is a rule of thumb. The panel doesn't use it. It searches upward through the exact product.

@list heading="First n past even odds" items="m = 64:  n = 10@sixty four|m = 128:  n = 14@one hundred and twenty eight|m = 365:  n = 23@three hundred and sixty five|m = 1000:  n = 38@a thousand"
At sixty four slots, even odds arrive at ten keys. At one hundred and twenty eight, at fourteen. At three hundred and sixty five, at twenty three. At a thousand, at thirty eight. Each is close to the square root of m. A thousand slot table is likely to collide at about four per cent full.

@art chains
That's why hash tables are built around load factors and chains, not around avoiding collisions. Collisions are the expected state of a table that's a few per cent full.

@chapter The maximum load
@words text="max load ≈ log n / log log n" sub="STATED, NOT PROVED"
With as many keys as slots, the mean load is exactly one. The maximum is about log n over log log n. The panel quotes it, labelled stated, not proved, because the proof needs Chernoff bounds, which this library doesn't teach. At three sixty five, the stated figure is three point three two. The tallest slot held four.

@art tall-slot
Those don't contradict each other. A growth rate with hidden constants isn't a prediction about one small instance. The expectations are derived here. The maximum is measured, and derived nowhere.

@chapter Where people slip
@list heading="Common slips" items="Claiming independence for linearity@The first|Confusing expected collisions with the chance of one@The second|Sizing for the mean load@And the third"
The first slip is claiming independence to justify linearity. The second is confusing the expected number of collisions with the chance of one. At twenty three keys those are point six nine three and point five zero seven. And the third is sizing capacity for the mean load, when the maximum is what fills up.

@end text="Collisions start near the square root"
Throw your own keys and watch the slots fill, on Learn. That's learn dot get er done dot I O.
