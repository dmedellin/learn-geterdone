---
format: long
lesson: separable-equations-growth-and-decay/why-separation-works
title: Why separating variables works: it's the chain rule
thumb: The chain rule, read backwards
---

@chapter The question
@title text="Why Separation Works" sub="Separable Equations, Growth and Decay" art=thumb
Separating variables can look like a trick. You integrate y times y prime as though it were the derivative of something. It is, and the reason is a rule you already know.

@chapter The chain rule
@art chain-gears
Here's the chain rule. If y is a function of t, and F is a function of y, then the rate of F of y of t is F prime of y, times y prime. That factor y prime is the rate the inside function moves.

@math heading="Chain rule" items="d/dt G(y(t)) = G′(y)·y′@G of y of t;;= g(y)·y′@g of y times y prime;;d/dt (y²/2) = y·y′@y squared over two"
Now let F be an antiderivative G, so G prime is g. The rate of G of y of t is g of y times y prime. For G of y equals y squared over two, that's y times y prime. So the left side of a separable equation really is a derivative.

@chapter The theorem
@words text="g(y)·y′ = h(t)" sub="exactly when G(y(t)) − H(t) is constant"
Here's the statement. Suppose G prime is g, H prime is h, and y is differentiable on an interval. Then g of y times y prime equals h of t on that interval exactly when G of y of t minus H of t is constant on it.

@math heading="Why" items="d/dt [G(y(t)) − H(t)] = g(y)·y′ − h(t)@the rate of;;= 0  when the equation holds@That's zero;;G(y(t)) − H(t) = C@one number"
By the chain rule, the rate of G of y of t minus H of t is g of y times y prime, minus h of t. That's zero for every t exactly when the equation holds. A function whose rate is zero on an interval doesn't change, so the difference is C, one number.

@art flat-difference
So the relation isn't a heuristic. Along a solution it holds with some constant. And the proof runs the other way too: a differentiable y that satisfies the relation satisfies the equation. That second direction is what a check uses.

@chapter Checking a solution
@math heading="y²/2 = t²/2 + 2" items="left side → y·y′@the left side gives;;right side → t@the right side gives;;y·y′ = t@the equation we started with"
Take the relation y squared over two equals t squared over two, plus two. Differentiate both sides with respect to t, remembering that y depends on t. By the chain rule the left side gives y times y prime. The right side gives t. So y times y prime equals t, the equation we started with.

@math heading="y = √(t² + 4)" items="y′ = t/√(t² + 4)@y prime is;;y·y′ = √(t² + 4) · t/√(t² + 4) = t@multiply by y"
The explicit form checks the same way, with one more use of the chain rule for the square root. y prime is t over the square root of t squared plus four. Multiply by y, the square roots cancel, and you get t.

@art round-trip
Whenever this course reports a solution, this is the test: differentiate it and compare. It needs no knowledge of how the answer was found.

@chapter Two more checks
@math heading="Two more" items="−1/y = t²/2 − 1  →  y′/y² = t@minus one over y;;y³ = t² + t + 1  →  3y²·y′ = 2t + 1@y cubed"
For minus one over y equals t squared over two, minus one, the derivative of minus one over y is y prime over y squared, and the right side gives t. That's the equation back. For y cubed equals t squared plus t plus one, the left gives three y squared times y prime, the right gives two t plus one. No cube root needed.

@art tangent-match
Each time, the factor y prime shows up on the left. That's the test of whether you have the idea: differentiate your own answer and find y prime in it.

@chapter About dy and dt
@words text="dy/dt means y′" sub="one symbol, not a fraction"
You'll often see this written as the integral of g d y equals the integral of h d t. That's a convenient record of the result. But here, d y over d t is one symbol for y prime. Nothing gets cancelled. The chain rule is doing the work, whether or not you ever write a differential.

@chapter Where people slip
@list heading="Common slips" items="Thinking dy and dt were cancelled@The first|Dropping the factor y′@The second|Trusting the derivative check for C@The third"
The first slip is thinking d y and d t were cancelled, so the method is a trick. It works because y times y prime is the derivative of y squared over two. The second is dropping the factor y prime. The third is trusting the derivative check to catch a wrong constant.

@art missing-factor
The derivative of y squared with respect to t is two y times y prime, not two y. Without that factor, the check shows a mismatch for every example.

@art two-tests
And the constant differentiates to zero, so a wrong C passes every derivative check. A solution needs two tests. The derivative gives the equation back, and the starting point satisfies the relation.

@chapter Try it
@words text="y³ = t² + t + 1" sub="differentiate, then check y(0) = 1"
Your turn. Differentiate y cubed equals t squared plus t plus one with respect to t, and find the factor y prime. Then put t equals zero and y equals one back in, to check the constant too.

@end text="Differentiate it and compare"
The lab's check view differentiates each answer line by line, on Learn. That's learn dot get er done dot I O.
