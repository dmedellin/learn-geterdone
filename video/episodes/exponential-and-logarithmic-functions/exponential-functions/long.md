---
format: long
lesson: exponential-and-logarithmic-functions/exponential-functions
title: Exponential functions: when the variable moves into the exponent
thumb: A line adds, this multiplies
---

@chapter The move
@title text="Exponential Functions" sub="Exponential and Logarithmic Functions" art=thumb
Every function you've met so far kept the variable in the base. x squared, x cubed, the square root of x. Now move the variable up into the exponent, and the values start behaving in a completely different way.

@art add-vs-multiply
A line adds. Raise x by one and it gains the same amount every time. An exponential multiplies. Raise x by one and it's multiplied by the same amount every time. That one difference is most of the lesson.

@math heading="Exponential function" items="f(x) = a·bˣ@f of x equals;;a ≠ 0,   b > 0,   b ≠ 1@a isn't zero;;f(0) = a@at x equals zero"
Here's the definition. f of x equals a times b to the x, where a isn't zero, b is positive, and b isn't one. The number b is the base. And at x equals zero, b to the zero is one, so the value there is a.

@chapter Why the base is fenced in
@art scattered-dots
Why must the base be positive? Try minus four. Minus four to the first is minus four, and squared it's sixteen. Fine. But minus four to the one half is the square root of minus four, which isn't real. What survives is a scattered set of points with no interval in it, so there's no curve to draw.

@art flat-line
A base of one doesn't break at all. One to any power is one, so you just get the constant a, a flat horizontal line. It's excluded because calling that exponential would make every statement about growth and decay false.

@chapter Constant ratio
@math heading="g(x) = 3 + 3x     f(x) = 3·2ˣ" items="x:   0,  1,  2,  3,  4@from zero to four;;g:   3,  6,  9,  12,  15     differences  3, 3, 3, 3@The line;;f:   3,  6,  12,  24,  48     ratios  2, 2, 2, 2@The exponential"
Take x from zero to four. The line, three plus three x, gives three, six, nine, twelve, fifteen. Its differences are three every time. The exponential, three times two to the x, gives three, six, twelve, twenty four, forty eight. Its ratios are two every time.

@words text="f(x + 1) / f(x) = b" sub="at every x"
That's no accident. Divide f of x plus one by f of x. The a cancels, a factor of b to the x cancels, and what's left is b, whatever x is. So to recognise an exponential from a table, divide neighbours. If the ratio stays put, that ratio is the base.

@words text="Two matching points prove nothing" sub="both pass through (0, 3) and (1, 6)   ·   at x = 4: 48 and 15"
Notice that both functions pass through zero, three and one, six. After that they part. At x equals four they're forty eight and fifteen. A line and an exponential can always be made to agree at two points.

@chapter The line it never touches
@art exponential-curve
Every value of b to the x is positive, so a times b to the x is never zero. For a base above one, as x runs off to the left, the values shrink without limit and the curve settles toward the line y equals zero without arriving. That line is the horizontal asymptote.

@math heading="Small is not zero" items="2⁻³ = 1/8@two to the minus three;;2⁻²⁰ = 1/1048576@two to the minus twenty"
Two to the minus three is one eighth. Two to the minus twenty is one over one million, forty eight thousand, five hundred and seventy six. Small, but not zero. No real exponent makes a positive base give zero.

@chapter Reading a formula
@math heading="f(x) = 2ˣ" items="f(0) = 1@f of zero is one;;asymptote  y = 0@The asymptote;;range: every y > 0@the range"
You can read a lot straight off a formula. Start with two to the x. Here a is one, so f of zero is one. The asymptote is y equals zero, and the range is every positive number.

@art lifted-curve
Now add three. Two to the x plus three is the same curve lifted by three, and the asymptote goes up with it, to y equals three. So f of zero is four, and the range is every number above three.

@art halving-bars
And three times one half to the x? It starts at three, then three halves, three quarters, three eighths, three sixteenths. Each value is half the one before. Still a constant ratio, and the ratio is one half.

@chapter Where people slip
@list heading="Common slips" items="Reading 2ˣ as 2x@The first|Reading 3·2ˣ as (3·2)ˣ@The second|Saying the curve reaches its asymptote@The third"
The first is reading two to the x as two times x. They agree at one and two, but at five they're thirty two and ten. The second is reading three times two to the x as six to the x. At x equals two, that's twelve against thirty six. The power comes first. The third is saying the curve reaches its asymptote.

@chapter Try it
@words text="h(x):  −4,  −12,  −36,  −108" sub="at x = 0, 1, 2, 3   ·   first ratio  (−12)/(−4) = 3"
Here's one to try. At x equals zero, one, two and three, a function gives minus four, minus twelve, minus thirty six and minus one hundred and eight. The first ratio is minus twelve over minus four, which is three. Finish the ratios and differences, decide what kind of function it is, and state a, b and the asymptote.

@end text="Ratio against difference"
You can set a and b, watch the ratio column, and try a negative base to see the curve fail, on Learn. That's learn dot get er done dot I O.
