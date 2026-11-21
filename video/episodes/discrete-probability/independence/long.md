---
format: long
lesson: discrete-probability/independence
title: Independence is an equation, not a story
thumb: Check the product
---

@chapter The idea
@title text="Independence" sub="Discrete Probability" art=thumb
When are two events independent? The tempting answer is a story: they don't affect each other, they happen in different places. But in probability, independence is an equation. And checking it means checking that equation.

@math heading="Independent events" items="P(A ∩ B) = P(A) · P(B)@times;;P(A | B) = P(A)   when P(B) > 0@conditioning on B"
A and B are independent when the probability of A and B equals the probability of A times the probability of B. Equivalently, when P of B is positive, P of A given B equals P of A. Conditioning on B changes nothing.

@art product-area
The second form is the meaning, and the first is the test. The product form is the official definition, because it's symmetric in A and B, and it doesn't need P of B to be positive.

@chapter Two dice
@art dice-columns
Roll two dice. Let A be the first die is even, and B be the second die is five. P of A is one half, P of B is one sixth, and A and B together is three outcomes out of thirty-six.

@math heading="First even, second is 5" items="P(A) = 1/2,  P(B) = 1/6@one half;;P(A ∩ B) = 3/36 = 1/12@three over thirty-six;;= (1/2)(1/6)  ✓ independent@independent"
P of A is one half, and P of B is one sixth. P of A and B is three over thirty-six, which is one twelfth. That's one half times one sixth, so they're independent. No surprise there.

@math heading="First even, sum is 7" items="P(A) = 1/2,  P(B) = 1/6@one half;;A ∩ B = {(2,5), (4,3), (6,1)}@two, five;;P(A ∩ B) = 3/36 = 1/12 = (1/2)(1/6)  ✓@one twelfth"
Now keep A, and let B be the sum is seven. Again P of A is one half and P of B is one sixth. A and B together is two, five, then four, three, then six, one. That's three thirty-sixths, one twelfth. Independent again!

@words text="The numbers decide"
And that's even though the sum obviously depends on the first die. Nothing in the physical description suggests independence. The numbers satisfy the equation, and that's what independence means.

@chapter Complements
@art complement-square
If A and B are independent, so are A and not B, not A and B, and not A and not B. Here's the first one.

@math heading="A and not B" items="P(A ∩ B̄) = P(A) − P(A ∩ B)@minus;;= P(A) − P(A) P(B)@times P of B;;= P(A)(1 − P(B))@one minus;;= P(A) P(B̄)  ✓@not B"
P of A and not B is P of A minus P of A and B. That's P of A minus P of A times P of B. Factor out P of A to get P of A times one minus P of B, which is P of A times P of not B.

@chapter Disjoint is not independent
@art disjoint-apart
Now a trap. If A and B are disjoint and both have positive probability, then P of A and B is zero, but P of A times P of B is positive. So they're dependent. Knowing B happened tells you A didn't, and that's a big change in what you know.

@math heading="Union of independent events" items="P(A ∪ B) = P(A) + P(B) − P(A)P(B)@inclusion and exclusion"
The only way to be both disjoint and independent is for one event to have probability zero. And for independent events, the union isn't the sum. Use inclusion and exclusion, with the product in place of the intersection.

@chapter Pairwise is not mutual
@art two-coins
For many events, mutual independence means every subset of them has the product rule, not just every pair. Flip two fair coins. A is first is heads, B is second is heads, and C is the two agree.

@math heading="Two fair coins" items="P(A) = P(B) = P(C) = 1/2@one half;;P(A ∩ C) = P(HH) = 1/4 = (1/2)(1/2)  ✓@each pair;;P(A ∩ B ∩ C) = P(HH) = 1/4@all three;;P(A)P(B)P(C) = 1/8  ✗@one eighth"
Each has probability one half, and each pair is independent. For example, P of A and C is the chance of two heads, one quarter, which is one half times one half. But P of all three is also the chance of two heads, one quarter, while the product is one eighth.

@art triangle-links
Any two of these events determine the third completely. So they can't be mutually independent, and checking only pairs gives the wrong conclusion.

@chapter Where people slip
@list heading="Common slips" items="Confusing independent with disjoint@with disjoint|Inferring independence from the description@from the description|Checking pairs and stopping@pairs and stopping"
First, confusing independent with disjoint. They're close to opposite. Second, inferring independence from the description. Compute the three probabilities and compare. Third, checking pairs and stopping, when mutual independence needs every subset.

@chapter Try it
@words text="First die even · at least one 6" sub="compare P(A ∩ B) with P(A)P(B)"
Your turn. Keep A as the first die is even, and let B be at least one six. Count the pairs in B, and in A and B, then compare P of A and B with the product. Are these two independent? And which way does knowing B push A?

@end text="Independence: check the product"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
