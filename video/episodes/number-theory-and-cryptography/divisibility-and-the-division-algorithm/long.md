---
format: long
lesson: number-theory-and-cryptography/divisibility-and-the-division-algorithm
title: The division algorithm: why minus seven mod three is two
thumb: The remainder is never negative
---

@chapter The question
@title text="Divisibility and the Division Algorithm" sub="Number Theory and Cryptography" art=thumb
Every time you divide one whole number by another, you get a quotient and a remainder. That sounds like primary school. But one careful statement of it holds up this entire course, from greatest common divisors all the way to RSA.

@art equal-groups
Start with the simplest case, when nothing is left over. Twelve counters split into groups of three, exactly, with none spare. We say three divides twelve.

@words text="b ∣ a  means  a = bk" sub="for some integer k, with b ≠ 0"
Here's the precise version. For integers a and b, with b not zero, b divides a means there's an integer k with a equal to b times k. Then b is a divisor, or a factor, of a.

@words text="3 ∣ 12 is true · 3/12 is ¼" sub="a statement, not a number"
Notice what kind of thing that is. Three divides twelve is a statement, true or false. Three over twelve is a number, a quarter. Mixing those two up is one of the first slips people make.

@chapter Three properties
@math heading="For integers a, b, c, d" items="d ∣ a and d ∣ b  ⟹  d ∣ (ax + by)@if d divides a;;a ∣ b and b ∣ c  ⟹  a ∣ c@if a divides b;;d ∣ a, a ≠ 0  ⟹  |d| ≤ |a|@and if d divides"
Divisibility has three basic properties. First, if d divides a and d divides b, then d divides a x plus b y, for any integers x and y. Second, if a divides b and b divides c, then a divides c. And if d divides a nonzero a, then d is no bigger than a in size.

@art shared-ruler
The first one is the workhorse, and its proof is one line. Write a as d times m, and b as d times n. Then a x plus b y is d times m x plus n y, and that bracket is an integer. So d divides it.

@words text="d ∣ (ax + by)" sub="Euclid's algorithm · infinitely many primes · Bézout"
That one line is what makes the Euclidean algorithm work, what proves there are infinitely many primes, and what makes Bezout's identity useful. Almost every proof in this course uses it.

@chapter The division algorithm
@words text="a = qb + r,  0 ≤ r < b" sub="q and r are unique"
Now the theorem itself. For any integer a and any positive integer b, there are unique integers q and r with a equal to q b plus r, and r at least zero but less than b.

@art leftover-blocks
Existence comes from the well-ordering principle. Look at all the non-negative numbers of the form a minus q b. There's a smallest one, r. If r were b or more, you could take away one more b and get something smaller, which can't happen. So r is less than b.

@art smallest-leftover
Uniqueness: suppose two pairs both work. Then b times the difference of the quotients equals the difference of the remainders. The right side is smaller than b in size, and the left side is a multiple of b, so both are zero. The pairs are the same.

@art remainder-wheel
That uniqueness is what makes the notation legitimate. a div b and a mod b name specific integers, not one of several possibilities. And a mod b always lands between zero and b minus one.

@chapter Negative numbers
@math heading="−7 divided by 3" items="−7 = (−3)(3) + 2@minus three times three;;q = −3,  r = 2@so the quotient;;✗  −7 = (−2)(3) + (−1)@not minus two"
Here's where it gets interesting. Divide minus seven by three. Minus seven is minus three times three, plus two, so the quotient is minus three and the remainder is two. It's not minus two times three, plus minus one, because the theorem needs the remainder to be at least zero.

@art number-line-steps
So the quotient rounds toward negative infinity, not toward zero. You step left past minus seven, to minus nine, then come back up by two.

@words text="−7 % 3:  C gives −1,  Python gives 2" sub="the mathematics agrees with Python"
And programming languages disagree with each other here. C style percent gives minus one. Python gives two. The mathematical convention is Python's, and it's the one that makes modular arithmetic work.

@chapter Divisibility by three
@math heading="Why the digit-sum test works" items="10ⁱ − 1 = 9, 99, 999, …  so  3 ∣ (10ⁱ − 1)@a string of nines;;n − (digit sum) = Σ dᵢ(10ⁱ − 1)@minus its digit sum;;3 ∣ n  ⟺  3 ∣ digit sum@three divides n;;4728 → 4 + 7 + 2 + 8 = 21,  4728 = 3 × 1576@four thousand seven hundred"
Here's the property at work. Every ten to a power, minus one, is a string of nines, so three divides it. A number minus its digit sum is a combination of those, so three divides that difference too. So three divides n exactly when three divides its digit sum. Four thousand seven hundred and twenty eight has digit sum twenty one, and it is three times fifteen hundred and seventy six.

@chapter Where people slip
@list heading="Common slips" items="Allowing a negative remainder@The first|Confusing b ∣ a with b/a@The second|Forgetting b ≠ 0@And the third"
The first slip is allowing a negative remainder. Minus seven mod three is two, and mixing language conventions with the mathematical one silently breaks modular arithmetic. The second is confusing b divides a with b over a. And the third is forgetting b can't be zero.

@chapter Try it
@words text="d ∣ (a + b) and d ∣ a  ⟹  d ∣ b ?" sub="one use of the linear-combination property"
Your turn. Prove that if d divides a plus b, and d divides a, then d divides b. It's one application of the property, and it's the shape of argument every later lesson repeats. Then work out minus eight mod three and minus nine mod three.

@end text="Divide, and watch the remainder"
You can divide negative numbers and watch the remainder stay non-negative, on Learn. That's learn dot get er done dot I O.
