---
format: long
lesson: lines-functions-and-graphs/what-a-function-is
title: What a function is: exactly one output for each input
thumb: Exactly one output
---

@chapter The definition
@title text="What a Function Is" sub="Lines, Functions and Graphs" art=thumb
A function sounds like a big idea. The definition is one sentence long, and the word that does all the work is exactly.

@art input-machine
A function is a rule that assigns to each input exactly one output. The set of inputs is the domain. The outputs it produces form the range.

@words text="each · exactly one"
Every word counts. Each means there's no input the rule can't handle. Exactly one means no input gets two answers. Fail either, and it isn't a function. Later lessons depend on this. Function notation assumes f of three names a single number.

@chapter What's allowed
@art many-to-one
Here's the part that surprises people. Outputs may repeat. Inputs may not. Lots of inputs sharing one output is ordinary and useful.

@math heading="f(x) = x²" items="3  →  9@three goes to nine;;−3  →  9@minus three;;two inputs, one output: a function@a function"
Take f of x equals x squared. Three goes to nine. Minus three also goes to nine. Two inputs share one output, and that's completely fine. It's a function.

@art one-to-many
The reverse is the problem. If one input has two outputs, then the output of that input doesn't exist. There are two candidates, and the rule doesn't say which.

@math heading="x² + y² = 25" items="x = 3  →  y = 4 and y = −4@x equals three;;x = 0  →  y = 5 and y = −5@x equals zero;;one input, two outputs: not a function@not a function"
Take the circle, x squared plus y squared equals twenty five. When x equals three, y is four and also minus four. When x equals zero, y is five and minus five. That's not a function. It's a fine curve. It just isn't a function of x.

@chapter The vertical line test
@art circle-vertical
On a graph you can check the whole condition by eye. A graph is a function of x if no vertical line meets it more than once. A vertical line is all the points with one fixed x, so two crossings mean one input with two outputs.

@art parabola-vertical
Now try y equals x squared. Wherever you put a vertical line, it crosses the curve exactly once. Every input gets one output, so it passes.

@art vertical-line-graph
Remember x equals five? Its graph is itself a vertical line, so a vertical line test meets it infinitely often. The input five gets every number as an output. That's the same exception that blocked slope, and slope intercept form, now explained.

@chapter Other representations
@list heading="How to check" items="Table: a repeated input with different outputs@A table|Pairs: same first coordinate, different second@a set of pairs|Equation: does solving for y force a ±?@an equation|Graph: the vertical line test@a graph"
For a table, look for a repeated input with different outputs. A repeated output doesn't matter. For a set of pairs, it's the same test on first coordinates. For an equation, try solving for y. If you're forced into a plus or minus, it's not a function. And for a graph, use the vertical line test.

@math heading="Six rules" items="y = 2x + 1   function@two x plus one;;y = x²   function@x squared;;y = |x|   function@absolute value;;y² = x   not: x = 4 gives 2 and −2@y squared equals x;;x = 5   not: every y at once@x equals five;;x² + y² = 25   not: x = 3 gives 4 and −4@twenty five"
Six rules. y equals two x plus one: function. y equals x squared: function. y equals the absolute value of x: function, since minus seven and seven both give seven. y squared equals x: not, because four gives two and minus two. x equals five: not. And x squared plus y squared equals twenty five: not.

@math heading="Two tables" items="x: 1 2 3 2 · y: 5 7 9 8  →  not a function@two appears twice;;x: 1 2 3 4 · y: 5 5 5 5  →  function@every output is five"
Tables work the same way. In the first, the input two appears twice, once with seven and once with eight. Not a function. In the second, every output is five. That looks suspicious, but each input appears once, so it's a function.

@words text="a function of x" sub="x = 5 fails for x, but works as a function of y"
One caution. The test always depends on which variable is the input. x equals five fails as a function of x, but it's a perfectly good function of y. The vertical line test assumes x goes across and y goes up.

@chapter Where people slip
@list heading="Common slips" items="Thinking repeated outputs break it@The first|Using the horizontal line test@The second|Saying not a function without a witness@The third"
The first slip is thinking repeated outputs break the definition. They don't. The second is using a horizontal line test. That tells you whether a function is one to one, a real property for inverses, but not whether it's a function. The third is answering not a function without naming the input that breaks it.

@chapter Try it
@words text="(−2, 1)  (0, 3)  (2, 1)  (0, 4)" sub="group by first coordinate"
Here's one to try. The pairs minus two, one, then zero, three, then two, one, then zero, four. Group them by first coordinate. Give the verdict, and name the exact input and two outputs that witness it. Then remove one pair so what's left is a function.

@end text="Test a graph yourself"
The full lesson is on Learn. That's learn dot get er done dot I O.
