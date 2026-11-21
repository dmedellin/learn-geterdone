---
format: long
lesson: strings-and-pattern-matching/a-rolling-hash-and-its-collisions
title: Rabin-Karp: a rolling hash, and three collisions you can check by hand
thumb: Equal hash is not a match
---

@chapter The question
@title text="A Rolling Hash, and a Collision You Can Read" sub="Strings and Pattern Matching" art=thumb
What if, instead of comparing characters, you turned every window of the text into a single number, and compared numbers? That's Rabin Karp. It's fast. But equal numbers don't mean equal strings, and you can see exactly where that bites.

@math heading="The window hash" items="H(w) = (w[0]·b^(m−1) + w[1]·b^(m−2) + … + w[m−1]) mod q@H of w"
Pick a base b and a modulus q. H of w, the hash of a window w reads its characters as the digits of a number in base b, each character contributing its code, and takes the result modulo q.

@chapter Rolling forward
@art roll-window
The trick is that the next window's hash comes from the current one in constant time. Drop the leading character's contribution, multiply by the base to shift everything up a place, add the new trailing character, and reduce.

@math heading="The roll" items="H(w′) = (b · (H(w) − t[s] · b^(m−1)) + t[s+m]) mod q@H of w prime"
In symbols, H of w prime is b times, H of w minus the leading character times b to the m minus one, plus the new character, all mod q. Reduction commutes with addition and multiplication, so reducing at every step gives the same answer as reducing at the end.

@art hash-tokens
So the scan is n steps of constant arithmetic, whatever m is. Plus m character comparisons for each window whose hash matches the pattern's. That second part is the one that depends on the text.

@chapter Seven candidates
@words text="the rain in spain stays mainly in the plain" sub="pattern ain · base 256 · modulus 41"
The lab opens on the rain in spain stays mainly in the plain, with pattern a i n, base two hundred and fifty six and modulus forty one. The pattern hashes to thirty six.

@list heading="Windows hashing to 36" items="4 matches: 5, 14, 25, 40@Four are|3 collisions: 33 ' th' · 36 'e p' · 38 'pla'@other three"
Of the forty one windows, seven hash to thirty six. Four are the real occurrences, at five, fourteen, twenty five and forty. The other three are at thirty three, thirty six and thirty eight. Their characters are a space then t h, then e space p, then p l a. None of those is a i n.

@math heading="Check one by hand" items="' th' = 32·256² + 116·256 + 104 = 2 126 952@A space is;;2 126 952 mod 41 = 36@leaves thirty six"
Check the first one. A space is thirty two, t is a hundred and sixteen, and h is a hundred and four. In base two hundred and fifty six, that's two million, one hundred and twenty six thousand, nine hundred and fifty two, which leaves thirty six mod forty one.

@words text="'ain' = 97·256² + 105·256 + 110 = 6 383 982" sub="mod 41 = 36"
And a i n is six million, three hundred and eighty three thousand, nine hundred and eighty two. Divide by forty one, and the remainder is also thirty six.

@art collision-pair
They agree in no position at all. A residue is a residue. So checking only the first character might happen to separate these three, but it won't in general. The check is over all m characters.

@chapter What the collisions cost
@math heading="Verification" items="7 candidates × 3 = 21 comparisons@seven candidates;;3 collisions × 3 = 9 wasted@nine of them"
Every candidate costs three comparisons to settle, match or not. Seven candidates, twenty one comparisons. Nine of them, three collisions at three each, produce nothing.

@art false-alarm
And nothing in the algorithm notices. A collision looks exactly like a match until the characters are compared. That's why the comparison is unconditional. An implementation that trusted the hash would be wrong on this very text, at three offsets, silently.

@chapter Exact arithmetic
@art exact-digits
At base two hundred and fifty six, a twelve character window is far too big for a double, and rounding would change which windows collide. So every hash here is an exact big integer. The three offsets are the same on every machine, and if you check one by hand and disagree, you've found a bug.

@art recompute
The roll is the one value derived from another value, so it's where an error could accumulate. The panel recomputes every window's hash from scratch and compares. On this text, zero disagreements.

@chapter Where people slip
@list heading="Common slips" items="Calling verification an optimisation@The first|Reading a low collision count as a hash property@The second|Assuming a collision shares characters@The third"
The first slip is treating verification as an optimisation you could skip. It's the correctness argument. The second is reading three collisions as a property of the hash function. It's this text, base and modulus together. The third is assuming a collision shares characters with the pattern.

@chapter Try it
@words text="'e p'" sub="base 256 · modulus 41"
Your turn. Take the window e space p. E is a hundred and one, space is thirty two, and p is a hundred and twelve. Work out its hash mod forty one, and check you get thirty six.

@end text="Find the collisions yourself"
You can change the modulus and watch which windows collide, on Learn. That's learn dot get er done dot I O.
