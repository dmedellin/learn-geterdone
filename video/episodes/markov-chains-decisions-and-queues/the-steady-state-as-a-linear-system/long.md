---
format: long
lesson: markov-chains-decisions-and-queues/the-steady-state-as-a-linear-system
title: The steady state is a linear system, not a limit
thumb: Solve it, don't wait for it
---

@chapter What a steady state is
@title text="The Steady State as a Linear System" sub="Markov Chains, Decisions and Queues" art=thumb
Most people think a steady state is where a chain ends up if you run it long enough. That's not the definition, and on one simple chain, it isn't even true.

@math heading="Stationary distribution" items="πP = π@pi P equals pi;;πᵢ ≥ 0,  Σπᵢ = 1@add to one"
A distribution pi is stationary when pi P equals pi. One step of the chain leaves it unchanged. Its entries are non negative and add to one. Nothing here mentions a starting point, a number of steps, or a limit.

@art balance-flow
Read as a linear system, it's one equation per state, saying the probability flowing into that state equals the probability flowing out.

@chapter One equation too many
@words text="Every column of P − I sums to 0"
But there's a catch. Every row of P sums to one, so in P minus I, every row sums to zero. That means the equations add up to zero equals zero. One of them is implied by the others.

@art dropped-row
So as written, the system only fixes pi up to a multiple, and zero satisfies all of it. The fix: drop one equation, by name, and put the sum of pi equals one in its place. That's the one fact pi P equals pi never contained.

@chapter The solve
@art three-brands
Here's the lesson's three brand chain. Row one is seven tenths, two tenths, one tenth. Row two, three, five and two tenths. Row three, one, three and six tenths.

@math heading="Drop state 3's balance" items="7/10 π₁ + 3/10 π₂ + 1/10 π₃ = π₁@state one;;2/10 π₁ + 5/10 π₂ + 3/10 π₃ = π₂@state two;;π₁ + π₂ + π₃ = 1@in its place;;π = (7/17, 11/34, 9/34)@seven seventeenths"
Notice each equation reads down a column of P. Keep the balance at state one and state two. Drop state three, and put the sum equals one in its place. Exact elimination gives seven seventeenths, eleven thirty fourths and nine thirty fourths.

@words text="πP − π = 0, exactly" sub="no tolerance"
Then check it. Recompute pi P from that vector, and every entry is exactly equal, as fractions, not within a tolerance. And it sums to one. Whichever equation you drop, the answer doesn't move.

@chapter Waiting instead
@art error-floor
Now the thing people think a steady state is: multiply again and again, in floating point. After one step the worst error is about point two nine. After twenty, about two times ten to the minus six. After sixty, about ten to the minus sixteen. And after four hundred, no better. It ran out of double, not out of steps.

@chapter No limit at all
@art cycle-no-limit
Now the three cycle. It's irreducible, so the system has exactly one solution, a third, a third, a third, and pi P minus pi is exactly zero. But P cubed is exactly the identity. The powers repeat forever, and the distance from pi is exactly two thirds at every single step.

@words text="A steady state that is not a limit"
That's not slow convergence. It's no convergence. The steady state isn't the limit of anything here. It's the solution of three equations, which exists and is unique whether or not any limit does.

@chapter No unique answer
@art family-of-solutions
And the two closed group chain? The reduced system has rank three, against four unknowns, so the lab prints nothing. Not for lack of answers: there are infinitely many.

@math heading="All stationary" items="(1/2, 1/2, 0, 0)@one half;;(0, 0, 3/11, 8/11)@three elevenths;;(1/4, 1/4, 3/22, 4/11)@a mixture"
One half, one half, zero, zero is stationary. So is zero, zero, three elevenths, eight elevenths. And so is a mixture, like a quarter, a quarter, three twenty seconds, four elevenths. Choosing one would be choosing.

@chapter Where people slip
@list heading="Common slips" items="Solving the transposed system@The first|Not replacing a dependent equation@The second|Quoting the power iteration as the answer@And the third"
The first slip is solving the transposed system, reading rows instead of columns. The second is solving all n equations without replacing one, which gives zero or a family. And the third is quoting a power iteration as the steady state. Compute pi, and use the iteration as the thing you compare against.

@chapter Try it
@words text="1/2 1/2 ; 1/4 3/4"
Your turn. Solve the fine and wet chain from earlier. Write both balance equations, drop one, add the sum to one, and solve exactly. Then recompute pi P and check it's exactly pi.

@end text="Solve it, then check it"
You can choose which equation to drop and watch the exact answer not move, on Learn. That's learn dot get er done dot I O.
