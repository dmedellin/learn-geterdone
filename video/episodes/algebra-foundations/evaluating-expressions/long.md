---
format: long
lesson: algebra-foundations/evaluating-expressions
title: Evaluating expressions: substitute with brackets, every time
thumb: Brackets, every time
---

@chapter The idea
@title text="Evaluating Expressions" sub="Algebra Foundations" art=thumb
To evaluate an expression, you replace every letter with its value and do the arithmetic. Easy to say. But one habit removes almost every error, and it's this: write the value inside brackets, every time.

@art slot-in
Evaluating means replacing every occurrence of each variable by its value, then working it out with the order of operations. The result is a single number, or else a statement that the expression has no value there.

@art same-value
Every occurrence of a letter takes the same value. In x squared minus x, at minus three, both xs are minus three. If two quantities can differ, they need two letters.

@chapter Brackets, every time
@math heading="x² at x = −3" items="with brackets:   (−3)² = (−3)(−3) = 9@with brackets;;without:   −3² = −(3 · 3) = −9@without them"
Here's why the brackets are the method, not a precaution. Take x squared at minus three. With brackets, minus three, squared, is minus three times minus three, which is nine. Without them, you've written minus three squared, and that's minus nine.

@art escaped-sign
That second line isn't a slip of the pen. It's a correct evaluation of a different string. The exponent binds tighter than the minus sign, so the sign escapes the base. The brackets are what carry the sign into the power.

@chapter A minus in the expression
@math heading="at x = −3" items="−x² = −((−3)²) = −9@minus x squared;;(−x)² = (−(−3))² = 3² = 9@minus x, all squared"
Now two expressions that differ only by brackets. At minus three, minus x squared means minus, x squared. That's minus nine. But minus x, all squared, negates first, giving three, then squares it, giving nine.

@art bracket-shield
Both answers are right. They answer different questions. Which one you're evaluating is decided by the brackets printed in the question, and the only way to keep them straight is to carry them through the substitution.

@chapter Operations you can't see
@art hidden-multiply
Three x means three times x. So at x equals four, it's three times four, which is twelve, never thirty four. Put a four next to a three without brackets, and two digits side by side mean something else entirely.

@math items="2x² at x = 3:   2 · (3²) = 18@two x squared;;(2x)² at x = 3:   (2 · 3)² = 36@two x, all squared"
A coefficient isn't part of the base, either. Two x squared at three is two times nine, which is eighteen. Two x, all squared, is six squared, which is thirty six. They're different expressions.

@chapter More letters, and no value
@math items="x² − y² at x = −3, y = 2:   9 − 4 = 5@x squared minus y squared;;5 − 2x at x = −4:   5 + 8 = 13@five minus two x;;1/(x − 2) at x = 2:   1/0, undefined@one over"
With several letters, substitute all of them before any arithmetic. x squared minus y squared, at minus three and two, is nine minus four, which is five. Five minus two x, at minus four, is five plus eight, thirteen. And one over, x minus two, at two, is one over zero.

@art no-value
That last one isn't a failure of the method. Division by zero has no value, so the expression has no value at two. Undefined is a complete answer. Producing a number anyway, usually zero, is worse, because it's a wrong answer.

@chapter A fraction, step by step
@math heading="2x² − 3x + 1 at x = −1/2" items="2(−1/2)² − 3(−1/2) + 1@in brackets;;(−1/2)² = 1/4,   2 · 1/4 = 1/2@the square;;−3 · (−1/2) = 3/2@minus three times;;1/2 + 3/2 = 2,   2 + 1 = 3@then add"
Here's the worked example. Substitute, in brackets. The square of minus a half is a quarter, so the first term is a half. Minus three times minus a half is three halves. Then add: a half plus three halves is two, and two plus one is three. Exact, with no decimal anywhere.

@words text="drop that sign and you get 0"
All the sign work is in that second product. Minus three times minus a half is plus three halves. Drop the sign, and you'd get zero instead of three.

@chapter Where people slip
@list heading="Common slips" items="Substituting a negative without brackets@without brackets|Treating the coefficient as part of the base@the coefficient|Assuming a value always exists@always exists"
Three slips. Substituting a negative value without brackets, so x squared at minus three comes out as minus nine. Treating the coefficient as part of the base, so two x squared at three comes out as thirty six. And assuming a value always exists, when sometimes the honest answer is undefined.

@chapter Try it
@words text="5 − 3x at x = −2"
Try five minus three x, at x equals minus two. Copy it as five minus three times, minus two, in brackets, and finish from there. You should get eleven. If you got minus one, the substituted sign got dropped.

@end text="Substitute, with brackets and without"
You can substitute with brackets and without, and see exactly where the two answers part, on Learn. That's learn dot get er done dot I O.
