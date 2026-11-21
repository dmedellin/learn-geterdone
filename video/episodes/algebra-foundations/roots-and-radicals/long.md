---
format: long
lesson: algebra-foundations/roots-and-radicals
title: Roots and radicals: one symbol, one number
thumb: √9 is 3, not ±3
---

@chapter The question
@title text="Roots and Radicals" sub="Algebra Foundations" art=thumb
The square root of nine. Is it three, or plus or minus three? It's three, and only three. A radical sign names one number, not two, and that's a convention worth stating plainly.

@art square-side
For x at least zero, the root of x is the one number r that's at least zero and whose square is x. The root of zero is zero. Picture the side of a square whose area is x.

@chapter One number, not two
@math items="x² = 9   →   x = ±3@x squared equals nine;;√9 = 3@the root of nine alone"
So where does plus or minus come from? From solving an equation. x squared equals nine has two solutions, three and minus three. The plus or minus is written there on purpose, because the root of nine alone only supplies three.

@art principal-root
That's why the quadratic formula carries a plus or minus in front of its root. The equation has two answers. The symbol names one.

@words text="√(−4): no real value" sub="every real square is ≥ 0"
And for a negative number? The square of any real number is at least zero, so nothing real squares to minus four. On this course, the square root of a negative number has no value.

@chapter Index and sign
@art odd-even
An n th root of x is a number r with r to the n equal to x, and n is called the index. When n is odd, every real has exactly one real n th root, with the same sign. When n is even, a positive x has two, and the radical names the positive one. A negative x has none.

@math items="∛8 = 2@cube root of eight;;∛(−8) = −2@minus eight is minus two;;⁴√16 = 2@fourth root of sixteen;;⁴√(−16):   no real value@no real value"
So the cube root of eight is two, and the cube root of minus eight is minus two. The fourth root of sixteen is two, even though minus two to the fourth is sixteen as well. And the fourth root of minus sixteen has no real value.

@chapter Why x squared needs bars
@math items="x = 5:    √(5²) = √25 = 5 = |5|@at five;;x = −5:    √((−5)²) = √25 = 5 = |−5|@at minus five"
Here's a cancellation people get wrong. The root of x squared has to be at least zero. At five, it's the root of twenty five, which is five. At minus five, it's still the root of twenty five, which is five, not minus five.

@art mirror-fold
So the root of x squared isn't x. It's the absolute value of x. For an odd index, no bars are needed: the cube root of x cubed is x for every real x, because a cube keeps the sign.

@chapter Simplifying
@art sum-split
For a and b at least zero, the root of a b is root a times root b, and quotients split the same way. Sums don't. The root of nine plus sixteen is five, but root nine plus root sixteen is seven.

@art prime-pairs
To simplify, factor the number under the root into primes, and take out each prime in complete groups of the index. Pairs for a square root, triples for a cube root. Whatever can't fill a group stays in.

@math heading="√72" items="72 = 2³ · 3² = 2² · 3² · 2@two cubed times three squared;;out: 2 and 3,    left in: 2@come out;;√72 = 6√2@six root two;;check:   (6√2)² = 36 · 2 = 72@check"
Seventy two is two cubed times three squared. One pair of twos and one pair of threes come out, and a single two stays in. So the root of seventy two is six root two. Check: six root two, squared, is thirty six times two, which is seventy two.

@math heading="∛(−54)" items="−54 = −(3³ · 2)@minus fifty four;;∛(−54) = −3 · ∛2@minus three times;;check:   (−3)³ · 2 = −54@cubing"
Odd index next: the cube root of minus fifty four. That's minus, three cubed times two. A triple of threes comes out, with the minus sign, and a two stays in. So it's minus three times the cube root of two. Cubing it back gives minus fifty four.

@words text="√(18/25) = 3√2 / 5"
And a fraction. The root of eighteen over twenty five is root eighteen over root twenty five. Root eighteen is three root two, and root twenty five is five. So it's three root two, over five.

@chapter Where people slip
@list heading="Common slips" items="√9 = ±3@plus or minus three|Splitting a root over a sum@splitting a root|√(x²) = x@cancelling"
Three slips. Writing that the root of nine is plus or minus three. Splitting a root over a sum. And cancelling the root of x squared to x, when it's really the absolute value of x.

@chapter Try it
@words text="√108" sub="factor first"
Your turn: the root of one hundred eight. Repeated division gives two squared times three cubed. Take one two and one three out, and stop, because a single three remains. You should get six root three.

@end text="Factor first, then pull out"
You can factor any number under a root and see what comes out and what stays in, on Learn. That's learn dot get er done dot I O.
