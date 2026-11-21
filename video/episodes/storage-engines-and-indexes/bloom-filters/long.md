---
format: long
lesson: storage-engines-and-indexes/bloom-filters
title: Bloom filters: under ten bits a key, at any size
thumb: Ten bits, one percent
---

@chapter The trick
@title text="Bloom Filters" sub="Storage Engines and Indexes" art=thumb
A log structured tree has to check every level for a key that isn't there. That's five disk probes for nothing. A Bloom filter buys almost all of them back, for a little under ten bits a key.

@art bit-array
A Bloom filter for n keys is an array of m bits, plus k hash functions. To insert a key, set the k bits it hashes to. To query a key, check those k bits.

@chapter One-sided error
@art clear-bit-no
If any one of them is clear, the key was certainly never inserted. That answer is exact. A clear bit means no inserted key ever hashed there.

@art false-positive
If all k are set, the key is possibly present. Other keys might have set those bits. That's a false positive, and its probability is p. So the error is one sided. The filter can say maybe about a key that's absent. It never says no about a key that's present.

@chapter Bits per key
@math heading="At the best k" items="bits a key ≈ log₂(1/p) / ln 2@log base two;;k ≈ log₂(1/p)@hash functions"
At the number of hash functions that minimises the error, the space is about log base two of one over p, divided by the natural log of two, bits a key. And the hash count is about log base two of one over p. The lesson states these. The Algorithms path proves them.

@math heading="1/ln 2 = 1.442695…" items="p = 1/10:  4.7925 bits a key@one in ten;;p = 1/100:  9.5851 bits a key@one in a hundred;;p = 1/1 000:  14.3776 bits a key@one in a thousand"
One in ten costs four point seven nine two five bits a key. One in a hundred, nine point five eight five one. One in a thousand, fourteen point three seven seven six. Each extra factor of ten costs the same four point seven nine bits, so the cost is linear in the number of nines.

@art grow-linear
And notice there's no n in that. A billion keys at one percent is one point two gigabytes. Two billion is two point four. Both are nine point five eight five one bits a key. Nothing gets relatively worse as the set grows.

@words text="9.585, not 9.57" sub="1/ln 2 = 1.442695…, not 1.44"
You'll often see nine point five seven quoted. That comes from rounding the constant to one point four four. The gap is about two megabytes over a billion keys. Small, but on a page about exact counting, worth explaining. And both figures are approximations anyway.

@chapter A filter on every level
@art level-skip
Now put a filter on every level of the tree. A lookup checks memory first. On the level that holds the key, it reads disk as before. On each of the other levels, it goes to disk only on a false positive.

@math heading="L = 5,  p = 1/100" items="probes = 1 + (L − 1)p@one plus L minus one;;= 1 + 4/100 = 26/25 = 1.0400@twenty six over twenty five"
So the expected probes are one plus L minus one times p. At five levels and one percent, that's one plus four hundredths, twenty six over twenty five, one point oh four. And that one is exact, because p is a target you chose and L is a count.

@art nines-cost
One in ten leaves one point four probes. One in a hundred, one point oh four. One in a thousand, one point oh oh four. The cost rises evenly, and the benefit falls off a cliff, which is why most engines sit at one percent and stop.

@words text="A filter only helps misses"
And a lookup that hits still reads its level. The filter's value is proportional to the miss rate, and that has to be measured.

@chapter Where people slip
@list heading="Common slips" items="Believing a filter can wrongly say no@The first|Sizing from bytes, not keys@The second|Quoting 9.57 as exact@the third"
The first slip is believing a filter can wrongly say no, and re reading on a negative, which throws the benefit away. The second is sizing a filter from the data's bytes instead of its keys. And the third is quoting nine point five seven bits a key as exact.

@chapter Try it
@words text="n = 10⁹,  L = 5,  p = 1/1 000" sub="first move: log₂(1000) = 9.9658"
Your turn. A billion keys, five levels, one in a thousand. Log base two of a thousand is nine point nine six five eight. Work out the bits a key and the memory, the read amplification, and what the extra six hundred megabytes bought compared with one percent.

@end text="Choose p first"
You can move the target rate and watch the memory and the probes, on Learn. That's learn dot get er done dot I O.
