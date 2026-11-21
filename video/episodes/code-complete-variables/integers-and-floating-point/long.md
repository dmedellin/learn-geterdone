---
format: long
lesson: code-complete-variables/integers-and-floating-point
title: When Java's arithmetic is wrong: overflow, division and 0.1
thumb: Right on paper, wrong in code
---

@chapter The problem
@title text="Integers and Floating Point" sub="Code Complete, chapter 12" art=thumb
Arithmetic that's right on paper can be wrong in code. Java's integers overflow silently, integer division drops the remainder, and a double can't hold most decimal fractions. The first half of chapter twelve is about exactly this.

@chapter Numbers in general
@list heading="Numbers in general" items="Avoid magic numbers@magic numbers|Anticipate division by zero@division by zero|Make conversions obvious@conversions|Fix your compiler's warnings@warnings"
Section twelve point one gives guidelines for numbers in general. Avoid magic numbers, literals in the middle of code with no explanation. Anticipate division by zero. Make type conversions obvious, and don't compare mixed types. And pay attention to your compiler's warnings. Top programmers, McConnell says, fix them rather than ignore them.

@chapter Integers
@art truncated-division
Integer division doesn't give the fraction. Seven divided by ten is zero. So ten times seven tenths is zero, where arithmetic says seven. The remedy is to reorder the expression so the division comes last.

@art odometer-wrap
The other danger is overflow. A Java int holds up to two billion, one hundred and forty seven million, four hundred and eighty three thousand, six hundred and forty seven. Go one past that, and Java keeps the low bits and carries on. You get the most negative int, with no error and no warning.

@art overflow-cup
Section twelve point two's method: think through each term of an expression, imagine the largest value it can take, and check the result fits, allowing for growth. And remember an intermediate result can overflow, even when the final one would fit.

@chapter Floating point
@quote text="Floating-point numbers that should be equal are not always equal. The main problem is that two different paths to the same number don’t always lead to the same number." cite="McConnell, Code Complete, 2nd ed., Section 12.3, p. 295"
Then floating point. Floating point numbers that should be equal are not always equal. The main problem is that two different paths to the same number don't always lead to the same number.

@art binary-fraction
Many decimal fractions can't be represented exactly in binary. A double stores the nearest fraction whose denominator is a power of two. So adding numbers of very different sizes can lose the small one, and values that should be equal often aren't.

@art tolerance-band
So compare floating point values within a tolerance, not with equals equals. And for rounding errors, use a type with more precision, a decimal type, or integers that count the smallest unit.

@chapter Java beside the exact
@math heading="Integers" items="2147483647 + 1 → −2147483648@plus one;;46341 × 46341: exact 2147488281 → int −2147479015@forty six thousand;;as a long → 2147488281@as a long;;7 ÷ 2 → 3, exact 3.5@seven divided by two"
The lab does Java's arithmetic beside the exact result. The largest int plus one prints minus two billion and change. Forty six thousand, three hundred and forty one squared is just past the largest int, so it prints a large negative number. Done as a long, it prints exactly. And seven divided by two, as ints, is three.

@math heading="0.1 added ten times" items="double: 0.9999999999999999@point nine nine;;stored: 9007199254740991/9007199254740992@one part;;exact: 1 · not the same@not the same"
Now the book's own example. Start at zero and add point one, ten times, in a double. Java prints point nine nine nine, and so on, not one. The stored value is one part in about nine quadrillion short of one. Close, and not the same.

@art cents-jar
The chapter's remedy for money is to count in the smallest unit. Add ten cents, ten times, in an int, and Java prints a hundred, exactly. Or use a decimal type, which in Java is big decimal, behind a class that hides the representation.

@chapter An intermediate overflow
@code block=1 lines=1-2 label=Java focus="1@milliseconds in a year|2@prints"
Here's an easy one to write without noticing. A line that computes the milliseconds in a year. Java multiplies left to right, in int, and then this prints the result.

@math heading="365 × 24 × 60 × 60 × 1000" items="365 × 24 × 60 × 60 = 31536000 (fits)@seconds;;× 1000 = 31536000000 (too big)@thirty one billion;;prints 1471228928@one billion;;fix: long, and 1000L@long literal"
The first four factors give thirty one million, five hundred and thirty six thousand seconds, which fits. Times a thousand is thirty one billion, which doesn't. So it prints one billion, four hundred and seventy one million and change. The fix: declare it a long, and write the last factor as a long literal, a thousand with an L after it.

@chapter Where people slip
@list heading="Common slips" items="Believing a double holds 0.1@The first|Expecting Java to stop on overflow@The second|Expecting integer division to round@the third"
The first slip is believing a double holds point one. It holds the nearest binary fraction. The second is expecting Java to stop on integer overflow. It wraps, silently. Only dividing by zero throws. And the third is expecting integer division to round. It truncates.

@chapter Try it
@code block=2 lines=1-5 label=Java focus="2-4@a thousand times|5@whether total overflows"
Your turn. This loop adds three million to an int total, a thousand times. Without the lab, say whether total overflows, which direction it wraps, and how to fix the code. Then check it in the lab.

@end text="Java's arithmetic, beside the exact"
You can run Java's int, long and double arithmetic beside the exact answer, on Learn. That's learn dot get er done dot I O.
