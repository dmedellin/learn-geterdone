---
format: long
lesson: intro-algorithms-algebraic-topics/number-theoretic-algorithms
title: Euclid's algorithm, modular equations and repeated squaring
thumb: Steps grow with digits
---

@chapter Useless no more
@title text="GCD and Modular Arithmetic" sub="Introduction to Algorithms, Sections 31.1–31.6" art=thumb
Chapter thirty one begins with a change of reputation.

@quote text="Number theory was once viewed as a beautiful but largely useless subject in pure mathematics." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 31"
Number theory was once viewed as a beautiful but largely useless subject in pure mathematics. Cryptography changed that. It rests on two facts: primes are easy to find, and their products are hard to factor.

@chapter Size is bits
@art bits-not-size
An input here is a few large numbers, and a number n is written in about log n bits. So an algorithm is efficient when its cost is polynomial in the number of bits, not in n. By that measure, trial division up to the square root of n is exponential.

@chapter Euclid's algorithm
@art euclid-staircase
Euclid rests on one identity: the gcd of a and b equals the gcd of b and a mod b. A number divides a and b exactly when it divides b and the remainder. Stop when the remainder is zero.

@math heading="gcd(1147, 851)" items="1147 = 1 · 851 + 296@eleven forty seven;;851 = 2 · 296 + 259@eight fifty one equals;;296 = 1 · 259 + 37@two ninety six equals;;259 = 7 · 37 + 0@two fifty nine equals"
On the lesson's pair, eleven forty seven equals one times eight fifty one, plus two ninety six. Eight fifty one equals two times two ninety six, plus two fifty nine. Two ninety six equals one times two fifty nine, plus thirty seven. Two fifty nine equals seven times thirty seven, remainder zero.

@words text="gcd = 37 in 4 calls" sub="Lamé's bound: fewer than 15"
So the gcd is thirty seven, in four recursive calls. Lamay's theorem promises fewer than fifteen for this pair, since eight fifty one lies between the Fibonacci numbers six ten and nine eighty seven.

@art fibonacci-worst
The worst pairs are consecutive Fibonacci numbers. Eighty nine and fifty five take nine divisions, every quotient one until the last. Since Fibonacci numbers grow exponentially, the number of calls is O of log b.

@chapter Extended Euclid
@math heading="ax + by = gcd" items="x = y′ · y = x′ − ⌊a/b⌋·y′@rewrites;;1147 · 3 + 851 · (−4) = 3441 − 3404 = 37@eleven forty seven times three"
The extended algorithm also returns x and y with a x plus b y equal to the gcd. On the way back from each call, it rewrites a mod b and collects terms. Here, eleven forty seven times three, plus eight fifty one times minus four, is thirty seven.

@chapter Modular equations
@art residue-clock
Now solve a x congruent to b, mod n. Let d be the gcd of a and n. The multiples of a, mod n, are exactly the multiples of d. So there's a solution exactly when d divides b, and then there are exactly d of them, spaced n over d apart.

@math heading="21x ≡ 14 (mod 35)" items="d = gcd(21, 35) = 7, divides 14@d is the gcd;;21·2 + 35·(−1) = 7 → x′ = 2@twenty one times two;;x = 2·(14/7) mod 35 = 4@the first solution;;4, 9, 14, 19, 24, 29, 34@seven solutions"
Solve twenty one x congruent to fourteen, mod thirty five. D is the gcd, seven, which divides fourteen. Twenty one times two, plus thirty five times minus one, is seven. So the first solution is two times fourteen over seven, mod thirty five, which is four. There are seven solutions, five apart.

@chapter Remainders and powers
@art two-clocks
The Chinese remainder theorem says that when the moduli share no factor, a number mod their product is the same thing as its list of remainders. Mod sixty three, that's a remainder mod seven and one mod nine.

@math heading="x ≡ 4 (mod 7), x ≡ 6 (mod 9)" items="c₁ = 9·4 = 36 · c₂ = 7·4 = 28@c one;;4·36 + 6·28 = 312 ≡ 60 (mod 63)@four times thirty six"
To go back from four and six, c one is nine times four, thirty six, and c two is seven times four, twenty eight. Four times thirty six plus six times twenty eight is three twelve, which is sixty mod sixty three.

@art repeated-squaring
To compute a to the b mod n, read the bits of b, squaring at every bit and multiplying by a at every one bit. Reduce after each step, so the numbers stay small. In the lab, five to the one seventeen mod three ninety one is two oh one, in six squarings and five multiplications, against a hundred sixteen done one at a time.

@chapter Where people slip
@list heading="Common slips" items="Measuring by the number's size@The first|Expecting one solution@The second|Reducing only at the end@the third"
The first slip is measuring a number algorithm by the size of the number, instead of its bits. The second is expecting a linear congruence to have one solution. It can have none, or d. And the third is computing the power first, and reducing at the end. Five to the one seventeen has eighty two digits.

@chapter Try it
@words text="(377, 233) · 15x ≡ 9 (mod 24) · 3⁴⁵ mod 101" sub="write 45 in binary first"
Your turn. Run extended Euclid on three seventy seven and two thirty three, and compare with Lamay's bound. Solve fifteen x congruent to nine, mod twenty four. And compute three to the forty five mod a hundred and one by repeated squaring.

@end text="Run Euclid yourself"
You can run Euclid, congruences, remainders and powers in one panel, on Learn. That's learn dot get er done dot I O.
