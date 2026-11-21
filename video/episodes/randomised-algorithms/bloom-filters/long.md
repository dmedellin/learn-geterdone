---
format: long
lesson: randomised-algorithms/bloom-filters
title: Bloom filters: a certain no, a probable yes, and the exact rate
thumb: A clear bit is a certain no
---

@chapter A set in a few bits
@title text="Bloom Filters" sub="Randomised Algorithms" art=thumb
Store a set of keys without storing the keys. A Bloom filter does it in a handful of bits per key. It can say no with certainty. Its yes is only probable, and you can compute exactly how probable.

@art bit-array
The filter is an array of m bits, all clear, and k hash functions. To insert a key, set the k bits it hashes to. To query a key, check whether all k of its bits are set. The filter never stores a key.

@words text="16 keys · 160 bits · 20 bytes"
Sixteen keys at ten bits each is a hundred and sixty bits, twenty bytes, for a set that would take at least sixteen machine words to store exactly. That saving is what the false positives pay for.

@chapter Proof and hint
@art clear-bit
If any of a key's bits is clear, that key was never inserted. That's a certain no. 

@art overlap-bits
If all of them are set, either the key is there, or other keys happened to set all k between them. The error is one sided, just like the primality test: one answer is a proof, the other is silence.

@chapter The rate
@math heading="False positive rate" items="P(bit still clear) = (1 − 1/m)^(kn)@clear;;P(false positive) = (1 − (1 − 1/m)^(kn))^k@all k"
Each of the k n bit settings misses a given bit with probability one minus one over m. So a bit is still clear with probability that, to the k n. A false positive needs all k of a query's bits set, so treating those as independent, you raise one minus that to the k.

@words text="the k bits are not quite independent"
That last step is an idealisation. Knowing one bit is set is mild evidence the filter is full, which makes the others likelier too. The lab computes this expression exactly, as an exact fraction, and its measured column is the only figure with no model in it.

@math heading="m = 160,  n = 16,  k = 7" items="exact expression:  0.008319  ≈ 1 in 120@point zero zero eight three one nine;;textbook (1 − e^(−kn/m))^k:  0.008194@point zero zero eight one nine four;;measured:  1 false positive in 200 queries@one false positive"
At a hundred and sixty bits, sixteen keys and seven hashes, the expression gives point zero zero eight three one nine, about one in a hundred and twenty. The familiar textbook formula gives point zero zero eight one nine four. And the real filter returned one false positive in two hundred queries.

@art three-numbers
Three numbers. The first is exact under the model. The textbook one approximates it, and it depends only on k and the bits per key, so it doesn't move when the key count changes. And one in two hundred is a measurement. You'd expect about one point six six, so zero or four would be unremarkable too.

@chapter Choosing k
@art k-curve
More hashes set more bits, which hurts. They also need more bits set for a false positive, which helps. So there's an optimum. The rule of thumb, bits per key times the natural log of two, suggests six point nine three. The panel doesn't use it. It scans every k from one to ten.

@list heading="m = 160, n = 16" items="k = 1:  0.095446@k equals one|k = 6:  0.008553@six|k = 7:  0.008319, the best@seven|k = 8:  0.008595@eight"
At k equals one, the rate is point zero nine five. At six, point zero zero eight five five. At seven, the best, point zero zero eight three one nine. At eight, point zero zero eight six. Flat near the minimum, steep on the left. Under hashing is expensive, and over hashing is cheap.

@chapter No deletion
@art delete-breaks
A Bloom filter can't delete. Clearing a removed key's bits would clear bits other keys set, and those keys would then be reported absent. A false negative is the one answer it exists never to give. So it's used where a certain no matters, like a cheap check in front of a disk read.

@chapter Where people slip
@list heading="Common slips" items="Quoting the exponential formula as the rate@The first|Reading a measured count as the rate@The second|Deleting by clearing bits@And the third"
The first slip is quoting the exponential formula as the rate. It's optimistic, and it ignores filter size. The second is reading a measured count as the rate. Two hundred queries can't resolve one in a hundred and twenty. And the third is deleting a key by clearing its bits.

@end text="A certain no, a probable yes"
Build a filter and scan k yourself, on Learn. That's learn dot get er done dot I O.
