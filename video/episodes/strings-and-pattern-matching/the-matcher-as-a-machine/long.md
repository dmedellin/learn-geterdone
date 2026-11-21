---
format: long
lesson: strings-and-pattern-matching/the-matcher-as-a-machine
title: String matching as a machine: one lookup per character, no comparisons
thumb: Zero comparisons, one table
---

@chapter The question
@title text="The Matcher as a Machine" sub="Strings and Pattern Matching" art=thumb
Knuth Morris Pratt still compares characters, and still falls back after a mismatch. What if you worked out every move in advance? Then the search becomes one table lookup per character, with no comparisons at all.

@art state-chain
Here's the machine. It has m plus one states, numbered zero to m. State j means the last j characters read match the pattern's first j, and no longer prefix ends here. The machine starts in state zero, reads the text one character at a time, and state m means a match.

@chapter The transition table
@math heading="Transition" items="δ(j, c) = longest prefix of p that is a suffix of p[0..j−1] + c@delta of j, c"
The transition delta of j, c is the length of the longest prefix of the pattern that's a suffix of the first j pattern characters, followed by c. It's a statement about strings. It mentions no algorithm.

@art table-grid
So the table can be built the obvious way. For each state and each character, form the string, and try every prefix length, longest first. That's m plus one, times sigma cells, where sigma is the alphabet size.

@chapter Why it works
@words text="state after t[0..i] = longest prefix of p that ends here"
The theorem says that after reading the text up to position i, the machine's state is the length of the longest prefix of the pattern that's a suffix of what's been read. So state m means an occurrence ends right there.

@art induction-step
The proof is induction. Say after the previous character, the state is j. Any longer match ending now must end with the new character, and before that be a suffix that's also a prefix, so of length at most j. Those candidates are exactly what delta of j looks at.

@chapter ababc
@words text="pattern ababc · alphabet {a, b, c}" sub="6 states × 3 letters = 18 cells"
The lab opens on the pattern a b a b c, over the letters a, b and c. That's six states and eighteen cells.

@math heading="State 4: abab matched" items="a → 3@on an a;;b → 0@on a b;;c → 5@on a c"
The row for state four, a b a b matched, reads: on an a, go to three. On a b, go to zero. On a c, go to five, a match. That first one is the interesting one.

@art border-compiled
Reading an a after a b a b gives a b a b a. Its longest suffix that's a prefix of the pattern is a b a, so the machine drops to three, not to zero. Everything the failure function would compute at run time is sitting in that one cell.

@list heading="Text abababcababcabababc" items="19 steps for 19 characters@nineteen steps|3 matches: 2, 7, 14@three occurrences|0 comparisons@no comparison"
The run over a nineteen character text takes exactly nineteen steps, and finds three occurrences, at two, seven and fourteen. And there's no comparison counter at all, because the machine makes none.

@chapter The trade
@list heading="Same text" items="KMP: 21 comparisons, stores 5 numbers@KMP makes|Machine: 0 comparisons, 19 steps, stores 18@The machine makes"
KMP makes twenty one comparisons on that text, and stores five numbers. The machine makes zero comparisons, takes nineteen steps, and stores eighteen. Neither one wins outright. It depends how many texts one table will serve.

@art two-trades
The table depends only on the pattern. So a program searching a thousand documents for one pattern pays for eighteen cells once, and nineteen steps a thousand times.

@math heading="Table cells per text character" items="binary 10110:  12 cells, n = 36  →  1/3@binary;;wide: the, σ = 13:  52 cells, n = 38  →  26/19@thirteen"
The run is always n steps, whatever the characters. The table grows with sigma. A binary pattern over two letters needs twelve cells for a thirty six character text, a third of a cell per character. The pattern t h e, over thirteen letters, needs fifty two, for thirty eight characters.

@art wide-alphabet
For bytes, that's two hundred and fifty six cells per state. For Unicode text, you'd never write the table out. That's why KMP is what actually gets used. It stores m numbers, whatever the alphabet. The machine is the clearer explanation. KMP is the compressed version of it.

@chapter Where people slip
@list heading="Common slips" items="Thinking a mismatch sends the machine to 0@The first|Counting the table as search cost@The second|Treating sigma as a property of the pattern@The third"
The first slip is thinking a mismatch sends the machine to state zero. It goes wherever the cell says. The second is counting the table as part of every search. It's built once. The third is treating sigma as a property of the pattern. An accented letter in the text widens every row.

@chapter Try it
@words text="pattern aaab · alphabet {a, b}"
Your turn. Build the table for a a a b over the letters a and b. That's five states and ten cells. Then work out where state three goes on an a, and explain why.

@end text="Run the machine yourself"
You can build the transition table for any pattern and run it, on Learn. That's learn dot get er done dot I O.
