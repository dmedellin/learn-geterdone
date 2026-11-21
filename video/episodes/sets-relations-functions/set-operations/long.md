---
format: long
lesson: sets-relations-functions/set-operations
title: Union, intersection, difference: set operations are logic
thumb: Or, and, not, for sets
---

@chapter The idea
@title text="Set Operations" sub="Sets, Relations and Functions" art=thumb
There are five ways to combine sets that you'll use constantly. Here's the good news: you already know all of them, because each one is a logical connective in disguise.

@art venn-union
Start with union. A union B is everything in A or in B. It's an inclusive or, so an element in both is in the union, once. A set has no multiplicities.

@art venn-intersection
Intersection is the and. A intersect B is everything that's in A and in B, the overlap. When two sets have nothing in common, their intersection is empty, and we call them disjoint.

@math heading="Union and intersection" items="A ∪ B = {x : x ∈ A ∨ x ∈ B}@in A or in B;;A ∩ B = {x : x ∈ A ∧ x ∈ B}@in A and in B"
So union is the set of x in A or in B, and intersection is the set of x in A and in B.

@chapter Difference and complement
@art venn-difference
The difference, A minus B, keeps what's in A and not in B. That's an and with a not inside it.

@art universe-box
The complement of A is everything not in A. But everything has to mean something. The complement only makes sense relative to a universal set, U, that contains everything under discussion. The complement of the even numbers is different inside the integers and inside the reals.

@math items="A \ B = {x : x ∈ A ∧ x ∉ B}@A minus B;;Ā = U \ A = {x ∈ U : x ∉ A}@the complement"
So A minus B is the x in A and not in B. And the complement of A is U minus A: the x in U that are not in A.

@chapter Symmetric difference
@art venn-symmetric
The fifth operation is symmetric difference: the elements in exactly one of the two sets. It's the exclusive or. You can build it as A minus B, together with B minus A.

@math heading="A = {1, 2, 3},  B = {3, 4}" items="A \ B = {1, 2}@A minus B;;B \ A = {4}@B minus A;;A △ B = {1, 2, 4}@their union;;A ∩ B = {3}@three, is exactly"
Take A as one, two, three and B as three, four. A minus B is one, two. B minus A is just four. So difference isn't symmetric. Their union, one, two, four, is the symmetric difference. And the intersection, three, is exactly what it leaves out.

@chapter The correspondence with logic
@list heading="Sets ↔ logic" items="∪ is ∨@union is or|∩ is ∧@intersection is and|complement is ¬@complement is not|△ is ⊕@exclusive or|⊆ is →@subset is"
Line them up. Union is or. Intersection is and. Complement is not. Symmetric difference is exclusive or. And subset is implication. This isn't an analogy. Every set identity is a logical equivalence, applied to membership.

@chapter Counting a union
@math heading="Inclusion-exclusion" items="|A ∪ B| = |A| + |B| − |A ∩ B|@the size of A union B;;7 + 5 − 2 = 10@seven plus five"
How big is a union? Add the sizes, and you count every element of the overlap twice. So subtract the overlap once. The size of A union B is the size of A plus the size of B, minus the size of their intersection. If A has seven, B has five, and they share two, that's seven plus five minus two: ten.

@art double-count
Just adding the sizes only works when the sets are disjoint. Otherwise the shared elements are counted twice.

@chapter A worked expression
@math heading="U = {1,…,8}  A = {1,2,3,4}  B = {3,4,5,6}  C = {4,6,8}" items="A \ B = {1, 2}@A minus B;;B ∩ C = {4, 6}@B intersect C;;(A \ B) ∪ (B ∩ C) = {1, 2, 4, 6}@the union"
Now evaluate A minus B, union B intersect C. A is one to four, B is three to six, C is four, six, eight. A minus B is one, two. B intersect C is four, six. So the union is one, two, four, six.

@words text="4 ∉ A \ B,  but  4 ∈ B ∩ C"
Check element four. It's in A and in B, so it's not in A minus B. But it's in B and in C, so it's in the second term. Checking single elements is how you catch a misplaced bracket.

@chapter Where people slip
@list heading="Common slips" items="Assuming A \ B = B \ A@The first|Adding sizes without subtracting the overlap@The second|Complementing without a universe@the third"
The first slip is assuming A minus B equals B minus A. They're different sets. The second is adding sizes without subtracting the overlap. And the third is taking a complement without a stated universe, which leaves the expression incomplete.

@chapter Try it
@words text="(A △ B) \ C" sub="write the membership condition"
Your turn. Take the symmetric difference of A and B, minus C, and write the condition for x to belong. If you get x in A exclusive or x in B, and x not in C, then the rest of set algebra is logic in different symbols.

@end text="Evaluate any expression"
You can evaluate any set expression on twelve elements, and compare two side by side, on Learn. That's learn dot get er done dot I O.
