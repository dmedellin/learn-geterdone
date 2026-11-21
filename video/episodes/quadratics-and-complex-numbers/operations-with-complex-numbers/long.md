---
format: long
lesson: quadratics-and-complex-numbers/operations-with-complex-numbers
title: Adding, multiplying and dividing complex numbers
thumb: The conjugate clears it
---

@chapter Little to learn
@title text="Operations with Complex Numbers" sub="Quadratics and Complex Numbers" art=thumb
Complex numbers were built so that every law you already know keeps working: commutativity, associativity, distribution. That's why there's so little new to learn here. An answer is finished when it's written as a plus b i, with a and b real.

@chapter Adding and subtracting
@art like-terms
Adding and subtracting just collects like terms. Real parts go with real parts, and imaginary parts with imaginary parts. b i and d i are both multiples of i, so they add the way three t and five t do.

@math heading="(2 − 7i) − (5 + 3i)" items="2 − 5 = −3@two minus five;;−7i − 3i = −10i@minus seven i;;= −3 − 10i@minus three minus ten i"
Take two minus seven i, minus five plus three i. Two minus five is minus three. Minus seven i minus three i is minus ten i. So the answer is minus three minus ten i. The minus sign has to reach both parts of the second bracket.

@chapter Multiplying
@math heading="(3 + 2i)(4 − 5i)" items="12 − 15i + 8i − 10i²@twelve;;−10i² = −10 · (−1) = +10@minus ten i squared;;= 22 − 7i@twenty two"
To multiply, expand the brackets just as you would with a variable, then replace i squared by minus one. Three plus two i, times four minus five i, is twelve minus fifteen i plus eight i, minus ten i squared. Now minus ten i squared is plus ten. So the answer is twenty two minus seven i.

@art expand-grid
That plus ten is where it usually goes wrong. Subtracting ten i squared adds ten. If your answer is twenty out from the right one, that step is probably the reason. There's a general formula, but don't memorise it. Expand, substitute, collect.

@chapter Powers of i
@math heading="Powers of i" items="i⁰ = 1   i¹ = i   i² = −1   i³ = −i@one, i;;i⁴ = (i²)² = (−1)² = 1@i to the fourth"
The powers of i go one, i, minus one, minus i. Then i to the fourth is minus one, squared, which is one, so the four values repeat for ever.

@art four-cycle
So a power of i depends only on the remainder when you divide by four. i to the twenty third: twenty three is four times five plus three, remainder three. So it's minus i.

@words text="√−4 · √−9 = 2i · 3i = −6" sub="not √36 = 6"
One law doesn't carry over. Root a times root b equals root a b is only for non-negative numbers. Root minus four times root minus nine is two i times three i, six i squared, which is minus six, not six. Convert to i first, then multiply.

@chapter The conjugate
@art mirror-pair
The conjugate of a plus b i is a minus b i. Same real part, opposite imaginary part. A number equals its own conjugate exactly when it's real.

@math heading="(a + bi)(a − bi)" items="a² − abi + abi − b²i²@expand;;= a² + b²@a squared plus b squared"
Multiply a number by its conjugate. Expand, and the two cross terms cancel. Minus b squared i squared becomes plus b squared. So you're left with a squared plus b squared. No i at all. It's never negative, and it's zero only when a and b are both zero.

@art cancel-cross
That's what makes division work. To divide by c plus d i, multiply top and bottom by c minus d i. That's multiplying by one, so the value doesn't change. Only the form does, and the new denominator is an ordinary real number.

@chapter Dividing
@math heading="(4 + i) / (2 + 3i)" items="(4 + i)(2 − 3i) = 8 − 12i + 2i − 3i² = 11 − 10i@on top;;(2 + 3i)(2 − 3i) = 4 + 9 = 13@underneath;;= 11/13 − (10/13)i@eleven thirteenths"
Here's one. Four plus i, over two plus three i. The conjugate of the bottom is two minus three i. On top, four plus i times two minus three i is eleven minus ten i. Underneath, four plus nine, thirteen. So the quotient is eleven thirteenths, minus ten thirteenths i.

@art balanced-fraction
And since a squared plus b squared is positive for any non-zero number, every non-zero complex number has a reciprocal. Adding, subtracting, multiplying and dividing never take you outside the system.

@chapter Where people slip
@list heading="Common slips" items="Leaving i² in the answer@The first|Multiplying only the bottom by the conjugate@The second|Using √a · √b = √(ab) on negatives@The third"
The first slip is leaving i squared in the answer. It's the number minus one, not a term to carry. The second is multiplying only the denominator by the conjugate, which changes the fraction's value. The third is using the root law on negatives, which gives a wrong sign.

@end text="Expand, substitute, conjugate"
Practise all four operations, on Learn. That's learn dot get er done dot I O.
