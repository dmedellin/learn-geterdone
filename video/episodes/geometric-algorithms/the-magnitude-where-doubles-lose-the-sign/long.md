---
format: long
lesson: geometric-algorithms/the-magnitude-where-doubles-lose-the-sign
title: Where floating point loses a right turn, and why it never flips one
thumb: Collapse, never a flip
---

@chapter The same turn at every size
@title text="The Magnitude Where Doubles Lose the Sign" sub="Geometric Algorithms" art=thumb
Here's a right turn that never changes. Make the numbers bigger and bigger, and at one exact size, ordinary floating point stops seeing it.

@math heading="The needle at 2ᵏ" items="a = (0, 0)@Let a be;;b = (2ᵏ + 1, 2ᵏ)@Let b be;;c = (2ᵏ, 2ᵏ − 1)@let c be"
Fix a whole number k. Let a be zero, zero. Let b be two to the k plus one, two to the k. And let c be two to the k, two to the k minus one.

@math heading="orient(a, b, c)" items="(2ᵏ + 1)(2ᵏ − 1) − 2ᵏ·2ᵏ@two to the k plus one;;= (2²ᵏ − 1) − 2²ᵏ@difference of squares;;= −1@minus one"
With a at the origin, the determinant is two to the k plus one, times two to the k minus one, minus two to the k squared. The first product is a difference of squares, two to the two k, minus one. Subtract and everything cancels except minus one. Every member of this family is the same right turn.

@art thin-triangle
Geometrically it's a long, thin sliver of a triangle, with area one half however far out it reaches. So sweeping k upward isn't sweeping through harder geometry. It's one question with a fixed answer, asked at larger and larger magnitudes.

@chapter The sweep
@art needle-sweep
The lab sweeps k from twenty to forty eight, twenty nine magnitudes. For each one it prints the exact determinant, the double precision determinant, and whether their signs agree. It doesn't quote a threshold. It counts.

@words text="22 of 29 wrong" sub="every one from 2²⁷ up"
The count is twenty two wrong, every one from two to the twenty seven upward, and seven right below that. Each failure is the double reporting zero: collinear.

@chapter Why twenty seven
@art bit-boxes
This isn't small errors piling up. There's no drift at all. Below the threshold the answer is exactly right, and above it the answer is exactly zero. It's a collision, and the lab prints both columns so you see it as a step.

@art spacing-ticks
A double holds fifty three bits of significand. Every integer up to two to the fifty three is exact. Above that, the representable numbers spread out, two apart, then four, and so on.

@math heading="The two products" items="2²ᵏ − 1  and  2²ᵏ@the two products;;2k ≤ 53  ⟹  both exact, answer −1@at most fifty three;;2k ≥ 54  ⟹  both round to 2²ᵏ, answer 0@fifty four or more"
The two products are two to the two k minus one, and two to the two k. When two k is at most fifty three, both are exact, and the answer is minus one. That's k up to twenty six. At fifty four or more, the gap is at least two, so both round to the same double, and the difference is zero.

@chapter Either side of the line
@math heading="k = 26  and  k = 27" items="4503599627370495 − 4503599627370496 = −1@twenty six;;18014398509481983 → 18014398509481984@twenty seven;;difference 0: called collinear@called collinear"
At k equals twenty six, the products are one apart, both under two to the fifty three, so the difference is minus one. At twenty seven, the first product isn't representable and rounds up to the second. The difference is zero, and a right turn is called collinear.

@art product-collision
One power of two apart, and the verdict changes from right to wrong. The coordinates are only about sixty seven million. It's the products that are huge. So double the bit width before you compare with fifty three.

@chapter A collapse, never a flip
@art one-sided-arrow
Here's the useful part. The coordinate differences are integers below two to the fifty three, so they're exact. Only the two products and the final subtraction round. And rounding to nearest is monotone: if one product is smaller, its rounded value can't end up bigger. It can only tie.

@words text="the double can lose a turn" sub="it cannot invent the opposite one"
So the double test can collapse a turn to zero, and it can never report the opposite turn. A hull built with it can be missing a corner, but can't have one in the wrong place. The checker threw thirty thousand random near collinear triples at both routes. They disagreed one thousand two hundred and fifty eight times, and never once the other way.

@chapter Where people slip
@list heading="Common slips" items="Checking the inputs, not the products@The first|Reading 22 of 29 as a failure rate@The second|Fixing it with a tolerance@And the third"
The first slip is checking the size of the inputs instead of the products. The second is reading twenty two of twenty nine as a failure rate. The family was built to fail, so the count finds the threshold, nothing more. And the third is fixing it with a tolerance, which turns real turns into collinearities and can't help when the value is exactly zero.

@chapter Try it
@words text="k = 26  vs  k = 27" sub="compute both products by hand"
Try it yourself. Write out the two products at k equals twenty six and twenty seven, and check which one stops being representable. The fix is exact arithmetic on the predicate.

@end text="Watch the sign collapse"
You can sweep all twenty nine magnitudes yourself on Learn. That's learn dot get er done dot I O.
