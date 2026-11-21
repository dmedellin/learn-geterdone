---
format: long
lesson: strings-and-pattern-matching/where-the-simple-algorithm-wins
title: When naive string matching beats KMP, and why that proves nothing
thumb: The simple one wins by m − 1
---

@chapter The question
@title text="Where the Simple Algorithm Wins" sub="Strings and Pattern Matching" art=thumb
Knuth Morris Pratt has the better guarantee. So surely it makes fewer comparisons than the naive matcher? Change one word, the pattern, and the naive matcher wins. Not by luck, but by a formula.

@words text="text: the rain in spain stays mainly in the plain" sub="pattern: zebra"
Keep the text from before, the rain in spain stays mainly in the plain, and search for zebra instead. There's no z anywhere in the text. So no alignment gets past its first comparison.

@chapter Naive pays per alignment
@art one-per-alignment
Every naive alignment starts by comparing a text character with the z, and fails at once. So each alignment costs exactly one comparison. There are n minus m plus one alignments, so that's the total. Here, thirty nine comparisons, against a bound of five times thirty nine, a hundred and ninety five.

@chapter KMP pays per character
@art one-per-character
Knuth Morris Pratt keeps k, the number of pattern characters matched so far. Its fallback step only runs while k is above zero. Here k starts at zero, every comparison against the z fails, and k stays zero. So it makes exactly one comparison per text character. That's n, forty three.

@math heading="The gap" items="KMP: n = 43@KMP;;naive: n − m + 1 = 39@naive;;n − (n − m + 1) = m − 1 = 4@m minus one"
KMP makes n, and naive makes n minus m plus one. Subtract, and the gap is m minus one, four in naive's favour. It doesn't depend on the text at all, only on the pattern's length. Lengthen zebra to zebraic, and it widens to six, without touching either algorithm.

@math heading="Text repeated 1 to 6 times" items="naive: 39, 82, 125, 168, 211, 254@Naive reads;;KMP: 43, 86, 129, 172, 215, 258@KMP reads"
Repeat the text one to six times. Naive reads thirty nine, eighty two, a hundred and twenty five, and so on. KMP reads forty three, eighty six, a hundred and twenty nine, which is n itself every time. The gap is four in every row, because it's m minus one, and m never moved.

@chapter What the guarantee is for
@art two-ceilings
Now switch to the text built to reach the bound. Naive makes a hundred, KMP forty four, on twenty four characters. KMP's count can never exceed two n, whatever you type. Naive's can't exceed m times n minus m plus one. Here those ceilings are forty eight and a hundred, and each count sits under its own.

@art reversal
So the counts reverse between two texts, and the bounds don't. Whichever side you want to argue, the evidence is a proof. The numbers are illustrations.

@art insurance
And KMP's table wasn't wasted here. For zebra, it's five zeros, and no fallback ever fires. That work is insurance. The same construction holds the count under two n on the bad text. You can't buy the guarantee only on the inputs that need it.

@chapter Horspool
@art skip-ahead
The third column reports fourteen. Horspool compares from the right end of the window, then shifts by where the character under the window's last position appears in the pattern. A letter that isn't in the pattern shifts the window by the full m. So it reads about one character in five.

@words text="Horspool: 14 here · 130 vs naive's 26 elsewhere"
That's the biggest saving on the page, and the one with least behind it. Horspool's worst case is the same as naive's. On a thirty character text in a later lesson, it makes a hundred and thirty comparisons, and naive makes twenty six.

@chapter Where people slip
@list heading="Common slips" items="Treating the reversal as an artefact@The first|Thinking the failure function was wasted@The second|Reading KMP's 43 as a loose bound@The third"
The first slip is treating the reversal as noise. Both counts are exact formulas. The second is thinking KMP's table was wasted. It was insurance. The third is reading forty three against a bound of eighty six as proof the bound is loose. Some texts really do approach two n.

@words text="One counterexample refutes · no examples confirm"
One text is enough to refute the claim that KMP always makes fewer comparisons. But no number of texts can confirm that naive is faster. Measurements refute. Only proofs confirm.

@chapter Try it
@words text="pattern: zebraic" sub="same text"
Your turn. Keep the text and search for zebraic, seven letters. Predict the naive count and the KMP count before running them, and check the gap is six.

@end text="Race the matchers yourself"
You can race naive, KMP and Horspool on any text you like, on Learn. That's learn dot get er done dot I O.
