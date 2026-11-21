---
format: long
lesson: knowledge-and-evidence/the-preface-paradox
title: The preface paradox: believe every sentence, doubt the book
thumb: Each claim likely, the whole not
---

@chapter The author's preface
@title text="The Preface Paradox" sub="Knowledge and Evidence" art=thumb
An author believes every sentence in her book. And in the preface she writes that errors surely remain. Is she contradicting herself? Or is she just being honest about how books get written? The answer turns on a little arithmetic.

@art checked-claims
She's checked a hundred claims. Each is supported strongly enough to have credence ninety nine hundredths. And the checks are independent: an error in one tells her nothing about another. At a threshold of ninety five hundredths, she accepts every claim. All hundred of them.

@art could-all-be-true
Unlike the lottery, nothing logical ties these claims together. They could all be true. The accepted set is consistent. So the real question is how likely it is that they are all true.

@chapter Multiply
@math heading="Independent claims multiply" items="P(A ∧ B) = P(A) · P(B)@the product;;P(all 100 true) = (99/100)¹⁰⁰ ≈ 0.37@to the power of a hundred"
Claims are independent when the probability of two together is the product of their separate probabilities, and likewise for any number. So the probability that all hundred are true is ninety nine hundredths, to the power of a hundred. That's about nought point three seven.

@art product-shrink
Watch what the multiplying does. Each claim you add multiplies the product by ninety nine hundredths again, and that can only lower it. No single factor looks dangerous. It's the number of them that does the damage. And raising the threshold changes what's accepted, but it doesn't change the product at all.

@art threshold-gap
That's well under her threshold of ninety five hundredths. So she accepts every claim, and she doesn't accept the claim that all of them are true. That's the preface paradox. She can say she's confident of each sentence, and that some error remains.

@chapter Not the lottery again
@list heading="Two paradoxes" items="Lottery: the conjunction is certainly false@the lottery|Preface: the conjunction is possible, just improbable@the preface"
The two paradoxes differ in kind. In the lottery, closure under conjunction fails because the conjunction is certainly false. In the preface, the conjunction is possible, and merely improbable. The lottery shows a threshold can accept an inconsistent set. The preface shows it can accept a consistent set, and reject the conjunction.

@chapter Long arguments
@art long-chain
This matters outside books. A valid argument preserves truth, not probability. If a conclusion follows from a hundred independent premises, each at ninety nine hundredths, the conclusion is only guaranteed to be as probable as their conjunction, about nought point three seven. A long chain of believable steps can end somewhere that isn't.

@math heading="Shorter books" items="10 claims at 9/10:  (9/10)¹⁰ ≈ 0.35@Ten claims;;100 claims at 1:  1¹⁰⁰ = 1@probability one"
Shorten the book and the effect shrinks. Ten claims at nine tenths give a conjunction of about nought point three five. Milder, but still far below the claims it's made of. It only vanishes at certainty. A hundred claims at probability one have a conjunction of probability one.

@words text="Closure is safe only for certainties."
So closure under conjunction holds for what's certain, and is at risk for everything else. Each claim added to a book, or each premise added to an argument, adds a little chance of error, and the little chances accumulate.

@art shared-source
One caution. These numbers assume independence. Real claims in a book are more often positively related, as when they rest on one source. That raises the probability that all are true, but not to one, and the paradox remains for any set with enough independent risk.

@chapter Where people slip
@list heading="Common slips" items="Thinking she must believe the book is error-free@The first|Treating the preface as the lottery again@The second|Dropping belief in each claim@the third"
The first slip is thinking an author who believes each sentence must believe the book has no errors. The second is treating the preface as the lottery again. They share a failure of closure, and differ in why. And the third is dropping belief in each claim because the whole is doubtful. No sentence has become less probable.

@chapter Try it
@words text="claims at 99/100" sub="how many before the whole falls below 1/2?"
Here's one to try. Each claim is at ninety nine hundredths, and all are independent. How many claims does it take before the probability that all are true falls below a half? Multiply, and find out.

@end text="Add claims, watch the whole fall"
You can change the number of claims, their probability and the threshold, on Learn. That's learn dot get er done dot I O.
