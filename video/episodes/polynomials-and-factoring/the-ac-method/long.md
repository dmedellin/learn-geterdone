---
format: long
lesson: polynomials-and-factoring/the-ac-method
title: The AC method: factoring when the leading coefficient isn't 1
thumb: Split the middle, then group
---

@chapter The question
@title text="The AC Method" sub="Polynomials and Factoring" art=thumb
Factoring x squared plus b x plus c is a quick search. But put a number in front of the x squared, and guessing the two brackets turns into a search with far too many branches. The AC method replaces the guess with arithmetic.

@art distributed-a
The old shortcut breaks because the leading coefficient distributes into both brackets. So the constant term is no longer the product of the two numbers you're looking for.

@chapter The method
@math heading="ax² + bx + c" items="compute ac@compute a c;;find m, n:  mn = ac,  m + n = b@find two integers;;bx → mx + nx@rewrite;;group the four terms@group"
Here's the method. First, compute a c. Then find two integers, m and n, whose product is a c and whose sum is b. Rewrite b x as m x plus n x. Then group the four terms, exactly as in factoring by grouping.

@math heading="Why the split is legal" items="mx + nx = (m + n)x = bx@m x plus n x"
That number a c seems to come from nowhere, so the method looks like a trick. But the only step that could be illegal is the split. And m x plus n x is m plus n times x, which is b x. The expression is equal for every x, so you've only rewritten it.

@chapter A first example
@math heading="6x² + 11x + 3" items="ac = 6 · 3 = 18@six times three;;1·18 sum 19 · 2·9 sum 11 · 3·6 sum 9@the factor pairs"
Six x squared plus eleven x plus three. a c is six times three, eighteen. The factor pairs are one and eighteen, two and nine, three and six, with sums nineteen, eleven and nine. So the pair is nine and two.

@math items="6x² + 9x + 2x + 3@splitting;;3x(2x + 3) + 1(2x + 3)@group;;(3x + 1)(2x + 3)@three x plus one"
Splitting gives six x squared plus nine x plus two x plus three. Now group it: three x times two x plus three, plus one times two x plus three. And you get three x plus one, times two x plus three.

@art either-order
The order of m and n doesn't matter. Split it the other way round, and you get the same two factors in the other order. If your two brackets don't match, you've made an arithmetic slip, not found a second answer.

@chapter With negatives
@math heading="12x² − 17x + 6" items="ac = 72@seventy-two;;(−8)(−9) = 72 · −8 + (−9) = −17@minus eight and minus nine;;12x² − 8x − 9x + 6@split;;4x(3x − 2) − 3(3x − 2)@group;;(4x − 3)(3x − 2)@four x minus three"
Twelve x squared minus seventeen x plus six. a c is seventy-two, positive, and b is negative, so both numbers are negative. The pair is minus eight and minus nine. Split, then group: four x times three x minus two, minus three times three x minus two. So it's four x minus three, times three x minus two.

@art sign-in-second-group
The second group is minus nine x plus six, and the factor to take out is minus three, not three. Take out three and the bracket won't match, and the grouping seems to fail. When two brackets differ only by an overall sign, fix the sign you took out.

@chapter When there's no pair
@math heading="2x² + 3x + 4" items="ac = 8@a c is eight;;1·8 sum 9 · 2·4 sum 6@nine and six;;(−1)(−8) sum −9 · (−2)(−4) sum −6@minus nine and minus six"
Now two x squared plus three x plus four. a c is eight. The positive pairs give sums nine and six, and the negative pairs give minus nine and minus six. None is three.

@art exhausted-search
And that's an answer. Any factorisation into integer brackets would produce a pair on the a c list. So an empty list proves the trinomial isn't a product of two integer binomials. Running out of pairs is the method succeeding.

@chapter Common factor first
@words text="12x² + 22x + 6 = 2(6x² + 11x + 3) = 2(3x + 1)(2x + 3)"
Always take out the common factor first. Twelve x squared plus twenty-two x plus six is two times six x squared plus eleven x plus three, which is the example you've already done.

@art big-search-small-search
Skip that step and the search gets big. Twenty-four x squared plus forty-four x plus twelve has a c of two hundred and eighty-eight, with nine factor pairs. Divide by four first, and a c is eighteen, with three.

@chapter Where people slip
@list heading="Common slips" items="Forgetting the common factor@The first|Losing the sign in the second group@The second|Treating a failed search as a failed attempt@The third"
The first slip is forgetting the common factor and searching a huge a c. The second is losing the sign when you group the second pair. And the third is treating a failed search as a failed attempt. It's actually a result: the trinomial is irreducible over the integers.

@chapter Try it
@words text="6x² − 7x − 20" sub="ac = −120 · need sum −7"
Your turn. Six x squared minus seven x minus twenty. a c is minus one hundred and twenty. Search the opposite sign pairs for a sum of minus seven, split, group and expand.

@math items="8 and −15@eight and minus fifteen;;(2x − 5)(3x + 4)@two x minus five"
The pair is eight and minus fifteen, giving two x minus five, times three x plus four. Minus eight and fifteen keep the product, but flip the middle coefficient.

@end text="Watch the pair search run"
You can enter any a, b and c and watch the a c pair search run, on Learn. That's learn dot get er done dot I O.
