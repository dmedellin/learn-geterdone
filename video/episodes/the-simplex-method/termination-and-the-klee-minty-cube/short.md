---
format: short
lesson: the-simplex-method/termination-and-the-klee-minty-cube
title: The cube that makes simplex visit every corner
---

@art corner-tour
Here's a cube where the simplex method visits every single corner.

@math items="n = 2, 3, 4:  3, 7, 15 pivots@three, seven, fifteen;;= 2ⁿ − 1@two to the n"
On the Klee Minty cube, the most negative rule takes three, seven, fifteen pivots, as the dimension grows. That's two to the n minus one.

@words text="Reverse the objective: 1 pivot"
But reverse the objective on the same cube, and the same rule takes one pivot. The worst case was built, not found.

@end text="Full lesson on Learn"
The full lesson, with every rule on the cube, is on Learn.
