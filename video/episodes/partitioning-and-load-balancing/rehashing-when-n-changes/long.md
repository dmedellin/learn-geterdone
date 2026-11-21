---
format: long
lesson: partitioning-and-load-balancing/rehashing-when-n-changes
title: Add one shard, move almost every key
thumb: Seven eighths of the keys move
---

@chapter The expectation
@title text="Rehashing When N Changes" sub="Partitioning and Load Balancing" art=thumb
You have seven shards and you add one. How many keys move? Most people say about a seventh, the share the new node will end up owning. Under a plain mod N assignment, that's wrong by a factor of about N.

@art mod-n-shuffle
A key k sits on shard h of k, mod N. Change N to N plus one, and h mod N plus one is a different residue for almost every h. Adding one node doesn't nudge the placement. It replaces it.

@words text="mod N moves N/(N+1)" sub="N = 7:  7/8 = 87.50%"
The true moved fraction is N over N plus one. At seven shards that's seven eighths, eighty seven and a half percent, which is six point one three times the one seventh prediction.

@chapter Why seven eighths
@art residue-grid
Here's the count. Take one complete cycle of hash values, N times N plus one of them. A key stays only when h mod N equals h mod N plus one. That common value has to be below N, so the agreeing pairs are v and v, for v from zero up to N minus one.

@math heading="N = 7 → 8" items="cycle = N(N+1) = 7 × 8 = 56@fifty six;;stay: h mod 7 = h mod 8 = v ≤ 6  →  7 values@seven values stay;;moved = 56 − 7 = 49 = 7²@forty nine;;49/56 = 7/8 = 87.50%@seven eighths"
Seven and eight have no common factor, so by the Chinese Remainder Theorem each pair of residues turns up exactly once in the cycle of fifty six. So seven values stay, and forty nine move. Forty nine is seven squared. Forty nine over fifty six is seven eighths.

@words text="N² out of N(N+1)" sub="a fact about consecutive integers"
That's the line worth remembering. N squared moved out of N times N plus one. It's a fact about consecutive integers, not about hashing, and there's no sampling anywhere in the argument.

@chapter The ring
@art ring-join
A consistent hash ring works differently. Nodes and keys both sit on a ring of hash values. Each node holds tokens, and a key belongs to the first token at or after its position, going clockwise. Adding a node adds tokens and moves nothing else. Only the keys in the arcs it claims relocate.

@math heading="The identity" items="ring moves 1/(N+1) = 1/8 = 12.50%@one eighth;;N/(N+1) + 1/(N+1) = 1@add to exactly one;;7/8 + 1/8 = 1@seven eighths plus"
In expectation, the ring moves one over N plus one, one eighth here. And the two fractions add to exactly one. Seven eighths plus one eighth is one. They split the same key set: every key either changes shard under mod N, or it's one the ring leaves alone.

@art whole-split
So this isn't a tuning choice. One scheme moves everything but a sliver, and the other moves the sliver. And the gap only widens as the fleet grows.

@chapter A sample, not the exact fraction
@art sample-scatter
Seven eighths is exact for a complete cycle. A real key set is a sample. The lab's six hundred seeded keys moved five hundred and nineteen times under mod N, eighty six point five percent. On the ring, eighty two moved, thirteen point six seven percent. Those are the keys in the arc the new node took, which on this seed measured twelve point eight nine percent of the ring, not twelve and a half. The ring spared four hundred and thirty seven keys.

@art bytes-to-move
And a fraction isn't yet a cost. Seven eighths of a forty eight terabyte dataset is forty two terabytes to copy. The ring moves six terabytes for the same growth step.

@chapter Where people slip
@list heading="Common slips" items="Predicting 1/N of the keys move@The first|Fractions that don't sum to one@The second|Chasing sample noise@the third"
The first slip is predicting that one over N of the keys move. The second is writing two fractions that don't add up to one, which means you aren't describing the same key set. And the third is expecting a sampled measurement to equal the exact fraction.

@chapter Try it
@words text="N = 12 → 13" sub="first move: cycle = 12 × 13 = 156"
Your turn. Go from twelve shards to thirteen. The cycle length is a hundred and fifty six. Work out how many stay, how many move, both fractions, and their sum. Then predict a range for the lab's six hundred key sample, and say which numbers are exact and which are a draw.

@end text="Count what moves"
You can add a shard and count the keys that move both ways, on Learn. That's learn dot get er done dot I O.
