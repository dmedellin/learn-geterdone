---
format: long
lesson: algebra-foundations/order-of-operations
title: Order of operations: one expression, one value
thumb: One expression, one value
---

@chapter The problem
@title text="Order of Operations" sub="Algebra Foundations" art=thumb
Here's an expression: two plus three times four. What is it? The answer depends on how you read it, and algebra can't start until everyone reads it the same way.

@math heading="Two readings of 2 + 3 · 4" items="left to right: (2 + 3) · 4 = 20@strictly left to right;;multiplication first: 2 + 12 = 14@multiplication first"
Read strictly left to right, it's twenty. Read with multiplication first, it's fourteen. Both readings make sense. The world settled on fourteen.

@art two-readings
That's a convention, not a theorem. Nothing forced it. It's convenient, because it lets you write three x squared plus five x plus seven with no brackets at all. What matters is that every book, calculator and program makes the same choice, so an expression names one number.

@chapter The four levels
@list heading="The order" items="1   Brackets, innermost first@brackets first|2   Exponents@then exponents|3   × and ÷, left to right@multiplication and division|4   + and −, left to right@addition and subtraction"
Here's the order. Brackets first, from the innermost outward. Then exponents. Then multiplication and division, together, left to right. Then addition and subtraction, together, left to right.

@art level-stairs
Look closely at levels three and four. Each one holds two operations, and within a level the rule is position, not the kind of operation. Multiplication doesn't outrank division. Addition doesn't outrank subtraction.

@chapter Left to right
@math items="8 − 3 + 2 = (8 − 3) + 2 = 7@eight minus three plus two;;not 8 − (3 + 2) = 3@not three;;24 / 4 / 2 = (24 / 4) / 2 = 3@twenty four over four over two;;not 24 / (4 / 2) = 12@not twelve"
So eight minus three plus two is five plus two, which is seven, not three. And twenty four over four over two is six over two, which is three, not twelve.

@art left-to-right
Both wrong answers come from doing the last named operation first. Acronyms like PEMDAS and BODMAS list four operations in a row, and quietly suggest an order between them that doesn't exist. Sweep from the left, and do whichever you meet first.

@chapter The base of an exponent
@math heading="Where the minus sign goes" items="−3² = −(3²) = −9@minus three squared;;(−3)² = (−3)(−3) = 9@in brackets"
An exponent applies to the smallest thing written just before it. A minus sign in front isn't part of that thing unless brackets say so. So minus three squared is minus nine. But minus three in brackets, squared, is nine.

@art exponent-base
This isn't a trick, and sources don't disagree about it. Exponents come before multiplication, and minus three squared is minus one times three squared. It matters the moment you substitute a negative for a letter. x squared at minus three is minus three in brackets, squared, which is nine.

@chapter Brackets you can't see
@art fraction-bar
Some brackets are invisible. A fraction bar groups everything above it, and everything below it. Type the fraction on one line, and you have to write those brackets back in.

@math items="(2 + 4) / (3 − 1) = 6 / 2 = 3@two plus four, over three minus one;;typed: 2 + 4 / 3 − 1 = 1 + 4/3 = 7/3@typed on one line"
Two plus four, over three minus one, is six over two, which is three. Typed on one line without brackets, it means two, plus four thirds, minus one. That's one plus four thirds, which is seven thirds.

@words text="√(9 + 16) = 5" sub="but √9 + √16 = 7"
A root sign groups the same way. The root of nine plus sixteen is the root of twenty five, which is five. But the root of nine plus the root of sixteen is three plus four, which is seven.

@chapter Every level at once
@math heading="20 − 2 · (5 − 8)² / 6 + 1" items="brackets: 5 − 8 = −3@the bracket gives;;exponents: (−3)² = 9@the exponent;;× and ÷: 2 · 9 = 18, 18 / 6 = 3@two times nine;;+ and −: 20 − 3 = 17, 17 + 1 = 18@twenty minus three"
Here's one that uses every level. The bracket gives minus three. The exponent squares minus three, brackets and all, to make nine. Then two times nine is eighteen, and eighteen over six is three. Last, twenty minus three is seventeen, and seventeen plus one is eighteen.

@art nested-brackets
The last level is where direction mattered. Group the end as twenty minus, three plus one, and you get sixteen. That's the single most common way to lose this expression.

@chapter Where people slip
@list heading="Common slips" items="Trusting an acronym over the two-level rule@trusting an acronym|Writing the base without its sign@the base of an exponent|Losing the invisible brackets@losing the invisible"
Three slips, then. Trusting an acronym over the rule that each level holds two operations. Writing the base of an exponent without its sign, so minus three squared turns into nine. And losing the invisible brackets when a fraction is typed on one line.

@chapter Try it
@words text="18 / 3 / 2 + (−2)²" sub="write only the next operation on each line"
Now one with less guidance. Eighteen over three over two, plus minus two in brackets, squared. Write only the next operation on each line. The answer is seven. If you got twelve, you grouped the division from the right.

@end text="Watch the queue build"
You can type an expression and watch the queue of operations build, one rule at a time, on Learn. That's learn dot get er done dot I O.
