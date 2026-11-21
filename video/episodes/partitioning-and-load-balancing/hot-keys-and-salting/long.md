---
format: long
lesson: partitioning-and-load-balancing/hot-keys-and-salting
title: Hot keys: why a thousand shards won't save you
thumb: More shards can't split one key
---

@chapter The hot key
@title text="Hot Keys and Salting" sub="Partitioning and Load Balancing" art=thumb
One key is getting twelve percent of all your traffic. The usual instinct is to add shards. Here's why that barely helps, and what does.

@art hot-key-shard
A hot key is a single key that gets a disproportionate share, f, of the traffic. Every partitioning function maps one key to one shard. So all of f times lambda lands on one node, however you choose the function, and however many shards there are.

@math heading="The hottest shard" items="hottest = f·λ + (1 − f)·λ/N@the hottest shard;;f·λ  has no N in it@has no N;;(1 − f)·λ/N → 0  as N grows@goes to zero"
So the hottest shard carries f times lambda, plus one minus f, times lambda over N. The first term has no N in it. Only the second term shrinks as N grows, and it goes to zero, leaving the first exactly where it was.

@chapter Resharding hits a floor
@math heading="λ = 100 000 /s,  f = 12%" items="floor = f·λ = 12 000 /s@twelve thousand;;N = 16:  hottest 17 500 /s,  2.80 × mean@at sixteen shards;;N = 1 024:  hottest 12 086 /s,  123.76 × mean@at a thousand and twenty four"
Take a hundred thousand requests a second with f at twelve percent. The floor is twelve thousand. At sixteen shards, the hottest shard takes seventeen thousand five hundred, two point eight times the mean. At a thousand and twenty four shards, it takes twelve thousand and eighty six.

@art floor-asymptote
Sixty four times the shards bought a thirty one percent reduction. And of those twelve thousand and eighty six, twelve thousand is the hot key, and eighty six is everyone else. Every further shard buys a slice of the eighty six. It's a curve falling toward a line it never meets.

@art many-shards-same-hot
Meanwhile the imbalance goes the other way, from two point eight times the mean to a hundred and twenty three point seven six, because the mean collapses and the hot shard doesn't. And if f times lambda is already above one node's capacity, no shard count is a solution.

@chapter Salting
@art salt-split
What works is splitting the key itself. Salting replaces it with s derived keys, key hash zero through key hash s minus one, picking a suffix at random on each write. Those are s distinct keys, so they hash to s different places.

@math heading="Salt into s = 8, back at N = 16" items="hot term = (0.12 / 8) × 100 000 = 1 500 /s@fifteen hundred;;hottest = 1 500 + 5 500 = 7 000 /s@seven thousand;;mean = 6 250 /s,  so 1.12 × mean@against a mean"
The hot term becomes f over s, times lambda, fifteen hundred a second. Add the five thousand five hundred of everyone else, and the hottest shard holds seven thousand, against a mean of six thousand two hundred and fifty. Eight salt pieces bought sixty percent, and left the fleet alone.

@chapter What it costs
@art read-fanout
The price is paid on reads. A read of the salted key has to fetch all eight pieces and combine them. So a read of that key is eight times as expensive, and waits for all of them.

@math heading="Two read multipliers" items="a read of the hot key:  × s = × 8@read of the hot key;;reads overall:  1 − f + f·s = 0.88 + 0.96 = 1.84@one point eight four"
So a read of the hot key costs times eight. Across the whole read stream, only the hot key fans out, so the multiplier is one minus f plus f times s, which is one point eight four. Both are true. The first sizes the latency of a read of that key. The second sizes the fleet.

@words text="s = 4:  within 1.5 × mean,  reads × 1.36" sub="s = 16:  exactly the mean,  reads × 2.80"
Choose s from a target. A salt of four already brings the hottest shard within one point five times the mean, at a read multiplier of one point three six. Sixteen reaches the mean exactly, at two point eight. The last bits of balance are the expensive ones.

@chapter When not to salt
@art cache-in-front
Salting has a running cost. If the hot key is read far more than it's written, a cache in front of it removes the load and doesn't touch the partitioning. If one client makes it hot, a rate limit is cheaper. Salt when the traffic is write heavy on a key that really has to be one key.

@list heading="Common slips" items="Answering a hot key with more shards@The first|Quoting only the fleet-wide read multiplier@The second|Salting a read-heavy key@the third"
The first slip is answering a hot key with more shards. The second is quoting only the fleet wide read multiplier, when a read of that key does eight requests. And the third is salting a key that's read far more than it's written.

@chapter Try it
@words text="f = 30%,  λ = 100 000 /s,  N = 16" sub="first move: floor = 30 000 /s"
Your turn. Take f to thirty percent, same traffic, sixteen shards. The floor is thirty thousand. Work out the hottest shard now and at a thousand and twenty four shards, then the salt that gets within one point five times the mean, and both read multipliers it costs.

@end text="Measure f before you reshard"
You can move f and the salt and watch the hottest shard, on Learn. That's learn dot get er done dot I O.
