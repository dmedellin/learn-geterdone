---
format: long
lesson: combinatorics-and-counting/binomial-coefficients
title: Pascal's triangle: every identity has a counting proof
thumb: Each entry is the two above it
---

@chapter A triangle of numbers
@title text="Pascal's Triangle" sub="Binomial coefficients" art=thumb
Write the numbers C of n, k in rows, one row for each n, and you get Pascal's triangle. Arranging them this way makes their identities visible, and every one of them has a counting proof.

@math heading="Rows 0 to 6" items="1@Row zero;;1  1@Then one one;;1  2  1@one two one;;1  3  3  1@one three three one;;1  4  6  4  1@four six four;;1  5  10  10  5  1@five ten ten;;1  6  15  20  15  6  1@And row six"
Row zero is just one. Then one one. One two one. One three three one. One four six four one. One five ten ten five one. And row six: one, six, fifteen, twenty, fifteen, six, one.

@chapter Pascal's rule
@art two-parents
Each entry is the sum of the two entries just above it. That's Pascal's rule, and it means the whole triangle can be built with nothing but addition. No factorials needed.

@math heading="Pascal's rule, for 1 ≤ k ≤ n − 1" items="C(n, k) = C(n−1, k−1) + C(n−1, k)@C of n, k equals;;C(6, 2) = 5 + 10 = 15@five plus ten"
In symbols, C of n, k equals C of n minus one, k minus one, plus C of n minus one, k. In row six, for example, C of six, two is five plus ten, which is fifteen.

@art fixed-element
Here's why it's true. Fix one element, x, and sort the k element subsets by whether they contain x. Those that do are fixed by their other k minus one elements, chosen from the remaining n minus one. Those that don't are k element subsets of the other n minus one.

@words text="in or out of a fixed element" sub="two disjoint classes → the two terms"
The two classes are disjoint, and between them they cover everything, so the sum rule gives the identity. Two lines, instead of combining fractions full of factorials.

@art pascal-triangle
One caution. The rule needs k between one and n minus one. The entries down the two edges have only one parent each, and C of n, zero and C of n, n are one by definition.

@chapter Rows and signs
@math heading="Row sums" items="Σ C(n, k) = 2ⁿ@two to the n;;row 6: 1 + 6 + 15 + 20 + 15 + 6 + 1 = 64@sixty four"
Every row sums to a power of two, two to the n, because a row counts every subset of an n element set, grouped by size. Row six adds up to sixty four.

@art parity-pairs
Now alternate the signs: plus, minus, plus. For n at least one, that sum is zero. Fix an element x, and pair each subset with the same subset with x added or removed. That matches every even sized subset with an odd sized one, so the two counts are equal.

@words text="n = 0: the alternating sum is 1" sub="no element to add or remove"
For n equals zero it fails. The empty set has one subset, of even size, and there's no element to pair it with. So there the alternating sum is one.

@chapter The hockey stick
@art hockey-stick
Run down a diagonal of the triangle, adding as you go, and the total sits just below and beside where you stopped. That's the hockey stick: the sum of C of i, k, for i from k up to n, equals C of n plus one, k plus one.

@words text="classify by the largest element"
To prove it, count the subsets of size k plus one, from one to n plus one, by their largest element. If the largest is i plus one, the other k come from one to i: C of i, k ways. Summing over i counts every subset exactly once.

@chapter Committees with a chair
@art chair-committee
Here's a fuller proof by counting. Show that the sum of k times C of n, k is n times two to the n minus one. Count committees with a chair, drawn from n people, where the chair is a member.

@math heading="Σ k · C(n, k) = n · 2ⁿ⁻¹" items="committee first: Σ k · C(n, k)@Committee first;;chair first: n · 2ⁿ⁻¹@Chair first;;same set ⟹ equal@Same set"
Committee first: a committee of size k in C of n, k ways, and its chair in k ways. Chair first: n ways to pick the chair, then everyone else independently in or out, two to the n minus one. Same set, two counts, so they're equal.

@words text="n is the chair · 2ⁿ⁻¹ is everyone else"
The algebraic proof means differentiating the binomial theorem. The counting proof explains the answer: the n is the chair, and the two to the n minus one is everyone else's decision.

@chapter Where people slip
@list heading="Common slips" items="Proving identities algebraically by default@The first|Applying Pascal's rule at the edges@The second|Forgetting n = 0 in the alternating sum@And the third"
The first slip is proving identities algebraically by default. Algebra confirms; counting explains. The second is applying Pascal's rule at the edges. And the third is forgetting the n equals zero exception in the alternating sum.

@chapter Try it
@words text="C(2n, 2) = 2·C(n, 2) + n²" sub="check at n = 3: the left side is 15"
Your turn. Prove that C of two n, two equals two times C of n, two, plus n squared. Split two n objects into two halves, and classify each pair by how many of its members come from the first half. Then check at n equals three, where the left side is fifteen.

@end text="Highlight an identity in the triangle"
You can highlight Pascal's rule or the hockey stick in the triangle, and watch the terms add up, on Learn. That's learn dot get er done dot I O.
