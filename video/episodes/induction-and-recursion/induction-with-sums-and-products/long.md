---
format: long
lesson: induction-and-recursion/induction-with-sums-and-products
title: Proving sum formulas by induction: peel, substitute, factor
thumb: Write the target first
---

@chapter One shape for every sum
@title text="Induction with Sums and Products" sub="Induction and Recursion" art=thumb
Sums of integers, squares, cubes, geometric series. Proving their formulas by induction can look like a different puzzle each time. It isn't. Every one of these proofs has the same shape, and once you see it they become routine.

@words text="Σᵢ₌₁ⁿ f(i) = f(1) + f(2) + ⋯ + f(n)" sub="empty sum = 0,  empty product = 1"
First, the notation. Sigma from i equals one to n of f of i means f of one, plus f of two, and so on up to f of n. When the upper limit is below the lower one, the sum is empty and equals zero. Products use a capital pi, and an empty product is one.

@chapter Peel, substitute, factor
@art peel-last
Here's the shape. The sum up to k plus one is the sum up to k, plus one more term. Peel that last term off, and the hypothesis now applies to everything else.

@list heading="The step" items="Write the claim at k+1@write down|Peel off the last term@peel off|Substitute the hypothesis@substitute|Factor toward the target@factor"
So: first write down the claim at k plus one, so you know what you're aiming at. Then peel off the last term. Substitute the hypothesis for the sum up to k. From there it's algebra with no sums in it: factor toward the target.

@chapter Sum of squares
@math heading="1² + 2² + ⋯ + n² = n(n+1)(2n+1)/6" items="n = 1:  1 = 1 · 2 · 3 / 6@one times two;;Σᵢ≤ₖ₊₁ i² = k(k+1)(2k+1)/6 + (k+1)²@plus k plus one squared"
Let's do the sum of squares, which is n times n plus one times two n plus one, over six. At n equals one, the left is one, and the right is one times two times three over six, also one. For the step, the sum up to k plus one is the formula at k, plus k plus one squared.

@math items="= (k+1)[k(2k+1) + 6(k+1)]/6@Take out;;= (k+1)(2k² + 7k + 6)/6@seven k;;= (k+1)(k+2)(2k+3)/6@k plus two"
Take out the common factor, k plus one. Inside, you get two k squared plus seven k plus six. That factors as k plus two, times two k plus three. And that's the claim at k plus one.

@art square-pyramid
That factoring is the only clever moment, and you find it by knowing the target. The claim at k plus one has to contain k plus two, so k plus two is what you look for.

@chapter Geometric series
@math heading="a + ar + ⋯ + arⁿ = a(rⁿ⁺¹ − 1)/(r − 1)" items="n = 0:  a(r − 1)/(r − 1) = a@At n equals zero;;r ≠ 1@not decoration"
The geometric series works the same way. At n equals zero, the left is a and the right is a times r minus one, over r minus one, which is a. And the condition that r isn't one is not decoration.

@art geometric-bars
At r equals one, the denominator vanishes, and the sum is simply a times n plus one. Every hypothesis in a theorem is doing work somewhere, and finding where is a good habit.

@chapter Sums that collapse
@math heading="Σ 1/(i(i+1))" items="1/(i(i+1)) = 1/i − 1/(i+1)@one over i minus;;(1 − 1/2) + (1/2 − 1/3) + ⋯ + (1/n − 1/(n+1))@one minus a half;;= 1 − 1/(n+1) = n/(n+1)@n over n plus one"
Some sums need no induction at all. One over i times i plus one is one over i minus one over i plus one. So the sum is one minus a half, plus a half minus a third, and so on. Everything cancels except one minus one over n plus one, which is n over n plus one.

@art telescope
That's a telescoping sum. Every middle term appears once with a plus and once with a minus, and the whole thing collapses.

@art pairing-reversal
Gauss's trick for one plus two up to n is another route: add the sum to its own reversal and you get n copies of n plus one. Induction verifies a formula you already have. Arguments like these produce one.

@chapter Products
@words text="Πᵢ₌₂ⁿ (1 − 1/i²) = (n+1)/(2n)" sub="n = 2:  1 − 1/4 = 3/4 = 3/(2 · 2)"
Products behave exactly like sums. The product to k plus one is the product to k, times one more factor. Here, at n equals two, both sides are three quarters. In the step you peel off the last factor and look for k plus two, which comes from a difference of two squares.

@art cancel-pairs
Written out, the product cancels just like the telescoping sum, down to n plus one over two n. That's a check on the answer, not the proof of it.

@chapter Where people slip
@list heading="Common slips" items="Not writing the target first@the target|Peeling the wrong term@wrong term|Using the wrong base case@base case"
Three slips. Doing the algebra without writing the target first turns the step into trial and error. Peeling off the wrong term, the first instead of the last, leaves a sum the hypothesis doesn't describe. And a formula claimed from n equals zero needs its base case checked at zero, not at one.

@chapter Try it
@math heading="Σᵢ₌₁ⁿ i · i! = (n+1)! − 1" items="n = 1:  1 · 1! = 1 = 2! − 1@one times one factorial;;[(k+1)! − 1] + (k+1)(k+1)!@peel off;;= (k+1)! · (k+2) − 1 = (k+2)! − 1@factor out"
Now try one that's less familiar: the sum of i times i factorial equals n plus one factorial, minus one. At n equals one, one times one factorial is one, and two factorial minus one is one. Peel off the last term and substitute. Then factor out k plus one factorial, and recognise what's left.

@end text="Check the identities yourself"
You can watch the sum of cubes match the square of the sum, row by row, on Learn. That's learn dot get er done dot I O.
