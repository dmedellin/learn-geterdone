---
format: long
lesson: greedy-and-matroids/huffman-codes
title: Huffman codes: merge the two lightest, and read the code off the tree
thumb: Rare symbols, long codewords
---

@chapter The question
@title text="Huffman Codes" sub="Greedy Algorithms and Matroids" art=thumb
Say you want to write a text in binary, and some symbols turn up far more often than others. Giving every symbol the same number of bits wastes space. So how do you give common symbols short codewords, and still read the bits back?

@art prefix-tree
The answer is a prefix code. No codeword is the start of another. That lets a decoder read the bits left to right and commit to a symbol the moment it sees one, with no separators and no guessing. Every binary tree with symbols at its leaves gives you one.

@math heading="The goal" items="minimise  Σ wᵢ · |cᵢ|@add them up;;expected length = Σ wᵢ · |cᵢ| / Σ wᵢ@divide"
Each symbol has a weight, how often it appears. Multiply each weight by its codeword's length, and add them up. That's the total number of bits, and you want it as small as possible. Divide by the total weight, and you get the expected codeword length.

@chapter The algorithm
@art merge-lightest
Huffman's algorithm builds the tree from the bottom up. Start with every symbol as a tiny tree of its own. Then, again and again, take the two lightest trees, join them under a new node whose weight is their sum, and put it back.

@words text="n symbols → n − 1 merges" sub="left edge 0 · right edge 1"
After n minus one merges, one tree is left. Label every left edge zero and every right edge one, and each leaf's path from the root is its codeword. The greedy commitment is the merge. Once two trees are joined, nothing ever separates them.

@chapter Six symbols
@math heading="a:45  b:13  c:12  d:16  e:9  f:5" items="f + e = 14@f plus e;;c + b = 25@c plus b;;14 + d = 30@fourteen plus d;;25 + 30 = 55@twenty five plus thirty;;a + 55 = 100@a plus fifty five"
The lab opens on six symbols: a forty five, b thirteen, c twelve, d sixteen, e nine and f five. First f plus e makes fourteen. Then c plus b makes twenty five. Then fourteen plus d makes thirty. Then twenty five plus thirty makes fifty five. And finally a plus fifty five makes a hundred.

@math heading="The codewords" items="a = 0@a gets;;c = 100 · b = 101 · d = 111@c gets;;f = 1100 · e = 1101@f and e"
Now read the codewords off the tree. a gets zero, a single bit. c gets one zero zero, b gets one zero one, and d gets one one one, three bits each. f and e get four bits: one one zero zero, and one one zero one.

@art weighted-leaves
The heaviest symbol got the shortest codeword, and the two lightest got the longest. That's the whole idea.

@math heading="Counting bits" items="total bits = 224,  total weight = 100@two hundred and twenty four;;expected length = 224/100 = 56/25@fifty six over twenty five;;fixed length: 3 bits each → 300 bits@three bits;;saving = 19/25 bit per symbol@nineteen over twenty five"
The total is two hundred and twenty four bits, over a total weight of a hundred. So the expected length is fifty six over twenty five. A fixed length code for six symbols needs three bits each, three hundred bits. Huffman saves nineteen over twenty five of a bit per symbol.

@chapter It depends on the input
@art equal-weights
Now give four symbols equal weights, ten each. Every codeword comes out two bits, the same as a fixed length code, and the saving is zero. Huffman did nothing wrong. There was nothing to do. Compression is a property of the input, not the algorithm.

@chapter A check by hand
@math heading="Kraft's sum" items="Σ 2^(−ℓᵢ) = 1  for any Huffman code@equals exactly one;;1/2 + 1/8 + 1/8 + 1/16 + 1/16 + 1/8 = 1@a half"
Here's a quick check. Add up two to the minus length, over every codeword. For a Huffman code, that sum equals exactly one, because the tree is full. On the opening code, that's a half, plus an eighth, an eighth, a sixteenth, a sixteenth and an eighth. Which is one.

@art full-tree
Any prefix code has a sum of at most one. Less than one means some branch goes nowhere, so the code could be shorter. More than one means it isn't a prefix code at all.

@chapter Where people slip
@list heading="Common slips" items="Averaging lengths instead of weighting them@The first|Believing Huffman always compresses@The second|Trusting a short code without decoding it@The third"
The first slip is averaging the codeword lengths. The plain mean here is three, but the expected length is fifty six over twenty five. The second is believing Huffman always compresses. Equal weights save nothing. The third is trusting a short code without a round trip. Encode a message, decode it, and check it comes back.

@art bit-stream
On the opening alphabet, the message a b c d e f encodes to eighteen bits, and decodes back exactly. A code that's short because it's wrong looks just like one that's short and right, until you read it back.

@chapter Try it
@words text="a:60  b:20  c:10  d:5  e:5"
Your turn. Run the merges on a sixty, b twenty, c ten, d five and e five. The common symbol should get one bit and the two rarest four. Check that the expected length is seventeen over ten, and that Kraft's sum is one.

@end text="Build your own Huffman tree"
You can type your own weights, watch the merges, and decode a message, on Learn. That's learn dot get er done dot I O.
