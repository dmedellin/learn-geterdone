---
format: long
lesson: lines-functions-and-graphs/function-notation
title: Function notation: f(x) is a value, not a product
thumb: f(x) is not f times x
---

@chapter The notation
@title text="Function Notation" sub="Lines, Functions and Graphs" art=thumb
f of x looks like f times x. It isn't. Getting that one thing straight clears up most of the mistakes in this part of algebra.

@art name-and-slot
f of x names the output that the function f gives for the input x. It's one number. f is the name of the rule, and x is a slot where the input goes.

@words text="f(x) = 2x + 1   g(t) = 2t + 1   h(u) = 2u + 1" sub="three names, one function"
The letters are arbitrary. f of x equals two x plus one, g of t equals two t plus one, and h of u equals two u plus one are three names for one function.

@words text="Nothing in f(x) is multiplied"
The brackets look like multiplication brackets, but that's an accident of history, not a hint. The notation is roughly three hundred years old, so the ambiguity is permanent. The only defence is reading the whole symbol as one name.

@chapter Evaluating at a number
@math heading="f(x) = x² − 4x + 5" items="f(3) = (3)² − 4(3) + 5 = 9 − 12 + 5 = 2@f of three;;f(0) = (0)² − 4(0) + 5 = 5@f of zero;;f(−2) = (−2)² − 4(−2) + 5 = 4 + 8 + 5 = 17@f of minus two"
Take f of x equals x squared minus four x plus five. To evaluate, replace every x with the input in brackets, then simplify. f of three is nine minus twelve plus five, which is two. f of zero is five. And f of minus two is four plus eight plus five, seventeen.

@math heading="without brackets" items="✗  −2² − 4·2 + 5 = −4 − 8 + 5 = −7@leave out the brackets"
That last one is where brackets earn their place. Leave out the brackets and minus two squared reads as minus four, and the second term as minus eight. You get minus seven instead of seventeen. And nothing looks wrong.

@chapter Evaluating at an expression
@art expression-in-slot
The slot accepts anything, including a whole expression. The procedure doesn't change. Replace every x with the expression in brackets, expand, and collect.

@math heading="f(a + 1)" items="(a + 1)² − 4(a + 1) + 5@a plus one, squared;;a² + 2a + 1 − 4a − 4 + 5@expand;;a² − 2a + 2@collect;;check a = 2:  f(3) = 2,  4 − 4 + 2 = 2  ✓@check"
So f of a plus one is a plus one, squared, minus four times a plus one, plus five. Expand, and collect, and you get a squared minus two a plus two. Check with a equals two: f of three is two, and four minus four plus two is also two.

@art not-distribute
Now compare f of a, plus f of one. That's a squared minus four a plus seven, a different expression. They agree only when a is five halves. A function doesn't distribute over addition.

@words text="f(1 + 1) = 5    f(1) + f(1) = 6" sub="f(x) = 2x + 1"
The mistake survives because it does work for f of x equals c x, the first kind you meet. But a constant term is enough to break it. Take f of x equals two x plus one. f of one plus one is five, but f of one plus f of one is six.

@chapter Two different questions
@art evaluate-vs-solve
There are two questions, and they go in opposite directions. Evaluate means you're given an input and asked for the output. Solve means you're given an output and asked which inputs produce it.

@math heading="g(x) = 3x − 7,  solve g(x) = 5" items="3x − 7 = 5@three x minus seven;;3x = 12@twelve;;x = 4@x is four;;check:  g(4) = 3(4) − 7 = 5  ✓@check"
Solve g of x equals five, where g of x is three x minus seven. That's three x minus seven equals five. So three x is twelve, and x is four. Check: g of four is twelve minus seven, five. The answer is an input, not the five you started with.

@art graph-read-up
On a graph, a point three, two means f of three equals two, because the graph is the set of input, output pairs. To find f of three, read up from three on the horizontal axis.

@art graph-read-across
To solve f of x equals two, read across from two and collect every x beneath. That can give several answers, or none.

@chapter Where people slip
@list heading="Common slips" items="Reading f(x) as f times x@The first|Substituting a negative without brackets@The second|Answering the other question@the third"
The first slip is reading f of x as f times x. The second is substituting a negative without brackets. And the third is answering the other question. The giveaway is the shape of the answer. Evaluating gives one number. Solving gives a set, which might be empty.

@chapter Try it
@words text="p(t) = t² + 3t − 1" sub="p(−2) = (−2)² + 3(−2) − 1"
Try this. Let p of t be t squared plus three t minus one. The substitution for p of minus two is set up for you. Simplify it, and check the sign of each term. Then form p of a minus one, and separately solve four x plus three equals nineteen.

@end text="Evaluate and solve"
The full lesson is on Learn. That's learn dot get er done dot I O.
