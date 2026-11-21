---
format: long
lesson: intro-algorithms-data-structures/open-addressing
title: Open addressing: probing, clustering and the 1 over 1 minus alpha bound
thumb: Full tables get slow fast
---

@chapter No more chains
@title text="Open Addressing" sub="Introduction to Algorithms, Section 11.4" art=thumb
Chaining stores colliding keys outside the table. Open addressing keeps every key inside it. There are no lists, so the table can fill up, and the load factor can never exceed one.

@art probe-walk
Instead of a chain, each key carries a probe sequence, an order in which to try the slots, which must reach every slot once. Insert walks the sequence to the first empty slot. Search walks the same sequence, and can stop at an empty slot, because the key would have been put there.

@chapter Deleting is hard
@art deleted-marker
That stopping rule makes deletion tricky. Empty a deleted key's slot, and you cut every probe sequence that passed through it. Keys further along can't be found any more. So mark the slot deleted instead. Insert may reuse it, and search walks past it.

@words text="Many deletions? Use chaining." sub="marked slots lengthen searches"
The price is that marked slots lengthen searches without holding keys, so search time no longer depends on alpha alone. That's why the authors say chaining is the usual choice when keys must be deleted.

@chapter Three probe rules
@quote text="Long runs of occupied slots tend to get longer, and the average search time increases." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 11.4"
Linear probing tries the home slot, then each next slot in turn, wrapping round. The book warns: long runs of occupied slots tend to get longer, and the average search time increases.

@art cluster-growth
Here's why. An empty slot after a run of i full ones is filled next with probability i plus one over m. A key landing anywhere in the run extends it. That's primary clustering. And the first probe fixes the whole sequence, so there are only m sequences.

@art double-hash-jumps
Quadratic probing breaks up the runs, but still has only m sequences. Double hashing steps by a second hash, so keys with the same home slot usually step differently. That gives theta of m squared sequences, and in practice it behaves close to uniform hashing.

@math heading="Double hashing" items="h(k, i) = (h₁(k) + i·h₂(k)) mod m@h one of k;;h₂(k) shares no factor with m@no factor"
h of k and i is h one of k plus i times h two of k, mod m. For that to reach every slot, h two of k must share no factor with m. Either m is a power of two and h two is always odd, or m is prime.

@chapter The bound
@math heading="Theorem 11.6" items="Pr{need an i-th probe} ≤ α^(i − 1)@the chance of needing;;1 + α + α² + … = 1/(1 − α)@one plus alpha"
Under uniform hashing, the first probe hits an occupied slot with probability alpha. Each further probe hits one with probability at most alpha, so the chance of needing an ith probe is at most alpha to the i minus one. Add up one plus alpha plus alpha squared and so on, and you get one over one minus alpha.

@art bound-curve
Read it as one probe always, a second about alpha of the time, a third about alpha squared. That's modest while the table is partly empty. But as alpha approaches one, it grows without limit. A successful search is at most one over alpha, times the log of one over one minus alpha.

@math heading="22 keys, 32 slots, α = 11/16" items="bound: 16/5 = 3.2@three point two;;linear probing: 5 probes, cluster of 12@linear probing;;double hashing: 3 probes, cluster of 8@double hashing"
In the lab, twenty two keys in thirty two slots give alpha eleven sixteenths. The bound for an absent key is sixteen fifths, three point two. Linear probing counts five probes, with a cluster of twelve slots. Double hashing counts three, with a longest cluster of eight.

@words text="α = 7/8: bound 8, linear ≈ 8.42" sub="the bound is about uniform hashing"
At seven eighths full, the bound is eight, and linear probing counts about eight point four two, with a cluster of sixteen. Linear above the bound and double below it is what you'd expect. The bound is for uniform hashing, which double hashing approximates and linear probing doesn't.

@chapter Perfect hashing
@art two-level
Section eleven point five is named here. When the keys never change, like a language's reserved words, two levels of universal hashing give constant time in the worst case. Each first level slot gets a small secondary table, sized to have no collisions at all.

@chapter Common slips
@list heading="Common slips" items="Expecting a gentle slowdown as it fills@The first|Deleting by emptying the slot@The second|Taking linear probing for uniform hashing@the third"
The first slip is expecting open addressing to slow down gently as the table fills. The second is deleting by emptying the slot. And the third is taking linear probing for uniform hashing. It has only m probe sequences.

@chapter Try it
@words text="27, 49, 16, 38, 60 into 11 slots" sub="h′(k) = k mod 11, linear probing"
Your turn. Insert twenty seven, forty nine, sixteen, thirty eight and sixty into eleven slots by linear probing, with k mod eleven. Delete forty nine by emptying its slot, and count how many keys can't be found. Then mark it deleted instead, and count the probes to find sixty.

@end text="Count the probes"
You can set counted probes beside the bound as the table fills, on Learn. That's learn dot get er done dot I O.
