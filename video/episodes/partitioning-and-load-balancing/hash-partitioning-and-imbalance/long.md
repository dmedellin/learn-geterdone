---
format: long
lesson: partitioning-and-load-balancing/hash-partitioning-and-imbalance
title: Hashing spreads keys uniformly, not evenly
thumb: Uniform is not equal
---

@chapter The claim
@title text="Hash Partitioning and Imbalance" sub="Partitioning and Load Balancing" art=thumb
Everybody says hashing spreads keys evenly across shards. It doesn't, quite. It spreads them uniformly at random, and that's a different sentence. The gap between the two is what a capacity plan has to be built on.

@art scattered-keys
Under hash partitioning, a key k goes to shard h of k, mod N. Keys that sit near each other in the key space get scattered, so range scans get expensive, but the placement stops depending on what the keys mean.

@words text="Uniform ≠ equal" sub="no shard favoured, but one is still fuller"
Uniform means no shard is favoured. It doesn't mean no shard is fuller. The occupancy of a shard is how many keys landed on it, and its mean over the fleet is m over N, whatever the hash does.

@chapter One placement
@art uneven-bins
The lab uses a seeded generator printed on the page, so random is reproducible. Put twelve hundred keys into twelve shards with seed seven, and count what lands where.

@math heading="1 200 keys, 12 shards, seed 7" items="mean = 1 200 / 12 = 100@exactly a hundred;;fullest = 122,  emptiest = 82@a hundred and twenty two;;max/mean = 122 × 12 / 1 200 = 61/50 = 1.220@sixty one over fifty;;excess = 122 − 100 = 22 = 2.20 √mean@twenty two keys"
The mean is exactly a hundred. The fullest shard holds a hundred and twenty two, and the emptiest eighty two. Max over mean is a hundred and twenty two times twelve over twelve hundred, which is sixty one over fifty, one point two two. And the excess is twenty two keys, or two point two times the square root of the mean.

@words text="max/mean is a ratio of counts" sub="nothing to approximate"
Notice that max over mean is a fraction of whole numbers. Nothing to model. You'd get the same figure counting the placement by hand.

@chapter One seed is one sample
@art reseed-dice
That one point two two is a single draw. Across seeds seven through fourteen, with the same keys and shards, the fullest shard ran from a hundred and twelve to a hundred and twenty two. Max over mean averaged one point one seven, and the worst was one point two two.

@chapter The square root term
@art ratio-shrinks
Now add keys. With twelve thousand keys, max over mean came out at one point oh four six. With a hundred and twenty thousand, one point oh one eight. It's tempting to say the imbalance is going away.

@art excess-grows
It isn't. It's being divided by a bigger mean. The excess over the mean went from twenty two keys, to forty six, to a hundred and eighty two, as the mean went from a hundred to a thousand to ten thousand. That grows like the square root of the mean.

@math heading="Excess in units of √mean" items="mean 100:  2.20 √mean@two point two;;mean 1 000:  1.45 √mean@one point four five;;mean 10 000:  1.82 √mean@one point eight two"
So the lab prints the excess in units of root mean. Measured that way, it stays a small number of order one: two point two, one point four five, and one point eight two. Noisy, but of a fixed size.

@chapter What it costs
@art over-bought
Provision every shard for the mean, and the fullest one is twenty two percent over. Provision every shard for the fullest, and eleven of the twelve are over bought. The usable answer is to size on a maximum you measured across several seeds, one point one seven on average and one point two two at worst here.

@words text="Θ(log n / log log n)" sub="stated, not proved"
There's a known result for when keys equal shards: the maximum grows like log n over log log n. The lesson states it and doesn't prove it. Keep three statuses apart. The mean is exact. A measured maximum is reproducible. The growth rate is stated.

@chapter Where people slip
@list heading="Common slips" items="Reading uniform as equal@The first|Quoting one placement@The second|Trusting a falling max/mean@And the third"
The first slip is reading uniform as equal. The second is quoting an imbalance from a single placement, which is a draw, not a property. And the third is treating a falling max over mean as a disappearing problem, when the excess actually grew.

@chapter Try it
@words text="12 000 keys · 12 shards" sub="first move: mean = 1 000"
Your turn. Keep twelve shards and take the keys to twelve thousand. The mean is a thousand. Predict whether max over mean gets closer to one, then read the fullest shard off the lab, and work out max over mean and the excess in root means. Which figure told you something about the hash? Reseed three times first.

@end text="Reseed and watch the max move"
You can reseed the placement and watch the fullest shard move, on Learn. That's learn dot get er done dot I O.
