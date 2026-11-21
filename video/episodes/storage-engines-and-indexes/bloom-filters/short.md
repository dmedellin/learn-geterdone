---
format: short
lesson: storage-engines-and-indexes/bloom-filters
title: A billion keys, one percent errors, 1.2 GB
---

@art bit-array
How much memory to skip almost every useless disk read? Under ten bits a key.

@math items="p = 1/100:  9.5851 bits a key@nine point five eight five one;;10⁹ keys:  1.20 GB@a billion keys"
A Bloom filter at a one percent false positive rate costs about nine point five eight five one bits a key, whatever the set size. For a billion keys, that's one point two gigabytes.

@art level-skip
On a five level tree, it turns five probes on a miss into one point oh four.

@end text="Full lesson on Learn"
The full lesson, with the target rate on a slider, is on Learn.
