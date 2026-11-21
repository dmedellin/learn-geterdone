---
format: long
lesson: sets-relations-functions/cardinality-and-countability
title: Countable and uncountable: why some infinities are bigger
thumb: Some infinities are bigger
---

@chapter The question
@title text="Cardinality and Countability" sub="Sets, Relations and Functions" art=thumb
Are there more natural numbers than even numbers? It seems obvious that there are, twice as many. But for infinite sets you can't count, so what would more even mean?

@words text="|A| = |B|  ⟺  a bijection A → B"
Here's the definition. Two sets have the same size when a bijection pairs them up, with nothing left over on either side. For finite sets this agrees with counting. For infinite ones, it's the only definition available.

@chapter The evens
@art pairing-lines
So pair them. Send n to two n. Zero goes to zero, one to two, two to four, three to six. It's injective, since two m equals two n forces m equals n. And it's surjective, since any even number two k comes from k.

@math items="f(n) = 2n@f of n;;|ℕ| = |E|,  although E ⊊ ℕ@same size"
With f of n equal to two n, the naturals and the evens are the same size, even though the evens are a proper subset that leaves out every odd number. For finite sets that's impossible. For infinite sets, it's the definition of infinite.

@chapter Countable means listable
@art zigzag
A set is countably infinite if it's in bijection with the naturals. That's exactly a list: a first element, a second, a third, with every element appearing exactly once. To prove a set countable, you produce the list.

@math heading="ℤ is countable" items="0, 1, −1, 2, −2, 3, −3, …@zero, one, minus one"
The integers? List them as zero, one, minus one, two, minus two, three, minus three, and so on. Every integer appears exactly once. The natural order doesn't work, because it has no first element. But reordering is allowed.

@art diagonal-walk
The rationals too. Put the fractions a over b in a grid, a for the row and b for the column, and walk the diagonals. One over one. Then one half, two over one. Then one third, two over two, three over one. Skip any fraction not in lowest terms. Each diagonal is finite, so the walk reaches every cell.

@art dense-line
That's genuinely surprising. Between any two rationals there's another, and there are still no more of them than counting numbers. Dense and uncountable are unrelated ideas.

@chapter Cantor's diagonal
@words text="No list of (0, 1) is complete"
So is every infinite set countable? No. Cantor showed the reals can't be listed. It's enough to show that the numbers between zero and one can't. Take any list at all, each number written as a decimal.

@art diagonal-tiles
Now build a new number, digit by digit, by walking down the diagonal of the list.

@math items="xₖ = 5  if  dₖₖ ≠ 5@isn't five;;xₖ = 4  if  dₖₖ = 5@if it is five"
For its k th digit, look at the k th digit of the k th number on the list. If that digit isn't five, write five. And if it is five, write four.

@words text="x differs from rₙ in place n"
The new number differs from the first number in the first place, from the second in the second, and from the n th in the n th place. So it's on no line of the list, yet it lies between zero and one. Every list misses something.

@words text="Why 4 and 5?" sub="0.4999… = 0.5000…"
Why only fours and fives? Some numbers have two decimal expansions, like zero point four nine recurring, which equals one half. Using only fours and fives means the new number never ends in recurring nines, so it has just one expansion, and the ambiguity never arises.

@chapter No largest infinity
@art power-cloud
Cantor went further. No set can be mapped onto its own power set. Given any function from A to its subsets, take D: the elements that are not in their own image. If D were the image of some d, then d is in D exactly when it isn't. So the power set is always strictly bigger. There's no largest infinity.

@chapter Where people slip
@list heading="Common slips" items="Thinking a proper subset must be smaller@The first|Confusing dense with uncountable@The second|Diagonalising against one specific list@the third"
The first slip is thinking a proper subset must be smaller. The evens show it isn't. The second is confusing dense with uncountable. And the third is diagonalising against one specific list. The argument has to start with an arbitrary one.

@chapter Try it
@words text="Cantor's proof for (0, 1)" sub="from memory"
Your turn. Write out Cantor's proof for the numbers between zero and one, including why the digits four and five are chosen. If you can state that reason, you have the argument, not just its outline.

@end text="Bijection as the definition of size"
You can see when sizes rule out a bijection, and why infinity removes that limit, on Learn. That's learn dot get er done dot I O.
