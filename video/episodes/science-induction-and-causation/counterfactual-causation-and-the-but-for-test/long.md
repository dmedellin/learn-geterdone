---
format: long
lesson: science-induction-and-causation/counterfactual-causation-and-the-but-for-test
title: The but-for test: flip the cause, recompute, and see
thumb: Flip it, recompute, compare
---

@chapter A fire
@title text="Counterfactual Causation and the But-For Test" sub="Science, Induction and Causation" art=thumb
What does it mean to say one thing caused another? One old answer: had the cause not happened, the effect wouldn't have either. Here's how to make that exact.

@art match-and-oxygen
A fire starts when a match is struck in a room with oxygen. Write S for the match is struck, and O for oxygen is present, each one if true and zero if false. These are inputs: nothing in the model determines them. And write F for the fire.

@math heading="A structural model" items="S = 1@S equals one;;O = 1@O equals one;;F = S ∧ O@F equals S and O"
S equals one. O equals one. And F equals S and O. That's a structural model. It lists the inputs with their actual values, and gives every other variable an equation in terms of the variables it depends on. The equations mustn't loop.

@chapter Flip and recompute
@math heading="Flip the strike" items="actual:  F = 1 ∧ 1 = 1@one and one;;flip S to 0:  F = 0 ∧ 1 = 0@zero and one"
Solve the equations, and F is one and one, which is one. Now ask the counterfactual question. Set S to zero, and recompute. F is zero and one, which is zero. The fire doesn't happen. So the strike is a but for cause.

@art flip-switch
Notice what the flip does. The flipped variable ignores its own equation and just takes the other value. Everything else keeps its equation, and gets recomputed from there.

@words text="The but-for test" sub="flip C, keep the inputs, recompute: does E change?"
Here's the test. A variable C is a but for cause of an effect E when flipping C, leaving every input at its actual value, and recomputing each variable that depends on C, changes the value of E.

@chapter Cause or condition?
@math heading="Flip the oxygen" items="flip O to 0:  F = 1 ∧ 0 = 0@one and zero"
Do the same for oxygen. Set O to zero, and F is one and zero, which is zero. So oxygen is a but for cause too.

@art symmetric-equation
Ordinary speech would call the strike the cause, and the oxygen a condition. But the equation contains no such difference. F equals S and O is symmetric in the two. Whatever separates a cause from a background condition, what's unusual, controllable or of interest, the test doesn't decide it.

@chapter Chains
@art causal-chain
Now a chain. A makes B happen, and B makes C happen: B equals A, C equals B, with A equal to one. Flip A, and B goes to zero, and then C goes to zero. So A is a but for cause of C, even though it acts only through B.

@words text="Follow the flip downstream."
That's why recomputing is required. A glance at the last equation isn't enough, because C's equation mentions only B. The test follows the dependency all the way downstream.

@chapter The model is a premise
@art pilot-light
What the test computes is only as good as the equations. Suppose the model leaves out a second source of fire, a pilot light that's on. Add it as another route to the fire, and flipping the strike no longer changes anything. No step of the computation could notice what the model left out.

@chapter Hume's second definition
@art hume-counterfactual
Hume added, almost in passing, a second definition of a cause: had the first object not been, the second would never have existed. The but for test is that counterfactual, with had not been replaced by a flip and a recomputation. It's exact for the model. And it has a famous failure, where an event is plainly a cause and the flip leaves the effect unchanged. That's the next lesson.

@chapter Where people slip
@list heading="Common slips" items="Expecting the test to separate cause from condition@The first|Applying it only to the nearest variable@The second|Treating a verdict as a fact about the world@the third"
The first slip is expecting the test to separate a cause from a background condition. It can't. If you want to say only the strike is the cause, you're relying on something outside the model, which is allowed, but should be said. The second is applying the test only to the nearest variable. And the third is treating a verdict as a fact about the world, rather than the model.

@chapter Try it
@list heading="Four steps" items="List the variables and inputs@List the variables|Write one equation for each other variable@Write one equation|Solve for the actual values@Solve|Flip the candidate and recompute@Flip the candidate"
Here's one to try, on any situation you can describe in a few variables. List the variables and the inputs. Write one equation for each other variable. Solve for the actual values, and check the effect comes out as it did. Then flip the candidate and recompute.

@end text="Flip the cause and recompute"
You can build your own models and flip any variable, on Learn. That's learn dot get er done dot I O.
