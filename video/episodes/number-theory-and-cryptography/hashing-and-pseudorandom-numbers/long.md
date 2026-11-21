---
format: long
lesson: number-theory-and-cryptography/hashing-and-pseudorandom-numbers
title: Hashing and pseudorandom numbers: mod at work
thumb: Pick the modulus carefully
---

@chapter Two everyday uses
@title text="Hashing and Pseudorandom Numbers" sub="Number Theory and Cryptography" art=thumb
Two things your software does constantly, storing keys in a hash table and generating random looking numbers, are both built on mod. Both work because of number theory, and both fail in ways number theory predicts.

@chapter Hash functions
@words text="h(k) = k mod m" sub="a large key space → {0, 1, …, m − 1}"
A hash function maps a huge space of keys into a small range of slots, zero up to m minus one. The simplest one is k mod m.

@art pigeonholes
Collisions are unavoidable. There are more possible keys than slots, so by the pigeonhole principle some slot gets more than one key. That's why hash tables are designed around collisions, by chaining, or by probing for another slot.

@chapter Choosing the modulus
@art pile-up
Now, which m? Say m is a power of two, two to the r. Then k mod m depends only on the low r bits of k. Hash memory addresses with m equal to sixteen, when every address is a multiple of sixteen, and every key lands in slot zero.

@art spread-out
Use seventeen instead, and the same keys spread across all seventeen slots. A prime modulus has no structure for your keys to line up with. It uses every bit.

@words text="first collision ≈ √m insertions" sub="10⁶ slots → about 1000 keys"
How soon do collisions start? The birthday problem says once the number of keys is around the square root of m. So a table of a million slots sees its first collision after about a thousand insertions. That's why load factors are managed, rather than collisions avoided.

@chapter Linear congruential generators
@words text="xₙ₊₁ = (a·xₙ + c) mod m" sub="multiplier a, increment c, modulus m, seed x₀"
Now random numbers. A linear congruential generator starts from a seed, and each next value is a times the last one, plus c, all mod m. Those three parameters fix the whole sequence.

@art cycle-loop
There are only m possible values, so the sequence must eventually repeat. Pigeonhole again. The period is how long that takes, and it's at most m.

@list heading="Hull–Dobell: full period exactly when" items="gcd(c, m) = 1@the gcd of c|every prime dividing m divides a − 1@must be divisible by every|if 4 ∣ m then 4 ∣ a − 1@by four"
The Hull Dobell theorem says when you get the full period m, for every seed. The gcd of c and m must be one. A minus one must be divisible by every prime that divides m. And if four divides m, a minus one must be divisible by four.

@chapter Two generators
@math heading="m = 16, c = 3, seed 1" items="a = 5:  1, 8, 11, 10, 5, 12, 15, 14, 9, 0, 3, 2, 13, 4, 7, 6, 1@with a equal to five;;period 16  ✓@every value;;a = 6:  1, 9, 9, 9, …@change a to six;;2 ∤ (a − 1) = 5  ✗@two doesn't divide"
Take m sixteen, c three, seed one. With a equal to five, all three conditions hold, and the sequence runs one, eight, eleven, ten, and on through every value before returning to one. Period sixteen. Now change a to six. The sequence is one, nine, nine, nine, forever. Two doesn't divide five, so the second condition fails.

@art dead-generator
One parameter changed by one, and the generator went from every value to a constant. That failure isn't a slow decline. It's total, and easy to ship without noticing. The theorem turns it into three divisibility checks.

@chapter Full period isn't enough
@art hyperplanes
Even a full period generator isn't statistically good. Consecutive values fall on a small number of planes in higher dimensions. RANDU, an LCG shipped by IBM in the nineteen sixties, was so bad in three dimensions that results computed with it were later retracted.

@words text="Looks random ≠ cannot be predicted" sub="never use an LCG for keys or tokens"
And for security, it's worse. Watch a few outputs and you can work out the parameters, and so every future value. That's fine for a simulation, and fatal for a key or a session token. Looks random and cannot be predicted are different properties.

@chapter Where people slip
@list heading="Common slips" items="A power-of-two hash modulus with structured keys@The first|Assuming full period means good statistics@The second|Using a general generator for security@And the third"
The first slip is using a power of two as a hash modulus with structured keys. The second is assuming a full period generator is statistically good. And the third is using a general purpose generator for security.

@chapter Try it
@words text="m = 100" sub="one passing (a, c), one failing"
Your turn. For m equal to a hundred, find a multiplier and an increment that give the full period, and another pair that fails. Check the three conditions, then run them and see.

@end text="Run a generator"
You can run a generator, change one parameter, and watch it live or die, on Learn. That's learn dot get er done dot I O.
