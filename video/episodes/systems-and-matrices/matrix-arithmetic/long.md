---
format: long
lesson: systems-and-matrices/matrix-arithmetic
title: Matrix products: rows against columns
thumb: Inner sizes must match
---

@chapter The idea
@title text="Matrix Products" sub="Systems and Matrices" art=thumb
Adding matrices is easy. Multiplying them is where it gets interesting: each entry of the product uses a whole row and a whole column, and the order of the factors changes the answer.

@words text="m × n" sub="m rows, n columns"
An m by n matrix has m rows and n columns. Two matrices are equal when they have the same size and agree in every position.

@chapter Sum and scalar multiple
@math heading="Entry by entry" items="A:   [ 2  −1   0 ]   [ 4   3   5 ]@Take A;;B:   [ 1   6  −2 ]   [ 0  −3   1 ]@And B;;A + B:   [ 3   5  −2 ]   [ 4   0   6 ]@A plus B;;3A:   [ 6  −3   0 ]   [ 12   9   15 ]@Three A"
Take A, with rows two, minus one, zero, and four, three, five. And B, with rows one, six, minus two, and zero, minus three, one. A plus B adds position by position: three, five, minus two, and four, zero, six. Three A multiplies every entry by three.

@art entrywise-add
Addition needs matching sizes, and then every rule you know carries over, one position at a time. A number acting on a matrix, like that three, is called a scalar.

@chapter The product
@art row-times-column
The product is different. The entry in row i, column j of A B comes from row i of A and column j of B. Multiply them in matching pairs, and add the results.

@art shape-rule
So the row length of A must equal the column height of B. Write the sizes side by side: m by n, then n by p. If the inner pair match, the outer pair give the size of the answer, m by p.

@art shape-mismatch
If the inner pair don't match, stop. The product doesn't exist. It isn't zero, and it isn't approximately anything. There is no such matrix.

@chapter A worked product
@math heading="C is 2 × 3, D is 3 × 2" items="C:   [ 1   2   0 ]   [ 3  −1   4 ]@one, two, zero;;D:   [ 2   1 ]   [ 0  −3 ]   [ 5   2 ]@D has rows;;CD is 2 × 2@two by two"
C has rows one, two, zero, and three, minus one, four. D has rows two, one, then zero, minus three, then five, two. C is two by three and D is three by two. The inner threes match, so C D is two by two.

@math heading="Row against column" items="row 1, col 1:   1(2) + 2(0) + 0(5) = 2@Row one, column one;;row 1, col 2:   1(1) + 2(−3) + 0(2) = −5@Row one, column two;;row 2, col 1:   3(2) + (−1)(0) + 4(5) = 26@Row two, column one;;row 2, col 2:   3(1) + (−1)(−3) + 4(2) = 14@Row two, column two"
Row one, column one: two plus zero plus zero, which is two. Row one, column two: one minus six plus zero, minus five. Row two, column one: six plus zero plus twenty, twenty six. Row two, column two: three plus three plus eight, fourteen.

@words text="CD = [ 2  −5 ]  [ 26  14 ]" sub="DC exists too, and is 3 × 3"
So C D has rows two, minus five, and twenty six, fourteen. D C exists too, but it's three by three. And every entry took three products, because the inner size was three. Counting them is a free check.

@chapter Order matters
@math heading="A = [ 1  2 ; 3  4 ],  B = [ 0  1 ; 1  0 ]" items="AB = [ 2  1 ]  [ 4  3 ]@A B has rows;;BA = [ 3  4 ]  [ 1  2 ]@B A has rows"
Even when both products exist and have the same size, they usually differ. Let A be one, two, three, four, and B be zero, one, one, zero. A B has rows two, one, and four, three. B A has rows three, four, and one, two.

@art swapper
B is a swapper. Multiplying A on the right by B exchanged the columns of A. Multiplying on the left exchanged the rows. Which side you multiply on is part of the expression, not a detail.

@chapter Why it's defined this way
@math heading="A system is one product" items="[ 1  1  1 ]  [ 2  −1  3 ]  [ −1  2  4 ]@the coefficient matrix;;× (x, y, z)  =  (6, 9, 15)@a column of unknowns;;Ax = b@A x equals b"
The rule looks arbitrary until you write a system with it. Take the coefficient matrix from Systems in Three Variables, times a column of unknowns, x, y, z, and set it equal to the constants, six, nine, fifteen. Each entry of the product is one equation's left side. So the whole system is the single statement A x equals b.

@art system-as-product
At one, two, three, the rows give one plus two plus three, six. Two minus two plus nine, nine. And minus one plus four plus twelve, fifteen. One product checks the whole system.

@chapter Where people slip
@list heading="Common slips" items="Multiplying entry by entry@The first|Right number, wrong position@The second|Assuming AB exists because BA does@the third"
The first slip is multiplying entry by entry. For the swapper example that gives zero, two, three, zero, which is neither product. The second is putting a correct number in the wrong position. And the third is assuming A B exists because B A does. A three by two times a two by five is fine. The other order pairs five against three.

@chapter Try it
@words text="C: rows (1, 0, −2), (3, 1, 4)     D: column (2, −1, 5)" sub="CD exists and is 2 × 1"
Your turn. C is two by three, with rows one, zero, minus two, and three, one, four. D is a column: two, minus one, five. C D exists and is two by one. Compute its two entries, then explain from the sizes why D C doesn't exist.

@end text="Rows against columns"
You can build a product one row and column at a time, on Learn. That's learn dot get er done dot I O.
