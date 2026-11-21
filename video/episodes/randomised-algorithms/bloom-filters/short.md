---
format: short
lesson: randomised-algorithms/bloom-filters
title: The data structure that can't say a false no
---

@art clear-bit
A Bloom filter can be wrong about yes. It's never wrong about no.

@art bit-array
Insert a key by setting its k bits. Query by checking them. If any bit is clear, the key was never inserted. Certain.

@words text="160 bits, 16 keys, 7 hashes" sub="false positives ≈ 1 in 120"
If all are set, other keys may have set them. With ten bits per key and seven hashes, that happens about one time in a hundred and twenty.

@end text="Full lesson on Learn"
The full lesson on Bloom filters is on Learn.
