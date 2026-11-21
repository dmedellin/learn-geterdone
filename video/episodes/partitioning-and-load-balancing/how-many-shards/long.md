---
format: long
lesson: partitioning-and-load-balancing/how-many-shards
title: How many shards? Two ceilings, and you build the larger
thumb: Two ceilings, build the max
---

@chapter The question
@title text="How Many Shards" sub="Partitioning and Load Balancing" art=thumb
How many shards should a system have? It sounds like it should have one formula. It doesn't, because there are two separate limits, and each one asks for its own count.

@art shard-vs-replica
First, what a shard is. A shard is a disjoint piece of a dataset, along with the node or nodes that serve it. Every key belongs to exactly one shard. A shard is not a replica. A replica is a copy of a piece. A shard is a piece.

@art two-ceilings
The two limits ask about different resources. Load asks how many nodes it takes for the peak request rate, shared among them, to sit under the utilisation you're willing to run at. Storage asks how many nodes it takes to hold the dataset once every item has been written RF times.

@chapter Two formulas
@math heading="Two ceilings" items="N_load = ⌈λ_peak / (c · ρ_target)⌉@the load count;;N_storage = ⌈D · RF / per-node⌉@the storage count;;N = max(N_load, N_storage)@you build the larger"
The load count is the ceiling of the peak rate over c times the target utilisation. The storage count is the ceiling of the dataset times the replication factor, over what one node holds. And you build the larger of the two.

@words text="c is ONE node's capacity" sub="not a count of nodes"
Watch the symbol c. It's the requests a second that a single node can serve. Read it as a number of machines and the whole expression turns over, and the answer still looks like a count, so nobody notices.

@chapter A worked example
@math heading="Load" items="c · ρ_target = 8 000 × 0.65 = 5 200 /s@five thousand two hundred;;⌈120 000 / 5 200⌉ = ⌈300/13⌉@three hundred over thirteen;;⌈23.0769…⌉ = 24@twenty four"
Take a peak of a hundred and twenty thousand requests a second, nodes that serve eight thousand, and a target of sixty five percent. The usable rate per node is five thousand two hundred. Divide, and you get three hundred over thirteen, about twenty three point oh eight. The ceiling is twenty four.

@math heading="Storage" items="D · RF = 48 TB × 3 = 144 TB@a hundred and forty four;;⌈144 / 4⌉ = 36@thirty six;;N = max(24, 36) = 36@storage binds"
Now the bytes. Forty eight terabytes at three copies is a hundred and forty four terabytes that have to fit. On four terabyte nodes, that's thirty six. So you build thirty six, and storage binds, by twelve shards.

@art three-copies
That replication factor is the whole storage constraint. Drop it and you'd get twelve shards instead of thirty six, a fleet a third the size, sized against a number that never existed on any disk.

@chapter What the slack tells you
@art fleet-of-nodes
At thirty six shards, each node serves about three thousand three hundred and thirty three requests a second, which is forty one point six seven percent of its capacity. Traffic could grow by more than half before load starts to bind.

@words text="144 TB / 36 = 4.00 TB of 4 TB" sub="no storage slack at all"
Storage has no slack at all. Each node holds exactly four terabytes of a four terabyte node. Grow the dataset by one byte, and you need another shard. A ceiling that comes out exact is the least comfortable answer this arithmetic can give.

@art binding-swap
And which limit wins can change. Take the peak to two hundred thousand, and load asks for thirty nine, so load binds by three. Instead shrink the dataset to twenty terabytes, and storage asks for fifteen, so load binds by nine.

@chapter Where people slip
@art ceiling-step
Round only at the ceiling. Three hundred over thirteen rounded to twenty three point one still gives twenty four. Rounded to twenty three, it gives twenty three, and you're a node short.

@list heading="Common slips" items="Sizing on one constraint only@The first|Dropping the replication factor@The second|Rounding before the ceiling@the third"
The first slip is sizing on one constraint and meeting the other in production. The second is dropping the replication factor, a factor of three in fleet size. And the third is rounding before the ceiling instead of at it.

@chapter Try it
@words text="260 000 /s · 60 TB" sub="first move: 5 200 /s per node"
Your turn. Keep the node at eight thousand a second, sixty five percent, four terabytes, and three copies. Take the peak to two hundred and sixty thousand and the dataset to sixty terabytes. The usable rate per node is still five thousand two hundred. Work out both ceilings, say which binds and by how much, and the utilisation each node runs at.

@end text="Two numbers, then the max"
You can move the load and storage sliders and watch which one wins, on Learn. That's learn dot get er done dot I O.
