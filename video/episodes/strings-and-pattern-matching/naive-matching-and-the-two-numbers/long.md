---
format: long
lesson: strings-and-pattern-matching/naive-matching-and-the-two-numbers
title: Naive string matching: the count you measured and the bound you proved
thumb: 50 measured, 123 proved
---

@chapter The question
@title text="Naive Matching, Measured and Bounded" sub="Strings and Pattern Matching" art=thumb
You want to find every place a short pattern appears in a long text. The simplest way slides the pattern along, one position at a time. How much work does that take? There are two honest answers, and they're very different numbers.

@art sliding-window
Here's the naive matcher. The text has length n and the pattern has length m. For each offset i, from zero up to n minus m, compare text and pattern one character at a time, and stop at the first disagreement. If all m agree, that's a match. Each offset is called an alignment.

@words text="n − m + 1 alignments" sub="nothing remembered between them"
There are n minus m plus one alignments. And nothing is remembered between them. Match five characters, fail on the sixth, and the matcher throws those five away and starts the next offset from scratch.

@chapter The bound
@math heading="Comparisons" items="per alignment:  at least 1,  at most m@at least one;;total ≤ m(n − m + 1)@m times;;total ≥ n − m + 1@at least n minus m"
At one alignment, the matcher makes at least one comparison and at most m. Multiply by the number of alignments. The total is at most m times n minus m plus one, and at least n minus m plus one. Both ends can actually be reached.

@chapter The rain in Spain
@words text="the rain in spain stays mainly in the plain" sub="pattern: ain · n = 43 · m = 3"
The lab opens on the rain in spain stays mainly in the plain, with pattern a i n. So n is forty three, m is three, and there are forty one alignments.

@art first-fail
Most alignments end almost before they start. The text's character simply isn't an a, and the matcher moves on after a single comparison.

@math heading="41 alignments, exactly" items="36 offsets without an a:  1 each = 36@thirty six;;offset 20 (stays):  a then y = 2@offset twenty;;4 matches:  3 each = 12@four real matches;;36 + 2 + 12 = 50@fifty"
Only five offsets have an a. The other thirty six fail on the first comparison, one each. Offset twenty matches the a of stays, then fails on the y, costing two. And the four real matches cost three each, twelve. Thirty six plus two plus twelve is fifty.

@art two-bars
The bound for the same lengths is three times forty one, a hundred and twenty three. The measurement is fifty. Both are right. Change one character and fifty moves. A hundred and twenty three won't move until the lengths do.

@chapter Why it's usually cheap
@math heading="Uniform alphabet of σ letters" items="P(survive k comparisons) = (1/σ)^k@one over sigma;;expected per alignment = Σ (1/σ)^k = σ/(σ − 1)@sigma over sigma minus one"
Suppose each text character is random, from an alphabet of sigma letters. An alignment survives k comparisons with probability one over sigma, to the power k. Add up that geometric series, and the expected cost per alignment is sigma over sigma minus one.

@words text="m isn't in it"
Notice that m isn't in that formula. A longer pattern gives more ways to fail early, not more work per alignment. That's why the simplest matcher is linear in practice.

@art english-vs-uniform
With thirteen distinct characters, that expectation is thirteen twelfths, just over one point oh eight. The measured figure is fifty over forty one, just over one point two two. English isn't uniform. The letter a is commoner than one in thirteen.

@chapter Repeating the text
@math heading="Text repeated 1 to 6 times" items="50, 102, 154, 206, 258, 310@fifty, a hundred and two;;differences: 52 every time@fifty two"
Repeat the text one to six times, same pattern. The counts are fifty, a hundred and two, a hundred and fifty four, and so on, up to three hundred and ten. The differences are fifty two every time.

@art straight-line
That's a straight line, not a parabola. It has to be. With m held fixed, even the bound is linear in n. A quadratic needs the pattern to grow along with the text.

@chapter Against the other matchers
@list heading="Same text, three matchers" items="Naive: 50@Naive|KMP: 44@Knuth Morris Pratt|Horspool: 25@Horspool"
On the opening text, Knuth Morris Pratt takes forty four comparisons and Horspool takes twenty five, against fifty for naive. All three report the same four matches, at five, fourteen, twenty five and forty, checked against a full scan, because a shorter list of correct positions looks exactly like a right answer.

@chapter Where people slip
@list heading="Common slips" items="Quoting the bound as the cost@The first|Quoting the measurement as the cost@The second|Forgetting a match costs m@The third"
The first slip is quoting the bound as the cost. Order n m is true, and almost never what happened. The second is quoting the measurement as the cost. Fifty on one text proves nothing about others. The third is forgetting that a match costs m comparisons.

@art full-match
A match is the most expensive alignment, not a free one. Here, four matches cost twelve of the fifty comparisons, almost a quarter of the total, from under a tenth of the alignments.

@chapter Try it
@words text="text: banana · pattern: ana"
Your turn. Search for a n a in banana. List every alignment, count the comparisons at each, and add them up. Then compare your total with m times n minus m plus one.

@end text="Count the comparisons yourself"
You can type any text and pattern, and see the count beside the bound, on Learn. That's learn dot get er done dot I O.
