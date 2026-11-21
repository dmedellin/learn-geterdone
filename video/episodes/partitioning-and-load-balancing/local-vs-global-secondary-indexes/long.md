---
format: long
lesson: partitioning-and-load-balancing/local-vs-global-secondary-indexes
title: Local or global index? It's one division
thumb: Crossover at 1/(N − 1)
---

@chapter Two placements
@title text="Local vs Global Secondary Indexes" sub="Partitioning and Load Balancing" art=thumb
You've partitioned a table by one key, and now you need to look rows up by something else. You need a secondary index, and there are two places to put it. The question is where it lives, and the answer is a calculation.

@art local-index
A secondary index maps a non key attribute to the rows that carry it. A local index lives beside its data. Each shard indexes only its own rows. So a write touches one shard. But a lookup has no idea which shards hold matches, so it asks all N.

@art global-index
A global index is partitioned by the indexed attribute, so all entries for one value live together. A lookup goes straight to the one shard holding that value's entries.

@art double-write
The price is on the write. A write now touches two shards, the row's own and the index's, on different machines.

@chapter Count both costs
@math heading="Shard operations a second" items="local = r·N + w@local index costs;;global = r + 2w@global index costs"
Count both in the same unit, shard operations a second, where a read to sixteen shards counts as sixteen. With r indexed reads, w writes and N shards, the local index costs r times N plus w. The global index costs r plus two w.

@math heading="r = 5 000 /s,  w = 2 000 /s,  N = 16" items="local = 5 000 × 16 + 2 000 = 82 000 ops/s@eighty two thousand;;global = 5 000 + 4 000 = 9 000 ops/s@nine thousand;;82 000 / 9 000 = 9.11×@nine point one one"
Take five thousand indexed reads and two thousand writes a second on sixteen shards. The local index costs eighty two thousand operations a second. The global index costs nine thousand. The global index wins by nine point one one times.

@chapter Where they cross
@art cost-lines
Now set the two equal and solve. That gives you the read to write ratio where the answer flips.

@math heading="The crossover" items="r·N + w = r + 2w@Set r N plus w;;r(N − 1) = w@r times N minus one;;r/w = 1/(N − 1)@one over N minus one"
Set r N plus w equal to r plus two w. Move things across, and r times N minus one equals w. So the designs cost the same when r over w is one over N minus one. It depends only on N.

@art crossover-shrinks
At two shards, the crossover is one: equal reads and writes, a real decision. At sixteen, it's one fifteenth. At sixty four, one sixty third, so any workload that reads the index at all is past it. The bigger the fleet, the smaller the read share that tips it to global.

@math heading="When does local win?" items="crossover at N = 16:  1/15 = 0.0667@one fifteenth;;this workload:  r/w = 2.500@two point five;;local wins only if r < 2 000/15 = 133 /s@a hundred and thirty three"
Our workload is two point five, far above one fifteenth. Hold the writes and the shards, and the local index wins only if indexed reads fall below a hundred and thirty three a second. That's a conclusion with a margin attached.

@chapter The other side of the line
@words text="audit log:  w = 10 000 /s,  r = 200 /s,  N = 4" sub="local 10 800  ·  global 20 200"
Here's a workload that goes the other way. An audit log with ten thousand writes a second and two hundred status lookups, on four shards. The local index costs ten thousand eight hundred, and the global costs twenty thousand two hundred. Local wins by nearly two to one, because point oh two is well below one third.

@chapter What the ratio leaves out
@art skewed-index
Three things the count misses. A local index read is a scatter gather, with its tail. A global index write touches two shards, so it's briefly inconsistent unless both commit together. And a skewed attribute makes the global index hot in one place.

@chapter Where people slip
@list heading="Common slips" items="Writing the crossover as 1/N@The first|Counting primary-key reads as indexed reads@The second|Treating the count as the whole decision@the third"
The first slip is writing the crossover as one over N. The minus one comes from the row write both designs do. The second is counting all reads as indexed reads, when a primary key lookup costs one either way. And the third is treating the operation count as the whole decision.

@chapter Try it
@words text="Same workload, N = 4" sub="first move: crossover = 1/3"
Your turn. Take the same five thousand reads and two thousand writes to a four shard fleet. The crossover is one third. Work out both costs, say which wins and by how much, and find the read rate where it flips. Why is the margin so much narrower than at sixteen?

@end text="Price the read, price the write"
You can move reads, writes and shards and watch the crossover, on Learn. That's learn dot get er done dot I O.
