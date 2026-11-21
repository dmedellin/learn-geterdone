---
format: long
lesson: scaling-laws-and-cost/storage-tiers
title: Storage tiers: when cold storage costs more than hot
thumb: Tier by rate, not by age
---

@chapter Cheap to keep, dear to read
@title text="Storage Tiers" sub="Scaling Laws and Cost" art=thumb
Archive anything older than thirty days. It sounds like an obvious saving. It can triple the bill for the data you move, and the rule that works is about how often data is read, not how old it is.

@art two-tiers
A cold tier is cheaper to keep and dearer to read. Call the hot price h, and the cold price c, both per gigabyte month. And t is the retrieval charge, per gigabyte read back from cold. Here c is a price, never a count of servers. So the real question is how often a gigabyte gets read.

@art saving-vs-reads
Moving a gigabyte cold saves h minus c every month. But every read costs t. One is monthly, the other per access, and setting them equal gives a rate.

@math heading="Break-even access rate" items="a* = (h − c) / t@a star;;(0.023 − 0.004) / 0.010 = 19/10@nineteen tenths;;= 1.9 reads a GB-month@one point nine"
That's a star, h minus c over t. At two point three cents hot, point four cold, and one cent to read back, it's nineteen tenths, one point nine reads per gigabyte a month. Read more than that, and cold costs more than hot.

@words text="a* has no volume in it"
And the break even is per gigabyte. It's the same for a terabyte and a petabyte. Volume decides how much the choice is worth, not which way it goes.

@chapter Age is a proxy
@art decay-steps
Data is tiered by age because reads usually fall with age. Here reads start at eight per gigabyte a month and halve every month: eight, four, two, one.

@math heading="Per 1 000 GB bucket" items="m 2:  2 reads,  hot $23.00  vs  cold $4.00 + $20.00 = $24.00@month two;;m 3:  1 read,  hot $23.00  vs  cold $4.00 + $10.00 = $14.00@month three"
Compare against one point nine at each month. Month two, two reads, still above. A thousand gigabytes costs twenty three dollars hot, and twenty four cold. Month three, one read, below. Twenty three hot against fourteen cold. So the boundary is month three.

@words text="Count, don't take a logarithm"
That's found by evaluating each integer age, not by taking a logarithm. A log would give two point oh seven, and then you'd have to argue which way to round. Comparing exact numbers needs no argument.

@chapter The whole archive
@art monthly-buckets
The archive keeps twenty four monthly buckets of a thousand gigabytes each, twenty four thousand in all.

@math heading="24 000 GB" items="all hot:  24 000 × $0.023 = $552.00@all hot;;tiered at month 3:  $69.00 + $84.00 + ≈$20.00 = $173.00@tiered at month three;;saving $379.00 a month@three hundred and seventy nine"
All hot, five hundred and fifty two dollars a month. Tiered at month three: three hot buckets at sixty nine dollars, twenty one cold buckets at eighty four, and about twenty dollars of retrieval. A hundred and seventy three in all. That saves three hundred and seventy nine a month, by moving twenty one thousand gigabytes.

@chapter Two ways to get it wrong
@art too-early
Moving too early is the expensive one. The newest bucket, read eight times a gigabyte, costs eighty four dollars cold against twenty three hot. Tiering it more than triples its bill. That's what archive after thirty days does to data whose reads haven't decayed yet.

@art too-late
Moving too late is cheap and dull. Leaving the oldest bucket hot costs twenty three dollars instead of four, nineteen a month. It never causes an incident, which is why it survives for years.

@words text="Retrieval latency is a constraint, not a cost"
And one thing isn't priced at all: how long a restore takes. If the data has a deadline and the cold tier answers in hours, it may be unusable at any price. Check that first, before any of this arithmetic.

@chapter Where people slip
@list heading="Common slips" items="Tiering by age without checking the rate@The first|Computing the saving from storage prices alone@The second|Reading c as a machine count@the third"
The first slip is tiering by age without checking the access rate. The second is computing the saving from storage prices alone, leaving out retrieval. And the third is reading c as a count of machines. Here it's a price.

@chapter Try it
@words text="Reads fall to 70% each month" sub="does a* move?"
Your turn. Slow the decay, so reads fall to seventy percent of the previous month instead of fifty. Predict first whether a star moves. Then find the new boundary age by evaluating the profile, and read the new saving off the lab.

@end text="Below a*, go cold"
You can move the prices and the decay and watch the boundary, on Learn. That's learn dot get er done dot I O.
