---
format: long
lesson: lines-functions-and-graphs/composition-of-functions
title: Composition of functions: f after g
thumb: f after g, so g first
---

@chapter The idea
@title text="Composition of Functions" sub="Lines, Functions and Graphs" art=thumb
What happens when you feed the output of one function straight into another? You get a new function, a composite. The only hard part is the order, because the notation reads backwards.

@art two-machines
f circle g of x means f of g of x. g runs first, on x, and then f runs on whatever g produced. Its domain is the inputs that suit g, and whose output then suits f.

@words text="f ∘ g  =  f after g"
Read the circle as after. f circle g is f after g. Saying it that way out loud puts the order back where it belongs: g happens, then f happens to the result.

@chapter Computing a composite
@math heading="f(x) = 2x + 3,  g(x) = x − 4" items="(f ∘ g)(x) = f(x − 4)@f after g;;= 2(x − 4) + 3@two times;;= 2x − 5@two x minus five"
Take f of x equals two x plus three, and g of x equals x minus four. f after g is f of x minus four. Put x minus four into f's slot: two times x minus four, plus three. That's two x minus eight plus three, so two x minus five.

@math heading="the other order" items="(g ∘ f)(x) = g(2x + 3)@g after f;;= (2x + 3) − 4@minus four;;= 2x − 1@two x minus one"
Now g after f. That's g of two x plus three, which is two x plus three, minus four. So two x minus one. Both are lines, and they're different functions.

@art step-by-step
Check at x equals two, one step at a time. g of two is minus two, and f of minus two is minus one. That matches two x minus five. The other way, f of two is seven, and g of seven is three. That matches two x minus one. Do this check every time.

@art order-swap
So order changes the answer. At two, one order gives minus one and the other gives three. Composition isn't commutative, even when everything involved is a line.

@chapter The domain of a composite
@art domain-gate
The domain is decided in two stages. The input has to be legal for the inner function. Then the inner function's output has to be legal for the outer one.

@math heading="f(x) = √x,  g(x) = x − 5" items="(f ∘ g)(x) = √(x − 5)  →  [5, ∞)@root of x minus five;;(g ∘ f)(x) = √x − 5  →  [0, ∞)@g after f is;;x = 9:  √(9 − 5) = 2   √9 − 5 = −2@nine"
Let f be the square root and g be x minus five. f after g is the root of x minus five, which needs x at least five. g after f is the root of x, minus five, which only needs x at least zero. And at nine, one gives two and the other gives minus two.

@chapter The trap
@math heading="f(x) = x²,  g(x) = √x" items="(f ∘ g)(x) = (√x)² = x@simplifies to x;;stage 1: √x needs x ≥ 0@stage one;;domain [0, ∞), even though the formula is x@even though"
Here's the trap. Take f of x equals x squared, and g of x equals the square root of x. f after g is root x, squared, which simplifies to x. But stage one still applies: root x needs x at least zero. So the domain is zero to infinity, even though the final formula is just x.

@art hidden-restriction
The simplified x looks happy at minus one. But g of minus one isn't a real number, so f is never reached. Find the domain before you simplify, and carry it beside the simplified rule. In the other order, the root of x squared is the absolute value of x, defined for every real x.

@chapter Where people slip
@list heading="Common slips" items="Composing in the written order@The first|Treating the circle as multiplication@The second|Reading the domain off the simplified formula@the third"
The first slip is composing in the written order. g goes first, even though f is written first. The second is treating the circle as multiplication. And the third is reading the domain off the simplified formula.

@art ring-vs-dot
With f of x equals three x minus one, and g of x equals x plus two, f circle g of one is eight. But f of one times g of one is six. A small ring, a small dot, and completely different meanings.

@chapter Try it
@words text="u(x) = 3x − 1,   v(x) = x + 2" sub="(u ∘ v)(x) = u(x + 2)"
Your turn. Take u of x equals three x minus one, and v of x equals x plus two. The first line is given: u after v is u of x plus two. Finish both orders, find each domain, and run minus one through each chain before checking the two formulas.

@end text="Compose them yourself"
The full lesson is on Learn. That's learn dot get er done dot I O.
