---
format: long
lesson: storage-engines-and-indexes/the-rum-trade-off
title: The RUM trade-off: pick two amplifications, pay in the third
thumb: Choose two, pay in the third
---

@chapter Three amplifications
@title text="The RUM Trade-off" sub="Storage Engines and Indexes" art=thumb
Which storage engine is best? There's no answer to that, and here's why. Every engine has three costs, and you can't make all three small at once.

@list heading="Three ratios" items="Read amplification@Read amplification|Update amplification@Update amplification|Memory amplification@Memory amplification"
Read amplification is the storage reads one lookup performs. Update amplification is the bytes written per byte ingested. Memory amplification is the bytes stored per byte of unique data. Every engine has all three.

@art rum-triangle
The RUM conjecture says no engine minimises all three. Levelled trees, tiered trees and B-trees sit at three corners of the same triangle. Each is best at something and pays for it somewhere else.

@words text="Memory amplification = disk space" sub="not RAM"
One warning about the name. Memory amplification is about space, not RAM. A memory amplification of ten means ten copies of a key on disk, and ten times the storage bill.

@chapter Two LSM shapes
@art levelled-runs
Take a fanout of ten and five levels. A levelled tree merges each incoming run into the level below straight away. So each level holds one sorted run, and a lookup probes five of them. But it rewrites each byte about five times per level, twenty five in all. Memory amplification is one plus one over F, eleven tenths.

@art tiered-runs
A tiered tree lets runs pile up and merges ten at once. So it writes each byte once per level, five times in all. But a lookup now has ten runs to search on every level, fifty probes, and it keeps up to ten copies of a key. Read and update almost exactly swap places.

@chapter The B-tree corner
@math heading="B-tree:  10⁹ keys,  B = 500" items="read = height = 4@is the height;;update = 4 000 / 128 = 125/4 = 31.25@thirty one point two five;;memory = 1 / (2/3) = 3/2@three halves"
Nothing in the B-tree row is looked up. Read amplification is the height, four for a billion keys at a fanout of five hundred. Update amplification is page over row. Writing a four thousand byte page to change a hundred and twenty eight byte row is thirty one point two five. And memory is one over the fill factor, pages about two thirds full, so three halves.

@art page-for-row
That's where the B-tree pays. It reads the least, but it rewrites a whole page to change one small row.

@art fill-factor
And it stores a little extra, because its pages keep room to grow.

@chapter The bandwidth question
@math heading="Ingest 50 MB/s × update amplification" items="levelled:  25 × 50 = 1.25 GB/s@one point two five;;tiered:  5 × 50 = 250.00 MB/s@two hundred and fifty;;B-tree:  31.25 × 50 = 1.56 GB/s@one point five six"
Now the number a device is chosen against. Sustained write bandwidth is ingest times update amplification. At fifty megabytes a second in, the levelled tree needs one point two five gigabytes a second, the tiered tree two hundred and fifty megabytes, and the B-tree one point five six gigabytes.

@art three-pipes
None of those is fifty megabytes a second. A device sized to the ingest rate is short by between five and thirty one times. And it doesn't fail at once. It falls behind, and read amplification climbs too.

@chapter Using the triangle
@words text="Name the cost you can't afford" sub="then read the other two"
So don't rank the corners. Name the amplification your workload can't afford, and then read what the other two cost. A write heavy pipeline that's rarely queried can live at the tiered corner. A point lookup service on expensive storage can't afford a memory amplification of ten.

@words text="Ratios compare shapes, not products"
And these are ratios. Compression moves memory amplification and nothing else. A block cache changes the reads you observe, not the engine's. And a real implementation can be twice as good or bad as its shape at every corner.

@chapter Where people slip
@list heading="Common slips" items="Sizing a device to the ingest rate@The first|Reading the triangle as a ranking@The second|Reading memory amplification as RAM@the third"
The first slip is sizing a device to the ingest rate. The second is reading the triangle as a ranking. Saying tiered engines are write optimised is true and useless without the two prices. And the third is reading memory amplification as RAM.

@chapter Try it
@words text="F = 4,  L = 5" sub="first move: levelled update = 10"
Your turn. Drop the fanout to four and keep five levels. The levelled update amplification falls to ten. Work out all three triples, say which engine moved most and which didn't move at all, then the three bandwidths at fifty megabytes a second.

@end text="Choose two, pay in the third"
You can move the fanout and watch all three engines, on Learn. That's learn dot get er done dot I O.
