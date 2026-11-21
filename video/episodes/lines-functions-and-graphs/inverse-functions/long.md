---
format: long
lesson: lines-functions-and-graphs/inverse-functions
title: Inverse functions: undoing a function, and when you can't
thumb: Undo it, if you can
---

@chapter The idea
@title text="Inverse Functions" sub="Lines, Functions and Graphs" art=thumb
A function takes an input to an output. Can you run it backwards, and get the input back from the output? Sometimes. And the times you can't are the interesting part.

@art round-trip
An inverse sends every output back to the input it came from. That only works if the function is one to one: different inputs always give different outputs. Then the inverse, written f inverse, has the range of f as its domain.

@math heading="f(x) = 3x − 7" items="f⁻¹(x) = (x + 7)/3@inverse is;;1/f(x) = 1/(3x − 7)@reciprocal;;at x = −1:  2  vs  −1/10@At minus one"
The little minus one is a label, not an exponent. f inverse of x is not one over f of x. For f of x equals three x minus seven, the inverse is x plus seven, over three. The reciprocal is one over three x minus seven. At minus one, they give two and minus one tenth.

@chapter The horizontal line test
@art horizontal-test-fail
Here's the test. A function has an inverse exactly when no horizontal line meets its graph more than once. A horizontal line is all the points with one output, so two crossings mean two inputs sharing an output.

@art horizontal-test-pass
It pairs with the vertical line test. The vertical test asks whether a graph is a function at all. The horizontal test asks whether that function can be run backwards.

@chapter The swap method
@math heading="f(x) = 3x − 7" items="y = 3x − 7@write y;;x = 3y − 7@swap;;x + 7 = 3y@add seven;;y = (x + 7)/3@divide by three"
To find an inverse, write y for the output. Swap x and y. Then solve for y. So y equals three x minus seven becomes x equals three y minus seven. Add seven, and divide by three. The inverse is x plus seven, over three.

@art mirror-line
The swap is doing something specific. The graph of the inverse is the graph of f reflected in the line y equals x. Exchanging the letters is that reflection, done on the equation.

@math heading="check both directions" items="f(2) = −1,  f⁻¹(−1) = 6/3 = 2@f of two;;f⁻¹(f(x)) = ((3x − 7) + 7)/3 = x@f inverse of f;;f(f⁻¹(x)) = 3((x + 7)/3) − 7 = x@f of f inverse"
Check it. f of two is minus one, and the inverse of minus one is six over three, two. Back where you started. Then prove it for every input. f inverse of f of x simplifies to x. And f of f inverse of x also simplifies to x.

@words text="✗  x/3 + 7" sub="f(2) = −1, but −1/3 + 7 = 20/3"
Order matters when you undo. Three x minus seven multiplies first and subtracts second. So the inverse adds first and divides second. Writing x over three, plus seven, fails at once: minus one over three, plus seven, is twenty thirds, not two.

@chapter When there's no inverse
@words text="2 → 4   and   −2 → 4"
Now x squared, on all the real numbers. The output four came from two and from minus two. An inverse would have to choose. So x squared has no inverse at all.

@art restricted-half
The repair is to restrict the domain. On x at least zero, x squared is one to one. Swap to get x equals y squared, so y is plus or minus root x. The restriction says y is at least zero, so take the positive root. The inverse is root x.

@math items="p(5) = 25@five squared;;p⁻¹(25) = √25 = 5@root twenty five"
Check it: five squared is twenty five, and root twenty five is five. Back to five.

@art two-halves
On the other half, x at most zero, the same swap picks minus root x. Both are correct inverses of different halves. So calling root x the inverse of x squared is only true once you say x is at least zero.

@list heading="Which are one-to-one?" items="Non-horizontal lines: yes, inverse slope 1/m@Every line|Horizontal lines: no@horizontal line|x², |x|, even powers: not without a restriction@Even powers|x³, odd powers: yes, the cube root@Odd powers"
Every line except a horizontal one is one to one, and its inverse is a line with slope one over m. A horizontal line isn't. Even powers and absolute value aren't, without a restriction. Odd powers are. x cubed inverts to the cube root, with no restriction.

@chapter Where people slip
@list heading="Common slips" items="Reading −1 as an exponent@The first|Undoing in the original order@The second|Dropping the restriction@the third"
The first slip is reading the minus one as an exponent. The second is undoing the steps in the order they were done. And the third is dropping the restriction.

@chapter Try it
@words text="g(x) = 5x + 2" sub="swap given: x = 5y + 2"
Try g of x equals five x plus two. The swap is given: x equals five y plus two. Solve for y, state the inverse's domain, and simplify both compositions. Use g of minus one equals minus three for a round trip. Then explain why h of x equals four can't pass the same test.

@end text="Run it backwards"
The full lesson is on Learn. That's learn dot get er done dot I O.
