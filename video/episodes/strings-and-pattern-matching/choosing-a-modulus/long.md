---
format: long
lesson: strings-and-pattern-matching/choosing-a-modulus
title: Choosing a Rabin-Karp modulus: why bigger isn't automatically safer
thumb: 137 collides, 11 doesn't
---

@chapter The question
@title text="Choosing a Modulus, and What the Sweep Says" sub="Strings and Pattern Matching" art=thumb
Rabin Karp's collisions depend on the modulus. So surely you just pick a big enough one, and the collisions go away? On one text, a big prime gives none. But sweep through the small primes, and the picture isn't a threshold at all.

@words text="modulus 1 000 003" sub="pattern hashes to 383 964 · 4 candidates · 0 collisions"
Keep the rain in spain, the pattern a i n, and base two hundred and fifty six. Set the modulus to one million and three. The pattern hashes to three hundred and eighty three thousand, nine hundred and sixty four. Four windows match it, all four are real, and the collision counter reads zero.

@art clean-run
The verification bill is twelve characters, four times three, the smallest it can be. That's the good case. But it's a measurement of one choice. The same text at modulus eleven is also clean, and eleven is nearly five orders of magnitude smaller.

@chapter The sweep
@art prime-strip
So the lab keeps the text and the base, and tries every prime below two hundred, all forty six of them. At each one, it counts how many windows collide.

@list heading="46 primes under 200" items="18 collide@Eighteen|largest that collides: 137@largest|smallest that's clean: 11@smallest|worst: 2, with 18 collisions@worst"
Eighteen of the forty six collide. The largest that collides is a hundred and thirty seven. The smallest that's clean is eleven. And the worst is two, with eighteen collisions on forty one windows.

@words text="41 ✗ · 43 ✓ · 47 ✗"
The clean and colliding primes interleave. Forty one and forty seven collide. Forty three, between them, doesn't. So there's no threshold above which every modulus is safe for this input.

@chapter Why it isn't monotone
@math heading="A collision at q" items="window value − pattern value = D@difference;;collision at q  ⟺  q divides D@q divides"
Here's why. A window collides at modulus q exactly when q divides the difference between that window's value and the pattern's. That difference is a fixed integer.

@art divisors
And whether a prime divides a fixed number has nothing to do with how big the prime is. A hundred and thirty seven divides one of these differences. Eleven divides none of them. Notice the proof shape. The claim is that such a pair exists, so one exhibited pair proves it.

@chapter What is proved
@art random-pick
What's actually proved is different. Pick q at random from a big enough range, and the chance that it divides any of the differences is small. Roughly n over q spurious hits, for a big prime. That's a statement about the random choice.

@art fixed-target
Read what it doesn't say. It doesn't say a particular large prime is safe on a particular text. It doesn't say collisions fall as the modulus rises. And if the modulus is a constant in your source code, there's no random choice to average over, and an adversary can build a text against it.

@chapter What a collision costs
@math heading="Verification bill" items="modulus 41: 7 candidates → 21, 9 wasted@forty one;;modulus 1 000 003: 4 candidates → 12, none wasted@one million and three;;modulus 2: 22 candidates, 18 collisions@modulus two"
Each candidate costs m comparisons. At modulus forty one, seven candidates cost twenty one, nine wasted. At one million and three, four cost twelve, none wasted. At modulus two, twenty two candidates, eighteen of them collisions. 

@art verify-bill
In that worst direction, the algorithm slides toward the naive matcher with extra arithmetic. So the modulus isn't a tuning detail. It decides how much of the constant work per window survives contact with the input.

@words text="binary preset: 6 of 46 · abracadabra: 15 of 46"
On other presets, the sweep moves too: six of forty six on the binary one, fifteen on the abracadabra one. But those also change the base, pattern and window count, so don't pin the difference on any one of them.

@chapter Where people slip
@list heading="Common slips" items="Treating the modulus as a threshold@The first|Reading the expectation as a bound on your input@The second|Comparing presets without holding the base fixed@The third"
The first slip is treating the modulus as a threshold to exceed. The second is reading the expectation as a bound on the input in front of you. The third is comparing collision counts across presets while four things change at once.

@chapter Try it
@words text="'ain' and ' th'" sub="base 256"
Your turn. The values of a i n and space t h are six million, three hundred and eighty three thousand, nine hundred and eighty two, and two million, one hundred and twenty six thousand, nine hundred and fifty two. Find their difference, and check whether forty one divides it, and whether eleven does.

@end text="Sweep the primes yourself"
You can sweep every prime modulus on your own text, and see which collide, on Learn. That's learn dot get er done dot I O.
