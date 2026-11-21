---
format: long
lesson: lines-functions-and-graphs/piecewise-functions
title: Piecewise functions: read the condition first
thumb: Condition first, then formula
---

@chapter The idea
@title text="Piecewise Functions" sub="Lines, Functions and Graphs" art=thumb
Some functions need more than one formula. One rule for small inputs, another for large ones. That's still one function, as long as the conditions decide which formula applies, and no input gets two different answers.

@art three-pieces
A piecewise function splits its domain into pieces and gives a formula for each. The cleanest way is with conditions that don't overlap, so each input picks exactly one piece.

@chapter One you already know
@art abs-v
You've met one already: absolute value. The absolute value of x is x when x is at least zero, and minus x when x is negative. Two formulas and a condition.

@math heading="|x|" items="|−7| = −(−7) = 7@minus seven;;|7| = 7@seven is just seven"
For minus seven, the condition picks the second line, so it's minus minus seven, which is seven. And seven is just seven. Notice that minus x gives positive outputs, because the minus is applied to an input that's already negative.

@chapter A three-piece function
@words text="−x − 1 if x < −1  ·  x² if −1 ≤ x < 2  ·  8 − 2x if x ≥ 2"
Here's the lesson's function. Minus x minus one below minus one. x squared from minus one up to, but not including, two. And eight minus two x from two upward. Together, the conditions cover every real number exactly once.

@math heading="Read the condition first" items="f(−3) = −(−3) − 1 = 2@Minus three is below;;f(−1) = (−1)² = 1@Minus one is in the middle;;f(0) = 0² = 0@At zero;;f(2) = 8 − 2(2) = 4@Two is in the last;;f(5) = 8 − 2(5) = −2@at five"
Evaluate by checking the condition first. Minus three is below minus one, so f of minus three is two. Minus one is in the middle piece, so it's one. At zero it's zero. Two is in the last piece, so it's four. And at five, it's minus two.

@math heading="the wrong branch" items="✗  8 − 2(−1) = 10@wrong formula"
Now the error this lesson exists to prevent. Put minus one into the wrong formula, eight minus two x, and you get ten. It's a real number from a real formula, and it looks fine. But it isn't f of minus one, because the condition x is at least two rules that piece out.

@chapter What happens at a join
@art step-join
At minus one, the neighbours disagree. Coming from the left, minus x minus one heads toward zero. But the value there is minus one squared, which is one. So the graph steps up by one, with an open circle at minus one, zero and a filled circle at minus one, one.

@art smooth-join
At two, they agree. x squared heads toward four, and eight minus two times two is four. The pieces meet, with no break and no circles. Whether a join steps or connects is settled by arithmetic, not by how the formulas look.

@chapter Endpoints
@list heading="The dots" items="Filled circle: a point the function attains@A filled circle|Open circle: approached, not included@An open circle|Never two filled circles above one input@never"
A filled circle marks a point the function actually takes. An open circle marks a point the graph approaches but doesn't include. And you can never have two different filled circles above one input.

@art stacked-dots
That would be two outputs for one input, and the vertical line test rules it out on sight.

@math heading="One symbol apart" items="x + 1 if x ≤ 3 · 2x if x ≥ 3  →  not a function@not a function;;x + 1 if x < 3 · 2x if x > 3  →  domain omits 3@omits three;;x + 1 if x ≤ 3 · 2x if x > 3  →  every real number@every real number"
Three rules, one symbol apart. x plus one if x is at most three, two x if x is at least three: at three, they say four and six, so it's not a function. With strict signs on both, it's a function whose domain omits three. And with exactly one included endpoint, it works on every real number.

@art gap-point
So a gap is legal. It just shrinks the domain. Only an overlap with disagreeing values breaks the definition.

@chapter Where people slip
@list heading="Common slips" items="Evaluating first, checking the condition after@The first|Both endpoint conditions non-strict@The second|Assuming every join is a break@the third"
The first slip is evaluating first and checking the condition afterwards. The second is writing both endpoint conditions with a non strict sign. And the third is assuming a join must be a break, when two formulas can meet.

@chapter Try it
@words text="2x + 1 if x < 0  ·  x² + 1 if 0 ≤ x < 3  ·  7 − x if x ≥ 3"
Try g of x: two x plus one for x below zero, x squared plus one from zero up to three, and seven minus x from three on. Evaluate at minus two, zero and three. Compute both formulas at each join, draw the endpoints, and say which join connects and which jumps.

@end text="Evaluate it yourself"
The full lesson is on Learn. That's learn dot get er done dot I O.
