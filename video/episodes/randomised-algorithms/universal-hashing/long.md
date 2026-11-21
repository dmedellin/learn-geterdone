---
format: long
lesson: randomised-algorithms/universal-hashing
title: Universal hashing: a collision bound an adversary can't break
thumb: Randomise the function, not the keys
---

@chapter The attack
@title text="Universal Hashing" sub="Randomised Algorithms" art=thumb
Every nice fact about hash tables assumes something about the keys. Someone who can see your hash function can break that assumption on purpose. Universal hashing takes the assumption away.

@art one-slot-pile
Take h of k equals k mod eight. Perfectly reasonable. Now hand it to someone who wants your table to be slow. They insert eight, sixteen, twenty four, thirty two. Every key lands in slot zero, and every lookup walks the whole chain.

@chapter Move the randomness
@art random-function
The fix is to move the randomness. Don't assume the keys are random. Let the keys be whatever they are, even chosen by someone who's read your code. Instead, pick the hash function at random, from a family, when the table is built.

@math heading="Universal family" items="for every x ≠ y:  P_h(h(x) = h(y)) ≤ 1/m@for every pair"
A family is universal if, for every pair of distinct keys, a randomly drawn function from it makes them collide with probability at most one over m. The probability is only over the choice of function.

@words text="for every pair, the average over functions is small"
The order matters. For every pair, the average over functions is small. Not: for every function, most pairs are fine. The adversary may pick the pair after seeing the family. They just can't see the coin that picks the function.

@chapter A family that works
@math heading="The family" items="h_ab(k) = ((a·k + b) mod p) mod m@a times k plus b;;p prime,  a in 1..p − 1,  b in 0..p − 1@p is a prime"
Here's one. h of k is a times k plus b, mod p, then mod m. p is a prime bigger than every key. a is from one to p minus one, b from zero to p minus one. That's p times p minus one functions.

@art field-pairs
Why does it work? Modulo a prime, as a and b range over every allowed pair, the two values a x plus b and a y plus b range over every pair of different values, each exactly once. So you only need to count pairs of different values that agree mod m. That's at most one over m of them.

@chapter Count the family
@math heading="p = 11,  m = 4,  keys 3 and 7" items="10 × 11 = 110 functions@a hundred and ten;;20 collide@twenty of them;;20/110 = 2/11 ≈ 0.18  ≤  1/4@two elevenths"
The lab doesn't take the proof on trust. It counts. At p equals eleven and m equals four, there are a hundred and ten functions. For the keys three and seven, exactly twenty of them collide. That's two elevenths, about point one eight, under the bound of a quarter.

@art count-grid
Change the pair and the count changes. But over every pair of distinct keys below eleven, the worst is still two elevenths. This family does better than universality requires.

@list heading="Three full counts" items="p = 11, m = 4, pair 3, 7:  2/11 vs 1/4@p equals eleven|p = 7, m = 3, pair 1, 4:  10 in 42 = 5/21 vs 1/3@p equals seven|p = 13, m = 5, pair 2, 9:  22 in 156 = 11/78 vs 1/5@p equals thirteen"
Here are three complete counts. At p equals eleven, two elevenths against a quarter. At p equals seven, ten of forty two, five twenty firsts, against a third. At p equals thirteen, twenty two of a hundred and fifty six, eleven seventy eighths, against a fifth. Every one is under its bound.

@chapter What it buys
@art chain-length
So why bound pairs? Because a pair bound is enough for a chain length.

@words text="E[chain length] ≤ 1 + (n − 1)/m" sub="for every input"
For one key, the expected chain length is one, plus the chance each of the other keys lands with it. Universality and linearity give at most one plus n minus one over m, for every input, including hostile ones. Only pairs matter, so no independence between pairs is needed.

@art fixed-vs-family
Compare a fixed function. Fix k mod four, and let the adversary pick one and five. They collide with probability one. Certainty. Against the family it's two elevenths. That's the whole argument. What you don't get is a promise about the function you drew. If you drew a bad one, you re draw and rebuild, at a real cost.

@chapter Where people slip
@list heading="Common slips" items="Calling one hash function universal@The first|Keeping the random-keys assumption@The second|Expecting the count to equal 1/m@And the third"
The first slip is calling one hash function universal. The word describes a family. The second is quietly keeping the random keys assumption. And the third is expecting the counted rate to equal one over m. It's an inequality, and families usually beat it on any given pair.

@end text="Randomise the function"
Pick your own pair of keys and count every function in the family, on Learn. That's learn dot get er done dot I O.
