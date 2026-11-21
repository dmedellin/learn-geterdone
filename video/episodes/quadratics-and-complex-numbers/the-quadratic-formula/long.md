---
format: long
lesson: quadratics-and-complex-numbers/the-quadratic-formula
title: The quadratic formula: where it comes from and how not to break it
thumb: One formula, every quadratic
---

@chapter Where it comes from
@title text="The Quadratic Formula" sub="Quadratics and Complex Numbers" art=thumb
Completing the square solves one quadratic at a time. Do it once with letters instead of numbers, and it solves every quadratic at once, and leaves a formula behind.

@math heading="Complete the square on ax² + bx + c = 0" items="x² + (b/a)x = −c/a@divide through by a;;x² + (b/a)x + b²/(4a²) = −c/a + b²/(4a²)@b squared over four a squared"
Divide through by a, which is allowed because a isn't zero, and move c over a across. Half the coefficient of x is b over two a, so add its square, b squared over four a squared, to both sides.

@math heading="Complete the square on ax² + bx + c = 0" items="(x + b/(2a))² = (b² − 4ac)/(4a²)@the left side;;x = (−b ± √(b² − 4ac)) / (2a)@x equals minus b"
Now the left side is x plus b over two a, squared, and the right is b squared minus four a c, over four a squared. Root both sides and tidy up, and x equals minus b, plus or minus root b squared minus four a c, all over two a.

@art no-crossing
Four a squared is positive, so the right side has the same sign as b squared minus four a c. If that's negative, there's no real solution. That's not a breakdown. The formula is reporting that there's nothing to find.

@art formula-machine
That quantity, b squared minus four a c, turned up without being asked for, and it decides everything about the answer. The next lesson is about it alone.

@words text="√(4a²) = 2|a|" sub="the ± makes 2a safe"
One subtle point. The root of four a squared is two times the absolute value of a, not two a. But the numerator already carries a plus or minus, so dividing by either gives the same two numbers, just listed in the other order. Writing two a is safe, and it keeps the formula short.

@chapter Using it
@list heading="Every time, in order" items="Rearrange into standard form@rearrange|Write a, b and c with their signs@write a, b and c|Compute b² − 4ac on its own line@compute"
Do three things in a fixed order, every time. First, rearrange into standard form. Then write a, b and c down, with their signs. Then compute b squared minus four a c on its own line, before you substitute anything else.

@math heading="2x² − 7x + 3 = 0" items="a = 2,  b = −7,  c = 3@a is two;;b² − 4ac = (−7)² − 4(2)(3) = 49 − 24 = 25@forty nine minus;;x = (7 ± 5) / 4@seven plus or minus five;;x = 12/4 = 3  or  x = 2/4 = 1/2@three or one half"
Take two x squared minus seven x plus three. a is two, b is minus seven, c is three. b squared minus four a c is minus seven, all squared, minus four times two times three, so forty nine minus twenty four, which is twenty five. That gives seven plus or minus five, over four. So x is three or one half.

@art signed-tiles
Minus b was minus minus seven, which is seven. And b squared was forty nine. Writing b equals minus seven on its own line first is what makes both of those automatic. And this one factors as two x minus one, times x minus three, so two separate methods agree.

@chapter Simplifying
@math heading="x² + 4x + 1 = 0" items="b² − 4ac = 16 − 4 = 12@sixteen minus four;;x = (−4 ± √12) / 2 = (−4 ± 2√3) / 2@root twelve;;x = −2 ± √3@minus two plus or minus"
The formula often hands back an unreduced fraction. For x squared plus four x plus one, b squared minus four a c is sixteen minus four, which is twelve. Root twelve is two root three, so x is minus four plus or minus two root three, over two. Divide both terms by two: minus two plus or minus root three.

@art split-numerator
Both terms, not just the convenient one. Minus four plus root three isn't a solution. Substitute it, and you get four minus four root three, not zero.

@chapter Negative a
@math heading="−x² + 5x − 6 = 0" items="b² − 4ac = 25 − 4(−1)(−6) = 1@twenty five minus;;x = (−5 ± 1) / (−2)  →  2 or 3@two and three"
a can be negative. Minus x squared plus five x minus six has a minus one, b five, c minus six. b squared minus four a c is twenty five minus twenty four, which is one, and x comes out as two and three.

@art flipped-parabola
Or multiply through by minus one first, to get x squared minus five x plus six. Same answers, far less sign handling. That's a free simplification, and worth taking.

@chapter The wrong tool
@art two-routes
x squared minus nine equals zero has b equal to zero. The formula gives plus or minus root thirty six over two, which is plus or minus three. Correct, but slower than the square root property, which reads x squared equals nine and stops. The formula always works. It's not always the shortest route.

@chapter Where people slip
@list heading="Common slips" items="Reading a, b, c before standard form@The first|Writing b² as a negative number@The second|Dividing only part of the numerator@The third"
The first slip is reading a, b and c before reaching standard form. Three x squared equals five x plus two has b minus five and c minus two. The second is writing b squared as negative. The third is dividing only part of the numerator.

@words text="−7² = −(7²) = −49" sub="b² − 4ac: 25 becomes −73"
That second one is worth a closer look. Without brackets, minus seven squared reads as minus forty nine, turning the twenty five from that example into minus seventy three, and two solutions into none. Brackets round a negative b settle it.

@end text="Standard form, signs, then the formula"
Work through the formula one line at a time, on Learn. That's learn dot get er done dot I O.
