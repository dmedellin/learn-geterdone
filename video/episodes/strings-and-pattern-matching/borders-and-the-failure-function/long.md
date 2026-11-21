---
format: long
lesson: strings-and-pattern-matching/borders-and-the-failure-function
title: Borders and the KMP failure function, built and checked
thumb: Prefix that's also a suffix
---

@chapter The question
@title text="Borders, and the Failure Function Built" sub="Strings and Pattern Matching" art=thumb
When a partial match fails, the naive matcher throws away everything it learned. Knuth Morris Pratt keeps some of it. Exactly how much it can keep comes down to one idea, the border.

@art border-overlap
A border of a string is a proper prefix that's also a suffix. Proper means shorter than the whole string. For a b a b a, the borders are a b a and a. For a b c, there's only the empty string, which is a border of every non empty string. So the longest border always exists.

@words text="fail[k] = longest border of the first k characters"
The failure function puts that into an array. Fail of k is the length of the longest border of the pattern's first k characters, one number for every k.

@chapter Seven prefixes of ababaca
@math heading="ababaca" items="a · ab → 0, 0@a, and a b;;aba → 1 · abab → 2 · ababa → 3@a b a;;ababac → 0@a b a b a c;;ababaca → 1@the whole pattern"
Take a b a b a c a. The prefixes a, and a b, have only the empty border. A b a has border a, one. A b a b has a b, two. A b a b a has a b a, three. A b a b a c drops to zero. And the whole pattern ends with a, so one.

@art rise-and-collapse
That rise from zero to three is the pattern's periodicity. And the collapse to zero is the c. It occurs nowhere else, so no prefix ending in c can match a prefix starting with a.

@art two-columns
The lab builds the array in linear time. Beside it, it computes every border straight from the definition, trying every length and comparing substrings. That's cubic, and obviously right. The two columns agree on all seven prefixes.

@chapter Why the slide is safe
@art slide-by-border
Now the key theorem. Say the pattern sits at offset i, its first k characters have matched, and the next comparison fails. Slide the pattern so its longest border lines up where its suffix was. That's offset i plus k minus fail of k.

@math heading="No match is skipped" items="a match at j with i < j < i + k@a match started at;;⇒ p[0..i+k−j−1] is a border of p[0..k−1]@would be a border;;⇒ i + k − j ≤ fail[k]@at most fail of k"
Could that skip a match? Suppose a match started at some j in between. Its start lies inside the part already matched, so it's a prefix of the pattern and a suffix of that part. It would be a border, of length i plus k minus j, which is at most fail of k. So j can't come before the slide.

@words text="the text pointer never moves back" sub="so at most 2n comparisons"
So the matcher just sets k to fail of k, and leaves the text pointer where it is. The text pointer only ever advances. That's where the bound of two n comes from.

@art fallback-chain
Apply fail repeatedly, and you get the fallback chain. On a b a b a c a, it's seven, then one, then zero. Every length in that chain is an alignment that could still match. On five a's, it's five, four, three, two, one, zero.

@chapter The counts
@list heading="29-character text" items="3 matches at 2, 12, 22@three occurrences|KMP: 34 comparisons@KMP makes|Naive: 61@naive matcher makes|Bound 2n: 58@The bound"
The panel searches a twenty nine character text, and finds three occurrences, at two, twelve and twenty two. KMP makes thirty four comparisons, and the naive matcher makes sixty one. The bound, two n, is fifty eight. Thirty four is a measurement. Fifty eight is a theorem. The gap between the two algorithms generalises least of all.

@chapter Where people slip
@list heading="Common slips" items="Including the whole string as a border@The first|Reading fail[k] as an index@The second|Thinking fail depends on the text@The third"
The first slip is counting the whole string as a border. Then fail of k would be k, and the matcher would never advance. The second is reading fail of k as an index rather than a length. The third is thinking the failure function depends on the text. It's computed from the pattern alone, once.

@art off-by-one
And always check the fast construction against the definition. An off by one in the fallback gives an array that's too small on periodic patterns. The matcher still finds every match, just slowly. The bug hides in the count, not the output.

@chapter Try it
@words text="aabaaab"
Your turn. Write out every prefix of a a b a a a b, find its longest border by hand, and build the failure array. Then follow the fallback chain from the full length down to zero.

@end text="Build the failure function yourself"
You can type any pattern and see the failure function checked against the definition, on Learn. That's learn dot get er done dot I O.
