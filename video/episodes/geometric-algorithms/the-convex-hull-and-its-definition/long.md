---
format: long
lesson: geometric-algorithms/the-convex-hull-and-its-definition
title: The convex hull, defined without any algorithm
thumb: Define it first, then check
---

@chapter What is a hull?
@title text="The Convex Hull and Its Definition" sub="Geometric Algorithms" art=thumb
Before you trust a convex hull algorithm, you need to know what a hull is, without mentioning any algorithm at all. Then the algorithm becomes a claim you can check.

@art rubber-band
The convex hull of a finite set of points is the smallest convex set that contains them. Picture a rubber band snapped around pins.

@list heading="Three descriptions, one set" items="The smallest convex set containing S@smallest convex set|The intersection of every half-plane containing S@every half plane|All convex combinations of points of S@weighted averages"
There are two other ways to say it. It's the intersection of every half plane that contains all the points. Or it's the set of all weighted averages of them. All three describe the same set. The smallest convex set is for arguing a construction returns the hull. The second turns into a test. The third tells you what not being a corner means.

@chapter Vertices
@art vertex-vs-boundary
A point p is a vertex of the hull when p isn't in the hull of the other points. In other words, p isn't an average of the others. Remove a vertex and the hull changes. Every vertex is on the boundary, but a point can sit in the middle of an edge, on the boundary but not a corner. That only happens with collinear points.

@chapter A finite test
@art separating-line
How do you test that? Here's the key fact. p is a vertex exactly when some line through p has every other point weakly on one side, and every point lying on that line strictly beyond p along it. That second clause is what tells a corner from a point in the middle of an edge.

@art rotating-line
And if such a line exists, you can rotate it about p until it first touches another point, without breaking anything. So you only need to try the n minus one lines through p and each other point. A loop, not a quantifier over every line. The whole test is cubic. Extravagant, and exactly right for a referee that shares no code with what it judges.

@chapter Nine points, four corners
@words text="(0,0) (6,0) (6,6) (0,6)" sub="plus (3,3) (2,1) (4,5) (1,4) (5,2) inside"
The lab opens on a square with corners zero, zero, six, zero, six, six and zero, six, with five more points scattered inside. The definition marks four vertices and four boundary points, and they're the same four. The monotone chain returns those four, gift wrapping returns those four, and the columns agree row by row.

@art inner-collinear
There are collinear triples here, for example zero, zero, then three, three, then six, six. But they all lie strictly inside the hull. What makes a hull input degenerate is collinearity on the boundary, a much narrower condition.

@chapter Two costs
@math heading="Monotone chain on nine points" items="18 pushes + 12 pops = 30@eighteen pushes;;pushes: 2n = 18@two n;;ceiling: 4n = 36@four n"
The chain is a sort plus a linear scan. On these nine points the lab counts eighteen pushes and twelve pops, thirty stack operations. Each chain pushes every point once, so two n, eighteen, pushes. Pops are at most another two n, so the ceiling is four n, thirty six.

@math heading="Gift wrapping" items="n work per vertex  ⟹  n·h@scanning all n;;n·h = 9 · 4 = 36@thirty six comparisons;;n·⌊log₂ n⌋ = 27@twenty seven"
Gift wrapping walks from vertex to vertex, scanning all n points to find each next one. That's n times h, where h is the number of hull points. Here that's thirty six comparisons, and the reference column beside it, n times the floor of log two of n, is twenty seven.

@words text="n·h < n log n  only when  h < log n"
So the output sensitive algorithm did more work here. That's because h is four, and log two of nine is only about three point one seven. Its advantage is a promise about inputs with tiny hulls. Twenty four points with three on the hull give seventy two against ninety six.

@chapter Hulls sort
@art parabola-lift
One last input. Lift the numbers five, one, nine, three, seven onto the parabola, as x and x squared. All five are hull vertices, and the lower chain reads them in sorted order. So any hull algorithm sorts, and the comparison lower bound for sorting applies.

@chapter Where people slip
@list heading="Common slips" items="Defining the hull by its algorithm@The first|Calling interior collinearity degenerate@The second|Trusting an output-sensitive bound blindly@And the third"
The first slip is defining the hull as whatever the algorithm returns, which makes correctness unaskable. The second is calling any collinear triple degenerate, when only the boundary matters. And the third is trusting an output sensitive bound without asking what h is on your data.

@end text="Define it, then check it"
You can type your own points and watch the definition referee two algorithms, on Learn. That's learn dot get er done dot I O.
