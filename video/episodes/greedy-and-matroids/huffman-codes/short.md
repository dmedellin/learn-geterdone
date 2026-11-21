---
format: short
lesson: greedy-and-matroids/huffman-codes
title: Huffman coding doesn't always compress
---

@art equal-weights
Huffman's algorithm is optimal, and sometimes it saves nothing at all.

@words text="a:45 b:13 c:12 d:16 e:9 f:5" sub="56/25 bits per symbol vs 3"
On six skewed weights, Huffman needs fifty six over twenty five bits per symbol, against three for a fixed length code.

@words text="a:10 b:10 c:10 d:10" sub="2 bits each · saving 0"
Give four symbols equal weights, and every codeword is two bits, exactly the fixed length. Compression comes from the input, not the algorithm.

@end text="Full lesson on Learn"
Try your own weights on Learn.
