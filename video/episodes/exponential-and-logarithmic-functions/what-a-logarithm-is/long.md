---
format: long
lesson: exponential-and-logarithmic-functions/what-a-logarithm-is
title: What a logarithm is: the exponent you were looking for
thumb: A logarithm is an exponent
---

@chapter One sentence
@title text="What a Logarithm Is" sub="Exponential and Logarithmic Functions" art=thumb
Here's the whole idea in one sentence. Log base b of x is the exponent you put on b to get x. Everything else about logarithms, the graphs, the laws, both kinds of equation, is that sentence applied.

@math heading="Definition" items="log_b(x) = y    means    bʸ = x@means exactly;;b > 0,   b ≠ 1,   x > 0@as long as"
So log base b of x equals y means exactly that b to the y equals x, as long as the base b is positive and not one, and the argument x is positive. b is the base of the logarithm, and x is its argument.

@art one-crossing
Why is there only one answer? Because b to the y is always increasing, or always decreasing. Either way, it takes each positive value exactly once, so there's one y, not two.

@art flat-line-base
That's also why the base can't be one. One to any power is one. So log base one of one would have every number as an answer, and log base one of five would have none.

@chapter Two forms, one fact
@math heading="Exponential  ⟷  logarithmic" items="2³ = 8    ⟷    log₂(8) = 3@Two cubed;;10⁻³ = 1/1000    ⟷    log₁₀(1/1000) = −3@Ten to the minus three;;5⁰ = 1    ⟷    log₅(1) = 0@Five to the zero;;9^(1/2) = 3    ⟷    log₉(3) = 1/2@nine to the one half"
Two cubed is eight, so log base two of eight is three. Ten to the minus three is one thousandth, so log base ten of one thousandth is minus three. Five to the zero is one, so log base five of one is zero. And nine to the one half is three, so log base nine of three is one half.

@art two-forms
Moving between the forms isn't a calculation, it's a change of notation. Three roles move around. The base stays the base. The result of the power becomes the argument. And the exponent becomes the value.

@words text="b^(log_b x) = x        log_b(bʸ) = y"
That gives two cancellation identities. b to the log base b of x is x. And log base b of b to the y is y. Both are just the definition, said aloud.

@chapter Ask the question
@words text="log₃(81) = ?" sub="3 to what power is 81?"
To evaluate a logarithm, ask the question. Log base three of eighty one: three to what power is eighty one? Three to the fourth is eighty one, so the answer is four.

@math heading="log₈(4)" items="8 = 2³,    4 = 2²@both powers of two;;(2³)ʸ = 2²    so    2^(3y) = 2²@two to the three y;;3y = 2    →    y = 2/3@three y equals two;;check:   8^(2/3) = (∛8)² = 2² = 4@To check"
When the answer isn't whole, the question still works if both numbers are powers of one base. Eight and four are both powers of two. So eight to the y equals four becomes two to the three y equals two squared. Then three y equals two, and y is two thirds. To check, the cube root of eight is two, and two squared is four.

@chapter Negative values, and no value
@words text="log₅(1/25) = −2" sub="because 5⁻² = 1/25"
A logarithm can be negative. Log base five of one twenty fifth is minus two, because five to the minus two is one twenty fifth. With a base above one, the value is negative exactly when the argument is between zero and one.

@art never-negative
What can't be negative is the argument. b to the y is positive for every real y, so no exponent gives zero, and none gives a negative number. Log base two of zero and log base two of minus eight name nothing. The question they ask has no answer.

@art bracket-bars
And most logarithms are irrational. Log base two of ten sits between three and four, because two cubed is eight and two to the fourth is sixteen. Its value is three point three two one nine and on, with no exact decimal form.

@chapter Where people slip
@art swap-cards
The commonest slip is swapping the base and the argument. Log base two of eight is three, but log base eight of two is one third. They're reciprocals, not equals. Say the base out loud: it's the number being raised to a power.

@list heading="Two more slips" items="Expecting log of 0 to be 0, or −∞@expecting log base b of zero|Refusing a negative logarithm@refusing a negative"
The others are expecting log base b of zero to be zero, or minus infinity, when it's simply undefined. And refusing a negative logarithm. The restriction is on the argument. The value can be any real number at all.

@chapter Try it
@words text="log₂₇(9) = y" sub="rewrite:   27ʸ = 9"
Your turn. Find log base twenty seven of nine. Start from the rewrite, twenty seven to the y equals nine. Write both sides as powers of three, solve for y, and check by raising twenty seven to your answer. Keep it as an exact fraction, and say which role each number plays.

@end text="The same fact, both ways round"
You can type any base and argument and get the exact exponent back as a fraction, on Learn. That's learn dot get er done dot I O.
