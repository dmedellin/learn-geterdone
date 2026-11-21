---
format: long
lesson: data-structures/open-addressing-and-linear-probing
title: Linear probing: why deleting a key can lose three others
thumb: Mark it, don't empty it
---

@chapter The question
@title text="Open Addressing and Linear Probing" sub="Data Structures" art=thumb
What if a hash table had no chains at all, and every key lived right inside the table? It works. But delete a key the obvious way, and other keys silently vanish.

@chapter The idea
@art probe-sequence
In open addressing, every key sits in a slot of the table. A key has a probe sequence, a list of slots to try. Insert walks it to the first free slot. Search walks it and stops when it finds the key, or hits an empty slot.

@math heading="Linear probing" items="h(k, i) = (h(k) + i) mod m@h of k comma i;;n ≤ m  ⟹  α ≤ 1@at most m"
Linear probing just tries the next slot, and the next. h of k comma i equals h of k plus i, mod m. And since every key needs its own slot, n is at most m, so alpha is at most one.

@words text="power-of-two table sizes" sub="odd step + m = 2ᵏ → every slot is reached"
Double hashing uses a second hash for the step size. The lab only offers power of two sizes, because its step is always odd, and an odd step reaches every slot exactly when m is a power of two.

@chapter The deletion trap
@art cut-chain
Say a key wanted slot five, found five and six taken, and landed in seven. Now delete the key in slot six by emptying it. A search for our key checks five, then six, finds it empty, and stops. It reports not found. The key is in slot seven, and it will never be found again.

@art tombstone
The fix is a tombstone. A slot can be empty, occupied, or dead. A search walks past a dead slot. An insert may reuse it. Only a truly empty slot stops a search.

@words text="22 keys · delete 8 · search the other 14" sub="tombstones: all 14 found · emptying: 3 lost"
The lab fills thirty two slots with twenty two keys, deletes eight, and searches for the fourteen left. With tombstones, all fourteen are found. Emptying the slots instead loses three, and nothing about the table looks wrong.

@chapter Clustering
@art clusters
Linear probing has a second problem. Occupied slots gather into runs. A long run is more likely to catch the next key, which makes it longer still. Chaining doesn't do that, because its chains are independent.

@math heading="Knuth, unsuccessful search" items="≈ ½ (1 + 1/(1 − α)²)@a half times;;not 1 + α@doesn't cost one plus alpha"
So an unsuccessful search doesn't cost one plus alpha. The standard analysis gives about a half times one plus one over one minus alpha squared. At alpha nought point nine, that's fifty point five, against chaining's one point nine.

@chapter Counted against the curve
@math heading="m = 32,  n = 22,  α = 11/16" items="unsuccessful:  counted 5.000 · curve 5.62@unsuccessful;;successful:  counted 2.318 · curve 2.10@successful;;longest run 12 of 32@longest run"
Here's the lab at eleven sixteenths full. Unsuccessful searches counted five probes, against the curve's five point six two. Successful ones counted two point three one eight, against two point one oh. The longest run of filled slots is twelve.

@words text="α = 7/8: counted 8.417 · curve 32.50" sub="a 32-slot table can't cost more than 32"
Push it to seven eighths, twenty eight keys, and the curve says thirty two point five. The table counted eight point four. Neither number is wrong.

@art table-ceiling
The curve describes a table big enough for its idealised clusters to hold. A thirty two slot table can't cost more than thirty two probes. At seven eighths it has four empty slots, and an unsuccessful search stops at one of them after about eight.

@art steep-curve
The curve is a model, not a count. Above alpha nought point nine eight the lab won't print it at all, because it's nearly vertical there: one over one minus alpha squared is two and a half thousand at nought point nine eight, and ten thousand at nought point nine nine.

@chapter Where people slip
@list heading="Common slips" items="Deleting by emptying the slot@The first|Pricing probing with 1 + α@The second|Mixing the curve with the count@And the third"
The first slip is deleting by emptying the slot. Mark it dead instead, and rebuild the table now and then. The second is pricing a probing search with one plus alpha, which is chaining's bound. And the third is reading the curve as the measurement, or the count as the bound.

@chapter Try it
@words text="Insert, search, delete with tombstones" sub="then read your probes against ½(1 + 1/(1−α)²)"
Your turn. Insert a few keys into a small probing table, delete one with a tombstone, and search for a key past it. Then empty the slot instead and see which key disappears.

@end text="Lose a key, then save it"
You can delete with and without tombstones and watch the missing keys get named, on Learn. That's learn dot get er done dot I O.
