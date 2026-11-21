---
format: long
lesson: sets-relations-functions/cartesian-products-and-tuples
title: Cartesian products: ordered pairs and why sizes multiply
thumb: Order matters here
---

@chapter The question
@title text="Cartesian Products and Tuples" sub="Sets, Relations and Functions" art=thumb
A set ignores order and ignores repetition. That's its whole nature. But plenty of things depend on order: a point on a graph, a date, a word. So you need an object where order counts. That object is the tuple.

@art pair-arrow
An ordered pair, a comma b, equals c comma d exactly when a equals c and b equals d. Coordinate by coordinate. So one, two is not the same pair as two, one, even though the set one, two equals the set two, one.

@math heading="Ordered pairs" items="(a, b) = (c, d)  ⟺  a = c and b = d@exactly when;;(1, 2) ≠ (2, 1)@is not the same pair;;(1, 1)  is a perfectly good pair@one, one"
So a, b equals c, d exactly when the coordinates match. One, two is not the same pair as two, one. And tuples allow repetition: one, one is a perfectly good pair. The same idea extends to n tuples, which agree in every position.

@chapter The product
@art grid-product
The Cartesian product of A and B is the set of every ordered pair whose first coordinate comes from A and whose second comes from B. Picture A down the side, B across the top, and one pair at every crossing.

@math heading="{1, 2} × {a, b, c}" items="A × B = {(a, b) : a ∈ A, b ∈ B}@Formally;;(1,a), (1,b), (1,c), (2,a), (2,b), (2,c)@one a;;2 · 3 = 6@two times three"
Formally, A cross B is the set of pairs a, b with a in A and b in B. Take one, two cross a, b, c. The pairs are one a, one b, one c, then two a, two b, two c. That's two times three, six pairs.

@words text="(a, 1) ≠ (1, a)" sub="A × B ≠ B × A"
Swap the factors and you get a different set. The pair a, one is a different object from one, a. The two products have the same size, but they aren't equal.

@chapter Sizes multiply
@math items="|A × B| = |A| · |B|@times the size;;A × ∅ = ∅@A cross the empty set"
Why do sizes multiply? Each pair is a first coordinate, chosen in the size of A ways, then a second, chosen independently in the size of B ways. So the size of A cross B is the size of A times the size of B. And if either factor is empty, A cross the empty set is empty.

@art empty-grid
There's no pair to form, which the formula also predicts. That's the product rule from counting. Independent choices multiply. They don't add.

@math items="|Aⁿ| = |A|ⁿ@to the n;;26⁴ = 456 976@twenty six"
The same goes for a set crossed with itself n times: its size is the size of A, to the n. With twenty six letters and n equal to four, that's the number of four letter strings: four hundred and fifty six thousand, nine hundred and seventy six.

@chapter Where products live
@art plane-point
Products are everywhere. The plane is the reals cross the reals, and coordinate geometry is just the observation that points are ordered pairs. Relations, coming next, are subsets of a product. And functions are relations with one extra condition.

@art bit-strings
Bit strings of length n are elements of zero, one, to the n. There are two to the n of them. And a set with n elements has two to the n subsets. That's not a coincidence.

@art subset-to-bits
A subset is exactly a choice of in or out for each element, and that's exactly a bit string. One per position, yes or no. This pairing between subsets and bit strings is why both are counted by two to the n.

@chapter A worked count
@math heading="Strings of length 4 from {a, b, c}" items="|{a, b, c}⁴| = 3⁴ = 81@three to the fourth;;no repeats: 3 · 2 · 1 · 0 = 0@no repeated letter"
How many strings of length four use letters from a, b, c? That's the fourth power of a three element set: three to the fourth, which is eighty one. How many use no repeated letter? Three choices, then two, then one, then zero. So none at all.

@words text="4 positions, 3 letters" sub="some letter repeats"
Four positions and three letters means some letter must be used twice. That's the pigeonhole principle, arriving early, by arithmetic.

@chapter Where people slip
@list heading="Common slips" items="Treating A × B and B × A as equal@The first|Adding sizes instead of multiplying@The second|Writing {a, b} when order matters@the third"
The first slip is treating A cross B and B cross A as the same set. They contain different objects. The second is adding sizes instead of multiplying. And the third is writing a set when order matters, which throws away exactly the information you were relying on.

@chapter Try it
@words text="P(A) ↔ {0, 1}ⁿ" sub="describe the pairing both ways"
Your turn. Describe the pairing between subsets and bit strings explicitly. Given a subset, produce its bit string. Given a bit string, produce its subset. That construction is what makes two to the n count both.

@end text="Ordered with repetition is a product"
You can slide the length and watch the product count change, on Learn. That's learn dot get er done dot I O.
