---
format: long
lesson: intractability-and-approximation/what-the-solution-map-preserves
title: One more clause, and a reduction becomes onto
thumb: The instance changed, not the map
---

@chapter Same construction, one more clause
@title text="What the Solution Map Preserves" sub="Intractability and Approximation" art=thumb
Last time, the map from independent sets back to assignments missed one model. Add one clause to the formula, and it misses nothing. The reduction didn't change. The instance did.

@math heading="Three clauses" items="(x₁ ∨ x₂ ∨ ¬x₃) ∧ (¬x₁ ∨ x₂ ∨ x₃) ∧ (x₁ ∨ ¬x₂ ∨ x₃)@the formula;;9 vertices,  k = 3@nine vertices"
Here's the formula: last lesson's two clauses, plus x one or not x two or x three. Three literal occurrences per clause gives nine vertices, and the target is k equals three.

@chapter Count the edges
@math heading="15 edges" items="triangles:  3 × 3 = 9@three clauses;;x₁ – ¬x₁:  1 + 1@x one;;x₂ – ¬x₂:  2@x two;;¬x₃ – x₃:  2@x three;;total 15@fifteen"
Don't take the picture on trust. Count. Three clauses times three triangle edges is nine. Then contradictions: x one in the first clause against not x one, and again from the third clause, two. x two's two occurrences against not x two, two more. And not x three against x three's two occurrences, two. Fifteen in all.

@chapter Three verdicts
@list heading="For the map back" items="Sound: every image really is a solution@Sound means|Injective: no two solutions share an image@injective means|Onto: every original solution is an image@onto means"
First, the words. For the map carrying each solution back, sound means every image really is a solution of the original. Injective means no two solutions share an image. Onto means every original solution is an image. All three together make a bijection, and a reduction requires none of them.

@art edge-count
The panel reports twelve independent sets of size three, and five satisfying assignments. Then it gives its three verdicts on the map back from sets to assignments.

@list heading="On three clauses" items="Sound: yes@Sound|Injective: no, three sets each on 110, 101 and 011@Injective|Onto: yes, the verdict that moved@Onto"
Sound: yes, as before, and as proved. Injective: no, as before. Three sets each land on one one zero, one zero one, and zero one one. Two land on one one one, and one on zero zero zero. Onto: yes.

@art map-arrows
Every one of the five models is now reached by at least one arrow. That's the verdict that's moved.

@chapter Why it moved
@art three-picks
On two clauses, all true had no preimage, because two chosen literals can't make three variables true. Now take x two from the first clause, x three from the second, and x one from the third. They're in different clauses, and none contradict. That set names all three variables positively, so all true is now an image.

@art two-vs-three
Nothing was fixed. The budget grew. With m clauses, m literals are chosen, so at most m variables can be named, and the rest are left false.

@words text="on this formula, the induced map is onto"
So the careful sentence is: on this formula, the induced map is onto. The shorter sentence, the reduction is onto, reads better and is wrong. Only one survives trying a different instance, and the panel makes that one click.

@chapter Three kinds of verdict
@list heading="Same style, different status" items="Sound: a theorem, being regression-tested@a theorem|Not injective: a structural cause, true in general@structural cause|Onto: a measurement, either way@a measurement"
Here's the subtle part. Soundness is a theorem, proved for every formula. The twelve checks test the implementation. Not injective has a structural cause: a clause with two true literals always offers more than one witness. Every model of a formula with such a clause has several preimages, so not injective in general is defensible. And onto is a measurement, which can go either way.

@art same-panel
All three are printed in the same style, by the same routine, in the same panel. The lab can't tell you which is which. The proof can.

@words text="satisfiable  ⟺  independent set of size m"
What survives every instance is just the yes or no answer. Everything else is a fact about this pair of instances. And a map that isn't a bijection isn't defective. A reduction that was one would be stronger, useful for counting solutions, say. This one simply isn't.

@art instance-swap
Both formulas are defaults in the same control. Whichever is on screen when you read the verdict becomes, if you aren't careful, the verdict for the reduction.

@chapter Where people slip
@list heading="Common slips" items="Generalising from the loaded instance@The first|Treating all verdicts as one kind@The second|Calling a non-bijection defective@And the third"
The first slip is generalising from whatever instance happened to be loaded. Write the instance into the sentence. The second is treating all three verdicts as the same kind of fact. And the third is concluding that a reduction that isn't a bijection is broken.

@end text="The instance changed, not the map"
Switch between the two formulas and watch one verdict flip, on Learn. That's learn dot get er done dot I O.
