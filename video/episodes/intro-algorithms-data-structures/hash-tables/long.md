---
format: long
lesson: intro-algorithms-data-structures/hash-tables
title: Hash tables with chaining, and the load factor
thumb: Compute where it goes
---

@chapter Compute, don't search
@title text="Direct Addressing and Hashing with Chaining" sub="Introduction to Algorithms, Sections 11.1 and 11.2" art=thumb
A linked list finds a key by walking. A hash table computes where the key belongs instead, and goes straight there.

@quote text="The bottom line is that hashing is an extremely effective and practical technique." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 11"
The authors are enthusiastic. The bottom line is that hashing is an extremely effective and practical technique. But they qualify it at once: the constant time is an average, and the worst case is as slow as a list.

@chapter Direct addressing
@art direct-table
Start where hashing isn't needed. If every key comes from a small universe, zero to m minus one, use an array with one slot per possible key. Search, insert and delete each touch a single slot. The trouble is size. When the universe is huge and you store only a few keys, almost the whole table sits empty.

@chapter Hashing
@art hash-arrow
A hash table keeps storage proportional to the keys actually stored. A hash function maps every key onto slots zero to m minus one, and key k goes to slot h of k. There are more keys than slots, so two keys can land in the same slot. That's a collision.

@art chains
The first remedy is chaining. Each slot holds a linked list of the elements that hash there. Insert puts a new element at the head of its list in constant time. Search walks one list. And delete splices an element out in constant time, if it's handed the element.

@math heading="Load factor" items="α = n / m@alpha is n over m"
For m slots holding n elements, the load factor alpha is n over m, the average number of elements per chain. Every average in the section depends on it.

@art load-factor
But alpha is only the mean. It can be below one, equal to one or above it, and the chains themselves vary. The longest chain is what an unlucky search pays.

@chapter The average
@art one-chain
The worst case is plain. If all n keys hash to one slot, the table is a single list, and search costs theta of n. So hashing is only useful because of the average. The authors assume simple uniform hashing: each key is equally likely to land in any slot.

@math heading="Theorems 11.1 and 11.2" items="unsuccessful: α on average → Θ(1 + α)@unsuccessful;;successful: 1 + (n − 1)/(2m)@successful;;= 1 + α/2 − α/(2n)@one plus alpha over two"
Then an unsuccessful search examines one whole chain, alpha elements on average. A successful search examines one plus n minus one over two m elements, which is one plus alpha over two minus alpha over two n. Both are theta of one plus alpha.

@art search-walk
Why that formula? New elements go to the head, so a search for x passes exactly the elements inserted into x's slot after x. Each later key shares the slot with probability one over m. Averaging gives one for x itself, plus half of the others' share. So if the table grows with the keys, alpha stays constant, and every operation is constant time on average.

@chapter In the lab
@math heading="20 keys, 8 slots" items="α = 5/2@five halves;;book's successful: 35/16 ≈ 2.19@thirty five sixteenths;;measured mean: 23/10 = 2.3@two point three;;longest chain 5, 1 slot empty@longest chain"
Twenty keys in eight slots give alpha five halves. The book's successful expectation is thirty five sixteenths, about two point one nine. The measured mean is two point three, with a longest chain of five, and one slot empty.

@words text="Multiples of 8, h(k) = k mod 8" sub="every key in slot 0 · mean 21/2"
Now make every key a multiple of eight, with h of k equal to k mod eight. The load factor is still five halves. But every key is in slot zero, and the mean is ten and a half. Nothing in the theorem is wrong. These keys break its assumption.

@chapter Common slips
@list heading="Common slips" items="Reading Θ(1 + α) as a guarantee@The first|Treating α as every chain's length@The second|Dropping the 1 from Θ(1 + α)@the third"
The first slip is reading theta of one plus alpha as a guarantee for every set of keys. The second is treating alpha as every chain's length. And the third is dropping the one. A search always costs at least a constant.

@chapter Try it
@words text="3, 14, 25, 9, 20, 31, 6, 17" sub="m = 11, h(k) = k mod 11"
Your turn. Hash three, fourteen, twenty five, nine, twenty, thirty one, six and seventeen into eleven slots, with k mod eleven. Draw the chains, find the mean cost of a successful search, and compare it with the theorem. Then try eight slots, and explain why the mean falls although alpha rises.

@end text="Measure your own chains"
You can set measured chain lengths beside the load factor and the book's expectations, on Learn. That's learn dot get er done dot I O.
