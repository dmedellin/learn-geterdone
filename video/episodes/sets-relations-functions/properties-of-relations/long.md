---
format: long
lesson: sets-relations-functions/properties-of-relations
title: Reflexive, symmetric, antisymmetric, transitive, and closures
thumb: Name the witness
---

@chapter The question
@title text="Properties of Relations" sub="Sets, Relations and Functions" art=thumb
A relation is just a set of pairs. So how do you tell one relation from another in a useful way? You ask four yes or no questions about it, and each one is a sentence you can check.

@art diagonal-loops
Reflexive: every element is related to itself. Every a has the pair a, a. And that means every element of the set, including ones that appear in no other pair.

@art two-way-arrows
Symmetric: whenever a is related to b, b is related to a. Every arrow has a matching arrow coming back.

@art one-way-arrows
Antisymmetric: if a is related to b and b is related to a, then a equals b. Distinct elements never relate both ways. Loops are fine.

@art triangle-shortcut
And transitive: if a is related to b, and b to c, then a is related to c. Every two step path has a one step shortcut.

@chapter Antisymmetric is not not symmetric
@math items="= : symmetric and antisymmetric@equality;;{(1,2), (2,1), (1,3)} : neither@one, two"
Here's the trap. Antisymmetric is not the negation of symmetric. Equality is both. And the relation one, two, then two, one, then one, three is neither: it has a two way pair, so it's not antisymmetric, and one, three has no reverse, so it's not symmetric.

@list heading="Familiar relations" items="≤ : reflexive, antisymmetric, transitive@less than or equal|< : antisymmetric, transitive@strictly less|a − b even : reflexive, symmetric, transitive@a minus b is even"
Some familiar ones. Less than or equal is reflexive, antisymmetric and transitive, but not symmetric. Strictly less than is transitive and antisymmetric, but not reflexive. And a minus b is even is reflexive, symmetric and transitive, but not antisymmetric.

@chapter A worked classification
@math heading="a divides b, on {1, 2, 3, 4, 6}" items="reflexive: a | a  ✓@a divides a;;symmetric: 2 | 4 but 4 ∤ 2  ✗@two divides four;;antisymmetric: a | b and b | a ⟹ a = b  ✓@for positive numbers;;transitive: a | b and b | c ⟹ a | c  ✓@a divides c"
Take divides, on one, two, three, four, six. Reflexive? Yes: a divides a. Symmetric? No: two divides four, but four doesn't divide two. That pair is the witness. Antisymmetric? Yes, for positive numbers. Transitive? Yes: if a divides b and b divides c, then a divides c.

@art divides-diagram
Reflexive, antisymmetric and transitive together make a partial order, which is the next lesson but one. And it really is only partial. Two and three are incomparable: neither divides the other, so not every pair of elements gets ranked.

@words text="2 | −2  and  −2 | 2" sub="antisymmetry fails over ℤ"
That antisymmetry used positivity. Over all the integers, two divides minus two and minus two divides two, yet two isn't minus two. A property depends on the set the relation lives on.

@chapter Closures
@art closure-fill
Now suppose a relation is missing a property. The closure is the smallest relation containing yours that has it. Not any repair that works: the least you can add.

@list heading="Three closures" items="Reflexive: add the diagonal@reflexive closure|Symmetric: add every reverse@symmetric closure|Transitive: add every path@transitive closure"
The reflexive closure adds the diagonal. The symmetric closure adds every reverse pair, so it's R union its inverse. And the transitive closure adds every path: R union R squared union R cubed, and so on.

@words text="R ∪ R² ∪ … ∪ Rⁿ"
Its pairs are exactly the ones joined by a path of one or more steps. On an n element set, the union stops at the n th power, because a longer path repeats a vertex and can be shortened. Warshall's algorithm finds the closure in n cubed steps, without computing the powers.

@words text="No antisymmetric closure"
There's no antisymmetric closure. Adding pairs can never remove a violation, so a closure only exists for properties that adding pairs can establish.

@chapter Where people slip
@list heading="Common slips" items="Reading antisymmetric as not symmetric@The first|Checking loops only on elements in pairs@The second|Stopping the transitivity check early@the third"
The first slip is reading antisymmetric as not symmetric. They're independent. The second is checking reflexivity only on elements that show up in pairs. An element in no pair at all is exactly what breaks it. And the third is stopping the transitivity check early. Every two step path counts, including ones through loops.

@chapter Try it
@words text="=   ≤   <   ⊆   same remainder mod 3"
Your turn. For equals, less than or equal, less than, subset, and has the same remainder mod three, say which of the four properties hold. For every failure, name the specific pair or triple. Naming the witness is the check.

@end text="Check properties, then close"
You can check every property of a relation, and see its closures in colour, on Learn. That's learn dot get er done dot I O.
