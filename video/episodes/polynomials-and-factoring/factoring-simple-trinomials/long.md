---
format: long
lesson: polynomials-and-factoring/factoring-simple-trinomials
title: Factoring x squared plus bx plus c: a search that always finishes
thumb: Product c, sum b
---

@chapter The question
@title text="Factoring Simple Trinomials" sub="Polynomials and Factoring" art=thumb
How do you factor something like x squared minus seven x plus twelve? It looks like guesswork. It isn't. It's a short search, and when it ends, you know the answer either way.

@chapter What to look for
@math heading="(x + p)(x + q)" items="x² + qx + px + pq@multiply out;;= x² + (p + q)x + pq@p plus q;;x² + bx + c@compare"
Multiply out x plus p, times x plus q. You get x squared plus q x plus p x plus p q, which is x squared plus p plus q, times x, plus p q. Now compare that with x squared plus b x plus c.

@art product-and-sum
So you need two integers whose product is c and whose sum is b. Two coefficients, two conditions. And because p has to divide c, there are only finitely many candidates to test.

@words text="leading coefficient 1" sub="otherwise: take it out, or use the AC method"
This works when the leading coefficient is one. If it isn't, take it out as a common factor if you can. Otherwise, the AC method is the next lesson.

@art candidate-ladder
Then search systematically. List the divisor pairs of c from one upward, so nothing gets skipped, and add each pair. Stop at the first pair whose sum is b. There can't be a second.

@chapter Read the signs first
@art sign-rules
The two conditions tell you the signs before you search. If c is positive, the numbers share a sign, and it's the sign of b. If c is negative, the signs are opposite, and the larger one carries the sign of b.

@words text="c > 0, b < 0 → both negative"
Take x squared minus seven x plus twelve. c is positive and b is negative, so both numbers are negative. These aren't extra rules to memorise. Each comes straight from the product and the sum, and working them out on the spot is safer than recalling them.

@chapter Two searches that succeed
@math heading="x² − 7x + 12" items="(−1)(−12)  sum −13@minus one and minus twelve;;(−2)(−6)  sum −8@minus two and minus six;;(−3)(−4)  sum −7  ✓@minus three and minus four;;(x − 3)(x − 4)@answer"
List the pairs. Minus one and minus twelve sum to minus thirteen. Minus two and minus six give minus eight. Minus three and minus four give minus seven, a match. The answer is x minus three, times x minus four.

@math heading="x² + 2x − 15" items="(1)(−15) sum −14 · (−1)(15) sum 14@one and minus fifteen;;(3)(−5) sum −2@three and minus five;;(−3)(5) sum 2  ✓@minus three and five;;(x − 3)(x + 5)@so it's"
Now x squared plus two x minus fifteen. c is negative, so opposite signs. One and minus fifteen sum to minus fourteen, and minus one and fifteen to fourteen. Three and minus five give minus two. Minus three and five give two. So it's x minus three, times x plus five.

@art larger-wins
The larger number in that pair is positive, matching b equals plus two, just as the signs predicted.

@chapter A search that fails
@math heading="x² + x + 1" items="(1)(1)  sum 2@one and one;;(−1)(−1)  sum −2@minus one and minus one;;no pair sums to 1@neither equals one"
Now x squared plus x plus one. The divisor pairs of one are one and one, with sum two, and minus one and minus one, with sum minus two. Neither equals one, and the list is exhausted.

@art empty-list
So this trinomial does not factor over the rationals. That's a proved result, not a surrender. The search ended because the list ran out, and an exhausted list is a proof.

@art two-locks
Compare x squared plus two x plus one. There the pair one and one sums to two, and the answer is x plus one, squared. One small change in b, and the lock opens.

@words text="no (x + 1/2)(x + 8) shortcuts" sub="rational factors of a monic trinomial are integers"
Could a pair of fractions work instead? For a monic trinomial with integer coefficients, no. Any rational numbers in its linear factors are integers, so they were already on the list. The rational root theorem proves it later.

@chapter Where people slip
@list heading="Common slips" items="Matching the product but not the sum@The first|Guessing signs instead of reading them@The second|Treating a failed search as unfinished@The third"
The first slip is matching the product but not the sum. x plus two times x plus ten has product twenty but sum twelve, so it isn't x squared plus nine x plus twenty. The second is guessing signs instead of reading them off. The third is treating a failed search as an unfinished one.

@chapter Try it
@words text="x² − 2x − 24" sub="opposite signs · the larger is negative"
Your turn. x squared minus two x minus twenty-four. The signs are opposite, and the larger absolute value is negative. List the divisor pairs of twenty-four, assign the signs, and expand to check.

@math items="4 · (−6) = −24 · 4 + (−6) = −2@four and minus six;;(x + 4)(x − 6)@x plus four"
The pair is four and minus six, so the answer is x plus four, times x minus six. Minus four and six give the right product, but the wrong middle coefficient.

@end text="Watch the search finish"
You can enter any b and c and watch every divisor pair get tested, on Learn. That's learn dot get er done dot I O.
