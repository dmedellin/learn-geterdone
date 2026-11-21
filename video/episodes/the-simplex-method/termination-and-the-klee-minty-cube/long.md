---
format: long
lesson: the-simplex-method/termination-and-the-klee-minty-cube
title: The Klee-Minty cube: when simplex visits every corner
thumb: Finite isn't fast
---

@chapter The question
@title text="Termination and the Klee-Minty Cube" sub="The Simplex Method" art=thumb
Bland's rule proves the simplex method stops. But how soon? A finite walk through a huge set can still be a very long walk.

@words text="n choose m bases"
The guarantee counts bases, and there are n choose m of them. With a hundred rows and two hundred columns, that's a number with more than fifty digits. Finite, on its own, promises nothing useful.

@chapter The cube
@art deformed-cube
Klee and Minty built a programme whose region is a squashed n dimensional cube, with two to the n corners. Start the most negative rule at the origin, and it visits every single corner, taking two to the n minus one pivots.

@math heading="n = 3" items="maximise 100x₁ + 10x₂ + x₃@a hundred x one;;x₁ ≤ 1@at most one;;20x₁ + x₂ ≤ 100@twenty x one;;200x₁ + 20x₂ + x₃ ≤ 10000@two hundred x one"
At n equals three, maximise a hundred x one plus ten x two plus x three. Subject to x one at most one. Twenty x one plus x two at most a hundred. And two hundred x one plus twenty x two plus x three at most ten thousand.

@math heading="Most-negative rule, from the origin" items="z: 0 → 100 → 900 → 1000@nine hundred;;z: 1000 → 9000 → 9100 → 9900@nine thousand;;z → 10000 at (0, 0, 10000)@ten thousand"
Watch z climb. Zero, a hundred, nine hundred, a thousand. Then nine thousand, nine thousand one hundred, nine thousand nine hundred. And finally ten thousand, at zero, zero, ten thousand.

@art corner-tour
Eight vertices, all eight stood at, and seven pivots. That's two cubed minus one.

@chapter Counting by rule
@math heading="Pivots taken" items="most negative:  3, 7, 15@three, seven, fifteen;;smallest index:  3, 5, 9@three, five, nine;;greatest improvement:  1, 1, 1@one every time"
Now compare rules at n equals two, three and four. The most negative rule takes three, seven, fifteen: two to the n minus one. The smallest index rule takes three, five, nine. Greatest improvement takes one, every time. The optimum is a hundred to the n minus one.

@art doubling-bars
The doubling is the whole point, and it's plain by fifteen. At n equals five it would be thirty one. That's why the lab stops at four.

@chapter Rule and objective
@art one-step
Keep the region, and reverse the objective coefficients: one, ten, a hundred. The optimal vertex doesn't move. Now the most negative rule takes one pivot, at every n. The smallest index rule takes three, five, nine, unchanged, because it never reads a coefficient.

@art adversarial
So two to the n minus one isn't a fact about cubes, or about the simplex method. It's one rule, on one objective, over one region, arranged to be adversarial together. Worst cases are built, not found.

@chapter Two false implications
@list heading="False implications" items="Exponential, so it's slow@The first|LP is polynomial, so simplex is@The second"
The first false step: it's exponential, so it's slow. That's a worst case over all inputs, applied to the inputs anyone actually has. Real problems finish in a small multiple of the number of rows. The second false step is its mirror: linear programming is polynomial, so simplex is.

@words text="Ellipsoid · interior point" sub="different algorithms"
Linear programming is solvable in polynomial time. The ellipsoid method established it, and interior point methods made it practical. Those are different algorithms. It's like concluding bubble sort is fast because sorting can be done in n log n.

@chapter What is true
@list heading="Three true statements" items="Finite@It's finite|Exponential in the worst case@exponential|Fast in practice@fast in practice"
Three statements, each true, none implying another. It's finite, because under a smallest index rule no basis repeats. It's exponential in the worst case, because this cube exists. And it's fast in practice, because cubes like this are constructed, not met. Drop any one, and you get a sentence that's wrong in a direction someone will act on.

@art exact-fractions
And neither famous result survives floating point. The count two to the n minus one holds only if comparisons among coefficients from one to ten to the n minus one land exactly. Here, exact arithmetic is the content, not the style.

@chapter Where people slip
@list heading="Common slips" items="Worst case as a statement about real problems@The first|Moving a complexity class to an algorithm@The second|Reading 2ⁿ − 1 as a property of the region@The third"
The first slip is reading the worst case as a statement about ordinary problems. The second is moving a complexity class from the problem to the algorithm. And the third is reading two to the n minus one as a property of the region.

@end text="March around the cube"
You can watch each rule walk the cube at two, three and four dimensions, on Learn. That's learn dot get er done dot I O.
