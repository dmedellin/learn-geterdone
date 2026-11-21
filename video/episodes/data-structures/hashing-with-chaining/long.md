---
format: long
lesson: data-structures/hashing-with-chaining
title: Hash tables aren't O(1), and here's the key set that proves it
thumb: Same load, five times slower
---

@chapter The question
@title text="Hashing with Chaining" sub="Data Structures" art=thumb
Everyone says a hash table lookup is constant time. That's half a sentence. The other half matters, and by the end you'll be able to build the keys that break it.

@chapter The structure
@art chained-table
A table has m slots and a hash function h that sends each key to one of them. Each slot holds a linked list, a chain, of every key that landed there. Insert puts the key at the front of its chain. Search computes h of k and walks the chain. Delete unlinks.

@math heading="Two definitions" items="α = n / m@alpha;;h(k) = k mod m@k mod m"
The load factor alpha is n over m, the number of keys divided by the number of slots. And the hash function here is the division method, h of k equals k mod m. It's used because the way it fails is plain arithmetic.

@words text="α can exceed 1" sub="20 keys in 8 slots works fine, just slower"
With chaining, alpha has no ceiling. Twenty keys in eight slots is two and a half per slot, and the table works fine. It's just slower.

@art probe-walk
A search costs one probe to find the slot, plus a walk along its chain. That first one matters when alpha is small. When alpha is large, the walk is what you pay for.

@chapter The expected cost
@art even-spread
Now assume simple uniform hashing. Each key is equally likely to land in any slot, independently. That's an assumption about the keys, not something the hash function guarantees.

@math heading="Expected probes" items="unsuccessful:  α@walks the whole chain;;successful:  1 + α/2 − α/2m@stops at the key;;both:  Θ(1 + α)@both are"
Under that assumption, an unsuccessful search walks the whole chain, which has expected length alpha, by linearity of expectation. A successful search stops at the key, on average halfway, so it's one plus alpha over two, minus alpha over two m. Both are Theta of one plus alpha.

@art funnel
The unsuccessful case uses only linearity of expectation. The expected number of keys in a slot is the sum over keys of the chance each one lands there, which is n times one over m. No independence is needed for that step.

@chapter A table you can draw
@math heading="m = 8,  n = 20" items="α = 20/8 = 5/2@five halves;;successful:  1 + 5/4 − 5/32 = 67/32@sixty seven over thirty two;;measured:  23/10 = 2.3@measured"
Twenty keys in eight slots. Alpha is five halves. The expected successful search is one plus five quarters minus five over thirty two, which is sixty seven over thirty two, about two point oh nine. The lab measured twenty three tenths, two point three. Close.

@words text="chains: 4 5 1 2 0 1 4 3" sub="average 2.5 · longest 5"
The chains came out four, five, one, two, zero, one, four, three. They average two and a half, as they must, because the average is alpha by arithmetic. What varies is the unevenness. The longest is five.

@chapter Breaking it on purpose
@art one-long-chain
Now keep m at eight and n at twenty, but pick the keys eight, sixteen, twenty four, and so on up to a hundred and sixty. Every one is a multiple of eight. So every one goes to slot zero.

@math heading="keys 8, 16, … 160" items="chains:  20 0 0 0 0 0 0 0@twenty in one;;α = 5/2, unchanged@unchanged;;measured:  21/2 = 10.5@ten and a half"
Twenty in one chain, seven slots empty. Alpha is five halves, unchanged. The expectation hasn't moved. But the mean search now costs twenty one halves, ten and a half. A factor of five.

@art aligned-keys
And keys like these aren't exotic. Record IDs spaced by a round number, addresses aligned to a power of two, prices in whole units. The table has become a linked list with an index on the front.

@words text="Θ(1 + α) expected · Θ(n) worst case"
This isn't a bad seed. It's the worst case, reached on purpose. For any fixed hash function, some set of keys all collide, because there are far more keys than slots. So the honest statement has two halves, and you need both.

@chapter Where people slip
@list heading="Common slips" items="Saying O(1) without the qualifications@The first|Reading α as a measurement@The second|Testing only on keys that suit the table@And the third"
The first slip is saying constant time without its two qualifications. The second is reading alpha as a measurement. It's the same on every key set; the longest chain is what tells two tables apart, five here against twenty. And the third is testing only on keys that suit the table.

@chapter Try it
@words text="m = 8: build a key set that degenerates" sub="then compute α and 67/32 yourself"
Your turn. With eight slots, work out alpha and the expected successful cost as exact fractions. Then write down a set of keys that puts everything in one slot, and say why mod m can't stop it.

@end text="Break a hash table yourself"
You can load random keys or a degenerate set and count the probes, on Learn. That's learn dot get er done dot I O.
