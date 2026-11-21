---
format: long
lesson: caching-and-hit-rates/popularity-is-skewed
title: Zipf popularity: why a tiny cache serves most of your traffic
thumb: 10% of keys, 90% of requests
---

@chapter The question
@title text="Popularity Is Skewed" sub="Caching and Hit Rates" art=thumb
A cache can only hold a small fraction of your data. So surely it can only serve a small fraction of your requests? That's the most common wrong idea about caching, and you can disprove it by adding fractions.

@art uniform-bars
If every key were equally popular, a cache holding a tenth of the keys would serve a tenth of the requests. But requests aren't spread evenly. A few keys get most of them.

@chapter The Zipf law
@art rank-curve
Sort the keys from most to least requested. Under a Zipf law, the key of rank i is requested in proportion to one over i to the s, where s is the exponent. So at s equals two, rank two gets a quarter of what rank one gets, and rank ten gets a hundredth.

@math heading="Zipf popularity" items="p_i = (1/iˢ) / H(N, s)@the key of rank i;;H(N, s) = 1 + 1/2ˢ + 1/3ˢ + … + 1/Nˢ@the generalised harmonic;;s = 0  →  p_i = 1/N@s equals zero"
The probability for the key of rank i is one over i to the s, divided by H of N and s, the generalised harmonic number, which just adds up every term. And s equals zero makes every key equally likely.

@words text="Measured workloads: s ≈ 0.7 to 1.2" sub="an empirical regularity, not a theorem"
Measured web and key value workloads usually land between about point seven and one point two. Two assumptions sit underneath: the law itself, which is observed, not proven, and a ranking that stays stable over your window.

@chapter The top k share
@math heading="The share of the top k keys" items="Σ p_i (i = 1…k) = H(k, s) / H(N, s)@Add up the first;;s = 0:  H(k, 0)/H(N, 0) = k/N@uniform"
Given the law, everything else is addition. Add up the first k probabilities, and the normaliser cancels down to a ratio of two harmonic sums, H of k over H of N. Under uniform popularity, that ratio is just k over N.

@chapter Fifty keys at s equals two
@math heading="N = 50, s = 2" items="H(5, 2) = 1 + 1/4 + 1/9 + 1/16 + 1/25@The top five give;;= 5269/3600@fifty two sixty nine;;H(50, 2) ≈ 1.625133@divide by;;share = H(5, 2)/H(50, 2) = 90.06%@ninety point oh six"
Take fifty keys at s equals two. The top five give one plus a quarter plus a ninth plus a sixteenth plus a twenty fifth, which is fifty two sixty nine over thirty six hundred. Divide by H of fifty and two, about one point six two five, and the top five carry ninety point oh six percent.

@art head-shaded
Five keys out of fifty, a tenth of the catalogue, carry ninety percent of the requests. One key alone, two percent of the catalogue, carries sixty one point five three percent. Under uniform popularity, those would be ten percent and two percent.

@chapter The multiple
@math heading="Better than proportional" items="top 5:  90.06% / 10% = 9.01×@nine point oh one;;top 1:  61.53% / 2% = 30.77×@thirty point seven seven;;s = 0:  1× for every k@at s equals zero"
Divide the share by k over N and you get how much better than proportional you're doing. Nine point oh one times for the top five. Thirty point seven seven times for the top one. And at s equals zero, it's one for every k.

@art diminishing-tail
That multiple shrinks as k grows. The first key is worth thirty times its weight, and the fiftieth is worth almost nothing. That shape is what decides how big a cache should be.

@chapter Exact, until it isn't readable
@art bracket
Every H is a finite sum of fractions, so it's exact. But H of fifty and two has forty three digits on top and bottom, so past fifty keys the lab shows a rounded value with a tilde. Real exponents are fractional, so bracket them: compute at s equals one and s equals two, and report the interval.

@chapter Where people slip
@list heading="Common slips" items="Assuming uniform popularity@The first|Putting the exponent on the wrong thing@The second|Taking N as the size of the database@The third"
The first slip is assuming uniform popularity, cache ten percent, get ten percent. That's exactly s equals zero. The second is putting the exponent on the wrong thing. It's the rank that's raised, so check H of three and two is forty nine thirty sixths. The third is taking N as the database size. N is the distinct keys your window touches.

@art key-window
A ten million row table read by forty thousand distinct keys a day has N of forty thousand for a daily cache. Use ten million, and every cache looks pointless.

@chapter Try it
@words text="N = 20, s = 1" sub="H(20, 1) = 55835135/15519504"
Your turn. Twenty keys at s equals one. You're given H of twenty and one. Compute the share carried by the top two keys, a tenth of the catalogue, and report it as a multiple of k over N. Then say what both numbers become at s equals zero, and why.

@end text="Set s to zero and watch the lines meet"
You can drag the exponent and watch the top keys' share pull away from the uniform line, on Learn. That's learn dot get er done dot I O.
