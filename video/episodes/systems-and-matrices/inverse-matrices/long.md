---
format: long
lesson: systems-and-matrices/inverse-matrices
title: Inverse matrices: how to undo a matrix
thumb: Multiply on the left
---

@chapter The question
@title text="Inverse Matrices" sub="Systems and Matrices" art=thumb
With matrix products, a whole system becomes one equation. And one equation looks like something you should be able to solve in a single step.

@math heading="One equation" items="4x + 7y = 1,    2x + 6y = 8@four x plus seven y;;A = [ 4  7 ; 2  6 ],   X = (x, y),   B = (1, 8)@A is;;AX = B@A X equals B"
Four x plus seven y equals one, and two x plus six y equals eight. A is four, seven, two, six. X is the column x, y, and B is one, eight. So A X equals B, which looks like it's asking to be divided by A.

@words text="no matrix division" sub="multiply by an inverse instead"
But there's no matrix division. What replaces it is multiplication by an inverse. So first, what's an inverse?

@art identity-grid
The identity, I, is the square matrix with ones down the main diagonal and zeros everywhere else. A times I and I times A are both A. It behaves the way one behaves among numbers.

@art undo-arrows
An inverse of a square matrix A is a matrix A inverse, the same size, with A times A inverse and A inverse times A both equal to I. A matrix has at most one, and only square matrices can have one.

@chapter The 2 by 2 formula
@math heading="If ad − bc ≠ 0" items="[ a  b ; c  d ]⁻¹  =  (1 / (ad − bc)) · [ d  −b ; −c  a ]@one over a d minus b c"
For a, b, c, d, with a d minus b c not zero, the inverse is one over a d minus b c, times the matrix d, minus b, minus c, a. If a d minus b c is zero, there's no inverse.

@art swap-negate
Notice what moves. a and d change places. b and c stay where they are, and change sign. Only one of those is a swap.

@math heading="Why it works" items="[ a  b ; c  d ] [ d  −b ; −c  a ]  =  (ad − bc) I@Multiply the two"
Multiply the two arrays first. The diagonal entries come out as a d minus b c, and the other two are zero. So the product is a d minus b c, times I. Divide by that number and you get exactly I. If it's zero, the product is the zero matrix, and no scaling can rescue it.

@chapter A worked inverse
@math heading="A = [ 4  7 ; 2  6 ]" items="ad − bc = 24 − 14 = 10@twenty four minus fourteen;;[ 6  −7 ; −2  4 ]@Swap the diagonal;;A⁻¹ = [ 3/5  −7/10 ; −1/5  2/5 ]@divide by ten"
For four, seven, two, six, a d minus b c is twenty four minus fourteen, which is ten. Swap the diagonal and negate the other two: six, minus seven, minus two, four. Then divide by ten. The inverse is three fifths, minus seven tenths, minus one fifth, two fifths.

@math heading="Check one entry, then solve" items="4(3/5) + 7(−1/5) = 12/5 − 7/5 = 1@four times three fifths;;x = (3/5)(1) + (−7/10)(8) = −5@x is;;y = (−1/5)(1) + (2/5)(8) = 3@y is"
Check the top left of A times A inverse: four times three fifths, plus seven times minus one fifth, is twelve fifths minus seven fifths, which is one. Now solve. x is three fifths minus twenty eight fifths, minus five. y is minus one fifth plus sixteen fifths, three.

@words text="X = A⁻¹B" sub="multiply on the left, on both sides"
That was X equals A inverse B. Multiplying both sides on the left by A inverse gives I X, which is X. It has to be on the left. X times A inverse is a different product, and usually isn't even defined.

@chapter Any size
@art augment-identity
For bigger matrices, skip the formula. Write A and the identity side by side, and row reduce. When the left half becomes I, the right half is A inverse, because the operations that carry A to I carry I to A inverse.

@math heading="[ A | I ]  →  [ I | A⁻¹ ]" items="[ 4  7 | 1  0 ]    [ 2  6 | 0  1 ]@four, seven, one, zero;;[ 1  0 | 3/5  −7/10 ]    [ 0  1 | −1/5  2/5 ]@the same inverse"
Start with four, seven, one, zero, and two, six, zero, one. Four row operations later the left half is the identity, and the right half is the same inverse the formula gave, entry for entry.

@chapter Singular matrices
@art singular-flat
Among numbers, only zero has no reciprocal. A matrix can lack an inverse without being zero. Two, three, four, six has a d minus b c equal to twelve minus twelve, zero, and no zero entry anywhere. It's called singular.

@math heading="The systems behind it" items="2x + 3y = 1,    4x + 6y = 2:    infinitely many@equals two;;2x + 3y = 1,    4x + 6y = 5:    none@equals five"
Its systems agree. Two x plus three y equals one, with four x plus six y equals two, has infinitely many solutions. With four x plus six y equals five instead, it has none. No single inverse could deliver both answers.

@art socks-shoes
One more fact. The inverse of A B is B inverse times A inverse. The order reverses, for the same reason socks come off after shoes.

@chapter Where people slip
@list heading="Common slips" items="Writing B over A@The first|Negating the diagonal@The second|Not dividing all four entries@the third"
The first slip is writing B over A. There's no matrix division, only multiplication by A inverse, on a side. The second is negating the diagonal instead of the other two entries. And the third is not dividing by the determinant. Six, minus seven, minus two, four is ten times the inverse.

@chapter Try it
@words text="Invert [ 2  1 ; 5  3 ]" sub="its determinant is nonzero"
Your turn. Invert two, one, five, three. Its determinant is nonzero, so an inverse exists. Swap and negate, divide every entry by the determinant, and multiply in both orders to check you get the identity.

@end text="Multiply back to check"
You can invert a matrix by row reduction, step by step, on Learn. That's learn dot get er done dot I O.
