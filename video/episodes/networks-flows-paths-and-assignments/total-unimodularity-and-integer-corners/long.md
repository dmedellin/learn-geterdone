---
format: long
lesson: networks-flows-paths-and-assignments/total-unimodularity-and-integer-corners
title: Why network LPs give whole-number answers: total unimodularity
thumb: Whole corners, for free
---

@chapter The puzzle
@title text="Total Unimodularity and Integer Corners" sub="Networks, Flows, Paths and Assignments" art=thumb
Every network optimum on this course has come out in whole units, and nobody asked for that. There was no integer constraint anywhere. So why does the simplex method keep landing on whole numbers?

@art lattice-corner
Because the corners of the feasible region all sit on whole-number points. And the simplex method stops at a corner. The reason the corners are whole is a property of the matrix, and it has a name.

@chapter The definition
@words text="Every square submatrix: det ∈ {0, +1, −1}"
A matrix is totally unimodular when every square submatrix, of every size, has determinant zero, plus one, or minus one. You choose any rows, the same number of columns, and take the determinant. Every single choice has to pass.

@art submatrix-sweep
On the five arc network from earlier, the incidence matrix is four by five. Checking every submatrix of size one, two and three means twenty, then sixty, then forty, which is one hundred and twenty in all. The lab sweeps all of them and finds no failures.

@words text="The whole matrix: det = 0" sub="its rows sum to the zero row"
And notice: the whole matrix is singular. Every column has one plus one and one minus one, so the rows add to zero. The determinant of the whole thing isn't what matters. Every submatrix is.

@chapter Cramer's rule is the proof
@math heading="A basic solution" items="B x_B = b@B times;;x_k = det(B_k) / det(B)@Cramer's rule;;det(B) = ±1@plus or minus one;;integer ÷ ±1 = integer@an integer"
A basic solution solves B times x B equals b, for a square piece B that is non singular. By Cramer's rule, each component is the determinant of B k, over the determinant of B. That bottom is plus or minus one. The top is whole when the data are whole. An integer divided by plus or minus one is an integer.

@art cramer-divide
That's the whole argument. It doesn't depend on the objective, so it holds at the optimum. Whole supplies and whole capacities give whole corners, with no integer constraint written anywhere.

@chapter Drop the directions
@art triangle-graph
Now take a triangle on three vertices and build the undirected incidence matrix instead, plus one at both ends of each edge. The picture hasn't changed. But this three by three matrix has determinant two.

@math heading="max x₁ + x₂ + x₃,  Ax ≤ 1,  x ≥ 0" items="corner x = (½, ½, ½)@one half;;value 3/2@three halves;;best whole answer: 1@best whole"
Solve a packing programme on it: maximise the sum of the three variables, with each row at most one. The exact simplex returns one half, three times. That's worth three halves. No integer point reaches three halves. The best whole answer is one.

@art half-corner
Those halves aren't rounding error. One half, one half, one half is a genuine corner, strictly better than any whole point inside. That gap is what the whole of integer programming is about.

@chapter Odd cycles, not undirectedness
@art square-cycle
Do the same on a four cycle. Its undirected incidence matrix has determinant zero, the sweep finds nothing outside zero and plus or minus one, and the corner is one, zero, one, zero, worth two. Whole. So it's the odd cycle that breaks it. An even cycle is bipartite, and that's why the assignment problem behaves.

@chapter Where people slip
@list heading="Common slips" items="Checking only the whole matrix's determinant@The first|Calling integrality a property of the problem@The second|Reading halves as a numerical glitch@And the third"
The first slip is checking only the whole matrix's determinant. The second is calling integrality a property of the problem. It's a property of the matrix you wrote. And the third is reading a fractional corner as a numerical glitch. Better arithmetic won't make it go away.

@words text="Sufficient, not necessary"
One more warning. Total unimodularity is enough for whole corners, but it isn't required. And a programme without it might still give a whole optimum on some instance. That's luck, not structure.

@chapter Try it
@words text="Rows 1, 2, 3 · Columns 1, 3, 4" sub="of N for s→a, s→b, a→b, a→t, b→t"
Your turn. Write out the incidence matrix for the five arc network. Pick rows one, two and three, and columns one, three and four, and compute that determinant by hand. The lesson's answer is one. Then try the directed triangle and see why it passes.

@end text="Sweep every submatrix"
You can sweep every submatrix and watch the triangle's corner turn into halves, on Learn. That's learn dot get er done dot I O.
