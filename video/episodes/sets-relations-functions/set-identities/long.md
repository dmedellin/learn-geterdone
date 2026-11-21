---
format: long
lesson: sets-relations-functions/set-identities
title: Set identities: De Morgan's laws and how to prove them
thumb: Name every step
---

@chapter The idea
@title text="Set Identities and Proofs" sub="Sets, Relations and Functions" art=thumb
Set algebra comes with a long list of laws. That sounds like a lot to memorise, but it isn't, because you've seen every one of them before, in logic.

@art mirror-laws
Put each set law beside its logical equivalence and the match is exact. Union for or, intersection for and, complement for not, the universe for true, and the empty set for false.

@math heading="A few of the laws" items="A ∪ ∅ = A    A ∩ U = A@identity;;A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)@distributive;;A ∪ (A ∩ B) = A@absorption;;A \ B = A ∩ B̄@difference"
Here are a few. Identity: A union the empty set is A. The distributive law. Absorption: A union A intersect B is just A. And the difference law: A minus B is A intersect the complement of B. That last one is the most useful, because it removes the minus sign and leaves only operations the other laws talk about.

@chapter De Morgan
@art de-morgan-venn
The most famous pair is De Morgan. The complement of A union B is the complement of A, intersect the complement of B. Not being in either set means missing both.

@math heading="De Morgan" items="(A ∪ B)‾ = Ā ∩ B̄@A union B;;(A ∩ B)‾ = Ā ∪ B̄@A intersect B"
So the complement of A union B is the intersection of the complements. And the complement of A intersect B is the union of the complements. The complement passes inward, and the operation flips.

@chapter Proof by double inclusion
@math heading="(A ∪ B)‾ ⊆ Ā ∩ B̄" items="x ∈ (A ∪ B)‾  ⟹  x ∉ A ∪ B@Let x be;;not (x ∈ A or x ∈ B)@it is not the case;;x ∉ A and x ∉ B@x is not in A;;x ∈ Ā ∩ B̄@so x is in"
Here's the proof. Let x be in the complement of A union B. Then x is not in A union B, so it is not the case that x is in A or x is in B. By De Morgan for propositions, x is not in A and x is not in B. So x is in the intersection of the complements.

@art two-way
The other direction is the same steps read backwards, because every step was an if and only if. When that happens you can write one chain of equivalences instead of two inclusions, but only if every step really is reversible.

@chapter A chain of laws
@math heading="A \ (B ∪ C)" items="= A ∩ (B ∪ C)‾@difference law;;= A ∩ (B̄ ∩ C̄)@De Morgan;;= (A ∩ A) ∩ (B̄ ∩ C̄)@idempotent;;= (A ∩ B̄) ∩ (A ∩ C̄)@commutative and associative;;= (A \ B) ∩ (A \ C)@twice"
The second route is a chain of named laws. Prove that A minus B union C equals A minus B, intersect A minus C. Apply the difference law. Then De Morgan. Then idempotent, backwards. Then commutative and associative. And the difference law, twice.

@art chain-links
Step three looks like a trick. Replacing A with A intersect A is legal because idempotence is an equality, and you can use it in either direction. It's what lets one A be shared between two factors. Every line names its law, so a step you can't name is a step you haven't made.

@chapter Why a Venn diagram isn't enough
@art three-circle-venn
What about Venn diagrams? Three circles make eight regions, which is every possible membership pattern for three sets. So a correctly shaded three set diagram really does check a three set identity.

@art four-circle-gap
But it doesn't generalise. The usual four circle picture is missing regions, so it isn't a case check at all, and there's no readable diagram for five sets. A diagram helps you see what's true. The proof is still owed.

@chapter Which route?
@list heading="Choosing a method" items="Two or three operations: chain the laws@two or three operations|Anything unfamiliar: double inclusion@anything unfamiliar|To refute: find one element@to refute"
So which route do you take? With two or three operations, chain the laws, rewriting minus as intersect a complement first. For anything unfamiliar, use double inclusion. It always works and needs no recall. And to refute an identity, find one element that's in one side and not the other. One is enough.

@chapter Where people slip
@list heading="Common slips" items="Complementing without flipping the operation@The first|Treating a Venn diagram as a proof for many sets@The second|Using a step you cannot name@the third"
The first slip is distributing a complement without flipping the operation. The complement of A union B is not the complement of A union the complement of B. The second is treating a Venn diagram as a proof for any number of sets. And the third is using a step you cannot name. Rearranging is where errors hide.

@chapter Try it
@words text="(A \ B) ∪ (B \ A) = (A ∪ B) \ (A ∩ B)" sub="once each way"
Your turn. Both sides of this are the symmetric difference. Prove they're equal twice: once by double inclusion, and once by a chain of laws. The chain will be shorter. Double inclusion is the one you can always produce.

@end text="Try to break an identity"
You can try to break an identity, element by element, and watch the wrong De Morgan fall apart, on Learn. That's learn dot get er done dot I O.
