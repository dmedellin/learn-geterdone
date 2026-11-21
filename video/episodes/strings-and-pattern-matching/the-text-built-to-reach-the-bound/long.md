---
format: long
lesson: strings-and-pattern-matching/the-text-built-to-reach-the-bound
title: The input that makes naive matching hit its worst case, exactly
thumb: The count IS the bound
---

@chapter The question
@title text="The Text Built to Reach the Bound" sub="Strings and Pattern Matching" art=thumb
Naive matching makes at most m times n minus m plus one comparisons. On English text it comes nowhere near. So can you build a text that hits the bound exactly? Yes. And then the harder question: does that make naive matching quadratic?

@art all-a-text
Here's the construction. The text is nothing but one letter, a, repeated. The pattern is m minus one a's, followed by a b. At every offset, the pattern agrees with the text on its first m minus one characters, and disagrees on the last.

@chapter Every alignment pays in full
@art full-pay
Every offset looks exactly the same as every other. That sameness is the whole trick, because it means every alignment does the maximum possible work.

@math heading="Text a^N, pattern a^(m−1) b" items="k < m − 1:  a = a  ✓@a against a;;k = m − 1:  a ≠ b  ✗@a against b;;m comparisons per alignment@exactly m;;total = m(N − m + 1)@the total"
Fix an alignment. Every comparison before the last is a against a, and succeeds. The last is a against b, and fails. So every alignment makes exactly m comparisons, and finds nothing. There are N minus m plus one alignments, so the total is m times N minus m plus one. That's the bound itself.

@words text="aaaaaaaaaaaaaaaaaaaaaaaa · aaaab" sub="measured 100 = bound 5 × 20 = 100"
The lab opens on twenty four a's and the pattern a a a a b. Twenty alignments, five comparisons each, a hundred in total. The bound is five times twenty, also a hundred. The measured count is the bound. No other preset produces that sentence.

@chapter A steep line is still a line
@math heading="Repeat the text 1 to 6 times" items="100, 220, 340, 460, 580, 700@a hundred, two hundred and twenty;;differences: 120 each@a hundred and twenty;;per character: 4.17 → 4.86@per character"
Repeat that text one to six times. The counts are a hundred, two hundred and twenty, three hundred and forty, and so on, up to seven hundred. The differences are a hundred and twenty each. Comparisons per character creep from four point one seven to four point eight six. That's a line, with a steep slope.

@art steep-line
It has to be a line. With m held fixed, the bound itself is linear in n. Four and a half comparisons per character is a big constant, but a constant times n is not quadratic, however large the constant. The kit's own author once called this table quadratic, and withdrew it.

@chapter The family where m grows
@art growing-family
To get a real quadratic, the pattern has to grow with the text. So build a family. At each m, take the text of two times m minus one a's, and the pattern of m minus one a's then a b. The pattern is half the text.

@math heading="n = 2(m − 1)" items="alignments = n − m + 1 = m − 1@alignment count;;each costs m  →  total m(m − 1)@each costs m;;per character = m/2@m over two"
Now the alignment count is n minus m plus one, which is m minus one. Each costs m, so the total is m times m minus one, equal to the bound in every row. Per character, that's m over two, and it grows without limit as m grows.

@list heading="m = 3 to 11" items="m = 3, n = 4: naive 6, KMP 6@m is three|m = 7, n = 12: naive 42, KMP 18@m is seven|m = 11, n = 20: naive 110, KMP 30@m is eleven"
When m is three, naive makes six. When m is seven, forty two. When m is eleven, a hundred and ten. Knuth Morris Pratt on the same family makes three times m minus one: six, eighteen, thirty. That's one and a half per character, flat in every row.

@art rising-ratio
That's the honest form of the claim. Not naive matching is quadratic, which is false on almost every input anyone types. But there's a family of inputs where its count is a constant times the product of the lengths, and here it is.

@chapter Horspool, at its best
@art right-first
Horspool, for contrast, makes just twenty comparisons on the opening text, five times fewer than naive. It compares the window from the right, so it meets the b first, and fails immediately. Reverse the pattern's letters, and a later lesson shows the same algorithm at its worst.

@chapter Where people slip
@list heading="Common slips" items="Calling a steep line a quadratic@The first|Believing the worst case is rare@The second|Reading m(n − m + 1) as nm@The third"
The first slip is calling a steep line a quadratic. Check whether the per character figure keeps rising. The second is believing the worst case is rare. Periodic input, like DNA or padded records, looks exactly like this. The third is reading the bound as n m. At m eleven, that's two hundred and twenty against the true hundred and ten.

@chapter Try it
@words text="m = 6" sub="text a^10 · pattern aaaaab"
Your turn. Take m equal to six, so the text is ten a's and the pattern is five a's then a b. Count the alignments, the comparisons per alignment, and the total, and check it equals m times m minus one.

@end text="Build the worst case yourself"
You can build the adversarial family and watch the count meet the bound, on Learn. That's learn dot get er done dot I O.
