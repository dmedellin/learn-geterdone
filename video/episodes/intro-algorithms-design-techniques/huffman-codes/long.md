---
format: long
lesson: intro-algorithms-design-techniques/huffman-codes
title: Huffman codes: merge the two rarest, and why it's optimal
thumb: Merge the two lightest
---

@chapter Short codes for common letters
@title text="Huffman Codes" sub="Introduction to Algorithms, Section 16.3" art=thumb
A fixed length code spends the same bits on every character, three bits each for an alphabet of six. But if some characters are far more common, why not give them shorter codewords?

@art fixed-vs-variable
That's a variable length code. The authors report typical savings of twenty to ninety percent, depending on the data. The catch is decoding. With different lengths, where does one codeword end and the next begin?

@chapter Prefix codes
@art bit-stream
The answer is a prefix code, where no codeword is the start of another. Then the bits decode themselves. Read until you've spelled a codeword, emit it, and start again. No separators needed.

@art code-tree
A prefix code is a binary tree. Each character is a leaf, and its codeword is the path from the root, zero for left, one for right. An optimal code's tree is full. A node with one child could be removed, shortening every codeword below it. And these aren't search trees, so the leaves needn't be in any order.

@math heading="Cost of a tree" items="B(T) = Σ c.freq · d(c)@B of T"
The bits the file takes are B of T, the sum over characters of frequency times depth. The depth is also the codeword's length.

@chapter Huffman's algorithm
@quote text="Huffman invented a greedy algorithm that constructs an optimal prefix code called a Huffman code." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 16.3"
Huffman invented a greedy algorithm that constructs an optimal prefix code called a Huffman code.

@words text="David Huffman, 1952" sub="a greedy merge"
The chapter notes date the algorithm to nineteen fifty two. It's greedy, and the hard part is proving its choice is always safe.

@art merge-step
Put the characters in a min priority queue by frequency. Then, n minus one times, take out the two least frequent items, make them children of a new node whose frequency is their sum, and put that node back. The last item left is the root. With a heap, that's O of n log n.

@math heading="a:14 b:6 c:10 d:21 e:4 f:5" items="e:4 + f:5 = 9@four and five;;b:6 + 9 = 15@six and the new nine;;c:10 + a:14 = 24@ten and fourteen;;15 + d:21 = 36@fifteen and twenty one;;24 + 36 = 60@twenty four and thirty six"
Take six characters with these frequencies, totalling sixty. Merge four and five to make nine, then six and the new nine make fifteen. Ten and fourteen make twenty four, and fifteen and twenty one make thirty six. Finally twenty four and thirty six make the root, sixty.

@math heading="Codeword lengths: a 2, c 2, d 2, b 3, e 4, f 4" items="B(T) = 14·2 + 10·2 + 21·2 + 6·3 + 4·4 + 5·4 = 144@a hundred and forty four;;= 9 + 15 + 24 + 36 + 60@sum of the merges;;144 / 60 = 2.4 bits per character@two point four"
That gives a, c and d two bits, b three, and e and f four. So the cost is a hundred and forty four bits. And notice, that's also the sum of the merges. Each merge pushes every leaf below it one level down. That's two point four bits a character, against three.

@chapter Why it's optimal
@art deepest-siblings
Lemma sixteen point two is the greedy choice. The two rarest characters can always be sibling leaves at the bottom of some optimal tree. Take any optimal tree, and swap them with the two deepest siblings. Rarer characters move down, and the cost can't rise.

@art merge-sequence
Lemma sixteen point three is optimal substructure. Replace the two rarest by one new character with their combined frequency. Any tree for that smaller alphabet, split back out, costs exactly their two frequencies more. So an optimal small tree gives an optimal big one, and Huffman's code is optimal.

@chapter In the lab
@words text="faced: 14 bits, not 15" sub="f 4 · a 2 · c 2 · e 4 · d 2"
In the lab, encode the word faced. f is four bits, a two, c two, e four, d two. Fourteen bits instead of fifteen, and it decodes back with nothing between the codewords.

@chapter Common slips
@list heading="Common slips" items="Thinking variable lengths need separators@The first|Merging by the original frequencies only@The second|Expecting Huffman to compress every file@the third"
The first slip is thinking a variable length code needs separators. The second is merging by the original frequencies only. The new node of nine competes in the queue like any character. And the third is expecting Huffman to compress every file. With equal weights, it saves nothing.

@chapter Try it
@words text="p:2 q:3 r:5 s:5 t:9 u:14" sub="break each tie both ways"
Your turn. Build the Huffman tree for these six frequencies by hand. Where does the queue hold equal frequencies? Break the first tie each way, and say whether the codeword lengths change, or the cost, or both.

@end text="Build a code yourself"
You can build a Huffman code and check it against every tree, on Learn. That's learn dot get er done dot I O.
