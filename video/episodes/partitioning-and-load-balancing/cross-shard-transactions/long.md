---
format: long
lesson: partitioning-and-load-balancing/cross-shard-transactions
title: Cross-shard transactions: half of them cross at two shards
thumb: N to the one minus k
---

@chapter The question
@title text="Cross-shard Transactions" sub="Partitioning and Load Balancing" art=thumb
Most of our transactions are local. That's a common belief, and it's worth checking, because the arithmetic says it's wrong from the very first shard you add.

@art two-keys-two-shards
A transaction is local when every key it touches lives on one shard, and cross shard otherwise. A local one commits on a single node. A cross shard one needs an atomic commitment protocol across the participants, and the standard one is two phase commit.

@chapter The local fraction
@math heading="k random keys over N shards" items="fix the first key's shard@Fix the first;;each other key matches with 1/N@one over N;;P(all on one shard) = (1/N)ᵏ⁻¹ = N¹⁻ᵏ@N to the one minus k;;k = 1:  N⁰ = 1  ✓@a single key"
Fix the first key's shard, whatever it is. Each of the other k minus one keys lands on that same shard with probability one over N, independently. So all of them do with probability N to the one minus k. Check it with a single key: N to the zero is one, always local.

@words text="k = 2,  N = 2:  P(local) = 1/2"
Now the smallest case. Two keys, two shards. The chance of staying local is one half. The first shard anybody adds already sends half of all two key transactions across a boundary.

@math heading="k = 2, crossing fraction" items="N = 16:  local 1/16 = 6.25%,  crosses 93.75%@at sixteen shards;;N = 64:  local 1/64 = 1.56%,  crosses 98.44%@at sixty four"
At sixteen shards, a two key transaction is local one time in sixteen, six point two five percent, and crosses ninety three point seven five percent of the time. At sixty four, it crosses ninety eight point four four percent.

@art collapse-in-k
And look at the exponent. N appears once, k appears up top. So at sixteen shards, going from two keys to three takes the local fraction from six point two five percent to point three nine percent. It collapses in k, not in N.

@words text="E[shards touched] = 1.938" sub="k = 2, N = 16"
The expected number of shards a transaction touches stays close to k. At two keys and sixteen shards it's one point nine three eight. So a two key transaction is a two participant commit almost always, and the protocol's cost doesn't grow with the fleet.

@chapter What two-phase commit adds
@art prepare-commit
Two phase commit has a prepare round, where every participant durably votes, then a commit round. Each round is a round trip plus an fsync at each participant.

@math heading="Round trip 2.00 ms,  fsync 0.50 ms" items="round trips = 2 × 2.00 = 4.00 ms@two round trips;;fsyncs = 2 × 0.50 = 1.00 ms@two fsyncs;;per crossing transaction = 5.00 ms@five milliseconds;;mean over all = 0.9375 × 5.00 = 4.688 ms@the mean over all"
Two round trips at two milliseconds is four. Two fsyncs at half a millisecond is one. So a crossing transaction pays five milliseconds. And the mean over all transactions, at ninety three point seven five percent crossing, is four point six eight eight.

@art price-times-probability
Two numbers, two purposes. Four point six eight eight is the mean, for a throughput calculation. The p ninety nine transaction certainly crosses, so it pays the full five. Put the mean in a tail budget and you understate it.

@art round-trip-vs-fsync
Keep the round trips and the fsyncs separate. The round trip term scales with distance and the fsync term doesn't. Put the participants in one rack and the four milliseconds can shrink a lot, while the one millisecond of durable votes stays put.

@chapter Avoiding the question
@art co-located-keys
The practical answers all make k equal one. Partition by the entity the transaction is about, orders by customer, posts by author. Or co locate related keys under a shared partition key prefix. Both are decisions about the partitioning function, and much harder to make after the data is placed. Changing the shard count isn't a lever at all.

@chapter Where people slip
@list heading="Common slips" items="Writing the exponent as k, not k − 1@The first|Assuming most transactions stay local@The second|Putting the mean in a tail budget@the third"
The first slip is writing the exponent as k instead of k minus one. At k equals one the formula has to give one. The second is assuming most transactions stay local. And the third is putting the mean added latency into a tail budget.

@chapter Try it
@words text="N = 16,  k = 3" sub="first move: 16⁻² = 1/256"
Your turn. Keep sixteen shards and take k to three. The local probability is one over two hundred and fifty six. Work out the crossing fraction, the expected participants, and the mean added latency. Which changed most, and would going to sixty four shards have changed them as much?

@end text="Make k equal one"
You can change keys and shards and watch the crossing fraction, on Learn. That's learn dot get er done dot I O.
