---
format: long
lesson: discrete-probability/conditional-probability
title: Conditional probability: shrink the sample space
thumb: Now B is the whole world
---

@chapter The idea
@title text="Conditional Probability" sub="Discrete Probability" art=thumb
You learn something. The die you can't see came up even, or the first card was an ace. How should your probabilities change? Conditional probability answers that, and it isn't a new axiom. It's the same counting, restricted to what you now know.

@math heading="Conditional probability" items="P(A | B) = P(A ∩ B) / P(B)@divided by;;P(B) > 0@greater than zero"
The probability of A given B is the probability of A and B, divided by the probability of B. It only makes sense when the probability of B is greater than zero.

@art shrink-space
In the equally likely model, you can see exactly what's happening. The sizes of S cancel, and you're left with the size of A and B over the size of B. The outcomes outside B have been thrown away. B is now the sample space.

@math heading="Equally likely" items="P(A | B) = |A ∩ B| / |B|@over the size of B"
So count the outcomes of A that lie in B, over the size of B. And for a fixed B, this function obeys all three axioms, so every theorem about probability holds for conditional probability too.

@chapter The multiplication rule
@art chain-steps
Turn the definition around and you get the multiplication rule. It's built for things that happen in steps, where each new step is conditioned on everything before it.

@math heading="Multiplication rule" items="P(A ∩ B) = P(A | B) · P(B)@times the probability of B;;P(A₁ ∩ A₂ ∩ A₃) = P(A₁) P(A₂ | A₁) P(A₃ | A₁ ∩ A₂)@it chains"
The probability of A and B is the probability of A given B, times the probability of B. You could equally condition the other way round. And for three events, it chains: A one, then A two given A one, then A three given both.

@chapter Two aces
@art card-draws
Draw two cards from a deck, without replacement. What's the chance both are aces? The first draw changes the deck, and conditioning is exactly how you handle that.

@math heading="P(both aces)" items="= P(first ace) · P(second ace | first ace)@the first is an ace;;= (4/52) · (3/51)@four over fifty-two;;= 1/221@one over two hundred"
It's the probability the first is an ace, times the probability the second is an ace given the first was. That's four over fifty-two, times three over fifty-one, which is one over two hundred twenty-one.

@chapter Which way round?
@words text="P(A | B) ≠ P(B | A)" sub="same numerator, different denominators"
Here's the main trap. The probability of A given B is usually a different number from the probability of B given A. Sometimes they happen to agree. With two dice, the chance the sum is seven given the first die is four is one sixth, and the reverse is also one sixth. That's a coincidence of symmetry, not a rule.

@art nested-sets
Now take dogs and mammals. The probability something is a mammal given it's a dog is one. The probability it's a dog given it's a mammal is small. Both share the same numerator. Their denominators differ, and that ratio is exactly how far apart they are.

@chapter Monty Hall
@art three-doors
Three doors, a prize behind one. You pick door one. The host, who knows where the prize is, opens a different door with no prize behind it, say door three, and offers you a switch. Should you take it?

@math heading="You pick door 1" items="prize at 1: host opens 2 or 3, switching loses@prize is behind door one;;prize at 2: host must open 3, switching wins@behind door two;;prize at 3: host must open 2, switching wins@behind door three;;each row 1/3 ⟹ switching wins 2/3@two thirds"
If the prize is behind door one, the host opens either other door, and switching loses. If it's behind door two, he must open door three, and switching wins. If it's behind door three, he must open door two, and switching wins. Each row has probability one third, so switching wins two thirds of the time.

@art host-opens
The step people miss is that the host isn't random. He knows, and he's forced to open a losing door. That constraint is information. If he opened a door at random and it just happened to be empty, the answer would be one half. Same picture, different problem.

@chapter Where people slip
@list heading="Common slips" items="Swapping the two conditionals@Swapping|Forgetting the denominator changed@denominator changed|Ignoring how the information arrived@how the information arrived"
First, swapping the two conditionals. They're different numbers with the same numerator. Second, forgetting the denominator changed. Divide by the size of S instead of B, and you get the probability of A and B, not A given B. Third, ignoring how the information arrived, which is the whole point of Monty Hall.

@chapter Try it
@words text="Two children: P(both boys)?" sub="given at least one boy · given the elder is a boy"
Your turn. A family has two children, with boy boy, boy girl, girl boy and girl girl equally likely. Find the chance both are boys given at least one is a boy. Then find it given the elder is a boy. Same family, different information. Do you get different answers?

@end text="Condition by shrinking the space"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
