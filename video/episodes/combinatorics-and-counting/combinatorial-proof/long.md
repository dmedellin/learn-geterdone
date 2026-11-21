---
format: long
lesson: combinatorics-and-counting/combinatorial-proof
title: Combinatorial proof: count it twice, or pair it up
thumb: One set, two counts
---

@chapter Proof without algebra
@title text="Combinatorial Proof" sub="Combinatorics and Counting" art=thumb
You can prove an identity by grinding through algebra. Or you can prove it by counting, and come away knowing why it's true. There are two techniques: count one set in two ways, or build a bijection between two sets.

@chapter Double counting
@art two-ways-count
To prove that A equals B, find a set S. Show that counting S one way gives A, and counting it another way gives B. S has only one size, so A equals B.

@art incidence-grid
Here's a classic. In any graph, the degrees of all the vertices add up to twice the number of edges. Count the incidences, the pairs of a vertex and an edge that meets it. By vertex, each one contributes its degree. By edge, each contributes two, one for each end.

@math heading="Σ C(n, k)² = C(2n, n)" items="Vandermonde: C(2n, n) = Σ C(n, k) · C(n, n − k)@Vandermonde;;symmetry: C(n, n − k) = C(n, k)@symmetry"
Some identities that look algebraic are double counts in disguise. The sum of C of n, k squared equals C of two n, n. Count the n element subsets of a two n set by how many come from the first half. That's Vandermonde, and symmetry turns it into squares.

@chapter A worked double count
@art nested-loops
Prove that C of n, k times C of k, j equals C of n, j times C of n minus j, k minus j. The objects are pairs A, B, where B sits inside A, and A sits inside an n element set S. A has k elements, and B has j.

@math heading="C(n,k)·C(k,j) = C(n,j)·C(n−j, k−j)" items="A first: C(n, k) · C(k, j)@Choose A first;;B first: C(n, j) · C(n − j, k − j)@choose B first;;one set, two counts ⟹ equal@One set"
Choose A first, in C of n, k ways, then B inside it, in C of k, j ways. Or choose B first, in C of n, j ways. Then A's other k minus j elements come from the n minus j outside B. One set, two counts, so the expressions are equal.

@words text="inner set first, or outer set first"
The algebraic proof expands four factorial expressions and cancels. It's correct, and it leaves you knowing nothing. The counting proof tells you why: you can choose the inner set before or after the outer one.

@chapter Bijective proof
@art bijection-arrows
The second technique. To prove two sets have the same size, construct an explicit bijection between them. Define the map, then show it's injective and surjective. Producing the inverse map is the cleanest way to do both.

@art bit-string-subset
Subsets of an n element set match bit strings of length n. Send a subset to the string with a one in position i exactly when the i th element is in. A subset is fixed by its members, and every string names a subset. So there are two to the n subsets.

@art gap-cuts
Here's a nicer one. The ways to write n as an ordered sum of positive integers number two to the n minus one. Write n as n ones in a row, with n minus one gaps between them. Choose which gaps to cut, and each choice gives exactly one sum.

@chapter Which one to use
@list heading="Which technique?" items="A sum on one side → double count@a sum|Two counts, no sum → bijection@no sum|Alternating signs → pairing or inclusion–exclusion@alternating signs"
If the identity has a sum on one side, double count, classifying by whatever the summation index measures. If it says two counts are equal, with no sum, look for a bijection. And if it has alternating signs, look for a pairing that cancels terms, or use inclusion and exclusion.

@words text="a combinatorial proof is a proof"
This isn't intuition. The obligations are precise. For double counting, name the objects, and check that both classifications are disjoint and exhaustive. For a bijection, define the map, and argue both directions.

@chapter Where people slip
@list heading="Common slips" items="Not saying what the objects are@The first|A classification with a gap or an overlap@The second|Asserting a bijection without defining it@And the third"
The first slip is not saying what the objects are. Naming them is most of the work. The second is a classification with a gap or an overlap. And the third is asserting a bijection without defining it. An obvious correspondence is exactly where errors hide.

@chapter Try it
@words text="Σ 2ᵏ · C(n, k) = 3ⁿ" sub="by double counting: what is one object?"
Your turn, twice. First, prove that the sum of two to the k times C of n, k is three to the n, by double counting. Say exactly what one object being counted is.

@words text="no two consecutive: C(n − k + 1, k)" sub="check at n = 5, k = 2: both sides are 6"
Second, prove by bijection that the k element subsets of one to n with no two consecutive numbers number C of n minus k plus one, k. Write down the inverse map, and check it at n equals five and k equals two, where both sides are six.

@end text="Watch the hockey stick add up"
You can watch the hockey stick identity add up in Pascal's triangle, on Learn. That's learn dot get er done dot I O.
