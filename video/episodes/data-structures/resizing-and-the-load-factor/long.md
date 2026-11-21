---
format: long
lesson: data-structures/resizing-and-the-load-factor
title: Hash table resizing: the threshold gap that stops thrashing
thumb: Two thresholds, not one
---

@chapter The question
@title text="Resizing and the Load Factor" sub="Data Structures" art=thumb
A hash table has to grow when it fills and shrink when it empties. That sounds like one rule. It's actually two thresholds, and if you put them in the same place, the table spends almost all its time rehashing.

@chapter Why resize at all
@art load-band
A table's cost depends on its load factor, alpha. Too high, and chains grow or probes cluster. Too low, and most of the memory sits empty. So alpha has to stay in a band.

@list heading="The standard policy" items="Grow: at α = 1, double m@grow|Shrink: at α = ¼, halve m@shrink|Either way, rehash all n keys@Either way"
The usual mechanism is to pick two thresholds. Grow, by doubling m, when alpha reaches one. Shrink, by halving m, when alpha falls to a quarter. Either way, every key is rehashed into the new table, because every slot is computed from m.

@art rehash-all
So a resize is Theta of n, and there's no cleverer way. That's fine. Like the two stack queue, the bound is amortised. The expensive operation is still there, but doubling makes resizes exponentially rare.

@chapter Why the gap matters
@art potential-meter
The proof uses a potential, a measure of how close the table is to its next resize. Roughly two n minus m above half full, and m over two minus n below. An ordinary operation changes it by a constant. A resize costs n, and releases the potential that the operations since the last resize paid in.

@words text="The gap guarantees ≈ n/2 operations between resizes"
And here's the key step. The gap between the thresholds guarantees there were at least about n over two operations since the last resize. So there's enough potential saved up to pay for the rehash, and every operation is constant amortised.

@art two-thresholds
That's why the standard pair is one and a quarter. The shrink threshold is deliberately far below half the growth threshold. After any resize, the load sits far from both lines, so many operations must happen before another is due. That gap is called hysteresis.

@art thrash
Now put both thresholds at a half. Grow, and alpha halves, so it's sitting right on the shrink threshold. No potential has built up. The next operation resizes again. That isn't a worse constant. There's no bound at all.

@chapter Forty operations, two ways
@math heading="Grow at 1, shrink at ¼" items="rehashes:  2@two rehashes;;keys moved:  12@twelve keys;;total:  52  ·  3m line at 120@fifty two"
Here's the lab's boundary pattern. Fill a table from m equals four, then alternate inserts and deletes, forty operations. With the standard policy, there are two rehashes, both early, moving twelve keys. Total cost fifty two, well under the line of a hundred and twenty.

@math heading="Grow at ½, shrink at ½" items="rehashes:  39 of 40@thirty nine;;keys moved:  455@four hundred and fifty five;;total:  495@four ninety five"
Now the equal thresholds, same forty operations. Thirty nine rehashes, out of forty. Four hundred and fifty five keys moved. A total of four ninety five, four times the bound. From operation eight, it swings between sixteen and thirty two slots on almost every step.

@words text="1.3 vs 12.375 per operation" sub="the second grows with the table"
That's one point three per operation against twelve point three seven five. And the second isn't a constant. Each thrashing resize costs n, so doubling the sequence roughly quadruples the cost.

@chapter Growth alone
@math heading="40 inserts, no deletes" items="rehashes at m = 4, 8, 16, 32@four rehashes;;4 + 8 + 16 + 32 = 60 keys@sixty keys;;total 100  ·  line 120@a hundred"
For contrast, forty inserts and no deletes. Four rehashes, at four, eight, sixteen and thirty two, moving sixty keys. Total, a hundred. The doubling costs form a geometric series, so reaching size n costs about two n, whatever the thresholds.

@art geometric-growth
That's the cleanest case of the amortised argument, and the one to look at first. It's also the easy case. Almost any pair of thresholds looks fine on pure growth, which is exactly why it's a bad test.

@chapter Where people slip
@list heading="Common slips" items="Shrinking at half the growth threshold@The first|Reading the measured average as the bound@The second|Testing a policy on growth only@And the third"
The first slip is shrinking at half the growth threshold, which sounds symmetric and thrashes. The second is reading one point three as the amortised constant. It's one run under a bound proved elsewhere. And the third is testing only on growth, where every policy looks fine. Alternation near a threshold is what tells them apart.

@chapter Try it
@words text="Count the rehashes under both policies" sub="insert/delete sequence of your own"
Your turn. Write a short insert and delete sequence, cost it under both pairs of thresholds, and name the one that thrashes, and the operation where it starts.

@end text="Make a table thrash"
You can run both policies on the same operations and watch the rehashes pile up, on Learn. That's learn dot get er done dot I O.
