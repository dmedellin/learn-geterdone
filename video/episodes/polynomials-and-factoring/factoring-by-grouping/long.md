---
format: long
lesson: polynomials-and-factoring/factoring-by-grouping
title: Factoring by grouping: four terms, two pairs, one shared bracket
thumb: Make the brackets match
---

@chapter The question
@title text="Factoring by Grouping" sub="Polynomials and Factoring" art=thumb
You've got four terms and nothing common to all of them. What now? Split them into pairs, take a common factor out of each pair, and hope the same bracket is left behind in both.

@chapter The method
@math heading="x³ + 3x² − 4x − 12" items="(x³ + 3x²) + (−4x − 12)@pair them;;x²(x + 3) + (−4)(x + 3)@out of each pair;;(x + 3)(x² − 4)@take that out"
Here's an example. x cubed plus three x squared minus four x minus twelve. First, pair them. Take x squared out of the first pair and minus four out of the second, out of each pair. Both leave x plus three, so take that out: x plus three, times x squared minus four.

@art shared-bracket
Why is that last step legal? For any polynomials A, B and P, A times P plus B times P is A plus B, times P. It's the distributive law with a common factor that happens to be a bracket. The law never cared what P was.

@chapter The sign in the second pair
@math heading="−4x − 12" items="−4(x + 3)  ✓ matches@minus four;;4(−x − 3)  ✗ doesn't@plus four"
When the third term is negative, take the negative out with the GCF. Factoring out minus four gives minus four times x plus three, which matches. Factoring out plus four gives four times minus x minus three, which doesn't.

@art mismatched-brackets
And then the method looks broken when it isn't. Only the sign choice was wrong. The rule of thumb is: make the second bracket match the first. If no choice of sign makes it match, the pairing really is wrong.

@chapter Regrouping
@math heading="ax + by + ay + bx" items="ax + ay + bx + by@reorder;;a(x + y) + b(x + y)@a times;;(x + y)(a + b)@x plus y times"
Sometimes the order you're given is unhelpful. a x plus b y plus a y plus b x, paired as given, shares nothing. So reorder: a x plus a y plus b x plus b y. That's a times x plus y, plus b times x plus y, which is x plus y times a plus b.

@art three-pairings
Rearranging the terms of a sum is always legal, so trying another pairing costs one line. With four terms there are only three genuinely different pairings, so the search is short.

@chapter Finish the job
@math items="(x + 3)(x² − 4)@not the end;;= (x + 3)(x − 2)(x + 2)@difference of squares"
A factorisation is complete only when nothing factors further. In our example, x plus three times x squared minus four is not the end. x squared minus four is a difference of squares, so the complete answer is x plus three, times x minus two, times x plus two.

@art complete-split
Stopping early is the most common way to lose marks on a factoring question that was otherwise done right. After every step, look at each factor again.

@words text="At x = 1: 1 + 3 − 4 − 12 = −12 · (4)(−1)(3) = −12"
Check at x equals one. The original gives one plus three minus four minus twelve, minus twelve. The factors give four times minus one times three, also minus twelve.

@math heading="6x³ − 9x² + 4x − 6" items="3x²(2x − 3) + 2(2x − 3)@three x squared;;(2x − 3)(3x² + 2)@two x minus three"
Knowing when to stop matters too. Six x cubed minus nine x squared plus four x minus six gives three x squared times two x minus three, plus two times two x minus three. So it's two x minus three, times three x squared plus two.

@art always-positive
And three x squared plus two is positive for every real x. It has no root, so it has no real linear factor. You're done.

@chapter When grouping fails
@words text="x³ + x² + 2x + 6 → x²(x + 1) + 2(x + 3)" sub="the brackets differ"
x cubed plus x squared plus two x plus six gives x squared times x plus one, plus two times x plus three. The brackets differ, and no reordering fixes it.

@art method-not-verdict
The honest conclusion is that grouping fails here, not that this doesn't factor. Whether it factors at all is a question for the factor theorem, later in the course.

@chapter Where people slip
@list heading="Common slips" items="Taking out + from a negative second pair@The first|Forcing two different brackets to match@The second|Stopping at the first product@The third"
The first slip is taking out a positive factor from a negative second pair. The second is forcing two different brackets to be the same. x plus three and x minus three are different polynomials, so regroup instead. And the third is stopping at the first product. Check every factor again.

@chapter Try it
@words text="2x³ + 4x² − 8x − 16 = 2(x³ + 2x² − 4x − 8)"
Your turn. Two x cubed plus four x squared minus eight x minus sixteen. The first move is given: take out two. Pair the four terms inside, choose the sign of the second factor, and factor every piece.

@math items="2(x + 2)²(x − 2)@two times x plus two, squared"
The complete result is two times x plus two, squared, times x minus two. If you stopped at two times x plus two times x squared minus four, there's a difference of squares left.

@end text="Try every pairing"
You can try every pairing of four terms and see which ones leave a matching bracket, on Learn. That's learn dot get er done dot I O.
