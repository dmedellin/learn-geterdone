---
format: long
lesson: partitioning-and-load-balancing/the-power-of-two-choices
title: The power of two choices: one extra look, a much flatter fleet
thumb: Look twice, pick the lighter
---

@chapter The setup
@title text="The Power of Two Choices" sub="Partitioning and Load Balancing" art=thumb
Here's one of the best bargains in systems design. One extra lookup per placement, and the fullest bin drops sharply. And it becomes much more predictable, too.

@art one-choice-pile
Put m keys into n bins, and look at the fullest bin. The clean case is m equals n, so the mean is exactly one key a bin. Any maximum above one is pure imbalance. A maximum of five means the fullest bin holds five times what an even placement would give it.

@art two-probes
The rule is simple. Instead of hashing a key to one bin and placing it there, pick d bins at random, look at how full each one is, and put the key in the least full. At d equals two, that's one extra lookup, and no coordination between placements.

@chapter The measurement
@art same-stream
The lab runs both rules from the same stream of random draws. That matters. Seed to seed, the one choice maximum moves between five and six, which is the same size as the effect, so comparing across seeds could show almost anything.

@math heading="1 024 keys into 1 024 bins" items="seed 3:  one choice max 5,  two choices max 3@seed three;;seeds 3 to 10, one choice:  5 5 5 5 5 6 6 5,  mean 5.25@one choice gave;;seeds 3 to 10, two choices:  3 3 3 3 3 3 3 3,  mean 3.00@two choices gave"
With a thousand and twenty four keys and bins, seed three gives a fullest bin of five under one choice, and three under two choices. Over seeds three to ten, one choice gave five or six, averaging five point two five. Two choices gave three, on every single seed.

@words text="Lower, and less variable" sub="5.25 → 3.00, a factor of 1.75"
So the rule doesn't just lower the maximum, by a factor of one point seven five here. It makes it far less variable, which is what a capacity plan actually wants.

@art two-choice-level
It shows in the empty bins too. On seed three, one choice left three hundred and seventy seven bins empty. Two choices left two hundred and forty three, because a key that would have piled onto a busy bin went to a quieter one.

@chapter Stated rates
@art log-log-curves
There are famous results here. One choice gives a maximum growing like log n over log log n. Two choices give something growing like log log n, a logarithm of a logarithm. Both are stated, not proved, anywhere in this library, because the proofs need Chernoff bounds.

@math heading="At n = 1 024, rounded" items="one choice:  ln n / ln ln n = 3.58  stated@three point five eight;;measured mean 5.25@five point two five;;two choices:  ln ln n = 1.94  stated@one point nine four"
At a thousand and twenty four, log n over log log n is about three point five eight, but the measured maximum averaged five point two five. Log log n is about one point nine four. These don't contradict each other. A growth rate drops its constants. It says how the maximum scales, not what it equals.

@words text="Rate for growth, measurement for provisioning"
So use the rate to answer what happens when the fleet is ten times bigger. Use the measurement to answer what you provision now. A plan built on three point five eight is short by a third.

@chapter Why not scan every bin?
@words text="The first extra look is nearly all of it"
Scanning every bin would be a little better. But the gain is nearly all in the first extra look. A full least loaded search needs every bin's load right now, which means a central allocator or a global view that's stale by the time you use it. A stale view herds new keys onto whichever bin looked emptiest.

@art balancer-two-backends
The same arithmetic runs a load balancer. Sample two backends, and send the request to the one with fewer outstanding requests. You get most of the benefit of least loaded balancing, with none of the coordination.

@chapter Where people slip
@list heading="Common slips" items="Quoting an asymptotic as a capacity figure@The first|Assuming you need a full least-loaded search@The second|Comparing the rules on different seeds@the third"
The first slip is quoting an asymptotic as a capacity figure. The second is believing the result needs a full least loaded search. And the third is comparing the two rules on different seeds.

@chapter Try it
@words text="n = 4 096,  d = 2" sub="stated: 3.93 and 2.12"
Your turn. Take n to four thousand and ninety six and reseed four times. The stated rates there are three point nine three and two point one two. Record both measured maxima, say how much each moved from a thousand and twenty four, and label every figure as measured or stated.

@end text="One extra look"
You can run both rules from the same stream and reseed, on Learn. That's learn dot get er done dot I O.
