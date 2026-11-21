---
format: long
lesson: capacity-estimation/memory-and-the-working-set
title: Sizing a cache: the working set and the knee
thumb: Find the knee first
---

@chapter The question
@title text="Memory and the Working Set" sub="Capacity Estimation" art=thumb
You have five terabytes of data and you want a cache. Do you need five terabytes of memory? Nobody buys that. You size memory to the part of the data the traffic actually touches, and the question isn't whether the data fits. It's how many of the reads do.

@art memory-chip
You can't afford a cache the size of the data. So the real question is what a much smaller one buys you.

@art hot-region
The working set is the part of the data the traffic touches over a window. Say a hot fraction f of the bytes takes a share s of the reads. If reads were spread evenly, caching a tenth of the data would buy a tenth of the hits. Skew is the whole business case for caching.

@chapter The hit rate curve
@math heading="Caching a fraction c" items="c ≤ f:  h(c) = s · c/f@inside the hot region;;c > f:  h(c) = s + (1 − s)(c − f)/(1 − f)@past the knee"
Cache a fraction c of the data, and the hit rate h comes in two straight pieces. Inside the hot region, h is s times c over f. Past the knee, h is s plus one minus s, times c minus f over one minus f.

@art knee-curve
Both pieces are straight lines, and they meet at the point f, s. That's the knee, and the knee is where the budget gets decided.

@art two-slopes
With f at ten percent and s at ninety, the first slope is nine. Each point of cached data buys nine points of hit rate. The second slope is one ninth. That's a factor of eighty one in the price of a hit, and it changes at a single point.

@chapter A worked example
@math heading="5 TB of timelines · f = 10% · s = 90%" items="target h = 80% ≤ s@eighty percent;;c = 0.1 · 80/90 = 4/45 = 8.89%@four over forty five;;5 TB · 4/45 = 444.44 GB@four hundred and forty four"
Five terabytes of timelines, ten percent of it taking ninety percent of the reads. You want eighty percent hits. That's inside the hot region, so c is zero point one times eighty over ninety, which is four over forty five, eight point eight nine percent. That's four hundred and forty four point four four gigabytes.

@art small-cache
Less than half a terabyte of memory serves four reads in five from a five terabyte store. That ratio, not the absolute figure, is why caches exist.

@chapter What the last points cost
@math heading="Past the knee" items="whole hot region: 500 GB → 9/10@five hundred gigabytes;;h = 95%:  c = 0.1 + 0.9 · 0.05/0.10 = 11/20@ninety five;;5 TB · 11/20 = 2.75 TB@two point seven five"
Caching the whole hot region costs five hundred gigabytes and gives nine tenths of the reads. Now ask for ninety five percent. That's past the knee, so c is zero point one plus zero point nine times zero point zero five over zero point one, which is eleven twentieths. That's two point seven five terabytes.

@art cold-region
The first ninety points of hit rate cost half a terabyte. The next five cost more than four times that again, because they're bought from the cold region, where reads are spread thinly over lots of bytes. A team that asks for ninety nine percent because it sounds rigorous has usually asked for the whole dataset.

@chapter What the model assumes
@list heading="Assumptions" items="Every key in a region equally popular@every key|f and s measured over a window@measured over"
The model assumes every key inside each region is equally popular, which is what makes the two pieces straight. That's not true of any real workload, but it gets the two structural facts right: a small cache buys a large hit rate, and there's a knee. And f and s are measured over a window. They move with releases, imports, and stories everyone reads at once.

@chapter Where people slip
@list heading="Common slips" items="Treating caching as all or nothing@The first|Pricing the last points like the first@The second|Taking the hot fraction as fixed@The third"
The first slip is treating caching as all or nothing. The second is assuming the last points of hit rate cost what the first did. And the third is taking the hot fraction for a property of the data, when it's a fact about traffic.

@chapter Try it
@words text="200 GB · 5% hot takes 75% of reads · target 95%" sub="95% > 75%: past the knee"
Your turn. A two hundred gigabyte catalogue, with five percent of it taking seventy five percent of the reads, and a target of ninety five percent. Ninety five is more than seventy five, so you're past the knee. Work out the fraction, the gigabytes, and what caching just the hot region would buy.

@end text="Find the knee, then pick a target"
You can move the hot fraction and the target and watch the knee, on Learn. That's learn dot get er done dot I O.
