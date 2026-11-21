---
format: long
lesson: randomised-algorithms/the-probabilistic-method
title: The probabilistic method: proving something exists without finding it
thumb: The average proves it exists
---

@chapter Existence from an average
@title text="The Probabilistic Method" sub="Randomised Algorithms" art=thumb
Here's a strange kind of proof. To show a good object exists, pick one at random, and show it's good on average. You've proved existence, and you haven't found it.

@chapter MAX-3-SAT
@art clauses
A three C N F formula is m clauses joined by and. Each clause is an or of three literals, where a literal is a variable or its negation. Max three sat asks for the assignment of true and false that satisfies as many clauses as possible.

@chapter Seven of eight
@art eight-cube
Take one clause on three distinct variables, like x one or x two or not x three. Its three variables have eight possible settings. Exactly one of them makes the clause false: the one that sets every literal against itself. So a random assignment satisfies it with probability seven eighths, whatever the signs.

@math heading="Linearity over clauses" items="E[Z_j] = 7/8@seven eighths;;E[Z] = Σ E[Z_j] = 7m/8@seven m over eight"
Let Z j be one if clause j is satisfied. The expectation of each is seven eighths. Add them up by linearity, and the expected number satisfied is seven m over eight.

@art shared-variables
The clauses can share variables heavily, so these indicators are strongly dependent. Linearity doesn't care. That's why the argument is two lines, and not a long inclusion exclusion.

@chapter So one exists
@art exists-arrow
Now the step that gives the method its name. You put a distribution on the objects, show the property holds on average, and conclude that some object has it.

@words text="some value ≥ the average" sub="⟹ an assignment with ≥ ⌈7m/8⌉ clauses"
A random variable can't always be strictly below its own average. So some assignment satisfies at least seven m over eight clauses, and since that's a whole number, at least the ceiling of it. That's a complete proof, and it names no assignment at all. Finding one is a different problem.

@chapter Four clauses
@math heading="Four clauses on x₁, x₂, x₃" items="mean = 4 × 7/8 = 7/2@four times seven eighths;;4 assignments satisfy 3,  4 satisfy 4@four of them;;mean of those = 7/2@exactly"
The lab's formula has four clauses on three variables. So the mean is four times seven eighths, seven halves. Enumerating all eight assignments confirms it: four of them satisfy three clauses, and four satisfy all four. The mean of those is seven halves, exactly.

@art average-line
The clause table on the panel performs that proof. Each row computes its own clause's share, and the last row checks the total against the mean over every assignment. Two independent routes to one number, and they agree.

@list heading="What the mean doesn't say" items="That a run satisfies 7/2 clauses@a run satisfies|That most runs reach the mean@most runs|That the best is near the mean@the best"
Now, what it doesn't say. It doesn't say a run satisfies seven halves of a clause. It doesn't say most runs reach the mean. Here, half the assignments are below it. And it doesn't say the best is near the mean.

@words text="120 seeds: mean 139/40 = 3.475" sub="every run landed on 3 or 4"
The measured column makes that concrete. Over a hundred and twenty seeded coin flips, the mean came out three point four seven five, against an expectation of three point five. Close, and not the expectation. And it's an average of whole numbers, none of which is three and a half.

@chapter Against the optimum
@art unsat-formula
A random assignment is a seven eighths approximation, and that ratio is to the optimum, not to m. Take all eight clauses on three variables. Every assignment falsifies exactly one, so every assignment satisfies seven, and the optimum is seven. The mean is also seven. So the ratio against the optimum is one, while against m it would be seven eighths.

@words text="8 clauses, 5 variables" sub="mean 7 · optimum 8 · 9 of 32 below the mean"
And here's the shape the guarantee is really about. Eight clauses on five variables: the mean is seven, the optimum is eight, and nine of the thirty two assignments do worse than the mean. The gap is what an algorithm has to close.

@chapter Where people slip
@list heading="Common slips" items="Treating the existence proof as an algorithm@The first|Reaching for independence@The second|Dividing the mean by m@And the third"
The first slip is treating the existence proof as an algorithm. The lab has to enumerate every assignment to name one. The second is reaching for independence. Linearity never needs it. And the third is dividing the mean by m to get a ratio, when a ratio is defined against the optimum.

@end text="An average proves existence"
Type your own formula and see every assignment, on Learn. That's learn dot get er done dot I O.
