---
format: long
lesson: lines-functions-and-graphs/transformations-of-graphs
title: Transformations of graphs: why the inside moves backwards
thumb: Inside goes backwards
---

@chapter The question
@title text="Transformations of Graphs" sub="Lines, Functions and Graphs" art=thumb
Change a formula slightly, and its graph moves. Add five and it goes up five. That's what you'd expect. But replace x with x minus three, and it moves three to the right. Why does the inside go backwards?

@art parent-shift-up
Start with a known graph, y equals f of x. The lesson uses a line, the absolute value of x, and x cubed. Changes outside the function act on the output, and they do exactly what they say.

@chapter Why inside is backwards
@art shift-right
Let g of x equal f of x minus three. Take any point t, f of t on the graph of f. Where does g take that same value? When x minus three equals t, which means x equals t plus three. Same height, input three larger. So every point moves three to the right.

@words text="x − 3 = t  →  x = t + 3"
That one rearrangement is the whole reason horizontal effects are inverted. It works for stretches too. g of x equals f of two x takes the value f of t at x equals t over two, so distances from the vertical axis are halved.

@chapter The four moves
@list heading="Four moves" items="f(x) + k: up k@plus k|a·f(x): stretch by |a|, flip if a < 0@a times|f(x − h): right h@x minus h|f(bx): squash by 1/|b|, flip if b < 0@b x"
f of x plus k shifts up by k. a times f of x stretches vertically, and flips over the horizontal axis if a is negative. f of x minus h shifts right by h, so f of x plus four moves left. And f of b x squashes toward the vertical axis by one over b.

@art squash
That last one catches people. f of two x is half as wide, not twice as wide. The graph reaches at x equals one what the parent reached at x equals two.

@art two-reflections
Keep the two reflections apart. Minus f of x flips the output, turning the picture upside down. f of minus x flips the input, turning it left to right. For f of x equals x plus one, the point zero, one flips to zero, minus one in the first case, and stays put in the second.

@chapter A combined formula
@words text="(x₀, y₀)  →  (x₀/b + h,  a·y₀ + k)"
For a combined formula, move points. A parent point x nought, y nought goes to x nought over b, plus h, and a times y nought, plus k.

@math heading="g(x) = −2|x − 3| + 5" items="(x₀, y₀) → (x₀ + 3, −2y₀ + 5)@point map;;(0, 0) → (3, 5)@corner;;(−1, 1) → (2, 3)@minus one, one;;(1, 1) → (4, 3)@one, one"
Take g of x equals minus two times the absolute value of x minus three, plus five. The point map adds three to x, and takes minus two times y, plus five. The corner zero, zero lands at three, five. Minus one, one lands at two, three. And one, one lands at four, three.

@art vertical-stretch-flip
So the V moves right three and up five, gets twice as steep, and flips upside down. Its corner ends up at three, five.

@art point-map
Check directly: g of three is five, and g of two and g of four are both three. Equal heights on either side confirm the V is symmetric about x equals three. Three points, and the transformed graph is drawn.

@chapter Factor the inside first
@words text="r(x) = f(2x + 6)" sub="the 6 is not the shift"
Now r of x is f of two x plus six, where f is x cubed. The six isn't the shift.

@math heading="r(x) = f(2x + 6),  f(x) = x³" items="f(2(x + 3)):  b = 2, h = −3@Factor it;;(0, 0) → (−3, 0)@zero, zero;;(1, 1) → (−5/2, 1)@one, one;;(−1, −1) → (−7/2, −1)@minus one, minus one"
Factor it: f of two times x plus three. So b is two and h is minus three. Zero, zero goes to minus three, zero. One, one goes to minus five halves, one. Minus one, minus one goes to minus seven halves, minus one.

@art squash
So the graph is half as wide and moved left by three. Reading the six as a shift of six would send zero, zero to minus six, zero, and substituting shows that's wrong. Outside constants act on y, inside constants on x. Mixing those up changes which quantity each one controls.

@chapter Where people slip
@list heading="Common slips" items="Reading x − 3 inside as a shift left@The first|Reading the number beside x as the shift@The second|Calling f(2x) a stretch by 2@the third"
The first slip is reading a subtraction inside as a shift left. Solve x minus three equals t, and the plus three appears. The second is reading the number beside x as the shift, before factoring. And the third is calling f of two x a stretch by two, when it's a squash by a half.

@chapter Try it
@words text="(2, −1) on f,   q(x) = 3f(2(x + 1)) − 4" sub="inside: 2(x + 1) = 2"
Your turn. The point two, minus one is on y equals f of x, and q of x is three f of two times x plus one, minus four. The inside equation is given: two times x plus one equals two. Solve it for the new x, compute the new y, and check by substituting.

@end text="Move a graph yourself"
The full lesson is on Learn. That's learn dot get er done dot I O.
