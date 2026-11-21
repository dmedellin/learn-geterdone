---
format: long
lesson: number-theory-and-cryptography/modular-arithmetic
title: Modular arithmetic: computing with remainders
thumb: Reduce early, cancel carefully
---

@chapter Same remainder
@title text="Modular Arithmetic" sub="Number Theory and Cryptography" art=thumb
What's the last digit of seven to the power one hundred? That number has eighty five digits, and you can find its last one with four multiplications. The trick is arithmetic on remainders.

@words text="a ≡ b (mod m)  ⟺  m ∣ (a − b)" sub="same remainder on division by m"
Here's the definition. For m bigger than zero, a is congruent to b mod m when m divides a minus b. Equivalently, a and b leave the same remainder when you divide by m.

@art clock-classes
Think of a clock. Wrap the integers around a circle with m positions, and two numbers are congruent when they land in the same place.

@art partition-rows
Congruence is an equivalence relation. It's reflexive, symmetric and transitive. So it splits the integers into classes, exactly m of them, one for each remainder from zero up to m minus one. That set of classes is written z mod m z, or z sub m.

@chapter Arithmetic is well defined
@math heading="a ≡ b,  c ≡ d  (mod m)" items="a = b + ms,  c = d + mt@write a as;;a + c = (b + d) + m(s + t)@then a plus c;;ac = bd + m(bt + ds + mst)@and a c"
Now the key fact. If a is congruent to b, and c is congruent to d, then the sums are congruent and so are the products. Write a as b plus m s, and c as d plus m t. Then a plus c is b plus d, plus a multiple of m. And a c is b d, plus a multiple of m.

@art reduce-first
That means you can reduce at any point. To find seventeen times twenty three, mod five, reduce first. Seventeen is two and twenty three is three, mod five. Two times three is six, which is one. No need to compute three hundred and ninety one and divide.

@chapter The last digit of seven to the hundred
@math heading="7¹⁰⁰ mod 10" items="7¹ ≡ 7@seven to the first;;7² = 49 ≡ 9@seven squared;;7³ ≡ 63 ≡ 3@seven cubed;;7⁴ ≡ 21 ≡ 1@seven to the fourth;;7¹⁰⁰ = (7⁴)²⁵ ≡ 1²⁵ = 1@a hundred is"
Back to the opening question. Seven to the first is seven. Seven squared is forty nine, which is nine, mod ten. Seven cubed is nine times seven, sixty three, which is three. Seven to the fourth is three times seven, twenty one, which is one. And a hundred is four times twenty five, so seven to the hundred is one to the twenty fifth. The last digit is one.

@art power-cycle
The powers cycle, seven, nine, three, one, with period four. That four isn't a coincidence, as Euler's theorem will show later in the course.

@chapter Where it breaks
@math heading="Cancellation fails" items="2 · 3 = 6 ≡ 16 = 2 · 8  (mod 10)@two times three;;but  3 ≢ 8  (mod 10)@but three;;gcd(2, 10) = 2 ≠ 1@because the gcd"
Most rules carry over, but one doesn't. Two times three is six, which is congruent to sixteen, two times eight, mod ten. But three isn't congruent to eight. You can't cancel the two, because the gcd of two and ten is two, not one.

@art collide
The rule is this. If a c is congruent to b c, and the gcd of c and m is one, then a is congruent to b. Coprimality gives c an inverse, and you multiply by it. Without coprimality, different numbers collide.

@art mult-table
And you get zero divisors. Two times five is ten, which is zero mod ten, though neither factor is zero. That can't happen in the integers. With a prime modulus it never happens: every nonzero element has an inverse, and z mod p is a field. For a composite m, only the elements coprime to m are invertible.

@chapter Casting out nines
@math heading="Check 4321 × 5678 = 24 534 638" items="4321 → 10 ≡ 1@four three two one;;5678 → 26 ≡ 8@five six seven eight;;1 · 8 = 8@one times eight;;24 534 638 → 35 ≡ 8  ✓@the claimed answer"
Here's a classic use. Ten is one, mod nine, so every number is congruent mod nine to its digit sum. To check four three two one times five six seven eight, the digit sums are ten, which is one, and twenty six, which is eight. One times eight is eight. The claimed answer has digit sum thirty five, also eight. Consistent. It catches most single digit errors, though not a transposition.

@chapter Where people slip
@list heading="Common slips" items="Cancelling without checking the gcd@The first|Reducing exponents modulo m@The second|Leaving negative representatives@And the third"
The first slip is cancelling a common factor without checking the gcd. The second is reducing an exponent modulo m. Exponents reduce modulo something else, phi of m, which comes later. And the third is leaving negative representatives. Add m to land between zero and m minus one.

@chapter Try it
@words text="123 · 456 (mod 7)" sub="reduce each factor first"
Your turn. Compute a hundred and twenty three times four hundred and fifty six, mod seven, by reducing each factor first. Two small multiplications instead of one big one, and the same answer.

@end text="See the tables"
You can see the addition and multiplication tables for any modulus, on Learn. That's learn dot get er done dot I O.
