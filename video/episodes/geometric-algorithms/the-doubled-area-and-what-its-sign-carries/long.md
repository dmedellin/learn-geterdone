---
format: long
lesson: geometric-algorithms/the-doubled-area-and-what-its-sign-carries
title: The shoelace formula: twice the area, and a sign that means something
thumb: The sign is the winding
---

@chapter One sum
@title text="The Doubled Area and What Its Sign Carries" sub="Geometric Algorithms" art=thumb
Add up one small determinant over every edge of a polygon. The total is twice the area, and its sign tells you which way round you typed the vertices. Both halves of that are useful.

@math heading="The shoelace formula" items="2A = Σ (xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ)@two A equals;;v₍ₙ₊₁₎ = v₁@wrapping;;2A > 0 counter-clockwise,  < 0 clockwise,  = 0 no area@positive"
Two A equals the sum, over the edges, of x i times y i plus one, minus x i plus one times y i, wrapping round so the last vertex connects back to the first. It's positive when the vertices run counter-clockwise, negative when clockwise, and zero when the polygon encloses no area.

@chapter Where it comes from
@art origin-fan
Each term is the orientation determinant of one edge against the origin. That's twice the signed area of the triangle from the origin to that edge. Add them up over every edge, and the triangles overlap and cancel.

@art polygon-fan
What survives is twice the area of the polygon. You can also see it by fanning triangles out from the first vertex. That needs the polygon to be simple. A self intersecting polygon still has a sum, but it counts how many times each region is enclosed, which is the winding number by another name.

@chapter The same square, twice
@math heading="Four corners, two orders" items="(0, 0), (5, 0), (5, 5), (0, 5):  2A = 50@fifty;;(0, 0), (0, 5), (5, 5), (5, 0):  2A = −50@minus fifty;;area 25 both times@twenty five"
Type zero, zero, five, zero, five, five, zero, five, and the lab says two A is fifty, counter clockwise. Type the same corners in the opposite order, and it says minus fifty, clockwise. Area twenty five both times.

@art square-both-ways
Nothing about the shape changed. The sign is reporting the listing. A negative number here isn't an error. Half the algorithms in computational geometry need a known orientation, and the cheapest way to get one is to compute the signed area and reverse the list if it's negative.

@chapter Why doubled
@art half-triangle
On a lattice, this triangle is as small as a triangle can be. Its area is one half, and a half isn't an integer. Two of them make a parallelogram of area one, and that's the trick.

@words text="area can be ½ · twice the area is an integer"
Why print twice the area? A lattice polygon's area can be a half. The smallest nonzero triangle has area one half. Twice the area is always an integer, so every step stays exact. You halve once, at the very end, and print an exact fraction.

@chapter A second route
@math heading="The trapezoid rule" items="Σ (xᵢ − xᵢ₊₁)(yᵢ + yᵢ₊₁)@the trapezoid rule"
The lab runs a second formula beside it. The trapezoid rule sums x i minus x i plus one, times y i plus y i plus one. Algebraically it's the same total. Arithmetically it's not: it multiplies differences of x by sums of y.

@art two-routes
A transposed subscript in either formula gives a plausible number. Only a route that's wrong in exactly the same way could hide it. So the lab prints both and marks a disagreement in red. The arithmetic checker adds a third route, the fan of orientation determinants, and requires all three to agree.

@chapter Zero is an answer
@art flat-polygon
Now a polygon with nothing inside it. A degenerate case that still answers is what separates a complete implementation from one that's never been given anything unusual.

@words text="(0, 0), (3, 3), (6, 6)" sub="2A = 0 · no orientation · no interior"
Three collinear vertices, zero, zero, three, three, six, six. Two A is zero. There's no orientation to report, and no interior. The page says so, rather than dividing by zero or refusing the input. The sum is still exact, and both formulas still agree. Only the orientation has no value, and it says so in words instead of picking one.

@chapter Where people slip
@list heading="Common slips" items="Forgetting the closing edge@The first|Taking absolute values inside the sum@The second|Halving as you go@And the third"
The first slip is forgetting the closing edge, from the last vertex back to the first. You get a plausible number that's off by one triangle. The second is taking absolute values inside the sum. The terms are meant to cancel. And the third is halving as you go, which lets a fraction, and then a float, into an exact calculation.

@end text="Twice the area, and its sign"
Type a polygon both ways round and watch the sign flip, on Learn. That's learn dot get er done dot I O.
