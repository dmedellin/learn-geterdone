---
format: long
lesson: algebra-foundations/properties-of-the-real-numbers
title: The properties of the real numbers: your licence to rearrange
thumb: Five permissions, nothing more
---

@chapter The licence
@title text="Properties of the Real Numbers" sub="Algebra Foundations" art=thumb
When you rearrange an expression, what gives you the right? The answer is a short list of five permissions. Everything later in algebra is one of them, applied to a longer expression.

@words text="Assumed, not proved" sub="know exactly what each one says"
These properties are assumed, not proved here. What matters is knowing exactly what each one says, because anything beyond that isn't allowed.

@chapter Order and grouping
@art reorder-swap
The commutative properties say order doesn't matter. A plus b equals b plus a, and a times b equals b times a. That's for addition and for multiplication, and for nothing else.

@art regroup
The associative properties say grouping doesn't matter. A plus b, then plus c, equals a plus, b plus c. The same goes for multiplication. That's why you can write a plus b plus c with no brackets, and still name one number.

@words text="Collect the x terms" sub="commutative + associative"
Together, those two say a sum can be added in any order and any grouping. That's the whole reason you're allowed to collect the x terms. You're moving terms past each other, and these two are your permission.

@chapter Distribution
@art distribute-arrows
The distributive property is the only one that mixes the two operations. A times, b plus c, equals a b plus a c. Read left to right, it expands a bracket. Read right to left, it factors one out. It's the same statement both ways.

@math heading="−(x − 3)" items="−(x − 3) = (−1)(x − 3)@minus one times;;= (−1)(x) + (−1)(−3)@then distribute;;= −x + 3@that's minus x plus three"
It's also why minus, x minus three, is minus x plus three. Write the minus as minus one times the bracket. Then distribute: minus one times x, plus minus one times minus three. That's minus x plus three. Nothing is remembered. Both signs are computed.

@chapter Identities and inverses
@art identity-frame
Zero is the additive identity: a plus zero is a. One is the multiplicative identity: a times one is a. Multiplying by one in disguise, like three over three, is how every common denominator gets built.

@art inverse-pair
Every real a has an additive inverse, minus a, and the two add to zero. Every real except zero has a multiplicative inverse, one over a, and they multiply to one. That single exclusion is why division by zero is undefined. There's simply no number that works.

@math heading="Why a · 0 = 0" items="0 = 0 + 0@zero is zero plus zero;;a · 0 = a · 0 + a · 0@by distribution;;a · 0 = 0@you're left with"
A times zero is zero isn't one of the assumptions. It follows from them. Zero is zero plus zero. So by distribution, a times zero equals a times zero plus a times zero. Add the inverse of a times zero to both sides, and you're left with zero equals a times zero.

@chapter Subtraction and division
@words text="7 − 3 ≠ 3 − 7" sub="(24 / 4) / 2 = 3,   24 / (4 / 2) = 12"
Subtraction and division have none of these properties. Seven minus three isn't three minus seven. And twenty four over four, over two, is three, while twenty four over, four over two, is twelve.

@words text="a − b = a + (−b)" sub="a / b = a · (1/b)"
The fix is to stop treating them as operations of their own. Subtracting is adding the negative. Dividing is multiplying by the reciprocal. Once you rewrite them, every property applies again.

@chapter Rules that don't exist
@math heading="Invented rules" items="a(bc) ≠ (ab)(ac):   24 against 48@forty eight;;√(a + b) ≠ √a + √b:   √13 against 5@root thirteen;;1/(a + b) ≠ 1/a + 1/b:   1/2 against 2@one half"
Most errors are invented rules, and each dies to one set of numbers. At two, three and four, a times b c is twenty four, while a b times a c is forty eight. The root of four plus nine is root thirteen, not five. And at one and one, one over, a plus b, is one half, not two.

@art counterexample
One counterexample is a complete disproof, and it takes about ten seconds. Unsure if a step is legal? Put small numbers into both sides. It won't tell you a rule is true. But it will tell you when one is false, and that's the direction the errors run.

@chapter Every step named
@math heading="5 − 2(x − 3)" items="= 5 + (−2)(x − 3)    adding the negative@adding the negative;;= 5 + [(−2)(x) + (−2)(−3)]    distributive@distribute;;= 5 + (−2x + 6)    arithmetic@plus six;;= 5 + (6 + (−2x))    commutative@swap the order;;= (5 + 6) + (−2x)    associative@regroup;;= 11 − 2x@eleven minus two x"
Here's the worked example: five minus two times, x minus three. Rewrite the subtraction as adding the negative. Distribute. Minus two times minus three is plus six, computed, not recalled. Swap the order, that's commutative. Regroup, that's associative. And you reach eleven minus two x.

@words text="at x = 4:   3 and 3" sub="the wrong answer −1 − 2x gives −9"
Check it at x equals four. The original gives three, and eleven minus eight is three. The common wrong answer, minus one minus two x, gives minus nine. Agreement at one value isn't proof. The named steps are the proof.

@chapter Where people slip
@list heading="Common slips" items="Reordering across a minus sign@reordering across|Distributing over a product@distributing over a product|A minus reaching only the first term@only the first term"
Three slips to watch. Reordering across a minus sign: five minus x isn't x minus five. Distributing over a product. And letting a minus sign reach only the first term in a bracket.

@chapter Try it
@words text="4 − 3(y − 2)" sub="one change per line, each one named"
Now try four minus three times, y minus two. Start by rewriting it as four plus minus three times, y plus minus two. Make one change per line, and name each one. You should reach ten minus three y.

@end text="Test a claim on your own numbers"
You can test each property, and a few fake ones, on your own numbers, on Learn. That's learn dot get er done dot I O.
