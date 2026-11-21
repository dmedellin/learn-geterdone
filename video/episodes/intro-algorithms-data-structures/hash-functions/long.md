---
format: long
lesson: intro-algorithms-data-structures/hash-functions
title: Hash functions and universal hashing
thumb: Randomize the function, not the keys
---

@chapter What makes a hash good
@title text="Hash Functions and Universal Hashing" sub="Introduction to Algorithms, Section 11.3" art=thumb
Chaining is fast only if keys spread evenly. That depends on the hash function. So what makes one good?

@words text="Simple uniform hashing" sub="rarely something you can check"
Ideally, it would satisfy simple uniform hashing. But that can rarely be checked. You usually don't know the distribution of the keys, and they may not be independent. So the aim is a hash that's unlikely to line up with patterns in the data. Strings are first read as numbers, with characters as digits in a large radix.

@chapter The division method
@art division-ring
The division method takes the remainder, k mod m. One division, so it's fast. Its weakness is the choice of m.

@art low-bits
If m is a power of two, the remainder is just the lowest bits of k, and the higher bits are ignored. So keys that agree in their low bits all collide. Thirty seven, fifty three, sixty nine and eighty five all land in the same slot mod sixteen. The authors advise a prime, not near a power of two.

@chapter The multiplication method
@math heading="Multiplication method" items="h(k) = ⌊m · (kA mod 1)⌋@multiplies k by;;A ≈ (√5 − 1)/2 ≈ 0.618@the golden ratio"
The multiplication method multiplies k by a constant A between zero and one, keeps the fractional part, scales by m and rounds down. Any A works, some better than others. The book reports Knuth's suggestion, the fractional part of the golden ratio, about point six one eight.

@art fraction-line
Here the value of m isn't critical, so it's usually a power of two. Then a machine computes the hash with one multiplication and a shift, and all the bits of k get mixed in.

@chapter The adversary
@art adversary-keys
But both methods are fixed functions. Someone who knows the function can pick n keys that all land in one slot, and then every search is a walk down one long list.

@quote text="Any fixed hash function is vulnerable to such terrible worst-case behavior." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 11.3.3"
The authors are blunt. Any fixed hash function is vulnerable to such terrible worst case behavior.

@art random-draw
The answer is the one quicksort used: randomize. When the table is created, pick the function at random from a family designed for the purpose, independently of the keys. Now no set of keys is bad every time. A bad outcome needs an unlucky draw.

@chapter Universal families
@words text="Any two keys collide with chance ≤ 1/m" sub="a universal family"
A family is universal if, for every pair of distinct keys, at most one m th of the functions send them to the same slot. Then by the indicator method, a stored key's chain has expected length at most one plus alpha. The expectation is over the function. Nothing is assumed about the keys.

@math heading="Theorem 11.5's family" items="p prime, larger than every key@a prime p;;h_ab(k) = ((ak + b) mod p) mod m@a k plus b;;a in 1..p − 1,  b in 0..p − 1@a from one"
Here's the book's family. Choose a prime p larger than every key. Then h of k is a k plus b, mod p, then mod m, with a from one to p minus one and b from zero to p minus one. That's p times p minus one functions.

@art collision-grid
The proof is a counting argument. Since p is prime, two different keys always give two different residues, and each choice of a and b gives a different pair of residues. So the number of colliding functions depends only on p and m, never on the keys.

@math heading="p = 11, m = 4" items="residue classes of sizes 3, 3, 3, 2@three, three, three and two;;3·2 + 3·2 + 3·2 + 2·1 = 20@twenty;;20 of 110 = 2/11 ≤ 1/4@two elevenths"
At p eleven and m four, the residues zero to ten fall into classes of sizes three, three, three and two. Ordered pairs within a class number twenty. So every pair of keys collides under twenty of the hundred and ten functions, a rate of two elevenths, within one quarter.

@chapter Common slips
@list heading="Common slips" items="Thinking universal hashing randomizes the keys@The first|A power of 2 with the division method@The second|Expecting every drawn function to be safe@the third"
The first slip is thinking universal hashing randomizes the keys. It randomizes the function. The second is using a power of two with the division method. And the third is expecting any one drawn function to be good for every set of keys. Bad draws are rare, not impossible.

@chapter Try it
@words text="p = 7, m = 3, keys 2 and 5" sub="count by residue pairs"
Your turn. With p seven and m three, and keys two and five, count by the residue pair argument how many functions send them to the same slot, without listing all forty two. Then check it in the lab.

@end text="Count every function"
You can count, over every function in the family, how often one pair collides, on Learn. That's learn dot get er done dot I O.
