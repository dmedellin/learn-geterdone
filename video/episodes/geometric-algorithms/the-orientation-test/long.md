---
format: long
lesson: geometric-algorithms/the-orientation-test
title: The orientation test: one determinant behind all of geometry
thumb: Left, right, or on the line
---

@chapter One number
@title text="The Orientation Test" sub="Geometric Algorithms" art=thumb
Which side of a line is a point on? Do two segments cross? Which way is a polygon wound? Does a corner survive on a hull? Every one of those questions comes down to the sign of one small determinant.

@art left-right-turn
Walk from a point a to a point b, then on to c. At b you either turn left, turn right, or carry straight on. The orientation test tells you which, using nothing but six integers.

@math heading="orient(a, b, c)" items="(bx − ax)(cy − ay) − (by − ay)(cx − ax)@b x minus a x;;sign 1  ⟹  left turn, counter-clockwise@sign is one;;sign −1  ⟹  right turn, clockwise@minus one;;sign 0  ⟹  collinear@zero"
Here it is. b x minus a x, times c y minus a y, minus b y minus a y, times c x minus a x. If the sign is one, the path turns left, counter-clockwise. If it's minus one, it turns right. And if it's zero, the three points lie on one line.

@chapter Order is data
@art swapped-arguments
All three arguments are ordered. Swap any two and the determinant changes sign. So left of the line through a and b is exactly the same statement as right of the line through b and a.

@words text="orient(a, b, c) = −orient(b, a, c)" sub="depends only on b − a and c − a"
And because it only uses the differences b minus a and c minus a, sliding all three points by the same amount changes nothing at all.

@chapter Twice an area
@art triangle-parallelogram
The size of the number means something too. Put a at the origin and call the two differences u and v. They span a parallelogram, and the triangle a b c is exactly half of it.

@words text="|orient(a, b, c)| = 2 × area(abc)"
So the absolute value of the determinant is twice the area of the triangle. The sign says whether v sits counter-clockwise or clockwise from u. And the determinant is zero exactly when the triangle is flat, which means the points are collinear.

@chapter Three routes
@math heading="(0, 0), (4, 0), (2, 3)" items="2×2:  (4 − 0)(3 − 0) − (0 − 0)(2 − 0) = 12@four minus zero;;3×3 by cofactors:  0·(0 − 3) − 0·(4 − 2) + (4·3 − 2·0) = 12@cofactors;;doubles:  12@floating point;;area = 12 ÷ 2 = 6@the area is six"
Take zero, zero, then four, zero, then two, three. The two by two route gives four minus zero times three minus zero, minus zero, which is twelve. Expanding the three by three determinant by cofactors also gives twelve. Ordinary floating point says twelve as well. So the area is six, and it's a left turn.

@art three-routes
Why compute the same thing three ways? Because it isn't the same arithmetic. One route multiplies differences, the other multiplies the coordinates themselves. A transposed subscript gives a number that looks perfectly reasonable, and only a second route catches it, as a disagreement.

@chapter Four questions, one test
@art hull-corner
Is c left of the directed line from a to b? That's orient greater than zero. Do two segments cross properly? Four such tests, with opposite signs in pairs. Is a polygon counter-clockwise? A sum of n determinants is positive. Did the last hull point make a non-left turn? The same test again.

@words text="Get the sign wrong once" sub="every answer still looks well formed"
Get the sign wrong once and the hull loses a vertex, and the segment test answers about the wrong pair. Each failure is silent. That's why the algorithms keep the sign and throw the magnitude away.

@chapter No such thing as nearly zero
@math heading="(0, 0), (7, 3), (5, 2)" items="7·2 − 3·5 = 14 − 15 = −1@fourteen minus fifteen;;area = 1/2@one half"
Now try zero, zero, then seven, three, then five, two. That's seven times two, minus three times five, fourteen minus fifteen, minus one. A triangle of area one half. The points are very nearly on a line, and they are definitely not.

@art near-collinear
With integer coordinates, one is the smallest nonzero determinant there is. There's no room between area one half and area zero for an integer to be unsure about. That's why the lab keeps the determinant as an integer, and doubles areas instead of halving them. The same habit keeps distances squared.

@chapter Where people slip
@list heading="Common slips" items="Reading the determinant as a distance@The first|Swapping two arguments@The second|Rounding a small determinant to zero@And the third"
The first slip is reading the determinant as a distance. It's twice an area, so only compare determinants across the same base pair. The second is swapping two arguments, which answers the negated question. It's the most common way a hull comes back inside out. And the third is rounding a small determinant to zero, which turns a genuine right turn into a false collinearity.

@chapter Try it
@words text="(0, 0), (4, 0), (2, 3)" sub="now try (0, 0), (2, 3), (4, 0)"
Your turn. Start from the lab's opening points and confirm the twelve by hand. Then swap the last two points and predict the new sign before you compute it.

@end text="Three routes, one sign"
You can compute the determinant three ways side by side on Learn. That's learn dot get er done dot I O.
