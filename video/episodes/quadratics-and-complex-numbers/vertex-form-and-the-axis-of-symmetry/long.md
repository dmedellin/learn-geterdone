---
format: long
lesson: quadratics-and-complex-numbers/vertex-form-and-the-axis-of-symmetry
title: Vertex form: read the vertex without solving anything
thumb: The vertex, in plain sight
---

@chapter The form
@title text="Vertex Form and the Axis of Symmetry" sub="Quadratics and Complex Numbers" art=thumb
The same quadratic can be written in more than one way. One way hides the parabola's most important point. The other puts it in plain sight.

@art vertex-point
The vertex is where a parabola meets its axis of symmetry. It's the lowest point when the curve opens upward, and the highest when it opens downward. A parabola has exactly one.

@math heading="Vertex form" items="y = a(x − h)² + k,  a ≠ 0@y equals a;;vertex (h, k),  axis x = h@the vertex is"
Vertex form is y equals a, times x minus h, squared, plus k. The vertex is h, k, and the axis is the line x equals h. And a is the same a as before, doing the same two jobs.

@words text="(x + 3)² = (x − (−3))²" sub="h = −3"
Watch the sign. The form has a minus built in, so x plus three, squared, is x minus minus three, squared. That means h is minus three, and the axis is x equals minus three. Reading plus three off the bracket puts the vertex on the wrong side.

@chapter Why k is the extreme
@art never-below
Here's why that point is special. x minus h, squared, is never negative, and it's zero only when x is h. If a is positive, multiplying keeps the inequality, so f of x is at least k. If a is negative, multiplying flips it, so f of x is at most k. Either way, the extreme is exactly at h.

@art arch-top
That proof says the vertex is the optimum without appealing to a picture. That matters for problems where there's no picture to look at.

@chapter Converting
@math heading="y = 2x² − 12x + 13" items="= 2(x² − 6x) + 13@factor two out;;= 2(x² − 6x + 9 − 9) + 13@add and subtract nine"
Convert two x squared minus twelve x plus thirteen. Factor two out of the x terms only, and leave the thirteen alone. Half of minus six is minus three, and that squared is nine, so add and subtract nine inside the bracket.

@math heading="y = 2x² − 12x + 13" items="= 2((x − 3)² − 9) + 13@x minus three;;= 2(x − 3)² − 18 + 13@minus eighteen;;= 2(x − 3)² − 5@minus five"
That makes x minus three, squared, minus nine. Bring the minus nine out of the bracket, and it becomes minus eighteen. So y is two times x minus three, squared, minus five.

@words text="vertex (3, −5)  ·  minimum −5" sub="check: f(3) = 18 − 36 + 13 = −5"
The vertex is three, minus five, and since a is positive, minus five is the minimum. Check: f of three is eighteen minus thirty six plus thirteen, minus five.

@art doubled-block
The minus eighteen line is where this goes wrong. The minus nine sits inside a bracket multiplied by two, so bringing it out costs minus eighteen, not minus nine.

@words text="y + 9 = 2(x² − 6x + 9) + 13  ✗" sub="defines y = 2x² − 12x + 22"
And don't add nine to both sides here. The nine inside the bracket carries the factor two, so the right rises by eighteen while the left rises by nine. That defines a different function. Add and subtract inside the expression instead.

@chapter A faster route
@math heading="Where h and k come from" items="b = −2ah  ⟹  h = −b/(2a)@b equals;;k = f(h)@And k is just"
Expand vertex form and compare it with standard form. The x terms give b equals minus two a h, so h is minus b over two a. And k is just f of h.

@art two-roads
So there are two routes. Completing the square shows the work. Minus b over two a, then f of h, is quicker, with fewer fractions. They agree, because one was derived from the other.

@math heading="Two more" items="−2x² + 8x − 5 = −2(x − 2)² + 3@minus two x squared;;x² − 3x + 1:  h = 3/2,  k = −5/4@x squared minus three x"
Minus two x squared plus eight x minus five becomes minus two, times x minus two, squared, plus three. The vertex is two, three, and since a is negative, three is the largest value. For x squared minus three x plus one, h is three halves, and f of three halves is minus five quarters. Keep the fractions.

@chapter Every parabola is one curve
@art shift-stretch
Vertex form is also a transformation. It's y equals x squared, stretched by a factor a, shifted h to the right, and k up. That's why every parabola really is the same curve, at a different size and in a different place.

@chapter Where people slip
@list heading="Common slips" items="Bringing the square out without multiplying by a@The first|Reading h with the wrong sign@The second|Changing one side of a function definition@The third"
The first slip is bringing the subtracted square out without multiplying by a. The second is reading h with the wrong sign. x plus three, squared, has its vertex at minus three. The third is changing one side of a function definition only, which defines a different function.

@end text="Add, subtract, read the vertex"
Convert a few quadratics to vertex form and check each vertex, on Learn. That's learn dot get er done dot I O.
