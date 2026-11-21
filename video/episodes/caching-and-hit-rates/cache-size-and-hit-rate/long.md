---
format: long
lesson: caching-and-hit-rates/cache-size-and-hit-rate
title: Cache size and hit rate: what the next nine costs
thumb: 90% costs 5, 99% costs 28
---

@chapter The question
@title text="Cache Size and Hit Rate" sub="Caching and Hit Rates" art=thumb
How big does a cache need to be? The usual answer is a guess at how much of the data is hot. There's a better answer, and it comes from the popularity curve you already have.

@art top-c-keys
Suppose the cache holds exactly the C most popular keys. A request hits when its key is in the top C. So the hit rate is the share of requests those C keys carry.

@chapter The curve
@math heading="Hit rate of the top C keys" items="h(C) = H(C, s) / H(N, s)@h of C;;h(0) = 0 · h(N) = 1@zero;;each key adds p_{C+1}, and they shrink@each additional key"
That's the same ratio of harmonic sums as before, read as a function of C. H of C over H of N. It starts at zero and ends at one. And each additional key adds its own probability, which is smaller than the last, so the increments shrink.

@art concave-curve
So the curve rises steeply, then flattens. And there's an assumption inside it worth naming. It assumes the cache holds the right C keys. No real policy knows which those are, so this is a ceiling, not a promise.

@chapter Inverting the curve
@words text="Add probabilities in rank order" sub="stop when the running total crosses the target"
To find the smallest cache for a target, add probabilities in rank order until the running total crosses it. There's no closed form for this. You just scan, over exact fractions, so the answer is truly the smallest.

@math heading="N = 50, s = 2" items="C = 1  →  61.533%@one key;;C = 2  →  76.917% · C = 3  →  83.754%@two keys;;C = 4  →  87.600%@four;;C = 5  →  90.061%  ← first ≥ 90%@five keys"
With fifty keys at s equals two, one key gives sixty one point five three three percent. Two keys give seventy six point nine, three give eighty three point eight. Four give eighty seven point six, and five keys give ninety point oh six one. That's the first to cross ninety.

@chapter The price of a nine
@math heading="Each target, N = 50, s = 2" items="90%  →  C = 5   (10% of the catalogue)@ninety percent;;95%  →  C = 10@ninety five;;99%  →  C = 28   (56%)@ninety nine;;99.9%  →  C = 47@ninety nine point nine"
Keep scanning. Ninety percent costs five keys, a tenth of the catalogue. Ninety five costs ten. Ninety nine costs twenty eight, more than half. And ninety nine point nine costs forty seven, out of fifty.

@art stretched-gap
From ninety to ninety nine, the cache goes from five keys to twenty eight. That's twenty three more keys, five point six times the memory. And past ninety nine, you're not really caching anymore. You're copying.

@words text="5 keys: load ÷ 10 · 28 keys: load ÷ 100"
But look at what you bought. Five keys cut the backend load by a factor of ten. Twenty eight cut it by a hundred. Whether that's a good deal depends on what the backend was doing at the higher load.

@chapter Choose the target first
@art memory-blocks
An earlier course sized a cache by assuming ten percent of the data is hot. That was a serviceable estimate, and an assumption. Here the hot fraction is a result. At fifty keys and s equals two, that ten percent happens to deliver ninety point oh six one percent. That's luck, not a law.

@art target-line
So run the procedure the right way round. Measure the skew. Choose the hit rate you need from what the backend can take. Then let the curve tell you the cache size. If the skew is unknown, bracket it: compute the size at s equals one and s equals two, and carry both.

@art two-curves
One caution. The flat end says the last nine is expensive in memory. It doesn't say it's worthless. On the backend side, that same nine is a tenfold cut in load every time. Read both curves together.

@chapter Where people slip
@list heading="Common slips" items="Scaling the hit rate with the cache size@The first|Sizing the cache before choosing the target@The second|Treating an assumed hot fraction as a measurement@The third"
The first slip is scaling the hit rate with the cache size. Ten keys give ninety five point three six three percent, not twice ninety. The second is sizing the cache before choosing the target, which comes from lambda and mu. The third is treating an assumed hot fraction, like ten percent, as a measurement. It's a consequence of the skew.

@chapter Try it
@words text="N = 50, s = 1" sub="find C for 90% and for 99%"
Your turn. Keep fifty keys, but set s to one. The head is much flatter, so every target costs more. Find the cache size for ninety and for ninety nine percent, and the ratio between them. Then say how confident you can be in a cache size when s is only known to within a point.

@end text="Move the skew, watch the gap grow"
You can drag the target and the skew and watch the required cache size move, on Learn. That's learn dot get er done dot I O.
