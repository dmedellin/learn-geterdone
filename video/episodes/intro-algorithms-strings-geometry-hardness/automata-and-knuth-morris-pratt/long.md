---
format: long
lesson: intro-algorithms-strings-geometry-hardness/automata-and-knuth-morris-pratt
title: Knuth-Morris-Pratt: string matching that never looks back
thumb: Remember what matched
---

@chapter What the naive matcher forgets
@title text="Finite Automata and Knuth-Morris-Pratt" sub="Introduction to Algorithms, Sections 32.3–32.4" art=thumb
Two sections of chapter thirty two answer one complaint.

@quote text="The naive string-matcher is inefficient because it entirely ignores information gained about the text for one value of s when it considers other values of s." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 32.1"
The naive string matcher is inefficient because it entirely ignores information gained about the text for one value of s when it considers other values of s.

@words text="Keep one number: q" sub="how much of the pattern just matched"
Both answers keep one number as they scan: how much of the pattern the text has just matched. And both use it to decide the next move, without looking back.

@chapter A string-matching automaton
@art automaton
The first answer is an automaton with states zero to m. It starts at zero and accepts at m. From state q on character a, it moves to the longest prefix of the pattern that ends the string read so far.

@math heading="Section 32.3" items="δ(q, a) = σ(P_q·a)@delta of q;;matching: Θ(n), one lookup per character@one table lookup;;table: (m + 1)·|Σ| entries@the table"
Delta of q and a is sigma of the first q pattern characters followed by a. Scanning is one table lookup per character, theta of n, with no character read twice. The price is the table: m plus one states, times the size of the alphabet.

@art table-vs-array
The book's straightforward construction of that table takes O of m cubed times the alphabet size. It can be brought down to m times the alphabet, but that's still a whole row for every state. The second answer needs just one short array.

@chapter The prefix function
@art border
Knuth, Morris and Pratt remove the alphabet factor. Suppose q characters have matched, and the next one fails. You know those q text characters: they're the pattern's first q. The next shift worth trying lines up the longest proper prefix of them that's also a suffix. That's a border, and its length is pi of q.

@art fallback
Pi depends only on the pattern, so it's computed once, in m entries, before the text is read. The matcher keeps a counter q, and on each mismatch falls back from q to pi of q, until the next character fits or q reaches zero.

@chapter Why it's linear
@art counter-rise-fall
One step can fall back many times. But the counter starts at zero, rises by at most one per character, and every fallback lowers it without going below zero. So all the falls together can't exceed all the rises, at most m minus one. It's an aggregate argument, from chapter seventeen. The same argument on the text gives theta of n.

@chapter The lesson's pattern
@math heading="P = abaabab" items="π = 0, 0, 1, 1, 2, 3, 2@pi is;;inner loop: 2 iterations, bound 6@inner loop;;fallback chain from 7: 7, 2, 0@fallback chain"
For the lesson's pattern, a b a a b a b, pi is zero, zero, one, one, two, three, two. The inner loop ran twice, against the book's bound of six. And the fallback chain from the whole pattern is seven, two, zero.

@math heading="Text: abaababaabaababab" items="KMP: 19 comparisons · shifts 0 and 8@nineteen comparisons;;naive: 35@naive;;bound 2n = 34@two n"
On a seventeen character text, KMP made nineteen comparisons and found the two valid shifts, zero and eight. The naive matcher made thirty five. The bound two n is thirty four, and nineteen is under it, as the proof says it must be on every text.

@art slide
Watch one slide. After six characters match and the seventh fails, pi of six is three. So the pattern slides by three, and its first three characters are already known to match.

@chapter Where people slip
@list heading="Common slips" items="One mismatch costs constant time@The first|π[q] is a shift@The second|The automaton is always better@the third"
The first slip is thinking one mismatch costs constant time. A single mismatch can fall back several times. Linear is a bound on all of them together. The second is confusing pi of q with a shift. It's a length, and the shift is q minus pi of q. And the third is treating the automaton as always better. Its table grows with the alphabet.

@chapter Try it
@code block=1 lines=1-1 focus="1@a b a c a b a b"
Your turn. For the pattern a b a c a b a b, compute pi one to pi eight by the procedure's rule, counting the inner loop iterations as you go. Give the longest border of the whole pattern, and the fallback chain from eight.

@end text="Build π yourself"
You can build pi one prefix at a time and check it against the definition, on Learn. That's learn dot get er done dot I O.
