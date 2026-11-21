---
format: long
lesson: rational-and-radical-expressions/adding-and-subtracting-rational-expressions
title: Adding and subtracting rational expressions without the sign error
thumb: Bracket the second numerator
---

@chapter Same units first
@title text="Adding and Subtracting Rational Expressions" sub="Rational and Radical Expressions" art=thumb
You can only add fractions when they count the same thing. So all the real work here happens in the denominator, and then, in subtraction, in one very easy sign.

@art same-units
Two sevenths plus three sevenths is five sevenths, because both count sevenths. With a common denominator, the rule is immediate: a over c plus b over c is a plus b, over c. Everything hard in this lesson is about getting to that situation.

@art different-units
a over c plus b over d counts two different things, and there's no rule that adds them directly. In particular, it is not a plus b, over c plus d. One numerical test settles that for good.

@chapter The least common denominator
@art lcd-stack
The least common denominator, the L C D, is built from factors. Take every distinct factor that appears in any denominator, and raise each one to the highest power it reaches in a single denominator.

@math heading="5/((x + 2)(x + 3))  +  3/(x + 2)²" items="distinct factors: x + 2,  x + 3@the distinct factors;;LCD = (x + 2)²(x + 3)@the L C D is;;✗  product of the denominators: (x + 2)³(x + 3)@not the product"
Take five over x plus two times x plus three, plus three over x plus two squared. The distinct factors are x plus two and x plus three. Their highest powers are two and one. So the L C D is x plus two squared, times x plus three, not the product, which would carry x plus two cubed.

@words text="The product always works. It's just wasteful." sub="the extra factor cancels at the very end"
Multiplying the denominators together is never wrong, only wasteful. The extra factor cancels at the end, after you've carried it through every line. In Solving Rational Equations, where the L C D multiplies a whole equation, that's a real cost.

@chapter Rebuilding each fraction
@art rebuild-fraction
Once you've chosen the L C D, rebuild each fraction to sit over it. Multiply the top and bottom by whatever factors the L C D has and the fraction lacks. That's legal, because you're multiplying by a form of one.

@math items="= 5(x + 2)/LCD  +  3(x + 3)/LCD@five times x plus two;;= (5x + 10 + 3x + 9)/LCD@expand;;= (8x + 19) / ((x + 2)²(x + 3))@eight x plus nineteen"
So the first becomes five times x plus two, over the L C D, and the second becomes three times x plus three, over the L C D. Expand the tops: five x plus ten, plus three x plus nine. That's eight x plus nineteen, over x plus two squared times x plus three.

@chapter Where the sign goes
@math heading="x/(x² − 9)  −  2/(x + 3)" items="x² − 9 = (x − 3)(x + 3)@x squared minus nine;;LCD = (x − 3)(x + 3),   x ≠ 3,  x ≠ −3@the L C D"
Now subtraction. x over x squared minus nine, minus two over x plus three. x squared minus nine is x minus three times x plus three, so that's the L C D, and three and minus three are excluded.

@math items="= [x − (2x − 6)] / LCD@in brackets;;= (x − 2x + 6) / LCD@distribute;;= (6 − x) / ((x − 3)(x + 3))@six minus x"
The second top becomes two times x minus three, which is two x minus six. Put it in brackets: x minus, two x minus six. Then distribute: x minus two x plus six. That's six minus x.

@art half-reached
Here's the error this lesson exists to prevent. Writing x minus two x minus six instead, so the minus only reaches the first term, gives minus x minus six, and every later step is wrong. The minus in front of a fraction applies to all of its top.

@art bracket-wrap
The defence is mechanical. Put the whole second numerator in brackets before you subtract, and only then distribute. It costs one pair of brackets, and removes the most common source of lost marks in the topic.

@math heading="Check at x = 0" items="0 − 2/3 = −2/3@zero minus two thirds;;6/((−3)(3)) = 6/(−9) = −2/3  ✓@six over"
Check at zero. The original is zero minus two thirds, minus two thirds. The answer is six over minus three times three, six over minus nine, also minus two thirds. And the domain still excludes three and minus three, inherited from where you started.

@chapter Where people slip
@list heading="Common slips" items="Subtracting only the first term@The first|Adding the denominators@The second|Cancelling against one term on top@the third"
The first slip is subtracting only the first term of the numerator. Bracket it, and the error becomes impossible. The second is adding the denominators. And the third is cancelling a factor against just one term on top. In eight x plus nineteen, over its denominator, nothing cancels.

@chapter Try it
@words text="2/(x² − x − 6)  −  1/(x − 3)" sub="x² − x − 6 = (x − 3)(x + 2), which is the LCD"
Your turn. Take two over x squared minus x minus six, minus one over x minus three. The bottom factors as x minus three, times x plus two, and that's also the L C D. Rebuild the second fraction, bracket its new numerator, and finish.

@end text="Bracket, then distribute"
You can practise building L C Ds and keeping the sign on Learn. That's learn dot get er done dot I O.
