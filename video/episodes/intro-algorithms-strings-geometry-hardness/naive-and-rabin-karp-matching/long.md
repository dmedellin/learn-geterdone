---
format: long
lesson: intro-algorithms-strings-geometry-hardness/naive-and-rabin-karp-matching
title: Naive and Rabin-Karp string matching, and the hope in a hash
thumb: Equal hashes are a hint
---

@chapter Every shift is a candidate
@title text="Naive and Rabin-Karp String Matching" sub="Introduction to Algorithms, Sections 32.1–32.2" art=thumb
Chapter thirty two finds a pattern in a text. Here's how it states the problem.

@art shifts
The text has n characters and the pattern m. The pattern occurs with shift s when the m characters after position s are exactly the pattern. Shifts run from zero to n minus m, so there are n minus m plus one candidates, and the task is to report every valid one.

@chapter The naive matcher
@art naive-slide
The naive matcher tries every shift, and at each one compares characters until one differs or all m agree. Its worst case is n minus m plus one, times m comparisons.

@words text="aaaa…a searched for aa…a" sub="every shift valid · every comparison needed"
And that's reached. A text of one repeated letter, searched for a run of the same letter, makes every shift valid and every comparison necessary. The diagnosis is that the naive matcher throws away what one shift taught it, before trying the next.

@chapter Strings as numbers
@art rolling-window
Rabin and Karp read each window of m characters as an m digit number. The next window's number follows from the current one: drop the high digit, multiply by the radix, and add the new low digit. All the window values together cost linear time.

@math heading="Too big for a word" items="reduce mod a prime q@modulo a prime;;h = d^(m−1) mod q@the weight;;different residues ⇒ different strings@different residues;;equal residues ⇒ check the characters@equal residues"
But an m digit number doesn't fit in a word. So everything is reduced modulo a prime q, with the weight of the high digit precomputed. Now different residues prove the window differs. Equal residues prove nothing, so every match is checked character by character.

@art fingerprint
Think of the residue as a fingerprint of the window. Fingerprints are small enough to compare in one step, and different fingerprints settle the question. But two different windows can share one.

@chapter The hope
@quote text="If q is large enough, then we hope that spurious hits occur infrequently enough that the cost of the extra checking is low." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 32.2"
The word to notice is hope. If q is large enough, then we hope that spurious hits occur infrequently enough that the cost of the extra checking is low.

@list heading="Two strengths of claim" items="worst case: Θ((n − m + 1)·m), proved@The worst case|expected O(n + m), under a heuristic@expected"
The section keeps two claims apart. The worst case is still the naive one, and that's proved. The expected time of O of n plus m rests on an assumption the authors label as one: that reduction mod q behaves like a random map, so spurious hits number about n over q.

@chapter Counting the hope
@math heading="“a banana and a bandana in a cabana” · ana · base 256" items="32 windows · naive bound 96@thirty two windows;;valid shifts: 3, 5, 19, 31@valid shifts;;mod 11: 1 collision, at shift 10@modulus eleven;;mod 17: 0 collisions@modulus seventeen"
Here's the lesson's own text, with the pattern a n a. Thirty two windows, so the naive bound is ninety six comparisons. The valid shifts are three, five, nineteen and thirty one. At modulus eleven there's one collision, at shift ten: an n, a d and a space. At modulus seventeen, none.

@art collision
Now set the modulus to thirteen. Suddenly there are eight spurious hits, thirty six characters compared, and twenty four wasted. Nothing about thirteen is small next to m equals three. The cause is in the text.

@art modulus-sweep
The lab also sweeps every prime under two hundred. On this text, seventeen of those forty six primes produce at least one collision, the largest of them one eighty one.

@words text="One text, one modulus" sub="the n/q estimate assumes random residues"
That's the gap the book's hedge leaves. The estimate assumes this text's residues look random, and on one text at one modulus they need not. A count is evidence about this text, not a test of the assumption.

@chapter Where people slip
@list heading="Common slips" items="Taking a matching residue for a match@The first|Reading expected time as a guarantee@The second|Expecting a larger modulus always to help@the third"
The first slip is taking a matching residue for a match. Fingerprints collide. The second is reading the expected time as a guarantee. And the third is expecting a larger modulus always to help. This text collides at thirteen but not seventeen, at twenty three but not nineteen.

@chapter Try it
@code block=1 lines=1-3 focus="1@same text|3@modulus thirteen"
Your turn. Use the same text and pattern, with modulus thirteen. Without computing a single window's hash, explain why thirteen makes so many windows collide. Hint: find the codes of a, n and space, and two fifty six, mod thirteen.

@end text="Count the collisions"
You can sweep the modulus and count every spurious hit, on Learn. That's learn dot get er done dot I O.
