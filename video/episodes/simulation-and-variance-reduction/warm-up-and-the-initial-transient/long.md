---
format: long
lesson: simulation-and-variance-reduction/warm-up-and-the-initial-transient
title: Warm-up and the initial transient: throw the beginning away
thumb: Delete, don't dilute
---

@chapter Starting empty
@title text="Warm-Up and the Initial Transient" sub="Simulation and Variance Reduction" art=thumb
Most queue simulations start with an empty system. It's convenient, and it quietly aims every average at the wrong number.

@art climbing-mean
At the start, the system is somewhere the steady state isn't. That's the initial transient. It isn't noise. The process is behaving correctly. It just isn't yet behaving like the long run you want to measure.

@math heading="Bias" items="bias(T) = E[T] − θ@bias"
The damage is bias: the expected value of the estimator, minus the true value. Bias is a property of the estimator. More replications don't shrink it, and it doesn't show in a standard error. The interval is just centred in the wrong place.

@art biased-cluster
And that makes it dangerous. A thousand runs started empty give a thousand estimates of the same wrong number, with a beautifully small standard error around it. A narrow interval around a biased estimate is worse than a wide one, because it's more convincing.

@chapter The transient, exactly
@math heading="p = 2/5 · q = 1/2 · started empty" items="E[N₀] = 0@zero;;E[N₁] = 2/5@two fifths;;E[N₂] = 3/5@three fifths;;E[N₃] = 37/50@thirty seven fiftieths;;stationary 12/5 = 2.4@twelve fifths"
For the same queue as last time, the number in system is a Markov chain, so you can push its whole distribution forward one slot at a time. The expected occupancy goes zero, two fifths, three fifths, thirty seven fiftieths, and on, climbing toward the stationary twelve fifths.

@math heading="Expected time averages" items="slots 0–399:  2.2443  (bias ≈ −0.1557)@from slot zero;;slots 100–399:  2.3717  (bias ≈ −0.0283)@after discarding"
So averaging from slot zero over four hundred slots is aimed at two point two four four three, about point one five six short. After discarding the first hundred, it's aimed at two point three seven one seven, only about point oh two eight short. That's exact, before any run is made.

@chapter Dilute or delete
@art dilute-vs-delete
The transient is a fixed lump of wrongness at the front. Run longer and its share falls like one over T. Discard it and it's gone.

@words text="100 → 400 slots: bias ÷ 3.5" sub="discard first 100 of 400: a further ÷ 5.5"
The numbers agree. Going from a hundred slots to four hundred divides the remaining bias by about three and a half. Discarding the first hundred of those four hundred divides it by about five and a half more, using a quarter of the data instead of four times the compute.

@art warmup-cut
So the cure is a warm up: throw the beginning away, and average only what comes after.

@chapter One run
@words text="Seed 0: 2.1125 → 2.4067" sub="after discarding 100 slots"
At seed zero, four hundred slots average two point one one two five from the start, and about two point four oh seven after the warm up. The estimate moved up, the direction the theory says.

@art seed-flip
But at seed one, the discard moves it down, from about one point three one to one point two four. That's not a counterexample. It's what a single observation looks like, and why the exact transient is printed beside the run.

@chapter Batch means
@art batches
To get an interval from one run, use batch means. Discard the warm up, split the rest into equal batches, and treat each batch mean as a replication. At seed zero, four batches of seventy five give one point three six, one point five five, point seven six, and five point nine six.

@words text="Average 361/150 · variance ≈ 5.72"
Their average is within point oh oh seven of twelve fifths. Their sample variance is about five point seven two. The point estimate couldn't be better, and the spread says the run has established almost nothing. Print both. And batches only work if they're long enough to forget each other.

@chapter Where people slip
@list heading="Common slips" items="Averaging from slot zero@The first|Fixing bias by running longer@The second|Building an interval from single slots@And the third"
The first slip is averaging from slot zero because that's where the run starts. The second is fixing bias only by running longer, the expensive way round. And the third is building an interval from the slots of one run, which are strongly dependent, so the interval is confidently narrow and wrong.

@chapter Try it
@words text="E[N₄] = 17/20" sub="push the distribution one more slot"
Your turn. Starting from the distribution after three slots, push it forward one more slot, departure first, then arrival. Check that the expected number in system comes out at seventeen twentieths.

@end text="Throw the beginning away"
You can move the warm up and watch the exact bias shrink, on Learn. That's learn dot get er done dot I O.
