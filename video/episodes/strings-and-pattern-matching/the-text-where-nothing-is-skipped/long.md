---
format: long
lesson: strings-and-pattern-matching/the-text-where-nothing-is-skipped
title: The text where Horspool skips nothing and loses five to one
thumb: Every shift is one
---

@chapter The question
@title text="The Text Where Nothing Is Skipped" sub="Strings and Pattern Matching" art=thumb
Horspool's algorithm is famous for skipping most of the text. So can it ever do worse than the naive matcher? Move one character in the pattern, and it does, by a factor of five.

@art run-of-a
Take a text of thirty a's in a row, and search for the pattern b a a a a. The odd character, the b, sits at the front instead of the end.

@chapter The table goes useless
@math heading="Table from baaa" items="a → 1@a goes to one;;b → 4@b goes to four"
The shift table is built from the first four letters, b a a a. So a goes to one, and b goes to four. Every character of the text is a, so every shift is one.

@art tiny-shifts
The window crawls along one tile at a time, and visits all twenty six alignments in turn. Nothing is skipped at all.

@art right-match-then-fail
And each alignment is expensive. Comparing from the right, the first four checks are a against a, and they all succeed. Only the last, b against a, fails. So every alignment costs the full five comparisons.

@math heading="Text a^30, pattern baaaa" items="26 alignments × 5 = 130@twenty six;;= m(n − m + 1),  the bound, attained@maximum possible"
Twenty six alignments at five comparisons each is a hundred and thirty. That's m times n minus m plus one, the maximum possible, attained. The panel reports zero alignments skipped, and an average shift of exactly one.

@words text="Horspool 130 · naive 26 · KMP 30"
The naive matcher on the same input compares the b first, at every alignment, and leaves after one comparison. That's twenty six in total. KMP makes thirty. The skipping algorithm makes five times what the naive one does.

@chapter The mirror image
@art mirror-pattern
Now flip the pattern to a a a a b, same thirty a's. The table still says a shifts one, so Horspool still visits all twenty six alignments. But comparing from the right, it meets the b first, and fails after one comparison.

@list heading="Text a^30, 26 alignments" items="baaaa: Horspool 130 · naive 26 · KMP 30@b a a a a|aaaab: Horspool 26 · naive 130 · KMP 56@a a a a b|aaaaa: Horspool 130 · naive 130 · KMP 30@five a's"
So with b a a a a, Horspool makes a hundred and thirty and naive twenty six. With a a a a b, they swap exactly: twenty six and a hundred and thirty. Neither algorithm was touched. And with five a's, every alignment matches, so both make a hundred and thirty, while KMP makes thirty.

@chapter What Horspool promises
@words text="Horspool's worst case = naive's worst case" sub="m(n − m + 1)"
So Horspool's guarantee is m times n minus m plus one, the same as naive's. There's no theorem saying Horspool is never worse than naive. This page is a counterexample.

@art average-cloud
What is true is a statement about an average. Over random text from a large alphabet, the expected comparisons are close to n over m. That's where the reputation comes from. But it's a claim about a distribution, so a single text can sit far from it in either direction, and refute nothing.

@chapter Which matchers are safe
@list heading="Bounds that don't depend on m" items="KMP: 30 and 56, both under 2n = 60@KMP makes|Automaton: exactly 30 steps@The automaton"
On thirty a's, KMP makes thirty comparisons with b a a a a, and fifty six with a a a a b, both under two n, sixty. The automaton takes exactly thirty steps on either. Their bounds are linear in n, with no m in them, so no text can make them blow up.

@art four-bounds
So the ranking of the four matchers changes with the input, and the bounds don't change at all. Naive and Horspool, m times n minus m plus one. KMP, two n. The automaton, exactly n. For text you haven't seen, the bounds are the only evidence.

@chapter Where people slip
@list heading="Common slips" items="Calling this input unrealistic@The first|Thinking Horspool should compare left to right@The second|Reading 130 vs 26 as a fivefold slowdown@The third"
The first slip is calling this input unrealistic. Padded records and zeroed disk blocks look just like it. The second is thinking Horspool should compare left to right. Then it has nothing to look up, and it's just naive. The third is reading a hundred and thirty against twenty six as a property of the algorithm. It's the pair.

@chapter Try it
@words text="text a^12 · pattern baaa"
Your turn. Take twelve a's and the pattern b a a a. Build the shift table, count the alignments, and work out Horspool's total and the naive total. Then reverse the pattern and check they swap.

@end text="Find Horspool's worst case yourself"
You can try your own texts and watch Horspool's shifts collapse to one, on Learn. That's learn dot get er done dot I O.
